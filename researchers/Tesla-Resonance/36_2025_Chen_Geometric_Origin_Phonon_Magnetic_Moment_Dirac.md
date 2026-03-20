# Geometric Origin of Phonon Magnetic Moment in Dirac Materials

**Authors:** Wenqin Chen, Xiao-Wei Zhang, Ting Cao, Shi-Zeng Lin, Di Xiao

**Year:** 2025

**Journal/Source:** arXiv:2505.09732

---

## Abstract

This paper develops a comprehensive theoretical framework treating phonons as emergent gauge and gravitational fields interacting with Dirac fermions embedded in curved spacetime. The authors classify electron-phonon couplings by angular momentum channels and identify two fundamental mechanisms generating phonon magnetism: one proportional to the electronic Hall conductivity through gauge field coupling, and another to the Hall viscosity through frame field coupling. First-principles calculations on Cd₃As₂ validate theoretical predictions with quantitative agreement to experimental observations.

---

## Historical Context

The interplay between lattice vibrations and electronic properties in Dirac materials has traditionally been treated through perturbative phonon-electron scattering corrections to band structure. This work elevates the conceptual framework by recognizing that phonons themselves, when propagating through a curved electronic background (shaped by Dirac topology), acquire effective gauge and gravitational properties analogous to those of fundamental particles in general relativity.

The recognition that phonons carry magnetic moments is particularly significant for experimental probes of topological materials. While Berry phase contributions to charge transport have been extensively studied (via anomalous Hall and orbital magnetization effects in Weyl semimetals), the phononic contribution to magnetic response has received limited attention. This gap is especially relevant to materials like Cd₃As₂ where Dirac fermions dominate transport and mechanical properties couple intimately to the electronic structure.

The geometric interpretation—that lattice deformations generate effective gravitational fields in the electronic subsystem—provides a bridge between condensed-matter physics and gravitational theory, enabling novel experimental signatures through inelastic light scattering and phonon spectroscopy.

---

## Key Arguments and Derivations

### Phonons as Emergent Fields

The central insight is that lattice vibrations, when expressed in the language of differential geometry, act as fluctuations in the metric (gravitational field) and the spin connection (gauge field) experienced by Dirac fermions.

For a Dirac material with Hamiltonian:

$$H = \mathbf{v_F} \cdot \boldsymbol{\sigma} \cdot (\mathbf{p} - \mathbf{A})$$

where $\mathbf{v_F}$ is the Fermi velocity, $\boldsymbol{\sigma}$ are Pauli matrices, and $\mathbf{A}$ is the gauge field, lattice distortions modify both the Fermi velocity and the effective Brillouin zone metric.

The electron-phonon Hamiltonian coupling can be decomposed:

$$H_{e-ph} = \int d^3r \, \Psi^\dagger (\mathbf{r}) \left[ V_{scalar}(u) + V_{vector}^a(u) \sigma^a + V_{tensor}^{ab}(u) \sigma^a \sigma^b \right] \Psi(\mathbf{r})$$

where $u$ represents the lattice displacement field $\mathbf{u}(\mathbf{r}, t)$. The scalar, vector, and tensor components couple to different angular momentum channels in the phonon spectrum.

### Gauge Field Coupling and Hall Conductivity

The authors show that the vector (pseudovector) component of electron-phonon coupling generates an effective gauge field:

$$\mathbf{A}_{eff}(u) = \sum_a \alpha_a \partial_a u_a$$

where $\alpha_a$ are material-dependent coupling constants. This effective gauge field gives rise to a Berry phase correction to the electronic wavefunction as it scatters off phonons, producing an anomalous contribution to the phonon velocity proportional to the electronic Hall conductivity $\sigma_{xy}$.

The magnetic moment acquired by a phonon mode $\lambda$ is then:

$$\mathbf{m}_{\lambda}^{(gauge)} = \frac{e \hbar}{2 m_e c} \sigma_{xy} \cdot f_\lambda(\mathbf{q})$$

where $f_\lambda(\mathbf{q})$ is a form factor depending on the phonon wavevector and polarization.

### Frame Field Coupling and Hall Viscosity

The symmetric tensor components generate an effective gravitational field (frame field or tetrad deformation):

$$e^\mu_a = \delta^\mu_a + \epsilon \partial^\mu u_a$$

where $\epsilon$ characterizes the strength of this coupling. In a curved background, the energy-momentum tensor acquires off-diagonal components related to the "Hall viscosity"—an anomalous viscosity tensor that appears in systems with broken time-reversal symmetry.

The corresponding magnetic moment is:

$$\mathbf{m}_{\lambda}^{(gravity)} \propto \eta_{Hall} \cdot g_\lambda(\mathbf{q})$$

where $\eta_{Hall}$ is the intrinsic Hall viscosity of the Dirac material and $g_\lambda(\mathbf{q})$ is a mode-dependent coupling function.

### Phonon Magnetic Moment Decomposition

The total phonon magnetic moment factorizes into two independent contributions:

$$\mathbf{m}_{\lambda}^{total} = \mathbf{m}_{\lambda}^{(gauge)} + \mathbf{m}_{\lambda}^{(gravity)}$$

This decomposition is non-trivial: the gauge contribution scales with the charge Hall conductivity (electronic origin), while the gravitational contribution arises from the viscosity tensor (structural origin). In magnetically ordered Dirac materials, both can align or oppose depending on the sign and magnitude of the gaps.

---

## Key Results

1. **Phonon Magnetic Moment Arises from Dual Sources:** Gauge field coupling (proportional to Hall conductivity) and gravitational frame field coupling (proportional to Hall viscosity) produce independent magnetic responses that can be experimentally distinguished.

2. **Cd₃As₂ Quantitative Agreement:** First-principles calculations reproducing experimental magnetic response of acoustic and optical phonon branches to 2-3% accuracy, validating the theoretical framework for a canonical Dirac semimetal.

3. **Angular Momentum Classification:** Phonon-electron coupling classified systematically into $\ell = 0$ (scalar), $\ell = 1$ (vector), and $\ell = 2$ (tensor) channels. Higher channels decouple for long-wavelength phonons, explaining the dominance of gauge and gravitational effects.

4. **Experimental Signature:** Phonon magnetic moment produces circular dichroism in Raman scattering and chiral phonon effects (momentum-locked circular polarization) measurable via inelastic light scattering above the Néel temperature.

5. **Universal Scaling:** The phonon magnetic moment scales universally with the ratio of Hall conductivity to phonon energy, suggesting applicability to other topological materials (Weyl semimetals, topological insulators, nodal-line semimetals).

---

## Impact and Legacy

This work opens a new window onto the electromagnetic and gravitational properties of quasiparticles in topological materials. By showing that lattice vibrations acquire magnetic moments through fundamental symmetry and topology principles, it enables:

- **Non-contact Probes of Dirac Gap:** Phonon magnetic response directly probes electronic Berry phases without direct charge excitation.
- **Chiral Phonon Engineering:** Design of materials with enhanced phononic magnetism for phononic circulator and isolator applications.
- **Quantum Metrology:** Phonon magnetic effects as sensitive probes of band-touching points and electron-phonon coupling strengths.

The framework also suggests that gravitational effects (curvature-induced modifications to phonon energies) can be experimentally addressed in condensed matter, providing a materials platform for studying gravity-matter couplings in a laboratory setting.

---

## Connection to Phonon-Exflation Framework

**HIGHLY RELEVANT.** The framework treats phonons as emergent excitations coupling to both gauge (internal U(1) charge, SU(3) color) and gravitational (spacetime metric) fields—precisely the duality identified in phonon-exflation. In the framework, phonons are collective modes of the M₄ × SU(3) substrate; this paper establishes that such phonons acquire topological properties (magnetic moments) purely from the geometry they inhabit.

The angular momentum decomposition ($\ell = 0, 1, 2$) echoes the classification of operators in the spectral triple: scalar (Higgs), vector (gauge boson), tensor (graviton) in a condensed-matter realization. The correspondence between Hall viscosity (geometric origin) and Hall conductivity (gauge origin) is a direct analog of the framework's identification of geometry and internal symmetry as two facets of the same spectral structure.

The paper's experimental pathways (inelastic light scattering, phonon spectroscopy) provide testable signatures for the phononic nature of particles once the framework is connected to observable matter.

