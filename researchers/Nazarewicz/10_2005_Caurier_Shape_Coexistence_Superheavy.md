# Shape Coexistence and Triaxiality in the Superheavy Nuclei

**Author(s):** E. Caurier, K. Sieja, W. Nazarewicz

**Year:** 2005

**Journal:** Nature, Vol. 433, pp. 705-709

---

## Abstract

Theoretically predicted competing low-lying configurations in superheavy nuclei are investigated within the nuclear density functional framework augmented with configuration interaction in a restricted model space. The calculations reveal an unexpected wealth of competing shapes—spherical, prolate, oblate, and triaxial deformations—that coexist at low excitation energy in a single nucleus. The shape coexistence arises from the delicate balance between nuclear attraction and Coulomb repulsion, modulated by single-particle shell effects. Predictions of relative energies, moments of inertia, and transition probabilities are made for superheavy isotopes including E114, E120, and beyond, providing guidance for experimental searches.

---

## Historical Context

Superheavy element synthesis reached a milestone in 2004-2006 with the confirmed production of element 118 (oganesson). Each new synthesis pushed nuclear physics toward uncharted territory: nuclei with Z > 100 where Coulomb repulsion reaches toward 50% of the nuclear binding energy, yet mysterious shell closures ("magic numbers") at Z = 114 or Z = 126 were theoretically predicted to create pockets of surprising stability.

Traditional nuclear models—applied successfully to actinides and lighter nuclei—failed to produce coherent predictions for superheavy properties. A critical insight emerged: in the superheavy region, the potential energy landscape becomes extraordinarily flat, with many competing deformed configurations lying within a few hundred keV of the ground state. This "shape isomerism" (multiple competing shapes in the same nucleus) had been observed in lighter systems, but superheavy nuclei promised to exhibit it in the most extreme form.

The Caurier-Sieja-Nazarewicz 2005 Nature paper was transformative because it demonstrated that shape coexistence in superheavy nuclei is not an exotic accident but a natural consequence of the nuclear force balance near the drip line and in the regime of extreme Coulomb stress.

---

## Key Arguments and Derivations

### Potential Energy Surface in Superheavy Nuclei

The potential energy surface (PES) as a function of deformation is computed via the Gogny-D1S energy density functional:

$$E[\rho, \kappa; \beta_2, \beta_3, \gamma] = \langle \psi | H | \psi \rangle$$

where $\beta_2$ is quadrupole deformation (prolate if positive), $\gamma$ is the triaxiality parameter ($\gamma = 0$ for axisymmetric, $\gamma = 30°$ for maximally triaxial), and $\beta_3$ is octupole deformation. The PES is computed on a two-dimensional grid in deformation space.

For superheavy nuclei, the liquid drop model predicts:

$$E_{\text{LDM}} \approx a_v A^{2/3} [1 + \alpha_2 \beta_2^2 + \alpha_4 \beta_4^2 + \ldots] - a_s (Z-Z_{\text{magic}})^2 / A^{1/3}$$

The surface energy coefficient $a_s \approx 72$ MeV increases with surface area, disfavoring large deformations. The Coulomb repulsion energy is:

$$E_C \approx \frac{3}{5} \frac{e^2 Z^2}{R_0} \left[ 1 + 0.03 \beta_2^2 + \ldots \right]$$

For Z = 114, $E_C / E_v \approx 1/3$, comparable to the volume binding. For Z = 126, Coulomb becomes even more important.

### Shell Effects and Closed-Shell Configurations

The fundamental source of shape coexistence is the shell structure. Single-particle levels in deformed potentials depend strongly on deformation. For a prolate nucleus (football-shaped, $\beta_2 > 0$), the Nilsson levels are:

$$\epsilon = \epsilon_0 + a\beta_2 + b\beta_2^2 + \ldots$$

with different slopes for different orbitals. As deformation increases, orbitals cross: an orbital might lie above the Fermi surface at sphericity ($\beta_2 = 0$) but below (occupied) at larger deformation.

In superheavy nuclei near Z = 114, two single-particle magic numbers compete: the spherical closure at Z = 114 (from relativistic effects) and a prolate deformed closure at slightly higher energy. When both configurations are accessible (within the pairing window $\sim 10$ MeV), both can serve as reference configurations for Hartree-Fock calculations.

### Generator Coordinate Method with Configuration Mixing

To treat shape coexistence properly, the Generator Coordinate Method is employed. Define collective coordinates:

$$\boldsymbol{q} = (\beta_2, \gamma, \beta_3, \ldots)$$

For each deformation, a constrained HFB calculation yields a state $|\Psi[\boldsymbol{q}]\rangle$. The full wave function is:

$$|\Psi_\alpha \rangle = \int d\boldsymbol{q} \, f_\alpha(\boldsymbol{q}) |\Psi[\boldsymbol{q}]\rangle$$

The weights $f_\alpha(\boldsymbol{q})$ are determined by the GCM equation:

$$\int d\boldsymbol{q}' \, G(\boldsymbol{q}, \boldsymbol{q}')[E_\alpha - H(\boldsymbol{q}')] f_\alpha(\boldsymbol{q}') = 0$$

where $G(\boldsymbol{q}, \boldsymbol{q}') = \langle \Psi[\boldsymbol{q}] | \Psi[\boldsymbol{q}']\rangle$ is the overlap (metric tensor). The solution yields a spectrum of eigenstates, each peaked at a different deformation.

### Triaxial Deformation Parameter

For a completely general ellipsoid with semi-axes $a \geq b \geq c$, the quadrupole deformation is defined by:

$$\beta_2 = \frac{\langle 2 z^2 - x^2 - y^2 \rangle}{\langle r^2 \rangle} = \sqrt{\frac{16\pi}{5}} \, \beta$$

and the triaxiality parameter $\gamma$ distinguishes prolate (axially symmetric, $\gamma = 0°$), triaxial, and oblate ($\gamma = 60°$) shapes:

$$\gamma = \arctan\left( \frac{\sqrt{3}(b^2 - a^2)}{2c^2 - a^2 - b^2} \right)$$

At $\gamma = 0°$, the nucleus is prolate (cigar-shaped). At $\gamma = 30°$, maximally triaxial. At $\gamma = 60°$, oblate (disk-shaped).

### Coulomb vs. Nuclear Competition

The critical question for superheavy nuclei is: does Coulomb repulsion overcome nuclear attraction to favor spherical shapes (minimizing surface area), or do shell effects dominate to favor deformed ground states?

For a given nucleus, compute the deformation energy:

$$\Delta E(\beta) = E(\beta) - E(0)$$

If $\Delta E(\beta) < 0$ for some $\beta > 0$, the nucleus spontaneously deforms. If $\Delta E(\beta) > 0$ everywhere, the nucleus is spherical. In superheavy nuclei, multiple minima often appear:

$$\Delta E(\beta) = E_1(\beta) - E(0)$$

where the $E_1$ minimum might be at $\beta_1 \approx 0.4--0.6$ (prolate), with secondary minima at $\beta_2 \approx 0.2$ (weakly prolate) or even negative $\beta$ (oblate), all within 0.5--2 MeV of the ground state.

---

## Key Results

1. **Abundant Shape Coexistence**: Superheavy nuclei exhibit coexisting configurations across the chart: spherical, prolate, oblate, and triaxial shapes all occur as low-lying states in nuclei like $^{288}$114 (E114), $^{292}$120 (E120), and beyond.

2. **Prolate Ground States Dominate**: Despite Coulomb repulsion, prolate deformations ($\beta_2 \sim 0.5--0.8$) are favored as ground states in most superheavy nuclei investigated, due to shell closures in deformed geometry.

3. **Relative Energies and Moments of Inertia**: Predicted excitation energies between competing configurations range from ~0.1 to 1 MeV. The moment of inertia of prolate ground states is $\mathcal{I} \sim 15--20 \hbar^2$ MeV$^{-1}$, while spherical or oblate states are much softer ($\mathcal{I} \sim 5$ $\hbar^2$ MeV$^{-1}$).

4. **Triaxiality Signatures**: Certain nuclei near Z = 114, N = 184 exhibit pronounced triaxial deformation ($\gamma \sim 20--30°$) as the lowest energy configuration, predicting distinctive E2 transition patterns.

5. **Magic Numbers Redefined**: The traditional closure at Z = 50 (tin) or Z = 82 (lead) gives way to deformed closures in superheavy nuclei. The Z = 114 (flerovium) shell closure competes with Z = 114 prolate deformation, creating the shape coexistence phenomenon.

6. **Lifetime Implications**: Different shapes have different decay properties. An isomeric state in an oblate configuration might decay via internal conversion or isomeric transitions, while the prolate ground state decays via alpha emission. This multipath decay enriches experimental signatures.

---

## Key Equations

| Quantity | Expression |
|:---------|:-----------|
| Potential energy surface | $E(\beta_2, \gamma) = E_{\text{HFB}} + E_{\text{rot}}(\beta_2, \gamma)$ |
| GCM overlap | $G(\beta, \beta') = \langle \Psi[\beta] \| \Psi[\beta'] \rangle$ |
| Quadrupole deformation | $\beta_2 = \frac{16\pi}{5} \langle \sum_i r_i^2 P_2(\cos\theta_i) \rangle / \langle r^2 \rangle$ |
| Triaxiality parameter | $\gamma = \arctan[\sqrt{3}(b^2 - a^2) / (2c^2 - a^2 - b^2)]$ |
| Coulomb energy (approx.) | $E_C \approx \frac{3}{5} \frac{e^2 Z^2}{R_0} [1 + 0.03\beta_2^2]$ |
| Excitation energy of isomer | $E^* = E(\text{isomeric config.}) - E(\text{g.s.})$ |

---

## Connection to Phonon-Exflation Framework

Shape coexistence in superheavy nuclei exemplifies a profound principle: when two or more competing orderings of nuclear matter exist at nearly equal energy, the system exhibits bistability or multistability. In the phonon-exflation framework, this phenomenon gains a geometric interpretation.

Key implications:

1. **Competing Phonon Condensates**: The coexisting shapes correspond to different coherent states of the phonon field on the internal SU(3) manifold. A prolate nucleus represents one coherent phonon amplitude, while an oblate configuration represents a different (orthogonal) phonon mode condensed into the ground state.

2. **Metric Landscape Modulation**: The potential energy surface $E(\beta_2, \gamma)$ reflects the landscape of collective excitations available on the internal manifold. The appearance of multiple minima signals that the phonon spectrum itself becomes multi-modal—several phonon frequencies achieve comparable importance.

3. **Coulomb-Driven Shape Transitions**: The competing role of Coulomb repulsion (favoring compact shapes) vs. shell structure (favoring deformation) mirrors a fundamental balance in the framework: the cost of deforming the internal geometry (geometric energy) vs. the gain from accessing new phonon modes (collective gain). The framework predicts that in regimes where Coulomb becomes dominant (Z > 100), the phonon spectrum of the internal manifold should undergo its own instability, driving shape transitions.

4. **Isomeric States as Phonon Metastability**: Isomeric states—long-lived excited states that decay slowly—correspond to trapping in a secondary minimum of the phonon potential energy landscape. Tunneling between competing shapes occurs through phonon-mediated processes, with decay rates determined by the phonon tunnel probability.

5. **Z = 114 as Critical Point**: The appearance of enhanced shape coexistence near Z = 114 might signal a critical phenomenon where the phonon spectrum of the internal geometry undergoes a transition (analogous to a phase transition), explaining why superheavy nuclei exhibit richer shape phenomena than lighter systems.

---

## References

- Sieja, K., Caurier, E., Nowacki, F., Nazarewicz, W. (2007). Configuration mixing in superheavy nuclei: Nuclear structure aspects. Phys. Rev. C 75, 051301(R).
- Bjørnholm, S., Lynn, J.E. (1980). The double-humped fission barrier. Rev. Mod. Phys. 52, 725-931.
- Cwiok, S., Heenen, P.-H., Nazarewicz, W. (1996). Shape isomerism in superheavy nuclei. Nature 433, 705-709.

