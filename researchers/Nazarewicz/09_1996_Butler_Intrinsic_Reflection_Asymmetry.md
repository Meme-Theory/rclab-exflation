# Intrinsic Reflection Asymmetry in Atomic Nuclei

**Author(s):** P.A. Butler, W. Nazarewicz

**Year:** 1996

**Journal:** Reviews of Modern Physics, Vol. 68, pp. 349-421

---

## Abstract

A comprehensive review of the experimental and theoretical evidence for intrinsic reflection-asymmetric (parity-violating) shapes in nuclei is presented. The theoretical methods cover mean-field approaches (Hartree-Fock-Bogoliubov with octupole deformation), algebraic approaches, and cluster models. Experimental data for nuclear ground states at low and high spin are surveyed, along with extensive compilation of electric dipole transition moments and electric octupole moments. The work demonstrates that atomic nuclei can develop stable octupole deformations—pear-shaped geometries that break the inversion symmetry—in specific regions of the nuclear chart, particularly the actinides and certain heavy isotopes. The fundamental mechanisms driving octupole instability are elucidated and the astrophysical implications discussed.

---

## Historical Context

Parity conservation was long considered a fundamental law of nature, until its violation in the weak interaction was discovered in 1956. In nuclear physics, the strong nuclear force conserves parity exactly, yet nuclei can spontaneously violate parity through deformation. This paradox—exact parity conservation of the underlying Hamiltonian coupled with spontaneous parity breaking in the ground state—exemplifies symmetry-breaking mechanisms central to modern physics.

The first experimental hints of octupole deformation came from anomalous electric dipole moments (E1 transitions) in certain nuclei, including Ra-223 and actinides like U-238. By the 1990s, accumulating spectroscopic evidence from Coulomb excitation, muonic atoms, and beta-decay correlations pointed unambiguously to parity violation in several nuclei. The Butler-Nazarewicz review synthesized disparate threads of theory and experiment into a coherent picture, establishing octupole deformation as a genuine and widespread nuclear phenomenon.

---

## Key Arguments and Derivations

### Octupole Deformation and Parity Violation

A nucleus with intrinsic octupole deformation breaks the parity operation $\mathcal{P}: \mathbf{r} \to -\mathbf{r}$ spontaneously. The monopole moment (charge) is invariant: $\langle Z \rangle = 0$ (on average). But the dipole moment:

$$\langle D_0 \rangle = \int d\mathbf{r} \, z \, \rho(\mathbf{r}) = \int_0^{\pi} d\theta \sin\theta \cos\theta \left[ \rho_n(r,\theta) + \rho_p(r,\theta) \right] r^3 dr$$

is nonzero for an octupole-deformed shape. The octupole deformation parameter is defined via the multipole expansion:

$$R(\theta) = R_0 \left[ 1 + \sum_k \beta_{2k} P_{2k}(\cos\theta) \right]$$

For octupole ($k=1$, $\lambda=3$), the deformation enters at odd multipolarity:

$$R(\theta) = R_0 [1 + \beta_2 P_2(\cos\theta) + \beta_3 P_3(\cos\theta)]$$

where $P_3(\cos\theta) = \frac{1}{2}(5\cos^3\theta - 3\cos\theta)$ is the Legendre polynomial. The $\beta_3$ term breaks parity—under $\theta \to \pi - \theta$ (parity operation), $P_3$ changes sign, while $P_2$ does not.

### Mean-Field Calculation of Octupole Stability

Within Hartree-Fock-Bogoliubov theory, the total energy is:

$$E[\rho, \kappa; \beta_2, \beta_3] = \langle H \rangle = T + V_{\text{mean-field}} + V_{\text{pair}} + V_{\text{Coulomb}}$$

The single-particle kinetic energy increases with deformation:

$$T[\beta] = \int d\mathbf{r} \, \frac{\hbar^2}{2m} \nabla^2 \rho(\mathbf{r})$$

The mean-field energy—evaluated in a deformed Woods-Saxon or Skyrme potential—also increases, disfavoring large deformation. However, certain combinations of nucleons create favorable shell effects for octupole shapes.

The pairing energy is modified by the deformed spectrum:

$$E_{\text{pair}} = -G \sum_{k,k'} u_k u_{k'} v_k v_{k'} = -\sum_{\alpha > \beta} V_{\alpha\beta} \rho_{\alpha\beta}$$

where $G$ is the pairing strength and $\rho_{\alpha\beta}$ are pair occupation probabilities. In an octupole-deformed mean field, the single-particle spectrum itself changes, altering the pairing correlations. For nuclei with certain magic number configurations, the spectrum reorganization creates favorable pairing binding in octupole-deformed configurations.

The Coulomb energy increases with surface area (favoring compact shapes) but also with asymmetry (favoring shape separation that creates dipole moment). The balance is:

$$E_{\text{Coulomb}} \approx 0.7 \frac{Z^2 e^2}{R_0} \left[ 1 + (0.03)\beta_2^2 + (0.05)\beta_3^2 + \ldots \right]$$

### Octupole Instability Condition

For a nucleus to spontaneously deform octupole, the second derivative of energy with respect to $\beta_3$ must be negative:

$$\frac{\partial^2 E}{\partial \beta_3^2}\bigg|_{\beta_3=0} < 0$$

This condition is satisfied in specific regions of the nuclear chart where shell effects overcome the surface and Coulomb cost of octupole deformation. The regions include:

1. **Actinides** (Ra, Ac, Th, Pa, U, Np, Pu): N ~ 134--140, Z ~ 88--94
2. **Radium isotopes**: Z = 88, N ~= 134--138
3. **Neutron-rich light nuclei**: N ~ 20 (in N ~ 20 region), where octupole shells close at N = 14, 20.

### Electric Dipole Transitions and Octupole Moments

An electric dipole transition connects states of opposite parity, and its strength is:

$$B(E1; I \to I') = \frac{e^2}{4\pi(2I+1)} |\langle I' || \mathbf{D} || I \rangle|^2$$

where $\mathbf{D}$ is the dipole operator. In octupole-deformed nuclei, parity-doublet bands appear—pairs of states with the same spin and angular momentum projection but opposite intrinsic parity. The E1 transitions between levels of the two bands (negative and positive parity) exhibit anomalously large transition strengths, a smoking gun for octupole deformation.

The electric octupole moment (E3 transition strength) is:

$$B(E3; 0^+ \to 3^-) = \frac{e^2}{4\pi} |\langle 3^- || \mathcal{Q}_3 || 0^+ \rangle|^2$$

where $\mathcal{Q}_3 \propto \sum_i r_i^3 P_3(\cos\theta_i)$ is the octupole operator. Large E3 strengths signal octupole deformation in the ground state.

### Hartree-Fock-Bogoliubov Solutions with Octupole Constraint

The HFB equations are solved with constraint on the octupole moment:

$$Q_3 = \langle 0 | \sum_i (r_i^3 / 2) P_3(\cos\theta_i) | 0 \rangle = \text{fixed}$$

This generates a one-dimensional curve $E(Q_3)$ in configuration space. If this curve possesses a minimum at $Q_3 \neq 0$, octupole deformation is energetically favored.

---

## Key Results

1. **Confirmed Octupole Deformation**: Ground states of Ra-223, Ra-225, Ac-225, Ra-226, Th-229, and several actinides exhibit intrinsic octupole deformation, confirmed by measurements of E1 transition strengths 100--1000 times larger than single-particle estimates.

2. **Parity Mixing**: Parity-violating transitions appear in electric dipole strengths. The admixture of negative-parity configurations in ostensibly positive-parity states ranges from 1% to 10%, measurable via electron scattering and muonic atom spectroscopy.

3. **Octupole Moments**: Measured octupole deformation moments Q$_3$ reach values of 10--20 b*fm (where b = barn = 100 fm$^2$), confirming substantial parity breaking.

4. **Regional Stability**: The actinide region (Z ~ 88--94, N ~ 134--140) exhibits the strongest and most systematic octupole effects, consistent with shell-model predictions of magic numbers at N = 126, 184 creating favorable configurations.

5. **High-Spin Implications**: Octupole deformations persist to high angular momentum, affecting the yrast sequence and occasionally dominating the ground-state rotational properties.

6. **Theoretical Mechanism**: Correlation between octupole instability and shell structure closure in certain single-particle configurations demonstrates that octupole deformation is fundamentally driven by mean-field effects, not collective phonon modes (though phonons couple to the deformation).

---

## Key Equations

| Quantity | Expression |
|:---------|:-----------|
| Octupole deformation parameter | $\beta_3$ (coefficient of $P_3(\cos\theta)$ in radius expansion) |
| Dipole moment from deformation | $D_0 \sim Z \langle r^3 \rangle \beta_3$ |
| Octupole instability condition | $\partial^2 E / \partial \beta_3^2 \|_{\beta_3=0} < 0$ |
| Electric dipole strength | $B(E1) = (e / 4\pi(2I+1)) \|\langle I' \| D \| I \rangle\|^2$ |
| Octupole moment | $Q_3 = \int d\mathbf{r} (r^3/2) P_3(\cos\theta) \rho(\mathbf{r})$ |
| Parity mixing ratio | $\delta = \sqrt{B(E1) / (e^2 a_0^2)}$ (related to parity admixture) |

---

## Connection to Phonon-Exflation Framework

Octupole deformation in nuclei provides a striking example of how fundamental symmetries (parity) can be spontaneously broken by the mean field. In the phonon-exflation framework, octupole deformations would correspond to collective excitations of the internal SU(3) manifold that break spatial inversion symmetry.

Key implications:

1. **Asymmetric Phonon Modes**: The phonon spectrum of the internal geometry would include odd-parity (dipole and octupole) excitation modes. In nuclei where such modes become energetically favorable relative to the ground state metric, they can drive deformations that break parity.

2. **Dynamical Symmetry Breaking**: The framework predicts that parity breaking in nuclear ground states reflects an instability of the phonon spectrum—when odd-parity phonon frequencies become imaginary (negative mass-squared), the system spontaneously cascades into an asymmetric state.

3. **Pairing Enhancement at Octupole Deformation**: The Butler-Nazarewicz analysis reveals that octupole deformation sometimes improves pairing correlations (certain shell configurations bind more strongly in deformed geometry). In the framework, this would reflect a feedback: the pairing modes of the internal manifold are enhanced when the background geometry deforms to match the phonon's natural frequency.

4. **Parity Violation Scale**: The magnitude of parity breaking ($\beta_3 \sim 0.1--0.3$) appears modest compared to quadrupole deformation ($\beta_2 \sim 0.4--0.6$). In the framework, this difference would reflect the different stiffnesses of the internal metric against even vs. odd-parity distortions, with odd-parity deformations being less energetically favorable.

5. **Astrophysical Consequences**: The framework's treatment of nuclear pairing and deformation directly impacts predictions for beta decay rates and neutron-capture cross sections in the r-process, with potential implications for kilonova spectra in neutron star mergers.

---

## References

- Spevak, V., Aberg, S., Flocard, H. (1990). Configuration-dependent octupole deformations in the actinide region. Nucl. Phys. A 504, 139-167.
- Frauendorf, S., Macchiavelli, A.O. (2000). Reflection-asymmetric shapes in nuclei. Nucl. Phys. News 10, 5-12.
- Nazarewicz, W., Wyss, R. (1992). Structure and decay of superheavy elements. In Nuclear and Atomic Physics Applications of the Exotic Nuclei. JINR, Dubna.

