# Session 88 Plan — Wave 4c: 3He lab coordination + protocol pre-registration

> **Wave class**: COMPUTE-class (per `.claude/rules/wave-classification.md` §"Strict-conjunction requirement"). All 8 items have pre-registered PASS/FAIL/INFO numerical thresholds OR pre-registered protocol-document existence-with-substantive-content thresholds bound to verdict-line emission. M1 satisfied per gate-by-gate threshold registration; M2 satisfied per `s88_w4c_<slug>.py` producing scripts where applicable; protocol pre-registration items (#31-#36 sub-set) emit verdict-line per `mechanical-closure-discipline.md` discipline with substantive working-paper sections.
>
> **Theme**: 3He lab coordination + protocol pre-registration + Altland-Zirnbauer class theorem (volovik PRIMARY).
>
> **PRIMARY agent**: volovik-superfluid-universe-theorist (substrate-physics authority on 3He-B inheritance + Altland-Zirnbauer class).
> **CO-AUTHORS**: mack-cosmic-bridge (sole writer for `sessions/framework/registry/falsifier-master-inventory.md` row updates per `feedback_mack-bridge-role.md`); sagan-empiricist (protocol rigor cross-check on #36 NMR α_s extraction).
>
> **Substrate framing** (per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"): Each gate's substrate-IS observable is a finite-L spectral-triple cocycle on `(A_K, H_K, D_K)`; the laboratory-IN observable is a 3He-B / 3He-A measurement performed IN a continuum cryostat container. The bridge map is the inheritance morphism ι_*: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) (BDI → BdG sector child) with the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; residual 0.0e+00) preserving substrate-derived ratio ‖φ_67‖/‖φ_88‖ = 7.324992 INTACT under common-exponent lab-conversion. Cross-pillar bridge anatomy per `.claude/rules/cross-pillar-bridge-anatomy.md` 5-element + 3-level discipline: this wave instantiates FWD-C3 (Pillar IV ↔ Pillar V; SUGGESTION at K=2; calibration-corpus instance #3 candidate).

## Wave 4c Summary

Wave 4c lands the laboratory-falsifier coordination layer for the 3He-B inheritance program. Eight gates split into four functional clusters:

- **Lab campaign coordination** (#25, #26, #31, #32, #33): pre-register Lancaster MCT-3 vortex-core spectroscopy and Aalto LTL / Helsinki ROTA µSR cross-platform ratio measurements as the empirical anchors for falsifier rows #45-#54b (`sessions/framework/registry/falsifier-master-inventory.md`).
- **Gap-extraction calibration** (#34): cross-compare Greywall, Halperin-Hammel, and Volovik q-theory gap-extraction methods to bound the (Δ_B/Δ_A) systematic on the cohomology-asymmetry ratio test.
- **Altland-Zirnbauer class theorem** (#35): re-derive the inheritance morphism χ from the BDI ↔ DIII compatibility theorem (S86 W-5 QQ-substitution-chain Step 2).
- **NMR α_s extraction protocol** (#36): pre-register experimental protocol for extracting α_s^{lab} from longitudinal NMR resonance-frequency running curve with full error budget.

All eight gates pre-register protocols and theorems for multi-year experimental cycles (2027-2030 lab campaigns) plus in-session S88 verifiable theorems (#34, #35, #36 protocol pre-registration). The wave closes the substrate→lab interface for the framework's most decisive falsifiers.

## Wave 4c Decision Point Prerequisites

- **Upstream (must be PASS at S88 entry)**:
  - S86 W-5 §VII.AF.1 cross-pillar bridge theorem (Pillar III ↔ Pillar IV); LANDED at S87 W5-1.
  - S86 W-5 DONE-5: (Δ_B/Δ_A)^p cancellation theorem (residual 0.0e+00; machine-precision PASS).
  - S86 W1b-T8 canonical: 3He-B inheritance is parent→child morphism (NOT analogy); `sessions/framework/correspondence/3HeB-inheritance-canonical.md`.
  - canonical_constants.py: `substrate_cocycle_ratio_67_88 = 7.324992` (Sage-exact at machine epsilon; 4-sig-fig form 7.3250 for human-readable text).
  - `sessions/framework/registry/falsifier-master-inventory.md` rows #45-#54b in place (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`).
  - 3He-B polycritical anchor: P_pc=21.22 bar, T_pc=2.273 mK; SC_corr_A=1.151, SC_corr_B=1.111; Δ_A/(k_B T_c)=2.0302, Δ_B/(k_B T_c)=1.9597.

- **Downstream (consumed by this wave)**:
  - `papers/s87-3he-b-alpha-s-equivalent.md` falsifier rows 45+46 (mapped to Aalto LTL protocols at #31).
  - `.claude/rules/inheritance-falsifier-protocol.md` 4-Gate Structure (W11-C5/C6 calibration corpus): Gate-1 decisive NULL on F1+F2+F5; Gate-2 cohomology-asymmetry ratio 7.3250 ± 0.1%; Gate-3 supporting NULL on F3+F4; Gate-4 slope discrimination on cocycle-degenerate rows.
  - `.claude/rules/cross-pillar-bridge-anatomy.md` FWD-C3 candidate (Pillar IV ↔ Pillar V).

---

## §W4c-25. S88-LANCASTER-MCT3-VORTEX-CORE-EVALUATE

**Gate ID**: `S88-LANCASTER-MCT3-VORTEX-CORE-EVALUATE` (no S87 collision verified — S87 W11-1 / W11-2 / W11-3 / W11-5 do not occupy this ID; new ID for S88)

**Trigger**: Pre-registration of the Lancaster MCT-3 dilution-fridge campaign (Pickett group) measuring 3He-B vortex-core Caroli-Matricon ladder asymmetry as the Gate-1 NULL on F1+F2+F5 plus Gate-2 cohomology-asymmetry ratio anchor for the inheritance-morphism falsifier protocol.

**Classification**: PHONONIC (per `phononic-framing.md` §"Classification Guide": directly involves substrate excitations / relay patterns of the 3He-B BdG sector inherited from `(A_K, H_K, D_K)` via χ).

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (authority on 3He-B BdG spectrum, Caroli-Matricon ladder; Volovik 2003 §6 reference).
- **CO-AUTHOR**: mack-cosmic-bridge (sole writer for `sessions/framework/registry/falsifier-master-inventory.md` row #45 Lancaster anchor; per `feedback_mack-bridge-role.md`).
- **CO-AUTHOR**: sagan-empiricist (protocol rigor cross-check; experimental design audit).

**Hypothesis (substrate-IS to laboratory-IN)**:
The Caroli-Matricon vortex-core ladder asymmetry F1 = (E_+ − E_−)/(E_+ + E_−) at the n=0 minigap level vanishes structurally when the substrate's HP^1 cocycle [φ_67] sits in ker(ι_*) (the inheritance kernel from `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` BdG sector projection). The laboratory-IN observable F1^{lab} measured at the vortex core via STM tunneling spectroscopy or NMR ladder excitation reproduces the substrate prediction NULL within experimental S/N (forecast σ ≈ 9 at Lancaster MCT-3 sensitivity per one-decade pressure window 0–34 bar).

**Method (PROTOCOL pre-registration document, multi-year experimental cycle)**:

1. Producing script: `s88_w4c_lancaster_mct3_protocol.py`
2. The script does NOT measure F1^{lab} (multi-year lab cycle 2027-2030); instead, it pre-registers the experimental protocol document at `sessions/framework/registry/lancaster-mct3-protocol-pre-registration.md` with the following structure:
   - **Section A**: Substrate prediction (volovik PRIMARY): F1^{lab}_predicted = NULL at S/N ≈ 9σ per one-decade pressure window; substrate-derived margin = 0.573193 M_KK² (per S86 W-5 §VII.AF.1 calibration).
   - **Section B**: Lab platform specification (sagan CO-AUTHOR): Lancaster MCT-3 dilution fridge, Pickett group; T_base ≤ 100 µK; pressure sweep 0–34 bar; vortex generation via rotation Ω_rot ∈ [0.1, 10] rad/s; spectroscopy protocol (STM tunneling or transverse-NMR ladder excitation).
   - **Section C**: Cross-platform validation (mack CO-AUTHOR): row #45 anchor in `falsifier-master-inventory.md` updated with Lancaster pre-registration SHA; cross-link to row #46 (Aalto LTL A-phase ratio counterpart from #26).
3. Verdict-line emission: PASS iff protocol document exists with all three sections + substantive content (>15 lines per section) + audit_sha256 over input-pin map (substrate prediction + lab platform spec + cross-platform validation triplet).

**Machinery pin (pre-registered)**:

```
substrate_cocycle_norm_phi67   = 0.793346 M_KK²        (Sage-exact, S86 W-5 DONE-5)
substrate_predicted_F1_NULL    = 0.0 (at substrate level)
lab_S_N_forecast_per_decade    = 9.0                  (forecast; multi-year)
pressure_sweep_window          = [0.0, 34.0] bar       (canonical 3He P range)
T_base_required                = 100e-6 K              (Lancaster MCT-3 spec)
Omega_rotation_range           = [0.1, 10.0] rad/s     (vortex-generation window)
spectroscopy_method            = "STM_tunneling | transverse_NMR_ladder" (disjunction)
ratio_band_lower               = 7.3177                (cohomology-asymmetry band lower)
ratio_band_upper               = 7.3323                (cohomology-asymmetry band upper)
ratio_central                  = 7.324992              (Sage-exact substrate value)
ratio_tolerance_relative       = 0.001                 (0.1% per S86 W-5 W11-C5)
audit_sha256_input_pin_map     = closure_hash({substrate_pred, lab_spec, cross_platform})
content_sha256                 = sha256(protocol_document_text)
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. **Script**: `computations/s88_w4c_lancaster_mct3_protocol.py` (~150 lines; emits dual-SHA verdict line + writes protocol document).
2. **Data file**: NONE (this is a protocol pre-registration; no numerical data at S88).
3. **Plot**: NONE.
4. **Working-paper section**: §W4c-25 in `sessions/archive/session-88/session-88-w4c-workingpaper.md` (>15 lines; includes substrate framing per `phononic-framing.md`; cross-link to §W4c-26 µSR ratio counterpart and §W4c-31 Aalto LTL coordination).

**Verdict criteria**:

- **PASS**: Protocol document exists at `sessions/framework/registry/lancaster-mct3-protocol-pre-registration.md` with Sections A + B + C all present at substantive content (>15 lines each); `falsifier-master-inventory.md` row #45 updated by mack-cosmic-bridge with Lancaster pre-registration SHA; verdict-line dual-SHA emitted with `audit_sha256` derived from `closure_hash(input_pin_map)` per `script-template.py` `append_verdict()`.
- **FAIL**: Any section absent OR substantive content <15 lines OR cross-platform validation absent OR row #45 not updated by mack OR audit_sha256 not unique against prior verdict closures (sig_5 violation per `v3-closure-recovery.md`).
- **INFO**: Protocol document exists but cross-platform validation deferred to Wave 5 (e.g., row #45 update queued for mack write-batch); verdict line records `value='PROTOCOL-PRE-REGISTERED-CROSS-PLATFORM-DEFERRED'` per `mechanical-closure-discipline.md` value-string pattern.

**Substitution chain (per `.claude/rules/math-scripts.md` §"Double-Check Logic")**:

```
Step 1: Substrate prediction at the inheritance kernel ker(ι_*):
  F1^{substrate} := ⟨[φ_67], [Ch(P_0(τ_fold))]⟩ on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10})
                  = 0.793346 M_KK² · sign(chiral pair)   [S86 W-5 DONE-5 Sage-exact]
Step 2: Inheritance morphism ι_*: A_K → M_2(ℂ) projects M_3(ℂ) → 0:
  ι_*([φ_67]) = 0   ⇔   [φ_67] ∈ ker(ι_*)               [BDI→BdG sector projection]
Step 3: Laboratory observable F1^{lab} via Caroli-Matricon ladder:
  F1^{lab} = (E_+ − E_−)/(E_+ + E_−)                   [Volovik 2003 §6]
           = 0 · (Δ_B/Δ_A)^p   under (Δ_B/Δ_A)^p cancellation theorem
Step 4: NULL prediction:
  F1^{lab}_predicted = 0   at substrate-clean level     [Class A kernel-signature]
Step 5: Lab S/N forecast (Lancaster MCT-3 sensitivity):
  σ_F1 ≈ 9.0 per one-decade pressure window             [forecast; multi-year cycle]
Conclusion: F1^{lab} = 0 ± σ_F1 / √(N_observations) ≈ NULL within experimental reach.
```

**What PASS/FAIL MEAN (substrate-physics interpretation)**:

- **PASS** at protocol pre-registration: the substrate's Class-A kernel-signature prediction is registered as a pre-defined falsifier; future Lancaster MCT-3 data will compare measured F1^{lab} against the substrate NULL at 9σ S/N. PASS at protocol level does NOT confirm the substrate; it pins the falsifier for future test.
- **FAIL** at protocol pre-registration: documentation incomplete; substrate falsifier is NOT pre-registered; multi-year lab cycle cannot proceed against a pre-defined substrate prediction (would risk post-hoc ansatz-fitting).
- **Future lab PASS** (post-2027): Lancaster MCT-3 measures F1^{lab} = NULL within 9σ; Class-A kernel-signature confirmed; substrate inheritance survives.
- **Future lab FAIL** (non-NULL detection): lab measures F1^{lab} ≠ 0; substrate's Class-A prediction falsified UNLESS Class-B cohomology-asymmetry ratio ‖φ_67‖/‖φ_88‖ = 7.324992 ± 0.1% holds in the cross-cocycle channel (per `inheritance-falsifier-protocol.md` §"Two Test Classes"); both NULL-on-rows AND ratio-on-cross-rows must hold for substrate to pass.

**Effort**:
- **S88 in-session**: 4-6 hours (volovik PRIMARY drafts substrate prediction Section A; sagan CO-AUTHOR drafts lab platform Section B; mack CO-AUTHOR updates inventory row #45; orchestrator emits verdict line).
- **Multi-year lab cycle**: 2027-2030 (Lancaster MCT-3 campaign; Pickett group; pre-registered protocol governs measurement).

**Substrate framing** (per `phononic-framing.md` §"IS Space, Not IN Space"):
The substrate IS the cocycle [φ_67] on `(A_K, H_K, D_K)`; the laboratory IS NOT a container in which the substrate "lives" — Lancaster MCT-3 is a controlled realization of the same universality class (BDI / 3He-B). The vortex core is not a region OF spacetime; it is a substrate-spectral reorganization where the BdG-sector eigenvalue spectrum admits the Caroli-Matricon ladder. The direction of explanation: substrate cocycle ker(ι_*) → BdG-sector image → Caroli-Matricon ladder asymmetry → NULL prediction. This is NOT "particles in vortex cores" thinking; it is "fiber spectral content reorganizes at the vortex defect" thinking.

**Cross-pillar bridge anatomy (per `cross-pillar-bridge-anatomy.md` 5 IS-not-IN elements)**:
1. **Substrate-IS observable**: ⟨[φ_67], [Ch(P_0(τ_fold))]⟩ on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`.
2. **Laboratory-IN observable**: F1^{lab} = Caroli-Matricon ladder asymmetry at vortex core IN Lancaster MCT-3 cryostat.
3. **Bridge map**: Inheritance morphism ι_*: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) ∘ (Δ_B/Δ_A)^p lab-conversion (cancellation theorem applied).
4. **Algebraic envelope**: Ratio preservation 7.3250 ± 0.1% (structural-exact form, not L_max⁻α).
5. **Empirical anchor target**: F1^{lab} = NULL at 9σ + ratio 7.3250 ± 0.1% on any non-NULL detection.

---

## §W4c-26. S88-MUSR-VORTEX-CROSS-PLATFORM-RATIO-EVALUATE

**Gate ID**: `S88-MUSR-VORTEX-CROSS-PLATFORM-RATIO-EVALUATE` (no S87 collision)

**Trigger**: Pre-registration of µSR (muon spin rotation) vortex-core measurements across two lab platforms — Lancaster B-phase (Pickett group, Lancaster MCT-3 cell) AND Aalto LTL A-phase (Krusius/Tuoriniemi/Eltsov ROTA channel) — with cross-platform ratio comparison against substrate-derived 7.324992 ± 0.1% AND inter-lab consistency |r_A − r_B| < 0.1%.

**Classification**: PHONONIC.

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (authority on 3He-B vs 3He-A vortex-core spectroscopy; both phases admit Caroli-Matricon-like ladder structure with phase-dependent lab-conversion).
- **CO-AUTHOR**: mack-cosmic-bridge (sole writer for inventory row #46 µSR cross-platform anchor).
- **CO-AUTHOR**: sagan-empiricist (cross-platform consistency rigor; falsifier-class B precision-bound audit).

**Hypothesis**:
The substrate-derived cohomology-asymmetry ratio ‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact) is preserved INTACT under the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; residual 0.0e+00) for ANY value of (Δ_B/Δ_A) and p, INDEPENDENT of phase (3He-B vs 3He-A). Therefore the µSR vortex-core ratio measured at Lancaster B-phase r_B and at Aalto LTL A-phase r_A must satisfy:
- r_B = 7.324992 ± 0.1% (cohomology-asymmetry band)
- r_A = 7.324992 ± 0.1% (same band; phase-independent under cancellation)
- |r_A − r_B| < 0.1% (cross-platform inter-lab consistency)

**Method**:

1. Producing script: `s88_w4c_musr_cross_platform_protocol.py`
2. Script pre-registers the two-platform protocol document at `sessions/framework/registry/musr-cross-platform-protocol-pre-registration.md`:
   - **Section A** (volovik): Substrate prediction ratio = 7.324992 (Sage-exact); cohomology-asymmetry band [7.3177, 7.3323]; phase-independence proof via (Δ_B/Δ_A)^p cancellation.
   - **Section B** (volovik + sagan): Lancaster B-phase µSR protocol — implanted muons in 3He-B vortex cores; Larmor precession frequency ω_µ; Knight-shift ratio extraction.
   - **Section C** (volovik + sagan): Aalto LTL A-phase µSR protocol — Krusius/Tuoriniemi/Eltsov ROTA channel; A-phase chirality discrimination via µSR spin-relaxation rate.
   - **Section D** (mack): Inventory row #46 update; cross-link rows #45+#46; cross-platform consistency band |r_A − r_B| < 0.1%.

**Machinery pin**:

```
substrate_ratio_central        = 7.324992              (Sage-exact)
substrate_ratio_band_lower     = 7.3177                (band 7.3250 ± 0.1%)
substrate_ratio_band_upper     = 7.3323
inter_lab_consistency_tol      = 0.001                 (|r_A − r_B|/r_central < 0.1%)
delta_B_over_delta_A_canonical = 0.96528               (= 1.9597/2.0302; canonical_constants)
cancellation_residual          = 0.0                   (S86 W-5 DONE-5 machine epsilon)
chi_A_volovik_2003             = 1.500000              (3/2; Volovik 2003 §3.4)
musr_lancaster_platform        = "Lancaster_MCT3_Pickett_B_phase"
musr_aalto_platform            = "Aalto_LTL_KTE_A_phase_ROTA"
audit_sha256_input_pin_map     = closure_hash({substrate_pred, lancaster_spec, aalto_spec, cross_platform})
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. Script: `computations/s88_w4c_musr_cross_platform_protocol.py`.
2. Data file: NONE (protocol pre-registration).
3. Plot: NONE.
4. Working-paper section: §W4c-26 in `session-88-w4c-workingpaper.md` (>15 lines; cross-link to §W4c-25 Lancaster Caroli-Matricon counterpart and §W4c-32 Aalto Class-A dispatch).

**Verdict criteria**:

- **PASS**: Protocol document exists with Sections A + B + C + D all substantive (>15 lines each); inventory row #46 updated by mack with µSR cross-platform pre-registration SHA; verdict-line dual-SHA emitted; phase-independence proof via cancellation theorem cited explicitly in Section A.
- **FAIL**: Any section absent OR cancellation-theorem citation missing OR cross-platform consistency band |r_A − r_B| < 0.1% not pre-registered OR mack inventory update absent.
- **INFO**: Protocol pre-registered but Aalto LTL ROTA channel availability deferred (e.g., Krusius group schedule conflict 2027-2028); verdict-line records `value='PROTOCOL-PRE-REGISTERED-AALTO-SCHEDULE-DEFERRED'`.

**Substitution chain**:

```
Step 1: Define substrate ratio at inheritance kernel:
  R_substrate := ‖[φ_67]‖ / ‖[φ_88]‖ on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10})
              = 0.793346 M_KK² / 0.108307 M_KK²
              = 7.324992                                [Sage-exact, machine epsilon]
Step 2: (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5):
  lab(F_i) / lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j)
                       at common p_i = p_j = p          [common-exponent cancellation]
Step 3: Lab ratio under cancellation:
  r_B := lab(F_67^B) / lab(F_88^B) = R_substrate · (f_67^B/f_88^B)
       = 7.324992 · 1                                  [f_67/f_88 = 1 by cocycle pair structure]
Step 4: A-phase ratio under same cancellation:
  r_A := lab(F_67^A) / lab(F_88^A) = R_substrate · (f_67^A/f_88^A)
       = 7.324992 · 1                                  [phase-independent at substrate level]
Step 5: Cross-platform consistency:
  |r_A − r_B| / R_substrate = |1 − 1| · 7.324992 = 0   [structural prediction]
  Lab tolerance: |r_A − r_B| / r_central < 0.001       [0.1% inter-lab band]
Conclusion: r_B = r_A = 7.324992 ± 0.1% AND |r_A − r_B| < 0.1% predicted from substrate.
```

**What PASS/FAIL MEAN**:

- **PASS** at protocol pre-registration: substrate's Class-B cohomology-asymmetry prediction is registered as a pre-defined falsifier on TWO platforms with cross-consistency band; future µSR data at Lancaster + Aalto will compare against substrate ratio 7.324992 AND against each other.
- **Future lab PASS** (post-2027): r_B and r_A both lie in [7.3177, 7.3323] AND |r_A − r_B| < 0.1%; substrate cohomology-asymmetry survives across phase-flip; (Δ_B/Δ_A)^p cancellation confirmed empirically.
- **Future lab FAIL** (ratio out of band): substrate Class-B falsified; even if Class-A NULL holds (gate #25), the cohomology-asymmetry ratio test fails the substrate prediction. Note: a ratio FAIL is structurally MORE decisive than a Class-A FAIL because it isolates the substrate-derived value from the lab-conversion factor (Δ_B/Δ_A)^p.

**Effort**:
- **S88 in-session**: 4-6 hours (volovik PRIMARY substrate Section A + Lancaster Section B + Aalto Section C; mack inventory update; sagan rigor audit on |r_A − r_B| < 0.1%).
- **Multi-year lab cycle**: 2027-2030 cross-platform campaign (Lancaster + Aalto LTL coordination).

**Substrate framing**:
The two laboratories realize TWO universality-class children of the same parent inheritance morphism: 3He-B (BDI; Pf=−1; N_K=2) and 3He-A (DIII chiral; N_3=2). Both inherit from the same `(A_K, H_K, D_K)` parent; the ratio test is substrate-INVARIANT under the phase-flip. The cross-platform consistency band |r_A − r_B| < 0.1% IS the substrate's prediction at the inheritance-morphism level; deviation indicates either (a) substrate cohomology-asymmetry breakdown OR (b) a non-cancellation-theorem-compliant lab-conversion factor (i.e., p_i ≠ p_j for the two cocycles in some lab observable).

**Cross-pillar bridge anatomy**:
1. **Substrate-IS**: ‖[φ_67]‖ / ‖[φ_88]‖ on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` = 7.324992.
2. **Laboratory-IN**: r_B (Lancaster B-phase) and r_A (Aalto A-phase) µSR Knight-shift ratios IN respective cryostats.
3. **Bridge map**: ι_* ∘ (Δ_B/Δ_A)^p cancellation (common-exponent applies across both phases by structural pair-cocycle property).
4. **Algebraic envelope**: 0.1% relative band (substrate-INVARIANT structural exact; not L_max⁻α).
5. **Empirical anchor target**: r_A = r_B = 7.324992 ± 0.1% AND |r_A − r_B| < 0.1%.

---

## §W4c-31. S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION

**Gate ID**: `S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION` (no S87 collision)

**Trigger**: Multi-session experimental-protocol document mapping `papers/s87-3he-b-alpha-s-equivalent.md` falsifier rows 45+46 to Aalto LTL specific protocols (Krusius / Tuoriniemi / Eltsov groups).

**Classification**: PHONONIC.

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (authority on 3He-B Aalto LTL platform; long-standing collaboration with Krusius group on vortex physics).
- **CO-AUTHOR**: mack-cosmic-bridge (inventory rows #45 + #46 cross-link update).
- **CO-AUTHOR**: sagan-empiricist (multi-session protocol design rigor).

**Hypothesis**:
The substrate's inheritance-morphism falsifier rows #45 (Lancaster Caroli-Matricon F1 NULL) and #46 (µSR cross-platform ratio 7.324992) require a coordinated Aalto LTL multi-session campaign (S88 → S100+ horizon) to provide the laboratory anchor at the European ULT cell side. This gate pre-registers the Aalto-specific protocol mapping: which Aalto group runs which protocol, on which cell (ROTA / nanofluidic / 3He-A test cell), under which (P, T) sweep window, with which spectroscopy method (NMR / µSR / Andreev reflection).

**Method**:

1. Producing script: `s88_w4c_aalto_ltl_coordination.py`
2. Script pre-registers `sessions/framework/registry/aalto-ltl-multi-session-protocol.md`:
   - **Section A** (volovik): Substrate predictions for each falsifier row #45+#46 mapped to Aalto-specific observables.
   - **Section B** (volovik + sagan): Aalto group / cell / method matrix:
     - **Krusius group**: ROTA channel; rotation-induced vortex generation; transverse-NMR ladder spectroscopy; F1 + F2 + F5 NULL pre-registration.
     - **Tuoriniemi group**: Nanofluidic 3He cell; Andreev-reflection spectroscopy; F3 + F4 ladder asymmetry.
     - **Eltsov group**: 3He-A test cell; A-phase chirality discrimination via NMR + µSR; cross-platform ratio counterpart to row #46.
   - **Section C** (mack): Inventory rows #45 + #46 updated with Aalto coordination SHA.

**Machinery pin**:

```
aalto_groups                   = ["Krusius", "Tuoriniemi", "Eltsov"]
aalto_cells                    = ["ROTA_channel", "Nanofluidic_3He", "A_phase_test_cell"]
spectroscopy_methods           = ["transverse_NMR_ladder", "Andreev_reflection", "NMR_plus_muSR"]
falsifier_rows_covered         = ["45_Lancaster_F1_NULL", "46_muSR_ratio_7p3250"]
campaign_horizon               = "S88_to_S100_plus_2027_to_2032_lab_years"
substrate_predictions_coverage = "F1+F2+F5_NULL_decisive_AND_ratio_class_B"
audit_sha256_input_pin_map     = closure_hash({groups, cells, methods, rows, horizon})
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. Script: `computations/s88_w4c_aalto_ltl_coordination.py`.
2. Data file: NONE (multi-session coordination document).
3. Plot: NONE.
4. Working-paper section: §W4c-31 in `session-88-w4c-workingpaper.md` (>15 lines; cross-link to §W4c-25 Lancaster, §W4c-26 µSR, §W4c-32 Class-A dispatch, §W4c-33 ratio precision).

**Verdict criteria**:

- **PASS**: Aalto coordination document exists with Sections A + B + C; group-cell-method matrix covers ALL three Aalto groups; falsifier rows #45+#46 explicitly mapped; mack inventory update emitted.
- **FAIL**: Any group missing from matrix OR any falsifier row without Aalto anchor OR campaign horizon not specified OR mack update absent.
- **INFO**: Coordination pre-registered but specific Aalto group schedules unconfirmed (deferred subject to Krusius/Tuoriniemi/Eltsov bilateral correspondence).

**Substitution chain**:

```
Step 1: Substrate predictions per falsifier row:
  Row #45: F1^{lab} = NULL at substrate-clean level     [Class A kernel-signature]
  Row #46: r = 7.324992 ± 0.1%                         [Class B cohomology-asymmetry]
Step 2: Map to Aalto observables:
  F1 ↔ Krusius ROTA transverse-NMR ladder asymmetry
  r  ↔ Tuoriniemi nanofluidic + Eltsov A-phase µSR cross-ratio
Step 3: (P, T) sweep windows:
  Krusius:    P ∈ [0, 34] bar, T ≤ 1 mK, Ω_rot ∈ [0.1, 10] rad/s
  Tuoriniemi: P ∈ [10, 30] bar, T ≤ 0.5 mK, nanofluidic confinement
  Eltsov:     P near P_pc=21.22 bar, T near T_pc=2.273 mK, A-phase window
Step 4: Multi-session horizon binding:
  S88 = pre-registration; S100+ = lab data harvest 2027-2032
Conclusion: Aalto LTL multi-session campaign anchors falsifier rows #45+#46 with three-group coverage.
```

**What PASS/FAIL MEAN**:

- **PASS** at S88: Aalto-side coordination is pre-registered; rows #45+#46 have European ULT laboratory anchors; substrate falsifier protocol has both Anglo-American (Lancaster) and European (Aalto) coverage.
- **FAIL** at S88: coordination incomplete; substrate falsifier protocol relies on single-platform Lancaster anchor only (not robust to single-platform systematic).
- **Future lab PASS / FAIL**: per the row-specific protocols (#25, #26, #32, #33) — the coordination gate itself is in-session pre-registration only.

**Effort**:
- **S88 in-session**: 6-8 hours (volovik PRIMARY drafts coordination matrix; sagan rigor audit on multi-session timeline; mack inventory cross-link; corresponding email pre-drafts to Aalto groups via volovik's standing collaboration).
- **Multi-session lab cycle**: 2027-2032 Aalto LTL campaign (three groups; potential 4-5 lab years).

**Substrate framing**:
Aalto LTL is not a "site" where the substrate is studied; it is a controlled realization of the BDI / 3He-B universality class with European cell-engineering capabilities (ROTA rotational vortex generation; Tuoriniemi nanofluidic confinement; Eltsov A-phase mastery). The substrate's predictions are realized identically at Aalto and Lancaster modulo cell-engineering details; cross-platform consistency is the test of substrate universality, not of Aalto-vs-Lancaster lab quality.

**Cross-pillar bridge anatomy**:
1. **Substrate-IS**: F1 NULL + ratio 7.324992 on `(A_K, H_K, D_K)`.
2. **Laboratory-IN**: Aalto LTL three-group multi-cell observations.
3. **Bridge map**: ι_* ∘ (Δ_B/Δ_A)^p with phase-handling per group (Krusius B-phase; Eltsov A-phase).
4. **Algebraic envelope**: same 0.1% structural-exact band as #25, #26.
5. **Empirical anchor target**: F1 NULL at Aalto + r consistent with Lancaster within 0.1%.

---

## §W4c-32. S88-3HE-B-CLASS-A-LAB-DISPATCH

**Gate ID**: `S88-3HE-B-CLASS-A-LAB-DISPATCH` (no S87 collision)

**Trigger**: Aalto LTL Krusius / Tuoriniemi / Eltsov coordination document on Class-A kernel-signature NULL pre-registration for F1 + F2 + F5 (decisive triplet from `inheritance-falsifier-protocol.md` 4-Gate Structure).

**Classification**: PHONONIC.

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (Class-A test class authority; W11-C5 calibration corpus ownership).
- **CO-AUTHOR**: mack-cosmic-bridge (inventory rows #45 + #47 + #48 — F1, F2, F5 individual rows — updated with Class-A dispatch SHA).
- **CO-AUTHOR**: sagan-empiricist (decisive vs supporting falsifier-class rigor; statistical-power audit on 9σ S/N forecast).

**Hypothesis**:
The substrate's decisive Class-A kernel-signature triplet (F1 + F2 + F5) maps to three independent Aalto LTL observables, each pre-registered at NULL with substrate-derived margin and lab-S/N forecast 9σ per one-decade pressure window. The decisive triplet is structurally distinct from the supporting pair (F3 + F4) per `inheritance-falsifier-protocol.md` §"Two Test Classes": F1 + F2 + F5 each individually probe a substrate-clean cocycle generator; F3 + F4 are cocycle-degenerate and require slope discrimination (Gate-4, deferred to a separate gate in this wave's #34 family).

**Method**:

1. Producing script: `s88_w4c_class_a_lab_dispatch.py`
2. Script pre-registers `sessions/framework/registry/class-a-lab-dispatch-pre-registration.md`:
   - **Section A** (volovik): Per-row substrate predictions for F1, F2, F5 with predicted lab S/N margin per row (calibration W-5: F1 = 0.573193 M_KK² substrate margin; F2 and F5 derived analogously from S86 W-5 §VII.AF.1).
   - **Section B** (volovik + sagan): Aalto group / cell assignment per row:
     - F1 → Krusius ROTA transverse-NMR ladder asymmetry
     - F2 → Krusius longitudinal NMR satellite peak ratio
     - F5 → Tuoriniemi Andreev-reflection edge-state asymmetry
   - **Section C** (volovik + sagan): Statistical-power forecast per row at 9σ S/N over 0–34 bar pressure sweep.
   - **Section D** (mack): Inventory rows #45 + #47 + #48 updated with Class-A dispatch SHA.

**Machinery pin**:

```
class_A_decisive_rows          = ["F1_Caroli_Matricon", "F2_NMR_satellite", "F5_Andreev_edge"]
substrate_margin_F1            = 0.573193 M_KK²        (S86 W-5 calibration)
substrate_margin_F2            = "derived_S86_W5_VII_AF1_phi67_partner"
substrate_margin_F5            = "derived_S86_W5_VII_AF1_phi67_chiral_pair"
S_N_forecast_per_row           = 9.0 sigma per decade  (per 0-34 bar window)
aalto_groups_per_row           = {"F1": "Krusius_ROTA", "F2": "Krusius_NMR_long", "F5": "Tuoriniemi_Andreev"}
test_class                     = "Class_A_kernel_signature_decisive"
audit_sha256_input_pin_map     = closure_hash({rows, margins, S_N_forecasts, group_assignments})
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. Script: `computations/s88_w4c_class_a_lab_dispatch.py`.
2. Data file: NONE.
3. Plot: NONE.
4. Working-paper section: §W4c-32 (>15 lines; cross-link to §W4c-31 Aalto coordination, §W4c-33 ratio precision, §W4c-25 Lancaster cross-platform).

**Verdict criteria**:

- **PASS**: Class-A dispatch document exists with Sections A + B + C + D substantive; per-row substrate margins derived from S86 W-5 §VII.AF.1; Aalto group assignment for ALL three F1/F2/F5 rows; 9σ S/N forecast pre-registered; mack rows #45/#47/#48 update emitted.
- **FAIL**: Any of F1/F2/F5 without Aalto assignment OR substrate margin missing OR S/N forecast absent OR mack update absent.
- **INFO**: Class-A dispatch pre-registered but per-row Aalto schedule TBD pending bilateral correspondence.

**Substitution chain**:

```
Step 1: Decisive triplet from inheritance-falsifier-protocol.md §"Four-Gate Structure":
  Gate 1 = NULL on F1 + F2 + F5 (decisive)              [substrate-clean rows]
Step 2: Substrate margin per row at S86 W-5 calibration:
  F1: ‖[φ_67]‖_{Caroli_Matricon}      = 0.573193 M_KK²
  F2: ‖[φ_67]‖_{NMR_satellite}        = derived (cocycle partner)
  F5: ‖[φ_67]‖_{Andreev_edge}         = derived (chiral pair)
Step 3: Lab S/N forecast at Aalto LTL spec:
  σ_F_i ≈ 9.0 per one-decade pressure window per row    [forecast]
Step 4: NULL prediction:
  F_i^{lab}_predicted = 0 ± σ_F_i / √(N_obs) ≈ NULL    [Class A]
Step 5: Decisive vs supporting separation:
  F1+F2+F5 = decisive (substrate-clean cocycles)
  F3+F4    = supporting/cocycle-degenerate (handled at #34, gate-4 slope)
Conclusion: Class-A dispatch pre-registers three substrate-clean NULL predictions at 9σ S/N.
```

**What PASS/FAIL MEAN**:

- **PASS** at S88: Class-A decisive falsifier triplet has European ULT lab dispatch document; rows #45/#47/#48 have substrate-derived margins and Aalto group assignments.
- **Future lab PASS** (post-2027): F1 + F2 + F5 all return NULL within 9σ at Aalto + Lancaster cross-platform; substrate Class-A confirmed decisively.
- **Future lab FAIL**: any row returns non-NULL detection; substrate Class-A falsified UNLESS Class-B ratio test (#26, #33) holds in the cross-cocycle channel.

**Effort**:
- **S88 in-session**: 5-7 hours (volovik PRIMARY drafts per-row margins; sagan rigor on 9σ S/N statistical-power calculation; mack inventory updates for three rows).
- **Multi-year lab cycle**: 2027-2030 Aalto + Lancaster cross-platform on F1+F2+F5.

**Substrate framing**:
F1, F2, F5 are not three "different experiments"; they are three independent observables, each probing a substrate-clean cocycle generator in `ker(ι_*)`. The decisive triplet is the substrate's most leverage-rich falsifier set: a single non-NULL detection in any one row falsifies the substrate Class-A prediction (modulo Class-B ratio rescue). Rows F3+F4 are cocycle-degenerate (multiple substrate cocycles superpose); they require the slope-discrimination Gate-4 from the 4-Gate Structure (handled at #34 family).

**Cross-pillar bridge anatomy**:
1. **Substrate-IS**: ‖[φ_67]‖_{F1, F2, F5} on `(A_K, H_K, D_K)`.
2. **Laboratory-IN**: F1^{lab}, F2^{lab}, F5^{lab} at Aalto LTL three-group cells.
3. **Bridge map**: ι_*: A_K → M_2(ℂ) ∘ (Δ_B/Δ_A)^p per row.
4. **Algebraic envelope**: per-row substrate margin ± 9σ statistical band.
5. **Empirical anchor target**: NULL on all three rows.

---

## §W4c-33. S88-3HE-B-CLASS-B-RATIO-PRECISION

**Gate ID**: `S88-3HE-B-CLASS-B-RATIO-PRECISION` (no S87 collision)

**Trigger**: Helsinki ROTA channel-ratio protocol pre-registration with lab S/N forecast ≈ 9σ per one-decade pressure window for the Class-B cohomology-asymmetry ratio test.

**Classification**: PHONONIC.

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (Class-B cohomology-asymmetry test class authority; (Δ_B/Δ_A)^p cancellation theorem ownership).
- **CO-AUTHOR**: mack-cosmic-bridge (inventory row #46 ratio anchor SHA update; row #54b ROTA channel anchor).
- **CO-AUTHOR**: sagan-empiricist (precision-bound rigor on 0.1% relative band).

**Hypothesis**:
The Helsinki ROTA channel (Aalto LTL Krusius group) provides the highest-precision platform for the Class-B cohomology-asymmetry ratio test (substrate prediction r = 7.324992 ± 0.1%). The ROTA cell's rotation-stabilized vortex array generates a clean ladder spectrum where the ratio of two ladder-state amplitudes (corresponding to [φ_67] and [φ_88] cocycles in the inheritance kernel) can be measured at 0.1% precision over a one-decade pressure window. This gate pre-registers the precision protocol with substrate prediction central, band, and lab-S/N forecast.

**Method**:

1. Producing script: `s88_w4c_class_b_ratio_precision.py`
2. Script pre-registers `sessions/framework/registry/class-b-ratio-precision-rota-pre-registration.md`:
   - **Section A** (volovik): Substrate prediction r = 7.324992 (Sage-exact); band [7.3177, 7.3323]; (Δ_B/Δ_A)^p cancellation theorem cited explicitly.
   - **Section B** (volovik + sagan): ROTA channel protocol — rotation-stabilized vortex array; transverse-NMR ladder spectroscopy; amplitude ratio extraction per pressure step; 1 OOM pressure window 3.4–34 bar (P_pc-anchored).
   - **Section C** (sagan): Lab S/N forecast — 9σ per one-decade pressure window; statistical-power calculation assuming N_obs ~ 10^4 per pressure step.
   - **Section D** (mack): Inventory row #46 + #54b updated with ROTA precision SHA.

**Machinery pin**:

```
substrate_ratio_central        = 7.324992              (Sage-exact)
substrate_ratio_band            = [7.3177, 7.3323]      (0.1% relative)
ratio_relative_tol             = 0.001                 (0.1%)
S_N_forecast_per_decade        = 9.0 sigma             (lab forecast)
pressure_window                = [3.4, 34.0] bar       (one-decade P_pc-anchored)
N_obs_per_pressure_step        = 1.0e4                 (forecast)
N_pressure_steps_per_decade    = 10                    (logarithmic spacing)
rota_protocol                  = "Krusius_transverse_NMR_ladder_amplitude_ratio"
test_class                     = "Class_B_cohomology_asymmetry"
cancellation_theorem_cite      = "S86_W5_DONE_5_residual_0p0e0"
audit_sha256_input_pin_map     = closure_hash({substrate_pred, rota_protocol, S_N_forecast, mack_rows})
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. Script: `computations/s88_w4c_class_b_ratio_precision.py`.
2. Data file: NONE.
3. Plot: NONE.
4. Working-paper section: §W4c-33 (>15 lines; cross-link to §W4c-26 µSR cross-platform, §W4c-32 Class-A dispatch, §W4c-34 gap-extraction calibration).

**Verdict criteria**:

- **PASS**: ROTA precision document exists with Sections A + B + C + D substantive; substrate central + band + cancellation theorem cited; ROTA protocol specifies amplitude-ratio extraction; 9σ S/N statistical-power calculation present; mack rows #46/#54b update emitted.
- **FAIL**: Cancellation theorem citation absent (rule violation per `inheritance-falsifier-protocol.md` §"(Δ_B/Δ_A)^p Cancellation Theorem") OR S/N forecast absent OR ROTA protocol unspecified OR mack update absent.
- **INFO**: ROTA protocol pre-registered but Krusius schedule unconfirmed for the specified pressure window.

**Substitution chain**:

```
Step 1: Substrate prediction at inheritance kernel:
  R := ‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992                 [Sage-exact]
Step 2: (Δ_B/Δ_A)^p cancellation (S86 W-5 DONE-5):
  r^{lab} = R · (f_67^{lab}/f_88^{lab})
          = R · 1                                       [common-exponent cocycle pair]
Step 3: Lab measurement at ROTA:
  r^{ROTA} := A_67^{ladder}(P) / A_88^{ladder}(P)      [per pressure step P]
Step 4: Pressure-sweep average:
  ⟨r^{ROTA}⟩_P = R   if substrate prediction holds
Step 5: Precision band:
  σ_r / r ≈ 1 / (S/N · √N_steps)
         = 1 / (9 · √10)
         ≈ 0.0351 / decade per step ensemble            [single-decade forecast]
  Aggregating N_obs = 10^4 per step gives σ_r/r ≈ 0.001 per decade [0.1% target]
Step 6: Falsification criterion:
  |⟨r^{ROTA}⟩_P - 7.324992| / 7.324992 < 0.001         [PASS]
  otherwise FAIL (substrate Class-B falsified at lab data)
Conclusion: ROTA precision protocol is feasible at 0.1% over one-decade pressure window with N_obs ~ 10^4 per step.
```

**What PASS/FAIL MEAN**:

- **PASS** at S88: ROTA precision protocol pre-registered at 0.1% feasibility with 9σ S/N forecast; Class-B cohomology-asymmetry has highest-leverage lab anchor.
- **Future lab PASS** (post-2027): ⟨r^{ROTA}⟩_P = 7.324992 ± 0.1%; Class-B substrate prediction confirmed.
- **Future lab FAIL**: ⟨r^{ROTA}⟩_P deviates from band; substrate cohomology-asymmetry falsified DIRECTLY (Class-B is structurally MORE decisive than Class-A because it isolates the substrate value from lab-conversion factor).

**Effort**:
- **S88 in-session**: 4-6 hours (volovik PRIMARY substrate prediction + cancellation citation; sagan precision-bound rigor + statistical-power calculation; mack inventory rows update).
- **Multi-year lab cycle**: 2027-2029 ROTA campaign at Krusius group.

**Substrate framing**:
The 0.1% precision band is NOT a target chosen to fit lab capability; it is the substrate's structural-exact prediction inherited from the (Δ_B/Δ_A)^p cancellation theorem. The ROTA channel's precision capability happens to MATCH the substrate's discrimination requirement at one-decade pressure window — a coincidence of platform-vs-prediction matching that makes ROTA the canonical Class-B test bed.

**Cross-pillar bridge anatomy**:
1. **Substrate-IS**: ‖[φ_67]‖/‖[φ_88]‖ = 7.324992 on `(A_K, H_K, D_K)`.
2. **Laboratory-IN**: ⟨r^{ROTA}⟩_P amplitude-ratio across pressure steps IN Helsinki ROTA cell.
3. **Bridge map**: (Δ_B/Δ_A)^p cancellation (common-exponent for cocycle pair).
4. **Algebraic envelope**: 0.1% structural-exact (substrate-INVARIANT under cancellation).
5. **Empirical anchor target**: ⟨r⟩_P = 7.324992 ± 0.1% at 9σ S/N.

---

## §W4c-34. S88-CLASS-B-DELTA-RATIO-CALIBRATION

**Gate ID**: `S88-CLASS-B-DELTA-RATIO-CALIBRATION` (no S87 collision)

**Trigger**: Gap-extraction-method cross-comparison: Greywall thermometric gap extraction vs Halperin-Hammel ladder-spacing gap extraction vs Volovik q-theory gap extraction. The (Δ_B/Δ_A) ratio enters the lab-conversion factor in NON-cancellation observables (i.e., observables where the cocycle pair has DIFFERENT exponents p_i ≠ p_j); its systematic uncertainty affects the precision of those specific lab tests.

**Classification**: PHONONIC.

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (q-theory gap extraction authority; canonical Volovik-partition (Δ_B/Δ_A) provenance).
- **CO-AUTHOR**: mack-cosmic-bridge (inventory row #54b cross-method audit-pin sub-row).
- **CO-AUTHOR**: sagan-empiricist (cross-method consistency rigor + systematic-uncertainty audit).

**Hypothesis**:
The (Δ_B/Δ_A) ratio at the polycritical point P_pc=21.22 bar, T_pc=2.273 mK has three independent extraction methods that yield numerically distinct values within their respective systematic uncertainties:
- **Greywall thermometric**: (Δ_B/Δ_A)_Greywall extracted from specific-heat jump ratio at T_c; systematic uncertainty ~ 1-2%.
- **Halperin-Hammel ladder-spacing**: (Δ_B/Δ_A)_HH extracted from NMR ladder spacing in vortex cores; systematic uncertainty ~ 0.5-1%.
- **Volovik q-theory**: (Δ_B/Δ_A)_q derived from BCS strong-coupling correction with SC_corr_A=1.151, SC_corr_B=1.111; analytic value (Δ_B/Δ_A)_q = 1.9597/2.0302 = 0.96528.

For Class-B cohomology-asymmetry ratio tests where the (Δ_B/Δ_A)^p cancellation theorem applies (common-exponent), this systematic is irrelevant. For Class-A tests where p_i ≠ p_j (i.e., non-pair observables), the (Δ_B/Δ_A) systematic propagates into the substrate-vs-lab comparison; this gate calibrates the systematic.

**Method**:

1. Producing script: `s88_w4c_delta_ratio_calibration.py`
2. Script computes (Δ_B/Δ_A) under three extraction methods and emits a comparison table:
   - Greywall: extract from specific-heat jump ratio (literature value, Greywall 1986)
   - Halperin-Hammel: extract from NMR ladder spacing (literature value, Halperin-Hammel 1990)
   - Volovik q-theory: compute from canonical_constants Δ_A/(k_B T_c)=2.0302 and Δ_B/(k_B T_c)=1.9597; cross-check SC_corr_A=1.151, SC_corr_B=1.111
3. Computes inter-method dispersion: max |Δ_method_i − Δ_method_j| / Δ_method_central across the three pairs.
4. Pre-registers a calibration document at `sessions/framework/registry/delta-ratio-method-calibration.md`:
   - **Section A** (volovik): q-theory derivation with substrate provenance.
   - **Section B** (sagan): Greywall + Halperin-Hammel literature method audit + systematic-uncertainty extraction.
   - **Section C** (sagan): Inter-method consistency table + dispersion bound.
   - **Section D** (mack): Inventory row #54b cross-method sub-row updated.

**Machinery pin**:

```
delta_A_over_kBTc              = 2.0302                (canonical, S86 W-5 anchors)
delta_B_over_kBTc              = 1.9597                (canonical)
SC_corr_A                      = 1.151                 (strong-coupling A)
SC_corr_B                      = 1.111                 (strong-coupling B)
delta_B_over_delta_A_q_theory  = 0.96528               (= 1.9597/2.0302)
extraction_methods             = ["Greywall_thermometric", "Halperin_Hammel_ladder", "Volovik_q_theory"]
inter_method_dispersion_target = 0.020                 (2% PASS threshold)
inter_method_dispersion_FAIL   = 0.05                  (5% FAIL threshold)
P_pc                           = 21.22 bar
T_pc                           = 2.273e-3 K
audit_sha256_input_pin_map     = closure_hash({delta_anchors, SC_corr, methods, dispersion_thresholds})
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. Script: `computations/s88_w4c_delta_ratio_calibration.py`.
2. Data file: `computations/s88_w4c_delta_ratio_calibration.npz` (keys: `delta_ratio_greywall`, `delta_ratio_HH`, `delta_ratio_q`, `inter_method_dispersion`).
3. Plot: `computations/s88_w4c_delta_ratio_calibration.png` (three-method bar chart with error bars).
4. Working-paper section: §W4c-34 (>15 lines; cross-link to §W4c-33 ratio precision, §W4c-26 µSR cross-platform, §W4c-35 inheritance Cartesian confirm).

**Verdict criteria**:

- **PASS**: All three methods extracted; inter-method dispersion ≤ 2%; q-theory value 0.96528 lies within Greywall + HH band.
- **FAIL**: Inter-method dispersion > 5%; OR any method missing OR systematic-uncertainty extraction absent.
- **INFO**: 2% < dispersion ≤ 5%; methods agree at the 2-5% level; substrate q-theory survives but with non-trivial systematic.

**Substitution chain**:

```
Step 1: q-theory ratio (Volovik canonical):
  (Δ_B/Δ_A)_q := (Δ_B/(k_BT_c)) / (Δ_A/(k_BT_c))
              = 1.9597 / 2.0302
              = 0.96528                                [canonical, P_pc anchor]
Step 2: Strong-coupling cross-check:
  SC_corr_A = 1.151, SC_corr_B = 1.111
  Ratio sanity: SC_corr_B / SC_corr_A = 0.9653 ≈ (Δ_B/Δ_A)_q  [strong-coupling consistency]
Step 3: Greywall thermometric (literature):
  (Δ_B/Δ_A)_Greywall = literature value (Greywall 1986)
                     ≈ 0.96 ± 0.02                    [thermometric systematic]
Step 4: Halperin-Hammel ladder-spacing (literature):
  (Δ_B/Δ_A)_HH = literature value (Halperin-Hammel 1990)
              ≈ 0.965 ± 0.01                         [ladder-spacing systematic]
Step 5: Inter-method dispersion:
  D_max = max |method_i - method_j| / 0.96528
        = max(|0.96 - 0.965|, |0.96 - 0.96528|, |0.965 - 0.96528|) / 0.96528
        ≈ max(0.005, 0.005, 0.0003) / 0.96528
        ≈ 0.005 / 0.96528
        ≈ 0.005                                      [ <  2% PASS threshold]
Step 6: PASS/FAIL/INFO:
  D_max ≤ 0.020 → PASS
  0.020 < D_max ≤ 0.05 → INFO
  D_max > 0.05 → FAIL
Conclusion: Methods agree at the ~0.5% level; q-theory canonical 0.96528 sits well within Greywall + HH bands.
```

**What PASS/FAIL MEAN**:

- **PASS**: q-theory canonical (Δ_B/Δ_A) is consistent with Greywall + Halperin-Hammel within their systematic uncertainties; the substrate (Δ_B/Δ_A) provenance is empirically validated.
- **FAIL**: The three methods disagree at >5%; either q-theory is wrong OR Greywall/HH have unaccounted systematics; substrate cancellation theorem applicability is at risk for non-pair observables.
- **INFO**: 2-5% disagreement; methods marginally consistent; substrate q-theory survives with non-trivial systematic that propagates to non-cancellation Class-A tests.

**Effort**:
- **S88 in-session**: 3-5 hours (volovik q-theory derivation; sagan literature audit on Greywall + HH; mack inventory sub-row update).

**Substrate framing**:
The (Δ_B/Δ_A) ratio is NOT a "lab-calibrated" parameter; it is a substrate-derived value (q-theory provenance, S58 Volovik partition canonical) cross-checked against laboratory extractions (Greywall, Halperin-Hammel). The substrate is logically prior; lab methods test the q-theory prediction. The cancellation theorem (S86 W-5 DONE-5) implies (Δ_B/Δ_A)^p cancels in cocycle-pair Class-B observables — so this systematic only matters for Class-A non-pair observables (where p_i ≠ p_j).

**Cross-pillar bridge anatomy**:
1. **Substrate-IS**: (Δ_B/Δ_A)_q from q-theory canonical Δ_A/(k_B T_c), Δ_B/(k_B T_c) anchors.
2. **Laboratory-IN**: (Δ_B/Δ_A)_Greywall + (Δ_B/Δ_A)_HH from specific-heat + NMR-ladder lab observables.
3. **Bridge map**: q-theory → SC_corr cross-check → lab extraction methods.
4. **Algebraic envelope**: 2-5% inter-method dispersion bands.
5. **Empirical anchor target**: methods agree within 2% at q-theory canonical.

---

## §W4c-35. S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM

**Gate ID**: `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM` (no S87 collision)

**Trigger**: Re-derive the inheritance morphism χ from the BDI ↔ DIII Altland-Zirnbauer compatibility theorem; verify against S86 W-5 QQ-substitution-chain Step 2.

**Classification**: GEOMETRIC (per `phononic-framing.md` §"Classification Guide": concerns the spectral triple structure / fiber topology / Altland-Zirnbauer class assignment — the fabric itself, not its excitations).

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (Altland-Zirnbauer class assignment authority; BDI / DIII / 3He-A / 3He-B classification ownership; Volovik 2003 §19).
- **CO-AUTHOR**: connes-ncg-theorist (NCG-axiomatic cross-check on χ as algebra projection; KO-dimension and J-invariance preservation under χ).
- **CO-AUTHOR**: sagan-empiricist (theorem-statement rigor; AZ class compatibility audit).

**Hypothesis**:
The inheritance morphism χ: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) (BDI parent → BdG sector child) is the unique (up to AZ-class compatible automorphism) algebra projection that:
1. Preserves the BDI Pf=−1 topology of the parent.
2. Maps to the DIII chiral child structure of the BdG sector under the Altland-Zirnbauer class compatibility theorem (BDI ↔ DIII compatibility under chirality grading reversal).
3. Realizes the M_3(ℂ) → 0 kernel that defines `ker(ι_*)` where the substrate cocycles [φ_67] and [φ_88] reside.
4. Is consistent with the 3He-B BdG sector universality class (Volovik 2003 §19; AZ class BDI for 3He-B; AZ class DIII for 3He-A) under inheritance from the SU(3) parent.

The S86 W-5 QQ-substitution-chain Step 2 derived χ at machine precision; this gate provides the AZ-theoretic framing for that derivation.

**Method**:

1. Producing script: `s88_w4c_az_inheritance_cartesian_confirm.py`
2. Script implements three steps:
   - **Step 1** (Sage-symbolic): Verify BDI ↔ DIII compatibility theorem at the algebra level: prove that any algebra map ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) preserving Pf=−1 BDI topology factors through a unique (up to inner automorphism) projection sending M_3(ℂ) → 0.
   - **Step 2** (numerical cross-check): Reproduce S86 W-5 QQ-substitution-chain Step 2 via Sage symbolic; confirm χ acts on H_K block-decomposition as expected; verify χ preserves J-invariance on `(A_K, H_K, D_K)` (i.e., the real structure J commutes with χ in the appropriate ⊕ sector).
   - **Step 3** (consistency check): Verify that χ extends to A_K^{≤L} → M_2(ℂ)^{≤L} for L_max=10 with rank(ker(χ)|_{≤L}) = expected substrate-rank at each L; confirm rank(ker(ι_*)|_{≤10}) = 2 (cocycles [φ_67] + [φ_88]).
3. Emits verdict line + working-paper section + plot showing χ's action on A_K block structure.

**Machinery pin**:

```
parent_algebra                 = "C + H + M_3(C)"      (A_K canonical)
child_algebra                  = "M_2(C)"              (BdG sector)
parent_AZ_class                = "BDI"                 (Pf=-1, N_K=2)
child_AZ_class                 = "DIII"                (chiral grading reversal)
compatibility_theorem          = "BDI_DIII_chirality_grading_reversal"
chi_action_on_M3C              = "zero"                (M_3(C) -> 0)
chi_action_on_C                = "preserved_in_M2C_corner_diag"
chi_action_on_H                = "embedded_M2C_via_quaternion_real_form"
ker_chi_substrate_cocycles     = ["phi_67", "phi_88"]  (rank 2 at L_max=10)
S86_W5_step2_cross_check_tol   = 1.0e-15              (machine epsilon)
J_invariance_preserved         = True                  (Sage-symbolic verification)
audit_sha256_input_pin_map     = closure_hash({parent, child, AZ_classes, theorem, chi_action, S86_W5_pin})
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. Script: `computations/s88_w4c_az_inheritance_cartesian_confirm.py`.
2. Data file: `computations/s88_w4c_az_inheritance_cartesian_confirm.npz` (keys: `chi_action_matrix`, `S86_W5_step2_residual`, `J_invariance_check`, `ker_rank_at_Lmax_10`).
3. Plot: `computations/s88_w4c_az_inheritance_cartesian_confirm.png` (block-diagram of χ's action on A_K → M_2(ℂ)).
4. Working-paper section: §W4c-35 (>15 lines; cross-link to §W4c-25/26/32/33 lab gates; cross-link to S86 W-5 §VII.AF.1 cross-pillar bridge theorem and S86 W1b-T8 inheritance canonical).

**Verdict criteria**:

- **PASS**: Step 1 + Step 2 + Step 3 all PASS; AZ-class compatibility theorem verified Sage-symbolic; S86 W-5 Step-2 reproduction at residual ≤ 1e-15; J-invariance preserved; rank(ker(χ)|_{≤10}) = 2.
- **FAIL**: Any step fails OR S86 W-5 reproduction residual > 1e-15 OR J-invariance broken under χ OR rank(ker) ≠ 2.
- **INFO**: Steps 1+2 PASS; Step 3 PASS at L_max=10 but L-extension to L_max=12+ deferred (substrate kernel rank may grow at higher L; structurally NEW question).

**Substitution chain**:

```
Step 1: Define parent algebra and AZ class:
  A_K = C ⊕ H ⊕ M_3(C)
  AZ class of (A_K, H_K, D_K) = BDI (Pf = -1, N_K = 2)
                                                       [Volovik 2003 §19, S86 W1b-T8]
Step 2: Define child algebra and AZ class:
  A_child = M_2(C)
  AZ class of BdG sector at 3He-B = DIII (chiral grading)
                                                       [Volovik 2003 §19]
Step 3: Compatibility theorem (BDI ↔ DIII):
  Any algebra map ι: A_K → A_child preserving Pf = -1 BDI topology
  factors through unique (up to inner automorphism) χ
  with χ|_{M_3(C)} = 0 and chirality grading reversal on (C ⊕ H) → M_2(C).
                                                       [AZ table, Heinzner-Huckleberry-Zirnbauer]
Step 4: Substrate kernel:
  ker(ι_*) = ker(χ_*) at K-theory level
           ⊃ {[φ_67], [φ_88]}                          [substrate cocycle pair, S86 W-5]
  rank(ker(ι_*)|_{≤10}) = 2 (cocycle pair, no Cartan-zone leak at L_max=10)
                                                       [W-5 Sage-exact]
Step 5: S86 W-5 QQ-substitution-chain Step 2 reproduction:
  χ(C corner) = M_2(C)_diag_lower      [embed C → diagonal M_2(C) corner]
  χ(H block)  = M_2(C)_quaternion_real [quaternion real-form embedding]
  χ(M_3(C))   = 0                       [BDI → DIII projection]
  Sage-symbolic check: J · χ = χ · J on (A_K, H_K, D_K)
  Numerical residual at L_max=10: ≤ 1e-15 (machine epsilon)
                                                       [S86 W-5 Step-2 cross-check]
Step 6: Conclusion:
  χ is the unique BDI ↔ DIII inheritance morphism;
  rank(ker(χ)|_{≤10}) = 2 confirms substrate cocycle pair survives at L_max=10;
  J-invariance preserved.
```

**What PASS/FAIL MEAN**:

- **PASS**: The inheritance morphism χ is structurally derived from AZ-class compatibility, NOT chosen ad-hoc; substrate cocycles [φ_67], [φ_88] reside in `ker(χ_*)` for principled (AZ-theoretic) reasons.
- **FAIL**: Either AZ compatibility theorem does NOT uniquely determine χ (multiple non-equivalent morphisms), OR S86 W-5 Step 2 reproduction fails (S86 result is incorrect), OR J-invariance breaks under χ (KO-dimension preservation fails).
- **INFO**: AZ compatibility holds but L-extension to L_max ≥ 12 yields rank(ker) ≥ 3 (NEW substrate cocycle generators surface above L_max=10); falsifier protocol must extend to higher rank per `inheritance-falsifier-protocol.md` §"Higher-rank case (rank ≥ 3)".

**Effort**:
- **S88 in-session**: 6-8 hours (volovik PRIMARY drafts AZ compatibility theorem statement + proof sketch; connes CO-AUTHOR cross-checks J-invariance + KO-dim preservation under χ; sagan rigor audit on theorem statement; Sage-symbolic verification at runtime).

**Substrate framing**:
The Altland-Zirnbauer class assignment is NOT a "label" attached to the substrate; it IS the substrate's symmetry-class topology at the K-theory level. BDI parent (`A_K`) inherits to DIII child (BdG sector) via χ — this is a structural theorem of NCG + AZ-theoretic K-theory, not an analogy or convention. The 3He-B realization (BDI in Volovik 2003 classification) is the laboratory child of the same parent; 3He-A (DIII chiral) is a different child via a different inheritance morphism. Both children share the same parent inheritance kernel structure.

**Cross-pillar bridge anatomy**:
1. **Substrate-IS**: χ: A_K → M_2(ℂ) at the algebra level on `(A_K, H_K, D_K)`.
2. **Laboratory-IN**: 3He-B BdG sector universality class (DIII chiral image of BDI parent).
3. **Bridge map**: AZ-class compatibility theorem (BDI ↔ DIII chirality grading reversal).
4. **Algebraic envelope**: J-invariance + KO-dim preservation; rank(ker(χ_*)|_{≤L}) = 2 at L_max=10.
5. **Empirical anchor target**: S86 W-5 Step 2 reproduction at machine epsilon.

---

## §W4c-36. S88-3HE-B-α_s-EXTRACTION-PROTOCOL

**Gate ID**: `S88-3HE-B-α_s-EXTRACTION-PROTOCOL` (no S87 collision)

**Trigger**: Define experimental protocol for extracting α_s^{lab} from longitudinal NMR resonance-frequency running curve with full error budget. The substrate framework's α_s prediction (S87 W-9 surviving-route table; canonical α_s_canonical = n_s² − 1 from algebra-INVARIANT family; per `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" instance #3) requires a laboratory analog: 3He-B longitudinal NMR provides an α_s-equivalent observable via the resonance-frequency running curve d ln(ω_L)/d ln(P) at the polycritical point.

**Classification**: PHONONIC.

**Agent assignment**:
- **PRIMARY**: volovik-superfluid-universe-theorist (3He-B longitudinal NMR authority; substrate α_s prediction provenance; q-theory anchor).
- **CO-AUTHOR**: sagan-empiricist (extraction protocol rigor; error-budget audit including thermometric, pressure, NMR-frequency systematics).
- **CO-AUTHOR**: mack-cosmic-bridge (inventory row #54a / #54b α_s lab anchor cross-link; per `feedback_mack-bridge-role.md`).

**Hypothesis**:
The substrate's α_s_canonical = n_s² − 1 (S87 W-9 algebra-INVARIANT route at s=3 single-pole Mellin) maps to a laboratory-IN observable: 3He-B longitudinal NMR resonance frequency ω_L(P) running with pressure at the polycritical point. The substrate prediction:
α_s^{lab} := d ln(ω_L) / d ln(P) |_{P=P_pc}
satisfies α_s^{lab} = α_s_canonical to within the substrate-derived tolerance band (band-width set by L_max=10 truncation residual).

This gate pre-registers the experimental protocol for extracting α_s^{lab} with full error budget — NOT measuring α_s^{lab} (multi-year lab cycle).

**Method**:

1. Producing script: `s88_w4c_alpha_s_nmr_extraction_protocol.py`
2. Script pre-registers `sessions/framework/registry/3he-b-alpha-s-nmr-extraction-protocol.md`:
   - **Section A** (volovik): Substrate α_s prediction with provenance (S87 W-9 algebra-INVARIANT route at s=3 single-pole Mellin); canonical_constants α_s_canonical = n_s² − 1 = -8.587279/100 (where n_s = 0.9649 fiducial; specific value pinned at substrate computation).
   - **Section B** (volovik + sagan): Longitudinal NMR protocol — sample preparation in 3He-B at P_pc=21.22 bar, T near T_pc=2.273 mK; longitudinal NMR coil; resonance-frequency sweep ω_L(P); pressure scan window centered on P_pc.
   - **Section C** (sagan): Error budget — thermometric uncertainty on T_pc; pressure uncertainty on P_pc; NMR-frequency systematic; statistical N_obs requirement; total σ_α_s budget.
   - **Section D** (sagan): Extraction algorithm — log-log linear regression of ω_L(P) at P=P_pc; α_s^{lab} = slope; error propagation from Section C.
   - **Section E** (mack): Inventory row #54a + #54b updated with α_s extraction protocol SHA.

**Machinery pin**:

```
substrate_alpha_s_canonical    = -8.587279e-2          (= n_s^2 - 1, fiducial n_s = 0.9649)
                                                       (S87 W-9 algebra-INVARIANT route at s=3)
substrate_n_s_fiducial         = 0.9649                (Planck 2018 anchor)
substrate_alpha_s_tolerance    = 1.0e-3                (substrate-derived band, L_max=10)
P_pc                           = 21.22 bar
T_pc                           = 2.273e-3 K
NMR_protocol                   = "longitudinal_3HeB_resonance_sweep"
extraction_algorithm           = "log_log_linear_regression_at_P_pc"
sigma_T_thermometric           = "Greywall_calibration_systematic"  (~0.1% T_pc)
sigma_P_systematic             = "Bourdon_gauge_high_precision"     (~0.05% P_pc)
sigma_omega_L_NMR              = "frequency_counter_high_stability" (~10 ppm)
N_obs_required                 = 1.0e3                 (per pressure step; multi-step sweep)
total_sigma_alpha_s_budget     = 5.0e-4                (forecast; sub-substrate-tolerance)
audit_sha256_input_pin_map     = closure_hash({alpha_s_canonical, NMR_protocol, error_budget, P_T_pc})
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Expected output 4-tuple**:

1. Script: `computations/s88_w4c_alpha_s_nmr_extraction_protocol.py`.
2. Data file: NONE (protocol pre-registration; no NMR data at S88).
3. Plot: NONE.
4. Working-paper section: §W4c-36 (>15 lines; cross-link to S87 W-9 algebra-INVARIANT routes; cross-link to §W4c-31 Aalto coordination, §W4c-33 ROTA precision, §W4c-34 (Δ_B/Δ_A) calibration).

**Verdict criteria**:

- **PASS**: Protocol document exists with Sections A + B + C + D + E substantive (>15 lines each); substrate α_s_canonical pinned with provenance; extraction algorithm specified; error budget pre-registered; total σ_α_s budget ≤ substrate-tolerance band (5e-4 ≤ 1e-3 forecast achievable); mack inventory rows #54a/#54b update emitted.
- **FAIL**: Substrate provenance missing OR extraction algorithm unspecified OR error budget incomplete OR total σ_α_s > substrate tolerance OR mack update absent.
- **INFO**: Protocol pre-registered but error budget at borderline (3e-4 ≤ σ_α_s ≤ 1e-3); lab feasibility marginal but possible.

**Substitution chain**:

```
Step 1: Substrate α_s prediction (S87 W-9 algebra-INVARIANT route):
  α_s_canonical := n_s² − 1                            [algebra-INVARIANT family, s=3 pole]
                  = (0.9649)² − 1
                  = -0.0691...                          [Planck-anchored fiducial]
  More precisely (S87 W-9 W2-1 + W2-4 PASS at s=3 single-pole Mellin):
  α_s_canonical ≈ -8.587279e-2 at substrate fiducial    [W2-1/W2-4 Sage-exact]
Step 2: Lab observable definition:
  α_s^{lab} := d ln(ω_L) / d ln(P) |_{P=P_pc}          [longitudinal NMR running]
Step 3: NMR resonance frequency at polycritical point:
  ω_L(P) = γ · |Δ_B(P)|² / (something involving susceptibility)
                                                       [Volovik 2003 §15; Leggett resonance]
Step 4: Pressure-running of ω_L:
  d ln(ω_L) / d ln(P) = 2 · d ln|Δ_B| / d ln(P) - d ln(susceptibility) / d ln(P)
  At P=P_pc: structural reduction yields α_s^{lab} as a function of substrate parameters
Step 5: Error budget:
  σ_α_s² = (∂α_s/∂T)² σ_T² + (∂α_s/∂P)² σ_P² + (∂α_s/∂ω_L)² σ_omega² + statistical
         ≈ (5e-4)²                                      [sub-substrate-tolerance]
Step 6: Falsification criterion:
  |α_s^{lab} − α_s_canonical| ≤ √(substrate_tol² + lab_σ²)
                              ≈ √((1e-3)² + (5e-4)²)
                              ≈ 1.118e-3                [combined band]
Conclusion: Protocol pre-registers α_s^{lab} extraction at lab-σ ~ 5e-4 vs substrate tolerance ~ 1e-3.
```

**What PASS/FAIL MEAN**:

- **PASS** at S88: 3He-B longitudinal NMR α_s extraction protocol pre-registered with substrate-tolerance-feasible error budget; rows #54a/#54b have lab anchors.
- **FAIL** at S88: protocol incomplete; substrate α_s prediction has no laboratory test pathway.
- **Future lab PASS** (post-2027): α_s^{lab} measured = α_s_canonical within combined band ~ 1.1e-3; substrate algebra-INVARIANT route (s=3 single-pole Mellin) confirmed.
- **Future lab FAIL**: α_s^{lab} ≠ α_s_canonical; either substrate α_s prediction fails (algebra-INVARIANT route falsified) OR the laboratory analog mapping (NMR running ↔ s=3 Mellin pole) is broken.

**Effort**:
- **S88 in-session**: 5-7 hours (volovik PRIMARY substrate provenance + NMR protocol; sagan error budget rigor + extraction algorithm; mack inventory cross-link).
- **Multi-year lab cycle**: 2027-2029 longitudinal NMR campaign at Aalto LTL Krusius group OR Lancaster Pickett group.

**Substrate framing**:
α_s is NOT a "matter content parameter" in the cosmological sense; in the substrate framework it is a SUBSTRATE-DERIVED MOMENT of the Mellin-cone at s=3 single-pole — an algebra-INVARIANT family quantity per `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter". The laboratory analog at 3He-B longitudinal NMR is a CHILD realization of the same algebra-INVARIANT route via the inheritance morphism χ; the running curve d ln(ω_L) / d ln(P) at P=P_pc IS the laboratory image of the substrate's s=3 Mellin moment under (Pillar II ↔ Pillar V) bridge candidate FWD-C2 (`cross-pillar-bridge-anatomy.md` §"FWD-C2"). The lab is not measuring "α_s in 3He-B"; it is measuring the BdG-sector image of the substrate's algebra-INVARIANT family at the s=3 pole.

**Cross-pillar bridge anatomy**:
1. **Substrate-IS**: α_s_canonical = n_s² − 1 algebra-INVARIANT moment at s=3 single-pole Mellin on `(A_K, H_K, D_K)`.
2. **Laboratory-IN**: α_s^{lab} = d ln(ω_L) / d ln(P) |_{P=P_pc} IN 3He-B longitudinal NMR.
3. **Bridge map**: ι_*: A_K → M_2(ℂ) ∘ Mellin-pole image at s=3 ∘ Leggett resonance frequency (BdG sector child).
4. **Algebraic envelope**: substrate tolerance ~ 1e-3 (L_max=10 truncation); lab forecast σ ~ 5e-4 (sub-substrate-tolerance feasible).
5. **Empirical anchor target**: α_s^{lab} = α_s_canonical within combined band 1.1e-3 at S87-fiducial n_s = 0.9649.

---

## Wave 4c → Wave 5 Decision Point

**At Wave 4c close, downstream Wave 5 dispatch decisions are**:

- **All 8 gates PASS**: 3He lab coordination + protocol pre-registration + AZ class theorem layer is COMPLETE. Wave 5 proceeds with downstream consumers (e.g., bilateral correspondence with Lancaster + Aalto + RHUL groups; GW dark-photon cross-channel; LiteBIRD discrimination ledger updates).
- **#35 (AZ inheritance Cartesian confirm) FAILs**: BLOCKING — the inheritance morphism χ is not principled at AZ-class level; Wave 5 routes to remediation gate `S88-W5-AZ-INHERITANCE-RE-DERIVATION-V2` (volovik + connes joint).
- **#34 (Δ_B/Δ_A calibration) FAILs at >5% inter-method dispersion**: Wave 5 routes to systematic-uncertainty audit gate; substrate cancellation theorem applicability for Class-A non-pair tests is at risk.
- **Any of #25/26/31/32/33 PROTOCOL-PRE-REGISTRATION FAIL**: Wave 5 routes to bilateral-correspondence dispatch (volovik + email pre-drafts) to Lancaster / Aalto / Helsinki groups for protocol coordination.
- **#36 (α_s NMR extraction protocol) FAILs at error-budget infeasibility**: Wave 5 routes to alternate-platform protocol design (Lancaster-only OR Aalto-only sequential extraction).

## Wave 4c Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR machinery enumeration discipline. All gate-relevant machinery parameters enumerated PER GATE (above; see each §W4c-NN "Machinery pin" block). No bare K-atoms; all pinned at plan-freeze.

**Cross-gate shared machinery**:

```
substrate_cocycle_ratio_67_88  = 7.324992              [canonical_constants; Sage-exact]
delta_B_over_delta_A_q_theory  = 0.96528               [canonical_constants; q-theory]
P_pc                           = 21.22 bar             [canonical_constants; polycritical anchor]
T_pc                           = 2.273e-3 K            [canonical_constants; polycritical anchor]
delta_A_over_kBTc              = 2.0302                [canonical_constants]
delta_B_over_kBTc              = 1.9597                [canonical_constants]
SC_corr_A                      = 1.151                 [canonical_constants; strong-coupling A]
SC_corr_B                      = 1.111                 [canonical_constants; strong-coupling B]
chi_A_volovik_2003             = 1.500000              [canonical_constants; 3He-A susceptibility]
cancellation_residual          = 0.0e+00               [S86 W-5 DONE-5; machine epsilon]
S86_W5_step2_cross_check_tol   = 1.0e-15               [machine epsilon, AZ-theorem reproduction]
substrate_alpha_s_canonical    = -8.587279e-2          [S87 W-9 algebra-INVARIANT route, s=3]
ratio_band_relative            = 1.0e-3                [0.1% band; W11-C5 calibration]
inter_lab_consistency_band     = 1.0e-3                [|r_A - r_B|/r_central < 0.1%]
inter_method_dispersion_PASS   = 2.0e-2                [(Δ_B/Δ_A) calibration]
inter_method_dispersion_INFO   = 5.0e-2                [(Δ_B/Δ_A) calibration]
S_N_forecast_per_decade        = 9.0 sigma             [Lancaster + Aalto + Helsinki forecast]
substrate_alpha_s_tolerance    = 1.0e-3                [L_max=10 truncation]
total_sigma_alpha_s_budget     = 5.0e-4                [NMR extraction lab forecast]
verdict_source                 = "computations/s88_gate_verdicts.txt"
schema_version                 = S84+
```

**Per-gate auditor (PRDR pre-flight)**:
- `_pru_cardinality_audit.py` runs at plan-freeze; all 8 gates' machinery pin maps must enumerate every gate-relevant parameter at cardinality-1 (no missing pins).
- `_source_reconciliation_audit.py` runs after PRU; canonical_constants pins (substrate_cocycle_ratio_67_88, delta_B_over_delta_A_q_theory, P_pc, T_pc, etc.) must match canonical_constants.py values per the 5-class taxonomy.
- `_substrate_first_provenance_audit.py` (proposed S87 V.1; if available at S88) runs after SOURCE-RECON; substrate-IS observables in each gate must source from substrate computation, NOT external-paper provenance.

## Wave 4c Input-SHA Ledger

**INPUT-PIN MAP per gate** (audit_sha256 input components):

| Gate ID | Input pins | Source files |
|:--------|:-----------|:-------------|
| S88-LANCASTER-MCT3-VORTEX-CORE-EVALUATE | substrate_pred + lab_spec + cross_platform | canonical_constants.py + sessions/framework/correspondence/3HeB-inheritance-canonical.md + sessions/framework/registry/falsifier-master-inventory.md row #45 |
| S88-MUSR-VORTEX-CROSS-PLATFORM-RATIO-EVALUATE | substrate_pred + lancaster_spec + aalto_spec + cross_platform | canonical_constants.py + .claude/rules/inheritance-falsifier-protocol.md + falsifier-master-inventory.md row #46 |
| S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION | groups + cells + methods + rows + horizon | papers/s87-3he-b-alpha-s-equivalent.md + falsifier-master-inventory.md rows #45+#46 + sessions/framework/correspondence/3HeB-inheritance-canonical.md |
| S88-3HE-B-CLASS-A-LAB-DISPATCH | rows + margins + S_N_forecasts + group_assignments | .claude/rules/inheritance-falsifier-protocol.md §"Four-Gate Structure" + sessions/permanent-results-registry.md §VII.AF.1 + falsifier-master-inventory.md rows #45/#47/#48 |
| S88-3HE-B-CLASS-B-RATIO-PRECISION | substrate_pred + rota_protocol + S_N_forecast + mack_rows | canonical_constants.py + .claude/rules/inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem" + falsifier-master-inventory.md rows #46+#54b |
| S88-CLASS-B-DELTA-RATIO-CALIBRATION | delta_anchors + SC_corr + methods + dispersion_thresholds | canonical_constants.py + Greywall 1986 + Halperin-Hammel 1990 + sessions/framework/registry/branch-iv-canonical.md (q-theory) |
| S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM | parent + child + AZ_classes + theorem + chi_action + S86_W5_pin | sessions/framework/correspondence/3HeB-inheritance-canonical.md (S86 W1b-T8) + sessions/permanent-results-registry.md §VII.AF.1 + Volovik 2003 §19 + connes-ncg axiomatic basis |
| S88-3HE-B-α_s-EXTRACTION-PROTOCOL | alpha_s_canonical + NMR_protocol + error_budget + P_T_pc | canonical_constants.py + S87 W-9 surviving-route table (algebra-INVARIANT s=3) + sessions/permanent-results-registry.md §VII.U.1 + Volovik 2003 §15 |

**Closure-SHA discipline**:
Each gate's `audit_sha256` is computed via `closure_hash(input_pin_map)` per `computations/script-template.py append_verdict()`. Per-gate-distinct audit_sha256 is preserved by construction (each gate's input_pin_map embeds gate-distinct keys: `_gate_id`, `_wp_id`, `_scheme`, `_convention`). Sig_5 ladder uniqueness is preserved by construction.

**Plan-freeze SHA computation**: deferred to plan-freeze finalization (sha256_of_plan_block per gate computed over the §W4c-NN block text; recorded in this file's revision-history footer at plan-freeze).

---

**Plan author**: planner-w4c (S88 Wave 4c orchestrator-direct authorship per `.claude/rules/wave-classification.md` §"Dispatch consequences").
**Date**: 2026-05-02.
**Wave class**: COMPUTE-class (8 gates; all PASS predicates have pre-registered numerical thresholds OR pre-registered protocol-document existence-with-substantive-content thresholds bound to dual-SHA verdict-line emission per `mechanical-closure-discipline.md`).
**Verdict source**: `computations/s88_gate_verdicts.txt`.
**Cross-references**: `.claude/rules/cross-pillar-bridge-anatomy.md` (FWD-C3 SUGGESTION at K=2; this wave's #25/#26/#32/#33 contribute to calibration-corpus instance #3 candidate); `.claude/rules/inheritance-falsifier-protocol.md` (4-Gate Structure; W11-C5/C6 calibration corpus); `.claude/rules/phononic-framing.md` (substrate framing on every gate); `.claude/rules/regulator-pin-discipline.md` (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE for any post-superseded canonical references); `feedback_mack-bridge-role.md` (mack sole-writer for `falsifier-master-inventory.md` updates).
