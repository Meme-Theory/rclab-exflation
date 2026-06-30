# Session 100b Synthesis: Fold |β_pivot|² Delta-Weight Convention Adjudication (W5 — z-pump vs √a-pump)

**Date**: 2026-06-07
**Agent**: transit-dynamics-theorist (Workhorse-Transit-Dynamics)
**Source Documents**:
- `sessions/session-100b/session-100b-w5-workingpaper.md` (W5-1 §"Barrier-branch and weight sensitivity", §"Normalization & window", substitution chain Steps 1–5; W5-2; Wave 5 Synthesis + CF-S101 specs)
- `sessions/session-plan/session-100b-plan-w5.md` (§W5-1 R3 gate block: `delta_weight_rule`, `normalization_pin`, `window_pin`, substitution chain, honest re-open laws (a)–(d); §W5-2)
- `.claude/agent-memory/transit-dynamics-theorist/MEMORY.md` (canonical mode equation; S79 3-stage ladder; fold-window barrier-convention debugging notes)

**Scope discipline**: the W5-1 and W5-2 gate verdicts (both PASS, audits `297a597c…` / `683a7e22…`) are authoritative and are NOT re-adjudicated here — the W5-1 PASS is delta-weight-INVARIANT by construction (identical Ω on both sides of `var_Nseg` and `rel_dev`). What this synthesis adjudicates is the **convention tuple that CF-S101-BETA-PIVOT-PROMOTION must pin at its S101 pre-registration**, before the plan-freeze default (the √a-pump weight) is inherited silently into a canonical constant. No computation scripts were executed and no verdict lines emitted; all numerics below are closed-form arithmetic on values documented in the WP/npz tables.

**Notation** (fold-normalized conformal clock throughout): η̃ = conformal time in fold units, `′ ≡ d/dη̃`; ã(τ_fold) = 1 (Convention B, S77 canonical); ℋ̃ ≡ ã′/ã = ãH̃ = 0.975393518773 M_KK (s77 pair `k_pivot/k_over_aH`); k_pivot = 14.311092688448717 M_KK; Δη̃ = 1.13014059×10⁻³ M_KK⁻¹. Dimensions: [k] = [Ω] = M_KK; [V] = [z″/z] = M_KK²; [Δη̃] = M_KK⁻¹; ΩΔη̃, kΔη̃, |β|² dimensionless.

---

## I. Session Outcome

Both W5 gates PASS (authoritative): S100b-BOX-DELTA-BOGOLIUBOV reopens the transfer-matrix corridor for the fold's sudden limit (var_Nseg − 1 = 6×10⁻¹⁰, Schmidt-Eq.-75 match 1.6×10⁻⁶, TM-vs-Radau 7×10⁻¹²), and S100b-FOLD-RANGE-SCALING pins the fold in the Rao v > v_c range-controlled class. The adjudication this synthesis delivers: **the substrate-IS jump operator at the fold's switch boundaries, for the canonical v_k mode equation, is the [z′/z] delta — Ω_z = ±1.288 M_KK — not the pinned Sparn-literal √a-pump weight Ω_ψ = (1/2)ã[ã′] = ±0.487 M_KK**; the production is weight-quadratic in the cancellation-dominated regime (|β|² ≈ (ΩΔη̃)², verified to 0.25% against every documented channel), so the ×6.96 fork is exactly (Ω_z/Ω_ψ)², and all three downstream consumers (S79 B-ladder, GGE n_Bog, UNIFIED-AS-79 F_amp slot) normalize to v_k-quanta. CF-S101-BETA-PIVOT-PROMOTION must therefore pre-register the full 4-component convention tuple — **(weight = Z-PUMP [z′/z]; barrier = branch-(c) stored z″/z channel; window = canonical fold-conformal clock; ladder-stage = IMPULSIVE-TRANSIT-WINDOW, non-comparable to B2)** — and recompute the canonical value at that tuple (≈ 2.12–2.14×10⁻⁶, in-gate) rather than silently promote the hybrid 3.045×10⁻⁷, which is retained as the permanent recipe-benchmark (√a-pump) verdict payload.

---

## II. Key Results

### II.1 The substrate-IS jump operator at the switch boundaries — Ω_v = [z′/z] (EXACT)

**Result**: across a sharp interface where z′ jumps (z continuous), the v_k barrier z″/z carries the distributional part [z′/z]·δ(η̃ − η̃_b); the v_k jump condition is [v′] = [z′/z]·v(η̃_b). Classification: **PHONONIC** (substrate mode-equation structure).

This is sub-question (a), settled by distribution theory with no approximation. Substitution chain (per `math-scripts.md`):

```
Claim: "For the substrate mode equation v_k″ + (k² − z″/z)v_k = 0, the delta
        weight at a sharp boundary η̃_b where z′ jumps is Ω_v = [z′/z];
        the pinned rule Ω_ψ = (1/2)ã[ã′] is the weight of the DIFFERENT
        variable ψ_k = √ã·v_k."

Step 1: v_k″ + (k² − z″/z) v_k = 0,  z = ã·√(2ε_H)·M_Pl_eff      (1)
        [canonical Mukhanov-Sasaki pin, agent-memory §Key Constants]
Step 2: z′(η̃) = z′_smooth(η̃) + [z′]·θ(η̃ − η̃_b)
        [definition of a sharp z′-jump; z itself continuous — a, ε_H bounded
        through the fold, so v acquires no δ′ pathology]
Step 3: z″(η̃) = z″_smooth(η̃) + [z′]·δ(η̃ − η̃_b)                  [θ′ = δ]
Step 4: z″/z = z″_smooth/z + ([z′]/z(η̃_b))·δ(η̃ − η̃_b)
        [f(η̃)δ(η̃−η̃_b) = f(η̃_b)δ(η̃−η̃_b) for f = 1/z continuous at η̃_b]
Step 5: ∫_{η̃_b−ϵ}^{η̃_b+ϵ} v″ dη̃ = ∫ (z″/z)·v dη̃  ⟹
        [v′] = ([z′]/z(η̃_b))·v(η̃_b) = [z′/z]·v(η̃_b)              (2)
Conclusion: Ω_v = [z′/z]. EXACT (no regime restriction).
```

The identical derivation run on the rescaled variable ψ_k = W·v_k with pump W: ψ″ + (k² − W″/W)ψ = 0; the delta weight is [W′/W]. For W = √ã (Sparn's 2+1D-BEC image; the WP's documented ψ_k = √a·v_k pump-correspondence):

```
Ω_ψ = [(√ã)′]/√ã(η̃_b) = (1/2)[ã′]/ã(η̃_b) = (1/2)ã[ã′]  at ã(η̃_b) = 1 ± 6e-4   (3)
```

— which is **exactly the plan's pinned `delta_weight_rule`**. Numerical confirmation from the npz keys: (1/2)ℋ̃ = 0.5 × 0.975393518773 = **0.487697**, vs Ω_on = +0.48716 / Ω_off = −0.48824, mean 0.48770 — exact to the on/off mean (the ±0.11% asymmetry is the ã, ℋ̃ growth across the window; the WP's intra-ψ nuance (1/2)[ã′] vs (1/2)ã[ã′] is 5.5×10⁻⁴ relative — three OOM below the fork adjudicated here).

**Verdict of (a)**: both weights are exact *in their own variable*. The fork is not an error in either rule — it is a **variable-choice fork**: Ω_ψ is the jump operator of the laboratory-IN analog variable (the √a-pump, Sparn's BEC projection of the transit); **Ω_v = [z′/z] is the jump operator of the substrate's own canonical phonon amplitude**. Substrate-first direction (`phononic-framing.md`): D_K eigenvalue flow → spectral moments → z″/z mode barrier → Bogoliubov |β_k|² — the z-pump IS the substrate barrier (the W5-1 chain's own Definition 1 identifies V_box ≅ (z″/z)|_fold); the √a-pump is the analog image. The gate as executed paired a z-pump box with √a-pump deltas — a hybrid whose origin is the plan-freeze pin itself (see §IV conflict flag), honestly disclosed by the producing agent's pump-correspondence paragraph.

### II.2 z′-jump attribution from the pinned channels — physical, decomposed 61% / 38% / ~1%

**Result**: Ω_z − Ω_ψ = 0.801 M_KK decomposes as 0.488 (pump-power kinematics, 60.9%) + ≈0.30 (genuine ε_H-flow at the fold, 37.6%) + ≈0.01 residual (quadratic ε-terms, M_Pl_eff(k)-flow, edge-vs-mean evaluation). **Not a channel-construction artifact.** Classification: PHONONIC.

This is sub-question (b). Substitution chain:

```
Claim: "The z-weight excess over the √a-image (±1.288 vs ±0.487) is physical:
        half is the pump-power factor (z ∝ ã¹ vs ψ-pump ã^{1/2}), the rest is
        the fold's ε_H-flow — the same η_H ≈ 0.956 physics as the branch-(b)/(c)
        barrier fork; it is NOT an s64 z_tau channel artifact."

Step 1: z = ã·√(2ε_H)·M_Pl_eff  ⟹  z′/z = ã′/ã + (1/2)ε_H′/ε_H + M′_eff/M_eff   (4)
        [log-derivative of the definition in (1)]
Step 2: ã′/ã|_edge = ℋ̃ = 0.97539 M_KK [s77 pair k_pivot/k_over_aH].
        The √a-image keeps only HALF of this: Ω_ψ = (1/2)ℋ̃ = 0.48770
        [matches npz Ω_on/off mean exactly, §II.1].
Step 3: ε-flow term: (1/2)ε_H′/ε_H = (1/2)ε₂ℋ̃ with ε₂ ≡ d ln ε_H/dN.
        From the stored-channel barrier ratio F_fold ≡ (z″/z)/ℋ̃² =
        2.76408/0.951392 = 2.9053 [WP "F_fold = 2.905" — exact match] and the
        standard expansion z″/z = ℋ̃²(2 − ε₁ + (3/2)ε₂ + O(ε²)):
        ε₂ = (2.9053 − 2 + ε₁)/1.5 = 0.604–0.618 for ε₁ ∈ [0, 0.022]
        ⟹ (1/2)ε₂ℋ̃ = 0.294–0.301 M_KK.
        [ε₂ > 0: ε_H GROWS through the window — the transit spikes ε_H;
        regime: the expansion drops O(ε₁ε₂, ε₂²) terms, the ~1% closure
        residual below]
Step 4: Sum: ℋ̃ + (1/2)ε₂ℋ̃ = 1.270–1.277 M_KK vs the pinned-channel value
        Ω_z = [z′/z] = 1.288 M_KK — closes to 0.9–1.4%.
Step 5: Excess attribution: Ω_z − Ω_ψ = 0.801 =
        0.4877 (the OTHER half of the ℋ̃-part; pure variable kinematics,
                present even in exact dS — NOT an ε-jump)            60.9%
      + ≈0.30  (ε_H-flow; genuine fold physics, η_H-violation class)  37.6%
      + ≈0.013 (residual: quadratic Hubble-flow terms + M_Pl_eff(k)-flow
                + edge-vs-window-mean evaluation)                     ~1.5%
Direction: both leading components are physical. The s64 z_tau channel passes
        its independent anchor cross-checks (W5-1 CHK-N non-circular
        re-derivation ratio 0.9999631; W5-2 s64 dS_fold anchor at 4.1e-10 rel)
        — channel construction is sound.
```

Internal consistency of the pinned channels: z″/z = (z′/z)′ + (z′/z)² requires (z′/z)′ = 2.7641 − 1.288² = 1.105 M_KK² — a *sustained fold-scale flow term*, implying z′/z grows by only 1.105 × Δη̃ ≈ 1.2×10⁻³ across the window (0.1%): the pump log-derivatives are effectively constant across the impulsive window, consistent with the box premise and with the 0.22% Ω_on/Ω_off asymmetry.

**One honest qualifier**: the impulsive window is SUB-GRID (δτ = 1.025×10⁻⁴ = 0.116 of one s64 grid cell; the cubic interpolant is the pinned machinery), so the **magnitude** 1.288 is the smooth fold-scale z′/z evaluated at the window edges (physical-as-pinned), while the **delta localization** — the jump TO ZERO outside — is the sudden-limit BD-in-out idealization (the true s64 profile does not vanish outside the window; the recipe's in/out regions are idealization-imposed). This localization assumption applies *identically to both weight conventions* (it is the validated BOX-DELTA-SUDDEN scheme itself, justified by kΔη̃ = 1.6×10⁻² ≪ 1 and H·dt = 0.663 < 1) and therefore does not bias the fork either way.

### II.3 The fork is weight-quadratic: |β_pivot|² ≈ (Ω·Δη̃)² — every documented channel reproduced

**Result**: in the delta-dominated, small-phase regime the recipe's pivot production obeys |β_pivot|² ≈ (ΩΔη̃)²; the weight fork is (Ω_z/Ω_ψ)² = 6.97, matching the reported ×6.96. Classification: PHONONIC (closed-form structure of the validated recipe).

Substitution chain, with the closed-form Born/junction limits reproducing all five documented numbers:

```
Claim: "|β_pivot|² scales as Ω² ⟹ the delta-weight pin is the single largest
        convention lever on the promoted value (×6.96)."

Step 1: single delta of weight Ω: match v_L = e^{−ikη̃} + r·e^{+ikη̃},
        v_R = t·e^{−ikη̃} under (2): continuity t = 1 + r; [v′] = Ω·v ⟹
        r = iΩ/(2k − iΩ),  |r|² = Ω²/(4k² + Ω²)        [exact 1-junction]
Step 2: on/off pair, opposite signs ±Ω, separation Δη̃ (phases interfere):
        β ≈ (Ω/2k)(1 − e^{2ikΔη̃}) ⟹ |β| ≈ (Ω/k)|sin kΔη̃| ≈ Ω·Δη̃
        [regime: Ω/k = 0.034–0.090 ≪ 1; kΔη̃ = 1.617e-2 ≪ 1 — both satisfied]
Step 3: numerical reproduction (documented values only):
        ψ-weight:  (0.48770 × 1.13014e-3)² = 3.038e-07  vs 3.0454e-07 (−0.25%)
        z-weight:  (1.288  × 1.13014e-3)² = 2.119e-06  vs 2.12e-06    (exact)
        box Born:  (V_box·Δη̃/2k)² = (1.90279×1.13014e-3/28.622)² = 5.645e-09
                   vs reported box-only 5.64e-09                      (exact)
        channel split: 3.06e-07/5.64e-09 = 54.3 vs reported ×54.2     (exact)
        phase: μ_pivot·Δη̃ = √(202.905)×1.13014e-3 = 1.60982e-2
                   vs WP 1.6098e-2                                    (exact)
Step 4: fork ratio: (Ω_z/Ω_ψ)² = (1.288/0.48770)² = 6.975;
        reported value ratio 2.12e-06/3.045e-07 = 6.96.               ✓
Conclusion: weight-quadratic confirmed; the −0.25% Step-3 residual on the
        ψ-row is the box term entering in near-quadrature (total 3.0454e-07
        sits 0.5% BELOW deltas-only 3.06e-07 — mild destructive interference)
        plus O((kΔη̃)²) corrections.
```

**Cancellation-depth corollary (why tuple coherence is load-bearing, not cosmetic)**:

```
Step 1: per-boundary reflection |r|² = Ω²/(4k²+Ω²):
        z-weight 2.02e-3; ψ-weight 2.90e-4
Step 2: net |β|² = |r|²·(2 sin kΔη̃)²·[1 + O(Ω/k, kΔη̃)];
        suppression (2 sin kΔη̃)² = 1.046e-3 ⟹ depth ≈ 956×
Step 3: check: 2.90e-4 × 1.046e-3 = 3.04e-07 ✓ (reported 3.045e-07)
Direction: the window value is a ~10³-deep two-boundary cancellation residual.
        Mixing conventions BETWEEN the two boundaries, or between the window
        stage and an adjacent ladder stage at composition, breaks the
        cancellation and injects error up to the per-boundary scale
        (10⁻³–10⁻⁴ in |β|²) — 3 OOM above the signal. The convention tuple is
        the recipe's validity condition.
```

### II.4 Consumer normalization and vacuum non-coincidence — v_k-quanta forced

**Result**: all three downstream consumers normalize to v_k-quanta; the ψ- and v-idealizations' BD-in-out vacua do NOT coincide at the fork-relevant level — the ×6.96 spread IS the vacuum-definition difference. Classification: PHONONIC.

This is sub-question (c). Substitution chain:

```
Claim: "S79 B2-ladder, GGE n_Bog, and the UNIFIED-AS-79 F_amp slot all count
        v_k-quanta; ã(boundary) = 1 ± 6e-4 does NOT make the two vacua
        coincide to better than ×6.96."

Step 1: S79 B-ladder: B1/B2/B3 are Bogoliubov (SU(1,1)) matrices between the
        SS and WKB bases OF THE v_k EQUATION (S79 P2-A canonical; agent-memory
        3-stage-ladder pin). Composition B3 = B2·W·B1-type products are only
        defined in a common basis.                          ⟹ v-quanta
Step 2: UNIFIED-AS-79 F_amp: the ledger factor multiplies P_ζ, and
        P_ζ = (k³/2π²)·|v_k/z|² — the amplified amplitude is v_k.
                                                            ⟹ v-quanta
Step 3: GGE n_Bog: relic occupation n_k = |β_k|² of the substrate's canonical
        phonon modes; the MS amplitude IS the substrate phonon variable
        (substrate-IS); ψ = √ã·v is the 2+1D-BEC laboratory-IN image.
                                                            ⟹ v-quanta
Step 4: vacuum-coincidence test. Amplitude map: √ã = 1 ± 3e-4 at the edges —
        harmless (the Sparn dictionary N_k = |b_k|²/|c_k|² is a RATIO,
        invariant under constant rescale). Derivative map:
        ψ′ = √ã·v′ + (√ã)′·v, and at the edges (√ã)′/√ã = 0.4877 ≠ z′/z = 1.288
        — the two BD-in-out vacuum PAIRS (mode, mode′) differ at first order
        in the pump flow.
Step 5: net occupation-amplitude offset after the on/off cancellation:
        β_z − β_ψ = ΔΩ·Δη̃ = (1.288 − 0.4877) × 1.13014e-3 = 9.045e-4
        — identically equal to √(2.119e-06) − √(3.038e-07) = 9.045e-4. The
        offset survives the cancellation at exactly the fork level.
Conclusion: NO — the vacua coincide only at the amplitude level (1 ± 3e-4);
        the pump-flow level mismatch IS the ×6.96. Consumer alignment forces
        the z-pump (v-quanta) pin for any value the B-ladder / F_amp / n_Bog
        chain consumes.
```

Note the structural reading this forces: the impulsive-window |β|² is a **stage coefficient in a declared convention** — meaningful for same-convention SU(1,1) composition with adjacent ladder stages (where the shared edge-vacuum conventions cancel telescopically) — not a stand-alone "particles produced at the fold" claim. That is also why the per-boundary 10⁻³ vacuum ambiguity (§II.3 corollary) is not a defect of the recipe: it cancels by construction *when and only when* both boundaries and both composed neighbors use one convention.

### II.5 The remaining tuple components: barrier branch, window, ladder stage

**(i) Barrier branch — pin branch (c), the stored s64 `zpp_over_z` channel.** The z-pump-consistent interior is the η_H-corrected stored channel (z″/z|_window = 2.7641 M_KK² = 1.4526× anchor): the SAME ε₂-flow physics that puts the 0.30 M_KK term into the weight (§II.2 Step 3) puts the (3/2)ε₂ term into the barrier — keeping it in the deltas while truncating it from the box (branch (b) = quasi-dS 2(ãH̃)² = 1.9028) would re-create a hybrid. Branch (b) retains exactly one role: the CHK-N normalization cross-check anchor (its actual function in-gate — it is k_pivot²/107.63558173571887 by construction, s77 script line 475, quasi-dS k²/(2aH²)). Precision chain:

```
Step 1: |β|²(c)/|β|²(b) − 1 = 3.0760e-07/3.0454e-07 − 1 = 1.005e-2   [WP table]
Step 2: Class-8.3 publication pin = 4 sig figs ⟹ downstream rel_tol ≥ 1e-4
Step 3: 1.005e-2 / 1e-4 = 100.5 — the branch choice moves the published value
        by ~100 units of its own precision floor
Direction: 1.005e-2 > 1e-4 ⟹ branch-distinguishable at publication precision
        ⟹ the branch MUST be pinned (an unpinned branch is Class-8 PRU freedom
        living at the value level).
```

Sub-horizon branch integrity under (c): μ_pivot² = k² − 2.76408 = 202.04 > 0, margin k²/V = 74.1× — the [VERIFY] chain's oscillating-sector conclusion (Schmidt Eq.-75 sin-branch) holds a fortiori; the promotion gate's chain restates it with the (c) barrier.

**(ii) Window — SETTLED at the canonical fold-conformal clock; not an open fork.**

```
Step 1: box+delta validity premise: interior ≈ plateau (flatness ≪ 1)
Step 2: canonical window (Δη̃ = 1.13014059e-3, τ ∈ [0.18994874, 0.19005127]):
        flatness 2.2e-3 ≪ 1 ⟹ box premise holds
Step 3: S38-internal-clock alternative (δτ = 0.0300, Δη_alt = 0.3349):
        flatness 0.92 = O(1) ⟹ interior NOT plateau-like ⟹ the box+delta
        class is INAPPLICABLE there (the WP's |β|²_alt = 1.29e-03 was computed
        under a broken premise — sensitivity seed only)
Direction: within scheme=BOX-DELTA-SUDDEN the window is structurally forced;
        the alternative is a different, unvalidated idealization class — any
        alt-window attempt is a NEW gate (plan/WP verbatim), never a re-pin.
```

**(iii) Ladder-stage anchor — declare IMPULSIVE-TRANSIT-WINDOW; non-comparable to B2 by construction.** log₁₀(3.045×10⁻⁷ / 1.7×10³) = −9.75 OOM against the S79 B2 anchor is a *stage-label mismatch, not a tension*: B2 spans post-fold-WKB → horizon-exit (≈3.1 e-folds of pump growth; N_pivot = 3.118), the window spans ΔN = ãH̃Δη̃ = 1.10×10⁻³ e-folds — a ~2800× e-fold-span mismatch under exponential pump growth. The F_amp-slot cross-check (F_amp^sc = 47.92, 3PI, a full-transit amplification object) is admissible ONLY through same-convention Bogoliubov composition with the ladder stages (which requires splitting S79's B1 at the window edges: B1 → B1a·W·B1b), never by direct magnitude comparison.

### II.6 W5-2 (S100b-FOLD-RANGE-SCALING) — orthogonal to the adjudication

**Result**: Rao v > v_c range-controlled class PINNED (ΔP_exc = 1.57×10⁻³ < 0.01 over Mach ∈ [5, 30], 6.43× inside the rate-flat boundary ε_b = 4.394×10⁻³; ρ_S = 1.000000, p_range = 1.00); rate-controlled KZ class EXCLUDED; Li diagnostic z′_eff = 2.090 < z + 1/ν = 3.904 SURVIVAL side with νz ≈ 1 an analytic first-order slope (fold tricritical-ADJACENT only). Classification: PHONONIC.

Recorded here for source completeness; it shares no convention surface with the delta-weight fork (P_exc and n_rel are LZ-class per-mode quantities, weight-independent), and its own CF (CF-S101-TRICRITICAL-ADJACENCY) propagates unchanged. The two PASSes compose substrate-first: the relic content is a COUNT of modes inside the spectral-excursion window (range), and the validated box+delta recipe prices the per-mode window deposit — at whichever weight convention the promotion gate now pins.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S100b-BOX-DELTA-BOGOLIUBOV (W5-1) | **PASS** (sign/magnitude/regime = PASS/PASS/VALID) | var_Nseg = 1.0000000006 < 2.0; rel_dev = 1.631×10⁻⁶ ≤ 0.10; payload `beta2_pivot=3.045e-07` (audit `297a597c3cfe6fa00eddf97cccc538241f12faf339793c05a195ad915e7e6498`) |
| S100b-FOLD-RANGE-SCALING (W5-2) | **PASS** (PASS/PASS/VALID) | ΔP_exc = 1.57×10⁻³ < 0.01; ρ_S = 1.000000 > 0.99 (audit `683a7e22e476411d41587ec7f23444e109b6f7dffaaa0d6436b4e663a5a53bc3`) |

Both verdicts authoritative and untouched. The W5-1 PASS is delta-weight-invariant (identical Ω enters both sides of each criterion); the VALUE in its payload is convention-conditioned — that is the entire subject of this adjudication. No UNTRUSTED-UPSTREAM caveat applies to either gate (W5 is not an s84-cache consumer; verdict rows carry no caveat).

---

## IV. Structural Implications

**1. The fork's origin is plan-freeze, not execution (conflict flag).** The plan's §W5-1 block is internally hybrid: its substitution-chain Definition 1 identifies `V_box ≅ (z″/z)|_fold` (z-pump interior) while its `delta_weight_rule` pins `Ω = (1/2)a[ȧ]` (√a-pump boundaries). The producing agent executed the pins faithfully and DISCLOSED the mismatch (the pump-correspondence paragraph: Sparn's Eq.-4 potential is the √a-pump barrier (1/2)a″/a − (1/4)(a′/a)² ≈ (3/4 − ε/2)(ãH̃)², plateau 0.7187 = 0.378·V_box; the substrate barrier is the z-pump z″/z ≈ 2(ãH̃)² → 2.7641 η_H-corrected). No execution fault, no convention-shopping; a plan-level convention hybrid surfaced honestly. The repair point is the NEXT gate's pre-registration — exactly where this synthesis lands it.

**2. The WP's CF-S101 draft would inherit the hybrid silently (conflict flag).** The Wave-5 synthesis CF spec reads "promote `beta2_pivot_box_delta = 3.045e-07`" — i.e., as drafted, the promotion gate would canonize the √a-pump-weighted hybrid number under a v-quanta-consuming slot. This synthesis REVISES that CF (§V): the promotion gate pins the adjudicated tuple and computes the v-quanta value in-gate; the 3.045×10⁻⁷ payload remains permanently on the W5-1 verdict line as the Sparn-literal recipe benchmark (it is what the closed-form match validated at machine precision) and is carried forward as a keyed diagnostic, not the canonical.

**3. What the adjudication closes.** (i) The ×6.96 silent-inheritance hazard — resolved by structural derivation (§II.1, §II.4), not by preference: the substrate-IS jump operator is [z′/z] and every consumer counts v-quanta. (ii) The barrier-branch freedom — branch (c) is forced by ε₂-flow self-consistency with the weight, and the 1.0% (b)↔(c) fork sits 100× above the 4-s.f. publication floor, so the pin is mandatory (Class-8.3). (iii) The window question — settled structurally by the plateau-flatness argument (2.2×10⁻³ vs 0.92); the S38-internal-clock reading is inadmissible *for this scheme class*. (iv) The ladder-stage ambiguity — the value anchors a NEW stage (impulsive window), non-comparable to B2 at −9.75 OOM by e-fold-span construction.

**4. What it sharpens about the recipe itself.** The window |β|² is a ~10³-deep cancellation residual (§II.3 corollary): per-boundary junction mixing (2×10⁻³ at Ω_z) exceeds the net signal (2.1×10⁻⁶) by three OOM and cancels only under per-boundary and per-stage convention coherence. The promoted constant is therefore a *composition input* (one SU(1,1) factor of the B-ladder in v-quanta), and the F_amp-slot cross-check must be built as a composition (B1a·W·B1b stage split), never as a magnitude comparison. This is the quantitative form of the Parra-López switch-dominance structure already in the verdict payload (deltas/box = ×54.2): production lives at the switch-on/off of the spectral reorganization — the transit IS the physics — and so does the convention-sensitivity.

**5. M-S-inapplicability wall respected throughout.** The fold history (N_e = 7.75, η_H ≈ 0.956, permanent) forbids slow-roll consistency relations; the gate used the EXACT mode equation, and this adjudication used only distribution theory plus the exact junction solution. The η_H residue enters precisely twice, as pinned physics: the branch-(b)/(c) barrier fork (1.4526×) and the ε₂-flow component of the weight (0.30 M_KK) — the same physics, kept coherently on both tuple components by the recommendation.

**6. THE COMPLETE CONVENTION-TUPLE RECOMMENDATION** (the deliverable CF-S101-BETA-PIVOT-PROMOTION's S101 pre-registration consumes):

| Tuple component | PIN | Basis (this synthesis) |
|:----------------|:----|:-----------------------|
| **Delta-weight rule** | `Z-PUMP: Ω = [z′/z]` at both switch boundaries (±1.288 M_KK from the pinned s64 z_tau channel at the window edges; per-edge values read from the channel in-gate) | §II.1 chain (substrate-IS jump operator, EXACT); §II.4 (consumers are v-quanta; vacua do not coincide); §II.3 (weight-quadratic ⟹ largest lever, ×6.96). The Sparn-literal `√a-PUMP: Ω = (1/2)ã[ã′]` (±0.487) is DEMOTED to recipe-benchmark/diagnostic, retained as a keyed companion. |
| **Barrier branch** | `(c) stored s64 zpp_over_z channel` (η_H-corrected; z″/z\|_window = 2.7641 M_KK² = 1.4526× anchor). Branch (b) 2(ãH̃)² retained ONLY as the CHK-N normalization cross-check anchor. | §II.5(i): ε₂-flow self-consistency with the weight; +1.005% fork = 100× the 4-s.f. floor ⟹ pin MANDATORY; μ²(c) = 202.04 > 0 (margin 74×, sin-branch intact). |
| **Window** | `CANONICAL FOLD-CONFORMAL CLOCK`: Δη̃ = 1.13014059×10⁻³ (conformal image of dt_transit in fold-normalized M_KK clock); τ ∈ [0.18994874, 0.19005127] | §II.5(ii): SETTLED — plateau flatness 2.2×10⁻³ ≪ 1 vs 0.92 under the S38-internal-clock alternative (box premise violated there; alt window = NEW gate, inadmissible as a re-pin). |
| **Ladder-stage anchor** | `IMPULSIVE-TRANSIT-WINDOW stage` (BD-in-out at the window edges; ΔN = 1.10×10⁻³ e-folds) — a stage DISTINCT from S79 B1/B2/B3 | §II.5(iii): −9.75 OOM vs \|β₂\|² ~ 1.7×10³ is non-comparable by construction (e-fold-span mismatch ~2800×); F_amp-slot cross-check via same-convention composition only (B1 → B1a·W·B1b split). |

Carried unchanged from W5-1 (declare, do not re-derive): scheme = BOX-DELTA-SUDDEN; convention = BD-in-out with an explicit **v-quanta / Z-PUMP suffix** on the promotion verdict line (e.g. `convention=BD-in-out-Z-PUMP-branchC-foldclock`, satisfying the multi-axis convention-tag discipline); fold normalization Convention B (ã(τ_fold) = 1) with CHK-N against k_pivot²/107.63558173571887; publication precision 4 s.f. with npz round-trip rel_tol ≥ 1e-4 (Class-8.3 items 1–3); unitarity ≤ 1×10⁻¹⁰ at every evaluation. **Value consequence**: under this tuple the canonical value is the (Ω_z, branch-(c)) recompute — Born-limit estimate band [2.119, 2.140]×10⁻⁶ ((Ω_zΔη̃)² = 2.119×10⁻⁶; branch-(c) correction ≤ +1.0%, smaller than at Ω_ψ since the box fraction is ×6.96 relatively weaker) — computed in-gate from the pinned channels, never promoted from this estimate. The 3.045×10⁻⁷ payload value is promoted ONLY as the keyed diagnostic `*_sqrtA_recipe` companion (pathway-keyed per the canonical write-order's structured-prediction sub-keying).

---

## V. Carry-Forward Computations

V.1. **CF-S101-BETA-PIVOT-PROMOTION (REVISED) — tuple-pinned recompute + canonical promotion of the fold impulsive-window |β_pivot|²**
   - **What**: re-evaluate the W5-1-validated box+delta recipe at the adjudicated tuple — weight Ω = [z′/z] per edge from the s64 z_tau channel (≈ ±1.288 M_KK), interior = stored `zpp_over_z` window mean (2.7641 M_KK², branch (c)), canonical fold-conformal-clock window, BD-in-out v-quanta — outputting `beta2_pivot_box_delta` (canonical, v-quanta; expected O(2.1×10⁻⁶)) plus the keyed diagnostic `beta2_pivot_box_delta_sqrtA_recipe = 3.045e-07` (the permanent W5-1 payload), each with the weight-decomposition diagnostic print (ℋ̃-part + (1/2)ε₂ℋ̃-part + residual per §II.2); then execute canonical write-order Steps 1–2 (verdict line → `update_constant`) with the FULL 4-component tuple in the PROVENANCE comment and a `convention=BD-in-out-Z-PUMP-branchC-foldclock` verdict tag.
   - **Inputs**: `computations/session-100b/s100b_box_delta_bogoliubov.npz` (V_box, Omega_on/off, Delta_eta, branchC keys, full-float64 β² values; SHA on disk), `computations/session-64/s64_mukhanov_sasaki.npz` (z_tau, zpp_over_z; SHA `e671f535…`), `computations/session-77/s77_n_pivot_map.npz` (k_pivot_com_fold, k2_over_zppz_fold; SHA `80fbf580…`), canonical_constants names `tau_fold`, `dt_transit`, `M_KK`.
   - **Gate**: revised CF-S101-BETA-PIVOT-PROMOTION pre-registration — PASS iff (i) recipe-internal criteria hold at the new tuple (unitarity ≤ 1×10⁻¹⁰ ABS; var_Nseg < 2.0 RATIO re-emitted; μ_pivot² > 0 sign row), (ii) the npz↔published round-trip holds at rel_tol ≥ 1×10⁻⁴ (Class-8.3), and (iii) the constant lands with the complete tuple + both keyed values. The Born-limit band [2.119, 2.140]×10⁻⁶ is a pre-registered DIAGNOSTIC cross-check (reported, never gated — the value is an output, not a target).
   - **Effort**: ≤ 1 h, 1 agent (parameter re-evaluation of a validated recipe + write-order Steps 1–2).

V.2. **CF-S101-LADDER-COMPOSITION — B1 stage-split and same-convention F_amp-slot cross-check**
   - **What**: split the S79 B1 stage (pre-fold SS → post-fold WKB) at the impulsive-window edges into B1a·W·B1b with W = the V.1 window stage (v-quanta SU(1,1) matrix from (α, β) at the adjudicated tuple); verify the composed |β|² across B1a·W·B1b reproduces the unsplit B1 within the per-boundary convention-coherence bound (§II.3 corollary), then carry the composition through B2 to state the F_amp-slot consistency claim at the ladder level (coherent-phase-limit caveat per the S79 product rule).
   - **Inputs**: V.1 outputs (window-stage (α, β) v-quanta), S79 P2-A ladder machinery + B1/B2 stage values (`sessions/archive/session-79/workshops/p2-a-as-ledger-dissonance.md`, SHA `2f2058…`; B1 |β₁|² ≈ 4.3×10⁴, B2 |β₂|² ≈ 1.7×10³ anchors), `s64_mukhanov_sasaki.npz` channels, UNIFIED-AS-79 F_amp slot spec (F_amp^sc = 47.92, slot-adjusted 0.3885).
   - **Gate**: NEW gate at S101 plan-freeze — PASS iff |composed(B1a·W·B1b)|²/|B1|² − 1 lands within a pre-registered band set at gate authorship from the §II.3 cancellation-depth arithmetic (the window stage perturbs B1 at the (ΩΔη̃)-amplitude level ≈ 1.5×10⁻³, so a band of O(10⁻²) RATIO is the natural pre-registration; planner pins the final number); INFO if composition is stable but the F_amp-slot statement requires phase information the S79 anchors do not carry (coherent-phase caveat fires).
   - **Effort**: 2–4 h, 1 agent (half-session compute; consumes V.1).

(CF-S101-TRICRITICAL-ADJACENCY from W5-2 propagates UNCHANGED — it shares no surface with this adjudication; its 4-field spec stands as written in the WP.)

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Substrate-IS jump operator at the fold's switch boundaries = [z′/z]·δ (EXACT distribution theory); pinned (1/2)ã[ã′] is the √a-pump (laboratory-analog) weight | PHONONIC | Derived (chain §II.1) | Resolves fork direction: z-pump is the substrate convention |
| 2 | Ω_z attribution: 1.288 = ℋ̃ (0.975) + ε₂-flow (≈0.30, ε₂ ≈ 0.60–0.62 from F_fold = 2.905) + ~1% residual; excess over √a-image = 61% kinematics + 38% ε_H-flow; channel sound (CHK-N 0.9999631) | PHONONIC | Derived + cross-checked (§II.2) | z-weight is physical, not a z_tau channel artifact; only delta-LOCALIZATION is idealization (both conventions equally) |
| 3 | \|β_pivot\|² ≈ (ΩΔη̃)², cancellation depth ≈956×; fork = (Ω_z/Ω_ψ)² = 6.97 ≡ reported ×6.96; all five documented channels reproduced closed-form (3.045e-07, 2.12e-06, 5.64e-09, ×54.2, μΔη̃ = 1.6098e-2) | PHONONIC | Verified (§II.3) | Weight is the dominant convention lever; tuple coherence is the recipe's validity condition |
| 4 | Consumers (S79 B-ladder, GGE n_Bog, UNIFIED-AS-79 F_amp) all normalize to v_k-quanta; ψ/v BD-in-out vacua differ at exactly the fork level (ΔΩ·Δη̃ = 9.045×10⁻⁴ amplitude) despite ã(edge) = 1 ± 6×10⁻⁴ | PHONONIC | Derived (§II.4) | Promotion value MUST be v-quanta (z-pump) |
| 5 | Barrier branch (b)↔(c) fork = +1.005% = 100× the 4-s.f. Class-8.3 floor; branch (c) forced by ε₂-coherence with the weight; μ²(c) = 202.04 > 0 (margin 74×) | PHONONIC | Derived (§II.5(i)) | Branch pin MANDATORY in the promotion gate |
| 6 | Window settled at canonical fold-conformal clock (flatness 2.2×10⁻³ vs 0.92); ladder stage = IMPULSIVE-TRANSIT-WINDOW, non-comparable to B2 (−9.75 OOM = stage-span label, ~2800× e-fold mismatch) | PHONONIC | Settled (§II.5(ii–iii)) | Two tuple components closed structurally; F_amp cross-check by composition only |
| 7 | COMPLETE TUPLE: (Z-PUMP [z′/z]; branch-(c) stored z″/z; fold-conformal-clock window; impulsive-window stage) + v-quanta convention tag; canonical value = in-gate recompute (est. band [2.119, 2.140]×10⁻⁶); 3.045×10⁻⁷ retained as keyed √a-recipe diagnostic | PHONONIC | RECOMMENDED (§IV.6) | CF-S101-BETA-PIVOT-PROMOTION pins by adjudication, not silent inheritance |
| 8 | W5-1, W5-2 gate PASSes authoritative and weight-invariant; W5-2 Rao range-controlled pin orthogonal to the fork | PHONONIC | Authoritative (§III) | No verdict re-adjudication anywhere in this synthesis |
