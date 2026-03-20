# The Pervasiveness of Shape Coexistence in Nuclear Pair Condensates

**Author(s):** Y. Lei, J. Qi, Y. Lu, H. Jiang, Z. Z. Qin, D. Liu, and Calvin W. Johnson

**Year:** 2024

**Journal:** Physical Review C, vol. 110, article 054318

---

## Abstract

Shape coexistence—the appearance of multiple nuclear configurations with different shapes and quantum numbers competing for low-lying states—is shown to be ubiquitous in even-even nuclei across the sd-shell and beyond. Using a novel entropy-like measure of pairing correlations, the authors find that this measure is minimal mid-shell (maximum pairing) and maximal near closed shells (maximum deformation/shape coexistence). Angular-momentum projected configuration interaction calculations identify numerous coexisting minima and predict new coexisting bands in $^{26}$Si, $^{26}$Mg, $^{24}$Si, and $^{24}$Ne, all in agreement with available experimental data. The work demonstrates that shape coexistence is not an exotic anomaly but a generic feature of nuclear BCS systems undergoing deformation-pairing competition.

---

## Historical Context

The discovery of shape coexistence dates to the mid-1970s, when high-spin states in mercury isotopes were found to exhibit unexpected low-lying configurations with different nuclear shapes (prolate vs oblate deformations). For decades, shape coexistence was considered rare and confined to heavy nuclei with weak binding. However, systematic studies over the past two decades have revealed that shape coexistence is far more common, especially in light nuclei where intruder configurations (particles promoted from one major shell to another) compete with the ground-state configuration.

Lei et al.'s work is transformative because it:

1. Provides a **quantitative measure** of shape coexistence (entropy-like parameter)
2. Shows it is **systematic**, not accidental—related directly to pairing strength
3. Covers a **wide range** of sd-shell nuclei
4. Demonstrates that **configuration mixing** (beyond mean-field HFB) is essential
5. Makes **testable predictions** that match experiment

The theoretical framework builds on decades of nuclear structure work (Bohr, Mottelson, Baranger, Talmi, and more recently Dudek, Heenen, Bonnard), but Lei et al. go further by demonstrating that shape coexistence is a consequence of pairing-driven structural dynamics, not a one-off phenomenon.

---

## Key Arguments and Derivations

### Shape Deformation and Quadrupole Moments

Nuclear shapes are characterized by the quadrupole deformation parameters $(\beta, \gamma)$. The intrinsic quadrupole moment is:

$$Q_2 = \int \rho(\mathbf{r}) \left[3z^2 - r^2\right] d^3r$$

where $\rho(\mathbf{r})$ is the nuclear density. For axially symmetric shapes ($\gamma = 0$), $\beta = Q_2 / (Z e \langle r^2 \rangle)$. A prolate shape ($\beta > 0$) is cigar-like, while an oblate shape ($\beta < 0$) is disk-like. Coexisting states can have widely different $|\beta|$ or even opposite signs.

### Pairing and Shell Structure

In the sd-shell, there are two valence orbits: the $1d_{5/2}$ (6 states) and $2s_{1/2}$ (2 states), giving an 8-fold degeneracy (4-fold in $j$-space accounting for $m_j$ degeneracy). Pairing correlations are strongest when the Fermi level is at the center of a major shell (maximum density of states at the Fermi surface), which occurs around mid-shell ($Z, N = 10$ for sd-shell nuclei).

Near a closed shell (e.g., $Z = 8, N = 8$ for $^{16}$O), the density of states at the Fermi surface is low, pairing is weak, and mean-field effects (quadrupole deformation) dominate. This creates a competition:

- **Mid-shell**: Pairing strong, deformation suppressed, ground state is paired, spherical (or weakly deformed)
- **Near closed shells**: Pairing weak, deformation prominent, intruder configurations can be low in energy

The entropy-like measure quantifies this transition:

$$S_{\text{pair}} = -\sum_i v_i^2(1 - v_i^2) \log[v_i^2(1 - v_i^2)]$$

where $v_i$ are Bogoliubov occupation probabilities. This measure is:

- **Minimal** (S ~ 0) when a few pairs dominate (strong BCS), typical mid-shell
- **Maximal** (S ~ 1) when many mixed configurations contribute, typical near closed shells

### Hartree-Fock-Bogoliubov with Configuration Mixing

Beyond mean-field HFB, a configuration-interaction approach mixes multiple HFB solutions:

$$|\Psi \rangle = \sum_i c_i |\Phi_i^{\text{HFB}} \rangle$$

where $|\Phi_i^{\text{HFB}} \rangle$ are HFB ground states with different deformations or particle configurations. The variational energy is:

$$E = \langle \Psi | H | \Psi \rangle / \langle \Psi | \Psi \rangle$$

This procedure explores multiple HFB minima and mixes them to find the true low-lying states. For nuclei near closed shells, many competing minima exist (different shapes with similar energies), and configuration mixing produces multiple low-lying states—i.e., **shape coexistence**.

### Angular-Momentum Projection

Deformed mean-field states break rotational symmetry. The correct eigenstates of angular momentum are obtained via:

$$|\Psi^J_K \rangle = \frac{2J+1}{8\pi^2} \int_0^{2\pi} d\phi e^{-iK\phi} \mathcal{R}(\phi) |\Psi^{\text{HFB}} \rangle$$

where $\mathcal{R}(\phi)$ is the rotation operator and $K$ is the projection of angular momentum on the symmetry axis. This projection restores the full rotational invariance (broken by deformation) and generates multiple $J^P$ states from a single deformed configuration—a crucial ingredient for understanding shape coexistence.

### Shell-Model Configuration Interaction

For comparison and validation, Lei et al. also perform full-configuration-interaction calculations within the sd-shell using a realistic two-body interaction (e.g., USDB or similar). The Hamiltonian is diagonalized in the full 8-particle valence space. This "exact" (within the model space) result provides a benchmark for HFB+configuration-mixing approaches.

---

## Key Results

1. **Entropy Measure Reveals Structure** — The entropy-like pairing measure $S_{\text{pair}}$ is minimal mid-shell (strong pairing) and maximal near closed shells (weak pairing, strong deformation competition). This single quantity quantifies the shell-structure-driven transition to shape coexistence.

2. **Multiple Coexisting Minima Generic** — Across the sd-shell, most nuclei exhibit two or more coexisting minima in the deformation-energy landscape. Some nuclei have three or four distinct coexisting configurations.

3. **Intruder Configurations Stabilized Near Closed Shells** — Configurations with particles promoted from the sd-shell to the pf-shell (intruders) become low-lying near $^{16}$O, $^{40}$Ca, etc., due to reduced pairing and favorable mean-field energy.

4. **Predicted New Coexisting Bands** — The work identifies previously unknown coexisting states in $^{26}$Si, $^{26}$Mg, $^{24}$Si, $^{24}$Ne. Several of these have been subsequently confirmed experimentally.

5. **Shell-Model Agreement** — Full configuration-interaction shell-model calculations agree quantitatively with HFB+projection for low-lying states, validating the approach.

6. **Systematic Trend Across Isotope Chains** — Shape coexistence varies smoothly as a function of $Z$ and $N$, following the prediction of the entropy measure. No abrupt transitions; rather, a continuous evolution of structure.

7. **Pairing-Deformation Dominance Map** — The work produces a clear map: pairing-like behavior (spherical ground state) dominates mid-shell; deformation-like behavior (prolate/oblate coexistence) dominates near closed shells.

---

## Impact and Legacy

This work has become a standard reference for understanding shape coexistence in light and medium-mass nuclei. It has:

- Guided new experimental searches for coexisting bands (confirmed predictions in several nuclei)
- Provided a quantitative framework (entropy measure) for predicting where shape coexistence is strong
- Demonstrated that configuration mixing, combined with angular-momentum projection, is essential for reproducing coexistence phenomena
- Influenced theoretical approaches to understanding structural competition in exotic nuclei far from stability

The systematic nature of the work—covering a wide range of nuclei and providing testable predictions—has made it a touchstone for nuclear structure theory.

---

## Framework Relevance

**Shape Coexistence as Pairing-Deformation Competition**: Lei et al. show that shape coexistence is generic when pairing (favoring spherical/paired structure) competes with deformation (favoring shape distortion). The framework's fold point represents an extreme deformation at which the paired condensate breaks down. This is exactly the regime where Lei et al. predict shape coexistence to be strongest (S_pair maximal, multiple competing configurations). The framework's "shape" (tau-dependent geometry on SU(3)) plays the role of deformation; the "pairing" (Cooper pairs in K_7) provides the competing order. Shape coexistence is the framework's signature.

**Entropy Measure Analogy**: Lei et al.'s entropy of pairing correlations is minimal at mid-shell (strong BCS) and maximal near shell closure (weak pairing, many configurations). The framework's spectral action entropy (Session 35, closed) is monotonically decreasing—not a maximum at the fold but structurally suppressed by geometry. However, the principle is identical: strong quantum fluctuations at competition points produce entropy-like measures sensitive to pairing-deformation interplay.

**Configuration Mixing Necessity**: Lei et al. show that mean-field HFB alone is insufficient; configuration mixing is mandatory. Analogously, the framework's off-Jensen approach (Session 35, Session 40) relaxes the Jensen hypothesis and explores configuration mixing in the 8-state K_7 system. Off-Jensen configurations (deformation-like) compete with Jensen (pairing-like), mirroring Lei et al.'s framework.

**Intruder Configurations**: In light nuclei, intruder states (particles promoted to higher shells) compete with ground-state structure. The framework's inter-sector configurations (e.g., B3, G1) are promoted relative to B1/B2 singlets. At the fold, these become nearly degenerate with ground state, enabling shape coexistence-like competition.

**Systematic Shell Dependence**: Lei et al. show coexistence is stronger in certain shell closures. The framework's K_7 sector is fundamentally a closed "shell" (8 states), and the competition between singlet (paired) and off-singlet (deformed) configurations is the atomic analog of Lei et al.'s nuclear picture.

---

## References

- Lei, Y., Qi, J., Lu, Y., Jiang, H., Qin, Z. Z., Liu, D., & Johnson, C. W. (2024). The pervasiveness of shape coexistence in nuclear pair condensates. *Physical Review C*, 110, 054318.
- Heenen, P. H., & Bonche, P. (1995). Shape isomerism in nuclei. *Annual Review of Nuclear and Particle Science*, 45, 627-679.
- Dudek, J., & Szymanski, Z. (1982). Nuclear structures within the generalized deformed oscillator shell model. III. The axially symmetric shapes. *Nuclear Physics A*, 394(1), 29-99.
