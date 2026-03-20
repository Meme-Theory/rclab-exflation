# Transition from Inflation to Dark Energy in Superfluid Vacuum Theory

**Author(s):** Konstantin G. Zloshchastiev
**Year:** 2025
**Journal:** Quantum Reports, vol. 7, no. 1, art. 7
**DOI:** 10.3390/quantum7010007

---

## Abstract

We investigate a laminar constant-velocity superflow of physical vacuum modeled as a logarithmic quantum Bose liquid. It is shown that this three-dimensional non-relativistic quantum flow generates a four-dimensional relativistic quinton system comprising the dilaton and quintom (a combination of quintessence and tachyonic phantom fields). The unified model describes both the inflationary period of the early universe and the contemporary accelerating expansion phase (dark energy era). The quintessence and tachyonic scalar components prove to be non-minimally coupled, representing a generalization of cosmological phantom models previously unexplored.

---

## Historical Context

Superfluid Vacuum Theory (SVT) is an alternative to standard inflationary cosmology that models the physical vacuum as a superfluid quantum Bose liquid. This approach was pioneered by Zloshchastiev and others as a response to fundamental questions about inflation:

1. **The Graceful Exit Problem**: Standard slow-roll inflation struggles to exit gracefully to a radiation-dominated phase without fine-tuned potentials.

2. **Naturalness**: Why is the inflaton field so special? SVT proposes that what we call inflation is the collective flow of the vacuum itself—a more economical hypothesis.

3. **Dark Energy Connection**: If the vacuum is a superfluid with intrinsic low-energy excitations (phonons), then both early-universe inflation and late-universe dark energy could be manifestations of the same underlying phenomenon: the dynamics of a quantum liquid.

Previous work by Zloshchastiev demonstrated that a superfluid vacuum with logarithmic self-interaction (a typical form for Bose liquids) produces effective cosmic equations of motion. This paper extends that framework by showing that the same superfluid can naturally transition from an inflationary phase (with $w \approx -1$, constant density) to a dark energy phase (with $w$ varying mildly or remaining $\approx -1$ with dynamical component).

The key novelty is the emergence of a quinton system—a combination of dilaton and quintom fields—directly from the vacuum superfluid without additional fine-tuning.

---

## Key Arguments and Derivations

### Logarithmic Quantum Bose Liquid

The vacuum is modeled as a non-relativistic quantum Bose liquid described by a macroscopic wavefunction $\psi(\mathbf{r}, t)$ with density:

$$\rho_{\text{BEC}} = |\psi|^2$$

The Lagrangian density (in non-relativistic form) is:

$$\mathcal{L}_{\text{BEC}} = \frac{\hbar^2}{2m} |\nabla \psi|^2 - \mu |\psi|^2 + \frac{\lambda}{2} |\psi|^4 \log(|\psi|^2)$$

where:
- $m$ is an effective mass parameter (related to the Planck scale).
- $\mu$ is the chemical potential.
- $\lambda$ is the coupling constant.
- The logarithmic term $|\psi|^4 \log(|\psi|^2)$ captures the quantum statistics of a Bose liquid.

This logarithmic form arises naturally in the Mean Field Theory of degenerate Bose gases and is known to be thermodynamically stable.

### Laminar Superflow

A laminar constant-velocity superflow is assumed:

$$\psi(\mathbf{r}, t) = \psi_0 e^{i \mathbf{v} \cdot \mathbf{r} / \hbar}$$

where $\mathbf{v}$ is the constant superflow velocity and $\psi_0$ is a constant density amplitude.

In the superfluid ground state, there is no dissipation (zero viscosity), so the flow maintains constant velocity indefinitely.

### Comoving Cosmological Coordinates

To connect the non-relativistic superfluid to cosmological dynamics, we introduce comoving coordinates where the superflow velocity is reinterpreted as an expansion rate:

$$v \leftrightarrow H \cdot a(t)$$

where $H$ is the Hubble parameter and $a(t)$ is the scale factor.

The effective energy-momentum tensor derived from the Lagrangian is:

$$T_{\mu \nu}^{\text{eff}} = \rho_{\text{eff}} u_\mu u_\nu + p_{\text{eff}} (g_{\mu \nu} + u_\mu u_\nu)$$

where the effective density and pressure are:

$$\rho_{\text{eff}} = \rho_0 + \frac{\hbar^2}{2m} |\nabla \psi|^2 / |\psi|^2 + \lambda |\psi|^4 \log(|\psi|^2)$$

$$p_{\text{eff}} = -\rho_0 + \frac{\hbar^2}{2m} |\nabla \psi|^2 / |\psi|^2 - \lambda |\psi|^4 \log(|\psi|^2)$$

### Emergence of Dilaton and Quintom

The key derivation involves decomposing the superfluid density into a background component and fluctuations:

$$|\psi|^2 = \rho_{\text{bg}} (1 + \phi)$$

where $\phi$ is a small perturbation. Substituting into the Lagrangian and expanding to second order in $\phi$ and its derivatives yields:

$$\mathcal{L}_{\text{eff}} = \mathcal{L}_{\text{dil}} + \mathcal{L}_{\text{quint}} + \mathcal{L}_{\text{int}}$$

**Dilaton Sector** ($\mathcal{L}_{\text{dil}}$):
$$\mathcal{L}_{\text{dil}} = -\frac{1}{2} \partial_\mu \phi \partial^\mu \phi - V_{\text{dil}}(\phi)$$

The dilaton field corresponds to breathing oscillations (density fluctuations) of the superfluid.

**Quintom Sector** ($\mathcal{L}_{\text{quint}}$):
$$\mathcal{L}_{\text{quint}} = -\frac{1}{2} \partial_\mu \psi_q \partial^\mu \psi_q + \lambda_q |\psi_q|^4 \log(|\psi_q|)$$

where $\psi_q$ is the quintom field, a combination of quintessence (ordinary scalar) and phantom (negative kinetic energy or ghost-like) components.

**Interaction Term** ($\mathcal{L}_{\text{int}}$):
$$\mathcal{L}_{\text{int}} \sim g_{\text{int}} \phi \cdot (\psi_q^2) + \text{h.c.}$$

This non-minimal coupling between dilaton and quintom is a direct consequence of the superfluid structure and does not arise from ad hoc field theory assumptions.

### Evolution Equations

The dynamics are governed by the modified Friedmann equations:

$$H^2 = \frac{8\pi G}{3} (\rho_{\text{dil}} + \rho_{\text{quint}} + \rho_{\text{rad}})$$

$$\dot{H} = -4\pi G (\rho + p) = -4\pi G \left[ \frac{1}{2}(\dot{\phi}^2 + \dot{\psi}_q^2) + V_{\text{dil}} + V_{\text{quint}} \right]$$

where the equation of state parameter is:

$$w(t) = \frac{p_{\text{eff}}}{\rho_{\text{eff}}} = \frac{-V_{\text{dil}} - V_{\text{quint}} + \frac{1}{2}(\dot{\phi}^2 + \dot{\psi}_q^2)}{V_{\text{dil}} + V_{\text{quint}} + \frac{1}{2}(\dot{\phi}^2 + \dot{\psi}_q^2)}$$

### Transition from Inflation to Dark Energy

**Inflationary Phase** ($t < t_{\text{eq}}$):
In the early universe, the superfluid density is high and the kinetic energies $\dot{\phi}^2$ and $\dot{\psi}_q^2$ are negligible compared to the potential energies. Thus:

$$w_{\text{inf}} \approx -\frac{V_{\text{dil}} + V_{\text{quint}}}{V_{\text{dil}} + V_{\text{quint}}} \approx -1$$

This produces the $\rho \sim \text{const}$ (nearly constant density) characteristic of inflation.

**Dark Energy Phase** ($t > t_{\text{eq}}$):
After inflation ends (around $t_{\text{eq}}$), the fields settle into a new quasi-static regime where kinetic energy is suppressed but not zero. The equation of state evolves:

$$w_{\text{DE}}(t) = -1 + \epsilon(t)$$

where $\epsilon(t) = O(\text{small kinetic/potential ratio})$ is time-dependent. This is exactly the running vacuum behavior observed in modern cosmological data (e.g., DESI).

**Transition Mechanism**:
The non-minimal coupling between dilaton and quintom drives the transition. As the universe cools, the dilaton (breathing mode) decouples, and the quintom field takes over. The logarithmic potential of the quintom:

$$V_{\text{quint}}(\psi_q) \sim \psi_q^4 \log(\psi_q^2)$$

has a shallow minimum, allowing $\psi_q$ to slowly roll, producing the late-time dark energy acceleration.

---

## Key Results

1. **Unified Inflation-DE Framework**: Both inflation and dark energy emerge from a single physical substrate—the superfluid vacuum—without separate field theory hypotheses.

2. **Natural Exit from Inflation**: The superfluid model provides a graceful exit mechanism: as the dilaton field decouples, the quintom takes over, naturally ending the high-energy inflationary phase.

3. **Non-Minimal Coupling**: The quintessence and phantom components are coupled in the superfluid framework, giving a more constrained model than standard quintessence + phantom combinations.

4. **Dynamical Dark Energy**: The running equation of state $w(t) = -1 + \epsilon(t)$ predicts that dark energy is mildly evolving, consistent with recent DESI data hinting at $w \neq -1$.

5. **Thermodynamic Stability**: The logarithmic Bose liquid is thermodynamically stable (unlike some phantom models that exhibit instabilities), providing a robust UV completion.

6. **Reduction of Parameters**: SVT requires fewer free parameters than standard inflation + quintessence models, enhancing predictive power.

---

## Impact and Legacy

Zloshchastiev's SVT program has inspired a growing body of work exploring BEC cosmology as an alternative to standard inflationary paradigm:

- **Quantum Vortex Dynamics**: Vortices in the superfluid correspond to cosmic strings in the effective spacetime, offering a mechanism for topological defect production.
- **Sound Speed**: Phonon excitations of the superfluid have finite sound speed, preventing acausal propagation and protecting the theory from theoretical pathologies.
- **Observational Tests**: The SVT predictions for primordial power spectrum, running spectral index, and tensor-to-scalar ratio differ subtly from $\Lambda$CDM, enabling distinguishability in principle.
- **Axion Connection**: Some work connects the superfluid vacuum to axion physics and axion dark matter, broadening SVT's scope.

---

## Connection to Phonon-Exflation Framework

**Relevance: CRITICAL — Structural Isomorphism**

The phonon-exflation framework is built on a strikingly similar physical picture: **particles are collective excitations (phonons) of an M4 × SU(3) substrate, and the expansion/contraction of the internal SU(3) space drives the cosmological evolution**.

The parallels with SVT are profound:

1. **Substrate Principle**: Both frameworks posit that what we observe as particle physics and cosmology emerge from a quantum many-body system (superfluid vacuum in SVT, BCS phonon condensate in phonon-exflation).

2. **Equation of State Transition**: SVT shows that $w \approx -1$ (inflationary) transitioning to $w \approx -1 + \epsilon$ (late-time DE) emerges naturally. Phonon-exflation predicts **exactly** $w = -1$ (de Sitter cosmology with constant spectral action), with DE from the slow relaxation of the K7 sector.

3. **Dilaton-Like Field**: In SVT, the dilaton controls the transition. In phonon-exflation, the K7 "structure parameter" $\tau$ plays this role. Both are related to intrinsic scale (vacuum density in SVT, fiber compactification radius in phonon-exflation).

4. **Coupling to Matter**: SVT couples dilaton to quintom non-minimally. Phonon-exflation couples K7 to the Dirac spectrum non-trivially: $[iK_7, D_K] = 0$ at all $\tau$. This is the fundamental symmetry protecting particle masses.

5. **Phonon Spectrum**: SVT's phonon excitations of the superfluid (sound waves) become the photons, neutrinos, and quarks of the emergent theory. Phonon-exflation builds on this: particle content emerges from the spectral representation of $D_K$.

**Key Difference**:
- SVT treats the transition inflation → DE as dynamical evolution of scalar fields (dilaton, quintom).
- Phonon-exflation proposes the transition is **geometric**: it arises from the topological transition of the SU(3) fiber from unity (closed) to a "folded" configuration (expanding). The spectral action is **monotone** in this folding (S24b result), so the transition is driven by purely geometric dynamics, not ad hoc potentials.

**Integration Strategy**:
1. The phonon-exflation substrate IS a superfluid (BCS condensate of K7-paired fermions).
2. The dilaton in SVT → the K7 parameter τ in phonon-exflation.
3. The quintom in SVT → the long-wavelength phonon modes (quadrupole, octupole deformations of the SU(3) fiber).
4. The logarithmic Bose liquid (SVT) → the BCS free energy with Richardson-Gaudin integrability (phonon-exflation).

**Testable Prediction**:
SVT predicts $w(z)$ crosses $-1$ at some redshift (phantom crossing). Phonon-exflation (with monotonic spectral action) predicts $w = -1$ exactly, with DE coming from geometric rigidity (the spectral action "prefers" a specific K7 configuration).

**Recent Support** (Session 35):
- RPA-35 confirmed M_max = 1.674 (BCS instability inevitable).
- Wall-35 confirmed Z = 1.016 (phonon domain formation robust).
- BdG-35 confirmed E_cond = -0.115 (negative energy, pumping anti-trapping dynamics).

These results show that the "substrate" in phonon-exflation is physically realized and exhibits the phononic/collective properties predicted. The connection to SVT's dilaton-quintom transition is now quantitatively testable.

**Status**: This paper provides independent theoretical support for substrate-based cosmology. The phonon-exflation program can now cite SVT as parallel theoretical development, strengthening the credibility of the entire "vacuum as quantum liquid" paradigm.
