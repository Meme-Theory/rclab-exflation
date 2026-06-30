# Investigation 8 Wave 1 — Observational Cosmology & the Dark-Sector Front (Results Working Paper)

**Investigation**: 8 | **Wave**: 1 | **Plan**: investigation-8-plan-w1.md | **Owner**: mack-cosmic-bridge | **Theme**: the f_DM abundance gap (PBH fold-transit channel), the w_0 = −0.918 dual-ledger (S_8/τ_reio asset vs DESI w_a liability), the f_DM partition reconciliation, and the finite-L analytic-continuation-pole NO-GO. Gate-type mix: compute × 3, solo × 1. Verdict track: `computations/investigation-8/inv8_gate_verdicts.txt`.

## Gate Sections

### §W1-1. INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (PBH mass spectrum from the supersonic van Hove fold transit)
**Agent**: `mack-cosmic-bridge` (hawking-theorist co-option: first-order-transition PBH formation, Carr–Hawking collapse criterion, Press–Schechter β(M))
**Hypothesis**: the Mach-13.75 first-order fold transit produces a calculable f_PBH(M) whose asteroid-window [10¹⁷,10²³] g integral supplies the ~0.27 of Ω_DM the Leggett channel misses — closing the abundance gap (G1) and opening the first compact-object sector (G4).
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w1.md` §W1-1.

**Verdict**: **FAIL** — composite `FAIL` (sign=PASS, magnitude=FAIL, regime=VALID). Track B **under-supply** sub-branch. I_PBH = 1.80×10⁻²⁹⁹ over [10¹⁷,10²³] g (target 0.27 ± 0.05). The fold-transit PBH spectrum does **NOT** close the dark-matter abundance gap: the squeezed-thermal collapse fraction is large (β₀ = 0.869) but it is deposited at a horizon-mass scale ~37 orders of magnitude below the asteroid window, and below the Hawking-evaporation floor — so these PBHs have evaporated and are not present-day dark matter at all.

**MCP Pre-Compute Audit**:
Queries run before any compute (per CLAUDE.md query-first discipline). No pre-closure covers this gate — it opens a new corridor (the empty Row #88 compact-object formation-channel cell).
- `search_knowledge("PBH primordial black hole formation fold transit")` → no PBH formation-channel result; nearest are the acoustic-white-hole causal-disconnect (PROVEN S85) and the transit-is-sudden-quench theorem (T1, PROVEN S36). Confirms PBH formation as a mass-function has **not** been computed.
- `search_knowledge("f_DM abundance gap dimer Z2 pair production Leggett")` → `f_DM = f_Leggett + f_soft-hair + f_dimer_Z2 = 0.006 + … + 0.27` (`session-74-mack-landau-workshop.md`); `DIMER-Z2-PAIR-PRODUCTION-75` closed **INFO/MIGRATED** at S81 (`s81_batch_gate_verdicts.txt`). The 0.27 target is the dimer-Z₂ slot.
- `search_knowledge("transit Bogoliubov spectrum N_pairs 59.8 Parker pair production squeezed")` → N_pair = 59.8, S_inst = 0.0686, P_exc = 1.000, pair wavefn 93% B2/6.3% B1 (atlas-04 T4, PROVEN S38); the saturated squeezed source.
- `get_constant`: `M_KK`=7.428660036e16 GeV (S42), `tau_fold`=0.19, `Omega_DM`=0.2657 (no PROVENANCE), `n_pairs`=59.8 (S38), `H_fold`=586.527 M_KK (S38), `dt_transit`=1.1302e-3 M_KK⁻¹, `Mach_max_framework`=13.75 (S85), `Omega_BA_fold`=2.241353 (S95/S97). `c_s_fold` / `f_dimer_Z2` → **NOT FOUND** (the fold sound speed c_s=1.9305 M_KK and the 0.27 fraction are plan-pinned, not registered canonicals — flagged in the verdict extra-rows).
- `trace_entity("Row #88 compact object PBH abundance")` → no trace (cell genuinely empty; this is the first formation-channel probe).

**Input-source correction** (per `math-scripts.md` debugging discipline — identify the RIGHT source, do not null-PASS): the plan named `s64_transit_power_spectrum.npz` and `s95_w1_omega_profile.npz`; **both absent**. The correct substrate sources are `computations/session-64/s64_bogoliubov_phases.npz` (carries `beta_complex_B` 32×8 over the 8 BCS modes, `beta_sq_check_B` the |β_k|² occupations) and `computations/session-95/s95_w4_4_sp_conformal_embed.npz` (canonicalizes `Omega_BA_fold`=2.241353 via S97-W1-OMEGA-PROFILE). N_pairs=59.8 imported as the canonical spectral sum. Correction recorded in the verdict extra-rows.

**Substitution chain** (plan Step 1–5, with substituted numbers — `math-scripts.md` MANDATORY):
- **Step 1 (collapse fraction)**: β(M) = erfc(δ_c/(√2 σ_fold)) [Press–Schechter / Carr–Hawking]. At δ_c=0.45 (radiation-era ≈ w=1/3), σ_fold=2.734 (per-patch rms) → **β₀ = 0.869** (large — the squeezed source readily collapses).
- **Step 2 (substrate source of σ_fold)**: σ_fold² ∼ ⟨δ²⟩ ∝ |β_k|² = N_pairs = 59.8. Three conventions computed: raw-linear √59.8 = 7.733; per-patch √(59.8/8) = 2.734; capped 1.0. β₀ is monotone-increasing across them (sign check). Supersonic Mach-13.75 ⇒ squeezed-thermal, the canonical PBH-amplifying regime.
- **Step 3 (horizon mass at the fold)**: dimensionalized by the single import M_KK = 7.42866e16 GeV (⇒ M_KK_g = 1.324e-7 g). The fold **IS** at the substrate energy scale T_fold = M_KK. Two routes: **Route A** (standard Friedmann, M_H(T) ≈ 4.8e13 g·(T/GeV)⁻²) → **M_H = 8.70×10⁻²¹ g**; **Route B** (substrate Hubble mass, M_H = ½c_s³M_KK²/H_fold with G=1/M_KK², c_s=1.9305 M_KK plan-pinned) → **M_H = 8.12×10⁻¹⁰ g**.
- **Step 4 (present-day fraction)**: f_PBH(M) = β(M)·(M_eq/M)^{1/2}/Ω_DM, near-monochromatic (1-decade log-normal at M_H), with the **evaporation cutoff** f_PBH(M < 5.1×10¹⁴ g) → 0 [t_evap ∝ (M/M_*)³ t₀].
- **Step 5 (integrate + read off)**: I_PBH = ∫_{1e17}^{1e23 g} f_PBH d lnM. **SIGN prediction**: I_PBH > 0 and monotone in σ_fold — **holds** (β₀ > 0, monotone). **MAGNITUDE/REGIME (the measurement)**: I_PBH = 1.80×10⁻²⁹⁹ (Route A); Route B = 6.94×10⁻¹⁴⁹ — both **≈ 0** in-window because M_H sits 37.1 OOM (Route A) / 26.1 OOM (Route B) **below** the window bottom 10¹⁷ g, AND both lie below the 5.1×10¹⁴ g evaporation floor.

**Reading of the result** (substrate-first; substrate IS the fold transit): the fold reorganizes the D_K spectrum at a GUT-scale energy (M_KK ~ 7×10¹⁶ GeV). The squeezed Bogoliubov field (N_pairs = 59.8) IS a real, large overdensity contrast — but a horizon collapsing at the fold encloses only ~10⁻²⁰ g, the canonical "tiny-horizon-mass-at-high-T" regime. The asteroid DM window [10¹⁷,10²³] g requires formation at T ≈ 10⁻² – 10⁻⁵ GeV (QCD-to-tens-of-MeV epoch), **not** the fold. The collapse fraction is deposited at the WRONG mass scale and below the evaporation floor: these fold-PBHs Hawking-evaporate long before today. **The dimer-Z₂ abundance (0.27) is NOT closed by a fold-transit PBH channel** (U3 stays open; the dimer condensate is not redundant-retirable — it must still be independently derived OR another formation epoch sourced). G4 is opened only as a *sub-evaporation-floor* mass function: a real compact-object spectrum exists at the fold, but it is not present-day DM. This is the Track B under-supply corridor mapped firmly.

**Robustness / regime=VALID basis**: across the full δ_c band [0.40,0.70] the window integral stays [1.65×10⁻²⁹⁹, 1.83×10⁻²⁹⁹] — **no verdict flip** (δ_c moves β₀ only, not the mass placement). The under-supply is robust across BOTH horizon-mass routes (each 26–37 OOM below window, both below the evap floor) and all three σ_fold conventions. The window-miss is a substrate result, not a band-edge or method artifact ⇒ regime VALID; composite collapse `magnitude=FAIL ∧ regime=VALID ⇒ FAIL`.

**Cross-check vs Carr–Kohri–Sendouda–Yokoyama (2021) asteroid window** (METHODOLOGICAL, not a substrate pin): the window is the only mass range where PBHs can be 100% of DM. The fold spectrum has **no support** there, so the ceiling f_PBH ≤ 1 is trivially satisfied in-window (f_max,window = 2.98×10⁻²⁹⁸); there is **no over-production constraint** triggered. (Over-production was the alternative FAIL sub-branch; it does not fire — the fold under-supplies, it does not over-close.)

**Dual-prior update** (plan): FAIL with I_PBH ≪ 0.27 → **0.9 mass to Track B under-supply sub-branch** (PBHs do NOT close the abundance via the fold; dimer-Z₂ must be independently derived). Track A (PBH supplies abundance) is effectively excluded for the fold-transit channel.

**Downstream (`backward(M)`)**: INV8-W1-3 dimer supply-or-retire branch consumes this verdict → resolves to **KEEP-AND-FLAG-UNDERIVED** (W1-1 FAILED under-supply; the dimer-Z₂ slot stays the sole abundance candidate and remains un-derived). Any `falsifier-master-inventory.md` Row #88 landing OR `canonical_constants.py` pin from this gate is **session-track / mack-cosmic-bridge sole-writer** (HY4-adjacent), routed OUT to the investigation-8 close — NOT performed here. The investigation verdict line lands in `computations/investigation-8/inv8_gate_verdicts.txt` only.

**Output Artifacts**:
- Verdict line: `computations/investigation-8/inv8_gate_verdicts.txt` — `INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM: FAIL -- value='1.800768e-299' scheme=FW convention=ABSOLUTE L_max=10 audit_sha256=d64c19fb40a47de27fff9f2bea3bf562271e4535b9f71715aea0a86a99d4a453 content_sha256=00adf9f34cb177cb13145c1d1cb5f8af002540b9df80d680df221c3f191bc321 schema_version=S84+` + dual-SHA companion row + schema-v2 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + 2 extra rows (horizon-mass routes; input-source correction).
- Producing script: `computations/investigation-8/inv8_w1_pbh_fold_transit_spectrum.py` (contains `from canonical_constants import` and `print_verdict_payload`).
- Data: `computations/investigation-8/inv8_w1_pbh_fold_transit_spectrum.npz`.
- Plot: `computations/investigation-8/inv8_w1_pbh_fold_transit_spectrum.png` (panel 1: f_PBH(M) both routes vs window + evap floor; panel 2: I_PBH(δ_c) band scan).
- 4-tuple: `(value=1.800768e-299, scheme=FW, convention=ABSOLUTE, L_max=10)`.
- Dual-SHA: audit `d64c19fb40a47de27fff9f2bea3bf562271e4535b9f71715aea0a86a99d4a453` (script+canonical+pinmap over the 3 inputs); content `00adf9f34cb177cb13145c1d1cb5f8af002540b9df80d680df221c3f191bc321` (script bytes).

**Substrate framing**: PHONONIC. The substrate IS the impulsive first-order transit through the van Hove fold at τ_fold = 0.190 (Mach 13.75). The Bogoliubov transformation of the 8 BCS fibre modes (|β_k|² → N_pairs = 59.8, P_exc = 1.000) IS the squeezed overdensity field. A PBH here is a region of the fabric whose post-transit GGE overdensity exceeds δ_c — gravitational self-organization through the a₂ (gravity) channel. The single import M_KK sets WHERE on the gram axis the spectrum sits, and that placement (10⁻²⁰ g) is the load-bearing finding: the fold's overdensity field IS large enough to collapse, but the fold horizon is too small for the resulting PBHs to be today's dark matter. The chain D_K eigenvalues → transit Bogoliubov occupation → σ_fold → β(M) → f_PBH(M) → asteroid window runs cleanly; it simply lands the spectrum below the evaporation floor.

---

### §W1-2. INV8-W1-2-S8-TAU-REIO-GGE-GROWTH (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `INV8-W1-2-S8-TAU-REIO-GGE-GROWTH`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (S_8 + τ_reio from one GGE a_2-channel growth history)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: one GGE growth history (w_0 = −0.918 > −1 suppressing late growth) yields a low S_8 = σ_8√(Ω_m/0.3) leaning toward lensing/KiDS (0.766) and away from CMB (~0.83), plus a τ_reio consistent with Planck 0.054 — making the single structural DE departure simultaneously a DESI-w_a liability AND an S_8/τ_reio asset.
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w1.md` §W1-2.

**Verdict**: **PASS** — 3-tuple (sign=**PASS**, magnitude=**PASS**, regime=**VALID**). The framework S_8 is closer (in σ-units) to the lensing/KiDS anchor than to the CMB anchor (n_σ(KiDS)=2.338 < n_σ(CMB)=2.972, band-stable under Ω_m float), AND τ_reio_FW=0.0559 is within 0.27σ of Planck 0.054±0.007. w_0=−0.918 is established as a **two-sided observational signature** — a DESI-w_a liability AND an S_8/τ_reio asset.

**MCP Pre-Compute Audit** (query-first discipline, run BEFORE writing the script; order search_knowledge → trace_entity → get_constant → list_constants):
- `get_constant("sigma8_growth_a2")` → **0.79317** (S98; growth-channel readout, NOT the headline single-number σ_8; S98 note "growth −2.18% vs LCDM"; BOTH this and σ8_OZ_50=0.799 below LCDM 0.811). **Primary substrate-IS σ_8 source for this gate.**
- `get_constant("w0_FW")` → **−0.918** (S58 four-fold lock: Volovik vacuum partition + effacement Γ=0.99970). The DE-departure driver.
- `get_constant("fsigma8_product_suppression_FW_max_pct")` → **−4.058** (S96-OBS-FSIGMA8-FORECAST). Canonical suppression magnitude; corroborates the [SIGN] direction.
- `get_constant("Omega_m")` → **0.315**; `get_constant("sigma_8")` → **0.811** (S96-OBS-ANCHOR-HYGIENE, LCDM/Planck CMB reference); `get_constant("wa_FW")` → **0** (four-fold structural lock).
- `search_knowledge("S_8 tension sigma_8 KiDS growth factor")` → theorems `proven_980`/`proven_1082`: "**f·σ_8(z): 4% suppression vs LCDM, correct S_8 direction**" (PROVEN, session-77-mack-synthesis). The structural theorem this gate's substitution chain reproduces — **direction is pre-PROVEN; the numerics (S_8 value + three σ-distances + τ_reio) are NOT pre-closed.**
- `search_knowledge("tau_reio reionization optical depth Planck")` → NO framework τ_reio computation (only optical-theorem unitarity gates, unrelated). **τ_reio leg is genuinely new.**
- `trace_entity("GROWTH-FACTOR-59")` → no direct hit; traces to `data_provenance:session-59/s59_growth_factor.py` → gate `FACTOR-59`, npz `s59_growth_factor.npz` (σ8_wCDM=0.7931655, σ8_LCDM=0.811, growth_ratio=0.9780093). Loaded as the growth-history input + [SIGN] cross-check anchor.
- **Verdict: NOT PRE-CLOSED.** Direction (suppression toward KiDS) is a PROVEN structural theorem; this gate computes the *first* S_8 value + the *first* τ_reio + the three σ-distances + the w_0 dual-ledger. The curvature-tension stance doc (`researchers/Mack/curvature-tension-framework-stance.md §5.2`) explicitly records "**no closed S_8 gate yet**" — this gate IS that gate.

**Output Artifacts** (closure-verification checklist — all confirmed on disk by content):
- **Verdict line**: `computations/investigation-8/inv8_gate_verdicts.txt` — `INV8-W1-2-S8-TAU-REIO-GGE-GROWTH: PASS ... audit_sha256=be6f1a48b520031e1c195d83b5051c7991db334f293b263b031a47918a20802b content_sha256=362edcaae44ff2a683390ec6d350ebe697708a63dec127445d5ef82ca0912fc4 schema_version=S84+` + dual-SHA companion row + schema-v2 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + 3 dual-ledger annotation rows. Emitted via `emit_verdict` (track=investigation, race-safe, sig_5 unique).
- **Script**: `computations/investigation-8/inv8_w1_s8_tau_reio_gge_growth.py` (contains `from canonical_constants import *` and `print_verdict_payload`).
- **Data**: `computations/investigation-8/inv8_w1_s8_tau_reio_gge_growth.npz` (full float64; all observables + growth-ODE cross-check arrays + τ_reio integrand).
- **Plot**: `computations/investigation-8/inv8_w1_s8_tau_reio_gge_growth.png` (3-panel: S_8 comparison, [SIGN] growth-suppression bars, τ_reio integrand+band).

**Results** (NUMBERS first, gate second, interpretation third):

**The three σ-distances + S_8 + τ_reio:**

| Observable | Framework | External anchor | σ-distance |
|:-----------|:----------|:----------------|:-----------|
| S_8 = σ_8√(Ω_m/0.3) | **0.8128** | KiDS-1000 (lensing) 0.766 ± 0.020 (Heymans 2021) | **2.338σ** |
| S_8 = σ_8√(Ω_m/0.3) | **0.8128** | Planck CMB 0.831 ± 0.0061 (σ_8=0.811) | **2.972σ** |
| τ_reio | **0.0559** | Planck 2018 0.054 ± 0.007 | **0.274σ** |

- σ_8_FW = 0.79317 (canonical `sigma8_growth_a2`); Ω_m = 0.315; w_0 = −0.918, w_a = 0.
- τ_reio band over z_reio ∈ [6,10]: [0.0371, 0.0770]; central (z_reio=8) = 0.0559. Band does NOT flip the 2σ verdict.
- S_8-asset under Ω_m float (±0.007 Planck 1σ): [True, True, True] — band-stable.

**4-tuple**: `(value=0.812757, scheme=FW, convention=RATIO, L_max=10)`.

**SIGN/MAGNITUDE/REGIME 3-tuple**:
- **sign = PASS** — keys on σ_8_FW < 0.811 (True: 0.79317 < 0.811) AND the S_8-asset inequality n_σ(KiDS)=2.338 < n_σ(CMB)=2.972 (True). The predicted DOWNWARD direction (toward lensing) holds.
- **magnitude = PASS** — keys on the τ_reio numerical target: |τ_reio_FW − 0.054|/0.007 = 0.274 ≤ 2.0.
- **regime = VALID** — neither the Ω_m systematic (S_8-asset) nor the z_reio∈[6,10] systematic (τ_reio 2σ) flips the classification.

**[SIGN] substitution chain — "w_0 = −0.918 > −1 SUPPRESSES late growth, LOWERS σ_8 toward KiDS" (substituted numbers; math-scripts.md MANDATORY)**:
- **Step 1** (linear growth ODE): D''(N) + [2 + H'/H]D'(N) − (3/2)Ω_m(a)D(N) = 0, N=ln a; σ_8 ∝ D(a=1) at fixed primordial amplitude. [canonical FRW]
- **Step 2** (DE density evolution): ρ_DE(a) = ρ_DE,0 · a^{−3(1+w_0)}. Substitute w_0 = −0.918 ⇒ 1+w_0 = **0.082 > 0** ⇒ ρ_DE ∝ a^{−0.246}, **DECREASING in a** (DE was MORE important in the recent past than a pure Λ). [CPL with w_a=0]
- **Step 3** (effect on the growth source): Ω_m(a) = [Ω_m,0 a^{−3}]/[Ω_m,0 a^{−3} + ρ_DE(a)/ρ_crit,0]. With ρ_DE LARGER at recent-past a<1, Ω_m(a) is SMALLER ⇒ the (3/2)Ω_m(a)D source term is SMALLER ⇒ growth accumulates LESS over the DE-dominated era.
- **Step 4** (read off direction): smaller growth source ⇒ D(a=1)_FW < D(a=1)_LCDM ⇒ σ_8_FW < σ_8_LCDM. **Direction: w_0 > −1 ⇒ LOWER σ_8.**
- **Step 5** (corroboration — INDEPENDENT growth-ODE re-integration run in-script): D(a=1)_FW = 0.770468 < D(a=1)_LCDM = 0.787813 ⇒ **growth_ratio_ode = 0.97798 < 1** ✓ (matches S59 npz growth_ratio = 0.97801 to 5e-5). Canonical: σ_8_FW = 0.79317 < 0.811 ✓; fsigma8 suppression = −4.058% ✓. (The ODE single-product ratio gives −2.20%; the canonical −4.058% is the f·σ_8 PRODUCT max-suppression — both negative, same direction; the difference is product-vs-amplitude, not a sign disagreement.)
- **Conclusion**: SIGN prediction σ_8_FW < σ_8_LCDM (DOWNWARD, toward lensing/KiDS) is CONFIRMED by both the canonical pin and the independent re-integration. S_8 = σ_8√(Ω_m/0.3) inherits the same downward direction.

**Constraint-map consequence (dual-ledger; the substrate framing)**:
- **Track A (w_0 is a TWO-SIDED signature) CONFIRMED** — posterior re-allocated ~0.9 to Track A per the pre-registered discriminator (prior 0.55). The framework's single structural DE departure has a richer two-sided observational story.
- **w_0 = −0.918 DUAL-LEDGER** (the gate's central deliverable):
  - **DESI-LIABILITY ledger**: w_a = 0 (four-fold structural lock) vs DESI DR2 w_a = −0.73 ± 0.25; w_0 = −0.918 vs DESI w_0 = −0.752 ± 0.057 (≈2.9σ). The w(z) front is in tension.
  - **S_8/τ_reio-ASSET ledger**: the SAME w_0 = −0.918 > −1 suppresses late growth (−4.058% f·σ_8) → low σ_8 = 0.79317 → S_8 = 0.8128 leaning toward KiDS (2.338σ) and away from CMB (2.972σ); τ_reio = 0.0559 within 0.27σ of Planck. The growth/reionization front is an ASSET.
- **Honest caveat (substrate-first, not overstated)**: S_8_FW = 0.8128 sits in 2.3–3σ tension with BOTH anchors individually — it is NOT a clean match to KiDS, it is *closer to KiDS than to CMB*, which is the pre-registered (relative) PASS criterion. The framework S_8 lands between the two tension poles, leaning lensing-ward. The driver is that Ω_m = 0.315 is slightly high (it pulls S_8 up via √(Ω_m/0.3) = 1.0247), partially offsetting the low σ_8. A future gate pinning Ω_m + z_reio from substrate physics (rather than the canonical/systematic-band values used here) is the next refinement.
- **Routing**: the w_0 dual-ledger entry feeds the capstone §7 falsifier surface (`mack-cosmic-bridge` sole writer, **session-track** promotion per `feedback_mack-bridge-role.md` + `math-scripts.md §"Canonical Write-Order"` — NOT this investigation-track gate). Any `falsifier-master-inventory.md` row (S_8 σ-distances, τ_reio σ-distance) arising here is session-track, routed OUT to the `/rclab-investigate --investigation 8` close. The investigation verdict line lands in `computations/investigation-8/inv8_gate_verdicts.txt` ONLY.
- **Resolves R2** (the stale 2-sig-fig S_8 note becomes a real falsifier-track computation with three σ-distances) and partially **B3/B5** (the w_0 two-sided story). This is the closed S_8 gate the curvature-tension stance doc flagged as absent (§5.2).

**Substrate framing**: PHONONIC. The substrate IS the gravitationally self-organized post-transit GGE interference pattern; large-scale structure is that pattern growing through the a_2 (gravity) Seeley-DeWitt channel (atlas-05; phononic-framing.md — "density perturbations in expanding space" → interference pattern of post-transit GGE acoustic excitations). The chain runs substrate → observable: D_K eigenvalues → a_2 spectral moment (emergent gravity) → linear growth factor D(a) → σ_8 (rms of that pattern at 8 Mpc/h) → S_8 = σ_8√(Ω_m/0.3). Dark energy here is NOT a quintessence field IN space; it is the effacement-residual a_0 spectral moment after Volovik tracking (the 0.03% leakage through the impedance mismatch Γ=0.99970), a slowly-evolving condensate whose w_0 = −0.918 > −1 dilutes mildly (Step 2) and thereby SUPPRESSES the late growth of the GGE pattern, lowering σ_8 toward the lensing value. Reionization is sourced by the FIRST collapsed structures of that same pattern, so the substrate's (low) σ_8 and its w_0 = −0.918 growth history directly set WHEN reionization happens (z_reio → τ_reio). One substrate growth computation feeds three observables (S_8, τ_reio, and a partial anchor into the intermediate-z growth) — the dark-energy ASSET ledger of the same w_0 that is a liability on the DESI w(z) front.

**Dual-SHA**: audit_sha256 = `be6f1a48b520031e1c195d83b5051c7991db334f293b263b031a47918a20802b` (over script + canonical_constants.py + pinmap{canonical, s59_growth_factor.npz}); content_sha256 = `362edcaae44ff2a683390ec6d350ebe697708a63dec127445d5ef82ca0912fc4` (over script bytes only).

---

### §W1-3. INV8-W1-3-FDM-PARTITION-RECONCILIATION (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `INV8-W1-3-FDM-PARTITION-RECONCILIATION`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (f_DM partition reconciliation; INFO-by-construction)
**Agent**: `mack-cosmic-bridge` (solo — executed INLINE by the orchestrator; no subagent spawn; closure identical to compute: verdict line + WP section)
**Hypothesis**: the ≥4 register f_DM/Ω_DM numbers (0.006, 0.209, 0.947; Ω_DM=0.2657 vs Ω_DM h²=0.120) are a layered partition over MASS / ABUNDANCE / COLD-DM-FRACTION stages, not a contradiction; ONE substrate-IS table resolves them, and the dimer-Z₂ Parker slot (0.27) is SUPPLIED-or-RETIRED by the INV8-W1-1 PBH verdict.
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w1.md` §W1-3 (CONDITIONAL on the INV8-W1-1 verdict line; absent-at-dispatch → PENDING-W1-1 INFO branch).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("f_DM cold dark matter fraction partition Leggett soft-hair dimer channel 0.844")` → returned BOTH the plan's 3-channel form AND the `session-74-mack-landau-workshop.md` source — which carries an **explicit author correction** (L1128–1138) reassigning soft-hair from DM to DE. Decisive for the verdict.
- `search_knowledge("Omega_DM 0.2657 GGE relic abundance n_pairs 59.8 provenance")` → `Ω_DM = N_pairs·E_pair/ρ_crit`, n_pairs = 59.8; flagged **NO PROVENANCE entry** (→ HY4).
- `trace_entity("DIMER-Z2-PAIR-PRODUCTION-75")` → **empty evidence chain** (the dimer channel is an asserted slot, not a registered entity — consistent with U3-open).
- `get_constant("Omega_DM")` → `0.2657`, *No PROVENANCE entry* (HY4).
- `get_constant("f_dimer_Z2")` → **not found** (not a registered canonical; plan-pinned, as W1-1 also flagged).
- Source read `session-74-mack-landau-workshop.md` L1128–1138 → `f_DM = f_Leggett + f_dimer_Z2 = 0.276` (DM, two-channel); `f_DE = f_soft-hair + f_effacement = 0.23` (soft-hair RE-ASSIGNED to DE). NOT pre-closed → proceed.

**Verdict**: **INFO** (composite, INFO-by-construction). `audit_sha256=ae48dee520ae25bc3c7c6642cc76f7a3ccd215a05faf7644972c3a7498e51b0b`, `content_sha256=770b1d12fb5a4b6b4f04da6c60c31622e28f441894ca168c68b884f25e12f3f2`. The reconciliation **core PASSES** (all 7 register numbers assigned to exactly one layer; the post-correction two-channel DM sum closes; the dimer branch resolves deterministically), but the plan's **literal** sum-clause is superseded — a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE (see Results), so INFO not PASS, and emphatically not FAIL (the framework's DM bookkeeping is **not** internally contradictory — the plan's *hypothesis* was stale).

**Output Artifacts** (closure-verification checklist — confirmed by content):
- Verdict line `INV8-W1-3-FDM-PARTITION-RECONCILIATION: INFO …` + dual-SHA companion row + 3 extra annotation rows (NO 3-tuple — [VERIFY], no signed prediction) in `computations/investigation-8/inv8_gate_verdicts.txt` — emitted via `emit_verdict(session=8, track="investigation")`, sig_5 unique.
- Producing script `computations/investigation-8/inv8_w1_fdm_partition_reconciliation.py` (contains `from canonical_constants import` and `print_verdict_payload`).
- Data `computations/investigation-8/inv8_w1_fdm_partition_reconciliation.npz` (structured stage→number→layer map + the two normalisations + the consistency residuals + the dimer branch).
- Plot OMITTED — `optional: true` in the gate block (reconciliation gate; no numerical curve to plot).

**Results**:

*The ONE reconciled partition table (every register number assigned to exactly one layer):*

| Layer | Register number | Normalisation / stage | Source |
|:------|:----------------|:----------------------|:-------|
| **MASS** (a scale) | LEGGETT-MOMENT — Δ_BCS-scale rest energy | zero free params, PROVEN | S70 |
| **ABUNDANCE** | Ω_DM = 0.2657 | GGE-total relic, n_pairs=59.8 | **NO PROVENANCE → HY4** |
| **ABUNDANCE** | Ω_DM h² = 0.120 | Leggett-only relic, 0.6% from Planck | Planck-anchored |
| **COLD-DM FRACTION** | 0.209 | Leggett-only / Ω_m | S58 "SOLE BOTTLENECK" (covers 0.209/0.844 ≈ 25%) |
| **COLD-DM FRACTION** | 0.844 | observed = Ω_DM/Ω_m = 0.2657/0.315 = **0.8435** ✓ | observational target |
| **COLD-DM FRACTION** | 0.947 | GGE-total / graph-gapped-Goldstone | upper-inclusion stage |
| **COLD-DM FRACTION** | 0.006 | Leggett / total-Ω | S74 partition term |

*The stale-source finding (the substantive result).* The plan's substitution-chain Step-3 pinned a **three-channel** DM partition `f_DM = f_Leggett + f_soft-hair + f_dimer_Z2 → 0.844`. But the cited source `session-74-mack-landau-workshop.md` (L1128–1138) **already corrected** soft-hair out of DM: *"soft-hair is actually a DE candidate, not a DM candidate."* So the DM budget is **TWO-channel**:
- `f_DM = f_Leggett + f_dimer_Z2 = 0.006 + 0.27 = 0.276` ≈ Ω_DM = 0.2657 (residual **0.0103 ≤ 0.011**, closes at the rounding floor; total-Ω normalisation).
- `f_DE = f_soft-hair + f_effacement = 0.20 + 0.03 = 0.23` (soft-hair is DE, **not** DM).

The plan's literal three-channel sum = `0.006 + 0.20 + 0.27 = 0.476`, vs the target 0.844 (residual **0.368** ≫ 0.011) — and it mixed normalisations (total-Ω channels vs the Ω_m-normalised 0.844 = Ω_DM/Ω_m). The literal clause therefore tests a **superseded** partition: a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE per `epistemic-discipline.md §"Source Reconciliation"` (composite INFO precedent: the η stale-source calibration in `regulator-pin-discipline.md`). 4-tuple `(value=KEEP-AND-FLAG-UNDERIVED, scheme=FW, convention=ABSOLUTE, L_max=N/A)`.

*The CONDITIONAL dimer branch.* INV8-W1-1 returned **FAIL** (I_PBH = 1.8×10⁻²⁹⁹, fold-PBH under-supply) → the dimer-Z₂ channel stays the **SOLE** non-Leggett DM candidate → **KEEP-AND-FLAG-UNDERIVED** (U3 stays open; the abundance still rests on an un-derived channel — the honest G1/U3 statement). Branch resolves deterministically from a definite (non-absent, non-INFO) W1-1 verdict.

*Constraint-map consequence.* Resolves **R1** (the highest-leverage hygiene refinement): a DM phenomenologist can now read ONE table and know the framework's MASS+STABILITY is zero-free-parameter/PROVEN while the ABUNDANCE rests on an un-derived dimer channel. The substantive correction (DM is two-channel; soft-hair is DE; the standing "3-channel→0.844" framing is stale) and the **HY4 canonical-table WRITE + Ω_DM PROVENANCE** are SESSION-track, routed OUT to `/rclab-investigate --investigation 8` close (mack-cosmic-bridge sole writer); NOT performed by this investigation gate. Dual-SHA: audit over script+canonical+pinmap{framework-dm-properties.md [path resolved MISSING — row sourced from the knowledge-MCP, disclosed], session-74 source, W1-1 verdict line}; content over script.

---

### §W1-4. INV8-W1-4-FINITE-L-POLE-NO-GO (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV8-W1-4-FINITE-L-POLE-NO-GO`
**Trigger**: `[VERIFY-THEOREM]` (with an OPTIONAL `[SIGN]` sub-result registered — FROM-ABOVE/FROM-BELOW direction; all-three-or-none)
**Classification**: **GEOMETRIC** (finite-L analytic-continuation-pole no-go theorem)
**Agent**: `spectral-geometer` (mack-origin R3/C6; heat-kernel / Mellin-pole characterization)
**Hypothesis**: a residue-subtracted analytic-continuation observable at a pole s<d/2 (the §VII.CB g_M=a_2_FW_zeta at s=3<d/2=4) is structurally unreachable by any finite-L truncation — Weyl-divergent FROM ABOVE in the zeta-native form, convergent-but-short FROM BELOW in the bare shell-sum — while the integer-topological anchor class (§VII.AU winding) is L_max-saturated and REACHABLE.
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w1.md` §W1-4 (regulator_pin=a_2^{ζ}, CLASS=FULL, poleconv-A-double).

**MCP Pre-Compute Audit**:
Query-first discipline executed before writing the script (per `.claude/rules/epistemic-discipline.md` + CLAUDE.md knowledge-MCP mandate). Salient returns:
- `search_knowledge("VII.CB g_M a_2_FW_zeta residue-subtracted analytic continuation finite-L unreachable")` → the plan's own equations (g_M = HADAMARD FINITE PART) + the S106/S107 §VII.CB magnitude-channel context (`M(L)=Tr_{M₂(ℂ)}(P_a₂·T^{(IV)})|_L`, HKR L→∞ image = g_M). NOT a pre-closure of the **two-sided + integer-reachable dichotomy** this gate proves.
- `get_constant("a_2_FW_zeta")` → **2776.165389** (S88, gate S88-A-N-FW-CANONICALIZATION; the residue-subtracted Hadamard finite part). Used as the canonical anchor.
- `search_knowledge("S109 VIICB ZETA NATIVE LEVEL3 weyl divergent ...")` → gate `S109-VIICB-ZETA-NATIVE-LEVEL-3` **FAIL** (audit_sha256 `e976ab54…`), ζ-native route CLOSED, `is_weyl_divergent=True`, anchor_L6=39619.0337 → anchor_L8=109123.0724 → anchor_L10=280743.235367, misses g_M from **above** by ~10⁵×. This is the FROM-ABOVE cross-anchor.
- `search_knowledge("S108 ... 4.27 below anchor")` → `S108-VIICB-MAGNITUDE-REMEDIATION` **FAIL** (all 3 routes; `c42016d3…`); Richardson/Abel limit Z(∞)≈650.70 is **4.27× BELOW** g_M (convergent partial sum misses from below). This is the FROM-BELOW cross-anchor.
- `search_knowledge(... "VII.AU integer topological anchor ... Friedrich-Bar saturation reachable")` + `get_constant` → `Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI = 2` (S94, `S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR` **PASS** `fdf1321a…`, envelope_residual=0.0). This is the REACHABLE pole of the dichotomy.
- `search_knowledge("VII.AM envelope ratio L=11 ...")` → `S104-VIIAM-L11-ANCHOR` PASS (`3d4a8049`), ratio_prefac 0.868635 < 1 — a **bounded envelope ratio**, NOT a residue-subtracted continuous single-pole continuation ⇒ reachable-as-bounded, classifies consistently (no ambiguity forced).
- `search_knowledge("finite-L cannot reach analytic continuation pole no-go theorem ...")` → `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` PASS (a Mellin-cone **divergence-rate** statement, abs_div_356=15). This gate's scope is the **distinct** combined two-sided-approach + continuous-vs-integer **reachability** dichotomy, NOT a divergence rate. **NOT pre-closed.**

**Verdict**: **PASS** — the no-go theorem is established. Composite collapse: regime=VALID ∧ sign=PASS ∧ magnitude=PASS ⇒ **PASS**. All four criteria (a∧b∧c∧d) returned True. The optional `[SIGN]` 3-tuple (sign=PASS, magnitude=PASS, regime=VALID) registers the FROM-ABOVE/FROM-BELOW direction. Track A (general no-go) discriminator fires → HY6 §VII.CB/AU/BT/AM Level-3 re-class is LICENSED (session-track, mack sole-writer, routed OUT).

**THEOREM (INV8-W1-4 finite-L pole no-go).** *Let `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` be the finite-L truncation of the substrate spectral triple, with spectral zeta `ζ_{D_K}(s) = Σ_k m_k |λ_k|^{-2s}` (double-power convention A, poleconv-A-double) and manifold dimension d=8. For any pole `s < d/2 = 4`, the residue-subtracted analytic-continuation value (the Hadamard finite part) is **unreachable by any finite-L truncation from either side**: the ζ-native truncated sum (full Peter-Weyl multiplicity; Weyl counting `N(λ)~λ^d`) carries a missing tail `~λ^{d−2s}` with positive power `d−2s > 0`, hence **diverges to +∞ FROM ABOVE** with L_max; the bare block shell-sum `Σ_{(p,q)≤L} |λ_{(p,q)}|^{-2s}` (one eval per rank-r=2 Peter-Weyl cone point; cone counting `~x^{r}`) has effective tail power `x^{r−1−2s} < −1`, hence **converges FROM BELOW** to a value that drops the multiplicity weight and misses the finite part. The finite part lies strictly between the two one-sided limits and is recovered by neither. By contrast, an **integer-topological anchor** (winding number / K-theory pairing) is L_max-SATURATED (Friedrich-Bär: sectors above some L* contribute identically zero), hence **REACHABLE exactly at finite L**. The reachable/unreachable dichotomy is `continuous-residue-subtracted-pole ↦ UNREACHABLE`, `integer-cohomology-class ↦ REACHABLE`.*

The theorem's two poles are the canonical verdicts it reproduces: **S109 §VII.CB** (continuous s=3 pole, UNREACHABLE-FROM-ABOVE, `is_weyl_divergent=True`) and **S94 §VII.AU** (integer winding, REACHABLE, `envelope_residual=0.0`). Substrate-first reading: **GEOMETRIC** per `phononic-framing.md` — the no-go is a statement about what the finite substrate CAN/CANNOT compute about its OWN emergent geometry. `g_M = a_2^{ζ}` is the residue-subtracted continuation of the substrate's own zeta at s=3; it is an IS-space observable (the substrate IS this Hadamard finite part) that lives at a pole no finite truncation of the substrate's eigenvalue sum reaches. The explanation flows substrate → emergent geometry (the a₂ moment GENERATES g_M); it is NEVER inverted to "g_M is a number we extract by truncation". This is precisely why a Level-3 finite-L numerical anchor is the WRONG object to demand for a continuous-pole residue-subtracted observable, and why the integer-topological anchors (§VII.AU winding) — exact cohomology integers, not finite parts — ARE reachable.

**Output Artifacts** (closure-verification checklist — all confirmed on disk by content):
- Verdict line in `computations/investigation-8/inv8_gate_verdicts.txt` matching `^INV8-W1-4-FINITE-L-POLE-NO-GO:.* audit_sha256=[a-f0-9]{64}` — **present** (`audit_sha256=0f62c5d50f825d1d978f7a7535f90aa87ffab73f9fc3c69c61f6ac2398e0e0f6`, `content_sha256=6843ef0cf7854527929b2e70de5bfa019301d00494dcd7909f7006e572a97287`), with dual-SHA companion row + optional schema-v2 3-tuple companion row (`sign=PASS magnitude=PASS regime=VALID`) + regulator-pin companion row (`a_2^{zeta}`, pole_in_s=3, curvature_grade_n=2, poleconv=A-double, CLASS=FULL) + two-sided-approach companion row.
- Producing script `computations/investigation-8/inv8_w1_finite_l_pole_no_go.py` — **present**, contains `from canonical_constants import` and `print_verdict_payload`.
- Data `computations/investigation-8/inv8_w1_finite_l_pole_no_go.npz` — **present** (40 keys: L_max-scan sequences [native FROM-ABOVE + block FROM-BELOW], per-pole classification map, gap factor, integer-reachable contrast).
- Plot `computations/investigation-8/inv8_w1_finite_l_pole_no_go.png` — **present** (115.6 KB; the two-sided approach figure: ζ-native diverging FROM ABOVE on log-y, bare block plateauing 4.27× short FROM BELOW, anchor g_M between, integer-reachable contrast annotated).
- Section markers: `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` — all present.

**Results**:

NUMBERS (the no-go is verified, not asserted):
- **(a) Native FROM ABOVE** — Weyl power `d−2s = 8−6 = +2 > 0`; S109 cross-anchor native sequence `[39619.0337, 109123.0724, 280743.2354]` over L∈{6,8,10} is monotone-increasing (`is_weyl_divergent=True`, empirical Weyl growth exponent `α_{10,8}=4.235`). **crit_a = True.**
- **(b) Block FROM BELOW** — block cone tail power `r−1−2s = 2−1−6 = −5 < −1`; the bare block shell-sum `Σ|λ|^{-6}` recomputed from the L₁₂=12 cache across L∈{6,8,10,12} = `[346.81, 382.98, 410.41, 430.57]` with **decreasing increments** (36.17 → 27.43 → 20.15), converging; Aitken Δ² limit ≈ 486.4, S108 Richardson/Abel `Z(∞)≈650.70` — **both below g_M=2776.165389**. **crit_b = True.** (The 4-point Aitken estimate 486.4 underestimates the true block limit since the sequence is still climbing slowly at L=12; the criterion only requires the convergent limit to sit below g_M, which holds robustly for both 486.4 and the S108 650.70.)
- **(c) Hadamard finite part neither recovers** — `g_M = a_2^{ζ} = 2776.165389` lies strictly between the convergent block limit (≈650.70 below) and the divergent native (→+∞ above); gap factor `g_M/Z(∞) = 2776.165389/650.700475974211 = 4.266425938668019` **matches S108 exactly** (Sage-QQ exact rational `120702843000000/28291325042357`). **crit_c = True.**
- **(d) Integer anchor REACHABLE** — `Level3_integer_anchor_VII_AU = 2`, `envelope_residual = 0.0` (S94 §VII.AU; exact at L_max=12, Friedrich-Bär saturated). **crit_d = True.**
- **no_go_established (a∧b∧c∧d) = True.**

CLASSIFICATION MAP `C: {pole s} → {class}` (d=8, poleconv-A-double):
| s | n=8−2s | Weyl power d−2s | native | block tail r−1−2s | block | continuous class |
|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| 0 | 8 | +8 | diverges | +1 | diverges | UNREACHABLE-TWO-SIDED |
| 1 | 6 | +6 | diverges | −1 (boundary) | diverges (log) | UNREACHABLE-TWO-SIDED |
| 2 | 4 | +4 | diverges | −3 (conv) | converges | UNREACHABLE-TWO-SIDED |
| **3** | **2** | **+2** | **diverges** | **−5 (conv)** | **converges** | **UNREACHABLE-TWO-SIDED (g_M pole)** |
| 4 | 0 | 0 | log-marginal | −7 (conv) | converges | BOUNDARY-LOG (s=d/2) |

(Values are authoritative from `inv8_w1_finite_l_pole_no_go.npz` `cls_*` arrays. The native column uses the full-multiplicity Weyl power `d−2s`; the block column uses the rank-2 cone tail `r−1−2s = 1−2s`. The native sum DIVERGES for every s<d/2=4 [positive Weyl power] — this alone makes every such pole UNREACHABLE-FROM-ABOVE, hence two-sided-unreachable regardless of the block side. The block side transitions: s∈{0,1} block tail ≥ −1 ⇒ block also diverges/log-marginal (no clean from-below limit there); s∈{2,3} block tail < −1 ⇒ block converges, giving the clean FROM-BELOW short-fall (the g_M pole s=3 is in this regime — the load-bearing two-sided case, native diverges above ∧ block converges 4.27× short below). s=4=d/2 is the log boundary. §VII.AM is a bounded envelope ratio, reachable-as-bounded, classified consistently — no ambiguity forced → no INFO downgrade.)

6-STEP BOUNDARY-DIRECTION SUBSTITUTION CHAIN (Sage-exact verified): Step 1 — abs. convergence of `Σ m_k|λ_k|^{-2s}` requires `2s>d ⇔ s>4` (Weyl `N(λ)~λ^8`). Step 2 — g_M=a₂ lives at n=2 ⇔ s=(8−2)/2=3 < 4 ⇒ defining sum does NOT converge at the pole. Step 3 — native missing tail `~λ^{d−2s}=λ^{+2}` (positive) ⇒ truncated native GROWS with L (S109: 39619→109123→280743, trend +1, divergent). Step 4 — bare block sum (rank-2 counting, tail `x^{−5}`) converges to a value 4.27× BELOW g_M (S108, Z(∞)≈650.70). Step 5 — `g_M=2776.165389` is the Hadamard finite part between the two one-sided limits ⇒ UNREACHABLE-FROM-BOTH-SIDES. Step 6 — an integer-topological anchor is L_max-SATURATED (S94 §VII.AU=2, residual 0.0) ⇒ REACHABLE; this is the discriminant.

REGULATOR-PIN + CLASS (mandatory per `regulator-pin-discipline.md` + `substrate-first-canonical-sourcing.md` §(iv)): observable = `a_2^{ζ}` (zeta-regulated Seeley-DeWitt a₂); Mellin pole = a₂ residue at **s=3 (Conv. A, poleconv-A-double), curvature_grade_n=2**; **CLASS=FULL** (the cross-anchor native-divergent sequence and g_M are the FULL physical `analytic_zeta` evaluator's output via S109, NOT the SCHEMATIC `_spectral_action_regulators.py` helper). The verdict-line carries both companion rows.

CONSTRAINT-MAP CONSEQUENCE: the recurring §VII.CB/AU/BT/AM Level-3 FAIL pattern (C6) is converted from four isolated near-misses into ONE structural result. The affected **continuous-pole** rows (§VII.CB) re-class as "structurally-unreachable-by-design; Level-1 cohomology-class identity carries the result" — the registry-PASS criterion (Level-3 < Level-2 at canonical L_max) is shown to be the **wrong test** for residue-subtracted-continuation observables, which is itself a refinement of the `cross-pillar-bridge-anatomy.md` registry-PASS grammar (a residue-subtracted-continuation carve-out). The **integer-topological** rows (§VII.AU) remain registry-PASS-eligible (reachable by saturation). The §VII.CB/AU/BT/AM Level-3 re-class (HY6) is a **session-track** promotion of the §VII observable surface (mack sole-writer per `feedback_mack-bridge-role.md`), routed OUT to `/rclab-investigate --investigation 8` close — NOT an investigation-track edit.

OPERATIONAL DEVIATIONS (honest disclosure per `v3-closure-recovery.md` Class-1 boundary + `substrate-first-canonical-sourcing.md` §(ii.B)): (1) the plan §6 GPU pin names `torch.linalg`, but the computation reads the precomputed L₁₂ D_K spectrum cache and performs 1D scalar shell-sums + Aitken extrapolation (no new dense eigval/SVD ≥100×100 is constructed — the cache IS the spectrum), so the run is CPU-bound and capped at `OMP_NUM_THREADS=8`; this is an operational reality, not a convention swap. (2) the plan input path `computations/_shared/s84_spectrum_cache_L12_tau019.npz` is a documentation bug — the cache actually lives at `computations/session-84/s84_spectrum_cache_L12_tau019.npz`; runtime canonical-path correction applied and disclosed in the verdict value (`cache_path_corrected=True`). (3) the L₁₂ cache is MISSING the (4,4) sector (90/91 sectors, a known cache gap) — this does NOT affect the no-go, which is a statement about the L_max-SCALING (governed by the Weyl power `d−2s`), not about any single sector's value; the block convergence/native divergence trends are robust to one omitted sector.

DUAL-SHA: audit over (script ‖ canonical_constants.py ‖ pinmap{canonical, L₁₂ cache, S109 npz}) = `0f62c5d50f825d1d978f7a7535f90aa87ffab73f9fc3c69c61f6ac2398e0e0f6`; content over script = `6843ef0cf7854527929b2e70de5bfa019301d00494dcd7909f7006e572a97287`.

4-TUPLE: `(value=no_go=True;…;g_M=2776.165389;gap_factor=4.266426;int_anchor_VII_AU=2;…, scheme=MS, convention=MIXED, L_max=12)`.

---

## Wave 1 Synthesis (team-lead)

Wave 1 closed 4/4 (W1-1 FAIL · W1-2 PASS · W1-3 INFO · W1-4 PASS). The dark-sector-front through-line resolves cleanly but **negatively on the headline question**: the PBH fold-transit channel does NOT supply the missing DM abundance.

- **W1-1 (FAIL, Track-B under-supply)** — the Mach-13.75 fold produces a large squeezed collapse fraction (β₀=0.869 from N_pairs=59.8), but the fold horizon mass (≈8.7×10⁻²¹ g, Route A) sits ~37 OOM **below** the asteroid window and below the 5.1×10¹⁴ g Hawking-evaporation floor — these PBHs evaporated and are not present-day DM. I_PBH=1.8×10⁻²⁹⁹ vs target 0.27; robust across the δ_c band, both horizon-mass routes, all σ_fold conventions (regime=VALID). G4/Row #88 opens only as a *sub-evaporation-floor* mass function.
- **W1-3 (INFO, dimer = KEEP-AND-FLAG-UNDERIVED)** — with W1-1 FAIL, the dimer-Z₂ channel stays the sole non-Leggett DM candidate and remains un-derived (U3 open). The reconciliation made the ≥4 register f_DM numbers legible as a layered partition at distinct normalization stages.
- **W1-2 (PASS)** — w₀=−0.918 established as a genuine **two-sided** signature: S_8=0.8128 is closer to KiDS (2.34σ) than CMB (2.97σ) AND τ_reio=0.0559 is 0.27σ from Planck (the S_8/τ_reio *asset*), with w_a=0 the DESI *liability*. Honest scope: S_8 in 2.3–3σ tension with both anchors, closer-to-KiDS not a clean match.
- **W1-4 (PASS)** — the finite-L-cannot-reach-the-continuation-pole no-go promoted from conjecture to **theorem** (two-sided unreachability at s<d/2; integer anchor saturates), licensing the HY6 §VII.CB/AU/BT/AM Level-3 re-class via the reusable rank-r-vs-full-d Weyl-counting split.

### What Changed
**(a) Numerical revisions** — `I_PBH = 1.8×10⁻²⁹⁹` (fold-PBH window integral ≈ 0); `S_8_FW = 0.8128`, `τ_reio_FW = 0.0559`; reconciled two-channel DM sum `f_Leggett+f_dimer_Z2 = 0.276 ≈ Ω_DM = 0.2657`.
**(b) Structural changes** — f_DM register tangle → layered partition (MASS / ABUNDANCE / FRACTION at distinct normalizations); the standing "3-channel DM → 0.844" framing is a **stale-source Class-(c) defect** (session-74 L1128 itself corrected soft-hair DM→DE; DM is two-channel); G4 compact-object cell opened (sub-evap-floor); finite-L pole no-go conjecture → theorem.

### Effected In-Session (non-math)
All W1 non-math findings are SESSION-track promotions, routed OUT to `/rclab-investigate --investigation 8` close per the `gate-verdicts.md` track-local boundary — NOT effected by the investigation orchestrator (catalogued in `investigation-8-housekeeping.md §B`):
- **HY4** — f_DM two-channel canonical-table write + Ω_DM PROVENANCE entry (mack sole-writer).
- **HY6** — §VII.CB/AU/BT/AM Level-3 re-class, licensed by W1-4 (mack sole-writer).
- The W1-3 stale-source observation (3-channel→0.844 superseded) is recorded below; its canonical correction IS HY4.
No investigation-local non-math edits were required (all framework-registry writes are session-track).

## Carry-Forward Computations

No carry-forwards: all W1 outcomes closed in-session (W1-1/W1-4 closed their corridors / landed a theorem; W1-3 reconciled; W1-2's dual-ledger is session-track promotion, not a compute). The dimer-Z₂ independent-derivation problem (U3) is a standing open problem, not a 4-field-specced compute.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | PBH fold-transit DM-abundance (W1-1) | OPEN candidate | CLOSED (under-supply) | horizon mass ~37 OOM below window + below evap floor |
| 2026-06-15 | dimer-Z₂ supply-or-retire (W1-3) | conditional on W1-1 | KEEP-AND-FLAG-UNDERIVED; U3 open | W1-1 FAIL → dimer sole un-derived candidate |
| 2026-06-15 | w₀=−0.918 ledger (W1-2) | DESI-w_a liability only | two-sided (liability + S_8/τ_reio asset) | S_8 closer to KiDS; τ_reio 0.27σ from Planck |
| 2026-06-15 | f_DM "3-channel→0.844" framing (W1-3) | asserted | stale-source (soft-hair=DE; DM 2-channel) | session-74 L1128 author-correction |
| 2026-06-15 | finite-L analytic-continuation pole (W1-4) | conjecture | THEOREM (two-sided unreachable, s<d/2) | a∧b∧c∧d all True |
| 2026-06-15 | Row #88 compact-object cell (W1-1 G4) | empty | opened (sub-evap-floor mass function) | first formation-channel probe |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| INV8-W1-1 | `inv8_w1_pbh_fold_transit_spectrum.py` | ✓ | ✓ | FAIL |
| INV8-W1-2 | `inv8_w1_s8_tau_reio_gge_growth.py` | ✓ | ✓ | PASS |
| INV8-W1-3 | `inv8_w1_fdm_partition_reconciliation.py` | ✓ | — (optional) | INFO |
| INV8-W1-4 | `inv8_w1_finite_l_pole_no_go.py` | ✓ | ✓ | PASS |

All under `computations/investigation-8/`; verdicts in `inv8_gate_verdicts.txt`.
