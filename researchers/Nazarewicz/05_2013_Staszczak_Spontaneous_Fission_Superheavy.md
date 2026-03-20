# Spontaneous Fission Modes and Lifetimes of Superheavy Elements in Nuclear Density Functional Theory

**Author(s):** A. Staszczak, A. Baran, W. Nazarewicz

**Year:** 2013

**Journal:** Physical Review C, Vol. 87, p. 024320

---

## Abstract

Competing decay modes of even-even superheavy nuclei with atomic numbers Z=108--126 are studied within nuclear density functional theory augmented with the generator coordinate method (GCM) to describe configuration mixing. The key innovation is the explicit treatment of deformation: reflection-symmetric and reflection-asymmetric spontaneous fission modes are computed on equal footing. It is shown that breaking of axial and space-inversion symmetries lowers spontaneous fission barriers significantly, reducing predicted lifetimes by up to seven orders of magnitude in some isotopes. The interplay of alpha decay, beta decay, and spontaneous fission determines the region of observable superheavy nuclei, with predictions of long-lived isotopes in the so-called "island of stability."

---

## Historical Context

The quest for superheavy elements beyond uranium has motivated experimental and theoretical efforts for decades. Relativistic heavy-ion collisions produce superheavy nuclei by fusing lighter projectiles and targets. Each new synthesis—oganesson (Og, Z=118) confirmed in 2016—pushes against the limits of nuclear stability.

Early theoretical work employed the liquid drop model, predicting superheavy nuclei to be unstable against fission due to the Coulomb repulsion overwhelming nuclear attraction. However, shell effects (magic numbers) provide additional binding, creating pockets of enhanced stability. By the 2010s, density functional theory enabled self-consistent calculations of superheavy potential energy surfaces (PES), including deformation effects.

The Staszczak-Baran-Nazarewicz calculation was transformative because it demonstrated that reflection-asymmetric deformations (octupole shapes) fundamentally alter the fission landscape—a surprise that emerged only from fully self-consistent calculations.

---

## Key Arguments and Derivations

### Potential Energy Surface and Generator Coordinate Method

The potential energy surface (PES) $E(\beta_2, \beta_3, \ldots)$ expresses the total energy as a function of deformation parameters. In a self-consistent density functional approach:

$$E[\rho, \kappa][\beta] = \int d\mathbf{r} \, \epsilon_{\text{eff}}(\rho, \nabla\rho, \ldots) + E_{\text{Coulomb}}[\rho]$$

The deformation parameters $\beta_{\lambda\mu}$ describe multipole moments of the nuclear density, with $\beta_2$ (quadrupole) and $\beta_3$ (octupole) being the most important. For a nucleus with quadrupole deformation $\beta_2 \approx 0.5--0.8$ and octupole deformation $\beta_3 \approx 0.1--0.2$, the shape is pear-like rather than ellipsoidal.

The Generator Coordinate Method (GCM) goes beyond the static PES by treating the deformation as a dynamic variable. The many-body wave function is:

$$|\Psi \rangle = \int d\beta_2 d\beta_3 \, f(\beta_2, \beta_3) |\Psi[\beta_2, \beta_3] \rangle$$

where $|\Psi[\beta]  \rangle$ are constrained Hartree-Fock-Bogoliubov solutions at fixed deformation. The weights $f(\beta)$ are determined by solving the GCM equations:

$$\int d\beta' \, G(\beta, \beta')[E - H(\beta')] f(\beta') = 0$$

where $G(\beta, \beta') = \langle \Psi[\beta] | \Psi[\beta'] \rangle$ is the overlap kernel. This enables configuration mixing and tunneling through fission barriers.

### Reflection-Asymmetric Shapes

In traditional nuclear structure, parity conservation constrains the Hamiltonian and wave functions to be either even or odd under the parity operation $\mathcal{P}: \mathbf{r} \to -\mathbf{r}$. However, this symmetry is not fundamental—it emerges as an approximate symmetry in most nuclei because the mean field is relatively spherical.

In superheavy nuclei with large deformations, reflection asymmetry (octupole deformation, $\beta_3 \neq 0$) becomes energetically favorable. The octupole deformed shape has intrinsic dipole moment:

$$D_0 = \int d\mathbf{r} \, z \, \rho(\mathbf{r})$$

For a nucleus with neutron number N and proton number Z, the octupole deformation energy is:

$$E_{\text{oct}} = E_{\text{surface}} + E_{\text{Coulomb}} + E_{\text{pair}} + \ldots$$

The surface energy favors small deformations. The Coulomb energy is minimized by spreading the charge (favoring large deformation). Pairing energy is modified by the altered single-particle spectrum induced by deformation. The balance determines whether octupole shapes are energetically preferred.

### Spontaneous Fission Barrier

The fission barrier is the maximum of the potential energy surface along the fission path. For a typical superheavy nucleus, the PES exhibits:

1. **Ground state minimum**: Typically at small quadrupole deformation ($\beta_2 \approx 0.4--0.6$) with octupole deformation either zero or small ($\beta_3 \lesssim 0.1$).

2. **First barrier**: Occurs at intermediate deformation ($\beta_2 \approx 1.0--1.5$, $\beta_3 \approx 0.1--0.3$). Height above ground state: $B_f \approx 6--7$ MeV.

3. **Isomeric state (second minimum)**: A secondary minimum at larger deformations, sometimes appearing between the first and second barriers.

4. **Second barrier**: A second ridge, lower than the first in superheavy nuclei.

### Spontaneous Fission Lifetimes

The spontaneous fission half-life is predicted using the WKB tunneling formula:

$$T_{1/2}^{SF} = \frac{\ln(2) \hbar}{2 \pi} \int_{R_{\text{inner}}}^{R_{\text{outer}}} \frac{dR}{D(R) (R_{\text{outer}} - R_{\text{inner}})} \exp\left( 2 \int_{R_{\text{inner}}}^{R} \frac{\sqrt{2m_{\text{eff}} B(R')}}{R_{\text{outer}} - R_{\text{inner}}} dR' \right)$$

where $D(R)$ is the dynamics (collective inertia tensor), $B(R)$ is the barrier height above the ground state, and $R$ parametrizes the fission coordinate. A small decrease in barrier height yields an exponential increase in lifetime—a 1 MeV reduction can change the lifetime by orders of magnitude.

### Reflection-Asymmetric Barrier Lowering

The critical finding is that including octupole deformation in the barrier calculation lowers the first fission barrier by 0.5--2 MeV in superheavy nuclei (Z > 100). This occurs because:

1. Octupole deformation increases the nuclear surface area at fixed volume, favoring Coulomb repulsion.
2. But the tensor force (effective in neutron-rich systems) and residual pairing interactions generate attractive octupole correlations.
3. The balance shifts with Z: for lighter nuclei, octupole shapes are energetically unfavorable; for superheavy nuclei with Z > 102, octupole deformations become competitive or favored.

The barrier lowering translates to spontaneous fission lifetimes reduced by factors of 10$^3$ to 10$^7$ compared to calculations omitting octupole deformations.

---

## Key Results

1. **Octupole-Driven Fission**: Reflection-asymmetric shapes are essential for quantitative predictions of superheavy fission barriers. Omitting octupole deformations yields unphysically long lifetimes.

2. **Island of Stability Redefined**: The region of long-lived superheavy nuclei is predicted to center on $^{294}$Ds (darmstadium, Z=110) with a half-life $\approx 1.5$ days, rather than at the often-quoted $^{298}$Fl (flerovium).

3. **Competing Decay Modes**: For Z > 110, alpha decay, beta-minus decay, and spontaneous fission all compete. The predicted half-lives vary over 20 orders of magnitude across the superheavy region.

4. **Triaxiality**: Minimum-energy shapes include triaxial (non-axisymmetric) configurations, predicting ground-state spins and deformations that differ from older axially-symmetric models.

5. **Configuration Mixing**: GCM treatment of mixing enhances tunneling rates by accounting for correlations between deformation configurations—a purely mean-field calculation underestimates tunneling probability.

---

## Key Equations

| Quantity | Expression |
|:---------|:-----------|
| Potential energy surface | $E(\beta) = T_{\text{rot}} + E_{\text{mean-field}}(\beta) + E_{\text{pair}}(\beta)$ |
| GCM overlap kernel | $G(\beta, \beta') = \langle \Psi[\beta] \| \Psi[\beta'] \rangle$ (Slater determinant overlap) |
| Octupole deformation energy | $E_{\text{oct}} \propto \left( \int d\mathbf{r} \, r^3 Y_3^0(\theta) \rho(\mathbf{r}) \right)^2$ |
| Spontaneous fission half-life | $T_{1/2}^{SF} = \ln(2) / \lambda_f$ where $\lambda_f = \nu \exp(-B/\hbar\omega)$ |
| WKB tunneling exponent | $\exp \left( -\frac{2}{\hbar} \int_a^b \sqrt{2m_{\text{eff}}(E - V(x))} \, dx \right)$ |

---

## Connection to Phonon-Exflation Framework

The spontaneous fission of superheavy nuclei exemplifies how nuclear shape dynamics emerge from competing microscopic mechanisms. In the phonon-exflation framework, nuclear deformations are collective excitations of the internal SU(3) geometry. The appearance of spontaneous reflection-asymmetric shapes in superheavy nuclei suggests that the compactified metric can itself undergo symmetry-breaking deformations.

Key implications:

1. **Geometric Instabilities**: In NCG (noncommutative geometry) on SU(3), the Dirac operator spectrum depends sensitively on the metric. Spontaneous octupole deformation would correspond to an instability of the round metric toward a pear-shaped configuration—a phenomenon that could arise from the spectral action if its potential possesses multiple minima.

2. **Barrier Tunneling as Phonon Tunneling**: The WKB tunneling formula can be reinterpreted as tunneling in the space of collective phonon amplitudes. In the framework, fission corresponds to a phonon-mediated collective coordinate evolving from one geometric configuration to another.

3. **Superheavy Elements as Probes**: Superheavy nuclei push the density, temperature, and neutron excess to extremes where collective phonon modes become strongly anharmonic. The surprising role of octupole deformations hints that the phonon spectrum of the internal compactification itself may become unstable in high-energy regimes.

4. **Coulomb and Strong Force Balance**: The Staszczak-Baran-Nazarewicz calculation reveals an exquisite balance between Coulomb repulsion (favoring fission) and strong nuclear attraction (opposing it), with deformation effects providing crucial corrections. In the phonon-exflation picture, this balance would reflect the interplay between the internal geometry's elastic properties (resisting distortion) and external forces coupling to its collective modes.

---

## References

- Sierk, A.J. (1986). Macroscopic model of rotating nuclei. Phys. Rev. C 33, 2039-2052.
- Bjørnholm, S., Lynn, J.E. (1980). The double-humped fission barrier. Rev. Mod. Phys. 52, 725-931.
- Hilaire, S., Girod, M. (2007). Large deformations of superheavy nuclei. Phys. Lett. B 646, 24-31.

