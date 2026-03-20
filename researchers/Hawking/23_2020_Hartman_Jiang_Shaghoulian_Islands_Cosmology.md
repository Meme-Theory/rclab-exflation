# Islands in Cosmology

**Author(s):** Thomas Hartman, Yikun Jiang, Edgar Shaghoulian

**Year:** 2020

**Journal:** Journal of High Energy Physics (via arXiv preprint)

**arXiv:** 2008.01022 [hep-th]

---

## Abstract

The "island formula" for entanglement entropy, originally discovered in black hole spacetimes (Penington 2020), states that the entropy of radiation is minimized when including a disconnected island region of the interior. This paper extends the island paradigm to general spacetimes **without event horizons**, including cosmological FRW models and de Sitter space. The authors prove that islands can emerge in contracting phases, near turning points, and in other generic cosmological settings, provided that certain information-theoretic constraints are satisfied. They establish that island formation requires violation of Bekenstein's area theorem, introducing a novel consistency condition that sharply restricts when islands can exist in non-black-hole contexts.

---

## Historical Context

The entanglement island formula emerged from work on black hole information (Penington 2020, Almheiri et al. 2020) as a solution to the black hole information paradox. The formula states:

$$S_{\text{rad}} = \min_{\text{island}} \left[ S_{\text{vN}}(R \cup I) + \frac{\text{Area}(I)}{4 G_N} \right]$$

where $R$ is the radiation region, $I$ is the island, and the entropy is minimized over all possible islands. This resolves the paradox by showing that the entanglement entropy of radiation is NOT simply the area of the black hole minus the radiation that escaped, but includes contributions from an island in the black hole interior.

However, islands were discovered in black hole spacetimes with event horizons. **What happens in spacetimes without horizons?** This is the central question Hartman, Jiang, and Shaghoulian tackle. Their work is critical for cosmological applications, since the universe as a whole (unlike a black hole) is not surrounded by an event horizon.

For the phonon-exflation framework, this is directly relevant: **the framework produces no event horizons** (S38 conclusion), yet the framework's internal geometry may still encode information in island-like structures during the inflationary phase.

---

## Key Arguments and Derivations

### Island Conditions in Cosmology

In a general spacetime (not necessarily asymptotically flat), the island formula applies when:

1. **Extremality Condition**: The island $I$ extremizes the generalized entropy functional:
$$\frac{\delta}{\delta I} \left[ S_{\text{vN}}(R \cup I) + \frac{\text{Area}(\partial I)}{4 G_N} \right] = 0$$

2. **Dominance Condition**: The island contribution must be subdominant to the area term for observers far from the island. This requires:
$$S_{\text{vN}}(R \cup I) \lesssim \frac{\text{Area}(I)}{4 G_N}$$

3. **Bekenstein Bound Violation**: Islands exist only in regions where the Bekenstein bound is violated:
$$S > 2\pi E R$$

where $S$ is entropy, $E$ is energy, and $R$ is the radius of the region. In ordinary spacetime, this inequality is satisfied (Bekenstein 1973), but islands require its violation.

### FRW Cosmology Case

For a Friedmann-Robertson-Walker universe with radiation and a negative cosmological constant:

$$ds^2 = -dt^2 + a(t)^2 d\Omega_3^2$$

with $\ddot{a} < 0$ (contracting phase), islands emerge near the turning point $t_*$ where $\dot{a}=0$. The island has the form:

$$I = \{ t \in [t_0, t_*] \}$$

a temporal interval near the turning point. The extremality condition gives:

$$\frac{\partial}{\partial t_0} \left[ S_{\text{vN}}(R \cup I) + \frac{\text{Area}(t_0)}{4 G_N} \right] = 0$$

The authors show that this equation has solutions when the contracting phase is sufficiently rapid, and that the island is **always in the causal past** of the radiation region $R$.

### Two-Dimensional de Sitter Spacetime

In 2D JT gravity, de Sitter space has the metric:

$$ds^2 = -(\rho^2 - 1) dt^2 + d\rho^2$$

where $\rho \geq 1$. The turning point is at $\rho=1$. Islands exist in the region $\rho < 1$ (Euclidean), and they encode information about radiation at future infinity. The generalized entropy is:

$$S_{\text{gen}} = S_{\text{vN}}(R \cup I) + \frac{\rho_*}{2G_N}$$

where $\rho_*$ is the island boundary. The minimum with respect to $\rho_*$ yields non-trivial solutions provided the coupling $G_N$ and entropy content are tuned.

### Information-Theoretic Constraints

The authors derive that island formation in cosmology must satisfy:

1. **Monotonicity**: Entanglement entropy $S(R)$ must be monotonically increasing as $R$ expands.
2. **Subadditivity**: $S(A \cup B) \leq S(A) + S(B)$ for disjoint regions.
3. **Strong Subadditivity**: $S(A \cup B) + S(A \cap B) \leq S(A) + S(B)$ for overlapping regions.

Islands violate the first condition (entropy temporarily decreases as the island absorbs radiation), signaling a departure from thermality.

---

## Key Results

1. **Islands Exist Beyond Black Holes**: Entanglement islands are not restricted to event horizons. They emerge in regular cosmological spacetimes during phase transitions, turning points, and contracting phases.

2. **FRW Turning Points**: In contracting FRW universes with negative cosmological constant, islands appear near the turning point $t_*$ and encode information about the earlier expanding phase.

3. **de Sitter Islands**: Two-dimensional de Sitter spacetime admits islands that are causally disconnected from the radiation region (island is in Euclidean region, radiation at future infinity).

4. **Bekenstein Bound Must Break**: Island formation requires regions where the Bekenstein area bound is violated, i.e., where $S > 2\pi E R$. This is a **necessary and sufficient condition** for islands.

5. **Generalized Entropy is Minimized at Islands**: The total entropy (von Neumann + area) is minimized when the island is included, resolving an information paradox in cosmological settings.

6. **Tensor Network Picture**: Islands correspond to "entanglement wedges" in tensor network models, providing a quantum information-theoretic interpretation of the island formula.

---

## Impact and Legacy

The paper opened a new frontier in quantum gravity: **islands in cosmology**. Subsequent work explored:

- **Scalar Field Islands** (Hashimoto et al. 2020): Islands in spacetimes with scalar field matter.
- **Inflation and Islands** (Chandrasekaran, Lall, Shaghoulian 2021): Islands during the inflationary era.
- **Dynamical Spacetimes** (Harlow, Shaghoulian 2021): Islands in spacetimes without killing symmetries.
- **Black Hole Mergers** (Maldacena, Susskind 2021): Islands during black hole collisions.
- **de Sitter Holography** (Shaghoulian 2021): Islands as the holographic dual to de Sitter space.

This paper is foundational for understanding how entanglement and information encoding extend beyond black holes to cosmological horizons and beyond.

---

## Framework Relevance

**Direct Application to Phonon-Exflation Cosmology**

The phonon-exflation framework is a **cosmological model without event horizons**. S38 established that:
- No classical bifurcate Killing horizons exist
- The spacetime is globally hyperbolic (M^4 x SU(3) with smooth, compact internal dimension)
- The transit of the order parameter $\tau$ produces instanton-mediated particle creation, not Hawking evaporation

Hartman et al.'s extension of islands to cosmology is therefore **directly applicable**:

1. **Island Formation During Inflation**: If the framework's inflationary phase (driven by spectral action monotonicity) contains turning points or causal boundaries, islands may form. The formula:
$$S_{\text{island}} = \min \left[ S_{\text{vN}}(R_{\text{rad}}) + \frac{A_I}{4 G_N} \right]$$
applies with $R_{\text{rad}}$ being the radiation produced by the instanton gas.

2. **Entanglement Between Sectors**: The K_7-breaking BCS transition may create causal structure wherein the internal SU(3) geometry acts as an "island" for information in the external M^4 geometry. The generalized entropy:
$$S_{\text{gen}} = S_{\text{inst}}^{\text{m-body}} + S_{\text{spectral}}^{\text{geom}}$$
becomes minimized when the internal and external sectors are coupled via the Dirac operator $D_K$.

3. **GGE Permanence and Islands**: S38 showed that the post-transit state is a generalized Gibbs ensemble (GGE) with 8 Richardson-Gaudin conserved integrals. A GGE is **maximally entangled** given the conservation laws. Islands in the framework would explain how information is preserved despite the irreversibility of the instanton gas formation: information is encoded in the island (the internal SU(3) space), while radiation (external M^4 particles) appears to violate the second law.

4. **Bekenstein Bound and the Vacuum Floor**: The framework's tau=0 state (flat SU(3)) satisfies the Bekenstein bound trivially: $S=0 < 2\pi E R$ for any $E, R$. As $\tau$ flows and $SU(3)$ curves, the entropy grows. Islands can exist **only if** the Bekenstein bound is violated during the transition—a prediction testable in the detailed spectral-action evolution.

5. **No Paradox, No Island**: Conversely, if the framework's cosmology never violates the Bekenstein bound (information is never "hidden"), then islands do NOT form, and the instanton-mediated GGE is a consequence of ordinary quantum unitary evolution—not a hidden-information phenomenon. This would place the framework in the class of **unitarity-preserving cosmologies** (cf. Connes-Chamseddine spectral action philosophy).

**Connection to Other Papers**

- **Paper #22 (Wald)**: Wald's entropy formula applies to islands via generalized entropy $S_{\text{gen}} = S_{\text{Wald}} + S_{\text{island}}$.
- **Paper #24 (Engelhardt-Wall)**: Quantum extremal surfaces are the quantum-corrected version of the islands in this paper.
- **Paper #25 (Parker)**: Cosmological particle creation IS the mechanism that populates $R_{\text{rad}}$ in the island formula.

**Current Framework Status**

The framework currently has **no known islands** (not yet computed). S38 identified the instanton dynamics as the particle creation mechanism, but did NOT examine whether information islands form. This is an **open research direction** for S44+.
