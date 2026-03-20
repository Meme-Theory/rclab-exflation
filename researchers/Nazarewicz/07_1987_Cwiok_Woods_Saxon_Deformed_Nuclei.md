# Single-Particle Energies, Wave Functions, Quadrupole Moments and g-Factors in an Axially Deformed Woods-Saxon Potential

**Author(s):** S. Cwiok, J. Dobaczewski, K. Heeger, A. Magierski, W. Nazarewicz

**Year:** 1987

**Journal:** Computer Physics Communications, Vol. 46, p. 379

---

## Abstract

An extensive computational study of the axially deformed Woods-Saxon potential is presented. Single-particle energies, normalized wave functions, quadrupole moments, and magnetic g-factors are calculated for a wide range of deformations, from near-spherical configurations to extreme shape elongations approaching fission into two fragments. The methodology employs an expansion of nuclear shape in spherical harmonics, allowing parametrization of arbitrary deformations including both prolate and oblate geometries. The results serve as a foundation for shell-model calculations of deformed and super-deformed nuclei and provide input for pairing interactions and collective model calculations.

---

## Historical Context

The deformed shell model, pioneered by Aage Bohr and Ben Mottelson, introduced the crucial insight that nuclei can possess permanent quadrupole deformation—no longer constrained to spherical shapes. The Nilsson model (using a deformed harmonic oscillator potential) became the standard tool for understanding deformed nuclei throughout the 1970s and 1980s.

However, the Nilsson model employs an idealized harmonic oscillator potential that diverges at large distances. The Woods-Saxon potential, by contrast, is a realistic mean-field potential with a diffuse surface reflecting the exponential density fall-off observed in experiments. The Cwiok-Dobaczewski-Nazarewicz work bridged this gap by providing comprehensive tabulations of deformed Woods-Saxon solutions, enabling more accurate shell structure calculations for deformed and transitional nuclei.

This seminal paper became the reference for all subsequent deformed shell-model calculations in the pre-density-functional-theory era and laid groundwork for computational codes used for decades.

---

## Key Arguments and Derivations

### Deformed Woods-Saxon Potential

The Woods-Saxon potential in spherical coordinates is:

$$U_{\text{WS}}(r) = -V_0 \frac{1}{1 + \exp[(r - R_0)/a]}$$

where $V_0$ (well depth) is ~50 MeV, $R_0 = r_0 A^{1/3}$ (nuclear radius with $r_0 \approx 1.25$ fm), and $a$ (surface thickness) is ~0.65 fm.

For an axially deformed nucleus, the nuclear radius is parametrized as:

$$R(\theta) = R_0 \left[ 1 + \sum_{k=1}^{\infty} \beta_{2k} Y_{2k}^0(\theta) \right]$$

where $\beta_{2k}$ are deformation parameters and $Y_{2k}^0$ are Legendre polynomials. In practice, expansions to $k=3$ or 4 are sufficient, giving:

$$R(\theta) \approx R_0 \left[ 1 + \beta_2 P_2(\cos\theta) + \beta_4 P_4(\cos\theta) + \ldots \right]$$

For prolate deformation (football-like), $\beta_2 > 0$; for oblate (disk-like), $\beta_2 < 0$. The deformed potential is:

$$U_{\text{def}}(\mathbf{r}) = -V_0 \frac{1}{1 + \exp[(r_{\text{deformed}} - R(\theta))/a]}$$

where $r_{\text{deformed}}$ is the distance measured perpendicular to the deformed surface.

### Single-Particle Hamiltonian with Spin-Orbit Coupling

The single-particle Schrödinger equation in the deformed potential is:

$$\left[ \frac{\mathbf{p}^2}{2m} + U_{\text{def}}(\mathbf{r}) + V_{\text{SO}}(r) \mathbf{L} \cdot \mathbf{S} + U_{\text{Coulomb}}(r) \right] \psi(\mathbf{r}) = \epsilon \psi(\mathbf{r})$$

The spin-orbit potential is:

$$V_{\text{SO}}(r) = \lambda_{\text{SO}} \frac{1}{2} \frac{d U_{\text{WS}}}{dr} \frac{1}{r}$$

with $\lambda_{\text{SO}} \approx 0.1$ fm$^2$ for nucleons. The coupling strength $V_{\text{SO}} \approx 5--10$ MeV at the nuclear surface and is crucial for producing the observed magic numbers (2, 8, 20, 28, 50, 82, 126).

### Numerical Solution via Finite Difference Method

The single-particle equation is solved numerically on a radial grid. For an axially symmetric potential, the wave function has the form:

$$\psi_{n_r, \Lambda, m_s}(\mathbf{r}) = R_{n_r, \Lambda}(r) \Phi_\Lambda(\phi) \chi_{m_s}(\sigma)$$

where $\Lambda$ is the projection of orbital angular momentum on the symmetry axis, $n_r$ indexes the radial nodes, $\Phi_\Lambda(\phi) = e^{i\Lambda\phi}$ is the azimuthal part, and $\chi_{m_s}$ is the spinor.

The radial Schrödinger equation becomes:

$$-\frac{\hbar^2}{2m} \frac{d^2 R}{dr^2} + \left[ U_{\text{eff}}(r) + \frac{\hbar^2 \Lambda(\Lambda \pm 1)}{2m r^2} \right] R = \epsilon R$$

where $U_{\text{eff}}(r)$ includes the deformed potential and spin-orbit term. Discretizing on a radial grid with spacing $\Delta r$ and applying outward integration from $r=0$ with inward integration from $r=\infty$, eigenvalues $\epsilon$ are found at matching points where the logarithmic derivatives coincide.

### Quadrupole Moments

The intrinsic quadrupole moment is:

$$Q_0 = \int d\mathbf{r} \, \psi^*(\mathbf{r}) e r^2 P_2(\cos\theta) \psi(\mathbf{r}) = e \left\langle r^2 P_2(\cos\theta) \right\rangle$$

For a deformed nucleus with coherent nucleon configurations, $Q_0$ is large and positive for prolate deformations, negative for oblate. The intrinsic quadrupole moment directly reflects the asphericity of the mean-field potential and is a key observable for testing shell-model predictions.

The calculation requires integration of the wave function density over space:

$$Q_0 = e \int_0^{\infty} dr \int_0^{\pi} d\theta \sin\theta \, r^2 P_2(\cos\theta) |\psi(r,\theta)|^2$$

For deformed nuclei in states with high K (aligned angular momentum on the symmetry axis), multiple nucleons contribute coherently, yielding large moments.

### Magnetic g-Factors

The magnetic g-factor relates the magnetic moment to angular momentum:

$$\mu = g \mu_N J$$

where $\mu_N = e\hbar / (2m_p)$ is the nuclear magneton. The single-particle g-factor is:

$$g_j = \frac{\langle \mathbf{J} \cdot \mathbf{\mu} \rangle}{\hbar^2 J(J+1)}$$

For a nucleon in an orbital with orbital angular momentum $\ell$ and spin $s=1/2$:

$$g_j = g_\ell \frac{\langle \mathbf{L} \cdot \mathbf{J} \rangle}{\hbar^2 J(J+1)} + g_s \frac{\langle \mathbf{S} \cdot \mathbf{J} \rangle}{\hbar^2 J(J+1)}$$

where $g_\ell = Z/A$ (orbital g-factor) and $g_s \approx 5.59$ (proton spin g-factor). The computation requires expectation values of $\mathbf{L} \cdot \mathbf{J}$ evaluated on the deformed wave functions.

---

## Key Results

1. **Shell Closure Energies**: Single-particle energy level spacing around magic closures (N/Z = 8, 20, 50, 82, 126) is reproduced with high accuracy using the Woods-Saxon + spin-orbit potential.

2. **Deformation-Dependent Level Ordering**: As deformation increases (e.g., for prolate nuclei with $\beta_2 = 0.4--0.6$), the level ordering changes significantly. Intruder orbitals—which lie high in energy at sphericity—lower and mix with traditional magic closures.

3. **Quadrupole Moments Spanning Decades**: Calculated Q$_0$ values range from nearly zero for magic nuclei to $\sim 10$ b (barns, 1 barn = 100 fm$^2$) for well-deformed nuclei, consistent with electromagnetic transition data.

4. **g-Factors and Magnetic Moments**: Predictions of single-particle g-factors are within a few percent of experiment when configuration mixing is included, validating the Woods-Saxon + spin-orbit model as a foundation for nuclear magnetism.

5. **Extreme Deformations**: For extremely elongated shapes ($\beta_2 > 1.0$) approaching the "necked-in" geometry preceding scission, the calculation remains stable, allowing investigation of fission dynamics.

6. **Transfer Reaction Form Factors**: Single-particle wave functions serve as input for transfer reaction calculations, enabling extraction of nuclear structure information from experimental cross sections.

---

## Key Equations

| Quantity | Expression |
|:---------|:-----------|
| Woods-Saxon potential | $U_{\text{WS}}(r) = -V_0 / (1 + \exp[(r - R_0)/a])$ |
| Deformed radius | $R(\theta) = R_0[1 + \beta_2 P_2(\cos\theta) + \beta_4 P_4(\cos\theta)]$ |
| Spin-orbit coupling | $V_{\text{SO}}(r) \mathbf{L} \cdot \mathbf{S}$ with $V_{\text{SO}} \approx \lambda (1/r)(dU/dr)$ |
| Intrinsic quadrupole moment | $Q_0 = e \langle r^2 P_2(\cos\theta) \rangle$ |
| Magnetic g-factor | $g_j = g_\ell \frac{\langle \mathbf{L} \cdot \mathbf{J} \rangle}{\hbar^2 J(J+1)} + g_s \frac{\langle \mathbf{S} \cdot \mathbf{J} \rangle}{\hbar^2 J(J+1)}$ |

---

## Connection to Phonon-Exflation Framework

The deformed Woods-Saxon potential provides an early glimpse into how mean-field deformations can emerge from nuclear interactions. In the phonon-exflation framework, nuclear deformations (quadrupole $\beta_2$, octupole $\beta_3$, etc.) are interpreted as collective phononic amplitudes of the internal SU(3) manifold.

Key implications:

1. **Deformation as Phonon Amplitude**: The quadrupole deformation parameter $\beta_2$ in Woods-Saxon calculations parallels the framework's treatment of $\beta_2$ as a coherent excitation of the internal geometry—where deformation corresponds to a shift in the metric tensor.

2. **Single-Particle Energies from Geometry**: In the Woods-Saxon model, the single-particle spectrum depends sensitively on the assumed deformation. In the phonon-exflation picture, the spectrum would arise from the Dirac operator eigenvalues on the deformed 3-manifold, with deformation affecting the eigenvalue distribution in exactly the way the Woods-Saxon potential demonstrates.

3. **Self-Consistency Problem**: The Woods-Saxon approach assumes a fixed deformation (external constraint). Modern HFB calculations determine deformation self-consistently from minimization of the energy functional. The phonon-exflation framework predicts that the self-consistent deformation should stabilize when the phonon density of states balances the cost of deforming the internal geometry.

4. **Magic Numbers from Topology**: The appearance of magic numbers (energy gaps) in the deformed shell structure hints at deeper topological structure—in the framework, magic numbers would reflect topological properties of the SU(3) manifold's spectral triple.

---

## References

- Nilsson, S.G. (1955). Binding states of individual nucleons in strongly deformed nuclei. Mat. Fys. Medd. Dan. Vid. Selsk. 29, No. 16.
- Mang, H.J. (1975). Deformed nuclei. In Encyclopedia of Physics, Vol. XXXVIII/2. Springer-Verlag.
- Davydov, A.S., Filippov, G.F. (1958). Rotational states in even nuclei. Nucl. Phys. 8, 237-249.

