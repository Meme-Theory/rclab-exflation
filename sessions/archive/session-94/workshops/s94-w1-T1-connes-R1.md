# W-1 Turn 1 — connes-ncg (Reading A steelman)

**Workshop**: W-1, §VII.AU.OP-PROJ α=−3 discharge status adjudication
**Turn**: T1 (steelman of Reading A; NO convergence, NO concession — strongest case only)
**Agent**: connes-ncg-theorist (Reading A owner; author of the S94 W2-3 derivation)
**Adjudication options on the table**: (a) FULL-RECOVERED honest; (b) structural-posit/consistency-confirmed with SCHEMATIC cap preserved; (c) two-layer split; (d) re-tag fine but verdict-line/registry must be reconciled.
**This turn argues for (a)** — and, where (a) needs a containment, pre-positions (c) as the fallback that PRESERVES (a)'s core claim, never (b).

---

## 0. The thesis, stated once and sharply

> The exponent `α = −3` of the §VII.AU.OP-PROJ Layer-1 convergence envelope is **not a fitted number**. It is the cohomology-class envelope exponent `−(d−1)` at `d = 4`, fixed by the structure of the substrate-distance-1 Mellin-cone pole `s = 3` on the finite spectral triple `(A_K, H_K, D_K)`. It is **regulator-invariant** at the cohomology-class layer (Layer-1, pole-universal F₂-class), and it is **L-independent**: it is `−3` at every `L`, including `L = ∞`, including the never-diagonalized window. The `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → FULL-RECOVERED` re-tag is therefore **honest**, because the object the corridor was deferring — the asymptotic value of the leading exponent — is *recovered as a structural fact*, not as an extrapolation residual. The `LEVEL_CLASS_PIN=SCHEMATIC tier_pin=TIER-2` annotation tags the **provenance of the numerical anchor's sourcing protocol**, not the structural status of the exponent; a sourcing-axis tag cannot cap a cohomology-class-axis recovery, because the two live on orthogonal axes (`epistemic-discipline.md §"Layer-Decomposition"` Phi-correspondence).

Everything below is the substitution chain and the cohomology-class reasoning that makes each clause of that thesis load-bearing.

---

## I. SUBSTRATE-FIRST framing (the direction of explanation)

The substrate IS the spectral triple `(A_K, H_K, D_K)` at the substrate-distance-1 Mellin-cone pole `s = 3`. `α` is a **substrate-IS spectral-functional**: it is the leading decay exponent of the residual

```
R_b(L) = ρ_FULL(s=3, L) − ρ_FULL(s=3, ∞)
```

between the finite-L bottom-K Mellin moment-ratio and its `L_max → ∞` HKR image. It is NOT a measurement made IN a container, NOT a quantity that "lives on" a continuum we are approximating. The continuum BZ-trace is the **laboratory-IN image** of the substrate-IS Hochschild pairing under the HKR bridge map (registry IS-not-IN anatomy, element 3: `HKR L_max → ∞`, Connes-Moscovici 1995 §III.4). The exponent governs the *rate* at which the substrate-IS finite-L observable presents its own `L_max → ∞` shadow. The question "what is α?" is therefore a question about the **spectral geometry of the fabric**, answerable from the pole structure of the dimension spectrum — not a question about how well a numerical fit converged.

This direction is the whole ballgame. Reading B's case, as I will show in T3, only has force if you (silently) invert this direction and treat the in-window numbers as the *primary* object and the cohomology-class exponent as a *posit about* them. Inverted, the SCHEMATIC tag looks like a cap. In the correct direction, the exponent is prior and the numbers are its finite-L shadow.

---

## II. The exponent is `−(d−1)`, structurally fixed — the cohomology-class reasoning

### II.1 The substitution chain (every symbol explicit)

The claim "α_asymptotic = −3" reduces, with no fit, to "−(d−1) = −3 at d=4". The chain (Sage-confirmed each step; verdict WP §W2-3 Step 1–4):

```
Step 1 [definition]:  The substrate-distance-1 pole is at s = 3 on a d = 4 spectral triple
                      (CM-1995 §III.4 simple-pole residue on Cell I; canonical
                      alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC, S91 W-5 EMERGENCE row 5).
                      [source: knowledge MCP get_constant — value −3.0, CLASS line]

Step 2 [definition]:  The Mellin-cone envelope governing the approach of a finite-L
                      dimension-spectrum residue to its continuum image at a d-dim pole
                      is  R_b(L) ~ c · L^{−(d−1)}.
                      The exponent −(d−1) is the codimension-1 boundary scaling of the
                      Mellin cone — the geometric envelope of the pole, fixed by d.

Step 3 [substitute]:  d = 4  ⇒  −(d−1) = −(4−1) = −3.        [Sage: −(d−1) = −3, exact]

Step 4 [read off]:    α_asymptotic = −3.   SIGN: −3 < 0 ⇒ NEGATIVE ⇒ convergent.
```

There is **no degree of freedom** in Steps 2–4. `d = 4` is the spectral dimension of the triple (an axiom-level invariant — the dimension spectrum's top simple pole; not adjustable). `−(d−1)` is the cone-boundary exponent. The conclusion `−3` is forced. This is the same `α = d − 1 = 3` result that the framework's W-5 d=4 envelope work registered for the §VII.AF.1 Pillar III↔IV bridge (knowledge MCP: *"W-5 Level-2 envelope at d=4 ... exponent α = d − 1 = 3"*) — **the SAME structural exponent appears at SAME d across distinct bridges**, which is exactly the signature of a structural fact rather than a per-gate fit.

### II.2 Why this is a *cohomology-class* statement, not a numerical one

The exponent `−(d−1)` is a property of the **Hochschild/Mellin pole**, i.e. of the cohomology class `[φ]` paired against `Ch(P_0)` in the IS-not-IN anatomy (registry element 1: `R_universal = ⟨[φ_n_s^sym], [Ch(P_0(τ_fold))]⟩`). The pole order and its cone exponent are determined by:

- the **orientability axiom** (the Hochschild cocycle representing the volume form fixes the top dimension `d`),
- the **dimension axiom** (the spectral triple is `d`-summable; the dimension spectrum's leading simple pole sits at the codimension determined by `d`),
- the **regularity axiom** (the residue functional `Res_{s=d-1}` is well-defined; the Wodzicki/Dixmier residue is the unique trace, Connes 1994 §2.3).

None of these is a fit parameter. They are the NCG axioms that the §VII.AU spectral triple satisfies (the framework's 6/7-axiom KK structure; the relevant axioms here — dimension, regularity, orientability — all hold). The exponent is read off the **class**, and classes do not move under the operations that the SCHEMATIC tag is about (numerical sourcing of a scalar). This is precisely the registry's own PROVEN statement, which I did not invent and which pre-dates this gate:

> **Level-1 layer (asymptotic universal): leading-term `−3` is REGULATOR-INVARIANT, L-INDEPENDENT cohomology-class identity at the Cell I × substrate-distance-1 pole `s = 3`.** — `permanent-results-registry.md`, status PROVEN (knowledge MCP `search_knowledge` theorem hit).

So the structural status of `−3` is **already a proven theorem in the registry**, independent of the W2-3 gate. W2-3 did not *establish* `−3`; it **discharged the deferral of reading it off via the analytic-saturation route**. The deferral was operational ("derive the asymptotic limit via the saturation argument so the bridge's Level-2 binding envelope is confirmed at its asymptotic limit"), not structural ("is the exponent −3?"). The structural answer was already PROVEN. That is the cleanest possible ground for "FULL-RECOVERED": you cannot be deferring a number whose structural value is a standing theorem; what you defer is the *certification that the chosen evaluation route lands on that theorem*, and that certification is exactly what W2-3 delivered.

---

## III. Regulator-invariance at the cohomology-class layer — the F₂-class identity

Reading B's strongest move is to point at `REGULATOR_PIN=a_4^{Mellin}` and `LEVEL_CLASS_PIN=SCHEMATIC` and say "this is one regulator's answer; it is not regulator-robust." This move **fails at the exponent layer**, and the reason is a second standing identity I did not invent:

> **`sub_term_R(Mellin) = sub_term_R(zeta) = 0` at d=4 substrate-distance-1 pole `s = 3`** — *"shifted between Mellin Re(s) > α₀ and zeta Re(s) = s* + ε via Cauchy's theorem with no extra pole crossings at d=4 substrate-distance-1."* (knowledge MCP `search_knowledge` structural hit, s91-w5 adjudication.)

The substitution chain for regulator-invariance:

```
Step 1:  α_R = leading exponent of R_b(L) under regulator R.
Step 2:  For R ∈ F₂ = {Mellin, zeta}, the two evaluations are CONTOUR variants of the
         SAME analytic continuation of the same dimension-spectrum residue:
            M[·](s) along Mellin contour  ≡  ζ-regulated residue along zeta contour,
         related by deforming the contour Re(s): α₀ → s*+ε.
Step 3:  At d=4 substrate-distance-1 (pole s=3), Cauchy's theorem gives NO extra pole
         crossings in the deformation strip ⇒ sub_term_R(Mellin) = sub_term_R(zeta) = 0.
Step 4:  Equal analytic object on both contours ⇒ α_Mellin = α_zeta EXACT at s=3.
         ⇒ The leading exponent is INVARIANT across the F₂ contour-deformation class.
```

This is the **FI (Functional-Invariant) classification** in the lizzi taxonomy, at the F₂-axis sub-projection (`regulator-pin-discipline.md §"β_shell FI Classification"`: *"β_shell is INVARIANT across the F₂ = {ζ, SDW} K-invariant identity sub-atlas"*; the parent F_traj a₂-ratio FI theorem; and the registry's own *"the within-channel F_2-axis FI contour-deformation identity (α_Mellin = α_zeta EXACT at s=3, CM-1995 §III.4) are PRESERVED"*, WP §W2-3 line 157). The β_shell sibling at the SAME d=4 s*=3 pole is registry-PROVEN FI: *"Level 3 per-shell shell-sum exponent ... β_shell ≈ 1.885 at d=4 substrate-distance s* = 3 IS FI at the F_2-class projection."* The α=−(d−1) exponent inherits the SAME FI class on the SAME axis.

**Consequence:** the exponent does not depend on the regulator within F₂. The `a_4^{Mellin}` UV-regulator pin is the *evaluation route*; the FI theorem says the *exponent* is the same on the ζ contour. The regulator-pin discipline's own four-axis orthogonality table makes this explicit — the UV-regulator axis (`a_n^{regulator}`) and the structural exponent are *different things*; tagging the route as Mellin does not make the exponent route-dependent when the route lives in an FI class.

This is the decisive separation Reading B must overcome and (I will argue in T3) cannot: **regulator-invariance of the exponent is a theorem about the contour-deformation class, established by Cauchy's theorem; the SCHEMATIC tag is about the numerical sourcing of a scalar pin.** They are not the same axis, so the second cannot veto the first.

---

## IV. The SCHEMATIC tier_pin is a SOURCING artifact, not a recovery cap — the orthogonal-axis argument

Here is the heart of why (a) is correct and (b) overreaches.

### IV.1 What the SCHEMATIC tag actually pins

Per `substrate-first-canonical-sourcing.md §(iv)` (K=4), `LEVEL_CLASS_PIN=SCHEMATIC` is a disclosure on the **CLASS pin axis**: it discloses that `alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = −3` was sourced via the *"SCHEMATIC two-pin convergence-exponent protocol"* (Level-1 asymptotic pin `−3` + Level-3 pre-asymptotic sample pin `+2.6926`), with `rho_FULL_CC_VII_AU_SAT_s3` PROVENANCE. The rule's own purpose statement (verbatim): the tag exists so that *"gate verdicts under SCHEMATIC helpers are NOT structurally indistinguishable from FULL-physical verdicts in downstream consumption — class-conflation pathology analogous to UV-regulator conflation."*

That is, the SCHEMATIC tag answers exactly one question: **"if a downstream gate imports this scalar `−3` and treats it as a FULL Pauli-Villars-at-Λ_UV number, is it being misled about the sourcing protocol?"** The honest answer is "the −3 came from the two-pin convergence-exponent protocol, not from a live full-physical Mellin-Barnes extraction at L≥13." The tag protects the **scalar pin's provenance in downstream import**.

### IV.2 What the SCHEMATIC tag does NOT pin

It does **not** make a claim about whether the exponent is structurally `−(d−1)`. Indeed it *cannot*, because the rule that defines it operates on the **methodology/sourcing layer** (`F: substrate → methodology` per `epistemic-discipline.md §"Layer-Decomposition"`), where the substrate-physics image of "exponent = −(d−1)" is the artifact "a scalar pin and its provenance string." Under the layer-functor Phi-correspondence, the SCHEMATIC tag is the F-image of a *sourcing* fact; the cohomology-class exponent is a *substrate-IS structural* fact. These are **orthogonal axes** in the four-axis orthogonality of `regulator-pin-discipline.md §"four-axis orthogonality (UV-regulator × Level × Binding × MACHINERY-SCOPE)"`, which states explicitly: *"The four axes are pairwise independent. ... A producing script may PASS one axis while FAILing another."* The Level axis (SCHEMATIC-vs-FULL) and the structural-exponent content are not the same axis.

The verdict-line says this in its own words, twice (companion lines 38/44, and WP §W2-3 line 185): *"the L^{−3} leading-term geometric envelope exponent −(d−1) at d=4 is the structural anchor."* The SCHEMATIC tag and the structural-exponent statement coexist in the SAME companion row **by design** — the row pins the *scalar provenance* as SCHEMATIC while naming the *exponent* as the structural anchor. There is no internal contradiction; there is a deliberate two-axis disclosure.

### IV.3 The crisp formal statement

```
Claim:  SCHEMATIC(scalar-pin provenance)  ⊥  STRUCTURAL(exponent = −(d−1))

Proof sketch (orthogonality):
  - SCHEMATIC lives on the Level-pin / sourcing axis (substrate-first-canonical-sourcing §(iv)).
  - −(d−1) lives on the cohomology-class axis (orientability+dimension+regularity axioms;
    registry-PROVEN regulator-invariant L-independent identity).
  - regulator-pin-discipline §"four-axis orthogonality": Level axis and the structural
    content are pairwise-independent axes; one may PASS while the other FAILs.
  ⇒ The truth-value of SCHEMATIC(provenance) does not constrain the truth-value of
    STRUCTURAL(exponent). In particular SCHEMATIC ≠ ¬FULL-RECOVERED at the exponent layer.
  ∎
```

Reading B needs `SCHEMATIC ⇒ ¬FULL-RECOVERED`. That implication only holds if the recovery claim is *about the scalar's full-physical sourcing*. But "FULL-RECOVERED" (housekeeping A9; the registry discharge annotation) is a claim **about the corridor** — "the asymptotic-α corridor is recovered" — and the corridor's content is the **exponent**, whose structural value is a standing theorem. So `SCHEMATIC(provenance) ∧ FULL-RECOVERED(corridor=exponent)` is consistent. To turn this into a contradiction you must redefine "FULL-RECOVERED" to mean "the scalar was extracted by a live full-physical pipeline" — which is a *different* claim that the registry never made and that "FULL-RECOVERED at the asymptotic-α axis" does not assert.

---

## V. The pre-asymptotic in-window values (−2.88 … −2.96) CONFIRM −3, they do not undercut it

Reading B will lean on `α_operational(L=35) = −2.876533` and `α(L=100) = −2.959997` being "not −3," and on the in-cache decay-magnitude sample `+2.6926` being "below 3." This is the **positive-finite-L-correction signature** of §VII.AU — and it is *predicted by the structure*, not a discrepancy.

### V.1 The local-exponent decomposition (the exact mechanism)

The signed local exponent of the FULL-physical residual is

```
α(L) = d ln R_b / d ln L = −(d−1) − (C₁/L)/(1 + C₁/L)
```

with `C₁ = −3.846` extracted from the REAL FULL-physical residual `R_b(L)` over L∈[12,22] (11 points, FULL CC-1995 §III.4 W7a-74 evaluator, R² = 0.99988, RMS = 7.75e-6; WP §W2-3 Step B). The leading term is `−(d−1) = −3` for ALL L; the second term is a `1/L` finite-L correction that vanishes as L→∞.

Sage evaluation (this turn, exact model arithmetic) of `α(L) = −3 − (C₁/L)/(1+C₁/L)` with C₁ = −3.846:

| L | α(L) | matches verdict line |
|:--|:-----|:---------------------|
| 12 | −2.528 | — (cache edge) |
| 15 | −2.655 | (sample window) |
| 22 | −2.788 | (sample window) |
| 35 | **−2.8765** | verdict α_operational = −2.876533 ✓ |
| 100 | **−2.9600** | verdict α_at_L100 = −2.959997 ✓ |
| 1000 | −2.9961 | → −3 |
| 100000 | −2.99996 | → −3 |
| ∞ | **−3.000000** | verdict α_asymptotic = −3 ✓ |

(The 4th-decimal agreement with the verdict-line values, off only by C₁ rounding, *reproduces the gate from the structural model* — confirming the in-window numbers ARE the finite-L shadow of the `−3` leading term, not an independent measurement that happens to sit near −3.)

### V.2 Why this strengthens (a)

The in-window values are NOT "candidate values for α that fall short of −3." They are the values of `α(L)` at finite L, and `α(L) → −3` **monotonically** with the `1/L` correction sign-fixed by the FULL-physical `C₁ < 0` (the positive-finite-L-correction: apparent decay magnitude < 3, rising to 3). The registry's own annotation (line 14906) pre-recorded this signature: *"finite-L above L^{−3} envelope, slower apparent decay."* So the data does exactly what a structurally-fixed `−3` exponent with a negative `1/L` correction MUST do. If the in-window values had *plateaued* away from −3, or trended the wrong way, that would threaten the structural claim. They do neither. The cross-check that the model reproduces the canonical pre-asymptotic sample `2.692624` to **rel_dev = 5.94e-15** (machine precision; WP §W2-3 Step B) is the load-bearing confirmation that the SAME observable is being read in two regimes — pre-asymptotic magnitude `+2.6926` and asymptotic signed `−3` are one object.

Crucially: **at C₁ = 0 the exponent is −3 at every L** (Sage: "C₁=0 pure L^−3 envelope alpha at any L = −3"). The C₁ term is a *sub-leading amplitude detail*; the *leading exponent* — the thing being recovered — is C₁-independent. Reading B's "the in-window α is not −3" conflates the finite-L local slope (which includes the `1/L` correction) with the leading exponent (which does not). The corridor was always about the leading exponent.

---

## VI. The never-diagonalized window does NOT undermine a structurally-fixed exponent — the Friedrich-Bär saturation argument

Reading B's last lever: "the L∈[35,100] window was never diagonalized; you fit a `1/L³` basis you assumed; this is not a FULL extraction." I take this head-on.

### VI.1 The exponent is read off the POLE, not off diagonalization

The exponent `−(d−1)` is determined by the dimension-spectrum pole structure (§II), which is fixed at the level of the spectral triple's *axioms* and *Peter-Weyl block decomposition* — it does NOT require diagonalizing any particular high-L block. Diagonalization at L≥13 is empirically infeasible (recursive Casimir irrep construction super-polynomial at p+q≥13, `math-scripts.md §"D_K Block-Diagonality Pre-Check"`), but that infeasibility is about **constructing eigenvalues**, not about **knowing the cone exponent**. The cone exponent is upstream of the eigenvalues. So "never diagonalized beyond L=12" is irrelevant to the exponent — it would only matter if the exponent had to be *measured* from high-L eigenvalues, which it does not.

### VI.2 Friedrich-Bär saturation: the window contributes NOTHING new to the bottom-K

Even granting that one wants the residual `R_b(L)` to be the FULL-physical object across the window, the Friedrich-Bär saturation theorem guarantees the bottom-K is **structurally frozen above L=12** — so the FULL-physical residual in the window is *determined* by the L≤12 cache, and the `L^{−3}` tail is the EXACT asymptotic tail, not an assumed basis. The substitution chain (WP §W2-3 Step A; Sage-verified):

```
Step 1:  Worst-case (smallest-C₂) NEW sector entering at level L is (L,0).
Step 2:  Its eigenvalue floor is  η_FB · √(C₂(L,0)+1)  with η_FB ≥ 0.40 (cache: η_FB_observed = 0.5472).
Step 3:  At L=35:  floor = 0.40·√(C₂(35,0)+1) = 8.4317.
         At L=100: floor = 23.4413.
Step 4:  bottom-K ceiling = botK_ceiling = 0.8452  (S92 W9-3).
Step 5:  8.4317  ≫  0.8452   (and 23.44 ≫ 0.845)   ⇒  NO new sector can enter the
         bottom-K window for ANY L ∈ [35,100]  (100% of NEW sectors excluded).
   ⇒ The bottom-K is frozen at its L=12-cache value across the entire window.
   ⇒ R_b(L) in the window is the FULL-physical residual continued from the frozen cache,
     and its decay is the EXACT analytic L^{−3} tail — NOT an imposed fit basis.
```

The NEW-sector floor `8.43` exceeds the bottom-K ceiling `0.845` by **~10×**. This is an enormous margin — there is no ambiguity about whether a new sector might "sneak in" and perturb the tail. The `1/L³` is therefore not an *assumed* basis: it is the *derived* asymptotic form of a residual whose generating spectrum is frozen, evaluated against a pole of fixed order. The `fit_basis: 1/L³` in the plan is the **structurally-correct** basis (it IS the cone exponent), and fitting `R_b(L) = c·L^{−3}(1+C₁/L)` to the REAL frozen-cache residual recovers `c, C₁` — *amplitude* parameters — while the *exponent* `−3` is input from the pole, confirmed by R² = 0.99988.

### VI.3 "Assumed the basis" reframed honestly

Yes, the fit assumed `L^{−3}`. But that is not circular, because **`L^{−3}` is not a free hypothesis being tested by the fit — it is the cohomology-class theorem `−(d−1) = −3` being USED as input**, and the fit's job is to (i) recover the amplitude and `1/L` correction, and (ii) *verify consistency* via R² and the machine-precision reproduction of the independent canonical sample `2.6926`. A fit that assumes a structurally-derived exponent and then confirms 99.988% variance-explained + machine-precision agreement with an independently-pinned sample is a **consistency certification of a theorem**, not a fitted discovery. The honest reading is: the exponent is known (theorem); the fit checks that the FULL-physical residual is consistent with it (it is, overwhelmingly). That is precisely what "FULL-RECOVERED at the leading-term geometric exponent layer" claims — no more, no less.

---

## VII. Anticipating Reading B's three best shots (and why none reaches (b))

I pre-empt, without conceding, to set up T3:

**B-shot 1 — "SCHEMATIC tag caps the recovery."** Rebutted in §IV: orthogonal axes (`regulator-pin-discipline.md §"four-axis orthogonality"`); the tag pins scalar-sourcing provenance for downstream import, not the exponent's structural status; `SCHEMATIC ⇏ ¬FULL-RECOVERED(corridor)`. The verdict-line itself names the exponent as "the structural anchor" in the SAME row that carries SCHEMATIC — by design.

**B-shot 2 — "in-window α is −2.88…−2.96, not −3."** Rebutted in §V: those ARE `α(L)` at finite L; leading term is −3 at all L; the `1/L` correction is sub-leading amplitude detail; monotone → −3; the model reproduces the verdict values and the canonical sample to machine precision. The corridor is about the leading exponent, which is C₁-independent.

**B-shot 3 — "window never diagonalized; fit basis assumed."** Rebutted in §VI: the exponent is read off the pole, upstream of eigenvalues; Friedrich-Bär freezes the bottom-K above L=12 with a ~10× margin, so the `L^{−3}` tail is the EXACT asymptotic form of a frozen-spectrum residual, not an imposed basis; the fit certifies consistency (R²=0.99988, sample rel_dev 5.94e-15), it does not discover the exponent.

If Reading B concedes the exponent's structural fixity (which the registry's own PROVEN theorem forces) but still wants the SCHEMATIC tag to mean *something*, the ONLY coherent residue is: **the FULL-physical numerical SCALAR extraction (a live Mellin-Barnes evaluation at high L) was not performed**. That is true — but it is a statement about the *scalar pin's sourcing*, which (a) already concedes via the SCHEMATIC tag's retention. It is NOT a statement that the exponent is unrecovered. This is why, if a containment is needed, the correct move is **(c) the two-layer split** — FULL-RECOVERED at the geometric-exponent/cohomology-class layer AND SCHEMATIC-pending at the numerical-scalar-FULL-extraction layer — which PRESERVES Reading A's core claim (the exponent is recovered) while honestly housing the residual sourcing caveat. Option (b) is wrong because it lets a sourcing-axis tag *cap* a cohomology-class-axis recovery, inverting the substrate-first direction and collapsing the orthogonal axes the framework's own four-axis discipline keeps separate.

---

## VIII. Summary of the steelman (Reading A)

1. **The exponent `−3` is `−(d−1)` at `d=4`, structurally fixed by the Mellin-cone pole `s=3`** (orientability + dimension + regularity axioms). Sage: `−(d−1) = −3` exact. It is a **registry-PROVEN regulator-invariant, L-independent cohomology-class identity** — a theorem that pre-dates and is independent of the W2-3 gate.

2. **Regulator-invariance at the exponent layer is a theorem** (F₂ FI class; Cauchy's theorem, `sub_term_R(Mellin)=sub_term_R(zeta)=0` at d=4 s=3; α_Mellin = α_zeta EXACT). The `a_4^{Mellin}` pin is the evaluation route, not a dependence of the exponent on the regulator.

3. **The SCHEMATIC tier_pin is a sourcing-axis artifact, orthogonal to the cohomology-class axis** (`regulator-pin-discipline.md §"four-axis orthogonality"`; `epistemic-discipline.md §"Layer-Decomposition"`). It pins the scalar's downstream-import provenance, not the exponent's structural status. `SCHEMATIC ⇏ ¬FULL-RECOVERED(corridor=exponent)`. The verdict-line names the exponent as "the structural anchor" in the same row that carries SCHEMATIC, by design.

4. **The pre-asymptotic in-window values confirm −3**: they are `α(L)` at finite L, leading term −3 for all L, monotone → −3, model reproduces verdict values + canonical sample to machine precision. The corridor concerns the leading exponent, which is C₁-independent (at C₁=0, α=−3 at every L).

5. **The never-diagonalized window does not undermine the exponent**: the exponent is read off the pole (upstream of eigenvalues); Friedrich-Bär freezes the bottom-K above L=12 with a ~10× margin (NEW-sector floor 8.43 ≫ bottom-K ceiling 0.845), so the `L^{−3}` tail is the EXACT asymptotic form of a frozen-spectrum residual, not an imposed basis; the fit certifies consistency (R²=0.99988), it does not discover the exponent.

**Verdict argued this turn**: **(a) FULL-RECOVERED is honest.** The discharge `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → FULL-RECOVERED` recovers the corridor's content (the asymptotic leading exponent) as a structural fact. If — and only if — a containment is demanded for the residual scalar-sourcing caveat, the correct containment is **(c) the two-layer split** (FULL-RECOVERED at the cohomology-class/exponent layer; SCHEMATIC-pending at the numerical-scalar-FULL-extraction layer), which preserves Reading A's core claim. **Option (b) is rejected**: it inverts the substrate-first direction and lets a sourcing-axis tag cap a cohomology-class-axis recovery, collapsing axes the framework's four-axis discipline holds orthogonal.

*(Steelman only — no convergence in this turn, per the workshop turn plan. lizzi answers in T2.)*
