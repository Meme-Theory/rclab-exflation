# NOISE Coverage Check - loose search results

Sample source: `tools\_noise_spot_check_seed43.md`
Sample size: 122 NOISE entries
Min key length: 15 chars (normalized)
VALID index size: 8704 entries (cross-table)
Source corpus: 4430 files loaded

## Aggregate (tiered priority — first match wins)
- **Tier 1 PRESERVED_IN_VALID_INDEX**: **6** (4.9%)  -  content in another VALID entry
- **Tier 2 PRESERVED_IN_SAME_FILE_MULTI**: **9** (7.4%)  -  multiple occurrences in own source
- **Tier 3 PRESERVED_IN_OTHER_SOURCE**: **22** (18.0%)  -  content appears in another file
- **PRESERVED total** (any tier): **37** (30.3%)
- **ORPHANED** (no match anywhere): **57** (46.7%)
- TOO_SHORT_TO_SEARCH: 28
- MISSING_FROM_BATCHES: 0

## Per-table breakdown

| Table | Total | T1-index | T2-same-file | T3-other-src | Orphaned | Too short |
|:------|----:|----:|----:|----:|----:|----:|
| closed_mechanisms | 2 | 0 | 0 | 0 | 0 | 2 |
| constants | 2 | 0 | 1 | 0 | 0 | 1 |
| data_provenance | 10 | 1 | 3 | 1 | 1 | 4 |
| equations | 8 | 1 | 2 | 1 | 4 | 0 |
| gates | 14 | 0 | 0 | 0 | 6 | 8 |
| open_channels | 25 | 3 | 1 | 7 | 7 | 7 |
| registries | 4 | 0 | 0 | 0 | 4 | 0 |
| researchers | 2 | 0 | 0 | 0 | 0 | 2 |
| session_files | 4 | 0 | 0 | 4 | 0 | 0 |
| theorems | 51 | 1 | 2 | 9 | 35 | 4 |

**Reading**: PRESERVED at any tier means dropping the NOISE entry doesn't lose content. ORPHANED means the math appears once, only in the noise's own source location — those are the real review priority (potential content loss).

---

## ORPHANED entries (real review priority)

### open_247  (open_channels)
- name: `Combined conservative`
- key: `combined conservative`
- own-file occurrences: 1 in `sessions/session-62/session-62-results-workingpaper.md`

### open_473  (open_channels)
- name: `FWD-C5 bridge family`
- key: `fwd-c5 bridge family`
- own-file occurrences: 1 in `sessions/session-91/session-91-w5-workingpaper.md`

### open_2  (open_channels)
- name: `W2 C10 verdict line (INFO, value 280743+0j, analytic-continuation, off-pole-Hankel)`
- key: `w2 c10 verdict line (info, value 280743+0j, analytic-continuation, off-pole-hankel)`
- own-file occurrences: 1 in `sessions/session-86/seeds/_seed-w10.md`

### open_455  (open_channels)
- name: ``s86-cluster-results.md` (memory)`
- key: `s86-cluster-results.md (memory)`
- own-file occurrences: 1 in `sessions/session-87/session-87-results-workingpaper.md`

### open_569  (open_channels)
- name: `Lefschetz n* = 60 promoted to permanent** (W3-C)`
- key: `lefschetz n = 60 promoted to permanent (w3-c)`
- own-file occurrences: 1 in `sessions/session-75/session-75-tesla-synthesis.md`

### open_60  (open_channels)
- name: `C-D (dilution / Volovik H²-scaling)`
- key: `c-d (dilution / volovik h²-scaling)`
- own-file occurrences: 1 in `sessions/permanent-results-registry.md`

### open_691  (open_channels)
- name: `Gates FAILED / NOT FIRE`
- key: `gates failed / not fire`
- own-file occurrences: 1 in `sessions/framework/registry/constraint-mega-matrix.md`

### proven_1133  (theorems)
- name: `8D Petrov Classification of Jensen-Deformed SU(3)** -- Type D at tau=0 (Einstein manifold), algebraically general with 8 distinct eigenvalues at all tau > 0. Stable multiplicity st`
- key: `8d petrov classification of jensen-deformed su(3) -- type d at tau=0 (einstein manifold), algebraically general with 8 distinct eigenvalues at all tau > 0. stab`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_698  (theorems)
- name: `Plan-vs-registry attribution reconciliation**: plan §W6-3 enumerated a 5-clause W-3 R3 attribution targeting the worksho`
- key: `plan-vs-registry attribution reconciliation: plan §w6-3 enumerated a 5-clause w-3 r3 attribution targeting the worksho`
- own-file occurrences: 1 in `sessions/session-90/session-90-w6-workingpaper.md`

### proven_1276  (theorems)
- name: `[NEW S45] Bogoliubov/KZ n_s (all k-mappings)`
- key: `[new s45] bogoliubov/kz n_s (all k-mappings)`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_1232  (theorems)
- name: `Bogoliubov Gaussianity Preservation: f_NL = O(eps) regardless of squeezing`
- key: `bogoliubov gaussianity preservation: f_nl = o(eps) regardless of squeezing`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_1381  (theorems)
- name: `HESS-40 (27th equilibrium closure), T_acoustic agreement (0.7%), 11 gates`
- key: `hess-40 (27th equilibrium closure), t_acoustic agreement (0.7%), 11 gates`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_336  (theorems)
- name: `W5-D** is the computational verification of one specific NUMERICAL_L3 item`
- key: `w5-d is the computational verification of one specific numerical_l3 item`
- own-file occurrences: 1 in `sessions/session-73b/session-73b-results-workingpaper.md`

### proven_713  (theorems)
- name: `Calibration corpus instance for deferred-pending sub-class**: CF-49 is K=2 calibration instance of `cross-pillar-bridge-`
- key: `calibration corpus instance for deferred-pending sub-class: cf-49 is k=2 calibration instance of cross-pillar-bridge`
- own-file occurrences: 1 in `sessions/session-90/session-90-w6-workingpaper.md`

### proven_302  (theorems)
- name: `SU(3) (8-dim manifold)`
- key: `su(3) (8-dim manifold)`
- own-file occurrences: 1 in `sessions/session-66/session-66-results-workingpaper.md`

### proven_1280  (theorems)
- name: `[NEW S48] Q-theory self-tuning Goldstone mass`
- key: `[new s48] q-theory self-tuning goldstone mass`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_65  (theorems)
- name: `K-counter advancement**: substrate-input-orthogonality K=2 → K=3 (SUGGESTION → MANDATORY status promotion event at S90 W`
- key: `k-counter advancement: substrate-input-orthogonality k=2 → k=3 (suggestion → mandatory status promotion event at s90 w`
- own-file occurrences: 1 in `sessions/permanent-results-registry.md`

### proven_1892  (theorems)
- name: `§XIII methodology-floor axis`
- key: `§xiii methodology-floor axis`
- own-file occurrences: 1 in `sessions/framework/registry/constraint-mega-matrix.md`

### proven_326  (theorems)
- name: `W5-D asks "is this one NUMERICAL result L_max-invariant?"`
- key: `w5-d asks "is this one numerical result l_max-invariant?"`
- own-file occurrences: 1 in `sessions/session-73b/session-73b-results-workingpaper.md`

### proven_167  (theorems)
- name: `Per-Bulletin-per-pole Level-1/2/3 ladder** declaration per W10-119 extension`
- key: `per-bulletin-per-pole level-1/2/3 ladder declaration per w10-119 extension`
- own-file occurrences: 1 in `sessions/session-88/s88-pending-edits-ledger.md`

### proven_416  (theorems)
- name: `What**: add a PROVENANCE row to `computations/canonical_constants.py` for `Gamma_effacement = 0.99970`. The MCP `get_con`
- key: `what: add a provenance row to computations/canonical_constants.py for gamma_effacement = 0.99970. the mcp get_con`
- own-file occurrences: 1 in `sessions/session-85/session-85-1a-cc-residue-phonon-first.md`

### proven_146  (theorems)
- name: `Source**: `s88-w22-w7a-74-rank-vs-magnitude.md` §IV.3, `s88-w18-w6a-51-geometric-resummation.md` §IV.1`
- key: `source: s88-w22-w7a-74-rank-vs-magnitude.md §iv.3, s88-w18-w6a-51-geometric-resummation.md §iv.1`
- own-file occurrences: 1 in `sessions/session-88/s88-pending-edits-ledger.md`

### proven_1151  (theorems)
- name: `Sakharov Induced Gravity from KK Spectrum`
- key: `sakharov induced gravity from kk spectrum`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_422  (theorems)
- name: `What**: Execute `S86-W?-3HE-B-INVERSION-CANONICAL-LANDING` (spec above). Compose the three subsection MDs (a, b, c) into`
- key: `what: execute s86-w?-3he-b-inversion-canonical-landing (spec above). compose the three subsection mds (a, b, c) into`
- own-file occurrences: 1 in `sessions/session-85/session-85-1b-3heb-inversion-landau.md`

### proven_1147  (theorems)
- name: `Trap 5: J-Reality PH Selection Rule`
- key: `trap 5: j-reality ph selection rule`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_876  (theorems)
- name: `Inputs**: `s83_w1_g4_epsilon_h_trajectory_fi.py`; S78 W-2D f_conv-anomaly table (same 3/2 structural ratio appears); f_2`
- key: `inputs: s83_w1_g4_epsilon_h_trajectory_fi.py; s78 w-2d f_conv-anomaly table (same 3/2 structural ratio appears); f_2`
- own-file occurrences: 1 in `sessions/session-83/session-83-gen-physicist-synthesis.md`

### proven_718  (theorems)
- name: `content_sha256** (full 64-char): `d252222f9580080bee4abf28c1d1c0a7ee095f6323df00f94da82aa705411bdd``
- key: `content_sha256 (full 64-char): d252222f9580080bee4abf28c1d1c0a7ee095f6323df00f94da82aa705411bdd`
- own-file occurrences: 1 in `sessions/session-90/session-90-w6-workingpaper.md`

### proven_778  (theorems)
- name: `What**: Promote K_HK = 9 FI partition cardinality result to permanent registry entry at algebra-axis Corner I per `perma`
- key: `what: promote k_hk = 9 fi partition cardinality result to permanent registry entry at algebra-axis corner i per perma`
- own-file occurrences: 1 in `sessions/session-91/session-91-w6-workingpaper.md`

### proven_346  (theorems)
- name: `L_max-invariance**: structural floor. Verified explicitly at L = 3, 5, 7 for representative observables (three-phonon ve`
- key: `l_max-invariance: structural floor. verified explicitly at l = 3, 5, 7 for representative observables (three-phonon ve`
- own-file occurrences: 1 in `sessions/session-74/session-74-results-workingpaper.md`

### proven_477  (theorems)
- name: `Registry patch (draft, assembled for future landing — see `s85_w3_consolidated_upgrade.json`)**: ready to append to `ses`
- key: `registry patch (draft, assembled for future landing — see s85_w3_consolidated_upgrade.json): ready to append to ses`
- own-file occurrences: 1 in `sessions/session-85/session-85-w3-workingpaper.md`

### proven_1244  (theorems)
- name: `BYPASSED at domain wall boundaries (W-32b: van Hove LDOS exceeds threshold)`
- key: `bypassed at domain wall boundaries (w-32b: van hove ldos exceeds threshold)`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_735  (theorems)
- name: `PASS-AND aggregation**: both reviewers must independently PASS each JOINT clause`
- key: `pass-and aggregation: both reviewers must independently pass each joint clause`
- own-file occurrences: 1 in `sessions/session-90/session-90-w6-workingpaper.md`

### proven_692  (theorems)
- name: `PRU compliance**: 14 machinery pins enumerated in plan §W6-2 §"Machinery pin (PRDR)" YAML block; all consumed in script `
- key: `pru compliance: 14 machinery pins enumerated in plan §w6-2 §"machinery pin (prdr)" yaml block; all consumed in script`
- own-file occurrences: 1 in `sessions/session-90/session-90-w6-workingpaper.md`

### proven_427  (theorems)
- name: `Gate**: `S86-W0-KR5-KCRIT-PROVENANCE`. PASS iff `mcp__knowledge__get_constant("K_R5")` returns the W8-7 + W8-2 provenanc`
- key: `gate: s86-w0-kr5-kcrit-provenance. pass iff mcp__knowledge__get_constant("k_r5") returns the w8-7 + w8-2 provenanc`
- own-file occurrences: 1 in `sessions/session-85/session-85-1b-3heb-inversion-landau.md`

### proven_507  (theorems)
- name: `Recomputed `sha256(s86_w3_pre_reg_inc_closure.py)` at synthesis time = `9252e6710fca3f7c0617536cdaffdd2ccc436bb12bf440f6`
- key: `recomputed sha256(s86_w3_pre_reg_inc_closure.py) at synthesis time = 9252e6710fca3f7c0617536cdaffdd2ccc436bb12bf440f6`
- own-file occurrences: 1 in `sessions/session-86/workshops/session-86-1b-s13-gen-physicist.md`

### proven_502  (theorems)
- name: `Inputs**: `computations/canonical_constants.py`; the original session producing M_KK = 7.428660e+16 GeV (likely S52-S58 `
- key: `inputs: computations/canonical_constants.py; the original session producing m_kk = 7.428660e+16 gev (likely s52-s58`
- own-file occurrences: 1 in `sessions/session-86/workshops/session-86-1a-s4-mack.md`

### proven_542  (theorems)
- name: `Class 8.3 publication-precision residual**: `4.297733078528765e-06``
- key: `class 8.3 publication-precision residual: 4.297733078528765e-06`
- own-file occurrences: 1 in `sessions/session-87/session-87-results-workingpaper.md`

### proven_1210  (theorems)
- name: `[T2] Breathing Mode Exclusion — delta g_ab^K = h(x)g_ab^K projects to 4D scalar, not tensor`
- key: `[t2] breathing mode exclusion — delta g_ab^k = h(x)g_ab^k projects to 4d scalar, not tensor`
- own-file occurrences: 1 in `sessions/framework/Atlas/atlas-07-permanent-results.md`

### proven_725  (theorems)
- name: `PRU compliance**: 19 machinery pins enumerated in plan §W6-5 §"Machinery pin (PRDR)" YAML; all consumed in script. No Cl`
- key: `pru compliance: 19 machinery pins enumerated in plan §w6-5 §"machinery pin (prdr)" yaml; all consumed in script. no cl`
- own-file occurrences: 1 in `sessions/session-90/session-90-w6-workingpaper.md`

### proven_476  (theorems)
- name: `Joint statement — "Landau structural block"**:`
- key: `joint statement — "landau structural block"`
- own-file occurrences: 1 in `sessions/session-85/session-85-w3-workingpaper.md`

### proven_246  (theorems)
- name: `Individual resonances overlap completely and cannot be resolved`
- key: `individual resonances overlap completely and cannot be resolved`
- own-file occurrences: 1 in `sessions/archive/session-42/session-42-results-workingpaper.md`

### proven_665  (theorems)
- name: `Session/Source: S89 / `S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2``
- key: `session/source: s89 / s89-higher-order-resolvent-expansion-o-tau2-kappa2`
- own-file occurrences: 1 in `sessions/session-90/session-90-w6-workingpaper.md`

### gate_T3-BATCH-S46-FWD-BWD-NS  (gates)
- name: `T3-BATCH-S46-FWD-BWD-NS`
- key: `t3-batch-s46-fwd-bwd-ns`
- own-file occurrences: 1 in `computations/session-81/s81_batch_gate_verdicts.txt`

### gate_T3-BATCH-S56-POST-TRANSIT-COH  (gates)
- name: `T3-BATCH-S56-POST-TRANSIT-COH`
- key: `t3-batch-s56-post-transit-coh`
- own-file occurrences: 1 in `computations/session-81/s81_batch_gate_verdicts.txt`

### gate_T3-BATCH-S46-BAYESIAN-GP  (gates)
- name: `T3-BATCH-S46-BAYESIAN-GP`
- key: `t3-batch-s46-bayesian-gp`
- own-file occurrences: 1 in `computations/session-81/s81_batch_gate_verdicts.txt`

### gate_T3-BATCH-S44-FOAM-CUTOFF  (gates)
- name: `T3-BATCH-S44-FOAM-CUTOFF`
- key: `t3-batch-s44-foam-cutoff`
- own-file occurrences: 1 in `computations/session-81/s81_batch_gate_verdicts.txt`

### gate_T3-BATCH-S52-JACOBSON-MULTI-T  (gates)
- name: `T3-BATCH-S52-JACOBSON-MULTI-T`
- key: `t3-batch-s52-jacobson-multi-t`
- own-file occurrences: 1 in `computations/session-81/s81_batch_gate_verdicts.txt`

### gate_T3-BATCH-S45-KRETSCHNER  (gates)
- name: `T3-BATCH-S45-KRETSCHNER`
- key: `t3-batch-s45-kretschner`
- own-file occurrences: 1 in `computations/session-81/s81_batch_gate_verdicts.txt`

### prov_96  (data_provenance)
- name: `connes_workshop_legacy`
- key: `connes_workshop_legacy`
- own-file occurrences: 0 in `computations/session-25/s25_connes_workshop_legacy.py`

### eq_18026  (equations)
- name: `diff = (W14-4_block before CF-27) XOR (W14-4_block after CF-27)`
- key: `diff = (w14-4_block before cf-27) xor (w14-4_block after cf-27)`
- own-file occurrences: 1 in `sessions/session-plan/archive/session-87-plan-w4.md`

### eq_16707  (equations)
- name: `beta_s = -0.1331 pin to 4.19e-5 = 42 ppm, 239x below the 1% PASS`
- key: `beta_s = -0.1331 pin to 4.19e-5 = 42 ppm, 239x below the 1% pass`
- own-file occurrences: 1 in `sessions/session-85/session-85-s3-alphas-registry-landau.md`

### eq_1843  (equations)
- name: `E_gs = 1.4025899717 (delta = -2.5872%)`
- key: `e_gs = 1.4025899717 (delta = -2.5872%)`
- own-file occurrences: 1 in `computations/session-52/s52_hfb_full_output.txt`

### eq_6978  (equations)
- name: `resolution_time = mid-session, AFTER plan-freeze — the`
- key: `resolution_time = mid-session, after plan-freeze — the`
- own-file occurrences: 1 in `sessions/session-85/workshops/s85-w3-methodology-debts.md`

### registry_Phononic-Crystal-Geometry  (registries)
- name: `Phononic Crystal Geometry of SU(3)`
- key: `phononic crystal geometry of su(3)`
- own-file occurrences: 1 in `sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md`

### registry__registry-template  (registries)
- name: `&lt;Registry Name&gt;`
- key: `&lt;registry name&gt`
- own-file occurrences: 1 in `sessions/framework/registry/_registry-template.md`

### registry_framework-bbn-hypothesis  (registries)
- name: `Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade`
- key: `framework bbn hypothesis: scale-dependent tau and the phonon cascade`
- own-file occurrences: 1 in `sessions/framework/ARCHIVE/framework-bbn-hypothesis.md`

### registry_lrd-observational-constraints  (registries)
- name: `LRD Observational Constraints Registry`
- key: `lrd observational constraints registry`
- own-file occurrences: 1 in `sessions/framework/registry/lrd-observational-constraints.md`

---

## PRESERVED entries — sample previews (top 10 per tier)

### Tier 1 (in VALID index)

#### open_588  (open_channels)
- name: `Step 2 (substitution)`
- key:  `step 2 (substitution)`
- found in **proven_102** (theorems):
    `...step 2 (substitution): at τ_fold = 0.190, 3/(3 + e^{12·0.190}...`
- found in **proven_105** (theorems):
    `...step 2 (substitution): for any same-regulator ratio m_i^r / m...`

#### open_509  (open_channels)
- name: `SM quantum numbers from Psi_+ = C^16`
- key:  `sm quantum numbers from psi_+ = c^16`
- found in **proven_1162** (theorems):
    `...sm quantum numbers from psi_+ = c^16 6 multiplets exact 7 branching_computat...`

#### open_593  (open_channels)
- name: `W7-BASELINE-HTILDE`
- key:  `w7-baseline-htilde`
- found in **gate_S85-W7-BASELINE-HTILDE-DERIVATION** (gates):
    `...s85-w7-baseline-htilde-derivation...`

#### proven_1253  (theorems)
- name: `Connes 8-cutoff positive sums`
- key:  `connes 8-cutoff positive sums`
- found in **closed_atlas02_eraI_10** (closed_mechanisms):
    `...connes 8-cutoff positive sums...`

#### prov_1217  (data_provenance)
- name: `desi_dr3_update`
- key:  `desi_dr3_update`
- found in **prov_1536** (data_provenance):
    `...desi_dr3_update...`

#### eq_5304  (equations)
- name: `Aitken Delta^2 (L=3,4,5, Gaussian):`
- key:  `aitken delta^2 (l=3,4,5, gaussian)`
- found in **eq_5305** (equations):
    `...======================================= aitken delta^2 (l=3,4,5, gaussian):...`

### Tier 2 (multi-occurrence in own file)

#### open_437  (open_channels)
- name: `Producing script`
- key:  `producing script`
- 25 occurrences in `sessions/session-87/session-87-results-workingpaper.md`

#### proven_730  (theorems)
- name: `Stage-2 dispatch ID**: `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY``
- key:  `stage-2 dispatch id: s91-or-later-four-corner-stage-2-cross-axis-verify`
- 2 occurrences in `sessions/session-90/session-90-w6-workingpaper.md`

#### proven_943  (theorems)
- name: `SU(3) -> U(1)_7`
- key:  `su(3) -> u(1)_7`
- 3 occurrences in `sessions/framework/Classification-of-phonon-exflation.md`

#### prov_372  (data_provenance)
- name: `first_sound_imprint`
- key:  `first_sound_imprint`
- 4 occurrences in `computations/session-44/s44_first_sound_imprint.py`

#### prov_1197  (data_provenance)
- name: `squeeze_reconciled`
- key:  `squeeze_reconciled`
- 2 occurrences in `computations/session-69/s69_squeeze_reconciled.py`

#### prov_263  (data_provenance)
- name: `collective_inertia`
- key:  `collective_inertia`
- 5 occurrences in `computations/session-40/s40_collective_inertia.py`

#### eq_17606  (equations)
- name: `convention=W13-2-forward-map+f_LISA-pivot+log-log-interp`
- key:  `convention=w13-2-forward-map+f_lisa-pivot+log-log-interp`
- 2 occurrences in `sessions/session-plan/archive/session-86-plan-w8.md`

#### eq_8784  (equations)
- name: `L_max=10 audit_sha256=<computed at runtime>`
- key:  `l_max=10 audit_sha256=<computed at runtime>`
- 2 occurrences in `sessions/session-89/workshops/s89-w2-r-canonical-observable-identity.md`

#### const_lambda_unit_canonical  (constants)
- name: `lambda_unit_canonical`
- key:  `lambda_unit_canonical`
- 2 occurrences in `computations/_shared/canonical_constants.py`

### Tier 3 (in another source file)

#### open_643  (open_channels)
- name: `Stage-2 cross-pillar bridge verify (§VII.W-3.LAB STAGE-1-CANDIDATE)**: per `joint-theorem-promotion.md` 4-stage pathway, Stage-2 two-agent parallel cross-axis i`
- key:  `stage-2 cross-pillar bridge verify (§vii.w-3.lab stage-1-candidate): per joint-theorem-promotion.md 4-stage pathway, stage-2 two-agent parallel cross-axis indep`
- found in `sessions/session-88/atlas-uplift-materials/atlas-08-open-questions-materials.md`

#### open_425  (open_channels)
- name: `A4 graded reality (KO-dim 6)`
- key:  `a4 graded reality (ko-dim 6)`
- found in `sessions/session-88/session-88-w11-workingpaper.md`

#### open_627  (open_channels)
- name: `Swampland c(tau)`
- key:  `swampland c(tau)`
- found in `computations/session-48/s48_volovik_string.py`
- found in `sessions/archive/session-47/session-47-wayforward.md`
- found in `sessions/session-72/session-72-audit-gen-physicist.md`

#### open_644  (open_channels)
- name: `§VII.AM Universal Lock Condition Stage-2 verify**: per `joint-theorem-promotion.md` 4-stage pathway, the 3-clause joint theorem (pixelation lock + effacement lo`
- key:  `§vii.am universal lock condition stage-2 verify: per joint-theorem-promotion.md 4-stage pathway, the 3-clause joint theorem (pixelation lock + effacement lock +`
- found in `sessions/session-88/atlas-uplift-materials/atlas-08-open-questions-materials.md`

#### open_516  (open_channels)
- name: `DNP instability for tau < 0.285`
- key:  `dnp instability for tau < 0.285`
- found in `sessions/archive/session-23/session-23b-synthesis.md`

#### open_426  (open_channels)
- name: `A5 Poincaré duality`
- key:  `a5 poincaré duality`
- found in `sessions/session-88/session-88-w5b-workingpaper.md`
- found in `sessions/session-88/session-88-w11-workingpaper.md`

#### open_553  (open_channels)
- name: `Multifield delta-N conversion`
- key:  `multifield delta-n conversion`
- found in `sessions/session-67/session-67-transit-phonon-first-workshop.md`
- found in `sessions/session-plan/archive/session-68-plan.md`
- found in `sessions/session-plan/archive/session-68-context.md`

#### proven_1880  (theorems)
- name: `Definitional-datum-vs-derived-theorem K-counter`
- key:  `definitional-datum-vs-derived-theorem k-counter`
- found in `sessions/framework/registry/permanence-map.md`
- found in `sessions/session-89/session-89-phonon-first-synthesis.md`
- found in `sessions/session-88/s88-pending-edits-ledger.md`

#### proven_45  (theorems)
- name: `§VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576): s=0 boundary corollary`
- key:  `§vii-b.zeta-not-physical-75 (registry line 4576): s=0 boundary corollary`
- found in `sessions/session-86/workshops/s86-sector-2-split-layer-taxonomy.md`

#### proven_1881  (theorems)
- name: `F(observable) vs F(trigger predicate) split`
- key:  `f(observable) vs f(trigger predicate) split`
- found in `sessions/session-plan/archive/session-89-context.md`
- found in `sessions/session-88/s88-pending-edits-ledger.md`
- found in `sessions/session-plan/session-90-plan-w1.md`

---

## TOO_SHORT / MISSING (no search performed)

- [TOO_SHORT_TO_SEARCH] closed_10 (closed_mechanisms): `[Berry]Q-2`
- [TOO_SHORT_TO_SEARCH] closed_46 (closed_mechanisms): `W10-5`
- [TOO_SHORT_TO_SEARCH] open_7 (open_channels): `Window-8`
- [TOO_SHORT_TO_SEARCH] open_720 (open_channels): `CUTOFF-SA-37`
- [TOO_SHORT_TO_SEARCH] open_467 (open_channels): `JSON detail`
- [TOO_SHORT_TO_SEARCH] open_119 (open_channels): `V_FR overlay`
- [TOO_SHORT_TO_SEARCH] open_77 (open_channels): `M_3(ℂ)`
- [TOO_SHORT_TO_SEARCH] open_795 (open_channels): `2040s`
- [TOO_SHORT_TO_SEARCH] open_456 (open_channels): `Verdict-line`
- [TOO_SHORT_TO_SEARCH] proven_1431 (theorems): `f_NL`
- [TOO_SHORT_TO_SEARCH] proven_1357 (theorems): `a_6 "theorem"`
- [TOO_SHORT_TO_SEARCH] proven_1103 (theorems): `Window-7`
- [TOO_SHORT_TO_SEARCH] proven_1472 (theorems): `§VII.U.7`
- [TOO_SHORT_TO_SEARCH] gate_ZFP (gates): `ZFP`
- [TOO_SHORT_TO_SEARCH] gate_QA-4 (gates): `QA-4`
- [TOO_SHORT_TO_SEARCH] gate_M3 (gates): `M3`
- [TOO_SHORT_TO_SEARCH] gate_E-4 (gates): `E-4`
- [TOO_SHORT_TO_SEARCH] gate_S85-W7-CC-6 (gates): `S85-W7-CC-6`
- [TOO_SHORT_TO_SEARCH] gate_GL-CUBIC (gates): `GL-CUBIC`
- [TOO_SHORT_TO_SEARCH] gate_fw_gates_22 (gates): `λ_fs (WDM)`
- [TOO_SHORT_TO_SEARCH] gate_L-1 (gates): `L-1`
- [TOO_SHORT_TO_SEARCH] prov_431 (data_provenance): `unexpanded_sa`
- [TOO_SHORT_TO_SEARCH] prov_264 (data_provenance): `gsl_transit`
- [TOO_SHORT_TO_SEARCH] prov_398 (data_provenance): `cc_gap_update`
- [TOO_SHORT_TO_SEARCH] prov_357 (data_provenance): `bayesian_f`
- [TOO_SHORT_TO_SEARCH] researcher_Lost-Treasures (researchers): `Lost-Treasures`
- [TOO_SHORT_TO_SEARCH] researcher_RF-Antimatter (researchers): `RF-Antimatter`
- [TOO_SHORT_TO_SEARCH] const_Vol_SU3_WRONG (constants): `Vol_SU3_WRONG`