# Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?

**Authors:** Albert Einstein, Boris Podolsky, Nathan Rosen
**Year:** 1935
**Journal:** *Physical Review*, **47**, 777--780

---

## Abstract

This paper -- universally known as the EPR paper -- presents the most famous challenge to the completeness of quantum mechanics. The authors construct a thought experiment involving two particles that have interacted and then separated, such that measuring one particle's position (or momentum) instantly determines the other's position (or momentum) with certainty, despite the particles being arbitrarily far apart. Since quantum mechanics assigns no simultaneous definite values to both position and momentum (the uncertainty principle), EPR argue that either quantum mechanics is incomplete (there exist "elements of reality" not captured by the wave function) or the measurement of one particle instantaneously influences the distant particle (violating locality). Assuming locality, they conclude that quantum mechanics is incomplete. The paper catalyzed decades of foundational debate and ultimately led to Bell's theorem (1964), which proved that no local hidden-variable theory can reproduce all quantum predictions, and to experimental tests confirming quantum nonlocality.

---

## Historical Context

### Einstein's Dissatisfaction with Quantum Mechanics

Einstein was never comfortable with the Copenhagen interpretation of quantum mechanics, despite having contributed foundational ideas (light quanta, stimulated emission, BEC statistics). His objections were not about the formalism's predictive success but about its interpretive completeness.

At the 1927 Solvay Conference, Einstein challenged Bohr with a series of thought experiments designed to circumvent the uncertainty principle. Bohr successfully defended the principle each time, but Einstein remained unconvinced. His concerns evolved from attempting to violate the uncertainty principle to questioning whether the quantum state provided a complete description of physical reality.

By the early 1930s, Einstein had crystallized his objection around what he saw as the central issue: quantum mechanics seemed to require "spooky action at a distance" (spukhafte Fernwirkung) -- the idea that measuring one particle could instantaneously affect the physical state of a distant particle.

### The Collaborators

Boris Podolsky and Nathan Rosen were both at the Institute for Advanced Study in Princeton with Einstein. Podolsky apparently wrote the published version, and Einstein later expressed some dissatisfaction with the presentation, feeling that the central physical point was obscured by the formalism. In later letters, Einstein presented the argument more clearly and concisely.

### The State of Quantum Mechanics in 1935

By 1935, quantum mechanics was a mature theory. The Schrodinger equation, matrix mechanics, and Dirac's relativistic electron theory were all well established. The Born interpretation (the wave function gives probabilities via $|\psi|^2$) was standard. The uncertainty principle was universally accepted as a feature of the formalism, though its physical interpretation was debated.

---

## Key Arguments and Derivations

### I. The Criterion of Reality

EPR begin with a seemingly innocuous definition:

> **Criterion of Reality:** "If, without in any way disturbing a system, we can predict with certainty (i.e., with probability equal to unity) the value of a physical quantity, then there exists an element of physical reality corresponding to this physical quantity."

This criterion is empiricist in spirit: a property is "real" if it can be predicted with certainty without disturbing the system. It does not require that the property be measured, only that it COULD be predicted.

### II. The Condition of Completeness

EPR define:

> **Completeness:** A physical theory is complete if every element of physical reality has a counterpart in the theory.

If a physical quantity has a definite value that can be predicted with certainty, a complete theory must contain a mathematical element representing that value.

### III. The Quantum-Mechanical Uncertainty Relations

For a single particle, quantum mechanics asserts:

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

If the wave function is a position eigenstate ($\Delta x = 0$), the momentum is completely undefined ($\Delta p = \infty$), and vice versa. In quantum mechanics, position and momentum cannot simultaneously have definite values.

Therefore, if one adopts the criterion of reality AND the completeness assumption, then position and momentum cannot simultaneously be "real" -- at most one can have a definite value at any time.

### IV. The EPR State

EPR now construct a two-particle state that creates a paradox. Consider two particles (1 and 2) that have interacted and then separated. Their joint wave function is:

$$\Psi(x_1, x_2) = \int_{-\infty}^{\infty} e^{(i/\hbar)(x_1 - x_2 + x_0)p}\,dp$$

This is a delta function in relative position: $\Psi \propto \delta(x_1 - x_2 + x_0)$, meaning the particles are perfectly correlated in position: $x_1 - x_2 = -x_0$ (a constant).

In momentum representation:

$$\Psi(p_1, p_2) \propto \delta(p_1 + p_2)$$

meaning the particles are also perfectly anti-correlated in momentum: $p_1 + p_2 = 0$.

In modern notation, the EPR state is an eigenstate of both the relative position $\hat{x}_1 - \hat{x}_2$ and the total momentum $\hat{p}_1 + \hat{p}_2$. These two operators commute:

$$[\hat{x}_1 - \hat{x}_2, \hat{p}_1 + \hat{p}_2] = [\hat{x}_1, \hat{p}_1] + [\hat{x}_1, \hat{p}_2] - [\hat{x}_2, \hat{p}_1] - [\hat{x}_2, \hat{p}_2]$$
$$= i\hbar + 0 - 0 - i\hbar = 0$$

so the state can be a simultaneous eigenstate of both, consistently with quantum mechanics.

### V. The Argument

Now suppose the two particles are far apart. An experimenter measures particle 1's position $x_1$ and obtains a definite value. From the perfect correlation, particle 2's position is then known with certainty: $x_2 = x_1 + x_0$. By the criterion of reality, $x_2$ is an element of physical reality.

Alternatively, the experimenter could instead measure particle 1's momentum $p_1$. From the anti-correlation, particle 2's momentum is then known: $p_2 = -p_1$. By the criterion of reality, $p_2$ is an element of physical reality.

The critical point: the choice of what to measure on particle 1 cannot physically affect particle 2, since they are far apart. (This is the **locality assumption** -- no faster-than-light influences.) Therefore, BOTH $x_2$ and $p_2$ are simultaneously elements of physical reality, regardless of which measurement is actually performed on particle 1.

But quantum mechanics does not assign simultaneous definite values to $x_2$ and $p_2$ (the uncertainty principle). Therefore, quantum mechanics is incomplete -- there are elements of reality not captured by the wave function.

### VI. The Logical Structure

The EPR argument has the form of a disjunctive syllogism:

1. Either quantum mechanics is incomplete, OR measurements on particle 1 instantaneously affect particle 2 (nonlocality).
2. Assume locality (no instantaneous action at a distance).
3. Therefore, quantum mechanics is incomplete.

The conclusion is conditional: IF locality holds, THEN QM is incomplete. EPR assume locality and conclude incompleteness. The alternative -- accepting nonlocality -- was considered by EPR to be so absurd as to be dismissible.

---

## Physical Interpretation

### Entanglement

The EPR state is what Schrodinger (1935), in direct response to the EPR paper, called an "entangled" (verschrankt) state. The two-particle wave function cannot be written as a product of single-particle wave functions:

$$\Psi(x_1, x_2) \neq \psi_1(x_1)\psi_2(x_2)$$

This non-separability is the mathematical signature of entanglement. The particles are correlated in a way that has no classical analog.

### Bohr's Response

Niels Bohr responded immediately (1935, same journal) with a paper of the same title. Bohr's response rejected the EPR criterion of reality, arguing that the experimental arrangement (the choice of what to measure on particle 1) defines what can be meaningfully said about particle 2. There is no context-independent "element of reality" -- physical properties are defined only relative to a measurement context.

Bohr's response was influential but widely regarded as obscure. The debate between Einstein and Bohr continued until Einstein's death in 1955, with neither convincing the other.

### Hidden Variables

EPR's conclusion -- that quantum mechanics is incomplete -- suggests that there exist "hidden variables" that, if known, would determine measurement outcomes with certainty. The wave function would then be a statistical description of an ensemble, not a complete description of an individual system.

Von Neumann (1932) had claimed to prove that hidden variables are impossible, but his proof contained a questionable assumption (additivity of expectation values for non-commuting observables). Bohm (1952) constructed an explicit hidden-variable theory (Bohmian mechanics) that reproduces all quantum predictions, demonstrating that von Neumann's "proof" was flawed.

---

## Impact and Legacy

### Bohm's Reformulation (1951)

David Bohm simplified the EPR argument by replacing continuous position/momentum variables with discrete spin-1/2 particles. The Bohm-EPR state is:

$$|\Psi\rangle = \frac{1}{\sqrt{2}}(|\uparrow\rangle_1|\downarrow\rangle_2 - |\downarrow\rangle_1|\uparrow\rangle_2)$$

This spin singlet state has the same structure as EPR: measuring particle 1's spin along any axis instantly determines particle 2's spin along the same axis. Bohm's formulation made the EPR paradox tractable for quantitative analysis.

### Bell's Theorem (1964)

John Bell proved that ANY local hidden-variable theory must satisfy an inequality (the Bell inequality) that quantum mechanics violates. See Paper 13 for a detailed analysis. Bell's theorem transformed EPR from a philosophical puzzle into an experimentally testable proposition.

### Experimental Tests

Aspect et al. (1982) performed the first convincing test, measuring polarization correlations of entangled photons and finding violations of Bell's inequality consistent with quantum predictions. Subsequent experiments (Zeilinger et al., 2015; loophole-free tests) have definitively confirmed quantum nonlocality.

The 2022 Nobel Prize in Physics was awarded to Alain Aspect, John Clauser, and Anton Zeilinger for their experimental work on entanglement and Bell inequality violations.

### Quantum Information

The EPR correlations, far from being a defect, have become a resource. Quantum entanglement is the foundation of:
- Quantum teleportation (Bennett et al., 1993)
- Quantum cryptography (Ekert, 1991)
- Quantum computing (entangled qubits as computational resource)
- Quantum error correction

---

## Connections to Modern Physics

### Entanglement Entropy

In quantum field theory and quantum gravity, the entanglement entropy between spatial regions:

$$S_A = -\text{Tr}(\rho_A \ln \rho_A)$$

(where $\rho_A$ is the reduced density matrix of region $A$) is a central concept. The Ryu-Takayanagi formula relates entanglement entropy to geometric areas in holographic theories, connecting EPR-type correlations to the structure of spacetime itself.

### ER = EPR

Maldacena and Susskind (2013) conjectured that entangled particles (EPR pairs) are connected by Einstein-Rosen bridges (wormholes). This "ER = EPR" correspondence suggests a deep connection between quantum entanglement and spacetime geometry -- precisely the two aspects of physics that Einstein kept separate.

### Nonlocality and Realism

The experimental violation of Bell inequalities forces a choice: abandon locality, abandon realism (definite pre-existing values), or both. The majority interpretation in quantum foundations is that realism fails -- measurement outcomes are not predetermined. However, nonlocal realistic theories (Bohmian mechanics) remain viable. The debate continues in quantum foundations.

### EPR in Kaluza-Klein and Extra-Dimensional Frameworks

In frameworks where quantum mechanics emerges from higher-dimensional classical geometry, the EPR correlations must be explained without fundamental nonlocality. If the 4D wave function is a projection from a higher-dimensional space, then the apparent nonlocal correlations could in principle arise from geometric connections in the full space that appear nonlocal only in the projected description. This is precisely the challenge identified in foundational analyses of emergence frameworks: demonstrating that CHSH = $2\sqrt{2}$ follows from the geometry, rather than being put in by hand.
