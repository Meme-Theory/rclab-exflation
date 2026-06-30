# Islands in Cosmology

**Author(s):** Thomas Hartman, Yikun Jiang, Edgar Shaghoulian
**Year:** 2020
**Journal:** Journal of High Energy Physics 2020, 166 (2020)
**arXiv:** 2008.01022
**Relevance:** MEDIUM

---

## Abstract

A quantum extremal island suggests that a region of spacetime is encoded in the quantum state of another system, like the encoding of the black hole interior in Hawking radiation. We study conditions for islands to appear in general spacetimes, with or without black holes. They must violate Bekenstein's area bound in a precise sense, and the boundary of an island must satisfy several other information-theoretic inequalities. These conditions combine to impose very strong restrictions, which we apply to cosmological models. We find several examples of islands in crunching universes. In particular, in the four-dimensional FRW cosmology with radiation and a negative cosmological constant, there is an island near the turning point when the geometry begins to recollapse. In a two-dimensional model of JT gravity in de Sitter spacetime, there are islands inside crunches that are encoded at future infinity or inside bubbles of Minkowski spacetime. Finally, we discuss simple tensor network toy models for islands in cosmology and black holes.

---

## Key Arguments and Derivations

### The Island Rule (Review)

For a non-gravitational system $R$ coupled to a gravitational region, the fine-grained entropy is:

$$S(R) = \min\left\{\text{ext}_I\left[\frac{\text{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I)\right]\right\}$$

An island $I$ is a region of the gravitational spacetime that is encoded in $R$.

### Three Necessary Conditions for Islands

**Condition 1: Violation of the Bekenstein Area Bound.**
An island can exist only if the matter entropy inside exceeds the area bound:

$$S_{\text{bulk}}(I) > \frac{\text{Area}(\partial I)}{4G_N}$$

This is a necessary condition: the island entropy must exceed what the boundary area can encode.

**Condition 2: The island $I$ is quantum normal.**
The generalized entropy must be non-decreasing under outward deformations of $\partial I$:

$$\frac{\partial S_{\text{gen}}}{\partial V^+} \bigg|_{\partial I} \geq 0, \qquad \frac{\partial S_{\text{gen}}}{\partial V^-} \bigg|_{\partial I} \geq 0$$

where $V^{\pm}$ are the null directions.

**Condition 3: The gravitating region $G$ is quantum normal.**
Similarly, the complement (gravitating region minus the island) must also be quantum normal.

### Islands Near the Turning Point in FRW

For a 4D FRW cosmology with radiation and negative cosmological constant $\Lambda < 0$:

$$ds^2 = -dt^2 + a^2(t)(dr^2 + r^2 d\Omega^2)$$

the universe expands to a maximum size and then recollapses. Near the turning point ($\dot{a} = 0$), the entropy of radiation in a large region can exceed the area bound, creating conditions for an island. The island appears near $a_{\max}$, encoding the region near the crunch in the state of an observer at early times.

### Islands in de Sitter / JT Gravity

In a 2D JT gravity model of de Sitter spacetime with big crunch singularities, islands appear encoding the region near the crunch. The island is located at a spacelike surface in the interior, with the QES at:

$$\frac{\partial}{\partial x}\left[\frac{\phi(x)}{4G_N} + S_{\text{bulk}}(R \cup I)\right] = 0$$

### Tensor Network Models

Simple tensor network models illustrate how islands arise. A random tensor network with bond dimension $\chi$ models the gravitational path integral. An island corresponds to a minimal cut through the tensor network that passes through the interior of the gravitational region.

### No Islands in Expanding Universes

The conditions for islands are extremely restrictive. In particular:
- Islands do NOT appear in eternally expanding (de Sitter) spacetimes with $\Lambda > 0$ and no crunch.
- Islands require either a crunch, a black hole, or some other mechanism that creates regions where the area bound is violated.

---

## Key Results

1. Three necessary conditions for islands are derived: Bekenstein bound violation, quantum normality of the island, and quantum normality of the complement.
2. Islands exist in **crunching cosmologies** -- near the turning point of a recollapsing FRW universe.
3. Islands do **not** appear in eternally expanding universes without crunches or black holes.
4. In FRW with $\Lambda < 0$, the island near the turning point encodes the crunching region.
5. Tensor network toy models provide intuition: islands correspond to minimal cuts through the network.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Island rule | $S(R) = \min\left\{\text{ext}_I\left[\frac{\text{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I)\right]\right\}$ | Sec. 2 |
| Bekenstein bound violation | $S_{\text{bulk}}(I) > \frac{\text{Area}(\partial I)}{4G_N}$ | Condition 1 |
| Quantum normality | $\frac{\partial S_{\text{gen}}}{\partial V^{\pm}}\big|_{\partial I} \geq 0$ | Condition 2 |
| Generalized entropy | $S_{\text{gen}} = \frac{\text{Area}}{4G_N} + S_{\text{bulk}}$ | Sec. 2 |
| QES condition | $\partial_x\left[\frac{\phi}{4G_N} + S_{\text{bulk}}\right] = 0$ | Sec. 3 |
| FRW metric | $ds^2 = -dt^2 + a^2(t)(dr^2 + r^2 d\Omega^2)$ | Sec. 4 |

## Relevance to Phonon-Exflation

The phonon-exflation framework has no crunching cosmology, no black hole horizons, and no negative cosmological constant -- precisely the conditions under which Hartman-Jiang-Shaghoulian show islands do NOT appear. This is consistent with the framework's resolution: the transit produces a product state ($S_{\text{ent}} = 0$) with no need for islands to encode hidden regions. The paper's result that islands require Bekenstein bound violation is a useful diagnostic: the framework's spectral geometry never violates this bound because there are no trapped surfaces.
