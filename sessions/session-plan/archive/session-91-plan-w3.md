# Session 91 Plan — Wave 3: Species-multiplicity cascade + LRD α-anchor parallel pathways

**Wave**: W3 (of S91)
**Total gate count**: 4
**Wave class**: MIXED (sub-classification per gate; two parallel tracks — Track A mack-led species-multiplicity cascade T1.6 → T1.7; Track B OAA-EXCLUDED-reviewer LRD α-anchor parallel pathways T1.8 + T1.9)
**Total effort**: ~8.5 wave-equivalents (T1.6 ~1.0 + T1.7 ~0.5 + T1.8 ~3.5 + T1.9 ~3.5)
**Dispatch path**: per-gate per-classification (compute-mode for T1.6/T1.8/T1.9 via `/rclab-coordinate` substantive computation gates; mechanical re-dispatch with Option-A supersedes for T1.7 conditional on T1.6 PASS). Track A (T1.6, T1.7) and Track B (T1.8, T1.9) are STRUCTURALLY INDEPENDENT (no shared upstream prerequisite); dispatch in parallel.
**Canonical verdict-file path** (per `gate-verdicts.md §"Canonical Verdict-File Path"`): `computations/session-91/s91_gate_verdicts.txt`. The variant `computations/_shared/s91_gate_verdicts.txt` is FORBIDDEN.

---

## Wave 3 Summary

Wave 3 dispatches four substrate-physics compute gates organized as two structurally INDEPENDENT tracks:

**Track A — Species-multiplicity cascade conditional chain (mack-led; T1.6 → T1.7)**. The S90 W4 CF-40 verdict closed the simplified `exp(-m/T)` Boltzmann-factor approximation as inadequate at the species-multiplicity layer: rel_dev exceeded the 10% RATIO band at 2 of 3 PDG anchors (T = 100 GeV: 13.54%; T = 1 GeV: 5.99% INFO; T = 1 MeV: 13.03%). The FAIL diagnosis identified the structurally correct refinement pathway: replace `boltzmann_factor()` with the canonical Kolb-Turner Eq.3.62 Fermi-Dirac and Bose-Einstein integrated forms `g_*_eff(T) = (15/π⁴) ∫ x²√(x²+(m/T)²) / (exp(√(x²+(m/T)²)) ± 1) dx`. T1.6 dispatches the refined retry. T1.6 PASS at 10% RATIO across all 3 PDG anchors unblocks (a) `g_star_BS_T_H` canonical promotion to `canonical_constants.py` with substrate-derived PROVENANCE; (b) `T_H = 1.057 MeV` canonical promotion (if not yet pinned); (c) T1.7 substantive re-dispatch of CF-39 `L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴`, with Option-A `supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` corrective canonical line emitted per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` (S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY chain at S88 verdict-file line 34, full-64-char form verified in S90 W4 dispatch trace). T1.7 is CONDITIONAL on T1.6 PASS: if T1.6 FAILs again at the canonical FD/BE integrated form, T1.7 closes as PRE-REG-INC blocked per `mechanical-closure-discipline.md` 5-clause admissibility (deferred to S92+ with further diagnosis of the canonical Kolb-Turner form's deviation from PDG/Planck g_*(T) reference values).

**Track B — LRD α-anchor PARALLEL evaluation (OAA-EXCLUDED-reviewer authoring; T1.8 + T1.9)**. The S90 W4 CF-37 verdict closed the (d)∘(b) compositional primary corridor at the PROXY-REFINEMENT-PENDING structural-ansatz layer: α'(M_LRD = 10⁷, L_max=10) = 4.80e-4 vs empirical 1/458 = 2.18e-3, rel_dev = 0.78 ≫ 0.30 RATIO band (Sub-clause B FAIL); envelope n ≈ 0 across the M-scan, R² = 0.20 (Sub-clause C FAIL). The (d)∘(b) closure routes to TWO parallel S91+ candidate pathways (per W4 carry-forward §716 + §724): T1.9 FULL CM-1995 §III.4 residue formula evaluation at the (d)∘(b) corridor (replaces the structural-ansatz layer with full physical Connes-Moscovici §III.4 evaluation; could revise χ'_weight ~4.5× larger than 0.5 and RECOVER (d)∘(b) as the LRD anchor candidate), AND T1.8 (c)∘(d) secondary corridor with modified-universal-kernel γ(s) ≠ Γ(s) (element-1 deformation replaced by a different cohomology-class shift; element-3 retains the inheritance-restricted projector P_HSS'(M)). The two pathways are PARALLEL (each evaluates a structurally distinct candidate for the LRD α-anchor); per `joint-theorem-promotion.md` Stage-2 logic, both could PASS (parallel admissibility — both corridors land in the 30% RATIO band of 1/458, in which case both are admissible LRD anchor candidates and the substrate's intrinsic determinism becomes the S92+ adjudication question), or one could PASS and the other FAIL (the PASS candidate becomes the canonical LRD anchor candidate), or both could FAIL (deferring to substrate-distance-2 §VII.AX forward gates per S91 W0 R5 landing).

**OAA exclusion (Track B; HARD)**. Per the S91 context file §"W3" line 185-186 + the S90 W-2 + W-3 workshops' Original-Authoring-Agent exclusion protocol per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` clause 2 (downstream-inheritance reach extension): `connes-ncg-theorist` and `phonon-first-cosmologist` are HARD-excluded from T1.8 and T1.9 reviewer roles. The CF-37 (d)∘(b) primary corridor and the AUX-4 (c)∘(d) secondary corridor were both AUTHORED by connes-ncg + phonon-first at the S90 W-1 workshop; their downstream-inheritance reach extends to the producing-script + cross-review layer at S91. Axis-A reviewer for T1.8 + T1.9 SHALL be selected from {volovik-superfluid-universe-theorist, van-den-dungen-bridge-theorist, gen-physicist}; Axis-B reviewer SHALL be selected from {mack-cosmic-bridge, landau-condensed-matter-theorist}. The "Connes-Moscovici 1995" textual reference in T1.9's hypothesis names a FIXED SOURCE document (the published CM-1995 paper §III.4); the EVALUATOR (the agent who computes the residue formula on the substrate spectral triple) MUST be a non-connes-ncg reviewer per OAA exclusion. The published source material is NOT subject to OAA; the cross-review machinery is.

All four gates are substantive-computation classification (compute-mode); none are mechanical-closure scripts EXCEPT T1.7 conditional-on-T1.6-FAIL branch (which routes to mechanical PRE-REG-INC closure per `mechanical-closure-discipline.md` if and only if T1.6 returns FAIL). Substrate framing: all four gates compute substrate-IS observables on `(A_K, H_K, D_K(τ_fold))` (T1.8 + T1.9: Connes-Karoubi pairing on inheritance-restricted Peter-Weyl horizon-spanning projector with element-1 deformation choice; T1.6: thermal-distribution integral on PDG reference temperatures specifying the laboratory-IN input to the substrate cascade-tail formula at S88 W6 §V.5; T1.7: substrate cascade-tail luminosity at substrate-pinned T_H = 1.057 MeV horizon). Direction substrate → bridge map → laboratory observable per `phononic-framing.md §"IS Space, Not IN Space"`; no container-thinking inversion.

---

## Wave 3 Decision Point Prerequisites

| Upstream dependency | Source | Required state |
|:--------------------|:-------|:---------------|
| `canonical_constants.py` `g_star_SM = 106.75`, `g_star_BBN = 10.75` (current SM and BBN canonical pins) | LANDED pre-S91 plan-freeze (canonical_constants.py:1577-1578) | LANDED — both pins present; T1.6 cross-checks against these as PDG anchor references at T=100 GeV (g_star_SM) and T=1 MeV (g_star_BBN) |
| `s90_w4_cf40_species_multiplicity_retry.py` producing script + `.npz` data + `.json` JSON sidecar (43.8 KB producing script with `boltzmann_factor()` helper to be replaced; .npz with 20 keys; .json with sidecar metadata) | LANDED at S90 W4 dispatch (per `session-90-w4-workingpaper.md §W4-4`) | LANDED — T1.6 forks the S90 script (preserves the 3-anchor framework; replaces `boltzmann_factor()` with Kolb-Turner Eq.3.62 integrated forms; re-emits new audit_sha256 distinct from S90's `66209e0d71b1ed19...`) |
| S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY full 64-char audit_sha256 = `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` in `computations/session-88/s88_gate_verdicts.txt` line 34 | VERIFIED in S90 W4 dispatch trace per `session-90-w4-workingpaper.md §W4-3` line 287 (disk grep confirmed) | VERIFIED — T1.7 emits Option-A corrective canonical line with `supersedes=<full-64-char>` token conditional on T1.6 PASS |
| `s84_spectrum_cache_L12_tau019.npz` (S84 master spectrum cache at L_max=12, τ_fold=0.190; 90 Peter-Weyl sectors, 155,984 eigenvalues; filtered to L_max=10 = 65 sectors / 78,080 eigenvalues for the LRD corridor evaluations) | LANDED pre-S86 (S84 master cache) | LANDED — T1.8 and T1.9 filter to L_max=10 (matching S90 CF-37 truncation) for direct comparability to the CF-37 PROXY-REFINEMENT-PENDING baseline |
| `s89_w2_a7_chi_prime_inheritance_morphism.npz` (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`; χ': A_K → M_2(C) ⊗ Cl(1) inheritance morphism with kernel rank 9 on M_3(C)) | LANDED at S89 §W2-3 (derived theorem 8-step proof; K-counter 2 → 3 advancement; per S90 W4 §W4-1 MCP audit) | LANDED — T1.9 consumes χ' inheritance morphism for the (d)∘(b) corridor's element-3 inheritance-restricted projector P_HSS'(M); T1.8 also consumes χ' for element-3 (the (c)∘(d) corridor retains element-3 (d), only element-1 changes) |
| `canonical_constants.py` `M_KK = 7.428660e+16` GeV, `M_Pl_reduced = 2.435e+18` GeV, `R_universal_HP1_strict_F4 = 1.030902`, `eps_H_HP1_norm = 16.197719`, `tau_fold = 0.190` | LANDED pre-S86 (canonical_constants.py:171, 250, 341, etc.) | LANDED — T1.8 and T1.9 use these pins as input to the residue formula evaluations; T1.8's γ(s) ≠ Γ(s) modified-universal-kernel choice is the discriminator at element-1, NOT a different canonical-constants pin |
| §VII.AF.1.OP-PROJ registry text (lines 14690-14722; cocycle source line 14704; W-5 baseline reference at S86) | LANDED at S86 W-5 | LANDED — T1.8 and T1.9 both cross-link to §VII.AF.1.OP-PROJ as the simultaneous element-1 + element-3 double-deformation pattern calibration corpus instance #1; T1.8 PASS or T1.9 PASS could land instance #2 (Hybrid Independence Test K-counter advancement deferred per S90 W4 §"Carry-forward summary") |
| `falsifier-master-inventory.md` Row #6 LRD α-anchor (T1.5 ATLAS-class observable; currently CLOSED-AT-PROXY-REFINEMENT-PENDING per S90 W4 CF-37 FAIL) | LANDED post-S90 close per S90 Constraint-Map Updates line 779 | LANDED — T1.8 PASS or T1.9 PASS would revise Row #6 from CLOSED-AT-PROXY-REFINEMENT to either ANCHOR-PROMOTED (sub-case (c)∘(d) PASS or (d)∘(b)+FULL-CM-1995 PASS) or PARALLEL-PASS (both T1.8 + T1.9 PASS); both FAIL would extend the closure to substrate-distance-2 §VII.AX forward gates queued at S91 W0 R5 landing |
| Mechanical-closure rule clauses (1)-(5) admissibility for T1.7's PRE-REG-INC FAIL branch | `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" | LANDED — T1.7's CONDITIONAL FAIL branch (only fires if T1.6 returns FAIL) satisfies clause 1 (upstream-block topology: T1.6 verdict ≠ PASS is the cause); clause 2 (verdict honesty: emit FAIL with `value='PRE-REG-INC_blocked_by_CF40_FAIL_supersedes_emission_deferred'`); clause 3 (per-gate-distinct audit_sha256); clause 4 (audit-trail signature); clause 5 (in-script working-paper update) |

**Track A → Track B parallelism**: T1.6 + T1.7 (Track A) and T1.8 + T1.9 (Track B) share NO upstream prerequisite at the substrate-physics layer. Track A operates on the thermal-distribution + cascade-tail axis (species multiplicity + luminosity); Track B operates on the spectral-pairing axis (Connes-Karoubi pairing + Peter-Weyl horizon-spanning projector). Both tracks dispatch in parallel at S91 W3 wave-open. The four-gate combinatorics (T1.6 PASS/FAIL × T1.8 PASS/FAIL × T1.9 PASS/FAIL) produce 8 possible composite outcomes (T1.7 conditional on T1.6); the W3 → W4 / W5 decision point §"Wave 3 → Wave 4 / Wave 5 Decision Point" below enumerates the consequence map.

---

## §W3-1. CF-S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED (T1.6)

### 1. Gate ID

`S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED` (synonym `CF-S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED`; origin: `sessions/archive/session-90/session-90-w4-workingpaper.md §"Carry-Forward Computations"` line 733-740 + S90 lizzi-s4-meta-p3-synthesis line 207 HIGH-EVOI-per-wave-equivalent priority; this is the S91 retry of S90 W4 CF-40 `S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED` which closed FAIL at audit_sha256 `66209e0d71b1ed19...`)

### 2. Trigger

`[VERIFY]` ∧ `[SIGN]` — `[VERIFY]` because the gate tests a quantitative claim about g_*_BS(T) accuracy at 3 PDG anchors against pre-registered 10% RATIO band; `[SIGN]` because the substitution chain pre-registers a direction (the canonical Fermi-Dirac and Bose-Einstein integrated forms are LESS aggressive than the bare exp(-m/T) approximation, so the refined g_*_BS(T) should land HIGHER than the S90 FAIL value at all 3 anchors — direction `g_*_BS_FD/BE(T) > g_*_BS_simplified(T)` at every T where ANY species has m_i/T in the bound band). Both trigger annotations are required per `gate-verdicts.md` S87+ schema-v2.

### 3. Classification

PARTICLE — species-multiplicity refinement is a particle-physics-anchor refinement; the species enumeration is the SM matter content + cascade-tail downstream species (per S88 W6 §V.5 Result 2 cascade form); the FD/BE integrated forms ARE the canonical Standard-Model thermodynamic-equilibrium kernels at temperature T per Kolb-Turner "The Early Universe" Eq. 3.62. The PASS predicate is a quantitative comparison against PDG/Planck g_*(T) reference values per laboratory-IN canonical anchors. Cross-classification with PHONONIC at the cascade-tail-INPUT layer: g_*(T) IS the laboratory-IN input to the substrate cascade-tail luminosity formula at S88 W6 §V.5 Result 2; the substrate-IS observable remains pinned at S88 W6 §V.5 (substrate cascade tail's f_M = (π²/60) · g_*(T) · A · T⁴), and this gate refines the laboratory-IN INPUT g_*(T) for downstream consumption by T1.7. The substrate-IS observable is NOT modified by this gate.

### 4. Agent type

**PRIMARY** (compute author + verdict emission): `mack-cosmic-bridge` per `feedback_mack-bridge-role.md` observational-anchor authority. Mack diagnosed the CF-40 FAIL at S90 W4 (per `session-90-w4-workingpaper.md §W4-4` and §"Closing Notes" item 4 "Mack's CF-40 FAIL diagnosis was structurally precise") and is the originating diagnostic agent for the Kolb-Turner Eq.3.62 refinement pathway. Mack runs the producing script + emits the verdict line.

**CO-AUTHOR** (numerical-integration cross-check): `gen-physicist` for cross-check on the `scipy.integrate.quad` numerical-integration tolerances + convergence diagnostics across the 3 PDG anchor temperatures. Gen-physicist authors the cross-check sub-section in the working paper; does NOT emit the verdict line.

**EXCLUDED**: None at this gate level (no OAA constraint applies — CF-40 was authored by mack at S90 W4, NOT by any of the LRD α-anchor reviewers).

NOT `gen-physicist` as primary — per spawn prompt constraint "DO NOT use `gen-physicist` as test-case agent type"; gen-physicist's role is restricted to the numerical-integration cross-check sub-section, NOT compute author.

### 5. Hypothesis

The canonical Fermi-Dirac and Bose-Einstein integrated forms of the species-suppression kernel per Kolb-Turner "The Early Universe" Eq. 3.62 — `g_*_eff(T) = (15/π⁴) ∫₀^∞ x²√(x²+(m/T)²) / (exp(√(x²+(m/T)²)) ± 1) dx` (the `+` sign for fermions, the `−` sign for bosons; the integral converges absolutely for all m/T ∈ [0, ∞)) — reproduces the PDG/Planck g_*(T) reference values at all 3 cross-check anchors T ∈ {100 GeV, 1 GeV, 1 MeV} within a 10% RATIO PASS band. PASS unblocks (a) `g_star_BS_T_H = g_*_FD/BE(T_H = 1.057 MeV)` canonical promotion to `canonical_constants.py` with substrate-derived PROVENANCE citing this gate's audit_sha256; (b) T_H = 1.057 MeV canonical promotion if not yet pinned; (c) T1.7 substantive re-dispatch of CF-39 L_H_canonical re-pinning with Option-A supersedes-tag emission. FAIL at any one of the 3 anchors > 10% RATIO indicates the canonical Kolb-Turner form ITSELF deviates from PDG/Planck g_*(T) — a structurally surprising outcome that would require deeper inspection of the cascade-tail downstream species enumeration (e.g., are the QCD-crossover degrees of freedom near T = 200 MeV properly accounted for at the T = 1 GeV anchor?).

### 6. Method — COMPLETE dispatch prompt for mack-cosmic-bridge

> **Dispatch prompt (verbatim)**:
>
> You are mack-cosmic-bridge dispatched as PRIMARY computation agent for `S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED` (T1.6 of S91 W3). Co-author cross-check role: gen-physicist (numerical-integration tolerance cross-check; receives your producing-script .npz output and runs scipy.integrate.quad convergence diagnostics in a separate sub-section).
>
> **Substrate framing reminder**: per `phononic-framing.md §"IS Space, Not IN Space"`, the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the cascade-tail observable f_M = (π²/60) · g_*(T) · A · T⁴ at S88 W6 §V.5 Result 2 IS the substrate cascade-tail luminosity formula. g_*(T) is the laboratory-IN input from the Standard-Model thermodynamic-equilibrium ledger at temperature T — NOT a substrate-IS observable; it is the laboratory's image of the SM matter content at that temperature. Your refinement here is on the laboratory-IN INPUT; the substrate-IS observable f_M's structural form does NOT change. Direction of explanation flows substrate cascade tail (S88 W6 §V.5) ← g_*(T) (laboratory-IN, refined here) → CF-39 bridge map L_H_canonical at substrate-pinned T_H = 1.057 MeV horizon. Do NOT frame the species-multiplicity refinement as "improving the substrate's predictions"; the substrate's prediction is the cascade-tail's structural form, and this gate refines the laboratory-IN INPUT to that form.
>
> **Producing script construction**:
>
> 1. Fork `computations/session-90/s90_w4_cf40_species_multiplicity_retry.py` (43.8 KB; 20 npz keys) to a new script `computations/session-91/s91_w3_cf40_kolb_turner_fd_be_integrated.py`. Preserve the 3-anchor framework (T ∈ {100 GeV, 1 GeV, 1 MeV}), the SM species enumeration, the lattice-QCD pin (Borsanyi 2016 / PDG canonical), and the PDG reference values for g_*_PDG_100GeV, g_*_PDG_1GeV, g_*_PDG_1MeV.
> 2. Replace the `boltzmann_factor()` helper function (which used `exp(-m/T)` for species in band m/T ∈ [0.2, 5], 1 otherwise) with two new helpers:
>    - `kolb_turner_eq_3_62_fermion(m_over_T)`: returns the integrated Fermi-Dirac contribution per fermionic species at m/T = m_over_T, computed via `(15.0 / math.pi**4) * scipy.integrate.quad(lambda x: x**2 * math.sqrt(x**2 + m_over_T**2) / (math.exp(math.sqrt(x**2 + m_over_T**2)) + 1.0), 0, np.inf, limit=200, epsabs=1e-10, epsrel=1e-8)[0]`
>    - `kolb_turner_eq_3_62_boson(m_over_T)`: same form with `(exp(...) - 1.0)` denominator
>    - Per-species multiplicity weighting: g_*_eff_species_i = g_i · k_KT(m_i/T) where k_KT is the appropriate fermion / boson kernel
> 3. Re-test at the 3 PDG anchors: T = 100 GeV, T = 1 GeV, T = 1 MeV. Compute g_*_BS_FD_BE_100GeV, g_*_BS_FD_BE_1GeV, g_*_BS_FD_BE_1MeV by summing over SM species (preserve the SM enumeration from the S90 script; include lattice-QCD-crossover degrees of freedom near Λ_QCD ≈ 200 MeV per the S90 script's existing handling at T = 1 GeV).
> 4. Compute rel_dev_i = |g_*_BS_FD_BE_i − g_*_PDG_i| / g_*_PDG_i for i ∈ {100 GeV, 1 GeV, 1 MeV}. The PASS band is rel_dev_i ≤ 0.10 RATIO at ALL 3 anchors (per `gate-verdicts.md` magnitude_verdict layer); the INFO band is 0.05 < rel_dev_i ≤ 0.10 at any anchor; the FAIL band is rel_dev_i > 0.10 at any anchor.
> 5. Also compute g_*_BS_FD_BE_T_H at T_H = 1.057 MeV (CF-39 anchor temperature; per S88 W6 §V.1). This is the value that will be promoted to `canonical_constants.py` as `g_star_BS_T_H_FW` on PASS.
> 6. The lizzi-s4-meta-p3-synthesis §1.3 line 122 predicted: "Refined CF-40 → rel_dev_100GeV ≈ 0.7%; PASS. Symmetrically at T=1 MeV: refined rel_dev ≈ 2% (e± threshold at FD form is well-modeled); PASS. At T=1 GeV the refined form lands within QCD-crossover model uncertainty (Borsanyi ±5%); already INFO at 6%, will land in 5–10% band → still INFO or PASS." Honest pre-registration: lizzi's prediction is that the canonical Kolb-Turner integrated form lands all 3 anchors within 10% RATIO; gate emits PASS if so, INFO if 1 GeV lands in (0.05, 0.10], FAIL if any anchor > 0.10. Lizzi's prediction is the structural prior; the gate's verdict is the empirical test.
> 7. Output npz keys (mandatory; preserve 20-key superset from S90 + 4 new keys for FD/BE comparison):
>    - g_star_BS_FD_BE_T_H (NEW; canonical-promotion candidate on PASS)
>    - g_star_BS_FD_BE_100GeV, g_star_BS_FD_BE_1GeV, g_star_BS_FD_BE_1MeV (NEW; integrated-form values)
>    - g_star_BS_simplified_100GeV, g_star_BS_simplified_1GeV, g_star_BS_simplified_1MeV (S90 baseline values for cross-comparison; cite from S90 W4 CF-40 npz)
>    - g_star_PDG_100GeV, g_star_PDG_1GeV, g_star_PDG_1MeV (preserved PDG references)
>    - rel_dev_FD_BE_anchors (NEW; 3-element array)
>    - rel_dev_simplified_anchors (preserved; 3-element array)
>    - kolb_turner_kernel_evaluations (NEW; dict per species per anchor; object array)
>    - T_H_value_MeV = 1.057 (preserved; CF-39 anchor)
>    - cascade_form_pin = "S88 W6 §V.5" (preserved)
>    - lattice_QCD_pin = "Borsanyi et al. 2016 / PDG canonical" (preserved)
>    - audit_sha256, content_sha256, schema_version (canonical companions)
> 8. Plot construction: 3-panel comparison (one per PDG anchor); for each, plot g_*_BS_simplified (S90 value) + g_*_BS_FD_BE (this gate's refined value) + g_*_PDG reference (horizontal line) + 10% RATIO PASS band (shaded); legend identifying each. PNG output at `computations/session-91/s91_w3_cf40_kolb_turner_fd_be_integrated.png`.
> 9. JSON sidecar at `computations/session-91/s91_w3_cf40_kolb_turner_fd_be_integrated.json` carrying the 3 rel_dev values + PASS/INFO/FAIL annotation per anchor + composite verdict.
>
> **Verdict line append**: `computations/session-91/s91_gate_verdicts.txt` per `gate-verdicts.md §"Canonical Verdict-File Path"` (variant `_shared/s91_gate_verdicts.txt` is FORBIDDEN). Use the single-shot AFTER-pattern emission per `registry-landing.md §"Bridge-Landing Script Architecture"`: build verdict text in memory → write_atomic_with_fsync → re-read → verify section matches → emit exactly one canonical line + one dual-SHA companion row + (since `[SIGN]` trigger) one 3-tuple annotation row. NO conditional rewrite-on-FAIL-and-re-emit-PASS BEFORE-pattern (would emit dual-trio defect per S87 W5 calibration corpus).
>
> **Verdict line format** (S87+ schema-v2):
>
> ```
> S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED: PASS|INFO|FAIL -- value='g_star_BS_FD_BE_T_H=<v_T_H>;g_star_BS_FD_BE_100GeV=<v_100>;rel_dev_100GeV=<r_100>;...;composite=<c>' scheme=kolb-turner-eq-3-62-FD-BE-integrated convention=mack-cosmic-bridge-primary-substrate-cascade-tail-INPUT-refinement L_max=N/A audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
> ```
>
> Companion dual-SHA row:
>
> ```
> # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED dual-SHA companion row (W9a-99 split)
> ```
>
> 3-tuple annotation row (since `[SIGN]` trigger):
>
> ```
> # sign_verdict=PASS|FAIL magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED 3-tuple annotation (S87 schema-v2)
> ```
>
> **On PASS**: promote `g_star_BS_T_H_FW = <computed value>` to `canonical_constants.py` with PROVENANCE entry citing this gate's audit_sha256; promote `T_H_FW = 1.057e-3` GeV (= 1.057 MeV) if not yet pinned. Per `math-scripts.md §"Canonical Write-Order for New Framework Predictions"` Step 1 (verdict-file emission) → Step 2 (canonical_constants.py promotion) → Step 3 (falsifier-master-inventory.md row landing by mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`).
>
> **On FAIL**: write to working paper §"Solution-space implications" the constraint-map advance: canonical Kolb-Turner integrated form ITSELF deviates from PDG/Planck g_*(T) at the failing anchor; identify which species's kernel contribution dominates the deviation; route to S92+ as a separate substrate-cascade-form scrutiny carry-forward. T1.7 mechanical PRE-REG-INC closure fires (per `mechanical-closure-discipline.md`).
>
> **Working paper section** at `sessions/archive/session-91/session-91-w3-workingpaper.md §W3-1`: ≥ 15 substantive lines (NOT a stub heading) per `agent-standards.md §"Completion Verification"`. Sections: Status (top), Gate ID, Trigger, Classification, Agent, Hypothesis, Plan reference, MCP Pre-Compute Audit (3+ knowledge-MCP queries documented), Verdict line + dual-SHA + 3-tuple, Results (key returns 4-tuple, integration tolerances, per-anchor table, per-species kernel evaluation table, plot description), Cross-checks performed (CC1 through CC5+), Data files produced, Solution-space implication, Substrate framing reminder.

### 7. Machinery pin (PRDR)

| PRDR Element | Pin | Source |
|:-------------|:----|:-------|
| **Integration library** | `scipy.integrate.quad` with limit=200, epsabs=1e-10, epsrel=1e-8 | Standard scipy adaptive Gauss-Kronrod quadrature; tolerances chosen so that ‖kernel_FD(m/T) − kernel_FD_truncated(m/T)‖ ≤ 1e-7 at m/T ≤ 10 |
| **Integration domain** | [0, ∞) with scipy's automatic substitution `x = (1-t)/t` mapping for the upper-bound divergence | scipy.integrate.quad default with `np.inf` upper limit |
| **PDG anchor reference values** | g_*_PDG_100GeV = 106.75 (= `g_star_SM` canonical_constants.py:1577), g_*_PDG_1GeV ≈ 61.75 ± 5 (QCD-crossover model uncertainty per Borsanyi 2016 ±5%), g_*_PDG_1MeV = 10.75 (= `g_star_BBN` canonical_constants.py:1578) | canonical_constants.py + Kolb-Turner Table 3.1 / Borsanyi 2016 |
| **PASS / INFO / FAIL band thresholds** | PASS: rel_dev_i ≤ 0.10 at ALL 3 anchors; INFO: 0.05 < rel_dev_i ≤ 0.10 at any one anchor; FAIL: rel_dev_i > 0.10 at any anchor | S90 W4 CF-40 plan §W4-4 §9 (preserved from S90 retry plan to preserve direct comparability of band) |
| **Sub-band tolerance for T = 1 GeV** | Extended INFO band to (0.05, 0.10] per lizzi-s4-meta-p3-synthesis §1.3 line 122 prediction of QCD-crossover model uncertainty Borsanyi ±5% | Lizzi prediction (NOT a substrate-physics claim; calibration prior for the gate's INFO band routing) |
| **SM species enumeration at each anchor** | Per S90 W4 CF-40 producing script's SM enumeration (preserved): quarks (u/d/s/c/b/t), leptons (e/μ/τ/ν×3), gauge bosons (γ/W±/Z/g×8), Higgs; lattice-QCD-crossover handling at T = 1 GeV per Borsanyi 2016 / PDG canonical | S90 W4 CF-40 producing script (preserved) + Kolb-Turner Table 3.1 |
| **T_H anchor** | T_H = 1.057 MeV (substrate-pinned per S88 W6 §V.1; promotion candidate as `T_H_FW` on PASS if not yet pinned) | S88 W6 §V.1 |
| **GPU usage** | None — scalar integral evaluations only; CPU-only is appropriate per `computation-environment.md §"CPU Thread Cap When GPU Not Used"` | thread cap OMP_NUM_THREADS=8 set BEFORE numpy import; no torch use |
| **Writer assignment** | mack-cosmic-bridge primary (compute + verdict emission); gen-physicist co-author (cross-check sub-section only) | `feedback_mack-bridge-role.md` |
| **Verdict file** | `computations/session-91/s91_gate_verdicts.txt` | `gate-verdicts.md §"Canonical Verdict-File Path"` |
| **PDG anchor source pin** | `canonical_constants.py:1577-1578` for g_star_SM, g_star_BBN | Static file SHA captured at runtime |

### 8. Expected output 4-tuple

`(value='g_star_BS_FD_BE_T_H=<v_T_H>;g_star_BS_FD_BE_100GeV=<v_100>;rel_dev_100GeV=<r_100>;g_star_BS_FD_BE_1GeV=<v_1G>;rel_dev_1GeV=<r_1G>;g_star_BS_FD_BE_1MeV=<v_1M>;rel_dev_1MeV=<r_1M>;composite=<PASS|INFO|FAIL>', scheme='kolb-turner-eq-3-62-FD-BE-integrated', convention='mack-cosmic-bridge-primary-substrate-cascade-tail-INPUT-refinement', L_max='N/A')`

L_max = N/A because the gate evaluates a thermal-distribution integral on the SM species enumeration; the substrate spectral triple's L_max truncation is irrelevant to g_*(T) (the substrate cascade-tail formula's structural form at S88 W6 §V.5 is L_max-independent at the laboratory-IN INPUT layer).

### 9. PASS / FAIL / INFO thresholds

- **PASS**: rel_dev_i ≤ 0.10 RATIO at ALL 3 PDG anchors T ∈ {100 GeV, 1 GeV, 1 MeV}. magnitude_verdict = PASS. sign_verdict = PASS (FD/BE integrated form gives g_*_BS larger than simplified at every anchor where ANY species has m_i/T in band — direction confirmed; see §10 substitution chain Step 5). regime_verdict = VALID (scipy.integrate.quad converges within pre-pinned tolerances at all 3 anchors). Composite collapse: PASS. Unblocks (a) `g_star_BS_T_H_FW` canonical promotion; (b) `T_H_FW = 1.057e-3` GeV canonical promotion; (c) T1.7 substantive re-dispatch.

- **INFO**: 0.05 < rel_dev_i ≤ 0.10 at exactly ONE anchor (typically T = 1 GeV per lizzi-s4-meta-p3-synthesis §1.3 line 122 prediction of QCD-crossover model uncertainty); other 2 anchors PASS. magnitude_verdict = INFO. sign_verdict = PASS (direction still confirmed). regime_verdict = VALID. Composite collapse: INFO. INFO band routes to T1.7 substantive re-dispatch with documented INFO caveat in canonical_constants.py PROVENANCE (g_star_BS_T_H_FW promoted with INFO-band sub-tag); the (T = 1 GeV) anchor's INFO routing is the QCD-crossover model-uncertainty pre-disclosure, NOT a substrate-physics failure.

- **FAIL**: rel_dev_i > 0.10 at any anchor. magnitude_verdict = FAIL. sign_verdict = PASS or FAIL depending on which direction the deviation lies (the substitution chain predicts the refined integrated form lands HIGHER than the simplified; if rel_dev exceeds 10% in either direction, sign-direction adjudication identifies WHICH species dominates the deviation). regime_verdict = VALID. Composite collapse: FAIL. FAIL routes to (i) T1.7 mechanical PRE-REG-INC closure per `mechanical-closure-discipline.md`; (ii) carry-forward to S92+ a separate substrate-cascade-form scrutiny gate (deeper inspection of which Kolb-Turner kernel term deviates from PDG, e.g., the lattice-QCD-crossover at T = 200 MeV); (iii) no canonical promotion of `g_star_BS_T_H_FW`.

### 10. Substitution chain (substrate-cascade-tail-INPUT direction; per `math-scripts.md §"Double-Check Logic Before Compute"`)

```
Step 1 (definition): The simplified Boltzmann-factor approximation g_*_simplified(T) = Σ_i g_i · k_simplified(m_i/T) where k_simplified(x) = exp(-x) for x ∈ [0.2, 5] and 1 elsewhere [S90 W4 CF-40 producing script's boltzmann_factor() helper]

Step 2 (definition): The Kolb-Turner Eq. 3.62 integrated form g_*_FD/BE(T) = Σ_i g_i · k_KT_i(m_i/T) where
    k_KT_fermion(x) = (15/π⁴) ∫₀^∞ u² √(u²+x²) / (exp(√(u²+x²)) + 1) du
    k_KT_boson(x) = (15/π⁴) ∫₀^∞ u² √(u²+x²) / (exp(√(u²+x²)) − 1) du
[Kolb-Turner "The Early Universe" Eq. 3.62]

Step 3 (substitution at m/T = 0): k_KT_fermion(0) = (15/π⁴) · (7/8) · π⁴/15 = 7/8 [standard Fermi-Dirac integral at m=0; relativistic limit];
                                    k_KT_boson(0) = (15/π⁴) · π⁴/15 = 1 [standard Bose-Einstein integral at m=0; relativistic limit];
                                    k_simplified(0) = 1 (since m/T = 0 < 0.2).
    Direction at m/T = 0: k_KT_fermion(0) = 7/8 < k_simplified_fermion(0) = 1; fermionic species are UNDERESTIMATED by simplified at m/T = 0.

Step 4 (substitution at m/T ≈ 1, threshold band): For m_W/T ≈ 0.8 at T = 100 GeV:
    k_simplified(0.8) = exp(-0.8) ≈ 0.449 [bare exp(-m/T)]
    k_KT_boson(0.8) ≈ 0.92 (per lizzi-s4-meta-p3-synthesis §1.3 line 116) [integrated FD/BE form]
    Direction at threshold: k_KT > k_simplified by factor ~2.0; simplified is too aggressive (suppresses too hard).

Step 5 (substitution at m/T ≈ 5, deep-Boltzmann tail): For m_top/T ≈ 1.73 at T = 100 GeV (top quark mass m_t ≈ 173 GeV):
    k_simplified(1.73) = exp(-1.73) ≈ 0.177
    k_KT_fermion(1.73) ≈ 0.13–0.16 (integrated form starts to match simplified in deep Boltzmann tail; small residual deviation from non-relativistic correction)
    Direction at deep tail: k_KT < k_simplified at m/T ≥ 2 (asymptotic agreement; refinement becomes less impactful).

Step 6 (composite over SM species at T = 100 GeV): Most SM species at T = 100 GeV have m_i/T ≪ 1 (light fermions: m_i/T ~ 1e-4 for electrons; same-order suppression dominates for the W/Z/H species which have m_i/T ∈ [0.8, 1.25]). The dominant contribution to the rel_dev is from threshold-band species (W, Z, H, top), all in the regime where Step 4 dominates (k_KT > k_simplified). Predicted direction: g_*_FD/BE(100 GeV) > g_*_simplified(100 GeV); per lizzi-s4-meta-p3-synthesis §1.3 line 118 quantitative prediction: g_*_FD/BE(100 GeV) ≈ 106 vs g_*_simplified(100 GeV) ≈ 92.3.

Step 7 (direction read-off): If lizzi prediction holds, g_*_FD/BE(100 GeV) ≈ 106 vs g_*_PDG_100GeV = 106.75 → rel_dev ≈ 0.7% → PASS (well inside 10% RATIO band). The refined integrated form sign_verdict = PASS: g_*_FD/BE(T) > g_*_simplified(T) at all 3 anchors where threshold-band species contribute.
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** (composite): the canonical Kolb-Turner Eq. 3.62 integrated form reproduces PDG/Planck g_*(T) within 10% RATIO at all 3 anchors. Constraint-map advance:
  - The simplified `exp(-m/T)` Boltzmann-factor approximation is closed as too aggressive at the species-multiplicity layer (S90 W4 CF-40 FAIL diagnosis confirmed as the structurally correct closure direction).
  - The canonical FD/BE integrated form is opened as the canonical species-multiplicity-kernel at all temperatures; `g_star_BS_T_H_FW` is promoted to `canonical_constants.py` for downstream consumption by T1.7 and any future CF-39-class cascade-tail substantive computation.
  - T1.7 is unblocked for substantive re-dispatch.
  - The CF-40 RD-class observation from lizzi-s4-meta-p3-synthesis §1.3 line 96 (the `g_*(T)` observable is RD-class because the Boltzmann-kernel choice IS the regulator-class axis at species-multiplicity) is sharpened: the canonical FD/BE integrated form IS the canonical-regulator-class representative; the simplified `exp(-m/T)` lands OUTSIDE the canonical regulator-class equivalence class.

- **INFO** (composite; INFO at exactly T = 1 GeV per QCD-crossover model uncertainty): canonical FD/BE integrated form is accurate at T = 100 GeV and T = 1 MeV (the regimes where SM species are clearly separated from QCD-crossover physics) but lands in the INFO band at T = 1 GeV (lattice-QCD-crossover-influenced regime). Constraint-map advance:
  - The canonical FD/BE form is accepted with documented INFO caveat at T = 1 GeV; downstream consumers (T1.7) inherit the INFO-band sub-tag on `g_star_BS_T_H_FW` promotion.
  - The QCD-crossover model-uncertainty pre-disclosure (Borsanyi 2016 ±5%) is the structural origin of the INFO routing; this is NOT a substrate-physics failure but a known laboratory-IN systematic.

- **FAIL** (composite): the canonical FD/BE integrated form ITSELF deviates from PDG/Planck g_*(T) at one or more anchors > 10% RATIO. Constraint-map advance:
  - Structurally surprising outcome (would invalidate the lizzi-s4-meta-p3-synthesis §1.3 line 122 prediction); identifies a deeper substrate-cascade-form scrutiny carry-forward to S92+ (which Kolb-Turner kernel term + which SM species contribution dominates the deviation).
  - T1.7 mechanical PRE-REG-INC closes per `mechanical-closure-discipline.md`; Option-A supersedes-tag emission to S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY chain remains DEFERRED at S88 absolute verdict permanence.
  - No canonical promotion of `g_star_BS_T_H_FW`.
  - The species-multiplicity refinement axis is closed at the canonical FD/BE form layer; further pursuit requires deeper SM-thermodynamic-ledger investigation (e.g., lattice-QCD higher-order corrections, electroweak-crossover degrees of freedom, additional fermionic contributions from νs at sub-MeV temperatures).

### 12. Effort estimate

~1.0 wave-equivalent (mack-cosmic-bridge primary author). Breakdown: ~30 min fork producing script + replace `boltzmann_factor()` helper; ~20 min scipy.integrate.quad integration runs at 3 anchors + T_H anchor; ~20 min cross-checks (gen-physicist co-author sub-section); ~10 min plot + JSON sidecar + verdict-line emission + working-paper section authoring. Total estimated wall time ~1.5 hours.

### 13. Substrate-framing reminder

In the dispatch prompt §6 above, the explicit reminder reads: "the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the cascade-tail observable f_M = (π²/60) · g_*(T) · A · T⁴ at S88 W6 §V.5 Result 2 IS the substrate cascade-tail luminosity formula. g_*(T) is the laboratory-IN input from the Standard-Model thermodynamic-equilibrium ledger at temperature T — NOT a substrate-IS observable; it is the laboratory's image of the SM matter content at that temperature. Your refinement here is on the laboratory-IN INPUT; the substrate-IS observable f_M's structural form does NOT change. Direction of explanation flows substrate cascade tail (S88 W6 §V.5) ← g_*(T) (laboratory-IN, refined here) → CF-39 bridge map L_H_canonical at substrate-pinned T_H = 1.057 MeV horizon." This satisfies `phononic-framing.md §"IS Space, Not IN Space"` directional pre-registration: the substrate's cascade-tail luminosity formula IS structural; the species-multiplicity kernel choice IS the laboratory's input-ledger choice; direction flows substrate → bridge map → laboratory observable, NOT inverse.

---

## §W3-2. CF-S91-CF39-RE-DISPATCH-POST-CF40-PASS (T1.7; CONDITIONAL on T1.6 PASS)

### 1. Gate ID

`S91-CF39-RE-DISPATCH-POST-CF40-PASS` (synonym `CF-S91-CF39-RE-DISPATCH-POST-CF40-PASS`; origin: `sessions/archive/session-90/session-90-w4-workingpaper.md §"Carry-Forward Computations"` line 742-749 + S90 W4 CF-39 mechanical closure at audit_sha256 `017258e3c8613ec8...` documenting the deferred substantive computation pending CF-40 PASS; this is the S91 retry of S90 W4 CF-39 `S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY`)

### 2. Trigger

`[VERIFY]` ∧ `[CHAIN]` — `[VERIFY]` because the gate tests a quantitative claim about L_H_canonical re-pinning at substrate-pinned T_H = 1.057 MeV against the S88 §W1c-69 reference baseline at 0.5 log-OOM ABSOLUTE band AND ≥ 1.0 log-OOM improvement of log_residual relative to S88; `[CHAIN]` because the gate emits a corrective canonical line per Option-A supersedes-tag protocol naming the S88 prior canonical line at full 64-char audit_sha256. Both trigger annotations are required.

### 3. Classification

PHONONIC — the substrate cascade-tail luminosity L_H_canonical IS the substrate-IS observable per S88 W6 §V.5 Result 2 (the cascade tail formula's structural form). The gate refines the laboratory-IN INPUT g_*(T_H) per T1.6 PASS and re-pins the substrate cascade tail's empirical anchor relative to S88 §W1c-69 reference. The substrate cascade tail IS the substrate observable; the L_H_canonical numerical value is its image under the inheritance morphism from substrate cascade form to laboratory-IN cosmological-horizon observable.

### 4. Agent type

**PRIMARY**: `mack-cosmic-bridge` per `feedback_mack-bridge-role.md`. Mack is the originating sole-writer for the L_H_canonical re-pinning per CF-39 origin; same author as T1.6 ensures coherent T1.6 → T1.7 cascade.

**EXCLUDED**: None at this gate level (CF-39 was authored by mack at S90 W4 mechanical closure, NOT by any of the LRD α-anchor reviewers; no OAA constraint).

NOT `gen-physicist` as primary per spawn-prompt constraint.

### 5. Hypothesis

CONDITIONAL on T1.6 PASS (g_star_BS_T_H_FW canonical promotion with substrate-derived PROVENANCE): the substrate cascade-tail luminosity L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴ at substrate-pinned T_H = 1.057 MeV with refined g_*(T_H) from T1.6 lands within 0.5 log-OOM ABSOLUTE of the S88 §W1c-69 reference baseline f(M_at_W1c69) AND `log_residual_improvement = log10(|residual_S88| / |residual_T1.7|) ≥ 1.0` log-OOM (the refined CF-40 g_*(T_H) reduces the 13-OOM residual of S88 §W1c-69 baseline by at least one order of magnitude). PASS emits the Option-A corrective canonical line with `supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` (full 64-char of S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY at S88 verdict-file line 34) per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`; downstream consumers shift to the latest non-superseded canonical line per supersession-chain reading discipline.

### 6. Method — COMPLETE dispatch prompt for mack-cosmic-bridge

> **Dispatch prompt (verbatim)**:
>
> You are mack-cosmic-bridge dispatched as PRIMARY computation agent for `S91-CF39-RE-DISPATCH-POST-CF40-PASS` (T1.7 of S91 W3). This gate is CONDITIONAL on T1.6 PASS: dispatch this gate ONLY AFTER T1.6 has returned a PASS verdict (or INFO at T = 1 GeV anchor with structural-tag acceptance). If T1.6 returns FAIL at any of the 3 PDG anchors, this gate mechanical-closes as PRE-REG-INC FAIL per `mechanical-closure-discipline.md` (the upstream-block topology fires: T1.6 verdict ≠ PASS is the cause; do NOT dispatch substantive computation).
>
> **Substrate framing reminder**: per `phononic-framing.md §"IS Space, Not IN Space"`, the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the substrate's cascade-tail luminosity at T_H = 1.057 MeV horizon IS the substrate-IS observable L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴ per S88 W6 §V.5 Result 2. Direction of explanation: substrate cascade form (S88 W6 §V.5 structural identity) → bridge map (this gate's L_H_canonical evaluation at substrate-pinned T_H) → laboratory-IN cosmological-horizon observable (S88 §W1c-69 reference baseline f(M_at_W1c69)). The Option-A supersedes-tag emission preserves S88 absolute verdict permanence (the S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY PASS line is RETAINED on disk at line 34 of `s88_gate_verdicts.txt`; this gate APPENDS a corrective canonical line; downstream consumers follow the supersession chain).
>
> **Producing script construction** (if T1.6 PASS):
>
> 1. New script at `computations/session-91/s91_w3_cf39_l_h_canonical_re_pinning.py`.
> 2. Read T1.6 npz `computations/session-91/s91_w3_cf40_kolb_turner_fd_be_integrated.npz`; verify T1.6 PASS via composite verdict check; extract `g_star_BS_FD_BE_T_H` value.
> 3. Verify g_star_BS_T_H_FW canonical promotion has landed in `canonical_constants.py` (per `math-scripts.md §"Canonical Write-Order"` Step 2); if not yet landed at compute-time, route to mechanical PRE-REG-INC FAIL closure per `mechanical-closure-discipline.md`.
> 4. Compute L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴ where:
>    - g_*(T_H) = g_star_BS_T_H_FW (canonical pin from T1.6 PASS)
>    - T_H = 1.057 MeV = 1.057e-3 GeV (substrate-pinned per S88 W6 §V.1; if `T_H_FW` canonical pin landed at T1.6 PASS, use canonical pin; otherwise use literal value with `# (local)` tag per `math-scripts.md §"Local Variable Tagging"`)
>    - A_horizon = substrate-IS horizon area (per S88 W6 §V.5; promote to canonical_constants.py if not already pinned)
>    - T_H⁴ in natural units (GeV⁴) for direct comparison with f(M_at_W1c69) reference baseline in matching units
> 5. Read S88 §W1c-69 reference baseline f(M_at_W1c69) value from S88 workshop or npz source (per S90 W4 CF-39 mechanical closure documentation referencing S88 §W1c-69 source).
> 6. Compute `residual = L_H_canonical_T1.7 − f(M_at_W1c69)` (in log10 units: `log_residual = log10(L_H_canonical) − log10(f_W1c69)`); compute `delta_log = |log_residual|` and `log_residual_improvement = log10(|residual_S88|) − log10(|residual_T1.7|)` (how many OOM the refinement reduces the residual).
> 7. PASS bands: `delta_log < 0.5` ABSOLUTE log-OOM AND `log_residual_improvement ≥ 1.0` log-OOM. INFO bands: `0.5 ≤ delta_log < 1.0` OR `0.5 ≤ log_residual_improvement < 1.0`. FAIL: `delta_log ≥ 1.0` OR `log_residual_improvement < 0.5`.
> 8. Output npz keys (mandatory):
>    - L_H_canonical_T1.7 (computed)
>    - g_star_BS_T_H_used (from canonical pin)
>    - A_horizon_value, T_H_value (canonical pins)
>    - f_W1c69_reference (from S88 source)
>    - residual_value, log_residual, delta_log
>    - residual_S88_value, log_residual_improvement
>    - supersedes_target_audit_sha256 = `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` (full 64-char)
>    - audit_sha256, content_sha256, schema_version
> 9. **On PASS**: emit Option-A corrective canonical line with `supersedes=<full-64-char>` token; per `gate-verdicts.md §"Option A — sig_5 remediation pathway"` Step 2, the corrective canonical line carries the `supersedes` tag in its `value=` field (or the dual-SHA companion comment row); downstream consumers cite the LATEST NON-SUPERSEDED line as canonical (per Option A Step 3).
> 10. **On FAIL or INFO**: emit corrective canonical line WITHOUT supersedes tag (the S88 PASS line remains canonical at S88 reading; the T1.7 FAIL/INFO documents the structural-refinement-attempt verdict but does NOT supersede S88).
>
> **Verdict line append**: `computations/session-91/s91_gate_verdicts.txt` per `gate-verdicts.md §"Canonical Verdict-File Path"`.
>
> **Verdict line format** (S87+ schema-v2; PASS branch with supersedes-tag):
>
> ```
> S91-CF39-RE-DISPATCH-POST-CF40-PASS: PASS -- value='L_H_canonical=<v>;delta_log=<dl>;log_residual_improvement=<lri>;supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d' scheme=substrate-cascade-tail-S88-W6-V5-resultII convention=mack-cosmic-bridge-primary-Option-A-supersedes-emission-corrective L_max=N/A audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
> ```
>
> Companion dual-SHA row + (NOT `[SIGN]`-only trigger; `[VERIFY]` ∧ `[CHAIN]` does NOT require 3-tuple annotation per `gate-verdicts.md` schema-v2 trigger-condition reading; however, since downstream consumers benefit from regime_verdict reading on a `[CHAIN]` gate, include the 3-tuple annotation as advisory):
>
> ```
> # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # S91-CF39-RE-DISPATCH-POST-CF40-PASS dual-SHA companion row (W9a-99 split)
> ```
>
> **FAIL branch (T1.6 returned FAIL)**: mechanical PRE-REG-INC closure per `mechanical-closure-discipline.md` 5-clause admissibility. Producing script at `computations/session-91/s91_w3_cf39_mechanical_closure_blocked_by_cf40.py` (forked from S90 W4 CF-39 mechanical-closure script):
>
> ```
> S91-CF39-RE-DISPATCH-POST-CF40-PASS: FAIL -- value='PRE-REG-INC_blocked_by_S91_CF40_FAIL_supersedes_emission_deferred' scheme=substrate-cascade-tail-S88-W6-V5-resultII convention=mack-cosmic-bridge-primary-mechanical-closure-PRE-REG-INC L_max=N/A audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
> ```
>
> Mechanical-closure rule audit (per `mechanical-closure-discipline.md`): (1) upstream-block topology: T1.6 verdict ≠ PASS in `s91_gate_verdicts.txt` is the cause; (2) verdict honesty: FAIL with `value='PRE-REG-INC_blocked_by_S91_CF40_FAIL_*'` pattern; (3) per-gate-distinct audit_sha256 embedding `_gate_id=S91-CF39-RE-DISPATCH-POST-CF40-PASS` + `_wp_id=W3-2` + `_scheme=...` + `_convention=...`; (4) audit-trail signature: future grep on `s91_gate_verdicts.txt` for `PRE-REG-INC_blocked_by_S91_CF40_FAIL` returns this gate's canonical line + upstream-block T1.6 FAIL line co-citation; (5) in-script working-paper update: §W3-2 §"Status" and §"Verdict" and §"Results" and §"Substrate framing" blocks all populated in the SAME run as the verdict-line append.
>
> **Working paper section** at `sessions/archive/session-91/session-91-w3-workingpaper.md §W3-2`: ≥ 15 substantive lines. Sections: Status (top — either PASS substantive or FAIL mechanical-closure), Gate ID, Trigger, Classification, Agent, Hypothesis, Plan reference, MCP Pre-Compute Audit (verify g_star_BS_T_H_FW canonical pin via get_constant call), Verdict line + dual-SHA, Results (PASS branch: L_H_canonical value + delta_log + log_residual_improvement + supersedes-tag emission diagnostics; FAIL mechanical branch: PRE-REG-INC closure documentation per `mechanical-closure-discipline.md`), Cross-checks performed, Data files produced, Solution-space implication (PASS: S88 supersession; FAIL: S88 reading stands), Substrate framing reminder.

### 7. Machinery pin (PRDR)

| PRDR Element | Pin | Source |
|:-------------|:----|:-------|
| **T1.6 PASS prerequisite check** | Read T1.6 npz; verify composite verdict = PASS | T1.6 producing script output |
| **g_star_BS_T_H pin source** | `g_star_BS_T_H_FW` from canonical_constants.py (post-T1.6-PASS canonical promotion) | T1.6 PASS triggers canonical promotion via Step 2 of `math-scripts.md §"Canonical Write-Order"` |
| **T_H pin** | T_H = 1.057 MeV = 1.057e-3 GeV (substrate-pinned per S88 W6 §V.1) | S88 W6 §V.1; promote to `T_H_FW` canonical pin if not yet landed |
| **A_horizon pin** | Substrate-IS horizon area per S88 W6 §V.5; promote to `A_horizon_FW` canonical pin if not yet landed | S88 W6 §V.5 |
| **L_H_canonical formula** | L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴ in natural units (GeV⁴) | S88 W6 §V.5 Result 2 substrate-IS cascade-tail formula |
| **f(M_at_W1c69) reference** | S88 §W1c-69 baseline value | S88 workshop or npz source |
| **PASS bands** | delta_log < 0.5 log-OOM ABSOLUTE AND log_residual_improvement ≥ 1.0 log-OOM | S90 W4 CF-39 plan §W4-3 §9 (preserved) |
| **Option A supersedes target full 64-char** | `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` | S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY at `s88_gate_verdicts.txt:34` (verified at S90 W4 §W4-3 line 287) |
| **Mechanical-closure rule** | `.claude/rules/mechanical-closure-discipline.md` 5-clause admissibility | Standard mechanical-closure protocol |
| **Writer** | mack-cosmic-bridge primary | `feedback_mack-bridge-role.md` |
| **Verdict file** | `computations/session-91/s91_gate_verdicts.txt` | `gate-verdicts.md §"Canonical Verdict-File Path"` |

### 8. Expected output 4-tuple

**PASS branch**: `(value='L_H_canonical=<v>;delta_log=<dl>;log_residual_improvement=<lri>;supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d', scheme='substrate-cascade-tail-S88-W6-V5-resultII', convention='mack-cosmic-bridge-primary-Option-A-supersedes-emission-corrective', L_max='N/A')`

**FAIL mechanical branch**: `(value='PRE-REG-INC_blocked_by_S91_CF40_FAIL_supersedes_emission_deferred', scheme='substrate-cascade-tail-S88-W6-V5-resultII', convention='mack-cosmic-bridge-primary-mechanical-closure-PRE-REG-INC', L_max='N/A')`

L_max = N/A because the cascade-tail formula is L_max-independent at the structural form layer (per S88 W6 §V.5 substrate cascade form; the L_max-dependent observable is the substrate cardinality refinement at the §W1-4 PBH band-edge gate, NOT the cascade-tail luminosity).

### 9. PASS / FAIL / INFO thresholds

- **PASS** (substantive branch): T1.6 PASS prerequisite met; delta_log < 0.5 log-OOM ABSOLUTE AND log_residual_improvement ≥ 1.0 log-OOM; Option-A `supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` token correctly emitted as FULL 64-character form (NOT 16-char head per `gate-verdicts.md` `closure SHA must be full 64-char` rule). PASS shifts downstream canonical reading from S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY to this T1.7 corrective line per supersession-chain reading discipline.

- **INFO** (substantive branch): T1.6 PASS prerequisite met; delta_log ∈ [0.5, 1.0) OR log_residual_improvement ∈ [0.5, 1.0). The refinement is structurally meaningful but does not reach the PASS band; documented as INFO advance with the supersedes-tag emission DEFERRED (the S88 reading remains canonical until a future PASS refinement); routes to S92+ as a deeper refinement carry-forward.

- **FAIL mechanical branch** (T1.6 returned FAIL): PRE-REG-INC closure per `mechanical-closure-discipline.md` 5-clause admissibility; no substantive computation performed; no supersedes-tag emission; S88 reading remains canonical at absolute verdict permanence; carry-forward to S92+ retry conditional on a refined T1.6 PASS in S92+.

- **FAIL substantive branch** (T1.6 PASS but delta_log ≥ 1.0 OR log_residual_improvement < 0.5): the refinement attempted but the residual remains > 1.0 log-OOM from baseline OR the improvement is < 0.5 log-OOM (the canonical FD/BE g_*(T_H) does NOT close the 13-OOM gap from S88 §W1c-69 baseline meaningfully); routes to S92+ as a deeper cascade-form-or-anchor scrutiny carry-forward. No supersedes-tag emission.

### 10. Substitution chain (substrate-cascade-tail-luminosity direction)

```
Step 1 (definition): Substrate cascade tail at S88 W6 §V.5 Result 2: f_M = (π²/60) · g_*(T) · A · T⁴ (substrate-IS observable; structural identity at the substrate cascade-tail formula layer)

Step 2 (substitution at T = T_H = 1.057 MeV horizon): L_H_canonical_T1.7 = (π²/60) · g_*_FD/BE(T_H) · A_horizon · T_H⁴

Step 3 (T1.6 PASS canonical promotion): g_*_FD/BE(T_H) = g_star_BS_T_H_FW [pinned at canonical_constants.py post-T1.6-PASS Step 2]

Step 4 (numerical substitution; representative trial values from lizzi-s4-meta-p3-synthesis prediction):
    Assume T1.6 PASS produces g_star_BS_T_H_FW ≈ 9.5-10.0 (refined from S90 CF-40 FAIL value 9.4083 toward the canonical PDG g_*(1 MeV) = 10.75)
    Then L_H_canonical_T1.7 ≈ (π²/60) · 9.7 · A_horizon · (1.057e-3 GeV)⁴
                            ≈ 1.596 · A_horizon · 1.247e-12 GeV⁴

Step 5 (comparison to S88 §W1c-69 reference baseline):
    f(M_at_W1c69) = <S88 reference value, in same natural units as L_H_canonical>
    residual_T1.7 = L_H_canonical_T1.7 − f(M_at_W1c69)
    delta_log = |log10(L_H_canonical_T1.7) − log10(f(M_at_W1c69))|

Step 6 (improvement relative to S88 baseline):
    residual_S88 = L_H_canonical_S88(g_*_simplified) − f(M_at_W1c69)   [original 13-OOM gap]
    log_residual_improvement = log10(|residual_S88|) − log10(|residual_T1.7|)

Step 7 (direction read-off): Sign of log_residual_improvement: if positive, refinement reduces gap (PASS direction); if negative, refinement WIDENS gap (sign_verdict = FAIL — would indicate the FD/BE form gives WORSE agreement than simplified, which is structurally unexpected).
    Predicted direction (T1.6 PASS): log_residual_improvement > 0 (FD/BE refinement reduces the gap). Required magnitude: ≥ 1.0 log-OOM for PASS.
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** (substantive + supersedes-emission): the substrate cascade-tail luminosity L_H_canonical at substrate-pinned T_H is re-pinned with refined g_*(T_H) from T1.6 PASS; the S88 §W1c-69 13-OOM gap is reduced by at least 1.0 log-OOM. Constraint-map advance:
  - The substrate cascade tail anchor at S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY is SUPERSEDED at downstream consumer reading; latest non-superseded canonical line is the T1.7 corrective line.
  - The species-multiplicity cascade T1.6 → T1.7 chain CLOSES with both PASSes; downstream §VII registry entries citing the cascade-tail luminosity can now cite the T1.7 audit_sha256 + the T1.6 audit_sha256 as the supersession-chain provenance.
  - The S88 absolute verdict permanence is preserved (the original PASS line remains on disk at `s88_gate_verdicts.txt` line 34; the corrective T1.7 PASS line APPENDS).

- **INFO** (substantive; refinement structurally meaningful but sub-band): the refinement reduces the gap but not to the PASS band. S88 reading remains canonical; documented as INFO advance with carry-forward to S92+ for deeper refinement (e.g., revisit A_horizon substrate-derivation, or revisit T_H pin from S88 W6 §V.1).

- **FAIL mechanical** (T1.6 FAIL): no substantive computation; PRE-REG-INC closure per `mechanical-closure-discipline.md`; S88 reading remains canonical; supersedes-emission deferred to S92+ retry. Constraint-map: the species-multiplicity cascade T1.6 → T1.7 chain does NOT close at S91; species-multiplicity refinement axis remains open.

- **FAIL substantive** (T1.6 PASS but T1.7 substantive FAIL): the FD/BE refinement does NOT close the 13-OOM gap; identifies a deeper substrate-cascade-form-or-anchor problem; routes to S92+ for inspection of either (a) the substrate-IS cascade-tail formula at S88 W6 §V.5 Result 2 (revisit the structural identity), or (b) the f(M_at_W1c69) reference baseline at S88 (revisit the laboratory-IN anchor), or (c) the A_horizon substrate-derivation, or (d) the T_H pin at 1.057 MeV.

### 12. Effort estimate

~0.5 wave-equivalent (mack-cosmic-bridge primary author). Breakdown: ~15 min T1.6 PASS verification + g_star_BS_T_H_FW canonical-pin read; ~15 min L_H_canonical computation + residual comparison + supersedes-tag emission; ~10 min cross-checks; ~10 min verdict line + working paper section. Total estimated wall time ~50 min. NOTE: FAIL mechanical branch is faster (~15 min total — mechanical closure script execution + working paper PRE-REG-INC documentation).

### 13. Substrate-framing reminder

In the dispatch prompt §6 above, the explicit reminder reads: "the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the substrate's cascade-tail luminosity at T_H = 1.057 MeV horizon IS the substrate-IS observable L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴ per S88 W6 §V.5 Result 2. Direction of explanation: substrate cascade form (S88 W6 §V.5 structural identity) → bridge map (this gate's L_H_canonical evaluation at substrate-pinned T_H) → laboratory-IN cosmological-horizon observable (S88 §W1c-69 reference baseline f(M_at_W1c69)). The Option-A supersedes-tag emission preserves S88 absolute verdict permanence." This satisfies `phononic-framing.md §"IS Space, Not IN Space"` directional pre-registration and `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` Step 1 (original line retained) + Step 2 (corrective line with supersedes tag).

---

## §W3-3. CF-S91-CF37-AUX-4-SECONDARY-CORRIDOR (T1.8) [EXCLUDED: connes-ncg + phonon-first-cosmologist]

### 1. Gate ID

`S91-CF37-AUX-4-SECONDARY-CORRIDOR` (synonym `CF-S91-CF37-AUX-4-SECONDARY-CORRIDOR`; origin: `sessions/archive/session-90/session-90-w4-workingpaper.md §"Carry-Forward Computations"` line 724-731 + S90 W-1 workshop secondary-corridor pre-registration; PARALLEL with T1.9 at S91 W3)

### 2. Trigger

`[VERIFY-THEOREM]` ∧ `[SIGN]` — `[VERIFY-THEOREM]` because the gate evaluates a Connes-Karoubi pairing structural identity on the substrate spectral triple with the (c)∘(d) compositional secondary corridor's element-1 = γ(s) ≠ Γ(s) modified-universal-kernel cohomology-class shift; `[SIGN]` because the substitution chain pre-registers the direction (0 < α''(M_LRD) < 1 sign-bounded prediction at element-3 inheritance-restricted projector saturation g(M_LRD, L=10) = 1.000 at L_max=10).

### 3. Classification

GEOMETRIC — Cell-I cohomology-class observable; algebra-INVARIANT spectrum-only functional (per S90 W4 §W4-1 CF-37 §3 classification; the (c)∘(d) corridor inherits CF-37's classification at the structural-deformation-pattern layer; the structural-output-type is the same Cell-I algebra-INVARIANT spectrum-only functional, only the element-1 deformation choice differs from (d) χ'-pullback to (c) γ(s) ≠ Γ(s) modified-universal-kernel).

### 4. Agent type

**EXCLUDED reviewers** (HARD; per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` clause 2 downstream-inheritance reach extension + S91 context file §"W3" line 185 OAA exclusion):
- `connes-ncg-theorist`: HARD-excluded. connes-ncg is the original co-author of the CF-37 (d)∘(b) primary corridor at S90 W-1 workshop and is the textual originator of the (c)∘(d) secondary corridor's AUX-4 pre-registration; downstream-inheritance reach extends to producing-script + cross-review layer at S91.
- `phonon-first-cosmologist`: HARD-excluded. phonon-first is the original primary author of CF-37 at S90 W4 (per `session-90-w4-workingpaper.md §W4-1` Agent line) and the originator of the LRD α-anchor pursuit hypothesis; downstream-inheritance reach extends to S91.

**PRIMARY** (compute author + verdict emission; non-connes / non-phonon-first):
- **Axis-A reviewer (substrate-physics)**: SELECT ONE from {`volovik-superfluid-universe-theorist`, `van-den-dungen-bridge-theorist`, `gen-physicist`}. Recommended: `volovik-superfluid-universe-theorist` per `feedback_agent-roster.md` (volovik is the framework's sharpest reviewer; cocycle/spectral-pairing machinery is volovik's domain).
- **Axis-B reviewer (NCG-axiomatic / bridge-map content; non-connes-ncg)**: SELECT ONE from {`van-den-dungen-bridge-theorist`, `mack-cosmic-bridge`, `landau-condensed-matter-theorist`}. Recommended: `van-den-dungen-bridge-theorist` (NCG submersion + bridge map specialist; non-connes-ncg domain expert on Connes-Karoubi pairings and HKR bridge maps).

**COMPOSITE assignment** (orchestrator selects at dispatch time; not pre-fixed at plan-freeze): Axis-A = volovik-superfluid-universe-theorist (primary compute author); Axis-B = van-den-dungen-bridge-theorist (cross-review on bridge map + γ(s) kernel choice substrate-derivation).

NOT `gen-physicist` as primary per spawn-prompt constraint; gen-physicist may serve as Axis-A only if volovik is unavailable, OR as numerical-integration cross-check co-author analogous to T1.6.

### 5. Hypothesis

Activate the W-1 workshop's secondary corridor (c)∘(d) where element-1 = (c) modified-universal-kernel γ(s) ≠ Γ(s) cohomology-class shift (instead of (b) χ'-pullback used in CF-37 (d)∘(b)) and element-3 retains the inheritance-restricted projector P_HSS'(M) = χ'^*(P_HSS(M)). Compute α''(M_LRD = 10⁷, L_max=10) at the (c)∘(d) corridor on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` via the Connes-Moscovici 1995 §III.4 residue formula MODIFIED for γ(s) ≠ Γ(s) kernel choice; test against empirical anchor 1/458 = 2.18e-3 at the default 30% RATIO band per Sub-clause B (per S90 W4 CF-37 plan §11; CF-38 FAIL retained default band rather than tightening to 10%); also test Sub-clause A (sign 0<α''<1) and Sub-clause C (envelope α''(M) = 1 + c·(M/M_thr)^{-n} with n>0 + R²≥0.95). Composite PASS opens (c)∘(d) as the LRD α-anchor candidate with substrate-derived provenance; advances the simultaneous element-1 + element-3 double-deformation pattern calibration corpus to instance #2 (instance #1 = §VII.AF.1.OP-PROJ W-5 baseline LANDED S87 W5-1).

### 6. Method — COMPLETE dispatch prompt for non-connes / non-phonon-first reviewer pair

> **Dispatch prompt (verbatim)**:
>
> You are dispatched as PRIMARY computation author for `S91-CF37-AUX-4-SECONDARY-CORRIDOR` (T1.8 of S91 W3). Per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` clause 2 downstream-inheritance reach extension, `connes-ncg-theorist` and `phonon-first-cosmologist` are HARD-EXCLUDED from BOTH reviewer roles for this gate; you are operating in a non-connes-ncg + non-phonon-first reviewer dispatch. Axis-A (substrate-physics): you are the primary compute author (recommended: volovik-superfluid-universe-theorist). Axis-B (NCG-axiomatic / bridge-map cross-review): a parallel-dispatched non-connes-ncg reviewer (recommended: van-den-dungen-bridge-theorist) authors the bridge-map cross-review sub-section.
>
> **Substrate framing reminder**: per `phononic-framing.md §"IS Space, Not IN Space"`, the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the (c)∘(d) compositional corridor evaluates a Connes-Karoubi pairing on the substrate's intrinsic Hochschild cocycle space (under element-1 = (c) modified-universal-kernel γ(s) ≠ Γ(s) cohomology-class shift) AND the inheritance-restricted Peter-Weyl horizon-spanning projector (element-3 = (d) χ' inheritance image of P_HSS(M) at M_LRD scale). The α''(M_LRD) prediction IS the substrate's intrinsic ratio at the LRD scale; the empirical 1/458 anchor is a laboratory-IN observable; direction substrate → bridge map → laboratory observable. Do NOT frame the AUX-4 corridor as "exploring different element-1 deformations to find the one that matches data"; the (c) modified-universal-kernel γ(s) is the W-1 workshop's pre-registered secondary candidate after (d)∘(b) closure at S90 W4 CF-37 FAIL, with γ(s) ≠ Γ(s) supplying a structurally distinct cohomology-class shift (NOT a numerical-tuning parameter).
>
> **Producing script construction**:
>
> 1. New script at `computations/session-91/s91_w3_alpha_m_aux4_corridor_c_compose_d.py` (~430+ lines; fork from `computations/session-90/s90_w4_alpha_m_alt_corridor_d_compose_b.py` to preserve the substrate-physics scaffolding, then replace element-1 deformation from (b) χ'-pullback to (c) γ(s) ≠ Γ(s) modified-universal-kernel).
> 2. Load substrate inputs:
>    - `s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 (78,080 eigenvalues across 65 sectors); preserve per-sector eigenvalue indexing
>    - `s89_w2_a7_chi_prime_inheritance_morphism.npz` (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`); element-3 retains χ' from S89 §W2-3 derived theorem (ker rank = 9 on M_3(C); Wedderburn 9 > 8 forces zero map on M_3(C))
>    - canonical_constants pins: M_KK = 7.428660e+16 GeV, M_Pl_reduced = 2.435e+18 GeV, R_universal_HP1_strict_F4 = 1.030902, eps_H_HP1_norm = 16.197719, tau_fold = 0.190
> 3. Specify the modified-universal-kernel γ(s) ≠ Γ(s) (Element-1 (c) deformation):
>    - The standard universal kernel is Γ(s) = ∫₀^∞ t^{s-1} e^{-t} dt (gamma function; the standard residue formula's kernel in Connes-Moscovici 1995 §III.4)
>    - γ(s) is the modified-universal-kernel of the W-1 workshop AUX-4 pre-registration. The structurally distinct form: γ(s) carries a substrate-modulated pole structure with shifted residues at substrate-distance poles s ∈ {1, 2, 3, ...} relative to Γ(s); the modification reflects the (c) cohomology-class shift away from the canonical universal kernel.
>    - Substrate-derivation of γ(s): per W-1 workshop AUX-4 source, γ(s) is the cohomology-class image under (c) of the universal kernel Γ(s); the closed form is `γ(s) = Γ(s) · (1 + c_aux · (s - s_*)^{-1})` for s_* the substrate-distance pole of element-1's modified-kernel residue (default candidate: s_* = 1 substrate-distance pole; alternative: s_* = 3 per substrate-distance Mellin pole pattern). The constant c_aux is substrate-derived; default candidate c_aux = (rank(C) − rank(M_2(C)) + rank(M_3(C))) / (rank(C) + rank(M_2(C)) + rank(M_3(C))) = (1 − 2 + 3)/6 = 1/3 (substrate-Wedderburn algebra weight at element-1 layer; ALTERNATIVE forms admissible if the substrate-derivation specifies otherwise — honest disclosure required in working-paper §"Methodology" subsection).
> 4. Construct P_HSS'(M_LRD) = χ'^*(P_HSS(M_LRD)) inheritance-restricted Peter-Weyl horizon-spanning projector (element-3 (d)). This is IDENTICAL to CF-37's element-3 construction; preserve from S90 W4 CF-37 script.
> 5. Compute α''(M_LRD = 10⁷, L_max=10) via:
>    - Connes-Karoubi pairing ⟨γ(s)·[φ_g^{sym}], [Ch(P_HSS'(M_LRD))]⟩ where γ(s) is the element-1 (c) modified-universal-kernel and [Ch(P_HSS'(M_LRD))] is the Chern character of the element-3 (d) inheritance-restricted projector
>    - The pairing is evaluated at the substrate-distance pole s = 1 (default) via residue formula `Res_{s=s_*} [γ(s) · pairing(s)]`
>    - Closed form (analogous to CF-37 structural ansatz, modified for element-1 (c) kernel choice): α''(M_LRD) = R_universal_HP1_strict_F4 · γ_weight_aux · (M_KK/M_Pl_reduced)² · g(M_LRD, L=10) where γ_weight_aux is the (c)-deformation analog of χ'_weight = 0.5 used in CF-37 (d)
>    - Default candidate for γ_weight_aux: a Wedderburn-rank-adjusted factor that accounts for the (c) cohomology-class shift — substrate-derivation candidates include (1) γ_weight_aux = (rank(C) + rank(M_2(C)) + rank(M_3(C))) / (rank(M_2(C)) + rank(M_3(C))) = 6/5 = 1.2 (un-restricted Wedderburn ratio; the (c) shift OPENS the M_3(C) summand that χ' kills), OR (2) γ_weight_aux = c_aux · χ'_weight = (1/3) · 0.5 = 1/6 ≈ 0.167 (γ-modulated χ'-weight via element-1 (c) shift), OR (3) γ_weight_aux derived from full residue evaluation at s_* (the most defensible — full CM-1995 §III.4 evaluation with γ(s) kernel substituted). Honest disclosure: list ALL three candidates in working-paper §"Methodology" with the substrate-physics arguments for each.
> 6. Run the M-scan at M ∈ {10⁵, 10⁶, 10⁷, 10⁸, 10⁹} M_sun (same scan as CF-37) to test Sub-clause C envelope.
> 7. Sub-clause band tests (preserve from CF-37 §W4-1 §9):
>    - Sub-clause A: 0 < α''(M_LRD) < 1 (sign + bounded existence)
>    - Sub-clause B: |α''(M_LRD) − 1/458| / (1/458) ≤ 0.30 (30% RATIO band per CF-37 default; CF-38 FAIL retained at S90)
>    - Sub-clause C: envelope α''(M) = 1 + c·(M/M_thr)^{-n} with n > 0 + R² ≥ 0.95
>    - Composite collapse: ALL THREE Sub-clauses PASS → composite PASS; ANY ONE FAIL → composite FAIL
> 8. Output npz keys (mandatory):
>    - alpha_double_prime_M_LRD_value (full float64); alpha_double_prime_M_LRD_pub5sf (5-sig-fig publication precision per Class 8.3)
>    - gamma_weight_aux_candidates (3-element array: candidates (1), (2), (3) per Step 5)
>    - gamma_weight_aux_canonical (selected canonical; documented in working paper)
>    - empirical_anchor_1_over_458 = 2.183406e-03
>    - rel_dev_M_LRD = |α'' − 1/458|/(1/458)
>    - sub_clause_A_verdict, sub_clause_B_verdict, sub_clause_C_verdict, composite
>    - M_scan, g_M_scan, alpha_double_prime_scan (M-scan results)
>    - envelope_c, envelope_n, envelope_R_squared
>    - bot20_occupation (preserve from CF-37; same substrate spectrum filtering)
>    - L_max = 10
>    - s_star (substrate-distance pole choice; default s_star = 1)
>    - c_aux (γ(s) kernel modulation constant)
>    - regulator_pin = "Mellin-Barnes-modified-universal-kernel-gamma-s"
>    - chi_prime_anchor_audit_sha = "90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843"
>    - calibration_corpus_instance = "instance_2_pending" (PASS would advance K=1 → K=2 on simultaneous element-1+element-3 double-deformation pattern)
>    - audit_sha256, content_sha256, schema_version
> 9. Plot: α''(M) vs M log-log with empirical anchor 1/458 + 30% RATIO band overlaid; analogous to CF-37 plot.
> 10. Single-shot AFTER-pattern emission per `registry-landing.md §"Bridge-Landing Script Architecture"`.
>
> **Axis-B parallel cross-review sub-section** (dispatched separately to non-connes-ncg bridge-map reviewer; recommended van-den-dungen-bridge-theorist):
>
> 1. Receive Axis-A producing-script .npz output (read-only consumption).
> 2. Cross-check the γ(s) ≠ Γ(s) modified-universal-kernel structural form against the W-1 workshop AUX-4 pre-registration source; verify the cohomology-class shift is a STRUCTURAL identity at the substrate algebra layer (NOT a numerical-tuning parameter).
> 3. Cross-check the γ_weight_aux candidate selection against substrate-derivation arguments; verify the canonical candidate's substrate-physics provenance (per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY level-pin discipline at K=4 promotion).
> 4. Cross-check the residue-formula evaluation at substrate-distance pole s_* against Connes-Moscovici 1995 §III.4 (with γ(s) kernel substituted); verify the modified-universal-kernel pole structure is consistent with the substrate-IS Hochschild cohomology.
> 5. Author cross-review sub-section in working paper §W3-3 §"Axis-B cross-review" (≥ 10 lines).
>
> **Verdict line** at `computations/session-91/s91_gate_verdicts.txt`:
>
> ```
> S91-CF37-AUX-4-SECONDARY-CORRIDOR: PASS|FAIL -- value='alpha_double_prime_M_LRD=<v>;empirical_anchor=2.18341e-03;rel_dev=<r>;sub_A=<a>;sub_B=<b>;sub_C=<c>;composite=<comp>;gamma_weight_aux_canonical=<g>;s_star=<s>;...' scheme=connes-karoubi-pairing-on-gamma-s-modified-universal-kernel convention=substrate-IS-Cell-I-K-counter-instance-2-AUX-4-SECONDARY-CORRIDOR-NON-CONNES-NON-PHONON-FIRST-AUTHOR L_max=10 audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
> ```
>
> Companion dual-SHA row + (since `[SIGN]` trigger) 3-tuple annotation:
>
> ```
> # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # S91-CF37-AUX-4-SECONDARY-CORRIDOR dual-SHA companion row (W9a-99 split)
> # sign_verdict=PASS|FAIL magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # S91-CF37-AUX-4-SECONDARY-CORRIDOR 3-tuple annotation (S87 schema-v2)
> ```
>
> **Working paper section** at `sessions/archive/session-91/session-91-w3-workingpaper.md §W3-3`: ≥ 20 substantive lines per W4 CF-37 precedent. Sections: Status (top), Gate ID, Trigger, Classification, Agent (non-connes / non-phonon-first declaration), Hypothesis, Plan reference, MCP Pre-Compute Audit, Verdict line + dual-SHA + 3-tuple, Results (4-tuple, γ_weight_aux candidate enumeration, sub-clause table, M-scan table, envelope fit, bot20_occupation, χ' anchor SHA, calibration-corpus instance status), Cross-checks performed (Axis-A self-checks; Axis-B parallel cross-review sub-section), Data files produced, Solution-space implication, Substrate framing reminder.

### 7. Machinery pin (PRDR)

| PRDR Element | Pin | Source |
|:-------------|:----|:-------|
| **Substrate spectrum cache** | `s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 | S84 master cache |
| **χ' inheritance morphism (element-3 (d))** | `s89_w2_a7_chi_prime_inheritance_morphism.npz` (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`) | S89 §W2-3 derived theorem |
| **Element-1 (c) modified-universal-kernel γ(s) ≠ Γ(s)** | γ(s) = Γ(s) · (1 + c_aux · (s − s_*)^{-1}) with default s_* = 1 substrate-distance pole + c_aux = 1/3 (substrate-Wedderburn algebra weight at element-1 layer) | W-1 workshop AUX-4 pre-registration; substrate-Wedderburn algebra-weight derivation |
| **γ_weight_aux candidate set** | Three candidates: (1) γ_weight_aux = 6/5 = 1.2; (2) γ_weight_aux = c_aux · χ'_weight = 1/6 ≈ 0.167; (3) γ_weight_aux from full residue evaluation at s_* (most defensible) | Honest disclosure in working paper; substrate-derivation candidates per §6 Step 5 |
| **R_universal_HP1_strict_F4 pin** | 1.030902 (Class-(d) PROVENANCE; PRIMARY canonical = eps_H_HP1_norm = 16.197719) | canonical_constants.py:250 |
| **eps_H_HP1_norm primary canonical** | 16.197719 | canonical_constants.py:171 |
| **M_KK, M_Pl_reduced canonical pins** | 7.428660e+16 GeV / 2.435e+18 GeV; (M_KK/M_Pl_reduced)² = 9.307286e-04 | canonical_constants.py:341 + CODATA 2018 |
| **L_max truncation** | L_max = 10 (matching S90 CF-37 truncation for direct comparability to PROXY-REFINEMENT-PENDING baseline) | S90 W4 CF-37 L_max pin |
| **bot20_occupation** | Substrate L=10 bot-20 sector occupation `{(0,0): 8, (0,1): 6, (1,0): 6}` total 20 ✓ | Per S90 W4 CF-37 §W4-1 *spectral content* table |
| **Sub-clause band thresholds** | A: 0 < α'' < 1; B: rel_dev ≤ 0.30 RATIO (30% band per CF-37 default; CF-38 FAIL retained); C: n > 0 AND R² ≥ 0.95 | S90 W4 CF-37 §W4-1 §9 thresholds (preserved) |
| **M-scan range** | M ∈ {10⁵, 10⁶, 10⁷, 10⁸, 10⁹} M_sun | S90 W4 CF-37 §W4-1 M-scan (preserved) |
| **Single-shot AFTER-pattern emission** | `registry-landing.md §"Bridge-Landing Script Architecture"` REQUIRED | Standard registry-landing script architecture |
| **Reviewer assignments** | Axis-A: volovik-superfluid-universe-theorist (recommended); Axis-B: van-den-dungen-bridge-theorist (recommended) — both NON-connes-ncg + NON-phonon-first | S91 context file §"W3" line 185 OAA exclusion |
| **Verdict file** | `computations/session-91/s91_gate_verdicts.txt` | `gate-verdicts.md §"Canonical Verdict-File Path"` |
| **Calibration-corpus instance status** | "instance_2_pending"; PASS advances K=1 → K=2 (instance #1 = §VII.AF.1.OP-PROJ W-5 baseline LANDED S87 W5-1) | `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` |
| **GPU usage** | None — closed-form arithmetic + small per-sector residue evaluations on filtered spectrum (78,080 × few floats); CPU-only is appropriate | `computation-environment.md §"CPU Thread Cap When GPU Not Used"` thread cap OMP_NUM_THREADS=8 |

### 8. Expected output 4-tuple

`(value='alpha_double_prime_M_LRD=<v>;empirical_anchor=2.18341e-03;rel_dev=<r>;sub_A=<a>;sub_B=<b>;sub_C=<c>;composite=<comp>;gamma_weight_aux_canonical=<g>;s_star=<s>;...', scheme='connes-karoubi-pairing-on-gamma-s-modified-universal-kernel', convention='substrate-IS-Cell-I-K-counter-instance-2-AUX-4-SECONDARY-CORRIDOR-NON-CONNES-NON-PHONON-FIRST-AUTHOR', L_max='10')`

### 9. PASS / FAIL / INFO thresholds

- **PASS** (composite): Sub-clause A PASS (0 < α'' < 1) AND Sub-clause B PASS (rel_dev ≤ 0.30 RATIO) AND Sub-clause C PASS (envelope n > 0 + R² ≥ 0.95). Calibration-corpus instance #2 LANDED at Cell-I simultaneous element-1+element-3 double-deformation pattern; Hybrid Independence Test K-counter advances K=1 → K=2 (W-5 baseline instance #1 = (d)∘(d) double-deformation at §VII.AF.1.OP-PROJ; T1.8 PASS instance #2 = (c)∘(d) double-deformation; structural axes of independence — element-1 deformation choice differs ((c) vs (d) on instance #1)). LRD α-anchor candidate opened at (c)∘(d) corridor with substrate-derived provenance.

- **INFO**: Sub-clause A PASS AND Sub-clause B INFO (0.10 < rel_dev ≤ 0.30) AND Sub-clause C PASS. PASS-band-near-but-not-PASS-band-met routing; identifies γ(s) kernel substrate-derivation candidate is structurally meaningful but not at PASS precision. Routes to S92+ for γ(s) kernel substrate-derivation refinement (e.g., choose different γ_weight_aux candidate or alternative s_* substrate-distance pole).

- **FAIL** (composite): ANY ONE Sub-clause FAILs. (c)∘(d) corridor CLOSED as the LRD α-anchor candidate at the structural-ansatz-with-γ(s)-kernel-pin layer; routes to (i) T1.9 substantive evaluation (if also FAIL, then both (d)∘(b)-PROXY-REFINEMENT-PENDING-revisit and (c)∘(d) closed); (ii) substrate-distance-2 §VII.AX forward gates at S91 W0 R5 landing if both T1.8 + T1.9 FAIL.

### 10. Substitution chain (substrate-IS sign + LRD-anchor direction; analogous to CF-37 §10 with element-1 (c) substituted)

```
Step 1 (definition): φ_g^{sym} ∈ HH^1(A_K) gradient-symmetric Hochschild 1-cocycle on A_K = C ⊕ H ⊕ M_3(C); cohomology class [φ_g^{sym}] regulator-class INVARIANT (W-5 calibration corpus instance #1 anchor); χ': A_K → M_2(C) ⊗ Cl(1) inheritance morphism (S89 §W2-3 derived theorem); γ(s) modified-universal-kernel ≠ Γ(s); P_HSS'(M) = χ'^*(P_HSS(M)) inheritance-restricted Peter-Weyl horizon-spanning projector.

Step 2 (positivity numerator): γ(s) modulated cohomology class image carries the (c) shift relative to Γ(s); for s_* > 0, the residue Res_{s=s_*}[γ(s) · pairing(s)] is non-zero by construction of the modified-universal-kernel pole. P_HSS'(M_LRD) is a positive idempotent in K_0(BdG-sub-algebra) → [Ch(P_HSS'(M_LRD))] non-negative element of HH^*_even. Pairing numerator > 0.

Step 3 (positivity denominator + dimensional bridge): M_KK² > 0, S_BH^semicl(M_LRD; M_Pl_reduced²) > 0, (M_KK/M_Pl_reduced)² = 9.307286e-04 > 0.

Step 4 (substrate saturation): g(M_LRD, L=10) = 1.000000 ∈ (0, 1] (inheritance-restricted projector saturates L=10 substrate at M_LRD = 10⁷ M_sun; SAME as CF-37 since element-3 (d) is identical).

Step 5 (combine; canonical γ_weight_aux candidate (3) — full residue evaluation): α''(M_LRD) = R_universal_HP1_strict_F4 · γ_weight_aux_canonical · (M_KK/M_Pl_reduced)² · g(M_LRD, L=10) = 1.030902 · γ_weight_aux_canonical · 9.307286e-04 · 1.000.

Step 6 (sub-clause direction read-off): 0 < γ_weight_aux_canonical < ∞ ⇒ 0 < α''(M_LRD) < (saturating bound). For candidate (1) γ_weight_aux = 1.2: α''(M_LRD) = 1.151e-3 (FAIL Sub-clause B: rel_dev = 0.47); for candidate (2) γ_weight_aux = 1/6: α''(M_LRD) = 1.600e-4 (FAIL Sub-clause B: rel_dev = 0.93); for candidate (3) full residue evaluation: α''(M_LRD) value is the gate's substantive output (NOT pre-committed numerically; the substrate-physics computation produces it). If candidate (3) lands in Sub-clause B 30% band [1.527e-3, 2.836e-3] ↔ γ_weight_aux ∈ [1.591, 2.953], composite PASS.

Step 7 (direction): the (c)∘(d) corridor sign-direction is the same as (d)∘(b) (Sub-clause A PASS by Step 4 saturation + positive pairing); the MAGNITUDE adjudication is the substantive substrate-physics question that the gate evaluates (NOT pre-determined). Honest direction read-off: 0 < α'' < 1 PRE-COMMITTED (Sub-clause A); magnitude is OPEN at plan-freeze (the gate's empirical content).
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** (composite): (c)∘(d) corridor opens as LRD α-anchor candidate with substrate-derived provenance. Constraint-map advance:
  - The simultaneous element-1+element-3 double-deformation pattern calibration corpus advances to K=2 (instance #1 = W-5 baseline §VII.AF.1.OP-PROJ; instance #2 = T1.8 PASS).
  - Hybrid Independence Test K-counter advances K=1 → K=2 on the element-1 deformation axis (structural independence: (c) vs (d) on element-1).
  - Empirical anchor 1/458 PROMOTION candidate: T1.8 PASS supplies substrate-derived provenance for a future `alpha_LRD_FW` canonical_constants.py promotion (per CF-38 FAIL diagnostic at S90 W4 — the 1/458 anchor needed substrate-derived provenance to promote).
  - Routes to S91+ AUX-5 three-axis Stage-2 cross-axis independent-verify (lizzi + volovik + mack; EXCLUDES connes-ncg + phonon-first per OAA — same exclusion pattern as T1.8 + T1.9).
  - If BOTH T1.8 + T1.9 PASS: parallel admissibility — both (c)∘(d) and (d)∘(b)+FULL-CM-1995 evaluations land in the 30% RATIO band; the substrate's intrinsic determinism becomes the S92+ adjudication question (which of the two pathways is the canonical LRD α-anchor derivation, or are they Two-Independent-Axes structures per §"Element 3 fiducial-anchor binding discipline" Joint-hypersurface form).

- **INFO**: (c)∘(d) corridor is structurally meaningful at the substrate-derivation layer but does not reach the 30% RATIO band PASS precision; routes to S92+ for γ(s) kernel substrate-derivation refinement.

- **FAIL** (composite): (c)∘(d) corridor CLOSED at the γ(s) modified-universal-kernel structural-ansatz layer. Constraint-map advance:
  - The (c)∘(d) secondary corridor is closed as the LRD α-anchor candidate at the structural-ansatz-with-γ(s)-kernel-pin layer; further pursuit requires γ(s) kernel substrate-derivation refinement OR routing to substrate-distance-2 §VII.AX forward gates.
  - The simultaneous element-1+element-3 double-deformation pattern calibration corpus stays at K=1 (W-5 baseline only); Hybrid Independence Test K-counter unchanged.
  - If BOTH T1.8 + T1.9 FAIL: the LRD α-anchor pursuit at substrate-distance-1 pole is closed at the structural-ansatz layer for BOTH (d)∘(b)-PROXY-REFINEMENT-PENDING-revisit and (c)∘(d) corridors; routes to substrate-distance-2 §VII.AX forward gates at S91 W0 R5 landing as the next candidate domain.
  - If T1.8 FAIL but T1.9 PASS: (d)∘(b) corridor RECOVERS as the canonical LRD α-anchor with FULL-CM-1995 substrate-derivation; (c)∘(d) corridor stays closed.

### 12. Effort estimate

~3.5 wave-equivalents (similar to S90 CF-37 BIG effort estimate; the substantive substrate-physics evaluation at the (c)∘(d) corridor with γ(s) kernel substitution requires equivalent depth to the (d)∘(b) primary corridor). Breakdown:
- ~1.5 we Axis-A primary computation: fork CF-37 producing script + replace element-1 (b) → (c) γ(s) ≠ Γ(s); construct modified-universal-kernel; derive γ_weight_aux candidates (3 substrate-derivation arguments); compute α'' on L_max=10 substrate at M-scan; sub-clause band tests; output npz + plot + JSON.
- ~1.0 we Axis-B parallel cross-review: γ(s) structural form verification + γ_weight_aux substrate-derivation cross-check + residue-formula evaluation cross-check at s_* + working paper cross-review sub-section.
- ~1.0 we orchestrator integration: dispatch coordination + verdict-line emission + working paper section authoring + carry-forward routing (W3 → W4/W5 decision-point map).

### 13. Substrate-framing reminder

In the dispatch prompt §6 above, the explicit reminder reads: "the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the (c)∘(d) compositional corridor evaluates a Connes-Karoubi pairing on the substrate's intrinsic Hochschild cocycle space (under element-1 = (c) modified-universal-kernel γ(s) ≠ Γ(s) cohomology-class shift) AND the inheritance-restricted Peter-Weyl horizon-spanning projector (element-3 = (d) χ' inheritance image of P_HSS(M) at M_LRD scale). The α''(M_LRD) prediction IS the substrate's intrinsic ratio at the LRD scale; the empirical 1/458 anchor is a laboratory-IN observable; direction substrate → bridge map → laboratory observable. Do NOT frame the AUX-4 corridor as 'exploring different element-1 deformations to find the one that matches data'; the (c) modified-universal-kernel γ(s) is the W-1 workshop's pre-registered secondary candidate after (d)∘(b) closure at S90 W4 CF-37 FAIL, with γ(s) ≠ Γ(s) supplying a structurally distinct cohomology-class shift (NOT a numerical-tuning parameter)." This satisfies `phononic-framing.md §"IS Space, Not IN Space"` directional pre-registration AND `v3-closure-recovery.md §PROHIBITED_ACTIONS` Class 1 (convention-shopping is FORBIDDEN; γ_weight_aux candidate selection is substrate-derived, NOT iteratively tuned).

---

## §W3-4. CF-S91-CF37-FULL-CM1995-RESIDUE (T1.9) [EXCLUDED: connes-ncg + phonon-first-cosmologist]

### 1. Gate ID

`S91-CF37-FULL-CM1995-RESIDUE` (synonym `CF-S91-CF37-FULL-CM1995-RESIDUE`; origin: `sessions/archive/session-90/session-90-w4-workingpaper.md §"Carry-Forward Computations"` line 715-722 + S90 W4 CF-37 PROXY-REFINEMENT-PENDING tag at audit_sha256 `10ee072fe2c193f3...`; PARALLEL with T1.8 at S91 W3)

### 2. Trigger

`[VERIFY-THEOREM]` ∧ `[SIGN]` — `[VERIFY-THEOREM]` because the gate evaluates the FULL Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula at the (d)∘(b) compositional primary corridor on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`, replacing CF-37's structural-ansatz layer (Wedderburn-rank-ratio χ'_weight = 3/6 = 0.5 + dimensional bridge M_KK²/M_Pl_reduced²) with the full physical residue evaluation; `[SIGN]` because the substitution chain pre-registers the direction (0 < α'(M_LRD) < 1 sign-bounded prediction at element-3 saturation g(M_LRD, L=10) = 1.000; magnitude is OPEN at plan-freeze and constitutes the substantive substrate-physics evaluation).

### 3. Classification

GEOMETRIC — Cell-I cohomology-class observable; algebra-INVARIANT spectrum-only functional (same as S90 W4 CF-37 §3 classification; T1.9 retains element-1 (b) χ'-pullback and element-3 (d) inheritance restriction; only the residue-formula evaluator changes from CF-37's structural ansatz to FULL CM-1995 §III.4 physical evaluator).

### 4. Agent type

**EXCLUDED reviewers** (HARD; same OAA pattern as T1.8): `connes-ncg-theorist` HARD-excluded (original co-author of CF-37 at S90 W-1 workshop + textual originator of the FULL-CM-1995-RESIDUE pre-registration; downstream-inheritance reach extends to S91); `phonon-first-cosmologist` HARD-excluded (original primary author of CF-37 at S90 W4; downstream-inheritance reach extends to S91).

**IMPORTANT clarification per spawn prompt note**: The Connes-Moscovici 1995 §III.4 paper is the FIXED SOURCE document (a published research paper authored by Alain Connes and Henri Moscovici in 1995; the published source material is NOT subject to OAA — it pre-dates the framework and is the canonical reference for the residue formula machinery on finite spectral triples). The EVALUATOR (the framework agent who performs the residue-formula computation on the substrate `(A_K, H_K, D_K)`) IS subject to OAA exclusion: the evaluator MUST be a non-connes-ncg-theorist + non-phonon-first reviewer per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` clause 2 downstream-inheritance reach extension. The published CM-1995 paper is the source material; the gate's substantive computation IS the framework-internal evaluation of that source on the substrate.

**PRIMARY** (compute author + verdict emission; non-connes / non-phonon-first):
- **Axis-A reviewer (substrate-physics)**: SELECT ONE from {`volovik-superfluid-universe-theorist`, `van-den-dungen-bridge-theorist`, `gen-physicist`}. Recommended: `van-den-dungen-bridge-theorist` per `feedback_van-den-dungen-bridge.md` (NCG submersion + residue formula specialist; van-den-dungen is the framework's primary non-connes NCG-axiomatic reviewer for finite-spectral-triple residue evaluations).
- **Axis-B reviewer (cross-pillar bridge-map verification; non-connes-ncg)**: SELECT ONE from {`mack-cosmic-bridge`, `landau-condensed-matter-theorist`, `volovik-superfluid-universe-theorist`}. Recommended: `mack-cosmic-bridge` (cross-pillar bridge-anatomy reviewer; mack-bridge sole-writer authority on §VII registry entries per `feedback_mack-bridge-role.md`).

**COMPOSITE assignment** (orchestrator selects at dispatch time): Axis-A = van-den-dungen-bridge-theorist (primary compute author; FULL CM-1995 §III.4 residue evaluation specialist); Axis-B = mack-cosmic-bridge (cross-review on bridge map + registry-text potential landing).

NOT `gen-physicist` as primary per spawn-prompt constraint; gen-physicist may serve as Axis-A only if van-den-dungen is unavailable.

### 5. Hypothesis

Replace the structural-ansatz layer used in S90 W4 CF-37 (Wedderburn-rank-ratio χ'_weight = 3/6 = 0.5 + dimensional bridge M_KK²/M_Pl_reduced²) with FULL Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula evaluation on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` at the (d)∘(b) compositional primary corridor. Compute χ'^*[φ_g^{sym}] pullback rigorously (verify dχ'^*φ_g^{sym} = 0 at machine epsilon); construct P_HSS'(M) = χ'^*(P_HSS(M)) inheritance-restricted Peter-Weyl horizon-spanning projector with cutoff form derived from inheritance restriction (NOT naive λ² ≤ M_KK²·(M_LRD/M_KK²) used in CF-37); compute Chern character via residue formula on Peter-Weyl-decomposed triple; re-evaluate Connes-Karoubi pairing as finite trace sum. Test against empirical anchor 1/458 = 2.18e-3 at default 30% RATIO band per Sub-clause B (per CF-37 plan §11; CF-38 FAIL retained at S90); also test Sub-clause A (sign 0<α'<1) and Sub-clause C (envelope α'(M) = 1 + c·(M/M_thr)^{-n} with n>0 + R²≥0.95). On PASS: the FULL evaluation produces a χ'_weight factor SUBSTANTIVELY DIFFERENT from CF-37's structural-ansatz 0.5; if the FULL evaluation produces χ'_weight ~4.5× larger than 0.5 (e.g., 2.3, accounting for the factor 4.5× CF-37 under-shoot), the (d)∘(b) corridor RECOVERS as the canonical LRD α-anchor candidate; CF-37 PROXY-REFINEMENT-PENDING tag converts to PASS at the FULL-CM1995 substrate-derivation layer.

### 6. Method — COMPLETE dispatch prompt for non-connes / non-phonon-first reviewer pair

> **Dispatch prompt (verbatim)**:
>
> You are dispatched as PRIMARY computation author for `S91-CF37-FULL-CM1995-RESIDUE` (T1.9 of S91 W3). Per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` clause 2 downstream-inheritance reach extension + S91 context file §"W3" OAA exclusion, `connes-ncg-theorist` and `phonon-first-cosmologist` are HARD-EXCLUDED from BOTH reviewer roles. The Connes-Moscovici 1995 §III.4 paper IS the fixed source material (NOT subject to OAA — it is a published research paper); the evaluator (you) MUST be a non-connes-ncg + non-phonon-first reviewer. Axis-A (substrate-physics; primary compute author): recommended van-den-dungen-bridge-theorist (NCG submersion + residue formula specialist). Axis-B (cross-pillar bridge-map verification; non-connes-ncg): parallel-dispatched non-connes-ncg reviewer (recommended mack-cosmic-bridge).
>
> **Substrate framing reminder**: per `phononic-framing.md §"IS Space, Not IN Space"`, the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the FULL Connes-Moscovici 1995 §III.4 residue formula evaluates the Chern character of the Peter-Weyl-decomposed inheritance-restricted projector P_HSS'(M) on the substrate's intrinsic algebra A_K = C ⊕ H ⊕ M_3(C); the Connes-Karoubi pairing IS the substrate's intrinsic structural identity at the algebra-axis orthogonality K=3 MANDATORY clause's algebra-INVARIANT spectrum-only functional family. Direction substrate (Cell-I cohomology class) → bridge map (residue formula + Chern character) → laboratory observable (α'(M_LRD) at LRD-scale M = 10⁷ M_sun). Do NOT frame the FULL-CM1995 evaluation as "tuning the residue formula to match data"; the residue formula's value IS the substrate's structural prediction at the (d)∘(b) corridor, with NO numerical tuning available — the gate's substantive output IS that intrinsic value.
>
> **Producing script construction**:
>
> 1. New script at `computations/session-91/s91_w3_alpha_m_full_cm1995_residue_d_compose_b.py` (~500-600 lines; substantively more complex than the structural-ansatz CF-37 script due to full residue-formula evaluation).
> 2. Load substrate inputs (same as T1.8 + S90 CF-37):
>    - `s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 (78,080 eigenvalues across 65 Peter-Weyl sectors)
>    - `s89_w2_a7_chi_prime_inheritance_morphism.npz` (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`)
>    - canonical_constants pins: M_KK, M_Pl_reduced, R_universal_HP1_strict_F4, eps_H_HP1_norm, tau_fold
>    - Connes-Moscovici 1995 §III.4 source: the published paper's §III.4 residue formula machinery (consult primary source for canonical equation; the formula is the standard finite-spectral-triple Chern character residue formula at the dimension-spectrum poles).
> 3. Implement FULL CM-1995 §III.4 residue formula evaluator (replaces CF-37's structural-ansatz):
>    - **Pullback evaluation**: Compute χ'^*[φ_g^{sym}] pullback rigorously. Verify dχ'^*φ_g^{sym} = 0 at machine epsilon (NOT just structurally asserted as in CF-37; explicit Python evaluation of the differential).
>    - **Inheritance-restricted projector**: Construct P_HSS'(M_LRD) = χ'^*(P_HSS(M_LRD)) on the Peter-Weyl decomposition of `(A_K, H_K, D_K)` at L_max=10. The cutoff form is DERIVED from the inheritance restriction (NOT naive λ² ≤ M_KK²·(M_LRD/M_KK²) used in CF-37 §W4-1); the derived cutoff respects the χ' image structure (M_2(C) ⊗ Cl(1)).
>    - **Chern character via residue formula**: Evaluate ch(P_HSS'(M_LRD)) on the substrate spectral triple via the CM-1995 §III.4 residue formula `ch_k(P) = ⟨Res_{z=k} [Tr(P · D^{-2z})], pole at z = k⟩` for k ∈ dimension spectrum of `(A_K, H_K, D_K)`. The dimension spectrum at L_max=10 is computed from the eigenvalue spectrum (Peter-Weyl-decomposed); the residues at each pole are finite trace sums.
>    - **Connes-Karoubi pairing**: Final pairing `α'_FULL(M_LRD) = ⟨χ'^*[φ_g^{sym}], [ch(P_HSS'(M_LRD))]⟩` evaluated as the finite trace sum of the residue products.
> 4. Compare α'_FULL(M_LRD) to CF-37's structural-ansatz α'_CF37(M_LRD) = 4.797450e-04:
>    - If α'_FULL / α'_CF37 ~ 4.5× (in either direction): the structural-ansatz under- (or over-)shot by the expected factor; (d)∘(b) corridor RECOVERS or PERMANENTLY CLOSES depending on direction.
>    - The FULL evaluation produces an effective χ'_weight_FULL value (back-compute from α'_FULL = R_universal · χ'_weight_FULL · (M_KK/M_Pl_reduced)² · g(M_LRD, L=10), assuming the same multiplicative decomposition holds at the FULL evaluation layer; if the FULL evaluation does NOT decompose this way, document the structural reason in the working paper §"Methodology").
> 5. Run the M-scan at M ∈ {10⁵, 10⁶, 10⁷, 10⁸, 10⁹} M_sun (same as CF-37 + T1.8) for Sub-clause C envelope test.
> 6. Sub-clause band tests (preserve from CF-37 §W4-1 §9):
>    - Sub-clause A: 0 < α'_FULL(M_LRD) < 1
>    - Sub-clause B: |α'_FULL(M_LRD) − 1/458| / (1/458) ≤ 0.30 (30% RATIO band; CF-38 FAIL default retained)
>    - Sub-clause C: envelope α'_FULL(M) = 1 + c·(M/M_thr)^{-n} with n > 0 + R² ≥ 0.95
> 7. Output npz keys (mandatory):
>    - alpha_prime_FULL_M_LRD_value (full float64); alpha_prime_FULL_M_LRD_pub5sf (5-sig-fig per Class 8.3)
>    - chi_prime_weight_FULL (back-computed; for comparison to CF-37 0.5 structural-ansatz)
>    - factor_vs_CF37 = alpha_prime_FULL / alpha_prime_CF37_structural_ansatz
>    - empirical_anchor_1_over_458 = 2.183406e-03
>    - rel_dev_M_LRD = |α'_FULL − 1/458|/(1/458)
>    - sub_clause_A_verdict, sub_clause_B_verdict, sub_clause_C_verdict, composite
>    - M_scan, g_M_scan, alpha_prime_FULL_scan
>    - envelope_c, envelope_n, envelope_R_squared
>    - bot20_occupation (preserve from CF-37)
>    - dimension_spectrum_poles (extracted from L_max=10 substrate spectrum)
>    - residue_evaluations_per_pole (dict; object array)
>    - chi_prime_pullback_differential (machine-epsilon verification: dχ'^*φ_g^{sym} = 0)
>    - chern_character_components (per dimension-spectrum pole)
>    - L_max = 10
>    - regulator_pin = "Mellin-Barnes-standard-universal-kernel-Gamma-s"
>    - residue_formula_source = "Connes-Moscovici 1995 §III.4 finite-spectral-triple-residue-formula"
>    - chi_prime_anchor_audit_sha = "90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843"
>    - calibration_corpus_instance = "instance_2_pending" (PASS would advance K=1 → K=2 on simultaneous element-1+element-3 double-deformation pattern at Cell-I)
>    - cf37_revision_status = "FULL-CM1995-substrate-derivation-replaces-structural-ansatz"
>    - audit_sha256, content_sha256, schema_version
> 8. Plot: α'_FULL(M) vs M log-log with empirical anchor 1/458 + 30% RATIO band overlaid + α'_CF37 structural-ansatz value annotated for direct visual comparison; analogous to CF-37 plot.
> 9. Single-shot AFTER-pattern emission per `registry-landing.md §"Bridge-Landing Script Architecture"`.
>
> **Axis-B parallel cross-review sub-section** (dispatched separately to non-connes-ncg bridge-map reviewer; recommended mack-cosmic-bridge):
>
> 1. Receive Axis-A producing-script .npz output (read-only consumption).
> 2. Cross-check the FULL CM-1995 §III.4 residue formula evaluator against the canonical Connes-Moscovici 1995 paper §III.4 (verify the formula transcription is correct).
> 3. Cross-check the dimension spectrum poles extracted from the L_max=10 substrate spectrum (verify the poles are at expected substrate-distance pattern positions per S82+ Mellin pole structure).
> 4. Cross-check the χ'^* pullback differential machine-epsilon verification (verify dχ'^*φ_g^{sym} = 0 substrate-derivation cleanly closes; per S89 §W2-3 derived theorem).
> 5. If PASS: assess whether the FULL-CM1995 PASS supplies sufficient substrate-derivation provenance to support a §VII registry STAGE-1-CANDIDATE landing for the (d)∘(b) corridor as the canonical LRD α-anchor (mack-cosmic-bridge sole-writer authority per `feedback_mack-bridge-role.md`); pre-register routing if so.
> 6. Author cross-review sub-section in working paper §W3-4 §"Axis-B cross-review" (≥ 10 lines).
>
> **Verdict line** at `computations/session-91/s91_gate_verdicts.txt`:
>
> ```
> S91-CF37-FULL-CM1995-RESIDUE: PASS|FAIL -- value='alpha_prime_FULL_M_LRD=<v>;empirical_anchor=2.18341e-03;rel_dev=<r>;sub_A=<a>;sub_B=<b>;sub_C=<c>;composite=<comp>;chi_prime_weight_FULL=<g>;factor_vs_CF37=<f>;cf37_revision_status=FULL-CM1995-substrate-derivation-replaces-structural-ansatz;...' scheme=full-cm1995-§III.4-finite-spectral-triple-residue-formula convention=substrate-IS-Cell-I-K-counter-instance-2-FULL-CM1995-D-COMPOSE-B-NON-CONNES-NON-PHONON-FIRST-AUTHOR L_max=10 audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
> ```
>
> Companion dual-SHA row + (since `[SIGN]` trigger) 3-tuple annotation:
>
> ```
> # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # S91-CF37-FULL-CM1995-RESIDUE dual-SHA companion row (W9a-99 split)
> # sign_verdict=PASS|FAIL magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # S91-CF37-FULL-CM1995-RESIDUE 3-tuple annotation (S87 schema-v2)
> ```
>
> **Working paper section** at `sessions/archive/session-91/session-91-w3-workingpaper.md §W3-4`: ≥ 20 substantive lines per W4 CF-37 precedent. Sections: Status (top), Gate ID, Trigger, Classification, Agent (non-connes / non-phonon-first declaration + CM-1995 source-vs-evaluator clarification), Hypothesis, Plan reference, MCP Pre-Compute Audit, Verdict line + dual-SHA + 3-tuple, Results (4-tuple, χ'_weight_FULL back-computation + factor_vs_CF37, dimension-spectrum poles, residue evaluations per pole, sub-clause table, M-scan table, envelope fit, bot20_occupation, χ' anchor SHA, calibration-corpus instance status, CF-37 PROXY-REFINEMENT-PENDING revision status), Cross-checks performed (Axis-A self-checks; Axis-B parallel cross-review sub-section; verify CM-1995 §III.4 formula transcription; verify dimension-spectrum-pole structure; verify χ'^* pullback differential machine-epsilon = 0; assess §VII registry landing routing if PASS), Data files produced, Solution-space implication, Substrate framing reminder.

### 7. Machinery pin (PRDR)

| PRDR Element | Pin | Source |
|:-------------|:----|:-------|
| **Substrate spectrum cache** | `s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 | S84 master cache |
| **χ' inheritance morphism (element-3 (d))** | `s89_w2_a7_chi_prime_inheritance_morphism.npz` (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`) | S89 §W2-3 derived theorem |
| **Element-1 (b) χ'-pullback** | χ'^*[φ_g^{sym}] with machine-epsilon-verified d-closedness | S89 §W2-3 + CM-1995 §III.4 pullback machinery |
| **FULL CM-1995 §III.4 residue formula evaluator** | Full physical residue formula on finite spectral triple; NOT structural ansatz | Connes-Moscovici 1995 §III.4 source paper |
| **Dimension spectrum extraction** | From L_max=10 substrate eigenvalue spectrum + Peter-Weyl decomposition | S82+ Mellin pole structure |
| **Residue evaluator per pole** | Finite trace sum on Peter-Weyl-decomposed triple | CM-1995 §III.4 finite-spectral-triple-residue-formula |
| **R_universal_HP1_strict_F4 pin** | 1.030902 (Class-(d) PROVENANCE; PRIMARY canonical = eps_H_HP1_norm = 16.197719) — used for back-comparison; NOT pre-committed for the FULL evaluation | canonical_constants.py:250 |
| **eps_H_HP1_norm primary canonical** | 16.197719 | canonical_constants.py:171 |
| **M_KK, M_Pl_reduced canonical pins** | 7.428660e+16 GeV / 2.435e+18 GeV | canonical_constants.py:341 + CODATA 2018 |
| **L_max truncation** | L_max = 10 (matching S90 CF-37 truncation for direct comparability to PROXY-REFINEMENT-PENDING baseline) | S90 W4 CF-37 L_max pin |
| **bot20_occupation** | Substrate L=10 bot-20 sector occupation `{(0,0): 8, (0,1): 6, (1,0): 6}` total 20 ✓ | Per S90 W4 CF-37 §W4-1 *spectral content* table |
| **Sub-clause band thresholds** | A: 0 < α'_FULL < 1; B: rel_dev ≤ 0.30 RATIO; C: n > 0 AND R² ≥ 0.95 | S90 W4 CF-37 §W4-1 §9 thresholds (preserved) |
| **M-scan range** | M ∈ {10⁵, 10⁶, 10⁷, 10⁸, 10⁹} M_sun | S90 W4 CF-37 §W4-1 M-scan (preserved) |
| **Single-shot AFTER-pattern emission** | `registry-landing.md §"Bridge-Landing Script Architecture"` REQUIRED | Standard registry-landing script architecture |
| **Reviewer assignments** | Axis-A: van-den-dungen-bridge-theorist (recommended); Axis-B: mack-cosmic-bridge (recommended) — both NON-connes-ncg + NON-phonon-first | S91 context file §"W3" line 185-186 OAA exclusion |
| **Verdict file** | `computations/session-91/s91_gate_verdicts.txt` | `gate-verdicts.md §"Canonical Verdict-File Path"` |
| **Calibration-corpus instance status** | "instance_2_pending"; PASS advances K=1 → K=2 (instance #1 = §VII.AF.1.OP-PROJ W-5 baseline LANDED S87 W5-1) | `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` |
| **GPU usage** | Conditional — if Peter-Weyl block-diagonal eigenvalue extraction or residue per-pole trace-sum benefits from matrix ops on per-sector blocks (Largest single block at L_max=10 is sub-1000 dim per block-diagonal cache), CPU is adequate. If full-spectrum matrix products needed (not anticipated), use torch.linalg per `math-scripts.md §"Heavy Linear Algebra — Prefer GPU"`. | `computation-environment.md §"Heavy Linear Algebra — Prefer GPU"` |
| **Level-pin discipline (substrate-first-canonical-sourcing.md §(iv))** | This gate's evaluator IS the FULL physical residue formula (NOT SCHEMATIC). Per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 level-pin discipline (S88 W7b-83 promotion), CLASS pin = FULL; convention-tag suffix is `FULL-CM1995` (NOT `-SCHEMATIC`). | `substrate-first-canonical-sourcing.md §(iv)` MANDATORY |

### 8. Expected output 4-tuple

`(value='alpha_prime_FULL_M_LRD=<v>;empirical_anchor=2.18341e-03;rel_dev=<r>;sub_A=<a>;sub_B=<b>;sub_C=<c>;composite=<comp>;chi_prime_weight_FULL=<g>;factor_vs_CF37=<f>;cf37_revision_status=FULL-CM1995-substrate-derivation-replaces-structural-ansatz;...', scheme='full-cm1995-§III.4-finite-spectral-triple-residue-formula', convention='substrate-IS-Cell-I-K-counter-instance-2-FULL-CM1995-D-COMPOSE-B-NON-CONNES-NON-PHONON-FIRST-AUTHOR', L_max='10')`

### 9. PASS / FAIL / INFO thresholds

- **PASS** (composite): Sub-clause A PASS (0 < α'_FULL < 1) AND Sub-clause B PASS (rel_dev ≤ 0.30 RATIO) AND Sub-clause C PASS (envelope n > 0 + R² ≥ 0.95). The FULL CM-1995 §III.4 evaluation produces a χ'_weight_FULL factor ~4.5× larger than CF-37's structural-ansatz 0.5 (most likely χ'_weight_FULL ∈ [1.591, 2.953] to land α'_FULL in the 30% RATIO band); CF-37 PROXY-REFINEMENT-PENDING tag converts to FULL-CM1995-PASS; (d)∘(b) corridor RECOVERS as the canonical LRD α-anchor candidate with substrate-derived provenance. Calibration-corpus instance #2 LANDED at Cell-I simultaneous element-1+element-3 double-deformation pattern; Hybrid Independence Test K-counter advances K=1 → K=2 (W-5 baseline instance #1 = T1.9 PASS instance #2 via FULL substrate-derivation; structural axes of independence — evaluator-class differs from instance #1 (W-5 used substrate-internal structural identity at the cohomology-class layer; T1.9 uses FULL CM-1995 §III.4 residue formula evaluator)).

- **INFO**: Sub-clause A PASS AND Sub-clause B INFO (0.10 < rel_dev ≤ 0.30) AND Sub-clause C PASS, OR Sub-clause A PASS AND Sub-clause B PASS AND Sub-clause C INFO (envelope marginal). Identifies the FULL evaluation is structurally meaningful (closes the structural-ansatz CF-37 layer) but lands marginally on Sub-clause B or C; routes to S92+ for deeper inspection (e.g., M_LRD scan refinement, alternative substrate-distance pole choice).

- **FAIL** (composite): ANY ONE Sub-clause FAILs. The FULL CM-1995 §III.4 evaluation does NOT produce a χ'_weight ~4.5× larger than 0.5; (d)∘(b) corridor PERMANENTLY CLOSES at the FULL-CM1995 substrate-derivation layer (NOT just at PROXY-REFINEMENT-PENDING); the LRD α-anchor candidate is closed at (d)∘(b) regardless of further refinement. Routes to (i) T1.8 (c)∘(d) secondary corridor verdict adjudication (if T1.8 PASS, (c)∘(d) becomes canonical; if T1.8 FAIL, both substrate-distance-1 corridors closed); (ii) substrate-distance-2 §VII.AX forward gates at S91 W0 R5 landing.

### 10. Substitution chain (substrate-IS Cell-I cohomology-class direction; analogous to CF-37 §10 with FULL CM-1995 §III.4 residue evaluator substituted for structural-ansatz)

```
Step 1 (definition): φ_g^{sym} ∈ HH^1(A_K) gradient-symmetric Hochschild 1-cocycle on A_K = C ⊕ H ⊕ M_3(C); cohomology class [φ_g^{sym}] regulator-class INVARIANT (W-5 calibration corpus instance #1 anchor); χ': A_K → M_2(C) ⊗ Cl(1) inheritance morphism with ker(χ'|_{M_3(C)}) = M_3(C) entire (S89 §W2-3 derived theorem); P_HSS(M) = Peter-Weyl horizon-spanning projector at mass scale M.

Step 2 (pullback machine-epsilon verification): Compute χ'^*[φ_g^{sym}] pullback on H_K^{≤10}. Verify dχ'^*φ_g^{sym} = 0 explicitly via Python evaluation (NOT just structurally asserted as in CF-37); the d-closedness IS the substrate-IS Hochschild-cohomology identity at the χ'-pulled-back cocycle.

Step 3 (inheritance-restricted projector construction): P_HSS'(M) = χ'^*(P_HSS(M)) on the Peter-Weyl decomposition of (A_K, H_K, D_K)|_{L_max=10}. The cutoff form is DERIVED from the inheritance restriction: λ² ≤ <derived bound from χ' image structure on M_2(C) ⊗ Cl(1)> (NOT the naive λ² ≤ M_KK²·(M_LRD/M_KK²) used in CF-37 §W4-1 Step 5).

Step 4 (Chern character via residue formula): ch(P_HSS'(M_LRD)) = Σ_{k ∈ dim_spec((A_K, H_K, D_K)|_{L_max=10})} Res_{z=k}[Tr(P_HSS'(M_LRD) · D_K^{-2z})] · (pole at z = k). The dimension spectrum at L_max=10 is computed from the Peter-Weyl-decomposed eigenvalue spectrum.

Step 5 (Connes-Karoubi pairing as finite trace sum): α'_FULL(M_LRD) = ⟨χ'^*[φ_g^{sym}], [ch(P_HSS'(M_LRD))]⟩ = finite trace sum over residue products at the substrate-distance poles. NO multiplicative decomposition into R_universal · χ'_weight · (M_KK/M_Pl_reduced)² · g is pre-committed at the FULL evaluation layer; if the decomposition holds at the result layer, back-compute χ'_weight_FULL for direct comparison to CF-37's 0.5.

Step 6 (M-scan substrate saturation): g(M, L=10) = N_χ'_image / N_substrate at each M-scan point. SAME as CF-37 since element-3 (d) is identical: g(M_LRD, L=10) = 1.000 (Λ(M_LRD)/M_KK = 4.58e+45 ≫ |λ|_max(L=10) = 4.67; the L=10 substrate is fully spanned by P_HSS'(M_LRD)).

Step 7 (direction read-off): Sub-clause A (sign): 0 < α'_FULL(M_LRD) by Step 4 positivity of Chern character on positive idempotent + Step 5 Connes-Karoubi positivity on substrate-coherent regulator-class. α'_FULL(M_LRD) is bounded above by the saturation factor; if Sub-clause A's < 1 bound is checked numerically (gate's output verifies). MAGNITUDE adjudication is the substantive substrate-physics question (NOT pre-determined): if χ'_weight_FULL ∈ [1.591, 2.953] back-computed at the FULL evaluation, α'_FULL ∈ [1.527e-3, 2.836e-3] (Sub-clause B 30% PASS band); if χ'_weight_FULL ≈ 0.5 (matching CF-37's structural-ansatz), Sub-clause B FAILs (PROXY-REFINEMENT-PENDING confirms as permanent (d)∘(b) closure).
```

### 11. What PASSES / FAILS mean for solution space

- **PASS** (composite): the FULL CM-1995 §III.4 substrate-derivation produces a χ'_weight_FULL substantially different from CF-37's structural-ansatz 0.5; α'_FULL lands in the 30% RATIO band of 1/458; (d)∘(b) corridor RECOVERS as canonical LRD α-anchor candidate with substrate-derived provenance. Constraint-map advance:
  - CF-37 PROXY-REFINEMENT-PENDING tag CONVERTS to FULL-CM1995-PASS; the (d)∘(b) corridor's structural-ansatz layer was the SOLE source of the CF-37 FAIL, not the substrate physics.
  - Hybrid Independence Test K-counter advances K=1 → K=2 (simultaneous element-1+element-3 double-deformation pattern at Cell-I instance #2 LANDED).
  - Empirical anchor 1/458 PROMOTION candidate: T1.9 PASS supplies substrate-derived provenance for `alpha_LRD_FW` canonical_constants.py promotion (per CF-38 FAIL diagnostic at S90 W4).
  - Routes to S91+ AUX-5 three-axis Stage-2 cross-axis independent-verify (lizzi + volovik + mack; EXCLUDES connes-ncg + phonon-first per OAA).
  - §VII registry STAGE-1-CANDIDATE landing routing: mack-cosmic-bridge sole-writer authority per `feedback_mack-bridge-role.md` lands §VII.{next-free}.OP-PROJ entry citing T1.9 audit_sha256 as substrate-derivation provenance.
  - If BOTH T1.8 + T1.9 PASS: parallel admissibility — both (c)∘(d) and (d)∘(b)+FULL-CM-1995 land in 30% band; substrate intrinsic determinism becomes S92+ adjudication question (Two-Independent-Axes structure per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding"` Joint-hypersurface form).

- **INFO**: FULL evaluation is structurally meaningful (closes the structural-ansatz CF-37 layer cleanly) but Sub-clause B or C lands marginally; routes to S92+ for deeper inspection (e.g., M_LRD scan refinement; alternative substrate-distance pole choice).

- **FAIL** (composite): the FULL CM-1995 §III.4 substrate-derivation does NOT recover (d)∘(b) — χ'_weight_FULL ≈ 0.5 confirms CF-37's structural-ansatz at the substrate-derivation layer; (d)∘(b) corridor PERMANENTLY CLOSES at the FULL-CM1995 layer. Constraint-map advance:
  - The (d)∘(b) corridor closure converts from PROXY-REFINEMENT-PENDING to PERMANENT-CLOSURE (the FULL substrate-derivation IS the canonical evaluation; no further refinement available at this corridor).
  - The CF-37 PROXY-REFINEMENT-PENDING revision-pending caveat is RESOLVED (FAIL direction); the structural ansatz was correct at the substrate-physics layer, the (d)∘(b) corridor simply does NOT reproduce the empirical 1/458 anchor.
  - If T1.8 PASS: (c)∘(d) corridor becomes the canonical LRD α-anchor candidate; (d)∘(b) permanently closed.
  - If T1.8 also FAIL: both substrate-distance-1 corridors closed at FULL substrate-derivation layer; routes to substrate-distance-2 §VII.AX forward gates at S91 W0 R5 landing as the next candidate domain. The LRD α-anchor pursuit moves from substrate-distance-1 pole s = 1 to substrate-distance-2 pole s = 2.

### 12. Effort estimate

~3.5 wave-equivalents (matches CF-37's original effort estimate of ~3.5 we BIG; the FULL CM-1995 §III.4 residue formula evaluation IS the substantive computation that CF-37 deferred via the structural ansatz). Breakdown:
- ~1.5 we Axis-A primary computation: fork CF-37 producing script; implement FULL CM-1995 §III.4 residue formula evaluator (pullback + Chern character via residues + Connes-Karoubi pairing); extract dimension-spectrum poles from L_max=10 substrate; evaluate per-pole residues + finite trace sums; back-compute χ'_weight_FULL; run M-scan; sub-clause band tests; output npz + plot + JSON.
- ~1.0 we Axis-B parallel cross-review: CM-1995 §III.4 formula transcription cross-check; dimension-spectrum-pole structure cross-check; χ'^* pullback differential machine-epsilon verification; §VII registry landing pre-registration (if PASS); working paper cross-review sub-section.
- ~1.0 we orchestrator integration: dispatch coordination + verdict-line emission + working paper section authoring + carry-forward routing (W3 → W4/W5 decision-point map; potential §VII registry landing routing on PASS via mack-cosmic-bridge sole-writer).

### 13. Substrate-framing reminder

In the dispatch prompt §6 above, the explicit reminder reads: "the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the FULL Connes-Moscovici 1995 §III.4 residue formula evaluates the Chern character of the Peter-Weyl-decomposed inheritance-restricted projector P_HSS'(M) on the substrate's intrinsic algebra A_K = C ⊕ H ⊕ M_3(C); the Connes-Karoubi pairing IS the substrate's intrinsic structural identity at the algebra-axis orthogonality K=3 MANDATORY clause's algebra-INVARIANT spectrum-only functional family. Direction substrate (Cell-I cohomology class) → bridge map (residue formula + Chern character) → laboratory observable (α'(M_LRD) at LRD-scale M = 10⁷ M_sun). Do NOT frame the FULL-CM1995 evaluation as 'tuning the residue formula to match data'; the residue formula's value IS the substrate's structural prediction at the (d)∘(b) corridor, with NO numerical tuning available — the gate's substantive output IS that intrinsic value." This satisfies `phononic-framing.md §"IS Space, Not IN Space"` directional pre-registration AND `v3-closure-recovery.md §PROHIBITED_ACTIONS` Class 1 (convention-shopping is FORBIDDEN; the FULL residue formula has NO tunable parameters at the substrate-physics layer — the evaluator IS the substrate's canonical evaluation of the (d)∘(b) corridor) AND `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 level-pin discipline (CLASS = FULL; convention-tag suffix is `FULL-CM1995`, NOT `-SCHEMATIC`).

---

## Wave 3 → Wave 4 / Wave 5 Decision Point

The four W3 gate verdicts (T1.6, T1.7, T1.8, T1.9) produce the following outcome-routing map for downstream waves:

### Track A consequence map (species-multiplicity cascade)

| T1.6 verdict | T1.7 verdict | Downstream consequence |
|:-------------|:-------------|:------------------------|
| PASS / INFO | PASS | S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY chain SUPERSEDED at latest non-superseded canonical reading; g_star_BS_T_H_FW + T_H_FW canonical pins LANDED; species-multiplicity cascade CHAIN CLOSES; W4 / W5+ downstream consumers cite T1.7 corrective canonical line. |
| PASS / INFO | INFO | g_star_BS_T_H_FW LANDED with INFO sub-tag; S88 reading remains canonical at supersession-chain reading; W4/W5+ inherit INFO caveat; carry-forward to S92+ for deeper refinement (revisit A_horizon or T_H substrate-derivation). |
| PASS / INFO | FAIL substantive | g_star_BS_T_H_FW LANDED but L_H_canonical re-pinning FAILs; routes to S92+ as deeper cascade-form-or-anchor scrutiny carry-forward; S88 reading remains canonical. |
| FAIL | FAIL mechanical (PRE-REG-INC) | g_star_BS_T_H_FW NOT promoted; species-multiplicity cascade chain does NOT close at S91; carry-forward to S92+ for T1.6 retry with deeper species-multiplicity-form scrutiny (which Kolb-Turner kernel term + which SM species dominates the FAIL); S88 reading remains canonical. |

### Track B consequence map (LRD α-anchor parallel pathways)

| T1.8 verdict | T1.9 verdict | Downstream consequence |
|:-------------|:-------------|:------------------------|
| PASS | PASS | Parallel admissibility — both (c)∘(d) AND (d)∘(b)+FULL-CM-1995 land in 30% RATIO band of 1/458; substrate intrinsic determinism becomes S92+ adjudication question (Two-Independent-Axes structure per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding"` Joint-hypersurface form (iii)); routes to W4 / W5+ AUX-5 three-axis Stage-2 cross-axis verify (lizzi + volovik + mack; EXCLUDES connes + phonon-first per OAA); calibration-corpus advances K=1 → K=2 (instance #2 LANDED with TWO independent substrate-derivation pathways). |
| PASS | FAIL | (c)∘(d) secondary corridor becomes canonical LRD α-anchor candidate; (d)∘(b) PERMANENTLY CLOSED at FULL-CM-1995 substrate-derivation layer; routes to W4 / W5+ AUX-5 Stage-2 verify on (c)∘(d) PASS; calibration-corpus advances K=1 → K=2 (instance #2 = (c)∘(d) at T1.8 PASS). |
| FAIL | PASS | (d)∘(b) corridor RECOVERS via FULL-CM-1995 substrate-derivation (CF-37 PROXY-REFINEMENT-PENDING tag converts to FULL-CM1995-PASS); (c)∘(d) corridor closed; routes to W4 / W5+ AUX-5 Stage-2 verify on (d)∘(b) PASS; calibration-corpus advances K=1 → K=2 (instance #2 = (d)∘(b) at T1.9 PASS). |
| FAIL | FAIL | Both substrate-distance-1 corridors CLOSED at FULL substrate-derivation layer; LRD α-anchor pursuit moves from substrate-distance-1 pole s = 1 to substrate-distance-2 pole s = 2 via §VII.AX forward gates queued at S91 W0 R5 landing (THREE S91+ parallel pathways: T1.8 = AUX-4 substrate-distance-1 secondary [FAIL]; T1.9 = FULL-CM1995 substrate-distance-1 primary [FAIL]; §VII.AX = substrate-distance-2 under {ζ, PV, Mellin} regulator atlas [S91 W0 R5 LANDED; ready for W4+ dispatch]); calibration-corpus stays K=1 at substrate-distance-1; the §VII.AX forward gates become the next candidate domain at S91+. |

### Composite W3 wave consequence

W3 closes with a Track A verdict + a Track B verdict tuple ∈ {16 composite outcomes from T1.6 × T1.7 × T1.8 × T1.9}. The W3 wave-synthesis section in the working paper integrates the two tracks' consequences and routes carry-forwards to W4 (Stage-2 cross-axis verifies on PASS branches) + W5+ (substantive carry-forwards on FAIL or INFO branches) per `feedback_fix-in-session-never-defer.md` 4-field spec discipline. Note that the §VII.AX substrate-distance-2 forward gates (S91 W0 R5 LANDED at NEW §VII slot for option (v) pre-registration at CF-37 with sub-class tag REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT) remain STRUCTURALLY INDEPENDENT of the W3 verdicts — they fire at W4+ regardless of W3 Track B outcomes, per the S91 W0 in-session housekeeping campaign R5 landing.

---

## Wave 3 Machinery-Enumeration Pin (PRDR across 4 gates)

This table enumerates the structural machinery shared across W3 gates + the per-gate distinguishing pins. Per `epistemic-discipline.md §"Pre-Registration Completeness"`, each pinned parameter is verified at plan-freeze; missing pins trigger Class-8 PRU remediation.

| Machinery axis | T1.6 (CF-40) | T1.7 (CF-39) | T1.8 (CF-37 AUX-4) | T1.9 (CF-37 FULL CM-1995) |
|:---------------|:--------------|:--------------|:--------------------|:---------------------------|
| **Substrate spectrum cache** | N/A (thermal-distribution gate) | N/A | s84_spectrum_cache_L12_tau019.npz filtered L_max=10 | s84_spectrum_cache_L12_tau019.npz filtered L_max=10 |
| **χ' inheritance morphism** | N/A | N/A | s89_w2_a7 (audit_sha256 `90bba262af80a04c...`) | s89_w2_a7 (audit_sha256 `90bba262af80a04c...`) |
| **Element-1 deformation choice** | N/A | N/A | (c) modified-universal-kernel γ(s) ≠ Γ(s) | (b) χ'-pullback (CF-37 primary) |
| **Element-3 deformation choice** | N/A | N/A | (d) inheritance-restricted projector P_HSS'(M) | (d) inheritance-restricted projector P_HSS'(M) |
| **Residue formula evaluator** | scipy.integrate.quad on Kolb-Turner Eq.3.62 FD/BE integrated | π²/60 · g · A · T⁴ formula (S88 W6 §V.5) | Modified CM-1995 §III.4 with γ(s) kernel | FULL CM-1995 §III.4 with Γ(s) standard kernel |
| **Level pin (SCHEMATIC vs FULL)** | FULL — canonical Kolb-Turner integrated form | FULL — substrate cascade tail S88 W6 §V.5 | SCHEMATIC at γ_weight_aux candidate layer (3 candidates documented per substrate-derivation); convention-suffix `-SCHEMATIC` OR `-FULL` depending on whether candidate (3) full residue is implemented or candidate (1)/(2) structural-ansatz back-fallback | FULL — Connes-Moscovici 1995 §III.4 residue formula; convention-suffix `FULL-CM1995` |
| **L_max truncation** | N/A | N/A | 10 | 10 |
| **Sub-clause band thresholds** | rel_dev ≤ 0.10 PASS at 3 anchors | delta_log < 0.5 PASS + log_residual_improvement ≥ 1.0 | A: 0<α''<1; B: rel_dev ≤ 0.30; C: n>0 + R²≥0.95 | A: 0<α'_FULL<1; B: rel_dev ≤ 0.30; C: n>0 + R²≥0.95 |
| **Supersedes target full 64-char SHA** | N/A | `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` | N/A | N/A |
| **Calibration corpus instance status** | N/A | N/A | instance_2_pending (K=1 → K=2 on PASS) | instance_2_pending (K=1 → K=2 on PASS) |
| **OAA exclusion** | None | None | HARD: connes-ncg + phonon-first | HARD: connes-ncg + phonon-first |
| **Primary reviewer** | mack-cosmic-bridge | mack-cosmic-bridge | volovik (recommended) | van-den-dungen (recommended) |
| **Cross-review reviewer** | gen-physicist | (none — solo mechanical or substantive) | van-den-dungen (recommended) | mack-cosmic-bridge (recommended) |
| **GPU usage** | None | None | None | Conditional |
| **Verdict file path** | computations/session-91/s91_gate_verdicts.txt | (same) | (same) | (same) |
| **Single-shot AFTER-pattern emission** | Yes | Yes (PASS branch); mechanical closure (FAIL branch) | Yes | Yes |
| **Trigger annotations** | [VERIFY] ∧ [SIGN] | [VERIFY] ∧ [CHAIN] | [VERIFY-THEOREM] ∧ [SIGN] | [VERIFY-THEOREM] ∧ [SIGN] |

---

## Wave 3 Input-SHA Ledger

For each W3 gate, the producing-script input-SHA pin map at plan-freeze + dispatch time (per `gate-verdicts.md` S81+ closure-hash pin):

### T1.6 input-SHA pins

| File | Pin form |
|:-----|:---------|
| `computations/session-90/s90_w4_cf40_species_multiplicity_retry.py` (S90 fork source) | `<runtime SHA captured>` |
| `computations/_shared/canonical_constants.py` (g_star_SM, g_star_BBN pins) | `<runtime SHA>` |
| Kolb-Turner Eq.3.62 source paper reference | (not file-based; verbal source pin) |
| PDG 2024 SM masses (laboratory anchor) | (canonical_constants.py + PDG online reference) |
| Borsanyi 2016 lattice-QCD source (T=1 GeV crossover) | (verbal source pin; lizzi-s4-meta-p3-synthesis §1.3 cited) |

### T1.7 input-SHA pins (PASS branch)

| File | Pin form |
|:-----|:---------|
| `computations/session-91/s91_w3_cf40_kolb_turner_fd_be_integrated.npz` (T1.6 PASS output) | `<runtime SHA — T1.6 PASS prerequisite>` |
| `computations/_shared/canonical_constants.py` (g_star_BS_T_H_FW post-T1.6 promotion) | `<runtime SHA>` |
| S88 W6 §V.5 source (substrate cascade tail formula) | `<runtime SHA>` |
| S88 §W1c-69 reference baseline f(M_at_W1c69) | `<runtime SHA>` |
| `computations/session-88/s88_gate_verdicts.txt` line 34 (S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY canonical line; full 64-char supersedes target) | `<runtime grep verification>` |

### T1.7 input-SHA pins (FAIL mechanical branch)

| File | Pin form |
|:-----|:---------|
| `computations/session-91/s91_gate_verdicts.txt` (T1.6 FAIL canonical line; upstream-block topology cause) | `<runtime grep verification>` |
| `computations/session-90/s90_w4_cf39_mechanical_closure_blocked_by_cf40.py` (S90 mechanical-closure script fork source) | `<runtime SHA>` |

### T1.8 input-SHA pins

| File | Pin form |
|:-----|:---------|
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (S84 master cache, filtered L_max=10) | `<runtime SHA captured>` |
| `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz` | audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843` |
| `computations/_shared/canonical_constants.py` (M_KK, M_Pl_reduced, R_universal_HP1_strict_F4, eps_H_HP1_norm, tau_fold) | `<runtime SHA>` |
| `sessions/permanent-results-registry.md` (§VII.AF.1.OP-PROJ W-5 baseline; calibration-corpus instance #1) | `<runtime SHA>` |
| S90 W-1 workshop AUX-4 pre-registration source (γ(s) modified-universal-kernel specification) | `<runtime SHA>` |
| `computations/session-90/s90_w4_alpha_m_alt_corridor_d_compose_b.py` (S90 CF-37 fork source) | `<runtime SHA>` |

### T1.9 input-SHA pins

| File | Pin form |
|:-----|:---------|
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (S84 master cache, filtered L_max=10) | `<runtime SHA captured>` |
| `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz` | audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843` |
| `computations/_shared/canonical_constants.py` (M_KK, M_Pl_reduced, R_universal_HP1_strict_F4, eps_H_HP1_norm, tau_fold) | `<runtime SHA>` |
| `sessions/permanent-results-registry.md` (§VII.AF.1.OP-PROJ W-5 baseline; calibration-corpus instance #1) | `<runtime SHA>` |
| Connes-Moscovici 1995 §III.4 source paper (residue formula machinery; FIXED published source) | (verbal source pin; not file-based) |
| `computations/session-90/s90_w4_alpha_m_alt_corridor_d_compose_b.py` (S90 CF-37 fork source) | `<runtime SHA>` |

---

**End of Session 91 Plan — Wave 3.**

**Carry-forward summary**: 4 gates totaling ~8.5 wave-equivalents (T1.6 ~1.0 + T1.7 ~0.5 + T1.8 ~3.5 + T1.9 ~3.5). Two parallel STRUCTURALLY INDEPENDENT tracks: Track A (T1.6 → T1.7) species-multiplicity cascade led by mack-cosmic-bridge; Track B (T1.8 + T1.9) LRD α-anchor parallel evaluation under HARD OAA exclusion of connes-ncg + phonon-first (Axis-A from {volovik, van-den-dungen, gen-physicist}; Axis-B from {mack, landau, volovik}). Downstream consequences mapped at the W3 → W4 / W5 Decision Point. Substrate framing: all four gates evaluate substrate-IS observables on `(A_K, H_K, D_K(τ_fold))` — T1.6 + T1.7 at the substrate cascade-tail formula's laboratory-IN INPUT axis (g_*(T)) + structural-form bridge to laboratory cosmological-horizon observable (L_H_canonical); T1.8 + T1.9 at the substrate's Cell-I cohomology-class layer (Connes-Karoubi pairing on inheritance-restricted projector) with different element-1 deformation choices. Direction substrate → bridge map → laboratory observable, NOT inverse.
