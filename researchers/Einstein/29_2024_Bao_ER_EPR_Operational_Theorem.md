# ER = EPR Is an Operational Theorem

**Author(s):** Chris Fields, James F. Glazebrook, Antonino Marciano, Emanuele Zappala
**Year:** 2024
**Journal:** Physics Letters B, vol. 857, p. 138972
**arXiv:** 2410.16496

---

## Abstract

We demonstrate that within a two-agent LOCC (local operations and classical communication) protocol, Alice and Bob cannot operationally distinguish monogamous entanglement from a topological identification of points in their respective local spacetimes. Therefore, in the operational setting accessible to local observers, ER = EPR can be recovered as an operational theorem. The construction provides a simple demonstration of the non-traversability of ER bridges, generalizes previous geometric approaches to ER = EPR since it does not depend on an embedding geometry, and shows that the local topology of spacetime is observer-relative.

---

## Historical Context

The ER = EPR conjecture, proposed by Maldacena and Susskind (2013), represents a profound claim that Einstein-Rosen bridges (wormholes) and Einstein-Podolsky-Rosen entanglement are equivalent descriptions of the same phenomenon. This conjecture attempts to unify quantum information theory with spacetime geometry—a central aspiration in quantum gravity.

Previous work has focused on geometric embeddings and holographic dualities to support the conjecture. However, the present work takes a more operational approach, grounded in what local agents can actually distinguish or measure. This framing is crucial: if two configurations produce identical operational outcomes under all measurements available to local observers, then they are operationally indistinguishable, even if they differ geometrically.

The result resonates with deep principles in quantum mechanics: the identification of physical states with what can be operationally determined about them. In curved spacetime, this principle extends to spacetime topology itself. The paper's key insight is that monogamous entanglement (the correlations in an EPR pair) and spacetime identification (the "gluing" of points that constitutes an ER bridge) produce the same observable consequences for local agents restricted to LOCC protocols.

---

## Key Arguments and Derivations

### LOCC Protocols and Operational Equivalence

In quantum information theory, LOCC protocols formalize what separated parties can accomplish using only local quantum operations and classical communication. The key constraint is that no quantum information can be transmitted between parties—only classical bits.

Consider two spatially separated regions, Region A (Alice) and Region B (Bob). In standard quantum mechanics, they may share an entangled state $|\psi\rangle_{AB}$. The monogamy of entanglement constraint states that if subsystem A is maximally entangled with subsystem B, then A cannot be entangled with any other system C. Mathematically:

$$E(A:B) + E(A:C) \leq E_{\text{max}}$$

where $E(A:B)$ denotes the entanglement between systems A and B.

### Spacetime Topology in Operational Frameworks

From Einstein's perspective, spacetime is a continuous manifold with a metric structure. An ER bridge connects two spatially remote points through a wormhole geometry:

$$ds^2 = -dt^2 + dr^2 + (M-2m)^2 dΩ^2$$

where $M$ is the ADM mass and $m$ is half the bridge length. For non-traversable wormholes (which preserve causality), the bridge width remains causally disconnected from any classical signal path.

The operational question becomes: if Alice in Region A and Bob in Region B are separated by either (a) monogamous entanglement with no classical channel, or (b) a non-traversable ER bridge, can they distinguish these scenarios using local operations?

### The Equivalence Theorem

The paper's core argument proceeds as follows:

**Theorem**: Under LOCC protocols restricted to each party's local Hilbert space, Alice and Bob cannot operationally distinguish monogamous entanglement (an EPR state) from a topological identification of points in their respective spacetime regions (an ER bridge).

**Proof sketch**:

1. Entanglement manifests operationally as perfect correlation in local measurement outcomes, despite space-like separation. An EPR state $|\psi\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ guarantees that if Alice measures spin-up on her qubit, Bob's measurement of his qubit will yield spin-up with certainty.

2. A non-traversable ER bridge geometrically connects the two regions but forbids any classical signal from crossing. From an operational viewpoint, this means Alice's local measurements cannot access Bob's spacetime region, and vice versa.

3. Both configurations produce identical constraints on what Alice and Bob can learn about correlated outcomes: they obtain perfect correlations without the ability to send classical information across the boundary. Any LOCC protocol returns the same statistics.

4. Therefore, the operational content—the set of all possible experimental outcomes and their probabilities—is identical in both cases.

### Non-Traversability and Causality

The paper emphasizes that the ER bridges under consideration are non-traversable (Schwarzschild wormholes). This is essential: a traversable wormhole would allow causal signaling, which would violate the LOCC constraint (it would enable "superluminal" classical communication).

The non-traversability condition ensures that Alice cannot classically signal through the bridge, preserving causality and maintaining the operational equivalence with pure entanglement.

### Observer-Dependent Topology

A profound consequence is that spacetime topology becomes observer-relative:

$$\text{Topology}(A) = \{\text{operational scenarios distinguishable to } A\}$$

An observer restricted to LOCC cannot distinguish ER from EPR. However, an observer with access to additional physical resources (e.g., a wormhole traversal method or an external reference frame) might perceive different local topologies.

This generalizes earlier insights from quantum mechanics that properties of quantum systems are reference-frame dependent.

---

## Key Results

1. **Operational Equivalence**: ER and EPR are operationally indistinguishable under LOCC protocols, establishing a rigorous operational foundation for the ER = EPR conjecture.

2. **Non-Embedding Generality**: Unlike prior geometric approaches, this framework does not require the spacetime to embed in a larger manifold. Topology is defined operationally by the set of distinguishable configurations.

3. **Non-Traversability Demonstration**: The construction naturally explains why ER bridges are non-traversable: traversability would create asymmetry between EPR and ER (allowing signaling), violating operational equivalence.

4. **Observer-Relative Topology**: Spacetime structure (at least locally) is not intrinsic but rather depends on the observer's operational capabilities.

5. **Quantum-Gravity Interface**: The result bridges quantum information concepts (entanglement, LOCC) with general relativity (spacetime topology), offering a new perspective on the information-geometry correspondence.

---

## Impact and Legacy

This paper contributes to a growing literature that approaches quantum gravity not through traditional field quantization but through quantum information theory. The operational perspective has proven fruitful in understanding entanglement entropy, black hole thermodynamics, and holography.

Fields, Glazebrook, and collaborators have built a program around local quantum field theory structures and their gravitational duals. By casting ER = EPR in operational terms, this work makes the conjecture more testable (in principle) and more resistant to objections about geometric ambiguity.

The result also supports the modern paradigm that spacetime emerges from quantum entanglement rather than being fundamental. If topology is operationally defined, then the emergence of topology from entanglement becomes less mysterious.

---

## Connection to Phonon-Exflation Framework

**Relevance: HIGH — CHSH Bound Challenge**

The framework's core mechanism derives particle masses and interactions from spectral properties of SU(3) Kaluza-Klein compactification. A critical open question is whether quantum correlations in the internal geometry can generate the CHSH bound violation observed in quantum systems.

The EPR result in this paper—that entanglement cannot be operationally distinguished from spacetime identification in an observer-dependent way—suggests a bridge: **if the internal SU(3) fiber space exhibits topological constraints (like non-traversable bridges at the Planck scale), then correlations in the spectrum of $D_K$ could manifest as EPR-type entanglement for observers probing the lower-dimensional effective spacetime**.

Specifically:
- The phonon-exflation framework assumes M4 × SU(3) with K7 symmetry emerging dynamically.
- K7 is a non-abelian gauge symmetry that couples to the Dirac spectrum.
- If K7 connects points in the fiber that cannot exchange classical signals (analogous to non-traversable wormholes), then the resulting entanglement structure would produce CHSH violations.
- The bound $S_{\text{CHSH}} = 2\sqrt{2}$ could emerge from the spectral operator's structure, specifically the mixing of matter representations under K7 holonomy.

**Current Status**: The framework predicts second-order phase transitions (BCS-type). If the internal topology exhibits ER-like bridges, this could explain why quantum correlations reach maximal violation.

**Next Step**: Compute K7 holonomy around closed loops in the SU(3) fiber and test whether the resulting gauge structure saturates CHSH bound for a specific observable pair.
