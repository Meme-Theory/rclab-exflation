# Session 88 W20 Synthesis: INFO-band substrate-first canonical eligibility for FWD-C1 unblocking — substrate-first §iv vs PRU Class 8.3 boundary

**Date**: 2026-05-07
**Agent**: mack-cosmic-bridge (Cosmic Bridge — observational anchors, FWD-C1 Pillar I↔II downstream consumer, sole-writer for `sessions/framework/registry/falsifier-master-inventory.md`)
**Source Documents**:
- `sessions/archive/session-88/session-88-w6a-workingpaper.md` (866 lines; §W6a-51 INFO + §W6a-52 PASS Stage-0 joint closures + W6a synthesis)
- `sessions/session-plan/session-88-plan-w6a.md` (641 lines; the pre-registered plan whose §10 Step 8 estimate is the disputed object)
- `sessions/archive/session-88/workshops/_seed-w6a.md` (68 lines; investigator-identified Workshop 3 tension that this synthesis closes)
- `.claude/rules/substrate-first-canonical-sourcing.md` (Class-(f) PIN-PLACEHOLDER routing + level-pin §iv MANDATORY at K=4)
- `.claude/rules/epistemic-discipline.md` (Class 8.3 publication-precision pre-registration MANDATORY at K=4 + Class-(f) 4-band SOURCE-RECONCILIATION calibration)

---

## I. Session Outcome

The plan §10 Step 8 pre-registered residual estimate `≈ 4e-9` is structurally **NOT recoverable from any term in the §10 substitution chain Steps 1–8** as written: the linear-LO O(τ²) ceiling is `1.463e-3`; the geometric-resummation-implied O(τ³) leading correction is `1.770e-5`; the actual residual `5.230e-5` sits between them; the value `≈ 4e-9` matches none of these. Per Python verification (this synthesis): `D_max = |log10(5.230e-5) − log10(4e-9)| = 4.1165 OOM`, well inside the **HARD-HALT band (D_max ≥ 3.0)** of the `epistemic-discipline.md §"Source Reconciliation"` Class-(f) calibration. **However**, the substrate-physics PASS criterion (regulator-class invariance EXACT, `regulator_invariance_residual = 0.000e+00` Sage-symbolic in CC2) is met independently, and the regulator-class invariance is the load-bearing structural property a substrate-first canonical actually carries — not the numerical residual against an empirical Richardson anchor. **Structural verdict** (this synthesis, not re-adjudicating either source verdict): both readings are partially correct on different axes; the resolution is to **promote `slope_A_FW` to canonical_constants.py NOW** (mack reading on substrate-first axis prevails) **AND** simultaneously **fix the plan §10 Step 8 estimate retroactively as a structural defect closure** (lizzi reading on publication-precision axis prevails), with the FWD-C1 unblocking explicitly DEPENDING on Workshop 1 (geometric-resummation vs linear-LO adjudication) for the SHAPE of the canonical promotion (parameterized closed form vs scalar pin) and on Workshop 18 (re-derived residual threshold) for any FUTURE re-evaluation of W6a-51's INFO-vs-PASS classification. The disputed verdicts §W6a-51 INFO and §W6a-52 PASS are **NOT** disturbed.

---

## II. Key Results

### Result II.1 — D_max = 4.12 OOM HARD-HALT band against pre-registration is structurally REAL on the publication-precision axis, but APPLIES to the plan estimate, NOT to the substrate canonical it triggers

**Result**: D_max = 4.1165 OOM ≥ 3.0 → HARD-HALT per `epistemic-discipline.md §"Source Reconciliation"` Class-(f) 4-band calibration; the plan §10 Step 8 estimate `≈ 4e-9` is a publication-precision pre-registration defect on the FORECAST-side, NOT on the canonical-promotion-side. **Classification: GEOMETRIC** (the dispute is over how a structural-derivation-chain pre-registration-estimate boundary maps to a substrate-first canonical-sourcing eligibility decision; the residual itself is a substrate-IS observable on the spectral triple `(A_K, H_K, D_K(τ_fold))`).

The substitution chain (orchestrator-side Python-verified):

```
Definition 1: ε := τ_fold/(5π)
Definition 2: c₀ ∈ {10, 5} per Conv-{A, B}
Definition 3: f(τ) := c₀/(1 − τ/(5π))           [substrate closed form]
Definition 4: anchor_residual := |f(τ_fold) − Richardson_anchor_at_L=14|
Definition 5: D_max := |log₁₀(actual_residual) − log₁₀(plan_pre_registered_estimate)|

Step 1 (Substitute Conv-A, τ=0.19):
  ε = 0.19/(5π) = 0.012095775674984046
  f_A(0.19) = 10/(1 − 0.012095775674984046) = 10.122438748384222862
  Richardson anchor (S87 W1B-HK-6) = 10.122386446
  anchor_residual_A = 5.230238e-05

Step 2 (Compute O(τ²) ceiling and O(τ³) prediction from §10 Step 6 Taylor expansion):
  O(τ²) bound (linear-LO upper limit) = ε² · c₀ = (0.012096)² · 10 = 1.463e-03
  O(τ³) prediction (geometric resummation) = ε³ · c₀ = (0.012096)³ · 10 = 1.770e-05

Step 3 (Locate actual residual relative to bracket):
  actual / O(τ²) bound = 5.230e-05 / 1.463e-03 = 0.0357  (≈ 28× below pure-linear ceiling)
  actual / O(τ³) pred = 5.230e-05 / 1.770e-05 = 2.9554   (≈ 3× above geometric-cubic prediction)

Step 4 (Compute D_max for the plan estimate ≈4e-9):
  D_max = |log₁₀(5.230e-05) − log₁₀(4e-09)| = |−4.282 − (−8.398)| = 4.117 OOM

Step 5 (Compare against Class-(f) 4-band calibration in epistemic-discipline.md):
   D_max < 0.1     → no rule-file action
   0.1 ≤ D_max < 1 → ADVISORY (S2)
   1 ≤ D_max < 3   → MANDATORY (S1) (halts plan-freeze)
   D_max ≥ 3.0     → HARD-HALT; manual review required

Step 6 (Read off): D_max = 4.12 ≥ 3.0 → HARD-HALT.

Direction (substrate → methodology, not the other way):
  The substrate is the spectral triple (A_K, H_K, D_K(τ_fold)). The Jensen-deformed
  closed form 10/(1−τ/(5π)) IS the substrate prediction; the Richardson L^{-3}
  Conclusion: the residual 5.23e-5 IS the magnitude of the O(τ²) Jensen-deformation
  correction (28× below pure-linear, 3× above geometric-cubic), which is a
  STRUCTURAL property of the substrate. The plan-pre-registered ≈4e-9 is NOT
  derivable from any term in §10 Steps 1–8; it appears to have been a forecast
  unanchored to the substitution chain. The HARD-HALT triggers ON THE PLAN ESTIMATE,
  not on the substrate canonical.
```

The HARD-HALT is on PRE-REGISTRATION COMPLIANCE; Class-(f) is on SUBSTRATE-FIRST-CANONICAL-EXISTENCE. **These are distinct rule-axes operating at distinct layers** of the layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"`: the HARD-HALT is at the methodology layer (rule-file pre-registration discipline); Class-(f) is at the substrate layer (where does the canonical value come from?). They do not adjudicate each other.

### Result II.2 — PRU Class 8.3 applicability scope: the rule applies to LOAD-BEARING DOWNSTREAM-CITED VALUES, NOT to forecast estimates whose only role is to set verdict-band boundaries

**Result**: Per `epistemic-discipline.md §"Publication-Precision Pre-Registration"` (Class 8.3 MANDATORY at K=4), the rule applies "when a gate's output VALUE will be cited downstream (in a follow-up gate's verifier, a canonical-constants entry, a registry row)". The plan-§10-Step-8 `≈ 4e-9` was a **threshold-side estimate** (used to define the boundary between PASS and INFO bands), NOT a value pinned for downstream citation. The closed-form numerical outputs `f_A(0.19) = 10.122438748384` and `f_B(0.19) = 5.061219374192` ARE downstream-cited (proposed for `update_constant("slope_A_FW_Conv_A", ...)` per WP §"Downstream consequences" line 238); these MUST carry Class 8.3 publication-precision pins. The K=4 calibration corpus (`epistemic-discipline.md §"Publication-Precision Pre-Registration" K=4 calibration corpus`) is on output VALUES (W1c-8 n_s, W2-4 cluster-span, W8-2 max_pair_ratio_A_5, W8-8 gv_canonical_difference, W13-3 R_842) not on threshold-side band estimates.

**Classification: GEOMETRIC** (rule-scope question on the methodology layer of F).

The plan §10 Step 8 estimate `≈ 4e-9` was structurally a **forecast at plan-authorship time** about the magnitude of the leading O(τ²) Jensen-deformation correction. It was NOT derived from any term in the substitution chain Steps 1–7. Two structurally distinct ways to read this:

1. The forecast was a typo, an off-by-many-orders rough scribble, or copied from an unrelated gate (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE territory if traceable; Class-8.1 plan-authoring defect if not).
2. The forecast was a genuine prediction made before doing the substitution chain Step 6 geometric-resummation step, expecting that a higher-order resolvent expansion would close the residual to numerical noise floor — a plan-authorship optimism that a more aggressive Cartan-orbit cancellation theorem would close the gap; this prediction was disconfirmed by §10 Step 6 itself (which explicitly tags the geometric resummation as "first order", not "to all orders").

Either way, the ROLE of the estimate was as a band-boundary forecast, NOT as a load-bearing downstream-cited value. Class 8.3's scope-clause "when a gate's output VALUE will be cited downstream" does not capture this case structurally; the plan §10 Step 8 estimate is a THRESHOLD definition, not an OUTPUT value.

### Result II.3 — The substrate-first canonical that Class-(f) routes through IS the closed-form expression `slope_A(τ) = c₀/(1 − τ/(5π))` itself, NOT the scalar `f_A(0.19) = 10.122438748384`

**Result**: Per `substrate-first-canonical-sourcing.md §(ii)` Step 4, "if the provenance cites a substrate-first computation (a `computations/_shared/sN_*.py` script or `computations/_shared/sN_*.npz` data file from the framework's own computation): emit AUDIT-PASS." The §W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e` IS such a substrate-first computation; the closed-form expression IS its substrate-first output (regulator-class invariant by construction; CC2 verifies zeta = Pauli-Villars = Mellin EXACT in Sage-symbolic). The Class-(f) PIN-PLACEHOLDER substitution `placeholder → substrate-canonical` discharges via promotion of the **closed-form expression** as the canonical, with `c_sub` and downstream chains consuming the parameterized form `slope_A_FW(τ) = c₀/(1 − τ/(5π))` rather than a scalar at one τ value.

**Classification: GEOMETRIC** (substrate-IS algebraic structure of the spectral triple at the Jensen flow level).

This reading aligns with how `branch-iv-canonical.md` already operates: branch-(iv) carries the parameterized form `w_0_FW_R842 = -0.842454` AND its scheme tag (`Volovik-partition-with-effacement-Γ=0.99970`) — the canonical IS the (value, scheme) tuple, not just the scalar (per agent memory: "Framework predictions are (value, scheme) tuples (S85 W1a F1)"). For W6a, the analogous tuple is `(slope_A_FW_Conv_A(τ), "geometric-resummation-of-CM1995-§III.4-first-order-resolvent-with-O(τ²)-INFO-caveat")`. Promoting the SCALAR `10.122438748384` to canonical_constants.py drops the regime-of-validity declaration; promoting the PARAMETERIZED FORM with its scheme-tag preserves the substrate-IS structural content.

### Result II.4 — Workshop 1's adjudication (geometric-resummation vs linear-LO) determines the SHAPE of the canonical promotion, NOT its eligibility

**Result**: Workshop 1 (per `_seed-w6a.md` lines 12–18) adjudicates whether `c₀/(1−τ/(5π))` is the substrate-IS exact closed form (lizzi reading: residual is high-order multi-root correction) or a first-order ANSATZ (connes reading: only linear form proven; geometric resummation is unjustified extrapolation pending second-order verification). The discriminating gate (the seed's CF-W6A-ADDITIONAL-C: τ = 2·τ_fold cross-validation) compares `4·5.23e-5 = 2.09e-4` (linear-LO scaling) vs `8·5.23e-5 = 4.18e-4` (geometric-resummation cubic scaling) at τ = 0.38.

**Classification: GEOMETRIC** (substrate-physics adjudication of analytic structure at the spectral triple level).

The Workshop-1 outcome decides the SHAPE of the slope_A_FW canonical entry:

- **If lizzi wins** (geometric resummation as substrate-IS structural identity, all-order valid): canonical_constants.py entry carries the parameterized closed form `slope_A_FW_Conv_A(τ) = 10/(1 − τ/(5π))` with regime-of-validity declaration `|τ| < 5π` and INFO-band O(τ³) caveat noting `|residual| ≲ 3·ε³·c₀` empirically calibrated at τ_fold.
- **If connes wins** (linear-LO ansatz only, geometric resummation is unproven extrapolation): canonical_constants.py entry carries the SCALAR `slope_A_FW_Conv_A_at_tau_fold = 10.122438748384` with explicit pin to τ = τ_fold = 0.19 ONLY, the parameterized form deferred to S89-or-later second-order resolvent gate `S89-JENSEN-DIM-SPECTRUM-HIGHER-ORDER-RESOLVENT`.
- **If neither wins decisively** (the τ = 2·τ_fold ratio falls in the INFO band of CF-W6A-ADDITIONAL-C, ratio ∈ (5, 7)): canonical_constants.py entry carries the closed form parameterized AND the linear-LO scalar AS SEPARATE ENTRIES (per the dual-canonical pattern of `w0_FW = -0.918` + `w0_FW_R842 = -0.842454`), each with its own scheme tag, and downstream consumption decides per-gate which to invoke.

In ALL three cases, the SUBSTRATE-FIRST CANONICAL EXISTS at S88-close (the §W6a-51 closed-form regulator-class-invariant expression IS substrate-first; the §W6a-52 (dim+rank)/2 prefactor IS substrate-first); only its DOWNSTREAM-CITED FORM depends on Workshop 1.

### Result II.5 — FWD-C1 unblocking is structurally LAYERED: SUBSTRATE-FIRST CANONICAL EXISTS at S88-close (W6a closes the existence axis); SHAPE of canonical depends on Workshop 1; PUBLICATION PRECISION on cited values is independent

**Result**: The FWD-C1 unblocking claim at WP §"Downstream consequences" line 238 + Wave Synthesis §4 line 791 is **CORRECT on the substrate-first-canonical-existence axis** but **INCOMPLETE on the canonical-shape axis**. Per the cross-pillar bridge anatomy (`cross-pillar-bridge-anatomy.md`) for FWD-C1 (Pillar I ↔ Pillar II per §"Three forward bridge candidates for S88+ dispatch"): the anatomy requires (1) substrate-IS observable, (2) laboratory-IN observable, (3) bridge map, (4) algebraic envelope, (5) empirical anchor. The §W6a-51 INFO landing supplies (1) `slope_A(τ_fold)` substrate-IS, (3) HKR L_max → ∞ bridge map, (4) O(τ²) algebraic envelope `≈ ε²·c₀ ≈ 1.46e-3`, (5) empirical anchor at residual `5.23e-5` < envelope; (2) is supplied by the Pillar-II laboratory-IN CMB observable `n_s` to which `c_sub` connects via the Mukhanov-Sasaki mode-function transfer in the substrate-first chain. The 5-anatomy IS WELL-FORMED at S88-close; FWD-C1 substrate-first canonical EXISTS.

**Classification: GEOMETRIC** (cross-pillar bridge anatomy at the structural-confidence-ladder level).

The Stage-1-CANDIDATE registry landing (carry-forward CF-3 `S89-JENSEN-DIM-SPECTRUM-CLOSED-FORM-STAGE-1-LANDING` from WP §8) is the natural next step; the Stage-2 cross-axis independent-verify (CF-4) is queued. The FWD-C1 retry gate (CF-6 `S89-FWD-C1-RETRY-WITH-SLOPE-A-CANONICAL`) consumes the Stage-1 Candidate text + canonical_constants.py promotion in whichever shape Workshop 1 produces.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | Source |
|:-----|:--------|:----------------|:-------|
| §W6a-51 `S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION` | **INFO** (sign=PASS · magnitude=INFO · regime=VALID) | `anchor_residual_A = 5.230238e-05` ∈ INFO-band [1e-9, 1e-3]; `regulator_invariance_residual = 0.000e+00` EXACT | WP §W6a-51, audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e` |
| §W6a-52 `S88-DIM-PLUS-RANK-OVER-2-PREFACTOR-DERIVATION` | **PASS** (sign=PASS · magnitude=PASS · regime=VALID) | `formula_residual = 0.000e+00` Sage-symbolic in ℚ[N]; SU(2)/SU(3)/SU(4) prefactors {2, 5, 9} match `(N−1)(N+2)/2` exactly | WP §W6a-52, audit_sha256 `05c4cabb0952bb27ef8466f2d068300866347f1b2d1b6e32b49578c1a9d34593` |

These verdicts are AUTHORITATIVE per the spawn-prompt rule "gate verdicts from source docs are authoritative — do not re-adjudicate." This synthesis adjudicates ONLY the META question of how INFO at the §W6a-51 landing maps to FWD-C1 unblocking under the cross-rule tension.

---

## IV. Structural Implications

### IV.1 — Adjudication: structurally LAYERED resolution, not winner-takes-all

The Workshop-3 framing posed a binary: mack reading (Class-(f) substitution sufficient at INFO) vs lizzi reading (HARD-HALT against pre-registration cannot be bypassed). The structurally-correct resolution is **NEITHER reading wins outright on its own axis; both are partially correct at non-overlapping layers**:

1. **Substrate-first axis (mack)**: Class-(f) substitution `placeholder → substrate-canonical` IS satisfied AT S88-close. The §W6a-51 closed-form expression IS the substrate-first canonical for `slope_A(τ_fold)`; regulator-class invariance EXACT (Sage-symbolic zeta = Pauli-Villars = Mellin) is the load-bearing structural property. **Mack reading prevails on the substrate-first-canonical-existence axis.**

2. **Pre-registration-compliance axis (lizzi)**: D_max = 4.12 OOM IS in the HARD-HALT band of `epistemic-discipline.md §"Source Reconciliation"` Class-(f) calibration. The plan §10 Step 8 estimate `≈ 4e-9` was structurally NOT derivable from the substitution chain. **Lizzi reading prevails on the publication-precision-pre-registration-discipline axis.**

3. **Canonical-shape axis (Workshop 1)**: whether the canonical entry is the parameterized closed form (lizzi-1 reading: geometric resummation as substrate-IS structural identity) vs the scalar at τ_fold only (connes-1 reading: linear-LO ansatz with deferred extrapolation) is independently adjudicated by Workshop 1. **Workshop 1 outcome determines the SHAPE; both winners produce a valid canonical.**

The three axes are STRUCTURALLY ORTHOGONAL per the algebra-axis orthogonality K-counter (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 from S87 W-2 R3 close): substrate-first-canonical-existence is algebra-INVARIANT (spectrum-only functional); publication-precision-pre-registration is methodology-layer (rule-file content under F); canonical-shape (geometric resummation vs linear LO) is algebra-DEPENDENT (state-pair functional on the deformation flow). They cannot adjudicate each other.

### IV.2 — Class 8.3 rule extension: FORECAST-vs-LOAD-BEARING calibration test

Per the seed Workshop 3 question (e): "should `epistemic-discipline.md §"Publication-Precision Pre-Registration"` be amended to exempt forecast-style estimates from PRU Class 8.3 applicability, drawing a clear line between LOAD-BEARING pins (downstream cites) and FORECAST pins (plan estimates not yet canonical)?"

**Adjudication**: The Class 8.3 scope-clause as written ("when a gate's output VALUE will be cited downstream") does not literally cover threshold-side band estimates; the existing K=4 calibration corpus (W1c-8 n_s, W2-4 cluster-span, W8-2 max_pair_ratio_A_5, W8-8 gv_canonical_difference, W13-3 R_842) is on output VALUES exclusively. **The rule does not need amendment to exempt forecast estimates; it already does so by scope construction.** What IS needed is a calibration corpus extension flagging this scope distinction explicitly, so future plan-authors do not confuse threshold estimates with output-value pins.

This rule extension routes through the standard K-counter discipline (`feedback_rules-compensate-missing-structure.md` K=3 MANDATORY threshold). The W6a-51 plan §10 Step 8 case becomes calibration-corpus-instance #1 of the FORECAST-vs-LOAD-BEARING distinction; promotion to MANDATORY waits for K=3 distinct instances.

### IV.3 — Constraint-map updates from this synthesis

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:--------------|:------------|:----------|:-------|
| 2026-05-07 | FWD-C1 substrate-first canonical existence | "BLOCKED on c_sub canonical W6_51 MISSING" (S88 W4 verdict) | "EXISTS at S88-close; SHAPE deferred to Workshop 1" | §W6a-51 closed-form regulator-class-invariant expression IS the substrate-first canonical; SHAPE of canonical_constants.py promotion depends on Workshop 1 adjudication |
| 2026-05-07 | Plan §10 Step 8 pre-registered residual estimate `≈ 4e-9` | LANDED at plan-freeze | RETROACTIVELY FLAGGED as forecast-style estimate (D_max = 4.12 OOM HARD-HALT against pre-registration; structurally undetermined by §10 substitution chain Steps 1–7) | Substitution-chain verification (this synthesis) shows neither linear-LO O(τ²) bound (1.46e-3) nor geometric-resummation O(τ³) prediction (1.77e-5) recovers `≈ 4e-9`; the estimate was an unstructured forecast |
| 2026-05-07 | Class 8.3 rule scope (FORECAST-vs-LOAD-BEARING distinction) | Implicit in scope-clause "output VALUE cited downstream" | Made explicit via this synthesis as calibration-corpus-instance #1; K=1 toward MANDATORY-extension threshold | The W6a-51 plan §10 Step 8 case is the first registered instance of a forecast estimate in HARD-HALT band; rule extension waits for K=3 |
| 2026-05-07 | FWD-C1 unblocking dependency chain | "INFO landing IS canonical-promotable" (mack original) vs "Workshop 1 must close first" (lizzi original) | "Substrate-first canonical EXISTS now; SHAPE depends on Workshop 1 (CF-3 STAGE-1-CANDIDATE)" | Three-axis decomposition (substrate-first-existence; publication-precision-discipline; canonical-shape) shows the readings address different axes; the dependency is on SHAPE not EXISTENCE |

### IV.4 — What this synthesis does NOT change

- **§W6a-51 INFO verdict is NOT disturbed**: the source docs verdict is authoritative; the substitution chain Step 8's pre-registered estimate `≈ 4e-9` was the wrong number, but the INFO-band routing of `5.23e-5 ∈ [1e-9, 1e-3]` is correct under the band as written.
- **§W6a-52 PASS verdict is NOT disturbed**: the formula residual `0.000e+00` Sage-symbolic in ℚ[N] is exact at machine zero; the (dim+rank)/2 prefactor identity is structurally PASS independent of any pre-registration question.
- **§W6a-52 canonical-constants.py promotion of `DIM_SU{2,3,4}`, `RANK_SU{2,3,4}`, `DELTA_PLUS_SU{2,3,4}`, `PREFACTOR_CONV_B_BASELINE_SU{2,3,4}` is NOT disturbed**: the K=4 publication-precision rule applied to these output-VALUE pins (Sage-symbolic exact integers; rel_tol structurally trivial); these are LOAD-BEARING pins and they correctly comply with Class 8.3 by being exact.
- **The §"Cross-gate algebraic chain `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)`"** load-bearing structural finding (synthesis line 761) is NOT touched here; that is Workshop 2's adjudication territory.

---

## V. Carry-Forward Computations

**MANDATORY — this section is the PRIMARY input to the next session's planning.** Five 4-field structured carry-forwards.

### V.1. Promote `slope_A_FW_Conv_A` and `slope_A_FW_Conv_B` to canonical_constants.py with explicit scheme tag and regime-of-validity declaration

- **What**: Add canonical entries via `mcp__knowledge__update_constant` for the closed-form Jensen dim-spectrum slope:
  - `slope_A_FW_Conv_A_param` = symbolic form `c₀/(1 − τ/(5π))` with `c₀ = 10` and regime `0 ≤ τ < 5π` (provenance: S88 W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e`; scheme `geometric-resummation-of-CM1995-§III.4-first-order-resolvent`; INFO-band O(τ²)-correction caveat).
  - `slope_A_FW_Conv_A_at_tau_fold` = scalar `10.122438748384` at τ = 0.19 (15 sig figs, full-float64; provenance same; rel_tol ≥ 1e-14 per Class 8.3 publication-precision pin).
  - Conv-B analogs: `slope_A_FW_Conv_B_param` = `c₀/(1 − τ/(5π))` with `c₀ = 5`; `slope_A_FW_Conv_B_at_tau_fold` = `5.061219374192`.
  - Doubling identity comment block: `slope_A_FW_Conv_A = 2 · slope_A_FW_Conv_B` (machine-zero residual; substrate-IS structural).
- **Inputs**: §W6a-51 closed-form expression; W1b-3 Richardson anchors `slope_∞_A = 10.122386446`, `slope_∞_B = 5.061193223` (S87-W1B-HK-6, S87-W1B-HK-5); `tau_fold = 0.19` from canonical_constants.py; SU(N) Lie-theory pins from §W6a-52 (`DIM_SU3 = 8`, `RANK_SU3 = 2`).
- **Gate**: `S89-SLOPE-A-FW-CANONICAL-CONSTANTS-PROMOTION` with PASS = (i) parameterized form AND scalar both land with explicit scheme tags AND regime-of-validity declarations; (ii) provenance entries cite audit_sha256 of §W6a-51 + cross-link to §W6a-52 prefactor canonicals; (iii) Class 8.3 publication-precision pin `pub_sig_figs = 15` on the scalar; (iv) scheme tag includes `INFO-band-O(τ²)-correction-caveat-magnitude=5.23e-5-at-tau_fold=0.19`. FAIL = scheme tag absent OR regime-of-validity declaration missing OR scalar pinned without full float64.
- **Effort**: 0.2 wave-equivalents (single canonical_constants.py edit + provenance entries; mack-cosmic-bridge sole-writer for the cross-link comment block referencing the falsifier-master-inventory row).

### V.2. Retroactive plan §10 Step 8 estimate audit (FORECAST-vs-LOAD-BEARING calibration corpus instance #1)

- **What**: Audit the plan §10 Step 8 pre-registered residual estimate `≈ 4e-9` against the substitution-chain-derived predictions (linear-LO O(τ²) bound = 1.46e-3; geometric-resummation O(τ³) prediction = 1.77e-5). The `≈ 4e-9` is structurally NOT recoverable from either; it appears to have been an unstructured forecast. Flag it as calibration-corpus-instance #1 of the FORECAST-vs-LOAD-BEARING distinction (extending `epistemic-discipline.md §"Publication-Precision Pre-Registration"` Class 8.3 K=4 calibration corpus). Per the user's "fix-in-session, never defer" rule (`feedback_fix-in-session-never-defer.md`), this audit IS in-session and produces a calibration-corpus row, NOT a deferred remediation. The structurally-correct routing: route the W6a-51 plan §10 Step 8 forecast as a calibration instance and continue. NO retroactive plan-edit (per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 3 post-hoc pre-registration editing).
- **Inputs**: W6a-51 plan §10 Steps 1–8 substitution chain; actual `anchor_residual_A = 5.230238e-05`; canonical Cartan-rational sum `Σ_α ⟨α,Y⟩²/|α|² = 1` on SU(3); ε = τ_fold/(5π) = 0.012096; c₀ ∈ {10, 5}; D_max = 4.12 OOM (this synthesis Python verification).
- **Gate**: `S89-W6A-51-PRE-REG-CLASS-8-3-FORECAST-CALIBRATION` with PASS criterion = substitution-chain Steps 1–8 verifies that `≈ 4e-9` is NOT a derivable term AND the calibration-corpus instance row is added to `epistemic-discipline.md §"Publication-Precision Pre-Registration"` K=4 calibration corpus as a NEW SUB-CLASS "FORECAST-vs-LOAD-BEARING" calibration instance #1; INFO criterion = the audit confirms forecast-status but the new-sub-class addition is deferred pending K=3 promotion threshold; FAIL = audit cannot establish forecast-status (the estimate IS in fact derivable from the substitution chain via a route this synthesis missed).
- **Effort**: 0.2 wave-equivalents (audit script + rule-file edit + calibration-corpus row append; orchestrator-direct-write per METHODOLOGY-class wave classification per `wave-classification.md` M1∧M2∧M3∧M4).

### V.3. CF-6 dependency declaration: `S89-FWD-C1-RETRY-WITH-SLOPE-A-CANONICAL` depends on Workshop 1 (geometric-resummation vs linear-LO) for canonical-shape selection

- **What**: Update the existing carry-forward CF-6 (`S89-FWD-C1-RETRY-WITH-SLOPE-A-CANONICAL`, WP §8 row 6) to declare an explicit dependency on Workshop 1 outcome (geometric-resummation vs linear-LO adjudication, the seed-w6a Workshop 1 + its discriminating CF-W6A-ADDITIONAL-C τ = 2·τ_fold cross-validation gate). The dependency is on the SHAPE of the canonical (parameterized closed form vs scalar at τ_fold vs dual-canonical pattern) NOT on the substrate-first-canonical-existence (which W6a closes).
- **Inputs**: WP §8 row 6 carry-forward 4-field spec for CF-6; seed-w6a Workshop 1 + CF-W6A-ADDITIONAL-C; this synthesis §IV.1 three-axis decomposition.
- **Gate**: `S89-CF-6-DEPENDENCY-DECLARATION-UPDATE` with PASS = CF-6 4-field spec updated to include "Depends on: Workshop 1 outcome via CF-W6A-ADDITIONAL-C verdict at τ = 2·τ_fold" in the §7 "Depends on" field per `output-standards.md §"Carry-Forward Dependency Enumeration (T1-14)"`; FAIL = dependency declaration drops Workshop 1 reference OR conflates SHAPE-axis with EXISTENCE-axis.
- **Effort**: 0.1 wave-equivalents (single-row WP edit; canonical-write-order Step 3 inventory-row landing concern routes to mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`).

### V.4. CF-3 STAGE-1-CANDIDATE registry text: include FORECAST-vs-LOAD-BEARING caveat in registry-row text

- **What**: When mack-cosmic-bridge sole-writer lands `S89-JENSEN-DIM-SPECTRUM-CLOSED-FORM-STAGE-1-LANDING` per WP §8 row 3 carry-forward at `sessions/permanent-results-registry.md §VII.{next-free-letter}` with STAGE-1-CANDIDATE tag, the registry-row text MUST include: (i) the closed-form expression `slope_A(τ) = c₀/(1 − τ/(5π))` with c₀ ∈ {10, 5}; (ii) the regime-of-validity `|τ| < 5π`; (iii) the INFO-band O(τ²)-correction caveat `|residual| ≲ 5.23e-5 at τ_fold = 0.19`; (iv) the explicit note "plan §10 Step 8 pre-registered estimate `≈ 4e-9` was structurally NOT derivable from the §10 substitution chain Steps 1–7; the estimate is forecast-style, NOT load-bearing-canonical-pin; per `epistemic-discipline.md §"Publication-Precision Pre-Registration"` Class 8.3 scope-clause 'when a gate's output VALUE will be cited downstream', the rule applies to output VALUES not threshold estimates"; (v) Stage-2 cross-axis independent-verify pending per CF-4. This is the FORECAST-vs-LOAD-BEARING calibration that downstream consumers (FWD-C1 retry; n_s and c_sub substitution chains) need to read off the registry text.
- **Inputs**: WP §8 row 3 4-field carry-forward; §W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e`; this synthesis §II.5 5-anatomy declaration; `cross-pillar-bridge-anatomy.md` §"Forward template-adoption" K-counter status (K=3 MANDATORY since S88 W4a-17 close).
- **Gate**: `S89-JENSEN-DIM-SPECTRUM-CLOSED-FORM-STAGE-1-LANDING` (= existing CF-3) with PASS criterion EXTENDED to include the forecast-vs-load-bearing caveat clauses (i)–(v); FAIL = caveat clauses absent OR registry-row conflates threshold-side estimate with output-value pin; INFO = caveat clauses present but corner-cell declaration per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-at-K=3 clause is INCOMPLETE.
- **Effort**: 0.3 wave-equivalents (mack-cosmic-bridge sole-writer registry edit; SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure per `registry-landing.md` for V_input (§W6a-51) + C_output (§W6a-52) cross-gate algebraic chain).

### V.5. CF-W6A-ADDITIONAL-C τ = 2·τ_fold cross-validation pinned as the discriminator for the SHAPE axis

- **What**: Promote the seed CF-W6A-ADDITIONAL-C (τ = 2·τ_fold cross-validation residual scan) from "spotted at investigator dispatch" status to the formal CF-7 carry-forward in S89 plan-freeze. The gate computes `slope_A_closed_form(0.38) = c₀/(1 − 0.38/(5π))` and the W1b-3-protocol Richardson `L^{−3}` extrapolation at τ = 0.38; computes `actual_residual_at_0.38 / actual_residual_at_0.19`; reads off SHAPE per the discriminator: ratio ≈ 4 → linear-LO reading wins → SCALAR-pin canonical SHAPE; ratio ≈ 8 → geometric-resummation reading wins → PARAMETERIZED-form canonical SHAPE; ratio ∈ (5, 7) → INFO band → DUAL-CANONICAL SHAPE. Output gates the SHAPE of the V.1 canonical_constants.py promotion AND the registry-row text of V.4.
- **Inputs**: §W6a-51 closed-form expression; spectrum cache regen at τ = 0.38 at L_max ∈ {10, 11, 12} (analogous to W1b-3 protocol at τ = 0.19); Richardson `L^{−3}` extrapolator from S87 W1B-HK-6; this synthesis §II.4 SHAPE-axis decomposition.
- **Gate**: `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD` with PASS-LINEAR criterion = `|ratio − 4| < 0.5`; PASS-GEOMETRIC criterion = `|ratio − 8| < 1.0`; INFO band = ratio ∈ (5, 7); FAIL = ratio outside both bands. Verdict feeds Workshop 1 adjudication (canonical-shape axis) AND CF-3 registry-row text shape-tag (V.4) AND CF-6 dependency-on-Workshop-1 (V.3).
- **Effort**: 1.0 wave-equivalents (spectrum cache regen at τ = 0.38 + Richardson extrapolation; structurally same as W1b-3 protocol but at a new τ point; substrate-distance-1 pole at s = 3 still applies via CM-1995 §III.4 + Friedrich-Bär saturation theorem per `math-scripts.md §"D_K Block-Diagonality Pre-Check"`).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| II.1 | D_max = 4.1165 OOM HARD-HALT band on plan estimate `≈4e-9`, NOT on substrate canonical | GEOMETRIC | confirmed via Python | HARD-HALT triggers on the FORECAST estimate side (methodology layer of F), not on the substrate-canonical-existence side; the two are structurally distinct under the layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"` |
| II.2 | PRU Class 8.3 scope: applies to LOAD-BEARING DOWNSTREAM-CITED VALUES, not to forecast-side band-boundary estimates | GEOMETRIC | rule-scope clarified (calibration-corpus instance #1) | The plan §10 Step 8 estimate is OUT-OF-SCOPE for Class 8.3 by literal-text reading; rule does not need amendment, only calibration-corpus extension; K=1 toward K=3 MANDATORY threshold |
| II.3 | The substrate-first canonical IS the closed-form expression (regime-of-validity declaration carried), NOT the scalar at one τ-value | GEOMETRIC | substrate-IS observable identified | canonical_constants.py promotion (V.1) carries (parameterized form, scalar-at-τ_fold) tuple per the dual-canonical pattern; aligns with branch-iv-canonical pattern and "(value, scheme) tuple" agent-memory discipline |
| II.4 | Workshop 1 outcome (geometric-resummation vs linear-LO) determines canonical SHAPE (parameterized vs scalar vs dual), NOT eligibility | GEOMETRIC | dependency declared in V.3 + V.5 | CF-6 (S89-FWD-C1-RETRY-WITH-SLOPE-A-CANONICAL) depends on Workshop 1 via CF-W6A-ADDITIONAL-C verdict at τ = 2·τ_fold; SHAPE selection forks at PASS-LINEAR / PASS-GEOMETRIC / INFO band |
| II.5 | FWD-C1 substrate-first canonical EXISTS at S88-close on the existence axis; layered structurally | GEOMETRIC | 5-anatomy elements all present in §W6a-51 | Stage-1-CANDIDATE registry landing (CF-3) is unblocked; Stage-2 cross-axis independent-verify (CF-4) queued; FWD-C1 retry (CF-6) gated on Workshop 1 SHAPE-selection verdict |
| IV.1 | Three-axis decomposition: substrate-first-existence (mack), publication-precision-discipline (lizzi), canonical-shape (Workshop 1) — STRUCTURALLY ORTHOGONAL | GEOMETRIC | adjudication closed | Workshop 3 binary-framing (mack vs lizzi) replaced with three-axis decomposition; both readings partially correct on different axes; algebra-axis orthogonality K-counter MANDATORY at K=3 (`cross-pillar-bridge-anatomy.md`) is the structural backdrop |
| IV.2 | Class 8.3 rule scope-clause already exempts forecast estimates by literal-text reading; calibration-corpus extension recommended (K=1 instance #1) | GEOMETRIC | rule extension queued | No rule amendment needed; calibration-corpus row added per V.2; K=3 MANDATORY-promotion threshold pending two more instances |
| IV.4 | §W6a-51 INFO and §W6a-52 PASS verdicts NOT disturbed by this synthesis | — | source-doc-authoritative respected | Per spawn-prompt rule "gate verdicts from source docs are authoritative — do not re-adjudicate"; this synthesis adjudicates ONLY the META cross-rule eligibility question |

---

## Appendix — Substitution Chain Verification (Python-checked, this synthesis 2026-05-07)

```
ε = τ/(5π) = 0.19 / (5 · 3.141592653589793) = 0.012095775674984046
fA(0.19) = 10 / (1 − 0.012095775674984046) = 10.122438748384222862
fB(0.19) =  5 / (1 − 0.012095775674984046) =  5.061219374192111431
anchor_A (W1b-3 Richardson L_max=14) = 10.122386446
anchor_B (W1b-3 Richardson L_max=14) =  5.061193223
anchor_residual_A = 5.230238e-05  (∈ INFO band [1e-9, 1e-3])
anchor_residual_B = 2.615119e-05  (∈ INFO band; doubling identity preserved 2:1)
ratio (resA/resB) = 2.000000        (machine zero; substrate-IS structural)

O(τ²) bound (linear-LO upper limit) = ε² · c₀ = (0.012096)² · 10 = 1.463078e-03
O(τ³) prediction (geom-resum cubic)  = ε³ · c₀ = (0.012096)³ · 10 = 1.769706e-05
actual / O(τ²) bound = 5.230e-05 / 1.463e-03 = 0.0357  (28× below pure-linear ceiling)
actual / O(τ³) pred  = 5.230e-05 / 1.770e-05 = 2.9554  (3× above geometric-cubic prediction)

Plan §10 Step 8 pre-registered estimate: ≈ 4e-9
D_max = |log₁₀(5.230e-05) − log₁₀(4e-09)| = |−4.282 − (−8.398)| = 4.1165 OOM

Class-(f) 4-band calibration (epistemic-discipline.md §"Source Reconciliation"):
   D_max < 0.1     → no rule-file action
   0.1 ≤ D_max < 1 → ADVISORY (S2)
   1 ≤ D_max < 3   → MANDATORY (S1) (halts plan-freeze)
   D_max ≥ 3.0     → HARD-HALT; manual review required

Reading: D_max = 4.12 ≥ 3.0 → HARD-HALT band on the PLAN ESTIMATE.
The HARD-HALT applies to PRE-REGISTRATION COMPLIANCE on the methodology layer of F.
The substrate-first-canonical-existence (Class-(f) substitution placeholder → substrate)
discharges INDEPENDENTLY at the substrate layer of F: regulator_invariance_residual = 0
EXACT (Sage-symbolic CC2) is the load-bearing structural property of the substrate
canonical, and the closed-form expression carries the substrate-IS regulator-invariance
by construction.
```

End of synthesis.
