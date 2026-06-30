# Session 88 Plan — Wave 3c: DR3 + script architecture + d_eff anchor audit

> **Authoring orchestrator role**: planner-w3c (split of stalled W3).
> **Theme**: DR3 demarcation theorem regulator-class-invariance audit (#29) + bridge-landing-script architecture refinement (#30) + d_eff anchor convention audit (#57).
> **Owners**: lizzi-spectral-functional-theorist PRIMARY on #29 + #57; gen-physicist hygiene-only on #30.
> **Provenance**: extracted from `sessions/session-plan/session-88-context.md` items #29, #30, #57; this wave is the spectral-functional-theorist-led portion of the parent W3 stall split.
> **Cross-references**:
> - `.claude/rules/regulator-convention-lockdown.md` (DR3 demarcation theorem; CAC binding form)
> - `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension"
> - `.claude/rules/wave-classification.md` (M1-M4 METHODOLOGY-class conjunction; #30 routes here)
> - `.claude/rules/methodology-wave-allowlist.md` (append-only allowlist for #30)
> - `.claude/rules/cross-pillar-bridge-anatomy.md` (5 IS-not-IN anatomy + 3-level ladder background for W5-1..W5-5 audit-trail subject of #30)
> - `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" (PRU Class-8 + Class 8.3 publication-precision)
> - canonical_constants.py: `w0_FW = -0.918`, `tau_fold = 0.190`, `gv_canonical_difference_FW = -40579.1500479506`, `max_pair_ratio_A_5_FW = 9.240438549812e-01`

---

## Wave 3c Summary

This wave pursues three structurally-independent items extracted from the S87→S88 carry-forward queue:

1. **§W3c-29 — DR3 regulator-class-invariance audit** (`S88-OR-LATER-W5-4-CF65-ETA-GV-REGULATOR-INDEPENDENCE`): re-runs the W5-4 CF65 (η=0, GV≠0) parity-twin signature across the A_5_extended atlas {zeta, Pauli-Villars, Mellin, lattice, legacy cutoff_sqrt} under the DR3 demarcation theorem's canonical-anchored convention (CAC). Test predicate: regulator-class-invariance of the (η=0 by even-grading parity-blindness; GV≠0 via odd-grading Heitsch) signature on (C_H, C_epsH). FUNCTIONAL-INDEPENDENT prediction — every admissible regulator MUST yield the same η/GV qualitative pattern.

2. **§W3c-30 — Bridge-landing-script architecture refinement** (`S88-BRIDGE-LANDING-SCRIPT-ARCHITECTURE-REFINEMENT`): METHODOLOGY-class wave per `wave-classification.md` M1-M4. W5-1 dual-trio audit-trail observation showed 4 of 5 W5 gates (W5-1, W5-3, W5-4, W5-5) emitted FAIL/INFO→PASS double-trios per S86 W1c-5 all-3-lines-retained discipline. Root cause: scripts perform `write → re-read → verify → conditionally re-write/append` instead of `write_promotion → fsync → re-read → verify → emit`. Refactor proposes single-shot pattern; deliverable is a refactored sample script + before/after diff + rule-file edit landed at registry/methodology layer.

3. **§W3c-57 — d_eff anchor convention numerology audit** (`S88-D-EFF-ANCHOR-CONVENTION-AUDIT`): W1b-3 Richardson L^{-3} extrapolation produced `slope_∞_B = 5.061193223` (Conv B); the coincidence `5.061 ≈ 4·τ_fold + correction ≈ 5.04 + ε` (with τ_fold = 0.190) admits two readings — (R1) structural identification `slope_∞_B = 5 + 4·τ_fold + small_correction` rooted in HK-5 form `slope_A(τ) = 5/(1−τ/(5π))`; (R2) numerical coincidence absent any derivation. Audit performs Sage-symbolic substitution chain comparison against the Conv-B baseline 5 (HK-5 at τ=0).

The wave is FUNCTIONAL-INDEPENDENT in spirit (#29 + #57) plus methodology hardening (#30); none of the three items depend on each other at runtime, so they can dispatch in parallel after Wave 3c Decision Point Prerequisites clear.

---

## Wave 3c Decision Point Prerequisites

The wave dispatches when ALL of the following PRDR prerequisites have landed:

| Prereq | Source | Required state |
|:-------|:-------|:---------------|
| P1: A_5_extended atlas pin | canonical_constants.py | `max_pair_ratio_A_5_FW = 9.240438549812e-01` AND `gv_canonical_difference_FW = -40579.1500479506` PRESENT (S87 W8 promoted) |
| P2: DR3 demarcation theorem | `.claude/rules/regulator-convention-lockdown.md` | LANDED at S86 W12-4 + 1a-S8; §"Demarcation theorem (admissibility class)" defines CAC binding form |
| P3: W-11 RULE-2 supersession | `.claude/rules/regulator-pin-discipline.md` §"Class-(c)" | even Seeley-DeWitt parity-blindness theorem PROMOTED-PARITY-BLINDNESS; (η=0, GV≠0) on (C_H, C_epsH) PERMANENT |
| P4: W11-1 §VII.AF.2 §VII.P-v2 | `sessions/permanent-results-registry.md` §VII.AF.2 + §VII.P-v2 | HP^1-content-distinct corridor recast PERMANENT (W11-1 V_4 substrate-falsification supersession event) |
| P5: W5-1..W5-5 audit-trail double-trios | `computations/s87_gate_verdicts.txt` | 4 of 5 W5 gates retain dual FAIL/INFO→PASS verdict-line trios per S86 W1c-5 all-3-lines-retained discipline (subject of #30) |
| P6: W1b-3 Richardson extrapolation | S87 W1b-3 verdict + npz | `slope_∞_A = 10.122386446` (Conv A) + `slope_∞_B = 5.061193223` (Conv B) PASS |
| P7: τ_fold = 0.190 canonical | canonical_constants.py:tau_fold | PIN PRESENT (S58 Volovik partition canonical, multi-session locked) |
| P8: A_F finite spectral algebra | `(A_K, H_K, D_K)` substrate-triple definition | A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) per S86 W-3 R3 SOURCE-DOUBLE-CITE-CO-PRIMARY pin |

Plan-freeze halts if any of P1-P8 absent at dispatch time. Each prerequisite is verified at plan-freeze by `_source_reconciliation_audit.py` post-V.2 + `_pru_cardinality_audit.py` cardinality pre-flight.

---

## §W3c-29. S88-OR-LATER-W5-4-CF65-ETA-GV-REGULATOR-INDEPENDENCE

**Owner**: lizzi-spectral-functional-theorist PRIMARY (sole-writer of registry-side functional-class invariance audit). Co-author advisory: connes-ncg-theorist (NCG-axiomatic verification of even-grading parity-blindness theorem applicability).

**Class**: COMPUTE (Level-1 substrate-first canonical sourcing per `substrate-first-canonical-sourcing.md`).

**Verdict source**: `computations/s88_gate_verdicts.txt`

**Substrate-IS observable**: the (η, GV) parity-twin signature evaluated on (C_H, C_epsH) — finite-L (L_max=10) spectral-triple Heitsch cocycle pairing AND eta-invariant of D_K^{≤10} restricted to the parity-twin sub-algebra ε_H · A_F · ε_H^{-1} (where ε_H is the J-parity grading operator from §VII.AF.2).

**Pre-registered PASS predicate**:

```
PASS iff for every regulator R ∈ A_5_extended = {zeta, Pauli-Villars, Mellin, lattice, cutoff_sqrt}:
    (i)  η^R(C_H, C_epsH; L=10, τ=0.190) = 0  with |residual| ≤ 1e-12
    (ii) GV^R(C_H, C_epsH; L=10, τ=0.190) ≠ 0 with |GV| ≥ 1e-6  (substrate-natural lower bound)
    (iii) sign(GV^R) is INVARIANT across all 5 regulators (FUNCTIONAL-INDEPENDENT signature)
    (iv) |GV^R(C_H) / GV^R(C_epsH)| ratio matches W11-5 Pillar-V calibration ratio 7.324992 ± 0.5%
         under the (Δ_B/Δ_A)^p cancellation theorem applicability declaration
```

**INFO predicate**: ratio (iv) drifts > 0.5% across regulators but signs and qualitative pattern (η=0 / GV≠0) preserved → INFO with regulator-class drift exposed; routes to next-session refinement.

**FAIL predicate**: any regulator violates (i)-(iii); structural FAIL of W-11 RULE-2 STRENGTHENED claim.

**Substrate-physics derivation chain**:

```
Step 1 (definitions):
  D_K^{≤10} = block-diagonal Dirac on (A_F, H_K^{≤10}) per Peter-Weyl decomposition
  A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)  (S86 W-3 R3 SOURCE-DOUBLE-CITE-CO-PRIMARY)
  ε_H = J-parity grading on H_K^{≤10}; ε_H^2 = 1, [ε_H, D_K] = 0
  C_H, C_epsH = parity-twin sub-algebras: C_H = {a ∈ A_F : ε_H a ε_H^{-1} = +a},
                                          C_epsH = {a ∈ A_F : ε_H a ε_H^{-1} = -a}
Step 2 (eta-invariant under regulator R):
  η^R(B; L) := lim_{s→0} sum_{λ ∈ spec(D_K|_B)} sign(λ) |λ|^{-s} · w_R(|λ|)
  where w_R is the regulator weight (zeta: w=1; PV: 1 - exp(-λ²/Λ²); Mellin: residue extractor; lattice: heaviside; cutoff_sqrt: sqrt cutoff)
Step 3 (even Seeley-DeWitt parity-blindness theorem; W-11 RULE-2 STRENGTHENED):
  for ANY even-grading regulator-weighted Mellin moment m_n^R(D_K^2):
    m_n^R(D_K^2)|_{C_H ⊕ C_epsH} = m_n^R(D_K^2)|_{C_H} + m_n^R(D_K^2)|_{C_epsH}
    AND parity-blindness ⇒ m_n^R(C_H) = m_n^R(C_epsH)  ∀ n  ∀ R ∈ A_5_extended
  ⇒ even-grading η contribution VANISHES on (C_H, C_epsH) parity-twin pair
Step 4 (GV-Heitsch odd-grading detector):
  GV^R(B; L) := <[φ_g^{sym}], [Ch(P_0(τ_fold))]>_R  on B = C_H or C_epsH
  GV is odd-grading (HP^1-class observable per §VII.AF.2 + §VII.P-v2)
  ⇒ GV^R(C_H) ≠ GV^R(C_epsH) by HP^1-content-distinct corridor recast (W11-1 PERMANENT)
Step 5 (regulator-class invariance under DR3 CAC):
  CAC: w_0^R(L) = ρ_X^R(L) + offset_X^R   with offset_X^R = w_0_FW - ρ_X^R(L=10)
  ⇒ at L=10 anchor every R ∈ A_5_extended satisfies w_0^R(10) = w_0_FW EXACTLY
  ⇒ at the L=10 anchor the substrate-IS HP^1 cocycle pairing GV^R is regulator-class-invariant
     up to the offset_X^R additive constant that absorbs effacement contribution
Step 6 (substitution + read off direction):
  η^R(C_H, C_epsH; 10, 0.190) = 0     ∀ R                    [Step 3, parity-blindness]
  GV^R(C_H) / GV^R(C_epsH) = ‖φ_67‖ / ‖φ_88‖ = 7.324992       [Step 4 + W11-5 Pillar-V calibration]
  sign(GV^R) invariant ∀ R ∈ A_5_extended                     [Step 5, CAC-anchored]
Conclusion: (η=0, GV≠0) signature regulator-class-invariant per W-11 RULE-2 STRENGTHENED.
            Pre-registered PASS predicate (i)-(iv) is a SUBSTRATE-FIRST FUNCTIONAL-INDEPENDENT prediction.
```

**Machinery pin (§0.11 PRDR enumeration)**:

| Pin | Value | Provenance |
|:----|:------|:-----------|
| `L_max` | 10 | W11-3 Friedrich-Bär saturation theorem L_max-saturation pin |
| `tau_fold` | 0.190 | canonical_constants.py:tau_fold (S58 Volovik partition canonical) |
| `regulator_atlas` | A_5_extended = ['zeta', 'Pauli-Villars', 'Mellin', 'lattice', 'cutoff_sqrt'] | S87 W8 promoted (`max_pair_ratio_A_5_FW`, `gv_canonical_difference_FW`) |
| `eta_residual_tol` | 1e-12 | publication-precision pin per `epistemic-discipline.md` §"Publication-Precision Pre-Registration"; full float64 |
| `gv_lower_bound` | 1e-6 | substrate-natural lower bound on HP^1 cocycle norm (Sage-exact φ_88 = 0.108307 M_KK² × 1e-6 truncation factor) |
| `ratio_target` | 7.324992 | W-5 Pillar-V calibration `‖φ_67‖ / ‖φ_88‖` Sage-exact (canonical_constants.py if landed; else inline pin from `permanent-results-registry.md` §VII.AF.1) |
| `ratio_tol` | 0.005 (= 0.5%) | Pre-registered; derived from W-5 Gate-2 0.1% × 5× regulator-class drift safety margin |
| `eta_method` | `'spectral_zeta_residue_at_s_eq_0'` | canonical η-invariant computation method |
| `gv_method` | `'connes_karoubi_pairing_at_band_0_projector'` | canonical GV-Heitsch HP^1 cocycle pairing |
| `cac_offset_per_R` | computed in-script as `offset_R = w_0_FW - rho_X_R(L=10)` | DR3 demarcation theorem (`regulator-convention-lockdown.md` §"Rule") |
| `J_parity_grading_op` | ε_H from §VII.AF.2 + §VII.P-v2 | W11-1 §VII.AF.2 + §VII.P-v2 PERMANENT |
| `A_F_decomp` | ℂ ⊕ ℍ ⊕ M_3(ℂ) | S86 W-3 R3 SOURCE-DOUBLE-CITE-CO-PRIMARY |
| `spectrum_cache_path` | `computations/s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 | S84 W2-7 master-spectrum cache (truncation_consistent verified) |
| `output_npz` | `computations/s88_w3c_eta_gv_regulator_independence.npz` | new file |
| `output_png` | `computations/s88_w3c_eta_gv_regulator_independence.png` | 2×5 panel: (top row η^R per regulator, bot row GV^R per regulator + ratio bars) |

**Substrate-IS framing (mandatory per `phononic-framing.md` §"IS Space, Not IN Space")**:

The (C_H, C_epsH) parity-twin pair IS the substrate-first finite-L spectral-triple structure on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. The eta-invariant η^R and GV-Heitsch cocycle pairing GV^R are substrate-IS observables — they are intrinsic structural numbers of the finite spectral triple, NOT BdG band-structure derivatives or container-spacetime quantities. The DR3 demarcation theorem's CAC anchors every regulator at L=10 to the substrate-canonical w_0_FW = -0.918 (S58 Volovik partition); this is what makes the (η=0, GV≠0) signature FUNCTIONAL-INDEPENDENT across the A_5_extended atlas.

**Audit trail / verdict-line emission**:

Verdict-line schema per `gate-verdicts.md`:

```
S88-OR-LATER-W5-4-CF65-ETA-GV-REGULATOR-INDEPENDENCE: {VERDICT} -- value={...} \
  scheme=substrate-IS-CAC-anchored convention=A_5_extended-FUNCTIONAL-INDEPENDENT \
  L_max=10 audit_sha256={64-char} content_sha256={64-char} schema_version=R3
```

`value=` field encodes 5-tuple `(eta_max_R, gv_min_R, ratio_max_R, ratio_min_R, sign_invariant_bool)`.

**Per-class compute rigor**:

- Import all canonical constants per `math-scripts.md` §"Canonical Constants"; never hardcode `tau_fold`, `w0_FW`, `M_KK`, `gv_canonical_difference_FW`, `max_pair_ratio_A_5_FW`, A_F decomposition.
- GPU pin: AMD RX 9070 XT via `torch.linalg`; D_K^{≤10} dense block sub-algebra ε_H · A_F · ε_H^{-1} restriction is at most ~10000×10000 (well below 0.5 × VRAM = 8.5 GB).
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`.
- Local-tag intermediate variables per `math-scripts.md` §"Local Variable Tagging".

**Carry-forward (if INFO)**: route to S89+ `S89-ETA-GV-REGULATOR-CLASS-DRIFT-RESOLUTION` with 4-field spec.

---

## §W3c-30. S88-BRIDGE-LANDING-SCRIPT-ARCHITECTURE-REFINEMENT

**Owner**: `lizzi-spectral-functional-theorist` (hygiene-only, methodology-class).

**Class**: METHODOLOGY-class per `wave-classification.md` M1-M4 strict conjunction:
- **M1 (PASS predicate type)**: artifact-existence-with-substantive-content (rule-file diff + sample refactored script + working-paper section ≥ 15 lines; NO numerical comparison against threshold).
- **M2 (producing-operation type)**: `Edit` / `Write` on `.claude/rules/registry-landing.md` AND `computations/_bridge_landing_script_template.py` (NEW); grep / SHA-256 cross-checks; integer counts (verdict-line trio counts in s87_gate_verdicts.txt). NO `.py` script with numerical threshold.
- **M3 (source-of-truth type)**: verbatim sub-diff from S87 W5-1 dual-trio audit-trail observation + S86 W1c-5 all-3-lines-retained discipline (existing rule). No new derivation; this wave-item lands the structural-discipline observation as a methodology rule + reusable script template.
- **M4 (allowlist membership)**: gate-ID `S88-BRIDGE-LANDING-SCRIPT-ARCHITECTURE-REFINEMENT` MUST be append-row in `.claude/rules/methodology-wave-allowlist.md` BEFORE plan-freeze (orchestrator-direct write at plan-freeze; subagent edit FORBIDDEN per recursion-attack closure).

**Verdict source**: `computations/s88_gate_verdicts.txt` (METHODOLOGY-class verdict line; dual-SHA closure per `wave-classification.md` §"Dual-SHA closure for METHODOLOGY-class": `content_sha256` over rule-file diff; `audit_sha256` over input-pin map of source documents).

**PASS predicate (artifact-existence-with-substantive-content)**:

```
PASS iff ALL of the following exist on disk:
  (a) .claude/rules/registry-landing.md edited with NEW §"Bridge-Landing Script Architecture (single-shot pattern)"
      sub-section AND content_sha256 of the diff matches input-pin-map-derived hash
  (b) computations/_bridge_landing_script_template.py NEW; substantive_line_count >= 60
      (full single-shot pattern: write_promotion → fsync → re-read → verify → emit)
  (c) computations/_bridge_landing_audit_trail_observation_S87_W5.md NEW; substantive_line_count >= 15;
      enumerates the 4-of-5 W5 gates that emitted FAIL/INFO→PASS double-trios with verdict-line SHAs
  (d) sessions/archive/session-88/session-88-w3c-workingpaper.md §W3c-30 substantive section >= 25 lines;
      includes BEFORE / AFTER pseudo-code diff + S86 W1c-5 cross-link
  (e) .claude/rules/methodology-wave-allowlist.md row appended with gate-ID + session=S88 +
      rationale + sha256_of_plan_block (computed at plan-freeze; pending OK at dispatch only as one-time exception)
```

**Substrate-physics derivation NOT REQUIRED (METHODOLOGY-class M3 substrate is verbatim-extract from prior closed observation)**.

**Audit trail observation (verbatim from S87 W5-1 dispatch trace)**:

W5-1 + W5-3 + W5-4 + W5-5 (4 of 5 W5 dispatch gates) emitted FAIL or INFO verdict line at first script run → re-read working-paper section → verify section content matches input-pin-map → conditionally emit corrective PASS verdict line. Result: each gate's verdict-line trio in `computations/s87_gate_verdicts.txt` shows `(FAIL/INFO line + companion comment row + PASS line + companion comment row)` → effective 4-line group per gate (instead of canonical 2-line dual-SHA closure). The S86 W1c-5 all-3-lines-retained discipline correctly preserves audit provenance, but the structural cause is the script architecture: scripts perform `write → re-read → verify → conditionally re-write/append` instead of single-shot `write_promotion → fsync → re-read → verify → emit`.

**Refactored single-shot pattern (deliverable (b) sample)**:

```python
# BEFORE (4-of-5 W5 pattern; emits double-trio under verifier-rubric mismatch):
def land_bridge(plan_block, registry_slot):
    write_registry_entry(plan_block, registry_slot)               # (1) write
    actual_section = re_read_registry_at(registry_slot)           # (2) re-read
    if not verify_section_matches(actual_section, plan_block):    # (3) verify
        emit_verdict_line('FAIL', ...)                            # (3a) emit FAIL
        rewrite_registry_entry(plan_block, registry_slot)         # (3b) corrective rewrite
        actual_section_2 = re_read_registry_at(registry_slot)     # (3c) re-read
        if verify_section_matches(actual_section_2, plan_block):  # (3d) re-verify
            emit_verdict_line('PASS', ...)                        # (3e) emit PASS
        else:
            emit_verdict_line('FAIL', ...)                        # (3f) double-FAIL
    else:
        emit_verdict_line('PASS', ...)

# AFTER (single-shot pattern):
def land_bridge(plan_block, registry_slot):
    promotion_text = build_promotion_text(plan_block, registry_slot)  # (1) build in memory
    write_atomic_with_fsync(promotion_text, registry_slot)              # (2) write + fsync
    actual_section = re_read_registry_at(registry_slot)                 # (3) re-read
    verdict = 'PASS' if verify_section_matches(actual_section,
                                                promotion_text) else 'FAIL'
    emit_verdict_line(verdict, content_sha256(actual_section),          # (4) emit ONCE
                      audit_sha256(input_pin_map))
```

The single-shot pattern eliminates the corrective-rewrite branch by requiring the promotion text to be FULLY built in memory before any disk write; the post-fsync re-read is the FINAL verification step (no conditional retry permitted; FAIL emits FAIL and the gate honestly closes per `mechanical-closure-discipline.md` if a structural defect is detected).

**Machinery pin (§0.11 PRDR enumeration)**:

| Pin | Value | Provenance |
|:----|:------|:-----------|
| `wave_class` | METHODOLOGY | `wave-classification.md` M1-M4 strict conjunction |
| `producing_ops_allowlist` | {Edit, Write, MultiEdit, grep, wc, sha256sum, integer counts} | `wave-classification.md` §M2 |
| `producing_ops_forbidden` | {.py with numerical threshold, eigenvalue compute, FFT, integral, fixture-with-hardcoded-numerical-target} | `wave-classification.md` §M2 |
| `target_files` | (a) `.claude/rules/registry-landing.md` (b) `computations/_bridge_landing_script_template.py` (c) `computations/_bridge_landing_audit_trail_observation_S87_W5.md` (d) `sessions/archive/session-88/session-88-w3c-workingpaper.md` (e) `.claude/rules/methodology-wave-allowlist.md` | enumerated above |
| `input_pin_map` | {S87_W5_dispatch_trace_sha, S86_W1c_5_rule_sha, registry_landing_md_pre_edit_sha, methodology_wave_allowlist_md_pre_edit_sha} | computed at plan-freeze |
| `dual_sha_closure_target` | `content_sha256(rule_file_diff) + audit_sha256(input_pin_map)` | `wave-classification.md` §"Dual-SHA closure for METHODOLOGY-class" |
| `allowlist_row_template` | `S88-BRIDGE-LANDING-SCRIPT-ARCHITECTURE-REFINEMENT \| S88 \| W3c-30 single-shot pattern landing per S87 W5-1 audit-trail observation \| {sha256_of_plan_block}` | `methodology-wave-allowlist.md` §"Schema" |
| `output_verdict_line` | `computations/s88_gate_verdicts.txt` METHODOLOGY-class entry | `gate-verdicts.md` |

**Substrate-IS framing**: this gate operates at the METHODOLOGY layer of the layer-functor F (per `epistemic-discipline.md` §"Layer-Decomposition" T2-7). The substrate-physics image of "single-shot script architecture" under F is "atomic substrate-IS observable evaluation at L_max=10 with no convention-shopping retry"; the audit-layer image is "single dual-SHA verdict line per gate with no FAIL/PASS double-trio". F preserves the discipline: a Class-8 PRU at the substrate layer (machinery pin missing) maps under F to a methodology Class-8 PRU (rule-file pre-registration missing) and to an audit Class-8 PRU (audit-line pre-registration missing). #30 lands the methodology-layer fix; substrate-layer and audit-layer images are downstream-preserved by F.

**PROHIBITED per `wave-classification.md` §M2**: any `.py` script in this gate's deliverables MUST NOT contain a numerical PASS threshold. The `_bridge_landing_script_template.py` deliverable (b) is a TEMPLATE FILE (re-usable pattern); its docstring + comments + reference implementations are the substantive content; it does NOT execute a numerical comparison.

**Carry-forward (if INFO/FAIL)**: route to S89 `S89-METHODOLOGY-WAVE-ALLOWLIST-RECURSION-AUDIT` with 4-field spec.

---

## §W3c-57. S88-D-EFF-ANCHOR-CONVENTION-AUDIT

**Owner**: lizzi-spectral-functional-theorist PRIMARY (sole-writer of HK-form spectral-functional dimension audit). Co-author advisory: connes-ncg-theorist (NCG-axiomatic verification of d_eff dimension-spectrum interpretation).

**Class**: COMPUTE (Level-1 substrate-first canonical sourcing per `substrate-first-canonical-sourcing.md`); structural numerology test.

**Verdict source**: `computations/s88_gate_verdicts.txt`

**Substrate-IS observable**: the W1b-3 Richardson L^{-3} extrapolated slope `slope_∞_B = 5.061193223` (Conv B baseline) interpreted as a substrate-IS dimension-spectrum observable on `(A_K, H_K, D_K)`. The numerical coincidence `5.061 ≈ 4·τ_fold + correction ≈ 5.04 + ε` admits structural-or-coincidence reading.

**Pre-registered three-track verdict** (per `epistemic-discipline.md` §"Dual-prior pre-registration as track-discriminator pattern" extended to triple-prior):

```
PASS iff slope_∞_B = HK-5(τ_fold)  EXACTLY (Sage-symbolic identity, residual ≤ 1e-12)
        AND substrate-physics derivation chain landed in working-paper §W3c-57
        AND derivation cites HK-5 form slope_A(τ) = 5/(1−τ/(5π)) at the appropriate τ pin

INFO iff slope_∞_B - HK-5(τ_anchor=0.190) < 1e-3 ABSOLUTE  (numerical near-match)
        AND substrate-physics derivation chain INCOMPLETE (suggestive but not closed)
        AND classified as candidate structural identification deferred to S89

FAIL (= numerology coincidence ruling) iff Sage-symbolic comparison shows
     |slope_∞_B - HK-5(τ_anchor)| ≥ 1e-3 ACROSS ALL CANDIDATE τ_anchor ∈ {0, τ_fold, τ_fold/2, 2·τ_fold}
     AND no algebraic identity of form `slope_∞_B = a + b·τ_fold + c·τ_fold² + ...`
     with rational (a, b, c) at small numerator/denominator coefficients matches within 1e-6
     ⇒ explicit numerology ruling: 5.061 ≈ 5 + 4·τ_fold ≈ 5.04 is COINCIDENCE absent derivation

Triple-prior pre-registration:
  Track A (structural identification, HK-5 closure): prior 0.30
  Track B (numerical near-match deferred): prior 0.45
  Track C (numerology coincidence, no derivation): prior 0.25
  PASS / INFO / FAIL maps to posterior re-allocation as documented above.
```

**Substrate-physics derivation chain (per `math-scripts.md` §"Double-Check Logic Before Compute")**:

```
Step 1 (definitions):
  slope_∞_B    := Richardson L^{-3} extrapolated slope of d_eff(L) under Conv B baseline
                  = 5.061193223  (S87 W1b-3 PASS, .npz key `slope_inf_B`)
  τ_fold       := 0.190  (canonical_constants.py:tau_fold; S58 Volovik partition canonical)
  HK-5(τ)      := 5/(1 − τ/(5π))   (Heat-Kernel-form 5 spectral-dimension predicate; W-?
                                    HK-5 family; cited in W1b-3 as Conv-B baseline form)
  Conv-B baseline := τ = 0 ⇒ HK-5(0) = 5
Step 2 (substitute τ_fold into HK-5):
  HK-5(τ_fold) = 5 / (1 − 0.190/(5π))
              = 5 / (1 − 0.190/15.70796...)
              = 5 / (1 − 0.0120953...)
              = 5 / 0.9879047
              = 5.061222...
Step 3 (compare against slope_∞_B):
  |slope_∞_B − HK-5(τ_fold)| = |5.061193223 − 5.061222...| ≈ 2.9e-5
                              [BELOW 1e-3 INFO threshold; ABOVE 1e-12 PASS threshold]
Step 4 (explicit substitution-chain reading):
  slope_∞_B ≈ HK-5(τ_fold)  to within ~3e-5 ABSOLUTE
            ≈ 5 + 5·τ_fold/(5π) + O(τ_fold²)/(5π)²
            ≈ 5 + τ_fold/π + small
            ≈ 5 + 0.0605 + ε
            ≈ 5.061  (matches W1b-3 numerical to 3-sig-fig)
  This is NOT equal to "5 + 4·τ_fold + ε" = 5 + 0.760 + ε = 5.76; the W3c-57 spawn-prompt
  hypothesis of "4·tau_fold" is REJECTED by Step 4 substitution chain.
  The correct candidate identification is slope_∞_B ≈ HK-5(τ_fold) = 5/(1−τ_fold/(5π)).
Step 5 (dimensionality + sign reading):
  HK-5 is increasing in τ on [0, 5π); τ_fold = 0.190 > 0 ⇒ HK-5(τ_fold) > HK-5(0) = 5
  ⇒ slope_∞_B > 5 by spectral-zeta-residue + Jensen-deformation argument
  ⇒ direction MATCHES W1b-3 measurement (5.061 > 5).
Step 6 (Sage-symbolic identity test):
  Run Sage `simplify((5/(1 - 19/(50*pi))) - 5.061193223)` to QQ
  Expected: residual ≈ 2.9e-5 (Track B INFO band)
Conclusion: SUBSTITUTION CHAIN IDENTIFIES Track B INFO at HK-5(τ_fold); spawn-prompt's
            "4·tau_fold" hypothesis is structurally INCORRECT and SUPERSEDED.
            INFO verdict expected; structural identification candidate for S89 closure.
```

**Machinery pin (§0.11 PRDR enumeration)**:

| Pin | Value | Provenance |
|:----|:------|:-----------|
| `slope_inf_B_observed` | 5.061193223 | S87 W1b-3 npz `slope_inf_B` Richardson L^{-3} extrapolation |
| `slope_inf_A_observed` | 10.122386446 | S87 W1b-3 npz `slope_inf_A` (Conv A; 2× ratio cross-check anchor) |
| `tau_fold` | 0.190 | canonical_constants.py:tau_fold (S58 Volovik partition canonical) |
| `hk_5_form_canonical` | `5/(1 − τ/(5π))` | W1b-3 Conv-B baseline; HK-5 family cited (substrate-physics derivation Step 1) |
| `hk_5_at_tau_fold` | computed in-script as `5/(1 - 0.190/(5*pi))` via Sage QQ | substitution chain Step 2 |
| `pass_threshold_absolute` | 1e-12 | publication-precision pin per `epistemic-discipline.md` §"Publication-Precision Pre-Registration" full float64 |
| `info_threshold_absolute` | 1e-3 | pre-registered numerical near-match band |
| `tau_anchor_candidate_set` | {0, τ_fold/2, τ_fold, 2·τ_fold} = {0, 0.095, 0.190, 0.380} | numerology coincidence ruling sweep |
| `algebraic_identity_search_grid` | rational (a,b,c) ∈ {-3..+3}/{1..30} for `slope = a + b·τ_fold + c·τ_fold²` | numerology coincidence ruling FAIL fallback |
| `algebraic_identity_match_tol` | 1e-6 | tighter than INFO threshold; structural identity vs near-match |
| `sage_method` | `mcp__sage__sage_eval` for symbolic π and QQ rationals | Sage MCP; `sage_simplify` for HK-5 reduction |
| `triple_prior` | (0.30, 0.45, 0.25) for Tracks (A: structural HK-5 / B: numerical near-match / C: coincidence) | `epistemic-discipline.md` extended dual-prior → triple-prior |
| `ratio_cross_check` | slope_∞_A / slope_∞_B = 10.122386 / 5.061193 = 2.000000 | Conv A / Conv B 2× factor structural cross-check |
| `output_npz` | `computations/s88_w3c_d_eff_anchor_audit.npz` | new file |
| `output_png` | `computations/s88_w3c_d_eff_anchor_audit.png` | 2-panel: (top) HK-5(τ) curve with τ_fold pin + slope_∞_B horizontal, (bot) algebraic identity grid heatmap |

**Substrate-IS framing**: the d_eff dimension-spectrum observable on `(A_K, H_K, D_K)` IS the spectral-functional reading of the heat-kernel form HK-5(τ). It is NOT a "spacetime dimension" of a container geometry. The Richardson L^{-3} extrapolation is the substrate-IS bridge map at L_max → ∞; the value 5.061 IS the substrate's spectral-action prediction under Conv B baseline. The audit at #57 is whether this prediction has a closed-form structural source (HK-5 at τ_fold) or is numerical-near-match-without-derivation (Track B INFO) or pure coincidence (Track C FAIL with numerology ruling).

**Numerology vs structural identification discipline (per `epistemic-discipline.md` §"What Does NOT Count as Evidence" item 4 "Analogies without quantitative backing")**:

The spawn-prompt's `5.061 ≈ 4·τ_fold + correction ≈ 5.04 + ε` reading is a NUMEROLOGICAL ANALOGY without quantitative substrate-physics backing. The substitution chain Step 4 EXPLICITLY REJECTS this reading: 5 + 4·τ_fold = 5.76 (not 5.04; arithmetic error in the spawn-prompt). The CORRECT structural candidate is HK-5(τ_fold) = 5/(1−τ_fold/(5π)) ≈ 5.061222, which matches slope_∞_B to ~3e-5. This is the working hypothesis the gate tests; the verdict classification depends on whether (a) the residual ~3e-5 is at L_max=10 truncation noise level (Track A PASS path with refined L_max=12 cross-check) or (b) the residual is genuinely above any plausible truncation-noise floor (Track B INFO path).

**Audit trail / verdict-line emission**:

```
S88-D-EFF-ANCHOR-CONVENTION-AUDIT: {VERDICT} -- value={...} \
  scheme=substrate-IS-Richardson-L3-extrapolation convention=HK-5-form-Conv-B-baseline \
  L_max=10 audit_sha256={64-char} content_sha256={64-char} schema_version=R3
```

`value=` field encodes 4-tuple `(slope_inf_B_observed, hk_5_at_tau_fold, residual_absolute, track_assigned)`.

**Per-class compute rigor**:

- Import all canonical constants per `math-scripts.md` §"Canonical Constants"; never hardcode tau_fold or HK-5 form.
- Sage MCP is the structural identity test substrate; use `mcp__sage__sage_eval` for symbolic π evaluation; `mcp__sage__sage_simplify` for HK-5 ratio reduction.
- Algebraic identity search grid is small (~3000 candidates); CPU sequential is sufficient; no GPU needed.
- Local-tag intermediate variables per `math-scripts.md` §"Local Variable Tagging".

**Carry-forward (if INFO)**: route to S89+ `S89-D-EFF-HK-5-STRUCTURAL-CLOSURE` with 4-field spec — full L_max=12 cross-check + Jensen-deformation second-order substitution Step 4 expansion + connes-ncg-theorist NCG-axiomatic verification of HK-5 dimension-spectrum interpretation.

**Carry-forward (if FAIL)**: numerology ruling → record at `sessions/framework/registry/coincidence-ruling-corpus.md` (NEW or existing); the residual is documented as "unexplained ≈ 5.061 with no algebraic identity in the (a,b,c) ∈ ±3/30 grid". Future investigation routed to deeper Mellin-cone substrate-distance analysis.

---

## Wave 3c → Wave 4 Decision Point

| If Wave 3c outcome | Wave 4 routing |
|:-------------------|:---------------|
| 3-of-3 PASS | continue per parent W3 split unblocking; W3a + W3b + W3c results integrate at S88 closeout synthesis |
| #29 INFO (regulator-class drift exposed) | route to S89 `S89-ETA-GV-REGULATOR-CLASS-DRIFT-RESOLUTION`; #30 + #57 verdicts unaffected; W4 dispatches normally |
| #29 FAIL (W-11 RULE-2 STRENGTHENED claim falsified) | HIGH-LEVERAGE result — escalate to plan-author halt + workshop dispatch (lizzi vs connes adversarial review of even Seeley-DeWitt parity-blindness theorem); W4 route halts pending resolution |
| #30 INFO/FAIL (allowlist row miswritten OR refactored template absent) | mechanical-closure-discipline: in-session orchestrator-direct-write fixes the deviation; never carry-forward methodology hygiene |
| #57 INFO (HK-5 near-match Track B) | route to S89 `S89-D-EFF-HK-5-STRUCTURAL-CLOSURE`; expected outcome class |
| #57 FAIL (numerology ruling Track C) | document at coincidence-ruling-corpus.md; W4 dispatches normally |
| #57 PASS (HK-5 EXACT structural identification) | UNEXPECTED-HIGH-LEVERAGE — promote slope_∞_B to canonical_constants.py with substrate-physics provenance; route to S89 `S89-D-EFF-HK-5-STRUCTURAL-IDENTITY-PROMOTION` |

---

## Wave 3c Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md` §"Pre-Registration Completeness" PRDR (Pre-Registration Dry-Run), the following machinery pins are enumerated at plan-freeze BEFORE dispatch. Any free parameter not listed here triggers Class-8 PRU detection at `_pru_cardinality_audit.py`.

### §W3c-29 machinery enumeration (12 pins; see §W3c-29 machinery table above)
- L_max, tau_fold, regulator_atlas, eta_residual_tol, gv_lower_bound, ratio_target, ratio_tol, eta_method, gv_method, cac_offset_per_R, J_parity_grading_op, A_F_decomp, spectrum_cache_path, output_npz, output_png

### §W3c-30 machinery enumeration (8 pins; see §W3c-30 machinery table above)
- wave_class, producing_ops_allowlist, producing_ops_forbidden, target_files (5-tuple), input_pin_map, dual_sha_closure_target, allowlist_row_template, output_verdict_line

### §W3c-57 machinery enumeration (15 pins; see §W3c-57 machinery table above)
- slope_inf_B_observed, slope_inf_A_observed, tau_fold, hk_5_form_canonical, hk_5_at_tau_fold, pass_threshold_absolute, info_threshold_absolute, tau_anchor_candidate_set, algebraic_identity_search_grid, algebraic_identity_match_tol, sage_method, triple_prior, ratio_cross_check, output_npz, output_png

**Total Wave 3c machinery pins**: 35 across 3 gate blocks; PRDR cardinality audit target = 35 (zero unpinned free parameters).

---

## Wave 3c Input-SHA Ledger

Per `gate-verdicts.md` and `epistemic-discipline.md` §"Source Reconciliation", the audit_sha256 of each Wave 3c gate is computed over the gate's INPUT-PIN MAP at plan-freeze time. The map below enumerates input-SHA pin sources:

### §W3c-29 input pins (10 sources)
| Pin | Source | SHA at plan-freeze |
|:----|:-------|:-------------------|
| `canonical_constants.py:tau_fold` | computations/canonical_constants.py | `<pinned at dispatch>` |
| `canonical_constants.py:w0_FW` | computations/canonical_constants.py | `<pinned at dispatch>` |
| `canonical_constants.py:gv_canonical_difference_FW` | computations/canonical_constants.py (S87 W8 promoted) | `<pinned at dispatch>` |
| `canonical_constants.py:max_pair_ratio_A_5_FW` | computations/canonical_constants.py (S87 W8 promoted) | `<pinned at dispatch>` |
| `permanent-results-registry.md §VII.AF.1` | sessions/permanent-results-registry.md (W-5 cross-pillar bridge LANDED) | `<pinned at dispatch>` |
| `permanent-results-registry.md §VII.AF.2 + §VII.P-v2` | W11-1 V_4 supersession PERMANENT | `<pinned at dispatch>` |
| `regulator-convention-lockdown.md §"Rule"` | DR3 demarcation theorem CAC binding form | `<pinned at dispatch>` |
| `regulator-pin-discipline.md §"Class-(c) W-11 RULE-2"` | even Seeley-DeWitt parity-blindness theorem STRENGTHENED | `<pinned at dispatch>` |
| `s84_spectrum_cache_L12_tau019.npz` | computations/s84_spectrum_cache_L12_tau019.npz | `<pinned at dispatch>` |
| `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` | (W-5 calibration cited; structural background) | `<pinned at dispatch>` |

### §W3c-30 input pins (4 sources)
| Pin | Source | SHA at plan-freeze |
|:----|:-------|:-------------------|
| `s87_gate_verdicts.txt W5-1 + W5-3 + W5-4 + W5-5 lines` | computations/s87_gate_verdicts.txt | `<pinned at dispatch>` |
| `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` | S86 W1c-5 all-3-lines-retained discipline | `<pinned at dispatch>` |
| `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"` | METHODOLOGY-class dispatch protocol | `<pinned at dispatch>` |
| `methodology-wave-allowlist.md` (pre-edit) | append-only allowlist; SHA over pre-edit content | `<pinned at dispatch>` |

### §W3c-57 input pins (6 sources)
| Pin | Source | SHA at plan-freeze |
|:----|:-------|:-------------------|
| `s87_w1b_3_richardson_extrapolation.npz keys slope_inf_A + slope_inf_B` | computations/s87_w1b_3_*.npz | `<pinned at dispatch>` |
| `canonical_constants.py:tau_fold` | computations/canonical_constants.py | `<pinned at dispatch>` |
| `s87_w1b_3 verdict-line` | computations/s87_gate_verdicts.txt | `<pinned at dispatch>` |
| `HK-5 form canonical reference` | W1b-3 substrate-physics derivation; HK-5 family per `regulator-pin-discipline.md` | `<pinned at dispatch>` |
| `epistemic-discipline.md §"What Does NOT Count as Evidence" item 4` | analogy-without-quantitative-backing exclusion | `<pinned at dispatch>` |
| `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator pattern"` | extended to triple-prior here | `<pinned at dispatch>` |

**No agent-memory pins anywhere in Wave 3c** — per AMRI Test 1 closure (`agent-standards.md` §"Calibration instance — S87 W0 plan-w13.md AMRI fix"), agent-memory file paths are NEVER input-pin sources. All 20 Wave 3c input pins source from canonical project artifacts (canonical_constants.py / sessions/ / .claude/rules/ / computations/).

**audit_sha256 closure**: each gate's audit_sha256 is computed via `closure_hash(input_pin_map)` per `computations/script-template.py append_verdict()` pattern; uniqueness verified at v3-closure-recovery sig_5 audit; per-gate-distinct guaranteed by per-gate identity keys (`_gate_id`, `_wp_id`, `_scheme`, `_convention`) embedded in the pinmap.

---

## Forward-looking notes

1. **#29 PRIMARY ownership rationale**: lizzi-spectral-functional-theorist holds the FUNCTIONAL-INDEPENDENT vs SCHEME-DEPENDENT classification authority across the framework (per agent-card §"Cosmological Constant Expertise"). The (η=0, GV≠0) regulator-class-invariance audit IS the canonical lizzi-signature test: take the same substrate observable, evaluate under multiple regulators, classify what survives (FUNCTIONAL-INDEPENDENT) and what depends on the choice (SCHEME-DEPENDENT). connes-ncg-theorist co-authors the NCG-axiomatic verification of even Seeley-DeWitt parity-blindness theorem applicability to A_5_extended.

2. **#30 hygiene-only scope**: gen-physicist owns the methodology hygiene because the deliverable is a script-architecture refactor + rule-file edit — NOT new physics. The METHODOLOGY-class M3 substrate is verbatim-extract from S87 W5-1 audit-trail observation; gen-physicist's role is to land the verbatim observation as a permanent rule-file structure without introducing novel derivation.

3. **#57 PRIMARY ownership rationale**: the d_eff anchor convention audit IS a spectral-functional question — does the W1b-3 Richardson L^{-3} extrapolated slope under Conv B baseline (HK-5 form) admit a closed-form structural identity? lizzi-spectral-functional-theorist is the framework's HK-form authority. connes-ncg-theorist co-authors the NCG-axiomatic verification (Connes-Moscovici 1995 §III.4 dim-spectrum residue formula applicability).

4. **Algebra-axis orthogonality K-counter is at K=3 (MANDATORY)** per `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter". None of the three Wave 3c gates introduce cross-corner co-primary structure tags (#29 = single corner II algebra-INVARIANT spectrum-only; #30 = methodology-floor; #57 = single corner II algebra-INVARIANT Mellin-pole). No registry-write hygiene halt expected.

5. **Substrate-first canonical sourcing discipline**: all three gates source from substrate-first canonical artifacts (computations/ npz files, canonical_constants.py, sessions/permanent-results-registry.md). No external-paper canonical citations; no placeholder pins; SUBSTRATE-FIRST-PROVENANCE sub-audit clears all three at dispatch.

6. **PRU cardinality at plan-freeze**: Wave 3c declares 35 machinery pins across 3 gates with zero unpinned free parameters. PRU cardinality audit target = 35; D_PRU_raw = 0 expected at plan-freeze.

7. **Publication-precision pre-registration**: #29 uses `eta_residual_tol = 1e-12` (full float64 publication); #57 uses `pass_threshold_absolute = 1e-12` (full float64) and `info_threshold_absolute = 1e-3` (relaxed near-match band). #30 is METHODOLOGY-class, no numerical threshold.

8. **High-density workshop template potential**: if #29 + #57 BOTH PASS, the wave's structural harvest could include (a) registry-§VII candidate at the FUNCTIONAL-INDEPENDENT vs SCHEME-DEPENDENT layer (W-13 4-corner classification §VII.U.2 + algebra-axis orthogonality cross-link), (b) methodology rule-file extension (cross-link to `cross-pillar-bridge-anatomy.md` K-counter at K=2), (c) coincidence-ruling-corpus.md update, (d) calibration corpus entry for the dual triple-prior pattern in #57. Per `agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE T2-5, multi-output decomposition slots pre-identified at plan-freeze.

---

**END Wave 3c plan.** Ready for plan-freeze + dispatch. PRDR cardinality audit + SOURCE-RECON + SUBSTRATE-FIRST-PROVENANCE sub-audits expected to clear at plan-freeze; dispatch routes #29 + #57 to lizzi-spectral-functional-theorist (parallel COMPUTE-class), #30 to gen-physicist (METHODOLOGY-class orchestrator-direct-write, skip /rclab-coordinate compute-mode per `wave-classification.md` §"Dispatch consequences").
