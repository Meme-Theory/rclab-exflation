# investigation-13 — Distillation Digest

**Reviewer:** phonon-first-cosmologist (neutral; not an inv-13 author — seed survey was gen-physicist + sagan).  **Date:** 2026-06-20.
**Topic:** Cross-domain + empirical audit of the S108 plateau — the 6 distinctive survivors after most cross-domain bridges deduped to specialist batches: GGE cosmological-collider bispectrum, a₄ strong-field QNM/tidal correction, branch-(iv) w₀ DR3-readiness, finite-μ color-superconductivity EoS, S₈ growth-suppression, and the post-S66 Bayesian re-anchor.
**inv-1 convergences/bridges executed:** CV-5 (GGE richest under-exploited asset; bridge B-5 collider bispectrum), CV-9 (no compact-object sector — anchor-free dimensionless prediction; bridges B-8 / dense-matter), CV-3/CV-7-adjacent (S₈ growth, LSS-distinguishing observable B-10-adjacent), CV-10 (register-optimism-outruns-derivation — the Bayesian re-anchor formalizes the recomposition).
**Gate tally:** 6 gates — **1 PASS / 2 FAIL / 2 INFO** (5 compute verdict lines) **+ 1 LANDED review** (W2-3, artifact-existence, no verdict line). **0 workshops by design** (the one adversarial tension — the A_s route-reconciliation — was owned by concurrent inv-12; honest registered count, NOT a gap).

---

## The structural spine (read first)

Every one of the five compute gates carries `sign_verdict=PASS` on its substitution chain. The substrate-physics DIRECTION is correct in all five; what falls short is MAGNITUDE (W2-1 EoS too soft; W1-2 73 OOM sub-detectable) or TRUNCATION-STABILITY on the L_max axis (W1-3). This is the inv-1 §0 one-sentence verdict instantiated on six independent axes: **solid where intensive/structural/sign-bearing, soft where dimensionful/dynamical/magnitude-bearing.** The single PASS (W2-2 S₈) is the one observable where the substrate's prediction is itself a dimensionless ratio landing in-band — exactly CV-9's "the first anchor-free prediction lives off the M_KK-limited CMB axis." The Bayesian re-anchor (W2-3) is the meta-statement of the same split: structural cohort UP, observational cohort DOWN, headline stationary by near-exact cancellation.

---

## 1. Per-gate ledger

| Gate | Verdict | Substrate reading (substrate-IS → bridge → lab-IN) | Framework claim touched (cite) | Verb | Magnitude |
|:-----|:--------|:---------------------------------------------------|:-------------------------------|:-----|:----------|
| **INV13-W1-1**-GGE-COLLIDER-SQUEEZED-FNL | INFO (ANALYTIC-LOCAL) | The post-transit GGE branch-multipliers λ_B1/B2/B3 ARE the substrate's heavy-field content; their dimensionless mass μ_a=λ_Ba/H_transit → cosmological-collider squeezed-limit feature in f_NL. On BOTH clock anchors μ_a lands far off the μ~O(1) collider window (deep-principal Boltzmann-killed under H̃_TD μ∈[247,1017]; deep-complementary Δ≈μ²/3<1e-4 under H_fold μ∈[2.5e-3,1.0e-2]). | GGE-BISPECTRUM-67 (HIGH; `f_NL_FW_S67_folded=0.129`, register). gen UB-2 "highest-leverage untraveled bridge" (inv-1 B-5 / CV-5). | **CHALLENGED** (corridor closed-as-NULL) | structural (Δ_fit=0; no μ~O(1) field on either clock) |
| **INV13-W1-2**-A4-HIGHER-CURVATURE-QNM-TIDAL | INFO (sign=PASS, mag=INFO, regime=VALID) | The a₄ Seeley-DeWitt moment IS the substrate's higher-curvature content (a₄^{ζ}/a₂^{ζ}=0.4865); heat-kernel/spectral-action bridge → emergent Weyl² (c_W=+5.556e-3>0) → definite + (blue-shift) QNM ringdown shift + definite + tidal-Love correction. | a₄/a₂=1000:1 hierarchy (atlas-04 S5); CV-9 empty compact-object sector (exterior leg, complementary to inv-11 W5-2 interior). | **BOLSTERED** (open gap → NAMED definite-sign mechanism + future-detector gate) | structural sign + ~73 OOM sub-detectable (m=1.324e-76 vs D_thr=1e-3) |
| **INV13-W1-3**-BRANCH-IV-W0-L1516-DR3 | FAIL (truncation-divergent) | w₀ IS the Zubarev branch-(iv) Mellin-zeta moment ρ_B of D_K's spectrum at τ_fold (Level-1 single-τ substrate-IS); CAC-anchored late-time w₀ → DESI DR3 w₀–w_a. Deep-truncation spread DIVERGES: 0.0443091 ({12,13,14}, S105) → 0.0629703 ({12..16}); L=15 grew spread +0.018456. | EVOI Q37 (DESI DR3 / branch-iv); register state `S105-BRANCH-IV-DIRECT-L1314 INFO, FB-envelope-bounded` (atlas-08-freshness-S105). w0_FW=−0.918. | **CHALLENGED** (optimistic Track_A falsified; corridor closed) | structural-numerical (spread 0.0630 > 0.05 FAIL ceiling; FB tail does NOT close) |
| **INV13-W2-1**-FINITE-MU-CFL-EOS | FAIL (sign=PASS, mag=FAIL, regime=VALID) | The diquark gap Δ_CFL(μ) IS the substrate BdG order parameter (same U(1)_7-breaking condensate as the cosmological fold, read at μ≠0); van Suijlekom D_μ=D+μQ → EoS pressure (spectral moment) → TOV M_max. dΔ_CFL/dμ>0 at all 25 scan points (VanHove-frac=1.000), but M_max=0.1631 M_⊙, Δ/μ=4.82 runaway. | CFL theorem + van Suijlekom BdG-SA (both PROVEN, register); CV-9 dense-matter NICER-orthogonal test; S38-CLOSED "no formalism" / S25-Goal-7 self-consistent-μ_eff. | **CHALLENGED** (corridor closed-at-this-construction; item RE-OPENED w/ named refinement) | structural sign + magnitude FAIL (~12× below 2 M_⊙ pulsar bound) |
| **INV13-W2-2**-FSIGMA8-GROWTH-S8 | **PASS** (sign=PASS, mag=PASS, regime=VALID) | Large-scale structure IS the interference pattern of post-transit GGE acoustic excitations through the a₂ growth channel; finite-coherence under-grows vs smooth ΛCDM → δ(f·σ8)<0 → S₈ below Planck. S8_FW=0.8128 in-band [0.76,0.83], 16/16 z-points negative, DESI-5yr-bindable. | `sigma8_growth_a2=0.79317` + `fsigma8_product_suppression_FW_max_pct=−4.058` (S96, register); CV-3/CV-7 S₈; inv-1 B-10-adjacent LSS-distinguishing observable. | **BOLSTERED** (static coincidence → quantitative z-dependent prediction; LIVE LSS flagship) | observational (S8 in-band, band-pos 0.75; DESI 1.001σ@z=0.5, Euclid 1.516σ 7 bins) |
| **INV13-W2-3**-BAYESIAN-REANCHOR | LANDED (review; no verdict line) | NON-PHONONIC empirical-conscience adjudication. Posterior odds factor over independent cohorts: structural ∏BF UP (10 blind STAGE-3 promotions), observational ∏BF DOWN (n_s 4.73σ global, w_a 3.43σ); headline ~22% holds by near-exact cancellation. | atlas-08 Q44 (standing Sagan re-anchor, frozen since S66 W2-A); CV-10 register-optimism-outruns-derivation; inv-1 §6 sagan recomposition. | **MUDDLED** (net-recomposition; components split on merits — see §3) | structural (the CANCELLATION is the finding, not the ~22%) |

---

## 2. Convergence read-back

Each attacked inv-1 convergence, with the inv-13 gate(s) that touched it and the resulting state.

- **CV-5 (GGE richest under-exploited asset; bridge B-5 collider bispectrum) → RELOCATED + bounded.** W1-1 ran the highest-leverage leg (collider squeezed-limit spectroscopy) and closed it as a clean NULL: the GGE branch content has no μ~O(1) heavy field addressable by the cosmological collider on EITHER physically-motivated clock. The GGE non-Gaussianity IS the folded-template amplitude `f_NL^folded=0.1293` and nothing more (register `GGE-BISPECTRUM-67`, reconfirmed from an independent direction: Gaussian-by-Wick, envelope-bounded `max|S|=0.1293 ≤ 1.505`). CV-5's *entanglement-spectrum / Page-curve* legs (B-5a/d) are UNTOUCHED by inv-13 and remain owned elsewhere (hawking, inv-4/inv-9). The collider-spectroscopy corridor specifically is now CLOSED; CV-5's broader "query the GGE" thesis survives only on its non-collider legs.

- **CV-9 (no compact-object sector — first anchor-free prediction) → CONFIRMED-as-hard + first sign-prediction landed.** Two inv-13 gates attacked the empty sector from opposite sides. W1-2 (exterior, strong-field) DELIVERS the framework's first definite-sign compact-object prediction (+ blue-shift QNM, + tidal Love) with zero free parameters — but ~73 OOM below detector reach. W2-1 (interior dense-matter EoS) confirms the diquark-pairing DIRECTION transfers (substrate-IS) but the EoS-stiffness map FAILs to support a 2 M_⊙ star at this construction. CV-9's promise ("dimensionless, anchor-free, escapes M_KK") is half-realized: the SIGNS are anchor-free and clean; the MAGNITUDES are either OOM-suppressed (W1-2) or too-soft (W2-1). The sector is no longer empty of *predictions* — it is empty of *detectable* ones.

- **CV-3 / CV-7-adjacent (S₈ / LSS-distinguishing observable) → CONFIRMED (the one clean win).** W2-2 promotes the framework's σ8-below-Planck from a static coincidence to a quantitative z-dependent f·σ8(z) curve, in-band and DESI/Euclid-bindable. This is the inv-1 B-10 thesis (LSS is the only ΛCDM-distinguishing axis when 2-pt stats match) realized on the growth channel. Honest scope: PARTIAL relief (Planck-side: −2.31% below Planck but +7.08% ABOVE KiDS), not a midpoint tension dissolution.

- **CV-10 (register status optimism outruns derivation) → CONFIRMED + formally adjudicated.** W2-3 is the direct answer to the standing atlas-08 Q44, frozen 40 sessions since S66 W2-A. It supplies elicited per-observable Bayes factors and the recomposition arithmetic. It does NOT itself mutate any register (track-local boundary); it is the INPUT to that mutation. The recomposition finding (structural UP / observational DOWN) is the quantified form of CV-10's meta-pattern.

- **DR3-readiness (not a numbered CV; the w₀ branch-iv secondary) → still-incoherent-NO, cleanly CLOSED.** W1-3 falsified the optimistic S105 register read (FB-envelope-bounded INFO). This is NOT a competing-readings incoherence — it is a settled FAIL on the L_max axis with derivation-admissibility (S101) explicitly UNAFFECTED. No workshop seed.

---

## 3. Four-verb classification

### BOLSTERED

- **a₄ strong-field correction gains a NAMED definite-sign mechanism + forward gate (W1-2).**
  *Claim:* the empty compact-object sector (CV-9) — before: no exterior strong-field prediction. *After:* the a₄ moment generates a definite **+ (blue-shift)** QNM ringdown shift and **+** tidal-Love correction, `sign_verdict=PASS`, sign read off `sign(δω/ω)=sign(c_W)·sign(a₄/a₂)·sign(k_QNM)=(+)(+)(+)`, zero new free parameters (magnitude fixed by canonical a₄^{ζ}/a₂^{ζ}=0.4865 and M_KK alone). *Magnitude:* structural sign; m=1.324e-76 ≪ D_thr=1e-3 (~73 OOM, the universal (ℓ_KK/r_obs)² hierarchy). *Citation:* INV13-W1-2 (audit_sha256 `86e848e8…`); atlas-04 S5 (a₄/a₂=1000:1). A PASS-direction at 0 free params IS evidence (`feedback_reporting-framing.md`); the OOM-suppression makes it a future-detector falsifier, not a present one.

- **S₈ growth-suppression: static coincidence → quantitative redshift-dependent prediction (W2-2).**
  *Claim:* `sigma8_growth_a2=0.79317` below Planck — before: a static single-number coincidence (register S96 INFO, per-bin σ-distances). *After:* a full f·σ8(z) curve, S8_FW=0.8128 in-band [0.76,0.83], suppression sign-PASS 16/16 z-points, DESI-5yr-bindable (1.001σ@z=0.5) + Euclid (1.516σ, 7 bins) — and, with the GW flagship retired (S96, atlas-09 Item 49), this is now the LIVE near-term LSS falsifier. *Magnitude:* observational PASS, band-position 0.75. *Citation:* INV13-W2-2 (audit_sha256 `435609fc…`); `fsigma8_product_suppression_FW_max_pct=−4.058` (register). The lone clean PASS of the investigation and the strongest single positive contribution.

### CHALLENGED

- **GGE cosmological-collider spectroscopy corridor CLOSED-as-NULL (W1-1).**
  *Claim:* gen UB-2 (inv-1 B-5 / CV-5) "highest-leverage untraveled bridge" — before: untraveled, presumed-promising. *After:* CLOSED-as-NULL — Δ_fit=0 on both clock anchors; no μ~O(1) collider-addressable heavy field in the GGE branch content; the framework predicts NO particle-content-off-CMB collider falsifier distinct from the τ_NL amplitude. *Magnitude:* structural (the branches are 150–680× off the μ_crit=3/2 boundary on both clocks). *Citation:* INV13-W1-1 (audit_sha256 `1015fc17…`). Constraint-map: a boundary that ELIMINATES a corridor AND reinforces (independent angle) the Gaussian-by-Wick / f_NL-envelope permanent result — a survivor-strengthening negative.

- **branch-(iv) w₀ DR3-readiness: optimistic Track_A FALSIFIED (W1-3).**
  *Claim:* EVOI Q37 — before: register `S105-BRANCH-IV-DIRECT-L1314 INFO, spread_CAC=0.0443091, FB-envelope-bounded` (the S105 hope that the Friedrich-Bär tail pulls convergence below the 0.025 PASS band). *After:* deep-truncation DIVERGES — spread_CAC=0.0629703 over {12..16} > 0.05 FAIL ceiling; L=15 (the genuinely-new point; L=16 FB-saturated ≡ L=15) GREW the spread +0.018456; ρ_B monotone-decreasing, decelerating-but-NOT-closing. *Magnitude:* structural-numerical; offset-cancellation identity held to machine-ε (`|spread_CAC−spread_rho|=1.11e-16`); CAC anchor exact (w₀^CAC(L=10)=w0_FW=−0.918, resid 0.0). *Scope (load-bearing):* L_max axis ONLY — does NOT retract branch-(iv) derivation-admissibility (`S101-W0-BRANCH-IV-EVALUATOR`, separately settled). *Citation:* INV13-W1-3 (audit_sha256 `ffafc349…`). The R_842-window w₀ secondary is not DR3-defensible on this branch against the ~2027 DESI measurement.

- **finite-μ CFL → dense-matter EoS corridor CLOSED-at-this-construction (W2-1).**
  *Claim:* CV-9 dense-matter NICER-orthogonal test (S38-CLOSED "no formalism" / S25-Goal-7) — before: untested, the cleanest escape from the M_KK problem. *After:* sign=PASS (dΔ_CFL/dμ>0, VanHove-frac=1.000 — substrate diquark pairing has the substitution-chain-predicted density dependence) but magnitude=FAIL (M_max=0.1631 M_⊙, ~12× below the 2 M_⊙ pulsar bound; runaway Δ/μ=4.82 vs physical CFL ~0.05–0.1 → c_s²=1 cap, B_phys ≈ 400× physical). *Magnitude:* structural sign + magnitude FAIL. *Citation:* INV13-W2-1 (audit_sha256 `59f33c74…`); CFL theorem + van Suijlekom BdG-SA (register, both PROVEN). Re-opens S25-Goal-7 with a named refinement (see §4 →COMPUTE-CF). The order parameter transfers (substrate-IS); the emergent EoS stiffness does not — a clean corridor-closing boundary, not an incoherence.

### CLARIFIED

- **(process) s84 cache (4,4)-sector completeness (W1-3 byproduct).**
  *Claim:* `s84_spectrum_cache_L12_tau019.npz` — before: assumed complete. *After:* missing the level-8 (4,4) sector (S84-era gap; S106 rebuilt, dim=125, 2000 eigenvalues); ρ_B on the complete S106 union differs from the s84-incomplete S105 basis by 1.68e-3 — a sector-set difference (both correct on their own set), NOT evaluator drift; apples-to-apples continuity verified (`rho12_continuity_s84=0.0e+00`). Truth value of the branch-iv evaluator UNCHANGED; the canonical truncation is the complete S106 union. *Citation:* INV13-W1-3 WP §W1-3 + lizzi memory; housekeeping process-observation. Precision/scope up, no claim moved — already documented, recorded here for cross-wave visibility only.

### MUDDLED

- **Framework-wide evidence composition: RECOMPOSED, headline stationary by cancellation (W2-3).**
  *Claim:* atlas-08 Q44 / CV-10 — before: EVOI ordinal proxies frozen since S66 W2-A; headline ~22% (S69 anchor) treated as static. *After:* the ~22% holds ONLY because two large opposite-signed cohort movements near-exactly cancel — structural ∏BF UP (10 blind STAGE-3 promotions, joint BF 25–55, constructive-independence per Stage-2 PASS-AND), observational ∏BF DOWN (n_s 4.73σ global post-look-elsewhere, w_a 3.43σ, A_s route-unstable). *Why MUDDLED (net):* the headline number CONCEALS the most important fact (where the framework is now strong vs exposed) — uncertainty about "is the framework getting stronger or weaker?" is INCREASED until the composition is read, which is the dissonance the review exposes and resolves into a directional split. *Component classification on merits (the four-verb rubric applied inside W2-3, per spawn instruction):*
  - n_s 4.73σ-global liability (BF 0.7–0.9, worsening; cannot be rescued by friendliest-anchor) → **CHALLENGED** (real after look-elsewhere; not an artifact).
  - w_a 3.43σ, data moving away (BF 0.6–0.8) → **CHALLENGED** (clearest dark-energy liability; decisive DESI DR3 2027).
  - 10 blind STAGE-3 structural promotions (joint BF 25–55) → **BOLSTERED** (constructive independence, NOT agreement-among-agents; the structural-UP driver).
  - w₀ branch-iv 0.731σ is derivation-INADMISSIBLE post-S86; canonical 2.13σ is the honest figure → **CLARIFIED** (branch-shopping look-elsewhere trap named and rejected; aligns with W1-3's L_max FAIL — the same branch failing on a second axis).
  - m_H +38.5σ with filter-INDEPENDENCE theorem (A10) blocking a 5-trial penalty → **CLARIFIED** (scale success keeps full BF; precision is the cap).
  - neutrino cluster (Σm_ν, m_ββ, NO, δ_CP) → **BOLSTERED** (under-credited zero-parameter sector; JUNO/0νββ near-term).
  *Citation:* INV13-W2-3 `investigation-13-bayesian-reanchor-synthesis.md` §III–§V. The net is MUDDLED-then-resolved-directionally; the components route per their individual verbs in §4.

---

## 4. Routing (pre-routed; orchestrator finalizes Stage 3)

### →WORKSHOP (Q1)

**NONE.** Honest count = 0, matching inv-13's registered design. Tested against the four-condition workshop definition (`Investigating-Workshops.md`): no inv-13 gate produced TWO competing readings of a substrate observable that cannot both be right. The two FAILs (W1-3, W2-1) are clean corridor-closures with scope explicitly bounded (W1-3 L_max-only, S101 admissibility intact; W2-1 this-construction-only, refinement named) — no reading-divergence. The two INFOs (W1-1, W1-2) are pre-registered Track_B nulls. The PASS (W2-2) is unambiguous. The one genuine adversarial tension in this neighborhood — the A_s route-reconciliation (3.15/6.89/9.47 OOM route instability) — is owned by concurrent **inv-12** (`inv-12-as-synthesis.md`, `workshops/as-wall-reading.md`), NOT inv-13. The W2-3 recomposition is MUDDLED-then-directionally-resolved by its own analysis, not a live ledger-dissonance requiring a panel. Q1 = NO across all six gates.

### →COMPUTE-CF (4-field + EVOI)

**CF-INV13-W2-1-FINITE-MU-REFINE** (native to `investigation-13-w2-workingpaper.md §"Carry-Forward Computations"`; the only genuine forward-compute item).
- **What:** re-run the finite-μ CFL gate with a self-consistent μ_eff (μ adjusted WITH density, not a fixed floor-relative scan) + physical pairing-window narrowing forcing Δ/μ → O(0.1); test whether the EoS stiffens M_max into [2.0, 2.6] M_⊙ WITHOUT post-hoc tuning. Re-opens S38-CLOSED "finite-density spectral action (P2b)" / S25-Goal-7.
- **Inputs:** `computations/investigation-13/inv13_w2_1_finite_mu_cfl_eos.npz` (μ-scan + g-calibration χ_ref); `bdg_spectral_triple.py` / `dirac_spectrum.py`; canonical `M_KK`, `Delta_BCS` (R-PROTECTED 0.4642547); L_max=10 D_K cache.
- **Gate:** M_max_FW ∈ [2.0, 2.6] M_⊙ AND Δ/μ ~ O(0.1) at the dense plateau, with `sign_verdict=PASS` retained. INFO if qualitatively stiffer but un-banded; FAIL if runaway Δ/μ persists.
- **Effort:** ~3 wave-equivalents (self-consistent μ_eff solver loop wrapping the existing GPU gap-solve).
- **EVOI:** MODERATE. The sign-PASS already established the substrate result; this tests whether a NICER-orthogonal *magnitude* falsifier can be landed. Per the W2-3 re-anchor §VI.2, a PASS on a non-CMB dataset is worth more than a CMB refinement — but the runaway Δ/μ is a structural culprit, so P(pass) is guarded. Below B-1 (TRANSIT-PS-67) on the session-wide EVOI ladder; this is an inv-13-internal carry-forward, not a survey-wide top item.

*Note — W1-3 does NOT license a CF.* Its SCHEME-DEPENDENT classification (Zubarev late-time functional) does not authorize a functional-shopping re-run: the CAC lockdown (`regulator-convention-lockdown.md`) pins the functional for DR3-class gates, so re-running under an alternative functional to seek convergence would be `v3-closure-recovery.md` Class-6-adjacent iterate-until-PASS. Correctly withheld by the WP.

### →HOUSEKEEPING (register cell + fix)

The inv-13 housekeeping ledger routes these as **§G session-track promotion candidates** (G1–G5) — NOT as an HY1-HY8 list (the spawn-prompt's "HY1–HY8" framing does not match the on-disk file; the actual structure is §G, 5 items). Each crosses the investigation track-local boundary (curated-register mutation) and so is a *lift candidate* for the `/rclab-investigate --investigation 13` close, not an in-investigation edit. Full rescue list in §6.

- **G3 — EVOI Q37 (DESI DR3 / branch-iv):** update from "S105 INFO 0.0443091 / FB-envelope-bounded" → "deep-truncation DIVERGES at L∈{12..16}, spread_CAC=0.0630 > 0.05 FAIL." Scope L_max-only; S101 admissibility UNAFFECTED. (W1-3 CHALLENGED → register-cell down-tag.)
- **G5 — EVOI Tier tables + atlas-08 Q44 closure:** re-anchor Tier-1/Tier-2 with the elicited per-observable P(pass) Bayes factors from the W2-3 synthesis (+ currency bump); closes the 40-session-standing Q44. (W2-3 MUDDLED → register re-anchor.)

### →CLOSED (corridor + note)

- **gen UB-2 GGE cosmological-collider spectroscopy → CLOSED-as-NULL** (W1-1, audit `1015fc17…`). Corridor: collider squeezed-limit feature at D_K eigenvalue ratios. Note: no μ~O(1) heavy field on either clock; reinforces Gaussian-by-Wick / f_NL-envelope permanent result. Constraint-map update recorded, not carried. (Housekeeping §G G1.)
- **finite-μ CFL dense-matter EoS at THIS construction → CLOSED** (W2-1, audit `59f33c74…`). Corridor: cosmological-fold BCS-on-SU(3) extended to finite μ quantitatively predicts 2-M_⊙ dense-matter phenomenology. Note: pairing DIRECTION transfers (sign-PASS), EoS-stiffness does not; the refinement (CF above) re-opens the *item*, not this construction.
- **branch-(iv) w₀ DR3-readiness optimistic Track_A → CLOSED** (W1-3, audit `ffafc349…`). Corridor: FB-tail converges branch-iv w₀ below the 0.025 PASS band. Note: falsified on the L_max axis; the branch-iv derivation itself survives (S101).

---

## 5. Cross-investigation hooks (Stage-2 de-double-count map)

inv-13 is the dedup-survivor batch; most of its conceptual neighbors are owned elsewhere. To prevent the Stage-2 rollup from double-counting, here is who else touches each claim — and where inv-13's contribution is genuinely DISTINCTIVE (the 6 survivors).

| inv-13 claim | Other investigation(s) on the SAME claim | inv-13's distinctive contribution (do NOT merge) |
|:-------------|:------------------------------------------|:--------------------------------------------------|
| GGE bispectrum / collider (W1-1) | **inv-10** (transit-dynamics; CV-5 TRANSIT-PS GGE acoustic P(k) / τ_NL, bridge B-1). inv-10 owns the *power-spectrum / amplitude* leg. | W1-1 is the *squeezed-limit COLLIDER-SPECTROSCOPY* leg specifically — sharper than inv-10's τ_NL, testing for non-analytic features at eigenvalue ratios. Closes that distinct corridor as NULL. Merge ONLY the shared "GGE non-Gaussianity is amplitude-only, no collider structure" conclusion; keep the two legs separate. |
| a₄ QNM/tidal (W1-2) | **inv-11** W5-2 (compact-object INTERIOR build); **inv-4** (einstein; CV-9 compact-object, greybody). | W1-2 is the strong-field EXTERIOR leg (QNM ringdown + tidal Love), explicitly complementary to inv-11's interior. The definite-+-sign result is inv-13-unique. |
| finite-μ CFL EoS (W2-1) | **inv-11** (landau; compact-object interior, NICER); CV-7-adjacent (mack PBH compact-object). | W2-1 is the dense-matter COLOR-SUPERCONDUCTIVITY EoS at high μ — genuinely untraveled (inv-1 §2 row), a NICER test orthogonal to the CMB axis. The sign-PASS/EoS-soft split is inv-13-unique. |
| S₈ / f·σ8(z) (W2-2) | **inv-7** (INV7-W1-6 model-vs-model joint χ²); **inv-8** (plan-w1 references the same suppression); cosmic-web (inv-1 B-10 Void/Betti). | W2-2 is the S₈-BAND-MEMBERSHIP + dense-grid DESI/Euclid BINDABILITY extraction — distinct observable from inv-7's joint χ² and S96's per-bin σ. Same growth-ODE machinery (matches INV7-W1-6 by construction), different deliverable. Merge the machinery, keep the observable distinct. |
| branch-iv w₀ DR3 (W1-3) | **inv-11** W5-1 (mkk-gap-vs-integer-scheme — adjacent w₀ machinery); session-track S101/S103/S105 (the prior DR3 chain). | W1-3 is the L∈{15,16} deep-truncation extension specifically — the genuine new computation past S105. Distinctive. |
| Bayesian re-anchor (W2-3) | **inv-12** (connes; A_s wall — the observational-axis neighbor); ALL investigations feed the recomposition. | W2-3 is the framework-WIDE empirical recomposition (Q44) — it CONSUMES the other investigations' outcomes as inputs to the BF table. At Stage-2 this is the natural aggregation node for the observational cohort; do NOT re-derive its per-observable BFs from the component investigations — cite W2-3 as the rollup. |

**The 6 distinctive survivors (inv-13's net contribution to the 13-investigation rollup):** (1) GGE collider-spectroscopy NULL; (2) a₄ exterior strong-field definite-sign null; (3) finite-μ color-SC EoS sign-PASS/soft-FAIL; (4) branch-iv w₀ L{15,16} truncation-divergence; (5) S₈ f·σ8(z) in-band LSS-flagship PASS; (6) the post-S66 Bayesian recomposition (Q44 closure). Everything else inv-13 touched is a shared-anchor companion to be merged at Stage-2.

---

## 6. Stranded hygiene (rescue list)

inv-13's housekeeping ledger §G enumerates **5 session-track promotion candidates** (G1–G5) — the items inv-13 routed OUT toward session-track registers but, by the investigation track-local boundary (`gate-verdicts.md §"Investigation-Track Canonical Path"`), could NOT apply in-investigation. These are the stranded-hygiene rescue list (the on-disk structure is §G, not the spawn-prompt's "HY1–HY8"). Each is turnkey (target + recommended edit verbatim from the ledger):

| # | Source gate / outcome | Promotion target (register cell) | Recommended edit | Verb it serves |
|:--|:----------------------|:---------------------------------|:-----------------|:---------------|
| **G1** | W1-1 INFO (ANALYTIC-LOCAL) | constraint-map / `falsifier-master-inventory.md` (mack sole-writer) | Record gen UB-2 (GGE cosmological-collider spectroscopy) CLOSED-as-NULL — no μ~O(1) collider-addressable heavy field on either clock anchor; reinforces Gaussian-by-Wick / f_NL-envelope permanent result. | →CLOSED |
| **G2** | W1-2 INFO (definite-sign sub-detectable) | `falsifier-master-inventory.md` (mack sole-writer) | Candidate row: a₄ higher-curvature QNM/tidal correction — definite **+** (blue-shift) sign, m≈10⁻⁷⁶ ≪ 10⁻³, zero free params; future-detector falsifier constraining M_KK from the strong-field side. audit_sha256 `86e848e8…`. | →BOLSTERED (forward-gate row) |
| **G3** | W1-3 FAIL (truncation-divergent) | EVOI register Q37 (DESI DR3 / branch-iv) | Update Q37: "S105 INFO 0.0443091 / FB-envelope-bounded" → "deep-truncation DIVERGES at L∈{12..16}, spread_CAC=0.0630 > 0.05 FAIL." Scope: L_max axis only; branch-iv derivation-admissibility (S101) UNAFFECTED. audit_sha256 `ffafc349…`. | →HOUSEKEEPING (CHALLENGED down-tag) |
| **G4** | W2-2 PASS (S8 in-band, bindable) | `falsifier-master-inventory.md` (mack sole-writer) | LSS-flagship row: the f·σ8(z) growth-suppression curve as a DESI-5yr (1.001σ@z=0.5) / Euclid (1.516σ, 7 bins) bindable S8-tension-relief discriminator; now the LIVE near-term LSS falsifier (GW flagship retired S96). Honest caveat: partial relief, Planck-side. audit_sha256 `435609fc…`. | →BOLSTERED (live-falsifier row) |
| **G5** | W2-3 LANDED (review) | `evoi-framework.md` Tier tables + mack/Sagan co-dispatch; atlas-08 Q44 | Re-anchor the EVOI Tier-1/Tier-2 tables with the elicited per-observable P(pass) Bayes factors from `investigation-13-bayesian-reanchor-synthesis.md` (+ currency bump); mack + Sagan co-dispatch on observational-surface rows (n_s 4.73σ, w_a 3.43σ, A_s wall, w₀ branch-shopping); closes the standing atlas-08 Q44. The review synthesis IS the input to this promotion. | →HOUSEKEEPING (Q44 closure + re-anchor) |

All five are register-edits effected at the `/rclab-investigate --investigation 13` close (or, if lifted into a session, at session-promotion), NOT compute gates. None is a math carry-forward (the sole math CF is CF-INV13-W2-1-FINITE-MU-REFINE in §4). The W2-3 mack/Sagan observational-surface co-dispatch (G5) carries the highest cross-register leverage: it touches the n_s 4.73σ and w_a 3.43σ load-bearing liability rows with the anti-rescue fence (PROHIBITED_ACTIONS Class 1) armed.

---

*Distillation complete. inv-13: 1 PASS / 2 FAIL / 2 INFO + 1 LANDED review; verbs B=2 / C=3 (+3 component-CHALLENGED inside W2-3) / CL=1 (+2 component-CLARIFIED inside W2-3) / M=1; workshops routed = 0 (registered honest count; the lone neighbor tension is inv-12's A_s reconciliation). The structural spine: sign-PASS on all five chains, magnitude/truncation the binding constraint — the inv-1 §0 verdict instantiated six ways.*
