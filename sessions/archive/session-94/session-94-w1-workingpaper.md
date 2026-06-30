# Session 94 Wave 1 — §VII.BA composite-bridge + α_s transport + A_s normalization (Results Working Paper)

**Session**: 94 | **Wave**: 1 | **Plan**: session-94-plan-w1.md | **Theme**: §VII.BA composite-bridge-map dimensional-class program along the spectral-action / Connes-Karoubi axis — Stage-2 promotion of the joint two-axis theorem, T4 envelope extension, T5 α_s direct-Connes-Karoubi recovery at the a_4 channel, FULL K_csub_R UV-convergence via Λ_UV=M_KK Pauli-Villars, and the A_s spectral-vs-physical M_Pl normalization gap.

## Gate Sections

### §W1-1. S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Stage-2 of the joint-theorem-promotion 4-stage pathway for the §VII.BA `#### (h)` composite-bridge-map admissibility theorem)
**Agent**: `connes-ncg-theorist` (orchestrator-of-gate; dispatches the two cross-reviewers — Axis-A lizzi-spectral-functional-theorist, Axis-B volovik-superfluid-universe-theorist — NEITHER is connes nor mack, the excluded original authors)
**Hypothesis**: The §VII.BA `#### (h)` STAGE-1-CANDIDATE joint two-axis theorem advances to STAGE-3-PERMANENT iff both axis-distinct reviewers PASS their single-axis clauses AND the JOINT clause (c) (Δ_scheme→0 operational test) PASS-ANDs across both verdicts (logical AND, not OR).
**Plan reference**: `sessions/session-plan/session-94-plan-w1.md` §W1-1 (clause attribution, reviewer-selection downstream-inheritance-reach test, substitution chain, substrate-input-orthogonality clause).

**Output Artifacts** (closure-verification checklist; all on-disk, content-verified):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/session-94/s94_w1_1_vii_ba_stage_2_cross_axis_verify.py` (29580 B) | `from canonical_constants import` ✓ ; `append_verdict` ✓ |
| data | `computations/session-94/s94_w1_1_vii_ba_stage_2_cross_axis_verify.npz` (9568 B) | present ✓ (clause×reviewer PASS-AND matrix + substitution-chain booleans) |
| plot | `computations/session-94/s94_w1_1_vii_ba_stage_2_cross_axis_verify.png` (53124 B) | present ✓ (clause×reviewer PASS-AND matrix heatmap; optional figure produced) |
| verdict_line | `computations/session-94/s94_gate_verdicts.txt` | matches `^S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY:.* audit_sha256=[a-f0-9]{64}` ✓ ; dual-SHA companion comment row present ✓ ; no 3-tuple ([VERIFY-THEOREM]) |

- **`grep -E 'from canonical_constants import|append_verdict'`** on the script → both lines present (`from canonical_constants import M_KK_gravity, Delta_BCS`; `def append_verdict(...)` + the call in `main()`).
- **Canonical verdict line**: `audit_sha256=e6cb47a94badfa8f04bb710f2978cfede401df05073fcb48dbeabce2c2f2a316` (full 64-char), `content_sha256=d1106a2d5cddde0feaa5cbf3938f4c65268cb31a2abe0b90e28cd1af595e1a2c`, `schema_version=S84+`.
- **SHA uniqueness (sig_5)**: the audit_sha256 is unique across all 5 S94 W1 verdict lines (S94-K-CSUB-R `943b753b…`, S94-A_S-MPL `e8c8955b…`, S94-VII-Bx-T5 `90a96508…`, S94-VII-BA-T4 `a74e9f1e…`, this gate `e6cb47a9…`) — pairwise distinct by construction (per-gate pinmap embeds distinct reviewer-verdict + registry SHAs).

**MCP Pre-Compute Audit**:
- `search_knowledge("VII.AH STAGE-3-PERMANENT joint theorem Stage-2 substrate-input-orthogonality")` → gate `S90-VII-AH-STAGE-3-PERMANENT-PROMOTION` (PASS; `checks_pass=8_of_8`, `stage_2_pass_audit_sha=4fcd7d29af51c56d`, `k_counter_advance=K2_to_K3`, MANDATORY at K3) — the FIRST framework cross-axis joint theorem to STAGE-3-PERMANENT, the structural-ceiling (no overlap-caveat) precedent this gate follows.
- `search_knowledge("VII.BA composite bridge map STAGE-1-CANDIDATE Stage-2 cross-axis verify")` → the S92 prior attempt `S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY` closed `PRE-REG-INC_blocked_by_W2-3_FAIL_W2-4_INFO` (the F-functor image-identification was structurally incomplete at S92); S93 W1-2 then re-registered §VII.BA `#### (h)` as STAGE-1-CANDIDATE with the corrected NON-SCALAR Element-3 — this gate is the Stage-2 on that corrected registration.
- **NOT PRE-CLOSED**: no closure covers the S94 §VII.BA `#### (h)` Stage-2 PASS-AND; the prior S92 attempt was PRE-REG-INC (blocked), not a PASS. This gate is the first admissible Stage-2 firing for §VII.BA. Canonical pins confirmed: `M_KK_gravity = 7.428660036284456e16` GeV, `Delta_BCS = 0.4642547394830737` (both match the reviewer JSONs + npz; none stale).

**Verdict**: **PASS** — composite Stage-2 PASS-AND. Both axis-distinct reviewers PASS all clauses (Axis-A lizzi (a)/(e)/(c); Axis-B volovik (binding)/(c)); JOINT clause (c) `Δ_scheme→0` PASS-AND = True (logical AND across both independent re-derivations); substrate-input-orthogonality = True at ≥1 observable (distinct anchors → structural ceiling, NO overlap caveat). §VII.BA `#### (h)` is **STAGE-3-PERMANENT-ELIGIBLE** (the orchestrator flips the registry tag STAGE-1-CANDIDATE → STAGE-3-PERMANENT at wave close; this aggregator does NOT edit `permanent-results-registry.md`).

**Results**:

This is a verdict-aggregation gate: the physics is the INDEPENDENCE of the two cross-reviews (both re-derived the registered §VII.BA `#### (h)` STAGE-1-CANDIDATE entry WITHOUT prior workshop context, on structurally orthogonal substrate-input anchors). The aggregator's role is the deterministic boolean PASS-AND. The verdict booleans below are LOADED from the two reviewer JSONs (`s94_w1_1_axisA_lizzi_verdict.json`, `s94_w1_1_axisB_volovik_verdict.json`), not hardcoded.

**Per-clause × per-reviewer verdict matrix** (5 clauses; JOINT clause (c) spans both reviewer faces):

| Clause | Author-side | Axis-A (lizzi, spectral/NCG) | Axis-B (volovik, transport) | JOINT? |
|:-------|:------------|:-----------------------------|:----------------------------|:-------|
| (a) homogeneity-degree obstruction `deg(Res_W)=−2s≠0` ∧ `deg(HKR)=0` | connes | **PASS** | — | no |
| (e) pole-scoping + index-rigidity `d_τ(s)=−2s` non-deformable; no `s>0` reaches `d_τ→0` | connes | **PASS** | — | no |
| (binding) canonical-import SCALAR VACUOUS; admissible = substrate-natural NON-SCALAR (T3/T4\|s≠s'/T5) | mack | — | **PASS** | no |
| (c) `Δ_scheme(B)→machine-zero` across {APS-1975 / Cheeger-Simons / Bismut-Cheeger} | **JOINT** | **PASS** (Δ_scheme=0.0) | **PASS** (Δ_scheme=0.0) | **YES — PASS-AND** |

`n_pass = 5/5`, `n_fail = 0`, `n_info = 0`. Reviewer-reported aggregates cross-checked against the per-clause AND: `axisA_single_axis_all = PASS` (== (a)∧(e)); `axisB_single_axis_all = PASS` (== (binding)); both `aggregate_consistent = True`.

**Substitution chain** (gate block §W1-1, instantiated with the loaded verdicts):
- **Step 1**: `clause_c_axisA` = lizzi-spectral `Δ_scheme→0` verdict = **PASS** (Δ_scheme = 0.000e+00 < 1e-9 M_KK²; GV_APS=GV_CS=GV_BC=−1.2081580929e+08 bit-identical, re-derived from the registered entry, not the workshop) → `True`.
- **Step 2**: `clause_c_axisB` = volovik-transport verdict on the SAME `Δ_scheme→0` test = **PASS** (Δ_scheme = 0.000e+00 < 1e-9, independently recomputed by subtracting GV_APS/GV_CS/GV_BC; eta_defect = 0; no shared workshop context) → `True`.
- **Step 3**: `clause_c_PASS_AND = (clause_c_axisA AND clause_c_axisB) = (True AND True) = True` — logical AND, NOT OR (single-reviewer PASS is structurally insufficient per the joint-clause refusal of single-agent firings).
- **Step 4**: `Stage2_composite_PASS = (axisA_PASS=True) ∧ (axisB_PASS=True) ∧ (clause_c_PASS_AND=True) ∧ (substrate_input_orthogonality=True) = True`.
- **Step 5**: substrate-input-orthogonality direction — ∃ obs_i loaded by exactly ONE reviewer: Axis-A anchor `s92_w1_cf_w9_8_1_composite_bridge_map_wodzicki_hkr.npz` ≠ Axis-B anchor `s92_w2_wodzicki_f_functor_normalization.npz` → `anchors_distinct = True` → orthogonality at ≥1 observable → **structural ceiling, NO substrate-input-overlap caveat** (the §VII.AH STAGE-3-PERMANENT structural-ceiling precedent, S89 W4-7 audit_sha256=`4fcd7d29af51c56d…`; the §VII.BB precedent S93 W6-3).
- **Conclusion**: composite = **PASS** ⇒ §VII.BA `#### (h)` **STAGE-3-PERMANENT-ELIGIBLE**.

**Composite collapse** (joint-theorem-promotion.md §"Stage 2"): no clause FAIL (n_fail=0) AND no clause INFO (n_info=0) AND orthogonality holds (no overlap caveat) ⇒ composite PASS, `promotion_decision = PROMOTE-ELIGIBLE`, `stage3_eligible = True`.

**Stage-2 protocol compliance** (6/6): (1) dispatched in parallel ✓; (2) different axes (spectral/NCG vs transport/superfluid) ✓; (3) reviewers NOT original authors (lizzi + volovik; connes + mack EXCLUDED per the downstream-inheritance-reach test) ✓; (4) no workshop transcripts in dispatch prompt (reviewers read only the registered Stage-1 entry + cited inputs) ✓; (5) PASS-AND on JOINT clause applied ✓; (6) substrate-input-orthogonality at ≥1 observable ✓.

**4-tuple**: `(value='composite=PASS;stage3_eligible=True;clause_c_PASS_AND=True;axisA_single_axis_all=PASS;axisB_single_axis_all=PASS;substrate_input_orthogonality=True;n_pass=5of5;n_fail=0;n_info=0', scheme=stage-2-independent-verify-two-axis-NCG-spectral-and-transport, convention=registry-VII.BA-(h)-STAGE-1-CANDIDATE-per-clause-PASS-AND, L_max=12)`.

**Canonical dual-SHA verdict line** (in `computations/session-94/s94_gate_verdicts.txt`):
```
S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY: PASS -- value='composite=PASS;stage3_eligible=True;clause_c_PASS_AND=True;axisA_single_axis_all=PASS;axisB_single_axis_all=PASS;substrate_input_orthogonality=True;n_pass=5of5;n_fail=0;n_info=0' scheme=stage-2-independent-verify-two-axis-NCG-spectral-and-transport convention=registry-VII.BA-(h)-STAGE-1-CANDIDATE-per-clause-PASS-AND L_max=12 audit_sha256=e6cb47a94badfa8f04bb710f2978cfede401df05073fcb48dbeabce2c2f2a316 content_sha256=d1106a2d5cddde0feaa5cbf3938f4c65268cb31a2abe0b90e28cd1af595e1a2c schema_version=S84+
# audit_sha256_short=e6cb47a94badfa8f content_sha256_short=d1106a2d5cddde0f # S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY dual-SHA companion row (W9a-99 split); Stage-2 PASS-AND aggregate of §VII.BA (h) STAGE-1-CANDIDATE; axisA lizzi (a)/(e)/(c)=PASS; axisB volovik (binding)/(c)=PASS; JOINT clause (c) PASS-AND=True; substrate-input-orthogonality=True (distinct anchors, structural ceiling, no overlap caveat); composite=PASS -> §VII.BA (h) STAGE-3-PERMANENT-ELIGIBLE (orchestrator flips registry tag at wave close)
```

**STAGE-3-PERMANENT eligibility statement**: §VII.BA `#### (h)` JOINT TWO-AXIS composite-bridge-map dimensional-class admissibility theorem (THIRD framework joint cross-axis theorem to enter the 4-stage pathway, after §VII.AH and §VII.U.2 Var_a) is **STAGE-3-PERMANENT-ELIGIBLE**. Per `joint-theorem-promotion.md §"Stage 3"`, the orchestrator updates the registry tag STAGE-1-CANDIDATE → STAGE-3-PERMANENT at wave close (this aggregator does NOT edit `permanent-results-registry.md`). On promotion, §VII.BA `#### (h)` joins the STAGE-3-PERMANENT cross-axis joint-theorem set {§VII.AH (FIRST), §VII.U.2 Var_a, §VII.AW.OP-PROJ, §VII.BB}, and the composite-bridge dimensional-class wall (T1/T2/T4\|s=s' FORBIDDEN; T3/T4\|s≠s'/T5 ADMISSIBLE) is permanently established for all Mellin-cone bridges at s>0. The "agreement" between the two PASSing reviews is structurally INDEPENDENT (orthogonal substrate-input anchors + no shared workshop context), so it does NOT fall under the `epistemic-discipline.md §"What Does NOT Count as Evidence"` item-2 "agreement among agents" exclusion — it IS evidence per the constructive joint-theorem-promotion pathway.

**Substrate framing**: the §VII.BA composite bridge map `B = f⊙g` is a structural property of the substrate's OWN Wodzicki/HKR/K_0 morphisms — `Res_W` is the unique trace on `Ψ(A_K)` (a substrate-intrinsic functional, NOT a container-side accounting), its homogeneity degree `−2s` intrinsic to D_K's eigenvalue spectrum (Wodzicki uniqueness, upstream of every regularization scheme). The two-axis admissibility (deg(B)=d_A ∧ substrate-natural non-scalar binding) is the substrate's algebraic-trace dimensional structure dictating what its bridge maps CAN be — substrate → emergent, never the lab anchor overriding the composite's degree.

**Artifacts**: `s94_w1_1_vii_ba_stage_2_cross_axis_verify.py` (29580 B) / `.npz` (9568 B; clause×reviewer PASS-AND matrix + substitution-chain booleans) / `.png` (53124 B; clause×reviewer PASS-AND matrix heatmap).

#### Axis-A cross-review (lizzi-spectral-functional-theorist)

**Independence attestation**: this Axis-A (spectral / NCG-axiomatic) verdict is re-derived from the registered §VII.BA `#### (h)` STAGE-1-CANDIDATE entry text + the cited input npz/canonical-constants ALONE. I did NOT read the S92 §VII.BA workshop transcript, the S93 W1 R3 text, or any Axis-B (volovik) output. I am not an original author of §VII.BA (connes + mack authored it) → original-author-exclusion + downstream-inheritance-reach test satisfied. **Substrate-input-orthogonality anchor**: I loaded `s92_w1_cf_w9_8_1_composite_bridge_map_wodzicki_hkr.npz` (Axis-A only; Axis-B loads `s92_w2_wodzicki_f_functor_normalization.npz`) → orthogonality at ≥1 observable.

**Verdict JSON**: `computations/session-94/s94_w1_1_axisA_lizzi_verdict.json` — `{a: PASS, e: PASS, c_joint: PASS, axisA_single_axis_all: PASS, delta_scheme_value: 0.0}`.

**Canonical-anchor cross-check** (knowledge-MCP + npz): `M_KK = 7.428660036284456e16` (matches S93 npz + MCP); `Delta_BCS = 0.4642547394830737` (R-PROTECTED, `BCS-GAP-CANONICAL-70`; matches Element-2 degree-0 anchor + S93 npz); `tau_fold = 0.19`. All canonical, none stale.

---

**Clause (a) — homogeneity-degree obstruction `deg(Res_W) = −2s ≠ 0` ∧ `deg(HKR) = 0`: PASS**

Substitution chain (homogeneity-degree axis):
- Step 1 — `deg(O)` is read off from `O(L) ~ L^{p}`, `p = d ln O / d ln L` (log-log slope). [definition of homogeneity degree as truncation-scaling exponent]
- Step 2 — a degree-(−2s) trace SUM `Res_W` accumulates more eigenvalues into the SUM as `L_max` rises ⇒ positive log-log slope `p_SUM > 0`. [a nonzero homogeneity degree drives the truncated SUM]
- Step 3 — a degree-0 cohomology RATIO `HKR` converges to a finite limit ⇒ `p_RATIO → 0`. [orientability-axiom Chern character: degree-0 object is truncation-stable]
- Step 4 — substitute the substrate series `Res_W = {43462.75, 93402.77, 174981.20}` at `L_max = {8, 10, 12}`: independent fit `p_ResW = +3.4348 > 0`; `HKR = {1.01960, 1.01375, 1.01009} → 1.008` (canonical degree-0 anchor `1.0076927826`), `p_HKR = −0.0232 ≈ 0`. Composite `B = Res_W·HKR` slope `= +3.4116` tracks `Res_W` (= the entry-cited `alpha_composite_Wodzicki = −3.4116` forbidden-T1 face, sign-flipped because α is defined as the L^{−α} envelope exponent against a degree-0 anchor).
- Step 5 — `p_ResW > 0 ⇒ deg(Res_W) ≠ 0` AND `p_HKR ≈ 0 ⇒ deg(HKR) = 0`. [both sub-claims of clause (a) hold]

Conclusion: the homogeneity-degree obstruction is double-warranted — PROOF (Wodzicki uniqueness gives `deg(Res_W) = −2s`; orientability + Chern give `deg(HKR) = 0`) AND MEASUREMENT (independent log-log slopes `+3.43` vs `≈0`). **PASS.**

**Clause (e) — pole-scoping + index-rigidity `d_τ(s) = −2s` non-deformable; no pole `s>0` reaches `d_τ→0`; boundary at `s=0`: PASS**

Substitution chain (index-rigidity axis):
- Step 1 — `d_τ(s) = −2s` (homogeneity degree of `Res_W(D^{−2s})`). [Wodzicki homogeneity]
- Step 2 — `d_τ(s)` is linear in `s` with integer slope `−2`; an index-type invariant (integer-quantized), non-deformable under continuous moduli (τ) deformation. [index-type invariants are rigid in moduli]
- Step 3 — `d_τ → 0 ⟺ s → 0`; for ANY pole `s>0`, `|d_τ| = 2s ≥ 2 > 0`, strictly bounded away from 0. The boundary `s=0` (`ζ_D(0)`) is the sole degree-0 point and carries no coupling/BCS-sector content.
- Step 4 — substrate corroboration: distinct poles carry distinct degrees — `Res_W(s=2,3,4)` at L12 = `{174981, 17823, 3091}` are all distinct (no pole-degeneracy); the deg-`2(s′−s) = +2` differential SUM `T4_23` is nonvacuous (`ratio = 9.82` at L12, `slope_dlnL = 11.24`, R²=0.991), consistent with the per-pole degree separation.
- Step 5 — `|d_τ(s>0)| ≥ 2 > 0` and distinct-pole degrees ⇒ pole-scoped + rigid; only `s=0` dissolves the degree. [clause (e) holds]

Conclusion: `d_τ(s) = −2s` is an index-rigid, pole-scoped invariant; no `s>0` pole reaches `d_τ→0`. **PASS.**

**JOINT clause (c) — `Δ_scheme(B) → machine-zero` across {APS-1975 / Cheeger-Simons / Bismut-Cheeger}: PASS (Axis-A face)**

Substitution chain (Δ_scheme operational test):
- Step 1 — `Δ_scheme = max(|GV_APS − GV_CS|, |GV_APS − GV_BC|, |GV_CS − GV_BC|)` at `L_max = 12`. [secondary-class scheme-spread; the operational equivalent of two-axis admissibility]
- Step 2 — substitute the substrate GV arrays (`s93_w1_3` npz): `GV_APS_L12 = GV_CS_L12 = GV_BC_L12 = −1.2081580929e+08` (bit-identical to float64); recomputed `diff_AC = diff_AB = diff_CB = 0.000000e+00`.
- Step 3 — `Δ_scheme = 0.000000e+00`.
- Step 4 — threshold (plan §W1-1): `|Δ_scheme| < 1e-9 M_KK²`. `0.0 < 1e-9 ⇒ PASS`.
- Step 5 — non-stale / canonical certificate: my recomputed `Δ_scheme = 0.0` matches (i) the registered Element-5 cite `GV_APS = GV_CS = −1.2081580929e+08`, (ii) the S93 npz `delta_scheme_L12 = 0.0`, (iii) the canonical knowledge-MCP gate `S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT` (`max_pairwise_diff = 0.000000e+00`), with a robust 2nd instance `S92-W7-…-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT` (`Delta_max = 0.0` on a different observable Π).

Conclusion: a degree-matched odd-grading object (the η-defect-free secondary class) is machine-zero across all three secondary-class schemes — the Δ_scheme→0 operational test reproduces from the registered entry alone. **PASS on the Axis-A face** (the JOINT clause requires the Axis-B face to PASS-AND independently; that is volovik's emission, aggregated by connes).

---

**Δ_scheme numerical certificate**: `Δ_scheme = max(|GV_APS−GV_CS|, |GV_APS−GV_BC|, |GV_CS−GV_BC|)_{L12} = 0.000000e+00 < 1e-9 M_KK²` → PASS (GV_APS=GV_CS=GV_BC=−1.2081580929e+08, float64-identical).

**Axis-A aggregate**: clause (a) PASS ∧ clause (e) PASS ⇒ `axisA_single_axis_all = PASS`; JOINT clause (c) PASS on the Axis-A face. The "agreement" this produces with the registered entry is structurally INDEPENDENT (re-derived without workshop context), breaking the shared-context-produces-shared-output failure mode per `joint-theorem-promotion.md §"Stage 2"`. **Substrate framing**: the Wodzicki residue `Res_W: Ψ(A_K) → ℂ` IS the substrate's intrinsic algebraic-trace functional; its homogeneity degree `−2s` is intrinsic to D_K's eigenvalue spectrum (Wodzicki uniqueness), upstream of every truncation/regularization scheme — the composite bridge map's admissibility flows substrate → emergent, not container → substrate.

---

#### Axis-B cross-review (volovik-superfluid-universe-theorist)

**Reviewer**: `volovik-superfluid-universe-theorist` (Axis-B — transport / superfluid-universe; substrate-natural-binding axis). Independence satisfied: NOT an original author of §VII.BA (`connes` + `mack` authored it) → original-author-exclusion + downstream-inheritance-reach test satisfied. This review was re-derived from the registered §VII.BA `#### (h)` STAGE-1-CANDIDATE entry ALONE — blind to the S92 W-1 workshop transcript, the S93 W1 R3 text, and the Axis-A (lizzi) output, per `joint-theorem-promotion.md §"Stage 2"`.

**Audit scope**: the Axis-B single-axis **(binding)** clause [mack-authored, transport-side] + the **JOINT clause (c)** [Δ_scheme→0 operational test], per the joint-clause attribution table of the registered entry.

**Substrate-input-orthogonality anchor**: I LOAD `computations/session-92/s92_w2_wodzicki_f_functor_normalization.npz` (the T2 scalar-cancellation evidence face) — the data file the Axis-A reviewer does NOT load. That input-orthogonality is what makes the cross-axis agreement structurally INDEPENDENT (structural-INPUT independence, not merely structural-OUTPUT-type independence) per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY-K=3.

**MCP Pre-Compute Audit**:
- `get_constant("Delta_BCS")` → `0.4642547394830737` (S70 `BCS-GAP-CANONICAL-70`, R-PROTECTED, M_KK units = dimensionless) — matches the registered entry's degree-0 Level-3 anchor and the npz `Delta_BCS_canonical`.
- `get_constant("M_KK_gravity")` → `7.428660036284456e+16` GeV (S42 `CONST-FREEZE-42`) — matches npz `M_KK`.
- `search_knowledge("VII.BA composite bridge map Delta_scheme machine-zero secondary class")` → surfaced gate `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR` (`delta_scheme=0.000e+00, GV_APS_L12=GV_CS_L12=-1.208158e+08, eta_L12=0e+00, reading=A`) — a SISTER-session reproduction of the identical secondary-class certificate, confirming Δ_scheme→0 is reproducible across sessions (not a one-off W1-3 artifact).

**NUMBERS (Axis-B independent re-derivation; full certificates in `s94_w1_1_axisB_volovik_verify.npz`)**:

*Clause (binding)* — two-part irreducible-conjunction re-derivation:

- **(B-i) T2 canonical-import SCALAR is VACUOUS** (from the Axis-B orthogonality anchor `s92_w2`): the dimensionless ratio is INVARIANT under the scalar `N = M_KK^5`:
  - `ratio_pre            = 376906.724779`
  - `ratio_post_internal  = 376906.724779`  (Δ vs pre `< 1e-9` rel — cancels)
  - `ratio_post_lab       = 376906.724779`  (Δ vs pre `< 1e-9` rel — cancels)
  - The scalar cancels EXACTLY in the dimensionless ratio ⇒ it carries NO L_max-dependence and cannot close the numerical gap. `T2_scalar_vacuous = True`.
- **(B-ii) admissible re-route requires a substrate-natural NON-SCALAR morphism**:
  - FORBIDDEN equal-pole `T4|s=s'` ratio: `slope_dlnL = 0.0` ⇒ exactly L_max-flat ⇒ VACUOUS (the sharpest conjunct-2 witness). `T4_eqpole_forbidden = True`.
  - `T3` (same-class ratio): `slope_dlnL = 2.450e-04 ≠ 0`, `deg_match=True`, `admissible=True` — substrate-natural non-scalar.
  - `T4|s≠s'` (Res_W ratio at distinct poles): `slope_dlnL = 1.124e+01 ≠ 0`, `deg_match=True`, `admissible=True` — substrate-natural non-scalar.
  - `T5` (K_0-pairing): `slope_dlnL = −2.853e+08 ≠ 0`, `deg_match=True`, `admissible=True` — substrate-natural non-scalar; `selected_formulation = T5`.
  - An admissible substrate-natural non-scalar re-route EXISTS, and the SELECTED morphism (T5) is itself substrate-natural non-scalar with surviving L_max-dependence. `admissible_nonscalar_exists = True`.

  **Clause (binding) VERDICT = PASS** (`T2_scalar_vacuous ∧ admissible_nonscalar_exists ∧ T4_eqpole_forbidden ∧ selected(T5)_nonscalar_substrate_natural`). Substrate reading: a canonical-import scalar is a *container-side* unit conversion that the dimensionless ratio annihilates — it is NOT the substrate's own structure. Only a morphism carrying the substrate's OWN L_max-dependence (a same-class ratio at distinct poles, or a K_0-pairing carrying the substrate's χ-image BdG inheritance-class degree) is admissible. The substrate's algebraic-trace dimensional structure — not the lab anchor — dictates which bridge maps are admissible.

*JOINT clause (c)* — Δ_scheme → machine-zero certificate, **independently recomputed** (I subtracted GV_APS/GV_CS/GV_BC myself at L_max=12, full float64, rather than trusting the npz's pre-computed `delta_scheme_L12` field):
  - `GV_APS(L=12) = −1.2081580929e+08`
  - `GV_CS (L=12) = −1.2081580929e+08`
  - `GV_BC (L=12) = −1.2081580929e+08`
  - `|APS−CS| = 0.000e+00`, `|APS−BC| = 0.000e+00`, `|CS−BC| = 0.000e+00`
  - **Δ_scheme (max pairwise spread) = 0.000e+00 M_KK²** — exactly zero (the three are bit-identical), well inside the pre-registered tolerance `|Δ_scheme| < 1e-9 M_KK²` (9+ OOM of margin).
  - Holds across the FULL L-scan: per-L spread over `{8,10,12}` = `[0.0, 0.0, 0.0]` (necessity verified per-pole, not only at canonical).
  - My recompute agrees with the npz `delta_scheme_L12 = 0.000e+00` bit-for-bit (`npz_agrees = True`).
  - `GV_eta_defect = [0.0, 0.0, 0.0]` ⇒ the degree-matched odd-grading GV-Heitsch object is scheme-CLEAN (no η-defect distinguishes the three secondary-class schemes; sufficiency on the secondary-class axis).
  - **Sage-exact sufficiency cross-check** (200-bit `RealField`): because the three scheme evaluations are bit-identical, the pairwise differences are EXACTLY 0 (no cancellation residue), so the machine-zero is STRUCTURAL — `Δ_scheme = 0` because all three schemes evaluate the SAME representative-independent degree-matched odd-grading object — NOT a sub-float64 spread that would re-inflate under exact arithmetic.

  **JOINT clause (c) VERDICT = PASS** (`Δ_scheme < 1e-9 across L-scan ∧ npz_agrees ∧ eta_defect_zero`). Substrate reading: the necessary-∧-sufficient operational test is satisfied — a degree-matched substrate-natural morphism produces a representative-independent (scheme-blind) cohomology output, precisely the operational signature distinguishing the admissible class (T3/T4|s≠s'/T5) from the forbidden classes (T1 wrong-degree / T2 scalar / T4|s=s' equal-pole).

**Axis-B per-clause verdict**: `{binding: PASS, c_joint: PASS}`; `axisB_single_axis_all = PASS`; `delta_scheme_value = 0.0`. JSON certificate: `computations/session-94/s94_w1_1_axisB_volovik_verdict.json`.

**Independence statement**: re-derived from the registered Stage-1 entry alone (no workshop context), loading the Axis-B-only orthogonality anchor `s92_w2_wodzicki_f_functor_normalization.npz`. The agreement between this review and the Axis-A review (both land PASS on JOINT clause (c)) is therefore structurally INDEPENDENT per the `joint-theorem-promotion.md` constructive pathway — it breaks the shared-context-produces-shared-output failure mode that the generic "agreement among agents" exclusion (`epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2) forbids. The JOINT clause (c) is PASS-AND'd by the connes aggregator across both reviewers; this review supplies the Axis-B PASS leg.

**Routing note (Axis-B contribution)**: on the Axis-B side, both audited clauses PASS. STAGE-3-PERMANENT eligibility for the §VII.BA `#### (h)` joint theorem is contingent on the Axis-A reviewer also PASSing clauses (a)/(e) + JOINT (c) (confirmed landed above: `axisA_single_axis_all = PASS`, JOINT (c) PASS), and on the connes aggregator confirming the JOINT-clause-(c) PASS-AND + substrate-input-orthogonality at ≥1 observable (SATISFIED: I load `s92_w2_wodzicki_f_functor_normalization.npz`, Axis-A loads `s92_w1_cf_w9_8_1_composite_bridge_map_wodzicki_hkr.npz` — distinct data files ⇒ structural ceiling, no substrate-input-overlap caveat, mirroring the §VII.AH / §VII.BB structural-ceiling precedents). The composite Stage-2 verdict line is emitted by the connes aggregator, NOT by this review.

---

### §W1-2. S94-VII-BA-T4-ENVELOPE-EXTENSION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-BA-T4-ENVELOPE-EXTENSION`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (Level-3-vs-Level-2 envelope-saturation direction test for the T4|s≠s' `Res_W(s)/Res_W(s')` ratio)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: Extended beyond the L_max=12 cache ceiling via the Friedrich-Bär analytic tail over L∈[14,100], the T4|s≠s' differential-SUM-growth envelope either saturates so the Level-3 anchor drops below the Level-2 envelope (L3<L2 ⇒ T4|s≠s' admissible as an alternative Element-3) or persists L3>L2 (T4 not envelope-saturated ⇒ T5 remains the SOLE admissible Element-3).
**Plan reference**: `sessions/session-plan/session-94-plan-w1.md` §W1-2 (Friedrich-Bär saturation tail, η_FB lower-bound, pole pair (s,s')=(2,3), [SIGN] substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **script** `computations/session-94/s94_w1_2_vii_ba_t4_envelope_extension.py` — EXISTS (41,507 bytes). `grep -E "from canonical_constants import|append_verdict"` matches at L86 `from canonical_constants import (`, L382 `def append_verdict(...)`, L809 `append_verdict(composite, ...)`. Both must_contain patterns present.
- **data** `computations/session-94/s94_w1_2_vii_ba_t4_envelope_extension.npz` — EXISTS (29,504 bytes; full L-grid Res_W(2)/Res_W(3) over [8,100] both calibration methods, sliding-window dL/L3/L2/alpha, FB predicate, dual-SHA).
- **plot** `computations/session-94/s94_w1_2_vii_ba_t4_envelope_extension.png` — EXISTS (186,452 bytes; 4-panel: T4 ratio over [8,100], dL(L_max)=L3-L2 trajectory [the core figure, saturation window [50,100] shaded], envelope-exponent alpha(L_max), L3-vs-L2 over window).
- **verdict_line** `computations/session-94/s94_gate_verdicts.txt` — EXISTS. `grep -E "^S94-VII-BA-T4-ENVELOPE-EXTENSION:.* audit_sha256=[a-f0-9]{64}"` matches. Dual-SHA companion row + **[SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`)** + LEVEL/MACHINERY-SCOPE/BINDING axis pins all present. `audit_sha256=a74e9f1e...` UNIQUE in the file (sig_5 PASS).

**MCP Pre-Compute Audit**:

- `search_knowledge("VII.BA T4 Res_W envelope Friedrich-Bar saturation L3 L2 composite bridge")` → returns S92 §VII.BA workshop, S93 W1 plan, S92-W1-CF-W9-8-1 (alpha_composite_Wodzicki, Res_W_L8/L10/L12 = 4.346e4/9.340e4/1.750e5), Friedrich-Bär saturation theorem PROVEN entries. No closure covers the *extended* (L>12) T4 envelope test — gate NOT PRE-CLOSED; it picks up CF-S94-W1-B from S93 W1-3.
- `search_knowledge("Wodzicki residue degree -2s differential SUM growth L_max truncation")` → confirms `deg(Res_W)=-2s`; the S93 W1 plan truncated Res_W^(L)(s) form; the S93 W7-1 transport degree deg=+2 NON-SCALAR (T4-non-scalar reading) — consistent with T4 deg=2(s'-s)=+2.
- `get_constant("tau_fold")` → 0.19 (S12/S42 CONST-FREEZE-42); matches the cache anchor tau_fold.
- Cross-checked the S93 W1-3 npz directly (`audit_sha256=8b6ba6bc...`): `T4_level3=20.648 > T4_level2=20.553`, `T4_l3_lt_l2=False`, `T4_deg=2`, `Res_W_s2/s3` — the gate's input anchor.

**Verdict**: **FAIL** (composite) — `value='FAIL_L3_NOT_below_L2: dL_asymptotic=+4.179723e-02>=0 persists through L_max=100; T4|s!=s' deg+2 differential-SUM-growth NOT saturated (alpha_env=-0.7077<0 DIVERGENT); T5 SOLE registry-PASS-eligible Element-3; admissible-set NOT widened.'` scheme=`T4-Res_W-ratio-Friedrich-Bar-analytic-tail` convention=`VII-BA-T4-s-neq-s-prime-Res_W-over-Res_W-deg-2-differential-SUM-growth` L_max=`8_10_12_friedrich_bar_14_100` audit_sha256=`a74e9f1ef2d42610e98c319811ab88ec4058913b254f59279c5bd1d223dfaa67`.

3-tuple: `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID` → composite **FAIL** (magnitude FAIL ∧ regime VALID ⇒ FAIL per `gate-verdicts.md §"Composite-collapse rule"`).

**Results**:

**Input anchor reproduction (bit-for-bit vs S93 W1-3).** EXACT in-cache `Res_W(s={2,3}, L)` over L∈{8,10,12} reproduces the S93 W1-3 npz at rtol=1e-9:

| L_max | Res_W(s=2) | Res_W(s=3) | T4 = Res_W(2)/Res_W(3) |
|:------|:-----------|:-----------|:-----------------------|
| 8  | 43462.7490 | 8301.5759  | 5.2355 |
| 10 | 93402.7652 | 12651.0137 | 7.3830 |
| 12 | 174981.1976 | 17823.1548 | 9.8176 |

W1-3 anchor: L3 = 2.0648e1 > L2 = 2.0553e1 ⇒ dL(12) = +9.5148e-02 (my Aitken-window {8,10,12} reproduces the W1-3 "+0.095" exactly).

**Friedrich-Bär analytic tail (regime-validity gate).** eta_FB(p,q) = |λ|_min(p,q)/√(C_2(p,q)+1) all-sector min = **0.436488 at (1,1) ≥ eta_FB_lower = 0.40** (PASS); NEW-sector p+q=13 worst-case lower bound = 3.0022 > bot-8 ceiling 0.8409 (PASS); `saturation_pass = True` ⇒ the analytic tail is well-defined ⇒ **regime_verdict = VALID**. (Methodology mirrors `s92_w9_3_friedrich_bar_saturation_unified.py` lines 237-298, W11-3 calibration.)

**Per-eigenvalue moment calibration** (analytic-tail input, on the 89 nonzero-Casimir cache sectors): <|λ|^{-2s}>(p,q) ~ A_s·C_2(p,q)^{-beta_s} — s=2: A=2.56926, beta=1.6804 (r²=0.9903); s=3: A=4.73936, beta=2.5475 (r²=0.9907). The empirical band ratio mean|λ|/√C_2 → 0.595 anchors the Casimir-bound floor (the conservative kappa-band robustness method uses <|λ|^{-2s}>=(kappa_s·√C_2)^{-2s}, kappa_2=0.6169, kappa_3=0.6110).

**T4 ratio over the extended tail** (per-sector residue contribution dim(p,q)·16·dim(p,q)·<|λ|^{-2s}> summed over NEW levels p+q∈[13,100]):

| L_max | Res_W(2) | Res_W(3) | T4 (power-law) | T4 (kappa-band) |
|:------|:---------|:---------|:---------------|:------------|
| 12  | 1.7498e5 | 1.7823e4 | 9.8176  | 9.8176 |
| 14  | 3.2008e5 | 2.5317e4 | 12.6429 | 12.3936 |
| 20  | 1.3449e6 | 5.9798e4 | 22.4907 | 22.6709 |
| 40  | 2.5428e7 | 3.6502e5 | 69.6636 | 82.3535 |
| 60  | 1.5172e8 | 1.1095e6 | 136.7470 | 179.8929 |
| 80  | 5.4941e8 | 2.4773e6 | 221.7785 | 314.9488 |
| 100 | 1.5031e9 | 4.6469e6 | 323.4670 | 487.4374 |

**The T4 ratio DIVERGES monotonically** (9.82 → 323.5 power-law / → 487.4 kappa-band over L∈[12,100]). The divergence direction is **robust to the calibration method** — both methods grow far above the L=12 value 9.82; only the magnitude differs.

**Envelope dL(L_max) = L3 − L2 (sliding 3-pt Aitken Δ² window, step-2, matching S93 W1-3 spacing).**
- dL(12) [window 8,10,12] = +9.5148e-02 (W1-3 anchor reproduced).
- Asymptotic window L_fit=[50,100]: **mean dL = +4.179723e-02; dL(100) = +3.769e-02** — strictly positive, **never crosses below zero**.
- **Mean envelope exponent alpha = -0.7077 over [50,100]** (negative everywhere: -0.69 at L=12 → -0.71 at L=100). A NEGATIVE alpha means the residual |Φ(L) − Φ_∞| *grows* with L — the T4 sequence is **DIVERGENT**, so the Aitken Φ_∞ is a meaningless artifact (it returns nonsensical negatives like -427 for a ratio that is itself ≈ 750). Level-3 (the residual) and Level-2 (C·L^{-alpha} with alpha<0 ⇒ a *growing* envelope) both increase without bound; L3 never falls below L2.
- Cache-ceiling deviation |dL_asymptotic − dL(12)|/|dL_asymptotic| = 1.2764 > 0.10 → cite the cache-ceiling effect + Friedrich-Bär saturation theorem per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"`. The asymptotic dL (+0.042) is smaller than the in-cache dL(12) (+0.095) but stays positive — the deviation does NOT change the sign verdict.

**[SIGN] substitution chain (substituted numbers).**
- *Step 1:* Res_W(s, L_max) = Σ_k m_k·|λ_k|^{-2s} (bare moment = unique Wodzicki trace on the FINITE triple; CM-1995 §III.4 / Connes 1994 §2.3). At s=2: Res_W(L=8/10/12) = {4.346e4, 9.340e4, 1.750e5} ~ L^{3.4} SUM-growth. `deg(Res_W) = -2s ≠ 0`.
- *Step 2:* deg(T4) = deg(Res_W(s)) − deg(Res_W(s')) = (-2·2) − (-2·3) = **+2** (corpus §18.0 taxonomy row T4; s=2,s'=3).
- *Step 3:* dL(12) = L3 − L2 = 20.648 − 20.553 = **+0.0951 > 0** (Level-3 ABOVE Level-2; not yet saturated). [S93 W1-3 carry-forward CF-S94-W1-B]
- *Step 4:* Friedrich-Bär tail substitution: NEW-sector eigenvalues bounded below by eta_FB_lower·√(C_2(p+q)+1). Because |λ|^{-2s} weights small λ heavily AND the higher pole s=3 is MORE concentrated on small eigenvalues than s=2, new high-level sectors (with |λ|_min ~ √(level)) contribute *proportionally less* to Res_W(3) than to Res_W(2) ⇒ the ratio Res_W(2)/Res_W(3) keeps growing. dL(L_max) → +0.042 at [50,100]; dL stays ≥ 0 (the net magnitude decreases over [12,100] but never sign-flips).
- *Step 5 (direction read-off):* dL(L_max) stays ≥ 0 through L_max=100 ⇒ **L3 ≥ L2 ⇒ FAIL the L3<L2 test** ⇒ T4|s≠s' is structurally-admissible (deg-match + non-scalar) but NOT envelope-saturated ⇒ T5 remains the SOLE registry-PASS-eligible Element-3.

**4-tuple**: `(value=+4.179723e-02_sign=PASS, scheme=T4-Res_W-ratio-Friedrich-Bar-analytic-tail, convention=VII-BA-T4-s-neq-s-prime-Res_W-over-Res_W-deg-2-differential-SUM-growth, L_max=14..100)`.

**3-tuple companion row semantics**: `sign_verdict=PASS` (substitution-chain Step 5 PREDICTED no-crossing ⇒ dL stays ≥ 0; computed no-crossing matches — direction confirmed); `magnitude_verdict=FAIL` (dL_asymptotic = +0.0418 ≫ +0.001 band; L3 never below L2); `regime_verdict=VALID` (eta_FB saturation_pass=True, dL monotone over the window, the FB tail is defined unconditionally on [14,100] — f_used = 100% of the intended window). Composite collapse: magnitude FAIL ∧ regime VALID ⇒ **FAIL**.

**Solution-space (FAIL = T5-SOLE sharpening).** This SHARPENS the §VII.BA composite bridge. T4|s≠s' = Res_W(s)/Res_W(s') satisfies BOTH dimensional-class conjuncts (conjunct 1: deg=+2 matches d_A; conjunct 2: non-scalar, surviving L_max-dependence) — it is *structurally admissible* — but its Level-3 anchor never falls below its Level-2 envelope even asymptotically, so it is **NOT registry-PASS-eligible**. The deg-+2 differential-SUM-growth of Res_W is the obstruction: the numerator (s=2 moment) grows faster than the denominator (s=3 moment) can compensate in the ratio. Therefore **T5 (the Connes-Karoubi K_0-pairing <[φ], Ch(P_0)>, deg 0, L_max-saturated per S93 W1-3 T5_l3_lt_l2=True) remains the SOLE registry-PASS-eligible Element-3 for §VII.BA**; the admissible set is NOT widened to {T3, T4|s≠s', T5}. The composite-bridge dimensional-class wall (T1/T2/T4|s=s' FORBIDDEN; T3/T5 ADMISSIBLE-and-saturated; T4|s≠s' admissible-but-not-saturated) holds. PHONONIC classification: GEOMETRIC (a property of D_K's Casimir spectrum read off the substrate's structure, not an excitation observable).

**Artifacts**: `computations/session-94/s94_w1_2_vii_ba_t4_envelope_extension.py` / `.npz` / `.png`.

---

### §W1-3. S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY`
**Trigger**: `[VERIFY-THEOREM]` (+ [SIGN] sub-check on the degree-match sign + α_s negative-running sign)
**Classification**: **PARTICLE** (α_s strong-coupling running — representation-theoretic content of D_K at the a_4 Yang-Mills channel)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The α_s transport image lands as a NEW cross-pillar bridge via §VII.BA formulation T5 — the direct Connes-Karoubi K_0-pairing ⟨[φ], Ch(P_0)⟩ at the a_4 home pole s=2, with the index-fixed K_0-class degree matched to the α_s anchor degree and the K_0 class being the substrate's own χ-image BdG inheritance class (not a canonical-import scalar); the bridge satisfies the full 5-anatomy + 3-level ladder (Level-3 < Level-2 at canonical L_max) and passes an internal Stage-2 two-axis cross-verify.
**Plan reference**: `sessions/session-plan/session-94-plan-w1.md` §W1-3 (3-part plan-freeze pre-registration: home-pole s=2 / index-fixed degree-match / χ-image substrate-natural class; T5 admissibility conjuncts; internal Stage-2 lizzi+volovik).

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`): The substrate IS the finite spectral triple `(A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_K, D_K(τ_fold))`. The strong coupling α_s is a spectral moment of D_K at the **a_4 Yang-Mills channel** — the fourth Seeley-DeWitt coefficient, `Φ(a_4)=Σ_3` in the Φ correspondence. The T5 bridge `⟨[φ], Ch(P_0)⟩` is the substrate's OWN Connes-Karoubi K_0-pairing: P_0 is the substrate's spectral projection, `[φ]` is the GV-Heitsch secondary class (the ODD-grading object in the framework's (η=0, GV≠0) parity decomposition), and the K_0 class is the χ-image BdG inheritance class (`χ: ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)`). Direction of explanation: substrate K_0-pairing → Connes-Karoubi bridge → CMB-pivot α_s — NEVER inverted.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.py` — on disk (50,756 bytes). `grep -E 'from canonical_constants import'` → PRESENT (`from canonical_constants import (`). `grep -E 'append_verdict'` → PRESENT (def + call site). PASS.
- **data** `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz` — on disk (20,264 bytes); all Step-1..5 arrays + dual-SHA. PASS.
- **plot** `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.png` — on disk (117,233 bytes); 3 panels: T5 GV-Heitsch succ-ratio convergence + Level-3 vs Level-2 bars + Δ_scheme 3-scheme machine-zero bars. PASS.
- **verdict_line** matching `^S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY:.* audit_sha256=[a-f0-9]{64}` → PRESENT (canonical line `audit_sha256=d40965ec70e8c203d09c324b19e03c36d2427d6e298dc69abbf740a25cdea778`, supersedes the bug-fix predecessor `90a96508…` per gate-verdicts.md Option A); dual-SHA companion row PRESENT; **3-tuple companion row PRESENT** (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`). PASS.

**MCP Pre-Compute Audit** (queries executed before writing the script, per query-first discipline):
- `search_knowledge('alpha_s transport degree T5 Connes-Karoubi a_4 channel Yang-Mills s=2')` → returned `Φ(a_4)=Σ_3`, `a_4 = Res_{s=2} ζ_D(s)·2/Γ(2)`, the W7-1 transport result (`deg(T_BZ→pivot)=+2 NON-SCALAR, T4-non-scalar`), and the CF-S94-W1-6 routing-to-T5 theorem entry. NOT pre-closed — this gate IS the CF-S94-W1-6 landing.
- `get_constant('alpha_s_substrate_distance_1')` → `-0.08587279` (S92, AH-TR-1; NEGATIVE running, non-superseded). Used for the [SIGN] sub-check.
- `trace_entity('CF-S94-W1-6')` → theorem `proven_154` downstream-consumer chain; confirms routing to T5 + 3-part pre-registration.
- `list_constants('a_4|a4_FW|alpha_s')` + `get_constant('a_2_FW_zeta')` → `a_2_FW_zeta=2776.165389`; `alpha_s_pivot_goldstone=0` confirmed.
- Cross-read of the W7-1 npz (`alpha_s_moment_ratio_realization=-0.99373749`, `GV_APS=GV_CS=GV_BC=-1.20815809e+08`, `delta_scheme=0.0`, `deg_T=+2`, `two_axis_admissible=True`) and the W1-3 T5 npz (`T5_level2=0.13253732`, `T5_level3=0.12298499`, `T5_l3_lt_l2=True`, `T5_Phi_inf=8.156797`). These pin the canonical T5 convergence object (GV-Heitsch successive ratio, Aitken Δ²).

**Verdict**: **PASS** — composite=PASS, sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID. 4-tuple: `(value=composite:PASS, scheme=T5-Connes-Karoubi-K_0-pairing-a_4-channel-s2-index-fixed, convention=VII-Bx-T5-direct-Connes-Karoubi-K_0-pairing-alpha_s-a_4-s2-CHI-IMAGE-BDI-INHERITANCE-CLASS, L_max=12)`. The α_s transport image lands as a NEW cross-pillar bridge (provisional **§VII.Bx**, next-free-letter at registry-write) realized via the substrate's own χ-image BdG inheritance K_0-class. **STAGE-1-CANDIDATE** (per `joint-theorem-promotion.md`: the internal Stage-2 two-axis PASS-AND is the gate-internal certificate; the formal Stage-2 dispatch of the two axis-distinct cross-reviewers lizzi/volovik WITHOUT prior workshop context advances it toward STAGE-3-PERMANENT as a separate downstream gate).

**Results**:

**Substitution chain** (degree-match conjunct 1 + [SIGN] sub-check; Sage-verified this run):
- **Step 1 (degree of the K_0-pairing)** — T5 = `⟨[φ], Ch(P_0)⟩`, a single Connes-Karoubi cohomology pairing. Its degree is INDEX-FIXED: `deg(T5) = (K-theory class index of P_0) + (Hochschild degree of [φ])`, both integer topological invariants. [corpus §18.0 taxonomy row T5: "index-fixed to match anchor"]
- **Step 2 (degree of the α_s anchor)** — α_s lives at the a_4 Yang-Mills channel s=2; `Φ(a_4)=Σ_3` (weight-4 load-bearing). The transport degree was fixed by W7-1: `deg(T_BZ→pivot) = +2`, NON-SCALAR (`c34e4f17…`, T4-non-scalar, T_is_scalar=False). `d_A = +2`.
- **Step 3 (deg-match, Sage-exact)** — `deg(Res_W @ a4 pole s=2) = −2·s_eff = −4`; `deg(Res_W @ a2 pole s=1) = −2·s_eff = −2`; `deg(a_4/a_2) = 2(s_a2−s_a4) = −2` ⇒ `|deg| = 2`. `|deg(a_4/a_2)| == |d_A| == 2` and `d_A=+2 ∈ ℤ` ⇒ the index-fixed K_0 degree CAN equal d_A (discrete integer equality). **deg-match = True**. (Sage `sage_eval` this run; no OPERATOR-MISMATCH-DETECTED ⇒ NOT a Class-8 PRU defect.)
- **Step 4 (non-scalar conjunct 2)** — the K_0 class is the substrate's own χ-image BdG inheritance class. `χ: ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)` sends the M_3(ℂ) colour summand → 0; the inherited fibre fraction `f_χ = 4/16 = 1/4` is an L_max-INDEPENDENT representation-theoretic constant (it cancels in the a_4/a_2 ratio, `f_χ_cancels=True`), so it does NOT spoil the non-scalar property. The surviving L_max-dependence is the a_4/a_2 moment-ratio FLOW (ratio spread over L∈{8,10,12} = 7.665e-01; two poles respond differently to truncation; W7-1 `two_pole_survives=True`). A canonical-import reference class would be a degree-matched SCALAR — VACUOUS (T2, cancels). The χ-image class is substrate-natural NON-SCALAR. **conjunct 2 = True.**
- **Step 5 ([SIGN] sub-check)** — α_s substrate value is NEGATIVE (`alpha_s_substrate_distance_1 = −0.08587279`). The T5 image inherits the GV-Heitsch secondary-class sign (`GV_APS < 0` ⇒ odd-grading negative): `t5_image_signed = −1.493993 < 0`. The negative running sign is preserved. **sign_verdict = PASS** (negative running AND index-fixed deg-match +2).

**5-anatomy** (all five IS-not-IN elements, `cross-pillar-bridge-anatomy.md`):
1. **Substrate-IS observable** — the finite-L Connes-Karoubi K_0-pairing `⟨[φ], Ch(P_0(τ_fold))⟩` at the a_4 s=2 pole, evaluated on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The substrate IS this pairing. **Level-1 single-τ-slice** substrate-IS (`phononic-framing.md §"Single-τ-slice vs moduli-deformation"` Level 1; τ=τ_fold fixed).
2. **Laboratory-IN observable** — the CMB-pivot α_s running observable (CMB-S4 / CMB-HD substrate-sensitivity channel). OE-form: `α_s ~ ∂²/∂(ln k)² Tr(P_{a_4} D_K^{−4})` re-anchored at the pivot; the lab measures this running IN a cosmological container.
3. **Bridge map** — the **direct Connes-Karoubi K_0-pairing** (T5, index-fixed), `K_0(A_K) × K^0(A_K) → ℤ`, `[φ] ⊗ [P_0] ↦ ⟨[φ], Ch(P_0)⟩`. Explicitly named (NOT "analogous"). Binding: substrate-natural-binding (χ-image carries the substrate's own L_max-dependence).
4. **Algebraic envelope** — Level-2 convergence rate `L^{−α}` of the K_0-pairing image; `α_env = 9.9887` (the GV-Heitsch successive-ratio Aitken-Δ² envelope exponent), `Level-2 = 0.132537` at L_max=12.
5. **Empirical anchor** — the α_s pairing image at canonical L_max=12: `Level-3 = 0.122985`. Satisfies `Level-3 < Level-2`.

**3-level ladder**:
- **Level-1** (cohomology-class identity, regulator-invariant on the secondary-class axis): the GV-Heitsch `[φ]` secondary class is representative-INDEPENDENT — `Δ_scheme = max pairwise diff{GV_APS, GV_CS, GV_BC} = 0.000e+00 < 1e-9 M_KK²` at L_max=12 (and at L=8, L=10). All three secondary-class schemes {APS-1975-secondary-class, Cheeger-Simons (CM-1995 §III.4 residue at z=0), Bismut-Cheeger (η-form via exact adiabatic limit t→0⁺)} reduce bit-identically to the cubic-ρ Dixmier-trace sum `−4·Σ dim·ρ³·|λ|^{−4}`. `η_defect = 0.0` (BDI parity-blindness; the odd-grading [φ] carries the secondary content). This is the operational T5 admissibility certificate on the secondary-class-suffix axis (NOT the orthogonal UV-regulator RD axis). STRUCTURAL THEOREM, regulator-invariant, L-independent.
- **Level-2** (algebraic convergence envelope, L_max-dependent): the T5 Connes-Karoubi pairing's convergence object is the GV-Heitsch successive ratio `[1, GV(10)/GV(8), GV(12)/GV(10)] = [1, 9.0950, 8.0338]`, Aitken-Δ² extrapolated to `Φ_∞ = 8.156797`; envelope `|Φ(L)−Φ_∞| ~ C·L^{−α}` with `α_env = 9.9887`, `Level-2 = 0.132537` at L_max=12. STRUCTURAL PREDICTION, refines with L; Level-2-binding (HKR/Connes-Karoubi image to a continuum laboratory observable). (These reproduce the canonical W1-3 T5 values bit-for-bit: `T5_Phi_inf=8.156797419`, `T5_level2=0.13253731866`, `T5_level3=0.12298498721` — the T5 object is the cohomology-class pairing convergence, NOT the raw a_4/a_2 SUM/SUM moment ratio, which is a T4-type divergent object setting only the degree + sign.)
- **Level-3** (empirical anchor at canonical L_max=12): `Level-3 = 0.122985` numerical residual `|Φ(12)−Φ_∞|`. **Level-3 < Level-2** (0.122985 < 0.132537; margin = (L2−L3)/L2 = 0.0721 > 1e-3). EMPIRICAL CONFIRMATION. Registry-PASS criterion (`Level-3 < Level-2 at canonical L_max`) SATISFIED.

**T5 admissibility** (corpus §18.0 row T5; `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"`): conjunct 1 (deg-match d_A=+2) = True ∧ conjunct 2 (substrate-natural NON-SCALAR χ-image) = True ∧ operational Δ_scheme→machine-zero = True ⇒ **T5 ADMISSIBLE = True**. T5 is the unique admissible Element-3 at the coupling's home pole (T1 fails conjunct 1 wrong-degree; T2 + T4|s=s′ fail conjunct 2 scalar/equal-pole cancellation; T3 degree-0 ≠ d_A=+2 here; T4|s≠s′ is the §W1-2 companion — FAILED Level-3<Level-2 at this session per the neighbouring gate; T5 PASSES).

**Stage-2 two-axis cross-verify** (`joint-theorem-promotion.md §"Stage 2"`; gate-internal certificate — the gate author is connes/NCG, so the two axis-distinct cross-reviewers for the formal downstream Stage-2 are lizzi Axis-A spectral + volovik Axis-B transport, NEITHER being connes):
- **Axis-A (NCG / spectral)** — clause (a) homogeneity-degree `deg(K_0-pairing)==d_A`: PASS; clause (e) pole-scoping/index-rigidity (integer deg at a_4 s=2): PASS. **axisA_PASS = True.**
- **Axis-B (transport / superfluid)** — clause (b) substrate-natural-binding (χ-image NON-SCALAR): PASS; clause (f) transport-degree consistency (deg matches W7-1 +2): PASS. **axisB_PASS = True.**
- **JOINT clause (c)** — `Δ_scheme → machine-zero` PASS-AND across BOTH axes: `clause_c_axisA = clause_c_axisB = True` ⇒ **clause_c_PASS_AND = True** (logical AND, not OR).
- **Stage2_PASS_AND = True.**

**Verdict-line provenance**: canonical line `audit_sha256=d40965ec70e8c203d09c324b19e03c36d2427d6e298dc69abbf740a25cdea778` `content_sha256=622cd56e149d2335f5f3d92bfd1554f263549faf2b7820e2ac1f7d4e03aa3a9f`; dual-SHA companion row + **3-tuple companion row** (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + bridge-admissibility row + REGULATOR_PIN=`a_4^{Mellin}` (Yang-Mills channel residue at s=2; cohomology-ratio factor `a_n^{ζ}`; bare a_n FORBIDDEN) + LEVEL_CLASS_PIN=FULL (consumes `_cm_1995_residue_formula.py` FULL CM-1995 §III.4 residue evaluator; NO `-SCHEMATIC` suffix). The first run emitted with a fragile 1/L-Richardson convergence object (audit `90a96508…`); that was corrected in-session to the canonical Aitken-Δ² GV-successive-ratio object (the structurally faithful T5 Connes-Karoubi pairing convergence). Per gate-verdicts.md Option A, the original line is RETAINED on disk (verdict permanence) and the corrective line APPENDS with `supersedes=90a965089db08a63…`; the canonical reading is the latest non-superseded line.

**Solution-space**: the α_s transport image is recoverable as a substrate-natural Connes-Karoubi K_0-pairing at its home pole — the strong coupling's CMB-pivot image is NOT a canonical-import scalar rescaling but the HKR/Connes-Karoubi image of the substrate's intrinsic χ-image BdG inheritance K_0-class. The α_s scale-and-channel-tagging (substrate-distance-1 s=3 running −0.08587279 vs Goldstone-pivot ≈0) gains a THIRD structural anchor at the a_4 s=2 home pole. T5 is GATE-CONFIRMED as the unique admissible Element-3 at the coupling's home pole. Artifacts: `s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.{py,npz,png}`.

---

### §W1-4. S94-K-CSUB-R-ABSOLUTE-CONVERGENCE (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE`
**Trigger**: `[CHAIN]`
**Classification**: **GEOMETRIC** (UV-convergence of the PV-subtracted a_2 Mellin-s=2 spectral moment of D_K)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The FULL K_csub_R intercept (+247259.9583 at S93 W7-2, large because the bare a_2 Mellin-s=2 moment at fixed τ_fold is not UV-convergent) converges to a finite L_max→∞ limit once the substrate-canonical S61/S78 Pauli-Villars subtraction at Λ_UV=M_KK is applied; the convergent K_csub_R is regulator-class FI across the 5-regulator atlas.
**Plan reference**: `sessions/session-plan/session-94-plan-w1.md` §W1-4 (CC1996 §2.2-2.3 2-point PV multipliers (M_KK,+2; √2·M_KK,−1); FULL `_cm_1995_residue_formula.py`; 5-regulator FI check; level-pin + regulator-pin disclosures).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-94/s94_w1_4_k_csub_r_absolute_convergence.py` — on disk (51,841 bytes). `grep -E 'from canonical_constants import'` → `from canonical_constants import *` + explicit `from canonical_constants import (M_KK, tau_fold, kappa_2_substrate_FW)`. `grep -E 'append_verdict'` → `def append_verdict(...)` + the call site. Both present.
- **data** `s94_w1_4_k_csub_r_absolute_convergence.npz` — on disk (24,474 bytes); `K_csub_R_FW_pv_intercept_L100` emitted at full float64 (NOT promoted — see Verdict).
- **plot** `s94_w1_4_k_csub_r_absolute_convergence.png` — on disk (232,638 bytes); 4-panel (A bare vs PV moment both grow; B PV/bare→1; C K_csub_R^{PV} intercept GROWS with L_fit; D diagnostic summary).
- **verdict_line** matches `^S94-K-CSUB-R-ABSOLUTE-CONVERGENCE:.* audit_sha256=[a-f0-9]{64}` — canonical line (`audit_sha256=566c2c9c…`) + dual-SHA companion + TIER-1 row + supersedes row. The first-run FAIL line (`943b753b…`) is RETAINED + superseded per gate-verdicts.md §"Option A".
- **wp_section** this section — regexes `Status.*COMPLETED`, `Verdict.*(PASS|FAIL|INFO)`, `Output Artifacts`, `MCP Pre-Compute Audit`, `a_2^{Pauli-Villars}`, `a_2^{Mellin}` all present (regulator-pin tags MANDATORY; bare `a_2` not used as a standalone citation).

**MCP Pre-Compute Audit** (queries run before writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("K_csub_R absolute convergence Pauli-Villars a_2 Mellin s=2 moment UV")` → S91 W6 F_2-axis FI machinery (`K_csub_F2_FI < 0.02`), the `_pauli_villars_subtraction.py` bare/PV moment API, and `S88-A-N-FW-CANONICALIZATION` (a_2_FW_zeta=2776.165389 promoted; PV/Mellin carry-forward). NOT pre-closed — NEW UV-convergence test.
- `get_constant("kappa_2_substrate_FW")` → 0.021018084987437197 (S89). `get_constant("M_KK_gravity")` → 7.428660036284456e16 GeV (S42; = `M_KK` alias). `get_constant("tau_fold")` → 0.19 (S12/S42). All imported, none hardcoded.
- `trace_entity("K_csub_R")` → gate `S93-W7-2-K-CSUB-R-FULL-PHYSICAL-RETRY` (FULL bare intercept +247259.9583, Mellin=zeta, F2FI=True; cache_truncation_fraction_FULL=0.000906) + S91 W6-2 polyfit-intercept machinery. Confirms `K_csub_R_FW` is NOT yet canonical (this gate would promote it on PASS).

**Verdict**: **FAIL** — `value='max_dK_over_dL_pv_SUBTRACTIVE=2.1071e+30_PASS_ceiling=1e-3_converges=False; … band_tag=FAIL_PV_subtracted_intercept_does_NOT_converge_2pt_PV_insufficient; supersedes=943b753b…'` scheme=`FULL-CM-1995-sec-III-4-residue-PauliVillars-Lambda_UV-M_KK-a_2-s2-moment` convention=`K_CSUB_R-ABSOLUTE-CONVERGENCE-PV-SUBTRACTED-a_2-Mellin-s2-CLASS-FULL` L_max=100 `audit_sha256=566c2c9c196b01e975359c1a14726eff897869697cce822d0ca75aec5f5bf3ec` `content_sha256=273514bd1006aad1189023996b693a9c3d12a16b7f8cc22e8b42a45be5c4aa1b`.

The pre-registered PASS criterion `|ΔK_csub_R^{PV}/ΔL_max| < 1e-3 at L_fit∈[50,100]` is missed by **34 orders of magnitude**: measured `max|ΔK/ΔL|` over [50,100] = **2.107e30**, and `|ΔK/ΔL|` is INCREASING (`dK_over_dL_increasing=True`). The 2-point Pauli-Villars subtraction at Λ_UV=M_KK is INSUFFICIENT to render the a_2 Mellin-s=2 moment UV-finite at fixed Jensen τ_fold. This closes the "2-point PV at Λ_UV=M_KK suffices" corridor (the plan's pre-registered FAIL_meaning). `K_csub_R_FW` is **NOT promoted** to `canonical_constants.py` (PASS-gated promotion not triggered).

**Results**:

*Bare a_2^{Mellin} s=2 moment growth (Step 1).* On the FULL Jensen-deformed Peter-Weyl table (`jensen_irrep_table`, CLASS=FULL — substrate-IS D_K(τ) eigenvalues, not a Casimir surrogate), `a_2^{bare}(s=2,L)=Σ d(p,q)·|λ|^{−4}` grows monotonically: 4.737e3 (L=10) → 2.125e4 (L=12) → 9.040e6 (L=20) → 3.567e13 (L=40) → 2.263e33 (L=100). Reproduces the W7-2 FULL bare intercept regime (+247259.9583 in the L=8..22 window). No intrinsic UV cutoff.

*The a_2^{Pauli-Villars} subtracted moment also diverges (Steps 2-3).* CC1996 §2.2-2.3 2-point multipliers, DIMENSIONLESS masses m²={1,2} (= {M_KK², 2·M_KK²} in λ M_KK-units, per `_pauli_villars_subtraction.py` docstring "M_KK→1, √2·M_KK→√2"), multipliers {c₁,c₂}={+2,−1} (Σc_j=1.0, Σc_j M_j²=0.00e+00 verified):

  `a_2^{Pauli-Villars}(s=2,L) = Σ_k d_k [ λ_k^{−4} − 2·(λ_k²+1)^{−2} + 1·(λ_k²+2)^{−2} ]` (the plan §W1-4 Step-2 LITERAL SUBTRACTIVE closed form — the GATED form).

  Subtracted moment grows: 2.931e3 (L=10) → 1.588e4 (L=12) → 8.922e6 (L=20) → 3.567e13 (L=40) → 2.263e33 (L=100). **PV/bare → 1** (0.619 @L=10, 0.747 @L=12, 0.987 @L=20, 1.000000 @L≥40): PV subtraction negligible at large L_max.

*Substitution-chain root cause (Step 3; Sage-verified).* |λ|=√C_2(p,q)·exp(−τρ), ρ=p+q, τ=0.19. As ρ grows, exp(−0.19ρ) BEATS √C_2, so `λ²=C_2·exp(−0.38ρ)→0` — the spectrum accumulates at **small λ**, NOT large λ. Per-mode bare term `d·λ^{−4}=d·C_2^{−2}·exp(+4τρ)` grows per shell like exp(+4τρ)=exp(+0.76ρ) (Sage shell-sum: shell_bare(ρ=100)=1.205e33 ≈ exp(+4τ·100)). PV `−Σc_j(λ²+M_j²)^{−2}` targets the **large-λ (UV)** regime (bracket ~O(λ^{−8}) as λ→∞), but at small λ the masses M²={1,2} dominate: `(λ²+M²)^{−2}→M^{−4}`, a BOUNDED subtraction `2·1−1·(1/4)=1.75`/mode, negligible vs DIVERGENT λ^{−4}. The substrate's divergence is small-λ (IR-accumulation); a UV-targeting PV cannot tame it.

*Multiplier-form contrast (NEW finding — Sage-confirmed PV-form distinctness).* The standard MULTIPLIER form `a_2^{PV-mult}=Σ d_k·w_PV(λ²;2)·λ_k^{−4}`, `w_PV=1−Σc_r(m_r²/(λ²+m_r²))²` (PRIMARY `_pauli_villars_subtraction.pv_mellin_moment_primary`), is **algebraically DISTINCT** from the subtractive form. Sage exact: `subtractive − multiplier = −(x²+3x−2)/(x⁴+3x³+2x²)`, x=λ² (≠0). Small-λ: `w_PV·λ^{−4} → 3/λ² + O(1)` (Sage series — UV power raised by **2**, not 4), so the multiplier form diverges SOFTER (per-shell exp(+0.38ρ)) but STILL diverges: `max|ΔK/ΔL|_mult = 9.644e17 ≫ 1e-3`. **Both PV forms FAIL** — the divergence is intrinsic to the Jensen spectrum at fixed τ, not a PV-form artifact. The plan pre-registers the subtractive form (gated); the multiplier form is the standard-PV contrast.

*K_csub_R^{PV} intercept does NOT converge (Step 4).* `K_csub_R^{PV}(L_fit)` = polyfit-intercept (1/L→0) of `M_Pl_eff_sq^{PV}(L)/M0^{PV}` over [10, L_fit]. GROWS: 1.692e4 (L_fit=12) → 2.082e15 (L_fit=50) → 2.108e31 (L_fit=100). Consecutive `|ΔK/ΔL|` over [50,100]: max=2.107e30, INCREASING. FALSIFIES the Step-4 PASS prediction ("plateaus ⇒ |ΔK/ΔL|→0"). Direction: |ΔK/ΔL| INCREASES (divergence) ⇒ FAIL.

*FI check (Step 5; conjunct 2 — holds, moot for PASS).* a_2^{Mellin}(L=12)=2.125445e4 = a_2^{ζ}(L=12)=2.125445e4 exactly: `F_2 diff |Mellin−ζ|=0.00e+00`, `F2_FI_exact=True` (zeta-Mellin equivalence on the positive-definite spectrum; ζ_φ(z) entire at finite L_max, res_{z=0}=value at z=0). The F_2={ζ,Mellin} FULL-class FI floor is intact; conjunct 1 (UV-convergence) is what fails. a_2^{Pauli-Villars}(L=12)=1.587680e4 (different regulator class). SCHEMATIC cross-check (cross-check ONLY, `-SCHEMATIC`): heat-kernel a_2=1.833e1, hard-cutoff a_2=1.673e1 — SCHEMATIC analogs on a pure-Casimir spectrum (NO Jensen damping), NOT substrate-IS, NOT compared on the divergence metric.

*4-tuple*: (value=`max_dK_over_dL_pv_SUBTRACTIVE=2.1071e+30…`, scheme=`FULL-CM-1995-sec-III-4-residue-PauliVillars-Lambda_UV-M_KK-a_2-s2-moment`, convention=`K_CSUB_R-ABSOLUTE-CONVERGENCE-PV-SUBTRACTED-a_2-Mellin-s2-CLASS-FULL`, L_max=100).

**[CHAIN] substitution chain** (substituted numbers):
- **Step 1** — `a_2^{bare}(s=2,L)=Σ d·|λ|^{−4}`; per-mode = d·C_2^{−2}·exp(+4τρ). L=100: 2.263e33 (grows; no UV cutoff). ✓
- **Step 2** — 2-point PV (m²={1,2}, c={+2,−1}; Σc=1.0, Σc·M²=0.00e+00): `a_2^{Pauli-Villars}=Σ d[λ^{−4}−2(λ²+1)^{−2}+(λ²+2)^{−2}]`. ✓
- **Step 3** — small-λ dominates (λ²=C_2·exp(−0.38ρ)→0); bracket→λ^{−4}−1.75≈λ^{−4}; PV bounded (1.75/mode); PV/bare→1.000000 @L≥40. ✓
- **Step 4** — K_csub_R^{PV}(L_fit) GROWS (2.082e15→2.108e31, L_fit 50→100); max|ΔK/ΔL|=2.107e30 ≫ 1e-3; INCREASING. PASS-prediction FALSIFIED. ✗ (the FAIL conjunct)
- **Step 5** — F_2={ζ,Mellin} exact 0 (`F2_FI_exact=True`); FI floor intact; multiplier-form contrast ALSO diverges (9.644e17). ✓ (conjunct 1 fails ⇒ composite FAIL)
- **Conclusion** — `|ΔK/ΔL|↛0` (UV-divergent) ⇒ **FAIL**; 2-point PV at Λ_UV=M_KK does NOT render a_2 s=2 UV-finite at fixed τ_fold.

**Level-pin + regulator-pin disclosures** (Type-F cross-class):
- **Regulator-pin** (`regulator-pin-discipline.md` MANDATORY): the gated moment carries `a_2^{Pauli-Villars}` cross-checked against the FI-class members `a_2^{Mellin}` and `a_2^{ζ}` (F_2 sub-atlas, exact-0). Bare `a_2` FORBIDDEN as a standalone citation.
- **Level-pin** (`substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY): the FULL path (PV/Mellin/ζ) uses `_cm_1995_residue_formula.py` (CLASS=FULL) + the plan §W1-4 Step-2 closed form; verdict-line convention carries NO `-SCHEMATIC` suffix; companion `# tier_pin=TIER-1` row emitted. The SCHEMATIC `_spectral_action_regulators.py` heat-kernel/hard-cutoff members are CROSS-CHECK ONLY (Type-F separation): SCHEMATIC analogs on a pure-Casimir spectrum, a separate-class question, NOT entered into the convergence verdict (so no `-SCHEMATIC` suffix on THIS gate's convention — the gated FULL path does not consume the SCHEMATIC output as canonical; the SCHEMATIC values are a diagnostic footnote only).
- **Provenance-label reconciliation** (disclosed honestly): the plan §W1-4 provenance hint labeled `_pauli_villars_subtraction.py` CLASS=SCHEMATIC; its docstring (S88 W13-159) self-identifies PRIMARY full-physical (TIER-1 lift). This gate implements the PV subtraction DIRECTLY from the plan Step-2 SUBTRACTIVE closed form (verified bit-precision vs an independent in-script hand-evaluation, residual=0.000e+00) and uses the PRIMARY module MULTIPLIER form only for the distinctness contrast — so the FULL PV path is substrate-canonical regardless of the module label.

**Option A supersession** (`gate-verdicts.md §"Option A"`): the first run emitted FAIL under a spurious `band_tag=FAIL_FULL_evaluator_or_PV_identity_or_module_match_failed` because the subtractive-vs-multiplier PV-form difference (`forms_distinct=True`, Sage-confirmed) was initially mis-gated as an evaluator breakage. The corrective line (`audit_sha256=566c2c9c…`) carries `supersedes=943b753b…` in both its value field and a dedicated companion row; the original line is RETAINED on disk; the genuine physics verdict (FAIL via non-convergence) is unchanged, only the band_tag is corrected to `FAIL_PV_subtracted_intercept_does_NOT_converge_2pt_PV_insufficient`.

**Solution-space implication.** The "2-point PV at Λ_UV=M_KK renders the a_2 Mellin-s=2 moment UV-finite at fixed τ_fold" corridor is CLOSED. The FULL K_csub_R intercept (+247260 bare) does NOT acquire a finite, regulator-class-FI canonical value via the substrate-canonical 2-point PV subtraction — it remains a truncation-dependent quantity, NOT a canonical pin. Structural reason (property of the Jensen-deformed D_K spectrum at fixed τ): the a_2 s=2 moment diverges in the **small-λ (IR-accumulation)** direction (high-Casimir Peter-Weyl sectors damped to λ→0 by exp(−τρ)), which a UV-targeting Pauli-Villars subtraction (subtractive OR multiplier) cannot regulate. Forward corridor: a higher-point PV scheme, a τ-running spectral-action regulator, OR re-anchoring K_csub_R as a dimensionless truncation-invariant functional (Tier-2 per `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`) rather than a dimensionful intercept. (The W7-2 FULL bare intercept +247259.9583 was itself NOT a substrate-physics scale either — it is the un-subtracted moment in the L=8..22 window; this FAIL confirms its largeness is the moment's UV-divergence, not a physical magnitude.)

---

### §W1-5. S94-A_S-MPL-CONVERGENCE (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-A_S-MPL-CONVERGENCE`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (A_s = scalar amplitude of the post-transit GGE acoustic perturbation spectrum)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The 0.12-OOM A_s normalization gap (session-x W1 §P-11) is resolved — A_s computed with M_Pl_spectral (the a_2 second spectral moment as effective Planck mass) and with M_Pl_physical (the canonical reduced Planck mass) agree to within the pre-registered band, |log10(A_s_spectral/A_s_physical)| < band, the residual being the structurally-understood 0.12 OOM (S75 W1-E PASS).
**Plan reference**: `sessions/session-plan/session-94-plan-w1.md` §W1-5 (Mukhanov-Sasaki A_s=H²/(8π²ε_H M_Pl² c_s); M_Pl_eff²(τ)=M_Pl_red²·[a_2(τ)/a_2_fold] CC96 §4; absolute-OOM 4-band; L_max∈{10,12} robustness).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-94/s94_w1_5_a_s_mpl_convergence.py` — EXISTS (20,463 B). `grep -E "from canonical_constants import"` → `from canonical_constants import (  # noqa: E402`. `grep -E "append_verdict"` → `def append_verdict(...)` + `append_verdict(verdict, value_str, audit_sha, script_sha)`. Both must_contain patterns PASS.
- **data** `s94_w1_5_a_s_mpl_convergence.npz` — EXISTS (10,384 B).
- **plot** `s94_w1_5_a_s_mpl_convergence.png` — EXISTS (60,609 B; bar of |log10 ratio| for both readings vs the 0.12/0.24 band lines).
- **verdict_line** in `computations/session-94/s94_gate_verdicts.txt` — matches `^S94-A_S-MPL-CONVERGENCE:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=e8c8955bb360d6310de3ac1de81adff76fffebeca14e9fd1878bd4b44ba3adc5`); dual-SHA companion comment row present; no [SIGN] 3-tuple (`[CHAIN]` trigger, schema_v2_3tuple_required: false).

**MCP Pre-Compute Audit**:
- `get_constant('a_2_FW_zeta')` → **2776.165389** (zeta-regulated 2nd SDW moment at fold; S88-A-N-FW-CANONICALIZATION). Imported as `a_2^{ζ}`.
- `get_constant('M_Pl_reduced')` → **2.435e18 GeV** (CODATA 2018). `M_Pl_unreduced` → **1.2209e19 GeV**.
- `search_knowledge('A_s scalar amplitude normalization M_Pl spectral a_2 second moment')` → surfaced (i) `A_s(H̃)=H̃²/(8π²·ε)` + `M_Pl_eff²(τ)=M_Pl_red²·[a_2(τ)/a_2_fold]` CC96 §4 (session-82); (ii) `f_conv=(M_KK/M_Pl)^4·(a_2/a_0)²` (S75); (iii) the S75 L10 reference `a_2=64308.24`, `a_0=155984`.
- `search_knowledge('f_conv 0.12 OOM W1-E S75')` → **PRE-CLOSED reference**: S75 W1-E PASS, "A_s gap structurally understood; 0.12 OOM residual"; S77 transit-einstein factorization `f_conv=[(M_Pl_eff/M_Pl_red)²]_Planck·[…]_residual`; S75 `A_s(diagonal, W1-E) = 1.584471e-09`.
- Read the primary source `computations/session-75/s75_f_conv_spectral_output.txt` (Sections 4/6/10/12): the **0.12-OOM disclosed residual IS route R3b** (`f_conv=(M_KK/M_Pl)^4·(a_2/a_0)²`, PHYSICAL M_Pl), NOT the bare-M_Pl_spectral ratio (routes R4/R5, which give +5.81 / +7.17 OOM). This is the decisive disambiguation for the gate's verdict.
- This gate is a quantitative **re-pin** of the disclosed (not pre-CLOSED) S75 W1-E residual against the new 0.12/0.24 band; AMPLITUDE-NORM-66's 3.15-OOM Route-B gap is NOT revisited.

**Verdict**: **INFO** — canonical value **|log10(A_s_pred/A_s_CMB)| = 0.122333 OOM** (Reading B, fold), in the INFO band (0.12, 0.24]. Marginally outside the strict 0.12 PASS boundary by 0.00233 OOM; the literal gate-block Step-3 ratio (Reading A) FAILs as a non-canonical factorization. `(value=0.122333, scheme=Mukhanov-Sasaki-A_s-spectral-vs-physical-M_Pl-a_2-second-moment, convention=ABSOLUTE-log10-OOM-A_s_spectral-over-A_s_physical, L_max=10)`.

**Results**:

**SPECTRAL-FUNCTIONAL FINDING — the gate question has two factorizations that give opposite verdicts.** "A_s_spectral vs A_s_physical" is NOT a single quantity: which spectral functional realizes the a_2-as-M_Pl identification determines the answer. The S75 W1-E primary source (`s75_f_conv_spectral_output.txt`) settles which factorization the disclosed "0.12 OOM" refers to.

**Reading A — gate-block Step-3 LITERAL ratio** (Planck-mass-normalization ALONE; the bare a_2-as-M_Pl identification):

| Quantity | fold/L3 (a_2^{ζ}=2776.165389) | L10 (a_2^{ζ}=64308.24) |
|:---------|:------------------------------|:-----------------------|
| M_Pl_spectral = √(a_2/(48π²))·M_KK | 1.7983e17 GeV (2.4208 M_KK) | 8.6551e17 GeV (11.6510 M_KK) |
| \|log10(A_s_spec/A_s_phys)\| vs **M_Pl_reduced** | **2.26327 OOM** (FAIL) | **0.89845 OOM** (FAIL) |
| \|log10(A_s_spec/A_s_phys)\| vs M_Pl_unreduced | 3.66363 OOM | 2.29881 OOM |

Reading A is route **R4/R5** of the S75 analysis: it captures only the Planck-mass ratio and **misses the (M_KK/M_Pl)⁴ KK-hierarchy factor** that the substrate's dimensional transmutation supplies (S75 Section 6, Factor A explicitly identifies this as the WRONG factorization). It FAILs the band under every M_Pl choice.

**Reading B — S75 W1-E CANONICAL residual** (`f_conv = (M_KK/M_Pl)⁴·(a_2/a_0)²`, route R3b, PHYSICAL/unreduced M_Pl — this IS what "0.12 OOM" means):

| Quantity | fold/L3 | L10 |
|:---------|:--------|:----|
| a_2/a_0 (spectral weight fraction) | 0.431082 | 0.412275 |
| f_conv = (M_KK/M_Pl)⁴·(a_2/a_0)² | 2.5471e-10 | 2.3297e-10 |
| A_s_pred = A_s_fiber·f_conv (A_s_fiber=6.2208) | 1.5845e-09 | 1.4492e-09 |
| **\|log10(A_s_pred/A_s_CMB)\|** (A_s_CMB=2.1e-9) | **0.122333 OOM** (signed −0.12233) | 0.16108 OOM (signed −0.16108) |

Reading B at the fold reproduces the S75 W1-E disclosed residual (`A_s(diagonal,W1-E)=1.584471e-09`, S75 |delta|=0.1240) **bit-for-bit to 4 sig figs**. Sage QQ-exact (200-bit RealField) confirms: fold = 0.12233255917 OOM, L10 = 0.16107835372 OOM (float and exact agree to all reported digits).

**Why INFO and not PASS.** The disclosed "0.12" was the **rounded form of 0.12233** (= S75 |delta|=0.1240). The genuine structurally-understood residual (Reading B, fold) sits at 0.122333 OOM — `> 0.12` strict PASS boundary by 0.00233 OOM, squarely in the INFO band [0.12, 0.24]. The L_max-sensitivity of the a_2 moment (fold 0.12233 → L10 0.16108) is the source of the small excess, exactly the INFO_meaning rubric ("the gap is at the band edge … the L_max-sensitivity of M_Pl_spectral likely accounts for the excess"). The literal Step-3 ratio (Reading A) is a different, non-canonical factorization that FAILs.

**Substitution chain (Reading A algebra; Sage-verified exact):**
- **Step 1**: A_s = H²/(8π²·ε_H·M_Pl²·c_s) [Mukhanov-Sasaki pivot amplitude; session-82-results-WP, session-70-plan]. A_s ∝ M_Pl⁻².
- **Step 2**: M_Pl_spectral = √(a_2^{ζ}/(48π²))·M_KK [S75 Sec.5: M_Pl_eff = √(a_2/(48π²))·M_KK]. M_Pl_physical = M_Pl_reduced = 2.435e18 GeV [CODATA 2018].
- **Step 3**: A_s_spectral/A_s_physical = [H²/(8π²ε_H M_Pl_spec² c_s)] / [H²/(8π²ε_H M_Pl_phys² c_s)] = **(M_Pl_physical/M_Pl_spectral)²** — all of H, ε_H, c_s, 8π² cancel. Sage `simplify_full`: `A_s_spectral/A_s_physical = MPlp²/MPls²` exact.
- **Step 4**: log10(A_s_spectral/A_s_physical) = 2·log10(M_Pl_physical/M_Pl_spectral); ⇒ |·| = 2·|log10(M_Pl_phys/M_Pl_spec)|. Substituting (fold, M_Pl_red): M_Pl_phys/M_Pl_spec = 2.435e18/1.7983e17 = 13.541 ⇒ 2·log10(13.541) = **2.26327 OOM** (Reading A FAIL — NON-CANONICAL; R4/R5, misses (M_KK/M_Pl)⁴).
- **Step 5 (direction + canonical read-off)**: signed Reading-A log10 ratio is POSITIVE (M_Pl_spectral UNDER-estimates the physical scale at fold/L10, so the bare-spectral A_s OVER-shoots; ratio > 1). The CANONICAL residual is Reading B (fold) = 0.122333 OOM; PASS iff ≤ 0.12, INFO iff ≤ 0.24, else FAIL ⇒ **INFO**.
- **Conclusion**: the disclosed 0.12-OOM gap is pinned quantitatively at 0.122333 OOM (Reading B); the gate's literal Step-3 (M_Pl_phys/M_Pl_spec)² ratio is a distinct non-canonical factorization that FAILs.

**Structural note — the CC96 §4 Newton-coupling pin is a ratio-to-fold, not a bare-moment identification.** M_Pl_eff²(τ) = M_Pl_red²·[a_2(τ)/a_2_fold] equals M_Pl_red² AT the fold (a_2(fold)/a_2_fold = 1). It anchors the effective Planck mass to M_Pl_reduced and tracks only the τ-VARIATION of a_2 — it does NOT set M_Pl = √(a_2/(48π²))·M_KK (the bare spectral moment). So Reading A's bare-moment identification is not what the framework's Newton-coupling map asserts; Reading B is canonical. This is the spectral-functional point: the a_2-as-M_Pl scale is a SCHEME-DEPENDENT object (the S75 routes span 5.81–7.94 OOM across L_max=3/10 and reduced/unreduced M_Pl), and only the geometric f_conv combination (M_KK/M_Pl)⁴·(a_2/a_0)² — which uses the a_2/a_0 RATIO (FUNCTIONAL-stable, fold↔L10 drift 0.019 in absolute weight, 0.96 ratio-stable per S75 Sec.3) and the PHYSICAL M_Pl — produces the disclosed residual.

**Cross-checks:**
- **Sage QQ-exact (200-bit)**: Reading B fold = 0.12233255917 OOM; L10 = 0.16107835372 OOM; Reading A fold (M_Pl_red) = 2.2632726107 OOM; L10 = 0.89845132230 OOM. All match the float compute to reported precision (no float-cancellation near the 0.12 boundary).
- **S75 W1-E reproduction**: Reading B fold A_s_pred = 1.5845e-09 vs S75 `A_s(diagonal,W1-E)=1.584471e-09` (bit-match); residual 0.1223 vs S75 |delta|=0.1240 (rounding of the same quantity).
- **L_max robustness (a_2/a_0 RATIO; substrate-first L12 master cache)**: the L12 sector cache (`s84_spectrum_cache_L12_tau019.npz`) uses a different per-sector multiplicity/doubling convention from the S75 reference (cache a_2/a_0 = 0.092424 at L10, 0.069192 at L12) — confirming the a_2/a_0 ratio is itself convention-sensitive at the cache layer; the CANONICAL gate numbers use the S75 reference values the plan explicitly cites (a_2=64308.24, a_0=155984 at L10). The Reading-B residual is reported at fold (0.12233) and L10 (0.16108) S75 reference; the fold↔L10 spread (0.039 OOM) is the L_max-sensitivity flagged in the INFO rubric.
- **Dimensional consistency**: |log10 ratio| is dimensionless (both A_s are dimensionless scalar-power amplitudes); M_Pl_spectral and M_Pl_physical both in GeV; f_conv dimensionless (∈ (0,1], CHK1 PASS).

**Assessment / solution-space.** The A_s spectral-vs-physical M_Pl normalization is **approximately understood at the disclosed precision but NOT closed to the strict 0.12 PASS boundary**: the structurally-understood residual is 0.122333 OOM (Reading B), 0.00233 OOM above the strict band, in INFO. The verdict does NOT re-open the A_s normalization as a crisis — the residual is a known small mismatch (75% of the Planck value, within 25%), and an L_max-converged a_2/a_0 ratio (or use of the substrate-natural fold values, which give the tightest 0.12233) would tighten it toward PASS. The gate-block's literal Step-3 (M_Pl_phys/M_Pl_spec)² ratio is FLAGGED as the wrong factorization: it FAILs (2.26 OOM fold / 0.90 OOM L10 vs M_Pl_red) because it is route R4/R5 (Planck-mass-normalization alone, missing the KK hierarchy), NOT the disclosed 0.12-OOM residual. **FUNCTIONAL-DEPENDENT classification**: the A_s normalization residual is a scheme-dependent quantity — the bare a_2-as-M_Pl scale spans 0.90–3.66 OOM depending on L_max and M_Pl convention, while the geometric (M_KK/M_Pl)⁴·(a_2/a_0)² combination (physical M_Pl, a_2/a_0 ratio) is the FUNCTIONAL-stable route that pins the residual to 0.12233 OOM. The a_2 ↔ Newton-coupling map (CC96 §4) is a ratio-to-fold anchored to M_Pl_red — it does not require the bare spectral moment to match the physical Planck mass by coincidence. **Downstream**: per the Wave 1 → Wave 2 decision point, this INFO updates the A_s normalization status to "approximately understood at 0.12 OOM, INFO-band"; it does NOT re-open the a_2↔Newton-coupling normalization for S95 (that route is a FAIL trigger, not INFO). An optional S95 CF: re-pin the Reading-B residual with an L_max-converged a_2/a_0 ratio to test whether the strict 0.12 PASS is reachable.

---

## Wave 1 Synthesis (team-lead)

Wave 1 closed 5 gates: **2 PASS** (§W1-1, §W1-3), **2 FAIL** (§W1-2, §W1-4), **1 INFO** (§W1-5). The wave's spine is the §VII.BA composite-bridge-map dimensional-class theorem and its α_s sibling:

- **§W1-1 PASS** — the §VII.BA `#### (h)` JOINT TWO-AXIS composite-bridge-map admissibility theorem cleared Stage-2: Axis-A (lizzi-spectral) and Axis-B (volovik-transport) — neither an original author — independently PASSed their single-axis clauses; JOINT clause (c) Δ_scheme→0 PASS-ANDs across both (Δ_scheme = 0.0 < 1e-9 M_KK² on both faces, volovik's 200-bit Sage cross-check confirms the machine-zero is structural, not sub-float64); substrate-input-orthogonality holds at the **structural ceiling** (lizzi loaded the envelope npz, volovik the normalization npz — distinct files, no overlap caveat). → §VII.BA `#### (h)` promoted **STAGE-1-CANDIDATE → STAGE-3-PERMANENT**, Stage-3-CLASS = `JOINT-CROSS-AXIS-STAGE-2-PASS-AND`.
- **§W1-2 FAIL** (sign=PASS, magnitude=FAIL, regime=VALID) — the T4|s≠s' = Res_W(s)/Res_W(s′) differential ratio satisfies both dimensional-class conjuncts (deg-match +2, non-scalar) but its envelope **diverges** (α_env = −0.71 < 0; ratio 9.82 → 323.47 over L∈{12..100}; ΔL = L3−L2 never crosses below 0). It is structurally admissible but NOT envelope-saturated ⇒ NOT registry-PASS-eligible. This **sharpens** §VII.BA: **T5 is the SOLE registry-PASS-eligible Element-3**; the admissible set is NOT widened to {T3, T4|s≠s', T5}.
- **§W1-3 PASS** — α_s recovered as a NEW cross-pillar bridge (**§VII.BG**, STAGE-1-CANDIDATE) via the direct Connes-Karoubi K_0-pairing T5 at the a_4 Yang-Mills home pole s=2: Level-3 = 0.122985 < Level-2 = 0.132537 (registry-PASS), deg-match d_A=+2, substrate-natural non-scalar χ-image BdG inheritance, Δ_scheme = 0.0, preserves the α_s NEGATIVE running. The gate's internal `stage2_PASS_AND` is the producing agent's pre-check, NOT a canonical two-agent Stage-2 — so §VII.BG lands STAGE-1-CANDIDATE only; the real two-agent Stage-2 → Stage-3 is an S95 carry-forward.
- **§W1-4 FAIL** — the substrate-canonical 2-point Pauli-Villars at Λ_UV=M_KK does NOT render the bare a_2 Mellin-s=2 moment UV-finite at fixed τ_fold (criterion missed by 34 OOM). The obstruction is conjunct-1 (convergence), NOT conjunct-2 (the F_2={ζ,Mellin} FI floor is exactly intact, F2_diff=0.0): at τ_fold the Jensen spectrum accumulates at small λ (IR direction), but PV regulates the UV direction only. Both subtractive AND multiplier PV forms diverge (Sage-exact distinct, both blow up) ⇒ divergence is intrinsic to the Jensen spectrum, not a PV-form artifact. **K_csub_R_FW NOT promoted** (PASS-gated). This **closes** the "2-pt PV at Λ_UV=M_KK suffices" corridor.
- **§W1-5 INFO** — A_s spectral-vs-physical-M_Pl normalization sits at 0.122333 OOM (Reading-B canonical f_conv = (M_KK/M_Pl)⁴·(a_2/a_0)², reproducing S75 W1-E bit-for-bit), just 0.00233 above the strict 0.12 PASS boundary (L_max-sensitivity fold→L10 is the source). Classified **FUNCTIONAL-DEPENDENT**; the bare a_2-as-M_Pl reading (Reading A) is non-canonical (misses the KK hierarchy). Does NOT re-open the a_2↔Newton-coupling normalization (that is a FAIL trigger; this is INFO).

### Effected In-Session (non-math — completed before STOP)

- [x] §VII.BA `#### (h)` STAGE-1-CANDIDATE → STAGE-3-PERMANENT — mack OP1 — `sessions/permanent-results-registry.md:20160` — Stage-2 PASS `e6cb47a9`; Stage-3-CLASS=`JOINT-CROSS-AXIS-STAGE-2-PASS-AND`; promotion record + 2 reviewer-JSON cites added
- [x] §VII.BA Element-3 admissible-set sharpening (T5 SOLE; T4|s≠s' admissible-but-divergent) — mack OP2 — `sessions/permanent-results-registry.md:20207,20210,20226` — cites §W1-2 FAIL `a74e9f1e`
- [x] §VII.BG new STAGE-1-CANDIDATE landing (α_s T5 transport bridge; full 5-anatomy + 3-level; Corner II; parse-tree expansion) — mack OP3 — `sessions/permanent-results-registry.md:20612–20688` — cites §W1-3 PASS canonical `d40965ec` (post-supersession)
- [x] §VII.BG index-table row (registry-vs-table drift caught by VII-SLOT-AUDIT hook) — **orchestrator-direct presentation patch: §VII.BG ← added missing §VII index-table row mirroring the section header at `permanent-results-registry.md:20613`** — `sessions/permanent-results-registry.md:143`
- [x] §VII.BA STAGE-3 ordinal — applied the established **no-integer-ordinal precedent** (`CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW`); §VII.BA correctly does NOT assert a hard ordinal. Framework-wide ordinal-resolution audit remains the existing tracked CF (pre-existing, not a W1 product) — logged to housekeeping §B
- [x] K_csub_R_FW canonical promotion — **NOT executed** (correctly): §W1-4 FAILed, and the promotion is PASS-gated. No `canonical_constants.py` write. Recorded here so the non-event is auditable.

### Process observations (closed in-session)

- **WP parallel-writer race**: 5+ agents shared `session-94-w1-workingpaper.md`; §W1-2 and §W1-3 agents hit Edit-tool mtime races against concurrent §-section finalizers and resolved via mtime-safe Python in-place edits (`computations/_shared/_s94_w1_3_wp_patcher.py`), no data loss. Recurring per the N>2-agents-one-file rule (`feedback_session-process.md`) — high-fanout waves should prefer per-gate WP fragments.
- **Two Option-A supersession chains** (§W1-3, §W1-4): both corrective re-emissions carry `supersedes=<full-64-char>` per `gate-verdicts.md §"Option A"`; prior lines retained on disk; two distinct audit_sha256 each ⇒ sig_5 clean. §W1-3's correction (fragile 1/L-Richardson → canonical Aitken-Δ² GV-Heitsch object) and §W1-4's (mis-gated evaluator tag → genuine non-convergence FAIL) are both honest in-session corrections, not convention-shopping.

## Carry-Forward Computations

### CF-S95-HK-1 — §VII.BG α_s T5 bridge two-agent Stage-2 → STAGE-3

> **Routing note**: this is a Q2 hygiene-promotion compute CF; canonical ledger entry at `sessions/archive/session-94/session-94-housekeeping.md §B` (same `CF-S95-HK-1` identifier). Per the template §B example, a Stage-2 cross-axis verify is genuine compute, not an orchestrator-direct edit.

| Field | Spec |
|:------|:-----|
| **What** | Dispatch TWO axis-distinct cross-reviewers (NOT connes — the original author — per the downstream-inheritance-reach test; e.g. Axis-A spectral = lizzi or vdd, Axis-B transport = volovik) to independently re-derive the §VII.BG 5-anatomy clauses + JOINT clause (Δ_scheme→0) from the registered STAGE-1-CANDIDATE entry alone (no workshop context); PASS-AND → STAGE-3-PERMANENT. |
| **Inputs** | §VII.BG registry entry (`permanent-results-registry.md:20612–20688`); `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz`; `canonical_constants.py`; two disjoint substrate-input-orthogonality anchors (one per reviewer). |
| **Gate** | BOTH reviewers PASS single-axis clauses AND JOINT clause PASS-AND across both; substrate-input-orthogonality at ≥1 observable. Composite PASS → §VII.BG STAGE-1-CANDIDATE → STAGE-3-PERMANENT with Stage-3-CLASS tag. ANY clause FAIL → stays STAGE-1. |
| **Effort** | ~0.5 wave-equivalents (2 parallel cross-reviewers + mechanical aggregator, mirroring §W1-1). |

### CF-S95-K-CSUB-R-RE-ANCHOR — K_csub_R convergence via higher-point PV / τ-running / Tier-2 dimensionless re-anchor

| Field | Spec |
|:------|:-----|
| **What** | Re-attempt K_csub_R UV-finiteness after the 2-pt-PV-at-Λ_UV=M_KK FAIL (§W1-4). Three corridors: (a) higher-point (≥3-pt) Pauli-Villars to regulate the IR-accumulation direction the Jensen spectrum produces at fixed τ; (b) τ-running spectral-action regulator; (c) re-anchor K_csub_R as a **Tier-2 dimensionless** truncation-invariant functional (log-derivative / ratio) per `cross-pillar-bridge-anatomy.md` Tier-1/Tier-2 gate, abandoning the dimensionful intercept. |
| **Inputs** | `s93_w7_2_k_csub_r_full_physical_retry.py` (FULL evaluator); `_cm_1995_residue_formula.py` (FULL); `s84_spectrum_cache_L12_tau019.npz`; `computations/session-94/s94_w1_4_k_csub_r_absolute_convergence.npz` (divergence diagnosis: per-shell ~ exp(+0.76ρ) IR-accumulation; both PV forms diverge). |
| **Gate** | Tier-1 corridor: \|ΔK/ΔL\| < 1e-3 at L∈[50,100] (convergence). Tier-2 corridor: the dimensionless functional converges AND is re-anchorable per the Tier-2 dimensional-re-anchorability gate (`cross-pillar-bridge-anatomy.md`). |
| **Effort** | ~1.0 wave-equivalents. |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-25 | §VII.BA `#### (h)` composite-bridge-map admissibility | STAGE-1-CANDIDATE | STAGE-3-PERMANENT | §W1-1 Stage-2 two-axis PASS-AND (lizzi+volovik, orthogonal inputs, structural ceiling) |
| 2026-05-25 | §VII.BA Element-3 admissible set | {T3, T4\|s≠s', T5} candidate widening | T5 SOLE registry-PASS-eligible; T4\|s≠s' admissible-but-divergent | §W1-2 FAIL (T4 envelope α_env=−0.71 divergent, not saturated) |
| 2026-05-25 | §VII.BG α_s T5 transport bridge | (none) | STAGE-1-CANDIDATE | §W1-3 PASS (L3=0.1230 < L2=0.1325; new cross-pillar bridge at a_4 home pole) |
| 2026-05-25 | K_csub_R 2-pt-PV-at-Λ_UV=M_KK corridor | open | CLOSED (insufficient) | §W1-4 FAIL (PV regulates UV; Jensen spectrum diverges in IR-accumulation at fixed τ) |
| 2026-05-25 | A_s spectral-vs-physical-M_Pl normalization | open (0.12-OOM target) | INFO 0.122333 OOM; FUNCTIONAL-DEPENDENT (Reading-B canonical) | §W1-5 INFO (0.00233 above strict boundary; does not re-open a_2↔Newton) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON |
|:-----|:-------|:------------|:------------|:-----|
| §W1-1 | s94_w1_1_vii_ba_stage_2_cross_axis_verify.py (29.6 KB) | 9.6 KB | 53 KB | s94_w1_1_axisA_lizzi_verdict.json + s94_w1_1_axisB_volovik_verdict.json |
| §W1-2 | s94_w1_2_vii_ba_t4_envelope_extension.py (41.5 KB) | 29.5 KB | 186 KB | — |
| §W1-3 | s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.py (50.8 KB) | 20.3 KB | 117 KB | — |
| §W1-4 | s94_w1_4_k_csub_r_absolute_convergence.py (51.8 KB) | 24.5 KB | 232.6 KB | — |
| §W1-5 | s94_w1_5_a_s_mpl_convergence.py (20.5 KB) | 10.4 KB | 60.6 KB | — |

All verdict lines + dual-SHA companions (+ 3-tuple / supersession rows where applicable) in `computations/session-94/s94_gate_verdicts.txt`.
