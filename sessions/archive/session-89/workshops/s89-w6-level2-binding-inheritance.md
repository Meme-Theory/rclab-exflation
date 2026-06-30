# Session 89 Workshop: lizzi x connes — Level-2-Binding Inheritance Adjudication

**Date**: 2026-05-12
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: lizzi (lizzi-spectral-functional-theorist), connes (connes-ncg-theorist)

**Source Documents**:
- `sessions/archive/session-89/session-89-w5-workingpaper.md` (§W5-3 line 528; §W5-4 line 863; §W5-6 line 1471)
- `sessions/permanent-results-registry.md` (§VII.AF.1.OP-PROJ baseline; §VII.AV / §VII.AU forward slots)
- `.claude/rules/cross-pillar-bridge-anatomy.md` (§"Level-2-binding" MANDATORY-at-K=3 spec; §"Level-2-non-binding" enforcement clause)
- `sessions/framework/registry/cross-pillar-bridge-corpus.md` (§1 K=2 calibration baseline)

**Focus Topics** (the four adjudication questions + cross-cutting §W5-6 analog):
1. **Adj-(a)**: Does cross-pillar-bridge-anatomy.md §"Level-2-binding" MANDATORY-at-K=3 spec admit Level-2-binding declaration for Corner-IV K-window log-derivative under §W5-3 INFO (envelope α = 5.0679 OUTSIDE [1.5, 5.0] PASS band by 1.4%; R² = 0.9244 MARGINAL; Casimir-bound Δ_eff(L_max) proxy)?
2. **Adj-(b)**: Is registry-anchor inheritance from §VII.AF.1.OP-PROJ (HP¹ cohomology in Pillar III ↔ Pillar IV HKR family) admissible for the Corner-IV K-window log-derivative observable, OR does the bridge-anatomy spec require per-observable Level-2-binding extraction?
3. **Adj-(c)**: Under §"Level-2-non-binding (FORBIDDEN for registry-PASS)" enforcement clause, does §W5-3's empirical envelope (failing predicted α = 3 by 69% with MARGINAL R²) constitute a "BARE-DECOMPOSITION convergence rate that does NOT bind Level-1", routing FWD-C2 §VII.AV to REGISTRY-INELIGIBLE pending CF-W5-3 full BdG re-derivation?
4. **Adj-(d)**: Rule-extension or calibration-corpus instance — what is the form of the rule-file diff (or §VII.AV downgrade form: REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE vs deferred-to-S90 reconstruction)?
5. **Cross-cutting**: Does the same logic apply to §W5-6 + §VII.AU FWD-C1 STAGE-1-CANDIDATE? If §VII.AV downgrades, does §VII.AU downgrade in parallel, or are the two FWD candidates structurally separable?

**Required deliverables** (per --context):
- (i) verdict on §W5-3 + §W5-4 status
- (ii) verdict on FWD-C2 §VII.AV STAGE-1-CANDIDATE status
- (iii) verdict on FWD-C1 §VII.AU STAGE-1-CANDIDATE status (§W5-6 analog)
- (iv) rule-file diff (advisory or MANDATORY) to be sourced into S90 plan-freeze
- 4-field carry-forward (what / inputs / gate / effort) per `feedback_fix-in-session-never-defer.md` at end of EACH round

**Substrate framing reminder**: Cross-pillar bridges flow `Substrate (Pillar A) IS [substrate-IS observable] → Bridge map (HKR / K-theory) → Laboratory (Pillar B) IN [laboratory-IN observable]`. The Corner-IV K-window log-derivative IS substrate-IS at the BdG sub-algebra; the laboratory-IN partner pillar is the cosmological-anchor (FWD-C2). Reading the empirical α = 5.07 as a property of "the substrate moving through L_max-coordinate space" is container-thinking; the L_max axis IS the substrate's regulator-truncation parameter, not a coordinate on an external container.

---

## Round 1 — lizzi: Opening Steelman (Registry-Anchor Inheritance Reading)

> **Position to steelman**: Level-2-binding inherits from registry-level §VII.AF.1.OP-PROJ HKR anchor; proxy-α = 5.07 is a SCHEMATIC artifact of the Casimir-bound Δ_eff(L_max) reconstruction (structurally too aggressive); HKR map identification is registry-anchored INDEPENDENT of this gate's α-extraction precision.

### L1: Adj-(a) — Level-2-binding admissibility under §W5-3 INFO

The §"Level-2-binding (admissible for registry-PASS)" sub-clause at `.claude/rules/cross-pillar-bridge-anatomy.md` lines 42-46 specifies, verbatim:

> "**Definition**: the algebraic envelope `L^{-α}` is the convergence rate of an HKR-image (Hochschild-Kostant-Rosenberg map) that BINDS the Level-1 cohomology class. Operationally, the envelope bounds `‖HKR(c_L) − c_continuum‖` where `c_L` is the substrate-IS finite-L cocycle / Hochschild moment / spectral-triple invariant and `c_continuum` is the HKR-image realized as the laboratory-IN continuum observable on the partner pillar."

The operative criterion is the existence of an HKR map identifying the substrate-IS finite-L cocycle with the laboratory-IN continuum image. The α value is a STRUCTURAL PREDICTION (per §"Level 2" line 22: "L_max-dependent; algebraically derived; refines with L-scan"), distinct from a STRUCTURAL THEOREM. Level 1 (line 13-18) is the cohomology-class identity at the regulator-invariant axiom level; Level 2 is a CONVERGENCE RATE on the binding of that identity under the HKR `L_max → ∞` map; Level 3 is empirical satisfaction at canonical L_max.

For the Corner-IV K-window log-derivative observable under §W5-3 INFO, the substitution chain reads (per `math-scripts.md §"Double-Check Logic"`):

- **Step 1** (definition). The substrate-IS observable IS `L(L_max) := d² ln P_GGE / d(ln K)² |_{K_horizon}` on `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})` — a finite-L Hochschild-pairing class with image in the K-window expansion of the GGE occupation variance (§W5-3 lines 615-620).
- **Step 2** (definition). HKR is the canonical map sending finite-L periodic Hochschild cohomology of the truncated spectral algebra `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})` to de Rham cohomology of the continuum image, per `cross-pillar-bridge-corpus.md §1` Step 1.
- **Step 3** (substitution). The §W5-3 substrate-IS observable's L_max → ∞ image is the canonical L_emp(∞) = -7.046336474406761, verified bit-for-bit at the operational L_max=12 truncation (§W5-3 line 568: "canonical | -7.046336474406761 (S87 W2-3 / S89 W5-2 PASS bit-for-bit)"). The Pillar-IV continuum image of this canonical IS the Peotta-Törmä BZ-trace `R_geom(τ_fold) := ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` per the verbatim §VII.AF.1.OP-PROJ theorem text at `permanent-results-registry.md` line 14704.
- **Step 4** (simplification). The HKR map's existence IS THE STRUCTURAL ANCHOR of Level-2-binding; the rule text at line 45 names this as the "registry-anchored" calibration: `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` Connes-Karoubi pairing on the Jensen-deformed band-0 projector. The §W5-3 substrate-IS observable lives in the SAME Pillar III ↔ Pillar IV bridge family as §VII.AF.1.OP-PROJ (Jensen-deformed `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})` finite-L Hochschild pairing → continuum BZ-trace on Peotta-Törmä quantum-metric).
- **Step 5** (direction). Therefore the K-window log-derivative IS Level-2-binding by structural inheritance: it has an HKR `L_max → ∞` map, its continuum image is the Pillar-IV BZ-trace, and the bridge map binds Level-1 cohomology-class identity (the regulator-invariant -7.046336 anchor) to a continuum laboratory observable on the partner pillar.

The empirical α = 5.0679 and R² = 0.9244 (§W5-3 line 599, verdict text) are properties of the **proxy reconstruction** used to render the L_max scan non-degenerate. §W5-3 line 552 is explicit: "A naive L_max scan of the §W5-2 protocol is degenerate (s52 8 BdG modes are FIXED structural inputs not parameterized by L_max; L_emp(L_max) = -7.046336 EXACTLY at all L_max). To produce a substantively meaningful L_max envelope, this gate uses a **Casimir-bound Δ_eff(L_max) rescaling** as the L_max-dependent reconstruction proxy." The α extraction is a measurement of the proxy's CONVERGENCE BEHAVIOR, not of the substrate's intrinsic L^{-3} HKR-image binding rate.

The 1.4% over-band on α and the MARGINAL R² band are diagnostic of proxy-fidelity (the Δ-rescaling is "structurally too aggressive in scaling Δ alone — a full BdG re-derivation at each L_max ... would refine the α estimate", §W5-3 line 746). Neither is diagnostic of HKR-map existence. The Level-2-binding admissibility clause does NOT require the empirical α to fall within the predicted-α band; it requires the HKR map identification AND the c_continuum reference quantity in the partner pillar's continuum to be cited. Both are satisfied at §W5-3 (cross-check (d) line 811: "identified per S86 W-5 §VII.W structural anchor; THEOREM (registry-level); PASS"; substrate framing line 611: "the bridge map IS the substrate's own structural identity at L_max → ∞").

**Concrete reading**: the Level-2-binding declaration at §W5-3 is structurally admissible under the rule's own definition. The composite=INFO verdict reflects a TWO-FACTOR proxy-precision borderline (α slightly out-of-band + R² in MARGINAL band) layered on top of an unambiguously PASS Level-2-binding declaration. The two layers are structurally orthogonal: proxy α-precision is a property of the Casimir-bound reconstruction; HKR-map binding is a registry-level cohomology-class structural anchor inherited from §VII.AF.1.OP-PROJ. Conflating them is exactly the layer-conflation that the §"Two-clause separation: registry-PASS (per-entry) vs K-counter advancement (rule-level corpus)" sub-section (rule lines 279-295) was authored to prevent.

**Question for connes (must answer R1-B)**: Does the §"Level-2-binding" admissibility definition — "the algebraic envelope `L^{-α}` is the convergence rate of an HKR-image that BINDS the Level-1 cohomology class" — require the empirical α to match the predicted α at registry-PASS time, or does it require only that the HKR map exist and the c_continuum reference be defined in the partner pillar? Cite verbatim rule-text in your answer. If the latter, on what grounds would you reject the §W5-3 Level-2-binding declaration as admissible?

### L2: Adj-(b) — Registry-anchor inheritance from §VII.AF.1.OP-PROJ

The §VII.AG.1 SHARED-ANCHOR-COMPANION precedent (`cross-pillar-bridge-corpus.md §3` lines 79-110) establishes the structural mechanism by which a §VII entry can RETAIN full registry-entry status while sharing a registry-anchored HKR bridge identification with §VII.AF.1.OP-PROJ. The Hybrid Independence Test substitution chain at corpus lines 96-102 reads:

> "**Step 3** (Substitution under `(i ∨ ii ∨ iii) ∧ iv`):
>   - §VII.AG.1 substrate-IS pillar = Pillar III (T7 quotient on Jensen-deformed band-0 sector); §VII.AF.1 W-5 substrate-IS pillar = Pillar III (HP^1 cohomology on same sector). **MATCH ⇒ clause (i) FAILS.**
>   - §VII.AG.1 laboratory-IN pillar = Pillar IV (S67 cyclic-fold image); §VII.AF.1 W-5 laboratory-IN pillar = Pillar IV (Peotta-Törmä BZ-trace). **MATCH ⇒ clause (ii) FAILS.**
>   - §VII.AG.1 bridge map = HKR `L_max → ∞` modulo cyclic-fold V_4 ... is a refinement of the same HKR class, not a structurally distinct bridge map class. **REFINEMENT-NOT-INDEPENDENT ⇒ clause (iii) FAILS.**
>   - Disjunction `(i ∨ ii ∨ iii) = (FAIL ∨ FAIL ∨ FAIL) = FALSE`."

§VII.AG.1's Hybrid Independence Test composite verdict is FALSE on all four clauses; the K-counter for the Hybrid Independence Test does NOT advance. Yet — and this is the structural point — `cross-pillar-bridge-anatomy.md` line 269 is explicit:

> "Registry entries that cite the 5-IS-not-IN + 3-level discipline but FAIL the Hybrid Independence Test are formally tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` and recorded OUTSIDE the K-counter table. **They retain full registry-entry status (the bridge-anatomy declaration remains valid for cross-citation purposes)** but do NOT advance the K-counter toward the K=3 MANDATORY promotion threshold."

The precedent is: §VII.AG.1 has the same substrate-IS pillar (III), same laboratory-IN pillar (IV), and same HKR class (the cyclic-fold V_4 quotient is a REFINEMENT of W-5's HKR map, NOT a structurally new bridge map). §VII.AG.1 nonetheless lives in the registry with full anatomy declaration. The Level-2-binding declaration on §VII.AG.1's `L^{-3}` envelope at d=4 (registry text at line 14518: "convergence rate bound `L^{-3}` at d=4 (inherited from S86 W-5 §VII.AF.1 calibration corpus; Pillar III ↔ Pillar IV bridge envelope is the immediate cousin)") is inherited from §VII.AF.1.OP-PROJ at the registry-anchor level — NOT independently extracted from a Hochschild-cocycle L_max scan on §VII.AG.1's own T7 quotient observable.

**This is the inheritance mechanism**: the registry-level HKR bridge identification IS the substrate's structural claim that the Pillar III ↔ Pillar IV bridge family admits an HKR `L_max → ∞` map. Once registered at §VII.AF.1.OP-PROJ (S87 W5-1; LANDED with `STRUCTURE tag: SOURCE-DOUBLE-CITE-CO-PRIMARY`), the HKR-map-existence anchor is available for downstream §VII observables in the same bridge family WITHOUT requiring independent per-observable HKR derivation. The Level-2 envelope α value MAY be observable-specific (different §VII observables may have different L^{-α} convergence rates depending on the proxy used for the L_max scan), but the Level-2-BINDING CLASS (i.e., the existence of an HKR map binding Level-1) is registry-anchored.

**Apply this to §W5-4's §VII.AV pre-registration**. §W5-4 line 942 reads:

> "The §W5-3 (A.26) HKR bridge identification per S86 W-5 §VII.W / S87 W5-1 §VII.AF.1.OP-PROJ established Pillar III ↔ Pillar IV structural anchor (substrate-IS Hochschild-pairing on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) ↔ Pillar IV continuum BZ-trace per Peotta-Törmä quantum metric). The K-window log-derivative IS at Cell IV (substrate-distance-2 algebra-DEPENDENT state-pair functional family per §VII.U.2 4-corner classification). Per the routing rule a26_hkr_identified_TRUE → corner-iv-singleton, the FWD-C2 substrate-IS observable c-projects to Cell IV (singleton, NOT joint)."

There is a structural subtlety here that connes will surely contest: §W5-4 separately CLAIMS that FWD-C2 satisfies the Hybrid Independence Test on all 4 clauses (substrate Pillar II ≠ Pillar I; lab Pillar V ≠ Pillar II; bridge Connes-Karoubi ≠ HKR; envelope independent) — see §W5-4 lines 968-986 + §W5-4 line 1078. So FWD-C2 §VII.AV would NOT be a SHARED-ANCHOR-COMPANION to §VII.AF.1.OP-PROJ in the same sense that §VII.AG.1 is. The §W5-4 disambiguation routing explicitly classifies FWD-C2 as the "Pillar II ↔ Pillar V" bridge with bridge map = Connes-Karoubi pairing.

**My structural reading of the tension**: the c-projection from Pillar II Mellin-Barnes residue (substrate-IS at the Pillar-II abstract algebra level) DOWN TO Cell IV via the K-window log-derivative ANCHOR (a Pillar IV-canonical observable inherited from §W5-3 / A.25 / A.26) IS the inheritance mechanism. The K-window log-derivative is the SAME observable as the one anchored at §VII.AF.1.OP-PROJ's Pillar III ↔ Pillar IV bridge — it IS the c_continuum reference quantity in Pillar IV's continuum (the Peotta-Törmä BZ-trace, evaluated at the K=K_horizon window). The FWD-C2 bridge identifies Pillar II Mellin-Barnes residue's L_max → ∞ image as `passing through` this Cell IV anchor; the HKR-map-existence is inherited from §VII.AF.1.OP-PROJ; the Connes-Karoubi pairing is the FWD-C2 specific lift to Pillar V. The two registry anchors (§VII.AF.1.OP-PROJ + §VII.AV) co-exist with §VII.AV satisfying the Hybrid Independence Test for K-counter advancement, AND simultaneously inheriting the HKR-map-existence anchor at the Pillar III ↔ Pillar IV layer.

This is structurally DIFFERENT from the §VII.AG.1 case (where all four HIT clauses FAIL). §VII.AV's HIT verdict is TRUE on all four clauses, so §VII.AV genuinely advances the HIT K-counter. The inheritance I am citing is the Level-2-binding CLASS inheritance — the substrate's claim that the HKR-map exists at the Pillar III ↔ Pillar IV layer is the registry-anchor; the §W5-3 K-window log-derivative is the operationalization of that anchor at the Cell IV substrate-IS observable level; §W5-4's FWD-C2 candidate then BUILDS on this anchor by c-projecting Pillar II's Mellin-Barnes residue to the Cell IV anchor and lifting to Pillar V via Connes-Karoubi.

**Question for connes (must answer R1-B)**: §VII.AG.1 retained full registry-entry status with `L^{-3}` envelope at d=4 inherited from §VII.AF.1.OP-PROJ at the registry-anchor level, with NO independent L_max scan on the T7 quotient observable (registry text at line 14518 explicitly inherits the envelope from "S86 W-5 §VII.AF.1 calibration corpus"). On what structural grounds would you reject the parallel inheritance for §VII.AV — i.e., the inheritance of the HKR-map-existence anchor at the Pillar III ↔ Pillar IV layer, while §W5-4 SEPARATELY satisfies the Hybrid Independence Test for cross-pillar bridge K-counter advancement at the Pillar II ↔ Pillar V FWD-C2 candidate level? Does the registry-PASS criterion for §VII.AV require an INDEPENDENT per-observable Level-2 envelope extraction (i.e., a full BdG re-derivation at each L_max producing α = 3 at d=4), or does it accept registry-anchor inheritance for the binding class with proxy-precision INFO on the empirical α?

### L3: Adj-(c) — Empirical α = 5.07 vs predicted α = 3 — SCHEMATIC artifact reading

§W5-3 line 826 contains the substrate-physics derivation of why the Casimir-bound proxy gives α ≈ 5 not α = 3, verbatim:

> "Why the Casimir-bound proxy gives α≈5 not α=3. The proxy rescales Δ_eff(L_max) = Δ_static · (L_max+1)/13 — a LINEAR rescaling in L_max. The induced shift in v_K² ∝ 1/sqrt(xi² + Δ_eff²) at K=K_horizon is approximately linear in (1−f(L_max)) = (12−L_max)/13 for small deviations. Squaring the variance and taking 2nd log-derivative gives a residual envelope dominated by the LINEAR shape, not a power-law L^{-3}. The empirical α=5.07 from the log-log regression is an artifact of the quasi-LINEAR proxy structure, not a substrate-distance-3 substrate-physics finding. A substrate-distance-2 d=4 α=3 envelope would require Δ_eff(L_max) = Δ_static · (1 − C·L_max^{-3}) — which would be circular (assuming the answer)."

The §W5-3 author is honest about the proxy's structural limitation. The reconstruction proxy uses `f(L_max) = sqrt((L_max(L_max+2)+1) / (12·14+1)) = (L_max+1)/13` (line 552 + line 637) — this is a LINEAR-in-L_max rescaling of Δ alone, with the 8 BdG modes (B1+B2+B3, FIXED structural inputs from `s52_bogoliubov_amp.npz`) held constant. The full BdG re-derivation at each L_max would re-run the BCS gap equation `1/V = Σ_a 1/(2 E_a) tanh(E_a/2T)` on the L_max-truncated D_K spectrum, regenerating both `Δ` and the 8 BdG mode amplitudes (u_k, v_k, E_qp) at each L_max — yielding a substrate-physics-faithful convergence whose envelope α IS the predicted L^{-3} at d=4.

The α = 5.07 is therefore a measurement of the proxy's quasi-LINEAR convergence shape under a log-log regression — NOT a measurement of the substrate-IS observable's intrinsic L^{-3} HKR-image binding rate. The §W5-3 cross-check (f) at line 813 honestly tags this: "Predicted α ≈ 3 at d=4 | extracted α = 5.068; 1.69× predicted | INFO if 1× ≤ ratio ≤ 2×; FAIL if > 2× | INFO (proxy structural mismatch)" — the proxy-fidelity tag is structural-disclosure.

**Falsification meaning** at §W5-3 line 830 is the substrate's own structural framing:

> "The Level-2-binding declaration is structurally falsified iff: (a) the HKR `L_max → ∞` map is shown to NOT exist for the Corner-IV K-window log-derivative (would invalidate S86 W-5 §VII.W bridge calibration at the registry level); (b) the Pillar IV Peotta-Törmä BZ-trace is shown to NOT be the continuum image (would invalidate the laboratory-IN observable identification). The α-extraction precision (proxy α=5.07 vs predicted α=3) is NOT a falsifier of Level-2-binding; it's a proxy-fidelity finding."

This is the canonical statement of the proxy-fidelity-vs-binding-class separation. The Level-2-binding sub-class admissibility (per `cross-pillar-bridge-anatomy.md` lines 42-46) depends on (a) the HKR map existing and (b) the c_continuum reference being defined. Both are anchored at §VII.AF.1.OP-PROJ at the registry level. Neither is implicated by α-extraction precision under a known structurally-too-aggressive reconstruction proxy.

**The CF-W5-3 carry-forward**. §W5-3 line 832 (iii) reads:

> "Carry-forward queue gains: full BdG re-derivation at each L_max (S52 BdG machinery extension) for refined α extraction; tag = `S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`."

This carry-forward EXISTS because the registry-level Level-2-binding declaration stands INDEPENDENT of proxy α-precision. If the Level-2-binding declaration depended on the empirical α, the §W5-3 verdict would be FAIL (1.4% over band + MARGINAL R²), not INFO; and §VII.AV pre-registration at §W5-4 would be blocked. The fact that §W5-3 closes INFO with HKR=True AND §W5-4 routes to corner-iv-singleton at PASS (§W5-4 verdict line 927: "PASS -- value='outcome=corner-iv-singleton; ... hit_PASS=1; ...'") reflects the substrate's own separation of the proxy-precision question (queued for S90) from the registry-anchor question (declared INFO-PASS at §W5-3 with HKR bridge identified).

**Substrate framing on the proxy structure** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). The Casimir-bound Δ rescaling IS a Level-1 single-τ-slice substrate-IS observable — at each L_max, the substrate IS the truncated spectral triple `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})` with a rescaled BCS gap kernel weight. The HKR `L_max → ∞` map is the substrate's structural identity at the Level-2 moduli-deformation layer (per `phononic-framing.md` Level-2 calibration corpus instance #1, §VII.AE). The α-extraction is a property of the moduli-deformation curve sampled at the 7 L_max values {6, 7, 8, 9, 10, 11, 12}; the proxy choice (Δ-rescaling vs full BdG re-derivation) determines the SHAPE of the curve, but the L_max → ∞ image (canonical -7.046336474406761) is invariant under proxy choice (the L_max=12 bit-for-bit reproduction at §W5-3 cross-check (a) line 808 confirms this; both the proxy at f(12)=1.0 and the canonical converge at L_max=12).

**Schematic-vs-physical level pin** (per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4 since S88 W7b-83). §W5-3 line 578 explicitly tags the convention with the `-CASIMIR-BOUND-PROXY` suffix; the convention disclosure is structural per the rule's `(L4 honesty-disclosure)` clause analog. §W5-3 follows the level-pin discipline correctly: the proxy class is declared in the convention tag (`convention=corner-iv-k-window-lmax-scan-level-2-envelope-CASIMIR-BOUND-PROXY` at the verdict line; §W5-3 line 592) AND the substrate-physics interpretation is disclosed in the (f) section (line 826). This is the W9c-1 POSITIVE-CALIBRATION pattern from S87, applied here. The S90 carry-forward will produce the FULL physical regularization at each L_max; the §W5-3 INFO verdict is the SCHEMATIC layer's honest verdict, not a substrate-physics falsifier.

**Question for connes (must answer R1-B)**: Do you accept the substrate-physics derivation at §W5-3 line 826 — that the proxy's quasi-LINEAR rescaling of Δ alone produces a log-log envelope DOMINATED by the linear shape, NOT the substrate's intrinsic L^{-3} HKR-image rate — as a sufficient diagnostic of proxy-fidelity? If yes, on what grounds would you require the empirical α to match the predicted α at registry-PASS time, when the §"Level-2-binding" admissibility clause names the HKR-map existence (Element 3 of the 5-IS-not-IN anatomy) and the c_continuum reference identification (Element 2) as the operative criteria? If no, can you propose an alternative substrate-physics derivation of why α=5.07 should NOT be read as a proxy-precision artifact?

### L4: Adj-(d) — Proposed rule-extension or calibration-corpus instance

I propose a NEW SUGGESTION sub-clause within `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction (S88 W8-88 hardening)"` that codifies the per-bridge-family registry-anchor inheritance pattern. The proposed sub-clause sits between the existing §"Level-2-non-binding (FORBIDDEN for registry-PASS)" block (lines 48-51) and the existing §"Substitution chain + calibration corpus + audit-script extension queue + substrate framing details" pointer (lines 53-55), so the inheritance discipline is structurally located between the admissibility classification (Level-2-binding vs Level-2-non-binding) and the audit-trail downstream pointers.

#### Concrete BEFORE/AFTER patch

**BEFORE** (rule file at lines 46-55, verbatim):

```
- **Calibration #2 (W3b-15 KDE Sub-test B, S88 W-11 V.3)**: `L^{-α}` envelope on the W3b-15 KDE Sub-test B observable IS Level-2-binding by HKR-image construction (cited W3b-15 audit_sha256=`cd13d13229aeb7961e74da5cf28f5612a3d45a524124aa0b9627654fc2dfa028`; envelope evidence at `sessions/archive/session-88/session-88-w3b-workingpaper.md §W3b-15` lines 59-67). K-counter advances K=1 → K=2. Full corpus row at `sessions/framework/registry/cross-pillar-bridge-corpus.md §1`.

#### Level-2-non-binding (FORBIDDEN for registry-PASS)

- **Definition**: the algebraic envelope `L^{-α}` is a bare-decomposition convergence rate that does NOT bind Level-1. Operationally, the envelope bounds `‖c_L − c_∞‖` where `c_∞` is a substrate-internal limit (e.g., a bare Mellin truncation `Tr(D_K^{-2s})`) WITH NO HKR image to a continuum laboratory observable on the partner pillar.
- **Counter-example pattern**: a `L^{-α}` envelope on `Tr(D_K^{-2s})` evaluated at substrate-distance pole s ∈ {3, 4, ...} that lacks an HKR image to a continuum lab observable. Such an envelope describes substrate-internal Mellin-truncation convergence; it does NOT describe the convergence of any cross-pillar bridge map. The `c_continuum` reference quantity is undefined for this envelope class.

#### Substitution chain + calibration corpus + audit-script extension queue + substrate framing details
```

**AFTER** (rule file with new sub-clause inserted between the existing two):

```
- **Calibration #2 (W3b-15 KDE Sub-test B, S88 W-11 V.3)**: `L^{-α}` envelope on the W3b-15 KDE Sub-test B observable IS Level-2-binding by HKR-image construction (cited W3b-15 audit_sha256=`cd13d13229aeb7961e74da5cf28f5612a3d45a524124aa0b9627654fc2dfa028`; envelope evidence at `sessions/archive/session-88/session-88-w3b-workingpaper.md §W3b-15` lines 59-67). K-counter advances K=1 → K=2. Full corpus row at `sessions/framework/registry/cross-pillar-bridge-corpus.md §1`.

#### Level-2-binding inheritance from registry anchor (S89 W6 hardening)

> **Provenance**: S89 W6 workshop §"L4" (lizzi-spectral-functional-theorist; CO-AUTHOR connes-ncg-theorist if R3 converges). Closes the per-observable independent-extraction false-FAIL pathway by which a §VII entry whose substrate-IS observable lives in a bridge family with a registry-anchored HKR map could be REJECTED at registry-PASS time on grounds of empirical α-extraction precision under a known-SCHEMATIC proxy reconstruction.

When a substrate-IS observable lives in a bridge family whose HKR map identification is registry-anchored at a prior §VII entry (e.g., §VII.AF.1.OP-PROJ for the Pillar III ↔ Pillar IV family), the Level-2-binding declaration MAY be inherited from the registry anchor REGARDLESS of the per-observable empirical α-extraction precision, PROVIDED:

(a) The per-observable HKR map identification (Element 3 of the IS-not-IN anatomy per §"IS-not-IN Anatomy (5 elements)" lines 93-111) is explicitly cited at plan-freeze, with the registry-anchor §-reference (e.g., "§VII.AF.1.OP-PROJ Pillar III ↔ Pillar IV HKR `L_max → ∞` map") named verbatim in the entry's Element-3 block.

(b) The per-observable c_continuum reference (Element 2 of the IS-not-IN anatomy) is the SAME continuum image as the registry anchor's Element 2 — i.e., the inheriting observable's L_max → ∞ image factors through the registry-anchor's bridge map at the same partner-pillar continuum observable (e.g., both observables resolve to the Pillar IV Peotta-Törmä BZ-trace `∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k`).

(c) The Level-3 empirical anchor is reported at the inheriting observable's own canonical L_max (typically L_max = 10 or 12), AND the proxy-reconstruction class (if any) is honestly disclosed in the verdict-line `convention=` field per `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` SCHEMATIC-vs-physical level pin discipline.

(d) The Level-2 envelope's empirical α extraction is reported alongside the inherited binding class; if the empirical α falls outside the predicted-α band (e.g., 1.4% over band, MARGINAL R² band) under a known-SCHEMATIC proxy, the verdict closes INFO (NOT FAIL) and a refinement carry-forward is queued for a FULL physical re-derivation at each L_max.

**Calibration**: §W5-3 Corner-IV K-window log-derivative under Casimir-bound Δ_eff(L_max) = Δ_static · (L_max+1)/13 proxy reconstruction (verdict `S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE: INFO` audit_sha256=`2943d4072574e062fbff3ab389830b2e42dc4a1b9bf43d0c2e5ad8fd1f6e81a2`; α = 5.0679; R² = 0.9244; HKR identified per registry anchor §VII.AF.1.OP-PROJ). Refinement carry-forward queued: `S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`. §W5-4 `S89-FWD-C2-OBSERVABLE-DISAMBIGUATION: PASS` (audit_sha256=`2eeb881b16b66298f87e486debd7e91d2d070c1ffe9bdb41a7bf54e51c623db5`) and §W5-6 `S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL: INFO` (audit_sha256=`273efb4b4e24e07bc372812cd53537a95afef9d268e41590109966ee5284cc67`) extend the corpus via downstream consumption.

**Status**: SUGGESTION at K=1 (S89 W6 W6 calibration baseline). Promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter threshold.

**Cross-corner co-primary check (preserved)**: this inheritance sub-clause does NOT relax the §"Algebra-axis orthogonality K-counter" MANDATORY-at-K=3 prohibition on cross-corner co-primary structures (parent rule lines 315-323). The inheriting observable and the registry anchor MUST live in the same algebra-axis cell, OR the inheritance routes through an explicit c-projection from one cell to another (per §W5-4 `outcome=corner-iv-singleton` c-projection from Pillar II Mellin-Barnes residue to Cell IV via the K-window log-derivative anchor; the c-projection IS the inheritance mechanism, not a violation of the cross-corner prohibition).

#### Level-2-non-binding (FORBIDDEN for registry-PASS)

- **Definition**: the algebraic envelope `L^{-α}` is a bare-decomposition convergence rate that does NOT bind Level-1. ...
```

**Cross-link to §"Audit at plan-freeze" (extension)**:

The audit at plan-freeze (parent rule lines 233-242) is extended with a new item 5b (sub-item to existing item 5 from §"Cross-link to §'Audit at plan-freeze'" at parent rule lines 67-74):

```
5b. If Level-2-binding declared via registry-anchor inheritance per §"Level-2-binding inheritance from registry anchor" (S89 W6 hardening): the registry-anchor §-reference MUST be cited verbatim in the Element-3 block AND the partner-pillar c_continuum reference MUST match the registry anchor's Element-2 verbatim. Missing either route to plan-freeze halt with remediation request.
```

**Audit-script extension queue**:

`computations/_shared/_cross_pillar_bridge_audit.py` (S86 W-5 AUDIT-1 SCAFFOLD; extended at S88 W7a-73 for OE-form; extended at S89 W6 hardening for inheritance) gains a new sub-check: regex-detect the `inherits-Level-2-binding-from-§VII\.[A-Z]+(\.[A-Z0-9-]+)*` pattern in the entry's Element-3 block; cross-reference the cited §-anchor's existing Element-2 c_continuum text; FAIL if the c_continuum text does not match.

#### Why this codifies §W5-3 / §W5-4 / §W5-6 rather than introducing new physics

The inheritance pattern is already operative in the framework (§VII.AG.1 inherits `L^{-3}` envelope from §VII.AF.1.OP-PROJ registry-anchor at line 14518 of `permanent-results-registry.md`). This SUGGESTION sub-clause formalizes the operative pattern as a rule-file convention; it does not add new physics. The K=1 calibration corpus instance (§W5-3 + §W5-4 + §W5-6 trio) provides the first explicit registration of inheritance; K=2 and K=3 instances will accumulate as future S90+ bridge candidates land at the Pillar III ↔ Pillar IV layer (each new substrate-IS observable in this family inherits the same registry anchor).

**Question for connes (must answer R1-B)**: Is the proposed sub-clause's structure (Provenance / Definition / Calibration / Status / Cross-corner check preservation) properly aligned with the parent rule's existing §"Level-2 Layer Distinction" sub-clause structure (lines 36-74)? Or do you propose an alternative form (e.g., a separate `§"Level-2 inheritance"` top-level sub-section co-equal with §"Level-2-binding" / §"Level-2-non-binding", versus the nested sub-clause I have proposed)? Cite the §-anchor where you would place the diff.

### L5: Cross-cutting — §W5-6 + §VII.AU FWD-C1 parallel analysis

§W5-6 (lines 1471-1789) is the FWD-C1 retry that pre-registers §VII.AU at STAGE-1-CANDIDATE. The structural pattern under my reading is even cleaner than §W5-4's §VII.AV inheritance, because §W5-6 inherits the Level-2 envelope α=3 from the L^{-3} HKR template at d=4 WITHOUT performing any L_max scan extraction at the FWD-C1 substrate-IS observable level. §W5-6 line 1511 reads, verbatim from the machinery pin table:

> "envelope_alpha_predicted | 3 (Level-2 L^{−3} at d=4)"

This is template-inheritance: the FWD-C1 Level-2 envelope IS the L^{-3} template structural-exact, NOT an extracted proxy value. §W5-6 does no L_max scan; it asserts the structural-exact envelope inherited from the W-5 calibration template. The §VII.AU registry slot pre-registration at §W5-6 line 1745-1746 reads:

> "proposed_registry_slot | **§VII.AU** | FWD-C1 STAGE-1-CANDIDATE pre-registration target
> proposed_stage_tag | **STAGE-1-CANDIDATE** | per joint-theorem-promotion.md Stage 1 of 4"

The structural identification is at §W5-6 lines 1502-1518: bridge map = HKR (Hochschild-Kostant-Rosenberg) per cross-pillar-bridge-anatomy.md FWD-C1 candidate. Level-3 anchor is `n_s_FW_exact = Fraction(9561, 10000)` (canonical_constants.py:1681; bit-exact rational per Route-B identity from S88 W-15 W4c-36). The substitution chain Step 5 (§W5-6 line 1614-1631) reads, with substituted numbers:

> "n_s_recomputed_substrate_IS = 1 - 2 * eps_FW * (c_sub_baseline / c_sub_corrected)
>                             = 1 - 2 * 0.02195 * (2.238 / 2.238)
>                             = 1 - 2 * 0.02195
>                             = 1 - 0.0439
>                             = 0.9561 EXACT  (matches n_s_FW_exact = 9561/10000 bit-precision)"

The Level-3 anchor is bit-exact by construction (Route-B identity at substrate-distance-1 Mellin pole). The slope_A canonical pin at canonical_constants.py:1719 is `slope_A_FW_Conv_A_GEOMETRIC = "10.0 / (1 - tau/(5*pi))"` (Reading-A geometric resummation); at τ_fold = 0.19 this evaluates to `slope_A_paramet = 10.1224387484` (Sage-exact `5000π/(500π − 19)`). The cross-check at §W5-6 line 1722 confirms D_max = 9.3e-15 (machine ε) against the scalar pin at line 1720, so substrate-first-provenance Class-(f) audit returns NO-ACTION (§W5-6 line 1723).

**Why §W5-6 template-inheritance is even cleaner than §W5-4 empirical-α inheritance**. §W5-3 performed an empirical L_max scan with a Casimir-bound proxy that extracted α=5.0679 (off the predicted α=3 by 1.69×, in MARGINAL R² band) — this is a proxy-fidelity finding requiring a CF-W5-3 refinement queue. §W5-6 does NOT scan at all; the Level-2 envelope is the structural-exact `L^{-3}` template inherited directly from the W-5 calibration corpus at the same d=4 substrate-distance-1 pole structure (matching the §VII.AF.1.OP-PROJ baseline at `permanent-results-registry.md` line 14704: "Convergence rate to continuum form is bounded by L^{-3} algebraic envelope at d=4").

§W5-6 line 1773 makes this inheritance explicit:

> "FWD-C1 advances the cross-pillar-bridge K-counter (already MANDATORY at K=3 per S88 W4a-17 close) by adding a structurally independent calibration instance distinct from §VII.AF.1 (Pillar III ↔ Pillar IV) AND FWD-C2 (Pillar II ↔ Pillar V; landed at §W5-4). The Hybrid Independence Test K-counter advances K=1→K=2 with this gate's structural-validation; one more PASS reaches K=3 MANDATORY status for HIT promotion (FWD-C3 candidate pending)."

So §W5-6's §VII.AU candidate satisfies the Hybrid Independence Test (all 4 clauses TRUE per §W5-6 lines 1656-1663) AND inherits the `L^{-3}` envelope template at d=4 from the registry corpus. The Planck observational distance 2.10σ (§W5-6 line 1737-1739: `|0.9561 − 0.9649|/0.0042 = 2.0952σ`) lives in the INFO band (1.5, 3.0] BY DESIGN — §W5-6 line 1647-1650 explicitly: "The 2.10σ distance is BY DESIGN: the framework's substrate-IS prediction (n_s_FW = 0.9561) intentionally differs from Planck observational (0.9649) at the 2-σ level. The FWD-C1 bridge's structural content IS this discrimination; the gap is the substrate's own claim against the Planck central value." The INFO verdict reflects the substrate-IS prediction's structural discriminator against the observational central value, NOT a proxy-fidelity issue.

**Symmetry with §W5-3 / §W5-4**. Under my reading at L1-L4 of this workshop:

- §W5-3 INFO (composite=INFO at α=5.07 proxy-fidelity borderline + MARGINAL R²) AND HKR registry-anchor identified.
- §W5-4 PASS (corner-iv-singleton; HIT all 4 clauses; 5-anatomy + 3-level + Level-2-binding sub-class explicit) AND §VII.AV STAGE-1-CANDIDATE pre-registered.
- §W5-6 INFO (composite=INFO at Planck σ=2.10 observational discriminator BY DESIGN) AND template-inheritance of `L^{-3}` envelope + HIT all 4 clauses TRUE + §VII.AU STAGE-1-CANDIDATE pre-registered.

Both §W5-4 and §W5-6 deliver registry-PASS-eligible STAGE-1-CANDIDATE entries under my reading. §W5-6's §VII.AU is cleaner because it uses template-inheritance of the structural-exact L^{-3} envelope rather than empirical-α extraction; §W5-4's §VII.AV inherits the HKR-map-existence anchor via c-projection from Pillar II Mellin-Barnes to Cell IV via the K-window log-derivative. The two inheritance modes are structurally distinct:

- **§W5-6 template-inheritance**: the Level-2 envelope IS structural-exact L^{-3} at d=4, inherited from the W-5 calibration template; no per-observable L_max scan required.
- **§W5-4 c-projection inheritance**: the Cell IV substrate-IS observable IS the K-window log-derivative anchor; FWD-C2 c-projects Pillar II Mellin-Barnes residue down to this anchor; the HKR-map-existence is inherited at the Pillar III ↔ Pillar IV layer, with Connes-Karoubi pairing as the lift to Pillar V.

Both fit naturally under the L4 proposed sub-clause `§"Level-2-binding inheritance from registry anchor"`. Both Calibration K=1 corpus instances (alongside §W5-3) feed the K=1-advisory status of the new sub-clause.

**If the workshop concludes registry-anchor inheritance is admissible, BOTH §VII.AV and §VII.AU stand as STAGE-1-CANDIDATE.** The two STAGE-1-CANDIDATE registrations would then enter the `joint-theorem-promotion.md` 4-stage pathway for Stage-2 cross-axis independent-verify dispatch (queued per §W5-4 line 1143 and §W5-6 line 1779). The HIT K-counter advances K=1→K=2 from §W5-4's PASS (per §W5-4 line 1137) AND K=2→K=3 from §W5-6's PASS (per §W5-6 line 1773) — reaching K=3 MANDATORY promotion of the Hybrid Independence Test discipline if both stand.

**If the workshop concludes registry-anchor inheritance is INADMISSIBLE** — i.e., the connes-side per-observable-extraction reading wins — then §W5-3 INFO becomes §W5-3 FAIL-equivalent (α=5.07 outside [1.5, 5.0] band; R² in MARGINAL band; Level-3 violates Level-2 envelope by ~1.69× ratio if α=5.07 is read as the Level-2 envelope rather than as a proxy-fidelity finding), and §VII.AV downgrades to REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE pending CF-W5-3 (S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX). §VII.AU FWD-C1 — being template-inheritance with structural-exact L^{-3} envelope — would be LESS affected by this conclusion, since it does not depend on the §W5-3 proxy α extraction.

**Question for connes (must answer R1-B)**: Under the per-observable-extraction reading, §VII.AU §W5-6 has Level-2 envelope α=3 declared by structural-exact template-inheritance from the W-5 calibration (no L_max scan was performed at the FWD-C1 substrate-IS observable level — §W5-6 line 1511 envelope_alpha_predicted=3 is template-asserted, not extracted). Does the per-observable-extraction reading require §W5-6 to perform an independent L_max scan on the parameterized slope_A canonical observable, or does the structural-exact L^{-3} template-inheritance suffice for FWD-C1 STAGE-1-CANDIDATE pre-registration? If the latter, why would the same template-inheritance NOT extend to §W5-4's §VII.AV (where the empirical α=5.07 is a proxy-fidelity finding under a known-SCHEMATIC Casimir-bound reconstruction)?

### L6: Round-1 carry-forward (4-field spec per `feedback_fix-in-session-never-defer.md`)

Per `feedback_fix-in-session-never-defer.md` (2026-04-18 originSession 83b1afb7-db09-469c-b0b2-804b9d8e2619), each carry-forward computation MUST have all four fields: What / Inputs / Gate / Estimated effort.

#### Carry-Forward #L6.1 — Full BdG re-derivation for refined α extraction at Corner-IV K-window log-derivative

(Already queued at §W5-3 line 832 (iii); this is the registry-side mirror under the L4 proposed sub-clause.)

- **What**: Refine the empirical envelope α extraction at the Corner-IV K-window log-derivative substrate-IS observable by performing a FULL BdG re-derivation at each L_max ∈ {6, 7, 8, 9, 10, 11, 12} instead of the Casimir-bound Δ_eff(L_max) = Δ_static · (L_max+1)/13 proxy. The full re-derivation re-runs the BCS gap equation `1/V = Σ_a 1/(2 E_a) tanh(E_a/2T)` on the L_max-truncated D_K spectrum at each L_max value (regenerating both `Δ` and the 8 BdG mode amplitudes u_k, v_k, E_qp from the truncated spectral kernel), then evaluates L_emp(L_max) via the §W5-2 numerical core. Output: refined `envelope_alpha`, `envelope_R²`, `envelope_log_A` over the 7 L_max sectors, with comparison to the §W5-3 Casimir-bound proxy α=5.0679 (proxy structural mismatch quantified as proxy-fidelity bias).

- **Inputs**:
  - `computations/session-52/s52_bogoliubov_amp.npz` (8-mode B1+B2+B3 BdG canonical amplitudes at L_max=12 reference; FIXED at L_max=12 only — at L_max < 12 the modes are RE-DERIVED, not just rescaled).
  - `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (full L_max=12 D_K spectrum cache; 90 Peter-Weyl sectors; 31,956,720 weighted eigenvalues). Per `math-scripts.md §"Machinery-Feasibility Audit"` Casimir-bound feasibility check + Friedrich-Bär saturation theorem cross-check on bottom-K observable invariance.
  - `computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz` (canonical anchor L_emp(∞) = -7.046336474406761 bit-for-bit per §W5-2 PASS).
  - `computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.npz` (Casimir-bound proxy α=5.0679 / R²=0.9244 reference for proxy-fidelity bias quantification).
  - canonical_constants.py: M_KK, tau_fold, Delta_BCS, M_KK-anchored BCS gap-equation parameters; n_modes_static = 8 (FIXED branch index; the L_max truncation operates on D_K spectrum, not on the BdG mode count which is fixed by the B1+B2+B3 branch index at the underlying SU(3) Peter-Weyl decomposition).

- **Gate**: `S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`. Pre-registered PASS criterion: extracted α ∈ [2.5, 3.5] (1-sigma band around predicted α=3 at substrate-distance-2 d=4 per S86 W-5 §VII.W) AND R² ≥ 0.95 (VALID band; tighter than §W5-3's MARGINAL [0.90, 0.95)) AND L_max=12 bit-for-bit anchor match (|L_emp(12) − (-7.046336474406761)| < 1e-9). INFO band: α ∈ [2.0, 2.5) ∪ (3.5, 4.5] OR R² ∈ [0.90, 0.95). FAIL: α outside [2.0, 4.5] OR R² < 0.90 OR L_max=12 anchor mismatch. The gate ALSO produces a proxy-fidelity bias estimate: `bias_factor = α_proxy / α_full_bdg = 5.0679 / α_extracted`, reported alongside the canonical α.

- **Estimated effort**: 1 agent-session (volovik-superfluid-universe-theorist PRIMARY, lizzi-spectral-functional-theorist CO-AUTHOR for the spectral-truncation cross-check). Wall-time estimate: ~30-60 min on AMD RX 9070 XT GPU for the 7-L_max BCS gap-equation iterative self-consistent solver + Bogoliubov diagonalization at each L_max sector (Peter-Weyl block-diagonal so each sector independently small; total ≈ 31M weighted eigenvalues across 90 sectors at L_max=12, sparse Lanczos via `torch.linalg` on GPU).

#### Carry-Forward #L6.2 — Register Level-2-binding inheritance sub-clause + extend audit-script

- **What**: Land the proposed sub-clause `§"Level-2-binding inheritance from registry anchor" (S89 W6 hardening)` at `.claude/rules/cross-pillar-bridge-anatomy.md` between existing §"Level-2-binding (admissible for registry-PASS)" line 46 (W3b-15 Calibration #2 closing line) and §"Level-2-non-binding (FORBIDDEN for registry-PASS)" line 48. Concrete BEFORE/AFTER patch text per L4 above. SUGGESTION status at K=1 with calibration corpus = {§W5-3 + §W5-4 + §W5-6 trio at S89 W6 close}. Promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md`. Extend `computations/_shared/_cross_pillar_bridge_audit.py` with a new sub-check: regex-detect `inherits-Level-2-binding-from-§VII\.[A-Z]+(\.[A-Z0-9-]+)*` pattern in Element-3 block + cross-reference cited §-anchor's Element-2 c_continuum text. METHODOLOGY-class per `wave-classification.md §M4` (gate-ID must be appended to `methodology-wave-allowlist.md` with computed `sha256_of_plan_block`); orchestrator-only-edit per the recursion-attack closure.

- **Inputs**:
  - `.claude/rules/cross-pillar-bridge-anatomy.md` (parent rule file; 323 lines; current state at S89 W6 close).
  - `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (Level-2 Layer Distinction calibration corpus extension target for the K=1 advisory entry).
  - `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ` (the registry-anchor whose HKR map identification is the inheritance source).
  - `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` (this workshop's R3 verdict text as the substitution-chain provenance).
  - `computations/_shared/_cross_pillar_bridge_audit.py` (audit script to extend).
  - `.claude/rules/methodology-wave-allowlist.md` (append gate-ID with computed sha256_of_plan_block).

- **Gate**: `S90-LEVEL-2-BINDING-INHERITANCE-SUB-CLAUSE-LANDING` (rule-file edit gate; METHODOLOGY-class per `wave-classification.md §M4`). Pre-registered PASS criterion (per `wave-classification.md §M1`): (i) the diff is applied verbatim at parent rule lines 46-48 insertion point; (ii) the audit-script regex extension is committed with positive-match (the §VII.AF.1.OP-PROJ baseline) and negative-match (a hypothetical entry citing inheritance from a non-existent §VII.X) test cases passing; (iii) the K=1 corpus instance is logged at `cross-pillar-bridge-corpus.md §1`; (iv) the gate-ID is appended to `methodology-wave-allowlist.md` with computed `sha256_of_plan_block`. Dual-SHA closure per `gate-verdicts.md` S87+ schema-v2.

- **Estimated effort**: 0.5 agent-session (lizzi-spectral-functional-theorist solo for the rule-file diff per S89 W6 PRIMARY authorship + `cross-pillar-bridge-audit.py` audit-script extension at the regex layer; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` for the corpus row landing; orchestrator-direct-write convention path per `wave-classification.md §"Dispatch consequences"`). The landing is honest-disclosure rule-file edit per the W9c-1 positive-calibration model: the convention tag carries explicit SUGGESTION-status + K=1-advisory tag; promotion to MANDATORY waits for K=3 distinct calibration instances accumulated across S90+.

#### Note on §W5-6 / §VII.AU template-inheritance carry-forward

§W5-6 already structurally validates §VII.AU STAGE-1-CANDIDATE via template-inheritance (no L_max scan performed; envelope_alpha_predicted=3 inherited directly from W-5 calibration template at d=4 substrate-distance-1 pole structure per §W5-6 line 1511). Per the mack-cosmic-bridge sole-writer protocol (per `feedback_mack-bridge-role.md`), the §VII.AU landing in `sessions/permanent-results-registry.md` is queued for S90+ at gate `S90-VII-AU-FWD-C1-STAGE-1-CANDIDATE-MACK-LANDING` (already queued at §W5-6 line 1779 (i)); this is NOT a new carry-forward I am introducing here. I cite it only to note that the §W5-6 → §VII.AU pathway is independent of the §W5-3 → §VII.AV pathway, and my L1-L5 reading does NOT require §W5-6 to perform an L_max scan it never proposed to perform.

---

## Round 1 — connes: Response & Original Analysis (Per-Observable Extraction Reading)

### Part 1: Response to lizzi's Sections

#### Re: L1 — Adj-(a) admissibility

**DISAGREE** on the reading that the §"Level-2-binding" definition admits the §W5-3 declaration as registry-PASS-eligible at S89 W6 close.

lizzi quotes the operative definition correctly at L1 line 39 from `.claude/rules/cross-pillar-bridge-anatomy.md` lines 42-46 verbatim:

> "**Definition**: the algebraic envelope `L^{-α}` is the convergence rate of an HKR-image (Hochschild-Kostant-Rosenberg map) that BINDS the Level-1 cohomology class. Operationally, the envelope bounds `‖HKR(c_L) − c_continuum‖` where `c_L` is the substrate-IS finite-L cocycle / Hochschild moment / spectral-triple invariant and `c_continuum` is the HKR-image realized as the laboratory-IN continuum observable on the partner pillar."

The operational form of the definition is what governs admissibility — not the bare existence of an HKR map at some level of abstraction. The rule names `c_L` with a subscript `_L` because the envelope is per-observable: the bound is on `‖HKR(c_L) − c_continuum‖` for the SPECIFIC substrate-IS observable being studied. The Hochschild-cohomology pairing on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` is a per-cocycle construction; HKR maps periodic Hochschild cohomology to de Rham cohomology element-by-element (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula). The envelope describes the convergence RATE of the HKR image of one particular cocycle class — not a family-wide existence claim.

The §W5-3 empirical α=5.0679 does not bound `‖HKR(c_L) − c_continuum‖` for the K-window log-derivative observable. It bounds the convergence of the **Casimir-bound Δ_eff(L_max) = Δ_static · (L_max+1)/13 proxy reconstruction** to its L_max=12 anchor. The proxy is a quasi-LINEAR rescaling of the BCS gap parameter alone; the 8 BdG mode amplitudes (u_k, v_k, E_qp) are held FIXED at L_max=12 values (§W5-3 line 552: "s52 8 BdG modes are FIXED structural inputs not parameterized by L_max"). The α-extraction therefore measures the proxy's quasi-LINEAR shape under log-log regression, NOT the substrate's HKR-image binding rate.

This is precisely the diagnostic signature of Level-2-non-binding per the rule's own definition at lines 48-51:

> "**Definition**: the algebraic envelope `L^{-α}` is a bare-decomposition convergence rate that does NOT bind Level-1. Operationally, the envelope bounds `‖c_L − c_∞‖` where `c_∞` is a substrate-internal limit (e.g., a bare Mellin truncation `Tr(D_K^{-2s})`) WITH NO HKR image to a continuum laboratory observable on the partner pillar."

What does `‖c_L − c_∞‖` map to in the §W5-3 case? `c_L` is the K-window log-derivative evaluated under the proxy at truncation L_max ∈ {6,...,12}; `c_∞` is the proxy's limit at f(L_max → ∞) (not the substrate's HKR-image; the proxy does not have an HKR continuation in the sense of the rule). The proxy convergence describes the substrate's internal evolution under a Casimir-bound rescaling rule — IT DOES NOT describe HKR-image binding to the Pillar IV Peotta-Törmä BZ-trace.

**On the lizzi question at L1 line 57**: the §"Level-2-binding" admissibility definition does NOT require the empirical α to match the predicted α at registry-PASS time — but it DOES require the empirical α to describe `‖HKR(c_L) − c_continuum‖` for the OBSERVABLE the bridge entry registers. The §W5-3 empirical α=5.07 describes a different quantity (proxy reconstruction convergence). lizzi's argument conflates two distinct rates: (i) the HKR-image binding rate for the K-window log-derivative observable (which has never been empirically extracted at S89 W6 close), and (ii) the Casimir-bound proxy's quasi-LINEAR convergence rate (which IS what α=5.07 measures). The Level-2-binding declaration would require (i); §W5-3 provides only (ii).

The enforcement-clause direction at rule lines 63-64 is unambiguous:

> "- IF Level-2-binding ∧ (Level-3 < Level-2 envelope at canonical L_max) → registry-PASS ELIGIBLE (other audit clauses still apply).
> - IF Level-2-non-binding (regardless of Level-3 vs Level-2 numerical comparison) → registry-INELIGIBLE; the bridge entry is registry-incomplete and routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum` reference quantity in the partner pillar's continuum."

§W5-3's empirical envelope under the Casimir-bound proxy is Level-2-non-binding in the rule's operative sense; the entry is registry-INELIGIBLE pending CF-W5-3 full BdG re-derivation. The §W5-3 INFO verdict (composite=INFO; magnitude=FAIL; regime=MARGINAL) is the CORRECT honest disclosure that the SCHEMATIC proxy cannot deliver registry-PASS-eligibility at S89 W6; that disclosure does NOT promote the entry to registry-PASS-eligible by separately citing the §VII.AF.1.OP-PROJ baseline (which anchors a DIFFERENT observable; see C3 below).

**Substrate framing**: per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`, the substrate IS the L_max-truncated spectral triple at moduli-deformation Level-2. The HKR map IS the substrate's own structural identity at L_max → ∞. The empirical envelope under the Casimir-bound proxy is a measurement of the proxy's substrate-internal trajectory under Casimir-bound rescaling — it is NOT a measurement of the substrate's HKR-image binding rate for THIS observable. Registry-PASS-eligibility at the Level-2-binding sub-class admissibility test requires per-observable extraction of the HKR-image binding rate; SCHEMATIC proxy reconstructions cannot substitute.

#### Re: L2 — Registry-anchor inheritance argument

**DISAGREE** on three structurally distinct grounds. The §VII.AG.1 "precedent" lizzi invokes does not carry the burden she places on it; the c-projection inheritance mechanism she names is the structurally-FORBIDDEN cross-corner co-primary pattern under a different label; and §W5-4 contains a substrate-IS observable identity inconsistency at the 5-anatomy declaration that her argument depends on to function. I take these in order.

**(i) §VII.AG.1 is NOT a precedent for K-counter-advancing Level-2-binding inheritance.**

lizzi's L2 cites §VII.AG.1 as the structural mechanism by which a §VII entry can RETAIN registry-entry status while inheriting an HKR bridge identification at the registry-anchor level (line 73 reading the SHARED-ANCHOR-COMPANION clause at `cross-pillar-bridge-anatomy.md` line 269). The reading is correct AS TO §VII.AG.1's status — it retains registry-entry status for cross-citation purposes — but the inference she draws from it is structurally inadmissible.

Per `cross-pillar-bridge-corpus.md §3` lines 96-102, the §VII.AG.1 Hybrid Independence Test substitution chain reads:

> "**Step 3** (Substitution under `(i ∨ ii ∨ iii) ∧ iv`):
>   - §VII.AG.1 substrate-IS pillar = Pillar III (T7 quotient on Jensen-deformed band-0 sector); §VII.AF.1 W-5 substrate-IS pillar = Pillar III (HP^1 cohomology on same sector). **MATCH ⇒ clause (i) FAILS.**
>   - §VII.AG.1 laboratory-IN pillar = Pillar IV (S67 cyclic-fold image); §VII.AF.1 W-5 laboratory-IN pillar = Pillar IV (Peotta-Törmä BZ-trace). **MATCH ⇒ clause (ii) FAILS.**
>   - §VII.AG.1 bridge map = HKR `L_max → ∞` modulo cyclic-fold V_4 ... is a refinement of the same HKR class, not a structurally distinct bridge map class. **REFINEMENT-NOT-INDEPENDENT ⇒ clause (iii) FAILS.**
>   - Disjunction `(i ∨ ii ∨ iii) = (FAIL ∨ FAIL ∨ FAIL) = FALSE`."

§VII.AG.1 retained registry-entry status PRECISELY BECAUSE it failed all 4 HIT clauses and was tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` OUTSIDE the K-counter. It does NOT advance the K-counter toward MANDATORY-at-K=3 — it is explicitly excluded from the count.

§W5-4's §VII.AV registration is the structurally OPPOSITE case: §W5-4 lines 968-986 demonstrate `(i) TRUE ∧ (ii) TRUE ∧ (iii) TRUE ∧ (iv) TRUE = HIT PASS`, AND §W5-4 SEEKS K-counter advancement explicitly ("counts toward Hybrid Independence Test K-counter advancement (K=1→K=2 path opened)", §W5-4 line 996). §VII.AV cannot simultaneously inherit the SHARED-ANCHOR-COMPANION classification (which by definition is OUTSIDE the K-counter) AND advance the K-counter; the two modes are mutually exclusive at the structural level.

lizzi anticipates this objection at L2 lines 83-85 and constructs a manufactured two-track distinction: "the Level-2-binding CLASS inheritance — the substrate's claim that the HKR-map exists at the Pillar III ↔ Pillar IV layer is the registry-anchor; the §W5-3 K-window log-derivative is the operationalization of that anchor at the Cell IV substrate-IS observable level; §W5-4's FWD-C2 candidate then BUILDS on this anchor by c-projecting Pillar II's Mellin-Barnes residue to the Cell IV anchor and lifting to Pillar V via Connes-Karoubi."

**Where is this two-track distinction in the rule text?** The only documented two-clause separation in the parent rule is at `cross-pillar-bridge-anatomy.md` lines 279-295 §"Two-clause separation: registry-PASS (per-entry) vs K-counter advancement (rule-level corpus)". That separation is between (a) per-entry epistemic adequacy (Level-3 < Level-2 at canonical L_max) and (b) corpus saturation toward MANDATORY promotion of the discipline itself. It is NOT a separation between "binding-class inheritance" and "HIT K-counter advancement"; it is a separation between TWO PREDICATES (per-entry vs corpus). The rule text at line 285 reads verbatim:

> "**Per-entry registry-PASS** (§'Registry-PASS criterion' above): gates whether a single registry entry's STAGE-tag may be promoted to STAGE-3-PERMANENT under the `joint-theorem-promotion.md` 4-stage pathway. Predicate: Level-3 < Level-2 at canonical L_max. Operates on the entry's own empirical satisfaction."

The §VII.AV per-entry registry-PASS predicate operates on §VII.AV's OWN empirical satisfaction — NOT on §VII.AF.1.OP-PROJ's HKR-map-existence anchor. There is no rule-text basis for the inheritance lizzi proposes.

**(ii) Cross-corner co-primary FORBIDDEN — Kill-shot #1.**

§VII.AF.1.OP-PROJ's substrate-IS observable is the Pillar III HP¹ cohomology finite-L Hochschild pairing `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` on the Jensen-deformed band-0 projector (rule line 18, registry §VII.AF.1.OP-PROJ baseline). This is the regulator-invariant Connes-Karoubi pairing — an ALGEBRA-INVARIANT spectrum-only functional family per §VII.U.2 4-corner partition (Cell I).

The §W5-3 K-window log-derivative `L(L_max) := d² ln P_GGE / d(ln K)² |_{K_horizon}` is constructed from the Bogoliubov occupation variance `P_GGE(K) = Var_a(v_K²)` evaluated on the BdG sub-algebra. §W5-3 line 609 is EXPLICIT on its corner classification:

> "The Corner-IV K-window log-derivative at substrate-distance-2 pole s=4 is an **algebra-DEPENDENT state-pair functional** per `cross-pillar-bridge-anatomy.md §'Algebra-axis orthogonality K-counter'` MANDATORY at K=3 (since S87 W-2 R3 close); it lives on Cell IV per `permanent-results-registry.md §VII.U.2` 4-corner classification."

So the inheritance mechanism lizzi proposes carries the Level-2-binding declaration from Cell I (algebra-INVARIANT) to Cell IV (algebra-DEPENDENT). Per `cross-pillar-bridge-corpus.md §6` lines 222-225, the plan-freeze enforcement for algebra-axis orthogonality reads:

> "1. **Corner-cell declaration**: every entry declares its 4-corner cell ∈ {I, II, III, IV} explicitly per the partition table in §VII.U.2.
> 2. **Cross-corner co-primary FORBIDDEN**: SOURCE-DOUBLE-CITE-CO-PRIMARY structure tags scoping anchors across distinct corner cells fail registry-landing.md §'Detection' criterion (1) by algebra-axis orthogonality."

And `registry-landing.md` Detection item 4 reads verbatim:

> "4. **Both anchors must be on the same algebra-axis cell** (S88 W-15 V.6; B.14) per `cross-pillar-bridge-anatomy.md §'Algebra-axis orthogonality K-counter'` MANDATORY at K=3. Cross-corner co-primary structures (one anchor on the algebra-INVARIANT spectrum-only-functional cell, the other on the algebra-DEPENDENT state-pair-functional cell) are STRUCTURALLY FORBIDDEN — the two cells live on orthogonal algebra-axes and cannot enter a single non-fungible chain."

lizzi's "c-projection IS the inheritance mechanism" (L2 line 83) renames the structurally-FORBIDDEN cross-corner co-primary pattern. The inheriting observable (§W5-3 K-window log-derivative; Cell IV) and the registry anchor (§VII.AF.1.OP-PROJ HP¹ cohomology; Cell I) live on orthogonal algebra-axes per the MANDATORY-at-K=3 clause. The corpus's substrate-physics derivation at §6 line 200 forecloses precisely this inheritance:

> "the algebra-INVARIANT family (spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT family (state-pair functionals on `A`) are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level — there is no closed-form `{λ_n}`-only identity reproducing any algebra-DEPENDENT functional, and conversely no state-functional-only identity reproducing any algebra-INVARIANT spectral moment."

If the algebra-INVARIANT and algebra-DEPENDENT functional families are structurally orthogonal in identity-class membership, then the HKR-image binding rate for one CANNOT be inherited as the HKR-image binding rate for the other. The cohomology classes themselves live on disjoint algebra-axes. Inheritance of an HKR-binding declaration across cells is a clause-(4) violation per `registry-landing.md`, and is structurally rejected at plan-freeze HARD-HALT per the S89-CROSS-CORNER-CO-PRIMARY-AUDIT extension lizzi herself cites in her L4 proposed sub-clause.

The L4 §"Cross-corner co-primary check (preserved)" parenthetical (workshop line 159) reads: "the inheriting observable and the registry anchor MUST live in the same algebra-axis cell, OR the inheritance routes through an explicit c-projection from one cell to another (per §W5-4 `outcome=corner-iv-singleton` c-projection from Pillar II Mellin-Barnes residue to Cell IV via the K-window log-derivative anchor; the c-projection IS the inheritance mechanism, not a violation of the cross-corner prohibition)." This proposed carve-out has no rule-text basis. The MANDATORY-at-K=3 clause does not contain a c-projection escape hatch; it forbids SOURCE-DOUBLE-CITE-CO-PRIMARY structures whose anchors scope distinct corner cells, period. lizzi's L4 sub-clause attempts to legislate an exception to a MANDATORY rule via a SUGGESTION-status K=1 entry — which is itself a structural violation of the K-counter advancement protocol (a K=1 SUGGESTION cannot abrogate a K=3 MANDATORY clause).

**(iii) §W5-4's substrate-IS observable identity inconsistency — Kill-shot #3.**

§W5-4 contains an internal structural inconsistency at the 5-anatomy declaration that must be surfaced. §W5-4 line 898 declares in the machinery pin table:

> "FWD_C2_substrate_pillar | Pillar II (Mellin-Barnes residue)"

This matches the canonical FWD-C2 spec at `cross-pillar-bridge-corpus.md §4` (Pillar II ↔ Pillar V; Mellin-Barnes residue ↔ BdG spectral triple). FWD-C2's substrate-IS observable, by template definition, is a Pillar-II Mellin-Barnes residue — an algebra-INVARIANT spectrum-only functional on the Mellin-cone (Cell II in §VII.U.2 partition).

§W5-4's 5-anatomy Step 6 declaration at line 1011 reads:

> "1. substrate-IS observable: K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) (inherited from A.25/A.26)"

This declares the substrate-IS observable to be the K-window log-derivative — an algebra-DEPENDENT state-pair functional on the BdG sub-algebra (Cell IV per §W5-3 line 609 explicit classification).

These are two DIFFERENT observables on TWO DIFFERENT pillars in TWO DIFFERENT corner cells:

| Source | Observable | Pillar | Corner cell |
|:-------|:-----------|:-------|:------------|
| §W5-4 line 898 (machinery pin) | Mellin-Barnes residue | Pillar II | Cell II (algebra-INVARIANT) |
| §W5-4 line 1011 (5-anatomy Step 6) | K-window log-derivative | Pillar III/IV (BdG) | Cell IV (algebra-DEPENDENT) |

The 5-anatomy declaration at Element 1 is INCOMPLETE-OR-CONFUSED. lizzi's "c-projection from Pillar II Mellin-Barnes residue to Cell IV via the K-window log-derivative anchor" (L2 line 83) is precisely the structural mechanism by which this confusion was generated — the c-projection is named as the inheritance mechanism, but it produces an Element-1 declaration that names a Pillar-IV/Cell-IV observable while the bridge entry is registered as Pillar-II/Cell-II.

Under the §"Audit at plan-freeze" rules (parent rule lines 233-242 + corpus §6 lines 218-227), §W5-4 §VII.AV fails:
- Item 1 (5 IS-not-IN anatomy elements present in entry text): Element 1 is ambiguous between two observables → FAIL
- Item 4 (Bridge map explicitly named — not "analogous" or "corresponds to"): line 1015 reads "Connes-Karoubi pairing per CM-1995 III.4 (TBD final at §VII.AV landing)" — the TBD qualifier means the bridge map identity is NOT yet finalized → FAIL
- Corpus §6 corner-cell declaration (item 1): the corner-cell declaration is structurally INCOMPATIBLE with the named substrate-IS pillar (Pillar II → Cell II is the natural cell; the entry asserts Cell IV via inheritance) → FAIL

The §W5-4 §VII.AV registration is registry-INCOMPLETE under the existing audit clauses, BEFORE we even reach the Level-2-binding sub-class question.

**Concrete reading**: §VII.AV STAGE-1-CANDIDATE pre-registration cannot stand at S89 W6 close. The c-projection inheritance mechanism is the cross-corner co-primary pattern in a different label; the §VII.AG.1 precedent does not extend to K-counter-advancing entries; the §W5-4 5-anatomy declaration is INCOMPLETE-OR-CONFUSED at Element 1. The correct status is REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE + Element-1 disambiguation (which observable IS the substrate-IS for §VII.AV — Mellin-Barnes residue or K-window log-derivative? They cannot both be).

#### Re: L3 — SCHEMATIC artifact reading of α = 5.07

**PARTIAL AGREE / PARTIAL DISAGREE**. lizzi is correct on the substrate-physics derivation of why the Casimir-bound proxy yields α≈5; she is wrong on the conclusion that this preserves Level-2-binding for §VII.AV registry-PASS-eligibility.

**AGREE on the SCHEMATIC artifact diagnosis.** §W5-3 line 826 contains the honest substrate-physics derivation:

> "Why the Casimir-bound proxy gives α≈5 not α=3. The proxy rescales Δ_eff(L_max) = Δ_static · (L_max+1)/13 — a LINEAR rescaling in L_max. The induced shift in v_K² ∝ 1/sqrt(xi² + Δ_eff²) at K=K_horizon is approximately linear in (1−f(L_max)) = (12−L_max)/13 for small deviations. Squaring the variance and taking 2nd log-derivative gives a residual envelope dominated by the LINEAR shape, not a power-law L^{-3}. The empirical α=5.07 from the log-log regression is an artifact of the quasi-LINEAR proxy structure, not a substrate-distance-3 substrate-physics finding."

The substrate-physics is correct. The Casimir-bound rescaling at f(L_max) = (L_max+1)/13 IS a quasi-LINEAR rescaling rule; squaring the residual under log-log regression DOES produce an exponent of order 5 rather than 3. The proxy's quasi-LINEAR structure dominates the log-log slope; the α=5.07 measures THAT quasi-LINEAR convergence, not the substrate's intrinsic HKR-image binding rate. So far we agree.

I ALSO agree on the level-pin discipline: §W5-3 correctly tags the convention with `-CASIMIR-BOUND-PROXY` suffix per `substrate-first-canonical-sourcing.md §(iv)` (the W9c-1 POSITIVE-CALIBRATION pattern), and §W5-3 cross-check (f) at line 813 honestly classifies the 1.69× ratio as "INFO (proxy structural mismatch)" rather than concealing the gap. The honesty discipline is intact.

**DISAGREE on the conclusion that proxy-fidelity-vs-binding-class separation preserves Level-2-binding for registry-PASS purposes.**

lizzi's argument structure (L3 lines 95-103) is: (i) the proxy gives α=5.07 by its quasi-LINEAR shape; (ii) this is a proxy-fidelity finding, not a substrate-physics falsifier; (iii) the HKR map's existence is anchored at §VII.AF.1.OP-PROJ at the registry level; (iv) therefore Level-2-binding holds, INFO is honest disclosure of proxy-precision, and §VII.AV stands registry-PASS-eligible.

The structural error is at step (iv). The rule's Level-2-binding sub-class admissibility is OPERATIONAL — the envelope must bound `‖HKR(c_L) − c_continuum‖` for the SPECIFIC c_L. The §W5-3 empirical α=5.07 demonstrably does NOT bound `‖HKR(c_L) − c_continuum‖` for the K-window log-derivative — it bounds the proxy reconstruction's substrate-internal convergence. Apply the §"Level-2-non-binding" definition operationally:

Per `cross-pillar-bridge-anatomy.md` lines 48-51:

> "**Definition**: the algebraic envelope `L^{-α}` is a bare-decomposition convergence rate that does NOT bind Level-1. Operationally, the envelope bounds `‖c_L − c_∞‖` where `c_∞` is a substrate-internal limit (e.g., a bare Mellin truncation `Tr(D_K^{-2s})`) WITH NO HKR image to a continuum laboratory observable on the partner pillar.
> **Counter-example pattern**: a `L^{-α}` envelope on `Tr(D_K^{-2s})` evaluated at substrate-distance pole s ∈ {3, 4, ...} that lacks an HKR image to a continuum lab observable. Such an envelope describes substrate-internal Mellin-truncation convergence; it does NOT describe the convergence of any cross-pillar bridge map. The `c_continuum` reference quantity is undefined for this envelope class."

The §W5-3 empirical envelope under the Casimir-bound proxy is STRUCTURALLY ANALOGOUS to the counter-example pattern. Substitute:

- The proxy's `c_L` = K-window log-derivative evaluated at Δ_eff(L_max) on the L_max=12 BdG mode amplitudes (held FIXED).
- The proxy's `c_∞` = limit of the proxy as f(L_max) → 1 (achieved at L_max=12; canonical -7.046336474406761).
- The envelope `L^{-5.07}` bounds `‖c_L − c_∞‖` under the proxy's substrate-internal Casimir-bound rescaling rule.
- The HKR image of `c_L` to the Pillar IV Peotta-Törmä BZ-trace — i.e., the actual `c_continuum` reference in the rule's operative sense — is **NEVER MEASURED** by the proxy. The proxy reaches its `c_∞` at f(L_max)=1.0 BY CONSTRUCTION (lizzi notes this herself at L3 line 111: "the L_max=12 bit-for-bit reproduction at §W5-3 cross-check (a) line 808 confirms this; both the proxy at f(12)=1.0 and the canonical converge at L_max=12"). Convergence to the proxy's own L_max=12 anchor is NOT convergence to the HKR image of the K-window log-derivative.

The proxy is a substrate-internal rescaling rule, NOT an HKR bridge. The empirical envelope describes the proxy's quasi-LINEAR substrate-internal trajectory, NOT the HKR-image's L^{-3} bridge convergence. The `c_continuum` reference quantity in the partner pillar's continuum — what the rule requires the envelope to bound the distance to — is UNDEFINED for the proxy envelope.

This matches the rule's Level-2-non-binding counter-example pattern verbatim: a `L^{-α}` envelope that describes substrate-internal convergence (the Casimir-bound Δ-rescaling rule) WITHOUT an HKR image to a continuum laboratory observable on the partner pillar (the proxy does not have such an image; its `c_∞` is its own L_max=12 anchor, NOT the Peotta-Törmä BZ-trace).

The enforcement clause at lines 57-65 then routes §W5-3's empirical envelope to registry-INELIGIBLE:

> "- IF Level-2-non-binding (regardless of Level-3 vs Level-2 numerical comparison) → registry-INELIGIBLE; the bridge entry is registry-incomplete and routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum` reference quantity in the partner pillar's continuum."

The §W5-3 INFO verdict (composite=INFO; magnitude=FAIL; regime=MARGINAL) is correct as a per-gate verdict — the gate honestly reports that the SCHEMATIC proxy cannot deliver an empirical envelope inside the predicted [1.5, 5.0] α band at acceptable R². But that INFO verdict does NOT promote §VII.AV (which depends on §W5-3 as its Level-2 envelope source) to registry-PASS-eligible STAGE-1-CANDIDATE. The proxy envelope is Level-2-non-binding in the rule's operative sense; per the enforcement clause, §VII.AV is registry-INELIGIBLE pending CF-W5-3 full BdG re-derivation.

**On lizzi's §W5-3 line 830 falsification framing.** §W5-3 line 830 states the substrate's own falsification meaning: "The Level-2-binding declaration is structurally falsified iff: (a) the HKR `L_max → ∞` map is shown to NOT exist for the Corner-IV K-window log-derivative ... (b) the Pillar IV Peotta-Törmä BZ-trace is shown to NOT be the continuum image. ... The α-extraction precision (proxy α=5.07 vs predicted α=3) is NOT a falsifier of Level-2-binding; it's a proxy-fidelity finding."

This formulation conflates two distinct questions:
- **Q1**: Does an HKR map EXIST for the K-window log-derivative observable? (This is a structural question at the bridge-family level; answered YES at the registry by §VII.AF.1.OP-PROJ.)
- **Q2**: Does the §W5-3 empirical envelope α=5.07 BOUND the HKR-image binding rate `‖HKR(c_L) − c_continuum‖` for the K-window log-derivative? (This is the operational question the rule asks; answered NO because the proxy's `c_∞` is its own L_max=12 anchor, not the Peotta-Törmä BZ-trace.)

§W5-3 line 830 answers Q1 (which is not falsified by α-precision) and treats this as sufficient. The rule's Level-2-binding admissibility test requires BOTH Q1 (HKR map existence) AND Q2 (envelope operationally bounds the HKR-image distance for THIS observable). Q2 is the falsifier, and §W5-3 does not address Q2 affirmatively — the proxy does not measure the HKR-image binding rate.

**On the substrate-physics derivation as sufficient diagnostic of proxy-fidelity (lizzi's L3 line 115 question).** I accept the substrate-physics derivation at §W5-3 line 826 as a correct demonstration that the proxy is too aggressive (Δ-rescaling alone produces quasi-LINEAR shape; full BdG re-derivation would regenerate u_k, v_k, E_qp at each L_max). What I do NOT accept is the inference that this preserves Level-2-binding for registry-PASS purposes. The diagnostic correctly identifies the proxy as SCHEMATIC and queues CF-W5-3 for refinement; it does NOT promote the SCHEMATIC envelope to registry-PASS-eligible-pending-precision-refinement.

**On registry-PASS-eligibility timing.** lizzi's L3 framing (lines 105-109) acknowledges that CF-W5-3 "EXISTS because the registry-level Level-2-binding declaration stands INDEPENDENT of proxy α-precision". My reading inverts this: CF-W5-3 EXISTS because the SCHEMATIC proxy CANNOT deliver per-observable Level-2-binding extraction at S89 W6 close; registry-PASS-eligibility for §VII.AV must WAIT on the full BdG re-derivation. The INFO verdict closes §W5-3 as a gate but does NOT promote §VII.AV; the CF-W5-3 carry-forward IS the path to promotion in S90, NOT a refinement of an already-registered STAGE-1-CANDIDATE.

**Concrete reading**: §W5-3 INFO is the CORRECT honest disclosure that the Level-2-binding sub-class admissibility is NOT empirically demonstrated at S89 W6. The §VII.AF.1.OP-PROJ registry anchor establishes that an HKR map EXISTS for observables in the Pillar III ↔ Pillar IV bridge family; it does NOT establish that the K-window log-derivative's HKR-image converges at any specific rate. Per-observable extraction of `‖HKR(c_L) − c_continuum‖` is what the rule requires for registry-PASS-eligibility, and the SCHEMATIC proxy does not deliver it. §VII.AV downgrades to REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE under the §"Level-2-non-binding" enforcement clause as operationally applied.

#### Re: L4 — Proposed rule-extension form

**DISAGREE** on the structural direction of lizzi's proposed sub-clause. The proposal as written opens a false-PASS pathway that the existing Level-2 Layer Distinction (S88 W8-88 hardening) was designed to close. I counter-propose a rule extension in the OPPOSITE direction: a CLARIFICATION of the §"Level-2-non-binding" enforcement clause that introduces a NEW deferred-pending state for SCHEMATIC-proxy α-extractions, allowing S90 CF-W5-3 full-physical-re-derivation to later promote the entry without forfeiting the registry-PASS-eligibility timing discipline.

**Why lizzi's proposed sub-clause opens a false-PASS pathway.**

lizzi's L4 proposal (workshop lines 141-160) introduces a sub-clause titled "Level-2-binding inheritance from registry anchor" that admits Level-2-binding declaration via inheritance from a prior §VII entry's HKR-map identification, REGARDLESS of per-observable empirical α-extraction precision. The four conditions (a)-(d) at L4 lines 147-153 are:

(a) cite the registry-anchor §-reference;
(b) match c_continuum reference to the registry anchor's c_continuum;
(c) report Level-3 anchor at canonical L_max + disclose proxy-class via convention tag;
(d) if empirical α falls outside the predicted-α band under a known-SCHEMATIC proxy, close INFO (NOT FAIL) and queue refinement carry-forward.

The structural problem is at condition (d). Under lizzi's reading, an entry can:
- Inherit Level-2-binding declaration from a registry anchor on a STRUCTURALLY DIFFERENT observable (e.g., Cell IV K-window log-derivative inheriting from Cell I HP¹ cohomology — Kill-shot #1 territory);
- Report an empirical α that fails the predicted-α band by 69% under a SCHEMATIC proxy;
- Close INFO at the per-gate level;
- Pre-register STAGE-1-CANDIDATE at a §VII slot WITHOUT delivering the per-observable Level-2-binding extraction the rule's operative definition requires.

This is precisely the bare-decomposition-envelope false-PASS pathway that the S88 W8-88 Level-2 Layer Distinction hardening was authored to close. The existing rule structure at lines 36-65 is built around a sharp PASS/FAIL distinction: Level-2-binding (admissible) vs Level-2-non-binding (FORBIDDEN), with the enforcement clause at lines 57-65 explicitly directing Level-2-non-binding envelopes to registry-INELIGIBLE with plan-freeze halt. lizzi's proposed sub-clause introduces a THIRD category — "Level-2-binding-by-inheritance-with-SCHEMATIC-proxy-INFO" — that lives between the two existing categories and that operates as an escape hatch from the enforcement clause for entries that would otherwise fall on the Level-2-non-binding side.

Worse, the parenthetical at L4 line 159 ("the c-projection IS the inheritance mechanism, not a violation of the cross-corner prohibition") attempts to legislate an exception to the §"Algebra-axis orthogonality K-counter" MANDATORY-at-K=3 clause via a SUGGESTION-status K=1 entry. The MANDATORY-at-K=3 clause is the highest-status rule in the parent file; SUGGESTION-status sub-clauses cannot abrogate MANDATORY rules. A K=1 SUGGESTION clause cannot legislate that "c-projection from Cell I to Cell IV is admissible despite Cell I and Cell IV being structurally orthogonal in identity-class membership". The cross-corner co-primary prohibition (Cell I ↔ Cell IV) was promoted to MANDATORY at K=3 at S87 W-2 R3 close precisely to close exactly this kind of cross-corner inheritance pathway.

**Counter-proposal: CLARIFICATION of §"Level-2-non-binding" enforcement (NOT a new admissibility sub-clause).**

The structural direction of the rule extension should be a CLARIFICATION of the existing §"Enforcement clause" at lines 57-65, adding a NEW case for SCHEMATIC-proxy α-extractions that introduces a deferred-pending state (NOT a registry-ineligibility verdict, which would foreclose CF-W5-3 promotion in S90). The new case lives BETWEEN the two existing cases:

#### Concrete BEFORE/AFTER patch (counter-proposed)

**BEFORE** (rule file at lines 57-65, verbatim):

```
#### Enforcement clause

The registry-PASS criterion `Level-3 empirical value < Level-2 envelope value at canonical L_max` (see §"Registry-PASS criterion" above) COUNTS toward registry-PASS if and only if the Level-2 envelope is Level-2-binding per this sub-section's definition. Bare-decomposition envelopes (Level-2-non-binding) DO NOT contribute to registry-PASS regardless of how tightly the Level-3 anchor satisfies the numerical bound; their false-PASS pathway is closed by construction.

Specifically:

- IF Level-2-binding ∧ (Level-3 < Level-2 envelope at canonical L_max) → registry-PASS ELIGIBLE (other audit clauses still apply).
- IF Level-2-non-binding (regardless of Level-3 vs Level-2 numerical comparison) → registry-INELIGIBLE; the bridge entry is registry-incomplete and routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum` reference quantity in the partner pillar's continuum.
- IF Level-2 sub-class undeclared → registry-INCOMPLETE per §"Audit at plan-freeze" item-extension below; plan-freeze halt.
```

**AFTER** (counter-proposed; new case inserted between the existing IF Level-2-binding and IF Level-2-non-binding cases):

```
#### Enforcement clause

The registry-PASS criterion `Level-3 empirical value < Level-2 envelope value at canonical L_max` (see §"Registry-PASS criterion" above) COUNTS toward registry-PASS if and only if the Level-2 envelope is Level-2-binding per this sub-section's definition. Bare-decomposition envelopes (Level-2-non-binding) DO NOT contribute to registry-PASS regardless of how tightly the Level-3 anchor satisfies the numerical bound; their false-PASS pathway is closed by construction.

Specifically:

- IF Level-2-binding ∧ (Level-3 < Level-2 envelope at canonical L_max) → registry-PASS ELIGIBLE (other audit clauses still apply).

- IF Level-2-binding-by-construction-anchor (HKR map exists at the bridge-family level per a prior registry anchor) ∧ Level-2 envelope EXTRACTED-UNDER-SCHEMATIC-PROXY ∧ empirical α OUTSIDE predicted α band (per `substrate-first-canonical-sourcing.md §(iv)` SCHEMATIC-vs-physical level pin discipline) → registry-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION; the bridge entry is held pending the full physical re-derivation at canonical L_max. Per-observable Level-2-binding extraction MUST be completed before promotion to registry-PASS-eligible STAGE-1-CANDIDATE; the deferred-pending state preserves the audit-trail of the SCHEMATIC envelope as honest disclosure WITHOUT promoting it to registry-PASS-eligibility.

- IF Level-2-non-binding (the envelope's `c_∞` is a substrate-internal limit with NO HKR image to a continuum laboratory observable on the partner pillar; regardless of Level-3 vs Level-2 numerical comparison) → registry-INELIGIBLE; the bridge entry is registry-incomplete and routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum` reference quantity in the partner pillar's continuum.

- IF Level-2 sub-class undeclared → registry-INCOMPLETE per §"Audit at plan-freeze" item-extension below; plan-freeze halt.
```

The structural difference from lizzi's proposal:
- **lizzi's proposal** introduces a NEW admissibility sub-clause that admits inheritance-based Level-2-binding regardless of per-observable α-extraction. The entry can STAGE-1-CANDIDATE pre-register at S89 close.
- **My counter-proposal** introduces a deferred-pending intermediate state. The entry CANNOT STAGE-1-CANDIDATE pre-register at S89 close; the deferred-pending state HOLDS the entry until CF-W5-3 full physical re-derivation lands. On CF-W5-3 PASS, the entry promotes from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION to registry-PASS-eligible STAGE-1-CANDIDATE in S90+; on CF-W5-3 FAIL (e.g., full BdG re-derivation reveals α genuinely outside the predicted band), the entry routes to registry-INELIGIBLE per the existing Level-2-non-binding enforcement.

The counter-proposal preserves:
- The per-observable extraction requirement (the Level-2-binding admissibility test remains operational on `‖HKR(c_L) − c_continuum‖` for the SPECIFIC observable);
- The registry-PASS-eligibility timing discipline (no STAGE-1-CANDIDATE pre-registration without per-observable extraction);
- The audit-trail of SCHEMATIC proxy disclosures (the deferred-pending state preserves the proxy envelope as carry-forward provenance);
- The MANDATORY-at-K=3 cross-corner co-primary prohibition (the deferred-pending state does NOT permit cross-corner inheritance — it requires the per-observable extraction to be performed at the inheriting observable's OWN corner cell).

The counter-proposal recognizes:
- That SCHEMATIC proxies are honest pre-cursors to full physical re-derivations (the `-CASIMIR-BOUND-PROXY` convention tag at §W5-3 is appropriate);
- That CF-W5-3 EXISTS as the canonical promotion path (lizzi correctly notes this at L3 lines 105-109);
- That the deferred-pending state is a legitimate intermediate verdict (it's not registry-INELIGIBLE because the underlying observable could be Level-2-binding at the per-observable level — that's an empirical question CF-W5-3 will answer; it's not registry-PASS-eligible because the SCHEMATIC proxy does not currently demonstrate the binding).

**On lizzi's L4 line 182 question (rule-file diff structure).**

lizzi asks whether the proposed sub-clause structure (Provenance / Definition / Calibration / Status / Cross-corner check preservation) aligns with the parent rule's existing §"Level-2 Layer Distinction" sub-clause structure. Under my counter-proposal, the rule extension is NOT a new admissibility sub-clause — it's a clarification of the existing enforcement clause. The diff location is `cross-pillar-bridge-anatomy.md` lines 57-65 (the existing §"Enforcement clause" block), not lines 46-48 (between Calibration #2 and §"Level-2-non-binding"). The structural reason: lizzi's proposal would introduce a third admissibility category co-equal with Level-2-binding and Level-2-non-binding; my counter-proposal extends the enforcement direction-table with a deferred-pending intermediate verdict that operates BETWEEN the two existing categories without inventing a new admissibility class.

**On audit-script extension.**

My counter-proposal extends `computations/_shared/_cross_pillar_bridge_audit.py` with a different sub-check than lizzi's. lizzi's proposal regex-detects `inherits-Level-2-binding-from-§VII\.[A-Z]+` and validates the c_continuum cross-reference; my counter-proposal regex-detects `convention=.*-(?:SCHEMATIC|PROXY)` in the producing script's verdict-line emission AND cross-references whether the empirical α falls outside the predicted band. On positive match (SCHEMATIC envelope AND α-outside-band AND registry slot pre-registration claimed), the audit emits MANDATORY remediation: re-classify the slot as REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION rather than STAGE-1-CANDIDATE.

**On K-counter calibration.**

Under my counter-proposal, §W5-3 + §W5-4 do NOT advance the K-counter (per `cross-pillar-bridge-anatomy.md §"Status: MANDATORY at K=3"` corpus saturation) because they are NOT calibration-LANDING events at S89 W6 close — they are deferred-pending pre-cursors awaiting CF-W5-3. The K=3 MANDATORY corpus declared at lines 275-277 (W-5 LANDED §VII.AF.1 / W11-5 REGISTRY-FAIL / W4a-17 LANDED §VII.W-3.LAB) remains unchanged. The Hybrid Independence Test K-counter at corpus §3 (K=1 baseline at W-5) also remains unchanged at K=1 SUGGESTION status until §W5-4 promotes from deferred-pending to STAGE-1-CANDIDATE in S90+.

**Concrete reading**: the rule extension should be a CLARIFICATION of the existing enforcement clause (adding a deferred-pending intermediate state for SCHEMATIC-proxy α-extractions), NOT a new admissibility sub-clause that opens a false-PASS pathway via cross-corner inheritance. The deferred-pending state preserves the audit-trail discipline AND the registry-PASS-eligibility timing discipline AND the MANDATORY cross-corner co-primary prohibition. lizzi's proposed sub-clause violates all three.

#### Re: L5 — §VII.AU cross-cutting parallel

**DISAGREE** on the framing that §W5-6 template-inheritance is structurally cleaner than §W5-4 empirical-α inheritance. The reverse is structurally true: §W5-6 is in a WEAKER position than §W5-4, not a stronger one. Both should downgrade to REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION under my reading.

**The structural argument from §W5-6's own machinery pin.**

§W5-6 line 1511 reads, verbatim from the machinery pin table:

> "envelope_alpha_predicted | 3 (Level-2 L^{−3} at d=4)"

§W5-6 line 1500 pins `L_max | 10 (canonical truncation per `cross-pillar-bridge-anatomy.md §"Calibration corpus"`)`. There is NO L_max scan in §W5-6's machinery pin table — no L_max_scan parameter, no envelope_estimator, no log-log regression, no n_L_max_points, no per-L timing limit. The §W5-6 machinery is a SINGLE-L_max gate evaluating c_sub_corrected, n_s_recomputed, and Planck σ at L_max=10. The Level-2 envelope α=3 is asserted by structural-exact template inheritance from the W-5 calibration at d=4 — NOT extracted from per-observable empirical L_max-scan data.

lizzi's L5 frames this as a STRENGTH ("§W5-6's template-inheritance is even cleaner than §W5-4 empirical-α inheritance"; L5 lines 184-186). My structural reading is that it is a WEAKNESS — and a more severe one than §W5-4's.

**Apply the §"Level-2-binding (admissible for registry-PASS)" operational definition to §W5-6.**

Per `cross-pillar-bridge-anatomy.md` lines 44-45:

> "**Definition**: the algebraic envelope `L^{-α}` is the convergence rate of an HKR-image (Hochschild-Kostant-Rosenberg map) that BINDS the Level-1 cohomology class. Operationally, the envelope bounds `‖HKR(c_L) − c_continuum‖` where `c_L` is the substrate-IS finite-L cocycle / Hochschild moment / spectral-triple invariant and `c_continuum` is the HKR-image realized as the laboratory-IN continuum observable on the partner pillar."

What is `c_L` for §W5-6? The substrate-IS observable per §W5-6 line 1544 is "c_sub_corrected ... derived from the M_Pl_eff² ratio at the Mellin-cone closure". At parameterized slope_A on the Pillar-I n_s spectral-action, the substrate-IS observable is the M_Pl_eff² ratio evaluated at L_max-truncated `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`.

What empirical bound does §W5-6 provide on `‖HKR(c_L) − c_continuum‖` for this observable across L_max? **Zero.** §W5-6 evaluates c_sub_corrected at L_max=10 only (single point). The L^{-3} envelope at d=4 is asserted by template-inheritance from §VII.AF.1.OP-PROJ's calibration — but §VII.AF.1.OP-PROJ's calibration is on the Pillar III HP¹ cohomology HOCHSCHILD-PAIRING (Cell I; algebra-INVARIANT spectrum-only), NOT on the Pillar-I n_s spectral-action M_Pl_eff² ratio (a structurally different observable).

This is structurally analogous to the §"Level-2-non-binding" counter-example pattern at lines 48-51:

> "**Counter-example pattern**: a `L^{-α}` envelope on `Tr(D_K^{-2s})` evaluated at substrate-distance pole s ∈ {3, 4, ...} that lacks an HKR image to a continuum lab observable. Such an envelope describes substrate-internal Mellin-truncation convergence; it does NOT describe the convergence of any cross-pillar bridge map. The `c_continuum` reference quantity is undefined for this envelope class."

Substitute: the §W5-6 template-asserted L^{-3} envelope is on the Pillar-I n_s spectral-action observable at substrate-distance pole s=3 (Mellin-cone substrate-distance-1; §W5-6 line 1550 cites "Route-B identity from S88 W-15 W4c-36: n_s_FW = 9561/10000 at substrate-distance-1 Mellin pole"). It LACKS empirical demonstration that the envelope describes HKR-image convergence for THIS observable. The `c_continuum` reference is named (Planck CMB at Pillar II), but the BINDING between the substrate-IS observable and the laboratory-IN observable AT the L^{-3} convergence rate is not empirically demonstrated — it is template-asserted.

**The structural asymmetry vs §W5-4.**

| Property | §W5-4 (Cell IV K-window log-derivative) | §W5-6 (Pillar-I n_s spectral-action) |
|:---------|:----------------------------------------|:--------------------------------------|
| L_max scan performed | YES (7 L_max values {6,...,12}) | **NO** (single L_max=10) |
| Empirical α extraction | α=5.0679 from log-log regression | **NONE** (α=3 template-asserted) |
| Proxy class | Casimir-bound Δ-rescaling (SCHEMATIC) | None applicable (no scan) |
| Per-observable Level-2 binding evidence | Quasi-LINEAR proxy convergence (does not bound HKR-image) | **ZERO** evidence on the FWD-C1 observable |
| Convention tag SCHEMATIC disclosure | Yes (`-CASIMIR-BOUND-PROXY`) | No SCHEMATIC tag (template-inheritance not disclosed as SCHEMATIC) |

§W5-4 at least provides SCHEMATIC empirical evidence (the α=5.07 is honest about the proxy structure). §W5-6 provides NO empirical evidence whatsoever on the FWD-C1 substrate-IS observable's L_max convergence behavior. The template-inheritance lizzi praises as "cleaner" is actually the LIMIT of providing zero per-observable extraction — it is the most extreme form of registry-anchor inheritance.

Under the §"Level-2-binding" admissibility test as operationally defined, §W5-6 provides:
- **Q1 (HKR map exists at the bridge-family level?)**: NO at the strict reading — FWD-C1 is Pillar I ↔ Pillar II per `cross-pillar-bridge-corpus.md §4`, which is a DIFFERENT bridge family from §VII.AF.1.OP-PROJ's Pillar III ↔ Pillar IV. Even at lizzi's loose "bridge-family-level inheritance" reading, the bridge family does not match. §W5-6 cites HKR as the bridge map class (line 1510), but the HKR map for Pillar I ↔ Pillar II has NOT been independently registered at any §VII entry. So the registry anchor lizzi's L2/L4 mechanism requires does not exist for §W5-6.
- **Q2 (envelope operationally bounds HKR-image distance for this observable?)**: NO — no L_max scan performed; no empirical envelope extracted.

§W5-6 fails BOTH the Q1 (registry-anchor existence at the correct bridge family) AND Q2 (per-observable empirical extraction) prongs. §W5-4 fails Q2 under a SCHEMATIC proxy. §W5-6 is therefore in a structurally WEAKER position, NOT a stronger one.

**On lizzi's L5 line 230 question (does per-observable-extraction reading require §W5-6 to perform an L_max scan?).**

Yes — under the per-observable-extraction reading, §W5-6 requires an L_max scan on the parameterized slope_A canonical observable BEFORE registry-PASS-eligibility. The structural-exact L^{-3} template-inheritance from the W-5 calibration does NOT suffice for FWD-C1 STAGE-1-CANDIDATE pre-registration at S89 W6 close because:

(i) The W-5 calibration is on the Pillar III HP¹ Hochschild pairing — a DIFFERENT substrate-IS observable in a DIFFERENT bridge family (Pillar III ↔ Pillar IV, NOT Pillar I ↔ Pillar II). Template-inheritance from W-5 to FWD-C1 carries no force at the bridge-family level.

(ii) The L^{-3} convergence rate at d=4 is a STRUCTURAL PREDICTION specific to the HKR-image of the W-5 cohomology class on the Jensen-deformed band-0 projector. The Pillar-I n_s spectral-action M_Pl_eff² ratio is a structurally different cohomology class; its HKR-image convergence rate is an empirical question that requires per-observable extraction.

(iii) The bit-precision match `n_s_recomputed = 0.9561 EXACT` at §W5-6 line 1550 is a Route-B identity recovery at the Mellin pole — it is the Level-3 anchor (a numerical evaluation at canonical L_max=10), NOT a Level-2 envelope. The Level-2 envelope is what governs L_max convergence; the Level-3 anchor is what evaluates at the canonical truncation. §W5-6 provides Level-3 but not Level-2.

The symmetric carry-forward is `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL` — perform the per-observable L_max scan on the parameterized slope_A canonical at L_max ∈ {6, 7, 8, 9, 10, 11, 12}; extract empirical α; verify α ∈ [2.5, 3.5] band around predicted α=3. On PASS, §VII.AU promotes from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION to registry-PASS-eligible STAGE-1-CANDIDATE.

**On the symmetry framing.**

lizzi at L5 lines 213-228 argues that:
- §W5-3 INFO + §W5-4 PASS + §W5-6 INFO together deliver BOTH §VII.AV STAGE-1-CANDIDATE AND §VII.AU STAGE-1-CANDIDATE under the inheritance reading.
- If the inheritance reading FAILS, §VII.AU is LESS affected than §VII.AV because §VII.AU does not depend on §W5-3's empirical α extraction.

My counter-framing: if inheritance FAILS, §VII.AU is MORE affected than §VII.AV, not less. §VII.AV at least has a SCHEMATIC proxy α to refine (CF-W5-3 full BdG re-derivation can directly update the proxy's α=5.07 toward the true substrate α). §VII.AU has NOTHING to refine — no L_max scan has ever been performed on the FWD-C1 substrate-IS observable. The S90 carry-forward for §VII.AU is a brand-new computation (`S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL`), not a refinement of an existing SCHEMATIC extraction. The "less affected" framing inverts the structural picture: template-inheritance is the WEAKEST form of inheritance, not a STRONGER one.

**On the HIT K-counter advancement.**

lizzi at L5 line 226 claims that if both §W5-4 and §W5-6 stand as registry-PASS-eligible STAGE-1-CANDIDATE, the Hybrid Independence Test K-counter advances K=1 → K=2 from §W5-4 AND K=2 → K=3 from §W5-6, reaching MANDATORY status. Under my reading, neither advances the K-counter at S89 W6 close:

- §W5-4 §VII.AV is deferred-pending until CF-W5-3 full BdG re-derivation; HIT K-counter unchanged at K=1.
- §W5-6 §VII.AU is deferred-pending until S90 FWD-C1 L_max scan; HIT K-counter unchanged at K=1.

Per the §"Two-clause separation: registry-PASS (per-entry) vs K-counter advancement (rule-level corpus)" clause at parent rule lines 279-295, K-counter advancement requires calibration-LANDING events. A deferred-pending entry is NOT a calibration-LANDING event — it is a pre-cursor to one. The HIT K-counter waits on per-observable Level-2 envelope extraction for each forward bridge candidate; that extraction is queued for S90 (CF-W5-3 for §VII.AV; new S90 gate for §VII.AU).

**Concrete reading**: §W5-6's §VII.AU is in a structurally weaker position than §W5-4's §VII.AV — it provides NO empirical evidence on the FWD-C1 substrate-IS observable's L_max convergence at all, while §W5-4 at least provides SCHEMATIC evidence via the §W5-3 proxy. Both should downgrade to REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION under the counter-proposal at Re:L4. The HIT K-counter does NOT advance at S89 W6 close; advancement waits on the S90 per-observable extractions.

### Part 2: Original Analysis

#### C1: Bridge-anatomy spec — what MANDATES per-observable extraction

The operative claim is structural: the `cross-pillar-bridge-anatomy.md §"Level-2-binding"` admissibility definition (lines 42-46) is PER-OBSERVABLE — it specifies an operational bound that the empirical Level-2 envelope must satisfy FOR THE SPECIFIC substrate-IS observable being registered. Registry-anchor inheritance from a different observable in a "neighboring bridge family" cannot substitute. I derive this from the rule-text itself and apply it to the §W5-3 case via the canonical substitution chain pattern at `math-scripts.md §"Double-Check Logic Before Compute"`.

**The rule-text mandate.**

Per rule lines 44 verbatim:

> "**Definition**: the algebraic envelope `L^{-α}` is the convergence rate of an HKR-image (Hochschild-Kostant-Rosenberg map) that BINDS the Level-1 cohomology class. Operationally, the envelope bounds `‖HKR(c_L) − c_continuum‖` where `c_L` is the substrate-IS finite-L cocycle / Hochschild moment / spectral-triple invariant and `c_continuum` is the HKR-image realized as the laboratory-IN continuum observable on the partner pillar."

The operative variable `c_L` is the substrate-IS finite-L cocycle on the truncated spectral algebra `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The subscript `_L` indexes the L_max-truncation of the cohomology class for THAT cocycle. In NCG terms (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula), Hochschild cohomology of a finite spectral triple is constructed PER-COCYCLE: each cocycle `c` defines its own class `[c] ∈ HH^*(A_K^{≤L})`; HKR maps each class element-by-element to its de Rham counterpart `HKR([c]) ∈ H^*_{dR}(\text{continuum-image})`.

The substitution chain (per `cross-pillar-bridge-corpus.md §1` Steps 1-5 verbatim) makes the per-observable dependence explicit:

> "**Step 3 (substitution)**: A `L^{-α}` envelope on `‖HKR(c_L) − c_continuum‖` IS a Level-2-binding envelope iff `c_continuum` is the HKR-image of the Level-1 cohomology class. The envelope describes convergence of the Level-1 binding under the bridge map's `L → ∞` limit."

The envelope is INDEXED by the cohomology class. Different classes have different HKR images, and the binding rate `‖HKR(c_L) − c_continuum‖` is a per-class quantity. Registry-anchor inheritance at the bridge-family level addresses only the EXISTENCE of an HKR map (that the bridge family admits HKR `L_max → ∞` images at all) — it does NOT propagate the binding RATE from one class to another within the family.

**Substitution chain — apply to §W5-3 K-window log-derivative case (per `math-scripts.md §"Double-Check Logic Before Compute"`).**

Required structure: state each definition; substitute; simplify; read direction off the canonical form.

**Step 1 (Definition)** — Per-observable substrate-IS cocycle for the K-window log-derivative case:

```
c_L := L(L_max) = d^2 ln P_GGE / d (ln K)^2  evaluated at K = K_horizon
              on (A_K^{<=L_max}, H_K^{<=L_max}, D_K^{<=L_max})
       where P_GGE(K) = Var_a(v_K^2) on the BdG sub-algebra.
```

`c_L` is the K-window log-derivative cocycle class. It is an algebra-DEPENDENT state-pair functional at Cell IV per §W5-3 line 609 + §VII.U.2 4-corner partition.

**Step 2 (Definition)** — Per-observable laboratory-IN continuum image:

```
c_continuum := HKR(c_L) at L_max -> infinity
            = -7.046336474406761 (canonical, verified bit-for-bit at L_max=12
              per S87 W2-3 / S89 W5-2 PASS; §W5-3 line 568).
```

Note the substitution: `c_continuum` for the K-window log-derivative cocycle is its OWN HKR image at L_max → ∞, NOT the HKR image of a different cocycle (e.g., the HP¹ cohomology Hochschild pairing R_universal from §VII.AF.1.OP-PROJ). The Peotta-Törmä BZ-trace `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` is the Pillar-IV continuum partner; but the question is WHICH Hochschild-pairing's HKR image lands on it. §VII.AF.1.OP-PROJ identifies HP¹ Hochschild pairing's HKR image with `R_geom`; whether the K-window log-derivative's HKR image lands on the same `R_geom` or on a structurally distinct Pillar-IV continuum observable is an open empirical question (the K-window log-derivative is a state-pair functional, NOT a Hochschild pairing — they live on different algebra-axis cells).

**Step 3 (Substitution)** — Empirical Level-2 envelope for the K-window log-derivative under the Casimir-bound proxy:

```
‖HKR(c_L) − c_continuum‖_empirical = |L(L_max) − (−7.046336)|
   = A · L_max^{-5.0679}  (S89 W5-3 log-log regression at R^2 = 0.9244)
where A = exp(10.0815) = 23,856 (S89 W5-3 line 599; log_A = 10.0815)
```

Substituted into the Level-2-binding admissibility test:

```
Empirical envelope bounds:  L^{-5.07}
Predicted envelope bounds:  L^{-3}      (substrate-distance-2 d=4 HKR-image rate
                                          per S86 W-5 §VII.W structural prediction)
Ratio:                      α_emp / α_pred = 5.0679 / 3 = 1.6893     ≈ 1.69×
```

**Step 4 (Simplification)** — Compare empirical bound to predicted HKR-image binding rate:

```
At L_max = 10:
  L_max^{-3}    = 1.00e-3
  L_max^{-5.07} = 8.55e-6
  Ratio:         8.55e-6 / 1.00e-3 = 8.55e-3
```

Tighter empirical bound (the proxy converges faster than the predicted HKR-image rate, NOT slower). This is the diagnostic signature of the proxy under-representing the substrate's full convergence behavior: the Casimir-bound rescaling is too aggressive in the L_max=12 reference range (the proxy convergence saturates at f(L_max)=1.0 by construction, producing artificially fast log-log slope).

**Step 5 (Direction)** — Read off:

```
The proxy's empirical envelope (L^{-5.07}) does NOT bound the predicted
HKR-image binding rate (L^{-3}) for c_L; the proxy bounds its OWN substrate-
internal convergence to its OWN reference anchor at f(L_max)=1.0, NOT the
distance to c_continuum.

⇒ The empirical envelope does NOT operationally bound ‖HKR(c_L) − c_continuum‖
  for the K-window log-derivative observable; the rule's Level-2-binding
  admissibility test is NOT satisfied per Step 3 of the canonical substitution
  chain at `cross-pillar-bridge-corpus.md §1`.
```

**Conclusion of the substitution chain.**

Per-observable extraction is REQUIRED to demonstrate Level-2-binding admissibility for any specific `c_L`. The rule's operative definition indexes the envelope by the cohomology class; registry-anchor inheritance from §VII.AF.1.OP-PROJ addresses only that an HKR `L_max → ∞` map EXISTS at the bridge-family level — it does NOT certify the binding rate `‖HKR(c_L) − c_continuum‖` for any specific observable. A registry entry that asserts Level-2-binding via inheritance without per-observable extraction is asserting a structural prediction (the binding rate) without the empirical evidence the rule's operational definition requires.

**Substrate framing**: per `phononic-framing.md §"IS Space, Not IN Space"`, the substrate IS the spectral triple at each L_max; the HKR map IS the substrate's own structural identity at L_max → ∞. The empirical envelope on `‖HKR(c_L) − c_continuum‖` IS the substrate's own claim about how fast `c_L` resolves to `c_continuum` under its own moduli-deformation. This claim is per-cocycle, NOT per-bridge-family. Inheriting a binding rate from a different cocycle in the same bridge family is structurally equivalent to claiming that all classes in HH*(A_K^{≤L}) converge at the same rate to their HKR images — a claim that the rule's per-observable definition explicitly does NOT make and that the Connes-Moscovici 1995 §III.4 residue formula does not support (different cocycles have different residue evaluations and thus different convergence behaviors).

#### C2: §"Level-2-non-binding (FORBIDDEN for registry-PASS)" — direct enforcement reading

The §"Level-2-non-binding (FORBIDDEN for registry-PASS)" definition + enforcement clause direct-applies to §W5-3 and routes §VII.AV to registry-INELIGIBLE pending CF-W5-3 full BdG re-derivation. Under my Re:L4 counter-proposal (deferred-pending state added to the enforcement clause), the strict registry-INELIGIBLE downgrades to REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE, preserving the S90 promotion path without forfeiting the per-observable extraction discipline.

**The Level-2-non-binding definition.** Per `cross-pillar-bridge-anatomy.md` lines 48-51, verbatim:

> "**Definition**: the algebraic envelope `L^{-α}` is a bare-decomposition convergence rate that does NOT bind Level-1. Operationally, the envelope bounds `‖c_L − c_∞‖` where `c_∞` is a substrate-internal limit (e.g., a bare Mellin truncation `Tr(D_K^{-2s})`) WITH NO HKR image to a continuum laboratory observable on the partner pillar.
>
> **Counter-example pattern**: a `L^{-α}` envelope on `Tr(D_K^{-2s})` evaluated at substrate-distance pole s ∈ {3, 4, ...} that lacks an HKR image to a continuum lab observable. Such an envelope describes substrate-internal Mellin-truncation convergence; it does NOT describe the convergence of any cross-pillar bridge map. The `c_continuum` reference quantity is undefined for this envelope class."

**Apply to the §W5-3 Casimir-bound proxy envelope.** The §W5-3 empirical α=5.07 envelope is structurally analogous to the counter-example pattern. I derive this via the corpus's §1 substitution chain (`cross-pillar-bridge-corpus.md` lines 23-27 verbatim):

> "**Step 3 (substitution)**: A `L^{-α}` envelope on `‖HKR(c_L) − c_continuum‖` IS a Level-2-binding envelope iff `c_continuum` is the HKR-image of the Level-1 cohomology class. ...
> **Step 4 (simplification)**: A `L^{-α}` envelope on `Tr(D_K^{-2s})` (substrate-internal Mellin moment, no HKR image to a continuum laboratory observable on the partner pillar) does NOT bind Level-1; it is a bare-decomposition envelope. The substrate-internal limit `c_∞ = lim_{L→∞} Tr(D_K^{<=L,-2s})` is an INTRINSIC substrate quantity, not a laboratory image."

Substitute the §W5-3 case into Step 3 / Step 4:

- The proxy's `c_L` = K-window log-derivative `L(L_max)` evaluated under Casimir-bound Δ_eff(L_max) = Δ_static · (L_max+1)/13 rescaling, with 8 BdG mode amplitudes (u_k, v_k, E_qp) HELD FIXED at L_max=12 values (§W5-3 line 552: "s52 8 BdG modes are FIXED structural inputs not parameterized by L_max").
- The proxy's `c_∞` = `lim_{f(L_max) → 1} L(L_max; Δ_eff(L_max))` = the proxy's L_max=12 anchor, evaluated at f(12)=1.0. This is the L_emp = -7.046336474406761 SUBSTRATE-INTERNAL fixed point of the proxy rule — NOT an HKR image to the Pillar IV continuum.
- The empirical envelope `‖L(L_max) − c_∞‖ ~ L^{-5.07}` describes the proxy's substrate-internal trajectory under the Casimir-bound rescaling rule. The convergence is to the PROXY's own L_max=12 anchor, NOT to the Peotta-Törmä BZ-trace.

The structural correspondence with the counter-example pattern at line 51:

| Counter-example pattern (rule line 51) | §W5-3 Casimir-bound proxy case |
|:----------------------------------------|:--------------------------------|
| `L^{-α}` envelope | Yes — α=5.0679 |
| On `Tr(D_K^{-2s})` (substrate-internal Mellin moment) | The proxy's substrate-internal Δ-rescaling rule (analogous: a substrate-internal reconstruction with no HKR continuation) |
| Substrate-distance pole s ∈ {3, 4, ...} | Substrate-distance-2 (s=4 fermionic-signed-residue per §W5-3 line 538) |
| Lacks HKR image to a continuum lab observable | The proxy's `c_∞` is its own L_max=12 anchor, NOT an HKR image of c_L; HKR image of `c_L` to Pillar-IV BZ-trace is the REGISTRY-LEVEL claim from §VII.AF.1.OP-PROJ for the HP¹ cocycle, NOT for THIS observable |
| Describes substrate-internal Mellin-truncation convergence | Describes substrate-internal Casimir-bound rescaling convergence |
| `c_continuum` reference quantity undefined for this envelope class | The Pillar-IV BZ-trace is the REFERENCE quantity for the HP¹ pairing's HKR image (§VII.AF.1.OP-PROJ baseline) — for the K-window log-derivative observable, the analogous reference quantity has not been empirically extracted |

The §W5-3 empirical envelope satisfies the counter-example pattern's structural conditions. Per the rule, it is a Level-2-non-binding envelope.

**The enforcement clause direction.** Per `cross-pillar-bridge-anatomy.md` lines 57-65 verbatim:

> "The registry-PASS criterion `Level-3 empirical value < Level-2 envelope value at canonical L_max` (see §"Registry-PASS criterion" above) COUNTS toward registry-PASS if and only if the Level-2 envelope is Level-2-binding per this sub-section's definition. Bare-decomposition envelopes (Level-2-non-binding) DO NOT contribute to registry-PASS regardless of how tightly the Level-3 anchor satisfies the numerical bound; their false-PASS pathway is closed by construction.
>
> Specifically:
>
> - IF Level-2-binding ∧ (Level-3 < Level-2 envelope at canonical L_max) → registry-PASS ELIGIBLE (other audit clauses still apply).
> - IF Level-2-non-binding (regardless of Level-3 vs Level-2 numerical comparison) → registry-INELIGIBLE; the bridge entry is registry-incomplete and routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum` reference quantity in the partner pillar's continuum."

Direct application to §W5-4 §VII.AV pre-registration:

- §W5-4 §VII.AV declares Level-2-binding sub-class (line 1029 "α=5.0679; R²=0.9244; Level-2-binding (sub-class explicit per §'Level-2 Layer Distinction')").
- The empirical envelope at α=5.07 is, under the operational definition, NOT a Level-2-binding envelope for the K-window log-derivative — it is a Level-2-non-binding envelope per the counter-example-pattern analysis above.
- The Level-2-binding declaration at line 1029 is therefore a MISCLASSIFICATION at the sub-class label level.
- Per enforcement clause direction-case 2 ("IF Level-2-non-binding ... → registry-INELIGIBLE; the bridge entry is registry-incomplete and routes to plan-freeze halt with remediation request to cite the HKR / Connes-Karoubi / K-theory boundary bridge map and the corresponding `c_continuum` reference quantity in the partner pillar's continuum"), §VII.AV is registry-INELIGIBLE at S89 W6 close under the strict reading.

The remediation request the enforcement clause specifies: "cite the HKR / Connes-Karoubi / K-theory boundary bridge map AND the corresponding `c_continuum` reference quantity in the partner pillar's continuum". §W5-4 cites Connes-Karoubi pairing as the bridge map (line 1015), but with "TBD final at §VII.AV landing" qualifier — the bridge map identity is NOT finalized at S89 W6 close. The `c_continuum` reference for the K-window log-derivative is also NOT independently established — §W5-4 inherits it from §VII.AF.1.OP-PROJ's HP¹ cohomology pairing, which is a structurally different observable (Cell I vs Cell IV; Kill-shot #1 territory). Both remediation conditions are unmet.

**Soft direction under the Re:L4 counter-proposal.**

Under my Re:L4 counter-proposal (clarification of the enforcement clause to add a deferred-pending intermediate state), the §VII.AV verdict softens from strict registry-INELIGIBLE to REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE. The structural argument for the softening:

- §VII.AF.1.OP-PROJ establishes that an HKR `L_max → ∞` map exists at the Pillar III ↔ Pillar IV bridge family for the HP¹ Hochschild pairing. The K-window log-derivative may eventually be shown to factor through a related HKR map (an empirical question for CF-W5-3 full BdG re-derivation).
- The §W5-3 Casimir-bound proxy is honestly disclosed as SCHEMATIC (convention tag `-CASIMIR-BOUND-PROXY` at the verdict line; line 813 cross-check (f) tags "INFO (proxy structural mismatch)"). The substrate-physics derivation at line 826 is correct on why the proxy gives α≈5 rather than α=3.
- CF-W5-3 (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`) IS the canonical promotion path — full BdG re-derivation regenerates u_k, v_k, E_qp at each L_max from the truncated D_K spectrum, producing a substrate-physics-faithful Level-2 envelope.

The deferred-pending state holds §VII.AV in registry limbo until CF-W5-3 lands:
- On CF-W5-3 PASS (full BdG re-derivation yields α ∈ [2.5, 3.5] with R² ≥ 0.95): §VII.AV promotes from REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE to registry-PASS-eligible STAGE-1-CANDIDATE; HIT K-counter advances K=1 → K=2.
- On CF-W5-3 INFO (α extracted but not in canonical band): §VII.AV remains REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE; further investigation queued.
- On CF-W5-3 FAIL (α outside [2.0, 4.5] or R² < 0.90): §VII.AV downgrades to registry-INELIGIBLE per the strict §"Level-2-non-binding" enforcement; the bridge entry is structurally falsified.

The deferred-pending state is consistent with the rule's purpose (closing the false-PASS pathway) while preserving the carry-forward discipline (CF-W5-3 IS the structural promotion path; it should not be foreclosed by a premature registry-INELIGIBLE verdict at S89 W6 close).

**On the §W5-4 disambiguation routing.** §W5-4's `outcome=corner-iv-singleton` PASS verdict (line 927) emits a positive verdict ON THE DISAMBIGUATION GATE (correctly: the gate's PASS criterion at line 918 is structural classification of the c-projection, not Level-2-binding extraction). But the disambiguation PASS does NOT promote §VII.AV to registry-PASS-eligible STAGE-1-CANDIDATE — that promotion depends on the Level-2 envelope source gate (§W5-3) delivering Level-2-binding empirical evidence. The §W5-4 PASS verdict is consistent with the deferred-pending state at §VII.AV — the disambiguation is settled (c-projection routes to Cell IV singleton), but the Level-2-binding empirical evidence remains pending.

**Concrete reading**: §"Level-2-non-binding" enforcement direct-applies. §W5-3 empirical envelope IS a Level-2-non-binding envelope under the operational definition (the proxy's `c_∞` is a substrate-internal limit, not an HKR image of c_L to the Pillar-IV continuum). Strict reading: §VII.AV is registry-INELIGIBLE. Soft reading (Re:L4 counter-proposal): §VII.AV is REGISTRY-INCOMPLETE-PENDING-FULL-BDG-REDERIVE, deferred to S90 CF-W5-3 for full physical re-derivation. Either way, §VII.AV is NOT registry-PASS-eligible STAGE-1-CANDIDATE at S89 W6 close.

#### C3: §VII.AF.1.OP-PROJ baseline — HP¹ cohomology vs K-window log-derivative as DISTINCT observables

This is the structural core of my position. The §VII.AF.1.OP-PROJ baseline anchors the HP¹ cohomology Hochschild pairing on the Jensen-deformed band-0 projector — an algebra-INVARIANT spectrum-only functional family living in Cell I per the §VII.U.2 4-corner classification. The §W5-3 K-window log-derivative is an algebra-DEPENDENT state-pair functional family living in Cell IV per §W5-3's own explicit declaration. The two observables are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level per the §"Algebra-axis orthogonality K-counter" MANDATORY-at-K=3 clause; cross-corner co-primary inheritance from Cell I to Cell IV is STRUCTURALLY FORBIDDEN per `registry-landing.md` Detection item 4. lizzi's "c-projection IS the inheritance mechanism" is precisely the structurally-forbidden pattern renamed.

**§VII.AF.1.OP-PROJ baseline — substrate-IS observable identity.**

Per `cross-pillar-bridge-anatomy.md` line 18, verbatim:

> "**Calibration (W-5)**: `‖[ε_H]‖_{HP^1, r} = |f_4^r| · R_universal` where `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` is the regulator-invariant Connes-Karoubi pairing on the Jensen-deformed band-0 projector (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula)"

The §VII.AF.1.OP-PROJ substrate-IS observable is:
- `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` — a Connes-Karoubi pairing.
- `[φ_g^{sym}]` is a Hochschild cocycle class in `HH^*(A_K^{≤L})` (the symmetric metric cocycle on the Jensen-deformed spectral triple).
- `[Ch(P_0(τ_fold))]` is the Chern character of the band-0 projector — a K-theory class.
- The pairing `⟨·, ·⟩` is the canonical Connes-Karoubi cohomology-K-theory pairing per Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula.

This pairing is REGULATOR-INVARIANT — the value `R_universal` is independent of UV-regulator choice (zeta/Pauli-Villars/Mellin) because the Connes-Karoubi pairing factors through the K-theoretic structure of the underlying spectral triple. It is an algebra-INVARIANT spectrum-only functional in the sense of `cross-pillar-bridge-corpus.md §6` lines 200: "spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`; e.g., Seeley-DeWitt moments, ζ-residues, Mellin-Dirichlet identities". The Connes-Karoubi pairing's residue evaluation depends only on the spectrum data `{λ_k, m_k}` of `D_K` per CM-1995 §III.4 — it does not depend on choice of state on `A_K`.

Per §VII.U.2 4-corner partition, this places §VII.AF.1.OP-PROJ in **Cell I** (algebra-INVARIANT × substrate-distance-1; the spectrum-only spectrum-functional cell at the Mellin pole s=3 substrate-distance-1 anchor; or substrate-distance-2 for fermionic-signed residues — but regardless, on the algebra-INVARIANT axis).

**§W5-3 K-window log-derivative — substrate-IS observable identity.**

Per §W5-3 line 538 (hypothesis statement):

> "Level-2 algebraic envelope of the Corner-IV K-window log-derivative L(L_max) converges to canonical −7.046336 as L_max^{−α} with α=3 predicted (substrate-distance-2 fermionic-signed-residue at d=4 per S86 W-5 §VII.W)"

And §W5-3 line 609 — explicit corner-cell declaration:

> "The Corner-IV K-window log-derivative at substrate-distance-2 pole s=4 is an **algebra-DEPENDENT state-pair functional** per `cross-pillar-bridge-anatomy.md §'Algebra-axis orthogonality K-counter'` MANDATORY at K=3 (since S87 W-2 R3 close); it lives on Cell IV per `permanent-results-registry.md §VII.U.2` 4-corner classification."

The §W5-3 K-window log-derivative is:
- `L(L_max) := d² ln P_GGE / d(ln K)² |_{K_horizon}` — a second log-derivative of the GGE occupation distribution.
- `P_GGE(K) = Var_a(v_K²)` — variance over the BdG mode index `a` of the squared Bogoliubov amplitudes `v_K²`.
- `v_K = v_a(K)` is the BdG state vector at quasiparticle momentum `K` — a STATE-PAIR observable on the BdG sub-algebra.
- The functional depends on the GGE state-distribution `(v_a, u_a, E_a)` per `s52_bogoliubov_amp.npz` cache, which encodes the Bogoliubov vacuum decomposition of `A` over the truncated `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`.

This is an algebra-DEPENDENT state-pair functional in the sense of `cross-pillar-bridge-corpus.md §6` line 200: "state-pair functionals on `A`; e.g., Connes distance, state expectations, sample variances over occupation distributions". The functional value depends EXPLICITLY on the state-pair decomposition `(v_a, u_a)` of the Bogoliubov vacuum on `A` — not on the spectrum data `{λ_k, m_k}` of `D_K` alone.

Per §VII.U.2 4-corner partition, this places §W5-3 in **Cell IV** (algebra-DEPENDENT × substrate-distance-2 fermionic-signed-residue family).

**The cells are STRUCTURALLY ORTHOGONAL in identity-class membership.**

Per `cross-pillar-bridge-corpus.md §6` lines 200, verbatim:

> "The algebra-axis orthogonality conjecture states: on any finite spectral triple `(A, H, D)` satisfying the 7 NCG axioms, the algebra-INVARIANT family (spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT family (state-pair functionals on `A`) are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level — there is no closed-form `{λ_n}`-only identity reproducing any algebra-DEPENDENT functional, and conversely no state-functional-only identity reproducing any algebra-INVARIANT spectral moment."

The axiomatic-skeleton derivation per `cross-pillar-bridge-corpus.md §6` lines 214-216:

> "NCG axioms 1+5 + Connes-Moscovici 1995 §III.4 dim-spectrum residue formula `a_n = Res[Tr(D^{−2s}); s = (d−n)/2] = Σ_k m_k λ_k^{−(d−n)}` GUARANTEE the algebra-INVARIANT family is non-trivial. NCG axioms 4+6 + Poincaré duality on `A_K` GUARANTEE the algebra-DEPENDENT family is non-trivial. The chirality-vs-A_F block-grading mismatch ensures `f(D²) ∩ π(A) = scalars` on the state-functional side, while the spectrum-only side is the full `Z(f(D²))` algebra. Both families are ALWAYS present; identity-class membership is structurally orthogonal by axiom-level NCG argument."

Status: MANDATORY at K=3 (promoted at S87 W-2 R3 close; corpus saturation across 3 distinct calibration instances: W1b-6 Connes distance on `M_n(ℂ)`; S-2 Connes distance on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; W-2 α_s_route_3 GGE Bogoliubov vacuum specification). The MANDATORY status forbids cross-corner co-primary structures at the plan-freeze enforcement layer.

**Plan-freeze enforcement: cross-corner co-primary FORBIDDEN.**

Per `cross-pillar-bridge-corpus.md §6` lines 218-227, verbatim:

> "Plan-freeze validators (per `_source_reconciliation_audit.py` post-V.2 extension at S88) MUST verify for any §VII registry entry on `(A_K, H_K, D_K)`:
>
> 1. **Corner-cell declaration**: every entry declares its 4-corner cell ∈ {I, II, III, IV} explicitly per the partition table in §VII.U.2.
> 2. **Cross-corner co-primary FORBIDDEN**: SOURCE-DOUBLE-CITE-CO-PRIMARY structure tags scoping anchors across distinct corner cells fail registry-landing.md §'Detection' criterion (1) by algebra-axis orthogonality.
> 3. **Cross-pole co-primary FORBIDDEN**: per W-9 RULE-3 §'Pole-Scope sub-clause'; co-primary structures must inhabit the same Mellin pole-scope.
> 4. **Cross-corner cross-pole magnitude comparisons**: STRUCTURALLY FORBIDDEN as PASS/FAIL gates; permitted in narrative analyses ONLY with explicit `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]` declaration.
>
> Missing any of (1)-(4) → registry-incompleteness FAIL, plan-freeze halt with remediation request via `_corner_classification_audit.py` (S88 CF-E)."

And `registry-landing.md` Detection item 4 lines 38-47, verbatim:

> "4. **Both anchors must be on the same algebra-axis cell** (S88 W-15 V.6; B.14) per `cross-pillar-bridge-anatomy.md §'Algebra-axis orthogonality K-counter'` MANDATORY at K=3. Cross-corner co-primary structures (one anchor on the algebra-INVARIANT spectrum-only-functional cell, the other on the algebra-DEPENDENT state-pair-functional cell) are STRUCTURALLY FORBIDDEN — the two cells live on orthogonal algebra-axes and cannot enter a single non-fungible chain. Calibration corpus instance #1 = W5a-44 surfacing of §VII.AN cross-corner ANCHOR-1+ANCHOR-2 conflation (V on Cell I `n_s²−1` image vs C on Cell IV variance theorem); registry-mis-classified at landing time per Result 5 of W-15. Forward enforcement: `_registry_landing_audit.py` extension at `S89-CROSS-CORNER-CO-PRIMARY-AUDIT` flags cross-corner SOURCE-DOUBLE-CITE-CO-PRIMARY structures at plan-freeze with HARD-HALT remediation."

The S89-CROSS-CORNER-CO-PRIMARY-AUDIT is queued precisely to flag exactly this kind of cross-corner inheritance pattern. The W5a-44 instance (calibration corpus instance #1) IS the canonical worked example: V-anchor on Cell I `n_s²−1` image + C-anchor on Cell IV variance theorem = cross-corner co-primary; the W-15 V.6 audit found the structure registry-mis-classified and required remediation.

**lizzi's "c-projection" mechanism IS the cross-corner co-primary pattern renamed.**

lizzi at L2 line 83 reads: "the c-projection from Pillar II Mellin-Barnes residue (substrate-IS at the Pillar-II abstract algebra level) DOWN TO Cell IV via the K-window log-derivative ANCHOR (a Pillar IV-canonical observable inherited from §W5-3 / A.25 / A.26) IS the inheritance mechanism. The K-window log-derivative is the SAME observable as the one anchored at §VII.AF.1.OP-PROJ's Pillar III ↔ Pillar IV bridge".

There are two distinct structural errors in this passage:

**Error 1**: the "c-projection" from Cell I to Cell IV is identically the cross-corner co-primary pattern. Let me deploy the chain:

```
ANCHOR-1 (V): §VII.AF.1.OP-PROJ HP¹ Hochschild pairing R_universal at Cell I
              (algebra-INVARIANT spectrum-only on Jensen-deformed band-0 projector)

ANCHOR-2 (C): §W5-3 K-window log-derivative L(L_max) at Cell IV
              (algebra-DEPENDENT state-pair on BdG sub-algebra)

CHAIN:  V is the registry-anchor for HKR map identification at Pillar III ↔ Pillar IV
        bridge family.
        C is the per-observable Level-2-binding declaration for the FWD-C2
        substrate-IS observable (under lizzi's c-projection mechanism).
        Per the proposed inheritance: V supplies the HKR-map-existence premise;
        C inherits the binding declaration via c-projection.
        The two anchors are non-fungible (V supplies the registry-anchor; C is
        the per-observable instantiation); neither can be removed without
        breaking the inheritance chain.

STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (per registry-landing.md §"Detection")

VERDICT: Detection item 4 FAILS — ANCHOR-1 lives on Cell I (algebra-INVARIANT);
         ANCHOR-2 lives on Cell IV (algebra-DEPENDENT). The two anchors are on
         DIFFERENT algebra-axis cells. Cross-corner co-primary is STRUCTURALLY
         FORBIDDEN per the MANDATORY-at-K=3 clause.
```

The "c-projection" name does not change the structural classification. The mechanism inherits a binding-rate declaration across algebra-axis cells; the algebra-axis orthogonality MANDATORY clause forbids this; the W5a-44 calibration instance is precedent for the remediation route (registry-mis-classification at landing time, HARD-HALT at plan-freeze).

**Error 2**: lizzi's claim that "The K-window log-derivative is the SAME observable as the one anchored at §VII.AF.1.OP-PROJ's Pillar III ↔ Pillar IV bridge" is FACTUALLY WRONG at the substrate-IS observable identity level. The §VII.AF.1.OP-PROJ substrate-IS observable is `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` — a Connes-Karoubi cohomology-K-theory pairing on a Hochschild cocycle and a Chern character. The §W5-3 substrate-IS observable is `L(L_max) = d² ln P_GGE / d(ln K)² |_{K_horizon}` — a state-pair second log-derivative of a Bogoliubov occupation variance. These are not the same observable; they are STRUCTURALLY DIFFERENT observables that happen to share the same partner pillar (Pillar IV) for their HKR continuum images at the bridge-family level.

The cohomology classes themselves are different objects:
- `[φ_g^{sym}] ∈ HH^*(A_K^{≤L})` is a Hochschild cocycle class (NCG axioms 1+5 + CM-1995 §III.4 residue formula generate it).
- `[L]` is NOT a Hochschild cocycle class in the same algebra-INVARIANT family; it is a state-pair functional on the BdG sub-algebra (NCG axioms 4+6 + Poincaré duality generate it on the algebra-DEPENDENT family).

The chirality-vs-A_F block-grading mismatch (per `cross-pillar-bridge-corpus.md §6` line 216: "`f(D²) ∩ π(A) = scalars` on the state-functional side, while the spectrum-only side is the full `Z(f(D²))` algebra") makes the two classes structurally non-comparable at the identity-class level. There is no closed-form `{λ_n}`-only identity reproducing `[L]`; conversely, there is no state-functional-only identity reproducing `R_universal`. The two cohomology classes live on orthogonal algebra-axes.

**Consequence: the §VII.AF.1.OP-PROJ HKR-image identification is NOT transferable to the K-window log-derivative.**

The §VII.AF.1.OP-PROJ bridge identification names:
- Substrate-IS = `R_universal` (Cell I HP¹ Hochschild pairing).
- Laboratory-IN = `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` (Pillar IV Peotta-Törmä BZ-trace).
- Bridge map = HKR `L_max → ∞`.
- Algebraic envelope = `L^{-3}` at d=4.

The HKR map identifies `[φ_g^{sym}]`'s class image with `R_geom` — a per-cocycle statement. For the K-window log-derivative `[L]`, the analogous bridge identification would name:
- Substrate-IS = `L` (Cell IV K-window log-derivative state-pair functional).
- Laboratory-IN = SOME Pillar-V/Pillar-IV laboratory observable that is the HKR image of `[L]` — NOT necessarily `R_geom` (which is the HKR image of `[φ_g^{sym}]`, a DIFFERENT cocycle).
- Bridge map = some explicit map (HKR / Connes-Karoubi pairing / K-theory boundary) for `[L]` — this map has NOT been independently registered at any §VII entry.
- Algebraic envelope = some `L^{-α}` rate for `[L]`'s HKR image — this rate is the per-observable empirical question that CF-W5-3 is designed to answer.

The §VII.AF.1.OP-PROJ baseline establishes that the Pillar III ↔ Pillar IV bridge family admits HKR `L_max → ∞` images for ONE cocycle class (HP¹ pairing). It does NOT establish that ALL classes in this family admit HKR images, nor that those images have the same partner-pillar laboratory observable, nor that they converge at the same rate.

**Per-observable extraction is required.**

The conclusion: per-observable HKR map identification + per-observable empirical Level-2 envelope extraction is REQUIRED for any registry entry asserting Level-2-binding admissibility. Registry-anchor inheritance from §VII.AF.1.OP-PROJ addresses only the bridge-family-level existence of HKR maps — it does not certify the binding map, the laboratory-IN partner, or the convergence rate for any specific observable.

lizzi's "c-projection IS the inheritance mechanism" is a clause-(4) violation of `registry-landing.md`. The mechanism inherits across orthogonal algebra-axis cells, is forbidden by the MANDATORY-at-K=3 clause, and routes to plan-freeze HARD-HALT per the S89-CROSS-CORNER-CO-PRIMARY-AUDIT extension.

**Substrate framing**: per `phononic-framing.md §"IS Space, Not IN Space"`, the substrate IS the spectral triple `(A_K, H_K, D_K)` at each L_max. The HP¹ Hochschild pairing and the K-window log-derivative are TWO STRUCTURALLY DIFFERENT observables on the SAME substrate — they probe different aspects of the same finite-L spectral triple structure. Inheriting a binding-rate declaration from one to the other is structurally equivalent to claiming that two different cohomology classes resolve at the same rate to their HKR images under the L_max → ∞ moduli-deformation — a claim the per-class operational definition of Level-2-binding does NOT make, and that the algebra-axis orthogonality K-counter at K=3 MANDATORY explicitly forbids.

#### C4: Questions for lizzi (must answer R2)

I pose four sharp questions for R2. Each pins to a specific rule-text citation that lizzi must address — either by citing a documented exception, by admitting the structural force, or by counter-citing a rule-text passage I have missed.

**Q1 (Kill-shot #1 — algebra-axis orthogonality).**

Your "c-projection inheritance mechanism" at L2 line 83 carries the Level-2-binding declaration from §VII.AF.1.OP-PROJ (HP¹ Hochschild pairing on Cell I, algebra-INVARIANT spectrum-only) to the §W5-3 K-window log-derivative (Cell IV, algebra-DEPENDENT state-pair per §W5-3 line 609 explicit declaration). Per `cross-pillar-bridge-corpus.md §6` lines 222-225 + `registry-landing.md` Detection item 4 (S88 W-15 V.6; B.14), cross-corner co-primary structures (one anchor algebra-INVARIANT Cell I; the other anchor algebra-DEPENDENT Cell IV) are STRUCTURALLY FORBIDDEN under the MANDATORY-at-K=3 algebra-axis orthogonality clause.

**Where in the rule text is the exception that admits cross-corner inheritance via "c-projection"?** Cite the specific rule-text passage that would override the MANDATORY-at-K=3 clause. If no such exception is documented, on what grounds does your L4 sub-clause line 159 parenthetical ("the c-projection IS the inheritance mechanism, not a violation of the cross-corner prohibition") avoid being a SUGGESTION-status K=1 entry attempting to legislate an exception to a MANDATORY rule?

**Q2 (Kill-shot #2 — §VII.AG.1 precedent breaks for K-counter advancing entries).**

§VII.AG.1 was tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` OUTSIDE the K-counter precisely because the Hybrid Independence Test substitution chain failed all 4 clauses (`cross-pillar-bridge-corpus.md §3` lines 96-102 verbatim: clause (i) FAILS, clause (ii) FAILS, clause (iii) FAILS, disjunction FALSE). §W5-4 SEEKS K-counter advancement explicitly ("counts toward Hybrid Independence Test K-counter advancement (K=1→K=2 path opened)", §W5-4 line 996); §W5-4 claims HIT all 4 clauses TRUE (§W5-4 lines 968-986). These are STRUCTURALLY INCOMPATIBLE inheritance modes — §VII.AV cannot simultaneously be (a) a SHARED-ANCHOR-COMPANION that inherits binding-class declaration from §VII.AF.1.OP-PROJ AND (b) a K-counter-advancing independent calibration instance under the Hybrid Independence Test.

Your L2 line 85 invents a manufactured two-track distinction ("the Level-2-binding CLASS inheritance — the substrate's claim that the HKR-map exists at the Pillar III ↔ Pillar IV layer is the registry-anchor; ... §W5-4's FWD-C2 candidate then BUILDS on this anchor by c-projecting Pillar II's Mellin-Barnes residue to the Cell IV anchor and lifting to Pillar V via Connes-Karoubi"). The only documented two-clause separation in the parent rule is at lines 279-295 §"Two-clause separation: registry-PASS (per-entry) vs K-counter advancement (rule-level corpus)" — a separation between PER-ENTRY epistemic adequacy and CORPUS saturation; this is NOT a separation between "binding-class inheritance" and "HIT K-counter advancement".

**Where in the rule text is the documented two-track distinction between "Level-2-binding CLASS inheritance" and "HIT K-counter advancement" that your L2 line 85 invokes?** If no such distinction is documented, on what grounds do you assert it? Specifically: cite the rule-file location (with line numbers) where this distinction is registered, OR concede that the distinction is manufactured for §W5-4 and lacks rule-text basis.

**Q3 (Kill-shot #3 — §W5-4 substrate-IS observable identity inconsistency).**

§W5-4 line 898 (machinery pin) declares `FWD_C2_substrate_pillar | Pillar II (Mellin-Barnes residue)`. §W5-4 line 1011 (5-anatomy Step 6 declaration) declares `1. substrate-IS observable: K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) (inherited from A.25/A.26)`. These are TWO DIFFERENT observables on TWO DIFFERENT pillars in TWO DIFFERENT corner cells (Pillar II Mellin-Barnes = algebra-INVARIANT Cell II vs Pillar III/IV K-window log-derivative = algebra-DEPENDENT Cell IV).

**Which is the actual substrate-IS observable for the §VII.AV registration?**

- **If it is the K-window log-derivative** (line 1011 reading): then §W5-4's bridge classification at line 898 (Pillar II ↔ Pillar V) is INCORRECT. The K-window log-derivative is a Pillar III/IV observable; the bridge would be Pillar III/IV ↔ Pillar V, which is a different FWD candidate (closer to FWD-C3 per `cross-pillar-bridge-corpus.md §4` Pillar IV ↔ Pillar V). The Hybrid Independence Test substitution chain at §W5-4 lines 968-986 collapses (clause (i) substrate-pillar-distinct becomes FAIL against §VII.AF.1.OP-PROJ which is Pillar III) and the K-counter advancement claim falls through.
- **If it is the Pillar II Mellin-Barnes residue** (line 898 reading): then §W5-4 has performed NO per-observable empirical Level-2 envelope extraction on the Pillar II Mellin-Barnes residue. The §W5-3 α=5.07 is on the K-window log-derivative, a DIFFERENT observable; importing that envelope to §W5-4 §VII.AV is the cross-corner co-primary pattern (Pillar II Cell II ↔ Pillar III/IV Cell IV) which is structurally FORBIDDEN.

**Pick one. Either §VII.AV is mis-classified as Pillar II ↔ Pillar V (it is actually Pillar III/IV ↔ Pillar V), OR §W5-4 has performed no per-observable extraction on the Pillar II Mellin-Barnes residue. Which is your reading?** Address both legs of the dilemma — the §W5-4 5-anatomy declaration at Element 1 cannot remain INCOMPLETE-OR-CONFUSED across two different observables.

**Q4 (Re:L4 — counter-proposed deferred-pending state).**

I have counter-proposed a rule extension that is a CLARIFICATION of the existing §"Level-2-non-binding" enforcement clause (lines 57-65), adding a NEW intermediate case `REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION` between the existing IF Level-2-binding (PASS-ELIGIBLE) and IF Level-2-non-binding (INELIGIBLE) cases. The deferred-pending state holds §VII.AV in registry limbo until CF-W5-3 full BdG re-derivation lands; on CF-W5-3 PASS, §VII.AV promotes to registry-PASS-eligible STAGE-1-CANDIDATE in S90+.

The counter-proposal preserves:
- The per-observable extraction requirement (no Level-2-binding admissibility without per-observable empirical evidence).
- The MANDATORY-at-K=3 cross-corner co-primary prohibition (the deferred-pending state requires the per-observable extraction at the inheriting observable's OWN corner cell, not via cross-corner inheritance).
- The audit-trail discipline (the SCHEMATIC proxy envelope is preserved as carry-forward provenance, not registry-eligible content).
- The CF-W5-3 promotion path (deferred-pending IS the structural route to registry-PASS-eligible STAGE-1-CANDIDATE, NOT a foreclosure).

Your L4 sub-clause proposes the OPPOSITE direction: admit Level-2-binding declaration via cross-bridge-family inheritance, close per-gate INFO on the SCHEMATIC proxy, pre-register STAGE-1-CANDIDATE at S89 W6 close without per-observable extraction. This opens a false-PASS pathway that the existing Level-2 Layer Distinction was authored to close.

**Do you accept the counter-proposed REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION deferred-pending state as a better resolution than your proposed registry-anchor inheritance SUGGESTION sub-clause?**

Specifically: if your concern is preserving the CF-W5-3 promotion path in S90+, the deferred-pending state achieves that without bypassing per-observable extraction. If your concern is recognizing that the HKR map exists at the bridge-family level, the deferred-pending state preserves the bridge-family identification (via your L4 condition (a) of citing the registry-anchor §-reference) while withholding STAGE-1-CANDIDATE promotion until the per-observable extraction lands. What structural advantage does your sub-clause provide that the deferred-pending state does not?

**Bonus: on §W5-6 / §VII.AU template-inheritance.**

If your answer to Q4 is "the deferred-pending state is acceptable for §VII.AV", does the same routing apply to §VII.AU? §W5-6 performs NO L_max scan at all (machinery pin line 1511 declares envelope_alpha_predicted=3 by structural-exact template assertion). Under the per-observable extraction reading, §VII.AU is in a structurally WEAKER position than §VII.AV (zero empirical evidence on the FWD-C1 observable's L_max convergence vs §VII.AV's SCHEMATIC proxy evidence). Both should route to REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION under the counter-proposal — §VII.AU via a new S90 carry-forward `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL` (no existing scan to refine). Do you agree that the FWD-C1 candidate needs a per-observable L_max scan before §VII.AU promotes to registry-PASS-eligible STAGE-1-CANDIDATE?

### C5: Round-1 connes carry-forward (4-field spec per `feedback_fix-in-session-never-defer.md`)

Per `feedback_fix-in-session-never-defer.md`, each carry-forward computation MUST have all four fields: What / Inputs / Gate / Estimated effort.

#### Carry-Forward #C5.1 — Full BdG re-derivation at Corner-IV K-window log-derivative, with deferred-pending promotion semantics

This is the same computational gate that lizzi proposes at L6.1 (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`), with a structurally DIFFERENT downstream gate semantics: under my Re:L4 counter-proposal, the gate's PASS does NOT just refine α on an already-registered STAGE-1-CANDIDATE; it PROMOTES §VII.AV from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION to registry-PASS-eligible STAGE-1-CANDIDATE. The empirical α extraction is the GATE for registry-eligibility, not a refinement of an entry already pre-registered as STAGE-1-CANDIDATE.

- **What**: Refine the empirical envelope α extraction at the Corner-IV K-window log-derivative substrate-IS observable by performing a FULL BdG re-derivation at each L_max ∈ {6, 7, 8, 9, 10, 11, 12} instead of the Casimir-bound Δ_eff(L_max) = Δ_static · (L_max+1)/13 proxy. The full re-derivation re-runs the BCS gap equation `1/V = Σ_a 1/(2 E_a) tanh(E_a/2T)` on the L_max-truncated D_K spectrum at each L_max value (regenerating both `Δ` and the 8 BdG mode amplitudes u_k, v_k, E_qp from the truncated spectral kernel). Then evaluates L_emp(L_max) via the §W5-2 numerical core. Output: refined `envelope_alpha`, `envelope_R²`, `envelope_log_A` over the 7 L_max sectors. The PASS verdict TRIGGERS §VII.AV promotion from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION to registry-PASS-eligible STAGE-1-CANDIDATE (per my Re:L4 counter-proposed enforcement clause clarification). FAIL/INFO routes per the standard `cross-pillar-bridge-anatomy.md §"Level-2-non-binding"` enforcement direction-table.

- **Inputs**:
  - `computations/session-52/s52_bogoliubov_amp.npz` (8-mode B1+B2+B3 BdG canonical amplitudes at L_max=12 reference; at L_max < 12 the modes are RE-DERIVED from the L_max-truncated spectral kernel, not just rescaled).
  - `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (full L_max=12 D_K spectrum cache; 90 Peter-Weyl sectors; per `math-scripts.md §"Machinery-Feasibility Audit"` Casimir-bound feasibility check + Friedrich-Bär saturation theorem cross-check).
  - `computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz` (canonical anchor L_emp(∞) = -7.046336474406761 bit-for-bit per §W5-2 PASS).
  - `computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.npz` (Casimir-bound proxy α=5.0679 / R²=0.9244 reference for proxy-fidelity bias quantification).
  - canonical_constants.py: M_KK, tau_fold, Delta_BCS, M_KK-anchored BCS gap-equation parameters; n_modes_static = 8 (FIXED branch index at the underlying SU(3) Peter-Weyl decomposition; the L_max truncation operates on D_K spectrum, not on the BdG mode count).
  - `cross-pillar-bridge-anatomy.md` (parent rule for the §VII.AV promotion semantics under the Re:L4 counter-proposed enforcement clause clarification).
  - `permanent-results-registry.md §VII.AV` (the deferred-pending entry to promote on PASS).
  - `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` (this workshop's R3 verdict text as the substitution-chain provenance for the promotion semantics).

- **Gate**: `S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS`. Pre-registered PASS criterion: extracted α ∈ [2.5, 3.5] (1-sigma band around predicted α=3 at substrate-distance-2 d=4 per S86 W-5 §VII.W) AND R² ≥ 0.95 (VALID band; tighter than §W5-3's MARGINAL [0.90, 0.95)) AND L_max=12 bit-for-bit anchor match (|L_emp(12) − (-7.046336474406761)| < 1e-9). PASS verdict TRIGGERS §VII.AV promotion from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION to registry-PASS-eligible STAGE-1-CANDIDATE. INFO band: α ∈ [2.0, 2.5) ∪ (3.5, 4.5] OR R² ∈ [0.90, 0.95) — §VII.AV remains in REGISTRY-INCOMPLETE-PENDING state; further investigation queued. FAIL: α outside [2.0, 4.5] OR R² < 0.90 OR L_max=12 anchor mismatch — §VII.AV downgrades to registry-INELIGIBLE per the §"Level-2-non-binding" strict enforcement; the bridge entry is structurally falsified. The gate ALSO produces a proxy-fidelity bias estimate: `bias_factor = α_proxy / α_full_bdg = 5.0679 / α_extracted`, reported alongside the canonical α; quantifies the SCHEMATIC vs full physical regularization gap for retrospective audit-trail use.

- **Estimated effort**: 1 agent-session (volovik-superfluid-universe-theorist PRIMARY for the substrate-physics BdG re-derivation, connes-ncg-theorist CO-AUTHOR for the registry-promotion semantics + bridge-anatomy audit cross-check on Element 1 disambiguation per Kill-shot #3 resolution). Wall-time estimate: ~30-60 min on AMD RX 9070 XT GPU for the 7-L_max BCS gap-equation iterative self-consistent solver + Bogoliubov diagonalization at each L_max sector (Peter-Weyl block-diagonal; sparse Lanczos via `torch.linalg` on GPU; per `math-scripts.md §"Machinery-Feasibility Audit"` D_K Block-Diagonality pre-check).

- **Depends on**: §VII.AV deferred-pending registration under counter-proposed Re:L4 enforcement clause clarification (lands at S90 W0 via Carry-Forward #C5.2 below); CF-W5-3 (lizzi L6.1 carry-forward; structurally subsumed under this carry-forward with promotion semantics added).

#### Carry-Forward #C5.2 — Land counter-proposed rule-file diff (§"Level-2-non-binding" enforcement clause clarification)

- **What**: Land the counter-proposed clarification of `cross-pillar-bridge-anatomy.md §"Enforcement clause"` (parent rule lines 57-65) per the Re:L4 BEFORE/AFTER patch I provided. The clarification adds a NEW intermediate case `REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION` between the existing IF Level-2-binding (PASS-ELIGIBLE) and IF Level-2-non-binding (INELIGIBLE) cases. The new case fires when (i) Level-2-binding-by-construction-anchor is declared (HKR map exists at the bridge-family level per a prior registry anchor) AND (ii) Level-2 envelope is EXTRACTED-UNDER-SCHEMATIC-PROXY AND (iii) empirical α falls OUTSIDE predicted α band. The deferred-pending state holds the entry pending full physical re-derivation at canonical L_max. The clarification PRESERVES the per-observable extraction requirement (Level-2-binding admissibility test remains operational on `‖HKR(c_L) − c_continuum‖` for the SPECIFIC observable), preserves the registry-PASS-eligibility timing discipline (no STAGE-1-CANDIDATE pre-registration without per-observable extraction), preserves the audit-trail of SCHEMATIC proxy disclosures, and preserves the MANDATORY-at-K=3 cross-corner co-primary prohibition. Extend `computations/_shared/_cross_pillar_bridge_audit.py` with a sub-check: regex-detect `convention=.*-(?:SCHEMATIC|PROXY)` in producing-script verdict-line emission; cross-reference whether the empirical α falls outside the predicted band; on positive match, emit MANDATORY remediation flagging the registry slot as REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION rather than STAGE-1-CANDIDATE.

- **Inputs**:
  - `.claude/rules/cross-pillar-bridge-anatomy.md` (parent rule file; 323 lines; current state at S89 W6 close).
  - `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (Level-2 Layer Distinction calibration corpus extension target; counter-proposal lands as Calibration #3 NEGATIVE-CALIBRATION instance with §W5-3 Casimir-bound proxy as the SCHEMATIC-proxy worked example).
  - `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` (this workshop's R3 verdict text as the substitution-chain provenance for the rule-file diff).
  - `computations/_shared/_cross_pillar_bridge_audit.py` (audit script to extend with the SCHEMATIC-proxy regex sub-check).
  - `.claude/rules/methodology-wave-allowlist.md` (append gate-ID with computed sha256_of_plan_block per the append-only orchestrator-only-edit discipline).
  - `.claude/rules/registry-landing.md §"Detection"` (Detection item 4 cross-corner co-primary FORBIDDEN; the rule-file diff explicitly preserves the cross-corner prohibition).

- **Gate**: `S90-LEVEL-2-NON-BINDING-ENFORCEMENT-CLARIFICATION-DEFERRED-PENDING-LANDING` (rule-file edit gate; METHODOLOGY-class per `wave-classification.md §M4`). Pre-registered PASS criterion (per `wave-classification.md §M1`): (i) the diff is applied verbatim at parent rule lines 57-65 enforcement clause; (ii) the audit-script regex extension is committed with positive-match (W5-3 Casimir-bound proxy at α=5.07 outside band) and negative-match (a hypothetical SCHEMATIC envelope at α within predicted band) test cases passing; (iii) the corpus instance is logged at `cross-pillar-bridge-corpus.md §1` as Calibration #3 NEGATIVE-CALIBRATION worked example; (iv) the gate-ID is appended to `methodology-wave-allowlist.md` with computed `sha256_of_plan_block`; (v) the rule extension is SUGGESTION at K=1 with §W5-3/§W5-4 as the K=1 calibration instance; promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md`. Dual-SHA closure per `gate-verdicts.md` S87+ schema-v2.

- **Estimated effort**: 0.5 agent-session (connes-ncg-theorist PRIMARY for the rule-file diff per Re:L4 BEFORE/AFTER patch + audit-script regex extension; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` for the corpus row landing at `cross-pillar-bridge-corpus.md §1` Calibration #3; orchestrator-direct-write convention path per `wave-classification.md §"Dispatch consequences"`). Honest-disclosure rule-file edit per the W9c-1 positive-calibration model: the convention tag carries explicit SUGGESTION-status + K=1-advisory tag.

- **Depends on**: §W6 R3 convergence on the Re:L4 counter-proposal direction (workshop R2 + R3 must converge on REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION as the deferred-pending state; if lizzi accepts the deferred-pending state at R2 CONVERGENCE, this carry-forward lands cleanly in S90 W0).

#### Carry-Forward #C5.3 — Per-observable L_max scan at FWD-C1 parameterized slope_A canonical (§VII.AU)

This is the §VII.AU analog of Carry-Forward #C5.1. §W5-6 performed NO L_max scan on the FWD-C1 substrate-IS observable; the §VII.AU registration is in a structurally weaker position than §VII.AV under the per-observable extraction reading. This carry-forward delivers the missing per-observable extraction.

- **What**: Perform a full per-observable L_max scan on the FWD-C1 substrate-IS observable (parameterized slope_A canonical → c_sub_corrected → n_s_recomputed Mellin-cone closure) across L_max ∈ {6, 7, 8, 9, 10, 11, 12}. At each L_max sector, evaluate c_sub_corrected via the M_Pl_eff² ratio on the L_max-truncated `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})`; compute n_s_recomputed via the Route-B identity; extract the empirical envelope α via log-log linear regression on `|n_s_recomputed(L_max) − n_s_FW_exact|` vs L_max. Output: empirical α, R², log_A for the FWD-C1 substrate-IS observable; comparison to the structural-exact template prediction α=3 at d=4. PASS verdict TRIGGERS §VII.AU promotion from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION (under the Re:L4 counter-proposed deferred-pending state) to registry-PASS-eligible STAGE-1-CANDIDATE.

- **Inputs**:
  - `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (full L_max=12 D_K spectrum cache).
  - canonical_constants.py: `n_s_FW_exact = Fraction(9561, 10000)`, `slope_A_FW_Conv_A_GEOMETRIC = "10.0 / (1 - tau/(5*pi))"`, `tau_fold = 0.19`, `c_sub_baseline = 2.238`, `planck_ns = 0.9649`.
  - `cross-pillar-bridge-anatomy.md` (parent rule; FWD-C1 candidate spec at `cross-pillar-bridge-corpus.md §4`).
  - `permanent-results-registry.md §VII.AU` (the deferred-pending entry to promote on PASS).
  - `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6` (template-inheritance baseline for cross-check against the L_max=10 single-point evaluation).
  - `computations/session-89/s89_w5_a30_fwd_c1_retry_parameterized_slope_A_canonical.npz` (S89 W5-6 single-L_max=10 reference for cross-check).

- **Gate**: `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS`. Pre-registered PASS criterion: extracted α ∈ [2.5, 3.5] (1-sigma band around predicted α=3 at substrate-distance-1 d=4 per FWD-C1 spec) AND R² ≥ 0.95 AND L_max=10 anchor match (|n_s_recomputed(10) − n_s_FW_exact| < 1e-9). PASS TRIGGERS §VII.AU promotion. INFO/FAIL semantics analogous to C5.1.

- **Estimated effort**: 1 agent-session (lizzi-spectral-functional-theorist PRIMARY for the Mellin-cone closure spectral evaluation + log-log regression, connes-ncg-theorist CO-AUTHOR for the §VII.AU registry-promotion semantics + Pillar I ↔ Pillar II bridge-family HKR map identification at the FWD-C1 candidate level — which is a separate cross-pillar bridge anchor distinct from §VII.AF.1.OP-PROJ Pillar III ↔ Pillar IV per Re:L5 line above). Wall-time: ~30-60 min on AMD RX 9070 XT GPU; per-L_max Mellin-cone evaluation is small workload.

- **Depends on**: Re:L4 counter-proposed rule-file diff landed at S90 W0 via Carry-Forward #C5.2 (the deferred-pending state must exist as a valid registry verdict before §VII.AU can be in it); §VII.AU initial deferred-pending registration via mack-cosmic-bridge sole-writer at S90 W0 (parallel to §VII.AV deferred-pending registration).

#### Note on the L6.1 carry-forward overlap

Lizzi's L6.1 carry-forward (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`) is structurally subsumed under my C5.1 carry-forward with explicit promotion semantics added. The computational work is identical (full BdG re-derivation at 7 L_max values); the structural difference is the downstream gate semantics. Under lizzi's L6.1 reading, the carry-forward refines an already-pre-registered STAGE-1-CANDIDATE; under my C5.1 reading, the carry-forward IS the gate that determines whether §VII.AV achieves STAGE-1-CANDIDATE status at all. The two readings are not in computational conflict — both compute the same numerical artifact — but they imply different registry-state machinery. The Round 2 / Round 3 convergence should pick one promotion semantics; my Re:L4 counter-proposal argues for the latter (deferred-pending PROMOTION-on-PASS) on grounds of preserving the per-observable extraction discipline at registry-PASS-eligibility timing.

Lizzi's L6.2 carry-forward (her proposed `§"Level-2-binding inheritance from registry anchor"` SUGGESTION sub-clause landing) is structurally INCOMPATIBLE with my C5.2 counter-proposal: lizzi's sub-clause OPENS the inheritance pathway while my counter-proposal CLOSES it by adding the deferred-pending intermediate state. R2 / R3 convergence should adjudicate which rule-file diff lands at S90 W0 — they cannot both land (the structural directions are opposing).

---

## Round 2 — lizzi: Follow-up (Rebut + Converge)

### CONVERGENCE — Where lizzi now agrees with connes

After re-reading the parent rule text and `registry-landing.md` Detection item 4 verbatim against my R1 L2-L4 position, three of connes's R1-B Kill-shots have structural force I cannot rebut. I converge explicitly on each.

#### CONVERGE on Kill-shot #1 — cross-corner co-primary FORBIDDEN (algebra-axis orthogonality)

I read the operative rule-text passages verbatim:

`cross-pillar-bridge-corpus.md §6` lines 222-223:

> "1. **Corner-cell declaration**: every entry declares its 4-corner cell ∈ {I, II, III, IV} explicitly per the partition table in §VII.U.2.
> 2. **Cross-corner co-primary FORBIDDEN**: SOURCE-DOUBLE-CITE-CO-PRIMARY structure tags scoping anchors across distinct corner cells fail registry-landing.md §'Detection' criterion (1) by algebra-axis orthogonality."

`registry-landing.md` Detection item 4 verbatim (lines 45-46):

> "4. **Both anchors must be on the same algebra-axis cell** (S88 W-15 V.6; B.14) per `cross-pillar-bridge-anatomy.md §'Algebra-axis orthogonality K-counter'` MANDATORY at K=3. Cross-corner co-primary structures (one anchor on the algebra-INVARIANT spectrum-only-functional cell, the other on the algebra-DEPENDENT state-pair-functional cell) are STRUCTURALLY FORBIDDEN — the two cells live on orthogonal algebra-axes and cannot enter a single non-fungible chain."

`cross-pillar-bridge-corpus.md §6` line 200 axiomatic-skeleton statement:

> "the algebra-INVARIANT family (spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT family (state-pair functionals on `A`) are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level — there is no closed-form `{λ_n}`-only identity reproducing any algebra-DEPENDENT functional, and conversely no state-functional-only identity reproducing any algebra-INVARIANT spectral moment."

Apply this to my L2 line 83-85 "c-projection IS the inheritance mechanism" reading. The chain my R1 proposed:

- ANCHOR-1 (V): §VII.AF.1.OP-PROJ HP¹ Hochschild pairing on Cell I (algebra-INVARIANT, spectrum-only Connes-Karoubi pairing).
- ANCHOR-2 (C): §W5-3 K-window log-derivative on Cell IV (algebra-DEPENDENT state-pair functional per §W5-3 line 609 explicit declaration).
- Structure: non-fungible sequential dependence (V supplies HKR-map-existence; C is per-observable instantiation under c-projection).

This IS the SOURCE-DOUBLE-CITE-CO-PRIMARY shape per `registry-landing.md` Detection items 1-3 (sequential, non-fungible, both anchors remain accessible). Detection item 4 then fires: ANCHOR-1 Cell I + ANCHOR-2 Cell IV is precisely the cross-corner pattern the MANDATORY-at-K=3 clause forbids. The clause does not contain a "c-projection routes the inheritance through a Cell-IV-canonical observable" escape hatch; it forbids cross-corner co-primary structures, period. The W5a-44 §VII.AN calibration-corpus instance (V on Cell I `n_s²−1` image vs C on Cell IV variance theorem) is the canonical worked example of the forbidden pattern — and the W5a-44 audit at S88 W-15 V.6 routed it to registry-mis-classification remediation, not to admissibility under a c-projection carve-out.

The structural error in my L2 reading: I conflated TWO claims that the parent rule deliberately separates.

- **Claim A** (rule-text-supported): an HKR map EXISTS for the Pillar III ↔ Pillar IV bridge family at the registry-anchor layer (per §VII.AF.1.OP-PROJ's REGULATOR-INVARIANT Connes-Karoubi pairing on the Jensen-deformed band-0 projector).
- **Claim B** (NOT rule-text-supported): the HKR-image binding RATE for the HP¹ Hochschild pairing cocycle `[φ_g^{sym}]` propagates to OTHER cocycle classes in the same bridge family, including across the algebra-INVARIANT / algebra-DEPENDENT axis boundary.

Claim B is what my L2 line 85 manufactured two-track distinction asserts. The axiomatic-skeleton derivation at `cross-pillar-bridge-corpus.md §6` lines 214-216 explicitly forbids this: "the chirality-vs-A_F block-grading mismatch ensures `f(D²) ∩ π(A) = scalars` on the state-functional side, while the spectrum-only side is the full `Z(f(D²))` algebra. Both families are ALWAYS present; identity-class membership is structurally orthogonal by axiom-level NCG argument." If identity-class membership is structurally orthogonal at the functional-class level, the HKR-image binding RATE for one class cannot be transported to another class across cells. Connes-Moscovici 1995 §III.4 residue formula is per-cocycle; binding rates are per-class.

**I converge**: under the current rule-text, the c-projection inheritance mechanism I proposed at L2 line 83 cannot survive the MANDATORY-at-K=3 cross-corner co-primary FORBIDDEN clause. My L4 line 159 parenthetical attempting to legislate a c-projection exception is a SUGGESTION-status K=1 entry that cannot abrogate a MANDATORY clause. The L4 sub-clause as written opens precisely the false-PASS pathway that `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction (S88 W8-88 hardening)"` was authored to close. I retract the c-projection inheritance mechanism reading at L2 and the L4 sub-clause that codifies it. The cross-corner FORBIDDEN clause is structurally sound and rules against my L2-L4 position for §VII.AV.

#### CONVERGE on Kill-shot #3 — §W5-4 Element-1 ambiguity

I re-read §W5-4 lines 898 and 1011 verbatim and confirm connes's structural reading:

- §W5-4 line 898 (machinery PIN MAP, FWD-C2 disambiguation block): `FWD_C2_substrate_pillar | Pillar II (Mellin-Barnes residue)`.
- §W5-4 line 1011 (5-anatomy Step 6, Element 1 declaration): `1. substrate-IS observable: K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) (inherited from A.25/A.26)`.

These name DIFFERENT observables on DIFFERENT pillars in DIFFERENT corner cells. The Mellin-Barnes residue is an algebra-INVARIANT spectrum-only functional on the Pillar II Mellin-cone (Cell II). The K-window log-derivative is an algebra-DEPENDENT state-pair functional on the BdG sub-algebra (Cell IV). They are not the same observable; they are not even on the same algebra axis.

My R1 L2 line 83 paragraph asserts the c-projection mechanism is what binds these together — but as I now converge above on Kill-shot #1, the c-projection mechanism is itself the FORBIDDEN cross-corner co-primary pattern in a different label. The §W5-4 Element-1 declaration is structurally ambiguous between the two observables, and that ambiguity is precisely the structural defect that the §"Audit at plan-freeze" Item 1 ("All 5 IS-not-IN anatomy elements present in entry text") flags as registry-INCOMPLETE.

**I converge**: §W5-4's §VII.AV pre-registration as currently written has a 5-anatomy Element-1 disambiguation defect. Either the substrate-IS observable IS the Pillar II Mellin-Barnes residue (in which case the empirical α=5.07 from §W5-3 is on a DIFFERENT observable and cannot bound `‖HKR(c_L) − c_continuum‖` for THIS bridge entry's c_L); or the substrate-IS observable IS the K-window log-derivative (in which case the bridge classification at line 898 as Pillar II ↔ Pillar V is wrong — the K-window log-derivative is a Pillar III/IV observable). Both options collapse §W5-4's K-counter advancement claim. The §VII.AV pre-registration cannot stand at S89 W6 close without disambiguation.

#### CONVERGE on Q4 — deferred-pending counter-proposal is structurally better than my L4 SUGGESTION sub-clause

Connes's Re:L4 counter-proposal introduces a `REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION` intermediate state in `cross-pillar-bridge-anatomy.md §"Enforcement clause"` (lines 57-65), located BETWEEN the existing IF Level-2-binding (PASS-ELIGIBLE) and IF Level-2-non-binding (INELIGIBLE) cases. After reading connes's Re:L4 BEFORE/AFTER patch verbatim and comparing it against my L4 BEFORE/AFTER patch, the deferred-pending state is structurally superior for four reasons that I cannot rebut:

1. **Preserves per-observable extraction discipline AT registry-PASS-eligibility timing**, not after-the-fact. My L4 sub-clause permits STAGE-1-CANDIDATE pre-registration at S89 W6 close WITHOUT per-observable extraction (because the SCHEMATIC proxy INFO suffices under condition (d)). The deferred-pending state withholds STAGE-1-CANDIDATE until CF-W5-3 lands the full physical re-derivation — restoring per-observable extraction as the gate for registry-PASS-eligibility.

2. **Preserves the MANDATORY-at-K=3 cross-corner co-primary prohibition.** My L4 sub-clause attempts to carve out a c-projection exception via the line 159 parenthetical — an exception that, as I converge above on Kill-shot #1, has no rule-text basis. The deferred-pending state requires the per-observable extraction to be performed at the inheriting observable's OWN corner cell; it does NOT permit cross-corner inheritance. This is structurally cleaner.

3. **Preserves the CF-W5-3 promotion path.** My initial concern at L3 lines 105-109 was that a strict registry-INELIGIBLE verdict at §W5-3 INFO would foreclose CF-W5-3 promotion in S90. The deferred-pending state achieves what I wanted (the CF-W5-3 path remains open) WITHOUT bypassing per-observable extraction. On CF-W5-3 PASS, §VII.AV promotes from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION to registry-PASS-eligible STAGE-1-CANDIDATE; on CF-W5-3 FAIL, it routes to registry-INELIGIBLE per the strict Level-2-non-binding enforcement. The promotion path is intact.

4. **Preserves the audit-trail of SCHEMATIC proxy disclosures.** The §W5-3 INFO verdict + `-CASIMIR-BOUND-PROXY` convention tag at line 592 + line 826 substrate-physics derivation remain as carry-forward provenance; the deferred-pending state preserves them as honest disclosure content. The deferred-pending state does not retroactively invalidate §W5-3's INFO closure; it correctly locates §W5-3 as a SCHEMATIC pre-cursor to the full physical extraction queued for S90.

**I converge**: connes's Re:L4 `REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION` deferred-pending state is the correct rule-extension direction. My L4 SUGGESTION sub-clause should be RETRACTED. I accept the rule-file diff direction of connes's Re:L4 BEFORE/AFTER patch at `cross-pillar-bridge-anatomy.md` lines 57-65 enforcement-clause clarification. The carry-forward L6.2 in my R1 (the lizzi inheritance sub-clause landing gate) is SUPERSEDED by connes's C5.2 (the deferred-pending enforcement-clause clarification landing gate). I retain a refinement proposal in EMERGENCE below — a sub-class distinction within the deferred-pending state for §VII.AV (PROXY-REFINEMENT) vs §VII.AU (FIRST-EXTRACTION) — but the structural direction is connes's, not mine.

### DISSENT — Where lizzi still disagrees (new evidence only)

Three structural positions where I maintain dissent, each grounded in rule-text or working-paper evidence not addressed in connes's Re:L1-Re:L5.

#### DISSENT #1 — §VII.AU is in a DIFFERENT pillar pair from §VII.AF.1.OP-PROJ; the cross-corner argument applies WITHIN a bridge family, not ACROSS pillar pairs

Connes's Re:L5 frames §VII.AU as in a structurally WEAKER position than §VII.AV ("zero empirical evidence on the FWD-C1 observable's L_max convergence vs §VII.AV's SCHEMATIC proxy evidence"). I dissent on the framing: §VII.AU lives in a STRUCTURALLY DIFFERENT bridge family from §VII.AF.1.OP-PROJ, so the cross-corner FORBIDDEN argument that destroys §VII.AV at L2 does NOT mechanically extend to §VII.AU at L5.

Per `cross-pillar-bridge-corpus.md §4` lines 120-128 verbatim (FWD-C1 spec):

> "**FWD-C1 — Pillar I ↔ Pillar II (substrate ↔ cosmology measurement)** ... **Substrate-IS observable** — n_s spectral-action prediction from finite-L D_K eigenmoments on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) — the n_s_FW value is a substrate-IS scalar moment of the Jensen-deformed band-0 sector at τ_fold. **Laboratory-IN observable** — Planck CMB scalar spectral index n_s = 0.9649 ± 0.0042 ... **Bridge map** — Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR `L_max → ∞` image of the substrate scalar spectral moment."

FWD-C1 is **Pillar I ↔ Pillar II**, NOT Pillar III ↔ Pillar IV. §VII.AF.1.OP-PROJ is **Pillar III ↔ Pillar IV**. These are DIFFERENT pillar pairs; the bridge families do not overlap. The cross-corner FORBIDDEN clause at `registry-landing.md` Detection item 4 forbids SOURCE-DOUBLE-CITE-CO-PRIMARY structures whose anchors scope distinct corner cells WITHIN a single non-fungible chain on a single bridge entry. §VII.AU's bridge entry does NOT take §VII.AF.1.OP-PROJ as an anchor (Mukhanov-Sasaki ∘ HKR is structurally a different bridge map composition from the W-5 HKR `L_max → ∞` image alone — the Mukhanov-Sasaki gauge-invariant mode-function transfer is the Pillar-I → Pillar-II cosmology pre-substrate composition factor). The two registry entries co-exist as Hybrid-Independence-Test-INDEPENDENT calibration instances per the HIT clause (i): distinct substrate-IS pillar (Pillar I vs Pillar III), distinct laboratory-IN pillar (Pillar II vs Pillar IV), distinct bridge map class (Mukhanov-Sasaki ∘ HKR vs HKR alone).

This means: even if §VII.AU's substrate-IS observable (parameterized slope_A canonical → c_sub_corrected → n_s_recomputed Mellin-cone closure) lives on a particular algebra-axis cell of §VII.U.2, it does NOT need to "inherit" a binding-class declaration from §VII.AF.1.OP-PROJ across cells — because §VII.AF.1.OP-PROJ is not in §VII.AU's bridge family in the first place. The cross-corner argument that destroys §VII.AV does not apply at the bridge-family level for §VII.AU.

What §VII.AU does inherit from W-5 is the `L^{-3}` envelope structural-exact form at d=4 — but as a **TEMPLATE pattern** (the structural prediction of HKR-image convergence rate at d=4 substrate-distance-1 pole structure), not as a cross-corner registry-anchor for §VII.AU's specific substrate-IS observable. This is structurally closer to the §VII.AG.1 SHARED-ANCHOR-COMPANION pattern — except §VII.AG.1's pattern was rejected from K-counter-advancement because its substrate-IS pillar, laboratory-IN pillar, and bridge map class ALL MATCHED §VII.AF.1.OP-PROJ (HIT all 4 clauses FAIL). §VII.AU's HIT is structurally OPPOSITE: distinct substrate-IS pillar (I vs III), distinct laboratory-IN pillar (II vs IV), distinct bridge map class (Mukhanov-Sasaki ∘ HKR vs HKR alone) — HIT clauses (i), (ii), (iii) ALL PASS for §VII.AU vs §VII.AF.1.OP-PROJ.

This is a partial dissent on Kill-shot #1: the cross-corner FORBIDDEN argument applies WITHIN a single non-fungible co-primary chain on a single bridge entry. §VII.AU does not have a non-fungible chain with §VII.AF.1.OP-PROJ — they live in different bridge families. The §VII.AV case is structurally distinct: §W5-4 explicitly invokes §VII.AF.1.OP-PROJ as the HKR-map-existence anchor for the K-window log-derivative observable (which lives on Cell IV, the algebra-DEPENDENT side), creating the cross-corner co-primary structure that the MANDATORY clause forbids.

#### DISSENT #2 — §W5-3 INFO is honest disclosure, not Level-2-non-binding falsifier (the SCHEMATIC convention tag IS the audit-trail content)

Connes's Re:L3 reading routes §W5-3's empirical envelope to the Level-2-non-binding counter-example pattern at `cross-pillar-bridge-anatomy.md` lines 48-51 ("a `L^{-α}` envelope on `Tr(D_K^{-2s})` ... that lacks an HKR image to a continuum lab observable"). I partially dissent on this routing.

The counter-example pattern at lines 48-51 names a `L^{-α}` envelope WITH NO HKR image to a continuum laboratory observable on the partner pillar. The §W5-3 case is not that — the K-window log-derivative observable HAS a continuum laboratory image at the bridge-family level (the Peotta-Törmä BZ-trace; established at §VII.AF.1.OP-PROJ for the HP¹ Hochschild pairing), even if the K-window log-derivative's OWN HKR image at the per-cocycle level is the open question CF-W5-3 will answer. The §W5-3 verdict-line convention tag `-CASIMIR-BOUND-PROXY` at line 592 IS the substrate-first-canonical-sourcing.md §(iv) MANDATORY-at-K=4 level-pin discipline operating correctly: the proxy class is honestly disclosed in the convention tag (W9c-1 POSITIVE-CALIBRATION pattern, S87); the substrate-physics derivation at §W5-3 line 826 honestly identifies why the proxy gives α≈5 not α=3.

This honesty-disclosure compliance matters at the §"Two-clause separation: registry-PASS (per-entry) vs K-counter advancement (rule-level corpus)" level (parent rule lines 279-295). The Two-clause separation states verbatim (line 289):

> "The two predicates are INDEPENDENT. A registry entry may be registry-INCOMPLETE under the first predicate (Level-3 deferred / not satisfied) and SIMULTANEOUSLY a valid calibration-LANDING under the second predicate."

The §W5-3 INFO closure is a valid PER-GATE verdict (honestly closes the gate at SCHEMATIC-proxy borderline). What it is NOT yet is a per-OBSERVABLE Level-2-binding extraction. These are two structurally different epistemic objects: the per-gate verdict at §W5-3 vs the per-observable Level-2-binding declaration that §VII.AV's registry-PASS-eligibility requires.

This is a refinement of connes's Re:L3, not a rebuttal: I AGREE that §VII.AV's registry-PASS-eligibility requires per-observable extraction, and I CONVERGE on the deferred-pending state holding §VII.AV pending CF-W5-3. What I dissent on is the framing that §W5-3 itself is Level-2-non-binding under the rule's operative definition. §W5-3 IS Level-2-binding-by-construction-anchor with SCHEMATIC-proxy α-extraction outside band — which is precisely connes's NEW intermediate case at Re:L4 line 501 verbatim: "Level-2-binding-by-construction-anchor (HKR map exists at the bridge-family level per a prior registry anchor) ∧ Level-2 envelope EXTRACTED-UNDER-SCHEMATIC-PROXY ∧ empirical α OUTSIDE predicted α band → registry-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION". The deferred-pending state IS the structural placement of §W5-3's INFO closure under the new enforcement-clause clarification.

The structural reading: §W5-3 is not in the strict Level-2-non-binding counter-example category (which describes bare Mellin truncations WITH NO HKR continuum image); it IS in the NEW deferred-pending intermediate category that connes's Re:L4 counter-proposal introduces. This subtle distinction matters for how the rule-file diff is written (the new case sits BETWEEN Level-2-binding and Level-2-non-binding, not WITHIN Level-2-non-binding).

#### DISSENT #3 — Rule-extension form refinement: the deferred-pending state needs sub-class distinction between PROXY-REFINEMENT (§VII.AV) and FIRST-EXTRACTION (§VII.AU)

I converge on connes's Re:L4 deferred-pending state as the correct rule-extension direction. I dissent on the BEFORE/AFTER patch text being structurally complete as written.

The deferred-pending state as connes wrote it at Re:L4 line 501 collapses two structurally distinct sub-cases into one verdict tag:

- **Sub-case A — §VII.AV**: SCHEMATIC proxy α=5.07 already extracted under known-too-aggressive Casimir-bound Δ-rescaling; CF-W5-3 (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`) is a REFINEMENT of the existing extraction (replace SCHEMATIC proxy with full BdG re-derivation). The audit trail HAS a SCHEMATIC envelope; the full extraction REFINES it.

- **Sub-case B — §VII.AU**: NO L_max scan has ever been performed on the FWD-C1 substrate-IS observable. §W5-6 evaluates c_sub_corrected at L_max=10 only (single point per §W5-6 line 1500 machinery pin); envelope_alpha_predicted=3 is asserted by template-inheritance (per §W5-6 line 1511). The S90 carry-forward for §VII.AU is a BRAND-NEW EXTRACTION (`S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL`), not a refinement of an existing extraction. The audit trail has TEMPLATE-asserted α; there is no SCHEMATIC envelope to refine.

These two cases differ structurally in three ways:

1. **Audit-trail content**: §VII.AV has SCHEMATIC proxy α=5.07 + R²=0.9244 + `-CASIMIR-BOUND-PROXY` convention tag as honest disclosure content (per §W5-3 line 592). §VII.AU has TEMPLATE-asserted α=3 with no scan-based audit content; the corresponding convention tag is not SCHEMATIC (it's TEMPLATE-INHERITED, per §W5-6 line 1513 `convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical`).

2. **Promotion path machinery**: CF-W5-3 (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`) replaces a SCHEMATIC proxy with a full BdG re-derivation on the SAME observable; the comparison `α_proxy / α_full_bdg` is meaningful. CF-W5-6-EXTENSION (the new S90 gate per connes's C5.3) is a first-ever L_max scan; there is no proxy-to-physical comparison.

3. **Pre-existing INFO closure**: §W5-3 is closed INFO at S89 W5; §W5-6 is closed INFO at S89 W5. The §W5-3 INFO is on a multi-L_max scan; the §W5-6 INFO is on a single-L_max evaluation against Planck σ. Different gate semantics; different audit trails.

I propose REFINING the deferred-pending state with two structurally distinct sub-class tags:

- `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` (for §VII.AV): the audit trail HAS a SCHEMATIC envelope under an honestly-disclosed proxy; the S90 carry-forward refines the SCHEMATIC envelope into a full physical envelope. Promotes on CF-W5-3 PASS.
- `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (for §VII.AU): the audit trail has TEMPLATE-asserted α only; no L_max scan has been performed at the per-observable level; the S90 carry-forward is the first-ever extraction. Promotes on CF-W5-6-EXTENSION PASS.

This sub-class refinement preserves the structural direction of connes's deferred-pending counter-proposal (both sub-tags are within the new intermediate category between Level-2-binding and Level-2-non-binding), but separates two structurally distinct kinds of "pending" that connes's Re:L4 patch collapses. The refinement matters because the audit-script extension at `_cross_pillar_bridge_audit.py` (proposed in connes's C5.2) regex-detects different patterns for the two sub-cases: PROXY-REFINEMENT fires on SCHEMATIC-proxy + α-outside-band; FIRST-EXTRACTION fires on TEMPLATE-INHERITED + no L_max scan in the producing script's machinery pin. The downstream knowledge-MCP indexing benefits from the sub-class distinction: future readers can route from a deferred-pending entry to the SPECIFIC S90 gate that promotes it.

### EMERGENCE — New insights from cross-pollination

The cross-pollination of my R1 L1-L6 + connes's Re:L1-Re:L5 + C1-C5 generates three structural insights not present in either R1 position alone.

#### EMERGENCE #1 — The SCHEMATIC convention tag at §W5-3 line 592 IS the audit-trail mechanism that operationally distinguishes Level-2-non-binding (lines 48-51 strict) from Level-2-binding-by-construction-anchor (connes's new intermediate case)

When I re-read connes's Re:L4 counter-proposed enforcement-clause clarification against the existing rule-text on the substrate-first-canonical-sourcing.md §(iv) MANDATORY-at-K=4 SCHEMATIC-vs-physical level-pin discipline (promoted at S88 W7b-83 close, 2026-05-05), a structural reading emerges that neither R1 position made explicit:

The new intermediate state connes proposes at Re:L4 line 501 — "Level-2-binding-by-construction-anchor ∧ Level-2 envelope EXTRACTED-UNDER-SCHEMATIC-PROXY ∧ empirical α OUTSIDE predicted α band" — is structurally NEW because the substrate-first-canonical-sourcing.md §(iv) level-pin discipline IS the new structural layer that distinguishes it from Level-2-non-binding.

Before the W7b-83 K=4 MANDATORY promotion of the SCHEMATIC level-pin discipline (which post-dates the S88 W8-88 Level-2 Layer Distinction hardening that the parent rule lines 36-65 codified), the parent rule's Level-2-binding / Level-2-non-binding dichotomy implicitly assumed that empirical α extractions were either FULL-physical-regularization (admissible) or BARE-DECOMPOSITION (Level-2-non-binding counter-example pattern). The W7b-83 promotion introduced a THIRD class — SCHEMATIC proxy extractions with HONEST convention-tag disclosure — that does not fit cleanly into the existing dichotomy. SCHEMATIC proxies HAVE an HKR continuum image (so they're not in the Level-2-non-binding bare-decomposition category); but they DON'T deliver per-observable full-physical envelope extraction (so they're not registry-PASS-eligible at the Level-2-binding admissibility test either).

The deferred-pending state connes proposes IS the rule-text placement for this third class. The structural reading: the deferred-pending state is the parent rule catching up with the level-pin discipline at the registry-anchor-timing layer. The W9c-1 POSITIVE-CALIBRATION pattern (S87) established that SCHEMATIC convention tags are admissible at the verdict-line layer; connes's Re:L4 deferred-pending state extends that admissibility to the registry-anchor layer with the corresponding intermediate verdict.

This means the SCHEMATIC convention tag at §W5-3 line 592 IS the audit-trail mechanism that operationally distinguishes Level-2-non-binding (Level-2-non-binding counter-example pattern at lines 48-51, which has NO HKR continuum image) from Level-2-binding-by-construction-anchor (which HAS an HKR continuum image at the bridge-family level but lacks per-observable full-physical extraction). The convention-tag honesty discipline IS the rule's downstream audit signal for which sub-class an empirical envelope belongs to. The audit-script extension at `_cross_pillar_bridge_audit.py` (per connes's C5.2) can mechanically distinguish the two cases by regex-detecting the `-SCHEMATIC` / `-PROXY` suffix on the verdict-line convention tag + comparing the empirical α against the predicted-α band.

This insight reconciles connes's per-observable-extraction reading with §W5-3's §(f) substrate-physics derivation at line 826: both are correct. The substrate-physics derivation correctly identifies the proxy as SCHEMATIC and queues CF-W5-3 for refinement (substrate-first-canonical-sourcing.md §(iv) honesty disclosure operating correctly); connes's per-observable-extraction reading correctly withholds registry-PASS-eligibility until CF-W5-3 lands the full-physical extraction. The deferred-pending state is the structural placeholder for honestly-disclosed SCHEMATIC envelopes pending full-physical refinement.

#### EMERGENCE #2 — Two structurally distinct sub-classes of the deferred-pending state (PROXY-REFINEMENT vs FIRST-EXTRACTION) match the W9c-1 vs W4-2 NEGATIVE-CALIBRATION pattern from S88 W7b-83

Building on EMERGENCE #1: §VII.AV and §VII.AU each map to a structurally distinct sub-class of the deferred-pending state, matching the W9c-1 POSITIVE-CALIBRATION vs W4-2 NEGATIVE-CALIBRATION pattern that S88 W7b-83 established for the substrate-first-canonical-sourcing.md §(iv) level-pin discipline.

- **§VII.AV ≈ W9c-1 pattern**: convention tag carries explicit `-CASIMIR-BOUND-PROXY` suffix at the verdict line; substrate-physics derivation at §W5-3 line 826 honestly discloses the SCHEMATIC class; the proxy is queued for refinement at CF-W5-3. This is the W9c-1 POSITIVE-CALIBRATION pattern operating correctly — TIER-2 SCHEMATIC declaration in honest disclosure form. Sub-class: PROXY-REFINEMENT.

- **§VII.AU ≈ W4-2-style pattern (pre-W7b-83 NEGATIVE-CALIBRATION)**: convention tag at §W5-6 line 1513 reads `lizzi-fwd-c1-retry-parameterized-slope-A-canonical` — NO `-SCHEMATIC` or `-TEMPLATE-INHERITED` suffix. The template-asserted α=3 at §W5-6 line 1511 is not flagged as SCHEMATIC or TEMPLATE-only at the verdict-line layer; it's asserted as if it were the substrate's own per-observable prediction. This is structurally analogous to the W4-2 (S86) post-hoc disclosure pattern that the S88 W7b-83 audit retroactively classed as NEGATIVE-CALIBRATION on rule (2) of the level-pin discipline (the level disclosure was in the working-paper post-hoc, not in the verdict-line convention tag). Sub-class: FIRST-EXTRACTION (with corollary that the verdict-line convention tag at §W5-6 should be retrofitted with a `-TEMPLATE-INHERITED` suffix per the substrate-first-canonical-sourcing.md §(iv) discipline).

This means: §VII.AU is in a structurally weaker position than §VII.AV NOT because §VII.AU lacks empirical evidence (which is connes's Re:L5 framing) but because §VII.AU's convention-tag honesty disclosure is structurally INCOMPLETE compared to §W5-3's. The retrofit clause from substrate-first-canonical-sourcing.md §(iv) — that pre-W7b-83 instances are GRANDFATHERED with mandatory disclosure retrofit at next-session plan-freeze — applies here: §W5-6's TEMPLATE-INHERITED convention tag should carry a structurally-equivalent disclosure suffix (e.g., `-TEMPLATE-INHERITED-FROM-W-5` or `-L-MINUS-3-AT-D-EQUAL-4-TEMPLATE`).

This is a sharpening of connes's Re:L5 reading. §VII.AU's weakness is at the SCHEMATIC-vs-TEMPLATE-vs-FULL-PHYSICAL level-pin disclosure layer, not at the empirical evidence layer per se. The S90 carry-forward for §VII.AU (`S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL` per connes's C5.3) is structurally distinct from CF-W5-3: it's a first-ever extraction, not a refinement. Both gates promote their respective §VII slots from deferred-pending to registry-PASS-eligible STAGE-1-CANDIDATE on PASS; the sub-class refinement (PROXY-REFINEMENT vs FIRST-EXTRACTION) lets the audit-script extension and the knowledge-MCP indexing distinguish them.

#### EMERGENCE #3 — The §VII.AG.1 SHARED-ANCHOR-COMPANION precedent does NOT extend to §VII.AU (the bridge-family-level argument I made at L2 for §VII.AV fails there, but for a structurally different reason than it fails at §VII.AV)

I argued at L2 that the §VII.AG.1 SHARED-ANCHOR-COMPANION precedent supports inheritance for §VII.AV. Connes correctly demolished this at Re:L2 (i): §VII.AG.1 is OUTSIDE the K-counter precisely because HIT all 4 clauses FAIL; §VII.AV seeks K-counter advancement explicitly, so the inheritance modes are mutually exclusive.

A new insight emerges from cross-pollination on §VII.AU: the §VII.AG.1 precedent ALSO does not extend to §VII.AU, but for a structurally different reason. §VII.AG.1 retained registry-entry status PRECISELY BECAUSE its substrate-IS pillar, laboratory-IN pillar, and bridge map class ALL MATCHED §VII.AF.1.OP-PROJ — that's what made it a SHARED-ANCHOR-COMPANION (not K-counter-advancing). §VII.AU's HIT is structurally the OPPOSITE: distinct substrate-IS pillar (I vs III), distinct laboratory-IN pillar (II vs IV), distinct bridge map class (Mukhanov-Sasaki ∘ HKR vs HKR alone). §VII.AU passes HIT clauses (i), (ii), (iii); it CANNOT inherit as a SHARED-ANCHOR-COMPANION because it's not a structural companion to §VII.AF.1.OP-PROJ at all.

What §VII.AU IS, structurally, is an INDEPENDENT K-counter-advancing candidate (HIT (i ∨ ii ∨ iii) ∧ iv = TRUE per the corpus §3 definition). The template-inheritance of the L^{-3} envelope at d=4 is a PARAMETER-CLASS template (structural prediction of HKR-image convergence rate for substrate-distance-1 poles at d=4), not a registry-anchor inheritance. Template-inheritance of structural-exact form at a parameter class IS admissible under the parent rule — but it does NOT substitute for per-observable Level-2-binding extraction at the §VII.AU substrate-IS observable. The deferred-pending state correctly captures this: §VII.AU has a TEMPLATE-asserted α=3 that needs first-ever empirical extraction at the per-observable level.

This emergent insight reconciles connes's Re:L5 (§VII.AU needs per-observable extraction; both §VII.AV and §VII.AU route to deferred-pending) with my Dissent #1 (§VII.AU's HIT is structurally distinct from §VII.AV's; the cross-corner argument doesn't apply at the bridge-family level for §VII.AU). The synthesis: §VII.AU routes to deferred-pending NOT because of the cross-corner cross-pillar-pair argument that destroys §VII.AV, but because the substrate-first-canonical-sourcing.md §(iv) level-pin discipline requires per-observable extraction for any TEMPLATE-INHERITED structural prediction to advance the K-counter. The two paths to deferred-pending are structurally distinct (cross-corner FORBIDDEN for §VII.AV; per-observable extraction MANDATORY for §VII.AU), but they converge on the same intermediate verdict tag at the registry-anchor layer.

### QUESTIONS — Sharper follow-ups; answer C4 from R1

#### Answer to Q1 (rule-text exception for cross-corner inheritance via "c-projection")

**No such exception is documented in the rule text.** I searched `cross-pillar-bridge-anatomy.md`, `cross-pillar-bridge-corpus.md`, `registry-landing.md`, `epistemic-discipline.md`, and `substrate-first-canonical-sourcing.md` for documented exceptions to the cross-corner co-primary FORBIDDEN clause; for "c-projection" carve-outs; for "binding-class inheritance" provisions; and for any mechanism that would route Level-2-binding inheritance across the algebra-INVARIANT / algebra-DEPENDENT cell boundary. None exists.

The MANDATORY-at-K=3 algebra-axis orthogonality clause is the highest-status rule in this rule family (the N=3 corpus saturated at S87 W-2 R3 close, 2026-04-30; promotion was structural, not narrative). My L4 line 159 parenthetical attempting to legislate a c-projection exception via a SUGGESTION-status K=1 sub-clause IS structurally a SUGGESTION attempting to abrogate a MANDATORY rule — which is itself a violation of the K-counter advancement protocol (K=1 SUGGESTION cannot override K=3 MANDATORY per `feedback_rules-compensate-missing-structure.md` K-counter threshold + the parent rule's hardness ladder).

**I concede Q1.** Under the current rule-text, the c-projection mechanism I proposed at L2 cannot inherit Level-2-binding from Cell I to Cell IV at the per-observable level for §VII.AV. The cross-corner co-primary FORBIDDEN clause rules against it. The L4 sub-clause should be RETRACTED (per my CONVERGE on Q4 above).

#### Answer to Q2 (rule-text basis for two-track distinction between "Level-2-binding CLASS inheritance" and "HIT K-counter advancement")

**No such distinction is documented in the rule text.** The only documented two-clause separation in `cross-pillar-bridge-anatomy.md` is at lines 279-295 §"Two-clause separation: registry-PASS (per-entry) vs K-counter advancement (rule-level corpus)". I read it verbatim:

> "**Per-entry registry-PASS** (§'Registry-PASS criterion' above): gates whether a single registry entry's STAGE-tag may be promoted to STAGE-3-PERMANENT under the `joint-theorem-promotion.md` 4-stage pathway. Predicate: Level-3 < Level-2 at canonical L_max. Operates on the entry's own empirical satisfaction.
>
> **Rule-level corpus K-counter advancement** ... Predicate: 3 distinct calibration-LANDING events satisfying the Hybrid Independence Test (i ∨ ii ∨ iii) ∧ iv. Operates on the rule's own corpus saturation."

This is a separation between (a) per-entry empirical adequacy and (b) corpus saturation toward MANDATORY promotion. It is NOT a separation between "binding-class inheritance" and "HIT K-counter advancement"; it is a separation between TWO PREDICATES (per-entry vs corpus) on disjoint epistemic objects (the entry vs the rule). My L2 line 85 invocation of a "Level-2-binding CLASS inheritance vs HIT K-counter advancement" two-track distinction is NOT what the parent rule documents.

**I concede Q2.** The two-track distinction I asserted at L2 is manufactured and lacks rule-text basis. Connes is correct that the only documented two-clause separation is at parent rule lines 279-295, which is about epistemic-adequacy vs corpus-saturation predicates on disjoint objects, NOT about cross-observable binding-class inheritance.

This is the structurally embarrassing concession. My L2 was an attempt to make §VII.AV's K-counter advancement compatible with the §VII.AG.1 SHARED-ANCHOR-COMPANION precedent by inventing a structural distinction that doesn't exist in the rule text. The §VII.AG.1 precedent is OUTSIDE the K-counter; §VII.AV claims to be INSIDE the K-counter. These are mutually exclusive at the structural level, and I cannot reconcile them with a manufactured two-track distinction.

#### Answer to Q3 (PICK-ONE — Mellin-Barnes residue vs K-window log-derivative)

**Neither fork survives intact.** I work through both legs of the dilemma honestly.

**Fork A — substrate-IS = Pillar II Mellin-Barnes residue (line 898 reading)**: Then §W5-4 has performed NO per-observable empirical Level-2 envelope extraction on the Pillar II Mellin-Barnes residue. The §W5-3 α=5.07 is at the K-window log-derivative observable (a Pillar III/IV BdG sub-algebra observable on Cell IV), NOT at the Pillar II Mellin-Barnes residue. Importing §W5-3's α to §W5-4's §VII.AV is the cross-corner pattern (Cell II algebra-INVARIANT Mellin-Barnes residue ↔ Cell IV algebra-DEPENDENT K-window log-derivative) that the MANDATORY-at-K=3 cross-corner co-primary FORBIDDEN clause rules out.

**Fork B — substrate-IS = K-window log-derivative (line 1011 reading)**: Then §W5-4's bridge classification at line 898 (Pillar II ↔ Pillar V) is structurally mis-specified. The K-window log-derivative is a Pillar III/IV observable; its bridge would be Pillar III/IV ↔ Pillar V (closer to FWD-C3 substrate cocycle ↔ 3He-B/3He-A laboratory observable per `cross-pillar-bridge-corpus.md §4` lines 142-148). The §W5-4 HIT substitution chain at lines 968-986 then fails clause (i): the substrate-IS pillar (Pillar III/IV) MATCHES §VII.AF.1.OP-PROJ's substrate-IS pillar (Pillar III), so clause (i) "distinct substrate-IS pillar" FAILS, and §VII.AV cannot advance the HIT K-counter at the Pillar II ↔ Pillar V candidate slot.

**Pick**: Fork B is the structurally honest reading. The K-window log-derivative IS the empirically-extracted observable at §W5-3; it lives on Cell IV; it's a Pillar III/IV observable. §W5-4's Element-1 declaration at line 1011 correctly names this. The line 898 machinery PIN MAP claim that FWD_C2_substrate_pillar = Pillar II is the structural error — it's the prior FWD-C2 spec from `cross-pillar-bridge-corpus.md §4` lines 132-138 (Mellin-Barnes residue ↔ BdG spectral triple), but §W5-3 / §W5-4 did not actually execute on that spec. §W5-3 / §W5-4 executed on the K-window log-derivative observable (the §W5-2 / §W5-3 inherited substrate-IS observable from A.25/A.26). The bridge entry should be re-classified as Pillar III/IV ↔ Pillar V (NEW candidate slot, possibly FWD-C2.bdg or a re-spec of FWD-C2 from the original Mellin-Barnes residue to the K-window log-derivative).

**Implication for §VII.AV registration**: §W5-4's §VII.AV pre-registration as a "Pillar II ↔ Pillar V" K-counter-advancing entry CANNOT STAND at S89 W6 close. Either (a) §VII.AV is re-classified as a "Pillar III/IV ↔ Pillar V" entry, in which case it inherits §VII.AF.1.OP-PROJ's substrate-IS pillar (Pillar III) and HIT clause (i) FAILS — collapsing K-counter advancement; or (b) §VII.AV is re-spec'd to actually execute on the Pillar II Mellin-Barnes residue per the original FWD-C2 spec, in which case §W5-3 / §W5-4 have not yet performed the per-observable extraction at all and the entry routes to REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (the FIRST-EXTRACTION sub-class from my EMERGENCE #2 above).

The cleanest structural reading: §W5-4's substrate-IS observable IS the K-window log-derivative (per line 1011); §W5-4's bridge classification is MIS-SPECIFIED as Pillar II ↔ Pillar V (per line 898); the §VII.AV registration should be RE-DEFERRED to a properly-classified bridge entry. Under connes's deferred-pending state, §VII.AV enters REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION with the explicit caveat that the bridge classification itself needs disambiguation (Element-1 anatomy element) in addition to the Level-2 envelope refinement. The S90 carry-forward CF-W5-3 (full BdG re-derivation per L6.1 / C5.1) is necessary but not sufficient; a bridge-classification disambiguation step is also required.

**I converge on connes's Kill-shot #3 framing** with this sharpening: §W5-4's §VII.AV is registry-INCOMPLETE on TWO axes simultaneously — (i) Element-1 anatomy ambiguity at lines 898 vs 1011 (Pillar II vs Pillar III/IV); (ii) per-observable Level-2-binding extraction under SCHEMATIC proxy. Both need to land cleanly in S90 before §VII.AV can promote to registry-PASS-eligible STAGE-1-CANDIDATE.

#### Answer to Q4 (deferred-pending counter-proposal accepted)

**Yes, I accept connes's Re:L4 counter-proposed deferred-pending state as the better resolution than my L4 SUGGESTION sub-clause.** I converge on this above in CONVERGENCE on Q4 with four structural reasons. The refinement I propose is the sub-class distinction between PROXY-REFINEMENT (§VII.AV) and FIRST-EXTRACTION (§VII.AU) per my DISSENT #3 + EMERGENCE #2 above.

The structural advantage my L4 sub-clause does NOT provide that the deferred-pending state DOES: the deferred-pending state preserves the MANDATORY-at-K=3 cross-corner co-primary prohibition. My L4 sub-clause violates that prohibition (via the c-projection carve-out at line 159 parenthetical). On this axis, connes's counter-proposal is strictly stronger; there is no structural advantage my sub-clause provides that the deferred-pending state lacks.

What my refinement adds to connes's Re:L4 patch:

1. **Sub-class distinction in the verdict tag**: `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` vs `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` rather than a single `REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION` tag.
2. **Convention-tag honesty discipline retrofit**: §W5-6's TEMPLATE-INHERITED convention tag at line 1513 should carry a `-TEMPLATE-INHERITED-FROM-W-5` suffix per the W4-2-style retrofit clause in `substrate-first-canonical-sourcing.md §(iv)`. This is structurally analogous to the W4-2 (S86) post-hoc disclosure pattern that S88 W7b-83 retroactively classed as NEGATIVE-CALIBRATION; §W5-6 should be retrofitted at S90 plan-freeze.
3. **Audit-script extension regex refinement**: `_cross_pillar_bridge_audit.py` (per connes's C5.2) regex-detects `convention=.*-(?:SCHEMATIC|PROXY)` for the PROXY-REFINEMENT sub-class; additionally regex-detects `convention=.*-TEMPLATE-INHERITED` (after retrofit) and no-L_max-scan in the producing-script machinery pin for the FIRST-EXTRACTION sub-class.

This refinement does NOT alter connes's structural direction; it sharpens the audit-trail of the deferred-pending state to distinguish two structurally distinct kinds of "pending" that the C5.2 patch text collapses.

#### Answer to Bonus (§VII.AU parallel)

**Both routings apply, but on structurally distinct grounds (see EMERGENCE #3 above).**

Connes's framing at Re:L5 + Bonus argues §VII.AU routes to REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION because zero empirical evidence has been performed on the FWD-C1 substrate-IS observable's L_max convergence. I AGREE that §VII.AU needs per-observable extraction (CF-W5-6-EXTENSION ≡ `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL` per connes's C5.3 is necessary before §VII.AU promotes to registry-PASS-eligible STAGE-1-CANDIDATE).

I dissent partially on the framing: §VII.AU's path to deferred-pending is NOT the cross-corner FORBIDDEN argument (which destroys §VII.AV); §VII.AU's path is the substrate-first-canonical-sourcing.md §(iv) MANDATORY-at-K=4 level-pin discipline operating on the TEMPLATE-INHERITED structural prediction. §VII.AU lives in a structurally DIFFERENT bridge family from §VII.AF.1.OP-PROJ (FWD-C1 Pillar I ↔ Pillar II vs §VII.AF.1.OP-PROJ Pillar III ↔ Pillar IV); the cross-corner argument that destroys §VII.AV does not extend at the bridge-family level. The two FWD candidates route to deferred-pending via different mechanisms, but converge on the same intermediate verdict tag at the registry-anchor layer.

**I converge on connes's C5.3 carry-forward** with the FIRST-EXTRACTION sub-class refinement: §VII.AU at REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; CF-W5-6-EXTENSION queued for S90; convention-tag retrofit at §W5-6 line 1513 to add `-TEMPLATE-INHERITED-FROM-W-5` suffix per the substrate-first-canonical-sourcing.md §(iv) discipline.

The asymmetric structural reading from EMERGENCE #3 — that §VII.AU enters deferred-pending via a different mechanism than §VII.AV — does not affect the routing outcome; both route to deferred-pending. It does affect the per-entry audit-trail content: §VII.AV's deferred-pending tag should record the bridge-classification disambiguation pending + the Level-2 envelope refinement pending; §VII.AU's deferred-pending tag should record the convention-tag retrofit pending + the per-observable first-extraction pending. The audit-script extension at `_cross_pillar_bridge_audit.py` distinguishes these.

### Round-2 lizzi carry-forward (4-field spec)

Per `feedback_fix-in-session-never-defer.md`, carry-forwards have 4 fields: What / Inputs / Gate / Estimated effort.

Per the R2 convergence on connes's C5.2 deferred-pending state direction, my R1 L6.2 carry-forward (lizzi inheritance sub-clause landing) is SUPERSEDED by connes's C5.2 carry-forward (enforcement-clause clarification landing). The L6.1 carry-forward (CF-W5-3 full BdG re-derivation) is RETAINED as the substrate-physics workload for §VII.AV's promotion path, structurally subsumed under connes's C5.1 with promotion semantics. I propose two REFINED carry-forwards.

#### Carry-Forward #R2.1 — Deferred-pending sub-class refinement in the C5.2 BEFORE/AFTER patch

- **What**: Refine connes's C5.2 BEFORE/AFTER patch to introduce two structurally distinct sub-class tags for the deferred-pending state: `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` (audit trail HAS SCHEMATIC envelope under honestly-disclosed proxy; the S90 carry-forward refines the SCHEMATIC envelope into full physical) and `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (audit trail has TEMPLATE-asserted α only; no per-observable L_max scan performed; the S90 carry-forward is first-ever extraction). The sub-class distinction is encoded at the verdict-tag layer + the audit-script regex-detection layer + the knowledge-MCP indexing layer. Refine the §"Enforcement clause" BEFORE/AFTER patch text at `cross-pillar-bridge-anatomy.md` lines 57-65 to read the new intermediate case as a disjunction over the two sub-classes:
  ```
  - IF Level-2-binding-by-construction-anchor (HKR map exists at bridge-family
    level per a prior registry anchor) ∧ Level-2 envelope EXTRACTED-UNDER-
    SCHEMATIC-PROXY ∧ empirical α OUTSIDE predicted α band
    → REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT
    (calibration: §W5-3 + §W5-4 Casimir-bound proxy at K-window log-derivative)
  - IF Level-2-binding-by-construction-anchor (structural-exact template
    inherited from prior calibration) ∧ NO per-observable L_max scan performed
    ∧ convention tag lacks SCHEMATIC/TEMPLATE-INHERITED suffix
    → REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (with retrofit clause)
    (calibration: §W5-6 template-inheritance at FWD-C1 parameterized slope_A)
  ```

- **Inputs**:
  - `.claude/rules/cross-pillar-bridge-anatomy.md` (parent rule file; §"Enforcement clause" lines 57-65 target).
  - `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` (MANDATORY-at-K=4 SCHEMATIC-vs-physical level-pin discipline; the audit-trail mechanism reference).
  - `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (Level-2 Layer Distinction calibration corpus extension target; lands as Calibration #3 with TWO sub-class entries).
  - `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` (this workshop's R3 verdict text as the substitution-chain provenance).
  - `computations/_shared/_cross_pillar_bridge_audit.py` (audit script to extend with two-sub-class regex detection per the W9c-1 vs W4-2 NEGATIVE-CALIBRATION pattern).
  - `.claude/rules/methodology-wave-allowlist.md` (append gate-ID with computed sha256_of_plan_block per the append-only orchestrator-only-edit discipline).

- **Gate**: `S90-LEVEL-2-NON-BINDING-ENFORCEMENT-CLARIFICATION-DEFERRED-PENDING-SUB-CLASS-REFINEMENT`. METHODOLOGY-class per `wave-classification.md §M4`. Pre-registered PASS criterion (per `wave-classification.md §M1`): (i) the refined diff is applied verbatim at parent rule lines 57-65 with both sub-class tags; (ii) audit-script regex extension distinguishes PROXY-REFINEMENT (`convention=.*-(?:SCHEMATIC|PROXY)` + α-outside-band) from FIRST-EXTRACTION (`convention=.*-TEMPLATE-INHERITED` after retrofit + no-L_max-scan in producing-script machinery pin); (iii) corpus row landed at `cross-pillar-bridge-corpus.md §1` Calibration #3 with TWO worked examples — §W5-3 + §W5-4 PROXY-REFINEMENT (§VII.AV) and §W5-6 FIRST-EXTRACTION (§VII.AU); (iv) gate-ID appended to `methodology-wave-allowlist.md` with computed `sha256_of_plan_block`; (v) SUGGESTION at K=1 with §VII.AV + §VII.AU as the two K=1 calibration instances; promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md`. Dual-SHA closure per `gate-verdicts.md` S87+ schema-v2.

- **Estimated effort**: 0.5 agent-session (connes-ncg-theorist PRIMARY for the structural direction per Re:L4 BEFORE/AFTER patch; lizzi-spectral-functional-theorist CO-AUTHOR for the sub-class refinement + audit-script regex extension; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` for the corpus row landing at `cross-pillar-bridge-corpus.md §1` Calibration #3; orchestrator-direct-write convention path per `wave-classification.md §"Dispatch consequences"`). Honest-disclosure rule-file edit per the W9c-1 positive-calibration model.

- **Depends on**: R3 convergence on the sub-class refinement direction. If R3 retains connes's single-tag deferred-pending state without the sub-class distinction, this carry-forward DOWNGRADES to a knowledge-MCP-indexing annotation only (tag the §VII.AV / §VII.AU deferred-pending entries at the registry-row layer rather than at the rule-file layer).

#### Carry-Forward #R2.2 — Convention-tag honesty retrofit at §W5-6 line 1513 (TEMPLATE-INHERITED suffix)

- **What**: Retrofit the verdict-line convention tag at `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6` line 1513 from `convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical` to `convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical-TEMPLATE-INHERITED-FROM-W-5` (or structurally-equivalent disclosure form), per the W4-2 retrofit clause in `substrate-first-canonical-sourcing.md §(iv)` ("pre-W7b-83 instances are GRANDFATHERED with mandatory disclosure retrofit at next-session plan-freeze"). The retrofit is honesty-discipline only; it does NOT change §W5-6's INFO verdict or the σ=2.10 Planck distance value. It DOES route §VII.AU's deferred-pending entry from REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION (generic) to REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (sub-class-refined per R2.1) by triggering the FIRST-EXTRACTION audit-script regex match. The retrofit ALSO updates the §W5-6 working-paper §(f) substrate-physics interpretation block to explicitly disclose the template-inheritance class per the W9c-1 POSITIVE-CALIBRATION pattern.

- **Inputs**:
  - `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6` (working-paper section to retrofit; lines 1505-1640 approximately).
  - `computations/session-89/s89_w5_a30_fwd_c1_retry_parameterized_slope_A_canonical.py` (producing script; verdict-line emission target for retrofit).
  - `computations/session-89/s89_gate_verdicts.txt` (verdict file; retrofit emits a SUPERSEDES-tagged corrective canonical line per `v3-closure-recovery.md` Option A sig_5 remediation pathway, retaining the original convention tag entry as audit-trail content).
  - `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` (MANDATORY-at-K=4 retrofit clause for pre-W7b-83 instances).
  - `.claude/rules/regulator-convention-lockdown.md` (cross-link for retrofit convention-tag discipline).
  - canonical_constants.py: existing pins unchanged (n_s_FW_exact, slope_A_FW_Conv_A_GEOMETRIC, tau_fold, c_sub_baseline, planck_ns).

- **Gate**: `S90-FWD-C1-CONVENTION-TAG-RETROFIT-TEMPLATE-INHERITED`. Hybrid-class (METHODOLOGY-leaning per `wave-classification.md §M4` since the retrofit is a structural disclosure update, not a new computation). Pre-registered PASS criterion: (i) retrofitted convention tag carries the `-TEMPLATE-INHERITED-FROM-W-5` suffix at the verdict-line layer; (ii) §W5-6 working-paper §(f) substrate-physics interpretation block disclosed the template-inheritance class explicitly; (iii) the §VII.AU deferred-pending tag at the registry layer updates from generic FULL-PHYSICAL-RE-DERIVATION to FIRST-EXTRACTION sub-class per R2.1; (iv) corrective canonical line emitted per `v3-closure-recovery.md` Option A sig_5 protocol with SUPERSEDES tag pointing to the original §W5-6 line 592-style verdict-line audit_sha256. Dual-SHA closure per `gate-verdicts.md` S87+ schema-v2.

- **Estimated effort**: 0.25 agent-session (lizzi-spectral-functional-theorist PRIMARY for the W9c-1-style honesty-disclosure retrofit; connes-ncg-theorist CO-AUTHOR cross-check on the deferred-pending sub-class routing; orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"`). Wall-time: minutes-scale; this is a structural disclosure update, not a numerical re-computation.

- **Depends on**: R2.1 landed at S90 W0 (the sub-class distinction must exist as a valid registry verdict before §VII.AU can be routed to the FIRST-EXTRACTION sub-class); §VII.AU initial deferred-pending registration via mack-cosmic-bridge sole-writer at S90 W0 (parallel to §VII.AV deferred-pending registration per connes's C5.2 + C5.3).

#### Note on retraction of L6.2

The R1 L6.2 carry-forward (lizzi inheritance sub-clause landing as `§"Level-2-binding inheritance from registry anchor"` SUGGESTION at `cross-pillar-bridge-anatomy.md` between lines 46-48) is RETRACTED per the R2 CONVERGENCE on Q4. The structural direction of the rule extension is connes's Re:L4 enforcement-clause clarification (BETWEEN existing Level-2-binding and Level-2-non-binding cases at lines 57-65), NOT a new admissibility sub-clause that opens the inheritance pathway my L4 proposed. L6.1 (CF-W5-3 full BdG re-derivation) is RETAINED as the substrate-physics workload — structurally subsumed under connes's C5.1 with promotion semantics per the deferred-pending state.

---

## Round 2 — connes: Cross-Synthesis (FINAL — fills Verdict + Wrap-Up)

### CONVERGENCE — Where connes accepts lizzi's corrections

Lizzi's R2-A contains three structural corrections to my R1-B Re:L1-Re:L5 framing that I accept explicitly. The workshop has converged on a CONVERGED-WITH-REFINEMENT outcome: my structural direction (deferred-pending state added to `cross-pillar-bridge-anatomy.md §"Enforcement clause"` lines 57-65 between the existing IF Level-2-binding (PASS-ELIGIBLE) and IF Level-2-non-binding (INELIGIBLE) cases) lands with lizzi's R2.1 sub-class refinement (PROXY-REFINEMENT vs FIRST-EXTRACTION). I take her three corrections in order.

#### CONVERGE on DISSENT #1 — §VII.AU bridge-family distinction (Pillar I ↔ Pillar II ≠ Pillar III ↔ Pillar IV)

Lizzi is structurally correct that my Re:L5 framing of §VII.AU as routed to deferred-pending via the SAME mechanism as §VII.AV is wrong. The cross-corner co-primary FORBIDDEN clause at `registry-landing.md` Detection item 4 + `cross-pillar-bridge-corpus.md §6` lines 222-225 operates WITHIN a single non-fungible co-primary chain on a single bridge entry — anchors of a SOURCE-DOUBLE-CITE-CO-PRIMARY structure that scope distinct corner cells fail Detection item 4. The structural object the prohibition operates on is a CHAIN, not a generic registry-anchor citation.

§VII.AV's chain at §W5-4 explicitly takes §VII.AF.1.OP-PROJ as ANCHOR-1 (registry-anchor for HKR-map-existence on the Pillar III ↔ Pillar IV bridge family) AND the K-window log-derivative on Cell IV as ANCHOR-2 (per-observable instantiation under the c-projection mechanism I demolished at Re:L2 (ii)). That's the chain; ANCHOR-1 lives on Cell I (algebra-INVARIANT spectrum-only Connes-Karoubi pairing per `cross-pillar-bridge-anatomy.md` line 18); ANCHOR-2 lives on Cell IV (algebra-DEPENDENT state-pair functional per §W5-3 line 609). The cells are orthogonal in identity-class membership per `cross-pillar-bridge-corpus.md §6` line 200; cross-corner co-primary chain is structurally FORBIDDEN.

§VII.AU at §W5-6 is in a structurally DIFFERENT position. Per `cross-pillar-bridge-corpus.md §4` lines 120-128, FWD-C1 is **Pillar I ↔ Pillar II** (substrate ↔ cosmology measurement), with bridge map class `Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR L_max → ∞`. §VII.AF.1.OP-PROJ is **Pillar III ↔ Pillar IV** (substrate ↔ Peotta-Törmä BZ-trace), with bridge map class `HKR L_max → ∞` alone. The pillar pairs do NOT overlap; the bridge map classes are non-fungibly distinct (Mukhanov-Sasaki ∘ HKR carries a Pillar-II cosmology pre-substrate composition factor absent from the pure HKR class). §VII.AU's bridge entry does NOT import §VII.AF.1.OP-PROJ as a co-primary anchor; the `L^{-3}` envelope at d=4 enters §W5-6 (line 1511) as a **SHARED-CALIBRATION-TEMPLATE pattern** — structural-exact prediction of HKR-image convergence rate at d=4 substrate-distance-1 pole structure that holds across bridge families inheriting from the W-5 calibration `L^{-α}` at d=4 algebraic envelope. Template-inheritance at a parameter class is admissible under the parent rule per the structural prediction status at `cross-pillar-bridge-anatomy.md` line 22 ("L_max-dependent; algebraically derived; refines with L-scan").

What §VII.AU lacks at S89 W6 close is a per-observable empirical extraction of the structural-exact L^{-3} template at the FWD-C1 substrate-IS observable (parameterized slope_A canonical → c_sub_corrected → n_s_recomputed Mellin-cone closure). The routing mechanism to deferred-pending is therefore the `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 level-pin discipline on TEMPLATE-INHERITED structural predictions — analogous to but structurally distinct from the cross-corner FORBIDDEN argument that destroys §VII.AV. CONVERGE on this distinction. The TWO FWD candidates converge on the same intermediate verdict tag at the registry-anchor layer (REGISTRY-INCOMPLETE-PENDING) via DIFFERENT structural mechanisms; lizzi's R2-A DISSENT #1 framing is canonical.

#### CONVERGE on DISSENT #2 — §W5-3 INFO is honest-disclosure, NOT strict Level-2-non-binding

Lizzi is structurally correct that my Re:L3 framing of §W5-3's empirical envelope as "Level-2-non-binding under the operative definition" is too strong as written. The strict Level-2-non-binding counter-example pattern at `cross-pillar-bridge-anatomy.md` lines 48-51 names a `L^{-α}` envelope on `Tr(D_K^{-2s})` (bare Mellin truncation) WITH NO HKR image to a continuum laboratory observable on the partner pillar — `c_continuum` reference quantity UNDEFINED for that envelope class.

§W5-3 is NOT that. The K-window log-derivative observable HAS a continuum laboratory image at the bridge-family level: the Peotta-Törmä BZ-trace `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` is established at §VII.AF.1.OP-PROJ as the Pillar-IV continuum partner for the Pillar III ↔ Pillar IV bridge family. The `c_continuum` reference quantity is DEFINED for the bridge family even if the K-window log-derivative's OWN HKR image at the per-cocycle level is the open empirical question CF-W5-3 will answer. The convention tag `-CASIMIR-BOUND-PROXY` at §W5-3 line 592 IS the `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 level-pin discipline operating correctly (W9c-1 POSITIVE-CALIBRATION pattern from S87): SCHEMATIC class declared in convention tag + substrate-physics derivation in working-paper §(f) at §W5-3 line 826 + carry-forward CF-W5-3 queued for full physical refinement.

What §W5-3 IS, structurally, is the NEW intermediate category my Re:L4 counter-proposal introduces: **Level-2-binding-by-construction-anchor** (HKR map exists at the bridge-family level per a prior registry anchor §VII.AF.1.OP-PROJ) ∧ **Level-2 envelope EXTRACTED-UNDER-SCHEMATIC-PROXY** (Casimir-bound Δ_eff(L_max) rescaling honestly disclosed in convention tag) ∧ **empirical α OUTSIDE predicted α band** (α=5.07 vs predicted α=3 under the proxy's quasi-LINEAR convergence shape). This is structurally BETWEEN Level-2-binding and Level-2-non-binding, not WITHIN Level-2-non-binding. The distinction matters for the rule-file diff: the new case sits between the two existing cases at lines 57-65 of the enforcement clause, exactly as my Re:L4 BEFORE/AFTER patch proposed.

CONVERGE on this sharpening of my Re:L3 framing. §W5-3 INFO is the honest per-gate verdict that the SCHEMATIC proxy cannot deliver registry-PASS-eligibility at S89 W6 close; it is NOT a strict Level-2-non-binding finding (that classification is reserved for envelopes with NO HKR continuum image at any level). The deferred-pending state IS the structural placement for honestly-disclosed SCHEMATIC envelopes pending full-physical refinement — this is lizzi's EMERGENCE #1 insight (the substrate-first-canonical-sourcing.md §(iv) level-pin discipline IS the audit-trail mechanism that operationally distinguishes the new intermediate state from strict Level-2-non-binding), which I accept structurally.

#### CONVERGE on DISSENT #3 — Sub-class refinement (PROXY-REFINEMENT vs FIRST-EXTRACTION)

Lizzi is structurally correct that my Re:L4 BEFORE/AFTER patch collapses two structurally distinct sub-cases into a single `REGISTRY-INCOMPLETE-PENDING-FULL-PHYSICAL-RE-DERIVATION` tag. The audit-trail content differs in three distinct ways between §VII.AV and §VII.AU:

(1) **Audit-trail content**: §VII.AV has SCHEMATIC proxy α=5.07 + R²=0.9244 + `-CASIMIR-BOUND-PROXY` convention tag as honest disclosure content at §W5-3 line 592; §VII.AU has TEMPLATE-asserted α=3 at §W5-6 line 1511 with NO per-observable scan content (single L_max=10 evaluation only per §W5-6 line 1500 machinery pin).

(2) **Promotion path machinery**: CF-W5-3 (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX`) REFINES the SCHEMATIC proxy into a full physical envelope on the SAME observable; the bias factor `α_proxy / α_full_bdg = 5.0679 / α_extracted` is a meaningful retrospective audit-trail quantity. CF-W5-6-EXTENSION (`S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL`) is a FIRST-EVER extraction; there is no proxy-to-physical comparison because no proxy was ever extracted.

(3) **Pre-existing convention tag**: §W5-3's verdict line carries `-CASIMIR-BOUND-PROXY` honesty disclosure already; §W5-6's verdict line at line 1513 reads `convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical` with NO `-TEMPLATE-INHERITED` suffix — structurally analogous to the W4-2 (S86) post-hoc disclosure pattern that S88 W7b-83 retroactively classed as NEGATIVE-CALIBRATION on rule (2) of the substrate-first-canonical-sourcing.md §(iv) level-pin discipline.

The two sub-class tags lizzi proposes (R2.1 BEFORE/AFTER patch) — `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` (for §VII.AV) vs `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (for §VII.AU) — encode this audit-trail distinction at the verdict-tag layer + the audit-script regex-detection layer + the knowledge-MCP indexing layer. The audit-script regex extension at `computations/_shared/_cross_pillar_bridge_audit.py` (proposed in my C5.2) can mechanically distinguish the two: PROXY-REFINEMENT fires on `convention=.*-(?:SCHEMATIC|PROXY)` + α-outside-band match; FIRST-EXTRACTION fires on `convention=.*-TEMPLATE-INHERITED` (after retrofit) + no-L_max-scan in producing-script machinery pin match.

CONVERGE on lizzi's R2.1 sub-class refinement to my Re:L4 BEFORE/AFTER patch. The consolidated rule-file diff that lands at S90 W0 is the disjunction over the two sub-classes at the new intermediate case in the enforcement clause:

```
- IF Level-2-binding-by-construction-anchor (HKR map exists at bridge-family
  level per a prior registry anchor) ∧ Level-2 envelope EXTRACTED-UNDER-
  SCHEMATIC-PROXY ∧ empirical α OUTSIDE predicted α band
  → REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT
  (calibration: §W5-3 + §W5-4 Casimir-bound proxy at K-window log-derivative)

- IF Level-2-binding-by-construction-anchor (structural-exact template inherited
  from prior calibration at parameter class — bridge family need not match)
  ∧ NO per-observable L_max scan performed
  ∧ convention tag lacks SCHEMATIC/TEMPLATE-INHERITED suffix
  → REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (with retrofit clause)
  (calibration: §W5-6 template-inheritance at FWD-C1 parameterized slope_A)
```

This is the canonical R3-stable rule-file diff. SUGGESTION at K=1 (two sub-class calibration instances from S89 W6: §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION); promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter threshold.

### DISSENT — Sharpen, don't repeat

The major structural disagreements have been resolved at CONVERGENCE. Two residual sharpenings remain — both are refinements of lizzi's R2-A framing, not new structural positions.

#### Sharpening 1 — §VII.AU is NOT a SHARED-ANCHOR-COMPANION pattern (in the §VII.AG.1 sense)

Lizzi's EMERGENCE #3 at lines 1196-1204 carefully argues that §VII.AU is "structurally adjacent to but NOT identical to §VII.AG.1's SHARED-ANCHOR-COMPANION pattern" — §VII.AG.1 failed HIT all 4 clauses (substrate III=III, lab IV=IV, bridge HKR=HKR refinement; clauses (i),(ii),(iii) FAIL; OUTSIDE the K-counter), while §VII.AU passes HIT clauses (i), (ii), (iii) (Pillar I ≠ Pillar III; Pillar II ≠ Pillar IV; Mukhanov-Sasaki ∘ HKR ≠ pure HKR). I accept this distinction. Sharpening: the structural reading is that §VII.AU is a **Hybrid-Independence-Test-PASS bridge candidate** (advances HIT K-counter on landing as an independent calibration instance per `cross-pillar-bridge-corpus.md §3` lines 96-102) WITH a missing per-observable extraction (routes to FIRST-EXTRACTION deferred-pending). The two structural properties are independent:

- HIT-PASS status is a property of the BRIDGE CANDIDATE — declared at bridge-spec time, independent of per-observable empirical evidence.
- FIRST-EXTRACTION deferred-pending is a property of the REGISTRY-ENTRY STATE — held pending per-observable Level-2 envelope extraction at the inheriting observable.

The two properties co-exist for §VII.AU at S89 W6 close. Lizzi's EMERGENCE #3 framing is correct as far as it goes; I sharpen by stating explicitly that the HIT K-counter advancement potential (K=1 → K=2 with §VII.AV landing; K=2 → K=3 with §VII.AU landing) is PRESERVED in the deferred-pending state. What is suspended is the registry-PASS-eligibility STAGE-1-CANDIDATE promotion, NOT the K-counter advancement claim. The S90 carry-forwards CF-W5-3 (PROXY-REFINEMENT) and CF-W5-6-EXTENSION (FIRST-EXTRACTION) are simultaneously per-observable extraction gates AND HIT calibration-LANDING gates — on dual PASS, both K-counters advance simultaneously (registry-PASS-eligibility lifts via the deferred-pending → STAGE-1-CANDIDATE promotion semantics in my C5.1/C5.3 carry-forwards; HIT K-counter advances per `cross-pillar-bridge-corpus.md §3` Step 4 corpus increment).

This sharpening matters for the §VII.AU registry-anchor citation discipline: the deferred-pending registration at §VII.AU should NOT inherit a `SHARED-ANCHOR-COMPANION` tag from §VII.AG.1's precedent (which lives OUTSIDE the K-counter). Instead, §VII.AU's deferred-pending registration tag carries the FIRST-EXTRACTION sub-class + an explicit `HIT-PASS-CANDIDATE-PENDING-EXTRACTION` qualifier in the registry text, signaling to downstream consumers that the entry is a structurally-independent K-counter-advancement candidate held pending per-observable empirical extraction in S90.

#### Sharpening 2 — TEMPLATE-INHERITED retrofit at §W5-6 is MANDATORY, not SUGGESTION

Lizzi's R2.2 carry-forward proposes the convention-tag retrofit at §W5-6 line 1513 (adding `-TEMPLATE-INHERITED-FROM-W-5` suffix) per the W4-2-style retrofit clause in `substrate-first-canonical-sourcing.md §(iv)` ("pre-W7b-83 instances are GRANDFATHERED with mandatory disclosure retrofit at next-session plan-freeze"). She frames the retrofit as a refinement to the deferred-pending machinery.

Sharpening: the retrofit is structurally MANDATORY at S90 plan-freeze, not optional. The §(iv) rule text at `substrate-first-canonical-sourcing.md` is MANDATORY-at-K=4 since S88 W7b-83 close (2026-05-05) — pre-S88 instances are GRANDFATHERED with the explicit constraint that "mandatory disclosure retrofit at next-session plan-freeze" applies. §W5-6 was authored at S89 (post-W7b-83 promotion to MANDATORY); it is NOT a pre-S88 grandfathered instance. The retrofit clause at §(iv) calibration corpus instance #1 (W4-2 at S86) applies retroactively to ANY S88+ producing script consuming a TEMPLATE-INHERITED structural prediction without explicit convention-tag disclosure — §W5-6 falls in this scope.

Concretely: the §W5-6 producing script `computations/session-89/s89_w5_a30_fwd_c1_retry_parameterized_slope_A_canonical.py` emits a verdict line at §W5-6 line 1513 with `convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical` and machinery pin at line 1511 `envelope_alpha_predicted=3` template-asserted. The convention tag lacks the `-TEMPLATE-INHERITED` suffix that the substrate-first-canonical-sourcing.md §(iv) MANDATORY-at-K=4 rule requires for template-inheritance disclosures (analogous to the `-SCHEMATIC` suffix W9c-1 carries for SCHEMATIC-helper consumption). The retrofit is therefore a MANDATORY compliance action, not a SUGGESTION — without the retrofit, §W5-6 is in the W4-2 NEGATIVE-CALIBRATION pattern at the substrate-first-canonical-sourcing.md §(iv) level-pin discipline layer. Lizzi's R2.2 carry-forward correctly identifies the retrofit; I sharpen the status from "carry-forward refinement" to "mandatory compliance action".

The structural consequence: S90 plan-freeze MUST land R2.2 (convention-tag retrofit) before R2.1 (sub-class refinement to the deferred-pending state) — the FIRST-EXTRACTION sub-class verdict tag requires the producing script's convention tag to be retrofitted to `-TEMPLATE-INHERITED` form so the audit-script regex (`convention=.*-TEMPLATE-INHERITED`) fires correctly. Without the retrofit, §VII.AU's deferred-pending entry would route incorrectly (to PROXY-REFINEMENT via false-negative match on the non-template convention tag, or to generic deferred-pending without sub-class distinction). The two carry-forwards are sequentially dependent; R2.2 lands at S90 W0 before R2.1.

### EMERGENCE — New cross-domain insights

The workshop's cross-pollination produces three structural insights that neither R1 position alone claimed.

#### EMERGENCE #1 — Deferred-pending state IS a structural innovation at the rule level (third verdict-class between Level-2-binding-eligible and Level-2-non-binding-ineligible)

The S88 W8-88 Level-2 Layer Distinction hardening codified a sharp binary at `cross-pillar-bridge-anatomy.md §"Enforcement clause"` lines 57-65: Level-2-binding (registry-PASS ELIGIBLE) vs Level-2-non-binding (registry-INELIGIBLE). The dichotomy implicitly assumed empirical α extractions were either full-physical-regularization (admissible) or BARE-DECOMPOSITION with NO HKR continuum image (counter-example pattern at lines 48-51). It did NOT anticipate the THIRD class lizzi's EMERGENCE #1 (R2-A lines 1170-1182) identifies: SCHEMATIC-proxy or TEMPLATE-INHERITED structural predictions with honest convention-tag disclosure per the post-W7b-83 (2026-05-05) MANDATORY-at-K=4 level-pin discipline at `substrate-first-canonical-sourcing.md §(iv)`.

The deferred-pending state IS the structural placement for this third class at the registry-anchor-timing layer. It is a NEW rule-file innovation, not just a calibration-corpus instance: the rule-file diff itself adds a new branch to the enforcement-clause direction table, sitting BETWEEN the existing two cases. The deferred-pending state's structural function:

- Preserve the per-observable extraction discipline (Level-2-binding admissibility test remains operational on `‖HKR(c_L) − c_continuum‖` for the SPECIFIC observable);
- Preserve the registry-PASS-eligibility timing discipline (no STAGE-1-CANDIDATE pre-registration without per-observable extraction);
- Preserve the audit-trail of honest convention-tag disclosures (SCHEMATIC / TEMPLATE-INHERITED suffix discipline operating per W7b-83 MANDATORY-at-K=4);
- Preserve the MANDATORY-at-K=3 cross-corner co-primary prohibition (the deferred-pending state does NOT permit cross-corner inheritance — per-observable extraction is performed at the inheriting observable's OWN corner cell, not via cross-corner inheritance);
- Preserve the CF-W5-3 / CF-W5-6-EXTENSION promotion paths (the deferred-pending state IS the structural route to registry-PASS-eligible STAGE-1-CANDIDATE, NOT a foreclosure).

Lizzi's R2.1 sub-class refinement (PROXY-REFINEMENT vs FIRST-EXTRACTION) is the structural calibration of the deferred-pending state's audit-trail granularity. The two sub-classes are the substrate-first calibration of where the audit-trail content differs structurally — PROXY-REFINEMENT preserves SCHEMATIC-envelope provenance and refines it via full-physical re-derivation on the same observable; FIRST-EXTRACTION preserves TEMPLATE-asserted-α provenance and performs first-ever empirical extraction at the per-observable level. Both sub-classes promote to registry-PASS-eligible STAGE-1-CANDIDATE on S90 carry-forward PASS, advancing the HIT K-counter simultaneously.

The rule-file innovation has K=1 calibration corpus at S89 W6 close (the §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION dual landing); it promotes to MANDATORY at K=3 distinct calibration instances. Plausible K=2 and K=3 instances are forecasted in lizzi's EMERGENCE #2 mapping to the W9c-1 vs W4-2 NEGATIVE-CALIBRATION pattern from S88 W7b-83 — future bridge candidates at the Pillar III ↔ Pillar IV layer (FWD-C2 / FWD-C3 derivatives in S91+) or the Pillar I ↔ Pillar II layer (FWD-C1 derivatives) admitting honestly-disclosed SCHEMATIC envelopes or TEMPLATE-INHERITED structural predictions will route to one of the two sub-classes by audit-script regex, accumulating the calibration corpus toward MANDATORY.

#### EMERGENCE #2 — HIT K-counter advancement potential PRESERVED for both §VII.AV and §VII.AU in deferred-pending state

The cross-pillar-bridge K-counter at `cross-pillar-bridge-anatomy.md §"Status: MANDATORY at K=3"` lines 275-277 reached MANDATORY at K=3 at S88 W4a-17 close (corpus: W-5 LANDED §VII.AF.1 / W11-5 REGISTRY-FAIL / W4a-17 LANDED §VII.W-3.LAB). The Hybrid Independence Test K-counter at `cross-pillar-bridge-corpus.md §3` lines 79-110 is at K=1 baseline (W-5 calibration only) and SUGGESTION status pending K=3 promotion.

§VII.AV (FWD-C2 — Pillar II ↔ Pillar V) and §VII.AU (FWD-C1 — Pillar I ↔ Pillar II) both PASS the Hybrid Independence Test all 4 clauses against §VII.AF.1.OP-PROJ AND against each other:

- §VII.AV vs §VII.AF.1.OP-PROJ: substrate-IS pillar (Pillar III/IV per Q3 Fork B resolution ≠ Pillar III, distinct); laboratory-IN pillar (Pillar V ≠ Pillar IV); bridge map class (Connes-Karoubi pairing ≠ pure HKR); algebraic envelope independent (per-observable extraction yields envelope distinct from W-5's HKR-image envelope).
- §VII.AU vs §VII.AF.1.OP-PROJ: substrate-IS pillar (Pillar I ≠ Pillar III); laboratory-IN pillar (Pillar II ≠ Pillar IV); bridge map class (Mukhanov-Sasaki ∘ HKR ≠ pure HKR); algebraic envelope inherited at parameter class (d=4 substrate-distance-1) but per-observable bound distinct.
- §VII.AV vs §VII.AU: substrate-IS pillar (Pillar III/IV ≠ Pillar I); laboratory-IN pillar (Pillar V ≠ Pillar II); bridge map class (Connes-Karoubi ≠ Mukhanov-Sasaki ∘ HKR); envelopes per-observable distinct.

The structural-independence is PRESERVED in the deferred-pending state. What deferred-pending suspends is the STAGE-1-CANDIDATE promotion (registry-PASS-eligibility), NOT the structural-independence claim that drives K-counter advancement. On CF-W5-3 PASS + CF-W5-6-EXTENSION PASS in S90, both candidates promote to STAGE-1-CANDIDATE simultaneously, and the HIT K-counter advances K=1 → K=3 in a single dispatch (one of the three K=3 promotion conditions per `feedback_rules-compensate-missing-structure.md`). The cross-pillar-bridge K-counter (already MANDATORY) gains two more structurally-independent calibration instances, hardening the MANDATORY status against future challenges.

This EMERGENCE matters because the structural innovation at EMERGENCE #1 might otherwise be read as a K-counter-blocking mechanism (deferred-pending entries don't count toward MANDATORY promotion). It is not: deferred-pending entries are PRE-CURSORS to calibration-LANDING events; on dual PASS in S90, the calibration-LANDING fires simultaneously with the STAGE-1-CANDIDATE promotion. The deferred-pending state is a structural BUFFER (preserving per-observable extraction discipline at registry-PASS-eligibility timing), not a structural BLOCKER (K-counter advancement is not foreclosed).

#### EMERGENCE #3 — Element-1 anatomy-element disambiguation IS a registry-INCOMPLETE flag distinct from Level-2-binding admissibility

My Re:L2 Kill-shot #3 surfaced the §W5-4 Element-1 ambiguity (line 898 "Pillar II Mellin-Barnes residue" vs line 1011 "K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L})"); lizzi's Q3 answer at R2-A converged on Fork B (K-window log-derivative IS the actual substrate-IS observable; line 898's Pillar II ↔ Pillar V bridge classification is mis-specified). This convergence surfaces a structural insight neither R1 position made explicit: **Element-1 anatomy-element ambiguity is a registry-INCOMPLETE flag at a DIFFERENT axis from Level-2-binding admissibility**.

The §"Audit at plan-freeze" sub-section at `cross-pillar-bridge-anatomy.md` lines 233-242 already lists Item 1 ("All 5 IS-not-IN anatomy elements present in entry text") as a separate audit clause; the structural defect at §W5-4 (Element 1 names two structurally distinct observables across different pillar pairs in different corner cells) fails Item 1 INDEPENDENTLY of the Level-2-binding admissibility test. Two structurally distinct registry-INCOMPLETE pathways operate on §VII.AV at S89 W6 close:

- **Pathway A (Level-2-binding admissibility)**: per-observable Level-2 envelope extraction is missing; §W5-3 SCHEMATIC proxy does not deliver registry-PASS-eligibility. Deferred-pending sub-class: PROXY-REFINEMENT (per the EMERGENCE #1 rule-file innovation).
- **Pathway B (Element-1 anatomy disambiguation)**: §W5-4 names two structurally distinct observables in Element-1; the Element-1 declaration is ambiguous, failing the §"Audit at plan-freeze" Item 1. The bridge classification at line 898 (Pillar II ↔ Pillar V) is mis-specified per Q3 Fork B; the actual substrate-IS observable IS the K-window log-derivative (Pillar III/IV per §W5-3 line 609 explicit corner-cell declaration).

The two pathways must be CO-RESOLVED at S90 before §VII.AV promotes to STAGE-1-CANDIDATE. Resolving Pathway A alone (CF-W5-3 PASS) without resolving Pathway B (Element-1 disambiguation) leaves §VII.AV's bridge classification inconsistent with its substrate-IS observable — a structural defect that would propagate downstream as a SHA-traceable registry-text ambiguity. Resolving Pathway B alone (Element-1 disambiguated to the K-window log-derivative + bridge re-classified to Pillar III/IV ↔ Pillar V) without Pathway A (full BdG re-derivation) leaves the per-observable Level-2 envelope extraction missing.

This necessitates a NEW S90 carry-forward `S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION` that lands BEFORE CF-W5-3 in the S90 wave-plan ordering. The disambiguation step re-specifies the bridge classification: §VII.AV is re-classified from "Pillar II ↔ Pillar V" (current §W5-4 line 898) to "Pillar III/IV ↔ Pillar V" (per Q3 Fork B Element-1 disambiguation), aligning the bridge classification with the K-window log-derivative substrate-IS observable. The implication is that §VII.AV may need to be re-anchored as a structurally distinct FWD candidate (closer to FWD-C3 substrate cocycle ↔ 3He-B/3He-A laboratory observable per `cross-pillar-bridge-corpus.md §4` lines 142-148), or as a re-spec of FWD-C2 with the substrate-IS observable updated from Mellin-Barnes residue to K-window log-derivative.

The structural reading: the §"Audit at plan-freeze" Item 1 (5-anatomy completeness) and the Level-2-binding admissibility test operate on disjoint epistemic objects (the entry's anatomy declaration vs the entry's empirical Level-2 envelope). Both must be satisfied for registry-PASS-eligibility; satisfying only one is registry-INCOMPLETE on the other axis. EMERGENCE #3 makes this orthogonality explicit at the rule-file audit-clause layer.

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Adj-(a) Level-2-binding admissibility under §W5-3 INFO | L1, Re:L1, C1, C2, R2-A CONVERGE on Q4 + DISSENT #2, R2 CONVERGENCE on DISSENT #2 | **Partial** | Level-2-binding-by-construction-anchor is admissible at the bridge-family registry-anchor level (HKR map exists for the Pillar III ↔ Pillar IV family per §VII.AF.1.OP-PROJ); per-observable empirical Level-2 envelope extraction at the K-window log-derivative cocycle class is REQUIRED for registry-PASS-eligibility. SCHEMATIC proxy α=5.07 under Casimir-bound Δ_eff(L_max) = Δ_static · (L_max+1)/13 rescaling routes §W5-3 to the NEW intermediate `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` deferred-pending sub-class. The §W5-3 INFO per-gate verdict STANDS as honest disclosure content. |
| 2 | Adj-(b) Registry-anchor inheritance from §VII.AF.1.OP-PROJ | L2, Re:L2, C3, R2-A CONVERGENCE on Kill-shot #1, R2 CONVERGENCE on DISSENT #1 | **Converged** | INADMISSIBLE at the per-observable Level-2-binding extraction level due to cross-corner co-primary FORBIDDEN clause at `registry-landing.md` Detection item 4 (MANDATORY-at-K=3 per S88 W-15 V.6): §VII.AF.1.OP-PROJ HP¹ Hochschild pairing lives on Cell I (algebra-INVARIANT spectrum-only Connes-Karoubi pairing); §W5-3 K-window log-derivative lives on Cell IV (algebra-DEPENDENT state-pair functional). The two cells are STRUCTURALLY ORTHOGONAL in identity-class membership per `cross-pillar-bridge-corpus.md §6` line 200; the c-projection mechanism is the FORBIDDEN cross-corner co-primary pattern renamed. HKR-map-existence is inheritable at the bridge-family level ONLY (Claim A); HKR-image binding RATE is per-cocycle and NOT inheritable across cells (Claim B retracted by lizzi). |
| 3 | Adj-(c) §"Level-2-non-binding" enforcement on α = 5.07 / R² = 0.92 | L3, Re:L3, C2, R2-A DISSENT #2, R2 CONVERGENCE on DISSENT #2 | **Converged-with-refinement** | §W5-3 is NOT in the strict Level-2-non-binding counter-example category at rule lines 48-51 (which names `L^{-α}` envelopes on `Tr(D_K^{-2s})` WITH NO HKR image to a continuum laboratory observable on the partner pillar; `c_continuum` reference quantity UNDEFINED). §W5-3 IS in the NEW intermediate `Level-2-binding-by-construction-anchor ∧ Level-2 envelope EXTRACTED-UNDER-SCHEMATIC-PROXY ∧ empirical α OUTSIDE predicted α band` category that the deferred-pending state introduces. The Peotta-Törmä BZ-trace `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` is the DEFINED Pillar-IV continuum partner at the bridge-family level even though the per-cocycle HKR image of `[L]` to that BZ-trace is the open empirical question CF-W5-3 will answer. |
| 4 | Adj-(d) Rule-extension form / §VII.AV downgrade form | L4, Re:L4, R2-A CONVERGE on Q4 + DISSENT #3, R2 CONVERGENCE on DISSENT #3 | **Converged** | Deferred-pending intermediate state added to `cross-pillar-bridge-anatomy.md §"Enforcement clause"` lines 57-65, sitting BETWEEN existing IF Level-2-binding (PASS-ELIGIBLE) and IF Level-2-non-binding (INELIGIBLE) cases. The state is decomposed into TWO sub-class tags per lizzi's R2.1 refinement: `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` (audit trail HAS SCHEMATIC envelope under honestly-disclosed proxy; S90 carry-forward refines into full physical) and `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (audit trail has TEMPLATE-asserted α only; no per-observable scan; S90 carry-forward is first-ever extraction). SUGGESTION status at K=1 with §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION as the K=1 dual calibration; MANDATORY at K=3 distinct instances. Lizzi's L4 SUGGESTION sub-clause RETRACTED (c-projection inheritance pathway was a SUGGESTION-status K=1 attempt to abrogate a MANDATORY-at-K=3 cross-corner FORBIDDEN clause). |
| 5 | Cross-cutting §W5-6 + §VII.AU FWD-C1 parallel | L5, Re:L5, R2-A DISSENT #1 + EMERGENCE #3, R2 CONVERGENCE on DISSENT #1 + Sharpening 1 | **Partial** | §VII.AU routes to deferred-pending via a STRUCTURALLY DIFFERENT mechanism from §VII.AV. Cross-corner FORBIDDEN argument operates WITHIN a single non-fungible co-primary chain on a single bridge entry — §VII.AU does NOT have a non-fungible chain with §VII.AF.1.OP-PROJ (Pillar I ↔ Pillar II ≠ Pillar III ↔ Pillar IV; Mukhanov-Sasaki ∘ HKR ≠ pure HKR). §VII.AU's path to deferred-pending is the `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 level-pin discipline on TEMPLATE-INHERITED structural predictions (FIRST-EXTRACTION sub-class). Convention-tag retrofit at §W5-6 line 1513 to add `-TEMPLATE-INHERITED-FROM-W-5` suffix is MANDATORY (not SUGGESTION) per the post-W7b-83 retrofit clause. §VII.AU HIT-PASS status (clauses (i),(ii),(iii) PASS) is INDEPENDENT of FIRST-EXTRACTION deferred-pending state — registry-PASS-eligibility suspended, K-counter-advancement potential preserved. |
| 6 | Deliverable (i) — §W5-3 + §W5-4 status verdict | All sections | **Converged** | Per-gate verdicts STAND at S89 W5 close: §W5-3 INFO (composite=INFO at α=5.07 SCHEMATIC proxy-fidelity borderline + R²=0.9244 MARGINAL); §W5-4 PASS (corner-iv-singleton disambiguation gate); §W5-6 INFO (Planck σ=2.10 BY DESIGN). The §W5-3 SCHEMATIC convention tag `-CASIMIR-BOUND-PROXY` at line 592 satisfies `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 level-pin discipline (W9c-1 POSITIVE-CALIBRATION pattern); the substrate-physics derivation at §W5-3 line 826 is preserved as audit-trail content. §VII.AV pre-registration DOWNGRADES from STAGE-1-CANDIDATE to `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` pending CF-W5-3 full BdG re-derivation + S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION Element-1 fix (per EMERGENCE #3). |
| 7 | Deliverable (ii) — FWD-C2 §VII.AV STAGE-1-CANDIDATE status | All sections, especially Re:L2 Kill-shots #1+#3, R2-A Q3 Fork B + CONVERGE on Kill-shot #3 | **Converged** | DOWNGRADED from STAGE-1-CANDIDATE pre-registration to `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`. Promotion to registry-PASS-eligible STAGE-1-CANDIDATE requires TWO co-dependent S90 carry-forwards: (i) CF-W5-3 full BdG re-derivation per L_max ∈ {6..12} with promotion semantics (`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS`) extracting refined α ∈ [2.5, 3.5] + R² ≥ 0.95; (ii) Element-1 anatomy disambiguation per Q3 Fork B (`S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION`) re-specifying bridge classification from "Pillar II ↔ Pillar V" (line 898) to "Pillar III/IV ↔ Pillar V" (line 1011 K-window log-derivative IS the actual substrate-IS observable per R2-A Q3 Fork B). |
| 8 | Deliverable (iii) — FWD-C1 §VII.AU STAGE-1-CANDIDATE status | L5, Re:L5, R2-A DISSENT #1 + EMERGENCE #2/#3, R2 CONVERGENCE on DISSENT #1 + Sharpening 2 | **Converged** | DOWNGRADED from STAGE-1-CANDIDATE pre-registration to `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`. Promotion to registry-PASS-eligible STAGE-1-CANDIDATE requires TWO sequentially-dependent S90 carry-forwards: (i) convention-tag retrofit at §W5-6 line 1513 to add `-TEMPLATE-INHERITED-FROM-W-5` suffix (`S90-FWD-C1-CONVENTION-TAG-RETROFIT-TEMPLATE-INHERITED`) — MANDATORY per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 retrofit clause for post-W7b-83 producing scripts; (ii) first-ever L_max scan on the FWD-C1 substrate-IS observable (`S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS`) extracting α ∈ [2.5, 3.5] + R² ≥ 0.95 from per-L_max c_sub_corrected / n_s_recomputed Mellin-cone closure. |
| 9 | Deliverable (iv) — Rule-file diff (advisory / MANDATORY) | L4, Re:L4, R2-A R2.1 + R2 CONVERGENCE on DISSENT #3 + EMERGENCE #1 | **Converged** | The consolidated rule-file diff at `cross-pillar-bridge-anatomy.md §"Enforcement clause"` lines 57-65 is the structural deliverable: enforcement-clause clarification adding the deferred-pending intermediate state decomposed into TWO sub-class tags (PROXY-REFINEMENT, FIRST-EXTRACTION). SUGGESTION status at K=1 with §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION as the dual K=1 calibration instances (S89 W6 close, 2026-05-12). Promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter threshold. Audit-script extension at `_cross_pillar_bridge_audit.py` regex-detects two distinct patterns: `convention=.*-(?:SCHEMATIC|PROXY)` + α-outside-band for PROXY-REFINEMENT; `convention=.*-TEMPLATE-INHERITED` (after R2.2 retrofit) + no-L_max-scan in producing-script machinery pin for FIRST-EXTRACTION. METHODOLOGY-class per `wave-classification.md §M4`; orchestrator-only-edit per the recursion-attack closure. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

---

## Remaining Open Questions

1. **K=3 promotion calibration for the deferred-pending sub-clause**: when do the second and third K-counter calibration instances arrive for PROXY-REFINEMENT vs FIRST-EXTRACTION sub-classes? PROXY-REFINEMENT pattern requires future bridge candidates admitting honestly-disclosed SCHEMATIC envelopes with empirical α outside predicted band; FIRST-EXTRACTION pattern requires future bridge candidates inheriting TEMPLATE-INHERITED structural predictions without per-observable extraction. Plausible K=2/K=3 sources: FWD-C3 (Pillar IV ↔ Pillar V; substrate cocycle ↔ 3He-B/3He-A laboratory observables per `cross-pillar-bridge-corpus.md §4` lines 142-148) derivatives in S91+ wave; cross-pole sub-rules at the FWD-C2.bdg re-classification of §VII.AV (if Q3 Fork B's "Pillar III/IV ↔ Pillar V" bridge family lands as a STRUCTURALLY-NEW candidate slot distinct from the original FWD-C2 Pillar II ↔ Pillar V spec). The promotion timeline directly affects when the deferred-pending audit-script enforcement at `_cross_pillar_bridge_audit.py` hardens from SUGGESTION (case-by-case verifier judgment) to MANDATORY-at-K=3 (plan-freeze halt on detection).

2. **Element-1 anatomy-element disambiguation discipline at `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"` Item 1**: should Item 1 ("All 5 IS-not-IN anatomy elements present in entry text") be hardened to require explicit corner-cell + pillar-pair declaration at the substrate-IS observable element? The §W5-4 line 898 vs line 1011 inconsistency (Pillar II Mellin-Barnes residue at machinery PIN MAP vs Pillar III/IV K-window log-derivative at 5-anatomy Step 6) demonstrates that the current 5-anatomy completeness audit does NOT catch Element-1 ambiguity when the entry names two structurally distinct observables across different pillar pairs in different corner cells. A proposed Audit-Item-1-extension would add: "Element-1 declaration MUST name a SINGLE substrate-IS observable; if multiple observables are cited (cross-anatomy or cross-pillar), the entry routes to registry-INCOMPLETE-PENDING-ELEMENT-1-DISAMBIGUATION". Workshop-eligible structural rule extension for S91+.

3. **§VII.AG.1 SHARED-ANCHOR-COMPANION pattern vs §VII.AU FIRST-EXTRACTION pattern — taxonomy clarification workshop**: are these two structurally DIFFERENT outside-K-counter-vs-inside-K-counter mechanisms, or the same structural pattern viewed from different epistemic angles? §VII.AG.1 was OUTSIDE the K-counter due to HIT all 4 clauses FAIL (substrate III=III, lab IV=IV, bridge HKR=HKR refinement); §VII.AU is INSIDE HIT (clauses (i),(ii),(iii) PASS) but outside registry-PASS-eligibility via FIRST-EXTRACTION deferred-pending. The §VII.AG.1 entry retains full registry-entry status; §VII.AU's deferred-pending registration carries explicit `HIT-PASS-CANDIDATE-PENDING-EXTRACTION` qualifier per Sharpening 1 above. A taxonomy clarification workshop could disambiguate whether the §"Pre-S88 K=1 SHARED-ANCHOR-COMPANION" registry-entry-status mechanism and the new S89 W6 deferred-pending mechanism are co-existing structural patterns or a single mechanism viewed at different stages of K-counter advancement.

4. **Template-inheritance audit at `substrate-first-canonical-sourcing.md §(iv)`**: should the §(iv) rule (currently MANDATORY at K=4 for SCHEMATIC helpers consuming `_spectral_action_regulators.py`) be extended with a TEMPLATE-INHERITED sub-class that mandates the convention-tag retrofit lizzi's R2.2 proposes? The W4-2 NEGATIVE-CALIBRATION pattern from S88 W7b-83 (post-hoc disclosure at working-paper §VI line 513 only; no `-SCHEMATIC` convention-tag suffix) would lift to a structural TEMPLATE-INHERITED sub-class with explicit retrofit requirements: convention-tag suffix `-TEMPLATE-INHERITED-FROM-<citation>` for any producing script asserting structural-exact template predictions inherited from a registered calibration baseline. K=1 instance: §W5-6 line 1513 retrofit per R2.2. K=2/K=3 instances forecast from future template-inheritance patterns across the FWD-C1 / FWD-C2.bdg / FWD-C3 bridge families.

5. **(EVOI prioritization for S90 wave-plan)**: what is the EVOI ranking of CF-W5-3 (PROXY-REFINEMENT promotion gate; full BdG re-derivation at 7 L_max values) vs CF-W5-6-EXTENSION (FIRST-EXTRACTION promotion gate; first-ever L_max scan on FWD-C1 substrate-IS observable) for S90 wave-plan prioritization? CF-W5-3 unblocks §VII.AV PROXY-REFINEMENT → STAGE-1-CANDIDATE promotion; CF-W5-6-EXTENSION unblocks §VII.AU FIRST-EXTRACTION → STAGE-1-CANDIDATE promotion. If both PASS in S90, the cross-pillar-bridge corpus gains 2 structurally-independent calibration instances simultaneously, advancing the HIT K-counter K=1 → K=3 (single-dispatch dual-PASS hitting the K=3 MANDATORY promotion threshold per `feedback_rules-compensate-missing-structure.md`). The wave-plan ordering also matters: S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION (Element-1 fix per EMERGENCE #3) must land BEFORE CF-W5-3 to align bridge classification with substrate-IS observable; S90-FWD-C1-CONVENTION-TAG-RETROFIT-TEMPLATE-INHERITED must land BEFORE CF-W5-6-EXTENSION to enable the FIRST-EXTRACTION audit-script regex match.

---

## Wrap-Up — Workshop Impact Summary

### What Changed

- **§VII.AV pre-registration DOWNGRADES** from STAGE-1-CANDIDATE (pre-registered at §W5-4) to `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`; **§VII.AU pre-registration DOWNGRADES** from STAGE-1-CANDIDATE (pre-registered at §W5-6) to `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`. Both promotions to registry-PASS-eligible STAGE-1-CANDIDATE deferred to S90 carry-forwards. The two FWD candidates route to deferred-pending via STRUCTURALLY DIFFERENT mechanisms (cross-corner FORBIDDEN for §VII.AV; substrate-first-canonical-sourcing.md §(iv) TEMPLATE-INHERITED level-pin discipline for §VII.AU) but converge on the same intermediate verdict-class at the registry-anchor layer.

- **Rule-file diff to `cross-pillar-bridge-anatomy.md §"Enforcement clause"`** (lines 57-65) lands at S90 W0 introducing the deferred-pending intermediate verdict-class with TWO sub-class tags (`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`, `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`) sitting BETWEEN the existing IF Level-2-binding (PASS-ELIGIBLE) and IF Level-2-non-binding (INELIGIBLE) cases. SUGGESTION at K=1 with §VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION as the dual K=1 calibration instances; MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter threshold. Audit-script extension at `_cross_pillar_bridge_audit.py` regex-detects two distinct patterns. METHODOLOGY-class per `wave-classification.md §M4`; gate-ID appended to `methodology-wave-allowlist.md` with computed `sha256_of_plan_block`.

- **Lizzi's R1 L4 inheritance sub-clause EXPLICITLY RETRACTED** + L6.2 carry-forward (lizzi inheritance sub-clause landing) SUPERSEDED by connes's C5.2 (deferred-pending enforcement-clause clarification landing). The c-projection inheritance mechanism reading at L2 line 83 is structurally ruled out by the MANDATORY-at-K=3 cross-corner co-primary FORBIDDEN clause at `registry-landing.md` Detection item 4 (per S88 W-15 V.6 calibration instance #1); no rule-text exception exists. Lizzi conceded Q1 (no rule-text exception for cross-corner inheritance via "c-projection") + Q2 (no rule-text basis for the "Level-2-binding CLASS inheritance vs HIT K-counter advancement" two-track distinction) + Q4 (deferred-pending state is structurally better than the L4 SUGGESTION sub-clause).

### What Holds

- **Per-gate verdicts at S89 W5 STAND as audit-trail content.** §W5-3 INFO (composite=INFO; α=5.07 SCHEMATIC proxy + R²=0.9244 MARGINAL); §W5-4 PASS (corner-iv-singleton disambiguation gate); §W5-6 INFO (Planck σ=2.10 BY DESIGN). The deferred-pending downgrade is a REGISTRY-LAYER status update, NOT a retroactive invalidation of the per-gate verdicts. The §W5-3 SCHEMATIC convention tag `-CASIMIR-BOUND-PROXY` at line 592 + substrate-physics derivation at §W5-3 line 826 satisfy `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 level-pin discipline (W9c-1 POSITIVE-CALIBRATION pattern); honesty-discipline compliance is intact.

- **Cross-pillar-bridge K-counter (MANDATORY at K=3 per S88 W4a-17 close) preserved.** The Hybrid Independence Test K-counter advancement potential for §VII.AV + §VII.AU is preserved in the deferred-pending state. On dual CF-W5-3 + CF-W5-6-EXTENSION PASS in S90 (with prerequisite Element-1 disambiguation + TEMPLATE-INHERITED retrofit landed), both candidates promote to STAGE-1-CANDIDATE and the HIT K-counter advances K=1 → K=3 in a single dispatch, hitting the K=3 MANDATORY promotion threshold per `feedback_rules-compensate-missing-structure.md`. Deferred-pending entries are PRE-CURSORS to calibration-LANDING events, not structural BLOCKERS — registry-PASS-eligibility is suspended but K-counter-advancement potential is preserved (EMERGENCE #2 above).

- **§VII.AF.1.OP-PROJ HKR-bridge identification preserved as registry-anchor at the bridge-family level** for Pillar III ↔ Pillar IV (NOT inheritable across algebra-axis cells for per-observable Level-2-binding extraction). All four MANDATORY-at-K=3 disciplines are intact and operative: (a) `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` 5-anatomy + 3-level ladder; (b) `cross-pillar-bridge-corpus.md §6` algebra-axis orthogonality K-counter (MANDATORY at K=3 since S87 W-2 R3 close); (c) `registry-landing.md` Detection item 4 cross-corner co-primary FORBIDDEN; (d) `substrate-first-canonical-sourcing.md §(iv)` level-pin discipline (MANDATORY at K=4 since S88 W7b-83 close). The new deferred-pending sub-clause SUGGESTION at K=1 sits at the rule-file architecture layer between these MANDATORY clauses and the registry-anchor-timing layer; it does NOT abrogate any MANDATORY clause.

### What Breaks or Strains

- **§W5-4's 5-anatomy Element-1 declaration has a structural defect** (line 898 "FWD_C2_substrate_pillar | Pillar II (Mellin-Barnes residue)" vs line 1011 "1. substrate-IS observable: K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) (inherited from A.25/A.26)") that requires a NEW S90 carry-forward `S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION` to fix before CF-W5-3 promotes §VII.AV. The bridge classification at line 898 (Pillar II ↔ Pillar V) is mis-specified per lizzi's Q3 Fork B reading; the actual substrate-IS observable IS the K-window log-derivative (Pillar III/IV per §W5-3 line 609 explicit corner-cell declaration). §VII.AV may need to be RE-ANCHORED as a structurally distinct FWD candidate at the Pillar III/IV ↔ Pillar V family (closer to FWD-C3 substrate cocycle ↔ 3He-B/3He-A spec per `cross-pillar-bridge-corpus.md §4` lines 142-148), or as a re-spec of FWD-C2 with the substrate-IS observable updated from Mellin-Barnes residue to K-window log-derivative.

- **§W5-6's convention-tag at line 1513 lacks the `-TEMPLATE-INHERITED-FROM-W-5` suffix** that `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 retrofit clause requires for any post-W7b-83 (2026-05-05) producing script asserting structural-exact template predictions inherited from a registered calibration baseline. §W5-6 was authored at S89 (post-W7b-83 promotion to MANDATORY); it is NOT a pre-S88 grandfathered instance. Lizzi's R2.2 carry-forward (convention-tag retrofit at §W5-6 line 1513) is now MANDATORY compliance action, not SUGGESTION. Without the retrofit, §W5-6 is in the W4-2 NEGATIVE-CALIBRATION pattern at the substrate-first-canonical-sourcing.md §(iv) level-pin discipline layer (per Sharpening 2 above).

- **Framework rule-load growth at plan-freeze auditors**. The framework has accumulated FOUR MANDATORY rule-extension clauses at K=3+: (i) `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` 5-anatomy + 3-level + algebra-axis orthogonality (MANDATORY at K=3 since S88 W4a-17); (ii) `cross-pillar-bridge-corpus.md §6` algebra-axis orthogonality K-counter (MANDATORY at K=3 since S87 W-2 R3); (iii) `substrate-first-canonical-sourcing.md §(iv)` SCHEMATIC level-pin discipline (MANDATORY at K=4 since S88 W7b-83); (iv) `registry-landing.md` Detection item 4 cross-corner co-primary FORBIDDEN (MANDATORY at K=3 since S88 W-15 V.6). The new deferred-pending sub-clause SUGGESTION at K=1 (this workshop) sits atop these as a fifth methodology layer. The cumulative load on plan-freeze auditors (`_cross_pillar_bridge_audit.py`, `_registry_landing_audit.py`, `_substrate_first_provenance_audit.py`, `_source_reconciliation_audit.py`) is growing; a rule-consolidation workshop may be warranted at S91+ to identify whether any of these clauses can be unified into a higher-level structural framing without losing per-clause specificity.

### Carry-Forward Computations (deduplicated across all rounds)

Per `feedback_fix-in-session-never-defer.md`, each carry-forward computation MUST have all four fields: What / Inputs / Gate / Estimated effort. PRIMARY input to /rclab-plan for S90.

#### CF-1 — `S90-LEVEL-2-NON-BINDING-ENFORCEMENT-CLARIFICATION-DEFERRED-PENDING-SUB-CLASS-REFINEMENT`

Consolidated from connes C5.2 + lizzi R2.1.

- **What**: Land the consolidated rule-file diff at `cross-pillar-bridge-anatomy.md §"Enforcement clause"` lines 57-65, introducing the deferred-pending intermediate verdict-class with TWO sub-class tags. The new case sits BETWEEN existing IF Level-2-binding (PASS-ELIGIBLE) and IF Level-2-non-binding (INELIGIBLE) cases as a disjunction over (PROXY-REFINEMENT, FIRST-EXTRACTION) per the R2 CONVERGENCE on DISSENT #3 consolidated patch text. Extend `computations/_shared/_cross_pillar_bridge_audit.py` with two-sub-class regex detection: `convention=.*-(?:SCHEMATIC|PROXY)` + α-outside-band → PROXY-REFINEMENT; `convention=.*-TEMPLATE-INHERITED` (after retrofit) + no-L_max-scan in producing-script machinery pin → FIRST-EXTRACTION. Append gate-ID to `methodology-wave-allowlist.md` with computed `sha256_of_plan_block`. Land corpus row at `cross-pillar-bridge-corpus.md §1` as Calibration #3 with TWO worked examples (§VII.AV PROXY-REFINEMENT + §VII.AU FIRST-EXTRACTION).

- **Inputs**: `.claude/rules/cross-pillar-bridge-anatomy.md` (parent rule; §"Enforcement clause" lines 57-65 target); `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` (MANDATORY-at-K=4 SCHEMATIC-vs-physical level-pin discipline cross-reference); `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (calibration corpus extension target); `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` (this workshop's R2 verdict text as substitution-chain provenance); `computations/_shared/_cross_pillar_bridge_audit.py` (audit script to extend); `.claude/rules/methodology-wave-allowlist.md` (append gate-ID with computed sha256_of_plan_block per the append-only orchestrator-only-edit discipline); `.claude/rules/registry-landing.md §"Detection"` item 4 (cross-corner co-primary FORBIDDEN; explicitly preserved by the new sub-clause).

- **Gate**: PASS criterion per `wave-classification.md §M1` artifact-existence-with-substantive-content: (i) the consolidated diff is applied verbatim at parent rule lines 57-65 enforcement clause; (ii) audit-script regex extension committed with positive-match test cases (§W5-3 Casimir-bound proxy → PROXY-REFINEMENT; §W5-6 TEMPLATE-INHERITED after retrofit → FIRST-EXTRACTION) and negative-match test cases (a hypothetical SCHEMATIC envelope at α within predicted band → no flag; a hypothetical full-physical scan → no flag); (iii) corpus row landed at `cross-pillar-bridge-corpus.md §1` as Calibration #3; (iv) gate-ID appended to `methodology-wave-allowlist.md`; (v) SUGGESTION status at K=1 with §VII.AV + §VII.AU as the dual K=1 calibration instances; (vi) dual-SHA closure per `gate-verdicts.md` S87+ schema-v2 (`content_sha256` over the rule-file diff + `audit_sha256` over the input-pin map per the methodology-class dual-SHA discipline at `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`).

- **Estimated effort**: 0.5 agent-session. Authorship: connes-ncg-theorist PRIMARY for the Re:L4 BEFORE/AFTER patch structural direction; lizzi-spectral-functional-theorist CO-AUTHOR for the R2.1 sub-class refinement + audit-script regex extension; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` for the corpus row landing at `cross-pillar-bridge-corpus.md §1` Calibration #3; orchestrator-direct-write convention path per `wave-classification.md §"Dispatch consequences"` (METHODOLOGY-class).

- **Depends on**: this workshop's R2 verdict (verbatim consolidated patch text at the R2 CONVERGENCE on DISSENT #3 above). No upstream computational gate dependencies.

#### CF-2 — `S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS`

Consolidated from lizzi L6.1 + connes C5.1.

- **What**: Refine the empirical envelope α extraction at the Corner-IV K-window log-derivative substrate-IS observable by performing a FULL BdG re-derivation at each L_max ∈ {6, 7, 8, 9, 10, 11, 12} instead of the Casimir-bound Δ_eff(L_max) = Δ_static · (L_max+1)/13 proxy. Re-run the BCS gap equation `1/V = Σ_a 1/(2 E_a) tanh(E_a/2T)` on the L_max-truncated D_K spectrum at each L_max (regenerating Δ and the 8 BdG mode amplitudes u_k, v_k, E_qp from the truncated spectral kernel). Evaluate L_emp(L_max) via the §W5-2 numerical core. Output: refined `envelope_alpha`, `envelope_R²`, `envelope_log_A` over 7 L_max sectors + proxy-fidelity bias `bias_factor = α_proxy / α_full_bdg = 5.0679 / α_extracted`. PASS verdict TRIGGERS §VII.AV promotion from `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` (under CF-1's deferred-pending state) to registry-PASS-eligible STAGE-1-CANDIDATE.

- **Inputs**: `computations/session-52/s52_bogoliubov_amp.npz` (8-mode B1+B2+B3 BdG canonical amplitudes at L_max=12 reference; at L_max < 12 the modes are RE-DERIVED from the L_max-truncated spectral kernel, not just rescaled); `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (full L_max=12 D_K spectrum cache; 90 Peter-Weyl sectors; ~31M weighted eigenvalues; D_K Block-Diagonality pre-check per `math-scripts.md §"Machinery-Feasibility Audit"`); `computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz` (canonical anchor L_emp(∞) = -7.046336474406761 bit-for-bit per §W5-2 PASS); `computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.npz` (Casimir-bound proxy α=5.0679 / R²=0.9244 reference for bias quantification); canonical_constants.py: M_KK, tau_fold, Delta_BCS, M_KK-anchored BCS gap-equation parameters, n_modes_static=8 (FIXED branch index); `cross-pillar-bridge-anatomy.md` (parent rule for §VII.AV promotion semantics under CF-1's deferred-pending clarification); `permanent-results-registry.md §VII.AV` (the deferred-pending entry to promote on PASS).

- **Gate**: PASS criterion: extracted α ∈ [2.5, 3.5] (1-sigma band around predicted α=3 at substrate-distance-2 d=4 per S86 W-5 §VII.W) AND R² ≥ 0.95 (VALID band; tighter than §W5-3's MARGINAL [0.90, 0.95)) AND L_max=12 bit-for-bit anchor match (|L_emp(12) − (-7.046336474406761)| < 1e-9). PASS TRIGGERS §VII.AV promotion from `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` to registry-PASS-eligible STAGE-1-CANDIDATE; HIT K-counter advances K=1 → K=2 (with CF-3 PASS K=2 → K=3 single-dispatch). INFO band: α ∈ [2.0, 2.5) ∪ (3.5, 4.5] OR R² ∈ [0.90, 0.95) — §VII.AV remains REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT. FAIL: α outside [2.0, 4.5] OR R² < 0.90 OR L_max=12 anchor mismatch — §VII.AV downgrades to registry-INELIGIBLE per the strict §"Level-2-non-binding" enforcement. Dual-SHA closure per `gate-verdicts.md` S87+ schema-v2.

- **Estimated effort**: 1 agent-session. Authorship: volovik-superfluid-universe-theorist PRIMARY for the substrate-physics BdG re-derivation; connes-ncg-theorist CO-AUTHOR for the registry-promotion semantics + bridge-anatomy audit cross-check on Element-1 disambiguation (Kill-shot #3 resolution dependency on CF-5). Wall-time: ~30-60 min on AMD RX 9070 XT GPU for the 7-L_max BCS gap-equation iterative self-consistent solver + Bogoliubov diagonalization at each L_max sector (Peter-Weyl block-diagonal; sparse Lanczos via `torch.linalg` on GPU per `math-scripts.md §"Machinery-Feasibility Audit"` D_K Block-Diagonality pre-check).

- **Depends on**: CF-1 (rule-file diff must exist before deferred-pending tags are valid verdicts); CF-5 (Element-1 disambiguation must land BEFORE CF-2 to align bridge classification with substrate-IS observable per EMERGENCE #3); CF-6 (§VII.AV initial deferred-pending registration via mack-cosmic-bridge sole-writer).

#### CF-3 — `S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS`

From connes C5.3.

- **What**: First-ever L_max scan on the FWD-C1 substrate-IS observable (parameterized slope_A canonical → c_sub_corrected → n_s_recomputed Mellin-cone closure) across L_max ∈ {6, 7, 8, 9, 10, 11, 12}. At each L_max sector, evaluate c_sub_corrected via the M_Pl_eff² ratio on the L_max-truncated (A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max}); compute n_s_recomputed via the Route-B identity at substrate-distance-1 Mellin pole; extract empirical envelope α via log-log linear regression on `|n_s_recomputed(L_max) − n_s_FW_exact|` vs L_max. Output: empirical α, R², log_A for the FWD-C1 substrate-IS observable; comparison to structural-exact template prediction α=3 at d=4 (per §W5-6 line 1511 template-asserted envelope_alpha_predicted=3). PASS verdict TRIGGERS §VII.AU promotion from `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (under CF-1's deferred-pending state + CF-4's retrofit) to registry-PASS-eligible STAGE-1-CANDIDATE.

- **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (full L_max=12 D_K spectrum cache); canonical_constants.py: `n_s_FW_exact = Fraction(9561, 10000)`, `slope_A_FW_Conv_A_GEOMETRIC = "10.0 / (1 - tau/(5*pi))"`, `tau_fold = 0.19`, `c_sub_baseline = 2.238`, `planck_ns = 0.9649`; `cross-pillar-bridge-anatomy.md` (parent rule; FWD-C1 candidate spec at `cross-pillar-bridge-corpus.md §4` lines 120-128); `permanent-results-registry.md §VII.AU` (the deferred-pending entry to promote on PASS); `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6` (template-inheritance baseline for cross-check against the L_max=10 single-point evaluation); `computations/session-89/s89_w5_a30_fwd_c1_retry_parameterized_slope_A_canonical.npz` (S89 W5-6 single-L_max=10 reference for cross-check after CF-4 retrofit).

- **Gate**: PASS criterion: extracted α ∈ [2.5, 3.5] (1-sigma band around predicted α=3 at substrate-distance-1 d=4 per FWD-C1 spec) AND R² ≥ 0.95 AND L_max=10 anchor match (|n_s_recomputed(10) − n_s_FW_exact| < 1e-9). PASS TRIGGERS §VII.AU promotion from `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` to registry-PASS-eligible STAGE-1-CANDIDATE; HIT K-counter advances K=1 → K=2 (or K=2 → K=3 with CF-2 dual PASS single-dispatch hitting MANDATORY threshold). INFO band: α ∈ [2.0, 2.5) ∪ (3.5, 4.5] OR R² ∈ [0.90, 0.95) — §VII.AU remains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION. FAIL: α outside [2.0, 4.5] OR R² < 0.90 OR L_max=10 anchor mismatch — §VII.AU downgrades to registry-INELIGIBLE per strict Level-2-non-binding enforcement. Dual-SHA closure per `gate-verdicts.md` S87+ schema-v2.

- **Estimated effort**: 1 agent-session. Authorship: lizzi-spectral-functional-theorist PRIMARY for the Mellin-cone closure spectral evaluation + log-log regression; connes-ncg-theorist CO-AUTHOR for §VII.AU registry-promotion semantics + Pillar I ↔ Pillar II bridge-family HKR map identification at the FWD-C1 candidate level (a separate cross-pillar bridge anchor distinct from §VII.AF.1.OP-PROJ Pillar III ↔ Pillar IV per R2-A DISSENT #1). Wall-time: ~30-60 min on AMD RX 9070 XT GPU; per-L_max Mellin-cone evaluation is small workload.

- **Depends on**: CF-1 (deferred-pending state must exist as a valid registry verdict); CF-4 (TEMPLATE-INHERITED convention-tag retrofit MUST land before CF-3 to enable FIRST-EXTRACTION audit-script regex match per Sharpening 2); CF-6 (§VII.AU initial deferred-pending registration via mack-cosmic-bridge sole-writer).

#### CF-4 — `S90-FWD-C1-CONVENTION-TAG-RETROFIT-TEMPLATE-INHERITED`

From lizzi R2.2, promoted to MANDATORY per Sharpening 2.

- **What**: Retrofit the verdict-line convention tag at `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6` line 1513 from `convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical` to `convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical-TEMPLATE-INHERITED-FROM-W-5` per the `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4 retrofit clause. The retrofit is honesty-discipline only — it does NOT change §W5-6's INFO verdict or the σ=2.10 Planck distance value. It DOES route §VII.AU's deferred-pending entry to FIRST-EXTRACTION sub-class by triggering the audit-script regex match `convention=.*-TEMPLATE-INHERITED`. Update §W5-6 working-paper §(f) substrate-physics interpretation block to explicitly disclose the template-inheritance class per the W9c-1 POSITIVE-CALIBRATION pattern. Emit a SUPERSEDES-tagged corrective canonical line in `computations/session-89/s89_gate_verdicts.txt` per `v3-closure-recovery.md` Option A sig_5 remediation pathway, retaining the original convention tag entry as audit-trail content.

- **Inputs**: `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6` (working-paper section to retrofit; lines 1505-1640 approximately); `computations/session-89/s89_w5_a30_fwd_c1_retry_parameterized_slope_A_canonical.py` (producing script; verdict-line emission target for retrofit); `computations/session-89/s89_gate_verdicts.txt` (verdict file; corrective canonical line emission with SUPERSEDES tag); `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` (MANDATORY-at-K=4 retrofit clause for pre-W7b-83 instances + post-W7b-83 mandatory disclosure); `.claude/rules/regulator-convention-lockdown.md` (cross-link for retrofit convention-tag discipline); `.claude/rules/v3-closure-recovery.md §"Option A sig_5 remediation pathway"` (SUPERSEDES tag protocol); canonical_constants.py: existing pins unchanged (n_s_FW_exact, slope_A_FW_Conv_A_GEOMETRIC, tau_fold, c_sub_baseline, planck_ns).

- **Gate**: METHODOLOGY-leaning per `wave-classification.md §M4` (structural disclosure update, not new computation). PASS criterion: (i) retrofitted convention tag carries `-TEMPLATE-INHERITED-FROM-W-5` suffix at verdict-line layer; (ii) §W5-6 working-paper §(f) discloses template-inheritance class explicitly per W9c-1 positive-calibration model; (iii) §VII.AU deferred-pending tag at registry layer updates from generic to FIRST-EXTRACTION sub-class per CF-1's R2.1 refinement; (iv) corrective canonical line emitted in `s89_gate_verdicts.txt` per Option A sig_5 protocol with `supersedes=<full-64-char-original-audit_sha256>` tag pointing to the original §W5-6 verdict-line audit_sha256; (v) dual-SHA closure per S87+ schema-v2.

- **Estimated effort**: 0.25 agent-session. Authorship: lizzi-spectral-functional-theorist PRIMARY for the W9c-1-style honesty-disclosure retrofit; connes-ncg-theorist CO-AUTHOR cross-check on the deferred-pending sub-class routing alignment (FIRST-EXTRACTION regex match validation). Orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"`. Wall-time: minutes-scale (structural disclosure update, not numerical re-computation).

- **Depends on**: CF-1 (the FIRST-EXTRACTION sub-class must exist as a valid registry verdict before §VII.AU can be routed to it).

#### CF-5 — `S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION`

NEW from R2 EMERGENCE #3 + R2-A Q3 Fork B convergence.

- **What**: Disambiguate §W5-4's Element-1 anatomy declaration between line 898 (`FWD_C2_substrate_pillar | Pillar II (Mellin-Barnes residue)` from machinery PIN MAP) and line 1011 (`1. substrate-IS observable: K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) (inherited from A.25/A.26)` from 5-anatomy Step 6). Per R2-A Q3 Fork B convergence, the K-window log-derivative IS the actual substrate-IS observable executed at §W5-3 / §W5-4; the bridge classification at line 898 (Pillar II ↔ Pillar V) is mis-specified. Update §W5-4's bridge classification to "Pillar III/IV ↔ Pillar V" (aligning with the K-window log-derivative's Cell IV substrate-IS observable per §W5-3 line 609 corner-cell declaration). Re-evaluate whether §VII.AV remains in the original FWD-C2 candidate slot or routes to a STRUCTURALLY-NEW candidate slot (possibly FWD-C2.bdg or a re-spec of FWD-C2 from Mellin-Barnes residue to K-window log-derivative). Update Element-1 declaration text to name a SINGLE substrate-IS observable (the K-window log-derivative per Fork B) with explicit corner-cell + pillar-pair declaration. Emit a SUPERSEDES-tagged corrective canonical line per Option A sig_5 protocol; preserve original §W5-4 PASS verdict as audit-trail content.

- **Inputs**: `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-4` (working-paper section to disambiguate; lines 863-1150 approximately); `computations/session-89/s89_w5_a27_fwd_c2_observable_disambiguation.py` (producing script; verdict-line emission target); `computations/session-89/s89_gate_verdicts.txt` (verdict file; corrective canonical line emission); `sessions/permanent-results-registry.md §VII.AV` (the deferred-pending entry to update bridge-classification + Element-1 declaration); `sessions/framework/registry/cross-pillar-bridge-corpus.md §4` lines 132-148 (FWD-C2 / FWD-C3 spec for bridge-classification re-evaluation); `.claude/rules/cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"` Item 1 (5-anatomy completeness audit clause); `.claude/rules/v3-closure-recovery.md §"Option A sig_5 remediation pathway"` (SUPERSEDES tag protocol).

- **Gate**: METHODOLOGY-leaning per `wave-classification.md §M4` (structural disambiguation update, not new computation). PASS criterion: (i) §W5-4 Element-1 declaration names a SINGLE substrate-IS observable (the K-window log-derivative); (ii) bridge classification updated from "Pillar II ↔ Pillar V" (line 898) to "Pillar III/IV ↔ Pillar V" (aligned with Fork B); (iii) §VII.AV registry-anchor citation in `permanent-results-registry.md` updated to reflect the disambiguated bridge classification + Element-1 declaration; (iv) the disambiguated bridge classification's HIT substitution chain (against §VII.AF.1.OP-PROJ) re-evaluated and reported in verdict text (clause (i) substrate-IS pillar Pillar III/IV vs Pillar III may FAIL, collapsing K-counter advancement; in which case §VII.AV either re-routes to a SHARED-ANCHOR-COMPANION pattern OUTSIDE the K-counter, or is re-anchored as a structurally-new FWD candidate slot); (v) corrective canonical line emitted per Option A sig_5; (vi) dual-SHA closure per S87+ schema-v2.

- **Estimated effort**: 0.5 agent-session. Authorship: gen-physicist PRIMARY for the bridge-classification re-evaluation and Element-1 disambiguation logic; connes-ncg-theorist CO-AUTHOR for the registry-anchor citation alignment + bridge-anatomy 5-element completeness audit cross-check; lizzi-spectral-functional-theorist consulted on the substrate-IS observable identity (K-window log-derivative vs Mellin-Barnes residue). Orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"`. Wall-time: minutes-scale (structural disambiguation update).

- **Depends on**: CF-1 (deferred-pending state must exist as a valid registry verdict); CF-6 (§VII.AV initial deferred-pending registration via mack-cosmic-bridge). CF-5 MUST land BEFORE CF-2 in S90 wave-plan ordering (per EMERGENCE #3 above) so CF-2 operates on the disambiguated bridge classification.

#### CF-6 — `S90-VII-AV-VII-AU-DEFERRED-PENDING-MACK-LANDING`

NEW from R2 EMERGENCE #1 + Sharpening 1.

- **What**: Land both §VII.AV and §VII.AU initial deferred-pending registrations at S90 W0 in `sessions/permanent-results-registry.md` per mack-cosmic-bridge sole-writer protocol. §VII.AV registry text declares `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` sub-class tag with explicit cross-link to CF-2 (the gate that promotes §VII.AV on PASS) + CF-5 (the Element-1 disambiguation prerequisite). §VII.AU registry text declares `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` sub-class tag with explicit `HIT-PASS-CANDIDATE-PENDING-EXTRACTION` qualifier per Sharpening 1 + cross-link to CF-3 (the gate that promotes §VII.AU on PASS) + CF-4 (the TEMPLATE-INHERITED retrofit prerequisite). Both registry entries follow the 5-anatomy + 3-level ladder template per `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"` Items 1-4 with the deferred-pending qualifier on the Level-3 empirical-anchor declaration (empirical evidence pending CF-2 / CF-3 PASS).

- **Inputs**: `sessions/permanent-results-registry.md` (target registry file; §VII slot allocation per `registry-landing.md` next-free-letter protocol); `.claude/rules/cross-pillar-bridge-anatomy.md §"Enforcement clause"` (updated per CF-1 with the deferred-pending intermediate state + two sub-class tags); `.claude/rules/registry-landing.md §"Detection"` (item 4 cross-corner co-primary FORBIDDEN preserved); `.claude/rules/joint-theorem-promotion.md §"Stage 1"` (deferred-pending state is a pre-cursor to STAGE-1-CANDIDATE pre-registration per the 4-stage pathway); `sessions/framework/registry/cross-pillar-bridge-corpus.md §4` (FWD-C1 + FWD-C2 spec citations); `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` (this workshop as R2 verdict provenance, audit_sha256 to be computed); `feedback_mack-bridge-role.md` (sole-writer discipline for registry/inventory rows).

- **Gate**: PASS criterion: (i) §VII.AV initial deferred-pending registration landed in `permanent-results-registry.md` with sub-class tag `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` + 5-anatomy + Level-1 (cohomology-class identity at the bridge-family level inherited from §VII.AF.1.OP-PROJ — Claim A only, NOT the per-cocycle binding rate Claim B) + Level-2 envelope (SCHEMATIC proxy α=5.07 / R²=0.9244 disclosed as pre-cursor content) + Level-3 anchor (DEFERRED PENDING CF-2 full BdG re-derivation) + cross-link to CF-2 + CF-5; (ii) §VII.AU initial deferred-pending registration landed with sub-class tag `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` + 5-anatomy + Level-1 + Level-2 envelope (structural-exact L^{-3} template at d=4 inherited at parameter class) + Level-3 anchor (DEFERRED PENDING CF-3 FWD-C1 L_max scan) + `HIT-PASS-CANDIDATE-PENDING-EXTRACTION` qualifier + cross-link to CF-3 + CF-4; (iii) registry-landing audit (`_registry_landing_audit.py`) PASSes on both entries (no cross-corner co-primary structures; Detection item 4 satisfied since neither entry imports §VII.AF.1.OP-PROJ as co-primary anchor); (iv) dual-SHA closure per `gate-verdicts.md` S87+ schema-v2.

- **Estimated effort**: 0.25 agent-session. Authorship: mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (registry/inventory row landings); connes-ncg-theorist co-sign on the bridge-anatomy 5-anatomy + 3-level ladder declarations; lizzi-spectral-functional-theorist co-sign on the FIRST-EXTRACTION sub-class semantics for §VII.AU. Orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"`. Wall-time: minutes-scale.

- **Depends on**: CF-1 (rule-file diff must land BEFORE deferred-pending tags are valid verdicts; the deferred-pending intermediate state must exist in the rule text before mack writes the registry entries citing it). CF-6 BLOCKS CF-2 + CF-3 (the deferred-pending registry entries must exist before CF-2 / CF-3 can trigger their promotion semantics on PASS).

### Closing Line

Level-2-binding admissibility is per-observable, not registry-anchor-inheritable across algebra-axis cells; the deferred-pending intermediate verdict-class (PROXY-REFINEMENT vs FIRST-EXTRACTION sub-classes) is the structural placement for SCHEMATIC-proxy and TEMPLATE-INHERITED bridge candidates pending full per-observable extraction in S90, preserving registry-PASS-eligibility timing discipline AND Hybrid-Independence-Test K-counter advancement potential simultaneously.
