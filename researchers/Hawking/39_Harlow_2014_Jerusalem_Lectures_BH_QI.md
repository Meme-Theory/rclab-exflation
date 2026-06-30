# Jerusalem Lectures on Black Holes and Quantum Information

**Author(s):** Daniel Harlow
**Year:** 2014 (revised 2022)
**Journal:** JHEP (lecture notes from 31st Winter School, Hebrew University)
**arXiv:** 1409.1231
**Relevance:** HIGH

---

## Abstract

In these lectures I give an introduction to the quantum physics of black holes, including recent developments based on quantum information theory such as the firewall paradox and its various cousins. I also give an introduction to holography and the AdS/CFT correspondence, focusing on those aspects which are relevant for the black hole information problem.

---

## Key Arguments and Derivations

### Section 2: Classical Black Holes
**2.1 - Schwarzschild geometry**: Reviews the metric ds^2 = (1 - 2GM/r) dt^2 + (1 - 2GM/r)^{-1} dr^2 + r^2 d Omega^2. Identifies the singularity at r = 0 (R^{abcd} R_{abcd} diverges) and the coordinate artifact at r_s = 2GM. Notes the sign flip of dt^2 and dr^2 coefficients inside the horizon, making r timelike. Discusses gravitational redshift near the horizon.

**2.2 - Kruskal extension**: Defines tortoise coordinate r* = r + log(r-1), then Kruskal-Szekeres coordinates U = -e^{-(r*-t)/2}, V = e^{(r*+t)/2}. The metric becomes ds^2 = (2/r) e^{-r} (-dU dV + dV dU) + r^2 d Omega^2, manifestly regular at the horizon. The full geometry is a non-traversable wormhole connecting two asymptotically flat universes.

**2.3 - Penrose diagrams**: Conformal compactification technique. Uses arctan to map infinity to finite distance. Diagrams for Minkowski space, de Sitter space (has horizons, no spatial infinity i^0, problematic for quantum gravity), and Schwarzschild (two asymptotic boundaries, singularities at top and bottom).

**2.4 - Real black holes**: Black hole formation from collapsing matter (stars or photon shells). Notes that the horizon extends into the purely Minkowski region --- one could currently be passing through the horizon of a yet-to-form black hole.

### Section 3: Entanglement in Quantum Field Theory
**3.1 - QFT basics**: Hilbert space as infinite tensor product over spatial points. Free scalar Hamiltonian H = (1/2) integral (pi^2 + |grad phi|^2 + m^2 phi^2).

**3.2 - Entanglement in the vacuum**: The vacuum state of a QFT is highly entangled across any spatial partition. For a free scalar, the entanglement entropy across a planar cut scales as S ~ (A / epsilon^2), where A is the area and epsilon is the UV cutoff (area law). This is connected to the Bekenstein-Hawking entropy.

**3.3 - Rindler decomposition**: The Minkowski vacuum, restricted to a Rindler wedge, looks thermal at the Unruh temperature T = a/2pi. The entanglement between the two Rindler wedges is essential for the smoothness of the horizon.

**3.4 - Free fields in Rindler space**: Detailed mode decomposition. Rindler Hamiltonian H_R = integral omega a^dagger_omega a_omega d omega. The thermal nature follows from the entangled structure of the vacuum.

**3.5 - Entanglement is important for horizon crossing (introduction to firewalls)**: If the entanglement between the two sides of a horizon is disrupted, a freely falling observer would encounter high-energy excitations --- a "firewall."

### Section 4: QFT in a Black Hole Background
**4.1 - Two-sided Schwarzschild and Rindler decomposition**: Near the horizon, Schwarzschild looks like Rindler space. The Hartle-Hawking state is the analog of the Minkowski vacuum.

**4.2 - Schwarzschild modes**: Decomposes the field into modes using the tortoise coordinate. The effective potential for radial modes has a peak near r = 3GM.

**4.3 - Hawking's calculation of black hole radiation** (reproduces Hawking 1975):
- The key insight: modes that are positive frequency with respect to the Kruskal time U near the past horizon become a mixture of positive and negative frequency modes with respect to the Schwarzschild time t at late times
- The Bogoliubov transformation gives a thermal spectrum at temperature T_H = 1/(8 pi GM) (kappa = 1/4GM for Schwarzschild)
- The calculation is equivalent to the statement that the Unruh vacuum state has outgoing thermal radiation at I^+

**4.4 - Evaporation**: The black hole loses mass as it radiates. Stefan-Boltzmann law gives dM/dt ~ -1/M^2, so the evaporation time is t_evap ~ M^3 (in Planck units). For a solar mass black hole, t_evap ~ 10^{67} years. The temperature increases as the black hole shrinks, leading to a runaway.

**4.5 - Entropy and thermodynamics**: Bekenstein-Hawking entropy S = A/4G. For a solar mass black hole, S ~ 10^{77}. This is vastly larger than the entropy of the star that formed it (S_star ~ 10^{58}), consistent with the second law.

**4.6 - The information problem** (reproduces Hawking 1976):
- In the semiclassical calculation, the outgoing Hawking radiation is exactly thermal and carries no information about the infalling matter
- After complete evaporation, a pure state has evolved into a mixed state, violating unitarity
- This is the black hole information paradox
- Three logical possibilities: (1) information is destroyed, (2) information escapes during evaporation, (3) information is stored in a remnant
- Current consensus (post-AdS/CFT): information must escape, but the mechanism is unknown

**4.7 - Brick wall model and stretched horizon**: 't Hooft's model places a reflecting boundary just outside the horizon. Reproduces S = A/4G with a suitable UV cutoff, suggesting black hole entropy is entanglement entropy. The "stretched horizon" is a membrane at Planck distance from the true horizon.

**4.8 - Euclidean black hole**: Wick-rotating t -> -i tau gives a smooth geometry if tau has period beta = 1/T_H = 8 pi GM. This provides an independent derivation of the Hawking temperature and connects to the partition function Z = Tr(e^{-beta H}).

### Section 5: Unitary Evaporation
**5.1 - S-matrix**: If evaporation is unitary, there must be an S-matrix mapping pure in-states to pure out-states.

**5.2 - Page curve**: The entanglement entropy of the radiation should follow the Page curve: initially increasing (as radiation is emitted), reaching a maximum at the "Page time" (when roughly half the entropy has been emitted), then decreasing back to zero. The Page time is t_Page ~ M^3/2 (half the evaporation time by entropy, much earlier than by mass).

**5.3 - Page's theorem**: For a random bipartite state in H_A tensor H_B with |A| << |B|, the reduced density matrix on A is nearly maximally mixed. This implies that early radiation looks thermal even if the total evolution is unitary.

**5.4 - How hard is it to test unitarity?**: The Harlow-Hayden argument: to verify non-unitarity of evaporation, one would need to perform a quantum computation on the early radiation that takes exponential time (longer than the evaporation time). This suggests the information paradox may be computationally inaccessible.

**5.5 - Typical microstates**: Discussion of what a "typical" black hole microstate looks like from the outside.

**5.6 - Scrambling and recovery**: Black holes are fast scramblers --- information dropped in is scrambled across all degrees of freedom in time t_scramble ~ M log M. Connection to Hayden-Preskill protocol.

**5.7 - Black hole complementarity**: Susskind's proposal that information is both reflected at the horizon (from the outside observer's perspective) and passes through (from the infalling observer's perspective). No single observer sees a contradiction.

### Section 6: Holography and AdS/CFT
**6.1 - Entropy bounds and holographic principle**: The Bekenstein bound S <= 2pi E R and the covariant entropy bound. Maximum entropy in a region scales with the boundary area, not the volume.

**6.2 - Statement of AdS/CFT**: The correspondence between string theory in AdS_{d+1} and a CFT_d on the boundary. The boundary theory is a complete, non-perturbative definition of quantum gravity in the bulk.

**6.3-6.9**: Perturbations, one-sided black holes, Hawking-Page transition, two-sided wormholes (ER = EPR), information problem in AdS/CFT. Demonstrates that unitarity is manifest in the boundary CFT.

**6.10 - Von Neumann entropy and Ryu-Takayanagi formula**: S(A) = Area(gamma_A) / 4G, where gamma_A is the minimal surface in the bulk homologous to boundary region A. This is the holographic entanglement entropy.

### Section 7: Paradoxes for the Infalling Observer
**7.1 - Entanglement monogamy problem** (AMPS firewall argument):
- Late Hawking radiation B must be entangled with early radiation R (for unitarity, Page curve)
- But B must also be entangled with the interior mode A (for smooth horizon)
- Monogamy of entanglement: B cannot be maximally entangled with both R and A
- Something must give: either unitarity, or the smooth horizon, or the equivalence principle
- AMPS conclude: a firewall (high-energy excitation) exists at the horizon of old black holes

**7.2 - Firewall typicality**: The argument extends to typical black hole microstates, not just old black holes.

**7.3 - Creation operator problem**: Constructing an operator that creates the interior mode from the CFT is state-dependent, which is problematic.

**7.4 - Marolf-Wall paradox**: Even for eternal (non-evaporating) black holes in AdS, reconstructing the interior is problematic.

### Section 8: Proposals for the Interior
- **Complementarity from computational complexity?** (Harlow-Hayden): The computation needed to verify the paradox takes exponential time, possibly allowing complementarity to survive
- **Nonlinearity?** (Papadodimas-Raju): State-dependent operators for the interior, at the cost of linearity
- **Postselection?** (Horowitz-Maldacena): Final state projection at the singularity
- **Firewalls?** (AMPS): Accept that the horizon is not smooth for old black holes

---

## Key Results

1. **Black hole information problem**: Pure states evolving to mixed states via Hawking evaporation violates unitarity. This is the central unsolved problem.

2. **Page curve**: The entanglement entropy of radiation must follow S_rad(t) = min(S_rad^{thermal}(t), S_BH(t)) if evaporation is unitary.

3. **Page time**: t_Page ~ M^3/2 in Planck units, when information starts to come out.

4. **Scrambling time**: t_scr ~ M log M (fast scrambler). Black holes scramble information in the shortest time allowed by quantum mechanics for a system with S ~ M^2 degrees of freedom.

5. **AMPS firewall paradox**: Entanglement monogamy forces a choice between unitarity, the equivalence principle, and low-energy effective field theory near the horizon.

6. **Harlow-Hayden computational complexity**: Verifying the paradox requires exponential quantum computation time, potentially rendering it operationally inaccessible.

7. **Ryu-Takayanagi formula**: S(A) = Area(gamma_A) / 4G provides the holographic dual of entanglement entropy.

8. **ER = EPR**: The two-sided eternal black hole in AdS corresponds to two entangled but non-interacting CFTs (Maldacena). The wormhole (Einstein-Rosen bridge) is dual to entanglement (Einstein-Podolsky-Rosen).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Schwarzschild metric | $ds^2 = (1 - 2GM/r) dt^2 + (1 - 2GM/r)^{-1} dr^2 + r^2 d\Omega^2$ | Eq. 2.1 |
| Kruskal relation | $UV = -(1-r)e^r$ | Eq. 2.7 |
| Area law for entanglement | $S \sim A / \epsilon^2$ | Sec. 3.2 |
| Hawking temperature | $T_H = 1 / (8\pi GM)$ | Sec. 4.3 |
| Evaporation time | $t_{\rm evap} \sim M^3$ (Planck units) | Sec. 4.4 |
| Bekenstein-Hawking entropy | $S_{\rm BH} = A / 4G$ | Sec. 4.5 |
| Euclidean periodicity | $\beta = 1/T_H = 8\pi GM$ | Sec. 4.8 |
| Page curve | $S_{\rm rad}(t) = \min(S_{\rm rad}^{\rm thermal}(t),\, S_{\rm BH}(t))$ | Sec. 5.2 |
| Scrambling time | $t_{\rm scr} \sim M \log M$ | Sec. 5.6 |
| Ryu-Takayanagi | $S(A) = {\rm Area}(\gamma_A) / 4G$ | Sec. 6.10 |
| Page's theorem (approx.) | $S(\rho_A) \approx \log |A| - |A| / (2|B|)$ for $|A| \ll |B|$ | Sec. 5.3 |

## Relevance to Phonon-Exflation

Harlow's comprehensive treatment of the information problem is relevant to the phonon-exflation framework in several ways. The framework's KK geometry has no horizon --- there is no event horizon in the M4 x SU(3) geometry during or after transit. This means the framework completely evades the AMPS firewall paradox (Section 7) and the information problem (Section 4.6): there is no information loss because there is no horizon to hide behind. The entanglement structure of the Rindler decomposition (Section 3.3) parallels the entanglement between the KK fiber and the 4D base that produces the GGE relic state. The Page curve formalism is relevant as a diagnostic for whether the framework's particle creation process preserves unitarity (it does, by construction, since the transit is a unitary evolution of a pure state followed by tracing over the fiber). The Ryu-Takayanagi formula connects to the spectral action = entropy identification pursued in earlier sessions.
