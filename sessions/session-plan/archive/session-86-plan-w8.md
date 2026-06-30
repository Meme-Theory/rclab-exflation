# Session 86 Plan — Wave W8: CGWB three-layer (P6 + P7 + C7)

**Generated**: 2026-04-25
**Owner**: `mack-cosmic-bridge`
**Output verdict file**: `computations/s86_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)
**Working-paper target**: `sessions/archive/session-86/session-86-w8-workingpaper.md` (created at compute time)
**Item count**: 3 (P6 + P7 + C7)
**Source**: `sessions/session-plan/session-86-partition.md` §1 Wave W8 + `sessions/session-plan/session-86-context.md` §2.2 (P6, P7) + §2.6 (C7)

---

## §0. Wave W8 Summary

Three gates close the **6A CGWB ⊥ α_s three-layer adjudication** opened at S85 close (context §1.3, surviving open channel #6A; context §1.2 W13-2 INFO verdict-line). The S85 W13-2 single-arm gate produced
`(α_s=−0.068968, Ω_GW(LISA)=8.299e−58, ρ_CGWB,α_s=0, Fisher PD=1)` under
`scheme=zeta, convention=LISA-PLS-2024+CMB-S4-Book-2019, L_max=10` and was tagged INFO because the §(f) band-width-diagnostic exceeded 20% — a numerical proxy that, on review (mack 9A §VI.1), measures **spectral slope**, not **truncation-sensitivity**. The mack 9A synthesis additionally noted that LAYER-3 (substrate-marginalized-observable) ρ over the W12-4 5-regulator atlas spot-checked at Pearson |ρ| ≈ 0.91 (R3), in tension with the LAYER-2 ρ=0 verdict. The 6A workshop converged on a **three-layer adjudication methodology** (parameter / experimental-Fisher / substrate-marginalized-observable); the methodology entry itself lands in **W0b R8** (which W8 depends on).

This wave commits the three deliverables that close the methodology open channel:
- **P6** (audit-class, registry-write): the **3-arm × 3-layer 9-cell diagrammatic commit** with 6 pre-registered pin axes.
- **P7** (substrate-prediction layer): the **LAYER-3 ρ Monte Carlo** over the W12-4 5-regulator atlas with sign-convention and atlas-weighting pre-pinned.
- **C7** (geometric-class): the **L_max-direct CGWB diagnostic** (L=8 vs L=10 spectrum at f_LISA = 3 mHz) replacing the W13-2 §(f) band-width proxy.

P6 and P7 can dispatch in parallel; C7 is independent of both. All three feed downstream **W13 P11 master-inventory** (LAYER-3 row class) and **W13 W3 watchlist edits** (Row #7 ρ_CGWB Companion-null-(C-regulator) column). Substrate framing throughout: every ρ value reports the substrate's CGWB ⊥ α_s correlation under regulator y, NOT an LCDM null-hypothesis test.

---

## §0.5. Wave W8 Decision-Point Prerequisites

W8 has **HARD plan-write dependencies** on:

1. **W0b R7** (`S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY`) — the four-witness single-name-conflation methodology entry must exist in `sessions/permanent-results-registry.md` before P6's diagrammatic commit can cite it as the meta-rule that licenses the 3-arm split (the 6A "ρ" was conflated across three semantically-distinct definitions; this is one of the four canonical witnesses per closeout §5).

2. **W0b R8** (`S86-PRR-THREE-LAYER-ADJUDICATION`) — the three-layer adjudication methodology entry (parameter / experimental-Fisher / substrate-marginalized-observable). Without R8 landed, the P6 diagrammatic commit is documenting an unannounced methodology and P7's LAYER-3 framing has no registry anchor.

W8 can plan-write in parallel with W0b (each planner reads `session-86-context.md` independently). At **compute time**, W0b verdict-lines for R7 + R8 must appear in `computations/s86_gate_verdicts.txt` BEFORE P6 + P7 + C7 dispatch, OR (per `feedback_dispatch-discipline.md`) P6 + P7 dispatch with a runtime-mismatch handler that flags the missing methodology entries as a CHAIN warning and lands provisional registry slots that the W0b R7/R8 closure later promotes.

---

## §I. Carry-Forward Items Mapping

| Wave-item | Source manifest entry | Source synthesis | Effort | PRDR class |
|:----------|:----------------------|:-----------------|:-------|:-----------|
| **W8-1 / P6** `S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT` | partition §1 W8 item 1 = context §2.2 P6 | gen-physicist 9A §4.10a + mack 9A §IV.3 | 0.5 wave | AUDIT (registry-write) |
| **W8-2 / P7** `S86-RHO-SUBSTRATE-PREDICTION-MC` | partition §1 W8 item 2 = context §2.2 P7 | mack 9A §VI.2 | 4-6h | VERIFY + SIGN |
| **W8-3 / C7** `S86-CGWB-LMAX-DIRECT` | partition §1 W8 item 3 = context §2.6 C7 | mack 9A §VI.1 | 1-2h | VERIFY |

**Wave-sum effort**: 6-9h total compute (P6 0.5 wave registry-write ≈ 2-3h + P7 4-6h + C7 1-2h). P6 + P7 in parallel, C7 independent → wall-time ≈ 4-6h on 2 concurrent agents.

---

## §W8-1. S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT (P6)

### 1. Gate ID
`S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT`

### 2. Trigger
**[AUDIT]** — diagrammatic commit is an audit-class clarification of the S85 W13-2 INFO verdict; it does not produce a new physics measurement but commits the methodology that interprets the existing measurement. Per `.claude/rules/gate-verdicts.md`, [AUDIT] gates compute against a structural-completeness threshold (all 9 cells present, all 6 pin axes documented), not a physical-quantity threshold.

### 3. Classification
**PHONONIC** — the substrate's CGWB-α_s correlation is a substrate-prediction layer, not an LCDM null. The 9-cell matrix maps how the substrate's ρ behaves under three independent semantic readings × three definitional scopes; LAYER-3 (substrate-marginalized-observable) is the substrate-prediction reading whose value is computed in P7.

### 4. Agent type
**`mack-cosmic-bridge`** (this planner; allowed at compute time per `.claude/rules/teammate-behavior.md` "one writer per output" — the **planner role here is distinct from the runner role at compute time**). Blacklist: do NOT dispatch `gen-physicist` as runner (per partition §5.4 specialist-vs-breadth-coordinator rule). Backup: `cosmic-web-theorist` if `mack-cosmic-bridge` stalls on R3 sub-iteration.

### 5. Hypothesis
The W13-2 ρ=0 verdict and the 6A spot-check |ρ|≈0.91 are **not contradictory** — they measure the substrate's CGWB-α_s correlation at three semantically-distinct layers (parameter / experimental-Fisher / substrate-marginalized-observable) under three independent arms (signed vs magnitude / canonical vs marginalized / pure-W12-4 vs LISA-fold-folded), and the 9-cell matrix renders each reading explicit so future joint-channel ρ verdicts cannot conflate them.

### 6. Method — COMPLETE dispatch prompt

```
TASK: Compose the 9-cell diagrammatic commit table for S86 W8-1 (P6) and write
      the verdict line + working-paper §VI.A registry-commit block.

You are mack-cosmic-bridge. Read these files (and ONLY these):
  - sessions/session-plan/session-86-plan-w8.md (this plan, §W8-1)
  - sessions/archive/session-85/session-85-w13-workingpaper.md §6A subsection
    (W13-2 INFO verdict-line context only — do NOT re-derive)
  - sessions/permanent-results-registry.md (verify R7 + R8 entries from
    W0b are landed; if absent, emit a CHAIN warning and proceed with
    provisional registry slot)

Computation script: computations/s86_w8_p6_cgwb_diagrammatic_commit.py

Imports:
  from canonical_constants import *  # MANDATORY per .claude/rules/math-scripts.md
  import os; os.environ.setdefault('OMP_NUM_THREADS', '8')  # CPU-only is fine
                                                            # for registry-write
                                                            # gate (no heavy
                                                            # linear algebra)

This gate is REGISTRY-WRITE class (audit). The "computation" is the
construction of the 9-cell matrix as a structured Python dict, the
6-axis pin-table as a list-of-tuples, and the SHA closure-hash over
the canonical input pins.

The 3 ARMS (one per row) are:
  Arm-1: signed-vs-magnitude. Whether ρ is computed as Pearson(signed)
         or as Pearson(|·|).
  Arm-2: canonical-vs-marginalized α_s. Whether α_s carries the W12-4
         canonical-regulator pin (zeta primary) or is marginalized over
         the 5-regulator atlas via the LAYER-3 weighting choice.
  Arm-3: pure-W12-4 vs LISA-fold-folded. Whether Ω_GW(f_LISA) is taken
         at the canonical 3 mHz pivot or convolved with the LISA PLS
         frequency-response window.

The 3 LAYERS (one per column) are:
  Layer-1: PARAMETER LAYER. ρ between the substrate parameters
           (α_s_substrate, Ω_GW_substrate) BEFORE any experimental
           response function is applied. Substrate-internal correlation.
  Layer-2: EXPERIMENTAL-FISHER LAYER. ρ propagated through the
           experimental Fisher matrix
           F = diag(1/σ(α_s_CMBS4)², 1/σ(Ω_GW_LISA)²)
           — this is the W13-2 reading; ρ=0 because the Fisher matrix
           is diagonal (uncorrelated experimental noise) and α_s and
           Ω_GW(LISA) at the substrate level were the same number to
           experimental precision.
  Layer-3: SUBSTRATE-MARGINALIZED-OBSERVABLE LAYER. ρ between
           (α_s, Ω_GW(f_LISA)) where each observable is realized
           across the W12-4 5-regulator atlas {ζ, Zubarev, SDW,
           cutoff_sqrt, anomaly}; Pearson |ρ| over the 5-point
           ensemble. This is where mack 9A §VI.2 spot-checked
           |ρ| ≈ 0.91 (R3).

The 9 CELLS are the 3×3 outer product. For each cell, document:
  (cell_id = "Arm{i}-Layer{j}",
   ρ_sign_convention = signed | magnitude,
   ρ_α_s_pin = canonical | marginalized,
   ρ_Ω_GW_pin = pure-W12-4 | LISA-fold-folded,
   ρ_method = "Pearson(signed)" | "Pearson(|·|)",
   ρ_value_status = "anchored-at-W13-2" | "computed-in-P7" | "deferred-to-S87" | "structural-zero" )

The 6 PRE-REGISTERED PIN AXES (orthogonal to the 9-cell decomposition;
these are the *machinery* axes that future joint-channel ρ gates must
explicitly pin):
  Axis-1: scheme {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}
  Axis-2: convention (LISA-PLS version + CMB-S4 forecast version + atlas
                      weighting + linear-vs-log-derivative-J + signed-vs-mag)
  Axis-3: L_max ∈ {8, 10, 12} (truncation level)
  Axis-4: layer ∈ {parameter, experimental-Fisher, substrate-marginalized}
  Axis-5: arm ∈ {signed-vs-magnitude, canonical-vs-marginalized,
                  pure-vs-LISA-fold-folded}
  Axis-6: f_pivot ∈ {f_LISA = 3 mHz canonical, f_band ∈ [0.5, 2] f_LISA
                     for sensitivity bands}

Output:
  - computations/_artifacts/s86_w8_p6_diagrammatic_matrix.npz
    with arrays: cells (9-element record array), axes (6-element
    record array), input_pin_map (ordered list)
  - computations/_artifacts/s86_w8_p6_diagrammatic_matrix.json
    (human-readable mirror)
  - sessions/archive/session-86/session-86-w8-workingpaper.md §VI.A
    (substantive 9-cell + 6-axis table; this section will be ≥40 lines
    of structured table content; exact length is content-driven, not
    line-target-driven per `feedback_max-effort-full-fidelity.md`)
  - computations/s86_gate_verdicts.txt: append the canonical
    verdict line + dual-SHA companion row per W9a-99 template.

Verdict line format (per .claude/rules/gate-verdicts.md S81+):
  S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT: PASS|FAIL|INFO
    -- value=(n_cells=<n>, n_axes=<m>, ρ_anchored_count=<a>,
              ρ_computed_count=<c>) scheme=registry-9cell
    convention=W13-2-anchor+P7-LAYER-3+W0b-R8-methodology
    L_max=10 sha256=<closure>

  audit_sha256: <ordered-input-pin closure SHA>  (companion comment row)

DO NOT compute new ρ values in this gate — those come from W13-2
(LAYER-2 anchor) and from P7 (LAYER-3 MC). The audit verdict is
strictly methodological completeness.

GPU note: torch.linalg unnecessary for this registry-write gate;
no matrices ≥100×100 are constructed. CPU-only with OMP cap is
sufficient.
```

### 7. Machinery pin (PRDR)
```yaml
schema_version: R3
gate_id: S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT
trigger: AUDIT
classification: PHONONIC
machinery_pin_map:
  L_max: 10                                  # canonical W13-2 truncation
  scheme: registry-9cell                     # registry-write taxonomy
  convention: W13-2-anchor+P7-LAYER-3+W0b-R8-methodology
  tolerance: structural (all 9 cells present + 6 axes pinned)
  random_seed: not_applicable                # registry-write, no MC
  GPU_path: not_applicable                   # CPU-only OMP=8
  cutoff_axis: spectral                      # per W0a R3 cutoff_axis YAML pin
  n_arms: 3
  n_layers: 3
  n_axes: 6
  ρ_anchor_source: S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT
  ρ_compute_source: S86-RHO-SUBSTRATE-PREDICTION-MC (P7, sister gate this wave)
input_sha_pins:
  - sessions/archive/session-85/session-85-w13-workingpaper.md  # 6A subsection
  - sessions/permanent-results-registry.md              # R7 + R8 methodology entries
  - computations/s85_gate_verdicts.txt             # W13-2 verdict line
  - computations/canonical_constants.py            # constant-import provenance
```

### 8. Expected output 4-tuple
```
(value=(n_cells=9, n_axes=6, ρ_anchored_count=1, ρ_computed_count=1),
 scheme=registry-9cell,
 convention=W13-2-anchor+P7-LAYER-3+W0b-R8-methodology,
 L_max=10)
```
Where `ρ_anchored_count=1` is the W13-2 LAYER-2 anchor and `ρ_computed_count=1` is the P7 LAYER-3 result (the other 7 cells are either structural-zero or deferred-to-S87 per the 9-cell taxonomy).

### 9. PASS / FAIL / INFO thresholds
- **PASS**: 9-cell matrix complete (all 9 cells documented with their 4-field signature) AND 6 pin axes documented (Axis-1 through Axis-6 each with scope + admissible-values list) AND `_artifacts/s86_w8_p6_diagrammatic_matrix.npz` written AND working-paper §VI.A populated with table.
- **FAIL**: any cell or axis absent. (Tolerance rule: STRUCTURAL-COMPLETENESS, RATIO not applicable; either every cell is present or the gate FAILs.)
- **INFO**: not applicable (registry-write gate has binary completeness; no INFO band).

### 10. Substitution chain
Not required for P6 — this is an audit-class gate with no sign/direction/threshold claim about a physical observable. The registry-completeness threshold is integer-valued (n_cells = 9, n_axes = 6) with no continuous quantity.

### 11. What PASSES / FAILS MEAN for solution space
- **PASS** closes the 6A diagrammatic commit (context §1.3 surviving open channel #6A); W13-2 INFO verdict is RE-CONTEXTUALIZED (not retracted) as the LAYER-2 anchor of a 3-layer methodology; the 6-axis pin table becomes the canonical machinery-pin template for ALL future joint-channel ρ verdicts (per W0b R8 generalization clause); the substrate-prediction LAYER-3 reading gets a registry slot that P7 fills with its computed value.
- **FAIL** leaves 6A open into S87+ and signals that the planner under-specified the 9-cell taxonomy. P7 + C7 still execute (they are not blocked by P6 FAIL since they compute physics); P6 retries with a refined cell taxonomy.

### 12. Effort estimate
0.5 wave ≈ 2-3h compute (registry-write gate; no heavy numerics; bulk of effort is 9-cell + 6-axis content + working-paper §VI.A drafting).

### 13. Substrate-framing reminder
The 9-cell matrix is **the substrate's CGWB-α_s correlation under regulator y at semantic layer z**. It is NOT an LCDM null-hypothesis test, NOT a frequentist correlation coefficient with a p-value interpretation, and NOT an experimental-noise-correlation diagnostic (Layer-2's Fisher reading touches that, but Layer-1 and Layer-3 are substrate-prediction layers). Every cell in the matrix should be read as: "the substrate's prediction for ρ(α_s, Ω_GW) is X under the (arm, layer) signature."

---

## §W8-2. S86-RHO-SUBSTRATE-PREDICTION-MC (P7)

### 1. Gate ID
`S86-RHO-SUBSTRATE-PREDICTION-MC`

### 2. Trigger
**[VERIFY] + [SIGN]** — VERIFY because it computes a ρ value to be compared against the 0.91 R3 spot-check (RATIO ≤ 1e-1 tolerance); SIGN because the sign-convention (signed Pearson vs magnitude Pearson) is one of the two pre-pinned freedoms whose direction outcome must be substantiated by a substitution chain.

### 3. Classification
**PHONONIC** — substrate-prediction layer (LAYER-3 of the P6 9-cell matrix). The Monte Carlo samples over the W12-4 5-regulator atlas, which IS the substrate's regulator-class structural floor (context §1.5: F_4 = {ζ, Zubarev, SDW} + M = {cutoff_sqrt, anomaly}); each regulator realizes a different (α_s, Ω_GW) pair and the Pearson |ρ| over the 5-point ensemble measures the substrate's predictive coherence across regulator schemes.

### 4. Agent type
**`mack-cosmic-bridge`** (this planner; runner role distinct). Blacklist: do NOT dispatch `gen-physicist` (per partition §5.4). Backup: `feynman-theorist` if the MC sampling stalls (Feynman owns the bootstrap-and-resampling literature in the project's reviewer roster).

### 5. Hypothesis
The substrate's LAYER-3 ρ_substrate-prediction over the W12-4 5-regulator atlas is **non-zero** under at least one combination of (sign-convention, atlas-weighting), with reference value Pearson |ρ| ≈ 0.91 (mack 9A §VI.2, R3 spot-check); the LAYER-3 MC anchors this value with explicit 4-tuple machinery pinning so the 6A workshop's spot-check becomes a registry-grade computation.

### 6. Method — COMPLETE dispatch prompt

```
TASK: Compute the LAYER-3 ρ_substrate-prediction Monte Carlo for S86 W8-2 (P7).

You are mack-cosmic-bridge. Read these files (and ONLY these):
  - sessions/session-plan/session-86-plan-w8.md (this plan, §W8-2)
  - computations/s85_w12_w0_regulator_taxonomy.py (W12-4 atlas
    construction; do NOT modify; load its output to inherit the
    5-regulator (a_0, a_2, a_4) tuples)
  - computations/s85_w13_2_cgwb_alpha_s_joint.py (W13-2 single-arm
    ρ infrastructure; reuse omega_gw_loglog_interp + the canonical
    α_s extraction; do NOT modify)
  - computations/canonical_constants.py (import M_KK, tau_fold,
    etc.; never hardcode)

Computation script: computations/s86_w8_p7_rho_substrate_mc.py

Imports:
  from canonical_constants import *
  import os; os.environ.setdefault('OMP_NUM_THREADS', '8')
  # GPU path: prefer torch.linalg + cupy random for matrices ≥100×100;
  # at N_samples = 10000 × 5 regulators = 50000-vector operations,
  # GPU is justified per .claude/rules/math-scripts.md.
  # Use:
  #   import torch
  #   device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  #   rng = torch.Generator(device=device).manual_seed(RANDOM_SEED)

Constants used (all imported from canonical_constants.py):
  M_KK, tau_fold, c_Gold, planck_ns
  Acoustic-channel pins from S69 / S85: f_LISA_pivot = 3.0e-3 Hz
  (lift to canonical_constants if absent; tag # (local) in script
   only if it is a one-off scan parameter, NOT a framework constant —
   here it IS a framework pin, so promote to canonical_constants.)

Method (4 steps; this is a [SIGN] gate, so substitution chain is mandatory
for the direction claim — see §10 of this plan-block):

  Step 1: Load the W12-4 5-regulator atlas (a_0^k, a_2^k, a_4^k)
          for k ∈ {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} from the
          inherited computation cache. Verify SHA pin against
          computations/s85_w12_w0_regulator_taxonomy outputs.

  Step 2: For each regulator k, compute the substrate observables
          (α_s^k, Ω_GW^k(f_LISA = 3 mHz)) using the W13-2 forward
          map from (a_n^k) to (α_s, Ω_GW). The forward map already
          exists in s85_w13_2_cgwb_alpha_s_joint.py — call it as a
          library function with regulator-pin substitution.

  Step 3: Monte-Carlo sample. Within each regulator k, draw N_samples
          = 10000 perturbations of (a_n^k) within their pre-registered
          uncertainty band (use the W12-4 5-class taxonomy uncertainty
          envelope; if absent, default to ±5% Gaussian and tag as
          PRDR Class 8.1 PINNED-BUT-DRIFT for follow-up).
          For each (regulator, sample) pair, propagate through
          forward map → (α_s, Ω_GW) realization.
          Total ensemble: 50000 (regulator, sample) points.

  Step 4: Compute Pearson ρ over the ensemble in 6 modes (the
          2×3 = 6 outer product of the two pre-pinned freedoms):
          - sign_convention ∈ {signed, magnitude}
          - atlas_weighting ∈ {uniform, PV-down-weighted, PV-excluded}
          where:
            uniform:           w_k = 1/5 ∀ k
            PV-down-weighted:  w_k ∈ {0.20, 0.20, 0.20, 0.10, 0.30}
                               with cutoff_sqrt down-weighted to 0.10
                               and anomaly up-weighted to 0.30 (PV-class
                               weighting per S-1 lift)
            PV-excluded:       w_k = 1/3 for k ∈ F_4 = {ζ, Zubarev,
                               SDW}, w_k = 0 for k ∈ M = {cutoff_sqrt,
                               anomaly}; this isolates the F_4 pure-a_4
                               family (context §1.5).
          The reference Pearson |ρ| ≈ 0.91 (R3 spot-check) was
          computed under (signed, uniform) per mack 9A §VI.2.

PRE-REGISTRATION PINS (these are the SIGN axes and must be enumerated
                       in the verdict line, NOT chosen post-hoc):
  sign_convention = ALL_SIX_COMBINATIONS_REPORTED (signed AND magnitude)
  atlas_weighting = ALL_THREE_COMBINATIONS_REPORTED (uniform, PV-dn,
                                                     PV-excluded)
  N_samples = 10000
  RANDOM_SEED = 0xCGWB_P7  # i.e. 0xCFAB1771 (substrate-tag, fixed
                            # at plan-freeze; do NOT change post-hoc
                            # per .claude/rules/v3-closure-recovery.md
                            # PROHIBITED_ACTIONS #2)
  forward_map_version = W13-2 canonical
  uncertainty_envelope = W12-4 5-class default (else ±5% Gaussian +
                          PINNED-BUT-DRIFT tag)

Output:
  - computations/_artifacts/s86_w8_p7_rho_mc_ensemble.npz
    with arrays:
      ensemble_alpha_s: shape (5, 10000)
      ensemble_omega_gw: shape (5, 10000)
      rho_grid: shape (2, 3) for (sign_convention, atlas_weighting)
      regulator_labels: ['zeta', 'Zubarev', 'SDW', 'cutoff_sqrt',
                         'anomaly']
  - computations/_artifacts/s86_w8_p7_rho_mc_grid.png
    (heatmap of Pearson |ρ| over 6 cells; X = atlas_weighting,
     Y = sign_convention; cell color = |ρ|; annotated with reference
     |ρ| ≈ 0.91 from R3 spot-check)
  - sessions/archive/session-86/session-86-w8-workingpaper.md §VI.B
    (3-paragraph + 1 table report: ρ_grid table, comparison to
     reference 0.91, substitution-chain documentation per §10
     of this plan-block, structural interpretation per §11)
  - computations/s86_gate_verdicts.txt: canonical verdict
    line + dual-SHA companion row.

Verdict line format:
  S86-RHO-SUBSTRATE-PREDICTION-MC: PASS|FAIL|INFO
    -- value=(rho_signed_uniform=<v1>, rho_signed_PV-dn=<v2>,
              rho_signed_PV-excl=<v3>, rho_mag_uniform=<v4>,
              rho_mag_PV-dn=<v5>, rho_mag_PV-excl=<v6>)
    scheme=substrate-marginalized-observable
    convention=W12-4-5-regulator-atlas+W13-2-forward-map+pre-pinned-6cell
    L_max=10 sha256=<closure>

  audit_sha256: <ordered-input-pin closure SHA>

GPU note: 50000-point Pearson + heatmap is well within CPU range,
but if extending to N_samples ≥ 1e5, switch to torch.linalg.std
+ torch.dot for the covariance computation on GPU (AMD RX 9070 XT
ROCm path per .claude/rules/computation-environment.md).
```

### 7. Machinery pin (PRDR)
```yaml
schema_version: R3
gate_id: S86-RHO-SUBSTRATE-PREDICTION-MC
trigger: VERIFY+SIGN
classification: PHONONIC
machinery_pin_map:
  L_max: 10
  scheme: substrate-marginalized-observable
  convention: W12-4-5-regulator-atlas+W13-2-forward-map+pre-pinned-6cell
  tolerance: RATIO ≤ 1e-1 vs reference |ρ| = 0.91 (R3 spot-check)
  random_seed: 0xCFAB1771               # 0xCGWB_P7 substrate-tag
  GPU_path: torch.linalg + cupy random (CPU fallback OMP=8)
  cutoff_axis: spectral
  N_samples: 10000
  N_regulators: 5
  ensemble_size: 50000
  sign_convention: ALL_SIX_COMBINATIONS_REPORTED
  atlas_weighting: ALL_THREE_COMBINATIONS_REPORTED
  forward_map_version: W13-2 canonical
  uncertainty_envelope: W12-4 5-class default (±5% Gaussian fallback
                                                 with PINNED-BUT-DRIFT
                                                 PRU-Class-8.1 tag)
  reference_rho_mag: 0.91                # R3 spot-check, mack 9A §VI.2
  f_pivot_Hz: 3.0e-3                     # f_LISA canonical
input_sha_pins:
  - computations/s85_w12_w0_regulator_taxonomy.py            # forward atlas
  - computations/_artifacts/s85_w12_w0_regulator_taxonomy.npz # output cache
  - computations/s85_w13_2_cgwb_alpha_s_joint.py             # forward map
  - computations/canonical_constants.py
  - sessions/archive/session-85/session-85-w13-workingpaper.md             # 6A subsection
  - sessions/permanent-results-registry.md                          # R7+R8 methodology
```

### 8. Expected output 4-tuple
```
(value=(rho_signed_uniform=<v1>, rho_signed_PV-dn=<v2>,
        rho_signed_PV-excl=<v3>, rho_mag_uniform=<v4>,
        rho_mag_PV-dn=<v5>, rho_mag_PV-excl=<v6>),
 scheme=substrate-marginalized-observable,
 convention=W12-4-5-regulator-atlas+W13-2-forward-map+pre-pinned-6cell,
 L_max=10)
```

### 9. PASS / FAIL / INFO thresholds
- **PASS**: |ρ_substrate-prediction| ∈ [0.819, 1.001] (RATIO ≤ 1e-1 of reference 0.91, capped at 1.0 by Cauchy-Schwarz) under at least one (sign_convention, atlas_weighting) combination of the 6, AND MC ensemble reproduces a stable Pearson statistic (bootstrap σ_ρ ≤ 0.05).
- **INFO**: |ρ| outside the [0.819, 1.001] band BUT consistent across ≥4 of 6 cells (sign of |ρ| same direction for ≥4/6) and bootstrap σ_ρ ≤ 0.05.
- **FAIL**: MC unstable (bootstrap σ_ρ > 0.05) OR |ρ| varies wildly across the 6 cells (max-min spread > 0.5) OR the script crashes before producing the 6-cell ρ_grid.

Tolerance rule: RATIO (≤ 1e-1) for PASS band; ABSOLUTE (σ_ρ thresholds 0.05) for stability checks.

### 10. Substitution chain — MANDATORY for [SIGN]

**Claim to verify**: "Magnitude Pearson |ρ| over the 5-regulator atlas measures the substrate's predictive coherence under regulator marginalization, with positive correlation when the regulators agree on the sign of (α_s − ⟨α_s⟩) and (Ω_GW − ⟨Ω_GW⟩)."

```
Step 1 (definitions):
  α_s^k          = substrate prediction for spectral running under regulator k
                   (k ∈ {ζ, Zubarev, SDW, cutoff_sqrt, anomaly})
  Ω_GW^k(f_LISA) = substrate prediction for stochastic GW background
                   amplitude at f = 3 mHz under regulator k
  ⟨X⟩           = ensemble mean over (regulator, sample) pairs:
                   ⟨X⟩ = (1/Σ_k w_k N_k) · Σ_k Σ_i w_k X_i^k
  σ_X            = ensemble standard deviation:
                   σ_X² = ⟨(X − ⟨X⟩)²⟩
  Cov(α_s, Ω_GW) = ensemble covariance:
                   Cov = ⟨(α_s − ⟨α_s⟩)·(Ω_GW − ⟨Ω_GW⟩)⟩
  ρ_signed       = Cov(α_s, Ω_GW) / (σ_α · σ_Ω)        [signed Pearson]
  ρ_magnitude    = |Cov(|α_s|, |Ω_GW|)| / (σ_|α| · σ_|Ω|)
                                                       [magnitude Pearson;
                                                        compares deviations
                                                        from MEAN of MAGNITUDES]

Step 2 (substitute the W12-4 atlas):
  Across k ∈ {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}, the W12-4
  taxonomy puts each k into class (a)/(b)/(c)/(d). Per W12-4 PASS
  (n_a=13, n_b=0, n_c=0, n_d=3), the substrate observables fall into
  INVARIANT (13 entries) + STRUCTURALLY-DIVERGENT (3 entries) classes.
  α_s and Ω_GW(f_LISA) belong to the INVARIANT class for k ∈ F_4 =
  {ζ, Zubarev, SDW}, and may diverge for k ∈ M = {cutoff_sqrt, anomaly}.

Step 3 (simplify):
  Under (signed, uniform):
    ρ_signed_uniform = Cov(α_s, Ω_GW)_uniform / (σ_α · σ_Ω)_uniform
  Under (signed, PV-excluded):
    ρ_signed_PV-excl restricts the sum to k ∈ F_4; the M family
    contribution vanishes by w_k = 0.
  Under (magnitude, *):
    The Pearson is taken over (|α_s|, |Ω_GW|), so sign-flips in the
    underlying observables cancel BEFORE the covariance computation.

Step 4 (direction read-off):
  If the 5 regulators' (α_s^k, Ω_GW^k) realizations are co-monotone
  (when α_s rises, Ω_GW rises with it), Cov > 0 and ρ_signed > 0.
  If they are anti-co-monotone, Cov < 0 and ρ_signed < 0.
  Magnitude Pearson cannot be negative (by construction);
  ρ_magnitude ≥ 0, with ρ_magnitude → 1 when the 5-point ensemble
  collapses to a 1D line in (|α_s|, |Ω_GW|) space.
  The 0.91 spot-check (mack 9A §VI.2) was computed under (signed,
  uniform) and reflects strong co-monotonicity across the 5 regulators
  → the substrate's α_s and Ω_GW(f_LISA) predictions are tightly
  correlated when scanned across regulator class.

Conclusion: the (signed, uniform) cell is the canonical reference.
Other cells (magnitude, PV-dn, PV-excluded) probe the robustness
of this co-monotonicity to definitional choices. PASS = |ρ| ∈
[0.819, 1.001] under ≥1 cell; the cells that report |ρ| ≈ 0.91
under canonical pins constitute the LAYER-3 substrate-prediction.
```

### 11. What PASSES / FAILS MEAN for solution space
- **PASS** (|ρ_substrate-prediction| ∈ [0.819, 1.001] under ≥1 cell): anchors LAYER-3 of the P6 9-cell matrix with a registry-grade ρ value; resolves the 6A apparent contradiction (W13-2 LAYER-2 ρ=0 vs spot-check |ρ|≈0.91) as a layer-disambiguation, not a numerical disagreement; opens a NEW substrate prediction — that joint-channel ρ at LAYER-3 is non-trivially structured by regulator class — for downstream LISA × CMB-S4 forecast work in W12 P11.
- **INFO** (|ρ| outside band but consistent across ≥4/6 cells): the 0.91 R3 spot-check was directionally correct but quantitatively subject to a definitional drift the spot-check did not pin; LAYER-3 anchor lands at the MC-converged value with a documentation row in W13 P11 noting the drift.
- **FAIL** (MC unstable OR |ρ| spread > 0.5 across 6 cells): the LAYER-3 reading is definitionally fragile and the 0.91 spot-check was a special-case artifact; the 6A workshop's three-layer methodology survives (W0b R8) but LAYER-3 cannot be anchored with a single number — the workingpaper records the 6-cell spread and the LAYER-3 reading is officially "scheme-dependent" per R7 single-name-conflation methodology.

### 12. Effort estimate
4-6h compute (MC sampling + 6-cell Pearson grid + heatmap + workingpaper §VI.B + verdict line + dual-SHA).

### 13. Substrate-framing reminder
The 50000-point ensemble is a sampling of the **substrate's regulator-class predictions** for (α_s, Ω_GW(f_LISA)). It is NOT a sampling over experimental noise (LAYER-2's territory) and NOT over a parameter prior (LAYER-1's territory). When the magnitude Pearson |ρ| → 0.91, the meaning is: the substrate's CGWB-α_s correlation under regulator y is X, and the value collapses onto a near-1D line because the 5 regulators agree on the substrate's directional response. State the result as: "the substrate's CGWB-α_s correlation under W12-4 5-regulator marginalization is |ρ| = <v>", NOT "α_s and Ω_GW are correlated in the data."

---

## §W8-3. S86-CGWB-LMAX-DIRECT (C7)

### 1. Gate ID
`S86-CGWB-LMAX-DIRECT`

### 2. Trigger
**[VERIFY]** — numerical L_max sensitivity check; the threshold (5% / 20%) is a quantitative magnitude claim about |Ω_GW(L=8) − Ω_GW(L=10)| / Ω_GW(L=10), which makes substitution-chain documentation mandatory per §10 of this plan-block.

### 3. Classification
**GEOMETRIC** — truncation-sensitivity is a spectral-geometry diagnostic of the D_K cache (the eigenvalue truncation level L_max controls how many of the 155,984 eigenvalues at L_max=10 enter the spectral action). The Ω_GW(f_LISA) value's response to L_max ∈ {8, 10} probes whether the W13-2 INFO band-width verdict was reflecting genuine truncation drift or merely the spectral-slope artifact mack 9A §VI.1 identified.

### 4. Agent type
**`mack-cosmic-bridge`** (this planner; runner role distinct). Blacklist: do NOT dispatch `gen-physicist` (per partition §5.4). Backup: `little-red-dots-jwst-analyst` (the JWST analyst owns the spectral-truncation diagnostic in the project's reviewer roster — the L_max convergence test is the same numerical pattern as the JWST emission-line truncation diagnostic).

### 5. Hypothesis
The S85 W13-2 §(f) band-width-diagnostic that returned >20% (driving the INFO verdict) was measuring the **spectral slope** of Ω_GW(f) in the [0.5 f_LISA, 2 f_LISA] band, NOT the truncation-sensitivity of Ω_GW at f_LISA itself; under a direct L=8 vs L=10 spectrum comparison at f = 3 mHz, |ΔΩ_GW|/Ω_GW(L=10) is small (target ≤ 5%) and the W13-2 INFO band can be RECONTEXTUALIZED as an artifact of the band-width proxy, not a genuine truncation defect.

### 6. Method — COMPLETE dispatch prompt

```
TASK: Direct L=8 vs L=10 spectrum comparison for Ω_GW(f_LISA = 3 mHz).

You are mack-cosmic-bridge. Read these files (and ONLY these):
  - sessions/session-plan/session-86-plan-w8.md (this plan, §W8-3)
  - computations/s85_w13_2_cgwb_alpha_s_joint.py (W13-2 source;
    inherit omega_gw_loglog_interp + the L_max=10 spectrum cache;
    do NOT modify)
  - sessions/archive/session-85/session-85-w13-workingpaper.md §6A §(f)
    (band-width-diagnostic context only)
  - computations/canonical_constants.py

Computation script: computations/s86_w8_c7_lmax_direct.py

Imports:
  from canonical_constants import *
  import os; os.environ.setdefault('OMP_NUM_THREADS', '8')
  # GPU note: spectrum-load + interpolation at 2 L_max values is light;
  # CPU is sufficient unless extending to L=12 (then torch.linalg
  # eigendecomposition recommended for matrices ≥ ~155984 entries
  # per .claude/rules/computation-environment.md).

Method (4 steps; this is a [VERIFY] gate with magnitude claim,
substitution chain mandatory per §10):

  Step 1: Load Ω_GW(f) spectrum at L_max = 10 from W13-2's cache.
          Verify SHA pin against computations/_artifacts/
          s85_w13_2_omega_gw_spectrum_L10.npz (if absent, regenerate
          from s85_w13_2_cgwb_alpha_s_joint.py invocation under
          L_max=10).

  Step 2: Compute (or load) Ω_GW(f) spectrum at L_max = 8 using the
          identical forward pipeline as W13-2 with L_max=8 substituted.
          Cache to computations/_artifacts/
          s86_w8_c7_omega_gw_spectrum_L8.npz.

  Step 3: Evaluate Ω_GW(f_LISA = 3 mHz) at each L_max via
          omega_gw_loglog_interp at exactly f = 3.0e-3 Hz.
          Record:
            Omega_L8  = omega_gw_loglog_interp(3e-3, spectrum_L8)
            Omega_L10 = omega_gw_loglog_interp(3e-3, spectrum_L10)

  Step 4: Compute relative L_max-sensitivity:
            delta_rel = |Omega_L8 - Omega_L10| / Omega_L10

CONTRAST WITH W13-2 §(f): the prior diagnostic computed
  Omega_band_min = omega_gw_loglog_interp(0.5 * f_LISA, spectrum)
  Omega_band_max = omega_gw_loglog_interp(2.0 * f_LISA, spectrum)
  band_width = |Omega_band_max - Omega_band_min| / Omega_at_f_LISA
which captured the spectral slope (frequency-derivative of the same
spectrum), not the truncation drift between two different spectra.
The C7 gate replaces band_width with delta_rel as the truncation
diagnostic.

Output:
  - computations/_artifacts/s86_w8_c7_omega_gw_spectrum_L8.npz
    (regenerated L=8 spectrum)
  - computations/_artifacts/s86_w8_c7_lmax_compare.json
    {"Omega_L8": <v>, "Omega_L10": <v>, "delta_rel": <v>,
     "f_LISA_Hz": 3.0e-3, "spectrum_L10_sha": "...",
     "spectrum_L8_sha": "..."}
  - computations/_artifacts/s86_w8_c7_lmax_compare.png
    (overlay log-log plot of Omega_L8(f), Omega_L10(f) over the
     [1e-4, 1e-1] Hz range with vertical line at f_LISA = 3 mHz
     and annotation of delta_rel)
  - sessions/archive/session-86/session-86-w8-workingpaper.md §VI.C
    (1-paragraph + 1-table report: delta_rel value, comparison to
     PASS/INFO/FAIL bands, contrast to W13-2 band_width proxy)
  - computations/s86_gate_verdicts.txt: canonical verdict line
    + dual-SHA companion row.

Verdict line format:
  S86-CGWB-LMAX-DIRECT: PASS|FAIL|INFO
    -- value=(Omega_L8=<v>, Omega_L10=<v>, delta_rel=<v>)
    scheme=L_max-direct-truncation-comparison
    convention=W13-2-forward-map+f_LISA-pivot+log-log-interp
    L_max=8-vs-10 sha256=<closure>

  audit_sha256: <ordered-input-pin closure SHA>

GPU note: 2 spectrum loads + interpolation is CPU-bounded.
Promote to torch.linalg only if extending to L=12 spectrum
generation in a follow-up gate.
```

### 7. Machinery pin (PRDR)
```yaml
schema_version: R3
gate_id: S86-CGWB-LMAX-DIRECT
trigger: VERIFY
classification: GEOMETRIC
machinery_pin_map:
  L_max_pair: [8, 10]                    # explicit pair, not single value
  scheme: L_max-direct-truncation-comparison
  convention: W13-2-forward-map+f_LISA-pivot+log-log-interp
  tolerance: RATIO ≤ 5e-2 (PASS) / 5e-2 < δ ≤ 2e-1 (INFO) / > 2e-1 (FAIL)
  random_seed: not_applicable            # deterministic spectrum load
  GPU_path: CPU OMP=8 sufficient (torch.linalg if extended to L=12)
  cutoff_axis: spectral
  f_pivot_Hz: 3.0e-3                     # f_LISA canonical
  forward_map_version: W13-2 canonical
  spectrum_cache_L10: computations/_artifacts/s85_w13_2_omega_gw_spectrum_L10.npz
  spectrum_cache_L8:  computations/_artifacts/s86_w8_c7_omega_gw_spectrum_L8.npz
                     (this gate generates if absent)
input_sha_pins:
  - computations/s85_w13_2_cgwb_alpha_s_joint.py
  - computations/_artifacts/s85_w13_2_omega_gw_spectrum_L10.npz
  - computations/canonical_constants.py
  - sessions/archive/session-85/session-85-w13-workingpaper.md
```

### 8. Expected output 4-tuple
```
(value=(Omega_L8=<v>, Omega_L10=<v>, delta_rel=<v>),
 scheme=L_max-direct-truncation-comparison,
 convention=W13-2-forward-map+f_LISA-pivot+log-log-interp,
 L_max=8-vs-10)
```

### 9. PASS / FAIL / INFO thresholds
- **PASS**: `delta_rel = |Omega_L8 - Omega_L10| / Omega_L10 ≤ 0.05` (5%) — truncation-stable at L_max=10; W13-2 INFO band-width verdict is RECONTEXTUALIZED as a spectral-slope artifact, not a truncation defect.
- **INFO**: `0.05 < delta_rel ≤ 0.20` (5%-20%) — modest truncation drift; the W13-2 INFO verdict is partially confirmed (truncation IS a contributor) but the spectral-slope component dominates; both effects coexist.
- **FAIL**: `delta_rel > 0.20` (>20%) — substantial truncation drift; the L_max=10 spectrum is not converged; downstream LISA forecasts based on Ω_GW(L=10) carry > 20% truncation error and need L=12 (or higher) spectra; W13-2 INFO verdict is upgraded to FAIL-equivalent for the truncation channel.

Tolerance rule: RATIO (5%, 20%).

### 10. Substitution chain — MANDATORY for [VERIFY] magnitude

**Claim to verify**: "Direct L=8 vs L=10 spectrum comparison at f_LISA measures truncation-sensitivity; band-width over [0.5 f_LISA, 2 f_LISA] at fixed L_max measures spectral-slope; these are different physical quantities."

```
Step 1 (definitions):
  Omega_GW(f; L_max) = stochastic GW background amplitude at frequency f
                       computed from the D_K spectral action with
                       eigenvalue truncation at L_max (i.e., using
                       the first n(L_max) eigenvalues of D_K).
                       For L_max=10, n(10) = 155984 per S85 cache.
                       For L_max=8,  n(8)  < n(10) per substrate
                       eigenvalue counting (specific n(8) extracted
                       from cache regeneration).
  f_LISA              = 3.0e-3 Hz (LISA peak-sensitivity pivot)
  f_band_lo           = 0.5 · f_LISA = 1.5e-3 Hz
  f_band_hi           = 2.0 · f_LISA = 6.0e-3 Hz

Step 2 (substitute the two diagnostics):
  W13-2 band-width diagnostic (band_width):
    band_width(L_max=10) = |Omega_GW(f_band_hi; L=10)
                          - Omega_GW(f_band_lo; L=10)|
                         / Omega_GW(f_LISA; L=10)
  C7 truncation-sensitivity diagnostic (delta_rel):
    delta_rel = |Omega_GW(f_LISA; L=8) - Omega_GW(f_LISA; L=10)|
              / Omega_GW(f_LISA; L=10)

Step 3 (simplify — what each diagnostic measures):
  band_width holds L_max FIXED at 10 and varies f over [f_band_lo,
                                                       f_band_hi].
  → It measures the LOG-DERIVATIVE of Omega_GW with respect to log(f):
    band_width ≈ |d Omega_GW / d log(f)| · Δlog(f) / Omega_GW(f_LISA)
              = (n_t + 1) · ln(4) (approximately, for power-law spectrum
                                   with tilt n_t)
    → band_width measures SPECTRAL SLOPE.

  delta_rel holds f FIXED at f_LISA and varies L_max from 10 to 8.
  → It measures the L_max-DERIVATIVE of Omega_GW at fixed f:
    delta_rel = |d Omega_GW / d L_max|_{f=f_LISA} · ΔL_max
              / Omega_GW(f_LISA; L=10)
    → delta_rel measures TRUNCATION SENSITIVITY.

Step 4 (direction read-off):
  band_width and delta_rel are independent quantities. A spectrum can
  have steep slope (large band_width) AND be truncation-stable
  (small delta_rel) — this is the case we expect for the substrate's
  CGWB if L_max=10 is converged. Conversely, a flat spectrum with
  large truncation drift would show small band_width and large
  delta_rel.
  W13-2 reported band_width > 20% → INFO verdict, ATTRIBUTED to
  truncation. C7 tests whether this attribution was correct by
  measuring delta_rel directly. If delta_rel ≤ 5%, the W13-2
  attribution was a misdiagnosis; the > 20% band_width was spectral
  slope, not truncation defect.

Conclusion: PASS at delta_rel ≤ 5% reclassifies the W13-2 INFO
verdict from "truncation-uncertain" to "spectral-slope-detected
+ truncation-stable."
```

### 11. What PASSES / FAILS MEAN for solution space
- **PASS** (delta_rel ≤ 5%): the L_max=10 D_K cache is truncation-converged at f_LISA; the W13-2 INFO band-width-diagnostic is RECONTEXTUALIZED as a spectral-slope detection (n_t structure), not a truncation defect; downstream LISA × CMB-S4 forecasts using Ω_GW(L=10) at f_LISA can be cited at full precision; the W13-2 verdict line should be amended (W0b R9 dual-SHA regen) to specify "INFO band-width-DIAGNOSTIC was spectral-slope, NOT truncation; C7 confirms truncation-stable."
- **INFO** (5% < delta_rel ≤ 20%): both spectral-slope and truncation effects contribute; the W13-2 INFO verdict stands at partial strength; downstream forecasts carry an L_max=10 truncation systematic of size delta_rel that must be propagated to LISA × CMB-S4 joint Fisher.
- **FAIL** (delta_rel > 20%): the L_max=10 spectrum is not converged; W13-2 forecast precision was overstated; W13 P11 master-inventory entry for Ω_GW(LISA) carries an L_max-truncation flag and a follow-up gate at L=12 must be queued for S87.

### 12. Effort estimate
1-2h compute (spectrum load + interpolation + plot + verdict + workingpaper §VI.C).

### 13. Substrate-framing reminder
The L_max parameter is **the substrate's spectral truncation level** — how many eigenvalues of D_K enter the spectral action. delta_rel is **the substrate's CGWB-prediction's response to substrate-truncation refinement**, not an experimental-noise propagation. State the result as: "the substrate's Ω_GW prediction at f_LISA changes by delta_rel = X when the spectral truncation is refined from L=10 to L=8 (or extended back from L=8 to L=10)." NOT "the LISA detector resolves Ω_GW to within X."

---

## §X. Wave W8 → Downstream Decision Point

### Downstream consumers of W8 outputs

1. **W13 P11** (`S86-MASTER-INVENTORY-W6-W13-LAND`) — the falsifier-master-inventory gets a NEW row class for **LAYER-3 ρ_substrate-prediction** entries. P7 PASS feeds the canonical |ρ| ≈ 0.91 anchor; P6 PASS feeds the 9-cell + 6-axis machinery-pin schema that LAYER-3 entries must use. C7 PASS feeds the L_max-truncation column in the inventory.

2. **W13 W3** (watchlist Row #7 CGWB ρ_AC) — the Companion-null-(C-regulator) column with W13-2.Ω value 8.299e-58 is documented (per partition §1 W14 W3 entry); P7 PASS adds the LAYER-3 |ρ| value as a parallel column "ρ_substrate-prediction (W12-4 5-regulator atlas)."

3. **W12 C30** (`S86-DETECTOR-READINESS-9-CELL`) — the LISA cell of the 9-detector readiness checklist gets a row "LAYER-3 ρ-substrate-prediction sensitivity" populated from P7 + C7.

### Decision rules at S86 close

- If **P6 + P7 + C7 ALL PASS**: 6A workshop officially closed (context §1.3 surviving open channel #6A removed); LAYER-3 substrate-prediction enters the registry as a permanent reading; W13-2 verdict line gets a §VII-cross-reference annotation (no value change; methodology re-contextualization).
- If **P6 PASS, P7 INFO, C7 PASS**: 6A methodology closed; LAYER-3 anchor flagged as scheme-dependent; W13 P11 entry carries the 6-cell ρ_grid as a table rather than a single number.
- If **P6 PASS, P7 FAIL**: 6A methodology stands; LAYER-3 anchor cannot be summarized in a single ρ value; the registry slot remains open with a "scheme-fragile" flag pointing to the 6-cell P7 output.
- If **C7 FAIL** (delta_rel > 20%): independent of P6/P7 outcome, an L=12 follow-up gate is queued for S87 (this is a NEW carry-forward not pre-anticipated by the partition manifest; the planner notes it for partition author awareness).

### Substrate-framing of the downstream chain
W8's three deliverables together produce a **substrate-prediction layer hardening** for CGWB ⊥ α_s: P6 commits the methodology (3 layers, 6 axes), P7 anchors the substrate-prediction value (LAYER-3 |ρ|), C7 hardens the truncation-stability of the underlying spectrum. None of these are LCDM-comparison gates; all three are substrate-internal-consistency hardening. Downstream LISA observation in 2030+ tests the substrate's |ρ| and Ω_GW(f_LISA) predictions against measured noise; the framework's predictions are pinned NOW so the comparison is unambiguous when data lands.

---

## §0.10. Wave W8 Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every gate-relevant machinery parameter is enumerated below per gate, with PRDR (Pre-Registration Dry-Run) classification (PINNED / PINNED-BUT-DRIFT / DECLARED-DIAGNOSTIC).

### P6 machinery enumeration
| Parameter | Value | Class |
|:----------|:------|:------|
| `L_max` | 10 | PINNED |
| `scheme` | `registry-9cell` | PINNED |
| `convention` | `W13-2-anchor+P7-LAYER-3+W0b-R8-methodology` | PINNED |
| `n_arms` | 3 | PINNED |
| `n_layers` | 3 | PINNED |
| `n_axes` | 6 | PINNED |
| `cutoff_axis` | `spectral` | PINNED (per W0a R3 YAML) |
| `random_seed` | not-applicable (registry-write) | N/A |
| `GPU_path` | CPU OMP=8 | PINNED |
| `tolerance` | structural-completeness (binary) | PINNED |
| `ρ_anchor_source` | `S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT` | PINNED (citation) |
| `ρ_compute_source` | `S86-RHO-SUBSTRATE-PREDICTION-MC` (P7) | PINNED (sister-gate citation) |

### P7 machinery enumeration
| Parameter | Value | Class |
|:----------|:------|:------|
| `L_max` | 10 | PINNED |
| `scheme` | `substrate-marginalized-observable` | PINNED |
| `convention` | `W12-4-5-regulator-atlas+W13-2-forward-map+pre-pinned-6cell` | PINNED |
| `tolerance` | RATIO ≤ 1e-1 vs reference 0.91 | PINNED |
| `random_seed` | `0xCFAB1771` (0xCGWB_P7) | PINNED |
| `GPU_path` | torch.linalg + cupy random; CPU fallback OMP=8 | PINNED |
| `cutoff_axis` | `spectral` | PINNED (per W0a R3 YAML) |
| `N_samples` | 10000 | PINNED |
| `N_regulators` | 5 | PINNED |
| `ensemble_size` | 50000 | PINNED (= N_samples × N_regulators) |
| `sign_convention` | ALL_SIX_COMBINATIONS_REPORTED | PINNED |
| `atlas_weighting` | ALL_THREE_COMBINATIONS_REPORTED | PINNED |
| `forward_map_version` | W13-2 canonical | PINNED (citation) |
| `uncertainty_envelope` | W12-4 5-class default; ±5% Gaussian fallback | PINNED-BUT-DRIFT (Class 8.1; tagged for S86 W0b R2 follow-up) |
| `reference_rho_mag` | 0.91 (R3 spot-check) | PINNED (mack 9A §VI.2 citation) |
| `f_pivot_Hz` | 3.0e-3 | PINNED |

### C7 machinery enumeration
| Parameter | Value | Class |
|:----------|:------|:------|
| `L_max_pair` | [8, 10] | PINNED |
| `scheme` | `L_max-direct-truncation-comparison` | PINNED |
| `convention` | `W13-2-forward-map+f_LISA-pivot+log-log-interp` | PINNED |
| `tolerance` | RATIO ≤ 5e-2 (PASS) / 5e-2 < δ ≤ 2e-1 (INFO) / > 2e-1 (FAIL) | PINNED |
| `random_seed` | not-applicable (deterministic spectrum load) | N/A |
| `GPU_path` | CPU OMP=8 (promote to torch.linalg if extended to L=12) | PINNED |
| `cutoff_axis` | `spectral` | PINNED (per W0a R3 YAML) |
| `f_pivot_Hz` | 3.0e-3 | PINNED |
| `forward_map_version` | W13-2 canonical | PINNED (citation) |
| `spectrum_cache_L10` | `computations/_artifacts/s85_w13_2_omega_gw_spectrum_L10.npz` | PINNED (load) |
| `spectrum_cache_L8` | `computations/_artifacts/s86_w8_c7_omega_gw_spectrum_L8.npz` | PINNED (generate-if-absent) |

PRDR aggregate: 3 gates × full machinery-pin map, **0 PRU-Class-8 unpinned parameters**, 1 PINNED-BUT-DRIFT entry (P7 uncertainty_envelope, queued for W0b R2 follow-up). Per `.claude/rules/epistemic-discipline.md` §PRU detection, this wave passes the dry-run audit at plan-freeze.

---

## §0.11. Wave W8 Input-SHA Ledger

The following input files are SHA-pinned at plan-freeze (compute-time SHAs computed by each producing script via `hashlib.sha256` per `.claude/rules/gate-verdicts.md`). Static files have precomputed hashes; dynamic inputs are marked `<computed-at-runtime>` and resolved when the producing script runs.

| Path | Used by | SHA-256 status |
|:-----|:--------|:---------------|
| `computations/canonical_constants.py` | P6, P7, C7 | `<computed-at-runtime>` (re-pinned each S86 wave) |
| `computations/s85_gate_verdicts.txt` | P6 (W13-2 verdict-line citation) | `<computed-at-runtime>` |
| `computations/s85_w13_2_cgwb_alpha_s_joint.py` | P7, C7 (forward map + omega_gw_loglog_interp) | `<computed-at-runtime>` |
| `computations/_artifacts/s85_w13_2_omega_gw_spectrum_L10.npz` | C7 (L=10 spectrum cache) | `<computed-at-runtime>` (regenerate if absent from W13-2 invocation under L_max=10) |
| `computations/s85_w12_w0_regulator_taxonomy.py` | P7 (5-regulator atlas forward) | `<computed-at-runtime>` |
| `computations/_artifacts/s85_w12_w0_regulator_taxonomy.npz` | P7 (5-regulator atlas output cache) | `<computed-at-runtime>` (regenerate if absent) |
| `sessions/archive/session-85/session-85-w13-workingpaper.md` | P6, C7 (6A subsection context) | `<computed-at-runtime>` |
| `sessions/permanent-results-registry.md` | P6, P7 (R7 + R8 methodology entries from W0b) | `<computed-at-runtime>` (verify R7 + R8 entries present; CHAIN warning if absent) |

**Closure-hash construction** (per `.claude/templates/script-template.py` Section 4): each producing script orders its input pins lexicographically by path, concatenates `path:sha256_hex\n` for each, and emits `sha256_of_bytes(pin_str)` as the canonical closure hash that goes in the verdict line `sha256=<closure>` field. The audit_sha256 companion-row entry uses the same construction; any divergence between content_sha and audit_sha indicates a dual-SHA scheme defect (per W0b R10 dual-SHA-uniqueness audit).

**Cross-check against partition §3 sequencing**: P6 + P7 cite `sessions/permanent-results-registry.md` for the W0b R7 + R8 methodology entries; this is the W8 → W0b dependency. At compute time, if the registry entries are absent (W0b not yet completed), each gate emits a CHAIN warning to its verdict-line companion row but does not block — provisional registry slots are written and W0b's R7/R8 closures later promote them per `feedback_dispatch-discipline.md`.

---

**End of Wave W8 plan.** Three gates (P6 audit-class, P7 substrate-prediction MC, C7 geometric truncation diagnostic) close 6A three-layer ρ adjudication into registry. Compute-time dispatch to `mack-cosmic-bridge` runner per partition §1 W8 owner. Concurrent dispatch acceptable for P6 + P7 + C7 (no inter-gate compute-time dependency within W8). Verdict file: `computations/s86_gate_verdicts.txt`.
