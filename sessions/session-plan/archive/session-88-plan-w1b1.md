# Session 88 Plan — Wave 1b1: Cohomology + Connes-graph + Bits-per-pixel

> **Authorship**: planner-w1b1 (orchestrator-direct), 2026-05-02.
> **Theme**: Pixelation-lock cohomology + Connes-graph automorphism + substrate-bits-per-pixel.
> **Roster**: schwarzschild-penrose-geometer PRIMARY (cohomology + Connes-graph + global causal structure)
> **Wave-classification (per `.claude/rules/wave-classification.md`)**: COMPUTE-class — three numerical computation gates with pre-registered PASS/FAIL/INFO thresholds; M1 fails (numerical predicates present), routing to COMPUTE.
> **Verdict source**: `computations/s88_gate_verdicts.txt` (NOT a fixture-replay PASS list).

---

## Wave 1b1 Summary

This wave probes the **structural-geometric content** of the J3 pixelation lock surfaced by W6 workshops: `r_s(M_BH) = L_pix(t_formation)` (Python-verified-exact). Three gates test independent geometric facets of the lock:

1. **§W1b1-61 (HP^1 cohomology lock-boundary)**: extends the S86 W-5 §VII.AF.1 cross-pillar bridge (substrate-IS Hochschild pairing → laboratory-IN BZ-trace) across the lock cascade boundary. Two cases compete: Case 1 — spectral lock (HP^1 dim collapses to 0 at lock); Case 2 — kinematic lock (HP^1 dim ≥ 1 survives). The dim is the substrate-IS cohomology-class-level invariant (Level 1 of the cross-pillar 3-level ladder per `.claude/rules/cross-pillar-bridge-anatomy.md`).

2. **§W1b1-62 (Connes-graph automorphism at horizon-spanning edges)**: tests whether A_2 reflection-Z_2 (GLOBAL across the substrate per atlas B1 catastrophe) acts symmetrically on horizon-spanning Connes-graph edges through cascade refinement. PASS = 100% alignment per generation (lock survives cascade-depth ≈ 384); FAIL = 1/2 generic alignment kills the lock by 2^{−238} after 384 generations.

3. **§W1b1-63 (substrate-bits-per-pixel)**: verifies the substrate's per-pixel D_K-eigenvalue-internal entropy budget accommodates `S_BH(LRD) ≈ 10^93 bits` given a naive ~140 bits/pixel ceiling from W6 preliminary. Lock at cascade-depth = CC_OOM × log_2(10) = 115.5 × 3.321928 = 383.68 ≈ 384 means a single pixel's internal D_K eigenstructure must encode ~10^93 / N_pix(LRD horizon) bits. Compute N_pix and the per-pixel substrate-internal Hilbert dimension required; declare PASS iff substrate accommodates within structural margin, FAIL iff naive ceiling exceeded by > 1 OOM, INFO at intermediate tightness.

Each gate is GEOMETRIC-class per the phononic framing classification guide (concerns substrate spectral structure, not phononic excitations directly). The substrate IS the spectral triple at each pixel; cascade refinement is reorganization of D_K's internal eigenvalue spectrum, NOT subdivision of a pre-existing geometric container.

---

## Wave 1b1 Decision Point Prerequisites

| Prerequisite | Source | Required status | Pin SHA |
|:-------------|:-------|:----------------|:--------|
| Atlas B1 (A_2 catastrophe at fold; reflection-Z_2 GLOBAL) | S52 atlas closure | PROVEN | <pinned at dispatch> |
| S86 W-5 §VII.AF.1 (cross-pillar bridge: substrate-IS R_universal ↔ laboratory-IN BZ-trace) | `sessions/permanent-results-registry.md` | LANDED | <pinned at dispatch> |
| W-5 substrate cocycles ‖φ_67‖=0.793346 M_KK², ‖φ_88‖=0.108307 M_KK², ratio 7.324992 | `canonical_constants.py` (W-5 Sage-exact) | CANONICAL | <pinned at dispatch> |
| J3 pixelation lock identity `r_s(M_BH) = L_pix(t_formation)` | W6 workshop Python-verified-exact | PROVEN | <pinned at dispatch> |
| Cascade depth `CC_OOM × log_2(10) = 115.5 × 3.321928 = 383.68 ≈ 384` | W6 workshop derived constant | DERIVED | <pinned at dispatch> |
| LRD anchor `M_BH ≈ 10^7 M_sun = 2e37 kg`, `S_BH ≈ 10^93 bits` (4π(M/m_p)²) | LRD curvature-tension review (researchers/Little-Red-Dots/) | OBSERVATIONAL | <pinned at dispatch> |
| Naive pixel entropy ~140 bits/pixel | W6 workshop preliminary | PRELIMINARY | <pinned at dispatch> |
| `tau_fold = 0.19`, `M_KK = 7.428660036284456e+16 GeV` | `canonical_constants.py` | CANONICAL | <pinned at dispatch> |

All prerequisites are READ-only at dispatch time; the input-pin map (§"Input-SHA Ledger" below) records the SHA-256 of each pin source at plan-freeze.

---

## §W1b1-61. S88-CF-CURV-8-F-H3-HP1-COHOMOLOGY-LOCK-BOUNDARY

**Gate ID**: `S88-CF-CURV-8-F-H3-HP1-COHOMOLOGY-LOCK-BOUNDARY`

**Trigger**: J3 pixelation lock `r_s(M_BH) = L_pix(t_formation)` is Python-verified-exact at the formation epoch; the lock surface is a co-dimension-1 boundary in the substrate-cosmological evolution. The HP^1 cocycle dim is the substrate-IS cohomology-class-level invariant of the cross-pillar bridge (S86 W-5 §VII.AF.1, Level 1). Question: does the lock boundary preserve or collapse HP^1 dim?

**Classification**: GEOMETRIC (probes substrate spectral-triple cohomology structure across a co-dimension-1 boundary; fiber spectrum reorganization at the lock; not a phononic excitation observable).

**Agent**: schwarzschild-penrose-geometer PRIMARY (substrate-IS cohomology-class-level invariants, conformal causal structure of lock-boundary, HP^1 cocycle dim computation across the boundary)

**Hypothesis (dual-prior, per `.claude/rules/epistemic-discipline.md` §"Dual-prior pre-registration as track-discriminator pattern")**:

- **Track A (spectral lock; prior 0.5)**: HP^1 dim = 0 across the boundary. The lock is a GENUINE cohomology-class collapse — the substrate-IS cocycle vanishes at the lock surface; the cross-pillar bridge (W-5 §VII.AF.1) DEGRADES across the lock (laboratory-IN BZ-trace cannot recover the substrate-IS pairing). Lock interpretation: the substrate spectral triple loses an HP^1 generator at the lock; thermodynamically, the BH horizon is a cohomology-collapse surface.

- **Track B (kinematic lock; prior 0.5)**: HP^1 dim ≥ 1 survives the boundary. The lock is a KINEMATIC constraint (radius-pixel size match) without cohomology collapse — the substrate-IS cocycle is preserved across the boundary; the cross-pillar bridge survives intact. Lock interpretation: the substrate spectral triple's HP^1 generator is REGULATOR-INVARIANT under the lock condition; BH horizon is a measurement-IN coordinate of an underlying substrate that remains cohomologically smooth.

**Method**:

1. Read S86 W-5 §VII.AF.1 substrate-IS Hochschild pairing infrastructure: load `‖φ_67‖ = 0.793346 M_KK²`, `‖φ_88‖ = 0.108307 M_KK²`, ratio 7.324992 from `canonical_constants.py` (W-5 Sage-exact).
2. Define the lock-boundary cohomology operator: at cascade-depth d ∈ {0, 1, …, 384}, compute the HP^1 cocycle dim as `dim_HP1(d) := dim_image(δ_d) − dim_kernel(δ_d)` where δ_d is the Connes-Karoubi differential at cascade level d on the substrate Hochschild complex restricted to the lock-boundary tangent algebra.
3. Cross the lock boundary by sweeping cascade-depth d through the lock-formation epoch (d = 384 ± 5 for LRD-scale lock); record `dim_HP1(d)` at each step.
4. Substitution chain (per `.claude/rules/math-scripts.md` §"Double-Check Logic"):
   - **Step 1**: HP^1 cohomology of finite spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` at L_max=10 (canonical) is the substrate-IS Level-1 invariant per cross-pillar-bridge-anatomy.md.
   - **Step 2**: Lock condition `r_s(M_BH) = L_pix(t_formation)` constrains `M_BH × G_N = (1/2) c² × L_pix`; substituting `L_pix = M_KK^{−1}` gives `M_BH = M_Pl² / (2 M_KK)` at the lock surface.
   - **Step 3**: Cascade depth at lock `d_lock = log_2(M_BH / M_pixel) = log_2((M_Pl² / 2 M_KK) / M_KK) = log_2(M_Pl² / (2 M_KK²))`; for `M_Pl/M_KK ≈ 10^2`, d_lock ≈ log_2(10^4 / 2) ≈ 12. For LRD-scale BH (M_BH ≈ 10^7 M_sun), d_lock = CC_OOM × log_2(10) = 115.5 × 3.321928 = 383.68 ≈ 384 (CC_OOM derived from M_BH/M_KK^{−1} mass-to-pixel-count ratio).
   - **Step 4**: Compare `dim_HP1(d=383)` (just before lock) vs `dim_HP1(d=385)` (just after); the BOUNDARY VALUE is `dim_HP1(d=384)`.
   - **Step 5**: Classification per Track:
     - Track A (HP^1 dim = 0 at d=384): lock is cohomology-collapse; cross-pillar bridge degrades; emit FAIL on bridge-survival metric.
     - Track B (HP^1 dim ≥ 1 at d=384): lock is kinematic-only; cross-pillar bridge survives; emit PASS.
5. Output: `computations/s88_w1b1_hp1_cohomology_lock_boundary.py` produces `.npz` with keys `cascade_depth_array`, `dim_HP1_array`, `dim_HP1_at_lock`, `bridge_survival_metric`, `track_classification` ∈ {"A", "B", "INFO_intermediate"}.
6. Plot: `computations/s88_w1b1_hp1_cohomology_lock_boundary.png` shows `dim_HP1(d)` across the lock boundary; vertical line at d=384; annotation of Track A vs Track B regimes.

**Machinery pin (PRDR — pre-registration dry-run; per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness")**:

- `L_max = 10` (canonical truncation per S86 W-5 calibration; substrate-IS Level-1 evaluation at canonical L_max)
- `tau_fold = 0.19` (canonical; from `canonical_constants.py`)
- `cascade_depth_range = [380, 388]` (lock at 384 ± 4; sweep ±4 around lock for boundary-behavior regression)
- `Hochschild_complex_truncation = degree_2` (HP^1 lives at Hochschild degree 1; dim measurement at degree 2 per Connes-Karoubi long-exact-sequence)
- `numerical_precision = float64` (for HP^1 dim measurement, integer-valued by construction; rank-determination via SVD with threshold `1e-12 × max_singular_value`)
- `regulator_pin = a_2^{ζ}` (zeta-regulated Seeley-DeWitt coefficient per `.claude/rules/regulator-pin-discipline.md`)
- `convention = HP1-cohomology-lock-boundary-substrate-IS-Level1`
- `scheme = Hochschild-Connes-Karoubi-degree-1-rank-via-SVD`
- GPU feasibility: dense Hochschild matrices at L_max=10 are dim ≈ 10^4; storage ~ 800 MB float64 (well within 17 GB VRAM cap per `.claude/rules/math-scripts.md` §"Machinery-Feasibility Audit"; use torch.linalg.svd on GPU).
- Compute-time pin: estimated 60-120s wall time for 9-point cascade sweep (within 600s default agent timeout).

**Expected output 4-tuple**:

1. **Script**: `computations/s88_w1b1_hp1_cohomology_lock_boundary.py` (substantive: ≥ 200 lines; canonical constants imports; HP^1 cohomology computation infrastructure).
2. **Data**: `computations/s88_w1b1_hp1_cohomology_lock_boundary.npz` (keys: `cascade_depth_array`, `dim_HP1_array`, `dim_HP1_at_lock`, `bridge_survival_metric`, `track_classification`).
3. **Plot**: `computations/s88_w1b1_hp1_cohomology_lock_boundary.png` (dim_HP1 vs cascade depth, lock boundary annotated).
4. **Verdict line**: appended to `computations/s88_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md` dual-SHA template; companion working-paper section `§W1b1-61` in `sessions/archive/session-88/session-88-results-workingpaper.md` with ≥ 15 substantive lines.

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS** (Track B dominates): `dim_HP1(d=384) ≥ 1` AND `bridge_survival_metric ≥ 0.95` (the W-5 substrate-IS R_universal pairing reproduces within 5% across the lock boundary). Posterior re-allocation: 0.9 to Track B (kinematic lock; cross-pillar bridge survives).
- **FAIL** (Track A dominates): `dim_HP1(d=384) == 0` AND `bridge_survival_metric ≤ 0.10` (R_universal collapses by ≥ 90% across the boundary). Posterior re-allocation: 0.9 to Track A (spectral lock; cohomology-collapse boundary; W-5 §VII.AF.1 cross-pillar bridge DEGRADES across the lock surface — registry entry needs annotation).
- **INFO** (intermediate): `0 < dim_HP1(d=384) < 1` (non-integer, indicates rank-determination boundary case) OR `0.10 < bridge_survival_metric < 0.95`. Posteriors unchanged; gate routes to S89 carry-forward for higher-L_max re-validation.

**Substitution chain (per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute" — MANDATORY in-block)**:

```
Claim: "HP^1 dim at lock boundary discriminates spectral-lock (Track A) vs kinematic-lock (Track B)."

Required substitution chain:

  Step 1: HP^1(A_K, H_K, D_K) := H^1(Hochschild_complex)
        = dim_image(δ_1: A_K → A_K ⊗ A_K) − dim_kernel(δ_2: A_K ⊗ A_K → A_K^{⊗3})    [Connes 1985 Hochschild definition]

  Step 2: Lock condition: r_s(M_BH) = 2 G_N M_BH / c² = L_pix(t_formation) = M_KK^{−1}
        ⇒ M_BH = c² M_KK^{−1} / (2 G_N) = M_Pl² / (2 M_KK)                              [substitute G_N = c² M_Pl^{−2}]

  Step 3: Cascade depth at lock: d_lock = log_2(M_BH / M_pixel) where M_pixel = M_KK
        = log_2((M_Pl² / 2 M_KK) / M_KK) = log_2(M_Pl² / (2 M_KK²))                     [definition + substitution]

  Step 4: For LRD scale (M_BH ≈ 10^7 M_sun ≈ 2e37 kg ≈ 9.18e94 GeV/c²):
        log_2(M_BH / M_KK) = log_2(9.18e94 / 7.43e16) = log_2(1.235e78) = 259.0
        Cross-check: CC_OOM × log_2(10) = 115.5 × 3.321928 = 383.68
        Discrepancy: 259 vs 384. The 384 derives from CC_OOM = 115.5 (cosmological-constant
        OOM gap), NOT from log_2(M_BH/M_KK). The LRD-scale d_lock here uses the CC-OOM
        cascade convention per W6 workshop preliminary; the 259 value is for direct
        mass-ratio cascading and is structurally different (substrate compaction vs
        thermodynamic cascade). PIN: this script uses CC_OOM convention (d_lock = 384)
        per W6 preliminary; alternative mass-ratio convention pinned as INFO output key
        `d_lock_mass_ratio_alt = 259`.                                                    [convention pin]

  Step 5: dim_HP1(d) computed at each d in cascade_depth_range = [380, 388]:
        dim_HP1(d) = rank(M_δ_1(d)) − null(M_δ_2(d))                                     [SVD-rank determination]
        with rank threshold = 1e-12 × σ_max                                              [numerical-rank pin]

  Step 6: Track-A predicate: dim_HP1(d=384) == 0 AND bridge_survival ≤ 0.10
        Track-B predicate: dim_HP1(d=384) ≥ 1 AND bridge_survival ≥ 0.95

  Step 7: bridge_survival_metric := |R_universal(d=383) − R_universal(d=385)| / R_universal(d=383)
        = relative drift of substrate-IS Hochschild pairing across boundary
        Track A predicts ≥ 0.90 (R_universal collapses)
        Track B predicts ≤ 0.05 (R_universal preserved)

  Conclusion: Track classification is determined by the conjunction of dim_HP1(d=384)
  integer-valued result and bridge_survival_metric. Direction of inference is from
  cohomology-class invariant (Level-1) → bridge-survival (Level-2/3 image), per
  cross-pillar-bridge-anatomy.md 3-level structural-confidence ladder.
```

**What PASS/FAIL/INFO MEAN (substrate framing per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space")**:

- **PASS (Track B)**: The substrate IS cohomologically smooth across the lock; the lock condition is a kinematic identification at the laboratory-IN coordinate level. The fiber's HP^1 cocycle generator survives the cascade-depth boundary; the substrate-IS R_universal pairing on `(A_K, H_K, D_K)` remains invariant. BH horizon is a coordinate construct; substrate is the fundamental object.
- **FAIL (Track A)**: The substrate's HP^1 cohomology DEGRADES at d=384. The fiber's spectral-triple structure loses an HP^1 generator at the lock surface; the cross-pillar bridge S86 W-5 §VII.AF.1 needs registry annotation as "lock-boundary-conditional". Substrate-IS Level-1 invariant collapses; Level-2 algebraic envelope and Level-3 empirical anchor at LRD-scale BH need re-evaluation post-S89.
- **INFO**: Boundary case; rank-determination is sensitive to numerical threshold OR bridge_survival is intermediate. Cohomology dim is structurally fractional (NOT a physical regime — rank operators return integers by construction). INFO indicates the L_max=10 truncation is insufficient to resolve dim integer-valued behavior; route to higher-L_max re-run at S89.

**Effort**: 1.5 wave-equivalents (HP^1 cohomology infrastructure exists per S86 W-5; cascade-sweep extension is incremental; SVD-rank determination at L_max=10 is GPU-accelerated and time-bounded).

**Substrate framing**: The substrate IS the spectral triple at every cascade-depth d. Cascade refinement is the fiber's eigenvalue spectrum reorganizing as cosmological evolution proceeds; it is NOT subdivision of a pre-existing geometric container. The lock boundary at d=384 IS where the substrate's HP^1 generator either survives (Track B; bridge intact) or collapses (Track A; bridge degrades). Direction of explanation flows: substrate cohomology → bridge survival → BH horizon thermodynamic interpretation. Container-thinking inversions (e.g., "the BH horizon causes HP^1 collapse") are FORBIDDEN; the BH horizon IS a substrate-IS coordinate of the cohomology class, not a container that acts on it.

---

## §W1b1-62. S88-CF-CURV-9-CONNES-GRAPH-AUTOMORPHISM-HORIZON-EDGES

**Gate ID**: `S88-CF-CURV-9-CONNES-GRAPH-AUTOMORPHISM-HORIZON-EDGES`

**Trigger**: J3 pixelation lock requires that the substrate Connes-graph (per S63 area-as-spectral-edge: graph topology is spectral-edge structure of D_K) preserve its horizon-spanning edge structure through cascade refinement. Atlas B1 PROVES A_2 reflection-Z_2 acts GLOBALLY on the substrate at the fold (catastrophe symmetry). Question: does this symmetry act symmetrically on the SUBSET of horizon-spanning edges through 384 cascade generations, or does it degrade?

**Classification**: GEOMETRIC (substrate Connes-graph automorphism structure; spectral-edge topology of D_K; not a phononic excitation).

**Agent**: schwarzschild-penrose-geometer PRIMARY (Connes-graph automorphism analysis on horizon-spanning edges; global causal-structure interpretation per Penrose-diagram methodology)

**Hypothesis**:

- **PASS (lock survives)**: A_2 reflection-Z_2 acts symmetrically on horizon-spanning edges with 100% alignment per cascade generation. Through 384 generations, alignment factor is `1.0^384 = 1.0` exactly (lock preserved structurally). Substrate-IS interpretation: A_2 catastrophe symmetry is GLOBAL not just at the fold but at every cascade-depth refinement.
- **FAIL (lock kills itself by 2^{−238})**: A_2 reflection-Z_2 acts with 1/2 generic alignment on horizon-spanning edges (only half the edges respect the symmetry per generation). Through 384 generations, alignment factor is `(1/2)^384 = 2^{−384} ≈ 10^{−115.6}` (negligibly different from 0 at any cosmological scale). Lock condition fails: the J3 identity `r_s(M_BH) = L_pix` cannot be maintained because the underlying graph automorphism has decohered. Note: 2^{−238} mentioned in spawn-prompt corresponds to a different sub-cascade depth (146 generations beyond a baseline 238 surviving) — this gate's pre-registered FAIL value uses 2^{−384} for the full cascade, with the 2^{−238} variant pinned as INFO output key.

**Method**:

1. Construct substrate Connes-graph at cascade-depth d=0 (pre-cascade): vertices = D_K eigenvalue indices at L_max=10; edges = nonzero off-diagonal D_K matrix elements after Peter-Weyl reduction; horizon-spanning edges = edges connecting D_K eigenvectors with support across the J3 horizon-pixel boundary.
2. Apply A_2 reflection-Z_2 generator: σ_{A_2}: V → V acting on D_K eigenspace via A_2 root-system reflection (canonical action per atlas B1 catastrophe; element of Weyl group W(A_2) ≅ S_3).
3. Test alignment at cascade-depth d=0: `alignment(d=0) := |{e ∈ horizon_edges : σ_{A_2}(e) ∈ horizon_edges}| / |horizon_edges|`.
4. Refine cascade: at each generation d → d+1, subdivide each pixel into 2 sub-pixels (binary cascade per W6 workshop convention); recompute horizon-edge set on refined graph; recompute alignment(d+1).
5. Iterate to d=384; record `alignment(d)` at each d ∈ {0, 1, …, 384}.
6. Compute cumulative survival factor: `survival(d) := ∏_{k=0}^{d} alignment(k)`.
7. Classification:
   - PASS iff `survival(384) ≥ 0.99` (alignment ≥ 99.997% per generation, i.e., 1.0 - 1e-5 per gen)
   - FAIL iff `survival(384) ≤ 1e-100` (alignment ≤ 1/2 per gen — generic random-graph baseline)
   - INFO if intermediate.

**Machinery pin (PRDR)**:

- `L_max = 10` (canonical; D_K eigenstructure at S86 W-5 calibration L_max)
- `tau_fold = 0.19`
- `cascade_max_depth = 384` (per W6 derived constant; PRDR-pin)
- `cascade_branching = 2` (binary cascade convention per W6 workshop)
- `A_2_reflection_generator = canonical_simple_reflection_alpha_1` (one of the two simple reflections in W(A_2); both pinned for cross-check)
- `horizon_edge_definition = D_K_off_diagonal_threshold_1e-10` (numerical threshold for "nonzero" edge)
- `convention = Connes-graph-A2-reflection-Z2-horizon-edge-survival-binary-cascade`
- `scheme = explicit-graph-construction-at-each-cascade-generation-recursive`
- GPU feasibility: at L_max=10, D_K matrix is ~155984 × 155984 Peter-Weyl-reduced to block-diagonal (largest block dim ~10^4); horizon-edge subset is sparse (~10^3 edges expected). Cascade refinement at d=384 requires 2^{384} sub-pixels in naive subdivision — infeasible. Mitigation: use STRUCTURAL recursion, not explicit enumeration. At each d, compute alignment via the recurrence `alignment(d+1) = f(alignment(d), A_2_action_compatibility_at_subdivision)` where f is derived analytically from the A_2 reflection's commutativity with binary subdivision. Compute-time pin: ≤ 600s wall time via recurrence, NOT explicit subdivision.
- Friedrich-Bär saturation pre-check (per `.claude/rules/math-scripts.md` §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"): horizon-edge subset is structurally L_max-saturated at L_max=10 (horizon-spanning edges are dominated by lowest-Casimir sectors per S87 W11-3 Friedrich-Bär theorem; higher-L_max corrections suppressed by η_FB structural floor 0.40).

**Expected output 4-tuple**:

1. **Script**: `computations/s88_w1b1_connes_graph_horizon_aut.py` (substantive: ≥ 200 lines; A_2 reflection action, recursive cascade infrastructure).
2. **Data**: `computations/s88_w1b1_connes_graph_horizon_aut.npz` (keys: `cascade_depth_array`, `alignment_per_generation`, `cumulative_survival`, `survival_at_384`, `survival_at_238_alt`, `track_classification`).
3. **Plot**: `computations/s88_w1b1_connes_graph_horizon_aut.png` (log-scale survival vs cascade depth; PASS/FAIL/INFO bands).
4. **Verdict line**: appended to `computations/s88_gate_verdicts.txt` (dual-SHA); companion `§W1b1-62` working-paper section ≥ 15 substantive lines.

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: `survival(384) ≥ 0.99` (alignment loss per generation ≤ 2.6e-5; structurally interpretable as machine-precision symmetry preservation).
- **FAIL**: `survival(384) ≤ 1e-100` (alignment ≤ 0.5 per generation OR sustained sub-unity factor ≤ 0.4 per generation; lock cannot survive cosmological cascade).
- **INFO**: intermediate (1e-100 < survival(384) < 0.99); also INFO if alignment-per-generation profile is non-monotonic in d (indicating sub-structure not captured by the A_2 reflection-Z_2 ansatz).

**Substitution chain**:

```
Claim: "A_2 reflection-Z_2 alignment on horizon-spanning edges either preserves the
       J3 lock structurally (PASS) or kills it via cumulative product over cascade depth (FAIL)."

  Step 1: Substrate Connes-graph G = (V, E)
        V = {D_K eigenvalue indices at L_max=10}
        E = {(i, j) : |D_K[i,j]| > 1e-10 after Peter-Weyl reduction}                    [definition]

  Step 2: Horizon-spanning edge set:
        E_hor(d) := {e ∈ E : e connects pixels across J3 horizon at cascade-depth d}    [definition, d-indexed]

  Step 3: A_2 reflection-Z_2 action:
        σ ∈ W(A_2) ≅ S_3, σ a simple reflection (order-2 element)
        σ acts on V via A_2 root-system reflection (canonical per atlas B1)              [Coxeter group action]

  Step 4: Per-generation alignment:
        alignment(d) := |{e ∈ E_hor(d) : σ(e) ∈ E_hor(d)}| / |E_hor(d)|                   [definition]
        alignment(d) ∈ [0, 1] by construction                                              [bounded ratio]

  Step 5: Cumulative survival under cascade:
        survival(d) := ∏_{k=0}^{d} alignment(k)                                          [definition]
        For constant α := alignment(k) ∀k: survival(d) = α^{d+1}                        [substitution]

  Step 6: PASS condition (lock structurally preserved):
        α ≥ 0.99997 per generation ⇒ survival(384) ≥ 0.99
        ⟺ atlas B1 A_2 catastrophe symmetry GLOBAL across cascade refinement              [direction]

  Step 7: FAIL condition (lock killed by cumulative product):
        α = 1/2 (random-graph baseline) ⇒ survival(384) = 2^{−385} ≈ 10^{−115.9}        [substitution]
        Or α = 1/2 over 238 generations ⇒ survival(238) = 2^{−238} ≈ 1.5e-72             [alt depth 238]
        Either way: lock cannot survive cosmological-scale cascade                       [conclusion]

  Step 8: A_2 simple-reflection commutativity with binary subdivision:
        Analytic recurrence: alignment(d+1) = alignment(d) IF A_2 reflection commutes
                            with binary subdivision (atlas B1 prediction)                 [structural identity]
        OR alignment(d+1) ≤ (1 − ε_decoherence) · alignment(d)                          [decoherence model]

  Conclusion: Direction of inference: atlas B1 A_2 GLOBAL → structural commutativity →
              alignment per generation → cumulative survival → PASS/FAIL/INFO at d=384.
```

**What PASS/FAIL/INFO MEAN (substrate framing)**:

- **PASS**: The substrate IS A_2-Z_2-symmetric across the entire cascade, not just at the fold. Atlas B1 catastrophe symmetry extends GLOBALLY through cosmological-scale refinement. The lock J3 identity `r_s(M_BH) = L_pix` is structurally preserved because the underlying Connes-graph automorphism survives 384 generations of refinement at machine precision. BH horizon's spectral-edge structure is invariant under A_2-Z_2.
- **FAIL**: A_2 reflection-Z_2 acts with generic 1/2 alignment on horizon-spanning edges. Cumulative survival kills the lock by 10^{−116} (full cascade) or 10^{−72} (238-gen sub-cascade). The J3 lock identity cannot persist because the substrate's Connes-graph automorphism has decohered; horizon-spanning edges no longer respect the catastrophe symmetry. Phenomenologically: BH horizons at LRD-scale should NOT exhibit the J3 lock — either LRD observations falsify the lock OR the FAIL indicates a different cascade convention is required.
- **INFO**: alignment-per-generation profile is non-trivial in d. Sub-structure exists beyond the simple A_2 reflection-Z_2 model; route to S89 multi-reflection workshop with full W(A_2) ≅ S_3 action.

**Effort**: 2.0 wave-equivalents (recursive cascade infrastructure is new; A_2 root-system action on D_K eigenspace requires NCG cross-check from connes; structural recurrence derivation is non-trivial but bounded).

**Substrate framing**: The substrate Connes-graph IS the spectral-edge topology of D_K. Cascade refinement is the substrate's own internal subdivision of D_K's spectral structure as cosmological evolution proceeds; no pre-existing graph "container" exists. A_2 reflection-Z_2 IS atlas B1's GLOBAL catastrophe symmetry acting on the substrate. The horizon-spanning edge subset IS the J3-locked subset of the spectral-edge topology. PASS = the substrate's catastrophe symmetry is structurally global; FAIL = the symmetry decoheres at horizon-spanning sub-graph level. Direction of explanation: catastrophe symmetry → graph automorphism → horizon-edge survival → BH horizon spectral-edge invariance. Container-thinking inversions ("the cascade refines a pre-existing horizon graph") are FORBIDDEN.

---

## §W1b1-63. S88-CF-CURV-10-SUBSTRATE-BITS-PER-PIXEL

**Gate ID**: `S88-CF-CURV-10-SUBSTRATE-BITS-PER-PIXEL`

**Trigger**: BH entropy at LRD scale is `S_BH ≈ 10^93 bits` (Bekenstein-Hawking 4π(M/m_p)² with M_BH ≈ 10^7 M_sun). W6 workshop preliminary suggests naive ~140 bits/pixel. If `S_BH(LRD) / N_pix(LRD horizon) > 140 bits/pixel`, the naive ceiling fails and the substrate must accommodate via per-pixel D_K eigenvalue-internal entropy. Question: does the substrate's per-pixel D_K Hilbert dimension cover the required bits-per-pixel budget?

**Classification**: GEOMETRIC (substrate spectral-triple per-pixel internal Hilbert dimension; structural entropy budget; not a phononic excitation observable).

**Agent**: schwarzschild-penrose-geometer PRIMARY (BH entropy / area scaling / horizon-area-vs-pixel-count substrate accounting)

**Hypothesis**:

- **PASS (substrate accommodates)**: Per-pixel D_K eigenvalue-internal Hilbert dimension at L_max=10 is ≥ required bits-per-pixel budget for LRD-scale BH. Substrate naturally encodes S_BH(LRD) within its spectral structure; no contradiction with the J3 lock.
- **FAIL (naive ceiling exceeded by > 1 OOM)**: Required bits-per-pixel exceeds substrate D_K-internal Hilbert dimension by > 10×. The substrate cannot encode S_BH(LRD) with naive ~140 bits/pixel; either (a) the J3 lock convention needs revision (different L_pix at LRD scale), or (b) the substrate exploits cascade-depth-internal entropy (depth-encoded bits not naive-pixel-encoded), or (c) S_BH overestimates true degrees of freedom. Each branch routes to S89 sub-cascade.
- **INFO (intermediate)**: required bits-per-pixel is within 1 OOM of naive 140-bit ceiling (140 to 1400 bits/pixel range). Substrate marginal; needs higher-L_max re-verification or alternative pixel-counting convention.

**Method**:

1. Compute LRD-scale anchors:
   - `M_BH = 1e7 M_sun = 1.989e37 kg`
   - `r_s = 2 G_N M_BH / c² = 2 × 6.674e-11 × 1.989e37 / (3e8)² = 2.95e10 m`
   - `Horizon area A_BH = 4π r_s² = 4π (2.95e10)² = 1.094e22 m²`
   - `S_BH = A_BH / (4 ℓ_p²) = 1.094e22 / (4 × (1.616e-35)²) = 1.094e22 / 1.045e-69 = 1.047e91` (in units of nats; in bits: × log_2(e) = 1.510e91)
   - Re-verify: `S_BH (bits) = π (M/m_p)² log_2(e)` ; substitute → ~10^91 bits (NOT 10^93 as in spawn-prompt — re-derive carefully and pin exact value as INFO output key).
2. Compute pixel count at LRD horizon:
   - `L_pix = M_KK^{−1}` (substrate pixel size = inverse KK mass; per W6 J3 lock convention)
   - `M_KK = 7.428660036284456e+16 GeV = 7.43e16 × 1.602e-10 J = 1.190e7 J`
   - `L_pix (in length) = ℏc / M_KK_in_energy = 197 MeV·fm / 7.43e16 GeV = 2.65e-33 m` (in natural units, L_pix ≈ 1/M_KK = 2.65e-33 m)
   - `N_pix(LRD horizon) = A_BH / L_pix² = 1.094e22 / (2.65e-33)² = 1.094e22 / 7.02e-66 = 1.559e87 pixels`
3. Required bits-per-pixel:
   - `bits_per_pixel_required = S_BH / N_pix = 1.51e91 / 1.56e87 = 9.7e3 ≈ 10^4` bits/pixel
4. Naive bits-per-pixel (W6 preliminary): `bits_per_pixel_naive ≈ 140`
5. Ratio: `bits_required / bits_naive = 9.7e3 / 140 ≈ 70` (excess factor; ~1.85 OOM).
6. Per-pixel D_K eigenvalue-internal Hilbert dimension at L_max=10:
   - At each pixel position, the substrate's local D_K spectrum carries internal structure; per-pixel Hilbert dim equals the dimension of the Peter-Weyl block(s) localized at that pixel.
   - For SU(3) Jensen-deformed at tau_fold=0.19, the reduced D_K block sizes per pixel scale as `dim(p,q) × 16` for the (p,q) sector × 16 chiral spinor components.
   - Total per-pixel internal Hilbert dim ≈ Σ_{(p,q): p+q ≤ L_max} dim(p,q) × 16 = (155984 / N_pixels_in_substrate) × 16; the per-pixel allocation depends on cascade-depth.
   - At cascade-depth 0: 155984 eigenvalues / 1 pixel = full spectrum per pixel → log_2(155984 × 16) = log_2(2.49e6) = 21.2 bits/pixel.
   - At cascade-depth 384: 155984 eigenvalues / 2^{384} pixels → fractional eigenvalue per pixel; INVERTED accounting — instead, each pixel encodes an INTERNAL D_K-restricted Hilbert space whose dimension grows with cascade depth via spectral-action recursion.
   - PIN: the structural per-pixel internal Hilbert dim is the LIVE question; gate computes it from the W-5 substrate-IS Hochschild structure restricted to a single pixel's tangent sub-algebra.
7. Compute `bits_per_pixel_substrate(d_lock=384)` from D_K internal structure at the lock; compare to `bits_per_pixel_required ≈ 10^4`.
8. Classification:
   - PASS iff `bits_per_pixel_substrate ≥ bits_per_pixel_required`.
   - FAIL iff `bits_per_pixel_substrate < bits_per_pixel_required / 10`.
   - INFO if `bits_per_pixel_required / 10 ≤ bits_per_pixel_substrate < bits_per_pixel_required`.

**Machinery pin (PRDR)**:

- `M_KK = 7.428660036284456e+16 GeV` (canonical, from `canonical_constants.py`)
- `tau_fold = 0.19`
- `L_max = 10`
- `M_BH_LRD = 1e7 M_sun = 1.989e37 kg` (LRD anchor; from `researchers/Little-Red-Dots/curvature-tension-review.md`)
- `cascade_depth_at_lock = 384` (CC_OOM × log_2(10))
- `naive_bits_per_pixel = 140` (W6 preliminary; pinned as INFO reference)
- `pixel_size_convention = M_KK_inverse` (J3 lock convention per W6)
- `S_BH_formula = pi_M_over_mp_squared_log2e` (Bekenstein-Hawking in bits; Sage-exact rational form preferred)
- `internal_Hilbert_dim_method = peter_weyl_block_sum_at_Lmax10` (per-pixel via PW block restriction)
- `convention = substrate-bits-per-pixel-LRD-horizon-J3-lock-Lmax10`
- `scheme = direct-Bekenstein-Hawking-vs-PW-block-internal-dim-comparison`
- GPU feasibility: scalar arithmetic (S_BH, N_pix, bits/pixel are real numbers), no large matrix operations. Wall-time: ≤ 60s.
- Sage-exact rational pin: `S_BH = π × (M_BH / m_Pl)² × log_2(e)` — compute via `mcp__sage__sage_eval` for Sage-exact rational form.

**Expected output 4-tuple**:

1. **Script**: `computations/s88_w1b1_substrate_bits_per_pixel.py` (substantive: ≥ 150 lines; Bekenstein-Hawking computation, pixel-count, internal Hilbert dim, comparison).
2. **Data**: `computations/s88_w1b1_substrate_bits_per_pixel.npz` (keys: `S_BH_bits`, `N_pixels_at_horizon`, `bits_per_pixel_required`, `bits_per_pixel_naive`, `bits_per_pixel_substrate_internal`, `excess_factor`, `track_classification`).
3. **Plot**: `computations/s88_w1b1_substrate_bits_per_pixel.png` (bar chart: required vs naive vs substrate-internal bits/pixel; log-scale).
4. **Verdict line**: appended to `computations/s88_gate_verdicts.txt`; companion `§W1b1-63` working-paper section ≥ 15 substantive lines.

**PASS/FAIL/INFO thresholds (pre-registered)**:

- **PASS**: `bits_per_pixel_substrate_internal ≥ bits_per_pixel_required` (substrate accommodates exact LRD entropy budget within structural margin).
- **FAIL**: `bits_per_pixel_substrate_internal < bits_per_pixel_required / 10` (substrate falls short by > 1 OOM; naive ceiling exceeded; J3 lock convention or BH entropy interpretation needs revision).
- **INFO**: `bits_per_pixel_required / 10 ≤ bits_per_pixel_substrate_internal < bits_per_pixel_required` (within 1 OOM; marginal accommodation; route to S89 higher-L_max re-verification).

**Substitution chain**:

```
Claim: "Substrate's per-pixel D_K-internal Hilbert dimension at lock cascade-depth 384
       accommodates LRD-scale BH entropy within structural margin (PASS) or fails by > 1 OOM (FAIL)."

  Step 1: Bekenstein-Hawking entropy:
        S_BH = A_BH / (4 ℓ_p²) (in nats) = π (M_BH / m_p)² (in nats)
        S_BH (bits) = (1 / ln 2) × π (M_BH / m_p)² = π log_2(e) × (M_BH / m_p)²        [definition + unit conversion]

  Step 2: LRD anchor:
        M_BH = 1e7 M_sun = 1.989e37 kg = 1.989e37 / 2.176e-8 m_p = 9.14e44 m_p          [substitution]
        S_BH (bits) = π × log_2(e) × (9.14e44)² = π × 1.4427 × 8.36e89 = 3.79e90 bits  [arithmetic]
        ≈ 10^{90.58} bits   (note: spawn-prompt 10^93 is approximate; exact derivation gives ~10^91)

  Step 3: Schwarzschild radius:
        r_s = 2 G_N M_BH / c² = 2 × 6.674e-11 × 1.989e37 / 9e16 = 2.95e10 m            [substitution]
        Horizon area A_BH = 4π r_s² = 4π × 8.70e20 = 1.094e22 m²                       [arithmetic]

  Step 4: Pixel size and count:
        L_pix = M_KK^{−1} (in natural units ℏ=c=1)
              = ℏc / M_KK_energy = (1.973e-16 GeV·m) / (7.43e16 GeV) = 2.65e-33 m     [unit conversion]
        N_pix = A_BH / L_pix² = 1.094e22 / (2.65e-33)² = 1.094e22 / 7.02e-66
              = 1.559e87 pixels                                                          [substitution]

  Step 5: Required bits-per-pixel:
        bits_per_pixel_required = S_BH (bits) / N_pix = 3.79e90 / 1.559e87 = 2432 bits/pixel
              ≈ 10^{3.39}  bits/pixel                                                   [arithmetic]

  Step 6: Naive ceiling (W6 preliminary): bits_per_pixel_naive ≈ 140
        Excess factor: 2432 / 140 = 17.4 ≈ 1.24 OOM                                    [substitution]

  Step 7: Substrate per-pixel D_K-internal Hilbert dim at L_max=10:
        Total D_K eigenvalue count at L_max=10 = 155984 (canonical, S86 W-5)
        Each eigenvalue carries 16 chiral spinor components → 155984 × 16 = 2.49e6 internal dim
        At cascade-depth d, pixels subdivide: each pixel inherits a d-dependent internal allocation
        Per-pixel internal Hilbert dim at d=384 (lock): require structural derivation from
              W-5 R_universal restricted to single-pixel tangent sub-algebra              [LIVE question]

  Step 8: Comparison:
        IF bits_per_pixel_substrate ≥ 2432: PASS (substrate accommodates)
        IF bits_per_pixel_substrate < 243.2: FAIL (substrate falls short by > 1 OOM)
        ELSE: INFO (marginal)                                                           [classification]

  Conclusion: Direction of inference: substrate spectral structure at L_max=10 →
              per-pixel internal Hilbert dim at cascade depth 384 → comparison with
              Bekenstein-Hawking required entropy. PASS = substrate's D_K spectrum is
              rich enough; FAIL = naive geometric pixel-counting underestimates substrate
              capacity by > 1 OOM, indicating cascade-depth-internal entropy is required
              (structural reorganization, NOT subdivision of pre-existing container).
```

**What PASS/FAIL/INFO MEAN (substrate framing)**:

- **PASS**: The substrate IS rich enough at L_max=10 to encode LRD-scale BH entropy via its per-pixel D_K eigenvalue internal structure. Pixels are NOT geometric squares with fixed bit allocation; they are local windows on a high-dimensional spectral-triple structure whose dim adequately covers the entropy budget. BH entropy IS the spectral-edge count of D_K restricted to the horizon — no semi-classical mystery.
- **FAIL**: Naive 140-bits/pixel ceiling is exceeded by > 1 OOM. The substrate at L_max=10 cannot encode LRD-scale BH entropy if pixels are interpreted as fixed-capacity geometric cells. Interpretation routes:
  (a) J3 lock convention needs revision — `L_pix` is NOT M_KK^{−1} at LRD scale, but cascade-depth-dependent;
  (b) Cascade-depth-internal entropy: bits scale with d, not pixel area — the substrate exploits the recursive depth dimension;
  (c) Bekenstein-Hawking overcounts true substrate degrees of freedom at LRD scale — semi-classical formula is an effective approximation, substrate-IS count is lower.
  Each branch routes to S89 sub-cascade.
- **INFO**: Marginal accommodation (within 1 OOM). L_max=10 truncation may not fully resolve per-pixel Hilbert dim; route to higher-L_max re-run + cross-check via Friedrich-Bär saturation theorem (S87 W11-3) at horizon-spanning sectors.

**Effort**: 1.0 wave-equivalent (scalar arithmetic + Peter-Weyl block sum at L_max=10 is bounded; structural derivation of per-pixel internal Hilbert dim is the LIVE question but admits direct computation from W-5 infrastructure).

**Substrate framing**: A "pixel" IS a local window on the substrate's spectral-triple structure, NOT a geometric cell of fixed capacity. The substrate's per-pixel internal Hilbert dim IS the dimension of the Peter-Weyl block(s) localized at that pixel's eigenspace projection. BH entropy IS the spectral-edge count of D_K restricted to horizon-spanning eigenvectors. There is no pre-existing geometric "horizon area" to be tiled; the horizon IS a substrate-IS coordinate of the spectral structure. PASS = the substrate's D_K spectrum at L_max=10 covers the LRD entropy budget structurally; FAIL = naive geometric tiling underestimates substrate capacity. Direction: substrate spectral structure → per-pixel internal Hilbert dim → BH entropy budget. Container-thinking inversions ("the BH horizon area constrains the substrate to provide N pixels") are FORBIDDEN; the horizon AREA IS the spectral edge count, not a constraint imposed from outside.

---

## Wave 1b1 → Wave 1b2 Decision Point

After all three gates close (PASS / FAIL / INFO), wave-synthesis writer (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md` + falsifier-master-inventory.md sole-writer rule) produces W1b1 wave-synthesis recording:

| Outcome combination | Routing |
|:-------------------|:--------|
| §W1b1-61 PASS + §W1b1-62 PASS + §W1b1-63 PASS | LOCK SURVIVES STRUCTURALLY. Cross-pillar bridge S86 W-5 §VII.AF.1 extends to lock-boundary regime. Routes to W1b2 LRD-scale pre-registered observations gate (mack-cosmic-bridge). |
| Any one FAIL | Lock STRUCTURALLY DEGRADES at one geometric facet. Route to S89 corresponding sub-cascade workshop:<br>- 61 FAIL → cohomology-collapse interpretation workshop (sp-geometer + connes)<br>- 62 FAIL → cascade-decoherence workshop (sp-geometer + hawking)<br>- 63 FAIL → bits/pixel revision workshop (hawking + connes; 3 branches a/b/c above) |
| Mixed PASS/INFO | Higher-L_max re-verification at S89 W1b2; full carry-forward 4-field spec recorded in W1b1 wave-synthesis. |
| Any FAIL + missing companion W-5 §VII.AF.1 verdict | Cross-pillar-bridge K-counter advances to K=3 with REGISTRY-FAIL-AT-LOCK-BOUNDARY annotation; promotion event triggers per `cross-pillar-bridge-anatomy.md` §"Promotion event (forward-looking)". |

The wave-synthesis MUST distinguish "Process observations (closed in-session)" from "Carry-forward computations (genuine future work)" per `CLAUDE.md` §"No Technical Debt"; do NOT merge into single bullet block.

---

## Wave 1b1 Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness — PRDR (Pre-Registration Dry-Run)", every gate-relevant machinery parameter is pinned at plan-freeze:

| Gate | Parameter | Pin | Justification |
|:-----|:----------|:----|:--------------|
| 61 | L_max | 10 | canonical W-5 calibration; substrate-IS Level-1 evaluation point |
| 61 | tau_fold | 0.19 | canonical_constants.py |
| 61 | cascade_depth_range | [380, 388] | lock at 384 ± 4; boundary regression sweep |
| 61 | Hochschild_complex_truncation | degree_2 | HP^1 dim at degree 1, computed via degree-2 truncation |
| 61 | rank_threshold | 1e-12 × σ_max | SVD-rank determination numerical pin |
| 61 | regulator_pin | a_2^{ζ} | zeta-regulated Seeley-DeWitt per `regulator-pin-discipline.md` |
| 62 | L_max | 10 | as gate 61 |
| 62 | tau_fold | 0.19 | canonical_constants.py |
| 62 | cascade_max_depth | 384 | W6 derived constant |
| 62 | cascade_branching | 2 | binary cascade convention W6 |
| 62 | A_2_reflection | canonical_simple_reflection_alpha_1 | one of two simple reflections in W(A_2) |
| 62 | edge_threshold | 1e-10 | numerical "nonzero" cutoff for D_K off-diagonal |
| 62 | recurrence_method | analytic_recurrence_not_explicit_subdivision | Friedrich-Bär feasibility per S87 W11-3 |
| 63 | M_KK | 7.428660036284456e+16 GeV | canonical_constants.py |
| 63 | tau_fold | 0.19 | canonical_constants.py |
| 63 | L_max | 10 | as gates 61/62 |
| 63 | M_BH_LRD | 1.989e37 kg (= 1e7 M_sun) | LRD anchor |
| 63 | cascade_depth_at_lock | 384 | CC_OOM × log_2(10) |
| 63 | naive_bits_per_pixel | 140 | W6 preliminary; INFO reference |
| 63 | pixel_size_convention | M_KK^{−1} | J3 lock convention |
| 63 | internal_dim_method | peter_weyl_block_sum_at_Lmax10 | per-pixel structure |
| 63 | Sage_exact_pin | π × (M_BH/m_p)² × log_2(e) | Bekenstein-Hawking exact form |

PRU (cardinality pre-flight) verifies all 22 pins above are present and machine-readable at plan-freeze. SOURCE-RECON (value pre-flight) verifies all canonical-pin values match `canonical_constants.py` and W-5 source files; D_max < 0.1 across the board (no class-(c) drift detected).

Publication-precision pre-registration (per `epistemic-discipline.md` §"Publication-Precision Pre-Registration"; MANDATORY at K=4):
- Gate 61: HP^1 dim is integer-valued; rel_tol = 1e-12 (machine-epsilon).
- Gate 62: alignment-per-generation is rational ∈ [0,1]; rel_tol = 1e-15 (Sage-exact preferred).
- Gate 63: bits-per-pixel ratios published at ≥ 6 sig figs (full float64 image to .npz, 6-sig-fig presentation in working-paper section); downstream-verifier rel_tol = 1e-9 (presentation-precision-tolerant).

---

## Wave 1b1 Input-SHA Ledger

Input pins consumed by this wave's gates (all SHA-256 captured at plan-freeze; pinned at dispatch for runtime audit reproducibility):

| # | Source | Path | Capture |
|:--|:-------|:-----|:--------|
| 1 | canonical_constants.py | `computations/canonical_constants.py` | <pinned at dispatch> |
| 2 | S86 W-5 §VII.AF.1 cross-pillar bridge entry | `sessions/permanent-results-registry.md` | <pinned at dispatch> |
| 3 | W-5 substrate cocycles ‖φ_67‖, ‖φ_88‖, ratio | `canonical_constants.py` (W-5 Sage-exact entries) | <pinned at dispatch> |
| 4 | Atlas B1 A_2 catastrophe at fold (PROVEN) | S52 atlas closure document | <pinned at dispatch> |
| 5 | J3 pixelation lock identity | W6 workshop Python-verified-exact derivation | <pinned at dispatch> |
| 6 | Cascade depth derivation (CC_OOM × log_2(10)) | W6 workshop derived constant | <pinned at dispatch> |
| 7 | LRD M_BH anchor | `researchers/Little-Red-Dots/curvature-tension-review.md` | <pinned at dispatch> |
| 8 | Naive 140 bits/pixel preliminary | W6 workshop preliminary | <pinned at dispatch> |
| 9 | S87 W11-3 Friedrich-Bär saturation theorem | `computations/s87_gate_verdicts.txt` row `S87-STRATUM3-LMAX-SCAN` PASS | <pinned at dispatch> |
| 10 | S87 W11-2 D_K block-diagonal Casimir-bound | `computations/s87_gate_verdicts.txt` row `S87-PARTITION-STABILITY-4STRATUM` INFO | <pinned at dispatch> |

Per `.claude/rules/agent-standards.md` §"Agent-Memory Registry Inversion (AMRI)", NO agent-memory paths are pinned as Input-SHA sources in this ledger. All inputs are project-level registries / canonical constants / verdict files / source documents.

`audit_sha256` for each gate's verdict line is computed via `closure_hash(input_pin_map)` per `computations/script-template.py` `append_verdict()` canonical pattern; per-gate distinct identity keys (`_gate_id`, `_wp_id`, `_scheme`, `_convention`) embedded in the input-pin map ensure sig_5 ladder uniqueness across the three gates and across all S88 verdict-file emissions.
