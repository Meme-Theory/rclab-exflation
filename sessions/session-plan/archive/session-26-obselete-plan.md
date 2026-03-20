# Session 26 Plan: Route B Computation

**Date**: 2026-02-23
**Source**: Framework Mechanism Discussion + 5-Agent Collaborative Review + 3 Addenda
**Framing**: Phononic-first. The substrate provides μ. Compute what happens.

---

## Guiding Principle

> "The formal mechanism IS 1d-to-4d phononic transformation. NCG is a waypoint in the math gauntlet, not the foundation."

The computation proceeds top-down from the substrate: given D_K with its known spectrum, given the Kosmann couplings, given that the substrate provides excitations at the gap edge — does the system condense, lock τ, and produce a specific phonon frequency spectrum that maps to observable physics?

---

## Priority 1: Multi-Mode BCS Gap Equation

**Cost**: Hours | **Data**: Existing .npz files (Sessions 12-25) | **Closure**: Largest BCS kernel eigenvalue < 1 at all physical μ

Solve the matrix gap equation:
```
Δ_n = -Σ_m V_{nm} [tanh(E_m / 2T) / (2E_m)] Δ_m
```
for modes with p+q ≤ 2. This is the decisive computation. Everything downstream depends on it.

### Built-In Quality Gates (zero-cost, mandatory)

| Gate | Source | Check | Fail Condition |
|:-----|:-------|:------|:---------------|
| **J-even projection** | Dirac S-1 | Decompose Δ = Δ₊ + Δ₋ at every iteration | \|Δ₋/Δ₊\| > 10⁻¹² = BUG |
| **Spectral pairing** | Dirac S-2 | λ ↔ -λ halves sum; (p,q)↔(q,p) halves again | Gives 4x computational savings |
| **CPT gate** | Dirac S-3 | m(particle) = m(antiparticle), Δ₋ = 0, N(particle) = N(antiparticle) at each τ | Any deviation > 10⁻¹² = BUG |
| **KO-dim 6 verify** | Dirac Q-1 | J²=+1, JD_eff = D_eff J, Jγ = -γJ at finite μ | Violation = structural failure |
| **Spectral Bianchi** | Einstein E-2 | Sector-weighted derivative sum with and without μ | Broken = μ violates gauge invariance |
| **Kernel eigenvalue** | Master V | Largest eigenvalue of linearized BCS kernel | < 1 at all physical μ = NO CONDENSATION (K-1e generalized) |
| **Confinement threshold** | Baptista S.4 | gΔ² > 0.109 (bound state exists) | Below = modulus not even localized |
| **Barrier threshold** | Tesla T-A.5 | gΔ² > 50 (cosmological lifetime) | Below = false vacuum too short-lived |
| **Trans-Planckian** | Hawking H-5 | BCS sum convergence vs. modes with λ_k ≫ Λ | Significant dependence = trans-Planckian problem |

### Piggyback Outputs (zero/low-cost, extract from solution)

| Output | Source | What | Why |
|:-------|:-------|:-----|:----|
| **Saxion mass** | Tesla T-2 | m²_saxion = d²V_eff/dτ² at τ₀ | m² < 0 = saddle, not minimum. CLOSED. |
| **Q_τ of lock** | Tesla T-3 | Solve BCS at τ₀ ± δτ, compute FWHM | Q < 1 = smeared predictions; Q > 10 = sharp |
| **Δ⁴ coefficient** | Dirac D-7 | Sign of Landau free energy quartic term | Negative = first-order transition (Sakharov-3) |
| **sin²θ_W benchmark** | Dirac D-11 | 0.354 at τ₀=0.15 (overshoots SM by 53%) | Quantitative target for running |
| **Clock constraint** | Dirac D-10 | δτ oscillation amplitude vs. ALPHA 2 ppt | τ_dot/τ < 6.5×10⁻¹³/yr required |
| **Solution uniqueness** | SP-7 | Number of fixed points in (τ, Δ, μ) space | Multiple = need additional selection; unique = predictive |
| **Jacobian stability** | Baptista B-7 | Eigenvalues of coupled-system Jacobian at fixed point | Both negative = stable; any positive = unstable |
| **Hawking-Page map** | Hawking H-3 | Z = Z_normal + Z_condensed; first-law thermodynamics | Predicts first-order transition |
| **J-decomp of coupling** | Dirac D-8 | J-even vs J-odd parts of BCS kernel at intermediate μ | Large J-odd = effective coupling reduced |
| **Path integral measure** | Hawking HT-5 | BCS stiffness δ²I_E/δΔ² | Small = measure destabilizes; large = saddle-point valid |

---

## Priority 2: Geodesic Completeness of (τ, Δ) Space

**Cost**: 1 hour | **Data**: G_ττ = 5 (Baptista Paper 15), Kosmann coupling τ-dependence | **Closure**: Incomplete geodesics = no self-consistent solution

Construct effective metric on (τ, Δ) mini-superspace. Determine whether geodesics reach boundary in finite affine parameter.

### Piggyback
- **Penrose inequality** (SP-12): Compute A_barrier from modulus-condensate metric → lower bound on Δ required to censor decompactification singularity.

---

## Priority 3: Spectral Bianchi Identity at Finite μ

**Cost**: Low-Medium | **Data**: Peter-Weyl decomposed eigenvalues | **Closure**: Constraint broken = μ violates gauge invariance

Also built into Priority 1 as a quality gate, but worth running independently as a standalone verification.

---

## Priority 4: GSL Balance Sheet

**Cost**: Zero (once Priority 1 gives Δ estimate) | **Closure**: GSL violated = condensation thermodynamically forbidden

Compute ΔS = S_normal − S_condensed and compare with ΔF = −½N(0)Δ².

### Enhancement
- **Revised delocalization entropy** (Hawking HT-3): Zero-point width δτ_zp = 0.956 exceeds well width 0.15 by 6.4x. GSL constraint is MORE stringent than originally estimated. Include delocalization entropy: δS ~ ln(δτ/δτ_zp).

---

## Priority 5: Resonant Cavity Self-Consistency

**Cost**: 50-line script | **Data**: All eigenvalue .npz files, Kosmann couplings | **Closure**: |T(τ)| < 1 for all τ = insufficient feedback gain

Define round-trip transfer function T(τ) = Δ_out/Δ_in. One BCS iteration at each τ. Self-consistency at |T| = 1, arg(T) = 0.

---

## Priority 6: Higher-Order Seeley-DeWitt (a₆)

**Cost**: 2-4 hours | **Data**: r20a_riemann_tensor.npz | **Closure**: B-1 minimum destroyed by a₆ corrections

Compute a₆(τ) at 21 τ values. Evaluate V_spec^(6) and check persistence of τ₀ = 0.15.

---

## Priority 7: Cooling Trajectory + Frequency Profile

**Cost**: Days | **Depends on**: Priority 1 (phase diagram), Priority 2 (geodesic completeness)

Solve coupled 4-variable system (Δ, τ, μ, H). Track whether Δ locks τ₀ before μ drops below λ_min.

### Built-In Diagnostics

| Diagnostic | Source | What |
|:-----------|:-------|:-----|
| **Sonic horizon** | Tesla T-4 | When μ_eff crosses λ_min: T_H ~ ℏ\|dλ_min/dτ\| / 2π. Cross-check: T_H ≈ T_BCS? |
| **Sakharov-3** | Dirac D-5 | Track Δ=0 → Δ₀ transition: continuous (no baryogenesis) or discontinuous (Sakharov satisfied) |
| **Landau-Zener** | Einstein E-5 | P_LZ = exp(−2πδ²/v\|Δλ'\|). Adiabatic invariant conservation? |
| **Bogoliubov coefficients** | Hawking H-4 | \|β_k\|² near gap edge. Particle creation spectrum = THE frequency profile |
| **First-order prediction** | Hawking HT-7 | Hawking-Page analogy predicts first-order (N_species ~ 104 < N_crit ~ 200) |

The Bogoliubov output IS the "frequency profile" — the phononic content of the framework. This is where phonons-in meets phonons-out.

---

## Priority 8: Multi-Dimensional Stability

**Cost**: High (new eigenvalue computations) | **Depends on**: Priority 1

Compute d²V/(dτ₁dτ₂) at τ₀ = 0.15 in the 8D space of left-invariant metrics. Check whether 1D minimum is a saddle.

### Elevated Urgency
- **Euclidean bounce mode** (Hawking HT-6): If d²V/dφ² < 0 at (σ=0.15, φ=0), the Euclidean saddle is a BOUNCE with single negative mode. False vacuum decays by inflating in φ (changing internal volume), not rolling in τ. This makes Priority 8 potentially DECISIVE.
- **Two-field from Baptista** (B-4): Paper 15 eq 3.80-3.81 gives the (σ, φ) potential. Need d²V_spec/dφ² at the B-1 point.

---

## Priority 9: NEC Audit Along Cooling Trajectory

**Cost**: Medium | **Depends on**: Priority 1

Check R_μν k^μ k^ν ≥ 0 for all null k at each τ in [0, 0.5]. Verify condensation locks τ₀ BEFORE reaching NEC violation at τ = 0.778.

---

## Priority 10: No-Boundary Constraint on μ

**Cost**: Moderate (theoretical) | **Depends on**: Benefits from Priority 1

Apply Hartle-Hawking no-boundary proposal to M⁴ × SU(3). If regularity at the South Pole selects μ uniquely, and the condensate shifts the Euclidean saddle from τ=0 to τ₀, then (τ₀, μ, Δ) are ALL determined by regularity. **Zero free parameters.**

### Enhancement
- **Coupled zero-parameter derivation** (Hawking HT-2): The saddle-point conditions dI_E/dτ = 0, dI_E/dμ = 0, plus gap equation form a closed system. Three equations, three unknowns.

---

## Structural Theorems (verify alongside computation)

These are zero-cost algebraic results that should be confirmed as part of the computation infrastructure:

| Theorem | Source | Statement |
|:--------|:-------|:----------|
| **Chirality-breaking** | Dirac D-9 / Master III.6 | Nonzero J-even condensate CANNOT be chirality-definite (Jγ = −γJ in KO-dim 6). Condensate is mass-like, mixing L and R. Internal Higgs mechanism. |
| **183x zero-point excess** | Baptista S.2 | ½ω₀ = 0.0548 exceeds ΔV = 0.0003 by 183x. Bare well has no localized ground state. No Euclidean thermal state (Hawking HT-1). |
| **ALPHA-g prediction** | Dirac D-4 | If Δ > 0, J-even condensate predicts a_g = g exactly. Pre-register for ALPHA-g (targeting 1% by 2028). |

---

## Investigation Bucket (longer-term, not blocking)

### Standalone Investigations

| ID | Item | Cost | Source |
|:---|:-----|:-----|:-------|
| I-1 | Phononic crystal bandgap protection of false vacuum | Low | Tesla T-8 |
| I-2 | Loop gain \|G\| of recycling oscillator | Low | Tesla T-7 |
| I-3 | Correct Gamow (not CDL) tunneling calculation | Low | Baptista B-3 |
| I-4 | DNP growth rate vs. condensation rate at τ₀ | Low | SP-8 |
| I-5 | Actual CDL/Gamow bounce ODE for B-1 | Low | SP-9 |
| I-6 | Petrov type at τ₀ = 0.15 | Low | SP-6 |
| I-7 | Bekenstein bound on minimum barrier height | Low | Hawking HT-4 |
| I-8 | Coupled (τ, TT-modes) stability analysis | Moderate | SP-10 |
| I-9 | Paper 18 modified Lie derivative L̃ vs L | Moderate | Baptista B-5 |
| I-10 | Spectral equivalence principle test | Med-High | Einstein E-4 |
| I-11 | Internal islands at finite density (Wall W5) | High | Hawking H-6 |
| I-12 | First-order condition [[D,a], JbJ⁻¹] = 0 at finite μ | Low-Med | Hawking H-7 |

### Physical Units Bundle (do once, apply everywhere)

| Item | Source | What |
|:-----|:-------|:-----|
| Thermal vs. tunneling escape | Tesla T-6 | ΔV/T_Planck comparison |
| Saxion frequency in GeV | Tesla T-9 | ω_mod at Λ = 5.72, M_KK |
| False vacuum energy → Λ_4 | SP-11 | V_spec(τ₀) in eV⁴ |
| All thresholds in GeV | Baptista B-6 | ΔV, ω₀, gΔ² converted |
| CC from condensation | Einstein E-1 | V_eff(τ₀, Δ) vs. ρ_Λ^obs |

### Theoretical Follow-ups

| Item | Source | What |
|:-----|:-------|:-----|
| Penrose diagram for phase boundary | SP-2 | Causal character: null/spacelike/timelike |
| Positronium BEC as experimental analog | Dirac S-6 | J-even cosmological condensate analog |
| No-boundary + condensate as zero-parameter system | Hawking HT-2 | Three equations, three unknowns |

---

## Execution Notes

1. **Priorities 1-6 have no interdependencies** — run in parallel where possible.
2. **Priority 7 requires Priority 1** (phase diagram) and **Priority 2** (geodesic completeness).
3. **Priority 8 requires new eigenvalue computations** — can start independently but results feed into Priority 7.
4. **Priority 9 requires Priority 1** results.
5. **Priority 10 is theoretical** — can proceed independently but benefits from Priority 1.
6. **The 19 zero-cost quality gates should be coded into the BCS solver from day one** — they are not optional.
7. **The frequency profile (Bogoliubov coefficients) from Priority 7 is the terminal output** — this IS the phononic content of the framework.

---

## Success Criterion

The computation succeeds if it produces a specific frequency spectrum {λ_n(τ₀), Δ_n, |β_n|²} that maps phononic excitations to observable particles. This is not "Δ > 0 therefore pass." This is: **start with phonons, end with phonons, and in between the NCG machinery tells you which phonons correspond to which particles.**
