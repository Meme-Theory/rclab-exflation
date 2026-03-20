# Eternal Black Holes in Anti-de Sitter Space

**Author(s):** Juan M. Maldacena
**Year:** 2001
**Journal:** Journal of High Energy Physics, Volume 0304, page 013
**arXiv:** hep-th/0106112

---

## Abstract

Maldacena provides a detailed AdS/CFT description of eternal black holes—maximally extended Schwarzschild-AdS geometries with both interior and exterior regions. He proposes that the dual CFT description involves two copies of the conformal field theory, with the black hole degrees of freedom encoded in the entanglement structure of an initial quantum state. This framework addresses the black hole information paradox, suggesting that information apparently lost into the black hole interior is preserved in the boundary CFT state, laying the conceptual groundwork for later ideas like ER=EPR.

---

## Historical Context

By 2001, the information paradox posed by Hawking's 1974 discovery of black hole evaporation remained unresolved. If black holes evaporate completely, they destroy information, violating quantum mechanics. The AdS/CFT correspondence suggested a solution: information is not lost but encoded in subtle correlations of the CFT.

Maldacena's 2001 paper made this concrete. He considered the simplest black hole in AdS—the eternal black hole or "Schwarzschild-AdS black hole." Unlike black holes that form from collapse, an eternal black hole has always existed, with both a past and future horizon. The topology of the spacetime is non-trivial: it is not simply connected to the AdS boundary.

Maldacena's key insight was that two separate CFT copies, prepared in an entangled state, could describe a single spacetime with a "wormhole" (Einstein-Rosen bridge) interior. This proposal—that spatial connectivity emerges from quantum entanglement—became the seed of the later ER=EPR conjecture (2013), which proposes that every entangled pair of objects is connected by a microscopic wormhole.

---

## Key Arguments and Derivations

### The Eternal Black Hole Geometry

An eternal black hole in AdS5 has the metric:

$$ds^2 = -f(r) dt^2 + \frac{dr^2}{f(r)} + r^2 d\Omega_3^2$$

where

$$f(r) = \frac{r^2}{L^2} + 1 - \frac{2 M L^2}{r^2}$$

and $L$ is the AdS radius. The metric has two horizons:

- **Event horizon:** At $r = r_+$ where $f(r_+) = 0$, with $r_+$ larger
- **Cauchy horizon:** At $r = r_-$ where $f(r_-) = 0$, with $r_- < r_+$

Between the two horizons lies the black hole interior. The spacetime is maximally extended, meaning that freely-falling observers can traverse both the event horizon and the Cauchy horizon.

The Hawking temperature is:

$$T_H = \frac{\kappa}{2\pi} = \frac{r_+ - r_-}{2\pi r_+^2}$$

In the limit of a large black hole ($r_+ \gg L$), the temperature is very low.

### Dual CFT Description: Two Copies and Entanglement

The AdS/CFT duality states that Type IIB strings on AdS5 x S5 are dual to N=4 super-Yang-Mills in four dimensions. For a black hole in the bulk, Maldacena proposes an unconventional boundary interpretation:

The dual CFT description requires **two copies** of the four-dimensional CFT, labeled "left" (L) and "right" (R), living on two separate boundaries. These two copies are not physically independent but are in an entangled quantum state:

$$|\Psi\rangle = \sum_n e^{-\beta E_n / 2} |\psi_n\rangle_L \otimes |\psi_n\rangle_R$$

where $\beta = 1 / T_H$ is the inverse temperature and $|\psi_n\rangle_L$, $|\psi_n\rangle_R$ are energy eigenstates of the left and right CFTs.

This state is the **thermofield double (TFD)** state, which encodes maximum entanglement between the two copies at a given temperature.

### Topological Non-Triviality and the Einstein-Rosen Bridge

The eternal black hole spacetime is topologically non-trivial. The spatial slices (at constant time $t$) are not simply connected: the region between the two horizons (the "interior") is disconnected from the asymptotic AdS region.

Maldacena's insight: this non-trivial topology is dual to the entanglement between the two CFT copies. The Einstein-Rosen bridge (the wormhole connecting the two asymptotic regions through the interior) is encoded in the entanglement structure $|\Psi\rangle$.

Operationally, an operator in the left CFT near the boundary corresponds to a field in the left asymptotic region of AdS. An operator in the right CFT corresponds to a field in the right asymptotic region. The entanglement between L and R CFT states means that operations in L and R are correlated, and this correlation is dual to the geometric connection (the Einstein-Rosen bridge) in the bulk.

### Information and Correlations

A fundamental question: where is the information about the black hole interior in the dual CFT?

Maldacena argues that information about the interior is not stored in any single operator's expectation value but in the **correlations** between left and right CFT operators. Specifically:

$$\langle O_L(t_L, \vec{x}_L) O_R(t_R, \vec{x}_R) \rangle_{\Psi} \neq \langle O_L(t_L, \vec{x}_L) \rangle_{\text{L}} \langle O_R(t_R, \vec{x}_R) \rangle_{\text{R}}$$

The deviation of the product of individual expectation values from the joint expectation value—a measure of entanglement—encodes the wormhole geometry.

### Connection to Thermodynamics

The eternal black hole at temperature $T_H$ is in thermodynamic equilibrium. The entropy of the system is given by the Bekenstein-Hawking formula:

$$S_{BH} = \frac{A}{4 G_N} = \frac{\pi r_+^2}{G_N}$$

On the CFT side, the thermofield double state has an entanglement entropy equal to the thermal entropy of a single CFT at temperature $T_H$:

$$S_{ent} = \int_0^\infty d\omega \, \omega \left( \frac{e^{\beta \omega} + 1}{e^{\beta \omega} - 1} \right) \nu(\omega)$$

where $\nu(\omega)$ is the density of states. For a large CFT with central charge $c$, this reproduces the black hole entropy.

### Hawking Radiation and Information Flow

In the standard Hawking evaporation picture, a black hole emits radiation and shrinks, eventually disappearing. In the dual CFT picture, this is reinterpreted:

The radiation is emitted by one of the CFT copies (say, the right). As the black hole radiates, $T_H$ decreases (the black hole cools), but the CFT state remains entangled with the other copy. Information about the initial state is progressively transferred from the interior (which is inaccessible to asymptotic observers) to the radiation (which can be collected at infinity).

By the end, the information is not lost but is encoded in the radiation and the final CFT state. This resolves the information paradox: information is conserved, and the black hole does not destroy quantum information.

---

## Key Results

1. **Eternal Black Holes Have Dual CFT Description:** A black hole in AdS is dual to two entangled CFT copies in a thermofield double state.

2. **Wormhole-Entanglement Duality:** The Einstein-Rosen bridge connecting the two asymptotic regions is the gravitational dual of entanglement between the two CFTs.

3. **Information Preservation:** Information about the black hole is not lost but encoded in CFT correlations. The information paradox is resolved.

4. **Topological Implications:** Non-trivial spacetime topology (like Einstein-Rosen bridges) corresponds to entanglement in the dual quantum state.

5. **Black Hole Thermodynamics from CFT:** The Bekenstein-Hawking entropy is reproduced as the thermal entropy of the dual CFT.

6. **Foundation for ER=EPR:** The paper establishes that spacetime connectivity is dual to entanglement, laying the groundwork for the later conjecture that all entangled pairs are connected by ER bridges.

---

## Impact and Legacy

Maldacena's 2001 paper had three major impacts:

**1. Information Paradox Resolution:** It provided a concrete mechanism (through CFT correlations) for how black hole information is preserved, addressing a 27-year-old puzzle.

**2. Holographic Principle Deepened:** The paper showed that even complex topological features of spacetime (like wormholes) have precise duals in the boundary theory. This suggested that spacetime is not fundamental but emergent.

**3. ER=EPR Conjecture:** Maldacena and Susskind's 2013 "Cool Horizons for Entangled Black Holes" (based on this 2001 work) proposed that every entangled pair is connected by a microscopic ER bridge. This has become a major avenue of research in quantum gravity.

The paper has over 3,000 citations by 2025 and remains central to discussions of black hole physics and quantum information in string theory.

---

## Connection to Phonon-Exflation Framework

**Conceptual resonance on emergence.** Maldacena's work shows that spacetime geometry (specifically, the wormhole) is emergent from quantum entanglement. The phonon-exflation framework similarly proposes emergence: particles are emergent as phonons from internal geometric structures (spectral triples on SU(3)).

**Parallels:**
- Both show that "fundamental" vs. "emergent" is relative
- Both use topological/geometric structures to encode physical information
- Both employ entanglement/correlation structures to explain observed physics

**Differences:**
- Maldacena's emergence is from lower-dimensional boundary theory to higher-dimensional bulk gravity
- Phonon-exflation's emergence is from geometric/spectral structure to particle fields
- Maldacena's framework is within string theory; phonon-exflation uses noncommutative geometry

**Potential bridge:** Could phonon-exflation admit an AdS/CFT-like dual where a 4D CFT on the SU(3) boundary is dual to some higher-dimensional gravity? This remains speculative.

---

## Critical Assessment

**Strengths:**
- Provides a concrete resolution to the black hole information paradox
- Reveals deep connection between entanglement and spacetime geometry
- Predictions (black hole entropy from CFT) verified numerically
- Opens new avenues for understanding quantum gravity

**Limitations:**
- The proposal relies on AdS/CFT, which applies only to AdS spaces, not our universe (which is approximately de Sitter)
- The two-copy CFT description is non-standard and lacks clear physical interpretation
- The mechanism for information recovery from Hawking radiation is not explicitly shown; the information is preserved "in principle" but its extraction is complex
- Depends on maximally entangled initial state (thermofield double); it is unclear what selects this state in a physical black hole

**Modern perspective:** The paper is foundational for understanding black holes in AdS/CFT. The ideas have been generalized (multiple boundaries, finite temperature, non-AdS spaces), but the core framework remains the same. The exact relationship to real astrophysical black holes remains uncertain.
