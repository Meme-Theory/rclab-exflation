# Session 100b Wave 7 — JWST LRD Consistency Ceilings (Results Working Paper)

**Session**: 100b | **Wave**: 7 | **Plan**: session-100b-plan-w7.md | **Theme**: S99-G8 JWST-LRD gates — Rinaldi selection-function floor wrapper; a₂^{ζ}-channel heavy-seed OPEN fork; PANORAMIC × Whitler two-axis joint structure-timing constraint. All three are consistency ceilings under the `LRD_demographics_not_discriminating` wall (no framework-vs-ΛCDM discrimination at z < 10²⁸; every source paper sits ~28 OOM below the wall).

## Gate Sections

### §W7-1. S100b-SELECTION-FUNCTION-FLOOR (little-red-dots-jwst-analyst)

**Status**: COMPLETED
**Gate ID**: `S100b-SELECTION-FUNCTION-FLOOR`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (observational-methodology floor; laboratory-IN survey arithmetic, no substrate excitation content)
**Agent**: `little-red-dots-jwst-analyst`
**Hypothesis**: A reusable selection-fold wrapper pinned to the Rinaldi ≲25% classic-color-cut capture floor reproduces the published JADES GOODS-S/N test-case capture fraction to ≤10% relative (≤0.30 absolute guard) and emits the folded band W(z) = 1/S(z) that W7-2 (C2b, SOFT) and W7-3 (HARD) consume — consistency infrastructure, INFO-by-design in discriminating power (wall law), discriminating nothing between framework and ΛCDM.
**Plan reference**: `sessions/session-plan/session-100b-plan-w7.md` §W7-1 (machinery pin, reproduction thresholds, ≥0.602-dex widening substitution chain, Rinaldi/CLUST-43 pins, fetched-text-only extraction protocol).

**Output Artifacts**:

| Artifact | Path | must_contain verification |
|:---------|:-----|:--------------------------|
| Wrapper module | `computations/_shared/s100b_selection_fold.py` | `def fold` ✓, `def unfold` ✓, `0.25` ✓ (grep-verified); imports `S_capture_floor_LRD_classic` from canonical_constants; importable (imported + exercised by the gate script in-run) |
| Gate script | `computations/session-100b/s100b_w7_selection_function_floor.py` | `from canonical_constants import` ✓, `print_verdict_payload` ✓, `s100b_selection_fold` ✓ (grep-verified) |
| Data | `computations/session-100b/s100b_w7_selection_function_floor.npz` | arrays: `z_grid` (101 pts, z∈[3.0,13.0], dz=0.1), `S_band_lo`, `S_band_hi`, `W_z`, `capture_wrapper` (NaN, non-circular-not-evaluable), `capture_published` (0.25), `extraction_status` — plus recovered-anchor extras (counts, areas, n_inclusive 4-bin densities, unfold demo bands, cross-check residuals, machinery + pinmap JSON; float64 round-trip per Class 8.3) |
| Plot | `computations/session-100b/s100b_w7_selection_function_floor.png` | panel 1: flat S-band [0.25, 1.0] + W(z)=4 on the z-grid; panel 2: Rinaldi inclusive n(z) anchors with the unfolded intrinsic band [n, 4n] (+0.602 dex arrow) |
| Verdict line | `computations/session-100b/s100b_gate_verdicts.txt` | canonical line matches `^S100b-SELECTION-FUNCTION-FLOOR:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion row ✓; schema-v2 3-tuple row ✓ (sign/magnitude/regime — mandatory because the substitution chain pre-registers a direction claim); +3 companion rows (canonical-promotion, extraction-detail, downstream-consumer); emitted via race-safe `emit_verdict` MCP (6 rows, sig_5 unique) |
| Run log | `computations/session-100b/s100b_w7_selection_function_floor_run.log` | full stdout incl. input-pin SHA block + extraction report + cross-checks + payload |
| Fetched-text provenance | `computations/session-100b/_s100b_w7_rinaldi_text.txt` | `read_arxiv_paper('2604.07138')` PDF-fallback extraction (139,476 chars; runtime sha `e0a54c339c24daec…`); PDF bytes SHA-pinned `e392aad4125b18d6…` = plan pin MATCH |

**MCP Pre-Compute Audit**:

1. `search_knowledge("LRD selection function capture floor Rinaldi")` → only this gate's own plan/WP-skeleton entries; no prior evaluation — NOT PRE-CLOSED.
2. `trace_entity("LRD_demographics_not_discriminating")` → closed mechanism `closed_180` (STAGING, `closed-gw-channels.md`): LRD/structure demographics cannot discriminate framework from ΛCDM at z < 10²⁸ — wall law verified live; this gate is consistency infrastructure only.
3. `trace_entity("CLUST-43")` → provenance edge `s43_lrd_clustering.py → CLUST-43` confirmed (prior-work anchor; wrapper composes with, does not modify, that machinery).
4. `list_constants("LRD|capture|selection|rinaldi")` → no matches; `get_constant("S_capture_floor_LRD_classic")` → not found → observational anchor added BEFORE use via `update_constant`: `S_capture_floor_LRD_classic = 0.25` (SECTION E, PROVENANCE entry, gate=S100b-SELECTION-FUNCTION-FLOOR, source=Rinaldi arXiv 2604.07138 PDF sha `e392aad4…`), per `math-scripts.md` add-with-provenance-before-use.

**Verdict**: **INFO** — `EXTRACTION-LIMITED-BOUND-FORM` (pre-registered declared-pin-gap branch). Schema-v2 3-tuple: `sign_verdict=PASS / magnitude_verdict=INFO / regime_verdict=VALID`; pre-registered collapse rule gives composite INFO == gate-rubric INFO (in-script assertion). `audit_sha256=9935d01ce452b871a30305ddfc7e1fb894942a3afb983c1717a06b904fd002b4`, `content_sha256=921f6c36c3c217ad6f381e3bf47b7dd444e745f273615047061c6825c1b17a4e`, schema_version=S84+.

**Results**:

Output 4-tuple: `(value=EXTRACTION-LIMITED-BOUND-FORM_declared-pin-gap;…, scheme=SELECTION-FOLD-RINALDI, convention=CAPTURE-FRACTION-MULTIPLICATIVE, L_max=N/A)`.

*Numbers first — extraction from fetched text (`read_arxiv_paper('2604.07138')`, PDF-fallback; per `feedback_research-corpus` no memory-fill):*

- **Inclusive photometric counts**: 598 (GOODS-S, of 304,366 parent) + 218 (GOODS-N, of 181,144 parent) = 816 — **plan-pin MATCH** (598+218 pinned). Areas 349.6 = 210.44 + 139.16 arcmin². Visually-confirmed main sample 220 + 101 = 321; + 91 complementary low-z (F090W-anchored) = **412-source census** (z ≈ 2–11).
- **Classic-cut definition recovered**: F277W−F444W > 1.5 mag (Akins 2025 / Barro 2024), 7 in-text mentions.
- **Global capture floor recovered**: classic extreme color cuts isolate ≲25% of the population — **3 independent capture-context attestations** (abstract; Figure-3 color-histogram discussion; §5 discussion), all literal "≲25%". Complementary bin: ≈55% of the population at F277W−F444W = 0.5–1 mag (recovered).
- **Inclusive number densities recovered** (UV LF integrated to M_UV ≤ −18.5, cMpc⁻³): (2.82±1.61)×10⁻⁵ @ z 2–4.5; (1.16±0.41)×10⁻⁴ @ z 4.5–6.5; (5.99±2.19)×10⁻⁵ @ z 6.5–8.5; (3.18±1.28)×10⁻⁵ @ z 8.5–10.5.
- **Qualitative per-z anchor recovered**: at z ≈ 2–4.5 the F277W−F444W > 1.5 cut *within the primary selection* yields **no sources** (S → 0 at the low-z end) — recorded as diagnostic; the pre-registered band [0.25, 1.0] is NOT modified post-hoc.
- **The decisive extraction — classic-cut sub-sample count: ABSENT from fetched text.** Pre-specified tight pattern family (subsample-defining phrases + integer, with 1 ≤ n ≤ 816 and not-year guards): **0 candidates**; loose diagnostic family: **0 candidates**. The published ≲25% is a Figure-3 histogram-derived bound; the extreme-cut LF/density points exist only as figure data (Tables 1–2 are primary-selection only: "Measurements refer to the primary selection criteria"). A per-z S_i(z) table is likewise not published in text.

*Gate evaluation (operator conjuncts):* the count-form reproduction `|capture_wrapper − capture_published|/capture_published ≤ 0.10 ∧ capture_wrapper ≤ 0.30` is **not evaluable non-circularly** — setting capture_wrapper := the published 0.25 and comparing to capture_published = 0.25 would be load-and-compare-to-self (forbidden execution-property class, `epistemic-discipline.md`). With wrapper + npz conjuncts satisfied and the count-form conjuncts extraction-blocked, the pre-registered INFO branch fires: **the wrapper lands with the bound-form floor S ≤ 0.25 only (global figure, 3-site attested, matching the litrev spot-verification), flagged for re-verification; downstream gates consume the flat-floor band.** capture_wrapper = NaN in the npz (downstream consumers use `S_band`/`W_z`, never capture_wrapper — enforced in `load_band_npz` docstring).

*Cross-checks (all 7 PASS):*

| CC | Test | Result |
|:---|:-----|:-------|
| CC1 | Round-trip identity `unfold(fold(n,S),[S,S]) = [n,n]` over n×S test grid | max resid **0.0e+00** ✓ |
| CC2 | Widening direction+magnitude: W_floor = 1/0.25 = **4.000000**; log₁₀(4) = **0.602060** ≥ 0.602 | ✓ |
| CC3 | Census arithmetic: 598+218=816; 220+101=321; 321+91=412; 210.44+139.16=349.6 | ✓ |
| CC4 | Plan-pin match (598, 218, 349.6) | ✓ |
| CC5 | Fold thins: fold(n, 0.25) ≤ n | ✓ |
| CC6 | Unfold band ordering exact: [n_obs, 4·n_obs] | ✓ |
| CC7 | ≥2 independent ≲25% capture-context attestations (found 3) | ✓ |

*Substitution chain (pre-registered, substituted numbers):*

```
Step 1: S_i(z) = P(true LRD at z enters classic-cut sample); published floor S <= 0.25
        [Rinaldi 2604.07138 fetched text; 3 attestations; classic cut = F277W-F444W > 1.5 mag]
Step 2: n_obs(z) = S(z) * n_int(z)                      [capture definition]
Step 3: n_int(z) = n_obs(z) / S(z)                      [substitute]
Step 4: S(z) <= 0.25  =>  1/S(z) >= 1/0.25 = 4.000      [simplify]
Step 5: W = 1/S >= 4;  log10(4) = 0.602060 >= 0.602     [direction from canonical form]
Concl.: n_int(z) >= 4 * n_obs(z) at the classic-cut floor — the intrinsic band extends
        UPWARD by >= 0.602 dex; a bare-LF comparison without this fold is an INVALID TEST.
Demo on recovered anchors: z 4.5-6.5 inclusive n_obs = 1.16e-4 => intrinsic band
        [1.16e-4, 4.64e-4] cMpc^-3 (plotted, panel 2).
```

sign_verdict=PASS is this chain confirmed in-run (CC2 + CC6); magnitude_verdict=INFO is the extraction-blocked reproduction; regime_verdict=VALID (full intended z-domain used, f_used = 1.00; S ∈ (0,1] everywhere; all W finite).

*Dual-SHA (per plan audit_discriminators)*: `audit_sha256 = sha256(script ‖ wrapper_module ‖ canonical_constants ‖ pinmap_json ‖ machinery_pin_json)` = `9935d01ce452b871…`; `content_sha256 = sha256(script)` = `921f6c36c3c217ad…`. All 5 static input SHAs MATCHED plan pins at runtime (Rinaldi PDF `e392aad4…`, index `246bb0c6…`, litrev-LRD `884f9960…`, litrev-mack `e83c2a0f…`, clust43 `842d8711…`); runtime pins logged for canonical_constants (`a13dddb1…`, post-promotion), wrapper (`abd5dea3…`), text dump (`e0a54c33…`).

*Assessment (interpretation third).* The selection-discipline floor is OPERATIONAL in bound form: every downstream abundance/clustering/UVLF comparison in this wave is now folded through S_band = [0.25, 1.0] (W = 4, +0.602 dex upward on the intrinsic side). The INFO is the honest branch, not a defect — the wrapper logic is verified exact (CC1/CC5/CC6 at machine zero), the floor is triple-attested in fetched text, and what is missing (an explicit classic-cut sub-sample integer, a per-z capture table) is figure-only data in the source paper. Substrate framing (NON-PHONONIC, declared): the substrate's post-transit structure IS the GGE acoustic-excitation interference pattern self-organized through the a₂^{ζ} channel; what JWST counts is that pattern shadowed through a color cut capturing ≤25% — the laboratory-IN shadow is up to 4× thinner than the substrate-IS pattern, and the "too massive/abundant too early" tension is only as sharp as the selection function is clean (it is not). Direction preserved: D_K eigenvalues → spectral moments → emergent assembly → SELECTION-FOLDED measurement. Wall law honored: this gate discriminates nothing at z < 10²⁸. Downstream: W7-3 HARD edge is UNBLOCKED (npz landed at the exact plan path; INFO ≠ FAIL, so no PRE-REG-INC closure fires); W7-2 C2b consumes the npz directly (mode-B fallback not needed — note the flat-floor band is numerically identical to mode-B's ×4 widening, so C2b is insensitive to the branch). Re-verification carry-forward: per-z S_i(z) + classic-cut count from the paper's machine-readable/figure data (4-field spec at wave synthesis; per plan Decision Point "W7-1 INFO → downstream gates consume the flat-floor band; re-verification carry-forward").

---

### §W7-2. S100b-A2-HEAVY-SEED-ABUNDANCE (little-red-dots-jwst-analyst)

**Status**: COMPLETED
**Gate ID**: `S100b-A2-HEAVY-SEED-ABUNDANCE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (heavy seed IS the GGE interference pattern self-organizing through the a₂^{ζ} channel into a compact relay-pattern attractor)
**Agent**: `little-red-dots-jwst-analyst`
**Hypothesis**: GGE acoustic interference self-organizing through the a₂^{ζ} gravity-moment channel lands a compact relay-pattern attractor at M_seed ~ 10⁵ M⊙ under gas-dynamical collapse with the annihilation term structurally zero (Leggett-channel DM; LEGGETT-MOMENT-70), at host abundance within 0.5 dex of the Pacucci DCBH benchmark — consistency ceiling only below the z = 10²⁸ wall (a PASS keeps the seeding fork OPEN, never discriminates vs ΛCDM); a C3 energy-source gap is the real-constraint FAIL branch (Track B 0.9).
**Plan reference**: `sessions/session-plan/session-100b-plan-w7.md` §W7-2 (C1∧C2a∧C2b∧C3 conjunction, fiducial collapse/abundance pins, chains 17-1/17-2/17-3, dual-prior tracks, mode-B fallback, f_DM=0.209 declared NOT re-tested).

**Output Artifacts**:

| Artifact | Path | must_contain verification |
|:---------|:-----|:--------------------------|
| Gate script | `computations/session-100b/s100b_w7_a2_heavy_seed_abundance.py` | `from canonical_constants import` ✓(2), `print_verdict_payload` ✓(3, template-pattern function), `a_2_FW_zeta` ✓(9), `LEGGETT` ✓(9) — all grep-verified |
| Data | `computations/session-100b/s100b_w7_a2_heavy_seed_abundance.npz` | arrays: `M_seed_fiducial_Msun` + corners grid, `n_ACH_emergent`/`n_ACH_LCDM_ref`/`dlog10_n_ACH` at z={6,8,10}, `f_req` + band, `P_extra_over_P_grav` + full energy ledger, `L_Edd_ratio` (band-center + fiducial), `N_H_core` (3 n_core), `G_eff_over_G_N` + head diagnostic, `M_J_diag` (3 n_core), `M_ACH` both pipelines, S_band(z=6), `mode_B_exercised=False`, machinery+pinmap JSON, dual-SHAs (float64 round-trip per Class 8.3) |
| Plot | `computations/session-100b/s100b_w7_a2_heavy_seed_abundance.png` | panel 1: M_seed fiducial + 4 corners vs C1 band + GR cap + Jeans floor; panel 2: n_ACH emergent vs ΛCDM-ref vs z + folded LRD intrinsic band + f_req; panel 3: energy ledger (E_annih structurally 0, hatched) + L_Edd/N_H/head-diagnostic annotations |
| Verdict lines | `computations/session-100b/s100b_gate_verdicts.txt` | canonical PASS line matches `^S100b-A2-HEAVY-SEED-ABUNDANCE:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion ✓; `[SIGN]` schema-v2 3-tuple row ✓; +5 companion rows (normalization, dual-prior, convention, OOM-disclosure, structural-identity); emitted via race-safe `emit_verdict` MCP. **Option-A supersedes chain**: original line `audit=1febbc8d…` RETAINED-superseded; canonical line `audit=37f64fcd…` carries `supersedes=1febbc8d…` (script-bug-fix class: emission plumbing refactored to the template `print_verdict_payload` function mid-dispatch; ALL physics values byte-identical) |
| Run log | `computations/session-100b/_s100b_w7_a2_heavy_seed_run.log` | full stdout incl. input-pin SHA block (6 static pins all MATCH) + head diagnostic + chains + payload |

**MCP Pre-Compute Audit**:

1. `search_knowledge("heavy seed DCBH abundance LRD a_2 atomic cooling halo")` → only this gate's own plan/WP-skeleton entries + the LIVE atlas-04 row "JWST LRD BH-seed mass spectrum" (LIVE-PENDING — the row this gate feeds) — NOT PRE-CLOSED.
2. `get_constant("M_KK_gravity")` → 7.428660036284456e16 GeV, S42, gate CONST-FREEZE-42, superseded=False — the anchor pin verified live.
3. `trace_entity("LEGGETT-MOMENT-70")` → CONDITIONAL (Γ_grav < H₀); Ω_DM h² = 0.1200; Leggett-channel CPT-neutral NON-annihilating; "Annihilation = 0 PASS, baseline-findings-s66" — the C3 structural-zero verified live.
4. `trace_entity("LRD_demographics_not_discriminating")` → closed mechanism `closed_180` (STAGING, closed-gw-channels.md): cannot discriminate framework from ΛCDM at z < 10²⁸ — wall law verified live.
5. `list_constants("f2|m_proton|m_hydrogen|M_sun|pc_to|yr_to|…")` → all absent → 5 constants added with provenance BEFORE use via `update_constant` (math-scripts.md): `m_proton_g=1.67262192369e-24` (CODATA 2018), `M_sun_g=1.98841e33` (IAU 2015 nominal GM_sun/G_N), `pc_to_cm=3.0857e18` (Mpc_to_cm/1e6 alias), `yr_to_s=3.15576e7` (Julian, exact), `f2_dict_CC=92.0` (CC §8.3 dictionary; S95-W3-3/S96-W1 machinery — this gate is the 3rd consuming script, triggering the 3+-script promotion rule).

**Verdict**: **PASS** — conjunctive C1∧C2a∧C2b∧C3 all inside pre-registered bands. Schema-v2 3-tuple: `sign_verdict=PASS / magnitude_verdict=PASS / regime_verdict=VALID`; pre-registered collapse rule gives composite PASS == gate-rubric PASS (in-script assertion). Canonical line: `audit_sha256=37f64fcd7e81ef8575b1781b0385d3a0db6bd8a2ba4647790e0a81b7164455c9`, `content_sha256=b8ae1b2f13cc356dd0fd4c0e2782e7a2e4d23bd59c229d70a78867f2f45a572e`, schema_version=S84+ (supersedes `1febbc8d…`; Option-A reading discipline: latest non-superseded line is canonical). **Wall law**: PASS = consistency only — the gas-dynamical seeding fork stays OPEN; zero framework-vs-ΛCDM discrimination below z = 10²⁸.

**Results**:

Output 4-tuple: `(value=C1_log10Mseed=5.300_in[4.5,5.5]…;C2a…;C2b…;C3…, scheme=A2-EMERGENT-FRIEDMANN-DCBH, convention=BORROWED-H-BASELINE-SUBSTRATE-NATURAL-G, L_max=N/A)`.

*Numbers first — head diagnostic (printed first per plan):*

- **Emergent-G reconstruction** (non-circular): dictionary `1/(16π G_eff) = f₂·M_KK²·a₂^{ζ}/(48π²)` with f₂ = f2_dict_CC = 92.0 (S95-W3-3 `G_eff_of_tau` / S96-W1 `F2_DICT` machinery, CC §8.3), a₂^{ζ} = a_2_FW_zeta = 2776.165389 (S88), Λ = M_KK_gravity = 7.428660036284456e16 GeV (S42 CONST-FREEZE-42 — the route DEFINES the anchor). G_eff = 6.686779e-39 GeV⁻² vs CODATA G_N = 6.708722e-39 GeV⁻² → **G_eff/G_N = 0.996729, |G_eff/G_N − 1| = 3.271e-3** (the 0.33% residual is the f₂~92-vs-exact dictionary rounding). The three inputs (S88 a₂, S42 anchor, S95 dictionary) are pinned independently of CODATA M_Pl — the 0.33% reproduction of Newton-scale gravity from the substrate a₂ moment is the gate's real normalization content. M_Pl_eff(red) = 1.72e18 GeV ≈ 0.9984× per-G-ratio-equivalent of CODATA reduced (2.435e18 under the 2f₂ convention fold). a₂/a₀ = 2776.165389/6440.0 = 0.431082 (gravity-to-vacuum moment ratio, computed in-script from canonical imports). τ-stability: |dG/G| ≤ κ₂·δτ² = 0.0210181×(0.01)² = **2.10e-6** over the collapse epoch (first order dG/dτ = 0, a₂-flat regime S95-W5-4) — G_eff is τ-stable at 6 OOM below the 0.5-dex band.

*C1 — gas-dynamical seed (chain 17-2 executed, substituted numbers):*

```
Step 1-2: c_s = sqrt(γ k_B T/(μ m_p)) = 9.4980e5 cm/s = 9.50 km/s   [chain: 9.5]
Step 3:   Mdot = α c_s³/G_eff = 0.1993 M_sun/yr                      [chain: ~0.20]
Step 4:   M(t_SMS = 1 Myr) = 1.9930e5 M_sun                          [chain: 2.0e5]
Step 5:   M_GR = 3.0e5 M_sun (Ilie ⟨Γ₁⟩_P < 4/3 + 2.5·GM/(Rc²), n=3 non-rotating)
Step 6:   M_seed = min(1.993e5, 3.0e5) × f_prompt(1.0) = 1.9930e5 M_sun
Canonical form: log10(M_seed/M_sun) = 5.2995  ∈ [4.5, 5.5]  ⇒ IN-BAND ✓
```

Corners (t_SMS Myr, f_prompt) → log₁₀M_seed: (1, 1.0) = 5.300 fiducial in-band; (2, 1.0) = 5.477 in-band (GR-capped, chain-predicted 10^5.48 ✓); (1, 0.1) = 4.300 and (2, 0.1) = 4.477 BELOW band — the Ilie prompt-floor diagnostic, reported NOT gated (chain-predicted 10^4.30 ✓). Jeans floor M_J(8000 K) = {1.41e4, 7.94e3, 4.46e3} M_sun at n_core = {1e7, 10^7.5, 1e8} cm⁻³ — M_J ≪ M_seed at every corner: monolithic accretion-fed growth, not single-clump fragmentation. **C1 PASS.**

*Chain 17-1 — X-ray ceiling diagnostic (direction BELOW, confirmed):*

L_Edd = 1.3e38·(M/M_sun) erg/s [M/M_sun, NOT M/1e8 — memory guard applied]. At the C1 band center M = 1e5: L_Edd = 1.300e43, ratio to the Sacchi 390 Ms stacked ceiling 3.0e43 (k_bol = 16.7) = **0.433 < 1** [chain: 0.433 exact]. At the fiducial M_seed = 1.993e5: L_Edd = 2.591e43, ratio = **0.864 < 1**. Both below the ceiling BEFORE Compton-thick self-screening: contracted-core column N_H = n_core·R_core = {6.15e25, 1.32e26, 2.86e26} cm⁻² at the three pinned cores (self-consistent R_core = {1.99, 1.36, 0.93} pc from M_gas = 1e7 M_sun) — **all ≥ 1e25 cm⁻²**: the screen IS the flow (Pacucci). t_ff(n_core) = {14.8, 8.3, 4.7} kyr ≪ t_SMS. An Eddington-limited a₂-channel seed is X-ray-stack-consistent — the framework's seeding fork does NOT collide with the Sacchi non-detection, which is as informative as any detection here.

*C2a — emergent vs ΛCDM-reference host abundance (chain 17-3, z ∈ {6, 8, 10}):*

| z | M_ACH_em [M_sun] | σ(M_ACH)·D | ν | n_ACH_em [cMpc⁻³] | n_ACH_ref [cMpc⁻³] | Δlog₁₀ [dex] |
|:--|:--|:--|:--|:--|:--|:--|
| 6 | 1.607e8 | 1.024 | 1.646 | 4.646e0 | 4.646e0 | −0.00000 |
| 8 | 1.104e8 | 0.822 | 2.053 | 4.213e0 | 4.213e0 | −0.00000 |
| 10 | 8.179e7 | 0.688 | 2.450 | 3.114e0 | 3.114e0 | −0.00000 |

max_z |Δlog₁₀ n_ACH| = **0.00000 dex ≤ 0.5** — **C2a PASS**. Pipeline: first-principles T_vir inversion (T_vir = (μ_vir m_p/2k_B)(G M H √(Δ_c/2))^{2/3}, Δ_c = 18π², δ_c = (3/20)(12π)^{2/3} derived in-script), EH98 no-wiggle transfer (s = 149.8 Mpc, α_Γ = 0.799), exact ΛCDM growth integral (D(z=6)/D(0) = 0.1811), Sheth-Tormen (0.3222/0.707/0.3), 400-pt log-M grid per z, σ_8 = 0.811 borrowed.

**STRUCTURAL-IDENTITY DISCLOSURE** (math-scripts.md multiplicative-cancellation discipline): the 0-dex residual is EXACT under the borrowed-(H₀, Ω, σ_8) baseline — M_ACH ∝ 1/(G·H) and ρ_m,0 ∝ 1/G scale identically, so with m ≡ M/ρ_m,0 the count above a fixed-T_vir threshold is n = ∫_{m_th} dm/m²·νf(ν)|dlnσ/dlnm| with every factor G-free. C2a's PASS is therefore convention-structural, NOT empirical chain evidence; the discriminating consistency content lives in (a) the head diagnostic |G_eff/G_N − 1| = 3.27e-3 (the substrate normalization reproduces Newton-scale gravity) and (b) the ABSOLUTE n_ACH landing vs the DCBH host requirement. Disclosed in-script, in the verdict companion rows, and here.

**Chain 17-3 Step-2 OOM deviation disclosed**: computed n_ACH(z=6) = 4.65 cMpc⁻³ sits ~0.7 dex ABOVE the pre-registered OOM expectation 1e-2..1e0 cMpc⁻³ (the plan's expectation was conservative for a bare T_vir > 1e4 K cut; ST at M > 1.6e8 M_sun, z=6 gives a few cMpc⁻³, consistent with standard ACH counts). The deviation moves C2b's sufficiency in the STRENGTHENING direction; the chain conclusion (f_req ≪ 1) is unchanged.

*C2b — selection-folded LRD sufficiency at z=6:*

Fold source: **W7-1 npz consumed** (`extraction_status=EXTRACTION-LIMITED-BOUND-FORM`; S_band(z=6) = [0.25, 1.00], W = 4.0; numerically identical to the mode-B ×4 fallback, so C2b is branch-insensitive; `mode_B_exercised=False`). n_LRD_obs ∈ [1e-5, 1e-4] cMpc⁻³ (z > 4 pin, sweep paper 03 Ma, selection-convolved) → intrinsic band [1.00e-5, 4.00e-4] cMpc⁻³ (+0.602 dex). Conservative upper edge: **f_req(z=6) = 4.00e-4/4.646 = 8.61e-5 ≤ 1** — **C2b PASS**, inside the pre-registered chain-17-3 envelope [1e-5, 4e-2]. f_req band over the observed range: [2.15e-6, 8.61e-5]. The substrate-sourced atomic-cooling hosts outnumber the folded LRD population by ~4 OOM; the surplus is absorbed by the sub-unity pristine/LW-synchronization efficiency (external by construction). Direction SUFFICIENT confirmed.

*C3 — energy ledger (annihilation entry structurally absent):*

| Ledger entry | Value | Role |
|:-------------|:------|:-----|
| E_grav (a₂ channel) = G_eff·M_gas²/R_core | 6.277e54 erg | source — gravitational binding released |
| E_compressional (isothermal work, ln(ρ_core/ρ_vir) = 21.64) | 2.329e53 erg | gravity-financed intermediate (E_comp/E_grav = 0.0371) |
| E_radiative (Lyα thermostat) | ~E_grav | SINK, not source |
| **E_annihilation** | **0 — STRUCTURAL** | LEGGETT-MOMENT-70: Leggett-channel GGE DM is CPT-neutral, NON-annihilating (mass anchor 11.97 Δ_BCS, CONDITIONAL Γ_grav < H₀); Annihilation = 0 PASS (baseline-findings-s66) |

**P_extra/P_grav = max(0, E_comp − E_grav)/E_grav = 0.000 ≤ 0.01** — **C3 PASS**. Gravity finances the compression with 26.9× margin: the gas-dynamical route is self-financing; reaching the C1 band requires NO power source beyond the a₂ moment. The framework's dark sector could not have supplied annihilation heating even if demanded — the route never asks.

*Schema-v2 3-tuple + dual-prior:* sign=PASS (chains 17-1 BELOW + 17-2 IN-BAND + 17-3 SUFFICIENT all confirmed), magnitude=PASS (all four conjuncts in PASS bands), regime=VALID (post-transit late-epoch z ∈ [6,10] only — transit-era physics untouched per S74 "Friedmann wrong question"; Ω_m(z=6) = 0.9937 so EdS Δ_c valid; S ∈ (0,1]; f_used = 1.00); collapse rule asserted == composite in-script. **Dual-prior re-allocation (pre-registered discriminator): PASS → Track A 0.9** — a₂-channel gas-dynamical seeding closes the DCBH benchmark; the energy-source-gap Track B drops to 0.1.

*Dual-SHA + pins:* `audit_sha256 = sha256(script ‖ canonical_constants ‖ pinmap_json ‖ machinery_json)` = `37f64fcd7e81ef85…`; `content_sha256 = sha256(script)` = `b8ae1b2f13cc356d…`. All 6 static input SHAs MATCHED plan pins at runtime (Pacucci `7178cf0d…`, Ilie `00b02df8…`, Sacchi `787239d5…`, index `246bb0c6…`, litrev-LRD `884f9960…`, litrev-mack `e83c2a0f…`); runtime pins logged for canonical_constants (`1adce7fc…`, post-promotion of the 5 new constants) and the W7-1 npz (`0dffa0c3…`, consumed). No PDF numeral extraction needed — every W7-2 numeral was plan-pinned at freeze from the litrev; PDF bytes pinned as provenance only.

*Assessment (interpretation third).* The OPEN side of the seeding fork is now exercised end-to-end at a new observable: the same a₂^{ζ} moment that generates the Einstein-Hilbert term (G_eff at 0.33% of G_N from f₂·a₂·M_KK²/(48π²), with a₂ and M_KK pinned in S88/S42 and the dictionary in S95 — three independent lineages) drives a gas-dynamical collapse that lands a 2.0e5 M_sun seed inside the Pacucci DCBH band, at host abundances that oversupply the selection-folded LRD density by ~4 OOM, with the annihilation ledger entry structurally zero. As LRD analyst I emphasize what this does and does not say observationally: it does NOT discriminate the framework from ΛCDM (wall law; an efficient-baryon ΛCDM DCBH route matches identical data); it DOES establish that the framework's non-annihilating dark sector is no obstacle to heavy seeding — the Ilie SMDS route's annihilation requirement is a channel the substrate structurally lacks, and this gate shows the substrate never needs it (26.9× gravity margin). The Sacchi X-ray non-detection is RESPECTED, not merely evaded: an Eddington-limited 10⁵ M_sun seed sits at 0.43× the stacked ceiling, and the Pacucci contracted core is Compton-thick (N_H ≥ 6e25 cm⁻²) at every pinned density corner — the obscuration is the collapse flow itself. Substrate framing preserved: D_K eigenvalues → a₂^{ζ} moment → emergent G_eff + Friedmann rate → collapse at the atomic-cooling floor → JWST LRD counts as the selection-folded laboratory-IN shadow. Honesty devices carried: the C2a zero-residual is declared convention-structural (exact G-cancellation under the borrowed baseline), the chain-17-3 OOM expectation miss is disclosed (strengthening direction), the f_prompt = 0.1 corner falls below band (Ilie prompt-floor, diagnostic), and the Option-A supersedes chain documents the mid-dispatch emission-plumbing fix with byte-identical physics. Downstream: W7-3 receives the assembly-machinery narrative cross-cite (no data edge); mack's SMDS registry row cites this gate's PASS as the OPEN-side status by audit_sha256 `37f64fcd…`.

---

### §W7-3. S100b-STRUCTURE-TIMING-TWO-AXIS (little-red-dots-jwst-analyst)

**Status**: COMPLETED
**Gate ID**: `S100b-STRUCTURE-TIMING-TWO-AXIS`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (assembly IS the GGE interference pattern self-organizing through the a₂ channel; a₂/GEOMETRIC channel flavor explicit in framing)
**Agent**: `little-red-dots-jwst-analyst`
**Hypothesis**: The selection-folded substrate assembly band simultaneously contains all four axes — PANORAMIC ≥1 dex quiescent-abundance excess [DECISIVE] × σ_CV = 0.7±0.3 clustering [MILD, 0.63σ nearest-edge per the carried spot-verification correction] and Whitler both-ends UV excess × steep α ∈ [−2.79, −2.16] — with **EXPECTED verdict INFO** (degenerate-with-ΛCDM below the z = 10²⁸ wall: a consistency ceiling, never a discriminator); a >1σ folded miss beyond the ε=1 baryon-budget ceiling is the real-constraint FAIL branch (mack-cosmic-bridge lands the watchlist row, sole writer).
**Plan reference**: `sessions/session-plan/session-100b-plan-w7.md` §W7-3 (A1/A2/B1/B2 axis pins, joint 3-tier encoding, chains 19-1/19-2, W7-1 HARD edge + PRE-REG-INC DPP, CLUST-43 machinery reuse).

**Output Artifacts**:
- `computations/session-100b/s100b_w7_structure_timing_two_axis.py` — producing script (contains `from canonical_constants import`, `print_verdict_payload`, `s100b_w7_selection_function_floor.npz` per plan `must_contain`; CONFIRMED by grep at closure)
- `computations/session-100b/s100b_w7_structure_timing_two_axis.npz` — per-axis (obs, fiducial, band_lo, band_hi, sigma_distance, folded flags), joint tier, ε grid, `n_max_eps_grid`(5 z-bins × 3 ε), `rho_UV_max`(2 z × 3 ε), `b_implied_band`, extraction/crosscheck/machinery/pinmap JSON; float64 (Class-8.3 round-trip)
- `computations/session-100b/s100b_w7_structure_timing_two_axis.png` — 4-panel (A1 obs vs ceilings; A2 chain 19-1; B1 ρ_UV vs accretion ceiling; B2 α band)
- `computations/session-100b/_s100b_w7_ji_text.txt` + `_s100b_w7_whitler_text.txt` — fetched-text dumps (`read_arxiv_paper` 2604.05022 / 2501.00984; direct PDF Read blocked, S99 litrev precedent), SHA-pinned into the audit closure
- Verdict line in `computations/session-100b/s100b_gate_verdicts.txt` matching `^S100b-STRUCTURE-TIMING-TWO-AXIS:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 3-tuple row + 3 extra rows (chains / per-axis / extraction), emitted via race-safe `emit_verdict` (6 rows appended; sig_5 unique)
- Canonical-constants promotion: `kappa_UV_MadauDickinson = 1.15e-28` added WITH PROVENANCE (gate-tagged) BEFORE use

**MCP Pre-Compute Audit**:
1. `search_knowledge("structure timing two axis PANORAMIC quiescent Whitler UV luminosity")` → no prior evaluation of this gate (only the S100b W7 plan/WP self-references); NOT PRE-CLOSED.
2. `search_knowledge("LRD demographics not discriminating wall")` → no FTS hit under that phrasing; wall law verified directly on disk: `sessions/framework/registry/closed-gw-channels.md` line 29 — `LRD_demographics_not_discriminating`, observational degeneracy, **STAGING**, "Cannot discriminate framework from ΛCDM at z < 10^28".
3. `get_constant("S_capture_floor_LRD_classic")` → 0.25 (S100b, gate S100b-SELECTION-FUNCTION-FLOOR, not superseded) — consumed as the wrapper-floor consistency check (CC5).
4. `list_constants("kappa_UV|Madau|rho_UV")` → ABSENT → `update_constant("kappa_UV_MadauDickinson", 1.15e-28, S100b, Madau & Dickinson 2014 ARA&A 52, 415)` landed with PROVENANCE before the script imported it (math-scripts.md add-before-use).

**Verdict**: **INFO** — the pre-declared EXPECTED outcome (degenerate-with-ΛCDM below the z = 10²⁸ wall). Schema-v2 3-tuple: `sign_verdict=PASS` (both pre-registered directional chains confirmed), `magnitude_verdict=INFO` (band-contained, fiducial sweep 1/4), `regime_verdict=VALID` (all decisive extractions landed; f_used = 1.0) → composite INFO under the pre-registered collapse rule. 4-tuple: `(value=INFO-BAND-CONTAINED-DEGENERATE;…, scheme=TWO-AXIS-JOINT-SELECTION-FOLDED, convention=CONSISTENCY-CEILING-INFO-BY-DESIGN, L_max=N/A)`. Dual-SHA: `audit_sha256=25002865ff190b5598bf9aa8076d14da0e4a37c35807f05b79a242fbb791478d`, `content_sha256=830174b7de104ce7079d39bdb09185c1b21b33331f9e67f102de84475d750669`.

**Results** (numbers first):

*W7-1 HARD edge*: upstream verdict INFO (`EXTRACTION-LIMITED-BOUND-FORM`) ≠ FAIL → this gate FIRED (no PRE-REG-INC mechanical closure). Band consumed via `s100b_selection_fold.load_band_npz`: flat S = [0.25, 1.0] over z ∈ [3, 13], W = 4 (+0.602 dex); `capture_wrapper`(NaN) untouched per the W7-1 consumer row.

*A1 — abundance (PANORAMIC gold, Table 1 re-extracted at runtime; DECISIVE axis)*. Published per-bin 1σ includes the CV error; folded intrinsic band = [(n−σ)/S_hi, (n+σ)/S_lo]; ceiling = Sheth-Tormen n(>M*/(f_b·ε), z_mid) at ε=1 on the borrowed Planck-2018 baseline:

| z bin | N | n ±σ [10⁻⁵ Mpc⁻³] | folded band [Mpc⁻³] | ε=1 ceiling | headroom |
|:--|:--|:--|:--|:--|:--|
| 3.0–3.5 | 36 | 1.81 ± 0.53 | [1.28e-5, 9.36e-5] | 1.35e-2 | +2.16 dex |
| 3.5–4.0 | 37 | 1.52 ± 0.48 | [1.04e-5, 8.00e-5] | 1.04e-2 | +2.11 dex |
| 4.0–5.0 | 21 | 0.54 ± 0.39 | [1.50e-6, 3.72e-5] | 6.53e-3 | +2.24 dex |
| 5.0–6.0 | 2 | 0.09 ± 0.07 | [2.00e-7, 6.40e-6] | 3.09e-3 | +2.68 dex |
| 6.0–8.0 | 5 | 0.07 ± 0.06 | [1.00e-7, 5.20e-6] | 7.71e-4 | +2.17 dex |

Contained 5/5 (headroom = ceiling minus folded UPPER edge; minimum +2.11 dex); band-excluded none; fiducial hits 0/5 (the ε=1 maximal-coherence fiducial sits ≥2 dex above obs — expected). The ≥1 dex model-underprediction claim at z ≳ 4 re-verified verbatim from fetched text; the model-envelope floor (n_obs/10 at z ≥ 4 bins) is trivially inside the folded band. Gold/silver (1.5 vs 3.1)×10⁻⁵ at z=3–4 re-verified; gold+silver Table-1 column (3.14→0.10)×10⁻⁵ extracted and stored.

*A2 — clustering (MILD axis; chain 19-1 with substituted numbers)*. σ_CV = 0.7 ± 0.3 re-verified verbatim (estimator detail: bootstrap 0.71(+0.20/−0.28), MCMC 0.65(+0.25/−0.30)); UniverseMachine mocks 0.43 (sSFR-matched) / 0.51 (halo-mass-matched) re-verified. Chain 19-1: obs 1σ interval [0.40, 1.00] ∩ mock band [0.43, 0.51] non-empty; nearest-edge tension (0.7 − 0.51)/0.3 = **0.6333σ < 1** → MILD, cannot reject at 1σ; direction over-clustering (substrate-favorable). Under-clustering FAIL test (the only A2 FAIL direction): 0.7 + 0.3 = 1.0 ≥ 0.43 → no FAIL. **Fold-invariance (exact)**: a flat multiplicative capture S cancels in the fractional count variance (N → S·N leaves σ_CV unchanged); verified against the flat W7-1 band, so A2 (and the B2 shape parameter) are selection-fold-invariant while A1/B1 (densities) widen by W = 4. Geometry-free implied bias excess b_obs/b_mock = σ_CV_obs/σ_CV_mock = [1.37, 1.63] central, [0.78, 2.33] at 1σ (σ_DM cancels — the robust quantitative inversion product). Absolute inversion (BOUND-FORM, pointing-area pin gap declared): count-weighted per-bin pencil variance with CLUST-43 ξ_DM at z_eff = 3.91 gives σ_DM = 0.1280 / 0.0967 / 0.0481 at the three fetched anchors (1 cMpc, 2 cMpc, survey-arithmetic √(1000/34)′ = 5.42′) → b_implied ∈ [3.1, 20.8] (central ~10), vs mock-implied [3.4, 10.6] at the same geometry; intersects the pre-registered b-scan [0.5, 12] (the +1σ/widest-anchor corner exits the scan ceiling — recorded raw). S43 CLUST-43 b = 2.0 ± 0.5 cited as machinery+context only (LRD population, NOT massive quiescent — not an A2 datum). Fiducial hit TRUE: |0.7 − 0.51| = 0.63σ ≤ 1.

*B1 — both-ends UV (Whitler Tables 5+6 re-extracted)*. ρ_UV(M_UV ≤ −17): z~9.8 Schechter 2.82(−0.33/+0.34)×10²⁵, DPL 2.98(−0.34/+0.35)×10²⁵; z~12.8 Schechter 0.90(−0.17/+0.23)×10²⁵, DPL 0.98(−0.20/+0.25)×10²⁵ erg s⁻¹ Hz⁻¹ Mpc⁻³ (prose 0.93×10²⁵ and the <2.51×10²⁴ z≥16 limit recorded). Ceiling ρ_UV,max = f_b·ε·ρ̇_M,coll(>M_ACH)/κ_UV with the first-principles atomic-cooling threshold (T_vir = 10⁴ K, μ_vir = 0.6, Δ_c = 18π²): M_ACH(9.8) = 8.38e7 M⊙, ρ̇_coll = 5.32 M⊙ yr⁻¹ Mpc⁻³ → ceiling(ε=1) = 7.24e27; M_ACH(12.8) = 5.80e7 M⊙, ρ̇_coll = 2.99 → 4.07e27. All four folded bands contained; minimum headroom +1.74 dex (z10 DPL); even the ε=0.1 ceiling (7.2e26 / 4.1e26) sits above every folded upper edge. Both-end Φ bins present and stored (bright: −21.4 → 0.40(−0.27/+0.45), −20.4 → 3.6(−1.2/+1.4); faint: −17.4 → 330 ± 80, ×10⁻⁵ mag⁻¹ Mpc⁻³) with the excess-direction prose re-verified ("slightly higher than many pre-JWST… difference grows larger at increasingly high redshifts"). φ* decline z10→z13: paper's "~2.1–2.3" re-verified verbatim (Table-6 ratios: Sch 2.47, DPL 2.14 — the plan-carried correction of the index's "~3" stands). Fiducial hits 0/4.

*B2 — steep α (set-membership + direction; INFO-only by design)*. z~10: α_Sch = −2.36(−0.18/+0.20), α_DPL = −2.60(−0.19/+0.17); z~13 (Table 6): α_Sch = −2.23(−0.30/+0.32), α_DPL = −2.42(−0.31/+0.32). Membership in [−2.79, −2.16]: 4/4. Direction α ≤ −2 (centrals): 4/4 (z13 Schechter upper edge crosses −2 at 0.72σ — detail, not a gate input). Disclosed drift: prose α(z~13) = −2.29/−2.41 vs Table 6 −2.23/−2.42 (plan pin cites the prose; both readings in-band; Table 6 used as authoritative, prose recorded).

*Joint 3-tier*: contained {A1: T, A2: T, B1: T, B2: T}; band-excluded {all F}; fiducial hits 1/4 (A2 only — PASS-tier structurally unreachable since B2 carries no quantitative substrate α) → **tier = INFO**, exactly the pre-declared EXPECTED outcome.

*Chains (pre-registered, substituted)*: **19-1** — σ_CV: [0.4, 1.0] ∩ [0.43, 0.51] ≠ ∅; (0.7−0.51)/0.3 = 0.6333σ < 1 → MILD confirmed; the abundance axis carries the joint weight. **19-2** — f_b = Ω_b/Ω_m = 0.0493/0.315 = 0.15651 (plan 0.1565); M_h_min(ε=1) = 10¹⁰/f_b = 6.389e10 M⊙ (plan 6.39e10); all folded observations sit BELOW the ε=1 ceilings (A1 min +2.11 dex, B1 min +1.74 dex) → INFO-side, FAIL branch unused.

*Cross-checks (8/8 PASS)*: CC1 CLUST-43 machinery fidelity — `growth_factor_ratio`/`xi_DM`/`wp_DM` ast-extracted from the SHA-pinned S43 script (top-level body NOT executed — protects the pinned S43 npz/png from rewrite) reproduce the stored `wp_dm` at max rel dev 0.00e+00. CC2 chain 19-1 arithmetic. CC3 chain 19-2 pins (f_b, M_h_min within 1% of plan). CC4 plan-pin re-verification 14/14 (1.81/0.07 endpoints; ΣN_gold = 101 and ΣN_gold+silver = 238 matching the abstract counts; 0.7±0.3; 0.43/0.51; ≥1 dex claim; (1.5 vs 3.1); α −2.36/−2.60; ρ_UV 2.82(−0.33/+0.34); φ* 2.1–2.3; 0.93×10²⁵). CC5 selection band: S_lo == canonical `S_capture_floor_LRD_classic` = 0.25, S_hi = 1, flat. CC6 σ_8 normalization round-trip |σ(R₈)−σ_8| = 0.00e+00. CC7 Table-1 count totals close the abstract arithmetic independently (μ = 238/34 = 7.0 matches the paper's prose). CC8 plan-frozen SHA match 7/7 static inputs (both PDFs, index, both litrevs, s43 .py+.npz).

*Declared pin gaps (bound-form, never memory-fill; `substrate-first-canonical-sourcing.md §(ii.B)` disclosure)*: (1) the single-NIRCam-pointing area in arcmin² is not stated numerically in the fetched Ji text → the ABSOLUTE bias inversion is bound-form over fetched anchors only (the "~1–2 Mpc, comparable to the size of a single NIRCam pointing" comparison + the 1000 arcmin²/34-sightline survey arithmetic); the geometry-free ratio b_obs/b_mock carries the quantitative A2 content. (2) α(z~13) prose-vs-Table-6 drift, both recorded. (3) the B1 model-envelope floor is qualitative (the paper's own excess-direction statements re-verified); the FAIL-relevant side — the ε=1 ceiling — is fully quantitative. Machinery deviations from plan: none (scheme, convention, ε grid, b-scan, ST parameters, EH98 transfer, z-bins all as pinned; deterministic, no random seed; cpu-cap-OMP8).

*Assessment (interpretation third)*. The two-axis joint constraint is now ENCODED and LIVE as a consistency ceiling, and the verdict is the honest one the wall law demands: every axis of both papers sits inside the substrate's selection-folded allowed band — with ≥2.1 dex (A1) and ≥1.7 dex (B1) of headroom to the ε=1 baryon-budget ceiling — while the maximal-coherence fiducial sweep fails (1/4), which is precisely the degenerate-with-ΛCDM configuration. Nothing here discriminates the framework from an efficient-baryon ΛCDM model, ~28 OOM below the z = 10²⁸ wall (`LRD_demographics_not_discriminating`, STAGING), and the pre-declared EXPECTED-INFO prevents over-claiming the containment as support. What the numbers DO say: the "too massive/abundant too early" tension at z ≈ 3–8 is a baryon-efficiency statement (≥1 dex above the published model envelope) and NOT an assembly-impossibility statement (≥2 dex below the maximal-assembly bound even after the ×4 selection unfolding) — for the substrate exactly as for ΛCDM. On the MILD axis the observed σ_CV excess leans the substrate-favorable way (over-clustering, 0.63σ; implied bias excess 1.4–1.6× over UniverseMachine at central values; standing-wave correlation-by-construction predicts exactly this direction) but cannot reject Poisson-sampled halos at 1σ. Substrate framing preserved: D_K eigenvalues → a₂^{ζ} spectral moment → emergent assembly + standing-wave correlation → SELECTION-FOLDED laboratory-IN counts. The ceiling sharpens only with more sightlines (A2 uncertainty ∝ 1/√n_field; the paper itself estimates >100 additional sightlines for a robust σ_CV verdict) or deeper LFs (B1/B2) — observational, not framework-side, work; FAIL branch unused → no mack watchlist row, no registry surface touched, no carry-forward computation from this gate.

---

## Wave 7 Synthesis (team-lead)

**Written**: 2026-06-07, session close. All 3 gates landed; verdicts verified on disk against each gate's `output_artifacts` must_contain set, including the W7-2 Option-A supersession chain. The wave's governing Wall Law (`LRD_demographics_not_discriminating`, STAGING, z < 10²⁸) was honored in every section: this entire wave is consistency infrastructure, zero framework-vs-ΛCDM discrimination claimed anywhere.

| Gate | Verdict | Headline value |
|:-----|:--------|:---------------|
| §W7-1 S100b-SELECTION-FUNCTION-FLOOR | **INFO** (EXTRACTION-LIMITED-BOUND-FORM) | floor operational in bound form: S_band = [0.25, 1.0], W = 4 (+0.602 dex); counts 598+218 = 816 plan-match (audit `9935d01ce452b871…`) |
| §W7-2 S100b-A2-HEAVY-SEED-ABUNDANCE | **PASS** (Option-A canonical; supersedes `1febbc8d…`) | all 4 conjuncts: M_seed = 1.99e5 M_⊙ in-band; f_req = 8.61e-5; energy 26.9× margin, E_annih = 0 STRUCTURAL (audit `37f64fcd7e81ef85…`) |
| §W7-3 S100b-STRUCTURE-TIMING-TWO-AXIS | **INFO** (EXPECTED, pre-declared) | band-contained degenerate: A1 5/5 (min headroom 2.11 dex), A2 MILD 0.63σ, B1 contained (1.74 dex), B2 4/4 (audit `25002865ff190b55…`) |

**Wave reading.** The LRD consistency-ceiling stack is now ENCODED and LIVE, and its honest summary is: **the "too massive / too abundant too early" tension is a baryon-efficiency statement, not an assembly-impossibility statement — for the substrate exactly as for ΛCDM.** W7-1 operationalizes the selection discipline in bound form (classic color cuts capture ≤ 25% of the LRD population, triple-attested in fetched text; every downstream comparison folds through S_band = [0.25, 1.0]) — the INFO is the honest branch, with the missing pieces (per-z capture table, classic-cut integer) being figure-only data in the source. W7-2 exercises the gas-dynamical (OPEN) seeding fork end-to-end at a new observable: a₂-channel heavy seeds land mid-band (1.99e5 M_⊙ vs GR cap 3.0e5), host anchors oversupply LRD demand by ~4 OOM through the W7-1 wrapper, and the energy ledger self-finances at 26.9× inside gravity with E_annihilation = 0 STRUCTURAL (Leggett-moment CPT-neutrality) — with the C2a 0-dex agreement correctly DISCLOSED as a structural identity (G-cancellation; empirical content = the non-circular head diagnostic |G_eff/G_N − 1| = 3.3e-3). W7-3's pre-declared EXPECTED-INFO is the wall law working as designed: every published axis sits INSIDE the substrate's selection-folded allowed band with ≥1.7–2.1 dex headroom to the ε=1 ceiling, the maximal-coherence fiducial fails (1/4) — precisely the degenerate-with-ΛCDM configuration — while the one MILD lean (σ_CV over-clustering, 0.63σ, fold-invariant, bias excess 1.4–1.6×) points the substrate-favorable way (standing-wave correlation-by-construction) but cannot reject Poisson halos at 1σ. The ceiling sharpens with sightlines and depth — observational work, not framework-side.

**Decision-point evaluation** (plan §"Wave 7 → Session Decision Point"): W7-1=INFO → downstream gates consumed the flat-floor band (both did, via the npz at the exact plan path; W7-2 C2b noted band ≡ mode-B so branch-insensitive); re-verification carry-forward opened (CF below). W7-2=PASS → fork stays OPEN; mack's SMDS Row #78 OPEN-side cite landed in-session (`falsifier-master-inventory.md:1828`, wall-law verbatim, CLOSED-branch falsifier structure unchanged). W7-3=INFO (EXPECTED) → "joint constraint encoded + live as a consistency ceiling; no registry action" — executed as written; FAIL branch unused → no watchlist row.

**Carry-Forward Computations (MATH ONLY — propagate to S101)**

### CF-S101-LRD-SELECTION-REVERIFY — per-z selection function + classic-cut count re-verification

Per the plan's W7-1 INFO routing ("downstream gates consume the flat-floor band; re-verification carry-forward") + §W7-1 assessment: **What** — replace the flat bound-form floor with the per-z selection function S_i(z) and the explicit classic-cut sub-sample integer, extracted from the Rinaldi+ machine-readable/figure data (the quantities that were figure-only in the text extraction), and re-verify the count-form capture fraction non-circularly; then re-fold W7-2 C2b and W7-3's A1/B1 axes through the refined band. **Inputs** — Rinaldi+ arXiv 2604.07138 machine-readable tables/figure data (when published or digitized), `s100b_w7_selection_function_floor.npz` (bound-form baseline + z_grid), `computations/_shared/s100b_selection_fold.py` (wrapper entry points unchanged), `s100b_w7_a2_heavy_seed_abundance.npz` + `s100b_w7_structure_timing_two_axis.npz` (re-fold targets). **Gate** — PASS iff the per-z refined band is CONTAINED in the bound-form band [0.25, 1.0] at all z ∈ [3, 13] (the bound-form conclusions then inherit unchanged); INFO iff containment fails at some z but no W7-2/W7-3 conjunct flips; FAIL iff any conjunct flips under the refined band. **Effort** — 1 compute gate, ≤ half a session (no new physics; extraction + re-fold).

### CF-W7-1 (MULT-CANCELLATION-DETECTOR-LAB-IN-AXIS) — extend the plan-freeze cancellation detector to ratio-of-pipelines + variance-functional signatures *(investigation append, 2026-06-07, /rclab-investigate consolidator; Q2 — §D methodology/audit-script extension; registry-hygiene carry-forward, first surfaced at investigation — NOT in housekeeping A1–A20)*

**What** — `math-scripts.md` §"Multiplicative-normalization cancellation invariants" is MANDATORY (K=3), but its plan-freeze pre-flight + queued `_machinery_feasibility_audit.py` extension key on log-derivative operator signatures (`d^n ln(·)/d(ln K)^n`) only. Wave 7 produced TWO instances the detector would have missed at plan-freeze (both instead self-detected at execution and disclosed per the MANDATORY discipline): (a) W7-2 C2a — the gated quantity `max_z |log₁₀(n_ACH_em/n_ACH_ref)|` is EXACTLY 0 by G-cancellation under the borrowed-(H₀, Ω, σ₈) baseline (M_ACH ∝ 1/(G·H), ρ_m,0 ∝ 1/G; count above fixed-T_vir threshold is G-free) — a log-RATIO-of-pipelines signature, not a log-derivative (audit `37f64fcd7e81ef85…`, structural-identity companion row on disk); (b) W7-3 A2 — flat multiplicative capture S cancels exactly in the fractional count variance (N → S·N leaves σ_CV invariant), verified in-run (audit `25002865ff190b55…`). The cancelling factors are laboratory-IN pipeline parameters (G, S) — a categorically NEW axis vs the rule's three K-counter rows (L_max-truncation / τ-moduli / Casimir-ceiling spectral-support weights). **Resolution (mechanical; any two methodology agents would derive it identically)** — extend the detector pattern set to ratio-of-pipelines and variance-functional signatures + append the two instances as calibration-corpus rows (rule already MANDATORY — corpus append only, no K-advancement decision; instances → `sessions/framework/registry/`-corpus per `feedback_rules-directive-only-no-session-info.md`). **Inputs** — `_machinery_feasibility_audit.py`, the two verdict companion rows above, `math-scripts.md` rule text. **Gate** — detector diff landed + self-test covering both new signature classes (synthetic positive each) + 2 corpus rows. **Effort** — one audit-script diff + corpus rows; no compute. Routing: housekeeping §D (orchestrator append — flagged in the consolidator's terminal output) with this block as the WP CF mirror per `Investigating-Workshops.md` §"Routing summary".

**Effected In-Session (NON-MATH — completed before STOP)**

- [x] SMDS Row #78 OPEN-side status cite (W7-2 PASS routing) — mack-cosmic-bridge sole-writer via `s100b_close_mack_registry_batch3.py` — `sessions/framework/registry/falsifier-master-inventory.md:1828` (row block 1811–1828) — audit `37f64fcd7e81ef85`
- [x] Constant `S_capture_floor_LRD_classic = 0.25` landed with PROVENANCE before use (W7-1 canonical write-order Step 2) — little-red-dots-jwst-analyst in-gate — `computations/_shared/canonical_constants.py:689,1890` — gate `S100b-SELECTION-FUNCTION-FLOOR`
- [x] Five unit/dictionary constants (`m_proton_g`, `M_sun_g`, `pc_to_cm`, `yr_to_s`, `f2_dict_CC`) landed with PROVENANCE before use (W7-2 Step 2) — little-red-dots-jwst-analyst in-gate — `computations/_shared/canonical_constants.py` SECTION E — gate `S100b-A2-HEAVY-SEED-ABUNDANCE`
- [x] Reusable selection wrapper published for future demographic gates — little-red-dots-jwst-analyst in-gate — `computations/_shared/s100b_selection_fold.py` (fold/unfold/selection_band/load_band_npz) — consumed by W7-2/W7-3 this session

**Process observations (closed in-session; do NOT propagate)**: W7-3's agent completed all artifacts, then wedged in an Edit-mtime retry loop against the shared W7 working paper (its sibling W7-2's concurrent section-write moved the file mtime); the section had already landed — the agent was stopped after disk verification, costing nothing but its farewell message. Two same-type LRD agents on one shared WP is the boundary case of the `feedback_session-process.md` N>2 single-writer rule; both sections landed intact (boundaries grep-verified), but the wrap-up race burned ~40 min of idle agent time. W7-1's plot title overlap noted by its agent as cosmetic — accepted as-is.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-07 | LRD selection systematics (observational-methodology axis) | qualitative caveat (litrev G8 §II.6) | OPERATIONAL bound-form floor: S_band = [0.25, 1.0], W = 4, +0.602 dex; wrapper canonical for future demographic gates | W7-1 INFO |
| 2026-06-07 | Gas-dynamical (SMDS-fork OPEN branch) heavy seeding via a₂ channel | fork OPEN, chain unexercised at abundance observable | fork OPEN, chain exercised END-TO-END (mass + abundance + sufficiency + energy all in-band); consistency only per wall law | W7-2 PASS |
| 2026-06-07 | LRD "too massive/abundant too early" tension (z ≈ 3–8) | undifferentiated tension | RE-SCOPED: baryon-efficiency statement (≥1 dex above published model envelope), NOT assembly-impossibility (≥2 dex below maximal-assembly even after ×4 unfolding) — substrate and ΛCDM alike | W7-3 INFO (EXPECTED) |
| 2026-06-07 | σ_CV clustering axis | unexamined vs substrate | MILD substrate-favorable lean (0.63σ over-clustering; bias excess 1.4–1.6×; standing-wave direction) — NOT significant at 1σ; sharpens only with >100 additional sightlines | W7-3 A2 axis |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other | Size |
|:-----|:-------|:------------|:------------|:------|:-----|
| W7-1 | s100b_w7_selection_function_floor.py | ✓ | ✓ | s100b_selection_fold.py (shared wrapper) + _s100b_w7_rinaldi_text.txt + run.log | 34.8 KB / 20.2 KB / 82.6 KB / 6.8 KB |
| W7-2 | s100b_w7_a2_heavy_seed_abundance.py | ✓ | ✓ | run.log; 5 constants promoted | 52.5 KB / 24.2 KB / 112 KB |
| W7-3 | s100b_w7_structure_timing_two_axis.py | ✓ | ✓ | — | 60.5 KB / 39.2 KB / 257 KB |
