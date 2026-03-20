# The Theory of a Fermi Liquid

**Author:** Lev Landau
**Year:** 1956
**Journal:** Zh. Eksp. Teor. Fiz., 30, 1058-1064 (Sov. Phys. JETP, 3, 920-925)

---

## 1. The Problem of Strongly Interacting Fermions

By the mid-1950s, a fundamental puzzle confronted condensed matter theory. The free
electron model of metals -- treating conduction electrons as non-interacting fermions in a
periodic potential -- was spectacularly successful. It correctly predicted the linear
specific heat at low temperatures, the Pauli paramagnetism, the existence of a Fermi
surface, and the basic transport properties of metals. Yet the model's central assumption
was manifestly wrong: electrons interact via the Coulomb repulsion e^2/r, with interaction
energies comparable to the kinetic energy. For a typical metal, the ratio of interaction
energy to kinetic energy (the Wigner-Seitz parameter r_s) is 2-5, firmly in the
strongly-interacting regime.

The same puzzle appeared in nuclear physics. The nuclear shell model treated nucleons as
independent particles in a mean-field potential, and it worked -- predicting magic numbers,
spin-orbit splittings, magnetic moments. Yet nucleons interact through the strong nuclear
force at distances of order 1 fm, with binding energies of ~8 MeV per nucleon.

Why do non-interacting models work for strongly interacting systems?

Landau's 1956 paper answered this question with an idea of extraordinary depth and
generality: the low-energy excitations of an interacting Fermi system are quasiparticles
-- entities that are in one-to-one correspondence with the excitations of the free Fermi
gas, carry the same quantum numbers (charge, spin, momentum), but have renormalized
properties (effective mass, lifetime, interactions).


## 2. Adiabatic Continuity

The foundational principle of Fermi liquid theory is adiabatic continuity. Consider a
system of N non-interacting fermions filling a Fermi sea up to the Fermi momentum k_F.
The ground state is the filled Fermi sphere; the excited states are particle-hole
excitations (a fermion promoted from below k_F to above k_F).

Now imagine turning on the interaction slowly -- adiabatically -- so that the system
remains in its ground state (or, more precisely, tracks a low-lying eigenstate
continuously). Landau's assumption is that the eigenstates of the interacting system evolve
continuously from those of the non-interacting system. There is a one-to-one mapping:

```
|non-interacting state> --> |interacting state>
```

This means:
- The ground state of the interacting system evolves from the filled Fermi sphere
- An excited state with one particle above k_F and one hole below k_F evolves into a
  state with one quasiparticle above k_F and one quasihole below k_F
- The Fermi surface survives the interaction (Luttinger's theorem: the volume enclosed
  by the Fermi surface is unchanged by interactions)

Adiabatic continuity does NOT mean the interactions are weak. It means the interactions
do not cause a phase transition -- the interacting ground state is continuously connected
to the non-interacting one. If a phase transition intervenes (superconductivity,
magnetism, charge density wave), the adiabatic connection breaks and Fermi liquid theory
fails.

The quasiparticle is NOT a bare electron. It is a bare electron "dressed" by a cloud of
particle-hole excitations -- a collective entity involving the correlated motion of many
electrons. But it carries the same quantum numbers as the bare electron and, near the
Fermi surface, behaves as a well-defined excitation with a long lifetime.


## 3. Quasiparticle Properties

**Effective mass m***: The quasiparticle dispersion near the Fermi surface is:

```
epsilon_k = epsilon_F + (hbar * k_F / m*) * (|k| - k_F)
```

where m* is the effective mass. The ratio m*/m encodes the effect of interactions on the
single-particle spectrum. Typical values:
- Liquid He-3: m*/m ~ 3-6 (strongly enhanced)
- Normal metals: m*/m ~ 1-3
- Heavy fermion systems: m*/m ~ 100-1000
- Nuclear matter: m*/m ~ 0.7 (reduced by nuclear attraction)

The effective mass determines the density of states at the Fermi level:

```
N(0) = m* * k_F / (pi^2 * hbar^2)
```

and hence the linear specific heat coefficient:

```
gamma = (pi^2 / 3) * k_B^2 * N(0) = (m*/m) * gamma_free
```

This is why the free electron model works for thermodynamics: the effect of interactions
is absorbed into a single parameter m*.

**Quasiparticle lifetime**: A quasiparticle with energy epsilon above the Fermi level has
a finite lifetime due to scattering. Landau showed that the decay rate is:

```
1/tau ~ (epsilon - epsilon_F)^2
```

This quadratic dependence is a consequence of phase space restrictions: a quasiparticle
near the Fermi surface can only scatter into states that are (a) above the Fermi level and
(b) have a partner hole below the Fermi level. Both conditions restrict the available phase
space, and the product gives the (epsilon - epsilon_F)^2 scaling.

At the Fermi surface itself (epsilon = epsilon_F), the lifetime is infinite: the
quasiparticle is an exact eigenstate. This is why the quasiparticle picture becomes exact
in the limit of low temperatures and low excitation energies.

**Quasiparticle weight Z**: The quasiparticle is not a sharp delta-function peak in the
spectral function but carries a weight Z < 1:

```
A(k, omega) = Z * delta(omega - epsilon_k/hbar) + A_incoherent(k, omega)
```

where Z is the quasiparticle residue (0 < Z <= 1) and A_incoherent is a smooth
incoherent background. Z = 1 for free fermions; Z < 1 for interacting systems. In liquid
He-3, Z ~ 0.3.


## 4. The Landau Energy Functional

Landau's key formal construction is the energy functional. The total energy of the system
is expressed as a functional of the quasiparticle distribution function n_k_sigma
(occupation number of state k with spin sigma):

```
E[n] = E_0 + sum_k,sigma epsilon_k^0 * delta_n_k_sigma
       + (1/2V) * sum_{k,sigma,k',sigma'} f(k,sigma; k',sigma') * delta_n_k_sigma * delta_n_k'_sigma'
```

where:
- E_0 is the ground state energy
- epsilon_k^0 is the quasiparticle energy in the ground state
- delta_n_k_sigma = n_k_sigma - n_k_sigma^0 is the deviation from equilibrium
- f(k,sigma; k',sigma') is the Landau interaction function
- V is the volume

The quasiparticle energy is defined as the functional derivative:

```
epsilon_k_sigma = delta(E) / delta(n_k_sigma) = epsilon_k^0 + (1/V) * sum_{k',sigma'} f(k,sigma; k',sigma') * delta_n_k'_sigma'
```

This is the crucial point: the energy of a quasiparticle DEPENDS ON THE DISTRIBUTION of
all other quasiparticles. This is the residual interaction between quasiparticles, and it
is what makes Fermi liquid theory more than just a free-particle model with a renormalized
mass.


## 5. Landau Parameters

For an isotropic Fermi liquid (like He-3), the interaction function f depends only on the
angle theta between k and k' (both on the Fermi surface) and on the spin indices. It can
be decomposed:

```
f(k,sigma; k',sigma') = f^s(theta) + f^a(theta) * sigma . sigma'
```

where f^s is the spin-symmetric (density-density) interaction and f^a is the
spin-antisymmetric (spin-spin) interaction. Expanding in Legendre polynomials:

```
f^{s,a}(theta) = sum_l  f_l^{s,a} * P_l(cos(theta))
```

The dimensionless Landau parameters are defined as:

```
F_l^{s,a} = N(0) * f_l^{s,a}
```

where N(0) is the density of states at the Fermi level.

These parameters encode all the thermodynamic and transport properties of the Fermi liquid:

**Effective mass:**
```
m*/m = 1 + F_1^s / 3
```

**Compressibility:**
```
kappa / kappa_free = (m*/m) / (1 + F_0^s)
```

**Spin susceptibility:**
```
chi / chi_free = (m*/m) / (1 + F_0^a)
```

**First sound velocity:**
```
c_1^2 = (k_F^2 / (3 * m * m*)) * (1 + F_0^s)
```

**Wilson ratio (specific heat / susceptibility):**
```
R_W = 1 / (1 + F_0^a)
```


## 6. Pomeranchuk Stability Conditions

Not all values of the Landau parameters correspond to stable Fermi liquids. Pomeranchuk
(1958) derived the conditions for stability by requiring that the free energy is a minimum
with respect to deformations of the Fermi surface:

```
F_l^s > -(2l + 1)    for all l
F_l^a > -(2l + 1)    for all l
```

Violation of a Pomeranchuk condition signals a spontaneous deformation of the Fermi
surface -- a phase transition that takes the system outside the Fermi liquid framework:

- F_0^s < -1: mechanical instability (negative compressibility --> phase separation)
- F_0^a < -1: magnetic instability (negative spin susceptibility --> ferromagnetism)
- F_1^s < -3: effective mass goes to zero (anomalous)
- F_2^s < -5: d-wave Fermi surface deformation (nematic order)

The Pomeranchuk conditions define the boundary of the Fermi liquid phase in parameter
space. Beyond these boundaries, new phases (magnetic, nematic, superconducting) emerge.


## 7. Zero Sound

One of the most striking predictions of Fermi liquid theory is the existence of zero sound
-- a collective oscillation of the quasiparticle distribution that propagates even in the
collisionless regime (omega * tau >> 1), where ordinary (first) sound cannot exist.

**First sound** (hydrodynamic, omega * tau << 1): density oscillation propagated by
collisions between quasiparticles. This is ordinary sound. Velocity:

```
c_1 = v_F / sqrt(3) * sqrt((1 + F_0^s) * (m/m*))
```

**Zero sound** (collisionless, omega * tau >> 1): a self-consistent oscillation of the
Fermi surface shape, where the quasiparticles move coherently without collisions. The
restoring force is the Landau interaction f, not thermalization. Velocity c_0 > c_1,
determined by:

```
F_0^s * integral = 1    (implicit equation for c_0/v_F)
```

For strong interactions (F_0^s >> 1): c_0 ~ v_F * sqrt(F_0^s / 3) >> v_F.
For weak interactions (F_0^s -> 0): c_0 -> v_F (the sound velocity approaches the Fermi
velocity from above).

Zero sound was predicted by Landau in 1957 and observed in liquid He-3 by Abel, Anderson,
and Wheatley in 1966 at temperatures below ~100 mK, where the quasiparticle mean free
path exceeds the sound wavelength.

The existence of zero sound demonstrates that the Landau interaction f is not just a
correction to single-particle properties but supports its own collective modes.


## 8. Liquid He-3: The Fermi Liquid Par Excellence

Liquid He-3 is the canonical Fermi liquid. The He-3 atom (two protons, one neutron, two
electrons) is a composite fermion with spin 1/2. At temperatures below ~1 K, the de
Broglie wavelength becomes comparable to the interatomic spacing, and quantum degeneracy
effects dominate.

Measured Landau parameters for He-3 at zero pressure:

| Parameter | Value | Physical meaning |
|:----------|:------|:----------------|
| F_0^s | 10.8 | Strong density interaction |
| F_1^s | 6.3 | m*/m = 3.1 |
| F_0^a | -0.70 | Enhanced spin susceptibility |
| F_1^a | -0.55 | Spin-current interaction |

The large F_0^s reflects the hard-core repulsion between He-3 atoms. The negative F_0^a
(close to the Pomeranchuk limit of -1) indicates strong ferromagnetic tendency -- indeed,
at high pressures, F_0^a approaches -1 and He-3 is close to a ferromagnetic instability.

Below ~2.7 mK (at zero pressure), He-3 undergoes a phase transition to a SUPERFLUID
state -- the BCS pairing of quasiparticles into Cooper pairs. The superfluid phases of
He-3 (A phase and B phase) are the most complex ordered states in nature, with orbital
and spin angular momentum L = 1, S = 1 (p-wave, spin-triplet pairing).

The success of Fermi liquid theory in He-3 -- predicting the specific heat, susceptibility,
zero sound, transport, and providing the normal-state starting point for BCS theory -- is
one of the great triumphs of 20th-century theoretical physics.


## 9. Breakdown of Fermi Liquid Theory

Fermi liquid theory is not universal. It can fail in several ways:

**One dimension (Luttinger liquids)**: In 1D, the Fermi "surface" consists of two points
(+k_F and -k_F), and any interaction causes the quasiparticle residue Z to vanish:

```
A(k, omega) ~ |omega|^{alpha}    (no delta-function peak)
```

The excitations are collective modes (spinons and holons), not quasiparticles. Spin and
charge propagate at different velocities (spin-charge separation). This occurs in carbon
nanotubes, quantum wires, edge states of quantum Hall systems.

**Non-Fermi liquids (strange metals)**: In certain strongly correlated systems,
particularly the cuprate high-temperature superconductors above T_c, the quasiparticle
picture breaks down. The hallmarks:
- Resistivity rho ~ T (linear, not T^2 as in Fermi liquids)
- Quasiparticle lifetime 1/tau ~ T (not T^2)
- Broad, incoherent spectral functions without sharp quasiparticle peaks
- "Planckian dissipation": tau ~ hbar/(k_B * T), the shortest possible relaxation time

The mechanism is debated: quantum critical fluctuations, holographic duality, or
fundamentally new collective behavior.

**Quantum critical points**: Near a zero-temperature phase transition (quantum critical
point), critical fluctuations destroy quasiparticles over parts or all of the Fermi
surface. The effective mass diverges (m* -> infinity) and the quasiparticle residue
vanishes (Z -> 0). This occurs in heavy fermion systems (CeCu6, YbRh2Si2) at
field-tuned or pressure-tuned quantum critical points.

**Mott insulators**: When the interaction is strong enough (U >> t in the Hubbard model),
the system becomes an insulator despite having an odd number of electrons per unit cell.
The Fermi surface is destroyed and the adiabatic continuity assumption fails completely.


## 10. Fermi Liquid Theory in Nuclear and Particle Physics

Landau's framework extends beyond condensed matter:

**Nuclear matter**: The nuclear shell model is a Fermi liquid theory. Nucleons in the
nucleus are quasiparticles with effective mass m* ~ 0.7*m (reduced by the attractive
nuclear force) and interactions parametrized by Landau-Migdal parameters g, g':

```
f(k,sigma; k',sigma') = C_0 * (g + g' * tau . tau') + ...
```

where tau are isospin Pauli matrices. The compressibility of nuclear matter (determining
the equation of state and hence neutron star structure) is directly related to F_0^s.

**Neutron stars**: The inner crust and core of a neutron star are Fermi liquids of
neutrons (with small proton and electron fractions). The Landau parameters determine
the neutrino emissivity, specific heat, and cooling rate of neutron stars. Superfluidity
of neutron pairs (analogous to He-3) occurs at ~10^9 K.

**Quark matter**: At asymptotically high densities (if reached in neutron star cores),
deconfined quark matter forms a Fermi liquid of quarks interacting via gluon exchange.
The Landau parameters can be calculated perturbatively from QCD at weak coupling. At
intermediate densities, non-Fermi liquid behavior may occur due to unscreened magnetic
gluon exchange:

```
1/tau ~ epsilon * ln(epsilon)    (marginal Fermi liquid)
```

**Heavy quark effective theory**: The bottom quark in a B meson behaves as a "heavy
quasiparticle" dressed by soft gluon interactions, with concepts directly borrowed from
Fermi liquid theory (effective mass, residual interactions, 1/m expansion).


## 11. Connection to Phonon-Exflation Framework

The connection between Fermi liquid theory and the phonon-exflation framework is not a
peripheral analogy but a central structural identification.

**Particles as quasiparticles**: The core claim of phonon-exflation is that quarks,
leptons, and gauge bosons are excitations of a condensate state on M4 x K, where
K = SU(3) with Jensen deformation. This is PRECISELY Landau's quasiparticle concept:
strongly interacting fundamental degrees of freedom (whatever they are at the Planck
scale) organize into weakly interacting quasiparticles (Standard Model particles) at
low energies. The adiabatic continuity that makes Fermi liquid theory work corresponds
to the stability of the compactification -- the internal geometry does not undergo a phase
transition as the temperature decreases from the compactification scale to zero.

**Effective mass from the Dirac spectrum**: In Fermi liquid theory, the quasiparticle
effective mass m* is determined by the Landau interaction functional through m*/m = 1 + F_1^s/3.
In the phonon-exflation framework, the physical particle masses are determined by the
eigenvalues of the Dirac operator D_K on deformed SU(3). The Dirac eigenvalues at
deformation parameter s_0 play the role of quasiparticle energies epsilon_k. The Session
12 computation finding phi_paasch-near ratios among Dirac eigenvalues at s ~ 0.15 is the
spectral analog of measuring the effective mass ratio m*/m in He-3.

**The Landau functional and the spectral action**: Landau's energy functional
E[n] expresses the total energy as a functional of the quasiparticle occupation numbers.
The spectral action Tr(f(D^2/Lambda^2)) expresses the total action (energy + dynamics) as
a functional of the Dirac spectrum -- which IS the quasiparticle spectrum in the
phonon-NCG dictionary. The Landau interaction function f(k,sigma; k',sigma') corresponds
to the off-diagonal elements of D^2 that couple different irreducible representations
of SU(3).

**Zero sound and phonon modes**: Landau's zero sound is a collisionless collective
oscillation of the Fermi surface. In the phonon-exflation framework, the phonon modes
of the condensate are the long-wavelength collective excitations of M4 x K. Both are
collective modes of a quantum liquid that propagate via the mean-field interaction rather
than through collisions. The first sound / zero sound crossover at omega * tau ~ 1
corresponds to the hydrodynamic / ballistic crossover in the phonon propagation, which
determines the freeze-out temperature in the cosmological expansion.

**Pomeranchuk stability and the V_eff minimum**: The Pomeranchuk conditions F_l > -(2l+1)
define when the Fermi liquid is stable against spontaneous deformations. In the exflation
framework, the V_eff minimum at s_0 defines when the internal geometry is stable against
Jensen deformation. The curvature V_eff''(s_0) is the analog of the restoring force
(1 + F_l/(2l+1)) that prevents Pomeranchuk instability. If V_eff''(s_0) were to vanish,
the internal geometry would undergo a "Pomeranchuk transition" -- a spontaneous shape
deformation analogous to the nematic Fermi surface distortion.

**Non-Fermi liquid behavior and strong coupling**: The breakdown of Fermi liquid theory
in strange metals and near quantum critical points warns that the quasiparticle picture
has limits. In the exflation framework, this corresponds to the regime near the
compactification scale where the effective 4D description breaks down and the full
higher-dimensional dynamics must be used. The "Planckian dissipation" bound tau >= hbar/(k_B*T)
in strange metals may have a geometric counterpart: the minimum relaxation time for the
Jensen deformation parameter s is bounded by the inverse KK mass gap.

**Adiabatic continuity and the stability of physics**: Perhaps the deepest connection is
philosophical. Landau showed that the apparent simplicity of weakly interacting
quasiparticles EMERGES from the complexity of strongly interacting fermions, without
requiring weak coupling as an input. The phonon-exflation framework proposes the same for
particle physics: the Standard Model's apparent simplicity (few particle types, well-defined
masses and couplings) EMERGES from whatever strongly-coupled dynamics operates at the
Planck scale, through the mechanism of compactification on SU(3). Just as Landau's
quasiparticles are protected by adiabatic continuity and Fermi surface topology, the
Standard Model particles are protected by the topological stability of the compactification
(KO-dimension 6) and the spectral gap of the Dirac operator.


## 12. Legacy and Influence

Landau's 1956 paper is one of the most consequential theoretical works in 20th-century
physics. Its influence spans:

1. **Condensed matter physics**: The conceptual foundation for metals, He-3, nuclear
   matter, heavy fermions, and the starting point for BCS superconductivity theory.

2. **The quasiparticle concept**: Now ubiquitous -- phonons, magnons, polarons, plasmons,
   excitons, Cooper pairs, Bogoliubov quasiparticles are all descendants of Landau's idea.

3. **Universality and emergence**: The insight that low-energy physics can be qualitatively
   different from microscopic physics -- that new "particles" emerge from collective
   behavior -- anticipated Anderson's "More Is Different" (1972) and the modern philosophy
   of emergence.

4. **Non-Fermi liquid physics**: By defining what a Fermi liquid IS, Landau implicitly
   defined what it is NOT, opening the door to the study of exotic quantum states
   (Luttinger liquids, strange metals, spin liquids, topological phases).

5. **Effective field theory in particle physics**: The Fermi liquid formalism, with its
   expansion in quasiparticle interactions near the Fermi surface, is a precursor to
   the modern effective field theory approach in particle physics, where the relevant
   degrees of freedom and their interactions change with the energy scale.

The central lesson of Fermi liquid theory -- that the correct description of a physical
system need not invoke its microscopic constituents but rather its collective excitations
near the ground state -- is the animating principle of the phonon-exflation framework
applied to the whole of particle physics.

---

**Key equations:**
- Quasiparticle energy: epsilon_k = epsilon_F + hbar*k_F*(|k|-k_F)/m*
- Quasiparticle lifetime: 1/tau ~ (epsilon - epsilon_F)^2
- Effective mass: m*/m = 1 + F_1^s/3
- Spin susceptibility: chi/chi_free = (m*/m)/(1 + F_0^a)
- Pomeranchuk stability: F_l^{s,a} > -(2l + 1)
- Zero sound velocity: c_0 > v_F, from implicit equation involving F_0^s
