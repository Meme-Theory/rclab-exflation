# The Theory of Superfluidity of Helium II

**Author:** Lev Davidovich Landau
**Year:** 1941
**Journal:** J. Phys. USSR, 5, 71-90; also Zh. Eksp. Teor. Fiz., 11, 592 (1941)
**Nobel Prize:** 1962, "for his pioneering theories for condensed matter, especially liquid helium"

---

## 1. Historical Context and the Problem

### 1.1 The Lambda Transition

Helium-4, when cooled below T_lambda = 2.17 K at atmospheric pressure, undergoes a
phase transition to a state designated He II. This transition, named for the
lambda-shaped specific heat anomaly, produces a liquid with properties unlike any
other known substance:

- **Zero viscosity flow**: He II passes through capillaries of arbitrarily small
  diameter with no measurable pressure drop. Kapitza (1938) and Allen & Misener
  (1938) demonstrated this independently.
- **Thermomechanical effect**: A temperature difference across a superleak (fine
  porous plug) produces a pressure difference (fountain effect).
- **Anomalous thermal conductivity**: He II conducts heat orders of magnitude
  better than the best metallic conductors, yet this "conduction" is not
  diffusive -- it is convective.
- **Film flow**: He II creeps as a thin film over container walls, seemingly
  defying gravity.

### 1.2 The Theoretical Challenge

Prior to Landau's work, F. London (1938) had connected superfluidity to
Bose-Einstein condensation (BEC), noting that the lambda transition temperature
T_lambda ~ 2.17 K was close to the ideal BEC transition T_BEC ~ 3.13 K for
non-interacting bosons at liquid helium density. However, London's picture could
not explain the thermal properties, the two seemingly contradictory behaviors
(zero viscosity yet finite thermal effects), or the specific form of the
excitation spectrum.

Tisza (1938) proposed a two-fluid model on phenomenological grounds, but without
a microscopic justification for the excitation spectrum.

Landau's 1941 paper provided the definitive theoretical framework.

---

## 2. The Two-Fluid Model

### 2.1 Fundamental Postulate

Landau's central insight was to describe He II not as two interpenetrating
liquids (Tisza's picture) but as a single quantum liquid whose low-energy
excitations behave as a gas of quasi-particles moving through a ground-state
background. The total momentum and energy of the liquid are:

    E = E_0 + sum_i epsilon(p_i)
    P = sum_i p_i

where E_0 is the ground state energy and the sum runs over all excited
quasi-particles with dispersion relation epsilon(p).

### 2.2 Normal and Superfluid Components

At finite temperature T, the thermal excitations carry momentum and entropy.
The total density rho splits into:

    rho = rho_s(T) + rho_n(T)

where:
- **rho_s** = superfluid density. Carries zero entropy, zero viscosity. The
  ground state condensate plus quantum depletion. At T = 0, rho_s = rho.
- **rho_n** = normal fluid density. Carried by the gas of thermal excitations.
  Has finite viscosity, carries all the entropy. At T = T_lambda, rho_n = rho.

The two "fluids" are not physically separable -- they represent two aspects of
the same quantum liquid's behavior. The superfluid component is the collective
ground state; the normal component is the ensemble of excited quasi-particles.

### 2.3 Two-Fluid Hydrodynamic Equations

The linearized two-fluid equations are:

    d(rho)/dt + div(j) = 0                          (mass conservation)
    j = rho_s * v_s + rho_n * v_n                    (total current)
    d(v_s)/dt = -grad(mu/m)                          (superfluid: irrotational)
    rho_n * d(v_n)/dt = -rho_n/rho * grad(P) + eta * laplacian(v_n) - rho_s * s * grad(T)
    d(s)/dt + s * div(v_n) = 0                       (entropy carried by normal fluid only)

Key constraint: the superfluid velocity is irrotational:

    curl(v_s) = 0

This follows from v_s = (hbar/m) * grad(phi), where phi is the phase of the
macroscopic wavefunction.

---

## 3. The Excitation Spectrum

### 3.1 Phonons

At low momenta, the excitations are sound quanta -- phonons -- with a linear
dispersion:

    epsilon(p) = c * p      (for p -> 0)

where c is the speed of (first) sound in He II, approximately 238 m/s. These
are longitudinal density oscillations of the liquid, identical in character to
sound waves in any fluid but quantized.

### 3.2 Rotons

Landau postulated that at higher momenta, the dispersion curve epsilon(p)
has a local minimum at a finite momentum p_0. Near this minimum:

    epsilon(p) = Delta + (p - p_0)^2 / (2 * mu*)

where:
- Delta = the roton energy gap
- p_0 = the roton momentum
- mu* = the effective mass at the roton minimum

Landau's 1941 estimates: Delta/k_B ~ 9.6 K, p_0/hbar ~ 2 A^{-1}.

### 3.3 The Full Dispersion Curve

The complete dispersion relation epsilon(p) has the shape:

    p = 0:     epsilon = 0 (ground state)
    low p:     epsilon = c*p (phonon branch, linear)
    p ~ p_1:   epsilon reaches a local maximum (the "maxon" peak)
    p = p_0:   epsilon reaches a local minimum Delta (the "roton" minimum)
    p > p_0:   epsilon increases again

This non-monotonic dispersion curve was confirmed experimentally by neutron
scattering (Henshaw & Woods, 1961), providing spectacular validation of
Landau's 1941 prediction.

### 3.4 Microscopic Origin

Landau did not provide a microscopic derivation of the roton minimum. This
came later:
- Feynman (1954): rotons as quantized vortex rings or backflow excitations
- Feynman & Cohen (1956): backflow-corrected wavefunctions reproduce the minimum
- Modern view: rotons reflect the short-range correlations (local order) of the
  liquid, with p_0 ~ 2*pi/d where d is the mean interparticle spacing

---

## 4. The Landau Critical Velocity

### 4.1 Derivation

Consider the superfluid flowing with velocity v past a stationary wall. In the
fluid rest frame, the wall moves with velocity -v. An excitation with momentum p
and energy epsilon(p) can be created only if the total energy in the lab frame
decreases:

    epsilon(p) - p . v < 0

This requires:

    v > epsilon(p) / p

for some p. The minimum velocity at which excitations can be created is:

    v_c = min_p [ epsilon(p) / p ]

This is the **Landau critical velocity**. Below v_c, the superfluid cannot
transfer energy to the walls -- it flows without dissipation.

### 4.2 Geometric Interpretation

On the epsilon-p plot, v_c is the slope of the line from the origin that is
tangent to the dispersion curve. For the phonon branch, epsilon/p = c (constant),
so v_c <= c. For the roton minimum:

    v_c = Delta / p_0

With Landau's parameters: v_c ~ Delta / p_0 ~ 60 m/s.

### 4.3 The Critical Velocity Problem

Experimentally, observed critical velocities are much lower (typically ~1 cm/s
to ~1 m/s) than Landau's prediction. This is because:
- Quantized vortices (Onsager 1949, Feynman 1955) provide lower-energy
  excitations not in Landau's original spectrum
- Vortex nucleation at surfaces limits v_c in practice
- The Landau criterion applies to the intrinsic spectrum; real flow includes
  topological excitations

---

## 5. Second Sound

### 5.1 Prediction

Landau predicted a second mode of sound propagation in He II. Ordinary (first)
sound is a density wave where rho_s and rho_n oscillate in phase:

    first sound:  delta(rho) != 0,  delta(T) ~ 0
    velocity:     u_1 = sqrt(dP/d(rho))_s ~ 238 m/s

Second sound is an entropy-temperature wave where rho_s and rho_n oscillate
out of phase, with total density nearly constant:

    second sound:  delta(rho) ~ 0,  delta(T) != 0
    velocity:      u_2 = sqrt(rho_s * s^2 * T / (rho_n * c_p))

At low T (where rho_n << rho): u_2 -> u_1 / sqrt(3) (phonon gas result).
At T -> T_lambda (where rho_s -> 0): u_2 -> 0.

### 5.2 Experimental Confirmation

Peshkov (1944, 1946) detected second sound experimentally, confirming Landau's
prediction. The measured velocity agreed quantitatively with the two-fluid
prediction over the full temperature range 0 < T < T_lambda.

Second sound is unique to superfluids. It has no analog in classical fluids
where entropy is carried by the bulk flow.

---

## 6. Quantized Circulation

### 6.1 Onsager-Feynman Quantization

Although not in the 1941 paper, the two-fluid framework leads directly to
quantized circulation. Since v_s = (hbar/m) * grad(phi) and phi must be
single-valued modulo 2*pi:

    oint v_s . dl = n * kappa,    kappa = h / m_He = 9.97 x 10^{-4} cm^2/s

where n is an integer. This was predicted by Onsager (1949) and Feynman (1955)
and confirmed experimentally by Vinen (1961) and Rayfield & Reif (1964).

### 6.2 Quantized Vortices

The irrotationality constraint curl(v_s) = 0 can be satisfied everywhere
except on singular lines -- quantized vortex filaments. Around each vortex:

    v_s(r) = kappa / (2 * pi * r)

The vortex core has size ~ xi (the healing length, ~1 A in He-4), inside which
the superfluid density drops to zero. These vortices carry the angular momentum
of the superfluid and form lattice structures under rotation (analogous to
Abrikosov flux lattices in type-II superconductors).

---

## 7. Thermodynamic Properties

### 7.1 Specific Heat

The phonon contribution to the specific heat:

    C_phonon = (2 * pi^2 / 15) * k_B * (k_B * T / (hbar * c))^3

This gives C ~ T^3 at low temperature (Debye law for the phonon gas).

The roton contribution:

    C_roton ~ (Delta / (k_B * T))^2 * exp(-Delta / (k_B * T)) * [roton density of states]

The total C(T) shows the lambda anomaly at T_lambda, which Landau's theory
describes as the temperature where the excitation gas becomes so dense that
the quasi-particle picture breaks down.

### 7.2 Normal Fluid Density

From the phonon and roton gases:

    rho_n(T) = rho_n^{phonon}(T) + rho_n^{roton}(T)

    rho_n^{phonon} = (2 * pi^2) / (45) * (k_B * T)^4 / (rho * hbar^3 * c^5)

    rho_n^{roton} = (2/3) * p_0^2 * n_roton(T) / (k_B * T)

where n_roton(T) ~ exp(-Delta / (k_B * T)) is the roton number density.

Andronikashvili's torsional oscillator experiments (1946) measured rho_n(T)
directly and found excellent agreement with Landau's predictions.

---

## 8. Limitations and Later Developments

### 8.1 What Landau Got Right
- The two-fluid model: quantitatively correct
- The phonon dispersion: exact (by definition -- it is sound)
- The roton minimum: confirmed by neutron scattering
- Second sound: confirmed by Peshkov
- The critical velocity criterion: correct for the intrinsic spectrum

### 8.2 What Required Modification
- The roton parameters needed adjustment (see 1947 sequel paper)
- Quantized vortices were not included (Onsager/Feynman)
- The connection to BEC was deliberately avoided by Landau but is now understood
  to be essential (Penrose-Onsager criterion for ODLRO)
- The lambda transition itself is now understood as a BEC transition of the
  interacting system, not a quasi-particle gas breakdown

### 8.3 The BEC Connection

Landau explicitly rejected the BEC interpretation, insisting that the
excitation spectrum alone (without reference to a condensate wavefunction)
was sufficient. History has shown that both perspectives are needed:
- Landau's quasi-particle picture: correct for thermodynamics and transport
- London's BEC picture: correct for the order parameter, phase coherence,
  quantized circulation, and the connection to the GPE

---

## 9. Connection to Phonon-Exflation Cosmology

### 9.1 The Prototype System

The superfluidity of He II is THE physical prototype for the phonon-exflation
framework. The structural parallels are:

| He II Property | Phonon-Exflation Analog |
|:---------------|:------------------------|
| BEC ground state | Vacuum condensate on M4 x K |
| Phonon excitations (linear) | Massless gauge bosons (gluons, photon) |
| Roton minimum (gapped) | Massive particle modes (W, Z, fermions) |
| Superfluid component | Vacuum (zero entropy, coherent) |
| Normal component | Thermal particle bath |
| Healing length xi | Compactification scale l_K |
| Two-fluid model | Vacuum + matter decomposition |
| Second sound | Coupled metric-matter oscillations |
| Quantized vortices | Topological defects (monopoles, strings) |

### 9.2 The Dispersion Relation as Mass Spectrum

The phonon-exflation claim is that the particle mass spectrum m_i arises from
the dispersion relation of excitations on M4 x K, exactly as the phonon-roton
spectrum arises from excitations in He II. The Dirac operator D_K on the
internal space K = SU(3) plays the role of the dynamical
matrix that determines epsilon(p).

The roton minimum at finite momentum p_0 maps to: massive KK modes at nonzero
KK quantum numbers. Just as rotons carry definite crystal momentum p_0, massive
particles carry definite internal quantum numbers (hypercharge, isospin, color).

### 9.3 Landau Critical Velocity and Vacuum Stability

The Landau critical velocity v_c = min(epsilon/p) has a direct cosmological
analog: the vacuum is stable against spontaneous particle creation as long as
the "flow velocity" (expansion rate) is below the critical threshold set by
the lightest excitation gap. This connects to:
- The cosmological particle creation rate during exflation
- The freeze-out condition for relic abundances
- The D/H ratio mechanism in the GPE simulation

### 9.4 The GPE Simulation

The GPE equation solved in `phonon-exflation-sim/` is:

    i * hbar * d(Psi)/dt = [-hbar^2/(2m) * laplacian + V_ext + g * |Psi|^2] * Psi

This is exactly the equation whose linearized excitations give the Bogoliubov
spectrum -- the quantum-corrected version of Landau's phonon-roton curve. The
simulation's healing length xi = hbar / sqrt(2 * m * g * n_0) plays the role
of the internal compactification scale, and the phonon speed c = sqrt(g*n_0/m)
sets the "speed of light" for the emergent relativistic dynamics.

---

## 10. Summary

Landau's 1941 paper established:

1. The two-fluid model of He II as ground state + quasi-particle gas
2. The phonon-roton dispersion relation epsilon(p)
3. The Landau critical velocity v_c = min(epsilon/p)
4. Second sound as an entropy wave
5. Quantitative predictions for thermodynamic properties

This work, recognized by the 1962 Nobel Prize, remains the foundation of our
understanding of quantum fluids. For phonon-exflation cosmology, it provides
the physical prototype: a system where the "particles" (phonons, rotons) are
collective excitations of a coherent ground state, their properties determined
entirely by the excitation spectrum of the medium rather than by fundamental
point-particle ontology.

---

## References

- L.D. Landau, "The Theory of Superfluidity of Helium II," J. Phys. USSR 5, 71 (1941)
- P.L. Kapitza, "Viscosity of Liquid Helium below the Lambda-Point," Nature 141, 74 (1938)
- F. London, "The Lambda-Phenomenon of Liquid Helium and the Bose-Einstein Degeneracy," Nature 141, 643 (1938)
- L. Tisza, "Transport Phenomena in Helium II," Nature 141, 913 (1938)
- V. Peshkov, "Second Sound in Helium II," J. Phys. USSR 8, 381 (1944)
- L. Onsager, "Statistical Hydrodynamics," Nuovo Cimento Suppl. 6, 279 (1949)
- R.P. Feynman, "Atomic Theory of the Two-Fluid Model of Liquid Helium," Phys. Rev. 94, 262 (1954)
- D.G. Henshaw, A.D.B. Woods, "Modes of Atomic Motions in Liquid Helium by Inelastic Scattering of Neutrons," Phys. Rev. 121, 1266 (1961)
