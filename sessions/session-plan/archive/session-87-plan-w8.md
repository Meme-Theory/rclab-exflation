# Session 87 Plan — Wave 8: cutoff_sqrt Atlas + Sixth Regulator + HBW + η-GV

**Wave owner**: gen-physicist (CF-47..CF-53 attribution per S86 W-8 closure recommending column; CF-65 W-11 single item folded by recommending-agent match per partition manifest §4 wave-owner heuristic)
**Specialist agents for execution**:
  - `gen-physicist` — CF-47 (atlas-propagation pointer-sweep, breadth)
  - `connes-ncg-theorist` — CF-48, CF-49, CF-50, CF-53 (NCG axiom-native + cluster-span + L2 channel work)
  - `lizzi-spectral-functional-theorist` — CF-51, CF-52 (Mellin-cone live + channel independence)
  - `volovik-superfluid-universe-theorist` — CF-65 co-sign (substrate-inheritance falsifier-protocol per `.claude/rules/inheritance-falsifier-protocol.md`)
**Wave class**: COMPUTE-class (per `.claude/rules/wave-classification.md` 4-test conjunction; M1 numerical predicates present, M2 `.py` producing scripts, gate IDs not on methodology-wave-allowlist).
**Carry-forward count**: 8 (CF-47, CF-48, CF-49, CF-50, CF-51, CF-52, CF-53, CF-65).
**Total wall-clock effort estimate**: ~33 hours.
**Concurrent dispatch cap**: ≤ 8 agents (per user-pinned `feedback_dispatch-discipline.md`); this entire wave fits under the cap.

---

## Wave 8 Summary

Wave 8 closes the structural carry-forward bundle from S86 W-8 (cutoff_sqrt GATE A/B/C trio + atlas-cardinality cascade) plus the W-11 single carry-forward (η-GV joint probe regulator-INDEPENDENCE follow-up). The S86 close-state anchor that enters W8 is:

- **GATE A FAIL** at S86 W-8 was canonical-record per pre-registration; α_star ∈ [−1.6, −1.0] across L ∈ {3,5,7,10}, asymptotic α → −2 from Peter-Weyl L^8/960 leading term. Atlas A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} CASCADED to **A_4 = {ζ, Zubarev, SDW, anomaly}**.
- **GATE B PASS** confirmed LAYER 2 axiom-sourcing for cutoff_AL2010 a_0 channel = {dim, fin} (most-minimal load-bearing axiom set).
- **GATE C INFO/FAIL** on f_6 = 0.1 framework-truncated residue MP-abs-conv at s=6 (HBW positive-cone test) indicated the f_6-residue slot decoupling vs. L^8 a_0 channel is unresolved at L_max=3.
- **W-11 η-GV joint probe**: η ≡ 0 EXACTLY across all 5 A_5 regulators (parity-blindness theorem confirmed); GV(C_H) − GV(C_epsH) = −40579.15 (~16 OOM above threshold). Bulletin #1 demoted, Bulletin #2 promoted to permanent wall (§VII.X parity-blindness theorem). The W-11 R1 INFO-flag drove CF-65 follow-up: verify GV-Heitsch is regulator-INDEPENDENT under the surviving A_4 atlas plus cutoff_sqrt as legacy diagnostic.

The W8 wave executes the plumbing consequences of these closures plus one structural-extension gate (sixth regulator). Eight gates total; structural mix is 1 propagation/edit-pass (CF-47), 1 re-run (CF-48), 1 promotion-with-pre-reg (CF-49), 1 audit (CF-50), 2 channel-localization tests (CF-51, CF-52), 1 axiom-native cross-check (CF-53), 1 regulator-INDEPENDENCE follow-up (CF-65).

The wave is COMPUTE-class throughout. Per `.claude/rules/wave-classification.md` §"Strict-conjunction requirement": M1 (numerical PASS predicates) holds across all 8 gates; M2 (`.py` producing scripts) holds; M4 (allowlist membership) FAILS — none of the 8 gate IDs is in `.claude/rules/methodology-wave-allowlist.md`, so M4 routes to COMPUTE fallthrough as expected. Wave classification: **COMPUTE**, partition-honest.

---

## Wave 8 Decision Point Prerequisites

W8 inherits no upstream W7 dependency that gates dispatch. The atlas A_4 reduction was canonical-record at S86 W-8 close (pre-registered); CF-47/48/50 consume the cascade as a SETTLED state, not a gate.

**Files-on-disk verified at plan-freeze (2026-04-27)**:
- `computations/canonical_constants.py` — EXISTS at S86-close state. CF-47 will assess provenance-status of any cutoff_sqrt-tagged constants.
- `computations/s86_gate_verdicts.txt` — EXISTS; contains GATE A FAIL canonical-record verdict line + W-11 η-GV verdict.
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` — EXISTS; W4-2 canonical adjudication source for atlas membership.
- `computations/_cluster_span_extract.py` — EXISTS; importable as `cluster_span(L_max)` per W2-4 module landing.
- `computations/s86_w2_c12_cluster_span_self_test.py` — EXISTS; per W2-4 calibration corpus instance for cluster-span canonical-metric `|ratio − 2|`.
- `computations/s84_spectrum_cache_L12_tau019.npz` — EXISTS; D_K(τ_fold) eigenvalue cache at L_max=12 (consumed by CF-50, CF-65).
- `computations/s84_spectrum_cache_L10_tau019.npz` — EXISTS; D_K(τ_fold) at L_max=10 (consumed by CF-65 per W-11 §1 anchor).
- `computations/s86_w11_eta_gv_joint_probe.py` + `s86_w11_eta_gv_joint_probe.npz` — EXISTS; CF-65 builds on this (extends regulator-independence test to joint η/GV).
- `sessions/permanent-results-registry.md` — EXISTS; CF-49 may target §VII.M layer-membership row if sixth-regulator search produces a candidate.

**Pre-dispatch sanity** (orchestrator-side at plan-freeze, NOT pinned as a gate): grep `computations/s87_gate_verdicts.txt` (if exists) for collisions with the 8 W8 gate IDs; expect zero matches.

---

## §W8-1. S87-CUTOFF-SQRT-ATLAS-PROPAGATION (CF-47)

### 1. Gate ID
`S87-CUTOFF-SQRT-ATLAS-PROPAGATION`

### 2. Trigger
`[VERIFY]` + `[AUDIT]`

### 3. Classification
GEOMETRIC (substrate atlas-cardinality structural propagation; not a phononic excitation gate).

### 4. Hypothesis
After S86 W-8 GATE A FAIL canonical-record, every downstream registry / working-paper / canonical_constants citation of `cutoff_sqrt` as an atlas member admits clean rewrite to A_4 = {ζ, Zubarev, SDW, anomaly}, with cutoff_sqrt downgraded to "legacy diagnostic" (kept for W-11-class regulator-class-independence audits) but never load-bearing in atlas-member operations.

### 5. PASS / FAIL / INFO threshold (RATIO/ABSOLUTE/THEOREM)
- **PASS**: `n_unflagged_residual_cutoff_sqrt_load_bearing_cites = 0` after the edit pass (THEOREM-level; integer count). Every grep hit for `cutoff_sqrt` in the four target documents (`session-86-w4-2-workingpaper.md`, `session-86-w6-workingpaper.md`, `session-86-w12-workingpaper.md`, `session-86-w13-workingpaper.md`) plus `canonical_constants.py` plus `sessions/framework/registry/cutoff-sqrt-adjudication.md` is either (a) flagged with `[LEGACY: cascade A_5→A_4 per S86 W-8 GATE A FAIL]` or (b) explicitly tagged as a regulator-class-independence diagnostic per W-11 calibration.
- **FAIL**: `n_unflagged_residual_cutoff_sqrt_load_bearing_cites ≥ 1` after the pass. Indicates the propagation missed a downstream consumer.
- **INFO**: `0 < n_unflagged_residual_cutoff_sqrt_load_bearing_cites ≤ 2` AND every residual is in a curated framework-folder root file (where bulk edits are forbidden per `feedback_framework-hygiene.md`). Records the residual as a manual-review carry-forward to S88.

Tolerance rule: ABSOLUTE (integer count, no float comparison).

### 6. Machinery pin (PRDR — `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness)
- `N_eval`: N/A (mechanical pointer-sweep + edit pass; no eigenvalue computation)
- `L_max`: N/A
- `scan_range`: 6 target files enumerated above; grep pattern `\bcutoff_sqrt\b`
- `step_size`: N/A
- `tolerance`: integer count; PASS = 0, INFO ≤ 2 in curated root only, FAIL ≥ 1 elsewhere
- `scheme`: text-pattern-match-and-classify (each match tagged LOAD-BEARING / DIAGNOSTIC / METADATA)
- `convention`: hits in `canonical_constants.py:PROVENANCE` strings classified as METADATA (no edit required); hits in computation scripts that import cutoff_sqrt-tagged constants → LOAD-BEARING (require flag); hits in `cutoff-sqrt-adjudication.md` per-row are pre-classified by the adjudication file structure
- `random_seed`: N/A
- `GPU path`: N/A (CPU text processing only; no linalg)
- `Python env`: `phonon-exflation-sim/.venv312/Scripts/python.exe`

### 7. Input SHA-256 pins (computed at runtime)
- `sessions/archive/session-86/session-86-w4-2-workingpaper.md` — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w6-workingpaper.md` — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w12-workingpaper.md` — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w13-workingpaper.md` — `<computed-at-runtime>`
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` — `<computed-at-runtime>`
- `computations/s86_gate_verdicts.txt` (for the GATE A FAIL canonical-record line cited in every flag) — `<computed-at-runtime>`

### 8. Expected output 4-tuple
`(value=n_unflagged_residual_cutoff_sqrt_load_bearing_cites=<int>, scheme=text-pattern-match-and-classify, convention=A_5_to_A_4_cascade_propagation, L_max=N/A)`

### 9. Substitution chain (per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute")

```
Step 1 (definitions):
  hits_total      := count of regex \bcutoff_sqrt\b across the 6 target files
  hits_metadata   := hits inside `canonical_constants.py:PROVENANCE` string literals
                     (recording origin; no edit needed)
  hits_diagnostic := hits explicitly tagged as W-11-class regulator-class-
                     independence diagnostics (e.g., the η-GV joint probe table)
  hits_load_bear  := hits where cutoff_sqrt is consumed as an active atlas
                     member of A_5 in a script's atlas list, a registry-row
                     citation as load-bearing, or an unqualified "atlas =
                     {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}" enumeration
  flagged         := hits_load_bear hits that the edit pass tagged with
                     [LEGACY: cascade A_5→A_4 per S86 W-8 GATE A FAIL ...]
  residual        := hits_load_bear − flagged

Step 2 (substitute):
  PASS predicate := (residual == 0)
  FAIL predicate := (residual >= 1) AND NOT (residual <= 2 AND all-in-curated-root)
  INFO predicate := (0 < residual <= 2) AND (every residual in curated framework root file)

Step 3 (simplify):
  Composite verdict via the composite-collapse rule (`.claude/rules/gate-verdicts.md`):
    sign_verdict     = PASS  (the prediction is "edit pass clears load-bearing
                              residuals to zero"; PASS direction = residual decreases
                              to 0; FAIL direction = residual remains ≥ 1)
    magnitude_verdict = PASS if residual == 0; FAIL otherwise
    regime_verdict    = VALID (mechanical text-pass; no regime-of-validity bound)

Step 4 (direction):
  residual = 0  ⇒  composite PASS
  residual = 1  ⇒  if in curated-root ONLY: composite INFO; else FAIL
  residual ≥ 2  ⇒  if all-in-curated-root: composite INFO; else FAIL
  residual ≥ 3  ⇒  composite FAIL unconditionally
```

The substitution chain has no sign/direction claim that requires a non-trivial algebraic step; the integer count IS the canonical form. Direction is read off mechanically.

### 10. What PASS / FAIL means for the solution space
- **PASS**: the A_5 → A_4 cascade is fully propagated; downstream consumers in W4-2/W6/W12/W13 are operationally consistent with the reduced atlas, and `cutoff_sqrt` is preserved only in legacy-diagnostic capacity (W-11-class probes). Future S87+ atlas-cardinality assertions can take A_4 as the unconditional canonical without per-citation provenance tracing.
- **FAIL**: at least one downstream consumer of cutoff_sqrt as a load-bearing atlas member survived the edit pass. The cascade has a logical leak; the failed citation must be tracked and re-flagged manually.
- **INFO**: residual ≤ 2 in curated framework-root files where bulk edits are forbidden per `feedback_framework-hygiene.md`; manual-review S88 carry-forward.

The PASS outcome closes the operational atlas to A_4 across the S87+ session corpus; FAIL/INFO leaves a tagged corner of the corpus where atlas-cardinality is ambiguous.

### 11. Owning agent
`gen-physicist` (per recommending-agent column of CF-47; mechanical breadth task across multiple working-paper sources is the cross-domain workhorse niche).

### 12. Producing script
`computations/s87_w8_cutoff_sqrt_atlas_propagation.py`

### 13. Output artifacts
- Script: `computations/s87_w8_cutoff_sqrt_atlas_propagation.py`
- Data: `computations/s87_w8_cutoff_sqrt_atlas_propagation.json` (per-file hit table: file_path × hits_total × hits_metadata × hits_diagnostic × hits_load_bearing × flagged × residual)
- Plot: NONE (text-pass; no quantity to plot)
- Verdict line: appended to `computations/s87_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md` S87+ schema-v2 (canonical line + dual-SHA companion + 3-tuple annotation since `[VERIFY]` + `[AUDIT]` triggers carry directional pre-registration)
- Working-paper section: §W8-1 of `sessions/archive/session-87/session-87-w8-workingpaper.md` (≥15 substantive lines per `.claude/rules/agent-standards.md` §Completion Verification)

### YAML
```yaml
gate_id: S87-CUTOFF-SQRT-ATLAS-PROPAGATION
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, AUDIT]
classification: GEOMETRIC
specialist: gen-physicist
effort_hours: 3
```

---

## §W8-2. S87-W4-2-RE-RUN-UNDER-A_4 (CF-48)

### 1. Gate ID
`S87-W4-2-RE-RUN-UNDER-A_4`

### 2. Trigger
`[VERIFY]` + `[VERIFY-THEOREM]`

### 3. Classification
GEOMETRIC (re-derivation under reduced atlas; spectral-cluster identity at the substrate-axiom layer).

### 4. Hypothesis
The W4-2 max_pair_ratio gate, originally evaluated on the A_5 5-column atlas, is invariant under the A_5 → A_4 reduction (cutoff_sqrt removed). Specifically: (a) max_pair_ratio computed on the 4-column atlas {ζ, Zubarev, SDW, anomaly} agrees with the original W4-2 value to bit-identical precision when cutoff_sqrt was a non-extremal column; (b) the cluster-span identity `b_pow(span_2) = 2 · b_pow(span_3)` (W0-3 CC-5 multiplicative identity) is preserved at canonical metric.

### 5. PASS / FAIL / INFO threshold

**Sub-gate (a) max_pair_ratio invariance**:
- **PASS**: `|max_pair_ratio_A4 − max_pair_ratio_A5| < 1e-15` (RATIO tolerance, bit-identical preservation when cutoff_sqrt was non-extremal). If cutoff_sqrt WAS the extremal column in A_5, the gate emits an explicit DIAGNOSTIC tag and routes to sub-case (a-bis): max_pair_ratio_A4 must produce the next-largest A_5 ratio, with the cutoff_sqrt-extremal pair recorded for the working paper.
- **FAIL**: `|max_pair_ratio_A4 − max_pair_ratio_A5| ≥ 1e-12`.
- **INFO**: `1e-15 ≤ |...| < 1e-12` (precision-floor band; A_4 = subset of A_5 algebraically forces 0 difference when extremum is non-cutoff_sqrt; any non-zero up to ~1e-12 indicates an upstream data-load precision issue).

**Sub-gate (b) cluster-span canonical-metric identity**:
- **PASS**: `|ratio − 2| < 1e-14` where `ratio = b_pow(span_2) / b_pow(span_3)` evaluated at L_max=12 on `_cluster_span_extract.py`'s `cluster_span(L_max=12)` output. Threshold `< 1e-14 ≈ 45 × float_eps` per the W2-4 calibration corpus and `.claude/rules/epistemic-discipline.md` §"Canonical-metric pin extension" T2-4 (refactor preservation criterion).
- **FAIL**: `|ratio − 2| ≥ 1e-13`.
- **INFO**: `1e-14 ≤ |ratio − 2| < 1e-13` (precision-floor; documents the achievable canonical-metric floor).

Tolerance rule for both sub-gates: RATIO. **Canonical metric for sub-gate (b) is `|ratio − 2|`, NOT the normalized form `|b2 − 2·b3| / |b2|`** (per `.claude/rules/epistemic-discipline.md` §"Canonical-metric pin extension"; the normalized form differs by a factor 2 at the float-cancellation floor and underflows the W0-3 PASS achievable floor at the same threshold).

Joint composite: PASS iff (a) PASS AND (b) PASS; INFO if either is INFO and neither FAIL; FAIL otherwise.

### 6. Machinery pin (PRDR)
- `N_eval`: number of eigenvalues at L_max=12 from `s84_spectrum_cache_L12_tau019.npz` (cache-determined; ≈ 350,000 PW-signed at L_max=12)
- `L_max`: 12 (cluster-span sub-gate); 10 for max_pair_ratio sub-gate (W4-2 original)
- `scan_range`: cluster-span: span ∈ {2, 3} per W0-3 CC-5 anchor; max_pair_ratio: 4-column atlas {ζ, Zubarev, SDW, anomaly}
- `step_size`: N/A (single-evaluation)
- `tolerance`: sub-gate (a): 1e-15 PASS / 1e-12 FAIL; sub-gate (b): 1e-14 PASS / 1e-13 FAIL
- `scheme`: cluster-span canonical metric `|ratio − 2|` where `ratio = b_pow(span_2)/b_pow(span_3)`
- `convention`: 4-column atlas A_4 = {ζ, Zubarev, SDW, anomaly}; max_pair_ratio definition per W4-2 working paper §3 (original); cluster-span scheme per W2-4 closure
- `random_seed`: N/A (deterministic)
- `GPU path`: CPU sufficient (sums + ratios; no eigvals computed in this gate, only loaded from cache); `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`

### 7. Input SHA-256 pins
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>`
- `computations/_cluster_span_extract.py` — `<computed-at-runtime>` (importable callable)
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w4-2-workingpaper.md` (max_pair_ratio_A5 anchor) — `<computed-at-runtime>`
- `computations/s86_gate_verdicts.txt` (W4-2 verdict line for max_pair_ratio_A5 anchor) — `<computed-at-runtime>`
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` — `<computed-at-runtime>`

### 8. Expected output 4-tuple
`(value=(max_pair_ratio_A4, |ratio−2|), scheme=cluster_span_canonical_metric, convention=A_4_post_cascade_4col, L_max=12)`

### 9. Substitution chain

```
Step 1 (definitions):
  cluster_span(L_max)     := the b_pow function returned by `_cluster_span_extract.py`
                             cluster_span(L_max), evaluated at the two spans 2 and 3
  ratio                   := b_pow(span_2) / b_pow(span_3)
  canonical_metric        := |ratio − 2|              (W0-3 CC-5 anchor metric)
  normalized_metric       := |b_pow(span_2) − 2·b_pow(span_3)| / |b_pow(span_2)|
                                                       (PROHIBITED form per §"Canonical-metric pin extension")
  max_pair_ratio_A_n     := max over all unordered pairs {r_i, r_j} ⊂ A_n of
                             |coupling_value(r_i) − coupling_value(r_j)| / min(|coupling_value(r_i)|, |coupling_value(r_j)|)
                             evaluated on the n-column atlas at L_max=10
  max_pair_ratio_A_5     := original W4-2 published value (anchor)
  max_pair_ratio_A_4     := this gate's recomputation on the 4-col atlas
  delta_pr               := |max_pair_ratio_A_4 − max_pair_ratio_A_5|
  span_invariant         := canonical_metric

Step 2 (substitute):
  Algebraic identity: ratio − 2 = (b_pow(span_2) − 2·b_pow(span_3)) / b_pow(span_3)
                  ⇒ canonical_metric = |b_pow(span_2) − 2·b_pow(span_3)| / |b_pow(span_3)|
  Normalized form:    normalized_metric = |b_pow(span_2) − 2·b_pow(span_3)| / |b_pow(span_2)|
  Identity ratio:     normalized_metric / canonical_metric = |b_pow(span_3)| / |b_pow(span_2)|
                                                          ≈ 1 / 2     (since b_pow(span_2) ≈ 2·b_pow(span_3) at PASS)
  ⇒ canonical_metric ≈ 2 × normalized_metric at the float-cancellation floor.

Step 3 (simplify):
  PASS predicate (a):  delta_pr < 1e-15
  PASS predicate (b):  canonical_metric < 1e-14   (= 45 × float_eps refactor band)
  Joint PASS:          (a) AND (b)

Step 4 (direction):
  Since A_4 ⊂ A_5 (set-theoretically: cutoff_sqrt is removed; the four
  remaining atlas members are unchanged), the max-over-pairs operation
  on A_4 is bounded above by max-over-pairs on A_5 (any pair in A_4 is
  also a pair in A_5; the maximum cannot increase).
  ⇒ max_pair_ratio_A_4 ≤ max_pair_ratio_A_5  (monotone direction).
  Equality holds iff the A_5 extremal pair did not include cutoff_sqrt.
  Strict inequality ⇒ A_5 extremal pair included cutoff_sqrt
    ⇒ A_4-recompute returns the next-largest A_5 ratio (DIAGNOSTIC tag fires).

  cluster-span direction: the W0-3 PASS at L_max=12 reports
  canonical_metric = 2.220e-15 (≈ 10 × float_eps); refactor preservation
  requires ≤ 45 × float_eps = 1e-14, which IS achievable per W2-4
  calibration. Direction: PASS conditional on bit-exact reproduction of
  the L_max=12 cache load.
```

### 10. What PASS / FAIL means for the solution space
- **PASS (joint)**: The A_5 → A_4 reduction is verified at the W4-2 max_pair_ratio level (no extremal cutoff_sqrt-pair was load-bearing), AND the cluster-span identity is preserved at canonical metric. The W4-2 gate's quantitative output is operationally identical under the reduced atlas.
- **FAIL on (a)**: The A_5 extremum was a cutoff_sqrt-involving pair, AND the next-largest pair on A_4 differs from the published value by more than precision floor — indicates a substantively different atlas-extremum after cascade. The new value becomes the canonical max_pair_ratio.
- **FAIL on (b)**: The cluster-span identity broke — indicates a regression in `_cluster_span_extract.py` or the L_max=12 cache. Routes to `_cluster_span_extract.py` regression debug as a NEW S87 carry-forward to S88.
- **INFO**: precision-floor band crossed but the result is still consistent with bit-equivalence; carry-forward only documentation.

### 11. Owning agent
`connes-ncg-theorist` (cluster-span identity is a substrate NCG-axiom-native operation; same agent who landed W2-4).

### 12. Producing script
`computations/s87_w8_w4_2_re_run_under_a_4.py`

### 13. Output artifacts
- Script: `computations/s87_w8_w4_2_re_run_under_a_4.py`
- Data: `computations/s87_w8_w4_2_re_run_under_a_4.npz` (max_pair_ratio_A4, max_pair_ratio_A5, delta_pr, ratio, canonical_metric, span_2, span_3, b_pow_span_2, b_pow_span_3, atlas_extremal_pair, was_cutoff_sqrt_extremal_in_A5)
- Plot: `computations/s87_w8_w4_2_re_run_under_a_4.png` (bar chart of pair-ratios per atlas pair, A_5 vs A_4 side-by-side, plus a horizontal line at the canonical-metric float-cancellation floor)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W8-2

### YAML
```yaml
gate_id: S87-W4-2-RE-RUN-UNDER-A_4
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, VERIFY-THEOREM]
classification: GEOMETRIC
specialist: connes-ncg-theorist
effort_hours: 2
```

---

## §W8-3. S87-C45-SIXTH-REGULATOR-PROMOTION (CF-49)

### 1. Gate ID
`S87-C45-SIXTH-REGULATOR-PROMOTION`

### 2. Trigger
`[VERIFY]` + `[CHAIN]` (multi-channel chain of admissibility tests)

### 3. Classification
GEOMETRIC (substrate-regulator atlas extension; structural admissibility against LAYER 2 axioms).

### 4. Hypothesis
There exists a candidate sixth regulator `R_6` such that R_6 (a) PASSes all 4 LAYER 2 admissibility channels enumerated by W-8 (channel-1 axiom-sourcing minimality, channel-2 inner-fluctuation lift, channel-3 HBW positive-cone, channel-4 routing/coupling-Λ-scaling) AND (b) matches §VII.M layer-membership target on `permanent-results-registry.md` (i.e., has a clean LAYER 2 admissibility ladder analogous to ζ / Zubarev / SDW / anomaly). PASS would promote A_4 → A_5_v2 with R_6 replacing cutoff_AL2010 in the slot.

### 5. PASS / FAIL / INFO threshold

Per `.claude/rules/methodology-wave-allowlist.md` PRE-REGISTRATION: enumerate the candidate sixth-regulator set BEFORE any channel test fires. The candidate set MUST be enumerated in PART-1 of the working-paper section (analogous to S82 W1 PART-1/PART-2/PART-3 schema for registration gates). The pre-registered candidate set IS:

`R_6_candidates := {Schwinger_proper_time, Lorentz_kinematic, dimensional_reg_d_minus_eps, Borel_resummation_kernel, Connes_Moscovici_Hopf_cocycle_dressing}`

Channel tests (each tested independently for each candidate):
- **Channel-1 (axiom-sourcing minimality)**: candidate's a_0-channel sources from a load-bearing CCM-2007 axiom subset of cardinality ≤ 4 (matches A_4 baseline).
- **Channel-2 (inner-fluctuation lift)**: candidate admits a Hopf-cocycle inner-fluctuation that redirects the L^8 mode-count growth out of the a_0 channel to a higher-residue slot (the structural fix that cutoff_AL2010 LACKED, per S86 W-8 GATE A FAIL substrate analysis).
- **Channel-3 (HBW positive-cone)**: candidate's f_n-residue MP-abs-conv at s ∈ {2, 4, 6} is positive-cone-preserving (no negative residues introduced).
- **Channel-4 (routing/coupling-Λ-scaling)**: candidate admits Λ(L_max) = Λ_0 · L_max^α with α ≥ 0 and bounded coupling g(L) → finite as L → ∞ (the gate that cutoff_AL2010 STRUCTURALLY FAILED at A_5 W-8).

- **PASS (R_6 promotion)**: ≥ 1 candidate PASSes all 4 channels AND lands a §VII.M ladder-row matching {ζ, Zubarev, SDW, anomaly} layer-membership pattern.
- **PARTIAL-PASS / INFO**: ≥ 1 candidate PASSes channels {1, 3} but FAILs channel-2 or channel-4 (i.e., axiom-clean but coupling-defective; analogous to cutoff_sqrt's LAYER 1 PRIVILEGED / LAYER 2 FAILING split). Records the candidate as a S88 "depth-extension promotion" carry-forward.
- **FAIL**: zero candidates pass all 4 channels. Atlas remains A_4; no sixth regulator promoted.

Tolerance rule: THEOREM (each channel is a binary admissibility predicate, not a numerical comparison; the channel-1 cardinality and channel-4 α-scan are the two sub-numeric tests, with thresholds: cardinality ≤ 4 PASS / > 4 FAIL; α_max ≥ 0 PASS / < 0 FAIL).

### 6. Machinery pin (PRDR)
- `N_eval`: per-candidate Peter-Weyl mode-count evaluation at L ∈ {3, 5, 7, 10} (matches W-8 GATE A probe set)
- `L_max`: 10 (probe set max); 7 for channel-1 subset-removal sweep (matches GATE B protocol)
- `scan_range`:
  - channel-1: subset-removal sweep over CCM-2007 axiom set {dim, reg, fin, real, 1st-order, orient, PD}
  - channel-2: Hopf-cocycle dressing space enumerated by Connes-Moscovici 1995 §III.4 generators (R_universal, R_BDI, R_PV, R_anomaly)
  - channel-3: MP-abs-conv at s ∈ {2, 4, 6} on framework-truncated f_2 = 0.0, f_4 = 0.05, f_6 = 0.1
  - channel-4: α ∈ [−2, +2] step 0.05 (matches GATE A scan)
- `step_size`: as enumerated per channel
- `tolerance`: see §5 thresholds
- `scheme`: 4-channel chain test per candidate; layer-membership match per `permanent-results-registry.md` §VII.M
- `convention`: A_4 baseline = {ζ, Zubarev, SDW, anomaly}; sixth-regulator slot identifier `R_6` reserved
- `random_seed`: 42 (deterministic; if any candidate involves a non-deterministic kernel, the seed is recorded but unused)
- `GPU path`: CPU sufficient (Peter-Weyl k_eff is integer-rational; channel-2 inner-fluctuation lift is symbolic Hopf-cocycle algebra dispatched to `mcp__sage__` per candidate)

### 7. Input SHA-256 pins
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` — `<computed-at-runtime>`
- `sessions/permanent-results-registry.md` (§VII.M layer-membership row anchor) — `<computed-at-runtime>`
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>` (for Peter-Weyl mode-count anchors at L ∈ {3..10})
- `computations/s86_gate_verdicts.txt` (GATE A/B/C verdict lines for A_4 baseline) — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w8-workingpaper.md` (substrate framing for channel decomposition) — `<computed-at-runtime>`

### 8. Expected output 4-tuple
`(value=(n_candidates_PASS_all_4_channels, R_6_winner_id_or_None), scheme=4-channel-chain-test, convention=A_4_to_A_5_v2_promotion_attempt, L_max=10)`

### 9. Substitution chain

```
Step 1 (definitions):
  candidate_set := {Schwinger_proper_time, Lorentz_kinematic,
                    dimensional_reg_d_minus_eps, Borel_resummation_kernel,
                    Connes_Moscovici_Hopf_cocycle_dressing}
  channel_i_PASS(R) := boolean predicate per §5 channel-i criterion
  passes_all(R)     := channel_1_PASS(R) AND channel_2_PASS(R)
                       AND channel_3_PASS(R) AND channel_4_PASS(R)
  layer_match(R)    := registry-anchor §VII.M layer-membership ladder
                       row for R matches the {ζ, Zubarev, SDW, anomaly}
                       layer-pattern (axiom-set ⊆ {dim, fin, reg, real, 1st-order, orient, PD},
                       inner-fluctuation lift to a higher-residue slot, HBW
                       positive-cone preservation across f_2/f_4/f_6)
  R_6_winner        := first R ∈ candidate_set with passes_all(R) AND layer_match(R)
  n_PASS            := |{R ∈ candidate_set : passes_all(R) AND layer_match(R)}|

Step 2 (substitute):
  PASS predicate := n_PASS ≥ 1
  INFO predicate := n_PASS = 0 AND ∃ R such that
                    channel_1_PASS(R) AND channel_3_PASS(R) AND
                    NOT (channel_2_PASS(R) AND channel_4_PASS(R))
  FAIL predicate := n_PASS = 0 AND no INFO-eligible candidate exists

Step 3 (simplify):
  Per W-8 GATE A FAIL substrate paragraph (workshop §"Substrate framing"):
  Peter-Weyl mode-count growth is L^8/960 at d=8; ANY positive-α regulator
  that reads off the a_0 channel directly (sharp cutoff or √x-modified sharp
  cutoff) inherits the L^8 growth and cannot satisfy α ≥ 0 boundedness.
  ⇒ channel-4 PASS requires the candidate to NOT read off a_0 directly;
  ⇒ candidate must implement a Hopf-cocycle inner-fluctuation lift
    redirecting the L^8 weight to a higher residue slot.
  ⇒ channel-2 is the gating channel for channel-4; failure of channel-2
    structurally precludes channel-4 PASS (one-way implication).

Step 4 (direction):
  The structural one-way implication (channel-2 FAIL ⇒ channel-4 FAIL) means:
  - a candidate that PASSes channel-2 may or may not PASS channel-4
    (depends on whether the inner-fluctuation lift puts the L^8 weight into
    a residue slot whose α-scan is bounded).
  - a candidate that FAILs channel-2 STRUCTURALLY FAILs channel-4.

  Direction prediction:
  - Among the 5 candidates, Connes_Moscovici_Hopf_cocycle_dressing is the
    most structurally promising (designed from the ground up to admit a
    Hopf-cocycle lift); it is the prime channel-2 PASS candidate.
  - Schwinger_proper_time and dimensional_reg_d_minus_eps share the
    a_0-direct-reading defect with cutoff_AL2010 → channel-2 FAIL likely.
  - Borel_resummation_kernel and Lorentz_kinematic admit asymmetric
    a_n-channel weights and may PASS channel-2; the channel-4 outcome
    is not pre-determined.
  This is a PREDICTION, not a verdict; the gate WILL execute the chain
  empirically.
```

### 10. What PASS / FAIL means for the solution space
- **PASS (R_6 promoted)**: A_4 promotes to A_5_v2 with a structurally clean sixth regulator. The W-8 atlas-cardinality cascade is reversed in a substrate-natural way; future atlas-cardinality assertions cite A_5_v2 with the new R_6 in the slot.
- **PARTIAL-PASS / INFO**: a candidate PASSes channels {1, 3} but FAILs {2, 4}. This is the cutoff_AL2010 structural mode (LAYER 1 PRIVILEGED / LAYER 2 FAILING). Records as S88 "depth-extension" carry-forward; A_4 stays canonical.
- **FAIL**: zero candidates clear all 4 channels. Atlas A_4 is the canonical 4-regulator atlas; no sixth-regulator route exists in this candidate set. Carry-forward to S88+ as a structural-search question (extend candidate set to e.g. CM-1995 § Hopf-cocycle classes beyond R_universal/R_BDI/R_PV/R_anomaly).

### 11. Owning agent
`connes-ncg-theorist` (NCG-axiom-native multi-channel admissibility chain; channel-2 Hopf-cocycle inner-fluctuation lift is connes' substrate competence).

### 12. Producing script
`computations/s87_w8_c45_sixth_regulator_promotion.py`

### 13. Output artifacts
- Script: `computations/s87_w8_c45_sixth_regulator_promotion.py`
- Data: `computations/s87_w8_c45_sixth_regulator_promotion.json` (per-candidate × per-channel PASS/FAIL matrix; channel-4 α-scan per candidate; channel-2 Hopf-cocycle lift symbolic results from `mcp__sage__`)
- Plot: `computations/s87_w8_c45_sixth_regulator_promotion.png` (5×4 PASS/FAIL grid, candidates rows × channels columns, color-coded; channel-4 α_max overlaid as numeric annotation per cell)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W8-3 in PART-1 (candidate enumeration) / PART-2 (per-channel results) / PART-3 (R_6 winner identification or FAIL summary) schema

### YAML
```yaml
gate_id: S87-C45-SIXTH-REGULATOR-PROMOTION
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, CHAIN]
classification: GEOMETRIC
specialist: connes-ncg-theorist
effort_hours: 6
```

---

## §W8-4. S87-HBW-AUDIT-ATLAS-A_4 (CF-50)

### 1. Gate ID
`S87-HBW-AUDIT-ATLAS-A_4`

### 2. Trigger
`[VERIFY]` + `[AUDIT]`

### 3. Classification
GEOMETRIC (substrate HBW positive-cone test under reduced atlas; channel-3 substructure resolution).

### 4. Hypothesis
All 4 surviving atlas members A_4 = {ζ, Zubarev, SDW, anomaly} pass HBW (Hausdorff-Bernstein-Widder) positivity at the f_6 = 0.1 framework-truncated residue slot, and the channel-3 substructure resolves into 5 sub-channels {3a, 3b, 3c, 3d, 3e} corresponding to (3a) MP-abs-conv at s=6 / (3b) positive-cone moment sequence / (3c) Bernstein-density factor sign / (3d) Widder-inversion well-posedness / (3e) Hausdorff-moment problem solvability.

### 5. PASS / FAIL / INFO threshold

For each (regulator R ∈ A_4) × (sub-channel c ∈ {3a, 3b, 3c, 3d, 3e}):
- **sub-PASS**: HBW c-criterion satisfied per pre-registered numerical test
- **sub-FAIL**: HBW c-criterion violated
- **sub-INFO**: c-criterion within precision floor of the boundary (e.g., positive-cone with `min_eigenvalue ∈ [-1e-12, +1e-12]`)

Aggregate (regulator-level): regulator R PASSes iff all 5 sub-channels sub-PASS.
Gate-level:
- **PASS**: all 4 regulators × all 5 sub-channels = 20 sub-PASSes.
- **FAIL**: ≥ 1 regulator has ≥ 1 sub-FAIL on a non-precision-floor margin.
- **INFO**: ≥ 1 sub-INFO and zero sub-FAIL.

Sub-channel thresholds:
- **3a (MP-abs-conv at s=6)**: `|Σ_n a_n^{(R)} · n^{-6}|` converges to a value V with `|V_truncated_at_L=10 − V_truncated_at_L=12| < 1e-10` (RATIO truncation tolerance)
- **3b (positive-cone moment sequence)**: `min_n a_n^{(R)} · w_R(n) ≥ -1e-12` for n ∈ {0, 2, 4, 6}; PASS iff non-negative within precision floor
- **3c (Bernstein-density factor sign)**: regulator's Bernstein-density factor `b_R(λ) := (-1)^k · d^k w_R(λ)/dλ^k` for k ∈ {0, 1, 2, 3} is non-negative for all λ in the spectral support [λ_min, λ_max] at L_max=12
- **3d (Widder-inversion well-posedness)**: condition number of the Widder-inversion operator `W_R := ∫_0^∞ e^{-λ s} · w_R(λ) dλ` evaluated as a discrete moment matrix is finite (`κ < 1e15`) — i.e., the inversion is numerically well-posed
- **3e (Hausdorff-moment problem solvability)**: the moment sequence `{a_n^{(R)}}_{n=0,2,4,6}` admits a representing measure on `[0, λ_max(L_max=12)^2]` per the Hausdorff completeness criterion (positive-definite Hankel matrix at order 4)

Tolerance rule: each sub-channel has its own (per §5 enumeration); aggregate is THEOREM (count-based).

### 6. Machinery pin (PRDR)
- `N_eval`: ≈ 350,000 PW-signed eigenvalues at L_max=12 from `s84_spectrum_cache_L12_tau019.npz`
- `L_max`: 12 (canonical L_max for HBW; 10 for cross-check)
- `scan_range`: regulators × sub-channels = 4 × 5 = 20 cells
- `step_size`: per sub-channel as enumerated
- `tolerance`: per sub-channel as enumerated
- `scheme`: HBW positivity = (Bernstein-density factor sign + Widder-inversion well-posedness + Hausdorff-moment Hankel positive-definiteness)
- `convention`: framework-truncated f_2 = 0.0, f_4 = 0.05, f_6 = 0.1 (per W-8 GATE C anchor); A_4 baseline 4-column atlas
- `random_seed`: N/A (deterministic)
- `GPU path`: matrix products and condition-number computations on Hankel matrices of order ≤ 4 are CPU-trivial; `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`

### 7. Input SHA-256 pins
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>`
- `computations/s84_spectrum_cache_L10_tau019.npz` (cross-check) — `<computed-at-runtime>`
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` (HBW reference per W-8 GATE C) — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w8-workingpaper.md` (channel-3 sub-classification source) — `<computed-at-runtime>`

### 8. Expected output 4-tuple
`(value=(n_sub_PASS_total, n_regulators_full_PASS), scheme=HBW_5_subchannel_audit, convention=A_4_4col_f6_0.1_residue, L_max=12)`

### 9. Substitution chain

```
Step 1 (definitions):
  HBW positive-cone iff (Bernstein-density factor sign + Widder-inversion
                        well-posedness + Hausdorff-moment Hankel
                        positive-definiteness)
  per Bernstein-Widder theorem (1929/1934):
    a function f on (0,∞) is COMPLETELY MONOTONIC iff
    (-1)^k · f^{(k)}(λ) ≥ 0 for all k ≥ 0 and λ > 0
    iff f admits a Laplace-Stieltjes integral representation
    f(λ) = ∫_0^∞ e^{-λ s} dμ(s) for some positive measure μ.

  For each regulator R ∈ A_4, define:
    w_R(λ) := the regulator weight function (per W-11 §2 anchors)
    a_n^{(R)} := Σ_lambda multiplicity(λ) · λ^n · w_R(λ)
    H_4^{(R)} := 5×5 Hankel matrix [a_{i+j}^{(R)}]_{i,j ∈ {0,1,2,3,4}}
    κ_R := condition number of W_R restricted to moments {0,2,4,6}

Step 2 (substitute):
  sub-PASS_3a(R) := |Σ_n a_n^{(R)} · n^{-6}| converges within 1e-10 between L_max=10 and L_max=12
  sub-PASS_3b(R) := min_n a_n^{(R)} · w_R(n) ≥ -1e-12 for n ∈ {0,2,4,6}
  sub-PASS_3c(R) := for all λ ∈ [λ_min, λ_max] at L_max=12,
                    (-1)^k · d^k w_R/dλ^k ≥ 0 for k ∈ {0,1,2,3}
  sub-PASS_3d(R) := κ_R < 1e15
  sub-PASS_3e(R) := H_4^{(R)} positive-definite (smallest eigenvalue > -1e-12)

Step 3 (simplify):
  regulator_PASS(R) := AND_{c ∈ {3a..3e}} sub-PASS_c(R)
  n_sub_PASS_total := Σ_R Σ_c sub-PASS_c(R)
  n_regulators_full_PASS := Σ_R regulator_PASS(R)

Step 4 (direction):
  Pre-W-8 anchor: ζ, Zubarev, SDW each have positive-monotonic
  weight w_R(λ) on λ > 0 (heat-kernel-derived); their Bernstein-density
  factors are non-negative by construction. anomaly's APS w_a(λ) ∝ 1/|λ|
  carries a sign at λ → 0+ but is positive on the spectral support
  bounded away from zero (λ_min > 0 at L_max=12 by W-11 §2).
  ⇒ structural prediction: ζ, Zubarev, SDW PASS all 5 sub-channels;
    anomaly may sub-INFO at 3c near λ_min.
  Direction: PASS likely; INFO on anomaly possible; FAIL would surface
    a substrate-axiom inconsistency (none anticipated).
```

### 10. What PASS / FAIL means for the solution space
- **PASS**: A_4 = {ζ, Zubarev, SDW, anomaly} is a fully HBW-positive-cone-preserving 4-regulator atlas, structurally consistent across the 5 sub-channels. The §VII.M layer-membership row stabilizes.
- **FAIL on 3a**: convergence anomaly between L_max=10 and L_max=12 — indicates s=6 truncation insufficiency; carry-forward to L_max=14 cache regeneration (cf. CF-10 deferred).
- **FAIL on 3b/3c/3e**: positive-cone violation — would force re-classification of the FAIL'd regulator out of A_4 (potential A_4 → A_3 cascade); structurally surprising given W-11 evidence; would route to high-priority re-investigation in S88.
- **FAIL on 3d**: ill-conditioned Widder-inversion — numerical-method failure; carry-forward as precision-floor S88 work.
- **INFO**: precision-floor band on at least one sub-channel; documents the achievable HBW-audit floor at L_max=12.

### 11. Owning agent
`connes-ncg-theorist` (HBW positivity is NCG-axiom-native; the Bernstein-Widder factorization is the substrate's spectral-action positive-cone structure).

### 12. Producing script
`computations/s87_w8_hbw_audit_atlas_a_4.py`

### 13. Output artifacts
- Script: `computations/s87_w8_hbw_audit_atlas_a_4.py`
- Data: `computations/s87_w8_hbw_audit_atlas_a_4.npz` (4×5 sub-PASS grid; per-cell numerical values: 3a convergence, 3b min-moment-with-weight, 3c min-Bernstein-derivative on spectral support, 3d Widder κ, 3e Hankel min-eigenvalue)
- Plot: `computations/s87_w8_hbw_audit_atlas_a_4.png` (4×5 heat-grid; PASS/FAIL/INFO color-coded; numerical values overlaid)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W8-4

### YAML
```yaml
gate_id: S87-HBW-AUDIT-ATLAS-A_4
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, AUDIT]
classification: GEOMETRIC
specialist: connes-ncg-theorist
effort_hours: 5
```

---

## §W8-5. S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY (CF-51)

### 1. Gate ID
`S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY`

### 2. Trigger
`[VERIFY]` + `[CHAIN]` (4-channel localization chain)

### 3. Classification
GEOMETRIC (Mellin-cone live infrastructure modification scoping; channel-localization audit).

### 4. Hypothesis
The W2 C9/C10 Mellin-cone live infrastructure modifications (per S86 W4-2 P5 mellin_cone_live=False fallback path) affect ONLY channel-2 (inner-fluctuation lift) of the W-8 4-channel admissibility decomposition. Specifically, swapping mellin_cone_live={True, False} produces measurable changes in channel-2 numerics, but channels {1, 3, 4} are bit-identical.

### 5. PASS / FAIL / INFO threshold

For each channel c ∈ {1, 2, 3, 4} on each regulator R ∈ A_4:
- compute `delta_c_R := |numerical_output_c(R, mellin_cone_live=True) − numerical_output_c(R, mellin_cone_live=False)|`
- normalized: `delta_c_R_norm := delta_c_R / |numerical_output_c(R, mellin_cone_live=False)|` (if denominator ≠ 0)

- **PASS**: `max_{R ∈ A_4} delta_c_R_norm < 1e-12` for c ∈ {1, 3, 4} (non-channel-2 unaffected) AND `max_{R ∈ A_4} delta_2_R_norm > 1e-6` (channel-2 measurably affected; the modification has bite)
- **FAIL**: `max_{R ∈ A_4} delta_c_R_norm ≥ 1e-9` for ANY c ∈ {1, 3, 4} (localization broken; modification leaks into other channels) OR `max_{R ∈ A_4} delta_2_R_norm < 1e-12` (modification is a no-op on channel-2; doesn't actually do anything)
- **INFO**: `1e-12 ≤ delta_c_R_norm < 1e-9` for some non-channel-2 c (precision-floor leakage; documents the achievable channel-isolation floor)

Tolerance rule: RATIO (normalized differences).

### 6. Machinery pin (PRDR)
- `N_eval`: ≈ 350,000 PW-signed eigenvalues at L_max=12
- `L_max`: 12 (canonical); 10 for cross-check
- `scan_range`: 4 channels × 4 regulators × 2 mellin_cone_live settings = 32 evaluations
- `step_size`: N/A
- `tolerance`: per §5 thresholds (1e-12 PASS / 1e-9 FAIL / 1e-6 channel-2-bite)
- `scheme`: 4-channel chain test with mellin_cone_live={True, False} toggle; channel definitions per W-8 substrate paragraph (channel-1 axiom-sourcing, channel-2 inner-fluctuation, channel-3 HBW positive-cone, channel-4 routing/Λ-scaling)
- `convention`: A_4 = {ζ, Zubarev, SDW, anomaly}; mellin_cone_live infrastructure per `computations/_spectral_action_regulators.py` (level pin: declare PRIMARY if live-Mellin-cone is full physical / SCHEMATIC if SCHEMATIC per `.claude/rules/substrate-first-canonical-sourcing.md` §"W4-2 SCHEMATIC vs full physical level rule")
- `random_seed`: 42 (deterministic; mellin_cone_live=True path may use Mellin-Barnes contour deformation that benefits from seed pinning)
- `GPU path`: CPU sufficient for channel evaluations; if Mellin-Barnes contour evaluation invokes large matrix exponentiation on D_K, use `torch.linalg` on AMD RX 9070 XT per `.claude/rules/computation-environment.md`

### 7. Input SHA-256 pins
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>`
- `computations/_spectral_action_regulators.py` (Mellin-cone live infrastructure) — `<computed-at-runtime>`
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w4-2-workingpaper.md` (W4-2 P5 mellin_cone_live=False fallback anchor) — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w8-workingpaper.md` (4-channel decomposition source) — `<computed-at-runtime>`

### 8. Expected output 4-tuple
`(value=(max_delta_2_norm, max_delta_non2_norm), scheme=mellin_cone_live_toggle_4channel_localization, convention=A_4_4col, L_max=12)`

### 9. Substitution chain

```
Step 1 (definitions):
  out_c(R, m) := numerical output of channel-c admissibility test on regulator R
                  with mellin_cone_live=m (boolean), for c ∈ {1, 2, 3, 4}, m ∈ {True, False}
  delta_c_R   := |out_c(R, True) − out_c(R, False)|
  delta_c_R_norm := delta_c_R / max(|out_c(R, False)|, 1e-30)
                    (the 1e-30 floor prevents division-by-zero when
                    out_c(R, False) = 0, e.g., a channel that returns
                    exactly 0 in both modes — caught as INFO rather than
                    PASS-by-vacuous-ratio)
  channel_2_bite := max_{R ∈ A_4} delta_2_R_norm
  channel_non2_leak := max_{c ∈ {1,3,4}} max_{R ∈ A_4} delta_c_R_norm

Step 2 (substitute):
  PASS predicate := (channel_2_bite > 1e-6) AND (channel_non2_leak < 1e-12)
  FAIL predicate := (channel_non2_leak >= 1e-9) OR (channel_2_bite < 1e-12)
  INFO predicate := else (i.e., channel_non2_leak in [1e-12, 1e-9) or
                    channel_2_bite in [1e-12, 1e-6))

Step 3 (simplify):
  Two sub-conditions for PASS:
    (a) channel-2 is materially affected: channel_2_bite > 1e-6
    (b) other channels are bit-identical: channel_non2_leak < 1e-12
  Both required.

Step 4 (direction):
  The localization hypothesis predicts:
  - mellin_cone_live introduces Mellin-Barnes contour deformation
    in the inner-fluctuation lift step (channel-2)
  - axiom-sourcing (channel-1), HBW positive-cone (channel-3), and
    routing/Λ-scaling (channel-4) are computed on heat-kernel
    expansions of D_K that do NOT route through the Mellin-Barnes
    contour
  ⇒ direction: channel_2_bite > 1e-6 (substantively non-zero);
    channel_non2_leak < 1e-12 (bit-identical).
  PASS direction confirmed iff localization holds; FAIL direction
  surfaces if (a) channel-2 is unaffected (modification is a no-op on
  the very channel it was designed for — surprising, indicates
  infrastructure-modification regression) or (b) channels {1,3,4} pick
  up non-trivial differences (localization is broken — channels are
  not orthogonal w.r.t. the Mellin-Barnes contour).
```

### 10. What PASS / FAIL means for the solution space
- **PASS**: Mellin-cone live infrastructure is correctly localized to channel-2 (inner-fluctuation lift); channels {1, 3, 4} are insulated. The W4-2 P5 fallback (mellin_cone_live=False) is operationally safe for any analysis NOT routing through channel-2. Future S87+ gates can adopt the live infrastructure for channel-2 work with confidence that channels {1, 3, 4} are unchanged.
- **FAIL on channel-2 silence (channel_2_bite < 1e-12)**: the live-Mellin infrastructure is a no-op; the modification doesn't change what it claims to change. Indicates a regression in `_spectral_action_regulators.py` or that the `mellin_cone_live=True` code path is not actually used downstream. Routes to infrastructure-debug S88 carry-forward.
- **FAIL on non-channel-2 leakage (channel_non2_leak ≥ 1e-9)**: the channels are not orthogonal under the Mellin-Barnes contour; the W-8 4-channel decomposition is structurally incomplete. Routes to channel-decomposition revision S88.
- **INFO**: precision-floor band; the channels are nearly orthogonal but not bit-identical-orthogonal. Documents the achievable channel-isolation floor at L_max=12.

### 11. Owning agent
`lizzi-spectral-functional-theorist` (Mellin-cone live infrastructure is lizzi's owned tooling per W2 C9/C10 implementation track).

### 12. Producing script
`computations/s87_w8_mellin_cone_live_channel_2_localization_verify.py`

### 13. Output artifacts
- Script: `computations/s87_w8_mellin_cone_live_channel_2_localization_verify.py`
- Data: `computations/s87_w8_mellin_cone_live_channel_2_localization_verify.npz` (4×4×2 grid: regulators × channels × mellin_cone_live; plus delta tables; plus normalized delta tables)
- Plot: `computations/s87_w8_mellin_cone_live_channel_2_localization_verify.png` (delta_c_R_norm bar chart, color-coded by channel; channel-2 expected to spike above 1e-6 and others to sit below 1e-12)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W8-5

### YAML
```yaml
gate_id: S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, CHAIN]
classification: GEOMETRIC
specialist: lizzi-spectral-functional-theorist
effort_hours: 4
```

---

## §W8-6. S87-CHANNEL-4-INDEPENDENCE-FROM-CHANNEL-3 (CF-52)

### 1. Gate ID
`S87-CHANNEL-4-INDEPENDENCE-FROM-CHANNEL-3`

### 2. Trigger
`[VERIFY]` + `[SIGN]`

### 3. Classification
GEOMETRIC (channel-orthogonality structural test; failure mode would be non-trivial logical implication between channels).

### 4. Hypothesis
Channel-3 (HBW positive-cone) and channel-4 (routing/coupling-Λ-scaling) of the W-8 4-channel decomposition are LOGICALLY INDEPENDENT. Operationally: there exists at least one regulator (real or constructed) that PASSes channel-4 and FAILs channel-3, OR PASSes channel-3 and FAILs channel-4. Existence of such a regulator certifies the channels are orthogonal as admissibility predicates; their conjunction is a non-trivial 2-test, not a redundant single test.

### 5. PASS / FAIL / INFO threshold

The producing script enumerates a candidate regulator set targeted at channel-3/channel-4 separation:
`R_separation_candidates := {ζ_with_α_negative_dressing, anomaly_with_Bernstein_violation, Schwinger_with_α_positive_dressing, hand_constructed_separation_R_a, hand_constructed_separation_R_b}`

For each candidate R:
- evaluate channel_3_PASS(R), channel_4_PASS(R) per the §W8-3 criteria
- check `independence(R) := (channel_3_PASS(R) XOR channel_4_PASS(R))` — i.e., one PASSes and the other FAILs

- **PASS**: ≥ 1 candidate has independence(R) = True. Channel-3 and channel-4 are operationally independent (logical XOR has a witness).
- **FAIL**: zero candidates have independence(R) = True. Either every candidate PASSes both channels (channels are jointly trivial on the candidate set), or every candidate FAILs both (jointly trivial in the failing direction). The candidate set IS the logical-independence test; if no separation witness exists in the set, channels appear logically dependent.
- **INFO**: a candidate is on the precision-floor boundary of one channel and FAIL on the other (e.g., channel_3 sub-INFO + channel_4 FAIL); records the boundary witness rather than a clean-XOR witness.

Tolerance rule: THEOREM (binary XOR predicate; the channel sub-thresholds are inherited from §W8-3 and §W8-4).

### 6. Machinery pin (PRDR)
- `N_eval`: ≈ 350,000 PW-signed eigenvalues at L_max=12
- `L_max`: 12
- `scan_range`: 5 candidate regulators × 2 channels (3, 4) = 10 cells; channel-4 α-scan ∈ [−2, +2] step 0.05 per candidate
- `step_size`: 0.05 (channel-4 α-scan)
- `tolerance`: inherited per channel from §W8-3 (channel-4 α ≥ 0 PASS) and §W8-4 (channel-3 5-subchannel HBW)
- `scheme`: 5-candidate × 2-channel XOR-witness search
- `convention`: candidates constructed by deliberately violating one channel's structural prerequisite; e.g., `hand_constructed_separation_R_a` chosen to satisfy positive-cone (channel-3 PASS) but with Λ-scaling forced negative (channel-4 FAIL); `hand_constructed_separation_R_b` chosen oppositely
- `random_seed`: 42 (deterministic for any candidate involving stochastic sampling; deterministic candidates ignore)
- `GPU path`: CPU sufficient

### 7. Input SHA-256 pins
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>`
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w8-workingpaper.md` (4-channel decomposition source) — `<computed-at-runtime>`
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` (W-8 channel anchors) — `<computed-at-runtime>`
- prior gate output (in this wave): `s87_w8_hbw_audit_atlas_a_4.npz` (channel-3 sub-channel anchors) — `<computed-at-runtime>` (cross-wave dependency: this gate runs AFTER §W8-4)

### 8. Expected output 4-tuple
`(value=(n_independence_witnesses, separation_winner_id_or_None), scheme=channel_3_4_XOR_witness_search, convention=A_4_plus_5_candidates, L_max=12)`

### 9. Substitution chain

```
Step 1 (definitions):
  candidate_set := R_separation_candidates (5 entries; per §6 enumeration)
  channel_3_PASS(R) := per §W8-4 aggregate definition (5-subchannel AND)
  channel_4_PASS(R) := per §W8-3 channel-4 definition (α ≥ 0 with bounded
                       coupling g(L) → finite as L → ∞)
  independence(R)   := channel_3_PASS(R) XOR channel_4_PASS(R)
  n_witnesses       := |{R ∈ candidate_set : independence(R)}|
  separation_winner := first R ∈ candidate_set with independence(R) (if any)

Step 2 (substitute):
  PASS predicate := n_witnesses ≥ 1
  FAIL predicate := n_witnesses = 0 AND no INFO-eligible candidate
  INFO predicate := n_witnesses = 0 AND ≥ 1 candidate has
                    (channel_3_subINFO XOR channel_4_PASS) or
                    (channel_3_PASS XOR channel_4_INFO)

Step 3 (simplify):
  XOR truth table (per candidate):
    channel_3_PASS  channel_4_PASS  independence
    ──────────────  ──────────────  ────────────
         T              T               F           (jointly admissible — A_4 baseline)
         T              F               T           (cone-positive but Λ-divergent witness)
         F              T               T           (cone-negative but Λ-bounded witness)
         F              F               F           (jointly inadmissible — cutoff_AL2010 mode)

  ⇒ channels are independent ↔ ≥ 1 witness in either off-diagonal cell.

Step 4 (direction):
  Pre-W8 direction prediction:
  - hand_constructed_separation_R_a: positive-monotonic w_R(λ) (PASSes 3a/b/c/d/e)
    + Λ-scaling deliberately set to α = -0.5 (FAILs channel-4) → cell (T, F).
    Witness candidate; expected PASS on independence(R_a).
  - hand_constructed_separation_R_b: w_R(λ) with deliberate Bernstein-density
    sign-flip at low-λ (FAILs 3c) + Λ-scaling absorbed via Hopf-cocycle
    inner-fluctuation lift to f_4 slot (PASSes channel-4) → cell (F, T).
    Witness candidate; expected PASS.
  - ζ_with_α_negative_dressing: ζ-regulator post-composed with sharp Λ ∝ L^{-0.3}
    (channel-4 FAIL; channel-3 PASS by Bernstein-monotonicity preservation)
    → cell (T, F). Backup witness.
  ⇒ direction: PASS likely; ≥ 2 witnesses in candidate set.

  Sign claim:
  - direction of the channel_3 / channel_4 PASS predicate flip is the
    structural consequence of the above truth table being non-trivially
    populated. The substitution chain reads off PASS direction from the
    truth-table diagonal vs off-diagonal occupancy.
```

### 10. What PASS / FAIL means for the solution space
- **PASS**: channels 3 and 4 are operationally independent admissibility predicates; the W-8 4-channel decomposition is non-redundant on the (3, 4) sub-pair. Future §VII.M layer-membership ladder rows can cite both channels with confidence that they encode distinct structural constraints.
- **FAIL**: no XOR witness in the candidate set. Either (i) channels 3 and 4 are logically dependent (e.g., channel-3 PASS implies channel-4 PASS by some unrecognized substrate identity) — would be a NEW STRUCTURAL DISCOVERY routing to a high-priority S88 theorem-extraction gate; OR (ii) the candidate set is too small / poorly chosen — routes to an extended candidate enumeration carry-forward.
- **INFO**: a witness lives on the precision-floor boundary of one channel; records the candidate as a "near-witness" and triggers a refinement carry-forward.

### 11. Owning agent
`lizzi-spectral-functional-theorist` (channel-decomposition orthogonality is a Mellin-cone-spec / spectral-cone audit; lizzi co-owns the W-8 channel framework with connes).

### 12. Producing script
`computations/s87_w8_channel_4_independence_from_channel_3.py`

### 13. Output artifacts
- Script: `computations/s87_w8_channel_4_independence_from_channel_3.py`
- Data: `computations/s87_w8_channel_4_independence_from_channel_3.npz` (5×2 PASS/FAIL grid; per-candidate channel_3 sub-channel breakdown; per-candidate channel_4 α_max + bounded-g flag; XOR witness tabulation)
- Plot: `computations/s87_w8_channel_4_independence_from_channel_3.png` (5-candidate × 2-channel matrix; XOR cells highlighted)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W8-6

### YAML
```yaml
gate_id: S87-CHANNEL-4-INDEPENDENCE-FROM-CHANNEL-3
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, SIGN]
classification: GEOMETRIC
specialist: lizzi-spectral-functional-theorist
effort_hours: 6
```

---

## §W8-7. S87-ZUBAREV-CHANNEL-1-2-4-VERIFY (CF-53)

### 1. Gate ID
`S87-ZUBAREV-CHANNEL-1-2-4-VERIFY`

### 2. Trigger
`[VERIFY]` + `[VERIFY-THEOREM]`

### 3. Classification
GEOMETRIC (axiom-native L2-FULLY-ADMISSIBLE singleton-claim binding test on Zubarev specifically).

### 4. Hypothesis
Zubarev regulator passes ALL of channels 1, 2, 4 (channel-1 axiom-sourcing minimality with cardinality ≤ 4; channel-2 inner-fluctuation lift admissible; channel-4 routing/Λ-scaling with α ≥ 0 and bounded g) at the L2 axiom-native slot. Combined with the W-8 GATE B/C result for the {dim, fin} axiom-sourcing of cutoff_AL2010, this verification — required to make the L2-FULLY-ADMISSIBLE singleton claim binding — closes the Open Question 1 from W-8 (whether L2-FULLY-ADMISSIBLE applies to Zubarev specifically as a singleton, not just to the {ζ, Zubarev, SDW, anomaly} ensemble).

### 5. PASS / FAIL / INFO threshold

For Zubarev specifically, evaluate each of channels {1, 2, 4} per the §W8-3 / §W8-6 thresholds:
- channel_1_PASS_Zubarev := axiom-sourcing cardinality ≤ 4 on the a_0 / a_2 / a_4 / a_6 channels (subset-removal sweep on CCM-2007 axiom set)
- channel_2_PASS_Zubarev := inner-fluctuation lift admissible (Hopf-cocycle dressing exists per Connes-Moscovici 1995 §III.4 generators)
- channel_4_PASS_Zubarev := α_max(Zubarev) ≥ 0 with bounded g(L) → finite as L → ∞

- **PASS**: all three channels PASS for Zubarev. The L2-FULLY-ADMISSIBLE singleton claim binds. The §VII.M layer-membership row for Zubarev is theorem-grade.
- **FAIL**: any one of the three channels FAILs for Zubarev. The L2-FULLY-ADMISSIBLE singleton claim does not bind for Zubarev alone; the W-8 §VII.K-PROP A/B/C-trio result must be re-narrated as ensemble-level only.
- **INFO**: any one channel sub-INFO; precision-floor.

Tolerance rule: THEOREM (binary admissibility); inherited sub-thresholds from §W8-3 (channel-4 α ≥ 0; cardinality ≤ 4 for channel-1) and connes-naturality criterion for channel-2.

### 6. Machinery pin (PRDR)
- `N_eval`: ≈ 350,000 PW-signed eigenvalues at L_max=12
- `L_max`: 12 (canonical); 7 for channel-1 subset-removal sweep matching W-8 GATE B
- `scan_range`:
  - channel-1: subset-removal over CCM-2007 axiom set {dim, reg, fin, real, 1st-order, orient, PD} for Zubarev's a_0/a_2/a_4/a_6 sourcing
  - channel-2: Hopf-cocycle inner-fluctuation lift via Connes-Moscovici 1995 §III.4 (R_universal, R_BDI, R_PV, R_anomaly)
  - channel-4: α ∈ [−2, +2] step 0.05 (matches GATE A scan)
- `step_size`: 0.05 (channel-4); subset-removal granularity = singleton remove-one-axiom (channel-1)
- `tolerance`: cardinality ≤ 4 (channel-1); Hopf-cocycle existence (channel-2 binary); α_max ≥ 0 with bounded g (channel-4)
- `scheme`: 3-channel chain test, Zubarev-specific
- `convention`: Zubarev weight `w_Z(λ) = (λ/Λ)² / (1 + (λ/Λ)⁴)` per CCM-2007 §1.143-1.145 and W-11 §2 anchor
- `random_seed`: 42 (deterministic)
- `GPU path`: CPU sufficient (Zubarev moments are scalar sums)

### 7. Input SHA-256 pins
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>`
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `sessions/permanent-results-registry.md` (§VII.K-PROP A/B/C trio anchor) — `<computed-at-runtime>`
- `sessions/archive/session-86/session-86-w8-workingpaper.md` (Open Question 1 source) — `<computed-at-runtime>`
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` — `<computed-at-runtime>`
- (post-§W8-3 dependency) `computations/s87_w8_c45_sixth_regulator_promotion.json` (channel-2 Hopf-cocycle infrastructure shared across W8 wave) — `<computed-at-runtime>`

### 8. Expected output 4-tuple
`(value=(channel_1_PASS_Z, channel_2_PASS_Z, channel_4_PASS_Z, alpha_max_Z), scheme=Zubarev_L2_axiom_native_3channel, convention=L2_FULLY_ADMISSIBLE_singleton_test, L_max=12)`

### 9. Substitution chain

```
Step 1 (definitions):
  Zubarev's a_n(L_max) := Σ_lambda multiplicity(λ) · λ^n · w_Z(λ; Λ=1)
  where w_Z(λ) = λ² / (1 + λ⁴)
  and the sum runs over all L_max=12 eigenvalues with positive multiplicity.

  channel_1_axiom_set_Zubarev := minimal CCM-2007 axiom subset that sources
                                 Zubarev's a_n moments via the GLOBAL-TRACE
                                 route a_n = Tr_H(λ^n · w_Z(λ)) / Vol_F
  channel_1_PASS_Z := |channel_1_axiom_set_Zubarev| ≤ 4

  channel_2_lift_Zubarev := Hopf-cocycle inner-fluctuation `δZ` such that
                            Zubarev + δZ admits a redirect of the L^8 Peter-Weyl
                            growth out of the a_0 channel (per CM-1995 §III.4)
  channel_2_PASS_Z := channel_2_lift_Zubarev exists

  k_eff_Zubarev(L) := log(a_0_Zubarev(L) / a_0_Zubarev(L-1)) / log(L/(L-1))
  alpha_max_Z       := −k_eff_Zubarev(L→∞) / 4
  channel_4_PASS_Z := alpha_max_Z ≥ 0 AND g(L) := f_0 · Λ_0^4 · L^{4·alpha_max_Z}
                      · a_0_Zubarev(L) bounded as L → ∞

Step 2 (substitute):
  Zubarev w_Z(λ) ~ λ² for λ → 0, ~ 1/λ² for λ → ∞ (heat-kernel-equivalent
  decay)
  ⇒ a_n_Zubarev(L_max) sums are dominated by mid-spectrum eigenvalues
    rather than the L^8 high-end (unlike cutoff_AL2010's sharp-cutoff
    sum-of-dim²).
  ⇒ k_eff_Zubarev does NOT inherit the L^8/960 leading term; instead it
    converges to a finite constant determined by the ∫ λ² · w_Z(λ) dν(λ)
    Stieltjes integral against the substrate spectral density ν(λ).

Step 3 (simplify):
  Zubarev's heat-kernel-derived decay ⇒ k_eff_Zubarev → finite as L → ∞
  ⇒ alpha_max_Z = −k_eff_∞ / 4 is FINITE
  ⇒ if k_eff_∞ ≤ 0 ⇒ alpha_max_Z ≥ 0 ⇒ channel_4 PASS direction
  ⇒ if k_eff_∞ > 0 ⇒ alpha_max_Z < 0 ⇒ channel_4 FAIL direction (analogous
    to cutoff_AL2010, but with finite k_eff rather than k_eff = 8)

  Sub-prediction: Zubarev's λ² weight at small λ DOMINATES the spectral
  sum's growth; for the Jensen-deformed SU(3) substrate with bounded
  spectral density ν(λ) on [λ_min, λ_max], the sum is bounded as L → ∞
  ⇒ k_eff_∞ → 0 ⇒ alpha_max_Z → 0 ⇒ channel_4 PASS.

Step 4 (direction):
  channel_1_PASS_Z direction: Zubarev is heat-kernel-derived (CCM-2007
  §1.143-1.145), which sources from {dim, reg, fin}; cardinality 3 ≤ 4
  ⇒ PASS direction confirmed.

  channel_2_PASS_Z direction: heat-kernel-derived regulators admit
  Hopf-cocycle inner-fluctuation by the CM-1995 generator structure;
  Zubarev's `(λ/Λ)² / (1 + (λ/Λ)⁴)` is a rational deformation of
  Pauli-Villars-equivalent form, so channel-2 lift exists by construction
  ⇒ PASS direction confirmed.

  channel_4_PASS_Z direction: as derived in Step 3, k_eff_∞_Zubarev is
  bounded; provided ν(λ) admits no L^8 contamination at high-λ (which
  it does NOT for Zubarev's mid-spectrum weighting), alpha_max_Z ≥ 0
  ⇒ PASS direction predicted; verification by the script's L-scan is
  the evidential step.
```

### 10. What PASS / FAIL means for the solution space
- **PASS**: Zubarev binds the L2-FULLY-ADMISSIBLE singleton claim. Open Question 1 from W-8 closes; the §VII.K-PROP A/B/C trio's L2-FULLY-ADMISSIBLE conclusion applies to Zubarev individually as a theorem-grade row, not just as part of the {ζ, Zubarev, SDW, anomaly} ensemble.
- **FAIL**: Zubarev does NOT bind the singleton claim. The W-8 §VII.K-PROP closure must be re-narrated as ensemble-level admissibility only; future §VII.M layer-membership ladder rows for Zubarev specifically are demoted to candidate-grade.
- **INFO**: precision-floor on the channel-4 α_max bound; the sub-claim is on the boundary of the bounded-g region. Carry-forward to L_max=14 for tighter bound.

### 11. Owning agent
`connes-ncg-theorist` (axiom-native L2 admissibility chain on Zubarev specifically; same agent who landed §VII.K-PROP at S86 W1a-1).

### 12. Producing script
`computations/s87_w8_zubarev_channel_1_2_4_verify.py`

### 13. Output artifacts
- Script: `computations/s87_w8_zubarev_channel_1_2_4_verify.py`
- Data: `computations/s87_w8_zubarev_channel_1_2_4_verify.npz` (channel_1 axiom-set table, channel_2 Hopf-cocycle existence + lift identity, channel_4 α_max + L-scan trace + bounded-g flag)
- Plot: `computations/s87_w8_zubarev_channel_1_2_4_verify.png` (3-panel: channel-1 axiom subset diagram, channel-2 Hopf-cocycle lift identity verification, channel-4 α-scan with PASS bounded-region highlighted)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W8-7

### YAML
```yaml
gate_id: S87-ZUBAREV-CHANNEL-1-2-4-VERIFY
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, VERIFY-THEOREM]
classification: GEOMETRIC
specialist: connes-ncg-theorist
effort_hours: 5
```

---

## §W8-8. S87-ETA-GV-FOLLOWUP (CF-65)

### 1. Gate ID
`S87-ETA-GV-FOLLOWUP`

### 2. Trigger
`[VERIFY]` + `[VERIFY-THEOREM]` + `[SIGN]`

### 3. Classification
PHONONIC × GEOMETRIC (η-invariant + Godbillon-Vey-Heitsch invariant on substrate (C_H, C_epsH) parity-twin pair; HP^1 odd-grading detection under regulator atlas).

### 4. Hypothesis
The Godbillon-Vey-Heitsch (GV) invariant evaluated on the (C_H, C_epsH) parity-twin channel is REGULATOR-INDEPENDENT under all 5 atlas regulators in A_5_extended = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}, with regulator-spread `max_{r ∈ A_5_extended} |GV_r(C_H) − GV_r(C_epsH) − GV_canonical_difference|` ≤ 1e-12. (cutoff_sqrt is included as legacy diagnostic per the W-11 calibration corpus; the gate verifies regulator-independence including the legacy regulator. If regulator-independence holds even when cutoff_sqrt is included, the structural conclusion is robust against atlas-cardinality changes.)

This gate cites the supersession-event precedent in `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension": the W-11 plan threshold tested η-difference, but η is parity-blind by Bulletin #2 promoted theorem; the structurally correct probe is the ODD-grading observable GV-Heitsch (not η). This follow-up uses GV-Heitsch as the OBSERVABLE OF RECORD; η is reported as a CONFIRMATION of parity-blindness only.

### 5. PASS / FAIL / INFO threshold

Sub-tests:

**Sub-test (a) — η parity-blindness regulator-invariance** (confirmation per Bulletin #2):
- compute `eta_r(C_H) − eta_r(C_epsH)` for r ∈ A_5_extended
- **sub-PASS_a**: `max_r |eta_r(C_H) − eta_r(C_epsH)| < 1e-13` (parity-blindness theorem holds across atlas; W-11 result holds)

**Sub-test (b) — GV-Heitsch regulator-independence** (PRIMARY observable):
- compute `gv_r(C_H) − gv_r(C_epsH)` for r ∈ A_5_extended
- compute `gv_spread := max_{r ∈ A_5_extended} |gv_r(C_H) − gv_r(C_epsH) − gv_canonical_difference|` where `gv_canonical_difference := −40579.15` is the W-11 anchor
- **sub-PASS_b**: `gv_spread < 1e-12` (regulator-INDEPENDENT)
- **sub-FAIL_b**: `gv_spread ≥ 1e-9`
- **sub-INFO_b**: `1e-12 ≤ gv_spread < 1e-9` (precision-floor)

**Sub-test (c) — GV non-vanishing magnitude check** (substrate detection certificate):
- **sub-PASS_c**: `min_r |gv_r(C_H) − gv_r(C_epsH)| > 1e-6` (HP^1 detection retained across the full atlas; the W-11 magnitude ~16 OOM above threshold is preserved at L_max=10 and L_max=12)

Aggregate:
- **PASS**: sub-PASS_a AND sub-PASS_b AND sub-PASS_c
- **FAIL**: sub-FAIL_b OR sub-test_a violation (η regulator-spread ≥ 1e-13) OR sub-test_c violation (some r yields gv difference ≤ 1e-6)
- **INFO**: sub-INFO_b AND PASS on the other two

Tolerance rules: RATIO for sub-test (b); ABSOLUTE for sub-tests (a) and (c).

### 6. Machinery pin (PRDR)
- `N_eval`: ≈ 155,000 PW-signed eigenvalues at L_max=10 (per W-11 §2 anchor: 65 distinct positive λ × multiplicity); cross-check at L_max=12
- `L_max`: 10 (canonical, matches W-11); 12 (cross-check)
- `scan_range`: 5 atlas regulators × 2 corridors (C_H, C_epsH) × 2 invariants (η, GV) = 20 evaluations × 2 L_max = 40 cells total
- `step_size`: N/A (single-evaluation per cell)
- `tolerance`: per §5 sub-test thresholds
- `scheme`: η via Mellin-cone moment of eta-function `ζ_η(s) = Tr(D|D|^{−s−1}) · χ_C` evaluated at s=0; GV via S83 G56 Heitsch-variation infrastructure (Dixmier-regularized transversal integral per W-11 §3)
- `convention`: corridors per S85 W2-7 catalog `s85_w2_disjoint_corridor_counter_construction.json` (composite_id LZ-S7-11); regulators per W-11 §2 weights w_r(λ); GV computed via S84 W10-115 explicit-construction script that closed the S83 G56 Heitsch-variation test
- `random_seed`: 42 (deterministic; GV stencil error pinned at 6.948e-13 per W-11)
- `GPU path`: GPU recommended for the L_max=12 cross-check eigenvalue load (use `torch.linalg.eigh` on AMD RX 9070 XT per `.claude/rules/computation-environment.md`); CPU sufficient for L_max=10 evaluation since data are loaded from cache; `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy` for CPU path

### 7. Input SHA-256 pins
- `computations/s84_spectrum_cache_L10_tau019.npz` — `<computed-at-runtime>`
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>` (cross-check)
- `computations/s85_w2_disjoint_corridor_counter_construction.json` — `<computed-at-runtime>` (corridor catalog with composite_id LZ-S7-11)
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `computations/s86_w11_eta_gv_joint_probe.npz` (W-11 anchor data) — `<computed-at-runtime>`
- `computations/s86_w11_eta_gv_joint_probe.py` (W-11 source script for refactor reference) — `<computed-at-runtime>`
- `computations/s86_w9_C24_parity_extension.npz` (HP^0 cross-anchor) — `<computed-at-runtime>`
- (S83/S84 GV infrastructure) `computations/s84_w10_115_gv_heitsch_explicit_construction.py` and `s84_w10_115_gv_heitsch_explicit_construction.npz` — `<computed-at-runtime>` (S83 G56 closure)

### 8. Expected output 4-tuple
`(value=(eta_max_spread, gv_spread, gv_min_magnitude), scheme=eta_GV_5_atlas_regulator_independence, convention=A_5_extended_with_legacy_cutoff_sqrt, L_max=10)`

### 9. Substitution chain (per `.claude/rules/inheritance-falsifier-protocol.md` cohomology-asymmetry test class B + `.claude/rules/regulator-pin-discipline.md` §Class-(c) supersession precedent)

```
Step 1 (definitions):
  η_r(C) := lim_{s→0+} Σ_n sign(μ_n) · w_r(λ_n; s) · ⟨ε_C, ε_C⟩_n
  (per W-11 §2 Step 1; r ∈ A_5_extended; w_r is the regulator weight per
  W-11 §2 anchors)

  GV_r(C) := the regulator-r-weighted Heitsch-variation evaluation on
  the corridor C, per S83 G56 docstring §D1-D4:
    GV_proxy_r(τ) := Σ_n ρ_n · d(ln λ_n)/dτ · |λ_n|^{−4} · w_r(|λ_n|; s=0) · ⟨ε_C, ε_C⟩_n
  with the standard Heitsch normalization integrated over the foliation's
  transversal 1-form ω_J = dτ.

  delta_eta_r := η_r(C_H) − η_r(C_epsH)
  delta_GV_r := GV_r(C_H) − GV_r(C_epsH)
  GV_canonical_difference := -40579.15 (W-11 §3 anchor; obtained at the
                              "canonical regulator" = direct S84 W10-115
                              non-regulator-weighted GV stencil)

  eta_max_spread := max_{r ∈ A_5_extended} |delta_eta_r|
  gv_spread     := max_{r ∈ A_5_extended} |delta_GV_r − GV_canonical_difference|
  gv_min_magnitude := min_{r ∈ A_5_extended} |delta_GV_r|

Step 2 (substitute):
  Per W-11 §2 Step 3 (parity-blindness theorem; Bulletin #2 PROMOTED):
  η_r is an even-grading observable: η_r pairs against the SYMMETRIC
  kernel of D_K² (positive heat-kernel weight w_r is a function of |λ|
  only, hence even in μ).
  ⇒ η_r(C_H) − η_r(C_epsH) = 0 EXACTLY by parity-grading orthogonality
    (HP^1 ε_H twist lives in ODD cyclic cohomology and has NO image
    under ch: K_0(A_F) → HP^0(A_F)).
  ⇒ delta_eta_r = 0 for every r ∈ A_5_extended ⇒ eta_max_spread = 0.
  Sub-test (a) PASS direction confirmed structurally.

  Per W-11 §3 anchor + S83 G56 derivation:
  GV_r(C) is an ODD-grading observable: it pairs against the
  ANTI-symmetric kernel of d/dτ (the Heitsch-variation lifts the
  HP^1 ε_H twist to a non-vanishing transversal-integral pairing).
  ⇒ delta_GV_r = GV_r(C_H) − GV_r(C_epsH) ≠ 0 generically.

  REGULATOR-INDEPENDENCE substrate identity:
  GV_r(C) = ⟨[ε_H], [Ch_GV(D, w_r)]⟩
  where Ch_GV is the GV-Chern character on the K-theoretic boundary
  derived from D and dressed by the regulator weight w_r.
  By Connes-Karoubi pairing on HP^*, the HP^1 cohomology class [ε_H]
  is INVARIANT under regulator-class-preserving deformations of w_r;
  positive-weight regulators in A_5_extended preserve the parity grading
  (they are functions of |λ| only) and therefore do NOT change the
  Connes-Karoubi pairing on HP^1.
  ⇒ GV_r(C) is INVARIANT under r ∈ A_5_extended.
  ⇒ delta_GV_r = GV_canonical_difference EXACTLY for every r.
  ⇒ gv_spread = 0 (structural prediction).

Step 3 (simplify):
  PASS_aggregate := (eta_max_spread < 1e-13)
                    AND (gv_spread < 1e-12)
                    AND (gv_min_magnitude > 1e-6)

Step 4 (direction):
  Direction prediction:
  - sub-test (a) PASS: η-blindness across atlas (W-11 §2 result;
    delta_eta_r = 0 for all r); confirmed structurally.
  - sub-test (b) PASS: GV regulator-INDEPENDENCE (substrate identity
    above; delta_GV_r = GV_canonical_difference for all r).
  - sub-test (c) PASS: |GV_canonical_difference| = 40579.15 ≫ 1e-6
    (~16 OOM above threshold per W-11 §3); confirmed.

  Sign claim (per [SIGN] trigger):
  GV_canonical_difference = -40579.15 (NEGATIVE by W-11 §3).
  Direction: GV_r(C_H) < GV_r(C_epsH) for all r ∈ A_5_extended
  (the C_epsH corridor's HP^1 ε_H twist creates a positive
  contribution to GV_r(C_epsH) relative to GV_r(C_H), so the
  difference is negative). The sign-PASS verdict requires
  sign(delta_GV_r) = sign(GV_canonical_difference) = -1 for all r.

  Composite collapse rule (per `.claude/rules/gate-verdicts.md`
  S87+ schema-v2):
    sign_verdict      = PASS  iff sign(delta_GV_r) = -1 for all r AND
                                  delta_eta_r = 0 for all r
    magnitude_verdict = PASS  iff PASS_aggregate (above)
    regime_verdict    = VALID iff L_max=10 / L_max=12 cross-check
                                  agrees within 1e-9 (regulator-class-
                                  preserving deformations are within
                                  validity regime; truncation at
                                  L_max=10 is canonical)
```

### 10. What PASS / FAIL means for the solution space
- **PASS**: GV-Heitsch invariant is regulator-INDEPENDENT under the full A_5_extended atlas (including legacy cutoff_sqrt). The substrate's HP^1 detection mechanism is operationally robust against regulator choice; the Bulletin #2 parity-blindness theorem and the W-11 §3 GV detection certificate are CONFIRMED and STRENGTHENED. Future falsifier-protocol gates testing the (C_H, C_epsH) channel can use ANY regulator from A_5_extended without affecting the GV-detection result. The W-11 follow-up Open Question closes; CF-65 is RESOLVED.
- **FAIL on sub-test (a)**: η-blindness violated under some regulator. Bulletin #2 parity-blindness theorem is contradicted; this would be a STRUCTURALLY MAJOR negative result requiring re-derivation of the parity-grading orthogonality claim. Routes to high-priority S88 Bulletin #2 retraction gate.
- **FAIL on sub-test (b)**: GV regulator-spread above 1e-9. The Connes-Karoubi pairing on HP^1 is NOT regulator-invariant under A_5_extended; the substrate identity in Step 2 has an unidentified regulator-dependent correction. Routes to S88 GV-regulator-correction-derivation gate.
- **FAIL on sub-test (c)**: GV magnitude below 1e-6 for some r. The HP^1 detection is regulator-suppressed under that r; GV-Heitsch is not a fully robust HP^1 detector. Routes to alternative odd-grading observable search (K-theoretic torsion, η-Cheeger-Simons secondary classes per `.claude/rules/regulator-pin-discipline.md` §"Forward-looking remediation").
- **INFO**: precision-floor on regulator-spread; documents the achievable HP^1-regulator-independence floor at L_max=10/12.

### 11. Owning agent
`gen-physicist` PRIMARY (per CF-65 W-11 recommending agent column); `volovik-superfluid-universe-theorist` CO-SIGN (per inheritance-falsifier-protocol substrate competence; the GV-Heitsch invariant is the cohomology-asymmetry test class B observable per `.claude/rules/inheritance-falsifier-protocol.md` §"Two Test Classes" Class B).

### 12. Producing script
`computations/s87_w8_eta_gv_followup.py`

### 13. Output artifacts
- Script: `computations/s87_w8_eta_gv_followup.py`
- Data: `computations/s87_w8_eta_gv_followup.npz` (5×2×2 grid: regulators × corridors × invariants {η, GV}; per-cell values + delta tables; eta_max_spread, gv_spread, gv_min_magnitude)
- Plot: `computations/s87_w8_eta_gv_followup.png` (2-panel: left = η deltas across atlas (expected 0 across; horizontal at zero), right = GV deltas across atlas (expected -40579.15 across; horizontal anchor with regulator-spread error bars))
- Verdict line: appended to `computations/s87_gate_verdicts.txt` (S87+ schema-v2 with 3-tuple annotation since `[SIGN]` trigger is present)
- Working-paper section: §W8-8

### YAML
```yaml
gate_id: S87-ETA-GV-FOLLOWUP
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: [VERIFY, VERIFY-THEOREM, SIGN]
classification: PHONONIC × GEOMETRIC
specialist: gen-physicist
co_sign: volovik-superfluid-universe-theorist
effort_hours: 2
```

---

## Wave 8 → Wave 9 Decision Point

W8 closes the structural carry-forward bundle from S86 W-8 (cutoff_sqrt cascade plumbing) plus the S86 W-11 single follow-up (η-GV regulator-INDEPENDENCE). The decision-point logic for W9 dispatch:

| W8 verdict pattern | W9 dispatch consequence |
|:-------------------|:-----------------------|
| All 8 PASS | W9 dispatches normally; A_4 atlas baseline binding; CF-65 closes; the L2-FULLY-ADMISSIBLE singleton claim binds for Zubarev. |
| §W8-3 (CF-49) PASS (sixth-regulator promotion) | A_4 → A_5_v2; W9 plan re-narrates atlas-cardinality assertions to A_5_v2; legacy A_4 references downgraded to "post-W-8 / pre-W8-3" historical. |
| §W8-3 (CF-49) FAIL with PARTIAL-INFO | A_4 stays canonical; "depth-extension" carry-forward to S88. |
| §W8-1 (CF-47) FAIL or INFO | residual cutoff_sqrt load-bearing cite manually flagged; W9 unaffected; carry-forward to S88. |
| §W8-2 (CF-48) FAIL on (a) | A_4 max_pair_ratio extremum diverges from A_5; new value becomes canonical max_pair_ratio; W4-2 working paper re-narration carry-forward. |
| §W8-2 (CF-48) FAIL on (b) | cluster-span identity broken; HIGH-PRIORITY S88 regression debug carry-forward. |
| §W8-4 (CF-50) FAIL | HBW positivity violation in A_4; A_4 → A_3 cascade investigation carry-forward. |
| §W8-5 (CF-51) FAIL on channel-2 silence | live-Mellin infrastructure regression; S88 infrastructure-debug carry-forward. |
| §W8-5 (CF-51) FAIL on non-channel-2 leakage | 4-channel decomposition is non-orthogonal; S88 channel-decomposition revision carry-forward. |
| §W8-6 (CF-52) FAIL | NEW STRUCTURAL DISCOVERY (channels 3 and 4 logically dependent); HIGH-PRIORITY S88 theorem-extraction carry-forward. |
| §W8-7 (CF-53) FAIL | L2-FULLY-ADMISSIBLE singleton claim does not bind for Zubarev; W-8 §VII.K-PROP closure re-narrated as ensemble-only. |
| §W8-8 (CF-65) FAIL on sub-test (a) | Bulletin #2 parity-blindness theorem CONTRADICTED; high-priority S88 Bulletin #2 retraction. |
| §W8-8 (CF-65) FAIL on sub-test (b) | GV regulator-spread above 1e-9; S88 GV-regulator-correction-derivation. |
| §W8-8 (CF-65) FAIL on sub-test (c) | GV-Heitsch is regulator-suppressed; S88 alternative odd-grading observable search per `.claude/rules/regulator-pin-discipline.md` §"Forward-looking remediation". |

W8 is COMPUTE-class throughout; no METHODOLOGY-class deliverables propagate out of W8 → W9. The W9 plan-author reads this decision-point block to scope post-W8 carry-forwards.

---

## Wave 8 Machinery-Enumeration Pin (§0.11)

PRDR machinery enumeration per `.claude/rules/epistemic-discipline.md` §"PRU Pre-Registration Completeness":

| Gate | Free parameters enumerated | Pin OR diagnostic-tag status |
|:-----|:--------------------------|:----------------------------|
| §W8-1 | `target_files_set`, `pattern_regex`, `LEGACY_FLAG_TEMPLATE`, `curated_root_filelist` | ALL PINNED in §6 (target = 6 files; regex = `\bcutoff_sqrt\b`; flag template = `[LEGACY: cascade A_5→A_4 per S86 W-8 GATE A FAIL]`; curated_root = root-level Phononic-*/framework-* files) |
| §W8-2 | `L_max`, `cluster_span_mode`, `max_pair_ratio_atlas_columns`, `precision_metric_choice` | ALL PINNED (L_max=12 for cluster-span / 10 for max_pair_ratio; mode = `_cluster_span_extract.py` callable; columns = A_4; metric = `\|ratio − 2\|` per `.claude/rules/epistemic-discipline.md` §"Canonical-metric pin extension") |
| §W8-3 | `candidate_set`, `channel_subtests_set`, `subset_removal_axiom_set`, `alpha_scan_grid`, `Hopf_cocycle_dressing_space`, `MP_abs_conv_residue_anchors`, `layer_membership_target_row` | ALL PINNED in §6 (candidate set = 5 enumerated; channels = 4 enumerated; axiom set = CCM-2007 7-element; α-scan = [-2,+2] step 0.05; dressing space = CM-1995 §III.4 generators; residue anchors = f_2/f_4/f_6 framework-truncated; target row = §VII.M) |
| §W8-4 | `subchannel_set`, `Hankel_matrix_order`, `Bernstein_derivative_orders`, `Widder_inversion_kappa_threshold`, `framework_residue_truncation` | ALL PINNED (subchannels = 5 enumerated; Hankel order = 4; Bernstein orders k ∈ {0,1,2,3}; κ < 1e15; f_2/f_4/f_6 = 0.0/0.05/0.1) |
| §W8-5 | `mellin_cone_live_toggle_set`, `channel_decomposition_set`, `regulator_set`, `level_pin_per_helper`, `bite_threshold`, `leak_threshold` | ALL PINNED (toggle = {True, False}; channels = 4 enumerated; regulators = A_4; level pin DECLARED at runtime per §6 (`level_pin_per_helper` = PRIMARY if live-Mellin is full physical / SCHEMATIC if SCHEMATIC); thresholds 1e-6 / 1e-12 / 1e-9) |
| §W8-6 | `candidate_set`, `XOR_witness_threshold`, `channel_3_subchannel_inheritance_pin`, `channel_4_inheritance_pin` | ALL PINNED (candidates = 5 enumerated; XOR = binary; sub-thresholds inherited from §W8-3/§W8-4) |
| §W8-7 | `axiom_subset_removal_protocol`, `Hopf_cocycle_lift_existence_proof_protocol`, `alpha_scan_grid`, `Zubarev_weight_form` | ALL PINNED (subset-removal = remove-one-axiom on CCM-2007 7-element set; Hopf-cocycle existence via CM-1995 §III.4 generator existence test; α-scan = [-2,+2] step 0.05; w_Z = (λ/Λ)²/(1+(λ/Λ)⁴)) |
| §W8-8 | `regulator_set`, `corridor_pair`, `invariant_set`, `L_max_set_with_canonical`, `eta_threshold`, `gv_spread_threshold`, `gv_magnitude_floor`, `gv_canonical_difference_anchor`, `regime_validity_cross_check_threshold` | ALL PINNED (regulators = A_5_extended 5-element; corridor = (C_H, C_epsH) per LZ-S7-11; invariants = {η, GV}; L_max = {10 canonical, 12 cross-check}; thresholds 1e-13 / 1e-12 / 1e-6; anchor = -40579.15; cross-check 1e-9) |

Wave 8 PRU cardinality status: ALL PINS DECLARED. Zero free machinery parameters at execution time. Plan-freeze auditor `_pru_cardinality_audit.py` should return `D_PRU_raw = 0` for each gate.

Source-reconciliation status (per `.claude/rules/epistemic-discipline.md` §"Source Reconciliation"):
- §W8-1: no canonical-pin drift (mechanical text-pass)
- §W8-2: cluster-span canonical metric `|ratio − 2|` MATCHES W0-3 CC-5 anchor (Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY closed at W2-4); no drift
- §W8-3: candidate set pre-enumerated; no canonical existing for any of 5 candidates (NEW carry-forward content); zero drift
- §W8-4: HBW thresholds derived from BWB-1929 / Widder-1934 textbook results; numerical thresholds (1e-12, 1e-15, 1e-10) at precision-floor band (D_max < 0.1 per `.claude/rules/epistemic-discipline.md` SR 4-band); no drift
- §W8-5: level pin DECLARED per `.claude/rules/substrate-first-canonical-sourcing.md` §"W4-2 SCHEMATIC vs full physical level rule"; SCHEMATIC undisclosed audit → PASS (level pin present)
- §W8-6: thresholds inherited from §W8-3/§W8-4; no drift
- §W8-7: Zubarev weight form per CCM-2007 §1.143-1.145 anchor; no drift
- §W8-8: GV_canonical_difference = -40579.15 from W-11 §3; SHA-pinned at runtime; no drift. Cites `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension" supersession-event precedent (η-arm is parity-blind per Bulletin #2 promoted theorem; the structurally correct probe is GV-Heitsch ODD-grading observable; this gate uses GV as PRIMARY observable per the supersession remediation).

Substrate-first canonical-sourcing audit (per `.claude/rules/substrate-first-canonical-sourcing.md`):
- §W8-1..§W8-7: substrate-first source = `computations/s84_spectrum_cache_L{10,12}_tau019.npz` + `_cluster_span_extract.py` (substrate computation, not external paper). PASS.
- §W8-8: substrate-first source = `s86_w11_eta_gv_joint_probe.npz` + `s84_w10_115_gv_heitsch_explicit_construction.npz` + canonical `s84_spectrum_cache_L10_tau019.npz`. PASS.

---

## Wave 8 Input-SHA Ledger

All input-SHA pins are computed at runtime by the producing script and recorded in the script's first 20 stdout lines per `.claude/rules/gate-verdicts.md`. The ledger entries below are the structural inventory; SHA values are NOT pre-pinned at plan-freeze (per the no-hardcoding rule for closure SHAs).

**Cross-wave shared inputs** (pinned in multiple gates above):
- `computations/canonical_constants.py` (§W8-1, §W8-2, §W8-3, §W8-4, §W8-5, §W8-6, §W8-7, §W8-8)
- `computations/s84_spectrum_cache_L12_tau019.npz` (§W8-2, §W8-3, §W8-4, §W8-5, §W8-6, §W8-7, §W8-8)
- `computations/s84_spectrum_cache_L10_tau019.npz` (§W8-4 cross-check, §W8-8 canonical)
- `computations/s86_gate_verdicts.txt` (§W8-1, §W8-2, §W8-3) — the GATE A FAIL canonical-record line + W4-2 max_pair_ratio_A5 anchor + §VII.K-PROP A/B/C trio anchor
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` (§W8-1, §W8-2, §W8-3, §W8-6, §W8-7)
- `sessions/archive/session-86/session-86-w8-workingpaper.md` (§W8-3, §W8-4, §W8-5, §W8-6, §W8-7) — channel decomposition source
- `sessions/permanent-results-registry.md` (§W8-3, §W8-7) — §VII.M layer-membership row + §VII.K-PROP A/B/C trio anchor

**Gate-specific inputs**:
- §W8-1: 4 working-paper sources (W4-2, W6, W12, W13)
- §W8-2: `_cluster_span_extract.py`, `s86_w2_c12_cluster_span_self_test.py`
- §W8-3: NONE additional (5 candidates constructed in-script)
- §W8-4: NONE additional
- §W8-5: `_spectral_action_regulators.py`, `session-86-w4-2-workingpaper.md`
- §W8-6: post-§W8-4 cross-wave dependency on `s87_w8_hbw_audit_atlas_a_4.npz`
- §W8-7: post-§W8-3 cross-wave dependency on `s87_w8_c45_sixth_regulator_promotion.json`
- §W8-8: `s85_w2_disjoint_corridor_counter_construction.json` (LZ-S7-11 corridor catalog), `s86_w11_eta_gv_joint_probe.npz`, `s86_w11_eta_gv_joint_probe.py`, `s86_w9_C24_parity_extension.npz`, `s84_w10_115_gv_heitsch_explicit_construction.py`, `s84_w10_115_gv_heitsch_explicit_construction.npz`

**Cross-wave dispatch order** within W8:
1. §W8-1, §W8-2, §W8-4, §W8-5, §W8-8 may dispatch in parallel (no intra-wave dependencies; all inputs pre-existing)
2. §W8-3 may dispatch in parallel with the above
3. §W8-6 dispatches AFTER §W8-4 completes (consumes `s87_w8_hbw_audit_atlas_a_4.npz`)
4. §W8-7 dispatches AFTER §W8-3 completes (consumes `s87_w8_c45_sixth_regulator_promotion.json` for shared Hopf-cocycle infrastructure)

Concurrent dispatch wave plan: 6 parallel (§W8-1, §W8-2, §W8-3, §W8-4, §W8-5, §W8-8) + 2 sequential (§W8-6 after §W8-4, §W8-7 after §W8-3). Maximum concurrent agent count = 6 ≤ 8 cap.

**End of session-87-plan-w8.md**.
