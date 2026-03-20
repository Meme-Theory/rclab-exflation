# Space-Time Approach to Non-Relativistic Quantum Mechanics

**Author:** Richard P. Feynman
**Year:** 1948
**Journal:** *Reviews of Modern Physics*, 20(2), 367--387

---

## Abstract

Feynman presents a reformulation of non-relativistic quantum mechanics in which the probability amplitude for a particle to travel from point $a$ to point $b$ is computed by summing over all possible spacetime trajectories connecting those points, each weighted by a phase factor $e^{iS/\hbar}$ where $S$ is the classical action along that path. This "sum over histories" formulation is shown to be mathematically equivalent to the Schrodinger equation but provides a fundamentally different physical picture: rather than a wave function evolving deterministically under a Hamiltonian, quantum mechanics emerges from a democratic superposition of classical paths. The formulation naturally explains the classical limit through stationary phase arguments and provides the conceptual foundation for Feynman's subsequent work on quantum electrodynamics, quantum field theory, and statistical mechanics.

---

## Historical Context

By the mid-1940s, quantum mechanics had been firmly established for two decades through two equivalent mathematical frameworks: Heisenberg's matrix mechanics (1925) and Schrodinger's wave mechanics (1926), unified by Dirac's transformation theory (1927). Both frameworks relied on operators acting on state vectors in Hilbert space, with time evolution governed by the Hamiltonian. While powerful, this operator formalism obscured the connection between quantum and classical mechanics, requiring Ehrenfest's theorem or WKB approximations to recover classical behavior.

Feynman's path integral approach has its intellectual roots in several earlier developments. Dirac had noted in a 1933 paper ("The Lagrangian in Quantum Mechanics") that the quantum mechanical transformation function between states at different times was "analogous to" $e^{iL\delta t/\hbar}$, where $L$ is the classical Lagrangian. Dirac, however, did not pursue the idea to its mathematical conclusion. The relationship between Dirac's remark and a usable formulation was, by Feynman's own account, pointed out to him by Herbert Jehle during a visit to Princeton.

Feynman's doctoral thesis (1942, supervised by John Archibald Wheeler) had already explored these ideas in the context of classical electrodynamics with the Wheeler-Feynman absorber theory. The thesis developed the "principle of least action" approach to quantum mechanics, but its wartime completion and delayed publication meant the 1948 Reviews of Modern Physics paper served as the definitive public statement.

The timing was significant. Quantum electrodynamics was in crisis: perturbation calculations produced infinite answers for basic quantities like the electron self-energy and the Lamb shift. The path integral approach would prove essential for Feynman's resolution of these infinities, providing an intuitive framework for his diagrams and regularization procedures. Schwinger and Tomonaga were simultaneously developing operator-based approaches to the same problems, but Feynman's spacetime picture offered unique computational and conceptual advantages.

---

## Key Arguments and Derivations

### 1. The Kernel (Propagator) $K(b,a)$

Feynman begins by defining the central object of the theory: the kernel or propagator $K(\mathbf{x}_b, t_b; \mathbf{x}_a, t_a)$, which gives the probability amplitude for a particle at position $\mathbf{x}_a$ at time $t_a$ to be found at position $\mathbf{x}_b$ at time $t_b$. The wave function at time $t_b$ is obtained from an earlier wave function via:

$$\psi(\mathbf{x}_b, t_b) = \int K(\mathbf{x}_b, t_b; \mathbf{x}_a, t_a) \, \psi(\mathbf{x}_a, t_a) \, d^3\mathbf{x}_a$$

This is a completeness relation in disguise: $K$ encodes the full unitary time evolution of the system. In the operator formalism, $K(b,a) = \langle \mathbf{x}_b | e^{-iH(t_b - t_a)/\hbar} | \mathbf{x}_a \rangle$, but Feynman's goal is to construct $K$ without reference to operators.

### 2. Sum Over Histories

The central postulate is that the kernel is given by a sum over all possible paths connecting $(\mathbf{x}_a, t_a)$ to $(\mathbf{x}_b, t_b)$:

$$K(b,a) = \int_{\text{all paths}} e^{iS[\mathbf{x}(t)]/\hbar} \, \mathcal{D}[\mathbf{x}(t)]$$

where $S[\mathbf{x}(t)]$ is the classical action functional evaluated along path $\mathbf{x}(t)$:

$$S[\mathbf{x}(t)] = \int_{t_a}^{t_b} L(\mathbf{x}, \dot{\mathbf{x}}, t) \, dt$$

and $L = T - V$ is the classical Lagrangian. The symbol $\mathcal{D}[\mathbf{x}(t)]$ denotes integration over all paths, which Feynman defines through a limiting procedure.

### 3. Time-Slicing Definition of the Path Integral

To give the path integral mathematical meaning, Feynman divides the time interval $[t_a, t_b]$ into $N$ equal segments of width $\epsilon = (t_b - t_a)/N$, with intermediate times $t_j = t_a + j\epsilon$. At each intermediate time, the particle has a position $\mathbf{x}_j$. The path integral is defined as:

$$K(b,a) = \lim_{N \to \infty} A^{-N} \int \cdots \int \exp\left(\frac{i}{\hbar} \sum_{j=0}^{N-1} L\left(\frac{\mathbf{x}_{j+1} + \mathbf{x}_j}{2}, \frac{\mathbf{x}_{j+1} - \mathbf{x}_j}{\epsilon}, t_j\right) \epsilon \right) \prod_{j=1}^{N-1} d^3\mathbf{x}_j$$

where $A$ is a normalization constant. For a particle of mass $m$ in one dimension, $A = \sqrt{2\pi i \hbar \epsilon / m}$, determined by the requirement that $K$ satisfy the correct free-particle limit.

The discretized Lagrangian for a particle of mass $m$ in potential $V(\mathbf{x})$ is:

$$L_j = \frac{m}{2} \left(\frac{\mathbf{x}_{j+1} - \mathbf{x}_j}{\epsilon}\right)^2 - V\left(\frac{\mathbf{x}_{j+1} + \mathbf{x}_j}{2}\right)$$

### 4. Free Particle Propagator

For a free particle ($V = 0$) in one dimension, the action along a straight-line path is:

$$S_{\text{cl}} = \frac{m(x_b - x_a)^2}{2(t_b - t_a)}$$

The Gaussian integrations at each time slice can be performed exactly. The integral over $x_1$ gives:

$$\int_{-\infty}^{\infty} \exp\left(\frac{im}{2\hbar\epsilon}\left[(x_2 - x_1)^2 + (x_1 - x_a)^2\right]\right) dx_1 = \sqrt{\frac{i\pi\hbar(2\epsilon)}{m}} \exp\left(\frac{im(x_2 - x_a)^2}{2\hbar(2\epsilon)}\right)$$

Iterating this process through all $N-1$ integrations yields:

$$K_0(b,a) = \sqrt{\frac{m}{2\pi i \hbar (t_b - t_a)}} \exp\left(\frac{im(x_b - x_a)^2}{2\hbar(t_b - t_a)}\right)$$

This is exactly the position-space matrix element of the free-particle evolution operator, confirming the formalism's consistency.

### 5. Composition Property

A crucial feature is the composition (or semigroup) property:

$$K(c,a) = \int K(c,b) \, K(b,a) \, d^3\mathbf{x}_b$$

for any intermediate time $t_b$ with $t_a < t_b < t_c$. This follows directly from the path integral: summing over all paths from $a$ to $c$ can be decomposed into summing over all paths from $a$ to $b$ (at fixed intermediate position $\mathbf{x}_b$), then from $b$ to $c$, and finally integrating over $\mathbf{x}_b$. This property is the path-integral expression of the completeness of position eigenstates.

### 6. Equivalence to the Schrodinger Equation

Feynman demonstrates the equivalence by considering the propagator for an infinitesimal time step $\epsilon$. For the one-dimensional case with Lagrangian $L = \frac{1}{2}m\dot{x}^2 - V(x)$:

$$\psi(x, t + \epsilon) = \frac{1}{A} \int_{-\infty}^{\infty} \exp\left(\frac{im\eta^2}{2\hbar\epsilon} - \frac{i\epsilon}{\hbar}V(x + \eta/2)\right) \psi(x + \eta, t) \, d\eta$$

where $\eta = x' - x$ is the displacement variable. The key insight is that for small $\epsilon$, the rapidly oscillating phase $e^{im\eta^2/2\hbar\epsilon}$ restricts the dominant contributions to $\eta \sim \sqrt{\epsilon}$. Expanding $\psi(x + \eta, t)$ and $V(x + \eta/2)$ in Taylor series around $x$:

$$\psi(x + \eta, t) = \psi + \eta \frac{\partial \psi}{\partial x} + \frac{\eta^2}{2}\frac{\partial^2 \psi}{\partial x^2} + \cdots$$

and performing the Gaussian integrals (using $\langle \eta^2 \rangle = i\hbar\epsilon/m$), the left-hand side becomes $\psi + \epsilon \partial\psi/\partial t + \cdots$. Matching terms of order $\epsilon$:

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi$$

which is the time-dependent Schrodinger equation. The equivalence is exact and holds for arbitrary potentials $V(x)$.

### 7. The Classical Limit and Stationary Phase

The path integral provides perhaps the most transparent derivation of the classical limit. When $S \gg \hbar$ for the relevant paths, the phase $e^{iS/\hbar}$ oscillates rapidly. Contributions from neighboring paths with significantly different actions cancel by destructive interference. The dominant contribution comes from the path of stationary action, $\delta S = 0$, which is precisely the Euler-Lagrange equation:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = \frac{\partial L}{\partial x}$$

More precisely, the stationary phase approximation gives:

$$K(b,a) \approx \sum_{\text{cl. paths}} \sqrt{\frac{1}{2\pi i\hbar} \left|\frac{\partial^2 S_{\text{cl}}}{\partial x_b \partial x_a}\right|} \exp\left(\frac{i}{\hbar}S_{\text{cl}} - \frac{i\pi}{2}\nu\right)$$

where the sum is over all classical paths connecting $a$ to $b$, and $\nu$ is the Morse index (number of conjugate points along the path). The amplitude factor involves the Van Vleck determinant $|\partial^2 S_{\text{cl}}/\partial x_b \partial x_a|$, which measures how neighboring classical trajectories spread.

For the harmonic oscillator $V = \frac{1}{2}m\omega^2 x^2$, the classical action is:

$$S_{\text{cl}} = \frac{m\omega}{2\sin\omega T}\left[(x_a^2 + x_b^2)\cos\omega T - 2x_a x_b\right]$$

where $T = t_b - t_a$, and the exact propagator is:

$$K(b,a) = \sqrt{\frac{m\omega}{2\pi i\hbar \sin\omega T}} \exp\left(\frac{i}{\hbar}S_{\text{cl}}\right)$$

This is one of the rare cases where the stationary phase approximation is exact, because the action is quadratic in the path.

### 8. Paths of Importance

Feynman emphasizes that the paths dominating the integral are not smooth curves but rather highly irregular, non-differentiable trajectories. The typical path in the integral has the property that the mean-square displacement scales as:

$$\langle (\Delta x)^2 \rangle \sim \frac{\hbar}{m} \Delta t$$

This is the same scaling as Brownian motion (with $\hbar/m$ replacing $D$, the diffusion coefficient), establishing a deep connection between quantum mechanics and stochastic processes. The "typical" quantum path is continuous but nowhere differentiable -- a fractal of Hausdorff dimension 2. This connection was later formalized through the Feynman-Kac formula, which relates the path integral (after Wick rotation $t \to -i\tau$) to the Wiener integral over Brownian paths.

---

## Physical Interpretation

The path integral formulation offers a radically different ontological picture from the standard formalism:

1. **Democracy of paths:** Every conceivable trajectory contributes to the amplitude. There is no privileged "actual" path; the particle explores all of configuration space simultaneously. Classical motion emerges not because non-classical paths are forbidden, but because they cancel.

2. **Lagrangian primacy:** The standard formulation is built on the Hamiltonian $H$, which requires a canonical decomposition into coordinates and momenta. The path integral uses the Lagrangian $L$, which is manifestly Lorentz-invariant (for relativistic systems) and does not require canonical variables. This makes the path integral naturally suited to gauge theories and general relativity.

3. **No wave function collapse:** The path integral computes transition amplitudes directly, without needing to invoke measurement postulates. The question "which path did the particle take?" is not answered because it is not asked -- only the endpoint information enters.

4. **Action as phase:** The identification of $S/\hbar$ as the quantum mechanical phase unifies the principle of least action with quantum interference. The Bohr-Sommerfeld quantization condition $\oint p \, dq = (n + 1/2)h$ appears naturally as a condition for constructive interference of paths.

---

## Impact and Legacy

### Immediate Impact

The path integral formulation was initially regarded with skepticism by much of the physics community. It lacked mathematical rigor (the measure $\mathcal{D}[\mathbf{x}(t)]$ is not well-defined in the Lebesgue sense for oscillatory integrals), and many physicists found it unnecessarily exotic when the Schrodinger equation worked perfectly well. However, its power became evident through Feynman's subsequent QED papers, where the path integral provided the natural language for his diagrammatic perturbation theory.

### Quantum Field Theory

The path integral generalization to fields replaces the sum over particle paths with a sum over field configurations:

$$Z = \int \mathcal{D}[\phi] \, e^{iS[\phi]/\hbar}$$

This functional integral formulation, developed fully by Feynman and later systematized by others, became the standard language of modern quantum field theory. It provides the most natural framework for:
- Deriving Feynman rules for any Lagrangian
- Understanding gauge symmetry and gauge fixing (Faddeev-Popov procedure)
- Non-perturbative methods (instantons, solitons)
- Lattice gauge theory (Wilson 1974)
- Topological quantum field theory

### Statistical Mechanics

The Wick rotation $t \to -i\tau$ transforms the path integral into a partition function:

$$Z = \int \mathcal{D}[\mathbf{x}(\tau)] \, e^{-S_E[\mathbf{x}(\tau)]/\hbar}$$

where $S_E$ is the Euclidean action. This establishes a deep correspondence between quantum mechanics in $d$ dimensions and statistical mechanics in $d+1$ dimensions, exploited extensively in condensed matter physics and lattice field theory.

### Mathematics

Despite (or because of) its lack of rigor, the path integral stimulated major mathematical developments:
- The Feynman-Kac formula gave rigorous meaning to the Euclidean path integral using Wiener measure
- The Atiyah-Singer index theorem can be derived via supersymmetric path integrals
- Topological invariants (Jones polynomial, Donaldson invariants) are computed as path integrals by Witten
- The theory of rough paths (Lyons) provides partial rigorous foundations

---

## Connections to Modern Physics

1. **Condensed matter:** The path integral is the natural language for the BCS theory of superconductivity (via Hubbard-Stratonovich transformation), superfluidity (coherent state path integrals), and the quantum Hall effect (Chern-Simons theory).

2. **String theory:** The Polyakov action for the string worldsheet is a two-dimensional path integral, and string amplitudes are computed as sums over worldsheet topologies -- a direct generalization of summing over particle paths.

3. **Quantum gravity:** The path integral over metrics, $Z = \int \mathcal{D}[g_{\mu\nu}] \, e^{iS_{\text{EH}}[g]/\hbar}$, remains the formal starting point for approaches to quantum gravity, including Euclidean quantum gravity, causal dynamical triangulations, and spin foams.

4. **Quantum computing:** The sum-over-histories picture provides the conceptual foundation for quantum algorithms, where quantum parallelism can be understood as simultaneous exploration of all computational paths.

5. **Phonon-exflation cosmology:** In frameworks where particles are phononic excitations of a higher-dimensional manifold, the path integral naturally extends to include sums over internal-space configurations, connecting the particle-physics Lagrangian to the underlying geometric structure through the spectral action $\text{Tr}(f(D/\Lambda))$.
