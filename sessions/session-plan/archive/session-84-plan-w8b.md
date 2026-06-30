# Session 84 Plan — Wave 8b: Schwarzschild-Penrose Causal Audits (6 gates)

## W8b Summary

Wave 8b dispatches six causal-geometric gates (indices 91-96 from §4.I of
`session-84-context.md`) against the `schwarzschild-penrose-geometer` agent.
The theme is **constraint-layer classification + Penrose-gear overlay + mesh
equation stability + dynamical-regime-boundary cross-reference + CMPP Petrov
invariance + gear-censorship**. All six gates share a single question: does the
rank-6 gear-machine (MG-0 Mellin cone + MG-1 τ_fold Jensen-curvature + MG-2 A_F
singleton) generate its outputs through a genuine causal-geometric substrate,
or do the 53 §VII-A + §VII-B identities admit layer double-counting / coordinate
artifacts that a causal audit would surface?

Wave 8b runs in parallel with Wave 8a (gates 85-90, Einstein variational/foundational).
Both waves feed the W9 decision point (gear-machine rank-6 master verification +
formal variational-principle reformulation).

### Wave-level invariants

- **Agent**: schwarzschild-penrose-geometer for all six gates. Gate 92 produces
  a TikZ deliverable via the `/penrose-diagram` skill; the plan pre-registers
  only the overlay construction, not the rendering.
- **Scripts**: `computations/s84_w8b_<slug>.py` with `from canonical_constants import *`
  at top. GPU-optional for these gates (no matrix ≥100×100 expected); default
  to CPU with `OMP_NUM_THREADS=8` cap.
- **Canonical Penrose library**: `sessions/framework/Penrose-Diagrams.md` contains
  the 9 definitive diagrams (modulus-space transit, acoustic horizons, sonic-horizon
  trapping). Gate 92 extends this library — it does not replace it.
- **Sessions/framework cross-refs**: τ_phase_trans=0.537 (S48), τ_DNP=0.285,
  τ_BCS_freeze=0.22, τ_fold=0.190, τ_NEC=1.382, tau_turnaround=1.614 (S77 overshoot).
- **Causal structure primitives**: clock constraint (permanent); BCS-horizon analog
  (sonic-horizon trapping, S70); cosmic-censorship in modulus space (S49 direction-dependent
  singularity; S63 topological censorship π_1(SU(3))=0).

### Wave-level dispatch plan

All six gates independent — dispatch in a single batch of 6 concurrent agents,
respecting the ≤8 concurrent cap. No inter-gate dependencies within W8b. The
W8b → W8a dependency exists only at the W9 synthesis level (both waves needed
for gear-master decision point).

---

## W8b Decision Point Prerequisites

Before dispatching W8b, confirm:

1. **Plan §0.10 PRDR pinned**: every machinery parameter in this wave is named
   in §W8b Machinery-Enumeration Pin below. No floating scan ranges.
2. **Input SHAs precomputed** for the static inputs (canonical_constants.py,
   Penrose-Diagrams.md, permanent-results-registry entries for MG-0/1/2).
   See §W8b Input-SHA Ledger below.
3. **Agent memory loaded**: schwarzschild-penrose-geometer has
   `.claude/agent-memory/schwarzschild-penrose-geometer/MEMORY.md` with the 37+
   closure index (S48 Jensen topology, S49 zones, S69 BCS Petrov invariance,
   S70 acoustic radiative white hole, S76/S77 CMPP transit-invariance).
4. **Skill availability**: `/penrose-diagram` skill resolves at
   `.claude/skills/penrose-diagram/SKILL.md` (required for Gate 92 TikZ output).

---

## §W8b-91. S84-CONSTRAINT-LAYER-AUDIT

### 1. Gate ID
`S84-W8B-91-CONSTRAINT-LAYER-AUDIT`

### 2. Trigger
`[AUDIT]` — re-examining the layer-taxonomy of 53 identities for silent
double-counting. Also `[VERIFY-THEOREM]` for the layer-uniqueness claim.

### 3. Classification
**GEOMETRIC** — the 53 identities are constraints on D_K eigenvalue structure
and Jensen deformation. Layer assignment is a classification of
mathematical-character at the substrate level, upstream of observable projection.

### 4. Hypothesis
The 53 §VII-A + §VII-B identities partition uniquely into exactly five mathematical
layers — **algebraic** (gear-loops, CC-5 propagation, Mellin-moment equalities),
**topological** (π_1(SU(3))=0, KO-dim=6, no-trapped-surfaces), **causal** (clock
constraint, BCS-horizon, sonic-horizon, acoustic white hole), **energetic** (NEC
at τ_NEC=1.382, spectral action monotonicity along Jensen, Weyl curvature
hypothesis), **thermodynamic** (Josephson relation, GGE relic, BCS gap, entropy
monotonicity) — with no row requiring joint assignment for mathematical reasons
distinct from linguistic overlap.

### 5. Pass/Fail/INFO Threshold (ABSOLUTE)
- **PASS**: all 53 identities receive a unique primary layer, with ≤1 row
  flagged "joint-assignment-linguistic" (layer overlap is vocabulary, not math).
- **INFO**: 1-3 rows genuinely require joint assignment from distinct
  mathematical roots (e.g., a thermodynamic-causal composite like sonic-horizon
  entropy). Each such row carries a stated mathematical reason.
- **FAIL**: ≥4 rows admit layer ambiguity → silent double-counting — the "8-layer
  censorship stack" narrative over-counts constraints, inflating apparent framework
  rigidity.

Tolerance rule: ABSOLUTE (count-based), threshold = 3.

### 6. Machinery Pin (PRDR)
- `source_file_A`: `sessions/framework/working-paper-VII-A.md` (extract all A-row identities)
- `source_file_B`: `sessions/framework/working-paper-VII-B.md` (extract all B-row identities)
- `identity_count`: 53 (pre-declared; if source-mined count differs, log discrepancy)
- `layer_taxonomy`: {algebraic, topological, causal, energetic, thermodynamic} (5 layers, ordered)
- `joint_assignment_threshold`: 3 (row-count for INFO boundary)
- `classification_method`: deterministic per-row — each identity tagged by (a)
  mathematical operator class: equality-of-spectral-moments (algebraic),
  homotopy/cohomology (topological), Killing-vector/causal-cone/horizon (causal),
  stress-energy/NEC/monotonicity (energetic), entropy/temperature/free-energy (thermodynamic)
- `audit_mode`: read-only — no modification of §VII-A/B source files
- `scheme`: `canonical-5-layer-v1` (version-pinned)
- `L_max`: N/A
- `random_seed`: N/A (deterministic)
- `GPU path`: not required (classification, no linear algebra)

### 7. Input SHA-256 Pins
- `working-paper-VII-A.md`: `<computed-at-runtime>`
- `working-paper-VII-B.md`: `<computed-at-runtime>`
- `permanent-results-registry.md`: `<computed-at-runtime>`
- `canonical_constants.py`: `<computed-at-runtime>`

### 8. Expected Output 4-tuple
`(value=<unique_count>/<total_count>, scheme=canonical-5-layer-v1, convention=per-row-primary-tag, L_max=N/A)`

Example target: `value=52/53, scheme=canonical-5-layer-v1, convention=per-row-primary-tag, L_max=N/A`

### 9. Substitution Chain (layer-assignment deterministic rule)
```
For each identity row r in §VII-A ∪ §VII-B:
  Step 1: Read operator structure O(r) (what mathematical object equality is asserted).
  Step 2: Classify O(r) by dominant operator class:
    - If O(r) is an equality/inequality of spectral moments a_k, Mellin integrals,
      or propagation exponents p_i:  tag = ALGEBRAIC
    - Else if O(r) invokes π_n(G), K-theory class, KO-dim, or orientability:
      tag = TOPOLOGICAL
    - Else if O(r) references Killing vectors, light-cones, trapped surfaces,
      horizon formation, causal precedence, or conformal boundaries:
      tag = CAUSAL
    - Else if O(r) is a stress-energy / NEC / DEC / SEC condition, or a
      monotonicity statement along a flow parameter with energy interpretation:
      tag = ENERGETIC
    - Else if O(r) references entropy, temperature, free energy, chemical
      potential, condensate/gap, or GGE weights:
      tag = THERMODYNAMIC
    - Else:  tag = UNASSIGNABLE (failure flag)
  Step 3: Check secondary operators — if O(r) admits a second dominant class
    with non-trivial mathematical content (not just linguistic borrow), flag
    as JOINT-r = {primary, secondary}.
  Step 4: Count JOINT-r entries; compare to threshold 3.
```

### 10. What PASSES / What FAILS Mean
- **PASS**: the "8-layer censorship" narrative (see MEMORY.md) is actually a
  5-layer mathematical taxonomy — the extra labels are vocabulary decomposition
  within the 5. Constraint count is honest; no inflation.
- **INFO**: the framework has a small number of genuine composite constraints
  (e.g., sonic-horizon entropy which is CAUSAL+THERMODYNAMIC by construction).
  These are properly composite, not double-counted. The substitution chain
  documents the mathematical source of joint assignment.
- **FAIL**: the framework counts many identities more than once across layers,
  and the apparent rigidity of the constraint stack is a linguistic artifact.
  Any argument that sums "constraints across 8 layers" must be retracted and
  recounted under the deduplicated layer-map. Triggers a §VII-A/B source edit
  with an explicit "primary-layer" column.

---

## §W8b-92. S84-PENROSE-GEAR-OVERLAY

### 1. Gate ID
`S84-W8B-92-PENROSE-GEAR-OVERLAY`

### 2. Trigger
`[VERIFY]` — construction-test: do the 7 T2 meshes place consistently on the
canonical M⁴×SU(3)(τ) modulus-space Penrose diagram?

### 3. Classification
**GEOMETRIC** — the overlay is a geometric annotation of an existing Penrose
diagram. Classification of each mesh as "region-local" (active only in one
causal region) vs "global" (active across horizons) is a property of the mesh
identity evaluated at distinct modulus-space points.

### 4. Hypothesis
The 7 T2 meshes from the Tesla gear-machine workshop (sin²(μ_BC)=3/(3+e^{12τ}),
r_CMB-epsilon_H identity, n_s-epsilon_H identity, F_traj=3/2, balanced-ratio
universality, α_s=n_s²-1, f_L≥0.6027 partition) each assign uniquely to a causal
region of the canonical modulus-space Penrose diagram — no mesh requires
simultaneous evaluation across the BCS-horizon (τ=0.22), the phase-transition
boundary (τ=0.537), or the fold (τ=0.190).

### 5. Pass/Fail/INFO Threshold (ABSOLUTE)
- **PASS**: all 7 meshes place into specific regions {pre-BCS, BCS-trapped,
  post-fold freeze, phase-transition layer, post-phase condensed region, Jensen
  line, modulus origin} without contradictions.
- **INFO**: 1-2 meshes exhibit genuine cross-region structure (e.g., a mesh
  referencing quantities from both pre- and post-fold regions) → global
  character, documented with mathematical reason (e.g., r_CMB is k-CMB observation
  of transit-scale amplitude, genuinely bridging transit horizon and post-fold).
- **FAIL**: ≥3 meshes cannot be placed consistently; the overlay reveals that
  the gear-machine narrative secretly assumes cross-causal-region identities
  that the causal structure forbids.

Tolerance rule: ABSOLUTE (count-based), threshold = 3.

### 6. Machinery Pin (PRDR)
- `canonical_diagram_source`: `sessions/framework/Penrose-Diagrams.md`, diagram
  #5 "M⁴×SU(3)(τ) modulus-space transit" (or the closest-named diagram;
  identify by diagram title match)
- `mesh_list`: 7 entries —
  M1 = sin²(μ_BC)=3/(3+e^{12τ}) (Γ1' cubic-BC locus)
  M2 = r_CMB transfer identity (tensor-to-scalar k-transit to k-CMB)
  M3 = n_s-epsilon_H Jensen-curvature identity
  M4 = F_traj=3/2 trajectory-amplitude ratio (Mellin a_2 slot)
  M5 = balanced-ratio universality (R-protected span ≤1.5)
  M6 = α_s = n_s² - 1 (single-parameter curvature relation)
  M7 = f_L ≥ 0.6027 Leggett-Bogoliubov partition
- `region_enumeration`: pre-BCS (τ>0.22), BCS-trapped (0.19<τ<0.22),
  post-fold freeze (τ=0.19-), phase-transition layer (τ≈0.537), post-phase
  condensed (0.22<τ<0.537), Jensen line (all τ, g_0 embedding), modulus origin (τ=0)
- `region_assignment_method`: evaluate at which τ-values the mesh identity
  is mathematically well-defined / physically active. A mesh is "region-local"
  if its support is entirely within one region; "global" if its evaluation
  requires data from ≥2 regions separated by a horizon/boundary.
- `tikz_output_path`: `figures/penrose/s84-gear-overlay.tex`
- `tikz_skill`: `/penrose-diagram` (invoked in secondary step, not in this gate's
  script)
- `scheme`: `canonical-gear-overlay-v1`
- `L_max`: N/A
- `random_seed`: N/A
- `GPU path`: not required

### 7. Input SHA-256 Pins
- `Penrose-Diagrams.md`: `<computed-at-runtime>`
- `working-paper-gear-machine.md`: `<computed-at-runtime>` (mesh definitions)
- `canonical_constants.py`: `<computed-at-runtime>`

### 8. Expected Output 4-tuple
`(value=<local_count>/<global_count>/<contradiction_count>, scheme=canonical-gear-overlay-v1, convention=region-local-primary, L_max=N/A)`

Example target: `value=5/2/0, scheme=canonical-gear-overlay-v1, convention=region-local-primary, L_max=N/A`

### 9. Substitution Chain (mesh-to-region assignment)
```
For each mesh M_i:
  Step 1: Extract mesh identity equation E_i(τ, spectral data).
  Step 2: Compute support(E_i) = {τ ∈ [0, τ_turnaround] : E_i is non-trivial}.
  Step 3: Cross-reference support(E_i) with region enumeration {R_1, ..., R_7}:
    If support(E_i) ⊆ R_k for some k:  tag = REGION-LOCAL(R_k)
    Else if support(E_i) spans ≥2 regions crossed by a horizon:  tag = GLOBAL
    Else if E_i evaluation yields a contradiction (e.g., identity requires
    pre-BCS data but gear workshop placed it post-fold):  tag = CONTRADICTION
  Step 4: Tally local/global/contradiction counts against thresholds.
```

### 10. What PASSES / What FAILS Mean
- **PASS**: the gear-machine mesh set respects the causal structure. Each mesh
  lives in one region, and the "gear rigidity" claim at τ_fold is a statement
  about co-incidence of 3 meshes at a single τ-point — not an ensemble identity
  hiding cross-region data transport.
- **INFO**: 1-2 meshes legitimately span regions, and these are the observational
  channels (r_CMB by construction; F_traj by construction if it involves amplitude
  at both transit and CMB pivots). The global character is documented, not
  silent.
- **FAIL**: the gear-machine secretly treats cross-region identities as local,
  implying the constraint stack assumes causal-structure violations. Requires
  per-mesh re-derivation with explicit region-transport factors.

Secondary deliverable: `figures/penrose/s84-gear-overlay.tex` — canonical TikZ
source for the annotated Penrose diagram, produced via `/penrose-diagram` skill.
Generation is a separate step AFTER gate verdict posts; the gate itself passes
on the region-classification, not on the TikZ compilation.

---

## §W8b-93. S84-MESH-EQUATION-STABILITY

### 1. Gate ID
`S84-W8B-93-MESH-EQUATION-STABILITY`

### 2. Trigger
`[SIGN]` — sensitivity sign/magnitude claim: if |d τ_fold / d a| is small, the
mesh is robust; if large, the fold is fine-tuned. Also `[VERIFY]` — threshold
numerical comparison.

### 3. Classification
**GEOMETRIC** — the mesh equation sin²(μ_BC)=3/(3+e^{a·τ}) is an identity on the
Jensen-deformed spectral triple; d τ_fold / d a is a derivative in the mesh's
parameter space, measuring whether τ_fold is a structural constant or a
coordinate-sensitive artifact.

### 4. Hypothesis
The cubic-BC mesh exponent a=12 is not fine-tuned: perturbing a by small
Δa shifts τ_fold by O(Δa / 12) — the functional form is robust to the exponent
at leading order, and |d τ_fold / d a|_{a=12} < 0.01 per unit of a, comparable
to or smaller than the sensitivity of τ_fold to Jensen-curvature convexity
(d²S/dτ² = +317863, a factor that the fold value is genuinely tied to).

### 5. Pass/Fail/INFO Threshold (ABSOLUTE)
- **PASS**: |d τ_fold / d a| < 0.01 per unit of a at a=12. Mesh robust — no
  fine-tuning of the exponent.
- **INFO**: 0.01 ≤ |d τ_fold / d a| < 0.1 per unit of a (3-decimal-place
  precision required to reproduce τ_fold=0.190). Mesh stable but borderline —
  structural, but framework users must not claim robustness to large
  exponent-family changes.
- **FAIL**: |d τ_fold / d a| ≥ 0.1 per unit of a (4+ decimal-place precision
  required). Mesh fine-tuned; the cubic-BC functional form is effectively a
  coordinate choice, and alternative BC parametrizations yield different
  τ_fold values outside the published [0.189, 0.191] window.

Tolerance rule: ABSOLUTE (per-unit-a threshold), three-level.

### 6. Machinery Pin (PRDR)
- `mesh_functional`: `sin²(μ_BC) = 3 / (3 + e^{a·τ})`
- `a_center`: 12.0 (canonical)
- `a_scan_range`: [11.0, 13.0]
- `a_step`: 0.1 (21 points)
- `tau_solver`: root-find τ_fold(a) from the joint system
  {Γ1' cubic-BC, Γ5' convex curvature d²S/dτ² = +317863, Γ6 three-band f_L ≥ 0.6027}
- `tau_bracket`: [0.10, 0.30] (matches S84-GEAR-MASTER-CANDIDATE §4.A-6)
- `tau_tolerance`: 1e-8 (root-finder xtol)
- `finite_difference_method`: centered 5-point stencil at a=12
- `sensitivity_cross_check`: compare to |d τ_fold / d (d²S/dτ²)| at nominal
  d²S = +317863 with relative perturbation 1e-4; target same-order magnitude
  as mesh-exponent sensitivity (both should be O(1e-4) to O(1e-2) if fold is
  structural)
- `scheme`: `canonical-mesh-stability-v1`
- `L_max`: N/A (mesh-equation-level, not spectral-truncation)
- `convention`: standard Jensen g_0 with τ_fold root tracked to 1e-8
- `random_seed`: N/A
- `GPU path`: not required (1D root finds, n=21)

### 7. Input SHA-256 Pins
- `canonical_constants.py`: `<computed-at-runtime>`  (τ_fold=0.19, d2S_fold=+317863)
- `permanent-results-registry.md`: `<computed-at-runtime>`  (Γ5' convexity entry)
- Mesh-derivation script (if exists): `<computed-at-runtime>`

### 8. Expected Output 4-tuple
`(value=<|d τ_fold / d a|_{a=12}>, scheme=canonical-mesh-stability-v1, convention=centered-5-pt, L_max=N/A)`

Example target: `value=0.0032, scheme=canonical-mesh-stability-v1, convention=centered-5-pt, L_max=N/A`

### 9. Substitution Chain (derivative chain — [SIGN] requires this)
```
Step 1: Define F(a, τ) = 0 as the joint cubic-BC × convex-curvature × three-band
  system. At a=12, τ_fold=0.190 is the unique root on [0.10, 0.30] per
  S84-ALTERNATIVE-TAU-MESH-UNIQUENESS (§4.L-119).

Step 2: Implicit-function theorem:
  d τ_fold / d a = -(∂F/∂a) / (∂F/∂τ) |_{a=12, τ=0.190}

Step 3: ∂F/∂a includes exp(a·τ)·τ = exp(12·0.190)·0.190 = exp(2.28)·0.190
  ≈ 9.776·0.190 ≈ 1.857  (local to the cubic-BC component)
  ∂F/∂τ includes exp(a·τ)·a = exp(2.28)·12 ≈ 117.3 plus convex-curvature
  contribution d²S/dτ² = +317863 that dominates if the curvature couples directly.

Step 4: Leading-order ratio |d τ_fold / d a| ≈ 1.857 / 117.3 ≈ 0.0158 if
  curvature is weakly coupled at the mesh level; smaller if curvature appears
  directly in the denominator. Threshold test: 0.0158 > 0.01 → would fall in
  INFO band (mesh borderline, not FAIL). Actual computation determines sign.

Step 5: Sign reading — |d τ_fold / d a| is positive-definite (magnitude, not
  signed). Direction of τ_fold shift under a-increase: since τ_fold solves
  sin²(μ_BC)=3/(3+e^{aτ}), increasing a at fixed μ_BC requires decreasing τ.
  Therefore sign(d τ_fold / d a) = negative (larger a → smaller τ_fold).
```

### 10. What PASSES / What FAILS Mean
- **PASS**: the mesh identity is structurally robust. Small changes in the
  "12" in the cubic-BC exponent do not shift τ_fold meaningfully. The claim
  that τ_fold=0.190 is a framework structural constant is supported at the
  mesh-stability level. Adjoin to permanent-results-registry as a stability
  theorem.
- **INFO**: the mesh is stable but not deeply so. 3-decimal-place precision is
  required to reproduce τ_fold=0.190; framework users should quote τ_fold
  as 0.190 ± 0.001, not 0.1900 ± 0.0001. Propagate this uncertainty into
  downstream observables that depend on τ_fold (A_s closure window,
  μ_BC_K3=188.185 GeV, etc.).
- **FAIL**: the mesh exponent is fine-tuned. The "a=12" in the cubic-BC
  parametrization is a coordinate choice whose perturbation at the 1% level
  yields τ_fold shifts >1% — the published fold value is sensitive to a
  functional-form choice without deeper derivation. Triggers DERIV-II
  re-dispatch with explicit derivation of a=12 from rep-theoretic
  decomposition (§4.K-106), or retreat of the "τ_fold structural" claim.

---

## §W8b-94. S84-DYNAMICAL-REGIME-BOUNDARIES-CROSS-REF

### 1. Gate ID
`S84-W8B-94-DYNAMICAL-REGIME-BOUNDARIES-CROSS-REF`

### 2. Trigger
`[AUDIT]` — tracing apparent additional boundaries back to a known generator
class. Also `[VERIFY-THEOREM]` — rank-6 gear-machine preserves its count.

### 3. Classification
**GEOMETRIC** — the four τ-boundaries (τ_phase_trans=0.537, τ_DNP=0.285,
τ_BCS_freeze=0.22, τ_fold=0.190) are critical points of dynamical-regime
transitions. If they all derive from MG-1 (τ_fold Jensen family) + generator
classes C-1..C-6, they are consequences of the rank-6 gear-machine, not
additional independent gears.

### 4. Hypothesis
The four dynamical-regime boundaries are all derivable from MG-1 (τ_fold
Jensen-curvature gear) via a single generator class C-* within the C-1..C-6
enumeration. Specifically:
- τ_phase_trans=0.537 is the C² sectional-curvature sign change (S48) →
  derives from the Jensen-curvature convexity evaluator (C-4 candidate).
- τ_DNP=0.285 is DNP crossing (dynamic nuclear polarization instability) →
  derives from the spectral-gap curvature at the same Jensen family (C-4 or C-5).
- τ_BCS_freeze=0.22 is post-transit freeze threshold → derives from BCS gap
  ↔ Jensen curvature lock (same C-*).
- τ_fold=0.190 is the MG-1 generator itself.

All four therefore consequences of MG-1, no rank increase.

### 5. Pass/Fail/INFO Threshold (ABSOLUTE)
- **PASS**: all 4 boundaries trace to a single generator class C-* (rank 6
  survives).
- **INFO**: 1-2 boundaries require joint derivation from two generator classes
  (e.g., τ_DNP derives from C-4 convexity AND C-5 spectral-gap separately) —
  composite, but still within C-1..C-6.
- **FAIL**: ≥3 boundaries require independent generator classes outside
  C-1..C-6, pushing rank to ≥8. Gear-master rank-6 verification
  (S84-GEAR-MASTER-CANDIDATE §4.A-6) would need revision.

Tolerance rule: ABSOLUTE (boundary-to-generator assignment count).

### 6. Machinery Pin (PRDR)
- `boundary_list`: [τ_phase_trans=0.537, τ_DNP=0.285, τ_BCS_freeze=0.22,
  τ_fold=0.190]
- `boundary_values`: pull from canonical_constants.py (τ_fold=0.19, τ_BCS_freeze
  via Delta_BCS; τ_DNP and τ_phase_trans from MEMORY.md and S48 anchor)
- `generator_classes`: C-1..C-6 (enumerate from gear-machine working paper;
  canonical list: C-1 Mellin cone extremum, C-2 A_F singleton closure, C-3
  Peter-Weyl block-diagonal, C-4 Jensen convexity, C-5 spectral-gap inversion,
  C-6 three-band partition)
- `derivation_test`: for each boundary B_i, attempt derivation τ_B_i = f(C_k,
  Jensen family, canonical inputs). Record minimum C_k set needed for
  closed-form or numerical reproduction within 0.5% of canonical value.
- `single_generator_threshold`: 1 (PASS requires all 4 to have min |C_k set| = 1)
- `joint_threshold`: 2 (INFO allows min |C_k set| ≤ 2)
- `scheme`: `canonical-boundary-trace-v1`
- `L_max`: N/A (boundary-trace level, not spectral-truncation)
- `convention`: MG-1 Jensen g_0 as base; perturb to find boundary via
  signature-change / gap-inversion / phase-transition criterion per boundary type
- `random_seed`: N/A
- `GPU path`: not required

### 7. Input SHA-256 Pins
- `canonical_constants.py`: `<computed-at-runtime>`
- `working-paper-gear-machine.md`: `<computed-at-runtime>` (generator-class enumeration)
- `permanent-results-registry.md`: `<computed-at-runtime>` (τ boundaries + S48 anchor)
- `MEMORY.md` (agent): `<computed-at-runtime>` (for τ_phase_trans=0.537, τ_DNP, τ_BCS_freeze citations)

### 8. Expected Output 4-tuple
`(value=<max_|C_k set|>/4, scheme=canonical-boundary-trace-v1, convention=MG-1-Jensen-base, L_max=N/A)`

Example target: `value=1/4, scheme=canonical-boundary-trace-v1, convention=MG-1-Jensen-base, L_max=N/A`

### 9. Substitution Chain
```
For each boundary τ_B ∈ {0.537, 0.285, 0.22, 0.19}:
  Step 1: Identify the dynamical phenomenon at τ_B:
    τ=0.537:  C² sectional curvature sign change (S48)
    τ=0.285:  DNP crossing
    τ=0.22:   BCS freeze (Delta_BCS crossing threshold)
    τ=0.19:   fold (MG-1 generator, by definition)

  Step 2: Express each in terms of generator-class outputs:
    τ_phase_trans(C-4): solve d sectional_K(τ) / dτ = 0 on Jensen family with
      C-4 convexity tracker; crossings give τ_phase_trans = 0.537.
    τ_DNP(C-5): solve spectral-gap inversion at DNP level; predict 0.285.
    τ_BCS_freeze(C-4 or composite): Delta_BCS(τ) = 0.4642 crosses threshold
      at τ_BCS_freeze = 0.22; this is same Jensen convexity evaluation.
    τ_fold(C-4): d²S/dτ² stationary + convexity-locked minimum; by
      construction MG-1.

  Step 3: Minimum-generator-class count per boundary:
    If each derives from exactly one C_k, max |C_k set| = 1, all 4 derive
    from the same or different single C_k's — both satisfy PASS.
    If a boundary requires joint {C_4, C_5}, |C_k set| = 2 for that one.

  Step 4: Report max |C_k set| across all 4. Threshold:
    max = 1 → PASS  (rank 6 survives)
    max = 2 → INFO  (rank 6 survives with joint-assignment notes)
    max ≥ 3 or |C_k ∪| > {C-1..C-6} → FAIL  (rank 7+)
```

### 10. What PASSES / What FAILS Mean
- **PASS**: the rank-6 gear-machine is genuine. The four boundaries are
  geometrically-implied critical points of the MG-1 Jensen-curvature flow,
  not independent inputs. This supports the gear-master claim (§4.A-6) that
  53 identities ↔ rank-6 machine.
- **INFO**: 1-2 boundaries need joint derivation. Rank 6 survives but the
  gear-machine's simplicity narrative needs refinement: the boundaries are
  composite consequences, and the gear-master table should split them.
- **FAIL**: multiple boundaries are genuine independent generators. Rank ≥ 8.
  The rank-6 gear-master is a reductive projection, not a complete
  classification. This does not invalidate MG-0/1/2 but requires honest
  rank reporting. Triggers a gear-master revision in W9 decision point.

---

## §W8b-95. S84-CMPP-PETROV-TYPE-INVARIANCE

### 1. Gate ID
`S84-W8B-95-CMPP-PETROV-TYPE-INVARIANCE`

### 2. Trigger
`[VERIFY-THEOREM]` — formalizing an existing observation as a theorem-level
claim against the MG-1 output list.

### 3. Classification
**GEOMETRIC** — CMPP (Coley-Milson-Pravda-Pravdová) Petrov classification is a
causal-structure invariant at the 4D effective-spacetime level. "Type D
static, Type G dynamic" across the full transit window [τ=0, τ=1.614] is a
statement about the Weyl-tensor algebraic type of the effective 4D geometry.

### 4. Hypothesis
The CMPP Petrov type is transit-invariant along the MG-1 Jensen family. The
observation from S76 and S77 — static 4D geometry is Type D (non-radiative),
dynamic 4D geometry is Type G (generic, radiative) — extends across the full
modulus-space transit including overshoot (τ=1.614), fold (τ=0.190), phase-transition
(τ=0.537), BCS-freeze (τ=0.22), and modulus origin (τ=0). The invariance is a
consequence of MG-1: the Jensen family preserves product-space topology +
block-diagonal D_K (B2-OFFJ-41 permanent), which forces Ψ_2-only Weyl-spinor
content (Type D) in static and a radiative overlay (Type G) in dynamic.

### 5. Pass/Fail/INFO Threshold (INFO-type, registry update)
- **PASS**: CMPP invariance registered as MG-1 output with causal-structure
  marker "causal-structure invariant (not gear-loop algebraic)". No verdict
  on observational consequence — this is a formal classification landing.
- **INFO** (default): if prior verification (S76/S77) is sufficient evidence,
  mark INFO and land the entry. No new computation required.
- **FAIL**: if cross-check at an additional τ point (e.g., τ_phase_trans=0.537
  or τ_turnaround=1.614) reveals a Petrov-type change, retract the invariance
  claim.

Tolerance rule: THEOREM (registered with classification marker).

### 6. Machinery Pin (PRDR)
- `prior_evidence`: S76 §X CMPP transit-invariant verification (τ ∈ {0.00,
  0.10, 0.19, 0.30, 1.614}; static D, dynamic G); S77 overshoot evaluation
  at τ=1.614
- `new_check_points`: {τ_phase_trans=0.537, τ_DNP=0.285, τ_BCS_freeze=0.22}
  — three additional points not in S76 set
- `computation`: at each new τ, compute 4D effective Weyl spinor Ψ_{ABCD}
  from the reduced M⁴ metric g_M (a_2 Seeley-DeWitt coefficient), classify
  CMPP (static: only Ψ_2; dynamic: Ψ_0..Ψ_4 populated)
- `petrov_classifier`: standard CMPP algorithm (compute CMPP boost-weight
  decomposition of Weyl spinor, identify principal null directions, assign
  type from {O, N, III, D, II, I, G})
- `invariance_criterion`: static-slice type = D at all 7 τ-points (S76 set
  ∪ new check set); dynamic-slice type = G at all 7 τ-points
- `registry_target`: `sessions/framework/permanent-results-registry.md` new
  entry: "MG-1 output list: CMPP Petrov type transit-invariant (static D,
  dynamic G) — causal-structure invariant"
- `scheme`: `canonical-CMPP-invariance-v1`
- `L_max`: N/A (4D effective, derived from spectral truncation at L_max=5
  via a_2)
- `convention`: a_2 = 1/6 R^(4) + higher-derivative terms truncated at
  second-order in curvature
- `random_seed`: N/A (deterministic classification)
- `GPU path`: not required (4D Weyl spinor ops, small)

### 7. Input SHA-256 Pins
- `S76-synthesis.md`: `<computed-at-runtime>` (CMPP transit-invariant section)
- `S77-synthesis.md`: `<computed-at-runtime>` (overshoot τ=1.614 evaluation)
- `canonical_constants.py`: `<computed-at-runtime>`
- `permanent-results-registry.md`: `<computed-at-runtime>`

### 8. Expected Output 4-tuple
`(value=<static_type>/<dynamic_type>/<check_points>, scheme=canonical-CMPP-invariance-v1, convention=a2-reduction-4D, L_max=N/A)`

Example target: `value=D/G/7, scheme=canonical-CMPP-invariance-v1, convention=a2-reduction-4D, L_max=N/A`

### 9. Substitution Chain
```
Step 1: At each τ ∈ {0.00, 0.10, 0.19, 0.22, 0.285, 0.30, 0.537, 1.614}:
  Compute 4D effective metric g_M from a_2 Seeley-DeWitt:
    g_M_μν(τ) = g_0_μν + O(R(τ))

Step 2: Compute Weyl spinor Ψ_{ABCD}(τ) from Riemann decomposition:
    Ψ_{ABCD} = (1/4)[C_{abcd} + i·(*C)_{abcd}]_{AB CD spinor equiv}
  where C is the Weyl tensor.

Step 3: Static slice (Killing vector ∂/∂t timelike, metric τ-independent):
    Only Ψ_2 is non-zero (product-space topology + block-diagonal D_K forces
    all other components to vanish).
    CMPP type: D.

Step 4: Dynamic slice (τ evolving, effective tensor field has time-dependence):
    Ψ_0, Ψ_1, Ψ_3, Ψ_4 pick up contributions from dτ/dt and Jensen-flow
    curvature. All components non-zero.
    CMPP type: G.

Step 5: Invariance check: types must be (D, G) at all 7-9 sample points.
    This is a causal-structure invariant because:
    - Product topology (M⁴ × SU(3)(τ)) is preserved by Jensen deformation.
    - Block-diagonal D_K is preserved (B2-OFFJ-41 permanent).
    - Therefore 4D effective Weyl spinor content is stable.
```

### 10. What PASSES / What FAILS Mean
- **PASS/INFO**: registry entry added. MG-1 Jensen family has a new output
  property — CMPP Petrov type transit-invariance. This is a causal-structure
  invariant (does not appear in gear-loop algebraic identities), so it should
  be tagged distinctly in the gear-master output list. Future reviewers can
  cite this as a non-algebraic consequence of MG-1.
- **FAIL**: if the 3 new check points (τ ∈ {0.22, 0.285, 0.537}) reveal a
  Petrov-type change, the S76/S77 claim of transit-invariance is refuted
  at those points. This would trigger a re-audit of MG-1 output list —
  invariance claim is LOCAL (limited to S76 interval) rather than transit-wide.

---

## §W8b-96. S84-GEAR-CENSORSHIP

### 1. Gate ID
`S84-W8B-96-GEAR-CENSORSHIP`

### 2. Trigger
`[VERIFY-THEOREM]` — evaluating whether an algebraic rigidity has a
cosmic-censorship analog. Also `[AUDIT]` — distinguishing algebraic incompatibility
from causal censorship.

### 3. Classification
**GEOMETRIC** — cosmic-censorship analogs are causal-structure statements. The
question is whether the algebraic uniqueness of τ_fold=0.190 as the closure of
(Γ1' ∧ Γ5' ∧ Γ6) on [0.10, 0.30] has an analog causal-structure statement
("perturbations off τ_fold are censored from observational access"), or whether
the uniqueness is purely algebraic (perturbations off τ_fold are simply
inconsistent with the identity set — no causal-censorship).

### 4. Hypothesis
The gear-rigidity at τ_fold=0.190 has a cosmic-censorship analog: perturbations
δτ that move the modulus off 0.190 are hidden from the effective 4D observer
by the BCS horizon (τ_BCS_freeze=0.22), which causally disconnects post-fold
observation from the pre-fold (transit / supersonic) modulus configurations.
The analog runs parallel to the acoustic-white-hole interpretation (S70): the
fold is the analog of an extremal horizon (κ=0, T_H=0), and δτ-perturbations
during/after transit cannot be probed by post-fold 4D observers.

### 5. Pass/Fail/INFO Threshold (THEOREM-type)
- **PASS**: formal censorship statement — "any perturbation δτ that displaces
  τ from 0.190 during or after the BCS freeze is causally inaccessible to
  post-fold 4D observers" — admits a proof via (a) acoustic-white-hole analog
  argument (pre/post-transit causally disconnected by supersonic flow), or
  (b) extremal-horizon κ=0 analog at the BCS freeze. The gear-rigidity is
  both algebraic and causal.
- **INFO**: gear-rigidity and causal-censorship are independent: the algebraic
  uniqueness holds but perturbations are detectable in principle via secondary
  channels (pre-fold imprints in GGE relic, Leggett modes). Neither negates
  the other.
- **FAIL**: the algebraic uniqueness of τ_fold is a coordinate artifact —
  change of Jensen parametrization yields a different τ_fold value, and the
  "0.190" specificity is conventional. The rigidity claim must be retracted
  or re-phrased.

Tolerance rule: THEOREM-type (formal argument with explicit analog structure).

### 6. Machinery Pin (PRDR)
- `uniqueness_claim_source`: S83 W1-8 R3.3 "τ_fold=0.190 is UNIQUE closure of
  (Γ1' ∧ Γ5' ∧ Γ6) on [0.10, 0.30]" with residual Γ1' 0.134%
  (cross-reference §4.L-119 S84-ALTERNATIVE-TAU-MESH-UNIQUENESS)
- `censorship_analog_candidates`:
  - A. Acoustic-white-hole pre/post-causal disconnection (S70)
  - B. Extremal-horizon κ=0 at BCS freeze (MEMORY.md: "Dump = extremal horizon
    (kappa=0, T_H=0)")
  - C. Topological censorship π_1(SU(3))=0 (S60)
  - D. Seven-layer censorship stack (MEMORY.md: energy + friction + no-trapped +
    Josephson + frag + 1-loop + topological)
- `argument_requirements`: for PASS, at least one analog admits a formal
  statement (mathematical or physical) linking gear-rigidity to causal-observer
  inaccessibility. Identify which of A-D supplies the argument; carry the
  explicit substitution chain.
- `coordinate_artifact_test`: change Jensen parametrization τ → f(τ) for
  monotone f; check whether uniqueness survives (support for PASS/INFO) or
  collapses (FAIL, coordinate artifact).
- `scheme`: `canonical-gear-censorship-v1`
- `L_max`: N/A (classification/argument-level)
- `convention`: MG-1 Jensen family as base; monotone reparametrizations tested
- `random_seed`: N/A
- `GPU path`: not required

### 7. Input SHA-256 Pins
- `S70-synthesis.md`: `<computed-at-runtime>` (acoustic-white-hole, extremal-horizon)
- `S60-synthesis.md`: `<computed-at-runtime>` (topological censorship π_1(SU(3))=0)
- `S83-W1-8-synthesis.md`: `<computed-at-runtime>` (R3.3 uniqueness claim)
- `MEMORY.md` (agent): `<computed-at-runtime>` (seven-layer censorship stack)
- `permanent-results-registry.md`: `<computed-at-runtime>`

### 8. Expected Output 4-tuple
`(value=<PASS_analog_set>/<INFO_flag>/<FAIL_coord_flag>, scheme=canonical-gear-censorship-v1, convention=MG-1-base, L_max=N/A)`

Example target: `value={A,B}/0/0, scheme=canonical-gear-censorship-v1, convention=MG-1-base, L_max=N/A`

### 9. Substitution Chain
```
Step 1: State uniqueness claim:
    U: τ_fold=0.190 is the unique solution on [0.10, 0.30] to
       (Γ1' cubic-BC) ∧ (Γ5' d²S/dτ²=+317863 convexity) ∧ (Γ6 f_L≥0.6027).

Step 2: Coordinate-artifact test:
    Let τ' = g(τ) for monotone g (smooth, bijective on [0, 2]). Under τ',
    the identity set (Γ1', Γ5', Γ6) transforms covariantly (substitute
    τ = g^{-1}(τ')). The unique fixed point is τ'_fold = g(0.190).
    Since g is bijective and the identity set is covariant, uniqueness
    survives: τ'_fold is unique under the transformed identity set.
    → NOT a coordinate artifact. Rules out FAIL.

Step 3: Causal-analog test A (acoustic white hole):
    Pre-fold supersonic transit (Ma=331, Re=0, S72) creates causal
    disconnection between pre-fold modulus configurations (including
    perturbed δτ≠0) and post-fold 4D observers. Post-fold observers
    see only the frozen τ_fold=0.190 value via BCS gap Δ_BCS=0.4642.
    Therefore: δτ perturbations during transit are causally inaccessible
    to post-fold observation.

Step 4: Causal-analog test B (extremal-horizon at BCS freeze):
    At τ_BCS_freeze=0.22, the BCS gap reaches Δ_BCS=0.4642 with surface
    gravity κ → 0 (extremal, T_H=0, S(0)=0). The freeze layer is an
    extremal-horizon analog: causally prevents trans-freeze observational
    access. δτ perturbations with τ_pert > 0.22 cannot communicate with
    τ_fold < 0.22 post-freeze observers.

Step 5: Combine: steps 3-4 provide the analog. Gear-rigidity algebraic
    uniqueness is paired with causal inaccessibility of perturbations.
    Formal statement:
        "Any δτ perturbation moving τ off 0.190 during or after the BCS
         freeze is hidden from post-fold 4D observers by the combined
         acoustic-white-hole (transit) + extremal-horizon (freeze) causal
         structure."

Step 6: Report analog set. If {A, B} both supply arguments → PASS.
    If neither A nor B succeeds but algebraic uniqueness holds → INFO.
    If coordinate-artifact test failed → FAIL.
```

### 10. What PASSES / What FAILS Mean
- **PASS**: the gear-rigidity at τ_fold has a bona fide cosmic-censorship
  analog. Perturbations off 0.190 are causally hidden from post-fold
  observers. This upgrades the gear-master rigidity from "algebraic uniqueness"
  to "causally censored rigidity" — a stronger claim that aligns gear-machine
  with the broader causal-structure substrate. Register in
  permanent-results-registry as a theorem linking MG-1 algebraic uniqueness
  to the seven-layer censorship stack.
- **INFO**: the two types of rigidity are independent. Gear-rigidity is
  algebraic; causal-censorship is a separate structure. Framework users must
  not conflate "unique closure" with "causally isolated" — the claim is
  purely algebraic.
- **FAIL**: the "uniqueness on [0.10, 0.30]" is coordinate-sensitive. Under
  alternative Jensen parametrizations, different τ-values solve the transformed
  identity set, and the 0.190 specificity is conventional. Triggers retraction
  of the uniqueness claim in S83 W1-8 R3.3 and a broader re-examination of
  alternative-parametrization sensitivity (§4.L-119 must be re-scoped).

---

## W8b → W8a Parallel Dispatch Note

W8b and W8a (Einstein variational/foundational, gates 85-90) are independent.
Both run in parallel as single-wave batches of 6 agents each, concurrent cap
respected (12 total < cap permits 8 concurrent per batch; stagger batches
if strict ≤8 needed).

No W8b gate depends on any W8a gate within the current session. Cross-wave
products are synthesized at the W9 decision point only.

---

## W8b → W9 Decision Point (joint with W8a)

The W9 decision point is:

**S84-GEAR-MASTER-CANDIDATE (§4.A-6, rank-6 verification)** —
**S84-VARIATIONAL-PRINCIPLE-REFORMULATION (§4.H-90)**

### W8b contributes to W9:

1. **Gate 91 (CONSTRAINT-LAYER-AUDIT) → gear-master**: whether the 53
   identities truly partition into 5 mathematical layers (supports rank-6
   with honest layer accounting) or inflate via double-counting (rank-6
   unsupported by current layer bookkeeping).

2. **Gate 92 (PENROSE-GEAR-OVERLAY) → variational-principle**: whether the
   7 T2 meshes respect the causal structure (supports the claim that
   gear-outputs are compatible with the canonical Penrose diagram of the
   modulus-space transit).

3. **Gate 93 (MESH-EQUATION-STABILITY) → gear-master Γ1' anchor**: whether
   the cubic-BC exponent a=12 is structural (supports Γ1' as a genuine
   mesh) or fine-tuned (weakens Γ1' and hence the uniqueness claim at τ_fold).

4. **Gate 94 (DYNAMICAL-REGIME-BOUNDARIES-CROSS-REF) → rank-6**: whether
   the four τ-boundaries derive from C-1..C-6 (rank 6 survives) or push
   to rank ≥8.

5. **Gate 95 (CMPP-PETROV-INVARIANCE) → MG-1 output list**: adds a
   causal-structure-invariant entry distinct from gear-loop algebraic
   identities, expanding the gear-master output list typology.

6. **Gate 96 (GEAR-CENSORSHIP) → formal censorship linkage**: links
   algebraic gear-rigidity to the seven-layer censorship stack, upgrading
   MG-1 from algebraic to algebraic+causal.

### W9 decision criterion (joint with W8a)

- Rank-6 gear-master VERIFIED iff: W8b-91 PASS or INFO, W8b-94 PASS,
  W8b-95 PASS (registry landing), W8b-96 PASS or INFO, and W8a gates
  (especially S84-MELLIN-CONE-THEOREM-UNIVERSALITY, S84-VARIATIONAL-PRINCIPLE-REFORMULATION)
  produce the ONE variational-principle statement.
- Rank-6 REFINED (rank-7 or layer-split) iff: W8b-94 INFO/FAIL, or W8b-91
  FAIL with ≥4 double-counted rows.
- Gear-master RETRACTED iff: W8b-93 FAIL (Γ1' mesh fine-tuned) AND W8b-96
  FAIL (coordinate artifact).

---

## W8b Machinery-Enumeration Pin (§0.11)

Every W8b gate's free parameters enumerated and pinned:

| Gate | Free Parameters | Pinned Value / Range |
|:-----|:----------------|:---------------------|
| 91 | `layer_taxonomy` | {algebraic, topological, causal, energetic, thermodynamic} (fixed 5-layer) |
| 91 | `joint_assignment_threshold` | 3 |
| 91 | `identity_count` | 53 (verify at source-mining; log discrepancy) |
| 92 | `canonical_diagram_source` | `sessions/framework/Penrose-Diagrams.md` diagram #5 (or title-matched) |
| 92 | `mesh_list` | 7 meshes {M1..M7} (enumerated in gate §6) |
| 92 | `region_enumeration` | 7 regions (enumerated in gate §6) |
| 92 | `tikz_output_path` | `figures/penrose/s84-gear-overlay.tex` |
| 93 | `a_center` | 12.0 |
| 93 | `a_scan_range` | [11.0, 13.0] |
| 93 | `a_step` | 0.1 (21 points) |
| 93 | `tau_tolerance` | 1e-8 |
| 93 | `finite_difference_method` | centered 5-point stencil at a=12 |
| 93 | `tau_bracket` | [0.10, 0.30] |
| 94 | `boundary_list` | [0.537, 0.285, 0.22, 0.19] |
| 94 | `generator_classes` | {C-1, C-2, C-3, C-4, C-5, C-6} (rank-6 canonical) |
| 94 | `single_generator_threshold` | 1 |
| 94 | `joint_threshold` | 2 |
| 95 | `new_check_points` | {0.537, 0.285, 0.22} (adding to S76 set) |
| 95 | `petrov_classifier` | CMPP standard algorithm |
| 95 | `a2_reduction_order` | 2 (Seeley-DeWitt truncation) |
| 96 | `uniqueness_claim_source` | S83 W1-8 R3.3 on [0.10, 0.30] |
| 96 | `censorship_analog_candidates` | {A: acoustic-WH, B: extremal-κ=0, C: topological-π_1, D: seven-layer-stack} |
| 96 | `coordinate_artifact_test` | monotone-reparam family τ' = g(τ), g bijective on [0, 2] |

All gate scripts MUST log these pins in the first 20 lines of stdout.

---

## W8b Input-SHA Ledger

Static inputs (hashes computed at dispatch time and logged):

| File | Note |
|:-----|:-----|
| `sessions/framework/working-paper-VII-A.md` | Source for Gate 91 identity mining |
| `sessions/framework/working-paper-VII-B.md` | Source for Gate 91 identity mining |
| `sessions/framework/Penrose-Diagrams.md` | Canonical diagram for Gate 92 |
| `sessions/framework/working-paper-gear-machine.md` | Generator-class enumeration (Gates 92, 94) |
| `sessions/framework/permanent-results-registry.md` | Pre-existing theorem ledger (Gates 91, 94, 95, 96) |
| `canonical_constants.py` | All gates (τ_fold=0.19, d2S_fold, Delta_BCS=0.4642, phi_paasch, etc.) |
| `.claude/agent-memory/schwarzschild-penrose-geometer/MEMORY.md` | Context (Gates 94, 96) |
| S76 synthesis | CMPP baseline (Gate 95) |
| S77 synthesis | Overshoot/turnaround (Gate 95) |
| S70 synthesis | Acoustic white hole, extremal horizon (Gate 96) |
| S60 synthesis | Topological censorship π_1(SU(3))=0 (Gate 96) |
| S83 W1-8 synthesis | R3.3 uniqueness claim (Gate 96) |
| S48 synthesis | Phase-transition τ=0.537 anchor (Gate 94) |

Each gate's script computes SHA-256 of exactly the files it reads and emits
the ordered input-pin map in the first 20 lines, closing with the full
64-char hexdigest per `.claude/rules/gate-verdicts.md`.

S84+ dual-SHA: each verdict line carries both `audit_sha256=<>` and
`content_sha256=<>` per S83-G55 FAIL carry-forward (W1-CF-SHA-SPLIT §4.J-99).

---

*End of Wave 8b plan. Six gates pre-registered. Dispatch target: single-batch
of 6 `schwarzschild-penrose-geometer` agents, concurrent with W8a.*
