# Session 89 Wave W2 — Connes-Karoubi pairing canonical pipeline + 3He-B inheritance retry (Results Working Paper)

**Session**: 89 | **Wave**: W2 | **Plan**: session-89-plan-w2.md | **Theme**: Connes-Karoubi pairing canonical infrastructure (A.3) → BCS-physics-grounded R_substrate via landau path (A.4) → χ' independent inheritance morphism with M_3(ℂ) annihilation as derived theorem (A.7) → Stage-2 dual-prior pre-registration on the canonical pairing (A.20) → chirality-fidelity 3-proxy recompute upgrading §VII.AQ Level-3 anchor canonical-import → substrate-natural binding (A.40).

## Gate Sections

### §W2-1. S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE (connes-ncg-theorist)

**Status**: CLOSED (composite verdict FAIL)
**Gate ID**: `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Connes-Karoubi pairing canonical infrastructure on BdG-restricted sub-algebra image; Level-1 cohomology-class identity)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: R_canonical = ⟨[φ_g^sym]_BdG, [Ch(P_0(τ_fold))]_BdG⟩ at L_max=10 on A_K^BdG_preimage admits a closed-form bit-precision evaluation matching R_universal_HP1_strict_F4 = 1.030902 within Class-A 0.0095% F_4 strict AND matching substrate_cocycle_ratio_67_88 = 7.324992 within bit-identity 1e-12.
**Plan reference**: `sessions/session-plan/session-89-plan-w2.md` §W2-1 (machinery pin, thresholds, two cross-checks: substrate cocycle ratio bit-identity 7.324992 + Class-A F_4 strict).

**Substrate framing** (plan §W2-1.13 verbatim; per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`):

> The Hochschild cocycle `[φ_g^sym]_BdG` IS the substrate-IS observable on the BdG-restricted sub-algebra image `A_K^BdG_preimage`; it is NOT "in" any 3He-B container. The Chern character `[Ch(P_0(τ_fold))]_BdG` IS the K-theoretic image of the band-0 Peter-Weyl projector `P_0(τ_fold)` restricted to the BdG sub-algebra. The Connes-Karoubi pairing `R_canonical` IS the bridge map between Hochschild cohomology and K-theoretic Chern character images per `cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing"`; it is NOT a comparison "between two containers." `A_K^BdG_preimage` IS the substrate algebra restricted to the BdG-inheritance-morphism image; it is NOT a container "for" the substrate. Direction of explanation: D_K eigenvalues → spectral-action moments → Hochschild cocycle norms → Connes-Karoubi pairing R_canonical → substrate-IS bit-identity 7.324992. NEVER explain R_canonical via "3He-B observables in curved spacetime"; ALWAYS explain via the substrate's inheritance-morphism image at A_K^BdG_preimage.

**Single-τ-slice level declaration** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`): §W2-1 operates at **Level 1 (single-τ-slice substrate-IS)** at τ_fold = 0.190 (R-PROTECTED). The L_max=10 operational truncation is a regulator-axis pin; the Connes-Karoubi pairing infrastructure is intrinsic to the spectral triple at the fixed τ-anchor.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("Connes-Karoubi pairing BdG-restricted Hochschild cocycle Chern character")` | Prior gate `S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` (S87) landed value=0.0950 (match/envelope ratio under W-5 calibration corpus instance #1) — closely related but DIFFERENT observable. `S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` PASSed `target_ratio=793346/108307` confirming substrate cocycle ratio canonical. |
| `search_knowledge("R_universal_HP1_strict_F4 1.030902 substrate cocycle ratio 7.324992")` | 9 equation hits confirm `substrate_cocycle_ratio_67_88 = 7.324992` (Sage-exact at machine precision per W-5 R2-B Convergence #3) AND `R_universal_HP1_strict_F4 = 1.030902` per W-5 V4 substitution chain Step 2 are TWO DISTINCT canonical observables. |
| `get_constant("substrate_cocycle_ratio_67_88")` | `7.324992` (S86 W-5 R2-B Convergence #3; W-5 CANONICAL-5; matches plan pin). |
| `get_constant("R_universal_HP1_strict_F4")` | `1.030902` (S86 W-5 V4 substitution chain Step 2; W-5 CANONICAL-2; matches plan pin). |
| `get_constant("cocycle_norm_phi67")` | `0.793346` (S86 W-5 C2 substrate-magnitude; W-5 CANONICAL-3). |
| `get_constant("cocycle_norm_phi88")` | `0.108307` (S86 W-5 C2 substrate-magnitude; W-5 CANONICAL-4). |
| `get_constant("tau_fold")` | `0.19` (S12/S42 CONST-FREEZE-42; matches plan pin). |
| `trace_entity("Connes-Karoubi pairing BdG-restricted")` (implicit via search) | NO PRE-CLOSED closure on the BdG-restricted variant; closest is the S87 PILLAR-III-IV bridge gate at substrate-distance-1 normalization. |

Outcome of audit: gate is structurally new at the BdG-restricted variant. Two canonical observables retrieved (cocycle ratio 7.324992; HP^1 universal F_4 strict 1.030902); they are STRUCTURALLY DISTINCT scalars. Proceeding with computation.

**Sage-QQ substitution chain** (substituted numerical values from Fraction arithmetic on canonical-pin rationals):

- **Step 1 (Definitions)** —
    - `cocycle_norm_phi67 = 0.793346` (canonical pin; 6-sig-fig publication form)
    - `cocycle_norm_phi88 = 0.108307` (canonical pin; 6-sig-fig publication form)
    - `substrate_cocycle_ratio_67_88 = 7.324992` (canonical pin; 7-sig-fig published target)
    - `R_universal_HP1_strict_F4 = 1.030902` (canonical pin; HP^1 F_4-strict universal anchor)

- **Step 2 (Substitute)** — by plan §W2-1.6 Step 5 structural argument (the BdG-restriction inherits the substrate cocycle ratio bit-identity under the (Δ_B/Δ_A)^p cancellation theorem):
    - R_canonical(BdG-restricted) = ‖φ_67‖_BdG / ‖φ_88‖_BdG = cocycle_norm_phi67 / cocycle_norm_phi88
    - Fraction(793346, 1000000) / Fraction(108307, 1000000) = Fraction(793346, 108307)

- **Step 3 (Simplify)** —
    - R_canonical = **793346 / 108307 = 7.324974378387362** (Sage-QQ exact; full float64)

- **Step 4 (Cross-check 1 — substrate cocycle ratio bit-identity)** —
    - target = 7.324992; rel_dev = |7.324974378 − 7.324992| / 7.324992 = **2.405684e-06**
    - threshold = 1e-12 (RATIO; plan §W2-1.9 xc1)
    - **xc1 = FAIL by 6 OOM** (publication-precision-floor failure; see diagnostic below)

- **Step 5 (Cross-check 2 — HP^1 universal F_4 strict)** —
    - target = 1.030902; rel_dev = |7.324974378 − 1.030902| / 1.030902 = **6.105403e+00 (610.5%)**
    - threshold = 9.5e-5 (RATIO; plan §W2-1.9 xc2 Class-A 0.0095%)
    - **xc2 = FAIL by 4 OOM** (different-observable failure; see diagnostic below)

- **Step 6 (Direction)** — composite_verdict = FAIL per plan §W2-1.9 FAIL clause (xc1 fails). sign_verdict = N/A ([VERIFY-THEOREM] gate; no signed direction). magnitude_verdict = FAIL. regime_verdict = VALID (truncation_consistent at L_max=10; Friedrich-Bär saturation valid).

**Verdict** (canonical line + dual-SHA companion + 3-tuple companion verbatim from `computations/session-89/s89_gate_verdicts.txt`):

```
S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: FAIL -- value='R_canonical=7.32497437838736;xc1=False;xc1_rel_dev=2.406e-06;xc2=False;xc2_rel_dev=6.105e+00;diag=class-8-3-pub-precision-and-xc2-diff-observable' scheme=Hochschild-cocycle-times-Chern-character convention=BdG-restricted-Connes-Karoubi-pairing-Connes-Moscovici-1995-III.4 L_max=10 audit_sha256=f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d content_sha256=13ff225857223c1e0e07a9f737fa3932e6f124646ad07a25a8489bf2ac84151e schema_version=S87+
# audit_sha256_short=f67458d183a95be8 content_sha256_short=13ff225857223c1e # S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE dual-SHA companion row (W9a-99 split)
# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID # S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE 3-tuple annotation (S87 schema-v2)
```

**Results**:

| Field | Value |
|:------|:------|
| 4-tuple | `(value=R_canonical=7.32497437838736, scheme=Hochschild-cocycle-times-Chern-character, convention=BdG-restricted-Connes-Karoubi-pairing-Connes-Moscovici-1995-III.4, L_max=10)` |
| R_canonical_value | 7.324974378387362 (Sage-QQ exact: 793346/108307) |
| Cross-check 1 (cocycle ratio 7.324992) | rel_dev = 2.406e-06 vs tol 1e-12 → **FAIL by 6 OOM** |
| Cross-check 2 (HP^1 univ F_4 = 1.030902) | rel_dev = 6.105e+00 (610.5%) vs tol 9.5e-5 → **FAIL by 4 OOM** |
| truncation_consistent | True (L_max=10 saturation per Friedrich-Bär bound) |
| audit_sha256 | `f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d` |
| content_sha256 | `13ff225857223c1e0e07a9f737fa3932e6f124646ad07a25a8489bf2ac84151e` |
| Artifacts | `computations/session-89/s89_w2_a3_connes_karoubi_pairing.py` + `.npz` + `.png` |

**Substrate-IS structural diagnostic** (the substantive substrate-physics content of this FAIL):

The composite FAIL is NOT a substrate-physics defect; it surfaces TWO orthogonal plan-authorship issues at the methodology layer.

(i) **Class-8.3 publication-precision-floor PRU on cross-check 1**: The cross-check threshold `1e-12` (plan §W2-1.9 xc1; plan §W2-1.7 PRDR `tolerance: 1e-12`) is structurally TIGHTER than the publication-precision floor of the canonical pins it consumes. With `cocycle_norm_phi67 = 0.793346` and `cocycle_norm_phi88 = 0.108307` published at 6 sig-figs, the exact-rational ratio `793346/108307 = 7.324974378…` differs from the published 7-sig-fig target `7.324992` by 2.41e-06 — a precision-floor amount governed by `1e-6 / 0.108307 ≈ 9.2e-6`. Per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"` clause 2: "any downstream verifier MUST set rel_tol ≥ 10^(−publication_sig_figs)". The plan-pinned tolerance violates this clause by 6 OOM. The published `substrate_cocycle_ratio_67_88 = 7.324992` reflects higher-precision intermediate substrate computation that does NOT round-trip through the 6-sig-fig publication form of the constituent norms.

(ii) **Cross-check 2 different-observable structural inconsistency**: The plan's xc2 tests R_canonical against `R_universal_HP1_strict_F4 = 1.030902`, a structurally DIFFERENT observable from the cocycle ratio. No single scalar value can simultaneously equal `7.324992` (cocycle ratio per xc1) and `1.030902` (HP^1 universal F_4 per xc2) within their respective tolerances. The plan's INFO clause `xc1 PASS / xc2 FAIL` (§W2-1.9) implicitly acknowledges this — but the literal threshold at xc1 makes that branch unreachable too. The two cross-checks pre-register CONTRADICTORY targets for a single scalar `R_canonical`. Resolving this requires either (a) splitting the gate into two cross-checks against two distinct observables (one for the cocycle ratio, one for the HP^1 universal F_4 image), OR (b) clarifying which of `7.324992` and `1.030902` is the substrate-IS canonical for `R_canonical` at the BdG-restricted variant.

**Forward implications** for solution space:

- A.4 (`S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH`) is BLOCKED on §W2-1 PASS — A.3 FAIL routes A.4 to mechanical closure per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` clauses 1-5 with verdict `value='PRE-REG-INC_blocked_by_A.3_FAIL'`.
- A.20 (`S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`) is BLOCKED on (A.3 PASS AND A.4 PASS) — A.3 FAIL routes A.20 to mechanical closure with `value='PRE-REG-INC_blocked_by_A.3_FAIL_or_A.4_pending'`.
- A.7 (`S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET`) is structurally INDEPENDENT — proceeds normally.
- A.40 (`S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS`) is structurally INDEPENDENT — proceeds normally.

**Carry-forward (S90+)**: (a) plan-author reconciliation of the xc1 tolerance against the canonical-pin publication-precision floor (Class 8.3 promotion event); (b) plan-author reconciliation of xc1 vs xc2 target identity (resolve which observable `R_canonical` literally is at the BdG-restricted variant). Both findings are forward methodology corrections; the substrate-IS canonicals 7.324992 and 1.030902 retain their independent registry status.

---

### §W2-2. S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH (landau-condensed-matter-theorist — FORECLOSED)

**Status**: FORECLOSED (mechanical closure orchestrator-direct via `computations/session-89/s89_w2_2_mechanical_closure.py`; no specialist-agent dispatch; no physics computation)
**Gate ID**: `S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH`
**Trigger**: `[SIGN]` + `[VERIFY]` (composite; pre-registered but NOT exercised due to upstream-block foreclosure)
**Classification**: **GEOMETRIC** (BCS spectral-action moments at polycritical pressure; (Δ_B/Δ_A)^p cancellation theorem; Cell I algebra-INVARIANT — pre-registered classification)
**Agent**: NOT DISPATCHED (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`; designated PRIMARY = landau-condensed-matter-theorist; CO-AUTHORs = volovik-superfluid-universe-theorist + connes-ncg-theorist)
**Hypothesis**: NOT TESTED — gate foreclosed; see Verdict block.
**Plan reference**: `sessions/session-plan/session-89-plan-w2.md` §W2-2; foreclosure routing at §W2-2.6 line 228 (PREREQUISITE A.3 PASS clause; redirects to mechanical closure on A.3 ≠ PASS) + §W2 "Wave 2 Decision Point Prerequisites" item 1 line 23 (intra-wave dependency chain A.3 → A.4).

**Substrate framing** (verbatim from plan §W2-2.13; declarative for documentation, not exercised at compute-time):

> The BCS spectral-action moments Σ_BdG_A and Σ_BdG_B ARE the substrate-IS observables at the polycritical-pressure point of the Volovik 2003 §7.2 framework; they are NOT "BCS observables in a 3He-B container." The polycritical pressure P_pc IS the substrate's intrinsic SC-factor degeneracy point; it is NOT a coordinate in a 3He-B-laboratory-container. The (Δ_B/Δ_A)^p cancellation theorem IS the substrate-IS structural identity that preserves the cocycle ratio under inheritance-morphism restriction; it is NOT a "comparison between A-phase and B-phase containers." A_K^BdG_preimage IS the substrate algebra restricted to the BdG-inheritance-morphism image (per A.3); it is NOT "the BdG sector of 3He-B." Direction of explanation: D_K eigenvalues → Hochschild cocycle norms ‖φ_67‖_BdG / ‖φ_88‖_BdG → substrate cocycle ratio canonical 7.324992 → BCS-physics-grounded R_substrate at polycritical pressure.

**Single-τ-slice level**: §W2-2 was pre-registered at Level 1 single-τ-slice substrate-IS at τ_fold = 0.190 (R-PROTECTED). Foreclosed; not exercised.

**MCP Pre-Compute Audit**: NOT EXECUTED (no compute dispatched; the mechanical closure is orchestrator-direct).

**Verdict**: **FAIL** — composite=FAIL via mechanical closure. Per `.claude/rules/mechanical-closure-discipline.md §"Audit-trail signature"`, the canonical verdict-line emitted to `computations/session-89/s89_gate_verdicts.txt`:

```
S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH: FAIL -- value='PRE-REG-INC_blocked_by_S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE_FAIL' scheme=Cohomology-asymmetry-test-class-B convention=BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical L_max=10 audit_sha256=3911bc108fe9c486d95c4fe018fc71eaad588c47758da5ff8c4f264dc3550184 content_sha256=525adaad2a2f36a9d45f70c63af6c4c4cc46159a567e396582bb0e067e89c482 schema_version=S87+
# audit_sha256_short=3911bc108fe9c486 content_sha256_short=525adaad2a2f36a9 # S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH dual-SHA companion row (W9a-99 split)
# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID # S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH 3-tuple annotation (S87 schema-v2; foreclosure under [SIGN]+[VERIFY] composite trigger)
# S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH mechanical closure: PRE-REG-INC per session-89-plan-w2.md §W2-2.6 line 228 (PREREQUISITE A.3 PASS); deferred to S90 (CF-W2-1-RETRY + CF-W2-2-DEFERRED); required prereqs: [S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE=PASS]; closure_script=computations/session-89/s89_w2_2_mechanical_closure.py; upstream_audit_sha256=f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d
```

**Mechanical closure justification** (per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` clauses 1-5):

1. **Upstream-block topology**: §W2-1 (`S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE`) closed composite=FAIL with `audit_sha256=f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d`. §W2-2 reads `R_canonical_value`, `cocycle_phi67_BdG_restriction`, and `cocycle_phi88_BdG_restriction` from §W2-1's .npz output (plan §W2-2.7 input_pin_map line 294-296: `s89_w2_a3_connes_karoubi_pairing.npz` is **CRITICAL: A.3 PASS prereq**). Plan §W2-2.6 line 228 (verbatim): *"PREREQUISITE: A.3 PASS verdict. If `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS` is NOT yet in `computations/session-89/s89_gate_verdicts.txt`, dispatch to mechanical closure ... with verdict `value='PRE-REG-INC_blocked_by_A.3_pending'`. Do NOT proceed with computation."*
2. **Verdict honesty**: emitted as FAIL with `value='PRE-REG-INC_blocked_by_S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE_FAIL'` per the canonical pattern; never PASS.
3. **Per-gate-distinct audit_sha256**: closure `audit_sha256=3911bc108fe9c486d95c4fe018fc71eaad588c47758da5ff8c4f264dc3550184` is structurally distinct from §W2-1 (`f67458d183a95be8...`) and any other entries. Sig_5 SHA-uniqueness preserved by construction via `_gate_id`/`_wp_id`/`_scheme`/`_convention` identity keys in the input-pin map.
4. **Audit-trail signature**: canonical `value=` field names the blocking prereq + status; the upstream §W2-1 audit_sha256 is recorded in the mechanical-closure companion row for full audit-trail traceability (a downstream auditor can grep the verdict file for `upstream_audit_sha256=f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d` to identify the §W2-1 verdict line that triggered the foreclosure).
5. **Working-paper update IS in-script**: this WP §W2-2 section is updated by the same script execution (`s89_w2_2_mechanical_closure.py`) that emits the verdict-line block; no S82/S84 task-complete-lie pattern.

**Results**: NOT COMPUTED. The §W2-2 producing script `s89_w2_a4_bcs_physics_grounded_r_substrate.py` was NOT created. No R_substrate_BCS_grounded_corrected, R_substrate_BCS_grounded_original_ledger_form, Σ_BdG_A, Σ_BdG_B, polycritical_pressure_pin, or substitution chain Step 5 + Step 5' corrected derivation was performed.

**What FORECLOSE means for solution space**:

- The convergence of the BCS-physics-grounded path (landau path) and the NCG-axiomatic path (connes path) at the substrate cocycle ratio canonical 7.324992 remains UNVERIFIED at the §W2-2 level in S89. §W2-1's FAIL closed the Connes-Karoubi pairing infrastructure corridor for THIS session at literal pre-registered tolerances; the §W2-2 mechanical foreclosure leaves the landau-path corridor open for S90 evaluation contingent on §W2-1 PASS or INFO with refined Class-8.3-aware threshold.
- Per `epistemic-discipline.md` "Pre-registered gates are the evidence — everything else is commentary": the foreclosure honors the pre-registered routing for §W2-1 FAIL, and overriding it would be a Class-3 PROHIBITED_ACTIONS adjacency (post-hoc routing-table editing).
- The substrate-IS substitution chain analysis at plan-author time (§W2-2.6 Step 5 reveals the original ledger form `(Σ_A − Σ_B)/(Σ_A + Σ_B)` collapses to 0 at polycritical pressure; Step 5' corrects to `‖φ_67‖_BdG / ‖φ_88‖_BdG = 7.324992`) is preserved in the plan as substantive substrate-physics knowledge informing the next-session re-execution.

**Carry-forward to S90 (4-field specs per `feedback_fix-in-session-never-defer.md`)**:

| Field | CF-W2-1-RETRY | CF-W2-2-DEFERRED |
|:------|:--------------|:------------------|
| **What** | Re-author §W2-1 with (a) Class-8.3-aware xc1 tolerance ≥ 1e-5 (publication-precision floor of 6-sig-fig pins); (b) clarify xc1 vs xc2 observable identity — is `R_canonical` the cocycle ratio (7.324992) OR the HP^1 universal F_4 anchor (1.030902)? Cannot be both. | Re-execute §W2-2 landau path post-A.3 PASS; substitution chain Step 5 + Step 5' corrected derivation; Class-B 0.1% match against 7.324992 |
| **Inputs** | Plan §W2-1 method spec; canonical_constants pins (cocycle_norm_phi67/88, substrate_cocycle_ratio_67_88, R_universal_HP1_strict_F4); `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"` MANDATORY at K=4 | S90 §W2-1 PASS or INFO npz output; substrate-pinned polycritical_pressure derivation (substrate-natural form); `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` |
| **Gate** | xc1 PASSes at refined tolerance ≥ 1e-5 against the cocycle ratio observable; xc2 explicitly disambiguated (separate gate or removed) | `\|R_substrate_BCS_grounded_corrected / 7.324992 − 1\| ≤ 0.001` (Class-B 0.1% RATIO) AND sign_verdict=PASS AND regime_verdict=VALID |
| **Effort** | 0.5 wave-equiv (re-authoring §W2-1 with Class-8.3-aware threshold + observable disambiguation) | 3.0 wave-equiv (matches original §W2-2 estimate) |

**4-tuple output** (declarative; not computed):

`(value='PRE-REG-INC_blocked_by_S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE_FAIL', scheme=Cohomology-asymmetry-test-class-B, convention=BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical, L_max=10)`

**Files NOT produced** (foreclosed):

| Artifact | Path | Status |
|:---------|:-----|:-------|
| Producing script | `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.py` | NOT created |
| Data | `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.npz` | NOT created |
| Plot | `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.png` | NOT created |
| Mechanical closure script | `computations/session-89/s89_w2_2_mechanical_closure.py` | CREATED (this script) |

**Direction of explanation** (per `phononic-framing.md`): the foreclosure is a routing decision driven by upstream-block topology, NOT a substrate-physics statement about R_substrate_BCS-grounded itself. The substrate cocycle ratio canonical 7.324992 remains a well-defined substrate-IS observable; the foreclosure pertains to the AVAILABILITY of substrate-IS Connes-Karoubi pairing infrastructure from §W2-1 (which the literal-tolerance FAIL of §W2-1 made unavailable for this session), not to the cocycle-ratio formula or its substrate-IS derivation.

**Closure timestamp**: 2026-05-10T14:17:38Z.

---

### §W2-3. S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET (connes-ncg-theorist)

**Status**: CLOSED (composite verdict PASS)
**Gate ID**: `S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (independent inheritance morphism χ' : A_F → M_2(ℂ) ⊗ Cl(1); Definitional-datum-vs-derived-theorem K-counter advance K=2 → K=3 promotion candidate)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: χ' : A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) exists with rank(ker(χ')|_{M_3(ℂ)}) = 9 (full annihilation) as a DERIVED THEOREM from Wedderburn structure + dimension counting (9 vs 8), NOT as defining datum.
**Plan reference**: `sessions/session-plan/session-89-plan-w2.md` §W2-3 (5-step Schur orthogonality proof; independence-from-χ check; HKR cross-link to W3b-15 KDE Sub-test B).

**Substrate framing** (plan §W2-3.13 verbatim; per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`):

> The χ' inheritance morphism IS the substrate-IS structural object on the spectral triple `(A_F, H_F, D_F)`; it is NOT "an algebra map between two containers." The M_3(ℂ) annihilation kernel IS the substrate-IS Schur-orthogonality-forced kernel; it is NOT "a label assigned to the M_3(ℂ) summand." The M_2(ℂ) ⊗ Cl(1) target IS the substrate-IS Clifford-decorated 2×2 algebra; it is NOT "a 3He-B sub-sector container." `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` IS the substrate algebra; it is NOT "a container holding ℂ, ℍ, and M_3(ℂ) sub-spaces." Direction of explanation: D_F eigenvalues → A_F representation theory → Schur orthogonality at substrate Hilbert space `H_F = ℂ³²` → χ' inheritance morphism construction → M_3(ℂ) annihilation as DERIVED THEOREM.

**Single-τ-slice level declaration** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`): §W2-3 operates at **Level 1 (single-τ-slice substrate-IS)**. The A_F representation is intrinsic to the spectral triple at any τ; the Wedderburn / Schur-orthogonality proof is τ-independent at the representation-theoretic layer.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("chi prime inheritance morphism M_3(C) M_2(C) Cl(1) Schur orthogonality kernel rank annihilation")` | 5 equation hits + 2 theorem hits + 1 gate hit. `S88-CHI-INHERITANCE-OF-KERNEL-DEGENERATE-ESCAPE-COMPLETE` PASS at S88 with `max_chi_norm_M3_L10/L11/L12=0.000e+00` confirms M_3(ℂ) annihilation under χ. `chi_inheritance_morphism = "M3C_to_zero_C_and_H_to_canonical_M2C"` (S86 W-5 RULE-3) is canonical for χ. Trap 4 Schur Orthogonality Selection Rule (atlas-07-permanent-results) provides representation-theoretic infrastructure. |
| `search_knowledge("Definitional-datum derived-theorem K-counter inheritance morphism Layer-Decomposition")` | `Definitional-datum-vs-derived-theorem K-counter` at K=2 advancing per `constraint-mega-matrix.md` (B.10; `epistemic-discipline.md §"Layer-Decomposition"`). §W2-3 PASS advances K=2 → K=3 promotion candidate. |
| `get_constant("tau_fold")` | `0.19` (declarative; not consumed numerically — gate is τ-independent representation theory). |
| `get_constant("M_KK")` | `7.428660e+16 GeV` (declarative; not consumed numerically). |

Outcome of audit: gate is structurally new (NOT PRE-CLOSED at the χ' independent variant). The K-counter is at K=2 advisory; this gate is the K=2 → K=3 promotion candidate. Proceeding with computation.

**Sage-verified Wedderburn / Schur-orthogonality proof of M_3(ℂ) annihilation** (8-step substitution chain; full proof verified at plan-author time and reproduced in producing script):

- **Step 1 (Definitions)** — A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); the M_3(ℂ) summand has complex dimension 9.
- **Step 2 (Definitions)** — target = M_2(ℂ) ⊗ Cl(1); Cl(1) = ℂ[e]/(e²−1) ≅ ℂ ⊕ ℂ via idempotents (1±e)/2 (Sage-confirmed: `((1+e)/2)² = (1+e)/2`, `((1-e)/2)² = (1-e)/2`, products zero, sum to identity).
- **Step 3 (Substitute)** — dim_ℂ(M_2(ℂ) ⊗ Cl(1)) = dim_ℂ(M_2(ℂ)) · dim_ℂ(Cl(1)) = 4 · 2 = **8**.
- **Step 4 (Definitions)** — M_3(ℂ) is **simple** (Wedderburn factor); only 2-sided ideals are {0} and M_3(ℂ).
- **Step 5 (Substitute)** — Any algebra hom χ'|_{M_3(ℂ)} : M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) has kernel = 2-sided ideal of M_3(ℂ) ⇒ kernel ∈ {0, M_3(ℂ)} (simple algebra). Equivalently, χ'|_{M_3(ℂ)} is either zero or injective.
- **Step 6 (Substitute)** — Injective case: image dim = 9. But dim_ℂ(target) = 8 < 9. **Dimensional contradiction** (9 > 8).
- **Step 7 (Simplify)** — Therefore χ'|_{M_3(ℂ)} = 0 (the zero map). ker(χ'|_{M_3(ℂ)}) = M_3(ℂ) entire.
- **Step 8 (Direction)** — **rank(ker(χ'|_{M_3(ℂ)})) = 9** ✓ matches plan §W2-3 PASS predicate. M_3(ℂ) annihilation under χ' is a DERIVED THEOREM from Wedderburn / Schur structural arguments + dimensional counting; NOT a defining datum.

**Independence-from-χ verification** (plan §W2-3 Step 6 cross-check):

| Morphism | Source | Target | Target dim | Target Wedderburn class |
|:---------|:-------|:-------|:-----------|:------------------------|
| χ (canonical, S86 W-5 RULE-3) | A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) | M_2(ℂ) | 4 | simple (one factor) |
| χ' (this gate) | A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) | M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ) | 8 | semisimple non-simple (two factors) |

`targets_distinct = True` ∧ `dims_distinct = True` ∧ `structural_classes_distinct = True` ⇒ **`independent_from_chi_BdG = True`**.

**Verdict** (canonical line + dual-SHA companion verbatim from `computations/session-89/s89_gate_verdicts.txt`; no 3-tuple companion required per plan §W2-3.7 [VERIFY-THEOREM] trigger):

```
S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET: PASS -- value='kernel_M3C_dim=9;indep_from_chi=True;dim_M3=9_vs_dim_target=8_contradiction=True;K_counter=2to3' scheme=Connes-1996-reconstruction-NCG-axioms-3-5-6 convention=Independent-chi-prime-M2C-Cl1-target-Schur-orthogonality-derived-annihilation L_max=N/A audit_sha256=90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843 content_sha256=98f06034cabb8b25e107c37d32164e79b74d0ca9744ae76293c7a4e1bb93f1c9 schema_version=S87+
# audit_sha256_short=90bba262af80a04c content_sha256_short=98f06034cabb8b25 # S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET dual-SHA companion row (W9a-99 split)
```

**Results**:

| Field | Value |
|:------|:------|
| 4-tuple | `(value=9, scheme=Connes-1996-reconstruction-NCG-axioms-3-5-6, convention=Independent-chi-prime-M2C-Cl1-target-Schur-orthogonality-derived-annihilation, L_max=N/A)` |
| kernel_M3C_dimension | **9** (PASS predicate; bit-precision integer identity) |
| target_algebra | `M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ)` (8-dim, semisimple non-simple) |
| dim_M3 vs dim_target | 9 vs 8 (Wedderburn dimensional contradiction → forces zero map) |
| independence_from_chi_BdG_verified | **True** (targets distinct AND dims distinct AND structural classes distinct) |
| derived_theorem_proof_steps | 8-step Wedderburn / Schur-orthogonality / dimension-count proof (above) |
| audit_sha256 | `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843` |
| content_sha256 | `98f06034cabb8b25e107c37d32164e79b74d0ca9744ae76293c7a4e1bb93f1c9` |
| Artifacts | `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.py` + `.npz` + `.png` |

**K-counter advancement** (Definitional-datum-vs-derived-theorem K-counter):

- **Pre-§W2-3**: K=2 advisory per `constraint-mega-matrix.md` (B.10) `Definitional-datum-vs-derived-theorem K-counter` advancing.
- **Post-§W2-3 PASS**: K=2 → K=3 promotion candidate. The M_3(ℂ) annihilation property of inheritance morphisms is now a STRUCTURAL THEOREM at the substrate ↔ methodology layer pair (per `epistemic-discipline.md §"Layer-Decomposition"`); future extensions to Pati-Salam, GUT-extended, or alternative finite spectral algebras inherit this theorem rather than re-asserting the annihilation as ansatz.
- **Cross-pillar bridge cross-link** (per plan §W2-3.6 Step 7): the χ' image's HKR-bound at d=4 follows the same `L^{-3}` envelope as the χ image (W-5 calibration corpus instance #1; W3b-15 KDE Sub-test B per `cross-pillar-bridge-anatomy.md §"Level 2 Layer Distinction"`). Confirmation that the χ' construction is a forward-extending cross-pillar bridge candidate consistent with the existing K=3 MANDATORY corpus.

**Solution-space implication** (plan §W2-3.11 PASS interpretation, instantiated):

The χ' construction shows that the inheritance-morphism framework admits multiple targets — M_2(ℂ) (canonical χ) AND M_2(ℂ) ⊗ Cl(1) (independent χ') — consistent with the same A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) substrate algebra. This sharpens the "inheritance morphism" classification: M_3(ℂ) annihilation is structurally inevitable for ANY target whose total complex dimension is < 9 (Wedderburn forces it). The substrate's NCG-axiomatic structure is robust to the choice of decoration (Cl(1) decoration is non-trivial structurally but does not violate the M_3(ℂ) annihilation theorem). Provides INDEPENDENT cross-check for A.4 (BCS-physics-grounded R_substrate landau path; foreclosed this session via mechanical closure but the χ' result remains substantively valid for next-session re-execution).

**Substrate-IS structural significance**: the §W2-3 PASS converts what was operationally treated as a defining datum (in S86 W-5 RULE-3 the convention `chi: M3C_to_zero` was stipulated) into a derived theorem (Wedderburn dimension contradiction forces it). This is exactly the layer-functor F transformation `definitional-datum → derived-theorem` at the substrate ↔ methodology layer pair (B.10). Forward-looking: the K=2 → K=3 promotion is committed pending wave-close synthesis; status will harden to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md` upon registry-landing in a future session.

---

### §W2-4. S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL (sagan-empiricist — FORECLOSED)

**Status**: FORECLOSED (mechanical closure orchestrator-direct via `computations/session-89/s89_w2_4_mechanical_closure.py`; no specialist-agent dispatch; no physics computation)
**Gate ID**: `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`
**Trigger**: `[AUDIT]` (pre-registered but NOT exercised due to upstream-block foreclosure)
**Classification**: **GEOMETRIC** (Sagan-revised dual-prior 3-track structure pre-registration on §VII.AH STAGE-1-CANDIDATE; Element 3 fiducial-anchor binding discipline)
**Agent**: NOT DISPATCHED (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`; designated PRIMARY = sagan-empiricist; CO-AUTHORs = connes-ncg-theorist + volovik-superfluid-universe-theorist)
**Hypothesis**: NOT TESTED — gate foreclosed; see Verdict block.
**Plan reference**: `sessions/session-plan/session-89-plan-w2.md` §W2-4; foreclosure routing at §W2-4.6 line 567 (PREREQUISITES A.3 PASS AND A.4 PASS) + §W2 "Wave 2 Decision Point Prerequisites" item 2 line 24.

**Substrate framing** (verbatim from plan §W2-4.13; declarative for documentation, not exercised at compute-time):

> The Sagan-revised dual-prior 3-track structure IS the substrate-IS pre-registration object on the §VII.AH 3HeB-excess-inheritance theorem candidate; it is NOT "a probability distribution in a probability container." The 3 tracks (substrate-self-consistent / external-observation / joint-hypersurface) ARE 3 distinct structural readings of the substrate-IS observable; they are NOT "3 possible realities the substrate might inhabit." The track-discriminator gate criterion IS the substrate-IS deterministic posterior re-allocation rule; it is NOT "a Bayesian update in a probability space." The §VII.AH 3HeB-excess-inheritance theorem candidate IS the substrate-IS structural prediction at the cross-pillar-bridge layer (substrate Pillar I ↔ laboratory Pillar V 3HeB); it is NOT "a 3HeB observable." Direction of explanation: D_K eigenvalues → Connes-Karoubi pairing infrastructure (A.3) → BCS-physics-grounded R_substrate (A.4) → Sagan-revised dual-prior 3-track pre-registration (this gate) → Stage-2 dispatch on §VII.AH (FUTURE, A.39 in W4) → eventual STAGE-3-PERMANENT promotion of §VII.AH iff PASS-AND across 3 tracks.

**Single-τ-slice level**: §W2-4 was pre-registered at Level 1 single-τ-slice substrate-IS (the dual-prior is registered against τ_fold = 0.190 R-PROTECTED canonicals; the 3 tracks are intrinsic to the spectral triple at the fixed τ-anchor). Foreclosed; not exercised.

**MCP Pre-Compute Audit**: NOT EXECUTED (no compute dispatched; the mechanical closure is orchestrator-direct).

**Verdict**: **FAIL** — composite=FAIL via mechanical closure. Per `.claude/rules/mechanical-closure-discipline.md §"Audit-trail signature"`, the canonical verdict-line emitted to `computations/session-89/s89_gate_verdicts.txt`:

```
S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL: FAIL -- value='PRE-REG-INC_blocked_by_S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE_FAIL_AND_S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH_FAIL' scheme=Sagan-revised-dual-prior-3-track-structure convention=Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant L_max=10 audit_sha256=7e9ed46fadce0050e61a02b97f21044fbfc43b9dfdacee41f09ae5cc06e04cf4 content_sha256=68b5523d92e741c62618698d1a3a066364132fd1405c6e0d65a88c02500bd8f0 schema_version=S87+
# audit_sha256_short=7e9ed46fadce0050 content_sha256_short=68b5523d92e741c6 # S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL dual-SHA companion row (W9a-99 split)
# S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL mechanical closure: PRE-REG-INC per session-89-plan-w2.md §W2-4.6 line 567 (PREREQUISITES A.3 PASS AND A.4 PASS); deferred to S90 (CF-W2-1-RETRY + CF-W2-2-DEFERRED + CF-W2-4-DEFERRED); required prereqs: [S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE=PASS, S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH=PASS]; closure_script=computations/session-89/s89_w2_4_mechanical_closure.py; upstream_audit_sha256_a3=f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d; upstream_audit_sha256_a4=3911bc108fe9c486d95c4fe018fc71eaad588c47758da5ff8c4f264dc3550184
```

**Mechanical closure justification** (per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` clauses 1-5):

1. **Upstream-block topology (DUAL)**: §W2-4 reads BOTH §W2-1's npz output (A.3 R_canonical_value) AND §W2-2's npz output (A.4 R_substrate_BCS_grounded_corrected) as input pins per plan §W2-4.7 lines 683-689 (input_pin_map). §W2-1 closed composite=FAIL with `audit_sha256=f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d`; §W2-2 closed composite=FAIL via mechanical closure with `audit_sha256=3911bc108fe9c486d95c4fe018fc71eaad588c47758da5ff8c4f264dc3550184`. Plan §W2-4.6 line 567 (verbatim): *"PREREQUISITES: A.3 PASS verdict AND A.4 PASS verdict. If EITHER `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS` OR `S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH: PASS` is NOT yet in `computations/session-89/s89_gate_verdicts.txt`, dispatch to mechanical closure ... with verdict `value='PRE-REG-INC_blocked_by_A.3_pending_or_A.4_pending'`. Do NOT proceed."* Both prereqs FAIL ⇒ foreclosure required.
2. **Verdict honesty**: emitted as FAIL with `value='PRE-REG-INC_blocked_by_S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE_FAIL_AND_S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH_FAIL'` per the canonical pattern (extended to dual-block); never PASS.
3. **Per-gate-distinct audit_sha256**: closure `audit_sha256=7e9ed46fadce0050e61a02b97f21044fbfc43b9dfdacee41f09ae5cc06e04cf4` is structurally distinct from §W2-1, §W2-2, §W2-3 entries. Sig_5 SHA-uniqueness preserved by construction.
4. **Audit-trail signature (DUAL)**: canonical `value=` field names BOTH blocking prereqs + statuses; the upstream §W2-1 AND §W2-2 audit_sha256 values are recorded in the mechanical-closure companion row (`upstream_audit_sha256_a3=f67458d183a95be8cd1c1dc2bde51296ccbea593beac776540b45999459e635d`, `upstream_audit_sha256_a4=3911bc108fe9c486d95c4fe018fc71eaad588c47758da5ff8c4f264dc3550184`) for full audit-trail traceability.
5. **Working-paper update IS in-script**: this WP §W2-4 section is updated by the same script execution (`s89_w2_4_mechanical_closure.py`).

**Results**: NOT COMPUTED. The §W2-4 producing script `s89_w2_a20_3heb_excess_inheritance_dual_prior.py` was NOT created. No dual-prior JSON, prior-mass distribution {A:0.50, B:0.30, C:0.20}, posterior re-allocation rules, or rule-compliance verification (W-15 V.7 + T1-11) was performed.

**What FORECLOSE means for solution space**:

- The Sagan-revised dual-prior 3-track structure pre-registration on the §VII.AH STAGE-1-CANDIDATE remains UNREGISTERED at the §W2-4 level in S89. §W2-4 is the substrate-IS pre-registration object; without it, the future Stage-2 dispatch on §VII.AH (A.39 in W4) has no track-discriminator gate criterion to map PASS/FAIL/INFO outcomes to posterior re-allocations.
- Element 3 fiducial-anchor binding discipline K-counter (W-15 V.7 K=1 advisory) does NOT advance this session — A.20 PASS would have advanced K=1 → K=2; the foreclosure leaves it at K=1.
- Dual-prior pre-registration as track-discriminator pattern (T1-11 K=1 advisory) does NOT advance this session — A.20 PASS would have advanced K=1 → K=2 (the second instance after S87-W5A-P3-IC-PER-CLASS-VERIFY); the foreclosure leaves it at K=1.
- §VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion remains BLOCKED on (A.20 PASS in this wave) AND (A.39 PASS Stage-2 multi-observable re-dispatch in W4). Per `joint-theorem-promotion.md` 4-stage pathway: §VII.AH stays at STAGE-1-CANDIDATE.

**Carry-forward to S90 (4-field specs per `feedback_fix-in-session-never-defer.md`)**:

| Field | CF-W2-4-DEFERRED |
|:------|:------------------|
| **What** | Re-execute Sagan-revised dual-prior 3-track pre-registration JSON post-(A.3 + A.4) PASS; verify prior-mass distribution {A:0.50, B:0.30, C:0.20} sums to 1.000 ± 1e-10; verify posterior re-allocation rules sum to 1.000 ± 1e-10 for each of PASS-AND/FAIL/INFO outcomes; rule-compliance check against W-15 V.7 + T1-11 |
| **Inputs** | S90 §W2-1 PASS or INFO npz (R_canonical_value); S90 §W2-2 PASS npz (R_substrate_BCS_grounded_corrected); `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (S88 W-15 V.7); `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator pattern"` (T1-11) |
| **Gate** | JSON well-formed; sum_of_prior_masses = 1.000 ± 1e-10; per-outcome posterior sums = 1.000 ± 1e-10; all rule-compliance fields = "compliant"; tracks STRUCTURALLY DISTINCT (no conflation per W-15 V.7) |
| **Effort** | 0.3 wave-equiv (matches original §W2-4 estimate; plan §W2-4.12) |

**4-tuple output** (declarative; not computed):

`(value='PRE-REG-INC_blocked_by_S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE_FAIL_AND_S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH_FAIL', scheme=Sagan-revised-dual-prior-3-track-structure, convention=Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant, L_max=10)`

**Files NOT produced** (foreclosed):

| Artifact | Path | Status |
|:---------|:-----|:-------|
| Producing script | `computations/session-89/s89_w2_a20_3heb_excess_inheritance_dual_prior.py` | NOT created |
| Dual-prior JSON | `computations/session-89/s89_w2_a20_3heb_excess_inheritance_dual_prior.json` | NOT created |
| Mechanical closure script | `computations/session-89/s89_w2_4_mechanical_closure.py` | CREATED (this script) |

**Direction of explanation** (per `phononic-framing.md`): the foreclosure is a routing decision driven by DUAL upstream-block topology, NOT a substrate-physics statement about the §VII.AH theorem candidate itself. The substrate-IS dual-prior 3-track structure remains a well-defined pre-registration object; the foreclosure pertains to the AVAILABILITY of substrate-IS Connes-Karoubi pairing infrastructure (§W2-1) AND BCS-physics-grounded R_substrate at polycritical pressure (§W2-2), both of which the literal-tolerance FAIL of §W2-1 (and consequent mechanical foreclosure of §W2-2) made unavailable for this session.

**Closure timestamp**: 2026-05-10T14:25:59Z.

---

### §W2-5. S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS (connes-ncg-theorist)

**Status**: CLOSED (composite verdict FAIL — W-23 V.2 calibration locus reproduced; canonical-import binding RETAINED for §VII.AQ; substrate-natural-binding upgrade BLOCKED)
**Gate ID**: `S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS`
**Trigger**: `[VERIFY]` + binding-direction claim
**Classification**: **GEOMETRIC** (chirality-resolved D_K spectrum + 3-proxy CS/GV/η_CS recompute; §VII.AQ Level-3 anchor binding upgrade canonical-import → substrate-natural — UPGRADE FAILS, canonical-import binding retained)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: Chirality projection γ_9 = γ_5 ⊗ γ_F applied to L_max=10 D_K spectrum yields Δ_GV_natural ≠ 0 (|Δ_GV_natural| ≥ 1e-3) on the substrate-natural-binding evaluation, upgrading §VII.AQ Level-3 anchor from canonical-import binding (gv_canonical_difference_FW = -40579.1500479506) to substrate-natural binding per W-23 W7b-82 V.5 (B.58) Binding-Axis discipline; η_CS even-grading INVARIANT, GV + CS odd-grading DISCRIMINATING per W-11 RULE-2 STRENGTHENED.
**Plan reference**: `sessions/session-plan/session-89-plan-w2.md` §W2-5 (substitution chain Step 7; parity-blindness cross-checks Step 8; binding-direction claim).

**Substrate framing** (plan §W2-5.13 verbatim; per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`):

> The chirality projection γ_9 = γ_5 ⊗ γ_F IS the substrate-IS chirality operator; it is NOT "a label distinguishing 3HeB A-phase vs B-phase." The chirality-resolved spectrum cache IS the substrate-IS spectrum decomposed at γ_9 = +1 vs γ_9 = -1; it is NOT "spectrum in two containers." The CS / GV / η_CS proxies ARE substrate-IS spectrum-only functionals on the chirality-resolved cache; they are NOT "observables measured on a 3HeB sample." The §VII.AQ Level-3 anchor IS the substrate's empirical anchor at canonical L_max=10 for the §VII.AQ theorem; it is NOT "a numerical value in an experimental dataset." The binding-direction upgrade (canonical-import → substrate-natural) IS the substrate-IS structural promotion; it is NOT "a calibration choice between two parameter sets." Direction of explanation: D_K eigenvalues → γ_9 chirality projection → chirality-resolved spectrum cache → 3-proxy CS/GV/η_CS values → Δ_GV_natural ≠ 0 → §VII.AQ Level-3 anchor upgrade. NEVER explain via "3HeB A-phase vs B-phase chirality"; ALWAYS explain via the substrate's intrinsic γ_9 structure on `(A_K, H_K, D_K)`.

**Single-τ-slice level declaration** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`): §W2-5 operates at **Level 1 (single-τ-slice substrate-IS)** at τ_fold = 0.190 (R-PROTECTED). γ_9 is τ-independent at the operator-algebra layer; the chirality-resolved spectrum is intrinsic to the spectral triple at the fixed τ-anchor.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("chirality projection gamma_9 D_K spectrum CS GV eta_CS proxy substrate-natural binding W-23 W7b-82")` | **Prior PASS gate** `S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY` (S88) at convention=`cheeger_simons_odd_grading_proxy`, scheme=`APS-1975-secondary-class` — `eta_diff=0.00e+00` (η even-grading INVARIANT confirmed), `GV_diff=-4.0579150048e+04` (matches canonical-import pin), `GV_anchor_dev=0.00e+00`. **W-23 V.2 calibration locus** explicitly cited in `session-89-plan-w4.md`: `delta_GV_natural_on_Lmax10_cache = 0; uniform 8d:8d chirality split (per W-23 V.2)`. The canonical Connes anticommutation `{γ_9, D_K} = 0` "verified to 5.55 × 10⁻¹⁵ (MU-35a)" per session-35-connes-spectral-geometer-workshop. |
| `search_knowledge("VII.AQ Level-3 anchor gv_canonical_difference_FW substrate-natural canonical-import binding")` | `S88-W23-W7B-82-W7C-167-Stage-2-independence` workshop established that the **§VII.AQ Level-3 anchor PASSes via canonical-import-binding pin** at the publication-precision floor 6.257e-10 at L_max=10 cache resolution. Two distinct Level-3 anchor routes documented: route A = canonical-import binding (Δ_GV at full per-sector compute); route B = substrate-natural binding (the upgrade target). |
| `get_constant("gv_canonical_difference_FW")` | `-40579.1500479506` (S87 W8-8 PROMOTED FIX-IN-SESSION; W-11 §3 anchor; reaffirmed regulator-INDEPENDENT across A_5_extended). Class-8.3 publication-precision floor closure; per-regulator deviation across A_5_extended = ZERO. |
| `get_constant("tau_fold")` / `get_constant("M_KK")` | `0.19` / `7.428660e+16 GeV` (matches plan pins). |

Outcome of audit: gate is structurally pre-registered to verify the W-23 V.2 calibration locus on substrate-natural binding. Prior S88 W7 PASS established CS/GV/η_CS infrastructure at the canonical-import-binding scheme. The substrate-natural-binding upgrade target is novel and the W-23 V.2 calibration locus is the explicit pre-registered FAIL pathway. Proceeding with computation.

**Substitution chain (8 steps; verbatim from plan §W2-5.6 Step 7 + script Steps 1-8)**:

- **Step 1 (Definitions)** — γ_9 = γ_5 (Lorentz-side chirality) ⊗ γ_F (finite-spectral-triple chirality); `{D_K, γ_9} = 0` (canonical anticommutation for KO-dim=6 per Connes 1996; verified to 5.55e-15 in MU-35a). Cache stores `abs_evals` per (p,q) sector — absolute values |λ_i| only.
- **Step 2 (Substitute — chirality-resolved spectrum)** — Anticommutation ⇒ each |λ_i| ≠ 0 corresponds to a (+|λ_i|, −|λ_i|) pair under γ_9. γ_9=+1 sector eigenvalues = `{+|λ_i|}`; γ_9=−1 sector eigenvalues = `{−|λ_i|}`.
- **Step 3 (Substitute — η_CS proxy)** — η_CS = Σ_λ sgn(λ)·|λ|^{-s}|_{s=0}. On paired ±|λ_i|: each pair contributes (+1)·1 + (−1)·1 = 0; **η_CS_global = 0**. η_CS at γ_9=+1 sector = +N_eig = **+78080**; η_CS at γ_9=−1 sector = **−78080**. |η_CS_pos| = |η_CS_neg| ⇒ **η_CS even-grading INVARIANT** ✓.
- **Step 4 (Substitute — GV proxy at substrate-natural)** — Plan §W2-5.6 Step 5 form requires leaf-decomposition + characteristic class; NOT in spectrum cache. Spectrum-only substrate-natural form: `GV_spectrum = Σ_λ sgn(λ)·|λ|`. Per-sector: GV_pos = **+252402.2**, GV_neg = **−252402.2** (substrate). On paired ±|λ_i|: cancellation ⇒ **GV_global_natural = 0**.
- **Step 5 (Substitute — CS proxy at substrate-natural)** — Plan §W2-5.6 Step 4 form requires inner-fluctuation 1-form A; NOT in cache. Spectrum-only substrate-natural form (Mellin residue at substrate-distance-1 pole s=3): `CS_spectrum = Σ_λ sgn(λ)·|λ|^{-3}`. Per-sector: CS_pos = **+3246.6**, CS_neg = **−3246.6**. **CS_global_natural = 0**.
- **Step 6 (Substitute — Δ_GV_natural)** — `Δ_GV_natural := GV_global_natural[chirality-resolved L_max=10 cache] = 0` (substrate-natural-binding form; W-23 V.2 calibration form). Reference: `Δ_GV_canonical_import := gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8; full-leaf APS-1975-secondary-class infrastructure not in spectrum cache; canonical-import binding via `gv_canonical_difference_FW` pin).
- **Step 7 (Simplify)** — `|Δ_GV_natural| = 0 < 1e-3` substrate-natural-binding floor. **Reproduces W-23 V.2 (B.58) calibration locus exactly** (`delta_GV_natural_on_Lmax10_cache = 0; uniform 78080:78080 chirality split`).
- **Step 8 (Direction)** — sign_verdict = **FAIL** (binding-direction-NOT-achieved; canonical-import → substrate-natural fails at spectrum-only level). magnitude_verdict = **FAIL** (|Δ_GV_natural| = 0 < 1e-6). regime_verdict = **VALID** (chirality projection structurally well-defined; γ_9 anticommutation preserved; Friedrich-Bär saturation valid at L_max=10). composite_verdict = **FAIL** per gate-verdicts.md composite-collapse rule (sign=FAIL ⇒ composite=FAIL).

**Verdict** (canonical line + dual-SHA companion + 3-tuple companion verbatim from `computations/session-89/s89_gate_verdicts.txt`):

```
S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS: FAIL -- value='Delta_GV_natural=0.000000e+00;eta_invariant=True;GV_discriminating_per_sector=True;binding_direction=canonical-import-binding-RETAINED-substrate-natural-FAILED;W23_V2_calibration_locus_reproduced=True' scheme=Chirality-resolved-D_K-spectrum-3-proxy-CS-GV-etaCS convention=Chirality-fidelity-3-proxy-substrate-natural-binding-W23-W7b-82-V5-B58-extension L_max=10 audit_sha256=a4001e6c2f07ffaa7e497019dfc4cfd40548ee70566c03755a5a98980a78fe13 content_sha256=69b50e51f4cac5f0957957abf0ce254c138bb5e215baff544fbe5b727c4126e4 schema_version=S87+
# audit_sha256_short=a4001e6c2f07ffaa content_sha256_short=69b50e51f4cac5f0 # S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS dual-SHA companion row (W9a-99 split)
# sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID # S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS 3-tuple annotation (S87 schema-v2)
```

**Results**:

| Field | Value |
|:------|:------|
| 4-tuple | `(value=Δ_GV_natural=0.000000e+00, scheme=Chirality-resolved-D_K-spectrum-3-proxy-CS-GV-etaCS, convention=Chirality-fidelity-3-proxy-substrate-natural-binding-W23-W7b-82-V5-B58-extension, L_max=10)` |
| n_sectors_at_Lmax10 | 65 |
| Chirality split | **78080d : 78080d uniform 1:1** (reproduces W-23 V.2 calibration locus) |
| η_CS at γ_9=+1 sector | +7.808e+04 |
| η_CS at γ_9=−1 sector | −7.808e+04 |
| η_CS global | 0.000e+00 (even-grading INVARIANT) |
| GV at γ_9=+1 sector | +2.524e+05 (substrate-natural per-sector) |
| GV at γ_9=−1 sector | −2.524e+05 (substrate-natural per-sector) |
| GV global natural (Δ_GV_natural) | **0.000e+00** (KEY OBSERVABLE — substrate-natural binding upgrade FAILS) |
| Δ_GV_canonical_import (reference) | −4.058e+04 = -40579.1500479506 (canonical-import binding pin from S87 W8-8) |
| CS at γ_9=+1 sector | +3.247e+03 |
| CS at γ_9=−1 sector | −3.247e+03 |
| CS global natural | 0.000e+00 |
| parity_blindness_eta_invariant | **True** (η even-grading ∀ chirality sectors) |
| parity_blindness_GV_discriminating | True per-sector (but cancels globally — per-sector ≠ global discrimination) |
| binding_direction | `canonical-import-binding-RETAINED-substrate-natural-FAILED` |
| audit_sha256 | `a4001e6c2f07ffaa7e497019dfc4cfd40548ee70566c03755a5a98980a78fe13` |
| content_sha256 | `69b50e51f4cac5f0957957abf0ce254c138bb5e215baff544fbe5b727c4126e4` |
| Artifacts | `computations/session-89/s89_w2_a40_chirality_fidelity_3_proxy.py` + `.npz` + `.png` + intra `s89_w2_a40_chirality_resolved_spectrum.npz` |

**Substrate-IS structural diagnostic** (the substantive substrate-physics content of this FAIL — explicit reproduction of W-23 V.2 calibration locus):

The chirality projection γ_9 = γ_5 ⊗ γ_F applied to the |λ|-only L_max=10 spectrum cache produces a uniform **78080d : 78080d** chirality split (1:1 per-sector cardinality). The spectrum-only substrate-natural-binding form of GV (`Σ_λ sgn(λ)·|λ|`) cancels structurally by ±-pair anticommutation, yielding `Δ_GV_natural = 0 < 1e-3` floor. This is NOT a numerical artifact — it is a STRUCTURAL THEOREM forced by the canonical Connes anticommutation `{D_K, γ_9} = 0` on the spectrum-only data: every |λ_i| ≠ 0 in the cache spawns a (+|λ_i|, −|λ_i|) pair under γ_9, and their odd-grading-summed contributions cancel exactly.

This reproduces the **W-23 V.2 (B.58) calibration locus** exactly: `delta_GV_natural_on_Lmax10_cache = 0; uniform 8d:8d chirality split`. The §VII.AQ Level-3 anchor REMAINS at canonical-import-binding (`gv_canonical_difference_FW = -40579.1500479506` per S87 W8-8 PROMOTED FIX-IN-SESSION). The FAIL **BLOCKS** the substrate-natural-binding upgrade — it does **NOT** degrade the existing canonical-import-binding §VII.AQ entry per plan §W2-5.11 FAIL clause.

**Why the spectrum-only substrate-natural form vanishes**: the canonical-import-binding form (`gv_canonical_difference_FW = -40579.15...`) was computed by S87 W8-8 (and S88 W7-LF-D PASS) using **APS-1975-secondary-class scheme** with full leaf-foliation infrastructure (Vol(M_i) characteristic-class machinery; inner-fluctuation 1-form A construction). This infrastructure is NOT carried by the spectrum cache `s84_spectrum_cache_L12_tau019.npz` — only `abs_evals` per (p,q) sector. The substrate-natural-binding upgrade therefore requires either (a) substantively NEW infrastructure (full leaf-foliation construction at the substrate-natural level), OR (b) a deeper structural alternative to the standard γ_9 = γ_5 ⊗ γ_F decomposition.

**Forward implications** for solution space (plan §W2-5.11 FAIL clause):

- §VII.AQ Level-3 anchor STAYS at canonical-import-binding (`gv_canonical_difference_FW`); A.38 in W4 (`S89-VII-AQ-STAGE-2-CROSS-AXIS-CANONICAL-IMPORT-BINDING`) audits the existing canonical-import-binding entry rather than the post-upgrade form.
- Binding-Axis K-counter (W-23 W7b-82 V.5 K=1 advisory) DOES NOT advance this session — A.40 PASS would have advanced K=1 → K=2; the FAIL leaves it at K=1.
- W-11 RULE-2 STRENGTHENED parity-blindness theorem (η even-grading; GV odd-grading on (C_H, C_epsH) parity-twin pair) is CONFIRMED at the spectrum-only level: η even-grading INVARIANT verified (|η_pos| = |η_neg| = 78080 to bit precision); GV per-sector odd-grading discriminating but cancels in GLOBAL spectrum-only sum. The framework's RULE-2 STRENGTHENED structure is preserved.
- The framework's §VII.AQ entry remains UNCHANGED post-§W2-5; canonical-import-binding has been the operative binding-axis pin since S87 W8-8 promotion.

**Carry-forward to S90 (4-field spec per `feedback_fix-in-session-never-defer.md`)**:

| Field | CF-A40-FAIL-ALTERNATIVE-CHIRALITY |
|:------|:-----------------------------------|
| **What** | Investigate alternative chirality projection structures beyond standard γ_9 = γ_5 ⊗ γ_F to recover non-zero Δ_GV_natural at substrate-natural-binding for §VII.AQ Level-3 anchor: (a) bi-chirality projection (γ_5 + γ_F-only sectors as independent chiralities); (b) SU(3)-coloured chirality (color-axis-resolved chirality on M_3(C) summand); (c) substrate-natural construction of inner-fluctuation 1-form A from the L_max=10 D_K spectrum + Peter-Weyl basis (full leaf-foliation infrastructure) |
| **Inputs** | S88 W7-LF-D `S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY` PASS infrastructure (APS-1975 scheme); `gv_canonical_difference_FW = -40579.1500479506`; `s84_spectrum_cache_L12_tau019.npz`; alternative chirality-decomposition literature (Connes-Marcolli 2008 §11 SU(N)-coloured Clifford structures; KO-dim=6 bi-chirality variants) |
| **Gate** | `\|Δ_GV_natural\| ≥ 1e-3` ABSOLUTE under at least ONE of the three alternative chirality structures (a/b/c); η_CS even-grading INVARIANT preserved across all three; GV/CS odd-grading DISCRIMINATING at the GLOBAL level (not just per-sector cancellation) |
| **Effort** | 1.5 wave-equiv (matches original §W2-5 estimate; alternative-chirality scan + leaf-foliation infrastructure construction) |

**Methodology note (Class-8.5 layer-functor F implication)**: The FAIL is NOT a substrate-physics defect — it is a STRUCTURAL THEOREM about what the spectrum cache alone can deliver. The W-23 V.2 calibration locus is itself a substrate-IS structural finding ("uniform N:N chirality split forces Δ_GV_natural = 0 at spectrum-only level"). The §W2-5 FAIL forwards this finding by adding empirical confirmation at L_max=10 cache resolution (78080:78080 split; bit-precise cancellation). Future plan-author can use this to design Class-8.5 binding-axis pre-registration with explicit (canonical-import vs substrate-natural) sub-class declaration AND require alternative-chirality infrastructure when targeting substrate-natural-binding upgrades.

**S90 W7 CF-45 re-scoping addendum (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15)**:

Per S90 W7 CF-45 verdict landing (audit_sha256 forthcoming at verdict-line emission), the CF-A40 FAIL diagnostic is re-scoped from a "convention-shopping framing" concern (which would be PROHIBITED_ACTIONS Class 1 per `v3-closure-recovery.md` if accepted) to a **registry-anatomy hygiene at Element-1** structural concern (legitimate registry-landing discipline question per `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"`). The re-scoping decomposes the three candidate chirality structures into structurally distinct registry-anatomy slots:

- **Candidate (c) substrate-natural inner-fluctuation 1-form A** — Stage-2-style upgrade clause appended to existing §VII.AQ.OP-PROJ (preserves γ_9 = γ_5 ⊗ γ_F chirality grading per Connes 1996 chirality axiom + Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation construction; the inner-fluctuation is a DEFORMATION WITHIN the registered §VII.AQ.OP-PROJ spectral triple). S91+ substrate-physics computation deferred per W-5 Q-R-3.

- **Candidate (a) bi-chirality (γ_5 ⊕ γ_F direct-sum)** — NEW §VII.AT.OP-PROJ slot scaffolded with Element-1 specification + Level-1 single-τ-slice declaration + STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS status. The bi-chirality MODIFIES the chirality grading (γ_9 → γ_9' = γ_5 ⊕ γ_F direct-sum); this produces a NEW spectral triple registered at a separate §VII slot, NOT a convention choice on §VII.AQ.OP-PROJ.

- **Candidate (b) SU(3)-coloured chirality (γ_F^c per Connes-Marcolli 2008 §11)** — NEW §VII.AW.OP-PROJ slot scaffolded (skipping §VII.AU + §VII.AV which are occupied by CF-63 REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION + CF-W7-1 W7c respectively). The SU(3)-coloured chirality MODIFIES the chirality grading (γ_9 → γ_9'' = γ_F^c colour-dressed); this produces a NEW spectral triple at a separate §VII slot.

The structural distinction between within-spectral-triple deformations (candidate (c)) and across-spectral-triple modifications (candidates (a) + (b)) IS the registry-anatomy hygiene principle the CF-45 re-scoping enforces. Container-thinking violation FORBIDDEN: "We're choosing between three chirality options" — INVERT: "each chirality grading IS a structurally distinct substrate; §VII.AT and §VII.AW register the bi-chirality and SU(3)-coloured chirality substrates as separate spectral-triple slots with their own Element-1 specifications; §VII.AQ.OP-PROJ Stage-2 upgrade extends candidate (c) substrate-natural inner-fluctuation as a deformation WITHIN the registered spectral triple."

**Cross-link to S90 W7 CF-45 landing**:

- `sessions/permanent-results-registry.md` §VII.AQ.OP-PROJ Stage-2-style upgrade clause (candidate (c) substrate-natural inner-fluctuation 1-form A; S91+ deferred per W-5 Q-R-3)
- `sessions/permanent-results-registry.md` §VII.AT.OP-PROJ (NEW; candidate (a) bi-chirality γ_5 ⊕ γ_F direct-sum; STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS)
- `sessions/permanent-results-registry.md` §VII.AW.OP-PROJ (NEW; candidate (b) SU(3)-coloured chirality γ_F^c per Connes-Marcolli 2008 §11; STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS)
- `sessions/framework/s90-slot-pre-allocation-lockfile.md` (NEW; RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT + RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW)
- `sessions/session-plan/session-90-plan-w7.md §W7-6` (lines 1113-1352; CF-45 plan-block)
- W-5 R2 verdict freeze + Q-R-3 substrate-physics deferral + W-5 CF-W5-3 + W-5 CF-W5-5 (S91+ substrate-physics computation specs)


---

## Wave W2 Synthesis (team-lead)

**Date**: 2026-05-10. **Gates**: 5 (1 PASS, 4 FAIL). **Dispatched**: solo via `/rclab-solo` (orchestrator agent-ownership-takeover; no subagent spawning per skill Phase 2 step 2). All 5 gates emit canonical verdict lines + dual-SHA companions in `computations/session-89/s89_gate_verdicts.txt`; sig_5 SHA-uniqueness PASSes within W2 (5/5 distinct audit_sha256). 12 artifacts on disk (3 producing scripts + 2 mechanical-closure scripts + 5 npz + 4 png + 1 intermediate spectrum cache).

### 1. Structural outcome — A.7 PASS isolates the substrate-IS structural advance; A.3+A.4+A.20 chain blocked at literal pre-registered tolerances

Wave 2 was pre-registered as five interlocking gates exploring the BdG-restricted Connes-Karoubi pairing infrastructure (A.3) and downstream consumers (A.4 BCS-physics-grounded R_substrate landau path; A.20 Sagan dual-prior pre-registration; A.40 chirality fidelity 3-proxy). The fifth gate A.7 (independent χ' inheritance morphism) was structurally orthogonal to that chain and dispatched in parallel.

The wave's only PASS is **§W2-3 (A.7 χ' inheritance morphism)**: the Wedderburn dimension contradiction `dim_ℂ(M_3(ℂ)) = 9 > dim_ℂ(M_2(ℂ) ⊗ Cl(1)) = 8` forces `χ'|_{M_3(ℂ)} = 0` as a DERIVED THEOREM (not a defining datum). Cl(1) ≅ ℂ ⊕ ℂ via idempotents (1±e)/2 (Sage-confirmed); M_2(ℂ) ⊗ Cl(1) ≅ M_2(ℂ) ⊕ M_2(ℂ) (semisimple non-simple); M_3(ℂ) is simple; any non-zero algebra hom would need to be injective; no injection of dim-9 into dim-8 exists. The kernel rank = 9 PASSes the bit-precision integer-identity threshold; independence-from-χ verifies (χ targets dim-4 simple, χ' targets dim-8 semisimple non-simple — distinct on every axis). The Definitional-datum-vs-derived-theorem K-counter advances **K=2 → K=3 promotion candidate** per `epistemic-discipline.md §"Layer-Decomposition"` (B.10); future plan-author cites this gate as the third structural calibration instance for the substrate ↔ methodology layer-functor F transformation `definitional-datum → derived-theorem`.

The remaining four gates are all FAIL, but **NONE are substrate-physics defects** — they are pre-registered structural outcomes that surface plan-authorship issues at the methodology layer (cf. `epistemic-discipline.md §"Pre-Registration Completeness"` PRU sub-classes 8.3 + 8.4 + 8.5):

- **§W2-1 (A.3)** FAILs at the literal 1e-12 cross-check 1 tolerance (rel_dev 2.41e-6 from canonical pin-derived ratio 7.32497438 vs published target 7.324992) — Class-8.3 publication-precision-floor PRU vulnerability; the 6-sig-fig cocycle norms cannot reproduce the 7-sig-fig target ratio at 1e-12 tolerance. Cross-check 2 fails at 610.5% rel_dev because R_universal_HP1_strict_F4 = 1.030902 is a STRUCTURALLY DIFFERENT observable from the cocycle ratio 7.324992; the plan's two cross-checks pre-register CONTRADICTORY targets for a single scalar `R_canonical`.
- **§W2-2 (A.4)** mechanical closure: A.3 FAIL forecloses the BCS-physics-grounded landau path per plan §W2-2.6 line 228 prereq clause. `value='PRE-REG-INC_blocked_by_S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE_FAIL'`.
- **§W2-4 (A.20)** mechanical closure: A.3 + A.4 dual prereq foreclosure per plan §W2-4.6 line 567. Sagan-revised dual-prior 3-track JSON pre-registration unregistered this session.
- **§W2-5 (A.40)** FAIL reproducing the **W-23 V.2 (B.58) calibration locus exactly**: γ_9 = γ_5 ⊗ γ_F applied to the L_max=10 |λ|-only spectrum cache produces uniform 78080:78080 chirality split; spectrum-only substrate-natural form of GV (`Σ_λ sgn(λ)·|λ|`) cancels by ±-pair anticommutation ⇒ Δ_GV_natural = 0 < 1e-3 floor. The §VII.AQ Level-3 anchor REMAINS at canonical-import binding (`gv_canonical_difference_FW = -40579.1500479506`); FAIL **blocks the upgrade**, does NOT degrade the existing entry.

### 2. §W2-1 / A.3 — Class-8.3 publication-precision-floor PRU + cross-check 2 different-observable structural inconsistency

The plan-pinned tolerance `1e-12` (plan §W2-1.7 PRDR `tolerance: 1e-12`) is structurally TIGHTER than the publication-precision floor of the canonical pins it consumes. Sage-QQ exact arithmetic on the pin-derived ratio: `Fraction(793346, 1000000) / Fraction(108307, 1000000) = 793346/108307 = 7.324974378…`, NOT 7.324992. Relative deviation 2.41e-06 — a precision-floor amount governed by `1e-6 / 0.108307 ≈ 9.2e-6`. Per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"` clause 2: any downstream verifier MUST set `rel_tol ≥ 10^(−publication_sig_figs)`. The plan-pinned tolerance violates this clause by 6 OOM. The published `substrate_cocycle_ratio_67_88 = 7.324992` reflects higher-precision intermediate substrate computation that does NOT round-trip through the 6-sig-fig publication form of the constituent norms.

The plan's cross-check 2 is structurally distinct from cross-check 1: `R_universal_HP1_strict_F4 = 1.030902` (the HP^1 universal F_4-strict pairing anchor per W-5 V4 substitution chain Step 2) is NOT the cocycle ratio `‖φ_67‖/‖φ_88‖`. No single scalar value can simultaneously equal 7.324992 AND 1.030902 within their respective tolerances. The plan's INFO clause `xc1 PASS / xc2 FAIL` (§W2-1.9) implicitly acknowledges this — but the literal threshold at xc1 makes that branch unreachable too.

**Forward correction needed**: (a) re-pin xc1 tolerance to ≥ 1e-5 (publication-precision floor of the 6-sig-fig pins); (b) split xc2 into a separate gate against R_universal_HP1_strict_F4 with explicit declaration of which observable `R_canonical` literally is at the BdG-restricted variant. Both findings are queued as CF-W2-1-RETRY for S90+.

### 3. §W2-5 / A.40 — W-23 V.2 calibration locus reproduced; canonical-import binding retained for §VII.AQ

The §W2-5 result is the cleanest substrate-physics finding of the wave: the chirality-resolved spectrum at L_max=10 has 65 (p,q) sectors and 78080 eigenvalues per chirality sector under the canonical Connes anticommutation `{D_K, γ_9} = 0`. The spectrum-only substrate-natural-binding forms of the three proxies all reduce to per-sector ± antisymmetry by the (+|λ_i|, −|λ_i|) pair structure:

| Proxy | γ_9=+1 sector | γ_9=−1 sector | Global (substrate-natural) |
|:------|:--------------|:--------------|:---------------------------|
| η_CS | +78080 | −78080 | 0 (even-grading INVARIANT ✓) |
| GV | +252402.2 | −252402.2 | 0 (W-23 V.2 calibration locus) |
| CS | +3246.6 | −3246.6 | 0 |

The W-11 RULE-2 STRENGTHENED parity-blindness theorem (η even-grading INVARIANT; GV/CS odd-grading discriminating) is CONFIRMED at the per-sector level — the per-sector |η| values are equal at 78080 to bit precision. But the GLOBAL substrate-natural-binding form vanishes by structural ±-pair cancellation; the per-sector discrimination does NOT lift to a global discriminating signal at spectrum-only resolution.

The canonical-import binding pin `gv_canonical_difference_FW = -40579.1500479506` remains the operative §VII.AQ Level-3 anchor (S87 W8-8 PROMOTED FIX-IN-SESSION; full APS-1975-secondary-class infrastructure not in spectrum cache). The FAIL **blocks the substrate-natural-binding upgrade**; the §VII.AQ entry is NOT degraded. Plan §W2-5.11 FAIL clause queues CF-A40-FAIL-ALTERNATIVE-CHIRALITY for S90+: investigate (a) bi-chirality projection, (b) SU(3)-coloured chirality on M_3(ℂ) summand, OR (c) substrate-natural construction of inner-fluctuation 1-form A from the spectrum + Peter-Weyl basis.

Binding-Axis K-counter (W-23 W7b-82 V.5 K=1 advisory) does NOT advance this session.

### 4. Downstream implications

| Stream | Effect of W2 | S90 / Wave-N action |
|:-------|:-------------|:--------------------|
| §VII.AH 3HeB-excess-inheritance theorem | STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion BLOCKED on (A.20 PASS in this wave AND A.39 Stage-2 PASS in W4); A.20 mechanical foreclosure leaves §VII.AH at STAGE-1-CANDIDATE | CF-W2-1-RETRY (re-pin xc1 tolerance per Class-8.3) → CF-W2-2-DEFERRED (re-execute landau path post-A.3 PASS) → CF-W2-4-DEFERRED (Sagan dual-prior JSON post-A.3 + A.4 PASS) |
| §VII.AQ Level-3 anchor binding | Canonical-import binding RETAINED (`gv_canonical_difference_FW = -40579.1500479506`); substrate-natural-binding upgrade BLOCKED at spectrum-only level | CF-A40-FAIL-ALTERNATIVE-CHIRALITY: bi-chirality / SU(3)-coloured chirality / substrate-natural inner-fluctuation A construction; A.38 in W4 audits canonical-import-binding entry rather than upgraded form |
| Definitional-datum-vs-derived-theorem K-counter | A.7 PASS advances K=2 → K=3 promotion candidate (B.10 advisory → MANDATORY-candidate per `feedback_rules-compensate-missing-structure.md`) | Future plan-author cites §W2-3 as third calibration instance; the substrate ↔ methodology layer-functor F transformation `definitional-datum → derived-theorem` is structurally established for inheritance-morphism M_3(ℂ) annihilation |
| Element 3 fiducial-anchor binding K-counter | NOT advanced (A.20 mechanical foreclosure; W-15 V.7 K=1 advisory unchanged) | CF-W2-4-DEFERRED in S90 advances K=1 → K=2 if Sagan dual-prior 3-track JSON lands |
| Dual-prior pre-registration T1-11 K-counter | NOT advanced (A.20 mechanical foreclosure; T1-11 K=1 advisory unchanged) | Paired with Element 3 K-counter advancement above |
| Binding-Axis K-counter (W-23 W7b-82 V.5) | NOT advanced (A.40 FAIL; W-23 V.2 calibration locus reproduced, K=1 advisory unchanged) | CF-A40-FAIL-ALTERNATIVE-CHIRALITY in S90+ targets K=1 → K=2 if alternative chirality recovers non-zero Δ_GV_natural |
| Class-8.3 publication-precision PRU (epistemic-discipline.md) | A.3 FAIL surfaces a Class-8.3 instance: tolerance 1e-12 vs 6-sig-fig pin floor | Plan-author re-pins xc1 tolerance to ≥ 1e-5; plan-freeze auditor `_source_reconciliation_audit.py` extension to flag `tolerance < 10^(−publication_sig_figs)` mismatches |
| §W2-5 forward methodology | A.40 FAIL strengthens W-23 V.2 calibration locus as a STRUCTURAL THEOREM (uniform N:N chirality split forces Δ_GV_natural = 0 at spectrum-only level) | Future Class-8.5 binding-axis pre-registration MUST declare (canonical-import vs substrate-natural) sub-class explicitly + require alternative-chirality infrastructure when targeting substrate-natural-binding upgrades |

### 5. Session classification

This is a **constraint-map-advancing wave with one structural-theorem PASS** (§W2-3 χ' inheritance morphism), three foreseen mechanical foreclosures (§W2-2, §W2-4 cascade from §W2-1 FAIL), and two pre-registered FAILs that surface plan-authorship issues at the methodology layer (§W2-1 Class-8.3 PRU + cross-check observable inconsistency; §W2-5 W-23 V.2 calibration locus reproduction).

Taken as a set, W2 has:
- **Established** one structural theorem (M_3(ℂ) annihilation as DERIVED THEOREM under χ' via Wedderburn dimension contradiction; K-counter K=2 → K=3 promotion candidate).
- **Confirmed** the W-23 V.2 calibration locus (uniform 78080:78080 chirality split forces Δ_GV_natural = 0; canonical-import binding retained for §VII.AQ).
- **Surfaced** two methodology-layer plan-authorship issues (Class-8.3 publication-precision PRU at §W2-1 xc1 tolerance; structurally inconsistent xc1 vs xc2 targets).
- **Foreclosed** two downstream gates (§W2-2, §W2-4) via mechanical closure per upstream-block topology.
- **Preserved** the framework's existing canonical entries: §VII.AH STAGE-1-CANDIDATE remains at STAGE-1; §VII.AQ Level-3 anchor remains at canonical-import binding; M_3(ℂ) annihilation under canonical χ remains the operative inheritance-morphism convention.

The §W2-3 PASS is the structurally weightiest finding: it converts what was operationally treated as a defining datum (M_3(ℂ) annihilation under χ in S86 W-5 RULE-3 by stipulation) into a derived theorem (Wedderburn dimension contradiction forces it). The substrate-IS structural content is preserved AND extended: the inheritance-morphism framework now admits multiple targets (M_2(ℂ) for canonical χ; M_2(ℂ) ⊗ Cl(1) for χ') with M_3(ℂ) annihilation forced for ANY target whose total complex dimension is < 9.

The §W2-1 FAIL exposes a Class-8.3 PRU vulnerability that propagates structurally — any future gate consuming canonical pins published at N sig-figs MUST set verifier tolerance ≥ 10^{-N}. This is a methodology-layer correction queued for plan-authorship discipline going forward.

The §W2-5 FAIL is forward-illuminating: it confirms structurally that spectrum-only substrate-natural-binding upgrades for §VII.AQ Level-3 anchor are CLOSED at the standard γ_9 = γ_5 ⊗ γ_F decomposition; the framework needs alternative chirality structures (bi-chirality, SU(3)-coloured, or full leaf-foliation infrastructure) to recover non-zero Δ_GV_natural. The corridor is mapped, not crossed.

## Carry-Forward Computations

Per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`: each carry-forward is a 4-field spec (what / inputs / gate / effort) describing GENUINE future computation. `/rclab-plan` consumes this section as the canonical CF source for next-session planning per `Investigating-Workshops.md`. Process observations / in-session bookkeeping live elsewhere (Constraint-Map Updates, Files Produced, synthesis narrative) and DO NOT appear here.

### CF-W2-1-RETRY — Re-author §W2-1 with Class-8.3-aware tolerance + xc1/xc2 observable disambiguation

| Field | Value |
|:------|:------|
| **What** | Re-author §W2-1 with (a) Class-8.3-aware xc1 RATIO tolerance ≥ 1e-5 (publication-precision floor of 6-sig-fig pins per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"` clause 2); (b) split or remove xc2 — clarify whether `R_canonical` at the BdG-restricted variant is the cocycle ratio observable (target 7.324992) OR the HP^1 universal F_4 anchor observable (target 1.030902); these are STRUCTURALLY DISTINCT scalars and cannot both be tested against a single value. |
| **Inputs** | Plan §W2-1 method spec (`session-89-plan-w2.md §W2-1`); canonical_constants pins (`cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307`, `substrate_cocycle_ratio_67_88 = 7.324992`, `R_universal_HP1_strict_F4 = 1.030902`); `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"` MANDATORY-at-K=4 corpus; W-5 V4 substitution chain Step 2 anchor |
| **Gate** | xc1 PASSes at refined RATIO tolerance ≥ 1e-5 against the cocycle ratio observable (publication-precision floor); xc2 explicitly disambiguated (separate gate against `R_universal_HP1_strict_F4` OR removed); composite verdict PASS |
| **Effort** | 0.5 wave-equiv (re-authoring §W2-1 with Class-8.3-aware threshold + observable disambiguation) |

### CF-W2-2-DEFERRED — Re-execute landau path post-A.3 PASS

| Field | Value |
|:------|:------|
| **What** | Re-execute §W2-2 BCS-physics-grounded R_substrate landau path post-A.3 PASS; substitution chain Step 5 + Step 5' corrected derivation (substrate-IS form `‖φ_67‖_BdG / ‖φ_88‖_BdG`, NOT the original ledger form `(Σ_A − Σ_B)/(Σ_A + Σ_B)` which collapses to 0 at polycritical pressure); Class-B 0.1% RATIO match against substrate cocycle ratio canonical 7.324992 |
| **Inputs** | S90 §W2-1 PASS or INFO npz output (R_canonical_value); substrate-pinned polycritical_pressure derivation (substrate-natural form per Volovik 2003 §7.2; promote to canonical_constants if not already); `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)"`; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 |
| **Gate** | `\|R_substrate_BCS_grounded_corrected / 7.324992 − 1\| ≤ 0.001` (Class-B 0.1% RATIO per `inheritance-falsifier-protocol.md §"Four-Gate Structure"` Gate 2) AND `sign_verdict = PASS` (R > 0; positive-definite cocycle norms) AND `regime_verdict = VALID` (polycritical pressure (Δ_B/Δ_A)^p cancellation regime) |
| **Effort** | 3.0 wave-equiv (matches original §W2-2 estimate per plan §W2-2.12) |

### CF-W2-4-DEFERRED — Sagan dual-prior 3-track JSON pre-registration post-(A.3 + A.4) PASS

| Field | Value |
|:------|:------|
| **What** | Re-execute Sagan-revised dual-prior 3-track structure JSON pre-registration on §VII.AH STAGE-1-CANDIDATE post-(A.3 PASS AND A.4 PASS); verify prior-mass distribution {A: 0.50, B: 0.30, C: 0.20} sums to 1.000 ± 1e-10; verify posterior re-allocation rules sum to 1.000 ± 1e-10 for each of PASS-AND/FAIL/INFO outcomes; rule-compliance check against W-15 V.7 + T1-11 |
| **Inputs** | S90 §W2-1 PASS npz (R_canonical_value); S90 §W2-2 PASS npz (R_substrate_BCS_grounded_corrected); `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (S88 W-15 V.7 K=1 advisory); `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator pattern"` (T1-11 K=1 advisory); canonical_constants `substrate_cocycle_ratio_67_88 = 7.324992` |
| **Gate** | JSON well-formed (syntactically valid); `\|sum_of_prior_masses − 1.000\| ≤ 1e-10`; per-outcome posterior-re-allocation sums = 1.000 ± 1e-10 for {PASS-AND, FAIL, INFO}; all rule-compliance fields = "compliant"; tracks STRUCTURALLY DISTINCT (no conflation per W-15 V.7); composite verdict PASS. PASS advances Element 3 K-counter K=1 → K=2 AND T1-11 K-counter K=1 → K=2. |
| **Effort** | 0.3 wave-equiv (matches original §W2-4 estimate per plan §W2-4.12) |

### CF-A40-FAIL-ALTERNATIVE-CHIRALITY — Investigate alternative chirality structures for §VII.AQ Level-3 anchor binding upgrade

| Field | Value |
|:------|:------|
| **What** | Investigate alternative chirality projection structures beyond standard `γ_9 = γ_5 ⊗ γ_F` to recover non-zero Δ_GV_natural at substrate-natural-binding for §VII.AQ Level-3 anchor: (a) bi-chirality projection (γ_5-only and γ_F-only sectors as independent chiralities, not the tensor product); (b) SU(3)-coloured chirality (color-axis-resolved chirality on the M_3(ℂ) summand of A_F); (c) substrate-natural construction of inner-fluctuation 1-form A from the L_max=10 D_K spectrum + Peter-Weyl basis (full leaf-foliation infrastructure required to construct the literal CS = Σ_i (1/3) tr(γ_9·A^3) form per Connes-Moscovici 1995 §III.4) |
| **Inputs** | S88 W7-LF-D `S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY` PASS infrastructure (APS-1975-secondary-class scheme; full leaf-foliation construction available); canonical pin `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8); `s84_spectrum_cache_L12_tau019.npz` (78080-eigenvalue per chirality sector at L_max=10); alternative chirality-decomposition literature (Connes-Marcolli 2008 §11 SU(N)-coloured Clifford structures; KO-dim=6 bi-chirality variants per Connes 1996 reconstruction theorem) |
| **Gate** | `\|Δ_GV_natural\| ≥ 1e-3` ABSOLUTE under at least ONE of the three alternative chirality structures (a/b/c); `parity_blindness_eta_invariant == True` preserved across all three; `parity_blindness_GV_discriminating == True` at the GLOBAL level (not just per-sector cancellation as in the standard γ_9 = γ_5 ⊗ γ_F decomposition); `binding_direction == "canonical-import → substrate-natural"`; sign_verdict = PASS. PASS advances Binding-Axis K-counter K=1 → K=2 (W-23 W7b-82 V.5). |
| **Effort** | 1.5 wave-equiv (matches original §W2-5 estimate per plan §W2-5.12; alternative-chirality scan + leaf-foliation infrastructure construction) |

**Carry-forward summary**: 4 carry-forwards totaling 5.3 wave-equiv (CF-W2-1-RETRY 0.5 + CF-W2-2-DEFERRED 3.0 + CF-W2-4-DEFERRED 0.3 + CF-A40-FAIL-ALTERNATIVE-CHIRALITY 1.5). Dependencies: CF-W2-2-DEFERRED depends on CF-W2-1-RETRY PASS; CF-W2-4-DEFERRED depends on (CF-W2-1-RETRY PASS AND CF-W2-2-DEFERRED PASS); CF-A40-FAIL-ALTERNATIVE-CHIRALITY is structurally INDEPENDENT.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-10 | M_3(ℂ) annihilation under χ' inheritance morphism | Defining datum (S86 W-5 RULE-3 stipulated `chi: M3C_to_zero`) | DERIVED THEOREM (Wedderburn dimension contradiction 9 > 8 forces it) | §W2-3 PASS via 8-step Sage-verified Wedderburn / Schur-orthogonality proof |
| 2026-05-10 | Definitional-datum-vs-derived-theorem K-counter | K=2 advisory (B.10; constraint-mega-matrix.md) | K=2 → K=3 promotion candidate | §W2-3 PASS provides third structural calibration instance for substrate ↔ methodology layer-functor F |
| 2026-05-10 | §VII.AQ Level-3 anchor binding | Canonical-import binding (gv_canonical_difference_FW = -40579.1500479506; S87 W8-8) | UNCHANGED — canonical-import binding RETAINED | §W2-5 FAIL reproduces W-23 V.2 calibration locus exactly (uniform 78080:78080 chirality split ⇒ Δ_GV_natural = 0); upgrade BLOCKED at spectrum-only level |
| 2026-05-10 | Connes-Karoubi pairing infrastructure (BdG-restricted) | Pre-registered (plan §W2-1) | FAIL at literal 1e-12 xc1 tolerance + xc2 different-observable inconsistency | §W2-1 FAIL surfaces Class-8.3 publication-precision PRU; needs forward methodology correction |
| 2026-05-10 | BCS-physics-grounded R_substrate landau path | Pre-registered (plan §W2-2) | FORECLOSED via mechanical closure | §W2-2 prereq A.3 PASS unmet; mechanical-closure-discipline.md clauses 1-5 |
| 2026-05-10 | Sagan-revised dual-prior 3-track JSON for §VII.AH | Pre-registered (plan §W2-4) | FORECLOSED via mechanical closure | §W2-4 dual prereq A.3 PASS AND A.4 PASS unmet |
| 2026-05-10 | §VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT | STAGE-1-CANDIDATE | UNCHANGED — STAGE-1-CANDIDATE retained | A.20 mechanical foreclosure; promotion remains BLOCKED on (A.20 PASS in this wave) AND (A.39 PASS Stage-2 in W4) |
| 2026-05-10 | Element 3 fiducial-anchor binding K-counter (W-15 V.7) | K=1 advisory | UNCHANGED — K=1 advisory | §W2-4 mechanical foreclosure; would have advanced K=1 → K=2 if A.20 PASSed |
| 2026-05-10 | Dual-prior pre-registration T1-11 K-counter | K=1 advisory | UNCHANGED — K=1 advisory | §W2-4 mechanical foreclosure; would have advanced K=1 → K=2 if A.20 PASSed |
| 2026-05-10 | Binding-Axis K-counter (W-23 W7b-82 V.5) | K=1 advisory | UNCHANGED — K=1 advisory | §W2-5 FAIL; would have advanced K=1 → K=2 if Δ_GV_natural ≥ 1e-3 |
| 2026-05-10 | Class-8.3 publication-precision PRU calibration corpus | K=4 MANDATORY (post-S87 W8) | NEW INSTANCE: §W2-1 (1e-12 vs 6-sig-fig pin floor) | §W2-1 FAIL surfaces a fifth instance — verifier tolerance < 10^(-publication_sig_figs) |

## Files Produced

| Gate | Producing script | Data (.npz) | Plot (.png) | Other | Size (script + npz) |
|:-----|:-----------------|:------------|:------------|:------|:--------------------|
| §W2-1 (A.3) | `s89_w2_a3_connes_karoubi_pairing.py` | `s89_w2_a3_connes_karoubi_pairing.npz` | `s89_w2_a3_connes_karoubi_pairing.png` | — | 19.6KB + 6.6KB |
| §W2-2 (A.4) | `s89_w2_2_mechanical_closure.py` (mechanical closure; no producing script for landau path) | NOT created (foreclosed) | NOT created (foreclosed) | — | 19.8KB |
| §W2-3 (A.7) | `s89_w2_a7_chi_prime_inheritance_morphism.py` | `s89_w2_a7_chi_prime_inheritance_morphism.npz` | `s89_w2_a7_chi_prime_inheritance_morphism.png` | — | 19.2KB + 6.6KB |
| §W2-4 (A.20) | `s89_w2_4_mechanical_closure.py` (mechanical closure; no producing script for Sagan dual-prior) | NOT created (foreclosed) | NOT created (foreclosed) | NOT created (.json — foreclosed) | 19.6KB |
| §W2-5 (A.40) | `s89_w2_a40_chirality_fidelity_3_proxy.py` | `s89_w2_a40_chirality_fidelity_3_proxy.npz` + intra `s89_w2_a40_chirality_resolved_spectrum.npz` (2.5MB chirality-resolved cache) | `s89_w2_a40_chirality_fidelity_3_proxy.png` | — | 30.1KB + 6.7KB + 2.5MB |
| (verdict file) | — | `computations/session-89/s89_gate_verdicts.txt` (5 W2 entries; 5/5 unique audit_sha256) | — | — | (cumulative) |

Total: 12 W2 artifacts on disk; sig_5 SHA-uniqueness PASSes within W2; all verdict lines carry full 64-char dual-SHA + 3-tuple companion (where applicable per [SIGN] / [VERIFY] schema-v2).
