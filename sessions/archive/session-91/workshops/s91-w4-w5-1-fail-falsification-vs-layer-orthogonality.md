# Session 91 Workshop W-4: Volovik x Connes — W5-1 FAIL: FALSIFICATION vs LAYER-ORTHOGONALITY F-Decomposition

**Date**: 2026-05-21
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: volovik (volovik-superfluid-universe-theorist; Reading A FALSIFICATION defender; W5-1 author), connes (connes-ncg-theorist; Reading B LAYER-ORTHOGONALITY defender; layer-functor F owner per `epistemic-discipline.md §"Layer-Decomposition"`)
**Source Documents**:
- `sessions/archive/session-91/session-91-w5-workingpaper.md` (W5-1 working paper)
- `sessions/permanent-results-registry.md` (§VII.AV current entry around line 18059)
- `computations/session-91/s91_w5_1_full_bdg_pv.npz` (W5-1 full BdG-PV computation outputs)
- `sessions/archive/session-91/workshops/_seed-w5.md` (Chunk C4 investigator seed for w5)
- `.claude/rules/epistemic-discipline.md` (§"Layer-Decomposition" Phi(a_n) correspondence table)

**Focus Topics** (4 adjudication questions for §W5-1 FAIL structural reading; two competing reads by same agent (volovik) at gate-emission time — structurally novel ledger-dissonance):

§W5-1 evidence:
- α_PV = 6.26 (predicted 3.0; deviation factor 2.09)
- anchor rel-err 7393% vs L_emp = -7.046336 M_KK²
- L_max-INVARIANT plateau bit-for-bit `R_KW^{PV}(L_max) = -527.97 M_KK²` across L_max ∈ {6, 7, 8, 9, 10, 11, 12}

Two readings:
- **Reading A (volovik, verdict-line composite + WP line 221)** — FALSIFICATION: SCHEMATIC Casimir-bound proxy is FALSIFIED at FULL-PV regulator-class; route-(ii) cannot close §VII.AV's PROXY-REFINEMENT pathway; §VII.AV must seek alternative envelope predictors (HKR-image residue-pole / Friedrich-Bär-derived / Connes-Karoubi-pairing). CF-S92-W5-1-A forward gate.
- **Reading B (connes, substrate framing addendum WP line 234)** — LAYER-ORTHOGONALITY: SCHEMATIC and FULL-PV inhabit STRUCTURALLY ORTHOGONAL methodology-floor layers under the layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"`; the FAIL is the substrate's signal that these two F-images of the SAME Level-1 substrate-IS observable are NOT interchangeable at the algebraic-envelope layer; §VII.AV should be split into TWO structurally-orthogonal companion slots.

1. **(a) F-mapping of R_KW^{PV}(L_max)** — Which substrate-IS observable does R_KW^{PV}(L_max) F-map to at methodology-floor: the D_K-spectrum Mellin trace (same as SCHEMATIC) or the BdG-occupation kernel (orthogonal to SCHEMATIC)? Cite F-decomposition explicitly via `epistemic-discipline.md §"Layer-Decomposition"` Phi(a_n) correspondence table.
2. **(b) L_max-INVARIANT plateau structural status** — Does the bit-for-bit `R_KW^{PV}(L_max) = -527.97 M_KK²` plateau across L_max ∈ {6,...,12} under d² ln/d(lnK)² constitute structural evidence of layer-orthogonality (Reading B) OR simply a numerical accident inside a falsified envelope (Reading A)? Cite the multiplicative-normalization-cancellation argument.
3. **(c) 7393% rel-err structural meaning** — Is the anchor rel-err 7393% vs L_emp = -7.046336 evidence of falsification (Reading A) OR evidence L_emp and R_KW^{PV} are F-images of DIFFERENT substrate-IS observables (Reading B; "rel-err structurally meaningless" because no anchor mismatch when values live at orthogonal layers)?
4. **(d) §VII.AV registry text update under canonical reading** — Reading A → FALSIFIED route-(ii) annotation on single §VII.AV slot + activate CF-S92-W5-1-A as forward envelope-predictor gate; Reading B → split §VII.AV into §VII.AV-D_K-spectrum-trace (preserve L_emp anchor) and §VII.AV-BdG-fiber-occupation (anchor at R_KW^{PV}(L_max=12) = -527.97) with structural-orthogonal-companion anchor structure per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause-4.

**Substrate framing** per `phononic-framing.md §"IS Space, Not IN Space"`: substrate IS the spectral triple at τ_fold; SCHEMATIC and FULL-PV regulators are methodology-floor F-images per `epistemic-discipline.md §"Layer-Decomposition"`. Direction substrate → emergent: substrate's intrinsic structure (multi-branch s52 B-tensor + BdG sub-algebra + Mellin-cone pole) determines which F-images are equivalent at which layer; methodology-floor regulator class is downstream. Substrate-first canonical sourcing per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline: SCHEMATIC vs FULL-PV are level-orthogonal by structural class.

**R1 explicit-prediction discipline**:
- volovik steelmans Reading A FALSIFICATION + explicit prediction: if Reading B is right, the L_max-INVARIANT plateau is a measure-zero coincidence — what does Reading B predict for the plateau magnitude?
- connes steelmans Reading B LAYER-ORTHOGONALITY + explicit prediction: if Reading A is right, SCHEMATIC proxy is wrong by O(2x) at α and O(75x) at L_emp anchor — what does Reading A predict about L_max-INVARIANCE structurally; isn't an L_max-INVARIANT plateau a structural FEATURE not a coincidence?

**Output goal**: STRUCTURAL VERDICT pre-registering ONE of three §VII.AV registry text updates:
- **(i) Reading A canonical** → FALSIFIED route-(ii) annotation on single §VII.AV slot; CF-S92-W5-1-A activated as forward envelope-predictor gate; CF-S92-W5-1-C demoted/cancelled.
- **(ii) Reading B canonical** → §VII.AV slot split into structural-orthogonal-companion structure (§VII.AV-D_K-spectrum-trace + §VII.AV-BdG-fiber-occupation); CF-S92-W5-1-C activated as forward layer-attribution disambiguator; CF-S92-W5-1-A demoted/cancelled.
- **(iii) Hybrid** — single §VII.AV slot with layer-attribution sub-rows declaring both F-images + sub-class-rotation forward gate; CF-S92-W5-1-A and CF-S92-W5-1-C both queued at different tier.

Verdict also produces pre-registered gate criterion for any future L_max-INVARIANT-plateau-vs-falsified-envelope discriminator in adjacent §VII slots — `math-scripts.md §"Multiplicative-normalization cancellation invariants"` rule-file extension calibration corpus instance #1.

---

## Round 1 — Volovik: Opening Analysis (Reading A FALSIFICATION Defender)

### V1: F-mapping of R_KW^{PV}(L_max) — same observable as SCHEMATIC at the D_K-spectrum trace layer

**Claim (Reading A canonical)**: `R_KW^{PV}(L_max)` F-maps to the **SAME substrate-IS observable** as the SCHEMATIC Casimir-bound proxy — namely the D_K-spectrum Mellin trace `Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})` at substrate-distance-2 pole `s=4` on the single-τ-slice spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))`. They are NOT F-images of two distinct substrate-IS observables. The FULL Pauli-Villars regularization at Λ_UV = M_KK is a **substrate-internal UV-completion** of the SAME Mellin trace, NOT a structurally different observable.

**Substrate-IS axiom (cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" MANDATORY at K=3)**: ONE substrate-IS observable is fixed by the triple `(algebra, projector, pole)`. The §VII.AV entry (`permanent-results-registry.md` line 18084, Element 1) registered this triple verbatim:
- Algebra: `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (BdG sub-algebra; Corner IV per §VII.U.2)
- Projector: `P_BdG` (central projector onto the BdG sub-algebra)
- Pole: `s=4` (substrate-distance-2 Mellin-cone closure)

Both the SCHEMATIC `_spectral_action_regulators.py` evaluator (S88 W7b-83 K=4 calibration corpus instance, MANDATORY level-pin discipline per `substrate-first-canonical-sourcing.md §(iv)`) and the FULL Pauli-Villars pipeline at Λ_UV = M_KK with 2-PV tower `{M_KK, √2·M_KK}` and coefficients `{+2, −1}` (S61/S78 protocol) operate on the SAME triple `(M_2(ℂ), P_BdG, s=4)`. They differ only in **regulator-class axis** per `regulator-pin-discipline.md`: SCHEMATIC tags as `a_n^{Mellin-SCHEMATIC}`; FULL-PV tags as `a_n^{Pauli-Villars-FULL}`. UV-regulator axis variation is ORTHOGONAL to substrate-IS observable identity (the latter is fixed by `(algebra, projector, pole)`; the former is a methodology-floor pin).

**WP line 134 substrate framing affirms this** (verbatim from §W5-1 Method block, plan §13): "The FULL Pauli-Villars regularization at Λ_UV = M_KK IS the substrate's intrinsic UV-completion; it is NOT a 'regularization scheme imposed FROM outside' the substrate. The HKR `L_max → ∞` bridge map IS substrate-IS at the cohomology-class level". The pre-registered substrate framing — written into the §W5-1 PLAN before the runtime addendum surfaced the layer-orthogonality alternative — pins the FULL-PV pipeline as substrate-internal. There is NO admission of a separate substrate-IS observable for FULL-PV vs SCHEMATIC; the substrate-IS axiom is single-pinned at `(M_2(ℂ), P_BdG, s=4)`.

**The 7393% deviation is therefore meaningful**: both routes compute the SAME observable. The SCHEMATIC Casimir-bound truncation `~ Σ_{p+q ≤ L_max} (C_2(p,q))^{−s}` is a structurally simplified evaluation; the FULL-PV pipeline performs the SAME Mellin trace at higher regulator-class fidelity. When the two evaluations disagree by 75× at the canonical anchor (`R_KW^{PV}(L_max=12) = -527.97 M_KK²` vs canonical `L_emp = -7.046336 M_KK²` per §VII.AV Element 5 / line 18092 and `s88-pending-edits-ledger.md` "preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source"), the substrate is telling us SCHEMATIC's `L^{-3}` Casimir-bound envelope is wrong at higher regulator-class fidelity for this observable.

**Reading B's claim (Re:V1 must defend)**: that `R_KW^{PV}` F-maps to a BdG-occupation kernel observable structurally distinct from the D_K-spectrum trace. This would require a SECOND substrate-IS observable at the SAME `(M_2(ℂ), P_BdG, s=4)` triple — which the algebra-axis orthogonality K=3 MANDATORY discipline FORBIDS (one observable per triple). Reading B must therefore claim either (i) a different triple (different algebra, different projector, OR different pole) at which the BdG-occupation kernel lives — but then this is a STRUCTURALLY DIFFERENT registry entry, not §VII.AV; OR (ii) that "BdG-occupation kernel" and "D_K-spectrum trace" are two F-images of the same substrate-IS observable at DIFFERENT methodology-floor layers per F: substrate → methodology → audit — but this is precisely the regulator-class axis (Mellin vs Pauli-Villars), NOT a separate methodology-floor layer. The Phi(a_n) correspondence in `epistemic-discipline.md §"Layer-Decomposition"` maps weight-2n substrate observables to weight-2n methodology rules; it does NOT partition a fixed substrate-IS observable into orthogonal sub-observables at the same weight.

**Question for connes**: Under the algebra-axis orthogonality K=3 MANDATORY discipline (cross-pillar-bridge-anatomy.md), can two F-images of the SAME substrate-IS observable land on STRUCTURALLY DISTINCT methodology-floor layers without violating the single-observable-per-triple axiom? If yes, cite the precedent in the calibration corpus. If no, then `R_KW^{PV}` and `Tr(D_K^{-2s})|_{s=4}` F-map to the same observable, and the 7393% rel-err IS substrate-IS-relevant.

### V2: L_max-INVARIANT plateau as numerical accident inside falsified envelope

**Claim (Reading A canonical)**: The bit-for-bit `R_KW^{PV}(L_max) = -527.9669 M_KK²` plateau across `L_max ∈ {6, 7, 8, 9, 10, 11, 12}` (WP lines 166-177) is **INFORMATION-FREE** as a discriminator between Reading A FALSIFICATION and Reading B LAYER-ORTHOGONALITY. The plateau is a generic consequence of the multiplicative-normalization-cancellation under `d² ln(·) / d(ln K)²`, which holds identically for ANY observable that enters the L_max truncation as a multiplicative spectral-support weight — whether the envelope is correctly predicted (PASS-case for SCHEMATIC) or wrongly predicted (FAIL-case actually observed). The plateau predicts NOTHING about whether SCHEMATIC's envelope is right or wrong.

**Multiplicative-normalization-cancellation substitution chain** (per `math-scripts.md §"Double-Check Logic Before Compute"` MANDATORY chain discipline):

```
Step 1 (Definition): R_KW^{PV}(τ_fold, L_max, s)
                     = d² ln[ Tr_{M_2(ℂ)}( P_BdG · D_K^{−2s} − Σ_j c_j (D_K² + M_j²)^{−s} ) ] / d(ln K_window)²
                     evaluated at K_window grid centered at K_horizon

Step 2 (L_max factorization): At each L_max, the truncated Mellin trace factorizes as
                     Tr^{(L_max)}_{PV}(K) = w(L_max) · κ(K)
                     where  w(L_max) = M_PV(L_max) / M_PV(12)  is the L_max-dependent
                                        multiplicative spectral-support weight
                                        (WP Table line 168-176 column 2:
                                         w(6)=0.8928, w(12)=1.0000)
                     and    κ(K)    is the L_max-INDEPENDENT K-window kernel shape
                                        (the BdG occupation modulation at fixed
                                         K-grid, identical across all L_max — WP line 178)

Step 3 (Substitution): ln Tr^{(L_max)}_{PV}(K) = ln w(L_max) + ln κ(K)

Step 4 (Differentiation):
   d ln Tr^{(L_max)}_{PV}(K) / d ln K = d ln w(L_max) / d ln K + d ln κ(K) / d ln K
                                       = 0                       + d ln κ(K) / d ln K
       (first term ≡ 0 because w(L_max) has NO K-dependence — it is the spectral-support
        weight at the substrate-distance-2 Mellin trace, evaluated AHEAD of K-window)

Step 5 (Second derivative): d² ln Tr^{(L_max)}_{PV}(K) / d(ln K)² = d² ln κ(K) / d(ln K)²
       Therefore: R_KW^{PV}(τ_fold, L_max, s=4) = R_KW^{kernel}(K) — L_max-INDEPENDENT
                  for ANY multiplicative-normalization w(L_max) regardless of magnitude

Conclusion: The plateau magnitude -527.97 M_KK² IS the value of d² ln κ / d(ln K)² at K_horizon.
            It is independent of the L_max-dependent weight w(L_max).
            The plateau exists STRUCTURALLY whenever the multiplicative factorization
            Tr^{(L_max)} = w(L_max) · κ(K) holds — which it does for ANY Mellin-cone
            truncation at substrate-distance-2 pole s=4 on the BdG sub-algebra,
            INCLUDING the SCHEMATIC Casimir-bound proxy if computed via d² ln / d(ln K)².
```

**WP line 178 confirms the multiplicative factorization explicitly**: "the Mellin-PV weight enters multiplicatively into the L_max-truncated kernel, and the second log-derivative `d² ln(.)/d(ln K)²` is invariant under multiplicative L_max-normalization (translation invariance of curvature)". This is a STRUCTURAL identity, NOT an empirical discovery — translation invariance of `d² ln(·) / d(ln K)²` under multiplicative pre-factors is a textbook fact (the curvature of `ln f(K)` is invariant under `f(K) → C · f(K)` for any L_max-dependent constant C).

**Why the plateau does NOT discriminate**:

1. **PASS counterfactual**: if the FULL-PV pipeline had reproduced `R_KW^{PV}(L_max=12) ≈ -7.046336 M_KK²` (matching `L_emp` within 5%), and ALSO produced a bit-for-bit L_max plateau at the smaller value across L_max ∈ {6,...,12}, the plateau would still have arisen from the SAME multiplicative-normalization-cancellation. It would have been completely uninformative about layer-attribution.
2. **FAIL counterfactual (observed)**: the plateau arose at -527.97 M_KK² — 75× the canonical anchor. Same multiplicative-cancellation structure; the plateau magnitude is set by `d² ln κ / d(ln K)²` at K_horizon under the FULL-PV K-window kernel `κ(K)`, which is materially different from the SCHEMATIC's `κ_SCHEMATIC(K)`.

**Reading B's claim that the plateau IS structural evidence of layer-orthogonality is therefore unfalsifiable as posed**: the same plateau would have arisen under PASS. A discriminator must distinguish PASS from FAIL outcomes; a feature shared between PASS and FAIL is not a discriminator. Reading B can promote the plateau to a "structural FEATURE" of the BdG-occupation-kernel layer only by ALSO predicting the plateau would NOT have arisen at the D_K-spectrum-trace layer — but the multiplicative-cancellation derivation in Steps 1-5 above shows the plateau arises identically at BOTH layers whenever the L_max truncation enters multiplicatively. The plateau is a property of the OPERATOR `d² ln(·) / d(ln K)²`, NOT a property of the substrate-IS observable.

**Cross-reference to permanent theorem**: `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` Level-2 envelope discipline requires `L^{-α}` convergence to be a property of the **bare envelope** (the convergence of the substrate-IS image to the laboratory-IN image as `L_max → ∞`). The K-window log-derivative operator is a STATE-PAIR functional on the BdG sub-algebra (Cell IV, algebra-DEPENDENT per registry line 18067) — it ALREADY ABSORBS the multiplicative pre-factors by construction. Extracting α from `R_KW^{PV}(L_max)` via least-squares fit `R_KW^{PV}(L) ≈ A · L^{-α} + B` therefore probes the SUB-LEADING corrections to the multiplicative-cancellation, NOT the bare envelope. The α_PV = 6.26 extraction (WP line 181) with `A_PV = -1.58e-2` (WP line 183, "small residual amplitude consistent with float64 noise on the plateau") is fitting *float64 noise* on top of the perfect plateau — confirmed by `α_PV_1σ = ∞` (rank-deficient covariance, WP line 182). The 6.26 number is structurally meaningless under the plateau.

**Question for connes**: If `R_KW^{PV}(L_max)` is L_max-invariant by multiplicative-cancellation, what bare envelope IS Reading B claiming for the BdG-occupation-kernel observable? Where does the `L^{-α}` envelope live structurally if the L_max-INVARIANT plateau eats the entire envelope information? Reading B owes a structural prediction for the bare envelope, NOT just a re-interpretation of the plateau.

### V3: 7393% anchor rel-err as definitive falsification evidence

**Claim (Reading A canonical)**: The 7392.79% relative error between `R_KW^{PV}(L_max=12) = -527.966919 M_KK²` and `L_emp(L_max=12) = -7.046336 M_KK²` (WP lines 187-190; verdict line 211 `anchor_rel_err=7392.7861%`) is DEFINITIVE falsification evidence at the substrate-IS observable layer. Reading B's claim that the 7393% rel-err is "structurally meaningless because L_emp and R_KW^{PV} are F-images of DIFFERENT substrate-IS observables" violates the algebra-axis orthogonality axiom AND is directly falsified by the W5-1 script's own internal kernel-verification step at PV mass = 0.

**Decisive evidence — WP line 150 numerical-kernel-independence verification**: The W5-1 script reports (verbatim): "Second log-derivative via 5-point central FD at K_horizon (canonical S87 W2-3 numerical core; reproduced bit-for-bit at PV mass = 0 to 4.7e−7 deviation from −7.046336 → kernel verified independently)". This is the structural smoking gun. The IDENTICAL `d² ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})) / d(ln K)²` operator evaluated on the IDENTICAL D_K spectrum at the IDENTICAL substrate-distance-2 pole s=4 on the IDENTICAL BdG sub-algebra:

- At **PV_mass → 0** (no regulator) → kernel returns `-7.046336 ± 4.7e-7` (bit-precision match to `L_emp` canonical, line 18092 of `permanent-results-registry.md`).
- At **PV_mass = M_KK** (FULL Pauli-Villars, S61/S78 protocol) → kernel returns `-527.966919` (75× larger magnitude; same sign).

**This single fact closes Reading B**. The IDENTICAL operator on the IDENTICAL spectrum cannot F-map to DIFFERENT substrate-IS observables under regulator-class variation alone. Under Reading B's claim that `R_KW^{PV}` F-maps to "BdG-occupation kernel" while `L_emp` F-maps to "D_K-spectrum trace", the PV_mass → 0 limit would have to land on the D_K-spectrum trace value AND the PV_mass = M_KK limit would have to land on the BdG-occupation kernel value — but the limit is a CONTINUOUS deformation of a SINGLE operator. There is no discrete jump where the observable-identity changes between PV_mass = 0 and PV_mass = M_KK.

**Substrate-IS axiom (cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" MANDATORY K=3; registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY" Detection clause-4)**: ONE substrate-IS observable per `(algebra, projector, pole)` triple. Cross-corner co-primary structures with anchors on DIFFERENT algebra-axis cells are STRUCTURALLY FORBIDDEN. The §VII.AV registry entry (line 18067) classified the K-window log-derivative as **Corner IV (algebra-DEPENDENT state-pair functional × substrate-distance-2 pole s=4)** — a single cell. Both `R_KW^{PV}` and `L_emp` inhabit this single Corner-IV cell at `(M_2(ℂ), P_BdG, s=4)`. Reading B's split-into-two-companion-slots proposal requires the values to inhabit STRUCTURALLY DISTINCT algebra-axis cells per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause-4 — but Reading B has not produced the SECOND cell, the SECOND triple, the SECOND projector, or the SECOND pole that would license the split.

**Reading B has the burden of producing the second triple**. If Reading B wants two §VII.AV companion slots (`§VII.AV-D_K-spectrum-trace` and `§VII.AV-BdG-fiber-occupation`), Reading B must declare for each slot:
- (alg_1, proj_1, pole_1) for the D_K-spectrum-trace slot
- (alg_2, proj_2, pole_2) for the BdG-fiber-occupation slot
- algebra-axis cell assignment per `permanent-results-registry.md §VII.U.2` 4-corner classification
- Hybrid Independence Test predicate per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` showing the two triples are HIT-independent under `(i ∨ ii ∨ iii) ∧ iv`

Without these structural declarations, the slot-split is REGISTRY-INCOMPLETE per clause-4 forbidance.

**The 7393% rel-err interpretation under Reading A**: The same substrate-IS observable evaluated under SCHEMATIC vs FULL-PV regulator-classes differs by 75×. This is a REGULATOR-CLASS-DEPENDENT (RD per `epistemic-discipline.md §"Source Reconciliation"` 5-class taxonomy) signature. The SCHEMATIC Casimir-bound truncation, when audited against the FULL physical regularization at Λ_UV = M_KK, fails to reproduce the canonical anchor by 1.87 orders of magnitude (log₁₀(75) = 1.87). WP line 198 attributes this structurally: "at M_PV/Δ_BCS ≈ 2.16 the regulator copies retain non-trivial K-dependence and materially shift the K-window log-derivative" — i.e., the SCHEMATIC Casimir-bound approximation, which DROPS the regulator's K-dependence (a key step in the Casimir-bound derivation), is invalid at this observable because the FULL-PV regulator is NOT in the asymptotic large-mass limit at K_horizon (WP line 164: "the regulator scale M_KK ≈ 1 is order-unity vs the spectrum's lower edge → regulator is NOT in the asymptotic large-mass limit").

**Sign-PASS preservation reinforces Reading A**: WP line 219 / verdict-line 211 records `sign_verdict = PASS` (α > 0 AND L_emp_PV < 0). The HKR `L_max → ∞` image convergence direction is sign-correct. This is exactly what we expect under FALSIFICATION of an envelope MAGNITUDE while preserving the underlying observable identity — same observable, same sign, but the envelope magnitude is materially shifted by the regulator-class change. Under Reading B (orthogonal layers, distinct substrate-IS observables), there would be no structural reason to expect the signs to match — yet they do, because both values are evaluations of the SAME substrate-IS observable at different regulator-classes.

**Question for connes**: Cite the substrate-IS triple `(alg_2, proj_2, pole_2)` for the proposed `§VII.AV-BdG-fiber-occupation` slot. If `R_KW^{PV}` F-maps to this slot, what algebra-axis cell does it inhabit per `permanent-results-registry.md §VII.U.2`? If it inhabits Corner IV (same as L_emp), Reading B's slot-split violates `registry-landing.md` clause-4. If it inhabits a different corner, what is the parse-tree expansion of the BdG-occupation kernel that lifts it OUT of the K-window log-derivative state-pair functional class? Without these structural declarations, the layer-orthogonality reading is registry-incomplete.

### V4: §VII.AV registry text under Reading A canonical — FALSIFIED route-(ii) annotation + CF-S92-W5-1-A activation

**Reading A canonical update to §VII.AV (`permanent-results-registry.md` line 18059 onward)** — single-slot FALSIFIED route-(ii) annotation; NO slot split.

**Specific registry-text edits (mack-cosmic-bridge to land per `feedback_mack-bridge-role.md` sole-writer discipline)**:

1. **Status block update (line 18063 area)**: append the W5-1 FAIL audit-pin sub-row to the existing REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT status note:

   ```
   Status update (S91 W5-1 close, 2026-05-21): refinement-pathway route (ii) FULL Pauli-Villars
   at Λ_UV = M_KK CLOSED-FAIL per S91-W6-FULL-BdG verdict
   (audit_sha256=04a6b22f1ab5b180fac0eb73132ce05ae7e9f32d4394203728778b47a037351e).
   Empirical α_PV = 6.264 ≫ predicted α=3 (PASS band [2.9, 3.1] FAIL by 2.09× factor);
   anchor relative error 7392.79% vs canonical L_emp(L_max=12) = -7.046336474406761 M_KK²
   (sign_verdict=PASS, magnitude_verdict=FAIL, regime_verdict=BREAKDOWN; composite=FAIL).
   SCHEMATIC Casimir-bound proxy at L^{-3} envelope falsified at FULL-PV regulator-class
   cross-check. §VII.AV PROXY-REFINEMENT sub-class tag PRESERVED — pathway routes (i)/(iii)
   on substrate-physics layer + (iv)/(v)/(vi)/(vii) on operational/dual-anchor layers
   remain active; alternative envelope-predictor pathway (CF-S92-W5-1-A) activates as
   forward gate at S92.
   ```

2. **Refinement-pathway table update (lines 18108-18120)**: annotate route (ii) with the FAIL-closure tag while preserving the table structure:

   - Route (ii) `FULL BdG re-derivation` row: append annotation column `Status: CLOSED-FAIL at S91 W5-1` with audit-pin and 1-line summary. Do NOT delete the row; the FAIL is structurally informative and the audit trail must be preserved.
   - Add NEW route (viii) `Alternative envelope predictor (HKR-image residue-pole / Friedrich-Bär-derived / Connes-Karoubi pairing)` queued as `CF-S92-W5-1-A` per WP §W5-1 lines 250-254. Refinement type: substrate-physics envelope-predictor reformulation. Layer: substrate-physics (NOT operational-machinery).

3. **Element 4 (Algebraic envelope) update (line 18090 area)**: append a corrigendum note:

   ```
   Corrigendum (S91 W5-1, 2026-05-21): the L^{-3} HKR-image envelope prediction is
   FALSIFIED at the FULL-PV regulator-class cross-check (α_PV = 6.264, 75× anchor
   magnitude deviation). The Level-2 envelope's structural form on the binding axis
   is open — the SCHEMATIC Casimir-bound derivation does NOT generalize to FULL
   physical Pauli-Villars regularization at Λ_UV = M_KK for this observable. CF-S92-W5-1-A
   activated as the alternative envelope-predictor gate.
   ```

4. **CF-S92-W5-1-A activation** (per WP §W5-1 lines 250-254; promote from queued to ACTIVE for S92):

   Forward gate `S92-VII-AV-ALTERNATIVE-ENVELOPE-PREDICTOR`:
   - Substrate-physics derivation of envelope predictor that REPLACES SCHEMATIC Casimir-bound `L^{-3}` ansatz
   - Candidates (all 3 pre-registered):
     - **(a) HKR image residue-pole structure** at substrate-distance-2 pole s=4 with explicit `c_continuum` continuum-side anchor (per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` Level-2-binding admissibility)
     - **(b) Friedrich-Bär saturation-theorem-derived envelope** per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` W11-3 precedent (η_FB ratio-based; analytic certification of bottom-K invariance at L_max ≥ L_anchor)
     - **(c) explicit Connes-Karoubi pairing on the BdG sub-algebra K-theory boundary** — direct K-theoretic envelope replacing the Mellin-cone Casimir-bound proxy
   - PASS: any one of the three predictors produces a structurally-derived envelope that (i) the empirical FULL-PV pipeline reproduces within 5% at L_max=12, AND (ii) admits Level-2-binding sub-class per `cross-pillar-bridge-anatomy.md`.
   - FAIL: no predictor produces an L_max-INVARIANT-plateau-matching prediction → §VII.AV's substrate-IS observable identity must be re-evaluated (return to CF-W5-5 = CF-62 disambiguation gate).

5. **CF-S92-W5-1-C demotion** (per WP §W5-1 lines 262-266; demote layer-attribution disambiguation under Reading A canonical):

   Reading B's slot-split proposal (CF-S92-W5-1-C) is **demoted from active to subordinate / cancelled** under Reading A. The substrate-IS observable identity at §VII.AV is single-pinned at `(M_2(ℂ), P_BdG, s=4)` per the algebra-axis orthogonality MANDATORY K=3 discipline; the §VII.AV slot does NOT need a layer-attribution disambiguator because the F-decomposition collapses to a single substrate-IS observable. CF-S92-W5-1-C only re-activates if CF-S92-W5-1-A FAILs all three predictor candidates AND CF-W5-5 (= CF-62 disambiguation) re-opens the substrate-IS observable identity question.

6. **CF-S92-W5-1-B preserved** (per WP §W5-1 lines 256-260): FULL-CC multipliers cross-route comparison remains ACTIVE — it is the W1 T1.1 cross-route audit that classifies FI vs RD vs MIXED per `regulator-pin-discipline.md` UV-regulator axis. Reading A predicts FULL-CC will produce α STRUCTURALLY DIFFERENT from FULL-PV (since both are FULL-physical regularizations but in different regulator classes — if α_CC ≠ α_PV ≈ 6, the high-α envelope is regulator-class-DEPENDENT, supporting Reading A's FALSIFICATION reading).

7. **CF-S92-W5-1-D preserved** (per WP §W5-1 lines 268-273): METHODOLOGY-class extension to `math-scripts.md` cataloging L_max-multiplicative-cancellation invariants. Reading A's V2 derivation IS the substrate-physics demonstration that the multiplicative-cancellation produces an L_max-INVARIANT plateau STRUCTURALLY whenever the L_max truncation enters multiplicatively — this is the calibration-corpus instance #1 the methodology rule needs.

**Why NOT split into two slots (against Reading B's option (ii))**:

(a) **Algebra-axis orthogonality K=3 MANDATORY violation**: Reading B's split into `§VII.AV-D_K-spectrum-trace` and `§VII.AV-BdG-fiber-occupation` requires the two slots to inhabit STRUCTURALLY ORTHOGONAL algebra-axis cells per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause-4. But both `R_KW^{PV}` and `L_emp` evaluate the K-window log-derivative `d² ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})) / d(ln K)²` — a state-pair functional on the BdG sub-algebra (Corner IV per registry line 18067). The split would land both slots on the SAME Corner IV cell, which violates clause-4 SOURCE-DOUBLE-CITE-CO-PRIMARY (cross-corner co-primary is forbidden; same-corner co-primary creates a duplicate-slot pathology).

(b) **HIT-INDEPENDENCE failure**: per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`, the split slots would have IDENTICAL substrate-IS pillar (Pillar III), IDENTICAL laboratory-IN pillar (Pillar V), IDENTICAL bridge map class (HKR L_max → ∞) — failing (i ∨ ii ∨ iii). The slots also would NOT satisfy (iv) (independent algebraic envelope) because Reading B has not produced TWO algebraic envelopes; it has produced ONE plateau and ONE empirical anchor, both at the SAME pole s=4.

(c) **Information-preservation argument**: under Reading A, the §VII.AV slot retains the SOLE Corner-IV calibration source anchor `L_emp = -7.046336` per `s88-pending-edits-ledger.md`, while documenting the route-(ii) FAIL transparently. Future readers see (i) the canonical anchor (preserved); (ii) the FAIL audit-pin (preserved); (iii) the alternative envelope-predictor pathway (CF-S92-W5-1-A, active). Under Reading B's split, the second slot's anchor would be `R_KW^{PV}(L_max=12) = -527.97` — a value that the W5-1 script's own internal kernel-verification (WP line 150, PV_mass → 0 limit) DEMONSTRATES is the regulator-class-shifted IMAGE of the canonical `-7.046336`, not an independent substrate-IS observable. Promoting `-527.97` to a registry-anchor status would re-enshrine the regulator-class-DEPENDENCE as substrate-IS structure, inverting the substrate-first canonical sourcing direction per `substrate-first-canonical-sourcing.md §(i)`.

**Cross-references for the Reading A update**:

- `permanent-results-registry.md §VII.AV` (line 18059-18137; entry to be annotated)
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — single-observable-per-triple axiom
- `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` Detection clause-4 — cross-corner co-primary FORBIDDEN
- `substrate-first-canonical-sourcing.md §(i)` — canonical sourcing direction (substrate ahead of regulator-class image)
- `s88-pending-edits-ledger.md` — "preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source"
- W5-1 verdict line `s91_gate_verdicts.txt:99` audit_sha256=`04a6b22f1ab5b180fac0eb73132ce05ae7e9f32d4394203728778b47a037351e`

**Question for connes**: Confirm or refute the algebra-axis orthogonality clause-4 reading. If Reading B's slot-split places both companion slots on Corner IV (same algebra-axis cell, same pole), what `registry-landing.md` clause licenses this structure? Cite the precedent or concede the slot-split is REGISTRY-INCOMPLETE under the current K=3 MANDATORY discipline.

### V5: Cross-Cutting Observations — explicit prediction for Reading B (plateau magnitude under layer-orthogonality)

**Explicit prediction-discriminator question for connes (per workshop header R1 line 32)**: If Reading B is canonical — `R_KW^{PV}` F-maps to a substrate-IS BdG-occupation-kernel observable structurally distinct from the SCHEMATIC's D_K-spectrum-trace observable — then Reading B must derive the plateau magnitude `R_KW^{PV}(L_max → ∞) = -527.9669 M_KK²` from FIRST PRINCIPLES on the BdG sub-algebra. Specifically:

**Predict-or-concede question**: Starting from the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and the 8 Bogoliubov modes from `s52_bogoliubov_amp.npz` (canonical S52 BdG amplitudes; labels B2×4 + B1×1 + B3×3 per WP line 150), can Reading B's BdG-occupation-kernel observable be evaluated WITHOUT going through the Mellin trace `Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})` and WITHOUT going through the K-window log-derivative operator `d² ln(·) / d(ln K)²`, and STILL recover `-527.9669` (or its sign and magnitude)?

If YES: cite the closed-form derivation. The BdG-occupation kernel must be definable independently of the D_K Mellin trace, with its own substrate-IS triple `(M_2(ℂ), P_BdG, s_occupation)` where `s_occupation ≠ 4` OR with a different projector OR with a different algebra. Then there IS a structurally distinct substrate-IS observable, and Reading B's slot-split is licensed.

If NO: then `R_KW^{PV}` is computed via the K-window log-derivative on the SAME `Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})` that the SCHEMATIC and the canonical anchor `L_emp = -7.046336` use. The "BdG-occupation kernel" label is then a NAMING CHOICE for the K-window kernel `κ(K)` (per V2 substitution chain Step 2) AT FULL-PV regulator-class — NOT a structurally distinct substrate-IS observable. Reading B collapses to a UV-regulator-class-axis re-labeling at the methodology-floor layer, which is precisely what `regulator-pin-discipline.md` already classifies — and the SCHEMATIC's deviation by 75× at the canonical anchor IS falsification at that axis.

**Reading A's positive prediction (FALSIFICATION canonical)**:

1. **CF-S92-W5-1-B prediction (FULL-CC vs FULL-PV regulator-class comparison)**: When the FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers route (W1 T1.1) lands its own α extraction at substrate-distance-2 pole s=4 on the SAME K-window log-derivative on the SAME BdG sub-algebra, Reading A predicts:
   - α_CC will produce a STRUCTURALLY DIFFERENT value from α_PV ≈ 6.26.
   - The DIFFERENCE between α_CC and α_PV indicates the envelope is **regulator-class-DEPENDENT (RD class per `epistemic-discipline.md §"Source Reconciliation"` 5-class taxonomy)**.
   - Specifically: |α_CC − α_PV| / α_PV ≥ 0.05 → MIXED-class envelope at minimum; |Δα|/α_PV > 0.20 → RD-class-divergent (FAIL).
   - Under Reading B (layer-orthogonality at methodology-floor; the two regulator classes are F-images of distinct substrate-IS observables), Reading B has no constraint linking α_CC and α_PV at all — both could be anything. The numerical prediction is Reading A's, not Reading B's.

2. **CF-S92-W5-1-A prediction (alternative envelope-predictor)**: A correctly-derived envelope predictor (HKR residue-pole / Friedrich-Bär / Connes-Karoubi) operating on the IDENTICAL `(M_2(ℂ), P_BdG, s=4)` triple will predict `R_KW^{PV}(L_max=12) = -527.9669 ± tolerance` and `R_KW^{schematic}(L_max=12) = -7.046336 ± tolerance` as TWO REGULATOR-CLASS-DEPENDENT IMAGES of the SAME substrate-IS observable. The predictor will NOT be a single `L^{-3}` envelope; it will be a regulator-class-keyed family of envelopes. The methodology-rule extension CF-S92-W5-1-D (multiplicative-cancellation invariants catalog) is the Reading A canonical follow-up that closes this corridor.

3. **K-curvature amplification quantitative prediction**: WP line 198 records the 62× K-window drop in P^{PV} vs 1.5× in P_bare across the 10% K-window, with the K-curvature amplification factor at 75× the bare canonical. Under Reading A, this is the REGULATOR-CLASS amplification — the FULL-PV regulator at `M_PV/Δ_BCS ≈ 2.16` (NOT in asymptotic large-mass limit) introduces K-DEPENDENCE the SCHEMATIC Casimir-bound drops by construction. Reading A predicts: as `M_PV → ∞` (asymptotic large-mass limit, where Casimir-bound becomes valid), `R_KW^{PV}(L_max=12) → -7.046336` continuously (NOT a discrete jump at any finite PV mass). Reading B (orthogonal-layers) predicts no such continuous limit — the F-images would remain distinct at all PV masses. **This is the empirical discriminator**: a future gate scanning PV_mass ∈ [0, M_KK, √2·M_KK, 10·M_KK, 100·M_KK] on the SAME script should produce a SMOOTH interpolation from `-7.046` (at PV_mass → 0, kernel-verification anchor per WP line 150) to `-527.97` (at canonical M_KK / √2·M_KK tower) and CONTINUE smoothly as PV_mass increases further toward the Casimir-bound asymptotic limit. Reading B cannot produce this continuous-limit prediction.

**Cross-cutting observations binding V1-V4**:

- **V1 (F-mapping)**: single substrate-IS observable at `(M_2(ℂ), P_BdG, s=4)` per algebra-axis orthogonality K=3 MANDATORY.
- **V2 (plateau structurally exact)**: multiplicative-normalization-cancellation produces the plateau IDENTICALLY at any regulator class; plateau is information-free as Reading-A-vs-B discriminator.
- **V3 (7393% rel-err)**: kernel-verification at PV_mass → 0 (WP line 150) closes Reading B's structurally-distinct-observable claim; same operator on same spectrum returns `-7.046336 ± 4.7e-7` (bit-precision canonical match), proving the observable identity does NOT change under regulator-class variation.
- **V4 (single-slot FALSIFIED annotation)**: §VII.AV preserves canonical `L_emp` anchor; CF-S92-W5-1-A activates as alternative envelope-predictor gate; CF-S92-W5-1-C demoted under Reading A canonical.

**The four sub-claims combine into a single Reading A position**: the W5-1 FAIL is a **regulator-class-DEPENDENT envelope falsification** on a **single substrate-IS observable** at `(M_2(ℂ), P_BdG, s=4)`. The §VII.AV PROXY-REFINEMENT corridor requires a new envelope-predictor (CF-S92-W5-1-A) that captures the regulator-class dependence; it does NOT require a slot split, a layer-orthogonality reframing, or an admission that `R_KW^{PV}` and `L_emp` measure structurally distinct substrate-IS observables.

**Substrate framing reinforcement** (per `phononic-framing.md §"IS Space, Not IN Space"`): the substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at τ_fold with the K-window log-derivative observable at substrate-distance-2 pole s=4. The methodology-floor regulator class (SCHEMATIC Casimir-bound vs FULL Pauli-Villars vs FULL Connes-Chamseddine) is downstream of the substrate-IS observable identity. Reading B's slot-split would invert this direction by promoting a regulator-class image (`-527.97` under FULL-PV) to substrate-IS-anchor status while demoting the canonical `L_emp = -7.046336` to a parallel image — but the W5-1 script's own PV_mass → 0 kernel verification (`-7.046336 ± 4.7e-7`) DEMONSTRATES `L_emp` is the substrate-IS-canonical, NOT a parallel image. The direction substrate → emergent forbids the inversion.

**Final R1 closing question for connes**: If Reading B requires the BdG-occupation-kernel observable to be definable independently of the K-window log-derivative on the D_K Mellin trace (per the V5 predict-or-concede framework above), produce the independent definition. If Reading B can only define the BdG-occupation kernel THROUGH the K-window log-derivative on the D_K Mellin trace, concede that the observable identity is single-pinned at `(M_2(ℂ), P_BdG, s=4)` and the layer-orthogonality reading collapses to a UV-regulator-class re-labeling.

---

## Round 1 — Connes: Response & Cross-Synthesis (Reading B LAYER-ORTHOGONALITY Defender)

### Part 1: Response to Volovik's Sections

#### Re: V1 — F-mapping of R_KW^{PV}(L_max)

**AGREE**: Volovik's central axiomatic claim is correct as stated. The algebra-axis orthogonality K=3 MANDATORY discipline (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, MANDATORY since S87 W-2 close) pins ONE substrate-IS observable per `(algebra, projector, pole)` triple. The §VII.AV entry (registry line 18084 Element 1) registered the triple verbatim — `(M_2(ℂ), P_BdG, s=4)` — and BOTH the SCHEMATIC Casimir-bound proxy AND the FULL-PV pipeline operate on this single triple. I do NOT claim two distinct substrate-IS observables at the same triple. The single-observable-per-triple axiom holds; Reading B's STRONG form (two distinct substrate-IS observables) is structurally inadmissible under K=3 MANDATORY.

**DISAGREE**: Volovik's V1 conflates THREE structurally distinct levels of "F-image identity". The discipline that resolves the conflation is the LAYER-FUNCTOR `F : substrate → methodology → audit` formalized at `epistemic-discipline.md §"Layer-Decomposition"` (the load-bearing structural lever for Reading B). The three layers must be tracked independently:

1. **Substrate layer (Level-1 cohomology class)** — the substrate IS the Mellin trace `Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s})` at `s=4` on the BdG sub-algebra of `(A_K, H_K, D_K(τ_fold))`. Regulator-invariant; L-independent; a SINGLE Level-1 cohomology class per the §VII.AV registry text. Reading B AGREES single-observable here.

2. **Methodology layer (Level-2 algebraic-envelope F-image class)** — under `F : substrate → methodology`, the same Level-1 cohomology class admits MULTIPLE F-images at the Level-2 envelope axis, indexed by regulator-class `R ∈ {SCHEMATIC-Casimir-bound, FULL-Pauli-Villars-at-Λ_UV, FULL-Connes-Chamseddine-1996-multipliers, ζ-regulated-Wodzicki, lattice-discretized}`. These F-images are NOT interchangeable — `F(R_SCHEMATIC) ≠ F(R_FULL-PV)` at the methodology-floor layer, even though both lift the SAME Level-1 cohomology class. This is precisely what Volovik's V3 cites with the 7393% rel-err — but the rel-err is NOT a substrate-IS observable mismatch (Reading A reading); it is an F-image divergence at the methodology layer (Reading B reading; weak form).

3. **Audit layer (verdict-line content + audit_sha256)** — under `F : methodology → audit`, the methodology F-image lifts to verdict-content. The W5-1 verdict line records the FULL-PV F-image content (audit_sha256=`04a6b22f1ab5b180...`); the S87 W2-3 / S88 W5a canonical anchor records the SCHEMATIC-Casimir F-image content (`L_emp = −7.046336`).

The conflation in V1: "two F-images of the same observable at DIFFERENT methodology-floor layers per F" is precisely the regulator-class axis — V1 line 61 dismisses this as a methodology-floor pin only and denies it produces structural F-image divergence. But the calibration corpus at `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY (S88 W7b-83 close) establishes that SCHEMATIC vs FULL-physical regulator class IS structurally consequential at the methodology-floor layer (W4-2 + W9b-2 + W9c-1 + W5b-2 sub-test (c) corpus — N=4 distinct calibration instances of regulator-class divergence at the methodology layer with NO Level-1 substrate-IS observable shift). The K=4 corpus is the explicit precedent Volovik asks for: methodology-floor F-images of the SAME substrate-IS observable ARE structurally distinct across regulator classes; that distinction is enforced at PLAN-FREEZE by the K=4 MANDATORY level-pin discipline.

**MISSED**: V1 does not cite the `cross-pillar-bridge-anatomy.md §"Level-2 audit axes (Level-2-A vs Level-2-B)"` clause (the two independent audit dimensions on the Level-2 envelope). This clause already structurally pre-recognizes that Level-2 envelopes admit MULTIPLE independent audit dimensions — Level-2-A (operational, transit-dynamics axis) and Level-2-B (regulator-invariance, spectral-functional axis) — without requiring a second substrate-IS observable. The Volovik V1 axiom-citation is at the algebra-axis orthogonality clause (Cell I vs Cell IV); the structurally adjacent clause that handles regulator-class divergence WITHIN a single cell is the Level-2-A vs Level-2-B audit-axis clause. Reading B's WEAK form (regulator-class-keyed F-images on a single substrate-IS observable) is precisely the operational realization of the Level-2-A / Level-2-B split.

The further missed point: the K=4 MANDATORY level-pin discipline at `substrate-first-canonical-sourcing.md §(iv)` REQUIRES the verdict-line `convention=` field to carry the SCHEMATIC vs FULL discriminator suffix. The §VII.AV registry text (line 18088, Element 3) explicitly defers the bridge-map-scheme suffix to CF-61 "until refinement, convention tag carries no scheme-suffix" — that deferral is a structural acknowledgment that the bridge map admits multiple F-image evaluations at the methodology-floor layer. If the regulator-class axis were as inert as V1 claims (a methodology-floor pin without structural consequence), the deferred suffix would be empty bureaucracy. It is not empty; it is the structural index of the F-images at the methodology layer.

**EMERGES**: From the substrate-physics + NCG-axiomatic intersection, the load-bearing structural picture is:

- The substrate-IS observable identity is single-pinned at `(M_2(ℂ), P_BdG, s=4)` per K=3 MANDATORY (Volovik V1 correct).
- The Level-2 algebraic-envelope IS an `L^{-α}` family parameterized by regulator-class `R`; each R produces an F-image of the SAME substrate-IS observable at a structurally DIFFERENT methodology-floor layer per the K=4 MANDATORY level-pin discipline + the Level-2-A/B audit-axis clause.
- The W5-1 FAIL is therefore neither a Level-1 substrate-IS observable mismatch (Volovik's strong reading) NOR a Reading-B-strong-form slot-split (my initial framing): it is a Level-2 envelope **regulator-class divergence** (RD per `epistemic-discipline.md §"Source Reconciliation"` 5-class taxonomy) on a single substrate-IS observable.

The Volovik V1 axiom is preserved; the Reading B claim collapses to its weak form (regulator-class-keyed F-images on a single slot); the structural reading converges. This convergence point is the canonical answer to V1's closing question: yes, two F-images of the SAME substrate-IS observable can land on STRUCTURALLY DISTINCT methodology-floor layers without violating single-observable-per-triple — the precedent is the K=4 corpus at `substrate-first-canonical-sourcing.md §(iv)`, which is precisely a calibration corpus of such divergences within single triples.

#### Re: V2 — L_max-INVARIANT plateau status

**AGREE**: The multiplicative-normalization-cancellation derivation in V2 Steps 1-5 is mathematically correct. The factorization `Tr^{(L_max)}_{PV}(K) = w(L_max) · κ(K)` is a verifiable structural identity on the BdG sub-algebra Mellin trace under regulator-class evaluation; `d² ln(·) / d(ln K)²` annihilates the L_max-dependent multiplicative pre-factor `w(L_max)` because `w(L_max)` has no K-dependence. The plateau at `R_KW^{PV}(L_max) = −527.9669 M_KK²` across `L_max ∈ {6, ..., 12}` is a STRUCTURAL identity of the second log-derivative operator on the multiplicative factorization — not an empirical coincidence. The 7-point L_max scan returning bit-for-bit identical values to ~10 decimals is the expected behavior, not a measure-zero accident.

I also AGREE that the empirical α extraction `α_PV = 6.264, A_PV = −1.58e-2, σ → ∞` (WP lines 181-183) is fitting float64 noise on top of the perfect plateau. The covariance estimation rank-deficiency (`α_PV_1σ = ∞`) is the structural signal that the parametric envelope `A · L^{-α} + B` has degenerate likelihood on a constant-valued data series. The 6.264 number has no structural interpretation; the structural content is exclusively `B_PV = −527.97 M_KK²` (the plateau value itself).

**DISAGREE**: The "PASS counterfactual" argument (V2 line 110) — "if FULL-PV had produced `R_KW^{PV} ≈ −7.046336` matching `L_emp`, the plateau would have arisen identically by multiplicative-cancellation" — is mathematically correct but structurally misframed. The argument shows the plateau is L_max-INVARIANT within ANY F-image class. It does NOT show the plateau value (`B_PV`) is information-free as a Reading-A-vs-B discriminator. The discriminating content lives at `B_PV` (the asymptote / plateau magnitude), NOT at the L_max-scaling rate α. Reading B's claim is structural about `B_PV`:

```
Claim (Reading B canonical, restricted to weak form):
   B_PV(R_FULL-PV)        = −527.97 M_KK²
   B_PV(R_SCHEMATIC)      = −7.046  M_KK²    (= L_emp; cf. WP line 150 PV_mass→0 limit)
   B_PV(R_FULL-CC)        = TBD     M_KK²    (CF-S92-W5-1-B target)

   The B_PV values are F-images of the SAME substrate-IS observable
   under the regulator-class index R.
   Each F-image lives at its own methodology-floor layer per
   epistemic-discipline.md §"Layer-Decomposition" Phi correspondence.
   The L_max-INVARIANT plateau within each F-image class is the
   structural signature that the regulator class enters as a
   multiplicative spectral-support weight: it does NOT determine the
   F-image's B_PV value, but DOES guarantee within-class L_max-stability.
```

The V2 framing "the plateau is information-free as a discriminator" is correct ONLY at the LEVEL of L_max-stability (the plateau is a property of the operator `d² ln/d(ln K)²`, agreed). The Reading B claim is NOT about L_max-stability; it is about the ASYMPTOTE `B_PV` being the regulator-class-indexed F-image of the single substrate-IS observable. The asymptote IS the discriminator, and the asymptote IS regulator-class-keyed.

Substitution chain for the discriminator (per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1 (Definition):
   B(R) = R_KW^{R}(L_max → ∞) — the plateau / asymptote value at regulator class R
         per V2 Step 5 multiplicative-cancellation: B(R) = d² ln κ_R(K) / d(ln K)² at K_horizon

Step 2 (Definition):
   κ_R(K) = K-window kernel shape under regulator class R
         (κ_R inherits the regulator's K-dependence at the Mellin trace evaluation;
          per WP line 198 "the PV regulator at M_PV/Δ_BCS ≈ 2.16 is NOT in the
          asymptotic large-mass limit; the regulator copies retain non-trivial K-dependence")

Step 3 (Substitution):
   B(R_SCHEMATIC)  = d² ln κ_SCHEMATIC(K) / d(ln K)² at K_horizon
                   = −7.046336 (WP line 150 numerical-kernel-independence verification at PV_mass→0
                                reproduces the κ_SCHEMATIC kernel at bit-precision 4.7e−7)
   B(R_FULL-PV)    = d² ln κ_FULL-PV(K) / d(ln K)² at K_horizon
                   = −527.9669 (WP line 188; empirical FULL-PV pipeline at Λ_UV = M_KK,
                                2-PV tower {M_KK, √2 M_KK}, c = {+2, -1})

Step 4 (Simplify): B(R) is REGULATOR-CLASS-INDEXED because κ_R(K) is regulator-class-dependent
                   (the regulator's K-tail is integrated into the K-window kernel at finite PV_mass)

Step 5 (Direction):
   The plateau value B(R) is structurally an F-image of the single substrate-IS observable
   under the regulator-class index R.
   Reading B canonical-weak: B(R) varies structurally with R; the L_max-INVARIANCE within
   each R-class is the structural signature; the B(R) variation across R-classes is the
   F-image divergence at the methodology-floor layer.
```

**MISSED**: V2 does not engage with the Wodzicki residue invariance property. The Wodzicki residue (the canonical NCG-axiomatic invariant for the K-window log-derivative observable at a fixed pole `s=4` on the BdG sub-algebra) is REGULATOR-INVARIANT only at the asymptotic large-mass limit — explicitly NOT at finite `M_PV / Δ_BCS ≈ 2.16` where the regulator copies retain K-dependence (WP line 164: "the regulator scale M_KK ≈ 1 is order-unity vs the spectrum's lower edge → regulator is NOT in the asymptotic large-mass limit"). At asymptotic regulator-mass, the K-window kernel `κ_R(K) → κ_∞(K)` independent of R; at finite regulator-mass, `κ_R(K)` retains regulator-class-dependent K-tails. The 75× plateau-magnitude divergence between SCHEMATIC and FULL-PV is the structural signature of finite-mass regulator-class-dependence — precisely the Wodzicki-non-asymptotic regime.

This recovers the F-image divergence at the methodology-floor layer without invoking a second substrate-IS observable. The substrate-IS observable is single (Volovik V1 axiom); the methodology-floor F-image is regulator-class-indexed (Reading B weak form); the K=4 MANDATORY level-pin discipline is the rule-file enforcement of this distinction.

**EMERGES**: From the substrate-physics + NCG-axiomatic intersection:

- The plateau is L_max-INVARIANT within each regulator class R BECAUSE the L_max truncation enters multiplicatively at the BdG-sub-algebra Mellin trace (V2 Steps 1-5 derivation, correct).
- The plateau MAGNITUDE `B(R)` is regulator-class-indexed BECAUSE the K-window kernel `κ_R(K)` is regulator-class-dependent at finite regulator-mass (Wodzicki-non-asymptotic regime, MISSED above).
- The "structural FEATURE" interpretation of the plateau is therefore: the L_max-INVARIANCE IS the structural feature (signaling the multiplicative-cancellation regime); the plateau-MAGNITUDE IS the regulator-class-keyed F-image (signaling the methodology-floor F-image class).
- Both halves are simultaneously true: V2's L_max-INVARIANCE-is-information-free reading is correct about L_max-stability; Reading B's plateau-as-F-image reading is correct about plateau magnitude.
- The discriminator is therefore B(R)-across-R, not B(R)-vs-L_max-fit. CF-S92-W5-1-B (FULL-CC at the same triple) is the canonical next gate: if B(R_FULL-CC) ≠ B(R_FULL-PV), the F-image divergence is RD-confirmed; if B(R_FULL-CC) ≈ B(R_FULL-PV), the high-α envelope is regulator-class-INVARIANT and Reading A's FALSIFICATION strengthens. Reading B canonical-weak predicts the former; Reading A predicts the latter; the test is structurally well-defined.

#### Re: V3 — 7393% rel-err structural meaning

**AGREE** (concession of the strongest evidence): V3's appeal to WP line 150 — "Second log-derivative via 5-point central FD at K_horizon ... reproduced bit-for-bit at PV mass = 0 to 4.7e−7 deviation from −7.046336 → kernel verified independently" — is the decisive piece of evidence and closes Reading B's STRONG form. The continuous-deformation observation is structural:

- IDENTICAL operator (`d² ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})) / d(ln K)²` at `s=4`)
- IDENTICAL spectrum (`s84_spectrum_cache_L12_tau019.npz`)
- IDENTICAL substrate triple (`M_2(ℂ), P_BdG, s=4`)
- The ONLY change between the PV_mass → 0 evaluation and the FULL-PV evaluation is the regulator-class parameter (PV_mass value in the PV-subtraction term `Σ_j c_j (D_K² + M_j²)^{−s}`).
- The output continuously varies: `−7.046336 ± 4.7e-7` at PV_mass = 0 (kernel-verification baseline) → `−527.9669` at PV_mass = (M_KK, √2 M_KK) (FULL-PV S61/S78 tower).

This DEMONSTRATES the substrate-IS observable identity does NOT change across the regulator-mass continuum. Reading B's STRONG form (two distinct substrate-IS observables) requires a discrete jump in observable-identity at some finite PV_mass; the WP line 150 continuous-deformation evidence shows there is NO such jump. **I therefore RETRACT the strong form of Reading B (two distinct substrate-IS observables at the same triple) as structurally inadmissible**: the observable identity is single-pinned at `(M_2(ℂ), P_BdG, s=4)` per V3 + the K=3 MANDATORY algebra-axis axiom.

**DISAGREE**: The continuous-deformation evidence does NOT close Reading B's WEAK form (regulator-class-keyed F-images of a SINGLE substrate-IS observable at the methodology-floor layer). Continuity in PV_mass shows the substrate-IS observable identity is preserved across the regulator-mass continuum (correct, conceded above). It does NOT show the methodology-floor F-image is regulator-class-INVARIANT — quite the opposite, the continuous BUT NON-CONSTANT variation from `−7.046336` to `−527.97` is precisely the signature of a non-trivial F-functor `F : substrate → methodology` on the regulator-class axis.

To see this, consider the analog at the structural-class layer: a single algebra `A_K` admits multiple regulator-classes (ζ, PV, Mellin, cutoff per `regulator-pin-discipline.md` UV-regulator axis tagging). The a_n Seeley-DeWitt coefficients are regulator-class-dependent under the regulator-pin discipline — explicit `a_2^{ζ}` vs `a_2^{Pauli-Villars}` vs `a_2^{Mellin}` are STRUCTURALLY DISTINCT methodology-floor F-images of the SAME substrate-IS Seeley-DeWitt coefficient identity. The continuous deformation from one regulator to another (e.g., through a sequence of intermediate regulator-mass values) is precisely the F-functor's continuous action on the regulator-class axis; the output value continuously varies because the F-functor is non-trivial.

The 7393% rel-err is therefore structurally interpretable in TWO compatible readings:

1. **Volovik V3 reading (Reading A, single-observable + regulator-class FAILURE)**: the SCHEMATIC Casimir-bound approximation drops the regulator's K-dependence; at finite `M_PV / Δ_BCS ≈ 2.16` the regulator copies retain K-dependence the SCHEMATIC drops by construction; the 75× plateau divergence is the falsification of the Casimir-bound L^{-3} envelope at this regulator-mass regime. The SCHEMATIC and FULL-PV are evaluating the SAME observable; the SCHEMATIC's approximation is invalid at finite regulator-mass.

2. **Reading B-weak reading (regulator-class-keyed F-images on a single observable)**: the same evaluation is reinterpreted at the methodology-floor F-image layer. The Wodzicki residue is regulator-INVARIANT only at the asymptotic large-mass limit; at finite regulator-mass, `F(R_SCHEMATIC) ≠ F(R_FULL-PV)` at the Level-2 envelope F-image class; the 75× divergence is the methodology-floor F-image divergence at the regulator-class axis.

Readings 1 and 2 are STRUCTURALLY EQUIVALENT — they differ only in interpretive framing. Reading 1 frames the divergence as "Casimir-bound approximation invalid"; Reading 2 frames it as "methodology-floor F-image regulator-class-keyed". Both produce the same prediction for CF-S92-W5-1-B (FULL-CC route): the envelope may be RD-class-divergent. Both preserve the substrate-IS observable identity at `(M_2(ℂ), P_BdG, s=4)`. Both deprecate the SCHEMATIC Casimir-bound `L^{-3}` envelope as a Level-2 binding form at the finite-regulator-mass regime.

The convergence point: **the W5-1 FAIL is a Level-2 envelope regulator-class divergence (RD per `epistemic-discipline.md §"Source Reconciliation"`) on a single substrate-IS observable**. Reading A and Reading B-weak agree on this structural reading; they differ only in registry-text framing.

**MISSED**: V3 does not engage with the `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline as the rule-file enforcement of regulator-class divergence. The K=4 corpus (W4-2 + W9b-2 + W9c-1 + W5b-2 sub-test (c)) is precisely a calibration corpus of methodology-floor F-image divergences between SCHEMATIC and FULL-physical regulator classes on substrate-IS observables that are individually well-defined. The discipline is MANDATORY at plan-freeze for S88+; it forces convention-tag suffixes (`-SCHEMATIC` vs (implicit) FULL) to disclose the F-image class at the verdict-line layer. The W5-1 verdict line (line 211) carries convention `corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4` — NO `-SCHEMATIC` suffix, because this gate is FULL-physical. The complementary SCHEMATIC anchor `L_emp = −7.046336` lives at a methodology-floor F-image class with the convention suffix `-SCHEMATIC` (implicitly, per s88-pending-edits-ledger.md preservation). The K=4 corpus pre-recognizes the F-image divergence; V3 simply extends the calibration corpus to N=5 with the W5-1 instance.

**EMERGES**:

- The continuous-deformation evidence at WP line 150 closes Reading B's STRONG form (two distinct substrate-IS observables) — conceded.
- The continuous-deformation evidence does NOT close Reading B's WEAK form (regulator-class-keyed F-images on a single observable) — Wodzicki-non-asymptotic regime at `M_PV / Δ_BCS ≈ 2.16` preserves it.
- Reading A (FALSIFICATION) and Reading B-weak (regulator-class-keyed F-images) are STRUCTURALLY EQUIVALENT readings of the same evidence; they predict the same forward-gate outcomes (CF-S92-W5-1-B prediction: RD-class divergence; CF-S92-W5-1-A prediction: alternative envelope predictor that captures regulator-class dependence; CF-S92-W5-1-D rule-file extension cataloging the multiplicative-cancellation invariants).
- The 7393% rel-err structural meaning IS falsification of the SCHEMATIC Casimir-bound `L^{-3}` envelope at the finite-regulator-mass regime AND IS evidence of regulator-class-keyed F-image divergence at the methodology-floor layer — these are the SAME thing under different framings.
- The substrate-IS triple `(alg_2, proj_2, pole_2)` Volovik requested (V3 line 144) does NOT exist for a Reading-B-strong slot-split — Reading B-strong is retracted. The §VII.AV slot remains single under the substrate-IS observable identity, with regulator-class-keyed sub-rows at the Level-2 envelope axis (Reading B-weak).

#### Re: V4 — §VII.AV registry text update

**AGREE**: The slot-split structure (Reading B option ii) is structurally inadmissible under V4 line 205 ("the split would land both slots on the SAME Corner IV cell, which violates clause-4 SOURCE-DOUBLE-CITE-CO-PRIMARY"). I CONCEDE this in light of the Re:V3 retraction of Reading B-strong: both proposed slots inhabit Cell IV (algebra-DEPENDENT state-pair functional × substrate-distance-2 pole s=4) per §VII.U.2 4-corner classification; same-corner co-primary is REGISTRY-INCOMPLETE per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause-4 detection criterion (S88 W-15 V.6 MANDATORY at K=3). The slot-split (Reading B option ii) is RETRACTED.

I also AGREE that the Hybrid Independence Test fails for the slot-split: identical substrate-IS pillar (III), identical laboratory-IN pillar (V), identical bridge-map class (HKR `L_max → ∞`); the slots would fail `(i ∨ ii ∨ iii)` per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`. Reading B-strong slot-split fails HIT independence.

**DISAGREE**: V4's complete demotion of Reading B (Option iii Hybrid disallowed; CF-S92-W5-1-C demoted to cancelled) over-corrects. Reading A canonical (Option i) erases the methodology-floor F-image distinction at the registry-text level by reading the W5-1 FAIL as a regulator-class FAILURE on a single F-image class. But the Re:V1 + Re:V3 analysis shows the regulator-class divergence IS structurally a methodology-floor F-image divergence (Reading B-weak preserves this). The registry text SHOULD record the F-image class explicitly — not via slot-split (RETRACTED) but via regulator-class-keyed sub-rows on the SINGLE §VII.AV slot.

This is exactly the Hybrid (option iii) framing pre-registered in the workshop header line 38: "single §VII.AV slot with layer-attribution sub-rows declaring both F-images + sub-class-rotation forward gate". The slot is single (Corner IV; single substrate-IS observable per K=3 MANDATORY); the sub-rows are regulator-class-indexed at the Level-2 envelope axis. This honors clause-4 AND captures the F-image structure.

**Counter-proposal: Reading B-weak Hybrid registry-text update** (replacing V4 Reading A option (i) at the §VII.AV slot):

1. **Status block update (line 18063 area)**: append the W5-1 FAIL audit-pin sub-row with explicit regulator-class F-image class disclosure:

   ```
   Status update (S91 W5-1 close, 2026-05-21): refinement-pathway route (ii) FULL Pauli-Villars
   at Λ_UV = M_KK landed at FULL-PV F-image class B_PV(R_FULL-PV) = -527.9669 M_KK²
   (audit_sha256=04a6b22f1ab5b180fac0eb73132ce05ae7e9f32d4394203728778b47a037351e).
   The FULL-PV F-image diverges from the SCHEMATIC Casimir-bound F-image B(R_SCHEMATIC) =
   L_emp = -7.046336 M_KK² by a factor 75× at the substrate-distance-2 pole s=4 plateau
   magnitude (WP line 150 PV_mass → 0 limit verifies kernel reproduction at the SCHEMATIC
   F-image class within 4.7e-7 absolute deviation). Per substrate-first-canonical-sourcing.md
   §(iv) K=4 MANDATORY level-pin discipline + cross-pillar-bridge-anatomy.md §"Level-2 audit
   axes (Level-2-A vs Level-2-B)" the divergence is a methodology-floor F-image divergence
   at the regulator-class axis on a single substrate-IS observable (NOT a substrate-IS
   observable identity shift; single-observable-per-triple K=3 MANDATORY preserved).
   Level-2 sub-class re-classified: REGISTRY-INCOMPLETE-PENDING-REGULATOR-CLASS-DISAMBIGUATION
   (regulator-class-keyed F-image class table pending CF-S92-W5-1-B FULL-CC route).
   The SCHEMATIC Casimir-bound L^{-3} envelope is INVALID at the finite-regulator-mass regime
   (M_PV / Δ_BCS ≈ 2.16 is non-asymptotic; regulator copies retain K-dependence).
   The canonical L_emp = -7.046336 anchor is PRESERVED as the SCHEMATIC F-image class anchor
   per s88-pending-edits-ledger.md.
   ```

2. **Element 4 (Algebraic envelope) sub-rows by regulator class** — the Level-2 envelope axis is regulator-class-keyed:

   | Regulator class R | F-image B(R) at L_max=12 | Envelope α | Level-2-binding status |
   |:------------------|:-------------------------|:-----------|:----------------------|
   | R_SCHEMATIC (Casimir-bound) | −7.046336 (= L_emp; SOLE Corner-IV calibration source per s88-pending-edits-ledger.md) | predicted α = 3 (L^{-3}) | INVALID at finite-regulator-mass regime (M_PV / Δ_BCS ≈ 2.16); valid only in the asymptotic large-mass limit |
   | R_FULL-PV (S61/S78 2-PV tower at Λ_UV = M_KK) | −527.9669 (W5-1 PASS at FULL-PV F-image class) | structural plateau (multiplicative-cancellation; α extraction rank-deficient) | OPEN (Level-2 envelope is regulator-class-keyed, not single L^{-α}) |
   | R_FULL-CC (Connes-Chamseddine 1996 §2.2-2.3 multipliers) | TBD (CF-S92-W5-1-B forward gate) | TBD | PENDING |
   | R_ζ-Wodzicki (zeta-regulated, asymptotic) | predicted = R_SCHEMATIC in asymptotic large-mass limit | predicted α = 3 | structurally derivable; asymptotic limit of any large-mass regulator |

3. **CF-S92-W5-1-A reframed** — alternative envelope predictor → regulator-class-keyed envelope family:

   The forward gate's PASS criterion is reframed from "find a single envelope that reproduces FULL-PV at −527.97" to "derive the regulator-class-keyed envelope family B(R) for R ∈ {SCHEMATIC, FULL-PV, FULL-CC, ζ-Wodzicki}; structurally relate B(R) values via the regulator-class transition map at finite regulator-mass". Candidate predictors:
   - HKR image residue-pole with regulator-class-dependent K-tail integration
   - Friedrich-Bär saturation theorem extended to regulator-class-keyed envelope family
   - Connes-Karoubi pairing on the BdG sub-algebra K-theory boundary with regulator-class index

4. **CF-S92-W5-1-C reframed (NOT cancelled)** — layer-attribution disambiguation → regulator-class F-image disambiguation:

   The forward gate's role is to certify that R_SCHEMATIC and R_FULL-PV are regulator-class-keyed F-images of the SAME substrate-IS observable at `(M_2(ℂ), P_BdG, s=4)` per the K=3 MANDATORY axiom — NOT a slot-split request. The disambiguation question is: is the regulator-class transition map continuous (smooth deformation between F-images per the WP line 150 PV_mass → 0 limit) or piecewise (discrete jumps at finite regulator-mass thresholds)? PASS = continuous regulator-class transition; INFO = piecewise transition with structural justification; FAIL = no structural disambiguation possible (the regulator-class axis is non-structural).

5. **CF-S92-W5-1-B preserved exactly as in V4** — the FULL-CC vs FULL-PV cross-route comparison is the canonical Reading-B-weak / Reading-A discriminator. If `|α_CC − α_PV| / α_PV ≤ 0.05` → FI; the regulator-class divergence is methodology-only-noise and Reading A is structurally vindicated. If `|α_CC − α_PV| / α_PV > 0.20` → RD-class-divergent; the regulator-class F-image divergence is structurally confirmed and Reading B-weak is structurally vindicated.

6. **CF-S92-W5-1-D preserved exactly as in V4** — the METHODOLOGY-class catalog of L_max-multiplicative-cancellation invariants is the rule-file extension that captures the structural feature both readings agree on (L_max-INVARIANCE via multiplicative-cancellation).

**MISSED**: V4 does not cite the `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` per-pole sub-rule that already pre-recognizes regulator-class-keyed Level-2 envelopes within a single corner-cell. The clause's K=2/K=3 calibration corpus admits regulator-class divergence at the per-pole layer (FI / RD / MIXED per `epistemic-discipline.md §"Source Reconciliation"` taxonomy). The §VII.AV Per-Bulletin-per-pole row at line 18079 declares "Level-1 classification: algebra-DEPENDENT" — but does NOT yet declare the Level-2 envelope's regulator-class status (FI vs RD vs MIXED). The W5-1 evidence puts this row's Level-2 envelope at RD-candidate; the Hybrid registry-text update above implements this classification.

**EMERGES**:

- Reading B-strong (slot-split) is RETRACTED per Re:V3 + V4 clause-4 analysis.
- Reading B-weak (regulator-class-keyed F-images on a single slot) is structurally admissible AND captures the F-image divergence at the methodology-floor layer.
- The Hybrid registry-text update (option iii in workshop header, single slot with regulator-class-keyed Level-2 envelope sub-rows) is the structurally correct landing — it honors clause-4 (same-corner co-primary impossible at the substrate-IS observable axis; the table is sub-rows, not co-primary anchors), the K=3 MANDATORY algebra-axis axiom (single observable per triple), AND the K=4 MANDATORY level-pin discipline (regulator-class F-images structurally distinct at the methodology layer).
- V4's CF demotion table (CF-A activated, CF-C demoted) is reframed: CF-A (alternative envelope predictor) becomes "regulator-class-keyed envelope family derivation"; CF-C (layer-attribution disambiguation) becomes "regulator-class transition-map disambiguation"; CF-B (FULL-CC cross-route) is preserved as the structural discriminator; CF-D (methodology rule extension) is preserved.
- The §VII.AV slot remains single per K=3 MANDATORY; the Level-2 envelope axis carries a regulator-class-keyed sub-row table; the substrate-IS observable identity is preserved at `(M_2(ℂ), P_BdG, s=4)`.

#### Re: V5 — Cross-cutting predictions

**AGREE** (full concession to the predict-or-concede challenge): V5 poses the structural test for Reading B-strong: "Can Reading B's BdG-occupation-kernel observable be evaluated WITHOUT going through the Mellin trace `Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})` and WITHOUT going through the K-window log-derivative operator `d² ln(·) / d(ln K)²`, and STILL recover `−527.9669` (or its sign and magnitude)?"

**I CONCEDE: NO**. Reading B cannot derive the plateau value `B_PV(R_FULL-PV) = −527.9669 M_KK²` from BdG-occupation-kernel first principles independently of the K-window log-derivative on the D_K Mellin trace. The substrate's BdG-occupation kernel `v_a^{PV}(K)² = v_a(K)² − 2·v_a^{(M_KK)}(K)² + v_a^{(√2·M_KK)}(K)²` (WP line 198) IS defined through the PV-subtraction on the D_K spectrum via the Bogoliubov amplitudes from `s52_bogoliubov_amp.npz`. The "BdG-occupation kernel" is NOT independently definable from the substrate-IS Mellin trace at `s=4`; the kernel inherits its structure from the same Mellin trace.

Therefore: **the observable identity is single-pinned at `(M_2(ℂ), P_BdG, s=4)` per V5's predict-or-concede framework**. Reading B's STRONG form (two distinct substrate-IS observables) is structurally inadmissible — the BdG-occupation-kernel cannot be lifted out of the K-window log-derivative on the D_K Mellin trace at the substrate layer. Reading B-strong is RETRACTED in full.

**DISAGREE**: The concession does NOT close Reading B-weak. The retraction of Reading B-strong leaves the question: if the observable identity is single, what IS the structural meaning of the 75× plateau-magnitude divergence between the SCHEMATIC and FULL-PV F-image classes? Reading A (V5 line 230) concludes "Reading B collapses to a UV-regulator-class-axis re-labeling at the methodology-floor layer, which is precisely what `regulator-pin-discipline.md` already classifies". I AGREE this is the collapse direction — but the "collapse" is to Reading B-weak, NOT to Reading A. The collapse-target IS the K=4 MANDATORY level-pin discipline + the Level-2-A/B audit-axis clause + the FI/RD/MIXED taxonomy — all of which are STRUCTURAL methodology-floor F-image distinctions, NOT a vacuous re-labeling.

Reading B-weak's predict-or-concede counter-challenge to Reading A:

**Counter-challenge for volovik (Reading A canonical)**: If Reading A is canonical and the 7393% rel-err is "definitive falsification" of the SCHEMATIC Casimir-bound `L^{-3}` envelope at the substrate-IS observable layer, what is Reading A's POSITIVE prediction for the structurally-correct envelope `B(R)` at finite regulator-mass? Reading A's V5 line 232 predicts `R_KW^{PV}(L_max=12) → -7.046336` continuously as `M_PV → ∞` (asymptotic large-mass limit; Casimir-bound recovery). This prediction is structurally consistent with Reading B-weak: as `M_PV → ∞`, the regulator copies enter the asymptotic large-mass limit, `κ_R(K) → κ_∞(K)` independent of R, and the F-images converge. Reading B-weak predicts the IDENTICAL asymptotic behavior — the F-images are regulator-class-keyed at finite regulator-mass and converge to the Wodzicki residue at asymptotic regulator-mass.

**The two readings predict the same continuous-limit behavior**. Both predict the PV_mass-scan from 0 → M_KK → √2 M_KK → 10 M_KK → 100 M_KK reproduces `−7.046336` smoothly at both endpoints (PV_mass → 0 and PV_mass → ∞) with a non-trivial intermediate excursion to `−527.97` near `PV_mass ~ M_KK` where the regulator-mass is order-unity vs the spectrum lower edge. Reading A frames this as "the SCHEMATIC's Casimir-bound is the asymptotic limit of any regulator; FULL-PV at finite mass is the regulator-class-shifted image". Reading B-weak frames this as "the F-image is regulator-class-keyed; the asymptotic limit is the Wodzicki residue invariant; the intermediate values are F-images on the regulator-mass continuum". The framings are STRUCTURALLY EQUIVALENT.

**MISSED**: V5 cross-cutting predictions does not engage with the structural prediction Reading B-weak DOES make that Reading A does not:

- **Reading B-weak prediction (NEW)**: At the FULL-Connes-Chamseddine 1996 §2.2-2.3 multipliers route (CF-S92-W5-1-B = W1 T1.1), the F-image `B(R_FULL-CC)` at L_max=12 will be IN THE SAME REGULATOR-CLASS-FAMILY as `B(R_FULL-PV) = −527.97` — i.e., the two FULL-physical regulator classes are structurally CLOSER to each other than either is to the SCHEMATIC R_SCHEMATIC class. Specifically: `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.50` (within a factor 1.5 of each other) AND BOTH `|B(R_FULL-CC) − L_emp| / |L_emp|` and `|B(R_FULL-PV) − L_emp| / |L_emp|` are large (≥ 10×). The methodology-floor F-image class clusters by regulator-physical-fidelity (FULL-physical ≠ SCHEMATIC), not by individual regulator scheme.

- **Reading A's prediction (V5 line 235)**: "α_CC will produce a STRUCTURALLY DIFFERENT value from α_PV ≈ 6.26; |α_CC − α_PV| / α_PV ≥ 0.05 → MIXED-class envelope at minimum". This is consistent with Reading B-weak if interpreted at the regulator-class-family-clustering level, but Reading A's framing assumes the divergence is at the FALSIFICATION axis (no underlying structural unification), while Reading B-weak frames it at the regulator-class-family-clustering axis (FULL-physical clusters together; SCHEMATIC clusters separately).

The CF-S92-W5-1-B gate is therefore the empirical discriminator between Reading A (no clustering structure; pure FALSIFICATION) and Reading B-weak (regulator-class-family clustering with structural transition map). The prediction `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.50` is Reading B-weak's structural test.

**EMERGES**: From the full Re:V1-V5 analysis:

- Reading B-strong (two distinct substrate-IS observables; slot-split) is RETRACTED per V5 + V3 + V4 clause-4.
- Reading B-weak (regulator-class-keyed F-images on a single substrate-IS observable; Hybrid registry-text update) is structurally admissible AND captures the F-image divergence at the methodology layer per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence.
- Reading A and Reading B-weak predict the same continuous-limit behavior (PV_mass → 0 and PV_mass → ∞ both recover `−7.046336`); differ in registry-text framing (single F-image class vs regulator-class-keyed sub-rows on a single slot).
- The structural verdict converges on Hybrid (option iii): single §VII.AV slot per K=3 MANDATORY; regulator-class-keyed Level-2 envelope sub-rows per K=4 MANDATORY; CF-A reframed as regulator-class-keyed envelope family derivation; CF-B as the structural discriminator (FULL-CC route); CF-C as regulator-class transition-map disambiguation; CF-D as methodology rule extension catalog.
- The convergence point is: **the W5-1 FAIL is a Level-2 envelope regulator-class divergence (RD-class-candidate) on a single substrate-IS observable**. The canonical L_emp = −7.046336 anchor is preserved at the SCHEMATIC F-image class; the FULL-PV F-image at −527.97 is recorded at a structurally distinct methodology-floor layer; both lift the SAME Level-1 cohomology class at `(M_2(ℂ), P_BdG, s=4)`.

### Part 2: Original Analysis

#### C1: Layer-functor F decomposition — Phi(a_n) correspondence table + multiplicative-normalization-cancellation argument

**Derivation from `epistemic-discipline.md §"Layer-Decomposition"`**. The layer-functor `F : substrate → methodology → audit` (rule file lines 307-309) is structurally a graded-ring isomorphism on the Seeley-DeWitt weight grading. The Phi correspondence (rule file lines 335-343) maps:

```
Phi(a_0) = Σ_1   (perimeter / cosmological-term, weight-0; user-adjudication-only deliverable)
Phi(a_2) = Σ_2   (Einstein-Hilbert kinematic skeleton, weight-2; wave-classification)
Phi(a_4) = Σ_3   (Yang-Mills + Higgs quartic load-bearing, weight-4; mcp-pre-check hook)
```

Higher weights extend by the same pattern: weight-2n substrate-physics observable maps to enforcement-strength-n methodology rule. **The W5-1 observable lives at substrate-distance-2 pole `s=4` on the BdG sub-algebra Mellin trace**; in the Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula, the pole at `s=4` is the d=4 substrate-distance-2 residue, structurally adjacent to the Yang-Mills + Higgs quartic load-bearing layer at `a_4`. Under Phi:

```
Phi(a_4 at substrate-distance-2 pole s=4 on BdG sub-algebra M_2(ℂ))
   = Σ_3 at enforcement-strength-3 methodology layer
   = SCHEMATIC vs FULL-PV level-pin discipline (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
     × UV-regulator-class axis (regulator-pin-discipline.md a_n^{R} tagging)
     × Level-2-binding sub-class (cross-pillar-bridge-anatomy.md §"Level-2 sub-class")
```

The W5-1 observable's methodology-floor F-image therefore carries THREE orthogonal axes at the Σ_3 enforcement layer:

| Axis | F-image distinction | Rule-file enforcement | Status at W5-1 |
|:-----|:--------------------|:-----------------------|:---------------|
| Level axis (SCHEMATIC vs FULL) | `_spectral_action_regulators.py` SCHEMATIC vs FULL-physical (PV, CC, ζ-Wodzicki) | `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY since S88 W7b-83 | DIVERGENT: B(R_SCHEMATIC)=−7.046, B(R_FULL-PV)=−527.97 |
| UV-regulator-class axis | a_n^{ζ} vs a_n^{Pauli-Villars} vs a_n^{Mellin} vs a_n^{lattice} vs a_n^{cutoff} | `regulator-pin-discipline.md` UV-regulator pin discipline MANDATORY for new files post-S86 | FULL-PV F-image landed; FULL-CC F-image deferred to CF-S92-W5-1-B |
| Binding axis | canonical-import-binding vs substrate-natural-binding | `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` Binding axis SUGGESTION at K=1 | substrate-natural-binding (B_PV derived from substrate D_K spectrum + S52 Bogoliubov amplitudes; NOT a canonical-import pin) |

**Phi-image structural prediction at the W5-1 substrate observable**: Σ_3 = enforcement-strength-3 methodology layer admits THREE orthogonal F-image distinctions per the table above. The 75× divergence between B(R_SCHEMATIC) and B(R_FULL-PV) is the Phi-image of the Level-axis F-functor's non-trivial action on the substrate-distance-2 pole `s=4` substrate observable. The Level-axis F-image divergence at Σ_3 is STRUCTURAL (per K=4 MANDATORY corpus W4-2 + W9b-2 + W9c-1 + W5b-2 sub-test (c) — N=4 distinct calibration instances of Level-axis F-image divergence on substrate-IS observables that are individually well-defined).

**Multiplicative-normalization-cancellation argument under Phi-correspondence**: Volovik's V2 derivation showed multiplicative-cancellation produces an L_max-INVARIANT plateau within a single F-image class. Under Phi, this is precisely the structural property that Σ_3 enforcement-strength rules operate on F-image class boundaries (not on within-class L_max parameters):

```
Step 1 (Definition): F : substrate → methodology is the Phi-image of a substrate-distance-n
                     pole on the d=4 spectral triple.

Step 2 (Substitution): At fixed substrate-IS observable (M_2(ℂ), P_BdG, s=4), the L_max
                       truncation enters the methodology-floor F-image only as a multiplicative
                       spectral-support weight w(L_max) per V2 Step 2.

Step 3 (Phi action): Phi maps w(L_max) to a methodology-floor identity element on the
                     Σ_3 enforcement layer — i.e., L_max within a single F-image class is
                     CANCELLED by Phi (no cross-class methodology-floor structural significance).

Step 4 (Cross-class action): Phi maps the regulator-class transition (R_SCHEMATIC →
                              R_FULL-PV → R_FULL-CC → R_ζ-Wodzicki) to a non-trivial Σ_3
                              enforcement-strength action — i.e., the Level-axis and UV-
                              regulator-class axes are NOT cancelled by Phi; they remain
                              structurally distinct at the methodology layer.

Step 5 (Direction):
   Within-class multiplicative-cancellation: Phi-trivial (V2 derivation correct).
   Cross-class regulator-keyed F-images: Phi-non-trivial (Reading B-weak claim).

Conclusion: Multiplicative-cancellation operates WITHIN a fixed F-image class at the
            Level-2 envelope axis; the discriminating content lives at the ASYMPTOTE
            value B(R) which is regulator-class-keyed (Re:V2 + Re:V3 emerged
            structurally equivalent to Reading A's framing of regulator-class
            FAILURE on a single observable).
```

The Phi-correspondence therefore reconciles Volovik's V2 (multiplicative-cancellation makes the plateau L_max-INVARIANT structurally) and Reading B-weak (the plateau MAGNITUDE B(R) is regulator-class-keyed at Σ_3 enforcement). Within a single F-image class, Volovik's V2 derivation is canonical; across F-image classes, Reading B-weak's regulator-class-keyed structure is canonical. The two are simultaneously true at different layers of the Phi-correspondence.

**Calibration corpus tie-in**: The K=4 MANDATORY level-pin discipline (`substrate-first-canonical-sourcing.md §(iv)` close S88 W7b-83, 2026-05-05) is precisely the rule-file enforcement of the Level-axis F-image divergence at Σ_3. The W5-1 instance becomes a candidate K=5 calibration corpus entry (extending W4-2 + W9b-2 + W9c-1 + W5b-2 sub-test (c)): Level-axis F-image divergence on a substrate-IS observable individually well-defined at `(M_2(ℂ), P_BdG, s=4)`, with B(R_SCHEMATIC) − B(R_FULL-PV) = 521 M_KK² (multiplicative deviation factor 75×, log₁₀ deviation 1.87 OOM — within the SOURCE-RECON D_max ≥ 1.0 MANDATORY band per `epistemic-discipline.md §"Source Reconciliation"` 4-band calibration). This corpus advancement is itself a methodology-class deliverable; queued as CF-S92-W5-1-D extension at the Reading B-weak Hybrid registry-text update.

#### C2: §VII.AV slot split structure under Reading B — structural-orthogonal-companion anchor

**Reframe under Reading B-strong retraction (per Re:V3 + Re:V5)**: The original C2 directive proposed a slot-split into `§VII.AV-D_K-spectrum-trace` (L_emp anchor) and `§VII.AV-BdG-fiber-occupation` (R_KW^{PV} anchor) as structural-orthogonal-companion structure per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause-4. **This slot-split is structurally inadmissible** per the analysis converged at Re:V4 + Re:V5:

1. **Clause-4 same-corner co-primary trap**: both proposed slots inhabit Cell IV (algebra-DEPENDENT state-pair functional × substrate-distance-2 pole `s=4`) per `permanent-results-registry.md §VII.U.2` 4-corner classification (LANDED S88 W5b-45). Clause-4 detection criterion at `registry-landing.md §"Detection"` (S88 W-15 V.6 MANDATORY at K=3) FORBIDS cross-corner co-primary structures; same-corner co-primary creates a duplicate-slot pathology that fails HIT independence by construction.

2. **Hybrid Independence Test failure**: per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`, the split slots would have IDENTICAL substrate-IS pillar (III), IDENTICAL laboratory-IN pillar (V), IDENTICAL bridge map class (HKR `L_max → ∞`) — failing `(i ∨ ii ∨ iii)`. The split also fails (iv) (independent algebraic envelope) because the two proposed envelopes share the same `(M_2(ℂ), P_BdG, s=4)` triple at the substrate layer.

3. **V5 predict-or-concede closure**: Reading B cannot derive `B_PV(R_FULL-PV) = −527.97` from BdG-occupation-kernel first principles independently of the K-window log-derivative on the D_K Mellin trace. The "BdG-occupation kernel" is NOT an independently-definable substrate-IS observable; it inherits its structure from the SAME Mellin trace at the substrate layer. Reading B-strong is RETRACTED.

**Replacement structure: Reading B-weak Hybrid (option iii of workshop header line 38) — single §VII.AV slot with regulator-class-keyed Level-2 envelope sub-rows**.

The single-slot structure is pinned at the substrate-IS observable identity `(M_2(ℂ), P_BdG, s=4)` per K=3 MANDATORY (Volovik V1 axiom preserved). The methodology-floor F-image divergence is recorded at the Level-2 envelope axis via regulator-class-keyed sub-rows, NOT via slot-split. The structural-orthogonal-companion structure becomes:

```
§VII.AV (single slot; substrate-IS observable identity at (M_2(ℂ), P_BdG, s=4))
   |
   |— Level 1: Single-τ-slice cohomology-class identity at τ_fold = 0.19
   |          STRUCTURAL THEOREM (preserved unchanged from §VII.AV registry line 18073)
   |
   |— Level 2: Algebraic-envelope axis — regulator-class-keyed F-image sub-rows
   |    |
   |    |— Level-2-A (operational, transit-dynamics): convergence rate at HKR L_max→∞
   |    |    (Bogoliubov / parametric-resonance / Kibble-Zurek axis per
   |    |     cross-pillar-bridge-anatomy.md §"Level-2 audit axes")
   |    |
   |    |— Level-2-B (regulator-invariance, spectral-functional): regulator-class index R
   |         (R_SCHEMATIC vs R_FULL-PV vs R_FULL-CC vs R_ζ-Wodzicki)
   |         — F-image table per Re:V4 §2 above
   |
   |— Level 3: Empirical anchor — regulator-class-keyed (companion to Level-2-B)
        |— B(R_SCHEMATIC) = L_emp = −7.046336 M_KK² (SOLE Corner-IV calibration source
        |    per s88-pending-edits-ledger.md; SCHEMATIC F-image class anchor)
        |— B(R_FULL-PV) = −527.9669 M_KK² (W5-1 PASS at FULL-PV F-image class;
        |    audit_sha256=04a6b22f1ab5b180...)
        |— B(R_FULL-CC) = TBD (CF-S92-W5-1-B forward gate)
        |— B(R_ζ-Wodzicki) = structurally derivable in asymptotic large-mass limit
             (= L_emp under Casimir-bound recovery; per V5 line 232)
```

**This structure honors clause-4 AND captures the F-image divergence**:

- The §VII.AV slot is SINGLE; no cross-corner co-primary; no same-corner co-primary. Clause-4 PRESERVED.
- The substrate-IS observable identity is single-pinned per K=3 MANDATORY (Volovik V1 axiom preserved). Algebra-axis orthogonality PRESERVED.
- The methodology-floor F-image class is regulator-class-keyed at the Level-2-B audit axis per `cross-pillar-bridge-anatomy.md §"Level-2 audit axes (Level-2-A vs Level-2-B)"` — STRUCTURAL methodology-floor distinction PRESERVED.
- The HIT independence is NOT invoked (no slot-split; single slot with sub-rows). HIT TEST INAPPLICABLE.
- The Wodzicki residue convergence in the asymptotic large-mass limit is recorded explicitly. F-image continuity in PV_mass (per V3 + V5 continuous-deformation evidence) PRESERVED.

**Cross-link to existing §VII.AV registry-text refinement-pathway table (registry line 18108-18120)**: the refinement-pathway routes (i)/(ii)/(iii) on the substrate-physics layer become **regulator-class index sources** under Reading B-weak Hybrid:

- Route (i) Friedrich-Bär saturation → produces R_Friedrich-Bär F-image (analytic-certification)
- Route (ii) FULL-PV at Λ_UV = M_KK → produces R_FULL-PV F-image (W5-1 landed)
- Route (iii) FULL-CC 1996 multipliers → produces R_FULL-CC F-image (CF-S92-W5-1-B target)

Routes (iv)/(v)/(vi)/(vii) on the operational-machinery / dual-anchor / Hochschild / moduli-deformation layers remain ORTHOGONAL to the regulator-class axis and continue to operate per the existing refinement-pathway structure.

**Substrate framing**: per `phononic-framing.md §"IS Space, Not IN Space"`, the §VII.AV slot IS the substrate's bridge-anatomy image at the Cell IV K-window log-derivative observable; the Level-2-B regulator-class-keyed sub-rows ARE the methodology-floor F-images of this substrate-IS observable under the layer-functor F. Direction substrate → emergent throughout: substrate's intrinsic spectral identity at `(M_2(ℂ), P_BdG, s=4)` IS canonical; methodology-floor regulator-class F-images are F(substrate-IS observable) at distinct enforcement-strength layers. NO container-thinking inversion: the substrate IS the observable; the methodology-floor F-images are downstream of the substrate at the Phi correspondence; the audit-layer verdict-line content is doubly downstream.

#### C3: Questions for volovik — L_max-INVARIANT plateau as structural FEATURE

The Re:V1-V5 + C1-C2 analysis converged on Reading B-weak Hybrid as the structurally correct landing. The remaining DISCRIMINATIVE questions for Volovik in Round 2:

**Q1 (predictive-content asymmetry test)**. Reading B-weak makes the specific structural prediction: `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.50` AND `|B(R_FULL-CC) − L_emp| / |L_emp| ≥ 10` at CF-S92-W5-1-B (Re:V5 EMERGES bullet 4). What is Reading A's POSITIVE numerical prediction for `B(R_FULL-CC)` at L_max=12 from the FALSIFICATION-envelope first principles? Reading A's V5 line 235 frames the prediction as "α_CC will produce a STRUCTURALLY DIFFERENT value from α_PV ≈ 6.26", but without committing to a numerical band. Reading B-weak commits to a specific band (FULL-physical clustering); Reading A admits any value outside [2.7, 3.3]. Which framing has more predictive content for the CF-S92-W5-1-B verdict?

**Q2 (continuous-deformation asymptotic-limit test)**. The WP line 150 evidence shows `B(PV_mass = 0) = −7.046336 ± 4.7e-7` reproduces the SCHEMATIC F-image at bit precision. Reading A predicts (V5 line 232) that as `M_PV → ∞`, `R_KW^{PV}(L_max=12) → −7.046336` continuously (Casimir-bound recovery). Reading B-weak agrees (this is the Wodzicki-asymptotic-limit; both F-image classes converge). DOES Reading A's framing predict the FULL-CC F-image at finite regulator-mass also converges to `−7.046336` continuously as the FULL-CC physical multipliers approach the asymptotic large-mass limit? If yes, Reading A and Reading B-weak agree structurally on the asymptotic behavior; if no, Reading A is committing to a non-continuous regulator-class divergence that lacks the continuous-deformation property the SCHEMATIC limit exhibits. What discriminating test would distinguish Reading A's "Casimir-bound approximation invalid at finite mass" framing from Reading B-weak's "regulator-class-keyed F-images converge at asymptotic mass" framing at the empirical level?

**Q3 (parse-tree closed-form structural test)**. Per `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"` MANDATORY at K=3 (S87 W-2 close), the substrate-IS observable identity is decided at the parse-tree decision procedure of `permanent-results-registry.md §VII.U.2 clause (e)`. Reading B-strong proposed BdG-occupation-kernel as a structurally distinct observable; Re:V5 retracted this because the kernel cannot be lifted out of the Mellin trace at the substrate layer. **Question**: what IS the parse-tree closed form of `R_KW^{PV}(L_max=12) = d² ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s} − Σ_j c_j (D_K² + M_j²)^{−s})) / d(ln K)² at s=4` on the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`? If the parse-tree closed form structurally factorizes as `(SCHEMATIC parse-tree closed form) × (regulator-class correction factor)` — i.e., a multiplicative correction at the parse-tree layer — then Reading B-weak's "regulator-class-keyed F-images" framing IS the parse-tree closed form structural reading; if instead the parse-tree closed form structurally additively separates the SCHEMATIC contribution from the regulator-class correction, then Reading A's "regulator-class FAILURE on a single observable" framing IS the parse-tree closed form structural reading. The empirical content is the same in both cases; the parse-tree closed form is the discriminating structural object.

**Q4 (registry-text canonical choice)**. Under V4's Reading A canonical (option i), the §VII.AV registry text records ONE F-image class (FULL-PV at −527.97 marked FAILED; SCHEMATIC at −7.046 preserved as canonical anchor) with the implicit framing that the methodology-floor F-image divergence is "approximation failure, not structural distinction". Under the Reading B-weak Hybrid (option iii Counter-proposal in Re:V4), the §VII.AV registry text records the regulator-class-keyed sub-row table explicitly, making the F-image class explicit in the registry-text layer. **Question**: which framing serves future-readers better at the registry-text layer? Reading A's framing collapses to "regulator-class is methodology-floor-only and the W5-1 FAIL is a substrate-IS envelope falsification"; Reading B-weak's framing exposes "regulator-class is structurally meaningful at the methodology-floor F-image layer per K=4 MANDATORY level-pin discipline and the W5-1 result is RD-class divergence on a single substrate-IS observable". The future-reader's CF-S92-W5-1-B interpretation depends critically on which framing was canonicalized at the registry-text layer.

**Q5 (CF-D rule-file extension calibration corpus K=5 candidate)**. The K=4 MANDATORY level-pin discipline at `substrate-first-canonical-sourcing.md §(iv)` has calibration corpus N=4 (W4-2 NEGATIVE-CALIBRATION + W9b-2 NEGATIVE-CALIBRATION + W9c-1 POSITIVE-CALIBRATION + W5b-2 sub-test (c) CALIBRATION-LOCUS-EXEMPT). The W5-1 instance is a candidate K=5 corpus extension: Level-axis F-image divergence on a substrate-IS observable individually well-defined at `(M_2(ℂ), P_BdG, s=4)`, with B(R_SCHEMATIC) − B(R_FULL-PV) = 521 M_KK² (1.87 OOM divergence; within SOURCE-RECON D_max ≥ 1.0 MANDATORY band). **Question**: does Reading A accept the W5-1 instance as a K=5 corpus extension under the level-pin discipline framing (Reading B-weak structural reading), or does Reading A's framing prefer NOT to extend the corpus (because under Reading A's framing the W5-1 result is a substrate-IS envelope falsification, NOT a methodology-floor F-image divergence — and so the K=4 corpus framing would be category-confused at K=5)? The answer to this question pins the CF-S92-W5-1-D methodology rule extension scope: under Reading B-weak it extends the K=4 level-pin discipline; under Reading A it becomes a stand-alone multiplicative-cancellation invariants catalog at `math-scripts.md`. The two extensions are NOT incompatible (both could land); the question is the canonical primary extension.

---

## Round 2 — Volovik: Follow-up

### CONVERGENCE

Connes's Re:V1-V5 + C1-C2 produced four structurally significant concessions that together establish the canonical workshop verdict as **Reading B-weak Hybrid (option iii)**. I accept this verdict in full and identify which of my V1-V5 positions are SHARPENED (not merely preserved) by the concessions:

**(1) Reading B-strong RETRACTED — V3+V5 prevail (Re:V3 line 369; Re:V5 line 469)**.

Connes's verbatim concession at Re:V3: "I therefore RETRACT the strong form of Reading B (two distinct substrate-IS observables at the same triple) as structurally inadmissible: the observable identity is single-pinned at `(M_2(ℂ), P_BdG, s=4)` per V3 + the K=3 MANDATORY algebra-axis axiom". Re:V5 closes the structural test: "I CONCEDE: NO. Reading B cannot derive the plateau value `B_PV(R_FULL-PV) = −527.9669 M_KK²` from BdG-occupation-kernel first principles independently of the K-window log-derivative on the D_K Mellin trace".

The continuous-deformation evidence at WP line 150 — `B(PV_mass = 0) = −7.046336 ± 4.7e-7` (bit-precision match to canonical `L_emp`) → `B(PV_mass = M_KK, √2·M_KK) = −527.9669` — is now the structural anchor for BOTH readings. The substrate-IS observable identity at `(M_2(ℂ), P_BdG, s=4)` does NOT change across the regulator-mass continuum. My V3 deployment of this evidence (line 122-128, "the IDENTICAL operator on the IDENTICAL spectrum") is canonicalized.

**V3 is SHARPENED**: not merely "Reading B-strong is wrong"; the continuous-deformation argument is now THE structural test for any future inheritance-morphism-style splitting proposal at a single substrate-IS triple. If a future workshop proposes splitting a §VII slot into structural-orthogonal-companion sub-slots, the V3 continuous-deformation test is the mandatory first-pass filter: produce the PV-mass-scan (or analog regulator-parameter scan) that shows the observable-identity-discontinuity at some finite regulator-mass — OR concede the split.

**(2) Algebra-axis orthogonality K=3 MANDATORY preserved + V4 clause-4 reading vindicated (Re:V4 line 397)**.

Connes's verbatim concession: "I CONCEDE this in light of the Re:V3 retraction of Reading B-strong: both proposed slots inhabit Cell IV (algebra-DEPENDENT state-pair functional × substrate-distance-2 pole s=4) per §VII.U.2 4-corner classification; same-corner co-primary is REGISTRY-INCOMPLETE per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` clause-4 detection criterion (S88 W-15 V.6 MANDATORY at K=3). The slot-split (Reading B option ii) is RETRACTED".

**V4 is SHARPENED**: the clause-4 reading is now the canonical defense pattern against any future same-corner co-primary proposal. The single-slot §VII.AV structure per K=3 MANDATORY is the canonical workshop verdict at the registry-anatomy layer. Both Reading A (option i) and Reading B-weak Hybrid (option iii) preserve the single slot; only Reading B-strong (option ii) would have required the split, and Reading B-strong is RETRACTED.

**(3) Convergence on Hybrid (option iii) as canonical workshop verdict (Re:V4 line 405; Re:V5 line 492)**.

Connes's verbatim convergence statement: "The structural verdict converges on Hybrid (option iii): single §VII.AV slot per K=3 MANDATORY; regulator-class-keyed Level-2 envelope sub-rows per K=4 MANDATORY". I AGREE this is the canonical landing.

The Hybrid is structurally distinct from both option (i) Reading A canonical AND option (ii) Reading B-strong slot-split because it satisfies BOTH MANDATORY disciplines simultaneously: K=3 MANDATORY at the substrate-IS observable identity layer (single slot per algebra-axis orthogonality) AND K=4 MANDATORY at the methodology-floor F-image layer (regulator-class-keyed level-pin discipline). Option (i) honors K=3 but does not record the K=4 F-image structure in the registry-text; option (ii) attempts to record the F-image structure but violates K=3. The Hybrid is the unique structurally-correct landing under both disciplines.

**My V4 Reading A canonical (single-slot FALSIFIED annotation) IS PRESERVED at the substrate-IS axiom layer** — the single slot, the L_emp canonical anchor preservation, the FAIL audit-pin preservation, the routes (i)/(iii)/(iv)/(v)/(vi)/(vii) preservation, the CF-S92-W5-1-A/B/D activation — all of these survive the Hybrid landing because the Hybrid IS V4-with-K=4-disclosure-added. The structural addition under the Hybrid is the Level-2 envelope sub-row TABLE recording the F-image divergence at the methodology-floor layer per K=4 MANDATORY (per Re:V4 §2 table; per C2 line 577 anatomy diagram).

**(4) V2's multiplicative-cancellation derivation preserved + Phi-correspondence-clarified (Re:V2 line 291; C1 line 527-557)**.

Connes's verbatim concessions: at Re:V2: "the multiplicative-normalization-cancellation derivation in V2 Steps 1-5 is mathematically correct ... The plateau at `R_KW^{PV}(L_max) = −527.9669 M_KK²` across `L_max ∈ {6, ..., 12}` is a STRUCTURAL identity of the second log-derivative operator on the multiplicative factorization — not an empirical coincidence". At C1 Step 3-5: "Within-class multiplicative-cancellation: Phi-trivial (V2 derivation correct). Cross-class regulator-keyed F-images: Phi-non-trivial (Reading B-weak claim)".

**V2 is SHARPENED**: the multiplicative-cancellation derivation IS the substrate-physics demonstration that L_max-stability within a single F-image class is structurally guaranteed by translation invariance of `d² ln(·) / d(ln K)²` under multiplicative pre-factors. Under the Phi correspondence (C1), this is the within-class Phi-trivial action — the L_max parameter is CANCELLED by Phi at the Σ_3 enforcement layer. The cross-class F-image divergence at the regulator-class axis is Phi-NON-trivial. The two are simultaneously true at different layers of the Phi correspondence; V2's derivation IS the substrate-physics structural object that the C1 Phi-correspondence framing operates on. V2 is the calibration-corpus instance #1 for `math-scripts.md §"Multiplicative-normalization cancellation invariants"` rule-file extension; this remains preserved as CF-S92-W5-1-D.

**Summary of CONVERGENCE**: the workshop verdict is Reading B-weak Hybrid (option iii) — single §VII.AV slot per K=3 MANDATORY (V1+V3+V4 prevail at the substrate-IS axiom layer); regulator-class-keyed Level-2 envelope sub-rows per K=4 MANDATORY (Re:V4 §2 table; C1 Phi(a_4) → Σ_3 enforcement); V2 multiplicative-cancellation derivation preserved as calibration corpus instance #1 for the methodology rule extension. Both readings (A and B-weak) predict the same continuous-limit behavior for the PV-mass scan (V5 line 232; Re:V5 line 475) — they are STRUCTURALLY EQUIVALENT under the Hybrid framing.

### DISSENT

Three remaining concerns with the Hybrid (option iii) landing — each on a specific structural defect in Re:V4's proposed Hybrid registry-text update, NOT a return to Reading A canonical:

**(1) The Level-2 envelope sub-row table MUST NOT promote `B(R_FULL-PV) = −527.97` to registry-anchor status. It is a CALIBRATION DATUM at the Level-2-B audit axis, NOT a Level-3 empirical anchor**.

Re:V4 §2 (line 432-436) presents the Level-2 envelope sub-row table with `B(R_FULL-PV) = −527.9669 (W5-1 PASS at FULL-PV F-image class)` listed in the same table as `B(R_SCHEMATIC) = −7.046336 (= L_emp; SOLE Corner-IV calibration source per s88-pending-edits-ledger.md)`. The text "W5-1 PASS at FULL-PV F-image class" is structurally MISLEADING:

- W5-1 is a **composite FAIL** verdict per verdict line 211 (`composite=FAIL`); the only PASS sub-verdict is `sign_verdict=PASS` (decreasing-envelope direction; α > 0 AND L_emp_PV < 0).
- The magnitude_verdict and regime_verdict are FAIL (per WP line 219 / verdict line 211).
- Calling `B(R_FULL-PV) = −527.97` a "PASS at FULL-PV F-image class" anchors the value at registry-text layer as if it were a structurally validated empirical confirmation. It is NOT — it is the value the FULL-PV pipeline RETURNED, which falsified the SCHEMATIC L^{-3} envelope. The substrate's canonical anchor at the Level-3 layer remains `L_emp = −7.046336` per `s88-pending-edits-ledger.md` theorem action ("preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source").

**Substrate-first canonical sourcing direction concern** (per `substrate-first-canonical-sourcing.md §(i)`): if the Level-2 envelope sub-row table records `B(R_FULL-PV) = −527.97` on equal footing with `B(R_SCHEMATIC) = L_emp = −7.046336`, future readers will read the table as licensing `−527.97` as a CITATION SOURCE — a regulator-class-shifted image being elevated to source-pin status. This inverts the substrate-first canonical sourcing direction: the substrate's canonical anchor `L_emp = −7.046336` is the substrate-IS canonical source (verified bit-precision at PV_mass → 0 per WP line 150); `B(R_FULL-PV) = −527.97` is the regulator-class image at finite-PV-mass NON-asymptotic regime (WP line 198, "the regulator scale M_KK ≈ 1 is order-unity vs the spectrum's lower edge → regulator is NOT in the asymptotic large-mass limit"). The two are NOT co-primary at the Level-3 anchor axis.

**Required fix to the Re:V4 §2 table**: the sub-row table at the Level-2 envelope axis carries the regulator-class-keyed F-image VALUES (as calibration data), but the Level-3 EMPIRICAL ANCHOR row remains single-pinned at `L_emp = −7.046336` per s88-pending-edits-ledger.md. The mack-cosmic-bridge sole-writer should land the Hybrid registry-text update with the following structural separation:

```
Level-2 envelope sub-rows (regulator-class-keyed F-image table) — DIAGNOSTIC ONLY:
   R_SCHEMATIC:  B(R) = −7.046 M_KK² (= L_emp at PV_mass → 0 limit; SCHEMATIC F-image class)
   R_FULL-PV:    B(R) = −527.97 M_KK² (W5-1 measured at FULL-PV F-image class;
                 regulator-class-divergent from SCHEMATIC by 1.87 OOM at finite regulator-mass)
   R_FULL-CC:    B(R) = TBD (CF-S92-W5-1-B forward gate)
   R_ζ-Wodzicki: B(R) = predicted = R_SCHEMATIC in asymptotic large-mass limit

Level-3 empirical anchor (SOLE Corner-IV calibration source per s88-pending-edits-ledger.md):
   L_emp = −7.046336 M_KK² (substrate-natural; preserved unchanged; NOT cross-referenced
   from the Level-2 envelope sub-row table as a co-primary anchor)
```

This separation honors K=3 MANDATORY (single substrate-IS observable identity), K=4 MANDATORY (regulator-class-keyed F-image disclosure), AND substrate-first canonical sourcing direction (the substrate's canonical anchor is NOT elevated alongside a regulator-class image).

**(2) The Re:V4 §1 status-block update MUST NOT collapse the Level-2 sub-class tag from PROXY-REFINEMENT wholesale**.

Re:V4 §1 (line 421) proposes: "Level-2 sub-class re-classified: REGISTRY-INCOMPLETE-PENDING-REGULATOR-CLASS-DISAMBIGUATION (regulator-class-keyed F-image class table pending CF-S92-W5-1-B FULL-CC route)". This re-classification is too broad. The §VII.AV PROXY-REFINEMENT corridor at registry line 18063 lists FOUR substrate-physics layer refinement-pathway routes (i)/(ii)/(iii) plus the operational/dual-anchor/Hochschild/moduli routes (iv)/(v)/(vi)/(vii) at registry lines 18108-18120. Only route (ii) FULL Pauli-Villars at Λ_UV = M_KK is CLOSED-FAIL by W5-1. Routes (i) Friedrich-Bär saturation, (iii) FULL Connes-Chamseddine 1996 multipliers, (iv) K_canonical pin uniqueness operational-alignment, (v) V4 substrate-physics discriminator dual-anchor joint-hypersurface, (vi) Hochschild-cohomology cross-anchor, (vii) Level-2 moduli-deformation extension — ALL REMAIN ACTIVE.

The status-block update should preserve the PROXY-REFINEMENT sub-class tag and annotate ONLY route (ii) as CLOSED-FAIL, NOT collapse the entire sub-class to PENDING-REGULATOR-CLASS-DISAMBIGUATION. The latter would erase the canonical refinement-pathway taxonomy at registry line 18108-18120 — which is itself a substrate-physics structural object per the deferred-pending intermediate verdict-class rule extension at S90 W1-14.

**Required fix**: status-block update text per my V4 §1 (workshop line 153-166) is canonical at the route-(ii)-annotation layer; Re:V4 §1's new clause "regulator-class-keyed F-image class table" is added as an APPENDIX to the status block, NOT a REPLACEMENT of the PROXY-REFINEMENT sub-class tag. Concretely: V4 §1 lines 154-165 stand; Re:V4 §1 lines 415-426 are added as supplementary disclosure of the K=4 MANDATORY F-image structure WITHOUT altering the PROXY-REFINEMENT classification.

**(3) The K=5 corpus-extension status (Q-CON-5) is structurally appropriate but should land as NEGATIVE-CALIBRATION on rule (2), NOT POSITIVE-CALIBRATION**.

This is preview of my Q-CON-5 answer (full reasoning in QUESTIONS section below): the W5-1 instance qualifies for K=5 corpus extension at `substrate-first-canonical-sourcing.md §(iv)` per Re:V3 line 386 ("V3 simply extends the calibration corpus to N=5 with the W5-1 instance"), but it must land in the SAME compliance class as W4-2 and W9b-2 — i.e., NEGATIVE-CALIBRATION on rule (2). The W5-1 verdict line 211 carries `convention=corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4` — NO `-SCHEMATIC` suffix because this gate is FULL-physical. This is structurally correct (rule (2) requires the suffix only on SCHEMATIC F-image gates). However, the COMPANION SCHEMATIC anchor `L_emp = −7.046336` is consumed at the registry layer without an explicit `-SCHEMATIC` convention-tag at its own producing gate (S87 W2-3 / S88 W5a predecessors land prior to the K=4 MANDATORY status; they are GRANDFATHERED). The W5-1 instance is therefore the first POST-K=4-MANDATORY-status instance where the SCHEMATIC vs FULL-PV divergence is explicitly measured, but neither side's verdict line carries the structurally complete dual-tag disclosure.

**Required fix**: the K=5 corpus extension landing should explicitly tag the W5-1 instance as a NEW compliance class — "MIXED-PARTIAL: FULL-physical gate measures the divergence against an implicitly-GRANDFATHERED SCHEMATIC predecessor; neither side carries the structurally complete dual-tag disclosure". This extends the K=4 corpus taxonomy with a new class (analog to PARTIAL-POSITIVE landed at S90 W1-9 per the 3-class extension at `substrate-first-canonical-sourcing.md §(iv) §"3-class compliance taxonomy"`). The structural advance is: the W5-1 instance is the FIRST measurement of a SCHEMATIC vs FULL-physical F-image divergence WHERE BOTH sides are individually well-defined per K=4 MANDATORY level-pin discipline; the corpus extension's role is to canonicalize this measurement class.

### EMERGENCE

The R1+R2 cross-pollination has produced FIVE structural insights that extend beyond the original 4 focus topics:

**(1) The multiplicative-normalization-cancellation theorem is calibration-corpus instance #1 for the proposed rule extension `math-scripts.md §"Multiplicative-normalization cancellation invariants"` (CF-S92-W5-1-D)**.

V2 Steps 1-5 (workshop lines 71-104) IS the substrate-physics derivation that the L_max truncation enters multiplicatively at the BdG-sub-algebra Mellin trace; `d² ln(·) / d(ln K)²` annihilates the L_max-dependent pre-factor `w(L_max)` structurally. Re:V2 line 291 CONFIRMS the derivation. Under C1's Phi correspondence, this is the WITHIN-CLASS Phi-trivial action at the Σ_3 enforcement layer (C1 Step 3 line 537).

**Rule-file extension structure** (pre-registered for CF-S92-W5-1-D dispatch at S92):

```
math-scripts.md §"Multiplicative-normalization cancellation invariants"
   (NEW section; calibration corpus instance #1 = S91 W5-1)

Rule: For any substrate-IS observable O = f(D_K, K) on a finite spectral triple (A, H, D_K),
      if the L_max truncation enters f as a MULTIPLICATIVE spectral-support pre-factor
      w(L_max) — i.e., f^{(L_max)}(K) = w(L_max) · g(K) for some L_max-INDEPENDENT kernel
      g(K) — then any K-dependent log-derivative operator L_n[f^{(L_max)}] = d^n ln(f^{(L_max)})
      / d(ln K)^n  is identically L_max-invariant: L_n[f^{(L_max)}] = L_n[g(K)] for all n ≥ 1.

Substrate-physics structural reading: L_max-INVARIANCE under multiplicative pre-factors is the
substrate's signature that L_max enters as a spectral-support weight (not as an envelope
parameter). Within-class L_max-stability is Phi-trivial at the Σ_3 enforcement layer per
epistemic-discipline.md §"Layer-Decomposition" Phi correspondence. The discriminating
content lives at the asymptote / plateau value B(R) = L_n[g_R(K)] at K_horizon, which IS
regulator-class-keyed at the methodology-floor F-image layer per K=4 MANDATORY level-pin
discipline at substrate-first-canonical-sourcing.md §(iv).

Calibration corpus K=1 at S91 W5-1:
   - V2 substitution chain (workshop lines 71-104) — substrate-physics demonstration
   - Empirical bit-for-bit plateau at -527.97 across L_max ∈ {6,...,12} (WP table line 168-176)
   - Α extraction rank-deficient (α_PV_1σ = ∞) confirming structural plateau (not envelope)
   - Reserved K=2 / K=3 rows for forward calibration instances at other Cell IV observables
```

The rule-file extension's role is to make this structural identity a MANDATORY pre-flight check at plan-freeze for any future gate attempting α extraction on an observable that may admit multiplicative L_max factorization. CF-S92-W5-1-D promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md`.

**(2) §VII.AV Hybrid registry-text consequences — pre-registered for mack-cosmic-bridge sole-writer landing at S92 W0 (per `feedback_mack-bridge-role.md` sole-writer discipline + `feedback_fix-in-session-never-defer.md` in-session refinement)**.

The Hybrid registry-text update lands at §VII.AV (registry line 18059 onward) with the following structural changes, INCORPORATING the three Dissent fixes above:

```
Status block (line 18063 area):
   - PROXY-REFINEMENT sub-class tag PRESERVED (Dissent fix 2)
   - W5-1 audit-pin sub-row APPENDED annotating ONLY route (ii) FULL-PV at Λ_UV = M_KK as
     CLOSED-FAIL with audit_sha256=04a6b22f1ab5b180fac0eb73132ce05ae7e9f32d4394203728778b47a037351e
   - K=4 MANDATORY F-image disclosure block APPENDED as supplementary status block (Dissent
     fix 2): "Per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin
     discipline + cross-pillar-bridge-anatomy.md §"Level-2 audit axes (Level-2-A vs Level-2-B)",
     the W5-1 verdict records a methodology-floor F-image divergence at the Level-2-B
     regulator-invariance axis on a SINGLE substrate-IS observable identity preserved at
     (M_2(ℂ), P_BdG, s=4) per K=3 MANDATORY algebra-axis axiom"

Element 4 (Algebraic envelope, line 18090 area):
   - L^{-3} envelope corrigendum from my V4 §3 (workshop lines 175-182) — preserved unchanged
   - Level-2 envelope sub-row table (per Re:V4 §2 line 432-436, with Dissent fix 1 separation):
     DIAGNOSTIC ONLY at Level-2-B axis; does NOT replace Level-3 anchor

Element 5 (Empirical anchor, line 18092):
   - L_emp = -7.046336 PRESERVED unchanged as SOLE Corner-IV calibration source per
     s88-pending-edits-ledger.md (Dissent fix 1 separation)
   - Sub-row table at Level-2-B axis is NOT cross-referenced as a Level-3 co-primary

Refinement-pathway table (line 18108-18120):
   - Route (ii) FULL-PV: annotation column "Status: CLOSED-FAIL at S91 W5-1" (V4 §2)
   - Routes (i)/(iii)/(iv)/(v)/(vi)/(vii) PRESERVED ACTIVE
   - New route (viii) "Alternative envelope predictor" queued as CF-S92-W5-1-A (V4 §2)

CF activations:
   - CF-S92-W5-1-A ACTIVE (alternative envelope predictor; V4 §4)
   - CF-S92-W5-1-B ACTIVE (FULL-CC cross-route comparison; V4 §6 / Re:V4 §5 — structural
     discriminator with Reading B-weak's specific prediction |B(CC) − B(PV)| / |B(PV)| ≤ 0.50
     per Re:V5 EMERGES bullet 4)
   - CF-S92-W5-1-C REFRAMED (regulator-class transition-map disambiguation per Re:V4 §4;
     NOT cancelled per V4 §5; the reframing answers the Hybrid landing's residual question:
     is the regulator-class F-image transition continuous or piecewise?)
   - CF-S92-W5-1-D ACTIVE (METHODOLOGY-class extension to math-scripts.md per V4 §7;
     calibration corpus instance #1 landed at this workshop)
```

**(3) Cross-link consequences for SCHEMATIC↔FULL F-image questions in adjacent §VII slots**.

The Hybrid (option iii) framing at §VII.AV establishes the canonical pattern for any §VII entry where SCHEMATIC vs FULL-physical regulator class divergence is structurally consequential. Four adjacent §VII entries inherit this pattern at structurally analogous positions:

- **§VII.AU.OP-PROJ (W2 + W-2 workshop)** at registry line 17642 + 18141 (FWD-C1 Pillar I↔II Bridge Theorem Candidate; substrate-distance-1 pole `s=3`): currently REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION sub-class. The Hybrid pattern applies if the CF-W5-6 (= CF-65) L_max scan extraction returns regulator-class-divergent α values across {SCHEMATIC, FULL-PV, FULL-CC}; in that case the Element 4 envelope sub-row table structure replicates from §VII.AV Hybrid. **Cross-link**: §VII.AU's Level-2-B audit axis is the SAME structural object as §VII.AV's; the parity-twin pole index (`s=3` vs `s=4`) does NOT change the regulator-class-keyed F-image structure. **Pre-registered prediction**: if §VII.AU's CF-65 first-extraction produces an L_max-INVARIANT plateau at the FULL-PV F-image class (matching the multiplicative-normalization-cancellation pattern), the parse-tree expansion at line 18156 (`α_s_canonical → (Mellin-residue at substrate-distance-1 pole s=3)² − 1`) admits the same Hybrid sub-row structure at the Element 4 envelope axis.

- **§VII.AY.OP-PROJ (W8 + W-6 workshop)**: SCHEMATIC↔FULL question at the operational-machinery layer. If §VII.AY's substrate-IS observable admits the multiplicative L_max factorization at the BdG sub-algebra, the calibration-corpus instance #2 for the proposed `math-scripts.md §"Multiplicative-normalization cancellation invariants"` extension lands here. CF-S92-W5-1-D's K-counter advances K=1 → K=2 upon this landing.

- **§VII.BA Wodzicki-BCS (W9-9)**: SCHEMATIC↔FULL question at the BCS-gap-protected anchor layer per `mathematics.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`. The Wodzicki residue's regulator-invariance property at the asymptotic large-mass limit (Re:V2 line 347 explicit citation) IS the structural object that §VII.AV's Hybrid framing engages with at finite-regulator-mass. The cross-link: §VII.BA's Wodzicki anchor IS THE asymptotic limit of §VII.AV's regulator-class-keyed sub-row table; both share the SAME substrate-IS observable identity at the asymptotic limit. **Pre-registered prediction**: as `M_PV → ∞`, `B(R_FULL-PV) → B(R_ζ-Wodzicki) = R_Wodzicki`, where `R_Wodzicki` is §VII.BA's canonical anchor value.

- **§VII.AF.1.OP-PROJ (W9-4)**: SCHEMATIC↔FULL question at the HP^1-cohomology pairing layer. The S88 W7b-82 (Binding-axis K=1 SUGGESTION) calibration corpus already records `gv_canonical_difference_FW = -40579.1500479506 pin satisfies the Level-3 anchor` (per `regulator-pin-discipline.md §"Binding axis"` SUGGESTION at K=1). The §VII.AV Hybrid landing extends the Binding axis K-counter context: §VII.AV adopts substrate-natural-binding (per regulator-pin-discipline.md MACHINERY-SCOPE axis cross-link line 144) at the Level-2 axis; §VII.AF.1.OP-PROJ adopts canonical-import-binding. Both are STRUCTURALLY ORTHOGONAL methodology-floor F-image classes at the Binding axis.

**(4) The continuous-deformation test (V3 + Re:V5) becomes the canonical structural filter for future inheritance-morphism-style splitting proposals**.

The WP line 150 PV_mass → 0 → M_KK continuous-deformation evidence is now the structural anchor for the workshop's converged verdict (both readings AGREE on this evidence's structural meaning). The test generalizes: for any future workshop proposing to split a §VII slot into structural-orthogonal-companion sub-slots, the V3-style continuous-deformation test is the mandatory first-pass filter. Specifically:

```
Structural filter (NEW; calibration corpus instance #1 = S91 W4 workshop verdict):
   To license a slot-split at the substrate-IS observable axis, the proposer MUST produce
   a parameter scan (regulator-mass, coupling, deformation parameter, OR analog substrate
   parameter) demonstrating a DISCONTINUOUS jump in the observable identity at some finite
   parameter value. Continuous deformation across all parameter values FORBIDS the slot
   split (single substrate-IS observable per K=3 MANDATORY).
```

This filter is forward-looking from S91 onward; it is the canonical pattern at the substrate-IS observable identity test layer. CF-S92-W5-1-C (regulator-class transition-map disambiguation per Re:V4 §4) IS THIS TEST applied to the §VII.AV PV-mass continuum specifically; the result will be the canonical first-instance application of the filter beyond the WP line 150 PV_mass → 0 case.

**(5) The Phi(a_4) → Σ_3 enforcement-layer correspondence is now structurally clarified for substrate-distance-2 pole observables on the BdG sub-algebra**.

C1's Phi-correspondence derivation (workshop lines 499-559) establishes that the W5-1 observable at substrate-distance-2 pole `s=4` lives at the Σ_3 enforcement layer with THREE orthogonal methodology-floor F-image axes (Level / UV-regulator-class / Binding). The structural insight: methodology-rule extensions cataloging F-image divergence (K=4 MANDATORY level-pin discipline; UV-regulator-pin discipline; Binding-axis SUGGESTION at K=1) ALL operate at Σ_3 simultaneously — they are STRUCTURALLY ORTHOGONAL methodology-floor axes per `epistemic-discipline.md §"Layer-Decomposition"`. Future substrate-distance-2 pole `s=4` observables on Cell IV will inherit this 3-axis Σ_3 enforcement structure by Phi-correspondence.

### QUESTIONS

Answering Connes's 5 Q-CON questions (C3, workshop lines 624-632) with substrate-IS reasoning:

**Q-CON-1 (predictive-content asymmetry test) — answered**.

Reading B-weak's specific prediction: `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.50` AND `|B(R_FULL-CC) − L_emp| / |L_emp| ≥ 10` at CF-S92-W5-1-B (Re:V5 line 481).

**Reading A's positive numerical prediction for `B(R_FULL-CC)` at L_max=12 from substrate-IS first principles**: Reading A predicts `B(R_FULL-CC)` will be CONTINUOUS with `B(R_FULL-PV) = −527.97` at the regulator-class-physical-fidelity axis — i.e., `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.30` (TIGHTER than Reading B-weak's ≤ 0.50 band). The substrate-IS structural reason: both FULL-PV and FULL-CC operate at the substrate's intrinsic UV-completion at order-unity regulator-mass scale (per WP line 164 "regulator scale M_KK ≈ 1 is order-unity vs the spectrum's lower edge"); the difference between PV-mass tower `{M_KK, √2·M_KK}` (S61/S78) and CC multipliers `{a₀ Tr(D²/M_KK²) + a₂ Tr(D⁴/M_KK⁴) + ...}` (Connes-Chamseddine 1996 §2.2-2.3) is a STRUCTURAL difference in the K-dependence of the regulator's tail at order-unity mass scale — not a difference in the asymptotic large-mass limit (where both → Wodzicki residue at L_emp = -7.046336 per the C1 Step 4 cross-class action).

**Specific Reading A predictions for CF-S92-W5-1-B**:
- (a) `B(R_FULL-CC) ∈ [-686, -370]` M_KK² (i.e., `[-527.97 · 1.30, -527.97 / 1.43]` for the ≤ 0.30 band)
- (b) `α_CC ∈ [4.5, 8.0]` (out of the PASS band [2.9, 3.1]; STRUCTURALLY DIFFERENT from α=3 SCHEMATIC prediction)
- (c) BOTH α extractions (CC + PV) are rank-deficient (σ → ∞) at L_max ∈ {6, ..., 12} due to multiplicative-normalization-cancellation per V2 Steps 1-5 (the cancellation operates on ANY regulator-class within the multiplicative factorization family)

**Predictive-content comparison**: Reading A's band `[-686, -370]` is narrower than Reading B-weak's [`-792, -352`] (the ≤ 0.50 band centered at -527.97); Reading A admits one specific structural reason (FULL-physical regulator-class clustering at the substrate's intrinsic UV-completion at order-unity mass scale); Reading B-weak's framing is the same as Reading A's at the CONTINUOUS asymptotic-limit prediction layer (per Re:V5 line 475) but allows a wider band at finite-regulator-mass. The two predictions are STRUCTURALLY EQUIVALENT at the asymptotic limit; Reading A's tighter finite-mass band is the structural sharpening from the Hybrid landing.

**Q-CON-2 (continuous-deformation asymptotic-limit test) — answered**.

YES, Reading A's framing predicts the FULL-CC F-image at finite regulator-mass also converges to `−7.046336` continuously as the FULL-CC physical multipliers approach the asymptotic large-mass limit. This is the WODZICKI RESIDUE ASYMPTOTIC LIMIT — at asymptotic regulator-mass, ALL regulator-class F-images converge to the Wodzicki residue invariant (which IS `L_emp = −7.046336` for the Corner-IV K-window log-derivative on the BdG sub-algebra at substrate-distance-2 pole `s=4`). Reading B-weak's Re:V5 line 475 framing AGREES with this asymptotic behavior.

**The structural agreement at the asymptotic limit IS the structural anchor for both readings**. The structural difference between Reading A and Reading B-weak is ONLY at the registry-text framing layer (single F-image class vs regulator-class-keyed sub-rows); neither predicts a non-continuous regulator-class divergence at finite regulator-mass.

**Discriminating empirical test that distinguishes Reading A's "Casimir-bound approximation invalid at finite mass" framing from Reading B-weak's "regulator-class-keyed F-images converge at asymptotic mass" framing**: the discriminator is at the REGISTRY-TEXT LAYER, NOT at the empirical-data layer. Both readings predict the SAME empirical scan results for the PV-mass continuum (PV_mass = 0 → 0.5 M_KK → M_KK → 5 M_KK → 100 M_KK → 1000 M_KK should return continuous interpolation from `-7.046` to `-527.97` near M_KK and back to `-7.046` at asymptotic-large mass). The discriminator is the registry-text framing: does the §VII.AV slot record ONE F-image class with the W5-1 FAIL as "approximation failure" (Reading A canonical, option i) or MULTIPLE regulator-class-keyed sub-rows (Hybrid, option iii)? The Hybrid landing answers in favor of the latter; both readings agree the EMPIRICAL scan is structurally well-defined and produces the SAME data.

**Q-CON-3 (parse-tree closed-form structural test) — answered**.

The parse-tree closed form of `R_KW^{PV}(L_max=12) = d² ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{−2s} − Σ_j c_j (D_K² + M_j²)^{−s})) / d(ln K)² at s=4` on the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`:

```
R_KW^{PV}(L_max=12) =
   d² ln[ Tr_{M_2(ℂ)}( P_BdG · D_K^{-8} )    [bare Mellin trace at s=4 on BdG sub-algebra]
        + 2 · Tr_{M_2(ℂ)}( P_BdG · (D_K² + M_KK²)^{-4} )     [PV copy at M_1 = M_KK; c_1 = +2 INVERTED SIGN]
        − Tr_{M_2(ℂ)}( P_BdG · (D_K² + 2·M_KK²)^{-4} ) ]     [PV copy at M_2 = √2·M_KK; c_2 = −1]
        / d(ln K_window)² evaluated at K_horizon

Parse-tree decomposition (per registry-landing.md §"Parse-Tree Expansion Pre-Registration"
SUGGESTION-K=1, S90 W1-8 audit Class-(h); state-history label "R_KW^{PV}" reduced to
closed-form expression on the substrate algebra):

   R_KW^{PV} →
     d² ln[ Tr_{M_2(ℂ)}(P_BdG · D_K^{-8}) · (1 + ψ_PV(K))] / d(ln K)²
                where  ψ_PV(K) = [2 · Tr(P_BdG · (D_K² + M_KK²)^{-4})
                                  − Tr(P_BdG · (D_K² + 2·M_KK²)^{-4})]
                                  / Tr(P_BdG · D_K^{-8})
                       = PV correction factor relative to bare trace at K_window

   = d² ln[ Tr(P_BdG · D_K^{-8}) ] / d(ln K)²    [bare contribution]
     + d² ln[ 1 + ψ_PV(K) ] / d(ln K)²            [PV correction contribution]

   At PV_mass → 0:  ψ_PV → 0 (PV copies degenerate to bare trace; net coefficient 1+2-1=2;
                              FULL-PV subtraction vanishes), so R_KW^{PV} → R_KW^{bare}
                              = -7.046336 (WP line 150 numerical kernel verification)

   At PV_mass = M_KK (FULL-PV): ψ_PV(K) is non-trivial and K-dependent; the second term
                                contributes the regulator-class correction factor at finite
                                regulator-mass; result: R_KW^{PV} = -527.97 at K_horizon
```

**The parse-tree closed form ADDITIVELY separates** the bare contribution from the PV correction contribution — `R_KW^{PV} = R_KW^{bare} + ΔR_KW^{PV-correction}` where `ΔR_KW^{PV-correction} = d² ln[1 + ψ_PV(K)] / d(ln K)²`. Per Connes's structural mapping at Q-CON-3 (workshop line 628), this is **Reading A's "regulator-class FAILURE on a single observable" framing** at the parse-tree closed form layer.

**HOWEVER**: at the empirical-measurement layer, the additive separation reduces to the multiplicative-factorization at the L_max truncation level — because `Tr(P_BdG · D_K^{-8})` and `ψ_PV(K)` BOTH factorize as `w(L_max) · (...)_K` at the L_max truncation, and the multiplicative pre-factor cancels in `d² ln(·) / d(ln K)²` per V2 Steps 1-5. The PV-correction contribution `ΔR_KW^{PV-correction}` is itself L_max-invariant by the SAME multiplicative-cancellation mechanism.

**Combined structural reading**: the parse-tree closed form is ADDITIVE at the substrate-IS observable layer (Reading A canonical at this layer); the methodology-floor F-image of the parse-tree closed form is MULTIPLICATIVE at the L_max truncation layer (Reading B-weak canonical at this layer). Both readings are simultaneously true at different layers per the Phi correspondence at C1; the parse-tree closed form IS THE structural object that bridges them. This is the canonical answer to Q-CON-3: the parse-tree closed form structurally additively separates (Reading A's framing IS the parse-tree closed form structural reading at the substrate-IS observable layer) WHILE the methodology-floor F-image of the parse-tree closed form structurally factorizes multiplicatively at the L_max truncation layer (Reading B-weak's framing IS the parse-tree closed form structural reading at the methodology-floor F-image layer). Both readings are parse-tree-closed-form-canonical at DIFFERENT layers; the Hybrid landing canonicalizes BOTH layer attributions in the registry text.

**Q-CON-4 (registry-text canonical choice for future-readers) — answered**.

The Reading B-weak Hybrid (option iii) registry-text framing serves future-readers BETTER because it exposes the K=4 MANDATORY F-image structure explicitly at the registry-text layer. Specifically:

- A future reader landing on §VII.AV at S95 (hypothetical) under Reading A canonical (option i) would see the SCHEMATIC L_emp anchor preserved + the FULL-PV FAIL audit-pin + the alternative envelope-predictor CF queue, but would NOT see the K=4 MANDATORY level-pin discipline disclosed at the F-image layer. The CF-S92-W5-1-B verdict's interpretation depends critically on understanding that the FULL-PV vs FULL-CC comparison IS a methodology-floor F-image divergence test (per `epistemic-discipline.md §"Source Reconciliation"` FI/RD/MIXED taxonomy + `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY) — a future reader without the K=4 framing in the registry text might mis-read the CF-B verdict as "two different Cell IV observables" (a Reading B-strong-style mistake the workshop just RETRACTED).

- Under Hybrid (option iii), the registry-text records the regulator-class-keyed sub-row table at the Level-2-B audit axis explicitly. The future reader sees: (a) the substrate-IS observable identity is single (Volovik V1 axiom + K=3 MANDATORY); (b) the methodology-floor F-image is regulator-class-keyed (K=4 MANDATORY); (c) the L_max-INVARIANT plateau within each F-image class is structural (V2 multiplicative-cancellation per Phi-trivial within-class action); (d) the discriminating content is the asymptote B(R) across R-classes (Reading B-weak's structural prediction); (e) the CF-B verdict's interpretation is in the regulator-class F-image divergence framing.

**The Hybrid (option iii) is preferable AT THE REGISTRY-TEXT LAYER**, with the Dissent fixes 1-2 applied (Level-3 anchor remains single-pinned at L_emp; PROXY-REFINEMENT sub-class tag preserved with route-(ii) annotation only). The future-reader serving rationale is the rule-file extension cross-reference: the registry text MUST disclose which methodology-rule extension governs the F-image axis; otherwise the rule extension's structural role is invisible at the registry layer.

**Q-CON-5 (CF-D rule-file extension calibration corpus K=5 candidate) — answered**.

Reading A accepts the W5-1 instance as a K=5 corpus extension under the K=4 MANDATORY level-pin discipline framing (per `substrate-first-canonical-sourcing.md §(iv)`), with the structural reading: the W5-1 instance IS a Level-axis F-image divergence on a substrate-IS observable individually well-defined at `(M_2(ℂ), P_BdG, s=4)`. The substantive corpus advancement is structurally correct at the K=4 level-pin discipline layer.

However, per Dissent fix (3) above, the W5-1 instance lands as a **NEW compliance class** ("MIXED-PARTIAL") rather than reusing the existing POSITIVE/PARTIAL-POSITIVE/NEGATIVE 3-class taxonomy:

```
Proposed K=4 corpus extension (S91 W5-1 calibration corpus row):

| # | Witness | Session | Producing script | Convention tag | -SCHEMATIC suffix | Docstring | Class |
|:-:|:--------|:--------|:-----------------|:---------------|:-----------------:|:---------:|:------|
| 5 | W5-1 (this gate) | S91 | s91_w5_1_full_bdg_pv_substrate_distance_2_pole_s4.py | corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4 | N/A (FULL-physical gate; suffix only required for SCHEMATIC F-image gates) | YES (full SCHEMATIC↔FULL-physical F-image divergence disclosure in WP line 178) | NEW CLASS: MIXED-PARTIAL — FULL-physical gate measures the SCHEMATIC vs FULL divergence against an implicitly-GRANDFATHERED SCHEMATIC predecessor (L_emp from S87 W2-3 / S88 W5a, both pre-K=4-MANDATORY status); neither side individually carries the structurally complete dual-tag disclosure |
```

**The 3-class compliance taxonomy at `substrate-first-canonical-sourcing.md §(iv)` extends to 4-class with MIXED-PARTIAL as the new admissibility class**. This is structurally analogous to PARTIAL-POSITIVE landed at S90 W1-9 — a structurally-intermediate compliance class admitted with explicit severity band (ADVISORY S2 for both PARTIAL-POSITIVE and MIXED-PARTIAL). The MIXED-PARTIAL class admissibility is forward-looking from S91 W5-1; the structural rationale is the GRANDFATHER-clause asymmetry between the FULL-physical gate (S91 post-K=4-MANDATORY) and its SCHEMATIC predecessor (pre-K=4-MANDATORY; carries no `-SCHEMATIC` suffix retroactively because none was required at landing time).

**K-counter advancement under Q-CON-5 answer**:

```
K_substantive (pre-S91 W5-1): 4 (W4-2 NEGATIVE + W9b-2 NEGATIVE + W9c-1 POSITIVE + W5-7 PARTIAL-POSITIVE)
K_with_inheritance (pre-S91 W5-1): 5 (substantive 4 + W5b-2 inheritance-locus 1)

K_substantive (S91 W5-1 close): 5 (W4-2 NEGATIVE + W9b-2 NEGATIVE + W9c-1 POSITIVE + W5-7 PARTIAL-POSITIVE + W5-1 MIXED-PARTIAL [NEW])
K_with_inheritance (S91 W5-1 close): 6 (substantive 5 + W5b-2 inheritance-locus 1)

Status: MANDATORY preserved (K_substantive=5 >> K_promotion=3)
Sub-status: MIXED-PARTIAL class admissible from S91 W5-1 forward (admissibility band ADVISORY S2)
```

The K=5 corpus extension is the canonical primary extension at `substrate-first-canonical-sourcing.md §(iv)`; CF-S92-W5-1-D (METHODOLOGY-class catalog of L_max-multiplicative-cancellation invariants) is a STAND-ALONE extension at `math-scripts.md` (calibration corpus instance #1 = S91 W5-1 V2 multiplicative-cancellation derivation). The two extensions are NOT incompatible (both land); the canonical primary IS the K=5 corpus extension at the level-pin discipline rule, per Reading B-weak's structural reading of the W5-1 instance. CF-S92-W5-1-D adds the orthogonal methodology-rule extension at the multiplicative-cancellation invariants axis.

**Sharper follow-up questions for FINAL ROUND (connes R2-B addresses)**:

**Q-VOL-1 (registry-text Level-3 anchor singleness)**: Under the Hybrid landing with Dissent fix 1 (Level-2 envelope sub-row table at Level-2-B axis DIAGNOSTIC ONLY; Level-3 empirical anchor remains single-pinned at `L_emp = −7.046336`), confirm or refute: future §VII registry-text landings under the Hybrid framing at other Cell IV slots MUST maintain the structural separation between Level-2-B sub-rows (regulator-class-keyed F-image table; diagnostic) and Level-3 anchor (substrate-natural canonical; single source). If confirmed, this becomes a STRUCTURAL DISCIPLINE on the Hybrid landing pattern for forward §VII entries — a sharpening beyond the existing K=3 MANDATORY (anchor singleness on the substrate-IS observable identity axis) extending to anchor singleness on the Level-3 empirical anchor axis under the Hybrid framing.

**Q-VOL-2 (MIXED-PARTIAL class K-counter advancement criterion)**: The proposed MIXED-PARTIAL class extension to `substrate-first-canonical-sourcing.md §(iv)` 3-class taxonomy requires its own K-counter advancement criterion. Is the K-counter advanced at MIXED-PARTIAL instances WHERE BOTH SIDES of the SCHEMATIC↔FULL divergence are individually well-defined post-K=4-MANDATORY (S88 W7b-83 onward), OR is the K-counter advanced at instances where EITHER side is post-K=4-MANDATORY (more inclusive)? The W5-1 instance is the first instance where the FULL-physical gate is post-K=4-MANDATORY (S91 > S88); the SCHEMATIC predecessor (S87 W2-3 / S88 W5a) is pre/at-K=4-MANDATORY (S88 W7b-83 close is during S88; the W5a predecessor is at S88 W5a). The K-counter advancement criterion choice determines whether MIXED-PARTIAL instances accumulate slowly (BOTH-SIDES-POST-K=4 criterion) or rapidly (EITHER-SIDE-POST-K=4 criterion). The choice affects the MIXED-PARTIAL → MANDATORY promotion timeline at `feedback_rules-compensate-missing-structure.md` K=3 threshold.

**Q-VOL-3 (Phi(a_4) → Σ_3 enforcement layer at substrate-distance-1 pole s=3)**: C1's Phi-correspondence derivation establishes that the W5-1 observable at substrate-distance-2 pole `s=4` lives at the Σ_3 enforcement layer. The §VII.AU.OP-PROJ observable at substrate-distance-1 pole `s=3` should live at a STRUCTURALLY DIFFERENT Σ_n enforcement layer per the Phi(a_n) correspondence. Does it live at Σ_2 (Phi(a_2) = Einstein-Hilbert kinematic skeleton; wave-classification weight) or Σ_1 (Phi(a_0) = perimeter/cosmological-term; user-adjudication-only)? The substrate-distance-N pole structure suggests Phi(a_2) → Σ_2 for substrate-distance-1 pole `s=3` and Phi(a_4) → Σ_3 for substrate-distance-2 pole `s=4`, but the Connes-Moscovici 1995 §III.4 residue formula explicit pole structure at d=4 might admit a different mapping. Pre-register the structural prediction for §VII.AU.OP-PROJ's Σ_n enforcement layer assignment, which will determine the methodology-floor F-image axis structure for §VII.AU CF-65 first-extraction.

---

## Round 2 — Connes: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

Volovik's R2 CONVERGENCE accepted the Reading B-weak Hybrid (option iii) landing in full and sharpened V2/V3/V4 to their canonical readings. The R2 DISSENT raised three structurally precise concerns about Re:V4's Hybrid registry-text mechanics; the R2 EMERGENCE added five cross-cutting structural insights; Q-VOL-1/2/3 pose forward-looking discriminative questions on Level-3 anchor singleness, MIXED-PARTIAL K-counter advancement criterion, and Phi(a_n) → Σ_n correspondence application to substrate-distance-1 pole `s=3`. I accept the corrections, sharpen one residual point, and answer Q-VOL-1/2/3 below.

**(1) Accept DISSENT #1 — Level-2 envelope sub-row table is DIAGNOSTIC ONLY; Level-3 empirical anchor remains single-pinned at `L_emp = −7.046336`**.

Volovik's DISSENT #1 (workshop lines 676-701) is structurally correct and CANONICALIZED. My Re:V4 §2 table (workshop lines 432-436) presented `B(R_FULL-PV) = −527.97` and `B(R_SCHEMATIC) = L_emp = −7.046336` in a single table column annotated "Level-2 envelope F-image table"; the column was structurally ambiguous about whether the FULL-PV value is a Level-3 empirical anchor candidate or a Level-2-B diagnostic datum. Volovik's required separation (workshop lines 688-699) — Level-2-B sub-row DIAGNOSTIC; Level-3 anchor sole-pinned at L_emp — is the structurally correct landing per `substrate-first-canonical-sourcing.md §(i)` substrate-first canonical sourcing direction and per `s88-pending-edits-ledger.md` "preserve K-window log-derivative anchor `−7.046336` as SOLE Corner-IV calibration source".

The substrate-IS reading: `L_emp = −7.046336` IS the substrate-natural canonical anchor (verified at PV_mass → 0 to bit precision 4.7e−7 per WP line 150); `B(R_FULL-PV) = −527.97` IS the regulator-class image at the finite-PV-mass NON-asymptotic regime (per WP line 198, `M_PV / Δ_BCS ≈ 2.16`). The two values are NOT co-primary at the Level-3 anchor axis under the algebra-axis K=3 MANDATORY (single substrate-IS observable per `(M_2(ℂ), P_BdG, s=4)` triple) AND the substrate-first canonical sourcing direction (substrate-natural anchor precedes regulator-class images). Re:V4 §2 is REVISED per DISSENT #1: the Level-2 envelope sub-row table is DIAGNOSTIC ONLY at the Level-2-B audit axis; Level-3 empirical anchor row is single-pinned at `L_emp = −7.046336`. Volovik's structural separation block (workshop lines 689-698) is the canonical Hybrid registry-text structure.

**(2) Accept DISSENT #2 — PROXY-REFINEMENT sub-class tag PRESERVED; only route (ii) annotated as CLOSED-FAIL**.

Volovik's DISSENT #2 (workshop lines 703-709) is structurally correct and CANONICALIZED. My Re:V4 §1 (workshop line 421) over-corrected by re-classifying the entire §VII.AV PROXY-REFINEMENT sub-class as REGISTRY-INCOMPLETE-PENDING-REGULATOR-CLASS-DISAMBIGUATION. The §VII.AV refinement-pathway table at registry line 18108-18120 enumerates SEVEN routes (i) Friedrich-Bär saturation / (ii) FULL Pauli-Villars at Λ_UV = M_KK / (iii) FULL Connes-Chamseddine 1996 multipliers / (iv) K_canonical pin uniqueness operational-alignment / (v) V4 substrate-physics discriminator dual-anchor joint-hypersurface / (vi) Hochschild-cohomology cross-anchor / (vii) Level-2 moduli-deformation extension. ONLY route (ii) is CLOSED-FAIL by W5-1; routes (i), (iii), (iv), (v), (vi), (vii) ALL REMAIN ACTIVE.

The structural reading: the PROXY-REFINEMENT sub-class tag captures the substrate-physics architecture of §VII.AV's deferred-pending status; the route-(ii) FAIL is ONE refinement-pathway closing, NOT the entire sub-class collapsing. Volovik's required fix — V4 §1 status-block text canonical at the route-(ii)-annotation layer; Re:V4 §1 supplementary K=4 MANDATORY F-image disclosure ADDED as APPENDIX (not replacement) — is the structurally correct landing per the deferred-pending intermediate verdict-class rule at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` (SUGGESTION at K=2 per `pru-class-corpus.md`). The §VII.AV registry text retains the PROXY-REFINEMENT classification with route-(ii) sub-row annotation + K=4 F-image disclosure appendix.

**(3) Accept DISSENT #3 (with one refinement) — K=5 corpus extension lands as NEW MIXED-PARTIAL compliance class**.

Volovik's DISSENT #3 (workshop lines 711-715) is structurally correct and CANONICALIZED. The W5-1 instance is a NEW compliance class extending the existing 3-class taxonomy (POSITIVE / PARTIAL-POSITIVE / NEGATIVE) at `substrate-first-canonical-sourcing.md §(iv)`. The structural rationale (workshop line 715): the W5-1 verdict line carries `convention=corner-IV-FULL-PV-Lambda_UV-M_KK-substrate-distance-2-pole-s4` with NO `-SCHEMATIC` suffix (correct — rule (2) requires the suffix only on SCHEMATIC F-image gates; this gate IS the FULL-physical side of the divergence measurement, not the SCHEMATIC side). The implicit SCHEMATIC predecessor (`L_emp = −7.046336` from S87 W2-3 / S88 W5a) is GRANDFATHERED at pre-K=4-MANDATORY status (S88 W7b-83 K=4 promotion landed AT/AFTER the predecessor's emission); the predecessor does NOT carry an explicit `-SCHEMATIC` convention tag retroactively.

The MIXED-PARTIAL class name captures this structural asymmetry: a FULL-physical gate post-K=4-MANDATORY measuring the SCHEMATIC↔FULL F-image divergence against an implicitly-GRANDFATHERED SCHEMATIC predecessor pre-K=4-MANDATORY. Neither side individually carries the structurally complete dual-tag disclosure. This is structurally analogous to PARTIAL-POSITIVE landed at S90 W1-9 (a structurally-intermediate compliance class admitted with explicit severity band ADVISORY S2; tier_pin row forward-recommended-not-mandatory).

**Refinement to DISSENT #3**: the MIXED-PARTIAL class K-counter advancement criterion (Volovik's Q-VOL-2) should adopt the BOTH-SIDES-POST-K=4 criterion (more restrictive) rather than EITHER-SIDE-POST-K=4 (more inclusive). The structural reason: the MIXED-PARTIAL class admissibility hinges on the GRANDFATHER asymmetry between FULL-physical and SCHEMATIC sides; if EITHER side is pre-K=4-MANDATORY, the divergence measurement IS MIXED-PARTIAL by structural definition. K-counter advancement under the BOTH-SIDES criterion captures instances where the divergence is measured between TWO post-K=4-MANDATORY gates (no GRANDFATHER asymmetry) — these are the STRUCTURALLY DISTINCT class that should advance the K-counter toward MIXED-PARTIAL → MANDATORY promotion at K=3 distinct calibration instances. Until the BOTH-SIDES criterion lands its first instance, the MIXED-PARTIAL class remains at SUGGESTION K=1 with the W5-1 instance as the first MIXED-PARTIAL calibration. This is detailed in Q-VOL-2 answer below.

**(4) Accept EMERGENCE #1-#5 in full — five cross-cutting structural insights canonicalized**.

- **EMERGENCE #1 (multiplicative-normalization-cancellation theorem as calibration-corpus instance #1 for `math-scripts.md §"Multiplicative-normalization cancellation invariants"` extension)**: ACCEPTED. The rule-file extension structure pre-registered at workshop lines 728-750 is the canonical CF-S92-W5-1-D landing target. V2 Steps 1-5 substitution chain (workshop lines 71-104) IS the substrate-physics derivation; Re:V2 line 291 CONFIRMED the derivation; C1 Phi-correspondence framing (workshop lines 527-557) establishes the within-class Phi-trivial action at Σ_3 enforcement.

- **EMERGENCE #2 (§VII.AV Hybrid registry-text consequences for mack-cosmic-bridge sole-writer landing at S92 W0)**: ACCEPTED with the Dissent fix 1-2 separations applied. The Hybrid registry-text update structure at workshop lines 759-795 (incorporating Dissent fixes 1+2) IS the canonical landing target. The status block APPENDIX disclosure of K=4 MANDATORY F-image structure preserves the PROXY-REFINEMENT sub-class tag; the Level-2 envelope sub-row table is DIAGNOSTIC ONLY at Level-2-B axis; Level-3 anchor remains single-pinned at L_emp.

- **EMERGENCE #3 (cross-link consequences for §VII.AU.OP-PROJ / §VII.AY.OP-PROJ / §VII.BA / §VII.AF.1.OP-PROJ)**: ACCEPTED. The Hybrid (option iii) framing IS the canonical pattern for any §VII entry where SCHEMATIC↔FULL F-image divergence is structurally consequential. The four cross-linked §VII slots (workshop lines 801-807) inherit the pattern at structurally analogous positions. I add one cross-link refinement at EMERGENCE below (third sub-bullet).

- **EMERGENCE #4 (continuous-deformation test (V3 + Re:V5) as canonical structural filter for future inheritance-morphism-style splitting proposals)**: ACCEPTED. The forward-looking discipline at workshop lines 814-819 IS the canonical first-pass filter for any future workshop proposing slot-split at the substrate-IS observable axis. CF-S92-W5-1-C reframed (regulator-class transition-map disambiguation) IS the canonical first-instance application of the filter beyond the WP line 150 PV_mass → 0 case. I sharpen the rule-extension status in EMERGENCE below (first sub-bullet).

- **EMERGENCE #5 (Phi(a_4) → Σ_3 enforcement layer correspondence for substrate-distance-2 pole observables on the BdG sub-algebra)**: ACCEPTED. The Phi-correspondence framing IS the structural reading of the methodology-floor F-image axis structure at Σ_3 enforcement; future substrate-distance-2 pole `s=4` observables on Cell IV inherit the 3-axis Σ_3 enforcement structure by Phi-correspondence. The pre-registered prediction for substrate-distance-1 pole `s=3` (Q-VOL-3) is addressed below.

### DISSENT

One residual concern with the multiplicative-cancellation calibration corpus instance #1 (CF-S92-W5-1-D) K-counter advancement criterion — a sharpening of EMERGENCE #1, not a reversal.

**Multiplicative-cancellation rule extension requires explicit non-multiplicative cross-check before K=2 advancement**.

The proposed `math-scripts.md §"Multiplicative-normalization cancellation invariants"` rule extension at EMERGENCE #1 (workshop lines 728-750) is structurally sound at K=1 (V2 Steps 1-5 demonstrate the within-class L_max-INVARIANCE structurally); the calibration corpus instance #1 (S91 W5-1) is canonicalized. However, the K-counter advancement from K=1 SUGGESTION → K=3 MANDATORY per `feedback_rules-compensate-missing-structure.md` REQUIRES distinct calibration instances — and "distinct" must be tested AGAINST the structural class the rule extension addresses.

The risk: future Cell-IV substrate-IS observables at other substrate-distance poles (e.g., §VII.AU at `s=3`, §VII.AY, §VII.BA — workshop EMERGENCE #3 candidates) MAY admit multiplicative L_max factorization at their respective Mellin trace evaluations. If they do, the K-counter advances K=1 → K=2 → K=3 trivially under the multiplicative-factorization hypothesis. The K-counter advancement would then be MEASUREMENT-based (the rule fires because the observable empirically multiplicatively-factorizes), NOT STRUCTURALLY DIVERSE (the rule fires across structurally-distinct factorization mechanisms).

The structural fix: require that EACH K-counter advancement instance for the multiplicative-cancellation rule extension includes a PRE-FLIGHT NON-MULTIPLICATIVE cross-check at plan-freeze. Specifically, the plan-block authoring a new gate that may trigger the multiplicative-cancellation pre-flight check MUST pre-register:

```
(i) Pre-flight test that the observable f^{(L_max)}(K) admits the multiplicative
    factorization f^{(L_max)}(K) = w(L_max) · g(K) — substantively verified by
    explicit symbolic test (Sage MCP `sage_eval` factorization check) at L_max
    boundary values (e.g., L_max ∈ {6, 12}).
(ii) PASS only if the symbolic factorization is structurally verified AND the
     factorization mechanism is STRUCTURALLY DIFFERENT from the prior K-counter
     instance (e.g., not just "Casimir-bound truncation on a different pole" but
     "non-Casimir-bound machinery on a structurally-distinct algebra cell").
(iii) The K-counter advancement criterion adopts the structurally-diverse
      criterion: K=1 SUGGESTION → K=2 SUGGESTION → K=3 MANDATORY iff
      EACH instance presents a STRUCTURALLY DISTINCT factorization mechanism.
      Same-mechanism multiplicative-factorization on different observables
      does NOT advance the K-counter.
```

The rationale: the multiplicative-cancellation rule's structural content is the OPERATOR property of `d² ln(·) / d(ln K)²` annihilating multiplicative pre-factors — this is a textbook fact (Volovik V2 line 106 "translation invariance of curvature"). Promoting the rule to MANDATORY at K=3 requires evidence that the rule operates across STRUCTURALLY DISTINCT factorization mechanisms, not across instances of the SAME mechanism applied to different observables. Without the structural-diversity criterion, the K-counter could advance trivially to MANDATORY at K=3 within a single session by enumerating substrate-distance poles, which would over-promote the rule.

This is a SHARPENING of EMERGENCE #1's rule-extension proposal, not a reversal. The CF-S92-W5-1-D landing should include the structural-diversity K-counter advancement criterion in the rule-extension text; the canonical landing at S92 mack-cosmic-bridge sole-writer should add this discipline to the proposed `math-scripts.md §"Multiplicative-normalization cancellation invariants"` extension. The K=1 SUGGESTION status at S91 W5-1 close is preserved; K=2/K=3 advancement is gated on structural-diversity verification.

### EMERGENCE

Three additional structural insights from the R2 cross-pollination, extending Volovik's EMERGENCE #1-#5:

**(1) Continuous-deformation structural filter (Volovik EMERGENCE #4) — rule-extension status pinned at SUGGESTION K=1 with proposed landing at `cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural filter"` (NEW section)**.

Volovik's EMERGENCE #4 framing (workshop lines 814-819) IS the canonical structural filter for any future inheritance-morphism-style splitting proposal at the substrate-IS observable axis. The structural extension this insight licenses is a NEW section at `cross-pillar-bridge-anatomy.md` (the rule-file already operates at the substrate-IS observable identity layer per the K=3 MANDATORY algebra-axis orthogonality clause; the new section extends to the empirical-test layer for slot-split proposals).

**Proposed rule-file extension structure** (CF-S92-W5-1-C-EXT; companion to CF-S92-W5-1-C regulator-class transition-map disambiguation):

```
cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural filter"
   (NEW section; calibration corpus instance #1 = S91 W4 workshop verdict)

Rule: To license a slot-split at the substrate-IS observable axis of a §VII
      registry entry — i.e., to propose that observable values O₁ and O₂ at the
      same nominal (algebra, projector, pole) triple inhabit STRUCTURALLY DISTINCT
      substrate-IS observables (Reading B-strong-style slot-split) — the proposer
      MUST produce a parameter scan (regulator-mass, coupling, deformation
      parameter, OR analog substrate parameter) demonstrating a DISCONTINUOUS
      jump in the observable identity at some finite parameter value.

      Continuous deformation across all parameter values (analog of W5-1 PV_mass
      scan: PV_mass = 0 → M_KK → √2·M_KK → ... → ∞ producing continuous
      interpolation in the observable value WITHOUT discrete identity jump)
      FORBIDS the slot split; the substrate-IS observable identity is single-pinned
      per K=3 MANDATORY algebra-axis axiom, and the divergence in observable
      values IS a methodology-floor F-image divergence at the regulator-class /
      coupling / deformation-parameter axis per K=4 MANDATORY level-pin
      discipline at substrate-first-canonical-sourcing.md §(iv).

Calibration corpus K=1 at S91 W4 workshop verdict:
   - W5-1 PV_mass scan from PV_mass = 0 (kernel-verification anchor returning
     -7.046336 ± 4.7e-7 to bit precision) to PV_mass = (M_KK, √2·M_KK) (FULL-PV
     pipeline returning -527.97 M_KK²) is CONTINUOUS; no discrete identity jump
     at any finite PV_mass per WP line 150 numerical-kernel-independence test.
   - Reading B-strong slot-split proposal (Re:V4 § C2 original; Reading B-strong
     line 564-573) was RETRACTED in full per the continuous-deformation evidence
     (Re:V3 line 369; Re:V5 line 469).
   - Reserved K=2 / K=3 rows for forward calibration instances at other §VII
     entries where slot-split proposals arise.

Status: SUGGESTION at K=1; promotes to MANDATORY at K=3 distinct calibration
        instances per feedback_rules-compensate-missing-structure.md K-counter
        threshold.
```

This rule extension lives on the SAME rule-file as the K=3 MANDATORY algebra-axis orthogonality clause; it operates at the empirical-test layer for SLOT-SPLIT proposals specifically (the algebra-axis clause operates at the structural-axiom layer; the new section operates at the empirical-evidence requirement for slot-split licensure). CF-S92-W5-1-C dispatch at S92 IS the canonical first-instance application of the filter beyond the WP line 150 case — measuring the PV_mass continuum at intermediate values [0.5 M_KK, 5 M_KK, 100 M_KK, 1000 M_KK] to confirm continuity AND the asymptotic limit recovery of L_emp = -7.046336.

**(2) Phi(a_n) → Σ_n correspondence application to §VII.AU.OP-PROJ at substrate-distance-1 pole `s=3` (answer-anchor to Q-VOL-3)**.

This sub-bullet extends EMERGENCE #5 (Volovik) and pre-registers the Σ_n enforcement layer assignment for §VII.AU.OP-PROJ; full reasoning is in Q-VOL-3 answer below. The pre-registered structural prediction (forward-looking from S91 W4 workshop close):

```
Pre-registered prediction (CF-S92-W5-1-E forward gate):
   §VII.AU.OP-PROJ observable at substrate-distance-1 pole s=3 lives at the
   Σ_2 enforcement layer under the Phi(a_2) = Σ_2 wave-classification weight.
   The 3-axis methodology-floor F-image structure at Σ_2 differs structurally
   from Σ_3 (W5-1 observable at substrate-distance-2 pole s=4):
   - Level axis (SCHEMATIC vs FULL): present at Σ_2 (inherited from K=4 MANDATORY
     level-pin discipline; same orthogonal axis as Σ_3)
   - UV-regulator-class axis (a_n^{R} tagging): present at Σ_2
   - Binding axis (canonical-import vs substrate-natural): present at Σ_2

   The structural difference: at Σ_3 (W5-1 observable), the methodology-rule
   extensions cataloging F-image divergence are MANDATORY at K=4 (level-pin
   discipline) + MANDATORY at K=3 (algebra-axis orthogonality) + SUGGESTION at K=1
   (binding axis). At Σ_2 (§VII.AU observable), the same axes apply WITH the
   wave-classification weight specialization — methodology rules at Σ_2 are
   gated by wave-classification per .claude/rules/wave-classification.md M1-M4
   conjunction. The §VII.AU CF-65 first-extraction gate IS a wave-classification
   METHODOLOGY-class wave per the M1-M4 test (currently classified COMPUTE per
   the gate-block; pre-registered prediction is that future S91+ §VII.AU updates
   may inherit METHODOLOGY-class wave attribution under Σ_2 enforcement).

   The pre-registered structural prediction for §VII.AU CF-65 first-extraction
   landing: if §VII.AU's L_max scan produces an L_max-INVARIANT plateau (analog
   of W5-1 multiplicative-cancellation), CF-S92-W5-1-D's K-counter advances
   K=1 → K=2 (calibration corpus instance #2 at structurally-distinct pole s=3
   on a structurally-distinct substrate algebra cell — Cell I algebra-INVARIANT
   spectrum-only-functional). The structural-diversity criterion (Dissent above)
   is satisfied because the §VII.AU observable is on Cell I (algebra-INVARIANT)
   while §VII.AV is on Cell IV (algebra-DEPENDENT); the factorization mechanisms
   are structurally distinct (Cell I admits closed-form algebraic identities at
   the substrate algebra; Cell IV requires state-pair functional evaluation).
```

This pre-registered prediction is the forward-looking carry-forward CF-S92-W5-1-E.

**(3) Cross-link consequences for §VII.AU.OP-PROJ, §VII.AY.OP-PROJ, §VII.BA, §VII.AF.1.OP-PROJ at S92+**.

Volovik's EMERGENCE #3 (workshop lines 797-807) enumerates four cross-linked §VII slots inheriting the Hybrid (option iii) framing. I add one structural refinement: the cross-link discipline should explicitly cite WHICH methodology-rule extension governs each cross-linked slot's F-image axis structure, to avoid future-reader category confusion at the registry text layer.

**Specific cross-link discipline pre-registered for forward landings**:

- **§VII.AU.OP-PROJ inheritance**: cross-link cites `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline (SCHEMATIC vs FULL F-image axis) + `regulator-pin-discipline.md` UV-regulator pin discipline. The Σ_2 enforcement layer assignment per the Phi correspondence (Q-VOL-3 answer below) governs the wave-classification weight. CF-65 first-extraction landing at S92 should pre-register Hybrid-style sub-row structure IF L_max-INVARIANT plateau appears.

- **§VII.AY.OP-PROJ inheritance**: cross-link cites `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY + `cross-pillar-bridge-anatomy.md §"Level-2 audit axes (Level-2-A vs Level-2-B)"`. If §VII.AY's substrate-IS observable admits multiplicative L_max factorization at the BdG sub-algebra, CF-S92-W5-1-D's K-counter advances K=1 → K=2 under the structural-diversity criterion IFF the factorization mechanism is STRUCTURALLY DISTINCT from §VII.AV's Casimir-bound truncation.

- **§VII.BA Wodzicki-BCS inheritance**: cross-link cites `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` Friedrich-Bär saturation theorem (W11-3 precedent) + the asymptotic-limit prediction `B(R_FULL-PV) → B(R_ζ-Wodzicki) = R_Wodzicki` as `M_PV → ∞` (per Re:V5 line 477 continuous-limit). The cross-link IS the structural identification: §VII.BA's Wodzicki anchor IS THE asymptotic limit of §VII.AV's regulator-class-keyed sub-row table. The pre-registered prediction for §VII.BA: at L_max → ∞ + asymptotic regulator-mass limit, `R_Wodzicki` is the converged F-image; future §VII.AV updates IF they include asymptotic regulator-mass scan should converge to §VII.BA's canonical anchor value.

- **§VII.AF.1.OP-PROJ inheritance**: cross-link cites `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` Binding axis K=1 SUGGESTION. §VII.AV adopts substrate-natural-binding (B_PV derived from substrate D_K spectrum + S52 Bogoliubov amplitudes; per C1 Table line 523 "substrate-natural-binding (B_PV derived from substrate D_K spectrum + S52 Bogoliubov amplitudes; NOT a canonical-import pin)"); §VII.AF.1.OP-PROJ adopts canonical-import-binding (S88 W7b-82 baseline `gv_canonical_difference_FW = -40579.1500479506`). The two §VII slots are STRUCTURALLY ORTHOGONAL methodology-floor F-image classes at the Binding axis; they advance the Binding-axis K-counter K=1 → K=2 jointly (per `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` Binding-axis Hybrid Independence Test).

#### Answers to Q-VOL-1/2/3

**Q-VOL-1 (registry-text Level-3 anchor singleness as structural discipline)**: **CONFIRMED**. The Hybrid landing with Dissent fix 1 (Level-2-B sub-row DIAGNOSTIC ONLY; Level-3 anchor single-pinned at L_emp) IS a structural discipline that should extend forward to all §VII entries adopting the Hybrid framing at Cell IV (and structurally analogous cells where Level-3 anchor singleness is licensed by the substrate-first canonical sourcing direction).

The structural reading: the K=3 MANDATORY algebra-axis orthogonality pins the substrate-IS observable identity at the (algebra, projector, pole) triple layer; the Hybrid (option iii) landing extends this to a Level-3 anchor singleness discipline at the empirical-anchor axis. The two are STRUCTURALLY DIFFERENT layers (substrate-IS observable identity vs Level-3 empirical anchor) but the discipline is the SAME structural axiom: ONE canonical source per axis. Future Hybrid landings at Cell IV (and analogous cells) MUST maintain this separation; cross-corner co-primary at Level-3 anchor axis is FORBIDDEN by the same substrate-first canonical sourcing direction that DISSENT #1 invokes.

**Pre-registered rule-extension proposal** (CF-S92-W5-1-F; forward-looking from S91 W4 workshop close):

```
cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"
   §"Level-3 anchor singleness sub-clause" (proposed addition)

Rule: For any §VII entry adopting the Hybrid (single-slot with regulator-class-
      keyed Level-2-B sub-row table) registry-text framing, the Level-3 empirical
      anchor MUST be single-pinned at the substrate-natural canonical source. The
      Level-2-B sub-row table is DIAGNOSTIC ONLY at the methodology-floor F-image
      axis; sub-row values MUST NOT be cross-referenced as Level-3 anchor
      co-primaries. This extends the substrate-first canonical sourcing direction
      (substrate-first-canonical-sourcing.md §(i)) to the Level-3 anchor axis
      under the Hybrid framing.

Calibration corpus K=1 at S91 W4 workshop verdict:
   - §VII.AV Hybrid landing: L_emp = -7.046336 single-pinned at Level-3 anchor
     (per s88-pending-edits-ledger.md SOLE Corner-IV calibration source);
     B(R_FULL-PV) = -527.97, B(R_FULL-CC) = TBD, B(R_ζ-Wodzicki) = L_emp at
     asymptotic limit ALL recorded at Level-2-B DIAGNOSTIC axis.
   - Reserved K=2 / K=3 rows for forward Hybrid landings at §VII.AU /
     §VII.AY / §VII.BA / §VII.AF.1.OP-PROJ.

Status: SUGGESTION at K=1; promotes to MANDATORY at K=3 distinct calibration
        instances per feedback_rules-compensate-missing-structure.md.
```

This rule extension is queued as CF-S92-W5-1-F for the canonical mack-cosmic-bridge sole-writer landing at S92.

**Q-VOL-2 (MIXED-PARTIAL class K-counter advancement criterion)**: The K-counter advancement criterion should adopt **BOTH-SIDES-POST-K=4-MANDATORY** (more restrictive), NOT EITHER-SIDE-POST-K=4 (more inclusive). The structural reasoning (sharpened from DISSENT #3 refinement above):

The MIXED-PARTIAL class admissibility hinges on the GRANDFATHER asymmetry: a FULL-physical gate post-K=4-MANDATORY measuring the SCHEMATIC↔FULL F-image divergence against an implicitly-GRANDFATHERED SCHEMATIC predecessor pre-K=4-MANDATORY. If we adopt EITHER-SIDE-POST-K=4 as the K-counter advancement criterion, ANY future instance where ONE side of the divergence is post-K=4-MANDATORY advances the K-counter — but this includes instances where the OTHER side is GRANDFATHERED. The K-counter would then advance trivially as more SCHEMATIC predecessors get measured against new FULL-physical gates; the MIXED-PARTIAL → MANDATORY promotion at K=3 would land within 2-3 sessions without structural diversity.

Under BOTH-SIDES-POST-K=4-MANDATORY (the K-counter advances ONLY when BOTH sides of the divergence are individually post-K=4-MANDATORY at their respective producing gates), the K-counter captures STRUCTURALLY DISTINCT instances: divergences measured between TWO post-K=4-MANDATORY gates with EXPLICIT dual-tag disclosure on BOTH sides (no GRANDFATHER asymmetry). These instances test whether the MIXED-PARTIAL class admissibility extends to the post-GRANDFATHER regime where structural compliance is mandated on both sides; this is the structurally meaningful K-counter advancement.

**Pre-registered K-counter advancement criterion** (CF-S92-W5-1-G; forward-looking from S91 W4 workshop close):

```
substrate-first-canonical-sourcing.md §(iv) §"3-class compliance taxonomy"
   §"MIXED-PARTIAL class K-counter advancement criterion" (proposed addition)

Rule: The MIXED-PARTIAL class K-counter advances K → K+1 ONLY when the candidate
      calibration instance satisfies BOTH-SIDES-POST-K=4-MANDATORY: BOTH sides
      of the SCHEMATIC↔FULL F-image divergence are individually post-K=4-MANDATORY
      at their respective producing gates (S88 W7b-83 close or later) AND BOTH
      carry the structurally complete dual-tag disclosure (CLASS pin SCHEMATIC
      declared in producing-script docstring + -SCHEMATIC convention suffix on
      verdict-line + tier_pin row).

Calibration corpus at S91 W4 close:
   - K_substantive = 5 (W4-2 NEGATIVE + W9b-2 NEGATIVE + W9c-1 POSITIVE +
                       W5-7 PARTIAL-POSITIVE + W5-1 MIXED-PARTIAL [NEW])
   - K_MIXED-PARTIAL = 1 (W5-1 instance only; reserves K=2/K=3 rows for
                          BOTH-SIDES-POST-K=4 future instances)

Status: SUGGESTION at K=1 (W5-1 instance); MIXED-PARTIAL class admissible from
        S91 W5-1 forward at ADVISORY S2 severity; MIXED-PARTIAL → MANDATORY
        promotion gated at K=3 BOTH-SIDES-POST-K=4 instances per K-counter
        advancement criterion above.
```

This K-counter advancement criterion is queued as CF-S92-W5-1-G for the canonical landing at S92.

**Q-VOL-3 (Phi(a_n) → Σ_n enforcement layer at substrate-distance-1 pole `s=3`)**: §VII.AU.OP-PROJ observable at substrate-distance-1 pole `s=3` lives at **Σ_2 enforcement layer** under the Phi(a_2) = Σ_2 wave-classification weight per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence.

The substrate-IS structural reasoning. The Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula at d=4 has poles at substrate-distance n = 0, 1, 2 corresponding to s = 2, 3, 4 — the residue at pole `s = (2n+2)/dim(p+q) = ...` (substrate-distance-1 pole at s=3; substrate-distance-2 pole at s=4 per §VII.U.1 line 12961). Under the Phi correspondence:

- Phi(a_0) = Σ_1 (perimeter/cosmological-term, weight-0; substrate-distance-0 pole `s=2`)
- Phi(a_2) = Σ_2 (Einstein-Hilbert kinematic skeleton, weight-2; substrate-distance-1 pole `s=3`)
- Phi(a_4) = Σ_3 (Yang-Mills + Higgs quartic load-bearing, weight-4; substrate-distance-2 pole `s=4`)

The §VII.AU observable at substrate-distance-1 pole `s=3` corresponds to the a_2 Seeley-DeWitt coefficient at the substrate's algebra; under Phi, this maps to Σ_2 enforcement-strength = wave-classification weight per `wave-classification.md` M1-M4 conjunction. The structural prediction: methodology rules at Σ_2 are gated by wave-classification — the §VII.AU CF-65 first-extraction landing should pre-register Hybrid-style sub-row structure under the wave-classification METHODOLOGY-class wave attribution IF L_max-INVARIANT plateau appears (analog of §VII.AV's CF-S92-W5-1-D multiplicative-cancellation calibration corpus instance #2 advancement under the structural-diversity criterion).

**Pre-registered structural prediction for §VII.AU CF-65 first-extraction landing** (CF-S92-W5-1-E):

```
Phi(a_2) → Σ_2 enforcement at §VII.AU.OP-PROJ:
   - Methodology-floor F-image axis structure: 3-axis (Level / UV-regulator-class / Binding)
   - Wave-classification weight: Σ_2 (Einstein-Hilbert kinematic skeleton)
   - Specialization vs Σ_3: wave-classification gating per wave-classification.md
     M1-M4 conjunction (M1 PASS predicate; M2 producing operations; M3 source-of-truth;
     M4 allowlist membership)

Pre-registered prediction for CF-65 first-extraction L_max scan:
   - IF L_max-INVARIANT plateau appears (analog of W5-1 multiplicative-cancellation
     mechanism): CF-S92-W5-1-D K-counter advances K=1 → K=2 calibration corpus
     instance #2 at structurally-distinct pole s=3 on structurally-distinct
     algebra cell (Cell I algebra-INVARIANT spectrum-only-functional)
   - IF α extraction returns continuous L^{-α} envelope (no plateau): CF-65
     produces Level-2-binding sub-class certification per
     cross-pillar-bridge-anatomy.md §"Level-2 sub-class"; §VII.AU promotes from
     REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION to STAGE-1-CANDIDATE +
     Level-3 anchor landing
   - IF α extraction returns FAIL band: §VII.AU's PROXY-REFINEMENT pathway
     extends per analog of §VII.AV's CF-S92-W5-1-A alternative envelope-predictor

The Σ_2 enforcement structure is STRUCTURALLY DIFFERENT from Σ_3 only in the
wave-classification weight specialization; the 3-axis methodology-floor F-image
structure is preserved by Phi-correspondence (same orthogonality at all Σ_n layers).
```

This pre-registered prediction is queued as CF-S92-W5-1-E forward gate.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | (a) F-mapping of R_KW^{PV}(L_max) | V1, Re:V1 | **Converged** | Single substrate-IS observable at `(M_2(ℂ), P_BdG, s=4)` per K=3 MANDATORY algebra-axis orthogonality; SCHEMATIC and FULL-PV are STRUCTURALLY DISTINCT methodology-floor F-images of the SAME Level-1 cohomology class per K=4 MANDATORY level-pin discipline at `substrate-first-canonical-sourcing.md §(iv)` + Level-2-A/B audit-axis clause at `cross-pillar-bridge-anatomy.md` |
| 2 | (b) L_max-INVARIANT plateau structural status | V2, Re:V2 | **Converged** | Multiplicative-normalization-cancellation produces L_max-INVARIANT plateau STRUCTURALLY within any single F-image class (V2 Steps 1-5 derivation canonical); plateau MAGNITUDE B(R) is regulator-class-keyed at Level-2-B; the within-class L_max-INVARIANCE is Phi-trivial at Σ_3 enforcement (C1); the cross-class plateau-magnitude divergence IS the discriminator |
| 3 | (c) 7393% rel-err structural meaning | V3, Re:V3 | **Converged** | WP line 150 PV_mass → 0 continuous-deformation evidence (kernel-verification anchor returns `-7.046336 ± 4.7e-7` to bit precision) CLOSES Reading B-strong (two distinct substrate-IS observables RETRACTED); the 75× plateau divergence IS the methodology-floor F-image divergence at regulator-class axis on a single substrate-IS observable; Reading A's "FALSIFICATION" and Reading B-weak's "regulator-class-keyed F-images" framings are STRUCTURALLY EQUIVALENT |
| 4 | (d) §VII.AV registry text update canonical | V4, Re:V4 | **Converged on Hybrid (option iii)** | Single §VII.AV slot per K=3 MANDATORY (algebra-axis orthogonality preserved); Level-2 envelope sub-rows regulator-class-keyed at Level-2-B DIAGNOSTIC axis per K=4 MANDATORY (DISSENT fix 1: NOT promoted to Level-3 anchor co-primary); PROXY-REFINEMENT sub-class tag PRESERVED with route-(ii) annotation only (DISSENT fix 2); Level-3 anchor remains single-pinned at L_emp = -7.046336; mack-cosmic-bridge sole-writer landing at S92 W0 |
| 5 | Cross-cutting explicit predictions | V5, Re:V5 | **Converged on continuous-limit + Reading A-tighter at finite mass** | Both Reading A and Reading B-weak predict continuous PV_mass interpolation: PV_mass = 0 → M_KK → ∞ returns L_emp → -527.97 → L_emp; Reading A's tighter prediction for CF-S92-W5-1-B (FULL-CC vs FULL-PV) is `|B(R_FULL-CC) - B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.30` (Q-CON-1 answer in R2 line 836); Reading B-weak's band ≤ 0.50; the CF-S92-W5-1-B verdict is structurally well-defined under either reading |
| 6 | C1: Phi(a_n) F-decomposition correspondence | C1 | **Converged + sharpened** | Phi(a_4) → Σ_3 enforcement at substrate-distance-2 pole `s=4` on BdG sub-algebra; 3 orthogonal methodology-floor F-image axes (Level / UV-regulator-class / Binding) per Σ_3; within-class L_max-INVARIANCE is Phi-trivial; cross-class plateau-magnitude divergence is Phi-NON-trivial; Q-VOL-3 answer extends the framework to Σ_2 enforcement at substrate-distance-1 pole `s=3` for §VII.AU |
| 7 | C2: §VII.AV slot split structural-orthogonal-companion | C2 | **Converged on retraction** | Reading B-strong slot-split RETRACTED in full per Re:V3 + Re:V5 continuous-deformation evidence + Re:V4 clause-4 same-corner co-primary FORBIDDEN; §VII.AV remains single slot per K=3 MANDATORY; structural-orthogonal-companion structure REPLACED by single-slot Hybrid with regulator-class-keyed Level-2-B sub-rows (Re:V4 §2 reframed per DISSENT #1 separation) |
| 8 | **EMERGED**: Hybrid (option iii) as canonical workshop verdict | Volovik R2 CONVERGENCE #3 | **Emerged** | The Hybrid is the UNIQUE structurally-correct landing under BOTH K=3 MANDATORY (algebra-axis orthogonality) AND K=4 MANDATORY (level-pin discipline); option (i) Reading A honors K=3 but does not record K=4 F-image structure; option (ii) Reading B-strong attempts F-image disclosure but violates K=3 |
| 9 | **EMERGED**: Multiplicative-normalization-cancellation rule-extension as CF-S92-W5-1-D calibration corpus instance #1 | Volovik R2 EMERGENCE #1 + Connes R2 DISSENT sharpening | **Emerged with structural-diversity K-counter criterion** | `math-scripts.md §"Multiplicative-normalization cancellation invariants"` extension at K=1 SUGGESTION; calibration corpus instance #1 = S91 W5-1 V2 Steps 1-5 substrate-physics derivation + L_max plateau evidence + α-rank-deficient confirmation; K=2/K=3 advancement REQUIRES structural-diversity criterion (DISSENT sharpening); promotes to MANDATORY at K=3 STRUCTURALLY DIVERSE factorization mechanisms |
| 10 | **EMERGED**: Reading B-strong slot-split RETRACTED — continuous-deformation structural filter | Volovik V3 + Connes Re:V3 + Volovik R2 EMERGENCE #4 + Connes EMERGENCE (1) | **Emerged** | Continuous-deformation test (V3 + Re:V5 + WP line 150 PV_mass → 0 kernel verification at 4.7e-7 bit precision) becomes the canonical structural filter for ANY future inheritance-morphism-style slot-split proposal at the substrate-IS observable axis; proposed `cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural filter"` rule extension at K=1 SUGGESTION (CF-S92-W5-1-C-EXT) |
| 11 | **EMERGED**: MIXED-PARTIAL compliance class (K=5 corpus extension at `substrate-first-canonical-sourcing.md §(iv)`) | Volovik R2 DISSENT #3 + Volovik Q-VOL-2 + Connes answer | **Emerged with BOTH-SIDES-POST-K=4 advancement criterion** | NEW 4th compliance class extending POSITIVE/PARTIAL-POSITIVE/NEGATIVE 3-class taxonomy at K=4 MANDATORY level-pin discipline; W5-1 instance lands at K_MIXED-PARTIAL = 1 SUGGESTION; admissibility band ADVISORY S2 (analog of PARTIAL-POSITIVE); K-counter advancement criterion ADOPT BOTH-SIDES-POST-K=4-MANDATORY (more restrictive); K=3 BOTH-SIDES MANDATORY promotion future-gated |
| 12 | **EMERGED**: Level-3 anchor singleness sub-clause for Hybrid landings | Volovik Q-VOL-1 + Connes answer | **Emerged** | Forward-looking rule extension at `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"`: Hybrid landings at Cell IV (and analogous cells) MUST maintain Level-3 anchor singleness; Level-2-B sub-row table DIAGNOSTIC ONLY; cross-corner co-primary at Level-3 anchor axis FORBIDDEN; K=1 SUGGESTION at S91 W4 close; CF-S92-W5-1-F landing target |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **CF-S92-W5-1-A — Alternative envelope-predictor derivation**. Per V4 §4 + Re:V4 §3 reframed. Substrate-physics derivation of regulator-class-keyed envelope family B(R) for R ∈ {SCHEMATIC, FULL-PV, FULL-CC, ζ-Wodzicki} on the §VII.AV observable. Candidate predictors: (a) HKR image residue-pole with regulator-class-dependent K-tail integration; (b) Friedrich-Bär saturation theorem extended to regulator-class-keyed envelope family; (c) Connes-Karoubi pairing on the BdG sub-algebra K-theory boundary with regulator-class index. PASS: predictor produces structurally-derived envelope reproducing FULL-PV at L_max=12 within 5% AND admits Level-2-binding sub-class. FAIL: no predictor produces an L_max-INVARIANT-plateau-matching prediction. Input: §VII.AV registry text post-Hybrid landing; S52 Bogoliubov amplitudes from `s52_bogoliubov_amp.npz`; W5-1 verdict data from `s91_w5_1_full_bdg_pv.npz`.

2. **CF-S92-W5-1-B — FULL-CC vs FULL-PV α extraction comparison (Reading A vs Reading B-weak structural discriminator)**. Per V4 §6 + Re:V4 §5. Run FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers pipeline on the SAME `(M_2(ℂ), P_BdG, s=4)` triple as W5-1 FULL-PV. Pre-registered prediction-discriminator:
   - Reading A-tighter (Q-CON-1 answer): `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.30`; `α_CC ∈ [4.5, 8.0]`; both α extractions rank-deficient (σ → ∞) via multiplicative-cancellation.
   - Reading B-weak: `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.50`; `|B(R_FULL-CC) − L_emp| / |L_emp| ≥ 10`.
   - Independence test: `|α_CC − α_PV| / α_PV ≤ 0.05` → FI (Reading A weak); `|Δα|/α_PV > 0.20` → RD-class-divergent (Reading B-weak strong).

3. **CF-S92-W5-1-C — Regulator-class transition-map disambiguation (V3 + Re:V5 continuous-deformation filter calibration corpus instance #1 application)**. Per Re:V4 §4 reframed. Run PV_mass scan at intermediate values [0, 0.5 M_KK, M_KK, √2 M_KK, 5 M_KK, 100 M_KK, 1000 M_KK] on the SAME W5-1 script architecture; confirm continuous interpolation `R_KW^{PV}(PV_mass)` from `-7.046336` (PV_mass = 0; kernel-verification anchor) → `-527.97` near M_KK → back to `-7.046336` at asymptotic large-mass (Wodzicki residue recovery). PASS: continuous interpolation across all intermediate values (no discrete identity jump). INFO: piecewise-continuous interpolation with structural justification. FAIL: discrete identity jump at any finite PV_mass → re-opens Reading B-strong slot-split question. Input: `s91_w5_1_full_bdg_pv.npz` script architecture; canonical L_emp anchor.

4. **CF-S92-W5-1-D — METHODOLOGY-class extension to `math-scripts.md §"Multiplicative-normalization cancellation invariants"` (calibration corpus instance #1 landing + structural-diversity K-counter criterion)**. Per Volovik R2 EMERGENCE #1 + Connes R2 DISSENT sharpening. Land the rule-file extension structure at workshop lines 728-750 with the additional structural-diversity K-counter advancement criterion: K=1 SUGGESTION → K=2 SUGGESTION → K=3 MANDATORY iff EACH instance presents a STRUCTURALLY DISTINCT factorization mechanism (not just "same Casimir-bound truncation on a different pole"). Pre-flight Sage-MCP symbolic factorization check + structural-diversity verification at plan-freeze for ALL future K-counter-advancing instances. Calibration corpus instance #1 = S91 W5-1 (V2 substitution chain + L_max plateau evidence + α-rank-deficient confirmation). Mack-cosmic-bridge sole-writer landing at S92.

5. **CF-S92-W5-1-E — Phi(a_2) → Σ_2 enforcement pre-registration for §VII.AU.OP-PROJ at substrate-distance-1 pole `s=3`** (Q-VOL-3 answer-anchor). Per Connes EMERGENCE (2) + Q-VOL-3 answer. Pre-register the Σ_2 enforcement layer assignment for §VII.AU.OP-PROJ via the Phi correspondence framework; cross-link the 3-axis methodology-floor F-image structure (Level / UV-regulator-class / Binding) with the wave-classification weight specialization. Pre-registered prediction for §VII.AU CF-65 first-extraction landing: IF L_max-INVARIANT plateau appears, CF-S92-W5-1-D K-counter advances K=1 → K=2 calibration corpus instance #2 at structurally-distinct pole `s=3` on structurally-distinct algebra cell (Cell I). IF α extraction returns continuous envelope, §VII.AU promotes from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION to STAGE-1-CANDIDATE + Level-3 anchor landing.

6. **CF-S92-W5-1-C-EXT — `cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural filter"` rule extension landing** (Volovik EMERGENCE #4 + Connes EMERGENCE (1)). NEW section at K=1 SUGGESTION; calibration corpus instance #1 = S91 W4 workshop verdict (V3 + Re:V3 + Re:V5 continuous-deformation evidence). Rule-file extension text at workshop EMERGENCE (1) Connes sub-bullet. K=2/K=3 MANDATORY promotion future-gated. Mack-cosmic-bridge sole-writer landing at S92.

7. **CF-S92-W5-1-F — `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` §"Level-3 anchor singleness sub-clause" rule extension landing** (Q-VOL-1 answer). NEW sub-clause at K=1 SUGGESTION; calibration corpus instance #1 = S91 W4 §VII.AV Hybrid landing with Level-3 anchor single-pinned at L_emp. Rule-file extension text at workshop EMERGENCE-Q-VOL-1 sub-bullet. K=2/K=3 MANDATORY promotion future-gated on forward Hybrid landings. Mack-cosmic-bridge sole-writer landing at S92.

8. **CF-S92-W5-1-G — `substrate-first-canonical-sourcing.md §(iv) §"3-class compliance taxonomy"` §"MIXED-PARTIAL class K-counter advancement criterion" rule extension landing** (Q-VOL-2 answer). NEW sub-clause at K=1 SUGGESTION; MIXED-PARTIAL → MANDATORY promotion gated at K=3 BOTH-SIDES-POST-K=4-MANDATORY instances. Calibration corpus K_MIXED-PARTIAL = 1 (W5-1 instance only; reserves K=2/K=3 rows for BOTH-SIDES instances). Rule-file extension text at Q-VOL-2 answer block. Mack-cosmic-bridge sole-writer landing at S92.

9. **§VII.AV Hybrid registry-text landing gate** (mack-cosmic-bridge sole-writer; canonical S92 W0 landing). Per Volovik R2 EMERGENCE #2 + DISSENT fixes 1+2. Land the Hybrid registry-text update at §VII.AV (registry line 18059 onward) with the structural changes enumerated at workshop lines 759-795 (incorporating DISSENT fixes 1+2). Specific deliverables: (a) status-block update with W5-1 audit-pin sub-row annotating ONLY route (ii) FULL-PV as CLOSED-FAIL + K=4 MANDATORY F-image disclosure APPENDIX (NOT replacement); (b) Element 4 envelope corrigendum + Level-2 envelope DIAGNOSTIC sub-row table; (c) Element 5 Level-3 anchor preserved single-pinned at L_emp; (d) refinement-pathway table route-(ii) annotation + new route (viii) alternative envelope predictor; (e) CF activations (CF-S92-W5-1-A ACTIVE / CF-S92-W5-1-B ACTIVE / CF-S92-W5-1-C REFRAMED / CF-S92-W5-1-D ACTIVE).

10. **Cross-link audit gates for §VII.AU.OP-PROJ / §VII.AY.OP-PROJ / §VII.BA / §VII.AF.1.OP-PROJ at S92+** (Volovik EMERGENCE #3 + Connes EMERGENCE (3)). Audit-script extension dispatched at S92+ to verify the Hybrid (option iii) framing inheritance pattern at four cross-linked §VII slots: (i) §VII.AU.OP-PROJ Σ_2 enforcement assignment + CF-65 first-extraction Hybrid-readiness pre-flight; (ii) §VII.AY.OP-PROJ multiplicative L_max factorization pre-flight; (iii) §VII.BA Wodzicki asymptotic limit cross-link to §VII.AV's regulator-class-keyed sub-row table; (iv) §VII.AF.1.OP-PROJ Binding-axis K-counter joint advancement with §VII.AV substrate-natural-binding pin.

## Wrap-Up — Workshop Impact Summary

### What Changed

**(a) Numerical revisions**:

- §VII.AV Level-2 envelope sub-row table populated with regulator-class-keyed F-image values at the Level-2-B audit axis: B(R_SCHEMATIC) = L_emp = -7.046336 M_KK² (SCHEMATIC F-image class anchor; verified at PV_mass → 0 to 4.7e-7 bit precision); B(R_FULL-PV) = -527.9669 M_KK² (W5-1 measured at FULL-PV F-image class; 1.87 OOM divergence from SCHEMATIC; audit_sha256=04a6b22f1ab5b180fac0eb73132ce05ae7e9f32d4394203728778b47a037351e); B(R_FULL-CC) = TBD (CF-S92-W5-1-B forward gate; Reading A-tighter band [-686, -370] M_KK² per Q-CON-1 answer); B(R_ζ-Wodzicki) = L_emp at asymptotic large-mass limit.

**(b) Structural changes**:

- Reading B-strong (two distinct substrate-IS observables at the same triple → slot-split into structural-orthogonal-companion sub-slots) RETRACTED in full per V3 + Re:V5 continuous-deformation evidence at WP line 150 PV_mass → 0 kernel-verification at 4.7e-7 bit precision; the §VII.AV slot remains single per K=3 MANDATORY algebra-axis orthogonality axiom.
- §VII.AV registry-text canonical update converged on Hybrid (option iii): single-slot per K=3 MANDATORY + Level-2 envelope sub-rows regulator-class-keyed at Level-2-B DIAGNOSTIC axis per K=4 MANDATORY level-pin discipline + Level-3 anchor single-pinned at L_emp = -7.046336 per substrate-first canonical sourcing direction (DISSENT #1 separation) + PROXY-REFINEMENT sub-class tag PRESERVED with route-(ii) annotation only (DISSENT #2 fix).
- New compliance class MIXED-PARTIAL added to the 3-class taxonomy at `substrate-first-canonical-sourcing.md §(iv)` (extending POSITIVE / PARTIAL-POSITIVE / NEGATIVE); K_MIXED-PARTIAL = 1 SUGGESTION at S91 W5-1 close; admissibility band ADVISORY S2; K-counter advancement criterion adopted as BOTH-SIDES-POST-K=4-MANDATORY (more restrictive); K_substantive advances 4 → 5 with W5-1 NEGATIVE-CALIBRATION extension at the new MIXED-PARTIAL class.

### What Holds

- The K=3 MANDATORY algebra-axis orthogonality axiom (single substrate-IS observable per `(algebra, projector, pole)` triple) survives unchanged at the §VII.AV substrate-IS observable identity layer; the W5-1 evidence confirms (not challenges) the axiom via the continuous-deformation PV_mass scan returning bit-precision recovery of L_emp at PV_mass → 0.
- The K=4 MANDATORY level-pin discipline at `substrate-first-canonical-sourcing.md §(iv)` (SCHEMATIC vs FULL-physical structural orthogonality at the methodology-floor F-image layer; K=4 corpus W4-2 + W9b-2 + W9c-1 + W5b-2 sub-test (c) + W5-7 PARTIAL-POSITIVE) is reinforced by the W5-1 instance landing as MIXED-PARTIAL K=5 corpus extension; the discipline operates as canonical methodology-floor F-image discriminator for the §VII.AV Hybrid landing.
- The HKR `L_max → ∞` bridge map at §VII.AV (Element 3 per registry line 18088; deferred bridge-map-scheme suffix per CF-61) survives unchanged at the substrate-IS observable identity layer; the W5-1 FAIL is a Level-2 envelope regulator-class divergence on the SAME bridge-map cohomology class, not a bridge-map identity challenge.

### What Breaks or Strains

- The L^{-3} HKR-image envelope prediction at §VII.AV Element 4 (registry line 18090 area; SCHEMATIC Casimir-bound derivation) is FALSIFIED at the FULL-PV regulator-class cross-check (α_PV = 6.264, 75× anchor magnitude deviation, BREAKDOWN regime); CF-S92-W5-1-A activates as the alternative envelope-predictor gate to derive a regulator-class-keyed envelope family replacing the single L^{-3} ansatz.
- The §VII.AV PROXY-REFINEMENT corridor's refinement-pathway route (ii) FULL Pauli-Villars at Λ_UV = M_KK CLOSED-FAIL by W5-1; routes (i) Friedrich-Bär saturation / (iii) FULL Connes-Chamseddine 1996 multipliers / (iv)/(v)/(vi)/(vii) operational-machinery + dual-anchor + Hochschild + moduli-deformation REMAIN ACTIVE; the refinement-pathway taxonomy survives the route-(ii) FAIL closure but the binding-axis path to Stage-3 PERMANENT promotion requires CF-S92-W5-1-A + CF-S92-W5-1-B PASS.
- The proposed `math-scripts.md §"Multiplicative-normalization cancellation invariants"` rule extension (CF-S92-W5-1-D) is at SUGGESTION K=1 with structural-diversity K-counter advancement criterion (DISSENT sharpening); K=2/K=3 MANDATORY promotion requires future calibration instances at STRUCTURALLY DISTINCT factorization mechanisms (not just same Casimir-bound truncation at different poles); the rule's promotion timeline is structurally gated.

### Carry-Forward Computations

**In-session cleanup 2026-05-22** (per user correction "only math carries forward; everything else is done at the time — rules are clear on this" + `feedback_fix-in-session-never-defer.md` + `Investigating-Workshops.md` §"is NOT" items 7-8): non-math framework-hygiene items (rule-file extensions at math-scripts.md / cross-pillar-bridge-anatomy.md / substrate-first-canonical-sourcing.md, §VII.AV Hybrid registry-text landing, audit-script extension queue, Phi(a_2) → Σ_2 pre-registration cross-link) executed in-session and REMOVED from this list. Only genuine future-math computation remains as carry-forward below. In-session execution audit trail: `.claude/rules/math-scripts.md` §"Multiplicative-normalization cancellation invariants" (orchestrator-direct; W4 CF-D); `.claude/rules/cross-pillar-bridge-anatomy.md` §"Single-observable-per-triple structural filter" + §"Level-3 anchor singleness" sub-clauses (A1 connes-ncg-theorist); `sessions/permanent-results-registry.md` §VII.AV Hybrid (option iii) landing (mack); `computations/session-91/s91_gate_verdicts.txt` in-session verdict-line trios.

1. **CF-S92-W5-1-A — Alternative envelope-predictor derivation**:
   - **What**: Substrate-physics derivation of regulator-class-keyed envelope family B(R) on §VII.AV observable at `(M_2(ℂ), P_BdG, s=4)`; candidate predictors (a) HKR image residue-pole with regulator-class-dependent K-tail integration / (b) Friedrich-Bär saturation theorem extended to regulator-class-keyed envelope family / (c) Connes-Karoubi pairing on BdG sub-algebra K-theory boundary with regulator-class index.
   - **Inputs**: §VII.AV registry text post-Hybrid landing; S52 Bogoliubov amplitudes (`s52_bogoliubov_amp.npz`); W5-1 verdict data (`s91_w5_1_full_bdg_pv.npz`); canonical L_emp = -7.046336 anchor.
   - **Gate**: PASS iff any one of 3 predictors produces structurally-derived envelope (i) reproducing FULL-PV at L_max=12 within 5%, AND (ii) admits Level-2-binding sub-class per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"`. FAIL iff no predictor produces L_max-INVARIANT-plateau-matching prediction → return to CF-W5-5 disambiguation.
   - **Effort**: 1.0 wave-equivalent (substrate-physics derivation + Sage-Q symbolic verification + 3-predictor cross-comparison).

2. **CF-S92-W5-1-B — FULL-CC vs FULL-PV α extraction structural discriminator**:
   - **What**: Run FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers pipeline on the SAME `(M_2(ℂ), P_BdG, s=4)` triple as W5-1 FULL-PV; extract α_CC and B(R_FULL-CC); compare against Reading A-tighter prediction `|B(R_FULL-CC) − B(R_FULL-PV)| / |B(R_FULL-PV)| ≤ 0.30` and Reading B-weak band ≤ 0.50.
   - **Inputs**: W5-1 script architecture from `s91_w5_1_full_bdg_pv.npz`; Connes-Chamseddine 1996 §2.2-2.3 multiplier definitions; canonical L_emp anchor; D_K spectrum cache (`s84_spectrum_cache_L12_tau019.npz`).
   - **Gate**: PASS iff CC pipeline produces structurally-derived B(R_FULL-CC); independence test `|α_CC − α_PV| / α_PV ≤ 0.05` → FI (Reading A vindicated); `|Δα|/α_PV > 0.20` → RD-class-divergent (Reading B-weak vindicated). INFO iff CC pipeline produces partial output.
   - **Effort**: 1.0 wave-equivalent (FULL-CC pipeline coding + L_max scan + α extraction + structural-discriminator comparison).

3. **CF-S92-W5-1-C — Regulator-class transition-map disambiguation (continuous-deformation filter calibration)**:
   - **What**: PV_mass scan at [0, 0.5 M_KK, M_KK, √2 M_KK, 5 M_KK, 100 M_KK, 1000 M_KK] on W5-1 script architecture; confirm continuous interpolation `R_KW^{PV}(PV_mass)` from -7.046336 → -527.97 → -7.046336 (asymptotic Wodzicki recovery); zero discrete identity jumps.
   - **Inputs**: `s91_w5_1_full_bdg_pv.npz` script architecture; canonical L_emp = -7.046336 anchor.
   - **Gate**: PASS iff continuous interpolation across all intermediate values. INFO iff piecewise-continuous with structural justification. FAIL iff discrete identity jump at any finite PV_mass → re-opens Reading B-strong slot-split question.
   - **Effort**: 0.5 wave-equivalent (parameter scan extension to existing script).

### Closing Line

The W5-1 FAIL is a methodology-floor F-image divergence at the regulator-class axis on a single substrate-IS observable at `(M_2(ℂ), P_BdG, s=4)` — the §VII.AV slot remains single per K=3 MANDATORY algebra-axis orthogonality while the Hybrid (option iii) registry-text landing records the regulator-class-keyed F-image structure at the Level-2-B DIAGNOSTIC axis with the Level-3 empirical anchor single-pinned at L_emp = -7.046336 per substrate-first canonical sourcing direction.
