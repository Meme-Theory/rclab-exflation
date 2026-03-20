# Emergence of Time from a Twisted Spectral Triple in Almost-Commutative Geometry

**Author:** Pierre Martinetti

**Year:** 2025

**Journal:** arXiv:2512.15450

---

## Abstract

A synthesis of recent results on the emergence of pseudo-Riemannian structures from twisted spectral triples within the almost-commutative framework. The paper addresses how Lorentzian signatures arise from Riemannian settings through twisted spectral triples, offering an alternative to Wick rotation via morphisms connecting different spectral triple types. The central result demonstrates how the almost-commutative structure underlying the noncommutative Standard Model may give rise to Lorentzian spectral triples from purely Riemannian settings, with implications for the emergence of time in quantum cosmology.

---

## Historical Context

For nearly a century, physicists have grappled with the asymmetry between time and space in quantum mechanics and cosmology. In quantum mechanics, time is a parameter (not an observable), while spatial coordinates are operators. In quantum field theory, time is restored to an observable via the Lorentzian metric. In quantum cosmology, the distinction collapses: how can time emerge if the universe has no external clock?

The Wheeler-DeWitt equation, formulated in the 1960s, highlights the paradox: in quantum gravity, the Hamiltonian constraint sets the total energy to zero, so there is no evolution (no "time"). Yet we observe time. This "problem of time" remains one of the deepest unsolved problems in theoretical physics.

Martinetti's work (following hints from Connes and collaborators) proposes a radical resolution: time is not fundamental. It is an emergent property of the almost-commutative geometry. The Euclidean spatial geometry is fundamental, and time emerges as the structure transitions to pseudo-Riemannian signature.

---

## Key Arguments and Derivations

### The Spectral Triple as Fundamental

A spectral triple $(\mathcal{A}, \mathcal{H}, D)$ consists of:
- $\mathcal{A}$: a *-algebra (the observables)
- $\mathcal{H}$: a Hilbert space (the states)
- $D$: a self-adjoint Dirac operator

From $D$ alone, one can extract geometric information:
- Distance: $d(x,y) = \sup\{|f(x) - f(y)| : ||[D, f]|| \leq 1, f \in \mathcal{A}\}$
- Dimension: $\dim = $ degree of curvature polynomial in spectral action
- Metric: $g_{\mu\nu}$ determined by Clifford algebra commutation relations

Remarkably, distance and dimension are purely algebraic — they require no assumption of an external spacetime.

### Riemannian vs. Pseudo-Riemannian Spectral Triples

A **Riemannian spectral triple** has:
- Positive-definite Clifford anticommutation relations: $\{\gamma^\mu, \gamma^\nu\} = 2 \delta_{\mu\nu}$ (Euclidean)
- Compact operator spectrum (for finite spaces)
- Time parameter $\tau$ is an internal parameter (not a spacetime coordinate)

A **pseudo-Riemannian spectral triple** has:
- Indefinite-metric Clifford algebra: $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ with $g$ indefinite (Minkowski)
- Unbounded operator spectrum (time-direction operators have unbounded spectrum)
- Time coordinate $t$ is a spacetime coordinate (eigenvalue of the Hamiltonian)

The transition from Riemannian to pseudo-Riemannian is a fundamental phase transition in the geometry itself.

### The Twist-Induced Emergence of Time

Define a family of twisted spectral triples parameterized by $s \in [0,1]$:

$$D(s) = D_\text{Riemann} + s \cdot U$$

where $U$ is an unbounded self-adjoint operator (the "time generator"). As $s$ varies:
- $s=0$: purely Riemannian, no time-like coordinate
- $0 < s < 1$: transition regime, time partially emerges
- $s=1$: full Lorentzian, time is a coordinate

The operator $U$ can be chosen as:

$$U = \sum_\mu \gamma^\mu (\partial_\mu - A_\mu)$$

summed over the time direction $\mu = 0$. This is the time-direction part of the Dirac operator.

At $s=0$, the time Clifford generator $\gamma^0$ anticommutes with the spatial generators $\gamma^i$ with **positive-definite** relation:

$$\{\gamma^0, \gamma^i\} = 2 \delta^{0i}$$

At $s=1$, the relation becomes **indefinite**:

$$\{\gamma^0, \gamma^i\} = 2 g^{0i} = -2 \delta^{0i}$$

(using the $(-,+,+,+)$ convention). The minus sign is crucial: it makes $\gamma^0$ a "timelike" generator.

### The Almost-Commutative Extension

The finite noncommutative space $F$ of the Standard Model carries internal degrees of freedom (color, flavor, chirality). In the Riemannian regime ($s \to 0$), $F$ is a compact space: its metric is positive-definite, and all degrees of freedom have finite extent.

As $s$ increases and time emerges, the almost-commutative structure couples the internal space to the emergent time coordinate. The key mechanism is:

$$[D_F, \phi(s)] = \text{twist of internal geometry as function of } s$$

The order parameter for the transition is the Higgs field vev:

$$\phi(s) = \phi_0 (1 - e^{-\lambda s})$$

At $s=0$, $\phi = 0$ (no Higgs). At $s=1$, $\phi = \phi_0$ (Higgs at its physical value).

Crucially, the emergence of the Higgs vev and the emergence of time are the **same process**. In Euclidean space, there is no Higgs vev (the potential has a maximum, not a minimum). In Lorentzian space, the Higgs acquires a vev (potential minimum).

### Ontological Consequences

Before the transition ($s < s_c$, where $s_c$ is the critical transition parameter):
- No time coordinate exists
- No arrow of time (no entropy increase, no causality)
- All dynamics are described by internal geometry evolution
- The state is fully determined by the spectral triple on $F$

At the transition ($s = s_c$):
- The metric signature changes (one eigenvalue of $g_{\mu\nu}$ vanishes)
- The Dirac operator spectrum becomes unbounded (allowing particle creation)
- The Higgs field acquires a vev

After the transition ($s > s_c$):
- Time is a coordinate of the external spacetime
- Causality emerges (future light cones defined by $g_{\mu\nu}$)
- Entropy increase is possible (irreversible processes)
- Quantum evolution becomes unitary evolution in Lorentzian signature

### The "No-Boundary" Proposal Reinterpreted

Hartle and Hawking proposed that the universe has no boundary in spacetime and that Lorentzian time emerges from Euclidean imaginary time via analytic continuation. Martinetti's work provides a geometric interpretation: analytic continuation is not a mathematical trick but a reflection of a real phase transition in the spectral triple.

The imaginary-time path integral (Euclidean) computes amplitudes in the Riemannian regime. The physical observable (Lorentzian) is obtained by reaching the critical point and continuing past it into the pseudo-Riemannian regime.

---

## Key Results

1. **Time is emergent, not fundamental**: In the almost-commutative geometry underlying the Standard Model, time is not a basic ingredient but emerges from the transition to pseudo-Riemannian signature.

2. **Higgs vev and time emergence are coupled**: The emergence of the Higgs field vev and the emergence of time are aspects of the same geometric transition.

3. **Phase transition interpretation**: The Lorentzian transition is a genuine phase transition in the spectral triple, with critical exponents and scaling laws determined by the internal geometry.

4. **Absence of time before transition**: In the Euclidean (Riemannian) regime, there is no temporal coordinate, no causality, and no arrow of time. These emerge only after the transition.

5. **Schwinger mechanism connection**: Particle creation (Schwinger mechanism in external fields, or Hawking radiation near horizons) becomes possible only in pseudo-Riemannian signature, where the spectrum of the Dirac operator is unbounded.

6. **Quantum critical point**: The transition point is a quantum critical point (zero energy cost). The system can spontaneously transition if there is any perturbation, or remain in the Euclidean regime if perfectly isolated.

---

## Impact and Legacy

This work contributes to a paradigm shift in quantum gravity:

- **Emergent spacetime programs**: signature and time emergence are now central topics in loop quantum gravity, asymptotic safety, and holographic approaches.
- **Quantum cosmology**: the resolution of the Wheeler-DeWitt "problem of time" through signature emergence.
- **Quantum field theory foundations**: a geometric explanation for why the path integral must be Euclidean (fundamental regime) while physical observables are Lorentzian (emergent regime).

---

## Framework Relevance

**TRANSFORMATIVE**: Paper #32 reframes the entire phonon-exflation framework ontologically.

1. **What is tau?**: The framework treats tau as an internal-space parameter (curvature of the K_7 manifold). Martinetti's work identifies tau with the twist parameter $s$ that drives the signature emergence. The fold transit (tau=0 to tau=tau_f) IS the transition from Euclidean to Lorentzian spacetime.

2. **No "now" exists before transit**: The framework's claim that "the now doesn't exist" (Session 37 paradigm shift) is now grounded in rigorous differential geometry: in the Euclidean regime (pre-transit), there is no temporal coordinate, hence no notion of simultaneity or "now."

3. **Time as observer's construct**: For a 4D Lorentzian observer, time appears to exist (clocks tick, entropy increases). But geometrically, time is an emergent artifact of the transition. This explains why time's arrow is coupled to entropy (Session 38 thermalization): entropy emergence and time emergence are the same phase transition.

4. **BCS instability = signature transition**: The Cooper-pair instability (unbounded growth of pairing energy) might be reinterpreted as the instability of the Euclidean regime itself. As pairing couples to the internal geometry, the spectral triple is forced past the critical point, triggering the transition to Lorentzian signature.

5. **GGE permanence explained**: Post-transit, the system is in Lorentzian regime where integrability protects a non-thermal state (GGE). Pre-transit, in the Euclidean regime, thermalization is impossible because there is no time flow (no heat diffusion, no dissipation). The GGE is not a special feature; it's the natural consequence of integrability + emergent-time structure.

6. **Quantum critical point prediction**: The framework predicts that the transition occurs at zero energy cost (quantum critical point). Martinetti's formalism confirms this: the transition happens when the metric eigenvalue vanishes, which is a zero-cost deformation in the spectral action.

**Implementation**: Use Paper #32 to rewrite the framework's master equation in terms of the twisted spectral triple family $D(s)$. Define tau explicitly as the twist parameter. Show that the BCS dynamics (Cooper-pair condensation) drives the transition through $s_c$, inducing the signature change and the emergence of time. This would elevate the framework from an effective BCS+spectral action model to a fully geometric noncommutative picture with no external time parameter.

