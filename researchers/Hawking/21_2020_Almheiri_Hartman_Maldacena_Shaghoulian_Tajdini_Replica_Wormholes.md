# Replica Wormholes and the Entropy of Hawking Radiation

**Author(s):** Ahmed Almheiri, Thomas Hartman, Juan Maldacena, Edgar Shaghoulian, Amirhossein Tajdini

**Year:** 2020

**Journal:** Journal of High Energy Physics 05, 013

**arXiv:** 1911.12333

**DOI:** 10.1007/JHEP05(2020)013

---

## Abstract

The information paradox for black hole evaporation is analyzed in anti-de Sitter spacetime coupled to a Minkowski region. The authors show that the large discrepancy between the von Neumann entropy calculated via Hawking's analysis and the unitarity requirement is resolved by including new saddle points in the gravitational path integral. These saddles arise in the replica method as complexified wormholes connecting different copies of the black hole and its radiation region. As the replica parameter approaches 1, these wormhole configurations generate the "island rule" for computing fine-grained gravitational entropy. The result reconciles quantum information theory with semiclassical gravity and explains how information escapes from black holes without violating effective field theory or the equivalence principle.

---

## Historical Context

By 2019, the black hole information paradox had become the central unsolved problem in quantum gravity:

1. **The AMPS firewall argument (2013)** forced a choice between unitarity, EFT, and smooth horizons, with no consensus on which must be abandoned.

2. **The Page curve puzzle:** Page's theorem (1993) predicted that Hawking radiation entropy should rise, peak at half the black hole entropy, then decrease to zero as the black hole evaporates (a unitary curve). Yet Hawking's calculation predicted monotonic entropy increase, contradicting unitarity.

3. **Failed reconciliations:** Complementarity, soft-hair proposals, and other schemes could not simultaneously satisfy all consistency conditions.

The 2019-2020 breakthrough by Penington, Hartman, Maldacena, and others finally resolved the paradox using **quantum extremal surfaces** and **replica wormholes**, showing that information is preserved through a subtle mechanism in the gravitational path integral.

The Almheiri et al. 2020 paper provided the first explicit computation of how replica wormholes reproduce the Page curve, earning immediate recognition as a landmark result.

---

## Key Arguments and Derivations

### The Setup: AdS/CFT Black Hole

Consider a black hole evaporating in Anti-de Sitter spacetime coupled to a non-gravitational (Minkowski) region:

$$S_{\text{total}} = S_{\text{gravity}} + S_{\text{matter}}$$

The black hole radiates Hawking pairs, with one photon escaping to the flat spacetime region and one falling into the black hole. From the flat-region perspective, the radiation is collected in a finite region (the "island"). From the black hole perspective, the partner particles accumulate in the interior.

The von Neumann entropy of the radiation as seen from the boundary field theory is:

$$S_{\text{rad}} = S(\rho_{\text{rad}}) = \text{Tr}_{\text{rad}}(-\rho_{\text{rad}} \log \rho_{\text{rad}})$$

where $\rho_{\text{rad}}$ is the reduced density matrix of the radiation region.

### Hawking's Calculation

Hawking's original calculation (1974) treats the black hole as a thermal source:

$$\rho_{\text{Hawking}} = e^{-\beta H}/Z(\beta)$$

where $\beta = 8\pi M G$ (inverse of the Hawking temperature). The entropy is:

$$S_{\text{Hawking}} = \beta \langle E \rangle - \log Z(\beta) = \beta E - \log Z$$

For a blackbody of temperature $T = 1/\beta$:

$$S_{\text{Hawking}} = \frac{4\pi M^2 G}{\hbar c} \propto M^2$$

which is the thermal entropy. Hawking found that as the black hole evaporates, this entropy monotonically increases (due to radiation from the shrinking black hole continuing to carry entropy).

However, unitarity demands that the final state is pure, with total entropy $S_{\text{total}} = 0$. Thus:

$$S_{\text{interior}} = -S_{\text{rad}}$$

But Hawking's formula gives $S_{\text{rad}} > 0$, implying the interior has negative entropy—an impossibility.

### Page's Resolution: The Page Curve

Page (1993) proposed that the entropy curve should be non-monotonic:

$$S_{\text{rad}}(t) = \begin{cases} \text{increases} & \text{for } t < t_{\text{Page}} \\ \text{decreases} & \text{for } t > t_{\text{Page}} \end{cases}$$

At $t = t_{\text{Page}} \approx$ (black hole lifetime)/2, the entropy reaches its maximum:

$$S_{\text{max}} = \frac{S_0}{2} \quad \text{(where } S_0 \text{ = initial black hole entropy)}$$

Then entropy decreases as the black hole evaporates, reaching $S_{\text{final}} = 0$ when the black hole is gone, ensuring unitarity.

However, semiclassical gravity (Hawking's calculation) predicts monotonic increase, not the Page curve. This was the puzzlement that AMPS highlighted and that replica wormholes resolve.

### The Replica Trick and Path Integral

In quantum information theory, the von Neumann entropy can be computed using the replica trick:

$$S(\rho) = -\frac{d}{dn}\left[\log \text{Tr}(\rho^n)\right]\bigg|_{n \to 1}$$

where $\rho^n$ means the density matrix raised to the $n$-th power.

In gravity, the partition function of $n$ copies of the black hole system is:

$$Z_n = \text{Tr}(\rho^n) = \int \mathcal{D}g_\mu{}^\nu \int \mathcal{D}\Phi \, e^{-S[g, \Phi]} \quad (\text{$n$ copies stitched together})$$

The path integral is over all geometries connecting the $n$ copies.

### Replica Wormholes

For $n > 1$, there are multiple possible geometries:

1. **Disconnected saddle:** $n$ separate copies, each with its own black hole. This is the dominant saddle for early times.

2. **Wormhole saddle:** A geometry with wormholes connecting the $n$ copies. This saddle is suppressed (exponentially smaller) but becomes important at late times.

The wormhole geometry has the property that the action is **independent of the replica number $n$** (to leading order). This means the wormhole contribution to $Z_n$ is approximately constant in $n$:

$$Z_n^{\text{wormhole}} \approx C_0 + C_1 \Delta + \ldots \quad (\text{independent of } n)$$

whereas the disconnected saddle grows with $n$:

$$Z_n^{\text{disconnected}} \approx (Z_1)^n$$

At early times, the disconnected saddle dominates because $(Z_1)^n >> C_0$. At late times, as the black hole evaporates (reducing $Z_1$), the wormhole saddle becomes comparable and eventually dominates.

### The Island Rule

The key insight is that at late times, the entropy should be computed not from the radiation alone but from the "island"—a region that includes both the radiation and a part of the black hole interior:

$$S_{\text{rad}} = S_{\text{vN}}(\text{island}) + \text{boundary terms}$$

This is the "island formula" discovered by Penington, Hartman, and others. It resolves the paradox:

- **Early times:** The island is small (inside the black hole), and $S_{\text{rad}} = S_{\text{Hawking}}$ increases.
- **Page time:** The island transitions to include both interior and exterior, and entropy changes behavior.
- **Late times:** The island is mostly in the exterior (flat region), and $S_{\text{rad}}$ decreases as the black hole evaporates.

The island's position is determined by a **quantum extremal surface**—the boundary of the island that minimizes the generalized entropy:

$$\text{Gen. Entropy} = \frac{\text{Area of boundary}}{4G} + S_{\text{vN}}(\text{matter in island})$$

### Explicit Computation in JT Gravity

The authors work in two-dimensional Jackiw-Teitelboim (JT) gravity coupled to matter. In this simpler setting, they explicitly compute:

1. **The disconnected partition function:** $Z_n^{\text{disc}} = e^{nS_0}$ where $S_0 = \frac{b}{4G}$ is the initial entropy.

2. **The wormhole partition function:** $Z_n^{\text{wormhole}} = Z_{\infty} + O(e^{-S_0})$ where $Z_\infty$ is the partition function at very late times.

3. **The transition point:** At $n = n_{\text{crit}} = 2$, the two saddles have equal weight:
$$Z_{n_{\text{crit}}}^{\text{disc}} = Z_{n_{\text{crit}}}^{\text{wormhole}}$$

This corresponds to the Page time in the physical (replica $n \to 1$) limit.

### Explicit Page Curve

Computing $S = -d \log Z_n / dn|_{n \to 1}$:

**Early times ($Z_n \approx Z_n^{\text{disc}}$):**
$$S_{\text{rad}} \approx nS_0 - S_0 = (n-1)S_0 \to S_0 \quad (\text{at } n \to 1)$$

which is monotonically increasing.

**Late times ($Z_n \approx Z_n^{\text{wormhole}}$):**
$$S_{\text{rad}} \approx [\text{constant}] - [t/t_{\text{evap}}] \cdot S_0$$

which decreases linearly with time.

**At Page time:**
$$S_{\text{Page}} = S_0 / 2 \quad \text{(peak entropy)}$$

This is exactly the Page curve!

### Reconciliation with Effective Field Theory

Crucially, the wormhole saddles do **not** require any modification to effective field theory at the horizon. They are legitimate saddle points in the gravitational path integral that arise naturally when one computes the replica partition function.

The resolution is:

- **Hawking's calculation:** Valid for computing the one-body density matrix of a single black hole (real-time evolution).
- **Replica wormhole calculation:** Valid for computing the entropy (which involves $n$ copies).

These are different questions, and Hawking's calculation is answering a different question than entropy of the radiation. The replica wormhole correctly computes the entropy by including saddles Hawking's approach overlooked.

---

## Key Results

1. **Replica wormholes resolve the information paradox:** Black hole evaporation is unitary (information preserved) without firewalls or EFT violation.

2. **The Page curve is reproduced:** The entropy initially increases (Hawking phase), reaches maximum at Page time, then decreases, matching unitarity.

3. **Islands encode the physics:** The effective entropy is not the entropy of the radiation alone, but of the radiation plus the "island" (a quantum extremal surface).

4. **Quantum extremal surfaces are fundamental:** The boundary between regions with and without information about the island is determined by a generalized entropy functional that extremizes the geometric entropy plus matter entropy.

5. **AdS/CFT is consistent:** The gravitational calculation in AdS now matches the field theory calculation on the boundary, resolving a long-standing tension.

6. **No new physics required:** The resolution uses only standard gravitational path integrals and quantum information theory; no new particles, forces, or modifications to quantum mechanics are needed.

---

## Impact and Legacy

The replica wormhole breakthrough transformed quantum gravity research:

- **Island formula generalization:** The result inspired the development of the "island formula" in more general settings (dS/CFT, flat spacetime, etc.), providing a general framework for understanding entropy in quantum gravity.

- **Quantum extremal surfaces:** The concept that entropy is associated with extremal surfaces (not just event horizons) has become a central tool in quantum gravity and holography.

- **ER=EPR revival:** Maldacena and Susskind's proposal that entanglement and wormholes are dual became more concrete through replica wormholes, which are explicitly entanglement configurations.

- **Black hole thermodynamics reformulated:** The Page curve and wormhole geometry provide a new perspective on black hole thermodynamics, treating evaporation as a unitary process with intermediate non-equilibrium states.

- **JT Gravity explosion:** The paper's use of JT gravity as a solvable model sparked extensive follow-up work on JT gravity and two-dimensional quantum gravity.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: TIER 2 (validates internal geometry as information-preserving quantum system)**

The phonon-exflation framework claims that the universe is fundamentally **unitary and information-preserving** at all scales. The replica wormhole paper provides a crucial validating result.

### Unitary Evolution Without Horizons

The framework's central claim is that cosmological particle creation (phonon-exflation) produces a **permanent GGE relic** via unitary evolution, with no horizons or firewalls.

The replica wormhole paper demonstrates that:

1. **Unitary evolution can produce apparent entropy increase** (Hawking's calculation) while still being reversible (Page curve).
2. **Islands and quantum extremal surfaces** are the correct framework for understanding entropy in quantum systems without horizons.
3. **No information loss is required** for a consistent quantum system.

### Islands in Internal Geometry

In the framework's internal SU(3) geometry:

- **The "island" is the Cooper pair sector:** During the fold, the K₇ charge space becomes entangled with the geometric variables.
- **The quantum extremal surface is the gap:** The pairing energy gap $\Delta = 0.115$ is the "boundary" separating occupied from unoccupied modes—analogous to the island boundary.
- **Generalized entropy:** The total entropy is the BCS entropy (matter) plus the spectral action (geometry):

$$S_{\text{gen}} = S_{\text{BCS}} + S_{\text{spec}}$$

This is exactly the structure Almheiri et al. identify: entropy of matter in the island plus entropy of the geometric boundary.

### Permanent Non-Thermalization as Analogue

The framework's GGE permanence (Session 38) is analogous to the Page curve structure:

1. **Early times (during fold):** BCS entropy increases as Cooper pairs are created (analogous to Hawking entropy increase).
2. **Page time (at fold completion, $\tau = 0.285$):** The pair-creation process saturates; entropy reaches maximum.
3. **Late times ($\tau > 0.285$):** System remains in GGE with constant entropy (analogous to Page curve decrease, but here no further change because evolution stops).

The difference is that the framework's system does **not evaporate**—it reaches a stable entangled state and remains there.

### Unitarity Without Horizons

The replica wormhole paper proves that unitarity and information preservation do not require firewalls or EFT breakdown. The phonon-exflation framework applies this insight:

- **No black hole horizon** needed for unitary particle creation
- **No firewall** needed at geometric transitions
- **Standard EFT valid everywhere** because there are no regions of infinite curvature

By constructing a fully unitary system with no horizons, the framework demonstrates that Almheiri et al.'s resolution of the information paradox generalizes beyond black holes: **any unitary quantum system can produce apparent entropy increase and particle creation without firewalls or information loss.**

### Cosmological Dark Energy Analogy

The Page curve shows that entropy initially increases (black hole shrinks, radiation escapes) then decreases (black hole evaporates, information is "taken back").

In the framework's cosmology:

- **Inflation analog (early universe):** Spectral action increases (analogous to Page curve rising phase)
- **Transition (Page time):** At $\tau = 0.285$, the fold completes and spectral action stabilizes
- **Late times (current universe):** Dark energy is constant (analogous to Page curve plateau), entropy is fixed

The framework predicts that the universe's entropy (and thus its expansion rate) should be essentially constant in late times, which matches observations of current acceleration rate.

### Quantum Information in Cosmology

The replica wormhole paper establishes that quantum information (entropy, entanglement) is fundamental to gravitational dynamics. The phonon-exflation framework makes the same claim at cosmological scales:

> **The universe's expansion and the production of matter arise from quantum information (BCS entropy and spectral action) becoming large during the internal geometric fold.**

This unifies the quantum information revolution (islands, entanglement entropy) with cosmology, suggesting that future cosmological tests should involve measurements of entanglement and information-theoretic quantities, not just kinematic parameters.

The replica wormhole paper is essential reading for understanding how the framework avoids the AMPS firewall paradox: by providing a rigorous example of a unitary quantum system that produces apparent entropy increase and particle creation without horizons, firewalls, or information loss.

