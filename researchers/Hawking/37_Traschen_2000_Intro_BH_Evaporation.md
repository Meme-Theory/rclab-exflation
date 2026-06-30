# An Introduction to Black Hole Evaporation

**Author(s):** Jennie Traschen
**Year:** 2000
**Journal:** Lecture notes (University of Massachusetts)
**arXiv:** gr-qc/0010055
**Relevance:** HIGH

---

## Abstract

Classical black holes are defined by the property that things can go in, but don't come out. However, Stephen Hawking calculated that black holes actually radiate quantum mechanical particles. The two important ingredients that result in black hole evaporation are (1) the spacetime geometry, in particular the black hole horizon, and (2) the fact that the notion of a "particle" is not an invariant concept in quantum field theory. These notes contain a step-by-step presentation of Hawking's calculation. We review portions of quantum field theory in curved spacetime and basic results about static black hole geometries, so that the discussion is self-contained. Calculations are presented for quantum particle production for an accelerated observer in flat spacetime, a black hole which forms from gravitational collapse, an eternal Schwarzschild black hole, and charged black holes in asymptotically deSitter spacetimes. The presentation highlights the similarities in all these calculations. Hawking radiation from black holes also points to a profound connection between black hole dynamics and classical thermodynamics. A theory of quantum gravity must predict and explain black hole thermodynamics. We briefly discuss these issues and point out a connection between black hole evaporation and the positive mass theorems in general relativity.

---

## Key Arguments and Derivations

### Section 1: Introduction
Reviews the three laws of classical black hole mechanics and their formal analogy with thermodynamics:
- **Zeroth law**: surface gravity kappa is constant on the horizon
- **First law**: delta_M = (kappa/8pi) delta_A + Omega delta_L - nu delta_Q (reproduces Bardeen, Carter & Hawking 1973)
- **Second law**: Hawking's area theorem delta_A >= 0 (reproduces Hawking 1971)

Notes the formal identification kappa <-> T and A <-> S, and the puzzle that classically black holes do not radiate. Reviews Bekenstein's 1973 conjecture and Hawking's 1975 resolution.

### Section 2: Quantum Fields in Curved Spacetimes
Develops the full Bogoliubov transformation formalism from scratch:
- Canonical quantization of a free scalar field satisfying the wave equation g^{ab} nabla_a nabla_b phi = 0
- Defines the conserved Klein-Gordon inner product on a Cauchy surface
- Constructs two complete bases {f_omega, f*_omega} and {p_omega, p*_omega} with their respective Fock spaces
- Derives the Bogoliubov coefficients alpha_{omega omega'} = (p_omega, f_{omega'}) and beta_{omega omega'} = -(p_omega, f*_{omega'})
- Shows the key particle production formula: <0_in | N^out_omega | 0_in> = integral |beta_{omega omega'}|^2 d omega'
- Emphasizes that the physics input is the choice of state and choice of time coordinate defining "positive frequency"

### Section 3: Accelerating Observers in Flat Spacetime (Rindler calculation)
Performs the Unruh effect calculation as a warm-up for Hawking radiation:
- Works in 1+1 Minkowski spacetime with null coordinates
- Defines Rindler coordinates covering the wedge region, with metric ds^2 = e^{2a xi}(-dT^2 + d xi^2)
- A Rindler observer at constant xi has constant acceleration ae^{-a xi}, proper time T
- Computes Bogoliubov coefficients by integrating over the past Cauchy horizon H^-
- Obtains alpha_{omega omega'} = (i/2pi)(1/sqrt{omega' omega})(i omega')^{-i omega/a} Gamma(1 + i omega/a)
- Derives the thermal spectrum <N^rind_omega> = 1/(e^{2pi omega / hbar a} - 1) at temperature T = hbar a / 2pi

### Section 4: Black Holes
Reviews Schwarzschild geometry in multiple coordinate systems:
- Standard coordinates (t, r), tortoise coordinate r*, null coordinates (u, v), and Kruskal coordinates (U, V)
- Surface gravity kappa = (1/2) V'(r_H) for static metrics of the form ds^2 = -V(r)dt^2 + dr^2/V + r^2 d Omega^2
- Separates the scalar wave equation into a radial Schrodinger-type equation with potential W(r) = (1 - 2M/r)(2M/r^3 + l(l+1)/r^2)
- Solutions are plane waves in (t +/- r*) both near the horizon and at infinity

### Section 5: Particle Emission from Black Holes (Hawking's calculation)
**Reproduces Hawking (1975) step by step** for the gravitational collapse spacetime:
1. Sets boundary conditions: positive frequency modes f_omega ~ e^{-i omega v} on I^- define the in-vacuum |0>_in
2. Out-modes p_omega ~ e^{-i omega u} on I^+ and modes q_omega on H^+ form the late-time basis
3. The reduced density matrix rho_red = Tr_{H+} rho makes <O_AF> independent of the choice of q_omega on H^+
4. Traces a ray gamma backwards from I^+ through the collapsing star to I^-
5. Uses geodesic deviation near H^+ to derive the key relation: v_0 - v = C^2 e^{-kappa u}
6. This gives phi ~ e^{(i omega / kappa) ln(v_0 - v)/C^2} on I^-
7. Computes the Bogoliubov coefficients: alpha_{omega omega'} is analytic in the lower half omega' plane with |alpha_{omega omega'}| = e^{pi omega / kappa} |beta_{omega omega'}|
8. Derives the thermal spectrum: <N^bh_omega> = Gamma_omega / (e^{2pi omega / hbar kappa} - 1)

This is **the same** Bogoliubov coefficient structure as the Rindler calculation, with acceleration a replaced by surface gravity kappa.

### Section 6: Extended Schwarzschild and Reissner-Nordstrom-deSitter Spacetimes
- **Eternal Schwarzschild**: Defines positive frequency on horizons using Kruskal coordinates (affine parameters for null generators), recovering the same thermal spectrum
- **Charged black holes in deSitter**: Treats RNdS spacetimes with three Killing horizons. Two sources of particle production (black hole and deSitter horizons). Shows the two fluxes equilibrate (beta^bh = beta^ds) if and only if |Q| = M (extremal). The equilibrium spectrum is non-thermal: <N_omega> = (pi^2/6)(kappa^2/8omega + kappa/2 sqrt{c/omega}) e^{-4 sqrt{c omega}/kappa}

### Section 7: Black Hole Evaporation and Positive Mass Theorems
- Connects positive mass theorems (M >= |Q|) to BPS states: extremal (M = |Q|) black holes have T = 0 and are the ground states
- Non-extremal black holes evaporate down to extremality, where evaporation stops
- Discusses string theory D-brane microstate counting (Strominger-Vafa) reproducing S = A/4
- Notes the puzzle: the role of the horizon in defining black hole entropy is still a mystery in string calculations

## Key Results

1. **Particle production is observer-dependent**: The definition of a "particle" depends on the choice of time coordinate/reference frame. This is the fundamental mechanism behind both the Unruh effect and Hawking radiation.

2. **Hawking temperature**: T = hbar kappa / 2pi, where kappa is the surface gravity. For Schwarzschild, kappa = 1/4M.

3. **Bekenstein-Hawking entropy**: S_bh = A/4 follows from the thermodynamic identification.

4. **Generalized thermal spectrum**: For charged/rotating black holes, <N^bh_omega> = Gamma_omega / (e^{2pi(omega - mu)/hbar kappa} +/- 1), where mu is the chemical potential and +1 for fermions, -1 for bosons.

5. **RNdS thermal equilibrium**: Two horizons in Reissner-Nordstrom-deSitter are in thermal equilibrium if and only if |Q| = M (extremal case).

6. **BPS stability**: Extremal black holes (T = 0) are quantum mechanically stable endpoints of Hawking evaporation, connected to positive mass theorems.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Klein-Gordon inner product | $(f,h) = -i \int d^3x \sqrt{-g} (f \dot{h}^* - \dot{f} h^*)$ | Eq. 2.5 |
| Bogoliubov coefficients | $\alpha_{\omega\omega'} = (p_\omega, f_{\omega'})$, $\beta_{\omega\omega'} = -(p_\omega, f^*_{\omega'})$ | Eq. 2.17 |
| Particle number | $\langle 0_{\rm in} | N^{\rm out}_\omega | 0_{\rm in} \rangle = \int d\omega' |\beta_{\omega\omega'}|^2$ | Eq. 2.20 |
| Rindler temperature | $T = \hbar a / 2\pi$ | Eq. 3.34 |
| Key geometric optics relation | $v_0 - v = C^2 e^{-\kappa u}$ | Eq. 5.57 |
| Hawking spectrum | $\langle N^{\rm bh}_\omega \rangle = \Gamma_\omega / (e^{2\pi\omega/\hbar\kappa} - 1)$ | Eq. 5.65 |
| Hawking temperature | $T = \hbar \kappa / 2\pi$ | Eq. 5.66 |
| Generalized spectrum (charged/rotating) | $\langle N^{\rm bh}_\omega \rangle = \Gamma_\omega / (e^{2\pi(\omega-\mu)/\hbar\kappa} \pm 1)$ | Eq. 5.69 |
| Bekenstein-Hawking entropy | $S_{\rm bh} = A/4$ | Eq. 5.68 |
| Kruskal coordinate | $U = -e^{-u/4M}$, $V = e^{v/4M}$ | Eq. 4.41 |

## Relevance to Phonon-Exflation

Traschen's step-by-step reproduction of the Bogoliubov transformation formalism is directly relevant to the phonon-exflation framework, where transit through the KK fold is Parker-type cosmological particle creation. The key relation v_0 - v = C^2 e^{-kappa u} (Eq. 5.57) has the same mathematical structure as the exponential map between affine parameters across a horizon, which parallels the exponential relationship between tau and the compactification modulus during transit. The framework's sudden quench (P_exc = 1.000, S38) produces a non-thermal GGE relic rather than a thermal Hawking spectrum precisely because there is no horizon in the KK geometry --- the particle creation is Parker-type (cosmological), not Hawking-type (horizon). The Bogoliubov coefficient technology reviewed here is the mathematical backbone for computing quasiparticle production in the instanton gas transit.
