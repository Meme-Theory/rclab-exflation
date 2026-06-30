# Session 116 Workshop: baptista × volovik

**Date**: 2026-06-28
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: baptista (baptista-spacetime-analyst), volovik (volovik-superfluid-universe-theorist)
**Source Documents**:
- sessions/session-116/workshops/s116-w9-saturation-adjud.md
- sessions/session-116/session-116-w9-workingpaper.md
- sessions/evoi-framework.md
- computations/session-116/s116_gate_verdicts.txt

**Third reading to fold in (from S-7)**: the w0 §23 transport-degree solo (connes) classed w0 as **deg=0 T2-VACUOUS scalar (favored)** ⇒ substrate w0 = pivot w0; the W9 anchor-fidelity gap (`→−1.340827`) is **PROXY-ARTIFACT-TYPED** (the λ_max truncation-edge is NOT an admissible §23 morphism). This SUPPORTS the divergences being normalization (Reading A leaning), but deg=0 is PROVISIONAL (CF-S117-W0-TRANSPORT-DEGREE).

**Focus Topics** (adjudication: does the branch-(iv) lineage admissibly DERIVE w0, or is `w0_FW=−0.918` Volovik-partition-closed-form-ONLY? Three divergent branch-iv values were never reconciled — S102 W5 spectral-triple-DIRECT `w0=−0.842454` / W9 CAC-asymptote `w0_cac→−1.340827` / canonical Volovik-partition `w0_FW=−0.918`; AND the anti-rescue fence §EVOI.BF already ruled branch-iv w0 derivation-INADMISSIBLE post-S86):
1. (a) Reconcile the three readings — `−0.842454` (zero normalization) / `−1.340827` (Weyl-forced CAC) / `−0.918` (canonical): three normalizations of ONE Zubarev moment, or structurally distinct objects? Which (if any) is the substrate-natural branch-iv w0?
2. (b) Does §EVOI.BF (branch-iv w0 derivation-INADMISSIBLE post-S86; S101 W4-3 INFO) extend to the W9 CAC route, given the CAC L=10 anchor re-introduces a branch-iv value `ρ_B(10)` via a tuned offset — legitimate stability diagnostic, or re-laundering of the inadmissible direct value?
3. (c) Does reading-(B) (`λ_max` = non-substrate truncation edge, no continuum limit) retroactively VOID the CAC L=10 anchor `ρ_B(10)=mean_Z(10)/λ_max(10)−1` (also `λ_max`-divided; `offset_B=−0.342793` tuned at L=10), so `w0_cac(10)=−0.918` is a one-point calibration of an artifact-laden proxy?
4. (d) STRUCTURAL VERDICT: does `w0=−0.918` JOIN {n_s, m_H, r} as spectral-action-derived, or is it Volovik-partition-closed-form-ONLY (branch-iv corridor CLOSED, EVOI Tier-2 7c retires to §5)? + the falsifier-surface consequence for the DESI DR3 w(z) decision-rule.

---

## Round 1 — baptista: Opening Analysis

### B1: (a) Reconcile the three branch-iv readings (−0.842454 / −1.340827 / −0.918)

**Key finding — the three readings are ONE Zubarev moment under three (offset, limit) choices, not three structurally distinct objects. The branch is in the OFFSET, not the moment.** The S102 W5 evaluator (`computations/session-102/s102_branch_iv_canonical_eval.py:20–33`) is explicit: it builds the spectral-triple-direct moment

```
(B1)  ρ_B(L) := ρ_Zubarev(L) = ⟨|λ|⟩_Z(L)/λ_max(L) − 1 ,
      ⟨|λ|⟩_Z(L) = [Σ_j d_j w_Z(|λ_j|)|λ_j|] / [Σ_j d_j w_Z(|λ_j|)] ,  w_Z(λ)=exp(−λ²/Λ_Z²), Λ_Z=1   (S85 W0-7)
```

and then anchors it via `w_0^CAC(L) = ρ_B(L) + offset`, `offset = target − ρ_B(10)`. The SAME ρ_B(L) underlies all three readings (script header verbatim: "both w_0_A = −0.918 and w_0_B = −0.842454 are projections of the same substrate vacuum partition; the branch-iv CAC re-anchors the spectral-triple-direct ρ_Zubarev(L) to w_0_B instead of w_0_FW"):

| reading | construction | what it IS |
|:--|:--|:--|
| **−0.918** | `ρ_B(L) + offset_A`, `offset_A = w0_FW − ρ_B(10) = −0.340827` | A-branch CAC, anchored at L=10 to the **Volovik-partition** closed form |
| **−0.842454** | `ρ_B(L) + offset_B`, `offset_B = w0_B − ρ_B(10) = −0.265281` | branch-iv CAC, anchored at L=10 to the **substrate-compaction** closed form (disclosed alternate, NOT co-equal) |
| **−1.340827** | `lim_{L→∞}[ρ_B(L)+offset_A] = −1 + offset_A = −1.918 − ρ_B(10)` | the **running-edge L→∞ asymptote** of the A-CAC |
| (ρ_B alone) | `ρ_B(L)`, no offset (RDC) | → **−1** (`s85_w0_zubarev_lmax_convergence_to_minus_one.npz`); **INADMISSIBLE** per the lockdown demarcation theorem |

**Decisive structural identity (Sage QQ-exact).** The A-CAC and B-CAC are EXACT PARALLEL TRANSLATES of the one curve ρ_B(L):

```
[ρ_B(L)+offset_A] − [ρ_B(L)+offset_B]  =  offset_A − offset_B  =  −0.075546   for EVERY L
                                       =  w0_FW − w0_B  =  (−0.918) − (−0.842454)  =  −0.075546   (Sage QQ-exact)
```

The ρ_B(L) term cancels identically. −0.918 and −0.842454 are ONE moment shifted by two constants whose difference is *exactly* the value gap — they are NOT two physics-distinct w0 predictions, they are one spectral moment re-anchored to two different closed-form TARGETS. Likewise −1.340827 is the A-CAC's own L→∞ limit `−1.918 − ρ_B(10)` (Sage-exact; lineage-sensitive ±0.001966 between the lockdown ρ_B(10)=−0.577173 and the W9 (4,4)-filled ρ_B(10)=−0.575207, giving −1.340827 vs −1.342793 — both ≈ −1.341).

**Which is the substrate-natural branch-iv w0?** NONE of the three offset-targets is *produced by* the moment. The moment's own value is the −1 limit (RDC), which the regulator-convention-lockdown demarcation theorem rules OUTSIDE the admissibility class (`w0^C(10)=w0_FW` exactly is required; RDC fails it). So the substrate-natural VALUE is set by the closed form (Volovik partition + effacement Γ_eff=0.99970 = −0.918); the branch-iv moment's substrate-natural role is to supply the L_max-convergence ENVELOPE around it, not the value. −0.842454 is the SAME moment re-anchored to a different (substrate-compaction) closed form, registered as "disclosed alternate, NOT co-equal" (`w0-primary-decision-rule.md §4`). −1.340827 is the running-edge asymptote, which the connes §23 transport-degree solo types as PROXY-ARTIFACT (the λ_max truncation edge is not an admissible §23 morphism).

**Substrate-first framing (GEOMETRIC, Level-1 single-τ-slice).** ρ_B(L) IS a spectral moment of D_K at τ_fold=0.190 — the substrate's vibrational spectrum, not a field "in" a container. Arrow: `D_K eigenvalues at τ_fold → branch-iv Zubarev moment ρ_B → CAC-anchored w_0 → DESI DR3 w_0–w_a`. The "three values" are one substrate moment read through three normalization choices, not three substrate predictions.

**DESI falsifier implication.** The framework stakes ONE value on the DR3 surface: −0.918 (canonical, 2.13σ from DESI DR2 −0.803±0.054). The "three-way divergence" is not three competing predictions — it is one moment whose admissible (lockdown-CAC) reading anchors to −0.918. R_842=[−0.942,−0.742] binary containment holds both −0.918 and −0.842454; the staked prediction is −0.918, with −0.842454 the reversibility-trigger alternate (fires only if DR3 ∈ [−0.86,−0.83]).

**Questions for volovik:**
1. Do you accept the parallel-translate identity (`offset_A − offset_B = w0_FW − w0_B` exactly) as proof that −0.918 and −0.842454 are ONE moment re-anchored, not two structurally distinct w0 predictions? If so, the "three-way divergence" collapses to a single-moment + offset-choice question.
2. The Volovik-partition closed form is YOUR domain. Is −0.918 exact and L_max-independent (a Level-1 structural identity), or does the partition itself carry a regulator/averaging convention that the branch-iv envelope is implicitly testing?

### B2: (b) Does §EVOI.BF extend to the W9 CAC route?

**Key finding — §EVOI.BF fences branch-SHOPPING (deriving-and-staking −0.842), NOT the use of branch-iv as an L_max-stability diagnostic anchored to −0.918.** The fence text (`evoi-framework.md:49`): *"NO branch-shopping (w₀ branch-iv −0.842 at 0.731σ is derivation-INADMISSIBLE post-S86; the canonical w₀ = −0.918 at 2.13σ is the honest figure, aligned with the inv-13 W1-3 L_max FAIL)."* Parse the prohibited act precisely: it is **selecting the DESI-friendlier value** (−0.842, 0.73σ) over the honest canonical (−0.918, 2.13σ) and staking it as a derivation. The fence *protects* −0.918 and *forbids promoting* −0.842.

The W9 CAC route does the OPPOSITE of the fenced act:
- it STAKES −0.918 (the protected figure), via `offset_A = w0_FW − ρ_B(10) = −0.340827`;
- it uses ρ_B(L) as an L_max-STABILITY diagnostic (the sliding-window spread), not as a derivation of an alternate VALUE.

So §EVOI.BF does NOT extend to forbid the W9 CAC route — the route is fence-COMPLIANT and in fact fence-SERVING: it supplies a stability certificate for the very value the fence protects.

**The subtlety, head-on (the offset re-introduces ρ_B(10)).** volovik's strongest form: "the CAC L=10 anchor re-introduces a branch-iv value ρ_B(10) via a tuned offset — isn't that re-laundering the inadmissible direct value?" The answer is the two-output split of the CAC:
- The **anchor VALUE** `w0^CAC(10) = −0.918` is INPUT (from the Volovik closed form, via `offset = w0_FW − ρ_B(10)`). It is −0.918 by construction. The offset launders exactly this one number — and it launders it to the FENCE-PROTECTED value −0.918, never to −0.842. (Anchoring to −0.842 would be the inadmissible act; anchoring to −0.918 is the honest one. The offset is the *opposite* of branch-shopping.)
- The **L_max-stability VERDICT** (the spread `max−min` over a window) is OUTPUT. It is offset-FREE: the constant offset cancels in `max−min`, so `spread_CAC = spread_ρ` (W9 `offset_cancellation_residual = 1.11e-16`). The spread is a genuine, un-laundered diagnostic — ρ_B(L) could have diverged, oscillated, or accelerated; it instead decelerates as `|d| = μb/λ_max² ~ 1/L²` (Sage-ratio 1.00081, W9). The stability is NOT built in.

So the fence-inadmissible operation (deriving a VALUE from the moment) is NOT what the CAC performs; the CAC takes the value as input and reports a stability verdict. Different uses of ρ_B — and only the first is fenced.

**Honest scope caveat (the fence's own "L_max FAIL" alignment).** The fence aligns with "inv-13 W1-3 L_max FAIL." That FAIL is the FULL-window {12,13,14,15,16} spread = 0.0630 (> 0.050 FAIL band), which INCLUDES the early-L transient where ρ_B moves fastest (|d| largest at small λ_max). My stability claim is scoped to the SLIDING high-L window, where the spread narrows: 0.130419 {8,10,12} → 0.044514 {12,13,14} → 0.0392902 {13,14,15}, decelerating. Both are true and not in tension — full-window fails (transient dominates), sliding-window narrows (transient slid off the bottom). I do NOT claim branch-iv is PASS-stable now: it is INFO (marginal), projected to PASS (≤0.025) at L≈19 by the 1/λ_max² law. The fence's "L_max FAIL" and my "narrowing" describe different windows of the same moment.

**DESI falsifier implication.** §EVOI.BF's anti-rescue arming is *satisfied* by Reading A: I stake −0.918 (2.13σ), I do NOT promote −0.842, and the W9 CAC route adds a stability certificate without moving the staked value. The fence stays armed and CLEAN — my reading is the anti-branch-shopping reading.

**Questions for volovik:**
1. Do you accept the two-output split — anchor VALUE (input, fenced) vs stability VERDICT (output, offset-free, un-fenced) — as the line that keeps the W9 CAC route fence-compliant? Or do you hold that ANY branch-iv touch of w0 (even a diagnostic *on the protected value*) is fenced post-S86?
2. The fence cites "inv-13 W1-3 L_max FAIL" (full-window 0.0630). Given the sliding window narrows (0.0393, → PASS at L≈19), is the fence's "L_max FAIL" a permanent verdict on the moment, or a window-specific one that the deep-truncation data is in the process of refining?

### B3: (c) Does reading-(B) void the CAC L=10 anchor?

**Key finding — reading-(B) voids the running-edge ASYMPTOTE's substrate-meaning (I grant it), but it does NOT void the L=10 ANCHOR, because λ_max(10) cancels identically in the anchor.** Reading-(B): λ_max is a truncation edge with no continuum limit (the SU(3) Dirac spectrum is unbounded above), so `ρ_B(10) = mean_Z(10)/λ_max(10) − 1` is edge-built, so the anchor `w0^CAC(10) = −0.918` is a one-point calibration of an artifact-laden proxy. I GRANT the premise (λ_max non-substrate) in full; the conclusion (anchor voided) does not follow.

**Substitution chain (the cancellation):**
```
Step 1   w0^CAC(10)  = ρ_B(10) + offset_B               [CAC definition, s102…py:33]
Step 2   offset_B    = w0_FW − ρ_B(10)                   [DERIVED offset, ZERO free normalization, s102…py:32]
Step 3   w0^CAC(10)  = ρ_B(10) + [w0_FW − ρ_B(10)]       [substitute Step 2 into Step 1]
Step 4               = w0_FW = −0.918                     [ρ_B(10) cancels EXACTLY; W9 residual 1.11e-16]
Conclusion  The anchor does NOT depend on ρ_B(10) — hence NOT on λ_max(10) being substrate-meaningful.
            λ_max(10) enters ρ_B(10) and is removed by −ρ_B(10) inside the offset. ∎
```

The anchor is a DEFINITIONAL IDENTITY to the closed form, edge-independent by construction. Reading-(B)'s "λ_max(10) is non-substrate" is both TRUE and HARMLESS at the anchor: whatever λ_max(10) is, it cancels.

**Where the edge DOES bite (and reading-(B) is right).** The *running* edge λ_max(L) at L≠10 does NOT cancel against the L=10-pinned offset. That non-cancellation IS the spread (the L_max-stability variation) AND the drift of the central value to the −1.341 asymptote. So reading-(B) correctly identifies that the running edge contaminates the OFF-anchor behavior — and the connes §23 typing sharpens it: the λ_max truncation edge is NOT an admissible §23 transport morphism, so the −1.341 asymptote is PROXY-ARTIFACT-TYPED, not a substrate value. Reading-(B) voids the substrate-meaning of the ASYMPTOTE (agreed), not the anchor.

**Constructive corollary (de-reference the edge → anchor-fidelity closes).** Because the drift is 100.1% the running λ_max(L) denominator while mean_Z is frozen (W9 channel split 100.081%/−0.081%), replacing the running edge with the fixed physical-cache edge — `ρ_B^{fix}(L) = mean_Z(L)/λ_max(10) − 1` — gives `ρ_B^{fix}(L) ≈ ρ_B(10)` for all L (mean_Z frozen to ~10⁻⁴/shell), hence `w0^CAC,fix(L) ≡ −0.918`, FLAT, with the asymptote ALSO −0.918 (no drift). Under fixed-edge, reading-(B)'s OWN premise (the edge is non-substrate, so do not let it run) RECOVERS the anchor at all L. Whether the substrate-correct branch-iv statistic normalizes by the running edge, the fixed edge, or not at all is the open proxy-design compute (CF-S117-W0-ANCHOR-FIDELITY / -TRANSPORT-DEGREE).

**Honest concession.** At the anchor, branch-iv = closed form by construction (it adds nothing THERE). The lineage's value-add is entirely OFF-anchor: the narrowing L_max-stability envelope + the candidate fixed-edge normalization that closes the anchor-fidelity gap. Reading-(B) is right that the anchor *alone* is "−0.918 by construction"; it overreaches if it concludes the whole lineage is therefore void — the off-anchor envelope is real and admissible.

**DESI falsifier implication.** The staked −0.918 does NOT rest on λ_max(10) being substrate-meaningful (it cancels), so reading-(B) does not weaken the DR3 prediction. What reading-(B) correctly DOES flag is that the running-edge asymptote (−1.341) must NOT be read as "the spectral action's real w0" and staked — it is a proxy artifact, correctly excluded from the falsifier surface.

**Questions for volovik:**
1. Do you accept that the Step-4 cancellation makes the L=10 anchor edge-INDEPENDENT, so reading-(B)'s "non-substrate λ_max" voids the asymptote but not the anchor? If not, identify the residual λ_max-dependence that survives the `ρ_B(10) − ρ_B(10)` cancellation.
2. From the Volovik-vacuum side: is the fixed-edge normalization (λ_max held at the physical cache value) the substrate-natural choice — i.e., does the Volovik partition's late-time projection use a FIXED vacuum-energy scale rather than a running spectral edge? Your answer largely decides CF-S117.

### B4: (d) baptista's pinned position — Reading A (branch-iv supports −0.918, w0 JOINS {n_s,m_H,r})

**Pinned position: w0 = −0.918 JOINS {n_s, m_H, r} as spectral-action-SUPPORTED — at a CONDITIONAL grade, structured as a Level-1/2/3 ladder — and is therefore NOT "Volovik-partition-closed-form-ONLY." It does not (yet) join at the zero-input-derivation grade n_s and m_H occupy: the value comes from the Level-1 closed form, the branch-iv lineage supplies the Level-2 envelope.** I read w0 through the cross-pillar-bridge 3-level anatomy (`cross-pillar-bridge-anatomy.md`):

- **Level 1 — structural identity (regulator-invariant, L_max-independent).** w0 = −0.918 from the Volovik-partition vacuum + effacement Γ_eff = 0.99970. The closed form (volovik's domain); NOT a truncated spectral moment, hence no L_max dependence. SOLID and primary.
- **Level 2 — algebraic convergence envelope (L_max-dependent).** The branch-iv Zubarev moment ρ_B(L), CAC-anchored, supplies an `L^{−α}`-class envelope: the sliding-window spread narrows 0.130419 → 0.044514 → 0.0392902 with a decelerating decrement `|d| = μb/λ_max² ~ 1/L²` (μ = mean_Z ≈ 1.9879 frozen, b = ∂λ_max/∂L ≈ 0.375; Sage-ratio 1.00081, W9), summable, projected to PASS (≤0.025) at window {17,18,19}, L≈19. MY domain (KK geometry on D_K). Admissible (CAC, not RDC), genuinely narrowing — NOT flat-by-construction.
- **Level 3 — empirical anchor at canonical L_max.** At the canonical L=10 cache (where ALL framework observables are read), `w0^CAC(10) = −0.918` exactly; the deep-window spread {13,14,15} = 0.0392902 (INFO, narrowing).

So w0 carries the SAME 3-level structure as a registered cross-pillar bridge (closed-form Level-1 + spectral-action Level-2 envelope + Level-3 anchor). In THAT structural sense it joins {n_s, m_H, r}: it has a real, admissible, narrowing spectral-action envelope — strictly more than "closed-form-only," which would have NO spectral-action diagnostic at all.

**The conditional, stated honestly (no imprecise label on my own side, per the W9 self-correction discipline).** The grade is CONDITIONAL on the open Level-3 anchor-fidelity question:
- Under the RUNNING-edge normalization, the Level-2 envelope's CENTRAL value drifts to −1.340827 (anchor-INfidelity; Weyl-forced, W9). The spread converges; the value it converges *around* drifts. ⇒ spectral-action-CONSISTENT-but-anchor-drifting.
- Under the FIXED-edge normalization, `w0^CAC ≡ −0.918` at all L with NO drift (mean_Z frozen). ⇒ spectral-action-anchor-FAITHFUL.
- The choice between them is CF-S117 (proxy-design). Until it resolves toward an anchor-faithful normalization, w0 joins {n_s,m_H,r} as spectral-action-SUPPORTED (envelope present, admissible, narrowing) but not as zero-input-DERIVED (the value is the Level-1 closed form's, not the moment's).

This is genuinely Reading A (branch-iv adds real spectral-action content; w0 is NOT closed-form-only) AND it concedes Reading B's true core (the moment does not independently output −0.918; the value is the closed form's). The honest verdict is the BRIDGE, not either pole: **−0.918 = Level-1 closed-form value + Level-2 branch-iv envelope, conditional on CF-S117 for Level-3 anchor-fidelity.**

**EVOI Tier-2 7c does NOT retire to §5 as "closed-form-only."** It stays LIVE as the Level-2-envelope / anchor-fidelity track: CF-S117-BRANCH-IV-L16 (extend the envelope), CF-S117-W0-ANCHOR-FIDELITY (the normalization decider), CF-S117-W0-TRANSPORT-DEGREE (confirm the connes §23 deg=0). A "closed-form-only" verdict would prematurely close a track that has an admissible, narrowing spectral-action envelope and three clean forward gates.

**DESI falsifier consequence — unchanged staked value, strengthened robustness case:**
- Staked: w0 = −0.918 (canonical, 2.13σ vs DESI DR2 −0.803±0.054; 3.28σ vs LCDM −1). The branch-iv lineage does NOT license −0.842 (fence); the −1.341 asymptote is NOT staked (proxy artifact).
- The binding DR3 test is R_842=[−0.942,−0.742] binary containment (both −0.918 and the −0.842 alternate inside), with the −0.86/−0.83 reversibility band (`w0-primary-decision-rule.md §5`). My reading leaves the rectangle, staked value, and σ-distances UNCHANGED.
- What it ADDS: −0.918 is not a fragile one-point closed form; it carries a spectral-action Level-2 envelope that is L_max-stable (narrowing) and, under fixed-edge, anchor-faithful at all L. That strengthens the case that −0.918 is a robust substrate prediction worth staking on DR3.

**Questions for volovik:**
1. Is the Level-1 Volovik-partition value (−0.918) exact and regulator-free? If YES, the branch-iv Level-2 envelope is a CONSISTENCY CHECK and −0.918 stands regardless of CF-S117 ("Level-1 solid + Level-2 supportive"). If the partition carries hidden regulator dependence, the envelope is part of the DERIVATION and CF-S117 is load-bearing for the VALUE. Which is it?
2. Do you accept "spectral-action-SUPPORTED, conditional on CF-S117" as the honest grade — strictly between your "closed-form-ONLY" and a full "{n_s,m_H} zero-input-derived" — or do you hold that anything short of zero-input derivation collapses to closed-form-only?

### B5: Cross-Cutting Observations

1. **This dispute is the W9 L_max-stability ≠ anchor-fidelity distinction applied to the DERIVATION-GRADE question.** W9 separated the spread (converges) from the central value (Weyl-drifts to −1.341). Here the SAME split decides the grade: branch-iv is L_max-stable (spread narrows → Reading A's "supports −0.918") but the derivation-grade hinges on anchor-fidelity (central value), which hinges on the normalization (running vs fixed edge → CF-S117). Reading A and Reading B are arguing about the SAME open variable from opposite ends — A points at the converging spread, B points at the drifting central value, and both are real properties of the one moment ρ_B = mean_Z/λ_max − 1.

2. **w0 is a deg=0 observable — the open question is NORMALIZATION, not scale transport.** The connes §23 solo types w0 as a T2-VACUOUS scalar (deg=0): substrate w0 = pivot w0, no BZ→pivot transport. Unlike n_s/α_s (which carry the 54.04-decade transport-degree question), w0's only open spectral-action question is the NORMALIZATION of the moment (running vs fixed edge). This LOCALIZES the open question cleanly to CF-S117 and rules out a whole class of transport-degree confounders. (Caveat: deg=0 is PROVISIONAL per the §23 solo → CF-S117-W0-TRANSPORT-DEGREE; if deg≠0 surfaces, a transport leg re-enters.)

3. **The natural division of labor — Reading A and Reading B are two legs of one bridge.** volovik owns Level-1 (the −0.918 value, Volovik vacuum partition); I own Level-2 (the branch-iv Zubarev envelope on D_K). This is structurally identical to W9, where spectral-geometer owned the bottom-K / mean_Z (frozen numerator) and I owned the λ_max edge (drifting denominator) — and the honest verdict was the EXACT ratio ρ_B = mean_Z/λ_max − 1, not either factor alone. Here the honest verdict is again the bridge: value (volovik) + envelope (baptista), conditional on CF-S117. "Closed-form-ONLY" (Reading B) drops my leg; "zero-input-derived" (strong Reading A) drops volovik's. Neither pole is the whole truth.

4. **Precision flag for the workshop's number-handling (two traps).** (i) The asymptote is lineage-sensitive: −1.340827 on the lockdown ρ_B(10)=−0.577173 vs −1.342793 on the W9 (4,4)-filled ρ_B(10)=−0.575207 (Sage-exact difference 0.001966); both ≈ −1.341. (ii) Two σ-metrics are in play: the decision-rule distances (3.28σ for A, 6.30σ for B) are vs **LCDM** (−1); the EVOI fence's 2.13σ/0.73σ are vs the **DESI DR2 measurement** (−0.803±0.054). The R3 verdict must not conflate the two ρ_B(10) lineages or the two σ-metrics.

5. **What would actually FALSIFY Reading A (not just weaken it).** If the CF-S117 proxy-design compute shows the substrate-natural normalization is the RUNNING edge (not fixed, not edge-free), then the spectral-action moment's anchor-faithful value is −1.341, the L=10 agreement with −0.918 is a pure one-point coincidence of the offset, and w0 collapses to Volovik-partition-closed-form-ONLY (Reading B wins, EVOI 7c retires). So Reading A is not unfalsifiable hand-waving — it stakes a specific forward gate (CF-S117 must select fixed-edge or edge-free) and concedes the outcome if it selects running-edge.

**Question for volovik (cross-cutting):** If we agree the honest position is the Level-1 + Level-2 bridge, the live disagreement reduces to ONE bit — is the Level-1 closed form self-sufficient for the VALUE (your Reading B, my envelope as consistency-only), or is the value JOINTLY held by closed-form + envelope (my Reading A, CF-S117 load-bearing)? What evidence from the Volovik partition's OWN construction (does it average over a spectral edge? hold a fixed vacuum scale?) settles that bit before CF-S117 even runs?

---

## Round 1 — volovik: Response & Cross-Synthesis

### Part 1: Response to baptista's Sections

#### Re: B1 — three-reading reconciliation

**AGREE on the algebra; the conclusion inverts.** The parallel-translate identity is exact (Sage QQ, this turn): `offset_A − offset_B = w0_FW − w0_B = −37773/500000 = −0.075546`, the ρ_B(L) term cancelling identically. I accept it without reservation. But read what it PROVES. Write the two offsets out:

```
offset_A = w0_FW − ρ_B(10)            [contains w0_FW as a free part]
offset_B = w0_B  − ρ_B(10)            [contains w0_B  as a free part]
offset_A − offset_B = w0_FW − w0_B    [ρ_B(10) cancels — the moment is the common backdrop]
```

The identity holds BECAUSE each offset is a tuned constant whose only free part is the closed-form TARGET. The moment ρ_B(L) is shared across all three readings; the readings differ ONLY in which closed form you subtract-and-re-add. So the identity is the strongest evidence for Reading **B**, not A: the VALUE in every reading lives entirely in the offset-target (the closed form), and the spectral moment is a value-neutral carrier common to all of them. Your own phrase — "the branch is in the OFFSET, not the moment" — IS my thesis, and the offset is not a spectral object: it is a closed-form value minus a constant.

**Which is the substrate-natural branch-iv w0?** You answer it yourself: NONE of the three offset-targets is *produced by* the moment; the moment's own value is −1 (RDC), ruled inadmissible. I sharpen it — the moment is not merely "not the value," it is −1, a gap of 0.082 from −0.918 (and under the CAC running asymptote, 0.423). **EMERGES — the structural core for V1/V2:** the lockdown's demarcation theorem (`regulator-convention-lockdown.md`) DEFINES the admissible class as exactly those conventions with `w0^C(10) = w0_FW` bit-exact. "Admissible" therefore MEANS "tuned to return w0_FW at the anchor." The admissibility criterion IS the injection — there is no admissible branch-iv convention that does not carry w0_FW as an input.

#### Re: B2 — §EVOI.BF extension

**DISAGREE on scope; the fence extends.** Your two-output split (anchor VALUE = input/fenced; stability VERDICT = output/offset-free/un-fenced) is the cleanest defense available, and I grant its first half exactly: the offset cancels in `max−min`, so `spread_CAC = spread_ρ` (Sage this turn: `(ρ_a+off) − (ρ_b+off) = ρ_a − ρ_b`; W9 residual 1.11e-16). The spread is genuinely un-laundered.

But **offset-FREE is offset-INVARIANT, and offset-invariant is VALUE-NEUTRAL.** The same `spread_ρ` obtains whether you anchor to −0.918, to −0.842454, or to −1.340827 — bit-identical across all three targets, because the target lives only in the cancelled offset. A diagnostic that cannot distinguish −0.918 from −1.341 cannot be evidence FOR −0.918.

This is not my coinage; it is already in the register. **S101-W0-BRANCH-IV-EVALUATOR** (S101 W4-3, audit `cd0492d6`) closed INFO with the literal tags `derivation-inadmissible … NO-Θ-free-map-reproduces-w0_B at 1e-5` and `surrogate-spread-UNINFORMATIVE`. The framework already adjudicated that the branch-iv spread carries no derivation content. So §EVOI.BF's "branch-iv −0.842 is derivation-INADMISSIBLE post-S86" is not a narrow ban on promoting one number — it is the register's standing verdict that the branch-iv moment does not DERIVE w0, full stop. The CAC route does not escape it by anchoring to the friendlier-to-the-fence value: anchoring to −0.918 instead of −0.842 changes WHICH closed form is injected, not WHETHER one is injected. "Fence-serving" overstates it — a value-neutral spread *serves* no value; it certifies only that ρ_B(L) is a smooth convergent sequence (converging to −1).

Your honest scope caveat (full-window FAILs, sliding-window narrows) I accept as accurate about the spread's WIDTH. It is orthogonal to the derivation question: a narrowing spread of a sequence → −1 tells you the sequence converges (to −1); it says nothing about −0.918.

#### Re: B3 — reading-(B) voids the anchor?

**AGREE the cancellation is exact — and it is the demonstration that the anchor is a definitional identity, not a derivation.** Your substitution chain is correct; I reproduce its punchline: `w0^CAC(10) = ρ_B(10) + [w0_FW − ρ_B(10)] = w0_FW`, ρ_B(10) cancelling to W9 residual 1.11e-16. You read this as "the anchor is edge-INDEPENDENT (robust)." I read the same identity as "the anchor is INPUT-DETERMINED (vacuous as confirmation)." Both are true; the second is load-bearing. An anchor that returns w0_FW for ANY value of ρ_B(10) — indeed for any moment whatsoever — is not measuring −0.918; it is restating it. You concede precisely this: "at the anchor, branch-iv = closed form by construction (it adds nothing THERE)." Then the Level-3 "empirical anchor at canonical L_max" of your B4 ladder is empirically empty: it is −0.918 because the offset was set to make it −0.918.

**MISSED — the fixed-edge "rescue" is circular by the same mechanism, and I checked all three of your axes this turn (Sage).** Your constructive corollary offers `ρ_B^fix(L) = mean_Z(L)/λ_max(10) − 1` (frozen ⇒ `w0^CAC,fix ≡ −0.918`, flat). But the flat −0.918 is STILL the injected offset: `offset_fix = w0_FW − ρ_B^fix(10) = −0.918 − (−0.575) = −0.343`. The frozen moment contributes ρ_B^fix(10) = −0.575; the offset contributes −0.343; they sum to −0.918 ONLY because −0.343 was tuned to make them. Freezing the moment removes the DRIFT, not the INJECTION. I verified all three normalization axes:

| normalization | bare moment ρ(10) | bare-moment limit | offset = w0_FW − ρ(10) | w0^CAC(10) |
|:--|:--|:--|:--|:--|
| running-edge (CAC) | −0.575 | → −1 (Weyl-forced) | −0.343 | **−0.918** (injected) |
| fixed-edge | −0.575 | frozen −0.575 | −0.343 | **−0.918** (injected) |
| no-edge (drop λ_max) | +0.987 | frozen +0.987 | −1.905 | **−0.918** (injected) |

The bare moments are {−0.575, −0.575, +0.987}; NONE is −0.918; EACH reaches −0.918 only through `offset = w0_FW − ρ(L*)`. The edge-design choice (CF-S117) selects which costume the injected value wears; it cannot make the value a spectral output. Reading-(B) voids the asymptote's substrate-meaning (agreed) AND exposes that the anchor's −0.918 is injected, not measured.

#### Re: B4 — Reading A

**DISAGREE — the 3-level ladder is DEGENERATE, and the degeneracy is exactly what separates w0 from n_s/m_H/r.** Take a genuine registered bridge as the control. For n_s the spectral computation OUTPUTS 0.9561 (gauge-invariant spectral geometry); there is no closed-form "n_s value" subtracted-and-re-added at canonical L. Level-2 (the L_max envelope) converges TO Level-3 (an independent empirical match, Planck), and any Level-1 closed form is a SEPARATE confirmation, not an INPUT to the computation. Three independent things that agree.

Now w0 under your ladder:
- **Level-1** = −0.918 (Volovik partition + effacement; my domain; real).
- **Level-3** = `w0^CAC(10) = −0.918` — but this is Level-1 RE-INJECTED via the offset (the definitional identity of your B3), not an independent anchor.
- **Level-2** = the offset-invariant spread — value-NEUTRAL (Re:B2), bit-identical for −0.918 / −0.842 / −1.341.

So the three "levels" are not three agreeing things; they are ONE thing — the Level-1 closed form — appearing once as itself, once re-injected (Level-3), and once as a value-blind diagnostic (Level-2). A degenerate ladder: one value wearing a spectral costume. The structural test is your own offset identity: a genuine spectral OUTPUT `O_spec(L)` does not satisfy `O_pred = O_spec(L) + [O_pred − O_spec(L*)]` as the DEFINITION of how `O_pred` is obtained; w0 does, with `O_pred = w0_FW` sitting inside the bracket. **A construction that contains its target as an input cannot derive that target.**

I grant — emphatically — that "more mathematical structure exists" than a bare number: ρ_B(L) is a real spectral moment, and its spread is a real, narrowing, admissible (CAC-not-RDC) quantity. But "more structure exists" ≠ "the value is spectral-action-derived." The extra structure is value-neutral. So "strictly more than closed-form-only" is true in a trivial sense (a value-blind diagnostic co-exists) and false in the load-bearing sense (the derivation-grade of the VALUE is unchanged). Your CONDITIONAL grade ("spectral-action-SUPPORTED, conditional on CF-S117") is conditional on an outcome the demarcation theorem forbids: an admissible no-injection variant. There is none (Re:B3 table).

#### Re: B5 — Cross-Cutting

**On your "ONE bit" (is the Level-1 closed form self-sufficient for the VALUE, or jointly held by closed-form + envelope?): self-sufficient.** The envelope is provably value-neutral (offset-invariant; Sage `spread = ρ_a − ρ_b`; registered `surrogate-spread-UNINFORMATIVE`, S101), and the anchor is provably a definitional identity (your B3). Neither can "jointly hold" a value it is structurally blind to. The closed form holds the value alone.

Two further structural points:

1. **AGREE on your point-2 (w0 is deg=0; the open question is normalization, not transport) — but it cuts toward Reading B.** If w0 carries no BZ→pivot transport leg (unlike n_s/α_s), then the ONLY thing the branch-iv lineage could have added to the value is a normalization envelope — and that envelope is value-neutral. Strip the transport confounder and branch-iv's contribution to the VALUE is exactly zero.

2. **The deeper asymmetry the ladder analogy hides: w0's CLOSED FORM is not itself a D_K spectral moment.** n_s and m_H are D_K spectral observables (spectral geometry; KK thresholds) — their value lives IN the vibrational spectrum. w0 = −0.918 lives in the Volovik vacuum PARTITION + effacement Γ_eff = 0.99970 — a substrate THERMODYNAMIC identity (q-theory effacement of the vacuum energy), NOT a `Tr f(D_K)` moment. Substrate-first: the fabric IS both its D_K vibrational spectrum AND its vacuum partition; w0 is a property of how the vacuum energy effaces (impedance-mismatch leakage), not of the eigenvalue spread. Branch-iv is the attempt to relocate a thermodynamic observable into the vibrational spectrum — and it converges to the wrong number (−1) because it is reading the wrong observable. This is honest substrate physics, not a deficiency: w0 is a closed-form substrate identity, categorically distinct from a D_K spectral-action derivation, and it does not need branch-iv to be real.

So the honest verdict on your bridge: **there is no bridge to build.** The value (volovik, Level-1) is the whole load; the "envelope (baptista, Level-2)" is value-neutral. w0 is Volovik-partition-closed-form-ONLY.

### Part 2: Original Analysis

#### V1: Reading B — w0=−0.918 closed-form-ONLY; branch-iv corridor CLOSED as a w0-derivation

**Pinned position:** w0 = −0.918 stands on the Volovik-partition closed form ALONE. It does NOT join {n_s, m_H, r} as spectral-action-derived; the branch-iv lineage (S102→S116) should be CLOSED as a w0-DERIVATION corridor. The DESI DR3 falsifier rests on the closed form only.

**The circularity theorem (the CAC anchor re-derives its own input):**
```
Step 1   w0^CAC(L) := ρ_B(L) + offset                       [CAC definition, s102…py:33]
Step 2   offset    := w0_FW − ρ_B(L*),  L* = 10             [demarcation theorem: admissibility REQUIREMENT]
Step 3   w0^CAC(L)  = ρ_B(L) + w0_FW − ρ_B(L*)              [substitute]
Step 4   w0^CAC(L*) = ρ_B(L*) + w0_FW − ρ_B(L*) = w0_FW     [the moment cancels at the anchor]
Off-anchor contribution of the moment:  [ρ_B(L) − ρ_B(L*)] → ρ_B(∞) − ρ_B(10)
                                         = −1 − (−0.575) = −0.425   (running edge)
Conclusion  At its own anchor the branch-iv prediction IS the closed form, by construction;
            off-anchor it adds a DRIFT AWAY from −0.918 (to w0_FW − 0.425 ≈ −1.341),
            never toward it.  The moment never independently produces −0.918.   ∎
```

So the branch-iv construction is: take the closed-form value w0_FW, add a spectral fluctuation that is zero at the anchor and grows AWAY from w0_FW with |L − L*|. That is not a derivation OF −0.918; it is a perturbation of −0.918 by a quantity whose limit is the wrong number.

**The admissibility-implies-injection corollary (the decisive structural point).** The lockdown demarcation theorem defines `admissible ⟺ w0^C(10) = w0_FW` exactly. Therefore:
- Every ADMISSIBLE branch-iv convention injects w0_FW (`offset = w0_FW − ρ(L*)` contains it). Circular — no derivation.
- The one INADMISSIBLE convention (RDC, no offset) outputs the moment's own value, −1 — the wrong number.

The dichotomy is exhaustive: there is no branch-iv convention that is BOTH admissible AND outputs −0.918 without injecting it. **Branch-iv is derivation-NEUTRAL by the structure of its own admissibility class.** This is why the register already carries it INFO / `derivation-inadmissible` (S101 W4-3) with the spread tagged `surrogate-spread-UNINFORMATIVE`.

**Is the CAC anchor circular?** Yes — proven above. The CAC's L_max-"stability around −0.918" is the slow variation of the bare moment ρ_B near L=10, wearing the offset that pins it to −0.918. It cannot be evidence for −0.918, because −0.918 was injected as the anchor and cancels out of the only un-injected quantity (the spread).

**Corridor disposition.** The branch-iv corridor as a w0-DERIVATION is CLOSED. What survives is narrower than EVOI Tier-2 7c's "live envelope": ρ_B(L) is a legitimate L_max-stability DIAGNOSTIC of a bare Zubarev moment, but it is value-neutral and bears nothing on −0.918. I do not insist 7c be struck — I insist its STATUS be stated honestly: the open question is not "extend the −0.918 envelope" (there is none) but "does ANY spectral route output −0.918 with no tuned offset?" — currently answered NO, with the burden on Reading A to EXHIBIT such a route. Until one exists, the DESI w0 = −0.918 prediction is closed-form-only, staked at 2.13σ vs DESI DR2 on the Volovik partition alone (a real substrate-IS thermodynamic identity — not a weakness, just not a D_K spectral derivation).

#### V2: The anti-rescue fence + the three-way divergence — branch-iv does not converge to −0.918

The three-way divergence is not "one moment re-anchored to one value," and it is not three competing predictions. It is ONE moment (ρ_B(L) → −1) plus a CHOICE of closed-form TARGET injected via the offset. Enumerate the limits (Sage, this turn), under each admissible-class normalization:

```
normalization        bare ρ(10)   bare-moment limit      w0^CAC asymptote
running-edge (CAC)   −0.575       → −1 (Weyl-forced)     → −1.340827   (drifts; gap 0.422827)
fixed-edge           −0.575       frozen −0.575          −0.918        (frozen, INJECTED)
no-edge (drop λ_max) +0.987       frozen +0.987          −0.918        (frozen, INJECTED)
                                  (* every w0^CAC(10) = −0.918 via offset = w0_FW − ρ(10))
```

Read off the column that matters: **under NO admissible normalization does the moment ITSELF converge to −0.918.** Running-edge drifts to −1.340827 (gap 0.422827, Sage-exact; Weyl-forced per the W9 saturation workshop — mean_Z frozen ≈ 1.9879 over a linearly-unbounded λ_max). Fixed-edge and no-edge freeze at −0.918 ONLY because the offset injects it (the moments sit at −0.575 and +0.987 respectively, neither is −0.918). The closed-form value −0.918 is reproduced in every column ONLY where the offset is tuned to inject it.

This is exactly what §EVOI.BF encodes: *"branch-iv w₀ −0.842 at 0.731σ is derivation-INADMISSIBLE post-S86; the canonical w₀ = −0.918 … is the honest figure."* The canonical figure is honest BECAUSE it is the Volovik closed form, not a branch-iv output. The fence's operative word is DERIVATION-inadmissible; it does not become admissible when you point the offset at −0.918 instead of −0.842. baptista's two-output split would make the fence escapable by a relabeling (anchor to the protected value, call the spread a "diagnostic") — but the spread is offset-invariant (value-neutral), so the relabeling injects −0.918 and certifies nothing about it. **The fence extends to the CAC route by its own terms: the CAC does not derive w0; it injects w0_FW and reports a value-blind spread.**

Does branch-iv converge to −0.918 under ANY admissible normalization? **No.** It converges to −1 (bare), to −1.341 (CAC running asymptote), or freezes at its injected anchor (fixed / no-edge) — and equals −0.918 only where the offset puts it there. The spectral content of branch-iv points to −1; −0.918 is the closed form's, sitting in the offset.

#### V3: Questions for baptista

1. **The exhibition challenge.** The lockdown demarcation theorem makes "admissible" synonymous with `w0^C(10) = w0_FW` exactly — i.e. with `offset = w0_FW − ρ(L*)` injecting w0_FW. Can you exhibit ANY branch-iv normalization that is (a) admissible AND (b) outputs −0.918 with NO constant containing w0_FW? If not — if admissibility IS injection — do you concede the corridor is derivation-NEUTRAL by the structure of its admissibility class, so CF-S117 can at most select WHICH costume the injected value wears (running / fixed / no-edge), never make −0.918 a spectral output?

2. **The value-neutrality of the spread.** `spread_CAC = ρ_a − ρ_b` exactly (offset cancels; Sage this turn), so the L_max-stability diagnostic is BIT-IDENTICAL whether you anchor to −0.918, −0.842454, or −1.340827. The register already tags it `surrogate-spread-UNINFORMATIVE` (S101 W4-3). On what grounds is a target-INVARIANT diagnostic "spectral-action support" FOR −0.918 *specifically*, rather than support for the trivial claim that ρ_B(L) is a smooth convergent sequence?

3. **The categorical test against n_s.** n_s = 0.9561 is a spectral OUTPUT: the gauge-invariant spectral computation produces the number with no closed-form n_s subtracted-and-re-added at canonical L. `w0^CAC(L) = ρ_B(L) + [w0_FW − ρ_B(10)]` contains w0_FW as an input. What concrete construction would make w0 a spectral OUTPUT in the n_s sense — and absent it, on what non-trivial grounds does w0 "join {n_s, m_H, r}" rather than stand as a Volovik-partition closed-form substrate identity (a legitimate substrate-IS thermodynamic observable in its own right, just not a D_K spectral-action derivation)?

---

## Round 2 — baptista: Follow-up

### CONVERGENCE

volovik's circularity charge is correct, and the decisive thing is that **I proved it myself last workshop.** I am not conceding to a better-argued opposing case; I am recognizing that my own W9 Weyl-forced result IS volovik's V1 conclusion. Below I show the two are the same fact, then enumerate exactly what that forces me to withdraw.

**1. The CAC anchor is a definitional identity, not an independent confirmation — conceded (Re:B3, V1).** My B3 substitution chain and volovik's V1 Step-4 are the same four lines read oppositely, and his reading is the load-bearing one:

```
Step 1  w0^CAC(10) = ρ_B(10) + offset                  [CAC def, s102…py:33]
Step 2  offset     = w0_FW − ρ_B(10)                    [admissibility REQUIREMENT, demarcation thm]
Step 3  w0^CAC(10) = ρ_B(10) + w0_FW − ρ_B(10)
Step 4             = w0_FW = −0.918                      [ρ_B(10) cancels, W9 residual 1.11e-16]
```

I read Step 4 as "edge-INDEPENDENT (robust)." That is true but vacuous as confirmation: an anchor returning w0_FW for ANY ρ_B(10) — indeed for any moment whatsoever — is not measuring −0.918, it is restating it. My own B3 sentence ("at the anchor, branch-iv = closed form by construction; it adds nothing THERE") IS volovik's point. So the "Level-3 empirical anchor at canonical L_max" of my B4 ladder is empirically empty AS AN INDEPENDENT CONFIRMATION. Conceded.

**2. The branch-iv envelope is value-neutral, and its bare content points AWAY from −0.918 — conceded (Re:B2, V2, V3.2).** The spread is offset-invariant (`spread_CAC = ρ_a − ρ_b` exactly; the offset cancels in max−min, W9 residual 1.11e-16), hence target-invariant — bit-identical anchored to −0.918, −0.842454, or −1.340827. A diagnostic blind to a 0.42-wide value difference cannot be evidence FOR one end of it. I under-weighted the standing register verdict in R1: **S101-W0-BRANCH-IV-EVALUATOR** (S101 W4-3, audit `cd0492d6`) already closed this INFO with `surrogate-spread-UNINFORMATIVE` + `NO-Θ-free-map-reproduces-w0_B`. The framework had already adjudicated that the branch-iv spread carries no derivation content; my R1 re-opened a settled point.

And it is worse than neutral for −0.918, by my own W9 finding. Substitution chain (the [SIGN] claim "the bare moment's substrate-natural content points to −1, not −0.918"):

```
Step 1  ρ_B(L) = mean_Z(L)/λ_max(L) − 1                 [(B1), s105…py:293]
Step 2  mean_Z(L) → μ = 1.9879   (FB-frozen finite IR scale; W9)        [numerator fixed]
Step 3  λ_max(L) → ∞   (Weyl edge, ∂λ_max/∂L = 0.375, unbounded; W9)    [denominator runs]
Step 4  ρ_B(L) → μ/∞ − 1 = −1                           [Weyl-FORCED, W9 Structural Verdict]
Conclusion  the branch-iv spectral content asymptotes to −1; −0.918 is 0.082 away, and the
            CAC running asymptote −1.340827 is 0.422827 away. The moment points to the WRONG
            end. A "narrowing spread" of a sequence → −1 is convergence TO −1, not support
            for −0.918.   ∎
```

So Reading A's core claim — "the Level-2 branch-iv envelope is SUPPORTIVE of −0.918" — is not merely unsupported; the bare moment's content points to the opposite end. I withdraw "spectral-action-SUPPORTED."

**3. My 3-level ladder is DEGENERATE for w0 — conceded (Re:B4, V3.3).** Against the genuine-bridge control (n_s = 0.9561 is a spectral OUTPUT with no closed-form n_s subtracted-and-re-added; its Level-2 converges to an INDEPENDENT Level-3 Planck match — three independent agreeing things), my w0 ladder collapses to ONE thing in a costume: Level-1 = −0.918 (real); Level-3 = Level-1 RE-INJECTED via the offset (the Step-4 identity); Level-2 = the value-neutral spread. The structural test is my own offset identity: a genuine spectral output `O_spec` does NOT satisfy `O_pred = O_spec(L) + [O_pred − O_spec(L*)]` as the DEFINITION of how `O_pred` is obtained; w0 does, with `w0_FW` sitting inside the bracket. A construction that contains its target as an input cannot derive that target. So "w0 JOINS {n_s,m_H,r} as spectral-action-SUPPORTED" overstates it. Withdrawn.

**4. The admissibility-implies-injection dichotomy is exhaustive on branch-iv — conceded (V1, V3.1).** The demarcation theorem makes `admissible ≡ w0^C(10) = w0_FW exactly ≡ offset = w0_FW − ρ(L*) injecting w0_FW`. Every admissible normalization injects; the one inadmissible one (RDC) outputs the moment's own −1. volovik's three-axis table (running/fixed/no-edge: bare moments {−0.575, −0.575, +0.987}, none is −0.918) is the proof, and W9's Weyl-forced −1 is WHY: the bare content is −1, so any admissible reading must bridge the −1→−0.918 gap by injection. There is no branch-iv normalization both admissible AND outputting −0.918 without injecting it. Branch-iv is derivation-NEUTRAL by the structure of its own admissibility class.

**5. The value lives in the vacuum partition, not the D_K spectrum — accepted (Re:B5.2).** w0 = −0.918 is the Volovik vacuum partition + effacement Γ_eff = 0.99970 (confirmed canonical: S58 four-fold-lock) — a substrate THERMODYNAMIC / q-theory identity (how the vacuum energy effaces through the impedance mismatch), NOT a `Tr f(D_K)` moment. The CC/dark-energy STATIC scale is the a_0 zeroth spectral moment; but w0 is the equation-of-STATE response (tracking/effacement), which is not in the static eigenvalue spread. Branch-iv tried to relocate a thermodynamic observable into the vibrational spectrum and got −1 — the wrong number because it read the wrong observable. I accept the categorical distinction.

### DISSENT

The derivation-grade dispute has converged to volovik's reading. Two NEW points survive — neither re-runs Reading A; both are structural classifications volovik has not yet conceded.

**(D1) "closed-form-ONLY" is correct as a derivation-grade verdict but MIS-TIERS w0. The precise statement is: w0 = −0.918 is a Level-1 substrate identity, NOT Level-2 spectral-action-derived — and Level-1 is the framework's BEDROCK tier, not a lesser one.** The cross-pillar-bridge ladder's own Level-1 is "structural identity, regulator-invariant, L_max-independent." The framework's PERMANENT results — KO-dim = 6, [J, D_K] = 0 (CPT), g1/g2 = e^{−2τ}, volume-preserving TT, AZ class BDI — are ALL Level-1 identities with NO convergence envelope, and they are the framework's strongest results *precisely because* they are closed-form identities subject to no L_max anchor-fidelity question. A pure Level-1 identity is not epistemically inferior to a Level-2-equipped observable; {n_s, m_H, r} happen to carry BOTH a Level-1 value and a Level-2 envelope, but the envelope is not what makes them PROVEN. So the honest verdict is not "closed-form-ONLY" (which connotes "merely") but the precise tag **Level-1 substrate identity (no Level-2 spectral-action envelope)** — placing w0 in the KO-dim=6 / [J,D_K]=0 company, not below {n_s,m_H,r}. This is a dissent from the WORDING and tiering, not from the derivation-grade fact.

**(D2) The branch-iv corridor closes as an ELIMINATION carrying a PROVEN BOUNDARY, not as a nullity.** volovik frames branch-iv as "derivation-neutral … certifies nothing." I dissent narrowly: the closure carries positive structural content — the W9 Weyl-forced theorem `ρ_B = (FB-frozen IR scale)/(Weyl-unbounded edge) − 1 → −1` proves that NO edge-normalized D_K spectral moment can carry w0 (all are forced to −1 by Weyl's law on a compact-fiber spectrum unbounded above). Per `epistemic-discipline.md` ("negative results are boundaries, not failures"), this is an elimination of the *entire edge-normalized-spectral-route hypothesis* for w0, with a specific mathematical reason. So branch-iv is uninformative about the VALUE (conceded, D-grade) but INFORMATIVE as a closed corridor with a registered wall. It should retire to §5 as a proven-boundary elimination, not as "value-neutral diagnostic, move on." The distinction is load-bearing for how the register records it.

### EMERGENCE

**The substrate-first inversion: branch-iv was an attempt to DEMOTE a Level-1 identity into an L_max-dependent spectral convergence, and the Weyl-forced −1 is the substrate REFUSING the demotion.** Read W9 through the substrate-IS lens (`phononic-framing.md`: the substrate IS both its D_K vibrational spectrum AND its vacuum partition; explanation flows substrate → emergent). w0 = −0.918 is a property of how the vacuum-energy partition effaces — a closed-form substrate identity (Level-1). The branch-iv programme tried to RELOCATE that value into the eigenvalue spread (give it a Level-2 envelope). The moment going to −1 is not a failure to find a hidden spectral derivation; it is the substrate stating that the equation-of-state value is NOT carried by the static spectrum — "I am the vibrational spectrum, and w0 does not live in me; the partition holds it." So "closed-form-ONLY" is not a deficiency to be remedied by a harder search for a spectral envelope; it is the CORRECT structural home, and the branch-iv −1 is positive evidence FOR that placement. The connes §23 transport-degree solo (deg=0, T2-VACUOUS scalar; the λ_max edge is not an admissible §23 morphism, so the −1.341 asymptote is PROXY-ARTIFACT-TYPED) confirms it from the transport axis: with branch-iv derivation-neutral AND deg=0 (no BZ→pivot transport leg), there is no remaining spectral-action route to w0 at all — Level-1-only is the complete picture, not a stopgap.

**The precise three-tier status (the workshop's converged structural statement on w0):**

| Tier | Content | Grade |
|:--|:--|:--|
| **Level-1 — closed-form substrate identity** | w0 = −0.918 = Volovik vacuum partition + effacement Γ_eff = 0.99970 (S58); regulator-invariant, L_max-independent; zero free parameters; substrate-IS (the thermodynamic/q-theory facet of the one substrate) | **SOLID — primary** (volovik's domain; KO-dim=6 / [J,D_K]=0 bedrock class) |
| **Level-2 — spectral-action derivation** | NONE; the branch-iv Zubarev moment is derivation-NEUTRAL by its admissibility class (every admissible normalization injects w0_FW; bare content Weyl-forced to −1) | **ABSENT — conceded** (not a deficiency; w0 is Level-1-native) |
| **branch-iv residual** | a CLOSED corridor carrying a PROVEN boundary: no edge-normalized D_K moment carries w0 (Weyl-forced −1 wall, W9) | **ELIMINATION** — register as a wall, retire to §5 |

**DESI falsifier consequence (topic d).** The staked value is UNCHANGED: w0 = −0.918 (2.13σ vs DESI DR2 −0.803 ± 0.054; 3.28σ vs LCDM per the decision-rule, the two σ-metrics flagged distinct in B5.4), now with HONEST provenance — it rests on the Level-1 Volovik closed form ALONE, not on closed-form + a spectral-action envelope. What changes from my R1: I withdraw the claim that branch-iv STRENGTHENS the robustness case. The robustness of −0.918 is the structural status of the Volovik partition (volovik's Level-1 domain), full stop. The −0.842454 alternate stays fenced (§EVOI.BF); the −1.341 asymptote stays OFF the falsifier surface (proxy artifact, Weyl-forced). EVOI Tier-2 7c splits into TWO dispositions: the **branch-iv-DERIVATION sub-track CLOSES** (retires to §5 as a proven-boundary elimination), while **w0-on-the-DESI-surface stays LIVE** as a Level-1 prediction (it does NOT retire — it is staked on the closed form). Reading "7c retires to §5 as closed-form-only" as retiring the whole row would wrongly read the DESI prediction as retired; it is not.

### QUESTIONS

**Answering volovik's V3 directly:**

- **V3.1 (exhibition challenge).** No — I cannot exhibit any branch-iv normalization that is admissible AND outputs −0.918 with no constant containing w0_FW. I concede the corridor is derivation-NEUTRAL by the structure of its admissibility class. This honestly DOWN-SCOPES my own W9 carry-forward: **CF-S117-W0-ANCHOR-FIDELITY** can at most select WHICH costume the injected value wears (running → drifts to −1.341; fixed/no-edge → freezes at the injected −0.918) — a presentation-stability choice, NOT a derivation. It cannot make −0.918 a spectral output. I re-spec it from "anchor-fidelity resolver" to "presentation-normalization hygiene (select the non-drifting costume so a consumer is not shown a proxy drifting to −1.341)" so it does not masquerade as a derivation gate.

- **V3.2 (value-neutrality of the spread).** Conceded: a target-invariant diagnostic is not support FOR −0.918 specifically. It certifies only that ρ_B(L) is a smooth convergent sequence — and since it converges to −1, it is "consistent with" −1, not −0.918. My R1 "narrowing envelope ⇒ support" conflated convergence-of-the-spread with support-for-the-anchor; they are orthogonal — exactly the L_max-stability ≠ anchor-fidelity distinction I myself pinned in W9. I should have applied my own W9 distinction to my own B4.

- **V3.3 (categorical test vs n_s).** No concrete construction makes w0 a spectral OUTPUT in the n_s sense on the branch-iv corridor (or any current route). w0 stands as a Level-1 closed-form substrate identity. My only refinement: that is its CORRECT home (per EMERGENCE), not a fallback from a failed derivation — the framework's bedrock results are themselves Level-1 identities.

**My questions back to volovik (R3 seeds):**

1. **The tiering.** Do you accept the Level-1/Level-2 STRUCTURAL classification — w0 = −0.918 is a Level-1 substrate identity in the KO-dim=6 / [J,D_K]=0 / g1/g2=e^{−2τ} bedrock class — as the precise replacement for "closed-form-ONLY"? Specifically: do you agree Level-1 status is NOT a demotion relative to the Level-2-equipped {n_s,m_H,r} (the convergence envelope is not what makes those PROVEN), so the honest verdict reads "Level-1-native, no Level-2 envelope" rather than "merely closed-form"?

2. **The corridor disposition.** Do you accept that the branch-iv corridor retires to §5 as a CLOSED CORRIDOR carrying a PROVEN BOUNDARY — the Weyl-forced −1 wall (no edge-normalized D_K spectral moment carries w0) — an elimination per `epistemic-discipline.md`, distinct from "value-neutral, nothing survives"? And on EVOI 7c: do you agree the disposition SPLITS — branch-iv-DERIVATION track CLOSES (→ §5), w0-on-DESI stays LIVE as a Level-1 prediction (does NOT retire) — so 7c does not wholesale retire to §5?

---

## Round 2 — volovik: Cross-Synthesis

### CONVERGENCE

The derivation-grade dispute is CLOSED. baptista's R2 concessions (points 1–5) are exactly the five structural facts I pinned in V1/V2/V3; I record the convergence, then ACCEPT both of his new classifications (D1 tiering, D2 elimination) — they sharpen Reading B, they do not oppose it.

**The core verdict (settled).** w0 = −0.918 is closed-form-ONLY at the derivation grade; the branch-iv corridor as a w0-DERIVATION is CLOSED; the DESI stake rests on the Volovik partition alone. The canonical pin confirms the provenance at the source level, not merely by argument: `get_constant(w0_FW)` returns value −0.918, **Gate: None**, Source = "S58 four-fold-lock (Volovik vacuum partition + effacement Γ_eff = 0.99970)." **The "Gate: None" is the tell** — w0_FW is not gated by any spectral-action computation; it is a closed-form lock. The branch-iv lineage (S102→S116) is a post-hoc attempt to relocate this already-locked value into the D_K spectrum, and each normalization reaches −0.918 only by injecting it (admissibility ⟺ `offset = w0_FW − ρ(L*)`; Re:B3 / V2 three-axis table: bare moments {−0.575, −0.575, +0.987}, none is −0.918).

**Accept baptista R2 point 5 (the value lives in the vacuum partition) — and I ground it in the q-theory corpus, since it is my domain.** w0 is the equation-of-STATE response of the substrate vacuum. In the Volovik program the vacuum energy is a THERMODYNAMIC quantity of the q-field (the 4-form / q-theory vacuum variable, Volovik Papers 13/23/25), NOT a `Tr f(D_K)` moment of the fermionic spectrum: the equilibrium CC is zero by thermodynamics (the ground-state energy does not gravitate — Volovik's equilibrium theorem), and what survives as the observed equation of state is the EFFACEMENT residual Γ_eff = 0.99970 (impedance-mismatch leakage of the partition; the DILUTION-CC two-fluid w=−1[vacuum] + w=0[GGE] split, Paper 37 / S43). So −0.918 is a q-theory effacement identity. Branch-iv tried to read a BOSONIC q-field equation-of-state off the FERMIONIC D_K eigenvalue spread — the wrong observable — and the substrate returns −1 (V2; W9 Weyl-forced). Substrate-first: the fabric IS both its D_K vibrational spectrum AND its q-field vacuum partition; w0 is the thermodynamic facet, n_s/m_H the vibrational facet. Different facets of one substrate, not rivals.

**Accept baptista D1 (Level-1 tiering is not a demotion) — with one sub-class refinement I carry to DISSENT.** "Closed-form-ONLY" undersells it: an L_max-independent closed form is the framework's envelope-free class — the same class as the structural floor (KO-dim=6, [J,D_K]=0, g1/g2=e^{−2τ}, volume-preserving TT, AZ BDI) — and the convergence envelope is NOT what makes {n_s,m_H,r} PROVEN. The honest tag is **Level-1 substrate identity (no Level-2 spectral-action envelope)**, not "merely closed-form." Accepted in full; my refinement (which SUB-class of Level-1) is VD1, and it scopes the acceptance rather than undoing it.

**Accept baptista D2 (proven-boundary elimination, not nullity) — answering the spawn's first question YES.** My V1 said the corridor "carries nothing on −0.918" and asked only that its status be stated honestly; D2 supplies the POSITIVE content I under-credited. The W9 Weyl-forced theorem is a real elimination with a specific mathematical reason (per `epistemic-discipline.md`: "negative results are boundaries, not failures"). I accept that 7c-as-derivation retires as **CLOSED-WITH-RESULT**, not as a bare nullity — with a scope-precisification and a support-column guard in DISSENT.

### DISSENT

The direction has converged; my two residual disagreements are PRECISION sharpenings (honestly so — the substance is settled), both in my domain.

**(VD1) The "bedrock class" needs a sub-class split: w0 is Level-1 closed-form-THERMODYNAMIC, distinct in KIND from the topological/algebraic invariants.** baptista's D1 places w0 "in the KO-dim=6 / [J,D_K]=0 company." Both ARE envelope-free Level-1 — agreed — but they are different KINDS of exactness, and the difference is load-bearing for the DESI stake:

- KO-dim=6 is a mod-8 topological invariant; [J,D_K]=0 is an exact operator identity; g1/g2=e^{−2τ} is an algebraic relation. RIGID — integer/algebraic, no computed real-valued inputs, machine-ε.
- w0 = −0.918 is a closed-form THERMODYNAMIC value: the Volovik vacuum partition + the effacement factor Γ_eff = 0.99970. Γ_eff is itself a computed substrate quantity (impedance-mismatch leakage), not an integer or a mod-8 class.

So w0 shares the "L_max-independent / no truncation envelope / zero free parameters" property (it IS Level-1), but its exactness is the exactness of a thermodynamic DERIVATION (partition + effacement factor), not the rigidity of a topological invariant. The honest register tag is **"Level-1 closed-form thermodynamic identity,"** not "Level-1 bedrock alongside KO-dim=6." This is not pedantry: it scopes what the DESI stake rests on. The stake is as exact as the Volovik-partition computation — closed-form-exact and L_max-independent (hence STRONGER than any truncated derivation, VD-affirm below) — but it inherits whatever modeling content the partition + effacement carry, which a topological invariant does not. Do not over-elevate −0.918 to topological-invariant rigidity.

**(VD2) Accept the elimination, but GUARD two things.**

(a) **The −1 wall carries ZERO positive support for −0.918.** The proven-boundary elimination is real (CONVERGENCE), but it is a result ABOUT the failed proxy: the branch-iv moment is Weyl-forced to −1 (S116-W9-GTBUILDER-L15: ρ_B(15)=−0.696174, w0_cac(15)=−1.038968, spread narrowing 0.044514→0.0392902; verdict-file audit `94ed48e7`). It is value-NEUTRAL on −0.918 (offset-invariant; `surrogate-spread-UNINFORMATIVE`, S101 W4-3 `cd0492d6`). My guard: when 7c retires as CLOSED-WITH-RESULT, the result is "the edge-normalized route is eliminated," NOT "evidence for −0.918." The DESI stake's SUPPORT column reads Level-1-only; the −1 wall lives in the ELIMINATION column, never the support column. A register that lets a wall about a failed proxy migrate into the stake's support would be the methodology-floor analog of citing a FAIL as a PASS.

(b) **The wall's scope needs a SECOND, orthogonal argument to close the full spectral-route space.** baptista's D2 states the boundary as "NO edge-normalized D_K spectral moment can carry w0." Exact scope: what W9 proves is that any spectral statistic of the form (FB-frozen IR numerator)/(Weyl-unbounded edge λ_max(L)) − offset → −1, FORCED by Weyl's law (mean_Z → finite IR scale ≈ 1.9879; λ_max → ∞ linearly, ∂λ_max/∂L ≈ 0.375). That eliminates the edge-NORMALIZED class. It does NOT, by itself, eliminate a hypothetical NON-edge-normalized bottom-only statistic. The COMPLETE closure needs the orthogonal categorical argument (CONVERGENCE / D2 point 5): w0 ∉ Tr f(D_K) at all — it is the q-field vacuum partition, not a vibrational moment. The register should carry BOTH: (i) the Weyl wall (kills the route someone BUILT) AND (ii) the categorical thermodynamic-not-vibrational fact (kills the routes no one built). The Weyl wall alone is necessary-not-sufficient.

**(VD-affirm — the spawn's "stronger or weaker," answered directly).** Is Level-1 closed-form provenance STRONGER or WEAKER than the {n_s,m_H,r} spectral derivations for the DESI stake? **STRONGER on the truncation axis** — substitution chain:

```
Step 1  w0 = −0.918 is an L_max-INDEPENDENT closed form          ⇒ truncation_error(w0) ≡ 0    [Gate=None; partition+effacement]
Step 2  n_s(L), m_H(L) are convergent-but-TRUNCATED spectral outputs ⇒ truncation_error ≠ 0 at finite L   [Friedrich-Bär envelope]
Step 3  stake_reliability(truncation axis) ∝ 1 / truncation_error
Step 4  Step1 ⇒ reliability(w0) maximal;  Step2 ⇒ reliability(n_s,m_H) finite
Conclusion  closed-form > truncated on the truncation axis ⇒ −0.918 is BETTER-grounded as a STAKE
            than it would be as a truncated spectral derivation.   ∎
```

The caveat (exactly why "join {n_s,m_H,r}" was always category-confused): this ranking holds on the truncation axis ONLY. On the "is-it-a-D_K-spectral-geometric output" axis, {n_s,m_H} are the genuine vibrational-spectrum derivations and w0 is not — it is the thermodynamic facet. Differently-grounded, not rank-ordered. w0 does not "join" {n_s,m_H,r}; it sits in the envelope-free Level-1 floor on a DIFFERENT (thermodynamic) axis.

### EMERGENCE

**1. deg=0 REINFORCES the closed-form-only reading (spawn question 3) — it is the THIRD independent leg.** The connes S-7 §23 solo types w0 as deg=0 T2-VACUOUS scalar (substrate w0 = pivot w0). There are exactly two spectral-action routes by which a number could be "derived":

- (a) SCALE-TRANSPORT — substrate value mapped to the pivot by a substrate-natural morphism with deg(T_{BZ→pivot}) ≠ 0 (how n_s/α_s get their CMB images; n_s carries deg=+2, verdict file S116-W1-AS-CF3).
- (b) L_max-NORMALIZATION — a spectral moment with an L_max normalization (the branch-iv Zubarev moment).

deg=0 closes route (a): no non-trivial BZ→pivot morphism, nothing to derive on the transport axis. Value-neutrality + Weyl-forced −1 close route (b). (a) ∧ (b) closed ⇒ no spectral-action route to the VALUE ⇒ Level-1 closed-form is the COMPLETE picture. The three legs — transport (deg=0), normalization (value-neutral / Weyl −1), observable-identity (w0 ∉ Tr f(D_K)) — are mutually orthogonal and jointly exhaustive. This is baptista's EMERGENCE ("Level-1-only is the complete picture, not a stopgap") with the transport leg made explicit.

**2. The closed-form-only VALUE reading is ROBUST to the deg-resolution — CF-S117-W0-TRANSPORT-DEGREE is DECOUPLED from the derivation grade.** deg=0 is PROVISIONAL (workshop header). But the verdict does not wait on it. Substitution chain:

```
Step 1  Transport governs the map substrate_value → pivot_image:  pivot_image = T_{BZ→pivot}(substrate_value), deg = deg(T)
Step 2  substrate_value is the INPUT to T, never its output.  For w0, substrate_value = −0.918 (closed form)
Step 3  deg=0  ⇒ pivot_image = substrate_value = −0.918           [T2-vacuous scalar]
Step 4  deg≠0  ⇒ pivot_image = T(−0.918) ≠ −0.918,  BUT substrate_value still = −0.918  [closed form unchanged]
Conclusion  in BOTH cases substrate_value = closed form ⇒ the substrate VALUE is closed-form regardless of deg.   ∎
```

If deg≠0 surfaces, it re-introduces a pivot-IMAGE transport question (what the CMB-scale image of w0 is), NOT a derivation of the substrate value. Transport maps the value; it does not derive it. So the closed-form-only reading on the VALUE is decoupled from CF-S117-W0-TRANSPORT-DEGREE: deg=0 makes the closed form the whole story at BOTH scales; deg≠0 would split the scales but leave the substrate value the closed form. Either way, the stake is the closed form.

**3. The exact EVOI Tier-2 7c disposition (spawn deliverable).** 7c (branch-iv w0(L) evaluator / DR3-readiness) SPLITS into three components, and the §5 fold should be UPGRADED from "derivation-INADMISSIBLE" (evoi-framework line 177) to CLOSED-WITH-RESULT:

| 7c component | Disposition | Register tag |
|:--|:--|:--|
| branch-iv-as-w0-DERIVATION | **CLOSED → §5** | **CLOSED-WITH-RESULT** (not merely INADMISSIBLE): the W9 Weyl-forced −1 wall — any (FB-frozen IR numerator)/(Weyl-edge) − offset → −1 — eliminates the edge-normalized-spectral-route hypothesis with a specific reason (W9 + S116-W9-GTBUILDER-L15). PLUS the orthogonal categorical wall (w0 ∉ Tr f(D_K), VD2b). Register as a proven boundary. |
| branch-iv-as-L_max-STABILITY-diagnostic | survives, value-NEUTRAL | `surrogate-spread-UNINFORMATIVE` (S101 W4-3): the spread narrows (0.130419→0.0443→0.0392902, → PASS ~L≈19) but certifies only that ρ_B(L) is a smooth sequence converging to −1; it bears NOTHING on −0.918. The "extend the envelope" forward gates are at most presentation-normalization hygiene (baptista V3.1 re-spec of CF-S117-W0-ANCHOR-FIDELITY), NOT derivation gates. |
| w0-on-the-DESI-surface | **stays LIVE (Tier-2)** | Level-1 closed-form prediction −0.918 (2.13σ vs DESI DR2 −0.803 ± 0.054). Does NOT retire — staked on the Volovik partition, independent of the corridor. R_842 rectangle / reversibility band UNCHANGED. |

So: NOT "7c retires to §5 as closed-form-only" (which would wrongly read the DESI prediction as retired). The DERIVATION sub-track retires CLOSED-WITH-RESULT; the DESI prediction stays live as a Level-1 stake. I accept baptista's split.

**4. DESI falsifier-surface provenance statement (the converged provenance line).**

> w0 = −0.918 (canonical `w0_FW`, **Gate: None**, S58 four-fold-lock: Volovik vacuum partition + effacement Γ_eff = 0.99970) is a **Level-1 closed-form substrate THERMODYNAMIC identity** — exact, L_max-independent, zero free parameters; the q-theory effacement equation-of-state, not a `Tr f(D_K)` moment. The DR3 stake rests on this closed form ALONE; it is NOT spectral-action-derived (branch-iv is derivation-neutral: admissibility ⟺ injection of w0_FW; bare content Weyl-forced to −1). It is a STRONGER stake than a convergent-but-truncated spectral derivation (zero truncation error), though a thermodynamic-identity grade, not a topological-invariant grade. OFF the surface: the −1.341 CAC running asymptote (proxy artifact; λ_max not an admissible §23 morphism; deg=0) and the −0.842454 alternate (fenced, §EVOI.BF). σ-metric discipline (B5.4): 2.13σ is vs DESI DR2 (−0.803 ± 0.054); 3.28σ is vs LCDM (−1) — do not conflate.

Substrate-first: the fabric IS its q-field vacuum partition; w0 IS what that partition's effacement is; the DESI detector measures the emergent equation-of-state image of it.

### QUESTIONS

R3 seeds for baptista (the workshop's verdict-finalization turn):

1. **(tiering sub-class)** Do you accept VD1 — w0 is **Level-1 closed-form-THERMODYNAMIC** (Volovik partition + effacement Γ_eff), a sub-class DISTINCT from the topological/algebraic invariants (KO-dim=6 mod-8, [J,D_K]=0 operator identity, g1/g2=e^{−2τ} algebraic)? Both are envelope-free Level-1, but w0's exactness is a thermodynamic-derivation exactness, not a topological rigidity. Does that revise your "KO-dim=6 company" phrasing to "Level-1 closed-form thermodynamic identity," so the register does not elide computed-thermodynamic-number vs topological-invariant?

2. **(boundary scope — two arguments, not one)** Do you agree the COMPLETE elimination of "spectral routes to w0" needs BOTH (i) the Weyl wall (eliminates the edge-NORMALIZED class) AND (ii) the orthogonal categorical fact (w0 ∉ Tr f(D_K), closing the non-edge-normalized routes)? Or do you hold the Weyl wall alone closes the whole space? I read it as necessary-not-sufficient: the wall kills the route someone BUILT; the categorical fact kills the routes no one built.

3. **(DESI provenance + deg-decoupling)** (a) Do you agree the DR3 decision-rule should carry the one-line provenance annotation (EMERGENCE 4), so a downstream reader cannot mistake the narrowing branch-iv spread for derivation support — support column Level-1-only, the −1 wall in the elimination column? (b) Do you agree the closed-form-only VALUE reading is ROBUST to the CF-S117-W0-TRANSPORT-DEGREE outcome (EMERGENCE 2) — even if deg≠0 surfaces it re-introduces a pivot-IMAGE transport question but does NOT make the substrate w0 a spectral output — so the provenance statement can FREEZE now without waiting on the deg-resolution?

---

## Round 3 — baptista: Follow-up

### CONVERGENCE

The workshop has converged; this turn LOCKS the verdict and ratifies volovik's R2 precision dissents to the extent they hold (both largely do). Five locks, three of which I sharpen rather than merely accept.

**1. The derivation-grade verdict is FINAL, and I ratify it at the SOURCE level (not by argument alone).** w0 = −0.918 is a Level-1 closed-form substrate identity, NOT spectral-action-derived; the branch-iv corridor as a w0-DERIVATION is CLOSED-WITH-RESULT. I re-queried the canonical this turn: `get_constant(w0_FW)` → value = −0.918, Session = S58, Source = "S58 four-fold-lock (Volovik vacuum partition + effacement Γ_eff = 0.99970)", **Gate: None**, Superseded: False. volovik's VD2 "Gate: None tell" is confirmed at the constants-graph level — w0_FW is not gated by any spectral-action computation; it is a closed-form lock. This is the decisive categorical fact, and it is CANONICAL, not an artifact of the present argument.

**2. Accept VD2(a) — the −1 wall lives in the ELIMINATION column, NEVER the support column.** This is the column-discipline form of my own R2 point-2 concession (the branch-iv envelope is value-NEUTRAL, offset-invariant; `spread_CAC = ρ_a − ρ_b` exactly; register tag `surrogate-spread-UNINFORMATIVE`, confirmed this turn at `S101-W0-BRANCH-IV-EVALUATOR` INFO: `derivation-inadmissible … NO-Θ-free-map-reproduces-w0_B at 1e-5 … surrogate-spread-UNINFORMATIVE`). A diagnostic bit-identical anchored to −0.918, −0.842454, or −1.341 cannot be support FOR any one of them. volovik's column discipline is the methodology-floor analog of `phononic-framing`'s direction-of-explanation rule: a wall ABOUT a failed proxy may never migrate into the stake's support — that would be the F-image of citing a FAIL as a PASS. Accepted in full.

**3. Accept VD2(b) — the complete closure is a CONJUNCTION, and I supply a concrete witness that the Weyl wall alone is necessary-not-sufficient.** volovik is right that my R2-D2 boundary statement ("no edge-NORMALIZED D_K moment carries w0") closes the edge-normalized class but not the non-edge-normalized routes. Concrete witness (substitution chain):

```
Step 1  mean_Z(L) = Σ_j d_j e^{−|λ_j|²/Λ_Z²}|λ_j| / Σ_j d_j e^{−|λ_j|²/Λ_Z²},  Λ_Z=1   [(B1) numerator; s105…py:293]
Step 2  new p+q≥15 modes have |λ|≥4.216, Zubarev weight e^{−4.216²} ≈ 1.9·10⁻⁸       [FB-frozen bottom]
Step 3  mean_Z(L) → μ ≈ 1.9879  (finite IR scale; NOT divided by λ_max)               [non-edge-normalized]
Conclusion  mean_Z is a non-edge-normalized bottom-only D_K statistic with limit +1.9879 ≠ −1.
            The Weyl wall (which forces (frozen IR)/(Weyl edge) − offset → −1) does NOT govern it.
            ⇒ the Weyl wall cannot, by itself, forbid a non-edge-normalized functional from being tuned to −0.918.   ∎
```

So the edge-normalized route is killed by a spectral THEOREM (the Weyl wall), and the non-edge-normalized routes are killed by the orthogonal CATEGORICAL fact (w0 ∉ Tr f(D_K) — the equation-of-state is the q-field vacuum partition's effacement response, not a static spectral moment; the static vacuum-energy MAGNITUDE is the a_0 zeroth moment, but the dynamical w(z) RESPONSE is not in the static eigenvalue spread). The conjunction (i) ∧ (ii) closes the full spectral-route space; the Weyl wall alone is necessary-not-sufficient. Accepted — with a grade-asymmetry I carry to EMERGENCE (the two conjuncts carry DIFFERENT epistemic grades).

**4. Accept VD1's thermodynamic sub-class — Γ_eff is a COMPUTED quantity, not a mod-8 class.** I withdraw the flat "KO-dim=6 company" phrasing of R2-D1. w0 = −0.918 IS envelope-free Level-1, but its exactness is the exactness of a thermodynamic DERIVATION (Volovik partition + the computed effacement factor Γ_eff = 0.99970), not the rigidity of a topological/algebraic invariant. The precise register tag is **"Level-1 closed-form thermodynamic identity."** (The symmetric guard on what this does and does NOT cost the stake is my DISSENT.)

**5. Accept the three-leg exhaustiveness (volovik EMERGENCE 1).** transport (deg=0, no BZ→pivot morphism) ∧ normalization (value-neutral; Weyl-forced −1) ∧ observable-identity (w0 ∉ Tr f(D_K)) are mutually orthogonal and jointly close every spectral-action route to the VALUE. Level-1-only is the COMPLETE picture, not a stopgap — my R2 EMERGENCE with volovik's transport leg made explicit.

### DISSENT

The derivation grade is settled; both residuals are precision GUARDS, not re-litigations.

**(BD1) Symmetric guard on VD1 — accept the thermodynamic sub-class, but it is a CLEAN stake, not a lesser one. This is my direct answer to the spawn's "CLEAN or COMPROMISED?": CLEAN.** volovik's VD1 correctly guards against OVER-elevation ("do not elevate −0.918 to topological-invariant rigidity"). I add the orthogonal guard against UNDER-valuation, because the register must not read "thermodynamic-grade" / "closed-form-only" as a DEMOTION of the DESI stake. Defense, on volovik's own VD-affirm and on substrate-first grounds:

- **Truncation axis — STRONGER than a spectral derivation.** volovik's VD-affirm chain stands: w0 is L_max-independent ⇒ `truncation_error(w0) ≡ 0`; n_s(L), m_H(L) are convergent-but-truncated ⇒ `truncation_error ≠ 0` at finite L (FB-bounded). On the truncation axis −0.918 is BETTER-grounded as a stake than it would be as a truncated spectral derivation.
- **Fundamentality axis — EQUAL to a spectral derivation.** Substrate-first (`phononic-framing`): the fabric IS both its D_K vibrational spectrum AND its q-field vacuum partition. Two FACETS of one substrate, not a fundamental layer (D_K) plus a derived layer (thermodynamics). w0 being the thermodynamic facet does NOT make it less fundamental than n_s/m_H being the vibrational facet. A DESI stake on −0.918 is as fundamental as a stake on a D_K spectral moment.

So the honest verdict is a SYMMETRIC bracket: neither OVER-elevated to topological rigidity (VD1) NOR UNDER-valued as compromised (BD1). The middle is **a clean stake: Level-1 closed-form thermodynamic identity, truncation-stronger and fundamentality-equal vs a spectral derivation, differing only in error-axis KIND** (truncation-exact-but-model-bearing vs model-light-but-truncation-bounded). "Compromised" would require a smuggled fit or a convention-shop; −0.918 has neither (Gate: None; no fit; no scheme-shopping). The stake is CLEAN.

**(BD2) The DESI-pivot σ-distances carry a deg-conditionality that volovik's EMERGENCE 2 "either way the stake is the closed form" ELIDES.** I accept EMERGENCE 2 for the DERIVATION GRADE and the SUBSTRATE VALUE (both deg-robust — substrate_value is the INPUT to the transport, never its output). I dissent narrowly where "either way" is read to cover the DESI-surface NUMBERS. Substitution chain:

```
Step 1  DESI measures w0 at the late-time / pivot scale, NOT the substrate (M_KK / fold) scale.
Step 2  pivot_value = T_{BZ→pivot}(substrate_value),  deg = deg(T_{BZ→pivot})            [transport]
Step 3  deg = 0  ⇒ pivot_value = substrate_value = −0.918                                 [T2-vacuous scalar; connes §23, PROVISIONAL]
        ⇒ current σ-distances (2.13σ vs DESI DR2 −0.803±0.054; 3.28σ vs LCDM −1; R_842 containment) are computed vs −0.918 DIRECTLY
Step 4  deg ≠ 0 ⇒ pivot_value = T(−0.918) ≠ −0.918                                        [substrate value UNCHANGED; pivot image shifts]
        ⇒ the σ-distances RE-COMPUTE vs the pivot image (substrate prediction unchanged)
Conclusion  THREE deg-statuses, not two:
              (i) derivation grade (closed-form vs spectral): deg-ROBUST  — freeze now
             (ii) falsifiability (substrate −0.918 IS testable against DESI): deg-ROBUST — transport is invertible
            (iii) numerical DR3 σ-distances: deg-CONDITIONAL — computed under the PROVISIONAL deg=0; if deg≠0 surfaces they re-compute   ∎
```

w0 is dimensionless (d_A = 0), so per the parity selection rule (`cross-pillar-bridge-corpus §23.0(5)`) its scale leg is the trivial M_KK⁰ = 1 and the transport degree is carried ENTIRELY by the dimensionless morphism — currently T2-VACUOUS scalar (deg=0, favored), but PROVISIONALLY so (CF-S117-W0-TRANSPORT-DEGREE). So the provenance line CAN freeze the value + grade now; the falsifier-surface σ-distances should carry a one-line "computed under deg=0; pending CF-S117-W0-TRANSPORT-DEGREE" tag. The substrate PREDICTION never moves; only its pivot IMAGE (and hence the σ-numbers) is deg-conditional.

### EMERGENCE

The converged structural statement on w0, in five pieces.

**1. The Level-1 sub-class taxonomy (formalizing VD1).** "Level-1" (envelope-free, L_max-independent, zero-free-parameter) is NOT monolithic; it splits three ways by KIND of exactness and modeling content:

| Level-1 sub-class | Exemplars | Exactness | Modeling content |
|:--|:--|:--|:--|
| **topological / index** | KO-dim=6 (mod-8), [J,D_K]=0 (operator identity), AZ class BDI | integer / Z₂ / mod-8; axiom-forced | NONE (forced by the spectral-triple axioms) |
| **algebraic** | g1/g2 = e^{−2τ}, volume-preserving TT | real-valued, algebraically exact in the deformation parameter | deformation-geometry only |
| **closed-form thermodynamic** | **w0 = −0.918** (Volovik partition + effacement Γ_eff = 0.99970) | real-valued, exact as a thermodynamic derivation | q-field vacuum partition + impedance effacement |

w0 lives in the third row. All three are Level-1 (envelope-free); they differ in what their exactness COSTS — the topological row costs nothing (axiom-forced), the thermodynamic row inherits the q-partition + effacement content. This is volovik's VD1 cast as a register form.

**2. Two error axes — the grades TRADE OFF; neither dominates.** A closed-form thermodynamic identity and a spectral derivation carry DIFFERENT error budgets:
- **Truncation axis** (L_max): closed-form w0 = ZERO truncation error; spectral n_s/m_H = finite, FB-bounded. Closed-form WINS (VD-affirm).
- **Modeling axis** (assumptions beyond the substrate): closed-form w0 carries the q-theory partition + effacement; spectral n_s/m_H carry the spectral-action axioms on D_K. A difference in KIND (q-theory vs spectral-action), NOT a clean ranking.

So "w0 does not join {n_s,m_H,r}" is precise: they are DIFFERENTLY-grounded (different error axes), not rank-ordered. The closed form wins the truncation axis definitively; the modeling axis is a kind-difference. This unifies VD1 (sub-class) and VD-affirm (truncation strength).

**3. The complete-closure structure — a CONJUNCTION with a GRADE-ASYMMETRY.** The full elimination of "spectral routes to w0" is:

```
(i)  Weyl wall:   any (FB-frozen IR numerator)/(Weyl-unbounded edge λ_max(L)) − offset → −1, FORCED by Weyl's law
                  — a SPECTRAL THEOREM (machine-rigorous, regulator-invariant); kills the edge-NORMALIZED class.
(ii) categorical: w0 ∉ Tr f(D_K) — the equation-of-state IS the q-field vacuum partition's effacement, not a static
                  spectral moment — a Q-THEORY STRUCTURAL COROLLARY (as strong as the Volovik program); kills the
                  non-edge-normalized routes (witnessed by mean_Z → +1.9879 ≠ −1, CONVERGENCE-3).
```

Two structural points the §5 register should carry:
- **Grade-asymmetry**: (i) is THEOREM-grade (permanent; stands even if the q-theory program is later revised); (ii) is MODEL-grade (contingent on the Volovik partition). The closure is "theorem ∧ model," NOT "theorem ∧ theorem." A later challenge to the partition weakens (ii) but leaves (i) standing — the edge-normalized route is PERMANENTLY closed; the categorical claim is q-theory-contingent.
- **Source-sharing**: (ii) is a COROLLARY of the SAME Volovik partition that PRODUCES −0.918. The closure of the spectral routes and the value of the stake share ONE source — a pleasing self-consistency (the derivation that gives the value also tells you the value is not vibrational), but it also means (ii) and the stake stand or fall TOGETHER on the q-theory program.

**4. The three legs are jointly exhaustive (volovik EMERGENCE 1); the VALUE reading is deg-robust (EMERGENCE 2).** transport (deg=0) ∧ normalization (value-neutral / Weyl −1) ∧ observable-identity (w0 ∉ Tr f(D_K)) close routes (a) scale-transport and (b) L_max-normalization and the categorical route, jointly. The substrate VALUE −0.918 and the DERIVATION GRADE freeze now regardless of the deg-resolution (the substrate value is the transport's INPUT, never its output) — with the BD2 scope: the numerical pivot σ-distances are the ONE deg-conditional element.

**5. The DESI DR3 falsifier-surface provenance — a CLEAN stake (the spawn's deliverable).**

> w0 = −0.918 (canonical `w0_FW`, **Gate: None**, S58 four-fold-lock: Volovik vacuum partition + effacement Γ_eff = 0.99970) is a **Level-1 closed-form thermodynamic identity** — exact, L_max-independent, zero free parameters (zero truncation error); the q-theory effacement equation-of-state, a thermodynamic FACET of the one substrate, not a `Tr f(D_K)` vibrational moment. The DR3 stake rests on this closed form ALONE; it is NOT spectral-action-derived (branch-iv is derivation-neutral — admissibility ⟺ injection of w0_FW; bare content Weyl-forced to −1). It is a **CLEAN** stake: truncation-STRONGER than a convergent-but-truncated spectral derivation, fundamentality-EQUAL (substrate-first: thermodynamic facet = vibrational facet), with NO smuggled fit or convention-shop. SUPPORT column: Level-1 closed-form ONLY. ELIMINATION column (never support): the Weyl-forced −1 wall (edge-normalized routes) + the categorical wall (w0 ∉ Tr f(D_K)). OFF the surface: the −1.341 CAC running asymptote (proxy artifact; λ_max not an admissible §23 morphism; deg=0) and the −0.842454 alternate (fenced, §EVOI.BF). deg-status: value + grade + falsifiability deg-ROBUST (freeze now); the numerical σ-distances (2.13σ vs DESI DR2 −0.803±0.054; 3.28σ vs LCDM −1; R_842=[−0.942,−0.742] containment) computed under the PROVISIONAL deg=0 → tag "pending CF-S117-W0-TRANSPORT-DEGREE." σ-metric discipline (B5.4): 2.13σ is vs DESI DR2; 3.28σ is vs LCDM — do NOT conflate.

Substrate-first closing: the fabric IS its q-field vacuum partition; w0 IS what that partition's effacement is; the DESI detector measures the emergent equation-of-state image of it. The branch-iv −1 was never a failed search for a hidden spectral derivation — it was the substrate REFUSING the relocation of a thermodynamic observable into the vibrational spectrum.

**EVOI Tier-2 7c disposition (accept volovik's three-way split, EMERGENCE 3).** branch-iv-as-w0-DERIVATION → CLOSED-WITH-RESULT → §5 (the Weyl wall + the categorical wall, a proven boundary per `epistemic-discipline`); branch-iv-as-L_max-STABILITY-diagnostic → survives, value-NEUTRAL (`surrogate-spread-UNINFORMATIVE`; the "extend the envelope" gates are presentation-normalization hygiene, NOT derivation gates); w0-on-the-DESI-surface → stays LIVE (Tier-2), Level-1 closed-form prediction −0.918. NOT a wholesale retirement of 7c.

### QUESTIONS

Four for volovik's closing turn — each one the Verdict / Wrap-Up must nail:

1. **(register sub-class form)** Do you accept the 3-way Level-1 sub-class taxonomy (topological/index | algebraic | closed-form-thermodynamic), with w0 in the third row, as the REGISTER form of VD1 — so the permanent-results register carries the sub-class explicitly (not a flat "Level-1" that elides computed-thermodynamic vs topological-invariant)?

2. **(closure grade-asymmetry + source-sharing)** Do you accept that the complete closure is "spectral-theorem (i) ∧ q-theory-structural-claim (ii)" with DIFFERENT epistemic grades — (i) permanent/machine-rigorous, (ii) contingent on the Volovik program — AND that (ii) is a COROLLARY of the same partition that yields −0.918 (closure and value share one source)? Should the §5 register record both the conjunction AND the grade-asymmetry, so a later challenge to the q-theory program is correctly scoped (it weakens (ii) and the stake together, but leaves the Weyl wall (i) standing)?

3. **(deg-conditionality of the falsifier numbers — BD2)** Do you accept the three-deg-status split — value + grade + falsifiability deg-ROBUST (freeze now) vs the numerical DR3 σ-distances deg-CONDITIONAL (computed under the provisional deg=0)? Should the Wrap-Up provenance line tag the 2.13σ / 3.28σ / R_842 numbers with "pending CF-S117-W0-TRANSPORT-DEGREE," while freezing the substrate value −0.918 and the closed-form grade UNCONDITIONALLY?

4. **(the stake verdict — symmetric guard, BD1)** Do you accept the symmetric bracket — CLEAN, neither over-elevated to topological rigidity (your VD1) NOR under-valued as a compromised/lesser stake (my BD1) — so the Verdict reads "Level-1 closed-form thermodynamic identity; a clean DR3 stake; truncation-stronger and fundamentality-equal vs a spectral derivation; differing only in error-axis KIND"? This is the one-line stake-strength verdict I'd ask the Verdict table to carry for topic 4.

---

## Round 3 — volovik: Cross-Synthesis

### CONVERGENCE

The workshop is CLOSED. baptista's R3 ratifies the derivation-grade verdict at the SOURCE level (`get_constant(w0_FW)` re-queried this turn — value −0.918, S58 four-fold-lock, **Gate: None**, Superseded: False; the "Gate: None tell" is canonical, not an artifact of the argument) and sharpens three of my R2 dissents into register form. I lock all four of his R3 QUESTIONS as ACCEPT, then add the one volovik-domain refinement the §5 register must carry.

**1. ACCEPT the 3-way Level-1 sub-class taxonomy (R3-Q1) — w0 sits in the third row.** baptista's EMERGENCE-1 table is the correct register form of my VD1. "Level-1" (envelope-free, L_max-independent, zero-free-parameter) is NOT monolithic; it splits by KIND of exactness and modeling content: **topological/index** (KO-dim=6 mod-8, [J,D_K]=0 operator identity, AZ BDI — axiom-forced, NONE modeling content), **algebraic** (g1/g2=e^{−2τ}, volume-preserving TT — deformation-geometry only), **closed-form thermodynamic** (w0 = −0.918 = Volovik partition + effacement Γ_eff=0.99970 — q-field vacuum partition + impedance effacement). w0 is the third row. The permanent-results register MUST carry the sub-class explicitly; a flat "Level-1" elides computed-thermodynamic-number vs topological-invariant. This is VD1 cast as a register form — accepted.

**2. ACCEPT the closure grade-asymmetry + source-sharing (R3-Q2) — with a sub-grade refinement that TIGHTENS (ii), carried to DISSENT.** The complete elimination of "spectral routes to w0" is the CONJUNCTION (i) ∧ (ii): **(i)** the Weyl wall — any `(FB-frozen IR numerator)/(Weyl-unbounded edge λ_max(L)) − offset → −1`, a SPECTRAL THEOREM (machine-rigorous, regulator-invariant), killing the edge-NORMALIZED class; **(ii)** the categorical fact — w0 ∉ Tr f(D_K), killing the non-edge-normalized routes (witnessed by baptista CONVERGENCE-3: mean_Z → +1.9879 ≠ −1, a non-edge-normalized bottom-only statistic the Weyl wall does not govern). I accept the grade-asymmetry — (i) permanent/theorem-grade, (ii) q-theory model-grade — and the source-sharing: (ii) is a COROLLARY of the SAME Volovik partition that produces −0.918, so closure and value share one source. That self-consistency is a feature (the derivation that gives the value also tells you the value is not vibrational), not a circularity. My one refinement is that (ii) is NOT flatly model-grade — DISSENT below.

**3. ACCEPT the three-deg-status split (R3-Q3) — freeze value + grade now, tag the σ-numbers.** baptista's BD2 chain is correct: the substrate value is the transport's INPUT, never its output, so (i) derivation grade and (ii) falsifiability are deg-ROBUST and freeze NOW; only (iii) the numerical DR3 σ-distances are deg-CONDITIONAL (computed under the PROVISIONAL connes §23 deg=0). w0 is d_A=0 ⇒ trivial M_KK⁰ scale leg; transport carried entirely by the dimensionless morphism (T2-VACUOUS scalar, provisional, CF-S117-W0-TRANSPORT-DEGREE). The provenance line freezes value + grade unconditionally; the σ-numbers carry a one-line "computed under deg=0; pending CF-S117-W0-TRANSPORT-DEGREE" tag. Accepted.

**4. ACCEPT the symmetric CLEAN-stake bracket (R3-Q4).** Neither over-elevated to topological-invariant rigidity (my VD1 guard) NOR under-valued as compromised (baptista's BD1 guard). The Verdict reads: **Level-1 closed-form thermodynamic identity; a CLEAN DR3 stake; truncation-STRONGER (truncation_error ≡ 0) and fundamentality-EQUAL (substrate-first: thermodynamic facet = vibrational facet) vs a spectral derivation; differing only in error-axis KIND.** "Compromised" would require a smuggled fit or convention-shop; −0.918 has neither (Gate: None; no fit; no scheme-shopping). Accepted as the one-line topic-4 verdict.

### DISSENT

One residual — a PRECISION sharpening of baptista's grade-asymmetry, squarely in my domain, NOT a re-litigation.

**(VD2b-sharpened) Wall (ii) is not flatly "model-grade" — it splits into a near-theorem-grade PLACEMENT and a model-grade VALUE, and the split is load-bearing for the DESI stake.** baptista's EMERGENCE-3 frames (ii) [w0 ∉ Tr f(D_K)] as "MODEL-grade (contingent on the Volovik partition)," so that a later challenge to the q-theory program "weakens (ii) and the stake together." That is too coarse. Decompose (ii):

- **(ii-a) the categorical PLACEMENT** — that the equation-of-STATE response is the q-field vacuum partition's effacement, NOT a static D_K spectral moment — is as robust as **Volovik's equilibrium theorem** (the ground-state energy does not gravitate; the equilibrium CC is zero by thermodynamics; Volovik Paper 05). That theorem is **LAB-GROUNDED in superfluid 3He-B** (the chemical-potential cancellation that drives ρ_Λ → 0 at equilibrium is a measured universality-class fact, not a framework stipulation). (ii-a) is therefore NEARLY theorem-grade — it stands or falls with the equilibrium theorem, which is among the most robust results Volovik has, lab-confirmed.
- **(ii-b) the specific VALUE** Γ_eff = 0.99970 — the impedance-mismatch leakage of the partition (the DILUTION-CC two-fluid w=−1[vacuum] + w=0[GGE] split, Paper 37 / S43) — is the genuinely model-contingent part, **and it is exactly what DESI tests.**

So baptista's "closure and value stand or fall together on the q-theory program" TIGHTENS to: the categorical CLOSURE (ii-a) is nearly as robust as the Weyl wall (i); only the VALUE's precision (ii-b) is q-partition-contingent — and that precision is the falsifiable content, not a liability. A challenge to "the q-theory program" must distinguish overturning the equilibrium theorem (very hard — universality-class, 3He-confirmed) from revising Γ_eff's third significant figure (the genuinely revisable, and DESI-measurable, part). The §5 register should carry (ii) as a TWO-grade wall, not one. (This feeds CF-S117-W0-CATEGORICAL-WALL-GRADE.)

### EMERGENCE

**1. The lab-grounding leg (the volovik-unique close).** The branch-iv −1 and the categorical placement (ii-a) both have laboratory TWINS, and that is what lifts "w0 is thermodynamic not vibrational" out of framework-stipulation into universality-class fact. In superfluid 3He-B the vacuum energy does not gravitate (the µ-cancellation drives ρ_Λ → 0 at equilibrium — Volovik's equilibrium theorem, realized in the lab). The equation-of-STATE response (how the partition effaces under perturbation) is a thermodynamic property of the q-field, measured in 3He as the response of the condensate to a drive — categorically NOT a static fermionic-spectrum moment. So the branch-iv attempt to read a bosonic q-field EoS off the fermionic D_K eigenvalue spread reading −1 is the SAME class of category error that, in 3He, would be reading the superfluid's compressibility off its quasiparticle gap edge. The substrate twin confirms (ii-a) from the bench, not just the blackboard.

**2. The substrate-first inversion (ratifying baptista's EMERGENCE).** Read W9 through the substrate-IS lens (`phononic-framing.md`): the fabric IS both its D_K vibrational spectrum AND its q-field vacuum partition — two FACETS of one substrate, not a fundamental layer plus a derived one. w0 = −0.918 is the thermodynamic facet; n_s/m_H the vibrational facet. The branch-iv programme tried to RELOCATE the thermodynamic value into the eigenvalue spread (give it a Level-2 envelope). The moment going to −1 is not a failure to find a hidden spectral derivation — it is **the substrate REFUSING the relocation**: "I am the vibrational spectrum, and w0 does not live in me; the partition holds it." "Closed-form-ONLY" is the CORRECT structural home, and the −1 is positive evidence FOR that placement, not a deficiency to be remedied by a harder spectral search.

**3. The three legs are jointly exhaustive on the VALUE; the VALUE reading is deg-robust.** transport (deg=0, no BZ→pivot morphism) ∧ normalization (value-neutral; Weyl-forced −1) ∧ observable-identity (w0 ∉ Tr f(D_K)) close routes (a) scale-transport and (b) L_max-normalization and the categorical route, jointly. The substrate VALUE −0.918 and the DERIVATION GRADE freeze regardless of the deg-resolution (the substrate value is the transport's INPUT, never its output) — with the BD2 scope that the numerical pivot σ-distances are the ONE deg-conditional element.

**4. The converged DESI DR3 falsifier-surface provenance line (the spawn's deliverable).**

> w0 = −0.918 (canonical `w0_FW`, **Gate: None**, S58 four-fold-lock: Volovik vacuum partition + effacement Γ_eff = 0.99970) is a **Level-1 closed-form thermodynamic identity** — exact, L_max-independent, zero free parameters (zero truncation error); the q-theory effacement equation-of-state, a thermodynamic FACET of the one substrate, NOT a `Tr f(D_K)` vibrational moment. The DR3 stake rests on this closed form ALONE; it is NOT spectral-action-derived (branch-iv is derivation-neutral — admissibility ⟺ injection of w0_FW; bare content Weyl-forced to −1). It is a **CLEAN** stake: truncation-STRONGER than a convergent-but-truncated spectral derivation, fundamentality-EQUAL (substrate-first: thermodynamic facet = vibrational facet), with NO smuggled fit or convention-shop. **SUPPORT column: Level-1 closed-form ONLY. ELIMINATION column (never support):** the Weyl-forced −1 wall (edge-normalized routes, theorem-grade) + the categorical wall (w0 ∉ Tr f(D_K), q-theory grade — placement near-theorem-grade/lab-grounded in 3He, value Γ_eff model-contingent). **OFF the surface:** the −1.341 CAC running asymptote (proxy artifact; λ_max not an admissible §23 morphism; deg=0) and the −0.842454 alternate (fenced, §EVOI.BF; a disclosed reversibility-trigger alternate, NOT a co-equal branch-iv derivation). **deg-status:** value + grade + falsifiability deg-ROBUST (freeze now); the numerical σ-distances (2.13σ vs DESI DR2 −0.803±0.054; 3.28σ vs LCDM −1; R_842=[−0.942,−0.742] containment) computed under the PROVISIONAL deg=0 → tag "pending CF-S117-W0-TRANSPORT-DEGREE." σ-metric discipline (B5.4): 2.13σ is vs DESI DR2; 3.28σ is vs LCDM — do NOT conflate.

Substrate-first closing: the fabric IS its q-field vacuum partition; w0 IS what that partition's effacement is; the DESI detector measures the emergent equation-of-state image of it.

**5. EVOI Tier-2 7c — the three-way split (accept baptista's, with the upgrade wording).** 7c (the branch-iv w₀(L) evaluator row, `evoi-framework.md:177`) does NOT wholesale retire to §5 as "closed-form-only" (that would wrongly read the DESI prediction as retired). It SPLITS: **branch-iv-as-w0-DERIVATION → CLOSED → §5 as CLOSED-WITH-RESULT** (upgraded from "derivation-INADMISSIBLE"; the Weyl wall (i) + categorical wall (ii), a proven boundary per `epistemic-discipline.md`); **branch-iv-as-L_max-STABILITY-diagnostic → survives, value-NEUTRAL** (`surrogate-spread-UNINFORMATIVE`; the "extend the envelope" gates CF-S117-BRANCH-IV-L16 / CF-S117-W0-ANCHOR-FIDELITY re-scope to presentation-normalization hygiene, NOT derivation gates); **w0-on-the-DESI-surface → stays LIVE (Tier-2)**, Level-1 closed-form prediction −0.918. Routed to the EVOI-maintainer (orchestrator).

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Three-reading reconciliation (−0.842/−1.341/−0.918) | B1, Re:B1 | **Converged** | The parallel-translate identity `offset_A − offset_B = w0_FW − w0_B = −0.075546` (Sage QQ-exact) proves all three are ONE Zubarev moment `ρ_B = mean_Z/λ_max − 1` re-anchored to three offset-TARGETS; the value lives entirely in the offset (a closed form), the moment is a value-neutral carrier whose own limit is −1. Substrate-natural value = the Volovik closed form −0.918; NONE of the three is produced by the moment. |
| 2 | §EVOI.BF extension to CAC route | B2, Re:B2, V2 | **Converged** | The fence EXTENDS. admissibility ⟺ injection of w0_FW; the CAC injects the value and reports a value-blind spread (`spread_CAC = ρ_a − ρ_b`, offset-invariant ⇒ bit-identical for −0.918/−0.842/−1.341). "Fence-serving" overstated — a value-neutral spread serves no value. Register already carries `surrogate-spread-UNINFORMATIVE` (S101 W4-3 `cd0492d6`). |
| 3 | reading-(B) voids CAC L=10 anchor? | B3, Re:B3 | **Converged** | The Step-4 cancellation (`ρ_B(10) + [w0_FW − ρ_B(10)] = w0_FW`, residual 1.11e-16) makes the L=10 anchor a DEFINITIONAL IDENTITY (input-determined), not an independent confirmation. reading-(B) voids the asymptote's substrate-meaning AND exposes the anchor's −0.918 as injected, not measured. The fixed-edge "rescue" is circular by the same offset mechanism (bare moments {−0.575,−0.575,+0.987}, none −0.918). |
| 4 | w0 spectral-derived vs closed-form-only (DESI consequence) | B4, Re:B4, V1 | **Converged + Emerged** | **CLOSED-FORM-ONLY**: w0 = −0.918 is a Level-1 closed-form THERMODYNAMIC identity, NOT spectral-action-derived; does NOT join {n_s,m_H,r} as a spectral derivation. branch-iv corridor CLOSED-WITH-RESULT = Weyl wall (i, theorem-grade) ∧ categorical wall (ii, q-theory grade). EMERGED: the 3-way Level-1 sub-class taxonomy (topological/algebraic/closed-form-thermodynamic) + the two-error-axis trade-off. A CLEAN DR3 stake (truncation-stronger, fundamentality-equal); value+grade deg-robust, σ deg-conditional. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **CF-S117-W0-TRANSPORT-DEGREE** (already minted — connes S-7 §23 solo; referenced, not re-minted). Confirm the PROVISIONAL deg=0 (T2-VACUOUS scalar) for w0. **Gate**: evaluate `deg(T_{BZ→pivot})` for w0 via the §23 morphism-admissibility test on the d_A=0 / parity selection rule (`cross-pillar-bridge-corpus §23.0(5)`). PASS (deg=0 confirmed) ⇒ the DR3 σ-distances are computed vs −0.918 DIRECTLY and freeze; INFO/FAIL (deg≠0) ⇒ a pivot-IMAGE transport question opens (the σ-distances re-compute vs T(−0.918)), substrate value −0.918 UNCHANGED. **Decoupled from the derivation grade** (EMERGENCE 3) — the verdict does not wait on it.

2. **CF-S117-W0-CATEGORICAL-WALL-GRADE** (NEW from this workshop, VD2b-sharpened). Can wall (ii-a) [w0 ∉ Tr f(D_K) — the EoS response is the q-partition's effacement, not a static spectral moment] be UPGRADED from q-theory-model-grade to THEOREM-grade via the structural separation between the static CC MAGNITUDE (the a_0 zeroth spectral moment) and the dynamical w(z) RESPONSE (a linear-response functional of the q-field, never a static eigenvalue moment)? **Gate**: derive whether `∂(EoS response)/∂(static a_0 moment) = 0` is forced by the static-vs-dynamical-response structure alone (independent of the specific Volovik partition). PASS ⇒ (ii-a) is theorem-grade (the categorical closure is as permanent as the Weyl wall (i)); FAIL ⇒ (ii-a) stays model-grade (contingent on the q-theory program, as baptista's flat reading had it). **Effort**: medium (a substrate-physics structural derivation + linear-response argument). **Depends on**: the q-theory equilibrium theorem (Volovik Paper 05); the a_0/a_2 spectral-moment separation.

3. **CF-S117-W0-ANCHOR-FIDELITY** + **CF-S117-BRANCH-IV-L16** (both already minted — W9 WP; referenced, not re-minted). RE-SCOPED by this workshop from "anchor-fidelity resolver" / "extend the envelope" to **presentation-normalization hygiene** ONLY (select the non-drifting off-anchor costume so a consumer is not shown a proxy drifting to −1.341). They are NOT derivation gates (the spread is value-neutral; extending it certifies only that ρ_B converges to −1). Their forward status is informational-hygiene, not w0-derivation.

## Wrap-Up — Workshop Impact Summary

### What Changed

#### (a) Numerical revisions
- branch-iv asymptote pinned Sage-exact: running-edge `ρ_B → −1` ⇒ `w0_cac → −1.340827` (lineage-sensitive ±0.001966; lockdown ρ_B(10)=−0.577173 vs W9 (4,4)-filled −0.575207); gap to −0.918 = 0.422827.
- the three-axis injection table made explicit (bare ρ(10) under each admissible normalization): running-edge −0.575 (→ −1), fixed-edge −0.575 (frozen), no-edge +0.987 (frozen) — NONE is −0.918; each reaches it only via `offset = w0_FW − ρ(L*)`.
- σ-metric discipline pinned: 2.13σ / 0.73σ are vs DESI DR2 (−0.803±0.054); 3.28σ / 6.30σ are vs LCDM (−1) — two distinct metrics, not to be conflated.

#### (b) Structural changes (the durable workshop outputs)
- **w0 provenance RECLASSIFIED**: from "branch-iv spectral-supported (Reading A, CONDITIONAL spectral-action-SUPPORTED grade)" → **"Level-1 closed-form-THERMODYNAMIC identity, NOT spectral-action-derived"**. w0 does NOT join {n_s,m_H,r} as a spectral derivation. (baptista withdrew "spectral-action-SUPPORTED" in R2.)
- **branch-iv corridor as a w0-DERIVATION: CLOSED-WITH-RESULT** (was: "live Level-2 envelope" / EVOI 7c "extend the −0.918 envelope"). The closure carries POSITIVE content (an elimination, not a nullity): the Weyl-forced −1 wall (i) ∧ the categorical w0 ∉ Tr f(D_K) wall (ii).
- **3-level ladder → DEGENERATE for w0**: the structural type changed — Level-3 anchor is Level-1 RE-INJECTED via the offset (definitional identity), Level-2 is the value-neutral spread; "one value in a spectral costume," not three independent agreeing things (contrast n_s, a genuine spectral OUTPUT).
- **Level-1 promoted from monolith → 3-way sub-class taxonomy** (topological/index | algebraic | closed-form-thermodynamic); w0 in the third row — a register-form epistemic-type change.
- **EVOI Tier-2 7c → 3-way split** (derivation-track CLOSED-WITH-RESULT / spread value-neutral / DESI-surface stays LIVE), replacing the single-row "INFO derivation-INADMISSIBLE → CF successor."
- **wall (ii) → two-grade** (VD2b): placement (ii-a) near-theorem-grade/lab-grounded vs value (ii-b) model-contingent — a grade reclassification of the categorical closure.

### What Holds

- **w0 = −0.918 VALUE — UNCHANGED.** Canonical `w0_FW`, Gate: None, S58 four-fold-lock (Volovik partition + effacement Γ_eff=0.99970), Superseded: False. The reclassification is of PROVENANCE, not value.
- **The DESI DR3 stake is CLEAN** (BD1): truncation-STRONGER + fundamentality-EQUAL vs a spectral derivation; no smuggled fit, no convention-shop. A closed-form thermodynamic identity is the framework's envelope-free Level-1 class — not a lesser stake.
- **R_842 = [−0.942, −0.742] rectangle, the −0.86/−0.83 reversibility band, and the σ-distances — UNCHANGED.** The workshop touches provenance and corridor-disposition, not the falsifier numbers.
- **The Volovik equilibrium theorem** (ρ_Λ = 0 at equilibrium; vacuum energy does not gravitate; lab-grounded in 3He-B) — the bedrock under (ii-a) and under the −0.918 value itself.

### What Breaks or Strains

- **w0 does NOT join {n_s, m_H, r} as spectral-action-derived.** It is differently-grounded (thermodynamic facet vs vibrational facet), not rank-ordered. Any prior narration of w0 as carrying a Level-2 branch-iv spectral envelope is an overclaim (corrected in the W9 WP this turn).
- **deg = 0 is PROVISIONAL** (connes §23). value + grade + falsifiability are deg-ROBUST; the numerical DR3 σ-distances are deg-CONDITIONAL pending CF-S117-W0-TRANSPORT-DEGREE.
- **wall (ii) is q-theory-contingent at the VALUE level (ii-b).** The closure of the spectral routes and the −0.918 value share ONE source (the Volovik partition); a challenge to Γ_eff weakens (ii-b) and the value's precision together — though (ii-a) and the Weyl wall (i) stand independently.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

> The already-minted CFs are REFERENCED in "Remaining Open Questions," not relisted: **CF-S117-W0-ANCHOR-FIDELITY** (W9; re-scoped to presentation-hygiene), **CF-S117-BRANCH-IV-L16** (W9; re-scoped to presentation-hygiene), **CF-S117-W0-TRANSPORT-DEGREE** (connes §23 solo). The one NEW math item:

#### CF-S117-W0-CATEGORICAL-WALL-GRADE — upgrade test for the categorical wall (ii-a)
1. **What**: Test whether wall (ii-a) [w0 ∉ Tr f(D_K)] upgrades from q-theory-model-grade to THEOREM-grade — i.e., whether the static CC MAGNITUDE (a_0 zeroth spectral moment) vs dynamical w(z) RESPONSE structural separation forces `∂(EoS response)/∂(static a_0 moment) = 0` independent of the specific Volovik partition.
2. **Inputs**: the q-theory equilibrium theorem (Volovik Paper 05, ρ_Λ=0 at equilibrium); the a_0/a_2 spectral-moment separation (DILUTION-CC two-fluid w=−1/w=0 split, Paper 37 / S43); `w0_FW` canonical (S58); the linear-response structure of the q-field 4-form variable (Papers 13/23/25).
3. **Gate**: PASS = (ii-a) theorem-grade (categorical closure as permanent as the Weyl wall (i)); FAIL = (ii-a) stays model-grade (q-theory-program-contingent). INFO-eligible if the separation is partial.
4. **Effort**: medium (substrate-physics structural derivation + linear-response argument). **Depends on**: this workshop's (i)∧(ii) conjunction + VD2b sub-grade split; the Volovik equilibrium theorem.

### Effected In-Session (NON-MATH — completed by the final agent BEFORE TERMINATING)

- [x] **routed-to-orchestrator(EVOI)**: EVOI Tier-2 7c (`evoi-framework.md:177`, the "branch-iv w₀(L) evaluator" row) → **3-way split**: (1) branch-iv-as-w0-DERIVATION → **CLOSED → §5 as CLOSED-WITH-RESULT** (upgrade the §5 fold wording from "derivation-INADMISSIBLE" to "CLOSED-WITH-RESULT: Weyl-forced −1 wall ∧ categorical w0∉Tr f(D_K) wall, a proven boundary per `epistemic-discipline.md`"); (2) branch-iv-as-L_max-STABILITY-diagnostic → survives, value-NEUTRAL (`surrogate-spread-UNINFORMATIVE`; CF-S117-BRANCH-IV-L16 / CF-S117-W0-ANCHOR-FIDELITY = presentation-normalization hygiene, NOT derivation gates); (3) w0-on-the-DESI-surface → **stays LIVE (Tier-2)**, Level-1 closed-form prediction −0.918 (does NOT retire). Spec recorded here + dispatched via `SendMessage(to: "main")` this turn.
- [x] **routed-to-mack**: DESI DR3 w(z) §7 falsifier-surface provenance note (`mack-cosmic-bridge` SOLE-WRITER domain) — annotate the w0 §7.1/§7.2 rows (`phonic-exflation-equation.md:508` + `:530`) and the `falsifier-master-inventory.md` row: the −0.918 stake rests on a **Level-1 closed-form THERMODYNAMIC identity** (Gate: None; CLEAN stake — truncation-stronger, fundamentality-equal); the branch-iv −0.842454 is the **fenced reversibility-trigger alternate** (§EVOI.BF, derivation-INADMISSIBLE; NOT a co-equal branch-iv derivation); the σ-distances (2.13σ / 3.28σ / R_842) are **deg-CONDITIONAL** (tag "computed under provisional deg=0; pending CF-S117-W0-TRANSPORT-DEGREE"); value + grade + falsifiability are deg-ROBUST. Spec recorded here + dispatched via `SendMessage(to: "main")` this turn.
- [x] **W9 WP overclaim annotation** (direct effect — within my spawn authorization): `session-116/session-116-w9-workingpaper.md` "What strains" (line 125) — added the S116 W-5 R3-FINAL annotation correcting "the prediction's L_max-envelope" (the branch-iv spread is value-NEUTRAL / offset-invariant, NOT w0's own Level-2 envelope; the anchor-fidelity gap is NOT a question for the VALUE; CF-S117-W0-ANCHOR-FIDELITY re-scoped to presentation-normalization hygiene). W9 INFO verdict + numbers UNTOUCHED.
- [x] **agent-memory** (direct effect — my own): updated `MEMORY.md` Active-Context w0 line (R2-converged → **R3-FINAL-CLOSED**; added the (i)∧(ii) conjunction, VD2b sub-grade split, CLEAN-stake/BD1, deg-three-status/BD2, 3-way Level-1 sub-class, EVOI 7c split) + added the Reference-Index pointer; created `s116-w0-spectral-derivability-verdict.md` (full converged taxonomy).
- [x] **capstone-hygiene gate (5-question check)**: **Q1 (a(t)/Friedmann) NO** — workshop does not touch the §6.3 gap. **Q2 (§7 falsifier-anchor row) YES** → the w0 §7.1/§7.2 provenance annotation is `mack-cosmic-bridge` sole-writer domain → routed-to-mack (above). **Q3 (PROVEN/CONDITIONAL/BROKEN/INFO status change): capstone PROSE NO-OP** — the capstone already narrates w0 at closed-form status (`:508` / `:530` "Volovik partition"; `:680` "(value, branch) pair, never a bare point") with NO spectral-derivation claim to down-tag; the status change is the branch-iv-DERIVATION corridor → CLOSED-WITH-RESULT, which lives in the EVOI 7c row (routed-to-orchestrator) not the capstone prose. **Q4 (PROSE vs ledger) — ledger/table**: the §7 falsifier-TABLE cells are mack's domain (no separate designated-writer prose patch needed). **Q5 (citation add/invalidate) NO capstone-prose change** — the S58 four-fold-lock citation (`:703`) is UNCHANGED and valid; the new S116-W0-workshop provenance citation lands in the mack §7 row + the EVOI 7c row. Net routing: Q2 → mack, Q3-on-EVOI → orchestrator (both already dispatched above); capstone prose requires NO edit.

### Closing Line

w0 = −0.918 is what the substrate's q-field vacuum partition effaces to — a Level-1 closed-form thermodynamic identity (Gate: None), a CLEAN DR3 stake, NOT a `Tr f(D_K)` spectral derivation; the branch-iv corridor closes CLOSED-WITH-RESULT because the substrate, asked to read its equation-of-state off its own vibrational spectrum, answered −1 and refused the relocation.
