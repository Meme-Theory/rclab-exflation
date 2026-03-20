# On the Magnetic Properties of Superconductors of the Second Group

**Author:** Alexei Alexeyevich Abrikosov
**Year:** 1957
**Journal:** Zh. Eksp. Teor. Fiz., 32, 1442-1452 (Sov. Phys. JETP, 5, 1174-1183)
**Nobel Prize:** 2003 (shared with Ginzburg and Leggett)

---

## 1. Historical Context: From London to Ginzburg-Landau

### 1.1 The Meissner Effect and the London Equations

Superconductivity was discovered by Kamerlingh Onnes in 1911 (mercury, T_c =
4.2 K). The defining property beyond zero resistance is the Meissner effect
(1933): a superconductor EXPELS magnetic flux from its interior. This is not
merely persistent currents (a perfect conductor would trap flux); it is active
expulsion (a thermodynamic equilibrium state).

The London brothers (1935) proposed phenomenological equations:

    curl(J_s) = -(n_s * e^2 / (m * c)) * B
    d(J_s)/dt = (n_s * e^2 / (m * c)) * E

These yield exponential screening of the magnetic field:

    B(x) = B_0 * exp(-x / lambda_L)

where lambda_L = sqrt(m * c^2 / (4 * pi * n_s * e^2)) is the London
penetration depth. Typical values: lambda_L ~ 50-500 nm.

### 1.2 Ginzburg-Landau Theory (1950)

Ginzburg and Landau elevated the description by introducing a complex order
parameter psi(r) -- a macroscopic wavefunction for the superconducting state.
The GL free energy functional is:

    F_GL = F_n + integral d^3r [
        alpha * |psi|^2 + (beta/2) * |psi|^4
        + (1/(2*m*)) * |(-i*hbar*grad - (e*/c)*A) psi|^2
        + B^2 / (8*pi)
    ]

where alpha < 0 below T_c (so psi != 0 is energetically favorable), beta > 0
(stabilizes the free energy), m* = 2*m_e and e* = 2*e are the effective mass
and charge of Cooper pairs (identified after BCS), and A is the vector
potential.

Minimizing F_GL yields two coupled equations:

    (1/(2*m*)) * (-i*hbar*grad - (e*/c)*A)^2 psi + alpha*psi + beta*|psi|^2*psi = 0
    J = (e*/(2*m*)) * [psi* (-i*hbar*grad - (e*/c)*A) psi + c.c.]

The first is a NONLINEAR SCHRODINGER EQUATION for the order parameter. The
second relates the supercurrent to the order parameter gradient.

### 1.3 Two Length Scales, One Ratio

The GL theory contains two characteristic lengths:

- **Coherence length xi**: the distance over which psi can vary.
  xi = hbar / sqrt(2 * m* * |alpha|)
  This is the size of a Cooper pair (loosely) and the minimum scale for
  spatial variation of the order parameter.

- **Penetration depth lambda**: the distance over which B decays.
  lambda = sqrt(m* * c^2 * beta / (4 * pi * e*^2 * |alpha|))
  This is the London penetration depth, modified by GL.

The GL parameter is their ratio:

    kappa = lambda / xi

This single dimensionless number determines the TYPE of superconductor.


## 2. Abrikosov's Insight: kappa > 1/sqrt(2)

### 2.1 The Surface Energy Argument

Ginzburg and Landau had noted that the surface energy of a normal-
superconductor boundary depends on kappa:

- For kappa < 1/sqrt(2): the surface energy is POSITIVE. The superconductor
  minimizes boundary area. Flux is expelled completely (Meissner effect)
  until the field reaches H_c, at which point the entire sample goes normal.
  This is TYPE I.

- For kappa > 1/sqrt(2): the surface energy is NEGATIVE. The superconductor
  MAXIMIZES boundary area. It becomes energetically favorable to create as
  many normal-superconducting interfaces as possible, subject to flux
  quantization. This is TYPE II.

### 2.2 Abrikosov's Calculation

Abrikosov took the kappa > 1/sqrt(2) case seriously. He solved the
linearized GL equation near the upper critical field H_{c2}, where psi is
small and the nonlinear term can be treated perturbatively.

Near H_{c2}, the linearized GL equation is:

    (1/(2*m*)) * (-i*hbar*grad - (e*/c)*A)^2 psi = |alpha| * psi

This is formally identical to the Schrodinger equation for a charged particle
in a uniform magnetic field -- the Landau level problem. The lowest Landau
level has energy hbar*omega_c/2 where omega_c = e*B/(m*c). The condition
for a nontrivial solution gives:

    H_{c2} = Phi_0 / (2 * pi * xi^2)

where Phi_0 = h*c/(2*e) = 2.07 x 10^{-15} Wb is the magnetic flux quantum.

For type-II superconductors (kappa > 1/sqrt(2)), H_{c2} > H_c, so there
exists a field range H_{c1} < H < H_{c2} where the superconductor is in
a MIXED STATE: neither fully superconducting nor fully normal.


## 3. The Vortex State

### 3.1 Single Vortex Structure

In the mixed state, magnetic flux penetrates in the form of quantized
vortices (flux lines). Each vortex is a topological defect of the order
parameter. The structure of a single vortex along the z-axis:

**Order parameter:**
    psi(r, theta) = f(r) * exp(i * theta)

where (r, theta) are cylindrical coordinates centered on the vortex core.
The function f(r) satisfies:
- f(0) = 0 (the order parameter vanishes at the core)
- f(r) -> psi_0 = sqrt(|alpha|/beta) as r -> infinity (bulk value)
- f(r) ~ r for small r (linear vanishing at the core)
- The core size is ~ xi (the coherence length)

**Magnetic field:**
    B(r) ~ (Phi_0 / (2*pi*lambda^2)) * K_0(r/lambda)    for r >> xi

where K_0 is the modified Bessel function of the second kind. Key features:
- B(0) ~ (Phi_0 / (2*pi*lambda^2)) * ln(kappa) at the core
- B decays exponentially over length lambda
- Total flux through the vortex = Phi_0 (exactly one flux quantum)

**Supercurrent:**
    J(r) circles the vortex core, peaking at r ~ lambda and decaying
    exponentially for r >> lambda.

### 3.2 Flux Quantization

The flux carried by each vortex is EXACTLY one flux quantum:

    integral B . dA = Phi_0 = h*c / (2*e) = 2.0678 x 10^{-15} Wb

This follows from the single-valuedness of psi. Going around the vortex core,
the phase must change by exactly 2*pi*n (n = integer). For a singly-quantized
vortex (n = 1):

    oint grad(phase) . dl = 2*pi

Combined with the London relation between current and phase gradient, this
yields Phi = Phi_0. Higher winding numbers (n > 1) are energetically unstable
and split into n singly-quantized vortices.

### 3.3 Energy Per Unit Length

The energy per unit length of a single vortex line (for kappa >> 1) is:

    epsilon_1 = (Phi_0 / (4*pi*lambda))^2 * ln(kappa)
              = (Phi_0^2 / (4*pi*mu_0*lambda^2)) * ln(kappa)    (SI units)

The logarithmic factor ln(kappa) comes from integrating the magnetic field
energy from the core (size xi) to the screening length (size lambda).


## 4. Vortex Interactions and the Abrikosov Lattice

### 4.1 Vortex-Vortex Interaction

Two parallel vortices separated by distance d interact with energy per unit
length:

    U(d) = (Phi_0^2 / (8*pi^2 * lambda^2)) * K_0(d/lambda)

For d >> lambda: U ~ exp(-d/lambda), exponentially decaying.
For d << lambda: U ~ -ln(d/xi) + const, logarithmically divergent.

CRUCIALLY, for type-II superconductors (kappa > 1/sqrt(2)), this interaction
is REPULSIVE for parallel vortices and ATTRACTIVE for antiparallel vortices.
Repulsion between like-sign vortices forces them to arrange in a regular
lattice.

### 4.2 The Vortex Lattice

Abrikosov solved for the periodic solution of the GL equations near H_{c2}.
The order parameter is:

    psi(x, y) = sum_n C_n * exp(2*pi*i*n*y/b) * exp(-(x - n*a')^2 / (2*l_B^2))

where l_B = sqrt(hbar*c/(e*B)) is the magnetic length and a', b are lattice
parameters.

Abrikosov found that the free energy depends on the lattice structure through
a single parameter:

    beta_A = <|psi|^4> / <|psi|^2>^2

where <...> denotes spatial average. The lattice that minimizes beta_A is the
energetically preferred structure.

### 4.3 Square vs Triangular: The Correction

Abrikosov originally computed beta_A for a SQUARE lattice and found beta_A =
1.18. He argued this was the minimum. However:

Kleiner, Roth, and Autler (1964) showed that the TRIANGULAR (hexagonal)
lattice has beta_A = 1.1596, which is LOWER. The triangular lattice is the
true ground state.

Abrikosov acknowledged this correction. The triangular vortex lattice is
now universally called the "Abrikosov lattice" despite the original paper's
square lattice.

### 4.4 Lattice Spacing

The mean distance between vortices is set by the flux density:

    n_v = B / Phi_0    (vortex density, number per unit area)

    a_0 = (2 * Phi_0 / (sqrt(3) * B))^{1/2}    (triangular lattice spacing)

At H_{c2}: a_0 ~ xi (vortex cores overlap, superconductivity destroyed).
At H_{c1}: a_0 ~ lambda (vortices widely separated, nearly isolated).


## 5. Critical Fields

### 5.1 Lower Critical Field H_{c1}

H_{c1} is the field at which it first becomes energetically favorable to
introduce a single vortex:

    H_{c1} = (Phi_0 / (4*pi*lambda^2)) * (ln(kappa) + 0.5)

For kappa >> 1: H_{c1} ~ (Phi_0 / (4*pi*lambda^2)) * ln(kappa)

Below H_{c1}: complete Meissner effect (no flux penetration).

### 5.2 Upper Critical Field H_{c2}

H_{c2} is the field at which vortex cores overlap and superconductivity is
destroyed throughout the bulk:

    H_{c2} = Phi_0 / (2*pi*xi^2) = sqrt(2) * kappa * H_c

where H_c = Phi_0 / (2*sqrt(2)*pi*lambda*xi) is the thermodynamic critical
field. For type-II materials, H_{c2} > H_c.

### 5.3 The Phase Diagram

The H-T phase diagram has three regions:

    H > H_{c2}(T):        Normal state
    H_{c1}(T) < H < H_{c2}(T):   Mixed state (vortex lattice)
    H < H_{c1}(T):        Meissner state (complete flux expulsion)

Both H_{c1}(T) and H_{c2}(T) vanish at T = T_c.


## 6. Experimental Confirmation

Key observations of the vortex lattice:

- **Decoration** (Essmann-Trauble, 1967): Ferromagnetic nanoparticles deposited
  on a Pb-In alloy collected at vortex cores, revealing the triangular lattice.
- **Neutron diffraction** (Cribier et al., 1964): Bragg peaks from the periodic
  B-field in niobium confirmed the lattice constant.
- **STM imaging** (Hess et al., 1989): Atomic-resolution conductance maps in
  NbSe_2 showed vortex cores with bound Caroli-de Gennes-Matricon states.
- **High-T_c cuprates** (kappa ~ 100): pancake vortices in CuO_2 layers,
  Josephson inter-layer vortices, vortex melting, and vortex glass phases.


## 7. Vortex Dynamics

Transport current J perpendicular to vortex lines exerts a Lorentz force
f_L = (J x Phi_0 * z_hat) / c per unit length, driving vortex motion and
dissipation. The flux-flow resistivity is rho_ff = rho_n * (B / H_{c2})
(Bardeen-Stephen, 1965).

In real materials, defects PIN vortices, creating a critical current J_c
below which resistance is zero. Above J_c, flux flow begins. At finite
temperature, pinned vortices escape by thermal activation (Anderson flux
creep): E = E_0 * exp(-U(J)/(k_B*T)). In high-T_c materials, thermal
fluctuations make creep a dominant effect.


## 8. Connection to Phonon-Exflation Cosmology

### 8.1 BEC Vortices as Abrikosov Analogs

The phonon-exflation simulation uses a Gross-Pitaevskii equation (GPE) to
model a BEC. The GPE:

    i*hbar * d(Psi)/dt = (-hbar^2/(2*m))*nabla^2(Psi) + g*|Psi|^2*Psi

is STRUCTURALLY IDENTICAL to the Ginzburg-Landau equation (time-dependent
version). The vortices in the BEC are quantized with circulation:

    kappa = h / m     (neutral superfluid, replaces Phi_0 = h*c/(2*e))

Each BEC vortex has the same structure as an Abrikosov vortex:
- |Psi| -> 0 at the core over length xi (healing length)
- Phase winds by 2*pi around the core
- Velocity field v = (hbar/m) * grad(phase) ~ 1/r

### 8.2 Vortex-Antivortex Pairs and D/H

The D/H ratio in the simulation is determined by the BINDING of vortex-
antivortex pairs. The interaction between a vortex and antivortex (opposite
circulation) is ATTRACTIVE:

    E_pair(d) ~ -(hbar^2 * n_s / m) * ln(d / xi)

where d is the pair separation and n_s is the superfluid density. When the
healing length xi grows during expansion (xi_t = xi_0 * R(t)), pairs with
separation d < xi_t become unbound (their cores overlap, E_bind > 0). The
fraction of surviving bound pairs at freeze-out determines the D/H ratio.

This is DIRECTLY analogous to vortex physics in type-II superconductors:
the pair binding energy, core structure, and interaction potential are all
governed by the same Ginzburg-Landau / Gross-Pitaevskii framework.

### 8.3 Healing Length as Coherence Length

The BEC healing length:

    xi = hbar / sqrt(2 * m * g * n_0) = 1 / sqrt(8 * pi * a * n_0)

(where a is the s-wave scattering length and n_0 is the condensate density)
is the EXACT analog of the GL coherence length xi = hbar/sqrt(2*m*|alpha|).
Both set the vortex core size.

In the simulation, xi grows as the condensate expands. This growth drives the
vortex-antivortex unbinding that determines D/H. The mechanism is:
1. Initial state: dense vortex-antivortex pairs with d << xi
2. Expansion: xi grows, pairs with d < xi lose their binding energy
3. Freeze-out: surviving bound pairs = "deuterium" analogs

### 8.4 Topological Defects as Particles

The vortices in the simulation are topological defects -- they cannot be
removed by smooth deformations of the order parameter. In the phonon-
exflation picture, PARTICLES are topological defects of the condensate
wavefunction on M4 x SU(3). The Abrikosov vortex provides the archetype:

- Quantized circulation -> quantized charge
- Vortex core -> particle localization (size ~ xi ~ Compton wavelength)
- Vortex-antivortex pairs -> particle-antiparticle pairs
- Flux quantization -> charge quantization

The analogy is not merely suggestive. The mathematical structures (GL/GPE
equations, topological winding numbers, core structure, interaction
potentials) are IDENTICAL. What differs is the physical arena: a 2D or 3D
superconductor/BEC vs the internal space SU(3) of the phonon-exflation model.

### 8.5 The Vortex Lattice and Cosmological Structure

The Abrikosov lattice -- the spontaneous crystallization of vortices into a
regular array -- is an example of EMERGENT spatial order from a uniform
background field. In the cosmological context, the analogous question is
whether topological defects of the condensate (particle excitations)
spontaneously organize into regular structures (the cosmic web, galaxy
clusters). The vortex lattice in the simulation provides a toy model for
this organizational tendency.

---

## References

1. A. A. Abrikosov, "On the magnetic properties of superconductors of the
   second group," Zh. Eksp. Teor. Fiz. 32, 1442-1452 (1957) [Sov. Phys.
   JETP 5, 1174-1183 (1957)].
2. V. L. Ginzburg and L. D. Landau, "On the theory of superconductivity,"
   Zh. Eksp. Teor. Fiz. 20, 1064-1082 (1950).
3. W. H. Kleiner, L. M. Roth, and S. H. Autler, "Bulk solution of
   Ginzburg-Landau equations for type II superconductors: upper critical
   field region," Phys. Rev. 133, A1226 (1964).
4. U. Essmann and H. Trauble, "The direct observation of individual flux
   lines in type II superconductors," Phys. Lett. A 24, 526 (1967).
5. H. F. Hess, R. B. Robinson, R. C. Dynes, J. M. Valles Jr., and
   J. V. Waszczak, "Scanning-tunneling-microscope observation of the
   Abrikosov flux lattice and the density of states near and inside a
   fluxoid," Phys. Rev. Lett. 62, 214 (1989).
6. M. Tinkham, Introduction to Superconductivity, 2nd ed. (McGraw-Hill,
   1996).
7. P. G. de Gennes, Superconductivity of Metals and Alloys (Benjamin,
   1966).
8. J. Bardeen and M. J. Stephen, "Theory of the motion of vortices in
   superconductors," Phys. Rev. 140, A1197 (1965).
