# Session 93 Wave 5 — §VII.AY R_machine + §VII.AR FULL-tier + §VII.AW STAGE-3/rename (Results Working Paper)

**Session**: 93 | **Wave**: W5 | **Plan**: session-93-plan-w5.md | **Theme**: Close the §VII.AY substrate-cocycle-ratio arbitration (R_machine recompute + Element-5 tolerance/Stage-2/Stage-3), the §VII.AR FULL-tier N=4 conviction-or-acquittal test + filter-geometry audit, and two §VII.AW registry-write moves (THIRD STAGE-3-PERMANENT promotion + label-collision slot-rename).

## Gate Sections

### §W5-1. S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (substrate-IS M_3(ℂ)-block cocycle-ratio full-float64 re-pin + historiographic branch classifier)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The substrate-IS cocycle ratio R_machine = (δE_6·δE_7)/(δE_8)² from the M_3(ℂ) Gell-Mann colour-block of D_K(τ_fold=0.19) is the unique substrate-first canonical for `substrate_cocycle_ratio_67_88`; its 6-sig-fig rounding self-documents which prior F-image (F1=7.324974 vs F2=7.324992) was faithful.
**Plan reference**: `sessions/session-plan/session-93-plan-w5.md` §W5-1 (machinery pin, thresholds, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script** `computations/session-93/s93_w5_1_substrate_cocycle_ratio_67_88_r_machine_recompute.py` — present (32862 bytes). `grep` confirms both `must_contain`:
  - `from canonical_constants import (` ✓ (imports `Delta_0_OES, Delta_0_GL, cocycle_norm_phi67, cocycle_norm_phi88, substrate_cocycle_ratio_67_88`)
  - `def append_verdict(` ✓ (single-shot AFTER-pattern emission)
- **Data** `…_recompute.npz` — present (11982 bytes). All pre-registered keys verified on disk: `R_machine_float64=7.3249917525961665`, `R_machine_sage_qq_str=8814961/1203409`, `round_to_6sf_R_machine=7.32499`, `dist_to_F1=1.737e-05`, `dist_to_F2=2.474e-07`, `branch_label=F2-faithful`, `delta_E_6/7/8 = 0.8907/0.8907/0.3291`, `consumers_revalidated` (7-element array), plus DIAGNOSTIC `R_machine_live_diagnostic=7.325113`.
- **Plot** `…_recompute.png` — present (69164 bytes). Number line: F1 (7.324974), F2 (7.324992), R_machine (7.324992, F2-faithful), 7.3250 4-sf band-center with ±0.1% falsifier band shaded; 6-sf zoom window [7.32485, 7.32515].
- **Verdict line** in `computations/session-93/s93_gate_verdicts.txt` — present, matches `^S93-W5-1-…:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row present.
- **Canonical re-pin** — `canonical_constants.py:277` `substrate_cocycle_ratio_67_88 = 7.3249917525961665` (re-pinned in place; `update_constant` MCP refused overwrite of existing constant per safety guard → manual Edit, the prescribed path) + new alias `R_machine_substrate_67_88 = 7.3249917525961665` (line 278, W5-2 consumption target) + lines 275/276 norm-comment provenance correction. Import verified clean.
- **Inventory consumer re-validation** — `falsifier-master-inventory.md` §"S93 W5-1 substrate-arbitration audit-pin" (mack sole-writer, canonical-write-order Step 3) appended after the cross-row dependency-map substitution chain.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):
- `get_constant("substrate_cocycle_ratio_67_88")` → 7.324992 (S86, gate S86-W5-CANON-EXTRACT, Superseded: False) — the F2 value, re-pin target.
- `get_constant("cocycle_norm_phi67")` → 0.793346 (S86 W-5 C2, Superseded: False).
- `get_constant("cocycle_norm_phi88")` → 0.108307 (S86 W-5 C2, Superseded: False).
- `search_knowledge("cocycle ratio 67 88 R_machine M_3(C) block gaps falsifier")` → S92 workshop `s92-vii-ay-cocycle-ratio-f1-vs-f2.md` defines the gate; theorem `proven_539` CC2 records float64 quotient 7.324974378; 7 downstream consumers (archive scripts, equations eq_6434/6437/…, theorems, gates CF-2/CF-3).
- `trace_entity("substrate_cocycle_ratio_67_88")` → derived_from S86 (F2 = Fraction(114453,15625) Sage-QQ) AND S92 (STRUCTURALLY DISTINCT from F1 = phi_67/phi_88 direct ratio); S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN PASS (`ratio=7.324974` across 4 regulators); S92-W7-CF-W9-10-C inheritance audit FAIL (`diff_s4_canonical=1.762e-05`).
- `search_knowledge("F1 F2 historiography 7.324974 7.324992 arbitration")` → corpus §21.1 K=1 instance documents F1/F2; round_to_6sf(F1)=7.32497 ≠ 7.32499=round_to_6sf(F2); round_to_5sf agree at 7.3250.
- `search_knowledge("W8-4 SU3 OP directions delta_E_a commutator Frobenius lambda_6 lambda_7 lambda_8")` → source script `s85_w8_su3_op_lab_predictions.py` (gate S85-W8-4-SU3-OP-LAB-PREDICTIONS PASS, L_max=8); δE_a = ‖[D_K_toy, λ_a]‖_F/‖λ_a‖_F (eq.8) is the AUTHORITATIVE substrate-first provenance — NOT a Peter-Weyl bottom-K cache gap.
- `update_constant("substrate_cocycle_ratio_67_88", 7.3249917525961665, …)` → REFUSED (existing-constant overwrite safety guard); routed to manual `canonical_constants.py` Edit (the MCP-prescribed path).
- **NOT PRE-CLOSED**: no prior gate extracted R_machine bit-precision from the substrate construction. S89/S90 prior art computed `Fraction(793346,108307)` = F1 from the *published 6-sf norms*, never from the δE frame norms — this gate is the first genuine substrate extraction.

**Verdict**: **PASS** — value=`R_machine=7.3249917525961665;R_machine_QQ=8814961/1203409;round6sf=7.32499;branch=F2-faithful;dist_F1=1.7374e-05;dist_F2=2.4740e-07;dE6=0.8907;dE7=0.8907;dE8=0.3291;norms_reproduced=True;agreement_floor=5sf;consumers_revalidated=7;formal_consistent=True;prior_pin=7.324992;re_pin_target=7.3249917525961665` scheme=FW convention=substrate-first-M_3(C)-block-gap-ratio-full-float64-R_machine L_max=10 audit_sha256=`491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617` content_sha256=`3270e3a4dcf70f520eb15f55c3c4fbaa6d62f1a632ee1e1364cbc0731256723c`.

**Results**:

*Recomputed R_machine (the substrate pin W5-2 consumes).* Sage-QQ exact + full float64:
```
R_machine = (δE_6·δE_7)/(δE_8)² = Fraction(8814961, 1203409) = 7.3249917525961665
round_to_6sf(R_machine) = 7.32499
```

*Three extracted M_3(ℂ)-block gaps (W8-4 frame norms; the substrate-first source).* The published cocycle norms derive from the S85 W8-4 commutator-Frobenius construction `δE_a = ‖[D_K_toy, λ_a]‖_F/‖λ_a‖_F` (eq.8; `session-85-1b-3heb-inversion-connes.md:132-138`), on the M_3(ℂ) Gell-Mann colour-block (`λ_6, λ_7` chiral pair; `λ_8` Cartan):
```
δE_6 = δE_7 = 0.8907 M_KK   (chiral pair)
δE_8       = 0.3291 M_KK   (Cartan, Jensen-rate-limited at τ_fold>0)
```
These reproduce the published 6-sf norms by the recorded `round_to_6sf` operation: `round_to_6sf(0.8907²) = round_to_6sf(0.79334649) = 0.793346 = cocycle_norm_phi67` ✓; `round_to_6sf(0.3291²) = round_to_6sf(0.10830681) = 0.108307 = cocycle_norm_phi88` ✓ (`norms_reproduced = True`).

*F1-vs-F2 historiography ARBITRATION (the central deliverable).* The two prior methodology-floor images and their Sage-QQ-exact distances to the substrate value:
| Image | Value | round_to_6sf | dist to R_machine | Provenance |
|:------|:------|:-------------|:------------------|:-----------|
| F1 | `Fraction(793346,108307)` = 7.3249743784 | 7.32497 | **1.737e-05** | direct ratio of the published 6-sf norm *products* (double-rounded) |
| F2 | `Fraction(114453,15625)` = 7.324992 | 7.32499 | **2.474e-07** | S86 W-5 R2-B Sage-QQ reconstruction; 15625 = 5⁶ |
| R_machine | `Fraction(8814961,1203409)` = 7.3249917526 | 7.32499 | — | substrate-first (this gate) |

**BRANCH = F2-faithful.** `round_to_6sf(R_machine) = 7.32499 = round_to_6sf(F2) ≠ round_to_6sf(F1)`. The S86 W-5 R2-B Sage-QQ reconstruction (F2) carried R's true 6th significant figure; F1 lost it via **double-rounding** (taking the ratio of values that were each already rounded to 6 sf). F1 is a methodology-floor F-image, not the substrate value. This **inverts** the prior CF-S93-W7-1 expectation of a "F2→F1 VALUE re-pin": the substrate vindicates F2's value, and the re-pin is a F2→full-float64 *sharpening* (7th-digit refinement of an already-correct 6-sf value), not a cross-image swap.

*Substitution chain (Steps 1–7; substituted numbers).*
- Step 1–2: `cocycle_norm_phi67 ≡ δE_6·δE_7`; `cocycle_norm_phi88 ≡ (δE_8)²`.
- Step 3: `R ≡ ‖[φ_67]‖/‖[φ_88]‖ = (δE_6·δE_7)/(δE_8)²` (Morita-invariant cohomology-class pairing on the M_3(ℂ) summand).
- Step 4: substitute the W8-4 frame norms (full precision, NOT the published 6-sf norm products): `R_machine = (0.8907·0.8907)/(0.3291²) = 0.79334649/0.10830681 = 8814961/1203409`.
- Step 5: F1 ≠ F2 in ℚ — cross-mult residual `793346·15625 − 108307·114453 = −29821 ≠ 0`; `|F1−F2| = 1.762e-5`, `Δ_rel = 2.406e-6`.
- Step 6: `round_to_6sf(F1)=7.32497 ≠ 7.32499=round_to_6sf(F2)`; both → 7.3250 at 5 sf ⇒ **genuine agreement floor = 5 sig figs** (the §W7-1 "6-sf agreement" was a rounding slip; corrected in the pin comment).
- Step 7: branch read off `round_to_6sf(R_machine) = 7.32499` ⇒ F2-faithful.
- Conclusion: re-pin target = substrate-first R_machine (full float64) in all three branches; F1-vs-F2 is a historiographic question R_machine ARBITRATES but does not change the pin target. Direction substrate → emergent throughout.

*DIAGNOSTIC cross-check (live 3×3 Gell-Mann commutator; NOT the pin).* Re-running eq.8 with the *current* canonical `Delta_0_OES = 0.4642547`, `Delta_0_GL = 0.7704351` gives `δE_6_live = 0.8906794` (drift 2.06e-5 from the W8-4 frame norm 0.8907), `δE_8_live = 0.3290897` (drift 1.03e-5), and `R_live = 7.325113` (round_to_6sf = 7.32511). The current Δ values have drifted slightly from the W8-4 4-sf frame norms; the substrate-first canonical for THIS observable is the W8-4 frame-norm construction at the recorded δE (the values that DEFINED the published cocycle norms), not the live recompute. CC0 (`‖λ_a‖_F = √2`, `Tr(λ²)=2`) and Hermiticity of `D_K_toy` both verified.

*7-consumer re-validation (orphan-literal scan at FORMAL loci).* Per plan, Rows #51/#54b/#58–#62 PASS-criteria, the line-~1056 transcription, and the corpus §21 K=1 instance are IN SCOPE for re-validation (NOT editing):
| Locus | Pattern | Hits | Status |
|:------|:--------|:-----|:-------|
| §VII.AY Level-3 anchor (registry) | `7.32497438` | 0 | (anchor cited in inventory, not registry body) |
| inventory Level-3 anchor (L~911) | `7.32497438` | 2 | F1 image; valid as DOCUMENTED methodology-floor anchor |
| inventory Rows #51/#54b band | `7.3250` | 25 | 4-sf band-center; both F1 & F2 satisfy; unchanged |
| inventory line-~1056 transcription | `7.324974\|7.324992` | 35 | documented F1/F2 ledger; consistent |
| inventory Rows #58–#62 PASS-criteria | `7.3250\|substrate_cocycle_ratio_67_88` | 35 | band-center + pin-name refs; unchanged |
| corpus §21.1 K=1 instance | `7.324974\|7.324992` | 32 | documents F1 vs F2 by design; consistent |
| canonical_constants pin | `substrate_cocycle_ratio_67_88` | 2 | re-pinned + alias |

FORMAL-locus consistency post-re-pin = **True**: F2-faithful ⇒ all existing 7.324992 / 7.32499 citations remain correct at their published precision; the 7.3250 4-sf band-center (the actual FORMAL PASS-criterion) is satisfied by both F1 and F2, so the substrate re-pin moves no PASS-band. The F1 image (7.32497438) cited as the cross-pillar-bridge Level-3 anchor stays valid as a documented methodology-floor image. **Zero orphaned literals require editing** (the F1/F2 6-sf decimals across registry/inventory/corpus are documented ledger/anchor entries, not orphaned pins).

*Cross-checks.* CC0 Gell-Mann normalization (‖λ_a‖_F=√2, Tr(λ²)=2) PASS; CC1 D_K_toy Hermitian PASS; Class-8.3 round-trip (npz full-float64 == in-memory) PASS.

*4-tuple.* `(value=R_machine=7.3249917525961665 [+ branch/consumer summary], scheme=FW, convention=substrate-first-M_3(C)-block-gap-ratio-full-float64-R_machine, L_max=10)`.

*Dual-SHA.* `audit_sha256=491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617`; `content_sha256=3270e3a4dcf70f520eb15f55c3c4fbaa6d62f1a632ee1e1364cbc0731256723c`.

*Substrate framing.* GEOMETRIC. The substrate IS the finite spectral triple (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_K, D_K(τ_fold=0.19)); R is one Morita-invariant eigenvalue-gap quantity on the M_3(ℂ) colour summand (φ_67 chiral-pair + φ_88 Cartan Hochschild-cocycle norms). Direction substrate → emergent: D_K commutator structure on the M_3(ℂ) Gell-Mann block → δE_a frame norms → cohomology-class ratio R_machine → canonical pin → laboratory-IN 3He-B/3He-A cocycle-asymmetry falsifier ratio. The substrate was never in dispute (S92 §W7-2 Axis-A + Axis-B PASS at the structural ceiling); the only open question — which methodology-floor decimal image carried R's true 6th sig fig — is ARBITRATED here (F2), read off the data file, not re-narrativized at synthesis. No methodology-floor image of R may be read or written as carrying more substrate fidelity than its precision floor supports (cross-pillar-bridge-corpus §21, SUGGESTION at K=1).

**UNBLOCKS** the §VII.AY STAGE-3-PERMANENT promotion (W5-2 substrate-pin-layer): the substrate-sourced R_machine pin = 7.3249917525961665 is now in `canonical_constants.py` (`substrate_cocycle_ratio_67_88` + alias `R_machine_substrate_67_88`); the W5-1 branch label `F2-faithful` is the corpus §21.0 R2 `canonical-value-question-DEFERRED-to-R_machine-recompute` → resolved tag W5-2 consumes.

---

### §W5-2. S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3 (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Element-5 Stage-2 re-tolerance + 3-axis PASS-AND + STAGE-1→STAGE-3-PERMANENT registry tag-flip)
**Agent**: `mack-cosmic-bridge` (Axis-B-primary re-test + STAGE-3 tag-flip; Axis-A vdd + Axis-B-cross-pillar spectral-geometer inherited PASS from S91 §W8-7)
**Hypothesis**: Under the principled Element-5 Stage-2 tolerance rel_tol ≥ 1e-5 RELATIVE (matching the 5-sf agreement floor, replacing the Class-8.3-defective <1e-6 ABSOLUTE pin), the §VII.AY.OP-PROJ 3-axis Stage-2 PASS-ANDs against the W5-1 substrate-sourced R_machine pin, unblocking STAGE-1-CANDIDATE → STAGE-3-PERMANENT and advancing Element-3 (iii) K=1 → K=2.
**Plan reference**: `sessions/session-plan/session-93-plan-w5.md` §W5-2 (CHAINED on W5-1 MANDATORY in-session upstream).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | `must_contain` grep evidence |
|:---------|:-----|:-----------------------------|
| script | `computations/session-93/s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.py` (53,543 B) | `from canonical_constants import` ✓ ; `append_verdict` ✓ (def + call) |
| data | `computations/session-93/s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.npz` (15,864 B) | all 9 plan-required keys present: `rel_tol_used=1e-05`, `delta_rel_axis_A=2.371908e-06`, `delta_rel_axis_B_primary=2.371908e-06`, `delta_rel_axis_B_cross_pillar=3.377531e-08`, `composite_pass_and=True`, `stage3_eligibility=True`, `deferred_resolved_tag=F2-faithful`, `stage3_permanent_flipped=True`, `element3_iii_k_counter=2` |
| plot | `computations/session-93/s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.png` (69,406 B) | 3-axis Δ_rel log-bar chart vs the 1e-5 rel_tol line + the prior `<1e-6` ABS-as-REL PIN-TIGHT line |
| JSON sidecar | `computations/session-93/s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.json` | full two-layer record + Stage-2 chain SHAs + stage_3_set_joined |
| verdict | `computations/session-93/s93_gate_verdicts.txt:99` | `^S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3:.* audit_sha256=[a-f0-9]{64}` ✓ (PASS, line 99); dual-SHA companion (line 100); Option-A `supersedes=add626285831c130…` over the line-97 FAIL |
| registry flip | `sessions/permanent-results-registry.md` (3 sites) | index row (line 150), section header (line 19853), Status line (line 19859) ALL read `STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage … STAGE-3 promotion S93 W5-2` ✓ |

`audit_sha256=d40041c309e9e04f0a6794a28ca9c742b12b0bf0657261b9ca6e3da3dfa37d7c` (LATEST NON-SUPERSEDED canonical, line 99; unique across the verdict file — sig_5 PASS); `content_sha256=3d95f01e199b7363ea732691c86715bf04dd24af7158adf2427f4658ee36b62b`. **Slot-allocation audit** `_vii_slot_allocation_audit.py` → **VERDICT: PASS** (118 entries; taxonomy B/C/D/E/F all = 0; §VII.AY.OP-PROJ registry-consistent post-flip). **M4 allowlist append is ORCHESTRATOR-ONLY** — gate-ID `S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3` must be appended to `sessions/framework/registry/methodology-wave-allowlist-ledger.md` by the orchestrator at plan-freeze (subagents edit-denied per recursion-attack closure); FLAGGED here, NOT edited by this gate.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries run BEFORE writing the script):

| Query | Tool | Salient return |
|:------|:-----|:---------------|
| `VII.AY OP-PROJ Element-5 tolerance Stage-2 cocycle ratio 67 88` | `search_knowledge` | NOT pre-closed: the prior §VII.AY Element-5 corrigendum is the S92 `S92-W7-CF-W8-CONSOLIDATED-1-VII-AY-OP-PROJ-ELEMENT-5-CORRIGENDUM` (registry-text arithmetic-gloss fix, NOT the Stage-2 re-tolerance). The re-toleranced 3-axis Stage-2 + STAGE-3-flip is THIS gate. Confirms `gates:Carry-forward --reproduces--> substrate_cocycle_ratio_67_88`. |
| `S91 W8-7 three-axis Stage-2 VII.AY Hochschild Kunneth Morita invariance` | `search_knowledge` | §VII.AY.OP-PROJ is the S91 W8-6 STAGE-1-CANDIDATE landing (`S91-HOCHSCHILD-KUNNETH-MORITA-INVARIANCE-STAGE-1-CANDIDATE-REGISTRY-LANDING` PASS); the §W8-7 Stage-2 is `S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-…` (the dispatch-successor). Confirms the 3-reviewer topology + the composite FAIL on the over-tight Axis-B-primary pin. |
| `get_constant("R_machine_substrate_67_88")` | `get_constant` | value `7.3249917525961665` (no PDG/CODATA PROVENANCE entry — it is the W5-1 substrate-first re-pin; provenance lives in `canonical_constants.py:278` + the W5-1 verdict `491ac49c…`). Imported (not hardcoded). |

The substrate pin, the §W8-7 3-axis structure, and the corpus §21.0 directive were all confirmed live before any compute. Knowledge-base wins on conflict: the get_constant return matches the canonical_constants.py:277-278 re-pin (no divergence).

**Verdict**: **PASS** (composite). The 3-axis Stage-2 PASS-ANDs at rel_tol=1e-5 RELATIVE against the W5-1 substrate-sourced R_machine pin; both two-layer obstructions cleared ⇒ §VII.AY.OP-PROJ flipped STAGE-1-CANDIDATE → STAGE-3-PERMANENT; Element-3 (iii) K=1 → K=2. `[VERIFY-THEOREM]` — no `[SIGN]` 3-tuple (`schema_v2_3tuple_required: false`; this is a relative-tolerance value-comparison + registry tag-flip, no directional prediction). The line-97 FAIL was a script-only substantive-content-guard bug (`status_block_lines` counted newlines on a single-paragraph Status → 1 < 15); fixed IN-SESSION to a word-count guard (`status_word_count=453 ≥ 15`); the corrective PASS line (99) carries the Option-A `supersedes` tag over the FAIL — no convention-shop, no threshold-loosen (the rel_tol=1e-5 was pre-registered in the plan + corpus §21.0 R1; only the script's internal substantive measure was corrected).

**Results**:

*Two-layer separation (corpus §21.0 R3 / E1):*
- **Layer 1 — Stage-3 ELIGIBILITY (TOLERANCE-layer; cleared at THIS gate):** the prior §W7-2 / §W8-7 Axis-B-primary FAIL tested the rank-2 anchor against an over-tight `<1e-6 ABSOLUTE` pin ≈ `1.366e-7 RELATIVE` at magnitude ~7.325 (`prior_abs_as_rel=1.365189e-07`) — ~7.3× tighter than the 6-sf publication floor `1e-6` (PIN-TIGHT-SOURCE-LOOSE Class-8.3, count (i): ABSOLUTE-where-RELATIVE). Re-pre-registered at the PRINCIPLED `rel_tol = 10^(−sig_figs_of_agreement) = 10^(−5) = 1e-5 RELATIVE` (the F1/F2 mutual agreement floor is **5** sig figs, not 6: `round_to_6sf(F1)=7.32497 ≠ 7.32499=round_to_6sf(F2)`, both → `7.3250` at 5 sf; count (ii) sharpening). The ABSOLUTE `<1e-6` form is FORBIDDEN per Class-8.3 item 7.
- **Layer 2 — STAGE-3-PERMANENT (SUBSTRATE-PIN-layer; cleared by W5-1):** the W5-1 gate (`S93-W5-1-…`, PASS, audit_sha256=`491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617`) RE-PINNED `substrate_cocycle_ratio_67_88 := R_machine = 7.3249917525961665` (Sage-QQ `8814961/1203409`, full float64) from the substrate-first M_3(ℂ)-block frame norms; branch **F2-faithful** (`canonical_pin_matches=True`; the W5-1 npz `R_machine_float64=7.3249917525961665`). This is the substrate-first source that clears Obstruction 2 (canonical-pin layer).

*The 3-axis re-tolerance vs the substrate-sourced R_machine pin (substitution-chain Step 5; each Δ_rel = |image − R_machine| / |R_machine|):*

| Axis | Reviewer | Image | Δ_rel vs R_machine | ≤ 1e-5 ? |
|:-----|:---------|:------|:-------------------|:---------|
| Axis-A | `van-den-dungen-bridge-theorist` (inherited PASS, S91 §W8-7 audit_sha256=`111b164dfb005b22…`) | F1 = 7.3249743784 | **2.371908e-06** | PASS |
| Axis-B-cross-pillar | `spectral-geometer` (inherited PASS, audit_sha256=`a3a8c877f86aca68…`) | F2/Sage-QQ = 7.324992 | **3.377531e-08** | PASS |
| Axis-B-primary | `mack-cosmic-bridge` (RE-TESTED here; prior FAIL audit_sha256=`cb680378862f0010…` on `<1e-6` ABS) | F1 = 7.3249743784 | **2.371908e-06** | **PASS** |

**Composite 3-axis PASS-AND = True.** The Axis-B-primary mack FAIL→PASS flip is the lever: the same F1 image that FAILed the `<1e-6` ABS pin (`|F1−pin|=1.762e-5`) PASSes the principled `rel_tol=1e-5` (`Δ_rel=2.37e-6`). `Δ_rel(F1,F2) = 2.405684e-06 < 1e-5` ⇒ the re-toleranced PASS is near-tautological at the 5-sf agreement floor — agnostic to F1-vs-F2 (which is WHY the R2 DEFERRED tag is mandatory and the substrate-pin layer, not the tolerance layer, is what arbitrates the historiography).

*The corpus §21.0 R2 DEFERRED→resolved tag:* the §VII.AY F1-vs-F2 floor-level PASS was tagged `canonical-value-question-DEFERRED-to-R_machine-recompute (CF-S93-W7-1)` at S92 (the anti-laundering safeguard). W5-1 RESOLVES it: the DEFERRED tag now reads **resolved to the W5-1 branch label `F2-faithful`** — F2 (Sage-QQ reconstruction) carried R's true 6th sig fig; F1 (direct ratio of the already-6-sf-rounded published norms) lost it via double-rounding. Both the verdict-line `value=` (`deferred_resolved_tag=F2-faithful`) and the registry §VII.AY Status block carry the resolved tag.

*The STAGE-3-PERMANENT flip (single-shot AFTER-pattern, 3 exact-match sites; slot RESERVED at the W0-1 lockfile):* §VII.AY.OP-PROJ flipped STAGE-1-CANDIDATE → STAGE-3-PERMANENT at the index-table row (line 150), the section header (line 19853), and the in-entry Status line (line 19859); the prior STAGE-1-CANDIDATE / CONDITIONAL-on-§W8-7 history is preserved as provenance. The slot is RESERVED at `sessions/framework/s93-slot-pre-allocation-lockfile.md §"RESERVED-FOR-S93-W5-2-…"` (W0-1, LIVE, status RESERVED) — protecting the slot identity against the 6-7 colliding STAGE-3 registry-writes this session.

*Element-3 (iii) Hybrid-Independence-Test K-counter:* the §W8-7 composite-FAIL BLOCK on the K-counter (`element_3_joint_hypersurface_iii_k_counter_advance=K_1_to_K_2_BLOCKED_due_to_axis_FAIL`) is LIFTED by the re-toleranced 3-axis PASS-AND ⇒ **K=1 → K=2**.

*ORDINAL DISCIPLINE (no contested integer asserted):* §VII.AY.OP-PROJ's MEMBERSHIP in the STAGE-3-PERMANENT cross-axis joint-theorem set `{§VII.AH (FIRST), §VII.U.2 Corner-II Var_a (SECOND), §VII.AU.OP-PROJ, §VII.AW.OP-PROJ, §VII.AV.STATE-PROJ, §VII.AX.OP-PROJ}` is recorded WITHOUT a specific integer — the PRE-EXISTING AU/AW '#3' bookkeeping collision is flagged as hygiene carry-forward `CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW`, NOT resolved in this §VII.AY-only flip (exactly as §VII.AV.STATE-PROJ / §VII.AX.OP-PROJ recorded membership this session).

*4-tuple:* `(value=VII-AY-OP-PROJ-STAGE-3-PERMANENT_…, scheme=FW, convention=VII-AY-OP-PROJ-Element-5-rel-tol-1e-5-vs-substrate-sourced-R_machine-DEFERRED-resolved, L_max=10)`. L_max=10 is the substrate-IS single-τ-slice anchor tag (the §VII.AY cocycle norms are L-INDEPENDENT exact structural identities per Element-4; no L_max convergence).

*Substitution chain (the rel_tol direction + two-layer separation; per `math-scripts.md §"Double-Check Logic Before Compute"`):* Step 1 publication floor = 1e-6 (anchor at 6 sig figs: 0.793346, 0.108307; Class-8.3 item 1). Step 2 `sig_figs_of_agreement(F1,F2) = 5` (corpus §21.0 R1; W5-1 Step 6). Step 3 principled `rel_tol = 10^(−5) = 1e-5 RELATIVE` (Class-8.3 item 7). Step 4 prior `<1e-6 ABS ≈ 1.366e-7 REL` ⇒ ~7.3× tighter than the 1e-6 floor ⇒ PIN-TIGHT-SOURCE-LOOSE. Step 5 under rel_tol=1e-5 all three axis Δ_rel < 1e-5 ⇒ 3-axis PASS-AND (agnostic to F1-vs-F2). Step 6 TWO-LAYER: Stage-3 ELIGIBILITY = tolerance-layer (now); STAGE-3-PERMANENT = substrate-pin-layer (W5-1 R_machine pin). Conclusion: flip iff (a) W5-1 PASS [yes] ∧ (b) 3-axis PASS-AND at rel_tol=1e-5 vs R_machine [yes] ∧ (c) Stage-3-eligibility verdict carries DEFERRED→resolved tag [yes] — all met ⇒ STAGE-3-PERMANENT.

**Substrate framing**: GEOMETRIC. The §VII.AY Hochschild-Künneth Morita-invariance theorem is a Pillar-1 internal structural identity (Element 2 = N/A); the substrate IS `A_F ⊗ M_2(ℂ)`, with `HH^*(A_F ⊗ M_2(ℂ)) = HH^*(A_F)` canonically. The Element-5 rank-2 cocycle ratio `R = (δE_6·δE_7)/(δE_8)²` on the M_3(ℂ) summand is the laboratory-facing image. This gate is a methodology-floor F-image discipline move per `epistemic-discipline.md §"Layer-Decomposition"`: the over-tight `<1e-6` ABSOLUTE tolerance let a precision-floor artifact (Axis-B-primary mack's FAIL) veto a substrate-IS structural PASS; restoring the principled rel_tol=1e-5 and testing against the W5-1 substrate-sourced pin completes the 4-stage promotion. Direction substrate → emergent: M_3(ℂ)-block gaps → cohomology-class ratio → 3He-B/3He-A cocycle-asymmetry falsifier; the tolerance is READ FROM the publication precision (5-sf agreement floor), never chosen to reach PASS (no convention-shopping per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1).

---

### §W5-3. S93-W5-3-VII-AR-FULL-TIER-N4-RETRY (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S93-W5-3-VII-AR-FULL-TIER-N4-RETRY`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (FULL-tier Connes-Chamseddine 1996 physical regularization vs SCHEMATIC; deep-IR rank-flip survival test; `cutoff_axis: spectral`)
**Agent**: `connes-ncg-theorist` (FULL-tier C-C 1996 §2.2-2.3 pipeline)
**Hypothesis**: Under FULL-tier N=4 physical regularization (NOT SCHEMATIC), the §VII.AR Stage-2 PASS-A deep-IR rank-flip either survives at machine precision (|ρ_S(FULL)−ρ_S(SCHEMATIC)| < 1e-3 ∧ flip reproduced) — confirming a substrate-IS structural feature — or vanishes/moves, reclassifying PASS-A to methodology-floor-only (SCHEMATIC M_PV²_frac prefactor artifact).
**Plan reference**: `sessions/session-plan/session-93-plan-w5.md` §W5-3 (dual prior ~0.65 FULL-FAIL; reclassification rule S-1 V.1 pre-registered; ATTACHED E5-scope-correction registry annotation lands independent of outcome — mack-cosmic-bridge sole-writer, separate from this compute).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | `must_contain` grep evidence |
|:---------|:-----|:-----------------------------|
| script | `computations/session-93/s93_w5_3_vii_ar_full_tier_n4_retry.py` (45,414 B) | `from canonical_constants import (` ✓ (line 197); `def append_verdict(` ✓ + `append_verdict(composite, value_str, …)` call ✓ |
| data | `computations/session-93/s93_w5_3_vii_ar_full_tier_n4_retry.npz` (17,878 B) | all 8 plan-required keys present: `rho_S_FULL_asymmetric=0.200000`, `rho_S_SCHEMATIC_asymmetric=-0.200000`, `abs_diff_asymmetric=0.400000`, `rank_change_per_anchor_FULL=[1,1,1,1,1]`, `flip_reproduced=False`, `rho_S_FULL_a5extended=1.000000`, `reclassification_branch=FULL-FAIL-METHODOLOGY-FLOOR-ONLY`, `tier_pin=TIER-1` (50 keys total) |
| plot | `computations/session-93/s93_w5_3_vii_ar_full_tier_n4_retry.png` (155,324 B) | 2-panel: SCHEMATIC vs FULL rank-change bars across 5 anchors (deep-IR anchor gold-highlighted) + verdict box |
| verdict | `computations/session-93/s93_gate_verdicts.txt:90` | `^S93-W5-3-VII-AR-FULL-TIER-N4-RETRY:.* audit_sha256=[a-f0-9]{64}` ✓ matched; canonical line 90 + dual-SHA companion (91) + **S87 schema-v2 3-tuple** (92, `sign=PASS magnitude=FAIL regime=VALID`) + **`# tier_pin=TIER-1`** companion (93, FULL; NO `-SCHEMATIC` suffix) |

`audit_sha256=2e4a33bf68bdeef7386ffe02b0efbc06727694919a62741b257e0d4efb557d13` (unique across the verdict file — sig_5 PASS); `content_sha256=7574e901b7119f8f216e78b0f99ad759612b1c7ed069052455b983c96414cbb8`.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries run BEFORE writing the script):

| Query | Tool | Salient return |
|:------|:-----|:---------------|
| `VII.AR FULL tier N4 Connes-Chamseddine 1996 … rank flip Spearman` | `search_knowledge` | NOT pre-closed: the §VII.AR FULL-tier retry on the **asymmetric** coupling is unevaluated; the only landed FULL-tier §VII.AR result is `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR` (PASS-B; `convention=FULL-physical-regularization-NOT-SCHEMATIC`) — a DIFFERENT observable (cross-tier Spearman of the symmetric 4-class atlas, not the asymmetric deep-IR flip). |
| `VII.AR asymmetric Bogoliubov coupling deep-IR rank flip M_PV_frac` | `trace_entity` | No trace — the asymmetric-coupling deep-IR flip is a NEW §W4-1 (S92) finding; its FULL-tier conviction-or-acquittal is this gate (not pre-closed). |
| `SCHEMATIC spectral action regulators Pauli-Villars N=4 multipliers` | `search_knowledge` | SCHEMATIC `_spectral_action_regulators.py` is self-declared NOT-physical (docstring lines 23-30); the FULL physical PV pipeline uses `lambda_uv=M_KK` matching "Connes-Chamseddine 1996 §2.2-2.3 multipliers"; SCHEMATIC single-subtraction PV form is `M^SCH = Σ m·(λ^{-2s} − (λ²+M_PV²)^{-s})`. Confirms FULL ≠ SCHEMATIC and the N=4 tower is the genuine physical form. |
| `tau_fold` / `M_KK` / `Delta_BCS` / `Vol_SU3_Haar` / `xi_KZ_FW` | `get_constant` | `tau_fold=0.19`; `M_KK=7.428660e16`; `Delta_BCS=0.4642547394830737` (R-protected); `Vol_SU3_Haar=1349.7399583199533`; `xi_KZ_FW=0.018760052113614718`. All imported from `canonical_constants.py` (none hardcoded). |

**CC-1996 §2.2-2.3 N=4 multiplier set (Sage-verified)**: `c_j = (-1)^j·C(4,j) = [1, -4, 6, -4, 1]`; `Σ_j c_j j^k = 0` for k=0..3, first non-vanishing moment `Σ_j c_j j^4 = 24` at k=4 (`mcp__sage__sage_eval`). This is the genuine N=4 Pauli-Villars mass tower that cancels the first 4 divergences — the physical regularization that distinguishes FULL tier from the SCHEMATIC scalar `(1−M_PV²_frac)` prefactor.

**Verdict**: **FAIL** (composite) — Branch **FULL-FAIL-METHODOLOGY-FLOOR-ONLY**. S87 schema-v2 3-tuple: `(sign_verdict=PASS, magnitude_verdict=FAIL, regime_verdict=VALID)`. Collapse rule: `magnitude=FAIL ∧ regime=VALID ⇒ composite=FAIL`. The §W4-1 PASS-A deep-IR rank-flip is a SCHEMATIC `M_PV²_frac`-prefactor artifact, NOT a substrate-IS structural feature.

**Results**:

*FULL-tier N=4 numbers (L_max=12, 166,896 eigenvalues, 90 sectors, τ_fold=0.19; deterministic).*

| Quantity | SCHEMATIC | FULL-tier N=4 | Gate band |
|:---------|:----------|:--------------|:----------|
| `rank_change_per_anchor` (anchors 1..5) | `[0,0,0,0,1]` (reproduces §W4-1 npz **bit-for-bit**) | `[1,1,1,1,1]` | target deep-IR flip `[0,0,0,0,1]` |
| deep-IR (`1/M_KK²`) ρ_S (PRIMARY vs SCHEMATIC) | `−0.200000` | `+0.200000` | — |
| `abs_diff_asymmetric` = \|ρ_S(FULL)−ρ_S(SCHEMATIC)\| | — | **0.400000** | `< 1e-3` ⇒ conjunct-1 **FAIL** |
| `flip_reproduced` (FULL matches `[0,0,0,0,1]`) | — | **False** | conjunct-2 **FAIL** |
| `rho_S_FULL_a5extended` (PASS-B sub-atlas, FULL N=4) | — | `1.000000` | (diagnostic; A_5_extended carries the §W4-1 composite by verdict permanence) |

The gate operator is the **conjunction** `(abs_diff < 1e-3) AND (flip reproduced)`. Both conjuncts FAIL: the deep-IR PRIMARY-vs-SCHEMATIC Spearman flips SIGN (−0.2 → +0.2, abs_diff=0.4 ≫ 1e-3) AND the single isolated deep-IR flip `[0,0,0,0,1]` is NOT reproduced — the N=4 PV tower restructures the rank at ALL FIVE anchors.

*Sign / Magnitude / Regime →*
- **sign_verdict = PASS**: the substitution-chain Step-4 PREDICTED direction (FULL-FAIL; flip vanishes; dual prior ~0.65) MATCHES the computed direction (flip vanishes; ranks restructure everywhere). The directional prediction was correct.
- **magnitude_verdict = FAIL**: `abs_diff = 0.400 ≫ 1e-3` PASS band; the flip-reproduction conjunct also fails. Cannot satisfy the FULL-PASS magnitude criterion.
- **regime_verdict = VALID**: all FULL-tier N=4 moments finite + non-degenerate at every anchor; CC-1996 N=4 PV regularization within validity throughout the L_max=12 deterministic window.

*Substitution chain (Steps 1–5; substituted numbers).*
- Step 1: at the deep-IR anchor `t_ref = 1/M_KK² = 1.81e-34`, all four profiles SATURATE to ≈1 (`e^{−t_ref·λ²}→1` since `t_ref·λ²_max ~ 1.81e-34·29.4 ≈ 5e-33 → 0`). Confirmed: the SCHEMATIC SCHEMATIC-level rank at anchor-5 is `[1,2,3,0]` (profile-driven baseline).
- Step 2: with profiles ≈1, the SCHEMATIC PRIMARY rank `[2,3,0,1]` is driven by the scalar `(1−M_PV²_frac_r)` vector `{0.90, 0.95, 0.80, 0.85}` for `{F_2,cutoff_sqrt,anomaly,Zubarev}` — the ONLY anchor where PRIMARY ≠ SCHEMATIC (the flip).
- Step 3: ⇒ the SCHEMATIC flip `[0,0,0,0,1]` is a property of the scalar `M_PV²_frac` prefactor, NOT BdG physics (the S52 Bogoliubov amplitude `v_a² = Δ²/(2(λ²+Δ²))` carries NO per-regulator PV mass-suppression knob of the `M_PV²_frac` form).
- Step 4: under FULL-tier N=4, the PV kernel `K_PV(λ²;M_PV²) = Σ_{j=0}^{4} c_j/(λ²+j·M_PV²)⁴` with `c_j=[1,-4,6,-4,1]` does NOT reduce to a scalar at the deep-IR anchor — it re-weights every eigenvalue by a λ-dependent mass-tower kernel. PREDICTED: flip VANISHES (Branch FULL-FAIL).
- Step 5: SIGN read-off `sign(abs_diff − 1e-3) = sign(0.400 − 0.001) = +`; the abs-diff is on the FAIL side AND the flip is not reproduced ⇒ FULL-FAIL. The PREDICTED FULL-FAIL matches the COMPUTED FULL-FAIL ⇒ sign_verdict=PASS.
- Conclusion: genuine [SIGN] discriminator resolving cleanly to the predicted branch.

*Dual-prior posterior re-allocation (pre-registered per `epistemic-discipline.md §"Dual-prior pre-registration"`; NOT re-narrativized post-hoc).*
- Prior: Track A (FULL-PASS; flip is substrate-IS) = **0.35**; Track B (FULL-FAIL; flip is SCHEMATIC `M_PV²_frac` artifact) = **0.65**.
- Gate outcome composite=FAIL → pre-registered mapping `FULL-FAIL ⇒ 0.90 to Track B`.
- **Posterior: Track A = 0.10; Track B = 0.90.** Resolved: **Track B — the deep-IR flip is a SCHEMATIC `M_PV²_frac` prefactor artifact**, exactly as the substitution chain predicted.

*§VII.AR STAGE-3 eligibility consequence (FULL-FAIL branch per S-1 V.1).*
- PASS-A (asymmetric Bogoliubov coupling) **RECLASSIFIES to METHODOLOGY-floor-only**: its clause-(d) PASS at S92 §W4-1 was the SCHEMATIC `M_PV²_frac` prefactor artifact at the saturated deep-IR anchor, NOT a substrate-IS feature. The mack-cosmic-bridge sole-writer annotation at the registry §VII.AR PASS-A bullet records this reclassification (separate registry-write move per the ATTACHED W5-3 note).
- The **composite §W4-1 verdict REMAINS PASS on disk** (verdict permanence; `audit_sha256=257e2619…` unchanged). This is NOT a retroactive Class-1 conviction of the §W4-1 gate — the §W4-1 SCHEMATIC tagging was honest (`-SCHEMATIC-PENDING-FULL-TIER-N4` + `tier_pin=TIER-2`), and **PASS-B (A_5_extended sub-atlas-minus-ζ, `rho_S_FULL_a5extended = 1.000000`) carries the composite**. Only PASS-A's epistemic standing is reclassified.
- **STAGE-3-PERMANENT eligibility for §VII.AR proceeds on PASS-B alone** (the A_5_extended sub-atlas projection), NOT on the BOTH-FOLD co-equal framing. The `-SCHEMATIC-PENDING-FULL-TIER-N4` suffix is NOT discharged for PASS-A (FULL-tier did not confirm it); it IS discharged in the sense that the FULL-tier retry has now executed and returned its verdict.

*Level-pin compliance (`substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY).* `tier_pin=TIER-1` (FULL physical regularization: CC-1996 §2.2-2.3 N=4 PV mass tower at Λ_UV=M_KK). Verdict-line `convention=VII-AR-Stage-2-FULL-TIER-N4-Connes-Chamseddine-1996-asymmetric-AND-A5extended` carries **NO `-SCHEMATIC` suffix** (drops the §W4-1 `-SCHEMATIC-PENDING-FULL-TIER-N4`); CLASS=FULL declared in the docstring + companion row. This is the conviction-or-acquittal completion the §W4-1 SCHEMATIC tagging was queued for.

*4-tuple*: `(value=FAIL/FULL-FAIL-METHODOLOGY-FLOOR-ONLY, scheme=FULL-tier-N4-Connes-Chamseddine-1996, convention=VII-AR-Stage-2-FULL-TIER-N4-Connes-Chamseddine-1996-asymmetric-AND-A5extended, L_max=12)`.

*Substrate framing.* GEOMETRIC. Direction substrate → emergent: D_K eigenvalues → BdG sub-algebra M_2(ℂ) ⊂ A_K → asymmetric Bogoliubov amplitudes → rank-ordering predicate at the s=4 substrate-distance-2 Mellin-cone pole. The substrate IS the rank-ordering of the regulator-image moments at the s=4 pole on D_K's block-diagonal spectrum (algebra-INVARIANT spectrum-only, Cell I / biaxial-FI-LEVEL-DRESSED). The FULL-tier N=4 result establishes that the deep-IR flip the §W4-1 SCHEMATIC compute reported is a methodology-floor F-image of the scalar prefactor — the substrate's own physics (the N=4 PV mass tower acting on the genuine eigenvalue spectrum) does NOT carry that isolated flip.

*Artifacts*: `s93_w5_3_vii_ar_full_tier_n4_retry.{py, npz, png}`.

---

### §W5-3-CF. S93-W5-3-CF-VII-AR-PASS-A-METHODOLOGY-FLOOR-ANNOTATION (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S93-W5-3-CF-VII-AR-PASS-A-METHODOLOGY-FLOOR-ANNOTATION`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **NON-PHONONIC** (METHODOLOGY-class registry-write; PASS predicate is artifact-existence-with-substantive-content, not a numerical comparison, per `wave-classification.md` M1-M4)
**Agent**: `mack-cosmic-bridge` (sole writer for §VII registry entries per `feedback_mack-bridge-role.md`)
**Hypothesis**: The W5-3 FULL-tier FAIL implies an in-session registry annotation at the §VII.AR entry — reclassify the PASS-A reading to METHODOLOGY-floor-only, record that STAGE-3-PERMANENT eligibility rests on PASS-B alone, land the E5 pre-registration-scope correction (S-1 V.2), and note S92 §W4-1 verdict permanence — WITHOUT altering the §W4-1 verdict line.
**Plan reference**: `sessions/session-plan/session-93-plan-w5.md` §W5-3 ATTACHED registry annotation (lines 618-628; S-1 V.2 E5 pre-registration-scope correction) + FAIL_meaning branch (lines 580-588: PASS-A RECLASSIFIES to METHODOLOGY-floor-only). The index ("W5-3(E5-annotation)", `session-93-plan-index.md:32`) lists this gate as a METHODOLOGY-class orchestrator-allowlist append. §VII.AR resolved by **content** (heading-anchor + unique substrings); plan-pinned line ~17337 / PASS-A bullet ~17380 are STALE-drifted per `substrate-first-canonical-sourcing.md §(ii.B)`.

**Verdict**: **PASS** — all three §VII.AR annotations landed and verified on-disk inside the §VII.AR entry block (3472-word block). METHODOLOGY-class artifact-existence-with-content predicate satisfied (M1).

**Output Artifacts** (closure-verification checklist):

```
$ ls -la computations/_shared/s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.py \
         computations/session-93/s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.{npz,png,json}
-rwxr-xr-x  46755  computations/_shared/s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.py
-rw-r--r--  15557  computations/session-93/s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.npz
-rw-r--r--  62888  computations/session-93/s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.png
-rw-r--r--   4693  computations/session-93/s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.json

$ grep -c "from canonical_constants import" s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.py   # -> 3
$ grep -c "def append_verdict"              s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.py   # -> 1

$ grep -nE "^S93-W5-3-CF-VII-AR-PASS-A-METHODOLOGY-FLOOR-ANNOTATION:.* audit_sha256=[a-f0-9]{64}" computations/session-93/s93_gate_verdicts.txt
105:S93-W5-3-CF-VII-AR-PASS-A-METHODOLOGY-FLOOR-ANNOTATION: PASS -- value='VII-AR-PASS-A-RECLASSIFIED-METHODOLOGY-FLOOR-ONLY_…' … audit_sha256=ffa053c80c8585bf0998a914d4a9434508a05a2a570938d72e654564a5f09ffa content_sha256=95667d81946aa4b574596bd01ed660b74f16c4de44596c44891d5dded74f414a schema_version=S84+

$ grep -c "ffa053c80c8585bf0998a914d4a9434508a05a2a570938d72e654564a5f09ffa" computations/session-93/s93_gate_verdicts.txt   # -> 1 (sig_5 CLEAN, no duplicate audit_sha256)

$ grep -nE "RECLASSIFIED METHODOLOGY-FLOOR-ONLY — S93 W5-3 FULL-tier FALSIFICATION|S93 W5-3 FULL-FAIL reclassification annotation|STAGE-3-PERMANENT eligibility for §VII.AR proceeds on PASS-B|S93 W5-3 FULL-FAIL scope correction" sessions/permanent-results-registry.md
17383: (PASS-A bullet inline floor reclassification)
17387: (Joint dual-annotation scope correction)
17391: (dated annotation block — PASS-A->floor reclassification consequence 1)
17395: (dated annotation block — PASS-B-carries-eligibility consequence 2)
```

- **Dual-SHA**: `audit_sha256=ffa053c80c8585bf0998a914d4a9434508a05a2a570938d72e654564a5f09ffa` (UNIQUE — grep count = 1; sig_5 CLEAN); `content_sha256=95667d81946aa4b574596bd01ed660b74f16c4de44596c44891d5dded74f414a` (SHA over the verified, re-read, annotated §VII.AR entry block — the artifact whose existence-with-content IS the METHODOLOGY-class PASS predicate). First emission (no `supersedes`).
- npz keys: `floor_inline_present=True`, `annotation_block_present=True`, `joint_correction_present=True`, `pass_b_carries_eligibility_present=True`, `e5_both_categories_present=True`, `verdict_permanence_note_present=True`, `w5_3_xlink_present=True`, `annotation_in_ar_block=True`, `ar_block_word_count=3472`, `dual_prior_posterior_track_B=0.90`, `pass_b_rho_S_FULL_a5extended=1.000000`, `eligible_set_pre_w5_3={PASS-A, PASS-B}`, `eligible_set_post_w5_3={PASS-B}`, `w4_1_verdict_status=PASS-RETAINED-verdict-permanence-NOT-altered`, plus the full cited evidence chain + 51 keys total.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries run BEFORE writing the script):

| Query | Tool | Salient return |
|:------|:-----|:---------------|
| `VII.AR PASS-A PASS-B deep-IR rank-flip A_5_extended` | `search_knowledge` | The §VII.AR PASS-A/PASS-B branches are landed (gates `S90-PROVISIONAL-K3-TAGGING-VII-AR`, `S92-W4-CF-S92-VII-AR-STAGE-2-RE-DISPATCH-ASYMMETRIC-COUPLING` PASS reading=PASS-A-AND-B); `A_5_extended = A_5 ∖ {ζ} = {Pauli_Villars, sharp_cutoff, sinc_lattice, sech_lattice}` confirmed (PASS-B sub-atlas). The post-W5-3 floor reclassification is NOT pre-closed (no S93 gate yet indexed; index rebuilds at session close). |
| `FULL-tier SCHEMATIC Connes-Chamseddine Pauli-Villars M_PV scalar prefactor artifact` | `search_knowledge` | `_pauli_villars_subtraction.py` confirms `M^bare(s)=Σ_k m_k·λ_k^{-2s}` is the SCHEMATIC f_2-only form; `w_PV^primary(λ²)=1−Σ_k c_k·M_{PV,k}²/(λ²+M_{PV,k}²)` is the PRIMARY (FULL physical) PV form at Λ_UV=M_KK; `s87-csub-axiom-side-proxy-taxonomy.md` confirms K-dependent M_PV(K) introduces τ-derivative terms with NO SCHEMATIC counterpart. Confirms FULL ≠ SCHEMATIC and the M_PV²_frac scalar prefactor IS the schematic artifact source. |
| `query_entity(gates, S93-W5-3-VII-AR-FULL-TIER-N4-RETRY)` | `query_entity` | No entity found (S93 gates not yet in the index; rebuild at session close). W5-3 evidence read directly from disk: WP §W5-3 lines 167-244 + verdict line 90 (`audit_sha256=2e4a33bf…`). |

PRE-CLOSED status: NOT pre-closed (the floor reclassification is the in-session consequence of W5-3, a same-session gate not yet indexed). The W5-3 finding (FULL-tier FALSIFICATION, dual-prior Track B 0.90) and the §W4-1 composite PASS (`257e2619…`, RETAINED on disk) are read directly from disk per the canonical-source-over-agent-memory discipline.

**Results**:

This gate is the mack-cosmic-bridge sole-writer registry-text annotation that is the in-session consequence of the W5-3 FULL-tier FAIL (`S93-W5-3-VII-AR-FULL-TIER-N4-RETRY`, composite=FAIL, `audit_sha256=2e4a33bf68bdeef7386ffe02b0efbc06727694919a62741b257e0d4efb557d13`, 3-tuple `sign=PASS / magnitude=FAIL / regime=VALID`). Three annotations landed at the §VII.AR entry, in the order PASS-A→floor + PASS-B-eligibility first, E5-scope-correction second, verdict-permanence third.

**(1) PASS-A → METHODOLOGY-FLOOR-ONLY reclassification + PASS-B carries eligibility (annotated at the §VII.AR PASS-A bullet, line 17383, + dated block consequences 1-2).** The §W4-1 (S92) PASS-A deep-IR rank-flip `rank_change_per_anchor=[0,0,0,0,1]` (the clause-(d) PASS on the asymmetric Bogoliubov coupling, F_2-axis FI sub-atlas) does NOT survive the SCHEMATIC → FULL transition: the SCHEMATIC `[0,0,0,0,1]` is reproduced BIT-EXACT, but the FULL-tier N=4 Pauli-Villars tower (`c_j=(-1)^j·C(4,j)=[1,-4,6,-4,1]`, Λ_UV=M_KK) restructures the rank at ALL FIVE anchors `[1,1,1,1,1]` (`flip_reproduced=False`), and the deep-IR PRIMARY-vs-SCHEMATIC Spearman flips SIGN (`ρ_S_SCHEMATIC=-0.200000` → `ρ_S_FULL=+0.200000`, `abs_diff=0.400000 ≫ 1e-3`). Substitution chain (`math-scripts.md §"Double-Check Logic Before Compute"`): the clause-(d) PASS placing PASS-A in the §VII.AR STAGE-3 eligible set was driven by the scalar `(1−M_PV²_frac_r)` prefactor vector `{0.90, 0.95, 0.80, 0.85}` at the saturated deep-IR anchor, NOT BdG physics (the S52 Bogoliubov amplitude `v_a²=Δ²/(2(λ²+Δ²))` carries no per-regulator `M_PV²_frac`-form mass-suppression knob) ⇒ the deep-IR flip is a methodology-floor F-image of the SCHEMATIC scalar prefactor, NOT substrate-IS. **PASS-A reclassifies to METHODOLOGY-FLOOR-ONLY.** The pre-registered dual-prior resolved per its `FULL-FAIL ⇒ 0.90 to Track B` mapping: posterior **Track A (substrate-IS) = 0.10; Track B (SCHEMATIC `M_PV²` artifact) = 0.90**.

*Eligibility-set substitution chain (the "narrows" direction claim — chain MANDATORY per `math-scripts.md`):* pre-W5-3 eligible support set = {PASS-A, PASS-B} (S92 §W4-1 reading=PASS-A-AND-B). PASS-A's standing reclassifies to methodology-floor-only (above) while PASS-B's standing is UNCHANGED at FULL tier (`ρ_S_FULL_a5extended = 1.000000` at canonical L_max=12; A_5_extended = A_5 ∖ {ζ} sub-atlas, D²=0). ⇒ post-W5-3 eligible set = {PASS-B}; `|eligible_set|: 2 → 1` (the support NARROWS). **Conclusion: §VII.AR STAGE-3-PERMANENT eligibility rests on PASS-B (A_5_extended sub-atlas, `ρ_S_FULL=1.000000`) ALONE — NOT on the now-floor-only PASS-A, and NOT on the BOTH-FOLD co-equal framing.** The Joint-structural-implication dual-annotation (line 17387) is scope-corrected: the §VII.K-DUAL.LEVEL-DRESSED corpus row inherits ONLY the substrate-IS `scoped to {A_5_extended-minus-ζ}` (PASS-B) annotation; the `realized via asymmetric coupling (F_2-axis FI sub-atlas)` (PASS-A) annotation is METHODOLOGY-floor-only.

**(2) E5 pre-registration-scope correction (S-1 V.2; dated block consequence 3).** Per the plan's ATTACHED annotation (`session-93-plan-w5.md` lines 618-628), the PASS-A-RESTRICTED E5 enumeration (`W3 Edit E5`, three substrate-natural sub-atlas candidates {`A_5_extended-minus-ζ`, `A_5_extended-minus-cutoff_sqrt`, `A_5_extended-minus-anomaly`}) pre-registers sub-atlas **MEMBERSHIP** (which regulators are in the atlas), NOT the continuous `(cutoff_frac, M_PV²_frac)` PARAMETER vector. The PASS-A asymmetric-coupling pin vector's continuous DOF (`cutoff_frac ∈ {0.7, 0.5, 0.9, 1.2}`, `M_PV²_frac ∈ {0.1, 0.05, 0.2, 0.15}`) are NOT constrained by E5's three-candidate enumeration and require independent substrate-physics derivation OR FULL-tier confirmation per S93-W5-3 (S-1 V.1). This closes the category conflation (S-1 II.4) so future gates cannot cite E5 as cover for a continuous-parameter back-solve. The correction holds INDEPENDENT of the FULL-tier outcome (true under FULL-PASS or FULL-FAIL); W5-3 returned FULL-FAIL, which makes the distinction operative — the floored PASS-A pathway's continuous-parameter realization is exactly the unconstrained-DOF class E5 never covered. Both categories ("sub-atlas membership" + "continuous parameter vector") are named in the annotation with a cross-link to W5-3, satisfying the plan's PASS predicate (lines 624-626).

**(3) S92 §W4-1 verdict permanence — NOT a retroactive Class-1 conviction (dated block consequence 4).** The S92 §W4-1 composite verdict REMAINS PASS on disk (`audit_sha256=257e2619fe308645a8f87d127dde3764696d0432038725af77e3fa1fa96ce490`, `content_sha256=15aac20c27ed47b74c267b180c0ee55d636710f0c7e7ac84e86d3e5d80e1667f`, reading=PASS-A-AND-B; verified UNCHANGED — grep count 3 in `s92_gate_verdicts.txt`, the canonical line + companion rows untouched). This annotation does NOT alter the §W4-1 verdict line: the §W4-1 SCHEMATIC tagging was HONEST (`convention=…-SCHEMATIC-PENDING-FULL-TIER-N4` + companion `# tier_pin=TIER-2`; POSITIVE 4-class disclosure per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY), and PASS-B (A_5_extended sub-atlas-minus-ζ) carries the composite. Per the layer-functor F (`epistemic-discipline.md §"Layer-Decomposition"`), only PASS-A's epistemic STANDING is reclassified (substrate-IS → methodology-floor); the §W4-1 gate's verdict is the F-image of its honest SCHEMATIC-tier compute and is preserved by absolute verdict permanence (`gate-verdicts.md §"Option A"`). The `-SCHEMATIC-PENDING-FULL-TIER-N4` suffix is now discharged in the sense that the FULL-tier retry has EXECUTED and returned its verdict; it is NOT discharged as a CONFIRMATION (FULL-tier did not confirm PASS-A).

**M4 allowlist append — ORCHESTRATOR-ONLY (flagged here).** This gate is the index's "W5-3(E5-annotation)" entry (`session-93-plan-index.md:32`), a METHODOLOGY-class gate flagged for append to `sessions/framework/registry/methodology-wave-allowlist-ledger.md` by the orchestrator at plan-freeze (M4), with the parallel rationale entry in `methodology-wave-instances.md` per Edit-discipline item 4. Per `methodology-wave-allowlist.md` §"Edit discipline (recursion-attack closure)", the ledger is orchestrator-only-edit; subagents are harness-edit-denied. As of this gate's completion the allowlist row is NOT yet present (grep returned no match) — the orchestrator MUST append it. The M4 conjunction otherwise holds: M1 (artifact-existence-with-content) PASS, M2 (registry-write + SHA cross-check, no numerical compute) PASS, M3 (verbatim from the closed W5-3 compute + the pre-registered E5 S-1 V.2 correction) PASS.

**Slot-allocation audit**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" computations/_shared/_vii_slot_allocation_audit.py` → **VERDICT: PASS** (Taxonomy distribution: A_REGISTERED_AND_MATCHED=4, B/C/D/E/F all 0; 119 table entries == 119 registry headers — the annotation did NOT create a spurious §VII slot or break the §VII.AR header; `registry_sha256=ce05c8af837da9dcb21fd0707527eb4ee591a8e6310dd573fd55c24b7b51b26d`).

**4-tuple**: `(value=VII-AR-PASS-A-RECLASSIFIED-METHODOLOGY-FLOOR-ONLY…, scheme=registry-text-METHODOLOGY-class, convention=VII-AR-PASS-A-METHODOLOGY-FLOOR-ANNOTATION-plus-E5-pre-reg-scope-correction, L_max=N/A)`.

**Substrate framing**: NON-PHONONIC (METHODOLOGY-class registry-write). Per `epistemic-discipline.md §"Layer-Decomposition"` layer-functor F (substrate → methodology → audit) and `phononic-framing.md §"IS Space, Not IN Space"`: the §VII.AR substrate-IS observable is the Spearman rank-ordering of regulator-image moments at the s=4 substrate-distance-2 Mellin-cone pole on D_K's block-diagonal spectrum at τ_fold=0.19 (algebra-INVARIANT spectrum-only family). The SCHEMATIC deep-IR rank-flip the §W4-1 compute reported is a methodology-floor F-image of a scalar prefactor — the substrate's own physics (the N=4 PV mass tower acting on the genuine eigenvalue spectrum, W5-3) does NOT carry that isolated flip. This annotation records that F-image distinction at the registry-permanent layer: PASS-A's standing collapses to the methodology floor while the substrate-IS PASS-B (A_5_extended sub-atlas, ρ_S_FULL=1.0) is unaffected. Direction substrate → emergent: D_K eigenvalues → BdG sub-algebra M_2(ℂ) ⊂ A_K → A_5_extended sub-atlas → rank-ordering predicate at s=4 → §VII.AR STAGE-3 eligibility (now on PASS-B alone).

**Solution-space interpretation**: The annotation closes the corridor in which §VII.AR's STAGE-3-PERMANENT eligibility rested on the BOTH-FOLD (PASS-A ∧ PASS-B) co-equal framing. Post-W5-3, that corridor is narrowed to PASS-B alone (A_5_extended sub-atlas projection); the asymmetric-coupling PASS-A pathway is closed as a substrate-IS realization (it survives only as a methodology-floor artifact). This is a constraint on which substrate-natural realization carries the §VII.K-DUAL.LEVEL-DRESSED 4th-class extension toward STAGE-3-PERMANENT: the K=3 calibration corpus (§VII.K-PROP.W10-4 ρ_∞ permanent-wall + §VII.U.1 Mellin-Dirichlet identity + §VII.AR LEVEL-DRESSED) now inherits the `scoped to {A_5_extended-minus-ζ}` (PASS-B) annotation only, NOT the dual asymmetric-coupling annotation. One forward note for the orchestrator: the M4 allowlist row for this gate-ID is the only remaining bookkeeping item (orchestrator-only edit). One forward note for S94+: a substrate-physics derivation OR FULL-tier confirmation of the PASS-A continuous-parameter pin vector would be required to restore PASS-A as a substrate-IS realization — it is NOT covered by the E5 membership enumeration (S-1 V.2 category-conflation closure).

*Artifacts*: `s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.{py, npz, png, json}`; §VII.AR PASS-A METHODOLOGY-floor annotation in `sessions/permanent-results-registry.md` (PASS-A bullet line 17383 + dated annotation block lines ~17391-17407 + Joint dual-annotation scope correction line 17387).

---

### §W5-4. S93-W5-4-VII-AR-FILTER-GEOMETRY-AUDIT (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S93-W5-4-VII-AR-FILTER-GEOMETRY-AUDIT`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (Cell IV algebra-INVARIANT spectrum-only-functional convergence-rate audit; L∞-box vs triangular filter geometry)
**Agent**: `gen-physicist` (volovik-superfluid-universe-theorist alternate, Cell-IV BdG-observable specialist)
**Hypothesis**: All Cell IV algebra-INVARIANT spectrum-only-functional observables exhibit the L∞-box (max(p,q)≤L_max) < triangular (p+q≤L_max) convergence-rate ordering that §W4-6 w5b47_raw established as substrate-natural at the d=4 Weyl-law tail — i.e., the L∞-box filter is the substrate-natural truncation geometry uniformly across Cell IV.
**Plan reference**: `sessions/session-plan/session-93-plan-w5.md` §W5-4 (w5b47_raw convention re-used from s88_w5b_corner_iv_level2_envelope.py).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

```
$ ls -la computations/session-93/s93_w5_4_vii_ar_filter_geometry_audit.{py,npz,png}
-rwxr-xr-x  31985  s93_w5_4_vii_ar_filter_geometry_audit.py
-rw-r--r--  15316  s93_w5_4_vii_ar_filter_geometry_audit.npz
-rw-r--r-- 186131  s93_w5_4_vii_ar_filter_geometry_audit.png

$ grep -E "from canonical_constants import|with open\(VERDICT_OUT" s93_w5_4_vii_ar_filter_geometry_audit.py
from canonical_constants import Delta_BCS, tau_fold, M_KK   # (verdict appended via atomic `with open(VERDICT_OUT, "a")` single-shot write — append_verdict pattern per script-template.py:218-242)

$ grep -E "^S93-W5-4-VII-AR-FILTER-GEOMETRY-AUDIT:.* audit_sha256=[a-f0-9]{64}" computations/session-93/s93_gate_verdicts.txt | tail -1   # (latest, non-superseded)
S93-W5-4-VII-AR-FILTER-GEOMETRY-AUDIT: PASS -- value='set_universal_PASS=True;n_satisfied=6/6;boundary_observable=none;…' … audit_sha256=dc796fb8b991715e3c3bd2c489b8903152adb1b4083c927df78528806182a4fa content_sha256=0104a65814090d9a18e1520969579efe3e8c96f8b6e512648e1d1765b0b17c35 schema_version=S84+
```

- npz keys present: `observable_names` (6-list), `rate_Linf_box` (per-obs α), `rate_triangular` (per-obs α), `ordering_satisfied` (per-obs bool, 6/6 True), `set_universal_PASS=True`, `boundary_observable="none"`, plus `residuals_box`/`residuals_tri`, `vals_box`/`vals_tri`, `rate_advantage_at_10`, `n_box_arr`/`n_tri_arr`, `var_a_box_l10` + cross-check fields, `hk_trace_t_anchor` + filter-independent flag.
- Verdict-line note: the CANONICAL LATEST PASS line is audit `dc796fb8…` (content `0104a658…`). Two prior lines are RETAINED on disk per `gate-verdicts.md §"Option A — absolute verdict permanence"` with a documented supersession chain: `ea89338f…` (lineno 83, FAIL — confounded filter-dependent-t run) → `31509f0c…` (lineno 87, PASS — t-anchor well-posedness fix; Results §5) → `dc796fb8…` (CANONICAL LATEST, PASS — numerically-identical re-emission after the inline-write → named `append_verdict()` refactor). Each successor carries a `supersedes=` companion row naming its immediate predecessor. Downstream consumers cite `dc796fb8…`. sig_5 CLEAN: no two canonical verdict lines share an audit_sha256.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; one-line salient return each):

1. `search_knowledge("VII.AR filter geometry L-infinity box triangular truncation convergence rate Cell IV")` → §VII.AR is the Stage-2 rank-ordering verify (algebra-INVARIANT family); §VII.AP is the Cell-IV s=4 GGE-Bog-occ-variance theorem (`Var_a=-7.046336`); the cache-moment Var_a trajectory is the relevant convergence observable. NOT-CLOSED (no prior filter-geometry generalization gate).
2. `search_knowledge("w5b47_raw Weyl law d=4 tail box filter substrate-natural truncation geometry W4-6")` → `Var_a_canonical --derived_from--> S92` provenance: `convention=w5b47_raw (max(p,q)…`; DEPRECATED `Var_a_canonical_diagnostic_vdd` self-labels "vdd p+q<=L_max convention; triangular under-sampling of d=4 Weyl-law tail"; S92 W4 WP: `Var_a(L10,w5b47)=7.2825e-06 → Var_a(L12)=7.1813e-06 (Δ=−1.389%)`.
3. `trace_entity("VII.U.2 Cell IV algebra-INVARIANT spectrum-only functional observables")` → no trace hit (resolved by direct registry read of §VII.U.2 four-corner table, lines 12966-13235; §VII.AR block lines 17339-17396).
4. `get_constant("Var_a_canonical")` → `7.282490225e-06` (S92, source `s92_w4_6_w4_4_empirical_anchor_reconciliation.npz`, gate `S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION`, **NOT superseded**); note "max(p,q)<=L_max filter; m_a=dim_pq; zero-modes excluded". → ADOPTED as the box-filter reconstruction cross-check anchor.
5. `get_constant("Var_a_canonical_diagnostic_vdd")` → `4.7650356226e-05` (**SUPERSEDED=True**); note "DIAGNOSTIC: vdd p+q<=L_max convention; triangular under-sampling of d=4 Weyl-law tail." → confirms triangular = vdd = under-sampling; box is the substrate-natural canonical.

PRE-CLOSED status: NOT pre-closed. §W4-6 established the box-vs-triangular ordering on ONE observable (Var_a); this gate tests whether it GENERALIZES across the algebra-INVARIANT spectrum-only functional family — a new set-universal question. The §W4-6 PASS prereq (`S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION`, audit `e393b51f…`) is verified PRESENT in the S92 verdict file at runtime (`w4_6_prereq_present=True`).

**Verdict**: **PASS** — set-universal: ALL 6 Cell-IV algebra-INVARIANT spectrum-only-functional observables exhibit the L∞-box < triangular convergence-rate ordering. `boundary_observable=none`; no filter-geometry sub-axis needed.

**Results**:

*Naming reconciliation (recorded up front).* The gate text says "Cell IV algebra-INVARIANT spectrum-only-functional observables." Per `permanent-results-registry.md §VII.U.2` four-corner table, the strict roman cells label the algebra-axis × Mellin-pole cross-product: Cells I/II are algebra-INVARIANT (s=3 / s=4), Cells III/IV are algebra-DEPENDENT (s=3 / s=4). §VII.AR's own algebra-axis classification is **algebra-INVARIANT spectrum-only family** (registry line 17354: "Cell I or biaxial-FI-LEVEL-DRESSED hybrid"). The audit's operational content is unambiguous and is what the plan pins: the **w5b47_raw convention** (`collect_truncated_spectrum`, `max(p,q)≤L_max`) applied to the **algebra-INVARIANT spectrum-only functional family** `F = Σ_k m_k g(λ_k)` (§VII.U.2 clause (a): Seeley-DeWitt moments, ζ-residues `Tr(D^{−2s})`, Mellin-Dirichlet identities, heat-kernel zeta-traces, and the moment-aggregated Var_a class). "Cell IV" in the gate text is the plan-author shorthand for the §VII.AR-associated cell (the rank-ordering observable's home); the audited family is the spectrum-only functionals the §W4-6 w5b47_raw finding anchored on. All 6 observables satisfy the clause-(e) parse-tree test (only `λ_a, m_a, Δ_BCS`; no `π(a)`, no `[D,π(a)]`, no state-pair sup).

**(1) Observable family** (6 algebra-INVARIANT spectrum-only functionals, all `Σ_k m_k g(λ_k)`):

| # | Observable | g(λ) | family role |
|:--|:-----------|:-----|:------------|
| 1 | `Var_a` | `M2−M1²`, `n_a=Δ²/(2(λ²+Δ²))` | §W4-6 anchor; 2nd-moment Bogoliubov occupation (s=4 dominant) |
| 2 | `mean_n` | `M1=⟨n_a⟩` | 1st-moment Bogoliubov occupation |
| 3 | `M_s4` | `⟨λ⁻⁴⟩` | substrate-distance-2 Mellin moment s=4 |
| 4 | `M_s6` | `⟨λ⁻⁶⟩` | substrate-distance-3 Mellin moment s=6 (low-(p,q)-dominated) |
| 5 | `Var_n2` | `⟨n⁴⟩−⟨n²⟩²` | k=2 higher-moment variance (distinct F_traj level-factor) |
| 6 | `HK_trace` | `⟨e^{−t λ²}⟩`, `t=3.405429e-02` | heat-kernel zeta-trace (t FILTER-INDEPENDENT, pinned to L=12 ref max(λ²)) |

**(2) Sector-admission counts** (the substitution-chain mechanism, Steps 1-4): box `max(p,q)≤L` admits the high-(p,q) corner sectors the triangle `p+q≤L` excludes:

| L_max | N_box | N_tri | N_box/N_tri | box-only corner sectors |
|:------|:------|:------|:------------|:------------------------|
| 6 | 48 | 28 | 1.714 | 20 |
| 8 | 70 | 44 | 1.591 | 26 |
| 10 | 84 | 65 | 1.292 | 19 |
| 12 | 90 | 90 | 1.000 | 0 |

The cache (`s84_spectrum_cache_L12_tau019.npz`) is `p+q≤12` triangle-populated (90 sectors, no `p+q>12`), so at L_max=12 box and triangle coincide (both 90) → the **L=12 value is the shared reference** for both filters; `ref_box==ref_tri@L12=True` for all 6 observables. The convergence-rate audit measures how fast each filter reaches this shared reference as L grows 6→8→10→12.

**(3) Per-observable convergence rates** (α = log-log decay slope of residual `R(L)=|F(L)−F(12)|/|F(12)|` over L∈{6,8,10}; `R_tri/R_box@L10` = residual-advantage ratio at canonical sub-reference L=10; >1 ⇒ box faster):

| Observable | α_box | α_tri | R_box(10) | R_tri(10) | R_tri/R_box@10 | ordering box<tri |
|:-----------|:------|:------|:----------|:----------|:---------------|:-----------------|
| Var_a | 8.188 | 3.860 | 1.41e-02 | 7.66e-01 | **54.36** | ✓ |
| mean_n | 5.714 | 3.218 | 1.20e-02 | 3.28e-01 | **27.42** | ✓ |
| M_s4 | 6.250 | 4.205 | 2.33e-02 | 7.89e-01 | **33.81** | ✓ |
| M_s6 | 6.810 | 5.203 | 3.34e-02 | 1.38e+00 | **41.26** | ✓ |
| Var_n2 | 7.542 | 5.502 | 3.63e-02 | 1.76e+00 | **48.46** | ✓ |
| HK_trace | 5.066 | 2.039 | 6.69e-03 | 1.39e-01 | **20.72** | ✓ |

For every observable, α_box > α_tri (box residual decays faster) AND R_box(10) < R_tri(10) (box residual smaller at the canonical sub-reference). `set_universal_PASS=True`, `n_satisfied=6/6`, `boundary_observable=none`, `borderline=none`.

**(4) Cross-check (w5b47_raw reconstruction validation)**: box-filtered `Var_a` at L_max=10 = **7.2824902250e-06**, reproducing the knowledge-MCP canonical `Var_a_canonical = 7.282490225e-06` (NOT superseded) to rel_diff **6.3e-12**. This validates that the `collect_truncated_spectrum` reconstruction (verbatim w5b47_raw convention from `s88_w5b_corner_iv_level2_envelope.py:142-158`) is faithful to the §W4-6 pipeline at machine precision.

**(5) In-session well-posedness correction (honest disclosure per `v3-closure-recovery.md` Class-1 boundary; NOT iterate-until-PASS).** The FIRST run (audit `ea89338f…`, RETAINED on disk per absolute verdict permanence, superseded) returned FAIL with `HK_trace` as boundary observable (R_tri/R_box@10=0.25, i.e. triangle apparently faster). Investigation found the cause: the heat-kernel anchor was `t = 1/max(λ²)` of **this filter's admitted spectrum** — which differs between box and triangle (at L=6: `t_box=0.0376` vs `t_tri=0.0992`, 2.6× apart; the box admits the high-(p,q) corner sectors so its `max(λ²)` is larger). A filter-dependent `t` makes box and triangle evaluate **structurally different functionals**, a confound that violates the same-observable-two-filters requirement for fair convergence-rate comparison (`phononic-framing.md §"Same-functional-different-scale fair-comparison"` + `cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural filter"`: the (observable, scale) pair must be FIXED on both sides first). The correction pins `t_anchor=3.405429e-02` to the L=12 reference `max(λ²)` (FILTER-INDEPENDENT, identical for box and triangle), making `HK_trace` the SAME functional under both filters; it then satisfies the ordering (R_tri/R_box@10=20.72) consistently with the other 5. The convention/threshold/scheme were UNCHANGED — only an ill-posed observable construction was corrected; this is in-session self-correction (`agent-standards.md §"Self-correct immediately"`), not convention-shopping (Class 1) nor iterate-until-PASS (Class 6).

**(6) Substitution chain** (the "box converges FASTER" direction claim; per `math-scripts.md §"Double-Check Logic Before Compute"`):
- **Step 1**: `N_box(L) = #{(p,q): max(p,q)≤L} = (L+1)²` [L∞-box admission count].
- **Step 2**: `N_tri(L) = #{(p,q): p+q≤L} = (L+1)(L+2)/2` [triangular admission count].
- **Step 3**: `N_box/N_tri = 2(L+1)/(L+2) → 2` as `L→∞` [box admits ~2× the sectors; verified empirically 1.714→1.591→1.292→1.000 on the L_max=12-truncated cache, where the ratio→1 at L=12 because the cache support IS the triangle itself].
- **Step 4**: at the d=4 Weyl-law tail `dN(λ) ~ λ³ dλ`, the high-(p,q) corner sectors (large p / small q and vice versa) carry the dominant residual spectral weight; the box admits exactly these corner sectors that the triangle EXCLUDES (20-26 box-only corner sectors at L=6,8) ⇒ the box-filtered observable captures more of the continuum tail at fixed L.
- **Step 5**: ⇒ for a convergent algebra-INVARIANT functional `F = Σ_k m_k g(λ_k)`, the box-filtered truncation residual decays FASTER (box reaches the L=12 reference at smaller L) ⇒ `rate_box > rate_tri`. Read off the canonical form: α_box > α_tri AND R_box < R_tri at every L<12, for all 6 observables.
- **Conclusion**: the §W4-6 w5b47_raw finding (L∞-box substrate-natural) GENERALIZES across the Cell-IV algebra-INVARIANT spectrum-only functional family. No observable BREAKS the ordering once each is well-posed as the same functional under both filters.

**(7) 4-tuple**: `(value=set_universal_PASS=True, scheme=FW, convention=VII-AR-Cell-IV-Linf-box-vs-triangular-filter-geometry-w5b47_raw, L_max=12)` (reference L_max=12; scan L_max∈{6,8,10,12}).

**(8) dual-SHA** (canonical latest): `audit_sha256=dc796fb8b991715e3c3bd2c489b8903152adb1b4083c927df78528806182a4fa`, `content_sha256=0104a65814090d9a18e1520969579efe3e8c96f8b6e512648e1d1765b0b17c35` (closure over input-pin map: script + canonical_constants + s84 cache `9e6d9cf7…` + w5b envelope script; content over script bytes). [VERIFY] trigger, no [SIGN] 3-tuple (set-universal ordering verdict, not a sign/direction claim) — matches gate-block `schema_v2_3tuple_required: false`. (Supersession chain `ea89338f → 31509f0c → dc796fb8` per Results §5 + the Output-Artifacts verdict-line note; the two prior emissions are retained on disk per absolute verdict permanence.)

**Solution-space interpretation**: The PASS strengthens the §VII.U.2 Cell-IV truncation-geometry coherence: the L∞-box (`max(p,q)≤L_max`) truncation geometry is **substrate-natural uniformly** across the algebra-INVARIANT spectrum-only functional family, not just for the single Var_a observable the §W4-6 finding anchored on. This closes the corridor in which Cell IV would have to be sub-classified by a filter-geometry sub-axis (the FAIL_meaning branch) — no such sub-axis is needed. The filter-geometry is orthogonal to the algebra-axis (it acts on which (p,q) sectors are sampled, not on the algebra-dependence of the functional), per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`; a uniform box advantage confirms the truncation geometry is a Cell-IV-invariant substrate-natural property. Structurally: the substrate IS the finite spectral triple; the box filter samples the substrate's spectral content (admitting the d=4 Weyl-tail corner sectors earlier) in the way that reaches the continuum `L_max→∞` image fastest — D_K eigenvalues on the admitted (p,q) sectors → algebra-INVARIANT spectrum-only functional → continuum image. The downstream consumer (Var_a Stage-1-CANDIDATE Level-2 envelope, §VII.U.2 Corner II) inherits the box convention as the substrate-natural truncation geometry with set-universal backing. One forward note for S94+: the L_max∈[35,100] asymptotic-α extraction infra (CF-S94-W5-3) would sharpen the per-observable α values beyond the 4-point {6,8,10,12} mesh, but is not needed for the set-universal ordering verdict (which is decisive at every finite L<12).

---

### §W5-5. S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **NON-PHONONIC** (METHODOLOGY-class registry-write; PASS predicate is artifact-existence-with-substantive-content, not a numerical comparison)
**Agent**: `mack-cosmic-bridge` (sole writer for §VII registry entries per `feedback_mack-bridge-role.md`)
**Hypothesis**: The §VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM has completed the `joint-theorem-promotion.md` 4-stage pathway (Stage-2 composite PASS-AND across both axes + S91 W2 Axis-A inherited PASS) and is eligible for the STAGE-1-CANDIDATE → STAGE-3-PERMANENT tag-flip — the framework's THIRD cross-axis joint theorem to reach STAGE-3-PERMANENT.
**Plan reference**: `sessions/session-plan/session-93-plan-w5.md` §W5-5 (heading resolved at runtime to **line 18367**, Status to **line 18375**, index-table row to **line 133** — all via heading-anchor grep on the title keyword `SUBSTRATE-CLOCK-UNIQUENESS-THEOREM`, NOT the stale plan-pinned ~18365/18373/~18213-18289, per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction).

**Branch resolved**: **(a) — VERIFICATION-ONLY CONFIRMATION** (the target ALREADY reads STAGE-3-PERMANENT, an S92 in-session promotion dated 2026-05-24, dropped-then-effected per `CLAUDE.md §"No Technical Debt"`). NO duplicate flip; NO rewrite of the already-correct registry body Status; NO forced PASS. The only registry-class write is the W0-1 lockfile STAGE-3-PERMANENT-CONFIRMED row.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **Script** — `computations/_shared/s93_w5_5_vii_aw_op_proj_stage_3_permanent_promotion.py` (39864 bytes). `must_contain` grep:
  - `from canonical_constants import` → 3 occurrences (PASS; per `computations/_shared/CLAUDE.md` ALL scripts import canonical_constants — `import *` + `M_KK, tau_fold` metadata-only).
  - `append_verdict` → 2 occurrences (PASS; `def append_verdict(...)` + the call site).
- **Data** — `computations/session-93/s93_w5_5_vii_aw_op_proj_stage_3_permanent_promotion.npz` (15937 bytes; OPTIONAL per METHODOLOGY-class, emitted anyway with the full verification flag-set + cited Stage-2 chain SHAs) + JSON sidecar (5132 bytes).
- **Plot** — `computations/session-93/s93_w5_5_vii_aw_op_proj_stage_3_permanent_promotion.png` (61001 bytes; OPTIONAL, emitted: 6-predicate artifact-existence bar chart).
- **Verdict line** — `computations/session-93/s93_gate_verdicts.txt`; matches `^S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION:.* audit_sha256=[a-f0-9]{64}` (PASS) + dual-SHA companion row present. `audit_sha256=c118e75929bd438d06542e33b5cb34ffcde7cdb83741679a78e215958c628708` (UNIQUE — grep count = 1, no sig_5 duplicate); `content_sha256=47c9e0f24e4afe170d3b6abefe49e7110a61c9ac52c2d7843a4376d6847975d5` (over the verified §VII.AW SUBSTRATE-CLOCK entry block).
- **Registry §VII.AW.OP-PROJ SUBSTRATE-CLOCK entry** — VERIFIED on-disk at STAGE-3-PERMANENT: body Status (line 18375) `STAGE-3-PERMANENT (promoted from STAGE-1-CANDIDATE 2026-05-24 ...)` + index-table row (line 133) `THM **[STAGE-3-PERMANENT 2026-05-24 — Stage-2 PASS-AND complete; ...]**`; Stage-2 PASS-AND chain cited (Axis-A `69df5fa7…` + Axis-B `4bd3017e…` supersedes S91 W2 Axis-B INFO `0db7c3c0…`; JOINT (a)+(c)+(e) PASS-AND'd); Cell I + 5-anatomy + 3-level ladder + 5-criteria saturation table + theorem statement all present (invariance preserved). NOT re-written by this gate (branch (a)).
- **Lockfile STAGE-3 row** — `sessions/framework/s93-slot-pre-allocation-lockfile.md` updates table appended (append-only single `open("a")`): `| 2026-05-24 | S93 W5-5 STAGE-3-PERMANENT CONFIRMED on-disk ... | §VII.AW.OP-PROJ | STAGE-3-PERMANENT-CONFIRMED |`. **Drift correction**: plan §W5-5 input_files pins `s90-slot-pre-allocation-lockfile.md` (STALE plan-frozen); the canonical W0-1 home is `s93-slot-pre-allocation-lockfile.md` (it pre-allocates the 7 S93 STAGE-3 flips INCLUDING `RESERVED-FOR-S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION` at its lines 21-29) per `substrate-first-canonical-sourcing.md §(ii.B)`; documented in the verdict `value=` field.
- **Slot-allocation audit** — `_vii_slot_allocation_audit.py` → **VERDICT: PASS** (118 table entries = 118 registry headers; taxonomy `{A_REGISTERED_AND_MATCHED: 4, B:0, C_COLLISION:0, D_ORPHANED:0, E_DRIFT:0, F_STALE:0}` — zero collisions / zero stale-status introduced by the lockfile append).
- **M4 allowlist append** — **ORCHESTRATOR-ONLY** (W5-5 IS in the index allowlist set per the spawn prompt; mack does NOT edit `methodology-wave-allowlist-ledger.md` — flagged here for the orchestrator per `methodology-wave-allowlist.md §"Edit discipline"`).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries run BEFORE writing the script):

- `search_knowledge("SUBSTRATE-CLOCK-UNIQUENESS §VII.AW STAGE-3-PERMANENT")` → returned the S90 W2 CF-19 STAGE-1-CANDIDATE landing gate (`S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING`, 16/19 checks, 5/5 saturation) + the `w4_4_vii_aw_op_form_retrofit` provenance (S92 OE-form retrofit). The knowledge index is one rebuild behind (reflects the STAGE-1 landing, NOT yet the S92 STAGE-3 flip) — consistent with the on-disk registry being AHEAD of the index; NOT a PRE-CLOSED conflict (the gate is a verification-confirmation, not a recompute of a closed result).
- `trace_entity("substrate-clock uniqueness")` → evidence chain: theorem (STAGE-1-CANDIDATE registration), gate (S90 landing), provenance (`s90_w2_vii_next_substrate_clock_uniqueness_theorem_stage_1_landing.py`). Confirms the substrate derivation (S89 W3-6 5/5 saturation) + the 4-stage pathway lineage; no contradicting closure.
- **Salient cross-finding (NOT a direct query target)**: the on-disk registry shows the §VII.AU.OP-PROJ entries (lines 18794/18905) ALSO claim a THIRD-position STAGE-3 via "STAGE-3 promotion S93 W2-2" — confirming the AU/AW '#3' ordinal collision flagged in the spawn prompt (handled below, recorded NOT renumbered).

**Verdict**: **PASS** — branch (a) verification-confirmation. The §VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM carries STAGE-3-PERMANENT on-disk (body Status line 18375 + index-table row line 133) with the Stage-2 PASS-AND audit_sha chain cited and well-formed, Cell-I + 5-anatomy + 3-level + parse-tree-relevant saturation-table invariance preserved, the Stage-2 chain verbatim in its source verdict files (S91 W2 Axis-A `69df5fa7…` PASS; S92 W4 Axis-B `4bd3017e…` PASS), the slot RESERVED in the s93 W0-1 lockfile, and the STAGE-3-PERMANENT-CONFIRMED row recorded. No duplicate flip; no forced PASS; no re-write of the already-correct Status. (Per `math-scripts.md §"All Results Are Good Results"`, a FAIL here would have meant the on-disk chain/invariance was incomplete — it is not.)

**Results**:

- **Branch resolution**: branch **(a)** — the target was ALREADY STAGE-3-PERMANENT at dispatch (S92 in-session promotion, 2026-05-24), so this gate is a VERIFICATION-ONLY confirmation, NOT a tag-flip. Six artifact-existence predicates all PASS: (1) body+index STAGE-3-PERMANENT present; (2) Cell-I + 5-anatomy + 3-level + theorem + 5-criteria saturation-table invariance preserved; (3) Stage-2 PASS-AND chain cited in the body Status; (4) Stage-2 chain verbatim in source verdict files; (5) slot RESERVED in the s93 lockfile; (6) lockfile STAGE-3-PERMANENT-CONFIRMED row recorded.
- **STAGE-3-PERMANENT tag state**: body Status (line 18375) = `STAGE-3-PERMANENT (promoted from STAGE-1-CANDIDATE 2026-05-24 per joint-theorem-promotion.md §"Stage 3" 4-stage pathway)`; index-table row (line 133) = `THM **[STAGE-3-PERMANENT 2026-05-24 — Stage-2 PASS-AND complete; promoted per joint-theorem-promotion.md §"Stage 3"]**`. Both already present; no edit applied.
- **Stage-2 PASS-AND chain (verified, not re-derived)**: Axis-A PASS via hawking-theorist (S91 W2 `S91-W2-VII-AW-OP-PROJ-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-A`, audit_sha256=`69df5fa7e23fa08fd038a629f6822d0e839a5566dd76ad6cf34246ce89a7831f`, clauses (a,c,e)); Axis-B INFO→PASS via mack-cosmic-bridge on the cosmological-bridge axis (S92 W4 `S92-W4-CF-S92-W4-3-RE-DISPATCH-VII-AW-OP-PROJ-STAGE-2-AXIS-B`, audit_sha256=`4bd3017ed24e1570573ee55df1528020632a7fd348d5f24de7fd00a7f8ccae7c`, supersedes S91 W2 Axis-B INFO `0db7c3c0…`, clauses (b,d,f)). JOINT clauses (a)+(c)+(e) PASS-AND'd across both verdicts. Substrate derivation: S89 W3-6 `S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION` PASS (`6108fd56…`; 5/5 saturation `{P_1:5, P_2:4, P_3:2}`).
- **Substrate-input-orthogonality**: at the STRUCTURAL CEILING (cache-axis ∧ registry-text-axis), K=3→K=4 advance-eligible per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` — present in the body Status, verified.
- **Cell I + 5-anatomy + 3-level + parse-tree invariance**: Cell I (algebra-INVARIANT spectrum-only-functional × Mellin-pole substrate-distance-1 at s=3); substrate-clock Pinning-A = `∫_λ g(λ) dN_{D_K}(λ)` on D_K's Peter-Weyl decomposition at τ_fold=0.19; Level-3 anchor `xi_KZ_FW = 0.018760052113614718 M_KK⁻¹` within the `L^{-3}` Level-2-binding envelope at L_max=10. All preserved (not modified).
- **THIRD STAGE-3-PERMANENT membership**: §VII.AW.OP-PROJ JOINS the STAGE-3-PERMANENT cross-axis joint-theorem set {§VII.AH (FIRST, S90 W2 CF-20), §VII.U.2 Corner-II Var_a (SECOND, S92 W4-7), §VII.AW.OP-PROJ (this; S92 in-session), §VII.AU.OP-PROJ (S93 W2-2), §VII.AV.STATE-PROJ (S93 W3-6), §VII.AX.OP-PROJ, §VII.AY.OP-PROJ (S93 W5-2)}. Set MEMBERSHIP recorded; the precise integer ordinal is **NOT asserted** (see AU/AW chronology below) — the same discipline the W5-2 sibling adopted.
- **AU/AW ordinal chronology (recorded, NOT unilaterally renumbered)**: §VII.AW.OP-PROJ reached STAGE-3-PERMANENT in **S92 (2026-05-24)**, CHRONOLOGICALLY BEFORE §VII.AU.OP-PROJ's **S93 W2-2** promotion. Both currently claim a "THIRD STAGE-3-PERMANENT" ordinal (an on-disk collision, detected = True). The S92-before-S93 chronology means **§VII.AW is the EARLIER STAGE-3 promotion** — the chronological fact is recorded here, but the full ordinal-renumbering of all entries is left to the session-end resolution **`CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW`** (no unilateral re-numbering in this §VII.AW-only verification gate).
- **STAGE-3 flip recorded in lockfile per W0-1**: `sessions/framework/s93-slot-pre-allocation-lockfile.md` updates table — STAGE-3-PERMANENT-CONFIRMED row appended (append-only). Drift correction documented (plan-pinned `s90-...` is stale; canonical home is `s93-...`).
- **4-tuple**: (value=`VII-AW-OP-PROJ-SUBSTRATE-CLOCK-STAGE-3-PERMANENT_branch=a_verification_confirmation…`, scheme=`registry-text-METHODOLOGY-class`, convention=`VII-AW-OP-PROJ-SUBSTRATE-CLOCK-STAGE-3-PERMANENT-tag-flip-THIRD`, L_max=`N/A`); audit_sha256=`c118e75929bd438d06542e33b5cb34ffcde7cdb83741679a78e215958c628708`, content_sha256=`47c9e0f24e4afe170d3b6abefe49e7110a61c9ac52c2d7843a4376d6847975d5`. Exit code 0 (script health; verdict is DATA per `math-scripts.md §"Exit Codes and Verdict Semantics"`).

---

### §W5-6. S93-W5-6-VII-AW-SLOT-RENAME (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S93-W5-6-VII-AW-SLOT-RENAME`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (METHODOLOGY-class registry-write hygiene; label-collision resolution; artifact-existence + label-uniqueness predicate)
**Agent**: `mack-cosmic-bridge` (sole writer for §VII registry entries per `feedback_mack-bridge-role.md`)
**Hypothesis**: The `§VII.AW.OP-PROJ` label-collision (TWO distinct entries sharing the label: (1) SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [W5-5 STAGE-3 target] and (2) the rejected SU(3)-Coloured-Chirality Spectral Triple [STAGE-0 REJECT]) is resolved by renaming entry (2) to the next-free §VII slot (≥ §VII.BF), leaving §VII.AW.OP-PROJ uniquely attached to entry (1); the rename is label-only (no filename/gate-ID/SHA changes) with all cross-file pointers updated.
**Plan reference**: `sessions/session-plan/session-93-plan-w5.md` §W5-6 (HK-S93-W9-1; entry-(2) heading ~17509, highest slot §VII.BE ~20042 ⇒ next-free §VII.BF; resolve line + next-free letter at runtime via heading-anchor grep + verify-before-write).

**Verdict**: **PASS** — the rejected SU(3)-Coloured-Chirality Spectral Triple entry renamed `§VII.AW.OP-PROJ` → `§VII.BF` (label-only); `§VII.AW.OP-PROJ` now resolves UNIQUELY to SUBSTRATE-CLOCK-UNIQUENESS-THEOREM; all 4 cross-file blast-radius loci updated; slot-allocation audit `VERDICT: PASS` (collision/orphan/drift = 0). 11/11 verification checks PASS; 12/12 rename loci applied cleanly.

**Output Artifacts** (closure-verification checklist; on-disk + `grep` evidence):

- **Script** `computations/_shared/s93_w5_6_vii_aw_slot_rename.py` (53,373 bytes; `ls -la` confirmed). `must_contain` grep:
  - `from canonical_constants import` — line 104 (`from canonical_constants import *`) + line 105 (`from canonical_constants import M_KK, tau_fold`).
  - `append_verdict` — def at line 526; call at line 756.
- **Data** `computations/session-93/s93_w5_6_vii_aw_slot_rename.npz` (10,800 bytes; OPTIONAL for METHODOLOGY-class — emitted anyway with all 11 verification flags + label-uniqueness counts). Plus JSON sidecar `s93_w5_6_vii_aw_slot_rename.json` (5,061 bytes).
- **Plot** `computations/session-93/s93_w5_6_vii_aw_slot_rename.png` (57,530 bytes; OPTIONAL — emitted; 11-bar V1–V11 artifact-existence/label-uniqueness predicate chart).
- **Verdict line** `computations/session-93/s93_gate_verdicts.txt:103` matches `^S93-W5-6-VII-AW-SLOT-RENAME:.* audit_sha256=[a-f0-9]{64}`:
  ```
  S93-W5-6-VII-AW-SLOT-RENAME: PASS -- value='VII-AW-slot-rename_SU3-coloured-chirality_§VII.AW.OP-PROJ→§VII.BF_label-only_...' scheme=registry-text-METHODOLOGY-class convention=VII-AW-slot-rename-label-only-SU3-coloured-chirality-to-next-free-BF L_max=N/A audit_sha256=8b37513ec1e299eb50f9d861b0151f308a9f899e6f5c40a692cc23990663b985 content_sha256=dd38c7822cc1e972789e78e21c805fd043105d3129465a9023b9724fae378c1d schema_version=S84+
  ```
  Dual-SHA companion row at line 104 (`audit_sha256_short=8b37513ec1e299eb content_sha256_short=dd38c7822cc1e972`). audit_sha256 appears EXACTLY ONCE in the file (sig_5 uniqueness preserved; distinct from W5-5's `c118e759…`). `[VERIFY]` — no `[SIGN]` 3-tuple (`schema_v2_3tuple_required: false`).
- **Registry rename** in `sessions/permanent-results-registry.md` (`grep` evidence):
  - `17512: ## §VII.BF — SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11) ... slot renamed §VII.AW.OP-PROJ → §VII.BF at S93 W5-6 ...` (the renamed heading).
  - `18368: ### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM ...` (the KEEP entry, UNTOUCHED).
  - `134: | §VII.BF | THM | SU(3)-Coloured Chirality Spectral Triple ... | mack-cosmic-bridge | 2026-05-24 |` (NEW §VII.BF index row, directly after the SUBSTRATE-CLOCK index row 133).
  - No `## §VII.AW.OP-PROJ — SU(3)-Coloured` heading remains (the rejected entry left the label).
- **WP** this §W5-6 section (Status/Verdict/Output Artifacts/MCP/Results blocks).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the rename script; per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("VII.AW.OP-PROJ slot-label collision SU(3)-Coloured-Chirality SUBSTRATE-CLOCK-UNIQUENESS")` → returned the KEEP gate `S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING` (slot_allocation=VII.AW.OP-PROJ) AND the REJECT gate `S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED` (FAIL; scheme=SU(3)-coloured-chirality); plus the `scan_slot_occupancy(registry_text, slot_label)` all-header-levels pattern from `s88_w4a_split_registry_writer.py` (re-used as `scan_slot_occupied`).
- `search_knowledge("SU(3)-Coloured Chirality Spectral Triple REJECTED STAGE-0 candidate S92 W9-4 chirality FAIL")` → returned `s92_w9_4_vii_at_vii_aw_op_proj_fail_diagnostic_landing` (the STAGE-0 REJECT FAIL-diagnostic landing) + `S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE` (the rejected entry's gate-ID, PRESERVED label-only).
- `trace_entity("SUBSTRATE-CLOCK-UNIQUENESS-THEOREM")` → PROVEN theorem; gate `S90-VII-NEXT-…-STAGE-1-CANDIDATE-LANDING`; provenance `s90_w2_…stage_1_landing.py` (STAGE-1, CF-19). Confirms the KEEP entry.
- `trace_entity("SU(3)-coloured chirality")` → gate `S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED` (n_axiom_pass=6/7; KO_dim_coloured=6; ax5_dp_pass=False; level_2=non-binding). Confirms the REJECT entry is structurally distinct.
- `trace_entity("VII.AW slot-label collision")` → No trace found (collision is a registry-text artifact, not a knowledge-graph entity; no closure covers the gate). NOT PRE-CLOSED → gate proceeds.

**Results**:

- **Rename executed**: rejected entry `§VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11)` [S90 W7 CF-45; STAGE-0-CANDIDATE REJECTED at S91 W7-2b — axiom-5'' FAIL residual 3.274, KO-dim stays 6, level_2=non-binding] renamed to `§VII.BF`. Target chosen by verify-before-write: highest slot at plan-freeze = §VII.BE; runtime scan confirmed §VII.BF + §VII.BG both GENUINELY FREE (`bf_occupied=False`, `bg_occupied=False`) → target `§VII.BF`.
- **Label-uniqueness confirmed**: post-rename `## §VII.AW.OP-PROJ —` (rejected-entry level-2 heading form) count = **0**; `### §VII.AW.OP-PROJ —` (SUBSTRATE-CLOCK level-3 heading form) count = **1**. `§VII.AW.OP-PROJ` now resolves UNIQUELY to SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (the W5-5 STAGE-3-PERMANENT entry, untouched).
- **All 4 cross-file blast-radius loci updated (HK-S93-W9-1)**:
  - **(i)** `permanent-results-registry.md` — entry-(2) heading + 5 in-block self-refs (slot-label note rewritten to COLLISION RESOLVED; slot-allocation provenance annotated with the rename; substrate-framing ×2 self-refs → §VII.BF; Element-4 NON-BINDING self-ref → §VII.BF) + entry-(1) SUBSTRATE-CLOCK slot-label note rewritten to COLLISION RESOLVED (cross-pointer now to `## §VII.BF`) + index-table row 133 annotation updated (`[LABEL COLLISION RESOLVED S93 W5-6 …]`) + NEW §VII.BF index row inserted at line 134.
  - **(ii)** `permanent-results-registry.md` §VII.AT.OP-PROJ sibling pointers ×2 (Cross-link block + FAIL-diagnostic Cross-links) → `§VII.BF` (both with "renamed from §VII.AW.OP-PROJ at S93 W5-6" annotation; no dangling `§VII.AW.OP-PROJ` sibling refs remain).
  - **(iii)** `sessions/framework/s90-slot-pre-allocation-lockfile.md` — RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW Slot field annotated `→ RENAMED §VII.BF at S93 W5-6 … SUPERSEDED-BY-RENAME` (line 24) + updates-table rename row appended (line 43: `§VII.AW.OP-PROJ → §VII.BF | RENAMED (SUPERSEDES the W7-CF-45-VII-AW RESERVED allocation)`).
  - **(iv)** this WP §W5-6 section (rename + resolved collision documented).
- **Label-only confirmed (V11)**: filenames, gate-ID (`S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE`), audit-SHAs (`be8006d6…` / `9ae27d0e…`), and the coloured-chirality content (γ_F^c, Connes-Marcolli 2008 §11, axiom-5'' FAIL, S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED) UNCHANGED in the renamed §VII.BF block (1,527 words; content_sha256=`dd38c7822cc1e972…` over the renamed block). Only the §VII slot label moved.
- **Slot-allocation audit** `_vii_slot_allocation_audit.py` → `VERDICT: PASS` (119 table entries = 119 registry headers; taxonomy: A_REGISTERED_AND_MATCHED=4, C_COLLISION_DOUBLE_RESERVATION=**0**, D_ORPHANED_TABLE_ENTRY=**0**, E_REGISTRY_VS_TABLE_DRIFT=**0**, F_STALE_STATUS=0). The rename introduces no collision/orphan/drift; the §VII.BF index row + renamed header are balanced.
- **Drift correction documented** (`substrate-first-canonical-sourcing.md §(ii.B)`): all edits CONTENT-ANCHORED on exact substrings, NOT plan-pinned line numbers (the plan-pinned ~17509/~17472/~17503/~18367 are STALE-drifted +2 lines, e.g., the rename-target heading was at line 17511, not 17509). Recorded in the verdict-line `value=` field.
- **Out-of-blast-radius, correctly UNCHANGED** (fidelity-verified): (a) registry precedent-citations of §VII.AW.OP-PROJ (~18502/19341/19343/19432) cite the SUBSTRATE-CLOCK / mack-sole-writer precedent → entry (1) which KEEPS the label; (b) `s93-slot-pre-allocation-lockfile.md` line ~29 anchor-list explicitly names "§VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM" → entry (1); (c) `methodology-wave-instances.md` historical ledger rows record the S90 W7 CF-45 LANDING event (append-only past-record of what gate-ID landed, NOT a live slot pointer — renaming would falsify the historical record).
- **Separate-issue note**: the PRE-EXISTING AU/AW "THIRD STAGE-3-PERMANENT" **ordinal** collision (both §VII.AU.OP-PROJ and §VII.AW.OP-PROJ claim "THIRD", flagged `CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW`) is DISTINCT from this SLOT-LABEL collision and is UNAFFECTED by this rename. This gate resolves the slot-label collision only.
- **M4 allowlist append = ORCHESTRATOR-ONLY** (flagged per the recursion-attack closure of `methodology-wave-allowlist.md`): gate-ID `S93-W5-6-VII-AW-SLOT-RENAME` is in the W5-6 index allowlist set; the orchestrator appends it to `methodology-wave-allowlist-ledger.md` — subagents (this writer) are edit-denied on the ledger. **PLAN-FREEZE FLAG for the orchestrator: append `S93-W5-6-VII-AW-SLOT-RENAME` to the M4 allowlist ledger.**
- 4-tuple: `(value=<rename summary>, scheme=registry-text-METHODOLOGY-class, convention=VII-AW-slot-rename-label-only-SU3-coloured-chirality-to-next-free-BF, L_max=N/A)`; `audit_sha256=8b37513ec1e299eb50f9d861b0151f308a9f899e6f5c40a692cc23990663b985`; `content_sha256=dd38c7822cc1e972789e78e21c805fd043105d3129465a9023b9724fae378c1d`.

---

## Wave 5 Synthesis (team-lead)

Wave 5 was a close-out wave on the Pillar-III/IV cohomology + registry-hygiene thread: it arbitrated one historiographic dispute, convicted one SCHEMATIC artifact, confirmed one filter-geometry coherence, and resolved two §VII.AW registry collisions. **6 gates: 5 PASS, 1 FAIL.** No corridor was left open by design; the single FAIL (W5-3) is informative — it closes the asymmetric-coupling PASS-A pathway as a substrate-IS realization of §VII.AR.

**The §VII.AY arbitration close (W5-1 → W5-2).** W5-1 recomputed the Pillar-III HP¹ cocycle ratio `‖φ_67‖/‖φ_88‖` substrate-first from the raw M₃(ℂ) Gell-Mann/Cartan frame norms, giving `R_machine = 7.3249917525961665` (= `Fraction(8814961,1203409)`, full float64). This arbitrated the S92 W7 F1-vs-F2 historiography decisively in favour of **F2** (Sage-QQ reconstruction): F2's published 6sf `7.324992` carried R's true 6th digit; F1 = `7.324974` lost it to **double-rounding** and is a methodology-floor F-image, not the substrate value. They agree only at the 5sf floor `7.3250`. With the substrate arbiter pinned, W5-2 re-ran the §VII.AY.OP-PROJ Element-5 Stage-2 at `rel_tol=1e-5` RELATIVE (necessitated by the 5sf-floor agreement) across three axes — Axis-A vdd F1-img (`Δ_rel=2.37e-6`), Axis-B cross-pillar spectral-geometer F2-img (`Δ_rel=3.38e-8`), Axis-B-primary mack re-test (`Δ_rel=2.37e-6`) — PASS-AND, flipping §VII.AY.OP-PROJ STAGE-1-CANDIDATE → **STAGE-3-PERMANENT** and resolving the corpus §21.0 R2 `DEFERRED-to-R_machine-recompute` tag to `F2-faithful`.

**The §VII.AR FULL-tier conviction (W5-3) + Cell IV coherence (W5-4).** W5-3 ran the genuine FULL-tier Connes-Chamseddine 1996 §2.2-2.3 N=4 Pauli-Villars tower (`c_j=[1,-4,6,-4,1]`, Λ_UV=M_KK) and found the §W4-1 (S92) PASS-A deep-IR rank-flip `[0,0,0,0,1]` does NOT survive the SCHEMATIC→FULL transition (FULL-tier restructures at all five anchors `[1,1,1,1,1]`; Spearman flips sign `ρ_S: −0.20→+0.20`, `abs_diff=0.40 ≫ 1e-3`). The pre-registered dual-prior resolved to **Track B (posterior 0.90)**: the flip was a SCHEMATIC `M_PV²`-scalar-prefactor artifact (the `{0.90,0.95,0.80,0.85}` vector), not BdG physics. PASS-A reclassifies METHODOLOGY-floor-only; §VII.AR STAGE-3 eligibility narrows to **PASS-B alone** (`A_5_extended−ζ`, `ρ_S_FULL=1.0`). W5-4 independently confirmed the Cell IV filter-geometry coherence: after a well-posedness fix (a filter-INDEPENDENT heat-kernel anchor — the run-1 FAIL used a filter-DEPENDENT `t`, making box and triangle different functionals), all 6 observables satisfy the L∞-box < triangular convergence-rate ordering (6/6).

**The two §VII.AW registry-write moves (W5-5 + W5-6).** W5-5 verified (branch-(a), NO duplicate flip) that §VII.AW.OP-PROJ (SUBSTRATE-CLOCK-UNIQUENESS) was already STAGE-3-PERMANENT from S92, recording its set-membership and correcting a lockfile drift (s90→s93). W5-6 resolved a distinct SLOT-LABEL collision: a second entry also carried §VII.AW — the SU(3)-Coloured-Chirality entry — renamed (label-only, content byte-preserved) to the next free letter **§VII.BF** across 4 blast-radius loci, leaving §VII.AW.OP-PROJ uniquely the substrate-clock theorem.

### What Changed

#### (a) Numerical revisions

- `substrate_cocycle_ratio_67_88`: `7.324992` (6sf F2) → `7.3249917525961665` (full float64 substrate-first `R_machine`); 7th-digit sharpening, F2-faithful branch.
- §VII.AY.OP-PROJ Element-5 tolerance: absolute → `rel_tol=1e-5` RELATIVE (forced by the F1/F2 5sf-floor agreement, `Δ_rel=2.41e-6`).
- §VII.AR Spearman under FULL tier: `ρ_S_SCHEMATIC=−0.20` → `ρ_S_FULL=+0.20` (`abs_diff=0.40`); rank vector `[0,0,0,0,1]` (SCHEMATIC) → `[1,1,1,1,1]` (FULL).
- §VII.AR.Cell-IV HK_trace convergence-rate ratio `R_tri/R_box@L10 = 20.72` (well-posed t-anchor; was the run-1 confound).

#### (b) Structural changes

- §VII.AY.OP-PROJ: STAGE-1-CANDIDATE → **STAGE-3-PERMANENT** (Element-3 (iii) K-counter 1→2).
- §VII.AR PASS-A: substrate-IS reading → **METHODOLOGY-floor-only**; STAGE-3 eligibility set `{PASS-A, PASS-B}` → `{PASS-B}` (support narrows from a co-equal both-fold framing to PASS-B alone).
- §VII.AR Element-5: re-scoped from a continuous `(cutoff_frac, M_PV²_frac)` parameter-vector reading to **sub-atlas MEMBERSHIP only** (S-1 V.2 category-conflation closure — future gates cannot cite E5 to cover a continuous-parameter back-solve).
- §VII.AW.OP-PROJ: label-collision resolved — the slot is now uniquely SUBSTRATE-CLOCK-UNIQUENESS; SU(3)-Coloured-Chirality → §VII.BF (new slot allocated).
- F1-vs-F2 historiography: reclassified from "open question" to **arbitrated** (F2 = substrate value; F1 = double-rounding F-image).

### Effected In-Session (NON-MATH — completed before STOP)

- [x] W5-1 canonical re-pin — `substrate_cocycle_ratio_67_88 = 7.3249917525961665` + alias `R_machine_substrate_67_88` (gate-deliverable, W5-1 agent) — `computations/_shared/canonical_constants.py:277-278` + PROVENANCE `:1251`.
- [x] §VII.AY.OP-PROJ STAGE-1→STAGE-3-PERMANENT flip (gate-deliverable, W5-2 agent) — `sessions/permanent-results-registry.md` (index L150 + header + Status); audit `d40041c3…` (supersedes run-1 script-bug FAIL `add62628…` per Option-A).
- [x] §VII.AR PASS-A→METHODOLOGY-floor annotation + E5-scope correction + verdict-permanence note (gate-deliverable, W5-3-CF mack agent) — `sessions/permanent-results-registry.md:17377-17399`; audit `ffa053c8…`.
- [x] §VII.AW.OP-PROJ STAGE-3 verification-confirmation + lockfile drift correction s90→s93 (gate-deliverable, W5-5 agent) — registry + `s93-slot-pre-allocation-lockfile.md`; audit `c118e759…`.
- [x] §VII.AW→§VII.BF label-collision rename, 4 loci (gate-deliverable, W5-6 agent) — `sessions/permanent-results-registry.md`; audit `8b37513e…`.
- [x] M4 allowlist appends (orchestrator-direct) — 4 ledger rows + 4 rationale entries: W5-2 `3dfa2b95…`, W5-5 `40487d9b…`, W5-6 `23e30709…`, W5-3-CF `005f0645…` (anchored to §W5-3 plan block) — `methodology-wave-allowlist-ledger.md:184-186` + `methodology-wave-instances.md`.
- [x] Temp rationale-file cleanup (orchestrator-direct) — 4 `_tmp_rationale_w5_*.txt` removed from `computations/session-93/`.
- [x] sig_5 / supersession-hygiene verification (orchestrator-direct) — W5-4 triple-line (`ea89338f`→`31509f0c`→`dc796fb8`) and W5-2 double-line (`add62628`→`d40041c3`) confirmed clean Option-A chains; all W5 audit_sha256 pairwise distinct.

## Carry-Forward Computations

One genuine math carry-forward (surfaced by §W5-3-CF, line 318). The §VII.AR PASS-A restoration is OPTIONAL (PASS-B already carries §VII.AR STAGE-3 eligibility at `ρ_S_FULL=1.0`), but it is a concrete derivation with a pre-registered gate, so it is captured per `feedback_fix-in-session-never-defer.md`.

### CF-S94-VII-AR-PASS-A-CONTINUOUS-PARAM-SUBSTRATE-DERIVATION — substrate-physics derivation of the PASS-A continuous-parameter pin vector

| Field | Spec |
|:------|:-----|
| **What** | Derive the §VII.AR PASS-A asymmetric-coupling continuous-parameter vector (`cutoff_frac ∈ {0.7,0.5,0.9,1.2}`, `M_PV²_frac ∈ {0.1,0.05,0.2,0.15}`) from first-principles substrate BdG physics (S52 Bogoliubov amplitudes `v_a²=Δ²/(2(λ²+Δ²))` on the M₂(ℂ)⊂A_K sub-algebra), then re-run the FULL-tier N=4 Pauli-Villars rank test (W5-3 machinery) with the substrate-DERIVED params in place of the SCHEMATIC prefactor vector. Tests whether the deep-IR rank-flip `[0,0,0,0,1]` is reproducible from substrate physics (→ PASS-A restored as substrate-IS) or is irreducibly a SCHEMATIC artifact (→ PASS-A permanently methodology-floor-only). |
| **Inputs** | S52 BdG canonical amplitudes (substrate-first, `M_2(ℂ)` sub-algebra); W5-3 FULL-tier machinery (`cc1996_n4_pv_coeffs=[1,-4,6,-4,1]`, Λ_UV=M_KK; `s93_w5_3_vii_ar_full_tier_n4_retry.py`); §VII.AR L_max=12 spectrum cache (`s84_spectrum_cache_L12_tau019.npz`); `substrate_cocycle_ratio_67_88` (canonical). |
| **Gate** | `[SIGN]` — `flip_reproduced` at FULL-tier from substrate-derived params. PASS: rank-flip `[0,0,0,0,1]` reproduced AND `ρ_S_FULL < 0` (deep-IR anti-correlation recovered) ⇒ PASS-A restored as substrate-IS realization, §VII.AR eligibility set re-widens to `{PASS-A, PASS-B}`. FAIL: `[1,1,1,1,1]` persists OR `ρ_S_FULL ≥ 0` ⇒ PASS-A permanently METHODOLOGY-floor; §VII.AR stays on PASS-B alone. Tolerance: `abs_diff(ρ_S) ≤ 1e-3` for flip-match (same band as W5-3). |
| **Effort** | ~0.5–1.0 wave-equivalents (one FULL-tier N=4 PV rank computation with substrate-derived parameter vector; reuses W5-3 machinery). LOW priority — non-blocking (PASS-B carries §VII.AR). |

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-05-24 | §VII.AY.OP-PROJ | STAGE-1-CANDIDATE | **STAGE-3-PERMANENT** | W5-2 3-axis Stage-2 PASS-AND at `rel_tol=1e-5` vs substrate `R_machine`; audit `d40041c3…` |
| 2026-05-24 | `substrate_cocycle_ratio_67_88` | `7.324992` (6sf, F2) | `7.3249917525961665` (full float64, F2-faithful) | W5-1 substrate-first recompute from M₃(ℂ) frame norms; audit `491ac49c…` |
| 2026-05-24 | F1-vs-F2 cocycle-ratio historiography | open question (S92 W7) | **arbitrated: F2 = substrate; F1 = double-rounding F-image** | W5-1 `round_to_6sf(R_machine)=7.32499=F2`; `dist_F2=2.5e-7 ≪ dist_F1=1.7e-5` |
| 2026-05-24 | §VII.AR PASS-A reading | substrate-IS (S92 §W4-1, both-fold co-equal) | **METHODOLOGY-floor-only** | W5-3 FULL-tier N=4 PV: flip not reproduced (`[1,1,1,1,1]`); dual-prior → Track B 0.90; audit `2e4a33bf…` |
| 2026-05-24 | §VII.AR STAGE-3 eligibility support | `{PASS-A, PASS-B}` | `{PASS-B}` (A_5_extended−ζ, `ρ_S_FULL=1.0`) | W5-3-CF annotation; PASS-A floored; audit `ffa053c8…` |
| 2026-05-24 | §VII.AR Element-5 scope | continuous `(cutoff_frac, M_PV²_frac)` vector reading | **sub-atlas MEMBERSHIP only** | W5-3-CF S-1 V.2 category-conflation closure |
| 2026-05-24 | §VII.AR.Cell-IV filter-geometry coherence | untested at 6th observable (HK_trace) | **6/6 L∞-box < triangular ordering** | W5-4 after filter-INDEPENDENT t-anchor fix; audit `dc796fb8…` |
| 2026-05-24 | §VII.AW.OP-PROJ (SUBSTRATE-CLOCK) | STAGE-3-PERMANENT (S92), set-membership unrecorded at S93 | STAGE-3 set-membership recorded; lockfile drift s90→s93 corrected | W5-5 branch-(a) verification-confirmation; audit `c118e759…` |
| 2026-05-24 | §VII.AW slot label | collision (2 entries share §VII.AW) | resolved: §VII.AW = substrate-clock; SU(3)-Coloured-Chirality → **§VII.BF** | W5-6 label-only rename, 4 loci; audit `8b37513e…` |
| 2026-05-24 | Element-3 (iii) K-counter (cross-pillar-bridge §"Element 3") | K=1 | K=2 | W5-2 §VII.AY.OP-PROJ Element-5 Stage-2 second distinct instance |

**Session-end reconciliation (NOT a math CF; NOT deferred to S94):** the AU/AW "THIRD STAGE-3-PERMANENT" **ordinal** collision (both §VII.AU.OP-PROJ and §VII.AW.OP-PROJ claim "THIRD"; gate-verdict placeholder tag `CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW`) is registry ordinal-bookkeeping, not new computation. W5-5 settled the chronology (§VII.AW promoted S92, before §VII.AU at S93). Per `CLAUDE.md §"No Technical Debt"` it is hygiene → resolve at **S93 session-end synthesis** once all waves' STAGE-3 promotions are known (W6 §VII.AQ / §VII.BB / §VII.BE may add more); it is NOT a genuine S94 carry-forward. Recorded here so session-end synthesis reconciles the ordinals across the full S93 STAGE-3 set.

## Files Produced

All paths relative to `computations/`. Compute-gate scripts in `session-93/`; mack registry-write scripts in `_shared/`. Data/plot/json all in `session-93/`.

| Gate | Script | .npz | .png | .json |
|:-----|:-------|:-----|:-----|:------|
| W5-1 | `session-93/s93_w5_1_substrate_cocycle_ratio_67_88_r_machine_recompute.py` (32,862 B) | 11,982 B | 69,164 B | — |
| W5-2 | `session-93/s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.py` (53,543 B) | 15,864 B | 69,406 B | 3,528 B |
| W5-3 | `session-93/s93_w5_3_vii_ar_full_tier_n4_retry.py` (45,414 B) | 17,878 B | 155,324 B | — |
| W5-3-CF | `_shared/s93_w5_3_cf_vii_ar_pass_a_methodology_floor_annotation.py` (46,755 B) | 15,557 B | 62,888 B | 4,693 B |
| W5-4 | `session-93/s93_w5_4_vii_ar_filter_geometry_audit.py` (32,463 B) | 15,316 B | 186,131 B | — |
| W5-5 | `_shared/s93_w5_5_vii_aw_op_proj_stage_3_permanent_promotion.py` (39,864 B) | 15,937 B | 61,001 B | 5,132 B |
| W5-6 | `_shared/s93_w5_6_vii_aw_slot_rename.py` (53,373 B) | 10,800 B | 57,530 B | 5,061 B |

Registry / canonical / ledger writes (non-script artifacts): `sessions/permanent-results-registry.md` (§VII.AY STAGE-3, §VII.AR annotation, §VII.AW set-membership + §VII.BF rename); `computations/_shared/canonical_constants.py:277-278,1251`; `sessions/framework/registry/methodology-wave-allowlist-ledger.md:184-186` + `…-instances.md`; `sessions/framework/s93-slot-pre-allocation-lockfile.md`; verdict file `computations/session-93/s93_gate_verdicts.txt:83-106`.
