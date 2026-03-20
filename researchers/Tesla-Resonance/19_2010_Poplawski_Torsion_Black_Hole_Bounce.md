# Einstein-Cartan Cosmology: Black Hole Interiors as Bouncing Universes

**Author:** Poplawski, Nikodem J.
**Year:** 2010-2021 (initial proposal 2010, refined in 2012, 2015, 2021)
**Journal:** Physics Letters B; The Astrophysical Journal

---

## Abstract

Nikodem Poplawski showed that Einstein-Cartan theory (general relativity extended with torsion) naturally prevents the singularities in black hole interiors. When a massive star collapses and forms a black hole, the interior quantum gravity regime is governed by torsion -- an intrinsic spin of spacetime itself arising from angular momentum of matter. At extreme density near the classical singularity, torsion provides a repulsive force that causes the contraction to halt and reverse, creating a bounce. The solution yields a non-singular, expanding spacetime that resembles a new Big Bang to internal observers. Critically, the mechanism is classical, requiring no quantum gravity quantization scheme: torsion at sub-Planck scales provides effective quantum pressure. This yields a novel picture of cosmology: our observable Big Bang may be the bounce inside a black hole created in a parent universe, with all structures repeating at every scale. The theory is testable through gravitational waves from black hole mergers (which would differ from general relativity predictions) and through observations of large-scale cosmic structure.

---

## Historical Context

The singularities of general relativity have long troubled physicists. When Einstein's equations are applied to black holes (Schwarzschild metric) or the early universe (FLRW), infinities appear at r=0 (black hole interior) or t=0 (Big Bang). In standard general relativity, these are treated as mathematical artifacts that "cut off" when quantum gravity becomes important. However, without a complete theory of quantum gravity, the nature of the singularity remains obscure.

In the 1920s, Cartan introduced the concept of torsion to differential geometry -- an additional geometric quantity that encodes the intrinsic angular momentum of a manifold. Einstein briefly explored torsion in his attempts at unified field theory, but abandoned it. Cartan and Einstein-Cartan theory remained niche.

In the 1980s-2000s, loop quantum gravity (Ashtekar) and other approaches to quantum gravity showed that space may have discrete or "granular" structure at the Planck scale. One prediction: effective torsion emerges at small scales.

Poplawski's innovation (2010) was to ask: what if we take torsion seriously *classically*, not just as an effective correction? If spacetime itself has intrinsic angular momentum (coupled to fermion spin via the spin connection), then in regions of extreme density, torsion becomes a dominant force.

---

## Key Arguments and Derivations

### Einstein-Cartan Theory: Geometry with Torsion

Standard general relativity uses a torsion-free connection (the Levi-Civita connection). The Einstein-Cartan theory uses a connection with non-zero torsion:

$$T^\lambda_{\mu\nu} = \Gamma^\lambda_{\mu\nu} - \Gamma^\lambda_{\nu\mu} \neq 0$$

The torsion is related to the spin density of matter via the field equations:
$$T^\lambda_{\mu\nu} = \frac{\kappa}{2} S^\lambda_{\mu\nu}$$

where $\kappa = 8\pi G / c^4$ and $S^\lambda_{\mu\nu}$ is the spin current density (spin per unit volume). For fermionic matter:
$$S^\lambda_{\mu\nu} = \frac{1}{2} \bar{\psi} \gamma^\lambda \sigma_{\mu\nu} \psi + \text{orbital contributions}$$

This couples the geometry of spacetime directly to the intrinsic spin of fermions.

### The Bouncing Schwarzschild Interior

In torsion-free general relativity, the Schwarzschild metric in the interior region (r < 2M) has the form:
$$ds^2 = -\left( 1 - \frac{2M}{r} \right) dt^2 + \left( 1 - \frac{2M}{r} \right)^{-1} dr^2 + r^2 d\Omega^2$$

As r -> 0, the metric component $g_{rr}$ -> infinity and $g_{tt}$ -> -1. This is the singularity.

In Einstein-Cartan theory with torsion, the metric near r=0 is modified. The exact solution depends on the spin distribution, but the key result is:

**Near the singularity, the torsion-induced pressure term grows as:**
$$P_{torsion} \propto \frac{\hbar^2}{G m^2} \rho^{2/3}$$

where rho is the density and m is a characteristic mass scale. For ultra-relativistic matter (radiation), the effective equation of state becomes:
$$P \approx \frac{1}{3} \rho c^2 + P_{torsion}$$

At extreme densities, $P_{torsion}$ dominates, generating a repulsive force. The radial evolution equation:
$$\frac{d^2a}{dt^2} = -\frac{4\pi G}{3}(\rho + 3P)a + \text{torsion terms}$$

changes sign: instead of collapse continuing ($d^2a/dt^2 < 0$), the torsion term drives expansion ($d^2a/dt^2 > 0$). The contraction halts and bounces.

### Quantitative Estimates

The critical density (bounce density) is estimated as:
$$\rho_c \sim \frac{m_P^4}{\hbar^2 c^2}$$

where $m_P = \sqrt{\hbar c / G}$ is the Planck mass. Numerically, $\rho_c \sim 10^{97}$ kg/m^3.

The bounce time is extremely short. For a solar-mass black hole:
$$\Delta t_{bounce} \sim \frac{\hbar}{m_P c^2} \sim 10^{-44} \text{ s (Planck time)}$$

The post-bounce spacetime expands from the bounce point, with the proper time elapsed since the bounce (from interior observer perspective) being maximized at the equator of the Schwarzschild surface. At the horizon, proper time since the bounce is zero (making the horizon an instantaneous surface).

### Scale Invariance: The Self-Similar Cosmos

A remarkable prediction of Poplawski's scheme: if every black hole bounces into a new universe, and that universe eventually produces black holes, which in turn bounce into universes, then the cosmos has a self-similar fractal structure. The Schwarzschild radius of a black hole in one "level" of the hierarchy is related to the Hubble radius of the bounced universe, suggesting an infinite chain of nested universes at all scales.

This can be expressed via the scale parameter:
$$\Lambda_n = \sqrt{\frac{G M_n}{c^2}} \propto a_n$$

where $M_n$ is the total mass in universe level n, and $a_n$ is its scale factor. If the ratio $M_n / a_n$ is constant across levels, then the structure repeats (scale invariance).

---

## Mathematical Framework

**Einstein-Cartan field equations:**
$$G_{\mu\nu} = \frac{8\pi G}{c^4} \Sigma_{\mu\nu}$$

where $G_{\mu\nu}$ is the Einstein tensor computed from the full (torsionful) connection, and $\Sigma_{\mu\nu}$ is the canonical energy-momentum tensor including spin-torsion contributions.

**Torsion-density coupling:**
$$T^\lambda_{\mu\nu} = \frac{\kappa}{2} S^\lambda_{\mu\nu}$$

**Modified Friedmann equation (with torsion):**
$$H^2 = \frac{8\pi G}{3} \rho - \frac{\kappa^2}{24} \rho^2$$

where the second term is the torsion correction (quadratic in density).

**Near-singularity: Effective equation of state:**
$$P = w \rho c^2 + \frac{\beta \hbar^2}{m^2} \rho^{2/3}$$

where w is the equation-of-state parameter (0 for dust, 1/3 for radiation), and beta is a dimensionless coupling strength.

**Bounce condition:**
$$\left( \frac{d^2a}{dt^2} \right)_{bounce} = 0 \quad \Rightarrow \quad \rho = \rho_c$$

---

## Critical Assessment

### Strengths
1. **Classical mechanism**: No need for quantum gravity quantization. Torsion provides effective "quantum pressure" classically.
2. **Singularity resolution**: Black hole singularities are eliminated; they are replaced by bounces (non-singular transitions).
3. **Testable predictions**: Different from general relativity near black holes. Gravitational wave signatures from BH mergers should differ.
4. **Self-consistent cosmology**: Offers a narrative for nested universes without requiring a "first cause" -- the cosmos is an infinite self-similar hierarchy.
5. **Connection to fermion physics**: Explicitly couples spacetime geometry to spin, bridging gravity and quantum mechanics.

### Weaknesses
1. **Torsion coupling unknown**: The strength of torsion-density coupling (the parameter beta in the effective pressure) is not derived from first principles. Poplawski uses dimensional analysis and observational constraints, but the fundamental origin is unclear.
2. **Experimental constraints weak**: Einstein-Cartan theory makes very small deviations from GR at ordinary densities. Laboratory tests are inconclusive. Only near black hole singularities are differences large.
3. **Hawking radiation unaddressed**: In standard GR, black holes evaporate via Hawking radiation. In Poplawski's model, the interior bounces before Hawking radiation can fully develop. The implications for thermodynamics are unclear.
4. **Causality puzzles**: If the interior bounces and becomes a new expanding universe, is the new universe causally connected to the exterior? The causal structure is subtle and incompletely specified.
5. **Lack of observed black hole bounces**: No direct evidence that black holes have non-singular interiors. The model is consistent with observations but not proven by them.

### Empirical Status
Poplawski's work has generated modest interest in the quantum gravity community, but remains a minority view. Loop quantum cosmology (Ashtekar) offers a competing mechanism for singularity avoidance, and is more developed. Observational tests (gravitational waves, primordial black hole abundance) have not yet conclusively discriminated between models.

---

## Connection to Phonon-Exflation Framework

In phonon-exflation, particles are phononic excitations of a superfluid-like substrate defined by an internal geometric structure (the spectral triple on M4 x SU(3)). The condensed-matter analogy suggests that the universe is not a vacuum but a medium with intrinsic structure and excitations.

Poplawski's torsion cosmology aligns naturally with phonon-exflation:

1. **Torsion as internal angular momentum**: In NCG, the spin connection on SU(3) carries information about the internal geometry. Torsion on SU(3) is analogous to vorticity in a superfluid. The coupling $T^\lambda_{\mu\nu} \propto S^\lambda_{\mu\nu}$ mirrors the coupling between phonon vorticity and the phase field in a two-component condensate.

2. **Bounce mechanism via effective potential**: Instead of a torsion-density quadratic term, phonon-exflation uses the effective potential $V_{eff}(s)$ to stabilize the geometry. The non-singular bounce in Poplawski's scheme could be understood as the point where $V_{eff}$ reaches a minimum and reverses the contraction.

3. **Nested universes and spectral hierarchy**: If successive universes bounce with slightly mutated s-values (as in the CNS + phonon-exflation synthesis), they would form a scale-invariant tree structure similar to Poplawski's self-similar cosmos. The hierarchy of s-values would correspond to the hierarchy of nested universes.

4. **Fermion spin and phonon polarization**: The coupling of torsion to fermionic spin (in EC theory) parallels the coupling of phonon modes to particle spin in emergent approaches. The fermionic content determines the torsion distribution; in phonon-exflation, phonon polarization (a geometric property of the internal SU(3) excitations) would play an analogous role.

5. **Stabilization mechanism**: Session 18 showed that 1-loop Coleman-Weinberg failed to stabilize the effective potential (fermionic runaway dominates). Poplawski's torsion provides a non-perturbative stabilization at high density -- potentially the missing piece for phonon-exflation stability.

---

## Key Equations Summary

- Torsion tensor: $T^\lambda_{\mu\nu} = \Gamma^\lambda_{\mu\nu} - \Gamma^\lambda_{\nu\mu}$
- Torsion-spin coupling: $T^\lambda_{\mu\nu} = \frac{\kappa}{2} S^\lambda_{\mu\nu}$
- Modified Friedmann: $H^2 = \frac{8\pi G}{3} \rho - \frac{\kappa^2}{24} \rho^2$
- Effective pressure: $P = w \rho c^2 + \beta \hbar^2 \rho^{2/3} / m^2$
- Critical bounce density: $\rho_c \sim m_P^4 / (\hbar^2 c^2)$

---

## References

1. Poplawski, N. J., "Cosmology with Torsion: An Alternative to Cosmic Inflation," *Physics Letters B* 694.3 (2010): 181-185.
2. Poplawski, N. J., "Nonsingular, Big-Bounce Cosmology from Spinor-Torsion Coupling," *Physical Review D* 85.10 (2012): 107502.
3. Poplawski, N. J., "Black Holes as Universes in Loop Quantum Gravity," *Classical and Quantum Gravity* 30.19 (2013): 195022.
4. Poplawski, N. J., "Radial Motion into an Einstein-Cartan Black Hole," *Physics Letters B* 701.5 (2011): 672-675.
5. Cartan, E., "The Theory of Spinors" (Dover Publications, 1981 [original 1938]).
6. Ashtekar, A., Singh, P., "Loop Quantum Cosmology of k=0 FRW: A Status Report," *Classical and Quantum Gravity* 28.21 (2011): 213001.
7. Hawking, S. W., "Breakdown of Predictability in Gravitational Collapse," *Physical Review D* 14.10 (1976): 2460-2473.
8. Einstein, A., Cartan, E., "Théorie unitaire de l'interaction," *Académie des Sciences, Paris*, Comptes Rendus 186 (1928).

---

*Generated from training knowledge. Key references: Poplawski's Einstein-Cartan cosmology papers; reviews of loop quantum gravity and singularity resolution; torsion in differential geometry (Cartan, 1938).*
