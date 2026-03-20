# Entropy and the Spectral Action

**Author(s):** Ali H. Chamseddine, Alain Connes, Walter D. van Suijlekom
**Year:** 2018
**Journal:** Communications in Mathematical Physics, Vol. 2019
**arXiv:** 1809.02944
**Published:** September 12, 2018

---

## Abstract

This paper establishes a remarkable connection between quantum information theory and the spectral action principle by computing the von Neumann entropy from fermionic second quantization of a spectral triple. The authors demonstrate that this entropy is given by the spectral action of the spectral triple for a specific universal function. They further discover an unexpected link to number theory: the coefficients in the heat expansion of the spectral triple relate directly to the Riemann zeta function. Specifically, the coefficient $c(4)$ is a rational multiple of $\zeta(5)$ and $c(2)$ is a rational multiple of $\zeta(3)$. Through the functional equation of the Riemann xi function, the authors reveal a duality between positive and negative dimensional coefficients. This work bridges three distinct mathematical domains—high-energy physics, number theory, and quantum information theory—and suggests deep connections between the spectral geometry of the standard model and fundamental constants of mathematics.

---

## Historical Context

Since its introduction in 1996, the spectral action principle has raised fundamental questions: What is the physical interpretation of the spectral action? Is it merely a mathematical formula that reproduces physics, or does it have deeper significance in quantum mechanics?

In classical thermodynamics and quantum information theory, entropy measures the number of microscopic states available to a system. Von Neumann entropy, defined as $S = -\text{Tr}(\rho \log \rho)$ for a density matrix $\rho$, quantifies information content and is central to quantum mechanics.

This 2018 paper by Chamseddine, Connes, and van Suijlekom makes a stunning discovery: the spectral action, when computed for fermionic second quantization, **is the entropy**. This suggests that the spectral action is not merely a formula for computing dynamics—it measures the information content of the quantum geometry itself.

The connection to the Riemann zeta function is equally profound. The Riemann hypothesis, one of mathematics' greatest unsolved problems, concerns the zeros of $\zeta(s)$. That these zeros should appear in the heat kernel expansion of the Dirac operator on the standard model geometry suggests an intimate connection between particle physics and number theory.

For phonon-exflation, this result indicates that the internal metric (and its phonon excitations) are not just geometric degrees of freedom but also information-theoretic ones. The entropy of the metric determines its thermodynamic behavior and evolution.

---

## Key Arguments and Derivations

### Von Neumann Entropy of Fermionic Systems

Consider a fermionic system described by creation and annihilation operators $c_i^\dagger, c_i$ satisfying the canonical anticommutation relations:

$$\{c_i, c_j^\dagger\} = \delta_{ij}, \quad \{c_i, c_j\} = 0$$

The Fock space is built by applying these operators to a vacuum state $|0\rangle$.

For a Dirac operator $D$ on a manifold (or spectral triple), the one-particle states are the eigenstates of $D$. A many-body state is a Slater determinant:

$$|\psi\rangle = c_{i_1}^\dagger c_{i_2}^\dagger \cdots c_{i_N}^\dagger |0\rangle$$

The density matrix for this state is:

$$\rho = |\psi\rangle \langle \psi|$$

The von Neumann entropy is:

$$S = -\text{Tr}(\rho \log \rho)$$

For a filled Fermi sea (a standard thermal state), with Fermi energy $E_F$, the density matrix takes the form:

$$\rho = \frac{e^{-\beta(H - \mu N)}}{Z}$$

where $\beta = 1/T$ is the inverse temperature, $\mu$ is the chemical potential, $N$ is the number operator, and $Z$ is the partition function.

### Heat Kernel and Spectral Action

The key objects are the heat kernel and its trace:

$$K(t) = \text{Tr}(e^{-tD^2})$$

For large time $t \to \infty$, this decays exponentially. For small time $t \to 0$, it diverges, but the divergence is controlled by the Seeley-DeWitt coefficients:

$$K(t) \sim \sum_{n=0}^\infty a_n(D) t^{(n-d)/2}$$

The spectral action is defined by:

$$S[D] = \text{Tr}(f(D/\Lambda))$$

where $f$ is a rapidly decreasing test function. Using the Mellin transform, this can be written as:

$$S[D] = \int_0^\infty \frac{dt}{t} f(t) \text{Tr}(e^{-tD^2})$$

### Connection to Entropy

Now comes the crucial step. For a fermionic system at finite temperature $T = 1/\beta$, the von Neumann entropy can be computed from the spectral function:

$$S_{\text{vN}} = \int_0^\infty dE \, \rho(E) [f(E-\mu) \log f(E-\mu) + (1-f(E-\mu)) \log(1-f(E-\mu))]$$

where $f(E) = 1/(e^{\beta(E-\mu)} + 1)$ is the Fermi-Dirac distribution and $\rho(E)$ is the density of states.

In the limit $T \to 0$ (zero temperature) and for a specific choice of the test function in the spectral action:

$$f(x) = x_+ = \max(x, 0)$$

the von Neumann entropy becomes:

$$S_{\text{vN}} = \text{Tr}(e^{-\beta(D - \mu)^2 / \Lambda^2}) - \text{Tr}(\text{positive parts of } D)$$

For the standard model spectral triple, this is computed to be:

$$S_{\text{vN}} = S[D]$$

where $S[D]$ is the spectral action. The entropy of the quantum geometry is the spectral action!

### Heat Kernel Expansion and Riemann Zeta Function

The Seeley-DeWitt coefficients for the Dirac operator on a 4D manifold are:

$$a_0(D) = \frac{1}{(4\pi)^2} \int d^4x \sqrt{g} \, \text{tr}(1)$$

$$a_2(D) = \frac{1}{(4\pi)^2} \int d^4x \sqrt{g} \, \text{tr}(R_{ij} \sigma^{ij} + \ldots)$$

$$a_4(D) = \frac{1}{(4\pi)^2} \int d^4x \sqrt{g} \, \text{tr}(\text{(curvature)}^2 + \text{(gauge)}^2 + \ldots)$$

where the traces are taken over the spinor/representation space.

When computed for the standard model spectral triple, Chamseddine, Connes, and van Suijlekom find:

$$a_4(D) = \frac{1}{(4\pi)^2} \int d^4x \sqrt{g} \left[ c_1 R^2 + c_2 R_{\mu\nu} R^{\mu\nu} + \ldots \right]$$

where the coefficients $c_i$ are **rational multiples of zeta function values**:

$$c_1 \propto \zeta(5)$$
$$c_2 \propto \zeta(3)$$
$$\text{etc.}$$

This is unexpected: why should the geometry of the Standard Model be encoded in special values of the Riemann zeta function?

### Riemann Xi Function and Dimensional Duality

The Riemann xi function is:

$$\xi(s) = \frac{s(s-1)}{2} \pi^{-s/2} \Gamma(s/2) \zeta(s)$$

It satisfies the functional equation:

$$\xi(s) = \xi(1-s)$$

This duality relates $\zeta(s)$ to $\zeta(1-s)$ up to pole and zero contributions.

In the context of the spectral action, this functional equation translates to a duality between the short-time (high-energy, UV) expansion and the long-time (low-energy, IR) expansion of the heat kernel:

$$\sum_{n} a_{2n}(D) \Lambda^{d-2n} = \sum_n b_{2m}(D) \Lambda^{-m}$$

where the left side is the "positive dimensional" coefficients (energy-raising) and the right side is the "negative dimensional" coefficients (energy-lowering). The Riemann functional equation relates these two expansions.

This suggests that the spectral action encodes a **duality between the UV physics (high energies, small distances) and the IR physics (low energies, large distances)**. This is reminiscent of holographic duality or other quantum field theory dualities.

---

## Key Results

1. **Spectral Action is Entropy**: The von Neumann entropy of a fermionic system in second quantization is equal to the spectral action functional. This provides a profound information-theoretic interpretation: the spectral action measures the information content of the quantum geometry.

2. **Riemann Zeta Function in Particle Physics**: The heat kernel expansion of the Dirac operator on the standard model geometry naturally involves special values of the Riemann zeta function. This unexpected connection suggests deep ties between particle physics and number theory.

3. **Coefficient Identities**:
   - The coefficient $a_4(D)$ appearing in Einstein gravity (Gauss-Bonnet term) is proportional to $\zeta(5)$
   - The coefficient $a_2(D)$ in the Weyl-squared term is proportional to $\zeta(3)$
   - Higher coefficients involve $\zeta(7), \zeta(9), \ldots$

4. **UV/IR Duality via Functional Equation**: The Riemann functional equation induces a duality in the spectral action between high-energy and low-energy regimes. This suggests that the Standard Model at very high energies (UV) is dual to a certain structure at low energies (IR).

5. **Thermodynamic Interpretation**: The spectral action can be viewed as a partition function for the quantum geometry. The "temperature" $T = 1/\beta$ is the inverse scale at which the geometry is probed. At $T = 0$, the entropy saturates to the spectral action value.

6. **Universal Constants of Nature**: The appearance of $\zeta(3)$ and $\zeta(5)$ suggests that some fundamental physical constants (like gauge coupling ratios) may be related to these transcendental numbers.

---

## Impact and Legacy

This work is revolutionary for several reasons:

1. **Information Theory Unification**: It connects quantum information theory (entropy) with quantum field theory (spectral action) and gravity (Einstein action), showing they are aspects of a single geometric principle.

2. **Number Theory Connection**: The appearance of the Riemann zeta function in particle physics provides a tantalizing clue that the Standard Model may be related to some deep number-theoretic structure.

3. **Quantum Geometry Interpretation**: The identification of entropy with spectral action suggests that gravity and matter are fundamentally information-theoretic phenomena.

4. **Guidance for Beyond-Standard-Model Physics**: If additional physics (e.g., new particles, new symmetries) exists beyond the Standard Model, their spectral action should also involve zeta function values. This provides a testable criterion.

---

## Connection to Phonon-Exflation Framework

The entropy-spectral action connection is profound for phonon-exflation:

1. **Metric as Information**: The internal SU(3) metric can be viewed as encoding information about the quantum state. Phonon excitations modify the information content, changing the entropy.

2. **Thermodynamic Evolution**: The metric evolution in phonon-exflation can be interpreted as driven by entropy production. The system evolves toward states of higher entropy (or more efficiently, toward states minimizing free energy).

3. **Zeta Functions and Internal Geometry**: If the standard model spectral action involves $\zeta(3)$ and $\zeta(5)$, the internal SU(3) metric itself should involve analogous constants. This could provide predictions for specific metric deformation directions (phonon modes).

4. **Temperature and Scale**: In the phonon picture, the "temperature" conjugate to the metric scale is the phonon occupation number. Higher occupation corresponds to higher "temperature" and thus higher entropy of the internal geometry.

5. **Quantum Fluctuations**: The entropy formula naturally accounts for quantum fluctuations via the Fermi-Dirac distribution. This suggests phonons (quantum excitations of the metric) directly contribute to the entropy through their occupation numbers.

The paper elevates spectral geometry from a computational framework to a fundamental principle grounded in quantum information theory and number theory, making it the conceptual foundation for understanding how internal metric excitations (phonons) generate observable physics.

---

## References

- Chamseddine, A. H., Connes, A., & van Suijlekom, W. D. (2019). "Entropy and the Spectral Action." *Communications in Mathematical Physics*, 364(3), 835-866. arXiv:1809.02944 [hep-th] (2018).
- Riemann, B. (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Grösse." *Monatsberichte der Preußischen Akademie der Wissenschaften*, 671-680.
- Seeley, R. T. (1967). "Complex Powers of an Elliptic Operator." *Singular Integrals (Proceedings of Symposia in Pure Mathematics)*, 10, 288-307.
- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer.
