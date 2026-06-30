# Session 86 Synthesis: W3 Prerequisite-Cascade Diagnosis + Dual-SHA Mechanical-Closure Precedent

**Date**: 2026-04-27
**Agent**: gen-physicist (workhorse)
**Slot**: 1b S-13
**Source Documents**:
- `sessions/archive/session-86/session-86-w3-workingpaper.md`
- `computations/s86_w3_pre_reg_inc_closure.py`
- `computations/s86_gate_verdicts.txt` (lines 19, 22, 24, 89, 91, 95, 118, 120, 122, 124, 126, 128 + companion comment rows)
- `.claude/rules/gate-verdicts.md`
- `.claude/rules/v3-closure-recovery.md`
- `.claude/rules/agent-standards.md` (target for proposed extension)
- `.claude/rules/epistemic-discipline.md` (PRU + SOURCE-RECON + Publication-Precision precedent)

---

## I. Session Outcome

W3 closed 6 / 6 PRE-REG-INCOMPLETE via orchestrator-authored mechanical closure (`computations/s86_w3_pre_reg_inc_closure.py`). Diagnosis (a) "L=10 cache structural common cause" is REJECTED — only 1 of 5 blocking prereqs (C14) is actually a cache-content defect; the remaining four (C9, C10, C12, C19) trace to four heterogeneous root-cause classes. Diagnosis (b) "methodology-discipline cluster" is PARTIALLY ACCEPTED but only as a covering set for the four non-cache prereqs; no single retrofit closes all five. Dual-SHA precedent VALIDATES: 6 unique `audit_sha256` values + 1 shared `content_sha256` is canonical dual-SHA semantics under the gate-verdicts schema, and the orchestrator-authored mechanical-closure pattern is rule-compliant when (i) verdicts are FAIL/PRE-REG-INC, (ii) the closure script computes `audit_sha256` from a per-gate-distinct pinmap, and (iii) the closure preserves the audit-trail provenance back to the upstream prereq state. Proposed rule extension: `mechanical-closure-discipline.md` (drafted as code block in §V).

---

## II. Key Results

### Result 1: Prerequisite-cascade root-cause taxonomy is heterogeneous, not single-source

**Result**: GEOMETRIC (audit-topology classification, no substrate observation).

The five blocking prereqs that cascaded into the 6/6 W3 PRE-REG-INC outcome decompose into four distinct root-cause classes:

| Prereq | Verdict (s86_gate_verdicts.txt) | Root-cause class | Cache-related? |
|:-------|:---------------------------------|:-----------------|:---------------|
| C9 `S86-MELLIN-HEAT-KERNEL-INFRA` (line 95) | FAIL value=9.456 | Numerical convergence (chi^2/dof > INFO_CHI2_MAX=5; MB vs direct-truncation a_n disagree at L=10) | NO — both methods consume the same cache; disagreement is method-internal |
| C10 `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (line 91) | INFO value=2.81e5+0j | Numerical calibration (off-pole Hankel contour magnitude lands in INFO band, not PASS band) | NO — calibration of the analytic-continuation contour |
| C12 `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` (line 89) | FAIL value=1.083e-15 | Plan-authoring threshold defect (`|b2 - 2·b3|/|b2|` metric vs canonical `|ratio - 2|` — algebraic factor-2 mismatch at machine-epsilon floor; per `.claude/rules/epistemic-discipline.md` Canonical-metric pin extension, S86 W2-4 calibration corpus entry) | NO — refactor is bit-exact; FAIL is precision-comparison artifact |
| C14 `S86-LAMBDA-TOP-DIRECT-EXTRACTION` (line 19) | FAIL value='no_eigvals_in_cache' | Cache-content defect (sub2 fails because cache holds per-L moment summaries not raw eigvals; sub3-sub6 cascade-fail from sub2) | YES — single member of the cache-defect class |
| C19 `S86-K-FLOOR-K-WALL-LAND` (line 24) | FAIL value='upstream_W5_D.4_FAIL_no_K_floor_K_wall_values' | Upstream-registry missing (K_floor / K_wall canonical_constants not registered; W5 D.4 derivation absent) | NO — registry / derivation chain |

C17 `S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION` (line 22) is the lone PASS prereq (value=2.035, BdG channel) and appears in W3-5's required set without unblocking it.

**Diagnosis (a) test — substitution chain**:
```
Definition 1: cache_root_cause(g)  = TRUE iff producing-script FAIL semantic = "raw eigvals absent at L=10 from cache"
Definition 2: total_blockers       = {C9, C10, C12, C14, C19}     (5 elements)
Definition 3: (a) PASS criterion   = |{g in total_blockers : cache_root_cause(g)}| / 5 >= 0.6  (≥3 of 5)

Substitution:
  C9:  cache_root_cause = FALSE  (chi^2/dof exceedance is a method-disagreement, not cache-miss)
  C10: cache_root_cause = FALSE  (off-pole Hankel calibration; cache load succeeds)
  C12: cache_root_cause = FALSE  (refactor is bit-exact at L_max=8/10/12; rel_err = 1.083e-15 is float-eps factor-2 artifact)
  C14: cache_root_cause = TRUE   (sub2 fails because raw eigvals key absent from .npz)
  C19: cache_root_cause = FALSE  (W5 D.4 K_floor/K_wall derivation never produced)

Simplify: |{g : cache_root_cause(g)}| = 1 = |{C14}|
Direction: 1 / 5 = 0.2 < 0.6  ⇒  Diagnosis (a) FAILS its criterion.

Conclusion: REJECTED. Cache rebuild closes 1 / 5 prereqs, opens 0 / 5 of the remaining four.
```

**Diagnosis (b) test — substitution chain**:
```
Definition 1: methodology_class(g)  = one of {numerical_convergence, plan_authoring, upstream_registry, cache_content}
Definition 2: methodology_retrofit  = (i) Mellin/heat-kernel scheme reconciliation + (ii) plan-authoring metric audit + (iii) registry-write completion
Definition 3: (b) PASS criterion    = retrofit closes ≥3 of 5 prereqs WITHOUT cache rebuild

Substitution:
  C9:  retrofit (i) [scheme reconciliation: re-derive a_n^Mellin-Barnes vs a_n^truncated convergence band]      ⇒ closeable
  C10: retrofit (i) [contour calibration: tighten Hankel off-pole stride to land in PASS band]                  ⇒ closeable
  C12: retrofit (ii) [adopt canonical |ratio - 2| metric per epistemic-discipline.md S86 W2-4 calibration]      ⇒ closeable
  C14: retrofit (iv-not-listed) [cache REGENERATION storing raw eigvals]                                        ⇒ NOT closeable by methodology alone
  C19: retrofit (iii) [land W5 D.4 derivation, register K_floor / K_wall in canonical_constants.py]             ⇒ closeable

Simplify: |{g : closeable}| = 4 = |{C9, C10, C12, C19}|
Direction: 4 / 5 = 0.8 >= 0.6  ⇒  Diagnosis (b) PASSES its criterion.

Conclusion: PARTIALLY ACCEPTED. Methodology retrofit closes 4 / 5; the remaining one (C14)
is the lone genuine cache-content item.
```

**Adjudication**: The framework is NOT facing a single L=10 cache structural collapse. It is facing four independent methodology-discipline issues + one cache-content issue. S87 W3 re-attempt strategy must therefore be a five-prong remediation, not a single-prong cache rebuild. The cache rebuild is necessary for C14 and only C14; assuming it closes the other four would be wrong-rooting.

### Result 2: Dual-SHA mechanical closure preserves audit uniqueness while sharing content_sha256

**Result**: GEOMETRIC (verdict-file audit-trail invariant).

Verified via Python:
- All 6 W3 `audit_sha256` values are pairwise distinct (count = 6 / 6 unique).
- All 6 W3 verdict lines carry the same `content_sha256` = `05071d10327d7f32fe88eb9d63278f3a4f737ca1f87280a3c51a5f8266c01686`.
- This is exactly the dual-SHA semantic the closure script implements: `audit_sha256 = sha256(script_bytes || canonical_bytes || pinmap_json)` where the pinmap embeds per-gate identity keys (`_gate_id`, `_wp_id`, `_scheme`, `_convention`) plus the per-gate required-prereq-state map; `content_sha256 = sha256(script_bytes)` is the script-only hash and is therefore identical across all 6 verdict lines emitted by the same closure script.

**Validation against `.claude/rules/gate-verdicts.md`**: PASS. The schema requires the canonical line to carry the full 64-character closure SHA (`audit_sha256` in dual-SHA form per S84+ `schema_version=S84+`). The 6 W3 lines satisfy this; the verdict-file consolidator (`_consolidate_intake.py`, ≥40-char minimum) accepts them.

**Validation against `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS**:
- Class 1 (convention-shopping): NOT triggered — no convention tag was changed; the W3 verdicts are FAIL/PRE-REG-INC, not coerced PASSes.
- Class 2 (iterate-until-PASS): NOT triggered — the closure script ran once; no re-runs to reach a target verdict occurred.
- Class 3 (post-hoc pre-registration editing): NOT triggered — plan thresholds are unchanged.
- Class 4 (ansatz-forced PASS): NOT triggered — the verdict file was appended via `open("a")` from a Python script (compliant with rule), and the verdicts emitted are honest FAIL declarations, NOT manually-coerced PASSes.

**Validation against v3 ladder sig_5** (`audit_sha256` uniqueness): the W3 sub-set is CLEAR (6 / 6 unique). However, an audit of the full `s86_gate_verdicts.txt` revealed THREE pre-existing duplicate `audit_sha256` values not in W3 — `aeb3441c...` (PERM-LAND-17 + PERM-LAND-17-RECONCILIATION at lines 34 + 61), `a88ff16e...` (MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION at lines 85 + 93), `df1726c4...` (LATTICE-SPACING-IMMUNIZATION-CANDIDATE at lines 157 + 160). These are sig_5 ladder violations from OTHER waves and are flagged here as observation; they are not within this dispatch's adjudication scope but should be carry-forwarded.

### Result 3: Pre-existing closure-script bytes drift after verdict emission (audit-provenance hazard)

**Result**: GEOMETRIC (verdict-file audit-trail invariant; not a substrate observation).

Cross-check verification:
- Recomputed `sha256(s86_w3_pre_reg_inc_closure.py)` at synthesis time = `9252e6710fca3f7c0617536cdaffdd2ccc436bb12bf440f60ac96fa58ba4c9b0`.
- The 6 W3 verdict lines carry `content_sha256 = 05071d10327d7f32fe88eb9d63278f3a4f737ca1f87280a3c51a5f8266c01686`.
- These do NOT match.

**Interpretation**: The closure script bytes have been edited AFTER the W3 verdicts were emitted. This does NOT invalidate the W3 verdicts (the `audit_sha256` values are still valid commitments to the script-state-at-emission-time), but it does mean a re-run of `s86_w3_pre_reg_inc_closure.py` today would produce a DIFFERENT `content_sha256` AND different `audit_sha256` values (because the script-bytes feed both hashes). The script's idempotent-recovery branch (lines 309-321) handles this: it parses existing verdict-file lines and re-uses the recorded SHAs rather than recomputing, but only for gates already in the file. New W3-style emissions would diverge from the original audit trail.

This is a forward-looking hazard for any orchestrator-authored closure script that may be edited post-emission. The proposed rule (§V below) addresses it by requiring closure scripts to be `chmod -w` after first execution OR to commit a tagged immutable snapshot of the script bytes alongside the verdict-file emission.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (W3-1) | FAIL (PRE-REG-INC) | value='PRE-REG-INC_blocked_by_C9_FAIL_C10_INFO' |
| `S86-W0-7-MB-RE-EMIT` (W3-2) | FAIL (PRE-REG-INC) | value='PRE-REG-INC_blocked_by_C10_INFO' |
| `S86-W0-11-MB-RE-EMIT` (W3-3) | FAIL (PRE-REG-INC) | value='PRE-REG-INC_blocked_by_C9_FAIL' |
| `S86-W0-20-MB-RE-EMIT` (W3-4) | FAIL (PRE-REG-INC) | value='PRE-REG-INC_blocked_by_C10_INFO' |
| `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` (W3-5) | FAIL (PRE-REG-INC) | value='PRE-REG-INC_blocked_by_C12_FAIL_C19_FAIL' |
| `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION` (W3-6) | FAIL (PRE-REG-INC) | value='PRE-REG-INC_blocked_by_C14_FAIL' |

All 6 W3 verdicts are accepted as honest PRE-REG-INC closures per `.claude/rules/gate-verdicts.md` §"A gate that cannot be evaluated because its producing machinery is unpinned (PRU Class 8) is NOT a FAIL — it is PRE-REG-INCOMPLETE." The `value='PRE-REG-INC_blocked_by_*'` string-pattern is the canonical descriptive form per S86 precedent (lines 19 + 24 of `s86_gate_verdicts.txt`).

Pre-registration outcome (per dispatch spec): **PASS** — proposed rule extension below distinguishes honest-mechanical-closure from S82/S84 task-complete-lie pattern via three structural invariants (verdict honesty, per-gate-distinct audit_sha256, and audit-trail provenance preservation). The rule extension preserves the W3 honesty pattern by construction.

---

## IV. Structural Implications

### IV.1 Constraint-map state at S86 boundary

No mechanism in the constraint map was eliminated, confirmed, or had its solution-space region re-mapped by W3 at S86. The wave produced no new structural constraints; the constraint surface is unchanged. Six gate corridors (T9, W0-7-MB, W0-11-MB, W0-20-MB, C13, C43) remain UNTESTED. Per `.claude/rules/epistemic-discipline.md` §"Evidence Hierarchy": this is a no-information outcome, not a corridor closure.

### IV.2 Mechanical-closure pattern fills a documented gap in `.claude/rules/`

The repository's existing rule corpus addresses:
- `gate-verdicts.md` — verdict-line schema, dual-SHA pin format
- `v3-closure-recovery.md` — Stage-1/2/3 fallback procedure, 4-item PROHIBITED_ACTIONS
- `agent-standards.md` — completion-verification (`§"Completion Verification (compute-mode dispatches)"`) addressing the S82/S84 task-complete-lie pattern
- `epistemic-discipline.md` — PRU + SOURCE-RECON + Publication-Precision pre-registration

But none of these documents the orchestrator-authored mechanical-closure pattern as a first-class operation. The W3 implementation occupies a permitted-but-unspecified corner of the rule-space:
- It is NOT a Stage-1 re-dispatch (no specialist-agent re-launch)
- It is NOT a Stage-2 V3-NON-COMPLIANT fallback (W3 verdicts are valid PRE-REG-INC, not unrecoverable)
- It is NOT a Stage-3 user-trigger event (no manual intervention required)
- It is NOT a PROHIBITED_ACTIONS violation (no PASS-coercion)

The rule extension proposed in §V formalizes this as a fourth class of recovery action: **mechanical metadata closure** for upstream-blocked downstream gates.

### IV.3 The audit-trail provenance signature is `value='upstream_*'` or `value='PRE-REG-INC_blocked_by_*'`

S86 already established a precedent for upstream-blocked verdict strings:
- Line 19 (`S86-LAMBDA-TOP-DIRECT-EXTRACTION`): `value='no_eigvals_in_cache'` — upstream is the spectral-cache regeneration
- Line 24 (`S86-K-FLOOR-K-WALL-LAND`): `value='upstream_W5_D.4_FAIL_no_K_floor_K_wall_values'` — upstream is W5 D.4 derivation
- Lines 118, 120, 122, 124, 126, 128 (all 6 W3): `value='PRE-REG-INC_blocked_by_<symbol>_<status>_*'` — upstream is the W2 / W0c prereq set

This descriptive-value-string pattern is the audit-trail signature that distinguishes honest mechanical closure from a coerced PASS. A future audit script (`_mechanical_closure_audit.py`, see §V Carry-Forward V.4) can grep canonical lines for `value='upstream_*'` or `value='PRE-REG-INC_*'` and verify per-gate that:
1. The named upstream gate exists and has the named status
2. The producing script's `audit_sha256` is per-gate-distinct
3. The verdict status is FAIL (not PASS)

### IV.4 Sig_5 ladder pre-existing duplicates flagged for next-session attention

Three duplicate `audit_sha256` pairs exist in `s86_gate_verdicts.txt` from waves outside W3:
- `aeb3441c...` shared by `S86-W0-PERM-LAND-17` (line 34) and `S86-W0-PERM-LAND-17-RECONCILIATION` (line 61)
- `a88ff16e...` shared by two emissions of `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` (lines 85 + 93)
- `df1726c4...` shared by two emissions of `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE` (lines 157 + 160)

Per `.claude/rules/v3-closure-recovery.md` sig_5 remediation: each duplicate indicates either (a) hardcoded SHA in the producing script OR (b) a gate emitted twice from the same input-pin map. Distinguishing requires inspecting the producing scripts. This is OUT OF SCOPE for the current dispatch (gen-physicist 1b S-13) but is recorded as Carry-Forward V.5.

### IV.5 Substrate framing

Per `.claude/rules/phononic-framing.md`: this synthesis reports on AUDIT TOPOLOGY, not on substrate spectral content. The gate corridors that W3 was structured to interrogate — Mellin-cone analytic continuation of D_K's spectral functional, asymptotic stability of the regularized spectral action `S_zeta_E^cont(L_max) / ζ_D(3, L_max)`, cluster-span identity `b_pow(span_2) = 2 · b_pow(span_3)` across the K-corridor, empirical-vs-Casimir Λ disambiguation under `Λ_actual = λ_max(L=10)` — all remain UNCHARACTERIZED at the S86 boundary. These are structural questions about the substrate's spectral content under different regulator conventions; their answers exist (the substrate is what it is), but the audit trail does not yet record them. The closure pattern is a HONEST RECORDING that the questions remain open, not a substantive substrate observation.

---

## V. Carry-Forward Computations

### V.1. L=10 spectral-eigenvalue cache regeneration with raw eigvals storage (CLOSES C14 ONLY)

- **What**: Regenerate `computations/data/dk_spectral_cache_L_max_<8,10,12>.npz` with the `eigvals` (full complex array) AND `eigenvalues` (legacy) keys populated, so that `s86_w0c_lambda_top_extract.py` sub2-sub6 can extract the raw eigvalue array. Run on GPU via `torch.linalg.eigvals` per `.claude/rules/computation-environment.md` §"Heavy Linear Algebra — Prefer GPU"; matrix dim at L=10 is 155,984 — well within 17 GB VRAM. Verify post-write that `np.load(cache_path).keys()` contains `'eigvals'`.
- **Inputs**: D_K spectral construction at L_max=10 (per S58+ canonical; see `mcp__knowledge__get_constant("M_KK")` and the spectral-action infrastructure); GPU venv `phonon-exflation-sim/.venv312/Scripts/python.exe`; expected output count = 155,984 (per `EXPECTED_COUNT` in `s86_w0c_lambda_top_extract.py` line 78).
- **Gate**: Re-emit `S86-LAMBDA-TOP-DIRECT-EXTRACTION` (carry-forward S87-LAMBDA-TOP-DIRECT-EXTRACTION-RERUN per `computations/_consolidate_intake.py` open-channel registry); PASS iff all 6 sub-criteria PASS (cache-integrity, count==155984, hermiticity max|imag|<1e-10, magnitude band [4.5,6.5]·M_KK, asymptotic L=10/L=12 ∈ [0.85,1.0], 6-sig-fig stability under reload).
- **Effort**: 4-6 hours, 1 agent session (connes-ncg-theorist or workhorse). Bottleneck is the GPU eigvals at L=10 (estimated ~30s wall time per L) plus the .npz write + sha256 verification.

### V.2. Mellin-Barnes vs direct-truncation a_n scheme reconciliation (CLOSES C9, partially C10)

- **What**: Re-derive the scheme reconciliation between `a_n^MB` and `a_n^truncated` at L_max=10 across regulators {ζ, Pauli-Villars, Mellin}. The current chi^2/dof = 9.456 at L=10 is interpreted as either (i) a genuine method-disagreement (one of the two methods is wrong), or (ii) a calibration drift in a shared sub-routine (e.g., the SD-subtraction normalization). Use `.claude/rules/regulator-pin-discipline.md` to ensure all `a_n` references are tagged `a_n^{<regulator>}`; cross-check at machine precision via `mcp__sage__sage_eval` on the simplest 2x2 illustrative case.
- **Inputs**: `computations/s86_w2_c9_mellin_heat_kernel_infra.py` (current FAIL=9.456 producer); regulator specifications per `regulator-pin-discipline.md`; cross-check via the C10 `analytic_zeta` at the same s-value.
- **Gate**: Re-emit `S86-MELLIN-HEAT-KERNEL-INFRA` (carry-forward S87-MELLIN-HK-INFRA-RERUN); PASS iff chi^2/dof ≤ PASS_CHI2_MAX (=5 per plan §10) AND `min(ratio_per_class) ≤ PASS_RATIO_MAX`. If the reconciliation also tightens the C10 off-pole Hankel calibration to land in PASS band (analytic_zeta(s=4) returns finite R_inf with χ²/dof ≤ 5), then C10 promotes from INFO to PASS as a side benefit.
- **Effort**: 4-6 hours, 1 agent session (lizzi-spectral-functional-theorist). The bottleneck is dimensional/regulator analysis, not compute time.

### V.3. Adopt canonical |ratio - 2| metric for cluster-span gates (CLOSES C12)

- **What**: Edit `computations/s86_w2_c12_cluster_span_self_test.py` to compute `dev = |ratio - 2|` where `ratio = b2 / b3`, NOT `dev = |b2 - 2*b3|/|b2|` (which carries an algebraic factor-2 mismatch with the W0-3 canonical metric, per `.claude/rules/epistemic-discipline.md` §Source Reconciliation, S86 W2-4 calibration corpus entry). Apply the canonical PASS threshold `dev < 1e-14` (≈45 × float_eps) per the same rule. The refactor is bit-exact at L_max=8/10/12 — only the metric formula and threshold change.
- **Inputs**: `s86_w2_c12_cluster_span_self_test.py` lines 240-275 (FAIL=1.083e-15 producer); `epistemic-discipline.md` Canonical-metric pin extension; `s85_gate_verdicts.txt` row `S85-CC-5-LMAX-ASYMPTOTIC-REFIT` for canonical-anchor cross-check (W0-3 PASS at value=2.220e-15 under canonical metric).
- **Gate**: Re-emit `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` (carry-forward S87-CLUSTER-SPAN-EXTRACTOR-METRIC-FIX); PASS iff `max(|ratio - 2|) < 1e-14` across L_max ∈ {8, 10, 12}. This is a refactor gate; the underlying physics is unchanged.
- **Effort**: 1-2 hours, 1 agent session (workhorse). The substantive work is documenting the metric change in the `# (local)` tag and verifying against the W0-3 canonical anchor.

### V.4. W5 D.4 K_floor / K_wall derivation + canonical_constants registration (CLOSES C19)

- **What**: Land the W5 D.4 derivation that produces `K_floor` and `K_wall` values, then register both as canonical constants via `mcp__knowledge__update_constant` AND `computations/canonical_constants.py` with full provenance (session, source gate, comment). The C19 verdict `value='upstream_W5_D.4_FAIL_no_K_floor_K_wall_values'` is the explicit declaration that this prereq is missing.
- **Inputs**: W5 D.4 plan block (per `sessions/session-plan/session-86-plan-w5.md` §D.4 — verify presence; if absent, this is a Class-8 PRU plan-authoring defect); the canonical-constants module `computations/canonical_constants.py`; the registry file `sessions/framework/registry/_registry-template.md`-derived structure.
- **Gate**: Re-emit `S86-K-FLOOR-K-WALL-LAND` (carry-forward S87-K-FLOOR-K-WALL-LAND); PASS iff both K_floor and K_wall are registered with non-null values, full SHA-pinned provenance, and the canonical-constants audit (`/weave --update`) reports zero violations on the registration lines. Also unblocks W3-5 (C13) cluster-span K-corridor extension if combined with V.3.
- **Effort**: 3-4 hours, 1 agent session (kitaev-topological-theorist or volovik-superfluid-universe-theorist; the K_floor/K_wall derivation typically lives in the BdG / vortex-channel domain).

### V.5. Sig_5 duplicate-audit_sha256 cleanup for non-W3 gates (RESOLVES LADDER VIOLATION)

- **What**: Inspect the producing scripts for the three gate-pairs sharing duplicate `audit_sha256`:
  - `S86-W0-PERM-LAND-17` (line 34) + `S86-W0-PERM-LAND-17-RECONCILIATION` (line 61) — audit `aeb3441c...`
  - `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` (lines 85 + 93) — audit `a88ff16e...`
  - `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE` (lines 157 + 160) — audit `df1726c4...`
  Per `v3-closure-recovery.md` sig_5 remediation, determine for each pair whether (a) the producing script hardcoded the audit SHA OR (b) the gate was emitted twice with bit-identical input-pin maps. If (a), patch the script to compute the audit hash from the closure pinmap and re-emit. If (b), one of the two lines is canonical and the other is a redundant re-run; mark the redundant line with a `# DUPLICATE` companion comment but DO NOT delete (the verdict file is append-only per `gate-verdicts.md`).
- **Inputs**: `computations/s86_w0_perm_land_17*.py`, `computations/s86_w*_mellin_multiplier_infinite_vector*.py`, `computations/s86_w*_lattice_spacing_immunization_candidate*.py`; `.claude/rules/v3-closure-recovery.md` Stage-1 sig_5 remediation procedure.
- **Gate**: Sig_5 ladder check (no individual gate ID; ladder sub-signal). PASS iff `len(set(audit_sha256_canonical_lines)) == len(audit_sha256_canonical_lines)` after remediation.
- **Effort**: 2-3 hours, 1 agent session (workhorse). Three gate-pairs to inspect; each takes ~30 minutes to diagnose + remediate.

### V.6. Mechanical-closure-discipline rule file (DRAFT) — PROPOSED FOR ORCHESTRATOR REVIEW

- **What**: Install the proposed rule file `.claude/rules/mechanical-closure-discipline.md` (drafted as code block immediately below) as a permanent epistemic rule. The rule formalizes when an orchestrator-authored mechanical-closure script is acceptable, when it indicates a planning defect, and what audit-trail signature distinguishes it from the S82/S84 task-complete-lie pattern. The rule is FORWARD-LOOKING; existing W3 closures need no remediation under it.
- **Inputs**: this synthesis (§II.2 dual-SHA validation, §III gate-verdicts adjudication, §IV.2 rule-corpus gap analysis, §IV.3 audit-trail signature characterization); cross-references to `.claude/rules/agent-standards.md` §"Completion Verification (compute-mode dispatches)" and `.claude/rules/v3-closure-recovery.md`.
- **Gate**: New gate ID `S87-MECHANICAL-CLOSURE-DISCIPLINE-RULE-LANDING`; PASS iff (i) rule file installed at `.claude/rules/mechanical-closure-discipline.md` per drafted text below, (ii) cross-reference added to `.claude/rules/agent-standards.md` §Completion Verification pointing to the new rule, (iii) `_mechanical_closure_audit.py` created and passes a synthetic test on the W3 closure script (verifies all 3 invariants — verdict honesty, per-gate audit uniqueness, audit-trail signature). INFO if the rule lands but `_mechanical_closure_audit.py` is deferred. FAIL only if the orchestrator review finds a missing case the rule does not cover (S87 plan-authoring should re-derive in that case).
- **Effort**: 1-2 hours orchestrator + 1-2 hours implementation (workhorse). Total ~3-4 hours; one orchestrator-driven session to install + one workhorse session to write the audit script.

### Proposed rule-file content (do NOT install directly; orchestrator review required)

```markdown
# Mechanical-Closure Discipline (Orchestrator-Authored Verdict-Line Emission)

> **Provenance**: S86 W3 6/6 PRE-REG-INC closure via `computations/s86_w3_pre_reg_inc_closure.py`,
> 2026-04-26. Validated against `gate-verdicts.md` schema, `v3-closure-recovery.md` PROHIBITED_ACTIONS,
> and v3 ladder sig_5 audit. Synthesis: `sessions/archive/session-86/session-86-1b-s13-gen-physicist.md` §V.6.

## Scope

Orchestrator-authored mechanical-closure scripts emit verdict lines to
`computations/s{N}_gate_verdicts.txt` WITHOUT specialist-agent dispatch
and WITHOUT physics computation. The mechanical closure documents that a
gate could not be evaluated because at least one upstream prerequisite has
verdict ≠ PASS — the gate is structurally untestable at this session.

This rule formalizes the pattern that distinguishes HONEST mechanical
closure from the S82/S84 task-complete-lie failure mode (verdict line
appended without working-paper section, agent reports completion while
final write skipped).

## When mechanical closure IS acceptable

A mechanical-closure script may be authored ONLY when ALL of the
following hold:

1. **Upstream-block topology is the cause**: every gate the script closes
   has ≥1 upstream prerequisite with verdict ≠ PASS, and the plan's
   downstream decision-point table specifies the documented outcome for
   prereq-block (typically "PRE-REG-INC, deferred to S{N+1}"). The plan
   author MUST have anticipated the prereq-block scenario; if the plan
   does not address it, the closure script is post-hoc plan editing
   (PROHIBITED_ACTIONS Class 3) and is FORBIDDEN.

2. **Verdict honesty**: emitted verdicts are FAIL or PRE-REG-INC, NEVER
   PASS. The descriptive value string MUST follow the
   `value='PRE-REG-INC_blocked_by_<symbol>_<status>_*'` or
   `value='upstream_<reason>'` pattern. PASS verdicts from a mechanical
   closure script are PROHIBITED_ACTIONS Class 4 (ansatz-forced PASS).

3. **Per-gate-distinct audit_sha256**: even when multiple gates share a
   prerequisite set (e.g., two gates both blocked solely on C10), the
   pinmap that feeds `audit_sha256` MUST embed per-gate identity keys
   (`_gate_id`, `_wp_id`, `_scheme`, `_convention`) so the resulting
   `audit_sha256` values are pairwise distinct across all gates the
   script closes. Sig_5 ladder uniqueness is preserved by construction.

4. **Audit-trail signature**: the verdict line MUST carry a descriptive
   `value` string that names the blocking prereq and its status. A
   future audit script MUST be able to grep the canonical line and
   verify the named upstream gate exists and has the named status in
   the same verdict file.

5. **Working-paper update is in-script**: the closure script MUST update
   the corresponding working-paper section's `**Status**`, `**Verdict**`,
   `**Results**`, and `**Substrate framing**` blocks IN THE SAME RUN as
   the verdict-line append. A closure script that emits the verdict line
   but skips the working-paper update is the S82/S84 task-complete-lie
   pattern and is FORBIDDEN.

## When mechanical closure indicates a PLANNING DEFECT

If the closure script's covered-gate count ≥ N_PLANNING_DEFECT_THRESHOLD
(pin: 4) of the wave's total gate count, the wave plan was OVER-OPTIMISTIC
about prerequisite landings. This is a Class-8 PRU vulnerability at
plan-authorship time: the planner should have routed the gates into a
later wave conditional on prereq landing, rather than into the current
wave with mechanical-closure deferral.

The closure script remains acceptable AT EXECUTION TIME (preserving the
audit trail honestly), but the next session's planner MUST log this as
a plan-authorship lesson and adjust wave-partitioning policy to avoid
recurrence.

## Audit-trail signature

The canonical verdict-line pattern for a mechanical closure is:

```
{GATE_ID}: FAIL -- value='PRE-REG-INC_blocked_by_<sym1>_<status1>[_<sym2>_<status2>...]' \
  scheme=<plan-pinned scheme> convention=<plan-pinned convention> \
  L_max=<plan-pinned L_max> \
  audit_sha256=<64-char> content_sha256=<64-char> schema_version=S84+
```

Companion comment row:

```
# audit_sha256 companion row: {GATE_ID} audit={short16} content={short16} \
# PRE-REG-INC per session-{N}-plan-w{W}.md §X; deferred to S{N+1}; \
# required prereqs: [<sym1>, <sym2>, ...]; \
# closure_script=computations/s{N}_w{W}_pre_reg_inc_closure.py
```

## Audit script

`computations/_mechanical_closure_audit.py` enforces this rule. It
greps `s{N}_gate_verdicts.txt` canonical lines for the
`value='PRE-REG-INC_blocked_by_*'` or `value='upstream_*'` patterns and
verifies for each match:

  (i) the named upstream gate exists in the same file
 (ii) the named upstream gate's status matches what the closure value
      string asserts
(iii) the closure-line `audit_sha256` is unique across all canonical
      lines in the file
 (iv) the corresponding working-paper section has been updated
      (status != "NOT STARTED", verdict block populated, substrate
      framing block present)

Output: JSON report flagging any closure that fails (i)–(iv).

## Carry-forward script-bytes immutability (forward-looking hazard)

A closure script that is EDITED after emitting verdicts produces a
`content_sha256` mismatch between the script-as-emitted and
script-at-current-time. This does NOT invalidate the previously-emitted
verdicts (the recorded SHAs are commitments to the script-state-at-
emission-time), but it does break re-running the closure script as an
audit-reproducibility tool.

Mitigation (forward-looking): after first execution, mechanical-closure
scripts SHOULD be made read-only (`chmod -w` or filesystem-equivalent),
OR a tagged immutable snapshot (`{script}.frozen-{audit_sha_short}.py`)
should be committed alongside the verdict-file emission. The script's
idempotent-recovery branch (parse-and-reuse of existing verdict-line
SHAs) handles re-runs from this state.

## Cross-references

- `.claude/rules/gate-verdicts.md` — verdict-line schema, dual-SHA pin
- `.claude/rules/v3-closure-recovery.md` — Stage 1/2/3 procedure, PROHIBITED_ACTIONS
- `.claude/rules/agent-standards.md` §"Completion Verification" — S82/S84
  task-complete-lie failure mode this rule prevents
- `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" — PRU
  Class 8 framework; mechanical closure is the in-session honest reporting
  for upstream-blocked PRU-clear gates
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Diagnosis (a) L=10 cache common cause | GEOMETRIC (audit-topology) | REJECTED (1/5 prereqs) | Cache rebuild closes only C14; the other four require independent remediation |
| 2 | Diagnosis (b) methodology-discipline cluster | GEOMETRIC (audit-topology) | PARTIALLY ACCEPTED (4/5 prereqs) | S87 W3 re-attempt is five-prong: V.1 + V.2 + V.3 + V.4 + V.5 |
| 3 | Dual-SHA mechanical-closure preserves audit uniqueness | GEOMETRIC (verdict-file invariant) | VALIDATED | 6/6 W3 audits unique; shared content_sha256 is canonical dual-SHA semantics |
| 4 | Closure-script bytes drift after emission | GEOMETRIC (audit-trail hazard) | FLAGGED | Script edited post-emission; re-run would diverge unless idempotent-recovery branch hits |
| 5 | Sig_5 ladder violations OUTSIDE W3 | GEOMETRIC (verdict-file invariant) | OPEN | 3 duplicate audit_sha256 pairs in non-W3 lines (PERM-LAND-17, MELLIN-MULT, LATTICE-SPACING) |
| 6 | Mechanical-closure rule extension drafted | GEOMETRIC (rule-corpus extension) | PROPOSED | `mechanical-closure-discipline.md` formalizes 5-condition acceptability test; preserves W3 honesty pattern, prevents S82/S84 lie pattern |
| 7 | Substrate spectral content interrogated by W3 | GEOMETRIC (uncharacterized at S86) | UNTESTED | T9, W0-7-MB, W0-11-MB, W0-20-MB, C13, C43 corridors remain open for S87 |
