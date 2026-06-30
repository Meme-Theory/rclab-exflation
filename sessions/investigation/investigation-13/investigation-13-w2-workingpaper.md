# Investigation 13 Wave 2 — Empirical bridges: dense-matter, growth-of-structure, Bayesian re-anchor (Results Working Paper)

**Investigation**: 13 | **Wave**: 2 | **Plan**: investigation-13-plan-w2.md | **Track**: investigation (verdict ledger `computations/investigation-13/inv13_gate_verdicts.txt`) | **Theme**: three empirical bridges orthogonal to the n_s/A_s/w_0 CMB axis — finite-μ CFL EoS, GGE growth-suppression f·σ8(z), post-S66 Bayesian re-anchor. **Mixed-type wave: 2 compute + 1 review.**

## Gate Sections

### §W2-1. INV13-W2-1-FINITE-MU-CFL-EOS (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `INV13-W2-1-FINITE-MU-CFL-EOS`
**Trigger**: `[SIGN]` (on dΔ_CFL/dμ)
**Classification**: **PHONONIC** (diquark gap IS a substrate order parameter of the BdG fabric)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: The van Suijlekom finite-density action D_μ = D + μQ at high μ (SU(3) fiber = color) yields a CFL/2SC gap Δ_CFL(μ) whose EoS stiffness supports M_max ≥ 2 M_⊙ in band [2.0, 2.6], the framework's first compact-object anchor on a NICER-orthogonal dataset.
**Plan reference**: `sessions/investigation/investigation-13/investigation-13-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain).

**Output Artifacts**:
- Script: `computations/investigation-13/inv13_w2_1_finite_mu_cfl_eos.py` — present; contains `from canonical_constants import` (line 84) and `print_verdict_payload` (defined line 712, called line 693). PASS.
- Data: `computations/investigation-13/inv13_w2_1_finite_mu_cfl_eos.npz` — present (13 KB); holds the full-float64 μ-scan (`mu_grid`, `Delta_grid`, `n_win_grid`, `chi_grid`, `dDelta_dmu`), the TOV curve (`M_tov`, `R_tov`, `eps_c_grid`), the calibration (`g_coupling`, `chi_ref`, `mu_ref`), the EoS diagnostics (`eos_*`), the 3-tuple sub-verdicts, and the dual-SHA. PASS.
- Plot: `computations/investigation-13/inv13_w2_1_finite_mu_cfl_eos.png` — present (122 KB); 3-panel (Δ_CFL(μ) gap curve vs Δ_BCS reference; TOV M–R with the [2.0, 2.6] M_⊙ PASS band; Van-Hove window occupation vs μ). PASS.
- Verdict line: `computations/investigation-13/inv13_gate_verdicts.txt` — `INV13-W2-1-FINITE-MU-CFL-EOS: FAIL` line present, matching `^INV13-W2-1-FINITE-MU-CFL-EOS:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + `[SIGN]` 3-tuple companion row + `regulator_pin` extra-row + calibration extra-row all landed (5 rows). PASS.

**Verdict-line closure checklist**:
- Emitted via `emit_verdict(session=13, track="investigation", ...)` → `computations/investigation-13/inv13_gate_verdicts.txt` (investigation track, NOT a session-{N} path). ✓
- Canonical 4-tuple: `value='M_max_FW=0.1631_Msun_band[2.0,2.6]_Delta_CFL_plateau=2.4107_MKK_dDelta/dmu>0=True_VanHove_frac=1.000_gap_ratio=4.8213'` scheme=`BdG-spectral-action-vanSuijlekom-Dmu` convention=`ABSOLUTE` L_max=`10`. ✓
- Dual-SHA (full 64-char): `audit_sha256=59f33c74b5b1df8bd3367de6dc72a196830885948895e277ed3d2d23e023f4fd`, `content_sha256=cd90e8202dd586ce7b8b870e606acf0cd8bf675d9c1fc9063dae37d6ecee6818`. ✓
- `[SIGN]` 3-tuple companion row: `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`. ✓
- `# regulator_pin=a_n^{Pauli-Villars}_LambdaUV_M_KK` companion row + calibration companion row (`Δ(μ_ref=0.10)=Δ_BCS=0.4642547`, R-PROTECTED, g pinned before scan). ✓
- sig_5 unique (tool-enforced, cross-process locked). ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("finite-mu CFL color superconductor diquark gap EoS neutron star maximum mass van Suijlekom")` → returns the **CFL theorem** (PROVEN, dense-QCD SU(3)_c × SU(3)_L+R → diagonal SU(3) at μ_QCD ≳ 1 GeV) + the **BdG spectral action paper** (PROVEN, "first application of van Suijlekom finite-density to BCS on SU(3)", `session-34-master-synthesis.md`) + prior `s66_finite_mu_sa.py` (SA-66) and `s66_color_singlet_cc.py` (CC-66). The finite-μ *formalism* is PROVEN/available; the finite-μ *CFL-gap-→-EoS-→-M_max* chain at the dense-QCD regime is NOT pre-closed — this gate runs it for the first time (confirming the "finite-density spectral action CLOSED-no-formalism S38 / self-consistent μ_eff OPEN S25-Goal-7" tags). NOT PRE-CLOSED.
- `get_constant("Delta_BCS")` → `0.4642547394830737` (S70, R-PROTECTED, gate `BCS-GAP-CANONICAL-70`, alias of `Delta_0_OES`). This is the calibration anchor; the script pins the pairing coupling g so the self-consistent gap at μ_ref reproduces it BEFORE the μ-scan (Paper 06 §III pre-registration discipline). VERIFIED — `Δ(μ_ref=0.10)=0.4683` reproduces the canonical to ~0.9% (linear-interp vs exact-root; coupling pinned correctly).

**Verdict**: **FAIL** — composite via the pre-registered 3-tuple collapse rule (`magnitude_verdict=FAIL ∧ regime_verdict=VALID ⇒ composite=FAIL`, `gate-verdicts.md §Composite-collapse`). The **[SIGN] axis PASSES** (`sign_verdict=PASS`): the durable physics result is that the substrate's diquark gap has the correct density-dependence. The **magnitude axis FAILS**: the EoS the gate constructs is far too soft. A FAIL closes the corridor "the finite-μ extension of the cosmological-fold BCS machinery quantitatively reproduces dense-matter (2-M_⊙-pulsar) phenomenology" — and per the dual prior re-allocates 0.9 mass to **Track B** (regime-limited / too-soft): the gap is qualitatively present and SIGN-correct, but the EoS is too soft, leaving the prediction outside the [2.0, 2.6] M_⊙ band. FAIL is a result, not an agent failure (`math-scripts.md §All Results Are Good Results`): it tells us the BCS-on-SU(3) object's EoS-stiffness mapping is fold-specific at this construction, not yet a universal substrate prediction.

**Results**:

*Numerical outputs (4 sig figs):*
- **Δ_CFL at the dense plateau** (μ = 0.5 M_KK): **2.411 M_KK** — runaway, ~5.2× the canonical Δ_BCS = 0.4643.
- **M_max_FW** = **0.1631 M_⊙** at R = 0.6755 km — ~12× below the 2.0 M_⊙ pulsar lower bound.
- **gap ratio Δ/μ at plateau** = **4.821** — the failure driver (real CFL has Δ/μ ~ 0.05–0.1; here the gap does NOT soften with density relative to μ).
- **4-tuple**: `(value=M_max_FW=0.1631_Msun_band[2.0,2.6]…gap_ratio=4.8213, scheme=BdG-spectral-action-vanSuijlekom-Dmu, convention=ABSOLUTE, L_max=10)`.
- **Calibration**: g = 1.3636e-04 pinned so Δ(μ_ref=0.10) = Δ_BCS (χ_ref = 7333.69); 78,080 eigenvalues w/ multiplicity loaded from the L_max=10 cache; GPU device = cuda.
- **EoS diagnostics**: c_s² = 1.000 (causal-capped, from 1/3 + (Δ/μ)² with Δ/μ = 4.82); B_phys = 23541 MeV/fm³ (~400× the physical 57–90 MeV/fm³ window) — the oversized bag constant is the proximate cause of the tiny, dense star.

*Substitution chain for the [SIGN] axis (dΔ_CFL/dμ), substituted with the computed numbers:*
- Plan Step 4 prediction: `d ln Δ_CFL/dμ = +[1/(g(μ)²·V_Kosmann)]·(dg/dμ)`, every RHS factor positive ⇒ dΔ_CFL/dμ > 0.
- Computed: dΔ_CFL/dμ > 0 at **every one of the 25 scan points** (`frac_increasing = 1.000`); Δ_CFL rises monotonically 0.0037 M_KK (μ=0) → 2.411 M_KK (μ=0.5), strictly increasing across the full scan. Read-off sign: **+** (matches the predicted +). **sign_verdict = PASS**.
- **regime_verdict = VALID**: the Van-Hove-dominated fraction over the dense scan (μ ≥ μ_ref) is **1.000** — the pairing window is non-empty and monotonically growing (`dn_window/dμ ≥ 0`) at every dense point (window occupation 1335 → 2548 modes); the cusp is captured from the dense side throughout, so the Step-2 DOS-monotonicity premise of the substitution chain holds across the entire window. No regime breakdown.
- **magnitude_verdict = FAIL**: `M_max = 0.1631 M_⊙ ∉ [2.0, 2.6]` and below the qualitatively-stiff INFO floor (0.5·2.0 = 1.0 M_⊙).

*Constraint-map consequence:*
- This gate is the **first run** of the finite-μ CFL-gap → EoS → M_max chain (the S38-CLOSED "no formalism" / S25-Goal-7 "self-consistent μ_eff OPEN" item, re-opened by this machinery). It establishes a clean structural result (SIGN + regime PASS) and a clean magnitude FAIL.
- **The corridor "the cosmological-fold BCS-on-SU(3) machinery, extended to finite μ, quantitatively predicts dense-matter phenomenology" is CLOSED at this construction.** The diquark pairing direction transfers (substrate-IS), but the EoS-stiffness map does not yet yield a 2-M_⊙-supporting star — the runaway Δ/μ (no density-softening of the gap relative to μ) is the structural culprit.
- **Carry-forward** (INFO_meaning route, but composite is FAIL because regime is VALID not MARGINAL): a finite-μ refinement is warranted — the gap-equation coupling is pinned at a single low-μ reference where the in-band DOS is enormous (χ_ref ≈ 7334), inflating the dense-μ gap; a self-consistent μ_eff (μ adjusted with density rather than a fixed floor-relative scan) and a physical pairing-window narrowing (Δ/μ → O(0.1)) are the next-session compute to test whether the EoS can be stiffened into band WITHOUT post-hoc tuning. See the Carry-Forward Computations block.

**Substrate framing** (PHONONIC): The substrate IS the finite-μ BdG spectrum. The direction of explanation flows D_K eigenvalues → the van Suijlekom shifted operator D_μ = D + μ Q → the Nambu-doubled BdG block `[[ξ, Δ],[Δ*, −ξ]]` whose gap edge `E_k = √(ξ² + Δ²)` IS the color-superconducting condensate → the EoS pressure (a spectral moment of the BdG spectrum) → the TOV maximum mass (the emergent observable NICER measures). A neutron-star core is NOT matter sitting IN a dense container — it is the **densest sustainable excitation of the D_K fabric**, the regime where the local τ-modulus (which tracks density per the substrate-compaction picture) is driven toward an extreme and the SU(3) fiber's color pairing saturates. The CFL gap Δ_CFL(μ) is the SAME substrate order parameter as the cosmological-fold U(1)_7-breaking BCS condensate (μ = 0 by particle-hole symmetry, proven S34), read here at a different point in the (μ, τ) plane (μ ≠ 0). The Van-Hove A_2-catastrophe structure (B1, RG-BCS-35 PROVEN) that makes Cooper pairing a theorem at the fold IS what makes the gap grow with μ at high density — which is exactly why the SIGN axis passes. The magnitude FAIL is the substrate telling us that the *order parameter* transfers but the *emergent EoS stiffness* does not yet land the compact-object observable; it does NOT invert the explanatory arrow — the EoS is still derived FROM the BdG spectrum, not imposed on it.

---

### §W2-2. INV13-W2-2-FSIGMA8-GROWTH-S8 (cosmic-web-theorist)

**Status**: COMPLETED
**Gate ID**: `INV13-W2-2-FSIGMA8-GROWTH-S8`
**Trigger**: `[SIGN]` (on the suppression direction: f·σ8 < ΛCDM)
**Classification**: **PHONONIC** (structure IS the interference pattern of post-transit GGE acoustic excitations)
**Agent**: `cosmic-web-theorist`
**Hypothesis**: Propagating the static σ8 + the −4.058% z=0.51 f·σ8 product-suppression seed into a redshift-dependent f·σ8(z) curve lands S8_FW ∈ [0.76, 0.83] (between Planck and weak-lensing) with a DESI/Euclid-bindable z-shape, and localizes a possible n_s failure to the K_pivot mapping.
**Plan reference**: `sessions/investigation/investigation-13/investigation-13-plan-w2.md` §W2-2 (machinery pin, thresholds, substitution chain).

**Output Artifacts**:
- Script: `computations/investigation-13/inv13_w2_2_fsigma8_growth_s8.py` (contains `from canonical_constants import`, `print_verdict_payload`) — present, 38,168 bytes.
- Data: `computations/investigation-13/inv13_w2_2_fsigma8_growth_s8.npz` — present, 21,633 bytes (z-grid, f·σ8 curves, δ(z), S8, bindability ratios, upstream cross-check arrays).
- Plot: `computations/investigation-13/inv13_w2_2_fsigma8_growth_s8.png` — present, 151,977 bytes (Panel 1: f·σ8(z) FW vs ΛCDM on the dense 16-pt grid + DESI-5yr forecast σ; Panel 2: per-z fractional suppression δ(z) with the DESI-5yr ±1σ bindability band; Panel 3: S8 placement vs Planck/KiDS/DES band).
- Verdict line: `computations/investigation-13/inv13_gate_verdicts.txt` line 13 matches `^INV13-W2-2-FSIGMA8-GROWTH-S8:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion (line 14) + `[SIGN]` 3-tuple companion (line 15) present.
- This WP section: `**Status**: COMPLETED`.

**Verdict-line closure checklist**:
- Emitted via `emit_verdict(session=13, track="investigation", ...)` → `computations/investigation-13/inv13_gate_verdicts.txt` (investigation-track canonical path).
- Canonical line 4-tuple: `(value=S8_FW=0.8128…, scheme=GGE-acoustic-growth-a2, convention=RATIO, L_max=N/A)`.
- `audit_sha256=435609fc74bc4d3c8b0ec79eb0a37e18571ebd9bd657d34ce9fc9c7874c56485` (full-64); `content_sha256=2d2e918a289024429452ee40865caaa535cb501196dd65d5d03bece2fd970a94` (full-64).
- `[SIGN]` 3-tuple companion (schema-v2): `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.

**MCP Pre-Compute Audit**:
- `get_constant("sigma8_growth_a2")` → 0.79317 (a₂ Seeley-DeWitt growth channel; FEEDS fσ8 forecasts; channel-distinct partner of the headline; **the value USED for growth normalization**).
- `get_constant("fsigma8_product_suppression_FW_max_pct")` → −4.058 (Row #71, S96; the z=0.51 product-suppression seed; source npz `s96_obs_fsigma8_forecast.npz`).
- `get_constant("f_bare_suppression_FW_pct")` → −0.311 (the SMALL bare-f number, distinct from the −4.058% product; cross-check anchor).
- `search_knowledge("fsigma8 growth suppression S8 tension redshift DESI Euclid")` → confirms `fsigma8_product_suppression_FW_max_pct` is sign-negative (suppression), reproduced by inv-7/inv-8 plans; the S96-OBS-FSIGMA8-FORECAST gate (INFO) is the producing gate. **NOT PRE-CLOSED**: this gate is a NEW deliverable (S8 band membership + dense-grid DESI/Euclid bindability) distinct from S96 (per-bin σ-distances) and INV7-W1-6 (model-vs-model joint χ²) — same growth-ODE machinery, different observable extraction.

**Verdict**: **PASS** — composite via the [SIGN] 3-tuple collapse (sign=PASS ∧ magnitude=PASS ∧ regime=VALID ⇒ PASS).

**Results**:

*Substrate framing.* PHONONIC. The substrate IS the GGE acoustic-interference structure. Direction of explanation: D_K eigenvalues → the post-transit GGE relic (59.8 quasiparticle pairs, P_exc=1.000) → the a₂ Seeley-DeWitt growth channel (the second spectral moment that generates the emergent Einstein–Hilbert action and thereby the linear-growth ODE) → the growth-rate suppression δ(f·σ8)(z) → the observed S8 and the f·σ8(z) curve DESI/Euclid measure. Large-scale structure is NOT density perturbations growing IN an expanding container — it IS the interference pattern of post-transit GGE acoustic excitations, gravitationally self-organized through the a₂ channel. A finite-coherence interference pattern under-grows relative to a smooth ΛCDM transfer, which is WHY the suppression is negative and WHY the framework's σ8 sits below the Planck reference.

*Sourcing discipline (load-bearing).* The growth normalization is `sigma8_growth_a2 = 0.79317` — the a₂ Seeley-DeWitt structure-growth-channel readout that FEEDS fσ8 forecasts — **NOT** the headline `sigma8_OZ_50 = 0.799` (O-Z / spectral-action channel). The two are channel-distinct substrate-IS readouts 0.735% apart; the spread is NOT a single-channel uncertainty band. The script imports and uses `sigma8_growth_a2`; the headline value is reported in the npz/plot for reference only (`S8_OZ_headline = 0.8187`), never in the growth normalization.

*4-tuple.* `(value=S8_FW=0.8128(band[0.76,0.83]:IN);S8_LCDM=0.8310;sign=16/16neg;…, scheme=GGE-acoustic-growth-a2, convention=RATIO, L_max=N/A)`.

*Substitution chain for the [SIGN] axis (δ(f·σ8) < 0), with substituted numbers:*
- Step 1: f·σ8(z) = f(z)·σ8(z), f(z) = dlnD/dlna (standard linear-growth observable).
- Step 2: σ8(z=0)_FW = `sigma8_growth_a2` = **0.79317** (a₂ growth channel, NOT the headline 0.799), already BELOW the ΛCDM reference σ8 = 0.811 (−2.18% vs ΛCDM).
- Step 3: GGE acoustic-interference modifies the growth rate: f·σ8_FW(z) = f·σ8_ΛCDM(z)·[1 + δ(z)], with δ(z=0.51) = `fsigma8_product_suppression_FW_max_pct`/100 = **−0.04058** (Row #71, NEGATIVE — the post-transit GGE relic suppresses small-scale growth).
- Step 4: propagating across z via the a₂-growth-channel ODE (FW: w = `w0_FW` = −0.918; ΛCDM: w = −1), the computed envelope is δ(z) ∈ **[−4.063%, −2.503%]** for z ∈ [0,1.5] (peak −4.063% at z=0.5; the dense-grid neighbor of the upstream −4.058% @ z=0.51).
- Step 5: every δ(z) < 0 (computed **16/16** grid points negative) ⇒ f·σ8_FW(z) < f·σ8_ΛCDM(z) ∀z ⇒ S8_FW < S8_ΛCDM. Read-off sign: **NEGATIVE (suppression)**. `sign_verdict = PASS`.

*Canonical-anchor reproduction (cross-check, ODE-integration precision ~3e-5):*
- f_FW(z=0) = 0.52546 vs canonical 0.52549 (Δ −2.9e-5); f_LCDM(z=0) = 0.52710 vs canonical 0.52713 (Δ −2.7e-5).
- bare-f suppression −0.3113% vs canonical −0.311%; product-suppression peak −4.058% @ z=0.51 (upstream npz).
- S8_FW = 0.8128 vs upstream S96 0.8128 (Δ +3e-6); S8_LCDM = 0.8310 vs upstream 0.8310 (exact). The growth-ODE machinery matches INV7-W1-6 by construction.

*Magnitude axis (S8 band).* S8_FW = `sigma8_growth_a2`·√(Ω_m/0.3) = **0.8128**, which is **inside** the target band [0.76, 0.83] (distance to the upper edge +0.0172; band fractional position 0.75, i.e. three-quarters of the way from the lensing edge toward the Planck edge). S8_LCDM = 0.8310. `magnitude_verdict = PASS`. **Honest placement caveat**: S8_FW sits −2.31% below Planck (S8≈0.832) but +7.08% **above** KiDS (S8≈0.759) — it is in-band but on the *Planck side* of the tension, a partial relief, not a midpoint resolution. The substrate's σ8 is below Planck (the relief direction is correct) but the magnitude of relief is modest; the framework predicts an S8 closer to Planck than to weak lensing.

*Bindability axis (DESI/Euclid).* Using the canonical-consistent absolute form `|Δf·σ8(z)| / σ_abs(z)` (where the S96 `sigma_desi5_per_bin` is verified to be an ABSOLUTE fσ8 error, = err_obs/2; dividing the *fractional* δ by it would be the mnemonic-vs-exact trap of `math-scripts.md` and would inflate the ratio ~2.1×): DESI-5yr max bind ratio = **1.001σ @ z=0.5** (1 bin ≥ 1σ), reproducing the upstream Row #71 headline 1.013σ @ z=0.51 within the dense-grid-vs-eff-z resolution. Euclid max bind ratio = **1.516σ** (7 bins ≥ 1σ). `bindable = True` at the headline survey ⇒ the PASS rubric's bindability requirement is met (marginally at DESI-5yr, decisively at Euclid).

*K_pivot-localization corollary (NON-gating, reported only).* `kpivot_localization_available = True`. The clustering scale (k ~ 0.1–0.3 h/Mpc, where the 8 h⁻¹ Mpc top-hat σ8 lives) is a different and more robustly-mapped scale than the CMB pivot K*. A growth-suppression success here while n_s fails at the CMB pivot (seed G1) would LOCALIZE a possible n_s failure to the K_pivot mapping (seed G3), NOT the underlying GGE growth physics. This is a diagnostic the framework currently cannot make from the n_s axis alone; it does NOT enter the verdict.

*Constraint-map consequences.*
- **Track A (S8-tension resolution; dual_prior posterior → 0.9):** S8_FW lands in-band with a strictly-negative suppression and a DESI/Euclid-bindable z-shape, so the framework's σ8 below Planck is promoted from a static coincidence to a QUANTITATIVE redshift-dependent prediction. The relief is partial (Planck-side, not midpoint), so this is a measured success, not a full tension dissolution.
- **LSS-flagship migration:** with the GW-detector flagship retired (S96, atlas-09 Item 49, peak GW-sterile at 8.48e39 Hz), this f·σ8(z) curve + the companion first-sound ring (Row #72, A_FS=0.204 @ k1=0.0193 Mpc⁻¹, SNR 8.6) are the LIVE near-term LSS falsifiers. The z=0.51 product suppression sits at the DESI-5yr 1σ edge — binding now, decisive with Euclid.
- **Carry-forward candidate** (route to mack-cosmic-bridge sole-writer + session-promotion, NOT landed here per the investigation track-local boundary): a falsifier-inventory row for the f·σ8(z) growth-suppression curve as a DESI-5yr/Euclid-bindable LSS discriminator, citing this gate's audit_sha256.

**Dual-SHA**: `audit_sha256=435609fc74bc4d3c8b0ec79eb0a37e18571ebd9bd657d34ce9fc9c7874c56485`; `content_sha256=2d2e918a289024429452ee40865caaa535cb501196dd65d5d03bece2fd970a94`.
**Artifacts**: `inv13_w2_2_fsigma8_growth_s8.py` / `.npz` / `.png`.

---

### §W2-3. INV13-W2-3-BAYESIAN-REANCHOR (sagan-empiricist)

**Status**: LANDED (review gate — artifact-existence-with-content closure per `wave-classification.md §M1`; NO verdict line, by design)
**Gate ID**: `INV13-W2-3-BAYESIAN-REANCHOR`
**Trigger**: `[AUDIT]` (evidence-audit / re-anchoring analysis — NOT a numerical-threshold gate)
**Classification**: **NON-PHONONIC** (empirical-conscience adjudication; closes by artifact-existence-with-content == `wave-classification.md §M1`)
**Agent**: `sagan-empiricist` (review executor = question owner, its own domain)
**Hypothesis**: A formal post-S66 Bayesian re-anchor — elicited per-observable P(pass) Bayes factors, look-elsewhere-corrected — shows the framework's evidence has RECOMPOSED (structural strengthened via 10 blind STAGE-3 promotions; observational weakened via n_s + w_a drift) while the headline probability sits near the ~22% S69 anchor.
**Plan reference**: `sessions/investigation/investigation-13/investigation-13-plan-w2.md` §W2-3 (`review:` block — sources, output path, required content).

**Artifact-existence closure checklist** (review gate — closes by artifact-existence-with-content; **NO verdict line, NO MCP Pre-Compute Audit block**):
- Deliverable `sessions/investigation/investigation-13/investigation-13-bayesian-reanchor-synthesis.md` — **EXISTS** (19.6 KB). Orchestrator-verified `grep` over the 9 `must_contain` markers returned 42 total hits with every distinct marker present: `## ` (section headers incl. §IV "Per-Observable P(pass) / Bayes-Factor Table"); `Bayes factor` / `P(pass)` (the §IV BF table); `look-elsewhere` (the Gross-Vitells correction on the multi-anchor n_s + the w₀ branch-shopping trap); `recomposition` (the structural-up/observational-down finding); `prediction` (the PREDICTION/FIT/ACCOMMODATION triage); `n_s` (the 4.73σ liability row); `blind` (the 10 blind-cross-axis STAGE-3 promotions); `track-local` (the boundary note). No missing marker ⇒ LANDED.

**Verdict**: **LANDED** — review closure is binary artifact-existence (not PASS/FAIL/INFO); the synthesis md is on disk with all 9 markers. NO verdict line in `inv13_gate_verdicts.txt` (a verdict line on a review gate is a type error per `gate-verdicts.md §"Investigation-Track Canonical Path"`).

**Results**: the deliverable `investigation-13-bayesian-reanchor-synthesis.md` carries the per-observable P(pass)/Bayes-factor table (n_s strongest LIABILITY 4.73σ post-look-elsewhere; α_s scale-channel rescope; A_s route-unstable wall; w₀ canonical 2.13σ with the branch-iv 0.731σ branch-shopping trap flagged; w_a 3.43σ; m_H +38.5σ capped by a filter-independence theorem; CC tracking-form; the neutrino cluster; and the 10 blind-cross-axis STAGE-3 promotions joint BF 25–55), the look-elsewhere correction on the multi-anchor n_s + α_s comparisons, the **recomposition finding** (structural-UP / observational-DOWN, headline near the ~22% S69 anchor — composition shifted toward publishable mathematics + lab/JUNO falsifiers and away from CMB-cosmology fit), and the **track-local boundary** note (this gate WRITES the analysis only; the EVOI Tier-table re-anchor + the mack + Sagan co-dispatch on the observational-surface rows are SESSION-TRACK actions routed to the `/rclab-investigate --investigation 13` close; this review is their INPUT, closing atlas-08 Q44). See the Wave 2 Synthesis "session-track promotions" note above.

---

## Wave 2 Synthesis (team-lead)

Two compute + one review empirical bridge — each pushing the framework onto an axis ORTHOGONAL to the n_s/A_s/w_0 CMB-cosmology axis that carries all its current empirical risk — closed: **1 PASS + 1 FAIL + 1 LANDED review**.

**Per-gate — what was computed, what region it constrains:**

- **§W2-1 finite-μ CFL EoS (FAIL; sign=PASS, magnitude=FAIL).** First run of the finite-μ CFL-gap → EoS → M_max chain (van Suijlekom `D_μ=D+μQ`). **sign=PASS** (the durable result): dΔ_CFL/dμ>0 at every one of the 25 scan points (Van-Hove-dominated frac=1.000) — the substrate's diquark gap has the substitution-chain-predicted density dependence. **magnitude=FAIL**: M_max=0.1631 M_⊙ (~12× below the 2 M_⊙ pulsar bound), driven by a runaway gap_ratio Δ/μ=4.82 (real CFL ~0.05–0.1) → c_s²=1 causal cap, B_phys≈23541 MeV/fm³ (~400× physical). **Constrains:** the cosmological-fold BCS-on-SU(3) diquark-pairing DIRECTION transfers to the dense regime (substrate-IS), but the EoS-stiffness map does NOT yet land a 2-M_⊙-supporting star — corridor CLOSED at this construction. Re-opens the S38-CLOSED "finite-density spectral action (P2b)" / S25-Goal-7 self-consistent-μ_eff item. Calibration verified (Δ(μ_ref)=Δ_BCS=0.4642547, R-PROTECTED, g pinned BEFORE the scan).

- **§W2-2 fσ8 growth S8 (PASS).** S8_FW=0.8128 in-band [0.76,0.83] (band-pos 0.75); suppression 16/16 z-points negative (sign=PASS); DESI-5yr bindable 1.001σ @ z=0.5 (1 bin) + Euclid 1.516σ (7 bins). Sourcing discipline honored: `sigma8_growth_a2=0.79317` used, NOT the headline `sigma8_OZ_50=0.799` (channel-distinct, 0.735% apart). **Constrains:** promotes the framework's σ8-below-Planck from a static coincidence to a quantitative redshift-dependent prediction; with the GW-detector flagship retired (S96, atlas-09 Item 49), this f·σ8(z) curve is the **LIVE near-term LSS falsifier**. **Honest caveat:** partial relief — Planck-side (−2.31% below Planck but +7.08% ABOVE KiDS), not a midpoint resolution of the S8 tension. K_pivot-localization corollary available (non-gating).

- **§W2-3 Bayesian re-anchor (LANDED review; no verdict line).** Synthesis md on disk with all 9 must_contain markers (verified). Per-observable P(pass)/Bayes-factor table: n_s the strongest LIABILITY (4.73σ global post-look-elsewhere, BF<1, worsening); w₀ branch-shopping flagged (canonical 2.13σ honest vs derivation-inadmissible branch-iv 0.731σ); m_H +38.5σ with a filter-independence theorem blocking a 5-trial penalty; the 10 blind-cross-axis STAGE-3 promotions as the structural-UP driver (joint BF 25–55, structurally-independent per Stage-2 PASS-AND). **Recomposition finding:** structural evidence UP, observational evidence DOWN, headline probability near the ~22% S69 anchor — the *composition* shifted toward publishable mathematics + lab/JUNO falsifiers and away from CMB-cosmology fit. Closes the standing atlas-08 Q44.

**What changed (`output-standards.md` numerical-vs-structural split):**

- *(a) Numerical revisions:* S8_FW=0.8128 (in-band, band-pos 0.75); M_max=0.1631 M_⊙, Δ/μ=4.82; DESI-5yr bind 1.001σ @ z=0.5; n_s liability quantified at 4.73σ post-look-elsewhere.
- *(b) Structural changes:* finite-μ CFL corridor `untested` → **CLOSED-at-this-construction** (pairing direction transfers, EoS-stiffness does not); f·σ8(z) `static σ8 coincidence` → **LIVE near-term LSS-flagship falsifier**; framework evidence `frozen since S66 W2-A` → **RECOMPOSED** (structural-up / observational-down, formalized with elicited per-observable BFs).

## Carry-Forward Computations

### CF-INV13-W2-1-FINITE-MU-REFINE — finite-μ CFL EoS refinement (self-consistent μ_eff)

| Field | Spec |
|:------|:-----|
| **What** | Re-run the finite-μ CFL gate with a self-consistent μ_eff (μ adjusted WITH density rather than a fixed floor-relative scan) + a physical pairing-window narrowing forcing Δ/μ → O(0.1); test whether the EoS stiffens M_max into [2.0, 2.6] M_⊙ WITHOUT post-hoc tuning. Re-opens the S38-CLOSED "finite-density spectral action (P2b)" / S25-Goal-7 self-consistent-μ_eff item that THIS gate's machinery revived. |
| **Inputs** | `computations/investigation-13/inv13_w2_1_finite_mu_cfl_eos.npz` (the W2-1 μ-scan + g-calibration χ_ref); `bdg_spectral_triple.py` / `dirac_spectrum.py`; canonical `M_KK`, `Delta_BCS` (R-PROTECTED 0.4642547); the L_max=10 D_K cache. |
| **Gate** | M_max_FW ∈ [2.0, 2.6] M_⊙ (the 2 M_⊙-pulsar band) AND Δ/μ ~ O(0.1) at the dense plateau (physical CFL window), with `sign_verdict=PASS` retained. INFO if qualitatively stiffer but un-banded; FAIL if the runaway Δ/μ persists. |
| **Effort** | ~3 wave-equivalents (a self-consistent μ_eff solver loop wrapping the existing GPU gap-solve; the gap machinery already exists, the new cost is the density-coupled outer iteration). |

**Session-track promotions** (route to `/rclab-investigate --investigation 13` close as housekeeping-ledger lift candidates — investigation-track-boundary actions NOT effected here, `gate-verdicts.md §"Investigation-Track Canonical Path"`): W2-2 PASS → LSS-flagship falsifier-master-inventory row (mack sole-writer) with explicit DESI/Euclid σ-distances; W2-3 LANDED → EVOI Tier-table re-anchor (rewrite `evoi-framework.md` §1–§4 with the elicited per-observable P(pass) BFs + currency bump) + mack + Sagan co-dispatch on the observational-surface rows; closes atlas-08 Q44.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-17 | finite-μ CFL-on-SU(3) → dense-matter EoS | S38-CLOSED "no formalism" / S25-Goal-7 OPEN | **FAIL — corridor CLOSED at this construction; item RE-OPENED** (INV13-W2-1) | sign=PASS (dΔ_CFL/dμ>0, VH-frac 1.000) but M_max=0.1631 M_⊙ ≪ 2 M_⊙; runaway Δ/μ=4.82; pairing direction transfers, EoS-stiffness does not |
| 2026-06-17 | f·σ8(z) GGE growth-suppression / S8 | static σ8=0.799 coincidence | **PASS — quantitative z-dependent prediction; LIVE LSS flagship** (INV13-W2-2) | S8_FW=0.8128 in-band, sign 16/16 neg, DESI/Euclid-bindable; GW flagship retired S96 → LSS now the live near-term falsifier |
| 2026-06-17 | framework evidence composition (post-S66) | EVOI ordinal proxies frozen since S66 W2-A; atlas-08 Q44 standing | **RECOMPOSED — structural-up / observational-down; headline ~22%** (INV13-W2-3 review) | elicited per-observable BFs; n_s 4.73σ liability; 10 blind STAGE-3 structural-UP driver; composition shifted to math + lab/JUNO falsifiers |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Deliverable md | Verdict |
|:-----|:-------|:------------|:------------|:---------------|:--------|
| INV13-W2-1 | `inv13_w2_1_finite_mu_cfl_eos.py` (41.8 KB) | `…_eos.npz` (13.1 KB) | `…_eos.png` (124.6 KB) | — | FAIL (sign=PASS) |
| INV13-W2-2 | `inv13_w2_2_fsigma8_growth_s8.py` (37.5 KB) | `…_s8.npz` (21.6 KB) | `…_s8.png` (152.3 KB) | — | PASS |
| INV13-W2-3 | — (review gate) | — | — | `investigation-13-bayesian-reanchor-synthesis.md` (19.6 KB) | LANDED (no verdict line) |

Compute verdicts in `computations/investigation-13/inv13_gate_verdicts.txt` (dual-SHA, sig_5 unique; W2-1 carries the [SIGN] 3-tuple companion row). W2-3 closes by artifact-existence-with-content.
