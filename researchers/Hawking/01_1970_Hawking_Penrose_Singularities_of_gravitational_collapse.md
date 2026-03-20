# The Singularities of Gravitational Collapse and Cosmology

**Authors**: Stephen W. Hawking, Roger Penrose
**Year**: 1970
**Journal**: *Proceedings of the Royal Society of London A*, **314**, 529--548

---

## Abstract (Analytical Summary)

Hawking and Penrose prove that spacetime singularities are a generic feature of general relativity under physically reasonable conditions. Building on Penrose's 1965 trapped surface theorem for gravitational collapse and Hawking's extensions to cosmological settings, the authors establish a unified singularity theorem that applies to both black holes and the Big Bang. The theorem demonstrates that geodesic incompleteness -- the existence of causal curves that cannot be extended to arbitrary affine parameter -- is inevitable whenever an energy condition, a causality condition, and a suitable trapping condition are satisfied. This result shattered the prevailing hope that singularities were artifacts of high symmetry (as in the Schwarzschild and Friedmann solutions) and established that classical general relativity necessarily predicts its own breakdown.

---

## Historical Context

### The Problem of Singularities Before 1965

The history of singularity theorems begins with the exact solutions. Schwarzschild's 1916 solution contains a singularity at $r = 0$, and Friedmann's 1922 cosmological solutions contain an initial singularity. For decades, the prevailing wisdom -- championed by the Soviet school led by Lifshitz, Khalatnikov, and Belinsky (BKL) -- held that these singularities were artifacts of perfect symmetry. The argument was intuitive: real physical systems lack exact spherical symmetry or exact spatial homogeneity, so perturbations should "bounce" the solution away from singular behavior. The Mixmaster universe (BKL, 1970) was partly motivated by this question.

### Penrose's 1965 Breakthrough

Roger Penrose transformed the discussion in 1965 by introducing two key innovations:

1. **Trapped surfaces**: A closed 2-surface $\mathcal{T}$ is *trapped* if both families of null geodesics orthogonal to it are converging. In flat space, the outgoing family always diverges; a trapped surface signals that gravity is so strong that even outward-directed light is being focused inward.

2. **Global causal methods**: Rather than analyzing specific solutions, Penrose used the topology of the causal structure of spacetime -- working with concepts like Cauchy surfaces, globally hyperbolic regions, and the domain of dependence.

Penrose's theorem showed that if a trapped surface exists, and if the null energy condition (NEC) holds, and if spacetime is globally hyperbolic, then spacetime is null geodesically incomplete. This was revolutionary: no symmetry assumptions whatsoever.

### Hawking's Cosmological Extensions (1966--1967)

Hawking recognized that Penrose's methods could be "time-reversed" to apply to cosmology. Where Penrose used a trapped surface (future-converging), Hawking used the expansion of the universe itself: if the Hubble expansion is everywhere below a certain rate, one can construct an *anti-trapped surface* (a past-converging surface), and the time-reverse of Penrose's argument yields a past singularity. Hawking published several variants (1966a, 1966b, 1967), each with slightly different assumptions, progressively weakening the conditions needed.

### The 1970 Synthesis

The 1970 paper represents the culmination: a single, clean theorem that subsumes all previous results as special cases. It is notable for its mathematical elegance, using a unified framework of causal geometry.

---

## Key Arguments and Derivations

### The Energy Conditions

The physical input to the theorem is an energy condition. The relevant ones are:

**Weak Energy Condition (WEC)**: For every timelike vector $t^a$,
$$T_{ab} \, t^a \, t^b \geq 0$$
This says that the energy density measured by any observer is non-negative.

**Strong Energy Condition (SEC)**: For every timelike vector $t^a$,
$$\left( T_{ab} - \frac{1}{2} g_{ab} T \right) t^a t^b \geq 0$$
Via Einstein's equations $R_{ab} = 8\pi G (T_{ab} - \frac{1}{2} g_{ab} T)$, this is equivalent to:
$$R_{ab} \, t^a \, t^b \geq 0$$
for all timelike $t^a$. This is the *timelike convergence condition*: gravity is always attractive (in the sense of focusing geodesic congruences).

**Null Energy Condition (NEC)**: For every null vector $k^a$,
$$T_{ab} \, k^a \, k^b \geq 0$$
or equivalently $R_{ab} \, k^a \, k^b \geq 0$. This is the weakest of the three and the one hardest to violate with classical matter.

### The Raychaudhuri Equation

The mathematical engine is Raychaudhuri's equation (1955), which governs the evolution of the expansion $\theta$ of a congruence of geodesics. For a timelike geodesic congruence with tangent $u^a$ ($u^a u_a = -1$):

$$\frac{d\theta}{d\tau} = -\frac{1}{3}\theta^2 - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} - R_{ab} u^a u^b$$

where $\sigma_{ab}$ is the shear tensor and $\omega_{ab}$ is the vorticity. For a null congruence with tangent $k^a$:

$$\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} - R_{ab} k^a k^b$$

The key observation: if the energy condition holds ($R_{ab} u^a u^b \geq 0$ or $R_{ab} k^a k^b \geq 0$) and the congruence is hypersurface-orthogonal ($\omega_{ab} = 0$), then:
$$\frac{d\theta}{d\tau} \leq -\frac{1}{3}\theta^2$$

This is a Riccati inequality. If $\theta = \theta_0 < 0$ at some initial point (the congruence is initially converging), then:
$$\theta(\tau) \leq \frac{3\theta_0}{3 + \theta_0 \tau}$$

The expansion $\theta \to -\infty$ within affine parameter $\tau \leq 3/|\theta_0|$. This means a *caustic* forms: neighboring geodesics cross. If spacetime were geodesically complete, this would lead to a topological contradiction under suitable global conditions.

### Trapped Surfaces and Their Role

A closed trapped surface $\mathcal{T}$ is a compact spacelike 2-surface such that the expansions $\theta_+$ and $\theta_-$ of both null normal congruences satisfy $\theta_+ < 0$ and $\theta_- < 0$ everywhere on $\mathcal{T}$.

The physical meaning: even the "outgoing" light rays are converging. In Schwarzschild spacetime, any 2-sphere at $r < 2M$ is trapped. The theorem guarantees that trapped surfaces form in any sufficiently concentrated gravitational collapse (Schoen and Yau later proved this rigorously).

### The Hawking--Penrose Theorem (Statement)

**Theorem**: A spacetime $(M, g_{ab})$ cannot be timelike and null geodesically complete if:

1. $R_{ab} K^a K^b \geq 0$ for every causal (timelike or null) vector $K^a$ (the generic energy condition);
2. The *generic condition* holds: every causal geodesic contains a point where $K_{[a} R_{b]cd[e} K_{f]} K^c K^d \neq 0$ (geodesics experience tidal forces somewhere);
3. There are no closed timelike curves (the chronology condition);
4. At least one of the following holds:
   - (a) There exists a compact achronal set without edge (a closed trapped surface or Cauchy surface);
   - (b) There exists a closed trapped surface;
   - (c) There exists a point $p$ such that the expansion of the future (or past) directed null geodesics from $p$ becomes negative along each geodesic.

Then $(M, g_{ab})$ contains at least one incomplete causal geodesic.

### Proof Strategy (Sketch)

The proof proceeds by contradiction. Assume geodesic completeness and derive a topological contradiction:

1. **Focusing**: By the energy condition and Raychaudhuri's equation, any initially converging congruence must develop conjugate points (caustics) within finite affine parameter.

2. **Achronal boundaries**: The edge of the future $J^+(S)$ of a set $S$ is generated by null geodesics. If $S$ is a trapped surface, these generators must leave $J^+(S)$ at conjugate points (by Step 1).

3. **Compactness argument**: If spacetime is geodesically complete, the edge of $J^+(S)$ would be both compact (because $S$ is compact and convergence forces the generators to terminate) and, by a topological argument, would need to extend indefinitely -- a contradiction.

The precise argument uses the notion of *maximum causal development* and properties of the *Cauchy horizon*. The contradiction arises between the compactness forced by focusing and the openness required by causality.

### The Generic Condition

Condition (2) deserves special comment. A geodesic satisfying the generic condition encounters nonzero tidal forces at at least one point. This rules out pathological spacetimes where all curvature vanishes along entire geodesics. It is satisfied generically (in the sense of Baire category) and is not a physically restrictive assumption. Its technical role is to ensure that the Raychaudhuri focusing actually produces conjugate points rather than asymptotically approaching them.

---

## Physical Interpretation

### What "Singularity" Means

Crucially, the theorem does NOT prove that curvature invariants blow up. It proves *geodesic incompleteness*: there exist causal curves (representing freely falling observers or light rays) that cannot be extended to arbitrary affine parameter. The observer's worldline simply *ends*. This is the mathematically precise definition of a singularity in general relativity.

The distinction matters: one can construct geodesically incomplete spacetimes where curvature remains bounded (e.g., by excising a point). However, in physically relevant cases (Schwarzschild, Kerr, FLRW), the geodesic incompleteness is accompanied by curvature divergence.

### Collapse Singularities vs. Cosmological Singularities

The theorem applies in two "directions":

- **Gravitational collapse**: A trapped surface forms during collapse of a massive star. The theorem guarantees a future singularity (the black hole singularity).
- **Cosmology**: If the universe is expanding and the SEC holds for matter content, then time-reversing the expansion gives a past-converging congruence, and the theorem guarantees a past singularity (the Big Bang).

### The Defeat of the BKL Conjecture (Partially)

The BKL claim that singularities are unstable was shown to be incorrect in the sense that geodesic incompleteness is *generic*. However, BKL were partially vindicated: the *nature* of the singularity (oscillatory/Mixmaster vs. monotone/Kasner) does depend on perturbations. The Hawking--Penrose theorem says singularities exist; it says nothing about their character.

---

## Impact and Legacy

### Immediate Impact

The theorem established singularity theory as a central pillar of general relativity. It earned Penrose the 2020 Nobel Prize in Physics ("for the discovery that black hole formation is a robust prediction of the general theory of relativity") and would have been a strong candidate for Hawking had he lived.

### The Call for Quantum Gravity

The most profound implication: classical general relativity predicts its own failure. At a singularity, the theory breaks down. This is universally interpreted as indicating that a quantum theory of gravity must replace classical GR at the Planck scale ($\ell_P = \sqrt{\hbar G / c^3} \approx 1.6 \times 10^{-35}$ m). The singularity theorems are thus the strongest motivation for quantum gravity research.

### Cosmic Censorship

The theorem says singularities exist but does not say whether they are visible. Penrose (1969) conjectured that singularities formed in gravitational collapse are always hidden behind event horizons (*weak cosmic censorship*). This remains one of the most important open problems in classical GR.

### Extensions

- Hawking and Ellis (1973, *The Large Scale Structure of Space-Time*) provide the definitive treatment.
- Borde, Guth, and Vilenkin (2003) extend to inflationary spacetimes.
- The theorem motivates the study of singularity resolution in loop quantum gravity and string theory.

---

## Connections to Modern Physics

1. **Penrose--Hawking theorems and black hole thermodynamics**: The singularity theorems provide the geometric foundation on which Hawking's subsequent area theorem and Bekenstein--Hawking entropy are built.

2. **Inflationary cosmology**: The SEC is violated during inflation ($\rho + 3p < 0$), so the singularity theorem does not directly apply. However, the Borde--Guth--Vilenkin theorem (2003) shows that past-geodesic incompleteness persists for inflationary spacetimes that are on average expanding, meaning inflation does not eliminate the initial singularity.

3. **Singularity resolution in quantum gravity**: Loop quantum cosmology replaces the Big Bang singularity with a "Big Bounce" via quantum corrections to the Raychaudhuri equation at Planck density. String theory approaches singularity resolution via brane collisions, T-duality, or fuzzball microstructure.

4. **Energy condition violations**: Quantum fields violate all pointwise energy conditions (Casimir effect, squeezed states). This motivates averaged energy conditions (ANEC), which are sufficient for weakened singularity theorems (Fewster and Galloway, 2011). The NEC violation by quantum effects is precisely what Hawking radiation exploits.

5. **For the phonon-exflation framework**: The singularity theorems are formulated in 4D. In Kaluza--Klein frameworks where the internal space evolves (compactification/exflation), the energy conditions in the full higher-dimensional spacetime may be satisfied while appearing violated in the 4D projection. The theorem would need to be applied to the full $M_4 \times K$ geometry.
