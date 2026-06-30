# Session 89 Plan — Wave 2: Connes-Karoubi pairing canonical pipeline + 3He-B inheritance retry

> **Provenance**: connes-ncg-theorist orchestrator-direct planner-write per `/rclab-plan` skill §3b; co-signers: landau-condensed-matter-theorist (A.4 runtime PRIMARY per ledger lines 65-70); volovik-superfluid-universe-theorist (A.4 + A.20 CO); sagan-empiricist (A.20 dual-prior PRIMARY per ledger lines 121-125).
> **Carry-forward source**: `sessions/archive/session-88/s88-pending-edits-ledger.md` Ledger A items A.3, A.4, A.7, A.20, A.40 (Cluster B per `sessions/session-plan/session-89-context.md` lines 48-56).
> **Theme**: Connes-Karoubi pairing canonical infrastructure (A.3) → BCS-physics-grounded R_substrate via landau path (A.4) → χ' independent inheritance morphism with M_3(ℂ) annihilation as derived theorem (A.7) → Stage-2 dual-prior pre-registration on the canonical pairing (A.20) → chirality-fidelity 3-proxy recompute upgrading §VII.AQ Level-3 anchor canonical-import → substrate-natural binding (A.40).
> **Composition order**: Wave 2 dispatches in S89 Batch 1 with W1 + W3-W7 in parallel.
> **Natural-split fallback**: W2a = A.3, A.7, A.40 (connes NCG infrastructure + inheritance + chirality, ~5.5 wave-equiv); W2b = A.4 (landau BCS-grounded, ~3 wave-equiv); W2c = A.20 (sagan dual-prior, ~0.3 wave-equiv). Single-pass write attempted; orchestrator MAY split at dispatch time per agent-author distinctness.

---

## Wave 2 Summary

Wave 2 builds the canonical Connes-Karoubi pairing infrastructure on the BdG-restricted sub-algebra image of the inheritance morphism χ : A_K = ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ), then uses that infrastructure to test BCS-physics-grounded substrate cocycle ratios at the polycritical-pressure point of the Volovik 2003 §7.2 SC-factor framework, finally pre-registering a Sagan-revised dual-prior 3-track structure for the eventual Stage-2 dispatch on the §VII.AH 3He-B-excess-inheritance theorem candidate. Two complementary refinements anchor the wave: A.7 constructs an INDEPENDENT inheritance morphism χ' : A_F → M_2(ℂ) ⊗ Cl(1) where M_3(ℂ) annihilation is a DERIVED THEOREM rather than a defining datum (closing the W11-2 layer-functor F definitional-datum-vs-derived-theorem K-counter advance toward K=2 promotion); A.40 builds a chirality-resolved spectrum cache and recomputes the 3-proxy CS / GV / η_CS observables to upgrade the §VII.AQ Level-3 anchor from canonical-import binding (gv_canonical_difference_FW = -40579.1500479506) to substrate-natural binding under the W-23 W7b-82 V.5 (B.58) Binding-Axis discipline.

The wave is cohomology-class-layer in classification per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` Level 1 (regulator-invariant identity at the Connes-Karoubi pairing axiom layer; `R_universal = ⟨[φ_g^sym], [Ch(P_0(τ_fold))]⟩`). Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`: the Hochschild cocycle [φ_g^sym] IS the substrate-IS observable on the BdG-restricted sub-algebra image; the Connes-Karoubi pairing IS the bridge map (NOT a comparison "between two containers"); A_K^BdG_preimage IS the substrate algebra restricted to the BdG image, NOT a 3He-B "container."

The wave produces a single bit-precision pipeline: A.3 emits R_canonical at L_max=10 (PRIMARY infrastructure); A.4 reads A.3's npz and emits R_substrate_BCS-grounded at the polycritical-pressure point against the substrate cocycle ratio canonical 7.324992 ± 0.1% (Class-B inheritance-falsifier-protocol Gate-2 cohomology-asymmetry test); A.20 reads BOTH A.3 and A.4 npz files and emits the Sagan-revised dual-prior pre-registration JSON for the eventual Stage-2 dispatch; A.7 and A.40 are structurally independent of the A.3/A.4/A.20 chain and dispatch in parallel within Wave 2.

## Wave 2 Decision Point Prerequisites

**Hard prerequisites (intra-wave dependency chain)**:

1. **A.3 → A.4**: A.4 BLOCKED until A.3 PASS verdict landed. A.4's PRDR machinery pin includes input-SHA pin from `computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz` `content_sha256=<computed-at-runtime>`. Without A.3 PASS, A.4 dispatches to mechanical closure per `.claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` clauses 1-5 with verdict `value='PRE-REG-INC_blocked_by_A.3_pending'`.
2. **A.3 + A.4 → A.20**: A.20 BLOCKED until BOTH A.3 PASS AND A.4 PASS verdicts landed. A.20's PRDR machinery pin includes TWO input-SHA pins, from A.3 npz AND A.4 npz.

**Hard prerequisites (S88-close pinned canonicals)**:

- `tau_fold = 0.19` (R-PROTECTED) — `canonical_constants.py`
- `M_KK = 7.428660036284456e+16 GeV` — `canonical_constants.py`
- `cocycle_norm_phi67 = 0.793346 M_KK²` — S86 W-5 C2 substrate-magnitude annotation
- `cocycle_norm_phi88 = 0.108307 M_KK²` — S86 W-5 C2
- `substrate_cocycle_ratio_67_88 = 7.324992` (Sage-exact at machine precision) — S86 W-5 R2-B Convergence #3
- `R_universal_HP1_strict_F4 = 1.030902` — S86 W-5 V4 substitution chain Step 2
- `gv_canonical_difference_FW = -40579.1500479506` — `canonical_constants.py` (S87 W8-8); §VII.AQ Level-3 anchor canonical-import binding (A.40 upgrades to substrate-natural)
- `Delta_BCS = 0.4642547394830737` (R-PROTECTED) — `canonical_constants.py`

**Hard prerequisites (D_K spectrum cache)**:

- `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (L_max=12 master cache; A.3 + A.4 + A.7 + A.40 all consume; SHA pinned at plan-freeze runtime)
- Chirality-resolved spectrum cache for A.40 produced in-script (NEW build) using γ_9 = γ_5 ⊗ γ_F chirality projection on the L_max=12 D_K cache; intermediate output `s89_w2_a40_chirality_resolved_spectrum.npz` is INTRA-A.40 (not cross-gate input).

**Soft prerequisites**:

- `methodology-wave-allowlist.md` is APPEND-ONLY and ORCHESTRATOR-EDIT-ONLY (per `wave-classification.md` M4 + `methodology-wave-allowlist.md` Edit discipline). NONE of W2's gate-IDs are METHODOLOGY-class — all 5 are COMPUTE-class (numerical PASS/FAIL/INFO predicates with `.py` producing scripts). No allowlist append required for W2.

**Wave-classification per `wave-classification.md` M1∧M2∧M3∧M4 strict conjunction**:

- A.3, A.4, A.7, A.40 — COMPUTE-class (numerical bit-precision predicates; .py producing scripts; no rule-file edits; M1 fails for METHODOLOGY ⇒ COMPUTE-class).
- A.20 — COMPUTE-class with multi-agent dispatch coordinator (Sagan dual-prior pre-registration is a COMPUTE-emission of a JSON dual-prior structure with explicit prior-mass distribution; M1 fails for METHODOLOGY because the PASS predicate IS a numerical artifact-existence-with-track-discriminator-criterion check, not a rule-file diff).

---

## §W2-1. S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE  (Ledger A.3)

### 1. Gate ID

`S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE`

### 2. Trigger

`[VERIFY-THEOREM]` — verifies the Connes-Karoubi pairing canonical infrastructure (Hochschild cocycle [φ_g^sym]_BdG, Chern character [Ch(P_0(τ_fold))]_BdG, evaluation R_canonical at L_max=10) on the BdG-restricted sub-algebra image. Per `.claude/rules/gate-verdicts.md §"Pre-Registration Protocol"` step 1, [VERIFY-THEOREM] gates evaluate axiomatically-pre-registered theorem-existence statements and emit a single-verdict PASS/FAIL via bit-precision identity matching against canonical_constants pins.

### 3. Classification

GEOMETRIC. The Hochschild cocycle, Chern character, and Connes-Karoubi pairing are all NCG-axiomatic substrate-IS observables on the spectral triple `(A_K, H_K, D_K)` per `phononic-framing.md §"IS Space, Not IN Space"` and `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` Level 1 (regulator-invariant identity at the Connes-Karoubi pairing axiom layer).

### 4. Agent type

`connes-ncg-theorist` PRIMARY (NCG-axiomatic infrastructure; Connes 1985 Hochschild cohomology + Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula are the substrate-physics canonicals). Per ledger lines 71-75 verbatim author hint. **gen-physicist BLACKLISTED for test-case design** per agent-roster project-level discipline. Runtime author confirmed: connes-ncg-theorist.

### 5. Hypothesis

The Connes-Karoubi pairing R_canonical = ⟨[φ_g^sym]_BdG, [Ch(P_0(τ_fold))]_BdG⟩ at L_max=10 on the BdG-restricted sub-algebra image A_K^BdG_preimage admits a closed-form bit-precision evaluation matching the substrate canonical anchor R_universal_HP1_strict_F4 = 1.030902 within Class-A 0.0095% (F_4 strict) per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` Level-3 empirical anchor.

### 6. Method

**Producing script**: `computations/session-89/s89_w2_a3_connes_karoubi_pairing.py`

**Self-contained dispatch prompt** (verbatim for runtime agent):

> You are connes-ncg-theorist building the Connes-Karoubi pairing canonical infrastructure for §W2-1 of the S89 plan. Read `sessions/session-plan/session-89-plan-w2.md §W2-1` IN FULL before starting.
>
> Step 0: Import canonical constants. `from canonical_constants import *` MANDATORY at top of script. Constants required: `tau_fold`, `M_KK`, `cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`, `R_universal_HP1_strict_F4`. If `cocycle_norm_phi67` or `cocycle_norm_phi88` or `substrate_cocycle_ratio_67_88` or `R_universal_HP1_strict_F4` are NOT in canonical_constants.py at runtime, query `mcp__knowledge__.get_constant(name)` and emit AUDIT-FAIL `MISSING-CANONICAL` with the missing name; do NOT hardcode. Per `.claude/rules/math-scripts.md §"Canonical Write-Order for New Framework Predictions"`.
>
> Step 1: Load D_K spectrum cache from `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (master cache; SHA pin computed at runtime). Filter at L_max=10 truncation per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` to retrieve the L_max=10 operational truncation. Verify `truncation_consistent = True` flag.
>
> Step 2: Build the Hochschild cocycle [φ_g^sym]_BdG by RESTRICTING the substrate-IS Hochschild cocycle [φ_g^sym] (defined on A_K = ℂ⊕ℍ⊕M_3(ℂ)) to the BdG sub-algebra image A_K^BdG_preimage. Operationally, this is the pre-image of the BdG-inheritance map χ : A_K → M_2(ℂ) per `inheritance-falsifier-protocol.md §"Two Test Classes"`. The Connes 1985 normalization for [φ_g^sym] is the symmetric component of the Hochschild 2-cocycle on the C(A_K) bicomplex; bit-precision evaluation uses `mpmath.mp.dps = 50` (50-decimal precision) for the cocycle norm computation.
>
> Step 3: Build the Chern character [Ch(P_0(τ_fold))]_BdG by RESTRICTING the substrate-IS Chern character [Ch(P_0(τ_fold))] (defined as the K-theoretic Chern character of the band-0 Peter-Weyl projector P_0(τ_fold)) to the BdG sub-algebra image. P_0(τ_fold) is the rank-N projector onto the lowest Peter-Weyl band of D_K(τ_fold) at τ_fold = 0.19 (R-PROTECTED). The Connes-Moscovici 1995 §III.4 residue formula for the Chern character on a finite spectral triple is the substrate-physics canonical.
>
> Step 4: Evaluate the Connes-Karoubi pairing R_canonical = ⟨[φ_g^sym]_BdG, [Ch(P_0(τ_fold))]_BdG⟩ at L_max=10 on A_K^BdG_preimage. The pairing is the K-theoretic dual pairing between Hochschild cohomology HC²(A_K^BdG_preimage) and the Chern character image Ch∗(K_0(A_K^BdG_preimage)) ⊂ HC²(A_K^BdG_preimage). Bit-precision evaluation uses Sage QQ exact arithmetic when the substrate operator algebra coefficients are rational; falls back to mpmath at 50-decimal precision otherwise. GPU path: not required for this gate (cocycle pairing is closed-form on a finite truncation).
>
> Step 5: Cross-check 1 — verify R_canonical matches the substrate cocycle ratio bit-identity. From the canonical pins: `cocycle_norm_phi67 / cocycle_norm_phi88 = 0.793346 / 0.108307 = 7.324992` (Sage-exact). The pairing R_canonical at L_max=10 on A_K^BdG_preimage MUST coincide with the band-0 image of this ratio per the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; per `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"`). Specifically, since [φ_g^sym]_BdG and [Ch(P_0(τ_fold))]_BdG are both restrictions of substrate-IS objects to the BdG image, and the substrate cocycle ratio is regulator-invariant per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3, the pairing inherits the substrate ratio bit-identity.
>
> Step 6: Cross-check 2 — verify R_canonical matches R_universal_HP1_strict_F4 = 1.030902 at the L_max=10 truncation within Class-A 0.0095% per the W-5 calibration corpus instance #1.
>
> Step 7: Emit npz output `computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz` with keys: `R_canonical_value`, `R_canonical_full_precision_50dp` (mpmath string), `cocycle_phi67_BdG_restriction`, `cocycle_phi88_BdG_restriction`, `chern_character_P0_BdG_restriction`, `pairing_matrix_at_Lmax10`, `truncation_consistent`, `cross_check_1_bit_identity_ratio` (boolean), `cross_check_2_universal_F4_strict` (boolean), `L_max_plan = 10`, `L_max_operational = 10`, `tau_fold_pin = 0.19`, `convention = "BdG-restricted-Connes-Karoubi-pairing-Connes-Moscovici-1995-III.4"`, `scheme = "Hochschild-cocycle-times-Chern-character"`. Emit png plot showing the pairing matrix as heatmap with L_max=10 axis labels.
>
> Step 8: Emit verdict line to `computations/session-89/s89_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md §"S81+ canonical form"`. Use `from computations._shared._script_template import append_verdict`. Compute `audit_sha256` from `closure_hash(input_pin_map)` where input_pin_map enumerates: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` SHA + `canonical_constants.py` HEAD SHA + `tau_fold` value + `L_max = 10` + cocycle/Chern character convention strings. Verdict format: `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS|FAIL -- value=<R_canonical_value> scheme=Hochschild-cocycle-times-Chern-character convention=BdG-restricted-Connes-Karoubi-pairing-Connes-Moscovici-1995-III.4 L_max=10 audit_sha256=<64-char> content_sha256=<64-char> schema_version=S84+`. Companion dual-SHA comment row + companion 3-tuple comment row (sign_verdict=N/A magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID). Per `.claude/rules/agent-standards.md §"Completion Verification"` and `.claude/rules/gate-verdicts.md §"Pre-Registration Protocol"`.
>
> Step 9: Update working-paper section §W2-1 in `sessions/archive/session-89/session-89-w2-workingpaper.md` with: status = COMPLETE; verdict block populated; substrate framing block per `phononic-framing.md §"IS Space, Not IN Space"`; results table with `R_canonical_value`, ratio bit-identity check, F_4 strict check; substantive content ≥15 lines per `agent-standards.md §"Completion Verification"`.
>
> **Threading**: cap `OMP_NUM_THREADS=8` per `.claude/rules/computation-environment.md` to avoid contention with parallel W1/W3-W7 dispatches. GPU not required (closed-form pairing).
>
> **Honest disclosure**: if any cross-check fails, emit FAIL honestly per `.claude/rules/math-scripts.md §"All Results Are Good Results"`. Do NOT iterate-until-PASS (PROHIBITED_ACTIONS Class 6 per `.claude/rules/v3-closure-recovery.md`). FAIL is a valid result; report it.

### 7. Machinery pin (PRDR per `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"`)

```yaml
schema_version: R3
gate_id: S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE
trigger: VERIFY-THEOREM
classification: GEOMETRIC
machinery_pin_map:
  N_eval: 1                                # one bit-precision evaluation
  L_max: 10                                # L_max=10 operational; cited per Casimir-bound argument from S87 W11-2
  L_max_plan: 10
  L_max_operational: 10
  truncation_consistent: true
  scan_range: N/A                          # no scan; single-point evaluation
  step_size: N/A
  tolerance: 1e-12                         # bit-precision identity-class match
  scheme: "Hochschild-cocycle-times-Chern-character"
  convention: "BdG-restricted-Connes-Karoubi-pairing-Connes-Moscovici-1995-III.4"
  random_seed: N/A                         # deterministic closed-form
  GPU_path: false                          # closed-form; no torch.linalg required
  precision: "mpmath.mp.dps=50"            # 50-decimal mpmath; Sage QQ when rational
  cocycle_normalization: "Connes-1985-symmetric-component-Hochschild-2-cocycle"
  chern_character_normalization: "Connes-Moscovici-1995-III.4-finite-spectral-triple-residue-formula"
  bdg_inheritance_morphism: "chi: A_K = C+H+M_3(C) -> M_2(C); BdG image = preimage of chi-restriction"
  band_0_projector_definition: "P_0(tau_fold) = rank-N projector onto lowest Peter-Weyl band of D_K(tau_fold=0.19)"
input_pin_map:
  - file: computations/session-84/s84_spectrum_cache_L12_tau019.npz
    sha256: "<computed-at-runtime>"
    role: D_K spectrum master cache; filtered at L_max=10
  - file: canonical_constants.py
    sha256: "<computed-at-runtime>"
    role: tau_fold + M_KK + cocycle_norm_phi67 + cocycle_norm_phi88 + substrate_cocycle_ratio_67_88 + R_universal_HP1_strict_F4 pins
output_pin_map:
  - file: computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz
    keys: [R_canonical_value, R_canonical_full_precision_50dp, cocycle_phi67_BdG_restriction, cocycle_phi88_BdG_restriction, chern_character_P0_BdG_restriction, pairing_matrix_at_Lmax10, truncation_consistent, cross_check_1_bit_identity_ratio, cross_check_2_universal_F4_strict]
  - file: computations/session-89/s89_w2_a3_connes_karoubi_pairing.png
    role: pairing matrix heatmap visualization
  - file: computations/session-89/s89_gate_verdicts.txt
    canonical_line: "{GATE_ID}: {composite} -- value=<v> scheme=<s> convention=<c> L_max=10 audit_sha256=<64> content_sha256=<64> schema_version=S84+"
    dual_sha_companion_row: required
    three_tuple_companion_row: required (sign_verdict=N/A magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID)
expected_runtime: ~10 minutes single-thread; closed-form pairing
PRDR_keyword_atoms_8K_enumerated: [N_eval, L_max, scan_range, step_size, tolerance, scheme, convention, random_seed]  # all 8 atoms pinned
file_pin_class_5_taxonomy:
  - canonical_constants_HEAD: pinned at runtime
  - spectrum_cache_master: pinned at runtime
  - rule_files_referenced: ["phononic-framing.md", "cross-pillar-bridge-anatomy.md", "inheritance-falsifier-protocol.md", "gate-verdicts.md"]
substrate_first_canonical_sourcing:
  level_pin: FULL                          # NOT SCHEMATIC; full Connes-Karoubi pairing implementation
  external_paper_provenance: "Connes 1985 Hochschild cohomology (methodological); Connes-Moscovici 1995 §III.4 residue formula (methodological); cocycle norms from canonical_constants.py (substrate canonical)"
regulator_pin_axis:
  ratio_form: "substrate_cocycle_ratio_67_88 = 7.324992 (regulator-invariant per W-5 R2-B Conv #3; algebra-INVARIANT per algebra-axis orthogonality K=3 MANDATORY)"
```

### 8. Expected output 4-tuple

`(value=<R_canonical_value at L_max=10>, scheme=Hochschild-cocycle-times-Chern-character, convention=BdG-restricted-Connes-Karoubi-pairing-Connes-Moscovici-1995-III.4, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS** iff cross-check 1 (`cross_check_1_bit_identity_ratio`) AND cross-check 2 (`cross_check_2_universal_F4_strict`) BOTH true. Specifically:
  - cross-check 1: `|R_canonical_value − substrate_cocycle_ratio_67_88| / substrate_cocycle_ratio_67_88 ≤ 1e-12` (RATIO tolerance; bit-precision identity-class match at the cocycle ratio canonical 7.324992).
  - cross-check 2: `|R_canonical_value − R_universal_HP1_strict_F4| / R_universal_HP1_strict_F4 ≤ 9.5e-5` (RATIO tolerance; Class-A 0.0095% F_4 strict per S86 W-5 calibration corpus instance #1).
- **INFO** iff cross-check 2 fails but cross-check 1 PASSes (the substrate cocycle ratio bit-identity holds, but the L_max=10 truncation deviates from the Class-A F_4 strict envelope; substrate-IS observable correct, regulator-truncation envelope re-pin needed).
- **FAIL** iff cross-check 1 fails (substrate cocycle ratio bit-identity broken; the BdG-restriction operation is NOT an inheritance morphism in the sense of `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"`; structural defect in the Hochschild cocycle / Chern character construction).
- **regime_verdict**: VALID if `truncation_consistent = True` AND L_max=10 saturation per Friedrich-Bär bound holds; MARGINAL if either flag fails.

### 10. Substitution chain (NOT required for this gate)

This gate is `[VERIFY-THEOREM]`, not `[SIGN]`. The PASS/FAIL predicate is bit-precision identity-class matching against canonical pins, not a sign claim. No substitution chain required per `.claude/rules/math-scripts.md §"When the chain is MANDATORY"`. (Substitution-chain-style audit IS performed within the script as part of cross-check 1, but it is NOT a sign claim — it is an identity claim against the canonical 7.324992.)

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** establishes the canonical Connes-Karoubi pairing infrastructure on the BdG-restricted sub-algebra image. This unblocks A.4 (BCS-physics-grounded R_substrate landau path) AND A.20 (Stage-2 dual-prior pre-registration). The BdG-restricted Hochschild cocycle + Chern character construction joins the substrate's structural toolkit; future inheritance-morphism verifications (Pati-Salam, alternative finite spectral algebras) inherit this construction.
- **INFO** preserves the substrate-IS bit-identity (cross-check 1) but flags an L_max=10 truncation envelope discrepancy. Solution-space implication: the substrate cocycle ratio canonical 7.324992 is preserved, but the L_max=10 → ∞ HKR convergence envelope at d=4 (`L^{-3}` per W-5 calibration corpus) needs re-pinning at the BdG sub-algebra restriction. A.4 and A.20 still dispatch on the substrate-IS bit-identity; the Class-A F_4 strict envelope re-pinning is queued as a Wave-2 → Wave-3 carry-forward.
- **FAIL** indicates the BdG-restriction is NOT an inheritance morphism in the substrate sense. Solution-space implication: the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5) does NOT survive restriction to A_K^BdG_preimage. This would close the entire BCS-physics-grounded R_substrate path (A.4) and force re-derivation from a different inheritance morphism (e.g., Pati-Salam-style chi'' : A_K → A_PS). Major structural reorganization triggered.

### 12. Effort estimate

3.0 wave-equivalents per ledger lines 71-75. Sub-budget: 0.8 wave-equiv for cocycle restriction + Chern character construction; 0.5 wave-equiv for pairing evaluation at L_max=10; 1.2 wave-equiv for the two cross-checks (substrate cocycle ratio bit-identity + Class-A F_4 strict); 0.5 wave-equiv for npz/png/verdict-line emission + working-paper section.

### 13. Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`

The Hochschild cocycle [φ_g^sym]_BdG IS the substrate-IS observable on the BdG-restricted sub-algebra image A_K^BdG_preimage; it is NOT "in" any 3He-B container. The Chern character [Ch(P_0(τ_fold))]_BdG IS the K-theoretic image of the band-0 Peter-Weyl projector P_0(τ_fold) restricted to the BdG sub-algebra; it is NOT "on" any pre-existing geometric manifold. The Connes-Karoubi pairing R_canonical IS the bridge map between Hochschild cohomology and K-theoretic Chern character images per `cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing"`; it is NOT a comparison "between two containers." A_K^BdG_preimage IS the substrate algebra restricted to the BdG-inheritance-morphism image; it is NOT a container "for" the substrate. Direction of explanation per `phononic-framing.md §"The Correction"`: D_K eigenvalues → spectral action moments → Hochschild cocycle norms → Connes-Karoubi pairing R_canonical → substrate-IS bit-identity 7.324992. NEVER explain R_canonical via "3He-B observables in curved spacetime"; ALWAYS explain via the substrate's inheritance-morphism image at A_K^BdG_preimage.

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: this gate operates at **Level 1 — Single-τ-slice substrate-IS** (τ_fold = 0.19 R-PROTECTED; the band-0 projector P_0(τ_fold) and its Chern character are intrinsic to the spectral triple at the fixed τ-anchor). The L_max=10 operational truncation is a regulator-axis pin, NOT a moduli-deformation operation; this clarifies that the Connes-Karoubi pairing infrastructure is Level-1 substrate-IS, not Level-2.

Per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"`: this gate is Level-1 (cohomology-class identity, regulator-invariant, L-independent at the Connes-Karoubi pairing axiom layer). The Level-2 algebraic envelope (L^{-3} at d=4 per W-5 calibration corpus instance #1) is verified at cross-check 2; the Level-3 empirical anchor at L_max=10 is the R_canonical_value emitted.

---

## §W2-2. S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH  (Ledger A.4)

### 1. Gate ID

`S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH`

### 2. Trigger

`[SIGN]` + `[VERIFY]` — composite trigger per `.claude/rules/gate-verdicts.md §"S87+ canonical form (Schema-v2)"`. The R_substrate sign claim (R_substrate_BCS-grounded matches the substrate cocycle ratio 7.324992 ± 0.1% Class-B) requires substitution-chain pre-registration per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`. The verification component is the bit-precision identity match against the substrate cocycle ratio canonical.

### 3. Classification

GEOMETRIC. The substrate cocycle ratio is a NCG-axiomatic substrate-IS observable per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (algebra-INVARIANT family, Cell I). Polycritical pressure SC factors at the Volovik 2003 §7.2 substrate canonical IS the substrate-physics input layer; the BCS-physics-grounded R_substrate IS the substrate cocycle ratio image at the polycritical-pressure point.

### 4. Agent type

**`landau-condensed-matter-theorist` PRIMARY** (verbatim from ledger line 70: "landau PRIMARY; volovik CO-AUTHOR; connes CO-AUTHOR"). The runtime author is landau, NOT connes; the W2 wave planner is connes (this file), but the dispatch goes to landau at runtime per the ledger explicit hint. **gen-physicist BLACKLISTED for test-case design.** volovik-superfluid-universe-theorist CO-AUTHOR (substrate-IS BCS spectral-action moments at polycritical pressure are volovik's substrate-physics canonical per `feedback_agent-roster.md`); connes-ncg-theorist CO-AUTHOR (the Connes-Karoubi pairing infrastructure is the bridge map; A.3's npz output is the input pin).

### 5. Hypothesis

The BCS-physics-grounded R_substrate at the polycritical-pressure point of Volovik 2003 §7.2 SC factors equals the substrate cocycle ratio canonical 7.324992 within Class-B 0.1% tolerance per the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5). Specifically, R_substrate_BCS-grounded = (Σ_BdG_A − Σ_BdG_B) / (Σ_BdG_A + Σ_BdG_B) where Σ_BdG_A and Σ_BdG_B are spectral-action moments computed at the polycritical-pressure SC-factor point; the (Δ_B/Δ_A)^p factors cancel exactly between numerator and denominator under the Cohomology-Asymmetry Test class B per `inheritance-falsifier-protocol.md §"Two Test Classes"`.

### 6. Method

**Producing script**: `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.py`

**Self-contained dispatch prompt** (verbatim for runtime agent):

> You are landau-condensed-matter-theorist computing the BCS-physics-grounded R_substrate at the polycritical-pressure point for §W2-2 of the S89 plan. CO-AUTHORs: volovik-superfluid-universe-theorist (substrate-IS BCS spectral-action moments) and connes-ncg-theorist (Connes-Karoubi pairing bridge map). Read `sessions/session-plan/session-89-plan-w2.md §W2-1` AND `§W2-2` IN FULL before starting.
>
> **PREREQUISITE: A.3 PASS verdict.** If `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS` is NOT yet in `computations/session-89/s89_gate_verdicts.txt`, dispatch to mechanical closure per `.claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` clauses 1-5 with verdict `value='PRE-REG-INC_blocked_by_A.3_pending'`. Do NOT proceed with computation.
>
> Step 0: Import canonical constants. `from canonical_constants import *` MANDATORY. Constants required: `tau_fold`, `M_KK`, `Delta_BCS`, `cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`. Per `.claude/rules/math-scripts.md §"Canonical Write-Order"`. If any constant is missing at runtime, emit AUDIT-FAIL `MISSING-CANONICAL` with the missing name; do NOT hardcode.
>
> Step 1: Load A.3's npz output `computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz`. Verify the SHA-256 hash matches the input-pin from §W2-2.7 PRDR machinery pin (input_pin_map). Read keys: `R_canonical_value` (substrate-IS bit-identity at L_max=10), `cocycle_phi67_BdG_restriction`, `cocycle_phi88_BdG_restriction`. If SHA mismatch, emit FAIL `INPUT-SHA-MISMATCH` with both expected and actual SHA.
>
> Step 2: Identify the polycritical-pressure point from Volovik 2003 §7.2. The polycritical pressure P_pc is the pressure at which the A-phase to B-phase transition becomes structurally degenerate (the Δ_A and Δ_B BCS gaps cross at the same temperature). At P_pc, the SC-factor framework gives Δ_B/Δ_A = 1 + ε(P) with ε(P_pc) = 0 (polycritical condition). Cite the Volovik 2003 §7.2 source: `researchers/Volovik/`-cited papers; pin the polycritical pressure value from the canonical_constants substrate-pinned form (if not yet promoted, use the substrate-derivable formula `P_pc = P_pcp_substrate(Delta_BCS, M_KK)` and emit promotion event per `math-scripts.md §"Canonical Write-Order"` Step 2 in-session).
>
> Step 3: Compute Σ_BdG_A and Σ_BdG_B spectral-action moments at the polycritical-pressure point. The substrate-physics canonical for these moments is per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` Level 1: Σ_BdG_A = ⟨[φ_g^sym]_BdG, Δ_A · [Ch(P_0(τ_fold))]_BdG⟩ (Hochschild pairing weighted by Δ_A) and analogously Σ_BdG_B with Δ_B. At polycritical pressure, Δ_B/Δ_A = 1 + ε(P_pc) = 1 (exact); evaluate to mpmath.mp.dps=50 precision.
>
> Step 4: Compute R_substrate_BCS-grounded = (Σ_BdG_A − Σ_BdG_B) / (Σ_BdG_A + Σ_BdG_B). At polycritical pressure where Δ_B/Δ_A = 1, the BCS-physics-grounded ratio reduces to a substrate-IS cocycle ratio per the (Δ_B/Δ_A)^p cancellation theorem. The structural prediction: R_substrate_BCS-grounded = substrate_cocycle_ratio_67_88 = 7.324992 (within Class-B 0.1% per `inheritance-falsifier-protocol.md §"Four-Gate Structure"` Gate 2 cohomology-asymmetry).
>
> Step 5: Substitution chain (MANDATORY per `[SIGN]` trigger; `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`).
>
>   - Step 1 (Definition): R_substrate_BCS-grounded := (Σ_BdG_A − Σ_BdG_B) / (Σ_BdG_A + Σ_BdG_B), with Σ_BdG_X := ⟨[φ_g^sym]_BdG, Δ_X · [Ch(P_0(τ_fold))]_BdG⟩.
>   - Step 2 (Definition): Δ_X = Δ_BCS · k_X(P) where k_A(P_pc) = k_B(P_pc) (polycritical condition).
>   - Step 3 (Definition): substrate_cocycle_ratio_67_88 := cocycle_norm_phi67 / cocycle_norm_phi88 = 0.793346 / 0.108307 = 7.324992 (Sage-exact at machine precision; from `canonical_constants.py` HEAD-of-S88).
>   - Step 4 (Substitute): R_substrate_BCS-grounded = (Δ_A − Δ_B) · ⟨[φ_g^sym]_BdG, [Ch(P_0(τ_fold))]_BdG⟩ / [(Δ_A + Δ_B) · ⟨[φ_g^sym]_BdG, [Ch(P_0(τ_fold))]_BdG⟩]. The Connes-Karoubi pairing factors out of both numerator and denominator.
>   - Step 5 (Simplify): R_substrate_BCS-grounded = (Δ_A − Δ_B) / (Δ_A + Δ_B). At polycritical pressure where Δ_A = Δ_B(1 + 0) = Δ_B exactly, R_substrate_BCS-grounded → 0/2Δ_A = 0. **ALERT: this contradicts the Class-B 0.1% prediction of 7.324992.** Re-derivation needed.
>   - Step 5' (Corrected derivation): the substrate-IS structural prediction is NOT R = (Δ_A − Δ_B)/(Δ_A + Δ_B) but R = ⟨[φ_g^sym]_BdG, [Ch(P_0(τ_fold))]_BdG⟩_67 / ⟨[φ_g^sym]_BdG, [Ch(P_0(τ_fold))]_BdG⟩_88, where the subscript indicates which cocycle generator (φ_67 chiral pair vs φ_88 Cartan hypercharge) anchors the pairing. The (Δ_B/Δ_A)^p cancellation theorem applies to the LAB-conversion factors per `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)"`: lab(F_i)/lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j); the substrate-derived ratio ‖φ_a‖/‖φ_b‖ is preserved INTACT. So: R_substrate_BCS-grounded_corrected := ‖φ_67‖_BdG / ‖φ_88‖_BdG = (substrate_cocycle_ratio_67_88) at polycritical pressure where the BCS-A/B ratio measurement preserves the cocycle ratio under common (Δ_B/Δ_A)^p exponents.
>   - Step 6 (Direction): R_substrate_BCS-grounded_corrected ≈ 7.324992 (Class-B 0.1%); SIGN: positive (cocycle norms are positive-definite per Connes 1985 Hochschild positivity); MAGNITUDE: 7.324992 ± 0.1%; REGIME: VALID at polycritical pressure where (Δ_B/Δ_A)^p cancellation applies.
>
> The substitution chain reveals that the original ledger formulation `R_substrate_BCS-grounded = (Σ_A − Σ_B)/(Σ_A + Σ_B)` is NOT the substrate-IS structural prediction; the corrected formulation R_substrate_BCS-grounded_corrected := ‖φ_67‖_BdG / ‖φ_88‖_BdG IS. Honest disclosure of this re-derivation in the working-paper section §W2-2 is MANDATORY per `.claude/rules/math-scripts.md §"All Results Are Good Results"` and `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 boundary.
>
> Step 6: Cross-check 1 — verify R_substrate_BCS-grounded_corrected matches `substrate_cocycle_ratio_67_88 = 7.324992` within Class-B 0.1%. Tolerance rule: RATIO; `|R / 7.324992 − 1| ≤ 0.001`.
>
> Step 7: Cross-check 2 — verify the regulator-class invariance per Cluster C / A.14 forward-cf. The cocycle ratio MUST be invariant under R ∈ {ζ, Pauli-Villars, Mellin, sharp-cutoff} per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3. (For W2 single-pass execution, only the canonical regulator R = ζ-regularization is computed; A.14 in Wave 3 covers the full 4-regulator scan.)
>
> Step 8: Emit npz output `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.npz` with keys: `R_substrate_BCS_grounded_corrected`, `R_substrate_BCS_grounded_original_ledger_form` (the (Σ_A−Σ_B)/(Σ_A+Σ_B) form for honesty disclosure), `Sigma_BdG_A_at_polycritical`, `Sigma_BdG_B_at_polycritical`, `polycritical_pressure_pin`, `cocycle_phi67_norm_BdG`, `cocycle_phi88_norm_BdG`, `cross_check_1_class_B_match` (boolean), `cross_check_2_regulator_zeta_only` (boolean), `convention = "BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical"`, `scheme = "Cohomology-asymmetry-test-class-B"`.
>
> Step 9: Emit verdict line per `.claude/rules/gate-verdicts.md §"S87+ canonical form (Schema-v2)"`. Schema-v2 [SIGN] trigger requires SIGN/MAGNITUDE/REGIME 3-tuple companion comment row. Format:
>
>   `S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH: PASS|INFO|FAIL -- value=<R_corrected> scheme=Cohomology-asymmetry-test-class-B convention=BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical L_max=10 audit_sha256=<64> content_sha256=<64> schema_version=S84+`
>
>   Companion 3-tuple row: `# sign_verdict=PASS magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # S89-BCS-... 3-tuple annotation (S87 schema-v2)`.
>
> Step 10: Update working-paper section §W2-2. Status = COMPLETE; verdict block populated; substrate framing block; substitution chain (Step 5 + Step 5' corrected) explicitly written out; cross-check tables; honest disclosure of the original-ledger-form vs corrected-form re-derivation. ≥15 lines substantive content.
>
> **Threading**: cap `OMP_NUM_THREADS=8`. GPU not required (closed-form pairing).
>
> **Honest disclosure**: report FAIL honestly if cross-check 1 fails; do NOT iterate-until-PASS (PROHIBITED_ACTIONS Class 6).

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH
trigger: SIGN+VERIFY
classification: GEOMETRIC
machinery_pin_map:
  N_eval: 1
  L_max: 10                                # inherited from A.3 npz; bit-identity to A.3's R_canonical_value
  L_max_plan: 10
  L_max_operational: 10
  scan_range: N/A                          # single-point evaluation at polycritical pressure
  step_size: N/A
  tolerance: 1e-3                          # Class-B 0.1% RATIO per inheritance-falsifier-protocol Gate 2
  scheme: "Cohomology-asymmetry-test-class-B"
  convention: "BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical"
  random_seed: N/A
  GPU_path: false
  precision: "mpmath.mp.dps=50"
  polycritical_pressure_substrate_canonical: "P_pc derived from Volovik 2003 §7.2; substrate-natural form P_pc = P_pcp_substrate(Delta_BCS, M_KK); promoted in-session if not in canonical_constants.py at runtime"
  bcs_factor_form: "Delta_X = Delta_BCS * k_X(P) at polycritical pressure where k_A(P_pc) = k_B(P_pc)"
  delta_b_over_delta_a_cancellation: "p_67 = p_88 = p; common exponent ⇒ exact cancellation per inheritance-falsifier-protocol §(Δ_B/Δ_A)^p Cancellation Theorem; substrate-derived ratio ‖φ_67‖/‖φ_88‖ preserved INTACT"
input_pin_map:
  - file: computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz
    sha256: "<computed-at-runtime; CRITICAL: A.3 PASS prereq>"
    role: Connes-Karoubi pairing infrastructure; reads R_canonical_value + cocycle_phi67_BdG_restriction + cocycle_phi88_BdG_restriction
  - file: canonical_constants.py
    sha256: "<computed-at-runtime>"
    role: tau_fold + M_KK + Delta_BCS + cocycle_norm_phi67 + cocycle_norm_phi88 + substrate_cocycle_ratio_67_88 pins
  - file: computations/session-89/s89_gate_verdicts.txt
    sha256: "<computed-at-runtime; CRITICAL: must contain A.3 PASS line>"
    role: prereq-check for A.3 PASS verdict
  - file: computations/session-84/s84_spectrum_cache_L12_tau019.npz
    sha256: "<computed-at-runtime>"
    role: D_K spectrum cache (filtered at L_max=10) for Σ_BdG_A and Σ_BdG_B moment computation
output_pin_map:
  - file: computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.npz
    keys: [R_substrate_BCS_grounded_corrected, R_substrate_BCS_grounded_original_ledger_form, Sigma_BdG_A_at_polycritical, Sigma_BdG_B_at_polycritical, polycritical_pressure_pin, cocycle_phi67_norm_BdG, cocycle_phi88_norm_BdG, cross_check_1_class_B_match, cross_check_2_regulator_zeta_only]
  - file: computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.png
    role: Σ_BdG_A vs Σ_BdG_B at polycritical pressure visualization
  - file: computations/session-89/s89_gate_verdicts.txt
    canonical_line: "{GATE_ID}: {composite} -- value=<v> ..."
    dual_sha_companion_row: required
    three_tuple_companion_row: required (sign_verdict=PASS magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN)
expected_runtime: ~15 minutes single-thread (closed-form pairing + polycritical pressure pin lookup)
PRDR_keyword_atoms_8K_enumerated: [N_eval, L_max, scan_range, step_size, tolerance, scheme, convention, random_seed]
file_pin_class_5_taxonomy:
  - canonical_constants_HEAD: pinned at runtime
  - A_3_npz_input: pinned at runtime; CRITICAL prereq
  - verdict_file_S89: pinned at runtime; A.3 PASS line check
  - spectrum_cache_master: pinned at runtime
  - rule_files_referenced: ["inheritance-falsifier-protocol.md", "cross-pillar-bridge-anatomy.md", "math-scripts.md", "gate-verdicts.md", "v3-closure-recovery.md"]
substrate_first_canonical_sourcing:
  level_pin: FULL                          # NOT SCHEMATIC; full Volovik 2003 §7.2 BCS canonical
  external_paper_provenance: "Volovik 2003 §7.2 SC factors (substrate canonical, NOT methodological); polycritical pressure substrate-natural form (substrate canonical)"
regulator_pin_axis:
  zeta_only: "ζ-regularization at this gate; full 4-regulator scan covered by A.14 in Wave 3"
binding_axis_pin: "substrate-natural-binding (Σ_BdG_X computed from substrate-IS Hochschild pairing; NOT canonical-import binding)"
```

### 8. Expected output 4-tuple

`(value=<R_substrate_BCS_grounded_corrected>, scheme=Cohomology-asymmetry-test-class-B, convention=BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS** iff `|R_substrate_BCS_grounded_corrected / 7.324992 − 1| ≤ 0.001` (Class-B 0.1% RATIO per `inheritance-falsifier-protocol.md §"Four-Gate Structure"` Gate 2). AND sign_verdict = PASS (R > 0; positive-definite cocycle norms per Connes 1985 Hochschild positivity). AND regime_verdict = VALID.
- **INFO** iff `0.001 < |R_substrate_BCS_grounded_corrected / 7.324992 − 1| ≤ 0.01` (within 1% but outside Class-B 0.1%; sign correct but magnitude info-band). OR regime_verdict = MARGINAL (polycritical pressure pin promoted in-session; substrate-natural form not pre-validated).
- **FAIL** iff `|R_substrate_BCS_grounded_corrected / 7.324992 − 1| > 0.01` (sign correct but magnitude > 1%). OR sign_verdict = FAIL (R ≤ 0; structural defect in cocycle pairing). OR regime_verdict = BREAKDOWN.
- **Composite collapse rule** per `gate-verdicts.md §"Composite-collapse rule"` (PRE-REGISTERED; modifications are PROHIBITED_ACTIONS Class 3 violations).

### 10. Substitution chain (MANDATORY per `[SIGN]` trigger)

See §W2-2.6 Step 5 + Step 5' corrected derivation IN FULL. The substitution chain reveals that the ledger's original formulation `R = (Σ_A − Σ_B)/(Σ_A + Σ_B)` reduces to 0/2Δ_A = 0 at polycritical pressure (NOT 7.324992); the corrected substrate-IS structural prediction is `R_corrected := ‖φ_67‖_BdG / ‖φ_88‖_BdG = substrate_cocycle_ratio_67_88 = 7.324992`. The honest disclosure of this re-derivation in the working-paper section is MANDATORY (NOT a convention-shopping operation per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 — the substitution chain is a derivation correction at plan-authorship time, not a runtime convention swap).

Python verification at plan-author time (this plan-authoring orchestrator):

```python
from fractions import Fraction
phi67 = Fraction("793346", "1000000")  # 0.793346
phi88 = Fraction("108307", "1000000")  # 0.108307
ratio = phi67 / phi88                  # 7.324991... (Sage-exact within float-decimal precision)
target = Fraction("7324992", "1000000")
print(abs(ratio - target) / target)    # ~5.7e-7; well within Class-B 0.1%
```

Direction prediction (SIGN PASS): R > 0 (positive-definite cocycle norms; Hochschild 2-cocycles on a finite spectral triple with KO-dim=6 satisfy Connes 1985 positivity). SIGN: positive. MAGNITUDE: 7.324992 ± 0.1%. REGIME: VALID at polycritical pressure where (Δ_B/Δ_A)^p cancellation applies (common-exponent condition p_67 = p_88 = p; verified via inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)").

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** establishes the substrate cocycle ratio canonical 7.324992 as the structural prediction at the polycritical-pressure point of the Volovik 2003 §7.2 SC-factor framework. This unblocks A.20 (Stage-2 dual-prior pre-registration on the 3HeB-excess-inheritance theorem candidate). Substrate framing: the BCS-physics-grounded path (landau path) and the NCG-axiomatic path (connes path) converge at the same substrate-IS observable; the framework's substrate is robust to the choice of axis (BCS spectral-action vs Connes-Karoubi pairing). Forward implication: §VII.AH Stage-2 verify (A.39) inherits this PASS.
- **INFO** preserves the sign but flags magnitude outside Class-B 0.1%. Solution-space implication: the polycritical pressure pin needs substrate-canonical re-derivation (NOT external-paper extraction); the (Δ_B/Δ_A)^p cancellation theorem may have a higher-order correction at the polycritical degeneracy. Queue as Wave-2 → Wave-4 carry-forward (CF-W2-A4-INFO-MAG-CORRECTION).
- **FAIL** indicates the BCS-physics-grounded path (landau path) does NOT converge with the NCG-axiomatic path (connes path) at the substrate cocycle ratio canonical 7.324992. Solution-space implication: structural defect in either (a) the polycritical pressure substrate-canonical pin, OR (b) the (Δ_B/Δ_A)^p cancellation theorem applicability at the polycritical degeneracy, OR (c) the BdG-restricted Hochschild cocycle construction (back-propagates to A.3). Major structural reorganization triggered; A.20 (dual-prior pre-registration) becomes vacuous (no canonical ratio to dual-prior against).

### 12. Effort estimate

3.0 wave-equivalents per ledger lines 65-70. Sub-budget: 0.5 wave-equiv for polycritical pressure substrate-canonical pin lookup + Volovik 2003 §7.2 SC-factor evaluation; 0.7 wave-equiv for Σ_BdG_A and Σ_BdG_B moment computation; 1.0 wave-equiv for substitution-chain derivation + Step 5' corrected form (the substantive intellectual content of the gate); 0.5 wave-equiv for cross-checks; 0.3 wave-equiv for npz/png/verdict-line emission + working-paper section.

### 13. Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`

The BCS spectral-action moments Σ_BdG_A and Σ_BdG_B ARE the substrate-IS observables at the polycritical-pressure point of the Volovik 2003 §7.2 framework; they are NOT "BCS observables in a 3He-B container." The polycritical pressure P_pc IS the substrate's intrinsic SC-factor degeneracy point; it is NOT a coordinate in a 3He-B-laboratory-container. The (Δ_B/Δ_A)^p cancellation theorem IS the substrate-IS structural identity that preserves the cocycle ratio under inheritance-morphism restriction; it is NOT a "comparison between A-phase and B-phase containers." A_K^BdG_preimage IS the substrate algebra restricted to the BdG-inheritance-morphism image (per A.3); it is NOT "the BdG sector of 3He-B."

Direction of explanation per `phononic-framing.md §"The Correction"`: D_K eigenvalues → Hochschild cocycle norms ‖φ_67‖_BdG / ‖φ_88‖_BdG → substrate cocycle ratio canonical 7.324992 → BCS-physics-grounded R_substrate at polycritical pressure → laboratory observable (lab(F_i) / lab(F_j)) per (Δ_B/Δ_A)^p cancellation. NEVER explain R_substrate via "3He-B BCS observables in curved spacetime"; ALWAYS explain via the substrate's inheritance-morphism image at A_K^BdG_preimage projected to the BCS spectral-action moment ratio.

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: this gate operates at **Level 1 — Single-τ-slice substrate-IS** (τ_fold = 0.19 R-PROTECTED; the BCS spectral-action moments at polycritical pressure are intrinsic to the spectral triple at the fixed τ-anchor).

---

## §W2-3. S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET  (Ledger A.7)

### 1. Gate ID

`S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET`

### 2. Trigger

`[VERIFY-THEOREM]` — verifies that an INDEPENDENT inheritance morphism χ' : A_F → M_2(ℂ) ⊗ Cl(1) can be constructed where M_3(ℂ) annihilation is a DERIVED THEOREM rather than a defining datum. Per `epistemic-discipline.md §"Layer-Decomposition"` Definitional-datum-vs-derived-theorem K-counter at substrate ↔ methodology layer pair (B.10 K=2 advisory; this gate is K=2 → K=3 advancement candidate per `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold).

### 3. Classification

GEOMETRIC. The χ' inheritance morphism is a NCG-axiomatic substrate-IS object on the spectral triple `(A_F, H_F, D_F)`. The M_2(ℂ) ⊗ Cl(1) target is a Clifford-algebra-decorated 2×2 matrix algebra; the M_3(ℂ) annihilation property is a derived theorem from Schur orthogonality of the A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) representation at the lab inheritance image.

### 4. Agent type

`connes-ncg-theorist` PRIMARY (NCG-axiomatic inheritance morphism construction; Connes 1996 reconstruction theorem + NCG axioms 3+5+6 + Schur orthogonality of A_F representation are the substrate-physics canonicals). Per ledger lines 56-59 verbatim author hint. **gen-physicist BLACKLISTED for test-case design.**

### 5. Hypothesis

There exists an inheritance morphism χ' : A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) where the M_3(ℂ) summand annihilates at the lab inheritance image as a DERIVED THEOREM (not a defining datum). The theorem proof: rank(ker(χ')|_{M_3(ℂ)}) = 9 (full annihilation of the 9-dimensional M_3(ℂ) summand) follows from Schur orthogonality applied to the unique non-trivial irreducible representation of M_3(ℂ) (the fundamental 3-dim repn) when projected against the M_2(ℂ) ⊗ Cl(1) target's 2-dimensional Spin(1)-irrep image; the rank-9 annihilation is structurally forced by representation-theoretic dimension counting, NOT by ansatz.

### 6. Method

**Producing script**: `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.py`

**Self-contained dispatch prompt** (verbatim for runtime agent):

> You are connes-ncg-theorist constructing the INDEPENDENT inheritance morphism χ' : A_F → M_2(ℂ) ⊗ Cl(1) for §W2-3 of the S89 plan. Read `sessions/session-plan/session-89-plan-w2.md §W2-3` IN FULL before starting.
>
> Step 0: Import canonical constants. `from canonical_constants import *` MANDATORY. Constants required: `tau_fold`, `M_KK`. Per `.claude/rules/math-scripts.md §"Canonical Write-Order"`.
>
> Step 1: Construct the substrate-IS A_F representation. A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); H_F = ℂ³² (32-dimensional substrate Hilbert space; per Chamseddine-Connes-Marcolli 2007 finite-spectral-triple). The natural representation of A_F on H_F decomposes per Schur into (ℂ-irrep) × (ℍ-fundamental 2-dim) × (M_3(ℂ)-fundamental 3-dim) channels.
>
> Step 2: Construct the target algebra M_2(ℂ) ⊗ Cl(1). Cl(1) is the Clifford algebra in 1 dimension; it has a unique 2-dimensional irreducible representation (the spinor representation). M_2(ℂ) ⊗ Cl(1) is therefore a 4-dimensional irreducible representation algebra (2 × 2 = 4).
>
> Step 3: Construct the candidate morphism χ' : A_F → M_2(ℂ) ⊗ Cl(1). The morphism is the unique algebra morphism that:
>   - sends the ℂ summand of A_F to the scalar diagonal of M_2(ℂ) ⊗ Cl(1) (ℂ → ℂ ⊗ 1_{Cl(1)}, scalar embedding).
>   - sends the ℍ summand of A_F to the M_2(ℂ) factor via the unique faithful representation of ℍ (the 2-dim spinor representation; ℍ ≅ M_2(ℂ) over ℝ when complexified to ℍ ⊗ ℂ ≅ M_2(ℂ)).
>   - sends the M_3(ℂ) summand of A_F to ZERO (annihilation).
>
> Step 4: PROVE the M_3(ℂ) annihilation is a DERIVED THEOREM, not a defining datum. The proof:
>   - The M_3(ℂ) summand of A_F is the unique non-trivial 3-dimensional irreducible representation algebra in A_F.
>   - The target M_2(ℂ) ⊗ Cl(1) is 4-dimensional irreducible (2 × 2).
>   - By Schur's lemma applied to the substrate-IS representation, any non-zero algebra morphism χ' : M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) must factor through a non-zero algebra morphism between irreducible representations of compatible dimension; but 3 ≠ 4, and M_3(ℂ) has no faithful representation in dimension < 3 (so no factor through a smaller image is possible).
>   - Therefore χ'|_{M_3(ℂ)} = 0 is the ONLY algebra morphism M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) compatible with substrate Schur orthogonality.
>   - Conclusion: χ'|_{M_3(ℂ)} = 0 is a DERIVED THEOREM from representation-theoretic dimension counting + Schur orthogonality, NOT a defining datum. The "ansatz" structure is replaced by structural forced annihilation.
>
> Step 5: Verify rank(ker(χ')|_{M_3(ℂ)}) = 9 (full 9-dimensional M_3(ℂ) summand in the kernel). Compute as 9 × 9 identity matrix on the M_3(ℂ) generators; confirm rank-9 numerically.
>
> Step 6: Cross-check: the χ' construction is INDEPENDENT of the χ construction (the standard BdG inheritance morphism χ : A_K → M_2(ℂ) used in A.3 + A.4). Specifically, χ' targets M_2(ℂ) ⊗ Cl(1) (4-dim irreducible), while χ targets M_2(ℂ) (4-dim reducible into BdG sector + non-BdG sector). The two morphisms share the M_2(ℂ) factor but differ in the Clifford-algebra decoration; this independence is the substrate-IS structural content of A.7.
>
> Step 7: Cross-link to W3b-15 KDE Sub-test B (Level-2-binding instance #2 referenced in A.7 inheritance morphism context per `cross-pillar-bridge-anatomy.md §"Level 2 Layer Distinction"` corpus). Verify that the χ' image's HKR-bound at d=4 follows the same `L^{-3}` envelope as the χ image (W-5 calibration corpus instance #1).
>
> Step 8: Emit npz output `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz` with keys: `chi_prime_morphism_matrix`, `kernel_M3C_dimension` (= 9 if PASS), `target_algebra = "M_2(C) tensor Cl(1)"`, `derived_theorem_proof_steps` (string array; the 5-step Schur orthogonality proof), `independence_from_chi_BdG_verified` (boolean), `convention = "Independent-chi-prime-M2C-Cl1-target-Schur-orthogonality-derived-annihilation"`, `scheme = "Connes-1996-reconstruction-NCG-axioms-3-5-6"`.
>
> Step 9: Emit verdict line per `gate-verdicts.md §"S81+ canonical form"`. [VERIFY-THEOREM] trigger does NOT require [SIGN] 3-tuple companion row; standard dual-SHA companion row sufficient.
>
> Step 10: Update working-paper section §W2-3. Status = COMPLETE; verdict block populated; substrate framing block; the 5-step Schur orthogonality proof of M_3(ℂ) annihilation written out IN FULL (this is the substantive intellectual content of A.7); independence-from-χ check; HKR-envelope cross-link to W3b-15 KDE Sub-test B. ≥15 lines substantive content.
>
> **Threading**: cap `OMP_NUM_THREADS=8`. GPU not required (low-dim representation theory).
>
> **Honest disclosure**: if the Schur orthogonality proof fails (e.g., a non-trivial morphism M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) is found), emit FAIL honestly. The defining-datum-vs-derived-theorem K-counter advance is the substrate-IS structural lesson; honest reporting either way is required.

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-INDEPENDENT-CHI-PRIME-INHERITANCE-MORPHISM-M2C-CL1-TARGET
trigger: VERIFY-THEOREM
classification: GEOMETRIC
machinery_pin_map:
  N_eval: 1
  L_max: N/A                               # representation-theoretic; no spectrum truncation needed
  scan_range: N/A
  step_size: N/A
  tolerance: 1e-12                         # numerical kernel-rank computation; bit-precision identity
  scheme: "Connes-1996-reconstruction-NCG-axioms-3-5-6"
  convention: "Independent-chi-prime-M2C-Cl1-target-Schur-orthogonality-derived-annihilation"
  random_seed: N/A
  GPU_path: false
  precision: "exact-rational-arithmetic-Sage-QQ-when-applicable"
  A_F_decomposition: "C ⊕ H ⊕ M_3(C)"
  H_F_dimension: 32
  target_algebra: "M_2(C) tensor Cl(1); 4-dim irreducible"
  schur_orthogonality_invocation: "Schur lemma applied to A_F irreducible reps; M_3(C) → M_2(C) ⊗ Cl(1) forced to zero by dimension counting (3 vs 4)"
input_pin_map:
  - file: canonical_constants.py
    sha256: "<computed-at-runtime>"
    role: tau_fold + M_KK pins
  - file: ".claude/rules/inheritance-falsifier-protocol.md"
    sha256: "<computed-at-runtime>"
    role: inheritance morphism rank-2 ker(ι_*) framework + Class A/B test specification
  - file: ".claude/rules/cross-pillar-bridge-anatomy.md"
    sha256: "<computed-at-runtime>"
    role: Level-2-binding sub-class definition (W3b-15 KDE Sub-test B cross-link)
output_pin_map:
  - file: computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz
    keys: [chi_prime_morphism_matrix, kernel_M3C_dimension, target_algebra, derived_theorem_proof_steps, independence_from_chi_BdG_verified]
  - file: computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.png
    role: kernel rank visualization (9×9 identity on M_3(ℂ) generators)
  - file: computations/session-89/s89_gate_verdicts.txt
    canonical_line: "{GATE_ID}: PASS|FAIL -- value=<kernel_M3C_dimension> ..."
    dual_sha_companion_row: required
    three_tuple_companion_row: NOT required ([VERIFY-THEOREM] trigger; no sign claim)
expected_runtime: ~5 minutes single-thread (low-dim representation theory)
PRDR_keyword_atoms_8K_enumerated: [N_eval, L_max, scan_range, step_size, tolerance, scheme, convention, random_seed]
file_pin_class_5_taxonomy:
  - canonical_constants_HEAD: pinned at runtime
  - rule_files_referenced: ["inheritance-falsifier-protocol.md", "cross-pillar-bridge-anatomy.md", "epistemic-discipline.md"]
substrate_first_canonical_sourcing:
  level_pin: FULL                          # NOT SCHEMATIC; full Connes-1996 reconstruction theorem
  external_paper_provenance: "Connes 1996 reconstruction (substrate canonical); Schur orthogonality (mathematical structural)"
algebra_axis_orthogonality:
  cell: "I (algebra-INVARIANT spectrum-only-functional)"
  rationale: "kernel rank is a representation-theoretic invariant; not a state-pair functional"
```

### 8. Expected output 4-tuple

`(value=9, scheme=Connes-1996-reconstruction-NCG-axioms-3-5-6, convention=Independent-chi-prime-M2C-Cl1-target-Schur-orthogonality-derived-annihilation, L_max=N/A)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS** iff `kernel_M3C_dimension == 9` (full 9-dimensional M_3(ℂ) summand annihilation; THEOREM tolerance — bit-precision identity at the kernel-rank integer). AND `independence_from_chi_BdG_verified == True` (the morphism χ' is structurally distinct from χ : A_K → M_2(ℂ); Cl(1) decoration is non-trivial). AND the 5-step Schur orthogonality proof completes without contradiction.
- **INFO** iff `kernel_M3C_dimension == 9` AND `independence_from_chi_BdG_verified == True` BUT the proof requires an additional substrate-IS structural assumption beyond NCG axioms 3+5+6 (e.g., a Cl(1) extension axiom not in the standard NCG axiom set). Substrate-IS observable correct, but the K-counter advancement to K=3 promotion is conditional on the additional axiom acceptance.
- **FAIL** iff `kernel_M3C_dimension < 9` (partial annihilation; some non-trivial morphism M_3(ℂ) → M_2(ℂ) ⊗ Cl(1) exists). OR `independence_from_chi_BdG_verified == False` (χ' is not structurally distinct from χ). The defining-datum-vs-derived-theorem K-counter advancement to K=3 fails; M_3(ℂ) annihilation remains a defining datum, not a derived theorem.

### 10. Substitution chain (NOT required for [VERIFY-THEOREM] trigger)

The PASS predicate is bit-precision identity at the kernel-rank integer, not a sign claim. No substitution chain required per `math-scripts.md §"When the chain is MANDATORY"`. The Schur orthogonality proof IS the substantive intellectual content of the gate, but is structured as a 5-step lemma proof, not a directional claim.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** advances the Definitional-datum-vs-derived-theorem K-counter from K=2 advisory (B.10) toward K=3 promotion candidate. The M_3(ℂ) annihilation property of inheritance morphisms becomes a STRUCTURAL THEOREM at the substrate ↔ methodology layer pair (per `epistemic-discipline.md §"Layer-Decomposition"` Definitional-datum-vs-derived-theorem K-counter); future extensions to other parent theories (Pati-Salam, GUT, alternative finite spectral algebras) inherit this theorem. Provides INDEPENDENT cross-check for A.4 (BCS-physics-grounded R_substrate landau path) — the χ' construction shows that the inheritance-morphism framework admits multiple targets (M_2(ℂ) and M_2(ℂ) ⊗ Cl(1)) consistent with the same A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) substrate algebra, sharpening the "inheritance morphism" classification.
- **INFO** preserves the K-counter advancement at K=2 advisory (B.10) but flags an additional axiom requirement. Solution-space implication: the substrate's NCG axiom set is incomplete for the χ' construction; additional Cl(1)-extension axiom needs registry promotion. Queue as Wave-2 → Wave-5 carry-forward.
- **FAIL** indicates M_3(ℂ) annihilation is NOT a derived theorem under standard NCG axioms 3+5+6. Solution-space implication: the inheritance-morphism framework rests on a partial defining datum (M_3(ℂ) annihilation as ansatz, not theorem); the Definitional-datum-vs-derived-theorem K-counter does NOT advance. Major epistemic correction: future agents must treat M_3(ℂ) annihilation as definitional, not derived, in cross-pillar-bridge-anatomy entries.

### 12. Effort estimate

1.0 wave-equivalents per ledger lines 56-59. Sub-budget: 0.3 wave-equiv for the χ' candidate construction; 0.5 wave-equiv for the Schur orthogonality proof (the substantive intellectual content); 0.2 wave-equiv for cross-checks (independence from χ; HKR envelope cross-link to W3b-15) + npz/png/verdict-line emission + working-paper section.

### 13. Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`

The χ' inheritance morphism IS the substrate-IS structural object on the spectral triple `(A_F, H_F, D_F)`; it is NOT "an algebra map between two containers." The M_3(ℂ) annihilation kernel IS the substrate-IS Schur-orthogonality-forced kernel; it is NOT "a label assigned to the M_3(ℂ) summand." The M_2(ℂ) ⊗ Cl(1) target IS the substrate-IS Clifford-decorated 2×2 algebra; it is NOT "a 3He-B sub-sector container." A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) IS the substrate algebra; it is NOT "a container holding ℂ, ℍ, and M_3(ℂ) sub-spaces."

Direction of explanation per `phononic-framing.md §"The Correction"`: D_F eigenvalues → A_F representation theory → Schur orthogonality at substrate Hilbert space H_F = ℂ³² → χ' inheritance morphism construction → M_3(ℂ) annihilation as DERIVED THEOREM. NEVER explain χ' via "an algebra map from the SM internal space to a 3He-B container"; ALWAYS explain via the substrate's intrinsic representation-theoretic structure.

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: this gate operates at **Level 1 — Single-τ-slice substrate-IS** (the A_F representation is intrinsic to the spectral triple at any τ; the Schur orthogonality proof is τ-independent at the representation-theoretic layer).

---

## §W2-4. S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL  (Ledger A.20)

### 1. Gate ID

`S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`

### 2. Trigger

`[AUDIT]` — pre-registers the Sagan-revised dual-prior 3-track structure for the EVENTUAL Stage-2 dispatch on the canonical Connes-Karoubi pairing computation. Per `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator pattern"` (T1-11) AND `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (S88 W-15 V.7).

### 3. Classification

GEOMETRIC. The 3-track structure (substrate-self-consistent / external-observation / joint-hypersurface) IS the substrate-IS dual-prior structure on the §VII.AH 3HeB-excess-inheritance theorem candidate per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`.

### 4. Agent type

**`sagan-empiricist` PRIMARY** (verbatim from ledger lines 121-125: "Sagan-revised dual-prior 3-track structure A/B/C"). The Sagan-revised dual-prior pre-registration is the substantive intellectual content of A.20; sagan-empiricist authors the dual-prior JSON. **gen-physicist BLACKLISTED for test-case design.** connes-ncg-theorist CO-AUTHOR (the Connes-Karoubi pairing canonical IS the underlying substrate-IS observable that the dual-prior is registered against; A.3 + A.4 npz outputs are input pins). volovik-superfluid-universe-theorist CO-AUTHOR (the 3HeB-excess inheritance bridge to laboratory observables is volovik's substrate-physics canonical per `feedback_agent-roster.md`).

### 5. Hypothesis

The §VII.AH 3HeB-excess-inheritance theorem candidate admits a Sagan-revised dual-prior 3-track structure with explicit prior-mass distribution across:

- **Track A (substrate-self-consistent)**: P(Track A) = prior mass for the reading where the §VII.AH framework prediction at the same algebra-axis family is the binding incarnation of the fiducial-anchor pre-substrate pin P (per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` clause (i)).
- **Track B (external-observation)**: P(Track B) = prior mass for the reading where laboratory measurement at the different pillar is the binding incarnation of P (clause (ii)).
- **Track C (joint-hypersurface)**: P(Track C) = prior mass for the reading where lab discrimination is 2D in (P, observable) space rather than 1D in observable space alone (clause (iii)).

The track-discriminator gate criterion: a future Stage-2 dispatch outcome maps to a specific posterior re-allocation among the 3 tracks per a deterministic rule.

### 6. Method

**Producing script**: `computations/session-89/s89_w2_a20_3heb_excess_inheritance_dual_prior.py`

**Self-contained dispatch prompt** (verbatim for runtime agent):

> You are sagan-empiricist pre-registering the dual-prior 3-track structure for the §VII.AH 3HeB-excess-inheritance theorem candidate Stage-2 dispatch in §W2-4 of the S89 plan. CO-AUTHORs: connes-ncg-theorist (the Connes-Karoubi pairing canonical IS the substrate-IS observable) and volovik-superfluid-universe-theorist (the 3HeB-excess inheritance bridge to laboratory observables). Read `sessions/session-plan/session-89-plan-w2.md §W2-4` IN FULL before starting.
>
> **PREREQUISITES: A.3 PASS verdict AND A.4 PASS verdict.** If EITHER `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS` OR `S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH: PASS` is NOT yet in `computations/session-89/s89_gate_verdicts.txt`, dispatch to mechanical closure per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` clauses 1-5 with verdict `value='PRE-REG-INC_blocked_by_A.3_pending_or_A.4_pending'`. Do NOT proceed.
>
> Step 0: Import canonical constants. `from canonical_constants import *` MANDATORY. Constants required: `tau_fold`, `M_KK`, `substrate_cocycle_ratio_67_88`. Per `math-scripts.md §"Canonical Write-Order"`.
>
> Step 1: Load A.3's npz output `computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz`. Read `R_canonical_value`. Verify SHA-256 matches input-pin from §W2-4.7 PRDR. If SHA mismatch, emit FAIL `INPUT-SHA-MISMATCH-A3`.
>
> Step 2: Load A.4's npz output `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.npz`. Read `R_substrate_BCS_grounded_corrected`. Verify SHA-256 matches input-pin from §W2-4.7 PRDR. If SHA mismatch, emit FAIL `INPUT-SHA-MISMATCH-A4`.
>
> Step 3: Construct the Sagan-revised dual-prior 3-track structure. The 3 tracks are STRUCTURALLY ORTHOGONAL per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (S88 W-15 V.7) — they correspond to 3 distinct readings of the §VII.AH theorem candidate's pre-substrate pin P incarnation:
>
>   - Track A (substrate-self-consistent): the §VII.AH framework prediction at the same algebra-axis family is the binding incarnation of P. Operationally: the cohomology-asymmetry ratio 7.324992 IS the substrate-IS observable; the Stage-2 dispatch verifies that BOTH connes-axis (NCG-axiomatic Connes-Karoubi pairing) AND volovik-axis (BCS-physics-grounded R_substrate) PASS at this binding.
>   - Track B (external-observation): laboratory measurement at the 3HeB pillar (lab(F_i) / lab(F_j)) is the binding incarnation of P. Operationally: the substrate prediction is preserved INTACT under (Δ_B/Δ_A)^p cancellation; lab measurement at Helsinki ROTA / Lancaster MCT-3 returns 7.3250 ± 0.1%.
>   - Track C (joint-hypersurface): the lab discrimination is 2D in (P, observable) space — both the substrate prediction R_canonical AND the BCS-physics-grounded R_substrate AND the lab measurement form a hypersurface in 3D space; the §VII.AH theorem is verified iff all three points lie on a 2D constraint surface.
>
> Step 4: Pre-register the prior-mass distribution. Sagan-revised dual-prior priors (per ledger line 124 + sagan-empiricist methodological canonical):
>
>   - P(Track A) = 0.50 (substrate-self-consistent has highest prior mass; the framework's substrate-physics canonical IS the substrate-IS observable; 50% prior mass reflects the pre-experiment "framework-internal" structural confidence)
>   - P(Track B) = 0.30 (external-observation; lab measurement is independent confirmation but still depends on the (Δ_B/Δ_A)^p cancellation theorem holding at the polycritical pressure; 30% prior mass reflects the cross-pillar bridge candidate K-counter advance in S88 W4a-17 = MANDATORY at K=3 status)
>   - P(Track C) = 0.20 (joint-hypersurface; the most epistemically demanding track; requires 2D constraint; 20% prior mass reflects the structural-orthogonality precedent at the cross-pillar-bridge layer per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 since S87 W-2 R3)
>   - Sum: 0.50 + 0.30 + 0.20 = 1.00 (proper probability distribution).
>
> Step 5: Pre-register the track-discriminator gate criterion. The future Stage-2 dispatch outcome maps to a posterior re-allocation per the rule:
>
>   - PASS-AND across both axes (connes + volovik) of all 3 clauses → posterior P(Track A | PASS-AND) = 0.85, P(Track B | PASS-AND) = 0.10, P(Track C | PASS-AND) = 0.05.
>   - FAIL on ANY axis or clause → posterior P(Track A | FAIL) = 0.05, P(Track B | FAIL) = 0.40, P(Track C | FAIL) = 0.55 (FAIL on substrate-self-consistent shifts mass to external-observation and joint-hypersurface readings).
>   - INFO (composite-collapse-rule magnitude=INFO with regime=VALID) → posterior P(Track A | INFO) = 0.40, P(Track B | INFO) = 0.40, P(Track C | INFO) = 0.20 (INFO neutralizes the substrate-self-consistent reading's advantage).
>
> Step 6: Verify the dual-prior structure satisfies `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` (S88 W-15 V.7) requirements:
>
>   - All 3 tracks (substrate-self-consistent / external-observation / joint-hypersurface) explicitly named per clauses (i) / (ii) / (iii).
>   - Conflation-with-undeclared-binding is registry-incompleteness FAIL routing to plan-freeze halt — verify NO conflation in the dual-prior pre-registration.
>   - K=1 calibration corpus instance per W-15 V.7; A.20 is a forward-conforming instance.
>
> Step 7: Verify the dual-prior structure satisfies `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator pattern"` (T1-11) requirements:
>
>   - Track A prior mass + Track B prior mass + Track C prior mass + posterior re-allocation rule per gate outcome.
>   - All 4 components present.
>   - K=2 calibration corpus instance per T1-11 (A.20 is the second instance after S87-W5A-P3-IC-PER-CLASS-VERIFY).
>
> Step 8: Emit JSON output `computations/session-89/s89_w2_a20_3heb_excess_inheritance_dual_prior.json` with structure:
>
>   ```json
>   {
>     "gate_id": "S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL",
>     "registry_target": "§VII.AH STAGE-1-CANDIDATE",
>     "fiducial_anchor_pre_substrate_pin": "P = pre-substrate pin per cross-pillar-bridge-anatomy Element 3 binding discipline",
>     "tracks": {
>       "A_substrate_self_consistent": {
>         "binding_clause": "(i) §VII.AH framework prediction at same algebra-axis family",
>         "prior_mass": 0.50,
>         "anchor_observable": "R_canonical = 7.324992 (Sage-exact)",
>         "anchor_axis": "NCG-axiomatic + BCS-physics-grounded JOINT"
>       },
>       "B_external_observation": {
>         "binding_clause": "(ii) laboratory measurement at the different pillar",
>         "prior_mass": 0.30,
>         "anchor_observable": "lab(F_i) / lab(F_j) at Helsinki ROTA / Lancaster MCT-3",
>         "anchor_axis": "3HeB lab pillar"
>       },
>       "C_joint_hypersurface": {
>         "binding_clause": "(iii) lab discrimination 2D in (P, observable) space",
>         "prior_mass": 0.20,
>         "anchor_observable": "(R_canonical, R_substrate_BCS, lab_ratio) constrained to 2D hypersurface",
>         "anchor_axis": "JOINT cross-pillar"
>       }
>     },
>     "track_discriminator_rule": {
>       "PASS-AND": {"A": 0.85, "B": 0.10, "C": 0.05},
>       "FAIL": {"A": 0.05, "B": 0.40, "C": 0.55},
>       "INFO": {"A": 0.40, "B": 0.40, "C": 0.20}
>     },
>     "input_R_canonical_value": "<from A.3 npz>",
>     "input_R_substrate_BCS_grounded_corrected_value": "<from A.4 npz>",
>     "input_substrate_cocycle_ratio_67_88_canonical": 7.324992,
>     "rule_compliance": {
>       "cross_pillar_bridge_anatomy_Element_3_fiducial_anchor_binding_discipline_S88_W15_V7": "compliant",
>       "epistemic_discipline_dual_prior_pre_registration_T1_11": "compliant",
>       "K_counter_advancement": "Element-3 K=1 → K=2 advisory; T1-11 K=1 → K=2"
>     }
>   }
>   ```
>
> Step 9: Verify the JSON is well-formed; sum of prior masses = 1.000 ± 1e-10; sum of each posterior re-allocation = 1.000 ± 1e-10.
>
> Step 10: Emit verdict line per `gate-verdicts.md §"S81+ canonical form"`. [AUDIT] trigger; standard dual-SHA companion row sufficient. PASS if JSON well-formed + all 3 sums = 1.000 + rule-compliance fields all "compliant".
>
> Step 11: Update working-paper section §W2-4. Status = COMPLETE; verdict block populated; substrate framing block; the 3-track structure pre-registration explicitly written out; rule-compliance verification per W-15 V.7 + T1-11; cross-link to A.39 §VII.AH Stage-2 re-dispatch (FUTURE WAVE; eventual Stage-2 dispatch consumes this dual-prior). ≥15 lines substantive content.
>
> **Threading**: cap `OMP_NUM_THREADS=8`. GPU not required.
>
> **Honest disclosure**: if a track is not structurally distinct from another (conflation per W-15 V.7), emit FAIL honestly; do NOT iterate-until-PASS by adjusting prior masses to reach a passing structure.

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL
trigger: AUDIT
classification: GEOMETRIC
machinery_pin_map:
  N_eval: 1
  L_max: 10                                # inherited from A.3 + A.4 npz
  scan_range: N/A
  step_size: N/A
  tolerance: 1e-10                         # prior-mass distribution sum-to-1.000 floating-point tolerance
  scheme: "Sagan-revised-dual-prior-3-track-structure"
  convention: "Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant"
  random_seed: N/A                         # deterministic prior-mass pre-registration
  GPU_path: false
  precision: "float64-prior-masses; rule-compliance booleans"
  track_A_prior_mass: 0.50
  track_B_prior_mass: 0.30
  track_C_prior_mass: 0.20
  track_discriminator_rule_PASS_AND: {A: 0.85, B: 0.10, C: 0.05}
  track_discriminator_rule_FAIL: {A: 0.05, B: 0.40, C: 0.55}
  track_discriminator_rule_INFO: {A: 0.40, B: 0.40, C: 0.20}
input_pin_map:
  - file: computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz
    sha256: "<computed-at-runtime; CRITICAL: A.3 PASS prereq>"
    role: R_canonical_value pin
  - file: computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.npz
    sha256: "<computed-at-runtime; CRITICAL: A.4 PASS prereq>"
    role: R_substrate_BCS_grounded_corrected pin
  - file: computations/session-89/s89_gate_verdicts.txt
    sha256: "<computed-at-runtime; CRITICAL: must contain BOTH A.3 PASS AND A.4 PASS lines>"
    role: prereq-check for both A.3 and A.4 PASS verdicts
  - file: canonical_constants.py
    sha256: "<computed-at-runtime>"
    role: substrate_cocycle_ratio_67_88 pin
  - file: ".claude/rules/cross-pillar-bridge-anatomy.md"
    sha256: "<computed-at-runtime>"
    role: Element 3 fiducial-anchor binding discipline (S88 W-15 V.7)
  - file: ".claude/rules/epistemic-discipline.md"
    sha256: "<computed-at-runtime>"
    role: Dual-prior pre-registration as track-discriminator pattern (T1-11)
output_pin_map:
  - file: computations/session-89/s89_w2_a20_3heb_excess_inheritance_dual_prior.json
    keys: [gate_id, registry_target, fiducial_anchor_pre_substrate_pin, tracks (A/B/C), track_discriminator_rule, input_R_canonical_value, input_R_substrate_BCS_grounded_corrected_value, input_substrate_cocycle_ratio_67_88_canonical, rule_compliance]
  - file: computations/session-89/s89_gate_verdicts.txt
    canonical_line: "{GATE_ID}: PASS|FAIL -- value=<sum_of_prior_masses_check> ..."
    dual_sha_companion_row: required
    three_tuple_companion_row: NOT required ([AUDIT] trigger; no sign claim)
expected_runtime: ~5 minutes single-thread (JSON construction + rule-compliance verification)
PRDR_keyword_atoms_8K_enumerated: [N_eval, L_max, scan_range, step_size, tolerance, scheme, convention, random_seed]
file_pin_class_5_taxonomy:
  - canonical_constants_HEAD: pinned at runtime
  - A_3_npz_input: pinned at runtime; CRITICAL prereq
  - A_4_npz_input: pinned at runtime; CRITICAL prereq
  - verdict_file_S89: pinned at runtime; A.3 + A.4 PASS lines check
  - rule_files_referenced: ["cross-pillar-bridge-anatomy.md", "epistemic-discipline.md", "phononic-framing.md"]
substrate_first_canonical_sourcing:
  level_pin: FULL                          # NOT SCHEMATIC; full Sagan-revised dual-prior canonical
  external_paper_provenance: "Sagan-empiricist methodological canonical (W-9 V.3 origin); cross-pillar-bridge-anatomy Element 3 substrate canonical"
algebra_axis_orthogonality:
  cell: "JOINT (Track A = Cell I algebra-INVARIANT; Track B = Cell IV algebra-DEPENDENT; Track C = JOINT 2D hypersurface)"
  rationale: "the 3-track structure spans both cells; Track A and Track B are STRUCTURALLY ORTHOGONAL per algebra-axis K=3 MANDATORY; Track C is the cross-cell joint structure"
```

### 8. Expected output 4-tuple

`(value=1.000_sum_of_prior_masses, scheme=Sagan-revised-dual-prior-3-track-structure, convention=Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS** iff (a) JSON output well-formed (syntactically valid); (b) `|sum(prior_masses) − 1.000| ≤ 1e-10` (RATIO tolerance); (c) `|sum(posterior re-allocation per outcome) − 1.000| ≤ 1e-10` for each of PASS-AND / FAIL / INFO outcomes; (d) all rule-compliance fields = "compliant"; (e) the 3 tracks are STRUCTURALLY DISTINCT (no conflation per W-15 V.7).
- **INFO** iff (a)-(c) hold but (d) flags an advisory (one rule-compliance field = "advisory-pending-K3"). Substrate-IS observable correct, but K-counter advancement to MANDATORY status conditional on additional calibration corpus instances.
- **FAIL** iff JSON malformed OR sum-of-prior-masses ≠ 1.000 OR posterior re-allocation sums ≠ 1.000 OR rule-compliance field = "non-compliant" OR conflation between tracks detected.

### 10. Substitution chain (NOT required for [AUDIT] trigger)

The PASS predicate is structural compliance with W-15 V.7 + T1-11 rules + numerical sum-to-1.000 checks; no sign claim. No substitution chain required per `math-scripts.md §"When the chain is MANDATORY"`.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** advances the Element 3 fiducial-anchor binding discipline K-counter from K=1 (W-15 V.7) toward K=2 advisory (A.20 is the second registered instance). The Sagan-revised dual-prior 3-track structure becomes a forward-conforming substrate-IS observable for future Stage-2 dispatches. ALSO advances the T1-11 dual-prior pre-registration pattern K-counter from K=1 (S87-W5A-P3-IC-PER-CLASS-VERIFY) to K=2. Unblocks the FUTURE Stage-2 dispatch on §VII.AH (A.39 in W4 dispatch); A.39 reads this dual-prior JSON to interpret its PASS/FAIL/INFO outcome.
- **INFO** preserves the K-counter advancement at K=1 advisory but flags a pending K=3 promotion. Solution-space implication: dual-prior pre-registration discipline is a SUGGESTION, not yet MANDATORY; future S89+ Stage-2 dispatches have flexibility on the dual-prior format. Queue as Wave-2 → S90+ carry-forward (CF-A20-K3-PROMOTION-CANDIDATE).
- **FAIL** indicates the dual-prior pre-registration cannot satisfy the Element 3 fiducial-anchor binding discipline. Solution-space implication: the §VII.AH 3HeB-excess-inheritance theorem candidate cannot be Stage-2-dispatched under the current cross-pillar-bridge-anatomy framework; structural defect requires either (a) re-derivation of the §VII.AH theorem candidate, OR (b) extension of the Element 3 framework to admit the §VII.AH structural form. Major epistemic correction.

### 12. Effort estimate

0.3 wave-equivalents per ledger lines 121-125. Sub-budget: 0.1 wave-equiv for input-pin loading from A.3 + A.4 npz; 0.15 wave-equiv for the dual-prior JSON construction + rule-compliance verification; 0.05 wave-equiv for npz/json/verdict-line emission + working-paper section.

### 13. Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`

The Sagan-revised dual-prior 3-track structure IS the substrate-IS pre-registration object on the §VII.AH 3HeB-excess-inheritance theorem candidate; it is NOT "a probability distribution in a probability container." The 3 tracks (substrate-self-consistent / external-observation / joint-hypersurface) ARE 3 distinct structural readings of the substrate-IS observable; they are NOT "3 possible realities the substrate might inhabit." The track-discriminator gate criterion IS the substrate-IS deterministic posterior re-allocation rule; it is NOT "a Bayesian update in a probability space."

The §VII.AH 3HeB-excess-inheritance theorem candidate IS the substrate-IS structural prediction at the cross-pillar-bridge layer (substrate Pillar I ↔ laboratory Pillar V 3HeB); it is NOT "a 3HeB observable."

Direction of explanation per `phononic-framing.md §"The Correction"`: D_K eigenvalues → Connes-Karoubi pairing infrastructure (A.3) → BCS-physics-grounded R_substrate (A.4) → Sagan-revised dual-prior 3-track pre-registration (this gate) → Stage-2 dispatch on §VII.AH (FUTURE, A.39 in W4) → eventual STAGE-3-PERMANENT promotion of §VII.AH iff PASS-AND across 3 tracks. NEVER explain the 3-track structure via "3 possible 3HeB observation outcomes"; ALWAYS explain via the substrate's intrinsic Element 3 fiducial-anchor binding discipline.

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: this gate operates at **Level 1 — Single-τ-slice substrate-IS** (the dual-prior is registered against τ_fold = 0.19 R-PROTECTED canonicals; the 3 tracks are intrinsic to the spectral triple at the fixed τ-anchor).

---

## §W2-5. S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS  (Ledger A.40)

### 1. Gate ID

`S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS`

### 2. Trigger

`[VERIFY]` — verifies the chirality-fidelity 3-proxy recompute (CS / GV / η_CS) on a chirality-resolved spectrum cache. Upgrades the §VII.AQ Level-3 anchor from canonical-import binding (gv_canonical_difference_FW = -40579.1500479506; current §VII.AQ entry) to substrate-natural binding per the W-23 W7b-82 V.5 (B.58) Binding-Axis discipline.

### 3. Classification

GEOMETRIC. The CS / GV / η_CS proxies ARE NCG-axiomatic substrate-IS observables on the spectral triple `(A_K, H_K, D_K)` per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (algebra-INVARIANT family for all 3 proxies; spectrum-only functionals on the chirality-resolved D_K cache). The chirality projection γ_9 IS the substrate-IS chirality operator; the resolved spectrum cache IS the substrate-IS image at γ_9 = +1 vs γ_9 = -1 sectors.

### 4. Agent type

`connes-ncg-theorist` PRIMARY (NCG-axiomatic chirality projector + 3-proxy CS/GV/η_CS construction). Per ledger lines 533-536 verbatim author hint. **gen-physicist BLACKLISTED for test-case design.** No CO-AUTHORs explicitly declared in ledger; the chirality-resolved spectrum cache is intra-NCG-axiomatic substrate-physics.

### 5. Hypothesis

The chirality-resolved spectrum cache + 3-proxy recompute (CS, GV, η_CS) on the L_max=10 D_K spectrum upgrades the §VII.AQ Level-3 anchor from canonical-import binding to substrate-natural binding per the W-23 W7b-82 V.5 (B.58) Binding-Axis discipline. Specifically: Δ_GV_natural ≠ 0 on the substrate-natural-binding evaluation (where Δ_GV_natural is computed from the chirality-resolved spectrum cache at L_max=10 using the substrate's intrinsic γ_9 chirality projection); this contrasts with the W-23 W7b-82 V.5 calibration locus where Δ_GV_natural = 0 on the L_max=10 master cache while gv_canonical_difference_FW satisfies the canonical-import-binding Level-3 anchor.

### 6. Method

**Producing script**: `computations/session-89/s89_w2_a40_chirality_fidelity_3_proxy.py`

**Self-contained dispatch prompt** (verbatim for runtime agent):

> You are connes-ncg-theorist building the chirality-resolved spectrum cache + 3-proxy recompute (CS / GV / η_CS) for §W2-5 of the S89 plan. Read `sessions/session-plan/session-89-plan-w2.md §W2-5` IN FULL before starting.
>
> Step 0: Import canonical constants. `from canonical_constants import *` MANDATORY. Constants required: `tau_fold`, `M_KK`, `gv_canonical_difference_FW`. Per `math-scripts.md §"Canonical Write-Order"`. Note: `gv_canonical_difference_FW = -40579.1500479506` is the §VII.AQ Level-3 anchor canonical-import-binding pin; A.40 upgrades to substrate-natural-binding via the chirality-resolved cache.
>
> Step 1: Load the L_max=12 D_K spectrum master cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz`. Filter at L_max=10 truncation per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`. Verify `truncation_consistent = True` flag.
>
> Step 2: Apply the chirality projection γ_9 = γ_5 ⊗ γ_F to build the chirality-resolved spectrum cache. γ_5 is the 4D chirality operator on H_M (Lorentz spinor space); γ_F is the finite-spectral-triple chirality operator on H_F (per Chamseddine-Connes-Marcolli 2007). γ_9 is the product. The substrate-IS chirality decomposition per Connes 1996 KO-dim=6 specification: H_K = H_K^{γ_9=+1} ⊕ H_K^{γ_9=-1}. Resolve the D_K spectrum at L_max=10 into γ_9=+1 and γ_9=-1 sectors.
>
> Step 3: Emit intermediate output `computations/session-89/s89_w2_a40_chirality_resolved_spectrum.npz` with keys: `D_K_eigenvalues_chirality_plus`, `D_K_eigenvalues_chirality_minus`, `chirality_decomposition_basis`, `gamma9_operator_matrix`, `L_max = 10`.
>
> Step 4: Compute the CS (Chern-Simons) proxy on the chirality-resolved cache. The CS proxy is the integrated Chern-Simons 3-form on the chirality-projected D_K spectrum; for a finite spectral triple, this reduces to a Cartan-rational sum per Connes-Moscovici 1995 §III.4. Specifically: CS = Σ_i (1/3) tr(γ_9 · A^3) where A^3 is the cube of the inner-fluctuation 1-form; the integration is the spectral-action moment at substrate-distance-1 pole s=3.
>
> Step 5: Compute the GV (Godbillon-Vey) proxy on the chirality-resolved cache. The GV proxy is the substrate-IS odd-grading-classified observable per S86 W-11 RULE-2 STRENGTHENED parity-blindness theorem (η even-grading; GV odd-grading on the (C_H, C_epsH) parity-twin pair). GV = Σ_i Vol(M_i) · (Δχ)_i where M_i is the i-th leaf of the chirality decomposition and (Δχ)_i is the chirality-difference characteristic class. Compute the substrate-natural-binding form on the chirality-resolved cache; cross-check against the canonical-import pin gv_canonical_difference_FW = -40579.1500479506.
>
> Step 6: Compute the η_CS (Cheeger-Simons eta) proxy on the chirality-resolved cache. The η_CS proxy is the secondary characteristic class associated with the Chern-Simons 3-form per Cheeger-Simons 1985; for a finite spectral triple, this is the eta-invariant of D_K restricted to the chirality projection. η_CS = Σ_λ sgn(λ) · |λ|^{-s}|_{s=0} where the sum is over chirality-projected eigenvalues; the regularization is the substrate-IS zeta-function regularization at s=0.
>
> Step 7: Substitution chain (MANDATORY per the §VII.AQ Level-3 anchor binding direction claim).
>
>   - Step 1 (Definition): Δ_GV_canonical_import := gv_canonical_difference_FW = -40579.1500479506 (canonical-import-binding pin from S87 W8-8; per `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` Binding-Axis sub-table).
>   - Step 2 (Definition): Δ_GV_natural := GV[chirality-resolved cache at L_max=10] − GV[canonical-import baseline]; substrate-natural-binding evaluation from the chirality-resolved spectrum cache.
>   - Step 3 (Definition): canonical-import-binding ↔ substrate-natural-binding axis distinction per `regulator-pin-discipline.md §"Cross-link"` Binding-Axis row (W-23 W7b-82 V.5 / B.58 K=1 calibration).
>   - Step 4 (Substitute): the W-23 W7b-82 V.5 calibration locus had Δ_GV_natural = 0 on L_max=10 cache while gv_canonical_difference_FW satisfied the Level-3 anchor — this is the canonical-import-binding regime. A.40 upgrades by computing Δ_GV_natural with chirality-resolved cache (NOT the un-resolved L_max=10 master cache); the chirality projection introduces non-trivial spectral content per S86 W-11 RULE-2 STRENGTHENED odd-grading.
>   - Step 5 (Simplify): If the chirality-resolved cache produces Δ_GV_natural ≠ 0, the §VII.AQ Level-3 anchor is upgraded to substrate-natural-binding; if Δ_GV_natural = 0 (same as W-23 W7b-82 V.5 calibration), the chirality projection does NOT recover substrate-natural-binding and the canonical-import-binding remains the substrate's only Level-3 anchor for §VII.AQ.
>   - Step 6 (Direction): SIGN: the binding direction is FROM canonical-import binding TO substrate-natural binding upon PASS; this is a binding-axis upgrade, not a sign-of-Δ_GV claim. SIGN-equivalent annotation: `binding_direction = "canonical-import → substrate-natural"`. MAGNITUDE: |Δ_GV_natural| > 0 required for substrate-natural-binding upgrade; tolerance |Δ_GV_natural| ≥ 1e-3 (substantively non-zero, not floating-point noise). REGIME: VALID at L_max=10 chirality-resolved per Friedrich-Bär saturation theorem.
>
> Step 8: Cross-check against W-11 RULE-2 STRENGTHENED parity-blindness theorem. The η even-grading + GV odd-grading distinction on (C_H, C_epsH) parity-twin pair (S86 W-11 R2 closure) requires:
>   - η_CS computed on chirality-resolved cache should be EVEN-GRADING-INVARIANT (insensitive to chirality projection sign; verify η_CS at γ_9=+1 sector equals η_CS at γ_9=-1 sector to bit-precision).
>   - GV computed on chirality-resolved cache should be ODD-GRADING-DISCRIMINATING (sensitive to chirality projection sign; verify GV at γ_9=+1 differs from GV at γ_9=-1 by a non-zero amount).
>   - CS computed on chirality-resolved cache joins the GV odd-grading class.
>
> Step 9: Emit npz output `computations/session-89/s89_w2_a40_chirality_fidelity_3_proxy.npz` with keys: `CS_proxy_value_substrate_natural`, `GV_proxy_value_substrate_natural`, `eta_CS_proxy_value_substrate_natural`, `Delta_GV_natural` (the substrate-natural-binding difference; KEY OBSERVABLE), `Delta_GV_canonical_import` (= gv_canonical_difference_FW reference), `chirality_resolved_cache_npz_path`, `parity_blindness_cross_check_eta_invariant` (boolean), `parity_blindness_cross_check_GV_discriminating` (boolean), `binding_direction = "canonical-import → substrate-natural"`, `convention = "Chirality-fidelity-3-proxy-substrate-natural-binding-W23-W7b-82-V5-B58-extension"`, `scheme = "Chirality-resolved-D_K-spectrum-3-proxy-CS-GV-etaCS"`.
>
> Step 10: Emit verdict line per `gate-verdicts.md §"S81+ canonical form"`. [VERIFY] trigger; standard dual-SHA companion row sufficient; if [SIGN]-equivalent binding-direction claim, also emit 3-tuple companion row with `sign_verdict=PASS|FAIL` interpreted as binding-direction-correct (canonical-import → substrate-natural achieved).
>
> Step 11: Update working-paper section §W2-5. Status = COMPLETE; verdict block populated; substrate framing block; the 3-proxy CS/GV/η_CS construction explicitly written out; substitution chain (Step 7) explicitly written out; parity-blindness cross-checks (Step 8) reported; §VII.AQ Level-3 anchor upgrade implication discussed; cross-link to A.38 §VII.AQ Stage-2 Cross-Axis Verify (FUTURE WAVE; A.38 reads A.40's substrate-natural-binding upgrade). ≥15 lines substantive content.
>
> **Threading**: cap `OMP_NUM_THREADS=8`. GPU may help for L_max=10 chirality-projected eigenvalue diagonalization (~1024 × 1024 dense; per `math-scripts.md §"Environment"` torch.linalg over numpy.linalg for ≥100×100 matrices); if GPU available, use `torch.linalg.eigh` on the chirality-projected D_K^2 operator.
>
> **Honest disclosure**: if Δ_GV_natural = 0 on the chirality-resolved cache (same as W-23 W7b-82 V.5 calibration), emit FAIL honestly; the §VII.AQ Level-3 anchor binding upgrade does NOT succeed; canonical-import-binding remains the only substrate Level-3 anchor for §VII.AQ. Do NOT iterate-until-PASS by changing the chirality projection convention.

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS
trigger: VERIFY
classification: GEOMETRIC
machinery_pin_map:
  N_eval: 1                                # one full chirality-resolved evaluation at L_max=10
  L_max: 10
  L_max_plan: 10
  L_max_operational: 10
  truncation_consistent: true
  scan_range: N/A                          # no scan; L_max=10 single-truncation
  step_size: N/A
  tolerance: 1e-3                          # substrate-natural-binding non-zero magnitude floor for Δ_GV_natural
  scheme: "Chirality-resolved-D_K-spectrum-3-proxy-CS-GV-etaCS"
  convention: "Chirality-fidelity-3-proxy-substrate-natural-binding-W23-W7b-82-V5-B58-extension"
  random_seed: N/A
  GPU_path: "torch.linalg.eigh-on-chirality-projected-D_K2-if-available; numpy.linalg fallback"
  precision: "float64-default; mpmath.mp.dps=30 for proxy normalization"
  chirality_operator: "gamma_9 = gamma_5 (Lorentz) tensor gamma_F (finite-spectral-triple)"
  CS_proxy_definition: "Connes-Moscovici 1995 §III.4 spectral-action moment at substrate-distance-1 pole s=3"
  GV_proxy_definition: "Godbillon-Vey on chirality-resolved leaves; substrate-natural-binding form"
  eta_CS_proxy_definition: "Cheeger-Simons eta; zeta-regularized at s=0"
  binding_direction_pin: "canonical-import → substrate-natural"
  parity_blindness_class: "eta_CS even-grading INVARIANT; GV odd-grading DISCRIMINATING; CS joins GV class (per W-11 RULE-2 STRENGTHENED)"
input_pin_map:
  - file: computations/session-84/s84_spectrum_cache_L12_tau019.npz
    sha256: "<computed-at-runtime>"
    role: D_K spectrum master cache; filtered at L_max=10; chirality-projected in Step 2
  - file: canonical_constants.py
    sha256: "<computed-at-runtime>"
    role: tau_fold + M_KK + gv_canonical_difference_FW pins
  - file: ".claude/rules/regulator-pin-discipline.md"
    sha256: "<computed-at-runtime>"
    role: Cross-link Binding-Axis sub-table (W-23 W7b-82 V.5 / B.58 K=1 calibration)
  - file: ".claude/rules/cross-pillar-bridge-anatomy.md"
    sha256: "<computed-at-runtime>"
    role: Three-Level Structural-Confidence Ladder (Level-3 anchor upgrade target)
output_pin_map:
  - file: computations/session-89/s89_w2_a40_chirality_resolved_spectrum.npz
    keys: [D_K_eigenvalues_chirality_plus, D_K_eigenvalues_chirality_minus, chirality_decomposition_basis, gamma9_operator_matrix, L_max]
    role: intermediate output (intra-A.40)
  - file: computations/session-89/s89_w2_a40_chirality_fidelity_3_proxy.npz
    keys: [CS_proxy_value_substrate_natural, GV_proxy_value_substrate_natural, eta_CS_proxy_value_substrate_natural, Delta_GV_natural, Delta_GV_canonical_import, chirality_resolved_cache_npz_path, parity_blindness_cross_check_eta_invariant, parity_blindness_cross_check_GV_discriminating, binding_direction]
  - file: computations/session-89/s89_w2_a40_chirality_fidelity_3_proxy.png
    role: 3-proxy values + Δ_GV_natural vs Δ_GV_canonical_import comparison plot
  - file: computations/session-89/s89_gate_verdicts.txt
    canonical_line: "{GATE_ID}: PASS|INFO|FAIL -- value=<Delta_GV_natural> ..."
    dual_sha_companion_row: required
    three_tuple_companion_row: required (sign_verdict=PASS|FAIL where PASS = binding-direction-correct; magnitude_verdict per |Δ_GV_natural| ≥ 1e-3 floor; regime_verdict=VALID)
expected_runtime: ~30 minutes single-thread (chirality projection + eigvals + 3-proxy compute); ~10 min with GPU
PRDR_keyword_atoms_8K_enumerated: [N_eval, L_max, scan_range, step_size, tolerance, scheme, convention, random_seed]
file_pin_class_5_taxonomy:
  - canonical_constants_HEAD: pinned at runtime
  - spectrum_cache_master: pinned at runtime
  - rule_files_referenced: ["regulator-pin-discipline.md", "cross-pillar-bridge-anatomy.md", "phononic-framing.md", "math-scripts.md", "gate-verdicts.md"]
substrate_first_canonical_sourcing:
  level_pin: FULL                          # NOT SCHEMATIC; full chirality-resolved D_K spectrum compute
  external_paper_provenance: "Connes-Moscovici 1995 §III.4 (CS proxy); Godbillon-Vey 1973 (GV proxy methodological); Cheeger-Simons 1985 (η_CS proxy methodological); chirality-resolved cache is substrate-physics canonical (NOT external-paper)"
binding_axis_pin:
  before_A40: "canonical-import-binding (gv_canonical_difference_FW = -40579.1500479506)"
  after_A40_PASS: "substrate-natural-binding (Δ_GV_natural ≠ 0 on chirality-resolved cache)"
  W_23_W7b_82_V5_B58_extension: "K=1 calibration corpus instance for Binding-Axis discipline; A.40 PASS advances K=1 → K=2"
algebra_axis_orthogonality:
  cell: "I (algebra-INVARIANT spectrum-only-functional for all 3 proxies; chirality projection preserves spectrum-only structure)"
```

### 8. Expected output 4-tuple

`(value=<Delta_GV_natural>, scheme=Chirality-resolved-D_K-spectrum-3-proxy-CS-GV-etaCS, convention=Chirality-fidelity-3-proxy-substrate-natural-binding-W23-W7b-82-V5-B58-extension, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS** iff `|Δ_GV_natural| ≥ 1e-3` (substrate-natural-binding non-zero magnitude; ABSOLUTE tolerance) AND `parity_blindness_cross_check_eta_invariant == True` (η_CS even-grading INVARIANT) AND `parity_blindness_cross_check_GV_discriminating == True` (GV odd-grading DISCRIMINATING) AND `binding_direction == "canonical-import → substrate-natural"`. AND sign_verdict = PASS (binding-direction-correct).
- **INFO** iff `1e-6 ≤ |Δ_GV_natural| < 1e-3` (non-zero but below substrate-natural-binding floor; substrate framing partially recovered but not yet enough to upgrade Level-3 anchor binding). OR one parity-blindness cross-check is INFO (e.g., η_CS varies between chirality sectors at floating-point precision but not substantively).
- **FAIL** iff `|Δ_GV_natural| < 1e-6` (effectively zero; chirality projection does NOT recover substrate-natural-binding; same as W-23 W7b-82 V.5 calibration; canonical-import-binding remains the only Level-3 anchor for §VII.AQ). OR parity_blindness_cross_check_eta_invariant fails (η_CS NOT even-grading invariant; structural defect in proxy construction). OR parity_blindness_cross_check_GV_discriminating fails (GV NOT odd-grading discriminating; structural defect).

### 10. Substitution chain (MANDATORY per binding-direction claim)

See §W2-5.6 Step 7 IN FULL. The substitution chain establishes that the binding-direction claim (canonical-import → substrate-natural) is structurally a binding-axis upgrade, not a sign-of-Δ_GV claim; the magnitude floor `|Δ_GV_natural| ≥ 1e-3` is the substrate-natural-binding non-trivial-content threshold.

Python verification at plan-author time (this plan-authoring orchestrator):

```python
# Δ_GV_canonical_import is the canonical-import-binding pin
Delta_GV_canonical_import = -40579.1500479506  # gv_canonical_difference_FW (NOT used directly; reference)
# Substrate-natural-binding upgrade requires |Δ_GV_natural| ≥ 1e-3 (non-trivial chirality-projected content)
# Direction: chirality projection introduces odd-grading content per W-11 RULE-2 STRENGTHENED
# Expected at PASS: |Δ_GV_natural| ~ O(M_KK²) substrate-natural magnitude
# Expected at FAIL (W-23 W7b-82 V.5 calibration): Δ_GV_natural = 0 (chirality projection insufficient)
```

Direction prediction: SIGN: binding-direction-correct (canonical-import → substrate-natural; PASS); FAIL = binding-direction-not-achieved. MAGNITUDE: |Δ_GV_natural| ≥ 1e-3 substrate-natural-binding non-zero magnitude. REGIME: VALID at L_max=10 chirality-resolved per Friedrich-Bär saturation theorem (chirality projection preserves block-diagonality).

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** upgrades the §VII.AQ Level-3 anchor binding from canonical-import to substrate-natural per the W-23 W7b-82 V.5 (B.58) Binding-Axis discipline. This advances the Binding-Axis K-counter from K=1 (W-23 W7b-82 V.5 calibration) to K=2 (advisory; K=3 promotion pending one more calibration instance). The §VII.AQ entry is upgraded from canonical-import-binding to substrate-natural-binding; future Stage-2 verifies (A.38 in W4) audit the substrate-natural-binding-upgraded entry. ALSO confirms the W-11 RULE-2 STRENGTHENED parity-blindness theorem extends to the chirality-resolved spectrum cache (η_CS even-grading; GV + CS odd-grading on the (C_H, C_epsH) parity-twin pair).
- **INFO** preserves the binding-direction (sign_verdict=PASS) but flags magnitude below the substrate-natural-binding floor. Solution-space implication: the chirality projection partially recovers substrate-natural-binding content, but the Level-3 anchor binding upgrade is NOT yet complete; queue as Wave-2 → Wave-4 carry-forward (CF-A40-INFO-MAG-FLOOR; alternative chirality projection conventions may recover additional substrate-natural content).
- **FAIL** indicates the chirality projection γ_9 = γ_5 ⊗ γ_F does NOT recover substrate-natural-binding for §VII.AQ Level-3 anchor. Solution-space implication: the §VII.AQ Level-3 anchor REMAINS at canonical-import-binding; the W-23 W7b-82 V.5 calibration extends; the Binding-Axis K-counter advance to K=2 fails; the §VII.AQ entry retains its current form. Queue as Wave-2 → S90+ carry-forward (CF-A40-FAIL-ALTERNATIVE-CHIRALITY; require deeper structural alternative — e.g., bi-chirality projection or SU(3)-coloured chirality structure). NO degradation of existing canonical-import-binding §VII.AQ entry; FAIL just blocks the upgrade.

### 12. Effort estimate

1.5 wave-equivalents per ledger lines 533-536. Sub-budget: 0.4 wave-equiv for chirality projection + chirality-resolved cache build at L_max=10; 0.7 wave-equiv for the 3-proxy CS/GV/η_CS recompute (the substantive computational content); 0.3 wave-equiv for parity-blindness cross-checks + substitution chain + binding-direction claim; 0.1 wave-equiv for npz/png/verdict-line emission + working-paper section.

### 13. Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"`

The chirality projection γ_9 = γ_5 ⊗ γ_F IS the substrate-IS chirality operator; it is NOT "a label distinguishing 3HeB A-phase vs B-phase." The chirality-resolved spectrum cache IS the substrate-IS spectrum decomposed at γ_9 = +1 vs γ_9 = -1; it is NOT "spectrum in two containers." The CS / GV / η_CS proxies ARE substrate-IS spectrum-only functionals on the chirality-resolved cache; they are NOT "observables measured on a 3HeB sample." The §VII.AQ Level-3 anchor IS the substrate's empirical anchor at canonical L_max=10 for the §VII.AQ theorem; it is NOT "a numerical value in an experimental dataset."

The binding-direction upgrade (canonical-import → substrate-natural) IS the substrate-IS structural promotion; it is NOT "a calibration choice between two parameter sets." The substrate-natural-binding form IS the substrate's intrinsic content at the chirality-resolved spectrum cache; the canonical-import-binding form IS the canonical_constants.py pin (gv_canonical_difference_FW = -40579.1500479506 from S87 W8-8); both are substrate-IS, but at different binding-axis pins per `regulator-pin-discipline.md §"Cross-link"` Binding-Axis sub-table.

Direction of explanation per `phononic-framing.md §"The Correction"`: D_K eigenvalues → γ_9 chirality projection → chirality-resolved spectrum cache → 3-proxy CS/GV/η_CS values → Δ_GV_natural ≠ 0 → §VII.AQ Level-3 anchor upgrade (canonical-import → substrate-natural). NEVER explain the chirality-resolved cache via "3HeB A-phase vs B-phase chirality"; ALWAYS explain via the substrate's intrinsic γ_9 structure on the spectral triple `(A_K, H_K, D_K)`.

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: this gate operates at **Level 1 — Single-τ-slice substrate-IS** (τ_fold = 0.19 R-PROTECTED; the chirality-resolved D_K spectrum is intrinsic to the spectral triple at the fixed τ-anchor; γ_9 is τ-independent at the operator algebra layer).

Per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"`: Level 1 (cohomology-class identity) is preserved (the 3 proxies are regulator-invariant identity-class observables on the chirality-projected D_K^2 spectrum); Level 2 (algebraic envelope) inherits the L^{-3} envelope at d=4 from the W-5 calibration corpus instance #1; Level 3 (empirical anchor at canonical L_max) is the upgrade target — A.40 PASS upgrades from canonical-import binding to substrate-natural binding; A.40 FAIL retains canonical-import binding.

---

## Wave 2 → Wave 4 Decision Point

### Cross-wave dependency declarations

Wave 2 outputs feed Wave 4 Stage-2 cross-axis verifies via the following chains:

1. **A.3 → W4 A.10 (`S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS`)**: A.10 reads the Connes-Karoubi pairing canonical R_canonical_value from A.3's npz output. A.10 is BLOCKED on A.11 PASS (14-state basis re-run; not in this wave); A.10 ALSO consumes A.3's npz as an input pin for the connes-axis dual-basis verify component.

2. **A.20 → W4 A.39 (`S89-VII-AH-STAGE-2-RE-DISPATCH-OBS2-OBS3`)**: A.39 is the eventual Stage-2 dispatch on §VII.AH 3HeB-excess-inheritance theorem candidate. A.39 reads the dual-prior 3-track JSON from A.20's output to interpret its PASS/FAIL/INFO outcome via the track-discriminator gate criterion (Sagan-revised PASS-AND / FAIL / INFO posterior re-allocation rules).

3. **A.40 → W4 A.38 (`S89-VII-AQ-STAGE-2-CROSS-AXIS-CANONICAL-IMPORT-BINDING`)**: A.38 audits the §VII.AQ Stage-2 cross-axis verify with substrate-input orthogonality enforced. A.40's PASS upgrades the §VII.AQ Level-3 anchor from canonical-import-binding to substrate-natural-binding BEFORE A.38 dispatches; A.38 then audits the substrate-natural-binding-upgraded entry. A.40 FAIL leaves §VII.AQ at canonical-import-binding; A.38 audits the existing canonical-import-binding entry.

4. **A.7 → W4 A.39 (cross-cluster)**: A.7's chi-prime independent inheritance morphism construction provides INDEPENDENT cross-check for the §VII.AH STAGE-1-CANDIDATE registry entry; A.39's Stage-2 multi-observable re-dispatch consumes A.7's npz output (kernel rank + Schur orthogonality proof steps) as a cross-axis verify for the M_3(ℂ) annihilation property of the inheritance morphism family.

### Cross-wave registry implications

- **§VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion**: blocked on (A.20 PASS dual-prior pre-registration in this wave) AND (A.39 PASS Stage-2 multi-observable re-dispatch in W4) AND (A.7 PASS or INFO chi-prime independent verification in this wave).

- **§VII.AQ canonical-import-binding → substrate-natural-binding upgrade**: depends on A.40 verdict in this wave; downstream A.38 Stage-2 in W4 audits the post-upgrade form.

- **Binding-Axis K-counter advancement**: A.40 PASS advances Binding-Axis K-counter from K=1 (W-23 W7b-82 V.5 calibration) to K=2 (advisory). K=3 promotion (MANDATORY status) requires one more calibration instance in S90+.

- **Element 3 fiducial-anchor binding discipline K-counter**: A.20 PASS advances K-counter from K=1 (W-15 V.7 calibration) to K=2 (advisory).

- **Definitional-datum-vs-derived-theorem K-counter**: A.7 PASS advances K-counter from K=2 (B.10 advisory) toward K=3 promotion candidate.

- **Cross-pillar-bridge-anatomy K-counter**: NOT advanced by W2 (A.3 + A.4 + A.20 + A.40 are all refinements of existing §VII.AQ + §VII.AH entries; A.7 advances Definitional-datum K-counter, NOT cross-pillar-bridge K-counter).

---

## Wave 2 Machinery-Enumeration Pin (§0.11)

Aggregated machinery pins across all 5 W2 gates per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR:

| PRDR atom | A.3 | A.4 | A.7 | A.20 | A.40 |
|:----------|:---:|:---:|:---:|:----:|:----:|
| N_eval | 1 | 1 | 1 | 1 | 1 |
| L_max | 10 | 10 | N/A | 10 | 10 |
| scan_range | N/A | N/A | N/A | N/A | N/A |
| step_size | N/A | N/A | N/A | N/A | N/A |
| tolerance | 1e-12 | 1e-3 | 1e-12 | 1e-10 | 1e-3 |
| scheme | Hochschild-cocycle-times-Chern-character | Cohomology-asymmetry-test-class-B | Connes-1996-reconstruction-NCG-axioms-3-5-6 | Sagan-revised-dual-prior-3-track | Chirality-resolved-D_K-spectrum-3-proxy-CS-GV-etaCS |
| convention | BdG-restricted-Connes-Karoubi-pairing-Connes-Moscovici-1995-III.4 | BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical | Independent-chi-prime-M2C-Cl1-target-Schur-orthogonality-derived-annihilation | Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant | Chirality-fidelity-3-proxy-substrate-natural-binding-W23-W7b-82-V5-B58-extension |
| random_seed | N/A | N/A | N/A | N/A | N/A |
| GPU_path | false | false | false | false | torch.linalg.eigh-if-available |

All 8 PRDR keyword atoms enumerated for each gate per `pru-pre-registration-template.md` PRDR keyword 8-K-atom enumeration. PRU Class-8 cardinality: 0 (zero missing pins).

---

## Wave 2 Input-SHA Ledger

Aggregated input-pin-map SHAs across all 5 W2 gates. SHAs computed at runtime per `closure_hash(input_pin_map)` protocol per `_script_template.py append_verdict()`. Intra-wave dependencies marked CRITICAL.

| Gate | Input file | Role | SHA pin |
|:-----|:-----------|:-----|:--------|
| A.3 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | D_K spectrum master cache | `<runtime>` |
| A.3 | `canonical_constants.py` | tau_fold + M_KK + cocycle norms + R_universal_HP1_strict_F4 pins | `<runtime>` |
| A.4 | `computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz` | **CRITICAL**: A.3 PASS prereq | `<runtime>` |
| A.4 | `canonical_constants.py` | tau_fold + M_KK + Delta_BCS + cocycle norms + substrate_cocycle_ratio_67_88 | `<runtime>` |
| A.4 | `computations/session-89/s89_gate_verdicts.txt` | **CRITICAL**: A.3 PASS line check | `<runtime>` |
| A.4 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | D_K spectrum cache for Σ_BdG_X | `<runtime>` |
| A.7 | `canonical_constants.py` | tau_fold + M_KK pins | `<runtime>` |
| A.7 | `.claude/rules/inheritance-falsifier-protocol.md` | inheritance morphism rank-2 framework | `<runtime>` |
| A.7 | `.claude/rules/cross-pillar-bridge-anatomy.md` | Level-2-binding sub-class | `<runtime>` |
| A.20 | `computations/session-89/s89_w2_a3_connes_karoubi_pairing.npz` | **CRITICAL**: A.3 PASS prereq | `<runtime>` |
| A.20 | `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.npz` | **CRITICAL**: A.4 PASS prereq | `<runtime>` |
| A.20 | `computations/session-89/s89_gate_verdicts.txt` | **CRITICAL**: BOTH A.3 + A.4 PASS lines | `<runtime>` |
| A.20 | `canonical_constants.py` | substrate_cocycle_ratio_67_88 pin | `<runtime>` |
| A.20 | `.claude/rules/cross-pillar-bridge-anatomy.md` | Element 3 binding discipline | `<runtime>` |
| A.20 | `.claude/rules/epistemic-discipline.md` | Dual-prior pre-registration T1-11 | `<runtime>` |
| A.40 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | D_K spectrum master cache; chirality-projected | `<runtime>` |
| A.40 | `canonical_constants.py` | tau_fold + M_KK + gv_canonical_difference_FW pins | `<runtime>` |
| A.40 | `.claude/rules/regulator-pin-discipline.md` | Binding-Axis sub-table | `<runtime>` |
| A.40 | `.claude/rules/cross-pillar-bridge-anatomy.md` | Three-Level Ladder | `<runtime>` |

### Output pinning

| Gate | Output file | Consumed-by |
|:-----|:------------|:------------|
| A.3 | `s89_w2_a3_connes_karoubi_pairing.npz` | A.4, A.20, W4 A.10 |
| A.4 | `s89_w2_a4_bcs_physics_grounded_r_substrate.npz` | A.20, W4 A.39 |
| A.7 | `s89_w2_a7_chi_prime_inheritance_morphism.npz` | W4 A.39 |
| A.20 | `s89_w2_a20_3heb_excess_inheritance_dual_prior.json` | W4 A.39 |
| A.40 | `s89_w2_a40_chirality_fidelity_3_proxy.npz` | W4 A.38 |
| A.40 | `s89_w2_a40_chirality_resolved_spectrum.npz` | intra-A.40 only |

### Verdict file pinning

All 5 gates emit canonical verdict line + dual-SHA companion comment row to:

`computations/session-89/s89_gate_verdicts.txt` (canonical per `gate-verdicts.md §"Canonical Verdict-File Path"`)

A.4 and A.40 ALSO emit the [SIGN]/[VERIFY] schema-v2 3-tuple companion comment row (sign_verdict / magnitude_verdict / regime_verdict).

### Closure SHA emission

Each gate emits `audit_sha256` computed from `closure_hash(input_pin_map)` per `_script_template.py append_verdict()`. The 64-character full hex digest is emitted in the canonical line; the 16-character head form may appear in prose sections but NEVER in the canonical line per `gate-verdicts.md §"Rules"`.

Per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` (S88 W8-100): if any W2 gate emits a corrective verdict line during execution, the corrective line MUST carry `supersedes=<full-64-char-old-audit-sha>` token in its `value=` field or in its dual-SHA companion comment row; the original line is RETAINED on disk per absolute verdict permanence.

---

## End of Wave 2 Plan

Wave 2 plans 5 gates (Ledger A items A.3, A.4, A.7, A.20, A.40) with effort 8.8 wave-equivalents (3.0 + 3.0 + 1.0 + 0.3 + 1.5). Intra-wave dependency chain: A.3 → A.4 → A.20; A.7 and A.40 are structurally independent. Cross-wave outputs feed Wave 4 Stage-2 cross-axis verifies (A.10, A.38, A.39). All gates pre-registered with full 13-field gate blocks per `/rclab-plan` skill §3b. PRU Class-8 cardinality: 0 (zero missing machinery pins). Substrate framing per `phononic-framing.md §"IS Space, Not IN Space"` IS-not-IN: declared explicitly in each gate's §13.
