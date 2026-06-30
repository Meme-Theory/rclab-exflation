# Exotic Lifshitz Transitions in Topological Materials

**Author(s):** G.E. Volovik
**Year:** 2017
**Journal:** [INCOMPLETE - not explicitly stated in PDF; appears to be a review/conference paper]
**arXiv:** 1701.06435
**Relevance:** HIGH

---

## Abstract

Topological Lifshitz transitions involve many types of topological structures in momentum and frequency-momentum spaces: Fermi surfaces, Dirac lines, Dirac and Weyl points, etc. Each of these structures has their own topological invariant ($N_1$, $N_2$, $N_3$, $\tilde{N}_3$, etc.), which supports the stability of a given topological structure. The topology of the shape of Fermi surfaces and Dirac lines, as well as the interconnection of the objects of different dimensions, lead to numerous classes of Lifshitz transitions. The consequences of Lifshitz transitions are important in different areas of physics. The singularities emerging at the transition may enhance the transition temperature to superconductivity; the Lifshitz transition can be in the origin of the small masses of elementary particles in our Universe; the black hole horizon serves as the surface of Lifshitz transition between the vacua with type-I and type-II Weyl points; etc.

---

## Key Arguments and Derivations

### Topological Objects in Momentum Space (Section I)

Volovik classifies topologically stable nodes in fermionic spectra by three types of topological invariants:

1. **Fermi surface** ($N_1$): A singularity in the Green's function forming a vortex ring in 4D $(p,\omega)$-space. The winding number $N_1 = \mathrm{tr}\oint_C \frac{dl}{2\pi i}G\partial_l G^{-1}$ provides stability against interactions -- this is the origin of Landau Fermi liquid theory. The Fermi surface cannot have edges (analogous to vortex lines not terminating in bulk).

2. **Weyl point** ($N_3$): A hedgehog (monopole) in 3D momentum space, with invariant:
$$N_3 = \frac{\epsilon^{\mu\nu\rho\sigma}}{24\pi^2}\mathrm{tr}\oint_{\Sigma_a} dS_\sigma\,G\frac{\partial G^{-1}}{\partial p_\mu}G\frac{\partial G^{-1}}{\partial p_\nu}G\frac{\partial G^{-1}}{\partial p_\rho}$$
This is a Berry phase monopole. The topological charge $N_3 = \pm 1$ protects massless Weyl fermions. Higher topological charges ($|N_3| > 1$) produce non-"relativistic" (non-linear) dispersions.

3. **Dirac line** ($N_2$): A vortex line in 3D momentum space with invariant $N_2 = \frac{1}{4\pi i}\mathrm{tr}\oint K\,dl\,H^{-1}\partial_l H$. Examples include the nodal line in the polar phase of 3He.

### Fermi Surface Lifshitz Transitions (Section II)

**Original Lifshitz transition:** Change of topology of the Fermi surface without symmetry breaking, when the Fermi surface crosses a stationary point of the electronic spectrum. Near the transition: $\epsilon_p = ap_x^2 + bp_y^2 + cp_z^2 - \mu$. For $a > 0, b > 0, c < 0$, the neck disruption at $\mu = 0$ is equivalent to reconnection of vortex lines in $(p,\omega)$-space -- analogous to vortex reconnection in turbulence.

**Pole to zero transition:** The Green's function residue can be suppressed to the point where the pole becomes a zero ($G \propto i\omega + \epsilon(p)$), as in Mott insulators. The topological invariant $N_1$ is preserved (Luttinger theorem remains valid even in the insulating phase).

**Flat band formation:** Strong electron-electron interactions can convert a Fermi surface into a "flat band" (Khodel-Shaginyan fermion condensate) where all states have zero energy. The superconducting $T_c$ becomes linear in coupling ($T_c \sim g V_{\mathrm{FB}}$) rather than exponentially suppressed. Flat bands form preferentially near conventional Lifshitz transitions. Possible relevance to high-$T_c$ superconductivity in pressurized sulfur hydride ($H_3S$).

### Weyl Point Lifshitz Transitions (Section III)

**Weyl point pair creation:** The typical transition involves formation of Weyl points with opposite charges $N_3 = \pm 1$ from a fully gapped state (massive Dirac vacuum). The intermediate state has a massless Dirac point with $N_3 = 0$.

**BEC-BCS crossover:** The transition from BEC (strong coupling, fully gapped) to BCS (weak coupling, gapless) is a Lifshitz transition with formation of Weyl points. In the $O(D_2)$ symmetry class, 4 right-handed and 4 left-handed Weyl points form at cube vertices, with total $N_3 = 0$ (fermion doubling). Each Standard Model generation contains 8 left and 8 right Weyl particles.

**Type-I to Type-II Weyl transition:** The Hamiltonian $H = c\boldsymbol{\sigma}\cdot\mathbf{p} - vp_z$ has a Weyl cone that tilts with increasing $v$. At $v > c$, the cone is "overtilted" forming two Fermi pockets connected by a type-II Weyl point. The transition at $v = c$ is a Lifshitz transition that enhances superconducting $T_c$.

### Black Hole Horizon as Lifshitz Transition Surface (Section III.D)

The Painleve-Gullstrand metric $ds^2 = -c^2\,dt^2 + (dr - v\,dt)^2$ with frame-dragging velocity $v(r) = -\hat{r}c\sqrt{r_h/r}$ describes a black hole. The Weyl fermion Hamiltonian in this gravitational field:
$$H = \pm c\boldsymbol{\sigma}\cdot\mathbf{p} - p_r v(r)$$

Behind the horizon ($v > c$), the Weyl cone is overtilted, forming type-II Weyl points with Fermi pockets. The event horizon at $r = r_h$ is therefore the surface of Lifshitz transition between type-I Weyl vacuum (outside) and type-II Weyl vacuum (inside).

This correspondence enables simulation of black hole horizons in inhomogeneous Weyl semimetals where the type-I/type-II transition surface acts as an event horizon. The relaxation process after creation of such an analogue looks similar to Hawking radiation.

**Type-III transition:** When $g^{00}$ changes sign (instead of $g_{00}$), one obtains type-III Weyl fermions in semimetals, or spacetimes with closed timelike curves in GR.

### Hierarchy Problem and Lifshitz Transitions (Section VI)

The observation that the most massive particle ($\sim 10^2$ GeV) is tiny compared to the Planck scale ($\sim 10^{19}$ GeV) implies the vacuum is practically gapless. Two topological scenarios:

1. **Weyl scenario:** The quantum vacuum belongs to the Fermi point universality class; physical laws emerge near Weyl points; masslessness is topologically protected.

2. **Topological quantum phase transition scenario:** Massless vacua emerge at Lifshitz transitions between fully gapped vacua with different topological charges. The Universe sits near the line of topological Lifshitz transition, where fermions are necessarily gapless. This is the topological analog of the Multiple Point Principle (Universe lives at the coexistence point of first-order phase transitions).

---

## Key Results

1. Lifshitz transitions are classified by the interplay of topological invariants $N_1$ (Fermi surface), $N_2$ (Dirac line), $N_3$ (Weyl point) in momentum space.
2. The Fermi surface is topologically stable (vortex in $(p,\omega)$-space), which is the microscopic origin of Landau Fermi liquid theory.
3. Flat bands from strong interactions near Lifshitz transitions can enhance superconducting $T_c$ from exponentially suppressed to linear in coupling.
4. The black hole horizon is a Lifshitz transition surface between type-I and type-II Weyl vacua.
5. The BEC-BCS crossover is a Lifshitz transition with Weyl point formation.
6. The hierarchy problem may be explained by the Universe being near a topological Lifshitz transition where fermion masslessness is enforced.
7. Each Standard Model generation has 8+8 Weyl fermions at cube vertices in $(p_x,p_y,p_z,\omega)$-space, with total $N_3 = 0$.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Green's function (free) | $G^{-1}(\omega,\mathbf{p}) = i\omega - \epsilon(\mathbf{p})$ | Eq. (1) |
| Fermi surface invariant | $N_1 = \mathrm{tr}\oint_C \frac{dl}{2\pi i}G\partial_l G^{-1}$ | Eq. (2) |
| Generic Lifshitz spectrum | $\epsilon_p = ap_x^2 + bp_y^2 + cp_z^2 - \mu$ | Eq. (3) |
| Non-Landau Green's function | $G = Z/(i\omega - \epsilon)$, $Z \propto (\omega^2 + \epsilon^2)^\gamma$ | Eq. (4) |
| Pole-to-zero | $G \propto i\omega + \epsilon(\mathbf{p})$ (at $\gamma = 1$) | Eq. (5) |
| Weyl point invariant | $N_3 = \frac{\epsilon^{\mu\nu\rho\sigma}}{24\pi^2}\mathrm{tr}\oint dS_\sigma\,G\partial_\mu G^{-1}G\partial_\nu G^{-1}G\partial_\rho G^{-1}$ | Eq. (6) |
| Type-I/II Weyl Hamiltonian | $H = c\boldsymbol{\sigma}\cdot\mathbf{p} - vp_z$ | Eq. (7) |
| Painleve-Gullstrand metric | $ds^2 = -c^2\,dt^2 + (dr - v\,dt)^2$ | Eq. (8) |
| BH frame dragging | $v(r) = -\hat{r}c\sqrt{r_h/r}$, $r_h = 2MG/c^2$ | Eq. (9) |
| Weyl in BH field | $H = \pm c\boldsymbol{\sigma}\cdot\mathbf{p} - p_r v(r)$ | Eq. (10) |
| Flat band $T_c$ | $T_c \sim \Delta = gV_{\mathrm{FB}}$ (linear, not exponential) | Sec. II.D |
| BCS $T_c$ | $T_c \sim \Delta = E_c\exp[-1/(gN(0))]$ (exponentially suppressed) | Sec. II.D |

---

## Relevance to Phonon-Exflation

This paper connects directly to the framework's mechanism chain in several ways. The BEC-BCS Lifshitz transition (Section III.B) is the same physics as the framework's BCS instability link: the transition from a gapped (BEC) vacuum to a gapless (BCS) vacuum with Weyl point formation. The flat band enhancement of $T_c$ (Section II.D) parallels the framework's van Hove singularity mechanism -- both involve enhanced density of states near topological transitions driving pairing instabilities. The black hole horizon as a Lifshitz transition surface between type-I and type-II Weyl vacua provides a momentum-space interpretation of horizons that complements the real-space acoustic metric picture; in the framework, the fiber transit (changing $\tau$) drives the effective vacuum through topological transitions analogous to these Lifshitz transitions. The hierarchy problem discussion (Section VI) -- the Universe sits near a topological phase transition where fermion masslessness is enforced -- directly supports the framework's claim that the fold in the SU(3) fiber geometry (a topological feature) determines the mass hierarchy. The invariant $N_3$ protecting Weyl fermions is the same topological charge that protects the framework's chiral fermion spectrum from perturbative corrections.
