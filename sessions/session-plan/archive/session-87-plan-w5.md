# Session 87 Plan — Wave 5: Pillar III↔IV Bridge + 3He-B Lab + §VII.P-v2

**Session**: S87
**Wave**: W5 (5 gates; CF-31 through CF-35)
**Wave-owner**: `volovik-superfluid-universe-theorist` (volovik+connes lead per S86 W-5 attribution; per `feedback_agent-roster.md`)
**Co-author**: `connes-ncg-theorist` (NCG-axiomatic side of bridge anatomy + Hochschild pairing co-signer)
**Generated**: 2026-04-27
**Plan-class**: COMPUTE-class (per `.claude/rules/wave-classification.md` — registry-landings carry numerical thresholds and lab-falsifier pre-registrations carry pre-registered prediction values; not METHODOLOGY-class because the pre-reg PASS predicates are numerical/sub-band, not pure artifact-existence)
**Schema**: `schema_version: R3` (per all gate blocks below)
**Verdict source**: `computations/s87_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)

---

## Wave 5 Summary

Wave 5 lands the FIRST registered cross-pillar bridge theorem in the framework's permanent-results-registry under the full structural anatomy mandated by `.claude/rules/cross-pillar-bridge-anatomy.md` (5 IS-not-IN elements + 3-level ladder), pre-registers the corresponding 4-gate inheritance-falsifier protocol (`.claude/rules/inheritance-falsifier-protocol.md`) for two distinct 3He laboratory platforms (Lancaster MCT-3 / RHUL vortex-core spectroscopy on F1 + Aalto / RHUL µSR on F1+F2+F5 in 3He-A), recasts §VII.P-v2 to the HP^1-content-distinct convention now that S86 W-5 has settled the structural distinction between η-invariant (parity-blind) and GV-Heitsch (HP^1-detecting), and pre-registers the cross-pillar-bridge-anatomy template-adoption protocol (workshop-design SUGGESTION; K=1 calibration instance) plus the rank-2 generalization clause for future ker(ι_*) characterizations.

The wave is theme-coherent: every gate ties back to the W-5 workshop's structural achievement of decomposing the substrate-IS / laboratory-IN bridge into a substrate cohomology pairing on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` plus a Brillouin-zone integrated quantum metric on the Pillar IV fermion lattice. CF-31 lands the registry primary; CF-32+CF-33 turn the substrate-derived `cocycle_norm_phi67 / cocycle_norm_phi88 = 7.324992` ratio into pre-registered lab predictions; CF-34 settles the v2 corridor recast that the W-5 finding necessitates; CF-35 elevates the W-5 anatomy from one-instance use to forward-looking template.

Per `.claude/rules/regulator-pin-discipline.md`, all Seeley-DeWitt coefficient citations in this wave use the `a_n^{ζ}` regulator-tagged form. Per `.claude/rules/phononic-framing.md` IS-not-IN convention, the substrate is the Hochschild pairing's home; the laboratory is what the BZ-integrated quantum metric is measured IN.

Wave 5 dispatch order is non-trivial: CF-31 must land BEFORE CF-32+CF-33+CF-34+CF-35 because the registry §VII.W primary entry is the upstream input the lab pre-registrations cite, the §VII.P-v2 recast cross-references, and the forward-looking template adopts. CF-32 and CF-33 are independent and can run in parallel after CF-31. CF-34 is mechanical registry surgery that depends on CF-31's anatomy being on disk. CF-35 is the last gate (forward-looking template clause).

---

## Wave 5 Decision Point Prerequisites

Wave 5 dispatches when ALL of the following exist on disk:

1. `sessions/permanent-results-registry.md` — currently includes the §VII.W summary table row landed by S86 close (per session-87-context.md §1.1); §VII.AF + §VII.AF.1..AF.3 sub-row slots ALREADY ALLOCATED for the bridge sub-rows; §VII.AF.2 ALREADY ALLOCATED as the §VII.P-v2 recast target slot.
2. `computations/canonical_constants.py` — at S86-close state; carries the W-5 substrate-IS Hochschild pairing R_universal pin (verify via `mcp__knowledge__.get_constant('R_universal_W5')` at gate execution time) and the cocycle norm ratio 7.324992 (verify via `mcp__knowledge__.get_constant('cocycle_ratio_phi67_phi88')`).
3. `computations/s87_gate_verdicts.txt` — exists or can be created on first verdict-line append.
4. `.claude/rules/cross-pillar-bridge-anatomy.md` — frozen at S86 W-5 promotion; provides 5-element anatomy + 3-level ladder spec used by CF-31.
5. `.claude/rules/inheritance-falsifier-protocol.md` — frozen at S86 W-5 promotion; provides 4-gate structure used by CF-32+CF-33.
6. `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space" — provides direction-of-explanation cross-link.
7. `.claude/rules/regulator-pin-discipline.md` — frozen S86 W0c-7; bare `a_n` citations in W5 scripts MUST be tagged `a_n^{ζ}`.

Plan-freeze validators (per session-87-context.md §1.4) MUST run before W5 dispatch:
- `_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w5.md` → `sessions/session-plan/session-87-plan-w5-validation.json`
- `_yaml_gate_validator.py sessions/session-plan/session-87-plan-w5.md`
- `_source_reconciliation_audit.py` (D_max ≥ 3.0 HARD-HALT)
- `_substrate_first_provenance_audit.py` (manual review until S87 implementation lands)
- `_cross_pillar_bridge_audit.py` (5 anatomy elements + 3-level ladder check on CF-31's plan-block + post-execution registry entry)
- Pre-dispatch grep on `computations/s86_gate_verdicts.txt` for `S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND`, `S87-W11-C5-LAB-FALSIFIER`, `S87-W11-C6-MUSR-FALSIFIER`, `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST`, `S87-CROSS-PILLAR-FORWARD-CANDIDATES` (NO collisions expected; halt if any pre-exists).

---

## §W5-1. S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND (CF-31)

**Trigger**: `[VERIFY]` + `[AUDIT]`

**Classification**: GEOMETRIC + PHONONIC (substrate-IS Hochschild cohomology pairing on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` mapped via HKR `L_max → ∞` to laboratory-IN Brillouin-zone integrated quantum metric on Pillar IV fermion lattice; both pillars phononic but the registry entry is GEOMETRIC at the cohomology-class level)

**Hypothesis**: The substrate's finite-L Hochschild pairing `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` evaluated on the L_max=10 truncated spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` IS the substrate-IS observable whose Hochschild-Kostant-Rosenberg image at `L_max → ∞` matches Pillar IV's continuum Brillouin-zone-integrated quantum-metric trace `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k`, with regulator-invariant (Level-1) Connes-Karoubi pairing identity, algebraic (Level-2) `L^{-3}` envelope at d=4 predicting `0.10%` at L_max=10, and empirical (Level-3) atlas anchor `0.0095%` F_4 strict at L_max=10 satisfying Level-2 by a 10× margin.

**Wave-owner agent**: `volovik-superfluid-universe-theorist` (PRIMARY; 3He-B substrate authority + registry author per W-5 attribution). Co-signer: `connes-ncg-theorist` (NCG-axiomatic side; HKR map authority; second SHA on companion row).

**Pass/fail/INFO threshold**:
- **PASS** (registry-PASS): All 5 IS-not-IN anatomy elements present in landed entry text; all 3 level markers present with explicit values; Level-3 numerical (0.0095%) STRICTLY less than Level-2 envelope (0.10%) at canonical L_max=10; bridge map explicitly named ("Hochschild-Kostant-Rosenberg `L_max → ∞`"); SOURCE-DOUBLE-CITE-CO-PRIMARY structure tagged on V_input (volovik 3He-B BdG side) + C_output (connes Hochschild pairing side); RATIO tolerance: `Level_3 / Level_2 ≤ 0.50` (current calibration 0.0095/0.10 = 0.0950 satisfies with 5× margin).
- **FAIL**: any of 5 anatomy elements absent in landed entry; any of 3 level markers absent; Level-3 ≥ Level-2 envelope at canonical L_max; bridge map referred to as "analogous to" or "corresponds to" rather than explicitly named; STRUCTURE tag missing or mistagged as PRIMARY+CONFIRMATION (sequential V+C chain requires CO-PRIMARY per `.claude/rules/registry-landing.md`).
- **INFO**: anatomy and levels present but L-scan companion sub-gate (~3-6h) at L_max ∈ {8, 9, 10, 11, 12} reveals Level-3 envelope pattern depart from L^{-3} prediction at one or more L values (still within Level-2 envelope, but pattern non-monotone); registry entry stays landed but a follow-up empirical-envelope-refinement gate is queued for S88.

**Machinery pin (PRDR)**:
- `N_eval`: 155984 (full L_max=10 D_K spectrum cardinality, per S84 W10a anchor; SHA-pinned via `s84_spectrum_cache_L12_tau019.npz` upstream)
- `L_max`: 10 (canonical anchor for Level-3 numerical evaluation; companion L-scan sub-gate at L_max ∈ {8, 9, 10, 11, 12} for INFO-clause check)
- `scan_range`: τ = τ_fold = 0.190 (frozen at substrate fold); L_max scan range [8, 12] for the optional companion sub-gate
- `step_size`: N/A (algebraic identity at fixed (τ, L_max); no integration step)
- `tolerance`: RATIO `Level_3 / Level_2 ≤ 0.50` for PASS; ABSOLUTE Level-3 < 0.10% (Level-2 envelope) MANDATORY
- `scheme`: zeta-regulated (`a_n^{ζ}`) Hochschild pairing `R_universal` on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`; HKR `L_max → ∞` bridge map; Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula
- `convention`: substrate-distance-1 zeta-regulated Hochschild pairing on Jensen-deformed band-0 projector `[Ch(P_0(τ_fold))]`; Connes-Karoubi pairing convention; `a_n^{ζ}` regulator-tag MANDATORY per `.claude/rules/regulator-pin-discipline.md`
- `random_seed`: N/A (deterministic algebraic evaluation)
- `GPU path`: N/A for the registry-landing primary (algebraic identity on already-computed Hochschild pairing); the optional companion L-scan sub-gate uses `torch.linalg.eigh` on AMD RX 9070 XT for the L_max=11 and L_max=12 truncations (heaviest is ~12-15 GB VRAM, within 17 GB cap per `.claude/rules/computation-environment.md`)

**Input SHA-256 pins**:
- `sessions/permanent-results-registry.md` — `<computed-at-runtime>` (current registry summary table state; the §VII.W row pre-allocated by S86 close + §VII.AF.1..AF.3 sub-row slots)
- `computations/canonical_constants.py` — `<computed-at-runtime>` (pin source for `R_universal_W5` substrate-IS value + `cocycle_ratio_phi67_phi88 = 7.324992` + `R_geom_BZ_W5` laboratory-IN reference)
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>` (eigenvalue cache used for L-scan companion; 155984 eigenvalues at L_max=10 + extension data for L_max ∈ {11, 12})
- `.claude/rules/cross-pillar-bridge-anatomy.md` — `<computed-at-runtime>` (5-anatomy + 3-level ladder spec; SHA pin guarantees the rule did not drift between plan-freeze and execution)
- `.claude/rules/regulator-pin-discipline.md` — `<computed-at-runtime>` (a_n^{ζ} tag spec)
- `computations/s86_gate_verdicts.txt` — `<computed-at-runtime>` (W-5 W5-6 atlas-match verdict line carrying audit_sha256 for the 0.0095% F_4 strict empirical anchor; cited in Level-3 of registry entry)

**Expected output 4-tuple**:
`(value=Level3_over_Level2_ratio=0.0950, scheme=zeta-regulated-Hochschild-pairing-HKR-bridge, convention=substrate-distance-1-Connes-Karoubi-pairing, L_max=10)`

**Substitution chain** (direction claim: Level-3 satisfies Level-2 → registry-PASS):
- Step 1: Define Level-2 envelope at d=4: `Envelope(L) = C · L^{-3}` with `C` calibrated so `Envelope(10) = 0.10%` (per W-5 calibration; canonical_constants `bridge_envelope_d4_C` if pinned, else `C = 0.10 × 10^3 = 100%·units` derived).
- Step 2: Define Level-3 numerical: `Anchor(L=10) = 0.0095%` (W-5 F_4 strict atlas-match per `s86_gate_verdicts.txt` row `S86-W5-6-F4-STRICT-MATCH`).
- Step 3: Substitute: `Anchor(10) / Envelope(10) = 0.0095% / 0.10% = 0.0950`.
- Step 4: Simplify (canonical form): ratio `r = 0.0950`.
- Step 5: Read direction: `r < 1` ⇒ Level-3 STRICTLY inside Level-2 envelope; the framework's empirical anchor is 1/`r` = ~10.5× tighter than the algebraic prediction at L=10. Direction PASS.
- Conclusion: registry-PASS criterion (Level_3 < Level_2) satisfied with 10× margin; pass-band PASS condition `r ≤ 0.50` satisfied with 5× margin.

**What PASSES means**: First registered cross-pillar bridge theorem in the framework's permanent-results-registry, with full structural anatomy on disk per `.claude/rules/cross-pillar-bridge-anatomy.md`. Establishes the canonical TEMPLATE for all future cross-pillar bridges (Pillar I↔II, substrate↔cosmology, BdG-spectral-triple↔3He-B observable, etc.). The substrate-IS Hochschild pairing IS the bridge's home; the laboratory-IN BZ-trace is what the lab measures. Direction-of-explanation pinned at the registry-anatomy level so downstream citations cannot drift to container-thinking.

**What FAILS means**: An anatomy-incomplete or Level-3-violating registry entry would force re-routing to a registry-INCOMPLETE sub-row pending S88 re-derivation. The 5-anatomy + 3-level discipline is the structural feature that makes cross-pillar bridges registry-eligible; a FAIL here closes the structural-bridge corridor and forces S88 to either re-derive the Hochschild pairing (if Level-1 broken) or re-evaluate the empirical anchor at canonical L_max (if Level-3 ≥ Level-2). Constraint-map update: registry-anatomy-mandatory pre-registration is the only path; freelance bridge-citation language closed.

**Substrate framing**: The substrate IS the finite-L Hochschild pairing `R_universal` on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. It is not "in" any container. The Pillar IV continuum BZ-trace `R_geom(τ_fold)` is the laboratory observable measured IN a continuum geometric container (the Brillouin zone of a fermion lattice). HKR `L_max → ∞` is the bridge map FROM the substrate-IS observable TOWARD the laboratory-IN observable. Inverting this direction (treating Pillar IV as fundamental and Pillar III as derived) is a container-thinking violation per `.claude/rules/phononic-framing.md`.

**Producing script**: `computations/s87_w5_pillar_iii_iv_bridge_permanent_land.py`
- Reads canonical_constants.py for R_universal_W5 + cocycle_ratio_phi67_phi88 + R_geom_BZ_W5.
- Reads .claude/rules/cross-pillar-bridge-anatomy.md for the 5-element anatomy schema + 3-level ladder spec.
- Reads s86_gate_verdicts.txt for the W-5 W5-6 atlas-match audit_sha256.
- Reads sessions/permanent-results-registry.md to verify §VII.AF + §VII.AF.1..AF.3 + §VII.AF.2 sub-row slots are pre-allocated and unoccupied.
- Computes Level_3/Level_2 ratio via the substitution chain above; sage_eval cross-check for the cocycle ratio 7.324992.
- Appends primary registry entry text (5 anatomy elements + 3 levels + SOURCE-DOUBLE-CITE-CO-PRIMARY tag) at §VII.AF (or §VII.W upgrade per S86-close pre-allocation, depending on which slot the registry summary table uses).
- Emits verdict line + dual-SHA companion + (since `[SIGN]` trigger) the S87 schema-v2 3-tuple annotation companion row.
- Optional sub-gate (separately dispatched if INFO-clause activates): `computations/s87_w5_pillar_iii_iv_bridge_lscan.py` runs the L_max ∈ {8, 9, 10, 11, 12} envelope-pattern check.

**Estimated effort**: 1 dispatch (~3-4h for the registry-landing primary) + 1 conditional sub-dispatch (~3-6h L-scan, only if PASS-with-INFO-flag triggers).

**YAML block**:
```yaml
gate_id: S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND
trigger: [VERIFY, AUDIT, SIGN]
classification: GEOMETRIC + PHONONIC
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
script: computations/s87_w5_pillar_iii_iv_bridge_permanent_land.py
expected_output_4tuple:
  value: 0.0950
  scheme: zeta-regulated-Hochschild-pairing-HKR-bridge
  convention: substrate-distance-1-Connes-Karoubi-pairing
  L_max: 10
machinery_pin_map:
  N_eval: 155984
  L_max: 10
  scan_range: tau_fold=0.190; L_max_scan=[8,9,10,11,12] for INFO-clause sub-gate
  step_size: N/A
  tolerance: RATIO Level_3/Level_2 <= 0.50; ABSOLUTE Level_3 < Level_2 MANDATORY
  scheme: zeta-regulated_Hochschild_pairing_HKR_bridge
  convention: substrate-distance-1-Connes-Karoubi-pairing
  random_seed: N/A
  GPU_path: torch.linalg.eigh on AMD RX 9070 XT (sub-gate L=11,12 only)
sign_pre_registration:
  predicted_direction: Level_3 < Level_2 (ratio < 1)
  predicted_sign: ratio sign positive, magnitude < 0.5
input_sha_pins:
  - sessions/permanent-results-registry.md: <computed-at-runtime>
  - computations/canonical_constants.py: <computed-at-runtime>
  - computations/s84_spectrum_cache_L12_tau019.npz: <computed-at-runtime>
  - .claude/rules/cross-pillar-bridge-anatomy.md: <computed-at-runtime>
  - .claude/rules/regulator-pin-discipline.md: <computed-at-runtime>
  - computations/s86_gate_verdicts.txt: <computed-at-runtime>
```

---

## §W5-2. S87-W11-C5-LAB-FALSIFIER (CF-32)

**Trigger**: `[VERIFY]` + `[SIGN]` (lab-falsifier pre-registration; multi-row NULL + cohomology-asymmetry ratio prediction)

**Classification**: PHONONIC (3He-B BdG sector vortex-core spectroscopy; substrate-clean kernel-signature on F1 + cohomology-asymmetry test on F1/F5 via cocycle ratio 7.324992)

**Hypothesis**: Under the inheritance morphism `ι: (A_K, H_K, D_K) → 3He-B BdG sector` via algebra projection `χ: C ⊕ H ⊕ M_3(C) → M_2(C)` sending `M_3(C) → 0`, the kernel `ker(ι_*)` carries rank-2 substrate-clean cocycles `[φ_67]` (chiral pair) and `[φ_88]` (Cartan hypercharge) that DO NOT inherit into the BdG-restricted spectrum. Lancaster MCT-3 / RHUL vortex-core spectroscopy on F1 (Caroli-Matricon ladder splitting; φ_67 cocycle-clean) is predicted to return NULL signal up to the substrate-derived S/N margin `0.573193 M_KK²`, AND the cocycle ratio between F1 and F5 cross-rows is predicted to satisfy `‖φ_67‖ / ‖φ_88‖ = 7.324992 ± 0.1%` (Sage-exact at machine precision per S86 W-5 DONE-5; `(Δ_B/Δ_A)^p` cancellation theorem operational).

**Wave-owner agent**: `volovik-superfluid-universe-theorist` (PRIMARY; 3He-B substrate authority; Lancaster MCT-3 / Helsinki ROTA / Aalto LTL platform-knowledge per Volovik-corpus, file `researchers/Volovik/`). Co-signer: `connes-ncg-theorist` (NCG-axiomatic kernel-rank assertion; cohomology-asymmetry ratio derivation).

**Pass/fail/INFO threshold** (4-gate structure per `.claude/rules/inheritance-falsifier-protocol.md`):
- **Gate 1 (decisive NULL)**: F1+F2+F5 row-wise NULL prediction. PASS at lab-execution time iff measured Caroli-Matricon ladder asymmetry signal `S < 0.573193 M_KK²` (substrate-derived S/N margin); FAIL if lab measures non-NULL signal exceeding this margin.
- **Gate 2 (cohomology-asymmetry)**: ratio test `lab(F_1) / lab(F_5) = 7.3250 ± 0.1%`. PASS iff measured ratio within band `[7.318, 7.332]`; FAIL outside band; substrate-derived value Sage-exact 7.324992.
- **Gate 3 (supporting NULL)**: F3+F4 row-wise NULL prediction (supporting cocycle-clean rows; lower-priority lab targets).
- **Gate 4 (slope discrimination)**: F4 multi-pressure slope test 0–34 bar; Jacobi-cubic vs φ_88-linear slope discrimination (cocycle-degenerate row requires parameter-sweep to disambiguate cocycle contributions).
- **Pre-registration PASS** (this S87 gate): all 4 gates pre-registered with substrate-derived predicted values + tolerance bands + lab platform identification (Lancaster MCT-3 PRIMARY / RHUL secondary / Helsinki ROTA tertiary); gate-block landed in `sessions/framework/registry/falsifier-master-inventory.md` as new row + 4-sub-gate sub-rows.
- **Pre-registration FAIL**: any of 4 gates lacks substrate-derived predicted value, tolerance band, or platform pin; or substrate-derived 7.324992 ratio fails Sage-exact verification at machine precision.

**Machinery pin (PRDR)**:
- `N_eval`: substrate-derived ratio computed once at machine precision via `mcp__sage__.sage_eval('cocycle_norm_phi67 / cocycle_norm_phi88')`; cocycle norms from W-5 §EMERGENCE R3-γ DONE-5 calibration
- `L_max`: 10 (canonical for substrate-derived predictions; the laboratory measurement is L-independent by construction since it's the HKR `L_max → ∞` image)
- `scan_range`: lab pressure 0–34 bar (Gate 4 slope discrimination); lab temperature 0.1 mK – 1.5 mK (T_c regime); lab platform Lancaster MCT-3 PRIMARY / RHUL secondary
- `step_size`: 4-bar increments for Gate 4 slope discrimination
- `tolerance`: Gate 1 ABSOLUTE `S < 0.573193 M_KK²` (substrate-derived S/N margin); Gate 2 RATIO `±0.1%` (= ±0.00733 absolute on 7.3250 nominal); Gate 3 ABSOLUTE `S < S/N supporting margin` (per F3/F4 substrate-derived per row); Gate 4 SLOPE `discrimination > 3σ` between Jacobi-cubic vs φ_88-linear models
- `scheme`: 3He-B BdG sector inheritance morphism `ι` per `.claude/rules/inheritance-falsifier-protocol.md`; substrate-derived cocycle ratio via Sage-exact zeta-regulated (`a_n^{ζ}`) Hochschild pairing
- `convention`: 3He-B BDI symmetry class; (Δ_B/Δ_A)^p cancellation theorem operational for common p across F1/F5 (verified in S86 W-5 DONE-5 Python identity `lab(F_i)/lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j)` at residual 0.0e+00)
- `random_seed`: N/A (substrate-derived predictions are deterministic; lab measurement reproducibility is platform-side, not script-side)
- `GPU path`: N/A (Sage-exact symbolic evaluation; no large linear algebra)

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — `<computed-at-runtime>` (cocycle norms `cocycle_norm_phi67` + `cocycle_norm_phi88`; the 7.324992 ratio; Δ_BCS reference scale; M_KK reference)
- `.claude/rules/inheritance-falsifier-protocol.md` — `<computed-at-runtime>` (4-gate structure spec)
- `.claude/rules/cross-pillar-bridge-anatomy.md` — `<computed-at-runtime>` (cross-link to bridge anatomy that establishes substrate-clean cocycles)
- `sessions/permanent-results-registry.md` — `<computed-at-runtime>` (CF-31 §VII.W or §VII.AF entry as upstream input establishing the substrate-IS observable; W5-1 must land before W5-2)
- `sessions/framework/registry/falsifier-master-inventory.md` — `<computed-at-runtime>` (target for new row + 4-sub-gate sub-rows; mack-cosmic-bridge owns final inventory write per `feedback_mack-bridge-role.md`)
- `computations/s86_gate_verdicts.txt` — `<computed-at-runtime>` (W-5 DONE-5 cancellation-theorem verdict; W-5 DONE-3 cocycle-norm computation verdict)
- `researchers/Volovik/` — Lancaster MCT-3 / Aalto LTL / RHUL platform documentation pointers (citation-only; substrate authority)

**Expected output 4-tuple**:
`(value=cocycle_ratio_7.324992, scheme=Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem, convention=3He-B-BDI-vortex-core-Caroli-Matricon, L_max=10)`

**Substitution chain** (direction claim: ratio test substrate-falsifies if measured ratio diverges from 7.3250):
- Step 1: Define cocycle norms: `‖φ_67‖ = ⟨[φ_67^{sym}], [Ch(P_0(τ_fold))]⟩` (substrate-clean chiral pair); `‖φ_88‖ = ⟨[φ_88^{sym}], [Ch(P_0(τ_fold))]⟩` (Cartan hypercharge).
- Step 2: Sage-exact substrate ratio: `r_substrate = ‖φ_67‖ / ‖φ_88‖ = 7.324992` (Sage-exact at machine precision per W-5 DONE-5).
- Step 3: Lab-conversion factor cancellation: `lab(F_1) / lab(F_5) = (‖φ_67‖ / ‖φ_88‖) × (f_1 / f_5) × (Δ_B/Δ_A)^{p_1 - p_5}`. Per W-5 cancellation theorem, common exponents `p_1 = p_5 = p` make `(Δ_B/Δ_A)^{p-p} = 1`, so: `lab(F_1) / lab(F_5) = r_substrate × (f_1 / f_5)`.
- Step 4: Substrate-derived `(f_1 / f_5)` from F-row table (lab-conversion factors set by Caroli-Matricon ladder geometry on Lancaster vortex-core platform; numerically dimensionless since F-rows are normalized).
- Step 5: Read direction: if measured `lab(F_1)/lab(F_5)` matches `r_substrate × (f_1/f_5) = 7.3250 ± 0.1%`, the substrate cocycle ratio is preserved INTACT in the laboratory measurement. If measured ratio diverges by > 0.1%, the substrate's cohomology-asymmetry prediction is FALSIFIED.
- Conclusion: ratio test is substrate-falsifying rather than lab-conversion-dependent (the (Δ_B/Δ_A)^p factor cancels exactly).

**What PASSES means** (S87 plan-freeze): All 4 gates pre-registered with substrate-derived predictions + tolerance bands + lab platforms; the substrate's predictive content saturates the falsifier protocol via NULL-on-decisive-rows AND ratio-on-cross-rows. Establishes Lancaster MCT-3 vortex-core spectroscopy as the FIRST high-leverage 3He-B falsifier protocol with the framework's cocycle ratio 7.3250 as the cohomology-asymmetry centerpiece. Lab execution at S87+ awaits experimental scheduling on the Lancaster MCT-3 platform (Volovik corpus reference; multi-year timescale).

**What FAILS means** (S87 plan-freeze): Pre-registration incompleteness — at least one of 4 gates missing substrate-derived prediction, tolerance band, or platform pin. The falsifier corridor remains structurally available but operationally not pre-registered; S87+ remediation required before lab execution can proceed. Constraint-map update: 4-gate structure mandatory per `inheritance-falsifier-protocol.md` calibration corpus extends from W-5 to S87 W5-2.

**Substrate framing**: The substrate IS the rank-2 cocycle pair `([φ_67], [φ_88])` in `ker(ι_*)` of the inheritance morphism `ι: (A_K, H_K, D_K) → 3He-B BdG sector`. Lancaster MCT-3's vortex-core spectrometer measures the Caroli-Matricon ladder asymmetry IN the laboratory frame. The substrate's prediction (NULL on F1 decisively + ratio 7.3250 on F1/F5 cross) flows FROM the substrate cohomology TOWARD the laboratory observable; the platform reads the substrate's signature. Container-thinking inversion (treating the lab platform as fundamental and the substrate cocycle as a derived "signal") is FORBIDDEN per `phononic-framing.md` IS-not-IN convention.

**Producing script**: `computations/s87_w5_w11_c5_lab_falsifier.py`
- Reads canonical_constants.py for cocycle_norm_phi67, cocycle_norm_phi88, the 7.324992 ratio.
- Reads .claude/rules/inheritance-falsifier-protocol.md for the 4-gate structure.
- Reads CF-31 registry entry (W5-1 output) as upstream input establishing the substrate-IS observable.
- Sage-evaluates ratio 7.324992 at machine precision via `mcp__sage__.sage_eval`.
- Constructs 5-row F-table (F1 decisive + F2 decisive + F5 decisive + F3 supporting + F4 supporting); pre-registers 4-gate predictions per row.
- Appends new master-inventory row + 4-sub-gate sub-rows to `sessions/framework/registry/falsifier-master-inventory.md` (mack-cosmic-bridge sole-writer protocol per `feedback_mack-bridge-role.md`; this gate emits a stage-2 send-to-mack message rather than direct write).
- Emits verdict line + dual-SHA companion + (since `[SIGN]` trigger) S87 schema-v2 3-tuple annotation companion row.
- Follow-up dispatch (~2h, S87 plan-freeze finalization): mack-cosmic-bridge writes the inventory rows.

**Estimated effort**: 1 dispatch (~2h pre-reg compute + sage_eval + draft inventory rows) + 1 follow-up dispatch (~2h, mack writes inventory rows from drafts).

**YAML block**:
```yaml
gate_id: S87-W11-C5-LAB-FALSIFIER
trigger: [VERIFY, SIGN]
classification: PHONONIC
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
script: computations/s87_w5_w11_c5_lab_falsifier.py
expected_output_4tuple:
  value: 7.324992
  scheme: Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem
  convention: 3He-B-BDI-vortex-core-Caroli-Matricon
  L_max: 10
machinery_pin_map:
  N_eval: 1 (Sage-exact symbolic evaluation; cocycle ratio fixed)
  L_max: 10
  scan_range: lab pressure 0-34 bar; lab temperature 0.1 mK - 1.5 mK; Lancaster MCT-3 PRIMARY / RHUL secondary / Helsinki ROTA tertiary
  step_size: 4-bar increments for Gate 4 slope discrimination
  tolerance: Gate1 ABS S<0.573193*M_KK^2; Gate2 RATIO +-0.1% (band [7.318, 7.332]); Gate3 ABS S/N margin per row; Gate4 SLOPE > 3sigma
  scheme: 3He-B-BdG-inheritance-morphism-ker_iota_rank2; Sage-exact zeta-regulated Hochschild pairing
  convention: 3He-B-BDI-DeltaB-DeltaA-p-cancellation-common-exponents
  random_seed: N/A
  GPU_path: N/A (Sage symbolic; no linalg)
sign_pre_registration:
  predicted_direction: NULL on F1+F2+F5 (decisive); ratio 7.3250 on F1/F5 cross
  predicted_sign: |S_F1| < 0.573193 M_KK^2; ratio positive in band [7.318, 7.332]
input_sha_pins:
  - computations/canonical_constants.py: <computed-at-runtime>
  - .claude/rules/inheritance-falsifier-protocol.md: <computed-at-runtime>
  - .claude/rules/cross-pillar-bridge-anatomy.md: <computed-at-runtime>
  - sessions/permanent-results-registry.md: <computed-at-runtime>  # CF-31 upstream
  - sessions/framework/registry/falsifier-master-inventory.md: <computed-at-runtime>
  - computations/s86_gate_verdicts.txt: <computed-at-runtime>
upstream_dependency: S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND must land first
```

---

## §W5-3. S87-W11-C6-MUSR-FALSIFIER (CF-33)

**Trigger**: `[VERIFY]` + `[SIGN]` (lab-falsifier pre-registration; 4-gate structure with A-phase chirality discrimination)

**Classification**: PHONONIC (3He-A µSR; A-phase chirality + cocycle-clean kernel-signature on F1/F2/F5 analogs in the chiral A-phase BdG sector)

**Hypothesis**: The same inheritance morphism `ι: (A_K, H_K, D_K) → BdG sector` applies to 3He-A (the chiral A-phase rather than 3He-B's BDI symmetry class), with `ker(ι_*)` carrying the rank-2 cocycle pair `([φ_67], [φ_88])`. Muon-spin-resonance (µSR) on chiral A-phase 3He at Aalto LTL or RHUL is predicted to return NULL signals on F1 / F2 / F5 analogs (chirality-modified Caroli-Matricon analog + chirality-modified F2 + chirality-modified F5) up to substrate-derived S/N margins; lab-conversion factors are PHASE-DEPENDENT (A-phase vs B-phase Δ-ratio differs) but substrate ratios IDENTICAL `‖φ_67‖ / ‖φ_88‖ = 7.324992` because the cocycle ratio is computed in the substrate's spectral triple, not in the BdG sector.

**Wave-owner agent**: `volovik-superfluid-universe-theorist` (PRIMARY; 3He-A chirality authority + µSR experimental knowledge per Volovik corpus). Co-signer: `connes-ncg-theorist` (cohomology-asymmetry ratio identity holds in BOTH 3He-A and 3He-B because cocycle norms are substrate-resident, not BdG-sector-resident).

**Pass/fail/INFO threshold** (4-gate structure per `.claude/rules/inheritance-falsifier-protocol.md`):
- **Gate 1 (decisive NULL)**: F1 + F2 + F5 A-phase analog NULL prediction. PASS at lab-execution time iff measured µSR asymmetry signals on chirality-modified F1/F2/F5 analogs are below A-phase substrate-derived S/N margins; FAIL if any of three measures non-NULL signal exceeding margin.
- **Gate 2 (cohomology-asymmetry)**: ratio test `lab_A(F_1) / lab_A(F_5) = 7.3250 ± 0.1%` (same band as B-phase; substrate ratio IDENTICAL since cocycles are substrate-resident).
- **Gate 3 (supporting NULL)**: F3 + F4 A-phase analog NULL.
- **Gate 4 (slope discrimination)**: F4 A-phase multi-pressure slope test (Jacobi-cubic vs φ_88-linear discrimination, 0–34 bar; modified by A-phase pressure-temperature-dependence).
- **Pre-registration PASS** (this S87 gate): all 4 gates pre-registered with A-phase-modified substrate predictions + tolerance bands + Aalto LTL / RHUL µSR platform pins; gate-block landed in `sessions/framework/registry/falsifier-master-inventory.md` as additional row + 4-sub-gate sub-rows tagged "A-phase".
- **Pre-registration FAIL**: any of 4 gates lacks A-phase-modified substrate-derived prediction; OR cohomology-asymmetry ratio drift between A-phase and B-phase lab predictions (would indicate the cocycle norms ARE BdG-sector-resident, contradicting the substrate-IS framing).

**Machinery pin (PRDR)**:
- `N_eval`: 1 (Sage-exact substrate cocycle ratio; identical 7.324992 to B-phase by substrate-resident argument)
- `L_max`: 10 (canonical anchor; cocycle norms substrate-resident at L_max=10)
- `scan_range`: lab pressure 0–34 bar; lab temperature 0.1 mK – 2.5 mK (A-phase regime extends higher than B-phase); Aalto LTL PRIMARY / RHUL secondary
- `step_size`: 4-bar increments for Gate 4 slope discrimination
- `tolerance`: Gate1 ABS A-phase substrate-derived S/N margins per row (chirality-modified; nominally `S < 0.573193 M_KK² × χ_A_correction` where χ_A_correction is A-phase chirality correction factor, expected ≤ 1.5×); Gate2 RATIO ±0.1% (identical to B-phase); Gate3 ABS A-phase margins; Gate4 SLOPE > 3σ
- `scheme`: 3He-A chiral BdG sector inheritance morphism; substrate-derived cocycle ratio Sage-exact via zeta-regulated (`a_n^{ζ}`) Hochschild pairing (substrate-resident, A-phase-independent)
- `convention`: 3He-A chiral symmetry class (NOT BDI); A-phase Δ_A/Δ_B ratio applied to lab-conversion factors but cancels in cohomology-asymmetry test by common-exponent argument
- `random_seed`: N/A
- `GPU path`: N/A (Sage symbolic)

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — `<computed-at-runtime>` (cocycle norms; M_KK; Δ_A vs Δ_B ratio for lab-conversion phase-dependence)
- `.claude/rules/inheritance-falsifier-protocol.md` — `<computed-at-runtime>`
- `sessions/permanent-results-registry.md` — `<computed-at-runtime>` (CF-31 upstream)
- `sessions/framework/registry/falsifier-master-inventory.md` — `<computed-at-runtime>` (target for new "A-phase" row + 4-sub-gate sub-rows; W5-2 lands B-phase rows first; W5-3 lands A-phase rows after)
- `computations/s86_gate_verdicts.txt` — `<computed-at-runtime>` (W-5 DONE-5 cancellation-theorem verdict)
- `researchers/Volovik/` — A-phase µSR platform documentation citations

**Expected output 4-tuple**:
`(value=cocycle_ratio_7.324992_A-phase, scheme=Sage-exact-zeta-regulated-Hochschild-pairing-substrate-resident, convention=3He-A-chiral-muSR-A-phase-modified, L_max=10)`

**Substitution chain** (direction claim: A-phase ratio identical to B-phase ⇒ cocycles substrate-resident):
- Step 1: Cocycle norms `‖φ_67‖`, `‖φ_88‖` are evaluated on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` — the substrate spectral triple, NOT on the BdG-sector restriction.
- Step 2: `r_substrate = ‖φ_67‖ / ‖φ_88‖ = 7.324992` (Sage-exact; same substrate, same ratio, regardless of B-phase or A-phase BdG restriction downstream).
- Step 3: Lab-conversion factors `(f_1/f_5)_A` differ from `(f_1/f_5)_B` by A-phase chirality correction; common-exponent (Δ_A/Δ_B)^p factor cancels in the cohomology-asymmetry RATIO test (W-5 cancellation theorem).
- Step 4: Predicted A-phase ratio `lab_A(F_1)/lab_A(F_5) = r_substrate × (f_1/f_5)_A`. If `(f_1/f_5)_A = (f_1/f_5)_B` (both normalized dimensionless), then lab ratio identical to B-phase 7.3250.
- Step 5: Read direction: identical-ratio prediction is the substrate-IS-not-IN signature; if A-phase µSR measures different ratio from B-phase vortex-core, cocycles are BdG-sector-resident (substrate framing FALSIFIED). If A-phase ratio = B-phase ratio = 7.3250 ± 0.1%, substrate framing CONFIRMED.
- Conclusion: A-phase µSR is the cross-platform substrate-resident-ness test. Identical ratio across two distinct BdG sectors (A-phase chiral vs B-phase BDI) is the substrate-framing prediction.

**What PASSES means** (S87 plan-freeze): All 4 gates pre-registered for 3He-A µSR with A-phase-modified substrate-derived predictions + identical cohomology-asymmetry ratio 7.3250 + Aalto LTL platform pin. The cross-platform identical-ratio prediction is the cleanest test of the substrate-IS-not-IN framing: if Lancaster B-phase vortex-core (W5-2) and Aalto A-phase µSR (W5-3) BOTH measure ratio 7.3250 ± 0.1%, the cocycles are confirmed substrate-resident.

**What FAILS means** (S87 plan-freeze): A-phase substrate-derived predictions not pinned, OR cohomology-asymmetry ratio drifts between A-phase and B-phase predictions. Drift would indicate the cocycle norms are BdG-sector-resident (not substrate-resident), forcing re-evaluation of the `.claude/rules/cross-pillar-bridge-anatomy.md` IS-not-IN anatomy. Constraint-map update: cross-platform identical-ratio prediction is the high-leverage substrate-vs-lab discriminator; failure here forces S88 re-anatomy.

**Substrate framing**: The substrate cocycle ratio `‖φ_67‖ / ‖φ_88‖ = 7.324992` IS computed on the substrate's spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`; it is NOT a property of any BdG-sector restriction. 3He-A and 3He-B both measure the same substrate via different inheritance morphisms (chiral A-phase χ_A and BDI B-phase χ_B); both inherit the same cocycle ratio. Aalto LTL's µSR spectrometer measures muon-spin-resonance asymmetry IN the laboratory frame. The substrate's prediction (identical ratio across A-phase and B-phase) flows FROM the substrate cohomology TOWARD both laboratory platforms.

**Producing script**: `computations/s87_w5_w11_c6_musr_falsifier.py`
- Reads canonical_constants.py for cocycle norms, M_KK, Δ_A/Δ_B ratio.
- Reads .claude/rules/inheritance-falsifier-protocol.md for 4-gate structure.
- Reads CF-31 registry entry (W5-1) and CF-32 inventory rows (W5-2) as upstream inputs.
- Sage-evaluates substrate-resident ratio 7.324992 (identical to B-phase by construction).
- Constructs 5-row A-phase F-table with A-phase chirality corrections to S/N margins.
- Drafts new master-inventory rows tagged "A-phase" (mack-cosmic-bridge writes rows; this gate produces drafts).
- Emits verdict line + dual-SHA companion + (since `[SIGN]`) S87 schema-v2 3-tuple companion.

**Estimated effort**: 1 dispatch (~2h).

**YAML block**:
```yaml
gate_id: S87-W11-C6-MUSR-FALSIFIER
trigger: [VERIFY, SIGN]
classification: PHONONIC
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
script: computations/s87_w5_w11_c6_musr_falsifier.py
expected_output_4tuple:
  value: 7.324992
  scheme: Sage-exact-zeta-regulated-Hochschild-pairing-substrate-resident
  convention: 3He-A-chiral-muSR-A-phase-modified
  L_max: 10
machinery_pin_map:
  N_eval: 1 (Sage-exact substrate cocycle ratio)
  L_max: 10
  scan_range: lab pressure 0-34 bar; lab temperature 0.1-2.5 mK; Aalto LTL PRIMARY / RHUL secondary
  step_size: 4-bar increments for Gate 4
  tolerance: Gate1 ABS A-phase S/N margins per row (chi_A correction); Gate2 RATIO +-0.1% identical to B-phase; Gate3 ABS A-phase margins; Gate4 SLOPE > 3sigma
  scheme: 3He-A-chiral-BdG-inheritance-morphism; substrate-resident cocycle ratio
  convention: 3He-A-chiral-Delta_A-Delta_B-common-exponent-cancellation
  random_seed: N/A
  GPU_path: N/A
sign_pre_registration:
  predicted_direction: NULL on F1/F2/F5 A-phase analogs; identical ratio 7.3250 to B-phase
  predicted_sign: signals < A-phase margins; ratio in [7.318, 7.332] same as B-phase
input_sha_pins:
  - computations/canonical_constants.py: <computed-at-runtime>
  - .claude/rules/inheritance-falsifier-protocol.md: <computed-at-runtime>
  - sessions/permanent-results-registry.md: <computed-at-runtime>  # CF-31
  - sessions/framework/registry/falsifier-master-inventory.md: <computed-at-runtime>  # CF-32
  - computations/s86_gate_verdicts.txt: <computed-at-runtime>
upstream_dependency: S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND (CF-31) + S87-W11-C5-LAB-FALSIFIER (CF-32) must land first
```

---

## §W5-4. S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST (CF-34)

**Trigger**: `[AUDIT]` (registry verification-of-landing; mechanical edit confirming sub-row already in summary table)

**Classification**: GEOMETRIC (NCG-axiomatic registry recast; HP^1-content distinction between η-invariant and GV-Heitsch invariant; promotes pre-S86 §VII.P-v1 to §VII.P-v2 corridor)

**Hypothesis**: The §VII.P parity-blindness theorem (S85 W2-7 → S86 strengthened) requires a v2 recast distinguishing the parity-blind η-invariant (even-grading regulator-weighted Mellin moment) from the HP^1-content-detecting GV-Heitsch invariant (odd-grading regulator-weighted Mellin moment). The §VII.AF.2 sub-row (already in registry summary table per S87 plan-write registry-sync) IS the §VII.P-v2 recast target slot; this gate verifies the row exists with correct HP^1-content-distinct convention text and cross-references §VII.P-v1 deprecation.

**Wave-owner agent**: `volovik-superfluid-universe-theorist` (orchestrator role for mechanical registry edit; co-signer connes-ncg-theorist for NCG-axiomatic v2 recast text). Per the spec, this gate is mechanical registry surgery rather than new derivation.

**Pass/fail/INFO threshold**:
- **PASS**: §VII.AF.2 sub-row exists in `sessions/permanent-results-registry.md` summary table with theorem-name "§VII.P-v2 HP^1-content-distinct corridor recast"; sub-row body cites both V1 (η-invariant parity-blindness; S85 W2-7 → S86 promotion) AND C1 (GV-Heitsch HP^1-detection; S86 W-5 R3-γ) per `.claude/rules/registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY structure; sub-row body explicitly DEPRECATES §VII.P-v1 with cross-reference; sub-row body cites the (η = 0, GV ≠ 0) signature on the (C_H, C_epsH) parity-twin pair per S86 W-11 closure; HP^1-content-distinct convention text matches `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension".
- **FAIL**: §VII.AF.2 sub-row absent; OR row body uses PRIMARY+CONFIRMATION instead of SOURCE-DOUBLE-CITE-CO-PRIMARY (sequential V+C chain misclassified); OR §VII.P-v1 deprecation cross-reference missing; OR HP^1-content-distinct convention text drifted from W-11 calibration corpus extension.
- **INFO**: row exists but optional convention-cross-link fields absent (e.g., missing pointer to CF-65 η-GV regulator-independence verification queued for S87 W?).

**Machinery pin (PRDR)**:
- `N_eval`: 1 (single registry row verification; no compute)
- `L_max`: N/A
- `scan_range`: N/A (mechanical edit)
- `step_size`: N/A
- `tolerance`: ABSOLUTE (string-match audit); row text MUST contain pattern `"§VII.P-v2 HP^1-content-distinct"` AND `"SOURCE-DOUBLE-CITE-CO-PRIMARY"` AND `"deprecates §VII.P-v1"` AND `"(η = 0, GV ≠ 0)"`
- `scheme`: registry verification-of-landing per `.claude/rules/mechanical-closure-discipline.md` (this is NOT a mechanical-closure script blocked on upstream PRE-REG-INC; it's a verification of pre-existing row content). Row may use either η-invariant `a_n^{ζ}` or GV-Heitsch invariant `a_n^{ζ}` regulator-tagged form per `.claude/rules/regulator-pin-discipline.md`.
- `convention`: HP^1-content-distinct corridor convention; even-grading vs odd-grading regulator-weighted Mellin moments
- `random_seed`: N/A
- `GPU path`: N/A

**Input SHA-256 pins**:
- `sessions/permanent-results-registry.md` — `<computed-at-runtime>` (target file; verify §VII.AF.2 sub-row exists)
- `.claude/rules/registry-landing.md` — `<computed-at-runtime>` (SOURCE-DOUBLE-CITE-CO-PRIMARY structure spec)
- `.claude/rules/regulator-pin-discipline.md` — `<computed-at-runtime>` (W-11 Class-(c) PIN-DRIFT-FROM-STALE-SOURCE calibration corpus extension; HP^1-content-distinct convention)
- `computations/s85_gate_verdicts.txt` — `<computed-at-runtime>` (W2-7 η-invariant parity-blindness theorem promotion verdict)
- `computations/s86_gate_verdicts.txt` — `<computed-at-runtime>` (W-5 R3-γ GV-Heitsch HP^1-detection verdict; W-11 (η=0, GV≠0) closure verdict)

**Expected output 4-tuple**:
`(value=row_exists_with_correct_text=1.0, scheme=registry-verification-of-landing, convention=HP1-content-distinct-corridor-recast, L_max=N/A)`

**Substitution chain** (direction claim: row exists ⇒ verification-PASS):
- Step 1: Row presence test: `present := grep("§VII.P-v2 HP^1-content-distinct", "sessions/permanent-results-registry.md") > 0`.
- Step 2: Convention-string tests: `co_primary := grep("SOURCE-DOUBLE-CITE-CO-PRIMARY", row_text) > 0`; `deprecation := grep("deprecates §VII.P-v1", row_text) > 0`; `signature := grep("(η = 0, GV ≠ 0)", row_text) > 0`.
- Step 3: Conjunction: `verification := present AND co_primary AND deprecation AND signature`.
- Step 4: Substitute: if all 4 grep tests return `True`, `verification = True`; else `False`.
- Step 5: Direction: `verification = True` ⇒ PASS (row landed with correct content); `verification = False` AND row absent ⇒ FAIL with remediation request to next-session (re-author row); `verification = False` AND row present but convention strings absent ⇒ FAIL with mechanical edit remediation.
- Conclusion: PASS criterion is conjunction of 4 grep tests; FAIL routes are diagnosable by which of 4 strings is missing.

**What PASSES means**: The §VII.P-v2 HP^1-content-distinct corridor recast is permanent registry state, with explicit DEPRECATION of §VII.P-v1, SOURCE-DOUBLE-CITE-CO-PRIMARY structure citing both V1 (parity-blindness) and C1 (HP^1-detection), and the (η=0, GV≠0) signature on (C_H, C_epsH). Future joint-probe gates targeting HP^1 detection have a registered registry anchor; bare η-invariant citations are no longer admissible per `regulator-pin-discipline.md` W-11 calibration corpus.

**What FAILS means**: §VII.AF.2 sub-row missing or convention strings drifted; pre-S87 v2 recast rough draft was not landed completely. Remediation: dispatch a mechanical edit to write the missing strings (or to author the entire row if absent). Constraint-map update: §VII.P-v2 corridor remains structurally available but operationally not pinned; CF-65 (η-GV regulator-independence verification) must be re-pre-registered against the v2 corridor convention.

**Substrate framing**: The substrate IS even-grading + odd-grading regulator-weighted Mellin moments of D_K. η-invariant IS the even-grading projection (parity-blind to HP^1); GV-Heitsch invariant IS the odd-grading projection (HP^1-detecting). Saying "η-invariant fails to detect HP^1 content because parity-blind" is the SUBSTRATE explanation; saying "η-invariant is a less powerful invariant than GV-Heitsch on HP^1 manifolds" inverts the direction (treats invariants as external choices rather than substrate spectral projections). The §VII.P-v2 row text must flow FROM substrate TOWARD invariant identification.

**Producing script**: `computations/s87_w5_vii_p_v2_hp1_content_distinct_recast_verify.py`
- Reads sessions/permanent-results-registry.md.
- Greps for the 4 conjunction strings (§VII.P-v2 HP^1-content-distinct + SOURCE-DOUBLE-CITE-CO-PRIMARY + deprecates §VII.P-v1 + (η = 0, GV ≠ 0)).
- If all 4 present → PASS. Emits verdict line.
- If any absent → FAIL with remediation. Drafts the missing row text (or amendments) and emits FAIL-with-remediation verdict (per mechanical-closure-discipline FAIL-with-remediation pattern); a follow-up Edit dispatch lands the strings.

**Estimated effort**: 1 dispatch (~30 min for verification; +30 min if FAIL routes to mechanical edit follow-up).

**YAML block**:
```yaml
gate_id: S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST
trigger: [AUDIT]
classification: GEOMETRIC
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
script: computations/s87_w5_vii_p_v2_hp1_content_distinct_recast_verify.py
expected_output_4tuple:
  value: 1.0
  scheme: registry-verification-of-landing
  convention: HP1-content-distinct-corridor-recast
  L_max: N/A
machinery_pin_map:
  N_eval: 1
  L_max: N/A
  scan_range: N/A
  step_size: N/A
  tolerance: ABSOLUTE string-match conjunction (4 patterns)
  scheme: registry_verification_of_landing
  convention: HP1-content-distinct-corridor-recast
  random_seed: N/A
  GPU_path: N/A
input_sha_pins:
  - sessions/permanent-results-registry.md: <computed-at-runtime>
  - .claude/rules/registry-landing.md: <computed-at-runtime>
  - .claude/rules/regulator-pin-discipline.md: <computed-at-runtime>
  - computations/s85_gate_verdicts.txt: <computed-at-runtime>
  - computations/s86_gate_verdicts.txt: <computed-at-runtime>
upstream_dependency: S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND (CF-31) anatomy on disk
```

---

## §W5-5. S87-CROSS-PILLAR-FORWARD-CANDIDATES (CF-35)

**Trigger**: `[AUDIT]` (forward-looking template-adoption pre-registration; workshop-design SUGGESTION model with K=1 calibration instance)

**Classification**: GEOMETRIC (cross-pillar-bridge-anatomy template adoption protocol; rank-2 generalization clause for future ker(ι_*) characterizations)

**Hypothesis**: The S86 W-5 cross-pillar-bridge-anatomy (5-element + 3-level) is one calibration corpus instance; per `.claude/rules/agent-standards.md` §"HIGH-DENSITY WORKSHOP TEMPLATE" the discipline hardens to a permanent rule when N=3 distinct workshops invoke it (K=3 promotion threshold). The pre-registered template-adoption SUGGESTION applies the anatomy to forward bridge candidates: Pillar I↔II (substrate↔cosmology measurement; e.g., n_s ↔ Planck CMB); BdG-spectral-triple↔3He-B observable (substrate-resident cocycles ↔ A-phase µSR + B-phase vortex-core; partially CF-32+CF-33); and the rank-2 generalization to higher-rank ker(ι_*) characterizations per `.claude/rules/inheritance-falsifier-protocol.md` Q8 "Generalization beyond 3He-B".

**Wave-owner agent**: `volovik-superfluid-universe-theorist` (orchestrator for the forward-looking template adoption; per `feedback_agent-roster.md`). Co-signer: `connes-ncg-theorist` (NCG-axiomatic side of any future Pillar A↔B bridge candidates).

**Pass/fail/INFO threshold**:
- **PASS**: Template-adoption SUGGESTION text landed in `.claude/rules/cross-pillar-bridge-anatomy.md` §"Calibration corpus" (or in a sibling §"Forward template-adoption" sub-section) listing W-5 as instance #1; rank-2 generalization clause from `.claude/rules/inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)" cross-referenced; 2-3 candidate forward bridge pairs explicitly enumerated (Pillar I↔II + BdG↔3He-B + one additional candidate per `feedback_fix-in-session-never-defer.md`); SUGGESTION-not-MANDATORY status declared (K=1 calibration; awaits N=3 promotion).
- **FAIL**: Template-adoption text absent OR enumeration of forward bridges absent OR SUGGESTION-vs-MANDATORY status not declared (would create false-PASS where authors believe the discipline is mandatory at K=1).
- **INFO**: Template text landed but rank-2 generalization clause cross-reference missing; structure operational but not yet cross-linked to inheritance-falsifier-protocol.md generalization clause.

**Machinery pin (PRDR)**:
- `N_eval`: 1 (single rule-file edit; calibration-corpus row addition + SUGGESTION clause)
- `L_max`: N/A
- `scan_range`: forward bridge candidate enumeration; minimum 2-3 candidates required per `feedback_fix-in-session-never-defer.md`
- `step_size`: N/A
- `tolerance`: ABSOLUTE (text-presence audit on `.claude/rules/cross-pillar-bridge-anatomy.md` post-edit); SUGGESTION-vs-MANDATORY status pinned
- `scheme`: workshop-design SUGGESTION-to-permanent-rule promotion ladder per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold
- `convention`: cross-pillar-bridge-anatomy template adoption; K=1 calibration; SUGGESTION-not-MANDATORY status pinned at S87-W5-5 plan-freeze
- `random_seed`: N/A
- `GPU path`: N/A

**Input SHA-256 pins**:
- `.claude/rules/cross-pillar-bridge-anatomy.md` — `<computed-at-runtime>` (target file for template-adoption SUGGESTION text; current §"Calibration corpus" carries W-5 instance #1)
- `.claude/rules/inheritance-falsifier-protocol.md` — `<computed-at-runtime>` (Generalization beyond 3He-B / Q8 cross-reference target)
- `.claude/rules/agent-standards.md` — `<computed-at-runtime>` (HIGH-DENSITY WORKSHOP TEMPLATE K=3 promotion threshold)
- `sessions/permanent-results-registry.md` — `<computed-at-runtime>` (CF-31 §VII.W or §VII.AF entry as the canonical W-5 calibration corpus instance #1)

**Expected output 4-tuple**:
`(value=template_landed_with_3_candidates_and_SUGGESTION_status=1.0, scheme=workshop-design-SUGGESTION-K1-calibration, convention=cross-pillar-bridge-anatomy-forward-template-adoption, L_max=N/A)`

**Substitution chain** (direction claim: K=1 ⇒ SUGGESTION not MANDATORY):
- Step 1: Define K = number of distinct high-density workshops invoking the template; W-5 is instance #1, so K = 1.
- Step 2: Define K_promotion = 3 (per `agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE forward calibration; aligns with `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold).
- Step 3: Substitute: K (=1) < K_promotion (=3).
- Step 4: Read direction: K < K_promotion ⇒ status = SUGGESTION (not MANDATORY).
- Step 5: Conclusion: this gate must declare SUGGESTION-not-MANDATORY status explicitly; promotion event triggers when N=3 calibration instances accumulate (likely S88+ from future cross-pillar bridges).

**What PASSES means**: The cross-pillar-bridge-anatomy template is positioned for forward use across the framework's pillars, with explicit calibration-corpus tracking (instance #1 = W-5; instances #2 + #3 are S88+ candidates to be enumerated). Any future bridge candidate (Pillar I↔II, etc.) MUST follow the 5-element + 3-level structure per the SUGGESTION; absence of structure routes to plan-freeze halt. Rank-2 generalization clause cross-referenced to inheritance-falsifier-protocol.md Q8 ensures higher-rank ker(ι_*) characterizations are also covered.

**What FAILS means**: Template-adoption SUGGESTION not landed; K=1 calibration instance not pinned; rank-2 generalization clause cross-reference missing. Forward bridge candidates have no methodological framework; future Pillar I↔II or higher-rank ker(ι_*) bridges land ad-hoc, breaking the structural-anatomy discipline. Constraint-map update: forward bridges remain available as research targets, but the methodology-floor pin is missing; S88 plan-freeze must re-pre-register before any bridge candidate proceeds.

**Substrate framing**: The substrate IS the cross-pillar bridge anatomy itself — a structural property of how finite-L spectral-triple observables (substrate-IS) map via HKR / K-theory / Connes-Karoubi pairing to continuum laboratory observables (laboratory-IN). The 5-element + 3-level discipline IS the anatomy; the K=3 promotion threshold IS the methodology-floor calibration ladder. Saying "the rule is too strict, let's loosen it" inverts the direction (treats the rule as external choice rather than substrate-anatomy crystallization). Forward template adoption flows FROM the anatomy TOWARD specific bridge candidates.

**Producing script**: `computations/s87_w5_cross_pillar_forward_candidates.py`
- Reads .claude/rules/cross-pillar-bridge-anatomy.md (current state of §"Calibration corpus").
- Reads .claude/rules/inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)".
- Reads .claude/rules/agent-standards.md §"HIGH-DENSITY WORKSHOP TEMPLATE" K=3 threshold.
- Drafts forward template-adoption SUGGESTION text (3 candidate bridges enumerated; rank-2 generalization clause cross-referenced; SUGGESTION-not-MANDATORY status declared at K=1).
- Appends drafted text to .claude/rules/cross-pillar-bridge-anatomy.md (orchestrator-only-edit per per-rule-file convention; this gate is volovik orchestrator role; subagent edit-denial does not apply since volovik is wave-owner orchestrator role).
- Emits verdict line + dual-SHA companion.
- Per CF-77 (`feedback_dispatch-discipline.md` SessionStart hook promotion at S87+), no concurrency cap concern for this gate.

**Estimated effort**: 1 dispatch (~1h drafting + edit + verification); scoped per future bridge per CF-35 brief.

**YAML block**:
```yaml
gate_id: S87-CROSS-PILLAR-FORWARD-CANDIDATES
trigger: [AUDIT]
classification: GEOMETRIC
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
script: computations/s87_w5_cross_pillar_forward_candidates.py
expected_output_4tuple:
  value: 1.0
  scheme: workshop-design-SUGGESTION-K1-calibration
  convention: cross-pillar-bridge-anatomy-forward-template-adoption
  L_max: N/A
machinery_pin_map:
  N_eval: 1
  L_max: N/A
  scan_range: 2-3 forward bridge candidates enumeration
  step_size: N/A
  tolerance: ABSOLUTE text-presence (SUGGESTION clause + 3 candidates + rank-2 cross-ref)
  scheme: workshop_design_SUGGESTION_to_MANDATORY_K3_promotion_ladder
  convention: cross-pillar-bridge-anatomy-forward-template-adoption-K1-calibration
  random_seed: N/A
  GPU_path: N/A
input_sha_pins:
  - .claude/rules/cross-pillar-bridge-anatomy.md: <computed-at-runtime>
  - .claude/rules/inheritance-falsifier-protocol.md: <computed-at-runtime>
  - .claude/rules/agent-standards.md: <computed-at-runtime>
  - sessions/permanent-results-registry.md: <computed-at-runtime>  # CF-31
upstream_dependency: S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND (CF-31)
```

---

## Wave 5 → Wave 6 Decision Point

After all 5 W5 gates verdict-emit and the V3 closure ladder validates:

- **All 5 PASS** → W5 complete; W6 (next wave per S87 plan partition) dispatches autonomously per `feedback_dispatch-discipline.md`. CF-31 establishes the registry anchor for any S88+ Pillar A↔B bridge candidates; CF-32+CF-33 lab pre-registrations queued for multi-year experimental scheduling on Lancaster MCT-3 / RHUL / Aalto LTL platforms; CF-34 settles §VII.P-v2 corridor; CF-35 positions forward template adoption.
- **W5-1 (CF-31) FAILS** → BLOCKING for W5-2 + W5-3 + W5-4 + W5-5. Mechanical-closure script `computations/s87_w5_pre_reg_inc_closure.py` per `.claude/rules/mechanical-closure-discipline.md` emits PRE-REG-INC verdicts for the 4 downstream gates with `value='PRE-REG-INC_blocked_by_S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND_FAIL'`; downstream re-dispatch deferred to S88+ once registry anatomy lands.
- **W5-2 or W5-3 FAILS** → not blocking for W5-4 / W5-5 (cohomology-asymmetry pre-registration is independent of v2 recast verification + forward-candidate template); downstream gates proceed; the FAILing lab-pre-reg routes to S88 remediation per the inheritance-falsifier-protocol.md 4-gate structure.
- **W5-4 FAILS (registry row absent)** → mechanical edit follow-up dispatch lands missing strings; auto-rerun verifies row content; not blocking for W5-5.
- **W5-5 FAILS (forward template not landed)** → not blocking for any W5 gate; structural status preserved; SUGGESTION clause re-routes to S88 per `feedback_fix-in-session-never-defer.md`.
- **V3 closure FAIL on any signal** → invoke `_recovery_controller.py` per `.claude/rules/v3-closure-recovery.md` Stage 1 (max 2 iterations per signal) → Stage 2 (V3-NON-COMPLIANT fallback) → Stage 3 (user trigger). Physics verdicts unchanged; ladder closure deferred to S88 leading carry-forward.

---

## Wave 5 Machinery-Enumeration Pin (§0.11)

Per PRDR (Pre-Registration Dry-Run, `.claude/rules/epistemic-discipline.md`), the following machinery parameters are enumerated and pinned at plan-freeze for ALL W5 gates:

| Parameter | Value (per gate; "—" = N/A) |
|:----------|:----------------------------|
| `schema_version` | `R3` (all 5 gates) |
| `verdict_source` | `computations/s87_gate_verdicts.txt` (all 5 gates) |
| `regulator_tag` | `a_n^{ζ}` (W5-1: zeta-regulated Hochschild pairing; W5-2/W5-3: zeta-regulated cocycle norms; W5-4/W5-5: N/A — no `a_n` citation) |
| `regulator_convention_lockdown` | N/A (W5 gates are not DR3-class L_max-stability gates per `.claude/rules/regulator-convention-lockdown.md` scope clause; W5-1's L-scan companion sub-gate IS DR3-adjacent — uses CAC if it activates) |
| `cross_pillar_bridge_audit` | MANDATORY (W5-1: `_cross_pillar_bridge_audit.py` runs at plan-freeze AND post-execution); not applicable W5-2/W5-3/W5-4/W5-5 |
| `inheritance_falsifier_4gate` | MANDATORY (W5-2 + W5-3: 4-gate structure per `inheritance-falsifier-protocol.md`); not applicable W5-1/W5-4/W5-5 |
| `source_double_cite_co_primary` | MANDATORY (W5-1 + W5-4: SOURCE-DOUBLE-CITE-CO-PRIMARY structure per `registry-landing.md`); not applicable W5-2/W5-3/W5-5 |
| `signed_pre_registration` | REQUIRED for W5-1 + W5-2 + W5-3 (`[SIGN]` trigger; S87 schema-v2 3-tuple companion row); W5-4/W5-5 pure `[AUDIT]` |
| `substrate_first_provenance_audit` | manual review (V.1 implementation pending; per session-87-context.md §1.4) |
| `mcp_query_required` | YES (all 5 gates: `mcp__knowledge__.search_knowledge` + `get_constant` + `trace_entity` per project mandate; W5-2 also `mcp__sage__.sage_eval` for ratio 7.324992 verification) |
| `GPU_path_VRAM_check` | W5-1 sub-gate: `torch.linalg.eigh` on AMD RX 9070 XT, ~12-15 GB VRAM (within 17 GB cap); other W5 gates N/A |
| `compute_time_envelope` | W5-1 ~3-4h primary + ~3-6h sub-gate; W5-2 ~2h+~2h; W5-3 ~2h; W5-4 ~30 min; W5-5 ~1h |

---

## Wave 5 Input-SHA Ledger

The following files are SHA-pinned across all W5 gate input-pin maps; each gate computes the SHA at runtime and emits via the `audit_sha256` companion-row protocol per `.claude/rules/gate-verdicts.md` schema-v2.

| File | Used by gates | Reason |
|:-----|:-------------|:-------|
| `sessions/permanent-results-registry.md` | W5-1, W5-2, W5-3, W5-4, W5-5 | registry target; CF-31 lands the §VII.AF entry; CF-32/CF-33 cite as upstream input; CF-34 verifies §VII.AF.2 sub-row; CF-35 cites W-5 calibration instance |
| `computations/canonical_constants.py` | W5-1, W5-2, W5-3 | substrate-IS pin source (R_universal_W5, cocycle norms, M_KK, Δ_A/Δ_B) |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | W5-1, W5-5 | 5-anatomy + 3-level ladder spec; forward template adoption target |
| `.claude/rules/inheritance-falsifier-protocol.md` | W5-2, W5-3, W5-5 | 4-gate structure spec; rank-2 generalization clause |
| `.claude/rules/regulator-pin-discipline.md` | W5-1, W5-2, W5-3, W5-4 | `a_n^{ζ}` tag spec; W-11 calibration corpus extension for HP^1-content distinction |
| `.claude/rules/registry-landing.md` | W5-1, W5-4 | SOURCE-DOUBLE-CITE-CO-PRIMARY structure spec |
| `.claude/rules/phononic-framing.md` | W5-1, W5-2, W5-3, W5-4, W5-5 | IS-not-IN convention + cross-pillar bridge anatomy framing-rule promotion |
| `.claude/rules/agent-standards.md` | W5-5 | HIGH-DENSITY WORKSHOP TEMPLATE K=3 promotion threshold |
| `computations/s86_gate_verdicts.txt` | W5-1, W5-2, W5-3, W5-4 | W-5 W5-6 atlas-match verdict (Level-3 anchor); W-5 DONE-5 cancellation theorem; W-11 (η=0, GV≠0) closure |
| `computations/s85_gate_verdicts.txt` | W5-4 | W2-7 η-invariant parity-blindness theorem promotion verdict |
| `computations/s84_spectrum_cache_L12_tau019.npz` | W5-1 (sub-gate only) | L_max ∈ {8,9,10,11,12} L-scan envelope-pattern check |
| `sessions/framework/registry/falsifier-master-inventory.md` | W5-2, W5-3 | target for new lab-falsifier rows + 4-sub-gate sub-rows; mack-cosmic-bridge sole-writer |
| `researchers/Volovik/` | W5-2, W5-3 | Lancaster MCT-3 / Aalto LTL / RHUL platform documentation citations |

---

**End of session-87-plan-w5.md.**
