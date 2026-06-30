# Ten Proofs of the Generalized Second Law

**Author(s):** Aron C. Wall
**Year:** 2009
**Journal:** Physical Review D (also PhD-related work, Maryland Center for Fundamental Physics)
**arXiv:** 0901.3865
**Relevance:** HIGH

---

## Abstract

Ten attempts to prove the Generalized Second Law of Thermodynamics (GSL) are described and critiqued. Each proof provides valuable insights which should be useful for constructing future, more complete proofs. Rather than merely summarizing previous research, this review offers new perspectives, and strategies for overcoming limitations of the existing proofs. A long introductory section addresses some choices that must be made in any formulation of the GSL: Should one use the Gibbs or the Boltzmann entropy? Should one use the global or the apparent horizon? Is it necessary to assume any entropy bounds? If the area has quantum fluctuations, should the GSL apply to the average area? The definitions and implications of the classical, hydrodynamic, semiclassical and full quantum gravity regimes are also discussed. A lack of agreement regarding how to define the "quasi-stationary" regime is addressed by distinguishing it from the "quasi-steady" regime.

---

## Key Arguments and Derivations

### Section 1: Introduction
**1.1 - The Generalized Second Law**:
The GSL states that the generalized entropy S_gen = (k A) / (4 G hbar) + S_out is nondecreasing with time, where A is the total area of all black hole horizons and S_out is the thermodynamic entropy of matter outside all event horizons.

**1.1.1 - Boltzmann vs Gibbs entropy**: Compares the two definitions:
- Boltzmann entropy: S = k ln N (number of microstates in a macrostate). Fluctuates.
- Gibbs entropy: S = -k Tr(rho ln rho). Conserved under unitary evolution, does not fluctuate.
- For the area term, the Gibbs approach gives S_gen = k Tr(rho(A - ln rho)) = k(<A>/4G hbar - Tr(rho ln rho))
- The GSL is easier to prove than the ordinary second law because the horizon provides an objective definition of what is observable outside, without requiring arbitrary coarse-graining.

**1.1.2 - Choice of horizon**:
- The GSL holds for the global event horizon (boundary of the past of I^+), not for arbitrary null surfaces
- Example: a trapped surface inside a Schwarzschild black hole has classically decreasing area of order G^{-1}, which cannot be compensated by matter entropy
- Apparent horizons are sometimes proposed (Hayward 2006), but the event horizon is preferred because it is always null, uses the more fundamental causal structure, and is less sensitive to metric fluctuations

**1.2 - Types of Regimes**:
Distinguishes carefully between:
- **Quasi-stationary**: small perturbation to a stationary metric (any time dependence)
- **Quasi-steady**: the matter is in an approximately steady state with respect to the horizon-generating Killing field (more restrictive)
- **Adiabatic**: first-order deviation from the Hartle-Hawking equilibrium state (most restrictive)

**The First Law of black hole mechanics** (reproduces Bardeen, Carter & Hawking 1973):
- In the quasi-steady regime: dE = T dS_BH + Omega dJ + Phi dQ
- Compact form using horizon generating Killing field: dE' = T dS with E' = E - Omega J - Phi Q

**1.2.3 - Classical BH thermodynamics**: The area theorem (Hawking 1971) is proved via the Raychaudhuri equation:
- -d theta / d lambda = (1/2) theta^2 + sigma_{ab} sigma^{ab} + 8 pi G T_{ab} k^a k^b
- Right-hand side is always positive by the null energy condition
- Therefore a generator with negative expansion must terminate at a finite affine parameter
- Since there are no singularities on the horizon (by assumption), all generators have non-decreasing area

**1.2.5 - Semiclassical regime**: The semiclassical Einstein equation G_{ab} = 8 pi G <T_{ab}> neglects gravitational fluctuations. Valid in the large N limit (matter fluctuations ~ sqrt{N} while effect ~ N) or quasi-stationary limit.

**1.3 - Entropy bounds**: Discusses whether the Bekenstein bound (S <= 2pi E R) or other entropy bounds are needed as separate assumptions for the GSL.

### Section 2: Proofs using the Ordinary Second Law (OSL) Applied to the Thermal Atmosphere
**2.1 - Proof by analogy to an ordinary blackbody (Zurek & Thorne 1985)**:
- Models the black hole as a blackbody in thermal equilibrium with its thermal atmosphere
- Objects dropped into the black hole are first thermalized by the atmosphere
- The entropy increase follows from the OSL applied to this thermalization
- Limitation: requires a "stretched horizon" and entropy localization assumptions

**2.2 - Proof by perturbing the thermal atmosphere (Wald 1994)**:
- Uses the first law: delta E' = T delta S
- For a perturbation from the Hartle-Hawking state, delta S_gen >= 0 follows from the positivity of relative entropy
- Works in the adiabatic regime
- Limitation: originally required adiabaticity, but this can be weakened

### Section 3: Proof using the S-Matrix (Frolov & Page 1993)
- Uses CPT invariance to relate the initial and final states
- In the quasi-steady regime, the Hartle-Hawking state is CPT invariant
- Since the Hartle-Hawking state maximizes entropy for given energy, any perturbation has less entropy
- This proves the GSL for quasi-steady perturbations
- Limitation: CPT alone is insufficient for charged black holes (needs extension)

### Section 4: Proofs from a Time-Independent State
**4.1 - Full quantum gravity version (Sorkin 1986)**:
- Uses the monotonicity of relative entropy under restriction to subalgebras
- The generalized entropy can be written as S_gen = S(rho || sigma) + constant for appropriate reference state sigma
- The increase of S_gen follows from a quantum channel inequality
- **Key theorem (Theorem 1)**: If a completely positive map Phi preserves a state sigma, then S(Phi(rho) || sigma) <= S(rho || sigma) for all states rho
- Limitation: the original assumptions are inconsistent (identified by Wall)

**4.2 - Semiclassical quasi-steady version (Sorkin 1998)**:
- Restricts to semiclassical gravity and uses the Bisognano-Wichmann theorem
- The Hartle-Hawking state is the KMS state at the Hawking temperature
- Monotonicity of relative entropy under restriction to the exterior algebra gives the GSL
- Limitation: requires thermality and non-superradiance

**4.3 - Combined with S-matrix (Mukohyama 1997)**:
- Combines Sorkin's approach with the S-matrix method
- Works for free scalar fields in the quasi-steady regime

### Section 5: Proofs via the Generalized Covariant Entropy Bound
**5.1 - Bekenstein-bound-inspired assumption (Flanagan, Marolf & Wald 2000)**:
- Uses the Bousso covariant entropy bound applied to light sheets
- If matter entropy on a light sheet satisfies S <= A/4G, then the GSL follows
- Works in the classical hydrodynamic regime for any perturbation size

**5.2 - Entropy gradient assumption (Bousso, Flanagan & Marolf 2003)**:
- Weakens the Bekenstein bound to a local entropy gradient condition
- Plus an "isolation condition" that the light sheet is not influenced by distant sources

### Section 6: 2D Black Holes (Fiola, Preskill, Strominger & Trivedi 1994)
- Uses the RST model (dilaton gravity in 1+1 dimensions)
- Explicitly computes the generalized entropy and shows it increases
- Works in the large N semiclassical regime for arbitrary (non-quasi-stationary) perturbations
- Uses the apparent horizon rather than the event horizon
- This is the only proof that goes beyond the quasi-stationary regime in more than two dimensions

### Section 7: Prospects
- No fully satisfactory proof exists in all regimes
- The main open problems: extending to non-quasi-steady perturbations in 4D, incorporating superradiance, and understanding the GSL in full quantum gravity
- A deeper understanding of the GSL requires a theory of quantum gravity

---

## Key Results

1. **Generalized entropy**: S_gen = A/(4G) + S_out is the correct thermodynamic entropy for gravitational systems with horizons.

2. **Raychaudhuri-based area theorem**: The classical second law (area increase) follows from the Raychaudhuri equation plus the null energy condition.

3. **Monotonicity of relative entropy (Theorem 1)**: If a completely positive map preserves a state sigma, then relative entropy S(Phi(rho) || sigma) <= S(rho || sigma). This is the mathematical backbone for the most rigorous GSL proofs.

4. **Ten distinct proof strategies**: Each operates in a different regime (classical, hydrodynamic, semiclassical, full QG) with different assumptions. None is complete.

5. **Quasi-stationary vs quasi-steady distinction**: These are different regimes previously conflated in the literature. Quasi-steady requires approximate stationarity of matter, not just of the metric.

6. **GSL is easier than the ordinary second law**: The horizon provides an objective coarse-graining, removing the need for arbitrary choices.

7. **The GSL applies to event horizons, not arbitrary null surfaces**: Trapped surfaces inside black holes have decreasing area that cannot be compensated by matter entropy.

8. **Table of proofs**: Wall provides a comprehensive table classifying all ten proofs by regime, perturbation type, and limitations.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Generalized entropy | $S_{\rm gen} = \frac{kA}{4G\hbar} + S_{\rm out}$ | Eq. 1 |
| Gibbs entropy | $S = -k\, {\rm tr}(\rho \ln \rho)$ | Eq. 3 |
| Generalized entropy (trace form) | $S_{\rm gen} = k\, {\rm tr}\!\left(\rho\!\left(\frac{A}{4G\hbar} - \ln\rho\right)\right) = k\!\left(\frac{\langle A\rangle}{4G\hbar} - {\rm tr}(\rho\ln\rho)\right)$ | Eq. 4 |
| First Law (compact) | $dE' = T\, dS_{\rm BH}$ | Eq. 9 |
| Raychaudhuri equation | $-\frac{d\theta}{d\lambda} = \frac{1}{2}\theta^2 + \sigma_{ab}\sigma^{ab} + 8\pi G\, T_{ab} k^a k^b$ | Eq. 11 |
| Semiclassical Einstein eq. | $G_{ab} = 8\pi G \langle T_{ab} \rangle$ | Eq. 12 |
| Adiabatic perturbation | $\sigma(\epsilon) = (1-\epsilon)\rho_{\rm HH} + \epsilon\,\rho$ | Eq. 10 |
| Quasi-steady conditions | $R\, dS_{\rm BH}/dt \ll S_{\rm BH}$; $R\, d^2 S_{\rm BH}/dt^2 \ll dS_{\rm BH}/dt$ | Eqs. 5-6 |

## Relevance to Phonon-Exflation

Wall's systematic treatment of the GSL is relevant to the phonon-exflation framework in several ways. The spectral action = entropy identification pursued in earlier sessions connects directly to the generalized entropy formula S_gen = A/4G + S_out. The framework's KK geometry has no horizon, so the GSL as stated does not directly apply, but the underlying principle --- that the total entropy (geometric + matter) is nondecreasing --- constrains the transit dynamics. The monotonicity of relative entropy (Theorem 1, Section 4.1) is the same mathematical tool (completely positive maps preserving reference states) that appears in the framework's analysis of the GGE relic: the post-transit state is a fixed point of the reduced dynamics, and its entropy is maximal given the conserved quantities. The Raychaudhuri equation formalism (Eq. 11) is the classical backbone for understanding how the KK fiber's expansion/contraction during transit affects the 4D observer's spacetime.
