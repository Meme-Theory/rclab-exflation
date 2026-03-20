# Quantum Extremal Surfaces: Holographic Entanglement Entropy beyond the Classical Regime

**Author(s):** Netta Engelhardt, Aron C. Wall

**Year:** 2014 (published 2015)

**Journal:** Journal of High Energy Physics, Vol. 2015, article 73

**arXiv:** 1408.3203 [hep-th]

---

## Abstract

The classical Ryu-Takayanagi formula relates the entanglement entropy of a boundary region in AdS/CFT to the area of a minimal surface in the bulk. However, this formula receives quantum corrections (e.g., from bulk entanglement entropy) that become important beyond the supergravity limit. Engelhardt and Wall introduce **quantum extremal surfaces** that generalize the minimal surface construction by including bulk quantum entanglement entropy. They define the **generalized entropy**:

$$S_{\text{gen}}(X) = \frac{\text{Area}(X)}{4 G_N} + S_{\text{vN}}(A)$$

where $X$ is a codimension-2 surface, $A$ is the bulk region on the "island" side of $X$, and $S_{\text{vN}}$ is the von Neumann entropy. The authors prove that $S_{\text{gen}}$ is extremized (not merely minimized) at the true quantum extremal surface, extending Wald's Noether charge formula to include quantum corrections.

---

## Historical Context

The Ryu-Takayanagi formula (Ryu, Takayanagi 2006) was a breakthrough in understanding AdS/CFT holography:

$$S_{\text{entanglement}}(R) = \frac{\text{Area}(\gamma_R)}{4 G_N}$$

where $R$ is a boundary region and $\gamma_R$ is the minimal-area surface in the bulk whose boundary is homologous to $\partial R$. This formula connects information-theoretic quantities (entanglement) to geometric quantities (area), giving holography a concrete operational meaning.

However, the formula is valid only at leading order in $G_N$ (i.e., in the classical supergravity limit). At subleading orders, bulk quantum fields contribute:

$$S_{\text{entanglement}} = \frac{\text{Area}(\gamma_R)}{4 G_N} + S_{\text{bulk}}(A) + O(G_N)$$

where $S_{\text{bulk}}$ is the entanglement entropy of quantum fields in the bulk region behind the minimal surface. **The question**: How do we systematically include these corrections?

Engelhardt and Wall's answer is the **generalized entropy**—a single functional that combines both classical geometry and quantum entanglement into a unified extremization principle. This extended the work of Penington (2020) on black hole islands retroactively, providing the formal foundation.

For the phonon-exflation framework, quantum extremal surfaces are relevant because the framework's internal SU(3) geometry may admit codimension-2 surfaces (e.g., U(1)_7 breaks or Killing horizons of Killing fields on SU(3)), and the generalized entropy formula applies.

---

## Key Arguments and Derivations

### The Generalized Entropy Functional

Define a codimension-2 surface $X$ in the bulk spacetime (either AdS or a more general geometry). Let $A$ be the "island" region: the portion of bulk space bounded by $X$ on one side and extending to the boundary on the other side. The generalized entropy is:

$$S_{\text{gen}}(X) = \frac{\text{Area}(X)}{4 G_N} + S_{\text{vN}}(A)$$

The von Neumann entropy $S_{\text{vN}}(A)$ is computed for the reduced density matrix of quantum fields in region $A$. Unlike the classical Ryu-Takayanagi surface, which is always at a minimum area, the quantum extremal surface extremizes (may maximize or saddle-point) the generalized entropy:

$$\frac{\delta S_{\text{gen}}}{\delta X} = 0$$

### Extremization Principle

The authors prove that the true quantum-corrected entanglement entropy is:

$$S_{\text{entanglement}}(R) = \min_{\text{islands}} \max_{X} S_{\text{gen}}(X)$$

(The order of quantifiers depends on boundary conditions; in black hole settings it's a double extremization.)

Crucially, the generalized entropy is **non-convex** in X: adding quantum bulk entanglement can lower the total entropy, allowing surfaces to jump discontinuously as parameters change. This is fundamentally different from the classical minimal surface, which always moves continuously.

### Example: Empty AdS

In empty AdS without matter, $S_{\text{vN}}(A)=0$ (vacuum state has zero entanglement), so:

$$S_{\text{gen}} = \frac{\text{Area}(X)}{4 G_N}$$

and the quantum extremal surface reduces to the Ryu-Takayanagi minimal surface. The formula is consistent with the classical limit.

### Example: AdS with Excited State

If the bulk is in an excited state (e.g., with a BTZ black hole), the island region $A$ may contain the black hole interior. The bulk entanglement entropy $S_{\text{vN}}(A)$ becomes substantial, and the generalized entropy surface moves inward (smaller area). This is the **island phenomenon**: quantum corrections push the extremal surface into the black hole interior, encoding information that would classically be lost.

### Wald's Noether Charge Entropy

A key insight is that Engelhardt-Wall generalize Wald's entropy formula (Paper #22) to include quantum corrections. Wald's formula:

$$S_{\text{Wald}}(X) = 2\pi \int_X Q[\xi^a] \, dA$$

(with Killing field $\xi^a$) applies to classical gravity. The generalized entropy adds the quantum correction:

$$S_{\text{gen}}(X) = S_{\text{Wald}}(X) + S_{\text{vN}}(A) + \text{higher orders}$$

For diffeomorphism-invariant theories (including the spectral action), both components are well-defined.

### Causal Structure of Quantum Extremal Surfaces

The authors prove that quantum extremal surfaces have specific causal properties:

1. **Spacelike Separation**: A quantum extremal surface $X$ lies outside the causal light cone of the boundary region $R$. This ensures that information on $R$ cannot be directly causally influenced by $X$; instead, entanglement is the mechanism.

2. **No Barrier Penetration**: In spacetimes with energy-momentum barriers (e.g., black hole interior), quantum extremal surfaces cannot cross certain causal boundaries. This prevents causality violations.

3. **Marginally Trapped Surfaces**: Quantum extremal surfaces are related to (but distinct from) marginally trapped surfaces, which are boundaries of black hole regions.

---

## Key Results

1. **Generalized Entropy Extremization**: Quantum extremal surfaces extremize (not necessarily minimize) the generalized entropy $S_{\text{gen}} = A/(4G_N) + S_{\text{vN}}(A)$, incorporating bulk quantum entanglement systematically.

2. **Quantum Corrections are Finite**: Despite the appearance of entanglement entropy (which can be infinite in field theory), the generalized entropy is finite when the island region $A$ is carefully chosen. This resolves technical divergences in naive sum-over-histories approaches.

3. **Consistency with Thermodynamics**: The generalized entropy satisfies the second law (entropy never decreases) and the first law, reproducing thermodynamic stability conditions.

4. **Island Formula Derivation**: In black hole spacetimes, the generalized entropy formula yields the island formula—information is "hidden" on an island in the black hole interior, and the boundary entropy is minimized when the island is included.

5. **Extension Beyond AdS/CFT**: The framework applies to any diffeomorphism-invariant theory, not just AdS. de Sitter, black hole spacetimes, and cosmological models all admit quantum extremal surfaces.

6. **Connection to Wormholes**: Islands and quantum extremal surfaces are the interior dual of wormhole geometries (ER=EPR), providing a geometric interpretation of entanglement.

---

## Impact and Legacy

Engelhardt and Wall's paper became a cornerstone of modern quantum gravity:

- **Black Hole Information Resolution** (Penington 2020): The island formula solves the black hole information paradox using quantum extremal surfaces.

- **Cosmological Islands** (Hartman et al. 2020): Quantum extremal surfaces extend to cosmological spacetimes (Paper #23), enabling analysis of information in the expanding universe.

- **Bulk Reconstruction** (Jafferis, Wall 2021): Quantum extremal surfaces enable systematic bulk reconstruction beyond the classical Ryu-Takayanagi limit.

- **Dynamical Horizons** (Hollands et al. 2022): Quantum extremal surfaces can be defined on dynamical (non-stationary) horizons, extending the framework to time-dependent geometries.

- **Generalized Thermodynamics** (Wald, Zouros 2023): The generalized entropy is now understood as the entropy of dynamical horizons in general relativity, unifying classical and quantum descriptions.

---

## Framework Relevance

**Application to Spectral Action on M^4 × SU(3)**

The phonon-exflation framework's spacetime is M^4 × SU(3) with metric:

$$ds^2 = g_{\mu\nu}^{(4)} dx^\mu dx^\nu + g_{ab}^{(3)} dy^a dy^b$$

Quantum extremal surfaces can exist on codimension-2 submanifolds. Key possibilities:

1. **Surfaces on SU(3) Slices**: A surface $X$ could be a circle $S^1$ in the SU(3) fiber (codimension 1 in the fiber, codimension 2 overall). The generalized entropy:
$$S_{\text{gen}}(S^1) = \frac{\text{Area}(S^1)}{4 G_N} + S_{\text{vN}}(\text{SU(3) bulk})$$
would quantify the entanglement between U(1)_7 sector and the rest of the internal geometry.

2. **Surfaces on M^4 Spacetime**: Standard cosmological horizons (e.g., de Sitter horizons in inflationary phase) are codimension-1 surfaces, corresponding to codimension-2 closed spacelike surfaces when viewed from M^4 × SU(3). The generalized entropy:
$$S_{\text{gen}}(\partial I) = \frac{\text{Area}_4(\partial I)}{4 G_N} + S_{\text{vN}}(\text{island})$$
applies with the island being a temporal interval during the inflationary phase.

3. **U(1)_7 Breaking as Island Formation**: S35 established that Cooper pairs carry U(1)_7 charge ±1/2, breaking the gauge symmetry spontaneously. If this breaking produces a causal boundary (a "kink" in spacetime topology), a quantum extremal surface would form, and the generalized entropy would determine whether information about the pre-breaking state is preserved:
$$S_{\text{after}} = \min \left[ S_{\text{vN}}(\text{BCS state}) + \frac{\text{Area(boundary)}}{4 G_N} \right]$$

4. **Instanton-Generated Islands**: S38 revealed that instantons mediate particle creation via Schwinger mechanism, producing a GGE relic. The instanton worldline is a codimension-2 object in spacetime (a worldline is codimension-3 in 4D, but in M^4 × SU(3) it traces a 1D path in internal space, codimension-2 overall). The generalized entropy at the instanton locus:
$$S_{\text{inst}} = \frac{\text{Area}_{\text{worldline}}}{4 G_N} + S_{\text{vN}}(\text{Cooper pair pairs})$$
quantifies how much entanglement is generated by pair creation.

**Connection to Parker Particle Creation (Paper #25)**

Parker's work on cosmological particle creation in curved spacetime is the bulk quantum field theory analog of what Engelhardt-Wall formalize. The "quantum bulk entanglement" $S_{\text{vN}}(A)$ in their formula is partly due to the particle creation described by Parker: virtual pair creation in curved spacetime produces entanglement between created particles and the original vacuum. Generalized entropy:
$$S_{\text{gen}} = S_{\text{classical gravity}} + S_{\text{Parker QFT}}$$

**Current Framework Status**

The framework has not yet computed quantum extremal surfaces explicitly. S38 established:
- Instanton dynamics (Schwinger pair creation)
- GGE permanence (8 conserved Richardson-Gaudin integrals)
- Non-thermal relic (no thermalization)

A natural next step (S44+) is to compute the generalized entropy of the instanton gas and determine whether quantum extremal surfaces form during the inflationary phase. This would test whether the framework's information preservation is encoded geometrically (via islands) or merely by integrability.

**No Direct Horizon Connection**

Since the framework has no event horizons (S38), the island formula does NOT directly apply to black hole information. However, the generalized entropy is still relevant for **cosmological horizons** (causal boundaries in de Sitter-like phases) and for **internal SU(3) geometry breaks**, where surfaces can extremize $S_{\text{gen}}$ and encode information.
