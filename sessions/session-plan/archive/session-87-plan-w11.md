# Session 87 Plan — Wave 11: V_4 Monodromy + 4-Stratum + 3He-B Excess

**Wave-owner**: `connes-ncg-theorist` (W-12 was joint connes+volovik per S86 attribution; lead-listed reviewer = connes per `connes+volovik → connes-ncg-theorist` row of §4 wave-owner heuristic in session-87-context.md).

**Wave items (6)**: CF-66, CF-67, CF-68, CF-69, CF-70, CF-71. All sourced from S86 W-12 (V_4 monodromy + 4-stratum partition workshop). CF-66 supersedes the pre-registered Z_4 pre-reg (`S87-MONODROMY-Z4-LANDING`) per W-12 RULE-W12-1 PRU Class 8.2 calibration. CF-71 is latent (not pre-registered in W-12 source) and treated as forward-research per `feedback_fix-in-session-never-defer.md`.

**Specialist-agent assignment**: connes-ncg-theorist owns CF-66/67/68/69/71 (NCG-axiomatic + spectral-action moments substrate); volovik-superfluid-universe-theorist owns CF-70 (3He-B substrate authority per `feedback_agent-roster.md`); spectral-geometer co-signs CF-69 (Sage-verify hypercube identity for d ∈ {2, 3, 4, 5}).

**Registry slot reservation**: §VII.AJ already pre-allocated as OPEN reservation in `sessions/permanent-results-registry.md` summary table for "W-12 Mellin-Moment Identities" landings. CF-66 (V_4 monodromy) and CF-69 (hypercube-vertex identity) are the primary §VII.AJ landing candidates; CF-67/CF-68 land at §VII.AJ.partition-stability sub-slot if PASS; CF-70 is a falsifier-master-inventory row, not a §VII.AJ entry.

---

## Wave 11 Summary

| # | Gate ID | Owner | Effort | Trigger | Classification | Theme |
|:--|:--------|:------|:-------|:--------|:---------------|:------|
| 1 | `S87-MONODROMY-V_4-EXPLICIT` | connes-ncg-theorist | ~6h | [VERIFY] | GEOMETRIC | V_4 parallelogram identity for spectral-action moments at τ_fold; supersedes Z_4 pre-reg |
| 2 | `S87-PARTITION-STABILITY-4STRATUM` | connes-ncg-theorist | ~4h | [VERIFY] | GEOMETRIC | Bottom-20 multiplicity profile of D_K(τ_fold ± δ_τ) under 5-point δ_τ scan |
| 3 | `S87-STRATUM3-LMAX-SCAN` | connes-ncg-theorist | ~4-6h | [VERIFY] | GEOMETRIC | Stratum-3 multiplicity stability at L_max ∈ {12,13,14,15} fixed-τ scan (sister gate to W11-2) |
| 4 | `S87-HYPERCUBE-VERTEX-IDENTITY-LANDING` | connes-ncg-theorist + spectral-geometer co-sign | ~2h | [VERIFY-THEOREM] | GEOMETRIC | (Z_2)^d hypercube-vertex character identity Sage-verified at d ∈ {2,3,4,5} |
| 5 | `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` | volovik-superfluid-universe-theorist | ~3-5h (lit) / ~10-15h (fresh BdG) | [VERIFY] | PHONONIC | 3He-B BdG-undoubled spectral excess at polycritical pressure point; substrate-IS / lab-IN bridge |
| 6 | `S87-MONODROMY-DEPTH-EXTENSION` | connes-ncg-theorist | ~6-10h | [VERIFY] | GEOMETRIC | Empirical test of d=2 exactness vs d>2 atlas extension; latent forward-research gate |

**Total wave estimate**: ~25-43h compute (low end with volovik-lit path on CF-70; high end with fresh-BdG path).

---

## Wave 11 Decision Point Prerequisites

This wave runs INDEPENDENT of W1-W10 W12+ landings. The 6 W-12-derived gates are self-contained against the L=12 master spectrum cache, the canonical_constants.py τ_fold pin, and the S86 W-12 4-stratum partition canonical.

### Upstream pin map (read-only inputs)

| Pin name | Source | Role |
|:---------|:-------|:-----|
| `computations/canonical_constants.py:tau_fold = 0.190` | S58 Volovik partition canonical | τ_fold value (CF-66/67/68/71 all evaluate AT τ_fold) |
| `computations/canonical_constants.py:M_KK` | S86 axiomatic sole external pin | KK mass scale anchor for spectral-moment dimensional bookkeeping |
| `computations/s84_spectrum_cache_L12_tau019.npz` | S84 W-10 master spectrum cache | D_K(τ_fold) eigenvalues at L_max=12; bottom-20 + full spectrum |
| S86 W-12 4-stratum partition (registry pin: §VII.K-PROP sub-row partition canonical) | S86 W-12 workshop closure | 4-stratum canonical at τ_fold; CF-67/CF-68 baseline |
| S86 W-12 V_4 cosets enumeration (workshop §EMERGENCE E-1 R3-volovik final round lines 1622-1641) | S86 W-12 source | 4-element V_4 coset structure; CF-66 input |
| `sessions/permanent-results-registry.md:§VII.W` (Pillar III ↔ IV bridge anatomy template) | S86 W-5 RULE-2 | CF-70 cross-pillar bridge format template (5 IS-not-IN elements + 3-level ladder) |
| S86 W-12 R3-A E-3 lines 1451-1462 (HIGH-DENSITY WORKSHOP TEMPLATE T2-5 calibration) | S86 W-12 → `agent-standards.md` | Multi-output decomposition pattern for CF-66 (literal pre-reg V_4-supersession + structural V_4 candidate + methodology Class 8.2 entry) |

### Validator coverage at Wave 11 plan-freeze

Per `session-87-context.md` §1.4, run before wave dispatch:
1. `_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w11.md` → `sessions/session-plan/session-87-plan-w11-validation.json`
2. `_yaml_gate_validator.py sessions/session-plan/session-87-plan-w11.md` (R3 schema_version + PRDR machinery checklist)
3. `_source_reconciliation_audit.py` (5+1 class taxonomy; HARD-HALT at D_max ≥ 3.0; class-(c) PIN-DRIFT for any stale W-12-source citation)
4. `_substrate_first_provenance_audit.py` manual review on CF-70 (substrate-IS observable must source from BdG spectral triple computation, not from Volovik 2003 §27 alone — Volovik 2003 is methodological cross-check per §"(i) When external-paper provenance is methodological vs canonical")
5. `_a_n_regulator_pin_audit.py` for CF-66 (a_n regulator-tag enforcement on `A_n^(g)` spectral-moment moments)
6. Post-dispatch grep on `computations/s86_gate_verdicts.txt` for collision check on `S87-MONODROMY-*`, `S87-PARTITION-*`, `S87-STRATUM3-*`, `S87-HYPERCUBE-*`, `S87-3HEB-*` gate IDs (no S87-prefixed entries should pre-exist).

---

## §W11-1. CF-66 — `S87-MONODROMY-V_4-EXPLICIT`

**Source**: S86 W-12 CF-W12-1 (priority-1; supersedes pre-registered `S87-MONODROMY-Z4-LANDING` per W-12 RULE-W12-1 PRU Class 8.2 calibration in `agent-standards.md` §"HIGH-DENSITY WORKSHOP TEMPLATE T2-5").

**Specialist agent**: `connes-ncg-theorist` (NCG-axiomatic + spectral-action moments substrate authority).

**Effort**: ~6h.

### 1. Gate ID

`S87-MONODROMY-V_4-EXPLICIT`

**Supersession event**: This gate REPLACES the pre-registered `S87-MONODROMY-Z4-LANDING` entry. The W-12 workshop's literal pre-registration ("PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)") admitted Klein-four V_4 as "similar" via cardinality match (both Z_4 and V_4 have order 4) DESPITE structural distinction via element orders (V_4 = [1,2,2,2] vs Z_4 = [1,2,4,4]). The "or similar" token was unintentionally permissive — workshop's actual finding (V_4) satisfied the literal rubric reading despite structurally falsifying Z_4. Per PRU Class 8.2 (`agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE T2-5 line 1432-1449), this gate explicitly cites the supersession-event in its verdict-line `value=` field.

### 2. Trigger

`[VERIFY]` — verify V_4 PARALLELOGRAM IDENTITY for spectral-action moments at τ_fold under all 4 V_4 cosets.

### 3. Classification

GEOMETRIC (substrate spectral-action structure; not phononic excitation, not particle quantum number).

### 4. Hypothesis being tested

The substrate's regulator-monodromy group at τ_fold on the 4-element coset partition is **Klein-four V_4 = (Z_2)^2**, NOT Z_4. The structural prediction is: spectral-action moments A_n^(g) for n ∈ {0, 2, 4} satisfy the V_4 PARALLELOGRAM IDENTITY:

```
A_n^(g_0) − A_n^(g_1) − A_n^(g_2) + A_n^(g_3) = 0
```

at τ = τ_fold = 0.190, for each n ∈ {0, 2, 4}, where {g_0, g_1, g_2, g_3} is the V_4 coset enumeration per S86 W-12 §EMERGENCE E-1 R3 lines 1622-1641. The Z_4 alternative would predict a different cyclic identity `A_n^(g_0) − i·A_n^(g_1) − A_n^(g_2) + i·A_n^(g_3) = 0` (with non-trivial phase weights), which is structurally DISTINCT from the V_4 form.

### 5. Pass/fail/INFO threshold

- **PASS**: V_4 PARALLELOGRAM IDENTITY holds at relative deviation `≤ 1e-12` (floor at ~5× float64 ULP = 5 × 2.22e-16 ≈ 1.11e-15; threshold pin 1e-12 = ~4.5 OOM above floor, allowing for accumulated rounding in spectral-moment summation; consistent with publication-precision pre-registration `agent-standards.md` §"Publication-Precision Pre-Registration") for ALL n ∈ {0, 2, 4}.
  - Tolerance rule: RATIO. Per-moment relative deviation `|A_n^(g_0) − A_n^(g_1) − A_n^(g_2) + A_n^(g_3)| / max(|A_n^(g_0)|, |A_n^(g_1)|, |A_n^(g_2)|, |A_n^(g_3)|) ≤ 1e-12`.
- **FAIL**: relative deviation `> 1e-9` for ANY n ∈ {0, 2, 4} (3 OOM above PASS band). Indicates the monodromy group is NOT V_4 (could be Z_4, larger non-abelian group, or no group structure at all).
- **INFO**: relative deviation `1e-12 < dev ≤ 1e-9` (3 OOM info band). Indicates V_4 structure plausible but precision-limited; carry-forward to higher-precision Sage-mpmath rerun.

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | full bottom-20 + extended top-K spectrum at L_max=10 (per S84 cache); ~155,984 eigenvalues addressable |
| `L_max` | 10 (canonical S84 master cache; L_max=12 cache available as cross-check; W11-3 sister gate scans L_max ∈ {12,13,14,15}) |
| `scan_range` | τ = τ_fold = 0.190 ONLY (single-point evaluation; no τ-scan in this gate) |
| `step_size` | N/A (no τ-derivative; static spectral-moment evaluation) |
| `tolerance` | RATIO `1e-12` per-moment (PASS); INFO band `(1e-12, 1e-9]`; FAIL above `1e-9` |
| `scheme` | Mellin-cone substrate-distance-1 (s=3 pole) for A_2; substrate-distance-0 (s=4 pole) for A_4; substrate-distance-3 (s=2 pole) for A_0. Per regulator-pin discipline `regulator-pin-discipline.md`, A_n entries tagged as `A_n^{Mellin}` (Mellin-cone via `analytic_zeta` callable). |
| `convention` | substrate-distance-{3,1,0} per Mellin-cone pole structure; V_4 coset enumeration g_0..g_3 per S86 W-12 §EMERGENCE E-1 R3 lines 1622-1641 (cite by line) |
| `random_seed` | N/A (deterministic spectral-moment evaluation; no Monte Carlo) |
| `GPU path` | `torch.linalg.eigh` on AMD RX 9070 XT (L_max=10 D_K matrix is 155,984×155,984 sparse; eigenvalues already cached in s84_spectrum_cache_L12_tau019.npz). For coset action evaluation on cached eigenvalues, CPU-only path acceptable with `OMP_NUM_THREADS=8` cap per `math-scripts.md` §Environment. |

### 7. Input SHA-256 pins

- `computations/canonical_constants.py` — tau_fold = 0.190, M_KK pins. Static; precompute SHA at plan-freeze.
- `computations/s84_spectrum_cache_L12_tau019.npz` — D_K(τ_fold) eigenvalues at L_max=12 (master spectrum cache from S84 W-10). Static; precompute SHA at plan-freeze.
- `sessions/archive/session-86/s86_w12_workingpaper.md` lines 1622-1641 — V_4 coset enumeration g_0..g_3. Static workshop-output; precompute SHA at plan-freeze.
- `computations/_spectral_action_regulators.py` (Mellin-cone callable wrapper). level pin: PRIMARY (full physical Mellin-cone via `analytic_zeta`, NOT SCHEMATIC schematic). Verify `convention=substrate-distance-1-MELLIN` (NOT `-SCHEMATIC`) per `substrate-first-canonical-sourcing.md` §(iv).

### 8. Expected output 4-tuple

`(value=max_n {|V_4 parallelogram dev|_n} for n ∈ {0,2,4}, scheme=Mellin-cone-substrate-distance-{3,1,0}, convention=V_4-coset-enumeration-W12-E1-R3, L_max=10)`

### 9. Substitution chain (sign/direction discipline per `math-scripts.md`)

The V_4 PARALLELOGRAM IDENTITY is an EQUALITY claim, not a directional inequality. Per `math-scripts.md` §"When the chain is NOT required" — definitions-only statements (no direction claim) — the substitution chain reduces to:

```
Step 1: A_n^(g) := Tr_g[D_K^{-2(n-2)}] for n ∈ {0, 2, 4}    [Connes-Chamseddine 1996 Mellin-cone definition]
Step 2: V_4 = {g_0=e, g_1, g_2, g_3 = g_1·g_2}             [Klein-four group structure: (Z_2)^2 with all non-identity elements of order 2]
Step 3: PARALLELOGRAM IDENTITY := A_n^{(g_0)} − A_n^{(g_1)} − A_n^{(g_2)} + A_n^{(g_3)} = 0
                                  (sum of "+" cosets minus sum of "−" cosets equals zero)
Step 4: For Z_4 alternative, identity would be A_n^{(g_0)} − i·A_n^{(g_1)} − A_n^{(g_2)} + i·A_n^{(g_3)} = 0
        (cyclic phase weights distinguish Z_4 from V_4)
Step 5: PASS direction: V_4 holds → real-valued parallelogram-form identity holds at machine precision
        FAIL direction: V_4 fails → either cyclic Z_4 structure (with imaginary phases) OR no group structure
```

### 10. What PASS and FAIL mean for the solution space

- **PASS**: V_4 = (Z_2)^2 is the substrate's regulator-monodromy group at τ_fold on the 4-element coset partition. Confirms W-12 workshop's structural finding; closes the Z_4 candidate corridor; lands §VII.AJ V_4-monodromy theorem candidate (per S86 W-12 §VII.AJ OPEN reservation in `permanent-results-registry.md`). PRU Class 8.2 calibration corpus instance #1 closes (V_4 vs Z_4 structurally distinct via element orders) per `agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE T2-5 lines 1432-1449.
- **FAIL**: Either (a) Z_4 cyclic structure holds (rerun with cyclic-phase-weighted identity to confirm), OR (b) no group structure on coset partition (deeper structural defect; W-12 V_4 framework is wrong; downstream W-12-derived gates CF-67/CF-68/CF-69/CF-71 are downstream-blocked). FAIL forces re-derivation of W-12's monodromy structure.
- **INFO**: Precision-limited; rerun with Sage-mpmath arbitrary-precision per `math-scripts.md` §"Sage-Exact Rationals" extension to push tolerance below `1e-15`.

### 11. Multi-output decomposition (per `agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE T2-5)

CF-66 is a HIGH-DENSITY workshop output that produces FOUR independent OUTPUT slots from a single bimodality probe (per W-12 calibration corpus instance #1):

1. **Literal pre-reg verdict slot**: `S87-MONODROMY-Z4-LANDING` closes as INFO-coincidence-with-V_4-sharpening (rubric-form failure: "Z_4 or similar" admitted V_4). Verdict line emitted under THIS gate ID, with explicit supersession marker.
2. **Structural candidate slot at bare-eigenvalue layer**: `§VII.AJ V_4-monodromy-theorem` candidate (registry promotion path; lands at OPEN-reserved §VII.AJ slot if PASS).
3. **Methodology rule-file extension slot**: PRU Class 8.2 added to `epistemic-discipline.md` §"Pre-Registration Completeness" sub-class taxonomy (already landed at S86 W-12 close per T2-4).
4. **Calibration corpus entry slot**: W-12 verdict added as the first instance of Class 8.2 (already landed at S86 W-12 close).

This gate's verdict-line emission services slots 1+2; slots 3+4 already landed in S86 close. The verdict line MUST cite the supersession-event in `value=` field per HIGH-DENSITY WORKSHOP TEMPLATE.

### 12. Output artifacts

- Script: `computations/s87_w11_v4_monodromy_explicit.py` (~250-400 lines; loads cached spectrum, applies 4 coset actions g_0..g_3, computes A_n^(g) via Mellin-cone callable for n ∈ {0,2,4}, evaluates parallelogram-identity deviation per moment, emits dual-SHA verdict line with supersession-event annotation).
- Data: `s87_w11_v4_monodromy_explicit.npz` (keys: `A_0_per_coset[4]`, `A_2_per_coset[4]`, `A_4_per_coset[4]`, `parallelogram_dev_per_n[3]`, `max_dev`, `coset_enumeration_label`).
- Plot: `s87_w11_v4_monodromy_explicit.png` (4-panel: A_n^(g) bar chart per n, with parallelogram-balance visualization showing "+" and "−" coset contributions).
- Verdict line: appended to `computations/s87_gate_verdicts.txt` per S87+ schema-v2 (canonical line + dual-SHA companion + 3-tuple annotation if [SIGN] trigger is added; here not required since trigger is [VERIFY]).
- Working-paper section: `sessions/archive/session-87/session-87-w11-workingpaper.md` §W11-1 (>15 lines; full V_4-vs-Z_4 substitution chain + PRU Class 8.2 calibration commentary + supersession-event audit trail).

### 13. YAML pin

```yaml
gate_id: S87-MONODROMY-V_4-EXPLICIT
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY
classification: GEOMETRIC
specialist_agent: connes-ncg-theorist
supersedes_gate_id: S87-MONODROMY-Z4-LANDING
supersession_rationale: PRU Class 8.2 calibration; "Z_4 or similar" admitted V_4 via cardinality match
high_density_workshop: true
output_slots: [literal_preg_supersession, structural_VII_AJ_candidate]
```

---

## §W11-2. CF-67 — `S87-PARTITION-STABILITY-4STRATUM`

**Source**: S86 W-12 CF-W12-2 (priority-2).

**Specialist agent**: `connes-ncg-theorist`.

**Effort**: ~4h wall-clock.

### 1. Gate ID

`S87-PARTITION-STABILITY-4STRATUM`

### 2. Trigger

`[VERIFY]` — verify 4-stratum partition stability under τ-perturbation around τ_fold.

### 3. Classification

GEOMETRIC (D_K eigenvalue-multiplicity profile is a substrate-spectral-triple property; not phononic excitation).

### 4. Hypothesis being tested

The 4-stratum partition of the bottom-20 eigenvalue-multiplicity profile of D_K(τ) at τ = τ_fold is **stable** (multiplicity counts per stratum are τ-invariant) across a 5-point τ-perturbation scan δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10} (i.e., evaluating D_K at τ_fold ± δ_τ for each δ_τ value, total 11 τ-points including τ_fold itself).

The 4-stratum canonical at τ_fold (per S86 W-12 §VII.K-PROP partition canonical) defines the strata by multiplicity-count signature. Stability means: at all 11 τ-points, the bottom-20 eigenvalues partition into 4 multiplicity-strata with the same per-stratum cardinality.

### 5. Pass/fail/INFO threshold

- **PASS**: 4-stratum cardinality vector `(N_1, N_2, N_3, N_4)` is INVARIANT (exact integer match) across all 11 τ-points.
  - Tolerance rule: THEOREM (exact integer match; no tolerance — partition cardinality is integer-valued).
- **FAIL**: any one of the 11 τ-points produces a different cardinality vector (e.g., a stratum splits or merges as δ_τ grows).
- **INFO**: cardinality vector matches at all τ_fold ± δ_τ for δ_τ ∈ {0.005, 0.01, 0.025, 0.05} but breaks at δ_τ = 0.10 ONLY (boundary effect at large perturbation; structural finding is "stability holds for δ_τ ≤ 0.05, breaks at 0.10").

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | bottom-20 eigenvalues per τ-point × 11 τ-points = 220 eigenvalue extractions |
| `L_max` | 10 (canonical; L_max=12 master cache available as cross-check; W11-3 sister gate handles L_max-axis variation) |
| `scan_range` | τ ∈ {0.090, 0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290} (= τ_fold ± δ_τ for δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10} plus τ_fold itself); 11 points total |
| `step_size` | not applicable (discrete 5-point δ_τ grid; no continuous derivative) |
| `tolerance` | THEOREM exact integer match on cardinality vector `(N_1, N_2, N_3, N_4)` |
| `scheme` | direct D_K eigenvalue extraction; multiplicity-stratum partition by integer-equal-eigenvalue clustering (within ULP floor, ~1e-14 absolute tolerance for "equal" eigenvalues) |
| `convention` | 4-stratum partition canonical per S86 W-12 §VII.K-PROP partition row (cite line) |
| `random_seed` | N/A (deterministic eigenvalue extraction) |
| `GPU path` | `torch.linalg.eigh` on AMD RX 9070 XT for 11 D_K(τ)-matrix eigendecompositions; falls under GPU-pin selectivity per `math-scripts.md` §"Machinery-Feasibility Audit" — D_K(τ) at L_max=10 fits well within 17.1 GB VRAM |

### 7. Input SHA-256 pins

- `computations/canonical_constants.py` — tau_fold pin. Static; precompute SHA at plan-freeze.
- `computations/build_dirac_operator.py` (or analogous D_K builder) — D_K(τ) constructor. Static module; precompute SHA.
- S86 W-12 §VII.K-PROP partition canonical — cite by registry slot ID + line range; precompute SHA over the cited block.
- `computations/s84_spectrum_cache_L12_tau019.npz` — cross-check at τ_fold (L_max=12 anchor); used to validate the L_max=10 evaluation at τ = 0.190 against the cache before scanning.

### 8. Expected output 4-tuple

`(value=number_of_taupoints_with_invariant_cardinality, scheme=integer-multiplicity-strata, convention=4-stratum-canonical-W12-VII.K-PROP, L_max=10)`

PASS = 11 (all τ-points invariant); FAIL = any value < 10; INFO = exactly 10 (only δ_τ = 0.10 breaks).

### 9. Substitution chain

```
Step 1: D_K(τ) := graded Dirac operator on Jensen-deformed SU(3) spectral triple at deformation parameter τ
        [substrate-IS observable; canonical_classes.py:308 EXFLATION_CLASS]
Step 2: bot20(τ) := {λ_1(τ), ..., λ_20(τ)} sorted ascending eigenvalues of D_K(τ)
        [smallest 20 eigenvalues by absolute value]
Step 3: stratum_partition(bot20) := equivalence classes under λ_i ~ λ_j iff |λ_i − λ_j| < ULP_tolerance
        [4-stratum canonical at τ_fold per S86 W-12 §VII.K-PROP]
Step 4: cardinality_vector(τ) := (|S_1|, |S_2|, |S_3|, |S_4|) where S_k is the k-th stratum
Step 5: PASS direction: cardinality_vector(τ) == cardinality_vector(τ_fold) for all 11 τ-points
        FAIL direction: any τ-point produces a different cardinality vector
```

No directional inequality; THEOREM equality on integer-valued cardinality. The chain is illustrative; no [SIGN] trigger annotation needed.

### 10. What PASS and FAIL mean for the solution space

- **PASS**: 4-stratum partition is τ-stable in a finite neighborhood of τ_fold (at least δ_τ = 0.10). Confirms the W-12 framework's substrate-physics claim that the 4-stratum structure is a topological invariant of the spectral triple (not a τ_fold-fine-tuning artifact). Lands §VII.AJ.partition-stability sub-slot if combined with W11-3 PASS.
- **FAIL**: The 4-stratum partition is τ_fold-fine-tuned; small perturbations split/merge strata; W-12's "4-stratum partition as substrate-physical observable" claim is invalidated; downstream gates W11-3, W11-6 require re-derivation.
- **INFO**: Stability holds at δ_τ ≤ 0.05 but breaks at 0.10 — informative; closes a corridor (the partition has finite-radius stability ~0.05). Carry-forward: re-scan with finer δ_τ ∈ {0.06, 0.07, 0.08, 0.09} to localize the breakdown.

### 11. Output artifacts

- Script: `computations/s87_w11_partition_stability_4stratum.py` (~200-300 lines).
- Data: `s87_w11_partition_stability_4stratum.npz` (keys: `tau_grid[11]`, `bot20_per_tau[11,20]`, `cardinality_vector_per_tau[11,4]`, `pass_count`, `delta_tau_breakdown_threshold`).
- Plot: `s87_w11_partition_stability_4stratum.png` (multi-panel: bot20 spectrum vs τ; cardinality vector evolution; stratum-color-coded eigenvalue map).
- Verdict line: appended to `computations/s87_gate_verdicts.txt`.
- Working-paper section: `sessions/archive/session-87/session-87-w11-workingpaper.md` §W11-2 (>15 lines).

### 12. YAML pin

```yaml
gate_id: S87-PARTITION-STABILITY-4STRATUM
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY
classification: GEOMETRIC
specialist_agent: connes-ncg-theorist
sister_gate: S87-STRATUM3-LMAX-SCAN
delta_tau_grid: [0.005, 0.01, 0.025, 0.05, 0.10]
```

---

## §W11-3. CF-68 — `S87-STRATUM3-LMAX-SCAN`

**Source**: S86 W-12 CF-W12-3 (priority-3; sister gate to W11-2 — partition-stability axis is τ-perturbation, this gate's axis is L_max-perturbation).

**Specialist agent**: `connes-ncg-theorist`.

**Effort**: ~4-6h.

### 1. Gate ID

`S87-STRATUM3-LMAX-SCAN`

### 2. Trigger

`[VERIFY]` — verify stratum-3 multiplicity stability under L_max-extension at fixed τ_fold.

### 3. Classification

GEOMETRIC (L_max convergence is a substrate-spectral-triple regulator-axis property).

### 4. Hypothesis being tested

The third stratum (S_3) of the 4-stratum partition of D_K(τ_fold) bottom-20 eigenvalues has STABLE cardinality |S_3| under L_max extension across L_max ∈ {12, 13, 14, 15} (with τ = τ_fold = 0.190 fixed). Stratum-3 is selected because S86 W-12 identified it as the most precision-sensitive stratum in the 4-stratum partition (per workshop §EMERGENCE E-3 line 1451-1462 calibration corpus). Cardinality stability at higher L_max confirms the partition is L_max-convergent (not a finite-truncation artifact).

### 5. Pass/fail/INFO threshold

- **PASS**: |S_3(L_max)| is INVARIANT across L_max ∈ {12, 13, 14, 15}.
  - Tolerance rule: THEOREM (exact integer match).
- **FAIL**: |S_3(L_max)| changes at any L_max in the scan (stratum-3 cardinality is a finite-truncation artifact).
- **INFO**: |S_3(L_max)| is invariant at L_max ∈ {12, 13, 14} but shifts at L_max=15 (signal of asymptotic instability; carry-forward to L_max=16+ scan).

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | bottom-20 eigenvalues × 4 L_max values; D_K matrix dimensions scale with L_max (L_max=12: ~155,984; L_max=13: ~~250,000 estimated; L_max=14: ~~400,000; L_max=15: ~~640,000) |
| `L_max` | scan {12, 13, 14, 15} |
| `scan_range` | L_max ∈ {12, 13, 14, 15}; τ = τ_fold = 0.190 fixed |
| `step_size` | discrete L_max integer grid; no continuous derivative |
| `tolerance` | THEOREM exact integer match on |S_3(L_max)| |
| `scheme` | direct D_K eigenvalue extraction at each L_max; stratum-3 isolation via S86 W-12 §VII.K-PROP partition canonical |
| `convention` | 4-stratum partition canonical at τ_fold; stratum-3 = third multiplicity-class by canonical ordering |
| `random_seed` | N/A |
| `GPU path` | `torch.linalg.eigh` on AMD RX 9070 XT. **GPU feasibility check** (per `math-scripts.md` §"Machinery-Feasibility Audit"): L_max=15 D_K matrix at ~640,000 × 640,000 dense storage = 640k² × 16 bytes (complex128) = 6,553 GB → DOES NOT FIT. Use sparse representation (`torch.sparse_coo_tensor` or scipy.sparse.linalg.eigsh) for L_max ∈ {13, 14, 15}; only bottom-20 eigenvalues needed. Sparse-iterative eigensolver (Lanczos / ARPACK) is the correct path; estimated wall-time ~1-2h per L_max-point on RX 9070 XT GPU (CuPy sparse) or ~3-5h CPU (scipy.sparse.linalg.eigsh with `OMP_NUM_THREADS=8`). Total wall-time estimate ~4-6h matches effort estimate. |

### 7. Input SHA-256 pins

- `computations/canonical_constants.py` — tau_fold pin. Static; precompute SHA.
- `computations/build_dirac_operator.py` — D_K(τ, L_max) constructor parameterized over L_max. Verify the constructor scales correctly to L_max=15 before plan-freeze (sparse-matrix construction must not require dense intermediate); precompute SHA.
- S86 W-12 §VII.K-PROP partition canonical — cite by registry slot ID + line range; precompute SHA.
- `computations/s84_spectrum_cache_L12_tau019.npz` — L_max=12 baseline anchor (confirms the script reproduces the canonical bottom-20 at L_max=12 before scanning to L_max=13/14/15).

### 8. Expected output 4-tuple

`(value=cardinality_invariant_count, scheme=sparse-Lanczos-eigvalsh, convention=4-stratum-canonical-W12-stratum-3, L_max=12-15-scan)`

PASS = 4; INFO = 3 (L_max=12,13,14 invariant; 15 shifts); FAIL ≤ 2.

### 9. Substitution chain

```
Step 1: D_K(τ_fold, L_max) := finite-mode-truncation Dirac on Jensen-deformed SU(3) spectral triple
        [substrate-IS observable parameterized by L_max regulator]
Step 2: bot20(L_max) := {λ_1(L_max), ..., λ_20(L_max)} at τ_fold
Step 3: stratum_partition := same 4-stratum canonical from W-12; isolate S_3
Step 4: |S_3(L_max)| := cardinality of third multiplicity-stratum at this L_max
Step 5: PASS direction: |S_3(L_max)| invariant across {12,13,14,15}
        FAIL direction: cardinality shift at any L_max
```

No directional inequality; THEOREM equality. No [SIGN] trigger.

### 10. What PASS and FAIL mean for the solution space

- **PASS**: stratum-3 cardinality is L_max-convergent at L_max ≥ 12; the 4-stratum partition is a substrate-physical observable, not an artifact of L_max=10 truncation. Combined with W11-2 PASS, this jointly lands §VII.AJ.partition-stability sub-slot.
- **FAIL**: stratum-3 cardinality shifts with L_max; the 4-stratum partition is regulator-truncation-dependent; W-12's substrate-physics claim is downgraded to L_max=10-specific. Forces re-derivation of the partition canonical at higher L_max.
- **INFO**: convergence holds at L_max ≤ 14, breaks at 15; carry-forward to L_max=16+ scan to localize the asymptotic stability boundary.

### 11. Output artifacts

- Script: `computations/s87_w11_stratum3_lmax_scan.py` (~250-400 lines; includes sparse-eigensolver wrapper for L_max ≥ 13).
- Data: `s87_w11_stratum3_lmax_scan.npz` (keys: `lmax_grid[4]`, `bot20_per_lmax[4,20]`, `cardinality_S3_per_lmax[4]`, `pass_count`, `lmax_breakdown_threshold`).
- Plot: `s87_w11_stratum3_lmax_scan.png` (multi-panel: bot20 spectrum vs L_max; stratum-3 cardinality stability).
- Verdict line: appended to `computations/s87_gate_verdicts.txt`.
- Working-paper section: `sessions/archive/session-87/session-87-w11-workingpaper.md` §W11-3 (>15 lines).

### 12. YAML pin

```yaml
gate_id: S87-STRATUM3-LMAX-SCAN
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY
classification: GEOMETRIC
specialist_agent: connes-ncg-theorist
sister_gate: S87-PARTITION-STABILITY-4STRATUM
lmax_grid: [12, 13, 14, 15]
gpu_feasibility: sparse-Lanczos-required-at-L_max>=13
```

---

## §W11-4. CF-69 — `S87-HYPERCUBE-VERTEX-IDENTITY-LANDING`

**Source**: S86 W-12 CF-W12-4 (priority-4).

**Specialist agent**: `connes-ncg-theorist` PRIMARY + `spectral-geometer` co-sign on Sage-verify step (per spawn prompt: "spectral-geometer co-signs CF-69 (Sage-verify hypercube identity)").

**Effort**: ~2h.

### 1. Gate ID

`S87-HYPERCUBE-VERTEX-IDENTITY-LANDING`

### 2. Trigger

`[VERIFY-THEOREM]` — algebraic identity verification at d ∈ {2, 3, 4, 5}.

### 3. Classification

GEOMETRIC (algebraic-character identity on hypercube vertices; structural NCG-axiomatic).

### 4. Hypothesis being tested

The (Z_2)^d hypercube-vertex character identity holds at d ∈ {2, 3, 4, 5} as an EXACT algebraic identity (Sage-verifiable in QQ; no float arithmetic). For d=2, this is the V_4 PARALLELOGRAM IDENTITY of CF-66 (reduces to the same algebraic form). For d ≥ 3, the identity generalizes to:

```
sum over hypercube vertices v ∈ {0,1}^d of (-1)^{|v|} · A^{(g_v)} = 0
```

where g_v is the (Z_2)^d coset element labeled by binary vertex v, |v| is the Hamming weight, and A^{(g_v)} is the spectral-action moment evaluated on the v-th coset. The identity is the d-dimensional alternating-sign sum analog of the 2D parallelogram identity.

This is a STRUCTURAL theorem about the (Z_2)^d group action on spectral-action moments — it claims the alternating sum vanishes IDENTICALLY (not approximately) at every d.

### 5. Pass/fail/INFO threshold

- **PASS**: Sage `sage_simplify` returns `0` (exact algebraic zero in QQ or QQbar) at d ∈ {2, 3, 4, 5}.
  - Tolerance rule: THEOREM (exact algebraic identity; no numerical tolerance).
- **FAIL**: Sage `sage_simplify` returns a non-zero algebraic expression at any d.
- **INFO**: Sage returns a non-zero expression at d=5 ONLY (boundary effect at high d; structural identity holds at d ≤ 4).

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | 4 d-values; (2^d) coset elements per d-value: d=2 → 4 elements; d=3 → 8; d=4 → 16; d=5 → 32. Total 60 symbolic-coset evaluations. |
| `L_max` | not applicable (algebraic identity on group structure; not a spectral truncation gate). For coset action SYMBOLIC evaluation, no L_max needed. |
| `scan_range` | d ∈ {2, 3, 4, 5} |
| `step_size` | discrete d-grid |
| `tolerance` | THEOREM (Sage `sage_simplify` returns exact 0 in QQ/QQbar) |
| `scheme` | Sage MCP `sage_eval` + `sage_simplify` per `.claude/rules/math-scripts.md` §"sage-compute"; symbolic coset action implemented as character-table multiplication |
| `convention` | (Z_2)^d hypercube-vertex enumeration: vertex v ∈ {0,1}^d; g_v = ∏ g_i^{v_i} where g_1..g_d are the d generators of (Z_2)^d. |
| `random_seed` | N/A (deterministic symbolic computation) |
| `GPU path` | N/A (Sage symbolic computation; CPU only) |

### 7. Input SHA-256 pins

- S86 W-12 §EMERGENCE E-1 R3 hypercube-vertex character formulation (cite by line range 1622-1641 + extended R3 discussion lines for d > 2 generalization). Static workshop output; precompute SHA.
- `computations/_sage_call_helpers.py` (or analogous Sage MCP wrapper) — Sage callable wrapper. Precompute SHA.
- Sage MCP backend version pin (recorded via `sage_backend_info`); pin in machinery as runtime-recorded.

### 8. Expected output 4-tuple

`(value=number_of_d_values_with_exact_zero_identity, scheme=Sage-QQ-symbolic-simplify, convention=Z2_d-hypercube-vertex-alternating-sum, L_max=N/A)`

PASS = 4 (d ∈ {2,3,4,5} all give exact 0); INFO = 3 (d ∈ {2,3,4} give 0; d=5 fails); FAIL ≤ 2.

### 9. Substitution chain

```
Step 1: (Z_2)^d := Klein-d-cube group with d generators g_1..g_d, each of order 2
Step 2: vertex v ∈ {0,1}^d ↔ group element g_v := g_1^{v_1} · g_2^{v_2} · ... · g_d^{v_d}
Step 3: Hamming weight |v| := sum_i v_i
Step 4: A^{(g_v)} := character of (Z_2)^d action on substrate spectral-moment
Step 5: HYPERCUBE-VERTEX IDENTITY := sum_{v ∈ {0,1}^d} (-1)^{|v|} · A^{(g_v)} = 0
        (alternating-sign sum over all 2^d hypercube vertices)
Step 6: At d=2: sum is A^{(g_00)} − A^{(g_01)} − A^{(g_10)} + A^{(g_11)} = 0
        (this IS the V_4 PARALLELOGRAM IDENTITY of CF-66)
Step 7: PASS direction: Sage `simplify` returns exact 0 in QQ/QQbar for all d ∈ {2,3,4,5}
        FAIL direction: any d returns non-zero expression
```

No directional inequality. THEOREM identity. No [SIGN] trigger.

### 10. What PASS and FAIL mean for the solution space

- **PASS**: The (Z_2)^d hypercube-vertex character identity is a STRUCTURAL theorem of the substrate's spectral-action algebra at all tested d. Lands §VII.AJ.hypercube-identity sub-slot in `permanent-results-registry.md` (per S86 W-12 §VII.AJ OPEN reservation). Generalizes the V_4 PARALLELOGRAM IDENTITY of CF-66 from d=2 to arbitrary d. Provides the structural foundation for CF-71 (monodromy depth extension): if the (Z_2)^d identity holds at all d, then "depth" of substrate's regulator-monodromy is bounded only by the substrate's largest (Z_2)^d sub-structure.
- **FAIL**: identity breaks at some d → either (a) the (Z_2)^d generalization is wrong (V_4 identity is d=2-specific accident), OR (b) the symbolic coset-action representation has a defect. Forces structural re-derivation; downstream CF-71 is downstream-blocked.
- **INFO**: identity holds at d ∈ {2,3,4} but breaks at d=5 (boundary-of-validity finding); carry-forward to d=6+ to map the breakdown structure.

### 11. Output artifacts

- Script: `computations/s87_w11_hypercube_vertex_identity.py` (~150-250 lines; Sage MCP wrapper for symbolic identity verification).
- Data: `s87_w11_hypercube_vertex_identity.npz` (keys: `d_grid[4]`, `identity_result_per_d[4]` (string-encoded Sage outputs), `pass_count`, `coset_action_table_per_d`).
- Plot: `s87_w11_hypercube_vertex_identity.png` (visualization: hypercube graph at d=2,3,4,5 with vertex weights ±1; identity sum-tree).
- Verdict line: appended to `computations/s87_gate_verdicts.txt`.
- Working-paper section: `sessions/archive/session-87/session-87-w11-workingpaper.md` §W11-4 (>15 lines; full Sage-symbolic verification trace + co-sign attestation by spectral-geometer).

### 12. YAML pin

```yaml
gate_id: S87-HYPERCUBE-VERTEX-IDENTITY-LANDING
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY-THEOREM
classification: GEOMETRIC
specialist_agent: connes-ncg-theorist
co_sign_agent: spectral-geometer
d_grid: [2, 3, 4, 5]
sage_required: true
```

---

## §W11-5. CF-70 — `S87-3HEB-EXCESS-INHERITANCE-COMPARISON`

**Source**: S86 W-12 CF-W12-5 (priority-5).

**Specialist agent**: `volovik-superfluid-universe-theorist` (3He-B substrate authority per `feedback_agent-roster.md`; per spawn prompt "volovik recommended").

**Effort**: ~3-5h via Volovik-literature path (cites Volovik 2003 §27 BdG analysis at polycritical pressure point); ~10-15h via fresh-BdG-computation path. **Default to Volovik-lit path** unless lit-path inputs are unavailable; budget ~5h.

### 1. Gate ID

`S87-3HEB-EXCESS-INHERITANCE-COMPARISON`

### 2. Trigger

`[VERIFY]` — verify substrate's spectral-excess prediction inherits to 3He-B's polycritical pressure point.

### 3. Classification

PHONONIC (the 3He-B BdG quasiparticle spectrum is a phononic-excitation laboratory analog of the substrate's BdG spectral excess).

### 4. Hypothesis being tested

The substrate's **BdG-undoubled spectral excess at first-order coexistence** (a structural prediction of the substrate's spectral-action moments at τ_fold) inherits to 3He-B at the polycritical pressure point (P_pc ≈ 2.13 MPa, T ≈ 0.93 mK in 3He phase diagram) via the inheritance morphism `ι : (A_K, H_K, D_K) → (BdG-3He-B sector)` per `inheritance-falsifier-protocol.md`.

The substrate-IS observable is the BdG-undoubled spectral excess `δN_BdG := N_BdG_undoubled(τ_fold) − 2·N_paired(τ_fold)`, where N_BdG_undoubled is the number of unpaired BdG quasiparticle states at first-order coexistence and N_paired is the paired-state count. The laboratory-IN observable is the analog 3He-B excess at the polycritical point: `δN_3HeB(P_pc, T_pc)`, which can be extracted from Volovik 2003 §27 BdG quasiparticle-density analysis or computed fresh from the BdG Hamiltonian on the 3He-B Fermi surface at the polycritical point.

### 5. Pass/fail/INFO threshold

- **PASS**: Substrate prediction matches 3He-B literature value within Volovik 2003 §27 reported uncertainty (typically ±5% for BdG quasiparticle counts at polycritical pressures). Inheritance morphism cancellation theorem `(Δ_B/Δ_A)^p` (per `inheritance-falsifier-protocol.md`) preserves the ratio `δN_substrate / N_paired_substrate = δN_3HeB / N_paired_3HeB` at relative tolerance ≤ 5%.
  - Tolerance rule: RATIO 5% relative; matches Volovik-lit-path uncertainty.
- **FAIL**: ratio mismatch > 25% (5× the lit-uncertainty band); indicates inheritance morphism does not preserve the spectral-excess structure (substrate prediction does not extend to 3He-B at polycritical point).
- **INFO**: ratio mismatch in (5%, 25%] band — indicates partial inheritance, possibly due to neglected M_3(C) contributions in the inheritance kernel ker(ι_*) (per `cross-pillar-bridge-anatomy.md` 5-element anatomy).

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | substrate side: full bottom-K spectrum at τ_fold (K ≈ 100-200 for BdG-undoubled excess characterization); 3He-B side: literature extraction from Volovik 2003 §27 (no eval) OR fresh BdG diagonalization on 3He-B Fermi surface at polycritical point (~10⁵ k-points × 4-band BdG Hamiltonian = ~4×10⁵ eigenvalues) |
| `L_max` | 10 (substrate side; canonical) |
| `scan_range` | substrate: τ = τ_fold = 0.190 ONLY; 3He-B: P = P_pc = 2.13 MPa, T = T_pc = 0.93 mK FIXED at polycritical point |
| `step_size` | N/A (single-point evaluation on each side) |
| `tolerance` | RATIO 5% PASS; (5%, 25%] INFO; > 25% FAIL |
| `scheme` | substrate side: BdG-undoubled spectral excess via spectral-action substrate-distance-1 pole (s=3) Mellin-cone callable. 3He-B side (lit-path): transcribe Volovik 2003 §27 BdG quasiparticle density at polycritical point. 3He-B side (fresh-path, fallback): BdG Hamiltonian H_BdG = (ε_k - μ)·τ_3 + Δ(k)·τ_1 with Δ(k) = Δ_0·(d-vector) for B-phase; diagonalize on Fermi-surface k-grid; count unpaired states at coexistence boundary. |
| `convention` | substrate side: substrate-distance-1-MELLIN; 3He-B side: Volovik-2003-Sec-27-polycritical (lit-path) OR fresh-BdG-B-phase-d-vector (fallback) |
| `random_seed` | N/A (deterministic) |
| `GPU path` | substrate: cached spectrum (no diagonalization). 3He-B fresh-path: `torch.linalg.eigh` on AMD RX 9070 XT for BdG diagonalization on k-grid; well within VRAM at ~10⁵ k-points × 4×4 BdG matrix. Lit-path: no compute. |

### 7. Input SHA-256 pins

- `computations/canonical_constants.py` — tau_fold pin, M_KK pin. Static; precompute SHA.
- `computations/s84_spectrum_cache_L12_tau019.npz` — substrate D_K(τ_fold) eigenvalues. Static; precompute SHA.
- `computations/_spectral_action_regulators.py` — Mellin-cone callable for substrate-distance-1 pole. level pin: PRIMARY (full physical Mellin-cone).
- Volovik 2003 §27 (3He-B BdG analysis at polycritical point) — METHODOLOGICAL cross-check citation per `substrate-first-canonical-sourcing.md` §(i) "When external-paper provenance is methodological vs canonical". The substrate-IS observable canonical is the substrate's spectral-action computation; Volovik 2003 is the lab-IN measurement reference. Methodological citation is correct usage here. Precompute SHA over the cited section.
- `sessions/permanent-results-registry.md:§VII.W` — Pillar III ↔ IV bridge anatomy template (5 IS-not-IN elements + 3-level ladder). CF-70 follows the same anatomy. Static; precompute SHA.

### 8. Expected output 4-tuple

`(value=relative_ratio_mismatch_substrate_vs_3HeB, scheme=Mellin-cone-substrate-distance-1-vs-Volovik-2003-Sec-27, convention=BdG-undoubled-excess-ratio, L_max=10)`

PASS = ratio mismatch ≤ 0.05; INFO = (0.05, 0.25]; FAIL > 0.25.

### 9. Substitution chain

```
Step 1: δN_BdG_substrate := N_unpaired(τ_fold) − 2·N_paired(τ_fold)   [substrate-IS observable]
        evaluated via Mellin-cone substrate-distance-1 pole on cached D_K(τ_fold) spectrum
Step 2: δN_3HeB(P_pc, T_pc) := lab analog at 3He-B polycritical point   [laboratory-IN observable]
        from Volovik 2003 §27 (lit-path) or fresh BdG Hamiltonian diagonalization
Step 3: substrate ratio R_substrate := δN_substrate / N_paired_substrate
        3He-B ratio R_3HeB := δN_3HeB / N_paired_3HeB
Step 4: Inheritance morphism (Δ_B/Δ_A)^p cancellation theorem (inheritance-falsifier-protocol.md):
        R_3HeB = R_substrate · 1   [the (Δ_B/Δ_A)^p factor cancels exactly when both observables
                                    share the same Δ-scaling exponent p]
Step 5: PASS criterion: |R_substrate − R_3HeB| / max(|R_substrate|, |R_3HeB|) ≤ 0.05
        FAIL criterion: ratio mismatch > 0.25
```

The inheritance ratio test relies on the (Δ_B/Δ_A)^p cancellation; both the substrate and 3He-B observables are dimensionless ratios of countable BdG-states, so p = 0 trivially, and the cancellation theorem applies. No directional sign claim — pure equality test. No [SIGN] trigger.

### 10. What PASS and FAIL mean for the solution space

- **PASS**: The substrate's BdG-undoubled spectral excess inherits to 3He-B at polycritical pressure with the predicted ratio. This is a CROSS-PILLAR BRIDGE result (substrate ↔ 3He-B laboratory) — extends §VII.W (Pillar III ↔ IV bridge) to the BdG-undoubled-spectrum-excess channel. Lands a new row in `sessions/framework/registry/falsifier-master-inventory.md` (NOT a §VII.AJ entry — falsifier rows are inventory entries, not registry theorems). 3He-B becomes a substrate-falsifier platform for the spectral-excess prediction.
- **FAIL**: ratio mismatch > 25% — inheritance morphism does NOT preserve the spectral-excess structure into 3He-B at polycritical pressure. Closes the corridor "substrate's spectral-excess prediction is universal (in the inheritance-morphism sense)"; substrate's prediction is τ_fold-specific (or platform-specific to the substrate's own SU(3) fiber). Forces re-examination of inheritance kernel ker(ι_*) — the M_3(C) sub-algebra contributions may not be negligible.
- **INFO**: partial inheritance (5%-25% mismatch) — informative; suggests inheritance morphism preserves the LEADING-order structure but neglected M_3(C) contributions cause O(20%) corrections. Carry-forward: extend the inheritance kernel analysis to include M_3(C) cocycles.

### 11. Cross-pillar bridge anatomy declaration (per `cross-pillar-bridge-anatomy.md`)

Per `cross-pillar-bridge-anatomy.md` STRUCTURAL REQUIREMENT, this gate's verdict-line declaration MUST include all 5 IS-not-IN anatomy elements:

1. **Substrate-IS observable**: `δN_BdG_substrate(τ_fold)` evaluated on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` via Mellin-cone substrate-distance-1 pole.
2. **Laboratory-IN observable**: 3He-B BdG-undoubled spectral excess at polycritical point P_pc ≈ 2.13 MPa, T_pc ≈ 0.93 mK (Volovik 2003 §27).
3. **Bridge map**: inheritance morphism `ι : (A_K, H_K, D_K) → BdG-3He-B sector` per `inheritance-falsifier-protocol.md`; (Δ_B/Δ_A)^p cancellation theorem at p=0 reduces the bridge to ratio-preservation.
4. **Algebraic envelope**: At leading order in the inheritance kernel rank-truncation (assuming ker(ι_*) M_3(C) contributions negligible), R_3HeB = R_substrate to machine precision. Sub-leading corrections from non-negligible ker(ι_*) generators bound the discrepancy to ≤ ~5% per Volovik 2003 §27 lit-uncertainty.
5. **Empirical anchor**: Volovik 2003 §27 reported value at P_pc = 2.13 MPa, T_pc = 0.93 mK; substrate prediction matches at relative 5% PASS band.

3-level ladder per `cross-pillar-bridge-anatomy.md`:
- **Level 1 (substrate-IS structural identity)**: `R_substrate = ‖δN‖_{spectral-distance-1, τ_fold} / ‖N_paired‖` is regulator-invariant at substrate-distance-1 Mellin pole.
- **Level 2 (algebraic convergence envelope)**: At leading order in inheritance kernel rank, 0% deviation; sub-leading corrections bounded by ker(ι_*) M_3(C) cocycle norm.
- **Level 3 (empirical anchor at canonical L_max)**: numerical evaluation at L_max=10 + 3He-B polycritical-point lit value; PASS if Level-3 mismatch ≤ Level-2 envelope.

Level 3 must satisfy Level 2 for registry-PASS; if PASS, the bridge entry is registry-eligible at falsifier-master-inventory (NOT §VII.AJ — falsifier rows are inventory, not registry).

### 12. Output artifacts

- Script: `computations/s87_w11_3heb_excess_inheritance_comparison.py` (~200-400 lines depending on lit-path vs fresh-path).
- Data: `s87_w11_3heb_excess_inheritance_comparison.npz` (keys: `R_substrate`, `R_3HeB_lit`, `R_3HeB_fresh` (optional, fallback path only), `ratio_mismatch`, `inheritance_kernel_rank`, `path_used` ∈ {'lit', 'fresh'}).
- Plot: `s87_w11_3heb_excess_inheritance_comparison.png` (substrate vs 3He-B excess ratio comparison; uncertainty bands).
- Verdict line: appended to `computations/s87_gate_verdicts.txt`.
- Working-paper section: `sessions/archive/session-87/session-87-w11-workingpaper.md` §W11-5 (>15 lines; full 5-element IS-not-IN anatomy + 3-level ladder declaration).

### 13. YAML pin

```yaml
gate_id: S87-3HEB-EXCESS-INHERITANCE-COMPARISON
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY
classification: PHONONIC
specialist_agent: volovik-superfluid-universe-theorist
cross_pillar_bridge: true
bridge_pillars: [substrate_BdG, 3HeB_BdG]
inheritance_morphism: ι_substrate_to_3HeB
delta_cancellation_p: 0
preferred_path: lit
fallback_path: fresh
```

---

## §W11-6. CF-71 — `S87-MONODROMY-DEPTH-EXTENSION`

**Source**: S86 W-12 CF-W12-6 (latent / NOT pre-registered in W-12 source). Per `feedback_fix-in-session-never-defer.md` 4-field stub format, this is treated as a forward-research gate.

**Specialist agent**: `connes-ncg-theorist`.

**Effort**: ~6-10h.

### 1. Gate ID

`S87-MONODROMY-DEPTH-EXTENSION`

### 2. Trigger

`[VERIFY]` — verify substrate's regulator-monodromy depth d=2 exactness vs d>2 atlas extension.

### 3. Classification

GEOMETRIC (substrate-axiomatic monodromy structure).

### 4. Hypothesis being tested

The substrate's regulator-monodromy depth `d_monodromy` is **exactly 2** (i.e., the (Z_2)^d substructure of the substrate's regulator-monodromy group is faithful at d=2 only; no non-trivial d>2 atlas extension exists). The alternative is that some d>2 atlas extension yields a non-trivial (Z_2)^d sub-monodromy whose hypercube-vertex character identity (CF-69) is non-vacuous.

The forward-research aspect: there is no S86 W-12 pre-registration of how to construct the d>2 atlas extension. CF-71 must FIRST construct candidate d>2 atlas extensions (e.g., enriching the substrate's 5-class regulator atlas A_5 to a 6-class A_6 by adding a new Mellin-cone pole, or enriching the (Z_2)^2 V_4 monodromy by adding a third Z_2 generator from a non-Mellin regulator), and SECOND test whether the new (Z_2)^d structure satisfies the CF-69 hypercube identity non-trivially (i.e., the d=3 identity holds AND no degenerate sub-cube collapse occurs).

### 5. Pass/fail/INFO threshold

This gate has TWO possible PASS modes:
- **PASS-d=2-exact**: No d>2 atlas extension exists with non-trivial monodromy. Empirically demonstrated by enumerating candidate d>2 extensions and showing each one (a) fails the (Z_2)^d sub-group structure (i.e., the third generator commutes trivially), OR (b) the d=3 hypercube identity reduces to the d=2 V_4 identity (degenerate sub-cube). At LEAST 3 candidate extensions tested.
- **PASS-d>2-extension**: A d>2 atlas extension is constructed AND its hypercube identity is non-trivially independent of d=2 sub-cubes. Empirically demonstrated by Sage-verifying the d=3 hypercube identity at the constructed atlas A_6.
- **FAIL**: <3 candidate d>2 extensions tested OR all candidates ambiguous (cannot conclusively classify as degenerate or non-trivial).
- **INFO**: 1-2 candidate d>2 extensions tested, all classified, but breadth insufficient to claim d=2 exactness.

Tolerance rule: STRUCTURAL (theorem-grade enumeration outcome; not a numerical threshold).

### 6. Machinery pin (PRDR)

| Field | PIN |
|:------|:----|
| `N_eval` | enumerate candidate d>2 extensions; minimum 3 extensions required for PASS. Each extension requires CF-69-style hypercube identity verification at d=3. |
| `L_max` | 10 (canonical) for any extensions involving Mellin-cone substrate-distance-{0,1,2,3} poles |
| `scan_range` | candidate extension space: enumerate (a) atlas-extension routes (A_5 → A_6 by adding sixth regulator), (b) generator-extension routes (V_4 + new Z_2 from non-Mellin regulator); min 3 distinct candidates. |
| `step_size` | discrete enumeration |
| `tolerance` | STRUCTURAL — for each candidate, classify as `degenerate` (reduces to d=2 sub-cube) or `non-trivial` (genuine d=3 monodromy) |
| `scheme` | Sage-symbolic identity verification per CF-69; cross-link to W-8 CF-49 (sixth-regulator promotion) and W-9 CF-58 (pole-specificity scan at s=4) for atlas-extension routes |
| `convention` | latent-gate forward-research per `feedback_fix-in-session-never-defer.md` 4-field stub |
| `random_seed` | N/A |
| `GPU path` | N/A (Sage symbolic + small-spectrum sanity checks) |

### 7. Input SHA-256 pins

- CF-66 verdict line (from `computations/s87_gate_verdicts.txt` after CF-66 closes) — V_4 monodromy at d=2 baseline. CF-71 is downstream-dependent on CF-66 PASS. <computed-at-runtime>
- CF-69 verdict line — hypercube identity at d ∈ {2,3,4,5}. CF-71 is downstream-dependent on CF-69 PASS at d=3 minimum. <computed-at-runtime>
- W-8 CF-49 atlas-extension carry-forward source (`session-86/session-86-w8-workshop.md` for sixth-regulator candidate enumeration). Static; precompute SHA.
- W-9 CF-58 pole-specificity scan at s=4 carry-forward source. Static; precompute SHA.
- `computations/_sage_call_helpers.py` — Sage MCP wrapper. Precompute SHA.

### 8. Expected output 4-tuple

`(value=number_of_candidate_extensions_classified, scheme=Sage-symbolic-identity-enumeration, convention=monodromy-depth-extension-research, L_max=10)`

PASS-d=2-exact = ≥3 candidates all classified `degenerate`; PASS-d>2-extension = ≥1 candidate classified `non-trivial`; INFO = 1-2 candidates classified; FAIL = <1 candidate or unclassifiable.

### 9. Substitution chain

```
Step 1: d_monodromy := faithful-(Z_2)^d depth of substrate's regulator-monodromy group at τ_fold
        [substrate-axiomatic property; W-12 CF-66 establishes d ≥ 2]
Step 2: Hypothesis A (d=2-exact): for all candidate d>2 atlas extensions e, the resulting (Z_2)^d
        sub-monodromy is degenerate (reducible to a d=2 sub-cube via generator collapse)
Step 3: Hypothesis B (d>2-extension): exists candidate e such that the resulting (Z_2)^d
        sub-monodromy is non-trivially d=3 (non-reducible)
Step 4: Discrimination protocol: enumerate candidates {e_1, e_2, e_3, ...}; for each, verify
        the d=3 hypercube identity (CF-69 at d=3) and check whether the result is independent
        of d=2 sub-cubes (non-degenerate) or reduces to V_4 (degenerate).
Step 5: PASS-d=2-exact direction: all candidates degenerate
        PASS-d>2-extension direction: at least one candidate non-trivial
        FAIL: insufficient candidates tested
```

No directional inequality on a continuous scalar; STRUCTURAL classification. No [SIGN] trigger.

### 10. What PASS and FAIL mean for the solution space

- **PASS-d=2-exact**: substrate's regulator-monodromy depth is exactly 2. Closes the corridor for d>2 substrate enrichments. Lands §VII.AJ.depth-exactness sub-slot. Constrains future atlas-extension proposals (any new regulator must commute trivially with V_4 generators).
- **PASS-d>2-extension**: substrate's regulator-monodromy depth is ≥ 3 under the constructed atlas extension. Opens new substrate-enrichment corridor; the constructed d>2 extension becomes a new substrate-axiomatic feature. Forces re-examination of CF-49 (sixth-regulator promotion) and CF-58 (pole-specificity scan at s=4) — the new generator may be sourced from these forward-gates.
- **FAIL** (insufficient candidates): forward-research gate stalled; carry-forward to S88+ with refined construction protocol.
- **INFO** (1-2 candidates classified): partial classification; carry-forward to expand candidate set to ≥3.

### 11. Output artifacts

- Script: `computations/s87_w11_monodromy_depth_extension.py` (~250-500 lines; candidate-extension enumerator + Sage-symbolic identity verifier per candidate).
- Data: `s87_w11_monodromy_depth_extension.npz` (keys: `candidate_extensions[N]` (string-encoded), `classification_per_candidate[N]` ∈ {'degenerate', 'non-trivial', 'unclassifiable'}, `pass_mode` ∈ {'d=2-exact', 'd>2-extension', 'INFO', 'FAIL'}, `n_classified`).
- Plot: `s87_w11_monodromy_depth_extension.png` (candidate-extension landscape; degenerate-vs-non-trivial classification map).
- Verdict line: appended to `computations/s87_gate_verdicts.txt`.
- Working-paper section: `sessions/archive/session-87/session-87-w11-workingpaper.md` §W11-6 (>15 lines; full candidate enumeration + classification audit trail).

### 12. YAML pin

```yaml
gate_id: S87-MONODROMY-DEPTH-EXTENSION
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
trigger: VERIFY
classification: GEOMETRIC
specialist_agent: connes-ncg-theorist
forward_research_gate: true
latent_in_W12_source: true
upstream_dependencies: [S87-MONODROMY-V_4-EXPLICIT, S87-HYPERCUBE-VERTEX-IDENTITY-LANDING]
pass_modes: [d=2-exact, d>2-extension]
min_candidates_for_PASS: 3
```

---

## Wave 11 → Wave 12 Decision Point

Wave 11 closes the W-12 (S86) carry-forward thread. Forward decisions:

| Outcome of W11-1 (CF-66 V_4) | Outcome of W11-2/3 (partition stability) | Outcome of W11-4 (hypercube identity) | Outcome of W11-5 (3He-B inheritance) | Outcome of W11-6 (depth extension) | W12+ action |
|:----------------------------|:----------------------------------------|:--------------------------------------|:------------------------------------|:----------------------------------|:------------|
| PASS | PASS | PASS | PASS | PASS-d=2-exact | Land §VII.AJ.{V_4-monodromy, partition-stability, hypercube-identity, depth-exactness} 4-sub-row registry promotion at S87 close. CF-70 lands falsifier-master-inventory row. Forward to S88 (Stage-2 cross-reviewer cross-check on Joint F_2-Class Path-(c) Theorem CF-59 elsewhere). |
| PASS | PASS | PASS | INFO | PASS-d=2-exact | Land §VII.AJ 4-sub-row; CF-70 INFO carry-forward to S88 (extend inheritance kernel to include M_3(C) cocycles). |
| PASS | PASS | PASS | PASS | PASS-d>2-extension | Land §VII.AJ 4-sub-row with d>2-extension augmentation; cross-link to CF-49 (sixth-regulator) and CF-58 (pole-specificity at s=4) which now have a new structural anchor. |
| PASS | INFO | INFO | * | * | Land §VII.AJ V_4-monodromy + hypercube-identity rows; partition stability sub-row carry-forward to S88 with finer δ_τ scan + L_max ≥ 16 scan. |
| FAIL on CF-66 | * | * | * | * | DOWNSTREAM-BLOCKED: CF-67/CF-68/CF-69/CF-71 are all conditioned on V_4 monodromy. FAIL forces re-derivation of W-12 monodromy structure; re-open the Z_4 candidate or alternative non-abelian groups. Carry-forward at S88 with full structural re-examination. |
| INFO on CF-66 | * | * | * | * | Re-run CF-66 with Sage-mpmath arbitrary-precision per `math-scripts.md` §"Sage-Exact Rationals"; downstream gates conditional. |

**Wave 11 closure criterion**: All 6 verdict lines emitted to `computations/s87_gate_verdicts.txt` with full S87+ schema-v2 (canonical line + dual-SHA companion + 3-tuple annotation where applicable); §W11-1..6 working-paper sections each ≥15 lines with substantive content; v3 ladder PRU + SOURCE-RECON + SUBSTRATE-FIRST-PROVENANCE audits PASS (or fall through to v3-closure-recovery Stage 1/2 per `v3-closure-recovery.md`).

---

## Wave 11 Machinery-Enumeration Pin (§0.11)

Per PRDR (Pre-Registration Dry-Run) discipline (`epistemic-discipline.md` §"Pre-Registration Completeness"), the per-gate machinery-pin tables in §W11-1..6 enumerate every free parameter accessible to the producing scripts. PRU cardinality D_PRU_raw = 0 expected at plan-freeze (no missing pins).

### Aggregate Machinery Manifest

| Pin name | Source | Used by gate(s) |
|:---------|:-------|:----------------|
| `tau_fold = 0.190` | canonical_constants.py:1243 | W11-1, W11-2, W11-3, W11-5 |
| `M_KK` | canonical_constants.py | W11-1, W11-5 |
| `L_max = 10` | canonical (S84) | W11-1, W11-2, W11-5 |
| `L_max ∈ {12, 13, 14, 15}` | scan-range pin | W11-3 |
| `δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10}` | scan-range pin | W11-2 |
| `d ∈ {2, 3, 4, 5}` | scan-range pin | W11-4 |
| 4-stratum partition canonical | S86 W-12 §VII.K-PROP partition row | W11-2, W11-3 |
| V_4 coset enumeration g_0..g_3 | S86 W-12 §EMERGENCE E-1 R3 lines 1622-1641 | W11-1, W11-4 |
| Mellin-cone substrate-distance-{0,1,2,3} pole structure | regulator-pin-discipline.md (PRIMARY) | W11-1, W11-5 |
| Sage MCP backend (sage_eval, sage_simplify) | math-scripts.md §sage-compute | W11-4, W11-6 |
| Polycritical pressure point (P_pc, T_pc) | Volovik 2003 §27 (lit-path) | W11-5 |
| Inheritance morphism (Δ_B/Δ_A)^p, p=0 | inheritance-falsifier-protocol.md | W11-5 |
| `OMP_NUM_THREADS = 8` (CPU fallback) | math-scripts.md §Environment | W11-1 (CPU path), W11-2 |
| `torch.linalg.eigh` (GPU path) | math-scripts.md §Environment | W11-2, W11-3 (sparse) |
| Random seed | N/A all gates (deterministic) | — |

### GPU feasibility table

| Gate | GPU path | Feasibility |
|:-----|:---------|:------------|
| W11-1 | CPU (cached spectrum lookup; no eigendecomposition) | OK |
| W11-2 | torch.linalg.eigh on D_K(τ) at L_max=10 | OK; D_K dimension ~155k, fits VRAM |
| W11-3 | sparse Lanczos / scipy.sparse.linalg.eigsh | OK at L_max=12,13,14; L_max=15 requires sparse-iterative (NOT dense; dense storage 6.5 TB) |
| W11-4 | CPU (Sage symbolic) | OK |
| W11-5 | torch.linalg.eigh on BdG-3HeB Hamiltonian (fresh path) | OK; ~10⁵ k-points × 4×4 matrix is trivial |
| W11-6 | CPU (Sage symbolic + small enumeration) | OK |

---

## Wave 11 Input-SHA Ledger

All input-pin SHAs are computed at plan-freeze time per PRDR. Static files are SHA-pinned; runtime-computed dependencies (verdict-line SHAs from upstream gates) are marked `<computed-at-runtime>`.

| Input file | Type | Used by | SHA |
|:-----------|:-----|:--------|:----|
| `computations/canonical_constants.py` | static | W11-1, W11-2, W11-3, W11-5 | <plan-freeze> |
| `computations/s84_spectrum_cache_L12_tau019.npz` | static | W11-1, W11-2, W11-3, W11-5 | <plan-freeze> |
| `computations/build_dirac_operator.py` | static | W11-2, W11-3 | <plan-freeze> |
| `computations/_spectral_action_regulators.py` | static | W11-1, W11-5 | <plan-freeze> |
| `computations/_sage_call_helpers.py` | static | W11-4, W11-6 | <plan-freeze> |
| `sessions/archive/session-86/s86_w12_workingpaper.md` lines 1622-1641 (V_4 cosets) | static | W11-1, W11-4 | <plan-freeze> |
| `sessions/permanent-results-registry.md:§VII.K-PROP partition row` | static | W11-2, W11-3 | <plan-freeze> |
| `sessions/permanent-results-registry.md:§VII.W` (bridge anatomy template) | static | W11-5 | <plan-freeze> |
| Volovik 2003 §27 (3He-B BdG analysis at polycritical point) | static (paper citation) | W11-5 | <plan-freeze> |
| `sessions/archive/session-86/session-86-w8-workshop.md` (CF-49 source) | static | W11-6 | <plan-freeze> |
| `sessions/archive/session-86/session-86-w9-workshop.md` (CF-58 source) | static | W11-6 | <plan-freeze> |
| CF-66 verdict line (from `computations/s87_gate_verdicts.txt`) | runtime | W11-6 | <computed-at-runtime> |
| CF-69 verdict line (from `computations/s87_gate_verdicts.txt`) | runtime | W11-6 | <computed-at-runtime> |

### Plan-freeze SHA computation note

Plan-freeze SHA computation runs after the wave plan is written but before dispatch. The orchestrator runs:

```bash
python computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w11.md
python computations/_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w11.md
python computations/_source_reconciliation_audit.py
```

before Wave 11 dispatch. SOURCE-RECON Class-(c) PIN-DRIFT scan should target any stale-source citation of W-12 lines 1622-1641 (verify the line numbers still match the workshop-output file). SUBSTRATE-FIRST-PROVENANCE manual review on CF-70 (verify Volovik 2003 §27 citation is METHODOLOGICAL cross-check, not CANONICAL replacement of the substrate's spectral-action computation).

---

## Notes for Specialist Agents

- **CF-66 (V_4 explicit)**: Be explicit about the supersession-event in the verdict-line `value=` field. Do NOT retain the Z_4 pre-registration. Cite PRU Class 8.2 calibration in the working-paper §W11-1 section.
- **CF-67/68 sister gates**: Coordinate τ-axis (W11-2) and L_max-axis (W11-3) results; the JOINT structural finding is "4-stratum partition is stable in BOTH axes" (or finds the breakdown). Do not synthesize joint conclusion until BOTH gates close.
- **CF-69 hypercube identity**: MANDATORY use Sage MCP `sage_eval` + `sage_simplify` per `.claude/rules/math-scripts.md` §"sage-compute" — float-arithmetic verification at d=4,5 is structurally insufficient (the identity is exact at every d; floats lose precision in symbolic algebraic manipulation). Co-sign attestation from spectral-geometer required in §W11-4 working-paper section.
- **CF-70 3He-B inheritance**: Default to Volovik-lit-path (~3-5h); fresh-BdG path (~10-15h) only if lit-path inputs unavailable. Cross-pillar bridge anatomy (5 IS-not-IN elements + 3-level ladder) MANDATORY in working-paper §W11-5 per `cross-pillar-bridge-anatomy.md` STRUCTURAL REQUIREMENT.
- **CF-71 depth extension**: Forward-research gate; minimum 3 candidate d>2 extensions enumerated for any PASS verdict. Cross-link to CF-49 (sixth-regulator promotion) and CF-58 (pole-specificity at s=4) as candidate-extension sources.

---

**Plan-freeze date**: 2026-04-27.
**Plan author**: connes-ncg-theorist (workshop participant per S86 W-12 attribution).
**Sources**: `sessions/session-plan/session-87-context.md` §1 + §2 (CF-66..CF-71); S86 W-12 workshop closure; `agent-standards.md` §"HIGH-DENSITY WORKSHOP TEMPLATE T2-5" (PRU Class 8.2 calibration); `cross-pillar-bridge-anatomy.md` (CF-70 anatomy); `inheritance-falsifier-protocol.md` (CF-70 cancellation theorem); `math-scripts.md` §"sage-compute" (CF-69 + CF-71 Sage discipline).
