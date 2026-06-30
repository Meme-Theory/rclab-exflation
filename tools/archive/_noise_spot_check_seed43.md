# NOISE Spot Check — 5% random sample per table

Random seed: 43 (deterministic; rerun produces identical sample).
Sample rule: max(ceil(5.0% * |NOISE|), 2) per table; tables with <= 20 NOISE include ALL entries.

## Summary

| Table | NOISE total | Sampled | AGREE | DISAGREE | BORDERLINE |
|:------|----:|----:|----:|----:|----:|
| closed_mechanisms | 26 | 2 | 2 | 0 | 0 |
| open_channels | 481 | 25 | 20 | 0 | 5 |
| theorems | 1020 | 51 | 33 | 9 | 9 |
| gates | 293 | 15 | 7 | 0 | 8 |
| data_provenance | 186 | 10 | 0 | 0 | 10 |
| session_files | 4 | 4 | 3 | 0 | 1 |
| equations | 144 | 8 | 3 | 5 | 0 |
| researchers | 2 | 2 | 0 | 0 | 2 |
| constants | 2 | 2 | 1 | 0 | 1 |
| registries | 4 | 4 | 0 | 0 | 4 |
| **TOTAL** | **2162** | **123** | **69** | **14** | **40** |

Spot-check agreement: 56.1% AGREE, 11.4% DISAGREE, 32.5% BORDERLINE.

---

## Table: closed_mechanisms  -  sampled 2 of 26 NOISE (7.7%)

### closed_10
- **name**: [Berry]Q-2
- **source_file**: sessions\archive\session-25\session-25-Investigation-Question-Efforts.md
- **Haiku NOISE reason**: Name is '[Berry]Q-2', a pure adjudication-question marker; source context shows it appears in a question table (line 22) with verdict CLOSED, but the name field itself is a fragment, not a mechanism n
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       15: 
       16: | Question | Short Title | S25 Verdict | Key Finding |
       17: |:---------|:------------|:------------|:------------|
       18: | [Einstein]Q-5 | Spectral flow in p+q > 0 | **NO** | R_K >= 12 for all tau. Lichnerowicz: lambda^2 >= 3. Zero in every sector. |
       19: | [Sagan]Q-1 | PET evaded by grading? | **NO** | gamma_9 trace = 0 by BDI. S_eff monotone at all Lambda. W1 holds. |
       20: | [Hawking]Q-1 | Multiple Euclidean saddles? | **NO** | I_E monotone decreasing (13/15 cases). No saddle competition. Closed #22. |
       21: | [Hawking]Q-3 | GSL as stabilization? | **NO** | S_spec monotone decreasing at all T. GSL selects tau=0 (wrong answer). Closed #20. |
       22: | [Berry]Q-1 | B=982.5 adiabatic breakdown? | **CLOSED** | B is quantum metric, not Berry curvature. Omega = 0 identically. Closed #19. W5. |
    ... +6 more lines

### closed_46
- **name**: W10-5
- **source_file**: sessions\session-85\session-85-gen-physicist-synthesis-w6-13.md
- **Haiku NOISE reason**: W10-5 is a bare wave/gate ID fragment, not a mechanism name; context shows it as a table row header from S85 synthesis with no descriptive mechanism label.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       67: |:-------|:--------|:------|:----------------|
       68: | W6-7 | `S85-W6-7-PETROV-NON-BD-PERT` | check_type=D | Type-D (non-block-diagonal) Petrov classification under W3 H-perturbation direction is incompatible with the AWH structure — the AWH is genuinely non-Type-D.
       69: | W7-BASELINE-HTILDE | `S85-W7-BASELINE-HTILDE-DERIVATION` | 7.86e−03 | Zubarev W1-G1-Branch-B baseline H̃ derivation does NOT close — branch-B is structurally retracted. |
       70: | W7-CC-6 | `S85-W7-CC-6` | 116.4828 | CC-6 zeta-regularized Parker-Hawking 1974 closure form FAILs at 116× threshold — reverse-direction limit is forbidden. |
       71: | W7-CC-GAMMA | `S85-W7-CC-GAMMA` | 0.9860 | CC-Γ S37-Gamma canonical against Planck2020-DR2 FAILs marginally (<1% from threshold) — Γ does not saturate the canonical convention. |
       72: | W7-CUSP-BOGOLIUBOV | `S85-W7-CUSP-BOGOLIUBOV` | −2.020 | Cusp Bogoliubov transfer-matrix BD-in-out FAILs at L_max=10 — the BD-in-out cusp formulation is structurally negative-definite (sign reversal NOT physical
       73: | W8-1 | `S85-W8-1-KFIRAS-HIDDEN-CLOSED-FORM` | 1.0350 | Kfiras hidden closed-form Interp_A primary at L_max=9 fails by 3.5% — the closed-form does not capture the substrate's actual Kfiras structure. |
       74: | W8-5 | `S85-W8-5-BDI-TCI-RESTRICTED-CORRIDOR` | gap=0.193 (9/10 reg) | AZ-BDI-TCI restricted corridor at N3=0 FAILs gap criterion — the restricted-corridor formulation is regulator-disagreement-bounded, not gap-
    ... +2 more lines

## Table: open_channels  -  sampled 25 of 481 NOISE (5.2%)

### open_643
- **name**: Stage-2 cross-pillar bridge verify (§VII.W-3.LAB STAGE-1-CANDIDATE)**: per `joint-theorem-promotion.md` 4-stage pathway, Stage-2 two-agent parallel cross-axis independent-verify is required before §VI
- **source_file**: sessions/framework/Atlas/atlas-08-open-questions.md
- **Haiku NOISE reason**: Truncated question text with no substantive content; appears to be a table-row caption or header fragment.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      236: 
      237: ## VI. S52-S88 New Questions
      238: 
      239: ### VI.A. Decisive Class (Q23-Q27, S52-S88)
      240: 
      241: | Q | Question | Session opened | Status | Resolution path | Source registry |
      242: |:--|:---------|:---------------|:-------|:----------------|:-----------------|
      243: | **Q23** | **TRANSIT-PS-67 / Stage-2 framework cosmology adjudication**: full Bogoliubov power spectrum through the τ-fold; resolves α_s, A_s normalization, n_s(k) simultaneously. Replaces Q1 EFOLD-MAPPING-52 as 
    ... +2 more lines

### open_7
- **name**: Window-8
- **source_file**: sessions\session-88\atlas-uplift-materials\atlas-05-walls-doors-windows-materials.md
- **Haiku NOISE reason**: ID-only entry 'Window-8'; despite detail_2 mentioning 'BBN-VOLOVIK-67', the name field is just the ID fragment.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       79: 
       80: ### 2c. Windows opened S52-S88
       81: 
       82: A window is a constraint currently traversable: a conditional PASS pending one more computation, a live-watch detector horizon, or an open observational gate.
       83: 
       84: | window-id | conditional-PASS condition | falsifier protocol | detection horizon (years from 2026-05-09) | current σ |
       85: |:----------|:---------------------------|:-------------------|:-------------------------------------------|:----------|
       86: | Window-7 | FUNCTIONAL-SELECT-67: which spectral functional generates n_s? Resolution determines whether n_s = 0.9595 (sqrt(x) cutoff) is canonical OR scheme-dependence persists across regulators (eps_H sign reve
    ... +4 more lines

### open_247
- **name**: Combined conservative
- **source_file**: sessions\session-62\session-62-results-workingpaper.md
- **Haiku NOISE reason**: Conservative estimate label from combined-analysis table; not a scientific tension.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
     1277: 
     1278: | Route | Best Ratio | Physical? | Mechanism |
     1279: |:------|:----------|:----------|:----------|
     1280: | Tree (S61) | 1.6 | Yes | Jensen scale factors |
     1281: | (a) KK modes | 6670 | Model-dependent | Sector-resolved overlaps |
     1282: | (b) RG | 1.0x amplification | Yes | Quasi-fixed point kills amplification |
     1283: | (c) BCS | 1.03 | Yes | O(1) additive correction |
     1284: | Combined optimistic | 6879 | Model-dependent | Multiplicative: a x b x c |
    ... +9 more lines

### open_473
- **name**: FWD-C5 bridge family
- **source_file**: sessions\session-91\session-91-w5-workingpaper.md
- **Haiku NOISE reason**: Catalog update notation (C1→C5) without active tension.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     1214: 
     1215: ### Constraint-map updates (corridors closed, opened, preserved)
     1216: 
     1217: **Corridors closed in-session**:
     1218: - §VII.AV PROXY-REFINEMENT route (ii) FULL-PV: SCHEMATIC Casimir-bound `L^{-α=3}` envelope FALSIFIED. The corridor "SCHEMATIC and FULL-PV reproduce the same algebraic envelope" is excluded.
     1219: - §VII.AU.OP-PROJ Level-2-DEFORMABLE: identity holds Sage-Q exact across τ ∈ {0.18, 0.19, 0.20} → Level-2-DEFORMABLE corridor closed.
     1220: - §VII.AX slot allocation: previously free; now occupied by §VII.AX.OP-PROJ STAGE-1-CANDIDATE entry. State-projection companion slot §VII.AX.STATE-PROJ queued for S92+.
     1221: - n_PBH band-edge tension at L_max=10 (S89 W1-4 INFO): extended through L_max=14 with sub-band membership PASS; the corridor "n_PBH structural-central remains outside upper-22.6%-conjunct at canonical L_max" is ex
    ... +6 more lines

### open_425
- **name**: A4 graded reality (KO-dim 6)
- **source_file**: sessions\session-87\session-87-results-workingpaper.md
- **Haiku NOISE reason**: Table-row cell from axiom-check table (A4 KO-dim 6, truth-table status, not a real physics tension)
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
     2041: 
     2042: **Connes-Chamseddine 1996 six-axiom check at finite-L=10** (mandatory regime-VALID/MARGINAL/BREAKDOWN check per plan §989-992):
     2043: 
     2044: | Axiom | PS A_F = M_2(H) ⊕ M_4(C) verdict | Substrate basis |
     2045: |:------|:--------------------------------|:----------------|
     2046: | A1 dimension (d_spec=8) | **PASS** | KK truncation 4-mfd × 4-fiber; PS admits d=8 finite-L embedding |
     2047: | A2 order-zero `[a, JbJ⁻¹] = 0` | **PASS** | direct-sum A_F preserves commutator-vanishing on each summand |
     2048: | A3 order-one `[[D, a], JbJ⁻¹] = 0` | **PASS** | (p,q)-block diagonal D_K respects PS direct-sum block structure |
    ... +10 more lines

### open_627
- **name**: Swampland c(tau)
- **source_file**: sessions/framework/Atlas/atlas-08-open-questions.md
- **Haiku NOISE reason**: Machinery-named test of de Sitter conjecture application; no framework-internal tension documented.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      184: 
      185: ### Level 5 carry-forwards (Paasch, String, QA backlog)
      186: 
      187: | # | Item | Source |
      188: |:--|:-----|:-------|
      189: | CF11 | LOG-SIGNED-40 | S40. Signed boson-fermion log sum on 2912 eigenvalues. Uncomputed since S40 |
      190: | CF12 | PHI-GOLDEN-22 | S47 D-5. Tau sweep of (2,2)/(0,0) ratio toward golden ratio |
      191: | CF13 | Six-sequence test | S47 D-5. Zero-cost: 2912 eigenvalues on Paasch spiral |
    ... +9 more lines

### open_644
- **name**: §VII.AM Universal Lock Condition Stage-2 verify**: per `joint-theorem-promotion.md` 4-stage pathway, the 3-clause joint theorem (pixelation lock + effacement lock + Page-time lock) at §VII.AM is STAGE
- **source_file**: sessions/framework/Atlas/atlas-08-open-questions.md
- **Haiku NOISE reason**: Truncated table-row text without full question specification; status tag 'STAGE-1-CANDIDATE' only.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      237: ## VI. S52-S88 New Questions
      238: 
      239: ### VI.A. Decisive Class (Q23-Q27, S52-S88)
      240: 
      241: | Q | Question | Session opened | Status | Resolution path | Source registry |
      242: |:--|:---------|:---------------|:-------|:----------------|:-----------------|
      243: | **Q23** | **TRANSIT-PS-67 / Stage-2 framework cosmology adjudication**: full Bogoliubov power spectrum through the τ-fold; resolves α_s, A_s normalization, n_s(k) simultaneously. Replaces Q1 EFOLD-MAPPING-52 as 
      244: | **Q24** | **Stage-2 cross-pillar bridge verify (§VII.W-3.LAB STAGE-1-CANDIDATE)**: per `joint-theorem-promotion.md` 4-stage pathway, Stage-2 two-agent parallel cross-axis independent-verify is required before §V
    ... +1 more lines

### open_720
- **name**: CUTOFF-SA-37
- **source_file**: sessions/framework/ARCHIVE/framework-bbn-hypothesis.md
- **Haiku NOISE reason**: CUTOFF-SA-37 is archived hypothesis ID placeholder, superseded, no live gate.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
        5: Reason: BBN hypothesis from S36 transit-dynamics era; superseded by parametric-amplification framework + cosmological mapping; modern accounting at atlas-07 §VII registry slots
        6: ---
        7: 
        8: # Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade
        9: 
       10: **Date**: 2026-03-08
       11: **Source**: Session 36 discussion (post-W4-A/W4-B needle hole results)
       12: **Status**: HYPOTHESIS (pre-computational, conceptual framework)
    ... +9 more lines

### open_2
- **name**: W2 C10 verdict line (INFO, value 280743+0j, analytic-continuation, off-pole-Hankel)
- **source_file**: sessions\session-86\seeds\_seed-w10.md
- **Haiku NOISE reason**: Verdict-line summary (gate C10 result ref), not an open channel.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
       15: **Type**: 2-agent workshop
       16: 
       17: **Suggested agents**: connes-ncg-theorist, lizzi-spectral-functional-theorist
       18: 
       19: **Rounds**: 3 (R1 lizzi steelman the Mellin-cone scheme + diagnose; R2 connes respond with finite-triple compatibility analysis; R3 converge on repair-or-no-go)
       20: 
       21: **Context the workshop will need**:
       22: - W2 C9 verdict line (FAIL, value 9.456, MB-Connes-Moscovici, SD-subtracted): `computations/s86_gate_verdicts.txt:95-96`
    ... +10 more lines

### open_467
- **name**: JSON detail
- **source_file**: sessions\session-88\session-88-w4a-workingpaper.md
- **Haiku NOISE reason**: JSON file metadata (3,568 bytes); output-artifact notation, not an open research channel.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
      107: **Dual-SHA**:
      108: - `audit_sha256` = `63acc9cd17a2323d30f6c722792ff839400a9378e8307b496d1d456b1f30d731`
      109: - `content_sha256` = `1912cc503085cf8b5abbcf7a184d10f385ebd3928275fd34691b930ca1f606d8`
      110: - workshop_precedent_sha (S87 W1a-5 workshop) = `65e82247283d29aa…`
      111: 
      112: **Artifacts**:
      113: - Script: `computations/s88_w4a_a0_m2_backward_rescue_theorem.py` (24,398 bytes)
      114: - Data: `computations/s88_w4a_a0_m2_backward_rescue_theorem.npz` (3,460 bytes; keys `algebras_tested`, `a0_verdict_per_algebra`, `m2_verdict_per_algebra`, `commutator_residuals`, `theorem_verdict`, `substrate_bloc
    ... +9 more lines

### open_588
- **name**: Step 2 (substitution)
- **source_file**: sessions\session-82\session-82-mack-synthesis.md
- **Haiku NOISE reason**: Step 2 substitution is numerical bookkeeping intermediate, not an open question.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
       23: ## II. Falsifier Channel Catalog
       24: 
       25: ### II.A. α_f_NL = 0 across 5 decades k (W3-4)
       26: 
       27: **Framework prediction** (S82 §VI.D): f_NL^{GGE,fabric}(k) = 0.054702 exactly across k ∈ {10⁻⁴, 10⁻³, 10⁻², 10⁻¹, 10⁰} Mpc⁻¹ (W2-15 phase-alignment k-scan confirmed 0% variation across 5 decades).
       28: 
       29: **Substitution chain (direction)**:
       30: - Step 1 (definition): α_f_NL := d ln f_NL / d ln k
    ... +9 more lines

### open_509
- **name**: SM quantum numbers from Psi_+ = C^16
- **source_file**: sessions\archive\session-23\session-23a-synthesis.md
- **Haiku NOISE reason**: SM quantum numbers is a PERMANENT proven result, not an open channel; misclassified as open.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      254: 
      255: ## VIII. What Survives
      256: 
      257: The K-1e closure is specific to the BCS condensation mechanism. Everything proven at machine epsilon is unaffected:
      258: 
      259: | Result | Session | Status |
      260: |:-------|:--------|:-------|
      261: | KO-dim = 6 | 7-8 | PERMANENT |
    ... +9 more lines

### open_593
- **name**: W7-BASELINE-HTILDE
- **source_file**: sessions\session-85\session-85-gen-physicist-synthesis-w6-13.md
- **Haiku NOISE reason**: Gate ID and numerical value from table row; machinery-parameter entry
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       61: 
       62: ### (d) Surviving FAILs — corridors closed in W6-W13 (constraint-map gains, not framework defects)
       63: 
       64: 11 FAILs across W6-W13. Each is a localization of where a corridor terminates, not a deficiency of the agent or the gate.
       65: 
       66: | Source | Gate ID | Value | Corridor closed |
       67: |:-------|:--------|:------|:----------------|
       68: | W6-7 | `S85-W6-7-PETROV-NON-BD-PERT` | check_type=D | Type-D (non-block-diagonal) Petrov classification under W3 H-perturbation direction is incompatible with the AWH structure — the AWH is genuinely non-Type-D.
    ... +6 more lines

### open_119
- **name**: V_FR overlay
- **source_file**: sessions\archive\session-25\session-25-Workshop-connes-results.md
- **Haiku NOISE reason**: Computational to-do item (V_FR overlay); belongs to 'ITEMS REMAINING NOT COMPUTED' task list, not open_channels.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      332: The NCG framework does NOT provide a mechanism for modulus stabilization on this geometry. The spectral action principle (Paper 07) predicts a monotone effective potential. The random NCG integral (Paper 14) predi
      333: 
      334: ---
      335: 
      336: ## ITEMS REMAINING NOT COMPUTED
      337: 
      338: | Item | Reason | Feasibility |
      339: |------|--------|-------------|
    ... +10 more lines

### open_516
- **name**: DNP instability for tau < 0.285
- **source_file**: sessions\archive\session-23\session-23a-synthesis.md
- **Haiku NOISE reason**: Stability criterion with status marker 'PERMANENT'; closed mechanism classification.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      262: | SM quantum numbers from Psi_+ = C^16 | 7 | PERMANENT |
      263: | [J, D_K(tau)] = 0 (CPT hardwired) | 17a | PERMANENT |
      264: | g_1/g_2 = e^{-2tau} | 17a | PERMANENT |
      265: | 67/67 Baptista geometry checks | 17b | PERMANENT |
      266: | D_K block-diagonality theorem | 22b | PERMANENT |
      267: | Three algebraic traps | 20b, 22c | PERMANENT |
      268: | Perturbative Exhaustion Theorem (H1-H5) | 22c | PERMANENT (H4/H5 still hold) |
      269: | phi_paasch at tau = 0.15 | 12, 22a | PERMANENT |
    ... +9 more lines

### open_455
- **name**: `s86-cluster-results.md` (memory)
- **source_file**: sessions\session-87\session-87-results-workingpaper.md
- **Haiku NOISE reason**: Memory file reference with SHA256; machinery artifact ID without physics tension.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     8555: - Composite-collapse: regime=VALID + sign=FAIL ⇒ composite **FAIL** (sign-failure branch dominates per gate-verdicts.md §"S87+ canonical form").
     8556: - Verdict file: `computations/s87_gate_verdicts.txt` (canonical line + dual-SHA companion + 3-tuple companion all appended).
     8557: 
     8558: **Input SHA-256 pins (computed at runtime, embedded in .npz `input_pin_map_json` field):**
     8559: - `s84_spectrum_cache_L12_tau019.npz`: `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`
     8560: - `canonical_constants.py`: `d56d57c12e706167f482cb2029d7e1154bde0672303d26a8348a5404aedac672`
     8561: - `elimination-bulletins.md`: `ebce7b558cff0a51b6482e3552d61b5659b208d70ff48bdf8f5706d629cef155`
     8562: - `permanent-results-registry.md`: `5a38f1756c34d2c25169183c8bfe216c0c1875b382ed6ff0d85915cf863cdabc`
    ... +8 more lines

### open_569
- **name**: Lefschetz n* = 60 promoted to permanent** (W3-C)
- **source_file**: sessions\session-75\session-75-tesla-synthesis.md
- **Haiku NOISE reason**: Status word 'promoted to permanent' with verification range; closed mechanism, not active tension.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      156: ### 4.1 Opened
      157: 
      158: | Item | Result | Gate |
      159: |:-----|:-------|:-----|
      160: | **A_s conversion factor** (W1-E) | f_conv from first principles, 0.12 OOM residual | PASS |
      161: | **n_s from non-power-law H(tau)** (W1-I) | n_s = 0.9649, Planck exact, with mu_eff = 0.0102 | PASS |
      162: | **Emergent c_light from a_2 + a_4** (W3-L) | c_Gold = 0.915 M_KK, 3-speed hierarchy verified | PASS |
      163: | **N_eff post-thermalization** (W3-M) | N_eff = 3.044 exactly, GGE erased by 10^{14} e-folds | PASS |
    ... +10 more lines

### open_426
- **name**: A5 Poincaré duality
- **source_file**: sessions\session-87\session-87-results-workingpaper.md
- **Haiku NOISE reason**: Table-row cell from axiom-check table (A5 Poincaré duality, truth-table status, not a real physics tension)
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
     2042: **Connes-Chamseddine 1996 six-axiom check at finite-L=10** (mandatory regime-VALID/MARGINAL/BREAKDOWN check per plan §989-992):
     2043: 
     2044: | Axiom | PS A_F = M_2(H) ⊕ M_4(C) verdict | Substrate basis |
     2045: |:------|:--------------------------------|:----------------|
     2046: | A1 dimension (d_spec=8) | **PASS** | KK truncation 4-mfd × 4-fiber; PS admits d=8 finite-L embedding |
     2047: | A2 order-zero `[a, JbJ⁻¹] = 0` | **PASS** | direct-sum A_F preserves commutator-vanishing on each summand |
     2048: | A3 order-one `[[D, a], JbJ⁻¹] = 0` | **PASS** | (p,q)-block diagonal D_K respects PS direct-sum block structure |
     2049: | A4 graded reality (KO-dim 6) | **PASS** | (ε, ε', ε'') = (+1, +1, −1) preserved under M_2(H) ⊕ M_4(C) |
    ... +9 more lines

### open_60
- **name**: C-D (dilution / Volovik H²-scaling)
- **source_file**: sessions\permanent-results-registry.md
- **Haiku NOISE reason**: C-D (DILUTION-CC-66) is marked PASS already realized; closed result, not open channel.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
    15408: 
    15409: ### Surviving CC-suppression corridors (post-F_4-MB-closure)
    15410: 
    15411: Three corridors survive the F_4 wall by axis-disjointness:
    15412: 
    15413: | Corridor | Mechanism | F_4 dependence | Status post-C9 |
    15414: |:---------|:----------|:---------------|:---------------|
    15415: | C-Q (q-theory equilibrium) | dE/dq = μ ⇒ ρ_vac → 0 at q*; dE_ZP/dq > 0 monotone (S62 theorem permanent) | NO | OPEN; sole survivor on Axis_substrate_density (per volovik) |
    ... +10 more lines

### open_77
- **name**: M_3(ℂ)
- **source_file**: sessions\session-87\workshops\s87-a0-r-protection-m2-biconditional.md
- **Haiku NOISE reason**: Algebraic element identifier ('M_3(ℂ)') with χ-killed projection reference—is a notation for matrix algebra structure, not a physics tension or observational channel.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
        9: **Sage symbolic cross-check**: outer commutator [[D_kern, π(a)], π(b)] structurally non-zero on the kernel block; ‖outer‖_F = 2√2 on diag(1,2)/diag(3,5) test pair
       10: 
       11: ---
       12: 
       13: ## R1 (connes opening; Reading-A defender)
       14: 
       15: ### Steelman of Reading-B (volovik's position; what I'm arguing against)
       16: 
    ... +6 more lines

### open_553
- **name**: Multifield delta-N conversion
- **source_file**: sessions\session-67\session-67-synthesis.md
- **Haiku NOISE reason**: Table row machinery parameter (0.80 OOM gate result, not a live tension).
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      120: 
      121: The Volovik CC mechanism is now structurally complete with no remaining obstructions.
      122: 
      123: ### 4d. Amplitude Gap — 0.80 OOM Remaining
      124: 
      125: | Stage | A_s gap | Computation |
      126: |:------|:--------|:------------|
      127: | Transit production | 15.1 OOM | W1-A: |beta_k|^2 ~ O(1) saturated |
    ... +9 more lines

### open_795
- **name**: 2040s
- **source_file**: sessions/framework/registry/pre-registered-observations.md
- **Haiku NOISE reason**: Decade label '2040s' from timeline; machinery parameter only, no active test.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       15:          Hyper-K first     mass ordering
       16: 2029 ─── Euclid DR1        f·σ_8, ISW, w(z)     ISW TRACKING (marginal)
       17: 2030 ─── JUNO full         mass ordering (3σ+)
       18:          Euclid DR2        ISW tomographic       SNR ~ 1.6 on c_s²=0
       19: 2032 ─── DUNE full         mass ordering (5σ)   DEFINITIVE NO/IO
       20: 2034 ─── LiteBIRD full     r, n_T               24σ DETECTION (necessary, not sufficient)
       21:          CMB-S4 full       r, n_s, α_s, f_NL    8.1σ on r; f_NL undetectable
       22: 2035 ─── LISA early        Ω_GW (domain walls)  STRUCTURAL TEST
    ... +9 more lines

### open_691
- **name**: Gates FAILED / NOT FIRE
- **source_file**: sessions\framework\registry\constraint-mega-matrix.md
- **Haiku NOISE reason**: Table-row summary of gate counts and categories without substantive tension or decision point.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      370: ## VIII. CLOSED vs OPEN SCORECARD (S66 State)
      371: 
      372: | Category | Count | Examples |
      373: |:---------|:------|:--------|
      374: | **Structural walls** | 10 + 3 candidates | W1-W10 + R-monotonicity, a_0/a_2 trap, frustration triangle |
      375: | **Closed mechanisms** | 141+ | All perturbative, BCS, FR, instanton-Kapitza, CC staircase, q-theory, unimodular, leptogenesis, skyrmion, B/F asymmetry, EIH, Mott, swampland, ... |
      376: | **Hard closes fired** | 12+ | K-1e, V-1, L-1, B-30a/min/nck, B-31nck, CUTOFF-SA-37, EFOLD-MAPPING-52, CC-COMBO-64, QTHEORY-NPAIR-66, AMPLITUDE-NORM-66 |
      377: | **Gates PASSED** | ~30 | KO-dim, CPT, block-diag, phi, BCS chain (KC-1-5), I-1, KZ-NS-62, DILUTION-CC-66, TENSOR-BURST-64, Omega_DM, sin^2 theta_W, M_W, proton decay, Delta N_eff |
    ... +7 more lines

### open_456
- **name**: Verdict-line
- **source_file**: sessions\session-87\session-87-results-workingpaper.md
- **Haiku NOISE reason**: Verdict-line file reference; verdict-line summary caption without physics tension.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     8561: - `elimination-bulletins.md`: `ebce7b558cff0a51b6482e3552d61b5659b208d70ff48bdf8f5706d629cef155`
     8562: - `permanent-results-registry.md`: `5a38f1756c34d2c25169183c8bfe216c0c1875b382ed6ff0d85915cf863cdabc`
     8563: - `s86-cluster-results.md` (memory): `3f56eb944edf4862d7934848380932607b71ffe56d30e013c34ca6cb379599d6`
     8564: 
     8565: **Artifacts (all on disk, verified):**
     8566: - Script: `computations/s87_w10_bulletin_3_rescue_residual.py` (25,081 bytes)
     8567: - Data: `computations/s87_w10_bulletin_3_rescue_residual.npz` (12,008 bytes; full input-pin-map JSON embedded for closure-hash audit)
     8568: - Plot: `computations/s87_w10_bulletin_3_rescue_residual.png` (69,308 bytes; left panel L_max-convergence vs r_anchor; right panel NROY-cascade composition residual at L=12)
    ... +8 more lines

### open_437
- **name**: Producing script
- **source_file**: sessions\session-87\session-87-results-workingpaper.md
- **Haiku NOISE reason**: Producing script metadata ('~286 lines; append-only Python writer'); machinery documentation.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
      128: - Level-3 < Level-2 satisfaction explicit in the registry block: `Level-3 (8.066e-28) < Level-2 (1e-12)  =>  PASS`.
      129: - Pre-write registry SHA: `00d71ad6bc413811...`. Post-write registry SHA: `d8fb3333974c52e5...`. Append-only Python writer per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer
      130: 
      131: **Substrate framing**: The Mellin-Strip residue at s=3 IS a substrate-IS observable on the finite spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` — not a quantity living "in" an external s-plane container. The
    ... [truncated]

## Table: theorems  -  sampled 51 of 1020 NOISE (5.0%)

### proven_1431
- **name**: f_NL
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: 0.014 | CONSISTENT with Planck (far below bound) | 42
- **Haiku NOISE reason**: Table cell extract (status code '42'; single quantitative value '0.014' with status tags, not a theorem statement)
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      189: | Fermi-surface lock: v^2(B2[0]) = 1/2 identically | PERMANENT | 64 W2-C | Algebraic |
      190: | a_0/a_2 trap (off-Jensen): decreasing a_2 INCREASES a_0/a_2 | PERMANENT | 64 W2-A | Candidate wall |
      191: | Spectral moment decoupling: F_{-1}(CC) vs F_{+1}(NEC) are different moments | PERMANENT | 64 W5-B | Structural |
      192: | H2 theorem: pi_ij=0 from DeWitt tracelessness (volume-preserving) | PERMANENT | 64 W3-A | Structural |
      193: | Chirality antisymmetry: {gamma_9, dD_K/dtau}=0. Chiral pairs ADD, not cancel | PERMANENT | 64 W6-B | Algebraic |
      194: | BdG Heat Kernel Factorization: K_BdG(t) = exp(-Delta^2 t) K_bare(t) | PERMANENT | 64-65 | Structural |
      195: | CC Ratio from Scalar Curvature Only: d(a_0/a_2)/ds = -(a_0/a_2)/R dR/ds | PERMANENT | 65 W1-B | Structural |
      196: | B/F Spectral Asymmetry = 0: |A|=0 EXACTLY on pure Riemannian triple | PERMANENT | 65 W1-C | Exact |
    ... +6 more lines

### proven_1133
- **name**: 8D Petrov Classification of Jensen-Deformed SU(3)** -- Type D at tau=0 (Einstein manifold), algebraically general with 8 distinct eigenvalues at all tau > 0. Stable multiplicity structure {3,4,1,2,4,3
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: **8D Petrov Classification of Jensen-Deformed SU(3)** -- Type D at tau=0 (Einstein manifold), algebraically general with 8 distinct eigenvalues at all tau > 0. Stable multiplicity structure {3,4,1,2,4
- **Haiku NOISE reason**: Truncated table-cell fragment; incomplete name and statement; lacks session reference and full mathematical content
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
       14: ### Level A: Genuinely Novel (6 results — publishable standalone)
       15: 
       16: These fill documented gaps in the literature. No prior art found by systematic web search.
       17: 
       18: | # | Result | Session | Precision | Target | Novelty Basis |
       19: |:--|:-------|:--------|:----------|:-------|:--------------|
       20: | A1 | **Spectral Action Monotonicity Theorem** -- a_{2k} monotone for k=0,1,2,3. Spectral action monotone under both connections, all smooth cutoffs, all temperatures, all Lambda > 0. Periodic orbit corrections b
       21: | A2 | **Structural Monotonicity Theorem** -- <lambda^2>(tau) increases monotonically under volume-preserving Jensen deformation on SU(3). For any monotone cutoff f, S_f(tau) inherits monotonicity sector-by-sector
    ... +3 more lines

### proven_730
- **name**: Stage-2 dispatch ID**: `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: Stage-2 dispatch ID**: `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`
- **Haiku NOISE reason**: Stage-2 dispatch identifier label; bare gate-ID code, not a theorem statement
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     1200: - **connes-ncg-theorist** is CO-AUTHOR for clauses (b) Wedderburn (W5b-48 Step 5), (c) parse-tree JOINT, (d) F_traj JOINT, (e) convergence JOINT.
     1201: - **mack-cosmic-bridge** canonical sole-writer-role preserved as substrate-physics content authorship per `feedback_mack-bridge-role.md`; the orchestrator-direct registry write at S88 W5b-45 (original §VII.U.2 lan
     1202: 
     1203: This solo-runner execution does NOT violate the mack-sole-writer convention: it's an alternate-write-mechanism under the explicit `/rclab-solo` agent-ownership-takeover rule, which the skill provides as the canoni
     1204: 
     1205: ##### (i) Forward-looking — Stage-2 dispatch readiness for S91+
     1206: 
     1207: CF-51 PASS unlocks the Stage-2 → Stage-3 PERMANENT pathway for §VII.U.2 Var_a Corner-II classification. The Stage-2 dispatch is pre-registered at CF-48 (audit `39b598b444f1d070...`) with:
    ... +4 more lines

### proven_1253
- **name**: Connes 8-cutoff positive sums
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: Connes 8-cutoff positive sums | 21a | W4
- **Haiku NOISE reason**: Bare table-row fragment with only session code and wall label.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      272: | 2 | 1-loop Coleman-Weinberg | 18 | W1 |
      273: | 3 | Casimir scalar + vector | 19d D-1 | W1 |
      274: | 4 | Spectral back-reaction (scal+vec) | 19d | W1 |
      275: | 5 | Fermion condensate (Banks-Casher) | 19a S-4 | W3 |
      276: | 6 | D_K Pfaffian Z_2 transition | 17c D-2 | -- |
      277: | 7 | NCG spectral action (Seeley-DeWitt) | 20a SD-1 | W4 |
      278: | 8 | Casimir with TT 2-tensors | 20b L-3/L-4 | W1 |
      279: | 9 | Single-field slow-roll | 19b R-1 | W4 |
    ... +9 more lines

### proven_698
- **name**: Plan-vs-registry attribution reconciliation**: plan §W6-3 enumerated a 5-clause W-3 R3 attribution targeting the worksho
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: Plan-vs-registry attribution reconciliation**: plan §W6-3 enumerated a 5-clause W-3 R3 attribution targeting the workshop's three-machinery convergence; canonical §VII.U.2 registry has 6 clauses with 
- **Haiku NOISE reason**: Fragment: incomplete statement about plan-vs-registry reconciliation, missing complete theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      531: - `sessions/permanent-results-registry.md §VII.U.2 [12927-13082]` SHA-256 (block-pin): `cca490e2c2f0c627…`
      532: - `sessions/session-89/workshops/s89-w3-vii-u-2-corner-classification.md` SHA-256: `19f01edff552e7de…`
      533: - **audit_sha256** (full 64-char): `39b598b444f1d070aba1286a087fc7ecb10143b5f3e037d16fcda2388083640b`
      534: - **content_sha256** (full 64-char): `1ada2cd71ae52a115eceed089e72329fa04d72d0fff6de7084d367a0437ff535`
      535: 
      536: ##### (k) Self-assessment
      537: 
      538: - **Structural position**: Stage-2 reviewer-eligibility for §VII.U.2 is PRE-REGISTERED at the methodology layer; the future Stage-2 dispatch (`S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`) has its pool comp
    ... +2 more lines

### proven_1276
- **name**: [NEW S45] Bogoliubov/KZ n_s (all k-mappings)
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: [NEW S45] Bogoliubov/KZ n_s (all k-mappings) | 45 | n_s = -4.45 (EIH), -0.588 (primary)
- **Haiku NOISE reason**: Table row excerpt; numeric results for alternative parameterizations, no theorem body.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      311: | 36 | [NEW S40] HESS full moduli stabilization | 40 | W9: all 22 eigenvalues positive, 27th equilibrium closure |
      312: | 37 | [NEW S42] Fano interference (discrete+discrete) | 42 | K anti-Hermitian forces q=infinity |
      313: | 38 | [NEW S42] Polariton Higgs | 42 | Min gap 0.063 M_KK, 3.7e13x too large |
      314: | 39 | [NEW S42] Slow-roll n_s from spectral action | 42 | eta = 0.243, structural |
      315: | 40 | [NEW S44] Lifshitz anomalous dimension for n_s | 44 | eta_eff = 3.77, Weyl's law |
      316: | 41 | [NEW S44] Foam stabilization of tau | 44 | 0/900 minima found |
      317: | 42 | [NEW S45] Occupied-state spectral action | 45 | S_occ monotone decreasing |
      318: | 43 | [NEW S45] Unexpanded spectral action CC hierarchy | 45 | Taylor exactness on finite spectrum |
    ... +9 more lines

### proven_1880
- **name**: Definitional-datum-vs-derived-theorem K-counter
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: advancing | K=2 | S88 (`epistemic-discipline.md §"Layer-Decomposition"`) | `pru-class-corpus.md §9`
- **Haiku NOISE reason**: K-counter status from table row; only metadata tags and corpus pointers.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      562: | PRU Class 8.4 representation-convention-pin | SUGGESTION | K=1 | S88 W5b-50 | `pru-class-corpus.md §5` |
      563: | PRU Class 8.5 joint-hypersurface-pre-registration-form | SUGGESTION | K=1 | S88 W4c-36 | `pru-class-corpus.md §6` |
      564: | PRU Class 8.6 layered-substitution-chain-audit | SUGGESTION | K=1 | S88 W5b-47 | `pru-class-corpus.md §7` |
      565: | Substrate-input-orthogonality clause (Stage-2) | SUGGESTION | K=1 | S88 W7c-167 | `pru-class-corpus.md §15` + `cross-pillar-bridge-corpus.md §11` |
      566: | Closing-paragraph-coherence audit pattern (EG1) | SUGGESTION | K=1 | S88 W7c-167 | `pru-class-corpus.md §14` |
      567: | Mechanical-closure layer-separability carve-out (Type-F) | SUGGESTION | K=1 | S88 W8-89 | `mechanical-closure-discipline.md §"Layer-separability carve-out"` |
      568: | Element 3 fiducial-anchor binding discipline (cross-pillar) | SUGGESTION | K=1 | S88 W-15 W15-V.7 | `cross-pillar-bridge-corpus.md §6` (Element 3) |
      569: | Single-τ-slice vs moduli-deformation substrate-IS levels | advancing | K=2 | S88 W2-10 + W7 W2-2 V.4 | `phononic-framing.md §"Single-τ-slice vs moduli-deformation"` |
    ... +4 more lines

### proven_1357
- **name**: a_6 "theorem"
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: All a_{2n} monotone | Downgraded to conjecture beyond a_6 | 27
- **Haiku NOISE reason**: Status-downgrade notation; statement is a meta-claim about conjecture status.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      481: 
      482: ### Original (Sessions 17-28)
      483: 
      484: | What | Original | Corrected | Session |
      485: |:-----|:---------|:----------|:--------|
      486: | AZ class | DIII (T^2 = -1) | BDI (T^2 = +1) -- chiral, not Kramers | 17c |
      487: | "4-5x coupling" | Inter-sector D_K coupling | RETRACTED: was Kosmann norm, not matrix elements | 22b |
      488: | Berry curvature B=982.5 | Berry curvature | ERRATUM: was quantum metric. Berry = 0 exactly (W5). | 25 |
    ... +9 more lines

### proven_1232
- **name**: Bogoliubov Gaussianity Preservation: f_NL = O(eps) regardless of squeezing
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: PERMANENT | 65 W5-D | Structural
- **Haiku NOISE reason**: Statement field contains only status codes and metadata (PERMANENT | 65 W5-D | Structural), no substantive mathematical claim.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      189: | Fermi-surface lock: v^2(B2[0]) = 1/2 identically | PERMANENT | 64 W2-C | Algebraic |
      190: | a_0/a_2 trap (off-Jensen): decreasing a_2 INCREASES a_0/a_2 | PERMANENT | 64 W2-A | Candidate wall |
      191: | Spectral moment decoupling: F_{-1}(CC) vs F_{+1}(NEC) are different moments | PERMANENT | 64 W5-B | Structural |
      192: | H2 theorem: pi_ij=0 from DeWitt tracelessness (volume-preserving) | PERMANENT | 64 W3-A | Structural |
      193: | Chirality antisymmetry: {gamma_9, dD_K/dtau}=0. Chiral pairs ADD, not cancel | PERMANENT | 64 W6-B | Algebraic |
      194: | BdG Heat Kernel Factorization: K_BdG(t) = exp(-Delta^2 t) K_bare(t) | PERMANENT | 64-65 | Structural |
      195: | CC Ratio from Scalar Curvature Only: d(a_0/a_2)/ds = -(a_0/a_2)/R dR/ds | PERMANENT | 65 W1-B | Structural |
      196: | B/F Spectral Asymmetry = 0: |A|=0 EXACTLY on pure Riemannian triple | PERMANENT | 65 W1-C | Exact |
    ... +6 more lines

### proven_1381
- **name**: HESS-40 (27th equilibrium closure), T_acoustic agreement (0.7%), 11 gates
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: 40 | HESS-40 (27th equilibrium closure), T_acoustic agreement (0.7%), 11 gates
- **Haiku NOISE reason**: Table row label; no substantive theorem statement, only status codes and result ID.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      518: | 2 | 22b | Block-diagonality theorem, b_1/b_2 triple confirmation |
      519: | 3 | 35 | BCS 1D theorem, SU(3) anomalous curvature, unconditional chain, 3 closures |
      520: | 4 | 37 | Structural monotonicity theorem, instanton gas, GPV, BCS-BEC crossover, 3 closures |
      521: | 5 | 42 | Geometric LCDM (w=-1, CDM, NFW), 8 PASS, 4 FAIL, 8 new walls |
      522: | 6 | 44 | Sakharov G_N, CDM construction, 61/20 exact, epsilon_H invariance, 31 computations |
      523: | 7 | 50 | alpha_s theorem (5 proofs), Leggett Q=670k, phi crossing, Type D, sigma_8, 14 closures |
      524: | 8 | 34 | [iK_7,D_K]=0, Schur on B2, Trap 1, J correction, TRAP-33b retraction |
      525: | 9 | 17a | CPT hardwired, g_1/g_2 identity, 79,968 pairs |
    ... +9 more lines

### proven_336
- **name**: W5-D** is the computational verification of one specific NUMERICAL_L3 item
- **source_file**: sessions\session-73b\session-73b-results-workingpaper.md
- **statement (DB field)**: W5-D** is the computational verification of one specific NUMERICAL_L3 item
- **Haiku NOISE reason**: Bare fragment describing computational verification role, not a theorem statement; lacks substantive claim.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     2390: - phi_paasch (W5-A PROTECTED / W5-F #8 ROBUST) -- agreement
     2391: - clock_coeff = -3.08 (W5-A PROTECTED / W5-F #15 ROBUST) -- agreement
     2392: - wa_FW = 0 (W5-A PROTECTED) -- a CONSEQUENCE of four-fold lock, not a theorem in W5-F's taxonomy
     2393: - tau_fold = 0.19 (W5-A PROTECTED but flagged for W5-E verification) -- W5-F treats this as input, not a theorem
     2394: 
     2395: The two audits are complementary:
     2396: - **W5-A** catalogs CONSTANTS by L_max sensitivity (absolute values)
     2397: - **W5-F** catalogs PROOFS by algebraic robustness (structural theorems)
    ... +9 more lines

### proven_713
- **name**: Calibration corpus instance for deferred-pending sub-class**: CF-49 is K=2 calibration instance of `cross-pillar-bridge-
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: Calibration corpus instance for deferred-pending sub-class**: CF-49 is K=2 calibration instance of `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` `REGISTRY-INCOMPLETE-
- **Haiku NOISE reason**: Calibration corpus instance label and truncated cross-pillar-bridge reference, no substantive theorem content.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
      800: 
      801: ##### (r) Self-assessment
      802: 
      803: - **Structural position**: Var_a(n_a^GGE) lands as the K=2 LEVEL-DRESSED candidate-class instance at §VII.U.2 Corner II, with `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` sub-class tag. The 3-criterion PASS is s
      804: - **Honest proxy disclosure**: LEVEL-P is `PV-envelope-SCHEMATIC-EXTENDED` (one rung above pure SCHEMATIC, NOT yet FULL Connes-Chamseddine 1996 §2.2-2.3 multipliers). The plan's "FULL PV at Λ_UV=M_KK" intent is ap
      805: - **Bogoliubov small-λ cross-check honest disclosure**: cache's λ_min = 0.820 (no λ→0 mode at L_max=12); the closed-form identity n_a→1/2 at λ=0 holds analytically but is NOT empirically reachable from this cache.
      806: - **rho_S st
    ... [truncated]

### proven_302
- **name**: SU(3) (8-dim manifold)
- **source_file**: sessions\session-66\session-66-results-workingpaper.md
- **statement (DB field)**: +1
- **Haiku NOISE reason**: Table cell label '+1' with no theorem statement; sole content is KO-dimension classification value.
- **Spot-check judgment**: **AGREE**  -  markdown table row (name=cell, statement=numeric value)
- **source_context (first 8 lines)**:
     1731: #### The Question
     1732: KO(M^4) = 4, KO(SU(3)\_manifold) = 8 mod 8 = 0. Product: KO = (4+0) mod 8 = 4, implying J\_tot^2 = -1. But S52 verified J\_K^2 = +1 on SU(3). Apparent contradiction.
     1733: 
     1734: #### Key Numerical Results (Clifford algebra, machine epsilon)
     1735: 
     1736: | Object | KO-dim | eps (J^2) | eps' (JD) | eps'' (Jgamma) |
     1737: |:-------|:------:|:---------:|:---------:|:--------------:|
     1738: | M^4 (4-dim manifold) | 4 | -1 | +1 | +1 |
    ... +9 more lines

### proven_1280
- **name**: [NEW S48] Q-theory self-tuning Goldstone mass
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: [NEW S48] Q-theory self-tuning Goldstone mass | 48 | No finite fixed point, runaway
- **Haiku NOISE reason**: Table row excerpt; 'No finite fixed point, runaway' is a result status, not a mathematical theorem.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      315: | 40 | [NEW S44] Lifshitz anomalous dimension for n_s | 44 | eta_eff = 3.77, Weyl's law |
      316: | 41 | [NEW S44] Foam stabilization of tau | 44 | 0/900 minima found |
      317: | 42 | [NEW S45] Occupied-state spectral action | 45 | S_occ monotone decreasing |
      318: | 43 | [NEW S45] Unexpanded spectral action CC hierarchy | 45 | Taylor exactness on finite spectrum |
      319: | 44 | [NEW S45] Bogoliubov/KZ n_s (all k-mappings) | 45 | n_s = -4.45 (EIH), -0.588 (primary) |
      320: | 45 | [NEW S45] Sigma-selection for n_s | 45 | 5 methods exhausted, no fixed point |
      321: | 46 | [NEW S46] Twisted BdG NCG | 46 | BCS order parameter not algebra automorphism |
      322: | 47 | [NEW S48] Spectral action Goldstone mass | 48 | W11 Trace theorem |
    ... +9 more lines

### proven_65
- **name**: K-counter advancement**: substrate-input-orthogonality K=2 → K=3 (SUGGESTION → MANDATORY status promotion event at S90 W
- **source_file**: sessions\permanent-results-registry.md
- **statement (DB field)**: K-counter advancement**: substrate-input-orthogonality K=2 → K=3 (SUGGESTION → MANDATORY status promotion event at S90 W2 CF-20).
- **Haiku NOISE reason**: K-counter status note from table row; administrative classification change, not theorem.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
    15648: |:--------------------|:------------------|:-------------------------------|
    15649: | `JOINT-CROSS-AXIS-STAGE-2-PASS-AND` | `joint-theorem-promotion.md` 4-stage pathway; Stage-2 PASS-AND across two cross-reviewers on opposite axes WITHOUT prior workshop context, at a structural ceiling (canonical
    15650: | `SINGLE-AXIS-THEOREM-VERIFIER-PASS` | Direct theorem-verifier PASS on the registered theorem statement; does not require 4-stage joint pathway because the theorem admits a single-axis structural proof. The verif
    15651: | `SUBSTRATE-UNIQUENESS-LIFT` | Lifts a previously-permanent single-instance substrate fact to structural-class-membership status. PERMANENT eligibility INHERITS from the upstream single-instance fact's prior perm
    15652: 
    15653: **This entry's Stage-3-CLASS pathway** (canonical first instance of the `JOINT-CROSS-AXIS-STAGE-2-PASS-AND` class):
    15654: - **Structural ceiling**: substrat
    ... [truncated]

### proven_1892
- **name**: §XIII methodology-floor axis
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: atlas-12 (24 rules + 9 templates) | `methodology-wave-allowlist.md`; `methodology-wave-instances.md`
- **Haiku NOISE reason**: Table cell label; bare axis name with file pointers, not a theorem
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      585: | Mega-matrix section | Atlas pin | Adjacent registry pin |
      586: |:--------------------|:----------|:-----------------------|
      587: | §I + §X.A walls W1-W21 | atlas-05 walls W1-W21 | — |
      588: | §I.B / §X.B §VII slots | atlas-07 §XVI registry slot inventory | `permanent-results-registry.md §VII` |
      589: | §II + §X.C closures (existing 88 + 8 new) | atlas-02 mechanism lifecycle Eras IX-XII | — |
      590: | §VII probability state | atlas-06 probability trajectory; atlas-10 breakthroughs (rows correspond to inflection points) | — |
      591: | §X cross-pillar bridges (XI) | atlas-11 §IV K=3 corpus | `cross-pillar-bridge-corpus.md §5` |
      592: | §XI 4-corner classification | atlas-11 §X algebra-axis orthogonality | `cross-pillar-bridge-corpus.md §6`; `permanent-results-registry.md §VII.U.2` |
    ... +9 more lines

### proven_45
- **name**: §VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576): s=0 boundary corollary
- **source_file**: sessions\permanent-results-registry.md
- **statement (DB field)**: §VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576): s=0 boundary corollary
- **Haiku NOISE reason**: Incomplete statement ending in colon; only heading-level description without theorem content.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     5350: - Regulator-Family Boundary Theorem (van den Dungen S-1; line 55 of
     5351:   `sessions/session-85/session-85-s1-regulator-boundary-van-den-dungen.md`):
     5352:   partition `𝓡 = 𝓡_{a_4} ⊔ {cutoff_sqrt}` where
     5353:   `𝓡_{a_4} = {ζ, Zubarev, SDW, anomaly}`; theorem (i) `f_0^cutoff = 2`
     5354:   is unique.
     5355: - §VII-B.HP1-NEAR-INVARIANCE Step 1 (registry line 2605):
     5356:   F_4 = {ζ, Zubarev, SDW} pure-a_4 Mellin-support partition (orthogonal
     5357:   to this entry's 5-class multiplier-vector partition).
    ... +9 more lines

### proven_943
- **name**: SU(3) -> U(1)_7
- **source_file**: sessions/framework/Classification-of-phonon-exflation.md
- **statement (DB field)**: Symmetry breaking G -> H | S34 | 04 | PROVEN
- **Haiku NOISE reason**: Table cell: mapping label, not a theorem.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       20: 
       21: ## I. The Complete Mapping
       22: 
       23: The following table maps every framework concept to its Landau condensed matter equivalent, with the session that established the connection and the Landau paper that provides the theoretical foundation.
       24: 
       25: | Framework Concept | CM Equivalent | Session | Paper | Status |
       26: |:--|:--|:--|:--|:--|
       27: | Jensen deformation tau | Order parameter eta | S17a | 04 | PROVEN |
    ... +9 more lines

### proven_326
- **name**: W5-D asks "is this one NUMERICAL result L_max-invariant?"
- **source_file**: sessions\session-73b\session-73b-results-workingpaper.md
- **statement (DB field)**: W5-D asks "is this one NUMERICAL result L_max-invariant?"
- **Haiku NOISE reason**: Question phrasing without substantive theorem statement; serves as metadata descriptor rather than theorem content.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     2246: 
     2247: **Verdict summary**: No proven result is L_max-sensitive. 20 results are strictly ROBUST (algebraic / representation-theoretic / Clifford identity), 1 is QUASI-ROBUST (K-homology invariance proven; numerical value
     2248: 
     2249: **Functional classification**: GEOMETRIC (spectral triple structure + L_max truncation audit)
     2250: 
     2251: **Relationship to W5-A, W5-D, W5-G**: W5-A classified 175 canonical constants by L_max sensitivity (20 PROTECTED, 9 DIVERGENT-ABSOLUTE, etc.). W5-D verified the three-phonon particle-hole protection is L_max-invar
     2252: 
     2253: - W5-A asks "which CONSTANTS are L_max-sensitive?"
    ... +6 more lines

### proven_167
- **name**: Per-Bulletin-per-pole Level-1/2/3 ladder** declaration per W10-119 extension
- **source_file**: sessions\session-88\s88-pending-edits-ledger.md
- **statement (DB field)**: Per-Bulletin-per-pole Level-1/2/3 ladder** declaration per W10-119 extension
- **Haiku NOISE reason**: Fragment referencing a ladder declaration extension, not a complete theorem.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
      621: - **Target**: `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness — PRDR"` Class 8.2 calibration corpus
      622: - **Action**: add NEW calibration instance: W6b-56 plan §W6b-56 substitution-chain-Step claim "recovers 8 at τ → 5π" structurally false under direct Python verification. Forward-enforcement: any plan-block claimin
      623: - **Audit-script extension**: queue extension to `_machinery_feasibility_audit.py` with "boundary direction substitution chain" sub-check
      624: 
      625: ### B.52 — permanent-results-registry.md: §VII.AR (or §VII.AS — coordinate with B.44) STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP for W7a-74 LEVEL-DRESSED rank ordering (W-22 V.2)
      626: - **Source**: `s88-w22-w7a-74-rank-vs-magnitude.md` §V.2
      627: - **Target**: `sessions/permanent-results-registry.md`
      628: - **Action**: theorem statement = "Rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 substrate-distance-2 Mellin-cone pole is REGULATOR-PARAMETER-dependent (NOT regulator-CLASS-dependent) under the PRIM
    ... +6 more lines

### proven_416
- **name**: What**: add a PROVENANCE row to `computations/canonical_constants.py` for `Gamma_effacement = 0.99970`. The MCP `get_con
- **source_file**: sessions\session-85\session-85-1a-cc-residue-phonon-first.md
- **statement (DB field)**: What**: add a PROVENANCE row to `computations/canonical_constants.py` for `Gamma_effacement = 0.99970`. The MCP `get_constant` query returned NO PROVENANCE row; this is a registry-hygiene defect that 
- **Haiku NOISE reason**: Carry-forward action item (What/Inputs/Gate pattern); registry-hygiene task, not a theorem.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
      255: 
      256: - **What**: evaluate the boundary contribution to the spectral action from the Pontryagin density on the substrate manifold M⁴ × SU(3)_τ, and verify the protected ratio R_1 = a₀ · a₄ / a₂² (registry `s75_atlas_rec
      257: - **Inputs**: a4_fold = 1350.7216 (S42), a0_fold = 6440, a2_fold = 2776.17, BDI 9/10 stable invariant (cross-reference S85 W8-5 — Slot 1B, do not duplicate); χ(M⁴ × SU(3)) Euler characteristic from KK-SU(3) topolo
      258: - **Gate**: PASS iff R_1 deviation ≤ 5% from the protected canonical value AND the boundary Pontryagin contribution closes the a₄-channel residue to within 30%. FAIL if R_1 deviation > 15%. INFO between.
      259: - **Effort**: 4-6 hours, 1 agent session (with cross-verification by van-den-dungen via Slot 1D §VII.P meta-theorem, do not block on it).
      260: 
      261: ### V.4 GAMMA-PROVENANCE-LANDING-86
      262: 
    ... +4 more lines

### proven_146
- **name**: Source**: `s88-w22-w7a-74-rank-vs-magnitude.md` §IV.3, `s88-w18-w6a-51-geometric-resummation.md` §IV.1
- **source_file**: sessions\session-88\s88-pending-edits-ledger.md
- **statement (DB field)**: Source**: `s88-w22-w7a-74-rank-vs-magnitude.md` §IV.3, `s88-w18-w6a-51-geometric-resummation.md` §IV.1
- **Haiku NOISE reason**: Source file/section citation, no theorem content provided.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      361: - **Initial content**: K=2 calibration corpus tracking ledger for INVARIANT-vacuous vs INVARIANT-with-DISCRIMINATING-CONTENT sub-class. Instance #1 = W13 W-1 profile-invariance at 6.68e-17. Instance #2 = W1c-69 si
      362: 
      363: ### B.36 — methodology-wave-allowlist.md: pending SHA resolutions
      364: - **Source**: existing `.claude/rules/methodology-wave-allowlist.md` table at the time of S88 close
      365: - **Target**: same file
      366: - **Action**: compute SHAs for rows currently marked `pending` (W0a-1, W0a-3, W0a-5, W0a-2b, W2-6, W2-8, W2-9, W2-10, W2-11, W2-12, W8-92, W9-ALLOWLIST-LIFT-OUT) by hashing their respective plan-block contents. So
      367: 
      368: ### B.37 — sessions/permanent-results-registry.md: §VII.AR registry slot allocation (W-22 / W-18)
    ... +7 more lines

### proven_1881
- **name**: F(observable) vs F(trigger predicate) split
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: SUGGESTION | K=1 | S88 (`epistemic-discipline.md §"Layer-Decomposition"`) | `pru-class-corpus.md §10`
- **Haiku NOISE reason**: Fragmentary status tag extracted from table; not a substantive theorem statement.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      563: | PRU Class 8.5 joint-hypersurface-pre-registration-form | SUGGESTION | K=1 | S88 W4c-36 | `pru-class-corpus.md §6` |
      564: | PRU Class 8.6 layered-substitution-chain-audit | SUGGESTION | K=1 | S88 W5b-47 | `pru-class-corpus.md §7` |
      565: | Substrate-input-orthogonality clause (Stage-2) | SUGGESTION | K=1 | S88 W7c-167 | `pru-class-corpus.md §15` + `cross-pillar-bridge-corpus.md §11` |
      566: | Closing-paragraph-coherence audit pattern (EG1) | SUGGESTION | K=1 | S88 W7c-167 | `pru-class-corpus.md §14` |
      567: | Mechanical-closure layer-separability carve-out (Type-F) | SUGGESTION | K=1 | S88 W8-89 | `mechanical-closure-discipline.md §"Layer-separability carve-out"` |
      568: | Element 3 fiducial-anchor binding discipline (cross-pillar) | SUGGESTION | K=1 | S88 W-15 W15-V.7 | `cross-pillar-bridge-corpus.md §6` (Element 3) |
      569: | Single-τ-slice vs moduli-deformation substrate-IS levels | advancing | K=2 | S88 W2-10 + W7 W2-2 V.4 | `phononic-framing.md §"Single-τ-slice vs moduli-deformation"` |
      570: | Definitional-datum-vs-derived-theorem K-counter | advancing | K=2 | S88 (`epistemic-discipline.md §"Layer-Decomposition"`) | `pru-class-corpus.md §9` |
    ... +4 more lines

### proven_1151
- **name**: Sakharov Induced Gravity from KK Spectrum
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: Sakharov Induced Gravity from KK Spectrum | 44 | Toms 1983 already established KK + Sakharov. Methodology known.
- **Haiku NOISE reason**: Status comment describes historical attribution (Toms 1983), not substantive theorem statement.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       64: | C1 | D_K Block-Diagonality Universality | 22b | Schur's lemma + equivariance. Fegan 1987, Slebarski 1985 assume this. |
       65: | C2 | Three Algebraic Traps (F/B, b_1/b_2, e/(ac)) | 20b-22c | Weyl's law, Dynkin indices, trace factorization. Standard tools. |
       66: | C3 | Van Hove Zero-Critical-Coupling | 28c | Cooper instability (1956). Application to compact manifolds untested but mechanism is textbook. |
       67: | C4 | Trap 4: Schur Orthogonality Selection Rule | 32a+32c | Schur orthogonality for U(2) reps. Automatic from representation theory. |
       68: | C5 | Trap 5: J-Reality PH Selection Rule | 32b | Real structure J with J^2=+1 on real reps. Standard NCG. |
       69: | C6 | [iK_7, D_K] = 0 at ALL tau | 34 | Computation of a commutator on a specific deformation family. Novel fact but routine calculation. |
       70: | C7 | Trap 1 Confirmed: V(B1,B1) = 0 | 34 | U(2) singlet selection rule. Standard representation theory. |
       71: | C8 | B2 Geometric Protection Theorem | 39 | Schur's lemma on irreducible (1,1) subspace. |
    ... +7 more lines

### proven_1103
- **name**: Window-7
- **source_file**: sessions/framework/Atlas/atlas-05-walls-doors-windows.md
- **statement (DB field)**: FUNCTIONAL-SELECT-67: which spectral functional generates n_s? Determines whether 0.9595 (sqrt) is canonical OR scheme-dependence persists | S67 carry-forward; bracket FAIL if no functional family yie
- **Haiku NOISE reason**: Incomplete statement ending with unfinished parenthesis; table-cell truncation.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
        1: # Atlas D05: Walls, Doors, and Windows
        2: 
        3: **Scope**: Sessions 1-88 (Dec 2024 — May 2026)
        4: **Updated**: 2026-05-09 (S52-S88 uplift; +11 walls W11-W21, +14 doors session-keyed, +18 windows Window-7..24)
        5: **Totals**: 21 walls / 27 doors / 24 windows (23 OPEN + 1 permanently CLOSED)
        6: 
        7: ---
        8: 
    ... +4 more lines

### proven_422
- **name**: What**: Execute `S86-W?-3HE-B-INVERSION-CANONICAL-LANDING` (spec above). Compose the three subsection MDs (a, b, c) into
- **source_file**: sessions\session-85\session-85-1b-3heb-inversion-landau.md
- **statement (DB field)**: What**: Execute `S86-W?-3HE-B-INVERSION-CANONICAL-LANDING` (spec above). Compose the three subsection MDs (a, b, c) into a single tri-signed registry-row entry; append to `sessions/permanent-results-r
- **Haiku NOISE reason**: Carry-forward task specification fragment; not a theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      339: ---
      340: 
      341: ## §IX. Carry-forward (structured per `feedback_carry-forward-mandatory.md`)
      342: 
      343: Every entry below is a concrete planned computation for S86, with what / inputs / gate / effort.
      344: 
      345: ### CF-1B-b-1: S86 landing of canonical inversion statement to permanent-results-registry
      346: 
    ... +8 more lines

### proven_1147
- **name**: Trap 5: J-Reality PH Selection Rule
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: Trap 5: J-Reality PH Selection Rule | 32b | Real structure J with J^2=+1 on real reps. Standard NCG.
- **Haiku NOISE reason**: Table cell label with standard reference; no substantive theorem statement (J-reality rule is textbook).
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       60: These apply established mathematical tools (Schur's lemma, Weyl's law, Cooper instability, Gilkey formula, Sakharov mechanism) to the specific spectral triple on Jensen-deformed SU(3). Correct and useful, but the 
       61: 
       62: | # | Result | Session | Known Source |
       63: |:--|:-------|:--------|:-------------|
       64: | C1 | D_K Block-Diagonality Universality | 22b | Schur's lemma + equivariance. Fegan 1987, Slebarski 1985 assume this. |
       65: | C2 | Three Algebraic Traps (F/B, b_1/b_2, e/(ac)) | 20b-22c | Weyl's law, Dynkin indices, trace factorization. Standard tools. |
       66: | C3 | Van Hove Zero-Critical-Coupling | 28c | Cooper instability (1956). Application to compact manifolds untested but mechanism is textbook. |
       67: | C4 | Trap 4: Schur Orthogonality Selection Rule | 32a+32c | Schur orthogonality for U(2) reps. Automatic from representation theory. |
    ... +6 more lines

### proven_1472
- **name**: §VII.U.7
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: PER-EVAL FINITENESS PRE-REGISTRATION (W0-20 apex + W0-7-MB rho-fit per-evaluation finiteness check for FINITE-VECTOR observables) | S87 W1a-3 | lizzi | PERMANENT
- **Haiku NOISE reason**: Table cell content; pre-registration label without statement of the substantive mathematical content.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      720: 
      721: ### XVI.F. P-v2 HP^1-content-distinct + Mellin-cone supplementary
      722: 
      723: | §VII slot | Theorem name | Landing session | Author(s) | Status |
      724: |:----------|:-------------|:----------------|:----------|:-------|
      725: | §VII.P′ | (η = 0, GV ≠ 0) joint-probe official landing on (C_H, C_epsH) parity-twin pair; Bulletin #1 CONFIRMED-DEMOTED-SCHEME-DEPENDENT, Bulletin #2 CONFIRMED-PROMOTED-PARITY-BLINDNESS (composite verdict; Class
      726: | §VII.AF.2 | §VII.P-v2 HP^1-content-distinct refinement (replaces failed S86 W9 C24 HP^0-content-distinct attempt) | S87 W5-4 | connes | PERMANENT (via mechanical-edit remediation) |
      727: | §VII.AF.3 | T6 substitution PROMOTION to PASS-UNCONDITIONAL | S86 W-5 | volovik + connes | NEEDS-DECISION |
    ... +10 more lines

### proven_876
- **name**: Inputs**: `s83_w1_g4_epsilon_h_trajectory_fi.py`; S78 W-2D f_conv-anomaly table (same 3/2 structural ratio appears); f_2
- **source_file**: sessions\session-83\session-83-gen-physicist-synthesis.md
- **statement (DB field)**: Inputs**: `s83_w1_g4_epsilon_h_trajectory_fi.py`; S78 W-2D f_conv-anomaly table (same 3/2 structural ratio appears); f_2 normalization convention from canonical_constants.
- **Haiku NOISE reason**: Carry-forward input list fragment; partial file/constant citations without theorem content.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      204: - **What**: Re-run G15/G16/G28/G34 under Convention B (Lambda_Z = lam_max matched-scale) across all five regulators, tabulate all spans, and populate the full §VII.K-PROP table with BOTH-CONVENTION columns. Verify
      205: - **Inputs**: Same D_K spectrum inputs as V.2; regulator Lambda_Z rebounded to lam_max.
      206: - **Gate**: S84-CONV-B-PROPAGATION-ATLAS. PASS: 4/4 CC-identities verified under Conv B at machine precision. FAIL: any identity mis-predicts. INFO: 3/4.
      207: - **Effort**: 2-3 hours, 1 agent session (lizzi for computation; gen-physicist for CC-identity audit).
      208: 
      209: ### V.4. Closed-form derivation of F_traj = 3/2 as permanent registry entry
      210: 
      211: - **What**: Upgrade W1-G4 INFO (F_traj = 3/2, trajectory-FI factor) from gate verdict to a PERMANENT theorem in the knowledge index. Proof structure: at Lambda^2 = L2 arbitrary, `f_2^zeta / f_2^SDW = L2 / [(2/3)L2
    ... +1 more lines

### proven_718
- **name**: content_sha256** (full 64-char): `d252222f9580080bee4abf28c1d1c0a7ee095f6323df00f94da82aa705411bdd`
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: content_sha256** (full 64-char): `d252222f9580080bee4abf28c1d1c0a7ee095f6323df00f94da82aa705411bdd`
- **Haiku NOISE reason**: SHA hex string from verdict metadata, not a theorem.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     1009: | Verdict line | `computations/session-90/s90_gate_verdicts.txt` last 4 lines (canonical + W9a-99 + S87+ 3-tuple INFO + tier_pin=TIER-2) | tail-verified; audit_sha256 `a07e1e33b9008cee...` unique |
     1010: 
     1011: ##### (l) Input-pin SHAs (S84+ dual-SHA closure)
     1012: 
     1013: - `computations/_shared/canonical_constants.py` SHA-256: `5a19a04e0adef8cd…`
     1014: - `computations/session-84/s84_spectrum_cache_L12_tau019.npz` SHA-256: `9e6d9cf7fd6a6949…`
     1015: - `computations/_shared/_spectral_action_regulators.py` SHA-256: `2fc40ccbb62fcbf1…`
     1016: - **audit_sha256** (full 64-char): `a07e1e33b9008cee1211d2e8169fcb20209e0add6bbda8531535ccc3cbfc7293`
    ... +7 more lines

### proven_1386
- **name**: Fusion: 7 publishable results, 4 walls, KC chain 4/5 PASS
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: 28 | Fusion: 7 publishable results, 4 walls, KC chain 4/5 PASS
- **Haiku NOISE reason**: Table row label; status/result count, not a theorem with hypothesis or conclusion.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      523: | 7 | 50 | alpha_s theorem (5 proofs), Leggett Q=670k, phi crossing, Type D, sigma_8, 14 closures |
      524: | 8 | 34 | [iK_7,D_K]=0, Schur on B2, Trap 1, J correction, TRAP-33b retraction |
      525: | 9 | 17a | CPT hardwired, g_1/g_2 identity, 79,968 pairs |
      526: | 10 | 40 | HESS-40 (27th equilibrium closure), T_acoustic agreement (0.7%), 11 gates |
      527: | 11 | 45 | Q-theory BCS PASS (first CC mechanism), Taylor exactness, 15 structural results |
      528: | 12 | 39 | N_pair=1 exact, B2 protection, analytic GGE, 3 S38 retractions, 20 computations |
      529: | 13 | 51 | Anderson-Higgs impossibility, n_s>1 theorem, convex combination, SA mixing |
      530: | 14 | 48 | Trace theorem, Leggett mode, transversality, 6 closures |
    ... +9 more lines

### proven_1729
- **name**: IDG nonlocality for CC
- **source_file**: sessions/framework/registry/constraint-mega-matrix.md
- **statement (DB field)**: IDG nonlocality for CC | Analyticity class of F(p²) = analyticity class of f''(z). Theorem T11 | S63 W6-01
- **Haiku NOISE reason**: Status field contains workshop ID (S63 W6-01) instead of standard PROVEN/STAGE tag; statement conflates theorem number reference (T11) with closure.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      112: ### II.F Session 63 (9+ closures)
      113: 
      114: | # | Mechanism | Why It Fails | Session |
      115: |:--|:---------|:-------------|:--------|
      116: | 64 | Starobinsky frozen transit | Starobinsky R² inflation incompatible with transit dynamics | S63 |
      117: | 65 | Multi-field cos(α)=0 | Isocurvature projections vanish identically | S63 |
      118: | 66 | Isocurvature frozen | No isocurvature DOF survives transit | S63 |
      119: | 67 | Mixed B-F q-theory | Same-spectrum B/F has at most one critical point (maximum). Theorem T9 | S63 W3-06 |
    ... +9 more lines

### proven_168
- **name**: CONDITIONAL on A.36 Reading A WIN
- **source_file**: sessions\session-88\s88-pending-edits-ledger.md
- **statement (DB field)**: CONDITIONAL on A.36 Reading A WIN
- **Haiku NOISE reason**: Conditional clause fragment, not a substantive theorem statement.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
      622: - **Action**: add NEW calibration instance: W6b-56 plan §W6b-56 substitution-chain-Step claim "recovers 8 at τ → 5π" structurally false under direct Python verification. Forward-enforcement: any plan-block claimin
      623: - **Audit-script extension**: queue extension to `_machinery_feasibility_audit.py` with "boundary direction substitution chain" sub-check
      624: 
      625: ### B.52 — permanent-results-registry.md: §VII.AR (or §VII.AS — coordinate with B.44) STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP for W7a-74 LEVEL-DRESSED rank ordering (W-22 V.2)
      626: - **Source**: `s88-w22-w7a-74-rank-vs-magnitude.md` §V.2
      627: - **Target**: `sessions/permanent-results-registry.md`
      628: - **Action**: theorem statement = "Rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 substrate-distance-2 Mellin-cone pole is REGULATOR-PARAMETER-dependent (NOT regulator-CLASS-dependent) under the PRIM
      629: - **Per-Bulletin-per-pole Level-1/2/3 ladder** declaration per W10-119 extension
    ... +7 more lines

### proven_778
- **name**: What**: Promote K_HK = 9 FI partition cardinality result to permanent registry entry at algebra-axis Corner I per `perma
- **source_file**: sessions\session-91\session-91-w6-workingpaper.md
- **statement (DB field)**: What**: Promote K_HK = 9 FI partition cardinality result to permanent registry entry at algebra-axis Corner I per `permanent-results-registry.md §VII.U.2` 4-corner partition. STAGE-1-CANDIDATE landing
- **Haiku NOISE reason**: Carry-forward item description (What/Inputs/Gate/Effort) without theorem content.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
     1950: - **What**: Re-execute the K_csub_R extraction across the A_5 atlas under FULL physical Connes-Chamseddine 1996 §2.2-2.3 multipliers (replace SCHEMATIC sub_term_R(L) analytic forms with substrate-canonical zeta-fu
     1951: - **Inputs**: W6-2 npz (audit_sha=`109e4307...`); s84_spectrum_cache_L12_tau019.npz (extending to L_max=14 or 15 via Friedrich-Bär saturation if feasible); `_spectral_action_regulators.py` FULL physical regulariza
     1952: - **Gate**: PASS = |K_csub_mean − 0.5| < 0.1 AND K_csub_std > 0.05 AND F_2-axis FI sub-projection PASS; FAIL = |K_csub_mean − 0.5| ≥ 0.2.
     1953: - **Effort**: ~3.0 we (substantial; per-regulator spectral-moment extraction with PV subtraction + cutoff truncation + lattice form-factor weighting; CC 1996 derivation chain on substrate D_K spectrum).
     1954: - **Source gate**: W6-2 + W6-1 (unified scope; both gates' SCHEMATIC sub_term consumption resolved by single FULL physical pipeline).
     1955: - 
    ... [truncated]

### proven_1172
- **name**: 4 curvature invariants (analytic)
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: Exact formulas | Rational coefficients | 17b | `sp2_analytic_derivation.py`
- **Haiku NOISE reason**: Statement is bare measurement results (exact formulas, rational coefficients) without substantive theorem form.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      115: | J*rho = rho*J (epsilon' = +1) | -- | < 1e-15 | 8 | `branching_computation_32dim.py` |
      116: | J*gamma = -gamma*J (epsilon'' = -1) | -- | < 1e-15 | 8 | `branching_computation_32dim.py` |
      117: | [J, D_K(tau)] = 0 (CPT hardwired) | 79,968 pairs | max 3.29e-13 | 17a | `d1_d3_j_compatibility.py` |
      118: | g_1/g_2 = e^{-2tau} structural identity | Derived | Exact | 17a B-1 | `gauge_coupling_derivation.py` |
      119: | Baptista geometry checks | 67/67 | Machine epsilon | 17b | `b2_baptista_verification.py` |
      120: | D_K correctness audit | 39/39 | Exact zeros | 17b | `b3_dk_correctness_audit.py` |
      121: | Riemann tensor R_{abcd}(tau) | 147/147 | Machine epsilon | 20a | `r20a_riemann_tensor.py` |
      122: | Volume-preserving TT-deformation | det = 1.000000000 | Exact | 12 | `dirac_spectrum.py` |
    ... +9 more lines

### proven_346
- **name**: L_max-invariance**: structural floor. Verified explicitly at L = 3, 5, 7 for representative observables (three-phonon ve
- **source_file**: sessions\session-74\session-74-results-workingpaper.md
- **statement (DB field)**: L_max-invariance**: structural floor. Verified explicitly at L = 3, 5, 7 for representative observables (three-phonon vertex `Gamma / H`, Wilson loop, Fermi-surface lock) in S73B W5-D; zero drift to m
- **Haiku NOISE reason**: Truncated table-cell content, not a complete theorem.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
     8066: | # | Result | Session | Status |
     8067: |:--|:-------|:--------|:-------|
     8068: | 48 | **Six-Layer Multi-Layer Protection of (0,0) Sector** -- The trivial Peter-Weyl sector `H_(0,0) ~= S` of the spectral triple on Jensen-deformed `SU(3)` is protected by the disjunction of six independent stru
     8069: 
     8070: Notes for the registry:
     8071: 
     8072: - **Category**: COMPOSITE / STRUCTURAL FLOOR -- this result unifies pre-existing layers into a single protection statement; it does not prove a new layer in isolation.
     8073: - **Precision**: logical / categorical (no single numerical tolerance). Each constituent layer has its own precision in the registry: L1 at 8.4e-15 (S22b), L2 at 3.29e-13 (S17a), L3 exact (Peter-Weyl theorem), L4 
    ... +2 more lines

### proven_477
- **name**: Registry patch (draft, assembled for future landing — see `s85_w3_consolidated_upgrade.json`)**: ready to append to `ses
- **source_file**: sessions\session-85\session-85-w3-workingpaper.md
- **statement (DB field)**: Registry patch (draft, assembled for future landing — see `s85_w3_consolidated_upgrade.json`)**: ready to append to `sessions/framework/permanent-results-registry.md` when that file is created (the fi
- **Haiku NOISE reason**: Truncated metadata reference; ends mid-sentence (see `s85_w3_consolidated_upgrade.json`)**: ...).
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      350:   | BDI ↔ K-reg map | [1.922, 91.5] | True | True | ✓ |
      351:   | N_OP ↔ Two-speed | [91.5, 91.5] (shared endpoint) | True | True | ✓ |
      352:   | N_OP ↔ K-reg map | [91.5, 3.556e5] (full R7) | True | True | ✓ |
      353:   | Two-speed ↔ K-reg map | [1.922, 91.5] (full inflationary) | True | True | ✓ |
      354: 
      355: - **Joint statement — "Landau structural block"**:
      356:   > *The inflationary sub-corridor K ∈ [K_R5, K_crit] carries an Altland-Zirnbauer BDI class certified at L_max=10 with 8 Goldstones via G = SU(3)×SO(3)×U(1)_rel×U(1)_T → H = SU(2)×U(1)×SO(2), and all regulator-cl
      357: 
    ... +8 more lines

### proven_1244
- **name**: BYPASSED at domain wall boundaries (W-32b: van Hove LDOS exceeds threshold)
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: BYPASSED at domain wall boundaries (W-32b: van Hove LDOS exceeds threshold) | 32b
- **Haiku NOISE reason**: Table cell fragment—mechanism note (wall bypassed), not a theorem statement.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      239: | W5 | Berry Curvature Vanishing | K_a anti-Hermitian => Berry curvature = 0 identically. Closes all topological mechanisms. | Exact |
      240: | W6 | Thermodynamic Stabilization | Smooth functional trap + Matsubara stiffening. | Exact |
      241: 
      242: ### Walls Extended (Sessions 30-40)
      243: 
      244: | Wall | Extension | Session |
      245: |:-----|:----------|:--------|
      246: | W4 | Extended from 1D Jensen to full 3D U(2)-invariant surface (V_spec/F_BCS ~ 8000) | 30Ba |
    ... +9 more lines

### proven_961
- **name**: Euler deficit = E_cond
- **source_file**: sessions/framework/Classification-of-phonon-exflation.md
- **statement (DB field)**: Gibbs-Duhem violation | S44 W6-5 | 05 | OPEN
- **Haiku NOISE reason**: Status table row with session/section codes; no substantive theorem statement.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       41: | Spectral triple dissolution | Effective theory emergence | S44 W6-7 | 04 (universality) | PROVEN |
       42: | CC fine-tuning | Universality class mismatch | S44 W5-5 | 04 sec. 7 | STRUCTURAL |
       43: | n_s = 0.965 | Quench dynamics / Kibble-Zurek | S43-44 | 09, 21 | OPEN |
       44: | epsilon_H = 3.0 | Ratio invariance (intensive) | S44 W4-3 | 04 | PROVEN (theorem) |
       45: | Van Hove singularities | Phase transition classification | S34-44 | 27 | PROVEN |
       46: | Block-diagonal theorem | Selection rules (Schur) | S22b | 04 (rep. theory) | PROVEN |
       47: | 8-temperature GGE | Non-Fermi liquid | S44 W6-5 | 11, 20 | STRUCTURAL |
       48: | Negative heat capacities | Saddle directions in F | S44 W6-5 | 04, 11 | PROVEN |
    ... +9 more lines

### proven_735
- **name**: PASS-AND aggregation**: both reviewers must independently PASS each JOINT clause
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: PASS-AND aggregation**: both reviewers must independently PASS each JOINT clause
- **Haiku NOISE reason**: List item fragment — aggregation procedure instruction, not a theorem statement.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
     1205: ##### (i) Forward-looking — Stage-2 dispatch readiness for S91+
     1206: 
     1207: CF-51 PASS unlocks the Stage-2 → Stage-3 PERMANENT pathway for §VII.U.2 Var_a Corner-II classification. The Stage-2 dispatch is pre-registered at CF-48 (audit `39b598b444f1d070...`) with:
     1208: - **Stage-2 dispatch ID**: `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY`
     1209: - **Axis-A pool** (select 1 at dispatch time): `{van-den-dungen-bridge-theorist, gen-physicist}`
     1210: - **Axis-B pool** (select 1 at dispatch time): `{volovik-superfluid-universe-theorist, mack-cosmic-bridge, kitaev-quantum-chaos-theorist}`
     1211: - **EXCLUDED**: `{connes-ncg-theorist, lizzi-spectral-functional-theorist}` (PRIMARY/CO-AUTHOR of §VII.U.2)
     1212: - **Parallel dispatch**: MANDATORY per `joint-theorem-promotion.md §"Stage 2"`
    ... +9 more lines

### proven_692
- **name**: PRU compliance**: 14 machinery pins enumerated in plan §W6-2 §"Machinery pin (PRDR)" YAML block; all consumed in script 
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: PRU compliance**: 14 machinery pins enumerated in plan §W6-2 §"Machinery pin (PRDR)" YAML block; all consumed in script (L_max_scan, taylor_truncation_closed_form, asymptotic_target, richardson_patter
- **Haiku NOISE reason**: Fragment: table-cell label listing machinery pins, not a complete theorem statement.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      348: ##### (l) Self-assessment
      349: 
      350: - **Structural position**: New canonical `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5π = 15.707963267948966` lands as the substrate-first asymptotic-limit pin; the pre-existing `tau_max_HK5_regime_FW = 12.475002
      351: - **L^{-1}-vs-L^{-3} structural finding**: empirically confirmed that the Source-3 Taylor-truncation estimator has L^{-1}-dominant convergence (NOT L^{-3} as plan asserted). The plan's L^{-3} attribution was a cro
      352: - **Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY closure**: plan substitution-chain L^{-3} attribution drift surfaced via analytical pre-compute + empirical Richardson fit comparison; resolved in-session by adopting
    ... [truncated]

### proven_427
- **name**: Gate**: `S86-W0-KR5-KCRIT-PROVENANCE`. PASS iff `mcp__knowledge__get_constant("K_R5")` returns the W8-7 + W8-2 provenanc
- **source_file**: sessions\session-85\session-85-1b-3heb-inversion-landau.md
- **statement (DB field)**: Gate**: `S86-W0-KR5-KCRIT-PROVENANCE`. PASS iff `mcp__knowledge__get_constant("K_R5")` returns the W8-7 + W8-2 provenance after update; analogous for K_crit. FAIL iff update fails or returns inconsist
- **Haiku NOISE reason**: Gate definition with PASS/FAIL conditions; test specification, not theorem.
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
      376: - **Inputs**: M_KK compactification scale (computation canonical); 3He-A Kelvin-wave dispersion baseline (literature, Volovik monograph); FeSe NMR baseline Knight shift K_0 (literature, FeSe NMR review); 173Yb 3-b
      377: - **Gate**: `S86-W?-LAB-OBS-SI-TRANSLATION`. PASS iff each of 9 rows has a quantitative SI-unit prediction with stated experimental uncertainty band; INFO iff 6-8 of 9 rows translate cleanly; FAIL iff < 6 of 9 row
      378: - **Effort**: 2 plan slots (medium-large; literature-driven SI-mapping work; potentially needs paper-search MCP for baseline values). Highest-payoff carry-forward for making the lab-observable registry experimenta
      379: 
      380: ### CF-1B-b-6: K_R5 / K_crit knowledge-MCP provenance update
      381: 
      382: - **What**: The knowledge MCP currently reports `K_R5 = 1.9222` and `K_crit = 91.5` with NO provenance entries. Add provenance via `update_constant`: K_R5 source = W8-7 PASS (audit_sha256=ac5ba998... content_sha25
      383: - **Inputs**: Knowledge MCP `update_constant` tool; W8-7 / W8-2 / S84 W5-55 verdict-line SHAs; canonical_constants.py current entries (if any) for cross-check.
    ... +2 more lines

### proven_507
- **name**: Recomputed `sha256(s86_w3_pre_reg_inc_closure.py)` at synthesis time = `9252e6710fca3f7c0617536cdaffdd2ccc436bb12bf440f6
- **source_file**: sessions\session-86\workshops\session-86-1b-s13-gen-physicist.md
- **statement (DB field)**: Recomputed `sha256(s86_w3_pre_reg_inc_closure.py)` at synthesis time = `9252e6710fca3f7c0617536cdaffdd2ccc436bb12bf440f60ac96fa58ba4c9b0`.
- **Haiku NOISE reason**: Bare SHA-256 hash computation observation; audit-trail item, not substantive theorem.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
       98: 
       99: **Validation against v3 ladder sig_5** (`audit_sha256` uniqueness): the W3 sub-set is CLEAR (6 / 6 unique). However, an audit of the full `s86_gate_verdicts.txt` revealed THREE pre-existing duplicate `audit_sha256
      100: 
      101: ### Result 3: Pre-existing closure-script bytes drift after verdict emission (audit-provenance hazard)
      102: 
      103: **Result**: GEOMETRIC (verdict-file audit-trail invariant; not a substrate observation).
      104: 
      105: Cross-check verification:
    ... +6 more lines

### proven_86
- **name**: W4a-17 split-writer: `computations/s88_w4a_split_registry_writer.py` + `.json`
- **source_file**: sessions\permanent-results-registry.md
- **statement (DB field)**: W4a-17 split-writer: `computations/s88_w4a_split_registry_writer.py` + `.json`
- **Haiku NOISE reason**: Script file path label, no substantive statement.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
    16776: - W4a-16 audit_sha256: `63acc9cd17a2323d30f6c722792ff839400a9378e8307b496d1d456b1f30d731`
    16777: - W4a-16 content_sha256: `1912cc503085cf8b5abbcf7a184d10f385ebd3928275fd34691b930ca1f606d8`
    16778: - Workshop precedent SHA (S87 W1a-5 R3 Prompt-3): `9c0a290ef55b128b`
    16779: 
    16780: **Producing artifacts**:
    16781: - W4a-16 script: `computations/s88_w4a_a0_m2_backward_rescue_theorem.py`
    16782: - W4a-16 data: `computations/s88_w4a_a0_m2_backward_rescue_theorem.npz` + `.json`
    16783: - W4a-16 plot: `computations/s88_w4a_a0_m2_backward_rescue_theorem.png`
    ... +9 more lines

### proven_502
- **name**: Inputs**: `computations/canonical_constants.py`; the original session producing M_KK = 7.428660e+16 GeV (likely S52-S58 
- **source_file**: sessions\session-86\workshops\session-86-1a-s4-mack.md
- **statement (DB field)**: Inputs**: `computations/canonical_constants.py`; the original session producing M_KK = 7.428660e+16 GeV (likely S52-S58 era); MCP `mcp__knowledge__update_constant` interface.
- **Haiku NOISE reason**: Input enumeration from a carry-forward action item; not a theorem statement.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
      211: - **What**: `S87-LAB-FALSIFIER-S-LEVEL-PROPOSAL` — propose a new sub-A level `LAB-FALSIFIER-S` for rows with detection_ratio ≥ 100. Currently 7/9 rows clear this floor (SW1=XA1=58958, SW2=XB2=72.9, SW3=28.5, XA2=3
      212: - **Inputs**: `s86_w11_lab_falsifier_evoi_tree.csv` (9 rows with detection_ratio); `sessions/framework/evoi-framework.md` (current level ladder); W11 C6 verdict for current ladder definition (LAB-FALSIFIER A/B/C/D
      213: - **Gate**: `S87-LAB-FALSIFIER-S-LEVEL-PROPOSAL`. PASS = new level-S landed with sub-A threshold, 7/9 rows reassigned to level-S, lab-pillar joint P_decisive recomputed under new ladder. INFO = proposal lands but 
      214: - **Effort**: ~2 hours, 1 agent session (sagan-empiricist primary; mack-cosmic-bridge consult).
      215: 
      216: ### V.5. M_KK PROVENANCE add to canonical_constants.py
      217: 
      218: - **What**: `S87-M-KK-PROVENANCE-ADD` — add the missing PROVENANCE entry for `M_KK = 7.428660036284456e+16` GeV in `computations/ca
    ... +1 more lines

### proven_542
- **name**: Class 8.3 publication-precision residual**: `4.297733078528765e-06`
- **source_file**: sessions\session-87\session-87-results-workingpaper.md
- **statement (DB field)**: Class 8.3 publication-precision residual**: `4.297733078528765e-06`
- **Haiku NOISE reason**: Class metric value extracted from results bullet point, not a theorem
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
     8630:   - Level-2: structural envelope |α|·L⁻² + |β|·L⁻⁴ at L=12 = `0.23968614470710264`; observed gap |ρ(L=12) − ρ_∞| = `0.17547970226692144` ≤ structural envelope. PASS-STRUCTURAL-INFO-LITERAL (the plan-literal `L⁻² =
     8631:   - Level-3: corridor populated — numerical pinpoint at L=12 inside Level-2 envelope. PASS.
     8632:   - Level-4: open carry-forward populated (FERMIONIC-SIGNED-RESIDUE Connes-Karoubi pairing class). PASS.
     8633: 
     8634: **Results**:
     8635: 
     8636: - **rho_inf full float64**: `-0.8103647022669215` (presentation precision 10 sig figs: `-0.8103647023`; 4-sig-fig presentation only: ≈ −0.8104)
     8637: - **rho_inf published canonical pin**: −0.810369 (6 sig figs from canonical_constants.py:481, S86-W10-CANON-EXTRACT)
    ... +6 more lines

### proven_1210
- **name**: [T2] Breathing Mode Exclusion — delta g_ab^K = h(x)g_ab^K projects to 4D scalar, not tensor
- **source_file**: sessions/framework/Atlas/atlas-07-permanent-results.md
- **statement (DB field)**: Exact | 63 | VdD-Hawking
- **Haiku NOISE reason**: Partial header: exact precision tag and source only, no full statement.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
      159: | [NEW S62] BdG gauge fraction: gauge/gravity = 2.723 (structural formula) | 8 modes | Algebraic identity | 62 | `s62_bdg_gauge_fraction.py` |
      160: | [NEW S62] Delta > 0.353 M_KK along softest Hessian direction | 20 points | 7.1x threshold | 62 | `s62_type_i_transit.py` |
      161: 
      162: ### S63 Permanent Theorems (T1-T17) — NEW
      163: 
      164: | Result | Precision | Session | Source |
      165: |:-------|:----------|:--------|:-------|
      166: | [T1] Zero First-Order Tensor — homogeneous transit on M^4 x K: pi_ij=0 | Exact | 63 | VdD-Hawking |
    ... +9 more lines

### proven_725
- **name**: PRU compliance**: 19 machinery pins enumerated in plan §W6-5 §"Machinery pin (PRDR)" YAML; all consumed in script. No Cl
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: PRU compliance**: 19 machinery pins enumerated in plan §W6-5 §"Machinery pin (PRDR)" YAML; all consumed in script. No Class-8 cardinality gap.
- **Haiku NOISE reason**: PRU compliance note listing 19 pins; bookkeeping entry, not a theorem statement
- **Spot-check judgment**: **BORDERLINE**  -  prose-length name; may be theorem or narrative fragment
- **source_context (first 8 lines)**:
     1019: ##### (m) Self-assessment
     1020: 
     1021: - **Structural position**: CF-50 surfaces the empirical finding that the S84 W3-24 F_traj=(k+1)/2 closed-form theorem is an **atlas-row identity at locked-norm L_k=1**, NOT a cache-moment ratio. The plan's BdG-cac
     1022: - **Theorem preservation**: S84 W3-24 F_traj theorem is STRUCTURALLY PRESERVED at its atlas-row normalization domain — CF-50 does NOT falsify the theorem itself, only the plan's BdG-cache extension specification. 
     1023: - **Class-(d) PIN-DERIVATIVE pattern**: this is the 4th gate in W6 (after CF-46, CF-47, CF-49) where the plan's theorem-identity transfers from canonical normalization domain to BdG-cache direct evaluation, and ca
     1024: - **Downstream impact (CF-51)**: clause (d) F_traj dressing-ratio machinery in the §VII.U.2 Corner-II Stage-1-CANDIDATE corrigendum must be re-framed to atlas-row form (S84 W3-24 theorem) rath
    ... [truncated]

### proven_476
- **name**: Joint statement — "Landau structural block"**:
- **source_file**: sessions\session-85\session-85-w3-workingpaper.md
- **statement (DB field)**: Joint statement — "Landau structural block"**:
- **Haiku NOISE reason**: Section heading with trailing colon; 'Joint statement — "Landau structural block"**:' is a label, not a theorem.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      347:   |------|------------------|-------|-----------|-----------|
      348:   | BDI ↔ N_OP | [91.5, 91.5] (shared endpoint K_crit) | True | True | ✓ |
      349:   | BDI ↔ Two-speed | [1.922, 91.5] (full inflationary) | True | True | ✓ |
      350:   | BDI ↔ K-reg map | [1.922, 91.5] | True | True | ✓ |
      351:   | N_OP ↔ Two-speed | [91.5, 91.5] (shared endpoint) | True | True | ✓ |
      352:   | N_OP ↔ K-reg map | [91.5, 3.556e5] (full R7) | True | True | ✓ |
      353:   | Two-speed ↔ K-reg map | [1.922, 91.5] (full inflationary) | True | True | ✓ |
      354: 
    ... +9 more lines

### proven_246
- **name**: Individual resonances overlap completely and cannot be resolved
- **source_file**: sessions\archive\session-42\session-42-results-workingpaper.md
- **statement (DB field)**: Individual resonances overlap completely and cannot be resolved
- **Haiku NOISE reason**: Single bare claim without quantitative support or structural context; incomplete assertion about resonance overlap.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
      578: 
      579: (a) The Kosmann connection K_a is anti-Hermitian (K + K^dag = 0). This is proved from the metric compatibility of the Levi-Civita connection. When K_a is placed in the off-diagonal block of H_coupled, the full Ham
      580: 
      581: (b) Both crystals have discrete spectra. Fano interference requires a discrete state embedded in a CONTINUUM -- the continuum provides the smooth background against which the discrete state creates an asymmetric l
      582: 
      583: Nuclear analog: this is the distinction between an isobaric analog resonance (discrete isospin state in the neutron continuum, producing genuine Fano shapes with |q| ~ 0.1-3) and coupled intermediate structure in 
      584: 
      585: **2. V/D = 55 places the system firmly in the Ericson fluctuation regime.** The coupling exceeds the mean level spacing by 55x. In the Ericson regime:
    ... +3 more lines

### proven_665
- **name**: Session/Source: S89 / `S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2`
- **source_file**: sessions\session-90\session-90-w6-workingpaper.md
- **statement (DB field)**: Session/Source: S89 / `S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2`
- **Haiku NOISE reason**: Session/source metadata label extracted as standalone, not a theorem statement.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
       78: 
       79: ##### (b) Pin A + Pin B canonical PROVENANCE structure
       80: 
       81: **Pin A — Taylor 2nd-order canonical (PRE-EXISTING, S89 W3-7)**:
       82: 
       83: - Name: `kappa_2_substrate_FW`
       84: - Value: `0.021018084987437196`
       85: - Closed form: `(1/2) · d²/dτ² [5/(1−τ/(5π))]|_{τ=τ_fold} = 1/(5π² · A³)` with `A = 1 − τ_fold/(5π)`
    ... +9 more lines

## Table: gates  -  sampled 15 of 293 NOISE (5.1%)

### gate_T3-BATCH-S46-FWD-BWD-NS
- **name**: T3-BATCH-S46-FWD-BWD-NS
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3-BATCH archive batch tag; FWD-BWD-NS is algorithmic descriptor without session+wave+mechanism context.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
     6435:   # script_sha: fee920b1fe542959889d741c18269a55d3593a0cc2c5f98216fde57670e8d4a8
     6436:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6437: T3-BATCH-S46-FABRIC-TESSELLATION: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=e90b8098d7bcb2a0bd0bc00cd7fb1d12885a28e340fc617838998748bfd91d48
     6438:   # script: tier0-archive\s46_fabric_tessellation.py
     6439:   # script_sha: 67f23fd95546abab2a20947ca7320f99c9a38df24603d8e014fc315232c1fa78
     6440:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6441:   # input: s44_coherent_wall.npz f3aee88b3478b1b06e26431ca90f98db87f9ec850dbe6da053e93c509fbb7214
     6442:   # input: s44_voronoi_fnl.npz 3fb6061fc37411fad57b27f071a218c3a7d45a2d73ccadb03c1f0b67ddb633e6
    ... +8 more lines

### gate_ZFP
- **name**: ZFP
- **source_file**: sessions\session-84\session-84-s4-lrd-falsifier-synthesis.md
- **Haiku NOISE reason**: Acronym tag (Zero-Free-Parameter) without session or gate context
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
       15: - agent memory at `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md`
       16: 
       17: **Domain framing disclosure**: The calling persona is the JWST-LRD observer. The S84 falsifier expansion is not LRD-specific; per agent memory (Closed Channels §), "LRD demographics cannot discriminate framework f
       18: 
       19: ---
       20: 
       21: ## I. Session Outcome
       22: 
    ... +4 more lines

### gate_T3-BATCH-S56-POST-TRANSIT-COH
- **name**: T3-BATCH-S56-POST-TRANSIT-COH
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: Batch legacy migration gate; T3-BATCH prefix and MIGRATED value identify as archival artifact, not active computation.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
     1262:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     1263:   # input: s56_ba_spectrum.npz 57e2abd64c79478d20f00b0b051e086b102c9351d0b00d09e8a0ec7ebb9ab273
     1264:   # input: s56_cba_sound.npz e9a606964aca5b9da0bceca0f772e2c8e86673a125430600dd629a7ff8e27416
     1265:   # input: s54_scale_factor.npz 7533792ae42d59211f832cf596874b4f90fd3d228ca4762126d14854a30f4197
     1266: T3-BATCH-S56-OMEGA-ATT-CONFIRM: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=e788dc9cf716c529ba2263c73dd175d17800486562cdefd42069a9ec0748bfae
     1267:   # script: tier0-computation\s56_omega_att_confirm.py
     1268:   # script_sha: d69e5db25de558b44a52b5d2e93fe2f66f1a410dab7b716e5a36dd0a5e247eb3
     1269:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +8 more lines

### gate_QA-4
- **name**: QA-4
- **source_file**: sessions\archive\session-22\session-22a-synthesis.md
- **Haiku NOISE reason**: Bare label QA-4; lacks session+wave+mechanism chain required for real gate ID.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
        8: ---
        9: 
       10: ## I. EXECUTIVE SUMMARY
       11: 
       12: Session 22a executed all ten pre-registered zero-cost computations from existing `.npz` data. The session produced two COMPELLING results, two INTERESTING results, one CLOSED, two NEUTRAL results, one STRUCTURAL r
       13: 
       14: **The central finding**: No single computation provides a decisive stabilization mechanism. However, three independent results converge on the same tau window and, taken together, constitute a coherent dynamical p
       15: 
    ... +4 more lines

### gate_M3
- **name**: M3
- **source_file**: sessions\session-74\session-74-tesla-mack-bells-workshop.md
- **Haiku NOISE reason**: Single-letter bare label; no session/wave/mechanism context; generic pre-registration marker, not substantive gate ID.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
      584: 
      585: - Total signal run: 10^5 seconds at 1 Hz repetition = 10^5 shots
      586: - Controls 1-7: 10^5 seconds each, total 7 x 10^5 seconds = ~8 months of beam time
      587: - Total experiment duration: ~1 year after apparatus commissioning and calibration phases
      588: - Effective total running time from "first light" to "analysis complete": 3-5 years
      589: 
      590: **CONTINGENT**: the control battery is only meaningful if the predicted signal rate is well-specified. Currently the signal rate is contingent on the five OQ-TESLA pre-computations. If those return unfavorable, th
      591: 
    ... +6 more lines

### gate_I (if dispatched)
- **name**: I (if dispatched)
- **source_file**: sessions\session-89\session-89-phonon-first-synthesis.md
- **Haiku NOISE reason**: Bare 'I' with conditional prose is not a substantive gate ID.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
       91: Pre-registered finding format `success_predicate(observable_class, kernel_class, regulator_class, cohomology_class)` populated for each S89 substrate-IS gate. **§VII.U.2 4-corner classification**: Cell I = (algebr
       92: 
       93: | # | Gate ID | Verdict | Observable class | Kernel class | Regulator class | Cohomology class | Cell |
       94: |:--|:--------|:-------:|:-----------------|:-------------|:----------------|:-----------------|:----:|
       95: | 1 | **S89-A24-SUBSTRATE-IS-MELLIN-CONE-CLOSURE-DERIVATION** (W7a) | **PASS** | Cell I s=3 | AlgEx (Sage-QQ) | FI regulator-INVARIANT | Level-1 (regulator-invariant, L-independent) | I |
       96: | 2 | **S89-A24-C-SUB-CORRECTED-ANCHOR-VERIFICATION** (W7b) | **PASS** | Cell I s=3 | ClosedScalar (τ-fixed) | FI under Reading-A geometric resummation | Level-3 anchor satisfying Level-2 envelope by ∞-fold | I |
       97: | 3 | **S89-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU** (W7c) | **FAIL** (7/8 best emission) | Registry landing | Single-shot AFTER-patter
    ... [truncated]

### gate_T3-BATCH-S46-BAYESIAN-GP
- **name**: T3-BATCH-S46-BAYESIAN-GP
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3-BATCH prefix is non-substantive; S46-BAYESIAN-GP lacks wave subdivision and mechanism context.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
     6406:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6407: T3-BATCH-S46-ANOMALOUS-DISPERSION: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=7a64be1a8692f32ac3c71856dff13d1990f15940c205fba18f993e3004e2dcd2
     6408:   # script: tier0-archive\s46_anomalous_dispersion.py
     6409:   # script_sha: d61b72a7f70cfb7ae94511198ca34ab0b876bb3a1109778db4cf4847d8241ea9
     6410:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6411:   # input: s44_dos_tau.npz 6110848e7db2ebc4d034e03c30b6fc7ad02c3c4fcc66ce1e5af5134ca63251ff
     6412:   # input: s42_hauser_feshbach.npz 9a8ea436a0ee7f398c01d4e5c5a6af1af0f566f322298614187b70f3c97e4ba1
     6413:   # input: s45_collective_ns_rpa.npz 2c919bed2bbc13ee86fe1a66a5b57284fe75d8c036fb7d55051538b9e93fe9d6
    ... +8 more lines

### gate_E-4
- **name**: E-4
- **source_file**: sessions\archive\session-28\session-28a-results.md
- **Haiku NOISE reason**: Bare single-letter label (E-4) lacks session+mechanism context required for substantive gate ID.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
       12: | # | Gate | Verdict | Decisive Number | Feeds Into |
       13: |:--|:-----|:--------|:----------------|:-----------|
       14: | 28a-1 | KC-1 Parametric Injection | **PASS** | B_k(gap) = 0.023, Γ = 29,643 at τ=0.40 | 28c (KC-2 through KC-5) |
       15: | 28a-2 | L-1 Thermal Spectral Action | **CLOSED** | dF/dτ > 0 everywhere, all T | L-7 deprioritized |
       16: | 28a-3 | E-1 Lichnerowicz Decomposition | **DIAGNOSTIC** | 84-95% of gap² from curvature in (1,0)/(0,1) | Context for BCS |
       17: | 28a-4 | C-1 S_can vs S_LC | **CLOSED** | S_can monotone ↓, all smooth cutoffs | V-1 confirmed connection-independent |
       18: | 28a-5 | C-4 Spectral Correlations | **DIAGNOSTIC** | q_can=0.28 vs q_K=0.16, weak signal | Needs higher irreps |
       19: | 28a-6 | S-2 M_max vs C_2 Dispersion | **DIAGNOSTIC** | M_max ~ C_2^{-1.49}, μ_crit/λ_min ~ 0.95 | KC-2 phonon model |
    ... +9 more lines

### gate_T3-BATCH-S44-FOAM-CUTOFF
- **name**: T3-BATCH-S44-FOAM-CUTOFF
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3-BATCH archive batch; FOAM-CUTOFF is schema-free descriptive label lacking gate-ID substance.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
     6105:   # script_sha: c39dfd27fce1b1152d9d9da2a46f5d1e04ae674b22b0bdf50aee03efda63fb99
     6106:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6107:   # input: s42_gradient_stiffness.npz 77578ddd09e8d07292cc28bdb4db8039329f2d649910febe8a5fafd01f5cfeb6
     6108:   # input: s43_acoustic_metric.npz 59342902edefdbd2b897b6b67686fb6009980595ca4c78189ede30a5d544d906
     6109:   # input: s43_thermal_conductivity.npz f4a7d412b44e90bd3eb22e9d73d8225405b761608871dbc99f701bcc63ae3503
     6110:   # input: s43_kk_cmb_transfer.npz 22d0ace29254eb8204361e3089327fe759d3d383336d217caa7994b6245842d1
     6111:   # input: s42_constants_snapshot.npz 39f613507950979327f0d9b7473bd73f7b0a7ea2d9d0c5507f6b8b939909f80b
     6112:   # input: s36_sfull_tau_stabilization.npz 6a172dfc7fb0103f4cc6a9d37dc2fb2b944f8c357edf8825e0e9c9427c4cbe1e
    ... +7 more lines

### gate_T3-BATCH-S52-JACOBSON-MULTI-T
- **name**: T3-BATCH-S52-JACOBSON-MULTI-T
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: Batch tag; lacks wave partition and specific gate context required for real gate ID format.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
      683: T3-BATCH-S52-HFB-FULL: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=89fdce245ae62347536a84b8e7b6f97b3c79dceb15f257b8da29a2e7f8a77542
      684:   # script: tier0-computation\s52_hfb_full.py
      685:   # script_sha: 10a92fc6cb4ac5c5693e6b8987a0e47b38b94408f91d0a70ef2e602d82c0387c
      686:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
      687: T3-BATCH-S52-INSPECT-DATA: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=aec25f4ffe89b6f1af2891cda500b0dc4ee598fb9b3bf46bae167b41531156ea
      688:   # script: tier0-computation\s52_inspect_data.py
      689:   # script_sha: c7021d7bbfa1294c42f9ec3567bc1d50c7cb6ec605fcaf59508b46d8d7844d94
      690:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +7 more lines

### gate_S85-W7-CC-6
- **name**: S85-W7-CC-6
- **source_file**: computations\session-85\s85_gate_verdicts.txt
- **Haiku NOISE reason**: Bare label: truncated mechanism identifier lacking context; insufficient gate identity for substantive framework reference.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
      134: # S85-W7-BASELINE-HTILDE-DERIVATION dual-SHA: content_sha256=204d8ed1f0abe71bf62c9d9e4dd9df3b5d255ce12c2641a42297a105c3e7e78b audit_sha256=ae747b7be7a7a2cda3e7ef621655843dbccb9f8ad680ff085256f3651f2417f6
      135: S85-W8-2-CONVA-BDG-MICRO: PASS -- value=np.float64(2.9678753351715477e-16) scheme=NG_block convention=ConvA_coth L_max=8 audit_sha256=bdacff6c0e8d849259f8d9d40e45a8a8c5472ce6fd45776f2c09f258597cb0a8 content_sha256
      136: # audit_sha256 companion row: S85-W8-2-CONVA-BDG-MICRO audit=bdacff6c0e8d8492 content=d7c2709f474af8a8
      137: S85-W9-BOREL-FLOOR-REGISTRY-LANDING: PASS -- value=1.0 scheme=W10-121-original convention=Borel-disk-pointwise L_max=5 audit_sha256=5bea2a903af1415f70b0987b00d10f1bb8ba0ba0708cf8f12bffb9d06e0d1947 content_sha256=1
      138: # audit_sha256 companion row: S85-W9-BOREL-FLOOR-REGISTRY-LANDING audit=5bea2a903af1415f content=1d29d866ef31d7fc
      139: S85-W5-2-HP0-INTRA-CORRIDOR: FAIL -- value=3 scheme=5-regulator-atlas convention=CCM-2008-A_F-basis L_max=3 audit_sha256=4536d99702607605654c2979a4c58014e4f666a13d47f3cddeab6ff7feb4db8f content_sha256=d92909cf4352
      140: S85-W8-3-MUKHANOV-SASAKI-SUB-CORRIDOR-AUDIT: PASS -- value='4/5' scheme=Interp_A_primary convention=ConvA_coth L_max=5 audit_sha256=6eb8efb008e9374c
    ... [truncated]

### gate_GL-CUBIC
- **name**: GL-CUBIC
- **source_file**: sessions\archive\session-36\session-36-sagan-collab.md
- **Haiku NOISE reason**: Single-word entry; no session or wave context; bare mechanism tag.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
        5: **Re**: Session 36 Results -- The Lava Inside the Tube
        6: 
        7: ---
        8: 
        9: ## Section 1: Key Observations
       10: 
       11: Session 36 is the most computationally dense session in the project's history: 14 gates, 11 agents, 4 waves. The results divide cleanly into two categories that I want to name plainly.
       12: 
    ... +6 more lines

### gate_fw_gates_22
- **name**: λ_fs (WDM)
- **source_file**: sessions/framework/ARCHIVE/baseline-findings-s66.md
- **Haiku NOISE reason**: Observable label 'λ_fs (WDM)' with no gate ID or session context; noise.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      250: 
      251: | Observable | Framework | Observed | Tension | Verdict |
      252: |:-----------|:----------|:---------|:--------|:--------|
      253: | Ω_DM h² (Leggett-only) | 0.120 | 0.1186±0.0020 | 0.7σ | PASS |
      254: | z_eq (Leggett) | 3425 | 3402±26 | 0.88σ | PASS |
      255: | σ/m | 0 | <1.25 cm²/g | — | PASS |
      256: | Direct detection | 0 | null | — | PASS |
      257: | Annihilation | 0 | null | — | PASS |
    ... +9 more lines

### gate_L-1
- **name**: L-1
- **source_file**: sessions\archive\session-28\session-28a-results.md
- **Haiku NOISE reason**: Bare single-letter label (L-1) without substantive gate ID combining session/wave/mechanism.
- **Spot-check judgment**: **AGREE**  -  bare ID fragment (e.g. KC-2, L-1)
- **source_context (first 8 lines)**:
        7: 
        8: ---
        9: 
       10: ## I. GATE VERDICTS
       11: 
       12: | # | Gate | Verdict | Decisive Number | Feeds Into |
       13: |:--|:-----|:--------|:----------------|:-----------|
       14: | 28a-1 | KC-1 Parametric Injection | **PASS** | B_k(gap) = 0.023, Γ = 29,643 at τ=0.40 | 28c (KC-2 through KC-5) |
    ... +9 more lines

### gate_T3-BATCH-S45-KRETSCHNER
- **name**: T3-BATCH-S45-KRETSCHNER
- **source_file**: computations\session-81\s81_batch_gate_verdicts.txt
- **Haiku NOISE reason**: T3-BATCH prefix is round-name noise; bare mechanism name without wave context.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
     6287: T3-BATCH-S45-GGE-BEATING: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=ec0176d0e57e21e4b31ea50fd2283afa26010dc9c013156dbe2db3378974ca6d
     6288:   # script: tier0-archive\s45_gge_beating.py
     6289:   # script_sha: 43fad8e6d394d84493715c0151b4e60c503c3a080cddcacc079d2b995532f256
     6290:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
     6291: T3-BATCH-S45-GL-GGE: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=a0503fa39f32d82cd8caf4f6f2a25625b9c730cbda174c89adf59dca6898b878
     6292:   # script: tier0-archive\s45_gl_gge.py
     6293:   # script_sha: 0dea8641b510d3fda5e7dd122b527171493d2b856ac9cdadcfe44367fc297053
     6294:   # canon_sha:  68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
    ... +8 more lines

## Table: data_provenance  -  sampled 10 of 186 NOISE (5.4%)

### prov_431
- **name**: unexpanded_sa
- **source_file**: computations/session-45/s45_unexpanded_sa.py
- **Haiku NOISE reason**: Session 45 does not exist in framework (framework starts at S50 per memory); script path is invalid.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      922:     # Key results
      923:     'min_c4_over_c2': min_ratio,
      924:     'taylor_20term_error': abs(S_exact - S_taylor) / abs(S_exact),
      925: 
      926:     # Gate
      927:     'gate_verdict': np.array([gate_verdict]),
      928: }
      929: 
    ... +9 more lines

### prov_264
- **name**: gsl_transit
- **source_file**: computations/session-40/s40_gsl_transit.py
- **Haiku NOISE reason**: Session-40 nonexistent; gsl_transit is speculative future work; no S39 integrability baseline ever computed.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      789: 
      790: # ======================================================================
      791: #  Step 11: Save data
      792: # ======================================================================
      793: print("\n" + "=" * 78)
      794: print("STEP 11: SAVE DATA")
      795: print("=" * 78)
      796: 
    ... +9 more lines

### prov_96
- **name**: connes_workshop_legacy
- **source_file**: computations/session-25/s25_connes_workshop_legacy.py
- **Haiku NOISE reason**: session-25/s25_connes_workshop_legacy.py is legacy/abandoned code with no outputs declared.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name 'connes_workshop_legacy' not found in source>
    --- file head ---
        1: """
        2: Connes-NCG-Theorist Workshop Computations -- Session 25
        3: =======================================================
        4: Computes all NOT COMPUTED items from the Connes collab document
        5: and the Investigation Effort documents.
        6: 
    ... +24 more lines

### prov_372
- **name**: first_sound_imprint
- **source_file**: computations/session-44/s44_first_sound_imprint.py
- **Haiku NOISE reason**: Session 44 does not exist; script path is invalid.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
     1056: # ============================================================
     1057: # SAVE RESULTS
     1058: # ============================================================
     1059: 
     1060: print(f"\n{'='*70}")
     1061: print("SAVING RESULTS")
     1062: print(f"{'='*70}")
     1063: 
    ... +9 more lines

### prov_1197
- **name**: squeeze_reconciled
- **source_file**: computations/session-69/s69_squeeze_reconciled.py
- **Haiku NOISE reason**: Script file computations/session-69/s69_squeeze_reconciled.py does not exist.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: #!/usr/bin/env python3
        2: """
        3: s69_squeeze_reconciled.py -- NON-BD-SQUEEZE-RECONCILED-69 (W1-F)
        4: ================================================================
        5: Variance-weighted r_eff and cosh(2r_eff) from 8-band BCS coherence factors
        6: with proper van Hove spectral weighting.
        7: 
        8: Reconciles the Lizzi-Transit naive estimate (0.26-0.50 OOM) with the
    ... +3 more lines

### prov_398
- **name**: cc_gap_update
- **source_file**: computations/session-45/s45_cc_gap_update.py
- **Haiku NOISE reason**: Consolidation script with no actual output files (empty outputs field); summary-only to stdout.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: """
        2: s45_cc_gap_update.py — CC Gap Update with ALL S45 Results (CC-GAP-UPDATE-45)
        3: 
        4: Consolidates all S45 CC-relevant computations into an updated gap picture.
        5: Inputs: 10 NPZ files from S44-S45 + canonical_constants.py.
        6: Output: Summary to stdout (written into W5-R1 of working paper).
        7: 
        8: Author: Gen-Physicist
    ... +2 more lines

### prov_357
- **name**: bayesian_f
- **source_file**: computations/session-44/s44_bayesian_f.py
- **Haiku NOISE reason**: Session-44 script path does not exist; s44_bayesian_f.py not found in the repository.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      755:     s43_grav_log10=s43_grav,
      756:     s43_gauge_log10=s43_gauge,
      757:     sigma_alpha_th=sigma_alpha_th,
      758:     # Gate
      759:     gate_name=np.array(['BAYESIAN-f-44']),
      760:     gate_verdict=np.array(['INFO']),
      761: )
      762: 
    ... +9 more lines

### prov_605
- **name**: ginzburg_fabric
- **source_file**: computations/session-53/s53_ginzburg_fabric.py
- **Haiku NOISE reason**: Script has no outputs listed and hardcoded output text path is suspicious stub pattern.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
       22: from canonical_constants import (
       23:     Vol_SU3_Haar, N_cells, xi_BCS, xi_GL, Delta_0_GL, E_B2_mean,
       24:     J_C2, J_su2, J_u1, L_over_xi, a_GL, b_GL, E_cond, barrier_0d,
       25:     rho_B2_per_mode, E_B1, E_B3_mean, T_acoustic, PI,
       26:     omega_PV, N_dof_BCS, E_cond_ED_8mode,
       27: )
       28: 
       29: # Output file
    ... +9 more lines

### prov_1217
- **name**: desi_dr3_update
- **source_file**: computations/session-70/s70_desi_dr3_update.py
- **Haiku NOISE reason**: session-70 does not exist in computations directory; no substantive script path
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: #!/usr/bin/env python3
        2: """
        3: s70_desi_dr3_update.py -- DESI-DR3-UPDATE-70: Decision Tree Update with S69-S70 Results
        4: ========================================================================================
        5: Gate: DESI-DR3-UPDATE-70
        6:   INFO: Updated decision tree and discriminating power forecast.
        7: 
        8: Physics:
    ... +3 more lines

### prov_263
- **name**: collective_inertia
- **source_file**: computations/session-40/s40_collective_inertia.py
- **Haiku NOISE reason**: Session-40 nonexistent; collective_inertia refers to fabricated S39 inputs (s39_cascade_spectroscopy.npz, s39_fubini_study.npz never produced).
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: #!/usr/bin/env python3
        2: """
        3: s40_collective_inertia.py  --  ATDHFB Collective Inertia at the Fold (M-COLL-40)
        4: 
        5: Computes the cranking-model collective inertia M_coll(tau) for the BCS condensate
        6: on the deformed SU(3) internal space.
        7: 
        8: The Inglis-Belyaev (IB) and ATDHFB cranking masses are:
    ... +3 more lines

## Table: session_files  -  sampled 4 of 4 NOISE (100.0%)

### sf_63:session-63-W7-workingpaper.md
- **name**: session-63-W7-workingpaper.md
- **source_file**: sessions/session-63/session-63-W7-workingpaper.md
- **Haiku NOISE reason**: Wave 7 template stub (10 KB) with agent instructions but no completed gate entries—only section header and 'NOT STARTED' status.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
    <name 'session-63-W7-workingpaper.md' not found in source>
    --- file head ---
        1: # Session 63 Wave 7 Working Paper
        2: 
        3: **Date**: 2026-03-30
        4: **Session**: S63 — Folding CC
        5: **Format**: Parallel single-agent computations across 7 waves
        6: **Plan**: `sessions/session-plan/session-63-plan.md`
    ... +24 more lines

### sf_66:session-66-wrapup.md
- **name**: session-66-wrapup.md
- **source_file**: sessions/session-66/session-66-wrapup.md
- **Haiku NOISE reason**: Stub file with 'to be filled' placeholder; only header and computation listing without substantive content.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
    <name 'session-66-wrapup.md' not found in source>
    --- file head ---
        1: # Session 66 Wrapup: Spectral Ops. Engagement
        2: 
        3: **Date**: 2026-04-04
        4: **Session**: 66
        5: **Format**: 8-wave parallel computation (37 tasks) + 10 collab reviews + 5 workshops + inflation deep dive + Bellazzini analysis
        6: **Planner**: lizzi-spectral-functional-theorist
    ... +24 more lines

### sf_sessions/framework/registry/_registry-template.md
- **name**: _registry-template.md
- **source_file**: sessions/framework/registry/_registry-template.md
- **Haiku NOISE reason**: Template file with placeholder content and instruction comments, not a substantive registry entry; belongs in framework/Templates, not framework/registry.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
    <name '_registry-template.md' not found in source>
    --- file head ---
        1: ---
        2: type: registry-template
        3: ingested-by: /weave --update
        4: ---
        5: 
        6: # &lt;Registry Name&gt;
    ... +24 more lines

### sf_sessions/session-plan/archive/session-29Aa-prompt.md
- **name**: session-29Aa-prompt.md
- **source_file**: sessions/session-plan/archive/session-29Aa-prompt.md
- **Haiku NOISE reason**: Path fragment is malformed (missing session number in anchor_id; says session='' in JSON), reads as session-29Aa-prompt.md but labeled with sessions/ prefix fragment.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
    <name 'session-29Aa-prompt.md' not found in source>
    --- file head ---
        1: # Session 29Aa: KC-3 Closure + Entropy Balance
        2: 
        3: **Date**: 2026-02-28
        4: **Author**: Hawking (hawking-theorist), dissected by team-lead
        5: **Depends on**: Session 28 (all sub-sessions: 28a KC-1 PASS, 28b self-consistent tau-T, 28c phonon T-matrix + van Hove BCS + Luttinger + steady-state mu)
        6: **Input data**:
    ... +24 more lines

## Table: equations  -  sampled 8 of 144 NOISE (5.6%)

### eq_18026
- **name**: diff = (W14-4_block before CF-27) XOR (W14-4_block after CF-27)
- **source_file**: sessions\session-plan\archive\session-87-plan-w4.md
- **Haiku NOISE reason**: Document operation descriptor (XOR on text blocks), not a mathematical or physics equation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
      395: 
      396: ```
      397: Step 1 (definitions):
      398:   W14-4_block       = current text at session-86-w14-workingpaper.md:414-422
      399:   locked_text       = pre-registered replacement text (source: S86 W-4 R3 joint-recommendation block)
      400:   inventory_row_f_NL_folded = Master Inventory row #9 (per CF-28; pre-split)
      401: 
      402: Step 2 (substitution):
    ... +9 more lines

### eq_16707
- **name**: beta_s = -0.1331 pin to 4.19e-5 = 42 ppm, 239x below the 1% PASS
- **source_file**: sessions\session-85\session-85-s3-alphas-registry-landau.md
- **Haiku NOISE reason**: Prose summary of numerical match to threshold; not an equation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
       69:    postulate; it follows symbolically (exact, Sage-verified residual 0)
       70:    from the OZ moment structure. Equivalently: the three OZ moments
       71:    satisfy a LANDAU-MINKOWSKI closure where the third moment is
       72:    algebraically determined by the first two.
       73: 
       74: 3. The chain-rule identity, evaluated at Planck n_s_canon = 0.9649 and
       75:    alpha_s_framework = -0.068968, yields
       76:    beta_s_derived = -0.13309442710..., matching the canonical
    ... +9 more lines

### eq_1843
- **name**: E_gs = 1.4025899717 (delta = -2.5872%)
- **source_file**: computations\session-52\s52_hfb_full_output.txt
- **Haiku NOISE reason**: Computation output line (E_gs value with iteration count) from HFB convergence log, not equation form.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
      110:   alpha_ph = 1.00: conv=True (47 iter)
      111:     E_gs = 1.4263553232 (delta = -0.9367%)
      112:     E_sp shift: max|Sigma| = 6.47e-02
      113:     n_k = [0.23288519 0.22240032 0.18452706 0.16981246 0.1767792  0.00404714
      114:  0.00435947 0.00518917]
      115:     n_B2=0.809625, n_B1=0.176779, n_B3=0.013596
      116: 
      117:   alpha_ph = 1.50: conv=True (46 iter)
    ... +9 more lines

### eq_21728
- **name**: (content_sha256=`e2ca24d63cdbdcca3c42b0c1841681134e9128f9d939b0af6f4e8f4e200882d3`,
- **source_file**: sessions\framework\registry\falsifier-master-inventory.md
- **Haiku NOISE reason**: SHA hash metadata embedded in prose; not a mathematical equation.
- **Spot-check judgment**: **AGREE**  -  name extracted as bullet sub-clause inside larger theorem/proof
- **source_context (first 8 lines)**:
      192:     (NOT scheme artifact; the dual prediction is real substrate physics)
      193:   - Registered tags: `DUAL_PATHWAY=true`, `SCHEME_FLOOR_EXCEEDED=true`
      194: 
      195: **SEQUENCED detector chain** (Stage 1 -> Stage 2):
      196: 
      197:   *Stage 1 (2026)* - **BK-Array (BICEP/Keck Array)**: first-light data
      198:   publication target 2026; pre-registered 4-branch decision tree per
      199:   S84 W4-42 `S84-BICEP-KECK-2026-PRE-REGISTER`
    ... +9 more lines

### eq_17606
- **name**: convention=W13-2-forward-map+f_LISA-pivot+log-log-interp
- **source_file**: sessions\session-plan\archive\session-86-plan-w8.md
- **Haiku NOISE reason**: Metadata convention tag from verdict-line format specification, not a mathematical equation.
- **Spot-check judgment**: **AGREE**  -  YAML pin / convention-tag (not a mathematical equation)
- **source_context (first 8 lines)**:
      583:      PASS/INFO/FAIL bands, contrast to W13-2 band_width proxy)
      584:   - computations/s86_gate_verdicts.txt: canonical verdict line
      585:     + dual-SHA companion row.
      586: 
      587: Verdict line format:
      588:   S86-CGWB-LMAX-DIRECT: PASS|FAIL|INFO
      589:     -- value=(Omega_L8=<v>, Omega_L10=<v>, delta_rel=<v>)
      590:     scheme=L_max-direct-truncation-comparison
    ... +9 more lines

### eq_8784
- **name**: L_max=10 audit_sha256=<computed at runtime>
- **source_file**: sessions\session-89\workshops\s89-w2-r-canonical-observable-identity.md
- **Haiku NOISE reason**: Verdict-line specification string with placeholder SHA values, not a mathematical equation.
- **Spot-check judgment**: **AGREE**  -  numerical result line in gate verdict-file output
- **source_context (first 8 lines)**:
     2376: 
     2377: **Audit-trail signature (anticipated)**:
     2378: 
     2379: ```
     2380: S90-W2-1-RETRY-OBSERVABLE-IDENTITY-RESOLVED: PASS -- value='R_canonical=7.324974378387362;
     2381:   xc1=True;xc1_rel_dev=2.41e-06;substrate_IS_observable=cocycle_ratio_Cell_I_INVARIANT_s3_FI_IDENTITY'
     2382:   scheme=Hochschild-cocycle-times-Chern-character
     2383:   convention=BdG-restricted-Connes-Karoubi-pairing-Cell-I-class-8.3-tolerance-compliant
    ... +9 more lines

### eq_5304
- **name**: Aitken Delta^2 (L=3,4,5, Gaussian):
- **source_file**: computations\session-66\s66_kk_threshold_l5_results.txt
- **Haiku NOISE reason**: Section heading only (RICHARDSON EXTRAPOLATION); no actual equation formula.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
      141:     3       0.35487823     2.742890
      142:     4       0.63943005     1.801829
      143:     5       0.77726154     1.215554
      144:     6       0.43249734     0.556437
      145: 
      146: ================================================================================
      147: 5. RICHARDSON EXTRAPOLATION
      148: ================================================================================
    ... +9 more lines

### eq_6978
- **name**: resolution_time = mid-session, AFTER plan-freeze — the
- **source_file**: sessions\session-85\workshops\s85-w3-methodology-debts.md
- **Haiku NOISE reason**: Document prose (plan-freeze timing statement) wrapped in substitution step labels, not an equation.
- **Spot-check judgment**: **DISAGREE**  -  algebraic identity with no table/bullet/verdict/pin context
- **source_context (first 8 lines)**:
     1263:         verdict.                                                          [definition]
     1264: Step 2: For sym/ref/top.AMRI/mth-i/mth-iii/aut.external-source/aut.band-change:
     1265:         resolution_time = plan-freeze (mechanical static analysis).      [substitution]
     1266: Step 3: For top.regulator (W1b-1 sub-tree flip A1->B2):
     1267:         the regulator-stratification axis (L_max ∈ {8, 10, 12}) is
     1268:         STATICALLY KNOWN at plan-freeze, but whether the cell-flip
     1269:         manifests requires partial execution at L=10 and L=12.            [substitution]
     1270: Step 4: For top.AMRI mid-session (W4-8 user-directive-flagged):
    ... +9 more lines

## Table: researchers  -  sampled 2 of 2 NOISE (100.0%)

### researcher_Lost-Treasures
- **name**: Lost-Treasures
- **source_file**: researchers/Lost-Treasures/index.md
- **Haiku NOISE reason**: Source file not found and paper count is zero; empty or deleted stub folder.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
    <source file not found: researchers\Lost-Treasures\index.md>

### researcher_RF-Antimatter
- **name**: RF-Antimatter
- **source_file**: researchers/RF-Antimatter/index.md
- **Haiku NOISE reason**: Index file not found; folder contains only 1 paper with empty description (missing metadata).
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
    <source file not found: researchers\RF-Antimatter\index.md>

## Table: constants  -  sampled 2 of 2 NOISE (100.0%)

### const_Vol_SU3_WRONG
- **name**: Vol_SU3_WRONG
- **source_file**: computations/_shared/canonical_constants.py
- **Haiku NOISE reason**: Deprecated constant marked DO NOT USE; explicitly flagged as wrong incorrect value kept only for audit trail.
- **Spot-check judgment**: **AGREE**  -  name extracted from markdown table cell (context shows table structure)
- **source_context (first 8 lines)**:
      303: # Residual (closed-form vs L=14 measured): |delta_A| = 5.23e-5, |delta_B| = 2.62e-5
      304: # under "10/(1 - tau/(5*pi))" form; |delta_A| = 3.44e-5, |delta_B| = 1.72e-5 under
      305: # the 2nd-truncation form "10*(1 + tau/(5*pi) + (tau/(5*pi))^2)". Both well within
      306: # the W1b-HK-5 PASS threshold 1e-3.
      307: 
      308: # SU(3) Haar volume — the CORRECT Weyl integration formula
      309: # S44 CORRECTION: 8*sqrt(3)*pi^4 = 1349.74 (replaces wrong sqrt(3)*(4*pi^2)^3/12 = 8880.93)
      310: Vol_SU3_Haar = 8.0 * np.sqrt(3) * PI**4   # = 1349.74 (S44 s44_constants_corrected)
    ... +9 more lines

### const_lambda_unit_canonical
- **name**: lambda_unit_canonical
- **source_file**: computations/_shared/canonical_constants.py
- **Haiku NOISE reason**: Value is string literal 'dimensionless_M_KK_natural' (not numerical); placeholder-form constant for unit labeling rather than physics value.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
      555: V2_weight_FW_sum = 23  # Schur-projected real-dim functional on A_F, sum across all 3 blocks = 1+4+18 = 23 = real_dim(A_F). Canonical Connes-Marcolli 2008 Thm 11.1; A_F = C+H+M_3(C) Connes-Chamseddine canonical em
      556: a_0_FW_zeta = 6440.0  # zeta-regulated zeroth Seeley-DeWitt coefficient of D_K^2 at tau_fold; substrate dimensionless mode count (a_0 = zeta_{D_K}(0) = Tr(1)) per CCM 2007 + S64 / S77 R-protection; W11-124 canonic
      557: a_2_FW_zeta = 2776.165389  # zeta-regulated second Seeley-DeWitt coefficient of D_K^2 at tau_fold; spectral-zeta sum a_2(spectral, S42) = 2776.165389; S46 a_2 split = a_2^zeta / a_2^SD = 2776.165389 / 0.7282349726
      558: xi_KZ_FW = 0.018760052113614717  # Substrate-natural xi_KZ derived from atlas T1 dt/T_L=1.25e-5 + Bogoliubov-unitary BdG-A_2 (nu=1/2, z=1, m=1/3) + S53 xi_BCS-analog 0.808346 M_KK^-1. M_KK^-1 units. Closes S88 W-2
      559: kappa_2_substrate_FW = 0.021018084987437196  # CM-1995 §III.4 second-order Jensen perturbation on HK-5 closed form 5/(1-tau/(5*pi)); kappa_2 = 1/(5*pi^2 * A^3) with A = 1 - tau_fold/(5*pi) at tau_fold = 0.19. Subs
      560: t
    ... [truncated]

## Table: registries  -  sampled 4 of 4 NOISE (100.0%)

### registry_Phononic-Crystal-Geometry
- **name**: Phononic Crystal Geometry of SU(3)
- **source_file**: sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md
- **Haiku NOISE reason**: Archived registry (superseded by Phononic-Substrate-Geometry); marked ARCHIVED per container-thinking reframe.
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
        1: ---
        2: ARCHIVED: 2026-05-10
        3: Last meaningful session: S41 (Fabric Discovery; superseded mid-S86)
        4: Superseded by: sessions/framework/Phononic-Substrate-Geometry.md
        5: Reason: Phononic-Crystal-Geometry framing replaced by Phononic-Substrate-Geometry framing post-S86 (substrate IS the spectral triple, not a crystal IN a container); per phononic-framing.md IS-not-IN substrate-dire
        6: ---
        7: 
        8: # Phononic Crystal Geometry of SU(3)
    ... +8 more lines

### registry__registry-template
- **name**: &lt;Registry Name&gt;
- **source_file**: sessions/framework/registry/_registry-template.md
- **Haiku NOISE reason**: Template stub file with placeholder text, not a substantive registry entry.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: ---
        2: type: registry-template
        3: ingested-by: /weave --update
        4: ---
        5: 
        6: # &lt;Registry Name&gt;
        7: 
        8: > **This is a template.** Copy to `sessions/framework/<slug>.md`, replace every `<...>` placeholder, delete this blockquote. `/weave --update` will ingest the resulting file into `tools/knowledge.db`.
    ... +6 more lines

### registry_framework-bbn-hypothesis
- **name**: Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade
- **source_file**: sessions/framework/ARCHIVE/framework-bbn-hypothesis.md
- **Haiku NOISE reason**: Archived file with SUPERSEDED status marker; conceptual hypothesis without computational closure.
- **Spot-check judgment**: **BORDERLINE**  -  uncertain
- **source_context (first 8 lines)**:
        1: ---
        2: ARCHIVED: 2026-05-10
        3: Last meaningful session: S36
        4: Superseded by: sessions/framework/framework-parametric-amplification.md + sessions/framework/Phononic-to-Cosmos.md
        5: Reason: BBN hypothesis from S36 transit-dynamics era; superseded by parametric-amplification framework + cosmological mapping; modern accounting at atlas-07 §VII registry slots
        6: ---
        7: 
        8: # Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade
    ... +8 more lines

### registry_lrd-observational-constraints
- **name**: LRD Observational Constraints Registry
- **source_file**: sessions/framework/registry/lrd-observational-constraints.md
- **Haiku NOISE reason**: Stub registry with minimal content (3 lines of header only, truncated at line 9).
- **Spot-check judgment**: **BORDERLINE**  -  short title; insufficient evidence to judge
- **source_context (first 8 lines)**:
        1: # LRD Observational Constraints Registry
        2: 
        3: **Registry ID**: `lrd-observational-constraints`
        4: **Owner agent(s)**: `little-red-dots-jwst-analyst`
        5: **Last updated**: `2026-04-23, S85-W4 AMRI migration`
        6: **Ingestion**: `/weave --update`; `knowledge.db` stores rows under `closed | open` per entry status.
        7: 
        8: ---
    ... +1 more lines
