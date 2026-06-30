# Berry Phase Effects on Electronic Properties

**Author(s):** Di Xiao, Ming-Che Chang, Qian Niu
**Year:** 2010
**Journal:** Reviews of Modern Physics 82, 1959 (2010)
**arXiv:** 0907.2021
**Relevance:** CRITICAL

---

## Abstract

Ever since its discovery, the Berry phase has permeated through all branches of physics. Over the last three decades, it was gradually realized that the Berry phase of the electronic wave function can have a profound effect on material properties and is responsible for a spectrum of phenomena, such as ferroelectricity, orbital magnetism, various (quantum/anomalous/spin) Hall effects, and quantum charge pumping. This progress is summarized in a pedagogical manner in this review. We start with a brief summary of necessary background, followed by a detailed discussion of the Berry phase effect in a variety of solid state applications. A common thread of the review is the semiclassical formulation of electron dynamics, which is a versatile tool in the study of electron dynamics in the presence of electromagnetic fields and more general perturbations. Finally, we demonstrate a re-quantization method that converts a semiclassical theory to an effective quantum theory. It is clear that the Berry phase should be added as a basic ingredient to our understanding of basic material properties.

---

## Key Arguments and Derivations

### I.C: Basic Concepts of the Berry Phase

**Cyclic adiabatic evolution:** For a parameter-dependent Hamiltonian $H(\mathbf{R})$ with $\mathbf{R}(t)$ varying along a closed path $\mathcal{C}$, a system initially in eigenstate $|n(\mathbf{R}(0))\rangle$ acquires the Berry phase:

$$\gamma_n = \oint_{\mathcal{C}} d\mathbf{R} \cdot \mathcal{A}_n(\mathbf{R}), \quad \mathcal{A}_n(\mathbf{R}) = i\langle n(\mathbf{R})|\frac{\partial}{\partial\mathbf{R}}|n(\mathbf{R})\rangle$$

**Berry curvature:** The gauge-invariant field tensor $\Omega^n_{\mu\nu} = \partial\mathcal{A}^n_\nu/\partial R^\mu - \partial\mathcal{A}^n_\mu/\partial R^\nu$. The summation formula (crucial for computation):

$$\Omega^n_{\mu\nu}(\mathbf{R}) = i\sum_{n'\neq n}\frac{\langle n|\frac{\partial H}{\partial R^\mu}|n'\rangle\langle n'|\frac{\partial H}{\partial R^\nu}|n\rangle - (\nu\leftrightarrow\mu)}{(\varepsilon_n - \varepsilon_{n'})^2}$$

Key property: $\sum_n \Omega^n_{\mu\nu}(\mathbf{R}) = 0$ (local conservation law). Berry curvature becomes singular at degeneracy points (monopoles).

**Two-level system** $H = \mathbf{h}(\mathbf{R})\cdot\boldsymbol{\sigma}$: Berry curvature $\boldsymbol{\Omega} = \mathbf{h}/(2h^3)$ -- a monopole field. Berry phase over $S^2$ gives Chern number = 1.

### I.D: Berry Phase in Bloch Bands

The Brillouin zone is the parameter space. Berry curvature of bands: $\boldsymbol{\Omega}_n(\mathbf{q}) = \nabla_\mathbf{q} \times \langle u_n(\mathbf{q})|i\nabla_\mathbf{q}|u_n(\mathbf{q})\rangle$. Zak's phase $\gamma_n = \int_\mathrm{BZ} d\mathbf{q}\cdot\langle u_n|i\nabla_\mathbf{q}|u_n\rangle$ is quantized to 0 or $\pi$ with inversion symmetry.

### II: Adiabatic Transport and Electric Polarization

**Anomalous velocity from Berry curvature:** $v_n(\mathbf{q}) = \partial\varepsilon_n/(\hbar\partial q) - \Omega^n_{qt}$. Adiabatic current $j = -\sum_n\int_\mathrm{BZ} (dq/2\pi)\,\Omega^n_{qt}$. Quantized particle transport (Chern number) over one cycle: $c_n = -(1/2\pi)\int_0^T dt\int_\mathrm{BZ} dq\,\Omega^n_{qt}$.

**Electric polarization** as Berry phase: modern theory links bulk polarization to Zak's phase via $P = \frac{e}{2\pi}\sum_n\int_\mathrm{BZ} dq\,\mathcal{A}_n(q)$.

### III: Anomalous Velocity and Hall Effects

The anomalous velocity $\dot{\mathbf{r}} = \partial\varepsilon_n/(\hbar\partial\mathbf{k}) - (e/\hbar)\mathbf{E}\times\boldsymbol{\Omega}_n(\mathbf{k})$ gives rise to:
- **Quantum Hall effect:** Hall conductance $\sigma_{xy} = (e^2/h)\sum_n c_n$ (TKNN formula, Chern numbers)
- **Anomalous Hall effect:** intrinsic contribution from Berry curvature of occupied bands
- **Valley Hall effect:** opposite Berry curvature in different valleys

### IV-V: Wave Packet Dynamics

Electron wave packet carries orbital magnetic moment $\mathbf{m}_n(\mathbf{k}) = -(e/2\hbar)\mathrm{Im}\langle\nabla_\mathbf{k} u_n|\times(H-\varepsilon_n)|\nabla_\mathbf{k} u_n\rangle$. Berry curvature modifies the density of states: $D(\mathbf{r},\mathbf{k}) = (1/(2\pi)^d)(1 + (e/\hbar)\mathbf{B}\cdot\boldsymbol{\Omega})$.

### VII-IX: Quantization, Magnetic Bands, Non-Abelian

Bohr-Sommerfeld quantization with Berry phase correction to Landau levels and Wannier-Stark ladders. Magnetic Bloch bands and Hofstadter spectrum. Non-Abelian Berry curvature for degenerate bands (spin Hall effect, Dirac electrons).

---

## Key Results

1. Berry curvature is a local, gauge-invariant quantity that acts as "magnetic field in parameter space."
2. The anomalous velocity $\dot{\mathbf{r}} = \partial\varepsilon/(\hbar\partial\mathbf{k}) + (1/\hbar)\dot{\mathbf{k}}\times\boldsymbol{\Omega}(\mathbf{k})$ is intrinsic to band structure.
3. Quantized Hall conductance = Chern number $\times e^2/h$ (TKNN invariant).
4. Electric polarization is a Berry phase across the Brillouin zone.
5. Orbital magnetization has a Berry curvature contribution of topological origin.
6. Berry curvature modifies the semiclassical density of states: $D \propto (1 + (e/\hbar)\mathbf{B}\cdot\boldsymbol{\Omega})$.
7. Quantized adiabatic particle transport = first Chern number (integer, topologically robust).
8. Total Berry curvature summed over all bands vanishes: $\sum_n\Omega^n_{\mu\nu} = 0$.
9. Degeneracy points are monopoles (sources/drains) of Berry curvature.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Berry phase | $\gamma_n = \oint_\mathcal{C} d\mathbf{R}\cdot\mathcal{A}_n(\mathbf{R})$ | Eq. (1.10) |
| Berry connection | $\mathcal{A}_n(\mathbf{R}) = i\langle n(\mathbf{R})\|\partial/\partial\mathbf{R}\|n(\mathbf{R})\rangle$ | Eq. (1.6) |
| Berry curvature (differential) | $\Omega^n_{\mu\nu} = \partial\mathcal{A}^n_\nu/\partial R^\mu - \partial\mathcal{A}^n_\mu/\partial R^\nu$ | Eq. (1.11) |
| Berry curvature (summation) | $\Omega^n_{\mu\nu} = i\sum_{n'\neq n}\frac{\langle n\|\partial_\mu H\|n'\rangle\langle n'\|\partial_\nu H\|n\rangle - (\nu\leftrightarrow\mu)}{(\varepsilon_n-\varepsilon_{n'})^2}$ | Eq. (1.13) |
| Conservation law | $\sum_n \Omega^n_{\mu\nu}(\mathbf{R}) = 0$ | Eq. (1.14) |
| Two-level monopole | $\boldsymbol{\Omega} = \mathbf{h}/(2h^3)$ | Eq. (1.20) |
| Bloch band Berry curvature | $\boldsymbol{\Omega}_n(\mathbf{q}) = \nabla_\mathbf{q}\times\langle u_n\|i\nabla_\mathbf{q}\|u_n\rangle$ | Eq. (1.27) |
| Anomalous velocity | $v_n = \partial\varepsilon_n/(\hbar\partial q) - \Omega^n_{qt}$ | Eq. (2.5) |
| Adiabatic current | $j = -\sum_n\int_\mathrm{BZ}(dq/2\pi)\Omega^n_{qt}$ | Eq. (2.6) |
| Quantized transport (Chern) | $c_n = -(1/2\pi)\int_0^T dt\int_\mathrm{BZ}dq\,\Omega^n_{qt}$ | Eq. (2.7) |
| Many-body adiabatic current | $j(\kappa) = \partial\varepsilon/(\hbar\partial\kappa) - \tilde{\Omega}_{\kappa t}$ | Eq. (2.19) |
| Zak's phase | $\gamma_n = \int_\mathrm{BZ} d\mathbf{q}\cdot\langle u_n\|i\nabla_\mathbf{q}\|u_n\rangle$ | Eq. (1.29) |
| Semiclassical EOM | $\dot{\mathbf{r}} = \partial\varepsilon_n/(\hbar\partial\mathbf{k}) + (1/\hbar)\dot{\mathbf{k}}\times\boldsymbol{\Omega}_n$; $\hbar\dot{\mathbf{k}} = -e\mathbf{E} - e\dot{\mathbf{r}}\times\mathbf{B}$ | Sec. V.A |
| Modified DOS | $D(\mathbf{r},\mathbf{k}) = (1/(2\pi)^d)(1+(e/\hbar)\mathbf{B}\cdot\boldsymbol{\Omega})$ | Sec. V.B |
| TKNN Hall conductance | $\sigma_{xy} = (e^2/h)\sum_n c_n$ (Chern numbers) | Sec. III.C |
| Orbital moment | $\mathbf{m}_n = -(e/2\hbar)\mathrm{Im}\langle\nabla_\mathbf{k}u_n\|\times(H-\varepsilon_n)\|\nabla_\mathbf{k}u_n\rangle$ | Sec. IV.A |

---

## Relevance to Phonon-Exflation

This review is the canonical reference for Berry phase effects in condensed matter, directly relevant to the phonon-exflation framework in multiple ways. The anomalous velocity formula shows how Berry curvature generates transverse transport -- the mechanism underlying the framework's Hall-type response predictions. The TKNN formula connecting quantized Hall conductance to Chern numbers provides the mathematical framework for understanding why the framework's BDI class with trivial winding (WIND-36=0) has zero quantized Hall response. The Berry curvature conservation law $\sum_n\Omega^n = 0$ explains why a vanishing Berry curvature in one band does not mean the curvature is absent from the full system -- it has been "projected out" to other bands, consistent with the ERRATUM finding of $\mathrm{Im}(T)=0$ for the ground state while the quantum metric $\mathrm{Re}(T) = 982.5$ remains large. The modified density of states $D \propto (1+(e/\hbar)\mathbf{B}\cdot\boldsymbol{\Omega})$ provides the mechanism by which an external magnetic field can probe the Berry curvature structure of the framework's fiber bundle. The electric polarization as Berry phase connects directly to measurable consequences even when curvature is small (Paper 21's topic).
