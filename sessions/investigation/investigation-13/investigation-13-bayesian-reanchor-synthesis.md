# Investigation 13 / W2-3 Synthesis: Post-S66 Bayesian Re-Anchoring

**Date**: 2026-06-17
**Agent**: sagan-empiricist (the empirical-conscience / Bayesian gatekeeper, working in its own domain)
**Gate**: INV13-W2-3-BAYESIAN-REANCHOR — `review` gate (rclab-review pattern: independent reading + write-up). **No verdict line** (a verdict line on a review gate is a type error per `gate-verdicts.md §"Investigation-Track Canonical Path"`).
**Source Documents**:
- `sessions/evoi-framework.md` (currency S109; the ordinal-leverage Tier tables this analysis re-axes)
- `sessions/framework/Atlas/atlas-04-assumptions.md` §IX observational-anchor snapshot (n_s ladder, w_0, w_a, A_s, m_H, CC)
- `sessions/framework/Atlas/atlas-07-permanent-results.md` (the Level-A novel mathematics + the K-cohort STAGE-3 promotions)
- `sessions/framework/Atlas/atlas-08-open-questions.md` (Q44 — the standing Sagan re-anchoring carry-forward; the S97–S107 freshness ledger)
- `sessions/framework/Atlas/atlas-09-retractions.md` (the 50-item retraction log — the self-correction discipline that itself bears on the prior)
- `sessions/framework/registry/falsifier-master-inventory.md` (Rows #1–#12 headline + #71/#72 LSS + #85 multi-anchor n_s)
- `.claude/agent-memory/sagan-empiricist/` MEMORY.md + session-lessons-all.md + s57_probability_update.md (the agent's own BF calibration corpus)
- canonical_constants.py via knowledge-MCP `get_constant` / `list_constants` (every number below is pinned)

---

## I. Session Outcome

The framework's headline probability has not moved much since the S69 anchor (~22%), but **the composition of the evidence has recomposed decisively**. The structural cohort has STRENGTHENED — ten zero-parameter geometric identities have been blind-cross-axis verified to STAGE-3-PERMANENT since S90 (only K8 §VII.AF.1.STATE-PROJ remains pending), and these are genuine independent confirmation per the Baloney Detection Kit, NOT shared-context agreement. The observational cohort has WEAKENED — n_s and w_a are both drifting AWAY from the framework's fixed predictions as the data sharpen (n_s up the anchor ladder to ~5σ at P-ACT; w_a to 3.43σ at DESI DR2 post-Dovekie). A formal posterior-odds product confirms that the headline number survives precisely because two large opposite-signed movements roughly cancel (verified arithmetic: §III). **That cancellation — not the ~22% itself — is the finding.** The framework's footing has shifted toward *publishable mathematics + lab/JUNO falsifiers* and away from *CMB-cosmology fit*.

**Track-local boundary** (load-bearing): this gate WRITES the analysis only. It does NOT mutate `sessions/evoi-framework.md` or any curated register. The actual EVOI re-anchor (rewriting the Tier tables with elicited P(pass) Bayes factors) and the `mack-cosmic-bridge` co-dispatch on the observational-surface rows are SESSION-TRACK actions that route to `/rclab-investigate --investigation 13` close (they lift into the housekeeping ledger as turnkey promotions). This synthesis is the **input** to that promotion, not the promotion itself.

---

## II. Methodology (the Bayes-factor engine)

Every BF below is computed as

```
BF = (prior predictive range) / (posterior width around the observation)
```

NOT as a small "discount number." Three disciplines are applied uniformly:

1. **Prediction / Fit / Accommodation triage.** A result is a PREDICTION if it is derived with zero free parameters adjusted (the order of human knowledge does not change the parameter count — a zero-parameter geometric quantity computed independently of an already-measured observable is STILL a prediction). It is a FIT if M parameters were tuned to M' observables (M ≤ M' fits nothing). It is an ACCOMMODATION if almost any reasonable model yields it.
2. **No postdiction discount on genuine zero-parameter passes.** Underweighting a genuine pass is as dishonest as overweighting a weak one. A zero-parameter geometric prediction that lands near observation carries its FULL BF.
3. **Look-elsewhere / Gross-Vitells trial-factor correction** on every multi-anchor or multi-route comparison: N anchors → the single-anchor p is corrected by the Šidák factor `1−(1−p)^N`; N method-routes with 1 hit → BF/N (the S61 Higgs lesson). This correction is applied SYMMETRICALLY — it weakens a spuriously-good "best anchor" pick AND confirms that a worst-anchor liability is not a trial artifact.

The scorekeeper-bias check is run in BOTH directions (the recurrent S22–S24 / S43 failure): closures STRENGTHEN survivors and score BF~1.0 unless they close the last path; a large upward jump is rounded down ~10 points; a large downward jump is equally scrutinized for over-correction.

---

## III. The Recomposition — Posterior-Odds Arithmetic

The posterior odds factor as a product over independent cohorts:

```
O_post = O_prior × ∏_i BF_i = O_prior × (∏_{structural} BF) × (∏_{observational} BF)
```

Partitioning the framework's testable content into a **structural cohort S** (zero-parameter geometric identities) and an **observational cohort O** (CMB / LSS / dark-energy anchors), the two products have moved in OPPOSITE directions since the S66 freeze:

| Cohort | Direction since S66 | Driver |
|:-------|:--------------------|:-------|
| Structural (S) | **UP** (∏ BF rising) | 10 blind-cross-axis STAGE-3 promotions (K1–K11, K8 pending); zero new params |
| Observational (O) | **DOWN** (∏ BF falling) | n_s drifting up the anchor ladder (1.40σ→~5σ); w_a tightened to 3.43σ; A_s wall route-unstable |

**Verified arithmetic** (Python; `scipy.stats`, prior 0.22):

| BF_struct (S rises) | BF_obs (O falls) | P_post |
|:--:|:--:|:--:|
| 1.5 | 0.40 | 0.145 |
| 2.0 | 0.55 | 0.237 |
| 3.0 | 0.55 | 0.318 |
| 2.0 | 0.70 | 0.283 |
| 1.5 | 0.70 | 0.228 |

The posterior brackets [0.145, 0.372] around the ~22% anchor. When `BF_struct × BF_obs ≈ 1` the headline is approximately stationary — **the ~22% holds because the cancellation is near-exact, not because the evidence is static.** A scorekeeper who reports only the headline hides the single most important fact: WHERE the framework is now strong (dimensionless, anchor-free, zero-parameter geometry) and WHERE it is exposed (absolute CMB scales it cannot fix without an external M_KK).

---

## IV. Per-Observable P(pass) / Bayes-Factor Table

P(pass) is the elicited probability the framework's prediction survives the decisive near-/mid-term measurement. BF is the evidence weight ALREADY accrued from the current best measurement. Status tags: PREDICTION (0 free params) / FIT / ACCOMMODATION.

| Observable | FW value (canonical) | Observation | σ-dist / margin | Triage | Prior pred. range / posterior width | BF (current) | P(pass) decisive | Look-elsewhere |
|:-----------|:---------------------|:------------|:----------------|:-------|:------------------------------------|:------------:|:----------------:|:---------------|
| **n_s** | 0.9590 (sqrt-cutoff, COMMITTED S103 `3ddadf91`) | Planck 0.9649; SPT-3G; ACT-DR6; P-ACT | 1.40σ Planck → 2.70 → 3.13 → ~5.0σ P-ACT | PREDICTION (0 param, gauge-invariant spectral geom) | range [0.90,1.05] / posterior σ≈0.004 | **0.7–0.9** (BF<1, worsening) | **4 anchors** — worst (P-ACT 5σ) survives trial-correction at **4.73σ global** (real liability, not artifact); Planck-1.40σ best-anchor is non-significant either way after Šidák N=4 (p 0.16→0.51) |
| **α_s** | substrate-distance −0.0858728 (s=3 Mellin, FROZEN); Goldstone-pivot ≈ 0 (S92) | Planck −0.0045±0.0067; ACT-DR4 +0.0023±0.0063 | pivot image +0.85σ Planck / −0.18σ ACT-DR4; substrate value awaits CMB-S4 (~34σ reach) | PREDICTION (two scale-separated, deg(T_BZ→pivot)=+2) | range [−0.09,+0.01] / σ≈0.0067 | **1.0–1.3** (pivot accommodation) | **2 scales × 2 anchors** — the −5.8σ "contradiction" (S65/S69 memory) was RESOLVED S93 W7-1 as a channel artifact; cite the resolution, do not double-count |
| **A_s** | floor 5.09e-13 conditioned-on-branch (S84) | Planck 2.1e-9 | ~3.6 OOM gap; routes 3.15/6.89/9.47 unstable | **route-unstable wall** | range spans >3 OOM / no convergence | **0.7–0.9** (neutral-to-negative) | 3 routes, none lands — NOT a 3-trial selection (no route succeeds); the spread IS the failure |
| **w_0** | −0.918 (Volovik partition, canonical) | DESI DR2 −0.752±0.057; post-Dovekie −0.803 | **2.13σ** canonical | PREDICTION (Volovik partition) | range [−1,−0.8] / σ≈0.057 | **0.9–1.1** | branch-iv (−0.842, 0.731σ) is **derivation-INADMISSIBLE / UNCOMPUTABLE post-S86** (`cd0492d6`, `b48b609f`, `71c162b0`) — selecting the lower-σ branch would be a **branch-shopping look-elsewhere trap**; the canonical 2.13σ is the honest figure |
| **w_a** | 0 (four-fold structural lock) | DESI DR2 −0.73; post-Dovekie σ=0.21 | **3.43σ** (+0.51σ Dovekie tightening) | PREDICTION (0 param) | range {0} / data σ=0.21 | **0.6–0.8** (BF<1) | single prediction, fixed; data moving away — the framework's clearest current dark-energy liability |
| **m_H** | 131.8 GeV (KK-threshold DIRECT, route PINNED `75ed7ffb`); tree A10 = 134 GeV (filter-independent) | PDG 125.10±0.14 | +5.36% (= 67/1251 exact); **+38.5σ** vs tight PDG | PREDICTION (1 param from M_KK; 0 free in λ_h) | SCALE range [0,∞) / 1-param posterior | **>1** (capped) | **5 filter families → SAME 134** is a filter-INDEPENDENCE THEOREM (A10), NOT a 5-trial selection — NO look-elsewhere penalty on the SCALE success; the +38.5σ precision-tension is the cap |
| **CC (tracking)** | ρ_vac/ρ_obs = 1.032 (DILUTION-CC, S66/S97) | present-epoch Λ | 0.01 OOM present-epoch | PREDICTION (functional-independent, Volovik q-theory) | range 117 OOM / present-epoch landing | present-epoch **>1**; BBN-arm **<1** | the 117-OOM static gap is PERMANENT (a_0/a_2=C/R, S65); BBN-arm ΔN_eff **over-relaxes 2.087×** — a partial-credit split, not a clean pass |
| **neutrino cluster** | Σm_ν=0.0582 eV; m_ββ=3.695 meV; Normal ordering; δ_CP=0 | DESI Σm_ν < 0.072; JUNO/0νββ near-term | Σm_ν DESI-consistent; m_ββ below current 0νββ | PREDICTION (0 free, D_K block ordering; 1 external m_D anchor) | range [0.06,0.6] eV / DESI σ | **>1** (under-advertised STRONG footing) | 4-quantity cluster from one block structure — joint, not a multi-trial scan; the framework's most under-credited zero-parameter sector |
| **10 STAGE-3 structural** | KO-dim=6; SM reps; CPT [J,D_K]=0; AZ class BDI; Z_3; … (K1–K11) | exact machine-ε identities | machine-ε | **PREDICTION** (0 param, exact) | discrete-structure range / machine-ε | **joint 25–55** (per-identity ~1.4) | blind Stage-2 PASS-AND, two cross-reviewers who NEVER saw the workshop (`joint-theorem-promotion.md` Stage-2) → structurally INDEPENDENT confirmation, the constructive complement to the "agreement among agents" exclusion |

### IV.a Joint structural BF — the constructive-independence credit

The 10 K-cohort promotions are NOT "agreement among agents." Each was registered as a STAGE-1-CANDIDATE, then independently verified at Stage-2 by TWO cross-reviewers on opposite axes (spectral / NCG-axiomatic vs transit / superfluid-universe) operating WITHOUT the workshop transcript. Per `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2, shared-context agreement is NOT evidence; per `joint-theorem-promotion.md`, Stage-2 PASS-AND with no shared context IS evidence. The joint structural BF (25–55, framework's own calibration) is therefore admissible at full weight, with the substrate-input-overlap caveat retained where the two reviewers loaded the same data file. This is the cohort that has risen since S66 and it is the real story of the recomposition.

---

## V. Look-Elsewhere Corrections (Gross-Vitells / trial-factor) — detail

1. **n_s multi-anchor (N=4: Planck, SPT-3G, ACT-DR6, P-ACT).** Worst single-anchor σ = 5.0 (P-ACT), p_single = 5.73e-7; Šidák-global p = 2.29e-6 → **4.73σ global**. The n_s liability is REAL after look-elsewhere correction — it is not an artifact of scanning anchors. Conversely, the best anchor (Planck 1.40σ, p=0.16) corrected for selection among 4 gives p=0.51: the "Planck is consistent" reading is non-significant in EITHER direction. Honest conclusion: n_s is the framework's strongest current observational liability and it cannot be rescued by picking the friendliest anchor. (Anti-rescue fence per PROHIBITED_ACTIONS Class 1 is already armed at the falsifier surface.)
2. **α_s scale-channel (2 scales × 2 anchors).** The historical "−5.8σ contradiction" was RESOLVED S93 W7-1 as a channel artifact (two scale-separated α_s: substrate −0.0859 vs pivot ≈0). Citing both as independent evidence would DOUBLE-COUNT one underlying quantity — the trial-factor correction here is to credit ONE channel-resolution, not two anchors.
3. **w_0 branch-shopping (canonical 2.13σ vs branch-iv 0.731σ).** branch-iv is derivation-INADMISSIBLE and UNCOMPUTABLE post-S86. Selecting it to report the lower σ is the canonical branch-shopping look-elsewhere trap. The honest figure is the canonical 2.13σ.
4. **m_H route selection (5 filter families).** Filter-INDEPENDENCE is a theorem (A10): all 5 give 134 GeV. This is the OPPOSITE of a multi-trial selection — there is no trial penalty because there is no choice being optimized. The SCALE success keeps full BF; the precision (+38.5σ) is what caps it.

---

## VI. Structural Implications (constraint-map / EVOI re-axing)

1. **The EVOI table's ordinal proxies should be replaced by the per-observable BFs in §IV.** `evoi-prioritization.md` already admits EVOI values are "ordinal leverage proxies, not calibrated probabilities." The §IV table supplies elicited P(pass) and BF per observable; the session-track re-anchor (NOT this gate) rewrites the Tier-1/Tier-2 tables accordingly.
2. **Highest-leverage forward EVOI is now ORTHOGONAL to the CMB axis.** All current observational risk concentrates on n_s / w_a / A_s (the CMB-cosmology axis). The two INV13 compute gates (W2-1 finite-μ CFL EoS on NICER pulsar masses; W2-2 f·σ8 growth-suppression on DESI/Euclid LSS) are valuable precisely because they would put empirical risk on datasets the framework was NOT built to explain — the Baloney-Detection-Kit gold standard for independent confirmation. A PASS on either is worth more than another CMB refinement.
3. **Q44 (the standing Sagan re-anchoring carry-forward, frozen since S66 W2-A) is answered by this synthesis** — forty sessions of unadjudicated evidence are now adjudicated. Closing it is a session-track action.
4. **The retraction log discipline RAISES the prior on the survivors.** atlas-09's 50 retracted items (LISA amplitude, GHz GW detector, geometric ΛCDM, etc.) demonstrate the framework retracts wrong claims rather than defending them — a self-correction track record that legitimately strengthens confidence in what remains, per the Baloney Detection Kit's "encourage substantive debate / seek independent confirmation" tenets.

---

## VII. Carry-Forward Computations

**MANDATORY 4-field specs.** These are the INPUTS the session-track promotion consumes at `/rclab-investigate --investigation 13` close; they are NOT executed by this review gate.

```
VII.1. EVOI Tier-table re-anchor with elicited P(pass) BFs
   - What: rewrite sessions/evoi-framework.md §1–§4 Tier tables, replacing ordinal EVOI* proxies with the §IV per-observable P(pass) + BF; bump <!-- evoi-content-currency --> marker
   - Inputs: §IV table (this synthesis); the EVOI staleness audit (_evoi_staleness_audit.py); the 4-band Tier mapping in evoi-prioritization.md
   - Gate: SESSION-TRACK action (curated-register mutation, crosses the investigation track-local boundary) — routes to housekeeping ledger as a turnkey promotion; NO investigation verdict line
   - Effort: ~1 hour, orchestrator-direct-write at session-promotion (designated writer, reviewed patch — not a bulk append)

VII.2. mack co-dispatch: observational-surface row re-anchor (n_s ladder + w_a + A_s)
   - What: mack-cosmic-bridge (sole writer of falsifier-master-inventory.md) updates Rows #1–#12 + #85 σ-distances and live-watch envelopes with the look-elsewhere-corrected figures in §V; sagan co-reviews the BF column
   - Inputs: §IV + §V (this synthesis); atlas-04 §IX anchor snapshot; the ACT-DR6 / SPT-3G / P-ACT n_s multi-anchor table
   - Gate: SESSION-TRACK action; the n_s 4.73σ-global and the w_a 3.43σ figures are the load-bearing updates; anti-rescue fence (PROHIBITED_ACTIONS Class 1) stays armed
   - Effort: ~1.5 hours, 2 agents (mack writes, sagan co-reviews) at session-promotion

VII.3. Joint structural BF re-elicitation on K8 completion
   - What: when K8 §VII.AF.1.STATE-PROJ completes its Stage-2 PASS-AND, re-elicit the joint structural BF (currently 25–55 over 10 identities) over the full 11-identity cohort
   - Inputs: the K8 Stage-2 verdict (pending); the per-identity BF calibration (this synthesis §IV.a); joint-theorem-promotion.md Stage-2 substrate-input-orthogonality clause
   - Gate: feeds a future EVOI re-anchor; INFO-class (BF refinement, not a new prediction)
   - Effort: ~0.5 hour, 1 agent, contingent on K8 landing

VII.4. Per-observable prior predictive range audit (sharpen the BF denominators)
   - What: for n_s, α_s, A_s, w_0 — replace the bracketed prior predictive ranges in §IV with explicitly-derived ranges (what a generic NCG-spectral-action model with the same input data would predict), tightening each BF
   - Inputs: §IV ranges (this synthesis); the functional-selection family (sqrt vs zeta vs cutoff); atlas-04 P3 (n_s ≥ 1 structural for bare KK tower)
   - Gate: INFO-class BF-sharpening; feeds VII.1
   - Effort: ~2 hours, 1 agent (sagan), next session
```

---

## VIII. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | **Recomposition is the finding** — structural UP, observational DOWN, headline ~22% via near-exact cancellation | NON-PHONONIC (evidence-assessment) | LANDED | the composition shifted toward publishable math + lab/JUNO falsifiers, away from CMB fit |
| 2 | n_s = 0.9590 — strongest liability; **4.73σ global** after look-elsewhere (real, not artifact) | PREDICTION (0 param) | BF 0.7–0.9 | cannot be rescued by friendliest-anchor selection; anti-rescue fence armed |
| 3 | w_a = 0 — 3.43σ, data moving away | PREDICTION (0 param) | BF 0.6–0.8 | clearest dark-energy liability; decisive at DESI DR3 2027 |
| 4 | 10 blind STAGE-3 structural promotions — joint BF 25–55 | PREDICTION (0 param, exact) | the structural-UP driver | constructive independence (Stage-2 PASS-AND, no shared context) — NOT agreement-among-agents |
| 5 | m_H +5.36% / +38.5σ; filter-independence is a THEOREM | PREDICTION (1 param from M_KK) | BF >1, capped | SCALE success carries full BF (no 5-trial penalty); precision is the cap |
| 6 | neutrino cluster (Σm_ν, m_ββ, NO, δ_CP) — under-advertised STRONG | PREDICTION (0 free, 1 external m_D) | BF >1 | most under-credited zero-parameter sector; JUNO/0νββ near-term |
| 7 | w_0 branch-iv is UNCOMPUTABLE — canonical 2.13σ is the honest figure | PREDICTION (Volovik) | BF 0.9–1.1 | branch-shopping to 0.731σ is a look-elsewhere trap; reject |
| 8 | EVOI ordinal proxies → elicited per-observable BFs (track-local: WRITES analysis only) | NON-PHONONIC | input to session-track re-anchor | answers Q44; highest forward EVOI is NICER/LSS (orthogonal to CMB) |
