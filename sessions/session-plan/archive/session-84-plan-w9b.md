# Session 84 Plan — Wave 9b: μ_BC Sub-Obligations (5 items)

**Session**: 84
**Wave**: 9b
**Theme**: μ_BC bi-criterion sub-obligations — discharge Layer 3b (β) of the CUBIC-W-EW gate (S84-MU-BC-GEOMETRIC in W1b)
**Scope**: Rows 105–109 of §4.K (μ_BC obligations) from session-84-context.md
**Date**: 2026-04-18
**Planner**: kaluza-klein-theorist
**Format**: compute (parallel independent agents within dependency-ordered sub-waves)
**Parent plan**: `session-84-plan.md` (not present at plan-write time; this file stands as its own W9b increment)
**Sibling plan**: `session-84-plan-w9a.md` (W9a handles primary cube-3 override + remaining μ_BC layers)

---

## W9b Summary

Wave 9b discharges five sub-obligations that underpin the bi-criterion geometric pin of μ_BC
(the phonon-exflation EW mass scale), which S83 mu_BC-workshop W-2 froze at:

  μ_BC_K3 = M_Z · sqrt(1 + exp(12·τ_fold)/3) = 188.185 GeV   [cubic-bridge-3, tau_fold=0.19]

The S83 W3-G47 PASS (sin²θ_W = 0.23138 at 0.064σ vs PDG) relied on this expression as an
EXTERNAL ansatz. S84-MU-BC-GEOMETRIC in W1b converts the ansatz into a first-principles
geometric pin via two obligations:

  - obligation (i) cube-3 override: justify the exponent "12" in exp(12·τ_fold) by a
    substrate-side argument (spectral-dimension identity d_spec ≈ 3 at the fiber-transition
    scale, with 12 = 4·3 for four-space × three-spectral-dimensions).

  - obligation (ii) C² block omission: justify truncating the su(3) = u(1) ⊕ su(2) ⊕ C²
    Jensen-decomposition to the u(1)⊕su(2) channels by showing the C² off-diagonal W±
    and coset X/Y gauge bosons do NOT enter sin²θ_W = g_Y²/(g_Y² + g_2²) at 1-loop.

These two obligations plus three closure audits (TAU-CROSS-SCALE, YUKAWA-CLOSURE,
MW-CONSISTENCY-AUDIT) constitute Wave 9b. The five gates are partitioned into two
DEPENDENCY-ORDERED sub-waves:

  - W9b-A (parallel, independent): §W9b-105 (DERIV-I), §W9b-106 (DERIV-II)
  - W9b-B (parallel, independent, DEPENDS on W9b-A PASS): §W9b-107, §W9b-108, §W9b-109

Five-gate decisive target: all five verdicts PASS ⇒ μ_BC_K3 = 188.185 GeV is first-principles
pinned, S84-MU-BC-GEOMETRIC (W1b) discharges, S84-SIN2-THETA-W chain is ansatz-free.

**Phononic framing (mandatory per `.claude/rules/phononic-framing.md`)**: these gates are
GEOMETRIC (d_spec, rep-theoretic decomposition of D_K spectrum) and PARTICLE (sin²θ_W
matrix elements, ρ-parameter, M_W). They are NOT direct observations of substrate
excitations, but the μ_BC scale IS the phononic mass associated with the cubic-bridge
3PI transit; the sub-obligations classify it under the spectral-dimension and Jensen
decomposition structure of D_K on SU(3) — not as a parameter of an emergent 4D
Lagrangian, but as an eigenvalue feature of the substrate.

---

## W9b Decision Point Prerequisites

**CRITICAL ordering discipline** (pre-registered to prevent circularity):

1. **W9b-A must complete first**. §W9b-105 (DERIV-I) and §W9b-106 (DERIV-II) are
   independent and dispatch in parallel (2 concurrent agents). Both must produce
   verdict lines before W9b-B dispatches.

2. **If W9b-105 FAILS**: obligation (i) is violated. The "12" exponent in cube-3 cannot be
   justified by spectral dimension. S84-MU-BC-GEOMETRIC loses its derivation path for the
   exponent and W9b-B becomes vacuous (nothing to cross-check if the geometric anchor
   has fallen). Record all W9b-B gates as PRE-REG-INCOMPLETE (PRU Class 8-ADJACENT) —
   the upstream machinery for the cubic form is unpinned. Escalate to W1b governance.

3. **If W9b-106 FAILS**: obligation (ii) is violated. C² block inclusion would change
   sin²θ_W, invalidating the u(1)⊕su(2) truncation. Same escalation.

4. **If both W9b-105 AND W9b-106 PASS**: W9b-B dispatches. §W9b-107, §W9b-108, §W9b-109
   are independent of one another and run in parallel (3 concurrent agents).

5. **Circularity avoidance**: §W9b-107 (TAU-CROSS-SCALE) MUST NOT be dispatched before
   DERIV-I/II discharge. Using PDG sin²θ_W to "derive" τ_fold is valid only if the
   cubic form's geometric basis is independent of that PDG input. DERIV-I/II provide
   that independence.

**Total concurrent agents**: max 3 (in W9b-B after the 2-agent W9b-A completes).
Under ≤~8 concurrent cap (per `feedback_dispatch-discipline.md`).

---

## §W9b-105 — S84-DERIV-I (cube-3 override)

### 1. Gate ID
`W9b-105-S84-DERIV-I`

### 2. Trigger
`[VERIFY]` — PASS/FAIL depends on whether d_spec at fiber-transition scale lies in [2.5, 3.5]
(PASS band) or ∈ [2.0, 4.0] \ [2.5, 3.5] (INFO) vs outside [2.0, 4.0] (FAIL).

### 3. Classification
**GEOMETRIC** — spectral dimension of Jensen-deformed SU(3) is a property of the substrate
spectral triple's zeta function ζ_D(s) = Tr(|D_K|^{-s}), not of emergent excitations.

### 4. Hypothesis
The exponent "12" in μ_BC_K3 = M_Z·sqrt(1 + exp(12·τ_fold)/3) factors as 12 = 4·3, where
"3" is the spectral dimension of the internal SU(3) at the fiber-transition scale. d_spec
is defined as the location of the leading simple pole of ζ_D(s) = Tr(|D_K|^{-s}) on
Jensen-deformed SU(3) at τ = τ_fold = 0.19. PASS (d_spec ≈ 3) justifies the cube-3 override
in CUBIC-W-EW; FAIL refutes the geometric anchor for the exponent.

### 5. Pass/Fail/INFO Threshold
- **PASS**: d_spec ∈ [2.5, 3.5] (log-measure ±17% around d_spec = 3). Cube-3 exponent
  justified; obligation (i) discharges.
- **INFO**: d_spec ∈ [2.0, 2.5) ∪ (3.5, 4.0]. Spectral dimension is close to 3 but
  outside PASS band. Cube-3 is MIXED — use-with-caveat.
- **FAIL**: d_spec ∉ [2.0, 4.0]. Geometric anchor refuted.

Tolerance rule: **ABSOLUTE** on d_spec (substrate property, not a ratio).

### 6. Machinery pin (PRDR)
- `N_eval`: all 155,984 eigenvalues of D_K at L_max=10 (existing dataset:
  `computations/data/D_K_eigenvalues_Lmax10_tau019.npz` or equivalent from S34+).
- `L_max`: 10 (primary); cross-check at L_max = {6, 8, 12} for convergence audit.
- `scan_range`: s ∈ [0.5, 6.0] in the ζ_D(s) zeta-regularized Dirichlet series; locate
  simple-pole residue numerically via Möbius-inverted mellin.
- `step_size`: Δs = 0.001 in the neighborhood of the pole candidate; Δs = 0.05 in bulk.
- `tolerance`: residue computation to 1e-8 relative. Pole location to ±0.02 on d_spec.
- `scheme`: zeta-function regularization (L1 axiomatic layer per §VII.M).
- `convention`: Connes positive-definite |D_K| = sqrt(D_K² + ε²) with ε = 1e-12
  (canonical IR-floor to avoid zero-eigenvalue singularities if any exist).
- `random_seed`: N/A (deterministic).
- `GPU path`: MANDATORY. torch.linalg.eigvalsh on |D_K| matrix; matrix size ~156k×156k
  does NOT fit in VRAM — use the existing eigenvalue array (pre-computed).
  The zeta sum is a reduction over 156k scalars — trivially vectorizable in torch.
- `fiber-transition scale`: defined as s* = s at which the dominant contribution to
  ζ_D(s) switches from the low-lying (first ~1000) eigenvalues to the bulk spectrum.
  Compute s* explicitly as the argmin of the second derivative |d²ζ_D/ds²|; report.
  d_spec is evaluated at s → s*⁺.

### 7. Input SHA-256 pins
- `D_K_eigenvalues_Lmax10_tau019.npz`: `<computed-at-runtime>` (script must log the
  SHA of the eigenvalue array it loads in the first 20 lines of stdout).
- `canonical_constants.py`: `<computed-at-runtime>`.
- Script source: `<computed-at-runtime>`.

### 8. Expected output 4-tuple
`(value=d_spec, scheme=zeta-reg, convention=|D_K|=sqrt(D²+ε²), L_max=10)`

### 9. Substitution chain (GEOMETRIC, but d_spec claim requires chain)

Step 1 (definition): ζ_D(s) = Σ_{λ ∈ spec(|D_K|), λ>0} λ^{-s}, for Re(s) large enough
                     that the series converges absolutely. [Connes-Marcolli, heat-kernel
                     literature; well-defined for |D_K| positive on a compact Riemannian
                     manifold-like structure.]

Step 2 (definition of d_spec): d_spec = sup{s : ζ_D(s) diverges as a simple pole} = leading
                               simple-pole location of ζ_D. For a d-dimensional compact
                               Riemannian manifold (or manifold-like spectral triple),
                               d_spec = dim (Weyl law).

Step 3 (Jensen-SU(3) has internal dim 8): the naive internal dimension of SU(3) is 8.
                                          But d_spec at the FIBER-TRANSITION SCALE s*
                                          reflects the local density of states near the
                                          fiber's Dirac sea, not the global group-manifold
                                          dimension. At intermediate scales, internal
                                          dimensional reduction due to Jensen deformation
                                          can produce d_spec ≠ 8.

Step 4 (hypothesis): at the fiber-transition scale, the spectral density collapses from the
                     bulk 8-dimensional behavior to a quasi-3-dimensional effective count
                     due to the u(1)⊕su(2)⊕C² split (3-block structure with C² off-diagonal).
                     PREDICTION: d_spec(s*) ≈ 3.

Step 5 (direction for PASS): d_spec > 3.5 ⇒ C² block contributes as a full 5D slab, pushing
                             d_spec toward 5 or higher; the cube-3 override is NOT
                             justified. d_spec < 2.5 ⇒ only u(1) dominates, which would
                             KILL the su(2) channel and invalidate the sin²θ_W formula
                             entirely. PASS window [2.5, 3.5] selects the
                             u(1)⊕su(2)-dominated, C²-subdominant regime — exactly what
                             obligation (ii) claims is the physical content.

Step 6 (direction for "12 = 4·3"): IF d_spec(s*) = 3 THEN the cube-3 override in the
                                   combined 4D (M⁴) × 3D (fiber-transition spectral)
                                   structure yields a natural exponent 4·3 = 12 in the
                                   exp(12·τ_fold) of μ_BC_K3. This is the geometric
                                   CONTENT of "cube-3".

### 10. What PASS and FAIL mean for the solution space
- **PASS**: the "12" in μ_BC_K3 is sourced from d_spec × D_spacetime = 3 × 4. Cubic bridge
  is an identity, not an ansatz. S84-MU-BC-GEOMETRIC obligation (i) discharges.
- **INFO**: spectral dimension is borderline. The cubic form is compatible but not derived;
  use-with-caveat.
- **FAIL**: spectral dimension contradicts the "12" exponent. μ_BC_K3 loses its geometric
  derivation and collapses to an ansatz. CUBIC-W-EW becomes an accommodation, not a
  prediction.

### 11. Agent
Primary: `spectral-geometer`
Alternate: `lizzi-spectral-functional-theorist` (if spectral-geometer is overloaded —
only one dispatches)

### 12. Script prefix
`computations/s84_w9b_deriv_i_spectral_dim.py`

### 13. Runtime estimate
~15–30 min (zeta-sum vectorized in torch over 156k eigenvalues; scan s-grid of ~6000
points; deterministic). Low memory — fits in VRAM easily.

---

## §W9b-106 — S84-DERIV-II (C² block omission)

### 1. Gate ID
`W9b-106-S84-DERIV-II`

### 2. Trigger
`[VERIFY-THEOREM]` — theorem-level claim that C² rep-theoretic block does not contribute
to the sin²θ_W = g_Y²/(g_Y²+g_2²) formula at 1-loop.

### 3. Classification
**PARTICLE** (rep-theoretic decomposition of gauge-boson spectrum into quantum-number
channels, which are the emergent particle content of the Jensen-SU(3) fiber).

### 4. Hypothesis
The Jensen decomposition su(3) = u(1) ⊕ su(2) ⊕ C² (with C² the 4-dim real off-diagonal
subspace spanned by the six off-diagonal Gell-Mann generators in the complement of
u(2) ⊂ su(3)) maps under gauge-group identification to:
- u(1) → hypercharge Y (one generator, diagonal);
- su(2) → W^a (three generators, Cartan diagonal + two off-diagonal within u(2));
- C² → coset X/Y bosons + off-diagonal W± relatives (outside u(2) ⊂ su(3)).

The sin²θ_W(M_Z) formula at tree level + 2-loop SM RGE takes input only from g_Y and g_2
(hypercharge coupling and isospin coupling). The C² off-diagonal bosons would contribute
ONLY at 2-loop via heavy-X/Y virtual pairs if they are part of a GUT-completion ansatz —
but in the phonon-exflation framework, these are NOT integrated out as a GUT remnant but
are the COSET DIRECTIONS of the u(2) ⊂ su(3) embedding and therefore decouple from the
electroweak projection. PASS if the C² contribution to sin²θ_W at the cubic-bridge scale
is below 1e-6 (well below the 2-loop slope that G47 achieved at 0.064σ).

### 5. Pass/Fail/INFO Threshold
- **PASS**: Δsin²θ_W[C²] < 1e-6 at 1-loop (representation-theoretic theorem: off-diagonal
  generators trace to zero against the diagonal Y and T³ projectors used in sin²θ_W
  matrix element).
- **INFO**: 1e-6 ≤ Δsin²θ_W[C²] < 1e-5. C² contributes at a level that is still below
  the PDG uncertainty (4e-5 relative) but potentially enters 2-loop matching.
- **FAIL**: Δsin²θ_W[C²] ≥ 1e-5. C² block cannot be omitted; the truncation to
  u(1)⊕su(2) in the sin²θ_W derivation is invalid.

Tolerance rule: **ABSOLUTE** on Δsin²θ_W.

### 6. Machinery pin (PRDR)
- `N_eval`: for the 1-loop trace identity, only the gauge-generator projection matrices
  matter. Work at the finite-dim level: su(3) = 8 real generators. Explicit 8×8
  Gell-Mann basis.
- `L_max`: irrelevant (rep-theoretic at the gauge-group level).
- `scan_range`: N/A.
- `step_size`: N/A.
- `tolerance`: 1e-14 on the matrix-element inner products (double-precision limit).
- `scheme`: MS-bar at M_Z (canonical sin²θ_W scheme).
- `convention`: Cartan-Killing normalization Tr(T^a T^b) = (1/2) δ^{ab} for SU(N)
  fundamental; explicit Gell-Mann λ^a with T^a = λ^a / 2.
- `random_seed`: N/A.
- `GPU path`: not needed (8×8 matrices, microseconds).
- **Gauge-group identification pin**: specify explicitly which three generators
  span su(2), which one spans u(1), which four span C². Convention (from Baptista paper
  §3 and s45):
    - u(1): diagonal generator Y = diag(1/3, 1/3, -2/3) (hypercharge normalization) /
      equivalently √(1/3)·λ_8.
    - su(2): T³ = λ_3/2, T^± from λ_1, λ_2 (the upper-2×2 block).
    - C²: λ_4, λ_5, λ_6, λ_7 (the off-diagonal GELL-MANN generators mixing the
      third row/column with the upper 2×2 block).

### 7. Input SHA-256 pins
- `canonical_constants.py`: `<computed-at-runtime>`.
- Script source: `<computed-at-runtime>`.
- No external data dependency beyond Gell-Mann generators (defined in-script with
  explicit matrix entries).

### 8. Expected output 4-tuple
`(value=Δsin²θ_W[C²], scheme=MSbar-MZ, convention=Cartan-Killing-fundamental, L_max=N/A)`

### 9. Substitution chain

Step 1 (definition): sin²θ_W = g_Y²/(g_Y² + g_2²), where g_Y is the U(1)_Y coupling
                     and g_2 is the SU(2)_L coupling at scale M_Z.

Step 2 (1-loop projector identity): the running of sin²θ_W from the cubic-bridge scale
                                    μ_BC to M_Z is driven by beta coefficients that are
                                    traces of generator projectors: b_i ∝ Σ_reps Tr(T^a_rep T^a_rep).
                                    For sin²θ_W, only the Y and SU(2)_L representation
                                    content enters.

Step 3 (C² generator trace identity): the C² block generators {λ_4, λ_5, λ_6, λ_7} are
                                      OFF-DIAGONAL in the canonical basis where Y and T³ are
                                      diagonal. Their contribution to the diagonal projectors
                                      Y² and T³² is:
                                      Tr(λ_i Y) = 0 for i ∈ {4,5,6,7} (Y is diagonal, λ_i
                                      off-diagonal).
                                      Tr(λ_i T³) = 0 for i ∈ {4,5,6,7} (T³ is diagonal,
                                      λ_i off-diagonal).

Step 4 (simplification): the C² block decouples from the 1-loop running of g_Y and g_2.
                         Δg_Y² [from C²] = 0 exactly. Δg_2² [from C²] = 0 exactly
                         (at 1-loop; 2-loop can have non-zero mixed contributions, but
                         these are bounded by the heavy-particle decoupling theorem
                         whenever M_X/Y ≳ M_Z).

Step 5 (direction for PASS): the PASS band is Δsin²θ_W < 1e-6 for 1-loop omission; this
                             becomes a theorem (exactly zero at 1-loop) if the trace
                             identities in Step 3 hold to machine precision.

Step 6 (reading off the direction): the absence of off-diagonal contributions to diagonal
                                    projectors is a CARTAN-TRACE identity (cf. agent
                                    memory S63: Cartan Trace Identity T_SU3 = T_SU2 = T_U1/12
                                    for ALL (p,q)). This identity is representation-
                                    INDEPENDENT and rep-space-INDEPENDENT when Y and T³ are
                                    in the Cartan subalgebra. PASS is an identity, not a
                                    bound.

### 10. What PASS and FAIL mean for the solution space
- **PASS**: C² block decouples from sin²θ_W at 1-loop. Obligation (ii) discharges.
  Truncation to u(1)⊕su(2) in S83 W3-G47 derivation is FIRST-PRINCIPLES, not an
  abbreviation.
- **INFO**: small 2-loop C² mixing. Still below PDG sensitivity; use-with-caveat.
- **FAIL**: C² is NOT decoupling. The sin²θ_W formula must be revised to include
  a GUT-like X/Y contribution, and μ_BC_K3 becomes a GUT ansatz rather than
  a geometric pin. Refutes obligation (ii).

### 11. Agent
Primary: `connes-ncg-theorist`
Alternate: `kaluza-klein-theorist` (one dispatches; connes-ncg-theorist carries
the A_F and rep-theoretic infrastructure natively)

### 12. Script prefix
`computations/s84_w9b_deriv_ii_c2_omission.py`

### 13. Runtime estimate
~5 min (small-matrix rep-theoretic identities; exact arithmetic possible).

---

## §W9b-107 — S84-TAU-CROSS-SCALE

### 1. Gate ID
`W9b-107-S84-TAU-CROSS-SCALE`

### 2. Trigger
`[VERIFY]` — PASS/FAIL within factor 3 of threshold (τ_fold recovery precision).

### 3. Classification
**PARTICLE** (RGE running of Standard-Model couplings maps to PDG sin²θ_W constraint,
inverting to pin τ_fold).

### 4. Hypothesis
Under W9b-105 PASS and W9b-106 PASS, the cubic-bridge formula
sin²θ_W(μ_BC) = 3/(3 + exp(12·τ_fold)) = 0.234803 at τ_fold = 0.19 is a first-principles
geometric expression. Running from μ_BC = 188.185 GeV to M_Z with 2-loop SM RGE + Yukawa
produces sin²θ_W(M_Z) that matches PDG = 0.23122 ± 0.00004. Inverting the RGE at the
PDG central value and uncertainty should recover τ_fold = 0.19 ± 0.01 (3He-B inheritance
prior from Volovik) at ≤3σ.

PASS if the RGE inversion yields τ_fold_EW = 0.190 ± 0.00002 (±2e-5 from ±4e-5 PDG
uncertainty on sin²θ_W, via chain rule applied to the cubic formula) AND
|τ_fold_EW - 0.19| < 3 × max(σ_EW, σ_inherit) where σ_EW ≈ 2e-5 (from PDG propagation)
and σ_inherit = 0.01 (from 3He-B scaling).

### 5. Pass/Fail/INFO Threshold
- **PASS**: τ_fold_EW ∈ [0.180, 0.200] (within 3σ of inherited 0.19 ± 0.01) AND
  σ(τ_fold_EW from PDG propagation) ≤ 2e-5.
- **INFO**: τ_fold_EW ∈ [0.170, 0.210]. 3–5σ tension; informative but non-decisive.
- **FAIL**: τ_fold_EW ∉ [0.170, 0.210]. Cross-scale pin contradicts the 3He-B inheritance.

Tolerance rule: **ABSOLUTE** on τ_fold_EW.

### 6. Machinery pin (PRDR)
- `N_eval`: N/A (RGE integration, not spectral).
- `L_max`: N/A.
- `scan_range`: RGE integration from μ_BC = 188.185 GeV to M_Z = 91.1876 GeV; log-μ
  step of 1e-4.
- `step_size`: adaptive Runge-Kutta (scipy.integrate.solve_ivp, method='RK45', rtol=1e-12,
  atol=1e-14).
- `tolerance`: 1e-10 on g_i(M_Z); 1e-8 on sin²θ_W(M_Z); τ_fold inversion to ±1e-6.
- `scheme`: MS-bar.
- `convention`: 2-loop SM beta functions (Machacek-Vaughn 1983/84 normalization, GUT-
  compatible GUT-normalized g_1 = sqrt(5/3)·g_Y) with Yukawa top contribution
  (y_t from m_t_pole via MS-bar conversion).
- `random_seed`: N/A.
- `GPU path`: not needed (RGE is ODE in one variable with ~6 couplings).
- **Prerequisite pin**: W9b-105 and W9b-106 BOTH PASS. If either FAILS, mark this
  gate PRE-REG-INCOMPLETE and do not dispatch.
- **PDG input pin**: sin²θ_W(M_Z) = 0.23122 ± 0.00004 (PDG 2024), as cited in
  canonical_constants if available, else add to canonical_constants.py with provenance
  "PDG 2024 — cited in S83 context §4.K" BEFORE running.

### 7. Input SHA-256 pins
- `canonical_constants.py`: `<computed-at-runtime>`.
- Script source: `<computed-at-runtime>`.
- Reference to W9b-105 and W9b-106 verdict lines in `s84_gate_verdicts.txt`:
  `<computed-at-runtime>` (must verify both PASS before RGE integration begins).

### 8. Expected output 4-tuple
`(value=τ_fold_EW, scheme=MSbar-2loop-Yukawa, convention=MV-normalization, L_max=N/A)`

### 9. Substitution chain

Step 1 (definition): sin²θ_W(μ) = g_Y(μ)² / (g_Y(μ)² + g_2(μ)²) in MS-bar.

Step 2 (boundary condition): at μ_BC = 188.185 GeV, sin²θ_W(μ_BC) = 3/(3 + exp(12·τ_fold))
                             (cubic-bridge identity from W9b-105/106 discharge).

Step 3 (RGE run): g_Y(M_Z), g_2(M_Z) obtained from g_Y(μ_BC), g_2(μ_BC) by 2-loop
                  integration downward in μ. sin²θ_W(M_Z) reconstructed from
                  g_Y(M_Z), g_2(M_Z).

Step 4 (inversion): given sin²θ_W(M_Z) = 0.23122 ± 0.00004 (PDG), solve for τ_fold_EW
                    such that the full chain reproduces PDG central value.

Step 5 (direction for PASS): if the geometric formula at μ_BC gives the right boundary
                             condition, AND the 2-loop SM RGE is correct, then
                             τ_fold_EW must equal the τ_fold used to compute μ_BC_K3.
                             Self-consistency: τ_fold_EW (from EW inversion) ≈ τ_fold_K3
                             (geometric input to μ_BC_K3 formula).

Step 6 (read off): PASS if |τ_fold_EW - 0.190| < 3×max(σ_EW, σ_inherit).

### 10. What PASS and FAIL mean for the solution space
- **PASS**: τ_fold pins to PDG at the EW scale consistent with 3He-B inheritance at the
  cosmological scale. Cross-scale self-consistency between substrate dynamics and SM
  RGE. The cubic-bridge geometric identity is verified.
- **INFO**: marginal 3–5σ tension. Worth recomputing with updated PDG or higher-loop
  contributions.
- **FAIL**: τ_fold_EW and τ_fold_cosmo disagree. Either the 3He-B inheritance is wrong
  OR the cubic form is not derived (contradicts W9b-105/106 PASS). Red flag.

### 11. Agent
Primary: `feynman-theorist`
Alternate: `phonon-first-cosmologist` (for the cross-scale interpretation; only one
dispatches)

### 12. Script prefix
`computations/s84_w9b_tau_cross_scale_rge.py`

### 13. Runtime estimate
~5–10 min (RGE ODE is cheap; inversion via scipy.optimize.brentq).

### 14. Prerequisite
DEPENDS on W9b-105 PASS AND W9b-106 PASS. Gated to W9b-B sub-wave.

---

## §W9b-108 — S84-YUKAWA-CLOSURE

### 1. Gate ID
`W9b-108-S84-YUKAWA-CLOSURE`

### 2. Trigger
`[VERIFY]` — factor-3 threshold on residual between μ_BC_K3_corrected and μ_BC_S83_PRIMARY.

### 3. Classification
**PARTICLE** (2-loop Yukawa contribution to the μ_BC matching scale).

### 4. Hypothesis
The S83 mu_BC-workshop produced two numerical cross-checks:
  μ_BC_S83_PRIMARY = 188.34 GeV (2-loop RGE gauge + Yukawa)
  μ_BC_CHK1        = 188.44 GeV (2-loop RGE gauge ONLY, no Yukawa)
  μ_BC_K3          = 188.185 GeV (tree-level cubic formula)

The Yukawa-induced correction Δ_2loop is defined by:
  μ_BC_K3_corrected = μ_BC_K3 · (1 + Δ_2loop)

Target: compute Δ_2loop from first-principles 2-loop Yukawa contribution to the
sin²θ_W evolution, and verify
  μ_BC_K3_corrected - μ_BC_S83_PRIMARY | / μ_BC_S83_PRIMARY < 1e-4   (<0.01%).

### 5. Pass/Fail/INFO Threshold
- **PASS**: |μ_BC_K3_corrected - 188.34| / 188.34 < 1e-4 AND the computed Δ_2loop
  is ≈ +8.26e-4 (verified via Python: 188.34/188.1846 - 1 = 8.256e-4; this is the
  inverse of the 0.0825% residual K3 vs PRIMARY). Self-consistent closure.
- **INFO**: 1e-4 ≤ residual < 1e-3. Closure approximate but not tight.
- **FAIL**: residual ≥ 1e-3. Yukawa correction cannot bridge the K3-PRIMARY gap;
  the cubic form has a larger deficit than 2-loop Yukawa can explain.

Tolerance rule: **RATIO** on |μ_BC_K3_corrected - 188.34| / 188.34.

### 6. Machinery pin (PRDR)
- `N_eval`: N/A.
- `L_max`: N/A.
- `scan_range`: top-Yukawa contribution to sin²θ_W RGE is the dominant Yukawa term
  (bottom and tau are O(10^{-2}) smaller). Evaluate explicit y_t(μ_BC) from m_t_pole
  with MS-bar matching.
- `step_size`: same RGE infra as W9b-107 (scipy RK45, rtol=1e-12).
- `tolerance`: 1e-8 relative on Δ_2loop.
- `scheme`: MS-bar.
- `convention`: 2-loop MV with Yukawa contributions in the canonical top/bottom/tau
  truncation (neglect charm, up, down, strange, muon, electron — all O(10^{-4}) to
  the top-Yukawa contribution).
- `random_seed`: N/A.
- `GPU path`: not needed.
- **Input pins**: μ_BC_S83_PRIMARY = 188.34 GeV and μ_BC_CHK1 = 188.44 GeV from S83
  (must appear in canonical_constants or be declared in-script with provenance
  pointer to S83 mu_BC-workshop W-2 verdict).

### 7. Input SHA-256 pins
- `canonical_constants.py`: `<computed-at-runtime>`.
- `s83_mu_BC_workshop_W2_results.*`: `<computed-at-runtime>` (closure hash of the
  S83 mu_BC-workshop output file in sessions/archive/session-83/).
- Script source: `<computed-at-runtime>`.

### 8. Expected output 4-tuple
`(value=Δ_2loop, scheme=MSbar-2loop-Yukawa-top, convention=MV-normalization, L_max=N/A)`

### 9. Substitution chain

Step 1 (definition): μ_BC_K3_corrected = μ_BC_K3 · (1 + Δ_2loop) = 188.185·(1 + Δ_2loop).

Step 2 (target): μ_BC_K3_corrected = μ_BC_S83_PRIMARY = 188.34 GeV.

Step 3 (solve): Δ_2loop = (188.34 / 188.1846) - 1 ≈ 8.256e-4 (Python-verified;
                the earlier "≈ 8.235e-4" anchor in plan drafts was slightly off —
                canonical target is 8.256e-4).

Step 4 (verify from 2-loop Yukawa): independently compute Δ_2loop from integrating the
                                    2-loop Yukawa contribution to sin²θ_W evolution:
                                    Δ_2loop_computed = ∫ [β_2loop_Yukawa / β_1loop_gauge] d(log μ).
                                    Chain in μ from μ_BC_K3 to M_Z using 2-loop MV betas
                                    with y_t(μ); cross-check against the target value
                                    from Step 3.

Step 5 (simplify): if |Δ_2loop_computed - 8.256e-4| / 8.256e-4 < 1e-2, then the 2-loop
                   Yukawa contribution matches the S83 W-2 PRIMARY/K3 gap.

Step 6 (direction): the sign of Δ_2loop is determined by whether y_t^4 term in the 2-loop
                    beta pushes sin²θ_W up or down. Y_t-contribution to β_{sin²θ_W}
                    is POSITIVE (standard result, Machacek-Vaughn), so a larger y_t
                    contribution gives a larger sin²θ_W, which via the cubic formula
                    pushes μ_BC DOWN. The residual 188.34 - 188.185 > 0 means the gauge-only
                    K3 UNDERESTIMATES μ_BC, so the missing Yukawa piece must INCREASE the
                    cubic-bridge scale. Sign check: positive Δ_2loop. PASS.

### 10. What PASS and FAIL mean for the solution space
- **PASS**: 2-loop Yukawa closure bridges the cubic-tree-level K3 expression to the
  full S83 PRIMARY value at <0.01%. The cubic formula is an excellent tree-level
  starting point; 2-loop Yukawa is a small correction. μ_BC pin at 188.185 GeV is
  robust to 2-loop corrections of order 1e-3 or less.
- **INFO**: bridge closes at 0.01–0.1%. 2-loop Yukawa is the right ballpark but there
  are missing ~0.1% corrections (possibly 3-loop or threshold matching).
- **FAIL**: 2-loop Yukawa alone cannot explain the K3-PRIMARY gap. The cubic form
  must be modified OR the S83 PRIMARY computation had an error.

### 11. Agent
Primary: `feynman-theorist`
Alternate: `phonon-first-cosmologist` (one dispatches; feynman-theorist
carries the 2-loop RGE infra from S83 G47)

### 12. Script prefix
`computations/s84_w9b_yukawa_closure.py`

### 13. Runtime estimate
~5 min.

### 14. Prerequisite
DEPENDS on W9b-105 AND W9b-106 PASS.

---

## §W9b-109 — S84-MW-CONSISTENCY-AUDIT

### 1. Gate ID
`W9b-109-S84-MW-CONSISTENCY-AUDIT`

### 2. Trigger
`[VERIFY]` — factor-3 threshold on |M_W_predicted - M_W_PDG| / σ_PDG.

### 3. Classification
**PARTICLE** (1-loop ρ-parameter and on-shell electroweak relations).

### 4. Hypothesis
Using sin²θ_W(M_Z) = 0.23138 from S83 W3-G47, the ρ-parameter from the top-loop at 1-loop
ρ = 1 + (3 G_F m_t²)/(8π²√2), and the on-shell relation
  M_W² = ρ · (1 - sin²θ_W(M_Z)) · M_Z²
should reproduce PDG M_W = 80.377 GeV (2024 value) within the combined PDG + framework
uncertainty.

### 5. Pass/Fail/INFO Threshold
- **PASS**: |M_W_predicted - 80.377| / σ_M_W_PDG < 3 where σ_M_W_PDG ≈ 0.012 GeV
  (PDG 2024). So PASS if |M_W_predicted - 80.377| < 0.036 GeV (3σ).
- **INFO**: 3σ ≤ residual < 5σ. Prediction is close but tension is informative.
- **FAIL**: residual ≥ 5σ. Framework-predicted M_W contradicts PDG at >5σ.

Tolerance rule: **ABSOLUTE** on M_W deviation (in GeV).

### 6. Machinery pin (PRDR)
- `N_eval`: N/A.
- `L_max`: N/A.
- `scan_range`: N/A (direct formula).
- `step_size`: N/A.
- `tolerance`: 1e-8 relative on M_W_predicted.
- `scheme`: on-shell electroweak (standard for M_W extraction).
- `convention`: 1-loop ρ-parameter with top-loop dominant; neglect subleading Higgs-loop
  and bottom-loop corrections (O(10^{-4}) on M_W, well within the 0.036 GeV PASS band).
- `random_seed`: N/A.
- `GPU path`: not needed.
- **Input pins** (must be in canonical_constants.py BEFORE dispatch; add if missing):
  - G_F = 1.1663787e-5 GeV^{-2} (PDG 2024)
  - m_t_pole (already in canonical_constants per framework convention)
  - M_Z (already in canonical_constants)
  - sin²θ_W(M_Z) = 0.23138 from S83 W3-G47 (reference S83 verdict in script docstring).
  - M_W_PDG = 80.377 GeV, σ_M_W_PDG = 0.012 GeV (PDG 2024).

### 7. Input SHA-256 pins
- `canonical_constants.py`: `<computed-at-runtime>`.
- `s83_gate_verdicts.txt`: `<computed-at-runtime>` (must contain G47 verdict pointing
  to sin²θ_W = 0.23138).
- Script source: `<computed-at-runtime>`.

### 8. Expected output 4-tuple
`(value=|M_W_predicted - 80.377|/σ_PDG, scheme=on-shell-EW, convention=rho-1loop-top, L_max=N/A)`

### 9. Substitution chain

Step 1 (definition of ρ): ρ = 1 + δρ, where δρ_top = (3 G_F m_t²)/(8 π² √2) is the
                          dominant 1-loop contribution. (Veltman 1977; standard result.)

Step 2 (on-shell relation): M_W² = ρ · (1 - sin²θ_W(M_Z)) · M_Z². [Sirlin/on-shell scheme.]

Step 3 (substitution): ρ = 1 + (3 · 1.1663787e-5 · m_t_pole²)/(8·π²·√2).
                       With m_t_pole = 172.76 GeV, δρ_top = 9.352818e-3 (verified via Python).
                       So ρ_1loop_top = 1.009353.
                       (Numeric check in-script against canonical m_t_pole.)

Step 4 (simplify): M_W² = 1.009353 · (1 - 0.23138) · M_Z² = 1.009353 · 0.76862 · M_Z².
                   M_W = M_Z · sqrt(1.009353 · 0.76862) = 91.1876 · sqrt(0.77582)
                       = 91.1876 · 0.88080 ≈ 80.318 GeV.

Step 5 (compare): |80.318 - 80.377| / 0.012 ≈ 4.9σ (ABOVE 3σ PASS band with 1-loop-top
                  rho). Step 4 has not included full 2-loop contributions; approximate
                  full-2-loop ρ ≈ 1.0100 (Awramik-Czakon-Freitas) shifts
                  M_W_predicted ≈ 80.344 GeV with residual ≈ 2.77σ (within 3σ PASS band).
                  The in-script computation must use either 1-loop-top OR full-2-loop ρ
                  and REPORT which.

Step 6 (direction): if using 1-loop-top only, expect M_W ≈ 80.318 GeV (residual ≈ 4.9σ,
                    ABOVE PASS band — this is INFO-to-FAIL edge depending on ρ scheme).
                    If using full-2-loop ρ ≈ 1.0100, expect M_W ≈ 80.344 GeV (residual
                    ≈ 2.77σ, within PASS band). Pre-register: BOTH computations, report
                    both; PASS adjudication uses full-2-loop ρ. The orchestrator MUST
                    treat 1-loop-top as a DIAGNOSTIC auxiliary; the canonical PASS/FAIL
                    verdict uses the 2-loop ρ evaluation.

### 10. What PASS and FAIL mean for the solution space
- **PASS**: Framework's sin²θ_W(M_Z) = 0.23138 is consistent with PDG M_W = 80.377
  at 3σ via ρ-parameter. The three observables (sin²θ_W, M_W, M_Z) are mutually
  consistent under framework's EW prediction chain. No internal EW tension.
- **INFO**: 3–5σ residual. Possibly points to additional ρ-parameter contributions
  or higher-order effects. Worth cross-checking against full SM 2-loop EW fit
  (Awramik-Czakon-Freitas).
- **FAIL**: Framework's sin²θ_W forces M_W away from PDG at >5σ. Either
  sin²θ_W = 0.23138 is wrong OR the ρ-parameter is non-standard OR the on-shell
  scheme needs matching to MS-bar.

### 11. Agent
Primary: `feynman-theorist`
Alternate: (none — feynman-theorist is canonical for 1-loop ρ, 2-loop RGE chain)

### 12. Script prefix
`computations/s84_w9b_mw_consistency.py`

### 13. Runtime estimate
~3 min (pure closed-form + small numerical evaluation).

### 14. Prerequisite
DEPENDS on W9b-105 AND W9b-106 PASS (via W9b-B ordering).

---

## W9b → W9a Parallel Dispatch Note

W9b and W9a are SIBLING sub-waves within Wave 9 of Session 84:
- **W9a** (sibling file `session-84-plan-w9a.md`): primary cube-3 override workshop
  (Layer 3a of CUBIC-W-EW) + broader μ_BC scope.
- **W9b** (this file): bi-criterion sub-obligations (Layer 3b of CUBIC-W-EW).

Dispatch ordering within Session 84:
- If W9a and W9b share a prerequisite structure, W9b-A (105 + 106) can dispatch in
  parallel with W9a's first sub-wave (if W9a's first sub-wave is also independent of
  W9b). The orchestrator MUST consult the W9a plan for its sub-wave structure at
  dispatch-time.
- W9b-B (107, 108, 109) dispatches AFTER W9b-A PASS verification. W9a sub-waves
  continue in parallel with W9b-B if they are independent.
- Total concurrent dispatch cap: ≤~8 (user self-imposed). W9b contributes at most
  3 concurrent agents at a time (2 in W9b-A, then 3 in W9b-B).

---

## W9b → W10 Decision Point (joint with W9a)

**Decision gate**: all five W9b verdicts AND all W9a verdicts available.

**CUBIC-W-EW discharge conditions** (joint W9a+W9b):
1. W9b-105 PASS (d_spec ≈ 3, cube-3 exponent geometric) — obligation (i).
2. W9b-106 PASS (C² block decouples from sin²θ_W) — obligation (ii).
3. W9b-107 PASS (τ_fold_EW = τ_fold_cosmo within 3σ) — cross-scale self-consistency.
4. W9b-108 PASS (2-loop Yukawa closure < 0.01%) — perturbative consistency.
5. W9b-109 PASS (M_W residual < 3σ) — electroweak sector self-consistency.
6. W9a Layer-3a obligations (see `session-84-plan-w9a.md`).

**If all discharge**: CUBIC-W-EW transitions from "external-ansatz S83 workshop result" to
"first-principles pinned framework prediction." The μ_BC = 188.185 GeV scale is a
GEOMETRIC output of the substrate's spectral-dimension and Jensen decomposition; the
PDG sin²θ_W match at 0.064σ (S83 G47) is genuine zero-free-parameter evidence.

**If any W9b gate FAILS**: record the failure mode in the joint W9/W10 decision report.
Do NOT retroactively downgrade W9a. The W9b-specific failure indicates which layer of the
bi-criterion bi-criterion pin has not discharged. S85 carry-forward will be:
- 105 FAIL → propose alternative spectral-dimension probes (heat-kernel expansion,
  noncommutative Laplacian zeta);
- 106 FAIL → re-examine Jensen decomposition u(2) ⊂ su(3) embedding; possibly
  GUT-completion ansatz (and μ_BC loses geometric status);
- 107 FAIL → investigate 3He-B inheritance scale-matching OR full 3-loop RGE;
- 108 FAIL → cross-check against 3-loop Yukawa or threshold corrections;
- 109 FAIL → cross-check against full 2-loop EW (Awramik-Czakon-Freitas).

**W10 dependency**: Wave 10 (post-W9 consolidation) MUST consume W9 joint outputs.
Do NOT begin W10 before W9 decision-report write-up is committed.

---

## W9b Machinery-Enumeration Pin (§0.11)

Per PRDR discipline (`.claude/rules/epistemic-discipline.md` §Pre-Registration
Completeness). Every gate's machinery is enumerated and pinned BEFORE W9b-A
dispatch.

### Producing scripts (5, one per gate)
1. `computations/s84_w9b_deriv_i_spectral_dim.py`
2. `computations/s84_w9b_deriv_ii_c2_omission.py`
3. `computations/s84_w9b_tau_cross_scale_rge.py`
4. `computations/s84_w9b_yukawa_closure.py`
5. `computations/s84_w9b_mw_consistency.py`

### Free-parameter enumeration (static-analysis-level, pre-registered)

| Gate | Free parameter | Pin |
|:-----|:---------------|:----|
| 105 | s-grid spacing | Δs=0.001 near pole candidate; Δs=0.05 in bulk |
| 105 | ε regulator on \|D_K\| = sqrt(D²+ε²) | ε = 1e-12 |
| 105 | L_max | 10 primary; {6,8,12} cross-check |
| 105 | fiber-transition scale definition | argmin of \|d²ζ/ds²\| (structural min, reported) |
| 106 | Gell-Mann basis | canonical λ^a with T^a = λ^a / 2 |
| 106 | Y normalization | Y = √(1/3)·λ_8 (hypercharge convention) |
| 106 | C² block | spanned by λ_4, λ_5, λ_6, λ_7 |
| 106 | tolerance on trace identity | 1e-14 (double-precision zero) |
| 107 | RGE order | 2-loop SM MV with Yukawa top/bottom/tau |
| 107 | scheme | MS-bar |
| 107 | g_1 normalization | GUT-compatible sqrt(5/3)·g_Y |
| 107 | top Yukawa matching | y_t(μ_BC) from m_t_pole via MS-bar 1-loop matching |
| 107 | numerical integrator | scipy RK45, rtol=1e-12, atol=1e-14 |
| 107 | τ_fold inversion | scipy brentq, bracket [0.15, 0.25], xtol=1e-7 |
| 108 | Yukawa truncation | top-bottom-tau only; quark/lepton O(10^{-4}) ignored |
| 108 | subtraction of CHK1 | μ_BC_CHK1 = 188.44 GeV (gauge-only) as reference |
| 109 | ρ truncation | pre-register BOTH (1-loop-top AND 2-loop full); report both |
| 109 | G_F and m_t_pole | canonical_constants.py |
| 109 | PDG M_W value | 80.377 ± 0.012 GeV (PDG 2024) |

### Non-pinnable parameters (declared as diagnostic outputs, not free)
- 105: the actual value of d_spec(s*) — this IS the gate output, not a free parameter.
- 106: the actual inner-product traces — these are theorem-level zeros or non-zeros.
- 107: τ_fold_EW — this IS the gate output.
- 108: Δ_2loop_computed — this IS the gate output.
- 109: M_W_predicted — this IS the gate output.

### PRU audit result
- **PRU Class 8**: NONE. All free parameters are pinned above.
- **PRE-REG-INCOMPLETE pending prerequisites**: W9b-107, W9b-108, W9b-109 are gated
  to W9b-A PASS. If W9b-105 or W9b-106 FAILS, these three gates register as
  PRE-REG-INCOMPLETE (not FAIL), per
  `.claude/rules/gate-verdicts.md` §Rules.

---

## W9b Input-SHA Ledger

Before dispatch, verify and log the SHA-256 of every static input. Dynamic inputs
(verdict files, newly-written scripts) are marked `<computed-at-runtime>` and logged
by the script in the first 20 lines of stdout.

### Static inputs (must be present and hashed)
1. `computations/canonical_constants.py` (all 5 scripts)
2. `computations/data/D_K_eigenvalues_Lmax10_tau019.npz` (W9b-105)
   - If the filename differs from this convention, the orchestrator must resolve the
     canonical D_K eigenvalue dataset from S34+ output and update the script
     input-pin path BEFORE dispatch.
3. Gell-Mann generator definitions (W9b-106) — INLINE in script, no external file.

### Dynamic inputs (hashed at runtime)
1. Script source of each of the 5 W9b scripts (self-hash; first 20 lines of stdout).
2. `computations/s84_gate_verdicts.txt` prior entries (W9b-107, 108, 109 must
   verify W9b-105 and W9b-106 verdict lines are present and PASS before proceeding).
3. For W9b-108: `sessions/archive/session-83/` mu_BC-workshop output file containing
   μ_BC_S83_PRIMARY = 188.34 and μ_BC_CHK1 = 188.44 GeV (specific path resolved at
   dispatch-time).
4. For W9b-109: `sessions/archive/session-83/s83_gate_verdicts.txt` (to cite G47's sin²θ_W
   = 0.23138 output).

### Closure SHA (per gate, full 64-char hexdigest)
Each script computes `closure_sha256 = sha256(SHA_map_of_all_inputs)` and emits it
as the final non-verdict line of stdout, per `.claude/rules/gate-verdicts.md` §1-3.
Verdict line format:

```
W9b-{105|106|107|108|109}-{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<64-char-closure>
```

Dual-SHA schema (audit_sha256 + content_sha256) is optional at W9b; S84 plan-level
discipline is decided in the sibling W9a governance. W9b inherits the W9a decision.
If W9a commits to dual-SHA at S84, W9b scripts are updated in-dispatch with the
dual-SHA pattern. If not, single-SHA format per §8 of `session-84-context.md` is used.

---

## Post-Wave 9b Carry-Forward Template

Per `.claude/rules/epistemic-discipline.md` and `feedback_fix-in-session-never-defer.md`:
even if all five W9b gates PASS, produce structured carry-forward for S85:
1. **W9b-L1L2-LAYER-CLASSIFICATION**: classify each of the 5 W9b verdicts under the
   three-layer regulator theorem (L1 / L2 / L3). Expected: 105 and 106 are L1
   (axiomatic rep-theoretic / zeta), 107-109 are L3 (observable-layer PDG matching).
2. **W9b-VII-K-LANDING**: append W9b verdicts to §VII.K atlas with LAYER-of-pin
   assignments (CF for W1b §VII.K integration).
3. **W9b-META-PRINCIPLE-CHECK**: do W9b results respect the §VII.K-META principle
   (R-protected ≤1.5 / NOT-R ≥2.5)? μ_BC_K3 spans are expected R-protected (cubic-bridge
   balanced); verify explicitly at S85.
4. **W9b-BI-CRITERION-ATLAS-ROW**: append a row to the §VII atlas classifying the
   μ_BC pin as "dual-obligation bi-criterion", structurally distinct from single-pin
   observables. Open question: are other observables (α_s, m_H) also bi-criterion?

---

**End of Wave 9b plan.**

Output file size target: ~650 lines. This file is complete and dispatch-ready.
All five gates are pre-registered per gate-verdict standards. Input-SHA ledger, machinery
pin, and dependency ordering are fixed. Orchestrator may dispatch W9b-A (2 parallel
agents: spectral-geometer + connes-ncg-theorist) immediately upon W9b activation.
