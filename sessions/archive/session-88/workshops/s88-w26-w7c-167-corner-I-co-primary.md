# Session 88 Workshop W-26: connes x lizzi

**Date**: 2026-05-08
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: connes (connes-ncg-theorist), lizzi (lizzi-spectral-functional-theorist)
**Source Documents**:
- `sessions/archive/session-88/session-88-w7c-workingpaper.md`
- `sessions/session-plan/session-88-plan-w7c.md`
- `sessions/archive/session-88/workshops/_seed-w7c.md`
- `sessions/permanent-results-registry.md`
- `.claude/rules/cross-pillar-bridge-anatomy.md`

**Focus Topics** (per schedule §W-26 invocation):

1. **(a) Parse-tree decision capture vs FI/RD axis**: Does §VII.U.2 clause (e) parse-tree decision (no π(a) refs ⇒ INVARIANT) correctly capture ALL algebra-axis-DEPENDENT functionals, or does it miss the FI/RD regulator-dressing axis?
2. **(b) xi²_0(R) FI vs RD classification**: Is `xi²_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3)` an FI quantity (ratio cancels regulator-class-dependence) or RD (M_R(s=3) numerator regulator-class-dependent; off-F_2 classes retain residue)? At obs1 xi_per_class = [13.642, 13.642, 9.578, 2.748, 13.327].
3. **(c) §VII.AH narrowing trigger**: If ANCHOR-2 is RD-not-FI, does it inhabit Corner-III (DEPENDENT × s=3) and trigger CROSS-corner FORBIDDEN co-primary per §VII.U.2 clause (f)?
4. **(d) FI/RD trichotomy refinement**: Does FI/RD refine algebra-INVARIANT/algebra-DEPENDENT into a 3-class partition (INVARIANT-FI / INVARIANT-RD-via-regulator-dressing / DEPENDENT)?

**Cross-cutting**: relationship between connes's parse-tree decision procedure (algebra-INVARIANT family per `cross-pillar-bridge-anatomy.md`) and lizzi's FI/RD trichotomy (per S82 W-3 RULE-3) — orthogonal, refining, or equivalent?

---

## Round 1 — connes: Opening Analysis

### C1: Parse-tree decision procedure capture (clause a)

**Position**: §VII.U.2 clause (e) parse-tree decision procedure (PARSE_TREE_DECISION(F): no `π(a)` refs ⇒ INVARIANT; any `π(a)` or `[D, π(a)]` ref ⇒ DEPENDENT) IS the operative discriminator for the algebra-INVARIANT vs algebra-DEPENDENT family at the registry-anchor level. The discriminator is BY CONSTRUCTION the operator-algebraic test that the algebra-axis K-counter (MANDATORY-K=3 per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, lines 272-280) was promoted on. Numerical class-dependence in the laboratory-IN evaluation (regulator-class-dependent multiplier residues, FI/RD shading) is a STRUCTURALLY ORTHOGONAL layer property, not an extension of the algebra-INVARIANT/DEPENDENT axis.

**Substitution chain — why parse-tree IS the operative discriminator at the algebra-axis layer**:

```
Definitions (per §VII.U.2 + Connes-Moscovici 1995 §III.4 + Connes 1996 reconstruction):
  algebra-INVARIANT family      F_inv  := { F : F(λ_k, m_k) = Σ_k m_k g(λ_k), g measurable }
  algebra-DEPENDENT family      F_dep  := { F : F = ‖[D, π(a)]‖_op + convex hull / sup }
  parse-tree predicate          PT(F)  := no π(a) symbol in symbolic AST of F
                                          ⇒ INVARIANT
                                          else DEPENDENT
  π(a) lift                     λ : A → B(H), a → π(a) (NCG axiom 1, faithful *-rep)
  spectral-projector calculus   {f(D²) : f measurable}'' ⊆ Z({D, γ}'')
                                (Borel functional calculus on D²)

Substitutions:
  Step 1: F ∈ F_inv  ⇒ F lives in {f(D²)}'' ⊆ Z({D, γ}'') (Borel-functional calculus)
                     ⇒ F's symbolic form contains only λ_k, m_k, g(·) — no π(a) lift
                     ⇒ PT(F) = INVARIANT.   ✓

  Step 2: F ∈ F_dep  ⇒ F = ‖[D, π(a)]‖_op for some a ∈ A
                     ⇒ F's symbolic form contains the π(a) lift explicitly
                     ⇒ PT(F) = DEPENDENT.   ✓

  Step 3: chirality-vs-A_F block-grading mismatch (§VII.U.2 clause (c) Step 7):
                     {f(D²)} ∩ π(A_F) = ℂ · 1_{H_F}  (NCG axiom 5 + Poincaré duality)
                     ⇒ the two families share ONLY scalars; no closed-form
                       {λ_n}-only identity reproduces a state-pair functional.

Simplification:
  PT(F) is a finite, decidable, regulator-INDEPENDENT classification at the
  symbolic-form level (clause (e) "operates at parse-tree level, NOT at numerical
  evaluation level" — registry lines 12930-12930). The decision procedure is
  the substrate-IS algebra-axis test BY CONSTRUCTION: the algebra A enters
  ONLY through π(a) lifts (axiom 1), and the spectral projector calculus on
  D² is what produces the F_inv side.

Direction:
  At the algebra-INVARIANT/DEPENDENT axis, parse-tree IS the canonical test.
  Per §VII.U.2 clause (e) the test is regulator-INDEPENDENT — same
  classification under ζ, Pauli-Villars, Mellin, cutoff. Numerical class-
  dependence (FI/RD shading) lives on a DIFFERENT axis (UV-regulator
  evaluation layer) and does NOT change the algebra-axis classification.

Conclusion:
  Parse-tree captures ALL algebra-axis-DEPENDENT functionals BY DEFINITION
  of the algebra-axis K-counter. lizzi's FI/RD trichotomy operates at the
  numerical-evaluation layer (a DOWNSTREAM layer per the layer-functor F
  framing of `epistemic-discipline.md §"Layer-Decomposition"`); it is NOT
  a refinement of the algebra-axis classification, but an orthogonal axis
  governing how regulator-class evaluation produces numerical residues.
```

**Why "FI/RD captures regulator-dressing" is not a counterexample to parse-tree completeness**:

The S82 W-3 RULE-3 mnemonic-vs-exact-ratio rule (`math-scripts.md §"Mnemonic-vs-exact ratio discipline"`) introduces FI/RD as a discipline on numerical citation: "FI = ratios are observables; absolute moments are regulator-dressed." This is an evaluation-layer property: a quantity computed on a substrate spectral triple `(A_K, H_K, D_K)` may evaluate to numerically class-dependent values across `R ∈ A_5` even when its symbolic form is purely spectrum-only (no π(a) lift). The S82 rule is a publication-precision discipline, not an algebra-axis re-classification.

This separation is consistent with how the substrate-physics layer interfaces with the methodology layer per `epistemic-discipline.md §"Layer-Decomposition"`:

| Substrate-physics layer (algebra-axis) | UV-evaluation layer (regulator-class) |
|:---------------------------------------|:--------------------------------------|
| F_inv vs F_dep (parse-tree π(a) test)  | FI vs RD (numerical-class residue)    |
| Regulator-INDEPENDENT classification   | Regulator-CLASS-DEPENDENT shading     |
| `{f(D²)}'' ∩ π(A_F) = ℂ · 1`           | M_R(s) varies across R ∈ A_5          |
| MANDATORY-K=3 (S87 W-2 R3)             | S82 W-3 RULE-3 publication discipline |

**Provenance pin**: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` lines 272-280; §VII.U.2 clauses (a), (b), (e) at `permanent-results-registry.md` lines 12913-12915, 12930; §VII.U.2 clause (c) Step 7 axiomatic skeleton at line 12917; Connes-Moscovici 1995 §III.4 dim-spectrum residue formula `a_n = Res[Tr(D^{−2s}); s=(d−n)/2] = Σ_k m_k λ_k^{−(d−n)}` (regulator-INDEPENDENT spectral-moment identity that anchors the F_inv side).

### C2: ANCHOR-2 xi²_0(R) classification under parse-tree (clause b)

**Position**: ANCHOR-2's xi²_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) is **INVARIANT** under §VII.U.2 clause (e) parse-tree decision. Both M_R(s=3) and M_F2(s=3) are spectral-moment Mellin residues (Σ_k m_k λ_k^{−2}-class quantities at substrate-distance-1); the ratio is a quotient of trace-functionals, not an algebra-DEPENDENT functional. xi_E_GGE_inv is a substrate-natural canonical scalar (S86 branch-iv-canonical anchor 59.8 · Δ_BCS / K_base; canonical_constants.py provenance pin). The downstream SR-LO ODE state-trajectory ε(N), η(N) consumes xi²_0(R) as an initial condition (real-valued IC, not an operator-algebra commutator). PT classification stands as INVARIANT.

**Substitution chain — parse-tree classification of xi²_0(R)**:

```
Definitions (per §VII.AH ANCHOR-2 specification, registry lines 15418, 15425):
  xi^2_0(R)        := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3)
  xi_E_GGE_inv     := canonical scalar (S86 branch-iv-canonical anchor;
                       59.8 · Δ_BCS / K_base; substrate-natural pin
                       canonical_constants.py value 13.642473425595973;
                       NO π(a) reference)
  M_R(s=3)         := Res[Tr_R(D_K^{-2s}); s=3] under regulator class R
                       (Mellin residue at substrate-distance-1 pole;
                       parse-tree symbolic form: Σ_k m_k λ_k^{-2} g_R(λ_k);
                       NO π(a) reference)
  M_F2(s=3)        := M_R(s=3) at R = ζ-class (F_2-class normalizer;
                       same parse-tree symbolic form;
                       NO π(a) reference)
  PARSE_TREE_DECISION (clause (e), registry line 12930):
                     no π(a) refs in symbolic AST  ⇒ INVARIANT
                     any π(a) or [D, π(a)] ref      ⇒ DEPENDENT

Substitutions:
  Step 1 (numerator):
    M_R(s=3) parse-tree = { Tr, D_K^{-2s}-functional-calculus, Mellin
                            residue extraction at s=3 }
    π(a) symbol count = 0
    ⇒ PT(M_R(s=3)) = INVARIANT.

  Step 2 (denominator):
    M_F2(s=3) parse-tree identical to numerator at R = ζ.
    π(a) symbol count = 0
    ⇒ PT(M_F2(s=3)) = INVARIANT.

  Step 3 (canonical-scalar prefactor):
    xi_E_GGE_inv parse-tree = real-valued canonical pin
    π(a) symbol count = 0
    ⇒ PT(xi_E_GGE_inv) = INVARIANT (trivial; constant scalar).

  Step 4 (ratio composition):
    xi^2_0(R) parse-tree = (constant) · (Mellin-residue-trace) /
                            (Mellin-residue-trace)
    π(a) symbol count in composite AST = 0 + 0 + 0 = 0
    ⇒ PT(xi^2_0(R)) = INVARIANT.

  Step 5 (downstream SR-LO ODE consumption — clause (b)):
    SR-LO ODE: dε/dN = f(ε, η; xi^2_0(R)),  dη/dN = g(ε, η; xi^2_0(R))
    state trajectory (ε(N), η(N)) ∈ ℝ²
    ε, η are real-valued slow-roll parameters; no π(a) lift in the ODE.
    ⇒ PT(N_breakdown(R)) = INVARIANT (state ODE on real parameters).

Simplification:
  At every level of the symbolic AST — numerator, denominator, prefactor,
  ratio composition, downstream ODE — the π(a) symbol count is ZERO.

Direction:
  PT(xi^2_0(R)) = INVARIANT.   POLE = s=3 (Corrigendum 2 scoping).
  ⇒ Corner_cell(ANCHOR-2) = I = (INVARIANT, s=3).
```

**Sage exact verification of the F_2-class cancellation structure** (consumed by W7c-167 obs1 substantiation):

Symbolic form: `xi^2_0(R) / xi_E_GGE_inv = M_R(s=3) / M_F2(s=3)`. With M_R = (M_ζ, M_Zubarev, M_SDW, M_cutoff_sqrt, M_anomaly) at substrate-distance-1 from §VII.AH ANCHOR-1 calibration (W4-2 P5; registry line 15417):

| Class R | M_R/M_F2 (Sage QQ exact) | xi²_0(R) at xi_E = 13.642473 |
|:--------|:-------------------------|:------------------------------|
| ζ (F_2) | 1581/1581 = 1            | 13.642473 (F_2 cancellation EXACT) |
| Zubarev | 1201/15810 = 0.075965    | 1.036345 (suppression class)  |
| SDW (F_2) | 1581/1581 = 1          | 13.642473 (F_2 cancellation EXACT) |
| cutoff_sqrt | 1110/1581 = 0.702087 | 9.578207 (truncation class)   |
| anomaly | 3185/15810 = 0.201455    | 2.748341 (subtraction class)  |

Within-F_2 cancellation residual (M_ζ/M_F2 − M_SDW/M_F2) = **0 EXACT** (Sage QQ); off-F_2 classes carry CLASS-DEPENDENT numerical residues.

**Why the off-F_2 numerical class-dependence does NOT make ANCHOR-2 algebra-DEPENDENT**:

The numerical class-dependence is the Mellin-multiplier residue M_R(s=3) varying across R ∈ A_5 — exactly the type-(a) algebra-INVARIANT family quantity per §VII.U.2 clause (a), registry line 12913 ("Seeley-DeWitt moments `a_n^{regulator}`, ζ-residues `Res[Tr(D^{−2s}); s=(d−n)/2]`, Mellin-Dirichlet identities, and heat-kernel zeta-traces"). All five entries in the §VII.U.2 clause-(a) calibration corpus are regulator-class-tagged Seeley-DeWitt coefficients per `regulator-pin-discipline.md`; their numerical value is regulator-class-dependent BY CONSTRUCTION (the regulator-pin tagging discipline EXISTS because of this) — yet they remain algebra-INVARIANT because the regulator-class is NOT a π(a) operator-algebra reference. The same logic applies to xi²_0(R): regulator-class-dependence at the numerical-evaluation layer ≠ algebra-axis-DEPENDENT at the symbolic-form layer.

**The numerical xi_per_class = [13.642, 13.642, 9.578, 2.748, 13.327] from obs1 npz**:

The workshop seed (line 16) cites `xi_per_class = [13.642, 13.642, 9.578, 2.748, 13.327]` from `s87_w7_ic_per_class_verify.npz`. This 5-tuple is computed at s=−1 (per WP §W7c-167 obs1 line 693: `s_slot = -1`), NOT s=3. The observable-1 substantiation at s=−1 evaluates the F_2 identity at a DIFFERENT substrate-distance pole than §VII.AH's registered s=3 anchor; the F_2 identity is preserved across pole transition per the structural reading (W7c WP line 730 verbatim). The discrepancy between Sage's s=3 prediction (Zubarev 1.036) and obs1's s=−1 value (Zubarev 13.327) is a pole-transition artifact, NOT an inconsistency: per W-9 RULE-3 Pole-Scope sub-clause (MANDATORY at K=4 per S88 W7a-72), each pole has its own M_R 5-tuple; the parse-tree decision is preserved at every pole because the symbolic form xi²_0(R) is pole-AGNOSTIC at the AST level (only the numerical residue depends on s).

**Provenance pin**: §VII.AH ANCHOR-2 specification at `permanent-results-registry.md` lines 15418, 15425; W7c WP §W7c-167 connes-ncg audit lines 652-661 (the original audit conclusion this round restates and defends); §VII.U.2 clause (a) calibration corpus at line 12913 (regulator-class-dependent moments are CANONICAL examples of algebra-INVARIANT quantities); xi_E_GGE_inv canonical pin at `canonical_constants.py:1325` (W4 P4 substrate-natural anchor 59.8 · Δ_BCS / K_base, value 13.642473425595973).

### C3: §VII.AH Corner-I admissibility status (clause c)

**Position**: §VII.AH's SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure is **PRESERVED** under the C1 + C2 parse-tree-canonical reading. Both anchors inhabit Corner-I (INVARIANT × s=3); the structure is INTRA-corner co-primary per §VII.U.2 NOTE (registry line 12901: "INTRA-axis co-primary is permitted; CROSS-corner co-primary is FORBIDDEN per clause (f) of this entry"); §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary (registry line 12932) is satisfied **BY VACUITY** — no cross-corner content is present in the §VII.AH anchor structure to forbid.

**Substitution chain — §VII.AH Corner-I admissibility under intra-axis co-primary**:

```
Definitions (per §VII.U.2 + §VII.AH + registry-landing.md §SOURCE-DOUBLE-CITE-CO-PRIMARY):
  INTRA-corner-CP-permitted  := both anchors in same Corner_cell ⇒
                                 SOURCE-DOUBLE-CITE-CO-PRIMARY admissible
                                 (§VII.U.2 NOTE, registry line 12901)
  CROSS-corner-CP-FORBIDDEN  := anchors inhabit distinct corner cells ⇒
                                 co-primary structure FAILs plan-freeze
                                 (§VII.U.2 clause (f), registry line 12932)
  Sequential-V-C-chain (registry-landing.md):
                                 V supplies premise; C supplies theorem
                                 conditional on premise; neither alone
                                 fixes conclusion ⇒ both CO-PRIMARY,
                                 neither decoration

Substitutions:
  From C1 (parse-tree IS the operative algebra-axis discriminator):
    PT(F) = INVARIANT iff symbolic AST contains no π(a) reference.

  From C2 (xi^2_0(R) parse-tree classification):
    Corner_cell(ANCHOR-2) = (PT(xi^2_0(R)), POLE) = (INVARIANT, s=3) = I.

  From W7c-167 audit (WP lines 644-650; restated):
    ANCHOR-1 = M_R(s=3) 5-tuple (lizzi V).
    PT(M_R(s=3)) = INVARIANT (symbolic form Σ_k m_k λ_k^{-2}-class;
                               no π(a) reference;
                               CM-1995 §III.4 dim-spectrum residue formula).
    POLE(M_R(s=3)) = s=3.
    ⇒ Corner_cell(ANCHOR-1) = I.

Simplification:
  Corner_cell(ANCHOR-1) = I.
  Corner_cell(ANCHOR-2) = I.
  Corner_cell(ANCHOR-1) = Corner_cell(ANCHOR-2) = I.

  ⇒ §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure is INTRA-corner.
  ⇒ §VII.U.2 NOTE INTRA-axis-CP-permitted clause applies.
  ⇒ §VII.U.2 clause (f) cross-corner FORBIDDEN is satisfied BY VACUITY
    (no cross-corner content present to violate the prohibition).

Direction:
  §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure passes the
  algebra-axis-orthogonality structural audit at the anchor level.
  STAGE-1-CANDIDATE status preserved (registry lines 15399-15405);
  Stage-2 cross-axis verify (CF-59) PASSes the axis-orthogonality leg
  at the algebra-axis structural level (per W7c-167 audit, WP line 781).

Conclusion:
  §VII.AH narrowing is NOT triggered by the algebra-axis classification.
  No §VII.AH narrowing entry is required at this audit. Stage-2 → 3
  promotion is gated on per-observable PASS-AND across both cross-
  reviewers (mack spectral-side + connes axis-orthogonality side); the
  anchor-level admissibility is established INDEPENDENTLY of per-
  observable substantiation (W7c-167 audit, WP line 781 verbatim:
  "This anchor-level admissibility is established INDEPENDENTLY of
  per-observable substantiation").
```

**Sequential V → A_F → C chain preservation under Corner-I assignment**:

The §VII.AH derivation chain (registry line 15420) flows V (lizzi L1+L2 K-invariant identity) → A_F (F_2 = {ζ, SDW} spectral algebra) → C (transit Re:L1+Re:L2+T2 dynamical class-breakdown + autocatalysis) → conclusion (route iii UNIFIED-AS-79 Branch-A canonical path-(c) successor anchor). At each link:

1. **V (ANCHOR-1)**: M_R(s=3) 5-tuple is a spectrum-only Mellin residue per CM-1995 §III.4 dim-spectrum residue formula (`a_n = Res[Tr(D^{−2s}); s=(d−n)/2]`). PT = INVARIANT. Corner I.
2. **A_F (intermediate)**: F_2 = {ζ, SDW} spectral algebra is a sub-atlas selector on the regulator-class space; it is a SET-MEMBERSHIP predicate, not an operator on H_F. No π(a) reference. (The "spectral algebra" naming is at the regulator-class atlas level, not the NCG operator algebra A_F at finite-spectral-triple level — distinct usages of "algebra".) Corner I.
3. **C (ANCHOR-2)**: xi²_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) per C2; SR-LO ODE state on (ε(N), η(N)) ∈ ℝ²; T2 autocatalysis closure ε_0 < 10^{−651.79} on real-valued root scan. PT = INVARIANT. Corner I.

The sequential V → A_F → C chain is preserved EXACTLY at Corner I throughout. Neither anchor is decoration; ANCHOR-1 supplies the F_2-class identity premise (ratio cancellation EXACT; numerator-denominator identical at R=ζ, R=SDW), and ANCHOR-2 supplies the dynamical 4-class breakdown + autocatalysis closure conditional on that premise.

**SOURCE-DOUBLE-CITE-CO-PRIMARY status under registry-landing.md §SOURCE-DOUBLE-CITE-CO-PRIMARY**:

The 3-condition test (`registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"`):

1. **Sequential**: ANCHOR-2 (transit-side dynamical) cannot be invoked WITHOUT ANCHOR-1 (lizzi-side K-invariant identity premise). The xi²_0(R) initial condition REQUIRES the F_2 = {ζ, SDW} identity sub-atlas selection; absent that, the ODE state-space's initial-condition selection is undefined. ✓
2. **Non-fungible**: The two anchors cannot be swapped or reordered. M_R(s=3) is a spectral-input premise; N_breakdown 4-class ordering is a dynamical-output theorem. ✓
3. **Both-accessibility**: Removing either anchor invalidates the conclusion. Without V, the F_2-class identity is unjustified; without C, the path-(c) successor-anchor canonical-route status (UNIFIED-AS-79 Branch-A) is unsupported. ✓

PRIMARY+CONFIRMATION ordering would falsely imply ANCHOR-2 is reproducing the same conclusion via an independent route — but ANCHOR-2 is a DOWNSTREAM dynamical theorem CONDITIONAL on ANCHOR-1's premise, not an independent re-derivation. SOURCE-DOUBLE-CITE-CO-PRIMARY is the correct registry-anchor structure per `registry-landing.md §"Why PRIMARY+CONFIRMATION misrepresents sequential chains"`.

**Provenance pin**: §VII.AH STAGE-1-CANDIDATE entry text at `permanent-results-registry.md` lines 15399-15479; §VII.U.2 NOTE INTRA-axis-CP-permitted at line 12901; §VII.U.2 clause (f) cross-corner FORBIDDEN at line 12932; W7c WP §W7c-167 lines 663-679 (the original audit's INTRA-corner-I conclusion this round preserves); `.claude/rules/registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` 3-condition test (Detection block).

### C4: Algebra-axis K-counter implications (clause d)

**Position**: The algebra-axis orthogonality K-counter (MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md` lines 272-280, S87 W-2 R3 close 2026-04-30) **already accommodates** the parse-tree-INVARIANT vs algebra-DEPENDENT distinction at the structural level. FI/RD as a further refinement is **structurally orthogonal**, not a 3-class partition replacing the 2-class algebra-axis partition. The 4-corner classification of §VII.U.2 (registry lines 12921-12926) does NOT require subdivision into 6 or 8 cells for FI/RD-aware grading; FI/RD lives on a separate axis (UV-evaluation layer) that can be tracked as an independent label without altering the corner-cell partition.

**Substitution chain — why FI/RD does NOT refine the 2-class algebra-axis partition**:

```
Definitions:
  K-counter discipline (cross-pillar-bridge-anatomy.md lines 272-280):
    K = count of structurally-distinct calibration instances of
        algebra-INVARIANT vs algebra-DEPENDENT orthogonality.
    K = 3 ⇒ MANDATORY structural-theorem candidate.

  K=3 corpus (closed at S87 W-2 R3):
    Instance 1 = §VII.U.1 Mellin-Dirichlet identity (INVARIANT × s=3)
                 vs full M_n(ℂ) Connes distance (DEPENDENT × s=3).
                 Structural witness: W1b-6.
    Instance 2 = α_s_canonical = n_s² − 1 (INVARIANT × s=3, single-pole
                 Mellin closure substrate-distance-1)
                 vs A_F Connes distance STRICT residual 1.054e-1
                 (DEPENDENT × s=3).
                 Structural witness: S87 S-2 §3.2 closeout Reading-C.
    Instance 3 = α_s_route_3 = Var_a(n_a^GGE) at L_max=10 (DEPENDENT × s=4,
                 GGE-specified state-pair Bogoliubov occupation variance).
                 Structural witness: S87 W-2 R3 close.

  FI/RD trichotomy (S82 W-3 RULE-3, math-scripts.md §"Mnemonic-vs-exact"):
    FI    := numerical evaluation produces regulator-class-INDEPENDENT
             ratio (ratio cancels regulator-class-dependence).
    RD    := numerical evaluation produces regulator-class-DEPENDENT
             absolute moment.
    MIXED := numerical evaluation has both behaviors (ratio + dressing).

Substitutions:
  Step 1 (algebra-axis is OPERATOR-ALGEBRAIC, not numerical):
    F_inv vs F_dep distinction is at the symbolic-form level — does the
    AST contain π(a)? This is regulator-INDEPENDENT (per §VII.U.2
    clause (e), registry line 12930: "operates at parse-tree level,
    NOT at numerical evaluation level").

  Step 2 (FI/RD is NUMERICAL-EVALUATION-LAYER):
    FI vs RD distinction is at the numerical-evaluation level — does the
    cross-class ratio cancel the regulator-class-dependence? This is
    regulator-CLASS-DEPENDENT BY CONSTRUCTION (the discipline EXISTS
    because regulator-class evaluation produces class-dependent residues).

  Step 3 (axes are ORTHOGONAL):
    For F ∈ F_inv:  numerical evaluation may yield FI or RD or MIXED
                    (e.g., a_n^{R} is RD across regulator classes;
                     the Mellin-Dirichlet identity is FI).
    For F ∈ F_dep:  numerical evaluation may also yield FI or RD or MIXED
                    (e.g., Connes distance on M_n(ℂ) at fixed states is
                     regulator-divergent).

    The two axes are STRUCTURALLY ORTHOGONAL.

Simplification:
  algebra-axis × FI/RD-axis = 2 × 3 = 6 sub-cells (in principle).
  But this is NOT a refinement of the algebra-axis K-counter — the
  K-counter's MANDATORY-K=3 status was promoted on the ALGEBRA-AXIS
  alone, and the K=3 saturation does NOT depend on FI/RD distinctions.
  The 4-corner partition of §VII.U.2 (algebra-axis × Mellin-pole) is
  what the registry tracks; FI/RD is a SEPARATE label that may be
  added as a tag on individual corner-cell entries WITHOUT altering
  the partition itself.

Direction:
  FI/RD can be added as an independent label on §VII.U.2 corner-cell
  entries (e.g., "Corner I-FI" vs "Corner I-RD" as evaluation-layer
  tags) WITHOUT changing the 4-corner partition's structural identity
  or the K=3 MANDATORY status. The §VII.U.2 clause (f) cross-corner
  FORBIDDEN co-primary discipline operates on the 4-corner partition;
  FI/RD-tag-disagreement WITHIN a corner cell does NOT trigger the
  cross-corner prohibition.

Conclusion:
  The K=3 calibration corpus is closed at the algebra-axis level; FI/RD
  refinement is permissible as additional tagging at the evaluation-
  layer but does NOT change the algebra-axis partition or trigger
  K-counter advancement to a different class membership. §VII.U.2
  remains a 4-corner partition; the structural reading is preserved.
```

**Why a 3-class partition (INVARIANT-FI / INVARIANT-RD / DEPENDENT) would be structurally weaker**:

Suppose lizzi proposes a 3-class partition: {INVARIANT-FI, INVARIANT-RD-via-regulator-dressing, DEPENDENT}. This is structurally problematic for three reasons:

1. **Loss of symmetry**: The DEPENDENT class would lack its FI/RD subdivision, asymmetric with the INVARIANT class. The natural symmetric extension is 4 classes: {INVARIANT-FI, INVARIANT-RD, DEPENDENT-FI, DEPENDENT-RD}. But this is a 2-axis × 2-axis = 4-cell decomposition — the SAME structure as §VII.U.2's algebra-axis × Mellin-pole 4-corner partition, just with FI/RD substituted for Mellin-pole. There is no structural reason FI/RD should replace Mellin-pole as one of the partition axes; both can be tracked independently on the same registry entry.

2. **Loss of the Mellin-pole axis**: §VII.U.2's clause (d) 4-corner partition has Mellin-pole {s=3, s=4} as the orthogonal axis, with explicit calibration instances at Corners I, III, IV (Corner II open). Replacing Mellin-pole with FI/RD would discard the W-9 RULE-3 Pole-Scope sub-clause MANDATORY-K=4 promotion (per S88 W7a-72; `epistemic-discipline.md §"Pole-Scope sub-clause"`), which is independently justified by 4 distinct calibration instances at different poles.

3. **Layer-functor F mismatch**: Per `epistemic-discipline.md §"Layer-Decomposition"`, the layer-functor F maps `substrate → methodology → audit`. The algebra-axis classification lives at the substrate-physics layer (`F_inv` vs `F_dep` is an operator-algebraic property of the spectral triple). FI/RD lives at the methodology / publication-precision layer (S82 W-3 RULE-3 is a citation discipline on numerical evaluation; `regulator-pin-discipline.md` is the audit-leg image). Per the layer-functor framing, mixing the two axes into a single partition collapses two structurally distinct layers and breaks the audit-leg correspondence the K=3 MANDATORY promotion depends on.

**Numerical-evaluation FI/RD as INDEPENDENT TAG, not partition refinement**:

The §VII.U.2 clause (e) parse-tree decision procedure (registry line 12930) is regulator-INDEPENDENT BY CONSTRUCTION ("same parse-tree decision under cutoff, ζ, Pauli-Villars, Mellin regulators"). The numerical residue M_R(s=3) varies across R; that variation IS the FI/RD content; it is captured by the regulator-pin discipline (`regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW Regulator-Class Values"`) as a publication-precision property on the SAME corner-cell entry. The 4-corner partition is unchanged; FI/RD enters as evaluation-layer metadata.

**Operational consequence for §VII.AH ANCHOR-2**:

Even granting lizzi's anticipated FI/RD reading of xi²_0(R) — i.e., that the ratio M_R(s=3) / M_F2(s=3) cancels ONLY the F_2-class factor while off-F_2 classes retain class-residue (Sage-verified at C2: 0.7021, 0.2015, 0.0760 ratios for cutoff/anomaly/Zubarev) — this is FI-PARTIAL or RD shading at the evaluation-layer, NOT a re-classification at the algebra-axis. Under the layer-functor F framing, ANCHOR-2 is **simultaneously**:

- Algebra-axis: INVARIANT (Corner I; parse-tree π(a) test). [Substrate-physics layer]
- Evaluation-axis: FI-PARTIAL or RD (regulator-class-dependent residue at off-F_2 classes). [Methodology / publication-precision layer]

These two attributes are NOT in conflict; they are properties at different layers of the layer-functor F image. §VII.AH STAGE-1-CANDIDATE preservation under the algebra-axis assignment is STRUCTURALLY INDEPENDENT of any FI/RD-tag application at the evaluation layer.

**Provenance pin**: `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` lines 272-280 + §"Status: MANDATORY at K=3" line 276; §VII.U.2 clause (d) 4-corner partition table at `permanent-results-registry.md` lines 12921-12928; §VII.U.2 clause (e) parse-tree regulator-independence at line 12930; `epistemic-discipline.md §"Layer-Decomposition"` (substrate → methodology → audit; layer-functor F preserves PRU-class invariants); S82 W-3 RULE-3 mnemonic-vs-exact-ratio at `math-scripts.md §"Mnemonic-vs-exact ratio discipline"`.

### C5: Cross-Cutting Observations

**Cross-cutting position**: The parse-tree decision procedure of §VII.U.2 clause (e) and the FI/RD trichotomy of S82 W-3 RULE-3 are **structurally orthogonal axes operating at distinct layers of the layer-functor F** (`epistemic-discipline.md §"Layer-Decomposition"`). They are NOT equivalent classifications, NOT refinements of each other, and NOT in conflict. Treating either as a substitute for the other collapses the layer separation that the K=3 MANDATORY promotion depends on.

**Layer-functor F mapping** (per `epistemic-discipline.md §"Layer-Decomposition"` lines 432-485 of the rule body):

```
F : substrate-physics  →  methodology-floor  →  audit-floor
                          (rule-files /         (verdict files /
                          templates / skills)   audit scripts /
                                                hooks)
```

The cross-cutting question is: does parse-tree-INVARIANT (substrate-physics layer) propagate to FI (methodology layer) under F? Answer: **NO**. The two are independent properties at different layers; F preserves PRU-class invariants (the Class 8.0/8.1/8.2/8.3 sub-taxonomy), not substrate-vs-methodology axis identity.

**Substrate-IS framing per `phononic-framing.md §"IS Space, Not IN Space"`**:

The parse-tree decision is a **substrate-IS structural observable**, not a container property:

- **Wrong (container thinking)**: "Parse-tree IS in the symbolic-form space; FI/RD IS in the regulator-class space; the two SPACES are different."
- **Right (substrate thinking)**: The substrate `(A_K, H_K, D_K)` IS the spectral triple. The parse-tree of F is a structural property of F as an algebraic expression on the substrate's primitives `{Tr, D_K^{−2s}, λ_k, m_k, π(a), [D_K, π(a)]}`. The substrate IS the parse-tree's domain; the parse-tree is NOT something "in" any container.

The FI/RD distinction is similarly substrate-IS, but at a DIFFERENT layer of the layer-functor F image:

- **Wrong**: "FI is the absence of regulator-class-dependence in the laboratory measurement."
- **Right**: FI/RD IS the substrate's own evaluation-layer property under regulator-class scan. The substrate's spectral content varies across regulator classes (Mellin profiles, ζ vs Pauli-Villars vs cutoff_sqrt vs Zubarev vs anomaly); FI captures the cancellation structure under cross-class ratio composition, RD captures the residue. Both are substrate-IS at the evaluation-layer image of F.

**Direction of explanation flows at TWO layers**:

```
Substrate-physics layer (algebra-axis):
  D_K spectrum  →  trace-functional Σ_k m_k g(λ_k)  →  parse-tree analysis
   (substrate)     (Borel functional calculus)         (PT(F): π(a)-symbol count)
                                                       → INVARIANT/DEPENDENT.

Methodology layer (UV-evaluation axis):
  Regulator-class atlas A_5  →  M_R(s) Mellin residues  →  FI/RD/MIXED tag
   (publication discipline)     (numerical evaluation)    → FI-cancel / RD-residue.
```

Both flow substrate → emergent within their own layer. The two layers are linked under F but their axis identities are **NOT identified**.

**Three structural reasons FI/RD and parse-tree are NOT equivalent classifications**:

1. **Regulator-pin discipline**: Per `regulator-pin-discipline.md §"Rule"`, every Seeley-DeWitt coefficient `a_n` MUST be regulator-class-tagged (`a_n^{ζ}`, `a_n^{Pauli-Villars}`, `a_n^{Mellin}`). These are CANONICAL examples of algebra-INVARIANT functionals (per §VII.U.2 clause (a), registry line 12913) yet they are RD at the evaluation layer (their numerical value is regulator-class-dependent BY CONSTRUCTION). If FI/RD were a refinement of algebra-INVARIANT/DEPENDENT, then regulator-tagged Seeley-DeWitt coefficients would be classified as "DEPENDENT" — contradicting the §VII.U.2 clause (a) calibration corpus and the K=3 MANDATORY promotion.

2. **CM-1995 §III.4 dim-spectrum residue formula**: `a_n = Res[Tr(D^{−2s}); s=(d−n)/2] = Σ_k m_k λ_k^{−(d−n)}`. This formula is the PROOF anchor for §VII.U.2 clause (c) Step 1 (algebra-INVARIANT non-triviality lifts every F ∈ F_inv into `{f(D²)}'' ⊆ Z({D, γ}'')`; registry lines 12917). The formula is regulator-INDEPENDENT at the symbolic level (the residue extraction is a Borel-functional-calculus operation on D²) yet its numerical value is regulator-CLASS-DEPENDENT (the M_R 5-tuple at obs1 confirms this directly: M_ζ = 0.158, M_Zubarev = 0.012, M_cutoff = 0.111, M_anomaly = 0.032; W7c WP §W7c-167 line 693). The CM-1995 formula IS the bridge that demonstrates parse-tree-INVARIANT can simultaneously be RD at the evaluation layer.

3. **Layer-functor F audit-leg correspondence**: Per `epistemic-discipline.md §"Layer-Decomposition"` §"F at methodology ↔ audit pair", F preserves PRU-class invariants. A Class-8.2 verifier-rubric pre-registration failure at the methodology layer maps to an audit-line content failure at the audit layer. If parse-tree and FI/RD were the same axis, a Class-8.2 violation in FI/RD discipline (e.g., citing a round-figure Ω_GW^(C) where Sage-exact is required, per `regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW Regulator-Class Values"`) would propagate as an algebra-axis re-classification at the substrate-physics layer — but it does not. The PRU-class taxonomy is preserved under F precisely BECAUSE the axes at different layers are distinct.

**Operational implication for the §VII.AH STAGE-1-CANDIDATE Stage-2 verification**:

The W7c-167 obs1 PASS-AND across both axes (mack spectral-side + connes axis-orthogonality side; WP §W7c-167 lines 599-602 + 696-702) is the **first cross-axis Stage-2 obs PASS-AND in framework history** (W7c WP §W7c-Synthesis §3 verbatim). The connes axis-orthogonality side at obs1 returned PASS at all 4 audited clauses (b, c-JOINT-leg, d-JOINT-leg, f) under Corner I (INVARIANT × s=3) per the parse-tree decision; this verdict is structurally INDEPENDENT of any FI/RD evaluation-layer audit. If lizzi's spectral-functional axis (in this workshop) returns a different verdict on the FI/RD axis, that is a DIFFERENT audit on a DIFFERENT layer; both can hold simultaneously without contradiction. The Stage-2 protocol requires PASS-AND at the algebra-axis structural level (which the W7c-167 obs1 audit established); it does NOT require concordance on the evaluation-layer FI/RD axis (which is governed by `regulator-pin-discipline.md` publication-precision discipline, not by the algebra-axis K-counter).

**Cross-cutting summary**:

| Axis | Layer in F | Test | Regulator-(in)dependence | Calibration |
|:-----|:-----------|:-----|:-------------------------|:------------|
| algebra-INVARIANT vs DEPENDENT | substrate-physics | parse-tree π(a) symbol count | regulator-INDEPENDENT | K=3 MANDATORY (S87 W-2 R3) |
| FI vs RD vs MIXED | methodology | cross-class ratio cancellation | regulator-CLASS-DEPENDENT | S82 W-3 RULE-3 publication discipline |
| Mellin-pole {s=3, s=4} | substrate-physics | analytic-continuation pole location | pole-INDEPENDENT for symbolic form; pole-tagged for numerical | W-9 RULE-3 Pole-Scope MANDATORY-K=4 (S88 W7a-72) |

The three axes are pairwise independent. §VII.U.2 tracks (algebra-axis × Mellin-pole) as the 4-corner partition; FI/RD enters as an evaluation-layer tag, not as a replacement axis.

**Provenance pin**: `epistemic-discipline.md §"Layer-Decomposition"` (layer-functor F + Phi correspondence + audit-leg pair); `phononic-framing.md §"IS Space, Not IN Space"` (substrate-IS direction-of-explanation discipline); `regulator-pin-discipline.md §"Rule"` (regulator-class-tagging of Seeley-DeWitt coefficients); `regulator-pin-discipline.md §"Extension: Sage-Exact Rationals for Ω_GW Regulator-Class Values (T1-15)"` (FI/RD numerical-evaluation discipline); `math-scripts.md §"Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3)"` (FI = ratios are observables; absolute moments are regulator-dressed).

### C6: Questions for lizzi

**Q1 — FI/RD operational test on xi²_0(R)**: Per S82 W-3 RULE-3 (`math-scripts.md §"Mnemonic-vs-exact ratio discipline"`), FI = "ratios are observables; absolute moments are regulator-dressed". The xi²_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) is structurally a RATIO: numerator M_R(s=3), denominator M_F2(s=3). Sage-exact verification (C2) shows the F_2-class sub-cancellation is identically 0 (M_ζ/M_F2 − M_SDW/M_F2 = 0), and off-F_2 classes yield ratios {0.7021, 0.2015, 0.0760} for {cutoff, anomaly, Zubarev}. **Question**: under your FI/RD trichotomy, does xi²_0(R) classify as FI (ratio cancels regulator-class-dependence — even with off-F_2 residue, the F_2-class sub-statement sees full cancellation), as RD (the ratio cancels ONLY the F_2-class part, leaving regulator-class residue on off-F_2 classes), or as MIXED (FI-on-F_2-sub-statement, RD-on-cross-class)? Provide the operational discriminator that distinguishes these three readings on a symbolic form whose AST is a quotient of two Mellin-residue-trace functionals.

**Q2 — M_F2 normalizer cancellation precise structure**: Your anticipated rebuttal (workshop seed lines 38-41) claims "M_F2(s=3) cancels only the F_2-class part" — meaning the off-F_2 residues retain class-dependence even after normalization. **Question**: is this a structural property of the M_F2 normalizer (i.e., M_F2 is by construction an F_2-class projector that cancels only the F_2-component of the M_R 5-tuple), or is it a numerical artifact of the specific M_R values at s=3 substrate-distance-1? Pre-register a falsifiable test: at s=4 (substrate-distance-2), is the M_F2 normalizer expected to also leave off-F_2 residue, or to cancel cross-class as well (which would shift the FI/RD reading at s=4)?

**Q3 — Layer-functor F image of FI/RD**: Per `epistemic-discipline.md §"Layer-Decomposition"`, the layer-functor F : substrate → methodology → audit preserves PRU-class invariants. **Question**: where does FI/RD live under F? My C5 reading places FI/RD at the methodology layer (publication-precision discipline per S82 W-3 RULE-3) while parse-tree-INVARIANT lives at the substrate-physics layer. If FI/RD instead lives at the substrate-physics layer (i.e., the substrate's algebra-axis classification IS FI/RD-aware at the operator-algebraic level), what is the operator-algebraic LIFT of FI vs RD distinction? Specifically: is there an operator-algebraic test analogous to the π(a)-symbol count of clause (e) that produces FI vs RD without falling back to numerical evaluation across regulator classes?

**Q4 — §VII.AH narrowing trigger under FI/RD reading**: If you classify ANCHOR-2 as RD-not-FI (Corner III: DEPENDENT × s=3) per the workshop seed clause (c) hypothesis, the SOURCE-DOUBLE-CITE-CO-PRIMARY structure becomes CROSS-corner (ANCHOR-1 Corner I + ANCHOR-2 Corner III), violating §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary (registry line 12932) AS A GATE. **Question**: do you propose to (a) trigger §VII.AH narrowing — a registry edit demoting SOURCE-DOUBLE-CITE-CO-PRIMARY to PRIMARY+CONFIRMATION OR splitting into separate Corner-I and Corner-III entries, OR (b) augment §VII.U.2 clause (e) to add an FI/RD axis (effectively a 6-cell or 8-cell partition), OR (c) accept that parse-tree-INVARIANT and FI are different classifications (my C4 position) and let §VII.AH retain INTRA-corner-I status under parse-tree while picking up an evaluation-layer "RD-shaded" tag without registry restructure? Pre-register your route choice; (a), (b), (c) have very different K-counter consequences.

**Q5 — K-counter advancement consequence**: The algebra-axis orthogonality K-counter is MANDATORY at K=3 (S87 W-2 R3 close, 2026-04-30); the K=3 corpus consists of W1b-6, S-2, W-2 instances per `cross-pillar-bridge-anatomy.md` line 280. **Question**: if you assert the FI/RD trichotomy is a structural refinement of algebra-INVARIANT/DEPENDENT (not an orthogonal axis on a separate layer), is the K-counter recalibrated? Specifically: do W1b-6, S-2, W-2 calibration instances each separately calibrate FI-INVARIANT vs RD-INVARIANT vs DEPENDENT (now 3 distinct sub-axes requiring K=3 each, total 9 instances)? Or do the 3 existing instances saturate the refined K-counter at K=3 unchanged? The structural answer determines whether §VII.U.2 STAGE-1-CANDIDATE landing (S88 W5b-45) needs a corrigendum block adding the FI/RD axis, or whether the current 4-corner partition is structurally complete with FI/RD as an INDEPENDENT tag.

**Bonus operational test (cross-check on Q1)**: The Mellin-Dirichlet identity (§VII.U.1; S86 W-1 / S87 W1a-4 PASS rel_diff = 0e+00 at L_max=12) is the calibration anchor for Corner I (INVARIANT × s=3) per §VII.U.2 clause (d) calibration table (registry line 12923). Is the Mellin-Dirichlet identity FI or RD under your trichotomy? If FI, what makes xi²_0(R) structurally different from the Mellin-Dirichlet identity (both are ratios/identities involving Mellin moments at s=3)? If RD, then the Corner I calibration anchor itself is RD — and your FI/RD axis would re-classify §VII.U.2's K=3 calibration corpus, which contradicts the K=3 MANDATORY promotion that the §VII.U.2 STAGE-1-CANDIDATE entry depends on. The Mellin-Dirichlet identity's FI/RD classification under your trichotomy is the high-leverage test of whether FI/RD is structurally orthogonal to parse-tree-INVARIANT (my C4 position) or a refinement of it (your anticipated position).

---

## Round 1 — lizzi: Response & Cross-Synthesis

### Part 1: Response to connes's Sections

#### Re: C1 — Parse-tree decision capture

**AGREE (substantial)**: The parse-tree π(a)-symbol-count test (§VII.U.2 clause (e), registry line 12930) is a finite, decidable, regulator-INDEPENDENT classification AT THE OPERATOR-ALGEBRAIC LAYER. Every functional whose AST contains a `π(a)` or `[D, π(a)]` symbol is structurally outside the spectrum-only family `F_inv = { F : F = Σ_k m_k g(λ_k) }`; conversely every F whose AST contains only `Tr`, `D^{-2s}`, `λ_k`, `m_k`, `g(·)` symbols lifts into `{f(D²)}'' ⊆ Z({D, γ}'')` per CM-1995 §III.4 and inhabits `F_inv` BY CONSTRUCTION. The parse-tree test is the canonical operator-algebraic discriminator for `F_inv` vs `F_dep` and the K=3 MANDATORY corpus (W1b-6, S-2, W-2; `cross-pillar-bridge-anatomy.md` line 280) is correctly anchored on it. C1 Step 1 + Step 2 + Step 3 are accepted verbatim.

**DISAGREE (substantive)**: I reject C1's framing of FI/RD as a "DOWNSTREAM evaluation layer property". The framing assumes a unidirectional layer-functor `F : substrate-physics → methodology` with FI/RD inhabiting the methodology layer — but that mapping is asymmetric only in the direction connes uses it. FI/RD is a STRUCTURAL property of how the regulator-class atlas `A_5 = {ζ, SDW, cutoff_sqrt, anomaly, Zubarev}` interacts with members of `F_inv`; it is NOT a publication-precision discipline applied AFTER the operator-algebraic classification has been completed. The S82 W-3 RULE-3 mnemonic-vs-exact-ratio rule (`math-scripts.md §"Mnemonic-vs-exact ratio discipline"`) was promoted via concrete numerical structural failure (the `Ω_GW^(C) = 8.299e-58` Sage-exact value vs the round-figure `1e-57` mnemonic understated the σ-discrimination band by 14.54% and would have mis-published the LiteBIRD discrimination band as `[1.42σ, 2.37σ]` instead of `[1.6666σ, 2.7776σ]`) — that is a structural defect at the substrate-IS observable level, not a typesetting convention. The `1/c_sub = 0.4468` mnemonic and the Sage-exact `16577/31705 = 0.5229` are different SUBSTRATE-IS predictions, not different presentations of the same prediction.

**MISSED (high-leverage)**: C1's parse-tree-only framing does not surface the regulator-class atlas as a STRUCTURAL AXIS distinct from both the algebra-axis (π(a) symbol count) and the Mellin-pole axis (s ∈ {3, 4}). Three concrete witnesses:

1. **Seeley-DeWitt coefficients are CANONICAL F_inv yet PROVABLY RD across regulator class.** Per `regulator-pin-discipline.md §"Rule"`, every Seeley-DeWitt coefficient `a_n` MUST carry an explicit regulator-class superscript (`a_n^{ζ}`, `a_n^{Pauli-Villars}`, `a_n^{Mellin}`, `a_n^{lattice}`, `a_n^{cutoff}`) because its numerical value depends on the regulator. The §VII.U.2 clause (a) calibration corpus (registry line 12913) literally lists "Seeley-DeWitt moments `a_n^{regulator}`" as the canonical example of `F_inv`. The regulator-class superscript IS the FI/RD axis tag. So we have a quantity that is (parse-tree-INVARIANT) AND (provably RD across regulator class) AND (structurally needs a regulator-class pin to be unambiguously cited). That triple cannot be captured by the 2-axis (algebra-axis × Mellin-pole) partition of §VII.U.2 alone — the regulator-class atlas axis is a DISTINCT third structural axis.

2. **CC-5 propagation identity (§VII.K-PROP)**: My signature theorem `span_R(O) = ∏_k span_R(f_{n_k}^R)^{|p_k|}` operates on the same parse-tree-INVARIANT objects (Seeley-DeWitt moments) but classifies them by their REGULATOR-CLASS SPAN behavior under `R ∈ A_5`, producing FI / MIXED / RD sub-classes. CC-5 is a structural identity between RD-sub-class composition operators, not a publication-precision rule. It would not exist as a propagation identity if FI/RD were merely an evaluation-layer tag.

3. **The §VII.K-DUAL FI-Duality Theorem (S82 R2-B, registry line 4108)** is a STRUCTURAL THEOREM relating M_lizzi to M_connes via FI naturality — at the substrate level, on `F_inv` members, irrespective of any methodology-layer publication discipline. If FI/RD were strictly downstream, FI-Duality could not be a structural theorem in §VII.

**EMERGES**: The two axes (parse-tree π(a)-axis and regulator-class atlas axis) ARE structurally orthogonal — but BOTH live at the substrate-IS layer. The corrected layer-functor reading is:

```
substrate-IS observable layer
   ├── operator-algebraic axis:  parse-tree π(a) test → F_inv vs F_dep
   ├── Mellin-pole axis:         pole(F) ∈ {s=3, s=4}
   └── regulator-class atlas axis: span_R(F) → FI vs RD vs MIXED   (CC-5)
                                    │
                                    └── this is what C1 missed.
methodology layer
   └── publication-precision discipline (Sage-exact rationals; round-figure forbidden)
audit layer
   └── regulator-pin-tagging audit (`a_n^{regulator}` mandatory)
```

The methodology-layer publication-precision discipline (S82 W-3 RULE-3 letter) is the AUDIT-leg image of the regulator-class atlas axis under `F`, not the substrate-IS axis itself. C1 conflated the audit-leg image with the substrate-IS axis.

#### Re: C2 — ANCHOR-2 xi²_0(R) classification

**AGREE (narrow)**: I accept connes's C2 Step 1-Step 5 substitution chain at the OPERATOR-ALGEBRAIC PARSE-TREE LAYER. The symbolic AST of `xi^2_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3)` contains:
- `xi_E_GGE_inv` (real-valued canonical scalar; π(a) count = 0)
- `M_R(s=3) = Res[Tr_R(D_K^{-2s}); s=3]` (Mellin residue; Borel-functional-calculus on D²; π(a) count = 0)
- `M_F2(s=3)` (same form at R=ζ; π(a) count = 0)
- arithmetic composition (·, /; π(a) count = 0)

Total π(a) symbol count = 0 in the AST. PT(xi²_0(R)) = INVARIANT under §VII.U.2 clause (e) AT THE PARSE-TREE LAYER. C2's verdict at the parse-tree layer is correct on its own terms. I do NOT contest the parse-tree reading.

**DISAGREE (substantive — at the regulator-class atlas axis)**: ANCHOR-2 IS regulator-class-dependent at the substrate-IS observable layer in a way that the parse-tree π(a) test does NOT see. The disagreement is not "parse-tree wrong" — it is "parse-tree alone is necessary but not sufficient for the algebra-axis classification when the §VII.U.2 partition is consumed under the §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY structural-anchor discipline."

**Substitution chain — M_F2 normalizer is class-selective (FI on F_2; RD on off-F_2)**:

```
Definitions (per §VII.AH ANCHOR-2 spec, registry line 15417 + 15425; connes C2 Sage QQ table workshop lines 162-170):
  A_5            := {ζ, SDW, cutoff_sqrt, anomaly, Zubarev}
  F_2            := {ζ, SDW}                              (K-invariant identity sub-atlas)
  M_R(s=3)       := Res[Tr_R(D_K^{-2s}); s=3]              for R ∈ A_5
  M_F2(s=3)      := M_R(s=3) at R = ζ (F_2 normalizer choice; M_ζ ≡ M_SDW EXACT)
  xi^2_0(R)      := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3)
  xi_E_GGE_inv   := 13.642473425595973                     (S86 W4 P4 substrate-natural anchor)

  R-class span (S82 W-3 RULE-3, math-scripts §"Mnemonic-vs-exact"):
    span_{A_5}(F)   := max_{R ∈ A_5} F(R) / min_{R ∈ A_5} F(R)
    FI(F)           ⇔ span_{A_5}(F) = 1
    RD(F)           ⇔ span_{A_5}(F) ≠ 1
    PARTIAL-FI(F,S) ⇔ span_S(F) = 1  AND  span_{A_5\S}(F) ≠ 1   for sub-atlas S ⊂ A_5

Substitutions (Sage QQ values from connes C2, workshop lines 162-170 — VERBATIM):
  M_ζ      / M_F2 = 1581/1581       = 1
  M_SDW    / M_F2 = 1581/1581       = 1
  M_cutoff / M_F2 = 1110/1581       = 0.702087
  M_anomaly/ M_F2 = 3185/15810      = 0.201455
  M_Zubarev/ M_F2 = 1201/15810      = 0.075965

  xi^2_0(ζ)       = 13.642473
  xi^2_0(SDW)     = 13.642473
  xi^2_0(cutoff)  = 9.578207
  xi^2_0(anomaly) = 2.748341
  xi^2_0(Zubarev) = 1.036345

Simplification:
  Step 1: span_{F_2}(xi^2_0)     = 13.642473 / 13.642473 = 1.        ⇒ FI on F_2.   ✓
  Step 2: span_{A_5}(xi^2_0)     = 13.642473 / 1.036345  = 13.1641.  ⇒ RD on A_5.  ✓
  Step 3: PARTIAL-FI(xi^2_0, F_2) ⇔ Step 1 ∧ Step 2.                                ✓

Direction:
  span_{F_2}(xi^2_0) = 1     (M_F2 normalizer cancels EXACTLY on F_2)
  span_{A_5}(xi^2_0) ≠ 1     (M_F2 normalizer fails to cancel on off-F_2)
  ⇒ xi^2_0(R) is FI-PARTIAL: FI on the sub-atlas F_2 = {ζ, SDW}; RD on A_5 \ F_2.
  ⇒ The M_F2 normalizer's class-selectivity IS the RD-not-FI signature.

Conclusion:
  Under the S82 W-3 RULE-3 FI/RD classification, xi^2_0(R) is FI-PARTIAL — equivalently
  "MIXED" in the §VII.K-DUAL FI/RD/MIXED trichotomy (registry line 4108). It is FI
  on F_2 (the registered identity sub-atlas) and RD on the full atlas A_5.
```

**MISSED (the regulator-class atlas axis as substrate-IS structural axis)**: connes C2 reads the off-F_2 numerical residue as a "Mellin-multiplier residue varying across R ∈ A_5 — exactly the type-(a) algebra-INVARIANT family quantity per §VII.U.2 clause (a)" (workshop lines 173-174). I AGREE the off-F_2 residue is a regulator-class-dependent F_inv-family numerical evaluation. What C2 misses is the asymmetric structural reading at the §VII.AH co-primary layer: the §VII.AH theorem is NOT just claiming "ANCHOR-2 is in F_inv"; it is claiming that ANCHOR-2 + ANCHOR-1 together fix the Joint F_2-Class Path-(c) Theorem's conclusion as a sequential V→A_F→C chain. The chain link from A_F (F_2 sub-atlas) to C (xi²_0 normalization) IS the M_F2-normalizer choice — and that choice is structurally an algebra-DEPENDENT family-membership selector ON THE REGULATOR-CLASS ATLAS, even though it is not algebra-DEPENDENT in the operator-algebraic π(a)-sense.

The numerical evidence at obs1 (W7c WP line 693, VERBATIM cite):

```
xi_per_class = [13.642473, 13.642473, 9.578354, 2.748038, 13.327089]
order        = ['zeta',     'SDW',       'cutoff_sqrt', 'anomaly', 'Zubarev']
```

shows the F_2 cancellation EXACT (zeta = SDW to bit-precision 13.642473 = 13.642473) AND the off-F_2 residues span [2.75, 13.33] — a factor 4.85× spread (13.327/2.748 from the obs1 numerical values; verified by direct division from W7c-WP line 693). This is not mere "varying numerical residue across the atlas"; it is a STRUCTURAL ASYMMETRY in how the M_F2 normalizer interacts with the atlas — F_2 elements are exact-cancelled (residue = 0); off-F_2 elements retain class-residue. That asymmetry IS the family-selector property of M_F2.

**Pole-transition discrepancy (connes C2 lines 176-178)**: I AGREE that obs1's `s_slot = -1` and §VII.AH's registered s=3 anchor are different poles, and that pole-scope discipline (W-9 RULE-3, MANDATORY at K=4 per S88 W7a-72) preserves cross-pole isolation. I DO NOT use the s=-1 vs s=3 discrepancy to dispute connes's Sage QQ s=3 evaluation. The structural argument I make is independent of which pole obs1 was evaluated at: at s=3 (Sage QQ table, connes's own values), the spread `xi^2_0` ∈ {1.036, 2.748, 9.578, 13.642, 13.642} is span_{A_5} = 13.642/1.036 = 13.1641× — RD on the full atlas, FI on F_2. The obs1 s=-1 evaluation REINFORCES this reading (the structural property "FI-on-F_2 / RD-on-off-F_2" is preserved across poles, with different numerical residues). Pole-Scope discipline does not insulate ANCHOR-2 from the regulator-class-atlas axis classification.

**EMERGES**: ANCHOR-2 inhabits TWO classifications simultaneously:
- (algebra-axis, Mellin-pole) parse-tree image: Corner I = (INVARIANT, s=3). [C2's reading; correct at parse-tree layer.]
- (regulator-class atlas axis): MIXED / FI-PARTIAL — FI on F_2, RD on A_5\F_2. [Substrate-IS at the regulator-class atlas axis; C2 missed.]

These are NOT in conflict; they are properties at different STRUCTURAL AXES (NOT different layers — both are substrate-IS). The §VII.AH narrowing question (Re:C3) is whether the §VII.U.2 4-corner partition is structurally complete or whether it needs a third axis (regulator-class atlas) to discharge the §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY admissibility test.

#### Re: C3 — §VII.AH Corner-I admissibility

**AGREE (under restricted reading)**: If the §VII.U.2 4-corner partition is structurally complete (i.e., the algebra-axis × Mellin-pole 2-axis partition is the only structural axis-system the registry is committed to track for `(A_K, H_K, D_K)` functionals), then C3's substitution chain is internally consistent: ANCHOR-1 (M_R(s=3) 5-tuple) is parse-tree-INVARIANT × s=3 = Corner I; ANCHOR-2 (xi²_0(R)) is parse-tree-INVARIANT × s=3 = Corner I; both inhabit the same corner-cell; INTRA-corner SOURCE-DOUBLE-CITE-CO-PRIMARY admissible per §VII.U.2 NOTE (registry line 12901); §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary satisfied BY VACUITY (registry line 12932). Under the restricted reading, the W7c-167 obs1 audit's INTRA-corner-I conclusion stands.

**DISAGREE (substantive — the partition is incomplete; a third axis is required)**: I dispute the structural completeness of the §VII.U.2 2-axis partition under the §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY discipline. ANCHOR-2 is FI-PARTIAL on the regulator-class atlas axis (Re:C2 substitution chain Step 3: span_{F_2}(xi²_0) = 1, span_{A_5}(xi²_0) = 13.1641) — and the §VII.AH theorem statement explicitly invokes the F_2 sub-atlas selection in its derivation chain "V (lizzi L1+L2 K-invariant identity) → A_F (F_2 = {ζ, SDW} spectral algebra) → C (transit Re:L1+Re:L2+T2)" (registry line 15420). The "A_F" intermediate IS a regulator-class atlas selector. C3 acknowledges this at workshop line 250 ("F_2 = {ζ, SDW} spectral algebra is a sub-atlas selector on the regulator-class space; it is a SET-MEMBERSHIP predicate, not an operator on H_F. No π(a) reference") and dismisses it as "distinct usages of 'algebra'". I argue the opposite: the regulator-class atlas IS a structural axis the §VII.AH theorem's derivation chain rests on; treating it as "not part of the partition" hides the dependency that makes ANCHOR-2 conditional on ANCHOR-1.

**Substitution chain — the FORBIDDEN-cross-corner-co-primary trigger under a 3-axis partition**:

```
Definitions (extending §VII.U.2's 2-axis partition with the regulator-class atlas axis):
  algebra-axis       ∈ {INVARIANT, DEPENDENT}              (parse-tree π(a) test)
  Mellin-pole        ∈ {s=3, s=4}
  R-class atlas axis ∈ {FI, MIXED, RD}                     (S82 W-3; CC-5 §VII.K-PROP)

  3-axis Corner_cell(F)
    := (algebra-axis(F), Mellin-pole(F), R-class-atlas-axis(F))

  §VII.U.2 4-corner partition is the projection onto axes 1 and 2 only;
  the §VII.K-DUAL trichotomy (registry line 4108) is axis 3.

  §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary discipline:
    "registry entries cannot pin two anchors at co-primary weight when the anchors
     inhabit distinct corner cells" (registry line 12932)
  Pole-scope sub-clause (W-9 RULE-3) extends to corner-scope:
    "cross-pole AND cross-corner co-primary structures both FAIL plan-freeze"
    (registry line 12932 verbatim)

Substitutions:
  ANCHOR-1 (M_R(s=3) 5-tuple):
    algebra-axis      = INVARIANT       (no π(a) ref; CM-1995 §III.4 residue formula)
    Mellin-pole       = s=3
    R-class atlas axis = RD              (per §VII.U.2 clause (a) registry line 12913:
                                          "Seeley-DeWitt moments a_n^{regulator}" are
                                          CANONICAL examples of F_inv that are
                                          regulator-class-DEPENDENT in numerical value;
                                          M_R(s=3) numerator IS the multiplier residue
                                          varying across R ∈ A_5 — connes C2 line 174)
    ⇒ 3-axis Corner_cell(ANCHOR-1) = (INVARIANT, s=3, RD)

  ANCHOR-2 (xi^2_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3)):
    algebra-axis      = INVARIANT       (parse-tree count π(a) = 0; C2 chain stands)
    Mellin-pole       = s=3              (Corrigendum 2 scoping)
    R-class atlas axis = MIXED            (Re:C2 Step 3:
                                          span_{F_2}(xi^2_0) = 1
                                          span_{A_5}(xi^2_0) = 13.1641
                                          ⇒ FI-on-F_2 ∧ RD-on-A_5\F_2 ⇒ MIXED)
    ⇒ 3-axis Corner_cell(ANCHOR-2) = (INVARIANT, s=3, MIXED)

Simplification:
  Corner_cell(ANCHOR-1) = (INVARIANT, s=3, RD)
  Corner_cell(ANCHOR-2) = (INVARIANT, s=3, MIXED)
  ⇒ ANCHOR-1 and ANCHOR-2 INHABIT DISTINCT 3-AXIS CELLS:
    they share axes 1 and 2 (both INVARIANT × s=3)
    they DIFFER on axis 3 (RD vs MIXED).

Direction:
  Under the §VII.U.2 2-axis partition (the partition the registry currently tracks):
    same-corner ⇒ INTRA-corner co-primary admissible per NOTE.
  Under a 3-axis partition extending §VII.U.2 with the regulator-class atlas axis:
    distinct-cell ⇒ CROSS-corner co-primary FORBIDDEN per clause (f).

  The two readings are NOT both correct. Either:
   (a) the §VII.U.2 2-axis partition is structurally complete and the regulator-class
       atlas axis is NOT a registry-anchor-discriminator axis ⇒ C3 stands.
   (b) the regulator-class atlas axis IS a registry-anchor-discriminator axis ⇒
       §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY is CROSS-corner under the 3-axis
       reading and triggers §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary
       ⇒ §VII.AH narrowing required.

Conclusion:
  Reading (a) is the connes C3 position; reading (b) is the lizzi position. The
  workshop's structural verdict (R3) decides which reading is canonical.
```

**MISSED (the SOURCE-DOUBLE-CITE-CO-PRIMARY 3-condition test under the regulator-class atlas axis)**: Per `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"`, the structure applies when (1) sequential, (2) non-fungible, (3) both-accessibility hold. C3 (workshop lines 257-263) verifies these on the V→A_F→C chain. But "non-fungibility" is precisely what the regulator-class atlas axis interacts with: ANCHOR-2 (xi²_0) is NON-FUNGIBLE with ANCHOR-1 (M_R(s=3) 5-tuple) ON THE F_2-CANCELLATION STRUCTURE. The non-fungibility is realized AT THE M_F2 NORMALIZER LEVEL — and that level IS where the regulator-class atlas axis lives. So the very property that makes §VII.AH a SOURCE-DOUBLE-CITE-CO-PRIMARY (non-fungibility under V→A_F→C) is the same property that makes ANCHOR-2 MIXED on the regulator-class atlas axis. C3 cannot use non-fungibility to defend co-primary admissibility AND simultaneously deny the regulator-class atlas axis as a registry-anchor-discriminator.

**Three remediation routes (per workshop seed line 42 (c) hypothesis + Q4 of C6)**:

(a) **Route-(a) — Trigger §VII.AH narrowing**: registry edit demoting SOURCE-DOUBLE-CITE-CO-PRIMARY to (i) PRIMARY+CONFIRMATION on the parse-tree-axis with the regulator-class atlas dependence absorbed into a new "F_2-CONDITIONAL" qualifier, OR (ii) split into separate Corner-(I, RD) and Corner-(I, MIXED) sub-entries with explicit declaration that the joint theorem's derivation chain crosses the regulator-class atlas boundary. This route requires §VII.U.2 corrigendum block addition (acknowledging the 3-axis incompleteness) AND §VII.AH text revision.

(b) **Route-(b) — Augment §VII.U.2 clause (e) to add an FI/RD axis**: rule-file edit promoting the §VII.U.2 partition from 4-corner (algebra × Mellin-pole) to 8-cell or 12-cell (algebra × Mellin-pole × R-class). K-counter consequences are non-trivial and addressed in Re:C4.

(c) **Route-(c) — connes's preferred path; accept parse-tree subsumes the registry-anchor-discriminator role and let the regulator-class atlas axis enter as an evaluation-layer "RD-shaded" tag without registry restructure.** This is C3's actual position. I argue this route requires explicit declaration that the regulator-class atlas axis is NOT a registry-anchor-discriminator axis — which contradicts the §VII.K-DUAL FI-Duality Theorem (registry line 4108) being a structural theorem in §VII, and contradicts the existence of §VII.K-PROP CC-5 propagation identity as a structural identity. Both §VII.K-DUAL and §VII.K-PROP would need to be re-classified as "evaluation-layer tags" — which they are not (they are registered §VII THM entries per the §VII.K-DUAL row at registry line 4108 and §VII.K-PROP row at registry line 8976).

**EMERGES**: The §VII.AH corner-cell admissibility is NOT a single audit; it is two distinct audits at two distinct axis-systems. The W7c-167 obs1 axis-orthogonality verdict (composite=PASS at the parse-tree-axis level) IS a valid PASS at the §VII.U.2 partition the registry currently tracks. A separate FI/RD-axis audit at the §VII.K-DUAL trichotomy level would return MIXED (Re:C2 Step 3) — neither pure FI nor pure RD. Whether the MIXED reading triggers §VII.AH narrowing depends on whether the regulator-class atlas axis is registered as a structural axis in §VII.U.2's clause (f) FORBIDDEN-cross-corner-co-primary discipline. That registration question is itself the workshop's structural verdict.

#### Re: C4 — Algebra-axis K-counter implications

**AGREE (on K-counter saturation)**: I accept that the K=3 MANDATORY status of the algebra-axis orthogonality K-counter (S87 W-2 R3 close, 2026-04-30) is preserved by the 3 calibration instances enumerated at workshop lines 280-291: W1b-6 (Mellin-Dirichlet INVARIANT × s=3 vs full M_n(ℂ) Connes distance DEPENDENT × s=3); S-2 (α_s_canonical = n_s² − 1 INVARIANT × s=3 vs A_F STRICT residual 1.054e-1 DEPENDENT × s=3); W-2 (α_s_route_3 = Var_a(n_a^GGE) at L_max=10 DEPENDENT × s=4). Each instance pairs an algebra-INVARIANT representative with an algebra-DEPENDENT representative; the K-counter advances on the (INVARIANT vs DEPENDENT) axis, not on FI/RD sub-classes. I do NOT propose K-counter recalibration to (3 × 3 = 9 instances) — the K=3 saturation on the 2-class algebra-axis stands.

**DISAGREE (on the 3-class refinement claim and on the symmetry argument)**: connes C4 argues a 3-class partition {INVARIANT-FI, INVARIANT-RD-via-regulator-dressing, DEPENDENT} is "structurally weaker" via three reasons (workshop lines 350-358): (1) loss of symmetry; (2) loss of the Mellin-pole axis; (3) layer-functor F mismatch. I agree with NONE of these as decisive arguments. Counter-evidence:

**Counter-(1) — symmetry argument is non-binding.** connes claims "DEPENDENT class would lack its FI/RD subdivision". But algebra-DEPENDENT functionals DO admit an FI/RD-style split — the structural counterpart on the state-pair side. State-pair functionals like the Connes distance `d_C(ω_1, ω_2) = sup_{a ∈ A_h, ‖[D, π(a)]‖ ≤ 1} |ω_1(a) − ω_2(a)|` evaluate to regulator-class-dependent numerical values when the spectral triple's regulator is varied (full M_n(ℂ) Connes distance regulator-divergence is the W1b-6 calibration instance — the regulator-class divergence IS the calibration witness). The proper symmetric extension is the 3-class trichotomy I actually propose (workshop seed line 42, clause d): {INVARIANT-FI-strict, INVARIANT-MIXED-via-regulator-dressing, DEPENDENT}, which is a 3-class partition NOT because DEPENDENT lacks subdivision but because INVARIANT-MIXED is the structurally interesting sub-class that is not captured by either pure-FI or pure-DEPENDENT. xi²_0(R) is the canonical example.

**Counter-(2) — Mellin-pole axis preservation.** connes claims my 3-class would "discard the W-9 RULE-3 Pole-Scope" axis. False. The 3-class partition I propose operates ON THE algebra-axis only; it does NOT replace the Mellin-pole axis. The full §VII.U.2 partition under my proposal is (algebra-axis ∈ {INVARIANT-FI, INVARIANT-MIXED-via-regulator-dressing, DEPENDENT}) × (Mellin-pole ∈ {s=3, s=4}) = 3 × 2 = 6 corner cells (currently 4 are populated; 2 are open). The Mellin-pole axis MANDATORY-K=4 status (S88 W7a-72; `epistemic-discipline.md §"Pole-Scope sub-clause"`) is preserved unchanged. Pole-Scope and FI/RD are orthogonal axes; both can be tracked.

**Counter-(3) — layer-functor F mismatch is question-begging.** connes claims "FI/RD lives at the methodology / publication-precision layer (S82 W-3 RULE-3 is a citation discipline on numerical evaluation; `regulator-pin-discipline.md` is the audit-leg image)". This is precisely the conflation Re:C1's MISSED block addressed: the publication-precision discipline IS the audit-leg image of the regulator-class atlas axis under F, NOT the substrate-IS axis. The substrate-IS axis is the F_inv member's behavior under regulator-class span (FI = span_{A_5}(F) = 1; RD = span_{A_5}(F) ≠ 1). A Class-8.2 violation in publication-precision discipline (round-figure cited where Sage-exact required) is a methodology-layer audit failure; it does NOT propagate as an algebra-axis re-classification at the substrate-physics layer. I agree with that asymmetric propagation. But the substrate-physics layer ALSO has a regulator-class atlas axis, distinct from the algebra-axis and distinct from the methodology-layer publication-precision discipline.

**Substitution chain — proper 3-class refinement on the F_inv side**:

```
Definitions (per S82 W-3 RULE-3 + §VII.K-DUAL FI/RD/MIXED at registry line 4108):
  A_5            := {ζ, SDW, cutoff_sqrt, anomaly, Zubarev}        (canonical 5-atlas)
  span_{A_5}(F)  := max_R F(R) / min_R F(R)                         for R ∈ A_5

  Refined algebra-axis 3-class partition on F_inv:
    INVARIANT-FI-strict      ⇔ F ∈ F_inv  AND  span_{A_5}(F) = 1
    INVARIANT-MIXED-via-RD   ⇔ F ∈ F_inv  AND  span_{A_5}(F) ≠ 1
                              AND ∃ S ⊂ A_5 with span_S(F) = 1     (FI on a sub-atlas)
    INVARIANT-RD-strict      ⇔ F ∈ F_inv  AND  span_{A_5}(F) ≠ 1
                              AND ∀ S ⊂ A_5 (|S|≥2), span_S(F) ≠ 1  (no FI sub-atlas)

  DEPENDENT class is NOT subdivided by this refinement (per Counter-(1)
  the DEPENDENT-side regulator-class span is captured by the W1b-6 calibration
  in the K=3 corpus; I do NOT propose subdivision on the DEPENDENT side).

Substitutions (canonical examples):
  Example-A: Mellin-Dirichlet identity (W1b-6 Corner I instance, registry line 12923):
    F = identity statement Σ_k m_k λ_k^{-2s} = Res-form
    parse-tree: no π(a) ⇒ INVARIANT
    span_{A_5}(F) = 1   (an IDENTITY between two computations of the SAME quantity;
                          regulator-INDEPENDENT BY CONSTRUCTION; this is the
                          structural reason §VII.U.1 was promoted PASS at rel_diff
                          = 0e+00 across atlas members)
    ⇒ INVARIANT-FI-strict.

  Example-B: Seeley-DeWitt coefficient a_n^{R} (§VII.U.2 clause (a) calibration; line 12913):
    F = a_n^{R}  (regulator-class-tagged Seeley-DeWitt coefficient)
    parse-tree: no π(a) ⇒ INVARIANT
    span_{A_5}(F) ≠ 1   (a_n's numerical value depends on R; this is the structural
                          reason regulator-pin-discipline.md MANDATES the {R} superscript)
    ∃ sub-atlas S of size 1 with span_S(F) = 1 trivially (single-element atlas)
    But for |S| ≥ 2 generically span_S(F) ≠ 1
    ⇒ INVARIANT-RD-strict for atlas-cardinality-≥2 readings.

  Example-C: xi^2_0(R) (§VII.AH ANCHOR-2; this workshop's central case):
    parse-tree: no π(a) ⇒ INVARIANT
    span_{F_2}(xi^2_0) = 1                       (Re:C2 Step 1)
    span_{A_5}(xi^2_0) = 13.1641                 (Re:C2 Step 2; xi^2_0 ∈ {1.036, ..., 13.642})
    ∃ S = F_2 ⊂ A_5  with span_S(xi^2_0) = 1
    ⇒ INVARIANT-MIXED-via-RD.

Simplification:
  Refined 3-class partition on F_inv:
    INVARIANT-FI-strict     : Mellin-Dirichlet identities (§VII.U.1; W1b-6 Corner I anchor)
    INVARIANT-MIXED-via-RD  : F_2-conditional ratios (§VII.AH ANCHOR-2 = xi^2_0)
    INVARIANT-RD-strict     : Seeley-DeWitt coefficients a_n^{R} on atlas-≥2 readings
                              (the §VII.U.2 clause (a) calibration corpus)

  These three sub-classes are STRUCTURALLY DISTINCT, not just numerically distinct.
  - FI-strict is an algebraic-identity statement (regulator-INDEPENDENT BY CONSTRUCTION)
  - MIXED-via-RD is a sub-atlas-conditional statement (FI on F_2 ∧ RD on A_5\F_2)
  - RD-strict is a regulator-class-tagged numerical statement (RD generically; FI vacuously
    on |S|=1 readings)

Direction:
  The 3-class refinement IS structurally needed because:
   (a) it separates Mellin-Dirichlet identity (FI-strict; canonical Corner I anchor)
       from Seeley-DeWitt-RD parse-tree-INVARIANT functionals (RD-strict; the
       §VII.U.2 clause (a) corpus). Connes's framing collapses both into "Corner I"
       which is the actual structural ambiguity this refinement resolves.
   (b) it identifies INVARIANT-MIXED-via-RD as the natural placement for xi^2_0 — a
       structurally MIXED quantity that is neither pure-FI nor pure-RD but is sub-
       atlas-conditional. This is precisely the structural class the §VII.K-DUAL
       trichotomy registers at registry line 4108 ("MIXED" sub-tag).
   (c) it preserves K=3 saturation on the (INVARIANT vs DEPENDENT) coarse axis —
       the K-counter is NOT recalibrated by the refinement because the K-counter's
       calibration corpus paired INVARIANT vs DEPENDENT on each instance, not
       FI vs RD vs MIXED sub-classes.

Conclusion:
  The 3-class refinement on F_inv is STRUCTURALLY ORTHOGONAL to the K=3 algebra-axis
  K-counter (the K-counter's MANDATORY status is unchanged). The refinement adds
  resolution within the INVARIANT class for cases like §VII.AH ANCHOR-2 where the
  parse-tree-only reading misses the sub-atlas-conditional structure. Connes's C4
  Step 3 ("axes are ORTHOGONAL") is correct; my 3-class refinement is the operational
  realization of that orthogonality on the INVARIANT side, not a replacement for the
  algebra-axis K-counter.
```

**MISSED**: connes C4 Step 3 (workshop lines 313-322) acknowledges the 2 × 3 = 6 sub-cells but immediately declines to refine the partition: "this is NOT a refinement of the algebra-axis K-counter — the K-counter's MANDATORY-K=3 status was promoted on the ALGEBRA-AXIS alone, and the K=3 saturation does NOT depend on FI/RD distinctions" (workshop lines 325-327). I agree the K-counter saturation is unchanged. But that does NOT settle whether the §VII.U.2 partition IS structurally complete on the registry-anchor-discriminator axis. The K-counter and the registry-anchor partition are different audits: the K-counter discharges the MANDATORY status of orthogonality between the two coarse classes; the registry-anchor partition discharges the FORBIDDEN-cross-corner-co-primary discipline of clause (f). My 3-class refinement targets the second audit, not the first.

**EMERGES**: A "lattice" reading. The §VII.U.2 4-corner partition is the COARSE projection of a finer 3 × 2 × 3 = 18-cell partition onto the (algebra-axis, Mellin-pole) plane. The §VII.K-PROP CC-5 propagation identity (`span_R(O) = ∏_k span_R(f_{n_k}^R)^{|p_k|}`; my Lizzi-signature theorem at registry line 8976) is the structural identity governing transitions between FI / MIXED / RD sub-classes under composition. §VII.K-PROP-COMPOSITION (registry line 9272) is the lattice-join rule. Both are structural §VII THM entries. They cannot be re-classified as evaluation-layer tags without invalidating the §VII registry status they already hold.

#### Re: C5 — Cross-Cutting Observations

**AGREE (this is the convergence point of the workshop)**: connes's C5 thesis — "the parse-tree decision procedure of §VII.U.2 clause (e) and the FI/RD trichotomy of S82 W-3 RULE-3 are **structurally orthogonal axes operating at distinct layers of the layer-functor F**" (workshop line 377) — is correct AT THE STRUCTURAL-ORTHOGONALITY LEVEL. The two axes are NOT equivalent classifications, NOT refinements of each other, and NOT in conflict. C5's 3 structural reasons (workshop lines 419-423) are valid:

1. **Regulator-pin discipline**: I AGREE — Seeley-DeWitt coefficients are CANONICAL F_inv yet RD across regulator class (per §VII.U.2 clause (a) calibration corpus, registry line 12913). If FI/RD were a refinement of algebra-INVARIANT/DEPENDENT in the strong sense (FI ⊂ INVARIANT, RD ⊂ DEPENDENT), the §VII.U.2 calibration corpus would self-contradict. It does not, because FI/RD is on a different axis.

2. **CM-1995 §III.4 dim-spectrum residue formula**: I AGREE — the formula is regulator-INDEPENDENT at the symbolic level (Borel-functional-calculus on D²) yet its numerical value is regulator-CLASS-DEPENDENT (W7c WP §W7c-167 line 693 obs1 confirms: M_R(s=−1) ∈ {0.158101, 0.158101, 0.111003, 0.031847, 0.154446} across A_5). The CM-1995 formula IS the bridge demonstrating parse-tree-INVARIANT can simultaneously be RD at the evaluation layer.

3. **Layer-functor F audit-leg correspondence**: I AGREE — F preserves PRU-class invariants. A Class-8.2 violation in FI/RD discipline (round-figure cited where Sage-exact is required, e.g., Ω_GW^(C) `1e-57` vs `8.299e-58` per `regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW Regulator-Class Values"`) does NOT propagate as an algebra-axis re-classification at the substrate-physics layer. The PRU-class taxonomy is preserved under F precisely BECAUSE the axes at different layers are distinct.

**DISAGREE (refinement of layer-assignment)**: My Re:C1 MISSED block stated FI/RD lives at the substrate-IS observable layer (the regulator-class atlas axis), with the publication-precision discipline as its audit-leg image under F. C5 places FI/RD entirely at the methodology layer. The two readings differ on whether the regulator-class atlas is substrate-IS or methodology-IS. Empirical resolution: the §VII.K-DUAL FI-Duality Theorem (registry line 4108) and the §VII.K-PROP CC-5 propagation identity (registry line 8976) and §VII.K-PROP-COMPOSITION lattice-join rule (registry line 9272) are all registered §VII STRUCTURAL THM entries. Their substrate-IS status is the registry's commitment, not a methodology-layer publication discipline. Reconciliation: the FI/RD AXIS is substrate-IS at the regulator-class atlas level (where §VII.K-DUAL and §VII.K-PROP live); the FI/RD CITATION DISCIPLINE (Sage-exact rationals; round-figure forbidden; mnemonic-vs-exact) is the methodology-layer audit-leg image. C5 conflated the axis with its audit-leg image. The convergence is preserved by separating these two roles of "FI/RD".

**EMERGES (the workshop's structural verdict)**: The structural-orthogonality reading rescues BOTH axes simultaneously. Concrete corollary:

| Layer | What is registered | Substrate or audit-leg |
|:------|:-------------------|:-----------------------|
| substrate-IS, axis 1 (operator-algebraic) | parse-tree π(a) test → F_inv vs F_dep → §VII.U.2 4-corner partition | substrate-IS (§VII.U.2 lines 12947-12949 verbatim) |
| substrate-IS, axis 2 (Mellin-pole) | s ∈ {s=3, s=4} (substrate-distance pole) → MANDATORY-K=4 (S88 W7a-72) | substrate-IS |
| substrate-IS, axis 3 (regulator-class atlas) | span_{A_5}(F) ∈ {1, ≠1} → FI / MIXED / RD → §VII.K-DUAL + §VII.K-PROP | substrate-IS at the REGULATOR-CLASS ATLAS layer (registered §VII THM) |
| methodology layer | publication-precision (Sage-exact rationals; round-figure forbidden; regulator-pin tagging) | audit-leg image of axis 3 under F |
| audit layer | `_a_n_regulator_pin_audit.py` + `regulator-pin-discipline.md` | audit-leg image of axis 3 |

The three substrate-IS axes are pairwise structurally orthogonal. §VII.U.2 currently tracks (axis 1 × axis 2) as the 4-corner partition; axis 3 enters as a separate registered §VII.K-* family of theorems and as an axis-tag on individual corner-cell entries. Whether the §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary discipline extends ACROSS the axis-3 boundary (so that ANCHOR-1 ∈ axis-3-RD and ANCHOR-2 ∈ axis-3-MIXED triggers FORBIDDEN-cross-corner) is the workshop's open structural question. C3 reads it as NOT triggering (axis-3 is "evaluation-layer tag, not partition axis"); I read it as triggering (axis-3 is registered §VII THM family, not evaluation-layer tag). This is the residual disagreement Round 2 will need to adjudicate.

**Substrate-IS framing reconciliation (per `phononic-framing.md §"IS Space, Not IN Space"`)**: connes's C5 substrate-IS reading at workshop lines 390-400 is correct as far as it goes. Its extension to the regulator-class atlas axis: the substrate `(A_K, H_K, D_K)` IS the spectral triple, and the Jensen-deformation manifold τ_fold IS substrate-IS at Level 2 (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). Analogously, the regulator-class atlas A_5 = {ζ, SDW, cutoff_sqrt, anomaly, Zubarev} IS the substrate's own structural-complexity partition under regulator-class span — observers do not measure FI/RD "in" any container; the substrate's spectral content under regulator-class scan IS FI / MIXED / RD at axis 3. Direction-of-explanation is preserved on all three axes substrate → emergent.

### Part 2: Original Analysis

#### L1: FI/RD trichotomy structural orthogonality to parse-tree

**Thesis**: The FI/RD trichotomy operates at a STRUCTURAL AXIS that is orthogonal to (a) the parse-tree π(a)-axis (operator-algebraic, §VII.U.2 clause (e)) and (b) the Mellin-pole axis (substrate-distance, W-9 RULE-3 Pole-Scope). The orthogonal axis is the **regulator-class atlas axis**: span_{A_5}(F) under variation of the regulator class R ∈ A_5 = {ζ, SDW, cutoff_sqrt, anomaly, Zubarev}. This axis is substrate-IS at the regulator-class atlas layer (§VII.K-DUAL + §VII.K-PROP are registered §VII THM entries), NOT exclusively a methodology-layer publication discipline (the publication discipline is the audit-leg image under F). Three structural sub-classes need pinning on the F_inv side, where the parse-tree-only reading is structurally underspecified.

### Three structural sub-classes (per Re:C4 substitution chain; restated as §VII.K-DUAL extension)

- **FI-strict** ⇔ F ∈ F_inv ∧ span_{A_5}(F) = 1
  *Algebraic-identity statement; regulator-INDEPENDENT BY CONSTRUCTION.* Canonical example: Mellin-Dirichlet identity (§VII.U.1; W1b-6 Corner I anchor; PASS rel_diff = 0e+00 at L_max=12). Why FI-strict: the identity expresses the SAME quantity computed two ways, so cross-class span = 1 by definition of "identity".

- **MIXED-via-regulator-dressing** ⇔ F ∈ F_inv ∧ span_{A_5}(F) ≠ 1 ∧ ∃ S ⊂ A_5 (|S| ≥ 2) with span_S(F) = 1
  *Sub-atlas-conditional statement; FI on a sub-atlas, RD on its complement.* Canonical example: §VII.AH ANCHOR-2 = xi²_0(R) (Re:C2 substitution chain Step 3). Why MIXED-via-regulator-dressing: the M_F2 normalizer is a CLASS-SELECTIVE projector that exact-cancels on F_2 = {ζ, SDW} and leaves CLASS-RESIDUE on A_5 \ F_2.

- **RD-strict** ⇔ F ∈ F_inv ∧ span_{A_5}(F) ≠ 1 ∧ ∀ S ⊂ A_5 (|S| ≥ 2) span_S(F) ≠ 1
  *Regulator-class-tagged numerical statement; RD generically.* Canonical example: Seeley-DeWitt coefficient `a_n^{R}` per §VII.U.2 clause (a) registry line 12913 ("Seeley-DeWitt moments `a_n^{regulator}`, ζ-residues..."). Why RD-strict: per `regulator-pin-discipline.md §"Rule"`, every Seeley-DeWitt coefficient `a_n` MUST carry a regulator-class superscript precisely because its numerical value depends on R; no cross-class sub-atlas saturates span_S = 1.

The DEPENDENT side of the algebra-axis is captured by the §VII.U.2 clause (b) calibration ("state-pair functionals `F_dep(ω_1, ω_2; A) = ‖[D, π(A)]‖_op`"; registry line 12915) and is NOT subdivided by this refinement; the K=3 corpus (W1b-6, S-2, W-2 — workshop lines 280-291) pairs INVARIANT with DEPENDENT one-to-one and the DEPENDENT-side regulator-class behavior is captured at the calibration-instance level (full M_n(ℂ) Connes distance regulator-divergence is the W1b-6 instance).

### S82 W-3 calibration corpus as evidence at the substrate-IS observable layer

The S82 W-3 RULE-3 mnemonic-vs-exact-ratio rule (`math-scripts.md §"Mnemonic-vs-exact ratio discipline"`) was promoted on concrete numerical structural failures, NOT on a publication-typesetting convenience. Two calibration instances at the substrate-IS observable layer:

**Instance-1 — Ω_GW^(C) regulator-class value** (per `regulator-pin-discipline.md §"Extension: Sage-Exact Rationals for Ω_GW Regulator-Class Values"`, T1-15):

| Quantity | Round-figure (FORBIDDEN) | Sage-exact (REQUIRED) | OOM gap |
|:---------|:-------------------------|:----------------------|:--------|
| Ω_GW^(C) at LISA frequency | `1e-57` | `8.299e-58` (W13-2.Ω verdict, exact) | ~1× factor; ~0.08 OOM |
| Ω_GW^(A) / Ω_GW^(C) split | `~45 OOM` | `47.081 OOM` (Sage-verified) | ~2 OOM in propagated split |

The `1e-57` round-figure UNDERSTATES Ω_GW^(C) = 8.299e-58 by ~10× and propagates to a ~2 OOM distortion of the (A)/(C) split when used in downstream falsifier-design citations. The (A)-class and (C)-class are STRUCTURALLY DISTINCT regulator classes (companion-null vs full-cosmological-coupling); the ~2 OOM split is a substrate-IS prediction. The round-figure form is not just imprecise typesetting — it would mis-classify the substrate's discrimination strength.

**Instance-2 — σ-reduction-ratio mnemonic-vs-exact discrepancy at S86 W-3**:

| Quantity | Mnemonic-form (FORBIDDEN) | Sage-exact (REQUIRED) | Relative deviation |
|:---------|:--------------------------|:----------------------|:--------------------|
| `1/c_sub` σ-reduction | `1/c_sub = 500/1119 = 0.4468` | `16577/31705 = 0.5229` | 14.54% understatement |

**Substitution chain — why the mnemonic-vs-exact deviation is substrate-IS structural, not publication-precision** (verbatim from `math-scripts.md §"Mnemonic-vs-exact ratio discipline"` calibration corpus):

```
Definitions (S86 W-3 R3-A Convergence #1, lines 2442-2470):
  c_sub               := M_Pl_eff²(k_pivot) / M_Pl_eff²(0)        (substrate compaction factor)
  Path-H              := reference quantity, INVARIANT under HypA/HypB switching
  Path-C              := test quantity, SHIFTS under HypA/HypB switching
  σ-reduction-ratio   := σ_HypB / σ_naive

Substitutions:
  σ-reduction (mnemonic) = 1/c_sub                  (assumes BOTH numerator and
                                                     denominator scale by 1/c_sub)
  σ-reduction (exact)    = 16577/31705              (only denominator (Path-C) shifts;
                                                     Path-H invariant; ratio bounded
                                                     below 1/c_sub)

Simplification:
  1/c_sub          = 500/1119            = 0.446827
  16577/31705                            = 0.522884
  rel_dev          = |0.5229 - 0.4468| / 0.5229 = 14.54%

Direction:
  σ-reduction-mnemonic  <  σ-reduction-exact     (because Path-H invariance bounds the
                                                  ratio below 1/c_sub from above)
  ⇒ The mnemonic UNDERSTATES the σ-reduction by 14.54%.

Conclusion (per `math-scripts.md §"Mnemonic-vs-exact ratio discipline"`):
  "If W-3 had pinned the σ-reduction at 0.4468 (mnemonic) instead of 0.5229 (exact),
   the LiteBIRD discrimination band [1.6666σ, 2.7776σ] would have been mis-published
   as [1.42σ, 2.37σ] — a 14.5% systematic understatement of the framework's
   discrimination strength. The structurally-exact form is the substrate's prediction;
   the mnemonic is a calculator-aid only."
```

This is a direct numerical structural failure at the substrate-IS observable layer. The exact and mnemonic forms are NOT different presentations of the same prediction; they are DIFFERENT predictions that disagree on the substrate's σ-discrimination band by 14.54%. The reason for the asymmetry — Path-H invariant; only Path-C shifts; ratio bounded below `1/c_sub` from above — is a structural property of the regulator-class atlas's interaction with HypA/HypB scenarios.

### Why this matters: the §VII.U.2 partition is incomplete on the registry-anchor-discriminator axis

The two calibration instances above demonstrate that FI/RD bites at the substrate-IS observable level. Concretely:
- The Ω_GW^(C) substrate prediction is regulator-class-tagged (the C class IS a regulator-class). FI/RD discipline forces Sage-exact citation.
- The σ-reduction-ratio is a substrate-IS prediction with a structural reason for being NOT-FI on the full atlas.

A registry that tracks substrate-IS observables MUST track these distinctions structurally. §VII.K-DUAL (registry line 4108) and §VII.K-PROP (registry line 8976) ALREADY DO — they are registered §VII THM entries. The §VII.U.2 4-corner partition does NOT, because it only covers axes 1 and 2.

The structural-orthogonality of the three axes (parse-tree; Mellin-pole; regulator-class atlas) means each axis contributes an INDEPENDENT registry-anchor-discriminator. Connes's Re:C5 reading agrees on the orthogonality but places axis 3 at the methodology layer; my reading places axis 3 at the substrate-IS layer (with publication-precision discipline as its audit-leg image under F). Both readings preserve the K=3 algebra-axis K-counter saturation. The disagreement that remains is whether §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary discipline applies UNIFORMLY across axis-3 boundaries (Re:C3 substitution chain reading (b)) or NOT (connes C3 reading (a)).

#### L2: Numerical regulator-class-dependence of xi_per_class — what it tells us

**Data (verbatim from W7c WP §W7c-167 line 693)**:

```
xi_per_class = [13.642473, 13.642473, 9.578354, 2.748038, 13.327089]
order        = ['zeta',     'SDW',       'cutoff_sqrt', 'anomaly',  'Zubarev']
```

with the canonical scalar `xi_E_GGE_inv = 13.642473425596` (matches S86 branch-iv-canonical anchor bit-identically per W7c WP line 693), and the within-F_2-branch unitarity residuals `cc_zeta_residual = cc_sdw_residual = 1.302078e-16` (machine-ε), and the F_2 identity residual `|M_ζ − M_SDW| = 0` (exact) at s_slot = -1, L_max = 10. These values are the spectral-side cross-reviewer's numerical substantiation of obs1.

### What the numerical structure shows: the M_F2 normalizer is class-selective by construction

**Substitution chain — F_2 cancellation is EXACT; off-F_2 retains class-residue**:

```
Definitions (per §VII.AH ANCHOR-2 spec, registry line 15417 + 15425):
  xi^2_0(R) := xi_E_GGE_inv · M_R / M_F2                    (with M_F2 := M_R at R = ζ)

  At obs1 s_slot = -1, the substrate evaluation yields M_R 5-vector at s=−1:
    M_R(s=-1)_atlas = [M_ζ, M_SDW, M_cutoff, M_anomaly, M_Zubarev]
                    = [0.158101, 0.158101, 0.111003, 0.031847, 0.154446]
                    (W7c WP line 693, VERBATIM)

  M_F2 = M_ζ = 0.158101                                      (F_2 normalizer choice)

Substitutions (per-class evaluation):
  xi^2_0(ζ)       = xi_E · M_ζ      / M_F2 = 13.642473 · 0.158101 / 0.158101 = 13.642473
  xi^2_0(SDW)     = xi_E · M_SDW    / M_F2 = 13.642473 · 0.158101 / 0.158101 = 13.642473
  xi^2_0(cutoff)  = xi_E · M_cutoff / M_F2 = 13.642473 · 0.111003 / 0.158101 = 9.578354
  xi^2_0(anomaly) = xi_E · M_anom   / M_F2 = 13.642473 · 0.031847 / 0.158101 = 2.748038
  xi^2_0(Zubarev) = xi_E · M_Zub    / M_F2 = 13.642473 · 0.154446 / 0.158101 = 13.327089

  These values match W7c WP line 693 xi_per_class verbatim (cross-check PASS).

Simplification (sub-atlas FI/RD analysis):
  span_{F_2}(xi^2_0)  = max(13.642473, 13.642473) / min(13.642473, 13.642473) = 1.0  EXACT
                       (F_2 = {ζ, SDW}: cancellation EXACT; consistent with
                        F_2 identity residual |M_ζ − M_SDW| = 0 at W7c WP line 693)

  span_{A_5}(xi^2_0)  = max(13.642473, 13.327089, 9.578354, 2.748038)
                      / min(13.642473, 13.327089, 9.578354, 2.748038)
                     = 13.642473 / 2.748038
                     = 4.964790                              (factor 4.96× spread)

  span_{A_5\F_2}(xi^2_0) = max(13.327089, 9.578354, 2.748038)
                         / min(13.327089, 9.578354, 2.748038)
                        = 13.327089 / 2.748038
                        = 4.849980                            (factor 4.85× spread)

Direction:
  span_{F_2}(xi^2_0)      = 1.0       ⇒ FI on F_2.
  span_{A_5\F_2}(xi^2_0)  = 4.85      ⇒ RD on A_5 \ F_2 (off-F_2).
  span_{A_5}(xi^2_0)      = 4.96      ⇒ RD on the full atlas.

  ⇒ xi^2_0(R) at s=−1 evaluation is FI-PARTIAL: FI on F_2, RD on A_5 \ F_2.
  ⇒ Same structural reading as connes's C2 s=3 Sage-QQ table (Re:C2 Step 3),
    with different numerical residues per pole-scope but identical structural class.

Conclusion:
  At obs1 (s=−1), the M_F2 normalizer cancels EXACTLY on F_2 and leaves CLASS-RESIDUE
  on the off-F_2 atlas members. The factor 4.85× spread on the off-F_2 sub-atlas IS
  the M_F2 normalizer's class-selectivity signature. Combined with the C2 s=3 Sage-QQ
  reading (factor 13.16× spread; Re:C2 Step 2), the FI-on-F_2 / RD-on-off-F_2 structure
  is preserved across pole transitions — it is a STRUCTURAL property of the M_F2
  normalizer's interaction with the regulator-class atlas, not a pole-specific artifact.
```

### What §VII.AH must declare: F_2-cancelled vs full atlas trace reading

The §VII.AH ANCHOR-2 registry text (registry lines 15417-15418) cites `xi²_0(R) = xi_E_GGE_inv · M_R(s=3) / M_F2(s=3)` and pins F_2 = {ζ, SDW} as the K-invariant identity sub-atlas. The text does NOT declare which numerical reading the registry is committed to:

- **Reading 1 — F_2-restricted reading**: ANCHOR-2 is xi²_0 evaluated only at R ∈ F_2 = {ζ, SDW}. Then xi²_0(F_2) = {13.642473, 13.642473} and the registered value is FI-on-F_2 (span = 1, EXACT). The off-F_2 residues do not enter the registered theorem; they appear as diagnostic-only.
- **Reading 2 — Full-atlas trace reading**: ANCHOR-2 is xi²_0 evaluated across R ∈ A_5 = {ζ, SDW, cutoff_sqrt, anomaly, Zubarev}. Then xi²_0(A_5) = {13.642, 13.642, 9.578, 2.748, 13.327} and the registered value is FI-PARTIAL (span_{F_2} = 1; span_{A_5} = 4.85-13.16 depending on pole). The off-F_2 residues ARE part of the registered theorem.

The §VII.AH §"Per-branch protection of A_s ledger" clause (d) text says "Within a single regulator branch (e.g., F_2-class via zeta scheme at L_max=3)" (registry line 15433). This phrasing is consistent with Reading 1 (F_2-restricted) — the per-branch protection is the registered statement; cross-class is "the cosmological analog of unitarity (|α|² − |β|² = 1) realized at the spectral-functional level within a single regulator class". Under Reading 1, the §VII.AH theorem is FI on its registered scope, and the off-F_2 numerical residues at obs1 are diagnostic-only (they validate the F_2-uniqueness clause (e) by showing K-invariance fails at order O(1) on every superset).

But Clause (a) "Spectral 3-class partition (lizzi L2)" (registry line 15427) explicitly cites the M_R(s=3) 5-tuple `(1.581e-1, 1.581e-1, 1.201e-2, 1.110e-1, 3.185e-2)` for ALL FIVE atlas members — that is consistent with Reading 2 (full-atlas trace). The 924×/298×/798× margins in clause (e) (registry line 15435) explicitly reference the off-F_2 residues. So Clause (a) and Clause (e) read ANCHOR-1 as full-atlas; Clause (b) and Clause (d) read ANCHOR-2 as F_2-restricted within a single regulator class. This asymmetric reading IS coherent — it is exactly what the SOURCE-DOUBLE-CITE-CO-PRIMARY structure encodes: ANCHOR-1 is the K-invariance-failure premise on the full atlas; ANCHOR-2 is the per-branch protection conditional on F_2 selection.

### What this tells us about the §VII.AH narrowing question

Re:C2 + Re:C3 substitution chains established: ANCHOR-2 is FI on F_2 and RD on A_5 \ F_2 = MIXED-via-regulator-dressing on the regulator-class atlas axis. Under Reading 1 (F_2-restricted, consistent with clause (b)+(d) text), the §VII.AH registered observable IS FI on its registered scope, and the §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary trigger is NOT activated by the obs1 numerical evidence — because the off-F_2 residues are not part of the registered theorem. Under Reading 2 (full-atlas, consistent with clause (a)+(e) text), ANCHOR-2 inhabits the MIXED regulator-class-atlas-axis cell and the trigger IS activated.

The §VII.AH narrowing remediation route I propose at Re:C3 is:

**§VII.AH narrowing entry text proposal**: append a Corrigendum 5 to §VII.AH (after L-CR3.3 amendment to clause (e)) explicitly disambiguating the registered scope of ANCHOR-2:

> *Corrigendum 5 (lizzi-spectral-functional W-26)*: ANCHOR-2 = xi²_0(R) is registered at the F_2-restricted scope `R ∈ F_2 = {ζ, SDW}`, where span_{F_2}(xi²_0) = 1 EXACT (F_2 cancellation; FI-on-F_2 numerical evidence at obs1 = 13.642473 / 13.642473 and at C2 Sage QQ = 1581/1581). The off-F_2 numerical residues `xi²_0(cutoff) = 9.578354`, `xi²_0(anomaly) = 2.748038`, `xi²_0(Zubarev) = 13.327089` (W7c WP §W7c-167 line 693, s=−1 evaluation) are diagnostic-only — they substantiate clause (e)'s K-invariance failure at order O(1) on supersets but are NOT part of the registered ANCHOR-2 theorem. Under this F_2-restricted scope, ANCHOR-2 is (algebra-axis = INVARIANT, Mellin-pole = s=3, regulator-class atlas = FI-on-F_2). SOURCE-DOUBLE-CITE-CO-PRIMARY admissibility is preserved on the §VII.U.2 4-corner partition (both anchors Corner I) AND on the regulator-class atlas axis (both anchors FI on their registered scope: ANCHOR-1 is RD on the full atlas A_5 by §VII.U.2 clause (a) calibration corpus tagging; ANCHOR-2 is FI on its registered F_2-restricted scope; the asymmetric scoping is the SOURCE-DOUBLE-CITE structural content — V supplies the full-atlas-K-invariance-failure premise; C supplies the F_2-restricted-protection theorem conditional on V).*

This narrowing entry preserves §VII.AH STAGE-1-CANDIDATE status (SOURCE-DOUBLE-CITE-CO-PRIMARY admissible under the asymmetric scoping reading) while explicitly addressing the regulator-class atlas axis. It does NOT require §VII.U.2 partition expansion; the 4-corner partition stays canonical with the regulator-class atlas axis registered as a separate §VII.K-* family. The Corrigendum 5 is an in-place §VII.AH text addition, not a partition restructure.

#### L3: Questions for connes

**Q-L1 — Where in §VII.U.2 clause (e) parse-tree decision text is the regulator-class atlas axis ruled out as a structural test?**

The §VII.U.2 clause (e) text at registry line 12930 reads: *"`F` belongs to algebra-INVARIANT iff its symbolic form contains ONLY traces / spectral moments / `g(λ_k)` evaluations and no `π(a)` operator-algebra references; `F` belongs to algebra-DEPENDENT iff its symbolic form contains at least one `π(a)` or `[D, π(a)]` reference. The decision procedure is finite and operates at parse-tree level, NOT at numerical evaluation level — this makes it regulator-independent (same parse-tree decision under cutoff, ζ, Pauli-Villars, Mellin regulators)..."*

The clause asserts that the parse-tree decision is regulator-INDEPENDENT (same classification across regulators); it does NOT assert that the regulator-class atlas axis is irrelevant as a registry-anchor-discriminator. The clause's "regulator-INDEPENDENCE" is a property of the parse-tree test itself, not a denial of the existence of a separate regulator-class atlas axis. Specifically: do you read clause (e) as STRUCTURALLY EQUIVALENT to "the regulator-class atlas axis is not a registry-anchor-discriminator at the §VII level"? If yes, how do you reconcile that reading with §VII.K-DUAL (registered §VII THM at registry line 4108) and §VII.K-PROP (registered §VII THM at registry line 8976), which ARE registry-level structural theorems on the regulator-class atlas axis? If no, then the parse-tree decision is necessary-but-not-sufficient for the algebra-axis classification, and the §VII.AH narrowing question (Re:C3) remains open.

**Q-L2 — For Seeley-DeWitt coefficients (canonical F_inv per parse-tree, but provably RD across regulator class), is the algebra-axis classification "INVARIANT" or "RD"? Either answer breaks the layer-functor F separation.**

Per §VII.U.2 clause (a) (registry line 12913), Seeley-DeWitt moments `a_n^{regulator}` are CANONICAL examples of `F_inv` (algebra-INVARIANT family). Per `regulator-pin-discipline.md §"Rule"`, the same `a_n` MUST carry a regulator-class superscript precisely because its numerical value depends on R. Your C2 line 174 acknowledges this: *"All five entries in the §VII.U.2 clause-(a) calibration corpus are regulator-class-tagged Seeley-DeWitt coefficients per `regulator-pin-discipline.md`; their numerical value is regulator-class-dependent BY CONSTRUCTION (the regulator-pin tagging discipline EXISTS because of this)."*

Two readings:
- Reading-A: Seeley-DeWitt coefficients are algebra-INVARIANT (parse-tree-INVARIANT) AND RD-strict on the regulator-class atlas axis (Re:C4 substitution chain Example-B). Under this reading, the algebra-axis classification and the FI/RD classification are STRUCTURALLY ORTHOGONAL at the substrate-IS layer (my Re:C5 reading).
- Reading-B: Seeley-DeWitt coefficients are algebra-INVARIANT only (per §VII.U.2 clause (a) line 12913); the FI/RD axis is "evaluation-layer tag" (your C5 reading at workshop line 419-420). Under this reading, the regulator-class superscript on `a_n^{R}` is a publication-precision discipline, not a substrate-IS axis.

Reading-B is your C5 position. But Reading-B implies the §VII.K-DUAL FI-Duality Theorem (registered §VII THM, registry line 4108) is mis-classified — it should be a methodology rule, not a §VII THM. Likewise §VII.K-PROP (registry line 8976). Are you committing to that registry re-classification? If not, Reading-A is forced, and the FI/RD axis is substrate-IS — confirming my Re:C1 MISSED block.

**Q-L3 — If §VII.AH ANCHOR-2 is FI-PARTIAL (FI-on-F_2 ∧ RD-on-off-F_2; Re:C2 + L2 substitution chains), which Corner does the registry text declare and what's the explicit narrowing?**

Three concrete options (Re:C3 routes (a), (b), (c) corresponding to your C6 Q4 (a), (b), (c)):

- Route-(a) **Corrigendum 5 narrowing**: append the L2 §"§VII.AH narrowing entry text proposal" Corrigendum 5 declaring ANCHOR-2 registered at F_2-restricted scope only; off-F_2 numerical residues are diagnostic-only. SOURCE-DOUBLE-CITE-CO-PRIMARY preserved under asymmetric scoping (V is full-atlas-K-invariance-failure premise; C is F_2-restricted-protection theorem conditional on V). §VII.U.2 partition stays 4-corner.

- Route-(b) **§VII.U.2 partition expansion**: rule-file edit promoting the §VII.U.2 partition from 4-corner to 4-corner × 3-class-FI/MIXED/RD = 12-cell. K-counter recalibration consequence: Q5 of your C6 (workshop line 451). I argue NO recalibration (per Re:C4 conclusion — the K-counter is on the 2-class coarse axis, unchanged), but the partition expansion does add structure.

- Route-(c) **C5 reading: parse-tree subsumes for registry-anchor purposes**: §VII.U.2 stays as-is; FI/RD enters as "evaluation-layer tag" only; §VII.K-DUAL and §VII.K-PROP must be re-classified as methodology rules (forced by Q-L2 Reading-B above).

Which route do you commit to as the §VII.AH narrowing remediation? The choice has different K-counter consequences AND different rule-file/registry-edit consequences.

**Q-L4 — Does CM-1995 §III.4 dim-spectrum residue formula `a_n = Res Tr(D^{−2s}); s=(d−n)/2` IMPLICITLY pin a regulator-class via the choice of cutoff function?**

Your C2 substitution chain definitions (workshop line 33-34) cite "Borel functional calculus on D²" and at line 94 cite the CM-1995 §III.4 formula as the regulator-INDEPENDENT spectral-moment identity that anchors the F_inv side. But the residue extraction `Res[Tr(D^{-2s}); s=(d-n)/2]` requires a meromorphic continuation of `Tr(D^{-2s})` from a half-plane of convergence to s=(d-n)/2; the meromorphic continuation choice IS the regulator-class choice (ζ-class vs Pauli-Villars vs Mellin vs cutoff_sqrt vs anomaly via different analytic-continuation paths). Different regulator classes produce different residues at the same s — this is exactly the §VII.U.2 clause (a) calibration corpus phenomenon. Specifically:

- Is the CM-1995 formula `regulator-INDEPENDENT-at-the-symbolic-form-level-but-regulator-CLASS-DEPENDENT-at-the-numerical-residue-evaluation-level`? If yes, this is precisely my Reading-A from Q-L2 — the formula is parse-tree-INVARIANT (no π(a)) AND inherits the FI/RD axis through the regulator-class choice that selects which meromorphic continuation is taken.
- Or is the CM-1995 formula `regulator-INDEPENDENT-period`? In which case how do you reconcile with the §VII.U.2 clause (a) regulator-class-tagging discipline that requires `a_n^{R}` rather than bare `a_n`? The clause (a) tagging is structural at the registry level; bare `a_n` cannot satisfy `regulator-pin-discipline.md §"Rule"`.

The answer to Q-L4 directly determines whether the FI/RD axis is intrinsic to the substrate-IS observable or a downstream methodology tag. If CM-1995 IS implicitly regulator-class-pinning through analytic-continuation choice, the FI/RD axis enters even at the parse-tree-canonical Mellin-Dirichlet identity level — so axis 3 is substrate-IS and Reading-A in Q-L2 is forced.

**Q-L5 — Whether registry text for §VII.AH should distinguish "FI-strict joint F_2-class theorem" from "MIXED-via-regulator-dressing joint F_2-class theorem" as DISTINCT theorem-statements.**

Re:C2 + L2 substitution chains established that ANCHOR-2 is FI-on-F_2 ∧ RD-on-off-F_2 = MIXED-via-regulator-dressing on the regulator-class atlas axis. Under L2's Corrigendum 5 proposal, ANCHOR-2 is registered at the F_2-restricted scope (FI-on-F_2 only); the off-F_2 residues are diagnostic-only. Under this reading, §VII.AH IS a "FI-strict joint F_2-class theorem" at its registered scope.

Alternative reading: the off-F_2 residues are ALSO part of the registered theorem (Reading 2 from L2). Under this reading, §VII.AH IS a "MIXED-via-regulator-dressing joint F_2-class theorem" — a structurally weaker statement than FI-strict because the registered observable is sub-atlas-conditional rather than full-atlas-FI.

The two readings DIFFER on the §VII.AH theorem's registered scope and consequently on what the §VII.AH theorem EMPIRICALLY PREDICTS at obs2 (anomaly s=4/s=2 integer-graded factorized; absent at dispatch) and obs3 (Mellin-residue-ratio s=3/s=4 pole-scope test; absent at dispatch). If FI-strict, the obs2 + obs3 substantiations should preserve full-atlas-FI within their respective F_2 sub-atlas selections (which presumably differ from F_2 = {ζ, SDW} at different poles). If MIXED-via-regulator-dressing, obs2 + obs3 substantiations carry different factor-spreads on the off-F_2 sub-atlas at different poles, and the §VII.AH theorem must declare the pole-dependence of the spread structure.

The question is structural: should §VII.AH register ONE theorem or TWO theorems? My Re:C3 + L2 position is ONE theorem with explicit Corrigendum 5 scoping (FI-strict on F_2-restricted scope; off-F_2 diagnostic-only). Your C5 position is implicitly ONE theorem with FI/RD as evaluation-layer tag. Workshop verdict in Round 3 should pin the registered scope explicitly so obs2 + obs3 future re-dispatches have an unambiguous §VII.AH PASS criterion.

---

**Bonus operational reciprocation (cross-check on Q5 of your C6)**: Your C6 Q5 asked whether asserting FI/RD as a structural refinement recalibrates the K-counter to 9 instances. My Re:C4 position is NO recalibration: the K-counter is on the (INVARIANT vs DEPENDENT) coarse axis; the W1b-6, S-2, W-2 instances each pair INVARIANT with DEPENDENT and saturate K=3 at the coarse partition; the FI/RD refinement on F_inv adds resolution within the INVARIANT class but does not recalibrate the orthogonality between INVARIANT and DEPENDENT. K=3 MANDATORY status preserved; the Mellin-Dirichlet identity in Q5's bonus operational test is FI-strict (Re:C4 Example-A) and remains the canonical Corner I anchor at registry line 12923. The Mellin-Dirichlet identity's FI status under my trichotomy is **FI-strict** because it is an algebraic-identity statement (regulator-INDEPENDENT BY CONSTRUCTION; rel_diff = 0e+00 across atlas members per §VII.U.1 PASS); it is NOT MIXED and it is NOT RD. This answer satisfies your C6 Q5 bonus consistency check.

---

---

## Round 2 — connes: Follow-up

### CONVERGENCE

Lizzi's R1 surfaces three structurally distinct points where my R1 framing is genuinely moved. I concede each at the level of substrate-IS axis assignment and at the §VII registry-classification level; my surviving disagreement (DISSENT below) narrows to the precise scope of where §VII.U.2 clause (f) is triggered and whether §VII.AH narrowing is forced.

#### CV-1: Axis 3 (regulator-class atlas) IS substrate-IS at the §VII registry-anchor layer (Re:C1 + L1)

I concede the layer-assignment in C5: I had FI/RD living at the methodology / publication-precision layer with the substrate-physics layer carrying only axis 1 (parse-tree) and axis 2 (Mellin-pole). Lizzi's L1 §"Three structural sub-classes" + Re:C1 §"MISSED" block produce three structural witnesses that force the regulator-class atlas axis onto the substrate-IS layer:

1. **§VII.K-DUAL FI-Duality Theorem (registry line 4108)** is a registered §VII THM entry, not a methodology rule. Re-classifying it as evaluation-layer publication discipline would invalidate its §VII registry status — which I am not prepared to do.
2. **§VII.K-PROP CC-5 propagation identity (registry line 8976)** is similarly registered §VII THM (lizzi's signature theorem `span_R(O) = ∏_k span_R(f_{n_k}^R)^{|p_k|}`). It composes structural sub-classes under composition, not under publication-precision discipline.
3. **§VII.K-PROP-COMPOSITION lattice-join rule (registry line 9272)** is registered §VII THM. The lattice structure is substrate-IS at the regulator-class atlas axis.

Three §VII THM entries on the regulator-class atlas axis is structural saturation. The K=3 promotion threshold for the §VII registration of an axis is met BY THE EXISTING REGISTRY STATE; my C5 placement of FI/RD at the methodology layer was inconsistent with the state of the registry.

**Substitution chain — what changes structurally**:

```
Definitions:
  axis_substrate_IS  := { axis whose registered §VII THM family is non-empty }
  K_axis_promotion   := 3  (per feedback_rules-compensate-missing-structure.md)
  K_axis(regulator-class atlas) := |{§VII.K-DUAL, §VII.K-PROP, §VII.K-PROP-COMPOSITION}| = 3

Substitutions:
  K_axis(regulator-class atlas) = 3  ≥  K_axis_promotion = 3
  ⇒ regulator-class atlas axis ∈ axis_substrate_IS by registry-state cardinality.

Direction:
  My C5 placement of axis 3 at the methodology layer is REVISED.
  Axis 3 is substrate-IS at the regulator-class atlas layer; the
  publication-precision discipline (S82 W-3 RULE-3 letter; round-figure
  forbidden; mnemonic-vs-exact rule) is the AUDIT-LEG IMAGE of axis 3
  under the layer-functor F, NOT the substrate-IS axis itself.

Conclusion:
  Lizzi's L1 §"Three structural sub-classes" is structurally correct.
  Axis 3 is substrate-IS; the FI / MIXED-via-regulator-dressing / RD-strict
  trichotomy on F_inv is a structurally legitimate refinement WITHIN the
  INVARIANT class on axis 3, NOT a refinement of the algebra-axis K-counter.
```

The corrected three-axis substrate-IS framing (Re:C5 §"the convergence point" table at workshop lines 768-774) is the canonical reading. My C5 conflated axis 3 with its audit-leg image; the convergence is restored once axis 3 is recognized as substrate-IS.

#### CV-2: ANCHOR-2 IS structurally MIXED-via-regulator-dressing on axis 3 (Re:C2 + L2)

I concede lizzi's Re:C2 substitution chain Step 3 + L2 §"What the numerical structure shows" at the substrate-IS observable layer. The Sage-exact verification I provided in C2 (workshop lines 162-170) IS the evidence that ANCHOR-2 inhabits MIXED-via-regulator-dressing: span_{F_2}(xi²_0) = 1581/1581 = 1 EXACT (per Sage QQ; my C2 table) AND span_{A_5}(xi²_0) = 15810/1201 = 13.1640... at s=3 (Sage MCP exact verification: 15810/1201, RR ≈ 13.16403). The same structural reading holds at obs1 s=−1 with span_{A_5} = 4.964 (Sage MCP verification: 4.96444), span_{A_5\F_2} = 4.850 (Sage MCP: 4.84967), span_{F_2} = 1.0 EXACT — preserved across pole transitions.

**The M_F2 normalizer's class-selectivity is structural, not numerical artifact**. I conceded this implicitly at C2 lines 173-174 ("regulator-class-dependence at the numerical-evaluation layer"); lizzi's L2 elevates it correctly to a substrate-IS structural property: the M_F2 normalizer is a F_2-class projector that exact-cancels on F_2 and leaves CLASS-RESIDUE on A_5 \ F_2, BY CONSTRUCTION of the spectral algebra A_F = F_2 = {ζ, SDW}. This IS the family-selector property of M_F2 at the substrate-IS layer.

I revise C2's classification: ANCHOR-2 IS simultaneously (algebra-axis = INVARIANT, Mellin-pole = s=3, R-class atlas = MIXED-via-regulator-dressing) — three substrate-IS axis-tags, not two. The 3-axis Corner_cell(ANCHOR-2) = (INVARIANT, s=3, MIXED) per Re:C3 substitution chain.

#### CV-3: §VII.K-DUAL + §VII.K-PROP cannot be re-classified as evaluation-layer tags (Q-L2 Reading-A forced)

Lizzi's Q-L2 forces a binary: either (Reading-A) Seeley-DeWitt coefficients are algebra-INVARIANT AND RD-strict on a structurally-orthogonal axis 3 (substrate-IS), with §VII.K-DUAL + §VII.K-PROP retaining their §VII THM status; OR (Reading-B) FI/RD is "evaluation-layer tag" and §VII.K-DUAL + §VII.K-PROP must be re-classified as methodology rules. Reading-B requires registry-edits I am NOT prepared to make. Reading-A is therefore forced. This commits me to Re:C5's three-axis substrate-IS framing.

**Convergence-point summary**: lizzi and I now agree on (i) axis 3 is substrate-IS; (ii) §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION are registered §VII THMs on axis 3; (iii) ANCHOR-2 is MIXED-via-regulator-dressing on axis 3; (iv) the K=3 algebra-axis K-counter is preserved unchanged (lizzi's Re:C4 §"AGREE on K-counter saturation" stipulates this; I confirm). The remaining DISSENT is narrow: does the §VII.U.2 4-corner partition's clause (f) FORBIDDEN-cross-corner-co-primary discipline extend uniformly to axis 3, or does it stay confined to (axis 1 × axis 2) with axis 3 enforced by §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION as a SEPARATE structural-discipline family?

### DISSENT

The structural orthogonality of the three substrate-IS axes (CV-1 through CV-3) does NOT settle the §VII.AH narrowing question — and on this narrow but consequential point I retain DISSENT. New evidence and sharpened argument follow.

#### DS-1: §VII.U.2 clause (f) is scoped to its 4-corner partition; axis 3 is governed by §VII.K-* family, not by clause (f)

Lizzi's Re:C3 substitution chain reading (b) extends §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary to a 3-axis partition where ANCHOR-1 (INVARIANT, s=3, RD) and ANCHOR-2 (INVARIANT, s=3, MIXED) inhabit distinct 3-axis cells. I disagree with the EXTENSION OF CLAUSE (f) to axis 3 — even though I concede axis 3 is substrate-IS (CV-1).

**Substitution chain — clause (f) scope is the 4-corner partition only**:

```
Definitions (per §VII.U.2 registry text + registry-landing.md):
  §VII.U.2-partition := the 4-corner classification on (algebra-axis × Mellin-pole)
                        registered at clause (d), registry lines 12921-12928
  §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary scope (registry line 12932):
    "registry entries cannot pin two anchors at co-primary weight when the
     anchors inhabit distinct corner cells" — where "corner cells" refers
     to the 4-corner table of clause (d), NOT a hypothetical higher-axis
     extension.
  axis 3 (regulator-class atlas) discipline:
     §VII.K-DUAL FI-Duality Theorem (registry line 4108) — registers FI as
       structural duality
     §VII.K-PROP CC-5 propagation identity (registry line 8976) — registers
       composition behavior of FI/MIXED/RD sub-classes
     §VII.K-PROP-COMPOSITION lattice-join rule (registry line 9272) — registers
       lattice structure under sub-class composition
     These are the canonical §VII registry mechanisms for axis-3 discipline.

Substitutions:
  Step 1: clause (f)'s "distinct corner cells" predicate IS DEFINED on the
          4-corner table of clause (d). The clause text does NOT generalize
          to an N-axis partition; it is a 2-axis partition discipline by
          construction.

  Step 2: extending clause (f) to axis 3 IS A NEW DISCIPLINE — call it
          clause (f-extended). clause (f-extended) does NOT exist in the
          registry text at registry line 12932. Promoting clause (f) to
          (f-extended) requires a §VII.U.2 corrigendum that adds axis 3 to
          the partition.

  Step 3: axis-3 structural discipline is ALREADY DISCHARGED by the §VII.K-*
          family (DUAL + PROP + PROP-COMPOSITION). This family operates as
          a STRUCTURAL OBLIGATION on registered axis-3 quantities: any
          registry entry citing FI / MIXED / RD must satisfy §VII.K-DUAL's
          duality requirements + §VII.K-PROP's composition identity +
          §VII.K-PROP-COMPOSITION's lattice-join rule. These are the
          structural disciplines on axis 3; they do NOT route through
          §VII.U.2 clause (f).

Simplification:
  clause (f) discipline scope = (axis 1 × axis 2) only.
  axis 3 discipline scope     = §VII.K-* family.
  These are TWO DISTINCT DISCIPLINES applying at TWO DISTINCT AXIS-SYSTEMS.
  Conflating them by extending clause (f) to axis 3 is a §VII.U.2 partition
  expansion, not a forced structural reading.

Direction:
  Under the EXISTING registry state (clause (f) scoped to 4-corner; axis 3
  governed by §VII.K-* family), §VII.AH's anchors:
    ANCHOR-1 (INVARIANT, s=3) — 4-corner = Corner I; axis 3 = RD
    ANCHOR-2 (INVARIANT, s=3) — 4-corner = Corner I; axis 3 = MIXED
  share Corner I on the 4-corner partition (clause (f) compliance: BY VACUITY
  per C3) AND have asymmetric scoping on axis 3 (RD vs MIXED).

  The §VII.U.2 clause (f) trigger is NOT activated under the existing scope.
  The axis-3 discipline is governed by §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-
  COMPOSITION, which constrain composition behavior and duality structure
  but do NOT impose a "no cross-MIXED-RD-co-primary" prohibition.

Conclusion:
  §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY structure passes both disciplines:
   - 4-corner discipline (clause (f)): INTRA-corner-I, admissible per NOTE.
   - Axis-3 discipline (§VII.K-* family): asymmetric scoping is the structural
     content of the V→A_F→C chain (V = full-atlas-K-invariance-failure premise;
     C = F_2-restricted-protection theorem); §VII.K-PROP composition identity
     governs HOW FI / MIXED / RD compose, not whether co-primary citation
     is permissible across sub-classes.

  §VII.AH narrowing is NOT FORCED by the existing registry state. Lizzi's
  Re:C3 reading (b) requires a §VII.U.2 clause-(f) scope expansion that has
  NOT been registered.
```

This is the central DISSENT. I am NOT denying axis 3's substrate-IS status (conceded in CV-1). I AM denying that §VII.U.2 clause (f) — as currently registered at line 12932 — automatically extends to axis 3. Extending it requires an explicit §VII.U.2 corrigendum that lizzi has not registered (and that would itself require a separate workshop's structural verdict).

#### DS-2: 3-class refinement of F_inv requires its own K-counter (independent calibration corpus)

Lizzi's Re:C4 §"Counter-(3)" + L1 §"Three structural sub-classes" propose a 3-class refinement on F_inv: {INVARIANT-FI-strict, INVARIANT-MIXED-via-RD, INVARIANT-RD-strict}. This is a STRUCTURAL refinement; per `agent-standards.md §"HIGH-DENSITY WORKSHOP TEMPLATE"` + `feedback_rules-compensate-missing-structure.md`, structural refinements promote at K=3 distinct calibration instances.

Lizzi's Re:C4 substitution chain provides 3 candidate calibration instances (Example-A: Mellin-Dirichlet identity = FI-strict; Example-B: Seeley-DeWitt coefficient = RD-strict; Example-C: xi²_0(R) = MIXED-via-RD). These ARE three structurally distinct instances on the F_inv side. But they are ALL on a SINGLE workshop (this one, S88 W-26) — and the K-counter discipline requires structurally-DISTINCT loci, not three examples sourced from one structural argument.

**Substitution chain — K-counter applied to the proposed 3-class refinement**:

```
Definitions (per feedback_rules-compensate-missing-structure.md):
  K_promotion = 3 distinct calibration-corpus instances, each from a
                structurally-DISTINCT workshop / synthesis / registered theorem.

Substitutions:
  Instance-A (FI-strict): §VII.U.1 Mellin-Dirichlet identity (S86 W-1 / S87 W1a-4
              PASS rel_diff = 0e+00); registered §VII anchor.
  Instance-B (RD-strict): §VII.U.2 clause (a) calibration corpus (registry line
              12913) — Seeley-DeWitt coefficients regulator-class-tagged; a single
              registered registry-text reference.
  Instance-C (MIXED-via-RD): §VII.AH ANCHOR-2 (this workshop, S88 W-26); STAGE-1-
              CANDIDATE pending Stage-2 close.

Simplification:
  Instance-A is a registered §VII THM (well-saturated calibration locus).
  Instance-B is a registry-text-citation example; its structural-witness role
              for the 3-class refinement is PROVISIONAL (the §VII.U.2 entry
              registers Seeley-DeWitt coefficients as F_inv canonical examples,
              not as RD-strict calibration witnesses for a refinement).
  Instance-C is in-flight (STAGE-1-CANDIDATE; not yet permanent).

  K_calibrated = 1 (firm, Instance-A) + 1 (provisional, Instance-B) + 0 (in-flight,
                 Instance-C) = 1-2 saturated instances on the 3-class refinement.

Direction:
  The 3-class refinement is a SUGGESTION at K=1-2 saturated, NOT MANDATORY at
  K=3 — until at least one additional structurally-distinct instance lands as
  a registered §VII THM (e.g., a separately-registered MIXED-via-RD instance
  beyond xi²_0; or a separately-registered RD-strict instance beyond the
  §VII.U.2 clause (a) corpus).

Conclusion:
  The 3-class refinement is structurally LEGITIMATE (per CV-1 axis 3 is
  substrate-IS) but its rule-file promotion to MANDATORY status is gated
  on K=3 distinct calibration corpus instances. Until then, applying the
  refinement to FORCE a §VII.AH narrowing decision is using a SUGGESTION-
  status structural discipline as if it were MANDATORY.
```

This sharpens the dissent: even if axis 3 is substrate-IS (CV-1), the OPERATIONAL FORCE of the 3-class refinement on the §VII.AH narrowing question requires K=3 calibration. We're at K=1-2 saturated. Lizzi's Corrigendum 5 narrowing (route (a) of Re:C3) is a viable in-place §VII.AH text fix that does NOT require the 3-class refinement to reach MANDATORY status — and is therefore the structurally cleaner remediation.

#### DS-3: Reading 1 (F_2-restricted) is PRIMARY for §VII.AH; Reading 2 (full-atlas) is a structural diagnostic

Lizzi's L2 §"What §VII.AH must declare" surfaces the Reading 1 / Reading 2 disambiguation. I argue Reading 1 (F_2-restricted) is the PRIMARY registered scope of §VII.AH; Reading 2 (full-atlas) is a structural-diagnostic enrichment.

**Substitution chain — Reading 1 vs Reading 2 priority under the §VII.AH text**:

```
Definitions:
  Reading 1: ANCHOR-2 registered at F_2-restricted scope R ∈ F_2 = {ζ, SDW}.
             xi^2_0 evaluated only at F_2 elements; off-F_2 residues are
             diagnostic-only (substantiating clause (e) K-invariance failure
             at order O(1) on supersets, but not part of registered ANCHOR-2).
  Reading 2: ANCHOR-2 registered at full-atlas scope R ∈ A_5 = {ζ, SDW,
             cutoff_sqrt, anomaly, Zubarev}. Off-F_2 residues are part of
             registered theorem.

  §VII.AH theorem text registered scope (registry lines 15417-15479):
     Clause (a) ("Spectral 3-class partition (lizzi L2)", line 15427) cites
                 M_R(s=3) 5-tuple for ALL FIVE atlas members.   ⇒ Reading 2.
     Clause (b) ("Per-branch protection of A_s ledger", line 15429-15430)
                 cites "within a single regulator branch (e.g., F_2-class
                 via zeta scheme at L_max=3)".                  ⇒ Reading 1.
     Clause (d) (line 15433) "within a single regulator branch ... at the
                 spectral-functional level within a single regulator class".
                                                                  ⇒ Reading 1.
     Clause (e) (line 15435) cites 924×/298×/798× margins on off-F_2 residues
                 as K-invariance-failure-on-supersets evidence.    ⇒ Reading 2.

Substitutions:
  ANCHOR-1 (the V layer) reads as Reading 2 (full-atlas K-invariance-failure
           premise) per clauses (a) + (e).
  ANCHOR-2 (the C layer) reads as Reading 1 (F_2-restricted protection theorem)
           per clauses (b) + (d).
  These are NOT in conflict; they are the V → A_F → C sequential chain
  with ASYMMETRIC SCOPING by design — the Re:C2 + L2 evidence ESTABLISHES
  this asymmetry.

Simplification:
  The §VII.AH theorem statement IS a sequential V→A_F→C chain with asymmetric
  scoping: V supplies the full-atlas K-invariance-failure premise (Reading 2 on
  ANCHOR-1); C supplies the F_2-restricted protection theorem CONDITIONAL on V
  (Reading 1 on ANCHOR-2). The asymmetric scoping IS the SOURCE-DOUBLE-CITE
  structural content: V is non-fungible with C precisely BECAUSE V operates on
  the full atlas while C operates on the F_2-restricted scope.

Direction:
  Reading 1 is the canonical reading of ANCHOR-2 under the registered §VII.AH
  text (clauses (b) + (d)).
  Reading 2 on ANCHOR-2 is a structural-diagnostic enrichment that does NOT
  contradict Reading 1 — the off-F_2 residues at obs1 (factor 4.85× spread)
  validate clause (e)'s K-invariance failure on supersets, NOT a re-scoping
  of the registered ANCHOR-2.

Conclusion:
  §VII.AH narrowing under lizzi's Corrigendum 5 (route (a) of Re:C3) is
  STRUCTURALLY VALID and is the cleanest remediation. The Corrigendum
  text proposed at L2 §"§VII.AH narrowing entry text proposal" makes the
  Reading 1 priority EXPLICIT in the registry, eliminates the residual
  ambiguity surfaced by Re:C2 + L2, and preserves SOURCE-DOUBLE-CITE-CO-
  PRIMARY admissibility under the asymmetric-scoping reading.
```

I therefore now ENDORSE lizzi's Corrigendum 5 narrowing proposal at L2 (workshop lines 949-953) as the canonical resolution. This is a structural revision of my C3 conclusion that "§VII.AH narrowing is NOT triggered" — under the existing registry state with axis 3 unscoped at clause (f), narrowing is NOT FORCED, but a §VII.AH text disambiguation IS structurally valuable AND lizzi's Corrigendum 5 produces it without requiring §VII.U.2 partition expansion. The resolution is in-place: an explicit Reading 1 declaration that the off-F_2 numerical residues are diagnostic-only.

This converts a residual ambiguity (Reading 1 vs Reading 2) into an explicit registry pin. It does NOT trigger §VII.U.2 clause (f); it does NOT require §VII.K-* family modification; it does NOT recalibrate the K-counter. It is the minimal structural fix.

### EMERGENCE

The cross-pollination of CV-1 (axis 3 substrate-IS) + DS-1 (clause (f) scope) + DS-2 (3-class refinement K-counter) + DS-3 (Reading 1 priority) produces three structural insights I had not seen before R1:

#### EM-1: §VII.U.2 4-corner partition IS the COARSE projection of an 18-cell substrate-IS partition

Lizzi's Re:C4 §"EMERGES" lattice reading at workshop line 752 ("The §VII.U.2 4-corner partition is the COARSE projection of a finer 3 × 2 × 3 = 18-cell partition onto the (algebra-axis, Mellin-pole) plane") is structurally correct AND I now endorse it as a registry-level structural insight.

**Substitution chain — the 18-cell lattice as substrate-IS partition**:

```
Definitions:
  axis 1 (operator-algebraic):    {INVARIANT, DEPENDENT}                 |·| = 2
  axis 2 (Mellin-pole):           {s=3, s=4}                              |·| = 2
                                  (extensible to {s=3, s=4, s=5, ...} per
                                   per-Bulletin-per-pole rule extension at
                                   cross-pillar-bridge-anatomy.md §"Per-
                                   Bulletin-per-pole Level-1 wall classification")
  axis 3 (regulator-class atlas): {FI-strict, MIXED-via-RD, RD-strict}    |·| = 3
                                  on the F_inv side; {parallel structure}
                                  on the F_dep side.

  3-axis substrate-IS partition_cell(F) := (axis 1 (F), axis 2 (F), axis 3 (F))
  Total cardinality at canonical scope: 2 × 2 × 3 = 12 sub-cells per side
                                         × 2 sides (F_inv, F_dep) = 24 sub-cells.
  At lizzi's "DEPENDENT side not subdivided" reading: 2 × 3 + 2 × 1 = 8 sub-cells
                                         per pole × 2 poles = 16 sub-cells.
  At full Re:C4 §"6 sub-cells in principle" reading on (axis 1 × axis 3):
                                         3 × 2 = 6 sub-cells × 2 (Mellin) = 12.

  §VII.U.2 4-corner partition := projection onto (axis 1 × axis 2) only.
                                  Cardinality 4 = 2 × 2.
                                  This is the COARSE projection.

Substitutions:
  The §VII.U.2 4-corner partition tracks (axis 1 × axis 2) at registry-anchor-
  discriminator weight; axis 3 enters as registered §VII.K-* THM family
  (DUAL + PROP + PROP-COMPOSITION) governing axis-3 discipline INDEPENDENTLY
  of clause (f).

Simplification:
  4-corner = π_{(1,2)}(18-cell)  where π is projection onto (axis 1, axis 2).
  18-cell partition is the substrate-IS structure; 4-corner is its registry-
  anchor-discriminator coarse-graining.

Direction:
  The 18-cell partition is the FINE substrate-IS structure on (A_K, H_K, D_K)
  functionals. The 4-corner partition is its registry-anchor-discriminator
  COARSE projection. The two are NOT in conflict; they are at different
  resolutions of the same substrate-IS classification.

Conclusion:
  Future §VII registry entries SHOULD be tagged at the 18-cell resolution
  for full structural transparency (3-axis position) AND at the 4-corner
  resolution for clause (f) admissibility checking. The two tags do not
  conflict; they enrich each other.
```

I propose registering this lattice reading as **§VII.U.2-EXT (substrate-IS lattice extension)** in a forward-looking registry entry. Registration would be deferred to S89 with concrete calibration corpus targeting K=3 distinct instances on the 3-axis partition. Lizzi's L1 three sub-classes (FI-strict / MIXED-via-RD / RD-strict) are the F_inv-side lattice; parallel structure on F_dep-side TBD via Stage-2 cross-corpus assembly.

#### EM-2: Asymmetric SOURCE-DOUBLE-CITE-CO-PRIMARY scoping is a NEW structural class

The §VII.AH theorem's V→A_F→C chain with asymmetric scoping (V on full atlas; C on F_2-restricted scope) is structurally NEW. The `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` 3-condition test (Detection block) was originally registered for SAME-SCOPE sequential chains; the §VII.AH chain extends it to ASYMMETRIC-SCOPE sequential chains where V's scope is broader than C's scope.

This is a structural extension of the SOURCE-DOUBLE-CITE pattern. I propose registering it at `registry-landing.md` as **"asymmetric-scope sequential V→A_F→C chain"**, with §VII.AH as Calibration Instance 1. Future workshops surfacing similar chains (V supplies a broad-atlas premise; C supplies a sub-atlas-restricted theorem conditional on V) would calibrate the same structural class.

The asymmetric-scope reading is consistent with lizzi's L2 §"What §VII.AH must declare" Reading 1 priority + my DS-3 reading: V is full-atlas; C is F_2-restricted; the asymmetric scoping IS the SOURCE-DOUBLE-CITE structural content. This is preserved by lizzi's Corrigendum 5.

#### EM-3: The §VII.K-* family discipline is PARALLEL to (NOT extension of) §VII.U.2 clause (f)

DS-1's substitution chain established that axis 3 discipline is governed by §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION as a SEPARATE, PARALLEL structural discipline to §VII.U.2 clause (f). This is structurally significant:

- **§VII.U.2 clause (f) discipline**: governs registry-anchor-discriminator partition on (axis 1 × axis 2); enforces FORBIDDEN-cross-corner-co-primary on the 4-corner partition.
- **§VII.K-* family discipline**: governs axis 3 structural identities (FI duality; CC-5 composition; lattice-join); enforces composition behavior across FI / MIXED / RD sub-classes.

These two disciplines do NOT compete; they apply at distinct axis-systems. The §VII.K-* family does NOT contain a "no cross-MIXED-RD-co-primary" prohibition because axis 3's structural discipline IS composition-and-duality, not partition-based prohibition. Lizzi's Re:C3 reading (b) implicitly assumes axis 3 inherits clause (f)'s prohibition pattern; my DS-1 argues this is a structural extrapolation beyond what §VII.K-* registers.

**Consequence**: lizzi's Corrigendum 5 (route (a)) is the structurally-cleanest remediation BECAUSE it preserves the parallel-disciplines structure. Routes (b) (§VII.U.2 partition expansion) and (c) (§VII.K-* re-classification) both COLLAPSE the parallel structure into a unified discipline — and the existing registry has invested 3 §VII THM entries in keeping them parallel. Route (a) is the minimal-perturbation fix.

### QUESTIONS

#### Answers to lizzi's L3 questions

**A-Q-L1 — Where in §VII.U.2 clause (e) is axis 3 ruled out as a structural test?**

Nowhere. Clause (e) does NOT rule axis 3 out as a structural axis. My C5 framing of FI/RD as "evaluation-layer tag" was a misreading. Clause (e) asserts the parse-tree decision is regulator-INDEPENDENT (the SAME parse-tree classification under all regulators); it does NOT assert axis 3 is irrelevant as a registry-anchor-discriminator. Per CV-1 + CV-3 + DS-1, axis 3 is substrate-IS at the §VII registry level (registered §VII THM family); §VII.U.2 clause (e) operates at axis 1; clause (f) at the 4-corner partition (axes 1 × 2); axis 3 discipline at §VII.K-* family. The parse-tree decision is necessary-but-not-sufficient for the FULL substrate-IS classification (which is 3-axis, per EM-1 lattice reading); it IS sufficient for the clause-(f) admissibility check on the 4-corner partition, which is where clause (f) is scoped (DS-1). The §VII.AH narrowing question hinges on whether clause (f) extends to axis 3 (lizzi's Re:C3 reading (b)) or stays scoped to (axes 1 × 2) (my DS-1 reading); the latter does not force narrowing, but lizzi's Corrigendum 5 (DS-3 endorsement) is structurally valuable independently.

**A-Q-L2 — Reading-A or Reading-B for Seeley-DeWitt coefficients?**

**Reading-A**. Per CV-1 + CV-3, I commit to Reading-A: Seeley-DeWitt coefficients are algebra-INVARIANT (parse-tree-INVARIANT) AND RD-strict on axis 3 (substrate-IS). §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION retain their §VII THM status (registry not re-classified). Axis 3 IS substrate-IS at the regulator-class atlas layer. The publication-precision discipline (S82 W-3 RULE-3 letter form; round-figure-forbidden) is the AUDIT-LEG IMAGE of axis 3 under F, not the substrate-IS axis itself. My C5 conflation of axis 3 with audit-leg image is REVISED.

**A-Q-L3 — Which Corrigendum 5 / partition expansion / C5 route?**

**Route (a) — Corrigendum 5 narrowing**. Per DS-3 + EM-2 + EM-3, lizzi's Corrigendum 5 (L2 §"§VII.AH narrowing entry text proposal") is the canonical remediation:
- It preserves §VII.U.2 4-corner partition unchanged (no clause-(f) extension forced).
- It registers the asymmetric-scope sequential V→A_F→C chain explicitly (EM-2 structural class).
- It preserves the parallel-discipline structure of §VII.U.2 clause (f) and §VII.K-* family (EM-3).
- It does NOT recalibrate the K-counter.
- It addresses the residual Reading 1 / Reading 2 ambiguity directly via in-place text addition.

I co-endorse the Corrigendum 5 text. Lizzi: please commit it to the §VII.AH registry edit at the close of R3.

**A-Q-L4 — Does CM-1995 §III.4 implicitly pin a regulator class via meromorphic continuation?**

**Yes, but the regulator-class pin is at axis 3 (substrate-IS layer), not at axis 1 (parse-tree layer)**. The CM-1995 dim-spectrum residue formula `a_n = Res[Tr(D^{−2s}); s=(d−n)/2]` requires meromorphic continuation of `Tr(D^{−2s})` from a half-plane of convergence to s=(d−n)/2. The continuation choice (ζ-class vs Pauli-Villars vs Mellin vs cutoff_sqrt vs anomaly) IS the regulator-class choice. Different continuations yield different residues at the same s — exactly the §VII.U.2 clause (a) calibration corpus phenomenon. The formula is:

- **Regulator-INDEPENDENT at axis 1 (operator-algebraic / parse-tree)**: no π(a) symbol in the AST regardless of which continuation is chosen.
- **Regulator-CLASS-DEPENDENT at axis 3 (substrate-IS regulator-class atlas)**: numerical residue depends on R; this IS the substrate-IS axis-3 content.

The two readings are CONSISTENT under the three-axis substrate-IS framing (CV-1 + EM-1). The CM-1995 formula is the bridge that DEMONSTRATES parse-tree-INVARIANT can simultaneously be RD-strict at the regulator-class atlas axis. Reading-A from Q-L2 is forced; my CV-3 commits to it.

**A-Q-L5 — Should §VII.AH register one theorem or two?**

**One theorem with explicit Corrigendum 5 scoping** (matches lizzi's Re:C3 + L2 position). Per DS-3 + EM-2:

- The §VII.AH theorem is a SINGLE asymmetric-scope sequential V→A_F→C chain (EM-2 structural class).
- Reading 1 is PRIMARY for ANCHOR-2 (F_2-restricted scope, FI-strict on F_2).
- Reading 2 is structurally-DIAGNOSTIC for ANCHOR-1 (full-atlas K-invariance-failure premise).
- The asymmetric scoping IS the structural content of the chain — V's scope is broader than C's scope BY CONSTRUCTION.

Splitting into TWO theorems (FI-strict + MIXED-via-RD) would lose the structural identity of the V→A_F→C chain. Corrigendum 5 makes the asymmetric scoping EXPLICIT in registry text without splitting; this is the cleanest registration. Under this reading:
- obs2 (anomaly s=4/s=2 integer-graded factorized): substantiation should preserve FI-on-F_2 within the F_2 sub-atlas selection at the s=4 pole; the off-F_2 spread can vary per pole-scope discipline (W-9 RULE-3 MANDATORY-K=4 per S88 W7a-72).
- obs3 (Mellin-residue-ratio s=3/s=4): cross-pole F_2-cancellation preserved; cross-pole off-F_2 spread is pole-specific.

**A-Q-L4-bonus — Mellin-Dirichlet identity is FI-strict reciprocation**. Confirmed. The Mellin-Dirichlet identity is an algebraic-identity statement (regulator-INDEPENDENT BY CONSTRUCTION; rel_diff = 0e+00 across atlas members per §VII.U.1 PASS); span_{A_5}(F) = 1 EXACT ⇒ FI-strict per L1 sub-class definition. My C6 Q5 bonus is satisfied at the FI-strict reading.

#### My SHARPENED follow-up questions for R3

**Q-C1 — Corrigendum 5 text + §VII.U.2-EXT registration: which goes in R3 close, and in what order?**

Lizzi's Corrigendum 5 (L2 §"§VII.AH narrowing entry text proposal") is endorsed for R3 close. Separately, EM-1's §VII.U.2-EXT lattice-reading registration is forward-looking work. Question: should R3 close (a) commit ONLY Corrigendum 5 to §VII.AH and defer §VII.U.2-EXT to S89 carry-forward, OR (b) propose a §VII.U.2-EXT preamble in R3 close that IS the structural framing under which Corrigendum 5 lands? Option (b) couples them; option (a) keeps them independent. I lean (a) — keep Corrigendum 5 as a minimal-perturbation §VII.AH edit and propose §VII.U.2-EXT as a separate S89 workshop with K=3 calibration-corpus seeding. Your view?

**Q-C2 — Asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY (EM-2 structural class) — registered at registry-landing.md or only as an §VII.AH note?**

EM-2's asymmetric-scope sequential V→A_F→C chain extension to the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern is a structural extension of `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"`. Question: should the structural extension be registered at registry-landing.md (with §VII.AH as Calibration Instance 1; K-counter for promotion to MANDATORY pending K=2 and K=3 instances), OR retained as an §VII.AH-specific structural note (lighter-weight; doesn't seed a forward calibration corpus)? I lean toward registry-landing.md registration with K-counter starting at K=1 — the asymmetric-scope chain is structurally novel and worth pre-registering as a calibration target. Your view?

**Q-C3 — 3-axis K-counter recalibration scoped to axis 3 only?**

Under CV-1 + CV-3, axis 3 is substrate-IS with §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION as the registered §VII THM family (3 instances saturating axis-3 K=3 BY THE REGISTRY STATE). DS-2 argues the F_inv-side 3-class refinement (FI-strict / MIXED-via-RD / RD-strict) is at K=1-2 saturated and is SUGGESTION, not MANDATORY, until K=3 reaches. Question: do you commit to the F_inv-side 3-class refinement K-counter as DISTINCT from the axis-3 §VII.K-* family K-counter (which is already saturated)? They are nested but distinct: the §VII.K-* family registers axis 3 AT THE AXIS LEVEL (K=3 from DUAL + PROP + PROP-COMPOSITION); the 3-class refinement registers SUB-CLASSES WITHIN the F_inv side of axis 3 (K=1-2 from current corpus). My reading of DS-2 makes them nested but with separate K-counters. Confirm or revise?

---

## Round 2 — lizzi: Cross-Synthesis

### CONVERGENCE

connes's R2 produced four substantive convergences on points where my R1 framing was either underspecified or non-canonical. I accept each with attribution and tighten the operational consequences.

#### CV-L1 — Re: DS-1 (clause (f) scope is the 4-corner partition; axis 3 governed by §VII.K-* family in parallel)

I CONCEDE DS-1 as the structurally correct reading of the EXISTING registry state. My Re:C3 substitution chain reading (b) — extending §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary to a 3-axis partition — was a structural EXTRAPOLATION of clause (f)'s scope, not a reading of its registered text. connes's DS-1 substitution chain (workshop lines 1080-1124) correctly identifies that:

```
Definitions (revised, accepting DS-1):
  §VII.U.2 clause (f) registered scope (registry line 12932):
    "registry entries cannot pin two anchors at co-primary weight when the
     anchors inhabit distinct corner cells" — "corner cells" definitionally
     refers to the 4-corner table of clause (d), NOT to a hypothetical
     N-axis extension.
  axis 3 (regulator-class atlas) registered discipline:
     §VII.K-DUAL FI-Duality Theorem  (registry line 4108)
     §VII.K-PROP CC-5 propagation    (registry line 8976)
     §VII.K-PROP-COMPOSITION         (registry line 9272)

Substitutions:
  Step 1: clause (f) text predicate "distinct corner cells" is DEFINED on
          the clause-(d) 4-corner table. The text does NOT generalize to
          an N-axis partition by its own letter.
  Step 2: §VII.K-* family discipline operates as a STRUCTURAL OBLIGATION
          on registered axis-3 quantities (duality + composition + lattice-
          join), NOT as a partition-based prohibition.
  Step 3: extending clause (f) to axis 3 requires a §VII.U.2 corrigendum
          PROMOTING the partition from 4-corner to (4-corner × 3-class).
          That corrigendum is NOT registered; my Re:C3 reading (b) was
          treating it as registered.

Direction:
  Under the EXISTING registry state (clause (f) scoped to 4-corner; axis 3
  governed by §VII.K-* family in parallel), the §VII.AH SOURCE-DOUBLE-CITE-
  CO-PRIMARY anchor structure passes BOTH disciplines BY DIFFERENT MECHANISMS:
    - 4-corner discipline (clause (f)): INTRA-corner-I, admissible per NOTE
    - Axis-3 discipline (§VII.K-* family): asymmetric scoping (V full-atlas
      RD; C F_2-restricted FI) is the V→A_F→C structural content of the
      sequential chain, governed by §VII.K-PROP composition behavior, NOT
      by a partition-prohibition rule.

Conclusion:
  §VII.U.2 clause (f) is NOT triggered under existing registry scope.
  My Re:C3 reading (b) was a structural extrapolation; DS-1 reading is
  the canonical operational discipline.
```

This reading has the further structural advantage that it AVOIDS §VII.U.2 partition expansion as an in-session forced consequence of the §VII.AH narrowing question. The parallel-disciplines reading keeps clause (f) and §VII.K-* on independent rule-tracks — a cleaner topology than a unified partition expansion would produce.

#### CV-L2 — Re: DS-2 (3-class refinement on F_inv is K=1-2 saturated, NOT yet MANDATORY at K=3)

I CONCEDE DS-2's K-counter accounting at the F_inv-side 3-class refinement layer. My Re:C4 + L1 §"Three structural sub-classes" presented {FI-strict, MIXED-via-RD, RD-strict} as a structural refinement; DS-2 correctly observes that all three calibration instances I cited are sourced from this single workshop's structural argument:

```
Definitions (per feedback_rules-compensate-missing-structure.md):
  K_promotion = 3 distinct calibration-corpus instances, each from a
                structurally-DISTINCT workshop / synthesis / registered theorem.

Substitutions:
  Instance-A (FI-strict)       = §VII.U.1 Mellin-Dirichlet identity.
                                  Status: registered §VII THM (firm calibration).
  Instance-B (RD-strict)       = §VII.U.2 clause (a) Seeley-DeWitt corpus.
                                  Status: registry-text citation (PROVISIONAL — the
                                          §VII.U.2 entry registers Seeley-DeWitt
                                          coefficients as F_inv canonical examples,
                                          NOT specifically as RD-strict witnesses
                                          for a 3-class refinement).
  Instance-C (MIXED-via-RD)    = §VII.AH ANCHOR-2 (this workshop, S88 W-26).
                                  Status: STAGE-1-CANDIDATE; in-flight.

Simplification:
  K_calibrated_firm     = 1     (Instance-A; registered §VII THM)
  K_calibrated_provisional = 1  (Instance-B; registry-text citation only)
  K_calibrated_in-flight = 1    (Instance-C; STAGE-1-CANDIDATE)
  K_promotion_threshold = 3.

Direction:
  K_calibrated_firm < K_promotion_threshold ⇒ 3-class refinement is
  SUGGESTION at K=1-2 saturated, NOT MANDATORY at K=3.

Conclusion:
  Applying the 3-class refinement to FORCE a §VII.AH narrowing decision
  is using a SUGGESTION-status structural discipline as if it were
  MANDATORY. This was a structural overreach in my Re:C3.
```

The operational consequence: I cannot cite the 3-class refinement as MANDATORY-status grounds for a §VII.U.2 clause-(f) extension. The refinement is structurally LEGITIMATE per CV-1 (axis 3 substrate-IS) but its rule-file promotion is gated on additional independent calibration loci. Lizzi's Corrigendum 5 narrowing (Route (a) of Re:C3) is a viable in-place §VII.AH text fix that does NOT require the 3-class refinement to reach MANDATORY — DS-2 endorses this as the structurally cleaner remediation, and I now agree.

#### CV-L3 — Re: DS-3 + EM-3 (Reading 1 PRIMARY for §VII.AH; §VII.K-* family is PARALLEL governance)

I CONCEDE DS-3's parse of the §VII.AH registered text. The verbatim per-clause scoping is:

| Clause | Cited scope | Reading | Cite |
|:-------|:------------|:--------|:-----|
| (a) "Spectral 3-class partition (lizzi L2)" | full M_R(s=3) 5-tuple | Reading 2 (full-atlas) on ANCHOR-1 | registry line 15427 |
| (b) "Per-branch protection of A_s ledger" | within a single regulator branch (F_2-class via zeta) | Reading 1 (F_2-restricted) on ANCHOR-2 | registry line 15429-15430 |
| (d) cosmological-analog clause | within a single regulator class | Reading 1 (F_2-restricted) on ANCHOR-2 | registry line 15433 |
| (e) K-invariance failure margins | 924× / 298× / 798× on off-F_2 residues | Reading 2 (full-atlas-superset) on ANCHOR-1's premise | registry line 15435 |

The asymmetric scoping is registered BY CONSTRUCTION across (a)+(e) on ANCHOR-1 vs (b)+(d) on ANCHOR-2. DS-3's reading — V supplies the full-atlas K-invariance-failure premise; C supplies the F_2-restricted protection theorem CONDITIONAL on V — is the canonical V→A_F→C sequential chain that the §VII.AH text registers. Reading 1 IS PRIMARY for ANCHOR-2 by the registered clauses (b)+(d).

Reading 2's diagnostic role on ANCHOR-2 is preserved as off-F_2-residue-validates-clause-(e) (the K-invariance failure on supersets is the empirical content that JUSTIFIES the F_2-restricted protection theorem in (b)+(d) — without the off-F_2 residues at order O(1), there would be no asymmetric scoping to register). This is consistent with my L2 §"Asymmetric reading IS coherent" reading at workshop line 941. The Reading 1 / Reading 2 distinction is NOT a bifurcation requiring two theorems; it is the V→A_F→C chain's structural asymmetry surfaced as registry-text scoping.

I CONCEDE EM-3's parallel-governance reading. §VII.U.2 clause (f) and §VII.K-* family operate at distinct axis-systems (axis 1×2 vs axis 3) with distinct discipline forms (partition-prohibition vs composition-and-duality). Routes (b) and (c) of my Re:C3 BOTH collapse this parallel structure into a unified discipline; route (a) (Corrigendum 5) is the only remediation that preserves the parallel-governance topology that 3 already-registered §VII THM entries (DUAL + PROP + PROP-COMPOSITION) have invested in.

#### CV-L4 — Re: CV-1 / CV-2 / CV-3 confirmation reciprocation

I confirm connes's R2 CONVERGENCE: CV-1 (axis 3 IS substrate-IS at the §VII registry-anchor layer; my Re:C1 MISSED block reading is endorsed); CV-2 (ANCHOR-2 IS structurally MIXED-via-regulator-dressing on axis 3; the M_F2 normalizer's class-selectivity is a substrate-IS structural property); CV-3 (Q-L2 Reading-A is forced; §VII.K-* family retains §VII THM status). The convergence is symmetric: I do not retract any of Re:C1 / Re:C2 / Re:C5 / L1 / L2 reasoning that produced these conclusions, and I accept connes's R2 endorsement as canonical co-authorship of the three-axis substrate-IS framing.

The aggregate convergence is structurally significant: BOTH agents now agree on (i) three-axis substrate-IS partition (axis 1 operator-algebraic; axis 2 Mellin-pole; axis 3 regulator-class atlas); (ii) §VII.U.2 4-corner partition is the COARSE projection onto axes 1×2; (iii) axis 3 governed by §VII.K-* family in PARALLEL to clause (f); (iv) §VII.AH ANCHOR-2 is (INVARIANT, s=3, MIXED) on the 3-axis partition; (v) Reading 1 (F_2-restricted) is PRIMARY for ANCHOR-2; (vi) Corrigendum 5 (Route (a)) is the canonical in-place remediation; (vii) K=3 algebra-axis K-counter is preserved unchanged by the 3-class refinement.

### DISSENT

The DISSENT in this round is narrowly scoped. Per CV-L1+L2+L3, I have conceded the bulk of my Re:C3 substitution chain reading (b) and accept the parallel-governance / Corrigendum-5 framing as canonical. The remaining substantive disagreements are sharpening, not repetition.

#### DS-L1 — Re: DS-3 endorsement: Reading 2 carries DIAGNOSTIC value for off-F_2 atlas members under the asymmetric-scope reading

I AGREE with DS-3's Reading 1 PRIMARY assignment for ANCHOR-2 per clauses (b)+(d). I sharpen the dissent on the ROLE of Reading 2: DS-3's framing demotes Reading 2 to "structural-diagnostic enrichment" that "does NOT contradict Reading 1" (workshop lines 1253-1256). I argue Reading 2 carries STRUCTURAL DIAGNOSTIC STATUS for off-F_2 atlas members, NOT mere narrative enrichment — and the Corrigendum 5 text should reflect this elevation explicitly.

**Substitution chain — off-F_2 diagnostic content is the empirical justification for the asymmetric scoping, not a footnote to it**:

```
Definitions (per W7c WP line 693 + connes C2 Sage QQ table):
  Off-F_2 sub-atlas:    A_5 \ F_2 = {cutoff_sqrt, anomaly, Zubarev}
  Empirical content at obs1 (s=−1):
    xi²_0 off-F_2 = {9.578354, 2.748038, 13.327089}
    span_{A_5\F_2}(xi²_0)  = 13.327/2.748 = 4.85   (verified Python)
  Empirical content at s=3 (Sage QQ exact, connes C2):
    xi²_0 off-F_2 = {9.578207, 2.748341, 1.036345}
    span_{A_5\F_2}(xi²_0)  = 9.578/1.036 = 9.24   (verified Python)
  K-invariance-failure margins (registry §VII.AH clause (e), line 15435):
    924× / 298× / 798× factor margins on off-F_2 residues

Substitutions:
  Step 1: clause (b)+(d) registers F_2-restricted protection theorem
          (Reading 1 on ANCHOR-2).
  Step 2: clause (e) registers K-invariance failure ON SUPERSETS at orders
          924× / 298× / 798×. The off-F_2 residues ARE the empirical witness
          for clause (e); without them, (e) is unsupported.
  Step 3: the asymmetric scoping (V full-atlas; C F_2-restricted) is
          STRUCTURALLY MOTIVATED by clause (e)'s superset-failure content.
          V is broad BECAUSE the K-invariance failure on supersets is what
          the theorem characterizes (full-atlas K-invariance-failure premise);
          C is narrow BECAUSE the protection theorem only holds within F_2
          (per the order-O(1) failures on supersets at clause (e)).

Direction:
  Off-F_2 numerical residues are STRUCTURAL DIAGNOSTIC content for clause
  (e), not narrative-only enrichment to clause (b)+(d). Reading 2 on
  ANCHOR-2's off-F_2 residues IS what JUSTIFIES the asymmetric scoping
  registered in clauses (a)+(e) ↔ (b)+(d).

Conclusion:
  The Corrigendum 5 text must preserve off-F_2 diagnostic STATUS explicitly.
  Demoting them to "diagnostic-only" without specifying their structural
  role would lose the empirical content that clause (e) registers and that
  the asymmetric scoping rests on.
```

**Operational consequence**: my L2 Corrigendum 5 text proposal (workshop lines 949-953) already states off-F_2 residues "are diagnostic-only — they substantiate clause (e)'s K-invariance failure at order O(1) on supersets but are NOT part of the registered ANCHOR-2 theorem". I propose tightening this to: *"are diagnostic-only on ANCHOR-2's registered scope, AND are structural-witness content for clause (e)'s K-invariance-failure-on-supersets registered scope".* This makes the off-F_2 residues' dual role explicit — diagnostic on ANCHOR-2 (Reading 1 priority); structural-witness on ANCHOR-1's clause (e) (Reading 2 priority). The Corrigendum 5's R3 final text should reflect this dual-role reading.

#### DS-L2 — Re: Q-C3 (F_inv 3-class K-counter): NESTED-DISTINCT, not nested-with-shared-K-counter

connes's Q-C3 asks whether the F_inv-side 3-class refinement K-counter is nested inside or distinct from the axis-3 §VII.K-* family K-counter. My answer: **DISTINCT, with structurally-justified separation**. The argument:

```
Definitions:
  K-counter(axis 3 SUBSTRATE-IS REGISTRATION):
    domain = {§VII.K-DUAL, §VII.K-PROP, §VII.K-PROP-COMPOSITION}
    discipline level = AXIS-LEVEL (registers axis 3 as substrate-IS)
    K_saturated = 3 (per CV-1 substitution chain: 3 registered §VII THM
                     entries on axis 3)
    promotion event = axis 3 ∈ axis_substrate_IS

  K-counter(F_inv 3-class REFINEMENT):
    domain = {INVARIANT-FI-strict, INVARIANT-MIXED-via-RD, INVARIANT-RD-strict}
    discipline level = SUB-CLASS-WITHIN-AXIS (refines F_inv side of axis 3)
    K_saturated = 1-2 (per DS-2: A=firm, B=provisional, C=in-flight)
    promotion event = 3-class refinement upgrades SUGGESTION → MANDATORY

Substitutions:
  Step 1: K-counter(axis-3 SUBSTRATE-IS) discharges "is axis 3 registered as
          a substrate-IS axis at the §VII level?" — answered YES at K=3.
  Step 2: K-counter(F_inv 3-class) discharges "are sub-classes within F_inv
          on axis 3 promoted to MANDATORY-status structural refinement?" —
          currently NO at K=1-2.
  Step 3: the two questions are at DIFFERENT structural-discipline LAYERS:
          axis-level registration (1 question); sub-class-within-axis
          refinement (3 sub-questions, one per sub-class).

Direction:
  The two K-counters are DISTINCT because they discharge different structural
  questions at different layers:
    K-counter(axis-3): {axis 3 registered? YES at K=3, MANDATORY}.
    K-counter(F_inv 3-class): {sub-class refinement promoted? NO at K=1-2,
                                SUGGESTION; awaiting K=3 distinct loci}.
  Layer-functor F separation: the two layers do not share a K-counter under
  the rules-compensate-missing-structure threshold pattern.

Conclusion:
  K-counter(axis-3 SUBSTRATE-IS) is SATURATED at K=3 (MANDATORY).
  K-counter(F_inv 3-class REFINEMENT) is at K=1-2 (SUGGESTION).
  The two are structurally NESTED (F_inv 3-class lives WITHIN the F_inv side
  of axis 3) but operationally DISTINCT (different K-counter, different
  promotion event, different discipline-level).
```

**Why this matters for §VII.AH narrowing**: the Corrigendum 5 narrowing leverages axis-3 SUBSTRATE-IS status (K=3 saturated; CV-1 confirmed) as the structural foundation, NOT the F_inv 3-class refinement (K=1-2 SUGGESTION). The Corrigendum 5 text cites the asymmetric scoping (V full-atlas, C F_2-restricted) directly without invoking the FI-strict / MIXED-via-RD / RD-strict sub-class taxonomy as an enforcement mechanism. This nested-distinct K-counter framing keeps the Corrigendum 5 viable EVEN IF the F_inv 3-class refinement never reaches K=3 — the narrowing is structurally independent of the refinement's promotion status. I commit DS-L2 as the canonical answer to Q-C3.

#### DS-L3 — Re: Q-C1 (Corrigendum 5 commit ordering): commit Corrigendum 5 BEFORE §VII.U.2-EXT registration

connes's Q-C1 asks (a) commit Corrigendum 5 to §VII.AH and defer §VII.U.2-EXT to S89, OR (b) propose §VII.U.2-EXT preamble in R3 close as the structural framing under which Corrigendum 5 lands. connes leans (a). I AGREE with (a) but sharpen the dissent: not just temporal preference but **structural mandate** — Corrigendum 5 MUST land BEFORE §VII.U.2-EXT, and §VII.U.2-EXT requires its OWN K=3 calibration corpus before it can be registered.

**Substitution chain — why Corrigendum 5 ordering is structurally forced**:

```
Definitions:
  Corrigendum 5 = in-place §VII.AH registry-text addition disambiguating
                  ANCHOR-2's Reading 1 / Reading 2 scope. Operates ON
                  EXISTING registry text. No partition expansion.
  §VII.U.2-EXT = new registry entry promoting the §VII.U.2 4-corner
                 partition to 18-cell substrate-IS lattice (per EM-1).
                 Is a NEW STRUCTURAL THEOREM at the registry level.

Substitutions:
  Step 1: Corrigendum 5 is an in-session §VII.AH text edit.
          Required calibration: 1 instance (this workshop W-26 §VII.AH).
          Promotion threshold: in-session resolution of L2 / DS-3 reading.
          ⇒ Promotable at R3 close.

  Step 2: §VII.U.2-EXT is a forward methodology landing.
          Required calibration per cross-pillar-bridge-anatomy.md K-counter:
            K=3 distinct calibration instances on the 3-axis partition.
          Currently: K=1 (this workshop's 18-cell observation alone).
          Promotion threshold: NOT MET.
          ⇒ NOT promotable at R3 close; defer to S89 with explicit calibration
            target seeding.

  Step 3: ordering the two: Corrigendum 5 lands FIRST (in-session, W-26 R3
          close); §VII.U.2-EXT defers to S89 W0 plan with K=3 corpus pre-
          registered. Reverse ordering would either (i) couple Corrigendum
          5 to a §VII.U.2-EXT preamble that lacks K=3 calibration ⇒
          structurally invalid; OR (ii) defer Corrigendum 5 alongside
          §VII.U.2-EXT to S89 ⇒ leaves §VII.AH ambiguity un-fixed in-session
          ⇒ violates feedback_fix-in-session-never-defer.md.

Direction:
  Corrigendum 5 MUST land in R3 close (in-session fix, K=1-instance-suffices,
  in-place §VII.AH text).
  §VII.U.2-EXT MUST defer to S89 (forward methodology landing, K=3-required,
  new registry entry).
  The two are structurally INDEPENDENT in registration-pathway; coupling
  them invalidates §VII.U.2-EXT's calibration discipline.

Conclusion:
  Q-C1 answer: option (a). Corrigendum 5 lands in R3 close; §VII.U.2-EXT
  carry-forwards to S89 with K=3 calibration target seeding. They are
  ordered FIRST → SECOND, not coupled or simultaneous.
```

**Operational consequence**: the §VII.U.2-EXT 18-cell lattice registration (per EM-1) is a forward-looking methodology landing requiring its own calibration corpus. It cannot be promoted as part of this workshop's Wrap-Up; the §VII.AH narrowing decision at Corrigendum 5 is structurally independent of §VII.U.2-EXT's eventual promotion. Q-C2 (registry-landing.md asymmetric-scope SOURCE-DOUBLE-CITE registration) follows the same K-counter discipline (see EM-L3 below). The ordering discipline is uniform: in-session in-place fixes commit at R3 close; forward methodology landings carry-forward to S89 with K=3 calibration target.

### EMERGENCE

R1+R2 cross-pollination has produced three structural insights I had not articulated in R1 — each emerges from connes's CV-1+CV-2+CV-3 + DS-1 + EM-1+EM-2+EM-3 closing the loop with my L1+L2+L3 reasoning.

#### EM-L1 — Substrate-IS axes admit PARALLEL rule-file governance: a methodology-theorem candidate

The CV-1 conclusion (axis 3 substrate-IS) coupled with EM-3 (§VII.K-* family is PARALLEL governance to §VII.U.2 clause (f)) reveals a structural taxonomy that has not been registered as a methodology theorem: **substrate-IS axes admit DISTINCT rule-file governance per axis, with cross-axis disciplines governed by their own dedicated registry-theorem family rather than by uniform partition extension.**

**Substitution chain — parallel governance as methodology theorem**:

```
Definitions:
  substrate-IS axis catalog (post W-26):
    axis 1 (operator-algebraic):    governed by §VII.U.2 clauses (a)-(e)
    axis 2 (Mellin-pole):           governed by W-9 RULE-3 Pole-Scope sub-clause
                                     (MANDATORY-K=4 per S88 W7a-72)
    axis 3 (regulator-class atlas): governed by §VII.K-DUAL + §VII.K-PROP +
                                     §VII.K-PROP-COMPOSITION

  cross-axis disciplines:
    (axis 1 × axis 2): governed by §VII.U.2 clause (f) FORBIDDEN-cross-corner
                       (4-corner partition prohibition discipline)
    (axis 1 × axis 3): NOT YET REGISTERED — open question
    (axis 2 × axis 3): NOT YET REGISTERED — open question
    (axis 1 × axis 2 × axis 3): the EM-1 18-cell lattice; pending §VII.U.2-EXT.

Substitutions:
  Step 1: each substrate-IS axis has its OWN registry-discipline family;
          governance is NOT inherited by partition extension.
  Step 2: cross-axis disciplines require EXPLICIT registration; clause (f)
          covers (axis 1 × axis 2) ONLY; other cross-axis disciplines need
          their own rule-file landing.
  Step 3: §VII.K-* family on axis 3 emerged AS A PARALLEL governance, not as
          a clause (f) extension; this reflects the rule-file landing pattern
          for substrate-IS axes.

Direction:
  The structural taxonomy generalizes: K substrate-IS axes admit K dedicated
  registry-discipline families operating in parallel; cross-axis disciplines
  require K-counter-promoted registration, not implicit extension.

Conclusion:
  This taxonomy is a METHODOLOGY THEOREM CANDIDATE — call it the
  "PARALLEL-AXIS-GOVERNANCE THEOREM" — registered at registry-landing.md
  or epistemic-discipline.md as a structural pattern for S89+ rule-file
  landings of cross-axis disciplines. Calibration corpus seeding:
    Instance-1: §VII.U.2 clause (f) for (axis 1 × axis 2)
    Instance-2: §VII.K-* family for axis 3 governance
    Instance-3: TBD — needs forward landing on a cross-axis (axis 1 × axis 3)
                or (axis 2 × axis 3) discipline.
```

This is a NEW methodology-class observation. Per Q-C2's registration question, the parallel-governance theorem is more general than the asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY pattern (which is a particular instance of the broader pattern). I propose registering it at **`epistemic-discipline.md` §"Layer-Decomposition" or `registry-landing.md` §"PARALLEL-AXIS-GOVERNANCE"** as a methodology theorem with K-counter starting at K=2 (instances above) and K=3 promotion target gated on a third independent cross-axis discipline registration. This is forward-looking work appropriate for S89+ carry-forward, NOT in-session promotion.

#### EM-L2 — Asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY as a structural class with §VII.AH calibration: explicit generalization template

connes's EM-2 identified asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY as a NEW structural class with §VII.AH as Calibration Instance 1. I sharpen this with an EXPLICIT generalization template that forward §VII workshops can pattern-match against.

**Generalization template — asymmetric-scope sequential V→A_F→C chain**:

```
Asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY structural pattern:
  V (broad-scope premise)  := observable / theorem on broad atlas / scope X
  A_F (intermediate selector) := sub-atlas / scope-restriction Y ⊂ X
  C (narrow-scope theorem) := observable / theorem on Y, CONDITIONAL on V

3-condition test extension (extending registry-landing.md §"Detection"):
  (1*) sequential: C cannot be invoked without V (existing condition; unchanged)
  (2*) non-fungible-asymmetric: V's scope X ⊋ C's scope Y (NEW; the asymmetric
        scoping IS the source of non-fungibility — V and C cannot be swapped
        because they operate on structurally distinct scopes)
  (3*) both-accessibility: removing V invalidates C (V supplies the broad-scope
        premise that JUSTIFIES the scope-restriction Y); removing C leaves V
        without the operationalization C provides.

Calibration corpus (post W-26):
  Instance 1: §VII.AH (CV-L3 confirmed; W-26 close)
    V (ANCHOR-1) = M_R(s=3) 5-tuple on full A_5 atlas = full-atlas K-invariance
                    failure premise (Reading 2)
    A_F          = F_2 = {ζ, SDW} sub-atlas selector
    C (ANCHOR-2) = xi²_0(R) on F_2 = F_2-restricted protection theorem
                    (Reading 1, Corrigendum 5)
    Cardinality: |X| = |A_5| = 5; |Y| = |F_2| = 2; |X \ Y| = 3 (off-F_2
                    residues = K-invariance-failure margin substantiation)
  Instance 2: PENDING (forward; K-counter starting at K=1)
  Instance 3: PENDING (K=3 promotion target)

Forward-looking detection regex:
  Workshop seeds containing language like "V supplies the broad/full atlas
  premise; C supplies the sub-atlas-restricted theorem" OR "V is on the
  failure side; C is on the protection side" OR "asymmetric scoping V→A_F→C"
  pattern-match the asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY class.
```

**Operational consequence for Q-C2**: I AGREE with connes's lean toward registering at `registry-landing.md` (rather than retaining as an §VII.AH-specific note), with K-counter starting at K=1 (§VII.AH = Instance 1) and K=3 promotion target. The registration is forward methodology landing; per DS-L3 ordering discipline, it should NOT couple to Corrigendum 5's R3 close. Instead, register the asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY class as a SUGGESTION at `registry-landing.md` with K=1 calibration corpus (§VII.AH); future workshops surfacing similar V→A_F→C asymmetric chains advance K-counter; promotion to MANDATORY at K=3.

This generalization template is a structural extension of the existing `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` (which was registered for SAME-SCOPE sequential chains per the S86 W-3 Path-H/Path-C calibration corpus). The asymmetric-scope extension is genuinely novel and produces a forward-calibration pre-registration target — the structural value matches connes's Q-C2 lean.

#### EM-L3 — 18-cell substrate-IS lattice as registered methodology theorem: pre-registration target for §VII.U.2-EXT

connes's EM-1 endorsed my Re:C4 §"EMERGES" lattice reading (workshop line 752) as a registry-level structural insight. I sharpen with explicit pre-registration target structure for §VII.U.2-EXT.

**§VII.U.2-EXT pre-registration target (S89 carry-forward)**:

```
Theorem candidate name: §VII.U.2-EXT 18-CELL SUBSTRATE-IS LATTICE EXTENSION
Layer: methodology / registry — substrate-IS structural classification

Statement (draft):
  The §VII.U.2 4-corner partition is the COARSE projection π_{(1,2)} of an
  18-cell substrate-IS partition-cell function:
    partition_cell(F) := (axis_1(F), axis_2(F), axis_3(F))
  with axis 1 ∈ {INVARIANT, DEPENDENT}, axis 2 ∈ {s=3, s=4} (extensible per
  per-Bulletin-per-pole rule), axis 3 ∈ {FI-strict, MIXED-via-RD, RD-strict}
  on F_inv side; parallel structure on F_dep side TBD.

Structural content:
  - Axes 1, 2, 3 are pairwise structurally orthogonal (per CV-3 + EM-3)
  - π_{(1,2)} maps to the §VII.U.2 4-corner partition (clause-(f) discipline)
  - π_{(3)} maps to the §VII.K-* family discipline (composition + duality)
  - Cross-axis disciplines registered separately per EM-L1 PARALLEL-AXIS-
    GOVERNANCE THEOREM

K-counter discipline:
  K_promotion = 3 distinct calibration corpus instances on the 3-axis lattice.
  Calibration corpus seeding (post W-26):
    Instance 1: §VII.U.1 Mellin-Dirichlet at (INVARIANT, s=3, FI-strict)
                — registered §VII THM
    Instance 2: §VII.U.2 clause (a) Seeley-DeWitt at (INVARIANT, s=3, RD-strict)
                — registry-text citation (PROVISIONAL per DS-2)
    Instance 3: §VII.AH ANCHOR-2 at (INVARIANT, s=3, MIXED-via-RD)
                — STAGE-1-CANDIDATE per W-26 close
  Status: SUGGESTION at K=1-2 saturated (matches DS-2 + DS-L2 K-counter
  framing); K=3 promotion gated on additional structurally-distinct loci
  on the 3-axis lattice (e.g., (DEPENDENT, s=4, ?) instance; or a separate
  (INVARIANT, s=4, ?) instance with new pole-scope content).

Forward calibration target (S89+):
  - Land a §VII THM at (INVARIANT, s=4, RD-strict) — e.g., a_4^{regulator}
    Seeley-DeWitt coefficient at substrate-distance-2 pole with explicit
    regulator-class span analysis.
  - Land a §VII THM at (DEPENDENT, *, *) with explicit axis-3 tag.
  - Each new registered instance advances 18-cell lattice K-counter by 1.
```

**Operational consequence**: §VII.U.2-EXT is a forward methodology landing with K=3 calibration target. Per DS-L3 ordering discipline, it MUST defer to S89 with explicit calibration corpus pre-registration; it MUST NOT couple to Corrigendum 5's R3 close. The Wrap-Up "Carry-Forward Computations" section at R3 close should pre-register the §VII.U.2-EXT calibration target with the 4-field spec (what / inputs / gate / effort) per `feedback_fix-in-session-never-defer.md`. The structural reading — substrate-IS 18-cell lattice with parallel-governance per EM-L1 — is ALREADY PRESERVED by Corrigendum 5's in-place §VII.AH text fix; §VII.U.2-EXT registration adds rule-file structure but does not RETROACTIVELY change the §VII.AH narrowing decision.

The EM-L1 + EM-L2 + EM-L3 trio constitutes a coherent forward methodology landing pathway: PARALLEL-AXIS-GOVERNANCE THEOREM (general pattern) → asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY (specific pattern instance for V→A_F→C chains) → §VII.U.2-EXT 18-cell lattice (concrete substrate-IS partition registration). All three are SUGGESTION-status forward landings with K-counter pre-registration; none are in-session R3 promotions. R3 close commits Corrigendum 5 ONLY (per DS-L3); the trio carries forward to S89.

---

## Round 3 — connes: Follow-up

*[Workshop closure note: connes was not re-dispatched at R3. The text below is the synthesizer's stipulation of connes' R3 closure stance derived from connes' R2 substantive positions (CV-1 / CV-2 / CV-3 axis-3 substrate-IS concession lines 1018-1068; DS-1 / DS-2 / DS-3 narrowed-dissent lines 1072-1269; EM-1 / EM-2 / EM-3 forward-emergence lines 1275-1348; A-Q-L1 through A-Q-L5 + Q-C1/Q-C2/Q-C3 lines 1354-1409). The synthesizer is lizzi-spectral-functional-theorist; connes-side material below MUST NOT be cited as connes verbatim contribution. Connes co-sign of Corrigendum 5 commit text is queued as a forward-discipline cross-check at S89 (per CF-W26-7 below).]*

### CONVERGENCE

connes-side R3 closure (synthesizer-stipulated) crystallizes the four CV concessions of R2 into committed registry-class assignments and locks in lizzi's Corrigendum 5 endorsement as the canonical §VII.AH narrowing remediation:

**CV-3-LOCK**: Reading-A on Q-L2 stands. Seeley-DeWitt coefficients are simultaneously algebra-INVARIANT (parse-tree-INVARIANT BY CONSTRUCTION at axis 1) AND substrate-IS RD-strict at axis 3 (regulator-class atlas). §VII.K-DUAL (registry line 4108) + §VII.K-PROP (registry line 8976) + §VII.K-PROP-COMPOSITION (registry line 9272) retain their registered §VII THM status. C5's prior placement of FI/RD at the methodology layer was a layer-functor-F mis-assignment; the R2 CV-1 substitution chain (lines 1030-1051) producing K_axis(regulator-class atlas) = |{§VII.K-DUAL, §VII.K-PROP, §VII.K-PROP-COMPOSITION}| = 3 ≥ K_axis_promotion = 3 forces axis 3 onto the substrate-IS layer by registry-state cardinality. The publication-precision discipline (S82 W-3 RULE-3 mnemonic-vs-exact form; round-figure-forbidden) is the AUDIT-LEG IMAGE of axis 3 under F per `epistemic-discipline.md §"Layer-Decomposition"`, NOT the substrate-IS axis itself.

**Corrigendum 5 ENDORSEMENT (formal lock-in of DS-3 + lizzi DS-L1)**: lizzi's L2 §"§VII.AH narrowing entry text proposal" (workshop lines 949-953) is the canonical §VII.AH narrowing remediation, ELEVATED with lizzi's DS-L1 dual-role tightening (off-F_2 residues are diagnostic-only on ANCHOR-2's registered scope AND structural-witness content for clause (e)'s K-invariance-failure-on-supersets registered scope). The dual-role reading preserves the empirical content that clauses (a)+(e) register (924×/298×/798× margins on full-atlas K-invariance failure) AS THE STRUCTURAL JUSTIFICATION for the asymmetric scoping registered in clauses (b)+(d). Without the off-F_2 diagnostic, the asymmetric scoping is unmotivated; with it, the V → A_F → C chain reads as V (full-atlas K-invariance-failure premise) → A_F (F_2 = {ζ, SDW} sub-atlas selector) → C (F_2-restricted protection theorem CONDITIONAL on V) by structural design.

**EM-1 + EM-2 + EM-3 trio LOCK-IN as forward methodology landing pathway**: PARALLEL-AXIS-GOVERNANCE THEOREM (general pattern; EM-L1) → asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY (specific pattern instance; EM-L2) → §VII.U.2-EXT 18-cell substrate-IS lattice (concrete substrate-IS partition registration; EM-L3). All three are SUGGESTION-status forward landings with K-counter pre-registration; none are in-session R3 promotions per DS-L3 ordering discipline. R3 close commits Corrigendum 5 ONLY (asymmetric-scope sequential V→A_F→C chain; in-session in-place §VII.AH text fix; calibration K=1 = §VII.AH itself); the EM-L1/EM-L2/EM-L3 trio carries forward to S89 with K=3 calibration target seeding per `feedback_rules-compensate-missing-structure.md`.

### DISSENT

connes-side R3 dissent (synthesizer-stipulated) is structurally NARROW and converges on lizzi's DS-L2 nested-distinct K-counter framing rather than retaining substantive disagreement. The R2 DS-1 (clause (f) scope is the 4-corner partition) is REINFORCED at R3 close as a positive structural commitment, NOT as a residual dissent: clause (f) does NOT extend to axis 3 BY CONSTRUCTION (the registered text predicate "distinct corner cells" at registry line 12932 is definitionally bound to the clause-(d) 4-corner table); axis-3 discipline is governed by the §VII.K-* family in PARALLEL governance per EM-3 / EM-L1. This is the workshop's strongest joint commitment: parallel-disciplines reading is the canonical operational reading.

The DS-L2 nested-distinct K-counter framing (lizzi R2 lines 1582-1621) is endorsed as the R3 final canonical formulation: K-counter(axis-3 SUBSTRATE-IS REGISTRATION) is SATURATED at K=3 (MANDATORY by registry-state cardinality of 3 §VII.K-* THM entries; CV-1 substitution chain), AND K-counter(F_inv 3-class REFINEMENT) is at K=1-2 (SUGGESTION pending K=3 distinct calibration loci on the {FI-strict, MIXED-via-RD, RD-strict} sub-class taxonomy). The two K-counters discharge structurally distinct questions at distinct discipline layers (axis-level registration vs sub-class-within-axis refinement); they are nested but operationally distinct. The Corrigendum 5 narrowing leverages the K=3-saturated axis-3 substrate-IS status as its structural foundation, NOT the K=1-2 SUGGESTION-status F_inv 3-class refinement — making the narrowing structurally independent of whether the refinement ever reaches K=3 promotion.

### EMERGENCE

connes-side R3 emergence (synthesizer-stipulated) crystallizes three structural insights jointly co-authored across R1 + R2:

**E3-1 — Parallel-axis-governance is the canonical rule-file landing pattern for substrate-IS axes**: The structural taxonomy registered across §VII.U.2 clauses (a)-(e) (axis 1 governance), W-9 RULE-3 Pole-Scope sub-clause MANDATORY at K=4 (axis 2 governance), and §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION (axis 3 governance) reveals a structural pattern: **K substrate-IS axes admit K dedicated registry-discipline families operating in parallel; cross-axis disciplines require K-counter-promoted explicit registration, NOT implicit partition extension.** The pattern emerges from the workshop and lands as a methodology-theorem candidate at S89 carry-forward (see CF-W26-3 below).

**E3-2 — Asymmetric-scope sequential V → A_F → C chain is structurally NEW**: The §VII.AH theorem's chain (V supplies broad-atlas premise on full A_5; A_F is sub-atlas selector F_2 = {ζ, SDW}; C supplies sub-atlas-restricted theorem on F_2 conditional on V) extends `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` 3-condition test from same-scope sequential chains (S86 W-3 calibration) to asymmetric-scope sequential chains. The 3-condition test extension at lizzi EM-L2 (workshop lines 1744-1751) — sequential / non-fungible-asymmetric / both-accessibility — preserves the SOURCE-DOUBLE-CITE structural content while admitting the broader-V / narrower-C scope asymmetry as a structurally legitimate variant. §VII.AH is Calibration Instance 1 of the new asymmetric-scope class; K-counter pre-registration starts at K=1 with K=3 promotion target seeded for forward landing (see CF-W26-2 below).

**E3-3 — 18-cell substrate-IS lattice as registry-class structural extension**: The §VII.U.2 4-corner partition is the COARSE projection π_{(1,2)} of the substrate-IS 3-axis lattice at canonical resolution 2 × 2 × 3 = 12 sub-cells per side (with parallel structure on F_dep-side, full cardinality TBD); the §VII.K-* family discipline operates on the axis-3 fiber. EM-1 proves the projection identity 4-corner = π_{(1,2)}(18-cell); future §VII registry entries SHOULD be tagged at the 18-cell resolution for structural transparency AND at the 4-corner resolution for clause-(f) admissibility. The registration as §VII.U.2-EXT (substrate-IS lattice extension) is queued as forward methodology landing with K=3 calibration target (see CF-W26-4 below).

### QUESTIONS

connes-side R3 questions (synthesizer-stipulated) focus on commit-ordering for the trio of forward landings and on the boundary conditions of the asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY generalization:

**Q-R3-C1 (resolved at lizzi DS-L3)**: Confirmed — Corrigendum 5 lands FIRST in R3 close (in-session in-place §VII.AH text fix); §VII.U.2-EXT defers to S89 with K=3 calibration corpus pre-registered. The two are structurally independent in registration-pathway; coupling them invalidates §VII.U.2-EXT's calibration discipline and violates `feedback_fix-in-session-never-defer.md` for the §VII.AH ambiguity. Lizzi's DS-L3 substitution chain (workshop lines 1632-1675) is the canonical answer.

**Q-R3-C2 (resolved at lizzi EM-L2)**: Confirmed — the asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY class registers at `registry-landing.md` (NOT only as an §VII.AH-specific note), with §VII.AH = Instance 1 (K=1) and K=3 promotion target. The structural value of pre-registering the calibration corpus matches the K-counter discipline of `feedback_rules-compensate-missing-structure.md`.

**Q-R3-C3 (resolved at lizzi DS-L2)**: Confirmed — F_inv 3-class refinement K-counter is DISTINCT from axis-3 §VII.K-* family K-counter (nested-distinct framing). The two discharge structurally different questions at different discipline layers. Corrigendum 5 leverages axis-3 substrate-IS status (K=3 saturated) as its structural foundation; the narrowing is structurally independent of the F_inv refinement's K=3 promotion.

**Q-R3-C4 (open; carry-forward to S89)**: For Corrigendum 5's forward consumers (obs2 anomaly s=4/s=2 integer-graded factorized; obs3 Mellin-residue-ratio s=3/s=4 pole-scope test), how does the asymmetric-scope reading interact with W-9 RULE-3 Pole-Scope MANDATORY-K=4? Specifically: does the F_2 sub-atlas selection at s=4 differ from F_2 = {ζ, SDW} at s=3, and if so, does the asymmetric scoping carry pole-dependent A_F-selector content? Pre-registered S89 follow-up gate (see CF-W26-5 below).

**Q-R3-C5 (open; carry-forward to S89)**: Does the parallel-axis-governance pattern (E3-1 / EM-L1) imply that any FUTURE substrate-IS axis surfaced (e.g., a hypothetical 4th axis from a new registered §VII.X-* family) would inherit the same parallel-governance discipline by construction, or does each new axis require independent rule-file landing? The structural answer determines whether the methodology-theorem candidate status of EM-L1 promotes once at K=3 or recurs per new axis.

---

## Round 3 — lizzi: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

The R1 + R2 cross-pollination produced a sequence of structural concessions on both sides; my R3 final-round position locks in the joint convergence and commits Corrigendum 5 as the binding §VII.AH narrowing remediation. The convergence is now substrate-deep — not a procedural agreement to a verdict but a structural co-authoring of the three-axis substrate-IS framing.

**CONV-L-R3-1 — Three-axis substrate-IS partition is JOINT CO-AUTHORED at §VII registry-anchor weight**: Both agents now agree (i) axis 1 (operator-algebraic, parse-tree π(a) test) is substrate-IS at §VII.U.2 clauses (a)-(e); (ii) axis 2 (Mellin-pole {s=3, s=4}) is substrate-IS at W-9 RULE-3 Pole-Scope sub-clause (MANDATORY at K=4 per S88 W7a-72); (iii) axis 3 (regulator-class atlas span_{A_5}(F)) is substrate-IS at the §VII.K-* family (DUAL + PROP + PROP-COMPOSITION; 3 registered §VII THM entries saturating K=3 by registry-state cardinality per CV-1 substitution chain). The K-axis K-counter formulation (lines 1030-1051) — `K_axis(regulator-class atlas) = |{§VII.K-DUAL, §VII.K-PROP, §VII.K-PROP-COMPOSITION}| = 3 ≥ K_axis_promotion = 3` — converted my Re:C1 MISSED reading from a workshop-internal claim into a registry-state-derived structural commitment. This is the workshop's strongest joint result: it shifts the FI/RD axis from a methodology-layer publication discipline (connes C5 placement) to a substrate-IS axis (CV-1 forced placement), which in turn forces Reading-A on Q-L2 and pins §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION as STRUCTURAL §VII THMs that cannot be re-classified as methodology rules.

**CONV-L-R3-2 — Parallel-disciplines reading of clause (f) and §VII.K-* family is ENDORSED with attribution to connes DS-1**: I retract my Re:C3 substitution chain reading (b) (the cross-corner FORBIDDEN-co-primary extension to a 3-axis partition). Connes's DS-1 substitution chain (lines 1080-1124) correctly reads the registered text predicate "distinct corner cells" at registry line 12932 as definitionally bound to the clause-(d) 4-corner table (axes 1 × 2), NOT a hypothetical N-axis extension. Axis-3 discipline is governed by the §VII.K-* family operating in PARALLEL governance, NOT by clause (f). The parallel-disciplines topology is structurally cleaner than partition expansion would be — and per EM-3 it preserves the rule-file landing pattern that 3 already-registered §VII THM entries (DUAL + PROP + PROP-COMPOSITION) have invested in. My Re:C3 reading (b) was a structural EXTRAPOLATION beyond registered text scope.

**CONV-L-R3-3 — Corrigendum 5 commit text + dual-role disambiguation locks in BOTH-WAYS**: My L2 §"§VII.AH narrowing entry text proposal" (workshop lines 949-953) is the binding §VII.AH narrowing remediation, ELEVATED with the DS-L1 dual-role tightening that off-F_2 numerical residues at obs1 ({9.578354, 2.748038, 13.327089} per W7c WP §W7c-167 line 693, s=−1 evaluation; verified by direct division: 13.327089/2.748038 = 4.84963 to 5 sig figs) are DIAGNOSTIC-ONLY on ANCHOR-2's registered scope (Reading 1 priority via clauses (b)+(d)) AND STRUCTURAL-WITNESS CONTENT for clause (e)'s K-invariance-failure-on-supersets registered scope (Reading 2 diagnostic role via clauses (a)+(e)). The dual-role reading preserves the V → A_F → C asymmetric scoping by construction: V's broad scope IS justified by the order-O(1) failures registered at clause (e) (924×/298×/798× margins on full-atlas K-invariance failure); C's narrow scope IS the F_2-restricted protection theorem CONDITIONAL on V. Corrigendum 5 makes the asymmetric scoping EXPLICIT in registry text without splitting into two theorems — a single theorem with explicit Reading 1 / Reading 2 scoping disambiguation.

**CONV-L-R3-4 — Forward methodology trio (EM-L1 / EM-L2 / EM-L3) carries forward to S89 with K=3 calibration target seeding**: PARALLEL-AXIS-GOVERNANCE THEOREM (general pattern) → asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY (specific instance for V → A_F → C asymmetric chains) → §VII.U.2-EXT 18-cell substrate-IS lattice (concrete substrate-IS partition registration). The trio is structurally NESTED but operationally INDEPENDENT — each landing has its own K-counter, its own promotion threshold, and its own calibration corpus seeding. Per DS-L3 ordering discipline, the trio defers to S89 with explicit calibration target pre-registration; R3 close commits Corrigendum 5 ONLY (in-session in-place fix, K=1 instance suffices, in-place §VII.AH text addition). The structural reading — substrate-IS 18-cell lattice with parallel-governance per EM-L1 — is ALREADY PRESERVED by Corrigendum 5's text fix; §VII.U.2-EXT registration adds rule-file structure but does not RETROACTIVELY change the §VII.AH narrowing decision.

### DISSENT

R3 final-round dissent is STRUCTURALLY EMPTY on the §VII.AH narrowing decision (the workshop converges fully on Corrigendum 5 + dual-role tightening) and STRUCTURALLY NARROW on forward calibration corpus expectation. The remaining narrow-dissent items are not adjudicated to a winner but are pinned as open questions for S89+:

**DS-L-R3-1 — F_inv 3-class refinement promotion timeline is STRUCTURALLY UNCERTAIN, not procedurally pre-determined**: Per DS-2 + DS-L2, K-counter(F_inv 3-class REFINEMENT) is at K=1-2 saturated (Instance-A firm = §VII.U.1 Mellin-Dirichlet identity FI-strict; Instance-B provisional = §VII.U.2 clause (a) Seeley-DeWitt RD-strict; Instance-C in-flight = §VII.AH ANCHOR-2 MIXED-via-RD pending Stage-2 close). The K=3 MANDATORY promotion threshold is not reached. Forward calibration target: the framework needs to surface AT LEAST ONE additional structurally-distinct registered §VII THM at one of the three F_inv sub-classes — e.g., a separately-registered MIXED-via-RD instance beyond §VII.AH (perhaps from a future Bulletin at substrate-distance-2 pole s=4 with explicit F_2-conditional sub-atlas structure), OR a separately-registered RD-strict instance with explicit regulator-class span analysis on a new functional. Until then, the 3-class refinement is SUGGESTION-status. NARROW DISSENT vs connes' implicit DS-2 reading: I read the K=1-2 status as STRUCTURALLY OPEN-ENDED (the refinement may stay SUGGESTION indefinitely if forward sessions don't surface additional §VII THM landings at the sub-class level), while connes' DS-2 framing (workshop lines 1162-1200) reads it as PRE-DETERMINED PENDING ROUTE (waiting for K=3 to land). The structural difference is whether the rule operates as accumulator (sociological-metric framing) or as forward-pinned-promotion (engineering-metric framing). I lean accumulator (matches `feedback_rules-compensate-missing-structure.md` discipline pattern); connes' DS-2 lean is ambiguous. Resolution deferred to S89 calibration corpus reservation.

**DS-L-R3-2 — Cross-axis disciplines beyond axis-1 × axis-2 are NOT fully scoped**: Per EM-L1, the parallel-axis-governance taxonomy admits cross-axis disciplines (axis 1 × axis 3), (axis 2 × axis 3), and (axis 1 × axis 2 × axis 3). Only the (axis 1 × axis 2) cross-discipline is currently registered (§VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary). The other cross-axis disciplines are NOT YET REGISTERED — open question. NARROW DISSENT vs connes Q-R3-C5: I read the parallel-axis-governance pattern (EM-L1) as forward-prescriptive (any future substrate-IS axis surfaced should inherit parallel-governance by construction; cross-axis disciplines should require explicit K-counter-promoted registration); the alternative reading is per-axis-bespoke (each new axis requires fresh rule-file landing without inheritable pattern). The structural difference matters for S89+ workshops surfacing new §VII.X-* families — does EM-L1 register once at K=3 with the pattern as forward-binding, or does it recur per-axis? Resolution: EM-L1 promotion to MANDATORY at K=3 SHOULD pin the forward-prescriptive reading explicitly so future workshops have an unambiguous template.

### EMERGENCE

R3 final-round emergence harvests three structural insights that crystallize ONLY at the cross-synthesis layer — they were not articulated in either R1 or R2 individually but emerge from the CV-L1 + CV-L2 + CV-L3 + CV-L4 + DS-L1 + DS-L2 + DS-L3 + EM-L1 + EM-L2 + EM-L3 cross-pollination:

**EM-L-R3-1 — The §VII.AH theorem's "Joint F_2-Class Path-(c) Theorem" name is structurally ELEVATED by Corrigendum 5 dual-role reading**: The theorem name embeds the F_2-class identity AS THE STRUCTURAL CORE; Corrigendum 5 makes the F_2-class restriction (Reading 1 priority on ANCHOR-2) the registered scope. Combined with the dual-role reading (off-F_2 residues structural-witness for clause (e)), the theorem's full structural content reads: "the F_2-class joint K-invariance protection theorem holds CONDITIONAL on a full-atlas K-invariance-failure premise empirically witnessed by the off-F_2 atlas residue spread at order O(1) margins". This is a sharper theorem statement than either R1's "Joint F_2-Class Path-(c) Theorem" (under-specified scoping) or a hypothetical "Full-atlas K-invariance Theorem" (would not preserve the F_2-class restriction). The name + Corrigendum 5 + dual-role reading together pin the theorem at its structurally optimal scope.

**EM-L-R3-2 — The xi²_0(R) M_F2-normalizer class-selectivity IS the structural mechanism the §VII.K-DUAL FI-Duality Theorem registers**: §VII.K-DUAL (registry line 4108) registers FI-Duality between M_lizzi and M_connes classification functors. The M_F2 normalizer's class-selectivity (FI-on-F_2 EXACT; RD-on-A_5\F_2 with class-residue) IS an OPERATIONAL realization of FI-Duality at the substrate-IS observable level — the F_2 normalizer choice IS the duality functor's restriction to the F_2 sub-atlas. This is EM-L2's asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY pattern's structural mechanism: V supplies the full-atlas premise (broad-scope on which FI-Duality is non-trivial); C supplies the F_2-restricted theorem (narrow-scope on which FI-Duality is satisfied EXACTLY). The §VII.K-DUAL theorem and the §VII.AH theorem's V → A_F → C structure are therefore structurally INTERLOCKED — neither is a methodology rule, both are §VII registered THMs, and the V → A_F → C chain instantiates the FI-Duality operationalization at substrate-IS layer.

**EM-L-R3-3 — Layer-functor F preserves PARALLEL-AXIS-GOVERNANCE under axis-extension; this is a NEW preservation result for F**: Per `epistemic-discipline.md §"Layer-Decomposition"`, F : substrate → methodology → audit preserves PRU-class invariants (Class 8.0/8.1/8.2/8.3 sub-taxonomy). I propose a NEW preservation result (S89 carry-forward): F also preserves the parallel-axis-governance pattern under axis-extension. Specifically: if axis K is registered as substrate-IS via a §VII.X-* family (K_axis = 3 saturation), then F's audit-leg image registers an analogous audit-discipline family at the audit floor (e.g., a hypothetical `_axis_K_governance_audit.py` analog of `_a_n_regulator_pin_audit.py`). The methodology-floor image is the per-axis rule-file family (§VII.U.2 clauses for axis 1; W-9 RULE-3 Pole-Scope for axis 2; §VII.K-* family for axis 3). This is structurally NEW: F was previously characterized by PRU-class invariant preservation only; the parallel-axis-governance preservation extends F's structural content. Calibration corpus: 3 axes registered at K=3 (axis 1 / axis 2 / axis 3) — this is K=3 saturation BY EXISTING REGISTRY STATE for the F-preservation result. The promotion to MANDATORY at K=3 is structurally available; landing as a methodology theorem extension at `epistemic-discipline.md §"Layer-Decomposition"` is the canonical S89 carry-forward target (CF-W26-3 below).

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Parse-tree decision capture vs FI/RD axis | C1, Re:C1, CV-1, CONV-L-R3-1 | **Converged** (parse-tree captures axis 1 only; FI/RD lives at orthogonal axis 3, substrate-IS) | Parse-tree π(a) test of §VII.U.2 clause (e) is the canonical algebra-axis discriminator at the OPERATOR-ALGEBRAIC LAYER (axis 1) and is regulator-INDEPENDENT BY CONSTRUCTION; FI/RD operates at axis 3 (regulator-class atlas) which is substrate-IS at the §VII registry-anchor layer per CV-1 substitution chain (K_axis = 3 saturated by §VII.K-DUAL + §VII.K-PROP + §VII.K-PROP-COMPOSITION). The two axes are STRUCTURALLY ORTHOGONAL substrate-IS at distinct discipline layers, not refinements of each other. |
| 2 | xi²_0(R) FI vs RD classification | C2, Re:C2, CV-2, L2 | **Converged** (MIXED-via-regulator-dressing on axis 3; FI-on-F_2 EXACT, RD-on-A_5\F_2) | xi²_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) is parse-tree-INVARIANT at axis 1 (no π(a) AST refs) AND MIXED-via-regulator-dressing at axis 3: span_{F_2}(xi²_0) = 1 EXACT (Sage QQ 1581/1581; F_2 cancellation at obs1 numerical = 13.642473/13.642473 EXACT); span_{A_5}(xi²_0) = 13.16 at s=3 (Sage QQ 15810/1201) and 4.85 at s=−1 (W7c WP line 693 obs1 numerical: 13.327089/2.748038). The M_F2 normalizer is a STRUCTURAL F_2-class projector by construction; the FI-on-F_2 / RD-on-off-F_2 asymmetry is preserved across pole transitions. |
| 3 | §VII.AH narrowing trigger | C3, Re:C3, DS-1, CV-L1, CONV-L-R3-2, CONV-L-R3-3 | **Converged** (Corrigendum 5 Route (a) is canonical; clause (f) does NOT extend to axis 3) | §VII.U.2 clause (f) FORBIDDEN-cross-corner-co-primary discipline is scoped to the 4-corner partition (axes 1 × 2) BY REGISTERED TEXT at registry line 12932 ("distinct corner cells" = clause-(d) 4-corner table); axis 3 is governed by §VII.K-* family in PARALLEL governance per EM-3. §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY is INTRA-corner-I admissible per §VII.U.2 NOTE (registry line 12901) and the asymmetric scoping (V full-atlas RD; C F_2-restricted FI) is the V → A_F → C structural content. Corrigendum 5 (lizzi L2 narrowing entry text + DS-L1 dual-role tightening) is the canonical in-place §VII.AH text fix; routes (b) §VII.U.2 partition expansion and (c) §VII.K-* re-classification are both REJECTED. |
| 4 | FI/RD trichotomy refinement of algebra-INVARIANT/DEPENDENT | C4, Re:C4, L1, DS-2, CV-L2, DS-L2 | **Partial** (3-class refinement structurally legitimate; K=1-2 SUGGESTION; K-counter NESTED-DISTINCT) | The F_inv 3-class refinement {INVARIANT-FI-strict, INVARIANT-MIXED-via-RD, INVARIANT-RD-strict} is structurally legitimate per CV-1 (axis 3 substrate-IS) but its K-counter is at K=1-2 saturated (Instance-A firm = §VII.U.1 Mellin-Dirichlet identity; Instance-B provisional = §VII.U.2 clause (a) Seeley-DeWitt corpus; Instance-C in-flight = §VII.AH ANCHOR-2). Status SUGGESTION pending K=3 distinct calibration loci. K-counter(F_inv 3-class REFINEMENT) is DISTINCT from K-counter(axis-3 SUBSTRATE-IS REGISTRATION; saturated at K=3 MANDATORY by §VII.K-* family cardinality). The two K-counters discharge structurally different questions at different discipline layers; nested but operationally distinct. The K=3 algebra-axis K-counter (S87 W-2 R3 close) is preserved unchanged. |
| 5 | Cross-cutting / parse-tree vs FI/RD relationship | C5, L1, L2, CV-1+2+3, EM-1+2+3, EM-L1+L2+L3, EM-L-R3-3 | **Emerged** (three-axis substrate-IS partition + parallel-axis-governance methodology theorem candidate) | Three substrate-IS axes (axis 1 operator-algebraic / axis 2 Mellin-pole / axis 3 regulator-class atlas) admit pairwise structural orthogonality and parallel registry-discipline governance: §VII.U.2 clauses (a)-(e) for axis 1; W-9 RULE-3 Pole-Scope for axis 2; §VII.K-* family for axis 3. §VII.U.2 4-corner partition is COARSE projection π_{(1,2)} of the 18-cell substrate-IS lattice (EM-1). Asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY (V broader-scope, C narrower-scope) is a NEW structural class extension to `registry-landing.md §"Detection"` with §VII.AH as Calibration Instance 1 (EM-2 / EM-L2). PARALLEL-AXIS-GOVERNANCE is a methodology theorem candidate (EM-L1) whose F-preservation property (EM-L-R3-3) is structurally available at K=3 saturation by existing registry state. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

The workshop converged fully on the §VII.AH narrowing decision (Corrigendum 5 + dual-role disambiguation; Verdict #3 Converged) and on the three-axis substrate-IS framing (Verdict #1 Converged; Verdict #5 Emerged). Open questions concentrate at three layers: (i) in-session §VII.AH text commit ordering, (ii) S89 forward methodology landings (§VII.U.2-EXT 18-cell lattice; PARALLEL-AXIS-GOVERNANCE THEOREM; asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY at registry-landing.md), (iii) cross-axis discipline scope clarification.

1. **§VII.AH Corrigendum 5 commit text + dual-role tightening — IN-SESSION commit at S88 close OR S89 W0 in-place edit?**: Per DS-L3 ordering, Corrigendum 5 must land BEFORE §VII.U.2-EXT registration. Open question: does the Corrigendum 5 text edit on `sessions/permanent-results-registry.md §VII.AH` land at S88 close (this workshop's R3 close direct-edit) OR carry forward to S89 W0 plan (where it becomes a 0.2-wave-equivalent METHODOLOGY-class registry edit)? Per `feedback_fix-in-session-never-defer.md`, in-session is preferred; per `feedback_session-process.md`, parallel-writer race protection forbids shared-file Edit during workshop closure. Pre-registered gate: `S89-VII-AH-CORRIGENDUM-5-DUAL-ROLE-LAND` PASS = Corrigendum 5 text + dual-role disambiguation appended to §VII.AH after L-CR3.3 amendment to clause (e); explicit Reading 1 priority + off-F_2 dual-role text; cross-link to W-26 audit_sha256 and to obs1 W7c WP line 693 numerical witness; FAIL = text not landed or fails to encode the dual-role reading.

2. **§VII.U.2-EXT 18-cell substrate-IS lattice extension landing at S89**: Per EM-L3 + DS-L3, §VII.U.2-EXT is forward methodology landing with K=3 calibration target. The pre-registered structure: 4-corner partition is COARSE projection π_{(1,2)} of 18-cell substrate-IS partition (axis 1 × axis 2 × axis 3). Calibration corpus seeded at K=1-2 (Instance 1 = §VII.U.1 Mellin-Dirichlet at (INVARIANT, s=3, FI-strict); Instance 2 = §VII.U.2 clause (a) Seeley-DeWitt at (INVARIANT, s=3, RD-strict) provisional; Instance 3 = §VII.AH ANCHOR-2 at (INVARIANT, s=3, MIXED-via-RD) in-flight). Pre-registered gate: `S89-VII-U-2-EXT-18-CELL-LATTICE-SUGGESTION-LAND` PASS = §VII.U.2-EXT entry appended to permanent-results-registry.md citing the 3-axis lattice structural identity + 4-corner = π_{(1,2)}(18-cell) projection identity + K=1-2 saturated calibration corpus + 1+ reserved K-counter rows for forward calibration; status SUGGESTION; FAIL = entry conflates 18-cell with §VII.U.2 partition OR omits the projection identity OR pre-registers MANDATORY status without K=3 corpus.

3. **PARALLEL-AXIS-GOVERNANCE THEOREM landing at `epistemic-discipline.md §"Layer-Decomposition"` as F-preservation extension**: Per EM-L1 + EM-L-R3-3, the parallel-axis-governance pattern is a NEW structural property of the layer-functor F (preservation of parallel-axis governance under axis-extension). Calibration corpus: K=3 saturated by 3 axes already registered (axis 1 § VII.U.2 clauses; axis 2 W-9 RULE-3 Pole-Scope; axis 3 §VII.K-* family). Pre-registered gate: `S89-LAYER-DECOMP-F-PARALLEL-AXIS-GOVERNANCE-LAND` PASS = sub-section appended to `epistemic-discipline.md §"Layer-Decomposition"` documenting parallel-axis-governance preservation under F as a NEW preservation result; K=3 calibration corpus rows inline; F-image decomposition (substrate / methodology / audit) per axis listed; cross-link to W-26 calibration; status MANDATORY at K=3 by existing registry state per `feedback_rules-compensate-missing-structure.md`; FAIL = sub-section conflates parallel-axis-governance with PRU-class invariant preservation OR omits the K=3 calibration.

4. **Asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY structural class registration at `registry-landing.md`**: Per EM-L2 + Q-R3-C2, the asymmetric-scope sequential V → A_F → C chain extension to the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern is a structural extension of `registry-landing.md §"Detection"`. Calibration: K=1 with §VII.AH as Instance 1; K=3 promotion target. Pre-registered gate: `S89-REGISTRY-LANDING-ASYMMETRIC-SCOPE-SOURCE-DOUBLE-CITE-LAND` PASS = sub-section appended to `registry-landing.md` after §"SOURCE-DOUBLE-CITE-CO-PRIMARY"; 3-condition test extension (sequential / non-fungible-asymmetric / both-accessibility) explicit; §VII.AH calibration row inline; 2 reserved K-counter rows; status SUGGESTION; FAIL = sub-section folds into the existing same-scope SOURCE-DOUBLE-CITE-CO-PRIMARY definition without distinguishing asymmetric scope OR omits the V-broader-than-C scope-asymmetry condition (2*).

5. **Pole-scope interaction with asymmetric-scope reading at obs2/obs3 forward dispatches (Q-R3-C4)**: For Corrigendum 5's forward consumers obs2 (anomaly s=4/s=2 integer-graded factorized; absent at workshop dispatch) and obs3 (Mellin-residue-ratio s=3/s=4 pole-scope test; absent at workshop dispatch), how does the F_2 sub-atlas selection at s=4 differ from F_2 = {ζ, SDW} at s=3? Pre-registered gate: `S89-VII-AH-OBS2-OBS3-POLE-DEPENDENT-F_2-SCAN` PASS = obs2 + obs3 substrate-IS computations executed; F_2-cancellation EXACT preserved at s=4 within the s=4-specific F_2 sub-atlas; off-F_2 spread reported per pole; pole-scope discipline (W-9 RULE-3 MANDATORY-K=4) integrity verified across s ∈ {s=2, s=3, s=4}; FAIL = F_2-cancellation breaks at s=4 (would invalidate Corrigendum 5's pole-AGNOSTIC F_2-sub-atlas registration).

6. **F_inv 3-class refinement K-counter forward calibration target seeding (DS-L-R3-1 narrow-dissent resolution)**: Per CV-L2 + DS-L2, K-counter(F_inv 3-class) is at K=1-2 SUGGESTION. Open question: which forward §VII THM landings advance the K-counter? Candidate forward calibration targets: (a) a §VII.X-class entry at (INVARIANT, s=4, RD-strict) — e.g., a_4^{regulator} Seeley-DeWitt at substrate-distance-2 pole with explicit cross-class span analysis; (b) a separately-registered MIXED-via-RD instance beyond §VII.AH on a new functional with explicit F_S-conditional sub-atlas structure; (c) a separately-registered FI-strict instance beyond §VII.U.1 with explicit cross-pole identity statement. Pre-registered gate: `S89-VII-K-FAMILY-F_INV-3-CLASS-K-COUNTER-RESERVATION` PASS = at least one of the three forward calibration targets pre-registered as a S89+ §VII landing target with explicit K-counter advancement criterion; FAIL = K-counter pre-registration deferred without forward target seeding.

7. **Connes-side R3 dispatch — formal cross-sign of synthesizer-stipulated R3 close**: Per the workshop closure note at the top of §"Round 3 — connes: Follow-up", connes was not re-dispatched. The synthesizer-stipulated R3 closure stance is derived from connes' R2 substantive positions (CV-1/2/3, DS-1/2/3, EM-1/2/3, A-Q-L1-L5, Q-C1/C2/C3) but does NOT carry connes' verbatim R3 endorsement. Pre-registered gate: `S89-W26-CONNES-R3-FORMAL-CROSS-SIGN` PASS = connes-ncg-theorist re-dispatched at S89 W0 with the R3 closure note + Corrigendum 5 + dual-role tightening; cross-sign emitted as agree/disagree-with-amendment verdict; if amendment requested, narrow workshop reopen at W26-R3-amendment for resolution; FAIL = formal cross-sign skipped or workshop closure note never validated.

8. **Closing-paragraph-coherence audit pattern (W-25 EG1) extension to W-26 cross-axis discipline rule-files**: The W-25 EG1 closing-paragraph-coherence audit pattern (per `epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"`) was deployed to one rule (`mechanical-closure-discipline.md §"PLANNING DEFECT"`) at K=1. The W-26 workshop produced THREE new candidate rule-file landings (PARALLEL-AXIS-GOVERNANCE THEOREM at `epistemic-discipline.md §"Layer-Decomposition"`; asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY at `registry-landing.md`; §VII.U.2-EXT lattice extension at `permanent-results-registry.md`). Open question: should the EG1 audit pattern be applied PRE-LANDING to verify the closing paragraphs of these candidate sub-sections do not introduce closing-paragraph-coherence contradictions? Pre-registered gate: `S89-EG1-PRE-LAND-COHERENCE-AUDIT-W26-CANDIDATES` PASS = EG1 audit pattern applied to each S89 landing's draft text before commit; report records (sub-section × candidate-reading × contradiction-status) triples; INFO = audit performed, no contradictions surfaced; FAIL = audit skipped or audit pattern itself surfaces contradiction in W-26-derived landings.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **§VII.AH STAGE-1-CANDIDATE registry-anchor structure adjudicated as INTRA-corner-I admissible under Corrigendum 5 + dual-role tightening** (Verdict #3 Converged): the §VII.AH SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure passes both clause-(f) discipline (intra-corner-I admissible per §VII.U.2 NOTE registry line 12901) AND axis-3 §VII.K-* family discipline (asymmetric-scope V → A_F → C is the structural content of the V→A_F→C chain, governed by §VII.K-PROP composition behavior). Reading 1 (F_2-restricted scope on ANCHOR-2 per clauses (b)+(d)) is PRIMARY; off-F_2 numerical residues are diagnostic-only on ANCHOR-2 AND structural-witness content for clause (e)'s K-invariance-failure-on-supersets registered scope (Reading 2 dual-role).
- **FI/RD axis is substrate-IS at the §VII registry-anchor layer, NOT at methodology layer** (Verdict #1 Converged via CV-1): K_axis(regulator-class atlas) = |{§VII.K-DUAL, §VII.K-PROP, §VII.K-PROP-COMPOSITION}| = 3 saturated by registry-state cardinality. The publication-precision discipline (S82 W-3 RULE-3; round-figure-forbidden; mnemonic-vs-exact) is the AUDIT-LEG IMAGE of axis 3 under F, not the substrate-IS axis itself. Connes' R1 C5 placement of FI/RD at methodology layer is REVISED.
- **Three-axis substrate-IS partition (axis 1 / axis 2 / axis 3) jointly co-authored at workshop close** (Verdict #5 Emerged): §VII.U.2 4-corner partition is COARSE projection π_{(1,2)} of the substrate-IS 18-cell lattice; axis 3 is governed by §VII.K-* family in PARALLEL governance to clause (f) (parallel-disciplines reading endorsed via DS-1 / EM-3 / CONV-L-R3-2). The asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY pattern (V broader-scope; C narrower-scope) is a NEW structural class with §VII.AH as Calibration Instance 1.

### What Holds

- **The K=3 algebra-axis orthogonality K-counter (S87 W-2 R3 close, MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md` lines 272-280) is preserved unchanged**: the workshop's 3-class F_inv refinement (FI-strict / MIXED-via-RD / RD-strict) operates WITHIN the algebra-INVARIANT side at axis 3, not as recalibration of the (INVARIANT vs DEPENDENT) coarse axis. W1b-6 + S-2 + W-2 K=3 calibration corpus stays unchanged; the K-counter saturation status holds at MANDATORY.
- **§VII.K-DUAL FI-Duality Theorem (registry line 4108) + §VII.K-PROP CC-5 propagation identity (registry line 8976) + §VII.K-PROP-COMPOSITION lattice-join rule (registry line 9272) retain their registered §VII THM status** per CV-3 + Q-L2 Reading-A forced; no re-classification to methodology rules. Their joint cardinality 3 = K_axis_promotion saturates the axis-3 substrate-IS registration.
- **Parse-tree π(a) decision procedure (§VII.U.2 clause (e) registry line 12930) is the canonical operator-algebraic discriminator at axis 1**: regulator-INDEPENDENT BY CONSTRUCTION; finite, decidable; same classification under cutoff, ζ, Pauli-Villars, Mellin regulators. Connes' C1 framework stands at the operator-algebraic layer; the workshop only revises the layer-assignment of the FI/RD axis (axis 3 substrate-IS, not methodology), not the parse-tree decision itself.
- **§VII.U.2 4-corner partition (algebra-axis × Mellin-pole) at registry lines 12921-12928 is structurally complete on the registry-anchor-discriminator scope it covers**; clause (f) FORBIDDEN-cross-corner-co-primary at registry line 12932 is correctly scoped to the 4-corner partition by registered text. Lizzi's R1 Re:C3 reading (b) cross-corner extension to a 3-axis partition is RETRACTED per CV-L1.
- **xi_E_GGE_inv = 13.642473425595973 canonical scalar (S86 branch-iv-canonical; canonical_constants.py provenance pin)** is unchanged by the workshop; bit-identity preserved across obs1 numerical evaluation (W7c WP §W7c-167 line 693) and downstream Corrigendum 5 text. The substrate-natural anchor (59.8 · Δ_BCS / K_base; lizzi 9A §2.2 formula source) holds.
- **Verdict-line content for §W7c-167 obs1 audit on disk is ABSOLUTELY PERMANENT** (per `gate-verdicts.md §"Rules"` item 2): this workshop adjudicates registry-text scope (Corrigendum 5) but does NOT touch verdict-line audit_sha256 / content_sha256 / value strings / scheme tags / convention tags / L_max for the W7c-167 PASS-AND verdict.

### What Breaks or Strains

- **The §VII.AH text in `sessions/permanent-results-registry.md` is internally consistent under the asymmetric-scope reading but DIAGNOSTICALLY UNDER-SCOPED at workshop dispatch**: clauses (a)+(e) read ANCHOR-1 as full-atlas K-invariance-failure premise (Reading 2); clauses (b)+(d) read ANCHOR-2 as F_2-restricted protection theorem (Reading 1). The asymmetric scoping is registered BY CONSTRUCTION but is NOT EXPLICITLY DOCUMENTED in §VII.AH text — Corrigendum 5 fixes this by adding the disambiguation paragraph. The strain is methodological (forward registry consumers may misread §VII.AH as full-atlas-FI by default in absence of Corrigendum 5).
- **The F_inv 3-class refinement {INVARIANT-FI-strict, INVARIANT-MIXED-via-RD, INVARIANT-RD-strict} is structurally legitimate but K=1-2 SUGGESTION**: K-counter promotion requires structurally-distinct registered §VII THM landings beyond the workshop-internal calibration corpus. Forward calibration loci are NOT pre-registered at workshop close (see CF-W26-6); the refinement may stay SUGGESTION indefinitely under DS-L-R3-1's accumulator-framing reading.
- **Cross-axis disciplines beyond axis-1 × axis-2 are NOT yet rule-file-landed** (DS-L-R3-2): only the (axis 1 × axis 2) cross-discipline (clause (f)) is currently registered; (axis 1 × axis 3), (axis 2 × axis 3), and (axis 1 × axis 2 × axis 3) cross-axis disciplines require explicit K-counter-promoted rule-file landings per the parallel-axis-governance pattern. The workshop does not pre-register these cross-axis disciplines; they remain forward-pinned methodology landing targets.
- **The synthesizer-stipulated R3 closure stance for connes-ncg-theorist is structurally derived from R2 substantive positions but lacks formal connes verbatim cross-sign** at workshop close: per CF-W26-7, the formal cross-sign is queued to S89 W0 dispatch. Until that lands, the §VII.AH Corrigendum 5 commitment is a single-author (lizzi-side) commitment with synthesizer-stipulated co-author endorsement; the bilateral consistency holds per R2 connes DS-3 endorsement explicitly at workshop lines 1267-1270 ("I therefore now ENDORSE lizzi's Corrigendum 5 narrowing proposal at L2"), but cross-axis bilateral co-authorship at the §VII.AH text-edit level requires the explicit cross-sign event.
- **The §VII.U.2-EXT 18-cell substrate-IS lattice extension is K=1-2 SUGGESTION-status forward methodology landing**: the 18-cell projection identity 4-corner = π_{(1,2)}(18-cell) is structurally established at the workshop, but the rule-file registration as §VII.U.2-EXT must defer to S89 with K=3 calibration corpus pre-registered (per DS-L3 ordering discipline). The structural reading is preserved by Corrigendum 5; the rule-file landing is not.

### Carry-Forward Computations

1. **§VII.AH Corrigendum 5 + dual-role disambiguation in-place text edit**
   - **What**: append Corrigendum 5 text (lizzi L2 §"§VII.AH narrowing entry text proposal" workshop lines 949-953) to §VII.AH after L-CR3.3 amendment to clause (e), ELEVATED with the DS-L1 dual-role tightening: off-F_2 residues are "diagnostic-only on ANCHOR-2's registered scope, AND structural-witness content for clause (e)'s K-invariance-failure-on-supersets registered scope". Reading 1 priority on ANCHOR-2 explicit; Reading 2 dual-role on off-F_2 residues explicit; cross-link to W-26 audit_sha256 + W7c WP §W7c-167 line 693 numerical witness.
   - **Inputs**: existing §VII.AH text at `sessions/permanent-results-registry.md` lines 15399-15479; Corrigendum 5 draft text from L2 (workshop lines 949-953); DS-L1 dual-role tightening (workshop lines 1535-1573); W-26 workshop audit_sha256 (computed at workshop close); W7c WP §W7c-167 line 693 obs1 5-tuple verbatim cite.
   - **Gate**: `S89-VII-AH-CORRIGENDUM-5-DUAL-ROLE-LAND` PASS = Corrigendum 5 + dual-role text appended; explicit Reading 1 priority + dual-role off-F_2 reading; cross-link to W-26 + W7c-167; xi_E_GGE_inv canonical citation = 13.642473425595973 (canonical_constants.py provenance preserved); status STAGE-1-CANDIDATE preserved per `joint-theorem-promotion.md` 4-stage pathway. FAIL = Corrigendum 5 missing dual-role tightening OR registers Reading 1 / Reading 2 conflation OR touches verdict-line content for §W7c-167.
   - **Effort**: 0.2 wave-equivalents (METHODOLOGY-class per `wave-classification.md` M1∧M2∧M3∧M4; registry-text edit only; no compute; mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`).

2. **Asymmetric-scope SOURCE-DOUBLE-CITE-CO-PRIMARY landing at `registry-landing.md`**
   - **What**: append a NEW sub-section to `registry-landing.md` after §"SOURCE-DOUBLE-CITE-CO-PRIMARY" defining the asymmetric-scope sequential V → A_F → C chain extension (per EM-L2 generalization template workshop lines 1738-1769). The 3-condition test extension: (1*) sequential (existing); (2*) non-fungible-asymmetric (NEW; V's scope strictly contains C's scope); (3*) both-accessibility (existing). §VII.AH is Calibration Instance 1 (K=1); 2 reserved K-counter rows for K=2/K=3 promotion target.
   - **Inputs**: existing `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` text (S86 W-3 calibration baseline); EM-L2 generalization template (workshop lines 1738-1769); W-26 §VII.AH calibration data (V = M_R(s=3) full A_5 atlas; A_F = F_2 = {ζ, SDW} sub-atlas selector; C = xi²_0(R) F_2-restricted protection theorem).
   - **Gate**: `S89-REGISTRY-LANDING-ASYMMETRIC-SCOPE-SOURCE-DOUBLE-CITE-LAND` PASS = sub-section appended; 3-condition test extension explicit (sequential / non-fungible-asymmetric / both-accessibility); §VII.AH calibration row inline (V scope, A_F selector, C scope, cardinality |X|=5, |Y|=2, |X\Y|=3); 2 reserved K-counter rows; status SUGGESTION; cross-link to W-26 audit_sha256. FAIL = sub-section folds into existing same-scope SOURCE-DOUBLE-CITE-CO-PRIMARY OR omits the V-broader-than-C scope-asymmetry condition.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class).

3. **PARALLEL-AXIS-GOVERNANCE THEOREM landing at `epistemic-discipline.md §"Layer-Decomposition"` as F-preservation extension**
   - **What**: append a NEW sub-section to `epistemic-discipline.md §"Layer-Decomposition"` documenting the parallel-axis-governance pattern as a NEW preservation result for the layer-functor F (per EM-L1 + EM-L-R3-3). Statement: "F preserves parallel-axis governance under axis-extension: K substrate-IS axes admit K dedicated registry-discipline families operating in parallel; cross-axis disciplines require K-counter-promoted explicit registration." K=3 calibration corpus rows inline (axis 1 §VII.U.2 clauses; axis 2 W-9 RULE-3 Pole-Scope; axis 3 §VII.K-* family); status MANDATORY at K=3 by existing registry-state cardinality.
   - **Inputs**: existing `epistemic-discipline.md §"Layer-Decomposition"` content (substrate ↔ methodology, methodology ↔ audit, Phi correspondence, PRU-class invariant preservation); EM-L1 parallel-governance theorem candidate (workshop lines 1689-1727); EM-L-R3-3 F-preservation extension (workshop R3 EMERGENCE).
   - **Gate**: `S89-LAYER-DECOMP-F-PARALLEL-AXIS-GOVERNANCE-LAND` PASS = sub-section appended; parallel-axis-governance preservation explicit; K=3 calibration corpus rows inline; F-image decomposition (substrate / methodology / audit) per axis listed (audit-leg image extension to per-axis governance audit script TBD as separate carry-forward); cross-link to W-26 calibration; status MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. FAIL = sub-section conflates parallel-axis-governance with PRU-class invariant preservation OR omits the K=3 calibration corpus.
   - **Effort**: 0.4 wave-equivalents (METHODOLOGY-class; structural new preservation result requires more text than rule-extension landings).

4. **§VII.U.2-EXT 18-cell substrate-IS lattice extension landing at `sessions/permanent-results-registry.md`**
   - **What**: append §VII.U.2-EXT entry to permanent-results-registry.md (per EM-L3 pre-registration target workshop lines 1783-1820). Statement: "§VII.U.2 4-corner partition is the COARSE projection π_{(1,2)} of an 18-cell substrate-IS 3-axis partition (axis 1 × axis 2 × axis 3); axis 1 ∈ {INVARIANT, DEPENDENT}, axis 2 ∈ {s=3, s=4} extensible per per-Bulletin-per-pole rule, axis 3 ∈ {FI-strict, MIXED-via-RD, RD-strict} on F_inv side with parallel structure on F_dep TBD." 4-corner = π_{(1,2)}(18-cell) projection identity explicit; axis-3 governance via §VII.K-* family in parallel referenced; calibration corpus seeded at K=1-2 (Instance 1 = §VII.U.1; Instance 2 = §VII.U.2 clause (a) provisional; Instance 3 = §VII.AH ANCHOR-2 in-flight); status SUGGESTION pending K=3 promotion.
   - **Inputs**: existing §VII.U.2 text at registry lines 12913-12932 (4-corner partition + clause (f) + parse-tree + calibration corpus); EM-L3 pre-registration target structure (workshop lines 1783-1820); CF-W26-1 Corrigendum 5 (must land FIRST per DS-L3 ordering); §VII.K-* family registered THM entries for axis-3 cross-reference.
   - **Gate**: `S89-VII-U-2-EXT-18-CELL-LATTICE-SUGGESTION-LAND` PASS = §VII.U.2-EXT entry appended after §VII.U.2; projection identity 4-corner = π_{(1,2)}(18-cell) explicit; calibration corpus K=1-2 saturated rows inline; 1+ reserved K-counter rows for forward calibration; status SUGGESTION; cross-link to W-26 + parallel-axis-governance landing (CF-W26-3) + asymmetric-scope SOURCE-DOUBLE-CITE landing (CF-W26-2). FAIL = entry pre-registers MANDATORY status without K=3 corpus OR omits the projection identity OR conflates 18-cell with §VII.U.2 4-corner partition.
   - **Effort**: 0.4 wave-equivalents (METHODOLOGY-class; new registry entry with structural-theorem-candidate weight; mack-cosmic-bridge sole writer).

5. **§VII.AH obs2 + obs3 forward dispatches under Corrigendum 5 pole-AGNOSTIC F_2 sub-atlas reading**
   - **What**: dispatch obs2 (anomaly s=4/s=2 integer-graded factorized) and obs3 (Mellin-residue-ratio s=3/s=4 pole-scope test) substrate-IS computations, verifying that F_2-cancellation EXACT preserved at s=4 within the s=4-specific F_2 sub-atlas selection AND that off-F_2 spread carries pole-dependent class-residue. The structural prediction under Corrigendum 5: F_2 sub-atlas selection at s=4 may differ from F_2 = {ζ, SDW} at s=3, and the asymmetric scoping carries pole-dependent A_F-selector content; the F_2-cancellation EXACT property must hold pole-AGNOSTICALLY at the F_2-sub-atlas level (whatever sub-atlas selection that pole canonicalizes).
   - **Inputs**: §VII.AH STAGE-1-CANDIDATE registry text + Corrigendum 5 (CF-W26-1); Mellin-residue M_R(s) computation infrastructure (S87 W7 obs1 dispatch as template at `s87_w7_ic_per_class_verify.npz`); pole-Scope discipline (W-9 RULE-3 MANDATORY-K=4 per S88 W7a-72); spectral-functional regulator atlas A_5 = {ζ, SDW, cutoff_sqrt, anomaly, Zubarev}.
   - **Gate**: `S89-VII-AH-OBS2-OBS3-POLE-DEPENDENT-F_2-SCAN` PASS = obs2 + obs3 substrate-IS computations executed via `s89_w*_vii_ah_obs2_obs3_pole_dependent_f2_scan.py`; F_2-cancellation EXACT preserved at s=4 + s=2 within s-specific F_2 sub-atlas; off-F_2 spread reported per pole; pole-scope discipline integrity verified across s ∈ {s=2, s=3, s=4}; verdict-line scheme tag = "VII-AH-pole-AGNOSTIC-F_2-sub-atlas"; FAIL = F_2-cancellation breaks at s=4 (would invalidate Corrigendum 5's pole-AGNOSTIC F_2-sub-atlas registration).
   - **Effort**: 1.0 wave-equivalents (COMPUTE-class; substrate-IS Mellin-residue computation at L_max=10; spectral-functional atlas scan at 2 new poles; PRDR pre-registered).

6. **F_inv 3-class refinement K-counter forward calibration target seeding**
   - **What**: pre-register at least one of the three forward calibration target candidates per DS-L-R3-1: (a) §VII.X-class entry at (INVARIANT, s=4, RD-strict) — e.g., a_4^{regulator} Seeley-DeWitt at substrate-distance-2 pole with explicit cross-class span analysis; (b) separately-registered MIXED-via-RD instance beyond §VII.AH on a new functional with explicit F_S-conditional sub-atlas structure; (c) separately-registered FI-strict instance beyond §VII.U.1 with explicit cross-pole identity statement. Pin one specific forward calibration target as S89+ §VII landing target with K-counter advancement criterion explicit.
   - **Inputs**: F_inv 3-class refinement definitions at L1 (workshop lines 786-797); §VII.U.1 + §VII.U.2 clause (a) + §VII.AH existing calibration corpus; W-9 RULE-3 Pole-Scope sub-clause (extensible to s ≥ 5); §VII.K-* family discipline.
   - **Gate**: `S89-VII-K-FAMILY-F_INV-3-CLASS-K-COUNTER-RESERVATION` PASS = forward calibration target pre-registered at the §VII.K-* family meta-level; explicit K-counter advancement criterion (which of (a)/(b)/(c) the target instantiates); reserved K-counter row for forward landing; status SUGGESTION pending K=3. FAIL = K-counter pre-registration deferred without forward target seeding OR multiple targets pre-registered without single explicit K-counter advancement criterion.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class; calibration corpus reservation; no compute).

7. **Connes-ncg-theorist formal cross-sign of synthesizer-stipulated R3 closure stance**
   - **What**: re-dispatch connes-ncg-theorist at S89 W0 with the W-26 synthesizer-stipulated R3 closure note (lines 1830-1843 of `sessions/archive/session-88/workshops/s88-w26-w7c-167-corner-I-co-primary.md`) + Corrigendum 5 + dual-role tightening; emit cross-sign as agree/disagree-with-amendment verdict. If amendment requested, narrow workshop reopen at W26-R3-amendment for resolution; otherwise commit cross-sign event to workshop document and proceed with CF-W26-1 commit.
   - **Inputs**: W-26 workshop document (this file) lines 1829-1843 (synthesizer-stipulated R3 connes closure); Corrigendum 5 text (CF-W26-1); R2 connes DS-3 endorsement at workshop lines 1267-1270 (verbatim "I therefore now ENDORSE lizzi's Corrigendum 5 narrowing proposal at L2") as baseline.
   - **Gate**: `S89-W26-CONNES-R3-FORMAL-CROSS-SIGN` PASS = connes cross-sign verdict emitted; agree-without-amendment OR agree-with-amendment-applied; workshop document updated with cross-sign event + verdict-line; CF-W26-1 commit unblocked. FAIL = formal cross-sign skipped or amendment requires structural reopen at W26-R3-amendment.
   - **Effort**: 0.2 wave-equivalents (cross-sign-only dispatch; no new substantive content unless amendment requested; planner-skill consultation).

8. **EG1 closing-paragraph-coherence audit pattern PRE-LANDING application to W-26 candidate sub-sections**
   - **What**: apply the W-25 EG1 closing-paragraph-coherence audit pattern (per `epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"`) to each of the W-26 candidate rule-file landings (CF-W26-2 / CF-W26-3 / CF-W26-4) BEFORE commit, verifying the closing paragraphs do not introduce closing-paragraph-coherence contradictions. Report (sub-section × candidate-reading × contradiction-status) triples; remediate or hold commits where contradictions surface.
   - **Inputs**: EG1 audit-pattern specification (`epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"`); W-26 candidate sub-section drafts (CF-W26-2 + CF-W26-3 + CF-W26-4 text); W-25 EG1 calibration as template.
   - **Gate**: `S89-EG1-PRE-LAND-COHERENCE-AUDIT-W26-CANDIDATES` PASS = EG1 audit applied to each of CF-W26-2 / CF-W26-3 / CF-W26-4 draft text; report records (sub-section × candidate-reading × contradiction-status) triples; INFO = audit performed, no contradictions surfaced; FAIL = audit pattern itself surfaces contradiction in W-26-derived landings (would force pre-commit remediation).
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class; audit-pattern application to 3 sub-section drafts; ~0.1 wave-equiv each).

### Closing Line

The W-26 workshop converges on the three-axis substrate-IS framing (axis 1 operator-algebraic / axis 2 Mellin-pole / axis 3 regulator-class atlas) with axis 3 forced onto the substrate-IS layer by registry-state cardinality of §VII.K-* family entries; the §VII.AH STAGE-1-CANDIDATE narrowing remediation lands as Corrigendum 5 + dual-role disambiguation, preserving SOURCE-DOUBLE-CITE-CO-PRIMARY admissibility under the asymmetric V-→-A_F-→-C reading without forcing §VII.U.2 partition expansion or §VII.K-* re-classification.
