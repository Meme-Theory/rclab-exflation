# Notes on Black-Hole Evaporation

**Authors**: William G. Unruh
**Year**: 1976
**Journal**: *Physical Review D*, **14**, 870--892

---

## Abstract (Analytical Summary)

Unruh discovers that a uniformly accelerating observer in flat Minkowski spacetime perceives the quantum vacuum as a thermal bath of particles at temperature $T = \hbar a / 2\pi c k_B$, where $a$ is the proper acceleration. This *Unruh effect* is derived by quantizing a scalar field in Rindler coordinates (the natural coordinates for an accelerating observer) and showing that the Minkowski vacuum contains Rindler particles with a Planck spectrum. The result illuminates the deep connection between acceleration, horizons, and temperature, and provides an independent derivation and conceptual clarification of Hawking radiation: the thermal radiation from a black hole can be understood as the Unruh effect experienced by a static observer near the horizon, redshifted to infinity.

---

## Historical Context

### The Puzzle of Hawking Radiation

Hawking's 1974--1975 derivation of black hole radiation used the specific dynamics of gravitational collapse: a star collapses, a horizon forms, and the Bogoliubov transformation between early-time and late-time mode functions produces thermal particles. A natural question arose: is the thermal radiation a consequence of the *dynamics* of collapse, or of the *kinematics* of having a horizon?

### The Equivalence Principle

Einstein's equivalence principle states that a uniformly accelerating frame in flat spacetime is locally indistinguishable from a gravitational field. If a black hole radiates, then by the equivalence principle, an accelerating observer should see something similar. Unruh made this precise.

### Rindler Space

The idea of quantizing fields in accelerating frames goes back to Fulling (1973), who showed that the Fock spaces built from Minkowski and Rindler mode functions are unitarily inequivalent. Unruh's contribution was to compute the physical content: an accelerating observer detects real particles.

---

## Key Arguments and Derivations

### Rindler Coordinates

A uniformly accelerating observer in Minkowski spacetime with proper acceleration $a$ follows the worldline:

$$t = \frac{c}{a}\sinh\left(\frac{a\tau}{c}\right), \qquad x = \frac{c^2}{a}\cosh\left(\frac{a\tau}{c}\right)$$

where $\tau$ is proper time. The observer is confined to the right Rindler wedge: $x > |ct|$. The surfaces $x = \pm ct$ are the Rindler horizons -- the boundaries of the region accessible to the accelerating observer.

Rindler coordinates $(\eta, \xi)$ cover the right wedge:

$$t = \xi \sinh(a\eta/c), \qquad x = \xi \cosh(a\eta/c)$$

where $\eta$ is the Rindler time (proportional to proper time along each accelerated worldline) and $\xi$ is the Rindler spatial coordinate. The Minkowski metric becomes:

$$ds^2 = -\left(\frac{a\xi}{c^2}\right)^2 c^2 d\eta^2 + d\xi^2 + dy^2 + dz^2$$

This is a static metric with a Killing horizon at $\xi = 0$ (the Rindler horizon). The surface gravity of this horizon is:

$$\kappa = a$$

### Quantization in Two Frames

**Minkowski quantization**: The scalar field $\phi$ is expanded in positive-frequency Minkowski modes $f_k \propto e^{-i\omega t + ikx}$ with $\omega > 0$:

$$\phi = \sum_k \left(a_k f_k + a_k^\dagger f_k^*\right)$$

The Minkowski vacuum is $|0_M\rangle$: $a_k |0_M\rangle = 0$ for all $k$.

**Rindler quantization**: In the right Rindler wedge, the field is expanded in positive-frequency Rindler modes $g_\Omega$ (positive frequency with respect to Rindler time $\eta$):

$$\phi = \sum_\Omega \left(b_\Omega g_\Omega + b_\Omega^\dagger g_\Omega^*\right)$$

The Rindler vacuum is $|0_R\rangle$: $b_\Omega |0_R\rangle = 0$ for all $\Omega$.

Crucially, $|0_M\rangle \neq |0_R\rangle$. The Minkowski vacuum contains Rindler particles.

### The Bogoliubov Transformation

The Rindler modes are related to the Minkowski modes by a Bogoliubov transformation:

$$g_\Omega = \sum_k \left(\alpha_{\Omega k} f_k + \beta_{\Omega k} f_k^*\right)$$

The number of Rindler particles in mode $\Omega$ as seen from the Minkowski vacuum is:

$$\langle 0_M | b_\Omega^\dagger b_\Omega | 0_M \rangle = \sum_k |\beta_{\Omega k}|^2$$

### Computing the Bogoliubov Coefficients

The calculation exploits the analytic structure of the Minkowski modes continued to the Rindler wedge. The Minkowski positive-frequency mode $e^{-i\omega t + ikx}$ restricted to the right Rindler wedge has the form:

$$f_k \Big|_R \propto \xi^{i\omega/a} = e^{(i\omega/a) \ln \xi}$$

The Fourier transform with respect to Rindler time gives the overlap with Rindler modes. The key step is the analytic continuation across the Rindler horizon ($\xi = 0$). The positive-frequency Minkowski mode analytically continues as:

$$f_k \to e^{-\pi\omega/a} \cdot f_k^* \qquad (\text{on the left Rindler wedge})$$

This gives the ratio:
$$|\beta_{\Omega k}|^2 = e^{-2\pi\Omega/a} |\alpha_{\Omega k}|^2$$

and therefore:
$$\langle N_\Omega \rangle = \frac{1}{e^{2\pi\Omega/a} - 1}$$

This is a **Planck spectrum** at temperature:

$$T_U = \frac{\hbar a}{2\pi c k_B}$$

### The Unruh Temperature

In SI units:
$$T_U = \frac{\hbar a}{2\pi c k_B} \approx 4.05 \times 10^{-23} \, a \text{ K}$$

where $a$ is in m/s$^2$. For everyday accelerations, this is absurdly small:
- $a = 10$ m/s$^2$ (Earth's gravity): $T \sim 4 \times 10^{-22}$ K
- $a = 10^{20}$ m/s$^2$ (electron in a strong laser): $T \sim 4$ K

Only at extreme accelerations $a \sim 10^{23}$ m/s$^2$ (approaching nuclear scales) does the Unruh temperature become significant.

### The Thermofield Double (TFD) Structure

Unruh shows that the Minkowski vacuum, expressed in the Rindler basis, takes the form of a thermofield double state:

$$|0_M\rangle = \frac{1}{Z^{1/2}} \sum_n e^{-\pi n \Omega / a} |n\rangle_R \otimes |n\rangle_L$$

where $|n\rangle_R$ and $|n\rangle_L$ are $n$-particle states in the right and left Rindler wedges, respectively. Tracing over the left wedge (inaccessible to the accelerating observer) gives:

$$\rho_R = \text{Tr}_L |0_M\rangle\langle 0_M| = \frac{1}{Z} e^{-2\pi \hat{H}_R / a}$$

a thermal density matrix at temperature $T = a / 2\pi$ (natural units). The entanglement between the two Rindler wedges is the origin of the thermal spectrum. This is the same structure that appears in the ER=EPR conjecture.

### Connection to Hawking Radiation

For a Schwarzschild black hole, a static observer at coordinate radius $r$ has proper acceleration:

$$a = \frac{M/r^2}{\sqrt{1 - 2M/r}}$$

Near the horizon ($r \to 2M$), $a \to \infty$. The local Unruh temperature diverges at the horizon. However, radiation observed at infinity is redshifted by the factor $\sqrt{1 - 2M/r}$:

$$T_\infty = \frac{a \sqrt{1 - 2M/r}}{2\pi} = \frac{1}{2\pi} \cdot \frac{M/r^2}{\sqrt{1 - 2M/r}} \cdot \sqrt{1 - 2M/r} = \frac{M}{2\pi r^2}$$

At the horizon ($r = 2M$):
$$T_\infty = \frac{1}{8\pi M} = \frac{\kappa}{2\pi}$$

This is exactly the Hawking temperature! The Hawking radiation is the Unruh effect for static observers near the black hole horizon, redshifted to infinity.

### The Unruh--DeWitt Detector

To make the particle detection operationally precise, Unruh (and independently DeWitt) introduced a model particle detector: a two-level system (with energy gap $E_0$) coupled to the scalar field. The excitation rate of the detector moving on worldline $x^\mu(\tau)$ is:

$$\dot{P}(E_0) = \int_{-\infty}^{\infty} ds \, e^{-iE_0 s} \, G^+(\tau, \tau - s)$$

where $G^+(x, x') = \langle 0 | \phi(x) \phi(x') | 0 \rangle$ is the Wightman function. For a uniformly accelerating detector in the Minkowski vacuum, the Wightman function is periodic in imaginary proper time with period $2\pi/a$, giving an excitation rate:

$$\dot{P}(E_0) \propto \frac{E_0}{e^{2\pi E_0/a} - 1}$$

a thermal spectrum at the Unruh temperature. This confirms that the accelerating observer genuinely *detects* particles, not merely "sees" them.

---

## Physical Interpretation

### The Vacuum Is Observer-Dependent

The most profound lesson of the Unruh effect is that "particle" is not an observer-independent concept in quantum field theory. The vacuum (zero-particle state) defined by one observer contains particles as measured by another. In flat spacetime, all inertial observers agree on the vacuum (this is the content of the Wigner--Poincare classification of particles). But accelerating observers disagree.

### Horizons Create Temperature

The Unruh effect, Hawking radiation, and the Gibbons--Hawking de Sitter temperature are all manifestations of a single principle: an observer with a causal horizon perceives the vacuum state as thermal. The temperature is universally $T = \kappa/2\pi$, where $\kappa$ is the surface gravity of the horizon.

### Entanglement as the Origin of Temperature

The thermal nature of the Unruh state is not due to an external heat bath. It arises from entanglement: the Minkowski vacuum is an entangled state across the Rindler horizon, and restricting to one side gives a thermal density matrix. This is the prototype for understanding black hole entropy as entanglement entropy.

---

## Impact and Legacy

### Theoretical Foundations

The Unruh effect established key concepts in quantum field theory on curved spacetimes:
1. Observer-dependence of the particle concept
2. The equivalence between thermal states and entanglement across horizons
3. The KMS condition (periodicity in imaginary time) as the defining property of thermal states

### Analogue Gravity

The Unruh effect (and its close cousin, Hawking radiation) inspired the analogue gravity program (Unruh, 1981). In a flowing fluid, sound waves experience an "acoustic metric." A supersonic flow creates a sonic horizon where the acoustic analogue of Hawking radiation occurs. Experiments in BEC (Steinhauer, 2016) and water waves have confirmed aspects of this analogy.

### Experimental Proposals

The Unruh effect has never been directly observed due to the tiny temperature. Proposals include:
- High-intensity laser pulses accelerating electrons (Chen and Tajima, 1999)
- Circular motion (acceleration $a = v^2/R$) in storage rings (Bell and Leinaas, 1983, proposed that the Sokolov--Ternov effect IS the circular Unruh effect)
- Superconducting circuits (analog Unruh radiation in circuit QED)

### The Bisognano--Wichmann Theorem

In axiomatic quantum field theory, the Bisognano--Wichmann theorem (1975, 1976) proves that the modular flow of the vacuum state restricted to a Rindler wedge IS the Rindler time translation, with temperature $T = 1/2\pi$ (in units where $a = 1$). This provides a rigorous mathematical foundation for the Unruh effect.

---

## Connections to Modern Physics

1. **ER=EPR and thermofield doubles**: Maldacena and Susskind (2013) conjectured that entangled pairs (EPR) are connected by Einstein--Rosen bridges (wormholes). The thermofield double structure of the Unruh state is the simplest example: the entanglement between left and right Rindler wedges is the Rindler analogue of a wormhole.

2. **Modular Hamiltonians and entanglement entropy**: In the modular approach to quantum field theory, the Unruh effect is the statement that the modular Hamiltonian for the vacuum restricted to a half-space is proportional to the boost generator. This connection is central to the derivation of the RT formula and to the "gravity from entanglement" program.

3. **Quantum information in QFT**: The Unruh effect demonstrates that the vacuum is a resource for quantum information protocols. Reznik (2003) showed that vacuum entanglement can be extracted and used for quantum teleportation.

4. **Dynamical Casimir effect**: When a mirror accelerates, it converts virtual photons into real ones -- the dynamical Casimir effect. This was observed by Wilson et al. (2011) using a SQUID in a superconducting circuit. The connection to the Unruh effect is through the same Bogoliubov transformation formalism.

5. **For the exflation framework**: In a Kaluza--Klein framework, a "static" observer in 4D may be accelerating in the higher-dimensional space if the internal geometry is evolving. The Unruh effect in the full $M_4 \times K$ spacetime would produce an effective 4D temperature that depends on both the 4D acceleration and the rate of change of the internal geometry. In the exflation model, the cosmological expansion driven by internal compactification would produce an analogue of the Gibbons--Hawking temperature, but with corrections from the internal space dynamics. The BEC analogue gravity connection is particularly relevant: if particles are phononic excitations, then the Unruh effect for phonons in a BEC IS the fundamental physics, not merely an analogy.
