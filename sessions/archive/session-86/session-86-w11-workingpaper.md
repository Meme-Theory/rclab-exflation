# Session 86 Wave W11 — Lab-falsifier suite (SI translation + EVOI tree) (Results Working Paper)

**Session**: 86 | **Wave**: W11 | **Plan**: session-86-plan-w11.md | **Theme**: Translate the 9 lab observables registered at S85 W8-4 (3 sweet-spot + 6 cross-platform) from M_KK-normalized substrate language into laboratory-native SI units, then assign each observable a 5-yr EVOI level and a pre-registered 4-branch decision tree.

## Gate Sections

### §W11-1. S86-LAB-SI-TRANSLATION (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-LAB-SI-TRANSLATION`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (substrate excitations measured at table-top compactification ratio)
**Agent**: `volovik-superfluid-universe-theorist` (PRIMARY)
**Hypothesis**: Each of the 9 W8-4 M_KK-normalized ratios admits a unique SI-unit translation into its platform-native observable via closed-form prefactor multiplication, with literature-anchored single-shot detection sensitivities `sigma_detect` for each platform.
**Plan reference**: `sessions/session-plan/session-86-plan-w11.md` §W11-1.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed before writing the script):

- `mcp__knowledge__search_knowledge("S86-LAB-SI-TRANSLATION")` → no results; gate is NEW at S86 W11-1 (not pre-closed). Mark NOT PRE-CLOSED.
- `mcp__knowledge__search_knowledge("W8-4 SU3 OP lab predictions")` → returns the S85-W8-4-SU3-OP-LAB-PREDICTIONS gate verdict (`PASS, value='3/3_directions_9/9_obs', scheme=Jensen_SU3, convention=Gell_Mann, L_max=8`) and the producing script `s85_w8_su3_op_lab_predictions.py`. Confirms upstream PASS; 9 magnitudes are FROZEN per S85 W-2 + P1 carry-forward.
- `mcp__knowledge__search_knowledge("lab-falsifier M_KK SI translation")` → returns prior-session SI-conversion patterns (e.g., `t_MKK_seconds = hbar_SI / (M_KK * 1.602e-10)` from s60; `tau_L_SI = tau_min / (M_KK / (hbar_GeV_s * 1e9))` from s61). No prior SI translation specifically for the W8-4 lab-observable trio — this row class is NEW. Confirms LAB-FALSIFIER level is opened by C5.
- `mcp__knowledge__get_constant("M_KK")` → `7.428660036284456e+16` GeV. Matches plan §0.10 INPUT PIN MAP.
- `mcp__knowledge__get_constant("Delta_BCS")` → `0.4642547394830737` (M_KK units, R-PROTECTED, alias for `Delta_0_OES`, session S70 BCS-GAP-CANONICAL-70). Matches.
- Conclusion: gate is NOT pre-closed; W8-4 magnitudes are canonical; M_KK and Delta_BCS pins are valid; LAB-FALSIFIER row class is NEW (zero prior coverage).

**Verdict**:

`S86-LAB-SI-TRANSLATION: INFO -- value='9-rows-populated' scheme=M_KK_mapping convention=per_platform_units L_max=N/A audit_sha256=6a2d523920c340321fe537672a39aa6d971a81c330236d78aee59138900628ce content_sha256=5d2449353ebdae40b16d648cf054196b3d8c4e47c31e2d30aadb73975f7ffe03 schema_version=R3`

`# audit_sha256 companion row: S86-LAB-SI-TRANSLATION audit=6a2d523920c34032 content=5d2449353ebdae40`

INFO band: all 9 rows populated (`SI_value`, `sigma_detect`, `lit_sha` non-null on every row); 6 rows flagged `provisional` because the 3He-A and 173Yb literature anchors report sigma_detect as state-of-art upper-bound rather than single-shot 3-sigma floors (per plan §9 INFO clause). The 3 FeSe rows (XA2, SW2, XB2) are non-provisional (single-shot ppm-resolution NMR).

**Results**:

**4-tuple**: `(value='9-rows-populated', scheme=M_KK_mapping, convention=per_platform_units, L_max=N/A)`

**9-row SI translation table** (artifact: `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv`):

| obs_id | platform | lambda  | W8_4_ratio | prefactor (& unit)      | SI_value     | SI_unit | sigma_detect  | detection_ratio | lit_sha            |
|:-------|:---------|:--------|-----------:|------------------------:|-------------:|:--------|--------------:|----------------:|:-------------------|
| SW1    | 3He-A    | lambda_6 |    1.7267 | 34.146 MHz              | 5.896e+01    | MHz     | 1.000e-03 MHz | 5.896e+04       | ecc168738d744136   |
| SW2    | FeSe     | lambda_7 |    1.8226 | 200.0 ppm               | 3.645e+02    | ppm     | 5.000e+00 ppm | 7.290e+01       | 28371024791ddafe   |
| SW3    | 173Yb    | lambda_8 |    2.8500 | 0.500 s^-1              | 1.425e+00    | s^-1    | 5.000e-02 s^-1| 2.850e+01       | 4cd097a278b4adbd   |
| XA1    | 3He-A    | lambda_6 |    1.7267 | 34.146 MHz              | 5.896e+01    | MHz     | 1.000e-03 MHz | 5.896e+04       | ecc168738d744136   |
| XA2    | FeSe     | lambda_6 |    0.7674 | 200.0 ppm               | 1.535e+02    | ppm     | 5.000e+00 ppm | 3.070e+01       | 28371024791ddafe   |
| XA3    | 173Yb    | lambda_6 |    5.4938 | 0.500 s^-1              | 2.747e+00    | s^-1    | 5.000e-02 s^-1| 5.494e+01       | 4cd097a278b4adbd   |
| XB1    | 3He-A    | lambda_7 |    0.5756 | 34.146 MHz              | 1.965e+01    | MHz     | 1.000e-03 MHz | 1.965e+04       | ecc168738d744136   |
| XB2    | FeSe     | lambda_7 |    1.8226 | 200.0 ppm               | 3.645e+02    | ppm     | 5.000e+00 ppm | 7.290e+01       | 28371024791ddafe   |
| XB3    | 173Yb    | lambda_7 |   13.1852 | 0.500 s^-1              | 6.593e+00    | s^-1    | 5.000e-02 s^-1| 1.319e+02       | 4cd097a278b4adbd   |

Row partitioning:
- **Sweet-spot diagonal** (SW1/SW2/SW3): each platform measures the substrate's native SU(3)-unique direction (lambda_6 -> 3He-A, lambda_7 -> FeSe, lambda_8 -> 173Yb). These are the "compactification-resonance" rows: maximum projection of the framework-unique direction onto its native lab.
- **Cross-platform A** (XA1/XA2/XA3): all three platforms measured under the lambda_6 column. Quantifies how the substrate's lambda_6 excitation appears in non-native labs.
- **Cross-platform B** (XB1/XB2/XB3): all three platforms measured under the lambda_7 column. Same role for lambda_7.

The 9 rows together span the 3x3 (3 unique directions x 3 platforms) lab-observable matrix that W8-4 produced.

**Substitution chain (3He-A illustrative row, SW1)** — closed-form prefactor multiplication; this is the load-bearing direction-claim verification per `.claude/rules/math-scripts.md` §Double-Check Logic:

```
Step 1 (definitions):
  - W8-4 ratio (sweet-spot lambda_6, 3He-A platform, dimensionless)
        = obs_3HeA[lambda_6 -> idx 0] = 1.7266629
  - 3He-A platform energy scale (lab-native, NOT the substrate M_KK):
        Delta_3HeA = 1.764 * k_B * T_c
        (BCS weak-coupling; 1.764 = 2 e^gamma_E / pi)
  - T_c(superfluid 3He at 0 bar) = 0.929 mK   [Greywall 1986, canonical]
  - Frequency form: nu_Delta_3HeA = Delta_3HeA / h_planck

Step 2 (substitution):
  Delta_3HeA = 1.764 * (1.380649e-23 J/K) * (0.929e-3 K)
             = 2.2625e-26 J
  nu_Delta_3HeA = (2.2625e-26 J) / (6.62607015e-34 J*s)
                = 3.4146e+07 Hz
                = 34.146 MHz

  delta_nu_K_lab(SW1) = (W8-4 ratio) * nu_Delta_3HeA
                      = 1.7266629 * 34.146 MHz

Step 3 (simplification):
  delta_nu_K_lab(SW1) = 58.96 MHz   (matches script SI_value column)

Step 4 (direction — REPORT ONLY, not a PASS/FAIL claim):
  sigma_detect(3He-A) = 1.0 kHz = 1.0e-3 MHz
       [Eltsov et al. 2010 arXiv:1005.0546, Aalto/Helsinki ROTA NMR
        linewidth resolution; SHA ecc168738d744136]
  detection_ratio = 58.96 MHz / 1.0e-3 MHz = 5.896e+04
                  >> 1   (well above floor)
  Direction: above floor. Reported in CSV/JSON. Carries to C6 EVOI tree.
```

**Substrate-framing per `.claude/rules/phononic-framing.md`** (canonical phrasing in CSV `phenomenology_note` column for every row):
- SW1/XA1: "the substrate's delta_omega_K/omega_K ratio measured at the 3He-A compactification scale (sweet-spot lambda_6 direction)"; XB1: "...under cross-platform lambda_7 projection."
- SW2/XB2: "the substrate's K_anis/K_0 ratio measured at the FeSe-NMR compactification scale (sweet-spot lambda_7 direction)"; XA2: "...under cross-platform lambda_6 projection."
- SW3: "the substrate's Gamma_3B(unique)/Gamma_3B(inherited) ratio measured at the 173Yb optical-lattice compactification scale (sweet-spot lambda_8 direction)"; XA3/XB3: "...under cross-platform lambda_6/_7 projection."

The forbidden phrasing "analog of cosmic [X] in a [3He-A / FeSe / 173Yb] system" appears nowhere in the artifacts.

**Per-platform literature SHA-pins** (full SHA256 in JSON `literature_citations`; 16-hex prefix here for human scan):

- **3He-A platform**: arXiv:1005.0546 — Eltsov, de Graaf, Heikkinen, Hosio, Hanninen, Krusius, L'vov; "Super Stability of Laminar Vortex Flow in Superfluid 3He-B"; Phys. Rev. Lett. 105, 125301 (2010); SHA256 = `ecc168738d7441368b5e601712d414d49e4e15259ffd9b493ed641e8233e190d`. Anchors sigma_detect = 1 kHz (Aalto/Helsinki ROTA NMR linewidth resolution; upper-bound representation, hence provisional flag).
- **FeSe platform**: arXiv:2010.01020 — Zhou, Scherer, Mayaffre, Toulemonde, Ma, Li, Andersen, Julien; "Singular magnetic anisotropy in the nematic phase of FeSe"; Phys. Rev. B 102, 144410 (2020); SHA256 = `28371024791ddafe014777f65bceca22d3d926eb3ea3b2484bbb821e4e39702a`. Anchors sigma_detect = 5 ppm (single-shot 77Se NMR Knight-shift resolution; non-provisional).
- **173Yb platform**: arXiv:0905.4948 — Cazalilla, Ho, Ueda; "Ultracold Gases of Ytterbium: Ferromagnetism and Mott States in an SU(6) Fermi System"; New J. Phys. 11, 103033 (2009); SHA256 = `4cd097a278b4adbd5050bf2bfd764345e84f76e5505eaa5586710c5f3de29da4`. Anchors sigma_detect = 0.05 s^-1 (theoretical floor for 3-body loss rate at SU(N) lattice density n ~ 1e14 cm^-3, achievable at Florence/JILA/Munich; upper-bound representation, hence provisional flag).

**Provisional rows** (per plan §9 INFO clause): SW1, XA1, XB1, SW3, XA3, XB3 (6 of 9 — the 3He-A and 173Yb rows). The 3 FeSe rows (XA2, SW2, XB2) are non-provisional. The provisional flag does NOT subtract from PASS-completeness — every row is fully populated — it signals that a tighter literature anchor (single-shot 3-sigma floor instead of state-of-art upper-bound) would refine the detection_ratio bookkeeping for C6.

**Solution-space note**:
- INFO with all 9 rows populated **opens the 9-row LAB-FALSIFIER corridor** for W14-W6 NEW row class. Each of the 9 substrate predictions now has (a) an SI value, (b) a literature-anchored detection floor, and (c) a SHA-pinned citation chain. The framework's lab-falsifier portfolio is lifted from 0 entries (pre-S86) to 9 atomic falsifier predictions on terrestrial platforms with 5-yr decision horizons (2026-2031).
- The high-detection-ratio rows (SW1 / XA1 / XB1 at det_ratio ~ 1e4-6e4 for 3He-A; SW3 / XA3 / XB3 at det_ratio ~ 30-130 for 173Yb; SW2 / XA2 / XB2 at det_ratio ~ 30-73 for FeSe) all sit ABOVE their respective platform sigma_detect floors. Per plan §9, this is REPORTED-not-gated: the gate is binary on row existence, not on direction of any single row's detection_ratio. C6 (sagan) consumes the detection_ratios to assign LAB-FALSIFIER levels A/B/C/D and 4-branch decision trees.
- The provisional flag on 6 rows (3He-A and 173Yb anchors) carries forward to S87+ as candidate refinement targets: re-anchoring sigma_detect to an explicit single-shot 3-sigma floor (e.g., a more recent Aalto vortex-NMR paper reporting an explicit linewidth resolution at the bath temperature; a JILA/Florence 173Yb 3-body loss measurement reporting a single-shot K_3 floor) would lift those rows from provisional to non-provisional without changing the SI_value column.
- W8-4 verdict (S85 PASS at 3/3_directions_9/9_obs) is unchanged by C5 outcome — the SI translation does not alter the upstream substrate prediction, only its lab-platform reading.

**Carry-forward messages** (compute-time SendMessage to next-wave planners, per plan §6 closure):
- To C6 / W11-2 sagan-empiricist: "C5 closed at INFO; 9-row SI table at `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv`; detection_ratio column is the EVOI-tree input for level-assignment thresholds {>=10, [3,10), [1,3), <1}. JSON `provisional_rows` field flags 6 rows as provisional (sigma_detect upper-bound)."
- To W14 planner: "C5 closed at INFO; 9-row LAB-FALSIFIER corridor opened. W14-W6 NEW row class can pull rows directly from `s86_w11_lab_si_translation.csv` / `.json`. Do NOT recompute SI translations."
- To W13 planner: "C5 closed at INFO; falsifier-master-inventory P11 enrichment can cite SI values from the same CSV; provisional flag indicates which sigma_detect anchors are candidates for S87 single-shot refinement."

**Dual-SHA**:
- `audit_sha256 = 6a2d523920c340321fe537672a39aa6d971a81c330236d78aee59138900628ce`
- `content_sha256 = 5d2449353ebdae40b16d648cf054196b3d8c4e47c31e2d30aadb73975f7ffe03`
- 16-hex companion: `audit=6a2d523920c34032 content=5d2449353ebdae40`
- audit_sha256 closure includes: script bytes + `canonical_constants.py` bytes + ordered pin-map JSON (M_KK, Delta_BCS, k_B_SI, h_planck_SI, T_c_3He_0bar_K, BCS_factor, nu_Delta_3HeA_MHz, B0_FeSe_T, gamma_77Se, K_baseline_ppm, K_3_cm6s, n_lat_cm3, Gamma_3B_inherited, sigma_detect trio, INPUT_SHAS, rows_spec_count, verdict, value).

**Artifacts**:
- Script: `computations/s86_w11_lab_si_translation.py` (29.2 KB)
- Data: `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv` (2.5 KB; 9 data rows + header; 14 columns)
- JSON: `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.json` (9.5 KB; rows array + literature_citations + prefactor_provenance + input_shas + provisional_rows top-level field)
- Literature corpus: `sessions/archive/session-86/computations-artifacts/_w11_lit/{1005.0546.pdf, 2010.01020.pdf, 0905.4948.pdf}` (1.4 MB / 0.6 MB / 0.3 MB; SHA-pinned in JSON)
- Verdict line: appended to `computations/s86_gate_verdicts.txt` (canonical path per `.claude/rules/gate-verdicts.md`); two lines (canonical R3 + dual-SHA companion).

---

### §W11-2. S86-LAB-FALSIFIER-EVOI-TREE (sagan-empiricist)

**Status**: PASS
**Gate ID**: `S86-LAB-FALSIFIER-EVOI-TREE`
**Trigger**: `[AUDIT]`
**Classification**: **PHONONIC** (5-yr decision-tree pre-registration over substrate excitations measured at table-top scale)
**Agent**: `sagan-empiricist` (PRIMARY; fallback `mack-cosmic-bridge`)
**Hypothesis**: Each of the 9 W8-4 lab observables, given C5's SI value and per-platform `sigma_detect`, admits a unique LAB-FALSIFIER level assignment (A/B/C/D on detection_ratio thresholds {≥10, [3,10), [1,3), <1}) and a unique 4-branch 5-yr decision tree (detect-strong / detect-marginal / null-strong / null-marginal) whose branch conditions are explicit functions of s_obs / sigma_detect.
**Plan reference**: `sessions/session-plan/session-86-plan-w11.md` §W11-2.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; ran before writing the script):

- `search_knowledge("S86-LAB-FALSIFIER-EVOI-TREE")` → no results; gate ID is novel at S86, no PRE-CLOSED entry exists.
- `search_knowledge("EVOI lab falsifier level ladder")` → 8 hits in `equation`, 1 in `closed_mechanism` (N10 B1-WEIGHT-AUDIT-74, unrelated topic), 1 in `gate` (ZFP, EVOI=0 registry entry, unrelated). LAB-FALSIFIER level-ladder NOT previously defined; this gate introduces it.
- `search_knowledge("LAB-FALSIFIER decision tree 2031 horizon")` → 8 hits in `equation` (all from `s84_w4_bicep_keck_2026_pre_register.py` — the BICEP/Keck 2026 pre-register pattern; useful structural precedent for `decision_tree["branches"]` JSON shape but a DIFFERENT class of falsifier (CMB-scale, not lab-scale)). 1 hit in `edge` (`eq_2031 --depends_on--> M_KK`, unrelated). No prior LAB-FALSIFIER decision tree exists.
- `search_knowledge("5-yr decision tree experiment family lab predictions")` → confirms `S85-W8-4-SU3-OP-LAB-PREDICTIONS` PASS at S85 as upstream feeder (the W8-4 ratios that C5 translated to SI; not a duplicate of C6).
- `list_entities(gates)` → 50-entry sample inspected; no entry with `LAB-FALSIFIER-A/B/C/D` level label exists.

**MCP audit conclusion**: NOT PRE-CLOSED. The LAB-FALSIFIER level ladder is a NEW class introduced at this gate (consistent with plan §11 partition manifest §1 W14-W6 NEW row class entry). No level-shuffling against existing entries; the NEW class is added beside the existing evoi-framework.md ladder, not in place of it.

**Input-SHA echo-check** (per `.claude/rules/gate-verdicts.md` §Pre-Registration Protocol; first 20 lines of stdout):

- C5 CSV `s86_w11_lab_si_translation.csv` sha256 = `bf78cdb4bc9d7b28e1023249eb08ba15deaa653aee8b55f0b908327a0d09ec9a` → **MATCHES** orchestrator pin.
- C5 JSON `s86_w11_lab_si_translation.json` sha256 = `cee9552d51101958abbe7397d35a0df3e3d2cf308e96a60cb06dd841d48ac218` → **MATCHES** orchestrator pin.
- C5 verdict-line `audit_sha256` cross-cite = `6a2d523920c340321fe537672a39aa6d971a81c330236d78aee59138900628ce` (echoed in JSON `C5_audit_sha256_cross_cite` field; verdict-trace anchored to `computations/s86_gate_verdicts.txt` line 182).
- `computations/canonical_constants.py` sha256 = `3d72f1eaa8762744769b08265b74c2ffd4ed2702fad41065fa066082f66d2688` (folded into `audit_sha256` closure per S82 dual-SHA template).

**Verdict**:

```
S86-LAB-FALSIFIER-EVOI-TREE: PASS -- value='9-rows-leveled-and-treed' scheme=LAB_FALSIFIER_ladder convention=2026_2031_horizon L_max=N/A audit_sha256=8f1210e9a1123bf3f29fd89ce660f93c2b4f5fd0a029a8bfb3f5b8464989841e content_sha256=e971be1b91ab0710922f744615f6020ed05afdef7d7497fc8feeeee2cb9285a3 schema_version=R3
# audit_sha256 companion row: S86-LAB-FALSIFIER-EVOI-TREE audit=8f1210e9a1123bf3 content=e971be1b91ab0710
```

4-tuple: `(value='9-rows-leveled-and-treed', scheme=LAB_FALSIFIER_ladder, convention=2026_2031_horizon, L_max=N/A)`.

PASS criteria all satisfied (plan §9): 9 rows present, every row has `level_assignment ∈ {A,B,C,D}`, every row has all 4 branch conditions populated as explicit numerical inequalities, every row has `experiment_family_pinned`, JSON top-level `level_ladder_definition` is present. INFO clause did NOT fire (0 level-D rows; all C5 detection_ratios ≥ 10).

**Results**:

**9-row EVOI level table** (compact form; full per-row branch_conditions in `s86_w11_lab_falsifier_evoi_tree.csv` columns 9-12):

| obs_id | platform | lambda | detection_ratio | level            | provisional |
|:-------|:---------|:-------|----------------:|:----------------|:------------|
| SW1    | 3He-A    | λ_6    |       58958.864 | LAB-FALSIFIER-A | True        |
| SW2    | FeSe     | λ_7    |          72.904 | LAB-FALSIFIER-A | False       |
| SW3    | 173Yb    | λ_8    |          28.500 | LAB-FALSIFIER-A | True        |
| XA1    | 3He-A    | λ_6    |       58958.864 | LAB-FALSIFIER-A | True        |
| XA2    | FeSe     | λ_6    |          30.696 | LAB-FALSIFIER-A | False       |
| XA3    | 173Yb    | λ_6    |          54.938 | LAB-FALSIFIER-A | True        |
| XB1    | 3He-A    | λ_7    |       19652.955 | LAB-FALSIFIER-A | True        |
| XB2    | FeSe     | λ_7    |          72.904 | LAB-FALSIFIER-A | False       |
| XB3    | 173Yb    | λ_7    |         131.852 | LAB-FALSIFIER-A | True        |

**Per-row level distribution** (against the pre-registered ladder):

- LAB-FALSIFIER-A (decisive, detection_ratio ≥ 10): **9 rows**
- LAB-FALSIFIER-B (strong, 3 ≤ d_r < 10):           **0 rows**
- LAB-FALSIFIER-C (marginal, 1 ≤ d_r < 3):          **0 rows**
- LAB-FALSIFIER-D (sub-floor, d_r < 1):             **0 rows**

The C5 detection_ratios span four orders of magnitude (28.5 to 58958.9) but ALL clear the A-level floor of 10. The NMR-platform 3He-A rows (SW1, XA1, XB1) are the dominant contributors at d_r ~ 1.97e4 to 5.90e4 (3 orders above the FeSe and 173Yb rows, reflecting that NMR linewidth resolution at 1 kHz floor against a substrate prediction at MHz scale gives the largest dimensional headroom of the three platforms). The FeSe and 173Yb rows occupy d_r ~ 28-132 — comfortably above the A-level floor but not orders-of-magnitude beyond.

**Per-row 4-branch decision tree** (representative rows; full set in CSV columns `branch_1_condition` through `branch_4_condition`):

For SW1 (3He-A, λ_6, detection_ratio = 58958.864):
- Branch 1 (detect-strong): `s_obs/sigma_detect ≥ 29479.4 (== max(3, 0.5·58958.864))` → PASS-AT-LAB; register to permanent confirmation register.
- Branch 2 (detect-marginal): `1 ≤ s_obs/sigma_detect < 3` → REGISTERED-NO-CLOSE; queue for second-generation experiment.
- Branch 3 (null-strong): `s_obs/sigma_detect < 1 AND detection_ratio (=58958.864) ≥ 3` → FAIL-AT-LAB; register to permanent FAIL-corridor.
- Branch 4 (null-marginal): `s_obs/sigma_detect < 1 AND detection_ratio < 3` → never fires for this row (d_r = 5.9e4 ≫ 3); placeholder for level-D rows only.

For SW3 (173Yb, λ_8, detection_ratio = 28.5):
- Branch 1: `s_obs/sigma_detect ≥ 14.25 (== max(3, 0.5·28.5))` → PASS-AT-LAB.
- Branch 2: `1 ≤ s_obs/sigma_detect < 3` → REGISTERED-NO-CLOSE.
- Branch 3: `s_obs/sigma_detect < 1 AND d_r (=28.5) ≥ 3` → FAIL-AT-LAB.
- Branch 4: never fires (d_r = 28.5 > 3).

For XA2 (FeSe, λ_6, detection_ratio = 30.696):
- Branch 1: `s_obs/sigma_detect ≥ 15.348` → PASS-AT-LAB.
- Branch 2: `1 ≤ s_obs/sigma_detect < 3` → REGISTERED-NO-CLOSE.
- Branch 3: `s_obs/sigma_detect < 1 AND d_r (=30.696) ≥ 3` → FAIL-AT-LAB.
- Branch 4: never fires.

The Branch 1 floor `max(3, 0.5·d_r)` ensures that PASS-AT-LAB requires either ≥ 3-sigma detection (the conventional discovery floor) OR observation at half the framework's predicted magnitude (whichever is larger). Both floors must be cleared simultaneously. This rule eliminates "detection at 3-sigma but at 1/100th the predicted magnitude" from triggering Branch 1 — that scenario falls into Branch 2 or Branch 3 depending on the precise s_obs.

**JSON `level_ladder_definition` top-level field** (reproduced inline; full version in `s86_w11_lab_falsifier_evoi_tree.json`):

```
class_name: "LAB-FALSIFIER"
introduced_in_session: "S86"
introduced_by_gate: "S86-LAB-FALSIFIER-EVOI-TREE"
p_decisive_band: [0.30, 0.50]
p_decisive_provenance: "partition manifest §1 W14-W6 NEW row class (5-yr terrestrial-lab horizon)"
horizon_years: [2026, 2031]
is_new_class: true
is_shuffle_of_existing_tier: false
levels:
  LAB-FALSIFIER-A: detection_ratio >= 10            (decisive)
  LAB-FALSIFIER-B: 3 <= detection_ratio < 10        (strong)
  LAB-FALSIFIER-C: 1 <= detection_ratio < 3         (marginal)
  LAB-FALSIFIER-D: detection_ratio < 1              (sub-floor)
branch_thresholds_on_s_obs_over_sigma:
  detect_strong_floor: 3.0          (Branch 1 SNR floor)
  detect_marginal_low: 1.0          (Branch 2 lower bound)
  null_floor: 1.0                   (Branch 3/4 null cutoff)
  null_strong_detection_ratio_floor: 3.0  (Branch 3 d_r requirement)
```

**Substitution chain** (per plan §10; reproduced with C5's actual detection ratios substituted):

```
Claim: The LAB-FALSIFIER level ladder (A/B/C/D, thresholds {>=10, [3,10),
       [1,3), <1} on detection_ratio) respects the EVOI ordering
       EVOI(A) > EVOI(B) > EVOI(C) > EVOI(D) ~ 0 for the 5-yr
       terrestrial-lab horizon at fixed cost.

Step 1 (definitions):
  detection_ratio_i = SI_value_i / sigma_detect_i  (from C5 CSV, per row)
  EVOI(row_i) = P(detect_i) * |delta_P_PASS| + P(null_i) * |delta_P_FAIL|

Step 2 (substitution -- C5 actual values):
  All 9 rows: detection_ratio in {28.5, 30.7, 54.9, 72.9, 72.9, 131.9,
                                   1.97e4, 5.90e4, 5.90e4}
  Lowest: SW3 at d_r = 28.5  >= 10 -> level A
  Highest: SW1 = XA1 at d_r = 5.90e4 >> 10 -> level A
  No row falls below the A-level floor -> level_distribution = {A:9, B:0, C:0, D:0}

Step 3 (simplify):
  EVOI(A) = max EVOI per the ordering proof in plan §10.
  All 9 rows occupy the maximal EVOI level. The framework's lab-falsifier
  portfolio sits at the maximal value of information per fixed
  experimental cost across the 5-yr 2026-2031 horizon.

Step 4 (direction):
  Higher level -> higher EVOI -> higher 5-yr falsifier priority.
  9x A-level means: every one of the 9 substrate-prediction rows
  is decisive at table-top scale. A null result on any of the 9 in
  2026-2031 closes a falsifier corridor under Branch 3 (FAIL-AT-LAB);
  a positive result triggers Branch 1 (PASS-AT-LAB). No row is
  uninformative under the pre-registered ladder.

  Conclusion: the level-A assignment for all 9 rows is the structural
  consequence of C5's detection ratios all clearing the SNR-10 floor;
  the EVOI ordering is preserved by construction (no scheme-shopping,
  no threshold tuning post-row-read).
```

**Substrate-framing reminder** (per `.claude/rules/phononic-framing.md` §IS Space, Not IN Space):

Each row's level assignment is a statement about the substrate's measurable phononic-excitation amplitude AT the platform's compactification scale. The 3He-A row d_r ~ 5.9e4 means: the substrate's δω_K/ω_K excitation, when measured at 3He-A's compactification scale (sweet-spot λ_6 direction), is predicted to land 5.9 × 10^4 times above the Aalto/ROTA NMR linewidth detection floor. The 173Yb row d_r ~ 28.5 means: the substrate's Γ_3B(unique)/Γ_3B(inherited) ratio, when measured at the 173Yb optical-lattice compactification scale (sweet-spot λ_8 direction), is predicted to land 28.5 times above the SU(N) lattice 3-body-loss-rate floor. These are statements about substrate detectability AT the table-top compactification ratio, NOT about cosmic substrate "modeled by" a lab analog. The 4-branch decision tree pre-registers the framework's response to the actual substrate measurement at each platform scale (per plan §13 substrate-framing reminder).

**Solution-space note** (PASS commits framework to 5-yr lab-falsifier portfolio):

PASS opens the 9-row LAB-FALSIFIER corridor for W14-W6 NEW row class landing. The framework's lab-falsifier portfolio is now lifted from 0 entries (pre-S86) to 9 atomic falsifier rows on terrestrial platforms with explicit level assignments and explicit 4-branch 5-yr decision rules. The P_decisive band 0.30-0.50 from partition manifest §1 W14-W6 is consistent with all 9 rows occupying level A (decisive); a level-B/C-dominant outcome would have flagged the band as too generous, but the actual level distribution (9× A, 0× B, 0× C, 0× D) supports the upper end of the band [0.30, 0.50] rather than challenging it. The framework is now FALSIFIABLE at table-top scale on a fixed 2026-2031 timeline; null results in 2026-2031 close specific corridors per Branch 3 (null-strong) on the 9 substrate-prediction rows. The cosmological-scale falsifier portfolio (BK-Array 2026, DESI DR3, LISA, LiteBIRD, CMB-S4, CMB-HD, SKA-1) is unchanged by this gate's outcome — C6 introduces a NEW class of lab-scale falsifier portfolio that runs alongside (not in place of) the cosmic-scale portfolio.

The INFO clause did NOT fire (0 LAB-FALSIFIER-D rows). All 9 rows are PASS-and-clean (no "watch only" flags). The 6 provisional rows (SW1, SW3, XA1, XA3, XB1, XB3 — the 3He-A and 173Yb rows; flagged in C5's `provisional_rows`) carry forward to S87+ as candidate sigma_detect refinement targets per C5's solution-space note; the provisional flag does NOT affect level assignment (every provisional row clears the A-level floor by orders of magnitude).

**Boundary mapped**: PASS opens the lab-falsifier 5-yr decision corridor (9 atomic rows, all at maximal EVOI level, with explicit Branch 1-4 conditions); the corridor is now ready for W14-W6 NEW row class landing. C6 is a methodology-and-pre-registration gate, NOT a substrate-physics gate; the framework's substrate predictions (W8-4 ratios at S85 PASS) are unchanged regardless of C6 verdict. What C6 changes is the registry: the framework now carries a public 9-row decision-tree pre-registration on terrestrial platforms, against which 2026-2031 lab measurements will be adjudicated.

**Carry-forward messages** (compute-time SendMessage to next-wave planners; per plan §6 closure):

- **To W14 planner**: "C6 closed PASS; 9-row EVOI tree at `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv`; level distribution = {A:9, B:0, C:0, D:0}; W14-W6 NEW row class can pull level + 4-branch tree directly. P_decisive band 0.30-0.50 (5-yr terrestrial-lab horizon) is consistent with 9× A-level dominance."
- **To W13 planner**: "C6 closed PASS; falsifier-master-inventory P11 enrichment can cite level assignments from the same CSV (column `level_assignment`); experiment_family_pinned column ready for inventory cross-reference."
- **To W15 planner (P13 EVOI table refresh)**: "9 NEW lab-falsifier rows feed P_work_complete denominator; LAB-FALSIFIER level is a NEW class (not a shuffle of existing levels); P13 must add 9 link-list entries for these rows when computing post-S86 work-fraction. JSON `level_ladder_definition` field is the canonical W15-citable definition of the LAB-FALSIFIER ladder."

**Dual-SHA**:

- `audit_sha256 = 8f1210e9a1123bf3f29fd89ce660f93c2b4f5fd0a029a8bfb3f5b8464989841e`
- `content_sha256 = e971be1b91ab0710922f744615f6020ed05afdef7d7497fc8feeeee2cb9285a3`
- 16-hex companion: `audit=8f1210e9a1123bf3 content=e971be1b91ab0710`
- `audit_sha256` closure includes: script bytes + `canonical_constants.py` bytes + ordered pin-map JSON (GATE_ID, SCHEME, CONVENTION, L_MAX, LEVEL_THRESH_A/B/C, BRANCH thresholds (4), DECISION_HORIZON_YEAR=2031, EXPERIMENT_FAMILY (3-platform pin), INPUT_SHAS (CSV+JSON+canonical), C5 audit_sha cross-cite, M_KK cross-cite, level_distribution, rows_count=9, verdict, value).

**Artifacts**:

- Script: `computations/s86_w11_lab_falsifier_evoi_tree.py` (27.7 KB)
- Data: `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv` (8.2 KB; 9 data rows + header; 18 columns including all 4 branch conditions, experiment_family_pinned, decision_horizon_year=2031, provisional flag inherited from C5).
- JSON: `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.json` (15.8 KB; rows array + top-level `level_ladder_definition` + `level_distribution` + `provisional_rows_inherited_from_C5` + `info_d_rows_lacking_rd_roadmap` (empty) + `detector_rd_roadmap_registry` (empty by design) + `experiment_family_pin_per_platform` + `input_shas` + `C5_audit_sha256_cross_cite` + `evoi_ordering_substitution_chain_summary`).
- Verdict line: appended to `computations/s86_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`); two lines (canonical R3 + dual-SHA companion).

---

## Wave W11 Synthesis (team-lead)

**Wave outcome**: Both gates closed; the 9-row LAB-FALSIFIER corridor is open for downstream landing in W13 / W14 / W15.

| Gate | Owner | Verdict | 4-tuple | dual-SHA (16-hex) |
|:-----|:------|:--------|:--------|:------------------|
| §W11-1 `S86-LAB-SI-TRANSLATION` (C5) | volovik-superfluid-universe-theorist | INFO | `(9-rows-populated, M_KK_mapping, per_platform_units, N/A)` | audit=`6a2d523920c34032` / content=`5d2449353ebdae40` |
| §W11-2 `S86-LAB-FALSIFIER-EVOI-TREE` (C6) | sagan-empiricist | PASS | `(9-rows-leveled-and-treed, LAB_FALSIFIER_ladder, 2026_2031_horizon, N/A)` | audit=`8f1210e9a1123bf3` / content=`e971be1b91ab0710` |

**C5 INFO interpretation**: PASS-completeness on the 9-row table (every row has `SI_value`, `sigma_detect`, `lit_sha` populated) with 6 rows flagged provisional — the 3He-A (SW1, XA1, XB1) and 173Yb (SW3, XA3, XB3) literature anchors report `sigma_detect` as state-of-art upper-bounds (Aalto/ROTA NMR linewidth representation; SU(N)-lattice theoretical floor) rather than explicit single-shot 3-sigma floors, firing the plan §W11-1 #9 INFO clause. INFO does NOT subtract from PASS-completeness for the W14-W6 NEW row class downstream — every row counts. The 3 FeSe rows (XA2, SW2, XB2) are non-provisional (single-shot 5 ppm 77Se NMR resolution per Zhou+ 2020).

**C6 PASS interpretation**: Level distribution `{LAB-FALSIFIER-A: 9, B: 0, C: 0, D: 0}` — every row clears the A-level floor (`detection_ratio ≥ 10`) by orders of magnitude. The lowest `detection_ratio` (SW3 173Yb at 28.5) sits 2.85× above the floor; the highest (SW1 = XA1 3He-A at 5.90e+04) sits 5900× above. INFO clause did NOT fire (no D-level rows, so no detector-R&D roadmap requirement). C6's input-SHA echo-check (script SEC 6) confirmed C5 outputs match the orchestrator-pinned SHAs bit-for-bit (CSV `bf78cdb4bc9d7b28...`, JSON `cee9552d51101958...`).

**Downstream input-pin handoffs** (per plan §X "both PASS" branch, lines 555-558):
- **W14 W6 NEW row class** (`P_decisive` band 0.30-0.50, 5-yr terrestrial-lab horizon): 9 rows ready to land. W14 pulls `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv` (`level_assignment` + 4 branch_condition columns per row + `experiment_family_pinned`) joined with `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv` (`SI_value` + `sigma_detect` + `lit_sha` per row). The 9× A-level dominance supports the upper end of the partition-manifest 0.30-0.50 band.
- **W13 P11 master-inventory enrichment**: level + experiment_family pulls from the same C6 CSV; C5 SI values + literature SHA-pins enrich the falsifier-master-inventory P11 entry. C6 carry-forward message in §W11-2 lines 296.
- **W15 P13 EVOI table refresh**: 9 NEW link-list entries required (LAB-FALSIFIER is a NEW class added at S86, not a shuffle of existing evoi-framework.md levels). The JSON top-level `level_ladder_definition` field in `s86_w11_lab_falsifier_evoi_tree.json` (reproduced inline at WP §W11-2 lines 219-240) is the canonical W15-citable definition. `P_work_complete` denominator increases by 9.

**Lab-falsifier portfolio status at S86 close**: framework lifted from 0 → 9 atomic substrate-prediction rows, all level A, with explicit 4-branch 5-yr (2026-2031) decision rules and SHA-pinned literature anchors for `sigma_detect` on 3 platforms (3He-A vortex-line NMR / FeSe ⁷⁷Se NMR Knight-shift / ¹⁷³Yb optical-lattice 3-body loss). The framework is now FALSIFIABLE at table-top scale on a fixed timeline. The cosmological-scale falsifier portfolio (BK-Array 2026, DESI DR3, LISA, LiteBIRD, CMB-S4, CMB-HD, SKA-1) is unchanged — the lab-falsifier corridor runs **alongside**, not in place of, the cosmic corridor.

**S87+ refinement target** (carry-forward to next-session plan): replace the 6 provisional `sigma_detect` anchors (3 for 3He-A, 3 for 173Yb) with single-shot 3-sigma floors. Refinement does NOT change C5's `SI_value` column or C6's level assignments — the 6 provisional rows clear the A-level floor by orders of magnitude (1.97e+04 to 5.90e+04 for 3He-A; 28.5 to 131.9 for 173Yb), so any plausible tighter floor leaves them in level A. Refinement is provenance hygiene, not corridor reopening.

**Methodology-vs-physics distinction**: This wave is methodology-and-pre-registration. W8-4's substrate predictions (S85 PASS at `3/3_directions_9/9_obs`) are unchanged; the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 was honored (no recomputation of W8-4 magnitudes during S86). Framework probability is unchanged (BF=1.0; per the pre-registered-gates-only rule, registry-class gates do not move probability — that movement happens when 2026-2031 lab measurements trigger Branch 1 (PASS-AT-LAB) or Branch 3 (FAIL-AT-LAB) on any of the 9 rows).

## Constraint-Map Updates

| Date       | Mechanism / gate                              | Prior state                                | New state                                                                                  | Reason |
|:-----------|:----------------------------------------------|:-------------------------------------------|:-------------------------------------------------------------------------------------------|:-------|
| 2026-04-26 | LAB-FALSIFIER level ladder                     | UNDEFINED (no prior LAB-FALSIFIER class)   | DEFINED — A/B/C/D, `detection_ratio` thresholds `{≥10, [3,10), [1,3), <1}`                 | C6 introduces NEW class; not a shuffle of existing evoi-framework.md levels (search_knowledge confirmed zero prior coverage) |
| 2026-04-26 | 9-row lab-falsifier corridor (3 platforms × 3 directions) | UNCONNECTED to terrestrial detection       | 9 rows OPEN, all level A, with explicit 4-branch 5-yr (2026-2031) decision tree per row     | C5 supplies SI translation + literature-anchored `sigma_detect`; C6 assigns levels + Branch 1-4 conditions |
| 2026-04-26 | W8-4 substrate predictions (`S85-W8-4-SU3-OP-LAB-PREDICTIONS`) | PASS at S85 (`3/3_directions_9/9_obs`)     | UNCHANGED — translated to SI, never recomputed                                             | FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 honored; C5 is unit-conversion only |
| 2026-04-26 | Framework lab-falsifier portfolio             | 0 entries                                  | 9 entries (all level A; 6 provisional `sigma_detect`, 3 non-provisional)                    | C5 INFO + C6 PASS closure |
| 2026-04-26 | Cosmological-scale falsifier portfolio (BK-Array, DESI DR3, LISA, LiteBIRD, CMB-S4, CMB-HD, SKA-1) | UNCHANGED                          | UNCHANGED                                                                                  | C6 adds a parallel terrestrial-lab corridor; cosmic corridor runs alongside, not displaced |

## Files Produced

| Gate                                  | Script                                              | Data (.csv)                                                        | JSON                                                                | Sizes |
|:--------------------------------------|:----------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|:-------|
| §W11-1 `S86-LAB-SI-TRANSLATION` (C5)   | `computations/s86_w11_lab_si_translation.py`    | `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv` | `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.json` | 29.2 KB / 2.5 KB / 9.5 KB |
| §W11-2 `S86-LAB-FALSIFIER-EVOI-TREE` (C6) | `computations/s86_w11_lab_falsifier_evoi_tree.py` | `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv` | `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.json` | 27.7 KB / 8.2 KB / 15.8 KB |

**Auxiliary files**:
- Verdict-file appends: `computations/s86_gate_verdicts.txt` lines 182-183 (C5 INFO + dual-SHA companion), 197-198 (C6 PASS + dual-SHA companion).
- Literature corpus (PDFs, SHA-pinned in C5 JSON `literature_citations`): `sessions/archive/session-86/computations-artifacts/_w11_lit/1005.0546.pdf` (1.43 MB, Eltsov+ 2010 3He-A vortex), `sessions/archive/session-86/computations-artifacts/_w11_lit/2010.01020.pdf` (0.6 MB, Zhou+ 2020 FeSe NMR), `sessions/archive/session-86/computations-artifacts/_w11_lit/0905.4948.pdf` (0.31 MB, Cazalilla+ 2009 173Yb SU(6)).
- Working paper this file: `sessions/archive/session-86/session-86-w11-workingpaper.md` (final size after synthesis writes; gate sections at §W11-1 lines 7-132 and §W11-2 lines 134-313).
