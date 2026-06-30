# Path B D2 Workshop — Substrate Dynamics Rule Licensing

## Origin

Conversation 2026-04-27. User has held a long-standing goal of building a
computation-grade direct simulation of the substrate (Path B), distinct from the GPE
analog at `phonon-exflation-sim/` (Path A). Triggered by dual-reviewer
assessment of Yu et al. 2025 PNAS plasma-ML force-inference (volovik-
superfluid-universe-theorist + landau-condensed-matter-theorist), where both
reviewers reached PORT-PARTIALLY conditional verdicts and the user determined
that direct substrate simulation has higher framework value than analog-
extension via the Yu et al. methodology.

This workshop addresses the single decision-question that gates whether a
Level B1 substrate simulator can be launched without an upstream theory-decision
session.

## Level B1 simulator — the proposed simplest viable path

**State variable**: Jensen deformation `τ(x, t)` only (other geometric data
assumed to adiabatically track τ).

**Evolution rule (D2(a) candidate)**:

```
d²τ/dt² + γ·dτ/dt = −δS_spec[τ]/δτ        (second-order, damped)
```

or the first-order gradient flow:

```
dτ/dt = −δS_spec[τ]/δτ                     (first-order, dissipative)
```

**Inner loop per timestep**: existing static `D_K(τ)` eigenvalue computation
at `L_max = 10` (155,984 eigenvalues, validated infrastructure across multiple
sessions) → spectral action `S_spec(τ) = Σ_n f(λ_n²(τ)/Λ²)` with cutoff
function `f` → numerical derivative `δS_spec/δτ` via finite difference or
adjoint method.

**Equilibrium gate**: `τ` converges to canonical `τ_fold = 0.190` (per
`mcp__knowledge__.get_constant("tau_fold")` provenance); equilibrium values
of `a_2(τ)`, `a_4(τ)` match canonical constants.

## The gating question

**Is D2(a) (gradient flow on the spectral action with Jensen `τ` as variable)
LICENSED by the framework's existing structure, or does it require additional
postulates?**

- "Licensed" means: derivable from the framework's existing variational
  structure or canonical equations, without external assumptions about
  dissipation, time-orientation, or dynamical hierarchy.
- "Not licensed" means: the gradient flow is a postulate one COULD impose,
  but it doesn't follow from the spectral action principle alone — the
  spectral action gives a critical-point principle (`δS_spec = 0`), not a
  flow rule.

The distinction matters because the Level B1 simulator's verdicts depend on
the dynamics rule being defensible. A rule that doesn't follow from the
framework's structure produces verdicts that are pre-registered conditional
on the rule, not conditional on the framework.

## Workshop format

Three sequential rounds, each agent writes their section after reading the
prior rounds. No round-skipping. Each round must reach a verdict.

## Round 1 — connes-ncg-theorist (NCG / spectral action perspective)

Address from the framework's noncommutative-geometry foundation:

1. Is `S_spec(τ)` a well-posed action functional with `τ` as a *dynamical*
   variable, or only as a *parameter* selecting different spectral triples?
   This is the foundational distinction — if `τ` is only a parameter, no
   dynamics rule on `τ` follows from the spectral action principle.

2. Does the spectral action principle (`δS_spec = 0`) license a dynamical
   flow toward the critical point, or only a critical-point principle? If
   only the latter, what additional structure (Hessian, Riemannian metric on
   the moduli space of Jensen deformations, dissipation tensor) would have
   to be supplied to define gradient flow?

3. Is `S_spec` known to be a Lyapunov function for any candidate gradient
   flow on Jensen deformations? Connes-Marcolli's NCG-quantum-fields-motives
   book has machinery for spectral-triple deformation; cite if relevant.

4. The framework has documented `τ_fold = 0.190` as the fold transit point.
   Is `τ_fold` known to be a critical point of `S_spec(τ)`? If yes, that's a
   structural endorsement of D2(a)'s equilibrium predictions. If no, D2(a)'s
   predicted equilibrium would not match the canonical fold.

5. Cite Connes-Marcolli or follow-up NCG literature that addresses dynamical
   evolution of deformation parameters of spectral triples — even if the
   conclusion is "this hasn't been done."

**Output**: section with verdict LICENSED / NOT LICENSED / LICENSED-WITH-
CAVEATS / RESEARCH-GAP, with structural reasoning. Be honest if the
literature does not address this — that is itself important information.

## Round 2 — spectral-geometer (heat-kernel / mathematical well-definedness)

After reading Round 1, address:

1. Is `S_spec(τ) = Σ_n f(λ_n²(τ)/Λ²)` differentiable in `τ` at all τ in
   `[0, 1]`, or are there branch points / level crossings (eigenvalues
   crossing each other or crossing zero) where the spectral action is not
   smooth as a function of `τ`? If branch points exist, where are they
   relative to `τ_fold = 0.190`?

2. Heat-kernel asymptotic expansion gives `S_spec ~ Σ_n a_n(τ) Λ^{4-n}` with
   Seeley-DeWitt coefficients `a_n(τ)`. How does the cutoff function `f`
   affect differentiability of `S_spec(τ)` — does choice of `f` introduce
   spurious smoothing or, conversely, expose discontinuities?

3. Is Jensen deformation parameter `τ` the right "coordinate" on the moduli
   space, or should the metric on moduli be determined by a Hessian
   `∂²S_spec/∂τ²` evaluated at `τ_fold`? The functional derivative
   `δS_spec/δτ` is metric-dependent; without a canonical metric the gradient
   flow is non-canonical.

4. Numerical stability: at `L_max = 10` with 155,984 eigenvalues, what's
   the realistic timestep `dt` for a symplectic Verlet integrator? Stiffness
   from high-`λ_n` modes — is mode-by-mode integration needed, or does the
   spectral action's UV-cutoff `f` automatically suppress stiff modes?

5. Adjoint vs finite-difference computation of `δS_spec/δτ`: which is
   numerically robust at L_max=10 GPU eigenvalue solve? `torch.func.jacrev`
   on the spectral-action function gives an adjoint; finite difference
   requires two eigenvalue solves per gradient evaluation.

**Output**: section with verdict on mathematical well-definedness + numerical
feasibility. Specifically address: do the eigenvalue level crossings as a
function of τ break smooth gradient flow, or are they isolated and
recoverable?

## Round 3 — volovik-superfluid-universe-theorist (analog grounding)

After reading Rounds 1+2, address whether existing substrate-action
variational dynamics provide precedent:

1. **q-theory** (Klinkhamer-Volovik): the q-field evolves via what dynamical
   rule on the cosmological action? Is it a gradient flow analogous to
   `dq/dt = −∂S/∂q`, or an oscillation on a non-dissipative phase space, or
   something else? Cite the variational principle explicitly.

2. **F-theory** (your own program of identifying the q-field with a
   thermodynamic variable): same question. Where does dissipation come from
   in F-theory if it is present at all?

3. **GPE Madelung dynamics**: in what regime does the BEC analog produce
   Jensen-tau-like dynamics, if any? The Madelung representation
   `ψ = √ρ exp(iθ)` gives `dθ/dt = -μ - v²/2 + ...`; is there an analog of
   "gradient flow on the spectral action of the GPE" that has been studied?
   Volovik-Mineev-Salomaa structure of superfluid action under deformations
   relevant.

4. Counter-examples: are there known substrate-action systems where gradient
   flow does NOT apply or produces unphysical results? In particular, when
   the action is unbounded below (typical for spectral actions with
   non-positive `a_0` contributions), gradient flow runs to infinity. How
   is this handled in q-theory / F-theory / GPE?

5. Practical assessment: if D2(a) is mathematically well-defined and NCG-
   licensed (Rounds 1+2), is it ANALOG-licensed in the sense that q-theory
   /F-theory/Madelung provide a parallel picture? Or does the analog
   contradict D2(a) — i.e., the existing substrate-action variational
   dynamics literature uses something other than gradient flow?

**Output**: section with verdict on analog precedent. Be explicit if your
existing q-theory/F-theory work uses gradient flow, oscillation, or a
mixture — that determines whether D2(a) is "the standard substrate-action
dynamics" or a novel rule that requires its own justification.

## Synthesis target

After three rounds, decide one of:

- **LAUNCH**: D2(a) is licensed by all three perspectives; proceed to Level
  B1 simulator architecture spec and ~1-month implementation. Decision
  artifacts: explicit citations to Connes-Marcolli / heat-kernel /
  q-theory literature; a clean derivation of D2(a) from those sources.

- **BLOCKED**: D2(a) is not licensed; recommend a D2 research session
  (literature review, alternative dynamics rules — Ricci flow, Wheeler-
  DeWitt, q-theory-style) before any simulator code is written. Decision
  artifacts: list of specific gaps that must close + recommended next
  workshops to close them.

- **CONDITIONAL**: D2(a) is licensed under specific conditions (adiabatic
  regime, small-deformation limit, specific cutoff function `f`, specific
  metric on Jensen moduli) that must be respected by the simulator
  architecture. Decision artifacts: the precise conditional clauses + Level
  B0 proof-of-concept scope inside the licensed regime.

The synthesis maps to a concrete next-action item, not to a narrative
summary.

---

## Round 1 — connes-ncg-theorist

**Date**: 2026-04-27. **Agent**: connes-ncg-theorist. **Method**: read `phonon_exflation_cosmology.md`-relevant priors via knowledge MCP (`tau_fold`, `dS_fold`, `S_fold`, `d2S_fold`, S84-W8a verdicts, S83 dynamics-dressing audit) and arXiv search of the Chamseddine-Connes spectral-action corpus.

### Q1. Is `S_spec(τ)` a well-posed action functional with `τ` as a *dynamical* variable, or only as a *parameter* selecting different spectral triples?

**Structural answer: τ is a *parameter labelling distinct spectral triples*, not a dynamical variable inside a single spectral triple.**

Substitution chain.

Step 1 (definition of spectral triple). A spectral triple `(A, H, D)` is a fixed triple of (algebra, Hilbert space, self-adjoint Dirac operator) satisfying the seven NCG axioms (dimension, regularity, finiteness, reality, first order, orientability, Poincaré duality). The Dirac operator is a single self-adjoint operator on a single Hilbert space.

Step 2 (definition of Jensen deformation). The Jensen deformation `τ ↦ D_K(τ)` produces a *family* of Dirac operators on a *fixed* Hilbert space H = L²(SU(3), S). Each value of τ yields a *different* spectral triple `(A, H, D_K(τ))`. The seven NCG axioms must be checked at each τ separately; in particular the regularity axiom (smoothness of `T ↦ [D, T]` operator-norm) and the dimension axiom (Weyl law) are τ-dependent statements about τ-dependent operators.

Step 3 (definition of spectral action). `S_spec(τ) := Tr f(D_K(τ)²/Λ²)` is a real-valued function on the moduli space of spectral triples parameterized by τ.

Step 4 (substitution into "dynamical variable" hypothesis). To call τ "dynamical" requires (a) a phase space `T*M_{Jensen}` carrying a symplectic or Poisson structure, and (b) a Hamiltonian or Lagrangian `H[τ, π_τ]` that generates time-evolution of τ. In Chamseddine-Connes (1996, 0512169, 0605011, 0812.0165, 1008.3980, 1008.0985, 1105.4637, 1809.02944), neither object is constructed for a deformation parameter of the spectral triple itself. The fields that ARE dynamical in the standard NCG-SM treatment are the *inner fluctuations* `D ↦ D + A + JAJ⁻¹` — gauge connections and Higgs fields living *on top of* a fixed spectral triple — not the deformation parameters of the triple.

Step 5 (direction). `S_spec(τ)` is well-posed as a smooth function `M_{Jensen} → ℝ`, but τ enters as a parameter labeling distinct spectral triples, NOT as a configuration variable of a single spectral-triple dynamics.

**Implication for D2(a)**: Treating τ as a dynamical variable adds external structure to the NCG framework — specifically, a metric on `M_{Jensen}` and a kinetic term for τ. This is a postulate, not a derivation.

### Q2. Does the spectral action principle license a flow toward the critical point, or only a critical-point principle?

**Structural answer: Only a critical-point principle. No flow rule is licensed by the principle alone.**

The Chamseddine-Connes spectral action principle (CC96, "The Spectral Action Principle", hep-th/9606001) states:

> The bosonic action is the spectral action `Tr χ(D/Λ)`. The classical equations of motion are obtained by varying the spectral triple data `(A, H, D)` over admissible deformations and setting `δS_spec = 0`.

This is *identical in logical structure* to the variational principle of classical mechanics: it singles out critical points but is *silent about how a non-critical configuration evolves toward them*. To convert "δS = 0" into "dτ/dt = -δS/δτ" one must additionally supply:

(a) **a Riemannian metric `G_{ττ}` on `M_{Jensen}`** to convert the cotangent-valued differential `δS/δτ ∈ T*M_{Jensen}` into a tangent-valued gradient `G^{ττ} δS/δτ ∈ TM_{Jensen}`. Without G, the gradient is not well-defined — only the differential is canonical.

(b) **a dissipation tensor or friction coefficient γ** if the flow is dissipative (first-order overdamped). This is a *thermodynamic* input, not a geometric one.

(c) **a kinetic mass `M_{ττ}`** if the flow is second-order Newtonian (`M ∂²τ/∂t² + γ ∂τ/∂t = -δS/δτ`).

None of (a), (b), (c) are produced by the Chamseddine-Connes axioms. The closest NCG-internal candidate for (a) would be the Bures-Uhlmann metric on the space of states or the Connes metric structure on the moduli of spectral triples, but no canonical "Jensen metric" has been derived in either Connes-Marcolli "Noncommutative Geometry, Quantum Fields and Motives" (CCM 2007) or its follow-ups.

**Substitution chain for the gradient-flow direction claim**:

Step 1 (definition). δS/δτ is a 1-form on `M_{Jensen}`, dim(M_{Jensen}) ≥ 1.
Step 2 (definition). Gradient flow `dτ/dt = -G^{ττ} δS/δτ` requires inverse metric `G^{ττ}`.
Step 3 (substitution). In NCG axioms, `M_{Jensen}` has no canonical Riemannian structure — different choices of G give *different* flows with *different* equilibria (in general), even though they share the same critical points.
Step 4 (simplification). The choice of G is part of the *postulate*, not a derivation.
Step 5 (direction). D2(a) requires picking a metric. Default `G_{ττ} = 1` (Euclidean on a 1-D parameter) is a *choice*, not a consequence.

### Q3. Is `S_spec` a Lyapunov function for any candidate gradient flow on Jensen deformations?

**Structural answer: NO — known framework results show `S_spec(τ)` is monotonic in τ (S77 baseline), so it is *trivially* monotonic along the gradient flow `dτ/dt = -δS/δτ`, but it is NOT bounded below as τ ranges over the Jensen interval, so it cannot be a *Lyapunov* function in the rigorous sense.**

Substitution chain.

Step 1 (definition of Lyapunov function). `V: M → ℝ` is a Lyapunov function for flow `Φ_t` at fixed point `x*` iff (i) `V(x*) = 0`, (ii) `V(x) > 0` for `x ≠ x*` in a neighborhood, (iii) `dV/dt(Φ_t(x)) ≤ 0` along the flow.

Step 2 (framework data). From `s76_alpha_s_first_principles.py`: "the spectral action V(τ) INCREASES with τ for τ > τ_fold". From canonical_constants: `S_fold = 250360.68` at τ_fold=0.190 with `dS_fold = +58672.80` (S42 absolute-value cutoff) or `dS/dτ = -2.036e+04` (Gaussian cutoff, S84 W8a-85). `dS_fold ≠ 0`, so τ_fold is *not* a critical point of `S_spec` — see Q4.

Step 3 (substitution). Without a critical point of `S_spec` inside the Jensen interval `[0,1]`, condition (i) fails: there is no τ* with `δS/δτ|_{τ*} = 0` AND `V(τ*) = 0` simultaneously. The S84 W8a-85 scan over `τ ∈ {0.17, 0.18, 0.19, 0.21, 0.22}` found NO sign change in `dS/dτ` for either Gaussian or absolute-value cutoff — i.e., no stationary point in the scanned range.

Step 4 (simplification). The function `τ ↦ S_spec(τ)` is monotonic on the explored Jensen window. Under gradient flow `dτ/dt = -δS/δτ`, τ flows monotonically to the *boundary* of the Jensen interval (τ → 0 or τ → 1, depending on sign), NOT to an interior fixed point.

Step 5 (direction). `S_spec` is not a Lyapunov function for any *interior* fixed point because there is no interior fixed point. It IS monotonic along the gradient flow by chain rule (`dS/dt = (δS/δτ)(dτ/dt) = -G^{ττ}(δS/δτ)² ≤ 0`), but the flow's ω-limit set is on the boundary, not at any geometric "fold".

**Permanent NCG result (S24a, baseline-findings-s66)**: Spectral Action Monotonicity Theorem — `a_{2k}` are monotone for k=0,1,2,3 with periodic-orbit corrections bounded at 10⁻³⁹. Combined with the Mellin-cone universality theorem (S84 W8a-89, PASS — `chi_2 ∈ [1.5, 2.5]`), this implies `S_spec(τ)` is a smooth monotonic function on the Jensen direction, NOT a function with an interior local minimum at τ_fold.

### Q4. Is `τ_fold = 0.190` known to be a critical point of `S_spec(τ)`?

**Structural answer: NO. This was *directly tested* in S84 W8a-85 (S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD) and FAILED.**

Verdict line (canonical, from `computations/s84_gate_verdicts.txt`):

```
S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD: FAIL --
  value=-2.035810e+04
  scheme=spectral_moment_analytic
  convention=Chamseddine-Connes-Gaussian
  L_max=10
  sha256=581a23921b9eb3aee1d4fc82c141cd0c02e47112c1c5224b6189b69e1f622308
```

Pre-registered threshold: PASS iff `|dS/dτ|_{0.19}| < 1e-10`. Computed: `dS/dτ_{Gauss} = -2.036e+04` (15 orders of magnitude above PASS threshold). Cross-check (absolute-value cutoff, S42 canonical convention): `dS_fold = +58672.80`, also 15 OOM above PASS. The two cutoffs disagree on *sign* but both confirm `|dS/dτ| ≫ 0`.

The S84 W8a-90 synthesizer (S84-VARIATIONAL-PRINCIPLE-REFORMULATION) *also* FAILed, value=2 (only 2 of 3 prerequisites passed; W8a-85 failure forced the synthesizer to FAIL). The constraint-map update from W8a-90 is explicit:

> **BARE-SPECTRAL-ACTION as Variational Principle: CLOSED.** Branch does not stabilize τ from first principles.
>
> **DRESSED-SPECTRAL-ACTION as V.P.: OPEN.** Bare S[D_K] is not stationary at τ_fold, but the DRESSED spectral action (BCS/GGE/Gilkey loop-corrections) may have its extremum moved to τ_fold.
>
> **EMPIRICAL-τ_fold RETENTION: ACTIVE (default fallback).**

**Implication for D2(a)**: The simulator's predicted equilibrium τ* (defined by `δS_spec/δτ|_{τ*} = 0` for the bare Chamseddine-Connes Gaussian functional) does *not* coincide with τ_fold = 0.190. It coincides with a *boundary* of the Jensen interval (or with no equilibrium at all, since the function is monotonic). This is a *structural* mismatch between the simulator's gate ("τ converges to τ_fold") and the framework's actual canonical: τ_fold is *empirical input*, not a critical point of the bare spectral action.

The S83 dynamics-dressing audit (feynman × transit, 2026-04-18) and the S84 W8a constraint map both leave OPEN the possibility that some *dressed* functional (BCS condensation free energy + GGE entropy + KK-loop corrections + Gilkey loop integrals) *could* extremize at τ_fold. None of these has been computed.

### Q5. Connes-Marcolli or follow-up NCG literature on dynamical evolution of spectral-triple deformation parameters?

**Structural answer: I have not found NCG-canonical work that addresses gradient-flow dynamics on the moduli of spectral-triple deformation parameters in the sense D2(a) requires. This is a RESEARCH GAP, not a settled question.**

Papers reviewed (arXiv search via mcp__paper-search__):

- **Connes-Marcolli 2007, "Noncommutative Geometry, Quantum Fields and Motives"** (the book): treats spectral-triple deformations through inner fluctuations, the Connes-Kreimer Hopf algebra of renormalization, and number-theoretic flows (the BC and GL₂ systems). The "dynamics" in CCM chapter 1 is *renormalization-group flow* on the coupling constants generated by inner fluctuations, NOT on the deformation parameters of the spectral triple's underlying geometry. Section 18 ("Riemann zeta and noncommutative geometry") and chapter 4 (BC system) involve KMS flows on a *type III* von Neumann algebra associated to the spectral triple, but these are flows on the *state space* of A, not on the moduli of D.
- **Chamseddine-Connes hep-th/9606001 (CC96)**: spectral action principle as `δS_spec = 0`. *No flow rule.*
- **Chamseddine-Connes hep-th/0512169 (2005, "Scale Invariance in the Spectral Action")**: introduces a *dilaton field* `φ` to make the cutoff scale Λ → Λ·e^φ dynamical. This is a step toward dynamics, but the dilaton is a *bosonic field added to the inner fluctuations* of D (not a geometric deformation of D itself), and the equation of motion for φ comes from `δS_spec/δφ = 0`, again a critical-point principle.
- **Chamseddine-Connes 0605011, "Inner fluctuations of the spectral action"**: deformation `D ↦ D + A` produces gauge connections via `δS_spec` over the space of inner fluctuations. NO geometric-parameter flow.
- **Chamseddine-Connes 1008.3980, "Spectral Action for Manifolds with Boundary"**: boundary terms; static, not dynamical.
- **Chamseddine-Connes-van Suijlekom 1809.02944, "Entropy and the spectral action"**: identifies the spectral action with the von Neumann entropy of the second-quantized Dirac state; this connects S_spec to thermodynamics, providing one *candidate* metric (the Bogoliubov-Kubo-Mori metric on states), but stops short of a τ-dynamics rule.
- **Cacic 2014 (arXiv:1408.4429), "A reconstruction theorem for Connes-Landi deformations"**: parameterizes Connes-Landi deformations by group-cohomology classes and proves rigidity under further deformation. Provides a *moduli structure*, but no gradient-flow dynamics.
- **Floricel-Ghorbanpour-Khalkhali 2016 (arXiv:1612.06688), "Ricci Curvature in NCG"**: defines a noncommutative Ricci density via spectral functionals on curved noncommutative tori. *This is the closest analogue* — a Ricci-flow-type evolution would be `dD/dt ∝ -Ric(D)` — but the paper stops at the static definition; no flow dynamics is constructed.
- **Fathizadeh-Khalkhali 2019 (arXiv:1901.07438), "Curvature in NCG" review**: comprehensive review; explicitly notes that *Ricci flow on noncommutative manifolds remains an open problem* (their §6.4 mentions it as a research direction).
- **Alexa 2025 (arXiv:2508.11652), "Spectral Deformation Flow and Dimension Recovery"**: independent (non-Connes-school) recent paper proposing a spectral deformation flow `Ĉ C_n(τ) = ...` for mode amplitudes. Uses spectral data of an effective Laplacian, not a Connes spectral triple. *Not* a Connes-Marcolli line of work.

**What would close the gap?** A program analogous to *Hamilton-Perelman Ricci flow lifted to NCG* — i.e., construct `dD/dt = F[D]` for some functional F derived from `δS_spec`, prove short-time existence, and verify that the framework's `τ_fold` is a fixed point or attractor. The Floricel-Ghorbanpour-Khalkhali Ricci density is the natural starting point, but the dynamics has not been written down. The Chamseddine-Connes-van Suijlekom entropy-spectral-action correspondence (1809.02944) is the natural source of a metric (BKM on states), but the lift from state space to D-deformation moduli has not been performed.

### Verdict

The framework's existing structure does *not* license D2(a) as written.

- Q1: τ is a parameter, not a dynamical variable; D2(a) implicitly adds a phase-space structure that is external to NCG.
- Q2: spectral action principle is *only* a critical-point principle; gradient flow requires an additional metric `G_{ττ}` and possibly a friction `γ` and mass `M`.
- Q3: `S_spec` cannot be a Lyapunov function for τ_fold because τ_fold is *not* a critical point.
- Q4: τ_fold is *empirically pinned*, not a critical point of `S_spec`. S84 W8a-85 FAIL with `dS/dτ|_{0.19} = -2.04e+04` (Gauss) / `+5.87e+04` (abs) — directly falsifies the equilibrium condition.
- Q5: NCG literature does not address τ-dynamics in the required sense; the closest precedents (CCM type-III KMS flows, Floricel-Ghorbanpour-Khalkhali Ricci density, CC-vS entropy-spectral correspondence) provide raw materials but no completed dynamics rule.

The question of whether D2(a) is licensable for a *dressed* functional (BCS+GGE+Gilkey corrections that *might* shift the extremum to τ_fold) is open per the S83 dynamics-dressing audit and the S84 W8a-90 constraint map. That is a different question from the one asked here — D2(a) as written uses the *bare* Chamseddine-Connes Gaussian spectral action, which is decisively *not* extremized at τ_fold.

**Round 1 verdict**: NOT LICENSED — bare-spectral-action gradient flow is silent on dynamics (critical-point principle only), τ_fold is not a critical point of bare `S_spec` (S84 W8a-85 FAIL, dS/dτ ~ 5×10⁴ at fold, 15 OOM above PASS threshold), and the NCG canon (CCM 2007 + Chamseddine-Connes 1996-2018 + Cacic + Floricel et al.) does not supply a Riemannian metric on Jensen moduli or a flow rule from the axioms.

**Caveats for Round 2/3 to consider**:
1. *Dressed* spectral action (BCS condensation + GGE entropy + Gilkey loop corrections) remains an OPEN constraint-map branch per S84 W8a-90. If the simulator targets a dressed functional whose extremum *is* at τ_fold, the question reopens. But that requires constructing the dressing, computing its extremum, and demonstrating the shift — none of which is in the framework today.
2. The Chamseddine-Connes-van Suijlekom 1809.02944 entropy-spectral-action correspondence supplies a candidate Riemannian metric on states (Bogoliubov-Kubo-Mori). Lifting this from states to D-deformation moduli would be a research program, not a derivation from existing axioms.
3. τ_fold = 0.190 is the value pinned by *cosmological epoch matching* (S58 Volovik partition, Mack gates), not by spectral-action stationarity. A simulator whose verdict depends on "τ converges to τ_fold under gradient flow on bare S_spec" tests a hypothesis that the framework *itself has already falsified* (S84 W8a-85 FAIL). The simulator would either (a) reproduce the FAIL, or (b) PASS only by importing dressing/empirical input that bypasses the "license from existing structure" requirement.
4. If Path B proceeds, the Level B0 proof-of-concept should be inside a *toy* spectral triple (e.g., the Connes-Landi noncommutative two-torus with one explicit deformation parameter where Floricel-Ghorbanpour-Khalkhali Ricci density is computable in closed form), to validate the gradient-flow numerics before investing in the full SU(3) Jensen geometry. The Cacic 2014 reconstruction theorem provides the right mathematical context for such a toy.

## Round 2 — spectral-geometer

**Date**: 2026-04-27. **Agent**: spectral-geometer. **Method**: read Round 1 in full; queried `mcp__knowledge__` for canonical constants (`tau_fold = 0.19`, `S_fold = 250360.677`, `dS_fold = +58672.80`, `d2S_fold = 317862.85`, `M_KK = 7.43e16`), prior level-crossing structure (S44, S45, S52), eigenvalue-perturbation infrastructure (Hellmann-Feynman across S43/S64, Z_spectral = 74,731 at fold from S42), and dressed-functional precedents (S65, S72 BCS-dressed SA; S63 Gilkey one-loop; S84 W8a-90). Verified Connes-Landi / Floricel-Ghorbanpour-Khalkhali / Dong-Khalkhali-vanSuijlekom citations via `mcp__paper-search__`. Two structural claims are anchored by `mcp__sage__` symbolic computation (substitution chains 1 and 2 below).

### Independent of Round 1: confirm or refine Q1-Q5

I begin by re-deriving a structural fact that subtly shifts Round 1's Q3-Q4 picture, then address the five sub-questions.

**Spectral action smoothness through eigenvalue crossings** (Sage-verified, substitution chain 1 below). Round 1 Q3-Q4 invoke the canonical S84 W8a-85 verdict `dS/dτ|_{τ=0.19} = -2.04×10⁴` for the Gaussian cutoff and `+5.87×10⁴` for the absolute-value cutoff. From a heat-kernel standpoint, the *spectral action itself* is C^∞ in τ on the open Jensen interval [0,1] **even at τ-values where eigenvalues cross** (S45 documents a TRUE crossing T3-T5 at τ = 0.19104 with Δ_min = 3.27×10⁻⁵, and an avoided crossing B1-B2 at τ = 0.10670 with gap 0.154 M_KK; per `tools/knowledge.db` `[NEW S45] Van Hove TRUE crossing T3-T5` + `s52_msw_transit.py` records). The spectral action is a *symmetric* function of the eigenvalue multiset, and symmetric functions are smooth where ordering changes are not. Round 1's W8a-85 dS/dτ value is therefore physically correct and fully reflects the smooth-but-monotonic nature of `S_spec(τ)` near the fold — there is no spectral non-smoothness to worry about at the τ_fold scan range.

### Q1 (heat-kernel revisited). Differentiability of `S_spec(τ) = Σ_n f(λ_n²(τ)/Λ²)` on `τ ∈ [0,1]`

**Structural answer: `S_spec(τ)` is C^∞ (real-analytic when f is real-analytic) on the OPEN interval `τ ∈ (0,1)`, including at the τ-values of true and avoided eigenvalue crossings. Boundary singularities at τ = 0 (bi-invariant limit, where Jensen amplitude `α(τ) = e^{2τ/3}` has well-behaved derivatives but the metric coefficients change rank-of-isometry) and τ → 1 (Jensen interval boundary) are separate concerns and are not relevant on the simulator scan window.**

#### Substitution chain 1 — symmetric-function smoothness across eigenvalue crossings

Step 1 (definition). The Jensen-deformed Dirac operator `D_K(τ)` is a smooth (real-analytic in τ) family of self-adjoint operators on the fixed Hilbert space `H = L²(SU(3), S)` because the metric coefficients `g₁(τ) = e^{-4τ/3}`, `g₂(τ) = e^{2τ/3}` (canonical Jensen) are real-analytic in τ and enter the Dirac operator linearly through the frame-spin connection.

Step 2 (Rellich-Kato theorem). For any analytic family `D_K(τ)` of self-adjoint operators, the eigenvalues admit a labelling `{μ_n(τ)}_{n∈ℤ}` such that **each `μ_n(τ)` is real-analytic in τ on (0,1)** — even at degeneracy points where two analytic branches `μ_i(τ)` and `μ_j(τ)` cross. The "ordered" eigenvalue functions `λ_min(τ) ≤ λ_2(τ) ≤ ...` need NOT be smooth at crossings (only Lipschitz), but the *unordered* analytic branches `{μ_n(τ)}` are. (Reference: Kato, *Perturbation Theory for Linear Operators*, II §6 and VII §3; this is precisely what makes Hellmann-Feynman valid block-by-block in the project's S43/S64 infrastructure.)

Step 3 (Sage symbolic verification). Take a 2-mode toy: `λ₁(τ) = a + bτ`, `λ₂(τ) = c + dτ` with `b ≠ d`. Then `S(τ) = f(λ₁²) + f(λ₂²)`. Differentiating:
```
S(τ)      = f((bτ+a)²) + f((dτ+c)²)
dS/dτ     = 2(bτ+a) b f'((bτ+a)²) + 2(dτ+c) d f'((dτ+c)²)
d²S/dτ²   = 4(bτ+a)² b² f''((bτ+a)²) + 4(dτ+c)² d² f''((dτ+c)²)
            + 2 b² f'((bτ+a)²) + 2 d² f'((dτ+c)²)
```
At the crossing `τ_c = (c−a)/(b−d)` we get `λ₁(τ_c) = λ₂(τ_c) = (bc−ad)/(b−d)`, and `S(τ_c) = 2 f(((bc−ad)/(b−d))²)`. All derivatives exist; no branch points in `S` despite the eigenvalue ordering swap.

Step 4 (direction). The S45 T3-T5 true crossing at τ = 0.19104 (Δ_min = 3.27×10⁻⁵) and S52 B1-B2 avoided crossing at τ = 0.10670 (gap 0.154 M_KK) **do not introduce non-smoothness in `S_spec(τ)`**. They are visible only in *ordered* trajectory plots (mode-by-mode tracking, S44/S45 "T3-T5 NEAR-CROSSING" diagnostic) and in *finite-dimensional* projections (S52 MSW two-level Stokes analysis). The spectral action functional `Σ f(λ²)` is blind to ordering.

Step 5 (conclusion). For the simulator's purposes, `S_spec(τ)` is C^∞ on the entire scan window `τ ∈ [0.05, 0.50]`. **Smoothness is not the obstruction to D2(a)**. The S45 crossing IS structurally important (it is the van Hove fold transit signature), but it does not break gradient flow per se.

**Caveat (important for Level B0 toy)**: in the Connes-Landi NC two-torus toy mentioned in Round 1's Caveat 4, the deformation parameter is the noncommutativity θ. Floricel-Ghorbanpour-Khalkhali (1612.06688) and Dong-Ghorbanpour-Khalkhali (1808.02977 for the 3-torus case) compute the Ricci density in closed form via Connes pseudodifferential calculus, but the deformation of D itself moves through a *family* of spectral triples whose Dixmier-trace-defined "Ricci flow" `dD/dt = −Ric(D)` has not been written down. Crossings on the NC torus are similarly invisible to the spectral action and similarly visible to mode-by-mode trajectories.

### Q2. Heat-kernel asymptotic and cutoff-function effects on differentiability

**Structural answer: the heat-kernel/Seeley-DeWitt expansion `S_spec ~ Σ_k a_{2k}(τ) Λ^{4-2k}` (CC96 eq 2.11; for d=8 manifolds, the relevant coefficients are `a_0, a_2, a_4` plus log corrections at `a_4`) makes `S_spec` *manifestly smooth in τ* in the small-`t = 1/Λ²` (UV) regime, since each `a_{2k}(τ)` is a polynomial in curvature invariants of the metric `g(τ)`, which is real-analytic in τ. The choice of cutoff function `f` does not introduce branch points or discontinuities; it changes the *moments* `f_k = ∫₀^∞ x^{k−1} f(x) dx` that multiply the coefficients, but `f`-smoothness preserves `S_spec`-smoothness. The S42 vs S84 W8a-85 cutoff disagreement (`dS_fold = +5.87×10⁴` for absolute-value vs `−2.04×10⁴` for Gaussian) reflects different *moments*, not a differentiability defect.**

Substitution chain. Step 1 (definition, regulator-pin discipline). For positive cutoff function `f: ℝ_≥0 → ℝ_≥0`, `f ∈ S(ℝ)` (Schwartz class for Gaussian; integrable for absolute-value variant), the heat-kernel coefficients `a_{2k}^{ζ}(τ) = (4π)^{−d/2} ∫_M tr(P_{2k}[R, ∇R, ...; g(τ)]) dvol_g(τ)` are smooth functions of τ via real-analyticity of `g(τ)`. Step 2 (substitution). `S_spec(τ; f, Λ) = Σ_k f_k a_{2k}(τ) Λ^{d-2k}` where `f_k = (1/Γ(k))∫₀^∞ x^{k-1} f(x) dx` (Mellin moments; CC96 §2). Step 3 (simplification). `dS_spec/dτ = Σ_k f_k (da_{2k}/dτ) Λ^{d-2k}`. Each `da_{2k}/dτ` is well-defined (analytic τ-dependence of curvature invariants); the sum converges absolutely under `f ∈ S(ℝ)`. Step 4 (direction). For Gaussian `f(x) = e^{-x}`: `f_k = Γ(k) / Γ(k) = 1`, all moments are 1. For abs-value `f(x) = (1−x)_+`: `f_0 = 1/2, f_2 = 1/12, f_4 = 0` (truncated polynomial Mellin moments). The two cutoffs disagree in the *coefficient-by-coefficient weighting*, hence dS_fold disagrees in numerical value AND sign, but BOTH are smooth in τ. Step 5 (conclusion). Cutoff-function choice changes the *effective functional* (different `f` = different physics) but does NOT change differentiability class. **Both the Gaussian `−2.04×10⁴` and the abs-value `+5.87×10⁴` confirm `S_spec(τ)` is monotonic in τ near τ_fold; they disagree only on the SIGN of the slope, which is a regulator-pin artifact** (per `.claude/rules/regulator-pin-discipline.md`, regulator must be pinned).

**Implication**: For D2(a), the simulator's verdict `τ → τ_fold` would depend on the choice of `f`. For Gaussian, `dS/dτ < 0` at τ = 0.19, so first-order gradient flow `dτ/dt = −δS/δτ` drives τ → 1 (boundary). For absolute-value, `dS/dτ > 0`, so flow drives τ → 0 (boundary). NEITHER reaches τ_fold from the bare functional. **The simulator's verdict is regulator-dependent and does not converge to τ_fold under either cutoff** — confirming Round 1 Q3-Q4 structurally.

### Q3. Right "coordinate" on moduli; Hessian-as-metric-source at non-critical τ_fold is degenerate

**Structural answer: Jensen `τ` is a perfectly good *parameter*, but the question of what *metric* on `M_Jensen` it carries is not settled by the spectral action principle. Round 1 Q2 already established this. The additional finding from heat-kernel geometry: at a NON-CRITICAL point (τ_fold per S84 W8a-85 FAIL), the Hessian `∂²S/∂τ²|_{τ_fold} = d2S_fold = 3.18×10⁵` is NOT a coordinate-invariant tensor and therefore CANNOT serve as a canonical metric source.**

#### Substitution chain 2 — Hessian-at-non-critical-point fails covariance

Step 1 (definition of metric). A Riemannian metric on the 1-D moduli `M_Jensen` is a smooth positive scalar `G_{ττ}(τ)` satisfying `G_{τ'τ'}(τ') = G_{ττ}(τ) (dτ/dτ')²` under reparametrization `τ' = φ(τ)`.

Step 2 (substitution: chain rule for Hessian under reparametrization). Let `τ = φ(u)`, so `S(u) = S(φ(u))`. Then `dS/du = (dS/dτ)(dτ/du)`, and
```
d²S/du² = (d²S/dτ²)(dτ/du)² + (dS/dτ)(d²τ/du²)
```
Sage verification (substitution chain 2): the explicit symbolic differentiation yields exactly this form, with the extra term `(dS/dτ)(d²τ/du²)` confirmed nonzero when `dS/dτ ≠ 0`.

Step 3 (simplification). The transformation rule for `d²S/dτ²` therefore requires the second term `(dS/dτ)(d²τ/du²)` to vanish for covariance. This holds **iff** either (a) `dS/dτ = 0` (critical point — Morse Hessian is then a tensor, the standard fact) OR (b) `d²τ/du² = 0` (linear reparametrization only — restricts the diffeomorphism class).

Step 4 (direction at τ_fold). At τ_fold, the canonical S42 absolute-value computation gives `dS_fold = +5.87×10⁴` and the S84 W8a-85 Gaussian gives `dS/dτ = −2.04×10⁴`. *Both are nonzero*, so τ_fold is a NON-CRITICAL point under both regulators. The Hessian `d2S_fold = 3.18×10⁵` is NOT covariant under nonlinear reparametrization at τ_fold. Therefore it cannot be the metric on M_Jensen.

Step 5 (conclusion). The natural NCG-internal candidate metric — Bogoliubov-Kubo-Mori (BKM) on states (Round 1 caveat 2, Chamseddine-Connes-vanSuijlekom 1809.02944 + Dong-Khalkhali-vanSuijlekom 1903.09624) — is not derivable from `S_spec` alone in any canonical way. Round 1 was therefore correct that Riemannian-metric supply is external to NCG axioms; the heat-kernel angle adds the further fact that the *naive* candidate (Hessian at the empirical fold) FAILS the covariance test by Sage-verified construction.

**Practical implication for D2(a)**: Without a canonical metric, the simulator's "first-order gradient flow `dτ/dt = −δS/δτ`" implicitly assumes `G_{ττ} = 1` (Euclidean parametrization in the τ chart). This is a *coordinate choice*. Different parametrizations of the same Jensen family (e.g. `τ = α(g₁/g₂)` vs. `τ = log(g₁/g₂)`) give DIFFERENT first-order flows with DIFFERENT non-equilibrium trajectories (though the same set of critical points, as required by the spectral action principle). The gate "τ converges to τ_fold" is thus reparametrization-dependent.

### Q4. Numerical stability at L_max=10; realistic timestep for symplectic Verlet

**Structural answer: Numerical stability is NOT the bottleneck. The 1-D τ dynamics reduces to a scalar ODE in τ after computing `dS/dτ` once per timestep from the spectral data; the multi-eigenvalue structure does not enter as multi-mode stiffness because the UV cutoff `f` exponentially suppresses high-`λ_n` contributions. Realistic timestep `dt ≈ 10⁻⁴` to `10⁻²` in M_KK^{-1} units depending on kinetic-mass choice. The dominant cost is the eigenvalue solve (O(few minutes per τ on AMD RX 9070 XT GPU at L_max=10), NOT integrator stability.**

Substitution chain. Step 1 (definition). Symplectic Verlet for `M·ddot{τ} + γ·dot{τ} = −dS/dτ`: stability requires `dt < 2/ω_max` where `ω_max = √(d²S/dτ²/M)` is the natural frequency. Step 2 (substitution). At τ_fold, `d2S_fold = 3.18×10⁵` (canonical, S42, abs-cutoff convention, not regulator-pinned). Step 3a (M = 1, dimensionless choice): `ω_max = √(3.18×10⁵) ≈ 564 M_KK`, so `dt_max ≈ 2/564 ≈ 3.5×10⁻³ M_KK^{-1}` and `dt_safe ≈ 0.1/564 ≈ 1.8×10⁻⁴ M_KK^{-1}`. About 5500 steps per fold-transit timescale (`τ ~ 0.05` → `0.50` is 0.45 of τ; with Verlet ~5500 dt → ~5500 eigenvalue solves). Step 3b (M = Z_42 = 74,731 — physical choice from S42 `Z_spectral`-as-kinetic-mass): `ω_max = √(3.18×10⁵/74,731) ≈ 2.06`, `dt_safe ≈ 0.05`, ~20 steps per transit — trivial. Step 4 (UV cutoff suppression of high-λ stiffness). At L_max=10, max `|λ_n|` ≈ 10 in M_KK units; for Gaussian `f(x) = exp(-x)` with Λ ≈ M_KK, the modes at `λ ≈ 10` contribute `exp(-100) ≈ 3.7×10⁻⁴⁴` to `S_spec` — completely IR-irrelevant. **The "stiff modes" simply do not contribute** to `S_spec(τ)` or `dS/dτ`. Step 5 (direction). The eigenvalue cost dominates over integrator stability. Per `session-86-plan-w3.md` and `session-84-plan-w8a.md`: full L_max=10 spectrum on AMD RX 9070 XT GPU via `torch.linalg` is feasible (cached in current pipeline at ~minutes per τ). For 5500 inner iterations per fold transit, total compute is ~1 day on the GPU. For 20 iterations (M = Z_42 choice), total is ~1 hour. Both feasible.

**Caveat (recovered from S64 + S43 infrastructure)**: the Hellmann-Feynman shortcut `dλ_n/dτ = ⟨ψ_n | dD_K/dτ | ψ_n⟩` exists in the project codebase (s43_adiabaticity.py, s64_chirality_selection.py); using HF to compute `dS/dτ = Σ_n f'(λ_n²/Λ²)·(2 λ_n/Λ²)·⟨ψ_n|dD_K/dτ|ψ_n⟩` from a SINGLE eigenvalue solve per τ avoids the two-solve finite-difference cost of Q5. (See Q5.)

**Implication**: Numerical-stability gate for D2(a) is GREEN. The mathematical and NCG gates remain RED (Round 1, Q1-Q5). The simulator could be CODED stably; what it COMPUTES would still be regulator-dependent + metric-arbitrary.

### Q5. Adjoint vs finite-difference computation of `δS_spec/δτ` at L_max=10 GPU

**Structural answer: Adjoint via Hellmann-Feynman is the correct method; `torch.func.jacrev` over the spectral-action function reduces to it on a self-adjoint problem. Finite-difference (two eigenvalue solves at τ ± Δτ) is roughly 2× more expensive but avoids the requirement that `D_K(τ)` and the spectral action be in differentiable form within `torch.func`. RECOMMEND: Hellmann-Feynman applied analytically to the spectral action (as the project's S43/S64 codebase already does), not torch autograd, because the Dirac operator construction at L_max=10 involves combinatorial/integer-arithmetic representation-theoretic data structures that are not natively differentiable.**

Substitution chain. Step 1 (definition). For `D_K(τ)` self-adjoint with eigenpairs `(λ_n(τ), |ψ_n(τ)⟩)` and `D_K|ψ_n⟩ = λ_n|ψ_n⟩`, Hellmann-Feynman (Kato Perturbation II §6) gives `dλ_n/dτ = ⟨ψ_n | dD_K/dτ | ψ_n⟩` for non-degenerate eigenvalues. At degenerate eigenvalues (true crossings, S45 T3-T5), one uses the within-degenerate-subspace diagonalization of `dD_K/dτ` (standard first-order degenerate perturbation theory). Step 2 (substitution). `S_spec(τ) = Σ_n f(λ_n²/Λ²)`, so `dS_spec/dτ = Σ_n f'(λ_n²/Λ²)·(2λ_n/Λ²)·(dλ_n/dτ) = Σ_n f'(λ_n²/Λ²)·(2λ_n/Λ²)·⟨ψ_n|dD_K/dτ|ψ_n⟩`. **Single eigenvalue+eigenvector solve per τ** (the eigenvectors are needed; eigvals-only solve is insufficient). Step 3 (substitution: `dD_K/dτ` operator). Construct `dD_K/dτ` analytically by differentiating the metric coefficients `g₁(τ) = e^{-4τ/3}, g₂(τ) = e^{2τ/3}` and the corresponding frame/spin connection contributions. This is a *fixed* sparse operator (same matrix structure as `D_K`, different numerical entries) — the project's `s43_adiabaticity.py` already builds it. Step 4 (cost comparison at L_max=10):
- **Hellmann-Feynman adjoint**: 1 × eigvalsh+eigvecs solve at τ (∼O(N³) with N=155,984 dense — but exploit `torch.linalg.eigh` block-by-Schur structure since `D_K` is block-diagonal across u(2)-isotypic sectors; effective block sizes are O(few×10³) to O(few×10⁴), GPU-feasible). Adds 1× sparse-vector operation `⟨ψ_n|dD_K/dτ|ψ_n⟩` per eigenvalue. **Total: ∼1 GPU eigh solve.**
- **Finite difference**: 2 × eigvalsh-only solves at τ ± Δτ. **Total: 2 GPU eigvalsh solves** (cheaper per solve since no eigenvectors, but 2 of them).
- `torch.func.jacrev`: would require `D_K(τ)` and `eigh(D_K(τ))` to be in autograd-traced form. `torch.linalg.eigh` IS differentiable in PyTorch — but the construction of `D_K(τ)` from representation-theoretic Casimir lookups + group-theoretic 6j-symbol contractions is NOT natively differentiable (involves integer-indexing of pre-computed tables). Wrapping the metric-coefficient τ-dependence in a torch tensor and re-tracing the sparse-operator assembly per τ is feasible but adds ~30% overhead vs. Hellmann-Feynman applied to a hand-built `dD_K/dτ`.

Step 5 (direction). **For the simulator, use Hellmann-Feynman with analytic `dD_K/dτ`**, exploiting the project's existing infrastructure (`s43_adiabaticity.py` builds it correctly per S52 W2 audit). This is the lowest-cost, highest-numerical-stability route at L_max=10. `torch.func.jacrev` is a fallback for a Level B0 toy where the Dirac operator is small and assembly is differentiable. Finite difference is a third-line cross-check.

### Engagement with Round 1's caveats

**Caveat 1 (dressed functional)**. From a heat-kernel standpoint, smooth dressing of the bare spectral action — `S_dressed(τ) = S_spec(τ) + S_BCS(τ) + S_GGE(τ) + Σ_loop` — preserves smoothness of the τ-derivative IF AND ONLY IF each dressing term is smooth in τ. The candidates:
- **S_BCS(τ)**: BCS condensation free energy `−(1/2) Δ²/g` with `Δ(τ)` solving a self-consistency gap equation `Δ = g·∫ν(E)·tanh(βE/2)·(Δ/E)·dE`. The gap function `Δ(τ)` is smooth in τ where the spectral density `ν(E; τ)` is smooth and the gap is non-vanishing. At a *quantum critical point* (Δ → 0), `S_BCS` is generically C^1 but not C^2 (square-root cusp from the BCS singularity). The S65/S72 BCS-dressed SA work confirms `Δ_BCS(τ)` is smooth across τ_fold per cached infrastructure. So this dressing piece is C^∞ on the simulator window.
- **S_GGE(τ)**: Generalized Gibbs ensemble entropy `−Σ_n β_n λ_n` (Lagrange-multiplier form). Smoothness in τ inherits from smoothness of {λ_n(τ)}, which is C^∞ per Q1.
- **Σ_loop (Gilkey one-loop)**: per S63 `s63_gilkey_oneloop.py`, the one-loop correction `S_1loop` is computed in the tree eigenbasis. It involves traces of operator products; smooth where `D_K(τ)` is smooth.

**Heat-kernel reality check on dressing-shift mechanism**: for the dressing to move the extremum to τ_fold, we need `dS_BCS/dτ + dS_GGE/dτ + dΣ_loop/dτ ≈ +2.04×10⁴` at τ_fold (Gaussian) to cancel the bare gradient. The S72 BCS-dressed correction `δn_s = 3.8×10⁻⁶` and S63 spin-curv ratio 1.32% suggest dressings are small (∼1% level). **Closing the 2×10⁴ bare gradient via small corrections is structurally implausible without a fine-tuning mechanism**. This is a heat-kernel mathematical remark, not a final verdict — the program is OPEN per S84 W8a-90, but the burden of proof on the dressing is heavy.

**Caveat 2 (BKM metric)**. Dong-Khalkhali-vanSuijlekom 1903.09624 extend Chamseddine-Connes-vanSuijlekom 1809.02944 with explicit *modified-Bessel-function* spectral coefficients for the BKM metric `g^{BKM}_{ρσ}(ω) = ⟨A; B⟩_ω := ∫₀¹ tr(ω^s A* ω^{1-s} B) ds` on states `ω` of a spectral-triple second-quantized algebra. **Restricting BKM to the 1-parameter Jensen family**: one would need to (a) construct a state `ω_τ` on the second quantization of `(A, H, D_K(τ))` for each τ, (b) lift the Jensen deformation to a tangent vector in state space, (c) evaluate `g^{BKM}` along that tangent. (a) is plausible (use the Gibbs state of the spectral action functional itself, which has an interpretation as von Neumann entropy of the Fock state per S52 `s52_jacobson_multi_t.py`). (b)-(c) are unwritten research. **This is not a derivation; it is a research program. RESEARCH-GAP**.

**Caveat 3 (empirical τ_fold)**. From a heat-kernel standpoint, for τ_fold to *become* a critical point of some functional, one of three structural modifications is needed:
1. **Add a smooth constraint term** `S_constraint(τ) = (μ/2)(τ − τ_fold)²` (a Lagrange-multiplier or Tikhonov regularization). Then `d/dτ[S_spec + S_constraint]|_{τ_fold} = dS_spec/dτ + 0 = dS_fold ≠ 0` UNLESS μ → ∞ (rigid pinning) or `dS_fold` is matched by exactly chosen `μ`. *This is not "letting the dynamics produce τ_fold"; it is hard-coding τ_fold and asking the dynamics to reproduce the input*. Tautological.
2. **Add dressing** (Caveat 1) sufficient to cancel `dS_fold ≈ 2×10⁴`. As noted, structurally implausible at the percent-level dressing scales already known.
3. **Replace the metric on M_Jensen** with a non-trivial `G_{ττ}(τ)` such that the *gradient* `G^{ττ} dS/dτ = 0` at τ_fold. This requires `G^{ττ}(τ_fold) = 0`, i.e., a *degenerate* metric at τ_fold — but a degenerate metric is not a Riemannian metric, and the gradient is undefined. **Not a viable mathematical option**.

**Caveat 4 (Connes-Landi NC two-torus toy)**. The Floricel-Ghorbanpour-Khalkhali 1612.06688 Ricci density on the curved noncommutative two-torus IS computed in closed form for the conformal-perturbation case (their main theorem). The deformation parameter is the conformal factor `e^h` (Weyl rescaling) of the modular spectral triple. **However**: a *gradient flow* on this moduli is NOT yet written down in the literature (Fathizadeh-Khalkhali 1901.07438 explicitly notes "Ricci flow on noncommutative manifolds remains an open problem"). The toy is therefore valuable as a NUMERICAL TESTBED for a hand-constructed gradient flow `dD/dt = −Ric(D)/G_BKM`, but the construction itself is the research deliverable, not a literature import. **Concrete advice for Level B0 PoC**: the Connes-Landi NC two-torus has spectral triple dim = 2, eigenvalue spectrum analytically known (Bochner-Weitzenboeck for the modular Laplacian), `Ric(D)` in closed form per FGK. A gradient-flow simulator can be constructed and validated against analytically-known fixed points (the flat metric is a fixed point of `dD/dt = −Ric(D)`). This is a 2-week effort, not 1 month.

### Heat-kernel + spectral-rigidity assessment of D2(a) viability

The mathematical landscape for D2(a) breaks into three regimes:

| Regime | Differentiability | Metric on M | Critical point at τ_fold? | D2(a) viable? |
|:---|:---:|:---:|:---:|:---:|
| Bare `S_spec`, Gaussian, G=Euclidean | C^∞ | postulated G=1 | NO (S84 W8a-85 FAIL) | NO |
| Bare `S_spec`, abs-value, G=Euclidean | C^∞ | postulated G=1 | NO (S42 dS_fold = 5.87×10⁴ ≠ 0) | NO |
| Bare `S_spec`, any cutoff, G=BKM-restricted | C^∞ | RESEARCH GAP | UNKNOWN | RESEARCH-GAP |
| Dressed `S_dressed`, any cutoff, G=Euclidean | C^∞ if dressings smooth | postulated G=1 | OPEN per S84 W8a-90; structurally implausible | RESEARCH-GAP |
| Dressed `S_dressed`, any cutoff, G=BKM | C^∞ | RESEARCH GAP | RESEARCH GAP | RESEARCH-GAP |
| Toy NC two-torus, Floricel et al. | C^∞ | use BKM or Hilbert-Schmidt | analytic fixed point at flat metric | YES (toy) |

The toy NC two-torus is the only regime where a complete mathematical license can be assembled today. For SU(3) Jensen, ALL routes are research-gap.

### Verdict — heat-kernel mathematics on D2(a)

The heat-kernel/spectral-geometry mathematics confirms Round 1's structural conclusion (D2(a) is not licensed by existing infrastructure on the bare spectral action) and adds two new structural facts:

1. **(positive)**: differentiability of `S_spec(τ)` is NOT the obstruction. The spectral action is C^∞ on the open Jensen interval even at true and avoided eigenvalue crossings. Numerical stability is NOT the obstruction either. The simulator CAN be coded; what it COMPUTES is regulator-dependent and metric-arbitrary.
2. **(negative)**: at non-critical τ_fold, the Hessian `d2S_fold = 3.18×10⁵` is NOT a covariant tensor under reparametrization (Sage substitution chain 2). It cannot serve as a canonical metric on M_Jensen. Any metric on Jensen moduli must come from a separate construction — either BKM lifted from state space (Caveat 2, research gap), or from a dressed functional Hessian at a hypothetical critical point (Caveat 1, research gap).

The Connes-Landi NC two-torus toy IS mathematically license-able as a Level B0 testbed: closed-form Ricci density (Floricel-Ghorbanpour-Khalkhali 1612.06688), analytic fixed point (flat metric), small spectrum, fast simulation, NCG-internal moduli structure. **For the SU(3) Jensen Level B1, the bare-spectral-action D2(a) is mathematically NOT-LICENSED-MATH; some dressed/BKM-metric combination MIGHT license it but every component of that combination is currently a research gap.**

**Round 2 verdict**: RESEARCH-GAP-MATH — `S_spec(τ)` is C^∞ across the relevant τ-window (including S45 T3-T5 true crossing) and numerically stable to integrate at L_max=10 GPU, but the bare spectral action is non-stationary at τ_fold under both Gaussian and abs-value cutoffs, the Hessian-at-non-critical-τ_fold is reparametrization-non-covariant and cannot be the moduli metric, and the canonical NCG candidates for a moduli metric (BKM lifted from states; dressed-functional Hessian at a hypothetical critical point) are unwritten research. The Connes-Landi NC two-torus toy with Floricel-Ghorbanpour-Khalkhali Ricci density is the only mathematically license-able Level B0 testbed today.

**Concrete mathematical work needed to close the gap (for Round 3 + synthesis targets)**:

1. **Regulator-pin the bare functional**: choose a canonical `f` (Gaussian per S77 baseline) and compute `dS/dτ` over fine τ-grid `[0.05, 0.50]` with the Mellin moment convention `f_k = Γ(k)/Γ(k) = 1`. Confirm sign + monotonicity across the window. This is a 1-day computation; closes the cutoff-disagreement ambiguity.

2. **Compute `a_n(τ)` of the dressed functional `S_dressed = S_spec + S_BCS + S_GGE + Σ_Gilkey-loop` on Jensen interval**: extends the existing S65/S72/S63 BCS+GGE+Gilkey infrastructure with explicit τ-derivative on a dense τ-grid. Verifies whether dressed `dS_dressed/dτ|_{τ_fold} = 0` is achievable. *Verifying or falsifying* the dressed-functional-extremum hypothesis is essential; per S84 W8a-90 OPEN status it is currently the most material gap. ∼2-3 sessions.

3. **Construct BKM metric restriction to 1-parameter Jensen family**: lift Dong-Khalkhali-vanSuijlekom 1903.09624 BKM metric on states of the second-quantized spectral triple to a metric `G^{BKM}_{ττ}(τ)` on `M_Jensen`. Requires (a) constructing the Gibbs state `ω_τ = e^{-βH(τ)}/Z(τ)` from the spectral action, (b) evaluating `g^{BKM}(δD_K/δτ, δD_K/δτ)` = ∫₀¹ tr(ω_τ^s ⟨ψ_n|dD_K/dτ|ψ_n⟩ ω_τ^{1-s} ⟨ψ_n|dD_K/dτ|ψ_n⟩) ds at the relevant tangent vector. ∼3-4 sessions; requires a dedicated NCG-mathematical workshop.

4. **Level B0 toy**: implement gradient flow `dD/dτ = −Ric(D)/G_BKM` on the Connes-Landi NC two-torus with Floricel-Ghorbanpour-Khalkhali Ricci density. Validate against analytically known fixed point (flat metric). ∼2 weeks. This is the FIRST simulation step that does not require a research breakthrough.

5. **Hellmann-Feynman + analytic `dD_K/dτ` infrastructure consolidation**: package the existing s43/s64 HF code into a callable `compute_dS_dtau(tau, f, Lambda)` that the simulator harness can call once per timestep. ∼1 day.

If items 1, 2, 3 produce structurally favorable answers (regulator pinned + dressing closes 2×10⁴ gap + BKM metric well-defined), then D2(a) becomes LICENSED-MATH-WITH-CAVEATS and Level B1 simulator launch is supported. If item 2 fails (dressing does not shift extremum to τ_fold) or item 3 hits a fundamental obstruction, then D2(a) is NOT-LICENSED-MATH in any extension, and Level B1 should pursue a different dynamics rule (Wheeler-DeWitt / q-theory / external phase-space construction) — Round 3 territory.

## Round 3 — volovik-superfluid-universe-theorist

**Date**: 2026-04-27. **Agent**: volovik-superfluid-universe-theorist. **Method**: read Round 1 (NOT LICENSED) and Round 2 (RESEARCH-GAP-MATH) in full; surveyed the Volovik corpus (`researchers/Volovik/`) — Klinkhamer-Volovik q-theory founding papers (#13 hep-th/0711.3170, #14 0811.4347, #21 1812.07046), Volovik's vacuum-energy thermodynamics (#04 gr-qc/0405012, #25 1004.0597), de Sitter decay and two-fluid (#15 2312.02292, #35 2410.04392), and the Painlevé-Gullstrand / hydraulic-jump white-hole papers (#27 gr-qc/9901077, #09 physics/0508215); queried `mcp__knowledge__` for q-theory dynamical-rule traces (8 theorems, 5 closed mechanisms, 4 gates, 10 equations). Two structural sign/direction claims anchored by `mcp__sage__` symbolic computation (substitution chains 3a and 3b below). The framework's own canonical scripts that operationalize Volovik's q-theory are inspected: `s53_q_theory_gge.py`, `s57_chi_q_microscopic.py`, `s60_q_theory_geodesic.py`, `s67_volovik_q_a0.py`, `s71_cc_from_gge_residual.py`.

### Reframing acknowledgement

Round 1's structural finding — that NCG licenses dynamics of EXCITATIONS (inner fluctuations `D → D + A + JAJ⁻¹`) on a fixed spectral triple, not dynamics of the spectral triple itself — is exactly Volovik's anti-GUT inversion. In Volovik's program (Paper 25 §VII, "Vacuum as topological medium"), gauge bosons and gravity are *expansion parameters around a Fermi point*, with Green's function `G^{-1}(p_μ) = e^β_α Γ^α (p_β − p^{(0)}_β) + ...`. The vierbein `e^β_α` and gauge potential `p^{(0)}_β` are *secondary collective modes living on top of* a vacuum whose topological universality class is fixed. The vacuum *itself* — the underlying medium with its conserved charge q — does NOT undergo gradient-flow dynamics on the action; its dynamics is set by Gibbs-Duhem thermodynamic identities at equilibrium, and by impulsive scattering (Hawking, ergoregion instability, hydraulic-jump white hole) when matter perturbs it. **The Volovik corpus is the strongest external endorsement of Round 1's reframing.** I address each sub-question against this background.

### Q1. q-theory dynamical rule on the cosmological action

**Structural answer: q-theory is NOT gradient flow on `S[q]`. The equilibrium condition is a thermodynamic identity (Gibbs-Duhem), and off-equilibrium relaxation is SECOND-ORDER OSCILLATION (Newtonian dynamics on `q`) with envelope-damping driven by the Hubble expansion of the EXTERNAL spacetime — friction is sourced by cosmological time, not by an autonomous dissipation tensor on q-moduli.**

The Klinkhamer-Volovik action (Paper 13 Eq. 1, Paper 21 Eq. 7, Paper 25 Eq. 4.1a) is

```
S_eff[g_μν, q] = ∫ d⁴x √(−g) [ R/(16π G_N) + ε(q) + L_M(q,ψ) ]
```

The dynamical rule for q is obtained by *varying the spectral-triple data for q* — for the four-form realization, `q² = −(1/24) F_κλμν F^κλμν` from a three-form gauge potential A; for the elasticity-tetrad realization (Paper 21), `q = (1/4) e^μ_a E^a_μ` with `E^a_μ = D_μ X^a`. Variation produces *Maxwell-like* equations (not gradient-flow equations). Specifically (Paper 25 §IV, Paper 13 §III, Paper 21 Eq. 14):

```
∂_μ ( dε/dq ) = 0    ⇒    dε/dq = μ = const   (integration constant, NOT a derived flow)
```

This is **not** `dq/dt = −γ δS/δq`. It is a *conservation law* whose integration constant μ (chemical potential) is fixed by initial / boundary data. The equilibrium vacuum value q₀ is then determined by the Gibbs-Duhem identity:

```
ρ_vac(q) := ε(q) − q · dε/dq = ε(q) − μ q     (thermodynamic potential, NOT energy ε)
ρ_vac(q₀) = 0  in equilibrium     (Volovik's vacuum-energy theorem)
```

**Off-equilibrium dynamics**. After a perturbation displacing q from q₀, Volovik's Paper 25 §V (Eq. 5.5) gives the late-time relaxation:

```
q(t) − q₀ ~ q₀ · sin(ω t)/(ω t),     ω ~ E_Planck
ρ_vac(t) ~ (ω²/t²) · sin²(ω t)
```

#### Substitution chain 3a — q-theory dynamics is OSCILLATION, not gradient flow (Sage-verified)

Step 1 (definition). q-field equation of motion (Paper 25, four-form realization, around Minkowski background): the q-field satisfies a *Maxwell-type wave equation* `□A = 0` for the three-form A whose dual is `qε` — this is a SECOND-ORDER WAVE EQUATION, not a first-order flow.

Step 2 (Sage check on Volovik's Eq. 5.5 envelope). Define `q_pert(t) := sin(ω t)/(ω t)`. Compute `d²q_pert/dt²`: leading terms at large t are

```
d²/dt²[ sin(ωt)/(ωt) ] = − ω · sin(ωt)/t  + (lower-order corrections in 1/t²)
                       = − ω² · q_pert(t) + O(1/t²)
```

This is *Hooke's law*: `d²q/dt² = −ω² q + (subleading)`. The leading dynamics is oscillation around q₀, not exponential decay toward q₀.

Step 3 (substitution: gradient-flow comparison). A first-order gradient flow `dq/dt = −γ · dε/dq` with quadratic ε would give `q(t) = q₀ + (q(0) − q₀) e^{−γ t}` — *exponential decay, no oscillation*. Volovik's q(t) − q₀ ~ sin(ωt)/(ωt) does NOT exponentially decay; it OSCILLATES with envelope ~1/t. The two functional forms are *qualitatively distinct*.

Step 4 (simplification: source of envelope damping). The 1/t envelope is *not* autonomous dissipation on q-moduli. It is the dilution of the q-field amplitude by cosmological expansion of the external spacetime: the Hubble-friction term `3H · dq/dt` enters the q-equation of motion only when q is coupled to a Friedmann background. Volovik's Paper 13 §III explicitly notes the equilibrium is a property of q-thermodynamics independent of any dissipation mechanism; the cosmological 1/t envelope arises *because the universe expands*, not because q has its own friction.

Step 5 (direction). q-theory is **second-order Newtonian-type dynamics** (oscillator with restoring force ω² ~ E_Planck²) **+ Hubble envelope friction sourced externally**. It is **not** first-order gradient flow on `S[q]`.

**Sage verification log** (executed 2026-04-27): `d²/dt²[sin(ωt)/(ωt)]` series at large t gives leading restoring-force term `−ω² · q_pert(t)`, confirming the oscillator structure. For a generic non-Abelian gluon-condensate effective potential `ε(q) = a q + b q ln q` (Paper 14 Eq. 5.1a), `ρ_vac(q) = ε(q) − q·dε/dq = −b q`, which equals zero **only at q₀ = 0** — i.e., the Gibbs-Duhem equilibrium is set algebraically by the Lagrange multiplier μ (from `∂_μ(dε/dq) = 0`), not as a fixed point of any gradient flow.

**Citations to the variational principle explicitly**:
- Paper 13 (KV 0711.3170) Eq. (1): action `S = ∫d⁴x √(−g) [R/(16π G_N) + ε(q)]`. Eq. (4): `ρ_vac = ε(q) − q dε/dq`. Eq. (9): equilibrium `dε/dq = μ`.
- Paper 21 (KV 1812.07046) Eq. (7): full action with elasticity tetrad. Eq. (14): conservation law `dε/dq = μ`.
- Paper 25 (Volovik 1004.0597) Eq. 4.1a: full action; Eq. 5.5a: late-time oscillation; Eq. 5.6: Minkowski-attractor solution.
- Framework operationalization: `s53_q_theory_gge.py` line "d(Lambda)/dt = −3H · (Λ − Λ_eq) · (1/χ_q) · Λ" — the Hubble factor 3H is explicit; this is *cosmological friction*, not autonomous gradient flow on Λ.

### Q2. F-theory dynamical rule and source of dissipation

**Structural answer: My own "F-theory" reading of the q-field as a thermodynamic variable does NOT change the dynamical type. F-theory inherits q-theory's structure: equilibrium by Gibbs-Duhem; off-equilibrium by oscillation. Dissipation is *external*: it is sourced either by (i) Hubble expansion of the gravitational background (cosmological friction `3H · dq/dt` in Friedmann backgrounds), or (ii) energy exchange with a matter component (two-fluid hydrodynamics, Paper 35 — vacuum ↔ Zel'dovich-stiff dark matter). It is NOT sourced by an intrinsic dissipation tensor on the q-moduli space.**

The user-validated identity "q-theory is F-theory in a dress" (memory `project_qtheory-ftheory.md`; corpus citation `researchers/Volovik/14_2009_Klinkhamer_Volovik_Gluonic_Vacuum_Q_Theory.md` "Relevance" §): same variational principle (`δS/δq = 0` with conservation law `dε/dq = μ`), different language (F-theory uses thermodynamic variable q identified with the QCD gluon condensate `q = ⟨(1/4π²) G^a_μν G^{aμν}⟩`).

**F-theory dissipation source (Paper 14 §VI)**: the cosmological-constant remnant

```
Λ ~ k_Λ K³_QCD / E²_Planck ~ (3 × 10⁻³ eV)⁴
```

arises because the Hubble expansion *perturbs* the gluon condensate from its self-tuned equilibrium. The resulting `ρ_vac ~ f |H| Λ³_QCD` (Paper 14 Eq. 6.3) is **driven by H**, not by autonomous q-dynamics. When H = 0 (Minkowski equilibrium), ρ_vac = 0 exactly, and the q-field has no internal mechanism to generate dissipation.

**Two-fluid extension (Paper 35, Volovik 2024)**: dark energy (vacuum, w = −1) and gravitational dark matter (Zel'dovich stiff matter, w = +1) are the two components of the de Sitter "two-fluid system." Energy exchange between them gives both a power-law decay (Paper 35 §V.A-C) — but the energy-exchange rate is set by the de Sitter local temperature `T = H/π` (twice the Gibbons-Hawking temperature), which is *itself driven by the cosmological expansion*. Again: dissipation is *external* (sourced by H), not intrinsic to q.

This is exactly the structure Round 1 identified as MISSING from the bare spectral action: there is no autonomous dissipation tensor γ on the moduli of D_K(τ); any γ that appears in a D2(a)-style equation must be sourced externally (a Friedmann background coupling, a thermal bath of post-fold quasiparticles, or a Yo-Dawg coupling to an outer-universe Hubble parameter — none of which is in the bare NCG axioms).

### Q3. GPE Madelung dynamics — regime where Jensen-τ-like dynamics emerges

**Structural answer: GPE Madelung dynamics in real time is HAMILTONIAN (canonical pair (ρ, θ) on a symplectic phase space), NOT gradient flow. The gradient-flow analog of D2(a) corresponds to IMAGINARY-TIME GPE — which is a numerical ground-state finder, not physical dynamics. Volovik-Mineev-Salomaa superfluid-action formalism uses Lagrangian / Hamiltonian variational principles giving wave-equation dynamics for the order parameter, never gradient flow on the order parameter modulus.**

#### Substitution chain 3b — Madelung is Hamiltonian, gradient flow is ground-state finder only (Sage-verified)

Step 1 (definition). Gross-Pitaevskii equation: `iℏ ∂_t ψ = (−ℏ²/2m ∇² + V + g|ψ|²) ψ`. Madelung ansatz `ψ = √ρ exp(iθ/ℏ)`. Substitute and split real/imaginary parts.

Step 2 (substitution and simplification — real-time). The Madelung equations are
```
∂_t ρ + ∇·(ρ v_s) = 0                                       (continuity)
∂_t θ + (1/2m)(∇θ)² + V + g ρ − (ℏ²/2m) ∇²√ρ/√ρ = 0       (Hamilton-Jacobi)
```
with v_s = ∇θ/m. These are **Hamilton's equations** for the canonical pair (ρ, θ) with Poisson bracket `{ρ(x), θ(y)} = δ(x−y)`. The Hamiltonian is `H = ∫ [ρ v_s²/2m + V ρ + (g/2)ρ² + (ℏ²/8m)(∇ρ)²/ρ ]`. Sage check at 0D (zero-mode toy with H = V·ρ + (g/2)ρ²): `dH/dρ = V + g·ρ` (chemical potential), `dH/dθ = 0`; canonical equations give `∂_t θ = −dH/dρ = −μ(ρ)` (the Josephson relation) and `∂_t ρ = +dH/dθ = 0`. **This is symplectic, not gradient.**

Step 3 (imaginary-time analog). Wick-rotate `t → −iτ`. The GPE becomes `−ℏ ∂_τ ψ = (−ℏ²/2m ∇² + V + g|ψ|²) ψ`. The L² norm of ψ then *decreases monotonically* under this flow (Lyapunov: dE/dτ ≤ 0). This IS a first-order gradient flow on `E[ψ]` and IS used in numerics (the canonical BEC ground-state-finder algorithm in `phonon-exflation-sim/src/gpe_solver.py`).

Step 4 (direction). The structural identification `D2(a) (first-order gradient flow on S_spec) ↔ imaginary-time GPE` makes D2(a) a **ground-state finder for the spectral action**, *not* a dynamical-evolution rule for the substrate. This is a critical scope distinction:
- **Real-time evolution** (asks: how does τ(t) evolve from `τ_0 = 0` to `τ_fold = 0.190`?) → must be Hamiltonian / wave-equation dynamics, NOT gradient flow.
- **Ground-state search** (asks: what is the τ at the minimum of S_spec?) → CAN be gradient flow (imaginary time), but the answer is `τ → boundary of [0,1]` per Round 2 Q2 (S_spec is monotonic; no interior minimum; gradient flow runs to the boundary, not to τ_fold).

Step 5 (Volovik-Mineev-Salomaa structure). The standard superfluid-action formalism (Volovik & Mineev, *Helium-3 and Helium-4*; Salomaa & Volovik, *Rev. Mod. Phys.* 59, 533 (1987) — both cited as foundations of the framework's BCS+GGE+Leggett infrastructure in S52/S65/S70) writes the order-parameter dynamics as a *Lagrangian variational principle*:

```
L = ∫ d³x [ iA_μν ∂_t A*_μν − F[A_μν, ∇A_μν] ]   (3He-A order parameter Lagrangian)
```

where the kinetic term `iA ∂_t A*` is FIRST-ORDER IN TIME (because it's a Schrödinger-type Lagrangian for a complex order parameter), giving a *Hamiltonian* equation of motion for A (analogous to the GPE for ψ), not a gradient flow on F. Dissipation, when present (Leggett-Takagi relaxation, BCS quasiparticle scattering, etc.), is added phenomenologically via a Rayleigh dissipation function on top of the Hamiltonian, with the dissipation coefficient computed from microscopic scattering cross-sections — *not* derived as a gradient on the action moduli.

**Implication for Jensen τ**: The closest superfluid-tradition analog of D2(a) would be a **Lagrangian** for τ of the form `L_τ = (1/2) M_ττ (∂_t τ)² − V_eff(τ)`, where V_eff IS the spectral action and M_ττ is a kinetic-mass term that must be *separately constructed* (not derived from S_spec). This is the second-order ODE form `M ∂²τ/∂t² = −δV/δτ`, with friction `γ ∂_t τ` added phenomenologically. **It is structurally the second-order branch of D2(a) (`d²τ/dt² + γ dτ/dt = −δS/δτ`)**, not the first-order gradient-flow branch.

The first-order gradient-flow branch of D2(a) (`dτ/dt = −δS/δτ`) has *no analog* in the Volovik-Mineev-Salomaa superfluid-action tradition. The closest precedent — *time-dependent Ginzburg-Landau* (TDGL) for a non-conserved order parameter — IS first-order gradient flow `∂_t Δ = −γ δF/δΔ`, but TDGL is explicitly an *effective theory near T_c with a thermal bath providing γ*; it is NOT the underlying superfluid dynamics, and it has *no validity in the T → 0 limit* where the BCS condensate is non-dissipative.

### Q4. Counter-examples — substrate-action systems where gradient flow fails

**Structural answer: YES, several. The most directly relevant are (i) actions unbounded below, (ii) actions monotonic on the moduli (no interior minimum — exactly Round 1+2's S_spec(τ) situation), and (iii) acoustic white-hole / hydraulic-jump configurations where the substrate dynamics is impulsive at a horizon and gradient flow either does not apply or produces unphysical results. The Volovik tradition is explicit about how to handle each.**

**(i) Action unbounded below — q-theory's resolution**. The bare gluon condensate effective potential `ε(q) = a q + b q ln q` (Paper 14 Eq. 5.1a) is *not bounded below* on `q ∈ (0, ∞)` — it diverges to `−∞` as `q → 0+` for `b > 0`. A naive gradient flow `dq/dt = −dε/dq` would drive q to a singular boundary configuration. Volovik's resolution (Paper 13 §III, Paper 14 §V): the relevant thermodynamic potential is NOT `ε(q)` but `ρ_vac(q) = ε(q) − μ q` (Legendre transform), which IS bounded below for `χ_vac > 0` (positive vacuum compressibility). The chemical potential μ is fixed by initial/boundary data and pins the equilibrium q₀ algebraically. **The CC problem is solved by Legendre-transforming the action, not by gradient-descending it**.

**(ii) Action monotonic on the moduli — boundary-attractor behavior**. Round 1 Q3 + Round 2 Q2 already documented `S_spec(τ)` is monotonic on the explored Jensen interval (`dS/dτ` ≠ 0 throughout, regulator-independent in sign-of-magnitude). A gradient flow on a monotonic action runs to the boundary of the moduli, NOT to an interior fixed point. This is *exactly* the Volovik-Paper-25-Eq.-5.6 result: in the four-form realization, the integration constant μ is *itself* a parameter of the solution (not the action), so different initial conditions select different boundaries. Volovik's resolution is to switch to the *aether-field* realization (Paper 25 §V), where μ is NOT an integration constant and the Minkowski vacuum becomes a unique attractor — i.e., **the dynamics is changed by changing the order-parameter realization, not by adding friction to a gradient flow on the same action**.

**(iii) Acoustic white-hole / hydraulic-jump impulsive dynamics**. Volovik Paper 09 (`physics/0508215`, "The hydraulic jump as a white hole"): the circular hydraulic jump in 4He produces a 2+1D Painlevé-Gullstrand metric with a *physical singularity* at the horizon — discontinuous metric, NOT smooth gradient flow. The dynamics inside the ergoregion is *Miles instability* (Eq. 7), which is a *second-order linearized wave equation with imaginary frequency*, sourced by friction with the wall:
```
M(k)(ω − k·v)² = ρg + k²σ − iΓω
```
Gradient flow on the underlying free energy of the fluid layer would NOT produce the white-hole horizon — the white hole arises from the *advective* (Hamiltonian-symplectic) flow exceeding the local sound speed. The substrate dynamics that produces a horizon is *kinematically* impulsive, not dynamically dissipative.

The framework's own analog is the *acoustic white hole at τ_fold* documented in `s85_w6_acoustic_white_hole_formal.py` (Mach 13.75 supersonic transit through the fold; project memory `project_substrate-not-c-limited.md` formalizes this). The transit is *first-order phase-transition impulsive*, not a slow-roll attractor approach — see also project memory `project_friedmann-wrong-question.md` (S74 W1-E FAIL is informative because it confirms the CC hierarchy splits at the fold). Round 1's framing language ("first-order transit through the fold," "cold big bang vacuum floor cascade") is the project's match to Volovik Paper 09's hydraulic-jump-as-white-hole picture: the substrate's dynamics at the fold is *impulsive scattering*, not gradient-flow attractor approach.

**(iv) GGE relic that never thermalizes**. From the framework's S37/S38/S60 results (project memory `project_3heb-inheritance.md` + S60 collab review): the post-fold state is a Generalized Gibbs Ensemble that *cannot* thermalize on cosmological timescales because the substrate is integrable (BDI class, T² = +1, with infinitely many conserved charges). A gradient-flow dynamics on `S_spec` would IMPLY thermalization (because gradient flow has a Lyapunov function `S_spec` that decreases monotonically — except `S_spec` is unbounded). **Gradient flow contradicts the GGE-permanence theorem** that the project established in S38 and that I confirmed in `project_3heb-inheritance.md`. The substrate cannot be both (a) integrability-protected GGE AND (b) gradient-flow-dissipative.

### Q5. Practical assessment — is D2(a) ANALOG-licensed?

**Structural answer: NOT-ANALOG-LICENSED for the first-order gradient-flow branch (`dτ/dt = −δS/δτ`). The analog tradition (q-theory, F-theory, GPE Madelung, Volovik-Mineev-Salomaa) does NOT use first-order gradient flow on the substrate action. It uses (i) Lagrangian/Hamiltonian variational principles giving SECOND-ORDER wave-equation dynamics, (ii) Gibbs-Duhem thermodynamic identities for equilibrium, (iii) impulsive Painlevé-Gullstrand / scattering matching at horizons / first-order phase transitions, and (iv) externally-sourced friction (Hubble expansion, two-fluid energy exchange) when dissipation is present. The first-order gradient-flow ansatz is the *imaginary-time* / *ground-state-finder* analog, not a real-time dynamical law.**

**The second-order branch of D2(a) (`d²τ/dt² + γ dτ/dt = −δS/δτ`) is ANALOG-LICENSED-WITH-CAVEATS** — it matches the Lagrangian-variational tradition for the order parameter (Volovik-Mineev-Salomaa Schrödinger-type Lagrangian, Klinkhamer-Volovik wave equation for the q-field), provided:
- (a) the kinetic-mass `M_ττ` is constructed externally (not from `S_spec`), e.g., from the Bogoliubov-Kubo-Mori metric on states (Round 1 Caveat 2; Round 2 Q3) or from a Volovik-style q-compressibility `M_ττ ~ χ_q` (Paper 13 Eq. 14);
- (b) the friction `γ` is sourced externally (Hubble friction `3H` if τ is coupled to a Friedmann background; two-fluid energy exchange if there's a matter component);
- (c) the equilibrium is pinned NOT by `dS_spec/dτ = 0` (which fails per S84 W8a-85), but by a Gibbs-Duhem identity on the dressed `ρ_vac(τ) := ε(τ) − τ · dε/dτ` (which may have an interior zero at τ_fold even if ε(τ) is monotonic — this is exactly the `S83-DRESSING` open branch from Round 1 Caveat 1).

**Where the analog SUPPORTS what's already in the framework**:
- The empirical-`τ_fold` retention (Round 1 W8a-90 default fallback) is *exactly* Volovik's "integration constant μ" — `τ_fold` is the cosmological-epoch-matching analog of μ pinned by initial/boundary data, not by spectral-action stationarity.
- The "first-order transit through the fold" + acoustic-white-hole language (`s85_w6_acoustic_white_hole_formal.py`) IS Volovik Paper 09's hydraulic-jump-as-white-hole picture. The framework already uses the right analog dynamics for cosmogenesis.
- The GGE relic (Session 38, project memory `project_3heb-inheritance.md`) IS Volovik's "integrability-protected non-equilibrium vacuum" (Paper 25 §V; Paper 35 two-fluid). The framework already uses the right analog dynamics for the post-transit phase.

**Where the analog CONTRADICTS the proposed D2(a) first-order branch**:
- Gradient flow on `S_spec` is incompatible with the GGE-permanence theorem (a Lyapunov function for τ_fold would force thermalization; the substrate is BDI-integrability-protected against thermalization).
- Gradient flow runs to a boundary on a monotonic action; the empirical τ_fold is not a boundary, it's an interior point selected by epoch-matching (analog: q₀ pinned by μ).
- Gradient flow has no analog in the Volovik-Mineev-Salomaa superfluid-action tradition for the underlying order parameter; the closest match (TDGL) is an effective theory near T_c with externally-sourced thermal bath, not the substrate's own dynamics.

### Engagement with the three reframed-question candidates

The user's reframings (RQ-1: inner-fluctuation simulator on fixed `D_K(τ_fold)`; RQ-2: Λ-running via Chamseddine-Connes scale-invariance dilaton; RQ-3: phase-transition simulator across the τ_fold boundary via Bogoliubov scattering matching) map onto the analog tradition as follows.

**RQ-1: Inner-fluctuation simulator on fixed `D_K(τ_fold)` — STRONGLY SUPPORTED by analog precedent.**
This is *exactly* what Volovik's anti-GUT program does. Paper 25 §VII: gauge bosons and gravity are *expansion parameters of the Green's function around a Fermi point* — i.e., inner fluctuations of the topologically-fixed Dirac operator. A simulator that fixes `D_K(τ_fold)` (the BDI-class topological vacuum) and evolves the gauge connection A and Higgs field S on top of it is *the Volovik program in NCG language*. The variational principle is well-defined (it's the Yang-Mills + Higgs sector of the NCG SM action `Tr f(D_A²/Λ²)` per Chamseddine-Connes 0605011), the dynamics is Hamiltonian/Lagrangian (gauge field evolution), dissipation is sourced externally (cosmological background, matter coupling), and the laboratory analog is concrete: 3He-A's emergent Weyl fermions + gauge fields living on a topologically-fixed Fermi-point vacuum. **My recommendation: this is the simulator branch with the strongest analog license.**

**RQ-2: Λ-running via Chamseddine-Connes scale-invariance dilaton (CC 0512169) — PARTIALLY SUPPORTED by analog precedent.**
The dilaton field φ in Chamseddine-Connes 0512169 makes the cutoff scale dynamical: `Λ → Λ · e^φ`, with φ obeying its own equation of motion `δS_spec/δφ = 0`. This IS analog-licensed by q-theory: the Volovik gluon-condensate four-volume q (Paper 14 §II) is also a *cutoff-like* variable with a dynamical equation (Paper 14 §III), and the resulting Λ-running matches the observed CC at the right order of magnitude (Paper 14 Eq. 6.7: `Λ ~ K³_QCD/E²_Planck ~ (3 × 10⁻³ eV)⁴`). The framework already has `s14_qtheory_running_lambda.py` etc. as candidate operationalizations. *Caveat*: CC's dilaton is still a *critical-point principle* (`δS/δφ = 0`), not a flow rule — so it inherits Round 1's "no autonomous flow" caveat, and it must be coupled to a cosmological background to relax. **My recommendation: this is the simulator branch most directly aligned with q-theory dynamics, but it must include the cosmological-background coupling explicitly and treat the dilaton equation as a Maxwell-type wave equation, not gradient flow.**

**RQ-3: Phase-transition simulator across τ_fold via Bogoliubov scattering matching — STRONGLY SUPPORTED by analog precedent.**
This is *exactly* Volovik Paper 09 (hydraulic-jump white hole) + Paper 27 (Painlevé-Gullstrand black hole in 3He-A film) lifted to the SU(3) substrate. The fold transit is a first-order phase transition; the dynamics across the transit is given by *matching pre- and post-fold Bogoliubov spectra* (Eq. 3 of Paper 27, Eq. 10-11 for the tunneling action), not by gradient flow on a smooth action. The framework's own `s85_w6_acoustic_white_hole_formal.py` already implements the kinematic match; what's missing is the full Bogoliubov-coefficient calculation that yields the GGE relic occupation numbers (already partially done in S37-38 and `s52_bogoliubov_amp.npz`). The variational principle is the *transit Lagrangian* with explicit horizon discontinuity; dissipation is *kinematic* (impulsive scattering, not relaxation); the laboratory analog is *direct*: the hydraulic-jump experiment in superfluid 4He (Rolley et al., cited in Paper 09). **My recommendation: this is the simulator branch with the most laboratory-grounded analog precedent. The framework's "first-order transit" + "GGE relic" language is already this picture; building the simulator around it is just operationalizing the project's existing physical content, not adding new structure.**

### Verdict

**Round 3 verdict**: NOT-ANALOG-LICENSED — the q-theory / F-theory / GPE-Madelung / Volovik-Mineev-Salomaa tradition does NOT use first-order gradient flow on the substrate action; it uses Lagrangian/Hamiltonian (second-order, Maxwell-type wave) dynamics for the q-field with Gibbs-Duhem equilibrium pinning and externally-sourced (Hubble / two-fluid) friction, plus impulsive Painlevé-Gullstrand / scattering-matching dynamics at horizons. D2(a) as a first-order gradient flow has no analog precedent; D2(a) as a second-order Newtonian flow with externally-sourced γ is ANALOG-LICENSED-WITH-CAVEATS but requires kinetic mass M_ττ and friction γ to be constructed externally, exactly mirroring Round 1's "phase-space structure is external to NCG" finding.

**Positioning of the three reframings against analog precedent**:

| Reframing | Analog status | Closest Volovik-corpus precedent |
|:----------|:--------------|:--------------------------------|
| **RQ-1**: Inner-fluctuation simulator on fixed `D_K(τ_fold)` | **STRONGLY SUPPORTED** | Paper 25 §VII (gauge fields and gravity as expansion around Fermi point). 3He-A laboratory analog with emergent Weyl fermions + gauge fields. |
| **RQ-2**: Λ-running via CC dilaton (CC 0512169) | **PARTIALLY SUPPORTED** | Paper 14 §V-VI (gluon-condensate q-running gives `Λ ~ K³_QCD/E²_Planck`). Caveat: dilaton-eom is still critical-point principle, must couple to FRW background. |
| **RQ-3**: Phase-transition simulator across τ_fold (Bogoliubov scattering matching) | **STRONGLY SUPPORTED** | Paper 09 (hydraulic-jump as white hole) + Paper 27 (Painlevé-Gullstrand black hole in 3He-A) + Volovik 1004.0597 §V (cosmology as relaxation via impulsive dynamics). Direct laboratory analog (Rolley et al. hydraulic-jump experiment). |

The original D2(a) gradient-flow ansatz is **CONTRADICTED** by all three branches of the analog tradition. The three reframings (RQ-1, RQ-2, RQ-3) are all SUPPORTED to varying degrees, with RQ-1 and RQ-3 having the strongest analog precedent and the most direct laboratory analogs in superfluid 3He / hydraulic-jump 4He experiments. The synthesis target should pivot from D2(a) launch to selecting among RQ-1/RQ-2/RQ-3 — most likely RQ-1 (inner-fluctuation simulator on fixed `D_K(τ_fold)`) as the cleanest mathematical + analog-licensed entry point, with RQ-3 (phase-transition simulator across the fold) as the framework-native "cosmogenesis" companion that operationalizes the existing acoustic-white-hole + GGE-relic infrastructure.

## Synthesis (orchestrator)

**Date**: 2026-04-27. **Author**: orchestrator. **Method**: synthesized the three independent rounds (NCG/Connes, heat-kernel math/spectral-geometer, analog tradition/Volovik) and the user's mid-workshop reframing. All three rounds were verified on disk before synthesis.

### Combined verdict on D2(a)

| Round | Angle | Verdict | Decisive evidence |
|:------|:------|:--------|:------------------|
| Round 1 | NCG axioms | **NOT LICENSED** | τ is parameter not variable; spectral action is critical-point principle only; CCM 2007 + CC 1996-2018 + FGK 1612.06688 do not address τ-dynamics; **τ_fold not a critical point of `S_spec`** (S84 W8a-85 FAIL: dS/dτ ≈ 5×10⁴, 15 OOM above PASS) |
| Round 2 | Heat-kernel math | **RESEARCH-GAP-MATH** | `S_spec` is C^∞ across the scan window incl. S45 T3-T5 crossing (Sage chain 1); numerics GREEN; **but** Hessian-at-non-critical-fold is reparametrization-non-covariant (Sage chain 2) so cannot serve as moduli metric; dressing-shift implausible (need to close 2×10⁴ gap with 1%-level dressings); BKM-on-Jensen-restriction is unwritten research |
| Round 3 | Analog tradition | **NOT-ANALOG-LICENSED** (first-order); ANALOG-LICENSED-WITH-CAVEATS (second-order) | q-theory: `q − q₀ ~ sin(ωt)/(ωt)` oscillation, NOT exponential decay (Sage chain 3a); Madelung GPE is symplectic Hamilton, NOT gradient (Sage chain 3b); GGE-permanence (S38) **contradicts** Lyapunov function on `S_spec`; equilibrium pinned by Gibbs-Duhem identity, friction sourced externally (Hubble / two-fluid) |

### D2(a) is CLOSED for cause

Three structural reasons:

1. **NCG axioms do not produce τ-dynamics**. Inner fluctuations (gauge + Higgs) are dynamical; spectral-triple deformation parameters are not (Round 1).
2. **The proposed equilibrium fails an already-recorded gate**. S84 W8a-85 FAIL with dS/dτ at τ_fold = -2.04×10⁴ (Gaussian) / +5.87×10⁴ (abs-value), 15 OOM above PASS threshold. The simulator's equilibrium gate would either reproduce this FAIL or PASS only by importing externally-pinned τ_fold (Round 1 Q4 + Round 2 Q3).
3. **Gradient flow on S_spec contradicts the project's S38 GGE-permanence theorem**. A Lyapunov function would force thermalization on a BDI-integrability-protected substrate (Round 3 Q4(iv)).

D2(a) is therefore closed by the workshop. The closure status is:

```
D2(a) (gradient flow on bare S_spec[τ]): BLOCKED
  - NCG license: ABSENT (Round 1)
  - Math license: GAP (Round 2)
  - Analog license: ABSENT for first-order, CONDITIONAL for second-order (Round 3)
  - Cross-check: contradicts S38 GGE-permanence theorem (Round 3 Q4(iv))
```

### The user's "wrong question" reframing is validated

The mid-workshop reframing — that the framework licenses dynamics of EXCITATIONS on a fixed spectral triple, not dynamics of the spectral triple itself — is endorsed by all three reviewers:

- Round 1 (Connes): "the fields that ARE dynamical in standard NCG-SM treatment are inner fluctuations `D → D + A + JAJ⁻¹`, not deformation parameters"
- Round 2 (spectral-geometer): the Connes-Landi NC two-torus toy IS license-able as a Level B0 testbed (closed-form Ricci density per FGK 1612.06688)
- Round 3 (Volovik): "Round 1's structural finding is exactly Volovik's anti-GUT inversion. Gauge bosons and gravity are expansion parameters around a Fermi point... the framework already uses the right analog dynamics for cosmogenesis (acoustic white hole, GGE relic)"

### Three reframed-question candidates ranked by combined license

| Candidate | Round 1 (NCG) | Round 2 (math) | Round 3 (analog) | Combined |
|:---|:---:|:---:|:---:|:---|
| **RQ-1** Inner-fluctuation simulator on fixed `D_K(τ_fold)` (gauge + Higgs evolution per CC 0605011) | LICENSED (standard NCG-SM dynamical content) | LICENSED (existing infrastructure handles `D_K(τ_fold)`; YM+Higgs eom mathematically standard) | STRONGLY SUPPORTED (Volovik #25 §VII = literal description) | **STRONGEST PIVOT TARGET** |
| **RQ-3** Phase-transition simulator across τ_fold (Bogoliubov scattering matching) | LICENSED (impulsive scattering does not require τ-evolution dynamics; matches CC dilaton-as-boundary-data treatment) | LICENSED (existing `s85_w6_acoustic_white_hole_formal.py` + `s52_bogoliubov_amp.npz` infrastructure) | STRONGLY SUPPORTED (Volovik #09 hydraulic-jump white hole; #27 PG black hole; lab analog Rolley et al.) | **FRAMEWORK-NATIVE COMPANION** |
| **RQ-2** Λ-running via Chamseddine-Connes scale dilaton (CC 0512169) | PARTIALLY LICENSED (dilaton has its own EOM via δS/δφ = 0; still critical-point only, needs FRW coupling) | PARTIALLY LICENSED (well-defined for FRW background; dilaton mass/friction is research question) | PARTIALLY SUPPORTED (q-theory matches `Λ ~ K³_QCD/E²_Planck`; caveat: must couple to FRW) | **SMALLER-SCOPE FALLBACK** |

### Recommended next-action

**PIVOT to RQ-1 as Level B1 simulator target. RQ-3 as parallel framework-native cosmogenesis companion. RQ-2 as smaller-scope fallback if cosmological-Λ running is the priority.**

Concretely, the user has three decisions to make in increasing order of commitment:

1. **Decision 1 (immediate)**: Accept that D2(a) is closed for cause. Action: this workshop is the artifact; no further D2(a) work proceeds. The workshop closure replaces what would otherwise become a multi-session research effort with a negative result that is structurally informative.

2. **Decision 2 (next session-scoped)**: Write a Level B1 architecture spec for **RQ-1** (Inner-fluctuation simulator on fixed `D_K(τ_fold)`). Architecture: state variable = (gauge connection A_μ, Higgs field S, KK mode amplitudes) on emergent 4D × SU(3); evolution rule = Yang-Mills + Higgs equations of motion from spectral action under inner fluctuations (CC 0605011); inner loop uses existing static `D_K(τ_fold)` infrastructure (precomputed once, no per-timestep eigenvalue solve); observables = gauge boson masses, Higgs profile, KK tower spectra, post-quench relaxation. Pre-registered gates:

   - **RQ1-G1 (static-equilibrium recovery)**: at equilibrium, simulator reproduces framework canonical observables (m_H = 131.8 GeV ± tolerance, m_W, m_Z, α_s(M_Z), n_s) within 5%. PASS gates the dynamical layer's faithfulness to the spectral side.
   - **RQ1-G2 (KK tower spectrum)**: fundamental + first KK frequencies match canonical M_KK and ratios within 2%. Tests the inner-fluctuation construction on the fixed `D_K(τ_fold)`.
   - **RQ1-G3 (GGE-permanence verification)**: post-quench relaxation of an excited state shows NO thermalization on simulator timescales (consistent with S38 GGE-permanence theorem). FAIL would surface a contradiction between the simulator's effective dynamics and the framework's integrability claim. This is the most discriminating gate.

3. **Decision 3 (parallel, framework-native)**: Develop **RQ-3** (Phase-transition simulator across τ_fold) using existing acoustic-white-hole + Bogoliubov-coefficient infrastructure (`s85_w6_acoustic_white_hole_formal.py`, `s52_bogoliubov_amp.npz`, S37-38 GGE-relic results). This is mostly operationalization rather than new research — the physical content is already in the framework; the simulator would just package it as a callable observable-generator. Pre-registered gates:

   - **RQ3-G1 (n_eff prediction)**: Post-transit GGE occupation numbers reproduce the framework's canonical n_eff prediction within 2%.
   - **RQ3-G2 (n_s from interference)**: post-fold acoustic interference pattern produces n_s = 0.9561 within tolerance.
   - **RQ3-G3 (Mach 13.75 transit)**: kinematic transit profile recovers the canonical Mach 13.75 supersonic crossing.

### Optional pre-pivot validation (low-effort decisive test)

Before committing to RQ-1 architecture, the user could run **Round 2's Item 4** as a 2-week sanity-check: implement gradient flow `dD/dτ = -Ric(D)/G_BKM` on the Connes-Landi NC two-torus with FGK Ricci density. If the toy simulator successfully recovers the analytic flat-metric fixed point, the *infrastructure* (gradient-flow numerics, FGK Ricci density evaluation, GPU eigenvalue inner loop) is validated for any future moduli-dynamics work — independent of D2(a) being closed. If it fails to recover the known fixed point, that's a numerical-infrastructure problem to fix before any of RQ-1/RQ-2/RQ-3 is attempted. **This is the cheapest decisive test.**

### Carry-forward summary

| Item | Status | Disposition |
|:---|:---|:---|
| D2(a) gradient flow on bare `S_spec[τ]` | CLOSED for cause (NCG + Math + Analog + GGE-permanence) | No further work; cite this workshop in any future Path-B planning |
| RQ-1 Inner-fluctuation simulator on `D_K(τ_fold)` | PROPOSED as Level B1 launch target | Architecture spec in next session-scoped plan; 3 pre-registered gates |
| RQ-3 Phase-transition simulator (Bogoliubov scattering) | PROPOSED as framework-native cosmogenesis companion | Mostly operationalization of existing infrastructure; 3 pre-registered gates |
| RQ-2 CC dilaton Λ-running | PROPOSED as smaller-scope fallback | Pursue only if cosmological-Λ running becomes the priority |
| Connes-Landi NC two-torus toy (Item 4) | OPTIONAL pre-pivot validation | 2-week numerics-infrastructure sanity check; runs independent of pivot choice |
| Items 1, 2, 3, 5 from Round 2's mathematical work list | DEFERRED | Only relevant if a future workshop reopens D2 on a dressed functional or BKM-metric construction; not on the current critical path |

