# Topological superconductors: a review

**Author(s):** Masatoshi Sato, Yoichi Ando
**Year:** 2017
**Journal:** Reports on Progress in Physics 80, 076501 (2017)
**arXiv:** 1608.03395
**Relevance:** HIGH

---

## Abstract

This review elaborates pedagogically on the fundamental concept, basic theory, expected properties, and materials realizations of topological superconductors. The relation between topological superconductivity and Majorana fermions are explained, and the difference between dispersive Majorana fermions and a localized Majorana zero mode is emphasized. A variety of routes to topological superconductivity are explained with an emphasis on the roles of spin-orbit coupling. Present experimental situations and possible signatures of topological superconductivity are summarized with an emphasis on intrinsic topological superconductors.

---

## Key Arguments and Derivations

### Topology in Quantum Mechanics (Sec. II)

Berry connection $\mathcal{A}^{(n)}(\mathbf{k}) = i\langle u_n(\mathbf{k})|\partial_\mathbf{k} u_n(\mathbf{k})\rangle$ and Berry curvature $\mathcal{F}^{(n)}_{ij}(\mathbf{k}) = \partial_{k_i}\mathcal{A}^{(n)}_{k_j} - \partial_{k_j}\mathcal{A}^{(n)}_{k_i}$. Chern number: $\mathrm{Ch}^{(n)}_1 = (1/2\pi)\int_\mathrm{BZ} dk_x dk_y\,\mathcal{F}^{(n)}_{xy}(\mathbf{k})$ -- integer topological invariant.

**Role of symmetry:** Without symmetry, only quantum Hall states (nonzero Chern number in 2D) are topological for $d \leq 3$. Time-reversal symmetry enables $\mathbb{Z}_2$ topological insulators. Homotopy group: $\pi_d(\mathcal{M}) = \{0, d=1,3; \mathbb{Z}, d=2\}$ for coset space $\mathcal{M} = U(n)/(U(m)\times U(n-m))$.

### Bogoliubov-de Gennes (BdG) Framework (Sec. III)

Particle-hole symmetry $\mathcal{C}\mathcal{H}(\mathbf{k})\mathcal{C}^{-1} = -\mathcal{H}(-\mathbf{k})$ is fundamental to superconductor topology. BdG Hamiltonian: $\mathcal{H}(\mathbf{k}) = \begin{pmatrix}\mathcal{E}(\mathbf{k}) & \Delta(\mathbf{k}) \\ \Delta^\dagger(\mathbf{k}) & -\mathcal{E}^t(-\mathbf{k})\end{pmatrix}$. Pairing symmetry: spin-singlet $\Delta = i\psi(\mathbf{k})s_y$ (even parity) vs spin-triplet $\Delta = i\mathbf{d}(\mathbf{k})\cdot\mathbf{s}\,s_y$ (odd parity).

### Topological Superconductor Theory (Sec. IV)

Altland-Zirnbauer (AZ) classification: 10-fold way. BDI class: time-reversal $\mathcal{T}^2 = +1$, particle-hole $\mathcal{C}^2 = +1$, chiral symmetry present. Topological invariant: $\mathbb{Z}$ winding number in 1D. Topological boundary states (Majorana fermions) protected by bulk gap.

### Majorana Fermions (Sec. V)

Majorana condition: $\gamma^\dagger = \gamma$ (particle is its own antiparticle). In BdG framework: Bogoliubov quasiparticles at $E = 0$ are Majorana fermions. Majorana zero modes at vortex cores/edges obey non-Abelian statistics.

### Routes to Topological SC (Sec. VI)

Odd-parity superconductors (e.g., Cu$_x$Bi$_2$Se$_3$), superconducting topological insulators, spin-singlet pairing with spin-orbit coupling. He-3 B-phase as prototype.

---

## Key Results

1. The AZ classification provides the 10-fold way for topological phases: symmetry class determines available topological invariants.
2. BDI class (our framework's class): $\mathcal{T}^2=+1$, $\mathcal{C}^2=+1$, chiral symmetry, $\mathbb{Z}$ winding number in 1D.
3. Particle-hole symmetry $\mathcal{C}\mathcal{H}(\mathbf{k})\mathcal{C}^{-1} = -\mathcal{H}(-\mathbf{k})$ is intrinsic to the BdG framework.
4. Topological superconductors host Majorana boundary/defect states protected by bulk topology.
5. Spin-orbit coupling provides key routes to topological superconductivity even with s-wave pairing.
6. Time-reversal-breaking is needed for nonzero Chern number; $\mathbb{Z}_2$ indices require TRS.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Berry connection | $\mathcal{A}^{(n)}(\mathbf{k}) = i\langle u_n(\mathbf{k})\|\partial_\mathbf{k} u_n(\mathbf{k})\rangle$ | Eq. (2) |
| Berry curvature | $\mathcal{F}^{(n)}_{ij}(\mathbf{k}) = \partial_{k_i}\mathcal{A}^{(n)}_{k_j} - \partial_{k_j}\mathcal{A}^{(n)}_{k_i}$ | Eq. (5) |
| Chern number | $\mathrm{Ch}^{(n)}_1 = \frac{1}{2\pi}\int_\mathrm{BZ} dk_x dk_y\,\mathcal{F}^{(n)}_{xy}$ | Eq. (9) |
| Hall conductance | $\sigma_{xy} = -(e^2/h)\mathrm{Ch}$ | Eq. (13) |
| Particle-hole symmetry | $\mathcal{C}\mathcal{H}(\mathbf{k})\mathcal{C}^{-1} = -\mathcal{H}(-\mathbf{k})$ | Eq. (61)/(74) |
| BdG Hamiltonian | $\mathcal{H}(\mathbf{k}) = \begin{pmatrix}\mathcal{E}(\mathbf{k}) & \Delta(\mathbf{k}) \\ \Delta^\dagger(\mathbf{k}) & -\mathcal{E}^t(-\mathbf{k})\end{pmatrix}$ | Eq. (72) |
| Spin-singlet pairing | $\Delta_{ss'}(\mathbf{k}) = i\psi(\mathbf{k})[s_y]_{ss'}$ | Eq. (77) |
| Spin-triplet pairing | $\Delta_{ss'}(\mathbf{k}) = i\mathbf{d}(\mathbf{k})\cdot[\mathbf{s}\,s_y]_{ss'}$ | Eq. (78) |
| $\mathbb{Z}_2$ index (2D) | $(-1)^{\nu_{2d}} = \prod_i \xi_i$ (parity eigenvalues at TRIM) | Eq. (34) |
| Topological insulator | $H_\mathrm{TI}(\mathbf{k}) = (m_0 - m_1 k^2)\sigma_x + v_z k_z\sigma_y + v\sigma_z(k_x s_y - k_y s_x)$ | Eq. (37) |

---

## Relevance to Phonon-Exflation

This paper provides the classification framework for the phonon-exflation system's BDI symmetry class with trivial winding number (WIND-36 = 0). The AZ 10-fold way classification confirms that BDI class in 1D supports a $\mathbb{Z}$ winding number invariant, and the framework's computed value of zero means no topological protection of boundary modes -- consistent with the "sensitivity without protection" regime where large quantum metric coexists with trivial topology. The BdG formalism reviewed here is the mathematical scaffolding for the framework's BCS mechanism chain, and the particle-hole symmetry constraint $\mathcal{C}\mathcal{H}\mathcal{C}^{-1} = -\mathcal{H}(-\mathbf{k})$ is the exact symmetry verified in the framework's Dirac operator analysis.
