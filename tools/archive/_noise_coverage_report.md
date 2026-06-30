# NOISE Coverage Check — loose search results

Sample: 123 spot-check entries
Min key length: 15 chars (normalized)
VALID index size: 8704 entries (cross-table)

## Aggregate
- **PRESERVED** (content found inside another VALID entry): **4** (3.3%)
- **ORPHANED** (content not found in any VALID entry): **91** (74.0%)
- TOO_SHORT_TO_SEARCH (key < min_key chars): 27
- MISSING_FROM_BATCHES (audit-internal anchor not in batch files): 1

## Per-table breakdown

| Table | Total | Preserved | Orphaned | Too short | Missing |
|:------|----:|----:|----:|----:|----:|
| ? | 1 | 0 | 0 | 0 | 1 |
| closed_mechanisms | 2 | 0 | 1 | 1 | 0 |
| constants | 2 | 0 | 1 | 1 | 0 |
| data_provenance | 10 | 0 | 6 | 4 | 0 |
| equations | 8 | 0 | 8 | 0 | 0 |
| gates | 15 | 0 | 9 | 6 | 0 |
| open_channels | 25 | 2 | 16 | 7 | 0 |
| registries | 4 | 0 | 4 | 0 | 0 |
| researchers | 2 | 0 | 0 | 2 | 0 |
| session_files | 4 | 0 | 4 | 0 | 0 |
| theorems | 50 | 2 | 42 | 6 | 0 |

**Reading**: high *Preserved* rates mean the NOISE filter is safe for that table (the content is already in the indexed VALID set via parent or sibling entries). High *Orphaned* rates mean dropping NOISE actually removes content not captured elsewhere — those entries warrant deeper review.

---

## ORPHANED entries (review priority — content not found elsewhere)

### closed_atlas02_eraXI_147  (closed_mechanisms)
- name: `§VII.K-PROP-W8.CELL-OCCUPANCY (cutoff_AL2010 / cutoff_sqrt L2 status update)`
- search key: `§vii.k-prop-w8.cell-occupancy (cutoff_al2010 / cutoff_sqrt l2 status update)`

### open_123  (open_channels)
- name: `M_GUT (10^16 GeV)`
- search key: `m_gut (10^16 gev)`

### open_368  (open_channels)
- name: `Concurrent agents`
- search key: `concurrent agents`

### open_339  (open_channels)
- name: `EMPIRICAL-τ_fold RETENTION`
- search key: `empirical-τ_fold retention`

### open_324  (open_channels)
- name: `F_amp(N3LO; N=3)`
- search key: `f_amp(n3lo; n=3)`

### open_682  (open_channels)
- name: `Threshold corrections for NCG-KK`
- search key: `threshold corrections for ncg-kk`

### open_208  (open_channels)
- name: `Route E (cumulative geometric corrections)`
- search key: `route e (cumulative geometric corrections)`

### open_803  (open_channels)
- name: `[-0.988, -0.942)`
- search key: `[-0.988, -0.942)`

### open_552  (open_channels)
- name: `Transit production`
- search key: `transit production`

### open_576  (open_channels)
- name: `A_s insensitive to E_C** (W2-G)`
- search key: `a_s insensitive to e_c (w2-g)`

### open_135  (open_channels)
- name: `[SP]S-5 Twistor correspondence`
- search key: `[sp]s-5 twistor correspondence`

### open_191  (open_channels)
- name: `Volume exchange`
- search key: `volume exchange`

### open_321  (open_channels)
- name: `R_req = F_amp_bare / F_amp_target`
- search key: `r_req = f_amp_bare / f_amp_target`

### open_511  (open_channels)
- name: `67/67 Baptista geometry checks`
- search key: `67/67 baptista geometry checks`

### open_124  (open_channels)
- name: `M_Planck (10^19 GeV)`
- search key: `m_planck (10^19 gev)`

### open_560  (open_channels)
- name: `N_eff = 3.044 post-thermalization`
- search key: `n_eff = 3.044 post-thermalization`

### open_660  (open_channels)
- name: `W11 Volovik CC Tracking promotion gap (§VII.AT slot allocation)**: W11 Volovik CC Tracking Wall (DILUTION-CC-66) is currently anchored at `framework-cc-oom.md` (Door 12 in atlas-05`
- search key: `w11 volovik cc tracking promotion gap (§vii.at slot allocation): w11 volovik cc tracking wall (dilution-cc-66) is currently anchored at framework-cc-oom.md (doo`

### proven_502  (theorems)
- name: `Inputs**: `computations/canonical_constants.py`; the original session producing M_KK = 7.428660e+16 GeV (likely S52-S58 `
- search key: `inputs: computations/canonical_constants.py; the original session producing m_kk = 7.428660e+16 gev (likely s52-s58`

### proven_57  (theorems)
- name: `Regulator-pin tag**: `a_2^{Mellin}` (per`
- search key: `regulator-pin tag: a_2^{mellin} (per`

### proven_375  (theorems)
- name: `Script: `computations/s82_w2_5_heat_kernel_mp.py``
- search key: `script: computations/s82_w2_5_heat_kernel_mp.py`

### proven_1925  (theorems)
- name: `STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (V supplies spectral-functional premise; C supplies SR-LO-dynamical theorem C`
- search key: `structure: source-double-cite-co-primary (v supplies spectral-functional premise; c supplies sr-lo-dynamical theorem c`

### proven_1615  (theorems)
- name: `Sessions S52–S60`
- search key: `sessions s52–s60`

### proven_218  (theorems)
- name: `Fermionic fiber: 16`
- search key: `fermionic fiber: 16`

### proven_434  (theorems)
- name: `W3-5 two-speed transfer identity c_S_canon = f_B** (PASS, machine precision): max|ratio−1| = 0.000e+00 across all 5 regu`
- search key: `w3-5 two-speed transfer identity c_s_canon = f_b (pass, machine precision): max ratio−1 = 0.000e+00 across all 5 regu`

### proven_688  (theorems)
- name: `Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY closure**: plan substitution-chain L^{-3} attribution drift surfaced via anal`
- search key: `class-(d) pin-derivative-vs-source-primary closure: plan substitution-chain l^{-3} attribution drift surfaced via anal`

### proven_748  (theorems)
- name: `Forward gate at S91+**: `S91-OR-LATER-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` Stage-2 dispatch (pre-registered at CF-48);`
- search key: `forward gate at s91+: s91-or-later-four-corner-stage-2-cross-axis-verify stage-2 dispatch (pre-registered at cf-48)`

### proven_634  (theorems)
- name: `content_sha256** (full 64-char): `e1d2cc0761a606a6d3787fcf5e9186b94496f60406b5e30dbd6e3cf75fe78f7c` = SHA-256`
- search key: `content_sha256 (full 64-char): e1d2cc0761a606a6d3787fcf5e9186b94496f60406b5e30dbd6e3cf75fe78f7c = sha-256`

### proven_685  (theorems)
- name: `content_sha256** (full 64-char): `f3d3386b169f624ff32a2a1cefb79c3568e15ec3128d07623453e9e483a098a4``
- search key: `content_sha256 (full 64-char): f3d3386b169f624ff32a2a1cefb79c3568e15ec3128d07623453e9e483a098a4`

### proven_138  (theorems)
- name: `Writer**: mack-cosmic-bridge`
- search key: `writer: mack-cosmic-bridge`

### proven_1928  (theorems)
- name: `Producing script: `computations/s86_w12_fisher_pdf_pin.py``
- search key: `producing script: computations/s86_w12_fisher_pdf_pin.py`

### proven_1359  (theorems)
- name: `phi_paasch status`
- search key: `phi_paasch status`

### proven_1590  (theorems)
- name: `Chirality antisymmetry: {γ_9, dD_K/dτ}=0. Chiral pairs ADD, not cancel`
- search key: `chirality antisymmetry: {γ_9, dd_k/dτ}=0. chiral pairs add, not cancel`

### proven_902  (theorems)
- name: `What**: Merge the W8-86 OZ derivation, W5-62 partition invariance, W10-123 axiomatic closure, and W6-52 CMB-S4 projectio`
- search key: `what: merge the w8-86 oz derivation, w5-62 partition invariance, w10-123 axiomatic closure, and w6-52 cmb-s4 projectio`

### proven_641  (theorems)
- name: `PRU compliance**: all machinery enumerated in plan §W2-2 §7 (registry slot allocation, writer assignment, co-signer chai`
- search key: `pru compliance: all machinery enumerated in plan §w2-2 §7 (registry slot allocation, writer assignment, co-signer chai`

### proven_1243  (theorems)
- name: `Extended from 1D Jensen to full 3D U(2)-invariant surface (V_spec/F_BCS ~ 8000)`
- search key: `extended from 1d jensen to full 3d u(2)-invariant surface (v_spec/f_bcs ~ 8000)`

### proven_1208  (theorems)
- name: `[NEW S62] Delta > 0.353 M_KK along softest Hessian direction`
- search key: `[new s62] delta > 0.353 m_kk along softest hessian direction`

### proven_1885  (theorems)
- name: `Cross-Reviewer Audit-Machinery Self-Citation`
- search key: `cross-reviewer audit-machinery self-citation`

### proven_1233  (theorems)
- name: `EIH Casimir Monotonicity: local a_0/a_2 increases with C_2(p,q)`
- search key: `eih casimir monotonicity: local a_0/a_2 increases with c_2(p,q)`

### proven_1863  (theorems)
- name: `Cross-pillar-bridge Pole-Scope (T1-20)`
- search key: `cross-pillar-bridge pole-scope (t1-20)`

### proven_727  (theorems)
- name: `lizzi-spectral-functional-theorist** is PRIMARY author of clauses (a) Cell-II identity (JOINT), (c) parse-tree decision `
- search key: `lizzi-spectral-functional-theorist is primary author of clauses (a) cell-ii identity (joint), (c) parse-tree decision`

### proven_458  (theorems)
- name: `Structural position**: AUDIT / registration gate; lands the ledger consequence of S84-W7-74's FAIL verdict. The PASS is `
- search key: `structural position: audit / registration gate; lands the ledger consequence of s84-w7-74's fail verdict. the pass is`

### proven_686  (theorems)
- name: `Structural position**: New canonical `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5π = 15.707963267948966` lands as the `
- search key: `structural position: new canonical tau_max_hk5_regime_fw_asymptotic_limit_fw = 5π = 15.707963267948966 lands as the`

### proven_1084  (theorems)
- name: `§VII.AF.1.STATE-PROJ companion slot`
- search key: `§vii.af.1.state-proj companion slot`

### proven_604  (theorems)
- name: `audit_sha256 (script || canonical || pinmap): `ae56c819b1cc3e038180728f4f7d0d05fd6ce92256dcc0d86a45741d61a37c47``
- search key: `audit_sha256 (script canonical pinmap): ae56c819b1cc3e038180728f4f7d0d05fd6ce92256dcc0d86a45741d61a37c47`

### proven_25  (theorems)
- name: `Canonical reference S66_RAW_RANGE = 381.0 in`
- search key: `canonical reference s66_raw_range = 381.0 in`

### proven_360  (theorems)
- name: `FUNCTIONAL-INDEPENDENT: eigenvalue ratios, moment ratios, ratio-of-ratios (1.7% L_max shift), tau-derivatives, block str`
- search key: `functional-independent: eigenvalue ratios, moment ratios, ratio-of-ratios (1.7% l_max shift), tau-derivatives, block str`

### proven_1276  (theorems)
- name: `[NEW S45] Bogoliubov/KZ n_s (all k-mappings)`
- search key: `[new s45] bogoliubov/kz n_s (all k-mappings)`

### proven_84  (theorems)
- name: `W4a-16 data: `computations/s88_w4a_a0_m2_backward_rescue_theorem.npz` + `.json``
- search key: `w4a-16 data: computations/s88_w4a_a0_m2_backward_rescue_theorem.npz + .json`

### proven_1883  (theorems)
- name: `Layer-2-A vs Layer-2-B coverage`
- search key: `layer-2-a vs layer-2-b coverage`

### proven_1177  (theorems)
- name: `TT stability: no tachyons`
- search key: `tt stability: no tachyons`

### proven_383  (theorems)
- name: `Hille-Phillips, *Functional Analysis and Semi-Groups* (1957): Bernstein functions have Levy-Khintchine representation bu`
- search key: `hille-phillips, functional analysis and semi-groups (1957): bernstein functions have levy-khintchine representation bu`

### proven_706  (theorems)
- name: `audit_sha256** (full 64-char): `2ba9d07429912025d7d9cac9d39ef4cfbdf794de5102f94e4406c1509d01dffe``
- search key: `audit_sha256 (full 64-char): 2ba9d07429912025d7d9cac9d39ef4cfbdf794de5102f94e4406c1509d01dffe`

### proven_481  (theorems)
- name: `CC-4** all L_max = 10:           **PASS`
- search key: `cc-4 all l_max = 10: pass`

### proven_471  (theorems)
- name: `PRU compliance**: 9/9 machinery-pin parameters pinned; 4 N/A for audit class, 5 substantive. No PRU Class-8 gap. No exec`
- search key: `pru compliance: 9/9 machinery-pin parameters pinned; 4 n/a for audit class, 5 substantive. no pru class-8 gap. no exec`

### proven_773  (theorems)
- name: `Depends on**: mack-cosmic-bridge sole-writer convention; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-`
- search key: `depends on: mack-cosmic-bridge sole-writer convention; cross-pillar-bridge-anatomy.md §"algebra-axis orthogonality k`

### proven_740  (theorems)
- name: `audit_sha256** (full 64-char): `8c89990382f16a9b1ffd9b506ee98bb8231fefed49d9b84da437aa564eae93d3``
- search key: `audit_sha256 (full 64-char): 8c89990382f16a9b1ffd9b506ee98bb8231fefed49d9b84da437aa564eae93d3`

### proven_1866  (theorems)
- name: `Joint-theorem 4-stage promotion pathway`
- search key: `joint-theorem 4-stage promotion pathway`

### proven_419  (theorems)
- name: `Registry citations (T-9, T-19, T-27, T-41, §VII.P, §XV-B, DILUTION-CC-66, framework-cc-oom CC Closures 5/6) traced via k`
- search key: `registry citations (t-9, t-19, t-27, t-41, §vii.p, §xv-b, dilution-cc-66, framework-cc-oom cc closures 5/6) traced via k`

### proven_1487  (theorems)
- name: `§VII.P → §VII.AF.2 v2`
- search key: `§vii.p → §vii.af.2 v2`

### gate_T3-BATCH-S21C-GB-DEBUG6  (gates)
- name: `T3-BATCH-S21C-GB-DEBUG6`
- search key: `t3-batch-s21c-gb-debug6`

### gate_T3-BATCH-S45-EULER-DEFICIT  (gates)
- name: `T3-BATCH-S45-EULER-DEFICIT`
- search key: `t3-batch-s45-euler-deficit`

### gate_T3-BATCH-S21C-NEUTRINO-FINE-GRID  (gates)
- name: `T3-BATCH-S21C-NEUTRINO-FINE-GRID`
- search key: `t3-batch-s21c-neutrino-fine-grid`

### gate_T3-BATCH-S52-RICCI-FLOW  (gates)
- name: `T3-BATCH-S52-RICCI-FLOW`
- search key: `t3-batch-s52-ricci-flow`

### gate_T3-BATCH-S45-COLLECTIVE-NS-RPA  (gates)
- name: `T3-BATCH-S45-COLLECTIVE-NS-RPA`
- search key: `t3-batch-s45-collective-ns-rpa`

### gate_T3-BATCH-S64-GSL-ENTROPY  (gates)
- name: `T3-BATCH-S64-GSL-ENTROPY`
- search key: `t3-batch-s64-gsl-entropy`

### gate_T3-BATCH-S52-HFB-FULL  (gates)
- name: `T3-BATCH-S52-HFB-FULL`
- search key: `t3-batch-s52-hfb-full`

### gate_T3-BATCH-S52-LIOUVILLIAN  (gates)
- name: `T3-BATCH-S52-LIOUVILLIAN`
- search key: `t3-batch-s52-liouvillian`

### gate_T3-BATCH-S52-ETA-B  (gates)
- name: `T3-BATCH-S52-ETA-B`
- search key: `t3-batch-s52-eta-b`

### prov_2076  (data_provenance)
- name: `w5_falsifier_inventory_consolidation_writer`
- search key: `w5_falsifier_inventory_consolidation_writer`

### prov_9  (data_provenance)
- name: `w1_deferred_pending_audit_test`
- search key: `w1_deferred_pending_audit_test`

### prov_7  (data_provenance)
- name: `w1_17_vii_ah_stage_2_orthogonality_k2_rule_update`
- search key: `w1_17_vii_ah_stage_2_orthogonality_k2_rule_update`

### prov_651  (data_provenance)
- name: `conformal_diagram`
- search key: `conformal_diagram`

### prov_658  (data_provenance)
- name: `euclid_continuum`
- search key: `euclid_continuum`

### prov_159  (data_provenance)
- name: `rge_running_legacy`
- search key: `rge_running_legacy`

### sf_63:session-63-W7-workingpaper.md  (session_files)
- name: `session-63-W7-workingpaper.md`
- search key: `session-63-w7-workingpaper.md`

### sf_66:session-66-wrapup.md  (session_files)
- name: `session-66-wrapup.md`
- search key: `session-66-wrapup.md`

### sf_sessions/framework/registry/_registry-template.md  (session_files)
- name: `_registry-template.md`
- search key: `_registry-template.md`

### sf_sessions/session-plan/archive/session-29Aa-prompt.md  (session_files)
- name: `session-29Aa-prompt.md`
- search key: `session-29aa-prompt.md`

### eq_19972  (equations)
- name: `scheme=stage-2-cross-axis-3-reviewer-axis-a-pillar-1-ncg-axiomatic \`
- search key: `scheme=stage-2-cross-axis-3-reviewer-axis-a-pillar-1-ncg-axiomatic \`

### eq_18596  (equations)
- name: `chi_A_volovik_2003             = 1.500000              [canonical_constants; 3He-A susceptibility]`
- search key: `chi_a_volovik_2003 = 1.500000 [canonical_constants; 3he-a susceptibility]`

### eq_7325  (equations)
- name: `N_C = 1/(1+N_B²) is NOT an emergent algebraic relation between two independent`
- search key: `n_c = 1/(1+n_b²) is not an emergent algebraic relation between two independent`

### eq_3790  (equations)
- name: `R(0)  = 4.0000000000`
- search key: `r(0) = 4.0000000000`

### eq_20639  (equations)
- name: `D_can slightly more repulsive (Delta_q = +0.075)`
- search key: `d_can slightly more repulsive (delta_q = +0.075)`

### eq_9821  (equations)
- name: `T^{(3)} = T^{(3)}_{[abc]}`
- search key: `t^{(3)} = t^{(3)}_{[abc]}`

### eq_19561  (equations)
- name: `pole s=4. Expected band: NO-ACTION or ADVISORY (SCHEMATIC and FULL-physical`
- search key: `pole s=4. expected band: no-action or advisory (schematic and full-physical`

### eq_22473  (equations)
- name: `s_cm2 = float(np.sum(c_arr * m_arr * m_arr))`
- search key: `s_cm2 = float(np.sum(c_arr m_arr m_arr))`

### const_lambda_unit_canonical  (constants)
- name: `lambda_unit_canonical`
- search key: `lambda_unit_canonical`

### registry_Phononic-Crystal-Geometry  (registries)
- name: `Phononic Crystal Geometry of SU(3)`
- search key: `phononic crystal geometry of su(3)`

### registry__registry-template  (registries)
- name: `&lt;Registry Name&gt;`
- search key: `&lt;registry name&gt`

### registry_framework-bbn-hypothesis  (registries)
- name: `Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade`
- search key: `framework bbn hypothesis: scale-dependent tau and the phonon cascade`

### registry_lrd-observational-constraints  (registries)
- name: `LRD Observational Constraints Registry`
- search key: `lrd observational constraints registry`

---

## PRESERVED entries (content found — sample previews)

### open_684  (open_channels)
- name: `Non-standard M_KK`
- search key: `non-standard m_kk`
- found in **proven_1677** (theorems):
    `...ation (pure kk), threshold corrections, non-standard m_kk....`

### open_590  (open_channels)
- name: `Step 4 (direction)`
- search key: `step 4 (direction)`
- found in **proven_103** (theorems):
    `...step 4 (direction): the mesh closes with m_h_framework = 9...`
- found in **proven_107** (theorems):
    `...step 4 (direction): same-regulator ratios are r-invariant....`

### proven_1687  (theorems)
- name: `Casimir scalar + vector`
- search key: `casimir scalar + vector`
- found in **closed_atlas02_eraI_3** (closed_mechanisms):
    `...casimir scalar + vector...`

### proven_938  (theorems)
- name: `Three algebraic traps`
- search key: `three algebraic traps`
- found in **proven_811** (theorems):
    `...all three algebraic traps share common root: tensor product struc...`
- found in **proven_1544** (theorems):
    `...three algebraic traps — f/b=4/11, b_1/b_2=4/9, e/(ac)=1/16. a...`

---

## TOO_SHORT / MISSING entries (no search performed)

- [TOO_SHORT_TO_SEARCH] closed_28 (closed_mechanisms): `CF-68`
- [TOO_SHORT_TO_SEARCH] open_245 (open_channels): `(b) RG`
- [TOO_SHORT_TO_SEARCH] open_63 (open_channels): `Plan SHA`
- [TOO_SHORT_TO_SEARCH] open_180 (open_channels): `EIGENVECTOR-48`
- [TOO_SHORT_TO_SEARCH] open_450 (open_channels): `Verdict file`
- [TOO_SHORT_TO_SEARCH] open_13 (open_channels): `Window-16`
- [TOO_SHORT_TO_SEARCH] open_329 (open_channels): ``scan_range``
- [TOO_SHORT_TO_SEARCH] open_298 (open_channels): `0.950`
- [MISSING_FROM_BATCHES] THEO-8835 (?): ``
- [TOO_SHORT_TO_SEARCH] proven_566 (theorems): `L_max: N/A`
- [TOO_SHORT_TO_SEARCH] proven_1819 (theorems): `52-60`
- [TOO_SHORT_TO_SEARCH] proven_1814 (theorems): `24b`
- [TOO_SHORT_TO_SEARCH] proven_1824 (theorems): `Fabric + n_s`
- [TOO_SHORT_TO_SEARCH] proven_1661 (theorems): `155,984`
- [TOO_SHORT_TO_SEARCH] proven_1716 (theorems): `30-55`
- [TOO_SHORT_TO_SEARCH] gate_G-29c (gates): `G-29c`
- [TOO_SHORT_TO_SEARCH] gate_E-2 (gates): `E-2`
- [TOO_SHORT_TO_SEARCH] gate_Higgs-sigma (gates): `Higgs-sigma`
- [TOO_SHORT_TO_SEARCH] gate_KC-1 (gates): `7-10%`
- [TOO_SHORT_TO_SEARCH] gate_QA-1 (gates): `QA-1`
- [TOO_SHORT_TO_SEARCH] gate_SP-3 (gates): `SP-3`
- [TOO_SHORT_TO_SEARCH] prov_775 (data_provenance): `neff_read`
- [TOO_SHORT_TO_SEARCH] prov_779 (data_provenance): `npz_probe`
- [TOO_SHORT_TO_SEARCH] prov_1214 (data_provenance): `chirp_penumbra`
- [TOO_SHORT_TO_SEARCH] prov_440 (data_provenance): `fwd_bwd_ns`
- [TOO_SHORT_TO_SEARCH] researcher_Lost-Treasures (researchers): `Lost-Treasures`
- [TOO_SHORT_TO_SEARCH] researcher_RF-Antimatter (researchers): `RF-Antimatter`
- [TOO_SHORT_TO_SEARCH] const_Vol_SU3_WRONG (constants): `Vol_SU3_WRONG`