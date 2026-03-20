# Particle Creation by Black Holes

**Authors**: Stephen W. Hawking
**Year**: 1975
**Journal**: *Communications in Mathematical Physics*, **43**, 199--220

---

## Abstract (Analytical Summary)

This paper provides the complete, rigorous derivation of the result announced in the 1974 *Nature* letter. Hawking shows that a black hole formed by gravitational collapse creates and emits particles as if it were a blackbody of temperature $T = \hbar \kappa / 2\pi k_B$, where $\kappa$ is the surface gravity. The derivation uses the formalism of quantum field theory on curved spacetime: a massless scalar field is quantized on the background of a collapsing star, and the Bogoliubov transformation between the "in" vacuum (defined before collapse) and the "out" modes (defined at late times at future null infinity) is computed. The key technical result is that the Bogoliubov coefficients satisfy $|\beta_{\omega\omega'}|^2 / |\alpha_{\omega\omega'}|^2 = e^{-2\pi\omega/\kappa}$, giving a Planck distribution. The paper also discusses greybody factors, the back-reaction problem, and the implications for black hole thermodynamics. This is one of the most cited papers in general relativity.

---

## Historical Context

### Quantum Field Theory on Curved Spacetime

By the mid-1970s, the framework for quantum field theory on curved backgrounds was well-developed, largely by DeWitt, Brill, Parker, Fulling, and others. Parker (1969) had already shown that particle creation occurs in expanding universes -- the expansion of space stretches quantum fluctuations, converting vacuum modes into real particle pairs. The key insight was that "particle" is an observer-dependent concept in curved spacetime: the vacuum state for one observer contains particles as seen by another.

Fulling (1973) had shown that even in flat spacetime, different choices of time coordinate lead to inequivalent quantizations -- a result closely related to the Unruh effect. Hawking's contribution was to apply these ideas to the specific geometry of gravitational collapse.

### Why a Collapsing Star, Not an Eternal Black Hole

Hawking made the crucial physical choice to study a *dynamical* spacetime -- one where a star collapses to form a black hole -- rather than an eternal (Kruskal-extended) black hole. This is physically correct: real black holes form from collapse. It is also technically necessary: the eternal black hole has ambiguities related to the white hole region and the choice of vacuum state that obscure the physics. The collapsing geometry has a unique natural vacuum state at early times (the "in" vacuum defined when the star is large and the spacetime is approximately flat).

---

## Key Arguments and Derivations

### Setup: Scalar Field on Collapse Background

Consider a massless scalar field $\phi$ satisfying $\Box \phi = 0$ on the background of a spherically symmetric star that collapses to form a Schwarzschild black hole. The spacetime has three regions:

1. **Early times** ($\mathscr{I}^-$, past null infinity): flat spacetime, where the field is quantized in the usual way.
2. **Collapse region**: the star's surface passes through its Schwarzschild radius and an event horizon forms.
3. **Late times** ($\mathscr{I}^+$, future null infinity): the exterior settles to Schwarzschild geometry.

### Mode Decomposition

On $\mathscr{I}^-$, the field is expanded in positive-frequency modes $f_i$ (with respect to the Killing vector $\partial/\partial t$ of the early-time flat region):

$$\phi = \sum_i \left( a_i f_i + a_i^\dagger f_i^* \right)$$

The "in" vacuum is defined by $a_i |0_{\text{in}}\rangle = 0$.

On $\mathscr{I}^+$, the field is expanded in a different set of modes. There are two sets:

- $p_i$: modes that reach $\mathscr{I}^+$ (outgoing radiation)
- $q_i$: modes that fall into the black hole (absorbed)

$$\phi = \sum_i \left( b_i p_i + b_i^\dagger p_i^* + c_i q_i + c_i^\dagger q_i^* \right)$$

### Bogoliubov Transformation

The relationship between the two sets of modes is a Bogoliubov transformation:

$$p_i = \sum_j \left( \alpha_{ij} f_j + \beta_{ij} f_j^* \right)$$

where $\alpha_{ij}$ and $\beta_{ij}$ are the Bogoliubov coefficients. The number of particles in mode $i$ observed at $\mathscr{I}^+$ when the field is in the "in" vacuum is:

$$\langle 0_{\text{in}} | b_i^\dagger b_i | 0_{\text{in}} \rangle = \sum_j |\beta_{ij}|^2$$

If $\beta_{ij} \neq 0$, particles are created.

### The Geometric Optics Calculation

The crucial step is computing the Bogoliubov coefficients. Hawking uses a geometric optics (WKB) approximation, valid for high-frequency modes. The key idea:

An outgoing mode $p_\omega$ at $\mathscr{I}^+$ with frequency $\omega$ is traced backward in time. Near the horizon, it is exponentially blueshifted. As the mode is traced back through the collapsing star and out to $\mathscr{I}^-$, the relationship between the affine parameters on $\mathscr{I}^-$ and $\mathscr{I}^+$ is:

$$u = -\frac{1}{\kappa} \ln\left(\frac{v_0 - v}{\text{const}}\right)$$

where $u$ is the retarded time on $\mathscr{I}^+$, $v$ is the advanced time on $\mathscr{I}^-$, $v_0$ is the advanced time of the last ray that just avoids the horizon, and $\kappa$ is the surface gravity. This logarithmic relationship is the essence of the entire calculation.

A mode of frequency $\omega$ on $\mathscr{I}^+$ (with phase $e^{-i\omega u}$) maps to a mode on $\mathscr{I}^-$ with phase:

$$e^{-i\omega u} = e^{i(\omega/\kappa) \ln(v_0 - v)} = (v_0 - v)^{i\omega/\kappa}$$

This is defined for $v < v_0$. The Fourier transform of this function (to obtain the overlap with positive-frequency modes $e^{-i\omega' v}$ on $\mathscr{I}^-$) is:

$$\alpha_{\omega\omega'} \propto \int_0^{v_0} dv \, e^{i\omega' v} (v_0 - v)^{i\omega/\kappa}$$
$$\beta_{\omega\omega'} \propto \int_0^{v_0} dv \, e^{-i\omega' v} (v_0 - v)^{i\omega/\kappa}$$

### The Thermal Spectrum

The integrals can be evaluated by deforming the contour in the complex $v$ plane. The function $(v_0 - v)^{i\omega/\kappa}$ has a branch cut. Analytic continuation around the branch point at $v = v_0$ gives:

$$(v_0 - v)^{i\omega/\kappa} \to e^{-\pi\omega/\kappa} (v - v_0)^{i\omega/\kappa} \quad \text{for } v > v_0$$

This means:
$$|\beta_{\omega\omega'}|^2 = e^{-2\pi\omega/\kappa} |\alpha_{\omega\omega'}|^2$$

Using the normalization condition $\sum_j (|\alpha_{ij}|^2 - |\beta_{ij}|^2) = 1$ (from the canonical commutation relations), the expected number of particles at frequency $\omega$ is:

$$\langle N_\omega \rangle = \frac{1}{e^{2\pi\omega/\kappa} - 1}$$

This is the **Planck distribution** with temperature:

$$T = \frac{\hbar \kappa}{2\pi k_B}$$

For fermions, the same calculation with anticommutation relations gives:

$$\langle N_\omega \rangle = \frac{1}{e^{2\pi\omega/\kappa} + 1}$$

the Fermi--Dirac distribution at the same temperature.

### Greybody Factors

The above result is the number of particles emitted by the horizon. Not all of these escape to infinity -- some are scattered back by the effective potential barrier surrounding the black hole. For a Schwarzschild black hole, the effective potential for a scalar field of angular momentum $\ell$ is:

$$V_\ell(r) = \left(1 - \frac{2M}{r}\right)\left(\frac{\ell(\ell+1)}{r^2} + \frac{2M}{r^3}\right)$$

The transmission coefficient $\Gamma_\ell(\omega)$ (greybody factor) modifies the spectrum:

$$\langle N_\omega \rangle = \frac{\Gamma_\ell(\omega)}{e^{2\pi\omega/\kappa} - 1}$$

For $\omega \gg \kappa$ (high energy), $\Gamma \to 1$ and the spectrum is approximately thermal. For $\omega \ll \kappa$ (low energy), $\Gamma \ll 1$ and radiation is suppressed. The greybody factors break the exact thermality of the spectrum as seen at infinity, but the radiation emitted at the horizon is exactly thermal.

### The Density Matrix

Hawking also derives the thermal nature from a density matrix perspective. The quantum state on $\mathscr{I}^+$ is obtained by tracing over the modes that fall into the black hole (the $q_i$ modes). Since the total state $|0_{\text{in}}\rangle$ is a pure state, tracing over the interior modes gives a mixed state:

$$\rho_{\text{out}} = \text{Tr}_{\text{interior}} |0_{\text{in}}\rangle\langle 0_{\text{in}}|$$

This reduced density matrix is thermal:

$$\rho_{\text{out}} = \frac{1}{Z} e^{-\hat{H}/T_H}$$

where $\hat{H}$ is the Hamiltonian for the exterior modes and $T_H$ is the Hawking temperature. The entanglement between interior and exterior modes is the origin of the thermal state -- it is entanglement entropy.

### Back-Reaction

Hawking discusses but does not fully solve the back-reaction problem: as the black hole radiates, it loses mass, so the background geometry changes. He argues that for large black holes ($M \gg M_P$), the radiation rate is so slow that a quasi-static approximation is valid -- the geometry at any moment is well-approximated by a Schwarzschild black hole of the current mass. The luminosity is:

$$L \sim \frac{\hbar c^6}{15360 \pi G^2 M^2}$$

and the evaporation timescale is:
$$t_{\text{evap}} \sim \frac{5120 \pi G^2 M^3}{\hbar c^4}$$

The quasi-static approximation breaks down when $M \to M_P$, and a full quantum gravity calculation is needed for the endpoint.

---

## Physical Interpretation

### The Nature of Particle Creation

The particles are not being "pulled out" of the black hole. Rather, they are created by the time-dependent gravitational field. The collapsing geometry provides the energy for particle creation. In the language of quantum field theory, the vacuum state defined by the freely falling observer at early times contains particles as measured by the static observer at late times. The key is the exponential redshift between the two observers' time coordinates near the horizon.

### The Role of the Horizon

The horizon plays two essential roles:

1. **Infinite redshift**: It produces the logarithmic relationship $u \sim -\kappa^{-1} \ln(v_0 - v)$ that gives the thermal spectrum.
2. **Tracing over interior modes**: It divides the Hilbert space into accessible (exterior) and inaccessible (interior) sectors, making the exterior state mixed.

### Universality

The thermal spectrum depends only on $\kappa$ (and the spin of the emitted particle). It is independent of: the details of the collapse, the composition of the star, and the exact form of the field equations beyond the near-horizon region. This universality is why analogue models (sonic horizons in fluids) reproduce the Hawking effect.

---

## Impact and Legacy

### Fixes the Bekenstein--Hawking Entropy Coefficient

The precise temperature $T = \hbar\kappa/2\pi$ combined with the first law $dM = (\kappa/8\pi) dA$ fixes:

$$dM = T \cdot \frac{dA}{4\ell_P^2}$$

so $S = A / 4\ell_P^2$. Before Hawking's calculation, Bekenstein could only determine that $S \propto A / \ell_P^2$; the factor of $1/4$ was unknown.

### Motivates Quantum Gravity Programs

The incompleteness of the calculation at $M \to M_P$ (the endpoint problem) and the information loss problem (see 1976 paper) have been primary motivations for string theory, loop quantum gravity, and other quantum gravity programs.

### Trans-Planckian Problem

The modes that become Hawking radiation, when traced back to the horizon, have arbitrarily high frequencies at any finite time before they escape. This "trans-Planckian problem" raised concerns about the robustness of the calculation. Unruh (1995) and Corley and Jacobson (1996) showed that modifying the dispersion relation at high energies (as in a lattice or superfluid) does not change the thermal result, demonstrating universality.

---

## Connections to Modern Physics

1. **Bogoliubov transformations in condensed matter**: The same mathematical structure appears in BCS superconductivity (Bogoliubov--de Gennes), cosmological particle creation (parametric amplification), and dynamical Casimir effect.

2. **Entanglement structure**: The Hawking state is a thermofield double state, closely related to the structure used in the ER=EPR conjecture (Maldacena and Susskind, 2013). The entanglement between interior and exterior modes is the microscopic origin of the thermal spectrum.

3. **Page curve**: The entanglement entropy of the radiation grows linearly with time (each emitted quantum is entangled with the interior). Page (1993) showed that unitarity requires this entropy to eventually decrease (after the "Page time"). The island formula (2019) recovers the Page curve from semiclassical gravity.

4. **Firewall argument**: AMPS (2012) argued that after the Page time, the outgoing mode cannot be simultaneously entangled with the interior partner (as Hawking demands) and with the early radiation (as unitarity demands). This "monogamy of entanglement" leads to a "firewall" at the horizon. The island formula may resolve this.

5. **Experimental analogues**: Steinhauer's BEC experiment (2016, 2019) observed correlated phonon pairs across a sonic horizon, consistent with the Hawking prediction. The thermal nature remains to be definitively confirmed.

6. **For the exflation framework**: The Bogoliubov transformation formalism is identical to that used for particle creation during cosmological expansion. In the exflation scenario, the evolution of the internal space provides an additional source of mode mixing. The spectrum of created particles would depend on the rate of change of the internal geometry $\dot{\sigma}/\sigma$, potentially providing a distinctive signature.
