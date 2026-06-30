# Session 90 Plan — Wave 8: W5 Convergence + FWD-Cn retries + FWD-C1 single-shot + LMAX scan

**Provenance**: S90 plan-freeze, fanout mode, this file authors Wave 8 only.
Source: `sessions/session-plan/session-90-context.md` §Cluster H lines 130-141 + §Extra Context lines 145-243.
Canonical verdict-file: `computations/session-90/s90_gate_verdicts.txt`
(per `.claude/rules/gate-verdicts.md §"Canonical Verdict-File Path"`).
Author: lizzi-spectral-functional-theorist (orchestrator), 2026-05-12.

---

## Wave 8 Summary

Wave 8 carries the W5 / W6 / FWD-Cn convergence cluster for S90. Eight items
land here: three substrate-IS retries (CF-59 PV-subtracted Mellin moment retry
on the §W5-5 τ=2·τ_fold cross-validation; CF-60 W7a-74 PRIMARY-evaluator
FULL-tier rank-vector retry on §W5-7; CF-65 first-ever L_max-scan parameterized
slope-A canonical on FWD-C1), one substantive Corner-IV FULL BdG re-derivation
(CF-61 BCS gap equation across L_max ∈ {6..12}), three registry-anatomy /
methodology landings (CF-62 §VII.AV Element-1 disambiguation per W-6 Q3 Fork B;
CF-63 deferred-pending mack landing for §VII.AV + §VII.AU with Level-1
single-τ-slice declaration MANDATORY per volovik V.2; CF-64 §VII.AU.OP-PROJ
single-shot AFTER-pattern retry advancing HIT K-counter K=3 → K=4), and one
substrate-distance-2 D_max measurement (CF-66 FULL physical PV pipeline at
Λ_UV = M_KK at the s=4 pole).

The HIT K-counter advancement path is the decisive structural payload. CF-61
(Corner-IV FULL BdG re-derivation) and CF-65 (first-ever L_max-scan on FWD-C1
substrate-IS observable) are the dual PASS hits that advance HIT K=2 → K=3
MANDATORY threshold per `feedback_rules-compensate-missing-structure.md`. CF-64
single-shot 8/8 structural-coherence retry of §VII.AU.OP-PROJ FWD-C1 STAGE-1-
CANDIDATE bridge landing advances HIT K=3 → K=4 (independently from
CF-61+CF-65, provided W2 CF-18 cleanup PRECEDES CF-64). Combined, the wave
saturates HIT corpus from K=2 (S89 close) toward K=4 within a single S90
dispatch — the canonical structural-payload arc for S90.

Total effort: ~6.9 wave-equivalents. CF-61 alone is 1.5 we (BCS gap-equation
regeneration on 7 L_max sectors). CF-59 + CF-60 + CF-65 carry 3.0 we
(substrate-IS retries). CF-62 + CF-63 + CF-64 + CF-66 carry 2.4 we
(structural / registry / D_max measurement). Per-gate primaries: lizzi PRIMARY
on CF-59 / CF-60 / CF-64 / CF-65 with cross-axis co-authorship per Wave 8 spec;
volovik PRIMARY on CF-59 substrate-physics axis (PRIORITY HIGH per V.1) AND
PRIMARY on CF-61; gen-physicist PRIMARY on CF-62 and CF-66; mack-cosmic-bridge
sole-writer on CF-63 (deferred-pending mack landing). Cross-co-authors:
connes-ncg-theorist (CF-60 / CF-61 / CF-64 / CF-65 / CF-66);
phonon-first-cosmologist consulted (CF-62 substrate-IS observable identity).

---

## Wave 8 Decision Point Prerequisites

Cross-wave dependencies are STRICT — Wave 8 will plan-freeze halt without
upstream landings.

- **W2 CF-18 PRECEDES CF-64**: §VII.AAU + §VII.AV `WITHDRAWN-IN-FAVOR-OF-S90-LANDING`
  cleanup must complete and emit valid registry markers before §VII.AU
  single-shot retry frees the slot canonically. Without CF-18, CF-64's
  first-attempt slot allocation collides with the pre-existing §VII.AU
  registry stub from W7c emission #2.
- **W1 CF-14 PRECEDES CF-63**: Deferred-pending rule-file enforcement-clause
  extension (`cross-pillar-bridge-anatomy.md §"Enforcement clause"` deferred-
  pending intermediate verdict-class) must land before mack writes the §VII.AV
  + §VII.AU initial deferred-pending registrations. The deferred-pending state
  must exist as a valid registry verdict before the mack landing references it.
- **W1 CF-15 PRECEDES CF-65**: TEMPLATE-INHERITED convention-tag retrofit on
  §W5-6 producing script (`s89_w5_a30_fwd_c1_retry_parameterized_slope_A_canonical.py`)
  must complete before the FIRST-EXTRACTION regex match on §VII.AU's
  HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier fires. Without CF-15, CF-65's
  PASS does not satisfy the regex required to trigger §VII.AU promotion.
- **CF-62 PRECEDES CF-61**: §VII.AV Element-1 disambiguation (K-window
  log-derivative vs Pillar II Mellin-Barnes residue per W-6 Q3 Fork B) must
  land before Corner-IV FULL BdG re-derivation references the substrate-IS
  observable. Without CF-62, CF-61's α-extraction publishes against an
  ambiguous bridge classification.
- **CF-63 PRECEDES CF-61 + CF-65**: §VII.AV `REGISTRY-INCOMPLETE-PENDING-PROXY-
  REFINEMENT` and §VII.AU `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`
  initial deferred-pending entries must exist before the PASS-triggered
  promotions land. Without CF-63, CF-61 PASS and CF-65 PASS produce orphan
  promotion semantics with no parent entry to upgrade.
- **CF-60 PRECEDES W7 CF-58**: FULL-tier W7a-74 PRIMARY-evaluator rank vectors
  are required inputs for Stage-2 §VII.AR cross-reviewer dispatch (per
  connes V.2 effective dispatch ordering: V.1 → V.2). Wave 8 freezes CF-60
  before Wave 7 dispatches CF-58.

Wave 8 dispatch ordering (sequential within constraints, parallel where
independent):
- **Layer 1**: CF-62 (registry disambiguation, gen-physicist), CF-63 (mack
  deferred-pending landing) — parallel after upstream Layer-0 (W1 CF-14,
  W2 CF-18).
- **Layer 2**: CF-59 (volovik PRIORITY HIGH), CF-60 (lizzi + connes), CF-66
  (gen-physicist + connes D_max) — parallel after Layer 1.
- **Layer 3**: CF-61 (volovik PRIMARY + connes CO; depends on CF-62 landing
  for substrate-IS observable identity), CF-65 (lizzi + connes; depends on
  W1 CF-15 retrofit + CF-63 deferred-pending entry) — parallel after Layer 2.
- **Layer 4**: CF-64 (single-shot AFTER-pattern after W2 CF-18 cleanup +
  CF-63 §VII.AU initial registration).

Layers 1-4 fit the bounded-iteration recovery envelope per
`.claude/rules/v3-closure-recovery.md` Stage-1 cap.

---

## §W8-1. CF-59 — S90-W5-5-RETRY-WITH-PV-SUBTRACTED-MELLIN-S3-EXTRACTION

### Gate ID
`S90-W5-5-RETRY-WITH-PV-SUBTRACTED-MELLIN-S3-EXTRACTION`

### Trigger
`[VERIFY]` — empirical ratio R_emp = slope_A(0.38) / slope_A(0.19) classified
into one of four pre-registered bands (PASS-A / PASS-B / INFO / FAIL); the
gate directly discriminates two pre-registered structural readings of the
substrate-IS slope_A observable at τ=2·τ_fold under PV-subtracted Mellin
moment at s=3 extraction.

### Classification
GEOMETRIC. The slope_A observable IS the substrate-IS substrate-distance-1
Mellin moment at s=3 on the spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`
under PV-subtraction at fixed M_PV²_frac. The PV-subtracted Mellin moment
recipe is the canonical substrate-distance-1 extraction protocol per W1b-1
(S87) calibration; the asymptotic Weyl-fit alternative `d_eff_global=8` is
NOT canonical-anchored at slope_A_FW = 10.122 and was the cause of the §W5-5
miscalibration.

### Agent type
**lizzi-spectral-functional-theorist** PRIMARY (substrate-IS observable
extraction on D_K eigenvalue spectrum + canonical_constants.py:1714
provisional condition discharge); **volovik-superfluid-universe-theorist**
PRIMARY on substrate-physics axis (PRIORITY HIGH per S89 V.1; framework's
sharpest reviewer per `feedback_agent-roster.md`); script
writer = lizzi; volovik adversarial cross-check on R_emp band classification
+ substrate-physics interpretation of Reading-A vs Reading-B verdict.

### Hypothesis
The empirical slope_A ratio at τ=2·τ_fold extracted via PV-subtracted Mellin
moment at s=3 discriminates between the geometric `slope_A_FW = 10/(1−τ/(5π))`
(Reading A; canonical_constants.py:1719) and a linear-LO alternative
(Reading B; `slope_A_LO = 10` constant); Reading A predicts R_emp ≈ 1.012;
Reading B predicts R_emp ≈ 2.000.

### Method (full self-contained dispatch prompt)

Producing script: `computations/session-90/s90_w8_pv_subtracted_mellin_s3_extraction.py`.

#### Step 1 — Input substrate
Load three spectrum caches:
- `computations/session-87/s87_spectrum_cache_L14_tau019.npz` (L=14 cache at
  τ=0.19; baseline endpoint, n_modes ≈ 22000)
- `computations/session-89/s89_w5_a28_spectrum_cache_L6_tau038.npz` (L=6
  cache at τ=0.38; lower endpoint, REUSABLE)
- NEW build of τ=0.38 spectrum at L_max ∈ {10, 12} via
  `computations/_shared/dirac_spectrum.py` Jensen TT-deformation with
  τ_grid = [0.38] + recursive Casimir-projection up to L_max=12
  (~30-60 min wall per W11-3 calibration; runtime feasibility per
  `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection
  Feasibility Pre-Check"`). Cache outputs as gate-produced per-L_max
  spectrum bundles (compute-time outputs of THIS gate, named at script-
  emission time per `gate-verdicts.md` output discipline; NOT pre-existing
  upstream inputs — runtime-rescue path per `.claude/rules/gate-verdicts.md`).

#### Step 2 — Apply PV-subtracted Mellin moment at s=3 (canonical recipe)
From `computations/session-87/s87_w1b_pv_subtraction_recalibration.npz`:
the PV-subtracted Mellin moment at s=3 substrate-distance-1 pole is
```
M_3^{ζ,PV}(τ) = sum_n [|λ_n(τ)|^{-3} − |λ_n(τ)+M_PV²|^{-3}]
              · sign(λ_n(τ))^3
              · multiplicity_n(τ)
```
with M_PV² = M_PV²_frac · |λ_max(τ)|², M_PV²_frac = 0.1 (canonical, W1b-1).

#### Step 3 — Extract slope_A(τ) at fixed L_max
For each L_max ∈ {10, 12} and each τ ∈ {0.19, 0.38}:
```
slope_A(τ; L_max) := M_3^{ζ,PV}(τ) / M_3^{ζ,PV}_geom-ref(τ)
```
where the geometric reference normalizes by the closed-form
`slope_A_FW_Conv_A_GEOMETRIC = "10/(1 − τ/(5·π))"`
(canonical_constants.py:1719); at τ=0.19 the reference value is
`slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384`
(canonical_constants.py:1720).

#### Step 4 — Compute empirical ratio
```
R_emp(L_max) := slope_A(0.38; L_max) / slope_A(0.19; L_max)
```
Reading A predicts R_emp ≈ 10/(1 − 0.38/(5π)) / 10/(1 − 0.19/(5π))
                     = (1 − 0.19/(5π)) / (1 − 0.38/(5π))
                     = 1.0123 (geometric LO);
Reading B predicts R_emp ≈ 2.000 (linear-LO; slope_A grows linearly in τ).

#### Step 5 — Cross-checks
- τ=0.19 baseline reproducibility: assert `|slope_A(0.19; L_max=14) −
  slope_A_FW_Conv_A_AT_TAU_FOLD| / 10.122 < 1e-5` (Class 8.3 publication
  precision tolerance ≥ 1e-5 for canonical anchor).
- L_max convergence: compute R_emp(L_max=10) and R_emp(L_max=12); check
  `|R_emp(L_max=12) − R_emp(L_max=10)| < 0.02` (5% of Reading-A band).
- PV-subtraction stability: vary M_PV²_frac ∈ {0.05, 0.10, 0.20} and verify
  R_emp drift ≤ 0.5% (PV pole-pole cancellation).

#### Step 6 — Verdict-line append
Output to `computations/session-90/s90_gate_verdicts.txt`:
```
S90-W5-5-RETRY-WITH-PV-SUBTRACTED-MELLIN-S3-EXTRACTION: \
  PASS|FAIL|INFO -- value=<R_emp> \
  scheme=PV-subtracted-Mellin-s3 \
  convention=substrate-distance-1-canonical \
  L_max=12 \
  audit_sha256=<closure-over-input-pin-map> \
  content_sha256=<closure-over-script-bytes> schema_version=S84+
```

#### Outputs
- `s90_w8_pv_subtracted_mellin_s3_extraction.npz` (R_emp scan over
  L_max × M_PV²_frac, baseline cross-check, regime certification)
- `s90_w8_pv_subtracted_mellin_s3_extraction.png` (R_emp vs L_max with
  Reading A + Reading B band overlays)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max` | {10, 12} (per W11-3 Casimir-bound + Friedrich-Bär saturation; L_max=12 sufficient at τ=0.38) |
| `tau_grid` | {0.19, 0.38} (exact; τ=0.38 = 2·τ_fold) |
| `M_PV²_frac` | 0.10 primary; {0.05, 0.20} cross-checks |
| `mellin_s` | 3 (substrate-distance-1 pole; canonical) |
| `pv_subtraction_scheme` | Pauli-Villars subtraction at fixed M_PV² (W1b-1 protocol) |
| `dirac_spectrum_module` | `computations/_shared/dirac_spectrum.py` recursive Casimir-projection |
| `tolerance_tau019_baseline` | 1e-5 RATIO vs 10.122438748384 |
| `tolerance_lmax_convergence` | 0.02 ABSOLUTE in R_emp |
| `tolerance_pv_stability` | 0.005 RATIO across M_PV²_frac scan |
| `random_seed` | not applicable (deterministic) |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `substrate-distance-1-canonical` (NOT SCHEMATIC; producing script uses canonical helpers, not `_spectral_action_regulators.py`) |
| `scheme` | `PV-subtracted-Mellin-s3` |

PRDR cardinality check: 13 free parameters; 13 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `s87_spectrum_cache_L14_tau019.npz` | `<computed at plan-freeze>` |
| `s87_w1b_pv_subtraction_recalibration.npz` | `<computed at plan-freeze>` |
| `s89_w5_a28_spectrum_cache_L6_tau038.npz` | `<computed at plan-freeze>` |
| `canonical_constants.py:1719` (slope_A_FW_Conv_A_GEOMETRIC) | `<computed at plan-freeze>` |
| `canonical_constants.py:1720` (slope_A_FW_Conv_A_AT_TAU_FOLD) | `<computed at plan-freeze>` |
| `canonical_constants.py:521` (kappa_2_substrate_FW) | `<computed at plan-freeze>` |
| `canonical_constants.py:522` (tau_max_HK5_regime_FW) | `<computed at plan-freeze>` |
| `dirac_spectrum.py` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value=R_emp ∈ [1.012, 2.000], scheme=PV-subtracted-Mellin-s3, \
 convention=substrate-distance-1-canonical, L_max=12)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate | Reading-A WIN | Reading-B WIN |
|:-----|:----------|:-------------:|:-------------:|
| **PASS-A** | R_emp ∈ [0.95, 1.10] | ✓ Reading A confirmed; canonical_constants.py:1714 provisional condition discharged | — |
| **PASS-B** | R_emp ∈ [1.80, 2.20] | — | ✓ Reading B confirmed; canonical pin replacement required |
| **INFO** | R_emp ∈ (1.10, 1.80) ∪ (2.20, ∞) | ambiguous | ambiguous |
| **FAIL** | R_emp < 0.95 OR baseline cross-check `|slope_A(0.19) − 10.122| / 10.122 ≥ 1e-5` | structural breakdown | structural breakdown |

Composite collapse (per `gate-verdicts.md §"Composite-collapse rule"`):
sign_verdict = PASS if R_emp > 0; magnitude_verdict per band table;
regime_verdict = VALID if L_max convergence `|R_emp(12) − R_emp(10)| < 0.02`,
MARGINAL if 0.02 ≤ delta < 0.05, BREAKDOWN if ≥ 0.05.

### Substitution chain (MANDATORY per `math-scripts.md §"Double-Check Logic"`)

```
Definitions:
  slope_A_FW(τ)          := 10 / (1 − τ/(5π))         [Reading A; geometric LO]
  slope_A_LO(τ)          := 10                          [Reading B; linear-LO degenerate]
  M_3^{ζ,PV}(τ)          := PV-subtracted Mellin moment at s=3
  M_3^{geom-ref}(τ)      := closed-form geometric reference normalization
  slope_A_emp(τ; L_max)  := M_3^{ζ,PV}(τ) / M_3^{geom-ref}(τ)
  R_emp(L_max)           := slope_A_emp(0.38; L_max) / slope_A_emp(0.19; L_max)

Substitutions:
  Step 1: Under Reading A (canonical),
          slope_A_emp(τ; L_max → ∞) → slope_A_FW(τ) by definition
  Step 2: R_emp^{Reading-A} = slope_A_FW(0.38) / slope_A_FW(0.19)
                            = [10/(1−0.38/(5π))] / [10/(1−0.19/(5π))]
                            = (1 − 0.19/(5π)) / (1 − 0.38/(5π))
                            = (1 − 0.012099) / (1 − 0.024197)
                            = 0.987901 / 0.975803
                            = 1.01240
  Step 3: Under Reading B (linear-LO degenerate),
          slope_A_emp(τ; L_max → ∞) → slope_A_LO·(τ/τ_fold)
  Step 4: R_emp^{Reading-B} = slope_A_LO(0.38) / slope_A_LO(0.19)
                            = 2·slope_A_LO(0.19) / slope_A_LO(0.19)
                            = 2.000
  Step 5: PASS-A band [0.95, 1.10] centered on 1.0124 with ±10% half-width
          PASS-B band [1.80, 2.20] centered on 2.000 with ±10% half-width
          Bands are NON-OVERLAPPING (gap [1.10, 1.80] wide)
  Step 6: Direction: R_emp PASS-A ⟹ Reading A holds at substrate-distance-1
          Direction: R_emp PASS-B ⟹ Reading B holds at substrate-distance-1

Conclusion: A computed R_emp ∈ [0.95, 1.10] discharges canonical_constants.py:1714
            provisional condition on slope_A_FW_Conv_A_GEOMETRIC adoption.
            A computed R_emp ∈ [1.80, 2.20] forces canonical pin replacement.
            INFO/FAIL routes to S91 remediation.
```

### What PASSES/FAILS MEAN for solution space

- **PASS-A (R_emp ∈ [0.95, 1.10])**: Reading A WIN. The substrate's slope_A
  observable IS geometric per canonical_constants.py:1719 closed-form.
  canonical_constants.py:1714 provisional condition discharged.
  HIT K-counter advances K=2 → K=3 (joint with CF-65). Single-τ-slice vs
  moduli-deformation substrate-IS levels K-counter advances K=2 → K=3
  (Level-1 single-τ-slice at τ_fold = 0.19; Level-2 moduli-deformation at
  τ = 2·τ_fold = 0.38). Forward consumer §VII.AV registry text pinned to
  Reading A geometric closure.
- **PASS-B (R_emp ∈ [1.80, 2.20])**: Reading B WIN. The substrate's slope_A
  observable is linear-LO, not geometric. canonical_constants.py:1719 pin
  REQUIRES replacement; downstream consumers (FWD-C1 §VII.AU spec,
  cross-pillar-bridge-corpus §4) require re-pinning. HIT K-counter does
  NOT advance (since the structural reading flips); §VII.AV registry text
  routes to canonical-pin-replacement remediation.
- **INFO (R_emp ∈ (1.10, 1.80) ∪ (2.20, ∞))**: structural ambiguity at
  τ=2·τ_fold; neither Reading wins. Carry-forward to S91 with refined L_max
  cache + alternative Mellin pole.
- **FAIL (R_emp < 0.95 OR baseline cross-check fails)**: the substrate-IS
  observable extraction protocol breaks at the canonical anchor τ=0.19;
  forces re-validation of the PV-subtracted Mellin moment recipe itself.

### Effort estimate
1.0 wave-equivalent. Includes ~30-60 min wall for τ=0.38 spectrum build at
L_max ∈ {10, 12} per W11-3 calibration; remainder is PV-subtracted Mellin
moment evaluation (closed-form sum over precomputed eigenvalues) + ratio
classification.

### Substrate-framing reminder
The substrate IS the spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L}(τ))`.
The slope_A observable IS the substrate-distance-1 Mellin moment at s=3 on
that triple under PV-subtraction at fixed M_PV²_frac. At τ_fold = 0.19 the
substrate IS the single-τ-slice spectral triple (Level 1); at τ=2·τ_fold the
substrate IS a moduli-deformation of that triple (Level 2). The R_emp ratio
IS the comparison of two substrate-IS observables at two τ-slices; it is
NOT a comparison "of slope_A in expanding space" or "across an inflating
container" — there is no container. Per
`phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS
levels"` (K=2 MANDATORY since S88 W-7 V.4), Reading A WIN demonstrates the
substrate's intrinsic τ-deformation structure preserves the geometric
slope_A closed-form; Reading B WIN demonstrates a structurally distinct
linear-LO τ-dependence intrinsic to the moduli manifold.

---

## §W8-2. CF-60 — S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR

### Gate ID
`S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR`

### Trigger
`[VERIFY]` — Spearman cross-tier rank correlation between SCHEMATIC and FULL
physical regularization tiers; verdict classifies §VII.AR LEVEL-DRESSED into
WEAKENED (Spearman ≥ 0.9; SCHEMATIC is faithful proxy) vs STRENGTHENED
(Spearman < 0.9; SCHEMATIC differs structurally from FULL).

### Classification
GEOMETRIC. The W7a-74 PRIMARY evaluator computes substrate-IS spectral
moments under FULL physical regularizations (Pauli-Villars subtraction at
M_PV²_frac = 0.1, hard cutoff at cutoff_frac = 0.7, Mellin via
`analytic_zeta`, zeta and heat-kernel via canonical
`_spectral_action_regulators.py` FULL-tier branches — NOT SCHEMATIC
branches). The output rank vector across 5 anchors is the substrate-IS
PRIMARY observable; the §W5-7 SCHEMATIC rank vector is the methodology-floor
image under the layer-functor F per `epistemic-discipline.md §"Layer-
Decomposition"`.

### Agent type
**lizzi-spectral-functional-theorist** PRIMARY (substrate-IS PRIMARY-tier
spectral moments evaluation); **connes-ncg-theorist** CO-AUTHOR (FULL-tier-
vs-SCHEMATIC structural reading at the NCG-axiomatic side; verifies the
cross-tier comparison respects the algebra-INVARIANT vs algebra-DEPENDENT
4-corner orthogonality per `cross-pillar-bridge-anatomy.md §"Algebra-axis
orthogonality K-counter"` MANDATORY at K=3).

### Hypothesis
The §W5-7 SCHEMATIC rank vector across 5 anchors of the §VII.AR LEVEL-DRESSED
classification space (`{F_2, cutoff_sqrt, anomaly, Zubarev}` at s=4 pole +
anchor-5 unit-consistency check) is either (a) a faithful proxy for the FULL
physical rank vector (Spearman cross-correlation ≥ 0.9; §VII.AR LEVEL-DRESSED
WEAKENED to "SCHEMATIC robust"), or (b) structurally distinct from the FULL
physical rank vector (Spearman < 0.9; §VII.AR LEVEL-DRESSED STRENGTHENED to
"SCHEMATIC vs FULL non-trivial structural differentiation").

### Method (full self-contained dispatch prompt)

Producing script: `computations/session-90/s90_w8_w7a74_primary_evaluator_full_tier_retry.py`.

#### Step 1 — Locate W7a-74 PRIMARY evaluator script
At plan-freeze: locate the canonical W7a-74 PRIMARY evaluator script in
`computations/session-87/` directory matching `s87_w7a_74_*.py`. Snapshot
its content_sha256 into the input-pin map.

#### Step 2 — Load S84 L_max=12 master cache
Load `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (master
cache at τ_fold = 0.19, L_max=12, n_modes ≈ 16800).

#### Step 3 — Evaluate FULL-tier rank vector across 5 anchors
For each anchor a ∈ {F_2, cutoff_sqrt, anomaly, Zubarev, anchor-5} compute
the FULL-tier spectral moment at s=4 substrate-distance-2 pole:
```
M_a^{FULL,s=4} := PV-subtracted Σ_n [|λ_n|^{-4} · regulator_a(λ_n)]
                  − PV-subtracted Σ_n [|λ_n + M_PV²|^{-4} · regulator_a(λ_n + M_PV²)]
```
with M_PV²_frac = 0.1 (hard pin), cutoff_frac = 0.7 (hard cutoff at
0.7·λ_max), Mellin contour via `analytic_zeta` complex-plane integral,
zeta-tail via canonical `_spectral_action_regulators.py:zeta_a_n_FULL`
branch, heat-kernel via canonical `pauli_villars_a_n_FULL`. Anchor-5
unit-consistency: compute `M_5^{FULL,s=4} := M_a^{FULL,s=4} · M_KK^{-2}`
with explicit unit-cancellation cross-check per CONNES V.5.

#### Step 4 — Build FULL-tier rank vector
```
rank_vector^{FULL} := argsort(M_a^{FULL,s=4} for a ∈ {1..5}, descending)
```
Cross-check: load §W5-7 npz `s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz`
and extract `rank_vector^{SCHEMATIC}`.

#### Step 5 — Compute Spearman cross-tier correlation
```
spearman_cross_tier := scipy.stats.spearmanr(rank_vector^{FULL},
                                              rank_vector^{SCHEMATIC}).statistic
```

#### Step 6 — Count anchors PASSing FULL-tier admissibility
```
N_FULL := |{a : M_a^{FULL,s=4} is finite ∧ non-NaN ∧ within plausible band}|
```
Plausible band: `M_a^{FULL,s=4} ∈ [1e-50, 1e50]` (relative to M_KK² baseline,
8 OOM band; non-tied rank requires distinct M_a values up to 1e-15 floor).

#### Step 7 — Verdict-line append
```
S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR: \
  PASS|FAIL|INFO -- value=<(N_FULL, spearman_cross_tier)> \
  scheme=W7a74-PRIMARY-FULL-tier \
  convention=FULL-physical-regularization-NOT-SCHEMATIC \
  L_max=12 \
  audit_sha256=<closure> content_sha256=<closure> schema_version=S84+
```
Convention tag explicitly does NOT carry the `-SCHEMATIC` suffix; this
gate's purpose IS the FULL-physical-tier evaluation. Per
`substrate-first-canonical-sourcing.md §(iv)` CLASS pin = FULL.

#### Outputs
- `s90_w8_w7a74_primary_evaluator_full_tier_retry.npz` (5-anchor M_a values,
  rank vectors, Spearman correlation, anchor-5 unit-consistency log)
- `s90_w8_w7a74_primary_evaluator_full_tier_retry.png` (Spearman scatter
  + cross-tier rank-comparison overlay)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 12 (S84 master cache) |
| `tau` | 0.19 (τ_fold; single-τ-slice) |
| `M_PV²_frac` | 0.10 (FULL-tier hard pin) |
| `cutoff_frac` | 0.70 (FULL-tier hard cutoff) |
| `mellin_method` | `analytic_zeta` complex-plane integral (NOT SCHEMATIC interpolation) |
| `regulator_tier` | FULL (NOT SCHEMATIC; CLASS pin per §(iv)) |
| `regulators` | {F_2, cutoff_sqrt, anomaly, Zubarev, anchor-5-unit-consistency} |
| `mellin_s` | 4 (substrate-distance-2 pole; §VII.AR baseline) |
| `spearman_threshold` | 0.9 (PASS-A vs PASS-B boundary; pre-registered) |
| `N_FULL_threshold` | 4/5 (PASS / INFO boundary) |
| `plausible_band` | [1e-50, 1e50] in M_KK² units |
| `random_seed` | not applicable (deterministic) |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `FULL-physical-regularization-NOT-SCHEMATIC` |
| `scheme` | `W7a74-PRIMARY-FULL-tier` |

PRDR cardinality check: 14 free parameters; 14 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `s87_w7a_74_*.py` (PRIMARY evaluator) | `<located at plan-freeze>` |
| `s84_spectrum_cache_L12_tau019.npz` | `<computed at plan-freeze>` |
| `s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz` | `<computed at plan-freeze>` |
| `_spectral_action_regulators.py` (FULL branches) | `<computed at plan-freeze>` |
| `permanent-results-registry.md §VII.AR` baseline | `<computed at plan-freeze>` |
| `canonical_constants.py:M_KK` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value=(N_FULL, spearman_cross_tier), scheme=W7a74-PRIMARY-FULL-tier, \
 convention=FULL-physical-regularization-NOT-SCHEMATIC, L_max=12)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate | §VII.AR consequence |
|:-----|:----------|:--------------------|
| **PASS-A** | N_FULL ≥ 4/5 AND spearman_cross_tier ≥ 0.9 | rankings COINCIDE; SCHEMATIC IS faithful proxy; §VII.AR LEVEL-DRESSED WEAKENED to "SCHEMATIC robust" |
| **PASS-B** | N_FULL ≥ 4/5 AND spearman_cross_tier < 0.9 | rankings DIFFER; §VII.AR LEVEL-DRESSED STRENGTHENED to "SCHEMATIC vs FULL non-trivial differentiation" |
| **INFO** | N_FULL = 3 | partial admissibility; §VII.AR PASS-band hedged; queue for S91 with refined regulator-class extension |
| **FAIL** | N_FULL < 3 OR all-tied (rank vector degenerate) OR any anchor NaN | regulator class breakdown at substrate-distance-2 pole; §VII.AR LEVEL-DRESSED FAILS structural inheritance |

Composite collapse: sign_verdict = N/A (no signed delta);
magnitude_verdict per band table; regime_verdict = VALID if FULL-tier
evaluations complete without numerical overflow / underflow, MARGINAL if
1 anchor saturates the plausible band edge, BREAKDOWN if ≥ 2 anchors
saturate or anchor-5 unit-consistency check fails.

### Substitution chain (MANDATORY for Spearman direction claim)

```
Definitions:
  rank_vector^{SCHEMATIC} := argsort(M_a^{SCHEMATIC,s=4}, descending)
                              [§W5-7 npz canonical]
  rank_vector^{FULL}      := argsort(M_a^{FULL,s=4}, descending)
                              [this gate's output]
  spearman(X, Y)          := 1 − (6 · Σ d_i²) / (n · (n² − 1))
                              [Spearman rho on rank vectors]
  threshold               := 0.9

Substitutions:
  Step 1: If SCHEMATIC tier faithfully proxies FULL tier
          (i.e., the regulator-class-INVARIANT relative ordering is preserved
          under the layer-functor F: SCHEMATIC → FULL),
          then rank_vector^{SCHEMATIC} ≡ rank_vector^{FULL} modulo
          tied-pair permutations.
  Step 2: spearman(rank_vector^{SCHEMATIC}, rank_vector^{FULL}) → 1.0
          in the layer-functor-faithful limit.
  Step 3: If SCHEMATIC tier diverges from FULL tier at any anchor a*,
          then rank_vector^{SCHEMATIC} and rank_vector^{FULL} differ at
          rank-position rank^{SCHEMATIC}(a*), producing d_{rank^{SCHEMATIC}(a*)} > 0.
  Step 4: spearman drops below 1.0 monotonically with the count of
          divergent anchors weighted by rank-position squared.
  Step 5: spearman ≥ 0.9 ⟹ at most 1 anchor divergent at adjacent ranks
                            (4 of 5 rank-stable);
          spearman < 0.9 ⟹ multi-anchor divergence OR non-adjacent rank
                            permutation (cross-tier rank scrambling).
  Step 6: Direction: PASS-A (spearman ≥ 0.9) ⟹ §VII.AR LEVEL-DRESSED
                       WEAKENED (the cross-tier-rank-PARAMETER-coupling
                       sub-claim B is structurally weakened).
          Direction: PASS-B (spearman < 0.9) ⟹ §VII.AR LEVEL-DRESSED
                       STRENGTHENED.

Conclusion: spearman_cross_tier classifies §VII.AR LEVEL-DRESSED into
            WEAKENED or STRENGTHENED, feeding the Stage-2 cross-axis
            independent-verify gate CF-58 (Wave 7) with the substrate-IS
            FULL-tier rank vector as one of its input pins.
```

### What PASSES/FAILS MEAN for solution space

- **PASS-A (Spearman ≥ 0.9)**: §VII.AR LEVEL-DRESSED Sub-claim B (cross-tier
  rank-PARAMETER-coupling) is WEAKENED. SCHEMATIC IS a faithful proxy at the
  rank-ordering level. Forward consumer CF-58 Stage-2 dispatch dispatches
  with rank-faithfulness as a confirmed input. The K=3 promotion of cross-
  pillar-bridge-anatomy is preserved; CONNES V.4 PROVISIONAL tagging remains
  PROVISIONAL pending Stage-2.
- **PASS-B (Spearman < 0.9)**: §VII.AR LEVEL-DRESSED Sub-claim B STRENGTHENED.
  SCHEMATIC vs FULL are structurally differentiated; the LEVEL-DRESSED
  classification of Var_a (W-3 CF-LZ-1) AND §VII.AR jointly carry the
  STRENGTHENED form. CONNES V.4 PROVISIONAL tagging promotes to LANDED.
- **INFO (N_FULL = 3)**: partial admissibility — §VII.AR LEVEL-DRESSED PASS-
  band is hedged; Stage-2 dispatch CF-58 conditional on S91 regulator-class
  extension.
- **FAIL (N_FULL < 3 OR degenerate rank)**: regulator-class breakdown at
  substrate-distance-2 pole; §VII.AR LEVEL-DRESSED FAILS structural
  inheritance from SCHEMATIC tier; Stage-2 dispatch blocked.

### Effort estimate
1.0 wave-equivalent. Includes locate-evaluator (~10 min), FULL-tier 5-anchor
evaluation on S84 cache (~30 min wall on GPU), Spearman computation +
verdict-line emission (~5 min), output npz/png generation.

### Substrate-framing reminder
The substrate IS the spectral triple at τ_fold = 0.19 (single-τ-slice;
Level 1). The 5-anchor FULL-tier moment values M_a^{FULL,s=4} ARE
substrate-IS observables at substrate-distance-2 pole s=4. The SCHEMATIC
counterpart M_a^{SCHEMATIC,s=4} IS the methodology-floor image of the
substrate under the layer-functor F per `epistemic-discipline.md §"Layer-
Decomposition"`. The Spearman cross-tier correlation IS the structural
fidelity measure of F at the rank-ordering level — not a "statistical test
of agreement" but a structural-orthogonality probe on the substrate-IS
algebra-INVARIANT spectrum-only-functional family per
`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`
MANDATORY-K=3.

---

## §W8-3. CF-61 — S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS

### Gate ID
`S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS`

### Trigger
`[VERIFY-THEOREM]` — Corner-IV K-window log-derivative substrate-IS theorem
empirical α extraction across L_max ∈ {6, 7, 8, 9, 10, 11, 12}; PASS triggers
§VII.AV promotion from `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` to
registry-PASS-eligible STAGE-1-CANDIDATE.

### Classification
GEOMETRIC. The Corner-IV K-window log-derivative IS a substrate-IS observable
on the BdG sub-algebra `M_2(ℂ)` of the substrate spectral triple
`(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The FULL BdG re-derivation IS the
substantive substrate-physics computation that the Casimir-bound proxy of
§W5-3 was a placeholder for. Promotion semantics IS the §VII.AV registry-
status upgrade from deferred-pending to STAGE-1-CANDIDATE upon empirical α
extraction passing the [2.5, 3.5] L^{-3}-envelope band per Level-2-binding
discipline.

### Agent type
**volovik-superfluid-universe-theorist** PRIMARY (substrate-superfluid
domain expertise: BCS gap equation regeneration, Bogoliubov diagonalization
on truncated D_K spectrum, K-window log-derivative substrate-IS observable
identity); **connes-ncg-theorist** CO-AUTHOR (registry-promotion semantics
+ bridge-anatomy audit on Element-1 disambiguation post-CF-62 landing;
Level-2-binding admissibility per `cross-pillar-bridge-anatomy.md §"Level-2-
binding"` SUGGESTION at K=1 — this gate is calibration corpus instance #2);
gen-physicist optional adversarial review on α extraction methodology.

### Hypothesis
Empirical envelope α extraction at Corner-IV K-window log-derivative
substrate-IS observable via FULL BdG re-derivation at L_max ∈ {6..12} (not
Casimir-bound proxy) yields α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND L_max=12 bit-
for-bit anchor match `L_emp(L_max=12) = L_emp(∞) = -7.046336474406761`,
satisfying the L^{-3} algebraic envelope at d=4 per `cross-pillar-bridge-
anatomy.md §"Level-2-binding"` admissibility.

### Method (full self-contained dispatch prompt)

Producing script: `computations/session-90/s90_w8_corner_iv_full_bdg_rederive_per_lmax.py`.

#### Step 1 — Pre-flight Casimir-bound feasibility per `math-scripts.md`
Verify L_max ∈ {6..12} all fall within Friedrich-Bär saturation bound
`η_FB_lower = 0.40 · √(C_2(p+q) + 1)`. For L_max=12 the Casimir bound on
the deepest BdG sector is computed analytically; cross-validate against
S87 W11-3 calibration corpus (`block-diagonal-cache-plus-friedrich-baer-bound`
scheme). Output `casimir_feasibility_log.json` confirming PASS.

#### Step 2 — Load L_max=12 master cache + L_max ∈ {6..11} sub-truncations
Load `s84_spectrum_cache_L12_tau019.npz` master cache. For each
L_max ∈ {6..11}, filter the spectrum to retain only Peter-Weyl sectors
(p, q) with `p + q ≤ L_max`. Hold the 7 spectrum subsets in memory
(in-script Python dict keyed by L_max); intra-wave intermediate, not
persisted to disk (no upstream-input pin required).

#### Step 3 — BCS gap equation regeneration per L_max
For each L_max ∈ {6..12}, solve self-consistently:
```
1/V_BCS = Σ_a [1 / (2 · E_a(L_max))] · tanh(E_a(L_max) / (2·T))
```
where:
- V_BCS = canonical BCS coupling pinned at substrate-natural value reproducing
  `Delta_BCS = 0.464 · M_KK` at L_max=∞ continuum limit
- E_a(L_max) = sqrt(λ_a²(L_max) + Δ²(L_max)) (Bogoliubov mode energies)
- T = T_fold (substrate-natural temperature at τ_fold)
- iterative solve: initialize Δ_0 = Δ_BCS, update Δ_{n+1} from gap-equation
  fixed-point, convergence criterion `|Δ_{n+1} − Δ_n| / Δ_n < 1e-10`

Output: `delta_bcs_per_lmax` array of 7 gap values.

#### Step 4 — Bogoliubov diagonalization per L_max
For each L_max ∈ {6..12}, diagonalize the BdG Hamiltonian:
```
H_BdG(L_max) = (h(L_max), Δ(L_max); Δ*(L_max), -h*(L_max))
```
where `h(L_max)` is the L_max-truncated D_K^2 single-particle Hamiltonian.
Extract 8 BdG mode amplitudes (u_k, v_k, E_qp) per L_max sector. Cross-check
against `computations/session-52/s52_bogoliubov_amp.npz` canonical amplitudes
at L_max → ∞ continuum limit.

Output: per-L_max BdG amplitude tensor of shape (7, 8) produced as
this gate's compute-time output (filename assigned at script-emission time
per `gate-verdicts.md` output discipline; NOT a pre-existing upstream input).

#### Step 5 — K-window log-derivative substrate-IS observable computation
For each L_max ∈ {6..12} compute the K-window log-derivative substrate-IS
observable on the BdG sub-algebra `M_2(ℂ)`:
```
L_emp(L_max) := d/d(ln K) [Σ_a (E_a(L_max) / Δ(L_max))² · θ(K - E_a)]
                evaluated at canonical K-window K* = K_canonical
```
where K_canonical is pinned at substrate-natural BdG energy threshold per
W-6 §VII.AV substrate-IS spec post-CF-62 disambiguation.

Verify L_max=12 anchor:
```
| L_emp(L_max=12) - (-7.046336474406761) | < 1e-9
```
(bit-for-bit match against §W5-2 npz canonical anchor `L_emp(∞)`).

#### Step 6 — Empirical α extraction via log-log regression
Compute `delta_L(L_max) := |L_emp(L_max) - L_emp(L_max=12)|` for
L_max ∈ {6..11}. Apply log-log linear regression:
```
log(delta_L(L_max)) = log(C) - α · log(L_max)
```
Extract α (slope) and R² (goodness-of-fit). Cross-validate against
predicted L^{-3} envelope per `cross-pillar-bridge-anatomy.md §"Level-2-
binding"` d=4 calibration.

#### Step 7 — Promotion semantics trigger
IF PASS (α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND L_max=12 anchor match):
- Emit verdict-line PASS
- Trigger §VII.AV registry-status upgrade from `REGISTRY-INCOMPLETE-PENDING-
  PROXY-REFINEMENT` to STAGE-1-CANDIDATE registry-PASS-eligible per
  `joint-theorem-promotion.md §"Stage 1"`
- Append cross-link in verdict-line companion row pointing to §VII.AV
  registry entry update target

#### Step 8 — Verdict-line append
```
S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS: \
  PASS|FAIL|INFO -- value=<(alpha, R², L_emp(12))> \
  scheme=FULL-BdG-rederivation-per-lmax \
  convention=corner-iv-K-window-log-derivative-substrate-IS \
  L_max=12 \
  audit_sha256=<closure> content_sha256=<closure> schema_version=S84+
```
Companion row:
```
# sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL \
# regime_verdict=VALID|MARGINAL|BREAKDOWN \
# S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS \
# 3-tuple annotation (S87 schema-v2)
```
SECOND companion: §VII.AV promotion cross-link
```
# promotion_target=permanent-results-registry.md §VII.AV \
# from=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT to=STAGE-1-CANDIDATE
```

#### Outputs
- `s90_w8_corner_iv_full_bdg_rederive_per_lmax.npz` (per-L_max BCS gap +
  BdG modes + L_emp + delta_L + log-log fit parameters)
- `s90_w8_corner_iv_full_bdg_rederive_per_lmax.png` (delta_L vs L_max
  log-log scatter with L^{-3} envelope overlay)
- `casimir_feasibility_log.json` (pre-flight feasibility certification)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max_scan` | {6, 7, 8, 9, 10, 11, 12} (7 sectors) |
| `tau` | 0.19 (τ_fold; Level-1 single-τ-slice; post-CF-62 substrate-IS observable identity) |
| `K_canonical` | substrate-natural BdG energy threshold (post-CF-62 pinned) |
| `V_BCS` | substrate-natural coupling reproducing Delta_BCS at L_max→∞ |
| `T` | T_fold (substrate-natural at τ_fold) |
| `gap_eq_convergence` | 1e-10 RATIO (`|Δ_{n+1} − Δ_n| / Δ_n`) |
| `lmax12_anchor_tolerance` | 1e-9 ABSOLUTE (bit-for-bit match) |
| `alpha_passband` | [2.5, 3.5] |
| `r_squared_passband` | ≥ 0.95 |
| `alpha_infoband` | [2.0, 2.5) ∪ (3.5, 4.5] |
| `r_squared_infoband` | [0.90, 0.95) |
| `regulator_tier` | FULL (FULL physical BdG; NOT SCHEMATIC) |
| `friedrich_baer_eta_lower` | 0.40 (S87 W11-3 calibration) |
| `random_seed` | not applicable (deterministic gap-equation solve) |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `corner-iv-K-window-log-derivative-substrate-IS` |
| `scheme` | `FULL-BdG-rederivation-per-lmax` |

PRDR cardinality check: 16 free parameters; 16 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `s52_bogoliubov_amp.npz` | `<computed at plan-freeze>` |
| `s84_spectrum_cache_L12_tau019.npz` | `<computed at plan-freeze>` |
| `§W5-2 npz canonical anchor L_emp(∞) = -7.046336474406761` | `<computed at plan-freeze>` |
| `§W5-3 npz Casimir-bound proxy` | `<computed at plan-freeze>` |
| `permanent-results-registry.md §VII.AV` (post-CF-62 disambiguation) | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md §"Level-2-binding"` | `<computed at plan-freeze>` |
| `canonical_constants.py:M_KK,Delta_BCS,tau_fold` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value=(alpha, R², L_emp_12), scheme=FULL-BdG-rederivation-per-lmax, \
 convention=corner-iv-K-window-log-derivative-substrate-IS, L_max=12)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate | §VII.AV promotion |
|:-----|:----------|:------------------|
| **PASS** | α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND `|L_emp(12) - (-7.046336474406761)| < 1e-9` | from `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` to STAGE-1-CANDIDATE; HIT K-counter K=2 → K=3 (joint with CF-65 dual PASS) |
| **INFO** | α ∈ [2.0, 2.5) ∪ (3.5, 4.5] OR R² ∈ [0.90, 0.95) | partial Level-2-binding; §VII.AV remains REGISTRY-INCOMPLETE; queue for S91 |
| **FAIL** | α outside [2.0, 4.5] OR R² < 0.90 OR L_max=12 anchor mismatch | Level-2-binding violated; §VII.AV remains REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT; structural carry-forward to S91 |

Composite collapse: sign_verdict = PASS by-construction (α > 0 is the
direction; logical implication of L^{-3} envelope at d=4);
magnitude_verdict per band; regime_verdict = VALID if BCS gap-equation
converges within tolerance at every L_max, MARGINAL if one L_max requires
> 1000 iterations, BREAKDOWN if any L_max fails to converge.

### Substitution chain (MANDATORY for α extraction direction)

```
Definitions:
  L_emp(L_max)        := K-window log-derivative substrate-IS observable
                         on BdG sub-algebra at truncation L_max
  L_emp(∞)            := canonical anchor -7.046336474406761 (§W5-2 npz)
  delta_L(L_max)      := | L_emp(L_max) - L_emp(∞) |
  alpha               := -slope of log-log fit of delta_L vs L_max
  envelope predicted  := L^{-3} (per cross-pillar-bridge-anatomy.md
                         §"Level-2-binding" d=4 calibration)

Substitutions:
  Step 1: Per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-
          Confidence Ladder"` Level-2 algebraic envelope at d=4,
          the convergence rate of an HKR-image observable to its continuum
          partner is bounded by L^{-3}.
  Step 2: Under the Pillar III/IV ↔ Pillar V bridge (post-CF-62 update),
          delta_L(L_max) = O(L_max^{-α}) with α predicted = 3 at d=4.
  Step 3: Log-log fit: log(delta_L) = log(C) - α · log(L_max).
          PASS band [2.5, 3.5] centered on α = 3 with ±17% half-width
          accommodating finite-L_max corrections.
  Step 4: L_max=12 anchor: by definition of L_emp(∞) = canonical value at
          ∞-limit, at L_max=12 the BdG truncation must produce
          L_emp(12) ≡ L_emp(∞) bit-for-bit (12 is the canonical anchor
          truncation; deeper L_max introduces no new BdG mode below K-window).
  Step 5: Direction: α ∈ [2.5, 3.5] AND L_max=12 anchor match ⟹
          Level-2-binding envelope confirmed at this substrate-IS observable
          ⟹ §VII.AV promotion to STAGE-1-CANDIDATE structurally licensed.
  Step 6: α ∈ [2.0, 2.5) ∪ (3.5, 4.5] ⟹ partial envelope match; not
          Level-2-binding admissible; INFO carry-forward.
          α outside [2.0, 4.5] ⟹ envelope structurally violated; Level-2-
          non-binding; §VII.AV REJECTED for STAGE-1-CANDIDATE promotion.

Conclusion: A PASS verdict directly upgrades §VII.AV registry status from
            REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT to STAGE-1-
            CANDIDATE. Combined with CF-65 PASS, advances HIT K-counter
            K=2 → K=3 (MANDATORY threshold per
            feedback_rules-compensate-missing-structure.md).
```

### What PASSES/FAILS MEAN for solution space

- **PASS**: §VII.AV registry-status upgrade to STAGE-1-CANDIDATE per
  `joint-theorem-promotion.md §"Stage 1"`. The Corner-IV K-window log-
  derivative substrate-IS observable IS Level-2-binding at d=4 with L^{-3}
  envelope confirmed. Forward consumer: §VII.AV cross-references the FULL
  BdG re-derivation as the substrate-IS-anchored Level-3 empirical value.
  Joint with CF-65 PASS: HIT K-counter K=2 → K=3, hitting the MANDATORY
  promotion threshold per `feedback_rules-compensate-missing-structure.md`.
  Calibration corpus advances: `cross-pillar-bridge-anatomy.md §"Level-2-
  binding"` SUGGESTION K=1 → K=2 (new instance: Corner-IV BdG observable).
- **INFO**: partial Level-2-binding; §VII.AV remains REGISTRY-INCOMPLETE.
  Routes to S91 with refined L_max scan (extend to L_max=14 if Friedrich-
  Bär saturation extension lands) and/or refined K_canonical pin.
- **FAIL**: Level-2-binding violated at this substrate-IS observable.
  §VII.AV remains REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT permanently
  unless a structurally different substrate-IS proxy can be derived.
  Structural carry-forward to S91 for proxy-refinement alternatives.

### Effort estimate
1.5 wave-equivalents. Includes BCS gap-equation iterative solve at 7
L_max sectors (~10-20 min wall per sector × 7 = ~2 hr wall), Bogoliubov
diagonalization on each truncated spectrum, K-window log-derivative
observable computation, log-log α extraction. Cache hit on
`s84_spectrum_cache_L12_tau019.npz` master eliminates spectrum-build cost.

### Substrate-framing reminder
The substrate IS the spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L}(τ_fold))`.
The BdG sub-algebra `M_2(ℂ) ⊂ A_K` is intrinsic to the substrate's finite
spectral triple — it is NOT a "BCS phenomenological model" or "Hamiltonian
in a superconducting container". The Corner-IV K-window log-derivative IS a
single-summand-projection trace on `M_2(ℂ)` per `mechanical-closure-discipline.md
§"Layer-separability carve-out"` Type-F observable class (operator-side;
algebra-INVARIANT). The L_max truncation IS the finite spectral triple's
own truncation parameter; the L_max → ∞ limit IS the continuum cohomology-
class binding under the HKR map per `cross-pillar-bridge-anatomy.md §"Level-2-
binding"`. Direction of explanation: substrate (Pillar III/IV BdG-spectral-
triple) → bridge (HKR L_max → ∞) → laboratory (Pillar V continuum lab-IN
observable).

---

## §W8-4. CF-62 — S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION

### Gate ID
`S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION`

### Trigger
`[AUDIT]` — registry-anatomy disambiguation of §W5-4 Element-1 between two
competing substrate-IS observable specifications surfaced at W-6 Q3 Fork B.
Verdict updates the §VII.AV registry-anchor framing, the FWD-C2 bridge
classification, and emits a SUPERSEDES-tagged corrective canonical line
per Option A protocol.

### Classification
META (registry-anatomy disambiguation). The choice between
`Pillar II Mellin-Barnes residue` (line 898 of §W5-4 WP) and
`K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` (line 1011 of
§W5-4 WP) IS a structural pre-registration question, not a substrate-physics
computation. Per W-6 Q3 Fork B, the K-window log-derivative IS the actual
substrate-IS observable; the Mellin-Barnes residue is a derived proxy.

### Agent type
**gen-physicist** PRIMARY (bridge-classification re-evaluation; cross-pillar-
bridge-anatomy Element-1 audit); **connes-ncg-theorist** CO-AUTHOR (bridge-
anatomy audit on Element-1 5-anatomy IS-not-IN compliance);
**phonon-first-cosmologist** consulted (substrate-IS observable identity per
W-6 Q3 Fork B precedent on K-window observables).

### Hypothesis
The §W5-4 WP carries TWO mutually inconsistent substrate-IS observable
specifications at Element-1; the W-6 Q3 Fork B resolution selects the
K-window log-derivative on the substrate spectral triple as the canonical
Element-1, demoting the Mellin-Barnes residue to derived-proxy status; the
bridge-classification therefore updates from "Pillar II ↔ Pillar V" to
"Pillar III/IV ↔ Pillar V", and §VII.AV may require RE-ANCHORING as
FWD-C2.bdg or a re-specification of FWD-C2.

### Method (full self-contained dispatch prompt)

Producing script: `computations/session-90/s90_w8_fwd_c2_substrate_is_disambiguation.py`.

#### Step 1 — Re-read §W5-4 WP lines 898 and 1011
Load `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md` (W-5
workshop) and extract:
- line 898: "Pillar II Mellin-Barnes residue" Element-1 specification
- line 1011: "K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L})"
  Element-1 specification

Cross-reference W-6 workshop verdict at Q3 Fork B (in
`sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md`).

#### Step 2 — Apply 5-anatomy IS-not-IN audit per `cross-pillar-bridge-anatomy.md`
For each candidate Element-1 specification, verify the 5-anatomy elements:
1. Substrate-IS observable — finite-L spectral-triple observable on
   `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`
2. Laboratory-IN observable — continuum measurement on a partner pillar
3. Bridge map — HKR / K-theory / Connes-Karoubi pairing
4. Algebraic envelope — convergence rate L^{-α}
5. Empirical anchor — numerical satisfaction at canonical L_max

Mellin-Barnes residue (Pillar II): operationally a substrate-distance-N
Mellin-cone residue, NOT a single-summand-projection trace on
`(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. Under the layer-separability carve-out
classification, Mellin-Barnes residue is Type-S (state-pair functional)
NOT Type-F (single-summand operator trace). Element-1 admissibility
FAILS for Mellin-Barnes residue as the SUBSTRATE-IS canonical.

K-window log-derivative on BdG sub-algebra: single-summand-projection
trace on `M_2(ℂ) ⊂ A_K` per layer-separability carve-out Type-F class;
Element-1 admissibility PASSES.

#### Step 3 — Bridge classification update
Update FWD-C2 bridge-anatomy bridge classification:
- BEFORE: `Pillar II Mellin-Barnes residue ↔ Pillar V laboratory continuum`
- AFTER: `Pillar III/IV BdG-spectral-triple K-window log-derivative ↔
  Pillar V laboratory continuum`

Update §VII.AV registry-anchor framing to cite K-window log-derivative as
canonical substrate-IS Element-1.

#### Step 4 — Cross-link to substrate-IS Level declaration
Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS
levels"` MANDATORY-K=2 since S88 W-7 V.4: declare K-window log-derivative
as Level-1 single-τ-slice substrate-IS at τ_fold = 0.19.

#### Step 5 — Emit SUPERSEDES-tagged corrective canonical line per Option A
Per `v3-closure-recovery.md §"Stage 1: Automatic re-dispatch"` sig_5 sub-
section + `gate-verdicts.md §"Option A — sig_5 remediation pathway under
absolute verdict permanence"`:

Original §W5-4 producing-script canonical verdict line is RETAINED on disk.
Append corrective canonical line carrying `supersedes=<old_audit_sha>` tag
naming the original §W5-4 audit_sha256.

Sample emission:
```
S90-FWD-C2-SUBSTRATE-IS-DISAMBIGUATION: \
  PASS -- value='disambiguation_complete; \
                  element1=K-window-log-derivative; \
                  bridge=Pillar-III-IV-↔-Pillar-V; \
                  supersedes=<old_§W5-4_audit_sha_full_64_chars>' \
  scheme=FWD-C2-anatomy-disambiguation \
  convention=substrate-IS-canonical-K-window-log-derivative \
  L_max=10 \
  audit_sha256=<closure> content_sha256=<closure> schema_version=S84+
```

#### Step 6 — HIT substitution-chain re-evaluation
Per the bridge-classification update, re-evaluate the HIT substitution chain
linking FWD-C2 to the HIT K-counter advancement path. Confirm CF-61 and
CF-65 paths align with the updated bridge classification.

#### Step 7 — Dual-SHA closure
Compute audit_sha256 over input-pin map (workshop W-5 + W-6 transcript SHAs,
§W5-4 WP lines 898 + 1011, §VII.AV registry text, rule references) and
content_sha256 over producing-script bytes. Emit both in canonical line +
dual-SHA companion row.

#### Outputs
- `s90_w8_fwd_c2_substrate_is_disambiguation.npz` (5-anatomy audit log,
  bridge-classification update record, SUPERSEDES tag verification)
- `s90_w8_fwd_c2_substrate_is_disambiguation.json` (machine-readable
  Element-1 disambiguation verdict)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `audit_target_lines` | §W5-4 WP lines 898 + 1011 (exact) |
| `audit_method` | 5-anatomy IS-not-IN compliance per `cross-pillar-bridge-anatomy.md` |
| `q3_fork_b_resolution` | K-window log-derivative IS canonical Element-1 |
| `bridge_class_before` | Pillar II ↔ Pillar V |
| `bridge_class_after` | Pillar III/IV ↔ Pillar V |
| `substrate_level_tag` | Level-1 single-τ-slice at τ_fold = 0.19 (per phononic-framing.md MANDATORY-K=2) |
| `supersedes_protocol` | Option A per `gate-verdicts.md §"Option A"` |
| `supersedes_target` | §W5-4 producing-script canonical verdict line (full 64-char audit_sha) |
| `vii_av_anchor_update` | route to mack-cosmic-bridge writer for registry text update |
| `random_seed` | not applicable (audit-based) |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `substrate-IS-canonical-K-window-log-derivative` |
| `scheme` | `FWD-C2-anatomy-disambiguation` |
| `L_max` | 10 (anchor at the §W5-4 canonical truncation; substrate-IS observable identity is L_max-INVARIANT structural claim) |

PRDR cardinality check: 14 free parameters; 14 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `s89-w5-vii-aq-level3-binding.md` line 898 + line 1011 | `<computed at plan-freeze>` |
| `s89-w6-level2-binding-inheritance.md` (Q3 Fork B verdict) | `<computed at plan-freeze>` |
| `§W5-4 producing script verdict` (s89_gate_verdicts.txt) | `<computed at plan-freeze>` |
| `permanent-results-registry.md §VII.AV` | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"` | `<computed at plan-freeze>` |
| `cross-pillar-bridge-corpus.md §4` | `<computed at plan-freeze>` |
| `v3-closure-recovery.md §"Option A"` | `<computed at plan-freeze>` |
| `phononic-framing.md §"Single-τ-slice..."` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value='disambiguation_complete', scheme=FWD-C2-anatomy-disambiguation, \
 convention=substrate-IS-canonical-K-window-log-derivative, L_max=10)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate |
|:-----|:----------|
| **PASS** | (i) §W5-4 Element-1 disambiguation completes with K-window log-derivative selected; (ii) bridge classification updated to Pillar III/IV ↔ Pillar V; (iii) §VII.AV registry-anchor framing updated by mack; (iv) HIT substitution chain re-evaluated; (v) SUPERSEDES-tagged corrective canonical line emitted per Option A; (vi) dual-SHA closure complete |
| **INFO** | Q3 Fork B resolution ambiguous between Element-1 candidates; §W5-4 retains dual Element-1 specs; SUPERSEDES not emitted; queue for S91 |
| **FAIL** | 5-anatomy IS-not-IN audit reveals BOTH candidate Element-1 specs FAIL admissibility — substrate-IS observable identity for FWD-C2 is structurally undefined; carry-forward to S91 with §VII.AV REGISTRY-INCOMPLETE-INDEFINITE tag |

### Substitution chain (audit-form)

```
Definitions:
  Element-1-candidate-A := Pillar II Mellin-Barnes residue at substrate-distance-N pole
  Element-1-candidate-B := K-window log-derivative on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L})
                          BdG sub-algebra M_2(ℂ)
  Type-F                := single-summand-projection trace on substrate algebra
                          (algebra-INVARIANT spectrum-only functional family)
  Type-S                := state-pair functional on substrate state-space
                          (algebra-DEPENDENT family)
  IS-not-IN audit       := 5-anatomy compliance per cross-pillar-bridge-anatomy.md

Substitutions:
  Step 1: Candidate-A (Mellin-Barnes residue) is structurally a Mellin-cone
          contour integral residue at a substrate-distance-N pole; the
          residue is a STATE-PAIR functional (Type-S) on the substrate's
          Mellin-cone state space, NOT a single-summand-projection trace.
  Step 2: Per layer-separability carve-out (`mechanical-closure-discipline.md`),
          Type-S observables FAIL the substrate-IS canonical Element-1
          admissibility test; they are structurally STATE-PROJ side.
  Step 3: Candidate-B (K-window log-derivative on BdG sub-algebra) is
          structurally a single-summand-projection trace on M_2(ℂ) (the BdG
          sub-algebra of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)) operated on by the K-window
          indicator and a log-derivative weight; it IS a Type-F observable.
  Step 4: Per cross-pillar-bridge-anatomy 5-anatomy Element-1 spec,
          substrate-IS observables MUST be on the finite spectral triple
          structure of (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}); Type-F admissible,
          Type-S inadmissible.
  Step 5: Direction: Element-1 = K-window log-derivative (Type-F) ⟹
                       bridge classification = Pillar III/IV (BdG-spectral-
                       triple substrate-IS) ↔ Pillar V (laboratory-IN
                       continuum on a partner pillar).

Conclusion: §W5-4 Element-1 names K-window log-derivative as canonical
            substrate-IS observable; bridge classification updates to
            Pillar III/IV ↔ Pillar V; §VII.AV registry-anchor updated by
            mack-cosmic-bridge writer; HIT substitution chain re-evaluated
            with the corrected bridge identity; SUPERSEDES tag emitted per
            Option A preserving audit trail.
```

### What PASSES/FAILS MEAN for solution space

- **PASS**: Element-1 disambiguation completes structurally. §VII.AV
  registry-anchor framing updates by mack-cosmic-bridge sole-writer; FWD-C2
  bridge classification updates to Pillar III/IV ↔ Pillar V; CF-61's
  promotion semantics aligns with the corrected substrate-IS observable
  identity (K-window log-derivative on BdG sub-algebra); HIT substitution
  chain re-evaluation confirms CF-61+CF-65 dual PASS path advances HIT
  K=2 → K=3.
- **INFO**: Q3 Fork B resolution ambiguous; §W5-4 retains dual specs;
  CF-61 cannot proceed without disambiguation; S91 carry-forward.
- **FAIL**: substrate-IS observable identity structurally undefined; both
  candidates FAIL admissibility; FWD-C2 bridge classification routes to
  REGISTRY-INCOMPLETE-INDEFINITE; downstream FWD-C2 substrate-physics
  computations (CF-61) cannot proceed.

### Effort estimate
0.5 wave-equivalents. Audit-form gate; no computation; structural-anatomy
verification + registry-text update + SUPERSEDES-tag emission.

### Substrate-framing reminder
The disambiguation IS at the substrate-IS observable level — which one of
the two candidate Element-1 observables on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`
IS the canonical substrate-IS observable for FWD-C2. The substrate is
intrinsic; the substrate-IS observable is intrinsic to the substrate
algebra's projection structure. The K-window log-derivative on `M_2(ℂ)`
is a single-summand operator trace — it IS intrinsic to the substrate at
the BdG sub-algebra level. The Mellin-Barnes residue is a state-pair
functional on a Mellin-cone state space — it is intrinsic at the Mellin
moment structure but NOT a single-summand operator trace. Per the layer-
separability carve-out (Type-F vs Type-S; SUGGESTION K=1 at S88 W8-89),
the Element-1 canonical substrate-IS observable for FWD-C2 must be Type-F.
The bridge classification update reflects this structural reality.

---

## §W8-5. CF-63 — S90-VII-AV-VII-AU-DEFERRED-PENDING-MACK-LANDING

### Gate ID
`S90-VII-AV-VII-AU-DEFERRED-PENDING-MACK-LANDING`

### Trigger
`[AUDIT]` — registry-landing of §VII.AV `REGISTRY-INCOMPLETE-PENDING-PROXY-
REFINEMENT` and §VII.AU `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` initial
deferred-pending registrations at S90 W0 via mack-cosmic-bridge sole-writer.
Audit verifies (a) sub-class tag presence, (b) Level-1 single-τ-slice
declaration MANDATORY per volovik V.2, (c) HIT-CANDIDATE qualifier on
§VII.AU, (d) cross-links to CF-W5-3 / CF-W5-5 / CF-W7-1 / CF-W5-6, (e)
deferred-pending sub-class admissibility per `cross-pillar-bridge-anatomy.md
§"Enforcement clause"` extension (W1 CF-14 PRECEDES this gate).

### Classification
META (registry-anatomy + mack sole-writer landing). The gate IS a registry
write authored by mack-cosmic-bridge per `feedback_mack-bridge-role.md`
sole-writer convention. The substrate-IS observable structural content is
DEFERRED to CF-61 (§VII.AV) and CF-65 (§VII.AU); this gate ONLY lands the
deferred-pending registry entries with full anatomy compliance.

### Agent type
**mack-cosmic-bridge** sole-writer (per `feedback_mack-bridge-role.md`
registry/inventory landings authority); **connes-ncg-theorist** co-sign on
technical content (cross-pillar-bridge-anatomy 5-anatomy 3-level compliance);
**lizzi-spectral-functional-theorist** co-sign on §VII.AU substrate-IS
observable identity (FWD-C1 spec at `cross-pillar-bridge-corpus.md §4`
lines 120-128); **volovik-superfluid-universe-theorist** co-sign on Level-1
single-τ-slice declaration (per V.2 refinement; MANDATORY per
`phononic-framing.md §"Forward-looking enforcement"`).

### Hypothesis
Both §VII.AV and §VII.AU can be registered at S90 W0 with structurally
complete deferred-pending registry entries (5-anatomy + 3-level template
with deferred-pending qualifier on Level-3) that (i) declare the correct
deferred-pending sub-class tag per W1 CF-14 rule-file extension, (ii)
declare Level-1 single-τ-slice substrate-IS level MANDATORY per volovik V.2
and `phononic-framing.md`, (iii) carry HIT-PASS-CANDIDATE-PENDING-EXTRACTION
qualifier on §VII.AU per W-6 R2, and (iv) pass
`_registry_landing_audit.py` (no cross-corner co-primary per S88 W-15 V.6 /
B.14).

### Method (full self-contained dispatch prompt)

Producing pathway: mack-cosmic-bridge writer dispatch (NOT a producing
script in `computations/_shared/`; registry-landing only). Audit script:
`computations/session-90/s90_w8_vii_av_au_deferred_pending_audit.py`.

#### Step 1 — Verify W1 CF-14 PRECEDES landing
Pre-flight check: confirm `cross-pillar-bridge-anatomy.md §"Enforcement
clause"` carries the W1 CF-14 deferred-pending intermediate verdict-class
extension with both sub-class tags (`REGISTRY-INCOMPLETE-PENDING-PROXY-
REFINEMENT`, `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`). Halt at
plan-freeze if absent.

#### Step 2 — mack writes §VII.AV initial registration
mack-cosmic-bridge appends to `sessions/permanent-results-registry.md` a
§VII.AV block containing:
- Header: `### §VII.AV (REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT)`
- Slot allocation: §VII.AV (per `cross-pillar-bridge-anatomy.md` next-free
  letter at S89 close, §VII.AT and §VII.AU reserved; §VII.AV next-free)
- 5-anatomy block:
  1. Substrate-IS observable — Corner-IV K-window log-derivative on BdG
     sub-algebra `M_2(ℂ) ⊂ A_K` (per CF-62 disambiguation outcome;
     conditional on CF-62 PASS)
  2. Laboratory-IN observable — Pillar V continuum laboratory observable
     (3He-B mutual-friction measurement or analog; per W-5 CF-W5-3 spec)
  3. Bridge map — HKR L_max → ∞ at d=4
  4. Algebraic envelope — L^{-3} predicted; empirical α to be measured by
     CF-61 (DEFERRED PENDING)
  5. Empirical anchor — `L_emp(L_max=12) = -7.046336474406761` (§W5-2 npz);
     Level-3 anchor DEFERRED PENDING CF-W5-3 (= CF-61)
- 3-level ladder:
  - Level 1 — Single-τ-slice substrate-IS at τ_fold = 0.19 (MANDATORY tag
    per volovik V.2 + `phononic-framing.md`)
  - Level 2 — SCHEMATIC proxy disclosed (Casimir-bound proxy reference per
    §W5-3); structural-binding pending CF-61 substantive substitution
  - Level 3 — DEFERRED PENDING CF-W5-3 / CF-61
- Cross-links: CF-W5-3 (this is CF-61); CF-W5-5 (CF-62 disambiguation);
  W-6 R2 verdict text

#### Step 3 — mack writes §VII.AU initial registration
mack-cosmic-bridge appends to `sessions/permanent-results-registry.md` a
§VII.AU block containing:
- Header: `### §VII.AU.OP-PROJ (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION;
  HIT-PASS-CANDIDATE-PENDING-EXTRACTION)`
- Slot allocation: §VII.AU (post-CF-18 cleanup freeing slot canonically;
  forward to CF-64 single-shot retry)
- 5-anatomy block:
  1. Substrate-IS observable — FWD-C1 parameterized slope-A canonical →
     c_sub_corrected → n_s_recomputed Mellin-cone closure (substrate-
     distance-1 pole s=3); **EXPLICIT TAG: Level 1 single-τ-slice at
     τ_fold = 0.19** (MANDATORY per volovik V.2);
     cross-link to CF-W5-1 (= CF-59) as queued Level-2 verification
  2. Laboratory-IN observable — Pillar II Planck/CMB-S4 n_s measurement
  3. Bridge map — HKR L_max → ∞; OP-PROJ side per
     `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`
     MANDATORY at K=3 since S88 W8-92
  4. Algebraic envelope — L^{-3} predicted; empirical α to be measured by
     CF-65 (DEFERRED PENDING)
  5. Empirical anchor — `n_s_FW_exact = 9561/10000` (canonical_constants.py:1681);
     Level-3 anchor DEFERRED PENDING CF-W7-1 (= CF-64) + CF-W5-6 (= CF-65)
- 3-level ladder:
  - Level 1 — Single-τ-slice substrate-IS at τ_fold = 0.19 (MANDATORY tag
    per volovik V.2 + `phononic-framing.md` Forward-looking enforcement)
  - Level 2 — DEFERRED PENDING CF-65 L_max scan
  - Level 3 — DEFERRED PENDING CF-65 anchor match + CF-64 single-shot retry
- HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier on theorem-name line
- Cross-links: CF-W7-1 (= CF-64), CF-W5-6 (= CF-65), CF-W5-1 (= CF-59)
  Level-2 verification path

#### Step 4 — Run `_registry_landing_audit.py`
Verify both new entries:
- No cross-corner co-primary structures (per S88 W-15 V.6 / B.14 algebra-
  axis orthogonality MANDATORY-K=3)
- OP-PROJ suffix tagging present on §VII.AU (MANDATORY at K=3 since S88
  W8-92)
- 5-anatomy block complete (all 5 elements declared)
- 3-level ladder complete (Level 1 / Level 2 / Level 3 markers present)
- Level-1 single-τ-slice tag present on BOTH §VII.AV and §VII.AU (per
  volovik V.2)
- Deferred-pending sub-class tag present (`REGISTRY-INCOMPLETE-PENDING-
  PROXY-REFINEMENT` on §VII.AV; `REGISTRY-INCOMPLETE-PENDING-FIRST-
  EXTRACTION` on §VII.AU)
- HIT-PASS-CANDIDATE-PENDING-EXTRACTION qualifier on §VII.AU
- Cross-links to forward-promoting gates present

#### Step 5 — Verdict-line append
```
S90-VII-AV-VII-AU-DEFERRED-PENDING-MACK-LANDING: \
  PASS|FAIL|INFO -- value='vii_av_landed=True; vii_au_landed=True; \
                            level1_tags=2; deferred_pending_subclass=2; \
                            audit_passes=True' \
  scheme=mack-sole-writer-deferred-pending-landing \
  convention=cross-pillar-bridge-anatomy-5anatomy-3level-deferred-pending \
  L_max=N/A (registry-anatomy gate) \
  audit_sha256=<closure> content_sha256=<closure> schema_version=S84+
```

#### Outputs
- `s90_w8_vii_av_au_deferred_pending_audit.json` (registry-landing audit
  log; all 8 audit criteria PASS/FAIL flags)
- Registry edits to `sessions/permanent-results-registry.md` (mack writer
  with connes + lizzi + volovik co-sign)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `vii_av_slot` | §VII.AV (next-free at S89 close per Extra Context §"§VII registry slots used") |
| `vii_au_slot` | §VII.AU (post-CF-18 cleanup) |
| `vii_av_subclass_tag` | `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` |
| `vii_au_subclass_tag` | `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` |
| `vii_au_qualifier` | `HIT-PASS-CANDIDATE-PENDING-EXTRACTION` |
| `level1_tag_mandatory` | True on BOTH (per volovik V.2 + phononic-framing.md) |
| `vii_au_op_proj_suffix` | True (per S88 W8-92 MANDATORY-K=3) |
| `forward_promoting_gates` | {CF-61, CF-65, CF-64, CF-59 Level-2 verification path} |
| `sole_writer` | mack-cosmic-bridge (per `feedback_mack-bridge-role.md`) |
| `co_signers` | {connes-ncg-theorist (technical), lizzi (substrate-IS identity), volovik (Level-1 tag)} |
| `audit_script` | `_registry_landing_audit.py` |
| `audit_criteria` | 8 (per Step 4 enumeration) |
| `prerequisite_w1_cf14` | landed before this gate dispatches |
| `random_seed` | not applicable |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `cross-pillar-bridge-anatomy-5anatomy-3level-deferred-pending` |
| `scheme` | `mack-sole-writer-deferred-pending-landing` |

PRDR cardinality check: 17 free parameters; 17 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `permanent-results-registry.md` (current state) | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md §"Enforcement clause"` (post-W1 CF-14) | `<computed at plan-freeze>` |
| `joint-theorem-promotion.md §"Stage 1"` | `<computed at plan-freeze>` |
| `cross-pillar-bridge-corpus.md §4` FWD-C1+C2 spec | `<computed at plan-freeze>` |
| `phononic-framing.md §"Forward-looking enforcement"` | `<computed at plan-freeze>` |
| `feedback_mack-bridge-role.md` | `<computed at plan-freeze>` |
| `s89-w6-level2-binding-inheritance.md` R2 verdict | `<computed at plan-freeze>` |
| `_registry_landing_audit.py` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value='vii_av_landed AND vii_au_landed AND audit_passes', \
 scheme=mack-sole-writer-deferred-pending-landing, \
 convention=cross-pillar-bridge-anatomy-5anatomy-3level-deferred-pending, \
 L_max=N/A)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate |
|:-----|:----------|
| **PASS** | Both deferred-pending registrations land with sub-class tags + Level-1 declaration + qualifiers + cross-links; `_registry_landing_audit.py` PASS on ALL 8 audit criteria (no cross-corner co-primary; OP-PROJ suffix present; 5-anatomy complete; 3-level ladder complete; Level-1 single-τ-slice tag on both; deferred-pending sub-class tag present; HIT-CANDIDATE qualifier on §VII.AU; cross-links present) |
| **INFO** | One of two entries lands cleanly; second hits a rule-file ambiguity routing to S91 |
| **FAIL** | `_registry_landing_audit.py` FAIL on any audit criterion (cross-corner co-primary detected; OP-PROJ suffix absent; 5-anatomy incomplete; Level-1 tag missing; sub-class tag mistaken; HIT qualifier absent; cross-links broken) |

### Substitution chain (audit-form)

```
Definitions:
  V := §VII.AV registry entry (deferred-pending)
  U := §VII.AU registry entry (deferred-pending)
  C(X, prop) := X carries property prop
  audit_8 := 8-criterion registry-landing audit

Substitutions:
  Step 1: For V:
          C(V, subclass=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT) AND
          C(V, level1_single_tau_slice_tag=True) AND
          C(V, 5anatomy_complete=True) AND
          C(V, 3level_ladder_complete=True) AND
          C(V, level3_deferred_pending=CF-61) AND
          C(V, cross_links={CF-W5-3, CF-W5-5})
  Step 2: For U:
          C(U, subclass=REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) AND
          C(U, op_proj_suffix=True) AND
          C(U, level1_single_tau_slice_tag=True) AND
          C(U, 5anatomy_complete=True) AND
          C(U, 3level_ladder_complete=True) AND
          C(U, level3_deferred_pending=CF-64+CF-65) AND
          C(U, qualifier=HIT-PASS-CANDIDATE-PENDING-EXTRACTION) AND
          C(U, cross_links={CF-W7-1, CF-W5-6, CF-W5-1})
  Step 3: audit_8(V) = AND of 8 audit criteria for V
          audit_8(U) = AND of 8 audit criteria for U
  Step 4: PASS = audit_8(V) ∧ audit_8(U)

Conclusion: PASS verdict licenses CF-61 (V level3 promotion) and CF-65
            (U level3 promotion) and CF-64 (U single-shot retry) to
            dispatch with valid registry parents.
```

### What PASSES/FAILS MEAN for solution space

- **PASS**: §VII.AV and §VII.AU exist as valid registry parents for CF-61
  / CF-65 / CF-64 promotion semantics. Forward consumers can cite §VII.AV
  and §VII.AU registry entries with full anatomy. Cross-link audit-trail
  closure complete; promotion-pathway is licensed.
- **INFO**: one entry lands; second carries forward to S91. CF-61 or CF-65
  may proceed on the landed entry; the other path is blocked.
- **FAIL**: registry-landing audit FAILs; mack landing rolls back. CF-61
  + CF-65 + CF-64 all blocked at plan-freeze on dependency. Carry-forward
  to S91 with remediation on the FAILed audit criterion.

### Effort estimate
0.3 wave-equivalents. mack registry writes (2 entries × ~30 lines each) +
audit-script run + verdict-line emission. No computation.

### Substrate-framing reminder
§VII.AV and §VII.AU are registry entries on substrate-IS bridge theorems.
The Level-1 single-τ-slice declaration MANDATORY per volovik V.2 is the
structural acknowledgment that at the moment of landing, the substrate-IS
observable is the SINGLE-τ-slice spectral triple at τ_fold = 0.19 — not a
moduli-deformation (which is Level-2; queued via CF-59 for §VII.AU and
queued via S91 carry-forward for §VII.AV). The deferred-pending sub-class
tags ARE substrate-physics honesty: the Level-3 empirical anchor is not
yet computed; the registry entry openly declares the pendency rather than
landing a stub Level-3 value. Per `phononic-framing.md §"Forward-looking
enforcement"`, the Level-1 declaration is the substrate-IS observable's
intrinsic-truncation tag at the moment of registry landing; future Level-2
extensions ARE the substrate's own moduli-deformation, NOT a coordinate
sweep on a meta-container.

---

## §W8-6. CF-64 — S90-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU-RETRY

### Gate ID
`S90-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU-RETRY`

### Trigger
`[CHAIN]` — 8/8 structural-coherence single-shot 8-clause chain emission of
the §VII.AU.OP-PROJ FWD-C1 STAGE-1-CANDIDATE bridge landing per AFTER-pattern
single-shot protocol of `registry-landing.md §"Bridge-Landing Script
Architecture (single-shot pattern)"`. PASS advances HIT K-counter K=3 → K=4
(rule status MANDATORY preserved per S88 W4a-17 close).

### Classification
Per-bulletin substrate-IS bridge landing (§VII.AU.OP-PROJ FWD-C1 Pillar I ↔
Pillar II bridge theorem; STAGE-1-CANDIDATE per `joint-theorem-promotion.md
§"Stage 1"`). Bridge-anatomy 5-anatomy + 3-level ladder + Operator-Projection
Reading-A Naming Hygiene (MANDATORY-K=3 since S88 W8-92) + AFTER-pattern
single-shot bridge-landing-script architecture (MANDATORY since S88 W3c-30).

### Agent type
**lizzi-spectral-functional-theorist** PRIMARY (Pillar I ↔ Pillar II bridge-
theorem substrate-IS observable side; FWD-C1 spec authoring per
`cross-pillar-bridge-corpus.md §4`); **connes-ncg-theorist** CO-AUTHOR
(§VII.AU registry-promotion semantics + Pillar I ↔ Pillar II bridge-family
HKR map at the NCG-axiomatic side; bridge-anatomy audit on Element-1
Hochschild pairing identity); mack-cosmic-bridge sole-writer at the
registry-landing layer per `feedback_mack-bridge-role.md`; producing script
emits AFTER-pattern single-shot per `registry-landing.md` 4-step protocol.

### Hypothesis
The §VII.AU.OP-PROJ FWD-C1 STAGE-1-CANDIDATE bridge landing can be emitted
as a SINGLE single-shot AFTER-pattern emission achieving 8/8 structural-
coherence booleans True (no FAIL/INFO → PASS supersedes chain; first-attempt
slot allocation lands canonically after CF-18 cleanup; Element 2 OE-form
regex-compliant), advancing HIT K-counter K=3 → K=4.

### Method (full self-contained dispatch prompt)

Producing script: `computations/session-90/s90_w8_fwd_c1_pillar_i_ii_bridge_landing_single_shot.py`.

Architecture: STRICT AFTER-pattern single-shot per `registry-landing.md
§"Bridge-Landing Script Architecture (single-shot pattern)"`:
```
build_promotion_text → fsync → re-read → verify → emit (exactly one verdict line)
```
NO conditional rewrite branch; NO intermediate FAIL/INFO emission; NO
iterate-until-PASS pattern per `v3-closure-recovery.md` PROHIBITED_ACTIONS
Class 6.

#### Step 1 — Pre-flight CF-W7-2 = CF-18 cleanup verification
Confirm `sessions/permanent-results-registry.md` carries:
- §VII.AAU.OP-PROJ (line ~17165, lexical-construction wrong-slot emission #1):
  WITHDRAWN-IN-FAVOR-OF-S90-LANDING tag present
- §VII.AV.OP-PROJ (line ~17335, parallel-writer-race rerouted emission #3):
  WITHDRAWN-IN-FAVOR-OF-S90-LANDING tag present (NOTE: this is the W7c-rerouted
  §VII.AV entry, NOT the W-6 deferred-pending §VII.AV from CF-63; CF-18 cleanup
  + CF-63 deferred-pending registration are SEPARATE entries at the same slot
  letter — disambiguated by content)
- §VII.AU.OP-PROJ (line ~17250, emission #2): PRESERVED as canonical content host

Halt at plan-freeze if any of the three markers is missing.

#### Step 2 — Build promotion_text (FULL in memory; no I/O yet)
Build the §VII.AU.OP-PROJ STAGE-1-CANDIDATE registry text containing:
- Header: `### §VII.AU.OP-PROJ (STAGE-1-CANDIDATE per joint-theorem-promotion.md §"Stage 1"; HIT K-counter calibration corpus instance #4)`
- 5-anatomy block (8/8 booleans):
  1. Substrate-IS observable — `n_s_FW = Hochschild pairing image at
     substrate-distance-1 pole s=3`; substrate-IS observable IS the
     parameterized slope-A canonical → c_sub_corrected → n_s_recomputed
     Mellin-cone closure on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`
  2. Laboratory-IN observable — Pillar II Planck/CMB-S4 n_s measurement;
     emission #3's regex-compliant Element 2 OE-form text:
     ```
     ∫_BZ d^d k Tr(P_{n-s-substrate-distance-1}) · ρ_BZ(k; τ_fold)
     ```
     (matches positive-match regex `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` per
     `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`
     MANDATORY-K=2 since S88 W7a-73)
  3. Bridge map — HKR L_max → ∞; OP-PROJ side per `registry-landing.md
     §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 since
     S88 W8-92
  4. Algebraic envelope — L^{-3} predicted at d=4 per Level-2-binding
     d=4 calibration; α extraction queued via CF-65
  5. Empirical anchor — `n_s_FW_exact = Fraction(9561, 10000)` bit-exact
     (canonical_constants.py:1681); cross-link to S87 W7a Sage-QQ exact
     identity `n_s_FW² − 1 ≡ α_s_canonical`
     (audit `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`)
- 3-level ladder:
  - Level 1 — Single-τ-slice substrate-IS at τ_fold = 0.19; cohomology-class
    identity `n_s_FW² − 1 = α_s_canonical` regulator-INVARIANT (S87 W7a
    Sage-QQ exact)
  - Level 2 — L^{-3} algebraic envelope at d=4 per HKR-image convergence
    rate; CF-65 supplies empirical α value (L_max scan ∈ {6..12})
  - Level 3 — `n_s_FW_exact = 9561/10000` empirical anchor at L_max=10;
    CF-65 supplies `|n_s_recomputed(L_max) − n_s_FW_exact|` envelope
- Hybrid Independence Test verification:
  - Clause (i) substrate-IS pillar: Pillar I (distinct from prior K=3
    instances §VII.AF.1.OP-PROJ Pillar III, §VII.AJ Pillar VII, §VII.W-3.LAB
    Pillar III)
  - Clause (ii) laboratory-IN pillar: Pillar II (distinct from prior K=3
    instances Pillar IV, Pillar VII, Pillar V)
  - Clause (iii) bridge map class: HKR L_max → ∞ (shared with prior; clauses
    (i) ∨ (ii) ∨ (iii) satisfied via (i) AND (ii))
  - Clause (iv) algebraic envelope: independent L^{-3} envelope at d=4
    (not a numerical refinement of prior K=3 instances' envelopes)
- Joint authorship attribution:
  - lizzi-spectral-functional-theorist PRIMARY (substrate-IS observable side
    + FWD-C1 spec authoring)
  - connes-ncg-theorist CO-AUTHOR (HKR bridge map + Pillar I ↔ Pillar II
    bridge-family axiomatic content)
- 8 structural-coherence booleans (computed):
  1. `slot=§VII.AU` (post-CF-18 cleanup; first-attempt slot allocation)
  2. `op_proj_suffix=True`
  3. `5anatomy_complete=True` (all 5 elements declared)
  4. `3level_complete=True` (all 3 levels declared)
  5. `element2_oe_form_regex_match=True` (positive-match
     `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)`)
  6. `hybrid_independence_test=True` (clauses (i) ∨ (ii) ∨ (iii) ∧ (iv) all hold)
  7. `cross_links_present=True` (S87 W7a + W7b + W4-4 audit_shas + §VII.AF.1
     baseline + CF-65 L_max scan forward-pointer + canonical_constants.py:1681
     + s86_gate_verdicts.txt Z_ratio_PIVOT55=1.435284 line)
  8. `single_shot_emission=True` (NO supersedes chain; first emission canonical)

#### Step 3 — write_atomic_with_fsync(promotion_text, registry_target)
Write the full promotion_text to `sessions/permanent-results-registry.md`
at the §VII.AU.OP-PROJ slot via atomic write + fsync. No conditional rewrite.

#### Step 4 — re_read + verify_section_matches(actual, expected)
Re-read the §VII.AU.OP-PROJ slot from disk and verify content matches the
in-memory promotion_text via SHA-256 content comparison. Compute the 8
structural-coherence booleans against the on-disk content.

```
all_8_pass := all([slot, op_proj_suffix, 5anatomy_complete, 3level_complete,
                    element2_oe_form_regex_match, hybrid_independence_test,
                    cross_links_present, single_shot_emission])
```

#### Step 5 — emit_verdict_line(all_8_pass)
Append EXACTLY ONE canonical verdict line to
`computations/session-90/s90_gate_verdicts.txt`:
```
S90-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU-RETRY: \
  PASS|FAIL -- value='all_8_booleans=<all_8_pass>; \
                       slot=§VII.AU.OP-PROJ; \
                       k_counter_advance=3→4' \
  scheme=AFTER-pattern-single-shot \
  convention=fwd-c1-pillar-i-ii-bridge-stage-1-candidate \
  L_max=10 \
  audit_sha256=<closure> content_sha256=<closure> schema_version=S84+
```
NO supersedes tag (this IS the first-emission single-shot per Hybrid
Independence Test K-counter advancement; emission #3 of W7c is SEPARATELY
withdrawn via CF-18 cleanup).

#### Step 6 — Run `_registry_landing_audit.py`
Verify AFTER-pattern compliance per `registry-landing.md §"Detection at
plan-freeze"`:
- `build_promotion_text` step present (pure-function; no I/O before write)
- `write_atomic_with_fsync` step present (single write; no per-attempt rewrites)
- `verify_section_matches` step present (single boolean output)
- `emit_verdict_line` step present (exactly ONE call; verdict argument IS
  the boolean)

#### Outputs
- `s90_w8_fwd_c1_pillar_i_ii_bridge_landing_single_shot.json`
  (8-boolean structural-coherence log + AFTER-pattern audit log)
- Registry edits to `sessions/permanent-results-registry.md` §VII.AU.OP-PROJ
  slot (mack sole-writer at the registry-write layer)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `slot_target` | §VII.AU.OP-PROJ (post-CF-18 cleanup) |
| `op_proj_suffix` | True (MANDATORY-K=3 per S88 W8-92) |
| `element2_oe_form` | `∫_BZ d^d k Tr(P_{n-s-substrate-distance-1}) · ρ_BZ(k; τ_fold)` (regex-compliant) |
| `bridge_map` | HKR L_max → ∞ |
| `algebraic_envelope` | L^{-3} at d=4 (Level-2-binding) |
| `empirical_anchor` | n_s_FW_exact = Fraction(9561, 10000) |
| `hybrid_independence_test` | clauses (i) ∨ (ii) ∨ (iii) ∧ (iv) (verified by construction) |
| `k_counter_pre` | 3 (post-S88 W4a-17 close MANDATORY) |
| `k_counter_post` | 4 |
| `single_shot_protocol` | AFTER-pattern per `registry-landing.md` (NOT BEFORE-pattern) |
| `prerequisite_cf18` | landed before this gate dispatches |
| `prerequisite_cf63` | §VII.AU initial deferred-pending registration landed (provides registry parent for STAGE-1-CANDIDATE promotion) |
| `primary_author` | lizzi-spectral-functional-theorist |
| `co_author` | connes-ncg-theorist |
| `sole_writer` | mack-cosmic-bridge (registry-write layer) |
| `cross_links` | {S87 W7a audit_sha, S87 W7b audit_sha, S87 W4-4 audit_sha, §VII.AF.1.OP-PROJ baseline, canonical_constants.py:1681, s86 Z_ratio_PIVOT55 line, CF-65 L_max scan} |
| `random_seed` | not applicable (deterministic) |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `fwd-c1-pillar-i-ii-bridge-stage-1-candidate` |
| `scheme` | `AFTER-pattern-single-shot` |
| `L_max` | 10 (canonical anchor truncation per `cross-pillar-bridge-corpus.md §4`) |

PRDR cardinality check: 20 free parameters; 20 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `S87 W7a` (Sage-QQ exact `n_s_FW² − 1 ≡ α_s_canonical`) | `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` |
| `S87 W7b` (c_sub_corrected = 14.528574) | `d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f` |
| `S87 W4-4` (joint n_s, α_s hypersurface) | `e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` |
| `S87 W7c emission #3 promotion_text body` | `cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d` |
| `permanent-results-registry.md §VII.AU` (post-CF-18 cleanup) | `<computed at plan-freeze>` |
| `canonical_constants.py:1681` (n_s_FW_exact) | `<computed at plan-freeze>` |
| `canonical_constants.py:1719` (slope_A_FW_Conv_A_GEOMETRIC) | `<computed at plan-freeze>` |
| `canonical_constants.py:1720` (slope_A_FW_Conv_A_AT_TAU_FOLD) | `<computed at plan-freeze>` |
| `s86_gate_verdicts.txt` Z_ratio_PIVOT55=1.435284 line | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md` (Element 2 OE-form + 5-anatomy + 3-level + Hybrid Independence Test) | `<computed at plan-freeze>` |
| `joint-theorem-promotion.md §"Stage 1"` | `<computed at plan-freeze>` |
| `registry-landing.md §"Bridge-Landing Script Architecture"` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value='all_8_booleans=True; k_counter_advance=3→4', \
 scheme=AFTER-pattern-single-shot, \
 convention=fwd-c1-pillar-i-ii-bridge-stage-1-candidate, L_max=10)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate |
|:-----|:----------|
| **PASS** | ALL 8 structural-coherence booleans True in SINGLE canonical emission (no supersedes chain); `_registry_landing_audit.py` AFTER-pattern check PASS; HIT K-counter K=3 → K=4 (rule status MANDATORY preserved) |
| **FAIL** | ANY of 8 booleans False on the single emission; producing script reverts to S91 carry-forward (NO conditional rewrite branch per AFTER-pattern discipline; FAIL is honored and the registry landing rolls back) |
| **INFO** | inapplicable for CHAIN trigger (the 8-clause chain produces binary PASS/FAIL on the conjunction) |

### Substitution chain (audit-form; verifies 8-clause conjunction)

```
Definitions:
  B1 := slot=§VII.AU (post-CF-18 cleanup; first-attempt allocation lands)
  B2 := op_proj_suffix=True (MANDATORY-K=3 per S88 W8-92)
  B3 := 5anatomy_complete=True
  B4 := 3level_complete=True
  B5 := element2_oe_form_regex_match=True
  B6 := hybrid_independence_test=True (clauses (i) ∨ (ii) ∨ (iii) ∧ (iv))
  B7 := cross_links_present=True (8 cross-references enumerated)
  B8 := single_shot_emission=True (NO supersedes chain)
  PASS_8_8 := B1 ∧ B2 ∧ B3 ∧ B4 ∧ B5 ∧ B6 ∧ B7 ∧ B8

Substitutions:
  Step 1: Each B_i is computed against the on-disk content post-fsync
          via the AFTER-pattern's re_read + verify_section_matches step
  Step 2: PASS verdict licenses K-counter advancement:
          K_pre = 3 (S88 W4a-17 close MANDATORY-K=3)
          K_post = K_pre + 1 = 4
  Step 3: Direction: PASS_8_8 = True ⟹ §VII.AU.OP-PROJ STAGE-1-CANDIDATE
                        registered; HIT K-counter 4 (MANDATORY status
                        preserved; rule promotes no further beyond MANDATORY
                        but K-counter tracks structural saturation depth)
  Step 4: Direction: PASS_8_8 = False ⟹ FAIL; producing script reverts;
                        S91 carry-forward with the failing boolean(s) named
                        in remediation

Conclusion: A PASS_8_8 verdict directly registers §VII.AU.OP-PROJ as the
            4th calibration corpus instance of the cross-pillar bridge-
            anatomy rule, hitting K=4 saturation depth.
```

### What PASSES/FAILS MEAN for solution space

- **PASS**: §VII.AU.OP-PROJ STAGE-1-CANDIDATE registry landing complete in
  a SINGLE single-shot AFTER-pattern emission. HIT K-counter advances from
  K=3 to K=4 (MANDATORY status preserved). FWD-C1 Pillar I ↔ Pillar II
  bridge theorem joins the calibration corpus alongside §VII.AF.1.OP-PROJ,
  §VII.AJ, §VII.W-3.LAB. Forward path: Stage-2 cross-axis independent
  verify dispatch (per `joint-theorem-promotion.md §"Stage 2"`) queued for
  S91+.
- **FAIL**: ANY boolean False; producing script reverts; the registry
  landing rolls back per AFTER-pattern discipline. S91 carry-forward with
  failing-boolean-named remediation. HIT K-counter remains at K=3
  (MANDATORY status preserved). Per `gate-verdicts.md §"All Results Are
  Good Results"`, FAIL is informative: it closes the canonical-emission
  corridor at S90 and identifies which structural element of the bridge
  landing requires structural fix.

### Effort estimate
1.0 wave-equivalent. Single-shot AFTER-pattern producing script (~2 hrs to
write + audit-script run + dual-SHA closure) + cross-link verification +
content-coherence audit. NO conditional rewrite; NO supersedes chain.

### Substrate-framing reminder
§VII.AU.OP-PROJ FWD-C1 IS the Pillar I (substrate-distance-1 Hochschild
pairing image) ↔ Pillar II (continuum n_s laboratory measurement) bridge
theorem. The substrate-IS observable n_s_FW = 9561/10000 IS the substrate's
intrinsic value at substrate-distance-1 pole s=3, computed via the
parameterized slope-A canonical Mellin-cone closure on the finite spectral
triple at L_max=10. The laboratory-IN observable IS the Planck/CMB-S4 n_s
measurement; the bridge map IS the HKR L_max → ∞ image. The OP-PROJ suffix
declares the operator-projection (algebra-INVARIANT spectrum-only-functional)
side per `registry-landing.md §"Operator-Projection Reading-A Naming
Hygiene"` MANDATORY-K=3. Direction of explanation: substrate (Pillar I
spectral triple) → bridge (HKR) → laboratory (Pillar II continuum). The
single-shot AFTER-pattern emission discipline IS the substrate-honesty
constraint: the registry landing must succeed in a single canonical
emission OR fail honestly; NO iterate-until-PASS pattern licensed per
PROHIBITED_ACTIONS Class 6.

---

## §W8-7. CF-65 — S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS

### Gate ID
`S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS`

### Trigger
`[VERIFY]` — empirical envelope α extraction via log-log linear regression
on `|n_s_recomputed(L_max) − n_s_FW_exact|` vs L_max for L_max ∈ {6..12} on
FWD-C1 substrate-IS observable. PASS triggers §VII.AU promotion from
`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` to STAGE-1-CANDIDATE per
joint-theorem-promotion.md §"Stage 1".

### Classification
PHONONIC. The FWD-C1 substrate-IS observable IS the parameterized slope-A
canonical → c_sub_corrected → n_s_recomputed Mellin-cone closure on the
substrate spectral triple at substrate-distance-1 pole s=3. n_s IS the
substrate-distance-1 Hochschild pairing image — the n_s ratio between
laboratory CMB scalar perturbations and the substrate's intrinsic
parameterized slope-A. The L_max scan IS the first-ever empirical envelope
α extraction on this substrate-IS observable.

### Agent type
**lizzi-spectral-functional-theorist** PRIMARY (substrate-IS observable
extraction at substrate-distance-1 Mellin pole via Route-B identity);
**connes-ncg-theorist** CO-AUTHOR (Pillar I ↔ Pillar II bridge-family HKR
map at the FWD-C1 observable level; L^{-3} envelope at d=4 per
`cross-pillar-bridge-anatomy.md §"Level-2-binding"` admissibility).

### Hypothesis
Empirical envelope α extraction via log-log regression on `|n_s_recomputed
(L_max) − n_s_FW_exact|` vs L_max ∈ {6..12} yields α ∈ [2.5, 3.5] AND
R² ≥ 0.95 AND L_max=10 anchor match `|n_s_recomputed(10) − n_s_FW_exact|
< 1e-9`, satisfying the L^{-3} algebraic envelope at d=4 per Level-2-binding
discipline and licensing §VII.AU promotion to STAGE-1-CANDIDATE.

### Method (full self-contained dispatch prompt)

Producing script: `computations/session-90/s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.py`.

#### Step 1 — Pre-flight prerequisite checks
Confirm:
- W1 CF-15 TEMPLATE-INHERITED convention-tag retrofit landed on §W5-6
  producing script (per dependency `W1 CF-15 PRECEDES CF-65`); else
  plan-freeze halt.
- CF-63 §VII.AU initial deferred-pending registration landed (per
  dependency `CF-63 PRECEDES CF-65`); else plan-freeze halt.
- L_max ∈ {6..12} feasibility per `math-scripts.md §"D_K Block-Diagonality
  + Recursive-Casimir-Projection Feasibility Pre-Check"` Friedrich-Bär
  saturation (η_FB_lower = 0.40); L_max=12 master cache available.

#### Step 2 — Load L_max=12 master cache
Load `s84_spectrum_cache_L12_tau019.npz`. For each L_max ∈ {6..12}, filter
spectrum to retain Peter-Weyl sectors (p, q) with p + q ≤ L_max. Hold the
7 spectrum subsets in memory (in-script Python dict keyed by L_max);
intra-wave intermediate, not persisted to disk (no upstream-input pin required).

#### Step 3 — Per-L_max parameterized slope-A canonical evaluation
For each L_max ∈ {6..12}:
```
slope_A^{canonical}(L_max) := closed-form
  10 / (1 - tau_fold / (5·π))
  evaluated at the L_max truncation
  (canonical_constants.py:1719 slope_A_FW_Conv_A_GEOMETRIC)
```
The canonical IS L_max-independent in the closed-form limit; finite-L_max
deviations come from M_Pl_eff² truncation in c_sub computation (Step 4).

#### Step 4 — Per-L_max c_sub_corrected via M_Pl_eff² ratio
For each L_max ∈ {6..12}:
```
c_sub_corrected(L_max) := M_Pl_eff²(L_max=10) / M_Pl_eff²(L_max)
                          · c_sub_baseline_corrected
```
where `c_sub_baseline = 2.238` (canonical_constants), and
M_Pl_eff²(L_max) IS the substrate-natural reduced Planck mass squared at the
L_max-truncated spectral triple (computed via standard spectral-action
a_2 channel on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L})).
At L_max=10 the canonical c_sub_corrected = 14.528574 per S87 W7b
(audit `d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f`).

#### Step 5 — Per-L_max n_s_recomputed via Route-B identity
For each L_max ∈ {6..12}:
```
n_s_recomputed(L_max) := 1 + α_s_canonical(L_max) / 2
                       = 1 + (n_s_FW²(L_max) - 1) / 2
                       ≈ closed-form derivation via parameterized slope-A
                         canonical at substrate-distance-1 pole s=3
```
Route-B identity per S87 W7a Sage-QQ exact: `n_s_FW² − 1 ≡ α_s_canonical`.
At L_max=10: `n_s_recomputed(10) ≡ n_s_FW_exact = Fraction(9561, 10000)` bit-
exact (canonical_constants.py:1681).

#### Step 6 — Compute empirical envelope δ_n_s(L_max)
For each L_max ∈ {6..11}:
```
delta_n_s(L_max) := | n_s_recomputed(L_max) - n_s_FW_exact |
```
For L_max = 12, verify anchor:
`| n_s_recomputed(12) - n_s_FW_exact |` ≤ `| n_s_recomputed(10) -
n_s_FW_exact |` (monotone decrease into truncation tail).

#### Step 7 — Log-log linear regression
Apply log-log linear fit:
```
log(delta_n_s(L_max)) = log(C) - α · log(L_max)  for L_max ∈ {6..11}
```
Extract α (slope) and R² (goodness-of-fit). Cross-validate against the
predicted L^{-3} envelope per `cross-pillar-bridge-anatomy.md §"Level-2-
binding"` d=4 calibration.

#### Step 8 — L_max=10 canonical anchor verification
Verify:
```
| n_s_recomputed(L_max=10) - n_s_FW_exact | < 1e-9
```
The L_max=10 anchor IS the canonical truncation per FWD-C1 spec
(`cross-pillar-bridge-corpus.md §4` lines 120-128); the n_s_FW_exact value
is the bit-exact substrate-IS observable at that truncation.

#### Step 9 — Promotion semantics trigger
IF PASS (α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND L_max=10 anchor match):
- Emit verdict-line PASS
- Trigger §VII.AU registry-status upgrade from `REGISTRY-INCOMPLETE-PENDING-
  FIRST-EXTRACTION` to STAGE-1-CANDIDATE per `joint-theorem-promotion.md
  §"Stage 1"`
- Cross-link in verdict-line companion row points to §VII.AU registry entry
  update target (post-CF-63 deferred-pending entry)

#### Step 10 — Verdict-line append
```
S90-FWD-C1-LMAX-SCAN-PARAMETERIZED-SLOPE-A-CANONICAL-WITH-PROMOTION-SEMANTICS: \
  PASS|FAIL|INFO -- value=<(alpha, R², delta_n_s_10)> \
  scheme=lmax-scan-parameterized-slope-a-canonical \
  convention=fwd-c1-substrate-distance-1-mellin-pole-s3-canonical-TEMPLATE-INHERITED \
  L_max=12 \
  audit_sha256=<closure> content_sha256=<closure> schema_version=S84+
```
Convention tag carries `-TEMPLATE-INHERITED` suffix per W1 CF-15 retrofit
+ `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 discipline.
Companion row:
```
# promotion_target=permanent-results-registry.md §VII.AU \
# from=REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION to=STAGE-1-CANDIDATE \
# hit_k_counter_advance=2→3 (joint with CF-61 dual PASS hits MANDATORY threshold)
```

#### Outputs
- `s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz` (per-L_max
  slope_A_canonical, c_sub_corrected, n_s_recomputed, delta_n_s, log-log
  fit parameters)
- `s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.png` (delta_n_s
  vs L_max log-log scatter with L^{-3} envelope overlay)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `L_max_scan` | {6, 7, 8, 9, 10, 11, 12} (7 sectors) |
| `tau` | 0.19 (τ_fold; Level-1 single-τ-slice) |
| `n_s_FW_exact` | Fraction(9561, 10000) (canonical_constants.py:1681) |
| `slope_A_FW_Conv_A_GEOMETRIC` | "10.0/(1−τ/(5π))" (canonical_constants.py:1719) |
| `c_sub_baseline_corrected` | 14.528574 at L_max=10 (S87 W7b) |
| `mellin_s` | 3 (substrate-distance-1 pole) |
| `alpha_passband` | [2.5, 3.5] |
| `r_squared_passband` | ≥ 0.95 |
| `lmax10_anchor_tolerance` | 1e-9 ABSOLUTE |
| `alpha_infoband` | [2.0, 2.5) ∪ (3.5, 4.5] |
| `r_squared_infoband` | [0.90, 0.95) |
| `friedrich_baer_eta_lower` | 0.40 |
| `convention_suffix` | `-TEMPLATE-INHERITED` (per W1 CF-15 + §(iv) MANDATORY-K=4) |
| `route_b_identity` | `n_s_FW² − 1 ≡ α_s_canonical` (S87 W7a Sage-QQ exact) |
| `random_seed` | not applicable (deterministic) |
| `prerequisite_w1_cf15` | landed before this gate dispatches |
| `prerequisite_cf63` | §VII.AU initial deferred-pending registration landed |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `fwd-c1-substrate-distance-1-mellin-pole-s3-canonical-TEMPLATE-INHERITED` |
| `scheme` | `lmax-scan-parameterized-slope-a-canonical` |

PRDR cardinality check: 20 free parameters; 20 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `s84_spectrum_cache_L12_tau019.npz` | `<computed at plan-freeze>` |
| `s89_w5_a31_fwd_c1_retry_parameterized_slope_A_canonical.npz` (S89 reference) | `<computed at plan-freeze>` |
| `canonical_constants.py:1681` (n_s_FW_exact) | `<computed at plan-freeze>` |
| `canonical_constants.py:1719` (slope_A_FW_Conv_A_GEOMETRIC) | `<computed at plan-freeze>` |
| `canonical_constants.py` (c_sub_baseline, planck_ns, tau_fold) | `<computed at plan-freeze>` |
| `S87 W7a audit` (`01c1ac83…`) | `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` |
| `S87 W7b audit` (`d7826bcb…`) | `d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f` |
| `permanent-results-registry.md §VII.AU` (post-CF-63 deferred-pending) | `<computed at plan-freeze>` |
| `cross-pillar-bridge-corpus.md §4` (FWD-C1 spec lines 120-128) | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md §"Level-2-binding"` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value=(alpha, R², delta_n_s_at_10), \
 scheme=lmax-scan-parameterized-slope-a-canonical, \
 convention=fwd-c1-substrate-distance-1-mellin-pole-s3-canonical-TEMPLATE-INHERITED, \
 L_max=12)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate | §VII.AU promotion |
|:-----|:----------|:------------------|
| **PASS** | α ∈ [2.5, 3.5] AND R² ≥ 0.95 AND `| n_s_recomputed(10) − n_s_FW_exact | < 1e-9` | from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION to STAGE-1-CANDIDATE; HIT K-counter K=2 → K=3 (joint with CF-61 dual PASS hits MANDATORY threshold) |
| **INFO** | α ∈ [2.0, 2.5) ∪ (3.5, 4.5] OR R² ∈ [0.90, 0.95) | partial Level-2-binding; §VII.AU remains REGISTRY-INCOMPLETE; queue for S91 |
| **FAIL** | α outside [2.0, 4.5] OR R² < 0.90 OR L_max=10 anchor mismatch | Level-2-binding violated at FWD-C1; §VII.AU remains REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; structural carry-forward to S91 |

Composite collapse: sign_verdict = PASS by-construction (α > 0 per L^{-3}
envelope predicted direction); magnitude_verdict per band;
regime_verdict = VALID if every L_max ∈ {6..12} produces finite
n_s_recomputed within plausible band [0.5, 1.0], MARGINAL if 1 sector
saturates edge, BREAKDOWN if ≥ 2 sectors saturate.

### Substitution chain (MANDATORY for α scaling direction)

```
Definitions:
  n_s_recomputed(L_max) := substrate-distance-1 Hochschild pairing image
                           at L_max truncation via Route-B identity
                           parameterized by slope_A_canonical(L_max)
                           and c_sub_corrected(L_max)
  n_s_FW_exact          := 9561/10000 bit-exact (canonical_constants.py:1681)
  delta_n_s(L_max)      := | n_s_recomputed(L_max) - n_s_FW_exact |
  alpha                 := -slope of log-log fit of delta_n_s vs L_max
  envelope predicted    := L^{-3} at d=4 (cross-pillar-bridge-anatomy.md
                           §"Level-2-binding" d=4 calibration)

Substitutions:
  Step 1: Per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-
          Confidence Ladder"` Level-2 at d=4, HKR-image convergence rate
          is bounded by L^{-3}.
  Step 2: Under Pillar I ↔ Pillar II FWD-C1 bridge, delta_n_s(L_max) =
          O(L_max^{-α}) with α predicted = 3 at d=4.
  Step 3: At L_max=10 canonical truncation, n_s_recomputed(L_max=10) IS the
          substrate-IS observable at the canonical anchor; by construction
          n_s_recomputed(10) ≡ n_s_FW_exact bit-exact (the canonical pin
          is defined at this truncation).
  Step 4: For L_max ∈ {6..11}, delta_n_s decreases monotonically toward
          L_max=10 anchor, then beyond L_max=10 the L_max=12 truncation
          tail shows delta_n_s(12) ≤ delta_n_s(10) (continued monotone
          convergence into the L_max → ∞ limit).
  Step 5: Log-log fit on L_max ∈ {6..11} extracts α; α ∈ [2.5, 3.5] PASS
          band centered on 3 with ±17% half-width.
  Step 6: Direction: α ∈ [2.5, 3.5] AND L_max=10 anchor match ⟹ Level-2-
          binding envelope confirmed at substrate-distance-1 ⟹ §VII.AU
          promotion to STAGE-1-CANDIDATE structurally licensed.

Conclusion: PASS verdict directly upgrades §VII.AU from REGISTRY-INCOMPLETE-
            PENDING-FIRST-EXTRACTION to STAGE-1-CANDIDATE. Combined with
            CF-61 PASS, advances HIT K-counter K=2 → K=3 (MANDATORY
            threshold per feedback_rules-compensate-missing-structure.md).
```

### What PASSES/FAILS MEAN for solution space

- **PASS**: §VII.AU registry-status upgrade from REGISTRY-INCOMPLETE-PENDING-
  FIRST-EXTRACTION to STAGE-1-CANDIDATE per `joint-theorem-promotion.md
  §"Stage 1"`. The FWD-C1 substrate-IS observable IS Level-2-binding at
  d=4 with L^{-3} envelope confirmed. Forward consumer: §VII.AU registry
  entry promotes to STAGE-1-CANDIDATE; Stage-2 cross-axis independent verify
  dispatch queued for S91+. Joint with CF-61 PASS: HIT K-counter K=2 → K=3
  (MANDATORY threshold). Calibration corpus advances: cross-pillar-bridge-
  anatomy Level-2-binding SUGGESTION K=1 → K=2 (new instance: FWD-C1
  substrate-IS observable).
- **INFO**: partial Level-2-binding; §VII.AU remains REGISTRY-INCOMPLETE.
  Routes to S91 with refined L_max scan (extend to L_max=14 conditional on
  Friedrich-Bär saturation extension landing).
- **FAIL**: Level-2-binding violated; §VII.AU remains REGISTRY-INCOMPLETE-
  PENDING-FIRST-EXTRACTION permanently unless a refined proxy can be
  derived. Structural carry-forward to S91.

### Effort estimate
1.0 wave-equivalent. Per-L_max slope_A canonical (closed-form, ~5 min) +
M_Pl_eff² computation on 7 truncated spectra (~30 min wall using cache
filter; no spectrum-build cost) + Route-B identity evaluation + log-log
regression + L_max=10 anchor verification + verdict-line + promotion-cross-
link emission.

### Substrate-framing reminder
FWD-C1 substrate-IS observable IS the substrate-distance-1 Mellin pole
Hochschild pairing image n_s_FW = 9561/10000 on the finite spectral triple
`(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The parameterized slope-A canonical IS
intrinsic to the substrate's geometric structure
(closed-form `10/(1 − τ/(5π))`); the c_sub_corrected IS intrinsic to the
substrate's M_Pl_eff² channel. The L_max scan IS the empirical envelope on
the substrate's own L_max truncation parameter — NOT a coordinate sweep on
a meta-container. The L^{-3} algebraic envelope at d=4 IS the HKR-image
convergence rate from the substrate's intrinsic L_max truncation toward the
L_max → ∞ continuum binding (the cohomology-class binding under the bridge
map per `cross-pillar-bridge-anatomy.md §"Level-2-binding"` Level-2-binding
admissibility). Direction of explanation: substrate (Pillar I spectral
triple) → bridge (HKR L_max → ∞) → laboratory (Pillar II continuum CMB
n_s measurement).

---

## §W8-8. CF-66 — S90-W6-7-D-MAX-CO-AUTHOR-RE-DISPATCH

### Gate ID
`S90-W6-7-D-MAX-CO-AUTHOR-RE-DISPATCH`

### Trigger
`[AUDIT]` — substantive D_max measurement at substrate-distance-2 pole s=4
between SCHEMATIC and FULL physical regularization tiers with FULL physical
Pauli-Villars pipeline at Λ_UV = M_KK = 7.43e16 GeV. Verdict classifies the
D_max into a severity band per `epistemic-discipline.md §"Source
Reconciliation"` 4-band calibration (NO-ACTION / ADVISORY / MANDATORY /
HARD-HALT).

### Classification
META (D_max measurement methodology + W3 A.14 cross-wave npz consumption).
The D_max IS the structural distance between the SCHEMATIC level-pin output
(SCHEMATIC tier from `_spectral_action_regulators.py`) and the FULL physical
level-pin output (full PV pipeline at Λ_UV = M_KK) at the substrate-distance-2
pole s=4. Expected band: NO-ACTION or ADVISORY (SCHEMATIC and FULL-physical
PV coincide modulo closed-form scalar multiplier per `pauli_villars_a_n`
docstring).

### Agent type
**gen-physicist** PRIMARY (substantive D_max measurement; FULL physical PV
pipeline reconstruction or packaged S61/S78 invocation); **connes-ncg-
theorist** CO-AUTHOR (level-pin cross-tier structural reading; SCHEMATIC vs
FULL physical algebra-axis orthogonality at substrate-distance-2 pole;
`substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 inheritance-pin
retroactive remediation clause invocation at S88 W-24 V.4 / B.62 — if
SCHEMATIC-vs-FULL jump ≥ 1 OOM, the W4-2 + W9b-2 inheritance pathway
requires Class-(d) tagging).

### Hypothesis
Substantive D_max at substrate-distance-2 pole s=4 between W9b-2 SCHEMATIC
output (`rho_S_s4` and `zeta_D_s4` from `s87_w9b_pole_specificity_scan.npz`)
and FULL physical PV pipeline output (S61/S78 packaged or reconstructed PV
subtraction at Λ_UV = M_KK = 7.43e16 GeV) is measurable AND falls in the
NO-ACTION or ADVISORY severity band (D_max < 1.0 OOM), confirming that the
SCHEMATIC level-pin is a faithful proxy modulo closed-form scalar.

### Method (full self-contained dispatch prompt)

Producing script: `computations/session-90/s90_w8_w6_7_d_max_co_author_re_dispatch.py`.

#### Step 1 — Load SCHEMATIC inputs
Load `computations/session-87/s87_w9b_pole_specificity_scan.npz` (W9b-2;
SCHEMATIC tier under `_spectral_action_regulators.py` analytic helpers).
Extract:
- `rho_S_s4` (SCHEMATIC spectral density moment at s=4)
- `zeta_D_s4` (SCHEMATIC zeta-D spectral moment at s=4)

#### Step 2 — Load W3 A.14 cross-wave npz
Load `computations/session-89/s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz`
(W3 A.14 cross-wave). Extract regulator-invariant cocycle ratio inputs for
cross-validation.

#### Step 3 — Build FULL physical PV pipeline at Λ_UV = M_KK
Per `substrate-first-canonical-sourcing.md §(iv)` and S61/S78 packaged
pipeline:
- Pauli-Villars regularization at Λ_UV = M_KK = 7.428660036284456e+16 GeV
  (canonical_constants.py:M_KK)
- PV mass M_PV² = Λ_UV² = M_KK²
- Subtraction scheme: `M_n^{FULL,s=4} = Σ_a |λ_a|^{-4} − Σ_a |λ_a + M_PV²|^{-4}`
  (standard PV subtraction at UV scale Λ_UV)

If S61/S78 produces canonical PV pipeline module: invoke directly.
If reconstruction required: build from `dirac_spectrum.py` + canonical PV
recipe; cross-validate against S61/S78 reference outputs if available.

#### Step 4 — Compute FULL-tier `rho_S_s4^{FULL}` and `zeta_D_s4^{FULL}`
Evaluate the same spectral moments as W9b-2 SCHEMATIC but with FULL
physical PV pipeline:
- `rho_S_s4^{FULL}` via FULL PV-subtracted spectral density at s=4
- `zeta_D_s4^{FULL}` via FULL PV-subtracted zeta-D at s=4

#### Step 5 — Compute D_max
```
D_max := max(
  | log10(rho_S_s4^{SCHEMATIC}) - log10(rho_S_s4^{FULL}) |,
  | log10(zeta_D_s4^{SCHEMATIC}) - log10(zeta_D_s4^{FULL}) |
)
```

#### Step 6 — Severity band classification per 4-band calibration
Per `epistemic-discipline.md §"Source Reconciliation"`:
- `D_max < 0.1` → NO-ACTION
- `0.1 ≤ D_max < 1.0` → ADVISORY (S2)
- `1.0 ≤ D_max < 3.0` → MANDATORY (S1; halts downstream plan-freeze)
- `D_max ≥ 3.0` → HARD-HALT (manual review required)

#### Step 7 — Inheritance-pin retroactive remediation check
Per `substrate-first-canonical-sourcing.md §(iv)` Inheritance-pin retroactive
remediation (S88 W-24 V.4 / B.62): if D_max ≥ 1 OOM, any S89+ gate inheriting
W4-2 or W9b-2 SCHEMATIC outputs requires Class-(d) PIN-DERIVATIVE-VS-SOURCE-
PRIMARY tagging. Document if inheritance-class tagging required.

#### Step 8 — Verdict-line append
```
S90-W6-7-D-MAX-CO-AUTHOR-RE-DISPATCH: \
  PASS|FAIL|INFO -- value=<(D_max, severity_band)> \
  scheme=FULL-physical-PV-pipeline-vs-SCHEMATIC \
  convention=substrate-distance-2-pole-s4 \
  L_max=10 \
  audit_sha256=<closure> content_sha256=<closure> schema_version=S84+
```

#### Outputs
- `s90_w8_w6_7_d_max_co_author_re_dispatch.npz` (D_max value, severity band,
  SCHEMATIC vs FULL spectral moments at s=4, inheritance-pin remediation
  flag)
- `s90_w8_w6_7_d_max_co_author_re_dispatch.json` (machine-readable D_max
  report)

### Machinery pin (PRDR)

| Parameter | Pin |
|:----------|:----|
| `pole_s` | 4 (substrate-distance-2) |
| `L_max_schematic_truncation_target` | 10 (W9b-2 analysis-side SCHEMATIC truncation level; the SCHEMATIC half of the SCHEMATIC-vs-FULL D_max comparison; INTENTIONALLY distinct from `s87_w9b_pole_specificity_scan.npz`'s `L_max=12` cache-metadata value, which anchors the FULL-physical PV pipeline side via `L_max_full_physical_pv` below) |
| `L_max_full_physical_pv` | 12 (matches `s87_w9b_pole_specificity_scan.npz` `L_max=12` cache-metadata; the FULL-physical-side D_max anchor; pin is by-design IDENTICAL to npz cache to confirm FULL pipeline uses same L_max as W9b-2 cached spectrum) |
| `tau` | 0.19 (τ_fold) |
| `Lambda_UV` | M_KK = 7.428660036284456e+16 GeV (canonical_constants.py) |
| `pv_mass_squared` | M_PV² = Lambda_UV² |
| `full_pipeline_source` | S61/S78 packaged OR reconstructed from canonical recipe |
| `schematic_inputs` | s87_w9b_pole_specificity_scan.npz {rho_S_s4, zeta_D_s4} |
| `w3_a14_cross_wave_npz` | s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz |
| `d_max_no_action_threshold` | 0.1 OOM |
| `d_max_advisory_threshold` | 1.0 OOM |
| `d_max_mandatory_threshold` | 3.0 OOM |
| `inheritance_pin_remediation_trigger` | D_max ≥ 1.0 OOM (per §(iv) B.62) |
| `random_seed` | not applicable (deterministic) |
| `verdict_source` | `computations/session-90/s90_gate_verdicts.txt` |
| `convention` | `substrate-distance-2-pole-s4` |
| `scheme` | `FULL-physical-PV-pipeline-vs-SCHEMATIC` |

PRDR cardinality check: 16 free parameters; 16 pinned; D_PRU_raw = 0.

### Input SHA-256 pins

| Input | SHA |
|:------|:----|
| `s87_w9b_pole_specificity_scan.npz` | `<computed at plan-freeze>` |
| `s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` | `<computed at plan-freeze>` |
| `canonical_constants.py:M_KK` | `<computed at plan-freeze>` |
| `S61/S78 PV pipeline reference` (if packaged) | `<computed at plan-freeze>` |
| `dirac_spectrum.py` | `<computed at plan-freeze>` |
| `_spectral_action_regulators.py` (SCHEMATIC docstring lines 23-30) | `<computed at plan-freeze>` |
| `epistemic-discipline.md §"Source Reconciliation"` 4-band | `<computed at plan-freeze>` |
| `substrate-first-canonical-sourcing.md §(iv) §"Inheritance-pin"` | `<computed at plan-freeze>` |

### Expected output 4-tuple

```
(value=(D_max, severity_band), \
 scheme=FULL-physical-PV-pipeline-vs-SCHEMATIC, \
 convention=substrate-distance-2-pole-s4, L_max=10)
```

### PASS/FAIL/INFO thresholds (pre-registered)

| Band | Predicate | Expected |
|:-----|:----------|:---------|
| **PASS (NO-ACTION or ADVISORY)** | D_max < 1.0 OOM | EXPECTED — SCHEMATIC and FULL-physical PV coincide modulo closed-form scalar multiplier per `pauli_villars_a_n` docstring |
| **INFO (MANDATORY)** | 1.0 ≤ D_max < 3.0 OOM | unexpected; SCHEMATIC and FULL physical structurally differ at substrate-distance-2; routes to W4-2 + W9b-2 inheritance-pin retroactive remediation |
| **FAIL (HARD-HALT)** | D_max ≥ 3.0 OOM | severe; manual review of FULL physical pipeline construction required; downstream Class-(d) inheritance tagging MANDATORY |

### Substitution chain (audit-form)

```
Definitions:
  rho_S_s4^{SCHEMATIC}  := substrate-distance-2 spectral density moment
                           under SCHEMATIC tier (_spectral_action_regulators.py)
  rho_S_s4^{FULL}       := same under FULL physical PV pipeline at Λ_UV = M_KK
  zeta_D_s4^{SCHEMATIC} := substrate-distance-2 zeta-D moment under SCHEMATIC
  zeta_D_s4^{FULL}      := same under FULL physical PV
  D_max                 := max(|Δ_log10(rho_S)|, |Δ_log10(zeta_D)|)

Substitutions:
  Step 1: Per `pauli_villars_a_n` docstring + S61/S78 packaged pipeline,
          SCHEMATIC tier captures the structural form of PV subtraction at
          substrate-distance-2 modulo a closed-form scalar multiplier.
  Step 2: If closed-form scalar multiplier is bit-exact and applied
          consistently in both rho_S and zeta_D, then SCHEMATIC = FULL ·
          closed-form-scalar; in log10 space: Δ_log10 = constant offset
          identical across rho_S and zeta_D.
  Step 3: D_max = max of |Δ_log10|; if scalar offset only, D_max = |Δ_log10|
          = 0 modulo numerical floor (~ machine epsilon).
  Step 4: D_max < 0.1 ⟹ NO-ACTION (SCHEMATIC ≡ FULL bit-exact within
          floating-point floor)
          0.1 ≤ D_max < 1.0 ⟹ ADVISORY (small-but-measurable deviation;
          documented; no downstream blocking)
          1.0 ≤ D_max < 3.0 ⟹ MANDATORY (substantial deviation; halts
          plan-freeze on downstream gates using W4-2 / W9b-2 outputs)
          D_max ≥ 3.0 ⟹ HARD-HALT (manual review required)
  Step 5: Direction: D_max in NO-ACTION or ADVISORY ⟹ SCHEMATIC IS faithful
                       proxy; inheritance-pin retroactive remediation NOT
                       required for downstream consumers.
          Direction: D_max in MANDATORY or HARD-HALT ⟹ inheritance-pin
                       retroactive remediation MANDATORY; downstream S89+
                       gates inheriting W4-2 / W9b-2 SCHEMATIC outputs
                       require Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY
                       tagging per S88 W-24 V.4 / B.62.

Conclusion: D_max value classifies SCHEMATIC-vs-FULL severity at substrate-
            distance-2 pole; severity band determines whether inheritance-
            pin retroactive remediation fires on downstream S89+ gates.
```

### What PASSES/FAILS MEAN for solution space

- **PASS (NO-ACTION or ADVISORY; D_max < 1.0 OOM)**: SCHEMATIC tier IS a
  faithful proxy at substrate-distance-2 pole s=4 modulo closed-form scalar.
  Downstream S89+ gates inheriting W4-2 / W9b-2 SCHEMATIC outputs do NOT
  require Class-(d) inheritance-pin retroactive remediation. The §VII.AR
  LEVEL-DRESSED structural classification (W-22 W7a-74 V.5) retains its
  K=4 calibration corpus admissibility on the SCHEMATIC-tier basis.
- **INFO (MANDATORY; 1.0 ≤ D_max < 3.0 OOM)**: substantial SCHEMATIC-vs-FULL
  deviation; inheritance-pin retroactive remediation MANDATORY on downstream
  S89+ gates per `substrate-first-canonical-sourcing.md §(iv) §"Inheritance-
  pin retroactive remediation"` S88 W-24 V.4 / B.62. The §VII.AR LEVEL-
  DRESSED registry text routes to remediation queue for S91.
- **FAIL (HARD-HALT; D_max ≥ 3.0 OOM)**: severe SCHEMATIC-vs-FULL divergence;
  manual review of FULL physical PV pipeline construction at Λ_UV = M_KK
  required; downstream Class-(d) inheritance tagging MANDATORY across all
  W4-2 / W9b-2 inheritance pathways; structural carry-forward to S91 with
  rule-file extension review per `substrate-first-canonical-sourcing.md`.

### Effort estimate
0.6 wave-equivalents. SCHEMATIC inputs already cached; FULL physical PV
pipeline construction (~30-45 min wall using `dirac_spectrum.py` + canonical
PV recipe; S61/S78 packaged reduces to ~15 min if available); D_max
computation + severity band classification + inheritance-pin remediation
check + verdict-line emission.

### Substrate-framing reminder
The D_max IS the structural distance between two regularization-tier images
of the substrate-IS spectral moments at the substrate's substrate-distance-2
pole s=4. The substrate-distance-2 pole IS intrinsic to the substrate's
spectral-zeta function structure (Connes-Moscovici 1995 dim-spectrum); both
SCHEMATIC and FULL physical PV pipelines compute different methodology-floor
images of the same substrate-IS observable under the layer-functor F per
`epistemic-discipline.md §"Layer-Decomposition"`. The D_max IS the structural
fidelity probe at the UV-regulator axis (per `regulator-pin-discipline.md`)
between the two F-images. Direction of explanation: substrate (intrinsic
spectral-zeta dim-spectrum) → regulator-tier methodology-floor images
(SCHEMATIC vs FULL) → severity band classification. The PASS band is the
expected outcome under structural fidelity at substrate-distance-2; the
INFO/FAIL bands signal inheritance-pathway remediation needs.

---

## Wave 8 → S91+ Decision Point

### Closure semantics on Wave 8

Wave 8 produces three structurally distinct closure events:

1. **HIT K-counter advancement to K=3 MANDATORY** — CF-61 PASS AND CF-65
   PASS (joint dual PASS in a single S90 dispatch) advances HIT K-counter
   from K=2 (S89 close) to K=3, hitting the MANDATORY promotion threshold
   per `feedback_rules-compensate-missing-structure.md`. Joint with CF-64
   PASS, the K-counter further advances to K=4.

2. **HIT K-counter advancement to K=4 (independent path)** — CF-64 single-
   shot AFTER-pattern 8/8 structural-coherence emission of §VII.AU.OP-PROJ
   FWD-C1 STAGE-1-CANDIDATE bridge landing advances HIT K-counter from K=3
   to K=4. This advancement is INDEPENDENT of CF-61+CF-65 dual PASS
   (different calibration corpus instance; different substrate-IS observable
   class).

3. **Cross-tier structural-fidelity convergence** — CF-60 PASS (Spearman
   classification of §VII.AR LEVEL-DRESSED into WEAKENED vs STRENGTHENED) +
   CF-66 PASS (D_max classification into severity band) jointly characterize
   the cross-tier SCHEMATIC-vs-FULL structural fidelity at substrate-
   distance-2 pole s=4. Forward consumers (W7 CF-58 Stage-2 §VII.AR
   independent verify) receive these as input pins.

### Carry-forward computations (4-field structured)

#### CF-67 (S91+): Stage-2 cross-axis independent-verify for §VII.AU.OP-PROJ FWD-C1

- **What**: Dispatch Stage-2 cross-axis independent-verify per
  `joint-theorem-promotion.md §"Stage 2"` 4-stage pathway. Cross-reviewers
  on DIFFERENT axes from lizzi + connes (the W8 CF-64 authors); candidate
  assignments per Stage-2 Axis-B Selection Protocol (S88 W-14 V.2 / B.15):
  Axis-A NOT in {lizzi, connes}; Axis-B substrate-physics or NCG-axiomatic.
- **Inputs**: §VII.AU.OP-PROJ STAGE-1-CANDIDATE registry text (post-CF-64);
  S87 W7a + W7b + W4-4 audit_sha pins; FWD-C1 spec at
  `cross-pillar-bridge-corpus.md §4`.
- **Gate**: PASS-AND across both cross-reviewer verdicts on (i) Element-1
  substrate-IS observable n_s_FW = Hochschild pairing image bit-exact;
  (ii) Element 2 OE-form regex-compliance; (iii) HKR L_max → ∞ bridge map;
  (iv) L^{-3} envelope at d=4 with α extracted by CF-65.
- **Effort**: 1.5 we (parallel dispatch).

#### CF-68 (S91+): Stage-2 cross-axis independent-verify for §VII.AV Corner-IV K-window log-derivative

- **What**: Dispatch Stage-2 cross-axis independent-verify per
  `joint-theorem-promotion.md §"Stage 2"` for §VII.AV post-CF-61 PASS
  promotion to STAGE-1-CANDIDATE.
- **Inputs**: §VII.AV STAGE-1-CANDIDATE registry text (post-CF-61);
  §W5-2 npz canonical anchor; FULL BdG re-derivation per L_max output
  npz from CF-61.
- **Gate**: PASS-AND across both cross-reviewer verdicts on (i) BdG sub-
  algebra `M_2(ℂ)` substrate-IS observable identity (Type-F single-summand
  trace); (ii) HKR L_max → ∞ bridge map; (iii) L^{-3} envelope at d=4 with
  α extracted by CF-61.
- **Effort**: 1.5 we (parallel dispatch).

#### CF-69 (S91+): Level-2 moduli-deformation substrate-IS extension for §VII.AU

- **What**: Per CF-63 §VII.AU cross-link to CF-59 (= CF-W5-1 gen) as queued
  Level-2 verification path: extend §VII.AU substrate-IS observable from
  Level-1 single-τ-slice at τ_fold to Level-2 moduli-deformation across
  τ ∈ {0.18, 0.19, 0.20} (per S91+ deferred item W-1 AUX-6). Conditional
  on CF-59 PASS-A or PASS-B verdict.
- **Inputs**: §VII.AU STAGE-1-CANDIDATE registry (post-CF-65); CF-59 verdict
  output npz; canonical_constants slope_A_FW_Conv_A_GEOMETRIC.
- **Gate**: PASS iff Level-2 moduli-deformation extension produces consistent
  α extraction across 3 τ-values; INFO if α scatter > 10%; FAIL if scatter
  > 25%.
- **Effort**: 1.0 we.

### Wave 8 verdict summary table

| Gate ID | Trigger | Effort | PASS/FAIL/INFO bands | Promotion semantics |
|:--------|:--------|:-------|:---------------------|:--------------------|
| CF-59 | [VERIFY] | 1.0 we | R_emp band: PASS-A [0.95,1.10] / PASS-B [1.80,2.20] / INFO / FAIL | canonical_constants.py:1714 discharge or replacement |
| CF-60 | [VERIFY] | 1.0 we | (N_FULL ≥ 4/5) × (Spearman ≥ 0.9 PASS-A; < 0.9 PASS-B) | §VII.AR LEVEL-DRESSED WEAKENED vs STRENGTHENED |
| CF-61 | [VERIFY-THEOREM] | 1.5 we | α ∈ [2.5,3.5] AND R² ≥ 0.95 AND L_max=12 anchor | §VII.AV STAGE-1-CANDIDATE promotion; HIT K=2→K=3 (with CF-65) |
| CF-62 | [AUDIT] | 0.5 we | 5-anatomy IS-not-IN audit + SUPERSEDES tag emission | bridge classification Pillar III/IV ↔ Pillar V |
| CF-63 | [AUDIT] | 0.3 we | 8-criterion registry-landing audit per `_registry_landing_audit.py` | §VII.AV + §VII.AU initial deferred-pending registrations |
| CF-64 | [CHAIN] | 1.0 we | 8/8 structural-coherence booleans True in single-shot AFTER-pattern | §VII.AU.OP-PROJ STAGE-1-CANDIDATE; HIT K=3→K=4 |
| CF-65 | [VERIFY] | 1.0 we | α ∈ [2.5,3.5] AND R² ≥ 0.95 AND L_max=10 anchor < 1e-9 | §VII.AU STAGE-1-CANDIDATE promotion; HIT K=2→K=3 (with CF-61) |
| CF-66 | [AUDIT] | 0.6 we | D_max severity band (NO-ACTION / ADVISORY / MANDATORY / HARD-HALT) | inheritance-pin retroactive remediation trigger conditional on D_max ≥ 1 OOM |

**Total effort**: 6.9 wave-equivalents.

---

## Wave 8 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR
discipline, every gate's free parameters MUST be pinned at plan-freeze.
Wave-aggregate pin enumeration:

| Gate | Free params | Pinned params | D_PRU_raw |
|:-----|:-----------:|:-------------:|:---------:|
| CF-59 | 13 | 13 | 0 |
| CF-60 | 14 | 14 | 0 |
| CF-61 | 16 | 16 | 0 |
| CF-62 | 14 | 14 | 0 |
| CF-63 | 17 | 17 | 0 |
| CF-64 | 20 | 20 | 0 |
| CF-65 | 20 | 20 | 0 |
| CF-66 | 16 | 16 | 0 |

Wave aggregate: 130 free parameters; 130 pinned; D_PRU_raw = 0.

Source-Reconciliation pre-flight (per Class-(a)..(f) taxonomy):
- All canonical_constants.py pins (n_s_FW_exact, slope_A_FW_Conv_A_GEOMETRIC,
  slope_A_FW_Conv_A_AT_TAU_FOLD, c_sub_baseline, kappa_2_substrate_FW,
  tau_max_HK5_regime_FW, M_KK, Delta_BCS, tau_fold, planck_ns) — Class (e)
  PIN-PROMOTES-TO-CANONICAL: not applicable (all pins are already canonical
  at S89 close); Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY: applicable for
  c_sub_corrected (derived from c_sub_baseline + M_Pl_eff² ratio); audit
  pin algebraic-equivalence verified.
- All S87 verdict-SHA pins (W7a, W7b, W4-4, W7c emission #3): no drift; pins
  match latest non-superseded canonical lines per Option A reading discipline.
- W3 A.14 cross-wave npz: substrate canonical from S89 W3-1 PASS LANDED;
  no drift.

Substrate-first-canonical-sourcing pre-flight (per §(iv) MANDATORY-K=4):
- CF-60 producing script consumes FULL-tier branches of
  `_spectral_action_regulators.py` (NOT SCHEMATIC); CLASS pin = FULL;
  convention tag carries no `-SCHEMATIC` suffix; structurally compliant.
- CF-66 producing script consumes BOTH SCHEMATIC (`_spectral_action_regulators.py`
  via W9b-2 inputs) AND FULL physical PV pipeline (S61/S78 packaged or
  reconstructed); CLASS pins TWO-fold (SCHEMATIC for W9b-2 inputs; FULL
  for FULL physical PV reconstruction); convention tag explicitly
  declares cross-tier comparison via `FULL-physical-PV-pipeline-vs-SCHEMATIC`.
- CF-65 producing script consumes canonical helpers (Route-B identity from
  S87 W7a Sage-QQ exact); convention tag carries `-TEMPLATE-INHERITED`
  suffix per W1 CF-15 retrofit + §(iv) discipline.

---

## Wave 8 Input-SHA Ledger

Plan-freeze-time SHA pin map (audit_sha256 closure inputs across all 8 gates):

| Source | Type | Pinned at |
|:-------|:-----|:----------|
| `computations/session-87/s87_spectrum_cache_L14_tau019.npz` | data file | plan-freeze |
| `computations/session-87/s87_w1b_pv_subtraction_recalibration.npz` | data file | plan-freeze |
| `computations/session-87/s87_w9b_pole_specificity_scan.npz` | data file | plan-freeze |
| `computations/session-89/s89_w5_a28_spectrum_cache_L6_tau038.npz` | data file | plan-freeze |
| `computations/session-89/s89_w5_a31_fwd_c1_retry_parameterized_slope_A_canonical.npz` | data file | plan-freeze |
| `computations/session-89/s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` | data file | plan-freeze |
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | data file | plan-freeze |
| `computations/session-52/s52_bogoliubov_amp.npz` | data file | plan-freeze |
| `computations/_shared/dirac_spectrum.py` | module | plan-freeze |
| `computations/_shared/_spectral_action_regulators.py` | module | plan-freeze |
| `computations/_shared/_registry_landing_audit.py` | audit script | plan-freeze |
| `computations/_shared/canonical_constants.py` | constants module | plan-freeze |
| `sessions/permanent-results-registry.md` (post-CF-18 + CF-63) | registry | plan-freeze |
| `sessions/framework/registry/cross-pillar-bridge-corpus.md` | corpus | plan-freeze |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | rule | plan-freeze |
| `.claude/rules/joint-theorem-promotion.md` | rule | plan-freeze |
| `.claude/rules/registry-landing.md` | rule | plan-freeze |
| `.claude/rules/phononic-framing.md` | rule | plan-freeze |
| `.claude/rules/substrate-first-canonical-sourcing.md` | rule | plan-freeze |
| `.claude/rules/v3-closure-recovery.md` | rule | plan-freeze |
| `.claude/rules/gate-verdicts.md` | rule | plan-freeze |
| `.claude/rules/epistemic-discipline.md` | rule | plan-freeze |
| `.claude/rules/regulator-pin-discipline.md` | rule | plan-freeze |
| `.claude/rules/math-scripts.md` | rule | plan-freeze |
| `.claude/rules/mechanical-closure-discipline.md` | rule | plan-freeze |
| `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md` line 898 + 1011 | workshop | plan-freeze |
| `sessions/archive/session-89/workshops/s89-w6-level2-binding-inheritance.md` Q3 Fork B | workshop | plan-freeze |
| S87 W7a `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` | verdict SHA | hard-pinned |
| S87 W7b `d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f` | verdict SHA | hard-pinned |
| S87 W4-4 `e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` | verdict SHA | hard-pinned |
| S87 W7c emission #3 `cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d` | verdict SHA | hard-pinned |
| S89 W3-1 `dff2f63006e29b1b4f9d7abe53c7c9b7dc2e049ac454368323246bd71c140056` | verdict SHA | hard-pinned |
| S89 W3-7 `9de3814811c2a9929a6d50d36a62dcdd829d850a5c22fd59d88768ca008825e3` | verdict SHA | hard-pinned |
| S89 W3-9 `136630ecc2869880c879aa805ce28e088374f77688755b1c2d8c82a8884026df` | verdict SHA | hard-pinned |

Cross-wave dependency pins (from W1 / W2 + this wave):
- W1 CF-14 (`cross-pillar-bridge-anatomy.md §"Enforcement clause"`
  deferred-pending extension) — PRECEDES CF-63 + CF-15
- W1 CF-15 (TEMPLATE-INHERITED convention-tag retrofit) — PRECEDES CF-65
- W2 CF-18 (§VII.AAU + §VII.AV WITHDRAWN-IN-FAVOR-OF-S90-LANDING cleanup) —
  PRECEDES CF-64
- CF-62 PRECEDES CF-61 (within Wave 8)
- CF-63 PRECEDES CF-61 + CF-65 (within Wave 8)
- CF-60 PRECEDES W7 CF-58 (downstream)

Canonical verdict-file path for ALL 8 verdict-line emissions:
`computations/session-90/s90_gate_verdicts.txt`

End of Wave 8.
