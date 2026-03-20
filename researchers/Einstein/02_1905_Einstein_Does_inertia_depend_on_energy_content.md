# Does the Inertia of a Body Depend Upon Its Energy Content?

**Author:** Albert Einstein
**Year:** 1905
**Journal:** *Annalen der Physik*, **18**, 639--641

---

## Abstract

In this remarkably brief three-page paper -- arguably the most consequential short paper in physics -- Einstein demonstrates that if a body emits electromagnetic radiation, its inertial mass decreases by an amount equal to the radiated energy divided by $c^2$. He concludes that the mass of a body is a measure of its energy content, establishing the equivalence $E = mc^2$. The derivation uses only the Lorentz transformations and the transformation properties of electromagnetic energy, with no additional assumptions. The result implies that all forms of energy -- kinetic, thermal, chemical, nuclear -- contribute to inertial mass, and conversely, that mass itself represents a reservoir of energy.

---

## Historical Context

### The September Paper

This paper, received by *Annalen der Physik* on September 27, 1905, is a direct sequel to the June paper on special relativity ("On the Electrodynamics of Moving Bodies"). Einstein refers to it explicitly and uses the transformation laws derived there. It represents Einstein's immediate recognition that special relativity had consequences far beyond electrodynamics -- it restructured the relationship between the most fundamental concepts in mechanics.

### Mass in Classical Physics

In Newtonian mechanics, mass appeared in two distinct roles: as the source of gravitational attraction (gravitational mass) and as resistance to acceleration (inertial mass). While the numerical equality of these two masses was a well-established empirical fact (Eotvos experiments), there was no theoretical reason for it. More relevantly for this paper, inertial mass in Newtonian mechanics was a conserved, immutable property of matter -- a body's mass was fixed regardless of its internal state.

### Electromagnetic Mass

The concept that electromagnetic energy might contribute to inertia was not entirely new. J.J. Thomson (1881) and others had noted that a charged particle possesses an "electromagnetic mass" $m_{em} \sim U_{em}/c^2$ due to the energy stored in its electric field. Abraham and Lorentz developed detailed models of the electron in which mass was entirely electromagnetic in origin. However, these were specific models tied to particular assumptions about the structure of the electron.

Einstein's contribution was to show that the relationship between energy and inertia is universal -- it follows from the structure of spacetime itself, not from any model of matter.

---

## Key Arguments and Derivations

### The Setup

Einstein considers a body at rest in frame $S$ with energy $E_0$. The body emits two pulses of electromagnetic radiation, each with energy $L/2$, in opposite directions along the $x$-axis. By symmetry, the body remains at rest after emission (no recoil, since the momenta cancel).

After emission, the body has energy $E_1$ in $S$, with:

$$E_0 = E_1 + L$$

This is simply energy conservation in the rest frame.

### Analysis in the Moving Frame

Now Einstein considers the same process from frame $S'$, moving with velocity $v$ along the $x$-axis relative to $S$. The body has energy $H_0$ before emission and $H_1$ after.

The key step is applying the Doppler effect and the relativistic transformation of electromagnetic energy. A light pulse of energy $\mathcal{E}$ emitted at angle $\phi$ to the $x$-axis in $S$ has energy in $S'$:

$$\mathcal{E}' = \mathcal{E} \cdot \gamma\left(1 - \frac{v}{c}\cos\phi\right)$$

For the two pulses emitted in opposite directions ($\phi = 0$ and $\phi = \pi$):

$$\mathcal{E}'_1 = \frac{L}{2}\gamma\left(1 - \frac{v}{c}\right)$$

$$\mathcal{E}'_2 = \frac{L}{2}\gamma\left(1 + \frac{v}{c}\right)$$

The total radiated energy in $S'$ is:

$$\mathcal{E}'_1 + \mathcal{E}'_2 = \frac{L}{2}\gamma\left(1 - \frac{v}{c}\right) + \frac{L}{2}\gamma\left(1 + \frac{v}{c}\right) = L\gamma$$

Energy conservation in $S'$:

$$H_0 = H_1 + L\gamma$$

### Extracting the Mass-Energy Relation

Now Einstein takes the difference of the energy equations between frames. Define:

$$K_0 = H_0 - E_0 \qquad \text{(kinetic energy before emission)}$$
$$K_1 = H_1 - E_1 \qquad \text{(kinetic energy after emission)}$$

Here Einstein uses the fact that $H - E$ represents the kinetic energy of the body, since $H$ is the total energy in the moving frame and $E$ is the rest-frame energy -- their difference is the kinetic energy due to the body's motion.

Subtracting the two conservation equations:

$$(H_0 - E_0) - (H_1 - E_1) = L\gamma - L$$

$$K_0 - K_1 = L\left(\gamma - 1\right)$$

Expanding $\gamma$ for small $v/c$:

$$\gamma - 1 = \frac{1}{\sqrt{1 - v^2/c^2}} - 1 \approx \frac{v^2}{2c^2} + \mathcal{O}(v^4/c^4)$$

Therefore:

$$K_0 - K_1 = \frac{L}{2}\frac{v^2}{c^2} + \text{higher order}$$

### The Interpretation

In Newtonian mechanics, the kinetic energy of a body of mass $m$ moving at velocity $v$ is $K = \frac{1}{2}mv^2$. If the body's mass changes from $m_0$ to $m_1$ but its velocity remains the same (the body is still at rest in $S$, moving at $v$ in $S'$), then:

$$K_0 - K_1 = \frac{1}{2}(m_0 - m_1)v^2$$

Comparing:

$$\frac{1}{2}(m_0 - m_1)v^2 = \frac{L}{2}\frac{v^2}{c^2}$$

$$m_0 - m_1 = \frac{L}{c^2}$$

**The mass of the body decreases by $L/c^2$ when it emits energy $L$.**

### Einstein's Generalization

Einstein then makes the crucial inductive leap. He writes:

> "If a body gives off the energy $L$ in the form of radiation, its mass diminishes by $L/c^2$. The fact that the energy withdrawn from the body becomes energy of radiation evidently makes no difference, so that we are led to the more general conclusion that the mass of a body is a measure of its energy-content."

This generalization -- from radiative energy to all forms of energy -- cannot be strictly proved from the specific calculation. It is a physical hypothesis, albeit one powerfully motivated by the universality of the Lorentz transformations. In modern language, the equivalence $E = mc^2$ follows from the structure of the Poincare group: the rest energy is the Casimir invariant $p_\mu p^\mu = m^2 c^2$.

### The Exact Relativistic Form

The full relativistic energy-momentum relation (not in the 1905 paper, but following directly) is:

$$E^2 = (pc)^2 + (mc^2)^2$$

For a body at rest ($p = 0$):

$$E_0 = mc^2$$

For a body in motion:

$$E = \gamma mc^2$$

The kinetic energy is:

$$K = E - E_0 = (\gamma - 1)mc^2$$

which reduces to $\frac{1}{2}mv^2$ for $v \ll c$.

---

## Physical Interpretation

### Mass as Stored Energy

The equation $E = mc^2$ means that mass is not an independent property of matter but is equivalent to energy. A hot object is (very slightly) more massive than a cold one. A compressed spring is more massive than a relaxed one. A hydrogen atom is less massive than a free proton plus a free electron by exactly the binding energy divided by $c^2$.

The conversion factor $c^2 \approx 9 \times 10^{16}$ J/kg is enormous, which explains why the mass-energy equivalence was not noticed in ordinary chemical reactions. The fractional mass change in chemical reactions is of order $10^{-9}$, far below the precision of any balance at the time.

### Nuclear Energy

The equivalence becomes spectacularly visible in nuclear reactions. In uranium-235 fission:

$$^{235}\text{U} + n \to \text{fragments} + \text{neutrons}$$

the mass deficit is about 0.1% of the total mass, corresponding to approximately 200 MeV per fission event, or about $8.2 \times 10^{13}$ J per kilogram -- a million times the energy density of chemical fuels.

In stellar nucleosynthesis, the pp-chain converts four protons into helium-4:

$$4p \to {}^4\text{He} + 2e^+ + 2\nu_e + 2\gamma$$

The mass deficit is 0.7% of the initial proton mass, and this powers the Sun.

### Particle Physics

In modern particle physics, $E = mc^2$ operates in both directions. Mass is routinely created from kinetic energy: in $e^+e^-$ colliders, the electron and positron annihilate and their combined energy materializes as new particles (quarks, leptons, gauge bosons). The Higgs boson, with mass $\approx 125$ GeV/$c^2$, was produced at the LHC from the kinetic energy of colliding protons.

For massless particles (photons, gluons), $E = pc$ and the rest mass is zero. For massive particles, the rest mass is the energy measured in the particle's rest frame.

---

## Impact and Legacy

### The Most Famous Equation

$E = mc^2$ has become the most widely recognized equation in science, a cultural icon representing the power and danger of physics. Its fame is partly due to its association with nuclear weapons -- though Einstein himself did not work on the Manhattan Project, his 1939 letter to Roosevelt (prompted by Szilard) warned of the possibility of nuclear chain reactions.

### Experimental Verification

The mass-energy equivalence has been verified to extraordinary precision:

- **Nuclear binding energies:** The mass deficits in nuclear reactions match the released energy to parts per million.
- **Particle-antiparticle annihilation:** $e^+ + e^- \to 2\gamma$ produces photons with total energy exactly $2m_e c^2$ (in the center-of-mass frame).
- **Pion mass determination:** The masses of hadrons computed from QCD lattice calculations match experiment, with the quark masses contributing only $\sim 1\%$ of the proton mass -- the rest is the kinetic and interaction energy of quarks and gluons.
- **Rainville et al. (2005):** Direct comparison of mass differences in neutron capture reactions with emitted gamma-ray energies, confirming $E = mc^2$ to $0.00004\%$.

### Conceptual Legacy

The mass-energy equivalence fundamentally altered the conservation laws of physics. In Newtonian mechanics, mass and energy are separately conserved. In relativity, only total energy (including rest energy) is conserved. "Conservation of mass" becomes an approximation valid when energies are small compared to rest energies.

---

## Connections to Modern Physics

### The Energy-Momentum Four-Vector

In modern formulation, a particle's four-momentum is:

$$p^\mu = (E/c, \mathbf{p})$$

The invariant mass is:

$$m^2 c^2 = -\eta_{\mu\nu} p^\mu p^\nu = \frac{E^2}{c^2} - |\mathbf{p}|^2$$

This is Lorentz-invariant: all observers agree on the rest mass. The "relativistic mass" $m_{rel} = \gamma m$ is now disfavored in pedagogy; only invariant mass and total energy are used.

### The Higgs Mechanism and the Origin of Mass

$E = mc^2$ tells us that mass IS energy, but it does not explain WHY particles have the specific masses they do. The Standard Model answers this partially: fermion masses arise from Yukawa couplings to the Higgs field, and the $W/Z$ masses from the Higgs mechanism. But the Yukawa coupling constants are free parameters -- the origin of the mass spectrum is unexplained.

The proton mass ($\sim 938$ MeV) is a particularly striking case: the constituent up and down quarks have masses of only $\sim 2-5$ MeV. Over 99% of the proton's mass comes from the kinetic energy of quarks and the energy stored in gluon fields -- a dramatic realization of Einstein's insight that energy has inertia.

### Cosmological Implications

In cosmology, the energy content of the universe determines its geometry and expansion history through Einstein's field equations. The equivalence of mass and energy means that radiation (photons, neutrinos) gravitates just as matter does. In the early universe, when radiation energy density dominated, the expansion rate was set by the energy density of massless particles.

### Phononic Analogies

In condensed matter systems where particles are modeled as collective excitations (phonons, quasiparticles), the effective mass of an excitation is determined by its dispersion relation $E(\mathbf{k})$. Near the bottom of a band, $E \approx E_0 + \hbar^2 k^2/(2m^*)$, and the effective mass $m^*$ plays the role of inertial mass. This is a low-energy analog of $E = mc^2$: the "rest energy" $E_0$ of the excitation contributes to its inertial response. In frameworks that treat fundamental particles as phononic excitations of an internal space, the mass-energy relation would emerge from the dispersion relation of the underlying medium.
