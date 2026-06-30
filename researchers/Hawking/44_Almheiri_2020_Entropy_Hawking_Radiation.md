# The Entropy of Hawking Radiation

**Author(s):** Ahmed Almheiri, Thomas Hartman, Juan Maldacena, Edgar Shaghoulian, Amirhossein Tajdini
**Year:** 2020
**Journal:** Rev. Mod. Phys. 93, 035002 (2021)
**arXiv:** 2006.06872
**Relevance:** CRITICAL

---

## Abstract

In this review, we describe recent progress on the black hole information problem that involves a new understanding of how to calculate the entropy of Hawking radiation. We show how the method for computing gravitational fine-grained entropy, developed over the past 15 years, can be extended to capture the entropy of Hawking radiation. This technique reveals large corrections needed for the entropy to be consistent with unitary black hole evaporation.

---

## Key Arguments and Derivations

### 2. Preliminaries

**2.1 Black Hole Thermodynamics.** The first law of black hole mechanics:

$$\frac{\kappa}{8G_N} d(\text{Area}) = dM - \Omega \, dJ$$

With $T = \hbar\kappa/2\pi$ (Hawking temperature), this becomes the first law $T \, dS_{BH} = dM - \Omega \, dJ$. The generalized entropy:

$$S_{\text{gen}} = \frac{\text{Area of horizon}}{4\hbar G_N} + S_{\text{outside}}$$

obeys the generalized second law $\delta S_{\text{gen}} \geq 0$.

**2.2 Hawking Radiation.** The Schwarzschild metric near the horizon ($r \to r_s$) reduces to flat Minkowski space in Rindler coordinates:

$$ds^2 \approx -\rho^2 d\tau^2 + d\rho^2$$

The Wick rotation $\tau = i\tau_E$ gives Euclidean polar coordinates with periodicity $2\pi$, identifying the temperature via the Tolman relation:

$$T_{\text{proper}} = \frac{a}{2\pi}$$

for a uniformly accelerated observer (Unruh effect). The Hawking temperature measured at infinity:

$$T = \frac{1}{4\pi r_s} = \frac{\hbar c^3}{8\pi G_N M k_B}$$

**2.3 The Euclidean Black Hole.** The Euclidean Schwarzschild geometry (the "cigar") requires periodicity $\beta = 4\pi r_s$ to avoid a conical singularity at the tip. The partition function:

$$Z(\beta) = \text{Path integral on Euclidean BH} \approx e^{-I_{\text{classical}}} Z_{\text{quantum}}$$

The entropy is obtained from $S = (1 - \beta\partial_\beta)\log Z(\beta)$.

**2.4 Evaporating Black Holes.** Hawking radiation carries energy to infinity, reducing the black hole mass. The process can be interpreted as pair creation near the horizon: one particle escapes, the other falls in. The two are entangled, making the outgoing radiation thermal (mixed state).

### 3. The Central Dogma

The authors define the "central dogma": as seen from the outside, a black hole can be described by a quantum system with $\text{Area}/(4G_N)$ degrees of freedom, evolving unitarily. This is supported by:
- Strominger-Vafa entropy counting for extremal black holes in string theory.
- The AdS/CFT correspondence, where the black hole + exterior maps to boundary degrees of freedom.

The central dogma is in tension with a naive reading of the spacetime geometry, which has two "asymptotic" regions (exterior and interior near the singularity).

### 4. Fine-Grained vs Coarse-Grained Entropy

**Von Neumann entropy** (fine-grained): $S_{\text{vN}} = -\text{Tr}[\rho \log \rho]$. Invariant under unitary evolution.

**Coarse-grained entropy** (thermodynamic): Maximize $S(\tilde{\rho})$ over all $\tilde{\rho}$ matching the coarse-grained observables. Obeys the second law. The generalized entropy (2.4) is the coarse-grained entropy of the black hole.

The semiclassical entropy $S_{\text{semi-cl}}(\Sigma)$ is the von Neumann entropy of quantum fields on a spatial region $\Sigma$ in the semiclassical geometry.

### 5. The Hawking Information Paradox

The paradox: the vacuum state split by the horizon produces entangled pairs. The fine-grained entropy of Hawking radiation grows linearly, eventually exceeding the Bekenstein-Hawking entropy $S_{BH} = \text{Area}/(4G_N)$, which bounds the black hole's degrees of freedom. If unitary, the entropy must follow the **Page curve**: rising until the Page time $t_{\text{Page}}$ (when $S_{\text{rad}} = S_{BH}$), then decreasing.

The paradox is robust: small corrections to the Hawking process cannot resolve it. Resolution must be non-perturbative in $G_N$.

### 6. Fine-Grained Entropy Formula in Gravity

The central technical advance. The Ryu-Takayanagi formula (and its generalizations) computes fine-grained entropy via a quantum extremal surface:

$$S = \min_X \left\{ \text{ext}_X \left[ \frac{\text{Area}(X)}{4G_N} + S_{\text{semi-cl}}(\Sigma_X) \right] \right\}$$

where $X$ is a codimension-2 surface, $\Sigma_X$ is the region bounded by $X$ and the cutoff surface, and $S_{\text{semi-cl}}(\Sigma_X)$ is the von Neumann entropy of quantum fields on $\Sigma_X$. The quantity in brackets is the generalized entropy $S_{\text{gen}}(X)$. One extremizes in space and time, then minimizes over all extremal surfaces.

### 7. Entropy of an Evaporating Black Hole

Two competing extremal surfaces:

1. **Vanishing surface**: $X$ shrinks to zero inside the black hole. Area term vanishes; entropy is just $S_{\text{semi-cl}}$ of the enclosed region. This grows as interior Hawking quanta pile up.

2. **Non-vanishing surface**: $X$ lies near the event horizon, appearing at a time $\sim r_s \log S_{BH}$ (the scrambling time) after formation. Its generalized entropy is dominated by the area term, which decreases as the black hole shrinks.

The true fine-grained entropy is the minimum of these two contributions. The transition from the vanishing surface (growing) to the non-vanishing surface (decreasing) reproduces the **Page curve**.

### 8. Entropy of Radiation: The Island Formula

The fine-grained entropy of the Hawking radiation is computed by the **island formula**:

$$S_{\text{Rad}} = \min_X \left\{ \text{ext}_X \left[ \frac{\text{Area}(X)}{4G_N} + S_{\text{semi-cl}}[\text{Rad} \cup \text{Island}] \right] \right\}$$

where the "island" is a region inside the black hole whose boundary is $X$. At early times, no island contributes and $S_{\text{Rad}}$ grows (Hawking's result). At late times, the island contribution -- with $X$ near the horizon -- becomes smaller, giving a decreasing entropy. The transition reproduces the Page curve.

The key insight: it is gravity itself that instructs us to include the island in the entropy calculation. The semiclassical state of the combined radiation and island is nearly pure (the island contains most interior modes that purify the outgoing radiation).

When the full state is pure, $S_{\text{semi-cl}}(\Sigma_X) = S_{\text{semi-cl}}(\text{Rad} \cup \text{Island})$, so the black hole entropy and radiation entropy agree -- as required by unitarity.

### 9. Entanglement Wedge and the Black Hole Interior

The entanglement wedge of the black hole (the region whose degrees of freedom are encoded in the exterior description) evolves:
- Before the Page time: the wedge includes the full interior up to the vanishing surface.
- After the Page time: the interior splits -- the outer portion belongs to the black hole's entanglement wedge, but the deep interior now belongs to the radiation's entanglement wedge (via the island).

This provides evidence that an observer with access to the full radiation can in principle reconstruct information about the black hole interior after the Page time.

### 10. Replica Wormholes

The island formula is derived from the gravitational path integral using the replica trick. Computing $\text{Tr}[\rho^n]$ requires $n$ copies of the geometry. For $n > 1$, new saddle points appear: **replica wormholes** that connect the copies. These saddles enforce unitarity in the entropy calculation. In the $n \to 1$ limit, the replica wormhole saddle becomes the island contribution.

### 11. Discussion

The authors note that the results apply to any semiclassical gravity theory and do not require AdS/CFT. Open problems include: the precise quantum state of the radiation (the formula gives only the entropy, not the state), the AMPS firewall paradox (partially addressed in Appendix A), and extending the results to de Sitter space and cosmology.

---

## Key Results

1. The quantum extremal surface formula computes the fine-grained (von Neumann) entropy of gravitational systems, not just the coarse-grained (thermodynamic) entropy.
2. The Page curve for black hole evaporation is reproduced from semiclassical gravity alone, without invoking the details of a UV-complete theory.
3. The island formula extends the entropy computation to the radiation region: interior "islands" must be included when computing radiation entropy at late times.
4. The transition from vanishing surface to non-vanishing surface at the Page time implements the unitarity-required turnover in the entropy curve.
5. Replica wormholes in the gravitational path integral provide the microscopic derivation of the island formula.
6. The entanglement wedge of the radiation includes the deep black hole interior after the Page time, implying information is recoverable in principle.
7. The results rely only on semiclassical gravity (no AdS/CFT required), suggesting they are universal properties of quantum gravity.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hawking temperature | $T = \hbar\kappa/(2\pi) = 1/(4\pi r_s)$ | Eq. (2.3), (2.14) |
| Generalized entropy | $S_{\text{gen}} = \frac{\text{Area}}{4\hbar G_N} + S_{\text{outside}}$ | Eq. (2.4) |
| Generalized second law | $\delta S_{\text{gen}} \geq 0$ | Eq. (2.5) |
| Euclidean periodicity | $\beta = 4\pi r_s$ | Eq. (2.17) |
| Von Neumann entropy | $S_{\text{vN}} = -\text{Tr}[\rho \log \rho]$ | Eq. (4.1) |
| Quantum extremal surface | $S = \min_X\{\text{ext}_X[\frac{\text{Area}(X)}{4G_N} + S_{\text{semi-cl}}(\Sigma_X)]\}$ | Eq. (6.2) |
| Island formula | $S_{\text{Rad}} = \min_X\{\text{ext}_X[\frac{\text{Area}(X)}{4G_N} + S_{\text{semi-cl}}(\text{Rad}\cup\text{Island})]\}$ | Eq. (8.2) |
| Horizon area entropy | $S_{\text{gen}} \approx \frac{\text{Horizon Area}(t)}{4G_N}$ | Eq. (7.1) |
| Unruh temperature | $T_{\text{proper}} = a/(2\pi)$ | Eq. (2.12) |
| Euclidean partition function | $Z(\beta) \approx e^{-I_{\text{classical}}} Z_{\text{quantum}}$ | Eq. (2.18) |
| Entropy from partition function | $S = (1 - \beta\partial_\beta)\log Z$ | Eq. (2.19) |

---

## Relevance to Phonon-Exflation

This paper is CRITICAL because the phonon-exflation framework evades the black hole information paradox entirely through a fundamentally different mechanism. In the framework: (1) there is no event horizon -- the instanton transit through the fold produces no trapped surface, so the Hawking-Penrose singularity theorems do not apply in the usual sense; (2) the post-transit state is a product state with $S_{\text{ent}} = 0$ (the GGE relic), not a thermal state -- there is no information loss because there is no entanglement between "interior" and "exterior" degrees of freedom; (3) the integrability-protected GGE relic never thermalizes, so the entire Page curve machinery is unnecessary. The island formula's key insight -- that gravity instructs us to include disconnected regions in entropy calculations -- has an analog in the framework's block-diagonal theorem, which separates the Hilbert space into sectors that cannot exchange quantum information. The replica wormhole derivation relies on the Euclidean path integral in ways that parallel the instanton gas computation in Sessions 37-38.
