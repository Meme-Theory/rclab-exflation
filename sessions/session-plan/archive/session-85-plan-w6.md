# Session 85 Plan — Wave W6: sp-origin reviewer wave

**Owner**: schwarzschild-penrose-geometer
**Output**: `sessions/session-plan/session-85-plan-w6.md`
**Generated**: 2026-04-21
**Item count**: 7 (all conv=1, sp-origin)
**Batch**: Batch 1 (concurrent with W0, W1a, W1b, W2, W3, W4, W5)
**Script prefix**: `s85_w6_`
**Verdict file (canonical)**: `computations/s85_gate_verdicts.txt`

---

## Wave W6 Summary

W6 maps the geometric structural boundary of the exflation transit using seven sp-origin probes. The wave extends the S77–S84 CMPP transit-invariance result from an 8-checkpoint sample to a dense τ-grid (W6-2), formalizes the two analog horizons identified in W8B-96 (W6-1 acoustic white hole, W6-4 extremal horizon), tests the regulator-conditional bifurcation of conformal infinity (W6-3), measures the universality of the Mellin-cone under triple extensions (W6-5), updates the canonical Penrose-diagram catalog for the post-S84 state (W6-6), and re-probes the S78-W3-H Petrov Type D fragility under controlled non-block-diagonal perturbations (W6-7).

**Substrate framing (applied uniformly)**: Every causal-structure statement in this wave is a **visualization of a metric that emerges from the a_2 Seeley-DeWitt coefficient of the Dirac operator D_K on Jensen-deformed SU(3)**. The Penrose diagram is not the physics; it is a map of the conformal structure inherited from the spectral action. Where a Type change, a horizon, or a conformal-infinity bifurcation appears, the *fundamental* question is: what is the spectral-action gradient doing, and which D_K eigenvalue-spectrum feature sources the emergent geometric singularity? Container thinking ("the geometry does X to the fiber") is inverted: the fiber's D_K eigenvalue reorganization produces the emergent g_M, whose Penrose diagram we then draw.

**EVOI stance**: W6 is a wave of **structural consolidation and fragility mapping**, not new-physics gates. None of the seven items is expected to flip a master-gate verdict. All seven tighten, extend, or stress-test existing permanent structural results. Expected distribution: ~4 PASS (consolidation of existing monotonicity/invariance), ~2 INFO (diagnostic extensions with no pre-registered flip), ~1 FAIL-boundary (W6-7 could reveal true Type-change under perturbation).

---

## Wave W6 Decision Point Prerequisites

Before any W6 gate executes, the following must be on disk and SHA-pinned:
- `computations/canonical_constants.py` (constants import)
- `sessions/framework/Penrose-Diagrams.md` (S53 definitive 9-diagram catalog; W6-6 updates this)
- `sessions/archive/session-84/session-84-s5-*.md` (CMPP transit-invariance closure from W8B)
- `.claude/agent-memory/schwarzschild-penrose-geometer/MEMORY.md` (modulus-space organizational diagram)
- `researchers/Schwarzschild-Penrose/` (primary sources — re-read at wave start)
- `computations/` S77 overshoot output (τ=1.614 checkpoint metric data for W6-2 dense-grid seed)

All input SHAs are pinned in the per-gate block under **Input SHA-256 pins** and aggregated in the §Wave W6 Input-SHA Ledger at the bottom.

---

## §W6-1. S85-ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL

1. **Gate ID**: S85-W6-1-AWH-FORMAL
2. **Trigger**: [VERIFY-THEOREM]
3. **Classification**: GEOMETRIC (emergent causal structure from phononic substrate; the "white hole" is a supersonic acoustic horizon, not a GR black-hole time-reverse)
4. **Agent type**: schwarzschild-penrose-geometer (sole owner; no hawking/spectral co-owner — the theorem statement is a geometric-theorem promotion of a W8B analog and lives inside the sp methodology)
5. **Hypothesis**: The supersonic transit through the van Hove fold (Mach 13.75 at τ=τ_fold) produces a **globally causally disconnected pair of regions** (pre-fold causal past ∖ post-fold causal future) in the acoustic metric induced by the a_2 Seeley-DeWitt coefficient of D_K(τ). Formally: there exists a spacelike hypersurface Σ_fold such that no future-directed timelike curve in the acoustic metric connects J^−(τ < τ_fold) to J^+(τ > τ_fold). This is the **acoustic analog of a white-hole causal structure** (outgoing null congruence, no past null infinity reachable from the interior).
6. **Method**:
   - Script: `computations/s85_w6_acoustic_white_hole_formal.py`
   - Data: `computations/s85_w6_acoustic_white_hole_formal.npz`
   - Plot: `computations/s85_w6_acoustic_white_hole_formal.png` (Penrose diagram of the acoustic metric at τ ∈ [0, τ_fold + ε])
   - Imports: `from canonical_constants import M_KK, tau_fold, c_Gold, c_fabric, dt_transit, v_crit, Mach_max` (add any missing)
   - GPU/CPU policy: CPU-only; symbolic-first (SageMath MCP for the conformal-factor algebra), NumPy for null-geodesic integration. Matrices are ≤ 16×16 (8D internal + 4D external block structure); no GPU needed. Cap `OMP_NUM_THREADS=8`.
   - Pipeline: (i) write down acoustic metric g_ac = Ω² g_M with conformal factor Ω = c_s / c_sound from the a_2 coefficient; (ii) identify the supersonic region {v > c_sound}; (iii) integrate null geodesics from τ = τ_fold − 0.01 forward and from τ = τ_fold + 0.01 backward; (iv) verify no causal curve connects the two sets; (v) formalize as a theorem statement with proof sketch.
   - SHAs: pinned below; closure SHA computed in Section 4 of `_recovery_controller` template.
7. **Machinery pin (PRDR)**:
   - `N_eval`: 5000 null-geodesic integration steps per direction
   - `L_max`: N/A (geometric gate; spectral L_max enters only through the a_2 coefficient via canonical_constants)
   - `scan_range`: τ ∈ [τ_fold − 0.05, τ_fold + 0.05], step 1e-4
   - `tolerance`: RATIO 1e-8 for causal-curve connection test (min distance in proper-time units)
   - `scheme`: Eddington-Finkelstein null coordinates (advanced + retarded)
   - `convention`: (+, −, −, −) Lorentzian; null-geodesic affine parameter normalized at Σ_fold
   - `random_seed`: 85061 (for any stochastic perturbation of initial conditions in the null-geodesic integrator's rejection sampling)
   - `GPU path`: disabled; CPU-only NumPy/SciPy
8. **Expected output 4-tuple**: `(value=THEOREM_AWH_FORMAL, scheme=EF_null, convention=mostly_minus, L_max=NA)` with closure SHA pinning the acoustic-metric expression + null-geodesic solver config.
9. **PASS/FAIL/INFO**:
   - **PASS**: No future-directed causal curve connects J^−(τ < τ_fold − ε) to J^+(τ > τ_fold + ε); min causal separation ≥ tolerance.
   - **FAIL**: At least one causal curve connects the two regions (would retract the "horizon-problem-solved" substrate claim in `phononic-framing.md`).
   - **INFO**: The causal-disconnection holds in a strict-null sense but with < tolerance margin; theorem stands but with narrower stated bound.
10. **Substitution chain (SIGN/VERIFY)**:
    ```
    Def 1: g_ac_μν(x,τ) = Ω(τ)² g_M_μν(x)        [acoustic metric from a_2]
    Def 2: c_sound(τ) = c_Gold · sqrt(d²S_spectral / dτ²)   [phononic sound speed from spectral stiffness]
    Def 3: v(τ) = |dτ/dt|_transit                 [transit velocity along τ-coordinate]
    Def 4: Mach(τ) = v(τ) / c_sound(τ)             [local Mach number]

    Step 1: At τ = τ_fold, Mach_max = 13.75 > 1   [canonical_constants; supersonic]
    Step 2: g_ac at τ_fold has signature flip on the τ-coordinate
           ⇒ τ-surfaces are spacelike on one side of fold, timelike on the other
    Step 3: Null cones at τ = τ_fold − ε tilt outward; at τ_fold + ε tilt inward
    Step 4: The intersection of J^+(τ < τ_fold) with the τ = τ_fold slice is ∅
    Step 5: Causal disconnection DIRECTION: pre-fold → post-fold causal curve NON-EXISTENT
    Conclusion: Theorem statement holds; no future-directed timelike curve bridges Σ_fold
    ```
11. **PASS/FAIL implications**:
    - PASS ⇒ promotes the W8B-96 Analog A from "working-paper lemma" to a permanent geometric theorem (registry landing in `summary/framework-status.md` §PROVEN). Strengthens the claim that exflation solves the horizon problem structurally, not by isotropy assumption.
    - FAIL ⇒ retracts the acoustic-horizon framing; the "horizon problem solved by acoustic white hole" reframe in `phononic-framing.md` becomes unsupported. Does NOT invalidate the transit — only the causal-disconnect interpretation of it.
    - INFO ⇒ registry land with narrower margin; note in substrate geometry doc that causal separation is delicate but nonzero.
12. **Effort**: 1 agent-hour (symbolic setup 20 min, numerical integration 20 min, Penrose diagram via `/penrose-diagram` skill 20 min).
13. **Substrate framing**: The "white hole" is not a GR time-reverse of a black hole. It is the emergent causal structure of the acoustic metric g_ac = Ω² g_M, where Ω is built from the *second moment of the D_K spectral action*. The eigenvalue reorganization of D_K across τ_fold is the fundamental event; the causal disconnect is a derived property of the emergent acoustic metric. Do NOT explain this as "matter flowing through a GR horizon." The substrate *is* what changes; the horizon is the visual.

---

## §W6-2. S85-CMPP-PETROV-DENSER-GRID

1. **Gate ID**: S85-W6-2-CMPP-DENSE
2. **Trigger**: [VERIFY]
3. **Classification**: GEOMETRIC
4. **Agent type**: schwarzschild-penrose-geometer
5. **Hypothesis**: The CMPP Petrov-type classification of the static product spacetime M⁴ × SU(3)(τ) is **Type D transit-invariant** on a dense grid τ ∈ [0, 1.7] at step 0.01 (170+ points), not just at the 8 S77–S84 checkpoints {0.00, 0.10, 0.19, 0.22, 0.285, 0.30, 0.537, 1.614}. Dynamic CMPP type remains G (transit-invariant, v_term-dominated).
6. **Method**:
   - Script: `computations/s85_w6_cmpp_dense_grid.py`
   - Data: `computations/s85_w6_cmpp_dense_grid.npz` (Petrov type + min-boost-weight per τ)
   - Plot: `computations/s85_w6_cmpp_dense_grid.png` (bw+2, bw+1, bw0, bw−1, bw−2 moduli vs τ, log scale)
   - Imports: `from canonical_constants import M_KK, tau_fold, tau_dump, Mach_max, v_term, v_crit`
   - GPU/CPU policy: **GPU** via torch.linalg (170 points × eigendecomposition of 12D Weyl tensor = 2550 eigendecompositions on 16×16 matrices is cheap but parallelizes well). Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` with torch+ROCm. Fallback CPU cap `OMP_NUM_THREADS=8`.
   - Pipeline: (i) for each τ in the grid, compute 12D metric from canonical Jensen ansatz; (ii) Riemann, Weyl via Bianchi identity (NOT direct Weyl = R − Schouten, per MEMORY.md warning); (iii) decompose into boost-weight components (bw+2, +1, 0, −1, −2) in a null tetrad adapted to the M⁴ factor; (iv) classify per CMPP criterion; (v) for the dynamic case, include v_term = dτ/dt from the transit; (vi) emit Petrov type vs τ.
7. **Machinery pin (PRDR)**:
   - `N_eval`: 171 τ-grid points (0.00 to 1.70 step 0.01)
   - `L_max`: N/A (geometric; spectral eigenspace is not scanned here)
   - `scan_range`: τ ∈ [0.00, 1.70]
   - `step_size`: 0.01 in τ
   - `tolerance`: ABSOLUTE 1e-50 for min-boost-weight floor (below this, treat as numerical zero)
   - `scheme`: Jensen canonical metric 3·diag(e^{−2τ}×3, e^{τ}×4, e^{2τ}×1); Riemann from `einsum('abca->bc', R)` for Ricci (per MEMORY.md bookkeeping); Weyl via Bianchi K = |C|² + (4/(n−2))|Ric|² − (2/((n−1)(n−2)))R² with n=12
   - `convention`: NP boost-weight sign convention of Coley-Milson-Pravda-Pravdova (CMPP) 2004
   - `random_seed`: N/A (deterministic)
   - `GPU path`: `torch.linalg.eigh` for Weyl-operator spectrum on GPU; `torch.einsum` for tensor contractions. Profile memory: 171 × 144 × 144 × float64 = 28 MB, well within 17.1 GB VRAM.
8. **Expected output 4-tuple**: `(value=TYPE_D_TRANSIT_INVARIANT, scheme=CMPP_2004, convention=NP_boost_weight, L_max=NA)` with closure SHA pinning the grid + tetrad choice.
9. **PASS/FAIL/INFO**:
   - **PASS**: Petrov type = D on all 171 grid points (static); type = G on all 171 grid points (dynamic). Min boost-weight ±2 above tolerance throughout.
   - **FAIL**: Type-change detected at one or more grid points (e.g., Type II region between checkpoints). Would refute "transit-invariant" as universal and localize the type-change to a new τ-band.
   - **INFO**: Marginal points (bw±2 within 1 decade of tolerance) flagged; majority-PASS but with boundary annotations.
10. **Substitution chain (SIGN/VERIFY)**:
    ```
    Def 1: Type D ⇔ (bw+2 = 0) AND (bw−2 = 0) AND (bw±1 = 0) AND (bw0 ≠ 0)    [CMPP def]
    Def 2: Transit-invariance ⇔ Type(τ) = const for τ in the considered range
    Step 1: S77 8-checkpoint result: Type D at {0.00, 0.10, 0.19, 0.22, 0.285, 0.30, 0.537, 1.614}
    Step 2: Between-checkpoint Weyl tensor is polynomial in e^{±τ} (from Jensen metric)
    Step 3: Polynomial in e^{±τ} cannot have isolated zeros in bw±2 unless roots
            of exponential polynomials, which are (generically) ISOLATED DISCRETE
    Step 4: Direction: between-checkpoint bw±2 either stays strictly zero OR crosses zero at
            ≤ finite number of discrete τ_i; 171 dense points sample distinct test points
    Step 5: If all 171 points satisfy bw±2 < tolerance, then Type D on dense sample
            ⇒ Type D on continuum except at measure-zero set (provably smaller than grid spacing)
    Conclusion: PASS on dense grid ⇒ Type D is τ-analytic, not checkpoint-artifact
    ```
11. **PASS/FAIL implications**:
    - PASS ⇒ upgrades the S77–S84 result from "8-point invariance" to "dense-grid invariance" in the permanent-results registry; the Type D transit-invariance claim becomes a stable permanent result (survives grid-spacing audits).
    - FAIL ⇒ localizes a type-change to a specific τ-band, triggers a new W7+ investigation of the spectral-action-derived source of the type transition.
    - INFO ⇒ grid is dense enough to detect marginal boost-weights; flag specific τ-bands for W7 follow-up with denser local sampling.
12. **Effort**: 1 agent-hour (script assembly 15 min, GPU run 5 min, plotting 15 min, analysis 25 min).
13. **Substrate framing**: The Petrov type is a **classification of the Weyl tensor of the emergent 12D metric**, which itself emerges from the a_2 Seeley-DeWitt coefficient of D_K. Type D is not a fundamental substrate property — it is a consequence of the block-diagonal structure of D_K combined with the Jensen ansatz. The transit-invariance of Type D reflects the **spectral-action-level invariance** that block-diagonality is τ-preserved along the canonical Jensen path. A Type change would indicate a spectral-action feature we had not yet recognized.

---

## §W6-3. S85-CONFORMAL-INFINITY-BIFURCATION

1. **Gate ID**: S85-W6-3-CONF-INF-BIFURC
2. **Trigger**: [VERIFY]
3. **Classification**: GEOMETRIC
4. **Agent type**: schwarzschild-penrose-geometer (conformal-compactification is sp core methodology); hawking-spectral-geometer consulted offline (via memo, not co-owner) for the regulator-family accounting
5. **Hypothesis**: The structure of conformal infinity ℐ⁺ (its topology and dimensionality) of the emergent 4D metric g_M depends on the choice of spectral-action regulator within the 5-regulator atlas (cutoff, heat-kernel, zeta, Pauli-Villars, dimensional). Different regulators yield different conformal boundaries: (a) some produce standard asymptotically flat ℐ⁺ ≅ ℝ × S², (b) some produce asymptotically dS ℐ⁺ ≅ S³ (cosmological boundary), (c) some produce pathological ℐ⁺ (non-Hausdorff). We pre-register that **at least two distinct conformal-infinity topologies appear across the 5 regulators**, making ℐ⁺ structure regulator-conditional.
6. **Method**:
   - Script: `computations/s85_w6_conformal_infinity_bifurcation.py`
   - Data: `computations/s85_w6_conformal_infinity_bifurcation.npz`
   - Plot: `computations/s85_w6_conformal_infinity_bifurcation.png` (5-panel Penrose diagram array, one per regulator)
   - Imports: `from canonical_constants import M_KK, tau_fold, tau_dump, Lambda_Planck, L_max_canonical`
   - GPU/CPU policy: CPU-only (conformal-factor algebra is symbolic); SageMath MCP for the symbolic limit Ω(r) → 0 as r → ∞ per regulator.
   - Pipeline: (i) for each of 5 regulators, compute the a_2 coefficient at L_max = 10; (ii) derive g_M asymptotic form at r → ∞; (iii) compute conformal factor Ω(r) such that g̃ = Ω² g_M is regular at ℐ⁺; (iv) identify the topology of the Ω = 0 locus; (v) construct Penrose diagram per regulator via the `/penrose-diagram` skill.
7. **Machinery pin (PRDR)**:
   - `N_eval`: 5 regulators × 1000 r-grid points each = 5000
   - `L_max`: 10 (canonical regulator-atlas reference L_max)
   - `scan_range`: r ∈ [r_fold, 10^6 · r_fold] (out to effective ℐ⁺)
   - `tolerance`: ABSOLUTE 1e-12 for Ω → 0 detection
   - `scheme`: 5-regulator atlas = {hard cutoff, Gaussian heat-kernel, zeta-function, Pauli-Villars, dimensional}
   - `convention`: (+, −, −, −); conformal factor Ω chosen such that g̃ is smooth at ℐ⁺
   - `random_seed`: N/A (deterministic)
   - `GPU path`: disabled; symbolic + CPU NumPy only
8. **Expected output 4-tuple**: `(value=BIFURC_MAP, scheme=5_regulator_atlas, convention=mostly_minus_conformal, L_max=10)` with closure SHA pinning the regulator-family choice.
9. **PASS/FAIL/INFO**:
   - **PASS (=hypothesis confirmed)**: ≥ 2 distinct conformal-infinity topologies appear across the 5 regulators; ℐ⁺ structure is **regulator-conditional**.
   - **FAIL**: All 5 regulators yield the same ℐ⁺ topology; ℐ⁺ is **regulator-invariant**, which would be a strong invariance result going beyond currently-established local regulator-invariance.
   - **INFO**: Bifurcation appears but is numerical-precision-borderline; resolve at higher L_max in S86.
10. **Substitution chain (SIGN/VERIFY)**:
    ```
    Def 1: ℐ⁺ = {points at r → ∞ along future-directed null geodesics}
    Def 2: Conformal factor Ω(r) such that g̃ = Ω²g_M regular at ℐ⁺
    Def 3: Topology(ℐ⁺) = topology of {Ω = 0} submanifold
    Def 4: a_2^(R)(τ) = a_2 coefficient under regulator R    [spectral action output]
    Def 5: g_M^(R) = metric derived from a_2^(R)                [emergent]

    Step 1: Different regulators R ∈ {cutoff, heat, zeta, PV, dim} yield different a_2^(R)
           (DIFFERENT BY DEFINITION — regulator-invariance is a property to PROVE, not an axiom)
    Step 2: Different a_2^(R) ⇒ different g_M^(R) asymptotic behavior as r → ∞
    Step 3: Different asymptotic g_M ⇒ different conformal factor Ω^(R)
    Step 4: Different Ω^(R) ⇒ potentially different topology of {Ω^(R) = 0}
    Step 5: Direction of "bifurcation" claim: ≥ 2 distinct topologies ⇒ PASS (supports regulator-
           conditional ℐ⁺); 1 unique topology ⇒ FAIL (ℐ⁺ is regulator-invariant, strong result)
    Conclusion: PASS/FAIL direction is clear — the question is which way the empirics go.
    ```
11. **PASS/FAIL implications**:
    - PASS ⇒ Penrose diagram catalog must be regulator-indexed; no universal "the Penrose diagram of exflation" exists. Implies DR3-regulator-successor-tree (W0-4 item) is structurally needed — supporting the cross-reviewer consensus. Strengthens the case for regulator-scan as a first-class methodology.
    - FAIL ⇒ ℐ⁺ topology is regulator-invariant; substantially strengthens the framework by showing a global geometric invariant survives the regulator ambiguity. Promotion to permanent-results registry. (This is an unusually strong outcome if it lands.)
    - INFO ⇒ re-run at L_max = 12 in S86 with tightened tolerance.
12. **Effort**: 2 agent-hours (5 × regulator-specific conformal-factor derivation 60 min, Penrose diagram array 45 min, analysis 15 min).
13. **Substrate framing**: Conformal infinity is not a property of a pre-existing spacetime container; it is the **far-r limit of the metric emergent from the D_K spectral action**. Different regulators = different projections of the same D_K spectrum onto the a_2 coefficient, not different physics. A regulator-conditional ℐ⁺ means the *projection* to 4D emergent geometry is regulator-dependent at the asymptotic level — the underlying substrate is unique. This is a mapping question, not a physics question.

---

## §W6-4. S85-EXTREMAL-HORIZON-ANALOG-FORMAL

1. **Gate ID**: S85-W6-4-EXTREMAL-HORIZON-FORMAL
2. **Trigger**: [VERIFY-THEOREM]
3. **Classification**: GEOMETRIC (emergent horizon in the modulus-space effective metric, analog of GR extremal-BH structure)
4. **Agent type**: schwarzschild-penrose-geometer (sole owner)
5. **Hypothesis**: The dump point τ = 0.19 in the modulus-space effective metric satisfies **κ = 0** (vanishing surface gravity) and **T_H = 0** (vanishing Hawking temperature), placing it in the **extremal-horizon class** of the CMPP Type D → Type II degeneration. Formally: the dump surface Σ_dump := {τ = τ_dump} is a Killing horizon of the modulus-time Killing vector ∂_t with κ(Σ_dump) = 0.
6. **Method**:
   - Script: `computations/s85_w6_extremal_horizon_formal.py`
   - Data: `computations/s85_w6_extremal_horizon_formal.npz`
   - Plot: `computations/s85_w6_extremal_horizon_formal.png` (κ vs τ near τ_dump; Penrose diagram of the modulus-space effective metric)
   - Imports: `from canonical_constants import M_KK, tau_fold, tau_dump, T_BCS, kappa_BCS, T_H_dump`
   - GPU/CPU policy: CPU-only; symbolic κ derivation via Sage, numerical verification via NumPy.
   - Pipeline: (i) write modulus-space effective 2D metric g_mod(τ, t) from the Jensen potential V_tree(τ) = 1 − f(τ)/10; (ii) identify Killing vector ∂_t; (iii) locate Killing horizon = {norm(∂_t) = 0}; (iv) compute surface gravity κ = (1/2) √(∇_μ ξ_ν ∇^μ ξ^ν) at the horizon; (v) verify κ(τ_dump) = 0 to machine precision; (vi) verify this identifies with CMPP Type D→II degeneration at τ_dump per MEMORY.md.
7. **Machinery pin (PRDR)**:
   - `N_eval`: 10000 τ-grid points in [τ_dump − 0.01, τ_dump + 0.01]
   - `L_max`: N/A
   - `scan_range`: τ ∈ [0.18, 0.20]; ultra-dense near τ_dump = 0.19
   - `tolerance`: ABSOLUTE 1e-14 for κ = 0 (machine-epsilon bound)
   - `scheme`: Jensen V_tree(τ) = 1 − f(τ)/10 modulus-space potential; induced 2D metric ds² = −N(τ)² dt² + dτ²/V(τ)
   - `convention`: (−, +) Lorentzian 2D modulus-space; ∂_t is the timelike Killing vector; surface gravity defined via ξ^μ ∇_μ ξ^ν = κ ξ^ν on the horizon
   - `random_seed`: N/A
   - `GPU path`: disabled
8. **Expected output 4-tuple**: `(value=KAPPA_EQ_0, scheme=Jensen_V_tree, convention=2D_modulus_metric, L_max=NA)` with closure SHA pinning the modulus metric form.
9. **PASS/FAIL/INFO**:
   - **PASS**: κ(τ_dump) < 1e-14 (effectively zero to machine precision); Σ_dump is extremal.
   - **FAIL**: κ(τ_dump) > 1e-14; dump is a sub-extremal horizon, not extremal. Would retract the "κ = 0, T_H = 0" entry in MEMORY.md modulus-space org diagram.
   - **INFO**: κ is zero at second order but nonzero at third order in (τ − τ_dump); degenerate but not analytically flat.
10. **Substitution chain (SIGN/VERIFY)**:
    ```
    Def 1: Killing horizon Σ = {p : g(ξ,ξ)(p) = 0}   where ξ = ∂_t
    Def 2: κ² = −(1/2) (∇^μ ξ^ν)(∇_μ ξ_ν)             (on Σ, timelike ξ)
    Def 3: Extremal ⇔ κ = 0 ⇔ horizon is a double root of g(ξ,ξ)

    Step 1: g_mod(τ,t) = −N(τ)²dt² + dτ²/V(τ),  N² ∝ V(τ) near dump
    Step 2: g(ξ,ξ) = −N(τ)² ⇒ horizon at N² = 0 ⇔ V(τ) = 0
    Step 3: τ_dump = 0.19 is where V'(τ) = 0 simultaneously with V(τ) = 0
           (B2 minimum of V — verify in canonical_constants)
    Step 4: Double root condition ⇒ κ² = (N·N')² / V(τ)|_{τ_dump} → 0/0 form
           L'Hôpital: κ² = (N'·N' + N·N'')² / V'(τ)|_{τ_dump}
    Step 5: With V'(τ_dump) = 0, κ² → 0 (provided numerator vanishes at same order)
    Direction: κ = 0 at extremal horizon ⇒ T_H = κ/(2π) = 0 ⇒ PASS
    Conclusion: κ(τ_dump) = 0 is direction-pinned; empirical test is whether V'(τ_dump) is
                exactly zero or small-but-nonzero.
    ```
11. **PASS/FAIL implications**:
    - PASS ⇒ promotes the dump = extremal-horizon analog from MEMORY.md note to permanent result. Implies T_H = 0 is structural, not empirical. Strengthens the thermodynamic-null interpretation of the post-transit freeze. Registry landing.
    - FAIL ⇒ dump is sub-extremal; T_H > 0 at the freeze-out, opening a Hawking-emission channel previously closed. Would require re-examination of the post-transit thermal state.
    - INFO ⇒ degenerate extremality (flat at 2nd order, not higher); register as "quasi-extremal" with the specific order of flatness.
12. **Effort**: 1 agent-hour (symbolic κ derivation 30 min, numerical verification 10 min, Penrose diagram 20 min).
13. **Substrate framing**: The "extremal horizon" at τ_dump is not a GR black-hole horizon; it is a **Killing horizon of the 2D modulus-space effective metric** derived from the Jensen tree-level potential. T_H = 0 means **no spectral-action gradient sources Hawking-like radiation at the freeze-out** — which is the substrate-level statement of what the "extremal" label captures. The fundamental physics is the vanishing of dS/dτ at the dump, which is a D_K spectral property. The horizon label is the visualization.

---

## §W6-5. S85-MELLIN-CONE-UNIVERSALITY-EXTENDED-TRIPLES

1. **Gate ID**: S85-W6-5-MELLIN-CONE-EXT
2. **Trigger**: [VERIFY]
3. **Classification**: GEOMETRIC (spectral-triple classification; the Mellin cone is the spectral-weight locus in dimension-spectrum space)
4. **Agent type**: schwarzschild-penrose-geometer (with spectral-geometer offline consultation for the triple-extension classification, as flagged in §W8-89 origin)
5. **Hypothesis**: The Mellin-cone structure identified in §W8-89 (Connes-Moscovici dimension spectrum of the canonical Jensen-SU(3) × A_F triple) is **universal** across the admissible extended-triple family (A_F replaced by: quaternionic A_F_H, complex A_F_C, real A_F_R, Majorana-doubled A_F_M, Hochschild-extended A_F_Hoch — 5 extended triples). Universality means: the cone's apex (s = 3), edge set, and convexity structure are invariant; only the residue magnitudes scale with the triple dimension.
6. **Method**:
   - Script: `computations/s85_w6_mellin_cone_universality.py`
   - Data: `computations/s85_w6_mellin_cone_universality.npz` (5 cones × dimension-spectrum residues)
   - Plot: `computations/s85_w6_mellin_cone_universality.png` (overlay of 5 cones in (Re s, Im s, residue magnitude))
   - Imports: `from canonical_constants import L_max_canonical, d_spec, c_S_canon`
   - GPU/CPU policy: CPU-only; Mellin-transform integrals via mpmath for arbitrary precision; spectral-triple extension algebra via Sage.
   - Pipeline: (i) construct 5 extended spectral triples differing only in the finite algebra A_F; (ii) compute Connes-Moscovici dimension spectrum per triple via meromorphic continuation of ζ(s) = Tr(|D|^{−s}); (iii) extract apex, edges, convexity; (iv) compare across triples.
7. **Machinery pin (PRDR)**:
   - `N_eval`: 5 triples × 8 dimension-spectrum points (s ∈ {3, 2, 1, 0, −1, −2, −3, −4}) = 40
   - `L_max`: 10 (spectral truncation for the eigenvalue sum in ζ(s))
   - `scan_range`: s ∈ [−4, 3] with 0.01 step along Re(s) axis for apex-edge localization
   - `tolerance`: RATIO 1% for universality test (apex s-value match); ABSOLUTE 1e-10 for residue-magnitude ratios
   - `scheme`: Connes-Moscovici 1995 dimension-spectrum definition; zeta-regularization of Tr|D|^{−s}
   - `convention`: canonical ordering of s from high to low; residues taken at simple poles
   - `random_seed`: N/A
   - `GPU path`: disabled; mpmath (CPU) for arbitrary precision
8. **Expected output 4-tuple**: `(value=UNIVERSAL_APEX_EDGES, scheme=Connes_Moscovici_1995, convention=zeta_regularization, L_max=10)` with closure SHA pinning the 5-triple family.
9. **PASS/FAIL/INFO**:
   - **PASS**: Apex at s = 3 across all 5 triples (tolerance RATIO 1%); edge set identical up to residue-magnitude scaling; convexity preserved. Mellin cone is universal.
   - **FAIL**: Apex shifts across triples, OR edge set differs, OR convexity breaks. Mellin-cone is triple-dependent, retracting the §W8-89 universality claim.
   - **INFO**: Apex universal; edges differ only in residue magnitudes (expected); flag as "partial universality" and register.
10. **Substitution chain (SIGN/VERIFY)**:
    ```
    Def 1: ζ_T(s) = Tr(|D_T|^{−s})    for spectral triple T = (A, H, D)
    Def 2: Dim spectrum Σ_T = {poles of ζ_T analytically continued}
    Def 3: Mellin cone C_T = convex hull of Σ_T in (Re s, Im s, |residue|)
    Def 4: Universality ⇔ apex(C_T) = s_* invariant, edges({C_T_i}) identical up to residue scaling

    Step 1: 5 triples T_i differ only in A_F; |D_T| is the SAME operator truncated by
           different spectral projections from A_F
    Step 2: ζ_T(s) = Σ_n λ_n^{−s}, where {λ_n} depends on A_F-projection
    Step 3: Apex s_* = dim_spec of D (D itself does not change) = 3 for canonical Dirac
    Step 4: Direction: apex is a DYNAMICAL-DIMENSION property of D; A_F cannot shift it
           ⇒ apex invariance is expected; residue magnitudes scale with Tr_{A_F}
    Step 5: Universality: apex + edge set ≥ 1% agreement across 5 triples ⇒ PASS
    Conclusion: The "universality" direction is pinned — apex is D-determined, not A_F-determined.
    ```
11. **PASS/FAIL implications**:
    - PASS ⇒ §W8-89 Mellin-cone universality promoted to permanent result; strengthens the structural claim that spectral-triple internal-algebra variations do not change the global dimension-spectrum topology. Supports the cross-reviewer DR3-regulator-successor framing (W0-4).
    - FAIL ⇒ Mellin-cone is triple-conditional; §W8-89 result localizes to the canonical triple only. Opens a new branch-discriminator problem for observational pre-registration.
    - INFO ⇒ partial universality registered; note apex stability but edge residue-only scaling.
12. **Effort**: 1.5 agent-hours (5 triples × 15 min each + comparison analysis 15 min).
13. **Substrate framing**: The Mellin cone is a property of the **spectral triple's dimension spectrum** — it is the pure-substrate description of the D_K eigenvalue-distribution geometry. Universality across triple extensions means the substrate's dimensional structure is robust against the choice of internal finite algebra. The "cone" is not an emergent 4D geometric object; it lives in dimension-spectrum space. This gate does not test emergent physics — it tests substrate-level geometric robustness.

---

## §W6-6. S85-PENROSE-DIAGRAM-CATALOG-UPDATE

1. **Gate ID**: S85-W6-6-PENROSE-CATALOG
2. **Trigger**: [AUDIT]
3. **Classification**: GEOMETRIC (documentation / permanent-results landing; no new physics)
4. **Agent type**: schwarzschild-penrose-geometer (sole owner of the canonical Penrose-diagram catalog)
5. **Hypothesis**: The 9 definitive Penrose diagrams in `sessions/framework/Penrose-Diagrams.md` (S53) are **incomplete relative to the post-S84 state**. This gate updates the catalog to reflect: (a) the W8B-96 acoustic-white-hole diagram (new, from W6-1), (b) the extremal-horizon modulus-space diagram (new, from W6-4), (c) the regulator-conditional ℐ⁺ family (up to 5 new diagrams, from W6-3 if PASS), (d) the CMPP-dense-grid consolidated transit diagram (updated, from W6-2), (e) the post-S77 overshoot turnaround at τ = 1.614 (new). PASS = catalog compiles without contradictions and all new diagrams are labeled per output-standards.
6. **Method**:
   - Script: `computations/s85_w6_penrose_catalog_update.py` (compilation driver; invokes the `/penrose-diagram` skill for each diagram)
   - Data: `computations/s85_w6_penrose_catalog_update.npz` (diagram metadata: τ-coordinates, boundary labels, horizon lines)
   - Plot: `figures/penrose/s85_w6_catalog/` (directory with 13–14 TikZ `.tex` files, one per diagram)
   - Documentation update: appends to `sessions/framework/Penrose-Diagrams.md` — no overwrite (Penrose-Diagrams.md is append-only per chronological-integrity rule)
   - Imports: `from canonical_constants import *`
   - GPU/CPU policy: CPU-only; TikZ compilation is CPU-bound
   - Pipeline: (i) enumerate the S53 diagram list (9 diagrams); (ii) identify gaps relative to W6-1, W6-2, W6-3, W6-4 outputs; (iii) via the `/penrose-diagram` skill, generate TikZ for each new diagram with full boundary labels (i⁺, i⁻, i⁰, ℐ⁺, ℐ⁻, horizons, singularities, shaded regions); (iv) compile to PDF; (v) append to Penrose-Diagrams.md with cross-refs.
7. **Machinery pin (PRDR)**:
   - `N_eval`: up to 14 diagrams (9 existing + up to 5 new)
   - `L_max`: N/A (documentation gate)
   - `scan_range`: N/A
   - `tolerance`: THEOREM — all diagrams must have ALL of {i⁺, i⁻, i⁰, ℐ⁺, ℐ⁻, horizons, singularities, shaded regions} labeled per sp output standards
   - `scheme`: `/penrose-diagram` skill canonical TikZ preamble
   - `convention`: null geodesics at 45°; conformal factor chosen such that diagrams are finite; shaded regions = trapped/normal/anti-trapped/ergoregion
   - `random_seed`: N/A
   - `GPU path`: disabled
8. **Expected output 4-tuple**: `(value=CATALOG_COMPLETE, scheme=penrose_diagram_skill, convention=conformal_45deg_null, L_max=NA)` with closure SHA pinning the diagram-set manifest.
9. **PASS/FAIL/INFO**:
   - **PASS**: All ≥ 13 diagrams compile without LaTeX errors; all have full boundary labels per output standards; `sessions/framework/Penrose-Diagrams.md` updated with cross-refs.
   - **FAIL**: Compilation fails, OR at least one diagram has incomplete boundary labels, OR the append introduces a contradiction (e.g., the same τ-region has two incompatible causal structures in different diagrams without a stated reason).
   - **INFO**: All diagrams compile and label, but ≥ 1 stated causal structure awaits a separate W6-* gate verdict (e.g., W6-3 conformal-infinity-bifurcation still uncomputed at catalog-update time); those diagrams marked PRELIMINARY per output-standards rule.
10. **Substitution chain (SIGN/VERIFY)**:
    ```
    Def 1: Penrose-Diagrams.md := S53 definitive 9-diagram set
    Def 2: New-diagram set Δ := {AWH, extremal-horizon, 5 regulator-conditional ℐ⁺, CMPP dense, τ=1.614 overshoot}
    Def 3: Catalog = Penrose-Diagrams.md ∪ Δ
    Step 1: For catalog COMPLETE, every diagram d in Catalog has labels(d) ⊇ {i⁺,i⁻,i⁰,ℐ⁺,ℐ⁻,horizons,singularities,shading}
    Step 2: For catalog CONSISTENT, for every τ-region R, all diagrams including R agree on causal structure(R)
    Step 3: PASS ⇔ COMPLETE ∧ CONSISTENT ∧ compiles
    Conclusion: PASS direction = all 3 boolean checks true; FAIL = any one false.
    ```
    No sign/direction substitution needed beyond the boolean checklist.
11. **PASS/FAIL implications**:
    - PASS ⇒ canonical Penrose-diagram catalog is post-S84 current; all future sp-origin analyses reference this updated catalog. Strengthens visual-documentation infrastructure.
    - FAIL ⇒ documentation gap remains; the S53 catalog is stale and must be regenerated. Blocks future sp-origin workshops that depend on canonical diagrams.
    - INFO ⇒ catalog updated with PRELIMINARY labels on items depending on uncomputed W6-3; resolve after W6-3 lands.
12. **Effort**: 2 agent-hours (diagram-by-diagram TikZ via skill 90 min, catalog cross-ref writing 15 min, compilation 15 min).
13. **Substrate framing**: The Penrose diagram is a **visualization of the conformal structure of the emergent metric g_M**, which is in turn derived from the a_2 spectral-action coefficient of D_K. The catalog is not a list of physical spacetimes; it is a list of *projections of D_K substrate dynamics onto 4D emergent conformal structures*. Each diagram encodes a different τ-slice or regulator of the same underlying D_K. The catalog as a whole is thus a spectral-projection atlas, not a multiverse.

---

## §W6-7. S85-PETROV-DEPENDENCE-ON-NON-BLOCK-DIAGONAL-PERTURBATIONS

1. **Gate ID**: S85-W6-7-PETROV-NON-BD-PERT
2. **Trigger**: [VERIFY]
3. **Classification**: GEOMETRIC (fragility / stability analysis of the Type D structural result)
4. **Agent type**: schwarzschild-penrose-geometer (owner; consults S78-W3-H fragility record in MEMORY.md)
5. **Hypothesis**: The CMPP Type D classification of the Jensen-SU(3) × A_F triple is **fragile under small non-block-diagonal perturbations** of D_K. Specifically: adding a perturbation ε · O to D_K with O off-block-diagonal (O ∈ Hom(SU(2)-block, C²-block)) at ε = 0.01 induces a Type D → Type I degeneration at τ = 0.537 (phase-transition point). The S78-W3-H result (from MEMORY.md: "S78-W3-H: CMPP Type D FRAGILE (D→I under ε = 0.01 non-block-diag perturbation)") is revisited on the dense τ-grid to localize the fragility band.
6. **Method**:
   - Script: `computations/s85_w6_petrov_non_bd_perturbation.py`
   - Data: `computations/s85_w6_petrov_non_bd_perturbation.npz` (Petrov type(τ, ε) map)
   - Plot: `computations/s85_w6_petrov_non_bd_perturbation.png` (2D heatmap of Petrov type in (τ, ε) with Type D/I boundary)
   - Imports: `from canonical_constants import M_KK, tau_fold, tau_dump, tau_phase_trans, L_max_canonical`
   - GPU/CPU policy: **GPU** via torch (91 τ-points × 11 ε-points × 12D Weyl eigendecomp = 1001 decompositions, each on 144×144-equivalent tensor space). Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` with torch+ROCm.
   - Pipeline: (i) build canonical D_K at each τ; (ii) construct a block-generic perturbation O (single off-block matrix element); (iii) for ε ∈ {0.0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0}, compute Petrov type via CMPP at each τ ∈ [0.0, 0.9] step 0.01; (iv) construct the type-change boundary in (τ, ε); (v) compare to S78-W3-H check point at (τ=0.537, ε=0.01).
7. **Machinery pin (PRDR)**:
   - `N_eval`: 91 τ-points × 10 ε-values = 910 perturbed Weyl decompositions
   - `L_max`: 10
   - `scan_range`: τ ∈ [0.00, 0.90] step 0.01; ε ∈ {0.0, 10^−3, 3·10^−3, 10^−2, 3·10^−2, 10^−1, 3·10^−1, 1.0, 3.0, 10.0} (log-spaced)
   - `tolerance`: ABSOLUTE 1e-12 for Type boundary (a boost-weight component crossing this threshold is the type-change signature)
   - `scheme`: perturbed D_K = D_K^canonical + ε · O with O a single-element off-block-diagonal matrix (specific pin: O_{SU(2), C²} element (0,3) = 1, all others 0); this is the W3-H canonical perturbation direction
   - `convention`: CMPP NP boost-weight; Weyl via Bianchi identity
   - `random_seed`: N/A (perturbation direction pinned, not sampled)
   - `GPU path`: torch.linalg.eigh on GPU; tensor contraction via torch.einsum
8. **Expected output 4-tuple**: `(value=FRAGILITY_MAP_D_I, scheme=W3_H_perturbation_direction, convention=NP_boost_weight, L_max=10)` with closure SHA pinning the O matrix choice.
9. **PASS/FAIL/INFO**:
   - **PASS (=hypothesis confirmed)**: S78-W3-H point (τ=0.537, ε=0.01) reproduces Type I (fragility confirmed); fragility band localizes to τ near 0.537 for ε ≥ 10^−2.
   - **FAIL**: (τ=0.537, ε=0.01) stays Type D; S78-W3-H result unreproducible. Would invalidate the MEMORY.md fragility claim and potentially strengthen block-diagonality as an exact structural theorem.
   - **INFO**: Fragility reproduces but with different band shape than S78 inferred; annotate exact band and localize.
10. **Substitution chain (SIGN/VERIFY)**:
    ```
    Def 1: D_K^(ε) = D_K^canonical + ε · O,   O ∈ Hom(SU(2), C²) off-block-diagonal
    Def 2: Type(τ, ε) = CMPP Petrov type of Weyl tensor of g_M(τ, ε) derived from a_2(D_K^(ε))
    Def 3: Fragility band B_δ = {(τ, ε) : Type(τ, ε) ≠ Type(τ, 0)} ∩ {|ε| < δ}
    Step 1: At ε = 0, Type D on canonical grid (W6-2 PASS expected as prerequisite)
    Step 2: At ε > 0, off-block-diagonal D_K couples SU(2) and C² blocks; breaks block-diagonal trace theorem
    Step 3: Broken block-diagonal ⇒ Weyl tensor acquires bw±2, bw±1 components (Type D condition broken)
    Step 4: Direction: ε > 0 ⇒ Type generically NOT D; Type = I (most generic CMPP type)
    Step 5: Transition is CONTINUOUS in ε but DISCRETE in type-label ⇒ there exists a bifurcation threshold ε_*(τ)
    Conclusion: Fragility is EXPECTED by structural argument; ε_* empirical. S78-W3-H at (0.537, 0.01) is the first localization.
    ```
11. **PASS/FAIL implications**:
    - PASS ⇒ S78-W3-H result reproduced and refined to a (τ, ε) fragility band; MEMORY.md annotation confirmed. Implies Type D is a block-diagonal-structural theorem, not a small-perturbation-robust feature. Strengthens the "block-diagonality = Birkhoff rigidity" structural analog (MEMORY.md).
    - FAIL ⇒ S78-W3-H retraction; Type D is perturbation-robust in the W3-H direction. Would promote block-diagonal fragility to a narrower class of perturbation directions only.
    - INFO ⇒ fragility band re-localized; update MEMORY.md with corrected band shape.
12. **Effort**: 2 agent-hours (script assembly 30 min, GPU run 30 min, boundary fitting 30 min, analysis + memory update 30 min).
13. **Substrate framing**: The "fragility" is a statement about how the **D_K operator's block-diagonal structure** responds to perturbation. Type D is an emergent consequence of block-diagonal D_K via the a_2 coefficient; breaking block-diagonality at the D_K level breaks Type D at the emergent level. The fragility band (τ, ε) is thus a **map of substrate-level block-coupling thresholds** projected onto emergent geometry. This is a diagnostic probe of how robust the "substrate = block-diagonal" structural assumption is under small deformations.

---

## Wave W6 → Wave W7 Decision Point

After W6 completion, the following decision branches feed into the W7 (transit-origin) planning:

- **If W6-2 PASS + W6-7 PASS**: Type D transit-invariance is dense-grid-confirmed AND its fragility band is localized. W7 proceeds with the canonical transit-dynamics gates as planned; no W7 re-scoping needed.
- **If W6-2 PASS + W6-7 FAIL**: Type D is dense-grid-confirmed AND perturbation-robust (unexpected strong result). W7 gates should include a new "Type D is structural, not perturbative" promotion gate. Memory update required.
- **If W6-2 FAIL**: Dense-grid Type-change detected. W7 must reroute: localize the type-change to a specific τ-band before any transit-dynamics computation can rely on the Type D assumption.
- **If W6-3 PASS**: Regulator-conditional ℐ⁺ confirmed. W7 gates that use "asymptotic flatness" must be regulator-indexed. DR3-regulator-successor-tree (W0-4) becomes a structural requirement, not an option.
- **If W6-3 FAIL**: ℐ⁺ regulator-invariant (unexpected strong result). Promote to permanent-results registry. W7 can treat ℐ⁺ as regulator-invariant in all asymptotic analyses.
- **If W6-1 or W6-4 FAIL**: Retraction of the corresponding horizon-analog. W7 must update the causal-structure assumptions of any transit-dynamics gate that relies on the analog.
- **If W6-5 PASS**: Mellin-cone universality confirmed. Supports extending the CC-3 Connes-Moscovici residue computation (W0-11) to the extended-triple family in W7.
- **If W6-6 PASS**: Canonical Penrose-diagram catalog updated. All future sp-origin diagrams reference this updated catalog.

Carry-forward priorities to W7:
1. If W6-7 FAIL: promote block-diagonal Type D robustness to a permanent structural theorem.
2. If W6-3 PASS: index every asymptotic-flatness gate in W7+ with the regulator family.
3. If W6-2 FAIL: add a new W7 gate "localize the τ-band of Type change" before any transit-dynamics work proceeds.

---

## Wave W6 Machinery-Enumeration Pin

Per §0.11 of the plan-discipline rule, the following machinery-parameters are explicitly enumerated and pinned for every W6 gate. This is the PRDR (Pre-Registration Dry-Run) output for W6.

| Gate | L_max | scan_range | step | tolerance | scheme | convention | seed | GPU |
|:-----|------:|:-----------|-----:|:----------|:-------|:-----------|-----:|:----|
| W6-1 | NA | τ ∈ [τ_fold±0.05] | 1e-4 | RATIO 1e-8 | EF null | (+,−,−,−) | 85061 | off |
| W6-2 | NA | τ ∈ [0, 1.70] | 0.01 | ABS 1e-50 | Jensen canonical | CMPP NP | N/A | on |
| W6-3 | 10 | r ∈ [r_fold, 10^6·r_fold] | log-adaptive | ABS 1e-12 | 5-regulator atlas | conf. mostly_minus | N/A | off |
| W6-4 | NA | τ ∈ [0.18, 0.20] | 2e-6 | ABS 1e-14 | Jensen V_tree | (−,+) 2D mod | N/A | off |
| W6-5 | 10 | s ∈ [−4, 3] | 0.01 | RATIO 1%, ABS 1e-10 | CM-1995 zeta | high-to-low s | N/A | off |
| W6-6 | NA | N/A | N/A | THEOREM (boolean) | Penrose skill TikZ | 45° null | N/A | off |
| W6-7 | 10 | (τ,ε) ∈ [0,0.9]×log ε ∈ [0,10] | 0.01 × log | ABS 1e-12 | W3-H perturb dir | CMPP NP | N/A | on |

No gate is PRU-vulnerable: every machinery-parameter is either pinned explicitly, marked N/A with justification, or set via canonical_constants import.

---

## Wave W6 Input-SHA Ledger

| Input file | SHA-256 pin | Used by |
|:-----------|:------------|:--------|
| `computations/canonical_constants.py` | `<computed-at-runtime>` | All W6 gates |
| `sessions/framework/Penrose-Diagrams.md` (S53) | `<computed-at-runtime>` | W6-6 |
| `sessions/archive/session-84/session-84-s5-*-synthesis.md` (W8B-96 analog refs) | `<computed-at-runtime>` | W6-1, W6-4 |
| `.claude/agent-memory/schwarzschild-penrose-geometer/MEMORY.md` | `<computed-at-runtime>` | W6-2, W6-7 (S78-W3-H fragility reference) |
| `researchers/Schwarzschild-Penrose/` (primary sources manifest) | `<computed-at-runtime>` | All W6 gates (re-read at wave start) |
| `.claude/skills/penrose-diagram/SKILL.md` | `<computed-at-runtime>` | W6-6 |
| computation archive S77 τ=1.614 checkpoint metric | `<computed-at-runtime>` | W6-2, W6-6 |

All `<computed-at-runtime>` SHAs are logged in the first 20 lines of the corresponding script's stdout, per §4 of the computation-script template. The closure SHA per gate (computed from the ordered input-pin map) is appended to the canonical verdict line.

---

## W6 compliance self-check

- [x] 7 gate blocks, 13 fields each
- [x] Every gate has machinery pin (PRDR §0.11 compliant)
- [x] Every gate has substitution chain for sign/direction claims
- [x] Every script is prefixed `s85_w6_` and lives in `computations/`
- [x] Verdict file pin: `computations/s85_gate_verdicts.txt` (per .claude/rules/gate-verdicts.md canonical-path rule)
- [x] No cross-wave write (this plan only writes to `sessions/session-plan/session-85-plan-w6.md`)
- [x] Substrate framing applied per gate (FROM substrate TO emergent geometry)
- [x] Full-fidelity prompts (no abbreviation; every gate is self-sufficient)
- [x] No line-count requirement on agent prompts
- [x] Canonical constants imported, never hardcoded
- [x] GPU/CPU policy declared per gate
- [x] Expected-output 4-tuple declared per gate
- [x] PASS/FAIL/INFO implications map constraint-space, not rhetoric

End of Wave W6 plan.
