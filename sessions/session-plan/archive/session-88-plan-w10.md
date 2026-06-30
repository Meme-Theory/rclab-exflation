# Session 88 Plan — Wave 10: W8 atlas + Bulletin #3/#4 + ρ_∞ + L1↔L2 axis

> **Theme**: W8 atlas remediation (cluster J, items 110-115) + Bulletin #3/#4 ρ_∞ landing + L1↔L2 axis composition (cluster K, items 116-120).
> **PRIMARY**: connes-ncg-theorist (substrate-physics + NCG-axiomatic + Mellin-cone substrate-distance pole structure)
> **CO-AUTHOR**: lizzi-spectral-functional-theorist (ensemble-level admissibility + observable-promotion authority)
> **AUDIT EXTENSION**: gen-physicist (audit-script extensions for items #115, #118)
> **WRITER**: mack-cosmic-bridge (rule-file pin for item #119, sole-writer per `feedback_mack-bridge-role.md`)

`verdict_source: computations/session-88/s88_gate_verdicts.txt`

---

## Wave 10 Summary

This wave executes 11 carry-forwards from S87 spanning two clusters:

**Cluster J (items 110-115)** — W8 atlas + ensemble + cache regen:
- Investigate A_4 → A_2 substrate-axiom-strict cascade
- Re-derive W-8 §VII.K-PROP A/B/C-trio under ensemble-level admissibility
- Regenerate L_max=14 cache and re-run §W8-4/§W8-5/§W8-6
- Extend `_source_reconciliation_audit.py` for plan-time filename-existence audit

**Cluster K (items 116-120)** — Bulletin #3/#4 + ρ_∞ + L1↔L2 axis:
- Bulletin #3 SOURCE-RECONCILIATION class-(c) PIN-DRIFT audit
- Re-emit §W10-3 with full lizzi promotion-authority dispatch
- Extend `_source_reconciliation_audit.py` for class-(b) PIN-LOOSE-SOURCE-TIGHT pattern (literal numerical pin tighter than structural-form-with-unpinned-coefficient)
- Per-Bulletin-per-pole Level-1 wall classification rule-file pin (cross-pillar-bridge-anatomy)
- Conditional dispatch shell for cross-distance theorem (DORMANT until future Bulletin lands at different substrate-distance pole)

The wave is structured as a MIXED-class wave per `wave-classification.md`: items #110-114 + #116-117 + #120 are GEOMETRIC/COMPUTE-class (substrate-physics with pre-registered numerical thresholds); items #115 + #118 + #119 are METHODOLOGY-class (audit-script extensions + rule-file pin). Per the NROY clause (`wave-classification.md` §"NROY clause"), the wave is sub-decomposed at the item level: each item carries its own classification, and the dispatch path branches on classification (compute-mode for COMPUTE-class; orchestrator-direct-write for METHODOLOGY-class).

---

## Wave 10 Decision Point Prerequisites

| Item | Prereq verdicts | Status at plan-freeze |
|:-----|:---------------|:----------------------|
| #110 | S87 W4-2 A_5 → A_4 cascade landing | LANDED `audit_sha256=a289004bff9ac728dd25f001cd65fc8df5fac2ac146897185f1b6ceeb569d270` |
| #111 | W-8 §VII.K-PROP A/B/C-trio L2-FULLY-ADMISSIBLE registry entry | LANDED at `permanent-results-registry.md` §VII.K-PROP-W8 |
| #112 | s84_spectrum_cache_L12_tau019.npz (master cache) | EXISTS at `computations/session-84/s84_spectrum_cache_L12_tau019.npz` |
| #113 | Connes-Chamseddine 1996 Mellin-cone live-evaluator module | SCHEMATIC at `computations/_shared/_spectral_action_regulators.py`; live-physical lift requires canonical D_K Peter-Weyl spectrum cache |
| #114 | XOR independence test partial cells from §W8-6 | PARTIAL (T,T) + (F,T) + (F,F) populated; (T,F) cell empty |
| #115 | `_source_reconciliation_audit.py` post-V.2 extension target | EXISTS; extension hook open |
| #116 | W-10 R3-B EMERGENCE E1 spectral-moment-realization claim | LANDED in workshop; SOURCE-RECON Class-(c) audit pending |
| #117 | #116 verdict | CONDITIONAL ON #116 ∈ {PASS, INFO} |
| #118 | W10-2 inconsistency pattern (literal numerical pin tighter than structural-form-with-unpinned-coefficient) | DOCUMENTED in S87 W10-2 verdict trace |
| #119 | `cross-pillar-bridge-anatomy.md` Level-1/2/3 ladder | LANDED at `.claude/rules/cross-pillar-bridge-anatomy.md` |
| #120 | Future Bulletin landing at different substrate-distance pole | NOT YET LANDED; dormant shell only |

---

## §W10-110 — S88-CF-W8-A1-A4-A2-CASCADE-INVESTIGATION

**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (substrate-physics, COMPUTE-class)
**Agent**: connes-ncg-theorist (PRIMARY)

### Hypothesis
Under W-8 §VII.K-PROP A/B/C-trio admissibility analysis, the substrate-axiom-strict cascade A_4 → A_2 is either (i) a convention artifact of CM-in-x vs CM-in-λ Mellin parameterization, or (ii) a genuine atlas-cardinality reduction whose structural cause is the `cutoff_sqrt` regulator's failure to satisfy NCG axiom 5 (regularity) at substrate-distance-1 poles.

**Reading_1 (CONVENTION-ARTIFACT)**: A_4 includes 2 regulators that are CM-in-x equivalents of A_2 regulators under the Mellin-Barnes substrate-distance-1 parameterization; the cardinality reduction is a parameterization redundancy, not a structural exclusion. Predicted PASS condition: bit-identical λ-spectrum at L_max=10 across A_2 ⊂ A_4 substrate-pair under the CM-in-λ parameterization (rel_diff ≤ 1e-12).

**Reading_2 (STRUCTURAL-EXCLUSION)**: A_4 \ A_2 contains regulators that fail NCG axiom 5 (regularity) at substrate-distance-1 poles structurally; the cascade is a genuine atlas-cardinality reduction. Predicted PASS condition: λ-spectrum at L_max=10 differs across A_2 ⊂ A_4 substrate-pair (rel_diff > 1e-9 on at least 1 of the 4 §VII.K-PROP regulators).

### Method
1. Load s84_spectrum_cache_L12_tau019.npz; extract bot-K=20 D_K eigenvalues at τ_fold=0.190.
2. Apply 4-channel layer-2 §VII.K-PROP regulator-weighted Mellin moments at substrate-distance-1 pole s=3 under both CM-in-x and CM-in-λ parameterizations.
3. Compute moment vectors `M^{(A_2)}` (under A_2 = {ζ, Zubarev}) and `M^{(A_4)}` (under A_4 = {ζ, Zubarev, SDW, anomaly}).
4. Bit-compare `M^{(A_4)}|_{A_2-subset}` vs `M^{(A_2)}` under each parameterization separately.

### Machinery pin
- `M_KK = canonical_constants.M_KK` (substrate-natural mass scale)
- `tau_fold = canonical_constants.tau_fold = 0.190`
- L_max = 10 (operational), 12 (cache truncation level)
- substrate_distance_pole = 3 (s=3 Mellin pole, apex-universal per S85-W6-5-MELLIN-CONE-EXT)
- regulator_atlas_A_2 = ["zeta", "zubarev"]
- regulator_atlas_A_4 = ["zeta", "zubarev", "SDW", "anomaly"]
- parameterization ∈ {"CM_in_x", "CM_in_lambda"}
- rel_tol_PASS = 1e-12 (Reading_1 PASS floor)
- rel_tol_FAIL = 1e-9 (Reading_2 FAIL floor; FAIL band [1e-9, ∞))
- INFO band: (1e-12, 1e-9) — between PASS and FAIL, indicates partial structural exclusion

### 4-tuple (M1 / M2 / M3 / M4)
- M1: numerical comparison `rel_diff < 1e-12` (PASS) vs `rel_diff > 1e-9` (FAIL) → COMPUTE-class predicate
- M2: `.py` script (`computations/s88_w10_w8_a1_a4_a2_cascade_investigation.py`) → COMPUTE-class operation
- M3: first-principles Mellin-cone moment computation → not METHODOLOGY-class
- M4: gate-ID NOT in allowlist → COMPUTE-class fallthrough confirmed

**Classification**: COMPUTE-class (M1+M2+M3+M4 all fail METHODOLOGY-class test → COMPUTE-class)

### Substitution chain (sign/direction discipline per `math-scripts.md` §"Double-Check Logic Before Compute")

```
Step 1: Define M^{(A_n)}_R(s) = Σ_k m_k · w_k^{(R)} · λ_k^{-s}    [Mellin-weighted moment, A_n atlas, regulator R]
Step 2: Define rel_diff(A_2, A_4 | param) = max_R |M^{(A_4)}_R(s=3) - M^{(A_2)}_R(s=3)| / |M^{(A_2)}_R(s=3)|
        for R ∈ A_2 (i.e., the 2 regulators present in BOTH atlases)
Step 3: Reading_1 (CONVENTION-ARTIFACT) predicts: rel_diff ~ 0 (machine epsilon)
        because under CM-in-λ parameterization, the substrate's spectral content
        is invariant under regulator-atlas embedding A_2 ⊂ A_4 when both atlases
        share the substrate-distance-1 pole structure.
Step 4: Reading_2 (STRUCTURAL-EXCLUSION) predicts: rel_diff > 1e-9
        because the 2 regulators in A_4 \ A_2 (SDW + anomaly) couple to the
        ζ + Zubarev subspace via off-diagonal Mellin-cone matrix elements
        that violate NCG axiom 5 at s=3.
Step 5: Direction: rel_diff is non-negative by construction (max of absolute values).
        PASS direction = rel_diff small ⇒ Reading_1 confirmed
        FAIL direction = rel_diff large ⇒ Reading_2 confirmed
        INFO direction = rel_diff in transition band ⇒ partial structural exclusion
```

### What PASS/FAIL/INFO MEAN

- **PASS** (rel_diff < 1e-12): A_4 → A_2 cascade is convention-artifact under CM-in-λ; the W-8 §VII.K-PROP cardinality reduction is parameterization-redundancy, not structural exclusion. Re-routes downstream W-8 admissibility analysis to ensemble-level (item #111) without singleton-binding pathology.
- **FAIL** (rel_diff > 1e-9): A_4 → A_2 cascade is genuine structural exclusion; SDW + anomaly regulators violate NCG axiom 5 at s=3. Confirms the W-8 cutoff_sqrt-structural-exclusion theorem at substrate-distance-1.
- **INFO** (1e-12 < rel_diff < 1e-9): Partial structural exclusion; one regulator in A_4 \ A_2 fails axiom 5 but the other does not. Routes to per-regulator NCG-axiom-5 audit (carry-forward to S89).

### Effort
~0.6 wave-equivalents (single-script + cache load + Mellin-moment computation + bit-compare; no new derivation).

### Substrate framing (per `phononic-framing.md` IS-not-IN)
The substrate IS the regulator-weighted spectral moment vector `M^{(A_n)}_R(s=3)`. Atlas A_n is not a "container" of regulators — it is the substrate's specification of which spectral-distance representations are admissible. Cardinality reduction A_4 → A_2 is the substrate's own structural property under axiom-5 violations, not an external selection rule applied to a pre-existing regulator list.

---

## §W10-111 — S88-CF-W8-A2-ENSEMBLE-LEVEL-L2-FULLY-ADMISSIBLE-RE-DERIVATION

**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (substrate-physics, COMPUTE-class)
**Agents**: connes-ncg-theorist (PRIMARY) + lizzi-spectral-functional-theorist (CO)

### Hypothesis
The W-8 §VII.K-PROP A/B/C-trio L2-FULLY-ADMISSIBLE composition theorem holds at the ensemble level across the full atlas A_4 = {ζ, Zubarev, SDW, anomaly} without singleton-binding to Zubarev. The original §VII.K-PROP-W8 derivation (S86 W-8) had Zubarev singleton-bound under CAC (canonical-anchored convention per `regulator-convention-lockdown.md`); the ensemble-level re-derivation lifts the binding while preserving the L2-FULLY-ADMISSIBLE composition law.

**Reading_1 (ENSEMBLE-PRESERVES-COMPOSITION)**: All 4 regulators in A_4 satisfy the L2-admissibility predicate independently; the composition law `L2(R) ∧ L2(R') ⇒ L2(R ⊗ R')` extends to the full atlas. Predicted PASS condition: 4-of-4 regulators yield bit-identical 4-channel layer-2 weights at substrate-distance-2 pole s=4 (rel_diff ≤ 1e-12 across pairs).

**Reading_2 (ZUBAREV-SINGLETON-BINDING)**: Only Zubarev satisfies L2-admissibility at substrate-distance-2; the other 3 regulators (ζ, SDW, anomaly) fail at s=4 due to anomaly-isolating proxy structure. Predicted PASS condition: 1-of-4 regulators (Zubarev) yields bit-identical weight; other 3 deviate at rel_diff > 1e-9.

### Method
1. Load s84_spectrum_cache_L12_tau019.npz.
2. Compute 4-channel layer-2 weights `W^{(R)}_i` for i ∈ {1, 2, 3, 4} channels and R ∈ A_4.
3. Apply ensemble-level admissibility predicate: for each pair (R, R') ∈ A_4 × A_4, verify L2(R) ∧ L2(R') ⇒ L2(R ⊗ R') via bit-comparison of `W^{(R⊗R')}_i` against the convolution `W^{(R)}_i ⊛ W^{(R')}_i`.
4. Tabulate pairwise admissibility verdicts (4 × 4 matrix; diagonal trivially PASS).

### Machinery pin
- L_max = 10 (operational from cache truncation)
- substrate_distance_pole = 4 (s=4, fermionic-signed-residue per §VII.K-PROP.W10-4)
- regulator_atlas = ["zeta", "zubarev", "SDW", "anomaly"]
- channel_count = 4 (i ∈ {1, 2, 3, 4})
- rel_tol_PASS_pair = 1e-12
- rel_tol_FAIL_pair = 1e-9
- composition_law: `W^{(R⊗R')}_i = (W^{(R)}_i ⊛ W^{(R')}_i)` (Mellin convolution)
- ensemble_size = binomial(4, 2) + 4 = 10 pairs (6 off-diagonal + 4 diagonal)

### 4-tuple
- M1: numerical PASS/FAIL on `rel_diff` per pair → COMPUTE-class
- M2: `.py` script (`computations/s88_w10_w8_a2_ensemble_level_l2_admissible.py`) → COMPUTE-class
- M3: re-derivation of W-8 §VII.K-PROP under ensemble-level → first-principles, not verbatim-extract → COMPUTE-class
- M4: not in allowlist → COMPUTE-class

**Classification**: COMPUTE-class

### Substitution chain
```
Step 1: L2(R) := (W^{(R)}_i ⊛ W^{(R)}_i = W^{(R⊗R)}_i for i ∈ {1,2,3,4})    [admissibility predicate]
Step 2: Ensemble-level L2-FULLY-ADMISSIBLE := ∀ (R, R') ∈ A_4 × A_4, L2(R) ∧ L2(R') ⇒ L2(R ⊗ R')
Step 3: Reading_1 predicts ALL 10 pairs PASS the composition law
Step 4: Reading_2 predicts ONLY pairs (Zubarev, Zubarev) PASS; other 9 pairs FAIL
Step 5: Direction: composition law is invariant under regulator-atlas extension
        IFF Reading_1 holds. The original W-8 derivation's Zubarev-singleton-binding
        is then a CAC-pin artifact, not a structural property.
```

### What PASS/FAIL/INFO MEAN

- **PASS** (10/10 pairs PASS): Ensemble-level L2-FULLY-ADMISSIBLE confirmed; W-8 §VII.K-PROP-W8 promotes from singleton-bound (Zubarev) to ensemble-bound (A_4). Re-publishes registry entry with ensemble-level scope.
- **FAIL** (≤ 1/10 pairs PASS): Zubarev-singleton-binding confirmed; W-8 §VII.K-PROP-W8 retains Zubarev-only scope. Anomaly-isolating proxy structure structurally excludes 3 of 4 regulators at s=4.
- **INFO** (2-9 pairs PASS): Partial ensemble admissibility; subset of A_4 satisfies the composition law. Routes to subset-identification audit (carry-forward).

### Effort
~0.8 wave-equivalents (4-regulator pairwise audit + composition-law verification + registry entry update if PASS).

### Substrate framing
The substrate IS the 4-channel layer-2 weight vector `W^{(R)}_i`. The composition law `L2(R) ∧ L2(R') ⇒ L2(R ⊗ R')` is the substrate's own algebraic structure under Mellin convolution; the ensemble-level admissibility predicate is the substrate IS-property, not an externally-imposed selection rule on a regulator-as-container.

---

## §W10-112 — S88-CF-W8-M4-LMAX-14-CACHE-REGEN-W8-4-RE-RUN

**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (substrate-physics, COMPUTE-class)
**Agent**: connes-ncg-theorist (PRIMARY)

### Hypothesis
The S87 W8-4 3a sub-channel threshold FAILed because the L_max=12 cache truncation propagated to the 3a sub-channel via spectral-tail underestimation. Regenerating the cache at L_max=14 and reformulating the 3a threshold as a RATIO (relative to L=12 anchor) produces a regulator-invariant verdict.

**Reading_1 (LMAX-14-CONVERGENCE)**: At L_max=14, the 3a sub-channel ratio `R_{3a}(L=14) / R_{3a}(L=12)` converges to 1 ± 1e-3, indicating L_max=12 truncation was within structural tolerance. PASS condition: |ratio − 1| < 1e-3.

**Reading_2 (TRUNCATION-DOMINATED)**: The L_max=12 truncation systematically biases the 3a sub-channel by > 1%; ratio `R_{3a}(L=14) / R_{3a}(L=12)` deviates from 1 at the 1e-2 level. FAIL condition: |ratio − 1| > 1e-2.

### Method
1. Regenerate `s84_spectrum_cache_L14_tau019.npz` via `dirac_spectrum.py` block-diagonal recursive Casimir-projection (per `math-scripts.md` §"D_K Block-Diagonality Pre-Check"; verify feasibility before dispatch).
2. Compute 3a sub-channel observable at L_max=14 and L_max=12 from the new + existing caches.
3. Form ratio `R_{3a}(L=14) / R_{3a}(L=12)`.
4. Compare against PASS threshold |ratio − 1| < 1e-3 (Reading_1) and FAIL threshold > 1e-2 (Reading_2).

### Machinery pin
- L_max_old = 12 (existing cache anchor)
- L_max_new = 14 (new cache target)
- substrate_distance_pole = 3 (s=3 sub-channel 3a)
- sub_channel = "3a" (W-8 GATE A 3a-sub-channel definition)
- rel_tol_PASS = 1e-3 (truncation-converged band)
- rel_tol_FAIL = 1e-2 (truncation-dominated band)
- INFO band: (1e-3, 1e-2) — partial convergence
- block_diagonal_pre_check: REQUIRED per `math-scripts.md` §"D_K Block-Diagonality Pre-Check" before L_max=14 cache regeneration
- estimated_irrep_construction_time_at_Lmax14: empirically infeasible per W11-3 calibration (irrep (13,0) construction did NOT complete in 10-min timeslot); MITIGATION: Friedrich-Bär saturation theorem applies if 3a sub-channel is bot-K-truncation-saturated at L_max=12

### 4-tuple
- M1: numerical comparison `|ratio − 1|` against thresholds → COMPUTE-class
- M2: `.py` script + cache regeneration → COMPUTE-class
- M3: re-execution of §W8-4 with reformulated threshold → not new derivation, but reformulation requires audit → COMPUTE-class
- M4: not allowlisted → COMPUTE-class

**Classification**: COMPUTE-class

### Substitution chain
```
Step 1: R_{3a}(L) = Σ_k m_k · w^{(3a)}_k(L) · λ_k(L)^{-3}    [3a sub-channel observable, substrate-distance-1]
Step 2: ratio(L=14, L=12) = R_{3a}(L=14) / R_{3a}(L=12)
Step 3: Reading_1 (truncation-converged) ⇒ ratio → 1 as L → ∞ at convergence rate L^{-α}, α ≥ 3
        At L=14 vs L=12, expected deviation ~ (12/14)^3 - 1 ≈ -0.37 (raw)
        BUT the RATIO formulation cancels leading-order truncation if both numerator and denominator
        share the truncation scaling ⇒ effective deviation ~ L^{-(α+1)} (subleading)
Step 4: Direction: |ratio − 1| → 0 as L_max → ∞ under Reading_1; |ratio − 1| stays > 1e-2 under Reading_2.
```

### What PASS/FAIL/INFO MEAN

- **PASS** (|ratio − 1| < 1e-3): L_max=12 truncation was structurally adequate; W8-4 3a sub-channel FAIL at L_max=12 was not truncation-driven. Confirms structural origin of the FAIL; routes to per-channel structural-cause audit.
- **FAIL** (|ratio − 1| > 1e-2): L_max=12 truncation systematically biased 3a sub-channel; W8-4 FAIL at L_max=12 was truncation-driven. Re-routes W8-4 to L_max=14 baseline; FAIL becomes "L_max=14 stability" rather than "3a sub-channel structural failure."
- **INFO** (1e-3 < |ratio − 1| < 1e-2): Partial truncation effect; bounded by structural cause but not negligible. Routes to L_max=16 cache (carry-forward to S89; effort > 1.0 wave-equivalents per Friedrich-Bär feasibility analysis).

### Effort
~1.2 wave-equivalents (cache regeneration is super-polynomial in dim(p,q); see `math-scripts.md` §"D_K Block-Diagonality Pre-Check" calibration corpus W11-3). If Friedrich-Bär saturation applies, downgrade to ~0.5 wave-equivalents (analytic bound replaces L_max=14 spectrum).

### Substrate framing
The substrate IS the 3a sub-channel observable `R_{3a}(L)`. L_max truncation is not a "container size" but the substrate's own representation-theoretic bound on Casimir-projection construction; convergence as L_max → ∞ is a substrate IS-property, not an external limit.

---

## §W10-113 — S88-CF-W8-M5-PRIMARY-LIFT-MELLIN-CONE-LIVE-W8-5

**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (substrate-physics, COMPUTE-class)
**Agent**: connes-ncg-theorist (PRIMARY)

### Hypothesis
S87 W8-5 was executed under SCHEMATIC `_spectral_action_regulators.py` SU(3) Casimir helpers; under live-physical lift (substituting canonical D_K Peter-Weyl spectrum cache for SCHEMATIC SU(3) Casimir), the verdict changes structurally. The LEVEL conflation pathology (per `substrate-first-canonical-sourcing.md` §(iv) "SCHEMATIC vs full physical" level rule) is the structural cause of the W8-5 verdict drift.

**Reading_1 (LEVEL-INVARIANT)**: PRIMARY and SCHEMATIC yield equivalent W8-5 verdicts (SCHEMATIC helpers faithfully approximate canonical Peter-Weyl at substrate-distance scales). PASS condition: PRIMARY verdict matches SCHEMATIC verdict; rel_diff < 1e-6 on the W8-5 observable.

**Reading_2 (LEVEL-DEPENDENT)**: PRIMARY and SCHEMATIC yield divergent verdicts; SCHEMATIC SU(3) Casimir miscaptures the substrate's spectral content at substrate-distance-1. FAIL condition: PRIMARY verdict diverges from SCHEMATIC; rel_diff > 1e-3.

### Method
1. Load canonical D_K Peter-Weyl spectrum cache `s84_spectrum_cache_L12_tau019.npz`.
2. Substitute canonical eigenvalue spectrum + multiplicity vector for `_spectral_action_regulators.py` SCHEMATIC SU(3) Casimir helpers; flag `mellin_cone_live=True` in W8-5 script.
3. Re-execute §W8-5 observable at PRIMARY fidelity.
4. Compare against SCHEMATIC result from S87 W8-5 verdict line.

### Machinery pin
- PRIMARY: canonical D_K Peter-Weyl spectrum from `s84_spectrum_cache_L12_tau019.npz` (operational L_max=10)
- SCHEMATIC: SCHEMATIC SU(3) Casimir helpers from `_spectral_action_regulators.py` (S87 W8-5 baseline)
- mellin_cone_live = True (PRIMARY mode flag)
- substrate_distance_pole = 3 (W8-5 default)
- rel_tol_PASS = 1e-6 (LEVEL-invariant band)
- rel_tol_FAIL = 1e-3 (LEVEL-dependent band)
- verdict_line_convention_suffix: must include `-PRIMARY` (per `substrate-first-canonical-sourcing.md` §(iv) item 2)

### 4-tuple
- M1: numerical PRIMARY vs SCHEMATIC comparison → COMPUTE-class
- M2: `.py` script (PRIMARY substitution) → COMPUTE-class
- M3: re-execution under LEVEL substitution → not new derivation, structural test → COMPUTE-class
- M4: not allowlisted → COMPUTE-class

**Classification**: COMPUTE-class

### Substitution chain
```
Step 1: O^{SCHEMATIC}_{W8-5} = M^{(R)}_{schematic-Casimir}(s=3)    [SCHEMATIC observable]
Step 2: O^{PRIMARY}_{W8-5} = M^{(R)}_{canonical-Peter-Weyl}(s=3)    [PRIMARY canonical observable]
Step 3: rel_diff = |O^{PRIMARY}_{W8-5} - O^{SCHEMATIC}_{W8-5}| / |O^{SCHEMATIC}_{W8-5}|
Step 4: Reading_1 (LEVEL-INVARIANT) ⇒ rel_diff < 1e-6 (SCHEMATIC ≈ canonical at substrate-distance-1)
        Reading_2 (LEVEL-DEPENDENT) ⇒ rel_diff > 1e-3 (SCHEMATIC fails at substrate-distance-1)
Step 5: Direction: rel_diff is non-negative; PASS direction = small ⇒ SCHEMATIC is faithful;
        FAIL direction = large ⇒ live-physical lift is required for W8-5 canonical verdict.
```

### What PASS/FAIL/INFO MEAN

- **PASS** (rel_diff < 1e-6): SCHEMATIC was faithful at W8-5; W8-5 verdict at SCHEMATIC retains canonical scope. SCHEMATIC helper is approved for substrate-distance-1 observables (with SCHEMATIC disclosure per §(iv) item 3).
- **FAIL** (rel_diff > 1e-3): live-physical lift changes W8-5 verdict structurally; the original SCHEMATIC W8-5 verdict is superseded. SCHEMATIC helper is disqualified for substrate-distance-1 W8-class observables; flag for PRIMARY-only re-runs across W8 cluster.
- **INFO** (1e-6 < rel_diff < 1e-3): Partial LEVEL-dependence; SCHEMATIC captures structural form but misses sub-leading content. SCHEMATIC disclosure mandatory; PRIMARY re-run required for canonical citation.

### Effort
~0.7 wave-equivalents (single-script + cache load + Mellin-cone live evaluation + bit-compare against W8-5 verdict).

### Substrate framing
The substrate IS the canonical D_K Peter-Weyl spectrum at L_max=10. SCHEMATIC SU(3) Casimir is a derived approximation (SCHEMATIC), not the substrate's own structure. live-physical lift restores canonical sourcing per `substrate-first-canonical-sourcing.md` §(iv).

---

## §W10-114 — S88-CF-W8-M6-T-F-CELL-W8-6-XOR-COMPLETION

**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (substrate-physics, COMPUTE-class)
**Agent**: connes-ncg-theorist (PRIMARY)

### Hypothesis
The §W8-6 XOR independence test populates 3 of 4 truth-table cells (T,T) + (F,T) + (F,F); the (T,F) cell is empty because no naturally-occurring substrate configuration produces (3a-sub-channel-PASS, regulator-class-FAIL). Constructing an analytic 3a-by-construction candidate (or using L_max=14 cache from #112) populates the (T,F) cell, completing the XOR independence audit.

**Reading_1 (XOR-INDEPENDENT)**: All 4 cells of the truth-table populate; the 3a sub-channel and regulator-class predicates are XOR-independent. PASS condition: (T,F) cell populates with at least one substrate configuration showing 3a-PASS + regulator-class-FAIL.

**Reading_2 (XOR-DEPENDENT)**: The (T,F) cell remains empty by construction; 3a-PASS implies regulator-class-PASS structurally. FAIL condition: no substrate configuration populates (T,F); the empty cell is a structural property.

### Method
1. Construct analytic 3a-by-construction substrate candidate (manually engineered to PASS 3a sub-channel) OR load L_max=14 cache from §W10-112 if PASS verdict landed there.
2. Apply 4-channel layer-2 §VII.K-PROP regulator-class predicate to the candidate.
3. Verify (3a-PASS, regulator-class-FAIL) cell population.
4. Tabulate full 4-cell truth table.

### Machinery pin
- candidate_source ∈ {"analytic_3a_by_construction", "L_max_14_cache_from_W10_112"}
- substrate_distance_pole = 3
- sub_channel_3a_PASS_threshold: as defined in S87 W8-4 verdict
- regulator_class_FAIL_threshold: as defined in S87 W8-6 truth-table predicate
- truth_table_cells = {(T,T), (T,F), (F,T), (F,F)}
- target_cell = (T, F)

### 4-tuple
- M1: cell-population predicate (existence test) → boundary case; COMPUTE-class because the population test is numerical (predicate evaluation on substrate candidate's spectral moments) → COMPUTE-class
- M2: `.py` script + analytic candidate construction → COMPUTE-class
- M3: not new derivation; verbatim-extension of W8-6 truth-table → could be METHODOLOGY-class IF restricted to verbatim — but candidate construction is first-principles → COMPUTE-class
- M4: not allowlisted → COMPUTE-class

**Classification**: COMPUTE-class

### Substitution chain
```
Step 1: 3a_PASS(candidate) = (R_{3a}(candidate) within W8-4 PASS threshold)    [boolean]
Step 2: regulator_class_FAIL(candidate) = (W8-6 regulator-class predicate FAILs on candidate)    [boolean]
Step 3: target_cell_population_test = ∃ candidate s.t. (3a_PASS = True) ∧ (regulator_class_FAIL = True)
Step 4: Reading_1 ⇒ test PASSes (some candidate populates (T,F))
        Reading_2 ⇒ test FAILs (no candidate populates (T,F); structural exclusion)
Step 5: Direction: test is existence-quantified; PASS direction = exists; FAIL direction = none-exists.
```

### What PASS/FAIL/INFO MEAN

- **PASS** (cell populated): XOR-INDEPENDENCE confirmed; 3a sub-channel and regulator-class are independent predicates. W8-6 truth-table is canonical 4-cell structure; structural analysis proceeds at the 4-cell granularity.
- **FAIL** (cell empty after analytic + cache attempts): XOR-DEPENDENCE confirmed; 3a-PASS structurally implies regulator-class-PASS. W8-6 truth-table collapses to 3-cell substrate-physics partition; reformulate independence test.
- **INFO** (cell partially populated; only 1 candidate found): Cell populates but with single-existence-only; does not confirm robustness. Routes to additional candidate search (carry-forward).

### Effort
~0.5 wave-equivalents (analytic candidate construction + cell-population test). Reduced to ~0.3 if §W10-112 L_max=14 cache PASSes (re-uses existing data).

### Substrate framing
The substrate IS the 4-cell truth-table populated by candidate spectra. Each cell is a substrate-class equivalence; cell-population is a substrate IS-property, not a container-of-classes selection.

---

## §W10-115 — S88-CF-W8-R3-PLAN-ANCHOR-FILENAME-EXISTENCE-AUDIT-EXTENSION

**Trigger**: [AUDIT]
**Classification**: METHODOLOGY (audit-script extension; allowlisted)
**Agent**: gen-physicist (audit-script extension)

### Hypothesis
The S87 W4-2 stale-rectangle relabel calibration corpus (`epistemic-discipline.md` §"Source Reconciliation" Class-(c) PIN-DRIFT-FROM-STALE-SOURCE) demonstrated that plan-document INPUT-PIN MAP citations to filenames + section anchors must be verified for filename-existence at plan-freeze. The current `_source_reconciliation_audit.py` checks pin-vs-canonical drift but does NOT verify that cited filenames exist on disk. Extension: add filename-existence grep to the audit pipeline.

**PASS predicate (METHODOLOGY-class M1)**: artifact-existence-with-substantive-content per `wave-classification.md` §M1:
```
PASS iff (file `computations/_shared/_source_reconciliation_audit.py` exists)
        AND (contains new method `verify_cited_filename_existence(plan_doc_path)`)
        AND (substantive_line_count(method) >= 15)
        AND (content_sha256 matches input-pin-map-derived hash)
```

### Method
1. Edit `computations/_shared/_source_reconciliation_audit.py` to add `verify_cited_filename_existence(plan_doc_path)` method.
2. Method greps plan-document INPUT-PIN MAP entries for `filename:section-anchor` patterns; for each, verifies (a) file exists on disk, (b) section anchor (if present) matches a header in the file.
3. Emit per-pin verdict to audit JSON output.
4. Run on S88 W10 plan as self-test; verify all 11 items' INPUT-PIN MAP entries pass filename-existence audit.

### Machinery pin
- target_file: `computations/_shared/_source_reconciliation_audit.py`
- new_method_signature: `verify_cited_filename_existence(plan_doc_path: str) -> dict[str, AuditVerdict]`
- pattern_set:
  - `plan-document-INPUT-PIN-MAP entry shape: <name> = <value> | source: <filename>(:<section-anchor>)?`
  - filename-existence test: `os.path.exists(<filename>)`
  - section-anchor test: `re.search(r'^#+ .*' + re.escape(anchor), open(filename).read(), flags=re.MULTILINE)`
- self_test_target: S88 W10 plan (this document); 11 items × ~3 INPUT-PIN MAP entries ≈ 33 filename + anchor checks
- substantive_line_count_threshold: ≥ 15 (per `wave-classification.md` §M1)

### 4-tuple
- M1: artifact-existence + section + line-count → METHODOLOGY-class predicate ✓
- M2: Edit on `computations/_shared/_source_reconciliation_audit.py` (allowed under METHODOLOGY-class M2 because computations/ extensions to `_*_audit.py` files are allowlisted as audit-script extensions per `methodology-wave-allowlist.md` §"Allowlist Rows" pattern) → METHODOLOGY-class operation ✓
- M3: verbatim-extract from `epistemic-discipline.md` §"Source Reconciliation" Class-(c) calibration corpus (W4-2 stale-rectangle precedent) → not new derivation ✓
- M4: gate-ID NOT yet in allowlist; orchestrator must append at plan-freeze before METHODOLOGY-class classification holds. **PLAN-FREEZE PREREQUISITE: orchestrator append S88-CF-W8-R3-PLAN-ANCHOR-FILENAME-EXISTENCE-AUDIT-EXTENSION to `methodology-wave-allowlist.md` rows table BEFORE dispatch.**

**Classification**: METHODOLOGY-class (CONDITIONAL ON M4 satisfaction at plan-freeze; if M4 not satisfied, fallthrough to COMPUTE-class with `.py` edit predicate, which fails M1 — routes to plan-freeze halt requesting allowlist append).

### What PASS/FAIL MEAN

- **PASS**: Audit-script extension landed; `verify_cited_filename_existence` callable from `/weave --update` Phase 6; future plan documents pass filename-existence audit at plan-freeze.
- **FAIL**: Edit not landed OR substantive_line_count < 15 OR self-test fails on S88 W10 plan. Re-dispatch via Stage-1 recovery per `v3-closure-recovery.md`.

### Effort
~0.4 wave-equivalents (single Edit + method addition + self-test + verdict-line emission with dual-SHA over the diff).

### Substrate framing (cross-link discipline)
This item operates at the audit-script layer (METHODOLOGY image of substrate-physics filename-existence under layer-functor F per `epistemic-discipline.md` §"Layer-Decomposition"). The substrate-physics analog is "verify pin-source canonical exists at substrate-spectral location"; the audit-layer extension is "verify cited-filename exists at filesystem location". F preserves the existence-predicate.

---

## §W10-116 — S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION

**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (substrate-physics, COMPUTE-class)
**Agent**: connes-ncg-theorist (PRIMARY)

### Hypothesis
The S87 Bulletin #3 PASS-B residual `c_sub^{corrected, central} = 3.5169` carries registry-flag grade `r/Γ(3) = 11/14 = 0.7857`. The W-10 R3-B EMERGENCE E1 spectral-moment-realization claim asserts this residual is a Γ-ladder coincidence (`Γ(11/4) ≈ 11/7` at 2.35%, NOT a substrate-spectral identity). SOURCE-RECONCILIATION class-(c) PIN-DRIFT audit tests whether the Bulletin #3 anchor citation drifted from the original PASS-A canonical (pre-W-10 R3-B EMERGENCE E1) to a stale post-W-10 R3-B reading.

**Reading_1 (PIN-DRIFT-CONFIRMED)**: Bulletin #3 anchor cites the W-10 R3-B EMERGENCE E1 spectral-moment-realization claim, but that claim was demoted from "substrate-spectral identity" to "Γ-ladder coincidence" at S87 W-10 R3-B closeout. The pin is structurally testing the wrong hypothesis (substrate-spectral identity) when the canonical view (Γ-ladder coincidence) post-supersedes. PASS condition: SOURCE-RECON class-(c) audit emits PIN-DRIFT advisory + remediation recommends re-pinning to Γ-ladder-coincidence canonical.

**Reading_2 (NO-DRIFT)**: Bulletin #3 anchor was always pinned to Γ-ladder-coincidence canonical; no PIN-DRIFT detected. INFO condition: SOURCE-RECON class-(c) audit emits NO-DRIFT verdict.

### Method
1. Query `mcp__knowledge__.get_constant("c_sub_corrected_central")` for canonical value + provenance.
2. Compare canonical provenance against Bulletin #3 anchor citation in `sessions/framework/registry/elimination-bulletins.md`.
3. Compute `D_max = |log10(pin) - log10(source)|` per `epistemic-discipline.md` §"Source Reconciliation" 4-band calibration.
4. Classify per the 5-class taxonomy: (a)/(b)/(c)/(d)/(e)/(f).
5. Emit verdict.

### Machinery pin
- canonical_constants_query_target: `c_sub_corrected_central`
- bulletin_3_anchor_path: `sessions/framework/registry/elimination-bulletins.md`
- W_10_R3B_E1_claim_path: `sessions/archive/session-87/workshops/s87-bulletin-3-4-corridor.md` (or W10-3 working paper §)
- D_max_band_PASS: 0.1 ≤ D_max < 1.0 (advisory S2)
- D_max_band_FAIL: D_max ≥ 3.0 (HARD-HALT)
- D_max_band_INFO: D_max < 0.1 (NO-DRIFT, S82-class-(d) absorbable)
- substrate_distance_pole = 3 (Bulletin #3 substrate-distance-1)
- expected_class_under_Reading_1: (c) PIN-DRIFT-FROM-STALE-SOURCE
- expected_class_under_Reading_2: NO-CLASS (no drift detected)

### 4-tuple
- M1: SOURCE-RECON class-(c) verdict against pre-registered class taxonomy → COMPUTE-class predicate
- M2: `.py` script invoking knowledge MCP + grep + log-diff computation → COMPUTE-class
- M3: not new derivation; verbatim-application of `epistemic-discipline.md` §"Source Reconciliation" → could be METHODOLOGY-class if restricted to audit-execution-only — but the verdict-classification step is numerical → COMPUTE-class
- M4: not allowlisted → COMPUTE-class

**Classification**: COMPUTE-class

### Substitution chain
```
Step 1: pin_value = bulletin_3_anchor_value (extracted from elimination-bulletins.md)
Step 2: source_value = mcp__knowledge__.get_constant("c_sub_corrected_central").value
Step 3: D_max = |log10(pin_value) - log10(source_value)|
Step 4: Classify per 5-class taxonomy:
        - If pin_value cites pre-W-10 R3-B canonical AND source_value is post-W-10 R3-B canonical:
          ⇒ class (c) PIN-DRIFT-FROM-STALE-SOURCE
        - Else: NO-CLASS
Step 5: Direction: D_max is non-negative; classification depends on provenance comparison, not magnitude alone.
        PASS direction = drift detected ⇒ remediation triggered
        INFO direction = no drift ⇒ Bulletin #3 anchor is already canonical
        FAIL direction = HARD-HALT band ⇒ manual review required
```

### What PASS/FAIL/INFO MEAN

- **PASS** (class (c) drift detected, 0.1 ≤ D_max < 1.0): PIN-DRIFT advisory; remediation = re-pin Bulletin #3 anchor to Γ-ladder-coincidence canonical. Routes to #117 Lizzi-observable promotion re-emit.
- **INFO** (NO-DRIFT, D_max < 0.1): Bulletin #3 anchor is already canonical; no remediation needed. Routes to #117 with NO-DRIFT context.
- **FAIL** (D_max ≥ 3.0): HARD-HALT; Bulletin #3 anchor has structurally invalid provenance. Manual review required; #117 BLOCKED.

### Effort
~0.3 wave-equivalents (audit-script invocation + provenance comparison + verdict emission).

### Substrate framing
The substrate IS the `c_sub_corrected_central` spectral-moment value at substrate-distance-1 pole. Bulletin #3 anchor citation is the methodology image (per layer-functor F) of the substrate's IS-property; PIN-DRIFT detection at the methodology layer reflects substrate-canonical-revision events at the substrate layer.

---

## §W10-117 — S88-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION-RE-EMIT

**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (substrate-physics, COMPUTE-class)
**Agents**: connes-ncg-theorist (PRIMARY) + lizzi-spectral-functional-theorist (CO; observable-promotion authority)
**Conditional**: REQUIRES #116 verdict ∈ {PASS, INFO}; BLOCKED if #116 FAIL

### Hypothesis
Conditional on §W10-116 PIN-DRIFT remediation (or NO-DRIFT confirmation), re-emit §W10-3 Bulletin #3 with full lizzi-spectral-functional-theorist observable-promotion authority. The lizzi promotion authority dispatches observable-promotion verdicts per the FI/RD/MIXED taxonomy at registry §VII.K (per S82 W-3 lizzi+connes regulator-dressing taxonomy workshop).

**PASS condition**: Bulletin #3 re-emitted at registry §VII.K-PROP.W10-3 with explicit lizzi-promotion authority signature; observable-class promoted to FI (Free-Invariant) or RD (Regulator-Dressed) per the taxonomy; both connes-ncg + lizzi co-sign verdict line.

**FAIL condition**: Bulletin #3 re-emit fails (registry-write race per `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race"); routes to one-shot Python-writer remediation.

### Method
1. Read #116 verdict from `computations/session-88/s88_gate_verdicts.txt`.
2. If #116 PASS (PIN-DRIFT detected): substitute Γ-ladder-coincidence canonical for the Bulletin #3 anchor; if #116 INFO (NO-DRIFT): retain existing canonical.
3. Dispatch lizzi-spectral-functional-theorist with observable-promotion authority (FI/RD/MIXED classification) on the Bulletin #3 c_sub_corrected_central residual.
4. Re-emit §W10-3 working-paper section with full lizzi promotion taxonomy + connes-ncg co-sign.
5. Append registry entry at §VII.K-PROP.W10-3 via append-only Python writer (per `epistemic-discipline.md` §"Registry-Write Hygiene" item 2).

### Machinery pin
- prereq_verdict_source: `computations/session-88/s88_gate_verdicts.txt` § S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION
- conditional_dispatch: PASS/INFO from #116 ⇒ proceed; FAIL ⇒ block + emit upstream-FAIL verdict
- lizzi_promotion_taxonomy: {"FI": "Free-Invariant", "RD": "Regulator-Dressed", "MIXED": "FI/RD-mixed"}
- registry_target: `sessions/permanent-results-registry.md` §VII.K-PROP.W10-3
- writer_protocol: append-only Python writer (per `epistemic-discipline.md` §"Registry-Write Hygiene" item 2)
- co_sign_required: connes-ncg-theorist + lizzi-spectral-functional-theorist
- substrate_distance_pole = 3

### 4-tuple
- M1: numerical re-emit verification (canonical match between re-emitted residual and remediated source) → COMPUTE-class
- M2: `.py` script + lizzi dispatch + registry append → COMPUTE-class
- M3: not new derivation; lizzi authority-promotion is verbatim FI/RD taxonomy application → COMPUTE-class with structural-claim verification
- M4: not allowlisted → COMPUTE-class

**Classification**: COMPUTE-class

### Substitution chain
```
Step 1: c_sub_residual = c_sub_corrected_central - 3.5169    [pre-existing PASS-B residual]
Step 2: Lizzi-taxonomy({c_sub_residual}) → {FI, RD, MIXED}    [lizzi-authority classification]
Step 3: Re-emit §W10-3 with classification + connes-ncg + lizzi co-sign
Step 4: Direction: classification is structural; the residual itself is a fixed value.
        Re-emit success = registry append + dual-SHA closure verdict line.
        Re-emit failure = registry-write race or co-sign mismatch.
```

### What PASS/FAIL MEAN

- **PASS**: Bulletin #3 re-emitted at §VII.K-PROP.W10-3 with full lizzi promotion authority + connes-ncg co-sign; classification documented (FI/RD/MIXED).
- **FAIL**: Re-emit failed (race or co-sign mismatch); routes to remediation per `v3-closure-recovery.md` Stage-1.

### Effort
~0.5 wave-equivalents (conditional dispatch + lizzi taxonomy classification + registry append + dual-SHA closure).

### Substrate framing
The substrate IS the `c_sub_corrected_central` spectral residual. FI/RD/MIXED classification is the lizzi-authority structural reading of the substrate's IS-property (regulator-invariance vs regulator-dressing). The classification is not an external label imposed on the residual but a substrate IS-property revealed by the FI/RD taxonomy.

---

## §W10-118 — S88-CF-C-SOURCE-RECONCILIATION-PLAN-FREEZE-CLASS-B-EXTENSION

**Trigger**: [AUDIT]
**Classification**: METHODOLOGY (audit-script extension; allowlisted)
**Agent**: gen-physicist (audit-script extension)

### Hypothesis
The S87 W10-2 inconsistency pattern surfaced a structural drift type not yet covered by the `_source_reconciliation_audit.py` 5-class taxonomy: literal numerical pin tighter than structural-form-with-unpinned-coefficient. Specifically: a pin value `r/Γ(3) = 11/14 = 0.7857` is a literal numerical pin; the structural-form-with-unpinned-coefficient is `Γ(11/4)·k`-class with `k` unpinned across regulator-classes. The pin is structurally TIGHTER than the canonical (which spans the full `k`-band), making it a class-(b) PIN-LOOSE-SOURCE-TIGHT FALSE-PASS direction at the methodology level.

**PASS predicate (METHODOLOGY-class M1)**: artifact-existence-with-substantive-content per `wave-classification.md` §M1:
```
PASS iff (file `computations/_shared/_source_reconciliation_audit.py` exists)
        AND (contains class-(b) extension recognizing literal-vs-structural-form pattern)
        AND (substantive_line_count(extension) >= 15)
        AND (content_sha256 matches input-pin-map-derived hash)
```

### Method
1. Edit `computations/_shared/_source_reconciliation_audit.py` to extend class-(b) detection.
2. Add pattern-set: literal numerical pin (e.g., `r/Γ(3) = 11/14`) tighter than structural-form-with-unpinned-coefficient (e.g., `Γ(11/4)·k` with `k` unpinned).
3. Add severity ladder: literal-vs-structural mismatch at narrowing factor > 10× → S1 MANDATORY.
4. Self-test on S87 W10-2 verdict trace; verify class-(b) FALSE-PASS direction caught at plan-freeze.

### Machinery pin
- target_file: `computations/_shared/_source_reconciliation_audit.py`
- new_class_pattern:
  - literal_pin_pattern: `<numerical_value> = <fraction_or_decimal>` (no `coefficient k` or unpinned-form qualifier)
  - structural_form_pattern: `<symbolic_expression>·<coefficient_name>` where coefficient is regulator-class-spanning
  - narrowing_factor_threshold: 10× (S1 MANDATORY)
- self_test_target: S87 W10-2 verdict trace `r/Γ(3) = 11/14`
- substantive_line_count_threshold: ≥ 15

### 4-tuple
- M1: artifact-existence + line-count + content-match → METHODOLOGY-class predicate ✓
- M2: Edit on `_source_reconciliation_audit.py` (allowed under METHODOLOGY-class M2) → METHODOLOGY-class operation ✓
- M3: verbatim-extract from `epistemic-discipline.md` §"Source Reconciliation" class-(b) PIN-LOOSE-SOURCE-TIGHT pattern → not new derivation ✓
- M4: gate-ID NOT yet in allowlist. **PLAN-FREEZE PREREQUISITE: orchestrator append S88-CF-C-SOURCE-RECONCILIATION-PLAN-FREEZE-CLASS-B-EXTENSION to `methodology-wave-allowlist.md` BEFORE dispatch.**

**Classification**: METHODOLOGY-class (CONDITIONAL ON M4 satisfaction at plan-freeze)

### What PASS/FAIL MEAN

- **PASS**: Audit-script class-(b) extension landed; future plans testing literal-vs-structural-form patterns trigger S1 MANDATORY at plan-freeze.
- **FAIL**: Edit not landed OR self-test fails OR substantive_line_count < 15. Re-dispatch via Stage-1 recovery.

### Effort
~0.4 wave-equivalents (single Edit + class extension + self-test + verdict-line emission).

### Substrate framing (cross-link discipline)
At the methodology layer, the audit-script class-(b) extension is the F-image (per layer-functor) of substrate-level pin-vs-canonical drift detection. The substrate IS the spectral observable; the methodology IS the audit-line content that detects pin-drift on that observable.

---

## §W10-119 — S88-BULLETIN-PER-POLE-PRIMARY-WALL-CLASSIFICATION-RULE-PIN

**Trigger**: [VERIFY]
**Classification**: METHODOLOGY (rule-file pin; allowlisted)
**Agent**: mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`)

### Hypothesis
Future Mellin-cone Bulletin landings at distinct substrate-distance poles (s ∈ {3, 4, 5, ...}) require per-Bulletin-per-pole Level-1 wall classification convention. The current `cross-pillar-bridge-anatomy.md` Level-1/2/3 ladder applies to cross-pillar bridges; this rule extends it to Bulletin-class registry entries within a single pillar (Pillar-VII Mellin-cone), where the Level-1/2/3 distinction operates over substrate-distance pole indices rather than pillar pairs.

**PASS predicate (METHODOLOGY-class M1)**: artifact-existence-with-substantive-content per `wave-classification.md` §M1:
```
PASS iff (file `.claude/rules/cross-pillar-bridge-anatomy.md` exists)
        AND (contains new sub-section on per-Bulletin-per-pole Level-1 wall classification)
        AND (substantive_line_count(sub-section) >= 15)
        AND (content_sha256 matches input-pin-map-derived hash)
```

### Method
1. Edit `.claude/rules/cross-pillar-bridge-anatomy.md` to add sub-section on per-Bulletin-per-pole Level-1 wall classification.
2. Specify mapping:
   - Level-1 (cohomology-class identity, regulator-invariant) ↔ per-pole substrate-distance-IS spectral identity
   - Level-2 (algebraic envelope, L_max-dependent) ↔ per-pole L_max-truncation envelope
   - Level-3 (empirical anchor at canonical L_max) ↔ per-pole numerical anchor at L_max=10
3. Cite §VII.K-PROP.W10-4 ρ_∞ permanent-wall (s=4) and §VII.U.1 Mellin-Dirichlet identity (s=3) as calibration corpus instances.
4. Mack writes per sole-writer protocol; connes-ncg-theorist co-signs the technical content.

### Machinery pin
- target_file: `.claude/rules/cross-pillar-bridge-anatomy.md`
- new_subsection_target: §"Per-Bulletin-per-pole Level-1 wall classification"
- calibration_corpus:
  - §VII.K-PROP.W10-4 ρ_∞ = -0.8103647022669215 (s=4 substrate-distance-2 fermionic-signed-residue permanent-wall)
  - §VII.U.1 Mellin-Dirichlet identity (s=3 substrate-distance-1 apex-universal anchor)
- writer: mack-cosmic-bridge (sole)
- co_sign: connes-ncg-theorist (technical content)
- substantive_line_count_threshold: ≥ 15

### 4-tuple
- M1: artifact-existence + sub-section + line-count → METHODOLOGY-class predicate ✓
- M2: Edit on `.claude/rules/cross-pillar-bridge-anatomy.md` → METHODOLOGY-class operation ✓
- M3: verbatim-extract from §VII.K-PROP.W10-4 permanent-wall + §VII.U.1 Mellin-Dirichlet identity calibration corpus → not new derivation ✓
- M4: gate-ID NOT yet in allowlist. **PLAN-FREEZE PREREQUISITE: orchestrator append S88-BULLETIN-PER-POLE-PRIMARY-WALL-CLASSIFICATION-RULE-PIN to `methodology-wave-allowlist.md` BEFORE dispatch.**

**Classification**: METHODOLOGY-class (CONDITIONAL ON M4 satisfaction at plan-freeze)

### What PASS/FAIL MEAN

- **PASS**: Rule-file pin landed at `cross-pillar-bridge-anatomy.md`; future Bulletin landings at distinct substrate-distance poles inherit Level-1/2/3 classification automatically.
- **FAIL**: Edit not landed OR substantive_line_count < 15 OR mack/connes co-sign mismatch. Re-dispatch via Stage-1 recovery.

### Effort
~0.4 wave-equivalents (single Edit + sub-section authoring + co-sign + verdict-line emission).

### Substrate framing
The substrate IS the Mellin-cone pole structure at substrate-distance values s ∈ {3, 4, 5, ...}. Each pole is a substrate IS-location (not a "container at distance s"). Per-pole Level-1 wall classification is the methodology image of the substrate's per-pole structural identity.

---

## §W10-120 — S88-CF-VERDICT-2-CONDITIONAL-CROSS-DISTANCE-THEOREM-DISPATCH

**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (DORMANT shell; conditional on future Bulletin landing at different substrate-distance pole)
**Agent**: connes-ncg-theorist (PRIMARY)

### Hypothesis
DORMANT. This is a conditional dispatch shell that activates ONLY when a future Bulletin lands at a substrate-distance pole different from those currently registered (s=3 §VII.U.1; s=4 §VII.K-PROP.W10-4). At activation, the shell dispatches a cross-distance theorem candidate testing whether the per-pole Level-1 wall classification (per §W10-119 rule-pin) extends to a cross-pole identity (e.g., a relation between s=3 and s=4 substrate-distance moments).

**Activation trigger**: Future Bulletin landing at s ∈ {5, 6, 7, ...} with registered §VII.K-PROP.W10-N entry, where N corresponds to the new pole index.

**Until activation**: Item carries DORMANT verdict; no compute fires; verdict-line emits `INFO -- value='DORMANT_pending_future_substrate_distance_pole_landing'` with audit_sha256 over the dormant-shell metadata.

### Method (at activation)
1. Detect new Bulletin landing at substrate-distance s_new via knowledge-MCP query `search_knowledge("Bulletin substrate-distance s=" + str(s_new))`.
2. Extract the new pole's Level-1 wall (regulator-invariant residue value).
3. Test cross-pole identity candidates:
   - Linear: `R(s_old) + R(s_new) = constant`
   - Multiplicative: `R(s_old) · R(s_new) = constant`
   - Γ-ladder: `R(s_old) / R(s_new) = Γ(α)/Γ(β)` for symbolic α, β
4. Verify any PASSing identity at machine-epsilon (rel_diff < 1e-12).

### Machinery pin (at activation; pre-pinned dormant)
- activation_trigger: `mcp__knowledge__.search_knowledge("Bulletin substrate-distance s=" + str(s_new)).top_hit.exists`
- candidate_identities: ["linear_sum", "multiplicative_product", "gamma_ladder_ratio"]
- rel_tol_PASS = 1e-12
- rel_tol_FAIL = 1e-9
- INFO band: (1e-12, 1e-9)
- dormant_verdict_line: `INFO -- value='DORMANT_pending_future_substrate_distance_pole_landing'`
- dormant_audit_sha256: computed over dormant-shell metadata at plan-freeze

### 4-tuple
- M1: At activation: numerical PASS/FAIL on cross-pole identity → COMPUTE-class
        Until activation: artifact-existence of dormant-shell verdict-line → could be METHODOLOGY-class
- M2: At activation: `.py` script + identity testing → COMPUTE-class
        Until activation: dormant-shell verdict-line emission → minimal scripting
- M3: At activation: first-principles cross-pole identity testing → COMPUTE-class
- M4: not allowlisted → COMPUTE-class

**Classification**: COMPUTE-class (DORMANT until activation; verdict-line emission at plan-freeze marks shell as pre-allocated).

### What PASS/FAIL/INFO MEAN (at activation)

- **PASS** (cross-pole identity holds at machine-epsilon): cross-distance theorem candidate confirmed; promote to §VII.K-PROP cross-pole entry.
- **FAIL** (no candidate identity holds at rel_tol > 1e-9): cross-pole structure is independent (no algebraic identity bridges the two poles).
- **INFO** (1e-12 < rel_diff < 1e-9): partial identity; routes to higher-precision audit (carry-forward).

### Until activation
- **DORMANT-INFO**: shell pre-allocated; no compute; verdict-line emits dormant marker with audit_sha256 over metadata.

### Effort
~0.1 wave-equivalents (dormant-shell verdict-line emission only; full compute deferred to activation event, ~0.6 wave-equivalents at that time).

### Substrate framing
The substrate IS the multi-pole Mellin-cone structure {R(s=3), R(s=4), R(s=5), ...}. Cross-pole identities (linear, multiplicative, Γ-ladder) are substrate IS-properties of the multi-pole spectral content, not externally-imposed relations between distinct "containers at different distances". The dormant shell pre-registers the test for future activation when the multi-pole structure populates beyond s=4.

---

## Wave 10 → Wave 11 Decision Point

| Item | Status at decision-point | Action if PASS | Action if FAIL | Action if INFO |
|:-----|:------------------------|:---------------|:---------------|:---------------|
| #110 | A_4→A_2 cascade verdict | Promote to ensemble-level (#111) | Confirm structural exclusion; route to per-regulator NCG-axiom-5 audit (S89) | Per-regulator NCG-axiom-5 audit (S89 carry-forward) |
| #111 | Ensemble L2-FULLY-ADMISSIBLE | Update §VII.K-PROP-W8 to ensemble-bound | Retain Zubarev-singleton scope | Subset-identification audit (S89) |
| #112 | L_max=14 cache + W8-4 re-run | Confirm structural origin of W8-4 FAIL; per-channel audit | L_max=14 baseline replaces L_max=12 for W8 cluster | L_max=16 cache (S89) |
| #113 | live-physical lift on W8-5 | SCHEMATIC approved with disclosure | PRIMARY-only re-runs across W8 cluster | PRIMARY re-run for canonical citation |
| #114 | (T,F) cell population | XOR-INDEPENDENCE confirmed | XOR-DEPENDENCE; reformulate truth-table | Additional candidate search (S89) |
| #115 | Audit-script extension | Self-test on S88 W10 plan PASSes | Re-dispatch Stage-1 | N/A (METHODOLOGY-class binary) |
| #116 | SOURCE-RECON class-(c) audit | Trigger #117 (PIN-DRIFT remediated) | BLOCK #117 (HARD-HALT) | Trigger #117 (NO-DRIFT context) |
| #117 | Bulletin #3 re-emit | §VII.K-PROP.W10-3 landed with lizzi authority | Re-dispatch Stage-1 | N/A (binary closure) |
| #118 | Class-(b) extension | Future plans test literal-vs-structural at plan-freeze | Re-dispatch Stage-1 | N/A |
| #119 | Per-pole Level-1 rule pin | Future Bulletins inherit Level-1/2/3 classification | Re-dispatch Stage-1 | N/A |
| #120 | DORMANT shell | DORMANT-INFO emitted; activation deferred | N/A | Activation pending future Bulletin |

**Wave 10 closure criterion**: All 11 items emit verdict lines (any of {PASS, FAIL, INFO, DORMANT-INFO}) with dual-SHA companion rows in `computations/session-88/s88_gate_verdicts.txt`. Working-paper sections at `sessions/archive/session-88/session-88-w10-workingpaper.md` populate per the artifact-existence checklist (§"ARTIFACT CHECKLIST" in spawn prompts).

**Decision-point routing to Wave 11**:
- If #110 PASS + #111 PASS: Wave 11 promotes ensemble-level §VII.K-PROP-W8 to permanent-results-registry §VII.K-PROP-W8-ENSEMBLE.
- If #112 FAIL: Wave 11 leads with L_max=14 cache regen as upstream prerequisite for the cluster.
- If #113 FAIL: Wave 11 dispatches PRIMARY-only W8 cluster re-run.
- If #116 FAIL (HARD-HALT): Wave 11 leads with manual review of Bulletin #3 anchor; #117 blocked.
- If #115 + #118 + #119 all PASS: Wave 11 inherits 3 new audit-script + rule-file extensions for plan-freeze use.
- #120 DORMANT carries forward to S89+ unchanged (activation pending future Bulletin landing).

---

## Wave 10 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md` §"Pre-Registration Completeness — PRDR" requirements, the wave's machinery pin enumerates every gate-relevant parameter for each item.

| Item | Parameters pinned |
|:-----|:------------------|
| #110 | M_KK (canonical), tau_fold=0.190, L_max=10, substrate_distance_pole=3, regulator_atlas_A_2, regulator_atlas_A_4, parameterization, rel_tol_PASS=1e-12, rel_tol_FAIL=1e-9 |
| #111 | L_max=10, substrate_distance_pole=4, regulator_atlas=A_4, channel_count=4, rel_tol_PASS_pair=1e-12, rel_tol_FAIL_pair=1e-9, ensemble_size=10 |
| #112 | L_max_old=12, L_max_new=14, substrate_distance_pole=3, sub_channel="3a", rel_tol_PASS=1e-3, rel_tol_FAIL=1e-2, block_diagonal_pre_check=REQUIRED |
| #113 | PRIMARY cache path, helper module, mellin_cone_live=True, substrate_distance_pole=3, rel_tol_PASS=1e-6, rel_tol_FAIL=1e-3, verdict_line_convention_suffix="-PRIMARY" |
| #114 | candidate_source ∈ {analytic, L_max=14}, substrate_distance_pole=3, sub_channel_3a_PASS_threshold (W8-4 trace), regulator_class_FAIL_threshold (W8-6 trace), target_cell=(T,F) |
| #115 | target_file path, new_method_signature, pattern_set, self_test_target=S88_W10_plan, substantive_line_count_threshold=15 |
| #116 | canonical_constants_query_target, bulletin_3_anchor_path, W_10_R3B_E1_claim_path, D_max_band_PASS, D_max_band_FAIL, substrate_distance_pole=3 |
| #117 | prereq_verdict_source, conditional_dispatch_rule, lizzi_promotion_taxonomy, registry_target=§VII.K-PROP.W10-3, writer_protocol=append-only, co_sign_required, substrate_distance_pole=3 |
| #118 | target_file path, new_class_pattern (literal_pin + structural_form + narrowing_factor_threshold=10×), self_test_target=S87_W10-2_trace, substantive_line_count_threshold=15 |
| #119 | target_file=`cross-pillar-bridge-anatomy.md`, new_subsection_target, calibration_corpus (§VII.K-PROP.W10-4 + §VII.U.1), writer=mack, co_sign=connes-ncg, substantive_line_count_threshold=15 |
| #120 | activation_trigger (knowledge-MCP query), candidate_identities, rel_tol_PASS=1e-12, rel_tol_FAIL=1e-9, dormant_verdict_line, dormant_audit_sha256 |

PRDR cardinality cleared at plan-freeze: every item's machinery pin enumerates all gate-relevant parameters (no `<pinned at dispatch>` placeholders without enumeration).

---

## Wave 10 Input-SHA Ledger

Per `cross-pillar-bridge-anatomy.md` §"Audit at plan-freeze" and `epistemic-discipline.md` §"Source Reconciliation" requirements:

| Source file | Role | Input-SHA at plan-freeze |
|:------------|:-----|:------------------------|
| `sessions/permanent-results-registry.md` §VII.K-PROP-W8 | Anchor for #111 | `<pinned at dispatch>` |
| `sessions/permanent-results-registry.md` §VII.K-PROP.W10-4 | Anchor for #119 + #120 | `<pinned at dispatch>` |
| `sessions/permanent-results-registry.md` §VII.U.1 | Anchor for #119 + #120 | `<pinned at dispatch>` |
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | Cache for #110, #111, #112, #113, #114 | `<pinned at dispatch>` |
| `computations/_shared/_spectral_action_regulators.py` | SCHEMATIC baseline for #113 | `<pinned at dispatch>` |
| `computations/_shared/_source_reconciliation_audit.py` | Edit target for #115 + #118 | `<pinned at dispatch>` |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | Edit target for #119 | `<pinned at dispatch>` |
| `.claude/rules/methodology-wave-allowlist.md` | Append target for #115, #118, #119 (orchestrator-only edit) | `<pinned at dispatch>` |
| `sessions/framework/registry/elimination-bulletins.md` | Anchor for #116 + #117 | `<pinned at dispatch>` |
| `computations/_shared/canonical_constants.py` | Pin source for M_KK, tau_fold, c_sub_corrected_central | `<pinned at dispatch>` |
| `sessions/archive/session-87/workshops/s87-bulletin-3-4-corridor.md` (or W10-3 working paper) | Anchor for #116 W-10 R3-B EMERGENCE E1 claim | `<pinned at dispatch>` |
| `computations/session-87/s87_gate_verdicts.txt` | Verdict trace for W10-1, W10-2, W8-4, W8-5, W8-6 prerequisites | `<pinned at dispatch>` |

`<pinned at dispatch>` indicates runtime-SHA capture per the canonical input-pin protocol. Per AMRI Test 1 (`agent-standards.md` §"Agent-Memory Registry Inversion"), no agent-memory files are listed as input-pin sources — all sources are project-level registries or canonical artifacts.

---

## Plan-freeze prerequisites (orchestrator action items)

Before dispatch:

1. **Methodology-wave allowlist appends** (per `wave-classification.md` §M4 + `methodology-wave-allowlist.md` §"Edit discipline" item 2):
   - Append `S88-CF-W8-R3-PLAN-ANCHOR-FILENAME-EXISTENCE-AUDIT-EXTENSION` (item #115) to `.claude/rules/methodology-wave-allowlist.md` Allowlist Rows table with computed `sha256_of_plan_block`.
   - Append `S88-CF-C-SOURCE-RECONCILIATION-PLAN-FREEZE-CLASS-B-EXTENSION` (item #118).
   - Append `S88-BULLETIN-PER-POLE-PRIMARY-WALL-CLASSIFICATION-RULE-PIN` (item #119).

2. **Input-SHA capture**: at dispatch time, compute SHA-256 of every source file in the Input-SHA Ledger; substitute into `<pinned at dispatch>` slots.

3. **Block-diagonality feasibility pre-check** (item #112): per `math-scripts.md` §"D_K Block-Diagonality Pre-Check", verify L_max=14 cache regeneration feasibility via Casimir-bound argument OR Friedrich-Bär saturation theorem before dispatching #112. If empirically infeasible (W11-3 calibration), dispatch with Friedrich-Bär saturation as analytic substitute.

4. **Conditional dispatch chain**: #117 requires #116 verdict; orchestrator dispatches #117 only after #116 verdict-line lands.

5. **Sub-class taxonomy alignment**: items #115, #118, #119 are METHODOLOGY-class CONDITIONAL on M4 satisfaction; if allowlist append fails, classification falls through to COMPUTE-class with `.py` edit predicate (which fails M1) → plan-freeze halt requesting allowlist append.

---

**END OF S88 PLAN W10**
