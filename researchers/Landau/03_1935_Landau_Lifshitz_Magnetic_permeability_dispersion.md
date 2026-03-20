# On the Theory of the Dispersion of Magnetic Permeability in Ferromagnetic Bodies

**Authors:** Lev Davidovich Landau, Evgeny Mikhailovich Lifshitz
**Year:** 1935
**Journal:** Physikalische Zeitschrift der Sowjetunion, 8, 153-169

---

## 1. Historical Context: Ferromagnetism in the 1930s

By 1935, the quantum theory of ferromagnetism was established in broad outline.
Heisenberg (1928) had shown that the exchange interaction between electron spins
could produce spontaneous magnetization below a critical temperature (the Curie
temperature T_c). Bloch (1930) had introduced spin waves -- the low-energy
collective excitations of the ferromagnetic state. Weiss's domain hypothesis
(1907) was widely accepted: ferromagnets break into macroscopic regions (domains)
with uniform magnetization, separated by domain walls.

What was missing was a DYNAMICAL theory. How does the magnetization M(r, t)
evolve in time? How do domain walls move? What determines the structure and
width of a domain wall? Landau and Lifshitz provided the answer.


## 2. The Landau-Lifshitz Equation

### 2.1 The Equation of Motion

The fundamental equation proposed by Landau and Lifshitz governs the time
evolution of the magnetization vector M(r, t):

    dM/dt = -gamma * (M x H_eff) + (alpha / M_s) * M x (M x H_eff)

where:
- gamma = g * mu_B / hbar is the gyromagnetic ratio (g ~ 2 for electrons)
- H_eff is the effective magnetic field (see Section 3)
- alpha is a dimensionless damping parameter
- M_s = |M| is the saturation magnetization (assumed constant in magnitude)
- "x" denotes the vector cross product

### 2.2 Physical Interpretation

The equation has two terms:

**Precession term** (-gamma * M x H_eff): The magnetization precesses around
the effective field, just as a gyroscope precesses around the gravitational
field. This term is conservative -- it preserves the energy. The precession
frequency is omega = gamma * H_eff, typically in the GHz range for laboratory
fields (the microwave regime).

**Damping term** (alpha/M_s * M x (M x H_eff)): This drives M toward alignment
with H_eff. Without damping, M would precess forever and never relax. The
double cross product M x (M x H_eff) points in the direction of steepest
descent on the unit sphere (toward H_eff), while remaining perpendicular to M
(preserving |M| = M_s).

### 2.3 The Gilbert Form

Gilbert (1955) proposed an equivalent but mathematically more convenient form:

    dM/dt = -gamma_G * (M x H_eff) + (alpha_G / M_s) * M x (dM/dt)

The Gilbert form has the damping proportional to dM/dt rather than to H_eff,
which simplifies the mathematical analysis. The two forms are related by:

    gamma = gamma_G / (1 + alpha_G^2)
    alpha_LL = alpha_G / (1 + alpha_G^2)

For small damping (alpha << 1), the distinction is negligible.

### 2.4 Conservation of |M|

Both the LL and Gilbert equations preserve |M| = M_s exactly. This can be
verified directly:

    d(|M|^2)/dt = 2 * M . (dM/dt)
                = 2 * M . (-gamma * M x H_eff) + 2 * M . (alpha/M_s * M x (M x H_eff))
                = 0 + 0 = 0

since M is perpendicular to both M x H_eff and M x (M x H_eff). The
magnetization vector traces a path on the sphere of radius M_s.


## 3. The Effective Field

### 3.1 Energy Functional

The effective field H_eff is derived from the total magnetic energy functional
E[M] via:

    H_eff = -(1/M_s) * delta_E / delta_m

where m = M / M_s is the unit magnetization. The energy functional contains
four contributions:

### 3.2 Exchange Energy

    E_ex = A * integral |grad(m)|^2 d^3r

where A is the exchange stiffness (units: J/m or erg/cm). This penalizes
spatial variations of the magnetization direction. The exchange length is:

    l_ex = sqrt(2A / (mu_0 * M_s^2))

typically 3-10 nm for common ferromagnets.

### 3.3 Magnetocrystalline Anisotropy

    E_anis = integral K_u * (1 - (m . n_hat)^2) d^3r  (uniaxial)

where K_u is the anisotropy constant and n_hat is the easy axis. This favors
alignment of M along crystallographic directions. For cubic anisotropy:

    E_anis = K_1 * integral (m_1^2*m_2^2 + m_2^2*m_3^2 + m_3^2*m_1^2) d^3r

### 3.4 Zeeman Energy

    E_Z = -mu_0 * integral M . H_ext d^3r

The coupling to the external applied field H_ext.

### 3.5 Demagnetization Energy

    E_demag = -(mu_0 / 2) * integral M . H_demag d^3r

where H_demag is the field produced by the magnetization itself (computed from
div(H_demag) = -div(M)). This is a long-range interaction that depends on the
sample geometry.


## 4. Domain Wall Structure

### 4.1 The Bloch Wall

Landau and Lifshitz solved for the static domain wall profile -- the
magnetization configuration that separates two domains with opposite
magnetization (say +z and -z). The Bloch wall solution rotates M in the plane
perpendicular to the wall normal:

    theta(x) = 2 * arctan(exp(x / delta))

where theta is the polar angle of M and delta is the domain wall width:

    delta = sqrt(A / K_u)

The domain wall energy per unit area is:

    sigma = 4 * sqrt(A * K_u)

### 4.2 Physical Scales

For iron: A ~ 2 * 10^{-11} J/m, K_u ~ 5 * 10^4 J/m^3, giving:

    delta ~ 20 nm (about 100 lattice constants)
    sigma ~ 3 * 10^{-3} J/m^2

The wall is microscopically thin but macroscopically smooth -- a true mesoscale
object.

### 4.3 The Neel Wall

In thin films, demagnetization energy favors in-plane rotation. The Neel wall
(1955) rotates M within the plane of the wall, avoiding surface magnetic
charges. The crossover thickness between Bloch and Neel walls is:

    t_c ~ delta * ln(delta / a)

where a is the lattice constant.

### 4.4 Domain Wall as a Topological Defect

A domain wall is a topological defect: it separates two regions of different
ground state. The wall cannot be removed by continuous deformation of M(r)
as long as the boundary conditions (M -> +z at x -> -infinity, M -> -z at
x -> +infinity) are maintained.

Mathematically, the domain wall maps the real line R to the target space S^1
(the equator of the magnetization sphere). The topological charge is:

    Q = (1/pi) * integral_{-inf}^{+inf} (d theta / dx) dx = 1

This is a 1D topological soliton, analogous to the kink in phi^4 field theory.


## 5. Domain Wall Dynamics

### 5.1 Walker Breakdown

A domain wall in a magnetic field moves with velocity:

    v = gamma * delta * H  (for H < H_Walker)

where H_Walker = alpha * K_u / M_s is the Walker field (equivalently alpha * H_K / 2, with H_K = 2*K_u/M_s the anisotropy field). Below
H_Walker, the wall moves rigidly. Above it, the wall undergoes oscillatory
motion with reduced average velocity -- the Walker breakdown.

### 5.2 Spin Waves and Magnons

Small oscillations about the equilibrium magnetization are spin waves (magnons).
Linearizing the LL equation:

    M = M_s * z_hat + m_perp * exp(i*(k.r - omega*t))

gives the dispersion relation:

    omega(k) = gamma * (H_ext + 2*A*k^2/M_s + H_anis)

For k -> 0, this is a gapped excitation (due to anisotropy). For large k,
omega ~ k^2 (quadratic, unlike phonons which are linear).

In quantum mechanics, magnons are bosons with occupation number given by the
Bose-Einstein distribution. At low temperature:

    delta_M(T) = M_s - M(T) ~ T^{3/2}  (Bloch T^{3/2} law)


## 6. Topological Defects in Magnetic Systems

### 6.1 Vortices

In 2D magnetic films, the magnetization can form vortex configurations:

    m(r, phi) = cos(Theta(r)) * z_hat + sin(Theta(r)) * (cos(C*phi + chi) * r_hat
                + sin(C*phi + chi) * phi_hat)

where C = +/-1 is the vorticity (chirality) and p = +/-1 is the polarity
(core magnetization direction). The vortex core has a size ~ l_ex.

### 6.2 Skyrmions

Magnetic skyrmions are 2D topological solitons characterized by a topological
charge:

    Q = (1/4*pi) * integral m . (dm/dx x dm/dy) dx dy

Skyrmions have Q = +/-1 and are topologically protected -- they cannot be
continuously deformed to the uniform state. They were theoretically predicted
by Bogdanov and Yablonskii (1989) and experimentally observed in MnSi by
Muhlbauer et al. (2009).

### 6.3 Classification by Homotopy

The topological classification of magnetic defects follows from homotopy theory:

- **Domain walls** (1D): pi_0(S^1) = Z (disconnected ground states)
- **Vortices** (2D): pi_1(S^1) = Z (winding number)
- **Skyrmions** (2D): pi_2(S^2) = Z (wrapping number)
- **Hedgehogs** (3D): pi_2(S^2) = Z (Brouwer degree)
- **Hopfions** (3D): pi_3(S^2) = Z (Hopf invariant)

This hierarchy of topological defects is universal -- it applies to ANY order
parameter field with the same symmetry.


## 7. The LL Equation as a Universal Field Equation

### 7.1 Connection to Other Nonlinear Equations

The LL equation is part of a family of nonlinear field equations that share
structural features:

| Equation | Order Parameter | Symmetry | Defects |
|:---------|:---------------|:---------|:--------|
| Landau-Lifshitz | M (unit vector) | O(3) -> O(2) | Walls, vortices, skyrmions |
| Gross-Pitaevskii | Psi (complex scalar) | U(1) | Vortices |
| Ginzburg-Landau | Psi (complex scalar) | U(1) | Vortices, flux tubes |
| Nonlinear sigma | n (unit vector) | O(N) -> O(N-1) | Instantons, solitons |
| Sine-Gordon | phi (real scalar) | Z | Kinks |

All share: a nonlinear PDE for an order parameter, topological defect solutions,
a conserved topological charge, and energy barriers between topological sectors.

### 7.2 Integrability

In 1+1 dimensions, the LL equation (without damping) is completely integrable.
Lakshmanan (1977) showed it is equivalent to the nonlinear Schrodinger equation
via a gauge transformation. This means exact multi-soliton solutions exist,
and the equation can be solved by the inverse scattering transform.

In 2+1 and 3+1 dimensions, the LL equation is NOT integrable, and the dynamics
of topological defects must be studied numerically or perturbatively.


## 8. Connection to Phonon-Exflation Cosmology

### 8.1 Structural Parallel: LL Equation and GPE

The Landau-Lifshitz equation and the Gross-Pitaevskii equation share deep
structural similarities. Both describe the dynamics of a condensed state's order
parameter:

| Feature | LL Equation | GPE |
|:--------|:-----------|:----|
| Order parameter | M(r,t) / M_s in S^2 | Psi(r,t) in C |
| Ground state manifold | S^2 (sphere) | S^1 (circle, phase only) |
| Conservative dynamics | Precession (M x H) | Schrodinger flow |
| Dissipation | Gilbert damping | Phenomenological gamma |
| Topological defects | Domain walls, skyrmions | Vortices |
| Topological charge | pi_2(S^2) = Z | pi_1(S^1) = Z |
| Conserved quantities | |M|, energy, momentum | |Psi|^2 integral, energy |
| Symmetry breaking | O(3) -> O(2) | U(1) -> 1 |

The GPE simulation in the phonon-exflation project (phonon-exflation-sim/) is
solving exactly this type of equation. The vortex dynamics tracked by the
defect census code (defect_census.py, vortex_detection.py) is the U(1) analog
of the skyrmion dynamics governed by the LL equation.

### 8.2 Domain Walls as Cosmological Defects

In the phonon-exflation framework, topological defects in the BEC condensate
are interpreted as particles. The domain wall solutions of the LL equation
provide a template:

- **Domain wall profile** theta(x) = 2*arctan(exp(x/delta)) is the 1D soliton
- **Width** delta = sqrt(A/K) is determined by the competition between gradient
  energy (exchange) and potential energy (anisotropy)
- **Energy** sigma = 4*sqrt(A*K) is the tension (energy per unit area)

In the GPE context:
- The **healing length** xi plays the role of the domain wall width delta
- The **interaction energy** g*|Psi|^2 plays the role of the anisotropy
- The **quantum pressure** (hbar^2/(2m))*nabla^2 plays the role of exchange

### 8.3 Defect Dynamics and Particle Physics

The Landau-Lifshitz equation demonstrates a key principle exploited by
phonon-exflation: topological defects in a continuous medium behave as
PARTICLES. Domain walls have mass (energy), momentum, and interact with each
other and with spin waves (magnons). The scattering of spin waves off domain
walls has a well-defined cross section.

This is precisely the phonon-exflation claim: particles ARE topological defects
(or quasi-particle excitations) of the condensate, and their interactions
(scattering cross sections, decay rates) emerge from the underlying field
equation.

### 8.4 Energy Functional and the Spectral Action

The magnetic energy functional E[M] = E_ex + E_anis + E_Z + E_demag is
analogous to the spectral action:

    S = Tr(f(D^2/Lambda^2))

Both are functionals of a field configuration (M(r) or the geometry encoded in
D). Both contain:
- A "kinetic" term penalizing gradients (exchange <-> Seeley-DeWitt a_2 term)
- A "potential" term with minima that break symmetry (anisotropy <-> a_0 cosmological term)
- Long-range interactions (demagnetization <-> gravitational sector)

The critical point of E[M] (domain wall) is analogous to the critical point of
S(s) (the sought-after s_0 where V_eff is minimized).

### 8.5 Universality of Order Parameter Dynamics

The LL equation reinforces the central thesis: the mathematical structures of
condensed matter physics (order parameters, symmetry breaking, topological
defects, collective excitations) are not merely analogies for particle physics
-- they may be IDENTITIES. The phonon-NCG dictionary (Session 15) lists 9
verified identifications. The LL equation adds another: magnetization dynamics
and gauge field dynamics are both instances of order parameter evolution on a
symmetric space.

---

## References

1. L. D. Landau and E. M. Lifshitz, "On the theory of the dispersion of
   magnetic permeability in ferromagnetic bodies," Phys. Z. Sowjetunion 8,
   153-169 (1935). Reprinted in Collected Papers of L. D. Landau (Pergamon
   Press, 1965).
2. T. L. Gilbert, "A phenomenological theory of damping in ferromagnetic
   materials," IEEE Trans. Magn. 40, 3443-3449 (2004). [Reprint of 1955
   thesis.]
3. N. L. Schryer and L. R. Walker, "The motion of 180-degree domain walls
   in uniform dc magnetic fields," J. Appl. Phys. 45, 5406 (1974).
4. A. N. Bogdanov and D. A. Yablonskii, "Thermodynamically stable 'vortices'
   in magnetically ordered crystals. The mixed state of magnets," Sov. Phys.
   JETP 68, 101-103 (1989).
5. S. Muhlbauer et al., "Skyrmion lattice in a chiral magnet," Science 323,
   915-919 (2009).
6. M. Lakshmanan, "The fascinating world of the Landau-Lifshitz-Gilbert
   equation: an overview," Phil. Trans. R. Soc. A 369, 1280-1300 (2011).
