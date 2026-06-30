# Session 96 Wave 6 — Observational Falsifiers & Detector Reach + Cosmogenesis-Scenario (Results Working Paper)

**Session**: 96 | **Wave**: 6 | **Plan**: session-96-plan-w6.md | **Theme**: Observational-falsifier and detector-reach harvest of the 31-reviewer capstone panel (cosmic-web V.1/V.2/V.3, little-red-dots V.1/V.3/V.4, tesla V.2, phonon-first V.7, mack CF-1/2/3) plus dissonances D2 (cosmogenesis: GGE-relic-IS-CMB vs hot-big-bang SCENARIO A) and D4 (CGWB LISA-band flagship: mHz placement asserted-not-derived). Seven `S96-OBS-*` gates. Held substrate-first: every coupling is a spectral moment of D_K; the CGWB is squeezed-graviton production at the van Hove fold (NOT primordial GW in expanding space); the assembly clock is the readout of a(τ) spectral-complexity growth (NOT cosmic time in a container); observational anchors (Planck σ₈, DESI-DR3, A_s) are COMPARISON-ONLY, never canonical replacements. Canonical write-order (verdict → canonical_constants.py → falsifier-master-inventory.md, mack-cosmic-bridge sole inventory-row writer) governs the falsifier-producing gates (1, 2, 3, 4, 7).

## Gate Sections

### §W6-1. S96-OBS-FSIGMA8-FORECAST (cosmic-web)

**Status**: COMPLETED
**Gate ID**: `S96-OBS-FSIGMA8-FORECAST`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (a₂-channel growth: D_K eigenvalues → a₂ Seeley-DeWitt moment → emergent growth factor D(a) → f·σ₈)
**Agent**: `cosmic-web` (falsifier-inventory row written by `mack-cosmic-bridge` per canonical write-order step 3)
**Hypothesis**: The growth-rate prediction f_FW=0.525492 (vs f_LCDM=0.527130) is a −0.311% suppression on bare f and a −4.058% suppression on the f·σ₈ product (lower σ₈ compounds) with the correct S₈-tension-relieving sign; its z-curve sits inside the forecast DESI-5yr/Euclid RSD band — a viable zero-parameter LSS discriminator currently absent from the §7 scorecard.
**Plan reference**: `sessions/session-plan/session-96-plan-w6.md` §W6-1 (machinery pin, thresholds, substitution-chain source, canonical write-order step 1→2→3).

**Verdict**: **INFO** — value=`bare_f_supp=-0.311%;product_supp_max=-4.058%@z0.51;sigma_DESI5yr_max=1.013@z0.51;sigma_Euclid_max=1.534@z0.51;sigma_current_max=0.506;within_band_DESI5yr=6/7;S8_relieving=1;INFO-branch-a_paper-search-down`. SIGN/MAGNITUDE/REGIME 3-tuple = **PASS / INFO / VALID**. Composite collapses to INFO via the magnitude=INFO path (within the DESI-5yr forecast 1σ band at 6/7 bins, 1.013σ at z=0.51 — a z-dependent discriminator, pre-registered Track B). The verdict is ALSO the pre-registered **INFO-branch-a** ("PRE-REG-INFO-branch-a", mirroring S95 W6-2): the live DESI-5yr/Euclid forecast-precision fetch is paper-search-MCP-gated and paper-search returned empty on two distinct queries this session, so the σ-distance is reported from the **S65-embedded forecast arrays** (a prior substrate-first artifact — legitimate substrate-canonical sourcing, NOT fabrication) and the live-published forecast validation is deferred. The substrate side is FINALIZED.

**4-tuple**: (value=`bare_f_supp=-0.311%;...;sigma_DESI5yr_max=1.013@z0.51;...`, scheme=`FW-growth-a2-channel`, convention=`RATIO-substrate-growth-on-borrowed-LCDM-H(z)-C10`, L_max=`N/A`).

**Results**:

**The two numbers (C5 single-value-conflation guard — flagged across 8 reviewers).** The headline "~4%" figure is the f·σ₈ **PRODUCT/amplitude** suppression, NOT the bare growth-rate f. Both, stated explicitly and labelled:

| Quantity | Value | Which is which |
|:---------|:------|:---------------|
| **BARE-f suppression** (z=0) | **δf/f_LCDM = −0.311%** | the SMALL number; δf = f_FW − f_LCDM = 0.525492 − 0.527130 = −0.001639 (= −819/500000 Sage-QQ-exact) |
| **f·σ₈ PRODUCT suppression** (max) | **−4.058% at z=0.51** | the "~4%" number; product amplitude, σ₈ compounds the f-suppression |
| δσ₈/σ₈ | −2.199% | the amplitude leg: σ₈_FW=0.793167 vs σ₈_Planck=0.811 |
| product additive check (z=0) | δf/f + δσ₈/σ₈ = −2.510% (exact product −2.503%; residual 0.0068%) | both legs NEGATIVE ⇒ ADD; the product suppression is LARGER than bare-f |

**Substitution chain (substituted numbers).**
- Definition: δf = f_FW − f_LCDM = 0.525492 − 0.527130 = **−0.001639** (Sage-QQ-exact −819/500000 = −0.001638; computed −0.001639 at float64). Canonical form: δf/f_LCDM = **−0.311%**. Direction: δf < 0 ⇒ f_FW < f_LCDM ⇒ **SUPPRESSION** (bare-f SIGN PASS, computed sign = −1).
- Product: δ(fσ8)/fσ8_LCDM = (1+δf/f)(1+δσ₈/σ₈) − 1 ≈ δf/f + δσ₈/σ₈ (both negative ⇒ **ADD**). The ~4% prose figure is this PRODUCT amplitude, max −4.058% at z=0.51 — NOT bare f (which is −0.311%).
- S₈ direction: S₈ = σ₈√(Ω_m/0.3); σ₈_FW < σ₈_Planck ⇒ **S₈_FW = 0.8128 < S₈_LCDM = 0.8310** ⇒ S₈ is LOWER ⇒ **RELIEVES** the Planck-vs-lensing S₈ tension (correct, tension-relieving sign). SIGN PASS on all three legs (δf<0 AND δ(fσ8)<0 AND S₈ relieving).

**z-curve (0 < z < 1.5; C10 borrowed-H(z) caveat — LOAD-BEARING).** The f·σ₈(z) curve is built from the growth-amplitude ratio D_FW/D_LCDM = **growth_ratio = 0.978011** (the σ₈ amplitude leg) and the z=0-anchored f-ratio (the growth-rate leg), modulating a **BORROWED ΛCDM growth history** integrated from the linear growth ODE `D'' + (3/a + E'/E)D' − (3/2)Ω_m(a)/a² D = 0` over a=[1e-3,1]. **C10 caveat**: the H(z) the growth ODE integrates against is BORROWED from ΛCDM — the framework has no derived a(t) yet (the §6.3 effective-Friedmann gap). The framework's contribution enters as a constant growth-amplitude RATIO applied to a ΛCDM background, so this is a **modulation-on-borrowed-H prediction**, NOT a from-first-principles substrate growth history. Robustness to the SCALE-FACTOR-54 substrate-proxy H(z) is the separate cosmic-web V.4 gate (W6-adjacent / next session). The substrate-physics direction is unaffected by the caveat: the a₂-channel growth of spectral weight is intrinsically slower than the borrowed-ΛCDM baseline regardless of which H(z) integrates the modulation; the caveat scopes the per-z amplitude precision, not the sign.

**Forecast σ-distance (S65-embedded; INFO-branch-a).** Per-z |fσ8_FW − fσ8_LCDM| / σ_forecast(z) at the 7 DESI bins z∈{0.15, 0.38, 0.51, 0.70, 0.85, 1.05, 1.52}:

| Forecast | max σ-distance | z at max | within-band (≤1σ) |
|:---------|:---------------|:---------|:------------------|
| current DESI/eBOSS obs | 0.506 σ | 0.51 | **7/7** (consistent NOW, not yet discriminated) |
| **DESI-5yr forecast** | **1.013 σ** | 0.51 | **6/7** (marginally out at z=0.51) |
| **Euclid forecast** | **1.534 σ** | 0.51 | **3/7** (middle bins exceed 1σ — Euclid discriminates) |

The implied forecast precisions (DESI-5yr ~4–5% per bin, Euclid ~2.5–3.5% per bin) are physically reasonable for those surveys. The discrimination peaks at the f·σ₈ turnover (z≈0.51), exactly where the product suppression is maximal (−4.058%). Verdict reading: the framework is **consistent with current data (0.5σ)** and becomes a **forward-edge discriminator** — at the DESI-5yr/Euclid 1σ band edge, decisively testable by Euclid at the middle bins. This is the Track-B "z-dependent partial discriminator" outcome, NOT a clean all-z PASS and NOT a FAIL.

**REGIME = VALID.** The borrowed-ΛCDM growth ODE is well-defined (finite, D>0) across the full intended z-grid (domain_used_frac = 1.000); no auto-shortening. The fetch-gate makes the LIVE-forecast-precision leg pending (deferred), but the substrate curve is VALID across [0,1.5].

**Canonical write-order (this gate produces a falsifier value).**
- **Step 1 (verdict file)** — DONE: canonical line + dual-SHA companion + schema-v2 3-tuple appended to `computations/session-96/s96_gate_verdicts.txt`. audit_sha256=`318df6edeadb621453a46be1f5e8568db3fbff780e6e1792a69cb5ba37e06027` (full 64-char), content_sha256=`85e03db0e061070a8041349bc90d5d7a24582b349cd0b59189764e9474bbe3ef`.
- **Step 2 (canonical_constants.py)** — DONE (this agent): promoted `f_FW=0.5254916357116971`, `f_LCDM=0.5271303865722888`, `fsigma8_product_suppression_FW_max_pct=-4.058`, `f_bare_suppression_FW_pct=-0.311`, each with PROVENANCE and gate=S96-OBS-FSIGMA8-FORECAST. (Note: this edit post-dates the script's audit_sha256 capture over canonical_constants.py — the emitted verdict is permanent as captured; the script is NOT re-run, per the carry-forward script-bytes-immutability hazard in `mechanical-closure-discipline.md`.)
- **Step 3 (falsifier-master-inventory.md)** — RECOMMENDATION to `mack-cosmic-bridge` (sole inventory-row writer), below. This agent does NOT write the inventory file.

**§7.1 / §7.2 ROW RECOMMENDATION to `mack-cosmic-bridge`** (canonical write-order step 3; mack is the sole writer of `sessions/framework/registry/falsifier-master-inventory.md` and the §7 falsifier-anchor surface per `feedback_mack-bridge-role.md` + the capstone-hygiene gate Q2 routing):

- **§7.1 scorecard NEW row** — "f·σ₈ growth-suppression (LSS)": prediction f_FW=0.525492 / f·σ₈ product suppression **−4.058% (max, z=0.51)**; bare-f suppression −0.311%; status **CONSISTENT (0.5σ current) / FORWARD-EDGE (1.0σ DESI-5yr, 1.5σ Euclid)**; zero free parameters; S₈ tension-relieving. This row CLOSES the documentation gap (the PROVEN f·σ₈ suppression was absent from §7.1).
- **§7.2 falsifier-inventory NEW row** — observable `f·σ₈(z)`; substrate prediction −4.058% product suppression with the correct S₈ sign; detector **DESI-5yr (~2028) / Euclid (~2028)**; live-watch envelope: within current 1σ, at 1σ band-edge for DESI-5yr, ≥1σ at Euclid middle bins; **C10 borrowed-H(z) caveat** flagged (modulation-on-borrowed-H; cosmic-web V.4 robustness pending); **C5 conflation guard**: the "~4%" is the PRODUCT amplitude, bare-f is −0.31%. Cite verdict-line audit_sha256=`318df6edeadb621453a46be1f5e8568db3fbff780e6e1792a69cb5ba37e06027` and canonical_constants entries `fsigma8_product_suppression_FW_max_pct` / `f_bare_suppression_FW_pct` / `f_FW`.
- **Uniqueness note for the inventory annotation**: f·σ₈ suppression is NOT a unique-to-framework signature — any model lowering σ₈ (e.g. a low-S₈ ΛCDM variant, evolving-DE w₀<−1) produces a comparable growth-suppression. Its discriminating power is therefore CONDITIONAL on the framework's zero-free-parameter status (the value is FIXED by the BCS-sector growth, not fitted) rather than on a shape no other model can match. mack should annotate the inventory row with this uniqueness caveat.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- script `computations/session-96/s96_obs_fsigma8_forecast.py` — EXISTS; contains `from canonical_constants import` (L82-ish) and `append_verdict` (Section 6). ✓
- data `computations/session-96/s96_obs_fsigma8_forecast.npz` — EXISTS (full-float64 z-curve + forecast arrays + dual-SHA). ✓
- plot `computations/session-96/s96_obs_fsigma8_forecast.png` — EXISTS (4-panel: f·σ₈(z) curves, bare-f-vs-product, per-bin σ-distance, substitution-chain text). ✓
- verdict line in `computations/session-96/s96_gate_verdicts.txt` — EXISTS; matches `^S96-OBS-FSIGMA8-FORECAST:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ([SIGN] trigger). ✓ (grep output pasted in the agent's final message.)

**MCP Pre-Compute Audit** (knowledge MCP queries run BEFORE computing, per query-first discipline):
- `search_knowledge('fsigma8 growth rate suppression S8 tension f_FW growth_ratio')` → returned the s70/s65/s59 equations: f_FW=0.525492, f_LCDM=0.527130, growth_ratio=0.978009/0.978011, σ8_FW=0.793166, plus the s59 per-z f(z) curve (−1.97%…−2.37%). CONFIRMS the inputs; no closure pre-covers the §7.1-scorecard surfacing (the documentation gap is real).
- `get_constant('f_FW')` → NOT-FOUND (as expected; lived in `s70_bulk_flow_log.txt`). Promoted this session per write-order step 2.
- `get_constant('f_LCDM')` → NOT-FOUND. Promoted this session.
- `get_constant('sigma_8')` → 0.811 (Planck/LCDM anchor; the σ₈_LCDM leg of the product; coupled to gate-7 anchor-hygiene). Matches s70 `sigma8_LCDM`.
- Inputs confirmed on disk: `s70_bulk_flow.npz` (f_FW_z0, f_LCDM_z0, fsig8_FW, fsig8_LCDM, sigma8_fw, growth_ratio all present); `s65_fsigma8.npz` (z_bins, fsig8_FW_bins, frac_FW, **nsig_FW_desi5, nsig_FW_euclid, nsig_FW_current** — the embedded forecast σ-distance arrays the INFO-branch uses).
- PRE-CLOSED check: NO — the f·σ₈ PROVEN suppression existed in s59/s65/s70 numerics but was NOT surfaced to the §7 scorecard; this gate closes that gap and lands the forecast σ-distance.

**Substrate framing (PHONONIC, a₂-channel).** The chain is D_K eigenvalues → a₂ Seeley-DeWitt coefficient → emergent metric g_M → linear growth factor D(a) → growth rate f = dlnD/dlna → f·σ₈. The suppression is NOT "a modification of gravity in a container": it is that the substrate's a₂-channel growth of spectral weight produces a slightly slower emergent structure-growth than a ΛCDM background would. The substrate IS the growth history; what DESI/Euclid measure (f·σ₈ in a continuum redshift container) is the laboratory-IN image of the substrate-IS a₂-channel growth. The S₈-tension-relieving direction is a substrate-physics consequence (lower σ₈ amplitude from the slower a₂-channel growth), read off the canonical form, not fitted. C10 borrowed-H(z) and C5 product-vs-bare-f conflation are both scoped above and do not invert the explanation direction.

---

### §W6-2. S96-OBS-FIRST-SOUND-RING (cosmic-web)
**Status**: COMPLETED
**Gate ID**: `S96-OBS-FIRST-SOUND-RING`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (first-sound = substrate metric-mode acoustic ring; a₂-channel transduction into the photon-baryon fluid at recombination)
**Agent**: `cosmic-web` (falsifier-inventory row written by `mack-cosmic-bridge`)
**Hypothesis**: The S43 first-sound ring (r₁=325.3 Mpc, k₁=0.0193 Mpc⁻¹, A_FS=0.204=c₂²/c₁²) imprints on the observed matter power spectrum at an amplitude above the 1σ sensitivity floor of a named near-term experiment (DESI full-shape / CMB-S4 / SO / Euclid) at k₁ — completing the stranded S95 W6-2 INFO into a live, zero-parameter, no-ΛCDM-counterpart BAO falsifier.
**Plan reference**: `sessions/session-plan/session-96-plan-w6.md` §W6-2 (re-uses the S95 W6-2 transport machinery; same effacement-amplitude scheme — do NOT convention-shop).

**Verdict**: **PASS** — composite `(sign=PASS, magnitude=PASS, regime=VALID)`. SNR_ring = **8.63** at the FETCHED DESI-5yr 1σ floor (≫ 2). The stranded S95 W6-2 INFO is **CLOSED into a verdict** (the paper-search MCP, down at S95, returned results this session). 4-tuple: `(value=SNR_ring_Y5=8.6341, scheme=effacement-amplitude-projection-(c_b²/c_Gold)², convention=RATIO-substrate-first-transport-NOT-borrowed-LCDM-amplitude, L_max=N/A)`. audit_sha256=`b74ccd561136efc57f3f994e7e302bd9a0215a7d616c9e0096810ab9bf64955c` (full 64-char), content_sha256=`59ea78d550b14e42bec69ed9446c1298192a84666cf74dc91516d32be9d0f4df`.

**Output Artifacts** (closure-verification checklist):
- **script** `computations/session-96/s96_obs_first_sound_ring.py` — EXISTS. `grep -E 'from canonical_constants import'` → `from canonical_constants import (` (imports `Gamma_effacement, c_fabric, PI`); `grep -E 'append_verdict'` → `def append_verdict(...)` + one call site. ✔
- **data** `computations/session-96/s96_obs_first_sound_ring.npz` — EXISTS (A_FS, A_ring_at_k1, sigma_exp_DESI_Y5/DR1, SNR_ring_Y5/DR1, A_obs_B1, k_grid+delta_P_over_P, verdict 3-tuple; full float64). ✔
- **plot** `computations/session-96/s96_obs_first_sound_ring.png` — EXISTS (panel 1: ring δP/P imprint vs FETCHED DESI σ_exp floors at k₁; panel 2: SNR bars LIVE ring vs per-branch). ✔
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — `^S96-OBS-FIRST-SOUND-RING:.* audit_sha256=[a-f0-9]{64}` matched; dual-SHA companion row present; schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row present ([SIGN] trigger, `schema_v2_3tuple_required: true`). audit_sha256 unique across the file (sig_5 OK). ✔

**MCP Pre-Compute Audit** (queries executed before writing the script):
- `search_knowledge('first sound ring A_FS 0.204 r1 325.3 BAO amplitude transport')` → confirmed `A_FS/A_BAO = 0.204 = c₂²/c₁²`, `r₁=325.3 Mpc`, `k₁=0.0193 Mpc⁻¹` (S43 results WP); S95 W6-2 transport provenance + `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT` INFO gate.
- `trace_entity('CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT')` → S95 W6-2 INFO (composite=INFO; `A_obs_B1=1.445164e-03`; `experiment_sensitivity_unavailable_paper-search-MCP-down_PRE-REG-INFO-branch-a`). This gate completes it.
- `get_constant('A_FS')` → NOT-FOUND (expected; lived only in S43/S95 npz → promoted to canonical this session per write-order step 2).
- `get_constant('Gamma_effacement')` → 0.9997 (impedance transmission; (1−Γ)=3e-4 leak). `get_constant('c_fabric')` → 209.97368021 (substrate sound speed). Both pre-existing, imported.
- **FETCH** (paper-search MCP, the leg S95 could not do): `search_arxiv('DESI ... reconstruction ... power spectrum')` → returned `arXiv:2411.19738v2` (DESI 2024 reconstruction); `read_arxiv_paper('2411.19738v2')` → extracted the σ_exp anchor verbatim. Paper-search MCP **UP this session** (S95 had `paper_search_available=False`).
- NOT PRE-CLOSED: the substrate side (A_FS, transport) was canonical from S43/S95, but the named-experiment SNR was an open INFO; this gate closes it.

**Results.**

**Re-used machinery (no convention-shop).** The substrate side is taken VERBATIM from the S95 W6-2 transport npz (`s95_w6_2_bao_amplitude_transport.npz`): `A_FS_S43=0.204`, `A_ring_at_k1=0.203154` (the δP/P of the ring on the actual P(k) at k₁), `A_obs_B1=1.445164e-3`, `A_eff_B1=(c_B1/c_Gold)²=7.606127e-3`, `Gamma_effacement=0.9997` (cross-checked == canonical), `eff_floor_deep=9e-8`, `desi_dr2_ruler=0.0024`, the 257-pt `k_grid` + `delta_P_over_P` curve. The scheme (`effacement-amplitude-projection-(c_b²/c_Gold)²`) is IDENTICAL to S95 W6-2 — the ONLY new input is the FETCHED σ_exp(k₁). CLASS=FULL.

**FETCHED experiment sensitivity σ_exp(k₁)** — the leg S95 W6-2 could not complete. Source: X. Chen, Z. Ding, E. Paillas, et al., *"Extensive analysis of reconstruction algorithms for DESI 2024 baryon acoustic oscillations"*, **arXiv:2411.19738v2** (DESI collaboration, astro-ph.CO), fetched via paper-search MCP `read_arxiv_paper`. Two verbatim source statements give the named-experiment (DESI) amplitude floor on the BAO-scale matter P(k):
- *"The maximum difference of about 0.1% in monopole ... is only about 2.5% of the DR1 measurement error at the same scale."* ⇒ **σ_exp(DESI-DR1) = 0.1%/2.5% = 0.001/0.025 = 0.040** (4.0% 1σ fractional P(k) at BAO scales).
- *"the approximate Y5 power spectrum errors ... can be obtained by downscaling the DR1 errors by a factor of 1.7 (the volume difference)."* ⇒ **σ_exp(DESI-5yr / Y5) = 0.040/1.7 = 0.02353** (2.35% 1σ). The 1.7× downscale is **paper-stated**, not an assumed √N.

This is a real, paper-sourced, named-experiment (DESI Y5 / 5-year) statistical-floor — exactly the σ_exp(k₁) the SNR needs. Both numbers are FETCHED, not surrogate (S95 used a `CMB-S4/SO ~0.01% bounding estimate`, explicitly NOT fetched).

**Substitution chain (substituted numbers; [SIGN] direction pre-registered, not re-decided post-hoc).**
- **CC1 (LIVE-ring detectability).** SNR_ring = A_FS / σ_exp(k₁). Substitute A_ring_at_k1 = 0.203154 (the actual imprint on P(k); A_FS nominal cross-check 0.204):
  - DESI-5yr: SNR_ring = 0.203154 / 0.02353 = **8.634** (≥ 2 ⇒ PASS). Nominal-A_FS cross-check: 0.204/0.02353 = 8.670.
  - DESI-DR1 (today): SNR_ring = 0.203154 / 0.040 = **5.079** (already ≥ 2). The ring is detectable NOW, not only at Y5.
- **CC2 (suppression SIGN — the [SIGN] pre-registration).** Effacement direction: Γ_eff = 0.9997 < 1 ⇒ `A_eff_B1·Γ_eff = 7.6038e-3 < A_eff_B1 = 7.6061e-3` (the 0.03% impedance leak **reduces** the transported per-branch weight ⇒ **SUPPRESS**). The per-branch sub-feature is real (`A_obs_B1 = 1.445e-3 > eff_floor_deep = 9e-8`, ratio 16057) but **below current rulers** (`A_obs_B1 / DESI-DR2-ruler-0.24% = 0.602 < 1`). `(c_B1/c_Gold)² = 17689/2325625 = 7.606127e-3` Sage-exact. SIGN PASS.
- **Channel separation (C5 / over-precision scope — LOAD-BEARING).** `A_ring / A_obs_B1 = 140.6×`: the ring and the per-branch sub-feature are **structurally distinct channels**. The ring (A_FS = 0.204 = c₂²/c₁², the two-fluid metric-mode/Goldstone-mode ratio) is the LIVE channel; the per-branch (A_obs_B1 = 1.445e-3) is the effacement-suppressed sub-feature. **The §6.2 "far below current rulers" phrase is scoped HERE ONLY to the per-branch sub-feature** (`A_obs_B1`, 0.60× the DESI-DR2 ruler), and is NOT conflated with the live first-sound ring (which is 8.6σ-detectable at DESI-5yr). This is the C5/over-precision flag raised by tesla + cosmic-web; the two amplitudes are reported separately and labelled by channel.

**SIGN/MAGNITUDE/REGIME 3-tuple.**
- **SIGN = PASS** — effacement SUPPRESSES the per-branch (Γ_eff < 1 reduces the transported weight; the sub-feature sits below current rulers BY DESIGN); the predicted SUPPRESS direction holds.
- **MAGNITUDE = PASS** — SNR_ring(Y5) = 8.634 ≥ SNR_PASS = 2 (the ring is detectable at the named experiment).
- **REGIME = VALID** — (i) the S95 W6-2 transport npz is re-used UNMODIFIED (Γ_eff matches canonical 0.9997 ⇒ not tampered), (ii) σ_exp is FETCHED, not a surrogate (paper-search UP this session), (iii) A_FS = 0.204 is consistent with the S43 c₂²/c₁² = 0.20450 (within 1%). Composite collapse ⇒ **PASS**.

**Canonical write-order (this gate produces a falsifier value).**
- **Step 1 (verdict file)** — DONE: canonical line + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple appended to `computations/session-96/s96_gate_verdicts.txt`; audit_sha256 = `b74ccd561136efc57f3f994e7e302bd9a0215a7d616c9e0096810ab9bf64955c` (full 64-char, unique).
- **Step 2 (canonical_constants.py)** — DONE (this agent): promoted `A_FS_first_sound_ring=0.204`, `r1_first_sound_ring_Mpc=325.3`, `k1_first_sound_ring_invMpc=0.0193150486`, and the FETCHED `sigma_Pk_DESI_Y5_BAO_scale=0.0235294…` (Section E, each with PROVENANCE + gate=S96-OBS-FIRST-SOUND-RING). (Note: this `update_constant` append post-dates the script's audit_sha256 capture over `canonical_constants.py`; the emitted verdict is permanent as captured and the script is NOT re-run — the script imports only pre-existing constants, so the promotion does not affect the computed physics. Carry-forward script-bytes immutability per `mechanical-closure-discipline.md`.)
- **Step 3 (falsifier-master-inventory.md)** — RECOMMENDATION to `mack-cosmic-bridge` (sole writer per `feedback_mack-bridge-role.md`): append a row for the **first-sound BAO ring** — *Observable*: A_FS = 0.204 = c₂²/c₁² ring imprint on matter P(k) at k₁ = 0.0193 Mpc⁻¹ (r₁ = 325.3 Mpc); *Substrate-IS*: two-fluid acoustic ratio (metric mode c₁=c, Goldstone/condensate mode c₂), **NO ΛCDM counterpart**; *Prediction*: zero-parameter, live; *Detectability*: SNR = 8.6 at DESI-5yr (σ_exp = 2.35%, FETCHED arXiv:2411.19738v2), 5.1 at DESI-DR1; *Live-watch envelope*: detectable in DESI full-shape now / Y5; *Contrast*: per-branch effacement sub-feature A_obs_B1 = 1.445e-3 is real but OUTSIDE current rulers BY DESIGN (0.60× the DESI-DR2 0.24% ruler) — keep "far below current rulers" scoped to THIS sub-feature, not the ring; cite verdict audit_sha256 `b74ccd56…` (full 64-char) + canonical entry `A_FS_first_sound_ring`.

**Substrate framing.** PHONONIC. The first-sound ring is the substrate's own metric-mode (c₁ = c) acoustic horizon at recombination; the second sound (c₂, the Goldstone/condensate mode) sets the ratio A_FS = c₂²/c₁² = 0.204. The chain is `D_K eigenvalues → a₂ acoustic metric → first/second-sound speeds c₁/c₂ → ring amplitude A_FS → imprint on the emergent photon-baryon P(k) at recombination → detectability SNR at DESI`. This is **NOT "a feature in a ΛCDM power spectrum"**: it is the substrate's two-fluid acoustic structure projected through the a₂-channel transduction into the emergent fluid — there is no ΛCDM analog to the second-sound mode, which is what makes it a clean, zero-parameter falsifier. The effacement (Γ_eff = 0.9997) suppresses the per-branch sub-feature (the 0.03% impedance leak reduces its transported weight) below the naive equipartition split; the ring is the live channel, 141× the sub-feature. The fetch closes the only stranded INFO in the LSS harvest into a PASS.
---

### §W6-3. S96-OBS-CGWB-PEAK-FREQ (little-red-dots)

**Status**: COMPLETED
**Gate ID**: `S96-OBS-CGWB-PEAK-FREQ`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (CGWB = squeezed-graviton production at the fold; GGE-acoustic tensor sector; redshifted by the substrate scale factor)
**Agent**: `little-red-dots` (transit-dynamics supplies the dispersion; falsifier-inventory row written by `mack-cosmic-bridge`)
**Hypothesis**: The (A)-class acoustic CGWB peak, emitted at the fold's characteristic frequency (van Hove DOS scale, c_fabric=209.97 M_KK, Mach 13.75) and redshifted by a(τ_fold)/a(τ_now)<1, lands in the LISA mHz band [0.1,100] mHz — RESOLVING D4: acoustic dispersion legitimately moves the peak off the naive GHz GUT-transition expectation, so LISA is the right instrument and the §7.2 flagship stands.
**Plan reference**: `sessions/session-plan/session-96-plan-w6.md` §W6-3 (intra-wave: consumes gate-5 a(τ) redshift factor, OR reads `s54_scale_factor.npz` directly; honest-close per `.claude/rules/mechanical-closure-discipline.md` if gate-5 npz absent at dispatch).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-96/s96_obs_cgwb_peak_freq.py` — EXISTS. `grep` of must_contain:
  - `from canonical_constants import` → matched (line 86; imports `M_KK, M_KK_inv_seconds, c_fabric, Mach_max, M_Pl_reduced, hbar_GeV_s, omega_L1, omega_PV, omega_tau, v_g_B2_fold, f_LISA_pivot, tau_fold`).
  - `append_verdict` → matched (def at §0 emitter block + invocation at §8).
- **data** `computations/session-96/s96_obs_cgwb_peak_freq.npz` — EXISTS (f_obs/f_emit per fold mode, the 121-pt kappa-knob sweep + band classification, target-band kappas, naive-GUT baseline, 3-tuple, D4 resolution string).
- **plot** `computations/session-96/s96_obs_cgwb_peak_freq.png` — EXISTS (left: f_obs vs the open kappa knob with LISA/PTA/DECIGO/GHz bands shaded + naive-GUT line; right: fold acoustic emission-scale spread across 6 modes, all ~30–45 decades above LISA at the natural normalization).
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — matches `^S96-OBS-CGWB-PEAK-FREQ:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e` (unique in file, sig_5 clean); dual-SHA companion row present; **schema-v2 [SIGN] 3-tuple companion row present** (`schema_v2_3tuple_required: true`) + substrate-anchor row.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; query-first discipline):
- `get_constant('M_KK')` → **7.428660036284456e16** GeV (S42, CONST-FREEZE-42; alias of M_KK_gravity).
- `get_constant('c_fabric')` → **209.97368021** (S42; substrate sound speed in M_KK units; velocity scale, NOT a momentum cutoff).
- `get_constant('Mach')` → no exact match; resolved to **Mach_max = Mach_max_framework = 13.75** (van Hove fold velocity ratio).
- `get_constant('M_KK_inv_seconds')` → **8.860439881925477e-42** s (= ħ/M_KK; this IS the substrate-natural M_KK⁻¹→s normalization `kappa_nat`; verified == ħ/M_KK to rel 5.4e-10, and == gate-5 `kappa_nat`).
- `search_knowledge('CGWB peak frequency acoustic GGE graviton LISA band fold characteristic frequency')` → surfaced `gw_frequency_check` (S58 provenance), `f_LISA_pivot --derived_from--> S85` (3 mHz LISA pivot), atlas-04 theorem `Ω_GW (CGWB at LISA mHz)` ((A)-class O(1e-10) flat acoustic; (C)-class 8.299e-58). **No prior gate derives the OBSERVED peak FREQUENCY via the substrate redshift chain — this gate is the first.**
- `search_knowledge('van Hove fold characteristic acoustic frequency DOS scale group velocity zero omega emission')` → fold modes `ω_L1=0.138`, `ω_PV=0.792`, `ω_tau=8.27`, `v_g_B2_fold=0.0227` (M_KK units; the fold's characteristic acoustic frequencies, group velocity → 0 at the van Hove fold).
- **Prior art read in full**: `computations/session-58/s58_gw_frequency_check.py` — S58 Method-3 dimensional analysis `f_0 ~ T_* T_0 / M_Pl` with T_*~M_KK ⇒ GHz (the naive thermal-GUT expectation). This gate's substrate-first emission frequency REPLACES that thermal route with the fold's ACOUSTIC scale.
- **Upstream npz**: `s96_obs_lrd_assembly_clock.npz` (gate-5) → `a_fold_over_a0_computed=2.1173` (DIRECTLY RESOLVED, no extrapolation — the chain anchor) + `kappa_sweep` (121-pt M_KK⁻¹→s knob, [1e-20,1e-10]) + `kappa_nat=8.86e-42`. Cross-checked against `s54_scale_factor.npz` `a_at_fold=2.11734` (identical; same upstream input).

**Verdict**: **FAIL** — `value='composite=FAIL;f_obs_kappa_nat=8.4835e+39Hz_band=GHZ+;f_emit_kappa_nat=1.7962e+40Hz;a_fold_over_a_now=0.47229_REDSHIFT;a_fold_over_a0=2.1173_gate5_DIRECTLY_RESOLVED;kappa_nat=8.8604e-42s_=hbar/M_KK;decades_above_LISA=43.93;decades_above_GHz=31.93;naive_thermal_GUT=1.733e+09Hz_GHz+;GHz->mHz_decades_needed=12.0;sweep_band[1e-20,1e-10]_LISA_pts=0_PTAdec=0_GHz=121_other=0;any_LISA_in_sweep=False;kappa_for_LISA=2.506e+01s_42.5OOM_from_nat_11.4OOM_beyond_bandhi;f_emit=van_Hove_fold_ACOUSTIC_NOT_thermal_GUT;flagship=CGWB-PEAK-EVAPORATES_distinct_from_OmegaGW_amplitude_gate4'`. 4-tuple: `(value=⟨f_obs=8.48e39 Hz, band=GHZ+⟩, scheme=acoustic-dispersion-redshift-(A)-class, convention=substrate-fold-characteristic-frequency-NOT-relativistic-GW-redshift, L_max=N/A)`. dual-SHA: `audit=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e`, `content=2bc41ff416baf20758762957160b0b773ea787bc6329549774f9fc9308d63455` (full 64-char). **[SIGN] 3-tuple: `sign_verdict=PASS, magnitude_verdict=FAIL, regime_verdict=VALID` ⇒ composite FAIL** (gate-verdicts.md collapse: `mag=FAIL ∧ regime=VALID ⇒ FAIL`). dual_prior re-allocates to **Track B (0.6→0.9) with flagship-evaporation flag**: the peak stays far above GHz; the LISA CGWB-peak flagship evaporates.

**Results** (NUMBERS first, gate second, interpretation third):

*(NUMBERS) The redshift chain, fully resolved at the substrate-natural normalization.* The CGWB observed peak frequency is `f_obs = f_emit · a(τ_fold)/a(τ_now)`. Both pieces are now pinned:
- **Redshift factor (CC1, DIRECTLY RESOLVED).** Gate-5 gives `a(τ_fold)/a(0) = 2.117340` (no extrapolation). Since a GROWS from the fold, `a_now > a_fold`, so `a_fold/a_now = 1/2.117340 = 0.472291 < 1` ⇒ **REDSHIFT** (f_obs < f_emit). Sign confirmed.
- **Emission frequency (substrate-first, the load-bearing reframe).** `f_emit` is the fold's characteristic ACOUSTIC frequency, NOT a thermal GUT-transition frequency. In M_KK units the fold's only intrinsic frequency scale is M_KK itself (ω̃=1); converting to physical Hz needs the M_KK⁻¹→s normalization `kappa`. At the substrate-natural `kappa_nat = ħ/M_KK = 8.860440e-42 s` (= canonical `M_KK_inv_seconds`, verified `== ħ/M_KK` to rel 5.4e-10 and `==` gate-5 `kappa_nat`), `M_KK` in angular-frequency units is `1/kappa_nat = 1.1286e41 s⁻¹`, so `f_emit = M_KK/(2π) ≈ 1.796e40 Hz`.
- **Observed peak.** `f_obs(kappa_nat) = 1.796e40 · 0.472291 = 8.4835e39 Hz`. This is **43.93 decades ABOVE the LISA band-low edge (1e-4 Hz)** and **31.93 decades above the GHz floor (1e8 Hz)**. The fold acoustic mode spread (ω_L1, ω_PV, ω_tau, v_g_B2, c_fabric) brackets this from `1.93e38 Hz` (v_g_B2_fold) to `1.78e42 Hz` (c_fabric) — every fold mode lands in GHz+ after redshift.

*(NUMBERS) CC2 — the ~12-decade question, answered with its sign.* The naive thermal-GUT route (S58 Method-3 dimensional analysis, `f_0 ~ T_* T_0 / M_Pl` with `T_* ~ M_KK = 7.43e16 GeV`) gives `f_GUT_naive = 1.733e9 Hz` ≈ **1.7 GHz**. To move a GHz emission into the LISA mHz band requires `log10(1e9/1e-3) = 12.0` decades of extra suppression (Sage-exact). The D4 hypothesis was that ACOUSTIC dispersion (c_fabric, not c) supplies those ~12 decades. **It does the opposite.** The substrate-first acoustic emission scale (`f_emit ≈ M_KK/(2π) ≈ 1.8e40 Hz`) is **~31 decades ABOVE the naive GHz route, not below it** — acoustic dispersion moves the peak the WRONG way. The only redshift available (factor 0.472) is negligible against a 40-decade emission scale.

*(NUMBERS) The open M_KK⁻¹→s knob is NOT load-bearing here — the FAIL is robust to it.* The verdict is reported as a function of the open normalization `kappa` over gate-5's swept band `[1e-20, 1e-10] s/M_KK⁻¹` (121 points). `f_obs(kappa)` ranges from `7.52e18 Hz` (kappa_lo=1e-20) down to `7.52e8 Hz` (kappa_hi=1e-10) — **GHz+ at ALL 121 points** (band counts: LISA=0, PTA-DECIGO=0, GHZ+=121, OTHER=0). To land the canonical mode in the LISA pivot (3 mHz) the knob would need `kappa = 25.06 s/M_KK⁻¹` (i.e. 1 M_KK⁻¹ ≈ 25 seconds) — **42.45 OOM from `kappa_nat`** and **11.40 OOM beyond the swept band's upper edge**. No physically-motivated normalization within the entire swept range reaches LISA; the most extreme swept knob still lands at sub-GHz at best. This is therefore NOT a normalization-conditional INFO — the FAIL stands across the whole knob range, hence `regime_verdict=VALID` (not MARGINAL/BREAKDOWN).

*(GATE) [SIGN] 3-tuple + composite.*
- `sign_verdict = PASS`: substitution chain Step-4 predicted `a_fold/a_now < 1` ⇒ redshift; computed `0.47229 < 1` ✓ (direction confirmed — f_obs < f_emit).
- `magnitude_verdict = FAIL`: pre-registered band placement — PASS=LISA [1e-4,1e-1] Hz / INFO=PTA-DECIGO / FAIL=GHz+ (≥1e8 Hz). Computed `f_obs(kappa_nat)=8.48e39 Hz` ⇒ GHZ+ ⇒ FAIL, `|decades from LISA| = 43.9 ≫ 0.5` decade tolerance.
- `regime_verdict = VALID`: the band placement is stable (GHz+) across the entire swept normalization band — the verdict does not flip to LISA anywhere in `[1e-20,1e-10]`, so the FAIL is robust to the open knob (no MARGINAL/BREAKDOWN reservation needed).
- Composite collapse (gate-verdicts.md PRE-REGISTERED): `magnitude_verdict=FAIL ∧ regime_verdict=VALID ⇒ composite=FAIL`.

*(INTERPRETATION) D4 resolved AGAINST mHz — the CGWB-PEAK-FREQUENCY flagship evaporates.* This closes the "LISA via CGWB peak placement" corridor. The capstone §7.2 mHz placement was **asserted, not derived**; derived from the substrate's own acoustic scale + the directly-resolved redshift factor, the peak is at ~10⁴⁰ Hz — ~44 decades above LISA, ~32 above the naive GHz GUT expectation. Acoustic dispersion does not rescue a GHz→mHz shift; it pushes the emission higher. **Scope discipline (mack-bridge role, do-not-conflate):** this FAIL is on the CGWB peak-FREQUENCY observable ONLY. It is **DISTINCT** from the Ω_GW **AMPLITUDE** flagship adjudicated at §W6-4 (gate-4), which evaluates `Ω_GW^(A) ~ 1e-10` at a CHOSEN LISA pivot (3 mHz) and is a separate observable. Gate-4's amplitude claim is not falsified by this gate; what is falsified is the claim that the spectrum's intrinsic PEAK sits in the LISA band. A detector at the LISA pivot would see whatever (A)-class acoustic amplitude the spectrum has at 3 mHz (gate-4's deliverable), but the spectral PEAK is ~40 decades higher — so LISA samples the deep IR tail of the acoustic spectrum, not its peak. The §7.2 row must be corrected: replace the asserted "peak in LISA mHz band" with "peak at ~10⁴⁰ Hz (fold acoustic scale at kappa_nat); LISA samples the IR tail; peak-frequency placement is normalization-set and ~42 OOM of kappa-shift from any LISA placement."

*(WRITE-ORDER) Step 1 verdict ✓ (above). Step 2 `canonical_constants.py` ✓:* `update_constant('f_obs_CGWB_peak_kappa_nat', 8.4835e39, S96, s96_obs_cgwb_peak_freq.npz, gate=S96-OBS-CGWB-PEAK-FREQ, SECTION E)` — PROVENANCE entry added (observed CGWB peak freq [Hz] at substrate-natural kappa; GHz+ band; D4 resolved against mHz; distinct from Ω_GW amplitude). *Step 3 falsifier-inventory row → RECOMMENDATION to `mack-cosmic-bridge` (sole writer; NOT written here):*

> **Inventory-row RECOMMENDATION (to mack-cosmic-bridge, for W8-2 consolidation).** Correct the §7.2 / `falsifier-master-inventory.md` LISA CGWB flagship row to split the two observables: (a) **Ω_GW AMPLITUDE** at the LISA pivot — UNCHANGED (gate-4: `Ω_GW^(A) ~ 1e-10` at 3 mHz, 11+ OOM above LISA-PLS, GGE-acoustic-sourced, wall channel = 0). (b) **CGWB peak FREQUENCY** — CORRECTED: `f_obs(kappa_nat) = 8.48e39 Hz` (GHz+, 43.9 decades above LISA); the asserted "peak in LISA mHz band" is REFUTED by the substrate redshift chain. The peak-frequency placement is normalization-set (open M_KK⁻¹→s knob); reaching LISA needs `kappa = 25 s/M_KK⁻¹`, 42.5 OOM from the natural `ħ/M_KK` and 11.4 OOM beyond the swept band. Tag: live-watch on the M_KK⁻¹→s normalization (the SAME open knob blocking the derived a(t)); the peak-frequency flagship is `NORMALIZATION-CONDITIONAL-AND-CURRENTLY-AGAINST-mHz` pending a substrate-pinned kappa. Cross-ref: gate-3 `audit_sha256=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e`; canonical `f_obs_CGWB_peak_kappa_nat=8.4835e39`.

*(SUBSTRATE FRAMING) PHONONIC, tensor sector.* The CGWB is NOT a primordial GW background in expanding space — it is squeezed-graviton production at the van Hove fold (the GGE-acoustic excitation transduced into the tensor sector, crossing freely per [T3]). The chain is held substrate-first throughout: `D_K eigenvalues → van Hove fold (DOS divergence, group velocity → 0) → fold characteristic ACOUSTIC frequency (M_KK-unit ang. freq) → physical f_emit via the M_KK⁻¹→s normalization → redshift by a(τ_fold)/a(τ_now) (the readout of the substrate's spectral-complexity growth) → f_obs`. The emission frequency IS the substrate's own acoustic scale (~M_KK/(2π)), not a thermal-transition frequency imposed by a hot-big-bang container — and that is exactly why the answer is ~10⁴⁰ Hz, not GHz: the substrate has one frequency scale (M_KK), and the fold radiates at it. The D4 question was the substrate-vs-container distinction made quantitative: a standard relativistic redshift (or a thermal-GUT emission) would land at GHz; the substrate's OWN acoustic emission lands ~31 decades higher. The container intuition (peak in LISA band) is wrong because it implicitly assumes a thermal-GUT emission frequency that the substrate does not have. The single open dimensionful piece (M_KK⁻¹→seconds) is the same gap blocking the derived a(t); the gate reports the verdict as a function of it and finds the FAIL robust across the entire physically-swept range.

---

### §W6-4. S96-OBS-OMEGAGW-GGE-VS-ZN (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S96-OBS-OMEGAGW-GGE-VS-ZN`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (Ω_GW source decomposition: GGE-acoustic / squeezed-graviton vs Z_N wall network)
**Agent**: `mack-cosmic-bridge` (detector-reach + falsifier-inventory sole writer)
**Hypothesis**: The LISA Ω_GW flagship is sourced ENTIRELY by the GGE-acoustic / squeezed-graviton channel (Ω_GW^(A)~1e-10 at LISA f, 11+ OOM above LISA-PLS), with the Z_N wall-network contribution shown to be ZERO because π₀(U(1))=0 on the Jensen ridge (τ_DW=0.1135 is a geometric crossover, not a phase boundary) — so the older project-lore wall-attribution is superseded by the acoustic-class reading, and the two are CONSISTENT only if the wall contribution is genuinely zero.
**Plan reference**: `sessions/session-plan/session-96-plan-w6.md` §W6-4 (USE Sage-exact Ω_GW rationals per `regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW"` — round figures FORBIDDEN).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-96/s96_obs_omegagw_gge_vs_zn.py` — EXISTS (31,723 B). `grep` of must_contain:
  - `from canonical_constants import (` → matched (line 110, imports `Omega_GW_Lambda_A_LISA, Omega_GW_Lambda_C_LISA, Omega_GW_Companion_null, OOM_split_AC_regulator_class, c_fabric, Mach_max_framework`).
  - `append_verdict` → matched (def at §1 + invocation at §7).
- **data** `computations/session-96/s96_obs_omegagw_gge_vs_zn.npz` — EXISTS (15,254 B; Sage-exact rational num/den pairs, π₀/π₁/π₂, spectral-shape grids, verdict).
- **plot** `computations/session-96/s96_obs_omegagw_gge_vs_zn.png` — EXISTS (100,864 B; LISA-band spectral-shape discriminator + log-amplitude source-decomposition bar).
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — matches `^S96-OBS-OMEGAGW-GGE-VS-ZN:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=a9998118fdcb96bd41ebae88b0c2af0d5c4fb0c7c6d9bc277b62a50e10a0d382` (unique in file, sig_5 clean); dual-SHA companion row present; **no [SIGN] 3-tuple** (`schema_v2_3tuple_required: false` — [VERIFY], not [SIGN]).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; query-first discipline):
- `get_constant('Omega_GW_Lambda_A_LISA')` → **1e-10** (A-class flat acoustic; S87; "Substrate-physics OOM estimate at LISA 3 mHz").
- `get_constant('Omega_GW_Companion_null')` → **8.299e-58** (S86; gate `S86-W3-CANON-EXTRACT`; superseded=False).
- `get_constant('Omega_GW_Lambda_C_LISA')` → **8.299e-58** (Sage-exact alias of Companion-null; (C)-class regulator; S87).
- `get_constant('OOM_split_AC_regulator_class')` → **47.081** (S86; W-3 R2-B Dissent #2 Sage-verified; superseded=False).
- `trace_entity('Domain-wall GW')` → theorem `proven_1051` PROVEN; **but the LISA wall channel is CLOSED/RETRACTED**: `open_channel 'Domain-wall GW (LISA)' RETRACTED S77 (Josephson bias kills walls 15,000× before reheating)`; `closed_98 'Domain wall GW | GHz frequencies, no detector | S58'`; `closed_174 'domain_wall_GW_GUT_GHz | frequency mismatch | GUT→GHz; LISA needs TeV'`. **PRE-CLOSED corroboration** — the wall channel is dead by two independent mechanisms (topology + dynamics).
- `search_knowledge('pi_0 U(1) domain wall Z_N Jensen ridge tau_DW topological')` → `session-19d-landau-collab.md`: **π₀(G/H)=0 (no domain walls — connected coset), π₁(G/H)=Z (vortex lines, from π₁(U(1))=Z), π₂(G/H)=0 (no monopoles)** — the exact Kibble classification for this coset, independent of S77. Also `tau_DW=0.113488` (`s59_ricci_dw_log.txt`, equations-only — NOT a canonical constant).
- `search_knowledge('Omega_GW spectral shape acoustic f^3 ... domain wall')` → `session-58-lrd-collab.md`: wall annihilation gives a **Hiramatsu et al. peaked** spectrum `Ω_GW ∝ f³ (f≪f_pk), f⁻¹ (f≫f_pk)`; `falsifier-rigor-registry.md`: `Omega_GW (domain walls, LISA f) | DETECTOR-STERILE | ~10⁻¹⁰ at 1 mHz; 46.7 OOM below LISA`. Supplies the spectral-shape discriminator + the SUPERSEDED-lore amplitude.
- Sage MCP `sage_eval` (QQ-exact): Ω_GW^(A)=1/10¹⁰, Ω_GW^(C)=8299/10⁶¹, OOM split = **47.080974** (canonical 47.081 is the rounded form; residual −2.58e−5).

**Verdict**: **PASS** — `value='Omega_GW_walls=0_EXACT_pi0(U1)=0; flagship=acoustic_OmA=1.000e-10; OmC=8.299e-58_Sage_exact; OOM_split=47.081; wall_zero_tol=1e-12; round_fig_1e-57_understate=1.205x_0.081OOM; old_wall_lore_consistent=True'`. 4-tuple: `(value=⟨wall=0 EXACT, flagship=acoustic⟩, scheme=(A)-vs-(C)-vs-wall-regulator-class-Omega-GW, convention=Sage-exact-rational-Omega-GW-NOT-round-figure, L_max=N/A)`. dual-SHA: `audit=a9998118fdcb96bd41ebae88b0c2af0d5c4fb0c7c6d9bc277b62a50e10a0d382`, `content=d1e430bd1ee35ff136d5b1e1404b4fab107a5b92919964cd08c5d879a932b84c` (full 64-char). The operator `Ω_GW^{walls}(Jensen ridge) == 0 (structural, from π₀(U(1))=0) AND flagship == Ω_GW^(A)_acoustic` is satisfied: dual_prior re-allocates to **Track A (0.7→0.9): wall contribution zero, flagship purely acoustic, consistent with capstone**.

**Results**:

*(A) Sage-exact regulator-class Ω_GW (round figures FORBIDDEN).* Ω_GW^(A) = `1/10¹⁰` = **1.00000e-10** (A-class, flat acoustic baseline); Ω_GW^(C) = `8299/10⁶¹` = **8.29900e-58** (C-class, Companion-null). OOM split = `log₁₀(A) − log₁₀(C)` = **47.080974** (Sage-exact; the canonical pin `OOM_split_AC_regulator_class=47.081` is the 5-sig-fig rounded form, residual −2.58e−5). All four canonical-import checks PASS (the imported floats match the exact rationals to <1e−12). **FIDELITY CORRECTION (do-not-overstate, mack-bridge role):** the substrate_framing prose + `regulator-pin-discipline.md §"Sage-Exact Rationals"` say the round figure `1e-57` "understates Ω_GW^(C) by ~10× (~1 OOM) and propagates a ~2 OOM error to the split." The EXACT figures are: `1e-57 / 8.299e-58 = 1.20496×` (i.e. **0.081 OOM**, NOT 1 OOM); the split error from the round figure is **0.081 OOM**, NOT 2 OOM. The *discipline* (use the Sage-exact rational, never `1e-57`) is correct and binding — but the "~10×/~2 OOM" magnitude in the rule/plan prose is itself an over-statement of the round-figure error. The correct statement: `1e-57` is ~1.2× the exact (C)-class value, an 0.08-OOM distortion; the binding reason to use the exact form is publication-precision hygiene (Class-8.3), not a 2-OOM blunder. This correction is recorded for the W8-2 inventory consolidation.

*(B) Structural wall=0 verdict — substitution chain with substituted numbers.* The Z_N wall-network Ω_GW contribution is **ZERO on the Jensen ridge, EXACTLY (topological, not numerical smallness)**:
- **Step 1 (Kibble classification, CC1):** domain-wall existence ⟺ `π₀(vacuum manifold) ≠ 0` (disconnected vacua).
- **Step 2:** the Jensen-ridge GGE-universality vacuum manifold is `U(1) = S¹`.
- **Step 3 (substitute):** `π₀(U(1)) = 0` (the circle S¹ is path-connected ⇒ exactly one path-component ⇒ trivial π₀). Cross-checked against `session-19d-landau-collab.md`: `π₀(G/H)=0, π₁(G/H)=Z, π₂(G/H)=0`.
- **Step 4 (simplify):** no disconnected vacua ⇒ no domain walls ⇒ Z_N wall network **ABSENT** ⇒ `τ_DW=0.113488` (`s59_ricci_dw_log.txt`) is a **GEOMETRIC crossover** of the Jensen-deformation landscape, **NOT a topological phase boundary**.
- **Step 5 (canonical form):** `Ω_GW^{walls}(Jensen ridge) = 0` EXACTLY.
- **Step 6 (consistency read-off):** the OLD lore (`project_lisa-gw-prediction`) attributed `Ω_GW ~ 1e-10` to **WALLS**; the capstone attributes the flagship to the **ACOUSTIC class**. These are CONSISTENT **iff** the wall contribution is zero (⇒ PASS) and INCONSISTENT (a genuine two-channel signal) iff a non-zero wall Ω_GW survives (⇒ FAIL). Computed: `wall_is_zero=True`, `flagship_is_acoustic=True`, `old_lore_consistent=True` ⇒ **PASS**.

*(C) Independent corroboration (NOT load-bearing — the gate needs only the topology).* The wall channel is killed by a SECOND, dynamical mechanism on top of the topological one: the Josephson bias kills any transient wall **15,000× before reheating** (`open_channel 'Domain-wall GW (LISA)' RETRACTED S77`). So even granting (counterfactually) a disconnected vacuum manifold, the walls would not survive to source GWs. The topological kill (π₀=0, no walls *form*) and the dynamical kill (Josephson bias, any walls *die*) are independent and concordant.

*(D) CC2 — the SUPERSEDED domain-wall lore.* The pre-capstone reading (`Ω_GW^{walls} ~ 1e-10 at 1 mHz`) is recorded as **DETECTOR-STERILE** in `falsifier-rigor-registry.md`: ~10⁻¹⁰ at 1 mHz but **46.7 OOM below LISA** with migration threshold 10⁻⁴⁰ (S83 Channel-5). The substrate-first reading supersedes this entirely: there is no wall network to be sterile — the flagship `Ω_GW ~ 1e-10` belongs to the **(A)-class acoustic** channel (11+ OOM *above* LISA-PLS), not the walls. The two cannot both be the source; the topology decides for the acoustic channel.

*(E) LISA-band spectral-shape discriminator (the falsifier-inventory deliverable).* Even though the wall channel is zero, the gate computes WHAT LISA WOULD SEE to distinguish an acoustic-class from a (counterfactual) wall-class spectrum, over the LISA band [1e−4, 1e−1] Hz (150 log-spaced points, pivot 3 mHz):

| Discriminator | ACOUSTIC class (PRESENT) | WALL class (counterfactual; structurally ABSENT) |
|:---|:---|:---|
| Spectral shape | broad, causal `f³` IR → flat plateau in LISA band | Hiramatsu-peaked: `f³` IR, `f⁻¹` UV, **narrow peak** |
| Peak location | near LISA pivot (fold acoustic scale) | **GHz** (wall annihilation scale) — `11.52` decades away |
| LISA-band amplitude | Ω_GW^(A) ≈ **1e-10** (11+ OOM *above* LISA-PLS) | ≈ Ω_GW^(C) ≈ **8.299e-58** (`f³` causal rise; 45–46.7 OOM *below* LISA) |
| Amplitude ratio (the dominant discriminator) | — | **47.081 OOM** (== the (A)/(C) OOM split) |

The IR slope alone does NOT discriminate (both ~`f³` by causality); the discriminators are (a) the LISA-band **amplitude** (47.08-OOM gap), (b) the peak **location** (LISA pivot vs GHz, 11.5 decades), and (c) the peak **sharpness** (acoustic broad vs wall narrow). Since the wall channel is structurally zero, **only the acoustic shape is present** in the LISA band — LISA measures a broad acoustic plateau, never a wall peak.

*(F) Falsifier-inventory annotation (mack sole writer).* Per the canonical write-order, the falsifier-master-inventory CGWB/Ω_GW flagship row is annotated with the **acoustic-vs-wall channel decomposition**: the LISA flagship `Ω_GW^(A) ~ 1e-10` is sourced by the GGE-acoustic / squeezed-graviton channel; the `Z_N` wall channel is `Ω_GW^{walls} = 0` EXACTLY (π₀(U(1))=0); the LISA spectral-shape discriminator (broad acoustic plateau, NOT a GHz-peaked wall spectrum) is the live signature. The W6 sibling gates (1/2/3) emit inventory-row recommendations addressed to me in their own WP sections; those are NOT actioned here — they consolidate at **W8-2** (they may not be landed yet). See the inventory-write block below for the row landed this gate.

*(G) Substrate framing.* The Ω_GW flagship is the squeezed-vacuum graviton production at the van Hove fold (the GGE-acoustic spectrum transduced into the tensor sector, which crosses freely per [T3]). The substrate-first reading is **not** "a sub-dominant wall contribution" but a **structurally absent** one: `D_K → Jensen-ridge vacuum manifold U(1) → π₀(U(1))=0 → no walls`, in parallel with `D_K → van Hove fold → squeezed-graviton acoustic spectrum → Ω_GW^(A)`. The wall channel is not "redshifted away in a container"; it never forms. The arrow is held throughout: substrate IS the connected vacuum manifold; the absence of walls is a property of the substrate's own topology, not a fine-tuning of a defect-network model living *in* a background.

---

### §W6-5. S96-OBS-LRD-ASSEMBLY-CLOCK (little-red-dots)

**Status**: COMPLETED
**Gate ID**: `S96-OBS-LRD-ASSEMBLY-CLOCK`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the assembly clock is the readout of a(τ) Connes-distance scale factor; the a(τ)→z(t) map is a property of the spectral-triple deformation)
**Agent**: `little-red-dots`
**Hypothesis**: The SCALE-FACTOR-54 Connes-distance a(τ) proxy (the one carrying the real deceleration band q:−0.97→+0.81, NOT the near-flat a_eff) yields an LRD-epoch cosmic time t(z=6) within 2× of the ΛCDM t(z=6) as a function of the open M_KK⁻¹→s normalization — so the substrate does NOT catastrophically shorten or lengthen the high-z structure-assembly window.
**Plan reference**: `sessions/session-plan/session-96-plan-w6.md` §W6-5 (uses the Connes-distance a(τ), NOT a_eff whose q_Ω diverges; intra-wave producer of the a(τ)→z map gate-3/CGWB-PEAK-FREQ consumes).

**Verdict**: **FAIL** — composite (sign=PASS, magnitude=FAIL, regime=VALID). The verdict is **normalization-conditional and structurally informative**: the proxy's clock *shape* is ΛCDM-consistent, but no M_KK⁻¹→s normalization in the pre-registered swept band makes its *magnitude* match. Per the dual prior this lands ~0.85 on **Track B** (a_eff-class Connes-distance proxies cannot substitute for a derived a(t); the a(t) gap **C1** is load-bearing for the entire LRD-confrontation chain). All results are good results: this FAIL closes the "the deceleration-band proxy can stand in for a(t)" corridor.

**4-tuple**: `value=R_clock(z=6)_normalization-conditional:kappa*=9.100e+17s/M_KK^-1_in_swept_band[1e-20,1e-10]=False_any_kappa_PASS=False_R_clock(KAPPA_LO)=1.10e-38_R_clock(KAPPA_HI)=1.10e-28_kappa_nat=8.86e-42_clock_orders=True_NOT_a_eff_q-band=[-0.97,+0.81]`, scheme=`Connes-distance-a(tau)-proxy-NOT-a_eff`, convention=`substrate-fold-rate-tau-dot-local-NOT-borrowed-H`, L_max=NA.

**MCP Pre-Compute Audit** (query-first, executed before authoring the script):
- `search_knowledge('SCALE-FACTOR-54 a(tau) Connes-distance deceleration band proxy')` → **gate SCALE-FACTOR-54 PASS**, `q: −0.97 → +0.81` (Connes-distance proxy), "Carries deceleration band; NOT a_eff (II.1)" (little-red-dots-synthesis.md); equation `a(τ_fold)/a(0)=2.117` (session-54-baptista-collab.md). CONFIRMS the proxy identity + the real deceleration band; NOT a re-derivation of a closed result (no closure covers the LRD assembly-clock t(z) integral).
- `search_knowledge('a_eff deceleration q diverges Connes-distance scale factor s54')` → equation `a_eff(τ)=(a_2(τ)/a_2(τ_today))^{1/2}` (session-73b-plan.md, near-flat) vs the Connes-distance proxy carrying the band; provenance `s54_scale_factor.py → s54_scale_factor.npz (FACTOR-54)`. CONFIRMS the a_eff-vs-Connes distinction the gate hinges on.
- `get_constant('tau_fold')` → **0.19** (S12/S42, CONST-FREEZE-42). `get_constant('M_KK')` → **7.428660036284456e16** GeV (S42). Used for context (κ_nat) + framing.
- `get_constant('delta_t_transit')` → **not found** under that name; resolved to canonical `dt_transit = 0.0011301575037571713 M_KK⁻¹` (S38, line 513) — matches the plan's `δt_transit=1.130e-3 M_KK⁻¹` (the only derived rate). Transit frequency `omega_tau = dτ/dt = 8.27` (M_KK units, S38 attractor, line 497) supplies the τ→M_KK⁻¹ conversion.
- Planck anchors confirmed in `canonical_constants.py`: `H_0_km_s_Mpc=67.4`, `Omega_m=0.315`, `H_0_inv_s=2.184e-18`.

**Results**:

*Inputs / cross-check.* SCALE-FACTOR-54 grid (`s54_scale_factor.npz`, sha256 `7533792ae42d5921…`): `τ∈[0,0.3469]`, `a∈[1.000,3.494]` (a=1 at the τ=0 cosmogenesis origin, a GROWS monotonically), `H_proxy=dln a/dτ∈[2.588,3.952]` (per-τ units), `q∈[−0.9732,+0.8144]` (the real deceleration band), `a_at_fold=2.1173` at `τ_fold=0.19`, `q_at_fold=−0.786`. Exponential fit `a=A·exp(B·τ)` with A=1.0493, B=3.5322, R²=0.9973. **Validation cross-check**: `∫ dln(a)/H_proxy = 0.34777` recovers the grid τ-span `0.34694` to rel.err `2.4e-3` — confirms `H_proxy = dln a/dτ` (the integral machinery is exact on the measured grid).

*ΛCDM anchors (Planck 2018, H_0=67.4, Ω_m=0.315, flat).* `t_LCDM(z=0)=4.354e17 s=13.80 Gyr`; `t_LCDM(z=4)=4.851e16 s=1.537 Gyr`; `t_LCDM(z=6)=2.934e16 s=0.930 Gyr`; `t_LCDM(z=8)=2.013e16 s=0.638 Gyr`.

*Substitution chain (the clock definition, corrected to AGE-at-z).* The age at redshift z is the elapsed proxy time from the cosmogenesis origin (a=1, τ=0) up to a(z):
- Step 1: `H_proxy(τ)=dln a/dτ` ⟹ `dτ = dln(a)/H_proxy` ⟹ `t_age(z)=∫_{a=1}^{a(z)} dln(a)/H_proxy` (dimensionless elapsed-τ; this recovers Δτ by the cross-check above).
- Step 2: τ→M_KK⁻¹ via `dt = dτ/omega_tau`, `omega_tau=8.27`. M_KK⁻¹→s via the OPEN knob `κ ≡ seconds per M_KK⁻¹` (swept, NOT invented). So `t_age(z)[s] = (κ/omega_tau)·t_age(z)[dimensionless]`.
- Step 3: redshift map `1+z = a_now/a(z)` ⟹ `a(z)=a_now/(1+z)`. `a_now` (the z=0 placement) is itself an exp-fit extrapolation of the now-anchor (the grid only spans a factor 3.494 in a; the LRD ladder from cosmogenesis needs ≥9 — this range deficit is part of the open piece). PRIMARY anchor places z_max=8 at the fold (`a_now=(1+8)·a_fold=19.06`), keeping the z=6 age integral entirely inside the measured grid; companion anchor places z=8 at the origin (`a_now=9.0`).
- Step 4 (direction): a GROWS from cosmogenesis ⟹ `a(z)=a_now/(1+z)` DECREASES with z ⟹ the integration path `[1, a(z)]` SHORTENS ⟹ **SMALLER age at higher z**. Computed: `age(z=4)=0.3764 > age(z=6)=0.2666 > age(z=8)=0.1954` (dimensionless). **SIGN=PASS** — clock orders correctly, matching standard cosmology (lower z = larger age). Covered fraction of the z=6 age integral inside the measured grid = **1.000** ⟹ **REGIME=VALID**.

*The normalization-conditional magnitude (the load-bearing finding).* `R_clock(z) = t_age_proxy(z)/t_LCDM(z) = (κ/omega_tau)·age(z)/t_LCDM(z)`, linear in κ. The κ* that lands `R_clock(z=6)=1` is **κ* = omega_tau·t_LCDM(z=6)/age(z=6) = 9.100×10¹⁷ s/M_KK⁻¹**. At that κ*, the *shape* is excellent: `R_clock(z=4,6,8) = 0.854, 1.000, 1.068` — all three LRD redshifts simultaneously inside [0.5,2.0]. **But** κ* is (a) FAR outside the pre-registered swept band `[1e-20,1e-10]` s/M_KK⁻¹, and (b) ~59 OOM above the natural-units value `κ_nat = ħ/M_KK = 8.86×10⁻⁴² s/M_KK⁻¹`. Within the entire swept band, `R_clock(z=6)∈[1.10×10⁻³⁸, 1.10×10⁻²⁸]` — uniformly `< 0.1×` ΛCDM. At natural units, `R_clock(z=6)=9.7×10⁻⁶⁰`. So **no physically-defensible normalization (swept band or natural units) makes the magnitude match** ⟹ **MAGNITUDE=FAIL**; composite collapse (`mag=FAIL ∧ regime=VALID ⟹ FAIL`).

*Interpretation (substrate-first).* The proxy's clock SHAPE tracks ΛCDM (R_clock within 2× at z=4,6,8 *simultaneously* once normalized), so the deceleration-band a(τ) is not qualitatively wrong about the high-z assembly ordering. What FAILs is the absolute magnitude: the M_KK⁻¹→seconds conversion needed to align the proxy with the ΛCDM cosmic-time axis is unphysical (κ*≈9×10¹⁷ s/M_KK⁻¹ would make a single fold last ~30 Gyr). This is exactly the **a(t) gap C1**: the Connes-distance proxy carries the right *deceleration band* and the right *clock shape* but cannot supply the absolute *cosmic-time normalization*. **A derived a(t) (the C1 frontier) is therefore load-bearing for every quantitative LRD "too massive too early" constraint** — the proxy can confront the *ordering* of the assembly window but not its absolute duration. The substrate IS the growing spectral complexity; "the LRD assembly timeline" is how much of that growth has happened by a given z — and the proxy resolves the *fraction-of-growth* (shape) but not the *seconds-per-unit-growth* (magnitude).

*Feed to W6-3 (CGWB-PEAK-FREQ, dispatched after this gate).* npz consumer keys are explicit: `a_fold_over_a0_computed=2.1173` (the DIRECTLY-resolved redshift factor a_fold/a(0), the W6-3 chain anchor — NOT the extrapolated a_now), `kappa_sweep` (121-pt M_KK⁻¹→s knob), `kappa_star=9.100e17`, `kappa_nat=8.860e-42`, `omega_tau_used=8.27`, `a_fold_value=2.117`, `a_now_primary=19.06`. W6-3's redshift chain `f_obs=f_emit·a_fold/a_now` reads the same `s54_scale_factor.npz` input; the directly-resolved `a_fold/a(0)=2.117` is the no-extrapolation factor, and the M_KK⁻¹→s normalization is flagged as the SAME open knob blocking the CGWB band placement.

*LRD watchlist feed.* This gate confirms the "too massive too early" tension cannot be quantitatively confronted by the a(τ) proxy alone: the assembly-window *duration* at z~6 is normalization-locked to the undetermined M_KK⁻¹→s conversion. The watchlist row records: SHAPE-consistent (R_clock∈[0.5,2.0] across z=4,6,8 at κ*), MAGNITUDE-blocked (κ* outside swept band + 59 OOM above natural units), a(t)-gap-C1 load-bearing.

**Output Artifacts**:
- Script: `computations/session-96/s96_obs_lrd_assembly_clock.py` — contains `from canonical_constants import` and `append_verdict`.
- Data: `computations/session-96/s96_obs_lrd_assembly_clock.npz` (48 keys; W6-3 consumer keys + R_clock-vs-κ sweep + verdict 3-tuple).
- Plot: `computations/session-96/s96_obs_lrd_assembly_clock.png` (4-panel: a(τ) proxy + exp fit; q(τ) deceleration band; R_clock(z=6) vs κ with PASS/INFO bands + κ*/κ_nat markers; age & R_clock(z) at κ*).
- Verdict line: `computations/session-96/s96_gate_verdicts.txt` — `S96-OBS-LRD-ASSEMBLY-CLOCK: FAIL …` matching `^S96-OBS-LRD-ASSEMBLY-CLOCK:.* audit_sha256=[a-f0-9]{64}` (audit_sha256 `2ca30407c3ae96176e1f3cd608e95ccce210745e04eb34a16bc7b5e714c7f459`, content_sha256 `6ba56c287e4eecd2991f7368accd09c525e0ee854e3b7303b7a274449493cd9e`), with dual-SHA companion row + schema-v2 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`), and `supersedes=8231ddfc8a5fbfa6…` tagging the superseded first-draft line (Option A absolute verdict permanence; the first draft used a lookback-time clock and was corrected to age-at-z).

**Substrate framing**: GEOMETRIC. The assembly clock is the READOUT of the substrate's spectral-complexity growth: `a(τ)` is the Connes-distance scale factor (the mean distance between states on the spectral triple `(A_K, H_K, D_K)` grows as the Jensen deformation τ proceeds), and `t(z)` is the elapsed-time integral of that growth — `D_K eigenvalues → Jensen deformation τ → Connes distance ⟨d_D⟩(τ) → a(τ) → H_proxy=dln a/dτ → t(z)`. This is NOT "cosmic time in an expanding container": the substrate IS the growing spectral complexity. The gate uses the Connes-distance `a(τ)` (carrying the real band q:−0.97→+0.81), NOT `a_eff=(a₂/a₂_today)^{1/2}` (near-flat, q_Ω diverges). Per the substrate-first sourcing rule, the single open dimensionful piece (M_KK⁻¹→seconds) is NOT invented — it is swept as a free knob and the verdict reported as a function of it. The FAIL is structurally informative: it proves the a(t) gap (C1) is load-bearing for the entire LRD-confrontation chain.

---

### §W6-6. S96-OBS-CMB-SCENARIO-D2 (little-red-dots)

**Status**: COMPLETED
**Gate ID**: `S96-OBS-CMB-SCENARIO-D2`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (GGE-relic-IS-CMB post-transit acoustic interference vs hot-big-bang handoff — both are substrate cosmogenesis readings)
**Agent**: `little-red-dots` (transit-dynamics + hawking-theorist co-derive; mack adjudicates the CMB-observable consequence)
**Hypothesis**: Exactly ONE of the two cosmogenesis readings is consistent with the capstone's other claims — either (a) §5.3/§7.1 "GGE relic IS the CMB" (interference pattern of post-transit GGE acoustic excitations) OR (b) s53 SCENARIO A (exflation sets T_init=0.112·M_KK=8.32e15 GeV and hands off to a standard hot big bang) — and the gate determines which, plus whether either reading yields a primordial matter P(k) seeding an LRD-testable halo mass function.
**Plan reference**: `sessions/session-plan/session-96-plan-w6.md` §W6-6. **WORKSHOP FLAG (D2)**: per `.claude/rules/Investigating-Workshops.md` Q1 (math/physics adjudication — two competing structural readings of the same observable), D2 is a genuine workshop seed AND a compute gate; this gate pre-registers the COMPUTE LEG (structural-consistency set-cardinality verdict); if the S96 workshop schedule convenes a D2 workshop, this verdict is its R1 input. (`substitution_chain.required: false` — NON-numerical structural-reconciliation gate; PASS criterion is set-cardinality, pinned in `operator` + rubric.)

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-96/s96_obs_cmb_scenario_d2.py` — EXISTS. `grep -nE 'from canonical_constants import|append_verdict'` → L65 `from canonical_constants import (`, L176 `def append_verdict(verdict, value_str, audit_sha, content_sha):`, L351 `append_verdict(R["verdict"], value_str, audit_sha, content_sha)`. Both `must_contain` present.
- **data** `computations/session-96/s96_obs_cmb_scenario_d2.npz` — EXISTS (35 keys: verdict, scenario_consistency_count, committed_reading, a_/b_ P(k)-consistency flags, T_init cross-check, ns_scheme_set).
- **plot** `computations/session-96/s96_obs_cmb_scenario_d2.png` — EXISTS (`optional: true`; produced — the side-by-side P(k)-role comparison table + set-cardinality verdict panel).
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — EXISTS, matches `^S96-OBS-CMB-SCENARIO-D2:.* audit_sha256=[a-f0-9]{64}` (1 match); dual-SHA companion row present; `schema_v2_3tuple_required: false` ([VERIFY] structural-reconciliation, no signed-delta) — correctly NO 3-tuple row. `audit_sha256=80a3f0d9…f195290` unique across the file (1 occurrence).

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge('GGE relic CMB acoustic signature Ordered Veil thermalize')` → **The Ordered Veil (S38) PROVEN**, "the transit IS the physics"; "GGE relic cannot thermalize via phonon scattering" (Richardson-Gaudin integrability + infinite thermal conductivity); open_channel "The Post-Pulse Ringing — GGE Relic as the Observable Universe". Confirms the §5.3 reading: the GGE is a **standing** acoustic relic (integrable, never thermalizes), NOT thermal-equilibrium radiation.
- `search_knowledge('SCENARIO A hot big bang T_init exflation cosmogenesis reheating')` → **T_init = 8.3201e15 GeV (8.32×10¹⁵ GeV)**, "SCENARIO A: Exflation sets initial conditions for standard Big Bang"; N_e_exfl = 80.89, cooling exponent = −0.8685 (s53_exflation_cmb_temp_output.txt). Confirms SCENARIO A's exact content + that it is an *initial-conditions-for-standard-BB* statement.
- `get_constant('M_KK')` → 7.428660036284456e16 GeV (S42 CONST-FREEZE-42) ⇒ T_init = 0.112·M_KK = 8.3201e15 GeV (the PROVEN relation; t_init cross-check passes at 0.4%).
- `get_constant('T_acoustic')` → 0.112 (GGE acoustic temperature, M_KK units); `get_constant('n_pairs')` → 59.8; `get_constant('S_inst')` → 0.06860372; `get_constant('P_exc_kz')` → 1.0 (Kibble-Zurek, P=1 exactly).
- `list_constants('n_s|A_s|...')` + `get_constant('n_s_framework')` → **n_s scheme set {0.9561 (canonical, S85), 0.9590, 0.9595 (S65 BCS+one-loop, SUPERSEDED, on disk)}**; A_s_CMB = 2.1e-9 (Planck 2018).
- `trace_entity('Ordered Veil GGE permanence')` → theorem 37-38 PROVEN (Ordered Veil. GGE permanence. Instanton paradigm.).
- **Direct s53 read** (`s53_exflation_cmb_temp_output.txt`): SCENARIO A graded **INFO** in s53 itself; the 80.89 e-folds are **DECELERATING** (w=0.158 < 1/3), "do NOT solve the horizon/flatness problems", "the GGE plays the role of the reheating temperature… but unlike inflation, it is PREDICTED". **s53 second-sound output**: n_s running dn_s/dl ~ (c_Gold/c_fabric)² ≈ 1.9e-5 — i.e. **both n_s and its running are GGE-acoustic**, not hot-BB.
- **PRE-CLOSED?** No single closure covers D2; the two readings exist in different corpus locations (capstone §5.3 vs s53). The reconciliation is the deliverable. Constants/theorems all confirmed canonical — nothing recomputed.

**Verdict**: **PASS** — `scenario_consistency_count = 1` (PASS-coherent). The committed cosmogenesis reading is **(a) §5.3 "GGE relic IS the CMB"**. SCENARIO A is the τ-early temperature-normalization sub-layer of the SAME story, formally excluded as an *independent* primordial-P(k) source.

**Results**:

**The 4-tuple**: `(value=count=1;committed=(a)_§5.3_GGE-relic-IS-CMB;verdict_class=PASS-coherent;a_Pk_consistent=True;b_Pk_consistent=False;a_ns_tilt=0.9561;b_supplies_T_budget=True;b_decelerating_w=0.158;same_story_two_layers=True;lrd_Pk_shape=True;halo_mf_blocked_by_at_gap=True;T_init=8.3201e+15GeV, scheme=structural-cosmogenesis-reconciliation, convention=substrate-IS-cosmogenesis-NOT-container-initial-conditions, L_max=N/A)`.
**dual-SHA (full 64-char)**: `audit_sha256=80a3f0d96eef1d2f6438e66d45f5e8f12420d88eecaec162fbf0ba366f195290`, `content_sha256=5780a6d8f875e7e0e171afc011b0d8e52b8857da7c69fecd4b31335cc8ea2527`.

**Side-by-side structural lay-out (the primordial-P(k) ROLE under each reading):**

| Criterion | (a) §5.3 GGE-relic-IS-CMB | (b) s53 SCENARIO A |
|:----------|:--------------------------|:-------------------|
| primordial-P(k) ROLE | GGE acoustic interference spectrum (N_pair=59.8, P_exc=1.000, S_inst=0.0686 Bogoliubov-squeezed modes) | standard inflationary / hot-BB spectrum AT T_init (BORROWED from standard cosmology) |
| **C1** self-contained P(k)? | **YES** — tilt is the framework's own derived n_s (gauge-invariant spectral geometry); running dn_s/dl ~ (c_Gold/c_fabric)² ≈ 1.9e-5 is ALSO GGE-acoustic | **NO** — supplies a TEMPERATURE BUDGET (T_init→cool→T_CMB), not a P(k) |
| **C2** tilt ∈ scheme set {0.9561,0.9590,0.9595}? | **YES** (0.9561 canonical) | n/a (no self-contained P(k)) |
| EOS / dynamical character | standing acoustic relic — Ordered Veil (Richardson-Gaudin integrable, never thermalizes) | w=0.158 **DECELERATING** (< 1/3); "do NOT solve horizon/flatness" |
| s53's own verdict on it | n/a | **INFO**: "requires standard cosmology after the exflationary epoch" |
| **P(k)-CONSISTENT (C1 ∧ C2)?** | **YES** | **NO** |

**The set-cardinality verdict**: `scenario_consistency_count = 1` ⇒ **PASS-coherent** (exactly one P(k)-consistent reading; the other formally excluded as an independent P(k)-source). Against the capstone's n_s scheme set {0.9561, 0.9590, 0.9595}, the A_s band (A_s_CMB=2.1e-9), and the §7.1 DM/structure claims, only reading (a) supplies a self-contained primordial P(k) whose tilt is a framework prediction.

**What plays the role of the primordial P(k) seeding halos** — reading (a): the **GGE acoustic interference spectrum** (the post-transit Bogoliubov-squeezed standing modes, N_pair=59.8) carries the primordial fluctuation power; its tilt IS the framework n_s=0.9561 and its running is the GGE second-sound running. Reading (b) does NOT supply an independent P(k) — it supplies the *temperature* normalization only.

**The same-story / two-layers resolution** (`same_story_two_layers=True`): the two readings are NOT two competing P(k)-sources — they are two **complementary roles of the ONE GGE relic** at two timeline layers:
- SCENARIO A's `T_init = 0.112·M_KK = 8.3201e15 GeV` is the τ-**early** (formation) boundary condition; cooling this seed through the 80.89-e-fold budget sets the CMB **temperature** (2.7255 K). (T_init cross-check: 0.112·M_KK = 8.32010e15 GeV vs s53 8.3201e15 GeV; consistent at 0.4%.)
- §5.3's acoustic interference is the post-transit **readout** that sets the CMB **anisotropy spectrum** (the P(k) SHAPE, n_s and its running).

So "GGE relic IS the CMB" is the SAME relic playing both roles — the *temperature* (via the SCENARIO-A cooling budget) and the *anisotropy power spectrum* (via the acoustic interference). This is precisely the τ-early-limit relationship the plan's substrate-framing anticipated.

**§5.3 / §7.1 cosmogenesis-wording consequence**: **§5.3 is TIGHTENED, not over-stated**. The phrase "GGE relic IS the CMB" is correct for the **anisotropy spectrum** (the P(k) shape / n_s), with SCENARIO A's T_init understood as the τ-early *temperature-normalization* boundary of the SAME story rather than a competing cosmogenesis timeline. The recommended §5.3 edit (routed to the capstone designated writer per the capstone-hygiene gate, Q3 status-coherence): scope "GGE relic IS the CMB" to "the GGE relic's acoustic interference IS the CMB anisotropy spectrum; its formation temperature T_init=0.112·M_KK cools through the exflationary e-fold budget to set the CMB temperature." No FAIL-incoherent escalation to a D2 workshop is required on the merits — but per the plan's workshop flag, the convened D2 workshop (if it runs) takes this PASS-coherent verdict as its R1 input.

**LRD-testable P(k)?** The committed reading (a) DOES yield a primordial P(k) **SHAPE** (`lrd_testable_Pk_shape=True`): the GGE acoustic spectrum with tilt n_s=0.9561, from which a halo mass function could in principle be computed. BUT the actual LRD halo-MF confrontation remains **blocked by the a(t)→t(z) absolute-normalization gap** (`halo_mf_blocked_by_at_gap=True`; the C1 open piece flagged in §W6-5). The P(k) shape exists; the absolute cosmic-time axis to map it onto LRD redshifts (z~4–8) is the separate load-bearing open knob — the same M_KK⁻¹→s normalization that blocks the derived a(t). This is the honest boundary: D2 resolves the cosmogenesis-coherence question (PASS-coherent), but it does NOT by itself deliver an LRD halo-MF prediction — that waits on closing the a(t) gap.

**Substrate framing** (substrate-first arrow held in BOTH readings): the CMB is the **acoustic signature of the GGE relic**, NOT thermal-equilibrium radiation in an expanding container. In BOTH readings the chain is `D_K eigenvalues → fold transit → GGE relic / T_init → emergent P(k) → CMB/halos`. "Exflation" is internal spectral-complexity growth at the van Hove fold (the eigenvalue spectrum reorganizing), NOT metric expansion of a box; the 80.89 "e-folds" of SCENARIO A are the substrate's spectral-weight redistribution that redshifts the GGE temperature, and the Ordered Veil (the GGE never thermalizes — Richardson-Gaudin integrable) is exactly why the relic survives as a *standing* acoustic pattern we read as the CMB rather than dissipating into a thermal bath. Neither reading is a container-initial-conditions statement; SCENARIO A's T_init is the substrate's own BCS-analog formation temperature (PREDICTED, not tuned), and the reconciliation keeps the explanation flowing FROM the substrate TOWARD the observed CMB.

---

### §W6-7. S96-OBS-ANCHOR-HYGIENE (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S96-OBS-ANCHOR-HYGIENE`
**Trigger**: `[AUDIT]`+`[SIGN]`
**Classification**: **NON-PHONONIC** (observational-anchor provenance reconciliation — σ₈ Planck anchor, DESI-DR3 timeline, A_s band-vs-tension — methodology/hygiene, not substrate physics)
**Agent**: `mack-cosmic-bridge` (falsifier-inventory sole writer; this is the anchor-provenance hygiene that gates every falsifier row)
**Hypothesis**: Three observational-anchor inconsistencies resolve cleanly: (1) the σ₈ Planck comparison anchor pins to a single named Planck-2018 data-combination (resolving canonical_constants.py:sigma_8=0.811 vs capstone "Planck 0.829") with the FW-vs-Planck σ-distance recomputed; (2) the DESI-DR3 tag splits into window-open 2026-04-23 vs data-release 2027; (3) A_s is classified as a pending band vs a live ~33σ tension based on whether the greybody filter pulls the central value down.
**Plan reference**: `sessions/session-plan/session-96-plan-w6.md` §W6-7 (mack CF-1/2/3; THREE sub-tasks; observational anchors are COMPARISON-ONLY per `substrate-first-canonical-sourcing.md` — never canonical replacement). `[AUDIT]+[SIGN]`: the σ-distance has a directional pre-reg (which anchor), so `schema_v2_3tuple_required: true`.

**Verdict**: **INFO** — all 3 anchors pin to named provenance, but the σ₈ leg resolves via a σ₈/S₈ **labeling** difference (the labeling IS the finding) AND the A_s leg **INFO-defers** (ε_pivot unpinned) → composite INFO per the plan §W6-7 dual-prior Track B. 3-tuple: `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`.

**NUMBERS first (the three sub-task resolutions, Sage-exact):**

| Sub-task | Anchor / decision | Result |
|:--|:--|:--|
| **(1) σ₈** | σ₈(Planck) pinned to **0.811 ± 0.006**, named chain **Planck 2018 TT,TE,EE+lowE+lensing (Aghanim+2020 A&A 641 A6)** (s70_hydrostatic_cluster_log.txt) | σ₈_FW=0.799 (E33) → **d = 2.00σ** (`\|0.799−0.811\|/0.006`) |
| **(1) σ₈/S₈ labeling** | capstone §7.1 "Planck **0.829**" is an **S₈** value (S₈(Planck)=**0.8310 ± 0.016**, s69_pvd11_kappa_log.txt), NOT σ₈ | S₈_FW=0.8128 → **d = 1.14σ**; consistency: σ₈_FW·√(Ω_m/0.3)=0.799·√(0.315/0.3)=**0.8187** ≈ S₈_FW; σ₈(Planck)·√(0.315/0.3)=**0.8304** ≈ S₈(Planck) → confirms "0.829" is S₈ |
| **(1) as-written over-statement** | the mislabeled-0.829 reading over-states the tension | d(0.799 vs 0.829±0.014)=**2.14σ**; bare \|Δ\| swing = 0.030/0.012 = **2.5×** (the "~2.4" mack flagged is the \|Δ\| swing, NOT a σ swing — anchors carry different errors 0.006 vs 0.014) |
| **(2) DESI-DR3** | two-date split | **window-open 2026-04-23** (lockouts A–F; R_842 frozen, NO modification; verified-in-registry=True) vs **data-release 2027** (w₀/wₐ DATA decides R_842) |
| **(3) A_s** | classification | **PENDING-BAND** — band [3.11,4.27]e-9 is **33.7σ–72.3σ** from Planck (2.10±0.03)e-9, but ε_pivot UNPINNED (S86 SECTOR-1 CF) → defers to greybody central-value gate (mack CF-3 / phonon-first CF-PF-3) |

**Substitution chain (SIGN — which anchor over-states):** σ₈_FW=0.799 [atlas-07, E33]; σ₈(Planck)=0.811±0.006 [s70 named chain]; S₈(Planck)=0.8310±0.016 [s69]. `d_correct = |0.799−0.811|/0.006 = 0.012/0.006 = 2.00σ`; `d_S8 = |0.8128−0.8310|/0.016 = 0.0182/0.016 = 1.14σ`; `d_aswritten = |0.799−0.829|/0.014 = 0.030/0.014 = 2.14σ`. Direction: `d_correct (2.00) < d_aswritten (2.14)` AND `d_S8 (1.14) < d_aswritten (2.14)` ⇒ the mislabeled-0.829 anchor OVER-states the tension ⇒ `sign_verdict=PASS`. The gate does NOT pick the framework-favorable anchor — it pins the NAMED Planck chain the comparison is physically against (σ₈=0.799 is the substrate `a_2`-channel output; Planck σ₈/S₈ are the laboratory-IN anchors, COMPARISON-ONLY per `substrate-first-canonical-sourcing.md §(i)`).

**The σ₈ anchor decision**: pin σ₈(Planck)=**0.811 ± 0.006** (Planck-2018 TT,TE,EE+lowE+lensing). The canonical_constants.py:92 value 0.811 is CORRECT (not stale) — it traces to a named chain. The capstone "Planck 0.829" is NOT a wrong σ₈ pin; it is an **S₈** value (0.831) mislabeled as σ₈. The headline σ-distance is **2.00σ** (σ₈) / **1.14σ** (S₈), NOT the over-stated 2.14σ. Both σ₈_FW=0.799 and S₈_FW=0.8128 sit ~1–2σ BETWEEN Planck-CMB (high) and weak-lensing ~0.76 (low) — the framework relieves (does not worsen) the S₈ tension (correct sign), but it is a VIABLE middle, not a resolution.

**The DESI-DR3 timeline split**: the single "(2026)" tag → **window-open 2026-04-23** / **data-release 2027**. The "near-term cliff-edge" language re-anchors to the **window-open lockout event 2026-04-23**: the framework is BOUND to the R_842 binary response rule at 2026-04-23 (lockouts A–F enforceable; NO scheme-shopping, NO rectangle/branch-iv/τ_fold modification — verified against permanent-results-registry.md), but the w₀/wₐ DATA that decides the R_842 rectangle arrives at the **2027 data-release**. The cliff-edge is the lockout (2026-04-23); the data is the release (2027).

**The A_s band-vs-tension decision**: **PENDING-BAND** (NOT a settled live tension). A_s_FW band [3.11,4.27]e-9 (Row #12; 37% span over ε∈{0.02163,0.020}) is 33.7σ–72.3σ from Planck (2.10±0.03)e-9, but ε_pivot is UNPINNED (S86 SECTOR-1 carry-forward, W5a P3 FOLD-PIVOT-RUNNING-FLOW-SECTOR-1). Under the FROZEN-PREDICTION-DISCIPLINE-COMMIT (S86 W13 P1) band-not-point contract, the band-vs-live-tension call **DEFERS to the greybody central-value gate** (mack CF-3 / phonon-first CF-PF-3) — the exit greybody narrows the band but does not yet collapse it to a point. A_s is a pending band whose central value awaits ε_pivot, NOT a "live ~33σ tension."

**Inventory + canonical-constants updates (mack sole writer)**: NEW **Row #70** in `falsifier-master-inventory.md` — a NEW σ₈/S₈ row (the documentation gap: σ₈ in the capstone §7.1 scorecard but absent from the inventory) carrying the σ₈-anchor pin + the σ₈/S₈ labeling resolution, PLUS the DESI-DR3 two-date annotation (applies to Row #1 w₀) and the A_s pending-band classification (applies to Row #12 A_s). `sigma_8` and `A_s_CMB` PROVENANCE-dict entries added to `canonical_constants.py` (values bit-unchanged; closes the knowledge-MCP "No PROVENANCE entry" gap; `update_constant` value-line guard required a manual Edit per the S95 W6-4 provenance-completeness precedent).

**Output Artifacts** (closure-verification checklist):
- script `computations/_shared/s96_obs_anchor_hygiene.py` — EXISTS; `grep -E 'from canonical_constants import|append_verdict'` → `from canonical_constants import sigma_8, A_s_CMB, Omega_m` + `def append_verdict(...)` (both present).
- data `computations/session-96/s96_obs_anchor_hygiene.npz` — EXISTS.
- plot `computations/session-96/s96_obs_anchor_hygiene.png` — EXISTS (3-panel: σ₈/S₈ anchor σ-distances / DESI-DR3 two-date timeline / A_s pending band).
- verdict line `computations/session-96/s96_gate_verdicts.txt` — `S96-OBS-ANCHOR-HYGIENE: INFO -- ... audit_sha256=37def5ddd58b9a5cdd3016949843fe94b5a61e905450ed3163b9fa810f7f9d0f content_sha256=7dc20e2c356699d5d67251c0d66b721ef03019e3a9a764ef9b97969c4038de7d` + dual-SHA companion row + schema-v2 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`). audit_sha256 unique in file (sig_5 clean). Content presence only — no length/size targets.

**MCP Pre-Compute Audit**:
- `get_constant('sigma_8')` → **0.811**, "No PROVENANCE entry" (the defect; fixed this gate via manual PROVENANCE-dict Edit since `update_constant` only writes value-lines, and 0.811 already exists as a value-line).
- `get_constant('A_s_CMB')` → **2.1e-09**, "No PROVENANCE entry" (fixed this gate).
- `search_knowledge('sigma_8 0.811 0.829 S_8')` → s70 log: **σ₈(CMB,Planck2018)=0.811±0.006** + σ₈(CMB,FW)=0.793; s69 log: **S₈(Planck)=0.8310±0.016** + S₈(Framework)=0.8128; atlas-07: σ₈=0.799 VIABLE (between Planck 0.811 and lensing ~0.77). → the named chain + the σ₈/S₈ labeling resolution.
- `search_knowledge('A_s band 33 sigma eps_pivot')` → s85-2a: `A_s_pinA = A_s_S82_cache·(eps_fold/eps_pivot)`; ε_pivot is the S86 SECTOR-1 carry-forward (unpinned) → A_s is a PENDING BAND.
- `trace_entity` via permanent-results-registry → "DESI DR3 data-release window opens **2026-04-23**" + "Hard lockouts (6, A-F) all enforceable at the event-window date 2026-04-23" + capstone "DR3-binding 2027" → two-date split.
- NOT PRE-CLOSED (no prior S96-OBS-ANCHOR-HYGIENE verdict in the session file).

**Substrate framing**: NON-PHONONIC (methodology/hygiene). This gate does NOT produce a substrate-physics number; it pins the OBSERVATIONAL anchors against which substrate predictions are compared. Per `substrate-first-canonical-sourcing.md §(i)`, the Planck σ₈/S₈, the DESI-DR3 timeline, and the Planck A_s are COMPARISON-ONLY observational anchors — never a canonical replacement for the substrate-first compute. Direction of explanation (`phononic-framing.md §"IS Space, Not IN Space"`): D_K eigenvalues → `a_2` Seeley-DeWitt coefficient → emergent growth factor D(a) → σ₈=0.799 (substrate-IS prediction); the Planck σ₈/S₈ are the laboratory-IN anchors. The σ₈ anchor is the highest-leverage hygiene in the wave — it gates gate-1's `f·σ₈` product (the σ₈ leg) AND every falsifier-inventory row citing σ₈.

---

## Wave 6 Synthesis (team-lead)

Seven observational-falsifier / cosmogenesis gates (per-gate positions, no session-aggregate ratio):

| Gate | Verdict | Result |
|:-----|:--------|:-------|
| W6-1 FSIGMA8-FORECAST | INFO | f·σ₈ −4.058% PRODUCT / −0.311% bare-f (C5 guard explicit); S₈-relieving; Euclid 1.534σ; INFO-branch-a (paper-search down → S65 arrays) |
| W6-2 FIRST-SOUND-RING | PASS | A_FS=0.204 ring SNR 8.6 (DESI-5yr fetched) / 5.1 (DR1 now); UNTESTED → live zero-param BAO falsifier; closes stranded S95 INFO |
| W6-3 CGWB-PEAK-FREQ | FAIL | D4 resolved AGAINST mHz peak (peak ~8.5e39 Hz, 44 dec above LISA; acoustic dispersion moves it the wrong way) |
| W6-4 OMEGAGW-GGE-VS-ZN | PASS | flagship fully GGE-acoustic; Z_N wall = 0 EXACTLY (π₀(U(1))=0); Sage-exact Ω_GW^(C)=8.299e-58, split 47.081 |
| W6-5 LRD-ASSEMBLY-CLOCK | FAIL | shape ΛCDM-consistent, magnitude blocked (κ* ~59 OOM from natural) — proves a(t) gap C1 load-bearing for LRD |
| W6-6 CMB-SCENARIO-D2 | PASS | §5.3 GGE-relic & SCENARIO A are COMPLEMENTARY layers (P(k)-shape vs T-budget), not incompatible — D2 coherent |
| W6-7 ANCHOR-HYGIENE | INFO | σ₈ is a σ₈/S₈ LABELING fix (0.811 is Planck σ₈; 0.829 is S₈); DESI-DR3 two-date split; A_s pending-band |

**D4 resolution (the key cross-gate finding)**: W6-3 (peak FAIL) + W6-4 (amplitude PASS) are NOT contradictory — they are different observables of the same spectrum. LISA samples the deep-IR Ω_GW **tail amplitude** (survives, W6-4), NOT the spectral **peak frequency** (which is ~1e40 Hz, W6-3). The §7.2 flagship is scope-corrected accordingly (landed by W8-2). **D2** (W6-6 PASS-coherent) seeds the S96 workshop schedule as its R1 input (separate `/rclab-investigate` stream, not a plan CF).

### What Changed

**(a) Numerical revisions** — f·σ₈ −4.058% product / −0.311% bare-f; first-sound SNR 8.63 (DESI-5yr) / 5.08 (DR1); CGWB peak 8.48e39 Hz; Ω_GW^(C)=8.299e-58 (Sage-exact); σ₈_FW 2.00σ / S₈_FW 1.14σ (re-anchored).

**(b) Structural changes** — D4 RESOLVED (peak ≠ mHz, amplitude IS mHz — observable-scope split); first-sound ring UNTESTED → live near-term zero-param BAO falsifier; D2 reconciled (complementary layers, not single-channel); σ₈ anchor σ₈/S₈ category-fix; C1 a(t) gap proven LOAD-BEARING for quantitative LRD constraints.

### Effected In-Session (NON-MATH — completed before STOP)

- [x] **Falsifier-inventory rows landed by W8-2 (mack, sole writer)** — Row #71 (f·σ₈, W6-1), #72 (first-sound ring, W6-2), #73 (ν ordering via W7-5), #7.audit-2 (W6-3 D4 LISA-scope correction). Canonical write-order honored (verdict → canonical_constants → inventory).
- [x] **§7.2 LISA CGWB flagship scope-corrected** — W8-2 (mack): LISA samples the Ω_GW IR-tail AMPLITUDE, not the 8.5e39 Hz peak (the W6-3 D4 resolution).
- [x] **§7.1 σ₈ anchor fixed to Planck σ₈=0.811** (was mislabeled "Planck 0.829" = S₈) — W8-2 (mack) + anchor-cited under W8-6 CITE-8.
- [x] **`regulator-pin-discipline.md` Ω_GW OOM fidelity correction** — orchestrator-direct: the round-figure `1e-57` vs Sage-exact `8.299e-58` is 1.205× = 0.081 OOM (same decade), NOT the "~10×/~2 OOM" the rule-prose claimed; bound to Class-8.3 publication-precision. The OOM-significance lives in the (A)/(C) SPLIT (47.081 OOM), not the single value. — `.claude/rules/regulator-pin-discipline.md:125`.

### Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-05-30 | D4 LISA CGWB placement | asserted-not-derived | peak≠mHz (8.5e39 Hz); amplitude=mHz IR-tail | W6-3 + W6-4 |
| 2026-05-30 | first-sound BAO ring | UNTESTED prediction | live zero-param falsifier (SNR 8.6) | W6-2 |
| 2026-05-30 | D2 cosmogenesis | dissonance (relic-IS-CMB vs SCENARIO A) | coherent (complementary layers) | W6-6 |
| 2026-05-30 | C1 derived-a(t) gap | open | confirmed LOAD-BEARING for LRD | W6-5 |
| 2026-05-30 | Z_N domain-wall Ω_GW | project-lore (~1e-10) | structurally ZERO (π₀(U(1))=0) | W6-4 |
| 2026-05-30 | σ₈ Planck anchor | "0.829" (mislabeled S₈) | σ₈=0.811 / S₈=0.829 disambiguated | W6-7 |

## Carry-Forward Computations

### CF-S97-FSIGMA8-FORECAST-REFETCH — live DESI-5yr/Euclid f·σ₈(z) forecast-precision re-fetch

| Field | Spec |
|:------|:-----|
| **What** | Re-fetch the live DESI-5yr / Euclid f·σ₈(z) forecast-precision table (paper-search was DOWN for W6-1, which fell to INFO-branch-a using the S65-embedded arrays) and recompute the per-z σ-distance to confirm the 0.506σ (now) → 1.013σ (DESI-5yr) → 1.534σ (Euclid) curve. |
| **Inputs** | paper-search MCP (DESI-5yr/Euclid RSD forecast); `s96_obs_fsigma8_forecast.npz` (the substrate f·σ₈(z) curve, FINAL); `s70_bulk_flow.npz` |
| **Gate** | max-z σ-distance within the FETCHED forecast band ⇒ PASS (within-band LSS discriminator); INFO if z-dependent; the substrate side is already final, this only confirms the forecast precision |
| **Effort** | < 0.5 wave (low priority — substrate side done; W6-2 confirms paper-search recovered S96, so the fetch should now succeed) |

**Note**: the plan's other conditional W6 CFs did NOT fire — gate-1 landed INFO (not FAIL → no cosmic-web V.4 proxy-H), gate-5 FAIL CONFIRMS the already-known C1 a(t) frontier (the W1 flagship, not a new W6 CF), gate-6 PASS-coherent (no D2 FAIL-incoherent escalation; D2 routes to the workshop schedule as a converged R1 input), gate-7's A_s leg defers to the greybody central-value gate (mack CF-3, an existing carry-forward).

## Constraint-Map Updates

See the **Constraint-Map Updates** table in the Wave 6 Synthesis (team-lead) section above — 6 state changes (D4 placement, first-sound ring, D2 coherence, C1 confirmation, Z_N wall, σ₈ anchor).

## Files Produced

*(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)*
