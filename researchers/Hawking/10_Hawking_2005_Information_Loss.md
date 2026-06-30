# Information Loss in Black Holes

**Author(s):** S.W. Hawking
**Year:** 2005
**Journal:** Phys. Rev. D 72, 084013 (2005)
**arXiv:** hep-th/0507171
**Relevance:** HIGH

---

## Abstract

The question of whether information is lost in black holes is investigated using Euclidean path integrals. The formation and evaporation of black holes is regarded as a scattering problem with all measurements being made at infinity. This seems to be well formulated only in asymptotically AdS spacetimes. The path integral over metrics with trivial topology is unitary and information preserving. On the other hand, the path integral over metrics with non-trivial topologies leads to correlation functions that decay to zero. Thus at late times only the unitary information preserving path integrals over trivial topologies will contribute. Elementary quantum gravity interactions do not lose information or quantum coherence.

---

## Key Arguments and Derivations

### I. Introduction

The black hole information paradox started in 1967 when Werner Israel showed the Schwarzschild metric was the only static vacuum black hole solution. The no hair theorem (only stationary rotating solutions are Kerr-Newman) implied all information about the collapsing body was lost from the outside region apart from mass, angular momentum, and electric charge. This was not a problem classically (information preserved inside forever), but became one when Hawking discovered quantum radiation. In the approximation used, the radiation was completely thermal and carried no information. Hawking first raised the question in 1975; the argument continued until AdS-CFT was claimed to settle it in favor of conservation. Since the boundary CFT is manifestly unitary, string theory in AdS must be information preserving. But HOW information escapes remained unclear.

### II. Euclidean Quantum Gravity

Black hole formation and evaporation is treated as a scattering problem with all measurements at infinity. One never probes the strong field region, so one cannot be sure a black hole forms classically. The quantum state on a spacelike surface is a functional:

$$\Psi[h_{ij}, \phi, t] \quad (1)$$

where $h_{ij}$ is the 3-metric, $\phi$ the matter fields, $t$ the time at infinity. There is no gauge-invariant way to specify the time position of the surface in the interior, so one cannot give the initial wave function without already knowing the entire time evolution.

Joining the final surface back to the initial surface and integrating over all spatial geometries gives the partition function when the interval at infinity is Euclidean distance $\beta$:

$$Z(\beta) = \int \mathcal{D}g\,\mathcal{D}\phi\; e^{-I[g,\phi]} = \mathrm{Tr}(e^{-\beta H}) \quad (2)$$

There is an infrared problem for asymptotically flat space (infinite volume makes $Z$ infinite). Adding a small negative cosmological constant $\Lambda$ makes the effective volume of order $\Lambda^{-3/2}$, yielding anti-de Sitter space with finite thermal partition function. Hawking argues asymptotically AdS space is the only arena where particle scattering in quantum gravity is well formulated.

### III. The Path Integral

The boundary at infinity has topology $S^1 \times S^2$. The path integral sums over all topologies fitting inside this boundary:

- **Trivial topology**: $S^1 \times D^3$ (periodically identified AdS). Can be foliated by surfaces of constant time. Path integral treated canonically by time slicing. Each time step unitary, so the whole path integral is unitary. Equivalent to global conservation of information flowing through a 3-cycle under time translation.

- **Non-trivial topology**: $S^2 \times D^2$ (Schwarzschild-AdS black hole). Cannot be foliated by constant-time surfaces (no spatial 3-cycle modulo boundary). No conserved quantity to prevent correlation function decay. Explicit calculations confirm correlation functions decay to zero at late Lorentzian times as waves fall through the horizon.

The key insight: the trivial topology gives unitary evolution; the non-trivial topology gives information loss. But BOTH contribute to the path integral simultaneously.

### IV. Giant Black Holes

Following Maldacena, Hawking considers the canonical ensemble for AdS at temperature $\beta^{-1}$. For $\beta \ll \Lambda$ there are three classical solutions: periodically identified AdS, a small black hole, and a giant black hole. Giant black holes have very large negative action and dominate the canonical ensemble.

Two-point correlation functions $\langle O(x) O(y) \rangle$ in the CFT are given by boundary-to-boundary Green functions on the AdS side. In the dominant giant black hole solution, Green functions have standard form at small separation but decay exponentially as $y$ goes to late times (information falls through horizon). On the CFT side, this corresponds to screening.

However, the CFT is unitary, so information must be recoverable from many-point correlation functions. Maldacena realized that Green functions in periodically identified AdS do NOT decay and have the right order of magnitude for unitarity. Hawking goes further: the path integral over topologically trivial metrics IS unitary.

"So in the end everyone was right in a way. Information is lost in topologically non-trivial metrics like black holes. This corresponds to dissipation in which one loses sight of the exact state. On the other hand, information about the exact state is preserved in topologically trivial metrics."

The paradox arose because people thought classically in terms of a single topology. The Feynman sum over histories allows BOTH topologies simultaneously -- like the two-slit experiment. Observation at infinity determines only that there is a unitary mapping from initial to final states.

### V. Small Black Holes

Small black holes ($M \ll \Lambda^{-1/2}$) are unstable and behave like asymptotically flat black holes. One cannot set up a small black hole and watch it evaporate; one can only consider correlation functions of operators at infinity.

Hawking states he now realizes there is no Euclidean geometry representing formation and evaporation of a single black hole -- only eternal black holes and pair creation/annihilation. Formation and evaporation should be represented by a superposition of trivial metrics and eternal black holes.

The microcanonical partition function projects to energy $E_0$:

$$Z(E_0) = \int_{-i\infty}^{+i\infty} d\beta\, Z(\beta)\, e^{\beta E_0} \quad (3)$$

For $E_0 \ll \Lambda^{-1/2}$, most states are thermal radiation in AdS (confining box of volume $\Lambda^{-3/2}$). Thermal fluctuations occasionally cause gravitational collapse forming a small black hole, which evaporates back to thermal AdS. Correlation functions on the boundary again show apparent information loss in the black hole solution, but information is preserved by topologically trivial geometries.

### VI. Conclusions

Hawking argues quantum gravity is unitary and information is preserved. The path integral over topologically trivial metrics is unitary (by time-slicing). The path integral over non-trivial topologies loses information and becomes asymptotically independent of initial conditions. The total path integral is unitary.

How information escapes: Hartle-Hawking showed radiation can be thought of as tunnelling from inside the black hole. It can therefore carry information out while the spacetime remains topologically trivial. "There is no baby universe branching off, as I once thought. The information remains firmly in our universe."

Hawking notes a fundamental limitation: the only observables in quantum gravity are field values at infinity. Semi-classical approximation (large $N$ matter fields, neglecting gravitational fluctuations) already throws away unitarity. "One can not ask when the information gets out of a black hole because that would require the use of a semi-classical metric which has already lost the information."

Hawking concedes his 1997 bet with Thorne against Preskill: "I gave John an encyclopedia of baseball, but maybe I should just have given him the ashes."

## Key Results

1. The Euclidean path integral over topologically trivial metrics ($S^1 \times D^3$) is unitary and information-preserving, demonstrated by canonical time-slicing.
2. The path integral over non-trivial black hole topologies ($S^2 \times D^2$) leads to correlation functions that decay to zero at late times -- information IS lost in these sectors.
3. The total path integral (sum over all topologies) is unitary because at late times only the trivial topology contributes.
4. The resolution of the information paradox is that spacetime topology is not fixed -- the Feynman sum includes both black hole and no-black-hole topologies simultaneously (two-slit analogy).
5. No baby universe branching: information remains in our universe.
6. Semi-classical methods inherently lose unitarity; asking "when" information escapes requires a semi-classical metric that has already lost the information.
7. The framework is well-defined only in asymptotically AdS spacetimes (IR divergence in flat space).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Wave functional | $\Psi[h_{ij}, \phi, t]$ | Eq. (1) |
| Partition function | $Z(\beta) = \int \mathcal{D}g\,\mathcal{D}\phi\; e^{-I[g,\phi]} = \mathrm{Tr}(e^{-\beta H})$ | Eq. (2) |
| Microcanonical projection | $Z(E_0) = \int_{-i\infty}^{+i\infty} d\beta\, Z(\beta)\, e^{\beta E_0}$ | Eq. (3) |
| Trivial topology | $S^1 \times D^3$ | Periodically identified AdS |
| Non-trivial topology | $S^2 \times D^2$ | Schwarzschild-AdS |
| Boundary topology | $S^1 \times S^2$ | Asymptotic boundary |

## Relevance to Phonon-Exflation

Hawking's resolution -- information preserved because the Feynman sum includes topologically trivial metrics alongside black hole metrics -- parallels the framework's structural avoidance of the information paradox. The phonon-exflation framework has no horizon at all: the tau-transit is a Parker-type cosmological particle creation process, not a black hole process. There is no tracing over interior degrees of freedom, so pure states remain pure. The post-transit GGE is determined by unitary evolution from the pre-transit ground state with 8 conserved Richardson-Gaudin integrals. Hawking's key insight that "the only observables in quantum gravity are the values of the field at infinity" resonates with the framework's measurement philosophy: all observables are defined on the M4 base, never in the internal SU(3) fiber. The Euclidean path integral methodology used throughout this paper is the same formalism underlying the framework's instanton gas calculations ($S_{\text{inst}} = 0.069$).
