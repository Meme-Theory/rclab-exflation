# Geometric phase from Aharonov-Bohm to Pancharatnam-Berry and beyond

**Author(s):** Eliahu Cohen, Hugo Larocque, Frederic Bouchard, Farshad Nejadsattari, Yuval Gefen, Ebrahim Karimi
**Year:** 2019
**Journal:** Nature Reviews Physics 1, 437-449 (2019)
**arXiv:** 1912.12596
**Relevance:** CRITICAL

---

## Abstract

Whenever a quantum system undergoes a cycle governed by a slow change of parameters, it acquires a phase factor: the geometric phase. Its most common formulations are known as the Aharonov-Bohm, Pancharatnam and Berry phases, but both prior and later manifestations exist. Though traditionally attributed to the foundations of quantum mechanics, the geometric phase has been generalized and became increasingly influential in many areas from condensed-matter physics and optics to high energy and particle physics and from fluid mechanics to gravity and cosmology. Interestingly, the geometric phase also offers unique opportunities for quantum information and computation. In this Review we first introduce the Aharonov-Bohm effect as an important realization of the geometric phase. Then we discuss in detail the broader meaning, consequences and realizations of the geometric phase emphasizing the most important mathematical methods and experimental techniques used in the study of geometric phase, in particular those related to recent works in optics and condensed-matter physics.

---

## Key Arguments and Derivations

### 1. Introduction: The Aharonov-Bohm Effect as Geometric Phase (Section 1)

The review opens with the Aharonov-Bohm (AB) effect as the foundational example. When two electronic wavepackets encircle a magnetic flux confined to a solenoid, they acquire a relative phase proportional to the enclosed magnetic flux, even though the magnetic field is zero along their paths. This AB phase is topological -- it depends only on topological invariants, not on the shape of the path. The AB phase is shown to be a special case of the broader geometric phase.

Berry's 1984 discovery is then presented: when parameters of a quantum Hamiltonian are slowly cycled around a closed path C, the system acquires a geometric phase gamma[C] in addition to the dynamical phase. This phase depends only on the geometry of the path in parameter space. The review traces the historical anticipations: Pancharatnam (1956, polarization optics), Longuet-Higgins (1958, molecular physics), and later generalizations by Wilczek-Zee (non-Abelian, 1984), Aharonov-Anandan (non-adiabatic, 1987), Samuel-Bhandari (non-unitary, non-cyclic, 1988), and Hannay (classical angles, 1985).

### 2. Open Systems and Geometric Dephasing (Section 1, continued)

For open (non-Hermitian) systems, the geometric phase becomes complex. The real part modifies the phase, while the imaginary part gives rise to "geometric dephasing." Following a closed trajectory adiabatically n times, the wavefunction picks up factors organized as an expansion in powers of 1/T: the T^1 term is the dynamical phase and dephasing; the T^0 term is the geometric contribution (proportional to winding number n); and higher-order terms are non-adiabatic corrections. The imaginary part of the geometric phase correction, dubbed geometric dephasing, can enhance or reduce standard dynamical dephasing depending on the winding direction.

### 3. Mathematical Formalism: Fiber Bundles and Holonomy (Section 2)

The geometric phase is formulated in the language of fiber bundles. The system's Hilbert space H and the parameter manifold M form a vector bundle M x H. Wavefunctions are sections of this bundle; differentiation requires a connection D (associated with the Berry connection A). Parallel transport along a closed path maps a state psi(R) to H(gamma,D) psi(R), where H is the holonomy -- this IS the geometric phase. The curvature of the bundle (the Berry curvature) corresponds to the holonomy of an infinitesimally small loop. The integral of the curvature over a closed surface yields an integer (the Chern number), encoding the topological structure of the bundle.

### 4. Geometric Phase in Optics (Section 3)

Two types of optical geometric phase are distinguished: (i) spin-redirection phase (light with fixed polarization changing direction), and (ii) Pancharatnam-Berry phase (fixed direction, changing polarization through anisotropic media).

**Pancharatnam-Berry phase:** Pancharatnam noted that when polarization is cycled through three states on the Poincare sphere, a non-transitive phase difference arises equal to half the enclosed solid angle: arg[<psi_A_tilde|psi_A>] = Omega_ABC/2. Berry showed this is equivalent to the adiabatic geometric phase in quantum mechanics.

**Optical phase elements and spin-orbit coupling:** A half-wave plate (HWP) with orientation angle theta imprints a geometric phase 2*theta on circularly polarized light while flipping its handedness. Spatially varying HWP orientation theta(x,y) creates space-variant phase patterns exp[+/-2i*theta(x,y)] for left/right circular polarization. This enables q-plates (liquid crystal devices with theta(phi) = 2q*phi) that generate orbital angular momentum (OAM) via spin-orbit coupling, conserving total angular momentum. Applications include quantum walks using OAM states as walker space and polarization as the coin.

### 5. Role in Condensed-Matter Physics (Section 4)

**Electronic Bloch states and Zak phase:** For electrons in periodic lattices, the Berry connection in k-space is A(k) = -i<u_k|nabla_k|u_k>. The Berry curvature is Omega(k) = nabla_k x A(k). As quasi-momentum traverses the Brillouin zone, the Bloch state acquires a geometric phase gamma = oint A(k) . dk. On a closed 2D torus (Brillouin zone), this integral is quantized by Chern numbers. Zak (1989) introduced the geometric phase for 1D Bloch electrons; with inversion symmetry, the Zak phase takes only values 0 or 2*pi*n.

**Quantum Hall Effect:** The TKNN formalism relates the Hall conductance directly to the Berry curvature. For a 2D electron gas in a perpendicular magnetic field, the transverse Hall conductance is sigma_xy = (e^2/h) * sum_n int (dk/2pi) Omega_z^n. Since the Chern number is an integer, the Hall conductance is quantized in units of e^2/h.

**Electric Polarization:** The modern theory of electric polarization (Resta, King-Smith & Vanderbilt) relates the change in polarization to the Berry curvature: dP_j/dlambda = (e/V) sum_{n,k} Omega_{k_j,lambda}^n(k). Using Stokes' theorem, Delta P = (e/2pi) sum_n gamma_n, directly connecting polarization change to the Zak phase.

**Exchange Statistics:** The Pauli sign (-1)^{2S} was derived as a geometric phase of topological origin. In 3D, exchange paths can be shrunk to a point, restricting statistics to bosons and fermions. In 2D, paths cannot be shrunk, allowing anyonic statistics with arbitrary phase theta_ij. Fractional quantum Hall quasi-particles are the primary realization of anyons.

### 6. Conclusion and Outlook (Section 5)

The geometric phase influences high energy physics, gravity and cosmology, fluid mechanics, and chemical physics. Non-Abelian geometric phases enable holonomic quantum computation: gates based on geometric phase naturally eliminate dynamical-phase errors, and degenerate states avoid bit-flip errors. Topological tuning can make such computation fault-tolerant.

## Key Results

1. The Aharonov-Bohm phase phi_AB = e*Phi/hbar is a special case of the geometric phase, being a topological invariant depending only on the enclosed flux.
2. Berry's geometric phase gamma[C] = i oint <n,t|nabla_R|n,t> . dR is a holonomy in a line bundle over parameter space.
3. In open systems, the geometric phase becomes complex, with an imaginary part causing geometric dephasing that depends on winding direction.
4. The Pancharatnam phase for three polarization states equals half the solid angle subtended on the Poincare sphere: Omega_ABC/2.
5. The Berry connection A(k) = -i<u_k|nabla_k|u_k> and curvature Omega(k) = nabla_k x A(k) characterize all energy bands in solids via the Zak phase.
6. The TKNN Hall conductance sigma_xy = (e^2/h) sum_n int (dk/2pi) Omega_z^n is topologically quantized by Chern numbers.
7. The modern theory of electric polarization relates Delta P to the sum of Zak phases: Delta P = (e/2pi) sum_n gamma_n.
8. Exchange statistics in 2D yield anyonic phases, with the geometric topological phase for double exchange being +/-2*theta_ij depending on winding direction.
9. Non-Abelian geometric phases (Wilczek-Zee) enable holonomic quantum computation that is intrinsically fault-tolerant.
10. The geometric phase has been generalized to non-adiabatic (Aharonov-Anandan), non-cyclic and non-unitary (Samuel-Bhandari) settings.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Aharonov-Bohm phase | $\varphi_{AB} = \frac{e\Phi}{\hbar}$ | Eq. (1) |
| Berry phase (adiabatic) | $\gamma[C] = i \oint_C \langle n,t \mid \nabla_{\mathbf{R}} \mid n,t \rangle \cdot d\mathbf{R}$ | Eq. (2) |
| Open-system phase expansion | $\mid\Psi_{final}\rangle = e^{iET\mid n\mid - \alpha T\mid n\mid} e^{i\theta^0_{Berry} T^0 n + i\delta\theta^{Re}_{Berry} T^0 n - \delta\theta^{Im}_{Berry} T^0 n} e^{(\ldots)T^{-1}\mid n\mid} \mid\Psi_{initial}\rangle$ | Eq. (3) |
| Bloch state with geometric phase | $\mid\psi_{n,\mathbf{k}(t)}(\mathbf{r},t)\rangle = e^{i\gamma_n} e^{-\frac{i}{\hbar}\int_{t_0}^{t} \mathcal{E}_n(\mathbf{k}(t'))dt'} \mid\psi_{n,\mathbf{k}(t)}(\mathbf{r},t_0)\rangle$ | Eq. (4) |
| Total Zak phase | $\gamma = \sum_n \gamma_n$ | Eq. (5) |
| Current density (Berry curvature) | $\mathbf{j} = -\frac{1}{V}\sum_{n,k} e\mathbf{v}_n(\mathbf{k}) = \frac{e^2}{\hbar}\int \frac{d^2\mathbf{k}}{(2\pi)^2}\sum_n \mathbf{\Omega}_n(\mathbf{k}) \times \mathbf{E}$ | Eq. (6) |
| TKNN Hall conductance | $\sigma_{xy} = \frac{e^2}{\hbar}\sum_n \int \frac{dk}{2\pi} \Omega_z^n$ | Eq. (7) |
| Polarization derivative | $\frac{dP_j}{d\lambda} = \frac{e}{V}\sum_{n,\mathbf{k}} \Omega^n_{k_j,\lambda}(\mathbf{k})$ | Eq. (8) |
| Berry curvature (polarization) | $\Omega^n_{k_j,\lambda} = i\left(\langle \frac{\partial u}{\partial k_j}\mid\frac{\partial u}{\partial \lambda}\rangle - c.c.\right)$ | Eq. (9) |
| 1D polarization change | $\Delta P = \frac{e}{2\pi}\int_0^1 d\lambda \sum_n \int_0^{2\pi} dk\; \Omega^n_{k,\lambda}$ | Eq. (10) |
| Polarization-Zak relation | $\Delta P = \frac{e}{2\pi}\sum_n \gamma_n$ | Eq. (11) |
| N-dim polarization change | $\Delta P_j = \frac{ef}{(2\pi)^N}\sum_n \int_0^1 d\lambda \int d^N k\; \Omega^n_{k_j,\lambda}$ | Eq. (12) |
| Exchange statistics (Abelian anyons) | $P_{i,j}\Psi(x_1,x_2,...,x_i,...x_j...) = e^{i\theta_{ij}}\Psi(x_1,x_2,...,x_i,...x_j...)$ | Eq. (13) |
| Berry connection | $\mathcal{A}(\mathbf{k}) = -i\langle u_{\mathbf{k}}\mid\nabla_{\mathbf{k}}\mid u_{\mathbf{k}}\rangle$ | Sec. 4 |
| Berry curvature | $\mathbf{\Omega}(\mathbf{k}) = \nabla_{\mathbf{k}} \times \mathcal{A}(\mathbf{k})$ | Sec. 4 |
| Pancharatnam phase | $\arg[\langle\psi_{\tilde{A}}\mid\psi_A\rangle] = \Omega_{ABC}/2$ | Sec. 3 |
| Geometric phase from HWP | $e^{\pm 2i\theta(x,y)}$ for L/R circular polarization | Sec. 3 |
| Dirac phase | $\frac{e}{\hbar}\int_\gamma \mathbf{A}\cdot d\mathbf{r}$ | Sec. 2 |
| Semi-classical EOM | $\mathbf{v} = \dot{\mathbf{r}} = \frac{1}{\hbar}\frac{\partial\mathcal{E}(\mathbf{k})}{\partial k} - \dot{\mathbf{k}}\times\mathbf{\Omega}(\mathbf{k}),\quad \dot{\mathbf{k}} = \frac{e}{\hbar}\mathbf{E}$ | Sec. 4 |

## Relevance to Phonon-Exflation

The geometric phase is the mathematical backbone of holonomy on the M4 x SU(3) fiber bundle central to the phonon-exflation framework. The Berry connection on the internal SU(3) fiber directly maps to the gauge connection governing transit physics: as the compactification parameter tau evolves, the Dirac operator on the total space acquires a geometric phase that encodes the Wilczek-Zee non-Abelian holonomy relevant to the P-30w gate. The paper's treatment of Berry curvature as the holonomy of infinitesimal loops, Chern number quantization, and the TKNN formula provide the precise mathematical language for spectral action computations over the KK fiber. The exchange statistics section connects to the BDI topological classification already proven for the framework's Dirac spectrum. The geometric dephasing discussion in open systems is directly relevant to understanding decoherence in the transit (non-equilibrium, non-Hermitian) regime.
