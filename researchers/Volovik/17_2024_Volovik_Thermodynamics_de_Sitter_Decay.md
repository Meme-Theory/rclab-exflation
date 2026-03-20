# Thermodynamics and Decay of de Sitter Vacuum

**Author:** Grigory E. Volovik
**Year:** 2024
**Journal:** Symmetry 16(6), 763 (2024)
**arXiv:** 2312.02292

---

## Abstract

The unique symmetry of de Sitter spacetime is invariant under modified translations. All comoving observers at any point of de Sitter space perceive the de Sitter environment as a thermal bath with temperature $T = H/\pi$, which is twice larger than the Gibbons-Hawking temperature $T_{GH} = H/(2\pi)$ of the cosmological horizon. This leads to heat exchange between gravity and matter, and to instability of the de Sitter state toward the creation of matter, its further heating, and finally to the decay of the de Sitter state. The temperature $T = H/\pi$ determines different processes in the de Sitter environment (such as ionization of an atom) that are not possible in Minkowski vacuum. It also determines the local entropy of the de Sitter vacuum state, allowing calculation of the total entropy inside the cosmological horizon. The paper establishes connections between de Sitter thermodynamics and the gravitational dynamics through modified translation symmetry.

---

## Historical Context

The relationship between thermodynamics and gravity has been a central theme since Bekenstein's discovery of black hole entropy and Hawking's thermodynamic derivation of black hole temperature. However, the de Sitter case—representing accelerated expansion—has received less attention. De Sitter thermodynamics is crucial for understanding cosmological horizons and the late-time universe's thermodynamic state.

Volovik's 2024 work extends the thermodynamic framework to de Sitter spacetime as a whole, demonstrating that the perceived temperature by comoving observers exceeds the naive Gibbons-Hawking value. This surprising result—$T = H/\pi$ versus $T_{GH} = H/(2\pi)$—implies fundamental consequences: the de Sitter vacuum is thermodynamically unstable and naturally decays through particle creation and heating.

The paper's significance lies in reframing cosmological acceleration not as a static state but as a dynamical process driven by thermodynamic instability. This perspective directly addresses the phonon-exflation framework's prediction of time-dependent dark energy ($w \neq -1$) and the GGE relic state's metastability.

---

## Key Arguments and Derivations

### Modified Translation Symmetry of de Sitter Space

De Sitter spacetime has metric:

$$ds^2 = -dt^2 + e^{2Ht} (dx^2 + dy^2 + dz^2)$$

where $H$ is the Hubble parameter. The symmetry group is $SO(1,4)$, which acts as modified translations in addition to rotations. Unlike Minkowski space where translations are simple $x \to x + a$, in de Sitter the translations mix temporal and spatial coordinates.

The key insight is that comoving observers follow worldlines parametrized by proper time $\tau$, while the coordinate time $t$ and spatial scale factor evolve. The transformation properties under "modified translations" (which preserve the de Sitter metric) are:

$$t \to t + \alpha, \quad \vec{x} \to e^{-H\alpha} \vec{x}$$

These translations form a continuous symmetry—comoving observers at different spatial points are related by this modification.

### The Comoving Thermal Bath Perception

From the perspective of a comoving observer at fixed comoving coordinates $(t, \vec{x}_c)$ where $\vec{x} = e^{-Ht} \vec{x}_c$, the thermodynamic properties of the de Sitter environment include:

1. **Radiation background**: The accelerating expansion continuously creates particle pairs (Schwinger-like production at the cosmological horizon).

2. **Effective temperature**: The comoving observer perceives radiation with spectrum determined by the Unruh acceleration. For de Sitter comoving observers at proper acceleration $a = H$ (due to geodesic expansion), the perceived temperature is:

$$T = \frac{\hbar H}{2\pi k_B}$$

(in natural units with $\hbar = k_B = 1$: $T = H/(2\pi)$)

However, Volovik's key result is that the full de Sitter thermodynamic environment perceived by the observer includes additional contributions from the modified translation symmetry. The total temperature is:

$$T_{total} = \frac{H}{\pi}$$

This is exactly twice the Gibbons-Hawking temperature. The factor of 2 arises from contributions beyond the cosmological horizon itself: the observer perceives heat exchange from the entire de Sitter manifold, not just from the boundary.

### Heat Exchange and Thermal Instability

The presence of a thermal bath at temperature $T = H/\pi$ drives thermodynamic processes in the de Sitter environment. Specifically, atomic ionization, vacuum decay, and particle creation become possible at rates determined by this temperature. For a process with activation energy $E$, the rate scales as:

$$\Gamma \propto e^{-E/T} = e^{-E\pi/H}$$

Since $H$ is tiny ($H_0 \approx 10^{-42}$ GeV in natural units), even processes with $E \sim$ eV become significant at cosmological timescales.

Moreover, the heat exchange between the de Sitter vacuum (at temperature $T = H/\pi$) and matter creates a thermodynamic driving force. If matter starts colder than $T = H/\pi$, it absorbs heat. The matter heats and eventually radiates back, but the net entropy production in the universe increases. Einstein's equations couple this entropy change to spacetime geometry:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}^{(matter)}$$

As matter heats and density increases, the right-hand side increases, accelerating the expansion briefly, then the matter's backreaction increases pressure, eventually suppressing further acceleration.

### De Sitter Entropy and Thermodynamic Stability

The de Sitter vacuum's entropy is related to the cosmological horizon area. Using Gibbons-Hawking formula:

$$S_{GH} = \frac{A_H}{4G} = \frac{4\pi H^{-2}}{4G} = \frac{\pi}{G H^2}$$

(in natural units: $S_{GH} = \pi / H^2$)

However, the local entropy density of the de Sitter environment, when accounting for the temperature $T = H/\pi$, includes additional contributions from radiation and matter excitations:

$$s_{local} = \rho_{rad} / T = \rho_{rad} \pi / H$$

As particles are created by the thermal bath and heat up, entropy increases. The total entropy evolution is:

$$\frac{dS_{tot}}{dt} = \frac{\pi}{H^2} \frac{dH}{dt} + \int dV \frac{1}{T} \frac{dE_{rad}}{dt}$$

Crucially, the creation and heating of particles **increases** the total entropy, making the process thermodynamically favorable. This drives the instability.

### Connection to f(R) Gravity

In modified gravity frameworks like $f(R)$ gravity, the modified Einstein equations are:

$$f'(R) R_{\mu\nu} - \frac{1}{2} f(R) g_{\mu\nu} + \left( \nabla_\mu \nabla_\nu - g_{\mu\nu} \Box \right) f''(R) = 8\pi G T_{\mu\nu}$$

In this formulation, $R$ and the effective coupling $f'(R)$ become thermodynamic variables. De Sitter thermodynamics in $f(R)$ gravity shows that:

$$T = \frac{H}{\pi}, \quad \text{pressure} \propto f''(R)$$

The instability manifests as $f''(R)$ becoming negative (repulsive effective pressure), destabilizing the de Sitter solution.

---

## Key Results

1. **Modified Temperature Relation:** Comoving observers in de Sitter perceive temperature $T = H/\pi$, exactly twice the Gibbons-Hawking horizon temperature, due to modified translation symmetry contributions.

2. **Thermodynamic Instability:** The de Sitter vacuum is thermodynamically unstable toward creation of matter, heating of that matter, and entropy increase—a second-law-driven process.

3. **Particle Creation Rates:** Processes with activation energy $E$ occur at rates $\propto \exp(-E\pi/H)$, becoming significant over cosmic timescales despite $H \ll 1$.

4. **Entropy Production:** The creation and heating of particles in the thermal bath increases total entropy, confirming the instability is thermodynamically favored.

5. **Horizon Area Law Preserved:** The relation between bulk entropy and boundary area (holography) remains valid despite instability, preserving Einstein's equations' consistency.

6. **Decay Time Scale:** For the de Sitter solution to remain metastable, the decay time must exceed the universe's age. Volovik shows this is achieved for realistic parameters, but decay is inevitable over sufficiently long timescales.

---

## Impact and Legacy

This paper reframes dark energy from a static cosmological constant to a metastable de Sitter-like state undergoing slow, thermodynamically-driven decay. The work influences modern understanding of:

- Late-time cosmology as a non-equilibrium process
- Thermodynamic bounds on inflation duration and current acceleration
- Entropy production and the second law in cosmology
- Connection between horizon temperature and vacuum particle creation

The result that $T = H/\pi$ (not $H/(2\pi)$) has implications for determining which vacuum decay channels dominate and how rapidly the accelerated expansion phase terminates.

---

## Connection to Phonon-Exflation Framework

Paper 17 provides critical physics for interpreting the **GGE-LAMBDA-38** and **FRIEDMANN-BCS-38** gates. Specifically:

- **De Sitter thermodynamic instability mirrors GGE non-equilibrium:** The de Sitter vacuum perceived at temperature $T = H/\pi$ is a thermal bath driving particle creation. Similarly, the phonon-exflation GGE relic (S38 W3) is a non-equilibrium state at effective "temperature" set by the Dirac spectrum's characteristic gap scale and chemical potential.

- **Particle creation as intanton gas:** Just as de Sitter's thermal instability drives continuous particle production, the instanton transit (S37-38) creates an 85.5% pair vibration (GPV) and dense pair gas (S_inst = 0.069). Both are manifestations of quantum critical dynamics.

- **Heat exchange and backreaction:** The heat exchange between de Sitter vacuum and matter (Volovik 2024) parallels the back-reaction of the BCS condensate onto the Dirac spectrum (Sessions 34-38). Both systems exhibit feedback: matter heating increases entropy; condensate formation releases spectral action energy, modifying the geometric background.

- **Non-equilibrium permanence:** Volovik shows de Sitter decay takes vast timescales despite instability—$\sim H^{-1} \cdot e^{\pi/H} \gg$ universe age. Phonon-exflation predicts GGE relic permanence for the same reason: integrability blocks thermalization. Both are metastable, long-lived non-equilibrium states.

- **Dynamical w(z) prediction:** If DESI observes $w(z) \neq -1$, this is exactly Volovik's prediction: not a static cosmological constant, but a decaying de Sitter-like state with time-dependent equation of state. The GGE relic's effective $w$ parameter depends on the instantaneous spectral action and condensate fraction, naturally producing the DESI phantom crossing at $z \approx 0.5$ (S36-38 predictions).

The phonon-exflation framework thus implements Volovik's thermodynamic de Sitter picture in a concrete microscopic model: the internal compactification is a Volovik quantum liquid (S37 paradigm shift), undergoing a BCS phase transition (thermal bath at $T \approx \Delta_0$), creating an instanton gas relic that mimics de Sitter decay through continuous energy dissipation to 4D gravity.

---

## References

- [2312.02292] Thermodynamics and decay of de Sitter vacuum (arXiv)
- Volovik, G.E., Symmetry 16, 763 (2024)
- Volovik, G.E., "The Universe in a Helium Droplet" (Oxford University Press, 2003)
- Gibbons, G.W. and Hawking, S.W., Phys. Rev. D 15, 2738 (1977)
