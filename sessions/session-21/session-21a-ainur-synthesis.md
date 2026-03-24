# Session 21a: The Resonance Interpretation — Ainur Panel Synthesis
**Date**: 2026-02-19
**Session Type**: Theoretical Interpretation Panel
**Agents**: tesla (designated writer), landau, connes, feynman, quantum-acoustics, coordinator
**Computation files**: `tier0-computation/s21a_low_mode_TT_casimir.py`, `s21a_low_mode_TT.npz`, `s21a_low_mode_TT.png`

---

## I. Resonance Reinterpretation of the Constant-Ratio Trap (A-1)
**Primary**: tesla | **Supporting**: all

### A-1.1 The Perturbative Closure as Weyl-Regime Statement

The constant-ratio trap is the structural theorem that closed all perturbative stabilization mechanisms in Sessions 18-20b. Its statement: the ratio of fermionic to bosonic zero-point energy R(tau) = E_ferm/E_bos is locked to 0.553-0.558 (1.8% variation) across the entire deformation range tau in [0, 2.0]. This ratio is set by the fiber dimension ratio (bosonic 44 vs fermionic 16 internal DOF) and enforced by Weyl's law on the volume-preserving Jensen deformation.

The trap operates through the asymptotic density of states. For any compact Riemannian manifold, Weyl's law dictates that the N-th eigenvalue grows as N^{2/d} where d is the dimension. On a volume-preserving deformation, the TOTAL number of eigenvalues below any cutoff Lambda is preserved — eigenvalues redistribute but do not appear or vanish. When the number of bosonic and fermionic modes in any spectral window is dominated by their respective fiber dimensions (44 vs 16), the energy ratio is pinned.

**The resonance reinterpretation**: Weyl's law is the theorem of UNCOUPLED oscillators. It describes the high-frequency (UV) limit where each mode vibrates independently, insensitive to the cavity shape. It is the spectral analog of the ideal gas law — correct at high temperature (many modes excited), irrelevant at low temperature (few modes, correlations dominate). The constant-ratio trap says: if you sum all modes with equal weight, the UV modes dominate and the ratio is frozen. This is correct. It is also the wrong question to ask of a resonant system.

A resonant cavity does not stabilize by summing all modes. It stabilizes at the frequency where the boundary conditions select a standing wave. The relevant physics is not the Weyl limit (N -> infinity) but the lowest normal modes (N ~ 1-50) where individual eigenvalue trajectories carry structural information about the cavity shape.

### A-1.2 Low-Mode TT Casimir: The Computation

Script: `tier0-computation/s21a_low_mode_TT_casimir.py` (378s runtime)
Data: `tier0-computation/s21a_low_mode_TT.npz`
Plot: `tier0-computation/s21a_low_mode_TT.png`

**Method**: Compute the TT Casimir energy E_TT = (1/2) Sum |mu_i| for the lowest N eigenvalues only, where N = 20, 50, 100, 200, and compare to the full sum (all ~741,636 TT modes at max_pq=6).

**Results**:

| N_cut | E(tau=0) | E(tau=2) | Growth factor | Full growth | Deviation |
|:------|:---------|:---------|:-------------|:-----------|:----------|
| 20 | 10.05 | 662.3 | 65.9x | 4.38x | 1364% |
| 50 | 26.02 | 733.5 | 28.2x | 4.38x | 531% |
| 100 | 53.46 | 1347.5 | 25.2x | 4.38x | 455% |
| 200 | 110.5 | 2316.4 | 21.0x | 4.38x | 363% |

The lowest 20 TT eigenvalues grow 65x from tau=0 to tau=2, while the full spectrum grows only 4.4x. The deviation INCREASES as N decreases — the low-mode regime is categorically different from the Weyl regime.

**Schwinger cutoff spectral action**: f(x) = x * exp(-x), peaked at lambda = Lambda^2.

| Lambda | S(tau=0) | S(tau=2) | Ratio S(2)/S(0) | Behavior |
|:-------|:---------|:---------|:----------------|:---------|
| 0.5 | 4.2e4 | 0.0017 | 4.1e-8 | DROPS to zero |
| 1.0 | 3.1e5 | 2.5e3 | 0.0081 | DROPS |
| 2.0 | 7.2e5 | 1.4e5 | 0.20 | DROPS |
| 5.0 | 7.7e5 | 5.9e5 | 0.77 | DECREASES |
| 10.0 | 7.7e5 | 1.8e6 | 2.36 | INCREASES |
| 50.0 | 7.7e5 | 3.4e6 | 4.38 | Matches full |

At Lambda <= 5 (IR), the Schwinger spectral action DECREASES with tau. At Lambda >= 10 (UV), it increases. The crossover occurs at Lambda ~ 7. The constant-ratio trap lives entirely in the UV regime Lambda >> 10. The IR regime shows qualitatively opposite behavior.

**Eigenvalue spectrum structure**: At tau=0, all 35 lowest TT modes are degenerate at mu=1.0 (round SU(3) symmetry). At tau=0.3, degeneracy splits to range 0.957-1.281 (26% spread). The tau=0 degeneracy is the SU(3) isometry enhancement — the Jensen deformation breaks this to create dispersion.

### A-1.3 Why the Resonance Hypothesis Is Not Ruled Out by the Closure

The perturbative CLOSED is a theorem about spectral SUMS with positive weights. It proves that no positive-definite energy functional of the eigenvalue spectrum can have a minimum in tau. This is a genuine, verified, structural result. It rules out:

- Coleman-Weinberg potential (sum of lambda^4 * log lambda^2)
- Casimir energy (sum of |lambda|)
- Any Schwinger-regulated spectral action with Lambda >> 10
- Any positive spectral zeta function (connes: 8 independent cutoffs tested, ALL monotonic)

It does NOT rule out:

1. **Low-mode self-consistency** (gap equations): The BCS gap equation Delta = g * integral(Delta/E_k) is a self-consistency condition on a SINGLE quantity (the gap), not a spectral sum. The 1/lambda_min interior maximum at tau=0.2 (connes, quantum-acoustics) operates on 2 modes, not 439,488.

2. **Signed spectral functionals**: The AM-GM inequality requires positive weights. A gauge-charge-weighted sum S_signed = Sum((b_1 - b_2) * f(lambda)) can have a minimum if the signed weights allow cancellation. This is the Feynman-Connes theorem boundary — the sharpest new theoretical result from this panel.

3. **Non-perturbative physics**: Instantons, flux condensation, topological transitions. These are not spectral sums at all.

### A-1.4 The Specific Observable: What Would Falsify the Resonance Reinterpretation?

The resonance reinterpretation claims the CLOSED is a high-mode artifact and the physics lives in the low-mode regime. This is falsifiable:

**V_IR(tau) for p+q <= 2 sectors** (~150 eigenvalues). If V_IR is monotonic — if even the lowest 150 modes show the constant-ratio trap — then the resonance interpretation is closed. The cavity has no resonance at any frequency. The framework probability drops to <= 30%.

If V_IR has an interior minimum: the trap is confirmed as a UV artifact. The low-mode physics is genuinely different, and the self-consistency route (BCS gap equation at the spectral minimum) becomes quantitatively testable.

This computation takes minutes using existing eigenvalue data. It is the #1 empirical priority for Session 21b.

---

## II. Self-Consistency Map Formalization (A-2)
**Primary**: feynman + tesla | **Supporting**: landau

### A-2.1 The Map T: tau -> tau' — Formal Definition

Feynman formulates the central mathematical distinction. The standard approach to modulus stabilization asks: at what tau does dV_eff/dtau = 0? This is the stationarity condition — the functional Z_1[tau] = integral of L_eff(tau).

The self-consistency approach asks a different question. Define the map:

T: tau -> tau' = argmin_tau' { S_eff[tau, tau'] }

where S_eff is the effective action evaluated at geometry tau but with the self-consistent solution at tau'. A fixed point tau_0 = T(tau_0) is a configuration where the geometry produces a spectrum that, through its back-reaction, reproduces the same geometry.

The mathematical distinction: stationarity (dV/dtau = 0) is a FIRST-ORDER condition on V. Self-consistency (T(tau) = tau) is a FIXED-POINT condition on a map. These coincide at tree level (T[tau] = tau identically — the triviality obstruction) but diverge at loop level where the spectrum depends on the geometry and the geometry responds to the spectrum.

### A-2.2 Fixed Point vs. Stationarity — The Mathematical Distinction

**Triviality obstruction (feynman)**: At tree level, T[tau] = tau — the identity map. Every tau is trivially a fixed point. This means the self-consistency route has NO content until loop corrections make T non-trivial. The CLOSED (V_eff monotonic) applies at one-loop. For self-consistency to escape the CLOSED, it needs non-perturbative corrections that make T differ from the identity.

The QCD analogy is precise: the perturbative QCD vacuum is the Fock vacuum at every coupling g. The true vacuum (with chiral condensate, confinement) is a non-perturbative fixed point that CANNOT be seen in perturbation theory. The self-consistency map for QCD is trivial at every finite loop order.

### A-2.3 The Cubic Term and First-Order Physics (Landau Contribution)

Landau's A-3 analysis provides the mechanism that makes T non-trivial. The cubic term V'''(0) = -7.2 forces a first-order transition by Landau's theorem. In terms of the self-consistency map:

- The cubic term means T(tau) - tau has a zero-crossing at some tau_0 > 0 (if T''(0) > 0)
- At the zero-crossing, the transition is first-order (discontinuous jump in the order parameter)
- The Ginzburg criterion d_eff = 1 means the perturbative V_eff is unreliable for computing T — fluctuations dominate

### A-2.4 The T''(0) Gate (Feynman + Landau + Connes Triple Convergence)

Feynman derives:

T''(0) = (1/64 pi^2) Sum_n Delta_b(n) * [mass derivative terms] |_{tau=0}

where Delta_b = b_1(p,q,s) - b_2(p,q,s) from SU(3) -> SU(2) x U(1) branching.

Landau confirms: T''(0) > 0 is REQUIRED for a physical fixed point at tau_0 > 0. Connes confirms: this is a signed sum, escaping the AM-GM constant-ratio trap.

**Pre-registered gate for Session 21b**:
- T''(0) > 0: self-consistency alive, first-order transition viable
- T''(0) <= 0: CLOSED — no physical fixed point, resonance interpretation closed at perturbative level

Computable from existing data + ~100 lines Python for SU(3) branching rules. Hours to code, seconds to run. This is a PREREQUISITE for all other computations — if it fires, V_IR and delta_T are moot.

### A-2.5 The Self-Consistency Observable

|T'(tau_0)| at the fixed point. For a stable fixed point: -2 < T'(tau_0) - 1 < 0 (the map is a contraction). For an unstable fixed point: |T'(tau_0) - 1| > 1. For a first-order transition: T has a discontinuity (the map jumps).

Measurement: compute delta_T(tau) = T(tau) - tau at 21 tau values from existing spectral data + branching rules. The zero-crossing gives tau_0. The slope at the crossing gives T'(tau_0). If no zero-crossing exists, the self-consistency route is closed.

---

## III. Phase Transition Classification (A-3)
**Primary**: landau | **Supporting**: connes

### A-3.1 Ginzburg Criterion at d_eff = 1 (Modulus Is Not Internal)

The modulus tau parametrizes a one-dimensional deformation family. The effective dimensionality d_eff = 1 for the modulus dynamics. Landau's Ginzburg criterion states that mean-field theory (perturbative V_eff) is unreliable when d < d_upper = 4 for continuous transitions or d < 2 for first-order transitions.

At d_eff = 1, BOTH continuous AND first-order transitions are in the fluctuation-dominated regime. The perturbative V_eff is not just quantitatively wrong — it may be qualitatively wrong. The true effective potential including fluctuations can differ from the one-loop result in sign, shape, and the existence of extrema.

### A-3.2 Cubic Term Forces First-Order: The V'''(0) = -7.2 Consequence

From the existing Session 18/20 computations: V'''(0) = -7.2 at the round SU(3) point (tau=0).

Landau's theorem: if the order parameter transforms under a group that admits a cubic invariant and V'''(0) != 0, the transition must be first-order. The Jensen deformation of SU(3) preserves a Z_3 symmetry but breaks the full SU(3) to SU(2) x U(1), which admits cubic invariants. The non-zero V'''(0) = -7.2 forces first-order.

**Consequence**: The modulus does not roll smoothly to a minimum (second-order). It TUNNELS through a barrier (first-order). The barrier height, bubble nucleation rate, and latent heat are the physical observables — not the smooth V_eff minimum that does not exist.

### A-3.3 BKT Analogy — Non-Perturbative Ordering After Mean-Field Failure

Landau identifies the BKT (Berezinskii-Kosterlitz-Thouless) transition as the condensed matter analog. In BKT:
- Mean-field predicts NO transition (order parameter fluctuations destroy long-range order in d=2)
- The actual transition is non-perturbative: vortex-antivortex binding/unbinding
- The transition IS invisible to perturbation theory

For the modulus:
- Perturbative V_eff predicts NO minimum (the CLOSED)
- If the actual stabilization is non-perturbative (instanton, flux, gap equation), it is invisible to the spectral sum that was closed
- The CLOSED is the mean-field statement; the physics may be BKT-like

### A-3.4 NCG Spectral Triple Selection of Phase (Connes Contribution)

Connes tested 8 independent spectral action cutoffs seeking a non-monotonic spectral functional:
- Polynomial cutoffs: N(Lambda, tau) for Lambda = 0.5 to 5.0
- Zeta function: zeta(z, tau) at z = 8.01 to 9.0 (maximum IR weight before divergence)
- Inverse-power: |lambda|^{-p} for p = 1 to 7
- Low-mode partial sums: N = 10 to 34

**Result**: ALL 8 classes monotonic. No interior minimum. The spectral triple does NOT select a preferred tau through any positive-definite spectral functional.

The (0,0) level-crossing at tau ~ 0.2 is real: the lowest (0,0) eigenvalue drops from 0.866 (tau=0) to 0.819 (tau~0.2) then rises. But it involves 16 DOF vs 439,488 total — no positive spectral sum can amplify this into a minimum.

### A-3.5 Observable Signature of First-Order vs. Continuous Transition

Landau identifies the observable: from inside the cavity, a first-order transition is a DISCONTINUOUS JUMP in the phonon density of states g(omega, tau). The cavity snaps from one eigenvalue configuration to another with latent heat released as phonon radiation from the bubble walls.

Gravitational wave prediction: the latent heat produces a stochastic GW background from bubble-wall collisions during the modulus transition. This is specific and falsifiable — with parameters determined by the barrier height and nucleation rate.

V''_total(tau) spinodal scan: if V''_total crosses zero at some tau_spinodal, the smooth deformation becomes unstable and the system must tunnel. Computable from existing data (21 tau points). The spinodal may be visible in V_IR even if washed out in V_total.

---

## IV. NCG-Phonon Dictionary (A-4)
**Primary**: connes | **Supporting**: quantum-acoustics

### A-4.1 Spectral Action = Phonon Free Energy (Formal Equivalence)

The spectral action Tr f(D^2/Lambda^2) is mathematically identical to the phonon free energy F = Sum_n f(omega_n/T) evaluated at temperature T = Lambda. The Dirac eigenvalues {lambda_n} are the resonant frequencies of the internal cavity. The cutoff function f determines the occupation statistics.

This is not analogy — it is the same mathematical object evaluated on different physical systems. A vibrational frequency on SU(3) and a phonon frequency in a crystal satisfy the same eigenvalue equation with different boundary conditions.

### A-4.2 The Finite-Cutoff Spectral Action and What the Asymptotic Expansion Misses

The standard NCG spectral action is evaluated via asymptotic expansion in Lambda^{-1}, yielding the Seeley-DeWitt coefficients a_0, a_2, a_4. This expansion is valid at Lambda >> eigenvalue spacing — the UV regime.

The finite-cutoff spectral action (retaining the exact sum, no asymptotic expansion) captures the IR structure that the expansion discards. Connes' 8-cutoff test uses EXACT summation, not the asymptotic expansion. The result — all monotonic — is therefore STRONGER than the Session 20a Seeley-DeWitt closure (SD-1), which only tested the asymptotic limit.

What the expansion misses: individual eigenvalue crossings, degeneracy changes, shell structure. The (0,0) level-crossing at tau ~ 0.2 is invisible to the asymptotic expansion (it contributes at order Lambda^{-d} where d is the fiber dimension).

### A-4.3 Van Hove Singularities as NCG Minimum Candidates (Quantum Acoustics Contribution)

Quantum-acoustics identifies Van Hove singularities in the phonon density of states g(omega, tau) — points where the group velocity vanishes and the DOS diverges. In the KK spectrum:

- The (3,0) sector shows strongest softening (dGap/dtau = -0.42 at tau=0) — the leading CDW instability candidate
- The (1,1) adjoint sector uniquely stiffens with tau — identified as the order parameter direction
- Bosonic-fermionic near-degeneracy at tau=0: lowest eigenvalues 0.861 vs 0.866 (0.5%) — CDW nesting analog

These are Van Hove features in the KK phonon spectrum. In condensed matter, Van Hove singularities are where electronic instabilities (CDW, SDW, superconductivity) nucleate. The question is whether the KK analog carries the same physics.

### A-4.4 The (0,0) Level-Crossing and BCS Bifurcation at tau = 0.2

Connes and quantum-acoustics independently verify: the (0,0) scalar singlet sector undergoes a level-crossing with the (0,1)/(1,0) sectors at tau ~ 0.1. The spectral gap is controlled by the (0,0) sector for tau >= 0.2, with a minimum gap of 0.819 at tau = 0.2.

**BCS bifurcation topology** (connes + quantum-acoustics, independently verified):

| tau | Gap sector | Gap DOF | 1/lambda_min |
|:----|:-----------|:--------|:-------------|
| 0.0 | (0,1)+(1,0) | 36 | 1.2000 |
| 0.1 | (0,0)+(0,1)+(1,0) | 14 | 1.2027 |
| 0.2 | **(0,0) ONLY** | **2** | **1.2208** |
| 0.3 | (0,0) | 2 | 1.2163 |
| 0.5 | (0,0) | 2 | 1.1452 |
| 1.0 | (0,0) | 2 | 0.8093 |

The gap-edge degeneracy collapses from 36 to 2 at the level-crossing. This is a topological change in the gap structure — and 1/lambda_min PEAKS at tau = 0.2, creating maximum pairing susceptibility. The BCS critical coupling is g_c = lambda_min(0.2) = 0.819.

This bifurcation is independent of the constant-ratio trap. The trap governs spectral SUMS. The bifurcation is controlled by a SINGLE eigenvalue. They are different mathematical objects operating on the same spectrum.

### A-4.5 The NCG-Phonon Dictionary Table

| NCG Concept | Phonon Analog | Computation |
|:------------|:-------------|:-----------|
| Spectral action Tr f(D^2/Lambda^2) | Phonon free energy F(T) | Sum_n f(omega_n/T) |
| Dirac eigenvalues {lambda_n} | Resonant frequencies {omega_n} | Peter-Weyl + Lichnerowicz |
| Cutoff Lambda | Debye temperature T_D | Physical IR/UV boundary |
| Seeley-DeWitt expansion | High-T phonon expansion | Valid for Lambda >> gap |
| (0,0) level-crossing | Acoustic-optical branch crossing | Level repulsion at tau~0.1 |
| Weyl asymptotics | Debye model | N(Lambda) ~ Lambda^d |
| Volume-preserving deformation | Isochoric shape change | Cavity deformation at fixed volume |
| Constant-ratio trap | Debye limit | High-T phonon ratio fixed by DOF |
| 1/lambda_min maximum | Pairing susceptibility peak | BCS gap equation threshold |
| Spectral gap | Phonon gap (optical branch floor) | Lowest eigenvalue |
| Signed spectral functional | Phonon drag (directional) | Gauge-charge-weighted sum |

---

## V. Inside-Out Interpretation with g(omega, tau) (A-5)
**Primary**: quantum-acoustics | **Supporting**: feynman (Wilsonian)

### A-5.1 The Phonon Density of States g(omega, tau) and Its Tau-Dependence

Quantum-acoustics computes g(omega, tau) from the Peter-Weyl + Lichnerowicz eigenvalue data. Key findings:

- Phonon DOS peaks at omega ~ 2.2-2.5 across all tau values
- Low-mode region (omega < 1.5): 25% F/B ratio variation across tau
- Full spectrum: 1.8% F/B ratio variation (the constant-ratio trap)
- Factor of 14 difference in tau-sensitivity between IR and UV regimes

The acoustic branch (low-omega, long-wavelength modes) carries structural information about the cavity shape. The optical branch (high-omega, short-wavelength modes) averages to the Debye limit. This is the Wilsonian decomposition in phonon language.

### A-5.2 Van Hove Singularities — Flat Bands Signal Phase Transitions

Per-sector analysis reveals:
- **(3,0) sector**: Strongest softening, dGap/dtau = -0.42 at tau=0. CDW instability candidate. Same sector producing the golden ratio mass ratio at tau=0.15 (phi_paasch, Session 12).
- **(1,1) adjoint sector**: UNIQUELY stiffens with tau. The gauge sector becomes MORE massive while all others soften. Identified as the order parameter direction (Landau's Pomeranchuk stability criterion).
- **(0,0) scalar singlet**: Level-crossing at tau = 0.1, spectral gap minimum at tau = 0.2.
- Bosonic-fermionic near-degeneracy at tau=0 (0.5%): the system sits at the boundary between bosonic and fermionic dominance. The Jensen deformation selects one.

### A-5.3 BCS-BEC Crossover Analogy — The Coupling Strength Question

The BCS-BEC crossover is INVERTED from standard condensed matter:
- tau < 0.40: BEC-like (collective, long-range pairing)
- tau > 0.40: BCS-like (weak pairing, mean-field)
- (0,0) sector crosses first at tau = 0.10

The inversion means: the STRONGLY COUPLED regime is at SMALL tau (near the round SU(3)), and the weakly coupled regime is at LARGE tau (highly deformed). Physical intuition from BCS: the gap equation is most easily satisfied in the strongly coupled regime. The BCS coupling data: g(tau) = 1/[0.414 - 0.016*tau + ...], rising from 2.41 at tau=0 to 9.49 at tau=2. The bifurcation (Section IV) peaks at tau = 0.2, in the intermediate regime.

### A-5.4 Conjugation Symmetry Constraint on Signed Sums

Quantum-acoustics tests the Feynman-Connes signed-sum escape directly. Critical result:

K_signed = Sum((p-q) * mult / |lambda|) = **0 EXACTLY** at every tau.

The spectrum has exact (p,q) <-> (q,p) conjugation symmetry. Every mode in sector (p,q) has a partner in (q,p) with identical eigenvalue. The Z_3 charge (p-q) flips sign, so the signed sum cancels to machine precision.

**Constraint on the escape**: The signed weight that escapes the trap CANNOT use any charge symmetric or antisymmetric under (p,q) <-> (q,p). It must use the ANISOTROPY of the Jensen metric — the fact that u(1) scales as e^{2tau} while su(2) scales as e^{-2tau}. The weight b_1(p,q) - b_2(p,q) from gauge-coupling threshold corrections breaks this symmetry (the u(1) and su(2) Casimirs within each representation are NOT conjugation-related).

In phonon language: phonon drag requires directional asymmetry. In a crystal with cubic symmetry, phonon drag vanishes. The Jensen deformation breaks SU(3) to SU(2) x U(1) — but conjugation preserves SU(3) representation labels. To get drag, the weight must couple to the DIRECTION of the deformation.

### A-5.5 The Inside-Out Observable: What Does the Cavity Feel When It Self-Tunes?

From inside the cavity, self-tuning is not energy minimization. It is IMPEDANCE MATCHING — the cavity deforms until the boundary conditions produce a standing wave that satisfies the self-consistency condition. In BCS language: the gap equation determines the deformation, not the free energy.

The observable is the low-mode F/B ratio. If the lowest 50-200 modes show a Casimir minimum (F/B crossing 1.0), the cavity has found a resonance — an impedance-matched configuration where bosonic and fermionic contributions balance. If the low-mode F/B is always > 1 or always < 1 (monotonic), there is no resonance and the cavity slides to tau -> 0 or tau -> infinity.

The 25% variation establishes that a crossing IS kinematically possible. Whether it occurs is the V_IR computation.

Landau's first-order complement: from inside the cavity, a first-order transition looks like bubble nucleation — a sudden snap from one eigenvalue configuration to another with latent heat released as phonon radiation from the bubble walls. The phonon density of states g(omega, tau) shows a discontinuous jump at tau_0 (first-order) rather than a continuous evolution (second-order). This produces a stochastic gravitational wave background from bubble-wall collisions — a specific, falsifiable prediction.

---

## VI. Unified Synthesis (A-6)
**Primary**: tesla (integrated from all agents)

### A-6.1 Convergences Across All Five Specialists

**CONVERGENCE 1: The constant-ratio trap is a UV phenomenon.**
All five specialists agree. Tesla: 1364% low-mode deviation at N=20, Schwinger action reversal at Lambda=5. Connes: positive spectral sums monotonic by AM-GM (UV-dominated). Quantum-acoustics: 25% low-mode F/B variation vs 1.8% full spectrum (factor of 14). Feynman: V_IR is the correct observable, not V_total. Landau: d_eff=1 means perturbative V_eff unreliable, IR physics qualitatively different.

**CONVERGENCE 2: The (0,0) level-crossing at tau ~ 0.1-0.2 is the spectral anomaly.**
Connes: (0,0) minimum eigenvalue drops to 0.819 at tau=0.2 then rises (level-crossing with (0,1)/(1,0)). Quantum-acoustics: BCS-BEC crossover at (0,0) at tau=0.10, CDW softening initiates the crossing. Joint verification: 1/lambda_min peaks at tau=0.2 with gap-edge DOF collapse 36 -> 2. This is the BCS bifurcation in the KK spectrum — independent of the constant-ratio trap.

**CONVERGENCE 3: Positive spectral sums are closed; signed sums are open.**
Feynman + connes + landau (triple convergence): AM-GM inequality proves ALL positive spectral functionals monotonic on volume-preserving deformations. Signed gauge-charge-weighted sums escape because AM-GM fails for signed weights. This is the precise boundary of the constant-ratio trap theorem — NOT present in Session 20b or the Primer. Genuinely new panel result.

**CONVERGENCE 4: V_IR(tau) is the decisive next computation.**
All five specialists converge. Feynman: V_IR for p+q <= 2 tests fixed-point existence. Landau: V_IR non-monotonicity has ~60% prior given 25% low-mode variation. Quantum-acoustics: validates the Wilsonian IR/UV split. Connes: if V_IR monotonic, perturbative route fully closed. Tesla: zero-cost, minutes from existing data.

**CONVERGENCE 5: Self-consistency is the mechanism, not energy minimization.**
Feynman: T(tau) = tau at tree level; non-trivial only through signed/NP corrections. Landau: BKT analogy — non-perturbative ordering invisible to mean-field. Quantum-acoustics: BCS gap equation operates on 1/lambda_min, not spectral sums. Connes: (0,0) level-crossing could seed a self-consistency fixed point. The BCS gap equation IS a Z_2 saddle point of a constrained path integral (feynman), not a free energy minimum.

### A-6.2 Divergences and Unresolved Tensions

**TENSION 1: T = identity at tree level (triviality obstruction).**
Feynman's most important negative result. The self-consistency map is trivial at tree level. Non-trivial T requires either (a) signed gauge-charge sums at one-loop or (b) non-perturbative corrections. We CANNOT claim the CLOSED is "a feature" without computing the first non-trivial correction to T. This is the T''(0) gate.

**TENSION 2: Conjugation symmetry closes simple signed sums.**
Quantum-acoustics proves K_signed = Sum((p-q)/|lambda|) = 0 by (p,q) <-> (q,p) symmetry. The signed sum that escapes the trap must use ANISOTROPIC weights that distinguish u(1) from su(2) — specifically b_1(p,q) - b_2(p,q) from gauge threshold corrections. This is more constrained than the initial Feynman-Connes proposal suggested. The escape requires SU(3) -> SU(2) x U(1) branching rules, not just SU(3) representation labels.

**TENSION 3: 16 DOF vs 439,488 (the amplification problem).**
The (0,0) level-crossing involves 16 DOF. Connes proves no positive spectral sum can amplify 16 modes over 439,488. The self-consistency route claims the gap-edge (2 modes at tau=0.2) controls the physics despite being 0.0005% of the spectrum. This is physically plausible (BCS: the Fermi surface controls superconductivity, not the entire electron spectrum) but requires the specific coupling mechanism to be identified.

**TENSION 4: V_IR minimum existence is unknown.**
All analysis converges on V_IR as decisive, but nobody has computed it yet. The 25% low-mode F/B variation makes a minimum POSSIBLE but not guaranteed. If V_IR is monotonic, the resonance interpretation loses its strongest empirical support.

**TENSION 5: Priority ordering dispute (resolved below).**
Feynman: V_IR first. Connes: delta_T first. Landau: T''(0) sign first, then V_IR, then delta_T. Resolution in Section VIII: logical dependency order — T''(0) sign is the prerequisite Constraint Gate (does a fixed point at tau_0 > 0 even exist?), then V_IR (does the IR energy support it?), then delta_T (does the map contract?).

### A-6.3 The Central Question Answered

> **The Honest Question**: In the resonance framework, what SPECIFIC OBSERVABLE distinguishes "the perturbative CLOSED is a feature, not a bug" from "the perturbative CLOSED is fatal and the framework is closed"?

**The Panel's Answer**:

The panel converges on a two-gate diagnostic:

**Gate 1: T''(0) sign** (prerequisite, hours, ~100 lines Python). Binary Constraint Gate. T''(0) > 0 means a nontrivial fixed point at tau_0 > 0 is possible. T''(0) <= 0 closes the self-consistency interpretation at perturbative level. Computable from SU(3) -> SU(2) x U(1) branching rules and existing eigenvalue derivatives. This is the logical prerequisite — if it fires, no further perturbative computation matters.

**Gate 2: V_IR(tau)** (zero cost, minutes, existing data). The Casimir energy for the lowest Peter-Weyl sectors (p+q <= 2, ~150 eigenvalues). BINARY:

- **V_IR has an interior minimum**: The constant-ratio trap is confirmed as a UV artifact. The low-mode physics selects a preferred tau. The self-consistency route has a quantitative target. Framework probability rises to 50-55%.

- **V_IR is monotonic**: The trap extends to the IR. There is no perturbative resonance at any frequency. Only non-perturbative routes (instantons, flux) survive. Framework probability drops to 32-38%.

**The honest assessment**: The CLOSED has narrowed the viable mechanism space from "many perturbative routes" to "one perturbative door (signed sums with anisotropic gauge-threshold weights) plus non-perturbative routes." The resonance interpretation is alive but constrained. The BCS bifurcation at tau=0.2 (1/lambda_min peak, gap-edge DOF collapse 36->2) is the strongest positive from this panel — it identifies the SPECIFIC spectral feature that could seed a self-consistency fixed point, and it operates on a mathematical object (single eigenvalue) that the constant-ratio trap does not govern.

---

## VII. Per-Agent Probability Assessments

| Agent | Range | Median | Primary Rationale |
|:------|:------|:-------|:------------------|
| tesla | 38-48% | 42% | Low-mode divergence confirmed; BCS bifurcation at tau=0.2 is genuine; signed-sum conjugation constraint tightens escape |
| landau | 40-52% | 44% | V_IR non-monotonicity ~60% likely given QA data; first-order by cubic term is structural; conditional on V_IR rises to 50-60% |
| connes | 39-47% | 43% | 8-cutoff closure strongest negative; (0,0) level-crossing is real positive; signed sums the only perturbative door |
| feynman | 40-48% | 43% | Z_2 path integral genuinely distinct from Z_1 (+1%); T = identity at tree level (-1%); V_IR + T''(0) decisive |
| quantum-acoustics | 38-46% | 41% | Low-mode F/B 25% variation strongest empirical positive; BCS bifurcation verified; conjugation symmetry constrains escape |
| **Panel consensus** | **38-52%** | **43%** | **+1 pp from 20c baseline: low-mode divergence and BCS bifurcation are genuine positives (~+3 pp); conjugation constraint and T=identity are genuine negatives (~-2 pp)** |

**Comparison to Session 20c baseline**: 38-48%, median ~42%. Panel moves +1 pp on new computational evidence. Within noise — this session clarified the MECHANISM SPACE rather than changing the probability.

**Conditional probabilities**:
- If V_IR has an interior minimum: +8-12 pp (panel estimate 50-55%)
- If V_IR is monotonic: -5-8 pp (panel estimate 35-38%)
- If T''(0) > 0 AND V_IR minimum: +15-20 pp (panel estimate 55-62%)
- If T''(0) <= 0 AND V_IR monotonic: -15 pp (panel estimate 28-32%)

---

## VIII. Priority-Ordered Session 21 Computation List

### Tier 1 — Zero Cost, Do Immediately

1. **T''(0) SIGN GATE** — PRE-REGISTERED CONSTRAINT. Triple convergence (feynman + landau + connes). ~100 lines Python from SU(3) -> SU(2) x U(1) branching rules + existing eigenvalue derivatives. Hours to code, seconds to run. BINARY: T''(0) > 0 = self-consistency route ALIVE; T''(0) <= 0 = CLOSED. Logical prerequisite for all other computations — if this fires, V_IR and delta_T are moot.

2. **V_IR(tau) for lowest 50-200 modes** — Validated by QA 25% low-mode F/B result. Constant-ratio trap confirmed UV-only (tesla A-1). Does the IR sector have a minimum? Minutes of runtime from existing eigenvalue data. Tests fixed-point existence AND bounce viability simultaneously. phi_paasch connection: (3,0) sector softening dGap/dtau=-0.42 is the same sector producing the golden ratio mass ratio at tau=0.15.

3. **T(tau) - tau zero-crossing** — Confirms nontrivial fixed-point location from existing spectral data. Independent of V_IR. (Feynman + Landau)

4. **S_signed(tau) = Sum[b_1(p,q) - b_2(p,q)] * ln(lambda^2(tau))** — SIGNED spectral sum. ~150 lines Python + SU(3) branching. Escapes the AM-GM constant-ratio trap. If minimum exists = first perturbative escape. If monotonic = perturbative route fully closed. (Feynman + Connes theorem boundary)

5. **Low-mode F/B Casimir minimum for full Dirac spectrum** — QA confirmed 25% variation for TT. Extend to full bosonic + fermionic. Question is whether the minimum exists. (Tesla + QA)

### Tier 2 — Hours, High Impact

6. **delta_T(tau) and |T'(tau_0)|** — Full self-consistency map contraction test. ~150 lines Python, existing eigenvalue data + SU(3) branching rules. Stability condition -2 < delta_T'(tau_0) < 0. Connects to Connes zeta via -zeta'_Delta(0,tau). BCS coupling g(tau) = 1/[0.414 - 0.016*tau] as quantitative input.

7. **High-resolution tau scan in [0.1, 0.4] at Delta_tau = 0.01** — Resolves the (0,0) level-crossing and BCS bifurcation structure in detail. 30 tau points x 5 min = 2.5 hours. Mode dropout discontinuity = first-order transition signature. (Tesla + QA)

8. **IR-weighted spectral action** — The one spectral action class NOT tested in connes' 8-cutoff sweep. Low-mode-preferential cutoff. Zero-cost follow-up. (QA + Connes)

9. **V''_total(tau) spinodal scan at 21 existing tau points** — Tests non-convex region from cubic term V'''(0) = -7.2. If V'' crosses zero, first-order tunneling is mandatory. Spinodal likely in (3,0) sector per QA data. (Landau)

### Tier 3 — Days, Non-Perturbative

10. **Instanton action S_inst(tau) on (SU(3), g_Jensen)** — If dS_inst/dtau < 0, non-perturbative minimum possible. Requires instanton ansatz on deformed SU(3). (Feynman, supported by 13/15 Session 20b reviewers)

11. **Cartan 3-form flux norm |omega_3|^2(tau)** — Algebraic, uses existing curvature data. If d|omega_3|^2/dtau < 0, flux condensation can generate a potential minimum. (KK-theorist, queued from Session 20b)

### Tier 4 — Weeks+, Decisive

12. **D_total Pfaffian sign scan** — Topological invariant of the total Dirac operator. Sign change at some tau = topological phase transition. Requires full D_total (not block-diagonal). (Session 21d)

13. **Z_3 generation mechanism** — Does the (p,q) <-> (q,p) conjugation symmetry generate exactly 3 generations? Failure drops framework to <= 25%. (Session 21d)

---

## IX. The Honest Question — Per-Agent Responses

*"What single computation would FALSIFY the resonance interpretation?"*

**tesla**: V_IR(tau) for p+q <= 2. If the lowest ~150 eigenvalues show the same constant-ratio behavior as the full spectrum (F/B constant, energy monotonic), then the "low-mode resonance" claim is empirically closed. There is no special frequency where the cavity shape matters. The trap extends from the UV all the way to the IR, and no reweighting or reinterpretation changes the answer.

**landau**: V''_total(tau) sign. If V'' > 0 everywhere (convex potential), there is no spinodal, no barrier, and no first-order transition. The cubic term V'''(0) = -7.2 predicts non-convexity, but the actual V'' could be dominated by the quadratic term. If V'' > 0 everywhere, the modulus is a stable harmonic oscillator with no phase transition at all.

**connes**: |T'(tau_0)| at the fixed point (if it exists). If |T'(tau_0) - 1| > 2, the fixed point is a repeller — the self-consistency map sends tau AWAY from tau_0, not toward it. Stability requires -2 < T'(tau_0) - 1 < 0. Even if V_IR has a minimum and T has a zero-crossing, an unstable fixed point means the system cannot settle.

**feynman**: T''(0) <= 0. If the second derivative of the self-consistency map at the round point is non-positive, there is no perturbative fixed point at tau > 0 and the signed-sum escape produces nothing. Combined with V_IR monotonic, this closes the perturbative route completely and leaves only instantons.

**quantum-acoustics**: Low-mode F/B for the full Dirac spectrum (not just TT). The A-1 computation uses TT 2-tensors only. If the FULL low-mode Dirac F/B (bosonic scalars + vectors + TT vs fermionic) also shows the constant-ratio trap at N <= 50, then even the phonon interpretation collapses — there is no acoustic branch with different physics from the optical branch.

---

## X. Coordinator Notes (Running Log)

### Progress Tracking

| Task | Agent | Status | Delivered |
|:-----|:------|:-------|:---------|
| A-1: Resonance reinterpretation | tesla | **COMPLETE** | s21a_low_mode_TT_casimir.py; s21a_low_mode_TT.npz; s21a_low_mode_TT.png |
| A-2: Self-consistency map | feynman + tesla | **COMPLETE** | feynman to tesla; landau A-2 support + T''(0) addendum delivered |
| A-3: Phase transition classification | landau | **COMPLETE** | delivered to tesla; addendum T''(0) also delivered |
| A-4: NCG-phonon dictionary | connes | **COMPLETE** | delivered to tesla; IR follow-up with (0,0) level-crossing table |
| A-5: Inside-out interpretation | quantum-acoustics | **COMPLETE + 4 ADDENDA** | Base + signed-sum test + BCS bifurcation verification |
| A-6: Unified synthesis | tesla | **COMPLETE** | This document |

### Cross-Pollination Log

| From | To | Insight |
|:-----|:---|:--------|
| feynman | all | Z_2 path integral distinct from Z_1; T = identity at tree level (triviality obstruction) |
| feynman + connes | all | Theorem boundary: positive sums CLOSED (AM-GM), signed sums OPEN |
| feynman + connes + landau | all | TRIPLE CONVERGENCE: T''(0) > 0 gate from signed sums. New panel finding, not in 20b or Primer. |
| landau | all | V'''(0) = -7.2 forces first-order; Ginzburg d_eff=1; BKT analogy |
| quantum-acoustics | all | Low-mode F/B 25% variation; (1,1) stiffens uniquely; BCS-BEC inverted at tau~0.40 |
| quantum-acoustics | all | K_signed = 0 by conjugation symmetry; anisotropic b_1-b_2 weights required |
| connes | all | 8 cutoffs all monotonic; (0,0) level-crossing at tau~0.2 real but 16 vs 439k DOF |
| connes + quantum-acoustics | all | BCS bifurcation VERIFIED: 1/lambda_min peaks at tau=0.2, gap DOF collapse 36->2 |
| landau | tesla | 25% low-mode F/B variation breaks trap in IR; (1,1) stiffening = order parameter direction |
| feynman | tesla | V_IR validated by QA 25% result; phi_paasch (3,0) sector link; g(tau) quantitative input |

### Key Session Findings (New, Not In 20b/20c)

1. **Signed spectral sums escape the constant-ratio trap** — Feynman-Connes-Landau triple convergence. AM-GM only applies to positive weights. Gauge threshold corrections (b_1 - b_2) are signed. First perturbative escape route identified.

2. **Conjugation symmetry constrains the escape** — QA proves simple Z_3-charge sums cancel exactly. The signed weight must use anisotropic gauge-coupling-specific branching (b_1 - b_2 from SU(3) -> SU(2) x U(1)), not SU(3) representation labels alone.

3. **BCS bifurcation at tau = 0.2** — Connes + QA independently verify. 1/lambda_min peaks, gap-edge DOF collapse 36->2, gap sector switches from (0,1)+(1,0) to (0,0) alone. Independent of constant-ratio trap (single eigenvalue, not spectral sum).

4. **Low-mode TT Casimir divergence** — Tesla A-1 computation. Lowest 20 modes grow 65x vs full 4.4x. Schwinger spectral action DECREASES for Lambda <= 5. IR and UV regimes are categorically different.

5. **T''(0) > 0 gate** — Pre-registered binary Constraint Condition for Session 21b. Computable from branching rules + existing data. Prerequisite for self-consistency interpretation.

### Divergence Alerts (Final Status)

1. **Connes 8-cutoff vs QA 25% low-mode F/B**: RESOLVED. Both correct — different regimes (UV vs IR).
2. **Priority ordering**: RESOLVED. Logical dependency: T''(0) sign -> V_IR -> delta_T.
3. **T = identity at tree level**: NOT RESOLVED. Central tension. T''(0) gate is the test.
4. **Conjugation symmetry vs signed sums**: PARTIALLY RESOLVED. Simple charges cancel; gauge-threshold weights may not. Computation needed.

---

### Post-Synthesis: T''(0) Implementation Brief (feynman, post-session)

Feynman delivered an explicit coding brief for the T''(0) gate computation. Recorded here for the Session 21b coder.

**Data files:**
- `tier0-computation/s19a_sweep_data.npz` — 11,424 Dirac eigenvalues at 21 tau values (tau=0.0 to 2.0, step 0.1). Keys: `tau_values`, `eigenvalues_{i}`, `sector_p_{i}`, `sector_q_{i}`, `multiplicities_{i}`, `fermionic_mult_{i}` for i=0..20.
- `tier0-computation/kk1_bosonic_spectrum.npz` — 2,170 bosonic modes at 4 tau values (0.0, 0.15, 0.30, 0.50).
- `tier0-computation/l20_TT_spectrum.npz` — Aggregate E_TT(tau) only, no per-mode eigenvalues.

**Numerical derivatives at tau=0 (from 21-point grid, dtau=0.1):**
```python
dlam_dtau_0  = (-3*lam[0] + 4*lam[1] - lam[2]) / (2 * 0.1)      # forward 2nd-order
d2lam_dtau2_0 = (2*lam[0] - 5*lam[1] + 4*lam[2] - lam[3]) / (0.1**2)  # forward 2nd-order
```

**delta_T(tau) formula:**
```
delta_T(tau) = (1 / (64 pi^2 e^{4*tau})) * Sum_n Delta_b(p_n, q_n) * ln(mu^2 / lambda_n(tau))
```
where mu = 1.0 (units: round SU(3) with R_K=1). Sign of T''(0) is mu-independent.

**Two implementation options:**

Option 1 — Exact (~100 lines, needs SU(3) branching):
- For each (p,q), compute Delta_b(p,q) = (2/3)[Sum_Y Y^2 - Sum_j T_2(j)] from SU(3)->SU(2)xU(1) weight enumeration.
- T_2(j) = j(j+1)(2j+1)/3. Check: j=1/2 gives T_2=1/2. U(1): T_1 = Y^2 per state.
- Evaluate delta_T at 21 tau points. Find zero crossing. Slope at crossing = T'(tau_0). Second derivative at tau=0 = T''(0).

Option 2 — Proxy (~30 lines, no branching):
- Delta_b_proxy(p,q) = (p-q)^2/3 - p(p+2)/6 (U(1) charge squared minus SU(2) Casimir at dominant weight).
- Same delta_T formula. Captures qualitative sign; may miss quantitative accuracy.

**Constraint Gate:** T''(0) > 0 = ALIVE. T''(0) <= 0 = CLOSED (no physical fixed point at tau > 0).

**Conjugation constraint (quantum-acoustics):** Simple (p-q) charges cancel by (p,q)<->(q,p) symmetry. Must use anisotropic b_1-b_2 gauge-threshold weights, not SU(3) representation labels alone.

*Recorded by coordinator, 2026-02-19 post-session.*

---

### Post-Synthesis: V''_total Spinodal Scan — COMPLETE (landau, post-session)

**Data source:** `tier0-computation/l20_vtotal_minimum.npz` (21-point Session 20b data)

**Result: V''_total > 0 EVERYWHERE. No spinodal in the full perturbative potential.**

| tau | V''_CW | V''_Casimir | Sign |
|:----|:-------|:------------|:-----|
| 0.0 | 1.20e+08 | 2.91e+05 | POS |
| 0.1 | 1.99e+08 | 4.32e+05 | POS |
| 0.3 | 4.88e+08 | 5.64e+05 | POS |
| 0.5 | 1.16e+09 | 5.86e+05 | POS |
| 1.0 | 1.09e+10 | 7.59e+05 | POS |
| 2.0 | 2.66e+11 | 8.28e+05 | POS |

V_cw is ~50x larger than E_casimir in absolute value; ~400x in second derivative. Full V_total dominated by V_cw, growing exponentially (~1.55x per dtau=0.1). V_total is not merely monotonic — it is exponentially convex.

**Interpretation:** Spinodal search in V_total is CLOSED. Any first-order transition requires either (a) non-perturbative physics at a scale overcoming exponential UV convexity, or (b) non-convexity that lives entirely in V_IR where small eigenvalues contribute little to V_cw and V_tree/V_cw are comparable. V_IR is the only remaining perturbative regime where a spinodal can appear.

**Section VIII update:** V''_total spinodal scan (was Tier 2 item #9) is DONE — answer is no spinodal. Demote to COMPLETED. V_IR for p+q<=2 confirmed as the decisive remaining test.

*Recorded by coordinator, 2026-02-19 post-session.*

---

### Post-Synthesis: 4-Sector Low-Mode F/B and Gap-Edge Convergence (quantum-acoustics, post-session)

**Question**: Does the 25% TT-only low-mode F/B variation survive in the full 4-sector Casimir (scalar + vector + TT + Dirac)?

**Answer: YES — and it's more dramatic than expected.**

#### Full 4-Sector Results (TT excluded from low-mode pool — min TT eigenvalue ~1.0 sits above the pool)

**Separate-pool counting** (lowest N from each sector independently — physical Casimir):

| N_cut | F/B range (tau 0.0-0.50) | Variation | Direction |
|:------|:-------------------------|:----------|:----------|
| 20 | 1.37 - 1.87 | 37% | Monotonically increasing |
| 50 | 1.37 - 1.65 | 21% | Monotonically increasing |
| 100 | 1.38 - 1.56 | 13% | Monotonically increasing |
| 200 | 1.30 - 1.43 | 11% | Monotonically increasing |
| Full | 0.553 - 0.558 | 1.8% | The constant-ratio trap |

**Fermions dominate bosons for the first 14,000-25,000 modes.** F/B crossover (F/B = 1) occurs at N_cross ~ 14,000 (tau=0) to ~25,000 (tau=0.5).

#### Gap-Edge Separation (Algebraic Identity at tau=0)

| tau | Bos gap (lambda_min) | Ferm gap (lambda_min) | Ratio | Note |
|:----|:--------------------|:---------------------|:------|:-----|
| 0.00 | 4/9 = 0.4444 | 5/6 = 0.8333 | 15/8 = 1.875 | **ALGEBRAIC** |
| 0.15 | 0.3692 | 0.8315 | 2.25 | |
| 0.30 | 0.3079 | 0.8221 | 2.67 | |
| 0.50 | 0.2431 | 0.8732 | 3.59 | |

The fermionic Dirac gap on round SU(3) is exactly 5/6 ((0,1) sector, degen 36). The bosonic Laplacian gap is exactly 4/9. Each fermionic mode carries sqrt(15/8) = 1.369x more zero-point energy. Jensen deformation WIDENS the separation: bosonic gap softens monotonically, fermionic gap rigid for tau < 0.3 (BDI topological protection), then slowly rises.

#### BCS Self-Consistency Mechanism (Enabled, Not Proven)

The gap-edge structure enables a natural BCS-type stabilization:
1. **Lambda_IR below fermionic gap** (< 0.83): Only bosonic modes contribute. V_eff decreases with tau. Runaway.
2. **Lambda_IR above fermionic gap**: Fermionic modes enter and DOMINATE (F/B > 1). Restoring force.
3. **Equilibrium**: Self-consistency condition lambda_ferm_min(tau_0) = Lambda_IR(tau_0). NOT energy minimization — self-consistency of a dynamical cutoff.

#### Honest Caveats
- **Phi match collapsed**: Energy ratio at tau=0.50 appeared to match phi_paasch^{3/2} at 0.2 ppm, but precise recomputation gives 0.54% match. Near-miss, not a hit.
- **N_cross ~ 20,000 is large**: Whether the physical cutoff sits in the fermion-dominated regime depends on dynamics not yet computed.
- **Probability unchanged**: 38-46% range. Sharpens mechanism but doesn't resolve dynamics.

#### Verdict for V_IR Gate
V_IR is REAL as a diagnostic. Low-mode F/B varies 10-37% vs 1.8% full-spectrum. The constant-ratio trap is definitively a UV phenomenon. BUT: separate-pool F/B is monotonically increasing in available data — V_IR minimum existence still requires computation at more tau values or with IR-weighted kernels.

*Recorded by team-lead from quantum-acoustics follow-up response, 2026-02-19 post-session.*

---

*Written by tesla-resonance, 2026-02-19. Integrated from contributions by feynman, landau, connes, quantum-acoustics, with coordination by coordinator. Post-session follow-ups appended by coordinator and team-lead.*
