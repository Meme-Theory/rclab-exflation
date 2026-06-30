# Session 94 Wave 8 — §VII.AV Stage-2 re-verify + §VII.AR PASS-A substrate-derivation (Results Working Paper)

**Session**: 94 | **Wave**: 8 | **Plan**: session-94-plan-w8.md | **Theme**: Close the two §VII.AV / §VII.AR BdG-substrate carry-forwards left open at S93 close — complete the OP-PROJ Stage-2 PASS-AND (Axis-A re-verify on the Cell-II-corrected entry) and adjudicate §VII.AR PASS-A's epistemic standing (substrate-BdG-derived coupling vs SCHEMATIC scalar prefactor). Both operate on the algebra-INVARIANT spectrum-only functional family at the substrate-distance-2 Mellin-cone pole s=4; both are GEOMETRIC.

## Gate Sections

### §W8-1. S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY (van-den-dungen-bridge-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Stage-2 cross-axis re-verify of the OP-PROJ corner-cell clause on the Cell-II-corrected registry entry)
**Agent**: `van-den-dungen-bridge-theorist`
**Hypothesis**: On the Cell-II-corrected §VII.AV.OP-PROJ entry, the vdd (Axis-A, NCG-submersion / spectral-functional) corner-cell clause — the SOLE clause that FAILed at S93 W3-6 (read as Cell I) — now PASSes (Cell II = INVARIANT × s=4 per §VII.U.2), and with Axis-B (mack) already PASS on disk the JOINT clauses PASS-AND across both verdicts, completing the OP-PROJ Stage-2 PASS-AND and rendering §VII.AV.OP-PROJ STAGE-3-eligible.
**Plan reference**: `sessions/session-plan/session-94-plan-w8.md` §W8-1 (machinery pin, thresholds, Stage-2 reviewer-selection protocol, substrate framing).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

- **Script** `computations/session-94/s94_vii_av_op_proj_stage2_axis_a_reverify.py` (33720 bytes) — must_contain verified:
  - `grep -nE "from canonical_constants import|def append_verdict"` →
    - `111: from canonical_constants import M_KK, tau_fold  # noqa: E402`
    - `652: def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:` (+ call site `566: append_verdict(verdict, value, audit_sha, content_sha)`)
- **Data** `computations/session-94/s94_vii_av_op_proj_stage2_axis_a_reverify.npz` (13603 bytes) — present (clause matrix, corner-cell re-derivation, JOINT PASS-AND, reviewer-selection protocol booleans, `stage_3_eligible=True`).
- **Plot** `computations/session-94/s94_vii_av_op_proj_stage2_axis_a_reverify.png` (102625 bytes) — present (Axis-A clause matrix incl. corner-cell W3-6-FAIL → Cell-II re-verify transition; JOINT PASS-AND across both axes; composite + STAGE-3-eligible row).
- **Verdict line** `computations/session-94/s94_gate_verdicts.txt` — matches `^S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY:.* audit_sha256=[a-f0-9]{64}`:
  - `S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY: PASS -- value='corner_cell_clause_PASS=True_Cell-II_INVARIANTxs4_label_match(claimed=Cell-II==derived=Cell-II)_axisA_single_axis_all_PASS=True_joint_pass_and_count=2of2_axisB_mack_on_disk=PASS_RSP_4cond_OK=True_OP-PROJ_Stage-2_PASS-AND_complete_BOTH_axes_VII.AV.OP-PROJ_STAGE-3-ELIGIBLE=True_...' ... audit_sha256=ba0c24d00d19db8b246ab33e3fd091b5c5742102a261a7d6ce97ba3d433d1652 content_sha256=a2c841a5c51ef818803c426f32b62de8cec2cb77c462889bc2c8b66afc57dd30 schema_version=S84+`
  - dual-SHA companion row present: `# audit_sha256_short=ba0c24d00d19db8b content_sha256_short=a2c841a5c51ef818 # S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY dual-SHA companion row; ... [VERIFY-THEOREM] no [SIGN] 3-tuple` — `companion_row_required` ✓; NO 3-tuple companion (`[VERIFY-THEOREM]`, not `[SIGN]`) ✓.
  - `audit_sha256` count across file = 1 (sig_5 SHA-uniqueness clean).
- **WP §W8-1 section** (this section) — 4 must_contain markers present: `**Status**: COMPLETED`, `**Verdict**: ... PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**`.

**MCP Pre-Compute Audit** (query-first discipline per `.claude/rules/knowledge-index-usage.md`; all queries executed BEFORE writing the script):

- `trace_entity('VII.AV')` → confirmed the §VII.AV Stage-2 history: gate `S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT` (INFO, one-clause-short) and `S93-W3-VII-AV-STATE-PROJ-STAGE-3-PERMANENT-PROMOTION` (STATE-PROJ companion already STAGE-3-PERMANENT on the W3-6 clean PASS-AND, audit `610d1ac85b5a2ef0`). NOT a re-compute conflict — the Axis-A re-verify gate is the pre-registered next step, not yet evaluated.
- `search_knowledge('OP-PROJ Stage-2 PASS-AND corner cell')` → returned the W3-6 gate value string `OP-PROJ_vdd=FAIL_mack=PASS_joint_PASS-AND=True_OP-PROJ_axisA_FAIL_corner_cell_only` — confirms the exact one-clause-short state (Axis-A FAIL on corner-cell ONLY; Axis-B mack PASS; JOINT PASS-AND already True).
- `search_knowledge('algebra-axis orthogonality corner cell INVARIANT s=4')` → §VII.U.2 (PROVEN, atlas-07): "Cell I = INVARIANT × s=3; **Cell II = INVARIANT × s=4**; Cell III = DEPENDENT × s=3; Cell IV = DEPENDENT × s=4" — the canonical 4-corner partition that is the AUTHORITY for the corner-cell label. INVARIANT × s=4 = Cell II, full stop.
- NOT PRE-CLOSED: no closure covers this Stage-2 Axis-A re-verify; the gate produces a new clause-PASS matrix + JOINT PASS-AND verdict against the Cell-II-corrected entry. Proceeding is correct.

**Verdict**: **PASS** — `corner_cell_clause_PASS=True AND joint_pass_and_count==n_joint_clauses (2 of 2)`. The OP-PROJ Stage-2 PASS-AND is complete across both axes; §VII.AV.OP-PROJ is STAGE-3-eligible.

**Results**:

*Mechanical-closure prerequisite (entry must be Cell-II at dispatch)*: PASS — the live registry §VII.AV.OP-PROJ entry is Cell-II-corrected at dispatch (`cell_ii_heading=True; corner_cell_II_marker=True; stale_cell_i_heading=False`; the Cell I→Cell II remediation, 19 markers, landed S93 W3-6 per `s93_w3_6_vii_av_op_proj_cell_ii_remediation.py`). No mechanical-closure INFO branch fired.

*First-principles corner-cell re-derivation (Axis-A, spectral-functional — re-derived, NOT carried)*: The 4-corner cell is the pair `(algebra-axis of parse-tree, Mellin pole s)` per §VII.U.2 clause (e). For `B_LAYER_A := Tr_{A_K}(P_a · |D_K|^{-2s})` at s=4 over PW sectors `{(0,2),(1,1),(2,0)}`:
- parse-tree terminus `Tr`, closed form `Σ_k m_k |λ_k|^{-2s}` — **no π(a)**, no `[D, π(a)]`, no state-pair `sup` ⇒ **algebra-INVARIANT** (clause (e): `PT(F) = INVARIANT iff AST contains no π(a) reference`);
- substrate-distance-2 pole ⇒ **s = 4**;
- ⇒ derived cell = partition`[(INVARIANT, 4)]` = **Cell II**.

*Corner-cell clause (exact-label match, NOT a numerical threshold)*: claimed (registry) = **Cell II** == derived (first-principles) = **Cell II** ⇒ **PASS**. This is precisely the clause that FAILed at W3-6: my W3-6 Axis-A verdict (`s93_w3_6_axis_a_vdd_verdicts.json`, corner-cell rationale) stated "the algebra-axis (INVARIANT) and pole (s=4) sub-claims are each correct; only the I-vs-II cell terminus is wrong … The corner-cell LABEL should read Cell II." The remediation flipped the label to exactly the value my derivation produces — the structural objection I raised is resolved, not papered over.

*Per-clause Axis-A OP-PROJ PASS matrix*:

| Axis-A clause | Source | Verdict |
|:--------------|:-------|:--------|
| `substrate_IS_observable_identity` | carried W3-6 (label-defect did not touch it) | PASS |
| `parse_tree_INVARIANT_classification` | carried W3-6 | PASS |
| `Level_1_single_tau_slice_tag` | carried W3-6 | PASS |
| `corner_cell_classification` (W3-6 prior) | W3-6 | FAIL (read Cell I) |
| `corner_cell_classification` (Cell-II re-verify) | **RE-VERIFY this gate** | **PASS** (Cell II = INVARIANT × s=4, exact-label match) |

All Axis-A single-axis clauses PASS (`all_single_axis_carried_PASS=True`; no carried clause is INFO ⇒ no Stage-2-INFO-deferred branch).

*JOINT-clause PASS-AND across {Axis-A re-verify, Axis-B mack on-disk}* (Axis-B leg from `s93_w3_6_vii_av_stage_2_cross_axis_verify.json`):

| JOINT clause | Axis-A | Axis-B (mack on-disk) | PASS-AND |
|:-------------|:-------|:----------------------|:---------|
| `JOINT_bridge_map` (HKR L_max→∞ at d=4 s=4; CM-1995 §III.4 residue on A_K; type-(i) substrate-self-consistent) | PASS | PASS | True |
| `JOINT_structural_orthogonal_companion` (Cell II vs Cell IV cross-corner co-primary FORBIDDEN) | PASS | PASS | True |

`joint_pass_and_count / n_joint_clauses = 2 / 2`. The `structural_orthogonal_companion` Axis-A leg was PASS-CONDITIONAL (raw) at W3-6, upgraded to PASS via the W3-3 Class-8.7 degeneracy-witness (`conditional_upgraded=True`, audit `f21af912…`); the Cell-II remediation also discharges the cell-pair-label condition the raw PASS-CONDITIONAL flagged (the JOINT clause's "Cell I vs Cell IV" label is now "Cell II vs Cell IV"). Axis-B mack on-disk OP-PROJ verdict = PASS (already PASS-AND on all OP-PROJ clauses at W3-6). The PASS-AND is a logical AND (both legs PASS), per `joint-theorem-promotion.md §"Stage 2"` (JOINT clauses PASS-AND'd, not OR'd).

*4-condition Stage-2 reviewer-selection protocol confirmation (vdd, `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`, applied to the Axis-A reviewer per plan §W8-1)* — all OK:
1. **Axis-distinctness** ✓ — Axis-A (vdd) = NCG-submersion / spectral-functional; Axis-B (mack, on disk) = cosmological-bridge / observational. Distinct axes.
2. **Original-authoring-agent exclusion + downstream-inheritance reach** ✓ — `workshop_transcript_read=false`; vdd NOT in {connes-ncg, phonon-first, volovik}; no `reference_*.md` citation of the §VII.AV W-3 R1/R2/R3 transcripts (`OAA_exclusion_satisfied=true`).
3. **Audit-coverage adequacy** ✓ — vdd's NCG-submersion / spectral-functional expertise covers the corner-cell parse-tree classification on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` + the OP-PROJ JOINT clauses (HKR/residue bridge map + algebra-axis orthogonality).
4. **Substrate-input orthogonality** ✓ — this re-verify does NOT load the OP-PROJ residue cache `s92_w3_9_…npz` (an Axis-B orthogonal input; `op_proj_cache_loaded_here=False`). The corner-cell re-derivation is a parse-tree / pole structural determination — no substrate numerical cache needed; the input-pin map explicitly excludes the cache. Structural ceiling, no overlap caveat.

*PASS/FAIL/INFO criterion*: PASS iff `corner_cell_clause_PASS==True AND joint_pass_and_count==n_joint_clauses`. Computed: `corner_cell_clause_PASS=True` ∧ `2==2` ∧ all single-axis carried PASS ∧ reviewer-selection 4-cond OK ⇒ **PASS**.

*4-tuple*: `(value=corner_cell_clause_PASS=True_Cell-II_INVARIANTxs4_label_match…_OP-PROJ_Stage-2_PASS-AND_complete_BOTH_axes_VII.AV.OP-PROJ_STAGE-3-ELIGIBLE=True_W3-6_INFO_one-clause-short_UPGRADED=True…convention_ends_FULL=True, scheme=joint-theorem-promotion-Stage-2-Axis-A-reverify-on-Cell-II-corrected, convention=Stage-2-OP-PROJ-vdd-AxisA-reverify-Cell-II-INVARIANT-x-s4-JOINT-PASS-AND-FULL, L_max=12)`.

*STAGE-3-eligibility statement (on PASS)*: The OP-PROJ Stage-2 PASS-AND is now complete with BOTH axes PASS (Axis-A vdd re-verify PASS on the corrected corner-cell clause + all single-axis clauses + both JOINT clauses; Axis-B mack on-disk PASS). Per `joint-theorem-promotion.md §"Stage 3 — Permanent Registration"`, **§VII.AV.OP-PROJ is STAGE-3-eligible**: at session-end synthesis the orchestrator flips `STAGE-1-CANDIDATE → STAGE-3-PERMANENT` (mack sole writer per `feedback_mack-bridge-role.md`; this gate does NOT edit the registry). On the flip, the §VII.AV pair is both-STAGE-3 — the §VII.AV.STATE-PROJ structural-orthogonal-companion already reached STAGE-3-PERMANENT at S93 W3-6 (audit `610d1ac85b5a2ef0`). The S93 W3-6 INFO (one-clause-short) is upgraded by this gate's PASS.

*Substrate framing (GEOMETRIC)*: §VII.AV.OP-PROJ's substrate-IS observable IS the central-projection trace-residue `Tr_{A_K}(P_a · |D_K|^{-2s})` on D_K's block-diagonal spectrum at the substrate-distance-2 Mellin pole s=4 (B_LAYER_A=375.227, W3-3). The 4-corner classification is a STRUCTURAL property of this observable's parse-tree on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`: spectrum-only sum (no state-pair) ⇒ algebra-INVARIANT; s=4 ⇒ Cell II. Direction substrate → emergent: D_K eigenvalues → central-projection trace at s=4 → INVARIANT-family corner-cell. The Stage-2 cross-axis re-verify is the methodology-floor F-image (`epistemic-discipline.md §"Layer-Decomposition"`) of this substrate-IS structural fact — it confirms the corner classification is derivable from first principles on the spectral-functional axis WITHOUT the workshop's reading-path, breaking the shared-context-produces-shared-output failure mode. No container-thinking: the substrate IS the trace-residue; the lab does not measure §VII.AV.OP-PROJ IN any continuum.

*Artifacts*: `s94_vii_av_op_proj_stage2_axis_a_reverify.py` / `.npz` / `.png`.

---

### §W8-2. S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (cutoff_axis: spectral — cutoff acts on D_K eigenvalues, not momentum-shell coherence)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: The §VII.AR PASS-A deep-IR rank-flip `[0,0,0,0,1]` + anti-correlated `ρ_S^{deep-IR} < 0` — which VANISHED at S93 W5-3 FULL-tier N=4 PV when the SCHEMATIC scalar `(1−M_PV²_frac_r)` prefactor was dropped (FULL: rank `[1,1,1,1,1]`, `ρ_S_FULL=+0.20`) — is RECOVERED when the per-regulator coupling is sourced from first-principles substrate BdG physics (S52 Bogoliubov occupation `v_a²=Δ²/(2(λ²+Δ²))` on M₂(ℂ)⊂A_K) in place of the SCHEMATIC prefactor; PASS ⇒ PASS-A restored substrate-IS (eligibility re-widens to {PASS-A, PASS-B}), FAIL ⇒ PASS-A permanently methodology-floor (stays {PASS-B}).
**Plan reference**: `sessions/session-plan/session-94-plan-w8.md` §W8-2 (machinery pin, dual-prior pre-registration, substitution chain, SCHEMATIC-vs-FULL level-pin discipline, substrate framing).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

- **Script** `computations/session-94/s94_vii_ar_pass_a_substrate_derivation.py` — EXISTS (56,916 bytes). `grep` proof:
  - `from canonical_constants import` → `from canonical_constants import *` + `from canonical_constants import (M_KK, tau_fold, Vol_SU3_Haar, Delta_BCS,)`
  - `append_verdict` → `def append_verdict(...)` + call site `append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, reg_v)`
- **Data** `computations/session-94/s94_vii_ar_pass_a_substrate_derivation.npz` — EXISTS (25,012 bytes; 66 keys). Core observables verified on reload: `rho_S_FULL_substrate=0.19999999999999998`, `rank_change_per_anchor_FULL_substrate=[1 1 1 1 1]`, `composite_verdict=FAIL`, `reclassification_branch=PASS-A-PERMANENTLY-METHODOLOGY-FLOOR`, `posterior_track_B=0.9`, `form_A_minus_form_B_max=0.056497110308371054`.
- **Plot** `computations/session-94/s94_vii_ar_pass_a_substrate_derivation.png` — EXISTS (222,295 bytes; rank-change bar panel + v_a²(λ) curve inset + verdict box).
- **Verdict line** `computations/session-94/s94_gate_verdicts.txt` — 4 rows landed, `audit_sha256` unique (grep count = 1):
  - Canonical (regex `^S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION:.* audit_sha256=[a-f0-9]{64}` ✓): `S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION: FAIL -- value='composite=FAIL;...' scheme=FULL-tier-N4-Connes-Chamseddine-1996-substrate-BdG-derived-coupling convention=VII-AR-PASS-A-substrate-derived-v_a2-BdG-M2C-asymmetric-FULL-tier-N4-Lambda-UV-M_KK L_max=12 audit_sha256=6cbe7e1223a21547498bc3cb963890d68ed907e9c7f4bb78981429950347975a content_sha256=0ee25523ec2204fd2ca185e8f93dbfb742b4783c1a91dd74261749c5b0bd9adc schema_version=S87+` — convention carries NO `-SCHEMATIC` suffix (FULL/TIER-1).
  - Dual-SHA companion: `# audit_sha256_short=6cbe7e1223a21547 content_sha256_short=0ee25523ec2204fd # ... dual-SHA companion row (W9a-99 split)`
  - `[SIGN]` 3-tuple companion (schema_v2_3tuple_required ✓): `# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID # ... 3-tuple annotation (S87 schema-v2)`
  - `# tier_pin=TIER-1` companion (FULL physical regularization, level-pin §(iv) ✓): `# tier_pin=TIER-1 # ... CLASS=FULL; NO -SCHEMATIC suffix; per-regulator coupling SOURCED from substrate-IS S52 BdG occupation v_a²=Δ²/(2(λ²+Δ²)) on M₂(ℂ)⊂A_K; SCHEMATIC scalar (1−M_PV²_frac) retained as W5-3 cross-check baseline ONLY (ρ_S_SCHEMATIC=−0.20), never the PASS source`
- **WP §W8-2 section** (this section) — 4 must_contain markers present (`**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**`).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md` — queried BEFORE writing the script; query-first discipline):

- `get_constant('Delta_BCS')` → **0.4642547394830737**, S70, alias for `Delta_0_OES`, gate `BCS-GAP-CANONICAL-70`, **R-PROTECTED: YES**, superseded: False. Matches the plan pin bit-for-bit; imported by name (never hardcoded).
- `trace_entity('VII.AR')` → §VII.AR contested between W-18 (W6a-51 dual-reading) and W-22 (W7a-74 LEVEL-DRESSED), PROVEN. Gate `S93-W5-3-CF-VII-AR-PASS-A-METHODOLOGY-FLOOR-ANNOTATION` (S93): `VII-AR-PASS-A-RECLASSIFIED-METHODOLOGY-FLOOR-ONLY_W5_3_FULL_FAIL`. **Confirms the S93 W5-3 reclassification this gate adjudicates; this S94 gate is NOT yet evaluated — the open conviction-or-acquittal question.** Not closed.
- `search_knowledge('PASS-A deep-IR rank-flip Spearman regulator atlas')` → `rho_S^{R}(s=4)` per-regulator Spearman at substrate-distance pole s=4; `R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}`; deep-IR companion `rho_inf_zubarev_deep_ir = −0.918`. Confirms the s=4 Spearman-rank observable + atlas context; the §VII.AR 4-regulator atlas {F_2, cutoff_sqrt, anomaly, Zubarev} (W7a-74 PRIMARY) reused verbatim.
- `search_knowledge('Bogoliubov occupation amplitude v_a BdG M2C')` → **`v_a(K)² = (1/2)(1 − ξ_a(K)/E_a(K))`** with `E_a=√(ξ_a²+|Δ_a|²)` (session-89-w5; Form B); **`|v_a(K)|² = Δ_a²/(2(λ_a²+Δ_a²))`** "per S52 BdG canonical amplitudes" (`s91-w1-operational-alignment-regulator-class-robustness.md:385`; Form A — flagged there as a **state-pair object on the BdG sub-algebra**, NOT a regulator-INVARIANT spectrum-only moment). Both substrate-weight equation entries confirmed.

**Sage exact-form pre-check** (`mcp__sage__sage_eval`, before finalizing the weight function — settles the two-form question): Form A `Δ²/(2(λ²+Δ²)) = ½ − (1/2Δ²)λ² + O(λ³)` (even-in-λ); Form B `(1/2)(1−λ/√(λ²+Δ²)) = ½ − (1/2Δ)λ + O(λ²)` (linear-in-λ term). They COINCIDE at λ=0 (both 1/2) and DIVERGE for λ>0: `diff(λ_min=0.820)=5.650e-2`, `diff(λ_max=5.419)=1.818e-3`. This confirms the plan's own `"= Δ²/(2(λ²+Δ²)) + O(...) at λ→0"` text: the algebraic identity is deep-IR-leading-order only. The plan PINS **Form A** as the operative weight (machinery_pin_map line 340 leading form); Form B is the λ→0-equivalent fundamental-BdG-occupation reference. Both recorded in the npz; no false bit-equality asserted.

**Verdict**: **FAIL** — composite = FAIL; reclassification_branch = **PASS-A-PERMANENTLY-METHODOLOGY-FLOOR**. The substrate-derived `v_a²(λ)` BdG-occupation weighting does NOT recover the deep-IR rank-flip; the S93 W5-3 reclassification stands. §VII.AR PASS-A is permanently methodology-floor-only; eligibility stays **{PASS-B}**. PASS-B carries §VII.AR STAGE-3 eligibility regardless (sub-atlas-minus-ζ, `ρ_S=1.0`); this gate governed ONLY PASS-A's standing.

**Results**:

**4-tuple**: `(value=FAIL/PASS-A-PERMANENTLY-METHODOLOGY-FLOOR, scheme=FULL-tier-N4-Connes-Chamseddine-1996-substrate-BdG-derived-coupling, convention=VII-AR-PASS-A-substrate-derived-v_a2-BdG-M2C-asymmetric-FULL-tier-N4-Lambda-UV-M_KK, L_max=12)`.

**Cache + weight (substrate input)**: L_max=12 spectrum cache `s84_spectrum_cache_L12_tau019.npz` (runtime canonical path; SHA `9e6d9cf7...` matches plan pin), 90 sectors, **166,896 eigenvalues**, λ ∈ [0.81974, 5.4189] at τ_fold=0.19. Operative weight (Form A, plan-pinned) `v_a²(λ_min=0.820)=0.121426` (deep-IR; largest), `v_a²(λ_max=5.419)=3.643e-03` (UV; smallest), monotone-decreasing — a ~33× deep-IR concentration. Δ=`Delta_BCS=0.4642547394830737` (R-protected).

**Rank-change vectors + ρ_S (the discriminator)**:

| quantity | SCHEMATIC baseline (W5-3 cross-check) | FULL N=4 + v_a² (this gate) | W5-3 FULL on-disk baseline |
|:---------|:-------------------------------------:|:---------------------------:|:--------------------------:|
| `rank_change_per_anchor` | `[0,0,0,0,1]` (flip at deep-IR) | **`[1,1,1,1,1]`** (flip NOT recovered) | `[1,1,1,1,1]` |
| deep-IR Spearman ρ_S (PRIMARY-vs-SCHEMATIC) | `−0.200000` | **`+0.200000`** | `+0.200000` |
| `abs_diff` (flip-match band) | — | **`0.400000`** ≫ 1e-3 | `0.400000` |

The SCHEMATIC baseline reproduces the W5-3 on-disk values bit-for-bit (`ρ_S_SCHEMATIC=−0.200000` ✓, deep-IR flip `[0,0,0,0,1]` ✓; `schematic_baseline_cross_check_match=True`) — the machinery is correctly wired. Under FULL+v_a², every anchor's PRIMARY rank changes (not just the deep-IR one), `ρ_S_FULL_substrate=+0.200000` (positive, NOT < 0).

**PASS/FAIL/INFO criterion**: PASS iff `rank_change_per_anchor==[0,0,0,0,1] AND ρ_S_FULL_substrate<0 AND abs_diff(ρ_S)≤1e-3`. All three conjuncts FAIL:
- conjunct-rank-flip (`rank==[0,0,0,0,1]`): **False** (got `[1,1,1,1,1]`)
- conjunct-rho-neg (`ρ_S_FULL_substrate<0`): **False** (got `+0.200000`)
- conjunct-abs-diff (`|Δρ_S|≤1e-3`): **False** (got `0.400000`)
⇒ composite **FAIL**; PASS-A permanently methodology-floor; eligibility stays {PASS-B}.

**Dual-prior posterior mapping (pre-registered; reported verbatim, NOT re-narrativized)**: Track A (substrate-IS-restored) prior **0.30**; Track B (methodology-floor-only) prior **0.70**. Outcome = FAIL ⇒ **posterior 0.90 to Track B** (Track A → 0.10). Resolved: **Track B (methodology-floor-only; v_a² is regulator-common)**. §VII.AR eligibility: **{PASS-B}** (unchanged; PASS-A permanently methodology-floor). [The plan pre-registers exactly this map: FAIL ⇒ posterior 0.90 to Track B; the realized FAIL maps to the pre-registered Track-B posterior with no re-narrativization.]

**5-step substitution chain (substituted numbers)**:
- **Step 1 (Definitions)**: W5-3 FULL baseline (on disk, `S93-W5-3-VII-AR-FULL-TIER-N4-RETRY`) `ρ_S_FULL=+0.200000`, `ρ_S_SCHEMATIC=−0.200000`, `rank=[1,1,1,1,1]`, `abs_diff=0.400000`. S52 BdG occupation Form A `v_a²(λ)=Δ²/(2(λ²+Δ²))`, Δ=`Delta_BCS=0.4642547394830737` (R-protected, BCS-GAP-CANONICAL-70); λ→0-equivalent Form B `(1/2)(1−λ/√(λ²+Δ²))` (Sage: coincide only at λ→0). CC-1996 N=4 PV kernel `K_PV(λ²;M_PV²)=Σ_{j=0}^{4} c_j/(λ²+j·M_PV²)^4`, `c_j=[1,-4,6,-4,1]`, Λ_UV=M_KK (a_2^{Pauli-Villars}).
- **Step 2 (Substitute — parameter SOURCE replacement)**: `M_r^{PRIMARY,sub}(t)=Σ_λ m_λ·profile_r(cf_r·t·λ²)·K_PV(λ²;M_PV²_frac_r·max(λ²))·v_a²(λ)` — the per-eigenvalue `v_a²(λ)` BdG occupation weight (computed from D_K's spectrum + Δ) replaces the SCHEMATIC scalar `(1−M_PV²_frac_r)` prefactor. The cf_r/M_PV²_frac_r atlas {0.7,0.5,0.9,1.2}/{0.1,0.05,0.2,0.15} and CC-1996 kernel reused VERBATIM from W5-3; the DISCRIMINATING change is `v_a²(λ)`.
- **Step 3 (structural fork)**: Track A — deep-IR-concentrated `v_a²(λ)` re-amplifies smallest-λ asymmetrically across regulators ⇒ flip recovers. Track B — `v_a²(λ)` is a regulator-COMMON multiplicative weight (SAME function of λ for all 4 regulators) ⇒ cannot break the FULL N=4 PV rank-ordering; rank stays `[1,1,1,1,1]`.
- **Step 4 (PREDICTED DIRECTION, ~0.70 Track B)**: FAIL — flip stays absent, `ρ_S≥0` — because `v_a²(λ)` is regulator-COMMON and the W5-3 finding localized the flip to the regulator-ASYMMETRIC SCALAR `M_PV²_frac` knob, which the substrate amplitude does not carry.
- **Step 5 (read-off)**: discriminator `d:=sign(|ρ_S_FULL_substrate−ρ_S_SCHEMATIC|−1e-3) AND sign(ρ_S_FULL_substrate)`. COMPUTED: `|0.200000−(−0.200000)|=0.400000 > 1e-3` AND `ρ_S_FULL_substrate=+0.200000 ≥ 0` ⇒ FAIL. **PREDICTED FAIL matches COMPUTED FAIL** ⇒ `sign_verdict=PASS`. Conclusion: the deep-IR flip is confirmed a property of the regulator-ASYMMETRIC SCHEMATIC `M_PV²_frac` scalar prefactor under profile saturation, NOT of substrate BdG occupation physics. PASS-A permanently methodology-floor.

**SIGN/MAGNITUDE/REGIME 3-tuple**: `sign_verdict=PASS` (Step-4 predicted direction FAIL/flip-stays-absent matches the computed FAIL); `magnitude_verdict=FAIL` (the gate's 3-conjunct numeric target is not met — flip not recovered ∧ ρ_S not negative ∧ |Δρ_S|=0.400 ≫ 1e-3); `regime_verdict=VALID` (`breach_frac=0.00` — all CC-1996 N=4 PV × v_a² moments finite + non-degenerate at all 5 anchors). Composite-collapse rule (gate-verdicts.md §"Composite-collapse rule", PRE-REGISTERED, modifying post-verdict is PROHIBITED Class-3): `regime=VALID ∧ magnitude=FAIL ⇒ composite=FAIL`. (The SIGN-PASS result is the honest physics: the substitution chain CORRECTLY predicted the flip would not recover; the gate FAILs because the PASS criterion required flip-recovery, which did not happen.)

**SCHEMATIC-vs-FULL level-pin disclosure (cross-class; substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)**: CLASS pin = **FULL** (TIER-1). The producing script executes the genuine CC-1996 §2.2-2.3 N=4 Pauli-Villars mass tower (`c_j=[1,-4,6,-4,1]`, masses `M_j²=j·M_PV²`, Λ_UV=M_KK), tagged **a_2^{Pauli-Villars}** (regulator-pin-discipline.md; bare a_2 FORBIDDEN) — NOT the SCHEMATIC scalar `(1−M_PV²_frac_r)` prefactor — AND sources the per-regulator coupling from the substrate-IS BdG amplitude `v_a²`. The verdict-line `convention=` carries **NO `-SCHEMATIC` suffix**; the `# tier_pin=TIER-1` companion row accompanies the canonical line. **The deep-IR flip's persistent ABSENCE under the substrate-DERIVED v_a² weighting at FULL-tier N=4 is the conviction-or-acquittal of the S92 §W4-1 PASS-A reading; the SCHEMATIC-scalar source is retained ONLY as the W5-3 cross-check baseline (ρ_S_SCHEMATIC=−0.20, reproduced bit-for-bit here), NEVER as the PASS source.** The S52 amplitude carries no per-regulator Pauli-Villars mass-suppression knob of the `M_PV²_frac` form; it is a regulator-COMMON multiplicative weight (consistent with `s91-w1:385`'s observation that `|v_a(K)|²` is a state-pair object on the BdG sub-algebra, not a regulator-INVARIANT spectrum-only moment). Sage-verified Form A vs Form B distinction recorded (coincide only at λ→0); the operative weight is the plan-pinned Form A.

**Plan-text-drift note (substrate-first-canonical-sourcing.md §(ii.B))**: `canonical_constants.py` plan-§W8-2 pin `102f8f76...` ≠ LIVE runtime SHA `e1f24ac5...` — drift between plan-freeze and runtime (the module gained unrelated constants). The LIVE canonical is authoritative (knowledge-base-wins). The consumed values are UNCHANGED and match the knowledge MCP canonical bit-for-bit: `Delta_BCS=0.4642547394830737`, `M_KK=7.428660036284456e+16`, `tau_fold=0.19`, `Vol_SU3_Haar=1349.7399583199533`. Drift documented in the verdict-line `value=` field (`canonical_drift=True;canonical_live_sha=e1f24ac5...;canonical_plan_pin=102f8f76...;Delta_BCS_unchanged_vs_MCP_canonical=True`); no remediation needed (consumed values bit-identical to plan-freeze values; D_max for the consumed constants = 0).

**§VII.AR eligibility statement (for mack, sole registry writer)**: §VII.AR PASS-A is **permanently METHODOLOGY-floor-only** — the substrate-derived BdG-occupation weighting FAILed to recover the deep-IR rank-flip. §VII.AR STAGE-3 eligibility stays **{PASS-B}** (PASS-B sub-atlas-minus-ζ carries it at `ρ_S=1.0`, unaffected by this gate). No registry status change vs the S93 W5-3 annotation (which already reflects PASS-A methodology-floor); this gate CONVICTS the PASS-A question (the conviction-or-acquittal closes in favor of conviction-as-methodology-floor). Cite this gate's `audit_sha256=6cbe7e1223a21547498bc3cb963890d68ed907e9c7f4bb78981429950347975a`.

**Substrate framing**: GEOMETRIC. The §VII.AR observable IS the Spearman rank-ordering of the 4-regulator atlas {F_2, cutoff_sqrt, anomaly, Zubarev} images at the substrate-distance-2 Mellin-cone pole s=4 on D_K's block-diagonal spectrum at τ_fold=0.19 — an algebra-INVARIANT spectrum-only functional. Direction substrate → emergent: D_K eigenvalues + Delta_BCS → BdG occupation amplitude v_a²(λ) on M₂(ℂ)⊂A_K → per-eigenvalue weighting → rank-ordering predicate at the s=4 pole. No container-thinking: the substrate IS the rank-ordering; the lab does not measure §VII.AR IN any continuum. The physics finding is that the deep-IR flip lives in the regulator-ASYMMETRIC SCHEMATIC scalar knob, not in the substrate's BdG occupation — a regulator-common weight cannot reproduce a regulator-asymmetric rank-flip.

**Artifacts**: `computations/session-94/s94_vii_ar_pass_a_substrate_derivation.py` (56,916 B), `.npz` (25,012 B, 66 keys), `.png` (222,295 B).

---

## Wave 8 Synthesis (team-lead)

Wave 8 closed the two §VII.AV / §VII.AR BdG-substrate carry-forwards left open at S93 close. Both gates operate on the algebra-INVARIANT spectrum-only functional family at the substrate-distance-2 Mellin-cone pole s=4; both GEOMETRIC. The wave is terminal for both sub-slots.

**Per-gate outcome:**

- **§W8-1 VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY** — **PASS**. On the Cell-II-corrected entry, the vdd (Axis-A, NCG-submersion/spectral-functional) corner-cell clause — the SOLE clause that FAILed at S93 W3-6 (mislabeled Cell I) — now PASSes (Cell II = INVARIANT × s=4, exact parse-tree label match per §VII.U.2 clause (e)). With Axis-B (mack) already PASS on disk, the JOINT clauses PASS-AND 2/2 across both verdicts → **OP-PROJ Stage-2 PASS-AND complete → §VII.AV.OP-PROJ STAGE-3-eligible**. The 4-condition Stage-2 reviewer-selection protocol held (axis-distinct vdd≠mack; OAA-exclusion + no downstream-inheritance, `workshop_transcript_read=false`; audit-coverage adequate; substrate-input orthogonality — vdd did NOT load the OP-PROJ residue cache). The S93 W3-6 one-clause-short INFO is upgraded.
- **§W8-2 VII-AR-PASS-A-SUBSTRATE-DERIVATION** — **FAIL** (composite; sign=PASS / magnitude=FAIL / regime=VALID; tier_pin=TIER-1 FULL). The substrate-derived S52 Bogoliubov occupation weight `v_a²=Δ²/(2(λ²+Δ²))` on M₂(ℂ)⊂A_K did NOT recover the §VII.AR PASS-A deep-IR rank-flip: rank stays `[1,1,1,1,1]` (vs target `[0,0,0,0,1]`), `ρ_S_FULL_substrate=+0.20` (vs target <0), abs_diff=0.40 ≫ 1e-3. The deep-IR flip is confirmed a property of the regulator-ASYMMETRIC SCHEMATIC `M_PV²_frac` scalar prefactor, NOT of substrate BdG occupation (v_a² is a regulator-COMMON multiplicative weight). The S93 W5-3 reclassification STANDS: **PASS-A is permanently methodology-floor-only; §VII.AR eligibility stays {PASS-B}**. The dual prior re-allocated 0.90 to Track B (pre-registered; reported verbatim, not re-narrativized). SCHEMATIC baseline reproduced W5-3 bit-for-bit (machinery correctly wired; the v_a² weighting is the isolated discriminating change). PASS-B carries §VII.AR STAGE-3 eligibility regardless (ρ_S=1.0) — unaffected.

**What Changed:**

### (a) Numerical revisions
- §VII.AR PASS-A substrate-derived `ρ_S_FULL_substrate = +0.20` (rank `[1,1,1,1,1]`; abs_diff 0.40 vs the 1e-3 flip-match band) — the flip does NOT recover.

### (b) Structural changes
- §VII.AV.OP-PROJ: **STAGE-1-CANDIDATE → STAGE-3-PERMANENT** (OP-PROJ Stage-2 PASS-AND complete; the §VII.AV pair — OP-PROJ + STATE-PROJ — is then both-STAGE-3) [promotion-pathway completion].
- §VII.AR PASS-A: **methodology-floor reclassification made PERMANENT** (the substrate-BdG conviction closes the PASS-A question; eligibility {PASS-A,PASS-B}→{PASS-B} confirmed permanent, not interim) [epistemic-standing finalization].

## Effected In-Session (orchestrator-direct; non-math)

- [x] §VII.AV.OP-PROJ STAGE-1-CANDIDATE → STAGE-3-PERMANENT registry flip — dispatched to `mack-cosmic-bridge` (sole registry writer; task #14) — W8-1 audit_sha `ba0c24d0`
- [x] §VII.AR PASS-A permanently-methodology-floor conviction annotation (eligibility stays {PASS-B}; no status change vs S93 annotation, records the closure) — dispatched to mack (task #14) — W8-2 audit_sha `6cbe7e12`
- orchestrator-direct presentation patch: none

## Carry-Forward Computations

**No math carry-forwards: both Wave 8 gates are terminal for §VII.AV / §VII.AR.** §W8-1 PASS completes the OP-PROJ Stage-2 PASS-AND (STAGE-3 flip effected via mack); §W8-2 FAIL closes the PASS-A question (permanently methodology-floor). The plan's W8→W9 Decision Point pre-registered a W8-2-PASS-conditional `ρ_S_FULL_substrate` canonical promotion — NOT triggered (the gate FAILed). No 4-field math spec remains.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-25 | §VII.AV.OP-PROJ | STAGE-1-CANDIDATE (one-clause-short, S93 W3-6 INFO) | STAGE-3-eligible → STAGE-3-PERMANENT (mack flip, task #14) | W8-1 PASS: corner-cell clause PASS on Cell II + JOINT PASS-AND 2/2 |
| 2026-05-25 | §VII.AR PASS-A | methodology-floor (S93 W5-3, interim) | permanently methodology-floor; eligibility {PASS-B} | W8-2 FAIL: substrate v_a² weight does not recover the flip |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) |
|:-----|:-------|:------------|:------------|
| W8-1 | `s94_vii_av_op_proj_stage2_axis_a_reverify.py` | `.npz` | `.png` |
| W8-2 | `s94_vii_ar_pass_a_substrate_derivation.py` | `.npz` | `.png` |
