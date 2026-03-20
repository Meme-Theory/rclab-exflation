# On the Anomalous Absorption of Sound Near Second-Order Phase Transitions

**Authors:** Lev Landau, Isaak Khalatnikov
**Year:** 1954
**Journal:** Doklady Akad. Nauk SSSR, 96, 469-472

---

## 1. Historical Context and the Problem

By the early 1950s, Landau's 1937 theory of second-order phase transitions had become
the standard framework for understanding continuous symmetry breaking in condensed matter.
The thermodynamic theory -- based on expanding the free energy F(phi, T) in powers of the
order parameter phi -- successfully described the equilibrium behavior near critical points:
the spontaneous magnetization of ferromagnets, the superfluid transition in He-4, the
ferroelectric ordering in BaTiO3, and the superconducting transition.

However, the equilibrium theory said nothing about dynamics. Experimentally, a striking
anomaly had been observed: the absorption of ultrasound passing through a material
increased dramatically as the temperature approached the critical temperature T_c of a
second-order phase transition. The absorption coefficient could increase by orders of
magnitude in a narrow temperature window around T_c, far exceeding any prediction from
standard acoustic theory.

This anomalous absorption was observed in:
- Liquid helium near the lambda point (T_lambda = 2.17 K)
- Ferroelectrics near the Curie temperature
- Order-disorder transitions in alloys (e.g., beta-brass)
- Magnetic systems near the Curie/Neel temperature

The question was fundamental: what mechanism couples sound waves to the order parameter,
and why does this coupling become catastrophically strong at T_c?


## 2. The Landau-Khalatnikov Kinetic Equation

Landau and Khalatnikov's insight was to write a kinetic equation governing how the order
parameter phi relaxes toward its equilibrium value. The key assumption is that the
relaxation is overdamped -- inertial terms are negligible, and phi evolves by gradient
descent on the free energy landscape:

```
d(phi)/dt = -(1/tau_0) * (dF/dphi)
```

where:
- phi is the order parameter (scalar, vector, or tensor depending on the transition)
- F(phi, T) is the Landau free energy functional
- tau_0 is a microscopic relaxation time (material-dependent, typically 10^{-10} to 10^{-13} s)
- dF/dphi is the thermodynamic force driving phi toward equilibrium

This is the Landau-Khalatnikov (LK) equation, also called the time-dependent
Ginzburg-Landau (TDGL) equation in later literature.

For the standard Landau expansion:

```
F(phi) = F_0 + (1/2) * a * (T - T_c) * phi^2 + (1/4) * b * phi^4
```

the thermodynamic force is:

```
dF/dphi = a * (T - T_c) * phi + b * phi^3
```

In the disordered phase (T > T_c), the equilibrium is phi_eq = 0. A small perturbation
delta_phi relaxes as:

```
d(delta_phi)/dt = -(1/tau_0) * a * (T - T_c) * delta_phi
```

giving exponential relaxation:

```
delta_phi(t) = delta_phi(0) * exp(-t/tau)
```

with the effective relaxation time:

```
tau = tau_0 / (a * (T - T_c))
```


## 3. Critical Slowing Down

The central prediction of the LK equation is immediate and dramatic: the effective
relaxation time tau DIVERGES as T -> T_c:

```
tau = tau_0 / (a * |T - T_c|)  ~  |T - T_c|^{-1}
```

This is critical slowing down. As the system approaches the phase transition, the free
energy landscape flattens near phi = 0 (the curvature d^2F/dphi^2 = a(T - T_c) vanishes),
and the restoring force driving phi back to equilibrium weakens. The order parameter
fluctuates more and more sluggishly, taking longer and longer to respond to perturbations.

In mean-field theory, the critical slowing exponent is 1:

```
tau ~ |T - T_c|^{-nu*z}
```

where nu is the correlation length exponent (nu = 1/2 in mean field) and z is the dynamic
critical exponent (z = 2 for diffusive/relaxational dynamics in the LK equation). Thus
nu*z = 1 in mean field.

Beyond mean field, critical fluctuations modify both nu and z. For the 3D Ising
universality class:
- nu ~ 0.63
- z ~ 2.02 (Model A dynamics, non-conserved order parameter)
- nu*z ~ 1.27

The divergence of tau means that near T_c, the order parameter cannot follow rapid
perturbations -- it falls "out of step" with any driving force that oscillates faster than
1/tau.


## 4. Sound Absorption Mechanism

A sound wave passing through a medium creates periodic compressions and rarefactions --
oscillating pressure and density. In a system near a phase transition, the local
thermodynamic state (and hence the local T_c) oscillates with the sound wave. The order
parameter attempts to track these oscillations, adjusting phi to its local equilibrium
value at each point in the pressure cycle.

At temperatures far from T_c, the relaxation time tau is short compared to the sound
period 1/omega, and phi tracks the oscillation adiabatically. Energy is temporarily stored
in the order parameter and returned to the sound wave each cycle, with minimal dissipation.

Near T_c, however, tau becomes comparable to or exceeds 1/omega. The order parameter lags
behind the sound oscillation, and this phase lag dissipates energy. The sound wave loses
energy to irreversible relaxation of phi, and the sound is absorbed.

The absorption coefficient alpha (energy attenuation per unit length) is:

```
alpha = (omega^2 * tau) / (2 * rho * c^3) * |dT_c/dP|^2 * C_p * (T - T_c)
```

where:
- omega is the angular frequency of the sound
- rho is the density
- c is the sound speed
- dT_c/dP is the pressure dependence of the critical temperature
- C_p is the specific heat

In the regime omega * tau << 1 (low frequency or far from T_c):

```
alpha ~ omega^2 * tau
```

This is the relaxation absorption regime. Since tau ~ |T - T_c|^{-1}, the absorption
diverges as T -> T_c.

In the regime omega * tau >> 1 (high frequency or very close to T_c):

```
alpha ~ 1/tau ~ |T - T_c|
```

The absorption actually DECREASES very close to T_c because the order parameter cannot
respond at all -- it is effectively frozen. The peak absorption occurs at omega * tau ~ 1.


## 5. The Fluctuation-Dissipation Connection

The LK equation encodes a deep connection between fluctuations and dissipation. Through
the fluctuation-dissipation theorem (which Landau's school formalized in Landau and
Lifshitz, "Statistical Physics"), the same relaxation time tau that governs dissipation
also controls the thermal fluctuation spectrum:

```
<|delta_phi(omega)|^2> = (2 * k_B * T * tau) / (1 + omega^2 * tau^2) * (1/V) * (d^2F/dphi^2)^{-1}
```

The spectral weight of order parameter fluctuations is Lorentzian with width 1/tau.
As T -> T_c, both the amplitude (d^2F/dphi^2 -> 0) and the characteristic time (tau -> inf)
diverge, producing the familiar critical opalescence and anomalous scattering.

Sound absorption is then understood as the ORDER PARAMETER CHANNEL of the fluctuation
spectrum coupling to the DENSITY CHANNEL through the thermodynamic derivative dT_c/dP.
The sound wave excites order parameter fluctuations, which relax irreversibly.


## 6. Spatial Generalization: The TDGL Equation

Landau and Khalatnikov treated phi as spatially uniform. The natural generalization
includes spatial gradients, giving the time-dependent Ginzburg-Landau (TDGL) equation:

```
tau_0 * d(phi)/dt = -dF/dphi + kappa * nabla^2(phi) + eta(x,t)
```

where:
- kappa * nabla^2(phi) is the gradient energy (Ginzburg term), penalizing spatial
  variations in phi
- eta(x,t) is a Langevin noise term satisfying the fluctuation-dissipation relation:
  <eta(x,t) * eta(x',t')> = 2 * k_B * T * tau_0 * delta(x-x') * delta(t-t')

This equation describes:
- Relaxation of the uniform order parameter (k = 0 mode)
- Diffusion of order parameter fluctuations (k != 0 modes): tau_k = tau_0/(a|T-T_c| + kappa*k^2)
- Domain wall motion after a quench through T_c
- Nucleation and growth dynamics

The TDGL equation is the foundation of dynamic critical phenomena for non-conserved order
parameters (Hohenberg-Halperin Model A).


## 7. Mode-Coupling and Beyond Mean Field

The LK/TDGL theory is a mean-field dynamic theory. It correctly identifies the mechanism
of critical slowing down but gets the wrong exponents near T_c in 3D due to critical
fluctuations.

The mode-coupling theory, developed by Kawasaki (1967-1970) and systematized by Halperin
and Hohenberg (1969-1977), goes beyond LK by including the nonlinear coupling between
the order parameter and other slow modes (conserved densities, currents).

The Hohenberg-Halperin classification defines dynamic universality classes:
- **Model A**: Non-conserved order parameter, no coupling to conserved densities. z = 2+eta.
- **Model B**: Conserved order parameter (e.g., binary alloy). z = 4-eta.
- **Model C**: Non-conserved OP coupled to conserved energy density. z depends on specific
  heat exponent alpha.
- **Model E/F**: Superfluid He-4 (OP is complex, current is conserved). z ~ 3/2.
- **Model H**: Liquid-gas critical point (OP couples to momentum). z ~ 3.

For sound absorption, the relevant coupling is between the order parameter (Model A or C)
and the sound mode (longitudinal phonon = density fluctuation). The mode-coupling
contribution produces:

```
alpha_sound ~ |T - T_c|^{-alpha_heat}    (singular part, Model C)
```

where alpha_heat is the specific heat critical exponent. This is weaker than the mean-field
LK prediction but still divergent.


## 8. Experimental Confirmation

The LK prediction of anomalous sound absorption has been confirmed in numerous systems:

**Liquid Helium (lambda transition)**:
- Absorption peaks sharply at T_lambda = 2.172 K
- Frequency dependence omega^2 confirmed for omega*tau << 1
- Dynamic scaling verified: alpha/omega^2 = f(omega * xi^z) with z ~ 1.5

**Ferroelectrics (BaTiO3, SrTiO3)**:
- Ultrasound absorption shows sharp peak at Curie temperature
- tau estimated at ~10^{-11} s far from T_c, diverging to ~10^{-8} s near T_c

**Magnetic transitions**:
- Ultrasound attenuation in MnF2, FeF2 near Neel temperature
- Spin-phonon coupling mechanism as predicted by LK

**Superconductors**:
- Ultrasound absorption shows sharp drop below T_c (BCS gap opening)
- The LK equation becomes the Ginzburg-Landau equation for the superconducting order
  parameter near T_c

The quantitative agreement is best in mean-field systems (long-range interactions,
high dimensionality, or Ginzburg criterion satisfied). In strongly fluctuating 3D systems,
mode-coupling corrections are necessary.


## 9. The Dynamic Critical Exponent z

The LK equation introduced the concept that dynamics near phase transitions has its own
universality, characterized by the dynamic critical exponent z:

```
tau ~ xi^z
```

where xi ~ |T - T_c|^{-nu} is the correlation length. Combined with nu*z governing the
relaxation time divergence:

```
tau ~ |T - T_c|^{-nu*z}
```

The value of z depends on:
- Whether the order parameter is conserved (z = 4-eta) or non-conserved (z = 2+eta)
- Whether there are mode-coupling effects with other slow variables
- The dimensionality and symmetry of the system

Representative values:
- Model A (non-conserved, 3D Ising): z ~ 2.02
- Model B (conserved, 3D Ising): z ~ 3.75
- Superfluid He-4 (Model E): z ~ 3/2
- Liquid-gas (Model H): z ~ 3

Dynamic universality is a richer structure than static universality. Systems with
identical static critical exponents can have different dynamic exponents if their
conservation laws differ.


## 10. Relation to the Gross-Pitaevskii Equation

The TDGL equation has a direct algebraic relationship to the Gross-Pitaevskii equation
(GPE) used in superfluid/BEC dynamics. The GPE for a complex order parameter psi:

```
i * hbar * d(psi)/dt = -(hbar^2/(2m)) * nabla^2(psi) + V(x)*psi + g*|psi|^2*psi
```

is a HAMILTONIAN (energy-conserving) evolution. The TDGL equation for the same psi:

```
tau_0 * d(psi)/dt = (hbar^2/(2m)) * nabla^2(psi) - V(x)*psi - g*|psi|^2*psi + eta
```

is a DISSIPATIVE (energy-minimizing) evolution.

The two are related by the substitution t -> -i*t (Wick rotation). GPE dynamics conserve
energy and particle number; TDGL dynamics minimize free energy while thermal noise
maintains fluctuations.

In practice, condensed matter systems exhibit both:
- GPE dynamics at T << T_c (deep in the ordered phase, coherent)
- TDGL dynamics near T_c (dissipative, fluctuation-dominated)
- A crossover described by the stochastic GPE (SGPE) or projected GPE (PGPE)

The LK insight that relaxation TOWARD equilibrium is governed by dF/dphi is the
dissipative complement to Hamiltonian dynamics governed by dF/dphi through Poisson
brackets.


## 11. Connection to Phonon-Exflation Framework

The Landau-Khalatnikov relaxation equation bears a structural relationship to the dynamics
of the phonon-exflation framework at several levels:

**TDGL and the GPE simulation**: The GPE solver in `phonon-exflation-sim/` implements
Hamiltonian evolution of a complex order parameter psi on a 2D grid, with expansion
encoded through a time-dependent scale factor R(t). The dissipative counterpart -- the
TDGL/LK equation -- governs the approach to the V_eff minimum in the moduli space
coordinate s. The GPE handles the fast (phonon) degrees of freedom; the LK equation
handles the slow (moduli) degree of freedom.

**Critical slowing down at the V_eff minimum**: If V_eff(s) has a minimum at s_0, then
small deviations delta_s relax with a timescale:

```
tau_s ~ 1 / V_eff''(s_0)
```

If V_eff''(s_0) is small (shallow minimum), the modulus s relaxes slowly -- critical
slowing down in moduli space. This determines the duration of the exflation transition
and the number of e-folds of spectral expansion.

**Sound absorption as phonon dissipation**: In the condensed matter context, sound
absorption near T_c means phonon energy is being converted to order parameter fluctuations.
In the exflation context, phonon modes on M4 x SU(3) couple to the Jensen deformation
parameter s. As s evolves toward s_0, phonon modes are created and destroyed (the spectrum
reshuffles). The rate of phonon production is governed by the same LK relaxation physics.

**Dynamic universality**: The Hohenberg-Halperin classification suggests that the dynamics
of the exflation transition belongs to a specific universality class determined by:
- Whether s is conserved or non-conserved (non-conserved -> Model A)
- Whether s couples to conserved currents (energy-momentum -> Model C or H)
- The dimensionality of the effective theory

The phonon freeze-out criterion H(t) ~ c_s/d_mean, which determines when phonon
pairs decouple from the expanding condensate, is the cosmological analog of the
omega*tau ~ 1 condition that determines peak sound absorption in the LK theory. Both mark
the boundary between adiabatic tracking and frozen-out dynamics.


## 12. Legacy

The Landau-Khalatnikov 1954 paper, though only four pages in Doklady, established:

1. The kinetic equation for order parameter dynamics (now the TDGL equation)
2. Critical slowing down as a universal phenomenon near phase transitions
3. The mechanism of anomalous sound absorption through order parameter relaxation
4. The relaxation time as a fundamental dynamic quantity, complementing the static
   critical exponents

These ideas became the foundation for the modern theory of dynamic critical phenomena,
culminating in the Hohenberg-Halperin classification (1977) and the renormalization group
treatment of dynamics by De Dominicis, Peliti, and others.

The LK equation remains the starting point for understanding non-equilibrium dynamics
near continuous phase transitions and, through its connection to the TDGL/GPE framework,
provides the dynamical language for condensed matter cosmology.

---

**Key equations:**
- LK relaxation: d(phi)/dt = -(1/tau) * (dF/dphi)
- Critical slowing: tau ~ |T - T_c|^{-nu*z}
- Sound absorption: alpha ~ omega^2 * tau / c (relaxation regime)
- Dynamic scaling: tau ~ xi^z (defining the dynamic critical exponent)
