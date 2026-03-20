# Space-Time Approach to Quantum Electrodynamics

**Author:** Richard P. Feynman
**Year:** 1949
**Journal:** *Physical Review*, 76(6), 769--789

---

## Abstract

Feynman presents the complete diagrammatic framework for computing scattering amplitudes in quantum electrodynamics. Building on the propagator formalism of the "Theory of Positrons," he develops systematic graphical rules -- Feynman diagrams -- for translating physical processes into mathematical expressions. Each diagram element corresponds to a specific mathematical factor: electron propagators, photon propagators, and vertex factors. The paper demonstrates the method through detailed calculations of Compton scattering, Moller scattering, pair annihilation, and electron self-energy, showing that the diagrammatic approach reproduces known results while providing vastly more efficient computational methods. The regularization of divergent integrals is handled through a covariant cutoff procedure. The relationship between Feynman's spacetime methods and the operator-based approaches of Schwinger and Tomonaga is discussed, with Feynman arguing that while the results are equivalent, the spacetime approach offers greater intuitive clarity and computational economy.

---

## Historical Context

### The Crisis of Infinities

By the late 1930s, quantum electrodynamics faced a severe crisis. Perturbative calculations of basic physical quantities -- the electron self-energy, the vacuum polarization, and vertex corrections -- produced divergent (infinite) results. The electron's electromagnetic self-energy, for instance, diverged logarithmically:

$$\delta m \sim \frac{3\alpha}{2\pi} m \ln\left(\frac{\Lambda}{m}\right)$$

where $\Lambda$ is an ultraviolet cutoff. These infinities cast doubt on the entire framework of quantum field theory.

### The Lamb Shift and Anomalous Magnetic Moment

The experimental discoveries of 1947 forced the issue. Willis Lamb and Robert Retherford measured a small splitting between the $2S_{1/2}$ and $2P_{1/2}$ levels of hydrogen (the Lamb shift, about 1057 MHz), which should have been degenerate according to the Dirac equation. Simultaneously, Polykarp Kusch measured the electron's magnetic moment to be slightly larger than the Dirac prediction: $g = 2(1 + a_e)$ with $a_e \approx \alpha/2\pi \approx 0.00116$.

These precision measurements demanded a consistent method for extracting finite, physically meaningful predictions from QED despite the divergences. Hans Bethe's non-relativistic estimate of the Lamb shift (1947) showed that subtracting the self-energy shift in a sensible way gave the correct answer, but a fully relativistic, systematic procedure was needed.

### Three Approaches

By 1948-49, three groups had independently developed renormalization methods:

- **Tomonaga** (from 1943, published in English 1946-48): Extended Dirac's many-time formalism to a covariant theory with a spacelike surface $\sigma$.
- **Schwinger** (1948-49): Developed a systematic operator-based approach using the interaction representation, computing the anomalous magnetic moment ($a_e = \alpha/2\pi$) and Lamb shift with full covariance.
- **Feynman** (1948-49): Developed the spacetime diagrammatic approach presented in this paper.

Dyson's proof of equivalence (1949) showed these were different computational tools for the same underlying theory.

---

## Key Arguments and Derivations

### 1. The Feynman Rules

The central achievement of the paper is the codification of a set of rules for writing down the amplitude $M$ for any QED process to any order in perturbation theory. These rules, in modern notation, are:

**External lines:**
- Incoming electron: $u(p, s)$
- Outgoing electron: $\bar{u}(p', s')$
- Incoming positron: $\bar{v}(p, s)$
- Outgoing positron: $v(p', s')$
- Incoming photon: $\epsilon_\mu(k, \lambda)$
- Outgoing photon: $\epsilon_\mu^*(k, \lambda)$

**Internal lines (propagators):**
- Electron propagator (Feynman uses $K_+$ from the positrons paper):

$$\frac{i(\gamma^\mu p_\mu + m)}{p^2 - m^2 + i\epsilon} = \frac{i}{\not{p} - m + i\epsilon}$$

- Photon propagator:

$$\frac{-ig_{\mu\nu}}{q^2 + i\epsilon} \quad \text{(Feynman gauge)}$$

**Vertices:**
- Each electron-photon vertex contributes a factor $-ie\gamma^\mu$ and a momentum-conservation delta function $(2\pi)^4 \delta^{(4)}(p_1 - p_2 - k)$.

**Integration:**
- Each undetermined internal momentum (loop momentum) is integrated: $\int d^4k/(2\pi)^4$.

**Combinatorics:**
- A relative minus sign between diagrams that differ by the exchange of two external fermion lines.
- A factor of $(-1)$ for each closed fermion loop.

### 2. Compton Scattering

Feynman illustrates the method by computing Compton scattering ($e^- + \gamma \to e^- + \gamma$). There are two diagrams at tree level, differing in the time order of absorption and emission:

**Diagram (a):** The electron absorbs the incoming photon first, then emits the outgoing photon.

$$M_a = (-ie)^2 \bar{u}(p')\gamma^\nu \epsilon_\nu^*(k') \frac{i(\not{p} + \not{k} + m)}{(p+k)^2 - m^2} \gamma^\mu \epsilon_\mu(k) u(p)$$

**Diagram (b):** The electron emits the outgoing photon first, then absorbs the incoming photon.

$$M_b = (-ie)^2 \bar{u}(p')\gamma^\mu \epsilon_\mu(k) \frac{i(\not{p} - \not{k}' + m)}{(p-k')^2 - m^2} \gamma^\nu \epsilon_\nu^*(k') u(p)$$

The total amplitude is $M = M_a + M_b$. The cross section computed from $|M|^2$ reproduces the Klein-Nishina formula:

$$\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{2m^2}\left(\frac{\omega'}{\omega}\right)^2\left(\frac{\omega}{\omega'} + \frac{\omega'}{\omega} - \sin^2\theta\right)$$

where $\omega$ and $\omega'$ are the initial and final photon frequencies and $\theta$ is the scattering angle.

### 3. Moller Scattering (Electron-Electron)

For electron-electron scattering, the two diagrams correspond to the exchange of a virtual photon in the $t$-channel and $u$-channel (related by exchange of the two identical final-state electrons):

$$M = \frac{-ie^2}{(p_1 - p_1')^2}\left[\bar{u}(p_1')\gamma^\mu u(p_1)\right]\left[\bar{u}(p_2')\gamma_\mu u(p_2)\right] - (p_1' \leftrightarrow p_2')$$

The relative minus sign between the two terms reflects the antisymmetry of the two-fermion state under exchange, a consequence of the Pauli exclusion principle built into the formalism through the Fermi statistics rules.

### 4. Self-Energy and Divergences

The electron self-energy arises from a loop correction to the electron propagator: the electron emits and reabsorbs a virtual photon. The self-energy operator is:

$$-i\Sigma(p) = (-ie)^2 \int \frac{d^4k}{(2\pi)^4} \gamma^\mu \frac{i(\not{p} - \not{k} + m)}{(p-k)^2 - m^2 + i\epsilon} \gamma_\mu \frac{-i}{k^2 + i\epsilon}$$

Using the identity $\gamma^\mu(\not{p} - \not{k} + m)\gamma_\mu = -2(\not{p} - \not{k}) + 4m$ (in 4 dimensions), this becomes:

$$\Sigma(p) = \frac{e^2}{(2\pi)^4}\int d^4k \frac{-2(\not{p} - \not{k}) + 4m}{[(p-k)^2 - m^2][k^2]}$$

This integral is logarithmically divergent. Feynman introduces a covariant regularization by modifying the photon propagator:

$$\frac{1}{k^2} \to \frac{1}{k^2} - \frac{1}{k^2 - \Lambda^2}$$

which makes the integral finite but cutoff-dependent. The physical mass is then:

$$m_{\text{phys}} = m_0 + \delta m, \quad \delta m = \Sigma(m) = \frac{3\alpha}{2\pi}m\ln\frac{\Lambda}{m} + \text{finite}$$

The infinite part is absorbed into a redefinition of the bare mass $m_0$ (mass renormalization).

### 5. Vacuum Polarization

The photon propagator receives a loop correction from a virtual electron-positron pair (closed fermion loop):

$$i\Pi^{\mu\nu}(q) = (-1)(-ie)^2 \int \frac{d^4k}{(2\pi)^4} \text{Tr}\left[\gamma^\mu \frac{i(\not{k} + m)}{k^2 - m^2} \gamma^\nu \frac{i(\not{k} - \not{q} + m)}{(k-q)^2 - m^2}\right]$$

The factor of $(-1)$ is the closed-loop sign. Gauge invariance (the Ward identity) requires $q_\mu \Pi^{\mu\nu} = 0$, which constrains $\Pi^{\mu\nu}$ to be transverse:

$$\Pi^{\mu\nu}(q) = (q^2 g^{\mu\nu} - q^\mu q^\nu)\Pi(q^2)$$

The scalar function $\Pi(q^2)$ is logarithmically divergent, but its physical effect is the running of the electric charge:

$$e^2_{\text{eff}}(q^2) = \frac{e^2}{1 - \Pi(q^2)} \approx e^2\left(1 + \frac{\alpha}{3\pi}\ln\frac{q^2}{m^2}\right)$$

for $|q^2| \gg m^2$. This is the charge screening effect: the effective coupling increases at short distances (high $q^2$).

### 6. The Vertex Correction and Anomalous Magnetic Moment

The vertex correction modifies the electron-photon coupling:

$$\Gamma^\mu(p', p) = \gamma^\mu + \Lambda^\mu(p', p)$$

where the one-loop correction is:

$$\Lambda^\mu(p', p) = (-ie)^2 \int \frac{d^4k}{(2\pi)^4} \gamma^\alpha \frac{i(\not{p}' - \not{k} + m)}{(p'-k)^2 - m^2} \gamma^\mu \frac{i(\not{p} - \not{k} + m)}{(p-k)^2 - m^2} \gamma_\alpha \frac{-i}{k^2}$$

Using the Gordon decomposition, the on-shell vertex can be written:

$$\bar{u}(p')\Gamma^\mu u(p) = \bar{u}(p')\left[F_1(q^2)\gamma^\mu + \frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2)\right]u(p)$$

where $q = p' - p$, $F_1$ is the charge form factor (divergent, renormalized to $F_1(0) = 1$), and $F_2$ is the anomalous magnetic moment form factor. Feynman computes:

$$F_2(0) = \frac{\alpha}{2\pi}$$

giving the anomalous magnetic moment $a_e = \alpha/(2\pi) \approx 0.00116$, in agreement with Schwinger's earlier result and Kusch's measurement.

### 7. The Ward Identity

Feynman discusses the relationship between the vertex correction and the self-energy, which is encapsulated in the Ward identity:

$$\frac{\partial \Sigma(p)}{\partial p^\mu} = \Lambda^\mu(p, p)$$

This identity ensures that the charge renormalization from the vertex correction exactly cancels the wave-function renormalization from the self-energy, so that the physical charge is renormalized only by vacuum polarization. It is a consequence of gauge invariance and is essential for the consistency of the renormalization program.

---

## Physical Interpretation

### Diagrams as Spacetime Processes

Each Feynman diagram represents a class of spacetime processes: the particle worldlines trace out all possible paths, with each path weighted by the appropriate amplitude. The sum over all diagrams at a given order gives the total amplitude for the process. The diagrams are not mere calculational devices -- they represent the physical processes occurring in the quantum vacuum.

### Virtual Particles

The internal lines in Feynman diagrams correspond to "virtual" particles that do not satisfy the mass-shell condition $p^2 = m^2$. Virtual particles can be off-shell by any amount, with the propagator $1/(p^2 - m^2)$ suppressing contributions from far-off-shell states. Virtual particles exist only within the context of a complete diagram; they are not observable individually.

### Renormalization as Physical Screening

The infinities encountered in loop calculations are interpreted as artifacts of treating the electron as a bare point charge. The physical (observed) mass and charge differ from the bare values due to the cloud of virtual particles surrounding the electron. Renormalization absorbs the infinite bare-to-physical corrections into redefined parameters, leaving finite predictions for all physical observables.

### Feynman vs. Schwinger: Complementary Pictures

Feynman's approach works in momentum space with explicit diagrams; Schwinger's works in the operator formalism with proper-time parametrizations. Feynman's method is more intuitive for individual diagrams and for understanding the physics of specific processes. Schwinger's method is more powerful for deriving general results (like the Ward identity) and for systematic all-orders arguments. In practice, the modern approach uses both.

---

## Impact and Legacy

### Revolution in Computational Methods

The Feynman diagram technique transformed theoretical physics. Before Feynman, computing a cross section at second order in QED required pages of algebra with creation and annihilation operators, tracking all possible time orderings. Feynman diagrams reduce this to drawing pictures and applying simple rules. Schwinger reportedly quipped that Feynman had brought quantum field theory calculations to the masses.

### Extension to All Quantum Field Theories

The diagrammatic approach extends immediately to any quantum field theory: one simply modifies the propagators, vertices, and symmetry factors according to the Lagrangian. Feynman rules have been derived for:
- Scalar field theories ($\phi^4$, Yukawa)
- Non-Abelian gauge theories (QCD, electroweak theory) -- with the addition of ghost propagators
- General relativity (graviton propagator and vertices)
- Effective field theories of all kinds

### Precision Tests of QED

Feynman's methods enabled the computation of QED predictions to extraordinary precision. The anomalous magnetic moment has been computed to fifth order in $\alpha$ (tenth order in perturbation theory, involving 12672 Feynman diagrams), giving:

$$a_e^{\text{theory}} = 0.001\,159\,652\,182\,032(720)$$

in agreement with experiment to better than one part in $10^{12}$, making QED the most precisely tested theory in all of science.

### S-Matrix Program

The diagrammatic approach influenced the S-matrix program of the 1960s, where the emphasis on scattering amplitudes and analyticity properties led to Regge theory, bootstrap methods, and ultimately to string theory.

---

## Connections to Modern Physics

1. **QCD and asymptotic freedom:** The vacuum polarization calculation, when extended to non-Abelian gauge theories, reverses sign due to gluon self-interactions, leading to anti-screening and asymptotic freedom -- the decrease of the strong coupling at short distances.

2. **Electroweak theory:** The Feynman rules for the Standard Model include $W^\pm$, $Z^0$, and Higgs propagators, with vertices determined by the $SU(2)_L \times U(1)_Y$ gauge structure. Precision electroweak measurements at LEP and the LHC use multi-loop Feynman diagram calculations.

3. **Modern amplitude methods:** While Feynman diagrams remain foundational, modern methods (color-kinematics duality, on-shell recursion, amplituhedron) have revealed deep structure in scattering amplitudes that is obscured by the diagram-by-diagram approach. These methods can compute amplitudes that would require millions of Feynman diagrams.

4. **Lattice field theory:** The perturbative expansion in Feynman diagrams complements non-perturbative lattice calculations. The two approaches must agree in the weak-coupling regime, providing consistency checks.

5. **Effective field theory:** Feynman's regularization with a cutoff $\Lambda$ foreshadows the modern Wilsonian perspective, where the cutoff has physical meaning as the scale below which the theory is valid. The renormalization group evolution of couplings is computed from the same loop diagrams Feynman introduced.
