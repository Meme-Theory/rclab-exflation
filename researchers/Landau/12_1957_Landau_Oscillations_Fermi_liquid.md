# Oscillations in a Fermi Liquid

**Author:** Lev Davidovich Landau
**Year:** 1957
**Journal:** Zh. Eksp. Teor. Fiz., 32, 59-66 (Sov. Phys. JETP, 5, 101-108)

---

## 1. Historical Context: The Fermi Liquid Program

By 1957, Landau had spent nearly a decade constructing his theory of Fermi
liquids -- a framework for understanding interacting fermion systems without
solving the full many-body Schrodinger equation. The first paper (1956)
established the quasiparticle concept and the Landau parameters. The second
paper (early 1957) derived thermodynamic properties: specific heat, magnetic
susceptibility, compressibility. This third paper completed the trilogy by
addressing DYNAMICS: the collective oscillations of a Fermi liquid.

The question was precise: what collective modes can propagate through a
degenerate Fermi system at low temperatures?

Ordinary sound -- first sound -- was well understood. It is a density wave
mediated by collisions between particles. In a classical gas, sound propagates
because particles collide frequently enough to establish local thermodynamic
equilibrium, and the pressure gradient drives bulk flow. The sound velocity is:

    v_s = sqrt(dP/d(rho))

where P is the pressure and rho is the mass density. For this mechanism to
work, the mean free path must be MUCH SHORTER than the wavelength: collisions
must be frequent on the scale of one oscillation period. Quantitatively, the
condition is:

    omega * tau << 1       (hydrodynamic regime)

where omega is the frequency and tau is the collision time (mean free time
between quasiparticle scatterings).

At low temperatures in a Fermi liquid, tau grows as 1/T^2 (Pauli blocking
suppresses scattering). So at sufficiently low T, the hydrodynamic condition
FAILS: omega * tau >> 1. In this regime, quasiparticles traverse many
wavelengths between collisions. First sound cannot propagate.

Landau asked: does ANYTHING propagate in this collisionless regime?


## 2. The Linearized Transport Equation

### 2.1 The Kinetic Equation for Quasiparticles

The Fermi liquid is described by a quasiparticle distribution function
n(p, r, t), where p is momentum, r is position, and t is time. In
equilibrium, this is the Fermi-Dirac distribution:

    n_0(p) = 1 / (exp(beta * (epsilon_p - mu)) + 1)

where epsilon_p is the quasiparticle energy (which itself depends on n
through the Landau interaction function f(p, p')).

The kinetic equation is:

    dn/dt + v_p . (grad_r n) + F . (grad_p n) = I_coll[n]

where v_p = grad_p(epsilon_p) is the quasiparticle velocity, F is any
external force, and I_coll is the collision integral.

### 2.2 The Collisionless Limit

In the zero-sound regime (omega * tau >> 1), we SET I_coll = 0. This is
the crucial simplification. The equation becomes:

    dn/dt + v_p . (grad_r n) = 0

But epsilon_p depends on n (through the Landau interaction), so this is a
NONLINEAR integro-differential equation. Landau linearized it.

### 2.3 Linearization

Write n = n_0 + delta_n, where delta_n is small. The quasiparticle energy
shifts by:

    delta_epsilon_p = sum_{p'} f(p, p') * delta_n(p')

where the sum is over all momenta (an integral in the continuum limit). The
linearized transport equation becomes:

    d(delta_n)/dt + v_p . grad_r(delta_n)
        + (dn_0/d(epsilon_p)) * v_p . grad_r(delta_epsilon_p) = 0

At low temperature, dn_0/d(epsilon_p) is sharply peaked at the Fermi surface:

    dn_0/d(epsilon_p) -> -delta(epsilon_p - mu)

This means that only the distribution ON THE FERMI SURFACE matters. The
perturbation is parameterized by a function on the Fermi sphere:

    delta_n(p, r, t) = -delta(epsilon_p - mu) * nu(theta_p, phi_p) * exp(i*k.r - i*omega*t)

where nu(theta_p, phi_p) describes the angular distortion of the Fermi surface.


## 3. The Zero Sound Equation

### 3.1 The Dispersion Relation

Substituting the plane-wave ansatz into the linearized equation and using the
Landau decomposition of f into Legendre harmonics:

    F(cos(theta)) = sum_l F_l^s * P_l(cos(theta))

where F_l^s = N(0) * f_l^s are the dimensionless symmetric Landau parameters
(N(0) is the density of states at the Fermi surface), one obtains the
fundamental equation for zero sound.

For the l=0 (isotropic) case, defining u = omega / (k * v_F) as the
dimensionless phase velocity, the zero-sound dispersion relation is:

    1 = (F_0^s / 2) * integral from -1 to +1 of [x * dx / (x - u)]

where x = cos(theta) is the angle between p and k. Evaluating the integral:

    1 = (F_0^s / 2) * [1 + (u/2) * ln((u+1)/(u-1))]     for |u| > 1

This is a transcendental equation for u in terms of F_0^s.

### 3.2 Solution: Zero Sound Velocity

For F_0^s > 0, there exists a real solution with u > 1, meaning the zero
sound velocity exceeds the Fermi velocity:

    v_0 = u * v_F > v_F

This is physically necessary: if v_0 < v_F, the mode would be Landau-damped
(absorbed by quasiparticles moving faster than the wave).

Key limiting cases:

- **Weak coupling (F_0^s << 1):**
  u -> 1 + 2 * exp(-2/F_0^s - 2)
  The velocity is barely above v_F, and the mode is exponentially weakly
  excited. It exists mathematically but is practically unobservable.

- **Strong coupling (F_0^s >> 1):**
  u -> sqrt(F_0^s / 3)
  The zero sound velocity scales as sqrt(F_0^s). In this limit, the zero
  sound velocity approaches the first sound velocity (v_s = v_F * sqrt(F_0^s / 3)
  for a Fermi liquid), and the two modes become indistinguishable.

- **Intermediate coupling (F_0^s ~ 1):**
  u ~ 1.2 to 2. The zero sound and first sound velocities are different,
  and the crossover is experimentally accessible.


## 4. Physical Interpretation: Fermi Surface Deformation

### 4.1 What Zero Sound IS

First sound is a density oscillation: particles move back and forth, pushed
by pressure gradients, with collisions maintaining local equilibrium. The
distribution function is an isotropic Fermi-Dirac distribution with slowly
varying density and temperature.

Zero sound is COMPLETELY DIFFERENT. It is a deformation of the Fermi surface
shape that propagates as a wave. In zero sound:

- There is NO local thermodynamic equilibrium
- The distribution function is NOT Fermi-Dirac at any point
- The Fermi surface oscillates between prolate and oblate shapes
- The restoring force is the Landau interaction f(p, p'), not pressure

Pictorially: imagine the Fermi sphere in momentum space. First sound uniformly
expands and contracts it (isotropic density oscillation). Zero sound distorts
it into an egg shape, with the long axis pointing along the propagation
direction, and this distortion propagates through the liquid.

### 4.2 The Self-Consistent Field Mechanism

The propagation mechanism is self-consistent:

1. A local distortion of the Fermi surface at point r creates a perturbation
   delta_epsilon_p through the Landau interaction.
2. This energy perturbation deflects quasiparticle trajectories.
3. The deflected quasiparticles create a Fermi surface distortion at
   neighboring points.
4. This distortion propagates as a wave.

No collisions are needed. The wave propagates through the MEAN FIELD of the
quasiparticle interactions. This is why zero sound exists in the collisionless
regime.

### 4.3 Landau Damping

For F_0^s < 0 (attractive interactions in the l=0 channel), there is no real
solution with u > 1. The mode is Landau-damped: any Fermi surface distortion
decays by transferring energy to individual quasiparticles that "surf" the
wave (move at the wave's phase velocity). This is the same mechanism as
Landau damping in plasma physics, which Landau had analyzed in 1946.


## 5. Higher Angular Momentum Modes

### 5.1 General Decomposition

The distortion nu(theta, phi) can be decomposed into spherical harmonics:

    nu(theta, phi) = sum_{l,m} nu_{l,m} * Y_l^m(theta, phi)

Each angular momentum channel l has its own zero-sound branch, governed by
the Landau parameter F_l^s (symmetric channel) or F_l^a (antisymmetric
channel, for spin waves).

### 5.2 Spin Zero Sound

The antisymmetric Landau parameters F_l^a govern spin-dependent interactions.
They give rise to SPIN ZERO SOUND: a propagating oscillation of the spin
polarization at the Fermi surface, without any density oscillation. The
dispersion is governed by:

    1 = (F_0^a / 2) * [1 + (u/2) * ln((u+1)/(u-1))]

with F_0^a replacing F_0^s. In He-3, F_0^a is negative and large in magnitude,
so spin zero sound is heavily damped. But in nuclear matter and neutron stars,
spin zero sound may propagate.

### 5.3 Quadrupolar and Higher Modes

The l=2 mode corresponds to a quadrupolar distortion of the Fermi surface.
Higher l modes require progressively larger Landau parameters to propagate
undamped. In practice, for most Fermi liquids, only the l=0 mode (density
zero sound) is undamped.


## 6. Temperature Crossover: Zero Sound to First Sound

### 6.1 The Crossover Criterion

At low T: omega * tau >> 1, zero sound propagates.
At high T: omega * tau << 1, first sound propagates.
The crossover occurs at omega * tau ~ 1.

Since tau ~ 1/T^2 in a Fermi liquid (Pauli blocking), the crossover
temperature for a mode of frequency omega is:

    T_cross ~ sqrt(hbar * omega / k_B) * (T_F)^{1/2} / (some numerical factor)

where T_F is the Fermi temperature.

### 6.2 Velocity Jump

In the crossover region, the sound velocity changes from v_0 (zero sound)
to v_1 (first sound). For He-3 at low pressure:

    v_0 / v_F ~ 1.2       (zero sound, T < 10 mK)
    v_1 / v_F ~ 0.6       (first sound, T > 100 mK)

The ratio v_0 / v_1 ~ 2 is a direct measure of the quasiparticle interaction
strength.

### 6.3 Attenuation Peak

At the crossover (omega * tau ~ 1), NEITHER regime applies cleanly. The
attenuation of sound reaches a maximum. This attenuation peak is a
characteristic experimental signature of the zero-sound to first-sound
crossover.


## 7. Experimental Observation

Liquid He-3 is the paradigmatic Fermi liquid (fermions, spin 1/2, strong
interactions with F_0^s ~ 10, Fermi temperature ~1 K). Abel, Anderson, and
Wheatley (1966) made the first definitive observation of zero sound, measuring
sound velocity at 15.4 MHz as a function of temperature. They found a clear
crossover at T ~ 50 mK (omega * tau ~ 1) with an attenuation peak, and the
measured v_0/v_F ratio agreed quantitatively with Landau's formula.


## 8. Zero Sound in Other Systems

Zero sound appears across many fermionic systems:

- **Nuclear matter**: Giant resonances are zero-sound modes. The isoscalar
  monopole (l=0) gives nuclear compressibility; the dipole (l=1) probes
  symmetry energy.
- **Metals**: Coulomb interactions convert the l=0 zero-sound mode into the
  plasmon. Zero sound in the strict sense requires short-range interactions.
- **Dense quark matter**: The quark Fermi surface supports zero-sound modes
  relevant for neutron star cooling and gravitational wave emission.
- **Ultracold Fermi gases** (Li-6, K-40): The BEC-BCS crossover modifies
  the zero-sound dispersion continuously from weak-pairing to tight-binding
  limits.


## 9. Connection to Phonon-Exflation Cosmology

### 9.1 Zero Sound as a Paradigm for Emergent Collective Modes

Zero sound demonstrates a critical physical principle: collective modes can
exist PURELY because of interactions between quasiparticles, without any
underlying thermal equilibrium or collision-mediated mechanism. The mode
propagates through self-consistent mean-field dynamics.

In the phonon-exflation framework, the phonon modes of the BEC condensate
(on M4 x SU(3)) are analogous to zero-sound modes. They are collective
excitations of the condensate order parameter that propagate through the
Fermi surface (or, for bosons, the condensate wavefunction) via self-consistent
interactions. The key structural parallel:

- **Fermi liquid**: Landau interaction f(p,p') --> zero sound
- **BEC condensate**: mean-field interaction g|Psi|^2 --> Bogoliubov phonons

### 9.2 The Collisionless Regime and High-Energy Physics

The zero-sound regime (omega * tau >> 1) corresponds to the high-energy limit
where individual quasiparticle scatterings are rare. In the phonon-exflation
picture, this maps onto the perturbative regime of particle physics: at high
energies, the coupling constants are small (asymptotic freedom for QCD), and
particles propagate freely between rare hard scatterings. The collective
excitations of the condensate in this regime are the "particles" of the
Standard Model.

The crossover from zero sound to first sound (omega * tau ~ 1) corresponds
to the confinement transition: as the energy scale decreases, interactions
become strong, the collisionless description breaks down, and collective
hydrodynamic behavior (hadrons, mesons) replaces perturbative quark dynamics.

### 9.3 Fermi Surface Distortion and Internal Geometry

Zero sound propagates as a SHAPE oscillation of the Fermi surface. In the
phonon-exflation framework, the Jensen deformation parameter s controls the
SHAPE of the internal space SU(3). The analogy is:

- Fermi surface shape <--> internal metric g_s on SU(3)
- Landau parameters F_l^s <--> Seeley-DeWitt coefficients a_n
- Zero-sound velocity <--> speed of propagation of geometric deformations
- Landau damping <--> instability of certain deformation modes

The Dirac operator D_K(s) on the deformed SU(3) has eigenvalues that depend
on s, just as the quasiparticle energies depend on the Fermi surface shape.
A propagating zero-sound-like mode in s-space would correspond to an
oscillation of the internal geometry -- which is precisely the mechanism
proposed for exflation.

### 9.4 The Spectral Action as a Landau Free Energy

Landau's Fermi liquid theory is a PHENOMENOLOGICAL theory: the Landau
parameters F_l are inputs, not derived from microscopic physics. Similarly,
the spectral action Tr(f(D^2/Lambda^2)) is a phenomenological functional that
encodes the dynamics of the internal geometry through a few parameters (the
cutoff Lambda and the shape of f).

The Landau free energy functional for the Fermi liquid is:

    F[n] = F_0 + sum_p epsilon_p^0 * delta_n_p
           + (1/2) * sum_{p,p'} f(p,p') * delta_n_p * delta_n_p' + ...

The spectral action for the deformed internal space is:

    S[s] = Tr(f(D_K(s)^2 / Lambda^2))
         = sum_n f(lambda_n(s)^2 / Lambda^2)

Both are functionals of a "distribution" (quasiparticle occupation / eigenvalue
spectrum) that determine the dynamics of collective modes. The parallel
suggests that techniques from Fermi liquid theory (Landau damping analysis,
stability criteria, collective mode classification) may be directly applicable
to the spectral action analysis.

---

## References

1. L. D. Landau, "Oscillations in a Fermi liquid," Zh. Eksp. Teor. Fiz. 32,
   59-66 (1957) [Sov. Phys. JETP 5, 101-108 (1957)].
2. L. D. Landau, "The theory of a Fermi liquid," Zh. Eksp. Teor. Fiz. 30,
   1058 (1956) [Sov. Phys. JETP 3, 920 (1957)].
3. L. D. Landau, "On the theory of the Fermi liquid," Zh. Eksp. Teor. Fiz.
   32, 59 (1957) [Sov. Phys. JETP 5, 101 (1957)].
4. W. R. Abel, A. C. Anderson, and J. C. Wheatley, "Propagation of zero
   sound in liquid He-3 at low temperatures," Phys. Rev. Lett. 17, 74-78
   (1966).
5. A. A. Abrikosov, L. P. Gorkov, and I. E. Dzyaloshinski, Methods of
   Quantum Field Theory in Statistical Physics (Dover, 1963).
6. G. Baym and C. Pethick, Landau Fermi-Liquid Theory: Concepts and
   Applications (Wiley, 1991).
7. D. Pines and P. Nozieres, The Theory of Quantum Liquids, Vol. 1:
   Normal Fermi Liquids (Benjamin, 1966).
8. P. Roach and J. B. Ketterson, "Observation of transverse zero sound in
   normal He-3," Phys. Rev. Lett. 36, 736 (1976).
