# Session 88 W5 Synthesis: §W1c-69 SIGN_VERDICT=PASS Reading — Substrate-Physics Directional Evidence vs Sign-Tautology by Non-Negative-Factor Algebra

**Date**: 2026-05-07
**Agent**: mack-cosmic-bridge (solo review; no opposing agent — sagan-empiricist's adversarial reading is steelmanned within this synthesis but the structural verdict is sole-authored)
**Source Documents**:
- `sessions/archive/session-88/session-88-w1c-workingpaper.md` (W1c results working paper, 745 lines; §W1c-69 lines 297-589)
- `sessions/session-plan/session-88-plan-w1c.md` (W1c plan, §W1c-69 gate block lines 297-389)
- `sessions/archive/session-88/workshops/_seed-w1c.md` (workshop seed; Workshop 1 lines 12-18)
- `computations/session-88/s88_gate_verdicts.txt` (lines 34-36; canonical + dual-SHA + 3-tuple `audit_sha256=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` `content_sha256=5d2597a55ecfa8696b9e91f894b083cdbda862c7272c1df44025168ae93c122a`; schema-v2 `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`)
- Agent memory: `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md`

---

## I. Session Outcome

The §W1c-69 schema-v2 3-tuple `(sign=PASS, magnitude=PASS, regime=VALID)` survives as a directional-evidence verdict only at the **upper-band edge** of the upstream CF-CURV-6 prior. Its sign component is **algebra-INVARIANT-with-DISCRIMINATING-CONTENT** (NOT vacuous, NOT algebra-DEPENDENT) — discriminating against substrate-internal counterfactual variants (F-H5 NEGATIVE, oscillatory branching, depopulating cascade) which are ruled out by *substrate-IS* monotonicity rather than by non-negative-factor algebra alone — but at the same time the magnitude reading is **band-edge-only PASS**: the WP §4 "2-OOM narrowing" framing is structurally a **band-edge consistency** statement, not a substrate-side narrowing of the CF-CURV-6 prior. The verdict line is permanent (no edit per `gate-verdicts.md §"Verdicts are permanent"`); the registry annotation in `falsifier-master-inventory` for CF-W1c-1 MUST carry both clauses (sign-PASS-with-discriminating-content + magnitude-PASS-only-at-upper-edge) and the §W4 "2-OOM narrowing" team-lead framing receives **NO-GO** as a CF-CURV-6 tightening; it is downgraded to a **tension diagnostic** for CF-W1c-2.

---

## II. Key Results

### II.1 Sign-prediction substitution chain — substrate-IS factor accounting

**Result**: The δ[Z/H] sign-prediction is **algebra-INVARIANT with DISCRIMINATING CONTENT** at the substrate-monotonicity layer. Classification: **PARTICLE** (cascade-tail Hawking spectrum + non-thermal MeV injection → Wagoner BBN → emergent [Z/H] excess); the *sign-prediction itself* is a substrate-IS structural identity, not a non-negative-factor tautology.

The substitution chain at WP §W1c-69 Step 4 reads:

- **Step 1 (definition)**: per-baryon non-thermal injection rate is `dE_inject/dt/n_baryon = n_PBH · L_H / n_baryon` with `n_PBH ≥ 0` (number density), `L_H ≥ 0` (Hawking luminosity flux), `n_baryon > 0` (BBN-epoch comoving baryon density).
- **Step 2 (substitution)**: at mid-band n_PBH = 1e-25 m⁻³, L_H = 3.5e19 W, n_baryon = 1e9 m⁻³ → injection_rate ≈ 0.02185 MeV/baryon/s (verified Python).
- **Step 3 (simplify)**: `δ_excess = injection_rate · t_BBN · F-H5 · branching` with t_BBN = 1000 s, F-H5 = +0.0127, branching = 0.01.
- **Step 4 (direction)**: `δ[Z/H] = log₁₀(1 + δ_excess)`. Since each factor in the product `n_PBH · L_H · F-H5 · branching · t_BBN` is **strictly non-negative on the substrate's IS realization at τ_fold**, the product is non-negative; the log-transform is monotone-increasing; therefore `δ[Z/H] ≥ 0` always.

**Structural distinction (this is the load-bearing point)**: the sagan-empiricist sign-tautology reading would be valid IF "non-negative" were imposed by **algebraic convention alone** (e.g., n_PBH ≥ 0 by physical-density definition, L_H ≥ 0 by branching-ratio convention). It is NOT valid here because the four substrate-physics factors carry *signed* substrate-IS content that COULD have been negative under a counterfactual substrate variant:

1. **F-H5 = +0.0127**: this is the *S87 J8 PROVEN* rank-2 Klein-V_4 modulation amplitude. The substrate's pixelation-lock workshop closure pinned **the SIGN of F-H5 as +**; the alternative substrate variant F-H5 NEGATIVE (≡ V_4 modulation that *suppresses* MeV-scale (n,γ) channels relative to thermal-Hawking baseline) is *structurally EXCLUDED* by the J8 derivation (rank-2 Klein-V_4 acts as a **constructive** modulation on the cascade-tail spectrum near the deuterium-bottleneck threshold). Were F-H5 a free sign, both signs would be admissible by non-negative-factor algebra; the sign-PASS would then BE tautological. F-H5's sign IS substrate-content.

2. **branching-to-metals = +0.01**: this is the BBN-network branching ratio for non-thermal MeV injection into nuclei heavier than He. Substrate-IS content: the cascade-tail Hawking spectrum at T_H ≈ 1 MeV is ABOVE the deuterium-bottleneck threshold (T_nuc ~ 0.070 MeV), so injected energy populates the (n,γ) and (γ,n) channels constructively. A counterfactual cascade-tail spectrum BELOW threshold would have `branching ≤ 0` (energy lost to thermal-photon dilution rather than nuclear branching) — substrate-content again.

3. **n_PBH(g_BBN)**: the cumulative-fraction-evap-today formula projects the cascade-tail population at generation g ≈ 322 to a non-negative number density (depopulating the population requires `dn_PBH/dg < 0` integrated negatively, which the cascade-tail-pile-up factor structurally PROHIBITS — see CF-CURV-6 derivation at W1a-59).

4. **L_H(M = 10¹³ kg)**: at cascade-tail mass, Hawking radiation is in the thermal-emission regime; positive flux is a substrate-IS property of `(A_K, H_K, D_K)` projected onto the BdG-spectral-triple sector with positive Hawking-temperature.

The four signs together produce a strict positivity result that DEPENDS on substrate-IS content (rank-2 Klein-V_4 modulation sign + above-threshold cascade-tail temperature + cumulative-pile-up non-negativity + thermal-emission-regime positivity). Any of these signs flipped by a counterfactual substrate variant produces a sign-FAIL. **Therefore the sign-prediction is non-trivial.**

### II.2 Discriminating counterfactual specification (Q1c.b)

**Result**: A concrete counterfactual substrate variant that produces sign-FAIL exists and is structurally exclusive of the framework's J8/CF-CURV-6 closure. Classification: **GEOMETRIC** (counterfactual lives in the rank-2 Klein-V_4 modulation moduli, not in any laboratory observable).

**Counterfactual variant CV-1: F-H5 NEGATIVE**. If the substrate's rank-2 Klein-V_4 modulation acted **destructively** on the (n,γ) channels at MeV-scale (i.e., if J8 had closed at F-H5 = −0.0127 instead of +0.0127), the substitution chain would produce `δ_excess < 0` (depopulation of metals relative to thermal-Hawking baseline) → `δ[Z/H] = log₁₀(1 + δ_excess) < 0`. Observed [Z/H] excess at Maiolino+24/Bunker+23 is strictly **positive** (+0.3 to +0.5 dex). CV-1 produces sign-FAIL by direct contradiction with observed direction.

**Counterfactual variant CV-2: oscillatory cascade with negative branching at the BBN-mass cohort**. If the cascade-tail population at generation g_BBN ≈ 322 had `dn_PBH/dg` oscillatory (some generations net-emit, some net-absorb) such that the BBN-epoch injection integrated negatively, `δ[Z/H]` could fall below zero. CF-CURV-6 PASS structurally excludes this (cascade-tail-pile-up factor is *monotone* in g, per W1a-59 closure).

**Counterfactual variant CV-3: cascade-tail temperature BELOW deuterium-bottleneck**. If `T_H(M = 10¹³ kg) < 0.070 MeV` (i.e., if the cascade-tail mass M were ~10¹⁵ kg instead of 10¹³ kg), `branching-to-metals ~ 0` and δ[Z/H] would be undetectably small but still ≥ 0 (sign-PASS preserved, magnitude vacuous). Distinct from the sign question; relevant to CF-CURV-7 mass anchor not the sign verdict.

**Direct sign-FAIL discriminators against alternative LRD-metallicity mechanisms**:

| Alternative mechanism | Predicted δ[Z/H] sign | Sign-discriminator vs substrate? |
|:---|:---:|:---|
| Late-time AGN feedback (Z dilution from outflow) | + (always positive on outskirts where new metals flow out) | NO sign discriminator (both predict +) |
| IMF top-heaviness (more massive stars → more metals) | + | NO sign discriminator (both predict +) |
| Pop-III chemical enrichment | + | NO sign discriminator (both predict +) |
| Cascade-tail-Hawking + F-H5 NEGATIVE (CV-1) | − | YES — substrate's actual J8 closure rules this out by structural identity |
| Cascade-tail-Hawking + below-bottleneck mass (CV-3) | 0 (vacuous) | YES — substrate's CF-CURV-7 mass anchor rules this out |

The sagan-empiricist reading captures something true: **against external alternative-mechanism sign-direction comparisons, the +sign is non-discriminating** (every plausible LRD-metallicity mechanism produces +sign, so observing +sign at z=6-8 LRD environments is consistent with all of them). But the sagan-reading misses that the substrate's sign-prediction is discriminating against **internal substrate counterfactuals** (CV-1, CV-2, CV-3). This is the algebra-INVARIANT-with-DISCRIMINATING-CONTENT category, not algebra-INVARIANT-vacuous.

### II.3 Magnitude reading: band-edge consistency vs substrate-side narrowing

**Result**: The team-lead "2-OOM narrowing" framing is structurally a **band-edge consistency** statement, NOT a substrate-side narrowing of CF-CURV-6. Classification: **NON-PHONONIC** (statistical / observational interpretation question; no direct phononic substrate consequence — the substrate cascade structure is unchanged either way, only the inferred n_PBH window narrows or fails to narrow).

Numerical re-verification (Python; canonical values from `s88_w1c_u1_bbn_chunky_hawking_metallicity.npz`):

```
Substitution chain:
  Step 1 (def):  δ[Z/H] = log₁₀(1 + n_PBH · L_H · F-H5 · branching · t_BBN / (n_baryon · E_baryon))
  Step 2 (sub):  proportional to n_PBH directly through the chain
  Step 3 (sim):  log₁₀(1 + δ_excess) with δ_excess ∝ n_PBH
  Step 4 (dir):  monotone-increasing in n_PBH

Three grid-point evaluations:
  n_PBH = 1e-28 m⁻³  →  δ[Z/H] = +1.205e-06 dex  (5.52 OOM below Maiolino+24 +0.4)
  n_PBH = 1e-25 m⁻³  →  δ[Z/H] = +1.203e-03 dex  (2.52 OOM below Maiolino+24 +0.4)
  n_PBH = 1e-22 m⁻³  →  δ[Z/H] = +5.768e-01 dex  (0.18 above; PASS within 0.3 threshold)

PASS-magnitude window:    n_PBH ≈ 5.450e-23 m⁻³  (Python re-derived from inverse map; matches WP)
CF-CURV-6 prior band:     [1e-30, 1e-20] m⁻³ (10 OOM wide)
PASS-magnitude window:    sits at log₁₀(5.45e-23) = -22.264
                          → 2.26 OOM BELOW upper edge (1e-20)
                          → 2.74 OOM ABOVE mid-band (1e-25)
```

**Substitution chain on the "narrowing" claim**:

- **Step 1 (def)**: "narrowing" of an observational prior means the posterior support is a strict subset of the prior support, with reduced width.
- **Step 2 (sub)**: prior CF-CURV-6 = log-uniform on [1e-30, 1e-20]; PASS-magnitude posterior support = neighborhood of n_PBH ≈ 5.45e-23 with width set by the magnitude-tier 0.3 dex tolerance.
- **Step 3 (sim)**: solving `log₁₀(1 + n_PBH/5.45e-23 · 1.51) ∈ [0.4 − 0.3, 0.4 + 0.3]` for n_PBH gives an asymmetric support running from approximately n_PBH ≈ 8.4e-24 to n_PBH ≈ 2.2e-22 (≈ 1.4 OOM wide, half-width ≈ 0.7 OOM each side of the central 5.45e-23).
- **Step 4 (dir)**: the posterior support [8.4e-24, 2.2e-22] is a strict subset of the prior [1e-30, 1e-20], and is bounded *above* by the prior upper edge (the upper end of the posterior at 2.2e-22 is barely 0.66 OOM below the prior's upper bound 1e-20).

The **direction of the constraint** matters: this is consistent with a "narrowing" interpretation IF the inferred posterior median (5.45e-23) sits comfortably interior to the prior; it is a "barely consistent at upper edge" interpretation IF the posterior is pushed up against the prior's upper boundary. The numbers say: **the inferred posterior central value sits 2.26 OOM below the prior upper edge** — this is interior, but only narrowly so (2.26 OOM in a 10-OOM prior is 22.6% of the way down from the top). The mid-band of CF-CURV-6's prior fails magnitude by 2.5 OOM and is excluded; the posterior is therefore pushed toward the top quintile of the prior.

This pattern is closer to **"barely consistent at upper end"** than to **"comfortably narrowed central value"**. The team-lead WP §4 framing ("2-OOM narrowing toward upper-band n_PBH") is technically true (the posterior IS narrower than the prior by ~2 OOM), but rhetorically it understates the structural finding: the substrate prediction REQUIRES n_PBH at the upper 22.6% of the prior to reproduce observed [Z/H], with mid-band and lower-band ruled out by 2.52 to 5.52 OOM respectively. This is informative — but the informativeness is **as much an upper-edge-constraint diagnostic as it is a narrowing**.

### II.4 Algebra-axis classification (Q1c.e)

**Result**: The δ[Z/H] sign-prediction maps to the **algebra-INVARIANT-with-DISCRIMINATING-CONTENT** sub-class. Classification: **GEOMETRIC** (algebra-axis structural classification per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3).

Per the algebra-axis K-counter (K=3 MANDATORY at S87 W-2 R3 close):

- **algebra-INVARIANT** (spectrum-only functionals; `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`): observables that depend only on the spectrum of D_K (or its derived spectrum after Mellin/zeta projection). The sign of `n_PBH · L_H · F-H5 · branching · t_BBN` factors through (i) the cascade-tail Hawking spectrum (spectral); (ii) the rank-2 Klein-V_4 modulation amplitude (J8 spectral pin at MeV-scale); (iii) the branching-ratio sign (a thresholding property of the spectrum vs the deuterium-bottleneck cutoff). All three are **spectrum-only properties** — algebra-INVARIANT.
- **algebra-DEPENDENT** (state-pair functionals on `A`): would arise if the prediction depended on a state-pair functional, e.g., a non-trivial off-diagonal density-matrix element on the BdG sub-algebra. The §W1c-69 prediction does NOT factor through any state-pair functional; the BBN-network forward calculation operates on energy-deposition rates derived from spectrum-only Hawking flux + spectrum-only branching ratios.

Within algebra-INVARIANT, the sub-classes admitted by the existing taxonomy are:

| Sub-class | Definition | This work? |
|:---|:---|:---|
| INVARIANT-vacuous | sign-prediction follows from algebraic non-negativity convention alone (no substrate-IS content distinguishes the prediction from any alternative model with positive sign) | NO — counterfactuals CV-1/CV-2/CV-3 demonstrate substrate content |
| INVARIANT-with-DISCRIMINATING-CONTENT | sign-prediction follows from substrate-IS spectrum-only properties; counterfactual substrate variants exist that produce sign-FAIL | **YES** — CV-1 (F-H5 NEGATIVE) is the definitional counterfactual |
| DEPENDENT | prediction depends on state-pair functional; algebra-DEPENDENT class | NO — no state-functional dependence in the chain |

The Pole-Scope MANDATORY-K=4 sub-clause (S88 W7a-72) per `epistemic-discipline.md §"Pole-Scope sub-clause"` does NOT directly apply here because §W1c-69 is not a Mellin-cone pole observable; the substrate-distance pole structure of `D_K^{-2s}` is one cohomological layer above the BBN-network forward calculation. However, the F-H5 = +0.0127 anchor itself is a **spectrum-only modulation amplitude at MeV-scale** that traces back to the J8 pixelation-lock spectral residue at substrate-distance pole s=4 (per S87 J8 closure). The sign-prediction is therefore **pole-scoped to the J8 substrate-distance-2 anchor**, and any pole-extension analysis would inherit the F-H5 sign from the J8 anchor. This is consistent with the K=4 corpus pattern: pole-specificity locks the sign at the pole where F-H5 is structurally pinned.

### II.5 Calibration-corpus extension to S88 W13 W-1 profile-invariance pattern

**Result**: §W1c-69 sign-PASS-with-discriminating-content is structurally analogous to S88 W13 W-1 profile-invariance at 6.68e-17 — both are "INVARIANT-vs-tautology" reading divergences. Classification: **NON-PHONONIC** (methodology-axis K-counter calibration corpus extension).

Per the seed file Workshop 1 cross-link, the W1c-69 reading-divergence has the same shape as the S88 W13 W-1 pattern (profile-invariance at 6.68e-17 floor, substrate-IS coherence vs K_ω-class-independence tautology). In both cases:

- One reading frames the result as **substrate-IS structural content** (substrate cascade produces +δ[Z/H] / substrate produces 6.68e-17 invariance by structural identity).
- The opposing reading frames it as a **definitional consequence of construction** (non-negative factors / class-independence by construction).

The structural verdict procedure is identical:

1. Enumerate the factors entering the prediction.
2. For each factor, identify whether its sign/direction encodes substrate-IS content (i.e., whether a counterfactual substrate variant could flip it).
3. If at least one factor encodes substrate content → INVARIANT-with-DISCRIMINATING-CONTENT (non-trivial).
4. If all factors are non-negative-by-convention → INVARIANT-vacuous (tautology).

Both W1c-69 and W13 W-1 should land at INVARIANT-with-DISCRIMINATING-CONTENT *if* the substrate content can be exhibited via at least one counterfactual; INVARIANT-vacuous otherwise. This procedure is the calibration-corpus content; promoting it to MANDATORY sub-class structure under the algebra-axis K-counter requires K=3 distinct calibration instances. With W1c-69 (sign-prediction) + W13 W-1 (profile-invariance) we have K=2; the third instance arrives when a future schema-v2 directional-PASS surfaces the same reading-divergence pattern.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY` (§W1c-69) | **PASS** (schema-v2 sign=PASS, magnitude=PASS, regime=VALID) | δ[Z/H] = +0.5768 dex at n_PBH = 1e-22 m⁻³; \|0.5768 − 0.4\| = 0.177 < 0.3; PASS-magnitude window n_PBH = 5.45e-23 m⁻³; audit_sha256=`2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` |

The verdict line is permanent (`gate-verdicts.md §"Verdicts are permanent"`); this synthesis adjudicates the *reading* of the verdict, not its existence. No re-emission is permitted under v3-closure-recovery; the structural verdict below propagates to the falsifier-master-inventory annotation and the CF-W1c-2 carry-forward framing.

---

## IV. Structural Implications

### IV.1 Structural verdict (Workshop 1 outputs i-v)

**(i) Algebra-axis classification**: δ[Z/H] sign-prediction = **algebra-INVARIANT-with-DISCRIMINATING-CONTENT**. Substitution-chain demonstration: of the five factors entering δ[Z/H], at least one (F-H5 = +0.0127 from S87 J8) carries a substrate-IS sign whose negative counterfactual (CV-1) is structurally excluded by J8 closure rather than by algebraic convention.

**(ii) Discriminating-counterfactual specification**:
- CV-1: F-H5 NEGATIVE (Klein-V_4 destructive modulation) → δ[Z/H] < 0 → sign-FAIL. *Excluded* by J8 PROVEN +sign closure at S87.
- CV-2: oscillatory cascade with `dn_PBH/dg < 0` integrated → δ[Z/H] < 0 → sign-FAIL. *Excluded* by CF-CURV-6 monotone-pile-up structure.
- CV-3: cascade-tail mass M = 10¹⁵ kg (T_H below bottleneck) → δ[Z/H] vacuous (≥ 0 but undetectable). *Excluded* by CF-CURV-7 mass anchor; tangential to sign question.

**(iii) GO/NO-GO on team-lead "2-OOM narrowing" framing for CF-W1c-2**: **NO-GO as a CF-CURV-6 tightening; downgraded to a tension diagnostic**. Substitution-chain reasoning: the PASS-magnitude window 5.45e-23 m⁻³ sits 2.26 OOM below the upper edge of the CF-CURV-6 prior (10⁻²⁰ m⁻³) and 2.74 OOM above the prior mid-band (10⁻²⁵ m⁻³); the posterior support [8.4e-24, 2.2e-22] is a 1.4-OOM-wide neighborhood pushed against the upper 22.6% of the prior. This is structurally a band-edge constraint, not a narrowing of the central value. CF-W1c-2 should reframe as: "n_PBH band [10⁻³⁰, 10⁻²⁰] is constrained by Maiolino+24/Bunker+23 to require n_PBH in the upper 1.4 OOM (≈ [8.4e-24, 2.2e-22]); the substrate's CF-CURV-6 mid-band reading at 10⁻²⁵ FAILS magnitude by 2.5 OOM; the sign matches at all viable n_PBH but the magnitude requires upper-band n_PBH within 1 OOM of the CF-CURV-6 upper edge."

**(iv) Revised schema-v2 3-tuple for §W1c-69 (registry annotation, NOT verdict-line edit)**: the canonical verdict line at `s88_gate_verdicts.txt:34-36` remains unchanged (verdict permanence; absolute on disk). The `falsifier-master-inventory.md` row for §W1c-69 (CF-W1c-1 mack-cosmic-bridge sole-writer landing) MUST carry the following annotation in its ANCHOR / SUBSTRATE-IS / LABORATORY-IN structure:

```
§W1c-69 (S88-CF-CURV-16) — composite=PASS via schema-v2 (sign=PASS, mag=PASS, regime=VALID)
  Sign-PASS reading: algebra-INVARIANT-with-DISCRIMINATING-CONTENT
    Substrate-IS factors: F-H5 sign (J8 PROVEN +0.0127); cascade-tail T_H
      above bottleneck (CF-CURV-7); cascade-tail population monotone-pile-up
      (CF-CURV-6 W1a-59); thermal-Hawking positive flux.
    Counterfactuals excluded: CV-1 (F-H5 negative) by J8; CV-2 (oscillatory
      cascade) by CF-CURV-6 structure; CV-3 (below-bottleneck mass) by CF-CURV-7.
    Discriminating against external alternatives (AGN feedback, IMF, Pop-III):
      NO at the sign axis (all predict +); the substrate-IS reading is
      discriminating against *substrate-internal* counterfactuals only.
  Magnitude-PASS reading: BAND-EDGE PASS at upper 22.6% of CF-CURV-6 prior
    PASS-magnitude window n_PBH = [8.4e-24, 2.2e-22] m⁻³ (≈ 1.4 OOM wide)
    CF-CURV-6 prior mid-band 10⁻²⁵ m⁻³ FAILS magnitude by 2.52 OOM
    Reading: posterior pushed against prior upper edge; substrate prediction
      requires upper-band n_PBH within 1 OOM of CF-CURV-6 upper boundary.
```

The `STAGE-1-CANDIDATE` recast of the §W1c-69 directional-prediction registry entry is **NOT REQUIRED** at S89 (the existing S87 schema-v2 annotation is already at the correct `(sign=PASS, mag=PASS, regime=VALID)` tuple); the ANNOTATION-ONLY revision in `falsifier-master-inventory` carries the discriminating-content + band-edge clauses without disturbing the verdict line.

**(v) Calibration-corpus extension**: §W1c-69 sign-PASS-with-discriminating-content is calibration instance **K=2** for the algebra-INVARIANT-with-DISCRIMINATING-CONTENT vs INVARIANT-vacuous sub-class distinction (instance K=1 = S88 W13 W-1 profile-invariance at 6.68e-17). Per `agent-standards.md §"HIGH-DENSITY WORKSHOP TEMPLATE"` + `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold, the sub-class hardens to MANDATORY when a third instance lands. The S89+ algebra-axis K-counter calibration corpus retains §W1c-69 as the canonical *cosmological-falsifier* instance (W13 W-1 is the *spectral-functional* instance; the third instance, when it lands, will likely be a *transit-dynamics* or *gravitational-wave* instance to complete the algebra-axis cross-pillar coverage).

### IV.2 Implications for `falsifier-master-inventory` (CF-W1c-1 sequencing)

CF-W1c-1 (mack-cosmic-bridge sole-writer mechanical landing of W1c falsifier rows from sidecar JSONs) SHOULD wait for this synthesis (Workshop 1) AND Workshop 2 (Page-1976 13-OOM L_H form pinning, separate dispatch) to close before landing. The §W1c-69 row content depends on:

- This synthesis (Workshop 1 output iv): annotation specifying sign-PASS reading is INVARIANT-with-DISCRIMINATING-CONTENT (vs INVARIANT-vacuous)
- Workshop 2 output (separate): annotation specifying L_H pin convention and Class-(c) PIN-DRIFT audit verdict

Landing CF-W1c-1 BEFORE Workshop 2 closure risks pinning a 13-OOM-convention-band-uncaveated row that MAY require revision; landing AFTER Workshop 2 absorbs the L_H form decision into a single landing pass. Recommend S89 W0 sequencing: Workshop 2 dispatch FIRST, then CF-W1c-1 mack-landing absorbs both Workshop 1 and Workshop 2 outputs.

### IV.3 Implications for CF-W1c-2 (n_PBH band narrowing feedback to W1a-59 CF-CURV-6)

The CF-W1c-2 4-field spec at WP §9 reads "Apply §W1c-69 PASS-magnitude n_PBH window 5.45×10⁻²³ m⁻³ as observational constraint on W1a-59 CF-CURV-6 PASS band [10⁻³⁰, 10⁻²⁰] m⁻³". Under this synthesis's Workshop 1 verdict (iii NO-GO on "2-OOM narrowing"), CF-W1c-2 reframes as:

**CF-W1c-2 (revised)**: "Apply §W1c-69 PASS-magnitude posterior support [8.4×10⁻²⁴, 2.2×10⁻²²] m⁻³ as observational constraint on W1a-59 CF-CURV-6 PASS band; this is a BAND-EDGE CONSTRAINT (posterior pushed against upper 22.6% of prior), NOT a substrate-side narrowing of the prior central value. Check cross-tension with CF-CURV-7 cascade-tail mass anchor: does the substrate-cascade-pile-up factor admit n_PBH in the [8.4e-24, 2.2e-22] window, or does it predict a substantially different central n_PBH? If the substrate's structural prediction is closer to the CF-CURV-6 mid-band 10⁻²⁵ m⁻³ than to the upper 22.6% of the prior, then §W1c-69 surfaces a substrate-vs-observation TENSION DIAGNOSTIC at the magnitude axis (sign matches; magnitude requires upper-edge n_PBH which the substrate may not preferentially predict). If the substrate's structural prediction natively favors n_PBH near the upper edge, then §W1c-69 IS a genuine narrowing." This reframing converts CF-W1c-2 from a putative narrowing computation into a **substrate-vs-observation reconciliation gate**.

### IV.4 Cross-link to Workshop 2 (L_H form pinning)

The 13-OOM Page 1976 L_H form pinning workshop (separate dispatch) directly affects this synthesis's quantitative anchors. If Workshop 2 closes with Eq. 1 (3.56e6 W) as canonical instead of Table-1 (3.5e19 W), the δ[Z/H] predictions at all three n_PBH grid points scale by 10⁻¹³, and the PASS-magnitude window for n_PBH shifts by ~13 OOM upward — far beyond the CF-CURV-6 prior upper edge (10⁻²⁰), causing magnitude-FAIL at every prior-supported n_PBH and structurally falsifying the cascade-tail-Hawking-injection chain at the 13-OOM level. If Workshop 2 closes with Table-1 as canonical (the plan-pinned form), this synthesis's quantitative anchors remain valid. If Workshop 2 surfaces a NEW substrate-derived form from cascade-tail D_K eigenvalue spectrum, the entire chain is re-evaluated.

The Workshop 1 sign-prediction structural verdict is **invariant under Workshop 2's L_H choice**: the sign of δ[Z/H] is non-negative regardless of L_H magnitude (because L_H ≥ 0 by Hawking-flux structure, and the other factors retain their substrate-IS signs). The MAGNITUDE PASS/FAIL status, however, is highly L_H-sensitive.

---

## V. Carry-Forward Computations

### V.1. Algebra-axis K=3 promotion calibration instance #3 dispatch

- **What**: Identify a third instance of algebra-INVARIANT-with-DISCRIMINATING-CONTENT vs INVARIANT-vacuous reading-divergence in S87/S88 schema-v2 directional-PASS verdicts, and produce its substitution-chain factor analysis to advance the K-counter from K=2 to K=3 (MANDATORY promotion of the sub-class). Candidate third instances surveyed from agent memory: (a) S82 W3-4 f_NL^GGE = 0.0547 sign-PASS vs Planck (transit-dynamics axis); (b) S65 NT-BLUE n_T(transit) = +0.4676 sign-PASS at LiteBIRD detector horizon (gravitational-wave axis).
- **Inputs**: `sessions/permanent-results-registry.md §VII.M.scorecard.{corroborations}`; `s82_gate_verdicts.txt` lines for f_NL^GGE; `s65_gate_verdicts.txt` lines for NT-BLUE; this synthesis as instance #2; W13 W-1 working paper synthesis as instance #1.
- **Gate**: `S89-ALGEBRA-AXIS-INVARIANT-DISCRIMINATING-CONTENT-K3-PROMOTION` PASS iff three instances exhibit (a) substrate-IS factor with sign-content that admits a counterfactual substrate variant producing sign-FAIL, AND (b) the counterfactual is structurally excluded by an upstream PROVEN identity (J8, NT-BLUE, or analogous). PASS triggers MANDATORY promotion of the INVARIANT-with-DISCRIMINATING-CONTENT sub-class; INFO if 2/3 instances demonstrate the pattern; FAIL if any instance reduces to algebra-only non-negativity without substrate counterfactual.
- **Effort**: 1 agent-session (3-5 hours); spectral-geometer or mack-cosmic-bridge solo synthesis with §VII.M.scorecard cross-reference.

### V.2. CF-W1c-2 reframing dispatch (substrate-vs-observation reconciliation)

- **What**: Re-derive CF-CURV-6 n_PBH(g_BBN) STRUCTURAL CENTRAL prediction (substrate's natural n_PBH at cascade-tail generation g ≈ 322) and compare against the observational PASS-magnitude posterior support [8.4×10⁻²⁴, 2.2×10⁻²²] m⁻³ from §W1c-69. Determine whether the substrate's structural CENTRAL prediction falls inside, at the edge of, or outside the observational posterior support window.
- **Inputs**: W1a-59 CF-CURV-6 npz output (`s88_w1a_cf_curv_6_n_pbh_per_cascade_generation.npz`); substrate structural derivation chain for n_PBH(g) from CC_OOM = 115.5 + cascade-tail-pile-up factor + Volovik-partition cascade-depth = 384 generations; S87 J8 PROVEN F-H5 anchor; canonical_constants.py CC_OOM pin.
- **Gate**: `S89-CF-CURV-6-STRUCTURAL-CENTRAL-VS-W1C69-POSTERIOR-RECONCILIATION` PASS iff substrate's structural central n_PBH falls within [8.4×10⁻²⁴, 2.2×10⁻²²] m⁻³ (substrate-vs-observation reconciled at 1.4-OOM band); INFO if substrate central is within 1 OOM of posterior support edge (consistency at edge); FAIL if substrate central is more than 1 OOM outside posterior support (structural tension surfaced — substrate predicts mid-band n_PBH which observation excludes by 2.5+ OOM, requiring CF-CURV-6 derivation revision OR re-evaluation of the cascade-tail-Hawking injection chain).
- **Effort**: 1 agent-session (2-4 hours); volovik-superfluid-universe or transit-dynamics solo synthesis with cascade-pile-up structural derivation.

### V.3. `falsifier-master-inventory.md` CF-W1c-1 mack-landing with Workshop-1 + Workshop-2 annotations absorbed

- **What**: Land 4 W1c falsifier rows (W1c-66, W1c-67, W1c-68, W1c-69) from sidecar JSONs into `sessions/framework/registry/falsifier-master-inventory.md` per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole-writer convention. The W1c-69 row MUST absorb (a) this synthesis's annotation per IV.1 output (iv) (sign-PASS reading: INVARIANT-with-DISCRIMINATING-CONTENT; magnitude-PASS reading: BAND-EDGE PASS at upper 22.6% of CF-CURV-6 prior) AND (b) Workshop 2's L_H form-pinning verdict (Table-1 plan-pinned canonical OR Eq. 1 conservative-floor OR new substrate-derived form).
- **Inputs**: W1c sidecar JSONs (4 files, all in `computations/`); this synthesis (Workshop 1 output); Workshop 2 synthesis (separate dispatch, must close BEFORE this gate); `falsifier-master-inventory.md` current state at S88 close; cross-link table to `mack-observational-constraints.md`, `branch-iv-canonical.md`, `pre-registered-observations.md`.
- **Gate**: `S89-CF-W1C-1-FALSIFIER-INVENTORY-LANDING` PASS iff 4 rows landed with full IS-not-IN anatomy (substrate-IS observable, laboratory-IN observable, bridge map, algebraic envelope, empirical anchor) per `cross-pillar-bridge-anatomy.md` MANDATORY-K=3, AND W1c-69 row carries the dual annotation (sign-PASS reading + magnitude-PASS reading + Workshop-2 L_H pin); FAIL if any row missing IS-not-IN element or W1c-69 missing dual annotation.
- **Effort**: 1 agent-session (4-6 hours); mack-cosmic-bridge sole-writer dispatch; sequencing: AFTER Workshop 2 closure.

### V.4. Sign-PASS reading audit-script extension to `_falsifier_inventory_audit.py` (forward-looking)

- **What**: Extend the falsifier-inventory audit script to detect schema-v2 directional-PASS rows and verify their accompanying registry annotation classifies the sign-PASS reading as INVARIANT-vacuous OR INVARIANT-with-DISCRIMINATING-CONTENT OR DEPENDENT (per the algebra-axis taxonomy). Audit FAILs if a sign-PASS row lacks the annotation; INFO if annotation is present but sub-class is incomplete.
- **Inputs**: `falsifier-master-inventory.md` current state; algebra-axis taxonomy from `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`; existing audit script template `computations/_shared/_cross_pillar_bridge_audit.py`.
- **Gate**: `S89-OR-LATER-FALSIFIER-INVENTORY-SIGN-CLASSIFICATION-AUDIT` PASS iff audit script implements the regex pattern + sub-class detection + annotation check; INFO if implemented but algebra-axis taxonomy not yet consolidated; FAIL if implementation diverges from algebra-axis MANDATORY-K=3 rule-file specification.
- **Effort**: 1 agent-session (3-5 hours); methodology-class wave (per `wave-classification.md` M1∧M2∧M3∧M4 with W9-allowlist append); volovik-superfluid-universe or kitaev-information-scrambling co-author.

### V.5. Calibration-corpus tracking ledger for INVARIANT-vacuous vs INVARIANT-with-DISCRIMINATING-CONTENT sub-class

- **What**: Establish a tracking ledger at `sessions/framework/registry/algebra-axis-discriminating-content-corpus.md` listing K instances of the INVARIANT-with-DISCRIMINATING-CONTENT sub-class with per-instance substitution-chain factor analysis + counterfactual specification + structural exclusion citation. Land instance #1 (W13 W-1 profile-invariance at 6.68e-17) and instance #2 (W1c-69 sign-PASS-with-discriminating-content from this synthesis); leave instance #3 slot for the V.1 promotion gate's outcome.
- **Inputs**: this synthesis (instance #2); W13 W-1 working-paper synthesis (instance #1, requires read-through to extract per-factor analysis); algebra-axis taxonomy from `cross-pillar-bridge-anatomy.md`; `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold.
- **Gate**: `S89-OR-LATER-ALGEBRA-AXIS-CORPUS-LEDGER-LANDING` PASS iff ledger landed with K=2 entries + structural template for instance #3; INFO if K=2 entries land but template incomplete; FAIL if instance #1 (W13 W-1) cannot be re-derived in the same factor-analysis form (would indicate that the calibration-corpus extension claim is structurally weaker than this synthesis assumes).
- **Effort**: 1 agent-session (3-5 hours); mack-cosmic-bridge or methodology-class synthesizer; AMRI-discipline check (the ledger is project-level, NOT agent-memory).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Sign-prediction is algebra-INVARIANT-with-DISCRIMINATING-CONTENT (NOT vacuous, NOT DEPENDENT) | PARTICLE / GEOMETRIC | STRUCTURAL VERDICT | sagan-tautology reading partially correct against external alternatives, structurally incorrect against internal substrate counterfactuals (CV-1 F-H5 NEGATIVE excluded by J8) |
| 2 | Counterfactual substrate variants producing sign-FAIL specified (CV-1 F-H5 negative; CV-2 oscillatory cascade; CV-3 below-bottleneck mass) | GEOMETRIC | STRUCTURAL VERDICT | Each counterfactual structurally excluded by an upstream PROVEN identity (J8, CF-CURV-6 monotone-pile-up, CF-CURV-7 mass anchor) |
| 3 | "2-OOM narrowing" framing for CF-W1c-2 receives **NO-GO** as CF-CURV-6 tightening; downgraded to band-edge tension diagnostic | NON-PHONONIC | STRUCTURAL VERDICT | Posterior support [8.4e-24, 2.2e-22] m⁻³ is 2.26 OOM below CF-CURV-6 upper edge; mid-band fails magnitude by 2.52 OOM; CF-W1c-2 reframes as substrate-vs-observation reconciliation gate |
| 4 | Schema-v2 3-tuple (sign=PASS, mag=PASS, regime=VALID) **NOT reclassified**; canonical verdict line permanent; registry annotation in `falsifier-master-inventory` carries dual-clause reading | NON-PHONONIC | REGISTRY ANNOTATION ONLY | sign=PASS-with-DISCRIMINATING-CONTENT; magnitude=PASS at upper-band 22.6% of CF-CURV-6 prior |
| 5 | Calibration-corpus extension to W13 W-1 profile-invariance pattern: K=2 instances of INVARIANT-with-DISCRIMINATING-CONTENT vs INVARIANT-vacuous sub-class | NON-PHONONIC | K=2 toward MANDATORY at K=3 | V.1 promotion gate identifies third instance from S82 f_NL^GGE or S65 NT-BLUE candidates |
| 6 | CF-W1c-1 mack-landing must absorb both this synthesis (Workshop 1) AND Workshop 2 (L_H form pinning) outputs | NON-PHONONIC | SEQUENCING DIRECTIVE | S89 W0 ordering: Workshop 2 dispatch first; then CF-W1c-1 mack-landing absorbs both outputs |
| 7 | L_H form pinning (Workshop 2 separate dispatch) does NOT affect sign-prediction structural verdict; affects MAGNITUDE 13-OOM | PARTICLE | CROSS-WORKSHOP CROSS-LINK | Sign verdict invariant under Workshop 2; magnitude verdict highly L_H-sensitive (13-OOM PASS/FAIL pivot) |

---

**Substrate framing**: The cascade-tail Hawking spectrum + F-H5 = +0.0127 substrate-IS modulation IS the substrate's own structural identity at the BBN epoch — emerging from the rank-2 Klein-V_4 cascade structure projected onto the deuterium-bottleneck threshold. The observational [Z/H] excess at z=6-8 LRD-progenitor environments (Maiolino+24 +0.3 to +0.5 dex, Bunker+23 +0.4 ± 0.2 dex) is the laboratory-IN measurement of the substrate's BBN-epoch metallicity-injection footprint per `phononic-framing.md §"IS Space, Not IN Space"` direction-of-explanation. The direction of inference flows: **substrate cascade structure (rank-2 Klein-V_4 at τ_fold) IS the J8 spectral identity → cascade-tail Hawking spectrum at BBN epoch → non-thermal MeV injection into Wagoner network → emergent +δ[Z/H] at LRD-progenitor environments → JWST-observed absorption-line metallicity excess**. Inverting (treating the observed [Z/H] excess as fundamental and the cascade as a derived consequence) is a container-thinking violation. The sign-PASS reading is substrate-IS evidence at the algebra-INVARIANT-with-DISCRIMINATING-CONTENT layer; the magnitude-PASS reading is band-edge consistency at the upper 22.6% of the CF-CURV-6 prior, requiring substrate-vs-observation reconciliation at S89.
