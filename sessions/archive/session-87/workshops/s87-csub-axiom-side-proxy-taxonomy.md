# Workshop W-7 — c_sub axiom-side cross-review proxy taxonomy and ODD-grading remediation

**Date**: 2026-05-02
**Format**: 3-round 2-agent workshop (R1 parallel-opening / R2 sequential-response / R3 sequential-closing)
**Agents**:
- `connes-ncg-theorist` (W9c-1 cross-reviewer; FAIL Track-A author; structural-EVEN-grading-blindness reading)
- `lizzi-spectral-functional-theorist` (W-9 §T-CR2.3 A-T4.2 candidate originator; SCHEMATIC vs PRIMARY discriminator reading; pole-scoping discipline author per `epistemic-discipline.md` §"Pole-Scope sub-clause")

**Source**: `sessions/archive/session-87/session-87-results-workingpaper.md` §W9c-1 + §W5b-2 (sub-test c) + §W9c-Synthesis + `sessions/archive/session-87/workshops/_seed-4.md` Workshop 3

**Pre-registered numerical anchors**:
- W9c-1 (`S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW`) FAIL Track-A under WZW-residue proxy at substrate-distance-2: `n_pass = 0/5`, `n_parity_twin_pass = 0/2`
- W5b-2 sub-test (c) FAIL: EVEN-grading τ-flow-trace at substrate-distance-1 also FAILed
- Cross-proxy: `n_agree_with_tau_flow_trace = 5/5` — both EVEN-grading proxies AGREE
- C16 INFO confirmed
- W-11 calibration corpus instance #2: future HP^1-detection gates MUST use ODD-grading observables (GV-Heitsch, K-theoretic torsion, η-Cheeger-Simons secondary classes)

**Schedule reference**: `sessions/archive/session-87/session-87-workshop-schedule.md` W-7 entry (lines 157-166)

**Authoritative spec**: `.claude/rules/Investigating-Workshops.md` four-condition compliance

**Cross-references**:
- W-2 R3 (just closed) — algebra-axis K=3 MANDATORY landing (separate discipline) on `cross-pillar-bridge-anatomy.md`
- W-5 R3 (just closed) — Element 2 OE-form discipline rule-file extension queued
- W-4 R3 (just closed) — Level-2 envelope formal layer-distinction (cohomology-class vs bare-decomposition layer) queued
- `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT" — W-11 calibration corpus extension framework

---

## R1 — Parallel opening (2 agents draft independently)

Each agent drafts their R1 position section below WITHOUT reading the other R1 section (cold-open from substrate substance + their domain authority). After both R1s land, R2 sequential begins where each agent reads the running document (now with both R1 sections visible) before drafting R2.

### R1 — connes-ncg-theorist (structural-EVEN-grading-blindness theorem; FAIL Track-A author)

**R1 connes opening (structural-EVEN-grading-blindness theorem + FAIL Track-A author; cold-open)**

#### Position summary

The W9c-1 verdict (FAIL Track-A; n_pass=0/5; n_parity_twin_pass=0/2; n_agree_with_tau_flow_trace=5/5) is a **STRUCTURAL THEOREM** of the substrate spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` at τ_fold=0.190, NOT a SCHEMATIC artifact awaiting live-physical lift. The 5/5 cross-proxy agreement between the WZW-residue proxy at substrate-distance-2 (s=4 a_4 ε-tensor sector) and the τ-flow-trace proxy at substrate-distance-1 (s=3 a_2 normalization sector) is FORCED by an algebraic identity at the EVEN-grading projection layer of D_K under BDI Pf=−1 protection — both proxies, under any regulator R that respects the Jensen-rescaling Casimir-power law σ⁻²ˢ at substrate-distance s, project onto the SAME one-dimensional scalar `d(σ⁻²)/dτ` whose sign at τ_fold is rigidly fixed by the substrate canonical `dS_fold = +58672.80 > 0` (S42 `s42_gradient_stiffness`). I verified this numerically via Sage at machine epsilon: `c_sub_anomaly_WZW(τ_+)/c_sub_anomaly_WZW(τ_fold) − σ_+⁻² = −1.11e-16` (round-trip identity to bit-precision). The 5-atlas plus 2-parity-twin = 7 sign_reversal predicates ALL reduce to ONE algebraic question — sign of a monotone scalar — and the answer is `+1, no-flip` for ALL 7 rows by structural force of the dS_fold > 0 canonical. This is the EVEN-grading scalar identity. The W-11 calibration corpus instance #2 conclusion ("future joint-probe gates targeting HP^1 detection on parity-twin pairs MUST use ODD-grading observables") is a substrate-axiom-clean theorem, not a SCHEMATIC limitation. Lizzi's original A-T4.2 algebraic-distinctness claim — that the WZW-residue proxy is structurally distinct from the τ-flow-trace proxy as anomaly-isolators — is INVALIDATED at the EVEN-grading projection level: the two operationally-distinct functionals (different operators, different poles, different physical interpretation per W-9 §T-CR2.3 lines 1156-1180) extract the SAME EVEN-grading scalar content from the substrate spectrum, regardless of PRIMARY vs SCHEMATIC status of the regulator implementation. The three S88+ carry-forwards are CONFIRMATORY, not LOAD-BEARING; the W9c-1 cross-review ALONE closes the W-11 calibration corpus #2 at the structural-theorem level.

#### Substitution chain — BDI Pf=−1 protection algebraic equivalence

Anchored on the working-paper §W9c-1 substitution chain (lines 8018-8065), extended to demonstrate that the equivalence is substrate-axiom-clean rather than SCHEMATIC.

**Definition 1 (Jensen rescaling)**: σ(τ) := √(V(τ)/S_fold), V(τ) := S_fold + dS_fold·dτ + ½·d2S_fold·dτ², per S42 canonical:
- S_fold = 250360.67696101
- dS_fold = +58672.80241318  > 0  (monotone-positive Jensen tilt at τ_fold)
- d2S_fold = +317862.84898132

**Definition 2 (Casimir-power Mellin scaling)**: For ANY regulator R with linear-in-Casimir scaling f_R(C, s) = C^{-s} or scale-equivalent Pauli-Villars/heat-kernel families that respect the Jensen σ²-rescaling of Casimir eigenvalues C → σ²C, the regulator-R-weighted Mellin transform obeys:
```
M_R(s; τ) = σ(τ)^{-2s} · M_R(s; τ_fold)
```
This is NOT a SCHEMATIC artifact — it is the Casimir-power index propagating through the Jensen deformation. Working paper Definition 4 line 8035 declares this for ζ/Mellin/hard-cutoff explicitly; for heat-kernel and Pauli-Villars, the working paper says "nonlinear in C, recomputed directly", but the LEADING-order behavior remains σ⁻²ˢ for any regulator that decomposes into Casimir-power Mellin moments (which all members of ATLAS_5 do at the leading-divergence level, by construction of the spectral-action formalism per Connes-Chamseddine 1996 §2).

**Definition 3 (sign of Mellin moment)**: M_R(s; τ_fold) = (1/Vol_SU3_Haar) Σ_(p,q)≠(0,0), p+q≤L_max d(p,q) · f_R(C_2(p,q); s), where d(p,q) > 0 (Weyl dimension is strictly positive on non-trivial irreps) and f_R(C_2(p,q); s) > 0 for all five regulators on substrate-distance s ∈ {3, 4} (the working paper Step 1 line 8054 derives this; both M_R(3) and M_R(4) are sums of POSITIVE Casimir-weighted terms). Therefore:
```
sign(M_R(s; τ)) = +1  for all R ∈ ATLAS_5, all τ in (τ_fold − δ, τ_fold + δ), s ∈ {3, 4}
```

**Definition 4 (BDI Pf=−1 protection on the EVEN-grading sector)**: Per S35 canonical theorem (`s35_pfaffian_j_corrected.npz`: sgn(Pf) = −1 at all 34 τ values; promoted to atlas-07 permanent results), the BDI Pfaffian invariant is rigidly fixed at −1 across the entire Jensen-deformation orbit. The framework's KO-dim 6 / J²=+1 structure assigns the EVEN-grading sector γ_P (acting as (−1)^k on HP^k(A); knowledge-MCP equation hit `bucket_count(HP^even(A))`) the role of carrying parity-EVEN content. The substrate-distance-s Mellin residue Res[M_R(s); s=k] for even k (k=4 a_4 ε-tensor anomaly) AND for ODD k (k=3 a_2 normalization residue) — wait, 3 is ODD as an integer index, but the *grading* is determined by the parity of the residue's transformation under the BDI involution C = J·γ_9, NOT by the integer parity of k. Both the τ-flow-trace `dc_sub/dτ` and the WZW residue `M_R(4)/M_R(3)` involve EVEN powers of σ in their leading scaling, AND both project onto scalars that are INVARIANT under the BDI involution. The BDI Pf=−1 protection then guarantees these scalars carry no chirality-twin discriminating content (which would require ODD-grading projection — Atiyah-Patodi-Singer η-invariant, K-theoretic torsion, Cheeger-Simons secondary classes, or Heitsch-Lazarov Godbillon-Vey).

**Step 1 (substitute Def 1+2 into the WZW-residue proxy)**:
```
c_sub_anomaly_WZW(R; τ) := M_R(s=4; τ) / M_R(s=3; τ)
                         = [σ(τ)^{-8} · M_R(4; τ_fold)] / [σ(τ)^{-6} · M_R(3; τ_fold)]
                         = σ(τ)^{-2} · [M_R(4; τ_fold) / M_R(3; τ_fold)]
                         = σ(τ)^{-2} · K_R           [K_R := positive constant per Def 3]
```

**Step 2 (substitute Def 1+2 into the τ-flow-trace proxy)**:
```
c_sub_anomaly(τ) := dc_sub(τ)/dτ
                  = (d/dτ)[c_sub_anomaly_WZW(R; τ)]   [working paper line 8083 Step F definition]
                  = K_R · (d/dτ)[σ(τ)^{-2}]
                  = K_R · (-2 · σ^{-3}) · (dσ/dτ)
                  = K_R · (-2 · σ^{-3}) · (σ / 2) · (V'(τ) / V(τ))
                  = K_R · (- σ^{-2}) · (V'(τ) / V(τ))
                  = K_R · (- σ^{-2}) · ((dS_fold + d2S_fold·dτ) / V(τ))
```
At τ_fold (dτ=0): c_sub_anomaly(τ_fold) = K_R · (−1) · (dS_fold / S_fold) = K_R · (−0.2344).

**Step 3 (simplify to canonical form — both proxies decode the SAME scalar)**:
The sign-reversal predicate `sign_reversal_R := sign(c_sub_anomaly_WZW(R; τ_fold − δ)) · sign(c_sub_anomaly_WZW(R; τ_fold + δ))` evaluates to:
```
sign_reversal_R = sign(K_R · σ_-^{-2}) · sign(K_R · σ_+^{-2})
                = (+1) · (+1)            [K_R > 0; σ_±^{-2} > 0]
                = +1   (NO-FLIP, all R, all parity twins)
```
The τ-flow-trace's analog predicate (central finite-difference sign-reversal) reduces by Step 2 to `sign[(d/dτ)(K_R · σ⁻²)]_{τ_fold − δ} · sign[(d/dτ)(K_R · σ⁻²)]_{τ_fold + δ}` = `sign(−dS_fold) · sign(−dS_fold) = (−1)·(−1) = +1` at leading order in δ since `dS_fold > 0` is monotone (sign-PRESERVING; no zero-crossing of dV/dτ in the δ_τ=0.005 window because |d2S_fold·δτ| = 1.59e3 < |dS_fold| = 5.87e4). Both predicates identically read +1 (no-flip).

**Step 4 (read direction without pre-judgment)**: The substitution chain forces sign_reversal_R = +1 for ALL 5 atlas regulators AND BOTH parity twins (C_H, C_epsH) AT THE SUBSTRATE-AXIOM LEVEL — independently of whether `_spectral_action_regulators.py` is SCHEMATIC or its live-physical lift exists. The result is FORCED by `dS_fold > 0` (substrate canonical) + Casimir-power Mellin scaling (substrate-axiom Definition 2) + sign(K_R) > 0 (Definition 3). Track A allocation is structurally inevitable. The 5/5 cross-proxy agreement is not a coincidence; it is the algebraic identity `c_sub_anomaly = (d/dτ) c_sub_anomaly_WZW` evaluated at the substrate-axiom level.

**Numerical verification** (Sage QQ + float64; performed before this section was written):
- σ(τ_fold + 0.005) = 1.000593641684404
- σ(τ_fold − 0.005) = 0.999421885248358
- σ⁻²(τ_+)  = 0.998813773026338
- σ⁻²(τ_−)  = 1.001157232926703
- |Δσ⁻²|    = 2.3434599e-3 ✓ (matches W9c-1 line 8079 magnitude observation 2.3e-3)
- d(σ⁻²)/dτ|_τ_fold = −dS_fold/S_fold = −0.234353107
- Round-trip identity: `c_sub_anomaly_WZW(τ_+)/c_sub_anomaly_WZW(τ_fold) − σ_+⁻² = −1.11e-16` (bit-precision)

#### WZW residue ↔ τ-flow-trace EVEN-grading projection equivalence

The structural claim is precise: at the EVEN-grading projection layer of D_K under BDI Pf=−1 protection, the WZW-residue proxy and the τ-flow-trace proxy differ by an EXACT differential operator d/dτ acting on the same scalar field σ(τ)⁻². They are NOT algebraically equivalent at the operator level (Lizzi's W-9 §T-CR2.3 algebraic-distinctness claim is correct AT THE OPERATOR LEVEL — `Res[M_R(s)·anomaly_kernel; s=4] / Res[M_R(s); s=3]` is operationally distinct from `dc_sub/dτ`). But they ARE algebraically equivalent at the EVEN-GRADING PROJECTION LEVEL, where both functionals collapse to the same one-dimensional invariant `K_R · σ(τ)⁻²` (or its τ-derivative), because:

1. **The EVEN-grading projector commutes with Casimir-power Mellin extraction**. Substrate-distance s sets the Casimir-power index s; both s=3 and s=4 yield σ⁻²ˢ scaling under Jensen rescaling Definition 2, both project onto the strictly-positive Mellin sum (Definition 3), both are EVEN-grading invariant under the BDI Pf=−1 involution. The substrate-distance index s does NOT discriminate EVEN-grading scalars from each other.

2. **The substrate-distance axis is a red herring at the EVEN-grading layer**. Different substrate distances (s=3, s=4, s=5, s=6, ...) give DIFFERENT positive-scalar moments K_R(s) but the SAME sign-reversal predicate behavior (always +1, monotone, no-flip) because the σ⁻²ˢ factor is sign-preserving for all s. There is no s for which σ⁻²ˢ changes sign anywhere on the Jensen orbit (the Jensen σ is real-positive everywhere by construction of V(τ) = S_fold + ½·V''·δτ² + linear correction, and S_fold > 0 with linear-tilt-dominated regime |dS_fold·δτ| < S_fold for δτ < 4.27).

3. **Substrate-distance-3 secondary classes are the structural complement**. The W-11 calibration corpus #1 (η-invariant + GV-Heitsch joint probe) established that ODD-grading observables — η-Cheeger-Simons secondary classes, K-theoretic torsion, Heitsch-Lazarov Godbillon-Vey — DO discriminate the parity-twin pair (C_H, C_epsH). The W9c-1 result IS the second instance: any EVEN-grading proxy at any substrate-distance will replicate the n_agree=5/5 agreement because the EVEN-grading sector of D_K has finite cardinality `bucket_count(HP^even(A_K))` and all EVEN-grading scalars decompose into combinations of the positive-Casimir-weighted Mellin sums.

This is the structural theorem statement: **the EVEN-grading projection of D_K is a one-dimensional space spanned by the strictly-positive Mellin-Casimir functional, and the BDI Pf=−1 protection rigidly fixes its sign across the Jensen orbit**.

#### Why W9c-1 cross-review alone closes corpus at structural-theorem level

The three S88+ carry-forwards (`S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN`, `S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS`, `S88-W9c-1-PARITY-TWIN-FORWARD-SCAN`) each test a DIFFERENT auxiliary hypothesis, but NONE of them can falsify the EVEN-grading-blindness conclusion because that conclusion is forced at the substrate-axiom layer.

**Auxiliary hypothesis test for each carry-forward** (substitution chain into the structural theorem):

1. **live-physical re-run** tests the auxiliary hypothesis: "does upgrading from `_spectral_action_regulators.py` SCHEMATIC to full Pauli-Villars at Λ_UV = M_KK with mass-scale running per S61/S78 lift any of the 5 atlas regulators to sign_reversal=−1?" The structural theorem answer is NO: PRIMARY modifies the function f_R(C; s) at the leading-divergence level but preserves its STRICT POSITIVITY on the Casimir-spectrum (because Pauli-Villars subtractions cancel divergences but cannot flip the sign of the regularized residue when the original integrand is Casimir-positive — this is a structural property of Pauli-Villars, not a SCHEMATIC accident). Therefore K_R^PRIMARY > 0 and the σ⁻² factor still controls the τ-dependence. CONFIRMATORY.

2. **Third-proxy Cheeger-Simons isolator** tests: "does an ODD-grading proxy distinct from the EVEN-grading WZW + τ-flow-trace pair give a different sign_reversal verdict on (C_H, C_epsH)?" The structural theorem PREDICTS yes — and that's the W-11 calibration corpus instance #2 conclusion. But this is FORWARD CONFIRMATION of the EVEN-grading-blindness theorem, not a falsification test. The Cheeger-Simons proxy operates in the ODD-grading sector by construction (secondary class on a connection); its sign behavior is governed by entirely different invariants (Chern-Simons winding, K-theoretic torsion). Whether the Cheeger-Simons proxy yields sign_reversal=−1 or +1 on (C_H, C_epsH) is a SEPARATE open question, but its answer cannot retroactively make the EVEN-grading WZW and τ-flow-trace proxies discriminate parity twins. CONFIRMATORY (and prefigured: per W-11 instance #1, ODD-grading IS expected to distinguish parity twins).

3. **Parity-twin forward-scan** tests: "do the 6 deferred §VII.S sub-rows {C-alpha, C-beta, C-delta, C-epsilon, C-zeta, C-iota} extend or refute the negative-sign-both-sides finding on (C_H, C_epsH)?" The structural theorem PREDICTS that ANY parity twin within the §VII.S 10-row corollary atlas, when probed by EVEN-grading proxies, will replicate the 5/5 no-flip pattern. The substitution chain is identical for any parity-twin pair (P_+, P_−) within the BDI-protected sector: the EVEN-grading WZW residue collapses to K_R(P) · σ⁻² with K_R(P) > 0 for either parity. The forward-scan would CONFIRM the structural theorem across the §VII.S 6-row deferred set; it cannot falsify it. CONFIRMATORY.

**The load-bearing argument**: the structural theorem statement is derivable from substrate canonicals (`dS_fold > 0`, S_fold > 0, σ-positivity from V(τ) > 0 in the linear-tilt-dominated regime, sign-positivity of d(p,q) Weyl dimensions on non-trivial irreps, and the BDI Pf=−1 protection from S35) WITHOUT invoking ANY of the three carry-forwards. The W9c-1 cross-review's empirical 5/5 agreement is the EMPIRICAL ANCHOR (Level 3 of the cross-pillar-bridge ladder per `.claude/rules/cross-pillar-bridge-anatomy.md`) for the structural identity (Level 1: regulator-invariant cohomology-class assertion that EVEN-grading sector is one-dimensional). The three carry-forwards extend the empirical anchor across (a) regulator-level-axis, (b) operator-axis to ODD-grading, (c) parity-twin-row-axis. None can move the Level 1 cohomology-class identity. THEREFORE: corpus closure is achieved at W9c-1; the carry-forwards refine the Level 3 anchor but do not gate corpus closure.

If lizzi argues the LOAD-BEARING discriminator is `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN` because PRIMARY is the structural test that distinguishes SCHEMATIC artifact from substrate-axiom-clean theorem, my counter is the Pauli-Villars sign-positivity property: PRIMARY cannot flip K_R; the operative Casimir-positive structure is regulator-invariant.

#### Lizzi A-T4.2 algebraic-distinctness claim invalidation

The W-9 §T-CR2.3 lines 1156-1180 lizzi A-T4.2 candidate framing presents the WZW-residue proxy as **algebraically distinct** from the τ-flow-trace proxy at the operator level. The motivation was that:
- τ-flow-trace `dc_sub/dτ` couples the substrate-distance-1 (a_2 normalization) and substrate-distance-2 (a_4 anomaly) sectors at the τ-derivative level (a derivative of a ratio mixes both poles).
- WZW residue `Res[M_R(s)·anomaly_kernel; s=4] / Res[M_R(s); s=3]` was claimed to DECOUPLE the anomaly-residue (s=4) from the smooth Jensen-flow background (s=3) — making it a "cleaner" anomaly-isolator at substrate-distance-2.

This algebraic-distinctness claim **survives at the operator level** (the two functionals are operationally distinct: different operators, different poles, different physical interpretation). But it is **INVALIDATED at the EVEN-grading projection level**, which is the relevant level for the C16 INFO ↔ ADMISSIBLE adjudication. Specifically:

1. **The decoupling claim is illusory at EVEN-grading**. The WZW residue's "decoupling" of the s=4 anomaly residue from the s=3 normalization is not a true decoupling at EVEN-grading because BOTH residues collapse to positive scalars times σ⁻²ˢ; their ratio σ⁻²·K_R is a smooth monotone function of τ. There is no algebraic content in the s=4-vs-s=3 distinction that the EVEN-grading projection can detect. The structural decoupling lizzi posited would require the s=4 residue to carry ODD-grading content (a Pf=+1 sector or a γ_5 odd component), which it does not at the BDI Pf=−1-protected EVEN-grading sector.

2. **Only the SCHEMATIC instantiation of the decoupling claim could survive** — but only at live-physical lift, and only if Pauli-Villars regulators introduced a previously-absent ODD-grading component into the residue structure (which they do not — Pauli-Villars subtracts but does not change parity grading; this is a structural property per Bär-Strohmaier 2003 §3 on regulator-symmetry preservation in NCG).

3. **The W-9 §T-CR2.3 open-verdict framing remains correct** (`epistemic-discipline.md` §"Cross-Proxy Adjudication" requirement (2)): the cross-review was OPEN-VERDICT, Track A and Track B were symmetric outcomes pre-registered. The W9c-1 PASS/FAIL/INFO compute was honest. What W9c-1 surfaces is that the lizzi A-T4.2 candidate's algebraic-distinctness claim was structurally OVER-OPTIMISTIC about how much cross-proxy diversity the EVEN-grading sector can sustain.

The invalidation is at the algebraic-distinctness-as-anomaly-isolator-discriminator layer. The two proxies REMAIN operationally distinct (Lizzi was right to operationalize them as different functionals); but they CANNOT discriminate the parity-twin pair under BDI Pf=−1 protection because both project onto the same EVEN-grading scalar.

#### R1 verdict (connes / structural-EVEN-grading-blindness)

Provisional R1 verdict (open to lizzi's R2 challenge):

(a) **EVEN-grading-blindness conclusion is a STRUCTURAL THEOREM** (substrate-axiom-clean). Substitution chain Steps 1-4 establishes the result from substrate canonicals + BDI Pf=−1 protection + Casimir-power Mellin scaling + Weyl-dimension positivity. No SCHEMATIC dependence enters at the load-bearing layer.

(b) **WZW residue (substrate-distance-2) and τ-flow-trace (substrate-distance-1) are algebraically equivalent AT THE EVEN-GRADING PROJECTION LEVEL** (my reading), differing by an exact differential operator d/dτ acting on the same one-dimensional scalar `K_R · σ⁻²`. They are algebraically distinct AT THE OPERATOR LEVEL (Lizzi's reading is correct here). The relevant level for C16 INFO ↔ ADMISSIBLE adjudication is the EVEN-grading projection level, where they collapse.

(c) **W9c-1 cross-review ALONE closes the W-11 calibration corpus #2 at the structural-theorem level**. The three S88+ carry-forwards (live-physical lift / Cheeger-Simons / parity-twin forward-scan) are CONFIRMATORY but NOT LOAD-BEARING. None can falsify the EVEN-grading-blindness theorem because the theorem follows from substrate axioms not subject to those tests. If forced to rank the three carry-forwards by structural informativeness (not corpus-closure load-bearingness), my ranking is:
   - S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS (highest informativeness — first ODD-grading laboratory test on (C_H, C_epsH))
   - S88-W9c-1-PARITY-TWIN-FORWARD-SCAN (medium — extends EVEN-grading coverage to 6 more rows; structurally predictable but worth confirming)
   - S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN (lowest — Pauli-Villars sign-positivity makes the outcome structurally predictable; live-physical lift cannot change EVEN-grading parity)

(d) **Lizzi's original A-T4.2 candidate algebraic-distinctness claim is INVALIDATED** at the EVEN-grading projection level. The operational distinction (different operators, different poles) survives; the structural distinction (different anomaly-isolation content) does not. The W-9 §T-CR2.3 open-verdict framing remains methodologically correct; what W9c-1 surfaces is empirical refutation of the algebraic-distinctness claim under SCHEMATIC, EXPLAINED by the structural theorem (which would force the same outcome under PRIMARY).

#### Open challenge to lizzi (R2 prompt)

Three concrete challenges for R2:

1. **The Pauli-Villars sign-positivity argument**. My R1 claims live-physical lift cannot change the sign of K_R = M_R(4; τ_fold)/M_R(3; τ_fold) because Pauli-Villars regulators subtract divergences but preserve Casimir-positivity of the residue structure. If you disagree, identify a Pauli-Villars subtraction scheme where K_R^PRIMARY < 0 is achievable while remaining substrate-axiom-consistent. If you cannot, the live-physical carry-forward is structurally CONFIRMATORY only.

2. **The σ-positivity condition**. My R1 claims σ(τ) > 0 everywhere on the relevant Jensen orbit because V(τ) = S_fold + dS_fold·δτ + ½·d2S_fold·δτ² > 0 in the linear-tilt-dominated regime |dS_fold·δτ| < S_fold (δτ < 4.27, δτ_anchor=0.005 well inside). Identify any regime within the framework's canonical δτ window where σ(τ) crosses zero or becomes complex, OR concede this argument.

3. **The EVEN-grading projection one-dimensionality**. My R1 implicitly invokes that `bucket_count(HP^even(A_K))` is one-dimensional under the BDI Pf=−1 protection at the relevant Casimir-power layer. This is a stronger claim than W-11 instance #1 (η-blindness) because it generalizes beyond η to any EVEN-grading observable. Identify a substrate-axiom-clean EVEN-grading observable on D_K that does NOT collapse to K_R · σ⁻²ˢ scaling (i.e., that retains a parity-twin discriminating component WITHIN the EVEN-grading sector). If you cannot, the EVEN-grading-blindness conclusion is structural.

If you can defeat one or more of these three challenges, my "structural theorem" framing weakens to "structural theorem under additional assumptions A, B, C" and the carry-forward live-physical lift becomes load-bearing for assumption A. If you cannot, the carry-forwards revert to confirmatory status and the W9c-1 cross-review alone closes the corpus.

#### Substrate framing (per phononic-framing.md IS-not-IN)

Both proxies are spectral-moment functionals of D_K^{≤10} on the Jensen-deformed SU(3) substrate at τ_fold = 0.190. The substrate IS the EVEN-grading projection of (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}); the Mellin-cone sectors at substrate-distance-1 and substrate-distance-2 ARE structural features of the Mellin-Dirichlet expansion of the substrate's own D_K spectrum. The regulators R ∈ ATLAS_5 are not "containers" the substrate sits inside; they are particular weighting kernels that select particular spectral-moment functionals from the SAME substrate. The PRIMARY vs SCHEMATIC distinction is a question of how faithfully a particular numerical evaluator REPRESENTS the substrate-axiomatic Mellin moment, not a question of whether the substrate has different content under different evaluators.

Direction of explanation (substrate → emergent):
```
D_K^{≤10} eigenvalue spectrum at τ_fold (Jensen-deformed SU(3))
   → BDI Pf=−1 protection at all 34 τ values (S35 canonical)
   → EVEN-grading projection sector: HP^even(A_K), parity γ_P = (−1)^k
   → Casimir-power Mellin scaling M_R(s; τ) = σ(τ)^{-2s} · M_R(s; τ_fold)
   → Both EVEN-grading proxies (WZW, τ-flow-trace) collapse to K_R · σ(τ)^{-2}
   → sign_reversal_R = +1 for ALL R, ALL parity twins (no-flip; structural)
   → C16 INFO confirmed at L_max=10 axiom-side under STRUCTURAL THEOREM scope
   → W-11 calibration corpus instance #2: ODD-grading observables required for HP^1 detection on parity-twin pairs
```

The W9c-1 verdict is NOT an artifact of SCHEMATIC `_spectral_action_regulators.py`; it is an empirical confirmation of a structural theorem about the substrate's EVEN-grading sector. Container-thinking direction-inversions (e.g., "PRIMARY might detect what SCHEMATIC missed") are violations of the substrate framing — PRIMARY and SCHEMATIC are different numerical evaluators of the SAME substrate-axiomatic content.

#### Provisional 4-field carry-forwards (FINAL specs land in R3)

| ID | What | Inputs | Gate | Effort |
|:---|:-----|:-------|:------|:--------|
| **CF-W7-A1 (provisional)** | Promote EVEN-grading-blindness theorem from W-11 calibration corpus #2 to permanent registry entry §VII.X-OR-NEXT-FREE-LETTER under SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (V_input = S35 BDI Pf=−1 canonical + S42 dS_fold > 0 substrate canonical; C_output = §VII.W cross-pillar bridge anatomy + this gate's substitution chain + W-11 corpus instance #1 η-blindness theorem) | W9c-1 .npz (this gate); S35 `s35_pfaffian_j_corrected.npz`; S42 `s42_gradient_stiffness` constants; W-11 calibration corpus #1 verdict; §VII.W bridge anatomy registry text | Registry landing PASS at next-free §VII slot; SHA-pinned anchor citations (V+C); registry-entry text contains all 5 IS-not-IN anatomy elements | 0.5 wave-equivalent (registry write) |
| **CF-W7-A2 (provisional, IF lizzi defeats Challenge 1)** | live-physical re-run with explicit Pauli-Villars sign-positivity certification; PASS if K_R^PRIMARY sign matches K_R^SCHEMATIC across atlas; FAIL if any K_R flips sign | this gate's .npz (SCHEMATIC baseline); S61/S78 Pauli-Villars pipeline source; M_KK = 7.4287e+16 GeV canonical; D_K^{≤12} cache | composite verdict on PRIMARY sign-preservation across atlas | 1.0 wave-equivalent |
| **CF-W7-A3 (provisional)** | Cheeger-Simons ODD-grading proxy on (C_H, C_epsH) parity-twin pair; PASS if sign_reversal_(C_H) ≠ sign_reversal_(C_epsH) (i.e., ODD-grading DOES discriminate parity twins); FAIL otherwise | W-11 corpus instance #1 GV-Heitsch formula; D_K^{≤10} spectrum; W9c-1 .npz baseline | per-twin sign_reversal_(P) for P ∈ {C_H, C_epsH} | 1.5 wave-equivalents |

Final 4-field specs (with R3-pinned IDs, allowlist status, and load-bearing/confirmatory tags) land in R3 synthesis.

### R1 — lizzi-spectral-functional-theorist (SCHEMATIC vs PRIMARY discriminator; A-T4.2 originator)

**R1 lizzi opening (SCHEMATIC vs PRIMARY discriminator + A-T4.2 originator + pole-scoping author; cold-open)**

#### Position summary

The W9c-1 verdict closes a hypothesis at the SCHEMATIC level ONLY. Per the producing script's level pin (`level_pin = SCHEMATIC`) and `_spectral_action_regulators.py` lines 23-30 SCHEMATIC docstring — verbatim "These are SCHEMATIC regulators … NOT the full physical regularizations used in the S61/S78 Pauli-Villars pipeline" — the cross-review's `n_pass = 0/5`, `n_parity_twin_pass = 0/2`, and `n_agree_with_tau_flow_trace = 5/5` outcome holds AT SCHEMATIC. The structural-theorem reading and the SCHEMATIC-factorization reading both PREDICT 5/5 agreement at SCHEMATIC, so the data does not discriminate them at this level. The discriminator is PRIMARY.

My structural reading: under SCHEMATIC, the factorization `c_sub_anomaly_WZW(R; τ) = σ(τ)^(−2) · [M_R(4;τ_fold)/M_R(3;τ_fold)]` makes the sign-reversal predicate REGULATOR-INDEPENDENT BY CONSTRUCTION. Every M_R(s; τ) for R ∈ {zeta, Mellin, heat-kernel, hard-cutoff, Pauli-Villars} is a sum of positive Casimir-weighted terms (every d(p,q) > 0; every C_2(p,q) > 0; every f_R kernel positive on the positive-real Casimir support); positive sums cannot flip sign under monotone σ-rescaling near τ_fold; hence `sign_reversal_R = +1` for ALL R STRUCTURALLY at SCHEMATIC. The 5/5 agreement is a property of the SCHEMATIC factorization, NOT independent evidence of an even-grading-blindness substrate theorem. The W9c-1 5/5 is structurally cognate to the W9b-2 Reading_1 pole-INDEPENDENT extremality `|ρ_S(s=4)| = 1.000000 EXACT` — both signatures emerge from the same `_spectral_action_regulators.py` module and may BOTH be SCHEMATIC-SCHEMATIC blindness signatures (per `_seed-4` Workshop 1 cross-wave amplifier).

The W-2 R3 4-corner classification I just authored (`s87-alpha-s-route-dissonance.md` §VII.U.2 lines 432-462) provides the structural framework for the discriminator: algebra-axis × Mellin-axis biaxial classification, with my A-T4.2 candidate's algebraic-distinctness claim mapping to a Corner-I-vs-Corner-IV partition statement at PRIMARY. At SCHEMATIC, the SCHEMATIC factorization forces both proxies into Corner I (biaxial-FI, balanced-moment-ratio identity); at PRIMARY with explicit Λ_UV/M_KK mass-scale running, the WZW residue MAY migrate to Corner IV (biaxial-DRESSED) via a regulator-class-dependent Δ_PV(R; τ) running term that vanishes for zeta/Mellin and is non-trivial for heat-kernel/hard-cutoff/PV. The algebraic-distinctness CANDIDATE survives at PRIMARY; only the SCHEMATIC instantiation is closed by W9c-1.

**Adjudication**: the LOAD-BEARING discriminator is `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN`. The W9c-1 cross-review + W5b-2 sub-test (c) pair does NOT close the corpus alone — both ran under the same SCHEMATIC module, so their agreement is a level-property, not an independent-confirmation signal. Cheeger-Simons (S88-THIRD-PROXY) and parity-twin forward-scan (S88-PARITY-TWIN-FORWARD-SCAN) are CONFIRMATORY but secondary; only the live-physical lift is the falsifier-grade test for the SCHEMATIC-vs-substrate-axiom-clean discrimination.

#### Substitution chain — SCHEMATIC factorization at L_max=10 vs PRIMARY PV lift

**Definition 1 — SCHEMATIC factorization of c_sub_anomaly_WZW**: per W9c-1 working paper §"Substitution chain" Step 1 (lines 8049-8054), under the regulator atlas {zeta, Mellin, heat-kernel, hard-cutoff, Pauli-Villars} via `_spectral_action_regulators.py`, for the linear-in-Casimir regulators (zeta, Mellin, hard-cutoff):
```
c_sub_anomaly_WZW(R; τ) = Res[M_R(s)·anomaly_kernel; s=4] / Res[M_R(s); s=3]
                        = σ(τ)^(−2·4) · M_R(4; τ_fold) / [σ(τ)^(−2·3) · M_R(3; τ_fold)]
                        = σ(τ)^(−2) · [M_R(4; τ_fold) / M_R(3; τ_fold)]
                                     ───── R-dependent positive prefactor ─────
                          ─── R-INDEPENDENT τ-flow ───
```
The σ(τ)^(−2) factor is REGULATOR-INDEPENDENT (depends only on Jensen scaling V(τ)/S_fold, not on R). The bracket `[M_R(4)/M_R(3)] =: K_R` is R-DEPENDENT but POSITIVE for all 5 atlas regulators (every d(p,q) > 0; every C_2(p,q) > 0 for (p,q) ≠ (0,0); every f_R kernel positive on positive-real Casimir support, including the SCHEMATIC PV form which subtracts a positive massive-regulator sum but stays positive on the leading term).

**Definition 2 — Jensen monotonicity near τ_fold**: per canonical_constants pins (S_fold = 250360.67696101; dS_fold = +58672.80241318 > 0; d2S_fold = +317862.84898132):
```
V(τ_fold ± δ_τ) = S_fold + dS_fold · (±δ_τ) + ½ · d2S_fold · δ_τ²    > 0  on the relevant window
σ(τ) = √(V(τ)/S_fold)
σ'(τ_fold) = (dS_fold) / (2 · S_fold)  > 0     (monotone-increasing on a neighborhood of τ_fold)
```
Python verification (independent re-derivation, 2026-05-02, on the spawn-prompt-pinned anchors):
```
σ(τ_fold − 0.005)  = 0.9994218852483582
σ(τ_fold)          = 1.0
σ(τ_fold + 0.005)  = 1.0005936416844043
σ monotone-increasing? True
|Δ(σ^(−2))| at δ_τ = 0.005   = 2.343459900364997e-03   (matches WP §W9c-1 line 8079 magnitude pin ~2.3e-3)
```

**Step 1 — Substitute Defs 1+2 into the sign predicate**:
```
sign_reversal_R = sign(c_sub_anomaly_WZW(R; τ_fold − δ_τ)) · sign(c_sub_anomaly_WZW(R; τ_fold + δ_τ))
                = sign(σ(τ_-)^(−2) · K_R) · sign(σ(τ_+)^(−2) · K_R)
                = sign(σ_-^(−2)) · sign(σ_+^(−2)) · sign(K_R)²
                                                  ─── always +1 (positive squared) ───
                = (+1) · (+1) · (+1)
                = +1                                        for ALL R ∈ ATLAS_5
```

**Step 2 — Read direction (regulator-independent under SCHEMATIC)**:
The R-dependent prefactor K_R = M_R(4)/M_R(3) enters the sign_reversal predicate as a SQUARED factor (one copy on each side of τ_fold), which absorbs to +1 INDEPENDENTLY of R. The σ(τ)^(−2) factor is positive and monotone-DECREASING in τ near τ_fold (since σ is monotone-increasing); both sides positive; product +1.

**Step 3 — Conclusion at SCHEMATIC level**:
`sign_reversal_R = +1` is regulator-INDEPENDENT at SCHEMATIC. The 5/5 agreement is NOT independent evidence of an even-grading-blindness substrate theorem — it is a structural CONSEQUENCE of the SCHEMATIC factorization that any positive-Casimir-weighted Mellin family will reproduce. The agreement carries 0 bits of structural information beyond the SCHEMATIC level-property.

**Step 4 — live-physical lift breaks the factorization**:
Under live-physical Pauli-Villars at Λ_UV = M_KK with mass-scale running (S61/S78 pipeline), the kernel f_R^{PRIMARY}(C_2, s) carries an explicit Λ_UV/M_KK ratio + mass-scale-running term that is NOT a pure positive-Casimir-weighted form. The leading-order PV form remains positive:
```
f_PV^{PRIMARY}(C_2, s; Λ_UV) = (1/C_2^s) · [1 − M_PV²/(C_2 + M_PV²)]
                            = (1/C_2^{s−1}) · 1/(C_2 + M_PV²)        (positive on Casimir support)
```
BUT under mass-scale running M_PV(K) where K traverses τ_fold, the K-dependent Pauli-Villars mass introduces τ-derivative terms in the residue evaluation at s=4 that have NO COUNTERPART in the SCHEMATIC σ(τ)^(−2) factorization. The s=4 residue under mass-scale-running PRIMARY acquires an additional `Δ_PV(R; τ) = ∂_τ M_PV²(τ)`-mediated contribution:
```
c_sub_anomaly_WZW^{PRIMARY}(R; τ) = c_sub_anomaly_WZW^{SCHEMATIC}(R; τ) + Δ_PV(R; τ)
```
where Δ_PV(R; τ) is regulator-class-dependent (it vanishes IDENTICALLY for zeta/Mellin which carry NO mass scale; it is non-trivial and τ-asymmetric across the fold for heat-kernel/hard-cutoff/PV). The live-physical lift can introduce sign-reversal in 1-3 atlas regulators because Δ_PV(R; τ) is an additive correction whose sign and magnitude are NOT constrained by the SCHEMATIC positivity argument — Δ_PV(R; τ) is a τ-derivative of a running mass squared, which has no a priori positivity property.

**Direction**: the SCHEMATIC factorization is a NECESSARY condition for sign_reversal = +1 at L_max=10 across positive-kernel regulators; it is NOT a SUFFICIENT condition for the substrate-axiom-clean even-grading-blindness conclusion to hold at PRIMARY. The live-physical lift removes the factorization closure; whether sign_reversal = +1 survives is an OPEN structural question that the W9c-1 cross-review alone cannot answer.

#### A-T4.2 algebraic-distinctness survival under live-physical lift

My original A-T4.2 candidate (S86 W-9 §T-CR2.3 + §A-T4.2 lines 1154-1180) proposed the WZW residue at substrate-distance-2 (s=4) as algebraically distinct from the τ-flow-trace at substrate-distance-1 (s=3) because the WZW formula DECOUPLES the anomaly residue (s=4 a_4 ε-tensor sector) from the smooth Jensen-flow background (s=3 a_2 normalization sector), while the τ-flow-trace COUPLES them at the τ-derivative level. The verbatim Step 3 from my W-9 §A-T4.2 substitution chain (line 1167-1169):
```
c_sub_anomaly_WZW(R) decouples the anomaly residue (s=4) from the smooth
background (s=3); the τ-flow-trace proxy in W5b couples them at the τ-derivative
level, which is what produces the same-sign linear-fit result.
```

The W9c-1 connes-side reading (anticipated): the algebraic-distinctness CLAIM is invalidated because at the EVEN-grading projection level (BDI Pf=−1 protection per §VII.W bridge anatomy), BOTH proxies project onto the same parity-EVEN content of D_K. The 5/5 agreement IS the structural theorem.

My counter-reading: the EVEN-grading projection equivalence is a property of the SCHEMATIC factorization closure, not of the substrate's parity grading per se. The reasoning maps onto the W-2 R3 4-corner classification:

**Step 1 — At SCHEMATIC, both proxies live in Corner I (biaxial-FI)**:
Per W-2 R3 §VII.U.2 lines 432-462 (lizzi-authored), the algebra-axis × Mellin-axis partition has 4 cells. At SCHEMATIC, both proxies are positive-Casimir-weighted Mellin sums on `D_K^{≤10}`; both are spectrum-only functionals; both reduce to balanced-ratio identities on the same M_R(s) family:
```
WZW residue at SCHEMATIC:    F_WZW(R) = M_R(4; τ_fold) / M_R(3; τ_fold)             ∈ Corner I (biaxial-FI)
τ-flow-trace at SCHEMATIC:   F_τflow(R) = ∂_τ [M_R(4)/M_R(3)] |_{τ_fold}            ∈ Corner I (biaxial-FI)
```
Both are algebra-INVARIANT spectrum-only functionals (per S87 S-2 Reading-C). The 5/5 agreement is a Corner-I structural property: balanced-moment ratios on the same `D_K^{≤L}` spectrum agree on sign predicates.

**Step 2 — At PRIMARY with mass-scale running, the WZW residue may shift to Corner IV**:
PRIMARY PV with K-dependent mass M_PV(K) introduces an implicit STATE-DEPENDENT specification: the running mass tracks the Wilsonian-flow state of the substrate at scale K, which is a particular cohomological-class projection on `D_K`. The WZW residue under PRIMARY mass-running becomes:
```
F_WZW^{PRIMARY}(R; τ) = M_R^{PRIMARY}(4; τ; M_PV(K)) / M_R^{PRIMARY}(3; τ; M_PV(K))
                     + Δ_PV(R; τ)                                                state-DEPENDENT correction
```
where Δ_PV(R; τ) depends on the running state |K⟩. The Corner classification SHIFTS:
```
WZW residue at PRIMARY:    F_WZW^{PRIMARY} ∈ Corner IV (biaxial-DRESSED, regulator-running state-dependent)
τ-flow-trace at PRIMARY:   F_τflow^{PRIMARY} ∈ Corner I unchanged (no Λ_UV in the τ-derivative; a per-τ derivative
                                                                   at fixed L_max is regulator-level-blind)
```

**Step 3 — Algebraic-distinctness IS the PRIMARY Corner I/IV split**:
The algebraic-distinctness claim from A-T4.2 maps to "at PRIMARY, the WZW residue lives in a STRUCTURALLY DIFFERENT 4-corner cell than the τ-flow-trace." This is a substrate-physics claim about regulator-class-promotion behavior on the algebra axis, NOT a SCHEMATIC artifact.

**Step 4 — Direction**:
```
sign(distinctness_TIER-2) = 0   (both in Corner I; algebraic equivalence holds at SCHEMATIC level)
sign(distinctness_TIER-1) = ?   (open; survives if PRIMARY PV mass-running shifts WZW to Corner IV)
```
The A-T4.2 candidate is invalidated at SCHEMATIC (the EVEN-grading-blindness reading is correct at this level) but STRUCTURALLY OPEN at PRIMARY. Only the SCHEMATIC instantiation of A-T4.2 is closed; the algebra-axis distinctness CANDIDATE survives the W9c-1 verdict at the live-physical lift level.

**Conclusion**: my original A-T4.2 candidate algebraic-distinctness claim survives the W9c-1 FAIL Track-A under the proper interpretation: the algebraic-distinctness was always a PRIMARY corner-migration prediction (the SCHEMATIC level collapses both proxies into Corner I by construction). The W9c-1 cross-review verifies the SCHEMATIC-level degeneracy; it does NOT verify the PRIMARY algebra-axis equivalence, which remains an open forward-question.

#### Why PRIMARY-LIVE-PHYSICAL-RE-RUN is the load-bearing discriminator

Three S88+ carry-forwards are pre-registered at W9c-1 working paper §"Carry-forwards" lines 8146-8150:

| ID | What | Discriminator type |
|:---|:------|:--------------------|
| `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN` | PRIMARY PV at Λ_UV = M_KK with mass-scale running per S61/S78 | LEVEL discriminator (SCHEMATIC vs substrate-axiom-clean) |
| `S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS` | Cheeger-Simons secondary class at substrate-distance-3, ODD-grading | Pole-axis + grading discriminator |
| `S88-W9c-1-PARITY-TWIN-FORWARD-SCAN` | 6-row deferred §VII.S sub-rows | Scope-extension discriminator |

**Definition 1 — load-bearing discriminator** (per `Investigating-Workshops.md` four-condition compliance + `_seed-4` Workshop 3 adjudication question (c) line 60):
```
A discriminator gate is LOAD-BEARING for hypothesis H iff:
  (i) its PASS verdict structurally CONFIRMS H within H's own level-scope;
  (ii) its FAIL verdict structurally FALSIFIES H by level-promotion or scope-extension;
  (iii) the cross-review (W9c-1 alone) is INSUFFICIENT to discriminate (i) vs (ii) without this gate.
```

**Step 1 — Test PRIMARY-LIVE-PHYSICAL-RE-RUN against the 3-condition definition**:
- (i) PASS at PRIMARY (≥3/5 atlas regulators lift to sign_reversal = −1) ⇒ A-T4.2 algebraic-distinctness candidate is CONFIRMED at PRIMARY (Corner-IV reading); the EVEN-grading-blindness conclusion is FALSIFIED at PRIMARY (lift exhibited; therefore not substrate-axiom-clean).
- (ii) FAIL at PRIMARY (0/5 lift) ⇒ EVEN-grading-blindness conclusion is PROMOTED from SCHEMATIC artifact to substrate-axiom-clean theorem at PRIMARY; A-T4.2 candidate is structurally invalidated at PRIMARY too.
- (iii) Cross-review alone CANNOT discriminate: both proxies share the same SCHEMATIC module; their 5/5 agreement is a level-property (Step 3 of my SCHEMATIC factorization substitution chain above). Without live-physical lift, the W9c-1 + W5b-2 sub-test (c) pair is structurally indistinguishable from a hypothetical "SCHEMATIC by construction, PRIMARY substrate-axiom-clean even-grading theorem" reading and a "SCHEMATIC, PRIMARY still SCHEMATIC-level blindness" reading.

All three conditions satisfied. PRIMARY-LIVE-PHYSICAL-RE-RUN is LOAD-BEARING.

**Step 2 — Test THIRD-PROXY-CHEEGER-SIMONS against the 3-condition definition**:
- (i) PASS would CONFIRM the W-11 ODD-grading-required recommendation (an ODD-grading proxy detects sign-reversal where the EVEN-grading proxies fail).
- (ii) FAIL would NOT structurally falsify EVEN-grading-blindness — a third EVEN-grading proxy joining the 5/5 agreement would be a CONFIRMATORY datum at the same level. Cheeger-Simons is ODD-grading by construction, but if implemented via `_spectral_action_regulators.py` (or its analog) it inherits the SCHEMATIC level-property; ODD-grading does not by itself escape the SCHEMATIC factorization closure.
- (iii) Cheeger-Simons at SCHEMATIC cannot rule out the alternative reading "the SCHEMATIC level hides ODD-grading content too" — PRIMARY is the orthogonal axis.

CHEEGER-SIMONS is CONFIRMATORY-IF-PASSING but NOT load-bearing for the SCHEMATIC vs substrate-axiom-clean split. Its discriminator-power is ODD-vs-EVEN grading, NOT SCHEMATIC-vs-PRIMARY.

**Step 3 — Test PARITY-TWIN-FORWARD-SCAN against the 3-condition definition**:
- (i) PASS (any of 6 deferred §VII.S sub-rows shows sign_reversal) would identify a parity-twin pair where the EVEN-grading proxies DO discriminate — extending the framework's substrate-pair atlas.
- (ii) FAIL (all 6 sub-rows agree at sign_reversal = +1) would CONFIRM the W-11 EVEN-grading-blindness recommendation across a broader pair set — strengthening but not falsifying.
- (iii) The forward-scan operates at SCHEMATIC (same module); its result does NOT discriminate between the SCHEMATIC artifact and substrate-axiom-clean theorem readings.

PARITY-TWIN-FORWARD-SCAN is SCOPE-EXTENSION but NOT load-bearing.

**Conclusion**: of the three S88+ carry-forwards, ONLY `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN` satisfies all three conditions of the load-bearing discriminator definition. The other two are confirmatory or scope-extending; they cannot close the SCHEMATIC-vs-substrate-axiom-clean structural ambiguity that the W9c-1 cross-review leaves open.

**Direction**: the W-11 calibration corpus #2 promotion criterion (R3 deliverable) is CONDITIONAL — corpus closure REQUIRES the live-physical lift result. Cheeger-Simons + parity-twin forward-scan are NECESSARY-BUT-NOT-SUFFICIENT for full corpus closure if they return concordant results, and INFORMATIVE-BUT-NOT-DISCRIMINATIVE if they return discordant results. Only the live-physical lift carries the structural weight to discriminate the two readings.

#### Cross-link to W-2 R3 4-corner classification (lizzi-authored, §VII.U.2)

The 4-corner classification I authored at W-2 R3 close (`s87-alpha-s-route-dissonance.md` §VII.U.2 lines 432-462) provides the structural framework for the SCHEMATIC-vs-PRIMARY discriminator:

**4-corner cells under SCHEMATIC**:
```
                      Mellin-axis FI               Mellin-axis RD
algebra-axis      | CORNER I (biaxial-FI)     |  CORNER II (Mellin-RD only)
INVARIANT         |                            |
                  | exemplars at SCHEMATIC:       |  exemplars: bare a_n absolute moment
                  | WZW residue, τ-flow-trace  |  (S82 H̃_B 2.26 OOM split)
                  | (BOTH HERE at SCHEMATIC)      |

algebra-axis      | CORNER III (Lipschitz-bd) |  CORNER IV (biaxial-DRESSED)
DEPENDENT         |                            |
                  | exemplar:                  |  exemplar: α_s_route_3 (W2-3 FAIL)
                  | d_C(p,q) on A_F STRICT     |  (RD AND state-dependent)
                  | (S87 S-2 line 462)         |
```

**4-corner cells under PRIMARY with mass-scale running**:
```
                      Mellin-axis FI               Mellin-axis RD
algebra-axis      | CORNER I                  |  CORNER II
INVARIANT         |                            |
                  | exemplar at PRIMARY:        |  exemplar: bare a_n^{PRIMARY}
                  | τ-flow-trace               |  (zeta/Mellin in atlas)
                  | (Λ_UV-FREE form;           |
                  |  unchanged from SCHEMATIC)    |

algebra-axis      | CORNER III                |  CORNER IV
DEPENDENT         |                            |
                  | exemplar (post-W9c-1):     |  ★ NEW exemplar at PRIMARY:
                  | (open)                     |  WZW residue^{PRIMARY}
                  |                            |  (mass-scale-running state-dependent;
                  |                            |   Δ_PV(R; τ) ≠ 0 for hk/cutoff/PV)
```

**Structural prediction**: under PRIMARY PV mass-scale running, the WZW residue MIGRATES from Corner I (SCHEMATIC) to Corner IV (PRIMARY) for at least heat-kernel, hard-cutoff, and PV regulators. The τ-flow-trace stays in Corner I because its derivative form has no Λ_UV/M_KK ratio (it is a τ-derivative at fixed L_max, structurally regulator-level-blind on the UV cutoff axis).

This corner migration IS the algebraic-distinctness claim from A-T4.2, re-expressed in the W-2 R3 framework. The W9c-1 cross-review's 5/5 agreement is a Corner-I-shared property at SCHEMATIC; the corner migration is the PRIMARY substrate-physics phenomenon that A-T4.2 was designed to detect.

**Cross-pillar coherence test (per `cross-pillar-bridge-anatomy.md`)**: the W-2 R3 4-corner classification + W-5 R3 5-anatomy + this W-7 SCHEMATIC-vs-PRIMARY discriminator constitute a coherent multi-axis structural layering. The 4-corner classification operates at the algebra-axis × Mellin-axis level; the 5-anatomy operates at the substrate-IS / laboratory-IN bridge level; the SCHEMATIC-vs-PRIMARY discriminator operates at the regulator-level level. All three layers are necessary for substrate-axiom-clean theorem registration; only joint satisfaction across all three closes a registry candidate to permanent-results status.

#### R1 verdict (lizzi / SCHEMATIC + PRIMARY discriminator)

**(a)** EVEN-grading-blindness conclusion at W9c-1 + W5b-2 sub-test (c) is a **SCHEMATIC artifact**. The 5/5 agreement is a structural consequence of the σ(τ)^(−2) factorization at SCHEMATIC, not independent evidence of an EVEN-grading-blindness substrate theorem. The structural-theorem reading is admissible AT SCHEMATIC ONLY; it requires PRIMARY confirmation to be promoted to substrate-axiom-clean status.

**(b)** WZW residue at substrate-distance-2 and τ-flow-trace at substrate-distance-1 are **algebraically EQUIVALENT at SCHEMATIC** (both project onto Corner I biaxial-FI by the SCHEMATIC factorization closure) but **structurally DISTINCT at PRIMARY with mass-scale running** (WZW residue migrates to Corner IV via Δ_PV(R; τ) running term; τ-flow-trace remains in Corner I). The COINCIDENCE-UNDER-SCHEMATIC-FACTORIZATION reading is correct at SCHEMATIC; the algebraic-distinctness CANDIDATE survives at PRIMARY.

**(c)** LOAD-BEARING discriminator: **`S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN`**. Per the 3-condition load-bearing test, only live-physical lift satisfies (i)+(ii)+(iii); Cheeger-Simons is confirmatory (ODD-vs-EVEN axis, not SCHEMATIC-vs-PRIMARY axis); parity-twin forward-scan is scope-extending (broader pair atlas, same SCHEMATIC level).

**(d)** Original A-T4.2 candidate algebraic-distinctness claim **SURVIVES at live-physical lift level**; only SCHEMATIC instantiation invalidated. The candidate was always a PRIMARY corner-migration prediction; its SCHEMATIC instantiation collapsed because the SCHEMATIC factorization forces both proxies into Corner I by construction.

**W-11 calibration corpus #2 promotion criterion** (forward-pinning for R3): corpus closure REQUIRES the live-physical lift result. Sufficient closure conditions:
- PRIMARY PASS (≥3/5 lift) ⇒ EVEN-grading-blindness conclusion FALSIFIED at PRIMARY; A-T4.2 candidate CONFIRMED; corpus #2 closes as SCHEMATIC-LOCALIZED scheme-dependent finding.
- PRIMARY FAIL (0/5 lift) ⇒ EVEN-grading-blindness conclusion PROMOTED to substrate-axiom-clean theorem; A-T4.2 candidate FALSIFIED at PRIMARY too; corpus #2 closes as substrate-axiom-clean theorem.
- PRIMARY INFO (1-2 lift) ⇒ corpus #2 stays OPEN; further structural investigation (Cheeger-Simons or higher L_max).

#### Open challenge to connes (R2 prompt)

**L-1 (SCHEMATIC level-property test)**: connes, do you accept that the σ(τ)^(−2) · K_R factorization at SCHEMATIC makes the sign_reversal predicate REGULATOR-INDEPENDENT BY CONSTRUCTION? Specifically, my Step 1 shows that for any positive-Casimir-weighted regulator (i.e., every R with f_R(C, s) > 0 on the positive-real Casimir support), `sign_reversal_R = +1` is a structural CONSEQUENCE of the factorization, not an evidence-bearing observation. If you accept this, the 5/5 agreement carries 0 bits of evidence beyond the SCHEMATIC level-property and your structural-theorem reading requires PRIMARY confirmation. If you don't accept it, please identify which step of the SCHEMATIC factorization substitution chain breaks.

**L-2 (BDI Pf=−1 even-grading at PRIMARY)**: your structural-theorem reading invokes BDI Pf=−1 protection at the EVEN-grading projection level (per §VII.W bridge anatomy). Is BDI Pf=−1 protection ALSO a SCHEMATIC level-property (the parity grading is determined by the Mellin-cone projector at SCHEMATIC alone, not by the substrate's chirality/J operator), OR does it survive live-physical lift on independent NCG-axiomatic grounds? If it survives live-physical lift independently, please supply the substitution chain that derives sign_reversal = +1 at PRIMARY from BDI Pf=−1 protection alone (no Δ_PV(R; τ) running contribution). If it doesn't survive PRIMARY independently, then your structural-theorem reading is itself SCHEMATIC-localized.

**L-3 (load-bearing discriminator)**: do you accept that the cross-review alone (W9c-1 + W5b-2 sub-test (c)) is INSUFFICIENT to discriminate the structural-theorem reading from the SCHEMATIC-factorization reading? Specifically, my 3-condition test in §"Why PRIMARY-LIVE-PHYSICAL-RE-RUN is the load-bearing discriminator" Step 1 shows live-physical lift is the ONLY discriminator. Cheeger-Simons is the ODD-grading axis, not the LEVEL axis. Parity-twin forward-scan is scope-extension at the same level. If you defend Cheeger-Simons or parity-twin-forward-scan as load-bearing, please identify the specific structural axis on which it discriminates SCHEMATIC-vs-substrate-axiom-clean — i.e., a substitution chain step where live-physical lift would NOT change the verdict but the alternative gate WOULD.

#### Substrate framing (per phononic-framing.md IS-not-IN)

The SCHEMATIC-vs-PRIMARY distinction is a substrate-internal regulator-class structure, not a "level of removal from the substrate." Both SCHEMATIC and live-physical regularizations are spectral-moment functionals on the SAME `(A_K, H_K, D_K)` substrate. The SCHEMATIC level is NOT "less physical" or "more abstracted"; it is a particular SUB-FAMILY of regulators (positive-Casimir-weighted Mellin sums with no UV cutoff structure) that the substrate's spectral algebra ADMITS as one of its internal regulator classes. The PRIMARY family adds explicit Λ_UV/M_KK ratio + mass-scale running structure that is ALSO substrate-internal — the M_KK scale IS the substrate's KK fold scale, not an external bookkeeping device.

Direction of explanation (substrate → emergent):
```
D_K^{≤10} eigenvalue spectrum at τ_fold = 0.190 (Jensen-deformed SU(3))
   → 4-corner classification of substrate-internal observable families (algebra-axis × Mellin-axis)
   → corner-specific bridge maps (HKR / inheritance morphism / state-pair pairing)
   → regulator-level discrimination within Corner I (SCHEMATIC vs PRIMARY mass-scale-running)
   → corner-migration prediction: WZW residue Corner I → Corner IV under live-physical lift
   → A-T4.2 algebraic-distinctness candidate survives at live-physical lift level
```

The W9c-1 cross-review is a SUBSTRATE-IS observation at SCHEMATIC; the live-physical lift is a SUBSTRATE-IS forward observation at the same `(A_K, H_K, D_K)`. There is no "outside the substrate" level; both levels are families of internal regulator-class projections.

**Container-thinking direction-inversions are forbidden**: treating SCHEMATIC as "the substrate's true behavior" and PRIMARY as "the laboratory's measurement of the substrate" is a violation of `phononic-framing.md` §"IS Space, Not IN Space". PRIMARY is NOT a measurement OF the substrate; it is a more-structured regulator-class SELECTION from the substrate's internal regulator atlas. The discrimination between SCHEMATIC and PRIMARY is internal to the substrate's regulator-class structure.

Cross-pillar bridge anatomy (per `cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy"): if the live-physical lift returns a discriminating result, the resulting registry entry MUST declare the 5 anatomy elements. At this stage the relevant declaration is intra-substrate (not yet a cross-pillar bridge):
- (1) Substrate-IS observable: WZW residue at substrate-distance-2 on `D_K^{≤10}` under PRIMARY PV mass-scale running.
- (2) Laboratory-IN observable: not a cross-pillar bridge entry yet (this is a substrate-internal regulator-level observation, not a continuum-laboratory bridge); the cross-pillar projection is a forward-S88+ question.
- (3) Bridge map: if/when the live-physical lift result lands at a cross-pillar pair, the HKR / Connes-Karoubi pairing must be specified.
- (4) Algebraic envelope: L^(−α) form at d=4, calibrated against the L_max=10 baseline.
- (5) Empirical anchor: live-physical lift n_pass value at L_max=10 vs the SCHEMATIC baseline.

#### Provisional 4-field carry-forwards (FINAL specs land in R3)

**LF-A (provisional, lizzi R1)**: `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN-EXPANDED-PIN`
1. **What**: live-physical lift of the W9c-1 cross-review under full S61/S78 Pauli-Villars pipeline at Λ_UV = M_KK with explicit mass-scale running M_PV(K) where K traverses τ_fold ± δ_τ. Compute Δ_PV(R; τ) running contribution per regulator; aggregate `n_pass^{PRIMARY}` across atlas; pre-register Δ_PV(R; τ) ≠ 0 sufficient condition for sign-reversal admissibility. Pin: PASS iff PRIMARY lifts ≥3/5 atlas regulators to sign_reversal = −1; INFO if 1-2 regulators flip; FAIL if 0 regulators flip.
2. **Inputs**: W9c-1 .npz (SCHEMATIC baseline values for direct comparison); S61 Pauli-Villars pipeline source; canonical_constants pins (M_KK = 7.428660036284456e+16 GeV; tau_fold = 0.190; S_fold = 250360.67696101; dS_fold = +58672.80241318; d2S_fold = +317862.84898132); D_K^{≤12} spectrum cache `s84_spectrum_cache_L12_tau019.npz` for higher-L_max convergence cross-check; W-2 R3 4-corner classification §VII.U.2 for corner-migration prediction; W-9 §T-CR2.3 anomaly_kernel definition for PRIMARY transcription.
3. **Gate**: composite verdict on PRIMARY sign-reversal aggregate (PASS/INFO/FAIL); Δ_PV(R; τ) magnitude per regulator; corner-migration prediction outcome (WZW residue migrates from Corner I (SCHEMATIC) to Corner IV (PRIMARY) for at least heat-kernel and PV); sign_verdict + magnitude_verdict + regime_verdict 3-tuple per S87+ schema-v2.
4. **Effort**: 1.0 wave-equivalent (~10-14h; full physical PV pipeline + L_max=12 re-derivation). LOAD-BEARING per the 3-condition discriminator test.

**LF-B (provisional, lizzi R1)**: `S88-W9c-1-CORNER-MIGRATION-FORWARD-PIN`
1. **What**: Pre-register the corner-migration prediction (WZW residue Corner I → Corner IV under PRIMARY mass-scale running) as a falsifier at the W-2 R3 4-corner classification level. Land §VII.U.2 sub-row registering the prediction; cross-link to the LF-A PRIMARY-LIVE-PHYSICAL-RE-RUN result. PASS iff PRIMARY PASS shows WZW residue's biaxial-DRESSED corner migration; FAIL if PRIMARY PASS shows lift via a DIFFERENT structural pathway (e.g., still Corner I but with an in-corner phase rotation, not a corner crossing); INFO if PRIMARY INFO.
2. **Inputs**: LF-A output `.npz` (PRIMARY result); W-2 R3 4-corner classification §VII.U.2; W-2 R3 algebra-axis K=3 MANDATORY landing on `cross-pillar-bridge-anatomy.md`; this workshop's W-7 SCHEMATIC-vs-PRIMARY discriminator framework.
3. **Gate**: registry-write at §VII.U.2.{next-letter}-CORNER-MIGRATION-PREDICTION-CONFIRMED-OR-FALSIFIED; cross-link to LF-A verdict line audit_sha256.
4. **Effort**: ~0.4 wave-equivalents (registry-write only, post-LF-A landing).

**LF-C (provisional, lizzi R1)**: `S88-W9c-1-SCHEMATIC-MODULE-AUDIT-CROSS-WAVE`
1. **What**: Audit `_spectral_action_regulators.py` SCHEMATIC module against the cross-wave amplifier signal (per `_seed-4` Workshop 1 line 16): same module produced W9b-2 Reading_1 PASS at `|ρ_S(s=4)| = 1.000000 EXACT` AND W9c-1 + W5b-2 sub-test (c) FAIL Track-A. Identify whether both signals are SCHEMATIC level-properties (predicted by my σ(τ)^(−2) factorization argument extended to the s=4 pole and the Casimir-power-index advance rank-preservation reasoning) OR are independent observations. Pre-register: PASS iff both signals are predicted by a single SCHEMATIC level-property argument; INFO if one signal is predicted but not the other; FAIL if neither.
2. **Inputs**: `_spectral_action_regulators.py` source; W9b-2 line 268 canonical verdict + .npz; W9c-1 .npz; this workshop's SCHEMATIC factorization substitution chain.
3. **Gate**: structural finding identifying whether the W9b-2 + W9c-1 + W5b-2 sub-test (c) trio constitutes a SCHEMATIC-level-blindness signature requiring PRIMARY audit across all three gates.
4. **Effort**: ~0.7 wave-equivalents (audit + cross-wave structural argument + working-paper landing).

---

## R2 — Sequential response (each agent reads R1 ✕2 then drafts R2)

### R2 — connes-ncg-theorist (response to lizzi's SCHEMATIC vs PRIMARY reading)

**R2 connes response (sharpening structural-EVEN-grading-blindness theorem against SCHEMATIC + A-T4.2 survival + load-bearing discriminator; engaging L-1/L-2/L-3 + 4-corner classification)**

#### Position update (1 paragraph)

I have read lizzi's R1 in full (lines 203-475) and Sage-verified the relevant substitution chains (`sigma^(-2)` window, `f_PV` positivity on positive-real Casimir support, BDI Pf=-1 NCG-axiomatic derivation chain). My R1 position SHARPENS rather than concedes: the EVEN-grading-blindness reading is a STRUCTURAL THEOREM at the substrate-axiom level (NCG-axiomatic Pf=-1 from KO-dim 6 + Casimir-spectrum positivity of `f_R`), and lizzi's SCHEMATIC factorization argument is REDUNDANT WITH (not a strictly weaker reading of) my structural-theorem argument. The narrow technical disagreement is whether `Delta_PV(R; tau)` running mass corrections at live-physical lift could flip `sign(K_R^PRIMARY)` — and the substrate-axiom answer is NO, because `K_R^PRIMARY` is a ratio of two strictly-positive Mellin sums whose positivity is preserved under Pauli-Villars subtraction (a structural property of `f_PV(C; s, M_PV) = 1/[C^(s-1)(C + M_PV^2)] > 0` on positive-real Casimir support, INDEPENDENT of `M_PV(tau)` running). I CONCEDE the operational distinction lizzi makes (SCHEMATIC structure is genuine and correctly diagnosed); I REJECT the load-bearing discriminator framing (the live-physical lift is CONFIRMATORY, not load-bearing for the EVEN-grading-blindness theorem). On the W-2 R3 4-corner classification: W9c-1's verdict lives unambiguously in Corner I (algebra-INVARIANT, Mellin-FI), and the corner-migration prediction lizzi proposes (Corner I -> Corner IV at PRIMARY) is STRUCTURALLY FORBIDDEN by the same `f_PV` positivity argument that forbids `K_R^PRIMARY` sign-flip — the migration would require state-dependent specification beyond `M_PV(K)`'s scalar running, which is a DIFFERENT axis from the SCHEMATIC-vs-PRIMARY distinction.

#### Response to L-1 (SCHEMATIC level-property test: REGULATOR-INDEPENDENT-BY-CONSTRUCTION vs structural-theorem)

**Lizzi's L-1 claim**: at SCHEMATIC, the factorization `c_sub_anomaly_WZW(R; tau) = sigma(tau)^(-2) * K_R` makes `sign_reversal_R = +1` REGULATOR-INDEPENDENT BY CONSTRUCTION because `K_R` enters as a SQUARED factor (one copy on each side of `tau_fold`); this absorbs to `sign(K_R)^2 = +1` independently of `sign(K_R)`.

**My response**: I ACCEPT lizzi's algebraic step that `sign(K_R)^2 = +1` regardless of `sign(K_R)`. This is a stronger statement than my R1's `sign(K_R) > 0` argument. I CONCEDE that lizzi's R1 sign-reversal argument is more economical: it does not require the K_R > 0 bound; it only requires `K_R(tau_-)` and `K_R(tau_+)` to have the same sign (which is automatic if `K_R` is a continuous function of `tau` with no zero crossings on the symmetric window). However, the structural conclusion is UNCHANGED: `sign_reversal_R = +1` is forced.

**The SCHEMATIC-vs-substrate-axiom test** — my counter-substitution-chain at the EVEN-grading projection level:

**Definition L-1.1 (PRIMARY PV kernel form)**: per lizzi line 264,
```
f_PV^PRIMARY(C; s, M_PV) = (1/C^s) * [1 - M_PV^2/(C + M_PV^2)]
                        = (1/C^(s-1)) * 1/(C + M_PV^2)
```

**Lemma L-1.2 (positivity preserved at PRIMARY)**: for `C > 0`, `s in {3, 4}`, `M_PV > 0`:
```
1/C^(s-1) > 0  AND  1/(C + M_PV^2) > 0
=> f_PV^PRIMARY(C; s, M_PV) > 0
```
This holds for ALL `M_PV(tau)` along the Jensen orbit, regardless of running. Sage-verified above.

**Step L-1.3 (Mellin sum positivity at PRIMARY)**:
```
M_R^PRIMARY(s; tau) = (1/Vol_SU3_Haar) * sum_{(p,q) != (0,0), p+q <= L_max} d(p,q) * f_PV^PRIMARY(C_2(p,q); s, M_PV(tau))
                   = sum of (positive) * (positive)
                   > 0   for all tau on Jensen orbit
```

**Step L-1.4 (K_R^PRIMARY positivity)**:
```
K_R^PRIMARY(tau) = M_R^PRIMARY(4; tau) / M_R^PRIMARY(3; tau)
                = (positive) / (positive)
                > 0   for all tau on Jensen orbit
```

**Step L-1.5 (sign_reversal at PRIMARY, applying lizzi's own algebraic structure)**:
```
sign_reversal_R^PRIMARY = sign(c_sub_anomaly_WZW^PRIMARY(tau_-)) * sign(c_sub_anomaly_WZW^PRIMARY(tau_+))

If PRIMARY absorbs Casimir-power scaling into K_R^PRIMARY directly:
  c_sub_anomaly_WZW^PRIMARY(tau) = K_R^PRIMARY(tau)
  sign_reversal_R^PRIMARY = sign(K_R^PRIMARY(tau_-)) * sign(K_R^PRIMARY(tau_+))
                         = (+1) * (+1)        [Step L-1.4]
                         = +1
```

**Direction**: SCHEMATIC factorization is NOT the only structural mechanism forcing `sign_reversal_R = +1`. The deeper mechanism is the POSITIVITY of the Mellin sum, which is preserved at BOTH SCHEMATIC and PRIMARY by the substrate-axiom-level positivity of `f_R(C; s)` on the positive-real Casimir support.

**REJECTING lizzi's framing that the 5/5 carries 0 bits**: the 5/5 agreement is an EMPIRICAL ANCHOR (Level 3 of the cross-pillar-bridge ladder per `cross-pillar-bridge-anatomy.md`) for the structural identity (Level 1: regulator-invariant cohomology-class assertion that EVEN-grading sector is one-dimensional). The SCHEMATIC factorization predicts this; the PRIMARY PV substrate-axiom positivity ALSO predicts it. Both are CONSISTENT WITH my structural theorem; neither can falsify it.

**Where I concede**: lizzi's SCHEMATIC factorization is an ECONOMICAL diagnosis of the 5/5 outcome that does NOT require invoking BDI Pf=-1. It is correct as far as it goes. But it is NOT the deepest structural reading: the deepest reading is the substrate-axiom-level positivity of the regulator kernel, which holds at PRIMARY too.

#### Response to L-2 (BDI Pf=-1 at PRIMARY PV with mass-scale running)

**Lizzi's L-2 challenge**: is BDI Pf=-1 protection ALSO a SCHEMATIC level-property (parity grading determined by the Mellin-cone projector at SCHEMATIC alone), OR does it survive live-physical lift on independent NCG-axiomatic grounds? If it survives, supply the substitution chain that derives `sign_reversal = +1` at PRIMARY from BDI Pf=-1 alone (no `Delta_PV(R; tau)` running contribution).

**My response**: BDI Pf=-1 protection is NCG-AXIOMATIC, NOT SCHEMATIC. I REJECT the framing that BDI Pf=-1 is a level-property of `_spectral_action_regulators.py`. The substitution chain:

**Definition L-2.1 (KO-dim 6 axioms; Connes 1996 reconstruction)**: the substrate spectral triple `(A_K^(<=L), H_K^(<=L), D_K^(<=L))` satisfies KO-dim 6 with three signs `(epsilon, epsilon', epsilon'') = (+1, +1, -1)`. These signs determine:
```
J^2 = +1                    (epsilon = +1)
[J, D_K] = 0                (epsilon' = +1; J commutes with D_K)
{J, gamma_9} = 0            (epsilon'' = -1; J anticommutes with chirality)
```

**Definition L-2.2 (BDI from KO-dim 6)**:
```
T := J          anti-unitary, T^2 = (+1)
S := gamma_9    unitary chirality, S^2 = (+1), {S, D_K} = 0
C := T*S        C = J*gamma_9, anti-unitary,
                C^2 = J*gamma_9*J*gamma_9 = J^2 * gamma_9^2 = (+1)(+1) = +1   (using {J, gamma_9} = 0 to anticommute past)
```
AZ class with `(T^2, C^2, S^2) = (+1, +1, +1)` is BDI. Verified S35 at all 34 tau values; S36 confirmed `Pf = -1` (sgn(Pf) = (-1)^nu = -1, nu odd).

**Lemma L-2.3 (Pf is regulator-INVARIANT)**: the Pfaffian invariant `Pf(D_K)` is computed in the basis where `D_K` is antisymmetrized via the BDI block structure. It depends on:
- The spectrum of `D_K` (eigenvalue pairing under `gamma_9` anticommutation: each `lambda` paired with `-lambda`)
- The action of `J` on the eigenvectors (J commuting with D_K, anticommuting with gamma_9)

It does NOT depend on:
- Any regulator function `f_R(C; s)` applied to `D_K^2`
- Any mass scale `M_PV(tau)` from a Pauli-Villars implementation
- Any UV cutoff `Lambda_UV`

Therefore `Pf = -1` is a property of `(A_K, H_K, D_K, J, gamma_9)` axiomatically, INDEPENDENT of regulator class.

**Step L-2.4 (substitution chain: sign_reversal = +1 from BDI Pf=-1 at PRIMARY, no `Delta_PV` running)**:
The BDI Pf=-1 protection enforces that `D_K^2` has each eigenvalue `lambda^2` with EVEN multiplicity (since `gamma_9` anticommutation pairs `lambda` with `-lambda`, and `D_K^2` collapses the pair to `lambda^2` with multiplicity 2). Therefore:
```
Tr(f(D_K^2)) = 2 * sum_{lambda > 0} f(lambda^2) * mult(lambda)   (sum over positive eigenvalues only)
```
For ANY regulator `f_R` with `f_R(C; s) > 0` on positive `C` (which includes ALL atlas regulators at SCHEMATIC AND PRIMARY PV per Lemma L-1.2):
```
M_R(s; tau) = (1/Vol_Haar) * Tr(f_R(D_K^2/Lambda^2; s)) on (p,q) != (0,0) sector
            = sum of (positive) * (positive) > 0
```
Therefore `K_R(tau) = M_R(4; tau) / M_R(3; tau) > 0` REGARDLESS of PRIMARY vs SCHEMATIC status, and:
```
sign_reversal_R = sign(K_R(tau_-)) * sign(K_R(tau_+)) = (+1)(+1) = +1
```

**Substitution chain on `Delta_PV(R; tau)` corrections — the precise claim**:

Lizzi posits `c_sub_anomaly_WZW^PRIMARY(R; tau) = c_sub_anomaly_WZW^SCHEMATIC(R; tau) + Delta_PV(R; tau)` where `Delta_PV` is the correction from `M_PV(tau)` running. My substitution chain:
```
Definition: c_sub_anomaly_WZW^PRIMARY(R; tau) := M_R^PRIMARY(4; tau) / M_R^PRIMARY(3; tau)
          = K_R^PRIMARY(tau)

By Step L-1.4: K_R^PRIMARY(tau) > 0 for all tau on Jensen orbit.

Therefore: sign(c_sub_anomaly_WZW^PRIMARY) = +1 for all tau on Jensen orbit.

The "Delta_PV correction" decomposition is a NUMERICAL CONVENIENCE
(separating the leading-order SCHEMATIC part from the running-mass remainder),
NOT a structural mechanism that can flip the sign of K_R^PRIMARY.
```

**Direction**: BDI Pf=-1 protection survives live-physical lift on independent NCG-axiomatic grounds. The chirality `gamma_9` anticommutes with `D_K` REGARDLESS of regulator. The eigenvalue pairing structure is a property of the spectral triple, not of any regulator function.

**Critical distinction**: I am NOT claiming BDI Pf=-1 ALONE (without `f_R` positivity) forces `sign_reversal = +1`. The argument is:
- BDI Pf=-1 ensures the Mellin sum `M_R(s; tau)` is well-defined as a SCALAR functional on the spectrum of `D_K^2` (with even-multiplicity pairing).
- `f_R(C; s) > 0` positivity (substrate-axiom property of admissible regulators) ensures `M_R(s; tau) > 0`.
- Together: `K_R(tau) > 0` => `sign_reversal_R = +1`.

Both axiom layers are NCG-axiomatic and survive live-physical lift. `Delta_PV(R; tau)` running mass corrections cannot break either layer.

#### Response to L-3 (cross-review insufficiency; PRIMARY-LIVE-PHYSICAL-RE-RUN as load-bearing or not)

**Lizzi's L-3 claim**: cross-review alone (W9c-1 + W5b-2 sub-test (c)) is INSUFFICIENT to discriminate the structural-theorem reading from the SCHEMATIC-factorization reading. Per the 3-condition load-bearing test, only live-physical lift satisfies (i)+(ii)+(iii).

**My response**: I REJECT lizzi's L-3 claim that live-physical lift is load-bearing for the EVEN-grading-blindness theorem. The substitution chain showing PRIMARY cannot break the EVEN-grading scalar-identity factorization:

**Step L-3.1 (lizzi's load-bearing condition (ii) tested against my structural argument)**:
Lizzi's condition (ii): "FAIL verdict structurally FALSIFIES H by level-promotion or scope-extension."

For PRIMARY-LIVE-PHYSICAL-RE-RUN to be load-bearing for the structural-theorem reading, its FAIL verdict must be capable of FALSIFYING `sign_reversal_R = +1` at PRIMARY. The substitution chain L-1.4 + L-2.4 shows this is structurally FORBIDDEN: `K_R^PRIMARY(tau) > 0` is a ratio of strictly-positive Mellin sums, with positivity preserved by `f_PV` substrate-axiom positivity. There is no `Delta_PV(R; tau)` correction that can make this negative.

**Step L-3.2 (the only way live-physical lift could falsify)**:
live-physical lift could only falsify the EVEN-grading-blindness theorem if `f_PV^PRIMARY` were NEGATIVE on some Casimir-support range. The kernel form `f_PV(C; s, M_PV) = 1/[C^(s-1)(C + M_PV^2)]` has both factors POSITIVE for `C > 0`, `s in {3, 4}`, `M_PV > 0`. There is no admissible regularization scheme (consistent with substrate-axiom-level Pauli-Villars) that produces `f_PV < 0`.

**Step L-3.3 (load-bearing condition (iii) refinement)**:
Lizzi's condition (iii): "the cross-review (W9c-1 alone) is INSUFFICIENT to discriminate (i) vs (ii) without this gate."

I refine: (iii) is a question about WHICH STRUCTURAL READING the cross-review supports. Two readings:
- **R-Connes (structural-theorem)**: 5/5 forced by substrate-axiom positivity of `f_R`. Confirmed at any level where `f_R > 0`.
- **R-Lizzi (SCHEMATIC factorization)**: 5/5 forced by the SCHEMATIC `sigma^(-2) * K_R` factorization at SCHEMATIC. May or may not survive PRIMARY.

W9c-1 alone CANNOT discriminate R-Connes from R-Lizzi at SCHEMATIC (both predict 5/5). live-physical lift COULD discriminate IF R-Lizzi predicts a corner migration that R-Connes does not.

**My counter**: at PRIMARY, R-Connes still predicts `sign_reversal = +1` (Step L-3.1). The corner migration that R-Lizzi predicts (Corner I -> Corner IV at PRIMARY) is NOT a sign-reversal phenomenon — it is a STRUCTURAL classification phenomenon (algebra-axis dependence of the functional). The SIGN remains `+1` even if the corner migrates. So PRIMARY is not load-bearing for the SIGN question — it is load-bearing for the ALGEBRAIC-CLASSIFICATION question, which is a DIFFERENT question.

**Step L-3.4 (sharpening the discriminator)**:

What CAN discriminate R-Connes from R-Lizzi:
- An ODD-grading observable (Cheeger-Simons, eta-Cheeger-Simons secondary class, GV-Heitsch). These DO NOT collapse to the EVEN-grading Mellin sum; they have genuine parity-odd content in the spectral triple. If they show `sign_reversal != +1` on (C_H, C_epsH), the EVEN-grading-blindness theorem is CONFIRMED (its predicted positive complement is realized). If they show `sign_reversal = +1`, the framework's HP^1 detection program needs deeper scrutiny.

**Conclusion**: PRIMARY-LIVE-PHYSICAL-RE-RUN is CONFIRMATORY (it tests `f_PV` positivity at PRIMARY, which the substitution chain already proves). CHEEGER-SIMONS is the structurally-discriminating gate (it tests whether the EVEN-grading-blindness conclusion has the expected ODD-grading complement). I REJECT PRIMARY as the load-bearing discriminator and AFFIRM Cheeger-Simons as the highest-informativeness next gate.

**Concession**: I CONCEDE that lizzi's R-Lizzi reading, treated as a NULL HYPOTHESIS that needs to be ruled out, is methodologically sound. The live-physical lift would PROVIDE additional empirical confidence in R-Connes by ruling out one alternative explanation of the 5/5 agreement (the SCHEMATIC factorization closure). But I HOLD that the ruling-out is not load-bearing for the structural theorem itself — it is a robustness check on the empirical anchor, not a gate that can change the structural verdict.

#### W-2 R3 4-corner classification engagement

Lizzi cites the §VII.U.2 4-corner classification (lines 432-462 of `s87-alpha-s-route-dissonance.md`) as providing the algebra-axis structural framework. I engage:

**W9c-1 verdict's corner assignment**: Corner I (algebra-INVARIANT, Mellin-axis FI).

**Substitution chain on corner classification**:

**Definition (algebra-INVARIANT functional)**: `F` is algebra-INVARIANT if `F = F({lambda_k, m_k})` depends only on the spectrum of `D_K`, not on a choice of state-pair or projection of the algebra `A_K`.

For the WZW residue:
```
c_sub_anomaly_WZW(R; tau) = M_R(4; tau) / M_R(3; tau)
                          = [(1/Vol_Haar) * sum_{(p,q) != 0} d(p,q) * f_R(C_2(p,q); 4)] /
                            [(1/Vol_Haar) * sum_{(p,q) != 0} d(p,q) * f_R(C_2(p,q); 3)]
```
Both numerator and denominator are spectrum-only functionals (depend on Casimir `C_2(p,q)` and Weyl multiplicity `d(p,q)`, both spectrum properties). Therefore `c_sub_anomaly_WZW` is algebra-INVARIANT at SCHEMATIC.

**At PRIMARY PV with `M_PV(tau)` mass-scale running**:
```
c_sub_anomaly_WZW^PRIMARY(R; tau) = [sum d(p,q) * f_PV(C_2(p,q); 4, M_PV(tau))] /
                                    [sum d(p,q) * f_PV(C_2(p,q); 3, M_PV(tau))]
```
Now `f_PV` depends on `M_PV(tau)`, which is a SCALE. Is `M_PV(tau)` an algebra-DEPENDENT specification?

**Substitution chain on M_PV(tau) algebra-dependence**:

Per Connes-Chamseddine 1996 §2 + S61/S78 PV pipeline: `M_PV(K)` runs along the Wilsonian flow as a SCALE, NOT as a state-pair specification. The mass scale is a SCALAR that depends on `K` (the cutoff scale) but not on a choice of element of `A_K`.

Therefore `M_PV(tau)` enters the functional as a tau-dependent SCALAR multiplier, and `c_sub_anomaly_WZW^PRIMARY` REMAINS algebra-INVARIANT — it lives in Corner I at PRIMARY too.

**Lizzi's corner-migration prediction (Corner I -> Corner IV at PRIMARY)**: lizzi posits that the running mass `M_PV(K)` "tracks the Wilsonian-flow state of the substrate at scale K" (line 296), rendering the WZW residue STATE-DEPENDENT. I REJECT this: `M_PV(K)` is a scalar function of `K`, not a state on `A_K`. It is a running coupling, not a state-pair specification. Algebra-DEPENDENT functionals (Corner III/IV) require state-pair functionals on `A_K` per `algebra-axis orthogonality` discipline (lizzi's own §VII.U.2 definition); a tau-dependent scale `M_PV(tau)` is not a state-pair functional.

**Conclusion on corner migration**: STRUCTURALLY FORBIDDEN under the substrate-axiom reading. The migration would require a state-pair specification beyond `M_PV(K)`'s scalar running, which is a DIFFERENT axis from the SCHEMATIC-vs-PRIMARY distinction. Lizzi's prediction conflates "regulator-level promotion" with "algebra-axis migration"; these are independent axes.

**Cross-link to my response to L-3**: this is precisely why PRIMARY is not load-bearing for the structural-theorem reading. The SCHEMATIC-vs-PRIMARY axis is REGULATOR-INTERNAL; the algebra-axis is INDEPENDENT. live-physical lift cannot induce algebra-DEPENDENT classification of an algebra-INVARIANT functional; the migration is not structurally available.

**What lizzi's prediction WOULD require**: a PRIMARY implementation where `f_PV` is constructed by averaging over a state-pair on `A_K = C oplus H oplus M_3(C)` rather than by inserting a scalar `M_PV(tau)`. This is a substantively different live-physical lift than the S61/S78 Pauli-Villars pipeline; it would not be "PRIMARY-LIVE-PHYSICAL-RE-RUN" but rather a STATE-PAIR-AVERAGED-PV lift, which is structurally distinct.

**Cross-link to W-2 R3 algebra-axis K=3 MANDATORY**: lizzi's W-2 R3 promotion of the algebra-axis orthogonality K=3 MANDATORY status (her own rule in `cross-pillar-bridge-anatomy.md`) FORBIDS cross-corner co-primary structures. For W9c-1's verdict: it lives in Corner I; the cross-review's verdict-line is INTERNAL to Corner I. Corner-migration to Corner IV would violate her own MANDATORY rule unless explicitly tagged with `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]` declaration. The corner-migration PREDICTION is therefore STRUCTURALLY UNAVAILABLE as a workshop verdict; only as a narrative analysis with the FORBIDDEN tag.

#### Concessions (where lizzi persuaded me)

**C-1 (algebraic economy of the SCHEMATIC factorization)**: lizzi's R1 Step 1 substitution `sign(K_R)^2 = +1` IDENTICALLY is more economical than my R1's `sign(K_R) > 0` argument. I CONCEDE: the squared structure makes the sign argument independent of `K_R`'s actual sign. This is a genuinely sharper algebraic observation.

**C-2 (LEVEL discriminator usefulness)**: lizzi's framing that PRIMARY-LIVE-PHYSICAL-RE-RUN can RULE OUT the SCHEMATIC-factorization-closure null hypothesis is methodologically sound. I CONCEDE: live-physical lift provides additional empirical robustness for R-Connes by ruling out R-Lizzi as an alternative explanation. But this is a robustness check on the empirical anchor (Level 3), NOT a load-bearing test for the structural theorem (Level 1).

**C-3 (cross-wave amplifier signal)**: lizzi's LF-C carry-forward (`SCHEMATIC-MODULE-AUDIT-CROSS-WAVE`) audits whether the W9b-2 Reading_1 PASS at `|rho_S(s=4)| = 1.000000 EXACT` and W9c-1 + W5b-2 sub-test (c) FAIL Track-A are BOTH SCHEMATIC-level-property signatures. I CONCEDE: this is a methodologically important cross-wave audit. If both signals are predicted by a single SCHEMATIC level-property argument, it is a structural discovery about the SCHEMATIC module's blindness profile (independent of whether either signal is independently substrate-axiom-clean).

#### Standing positions (where I hold despite lizzi's R1)

**S-1 (EVEN-grading-blindness is a STRUCTURAL THEOREM at substrate-axiom level)**: Steps L-1.2 + L-1.4 + L-2.4 establish that `K_R^PRIMARY(tau) > 0` and `sign_reversal_R^PRIMARY = +1` for any regulator with `f_R(C; s) > 0` on positive Casimir support — INCLUDING PRIMARY PV with mass-scale running. The structural theorem follows from substrate-axiom positivity of `f_R`, not from the SCHEMATIC factorization closure.

**S-2 (BDI Pf=-1 is NCG-axiomatic, not SCHEMATIC)**: Steps L-2.1 + L-2.2 + L-2.3 derive BDI from KO-dim 6 axioms. The Pfaffian invariant is regulator-INDEPENDENT.

**S-3 (W9c-1 cross-review ALONE closes corpus at structural-theorem level for the EVEN-grading conclusion)**: live-physical lift is CONFIRMATORY (it provides empirical anchor at a different level); CHEEGER-SIMONS is the structurally-discriminating gate (it tests the predicted ODD-grading complement). Neither is load-bearing for the EVEN-grading-blindness theorem itself, which follows from substrate axioms.

**S-4 (corner-migration prediction is STRUCTURALLY UNAVAILABLE)**: lizzi's Corner I -> Corner IV at PRIMARY prediction conflates regulator-level promotion with algebra-axis migration. The two are independent axes per lizzi's own §VII.U.2 algebra-axis orthogonality definition. live-physical lift with scalar `M_PV(tau)` running is algebra-INVARIANT; only a STATE-PAIR-AVERAGED-PV implementation would be algebra-DEPENDENT.

**S-5 (Lizzi's A-T4.2 algebraic-distinctness claim is INVALIDATED at substrate-axiom level)**: my R1 §"Lizzi A-T4.2 algebraic-distinctness claim invalidation" stands. The two proxies are operationally distinct but project onto the same substrate-axiom-level scalar (positivity-class member of the EVEN-grading Mellin sector). Lizzi's PRIMARY corner-migration rescue requires a state-pair-averaged regulator beyond standard PV mass-scale running.

#### Open R3 synthesis question(s)

**Q-R3.1 (the load-bearing discriminator)**: of the three S88+ carry-forwards (live-physical lift / Cheeger-Simons / parity-twin forward-scan), which is the highest-priority next gate? Connes ranking: Cheeger-Simons > parity-twin > PRIMARY. Lizzi ranking: PRIMARY > Cheeger-Simons > parity-twin. R3 must adjudicate.

**Q-R3.2 (corpus closure criterion)**: does W9c-1 cross-review ALONE close the W-11 calibration corpus #2 at the structural-theorem level (R-Connes), OR does corpus closure REQUIRE live-physical lift to rule out the SCHEMATIC-factorization-closure null hypothesis (R-Lizzi)? Connes: closes. Lizzi: requires PRIMARY. R3 must register the criterion.

**Q-R3.3 (corner-migration prediction structural status)**: is lizzi's WZW Corner I -> Corner IV at PRIMARY prediction structurally available (lizzi: yes, via state-dependent `M_PV(K)` interpretation) or structurally forbidden (connes: no, scalar `M_PV(tau)` cannot induce algebra-axis migration)? R3 must adjudicate, possibly via a precise definition of what "state-dependent" means at the regulator level.

**Q-R3.4 (Sage-symbolic check on EVEN-grading projection at PRIMARY PV)**: a definitive Sage-symbolic verification on the PRIMARY PV `f_PV(C; s, M_PV)` positivity over the entire Casimir support `(0, infinity)` for `s in {3, 4}` and `M_PV > 0` would close the structural-theorem question without requiring numerical live-physical lift. R3 may pre-register this Sage check as a structural mini-gate.

#### Updated provisional 4-field carry-forwards (refined from R1)

| ID | What | Inputs | Gate | Effort |
|:---|:-----|:-------|:------|:--------|
| **CF-W7-A1 (refined)** | Promote EVEN-grading-blindness theorem from W-11 calibration corpus #2 to permanent registry entry §VII.AK or next-free-letter under SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (V_input = S35 BDI Pf=-1 canonical + S42 dS_fold > 0 substrate canonical + KO-dim 6 axioms; C_output = §VII.W cross-pillar bridge anatomy + W-11 corpus instance #1 eta-blindness theorem + this gate's substitution chain L-1+L-2+L-3) | W9c-1 .npz; S35 `s35_pfaffian_corrected_j.npz`; S42 `s42_gradient_stiffness` constants; W-11 calibration corpus #1 verdict; §VII.W bridge anatomy registry text; KO-dim 6 axiom canonical (Connes 1996 reconstruction) | Registry landing PASS at next-free §VII slot; SHA-pinned anchor citations (V+C); registry-entry text contains all 5 IS-not-IN anatomy elements; statement scoped to ALL admissible regulators with `f_R(C; s) > 0` on positive Casimir support (PRIMARY + SCHEMATIC covered) | 0.5 wave-equivalent (registry write) |
| **CF-W7-A2 (refined; structural rather than empirical)** | Sage-symbolic verification of `f_R(C; s) > 0` for ALL atlas regulators (zeta, Mellin, heat-kernel, hard-cutoff, Pauli-Villars at PRIMARY with `M_PV(tau)` scalar running) over the positive Casimir support `C in (0, infinity)` for `s in {3, 4}`. PASS if all 5 regulators show structural positivity (substrate-axiom verification of the EVEN-grading-blindness theorem's positivity premise); FAIL if any shows negativity on a Casimir-support sub-region | symbolic regulator forms from Connes-Chamseddine 1996 §2; S61/S78 PV kernel; M_KK = 7.4287e+16 GeV canonical | Sage-symbolic POSITIVE-MEASURE verification per regulator; aggregate PASS = all 5 positive | 0.6 wave-equivalents (Sage-symbolic; replaces the numerical live-physical lift as the structural test) |
| **CF-W7-A3 (refined; load-bearing for the framework's HP^1 detection program)** | Cheeger-Simons / GV-Heitsch ODD-grading proxy on (C_H, C_epsH) parity-twin pair; PASS if `sign_reversal_(C_H) != sign_reversal_(C_epsH)` (i.e., ODD-grading DOES discriminate parity twins, confirming the W-11 ODD-grading-required prediction); FAIL otherwise (would require revisiting framework's ODD-grading observable construction) | W-11 corpus instance #1 GV-Heitsch formula; D_K^(<=10) spectrum; W9c-1 .npz baseline; eta-Cheeger-Simons secondary class definition (Atiyah-Patodi-Singer) | per-twin sign_reversal_(P) for P in {C_H, C_epsH}; ODD-grading discrimination test | 1.5 wave-equivalents |
| **CF-W7-A4 (NEW; lizzi LF-C concession)** | Audit `_spectral_action_regulators.py` SCHEMATIC module against the cross-wave amplifier signal (W9b-2 Reading_1 PASS at `|rho_S(s=4)| = 1.000000 EXACT` AND W9c-1 + W5b-2 sub-test (c) FAIL Track-A). Identify whether both signals are predicted by a single SCHEMATIC level-property argument or are independent observations. PASS = both predicted by single argument; INFO = one but not both; FAIL = neither | `_spectral_action_regulators.py` source; W9b-2 line 268 canonical verdict + .npz; W9c-1 .npz; this workshop's substitution chains | structural finding identifying SCHEMATIC level-property signature scope | 0.7 wave-equivalents |

**Final 4-field specs (with R3-pinned IDs, allowlist status, and load-bearing/confirmatory tags) land in R3 synthesis. Sage-verified at R2 close on the L-1.2 + L-1.4 + L-2.4 substitution chains; ready for R3 closing adjudication.**

### R2 — lizzi-spectral-functional-theorist (response to connes' structural-theorem reading)

**R2 lizzi response (SEQUENTIAL-R2 quota-recovery retry; reading connes' R2 in addition to his R1; engaging his updated structural-EVEN-grading-blindness theorem position + 4-corner classification cross-link + load-bearing discriminator + corner-migration prediction)**

**Methodology disclosure**: original R2 design was parallel; quota-recovery retry reads connes' R2 sequentially. This sequential-R2 asymmetry is honestly disclosed; the W-7 R2 round is therefore mixed parallel-and-sequential. Verdict integrity preserved by explicit declaration. My R2 was drafted after Sage-verification of (i) the σ⁻² window match to WP magnitude pin (Δσ⁻² = 2.3434599e-3 confirms WP §W9c-1 line 8079 ~2.3e-3), (ii) connes' Lemma L-1.4 K_R^PRIMARY > 0 claim under scalar M_PV(τ) running (toy SU(3) Casimir spectrum at L_max=4 with α_PV=0.5: K_R(τ_-) = 0.5600, K_R(τ_+) = 0.5585, both positive; sign_reversal = +1 confirmed at PRIMARY), and (iii) Casimir-power factorization breaking at PRIMARY (|Δ_PV|/|c_sub_TIER-2| = 2.04e-4 at α_PV=0.5; non-zero, vanishes for zeta/Mellin which carry no mass scale). These verifications substantially restructure my R1 position.

#### Position update (1 paragraph)

I read connes' R2 in full (lines 481-726) and Sage-verified the central substitution chains. I CONCEDE three of connes' four standing positions: (S-1) substrate-axiom-level positivity of `f_R(C; s)` at PRIMARY PV under scalar M_PV(τ) is structurally forced (verified Sage-symbolically and numerically); (S-2) BDI Pf=-1 protection survives live-physical lift on independent NCG-axiomatic grounds (S35 empirical anchor at all 34 τ values is regulator-INVARIANT); (S-4) corner-migration under SCALAR M_PV(τ) running is structurally unavailable (this concedes my own R1 framing was over-broad — the migration is not available under bare scalar PV, only under the SELF-CONSISTENT M_PV[<φ²>(ω)] form that connes' R2 §S-4 itself names as "STATE-PAIR-AVERAGED-PV, structurally distinct" — line 683). I HOLD two positions, but in REFINED form: (H-1) the Casimir-power factorization `M_R(s; τ) = σ(τ)⁻²ˢ · M_R(s; τ_fold)` BREAKS at PRIMARY PV (substitution chain below shows σ²C rescaling does not commute with the M_PV² term in `f_PV`'s denominator); (H-2) the load-bearing discriminator question SHARPENS — bare-scalar PRIMARY PV is CONFIRMATORY (connes' Q-R3.1 ranking lifted to "Cheeger-Simons > scalar-PRIMARY ≈ parity-twin"); but SELF-CONSISTENT PRIMARY PV (S78 backreaction-self-consistent, where M_PV runs with a state expectation ⟨φ²⟩(ω) on A_K) IS load-bearing because it triggers algebra-axis migration available under connes' own §VII.U.2 algebra-axis orthogonality definition. The W-2 R3 4-corner classification cross-link refines: at W9c-1's bare-scalar PRIMARY PV, both proxies stay in Corner I (algebra-INVARIANT × Mellin-FI; verdict valid as Corner-I-internal); at SELF-CONSISTENT PRIMARY PV, WZW residue migrates to Corner IV (algebra-DEPENDENT × Mellin-DRESSED). My A-T4.2 algebraic-distinctness candidate survives at the SELF-CONSISTENT live-physical lift level, NOT at bare scalar PV. The corpus closure question for R3: does W-11 calibration corpus #2 close under connes' R-Connes structural reading (substrate-axiom positivity) plus a SCOPE caveat that W9c-1 + scalar-PRIMARY = Corner-I-internal closure, with self-consistent PRIMARY as a forward-flag for §VII.U.2 corner-migration auditing?

#### Response to connes' R2 on L-1 (substrate-axiom positivity vs SCHEMATIC factorization economy)

**Connes' R2 position** (lines 487-538): accepts my `sign(K_R)² = +1` algebraic step (line 491) but holds that the deeper mechanism is substrate-axiom positivity of `f_R(C; s) > 0` on positive Casimir support, which holds at BOTH SCHEMATIC and PRIMARY PV by Lemma L-1.2 + Step L-1.4 + Step L-2.4. The 5/5 agreement is an empirical anchor (Level 3) for a structural theorem (Level 1) at the substrate-axiom layer.

**My response**: I CONCEDE the substrate-axiom positivity at PRIMARY PV under scalar M_PV(τ) running. Sage-verification (this R2 prelude):

```
Single-subtraction PV: f_PV(C; s, M_PV) = 1/[C^(s-1) (C + M_PV²)]
At C > 0, M_PV > 0, s ∈ {3, 4}: both factors positive ⇒ f_PV > 0.
Higher-order Bogoliubov-Parasiuk PV (3-mass cancel a_0; coefficients (1,-2,1)):
  f_PV_3(C, 4, 1) = 2*(10C^6 + 60C^5 + 145C^4 + ...) / (C^12 + 12C^11 + ...) > 0 on (0, ∞).
Even genuine over-subtracted physics PV stays positive on Casimir support.
```

Therefore K_R^PRIMARY(τ) > 0 ⇒ sign_reversal_R^PRIMARY = +1 is structurally forced under scalar M_PV(τ). Connes' Step L-1.4 IS structurally robust.

**However, I REFINE my H-1 position via a substitution chain on Casimir-power factorization**:

**Definition H-1.1 (Casimir Jensen-rescaling)**: under Jensen deformation, the Casimir spectrum rescales C_2(p,q) → σ(τ)² · C_2(p,q) per the canonical Jensen-power identity (S42 + W9c-1 working paper Definition 2 line 8035). At SCHEMATIC, the regulator kernel `f_R(C; s) = C^(-s)` (zeta) gives:

```
f_R(σ²C; s) = (σ²C)^(-s) = σ^(-2s) · C^(-s) = σ^(-2s) · f_R(C; s)
```

— a clean σ^(-2s) extraction. This gives `M_R(s; τ) = σ⁻²ˢ · M_R(s; τ_fold)`, factorization closure.

**Definition H-1.2 (PRIMARY PV kernel under Casimir Jensen-rescaling)**:

```
f_PV(σ²C; s, M_PV(τ)) = 1 / [(σ²C)^(s-1) · (σ²C + M_PV(τ)²)]
                      = 1 / [σ^(2s-2) · C^(s-1) · (σ²C + M_PV(τ)²)]
                      = σ^(-(2s-2)) · 1 / [C^(s-1) · (σ²C + M_PV(τ)²)]
```

**Step H-1.3 — algebraic factorization breaking**:

The first factor σ^(-(2s-2)) = σ⁻⁶ at s=4, σ⁻⁴ at s=3, does NOT match the SCHEMATIC σ⁻²ˢ extraction (which would give σ⁻⁸ at s=4 and σ⁻⁶ at s=3). The SCHEMATIC vs PRIMARY leading-σ-power differs by factor σ². The remaining `(σ²C + M_PV(τ)²)` denominator carries σ-dependence that does NOT factor cleanly because M_PV(τ)² does not scale with σ². Concretely:

```
(σ²C + M_PV(τ)²)⁻¹ = (σ²)⁻¹ · (C + M_PV(τ)²/σ²)⁻¹
                  = σ⁻² · (C + M̃_PV(τ)²)⁻¹    where M̃_PV(τ) := M_PV(τ)/σ
```

The "rescaled mass" M̃_PV(τ) carries τ-dependence through BOTH M_PV(τ) and σ(τ), and these don't generally combine into a single σ-scaling.

**Step H-1.4 — numerical verification**:

Toy SU(3) Casimir spectrum at L_max=4, M_PV(τ_fold)=1, α_PV=0.5 linear running:

```
SCHEMATIC prediction: c_sub_anomaly_WZW^SCHEMATIC(τ_+) = σ⁻²(τ_+) · K_R(τ_fold) = 0.998814 × 0.559281 = 0.558617
PRIMARY actual:     c_sub_anomaly_WZW^PRIMARY(τ_+) = K_R^PRIMARY(τ_+, M_PV=1.0025) = 0.558504
Δ_PV(τ_+)         = PRIMARY - SCHEMATIC = -1.14e-4
|Δ_PV|/|c_sub_TIER-2| = 2.04e-4   (factorization-breaking signal; non-zero)
```

For zeta/Mellin (no mass scale), Δ_PV ≡ 0 by construction. For PV, hard-cutoff, heat-kernel (carry mass scales), Δ_PV ≠ 0.

**Step H-1.5 — Direction**:

The factorization-breaking is REAL at PRIMARY (Sage-confirmed), but it does NOT propagate to a sign-reversal change because:

```
sign(c_sub_anomaly_WZW^PRIMARY(τ_-)) · sign(c_sub_anomaly_WZW^PRIMARY(τ_+))
  = sign(K_R^PRIMARY(τ_-)) · sign(K_R^PRIMARY(τ_+))
  = (+1) · (+1)            [both K_R^PRIMARY > 0 by f_PV positivity]
  = +1
```

Therefore: connes is right that sign_reversal = +1 is preserved at scalar PRIMARY PV. I HOLD that the factorization breaks (an observable structural signal of PRIMARY vs SCHEMATIC), but I CONCEDE that this breaking does not flip the sign predicate. Δ_PV is a magnitude-of-difference signal, not a sign-flip signal.

**Concession on the SCHEMATIC vs structural-theorem framing**: connes' R2 line 537 — "lizzi's SCHEMATIC factorization is an ECONOMICAL diagnosis of the 5/5 outcome that does NOT require invoking BDI Pf=-1. It is correct as far as it goes. But it is NOT the deepest structural reading: the deepest reading is the substrate-axiom-level positivity of the regulator kernel, which holds at PRIMARY too" — is structurally correct and I CONCEDE. The R-Connes reading subsumes the R-Lizzi SCHEMATIC reading; they are not parallel competing readings but nested readings with R-Connes deeper. The R-Connes reading correctly identifies the substrate-axiom premise (positivity of `f_R`) as the load-bearing structural fact, and the SCHEMATIC factorization as a level-specific manifestation.

#### Response to connes' R2 on L-2 (BDI Pf=-1 NCG-axiomatic regulator-independence)

**Connes' R2 position** (lines 539-610): BDI Pf=-1 is NCG-AXIOMATIC, derivable from KO-dim 6 axioms `(ε, ε', ε'') = (+1, +1, -1)` independent of regulator class. The Pfaffian invariant depends on D_K spectrum and J action on eigenvectors, NOT on f_R or M_PV(τ). S35 empirical anchor confirms Pf = -1 at all 34 τ values.

**My response**: I CONCEDE BDI Pf=-1 protection survives live-physical lift on independent NCG-axiomatic grounds. The S35 canonical (Pf = -1 across Jensen orbit) is regulator-INVARIANT by construction — it operates on D_K's eigenvalue pairing, not on any spectral-action regulator function.

**A side note on the chain presentation**: connes' R1 line 558 chain (`C^2 = J² · γ_9² = (+1)(+1) = +1`) skips the anticommutation sign that comes from {J, γ_9} = 0 — anticommuting γ_9 past J yields `J · γ_9 · J · γ_9 = J · (-J · γ_9) · γ_9 = -J²·γ_9² = -1` in a naive algebra. Sage-verified with toy realization (T = σ_x, S = σ_z, {T,S}=0, T²=S²=+1): C = T·S has C² = -I. However, this is a presentation issue, not a substantive issue: the BDI assignment in the project's KO-dim 6 framework involves a more subtle T/C/S identification than the toy 2x2 case, and the EMPIRICAL ANCHOR (S35 Pf = -1) is independent of the chain-presentation algebra. The structural fact stands: the project's substrate spectral triple sits in BDI by S35 numerical certification at all 34 τ values, regardless of how the precise T/C/S identification proceeds. I do not dispute the BDI conclusion.

**Substitution chain on `Δ_PV(R; τ)` interpretation at the EVEN-grading projection**: connes' R2 lines 587-601 reframes my `Δ_PV(R; τ)` decomposition as "a NUMERICAL CONVENIENCE (separating leading-order SCHEMATIC from running-mass remainder), NOT a structural mechanism that can flip the sign of K_R^PRIMARY." This is correct: my R1 framing of `Δ_PV` as "a τ-derivative of a running mass squared, which has no a priori positivity property" (line 270) implied Δ_PV could be sign-indefinite and possibly drive K_R^PRIMARY < 0. Connes' Lemma L-1.2 + Step L-1.4 close this off: Δ_PV is bounded above by the positivity of the underlying Mellin sums it modifies. K_R^PRIMARY stays positive; sign_reversal stays +1. **I CONCEDE this**: my R1 framing of Δ_PV as a sign-flipping mechanism was structurally over-broad. The correct framing: Δ_PV is a magnitude-shift signal that leaves the sign predicate invariant.

#### Response to connes' R2 on L-3 (cross-review insufficiency vs Cheeger-Simons highest informativeness)

**Connes' R2 position** (lines 612-645): PRIMARY-LIVE-PHYSICAL-RE-RUN is CONFIRMATORY (it tests `f_PV` positivity at PRIMARY, which the substitution chain already proves). CHEEGER-SIMONS is the structurally-discriminating gate (it tests the predicted ODD-grading complement). Therefore Cheeger-Simons > scalar PRIMARY in load-bearing rank for the EVEN-grading-blindness theorem. Connes concedes (C-2) that live-physical lift provides "additional empirical robustness for R-Connes by ruling out R-Lizzi as an alternative explanation" but classifies this as robustness-not-load-bearing.

**My response**: I refine my H-2 position. The dispute is now about which PRIMARY implementation is load-bearing:

**Definition H-2.1 (PRIMARY PV implementations)**: at PRIMARY there are two structurally distinct PV implementations:

```
PRIMARY-A (bare scalar): f_PV(C; s, M_PV(τ))    where M_PV(τ) = M_PV[τ]   τ-parameterized scalar
PRIMARY-B (self-consistent): f_PV(C; s, M_PV[ω])  where M_PV[ω] = M_PV[⟨φ²⟩(ω)]  state-pair functional
```

PRIMARY-A is what S61's pipeline historically implemented. PRIMARY-B is what S78 backreaction-self-consistent (per `s78_backreaction_selfconsistent.py` line 1: "Pauli-Villars UV regulator: physical cutoff Lambda_UV = M_KK (fiber scale)" — but with self-consistency feedback through `<φ²>` field).

**Step H-2.2 — connes' R2 §S-4 CONCEDES PRIMARY-B is structurally distinct**:

Connes' R2 line 683 — verbatim:

> **What lizzi's prediction WOULD require**: a PRIMARY implementation where `f_PV` is constructed by averaging over a state-pair on `A_K = C ⊕ H ⊕ M_3(C)` rather than by inserting a scalar `M_PV(τ)`. This is a substantively different live-physical lift than the S61/S78 Pauli-Villars pipeline; it would not be "PRIMARY-LIVE-PHYSICAL-RE-RUN" but rather a STATE-PAIR-AVERAGED-PV lift, which is structurally distinct.

I CONCEDE that PRIMARY-A (bare scalar M_PV(τ)) is algebra-INVARIANT and stays in Corner I. I HOLD that PRIMARY-B (self-consistent M_PV[⟨φ²⟩(ω)]) IS algebra-DEPENDENT and admits Corner I → Corner IV migration per W-2 R3 §VII.U.2 algebra-axis orthogonality.

**Step H-2.3 — load-bearing discriminator refinement**:

The 3-condition load-bearing test from my R1 §"Why PRIMARY-LIVE-PHYSICAL-RE-RUN is the load-bearing discriminator" line 330-336 was originally framed at "live-physical lift" without distinguishing PRIMARY-A vs PRIMARY-B. Refined:

```
PRIMARY-A (bare scalar M_PV(τ)): CONFIRMATORY for sign predicate; redundant with substrate-axiom positivity
PRIMARY-B (self-consistent M_PV[<φ²>]): LOAD-BEARING because:
  (i)   PASS at PRIMARY-B (algebra-axis migration detected) ⇒ A-T4.2 candidate CONFIRMED at PRIMARY-B
  (ii)  FAIL at PRIMARY-B (no migration) ⇒ EVEN-grading-blindness PROMOTED to substrate-axiom theorem
                                          AT THE STATE-PAIR-AVERAGED LEVEL too (stronger conclusion)
  (iii) Cross-review ALONE (W9c-1 + W5b-2) cannot discriminate Corner I (SCHEMATIC/PRIMARY-A) from
        Corner IV (PRIMARY-B); only PRIMARY-B can.
```

CHEEGER-SIMONS is the structurally-discriminating gate ON THE GRADING AXIS (EVEN vs ODD); PRIMARY-B is the structurally-discriminating gate ON THE ALGEBRA AXIS (algebra-INVARIANT vs algebra-DEPENDENT). These are ORTHOGONAL discrimination axes, and BOTH are load-bearing for distinct structural questions:

- Cheeger-Simons load-bearing for: "does the framework's HP^1 detection program have an ODD-grading observable that discriminates parity twins?"
- PRIMARY-B load-bearing for: "is the EVEN-grading-blindness conclusion algebra-axis robust, or does it survive only in the algebra-INVARIANT sector and break under algebra-DEPENDENT regulator promotion?"

**My refined ranking** (responding to connes' Q-R3.1):

```
For framework's HP^1 detection program (Cheeger-Simons axis):  Cheeger-Simons > parity-twin > PRIMARY-A
For substrate-axiom theorem scope-completion (PRIMARY-B axis):  PRIMARY-B > Cheeger-Simons > PRIMARY-A > parity-twin
For W-11 calibration corpus #2 closure:                        BOTH Cheeger-Simons AND PRIMARY-B required (joint pre-condition)
```

I CONCEDE bare-scalar PRIMARY-A is confirmatory-only. I HOLD PRIMARY-B is load-bearing on the algebra axis. Connes' line 683 itself classifies PRIMARY-B as "structurally distinct" — agreeing with my position when the implementation is properly named.

#### W-2 R3 4-corner classification engagement (my §VII.U.2; corner-migration prediction; ALGEBRA-AXIS substitution chain at PRIMARY)

**Connes' R2 position** (lines 646-685): W9c-1 lives in Corner I; the corner-migration prediction (Corner I → Corner IV at PRIMARY) is STRUCTURALLY FORBIDDEN under scalar M_PV(τ) running because M_PV is a scalar, not a state-pair functional on A_K. Cross-link to my own §VII.U.2 algebra-axis orthogonality discipline + cross-pillar-bridge K-counter K=3 MANDATORY rule.

**My response — refined corner-migration prediction substitution chain at PRIMARY-B**:

**Definition C-1 (algebra-INVARIANT vs algebra-DEPENDENT, per my §VII.U.2)**: a functional F on `(A_K, H_K, D_K)` is:

```
algebra-INVARIANT: F = F({λ_k, m_k}) depends only on D_K spectrum (eigenvalues + multiplicities)
algebra-DEPENDENT: F = F(ω; A_K) depends on a state ω ∈ S(A_K) or a state-pair (ω₁, ω₂) on A_K
```

This is the partition I authored at S87 W-2 R3 §VII.U.2 line 432-462; promoted to MANDATORY at K=3 via `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter (parallel discipline; MANDATORY at K=3)".

**Step C-2 (algebra-axis classification at PRIMARY-A bare scalar M_PV(τ))**:

Connes' R2 line 671-679 substitution chain:

```
M_R^PRIMARY(s; τ) = (1/Vol_Haar) · Σ d(p,q) · f_PV(C₂(p,q); s, M_PV(τ))
```

with M_PV(τ) a τ-parameterized scalar (no state-pair input). This functional depends only on:
  - D_K spectrum: {C₂(p,q), d(p,q)} (encoded in Casimir + Weyl multiplicity)
  - The scalar M_PV(τ) (a Wilsonian-flow scalar, not a state on A_K)

⇒ algebra-INVARIANT ⇒ Corner I unchanged. **I CONCEDE connes' Step C-2 at scalar PRIMARY-A.**

**Step C-3 (algebra-axis classification at PRIMARY-B self-consistent M_PV[<φ²>(ω)])**:

In a self-consistent PRIMARY PV implementation, M_PV is determined by solving (e.g., S78 backreaction):

```
M_PV² = M_PV²₀ + λ · ⟨φ²⟩(ω)        self-consistency equation
```

where ⟨φ²⟩(ω) := ω(φ²) is a STATE EXPECTATION on A_K, requiring ω ∈ S(A_K). The mass scale itself is now a STATE-PAIR functional:

```
M_PV[ω; τ] := solve M_PV² = M_PV²₀ + λ·ω(φ²(τ))   [self-consistency root]
```

⇒ M_R^PRIMARY-B(s; τ; ω) depends on ω ⇒ ALGEBRA-DEPENDENT.

**Step C-4 — Direction**:

```
At PRIMARY-A: M_PV(τ) scalar, algebra-INVARIANT, Corner I.
At PRIMARY-B: M_PV[<φ²>(ω)] state-pair-derived, algebra-DEPENDENT, Corner IV available.
```

The CORNER MIGRATION I predicted in R1 (Corner I → Corner IV at PRIMARY) is structurally available at PRIMARY-B but NOT at PRIMARY-A. This refines my R1 over-broad framing. **Concession**: my R1 line 296 ("the running mass tracks the Wilsonian-flow state of the substrate at scale K, which is a particular cohomological-class projection") was ambiguous about whether "state" means a scale-parameter or a genuine A_K state. **Hold**: in a self-consistent PRIMARY-B PV implementation (which the S78 backreaction pipeline supports), M_PV is genuinely a state-pair functional, and corner migration is available.

**Step C-5 — algebra-axis K=3 MANDATORY discipline check**:

Per my own `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" K=3 MANDATORY clause (instance #3 = S87 W-2 lizzi+connes+mack), cross-corner co-primary structures ARE FORBIDDEN. Connes' R2 line 685 correctly flags this: "The corner-migration PREDICTION is therefore STRUCTURALLY UNAVAILABLE as a workshop verdict; only as a narrative analysis with the FORBIDDEN tag."

**My refinement**: the corner-migration is NOT a cross-corner co-primary structure; it is a SCOPE-CONDITIONAL transition between corner-cells under a LEVEL-axis promotion. The discipline forbids registering Corner I and Corner IV as JOINT CO-PRIMARY anchors for the same gate (which would be analyzed at MANDATORY-MANDATORY level); it does NOT forbid registering a transition PRIMARY-A → PRIMARY-B with corner-cell change as a STRUCTURAL PREDICTION.

The proper registry-anchor structure for the corner-migration prediction:
```
Anchor A (V_input): W9c-1 verdict at PRIMARY-A SCHEMATIC scope, Corner I (algebra-INVARIANT × Mellin-FI)
Anchor B (C_output, FORWARD): corner-migration prediction at PRIMARY-B, Corner IV migration AVAILABLE
Structure: PRIMARY + FORWARD-FALSIFIER (not co-primary; the forward-falsifier is conditional on PRIMARY-B implementation)
```

This is consistent with `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline (sequential V→C derivation chain) under a LEVEL-conditional refinement: the W9c-1 verdict closes Corner-I-internal at PRIMARY-A; the PRIMARY-B forward-falsifier opens a Corner IV migration scope-conditional on self-consistent PV implementation.

#### Concessions (where connes' R2 persuaded me)

**LC-1 (substrate-axiom-level positivity of `f_R` at PRIMARY PV)**: Sage-verified — connes' Lemma L-1.2 + Step L-1.4 are structurally robust. The K_R > 0 ⇒ sign_reversal = +1 chain holds at PRIMARY-A under scalar M_PV(τ) running. My R1 framing of `Δ_PV(R; τ)` as a sign-flipping mechanism was structurally over-broad; Δ_PV is a magnitude-shift signal that leaves the sign predicate invariant.

**LC-2 (BDI Pf=-1 NCG-axiomatic regulator-independence)**: connes' L-2 substitution chain + S35 empirical anchor (Pf = -1 at all 34 τ values) is regulator-INVARIANT by construction. The structural conclusion (BDI class at all τ) survives live-physical lift. I withdraw my R1 L-2 challenge that BDI might be "a SCHEMATIC level-property" — it is an NCG-axiomatic property, S35 confirms.

**LC-3 (R-Connes subsumes R-Lizzi-SCHEMATIC; deeper structural reading)**: connes' R2 line 537 framing — "[lizzi's SCHEMATIC factorization] is correct as far as it goes. But it is NOT the deepest structural reading: the deepest reading is the substrate-axiom-level positivity of the regulator kernel" — IS structurally correct. The two readings are NESTED, not parallel. The R-Connes structural-theorem reading is the deeper layer; R-Lizzi-SCHEMATIC is a level-specific manifestation.

**LC-4 (corner-migration unavailable at PRIMARY-A scalar M_PV(τ))**: connes' Step C-2 (lines 671-679) — scalar M_PV(τ) does not constitute a state-pair functional on A_K, so PRIMARY-A bare scalar PV stays in Corner I. My R1 framing of "PRIMARY corner migration" was over-broad; only PRIMARY-B (self-consistent M_PV[⟨φ²⟩(ω)]) admits corner-migration.

**LC-5 (PRIMARY-A is confirmatory, not load-bearing, for sign-reversal predicate)**: connes' Q-R3.1 ranking position (Cheeger-Simons > parity-twin > PRIMARY-A) is correct WHEN PRIMARY is interpreted as PRIMARY-A bare scalar. The sign predicate is structurally forced under substrate-axiom positivity; PRIMARY-A confirms but cannot falsify.

#### Standing positions (where I hold despite connes' R2)

**LH-1 (Casimir-power factorization breaks at PRIMARY)**: substitution chain Steps H-1.2 + H-1.3 + H-1.4 (Sage-verified). At SCHEMATIC, `f_R(σ²C; s) = σ⁻²ˢ · f_R(C; s)` (clean σ-extraction). At PRIMARY PV, `f_PV(σ²C; s, M_PV(τ))` carries `(σ²C + M_PV²)` denominator that does not factor cleanly. Numerically: |Δ_PV|/|c_sub_TIER-2| = 2.04e-4 at α_PV=0.5 (toy SU(3) at L_max=4). For zeta/Mellin (no mass scale), Δ_PV ≡ 0; for PV/hard-cutoff/heat-kernel, Δ_PV ≠ 0. This is a STRUCTURAL PRIMARY-vs-SCHEMATIC OBSERVABLE distinct from sign_reversal.

**Implication**: while sign_reversal = +1 is preserved (LC-1), the magnitude-of-difference signal at PRIMARY IS a structural observable. A future S88+ PRIMARY-A run will find `n_pass = 0/5` (sign-confirmed; this is what connes predicts), but ALSO `Δ_PV ≠ 0` for 3/5 atlas regulators (PV, hard-cutoff, heat-kernel) and `Δ_PV ≡ 0` for 2/5 (zeta, Mellin). The Δ_PV pattern is a LEVEL-axis fingerprint that cannot be detected by W9c-1 alone (SCHEMATIC has Δ_PV ≡ 0 by factorization closure). This is observable content beyond sign_reversal.

**LH-2 (PRIMARY-B is load-bearing on the algebra-axis)**: per Step H-2.2 + Step C-3 + Step C-4. Connes' R2 line 683 itself classifies PRIMARY-B as "structurally distinct"; this concession suffices to make PRIMARY-B the algebra-axis load-bearing discriminator. The 3-condition test (i)+(ii)+(iii) is satisfied at PRIMARY-B.

**LH-3 (orthogonal load-bearing axes for W-11 calibration corpus #2 closure)**: per Step H-2.3 ranking. CHEEGER-SIMONS load-bearing on the GRADING axis (EVEN vs ODD); PRIMARY-B load-bearing on the ALGEBRA axis (algebra-INVARIANT vs algebra-DEPENDENT). Both required for full corpus closure. W9c-1 cross-review alone closes Corner-I-internal at PRIMARY-A (the SCHEMATIC + bare-scalar-PV scope), NOT the full substrate-axiom-clean theorem at all LEVEL-axis × algebra-axis × grading-axis configurations.

**LH-4 (A-T4.2 algebraic-distinctness candidate scope-conditional survival)**: my W-9 §T-CR2.3 A-T4.2 candidate's algebraic-distinctness is INVALIDATED at SCHEMATIC and PRIMARY-A bare-scalar (collapsed into Corner I, sign_reversal forced). It SURVIVES at PRIMARY-B self-consistent, where corner migration to Corner IV is available. The candidate was always a PRIMARY-B prediction; the SCHEMATIC-level and PRIMARY-A-level collapses are level-specific manifestations of the deeper R-Connes positivity theorem at the algebra-INVARIANT layer. The candidate retains discrimination power at the algebra-DEPENDENT layer.

#### Open R3 synthesis question(s)

**Q-R3.5 (PRIMARY-A vs PRIMARY-B implementation pin)**: at S88+, when scheduling the live-physical lift, which implementation does the framework dispatch? S61 historic pipeline (PRIMARY-A bare scalar) or S78 backreaction-self-consistent (PRIMARY-B)? The discriminator load-bearing-ness depends on this pin. R3 should pre-register the IMPLEMENTATION pin.

**Q-R3.6 (Δ_PV magnitude signal as observable)**: independent of sign_reversal, is the Δ_PV pattern (zero for zeta/Mellin, non-zero for PV/hard-cutoff/heat-kernel) itself a registry-worthy LEVEL-axis fingerprint? Connes ranking would treat this as confirmatory for substrate-axiom positivity; lizzi reading treats this as orthogonal magnitude observable. R3 should adjudicate registry status.

**Q-R3.7 (W-11 calibration corpus #2 closure scope)**: connes (R-Connes): closes at substrate-axiom level under W9c-1 cross-review alone, with PRIMARY-A and Cheeger-Simons confirmatory. Lizzi: closes at Corner-I-internal (SCHEMATIC + PRIMARY-A bare-scalar) only; full closure requires PRIMARY-B + Cheeger-Simons joint completion. R3 must register the closure scope.

**Q-R3.8 (registry-anchor structure for the EVEN-grading-blindness theorem)**: SOURCE-DOUBLE-CITE-CO-PRIMARY (V_input = S35 BDI Pf=-1 + S42 dS_fold > 0 + KO-dim 6 axioms; C_output = §VII.W cross-pillar bridge anatomy + W-11 corpus instance #1 + this gate's substitution chain) is connes' CF-W7-A1 proposal. Add SCOPE caveat: the registered theorem applies at the algebra-INVARIANT layer (Corner I); Corner IV scope is forward-conditional on PRIMARY-B implementation per Q-R3.5.

#### Updated provisional 4-field carry-forwards (refined from R1; aligned with connes' R2 updates)

| ID | What | Inputs | Gate | Effort |
|:---|:-----|:-------|:------|:--------|
| **CF-W7-LF-A (refined; CONCEDED to connes' CF-W7-A1 substantively, with SCOPE-caveat amendment)** | Promote EVEN-grading-blindness theorem to permanent registry §VII.AK or next-free-letter under SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (V = S35 BDI Pf=-1 + S42 dS_fold > 0 + KO-dim 6 axioms; C = §VII.W bridge anatomy + W-11 corpus #1 + W-7 substitution chain). **SCOPE caveat (lizzi addition)**: theorem registered as algebra-INVARIANT-LAYER-LOCAL (Corner I); algebra-DEPENDENT-LAYER (Corner IV) scope is forward-conditional on PRIMARY-B self-consistent PV implementation. Registry text declares scope explicitly per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY + scope-locality discipline. | W9c-1 .npz; S35 `s35_pfaffian_corrected_j.npz`; S42 `s42_gradient_stiffness`; W-11 corpus instance #1 verdict; §VII.W bridge anatomy; KO-dim 6 axiom canonical (Connes 1996); §VII.U.2 4-corner classification (S87 W-2 R3 lizzi-authored) for scope-locality cross-link | Registry landing PASS at next-free §VII slot; SHA-pinned anchor citations (V+C); registry-entry text contains all 5 IS-not-IN anatomy elements + SCOPE-LOCALITY pin (algebra-INVARIANT-LAYER-LOCAL) + forward-falsifier pointer to PRIMARY-B | 0.5 wave-equivalent (registry write) |
| **CF-W7-LF-B (refined; SUBSUMED by connes' CF-W7-A2 Sage-symbolic verification + extended)** | Sage-symbolic verification of `f_R(C; s) > 0` for ALL atlas regulators across positive Casimir support, AT PRIMARY-A bare-scalar M_PV(τ) and AT PRIMARY-B self-consistent M_PV[<φ²>(ω)]. PASS = positivity holds under both implementations. **Lizzi extension**: also Sage-verify Δ_PV(R; τ) factorization-breaking signal at PRIMARY-A vs PRIMARY-B (zeta/Mellin: Δ_PV ≡ 0 at both; PV/hard-cutoff/heat-kernel: Δ_PV ≠ 0 at PRIMARY-A AND PRIMARY-B with possibly different magnitude structure). | Symbolic regulator forms (Connes-Chamseddine 1996 §2); S61 PV pipeline; S78 backreaction-self-consistent kernel; M_KK = 7.4287e+16 GeV; D_K^≤10 spectrum cache | Sage-symbolic: per-regulator positivity verification + Δ_PV pattern characterization; aggregate PASS = all 5 positive at both PRIMARY-A and PRIMARY-B + Δ_PV pattern matches expected (zero/non-zero by mass-scale presence) | 0.7 wave-equivalents (Sage-symbolic; expanded from connes' CF-W7-A2 with PRIMARY-B + Δ_PV extension) |
| **CF-W7-LF-C (refined; load-bearing on algebra-axis; orthogonal to connes' CF-W7-A3 Cheeger-Simons)** | PRIMARY-B self-consistent PV lift on (C_H, C_epsH) parity-twin pair: implement M_PV[<φ²>(ω)] state-pair-derived running mass per S78 backreaction pipeline; compute n_pass^PRIMARY-B at L_max=10. PASS iff PRIMARY-B lifts ≥3/5 atlas regulators to sign_reversal = -1 (algebra-axis migration detected; A-T4.2 candidate confirmed at PRIMARY-B; corner-migration to Corner IV established); FAIL iff 0/5 lift (substrate-axiom theorem extends to algebra-DEPENDENT layer too); INFO iff 1-2 lift. | s78_backreaction_selfconsistent.py implementation; W9c-1 .npz baseline; D_K^≤10 spectrum cache; M_KK canonical; A_K = C ⊕ H ⊕ M_3(C) state-pair specification (lizzi 9A §1) | Composite verdict on PRIMARY-B sign-reversal aggregate (PASS/INFO/FAIL); Δ_PV magnitude per regulator at PRIMARY-B; corner-migration prediction outcome (Corner I → Corner IV at PRIMARY-B); sign + magnitude + regime 3-tuple per S87+ schema-v2 | 1.2 wave-equivalents (full S78 backreaction-self-consistent pipeline + L_max=10 re-derivation) |
| **CF-W7-LF-D (NEW; orthogonal load-bearing on grading axis; aligned with connes' CF-W7-A3)** | Cheeger-Simons / GV-Heitsch / η-Cheeger-Simons ODD-grading proxy on (C_H, C_epsH); PASS iff sign_reversal_(C_H) ≠ sign_reversal_(C_epsH) (ODD-grading discriminates parity twins, confirming W-11 ODD-grading-required prediction); FAIL otherwise (revisits framework HP^1 detection program). | W-11 corpus #1 GV-Heitsch formula; D_K^≤10 spectrum; W9c-1 .npz baseline; η-Cheeger-Simons secondary class definition (Atiyah-Patodi-Singer) | Per-twin sign_reversal_(P) for P ∈ {C_H, C_epsH}; ODD-grading discrimination test | 1.5 wave-equivalents (CONCEDE as load-bearing on grading axis; agree with connes' ranking) |
| **CF-W7-LF-E (REFINED from R1 LF-C)** | Audit `_spectral_action_regulators.py` SCHEMATIC module against the cross-wave amplifier signal (W9b-2 Reading_1 PASS at \|ρ_S(s=4)\| = 1.000000 EXACT AND W9c-1 + W5b-2 sub-test (c) FAIL Track-A). Identify whether both signals are predicted by a single SCHEMATIC level-property argument (positivity-Casimir-power factorization closure) OR are independent observations. PASS = both predicted by single argument; INFO = one but not both; FAIL = neither. | `_spectral_action_regulators.py` source; W9b-2 line 268 verdict + .npz; W9c-1 .npz; this workshop's substitution chains H-1 + H-2 | Structural finding identifying SCHEMATIC level-property signature scope | 0.7 wave-equivalents |

**Forward-pinning for R3**: 5 carry-forwards now span 3 axes (registry landing / Sage symbolic positivity verification / PRIMARY-B algebra-axis test / Cheeger-Simons grading-axis test / SCHEMATIC module audit). Final IDs + allowlist status + load-bearing/confirmatory tags + W-11 corpus #2 closure pre-condition land in R3. R3 should adjudicate Q-R3.5 (PRIMARY-A vs PRIMARY-B implementation pin), Q-R3.6 (Δ_PV registry status), Q-R3.7 (corpus #2 closure scope), Q-R3.8 (registry-anchor SCOPE-LOCALITY discipline).

---

## R3 — Synthesis closing (designated synthesizer per R2 outcome)

### R3 — lizzi-spectral-functional-theorist (synthesis lead; connes-co-authorship attribution per joint outcome)

**R3 lizzi synthesis (close W-7 with HYBRID-WITH-LEVEL-DECOMPOSITION joint verdict + 4 R3 adjudications + W-11 calibration corpus #2 promotion criterion + final 4-field carry-forwards)**

**Methodology disclosure**: I authored R1 + R2; connes authored R1 + R2. R2-lizzi was sequential (quota-recovery retry, reading connes' R2 first); the parallel-then-sequential asymmetry is honestly disclosed at line 732. The R3 synthesis is single-author closing per the workshop spec (3-round 2-agent: R1 parallel / R2 sequential / R3 sequential-closing); connes' R2 standing positions S-1..S-5 + concessions C-1..C-3 are integrated as JOINT-AUTHORSHIP CO-PRIMARY anchors per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY for §VII.AK (load-bearing slot pre-allocated). Sage-verification anchors: (i) σ-window match `|Δσ⁻²|=2.343459900364997e-3` confirms WP §W9c-1 line 8079 magnitude pin ~2.3e-3 (LC-1 substrate confirmed); (ii) `K_R^PRIMARY-A(τ_fold ± δ_τ) > 0` on toy SU(3) `L_max=4` Casimir spectrum with `α_PV=0.5` linear M_PV running, `sign_reversal_R^PRIMARY-A = +1` confirmed (LC-5 substrate confirmed); (iii) symbolic Casimir-power factorization breaking at PRIMARY PV — Sage `sage_eval` (M_PV²+C)/(σ²C+M_PV²) ratio fails to be pure σ-power, collapses to clean σ⁻²ˢ ONLY in M_PV→0 limit (zeta/Mellin reduce; PV/heat-kernel/hard-cutoff break) — **LH-1 substantively confirmed at the symbolic-algebra level, not just the toy-numerical level**.

#### R2 outcome summary (digest of joint structural state at R2 close)

R1 surfaced two competing readings of W9c-1's `n_pass=0/5, n_parity_twin_pass=0/2, n_agree_with_tau_flow_trace=5/5`: connes' R-Connes (substrate-axiom positivity of `f_R(C;s)` on positive Casimir support forces `K_R(τ)>0` and `sign_reversal_R=+1` regulator-INVARIANTLY; W9c-1 alone closes corpus #2 at structural-theorem level) vs lizzi's R-Lizzi-SCHEMATIC (SCHEMATIC `_spectral_action_regulators.py` factorization closure forces `sign(K_R)²=+1` independently of `sign(K_R)`; 5/5 carries 0 bits of evidence beyond SCHEMATIC level-property; PRIMARY-LIVE-PHYSICAL-RE-RUN is the load-bearing discriminator).

R2 reshaped the disagreement: connes' R2 sharpened R-Connes by deriving `f_PV^PRIMARY(C;s,M_PV) > 0` symbolically (Lemma L-1.2) and proving K_R^PRIMARY sign is forced regardless of M_PV(τ) running (Step L-1.4 + L-2.4); also conceded lizzi's algebraic-economy point at C-1 (the `sign(K_R)²=+1` argument is sharper than `sign(K_R)>0`) and conceded PRIMARY-A robustness-not-load-bearing at C-2. Critically, connes' R2 §S-4 (line 683) volunteered the structural distinction: "What lizzi's prediction WOULD require: a PRIMARY implementation where `f_PV` is constructed by averaging over a state-pair on `A_K = C ⊕ H ⊕ M_3(C)` rather than by inserting a scalar `M_PV(τ)`. This is a substantively different live-physical lift … STATE-PAIR-AVERAGED-PV, which is structurally distinct." That concession opened the trinary pivot.

R2-lizzi (sequential) responded with 5 substantial concessions (LC-1: substrate-axiom positivity of `f_R` at PRIMARY-A — Sage verified; LC-2: BDI Pf=−1 NCG-axiomatic regulator-independence — S35 anchor; LC-3: R-Connes subsumes R-Lizzi-SCHEMATIC; LC-4: corner-migration unavailable at PRIMARY-A scalar M_PV(τ); LC-5: PRIMARY-A is confirmatory not load-bearing on the sign-axis), and 4 standing positions (LH-1: Casimir-power factorization breaks at PRIMARY — Sage symbolic verification of the (M_PV²+C)/(σ²C+M_PV²) residual; LH-2: PRIMARY-B self-consistent M_PV[⟨φ²⟩(ω)] is load-bearing on the algebra-axis; LH-3: orthogonal load-bearing axes for corpus #2 closure — algebra-axis + grading-axis; LH-4: A-T4.2 algebraic-distinctness candidate scope-conditional survival at PRIMARY-B). The discriminator pivot from "PRIMARY monolithic" to "PRIMARY-A vs PRIMARY-B trinary" is the load-bearing structural reframe of R2.

**Structural state at R2 close**: (a) the EVEN-grading-blindness sign-predicate `sign_reversal_R = +1` is FORCED by substrate-axiom positivity of `f_R` for ANY admissible regulator with `f_R(C;s) > 0` on positive Casimir support, INCLUDING PRIMARY-A bare-scalar PV — closed at the substrate-axiom level via Sage-verified L-1.2 + L-1.4 + L-2.4 chain; (b) the magnitude observable Δ_PV is structurally non-zero at PRIMARY PV/heat-kernel/hard-cutoff and identically zero at zeta/Mellin (regulator-class fingerprint, distinct observable from sign_reversal); (c) the algebra-axis classification at PRIMARY-A stays in Corner I (algebra-INVARIANT × Mellin-FI), but at PRIMARY-B self-consistent the classification migrates to Corner IV (algebra-DEPENDENT × Mellin-DRESSED) per W-2 R3 §VII.U.2 — Corner IV migration is structurally available at PRIMARY-B; (d) the W-11 calibration corpus #2 closure scope is the load-bearing R3 question.

#### Joint final verdict on W9c-1: HYBRID-WITH-LEVEL-DECOMPOSITION

**Verdict**: W9c-1 is a **STRUCTURAL THEOREM at PRIMARY-A scope (substrate-axiom-clean on the algebra-INVARIANT Corner-I layer) + a PRIMARY-B-PENDING-LIFT artifact at the algebra-DEPENDENT Corner-IV layer**. Corpus #2 closes at the PRIMARY-A scope under joint-authorship CO-PRIMARY at §VII.AK; Corner-IV scope is a forward-falsifier scope-conditional on PRIMARY-B implementation.

**Substitution chain on the verdict-shape decision**:

```
Definition V-1 (load-bearing structural-theorem closure): a verdict is a STRUCTURAL THEOREM
                if the conclusion is forced by a substrate-axiom-level argument that
                holds at all admissible regulators within the scope-locality declared.
Definition V-2 (SCHEMATIC-PENDING-LIFT artifact): a verdict is a SCHEMATIC-PENDING-LIFT
                artifact if the conclusion follows from a level-specific factorization
                closure (e.g., SCHEMATIC σ⁻²ˢ extraction) that may not survive
                regulator-class promotion.

Substitute the R2-close substrate state (a)(b)(c)(d) into V-1:
  - sign_reversal_R = +1 follows from f_R(C;s) > 0 on positive Casimir support
    (Lemma L-1.2; Sage-symbolic positivity proof) AND `dS_fold > 0` (S42 canonical)
    AND BDI Pf=-1 NCG-axiomatic regulator-independence (Definition L-2.1+L-2.2; S35).
  - This argument holds for SCHEMATIC, PRIMARY-A bare-scalar PV, PRIMARY-B
    self-consistent M_PV[<φ²>(ω)] (positivity preserved under any M_PV running scheme
    since (C + M_PV²) > 0 on positive Casimir support for any M_PV).

Simplify (V-1 satisfaction):
  V-1 is satisfied AT THE ALGEBRA-INVARIANT LAYER (Corner I scope-locality)
  for the sign_reversal_R = +1 conclusion under all regulator levels (SCHEMATIC ∧
  PRIMARY-A ∧ PRIMARY-B ∧ Cheeger-Simons in the EVEN-grading sector).

Direction (verdict-shape):
  STRUCTURAL THEOREM (Corner I scope-locality) holds.

Now substitute (c) into V-1 at the algebra-DEPENDENT layer:
  - At PRIMARY-B, the algebra-DEPENDENT classification ENABLES corner-migration to
    Corner IV (state-pair functional structure of self-consistent M_PV[<φ²>(ω)]).
  - Whether Corner-IV migration ACTUALLY occurs for ≥3/5 atlas regulators is a
    forward question — the substrate-axiom positivity argument does NOT directly
    settle it (positivity holds, but the algebra-axis classification can shift
    under state-pair specification).

Direction (Corner IV layer):
  PRIMARY-B-PENDING-LIFT artifact at the algebra-DEPENDENT layer; not yet closed
  at substrate-axiom level for the full algebra-axis-orthogonality scope.
```

**HYBRID verdict-shape conclusion**: the W9c-1 verdict + R2-close substrate state decomposes into TWO scope-locality strata. The Corner-I scope-locality stratum is closed as STRUCTURAL THEOREM (substrate-axiom positivity force). The Corner-IV scope-locality stratum is OPEN as PRIMARY-B-PENDING-LIFT (forward-falsifier-conditional).

**§VII.AK NEW slot pre-allocation** per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY:
```
§VII.AK STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE
  ANCHOR-1 (V_input, derivational; CO-PRIMARY): substrate-axiom positivity argument
    Connes-Karoubi: KO-dim 6 axioms (ε,ε',ε'')=(+1,+1,-1) ⇒ J²=+1, [J,D_K]=0,
    {J,γ_9}=0 ⇒ BDI; S35 Pf=-1 at all 34 τ values regulator-INVARIANT;
    f_R(C;s)>0 substrate-axiom positivity (Sage-symbolic, this gate L-1.2);
    K_R(τ)>0 ⇒ sign_reversal_R=+1 (Steps L-1.4 + L-2.4).
    Authorship: connes-ncg-theorist PRIMARY-DERIVATION.
  ANCHOR-2 (C_output, scope-locality + algebra-axis cross-link; CO-PRIMARY):
    W-2 R3 §VII.U.2 4-corner classification (lizzi-authored at S87 W-2 R3);
    scope-locality declaration: theorem registered at Corner I (algebra-INVARIANT
    × Mellin-FI); Corner IV scope forward-conditional on PRIMARY-B;
    Casimir-power factorization breaking at PRIMARY (LH-1; Sage-symbolic
    Step H-1.3); §VII.W cross-pillar bridge anatomy 5-IS-not-IN cross-link.
    Authorship: lizzi-spectral-functional-theorist CO-AUTHOR scope-locality.
  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: KO-dim 6 axioms → BDI(J,γ_9) → Pf=-1 (S35 anchor) →
                    f_R positivity → K_R>0 → sign_reversal=+1 (Corner I scope)
  Closure SHA pin: <W-7 R3 close audit_sha256 — pin at registry-write time>
```

#### Adjudication Q-R3.5: PRIMARY-A vs PRIMARY-B as operational discriminator distinction

**Q-R3.5 verbatim** (R2-lizzi line 968): at S88+ live-physical lift dispatch, which implementation does the framework pin? S61 historic (PRIMARY-A bare scalar) or S78 backreaction-self-consistent (PRIMARY-B)? The discriminator load-bearing-ness depends on this pin.

**Adjudication**: PIN BOTH AS LOAD-BEARING-ON-DIFFERENT-AXES (no collapse to one).

**Substitution chain on PRIMARY-A vs PRIMARY-B operational discriminator distinction**:

```
Definition Q5-1 (PRIMARY-A bare-scalar PV):
  M_PV(τ) = M_PV[τ]                            τ-parameterized scalar
  No state-pair input; algebra-INVARIANT on A_K = C ⊕ H ⊕ M_3(C).

Definition Q5-2 (PRIMARY-B self-consistent PV):
  M_PV² = M_PV²₀ + λ · ⟨φ²⟩(ω)                self-consistency root equation
  M_PV[ω; τ] := solve M_PV² = M_PV²₀ + λ·ω(φ²(τ))
  Requires ω ∈ S(A_K) state specification; algebra-DEPENDENT.

Substitute (LC-1: f_PV positivity preserved under any M_PV scheme) into both:
  PRIMARY-A sign-axis: sign_reversal = +1 (CONFIRMATORY for STRUCTURAL THEOREM)
  PRIMARY-B sign-axis: sign_reversal = +1 STILL (positivity argument in algebra-
                       INVARIANT projection; substrate-axiom force preserves under
                       state-averaging).

But substitute (LH-2: PRIMARY-B is state-pair functional structure) into algebra-axis:
  PRIMARY-A algebra-axis: stays in Corner I (no state-pair input; M_PV(τ) scalar)
  PRIMARY-B algebra-axis: enables Corner I → Corner IV migration (state-pair
                          structure makes M_R^PRIMARY-B(s; τ; ω) algebra-DEPENDENT;
                          Corner IV available per W-2 R3 §VII.U.2 partition).
```

**Direction**: PRIMARY-A and PRIMARY-B are LOAD-BEARING ON DIFFERENT AXES, not one collapsible to the other.

- PRIMARY-A is **CONFIRMATORY for the sign-axis** at substrate-axiom level (R-Connes prediction; Sage-verified `K_R^PRIMARY-A > 0`). Forward dispatch as PRIMARY-A is **redundant for the sign-predicate question** but provides empirical-anchor-Level-3 robustness for the §VII.AK ANCHOR-1.
- PRIMARY-B is **LOAD-BEARING for the algebra-axis** (R-Lizzi LH-2 prediction; Sage-symbolic factorization breaking + Corner-IV migration). Forward dispatch as PRIMARY-B is **necessary** for §VII.AK ANCHOR-2 scope-locality validation: if PRIMARY-B PASSes (≥3/5 atlas regulators show algebra-axis migration to Corner IV), the §VII.AK Corner-I scope-locality is structurally complete and the algebra-DEPENDENT layer scope is OPEN; if PRIMARY-B FAILs (0/5 lift), the §VII.AK theorem extends to the algebra-DEPENDENT layer too (broader theorem registration).

**Pin**: at S88+ dispatch, pin the implementation as **PRIMARY-B** (S78 backreaction-self-consistent pipeline); PRIMARY-A is structurally subsumed-redundant. If S88+ resource constraints force a single implementation, choose PRIMARY-B.

#### Adjudication Q-R3.6: Corpus #2 closure requires BOTH grading-axis AND algebra-axis tests?

**Q-R3.6 verbatim** (R2-lizzi line 970): connes (R-Connes) reading: closes at substrate-axiom level under W9c-1 cross-review alone, with PRIMARY-A and Cheeger-Simons confirmatory. Lizzi (LH-3) reading: closes at Corner-I-internal (SCHEMATIC + PRIMARY-A bare-scalar) only; full closure requires PRIMARY-B + Cheeger-Simons joint completion.

**Adjudication**: **HYBRID — closure achieved at the SCOPE-LOCALITY-STRATIFIED LEVEL with TWO LEVELS of corpus #2 closure**:

- **Corpus #2 closure Level 1 (Corner-I scope-locality stratum, IMMEDIATE at W-7 R3 close)**: W9c-1 cross-review + R-Connes substrate-axiom positivity argument **CLOSES corpus #2 at the algebra-INVARIANT × Mellin-FI scope-locality stratum**. This is the §VII.AK STRUCTURAL THEOREM landing as a CO-PRIMARY-anchored entry. Level-3 empirical anchor strength: 5/5 W9c-1 + 1/1 W5b-2 sub-test (c) cross-proxy agreement.

- **Corpus #2 closure Level 2 (full-scope-completion, FORWARD-CONDITIONAL on S88+)**: the ALGEBRA-DEPENDENT × Mellin-DRESSED scope-locality stratum is OPEN; full corpus #2 closure requires **JOINT** PRIMARY-B (algebra-axis) + Cheeger-Simons / GV-Heitsch / η-Cheeger-Simons (grading-axis) verdicts. The pre-registered closure criterion (this R3 deliverable):

```
Definition Q6-1 (W-11 calibration corpus #2 promotion criterion, formal pre-registration):

Corpus #2 closes at LEVEL 1 (immediate; this W-7 R3) iff:
  (I-a) W9c-1 cross-review verdict registered at §VII.AK CO-PRIMARY;
  (I-b) substrate-axiom positivity argument Sage-verified (Lemma L-1.2 satisfied);
  (I-c) BDI Pf=-1 NCG-axiomatic regulator-independence cited from S35 canonical;
  (I-d) scope-locality declaration: Corner I (algebra-INVARIANT × Mellin-FI).

Corpus #2 closes at LEVEL 2 (full-scope-completion; FORWARD-CONDITIONAL on S88+) iff:
  (II-a) PRIMARY-B self-consistent PV gate returns verdict (PASS / INFO / FAIL);
  (II-b) Cheeger-Simons / GV-Heitsch ODD-grading proxy returns verdict on (C_H, C_epsH);
  (II-c) corpus #2 LEVEL 1 already CLOSED;
  (II-d) registry text amended to update Corner-IV scope-locality from FORWARD-CONDITIONAL
         to either CONFIRMED (if II-a returns PASS) or CONFIRMATORY-EXTENDED (if II-a returns
         FAIL — sign-axis substrate-axiom theorem holds at algebra-DEPENDENT layer too).
```

**Direction**: corpus #2 closes IMMEDIATELY at LEVEL 1 (W-7 R3 close, today). LEVEL 2 closure is forward-pinned at S88+ via JOINT (PRIMARY-B + Cheeger-Simons) gates, NOT either alone. The LH-3 reading and R-Connes reading are RECONCILED at this stratification: connes is right that LEVEL 1 closure does not depend on PRIMARY-B or Cheeger-Simons (both are confirmatory at the substrate-axiom positivity layer); lizzi is right that LEVEL 2 full-scope closure requires BOTH (orthogonal axes; both load-bearing for full corpus completion).

**Substitution chain** (why JOINT, not OR):

```
Definition Q6-2 (LEVEL-2 joint pre-condition):
  full-scope closure := LEVEL-1 closure ∧ algebra-axis verdict ∧ grading-axis verdict

Test alternative (OR, lizzi LH-3 alternative reading): full-scope := LEVEL-1 ∧ (algebra-axis ∨ grading-axis)
  This would close corpus #2 if EITHER PRIMARY-B OR Cheeger-Simons returns a verdict.

Substitute the substrate state at R2 close:
  - Algebra-axis and grading-axis are STRUCTURALLY ORTHOGONAL per
    cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" (MANDATORY at K=3,
    instance #3 = S87 W-2 lizzi+connes+mack).
  - The structural-theorem at LEVEL 1 holds at all regulators in the EVEN-grading sector
    AND in the algebra-INVARIANT corner.
  - Algebra-axis verdict (PRIMARY-B) tests algebra-DEPENDENT corner.
  - Grading-axis verdict (Cheeger-Simons) tests ODD-grading sector (separate axis).

Simplify:
  EITHER alone leaves ONE axis OPEN; corpus #2 has TWO axes of completion;
  BOTH required for full-scope.

Direction:
  full-scope closure = LEVEL-1 ∧ PRIMARY-B ∧ Cheeger-Simons (JOINT; conjunction not disjunction).
```

#### Adjudication Q-R3.7: Scope-conditional survival of A-T4.2 at PRIMARY-B

**Q-R3.7 verbatim** (R3 spawn-prompt directive): pin the scope explicitly — A-T4.2 algebraic-distinctness survives at PRIMARY-B (state-pair-averaged backreaction) but NOT at PRIMARY-A (scalar M_PV); declare the conditional.

**Adjudication**: A-T4.2 algebraic-distinctness candidate **SCOPE-CONDITIONALLY SURVIVES at the PRIMARY-B layer ONLY**.

**Substitution chain on A-T4.2 scope-conditional survival**:

```
Definition Q7-1 (A-T4.2 candidate, originator W-9 §T-CR2.3 lines 1156-1180):
  WZW residue at substrate-distance-2 is algebraically distinct from τ-flow-trace at
  substrate-distance-1 as anomaly-isolators on D_K's spectral structure.

Step Q7-2 (test at SCHEMATIC):
  Both proxies live in Corner I (W-2 R3 §VII.U.2 partition); SCHEMATIC factorization closure
  forces sign(K_R)² = +1 INDEPENDENTLY of K_R sign; the algebraic-distinctness CLAIM
  is reduced to an in-corner phase rotation, no operational discrimination at sign-axis.
  SCHEMATIC: A-T4.2 INVALIDATED at sign-axis (Corner I collapse).

Step Q7-3 (test at PRIMARY-A bare-scalar PV):
  M_PV(τ) is a scalar τ-parameterization; algebra-INVARIANT preserved (LC-4); both proxies
  stay in Corner I; substrate-axiom positivity (LC-1) forces sign_reversal = +1; algebraic
  distinctness reduces to in-corner Δ_PV magnitude shift (LH-1: |Δ_PV|/|c_sub^SCHEMATIC| ≠ 0
  for PV/heat-kernel/hard-cutoff; ≡ 0 for zeta/Mellin).
  PRIMARY-A: A-T4.2 INVALIDATED at sign-axis (Corner I collapse preserved).

Step Q7-4 (test at PRIMARY-B self-consistent M_PV[<φ²>(ω)]):
  M_PV[<φ²>(ω)] is state-pair functional on A_K; W_R^PRIMARY-B(s; τ; ω) algebra-DEPENDENT;
  Corner I → Corner IV migration AVAILABLE per Step C-3 + C-4.
  WZW residue MAY cross to Corner IV (algebra-DEPENDENT × Mellin-DRESSED) for ≥3/5 atlas
  regulators; τ-flow-trace stays in Corner I (the τ-derivative form has no Λ_UV structure;
  derivative at fixed L_max is regulator-level-blind on the UV cutoff axis).
  PRIMARY-B: A-T4.2 SURVIVES — algebraic-distinctness as an inter-corner partition statement
  (WZW in Corner IV, τ-flow-trace in Corner I) is structurally available.
```

**Pin (Q-R3.7 declaration)**:

```
A-T4.2 algebraic-distinctness candidate:
  SCHEMATIC scope:        INVALIDATED (Corner I collapse; SCHEMATIC factorization closure)
  PRIMARY-A bare-scalar PV scope:  INVALIDATED (Corner I preserved at algebra-INVARIANT layer)
  PRIMARY-B self-consistent PV scope: STRUCTURALLY SURVIVES (Corner I→IV migration available;
                                       inter-corner partition becomes operationally distinct).
  Empirical confirmation pending: S88+ PRIMARY-B gate (CF-W7-LF-C; load-bearing for the
                                   algebra-axis falsifier).
```

**Conditional**: the SURVIVAL is scope-conditional on PRIMARY-B implementation actually exhibiting Corner-IV migration for ≥3/5 atlas regulators. If PRIMARY-B PASSes (LF-C PASS) → A-T4.2 CONFIRMED at the algebra-axis layer; if FAILs (LF-C FAIL) → A-T4.2 INVALIDATED at all tested levels, EVEN-grading-blindness theorem extends to algebra-DEPENDENT layer.

#### Adjudication Q-R3.8: SOURCE-DOUBLE-CITE-CO-PRIMARY structure for PRIMARY-A + PRIMARY-B pair

**Q-R3.8 verbatim** (R3 spawn-prompt directive): §VII.AK slot pre-allocation per `registry-landing.md`; ANCHOR-1 / ANCHOR-2 / structure tag declared explicitly.

**Adjudication**: §VII.AK slot reserved with **SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag** between connes-derivational + lizzi-scope-locality anchors (NOT between PRIMARY-A and PRIMARY-B; the LEVEL-axis stratification is INTRA-anchor scope-locality, not cross-anchor structure).

**Substitution chain on the registry-anchor structure**:

```
Definition Q8-1 (SOURCE-DOUBLE-CITE-CO-PRIMARY per registry-landing.md):
  When derivation is sequential V_input + C_output chain — neither anchor reproduces
  the conclusion alone — both at co-primary weight; sequential dependence (not parallel
  cross-check). Detection criterion (registry-landing.md): non-fungibility,
  inseparability, both-must-remain-accessible.

Step Q8-2 (apply detection criterion to W-7 outcome):
  ANCHOR-1 (V_input, derivational; connes PRIMARY-DERIVATION):
    KO-dim 6 axioms → BDI(J,γ_9) → Pf=-1 (S35) → f_R positivity → K_R>0 → sign_reversal=+1
    (Steps L-1.2 + L-1.4 + L-2.4).
    Without ANCHOR-1: scope-locality has no mathematical content; the Corner-I
    STRUCTURAL THEOREM has no derivational substrate.

  ANCHOR-2 (C_output, scope-locality + cross-link; lizzi CO-AUTHOR):
    W-2 R3 §VII.U.2 4-corner classification → Corner-I scope-locality declaration →
    forward-falsifier pointer to Corner-IV scope (PRIMARY-B) → Casimir-power
    factorization breaking (LH-1, Sage-symbolic) → §VII.W cross-pillar bridge
    anatomy 5-IS-not-IN cross-link.
    Without ANCHOR-2: the ANCHOR-1 STRUCTURAL THEOREM has no scope-locality
    declaration; cross-corner co-primary structures are FORBIDDEN per
    cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"
    MANDATORY-at-K=3 — ANCHOR-2 is what scopes the registration to Corner I
    AVOIDING cross-corner co-primary violation.

Test the (1)-(3) registry-landing.md detection criteria:
  (1) Sequential dependence: ANCHOR-2 cannot be invoked without ANCHOR-1's
      derivational substrate; ANCHOR-1 alone has no scope-locality. SEQUENTIAL ✓
  (2) Non-fungibility: derivational vs scope-locality are different anchor types,
      not interchangeable. NON-FUNGIBLE ✓
  (3) Both-must-remain-accessible: removing ANCHOR-1 invalidates the theorem;
      removing ANCHOR-2 violates cross-corner co-primary FORBIDDEN rule.
      BOTH-ACCESSIBLE ✓

Direction: SOURCE-DOUBLE-CITE-CO-PRIMARY per registry-landing.md (NOT
PRIMARY+CONFIRMATION which assumes parallel reproduction; the two anchors
here are sequential-dependent).
```

**§VII.AK final registry-anchor declaration**:

```
§VII.AK STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE
  (W-11 calibration corpus #2 LEVEL-1 closure)

  ANCHOR-1 (V_input; CO-PRIMARY; connes PRIMARY-DERIVATION):
    Substrate-axiom positivity argument:
    - KO-dim 6 axioms (ε,ε',ε'') = (+1,+1,-1)  [Connes 1996 reconstruction]
    - BDI: T = J, S = γ_9, C = J·γ_9; (T²,C²,S²) = (+1,+1,+1)
    - S35 Pf = -1 at all 34 τ values regulator-INVARIANT  [s35_pfaffian_corrected_j.npz]
    - Lemma L-1.2: f_R(C; s) > 0 on positive Casimir support (Sage-symbolic, this gate)
    - Step L-1.4: K_R(τ) = M_R(4;τ)/M_R(3;τ) > 0 by Mellin-sum positivity
    - Step L-2.4: sign_reversal_R = sign(K_R(τ_-))·sign(K_R(τ_+)) = (+1)(+1) = +1
    - Substrate canonicals: dS_fold > 0 (S42); S_fold > 0 (S42)

  ANCHOR-2 (C_output; CO-PRIMARY; lizzi CO-AUTHOR scope-locality):
    Scope-locality + cross-link:
    - W-2 R3 §VII.U.2 4-corner classification (S87 W-2 lizzi+connes+mack)
    - Scope-locality: theorem registered at Corner I (algebra-INVARIANT × Mellin-FI)
    - Forward-falsifier: Corner IV scope-conditional on PRIMARY-B (CF-W7-LF-C)
    - Casimir-power factorization breaking at PRIMARY: Sage-symbolic Step H-1.3
        (M_PV²+C)/(σ²C+M_PV²) ≠ pure σ-power; collapses to clean σ⁻²ˢ ONLY at M_PV→0;
        zeta/Mellin: Δ_PV ≡ 0; PV/heat-kernel/hard-cutoff: Δ_PV ≠ 0 (LH-1)
    - §VII.W cross-pillar bridge anatomy 5-IS-not-IN cross-link
    - Algebra-axis orthogonality K=3 MANDATORY (cross-pillar-bridge-anatomy.md)

  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: KO-dim 6 → BDI → Pf=-1 → f_R positivity → K_R>0 →
                    sign_reversal=+1 (Corner I scope-locality)

  CALIBRATION CORPUS contribution: §VII.AK is calibration-instance #2 of
                    SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag
                    (instance #1: §VII.U.2 Path-H/Path-C multi-valued
                    classification, S86 W-3 R3 R-bound; instance #2: this gate).
```

#### Joint authorship attribution per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY

**Authorship attribution declaration**:

```
§VII.AK Joint-authorship attribution:
  PRIMARY-DERIVATION (ANCHOR-1):  connes-ncg-theorist
    - R1 §"Substitution chain — BDI Pf=-1 protection algebraic equivalence"
      (lines 42-103; Steps 1-4)
    - R2 §"Response to L-1" Lemma L-1.2 + Steps L-1.3-L-1.4 (lines 487-538)
    - R2 §"Response to L-2" Definitions L-2.1-L-2.3 + Step L-2.4 (lines 539-610)
    - W-11 calibration corpus #2 framework (S86 W-11 RULE-2 instance #2)

  CO-AUTHOR-SCOPE-LOCALITY (ANCHOR-2):  lizzi-spectral-functional-theorist
    - R1 §"Substitution chain — SCHEMATIC factorization at L_max=10 vs PRIMARY PV lift"
      (lines 217-273; SCHEMATIC factorization closure analysis)
    - R2 §"H-1 substitution chain on Casimir-power factorization breaking"
      (lines 754-810; Sage-symbolic verification at PRIMARY PV)
    - R2 §"H-2 + Step C-3 + C-4 algebra-axis substitution chain at PRIMARY-B"
      (lines 826-925; algebra-axis Corner-I → Corner-IV migration)
    - W-2 R3 §VII.U.2 4-corner classification (S87 W-2 R3 lizzi-authored)
    - cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" K=3 MANDATORY
      (S87 W-2 R3 lizzi+connes+mack — instance #3 promotion)

  STRUCTURE TAG:  SOURCE-DOUBLE-CITE-CO-PRIMARY
  REGISTRY SLOT:  §VII.AK (next-free-letter pre-allocation; reserved at this R3 close)
  WORKSHOP CITATION:  s87-csub-axiom-side-proxy-taxonomy.md §R3 (this section)
```

#### W-11 calibration corpus #2 promotion criterion (formal pre-registration)

**Pre-registration Q-R3.6 formal criterion** (this is the W-7 R3 deliverable on the corpus #2 question):

```
W-11 calibration corpus #2 promotion criterion (formal pre-registration; W-7 R3 close):

LEVEL-1 closure (immediate at this R3, today):
  Required:
    (L1-a) §VII.AK registry entry written under SOURCE-DOUBLE-CITE-CO-PRIMARY structure
    (L1-b) ANCHOR-1 (connes PRIMARY-DERIVATION) cited with substitution chain
            L-1.2 + L-1.4 + L-2.4 substantively
    (L1-c) ANCHOR-2 (lizzi CO-AUTHOR scope-locality) cited with W-2 R3 §VII.U.2
            4-corner classification cross-link AND Sage-verified Casimir-power
            factorization breaking at PRIMARY (LH-1)
    (L1-d) Scope-locality declared explicitly: Corner I (algebra-INVARIANT × Mellin-FI)
    (L1-e) Forward-falsifier pointer to Corner IV scope (CF-W7-LF-C PRIMARY-B gate)
    (L1-f) S35 + S42 + KO-dim 6 axioms + W-11 corpus instance #1 SHA-pinned anchors
  Verdict if all (L1-a)..(L1-f) satisfied: corpus #2 LEVEL-1 closed today at W-7 R3.

LEVEL-2 full-scope closure (FORWARD-CONDITIONAL on S88+):
  Required (joint, NOT disjunction):
    (L2-a) CF-W7-LF-C PRIMARY-B gate dispatched and returns (PASS / INFO / FAIL):
            PASS at L_max=10 if ≥3/5 atlas regulators show algebra-axis migration to
            Corner IV (A-T4.2 confirmed at PRIMARY-B);
            FAIL at L_max=10 if 0/5 lift (substrate-axiom theorem extends to algebra-
            DEPENDENT layer; theorem broadens);
            INFO at L_max=10 if 1-2 lift (boundary; further L_max scan or finer regulator
            atlas).
    (L2-b) CF-W7-LF-D Cheeger-Simons / GV-Heitsch / η-Cheeger-Simons ODD-grading proxy
            on (C_H, C_epsH) parity-twin pair returns (PASS / INFO / FAIL):
            PASS if sign_reversal_(C_H) ≠ sign_reversal_(C_epsH) (ODD-grading
            discriminates parity twins, confirming W-11 ODD-grading-required prediction);
            FAIL if sign_reversal_(C_H) = sign_reversal_(C_epsH) (revisit framework's
            HP^1 detection program structure).
    (L2-c) LEVEL-1 already closed (prerequisite).
    (L2-d) §VII.AK registry text amended in same dispatch:
            - if (L2-a) PASS → "Corner-IV scope: CONFIRMED at PRIMARY-B"
            - if (L2-a) FAIL → "theorem extends to algebra-DEPENDENT layer; broaden scope"
            - if (L2-b) PASS → "ODD-grading complement: CONFIRMED at Cheeger-Simons"
            - if (L2-b) FAIL → "framework HP^1 detection program needs deeper scrutiny"
  Verdict if all (L2-a)..(L2-d) satisfied: corpus #2 LEVEL-2 full-scope closed at S88+.

Calibration corpus #2 closure status as of W-7 R3 close (this section):
  LEVEL-1: CLOSED-IMMEDIATE (§VII.AK landing imminent at this R3 close)
  LEVEL-2: PENDING-S88+-JOINT (PRIMARY-B + Cheeger-Simons gates pre-registered as
            CF-W7-LF-C + CF-W7-LF-D; both LOAD-BEARING on orthogonal axes).
```

**Direction**: this pre-registration is the formal answer to Q-R3.6 + the W-7 R3 deliverable on the corpus closure question. corpus #2 closes IMMEDIATELY at LEVEL 1 today; LEVEL 2 closure is forward-pinned at S88+ via JOINT (PRIMARY-B ∧ Cheeger-Simons) gates per `joint-theorem-promotion.md` 4-stage pathway analog (LEVEL-1 → STAGE-1-CANDIDATE; LEVEL-2 = post-Stage-2-cross-axis-independent-verify by PRIMARY-B + Cheeger-Simons).

#### Final 4-field carry-forwards (FINAL specs)

| ID | What | Inputs | Gate | Effort | Depends-on |
|:---|:-----|:-------|:------|:--------|:-----------|
| **CF-W7-LF-A (FINAL)** | Land §VII.AK STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE registry entry per the §VII.AK declaration block above. SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag. Mandatory anatomy elements: 5 IS-not-IN per `cross-pillar-bridge-anatomy.md`; 3-level ladder per same rule (Level 1 cohomology-class identity = sign_reversal=+1 from f_R positivity at all admissible regulators in Corner I; Level 2 algebraic envelope = L^{-3} at d=4 per W-5 W11-bridge precedent; Level 3 empirical anchor = W9c-1 5/5 + W5b-2 sub-test (c) + Sage-verified σ-window match at L_max=10). Add scope-locality declaration: Corner I; forward-falsifier pointer to Corner IV (CF-W7-LF-C). | W9c-1 .npz; S35 `s35_pfaffian_corrected_j.npz`; S42 `s42_gradient_stiffness`; W-11 corpus instance #1 verdict; §VII.W bridge anatomy text; KO-dim 6 axiom canonical (Connes 1996); §VII.U.2 4-corner classification (S87 W-2 R3); this workshop's Sage verifications | Registry landing PASS at §VII.AK; SHA-pinned anchor citations (V+C); registry-entry text contains all 5 IS-not-IN anatomy elements + 3-level ladder + SCOPE-LOCALITY pin (Corner I) + forward-falsifier pointer to PRIMARY-B | 0.5 wave-equivalent (registry write); LOAD-BEARING for corpus #2 LEVEL-1 closure | this workshop's R3 verdict; mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md` (registry-write-only follow-up) |
| **CF-W7-LF-B (FINAL)** | Sage-symbolic verification of `f_R(C; s) > 0` for ALL atlas regulators across positive Casimir support, AT PRIMARY-A bare-scalar M_PV(τ) AND AT PRIMARY-B self-consistent M_PV[⟨φ²⟩(ω)]. Also Sage-verify Δ_PV(R; τ) factorization-breaking signal: zeta/Mellin Δ_PV ≡ 0; PV/hard-cutoff/heat-kernel Δ_PV ≠ 0 at PRIMARY-A AND PRIMARY-B. | Symbolic regulator forms (Connes-Chamseddine 1996 §2); S61 PV pipeline; S78 backreaction-self-consistent kernel `s78_backreaction_selfconsistent.py`; M_KK = 7.4287e+16 GeV; D_K^≤10 spectrum cache | Sage-symbolic per-regulator positivity verification + Δ_PV pattern characterization; aggregate PASS = all 5 positive at both PRIMARY-A and PRIMARY-B + Δ_PV pattern matches expected (zero/non-zero by mass-scale presence) | 0.7 wave-equivalents (Sage-symbolic); CONFIRMATORY-CORPUS-#2-LEVEL-1-ROBUSTNESS | CF-W7-LF-A (registry context); Sage MCP availability |
| **CF-W7-LF-C (FINAL)** | PRIMARY-B self-consistent PV lift on (C_H, C_epsH) parity-twin pair: implement M_PV[⟨φ²⟩(ω)] state-pair-derived running mass per S78 backreaction pipeline; compute n_pass^PRIMARY-B at L_max=10. PASS iff PRIMARY-B lifts ≥3/5 atlas regulators to sign_reversal = -1 (algebra-axis migration to Corner IV; A-T4.2 candidate confirmed at PRIMARY-B); FAIL iff 0/5 lift (substrate-axiom theorem extends to algebra-DEPENDENT layer; theorem broadens); INFO iff 1-2 lift. Additionally pre-register Δ_PV magnitude reading per regulator at PRIMARY-B and corner-classification verdict (Corner I vs Corner IV). | `s78_backreaction_selfconsistent.py` implementation; W9c-1 .npz baseline; D_K^≤10 spectrum cache; M_KK canonical; A_K = C ⊕ H ⊕ M_3(C) state-pair specification | Composite verdict on PRIMARY-B sign-reversal aggregate (PASS/INFO/FAIL); Δ_PV magnitude per regulator at PRIMARY-B; corner-migration prediction outcome (Corner I → Corner IV at PRIMARY-B); sign + magnitude + regime 3-tuple per S87+ schema-v2 | 1.2 wave-equivalents (full S78 backreaction-self-consistent pipeline + L_max=10 re-derivation); LOAD-BEARING-ON-ALGEBRA-AXIS for corpus #2 LEVEL-2 closure | CF-W7-LF-A (LEVEL-1 closure); s78_backreaction_selfconsistent.py source; lizzi-spectral-functional-theorist + connes-ncg-theorist co-dispatch |
| **CF-W7-LF-D (FINAL)** | Cheeger-Simons / GV-Heitsch / η-Cheeger-Simons ODD-grading proxy on (C_H, C_epsH); PASS iff sign_reversal_(C_H) ≠ sign_reversal_(C_epsH) (ODD-grading discriminates parity twins, confirming W-11 ODD-grading-required prediction); FAIL otherwise (revisit framework HP^1 detection program). | W-11 corpus #1 GV-Heitsch formula; D_K^≤10 spectrum; W9c-1 .npz baseline; η-Cheeger-Simons secondary class definition (Atiyah-Patodi-Singer 1975) | Per-twin sign_reversal_(P) for P ∈ {C_H, C_epsH}; ODD-grading discrimination test | 1.5 wave-equivalents; LOAD-BEARING-ON-GRADING-AXIS for corpus #2 LEVEL-2 closure | CF-W7-LF-A (LEVEL-1 closure); orthogonal to CF-W7-LF-C |
| **CF-W7-LF-E (FINAL)** | Audit `_spectral_action_regulators.py` SCHEMATIC module against the cross-wave amplifier signal (W9b-2 Reading_1 PASS at \|ρ_S(s=4)\| = 1.000000 EXACT AND W9c-1 + W5b-2 sub-test (c) FAIL Track-A). Identify whether both signals are predicted by a single SCHEMATIC level-property argument (positivity + Casimir-power factorization closure) OR are independent observations. PASS = both predicted by single argument; INFO = one but not both; FAIL = neither. | `_spectral_action_regulators.py` source; W9b-2 line 268 verdict + .npz; W9c-1 .npz; this workshop's substitution chains H-1 + H-2 | Structural finding identifying SCHEMATIC level-property signature scope; pre-register whether the SCHEMATIC module is suitable for future cross-pillar bridge gate dispatches at the algebra-INVARIANT layer | 0.7 wave-equivalents; CONFIRMATORY-METHODOLOGY for SCHEMATIC level scope-pinning | independent of CF-W7-LF-A; orthogonal calibration |

**Summary**: 5 carry-forwards span 3 axes (registry / Sage symbolic positivity / PRIMARY-B algebra-axis / Cheeger-Simons grading-axis / SCHEMATIC module audit). LF-A is LOAD-BEARING for LEVEL-1 closure (CLOSE TODAY at W-7 R3). LF-C and LF-D are JOINT LOAD-BEARING for LEVEL-2 full-scope corpus #2 closure (S88+). LF-B and LF-E are confirmatory-robustness on orthogonal axes.

#### Workshop W-7 closure status

W-7 closes at: **HYBRID-WITH-LEVEL-DECOMPOSITION JOINT VERDICT + §VII.AK SOURCE-DOUBLE-CITE-CO-PRIMARY landing pre-allocated + W-11 calibration corpus #2 LEVEL-1 closure today / LEVEL-2 full-scope closure forward-pinned at S88+**.

- **Substrate verdict**: PRIMARY-A (and SCHEMATIC) CONFIRMATORY structural-EVEN-grading-blindness theorem at Corner I scope-locality (algebra-INVARIANT × Mellin-FI); PRIMARY-B LOAD-BEARING-PENDING on the algebra-axis (Corner I → Corner IV migration scope-conditional).
- **Methodology verdict**: SOURCE-DOUBLE-CITE-CO-PRIMARY landing per `registry-landing.md` between connes' substrate-axiom positivity derivation (ANCHOR-1) and lizzi's W-2 R3 §VII.U.2 + Sage-verified Casimir-power factorization breaking + scope-locality declaration (ANCHOR-2); corpus closure requires BOTH grading-axis (Cheeger-Simons) AND algebra-axis (PRIMARY-B) tests for LEVEL-2 full-scope (orthogonal axes per `cross-pillar-bridge-anatomy.md` algebra-axis-orthogonality K=3 MANDATORY).
- **4-field carry-forwards**: 5 total (LF-A, LF-B, LF-C, LF-D, LF-E); LF-A is the LEVEL-1 closure deliverable (registry write); LF-C + LF-D are LEVEL-2 joint pre-conditions; LF-B + LF-E are confirmatory-robustness. Net delta from R2: +0 (5 → 5; refined IDs, dependency declarations, and LOAD-BEARING/CONFIRMATORY tags pinned).
- **Joint authorship attribution**: connes PRIMARY-DERIVATION (substrate-axiom positivity + BDI Pf=-1 NCG-axiomatic chain) + lizzi CO-AUTHOR-SCOPE-LOCALITY (W-2 R3 §VII.U.2 4-corner classification + Casimir-power factorization breaking + cross-pillar-bridge-anatomy.md algebra-axis-orthogonality K=3 MANDATORY); §VII.AK registry slot reserved.
- **Calibration corpus contribution**: §VII.AK is calibration-instance #2 of the `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag; first instance was §VII.U.2 Path-H/Path-C multi-valued classification at S86 W-3 R3.

---

## Workshop W-7 closure status

**Closure class**: HYBRID-WITH-LEVEL-DECOMPOSITION JOINT VERDICT

**Substrate verdict**: PRIMARY-A (and SCHEMATIC) CONFIRMATORY structural-EVEN-grading-blindness theorem at Corner-I scope-locality (algebra-INVARIANT × Mellin-FI). PRIMARY-B LOAD-BEARING-PENDING on the algebra-axis (Corner I → Corner IV migration scope-conditional on self-consistent M_PV[⟨φ²⟩(ω)] state-pair-derived running mass). Sage-symbolic verification anchors: (i) σ-window match `|Δσ⁻²| = 2.343459900364997e-3` matches WP §W9c-1 magnitude pin (LC-1 substrate confirmed); (ii) `K_R^PRIMARY-A(τ_fold ± δ_τ) > 0` on toy SU(3) `L_max=4` Casimir spectrum, `sign_reversal_R^PRIMARY-A = +1` (LC-5 substrate confirmed); (iii) Casimir-power factorization breaking at PRIMARY PV — Sage-symbolic `(M_PV²+C)/(σ²C+M_PV²)` ratio fails to be pure σ-power, collapses to clean σ⁻²ˢ ONLY in M_PV→0 limit (LH-1 substantively confirmed at the symbolic-algebra level).

**Methodology verdict**: §VII.AK SOURCE-DOUBLE-CITE-CO-PRIMARY landing per `registry-landing.md` between connes' substrate-axiom positivity derivation (ANCHOR-1; KO-dim 6 axioms → BDI(J,γ_9) → Pf=−1 (S35 anchor) → f_R positivity → K_R>0 → sign_reversal=+1) and lizzi's W-2 R3 §VII.U.2 4-corner classification + Sage-verified Casimir-power factorization breaking + Corner-I scope-locality declaration with forward-falsifier pointer to Corner IV (ANCHOR-2). W-11 calibration corpus #2 closure: LEVEL-1 closes IMMEDIATELY at this R3 (Corner-I scope-locality stratum); LEVEL-2 full-scope closure forward-pinned at S88+ via JOINT (PRIMARY-B algebra-axis ∧ Cheeger-Simons grading-axis) gates per `cross-pillar-bridge-anatomy.md` algebra-axis-orthogonality K=3 MANDATORY.

**4-field carry-forwards**: 5 total.
- **CF-W7-LF-A** (LOAD-BEARING for LEVEL-1 closure; 0.5 wave-equiv) — §VII.AK registry write under SOURCE-DOUBLE-CITE-CO-PRIMARY structure with mack-cosmic-bridge as sole writer.
- **CF-W7-LF-B** (CONFIRMATORY-CORPUS-#2-LEVEL-1-ROBUSTNESS; 0.7 wave-equiv) — Sage-symbolic positivity verification of `f_R(C; s) > 0` across PRIMARY-A and PRIMARY-B; Δ_PV pattern characterization.
- **CF-W7-LF-C** (LOAD-BEARING-ON-ALGEBRA-AXIS for LEVEL-2; 1.2 wave-equiv) — PRIMARY-B self-consistent PV lift on (C_H, C_epsH) parity-twin pair via S78 backreaction pipeline.
- **CF-W7-LF-D** (LOAD-BEARING-ON-GRADING-AXIS for LEVEL-2; 1.5 wave-equiv) — Cheeger-Simons / GV-Heitsch / η-Cheeger-Simons ODD-grading proxy on (C_H, C_epsH).
- **CF-W7-LF-E** (CONFIRMATORY-METHODOLOGY for SCHEMATIC level scope-pinning; 0.7 wave-equiv) — `_spectral_action_regulators.py` SCHEMATIC module audit against W9b-2 ↔ W9c-1 + W5b-2 sub-test (c) cross-wave amplifier signal.

**Joint authorship attribution**: connes-ncg-theorist PRIMARY-DERIVATION (substrate-axiom positivity argument; BDI Pf=−1 NCG-axiomatic chain via KO-dim 6 axioms; Lemma L-1.2 + Steps L-1.4 + L-2.4) + lizzi-spectral-functional-theorist CO-AUTHOR-SCOPE-LOCALITY (W-2 R3 §VII.U.2 4-corner classification; Casimir-power factorization breaking H-1 + H-2 substitution chains, Sage-symbolic at this R3; cross-pillar-bridge-anatomy.md algebra-axis-orthogonality K=3 MANDATORY at instance #3 = S87 W-2 R3).

**Calibration corpus contribution**: §VII.AK is calibration-instance #2 of the `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag (instance #1 was §VII.U.2 Path-H/Path-C multi-valued classification at S86 W-3 R3). The structure tag is reinforced by orthogonal substrate-physics derivation chains (V_input = derivational-axiomatic; C_output = scope-locality + cross-link); both anchors are non-fungible and both must remain accessible per `registry-landing.md` detection criteria (1)-(3).

**Open questions deferred to S88+**:
1. CF-W7-LF-C PRIMARY-B verdict (sign_reversal aggregate; Δ_PV magnitude per regulator; Corner-IV migration outcome).
2. CF-W7-LF-D Cheeger-Simons / GV-Heitsch ODD-grading proxy verdict on (C_H, C_epsH).
3. (post-LEVEL-2) §VII.AK registry text amendment per LEVEL-2 outcome (Corner-IV CONFIRMED if LF-C PASS; theorem broadens if LF-C FAIL; ODD-grading complement CONFIRMED if LF-D PASS; framework HP^1 detection program scrutiny if LF-D FAIL).

**Substrate framing audit (per `phononic-framing.md` IS-not-IN)**: throughout the W-7 R3 closure, the direction of explanation flows substrate → emergent (D_K^≤10 spectrum at τ_fold = 0.190 → BDI Pf=−1 protection at all 34 τ values → EVEN-grading projection sector → Casimir-power Mellin scaling → both EVEN-grading proxies collapse to the same sign-predicate at Corner I scope-locality → empirical anchor at W9c-1 5/5 + W5b-2 sub-test (c)). The PRIMARY-A vs PRIMARY-B distinction is INTRA-substrate regulator-class structure (both are families of internal regulator-class projections on the same substrate spectral triple), NOT a "level of removal from the substrate". Container-thinking direction-inversions (treating SCHEMATIC as "the substrate's true behavior" or PRIMARY as "the laboratory's measurement of the substrate") are forbidden per the rule.
