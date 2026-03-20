# Mathematical Formulation of the Quantum Theory of Electromagnetic Interaction

**Author:** Richard P. Feynman
**Year:** 1950
**Journal:** *Physical Review*, 80(3), 440--457

---

## Abstract

Feynman provides a systematic and self-contained derivation of the rules for quantum electrodynamics starting from the path integral over particle trajectories, including a rigorous treatment of spin through the Dirac equation, the coupling to the electromagnetic field, and the complete renormalization procedure. The paper derives the Feynman rules from first principles rather than stating them as recipes, establishes the equivalence with canonical quantization, and presents the calculation of the anomalous magnetic moment of the electron and the Lamb shift as applications. A key technical contribution is the development of parametric integral representations for loop integrals, including what are now called Feynman parameters, which enable the systematic evaluation of divergent integrals in a Lorentz-covariant manner.

---

## Historical Context

The two preceding Feynman papers -- "Theory of Positrons" and "Space-Time Approach to Quantum Electrodynamics" -- had presented the physical ideas and computational rules for QED but had not derived them from a systematic theoretical foundation. The rules were presented as prescriptions, justified by their agreement with known results and by heuristic arguments from the path integral. This left open the question of whether the rules were merely convenient recipes or consequences of a complete theory.

This paper closes that gap. Feynman starts from the path integral for a charged particle coupled to the electromagnetic field and systematically derives all the Feynman rules, including the treatment of spin, the photon propagator, and the renormalization of mass, charge, and wave function. The paper also serves as a technical manual, introducing the computational tricks (Feynman parametrization, Wick rotation, dimensional counting of divergences) that remain standard tools.

The paper was written partly in response to criticism that Feynman's methods, while producing correct answers, lacked a rigorous foundation. Schwinger's approach, by contrast, was derived from standard canonical quantization principles, even if the calculations were far more laborious. Feynman needed to show that his path integral approach was not just a set of tricks but a principled theoretical framework.

---

## Key Arguments and Derivations

### 1. Path Integral for a Scalar Charged Particle

Feynman begins with the simplest case: a spinless charged particle coupled to the electromagnetic field $A_\mu$. The transition amplitude from spacetime point $a$ to point $b$ is:

$$K(b,a) = \int \mathcal{D}[\mathbf{x}(s)] \exp\left(\frac{i}{\hbar}\int_a^b \left[\frac{m}{2}\dot{x}^\mu \dot{x}_\mu + e\dot{x}^\mu A_\mu(x)\right] ds\right)$$

where $s$ is a proper-time parameter along the worldline. The interaction term $e\dot{x}^\mu A_\mu$ is precisely the minimal coupling of classical electrodynamics, now integrated over all possible worldlines.

Expanding the exponential of the interaction to order $e^n$ gives the perturbation series:

$$K = K^{(0)} + eK^{(1)} + e^2 K^{(2)} + \cdots$$

where $K^{(0)}$ is the free propagator and each higher order involves additional insertions of $A_\mu$ along the worldline.

### 2. Incorporation of Spin: The Dirac Case

For a spin-1/2 particle, Feynman uses a proper-time representation of the Dirac propagator. The Feynman propagator can be written:

$$S_F(p) = \frac{\not{p} + m}{p^2 - m^2 + i\epsilon} = (\not{p} + m)\int_0^\infty ds \, e^{-is(p^2 - m^2 + i\epsilon)}$$

This proper-time representation allows the Dirac propagator to be treated similarly to the scalar case, with the Dirac matrices appearing as ordering factors at the vertices. The path integral for the Dirac particle is over worldlines in spacetime, with an additional factor of a path-ordered exponential of the spin connection:

$$\mathcal{P}\exp\left(-\frac{ie}{4}\int \sigma^{\mu\nu}F_{\mu\nu} \, ds\right)$$

where $\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu, \gamma^\nu]$ and $F_{\mu\nu}$ is the electromagnetic field tensor. This is the Pauli coupling, which reduces to the Dirac equation in the appropriate limit.

### 3. Quantization of the Electromagnetic Field

The electromagnetic field is treated as a collection of harmonic oscillators (one for each mode). Feynman integrates out the field, performing the path integral over $A_\mu$ exactly. This produces an effective action for the charged particles that includes a non-local interaction:

$$S_{\text{eff}} = S_{\text{particle}} + \frac{e^2}{2}\int\int J^\mu(x) D_F(x - x') J_\mu(x') \, d^4x \, d^4x'$$

where $J^\mu$ is the current density and $D_F$ is the Feynman propagator for the photon:

$$D_F(x - x') = \int \frac{d^4q}{(2\pi)^4} \frac{-i}{q^2 + i\epsilon} e^{-iq\cdot(x - x')}$$

This step is crucial: by integrating out the photon field, the interaction between charged particles becomes a direct (but retarded/advanced) coupling, mediated by $D_F$. This is the mathematical expression of virtual photon exchange.

### 4. Feynman Parametrization

For the evaluation of loop integrals, Feynman introduces the parametric identity that bears his name. For two propagator denominators:

$$\frac{1}{AB} = \int_0^1 \frac{dx}{[Ax + B(1-x)]^2}$$

and more generally, for $n$ denominators:

$$\frac{1}{A_1 A_2 \cdots A_n} = (n-1)! \int_0^1 \cdots \int_0^1 \frac{\delta(1 - \sum x_i) \prod dx_i}{[\sum x_i A_i]^n}$$

This identity allows multiple propagator denominators to be combined into a single denominator, after which the loop momentum integral becomes a standard Gaussian. For example, the one-loop self-energy integral:

$$\int \frac{d^4k}{(2\pi)^4} \frac{N(k)}{(k^2 - m^2)((p-k)^2 - m^2)}$$

becomes, after Feynman parametrization with $k \to k + xp$ (shifting the integration variable):

$$\int_0^1 dx \int \frac{d^4k}{(2\pi)^4} \frac{N(k + xp)}{[k^2 - \Delta]^2}$$

where $\Delta = m^2 - x(1-x)p^2 - i\epsilon$. The $k$ integral is now symmetric in $k$ and can be evaluated by Wick rotation $k^0 \to ik^0_E$, converting to a Euclidean integral:

$$\int \frac{d^4k_E}{(2\pi)^4} \frac{1}{(k_E^2 + \Delta)^2} = \frac{1}{16\pi^2}\frac{1}{\Delta} \cdot \frac{1}{0!} = \frac{i}{16\pi^2\Delta}$$

### 5. Systematic Renormalization

Feynman presents the renormalization procedure as a systematic algorithm:

**Step 1: Regularize.** Replace the photon propagator with a regularized version:

$$\frac{1}{k^2} \to \int_0^\infty \frac{C(\Lambda^2)}{(k^2 - \Lambda^2)} d\Lambda^2$$

where $C(\Lambda^2)$ is a weight function that falls off rapidly for $\Lambda^2 \gg \Lambda_{\text{max}}^2$, making all integrals finite.

**Step 2: Compute.** Evaluate all loop integrals using Feynman parametrization and Wick rotation.

**Step 3: Identify divergences.** As $\Lambda_{\text{max}} \to \infty$, certain terms diverge. These are classified by their Lorentz structure:
- Self-energy: $\Sigma(p) = A + B(\not{p} - m) + \Sigma_{\text{finite}}(p)$, where $A$ diverges linearly and $B$ diverges logarithmically.
- Vacuum polarization: $\Pi_{\mu\nu}(q) = (g_{\mu\nu}q^2 - q_\mu q_\nu)\Pi(q^2)$, where $\Pi(0)$ diverges logarithmically.
- Vertex correction: $\Lambda^\mu(p',p) = L\gamma^\mu + \Lambda^\mu_{\text{finite}}$, where $L$ diverges logarithmically.

**Step 4: Renormalize.** Absorb the divergences into redefinitions of the bare parameters:

$$m_0 = m_{\text{phys}} - \delta m, \quad e_0 = Z_3^{1/2} e_{\text{phys}}, \quad \psi_0 = Z_2^{1/2}\psi_{\text{phys}}$$

where $\delta m = A$, $Z_2 = 1 + B$, $Z_3 = 1/(1 - \Pi(0))$. The Ward identity ensures $Z_1 = Z_2$ (the vertex and wave-function renormalization constants are equal), so only two independent renormalization constants are needed: $\delta m$ and $Z_3$ (or equivalently, the renormalized mass and charge).

**Step 5: Remove regulator.** The renormalized amplitudes have finite limits as $\Lambda_{\text{max}} \to \infty$. All dependence on the cutoff is absorbed into the bare parameters.

### 6. Anomalous Magnetic Moment Calculation

Feynman presents the complete one-loop calculation. The vertex correction gives:

$$\bar{u}(p')\Lambda^\mu(p',p)u(p) = \bar{u}(p')\left[\gamma^\mu F_1^{(1)}(q^2) + \frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2^{(1)}(q^2)\right]u(p)$$

Using Feynman parametrization with three denominators (two electron propagators and one photon propagator), the calculation proceeds through several steps. After combining denominators, shifting the loop momentum, and performing the $d^4k$ integral:

$$F_2^{(1)}(0) = \frac{\alpha}{2\pi}\int_0^1 dx \int_0^{1-x} dy \, \frac{2m^2(1-x)(1-y) - 2m^2 xy}{m^2[(1-x)(1-y) + xy]^2/(1-x-y)}$$

Evaluating this (after considerable algebra involving the parametric integrals):

$$F_2^{(1)}(0) = \frac{\alpha}{2\pi}$$

The electron's anomalous magnetic moment is therefore:

$$a_e = \frac{g-2}{2} = \frac{\alpha}{2\pi} + O(\alpha^2)$$

giving $a_e \approx 0.001\,161\,4$, in agreement with the experimental value.

### 7. The Lamb Shift

The Lamb shift arises from three contributions:
1. **Electron self-energy:** The dominant contribution. The mass renormalization removes the divergence, leaving a finite, state-dependent shift proportional to $|\psi(0)|^2$ (the wave function at the nucleus).
2. **Vacuum polarization (Uehling potential):** A smaller correction of opposite sign, arising from the modification of the Coulomb potential at short distances due to virtual pairs.
3. **Vertex correction:** Contributes to the anomalous magnetic moment coupling.

The combined result for hydrogen is:

$$\Delta E(2S_{1/2} - 2P_{1/2}) = \frac{4\alpha^5 m}{3\pi}\left[\ln\frac{m}{2\langle E \rangle} + \frac{19}{30} - \frac{1}{5} + \frac{3}{8}\right] \approx 1052 \text{ MHz}$$

where $\langle E \rangle$ is a mean excitation energy determined numerically. The additional contribution from the anomalous magnetic moment and higher-order corrections brings the theoretical value to approximately 1057 MHz, in agreement with Lamb and Retherford's measurement.

---

## Physical Interpretation

### Renormalization as Physical Dressing

The renormalization procedure has a clear physical interpretation: the bare electron (a mathematical abstraction with mass $m_0$ and charge $e_0$) is surrounded by a cloud of virtual photons and virtual electron-positron pairs. The observed (physical) mass $m$ and charge $e$ are the values measured at macroscopic distances, which include the effects of this virtual cloud. The "infinities" arise from treating the bare particle as a point charge; they are analogous to the classical divergence of the electrostatic self-energy of a point charge, $U = e^2/(4\pi\epsilon_0 r) \to \infty$ as $r \to 0$.

### Universality of the Procedure

Feynman emphasizes that the renormalization procedure works to all orders in perturbation theory: at each order, the divergences are of the same form (mass, charge, and wave-function renormalization) and can be absorbed into the same redefined parameters. This was later proved rigorously by Dyson (to all orders in perturbation theory) and by Bogoliubov, Parasiuk, Hepp, and Zimmermann (the BPHZ theorem, for arbitrary overlapping divergences).

### The Proper-Time Method

Feynman's use of the proper-time parameter $s$ to represent propagators as:

$$\frac{1}{p^2 - m^2 + i\epsilon} = -i\int_0^\infty ds \, e^{is(p^2 - m^2 + i\epsilon)}$$

provides a worldline representation of loop integrals that has deep connections to:
- Schwinger's proper-time formalism
- The heat kernel expansion in mathematics
- String theory (where the proper time becomes the modular parameter of the worldsheet)
- The worldline formalism of Bern and Kosower (1990s)

---

## Impact and Legacy

### Computational Standard

The Feynman parametrization technique and the systematic renormalization procedure established in this paper became the standard computational toolkit for quantum field theory. Every graduate textbook on QFT (Peskin and Schroeder, Weinberg, Srednicki, Schwartz) follows essentially the same approach.

### Higher-Order Calculations

The systematic nature of Feynman's procedure enabled progressively more precise calculations. The anomalous magnetic moment has been pushed to:
- $O(\alpha^2)$: Petermann and Sommerfield (1957)
- $O(\alpha^3)$: Laporta and Remiddi (1996)
- $O(\alpha^4)$: Kinoshita and collaborators (2007)
- $O(\alpha^5)$: Aoyama, Kinoshita, and Nio (2012, numerical; 12672 diagrams)

### Power Counting and Renormalizability

Feynman's classification of divergences by their Lorentz structure and degree of divergence laid the groundwork for the concept of renormalizability. A theory is renormalizable if only finitely many types of divergences appear (mass, charge, and wave-function renormalization for QED). Non-renormalizable theories (like quantum gravity) require infinitely many new counterterms at each order.

### Dimensional Regularization

While Feynman used covariant cutoff regularization, the modern standard is dimensional regularization ('t Hooft and Veltman, 1972), which regulates integrals by continuing to $d = 4 - 2\epsilon$ dimensions. The Feynman parametrization step remains identical; only the final $d^dk$ integration is modified.

---

## Connections to Modern Physics

1. **Precision tests:** The anomalous magnetic moment of the muon, $a_\mu$, has been measured at Fermilab (2021-) and shows a persistent tension with the Standard Model prediction at the 4-5 sigma level. The theoretical calculation uses the same Feynman diagram techniques, extended to include electroweak and hadronic contributions.

2. **Effective field theories:** Feynman's renormalization procedure generalizes to effective field theories (Weinberg 1979), where non-renormalizable interactions are included but organized by a power-counting hierarchy. This is the modern understanding of the Standard Model itself -- as an effective theory valid below some cutoff.

3. **Asymptotic safety:** The question of whether gravity is non-perturbatively renormalizable (Weinberg's "asymptotic safety" conjecture) requires understanding the structure of gravitational Feynman diagrams at all loop orders, extending the power-counting analysis of this paper to the gravitational case.

4. **Worldline formalism:** The proper-time/worldline approach has been revived as the "worldline formalism" for efficient multi-loop calculations, particularly in QCD and gravity. The one-loop effective action can be written as a quantum-mechanical path integral over a particle worldline, directly extending Feynman's approach.
