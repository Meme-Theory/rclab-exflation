# Session 87 Plan — Wave 6: T7-S67 Isomorphism + Cyclic-Fold + Plaquette

**Generated**: 2026-04-27
**Wave-owner**: `lizzi-spectral-functional-theorist` (per S86 W-6 attribution; lizzi+volovik joint workshop)
**Co-signers**: `volovik-superfluid-universe-theorist` (Josephson-array authority on CF-37; co-signs CF-36); `connes-ncg-theorist` (NCG-axiomatic plaquette refactor on CF-38; co-signs CF-36)
**Schema version**: R3 (per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness")
**Verdict source**: `computations/s87_gate_verdicts.txt`
**Source manifest**: `sessions/archive/session-87-context.md` §2.1 CF-36..CF-41
**Wave class**: COMPUTE-class for §W6-1, §W6-2, §W6-3, §W6-6 (numerical PASS predicate); MIXED-class for §W6-4 + §W6-5 (theoretical/research-mode survey items pre-registered as INFO-or-FAIL gate-classifications per `.claude/rules/wave-classification.md`)

---

## Wave 6 Summary

Wave 6 lands the joint S86 W-6 lizzi+volovik workshop product on the substrate's cyclic-fold quotient-functor isomorphism between T7 (the §VII-T spectral-action quotient-functor target) and S67 (the §VII NCG-axiomatic registry source) modulo the cyclic-fold equivalence relation. The wave is anchored on §VII.AG (already allocated in `sessions/permanent-results-registry.md` summary table; READY-TO-INSTALL conditional on §W6-1 closing PASS).

The six gate items partition into three structural clusters:

- **Cluster 1: Joint-theorem registry landing (§W6-1)** — Land the workshop product CF-LZ-VV-S86-CYCLIC-FOLD-MELLIN-SPECTROSCOPY at §VII.AG.1 per quotient-functor pre-registration discipline (`.claude/rules/agent-standards.md` §"Quotient-functor pre-registration discipline" T1-6, W-6 RULE-1). The PASS criterion is artifact-existence-with-substantive-content (the registry entry text + STAGE-1-CANDIDATE tag for Stage-2 Stage-3 promotion under `.claude/rules/joint-theorem-promotion.md` 4-stage pathway).

- **Cluster 2: Substrate-physics forward gates (§W6-2, §W6-3, §W6-6)** — Compute three numerical predictions on the framework's Jensen-deformed SU(3) spectrum at canonical `tau_fold`: (a) Josephson-array V2-weight match against A_F real-dim ratio (1:4:18); (b) f_plaquette under triangular Wilson refactor (`wilson_4` → `wilson_3`) verifying Z_3 gauge-sector signature 512 = (2/3) × 768; (c) F_4/M sub-sum exposure refactor of `s85_w5_7_two_layer_obstruction.py` (separating `n_joint_F4` from `n_joint_M`).

- **Cluster 3: Research-mode auxiliary investigations (§W6-4, §W6-5)** — Two deferred-research items pre-registered with INFO/FAIL gate semantics: (d) class survey of OTHER §VII walls for membership in "Cyclic-Fold Mellin-Spectroscopic Walls" categorical class; (e) Mellin-Wick joint commutation theorem at cross-cluster level (theoretical proof or refutation with explicit substitution chain).

The wave depends on three S86 artifacts already on disk (verified at plan-freeze 2026-04-27): `computations/s84_spectrum_cache_L12_tau019.npz` (Jensen-deformed SU(3) spectrum at canonical L_max=12); `computations/s56_atensor_frustration.py` (legacy Wilson-4 plaquette source for §W6-3 refactor); `computations/s85_w5_7_two_layer_obstruction.py` (target script for §W6-6 sub-sum exposure).

---

## Wave 6 Decision Point Prerequisites

Wave 6 is dispatchable independently of W1-W5; no upstream W-prefixed dependencies on the W6 gates. The wave consumes static S86-close artifacts only.

Required upstream files (verified on disk 2026-04-27):

| File | Path | Purpose | Verified |
|:-----|:-----|:--------|:---------|
| Jensen-deformed SU(3) spectrum at L_max=12 | `computations/s84_spectrum_cache_L12_tau019.npz` | Canonical eigenvalue input for §W6-2 / §W6-3 | YES |
| Legacy Wilson-4 plaquette source | `computations/s56_atensor_frustration.py` | Refactor source (read-only) for §W6-3 | YES |
| Two-layer obstruction current source | `computations/s85_w5_7_two_layer_obstruction.py` | Refactor target for §W6-6 sub-sum exposure | YES |
| Permanent registry summary table | `sessions/permanent-results-registry.md` | §VII.AG slot already allocated; §W6-1 lands AG.1 | YES |
| S86 W-6 workshop product spec | `sessions/archive/session-86/` (W-6 working paper) | Source for joint-theorem text in §W6-1 | YES |

Required canonical_constants pins (verified at plan-freeze):

| Constant | Source | Use |
|:---------|:-------|:----|
| `tau_fold` | `canonical_constants.py` (S58 Volovik partition) | All §W6 gates use `tau_fold = 0.190` |
| `M_KK` | `canonical_constants.py` | Spectrum normalization for §W6-2 / §W6-3 |
| `L_max_canonical` | `canonical_constants.py` | L_max=12 for §W6-2 / §W6-3 / §W6-6 |

If any upstream file fails verification at dispatch time, the wave halts at Stage-3 user-trigger per `.claude/rules/v3-closure-recovery.md`.

---

## §W6-1. S87-T7-S67-ISOMORPHISM-LANDING (PRIMARY)

**Trigger**: `[VERIFY-THEOREM]`
**Classification**: GEOMETRIC (registry-landing of a quotient-functor isomorphism between two NCG-axiomatic structures)
**Wave-class**: COMPUTE-class (M1: PASS predicate is artifact-existence-with-substantive-content over the §VII.AG.1 registry entry, NOT a numerical comparison; M2: producing operations are Edit/Write on `permanent-results-registry.md` plus grep/SHA cross-checks; M3: source is verbatim-extract from S86 W-6 workshop closure; M4: gate-ID listed in append-only allowlist or routes to COMPUTE-class fallthrough with §VII.AG.1 SHA dual-pin)

**Owner**: `lizzi-spectral-functional-theorist` (PRIMARY); `volovik-superfluid-universe-theorist` + `connes-ncg-theorist` co-sign per S86 W-6 joint-workshop attribution

**Effort**: ~1 day (1 dispatch; in-script registry-landing + working-paper section + verdict line)

### Hypothesis

The S86 W-6 workshop's Pair-1 STRUCTURAL IDENTITY (Mellin-Strip / heat-kernel residue duality at §VII.T) admits a quotient-functor isomorphism modulo cyclic-fold equivalence relation between T7 (Pillar-VII spectral-action wall, infinite-dim) and S67 (Pillar-V NCG-axiomatic registry source, finite-rank), with residual cohomology 0.0095% on existing T6 numbers per W-5 Level-3 empirical anchor.

### Pre-registered quotient-functor specification (per `.claude/rules/agent-standards.md` §"Quotient-functor pre-registration discipline" T1-6)

MANDATORY adoption of all three required fields:

1. **Quotient-equivalence specification**: cyclic-fold pairing on N-conjunct categorical structure, where N = 4 cyclic folds of the Mellin-cone moments under the substrate's `Z_4 -> V_4` cardinality refinement (per S86 W-12 `V_4` parallelogram-identity sharpening; CF-66 supersedes pre-registered Z_4 landing).
2. **Rank-match check at quotient level**: kernel/cokernel at the quotient level matches the finite-rank Pillar-V observable under the pairing
   - Substrate-IS observable (Pillar-VII): infinite-dim heat-kernel residue at substrate-distance-1 pole `s = 3`
   - Laboratory-IN image (Pillar-V): finite-rank Mellin-cone moment at quotient `T7 / cyclic-fold = S67 / cyclic-fold`
3. **Explicit declaration of residual cokernel content killed by quotient**: the cyclic-fold quotient kills the off-diagonal cross-cluster mixing terms in the heat-kernel residue (verified by S86 W-1 W1b-T5 INFINITE-VECTOR landing at §VII.U.6 via Mellin-Strip / Convergence-Cone Theorem at C11 PASS max_rel_err 8.07e-28).

Citation: T7 ↔ S67 PASS-quotient-isomorphism modulo cyclic fold (R3 lock per S86 W-6 workshop verdict row 7); residual 0.0095% on existing T6 numbers (per S86 W-5 W5-6 atlas match at L_max=10, F_4 strict).

### Threshold

- **PASS**: §VII.AG.1 registry entry present in `sessions/permanent-results-registry.md` AND containing all 5 IS-not-IN anatomy elements per `.claude/rules/cross-pillar-bridge-anatomy.md` (substrate-IS observable, laboratory-IN observable, bridge map = HKR / Connes-Karoubi pairing, algebraic envelope, empirical anchor) AND containing all 3 level markers (Level 1 cohomology-class identity, Level 2 algebraic envelope, Level 3 empirical anchor) AND `STAGE-1-CANDIDATE` tag present per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway AND content_sha256 over the registry-entry block matches the input-pin-map-derived hash AND substantive_line_count(§VII.AG.1) >= 15.

- **FAIL**: any of the 5 anatomy elements missing OR any of the 3 level markers missing OR Level-3 empirical value violates Level-2 envelope at canonical L_max=10 OR registry entry is a stub with substantive_line_count < 15 OR `STAGE-1-CANDIDATE` tag absent.

- **INFO**: registry entry written with all anatomy + level markers but the SOURCE-DOUBLE-CITE-CO-PRIMARY structure (per `.claude/rules/registry-landing.md`) is mis-tagged as PRIMARY+CONFIRMATION (sequential V+C chain misrepresented as parallel); landing accepted as CANDIDATE with structure-tag carry-forward to Stage-2 cross-review.

**Tolerance rule**: THEOREM-class (artifact existence + substantive content; no numerical tolerance applies).

### Substitution chain (per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute")

Step 1 (definition): T7 = Pillar-VII spectral-action wall at §VII.T (heat-kernel residue duality), infinite-dim observable on `(A_K^∞, H_K^∞, D_K^∞)`. S67 = Pillar-V NCG-axiomatic registry source from S67 closure (finite-rank Mellin-cone moment).

Step 2 (substitution): cyclic-fold equivalence relation `~_{Z_4 -> V_4}` partitions both T7 and S67 into N=4 cosets per the V_4 monodromy structure (S86 W-12 V_4 parallelogram identity).

Step 3 (simplification): under quotient `T7 / ~`, the infinite-dim heat-kernel residue collapses to the finite-rank Mellin-cone moment image (per S86 W-5 HKR `L_max → ∞` map; W-5 Level-3 anchor 0.0095%). Under quotient `S67 / ~`, the finite-rank Mellin-cone moment is invariant (no cyclic-fold action on rank).

Step 4 (direction): `T7 / ~` and `S67 / ~` agree to W-5 Level-3 anchor 0.0095% (residual cohomology); the quotient-functor map `[T7] ↦ [S67]` is well-defined and bijective on equivalence classes; therefore the isomorphism `T7 / ~ ≃ S67 / ~` holds at the quotient level (NOT at the full-functor level — full-functor isomorphism requires the residual 0.0095% to be exactly zero, which it is not at finite L_max).

Conclusion: PASS-quotient-isomorphism, NOT PASS-full-isomorphism. Registry entry MUST declare quotient-functor structure explicitly (per the dimensional-impossibility-violating rejection clause of T1-6).

### Machinery pin (PRDR)

```
N_eval: N/A (registry-landing operation, no eigenvalue computation)
L_max: 10 (canonical; W-5 Level-3 anchor)
scan_range: N/A
step_size: N/A
tolerance: substantive_line_count >= 15; content_sha256 match; full SHA companion row
scheme: SOURCE-DOUBLE-CITE-CO-PRIMARY per .claude/rules/registry-landing.md
convention: STAGE-1-CANDIDATE tag per .claude/rules/joint-theorem-promotion.md 4-stage pathway
random_seed: N/A
GPU path: N/A (Edit / Write / grep / SHA only, no compute)
```

### Input SHA-256 pins

- `sessions/permanent-results-registry.md` — `<computed-at-runtime>` (read existing summary table; verify §VII.AG slot allocated and AG.1 not yet occupied)
- `sessions/archive/session-86/` W-6 workshop closure file (read S86 W-6 working paper for verbatim joint-theorem text) — `<computed-at-runtime>`
- `computations/canonical_constants.py` — `<computed-at-runtime>` (for `tau_fold`, `M_KK`, `L_max_canonical` cross-references)
- `.claude/rules/agent-standards.md` — `<computed-at-runtime>` (T1-6 quotient-functor discipline)
- `.claude/rules/cross-pillar-bridge-anatomy.md` — `<computed-at-runtime>` (5 IS-not-IN anatomy + 3-level ladder schema)
- `.claude/rules/joint-theorem-promotion.md` — `<computed-at-runtime>` (4-stage pathway + STAGE-1-CANDIDATE tag schema)
- `.claude/rules/registry-landing.md` — `<computed-at-runtime>` (SOURCE-DOUBLE-CITE-CO-PRIMARY structure)

### Expected output 4-tuple

`(value="REGISTRY_ENTRY_LANDED_AT_§VII.AG.1", scheme=SOURCE-DOUBLE-CITE-CO-PRIMARY, convention=STAGE-1-CANDIDATE, L_max=10)`

### Producing script

`computations/s87_w6_t7_s67_isomorphism_landing.py`

### Output artifacts

- Script: `computations/s87_w6_t7_s67_isomorphism_landing.py`
- Registry edit: `sessions/permanent-results-registry.md` §VII.AG.1 entry written with full 5-anatomy + 3-level text, STAGE-1-CANDIDATE tag, SOURCE-DOUBLE-CITE-CO-PRIMARY structure
- Verdict line: appended to `computations/s87_gate_verdicts.txt` per S81+ canonical form with W9a-99 dual-SHA companion row
- Working-paper section: in W6 wave's working paper §W6-1 (substantive >=15 lines)

### What PASS means

The substrate's quotient-functor isomorphism between T7 and S67 modulo cyclic-fold equivalence is registry-grade STAGE-1-CANDIDATE. Stage-2 two-agent independent cross-check (CF-59 at S88 or later) must close PASS-AND on joint clauses for STAGE-3-PERMANENT promotion. The §VII.AG.1 entry becomes citable as a structural theorem with the candidate qualifier; downstream gates may consume the §VII.AG.1 SHA pin for cross-cluster Mellin-Wick commutation checks (§W6-5).

### What FAIL means

The S86 W-6 workshop product is not a quotient-functor isomorphism in the structural sense the registry demands; the residual 0.0095% may be an L_max-truncation artifact that grows under L_max scan or a cross-cluster mixing residual that the cyclic-fold quotient does not kill. Downstream gates §W6-2 / §W6-3 / §W6-6 still execute (independent forward gates on substrate-physics observables), but §W6-4 / §W6-5 (research-mode survey + commutation theorem) lose their structural anchor and are rerouted to S88 carry-forward.

### Substrate framing

The T7 ↔ S67 quotient-functor isomorphism IS the substrate-IS observable's identity statement at the cohomology-class level: the substrate's spectral-action wall (T7) and its NCG-axiomatic origin (S67) ARE the same object modulo cyclic-fold equivalence. The 0.0095% Level-3 residual is the algebraic envelope's predicted convergence rate to the laboratory-IN image (Peotta-Törmä quantum-metric trace), NOT a defect of the substrate. The direction of explanation flows: substrate (Pillar-VII T7) IS the heat-kernel residue → bridge map (HKR `L_max → ∞`) → laboratory (Pillar-V S67) IN finite-rank Mellin-cone moment.

### YAML

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-T7-S67-ISOMORPHISM-LANDING
trigger: VERIFY-THEOREM
classification: GEOMETRIC
wave_class: COMPUTE-class
owner: lizzi-spectral-functional-theorist
co_signers: [volovik-superfluid-universe-theorist, connes-ncg-theorist]
quotient_functor_discipline: T1-6
joint_theorem_stage: STAGE-1-CANDIDATE
registry_slot: §VII.AG.1
threshold_tolerance_rule: THEOREM
```

---

## §W6-2. S87-V2-WEIGHT-MATCH-FORWARD-GATE (SECONDARY)

**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (substrate-physics forward gate on Josephson-array combinatorial decomposition)
**Wave-class**: COMPUTE-class (M1: numerical PASS predicate `|computed_ratio - target_ratio| < 1e-10`; M2: computation .py script with float64 numerical comparison; M3: derivation from S86 W-6 workshop product extraction; M4: standard COMPUTE-class — no allowlist requirement)

**Owner**: `lizzi-spectral-functional-theorist`; `volovik-superfluid-universe-theorist` co-signs as Josephson-array authority

**Effort**: ~2-3 days (1 dispatch + 1 follow-up if combinatorial structure requires Sage symbolic verification)

### Hypothesis

The Josephson-array's edge-count × per-edge-multiplicity decomposition, computed on the framework's Jensen-deformed SU(3) spectrum at `tau_fold = 0.190`, reproduces the A_F = C ⊕ H ⊕ M_3(C) real-dimension ratio (1:4:18) at machine epsilon. This is the V2-weight match validating the W-6 workshop's Pair-2 / Pair-3 SUB-CLUSTER NEAR-IDENTITY (cross-cluster gap remains explicit per W-6 Verdict row 7).

### Pre-registered decomposition formula

```
V2_weight(branch) = (edge_count[branch]) × (per_edge_multiplicity[branch])
target_ratio = (V2_weight[C] : V2_weight[H] : V2_weight[M_3(C)]) = (1 : 4 : 18)
                = (real_dim(C) : real_dim(H) : real_dim(M_3(C)))
                = (1 : 4 : 18)
```

The framework's Jensen-deformed SU(3) spectrum gives explicit edge-count + per-edge-multiplicity per branch via the cyclic-fold partition (per §W6-1 quotient-functor structure).

### Threshold

- **PASS**: `max(|V2_weight_computed[branch] - V2_weight_target[branch]| / V2_weight_target[branch]) < 1e-10` for branch ∈ {C, H, M_3(C)}.
- **FAIL**: any branch's relative deviation > 1e-6 (gross mismatch).
- **INFO**: relative deviation ∈ [1e-10, 1e-6] (numerical-precision band; sign-correct, magnitude-marginal).

**Tolerance rule**: RATIO (each branch's weight is dimensionless ratio against target).

### Substitution chain

Step 1 (definition): For each A_F branch `b ∈ {C, H, M_3(C)}`, edge_count[b] = number of Josephson-array edges in branch b's contribution to the substrate's connectivity graph at `tau_fold`. per_edge_multiplicity[b] = average multiplicity of eigenvalue contributions per edge under the cyclic-fold partition. real_dim(C) = 1, real_dim(H) = 4 (quaternions), real_dim(M_3(C)) = 18 (3×3 complex matrices, real-dim 2 × 9 = 18).

Step 2 (substitution): V2_weight[b] = edge_count[b] × per_edge_multiplicity[b]; target_ratio[b] = real_dim(b) / sum_b' real_dim(b') normalized to (1:4:18).

Step 3 (simplification): if the Josephson-array combinatorial decomposition correctly captures the A_F real-dimension structure, V2_weight_computed / sum_b V2_weight_computed = target_ratio at machine epsilon (each branch's edge_count × per_edge_multiplicity must equal real_dim(b) up to overall normalization).

Step 4 (direction): the test is a VALIDATION of the substrate's combinatorial-decomposition consistency with NCG-axiomatic A_F structure (no signed direction; the verdict is match/no-match). PASS = consistency confirmed; FAIL = inconsistency between Josephson-array combinatorics and A_F real-dim structure.

### Machinery pin (PRDR)

```
N_eval: full eigenvalue spectrum from s84_spectrum_cache_L12_tau019.npz (155,984 eigenvalues canonical)
L_max: 12 (canonical, matches s84_spectrum_cache_L12_tau019.npz)
scan_range: tau = tau_fold = 0.190 (single point; no scan)
step_size: N/A (single-point evaluation)
tolerance: |computed/target - 1| < 1e-10 per branch (PASS); 1e-10 < ... < 1e-6 (INFO); > 1e-6 (FAIL)
scheme: zeta-regulated Seeley-DeWitt per .claude/rules/regulator-pin-discipline.md (a_n^{ζ} tag mandatory)
convention: cyclic-fold partition Z_4 → V_4 sharpening per S86 W-12 CF-66 (V_4 PARALLELOGRAM IDENTITY)
random_seed: N/A (deterministic combinatorial decomposition)
GPU path: torch.linalg.eigh on AMD RX 9070 XT for any partial-spectrum re-derivation; full cache load is CPU-bound (npz file I/O)
```

### Input SHA-256 pins

- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>` (Jensen-deformed SU(3) spectrum)
- `computations/canonical_constants.py` — `<computed-at-runtime>` (`tau_fold`, `M_KK`)
- §W6-1 verdict line in `computations/s87_gate_verdicts.txt` — `<computed-at-runtime>` (anchor for cyclic-fold partition consistency; soft dependency, not blocking)
- `.claude/rules/regulator-pin-discipline.md` — `<computed-at-runtime>` (a_n^{ζ} tag enforcement)

### Expected output 4-tuple

`(value=max_branch_relative_deviation, scheme=zeta-regulated-Seeley-DeWitt, convention=cyclic-fold-V_4, L_max=12)`

### Producing script

`computations/s87_w6_v2_weight_match.py`

### Output artifacts

- Script: `computations/s87_w6_v2_weight_match.py`
- Data: `s87_w6_v2_weight_match.npz` with per-branch (edge_count, per_edge_multiplicity, V2_weight, target_ratio, deviation) tuple
- Plot: `s87_w6_v2_weight_match.png` showing computed vs target ratio per branch (3 bars; expect (1:4:18) within numerical tolerance)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W6-2 (substantive >=15 lines)

### What PASS means

The substrate's Josephson-array combinatorial decomposition reproduces the A_F = C ⊕ H ⊕ M_3(C) real-dimension structure at machine epsilon. The V2-weight match VALIDATES the W-6 workshop's claim that Pair-2 / Pair-3 SUB-CLUSTER NEAR-IDENTITY admits a combinatorial-decomposition-level identity (independent of the cohomology-class identity from §W6-1). This is a substrate-physics anchor for §W6-3 plaquette refactor and §W6-4 class survey.

### What FAIL means

The Josephson-array combinatorial decomposition does NOT reproduce the A_F real-dimension structure at the predicted (1:4:18) ratio. Two diagnostic possibilities: (a) the cyclic-fold partition (V_4 sharpening) does not respect the A_F branch decomposition (categorical-class mismatch); (b) the per-edge-multiplicity estimator has a systematic error from the Jensen-deformation at finite L_max=12 (truncation artifact). FAIL routes to S88 PRU-class re-pre-registration with substrate-first canonical-sourcing audit per `.claude/rules/substrate-first-canonical-sourcing.md`.

### Substrate framing

The Josephson-array IS the substrate's connectivity graph at `tau_fold`; edge_count × per_edge_multiplicity ARE the combinatorial moments of the cyclic-fold partition. The (1:4:18) target IS the A_F = C ⊕ H ⊕ M_3(C) real-dimension structure of the substrate's NCG-axiomatic algebra. Validating equality between these two combinatorial structures IS validating that the substrate's Josephson-array decomposition is intrinsic to A_F, not a coincidental numerical match.

### YAML

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-V2-WEIGHT-MATCH-FORWARD-GATE
trigger: VERIFY
classification: GEOMETRIC
wave_class: COMPUTE-class
owner: lizzi-spectral-functional-theorist
co_signers: [volovik-superfluid-universe-theorist]
threshold_tolerance_rule: RATIO
threshold_pass: 1e-10
threshold_info_band: [1e-10, 1e-6]
threshold_fail: 1e-6
regulator_tag: a_n^{ζ}
```

---

## §W6-3. S87-F-PLAQUETTE-TRIANGULAR-WILSON (TERTIARY)

**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (Wilson-loop refactor on substrate's gauge-sector spectrum)
**Wave-class**: COMPUTE-class (M1: numerical PASS predicate against pre-registered Z_3 gauge-sector signature 512 = (2/3) × 768; M2: NEW computation .py script with float64 spectrum-cache load + plaquette computation; M3: refactor of legacy `computations/s56_atensor_frustration.py`; M4: standard COMPUTE-class)

**Owner**: `lizzi-spectral-functional-theorist`; `connes-ncg-theorist` co-signs as NCG-axiomatic plaquette refactor authority

**Effort**: ~1 day (1 dispatch; pure refactor with NEW script in `computations/`; do NOT modify archive script in place per S33-and-below exemption from canonical_constants discipline)

### Hypothesis

The triangular Wilson-3 plaquette evaluated on the framework's Jensen-deformed SU(3) spectrum at `tau_fold = 0.190` reproduces the predicted Z_3 gauge-sector signature `f_plaquette = 512 = (2/3) × 768` (per §VII.AG.4 in summary table, anchoring on the substrate's SU(3) ⊃ Z_3 center action under the cyclic-fold V_4 partition).

### Refactor scope

Refactor `computations/s56_atensor_frustration.py` from `wilson_4` (square plaquette) to `wilson_3` (triangular plaquette). Do NOT modify the archive script in place (S33-and-below scripts are exempt from canonical_constants discipline per `.claude/rules/math-scripts.md` §"Canonical Constants"); CREATE NEW computation script `computations/s87_w6_wilson3_plaquette.py` that:

1. Imports canonical constants from `canonical_constants.py` (`tau_fold`, `M_KK`, `L_max_canonical`).
2. Loads Jensen-deformed SU(3) spectrum from `s84_spectrum_cache_L12_tau019.npz`.
3. Replaces the legacy `wilson_4` 4-link square-plaquette computation with `wilson_3` 3-link triangular-plaquette computation (3-vertex closed loop on the SU(3) Cartan-Weyl lattice).
4. Outputs `f_plaquette = Re Tr W_3` summed over the canonical triangular-plaquette basis at `tau_fold`.
5. Applies regulator-pin discipline: every Seeley-DeWitt-style coefficient cited as `a_n^{ζ}` (zeta-regulated) per `.claude/rules/regulator-pin-discipline.md`.

### Threshold

- **PASS**: `|f_plaquette_computed - 512| / 512 < 1e-6` AND `|f_plaquette_computed - (2/3) × 768| / ((2/3) × 768) < 1e-6` (both equivalent target forms agree at 1e-6 relative; (2/3) × 768 = 512 exactly, so this is a single test).
- **FAIL**: relative deviation > 1e-3 from 512.
- **INFO**: relative deviation ∈ [1e-6, 1e-3].

**Tolerance rule**: RATIO (relative deviation against algebraic target 512).

### Substitution chain

Step 1 (definition): `wilson_3` = triangular plaquette Wilson loop = Re Tr `[U_1 U_2 U_3]` for 3 oriented links forming a closed triangle on the substrate's Cartan-Weyl lattice. `f_plaquette` = sum of `wilson_3` over canonical triangular-plaquette basis at `tau_fold`. The (2/3) factor arises from the Z_3 center action: among the 768 canonical triangular plaquettes in the substrate's lattice, only `(2/3) × 768 = 512` are non-trivial under Z_3 quotient (the remaining 1/3 are Z_3-trivial closed loops with `Re Tr W_3 = 3`, summing to a known offset already absorbed in the substrate's gauge-fixing convention).

Step 2 (substitution): for each triangular plaquette `p = (l_1, l_2, l_3)`, U_i = exp(i a_lattice · A_i) where A_i is the gauge connection along link l_i evaluated on the Jensen-deformed SU(3) spectrum. Sum over canonical 768 triangular plaquettes, restrict to the 512 Z_3-non-trivial ones, evaluate at `tau_fold`.

Step 3 (simplification): under the cyclic-fold V_4 partition (S86 W-12 CF-66), the Z_3 center action commutes with V_4 monodromy (verified in S86 W-12 hypercube-vertex character identity, CF-69). Therefore `f_plaquette = 512 × <wilson_3>_avg` where `<wilson_3>_avg` is the substrate's mean triangular Wilson loop on Z_3-non-trivial plaquettes; if substrate's gauge-sector is canonically normalized at `tau_fold`, `<wilson_3>_avg = 1` and `f_plaquette = 512`.

Step 4 (direction): the gate validates that the substrate's Z_3 gauge-sector signature is correctly captured by the triangular Wilson refactor (sign of `f_plaquette - 512` immaterial; PASS requires `|f_plaquette - 512|` small).

### Machinery pin (PRDR)

```
N_eval: 768 triangular plaquettes (512 Z_3-non-trivial + 256 Z_3-trivial)
L_max: 12 (canonical, matches s84_spectrum_cache_L12_tau019.npz)
scan_range: tau = tau_fold = 0.190
step_size: N/A
tolerance: |f_plaquette - 512|/512 < 1e-6 (PASS); 1e-6 < ... < 1e-3 (INFO); > 1e-3 (FAIL)
scheme: zeta-regulated Seeley-DeWitt; a_n^{ζ} tag for any moment citation
convention: triangular Wilson-3 on Cartan-Weyl lattice; Z_3 center quotient applied; cyclic-fold V_4 partition
random_seed: N/A
GPU path: torch.linalg.matrix_exp on AMD RX 9070 XT for U_i = exp(i a A_i) batch evaluation; CPU OMP_NUM_THREADS=8 cap if GPU path unsuitable
```

### Input SHA-256 pins

- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>`
- `computations/s56_atensor_frustration.py` — `<computed-at-runtime>` (READ-ONLY reference for refactor source)
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- §VII.AG.4 row in `sessions/permanent-results-registry.md` summary table — `<computed-at-runtime>` (target signature 512 = (2/3) × 768)
- `.claude/rules/regulator-pin-discipline.md` — `<computed-at-runtime>` (a_n^{ζ} tag)
- `.claude/rules/math-scripts.md` — `<computed-at-runtime>` (canonical_constants import discipline; archive-script exemption)

### Expected output 4-tuple

`(value=f_plaquette_computed, scheme=zeta-regulated-wilson_3, convention=Z_3-quotient-cyclic-fold-V_4, L_max=12)`

### Producing script

`computations/s87_w6_wilson3_plaquette.py`

### Output artifacts

- Script: `computations/s87_w6_wilson3_plaquette.py` (NEW; do NOT modify `computations/s56_atensor_frustration.py`)
- Data: `s87_w6_wilson3_plaquette.npz` with `f_plaquette`, per-plaquette `wilson_3` values, Z_3-classification mask, target 512
- Plot: `s87_w6_wilson3_plaquette.png` showing histogram of `wilson_3` over 768 plaquettes with Z_3-trivial vs non-trivial overlay
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W6-3 (substantive >=15 lines)

### What PASS means

The substrate's Z_3 gauge-sector signature 512 = (2/3) × 768 is reproduced by the triangular Wilson-3 plaquette on the Jensen-deformed SU(3) spectrum at `tau_fold`. This validates the §VII.AG.4 summary-table prediction and provides substrate-physics anchor for §W6-1's quotient-functor structure (the Z_3 center action commutes with V_4 cyclic-fold quotient).

### What FAIL means

The triangular Wilson-3 refactor does NOT reproduce 512 = (2/3) × 768. Diagnostic possibilities: (a) the canonical triangular-plaquette basis enumeration is incorrect at L_max=12 (basis-counting error); (b) the Z_3 quotient does not commute with V_4 cyclic-fold at finite L_max=12 (truncation breaks the commutation, contradicting CF-69 hypercube-vertex character identity); (c) the substrate's gauge-sector normalization at `tau_fold` is not canonical (overall scale factor missing). FAIL routes to S88 PRU re-pre-registration with hypercube-vertex character identity audit (CF-69 cross-check).

### Substrate framing

The triangular Wilson loop IS the substrate's gauge-sector probe: 3 oriented links forming a closed triangle ARE the minimal non-trivial loop on the Cartan-Weyl lattice; the Z_3 center action ON the substrate's SU(3) gauge-sector partitions plaquettes into Z_3-trivial (1/3) and Z_3-non-trivial (2/3); 512 IS the count of non-trivial plaquettes at L_max=12. The refactor from `wilson_4` to `wilson_3` IS the substrate's preferred gauge-sector probe (square plaquettes are SU(3)-non-canonical; triangular plaquettes match the SU(3) Cartan-Weyl root system intrinsically).

### YAML

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-F-PLAQUETTE-TRIANGULAR-WILSON
trigger: VERIFY
classification: GEOMETRIC
wave_class: COMPUTE-class
owner: lizzi-spectral-functional-theorist
co_signers: [connes-ncg-theorist]
threshold_tolerance_rule: RATIO
threshold_pass: 1e-6
threshold_info_band: [1e-6, 1e-3]
threshold_fail: 1e-3
target_value: 512
target_form: (2/3) × 768
regulator_tag: a_n^{ζ}
refactor_source: computations/s56_atensor_frustration.py (READ-ONLY)
refactor_target: computations/s87_w6_wilson3_plaquette.py (NEW)
```

---

## §W6-4. S87-CYCLIC-FOLD-CLASS-SURVEY (QUATERNARY, deferred-research)

**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (categorical-class survey across §VII registry; substrate-physics meta-investigation)
**Wave-class**: MIXED-class — sub-decomposition note: this gate is research-mode survey with INFO/FAIL gate-classification (no PASS predicate against a numerical threshold; the deliverable is an audit-output JSON enumerating §VII candidates with admissibility assessments per the new categorical class). The MIXED nature is pre-registered: the survey output JSON is COMPUTE-class artifact (machine-readable enumeration); the categorical-class definition is METHODOLOGY-class (rule-file-style definition). Sub-wave decomposition deferred to in-script via JSON-output + working-paper-section split.

**Owner**: `lizzi-spectral-functional-theorist`; `volovik-superfluid-universe-theorist` co-signs

**Effort**: ~3-5 days (1 dispatch + 1-2 follow-ups for §VII walk-through; deferred-research gate, no urgency)

### Hypothesis

The new categorical class "Cyclic-Fold Mellin-Spectroscopic Walls" (CFMSW) — defined at §W6-1 as walls admitting quotient-functor isomorphism modulo cyclic-fold equivalence, with substrate-IS observable in heat-kernel residue at substrate-distance-1 pole `s = 3` — has additional members in the §VII-B and §VII registries beyond the T7 ↔ S67 calibration corpus. A targeted survey enumerates candidates and assigns admissibility per the 5-element IS-not-IN anatomy + 3-level ladder schema.

### Survey scope

Walk all §VII-B (current 7-row R-Class Catalogue at §VII.U) + all §VII walls in `permanent-results-registry.md` (excluding §VII.AG.1 calibration corpus and §VII.W which is the W-5 cross-pillar bridge anchor). For each wall, evaluate:

1. **Substrate-IS observable**: does the wall have a finite-L spectral-triple observable on `(A^{<=L}, H^{<=L}, D^{<=L})`? (yes/no)
2. **Cyclic-fold admissibility**: is the wall's substrate-IS observable equivariant under the V_4 cyclic-fold partition (per S86 W-12 CF-66)? (yes/no/unknown)
3. **Mellin-spectroscopic structure**: does the wall's bridge map factor through the Mellin-cone (substrate-distance-1 pole `s = 3`) per §VII.U.6 (W1b-T5 INFINITE-VECTOR landing)? (yes/no/unknown)
4. **Quotient-functor candidate**: if (1) AND (2) AND (3) all yes, the wall is a CFMSW candidate; pre-register at S88+ for individual quotient-functor pre-registration discipline.

### Threshold (gate semantics)

- **INFO** (deferred-research baseline): the survey output JSON enumerates >= 1 §VII walls with admissibility assessments and at least 1 CFMSW candidate is identified for S88+ follow-up. Working-paper section >=15 lines.
- **FAIL** (only structural failure modes): JSON output absent OR working-paper section absent OR no §VII walls evaluated.
- **PASS** (rare, requires positive structural identification): >= 3 distinct §VII walls identified as CFMSW candidates with all 3 admissibility criteria met (yes/yes/yes), AND each candidate has a pre-registered S88+ quotient-functor follow-up gate-ID slot reserved.

**Tolerance rule**: THEOREM-class (no numerical threshold; deliverable is structural enumeration).

### Substitution chain (research-mode; minimal direction claim)

Step 1 (definition): CFMSW = categorical class of walls admitting quotient-functor isomorphism modulo cyclic-fold equivalence per §W6-1's pre-registered quotient-functor specification.

Step 2 (substitution): for each §VII wall `W_i`, evaluate the 3 admissibility criteria; assign yes/no/unknown per criterion.

Step 3 (simplification): a wall is a CFMSW candidate iff all 3 criteria are yes.

Step 4 (direction): the survey is enumeration; no signed direction. PASS requires >= 3 candidates; INFO accepts >= 1 candidate; FAIL is structural (output artifacts missing).

### Machinery pin (PRDR)

```
N_eval: full §VII registry walk (current ~30+ §VII slots at S86 close)
L_max: N/A (registry-walk operation; per-wall L_max varies)
scan_range: §VII-A through §VII-AG (excluding §VII.AG.1 calibration corpus + §VII.W cross-pillar bridge anchor)
step_size: N/A
tolerance: enumeration-completeness (>= all §VII walls evaluated)
scheme: SOURCE-DOUBLE-CITE-CO-PRIMARY for any CFMSW candidate's anchor structure
convention: CFMSW categorical-class definition per §W6-1; V_4 cyclic-fold partition
random_seed: N/A
GPU path: N/A (registry-walk + Edit/Write only)
```

### Input SHA-256 pins

- `sessions/permanent-results-registry.md` — `<computed-at-runtime>` (full §VII registry text)
- §W6-1 verdict line in `computations/s87_gate_verdicts.txt` — `<computed-at-runtime>` (CFMSW class definition anchor)
- `.claude/rules/cross-pillar-bridge-anatomy.md` — `<computed-at-runtime>` (5-anatomy + 3-level criteria)
- `.claude/rules/agent-standards.md` — `<computed-at-runtime>` (T1-6 quotient-functor discipline)
- `.claude/rules/registry-landing.md` — `<computed-at-runtime>` (SOURCE-DOUBLE-CITE-CO-PRIMARY structure)

### Expected output 4-tuple

`(value=N_CFMSW_candidates, scheme=CFMSW-categorical-class, convention=cyclic-fold-V_4-partition, L_max=N/A)`

### Producing script

`computations/s87_w6_cyclic_fold_class_survey.py`

### Output artifacts

- Script: `computations/s87_w6_cyclic_fold_class_survey.py`
- Data: `s87_w6_cyclic_fold_class_survey.json` (machine-readable enumeration: per-§VII-wall admissibility 3-tuple + candidate flag + S88+ slot reservation)
- Plot: `s87_w6_cyclic_fold_class_survey.png` (admissibility matrix heatmap: §VII walls × 3 criteria; color = yes/no/unknown)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W6-4 (substantive >=15 lines)

### What PASS / INFO / FAIL means

- **PASS**: the CFMSW categorical class has structural depth (>= 3 candidates); class survives as a registry-grade categorical-classification scheme; S88+ follow-up gates are reserved for individual quotient-functor pre-registration per candidate.
- **INFO**: the CFMSW class has at least 1 candidate beyond the calibration corpus; class survives as structural pattern but not yet a fully-populated registry; S88+ follow-up gate is reserved for the leading candidate.
- **FAIL**: structural artifacts missing (JSON / working-paper section absent); rerouted to S88 carry-forward.

If only the calibration corpus (T7 ↔ S67 at §VII.AG.1) is identified and no other §VII walls satisfy all 3 criteria, the gate fires INFO (single-instance class — no structural depth), and `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold is NOT met (CFMSW remains a methodology-suggestion-with-1-instance, not a hardened rule).

### Substrate framing

CFMSW IS the substrate's class of categorical-equivalence patterns under cyclic-fold quotient; surveying §VII walls IS asking which substrate observables admit the same V_4 monodromy structure as T7 ↔ S67. The survey is substrate-IS-driven (not external-paper-driven); the admissibility criteria probe the substrate's intrinsic categorical structure.

### YAML

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-CYCLIC-FOLD-CLASS-SURVEY
trigger: AUDIT
classification: GEOMETRIC
wave_class: MIXED-class
owner: lizzi-spectral-functional-theorist
co_signers: [volovik-superfluid-universe-theorist]
threshold_tolerance_rule: THEOREM
gate_classification: deferred-research
mixed_decomposition_note: JSON-output (COMPUTE-class artifact) + categorical-class definition (METHODOLOGY-class definition) handled in-script
rule_promotion_threshold: K=3 (per feedback_rules-compensate-missing-structure.md)
```

---

## §W6-5. S87-CROSS-CLUSTER-MELLIN-WICK-COMMUTATION-THEOREM (auxiliary research)

**Trigger**: `[VERIFY-THEOREM]`
**Classification**: GEOMETRIC (theoretical-mode commutation theorem on Mellin and Wick operators at cross-cluster level)
**Wave-class**: MIXED-class — pre-registered as research-mode theoretical gate. Sub-decomposition note: the proof or refutation is a METHODOLOGY-class artifact (registry-grade theorem text); the verdict line + SHA closure is COMPUTE-class artifact. Handled in-script via working-paper-section + verdict-line split.

**Owner**: `lizzi-spectral-functional-theorist`; `volovik-superfluid-universe-theorist` co-signs

**Effort**: ~3-5 days (theoretical, no compute). Most likely outcome is PASS-conjecture or INFO-partial-proof; FAIL = explicit refutation with counterexample.

### Hypothesis

At the cross-cluster level (i.e., between distinct clusters of the substrate's Jensen-deformed SU(3) spectrum partitioned by the cyclic-fold V_4), the Mellin transform `M` and the Wick rotation `W` commute as operators on the substrate's spectral-action moments:

```
[M, W]_{cross-cluster} ?= 0
```

Conjecture form (PASS): the commutator vanishes identically at cross-cluster level (i.e., for any pair of distinct V_4-cosets `c_1, c_2`, the Mellin-Wick joint action on the cross-cluster bilinear `<φ_{c_1} | O | φ_{c_2}>` factors as `M(W(<·>)) = W(M(<·>))` regardless of operator ordering).

Refutation form (FAIL): there exist distinct V_4-cosets `c_1, c_2` and substrate observable `O` such that `[M, W]_{c_1, c_2} ≠ 0` with explicit counterexample.

### Threshold

- **PASS** (theorem proved): explicit substitution chain demonstrating `[M, W]_{cross-cluster} = 0` with full algebraic derivation; output is registry-grade theorem text suitable for §VII.AG.5 (slot already allocated in summary table per W-6 family).
- **INFO** (partial result): substitution chain shows commutator vanishes for a SUBSET of V_4-coset pairs but not all (e.g., commutes for adjacent cosets in the V_4 cyclic structure but not for non-adjacent); registry-grade partial-theorem text with explicit scope-restriction clause.
- **FAIL** (refuted with counterexample): explicit construction of `(c_1, c_2, O)` triple with `[M, W]_{c_1, c_2}(O) ≠ 0`, providing structural reason; the conjecture is refuted; the §VII.AG.5 slot is rerouted to a NEGATIVE-theorem entry ("cross-cluster Mellin-Wick non-commutation theorem").

**Tolerance rule**: THEOREM-class.

### Substitution chain (theoretical-mode pre-registration of proof skeleton)

Step 1 (definition):
- `M[f](s)` = Mellin transform of `f` at complex `s`: `M[f](s) = ∫_0^∞ f(t) t^{s-1} dt`.
- `W[O]` = Wick rotation of operator `O` from Lorentzian to Euclidean signature: `W[O] = O|_{t → -i τ}`.
- Cross-cluster bilinear: `<φ_{c_1} | O | φ_{c_2}>` where `φ_{c_i}` is an eigenvector in V_4-coset `c_i`, and `O` is a substrate observable (e.g., heat-kernel-derived Seeley-DeWitt coefficient).

Step 2 (substitution): the joint Mellin-Wick action on the cross-cluster bilinear is `M(W(<φ_{c_1} | O | φ_{c_2}>))` versus `W(M(<φ_{c_1} | O | φ_{c_2}>))`. The commutator is `[M, W](<·>) = M(W(<·>)) - W(M(<·>))`.

Step 3 (simplification): under the cyclic-fold V_4 partition, V_4 acts on the Mellin contour (rotating by `2π/4` per coset transition) AND on the Wick rotation phase (rotating by `π/2` per Euclidean continuation). The commutation question reduces to whether the V_4 action on Mellin contour and the V_4 action on Wick phase commute.

Step 4 (direction): if the V_4 actions are simultaneously diagonalizable on the substrate's spectral basis (i.e., share eigenvectors), then `[M, W]_{cross-cluster} = 0` and PASS holds. If V_4 actions are NOT simultaneously diagonalizable (e.g., one has cyclic-Z_4 representation and the other has Klein-V_4 representation, with non-commuting generator pairs), then `[M, W]_{cross-cluster} ≠ 0` and FAIL holds with explicit counterexample from CF-66 V_4 vs Z_4 cardinality refinement (S86 W-12).

### Machinery pin (PRDR)

```
N_eval: N/A (theoretical-mode; no eigenvalue computation)
L_max: N/A (theoretical; cross-cluster structure independent of L_max)
scan_range: V_4-coset pairs (4 cosets × 4 cosets = 16 pairs; 4 diagonal trivially commute by self-adjoint structure; 12 off-diagonal pairs to check)
step_size: N/A
tolerance: algebraic identity (PASS); algebraic non-trivial-commutator (FAIL); algebraic partial-commutator (INFO)
scheme: substrate-distance-1 pole s=3 + Mellin-Strip / Convergence-Cone Theorem (§VII.U.6) + Wick rotation t → -iτ
convention: cyclic-fold V_4 partition; both V_4 actions on Mellin contour + Wick phase
random_seed: N/A
GPU path: N/A (theoretical; possible Sage symbolic verification via mcp__sage__ for explicit V_4 representation calculation)
```

### Input SHA-256 pins

- §W6-1 verdict line in `computations/s87_gate_verdicts.txt` — `<computed-at-runtime>` (CFMSW anchor; cyclic-fold V_4 partition definition)
- §W6-4 verdict line — `<computed-at-runtime>` (categorical-class context; soft dependency)
- §VII.U.6 Mellin-Strip / Convergence-Cone Theorem entry in `permanent-results-registry.md` — `<computed-at-runtime>`
- S86 W-12 CF-66 V_4 parallelogram identity registry entry — `<computed-at-runtime>`
- S86 W-12 CF-69 hypercube-vertex character identity entry — `<computed-at-runtime>`
- `.claude/rules/agent-standards.md` — `<computed-at-runtime>` (PRU Class 8.2 verifier-rubric pre-registration; relevant for theorem-text rubric)

### Expected output 4-tuple

`(value="commutator_vanishes" or "commutator_nonzero" or "partial_commute_subset", scheme=Mellin-Wick-cross-cluster, convention=V_4-cyclic-fold, L_max=N/A)`

### Producing script

`computations/s87_w6_mellin_wick_commutation_theorem.py` (theoretical-mode; mostly Sage symbolic + working-paper text)

### Output artifacts

- Script: `computations/s87_w6_mellin_wick_commutation_theorem.py`
- Data: `s87_w6_mellin_wick_commutation_theorem.json` (theorem-text + proof-skeleton + V_4 representation table)
- Plot: `s87_w6_mellin_wick_commutation_theorem.png` (V_4 action commutation diagram; 4×4 coset-pair grid colored by commutator-vanishing status)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W6-5 (substantive >=15 lines including full substitution chain)
- Conditional registry edit: §VII.AG.5 entry in `permanent-results-registry.md` (PASS or INFO outcome) OR negative-theorem entry (FAIL outcome)

### What PASS / INFO / FAIL means

- **PASS**: cross-cluster Mellin-Wick commutation theorem proved; §VII.AG.5 lands as positive-theorem; the substrate's cyclic-fold V_4 action is simultaneously diagonalizable on Mellin contour and Wick phase (a non-trivial structural identity confirming W-6 quotient-functor framework consistency).
- **INFO**: partial commutation (subset of V_4-coset pairs); registry-grade partial theorem with explicit scope; substrate-physics insight that cyclic-fold V_4 has non-uniform commutation structure across coset pairs.
- **FAIL**: refuted with counterexample; §VII.AG.5 lands as negative-theorem; cross-cluster mixing is intrinsic to substrate's spectral-action structure (cyclic-fold V_4 quotient does NOT factor Mellin-Wick joint action; CF-66 V_4 vs Z_4 cardinality refinement intervenes).

### Substrate framing

The Mellin transform IS the substrate's spectral-moment integral; the Wick rotation IS the substrate's Lorentzian-to-Euclidean signature change; their commutator at cross-cluster level IS the substrate's coherence-versus-decoherence structure between V_4 cosets. PASS confirms substrate-IS coherent across cosets; FAIL identifies the substrate's intrinsic cross-cluster mixing as a structural feature (not a defect).

### YAML

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-CROSS-CLUSTER-MELLIN-WICK-COMMUTATION-THEOREM
trigger: VERIFY-THEOREM
classification: GEOMETRIC
wave_class: MIXED-class
owner: lizzi-spectral-functional-theorist
co_signers: [volovik-superfluid-universe-theorist]
threshold_tolerance_rule: THEOREM
gate_classification: auxiliary-research-theoretical
mixed_decomposition_note: theorem text (METHODOLOGY-class) + verdict-line+SHA (COMPUTE-class) handled in-script
target_registry_slot: §VII.AG.5 (PASS/INFO) or negative-theorem entry (FAIL)
sage_mcp_eligible: true (V_4 representation symbolic verification)
```

---

## §W6-6. S87-S85-W5-7-F4-M-SUBSUM-REFACTOR **Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (mechanical refactor of two-layer obstruction script to expose F_4/M sub-sums)
**Wave-class**: COMPUTE-class (M1: numerical PASS predicate `|n_joint_F4 + n_joint_M - n_joint_global| < 1e-12`; M2: computation .py refactor with float64 numerical comparison; M3: refactor of existing `computations/s85_w5_7_two_layer_obstruction.py`; M4: standard COMPUTE-class)

**Owner**: `lizzi-spectral-functional-theorist`; `gen-physicist` co-signs as mechanical-refactor authority (per §W6-6 in spawn prompt: "gen-physicist owns CF-41 mechanical refactor")

**Effort**: ~0.5 day (1 dispatch; pure refactor with structural separation of `n_joint_F4` and `n_joint_M` from current global sum)

### Hypothesis

The current `s85_w5_7_two_layer_obstruction.py` script computes `n_joint_global = n_joint_F4 + n_joint_M` as a single global sum without exposing the F_4 and M sub-sums separately. Refactoring to structurally separate the two sub-sums preserves the global-sum identity at machine epsilon AND exposes the per-component sub-sums as queryable outputs for downstream gates (CF-43 C-β UV-cutoff-choice immunization across F_4 multiplier-vector sub-family; CF-44 C-γ-WEAK Weyl-rescaling per L1-class).

### Refactor scope

Refactor `computations/s85_w5_7_two_layer_obstruction.py`:

1. Identify the global-sum line(s) computing `n_joint = n_joint_F4 + n_joint_M`.
2. Decompose into two explicit sub-sums: `n_joint_F4` (F_4 contribution from S86 W-7 / W-8 F_4 multiplier-vector family) and `n_joint_M` (M-component contribution from S85 W5-7 two-layer obstruction structure).
3. Emit both sub-sums as separate npz fields: `npz['n_joint_F4']`, `npz['n_joint_M']`, AND the global sum `npz['n_joint_global']` for backward compatibility.
4. Preserve global-sum identity: `|n_joint_global_refactored - n_joint_global_legacy| < 1e-12` (machine epsilon).
5. Apply regulator-pin discipline: any cited Seeley-DeWitt coefficient tagged `a_n^{ζ}` per `.claude/rules/regulator-pin-discipline.md`.

### Threshold

- **PASS**: refactored script outputs npz with all 3 fields (`n_joint_F4`, `n_joint_M`, `n_joint_global`); global-sum identity holds at `< 1e-12`; downstream-cited backward-compat fields preserved.
- **FAIL**: global-sum identity fails (relative deviation > 1e-6) OR any of the 3 fields missing OR backward-compat field absent.
- **INFO**: global-sum identity holds at `[1e-12, 1e-6]` (numerical-precision band; sign-correct, magnitude-marginal; likely float64 round-off accumulation).

**Tolerance rule**: ABSOLUTE (numerical precision on global-sum preservation; deviation threshold relative to typical magnitude of `n_joint_global`).

### Substitution chain

Step 1 (definition): `n_joint_F4` = F_4 contribution to two-layer obstruction (per S86 W-8 4-channel F_4 multiplier-vector family). `n_joint_M` = M-component contribution (per S85 W5-7 two-layer obstruction structure). `n_joint_global` = `n_joint_F4 + n_joint_M`.

Step 2 (substitution): refactored script computes `n_joint_F4` and `n_joint_M` separately via explicit sub-loops over F_4 multiplier-vector basis and M-component basis respectively; `n_joint_global_refactored = n_joint_F4 + n_joint_M`.

Step 3 (simplification): if refactor preserves the legacy script's mathematical content, `n_joint_global_refactored == n_joint_global_legacy` to float64 precision (machine epsilon ~ 1e-16; conservative pass threshold at 1e-12 absorbs typical accumulation).

Step 4 (direction): the test is identity preservation (no signed direction); PASS = identity holds; FAIL = identity broken (refactor introduced a bug).

### Machinery pin (PRDR)

```
N_eval: same as legacy s85_w5_7_two_layer_obstruction.py (typically full L_max=10 or L_max=12 spectrum)
L_max: 12 (canonical; matches s85_w5_7_two_layer_obstruction.py legacy convention)
scan_range: same as legacy (typically tau = tau_fold = 0.190)
step_size: N/A (single-point evaluation matches legacy)
tolerance: |n_joint_global_refactored - n_joint_global_legacy| < 1e-12 (PASS); 1e-12 < ... < 1e-6 (INFO); > 1e-6 (FAIL)
scheme: zeta-regulated Seeley-DeWitt; a_n^{ζ} tag for any moment citation
convention: F_4 multiplier-vector basis (S86 W-8) + M-component basis (S85 W5-7)
random_seed: N/A
GPU path: same as legacy s85_w5_7_two_layer_obstruction.py
```

### Input SHA-256 pins

- `computations/s85_w5_7_two_layer_obstruction.py` — `<computed-at-runtime>` (LEGACY source, READ-ONLY for reference; refactor target produces NEW output)
- Legacy npz output (if cached): `s85_w5_7_two_layer_obstruction.npz` — `<computed-at-runtime>` (backward-compat cross-check anchor)
- `computations/canonical_constants.py` — `<computed-at-runtime>`
- `computations/s84_spectrum_cache_L12_tau019.npz` — `<computed-at-runtime>` (if legacy script depends on spectrum cache)
- `.claude/rules/regulator-pin-discipline.md` — `<computed-at-runtime>` (a_n^{ζ} tag)

### Expected output 4-tuple

`(value=|n_joint_global_refactored - n_joint_global_legacy|, scheme=zeta-regulated-Seeley-DeWitt, convention=F_4-plus-M-decomposition, L_max=12)`

### Producing script

`computations/s87_w6_f4_m_subsum_refactor.py` (NEW; wraps the refactor; preserves backward compat and adds sub-sum exposure)

### Output artifacts

- Script: `computations/s87_w6_f4_m_subsum_refactor.py`
- Data: `s87_w6_f4_m_subsum_refactor.npz` with fields `n_joint_F4`, `n_joint_M`, `n_joint_global` (refactored), `n_joint_global_legacy_match_deviation`
- Plot: `s87_w6_f4_m_subsum_refactor.png` showing decomposition bar chart (F_4 contribution + M contribution = global)
- Verdict line: appended to `computations/s87_gate_verdicts.txt`
- Working-paper section: §W6-6 (substantive >=15 lines)

### What PASS means

The refactor preserves the legacy global-sum identity at machine epsilon AND exposes F_4 and M sub-sums separately. Downstream gates CF-43 (C-β UV-cutoff-choice immunization across F_4 multiplier-vector sub-family) and CF-44 (C-γ-WEAK Weyl-rescaling per L1-class) can now consume `n_joint_F4` and `n_joint_M` independently, enabling per-class sensitivity analysis.

### What FAIL means

The refactor introduced a bug (global-sum identity broken) OR the legacy script's F_4/M decomposition cannot be cleanly extracted (possibly because the original computation entangled F_4 and M contributions via cross-terms that were absorbed into the global sum without explicit per-component tracking). FAIL routes to S88 PRU re-pre-registration with substrate-first canonical-sourcing audit on the F_4 vs M decomposition canonical source.

### Substrate framing

The two-layer obstruction n_joint_global IS the substrate's combined obstruction count from F_4 (4-channel multiplier-vector sub-family) and M (M-component basis) contributions. Exposing the sub-sums separately IS revealing the substrate's intrinsic two-source structure of the obstruction; the refactor does not change the substrate, only makes its decomposition machine-queryable.

### YAML

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-S85-W5-7-F4-M-SUBSUM-REFACTOR
trigger: VERIFY
classification: GEOMETRIC
wave_class: COMPUTE-class
owner: lizzi-spectral-functional-theorist
co_signers: [gen-physicist]
threshold_tolerance_rule: ABSOLUTE
threshold_pass: 1e-12
threshold_info_band: [1e-12, 1e-6]
threshold_fail: 1e-6
regulator_tag: a_n^{ζ}
refactor_source: computations/s85_w5_7_two_layer_obstruction.py (READ-ONLY reference)
refactor_target: computations/s87_w6_f4_m_subsum_refactor.py (NEW)
backward_compat_field: n_joint_global (preserved)
new_exposed_fields: [n_joint_F4, n_joint_M]
```

---

## Wave 6 → Wave 7 Decision Point

Wave 6 closes with 6 verdict lines in `computations/s87_gate_verdicts.txt`. The downstream consumers in Wave 7+ depend on the following:

| §W6 gate | PASS triggers | FAIL triggers | INFO triggers |
|:---------|:--------------|:--------------|:--------------|
| §W6-1 (T7-S67 isomorphism) | §VII.AG.1 STAGE-1-CANDIDATE consumed by §W6-4 (CFMSW anchor) and §W6-5 (cross-cluster cyclic-fold V_4 anchor); CF-59 Stage-2 reserved for S88+ | §W6-4 + §W6-5 reroute to S88 (lose structural anchor); §W6-2 / §W6-3 / §W6-6 still execute | structure-tag carry-forward to Stage-2 cross-review at S88+; §W6-4 / §W6-5 still execute |
| §W6-2 (V2-weight match) | A_F real-dim ratio (1:4:18) confirmed at machine epsilon; substrate-physics anchor for §W6-3 / §W6-4 | rerouted to S88 PRU re-pre-registration with substrate-first canonical-sourcing audit | numerical-precision diagnostic; rerun at higher L_max=14 if §W6-3 also INFOs |
| §W6-3 (triangular Wilson-3 plaquette) | Z_3 gauge-sector signature 512 confirmed; §VII.AG.4 anchor closed; substrate validation for cyclic-fold V_4 commutation with Z_3 center | rerouted to S88 PRU re-pre-registration with hypercube-vertex character identity audit (CF-69 cross-check) | numerical-precision diagnostic; rerun with explicit Z_3 quotient gauge-fixing |
| §W6-4 (cyclic-fold class survey) | CFMSW class has structural depth (>= 3 candidates); S88+ slots reserved per candidate | rerouted to S88 carry-forward; CFMSW class retired | single-instance class; no rule promotion; carry-forward for monitoring |
| §W6-5 (Mellin-Wick commutation theorem) | §VII.AG.5 positive-theorem; substrate-IS coherent cross-cluster | §VII.AG.5 negative-theorem; substrate's intrinsic cross-cluster mixing identified as feature | partial-commutation theorem; scope-restricted registry entry |
| §W6-6 (F_4/M sub-sum refactor) | downstream CF-43 / CF-44 consumers gain per-class queryability | rerouted to S88 PRU with substrate-first audit on F_4 vs M decomposition canonical source | float64 round-off; backward-compat preserved; downstream consumers proceed |

If §W6-1 FAILs, the entire Cluster 1 + Cluster 3 (research-mode items) reroute to S88. The Cluster 2 forward gates (§W6-2 / §W6-3 / §W6-6) are independent and proceed regardless.

---

## Wave 6 Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness", every gate in this wave has its full PRDR machinery checklist enumerated above. Aggregate machinery pins for Wave 6:

| Pin name | §W6-1 | §W6-2 | §W6-3 | §W6-4 | §W6-5 | §W6-6 |
|:---------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| N_eval | N/A | full L=12 spectrum | 768 plaquettes | full §VII walk | N/A | full L=12 spectrum |
| L_max | 10 (W-5 anchor) | 12 | 12 | N/A | N/A | 12 |
| scan_range | N/A | tau_fold | tau_fold | §VII walls | V_4-coset pairs | tau_fold (legacy match) |
| step_size | N/A | N/A | N/A | N/A | N/A | N/A |
| tolerance | substantive_line_count >= 15; SHA match | 1e-10 RATIO | 1e-6 RATIO vs 512 | enumeration-completeness | algebraic identity | 1e-12 ABSOLUTE |
| scheme | SOURCE-DOUBLE-CITE-CO-PRIMARY | a_n^{ζ} | a_n^{ζ} wilson_3 | CFMSW | Mellin-cone s=3 + Wick rotation | a_n^{ζ} |
| convention | STAGE-1-CANDIDATE | cyclic-fold V_4 | Z_3-quotient cyclic-fold V_4 | V_4 partition | V_4 cyclic-fold | F_4 + M decomposition |
| random_seed | N/A | N/A | N/A | N/A | N/A | N/A |
| GPU path | N/A | torch.linalg.eigh on AMD RX 9070 XT (partial) | torch.linalg.matrix_exp | N/A | N/A (Sage MCP eligible) | same as legacy script |

PRDR Pre-Registration Dry-Run validation required at plan-freeze: run `computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w6.md` for PRDR machinery checklist + R3 `schema_version` per gate. Run `computations/_pru_cardinality_audit.py` to verify D_PRU_raw = 0 across all 6 gates.

---

## Wave 6 Input-SHA Ledger

Single-source consolidated ledger of all upstream files Wave 6 consumes (cross-referenced from per-gate Input SHA-256 pins above):

| File | Used by gate(s) | Purpose | SHA-pin policy |
|:-----|:----------------|:--------|:---------------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | §W6-2, §W6-3, §W6-6 | Jensen-deformed SU(3) spectrum at canonical `tau_fold` | `<computed-at-runtime>` |
| `computations/s56_atensor_frustration.py` | §W6-3 | Legacy Wilson-4 source (READ-ONLY refactor reference) | `<computed-at-runtime>` |
| `computations/s85_w5_7_two_layer_obstruction.py` | §W6-6 | Legacy two-layer obstruction script (READ-ONLY refactor reference) | `<computed-at-runtime>` |
| `computations/canonical_constants.py` | §W6-1, §W6-2, §W6-3, §W6-6 | `tau_fold`, `M_KK`, `L_max_canonical` | `<computed-at-runtime>` |
| `sessions/permanent-results-registry.md` | §W6-1, §W6-4, §W6-5 | §VII registry walk + §VII.AG slot landings | `<computed-at-runtime>` |
| `sessions/archive/session-86/` W-6 workshop closure file | §W6-1 | Verbatim joint-theorem text source | `<computed-at-runtime>` |
| `computations/s87_gate_verdicts.txt` | §W6-2, §W6-4, §W6-5 (consume §W6-1 anchor) | Verdict-line append target + §W6-1 anchor pin for downstream | `<computed-at-runtime>` |
| `.claude/rules/agent-standards.md` | §W6-1, §W6-5 | T1-6 quotient-functor discipline + PRU Class 8.2 verifier-rubric | `<computed-at-runtime>` |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | §W6-1, §W6-4 | 5 IS-not-IN anatomy + 3-level ladder schema | `<computed-at-runtime>` |
| `.claude/rules/joint-theorem-promotion.md` | §W6-1 | 4-stage pathway + STAGE-1-CANDIDATE tag schema | `<computed-at-runtime>` |
| `.claude/rules/registry-landing.md` | §W6-1, §W6-4 | SOURCE-DOUBLE-CITE-CO-PRIMARY structure | `<computed-at-runtime>` |
| `.claude/rules/regulator-pin-discipline.md` | §W6-2, §W6-3, §W6-6 | a_n^{ζ} tag enforcement | `<computed-at-runtime>` |
| `.claude/rules/math-scripts.md` | §W6-3 | canonical_constants import + archive-script exemption | `<computed-at-runtime>` |
| §VII.U.6 entry (Mellin-Strip / Convergence-Cone Theorem) | §W6-5 | Cross-cluster Mellin transform anchor | `<computed-at-runtime>` |
| S86 W-12 CF-66 V_4 parallelogram identity entry | §W6-3, §W6-5 | V_4 cardinality refinement + Z_3 commutation | `<computed-at-runtime>` |
| S86 W-12 CF-69 hypercube-vertex character identity entry | §W6-3, §W6-5 | (Z_2)^d hypercube-vertex character verification | `<computed-at-runtime>` |
| S86 W-5 §VII.W cross-pillar bridge theorem | §W6-1 (Level-3 anchor reference) | 0.0095% F_4 strict at L_max=10 calibration corpus | `<computed-at-runtime>` |

All SHA-256 values are `<computed-at-runtime>` per the dynamic-input convention; the producing scripts MUST log all input SHAs in their first 20 lines of stdout per `.claude/rules/gate-verdicts.md`.

---

**End of session-87-plan-w6.md.**
