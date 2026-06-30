# Geometric orbital susceptibility: quantum metric without Berry curvature

**Author(s):** Frederic Piechon, Arnaud Raoux, Jean-Noel Fuchs, Gilles Montambaux
**Year:** 2016
**Journal:** Physical Review B (submitted; arXiv preprint)
**arXiv:** 1605.01258
**Relevance:** CRITICAL

---

## Abstract

The orbital magnetic susceptibility of an electron gas in a periodic potential depends not only on the zero field energy spectrum but also on the geometric structure of cell-periodic Bloch states which encodes interband effects. In addition to the Berry curvature, we explicitly relate the orbital susceptibility of two-band models to a quantum metric tensor defining a distance in Hilbert space. Within a simple tight-binding model allowing for a tunable Bloch geometry, we show that interband effects are essential even in the absence of Berry curvature. We also show that for a flat band model, the quantum metric gives rise to a very strong orbital paramagnetism.

---

## Key Arguments and Derivations

### Section II: Geometry -- Quantum Metric and Berry Curvature

The paper begins by recalling Berry's quantum geometric tensor (QGT) for cell-periodic Bloch states $|u_\alpha(\mathbf{k})\rangle$:

$$T_{\alpha ij}(\mathbf{k}) = \langle \partial_i u_\alpha | 1 - \mathscr{P}_\alpha | \partial_j u_\alpha \rangle$$

where $\mathscr{P}_\alpha = |u_\alpha\rangle\langle u_\alpha|$ is the band projector. The imaginary (antisymmetric) part is the Berry curvature $\Omega_{\alpha ij} = -2\,\mathrm{Im}\,T_{\alpha ij}$, and the real (symmetric) part is the quantum metric tensor $g_{\alpha ij} = \mathrm{Re}\,T_{\alpha ij}$, characterizing a distance in Hilbert space:

$$ds^2_\alpha = 1 - |\langle u_\alpha(\mathbf{k}) | u_\alpha(\mathbf{k}+d\mathbf{k})\rangle|^2 = g_{\alpha ij}\,dk^i\,dk^j$$

For two-band models $\hat{h}(\mathbf{k}) = \varepsilon_0(\mathbf{k})\mathbb{1} + \varepsilon(\mathbf{k})\,\mathbf{n}(\mathbf{k})\cdot\boldsymbol{\sigma}$, the Berry curvature and metric satisfy $\Omega_{\alpha ij} = \alpha\,\Omega_{ij}$ and $g_{\alpha ij} = g_{ij}$ with:

$$\Omega_{ij} = \tfrac{1}{2}(\partial_i \mathbf{n} \times \partial_j \mathbf{n})\cdot\mathbf{n}, \qquad g_{ij} = \tfrac{1}{4}\,\partial_i \mathbf{n}\cdot\partial_j \mathbf{n}$$

A key identity relates the two:

$$\Omega^2_{ij} = 4(g_{ii}g_{jj} - g^2_{ij})$$

This means the quantum metric determines the *magnitude* of the Berry curvature but not its k-dependent sign.

### Section III: Orbital Susceptibility for Two-Band Models

The orbital susceptibility decomposes as:

$$\chi_\mathrm{orb} = \chi_\mathrm{LP} + \chi_\mathrm{inter}$$

where the Landau-Peierls (LP) term depends only on the band spectrum, while the interband term encodes all wavefunction geometric effects. The interband contribution further decomposes into three parts:

$$\chi_\mathrm{inter} = \chi_\Omega + \chi_g + \tilde{\chi}_g$$

Each separately obeys the sum rule $\int d\mu\,\chi_\lambda(\mu) = 0$.

**$\chi_\Omega$** depends on Berry curvature through the orbital magnetic moment $\mathscr{M} = \varepsilon\Omega$. It contains a Pauli-like Fermi surface term and a diamagnetic Fermi sea term. It vanishes for centrosymmetric systems.

**$\chi_g$** depends on the quantum metric through $Z_g = \tfrac{1}{2}\partial_j(\varepsilon^2 \partial_i g^{ij})$, involving the contravariant metric tensor. This is a pure Fermi sea term. It is "more fundamental" since it never vanishes for coupled bands -- it persists even when $\Omega = 0$.

**$\tilde{\chi}_g$** depends on the metric tensor and only appears when particle-hole symmetry is broken. It involves $\tilde{Z}_g = g^{ij}\partial_i\varepsilon_0\partial_j\varepsilon_0 + \alpha\varepsilon\,\partial_i(g^{ij}\partial_j\varepsilon_0)$.

### Section IV: Examples

**Square-to-honeycomb lattice ($\lambda$ interpolation):** A tunable brickwall lattice with staggered potential $\Delta$ interpolates between a square lattice ($\lambda=1$, zero Berry curvature) and a distorted honeycomb lattice ($\lambda=0$, finite Berry curvature at Dirac points). For the square lattice, there is no Berry curvature ($\chi_\Omega = 0$), yet the quantum metric $g_{ij}$ and $Z_g$ are nonzero and produce a paramagnetic plateau in the gap. This is the paper's central demonstration: interband coupling is NOT only encoded in Berry curvature.

**Lattice vs. low-energy model:** For the linearized (Dirac) model, $3\mathscr{H} = \mathscr{M}^2 = Z_g$. The susceptibility $\chi_\mathrm{orb}$ is a diamagnetic plateau in the gap and zero outside (from fortuitous cancellation of $\chi_\mathrm{LP}$, $\chi_\Omega$, $\chi_g$). However, the lattice model shows $\chi_g$ requires the whole Brillouin zone, not just Dirac point vicinity.

**Mielke checkerboard lattice (flat band):** Inversion-symmetric ($\chi_\Omega = 0$) but extremely particle-hole asymmetric. The flat band touching the bottom of a dispersive band gives rise to a huge $\tilde{\chi}_g$ contribution -- a diverging paramagnetic peak at the flat band energy. Only metric-dependent terms ($\chi_g$ and $\tilde{\chi}_g$) explain the strong interband effects.

### Section V: Heuristic Derivation

The three interband contributions are interpreted through a field-dependent effective density of states valid to second order in B. The Berry connection acquires field-induced corrections $\mathbf{a}_g$ and $\tilde{\mathbf{a}}_g$ that define field-induced Berry curvature shifts:

- $\chi_\Omega$ measures k-space fluctuations of spontaneous orbital magnetization
- $\chi_g$ and $\tilde{\chi}_g$ are field-induced effects from positional shifts of Bloch wavepackets

### Section VI: Comparison with Other Works

The decomposition is compared to Blount's formula (1962) and Gao et al. (2015). The authors show their three-term decomposition has the advantage that each term (i) vanishes outside the band spectrum, and (ii) satisfies the sum rule -- properties not shared by alternative decompositions.

### Section VII: Conclusion

The quantum metric (real part of QGT) carries physical information independent of Berry curvature (imaginary part). Even when $\Omega = 0$, the metric produces observable susceptibility effects. For flat bands, it generates very strong orbital paramagnetism.

---

## Key Results

1. The orbital susceptibility of two-band models decomposes into four terms: $\chi_\mathrm{orb} = \chi_\mathrm{LP} + \chi_\Omega + \chi_g + \tilde{\chi}_g$, where the last two depend only on the quantum metric tensor.
2. Interband effects are essential even when Berry curvature vanishes ($\Omega = 0$); the quantum metric alone generates observable susceptibility.
3. For centrosymmetric systems, $\chi_\Omega = 0$ but $\chi_g$ provides the paramagnetic gap plateau.
4. For flat band models, the quantum metric gives rise to a diverging paramagnetic susceptibility -- a purely metric effect.
5. The identity $\Omega^2 = 4\det g$ shows the metric determines the curvature magnitude but not its sign.
6. Each of the three interband contributions independently satisfies the sum rule $\int d\mu\,\chi = 0$.
7. The gap susceptibility has an exact form: $\chi_\mathrm{gap} = \langle \frac{1}{\varepsilon}(-\varepsilon^2\Omega^2 + \frac{1}{2}\partial_i(\varepsilon^2\partial_j g^{ij}) + g^{ij}\partial_i\varepsilon_0\partial_j\varepsilon_0) \rangle_\mathrm{BZ}$.
8. For the linearized Dirac model, the three interband terms are equal: $3\mathscr{H} = \mathscr{M}^2 = Z_g$.
9. $\chi_g$ is the most fundamental interband contribution -- it survives when both inversion and particle-hole symmetries are present.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| QGT definition | $T_{\alpha ij}(\mathbf{k}) = \langle \partial_i u_\alpha \| 1 - \mathscr{P}_\alpha \| \partial_j u_\alpha \rangle$ | Eq. (4) |
| Hilbert distance | $ds^2_\alpha = 1 - \|\langle u_\alpha(\mathbf{k}) \| u_\alpha(\mathbf{k}+d\mathbf{k})\rangle\|^2 = g_{\alpha ij}\,dk^i dk^j$ | Eqs. (5)-(6) |
| Two-band curvature & metric | $\Omega_{ij} = \frac{1}{2}(\partial_i \mathbf{n} \times \partial_j \mathbf{n})\cdot\mathbf{n}$, $g_{ij} = \frac{1}{4}\partial_i\mathbf{n}\cdot\partial_j\mathbf{n}$ | Eq. (8) |
| Curvature-metric identity | $\Omega^2_{ij} = 4(g_{ii}g_{jj} - g^2_{ij})$ | Eq. (9) |
| Determinant form | $\Omega^2 = 4\det g = 4g_{ij}g^{ij}$ | Eq. (11) |
| Total susceptibility | $\chi_\mathrm{orb} = \chi_\mathrm{LP} + \chi_\Omega + \chi_g + \tilde{\chi}_g$ | Eq. (14), (17) |
| Landau-Peierls | $\chi_\mathrm{LP} = \langle \frac{n'_\alpha}{12}(\partial^2_x\varepsilon_\alpha\,\partial^2_y\varepsilon_\alpha - (\partial^2_{xy}\varepsilon_\alpha)^2) \rangle_\mathrm{BZ}$ | Eq. (15) |
| Berry curvature contribution | $\chi_\Omega = \langle (-n'_\alpha + \alpha\frac{n_\alpha}{\varepsilon})\mathscr{M}^2 \rangle_\mathrm{BZ}$, $\mathscr{M} = \varepsilon\Omega$ | Eq. (19) |
| Metric contribution | $\chi_g = \langle -\alpha\frac{n_\alpha}{\varepsilon} Z_g \rangle_\mathrm{BZ}$, $Z_g = \frac{1}{2}\partial_j(\varepsilon^2\partial_i g^{ij})$ | Eq. (20) |
| Asymmetric metric contribution | $\tilde{\chi}_g = \langle -\alpha\frac{n_\alpha}{\varepsilon}\tilde{Z}_g \rangle_\mathrm{BZ}$, $\tilde{Z}_g = g^{ij}\partial_i\varepsilon_0\partial_j\varepsilon_0 + \alpha\varepsilon\,\partial_i(g^{ij}\partial_j\varepsilon_0)$ | Eqs. (21)-(22) |
| Gap susceptibility | $\chi_\mathrm{gap} = \langle \frac{1}{\varepsilon}(-\varepsilon^2\Omega^2 + \frac{1}{2}\partial_i(\varepsilon^2\partial_j g^{ij}) + g^{ij}\partial_i\varepsilon_0\partial_j\varepsilon_0) \rangle_\mathrm{BZ}$ | Sec. VII |
| Sum rule | $\int d\mu\,\chi_\mathrm{LP} = \int d\mu\,\chi_\Omega = \int d\mu\,\chi_g = \int d\mu\,\tilde{\chi}_g = 0$ | Eq. (18) |
| Dirac model identity | $3\mathscr{H} = \mathscr{M}^2 = Z_g = \frac{\Delta^2 v_x^2 v_y^2}{4\varepsilon^4}$ | Eq. (23) |
| Field-induced curvature (metric) | $\Omega_g(\mathbf{k}) = [\nabla_\mathbf{k}\times\mathbf{a}_g]_z = -\frac{1}{2}\partial_i\partial_j g^{ij}$ | Eq. (31) |
| Field-induced curvature (asymmetric) | $\tilde{\Omega}_g(\mathbf{k}) = [\nabla_\mathbf{k}\times\tilde{\mathbf{a}}_g]_z = -\partial_i(\frac{g^{ij}\partial_j\varepsilon_0}{\varepsilon})$ | Eq. (32) |
| Langevin (tight-binding) | $\chi_\mathrm{Langevin} = \langle -n_\alpha[\frac{1}{4}g^{ij}\partial^2_{ij}\varepsilon_\alpha + \frac{1}{2}\alpha\varepsilon\Omega^2 + \frac{1}{2}\alpha\frac{\partial_i(\varepsilon^2\partial_j g^{ij})}{\varepsilon}] \rangle_\mathrm{BZ}$ | Eq. (42) |
| Decomposition equivalence | $\chi_\Omega + \chi_g = \chi_\mathrm{Pauli} + \chi_\mathrm{geom} + \chi_\mathrm{Langevin}$; $\tilde{\chi}_g = \chi_\mathrm{VV} + 2\chi_\mathrm{Polar}$ | Eq. (43) |

---

## Relevance to Phonon-Exflation

This paper is directly relevant to the phonon-exflation framework's ERRATUM result where the quantum geometric tensor was computed and found to have $\mathrm{Im}(T) = 0$ (Berry curvature vanishes) while $\mathrm{Re}(T) = g = 982.5$ (quantum metric is large). Piechon et al. prove that physical observables -- specifically orbital susceptibility -- depend on the quantum metric *even when Berry curvature is identically zero*. Their decomposition $\chi_\mathrm{inter} = \chi_\Omega + \chi_g + \tilde{\chi}_g$ shows that $\chi_g$ is the "most fundamental" interband contribution, surviving under both inversion and particle-hole symmetry. This explains the framework's "sensitivity without topological protection" regime: the large quantum metric $g = 982.5$ drives interband coupling and physical response through the metric channel, while the vanishing Berry curvature ($\Omega = 0$) means there is no topological protection (no quantized Hall-type invariant). The flat-band paramagnetism result is also relevant: the framework's BDI class with trivial winding (WIND-36=0) but large metric is analogous to the checkerboard model where $\chi_\Omega = 0$ but $\chi_g$ and $\tilde{\chi}_g$ produce strong observable effects.
