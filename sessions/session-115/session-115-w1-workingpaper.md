# Session 115 Wave 1 — §VII.CK SHAPE-branch closed-class STAGE-3 promotion + forced-PMNS-texture corridor test (Results Working Paper)

**Session**: 115 | **Wave**: 1 | **Plan**: session-115-plan-w1.md | **Theme**: Stage-2 blind cross-axis verify of the §VII.CK D1–D3 closed-class obstruction (STAGE-1-CANDIDATE → STAGE-3-PERMANENT, D4-open RETAINED) + a forced A_K⋊SU(3)_R lepton-PMNS texture corridor test (surviving-vs-washed-out against observed J).

## Gate Sections

### §W1-1. S115-VIICK-STAGE2-VERIFY (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S115-VIICK-STAGE2-VERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (intra-pillar spectral-triple γ₉/orientation obstruction)
**Agent**: `gen-physicist` (PLANNER/CLOSEOUT owner; EXECUTORS = blind cross-reviewers `lizzi-spectral-functional-theorist` Axis-A × `kitaev-quantum-chaos-theorist` Axis-B)
**Hypothesis**: Two axis-distinct blind reviewers, each reading ONLY the registered §VII.CK Stage-1 entry, independently PASS each of D1/D2/D3 → §VII.CK promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT (D4-open scope qualifier RETAINED).
**Plan reference**: `sessions/session-plan/session-115-plan-w1.md` §W1-1 (Stage-2 dispatch machinery, PASS-AND set-membership criterion, reviewer-exclusion + axis-distinctness pins, substitution chain source).

**Verdict**: **PASS** (composite PASS-AND). Both blind cross-reviewers independently re-derived D1/D2/D3 from first principles and returned **PASS on all three** — 6-of-6 per-clause-per-axis booleans TRUE → composite PASS. §VII.CK promoted **STAGE-1-CANDIDATE → STAGE-3-PERMANENT** with the **D4-open scope qualifier RETAINED** (the promoted scope is the CLOSED-INTERNAL class {A_K-built ∪ Casimir-graded ∪ γ₉-traced}; the D4 right-regular SU(3)_R unconditional re-scope is the SEPARATE W2 gate `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`, NOT promoted here). Registry tag-flip applied + re-read-verified (5/5 checks True); registry SHA `c49cba61214f082c…` → `03f7fac628b4c6f0…`. No 3-tuple (VERIFY-THEOREM PASS-AND adjudication, not a directional band).

**Output Artifacts**:
- `computations/session-115/s115_viick_stage2_verify_closeout.py` — `from canonical_constants import` ✓ (line 76, `from canonical_constants import *`), `print_verdict_payload` ✓ (def + call). Exit 0.
- `computations/session-115/s115_viick_stage2_verify_closeout.npz` — stores `clauses`, `verdict_A`, `verdict_B`, `booleans_keys/vals` (6-boolean PASS-AND), `composite_pass`, `verdict`, `w3_3_landing_audit_sha256`, `registry_pre_sha`, `registry_post_sha`, `flip_verify_keys/vals`, `audit_sha256`, `content_sha256`.
- (no `.png` — adjudication gate, no plot per plan `output_artifacts.plot.optional: true`.)
- Verdict line in `computations/session-115/s115_gate_verdicts.txt`: `S115-VIICK-STAGE2-VERIFY: PASS -- value='composite_PASS=True_…6of6_PASS-AND_VIICK_STAGE-1-CANDIDATE->STAGE-3-PERMANENT_D4-open-RETAINED…' scheme=FW convention=VII-STAGE-2-CROSS-AXIS-VERIFY L_max=N/A audit_sha256=2b6ff17ec41b752225dd0d09d9ce0fc1fa213a7919e251688ec3a291d2ab8f41 content_sha256=dd4a6eadfece76a2bb914b792b7b4456663ced92411f32309a8c07b14e856cc7 schema_version=S84+` + dual-SHA companion row + 4 annotation extra-rows (blind PASS-AND tally; registry tag-flip pre/post SHA; substrate-input-orthogonality SATISFIED; D4-NOT-promoted-here pointer). Emitted via `emit_verdict` MCP tool (race-safe; 6 rows; sig_5 unique). NO 3-tuple row (correct — VERIFY-THEOREM, not [SIGN]).
- `sessions/session-115/session-115-w1-viick-verify-axis-a.md` — Axis-A (lizzi) blind synthesis; `## ` ✓, `D1`/`D2`/`D3` ✓, `PASS` ✓ (D1/D2/D3 all PASS).
- `sessions/session-115/session-115-w1-viick-verify-axis-b.md` — Axis-B (kitaev) blind synthesis; `## ` ✓, `D1`/`D2`/`D3` ✓, `PASS` ✓ (D1/D2/D3 all PASS; D4 OUT OF SCOPE).

**MCP Pre-Compute Audit** (per the knowledge-first rule; queries executed BEFORE writing the closeout):
- `trace_entity("§VII.CK")` → ONE extracted gate hit: `CF-S114-YUK-SHAPE-WALL-VII-LANDING` (the S114 W3-3 Stage-1 registration this gate verifies). Confirms §VII.CK is the recent S114 landing and **no closure already supersedes the promotion** — the Stage-2 verify is the first cross-axis adjudication of D1-D3.
- `search_knowledge("VII.CK SHAPE-Branch Homogeneity Obstruction STAGE-1-CANDIDATE")` → returns the Tier-2 #9b homogeneity-obstruction genus (SHAPE/SPLITTING branch; the `CF-S103-NO-SIGN-HANDLE` WALL lineage) + the load-bearing **"Reality is innocent"** finding (S99: the obstruction is HOMOGENEITY, not `[J,D_K]=0` — reality is the *enforcer* that forces t=1/t=2 spectra identical, the exact mechanism D2 invokes to cancel conjugation-odd C₃). Confirms the registered theorem's structural pedigree; not pre-closed at the Stage-2 level.
- Proven anchors confirmed via both reviewers' own MCP queries (recorded in their syntheses): `{γ₉,D_K}=0` (S34/S56, D1 anchor), `[J,D_K]=0` (S17a/BDI/KO-dim 6, D2 anchor), `proven_384` `t=(p−q) mod 3` (D3 generation-index anchor). All three PERMANENT; none retracted.

**Results**:

**Per-clause-per-axis verdict table** (extracted from the two blind reviewer syntheses on disk via anchored regex; refuses to default on ambiguity):

| Clause | Axis-A (lizzi) `verdict_A` | Axis-B (kitaev) `verdict_B` | PASS-AND (A∧B) | Decisive identity |
|:-------|:--------------------------|:----------------------------|:---------------|:------------------|
| **D1** `Tr[γ₉ D_K^{2k+1}] ≡ 0` | **PASS** | **PASS** | **TRUE** | `{γ₉,D_K}=0` + cyclicity ⇒ `2·Tr=0` ⇒ exact 0; per-block, L_max-INVARIANT (both axes Sage-QQ exact, odd powers up to 5/9; kitaev's even-power survivor = McKean–Singer index only ⇒ not vacuous) |
| **D2** even moment ⇒ C₂ only | **PASS** | **PASS** | **TRUE** | `[J,D_K]=0` BDI conjugate-pair `(p,q)↔(q,p)` cancels conjugation-ODD `C₃` (`C₃∝(p−q)=t`-carrier), doubles conjugation-EVEN `C₂`; both axes confirmed `C₂−C₂∘C=0`, `C₃+C₃∘C=0` over QQ |
| **D3** A_K-built ⇒ multiplicity-scalar | **PASS** | **PASS** | **TRUE** | Skolem–Noether `π(a)=⊕π_{(p,q)}(a)⊗1_{m(p,q)}` + subalgebra closure (lizzi); double-commutant `[a⊗1,1⊗b]=0` + `t(O)=0` triality-diagonal (kitaev, two independent routes); escape requires a NON-A_K leg-entangling operator |

**6-boolean PASS-AND closeout**: `A_D1 ∧ B_D1 ∧ A_D2 ∧ B_D2 ∧ A_D3 ∧ B_D3 = TRUE ∧ TRUE ∧ TRUE ∧ TRUE ∧ TRUE ∧ TRUE = TRUE` ⇒ `composite_PASS = TRUE` ⇒ **verdict = PASS**.

**4-tuple**: `(value='composite_PASS=True_A=D1:PASS,D2:PASS,D3:PASS_B=D1:PASS,D2:PASS,D3:PASS_6of6_PASS-AND_VIICK_STAGE-1-CANDIDATE->STAGE-3-PERMANENT_D4-open-RETAINED_reg_pre=c49cba61214f082c_reg_post=03f7fac628b4c6f0_flip_verify=True', scheme=FW, convention=VII-STAGE-2-CROSS-AXIS-VERIFY, L_max=N/A)`. `L_max=N/A` is correct: D1 is a PER-BLOCK exact-zero, L_max-INVARIANT (the identity holds at every truncation; the W3-3 reproduction's operational-L=10 with 4 pure-symmetric corners contributing 0 by the same per-block argument does NOT weaken it).

**Stage-2 protocol pre-flight confirmation** (`joint-theorem-promotion.md §"Stage 2"` audit items 1-6):
1. **PARALLEL dispatch** — both reviewers dispatched in the same batch (tasks #4, #5 completed in parallel); NOT sequential.
2. **Axis-distinctness** — Axis-A = lizzi (NCG / spectral-functional axis), Axis-B = kitaev (quantum-chaos / spectral-statistics / operator-algebra axis). Distinct axes; neither is the other's specialty.
3. **Non-author + downstream-inheritance-clean** — the YUKSHAPE Stage-0 authors `connes-ncg-theorist` (Reading-A pole) + `paasch-mass-quantization-analyst` (Reading-B pole) are EXCLUDED; neither reviewer is an author or a downstream-inheritance successor of the `ws-s113-7-yukshape` reading-path (both reviewers' blindness attestations confirm they did NOT open the workshop transcript `5cd77110ea2d…`).
4. **W2/W3-reviewer exclusion (disjoint-pair)** — `volovik` (W2 Axis-B) + `transit-dynamics-theorist` (W3 planner) excluded HERE so the W1-1 ↔ W2-1 reviewer pairs are DISJOINT (W2-1's pinned pair is {spectral-geometer/lizzi-side, volovik}; W1-1 takes {lizzi, kitaev} ⇒ 4 distinct reviewers, no overlap).
5. **JOINT-clause PASS-AND** — D1/D2/D3 each PASS-AND'd across both verdicts (logical AND, not OR); all three TRUE.
6. **Reviewer-machinery non-self-authorship** — D1/D2/D3 are NCG-axiomatic identities (`{γ₉,D_K}=0` / `[J,D_K]=0` / Skolem–Noether), NOT a reviewer-private decision procedure; audit item 6 SATISFIED.

**Substrate-input-orthogonality** (`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`): SATISFIED. The D1 machine-exact artifact (W3-3 npz `s114_yuk_shape_wall_vii_landing.npz`) was read by EXACTLY ONE reviewer — Axis-A (lizzi), who owns the supertrace clause; Axis-B (kitaev) re-derived D3 from the registered text + the Skolem–Noether operator algebra WITHOUT the npz (kitaev's blindness attestation explicitly states "did NOT read the D1 W3-3 npz artifact"). The data consumed by ≥1 observable is loaded by only ONE cross-reviewer ⇒ the predicate `∃ obs_i loaded by exactly one reviewer` holds ⇒ **structural-INPUT independence** (not merely structural-output-type independence) ⇒ **NO substrate-input-overlap caveat owed**. This is the structural CEILING for the procedural-floor independence guarantee.

**Substitution chain (logical-AND monotonicity; per `math-scripts.md §"Double-Check Logic Before Compute"` + plan §W1-1 substitution_chain)** —
- **Def 1**: `composite_PASS := (verdict_A(D1)=PASS ∧ verdict_B(D1)=PASS) ∧ (verdict_A(D2)=PASS ∧ verdict_B(D2)=PASS) ∧ (verdict_A(D3)=PASS ∧ verdict_B(D3)=PASS)` [`joint-theorem-promotion.md §"Stage 2"` PASS criterion: JOINT clauses PASS-AND'd, logical AND not OR].
- **Def 2**: STAGE-3-PERMANENT eligibility := `composite_PASS` AND (Stage-2 dispatch satisfies audit items 1-6, confirmed above).
- **Def 3**: D4-open RETAINED := the promotion scope is the registered CLOSED class {A_K-built ∪ Casimir-graded ∪ γ₉-traced} (D1-D3); the D4 right-regular SU(3)_R unconditional re-scope is NOT promoted here (separate gate).
- **Substitute** (the 6 on-disk booleans): `composite = (T∧T) ∧ (T∧T) ∧ (T∧T)`.
- **Simplify**: `composite = T ∧ T ∧ T = TRUE` ⇒ PASS (promotion fires, D4-open).
- **Direction**: the promotion is **MONOTONE in the conjunction** — adding a FAIL or INFO on ANY of the 6 booleans STRICTLY blocks STAGE-3 (it cannot promote on a 5-of-6 partial). This is the `joint-theorem-promotion.md` anti-shared-context discipline, NOT a magnitude band: the agreement counts as evidence ONLY because both reviewers were blind (neither read the workshop), so their independent PASS on each JOINT clause is structurally-independent confirmation per `epistemic-discipline.md §"What Counts as a Result"`.
- **Conclusion**: §VII.CK → STAGE-3-PERMANENT (D4-open scope qualifier RETAINED), since both blind reviewers independently PASS all three of D1/D2/D3.

**Registry tag-flip (STAGE-1-CANDIDATE → STAGE-3-PERMANENT, D4-open RETAINED; single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture"`)** — `build_promotion_text → write_atomic_with_fsync → re-read + verify_section_matches → exactly ONE emit`. Three flip targets, each matched as a UNIQUE literal substring (count==1 asserted, else HARD error — the flip cannot silently no-op or double-apply):
- **T1** body header sentence (`### §VII.CK …` block, ~line 22422): `(STAGE-1-CANDIDATE, S114 W3-3 …)` → `(STAGE-3-PERMANENT [D4-open scope qualifier RETAINED; S115 W1-1 Stage-2 PASS-AND], S114 W3-3 …)`.
- **T2** the STAGE TAG line (~22424): `**STAGE TAG: STAGE-1-CANDIDATE**` → `**STAGE TAG: STAGE-3-PERMANENT**` + the D4-open scope qualifier + the Stage-2 provenance (`joint-theorem-promotion.md §"Stage 3 — Permanent Registration"`).
- **T3** master-index row 173: `…the SHAPE handle is external (…); STAGE-1-CANDIDATE; intra-pillar GEOMETRIC…` → `…; STAGE-3-PERMANENT (S115 W1-1 `S115-VIICK-STAGE2-VERIFY` Stage-2 blind cross-axis PASS-AND, Axis-A lizzi × Axis-B kitaev, D1/D2/D3 PASS/PASS/PASS each axis; D4-open RETAINED); intra-pillar GEOMETRIC…`.

Post-flip `verify_section_matches` (ALL 5 True required for the AFTER-pattern composite): `body_header_stage3=True`, `stage_tag_stage3=True`, `master_index_stage3=True`, `d4_open_scope_retained=True` (the literal `class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}` survives), `no_residual_stage1_tag=True` (no `**STAGE TAG: STAGE-1-CANDIDATE**` for §VII.CK remains). **Runtime registry SHA: pre-flip `c49cba61214f082c…` → post-flip `03f7fac628b4c6f0…`.** The §VII.BL co-author cross-reference at registry line 21291 (baptista's designated annotation, which already anticipated "STAGE-1-CANDIDATE → STAGE-3-PERMANENT-UNCONDITIONAL upgrade owed to the FUTURE Stage-2 gate") was NOT edited — it describes the *future-pending D4-UNCONDITIONAL* upgrade (W2), not the §VII.CK D1-D3 tag itself, and it is baptista's sole-writer §VII.BL annotation.

**Dual-SHA** — `audit_sha256=2b6ff17ec41b752225dd0d09d9ce0fc1fa213a7919e251688ec3a291d2ab8f41` (over the ordered input-pin map {registered_entry_anchor_body, W3_3_landing_audit_sha256, reviewer_axis_A_verdict, reviewer_axis_B_verdict, pinmap} + per-gate identity keys, per plan §W1-1 `audit_discriminators`), `content_sha256=dd4a6eadfece76a2bb914b792b7b4456663ced92411f32309a8c07b14e856cc7` (closeout script bytes). Computed at runtime from the closure — never hardcoded; sig_5-unique against all prior session lines.

**Solution-space consequence** — §VII.CK is now a PERMANENT structural wall over the closed class {A_K-built ∪ Casimir-graded ∪ γ₉-traced}: the fermion-mass generation SHAPE texture is permanently external to the substrate's A_K/Casimir/γ₉-trace functional class — one more internal corridor CLOSED. The lizzi Axis-A contribution sharpens this: the obstruction is **FUNCTIONAL-INDEPENDENT** (it holds identically under cutoff / zeta / anomaly-derived spectral functionals — there is no "switch the spectral functional" escape, because D1/D2/D3 live in the symmetry algebra `(γ₉, J, A_K)`, not in any spectral moment). The kitaev Axis-B contribution sharpens it as a **symmetry-forced selection rule** (three hard symmetries — `{γ₉,D_K}=0` chiral/BDI, `[J,D_K]=0` reality, `t=(p−q) mod 3` Z₃ center — each independently forbid a different functional sub-class from carrying a sign-changing per-generation handle; not a chaos/scrambling bound). Both blind axes independently locate the only escape as a NON-A_K leg-entangling operator — the `ε_LX` channel (§VII.BL) and its right-regular `R_{E_α}` avatar (the D4 door, owed to W2). The D1-D3 wall correctly does NOT close D4; the D4-open scope qualifier is RETAINED.

**Substrate framing** — GEOMETRIC (intra-pillar, spectral-triple γ₉/orientation axis). The substrate IS the homogeneous Jensen-deformed spectral triple `(A_K, H_K, D_K, γ₉, J)`, `A_K = ℂ⊕ℍ⊕M₃(ℂ)`, KO-dim 6. Direction (never inverted): `D_K eigenvalues + {γ₉,D_K}=0 (D1) + [J,D_K]=0 conjugation-evenness (D2) + Skolem–Noether leg-membership (D3) → every A_K-built form is generation-blind on the multiplicity leg ℂ^{m(p,q)} → the fermion-mass SHAPE texture is external (the ε_LX channel that also carries the §VII.BL magnitude)`. The Stage-2 cross-axis verify is the constructive pathway (`joint-theorem-promotion.md`) by which a substrate-internal structural identity becomes a PERMANENT wall — verified to survive blind first-principles re-derivation on TWO independent axes — not a methodology artifact.

---

### §W1-2. S115-LEPTON-PMNS-FORCED-TEXTURE (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S115-LEPTON-PMNS-FORCED-TEXTURE`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (PMNS mixing / generation texture — representation-theoretic content of D_K)
**Agent**: `neutrino-detection-specialist` (PMNS owner / EXECUTOR; gen-physicist contributes the A_K⋊SU(3)_R right-regular circulant U_R)
**Hypothesis**: The A_K⋊SU(3)_R right-regular circulant on the LEPTON sector, with the ℂ⊕ℍ charged-lepton-vs-neutrino sector-asymmetry imposed, forces a tri-maximal neutrino texture whose physical PMNS Jarlskog (after the charged-lepton correction U_mix=U_L†U_R) either SURVIVES near observed J≈0.033 (zero-parameter corridor prediction) or is WASHED OUT (symmetric-limit coincidence).
**Plan reference**: `sessions/session-plan/session-115-plan-w1.md` §W1-2 (forced-circulant + coset-diagonal machinery pins, J_PMNS external observational anchors, M₃(ℂ) quark negative control, substitution chain).

**Verdict**: **FAIL** (forced-and-**WASHED-OUT**). Composite collapse of the [SIGN] 3-tuple `sign=PASS · magnitude=FAIL · regime=VALID` → FAIL per `.claude/rules/gate-verdicts.md` composite rule (`magnitude=FAIL ∧ regime=VALID ⇒ composite=FAIL`). The forced tri-maximal lepton texture's physical PMNS Jarlskog `J_forced_corrected = 1/(6√3) = 0.0962250` sits at `dev = 1.924773` (ratio 2.924773×) ABOVE the observed value and OUTSIDE the NuFIT 5.2 / PDG 2024 normal-ordering 3σ Jarlskog band `[0.0086, 0.0331]`. The ℂ⊕ℍ-forced coset-diagonal charged-lepton correction CANNOT repair the gap — by the rephasing-invariance of the Jarlskog, a coset-diagonal `U_L = diag(e^{iα_k})` leaves J at the maximal value EXACTLY (`J_scan_spread = 8.33e-17` across 25 coset-diagonal phase samples). The named external `A_K⋊SU(3)_R` corridor's forced lepton residue is observationally excluded — it is a symmetric-limit coincidence, NOT a surviving zero-parameter PMNS observable.

**Output Artifacts**:
- `computations/session-115/s115_lepton_pmns_forced_texture.py` — `from canonical_constants import` ✓ (line 86), `print_verdict_payload` ✓ (def + call). Exit 0.
- `computations/session-115/s115_lepton_pmns_forced_texture.npz` — stores `U_R`, `U_L_phys`, `U_mix`, `U_mix_quark`, `J_bare`, `J_exact`, `J_forced_corrected`, `magsq_UR`, `magsq_Umix`, `dev`, `ratio`, `quark_ckm_ratio`, `in_band`, `J_PMNS_OBS/_LOW/_HIGH`, `J_scan`, `J_scan_spread`, `neg_ctrl_resid`, `neg_ctrl_pass`, `J_quark`, 3-tuple fields.
- `computations/session-115/s115_lepton_pmns_forced_texture.png` — (a) `|U_mix,ij|²` tri-maximal heatmap; (b) forced J vs PMNS 3σ band number line; (c) J flatness across coset-diagonal U_L phases + negative-control residual.
- Verdict line in `computations/session-115/s115_gate_verdicts.txt`: `S115-LEPTON-PMNS-FORCED-TEXTURE: FAIL -- value='dev=1.924773_…' … audit_sha256=66ffd63c94af0434d73b7e90ff45c05bcf7e679b28b712cd5587128a2faae906 content_sha256=509ea799d1ce36aca4ad900015656a0111fd38bed5c5b8aeb9b6ad1d04c77f4d schema_version=S84+` + dual-SHA companion row + [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + 3 annotation extra-rows (rephasing-invariance, negative-control, registry cross-check). Emitted via `emit_verdict` MCP tool (race-safe; 6 rows).

**MCP Pre-Compute Audit** (per the knowledge-first rule; queries executed BEFORE writing the script):
- `search_knowledge("VII.CK D4-disposition forced-texture tri-maximal Jarlskog circulant PMNS")` → returned the historical PMNS extraction lineage (S29/S32/S35/S36/S52/S96 `pmns_*` scripts + gates PMNS-3/PMNS-36/PMNS-52/CORRECTED-35); NO prior gate computes the **forced crossed-product corridor** lepton Jarlskog against the observed band ⇒ NOT pre-closed, this gate is the first.
- `get_constant("J_PMNS")` → **not found** ✓ (confirms J_PMNS is an EXTERNAL anchor, NOT a framework constant; hardcoded as `# (local)` observational pin with NuFIT 5.2 / PDG 2024 NO citation per `substrate-first-canonical-sourcing.md §(i)`).
- `get_constant("delta_CP_PMNS_substrate")` → `0.0` (S100b, S99-W3-SEESAW-SUMMNU `δ_CP∈{0,π}`) — the SEPARATE substrate seesaw δ_CP prediction; distinct from this external-corridor test.
- `get_constant("J_CP_PDG")` → `3.08e-05` (S100a, PDG 2024 CKM global fit) — the quark-CKM Jarlskog used as the negative-control reference (~3124× quark falsification).
- `trace_entity("VII.CK forced-texture lepton PMNS crossed-product")` → no trace (the §VII.CK landing is the very recent S114 W3-3 registration, not yet in the extracted index); cross-checked the values directly against `permanent-results-registry.md §VII.CK` D4-disposition annotation (body line ~22460): `|U_ij|²=1/3`, `arg(w)=2π/3`, `J=1/(6√3)=0.0962`, quark ~3124×, lepton ~2.9× — all reproduced from scratch and asserted-equal in-script.

**Results**:

| Quantity | Value | Notes |
|:---------|:------|:------|
| `J_bare` (numeric, U_R=DFT₃) | `0.09622504` | = exact `1/(6√3)` to machine precision (\|num − exact\| < 1e-12) |
| `J_exact = 1/(6√3) = √3/18` | `0.09622504` | exact algebraic number (NOT rational) |
| `J_forced_corrected` (U_mix = U_L†U_R) | `0.09622504` | coset-diagonal U_L leaves J unchanged |
| `J_PMNS,obs` (NuFIT 5.2 / PDG 2024 NO) | `0.0329` | EXTERNAL `# (local)` anchor |
| 3σ Jarlskog band `[J_low, J_high]` | `[0.0086, 0.0331]` | NuFIT 5.2 NO 3σ (low side → 0 as δ_CP→0/π; high capped by measured angles) |
| `dev = \|J_fc − J_obs\|/J_obs` | `1.924773` | matches plan pre-reg `dev_bare=1.92477` |
| `ratio = J_fc/J_obs` | `2.924773` | matches plan pre-reg `ratio=2.92477` |
| `in_band` | **False** | J_forced = 0.0962 ≫ band upper edge 0.0331 |
| `\|U_R,ij\|²` max dev from 1/3 | `1.11e-16` | tri-maximal confirmed |
| coeff-independence (arbitrary circulant \|eigvec\|² dev) | `3.89e-16` | texture coefficient-INDEPENDENT (any c_a) |
| **J spread across coset-diagonal U_L (25 samples)** | **`8.33e-17`** | **rephasing-invariance — the WASHED-OUT decider** |
| quark-CKM ratio | `3124.2×` | matches registry "~3124×" |
| neg-control `\|U_mix_quark − I\|_F` | `5.17e-16` < 1e-12 ✓ | two M₃(ℂ) circulants ⇒ U_mix = I ≠ CKM |
| neg-control `J_quark` | `0.0` | identity ⇒ zero CP (zero quark mixing) |
| registry cross-checks (\|U_ij\|², J, arg w) | `True / True / True` | reproduced from scratch, asserted-equal |

**Substitution chain (with substituted numbers; per `math-scripts.md §"Double-Check Logic Before Compute"`)** —
- **Def 1**: `J_forced(bare)` = tri-maximal circulant Jarlskog = `1/(6√3)` [B2 Sage-exact; registry §VII.CK D4-disposition].
- **Def 2**: `J_PMNS,obs ≈ 0.0329` [NuFIT 5.2 / PDG 2024 NO best fit; EXTERNAL anchor].
- **Def 3**: `U_mix = U_L†U_R`, `U_R` = right-regular circulant (neutrino) = DFT₃, `U_L` = coset-diagonal charged-lepton rotation [W-2 Q3: one-circulant-one-coset-diagonal ⇒ tri-maximal; two-circulant ⇒ identity].
- **Def 4**: `dev = |J_forced_corrected − J_PMNS,obs| / J_PMNS,obs`.
- **Substitute** (symmetric-limit, U_L = coset-identity): `J_forced_corrected = 1/(6√3) = 0.09622504`; `dev_bare = |0.09622504 − 0.0329| / 0.0329 = 1.924773`; `ratio = 2.924773`. ✓ (matches the script's computed `dev=1.924773`, `ratio=2.924773` to 6 sig figs).
- **Direction**: `dev_bare = 1.92 ≫ 0` ⇒ the BARE tri-maximal J is `2.92×` the observed PMNS J — OUTSIDE the 3σ Jarlskog band. The PHYSICAL charged-lepton correction (the load-bearing physics) is then computed: the ℂ⊕ℍ sector-asymmetry forces `U_L` **coset-diagonal**, i.e. a diagonal phase matrix `diag(e^{iα_k})`. The Jarlskog is the UNIQUE rephasing-invariant CP measure: each generation index appears once unconjugated and once conjugated in the quartet `U_{00}U_{11}U*_{01}U*_{10}`, so the row phases of a diagonal `U_L` cancel exactly. Hence `J_forced_corrected = J_bare` for ANY coset-diagonal `U_L` — demonstrated numerically by the 25-sample phase scan (`J_scan_spread = 8.33e-17`, `|U_mix,ij|²` dev `3.89e-16`).
- **Conclusion**: the SIGN of `(J_forced_corrected − J_obs)` is POSITIVE (overshoot, predicted) and `dev = 1.92 ≫ band` ⇒ **WASHED-OUT**. The coset-diagonal correction structurally cannot move J off maximal, so no charged-lepton rotation in the forced ℂ⊕ℍ class repairs the gap. (The registry's own "lepton-PMNS RESONANT-CONDITIONAL ~2.9× from observed" is exactly the bare-limit shadow of this gate — here CONFIRMED as the full physical disposition.)

**[SIGN] 3-tuple** — `sign_verdict=PASS` (computed `J_fc − J_obs = +0.0633 > 0`, matching the pre-registered Step-4 prediction of a positive overshoot); `magnitude_verdict=FAIL` (`J_fc = 0.0962` outside the 3σ band `[0.0086, 0.0331]`); `regime_verdict=VALID` (the coset-diagonal construction is self-consistent throughout — J flat to machine precision across all coset-diagonal phases, no regime breakdown). Composite = **FAIL** (`magnitude=FAIL ∧ regime=VALID ⇒ FAIL`).

**Dual-prior reallocation** — pre-registered prior: Track A (surviving) 0.15 / Track B (washed-out) 0.85; discriminator: FAIL (outside band) → reallocate ~0.9 to Track B. Outcome **FAIL** ⇒ posterior ≈ **0.9 Track B (forced-and-WASHED-OUT)** / 0.1 Track A. The lepton resonance DOWN-TAGS to a symmetric-limit coincidence; the named crossed-product corridor closes the §VII.CK D4 door as external-AS-A-COUPLING WITHOUT a surviving lepton observable (as it is ~3124× excluded for the quarks). No live falsifier row results (Track-A surviving would have routed a mack falsifier-inventory row; the washed-out outcome does not).

**Solution-space consequence** — the named external `A_K⋊SU(3)_R` crossed-product corridor's forced texture is observationally excluded for BOTH the quarks (`U_mix → I`, ~3124× CKM) AND the leptons (tri-maximal J = 2.92× observed PMNS, coset-diagonal correction rephasing-invariant). This is the expected dual-prior Track-B outcome — informative (it closes the corridor's phenomenological shadow), NOT an agent failure: the D4 door is decided external-as-a-coupling on structural grounds (the W2 gate) regardless, and this gate confirms the corridor leaves no surviving zero-parameter lepton-mixing observable.

**Dual-SHA** — `audit_sha256=66ffd63c94af0434d73b7e90ff45c05bcf7e679b28b712cd5587128a2faae906`, `content_sha256=509ea799d1ce36aca4ad900015656a0111fd38bed5c5b8aeb9b6ad1d04c77f4d`. **4-tuple** — `(value='dev=1.924773_ratio=2.924773_Jforced=0.0962250_…WASHED-OUT…', scheme=FW, convention=FORCED-CROSSED-PRODUCT-TEXTURE-LEPTON, L_max=N/A)`.

**Substrate framing** — PARTICLE (representation-theoretic content of D_K). Direction (never inverted): D_K multiplicity leg + SU(3)_R right-regular action → forced Z₃-circulant on the neutrino sector → ℂ⊕ℍ sector-asymmetry (charged leptons coset-diagonal, neutrinos circulant) → physical `U_mix = U_L†U_R` → PMNS Jarlskog, tested against the observed lepton-mixing value. The negative control is the substrate's own statement that the quark chiralities SHARE the M₃(ℂ) leg ⇒ two circulants ⇒ `U_mix → I ≠ CKM`. This is a CONTINGENCY-pinned test of the external corridor's residue — NOT a claim that the substrate INTERNALLY predicts the PMNS (the §VII.CK genus proves the SHAPE handle is external).

---

## Wave 1 Synthesis (team-lead)

**Per-gate verdict roll-up**

| Gate | Verdict | One-line |
|:-----|:--------|:---------|
| W1-1 `S115-VIICK-STAGE2-VERIFY` | **PASS** | 6-of-6 PASS-AND (Axis-A lizzi D1/D2/D3 = PASS/PASS/PASS ⊥ Axis-B kitaev D1/D2/D3 = PASS/PASS/PASS, blind, independent Sage-QQ re-derivations) → §VII.CK STAGE-1-CANDIDATE → **STAGE-3-PERMANENT** (D4-open scope qualifier RETAINED) |
| W1-2 `S115-LEPTON-PMNS-FORCED-TEXTURE` | **FAIL** | forced-and-**WASHED-OUT**: bare tri-maximal `J=0.0962` is `2.92×` the observed PMNS `J≈0.0329`, outside the 3σ band `[0.0086,0.0331]`; the ℂ⊕ℍ coset-diagonal charged-lepton correction is rephasing-invariant (`J_scan_spread=8.33e-17`) ⇒ cannot move J — symmetric-limit coincidence, no surviving zero-parameter lepton observable |

**§VII.CK promotion outcome.** The Stage-2 two-agent blind cross-axis independent verify (`joint-theorem-promotion.md` §"Stage 2") returned a clean 6-of-6 PASS-AND. Both reviewers re-derived D1 (γ₉-graded odd-power supertrace ≡ 0 by `{γ₉,D_K}=0`), D2 (γ₉-even moment carries C₂ only, not the generation-resolving cubic C₃, by `[J,D_K]=0` BDI reality), and D3 (every A_K-built form is multiplicity-scalar by Skolem–Noether leg-membership) **from first principles, blind to the YUKSHAPE workshop transcript** — so the agreement is structurally independent (counts as evidence per `epistemic-discipline.md`). Two protocol strengths beyond the registered claim: (i) kitaev (Axis-B) stress-tested the *vacuity* failure mode and confirmed D1's odd-power zero is symmetry-forced (the McKean–Singer index `dim₊−dim₋=1` survives at k=0), not a trivial γ₉-trace identity; (ii) lizzi (Axis-A) re-derived D1 over **powers 1–9 on a genuine 6-dim block** where the registered D1 npz checked only powers 1,3 on a 2×2 toy — the blind verify *strengthened* the evidence base. The registry tag-flip is on disk (3 targets: body header L22422, STAGE TAG L22424, master-index row 173; runtime SHA `c49cba61 → 03f7fac6 → 06d7162a` incl. the closeout's in-session prose-coherence fix; 0 residual STAGE-1-CANDIDATE markers).

**Lepton-corridor disposition.** W1-2 closed the named external `A_K⋊SU(3)_R` crossed-product corridor's lepton residue as **washed-out** — the expected dual-prior Track-B outcome (posterior ≈ 0.9). The structural reason is exact: a coset-diagonal `U_L=diag(e^{iα_k})` is a pure rephasing and the Jarlskog is rephasing-invariant, so the bare tri-maximal `J=1/(6√3)` *is* the physical prediction, `2.92×` too large. The corridor is now observationally excluded for BOTH quarks (`U_mix→I`, ~3124× CKM, neg-control residual `5.2e-16`) and leptons. No live falsifier row results.

**W1 → W2 decision-point state.** **W1-1 = PASS ⇒ W2 (`S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`) is UNBLOCKED** — it runs the full Stage-2 D4-external cross-axis verify (spectral-geometer × volovik), NOT the mechanical PRE-REG-INC closure branch. The two §VII.CK promotions land with disjoint reviewer pairs: W1-1 `{lizzi, kitaev}` ⊥ W2-1 `{spectral-geometer, volovik}` (4 distinct reviewers, §EVOI.BF cross-reviewer-independence).

### Effected In-Session (NON-MATH — completed before W2 dispatch)

- [x] §VII.CK registry tag-flip STAGE-1-CANDIDATE → STAGE-3-PERMANENT (D4-open RETAINED) — executed by the W1-1 closeout gate as its load-bearing output (3 registry targets) — `sessions/permanent-results-registry.md:22422,22424` + master-index row 173 — verified on disk (`reg_post=03f7fac6`, 0 residual STAGE-1-CANDIDATE).
- [x] STAGE-TAG-paragraph prose-coherence fix (stale "FUTURE gate" → "EXECUTED at S115 W1-1") — executed by the closeout in-session per `feedback_fix-in-session-never-defer.md` — `sessions/permanent-results-registry.md` (post-fix SHA `06d7162a`); baptista's §VII.BL D4-pathway cross-ref (L21291) correctly left untouched (sole-writer boundary + still-pending D4-UNCONDITIONAL).
- No orphaned orchestrator-direct non-math items: the FUNCTIONAL-INDEPENDENT structural strengthening (Axis-A) is recorded in `session-115-w1-viick-verify-axis-a.md` + Constraint-Map below; it is a completed structural finding, not a registry hygiene edit owed. Capstone-hygiene 5-question gate (this session touches the permanent-results register) runs at session-close in the W3 housekeeping ledger.

## Carry-Forward Computations

### CF-S116-D2-ANOMALY-IDENTIFICATION — Is the cubic Casimir C₃ the SU(3) cubic gauge-anomaly invariant? (OPTIONAL, low-EVOI)

Surfaced by the Axis-B (kitaev) blind verify as a structural-strengthening question, NON-gating on the already-PERMANENT §VII.CK promotion.

| Field | Spec |
|:------|:-----|
| **What** | Test whether the conjugation-odd cubic Casimir `C₃ ∝ (p−q)` (the unique generation-resolving su(3) invariant, forbidden to the γ₉-even moment by D2) coincides — up to overall normalization — with the SU(3) cubic gauge-anomaly invariant `A(R) = Tr_R({T^a,T^b}T^c)/Tr_fund(...)`. |
| **Inputs** | `C₃(p,q)` on the Peter-Weyl irreps (closed form `(p−q)(p+2q+3)(2p+q+3)/...`); the cubic-anomaly coefficients `A(p,q)`; no new substrate compute (both are closed-form SU(3) rep-theory). |
| **Gate** | INFO/PASS: PASS iff `C₃(R)/A(R) = const` across a basis of irreps `{(1,0),(2,0),(1,1),(3,0),...}` to `< 1e-10` (coincide up to normalization); INFO otherwise (they are distinct cubic invariants). |
| **Effort** | ~0.25 wave (closed-form rep-theory ratio check; Sage-QQ exact). |

*(No other math carry-forwards: W1-1 closed in-session as STAGE-3-PERMANENT; W1-2's washed-out FAIL closes the lepton corridor with no live falsifier. The numerical D2-Casimir-projection corroboration kitaev also suggested is NOT carried — it numerically re-confirms an already-PERMANENT structural result, which is corroboration-hygiene, not genuine new future work.)*

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-06-24 | §VII.CK SHAPE-Branch Homogeneity Obstruction (D1–D3 closed-internal class) | STAGE-1-CANDIDATE | **STAGE-3-PERMANENT** (D4-open RETAINED) | W1-1 6-of-6 Stage-2 blind PASS-AND (lizzi × kitaev) |
| 2026-06-24 | §VII.CK D1/D2/D3 regulator-dependence | (unstated) | **FUNCTIONAL-INDEPENDENT** (regulator-invariant under cutoff/zeta/anomaly-derived) | Axis-A (lizzi) structural finding: the obstructions live in the symmetry algebra (γ₉, J, A_K), not in any spectral moment ⇒ no regularization-scheme escape |
| 2026-06-24 | Lepton-PMNS forced-texture corridor (`A_K⋊SU(3)_R` external residue) | RESONANT-CONDITIONAL (~2.9× from observed, bare-limit shadow) | **WASHED-OUT** (symmetric-limit coincidence; coset-diagonal correction rephasing-invariant) | W1-2 FAIL: physical `J=2.92×` observed PMNS, structurally unrepairable; corridor excluded for quarks AND leptons |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Reviewer-md | Size |
|:-----|:-------|:------------|:------------|:------------|:-----|
| W1-1 | `s115_viick_stage2_verify_closeout.py` (27.2 KB) | `s115_viick_stage2_verify_closeout.npz` (5.6 KB) | — (adjudication gate) | `session-115-w1-viick-verify-axis-a.md` (22.2 KB), `session-115-w1-viick-verify-axis-b.md` (21.3 KB) | — |
| W1-2 | `s115_lepton_pmns_forced_texture.py` (29.5 KB) | `s115_lepton_pmns_forced_texture.npz` (8.2 KB) | `s115_lepton_pmns_forced_texture.png` (92.9 KB) | — | — |
| (verdicts) | `computations/session-115/s115_gate_verdicts.txt` — 2 canonical lines (W1-1 PASS, W1-2 FAIL), 2 distinct audit_sha256, W1-2 [SIGN] 3-tuple row | | | | |
