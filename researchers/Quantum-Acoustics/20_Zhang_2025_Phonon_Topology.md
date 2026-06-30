# Advances in Phonons: From Band Topology to Phonon Chirality

**Author(s):** Tiantian Zhang, Yizhou Liu, Hu Miao, Shuichi Murakami
**Year:** 2025
**Journal:** [preprint]
**arXiv:** 2505.06179
**Relevance:** HIGH

---

## Abstract

Phonons are ubiquitous quasiparticles in solid state systems describing the quantized vibrations of a crystal lattice. Phonons play a central role in a wide range of physical phenomena, from transport to symmetry-breaking orders, such as charge density waves and superconductivity. Traditionally treated as spin-0 bosons that obey Bose-Einstein statistics, phonons have recently emerged as a fertile ground for exploring topological physics, spurred by the rapid development of topological band theory initially formulated for fermionic systems. It is now understood that the phonon eigenstates, characterized by their eigenvalues and eigenvectors, can carry nontrivial topological invariants, including the Berry phase and Chern number. This new understanding opens up avenues to investigate the interplay between lattice dynamics, topology, and chirality in bosonic systems. In this article, we review recent theoretical and experimental advances in the field of topological phonons and circularly polarized phonons. We introduce foundational concepts, including the classification of phononic band structures, symmetry-protected topological phases, and the definition of topological invariants in bosonic systems. We emphasize the concept of phonon angular momentum and its fundamental connection to Weyl phonons in PT-breaking systems. Key experimental progresses on topological and circularly polarized phonons are discussed. We also outline outstanding challenges and promising directions for future research, such as the role of topology in phonon-mediated quasiparticle interactions and the manipulation of phonon angular momentum for potential applications in quantum technologies.

---

## Key Arguments and Derivations

### I. Phonons: Theoretical Basis and Experimental Probes

The review begins with the harmonic approximation for lattice dynamics. For a system with one atom per unit cell, the lattice Hamiltonian is expressed as kinetic plus potential energy with force constants $\Psi^{\alpha\beta}_{ij}$. The eigenvalue problem $\det|D(\mathbf{q}) - \omega^2 I| = 0$ determines the phonon dispersion, where $D(\mathbf{q})$ is the dynamical matrix constructed from Fourier-transformed force constants. For multi-atom unit cells with $r$ atoms, the dynamical matrix generalizes to a $3r \times 3r$ matrix yielding 3 acoustic and $(3r-3)$ optical modes.

The phonon dynamical structure factor $S(\mathbf{Q}, \omega)$ is derived from the charge density correlation function, expanded under the harmonic approximation using the Baker-Hausdorff theorem. The single-phonon term provides direct access to both eigenvalues (frequencies) and eigenvectors (through scattering intensity). Experimental probes covered include infrared spectroscopy (dipole selection rules), Raman scattering (polarizability tensor, Stokes/anti-Stokes processes), inelastic X-ray scattering (IXS), inelastic neutron scattering (INS), resonant inelastic X-ray scattering (RIXS via Kramers-Heisenberg formalism), and momentum-resolved electron energy loss spectroscopy (HR-MEELS).

### II. Topological Phonons: General Topological Band Theory

The paper presents the "ten-fold way" classification (Altland-Zirnbauer) adapted to phononic systems. Phonons, being spin-0 bosons, have $T^2 = +1$ (or $T^2 = 0$ if time-reversal is broken). This restricts gapped phonon topological classifications to classes A, AI, AIII, BDI, D, C, and CI. The classification is determined by:
- Time-reversal symmetry $T$: $T^{-1}H(\mathbf{k})T = H(-\mathbf{k})$, with $U_T U_T^* = \pm 1$
- Particle-hole symmetry $C$: $C^{-1}H(\mathbf{k})C = -H(-\mathbf{k})$
- Chiral symmetry $S$: $S^{-1}H(\mathbf{k})S = -H(\mathbf{k})$

The Chern number $C = \frac{1}{2\pi}\int_{\text{BZ}} \Omega(\mathbf{k})\, d^2k$ classifies Class A in 2D (the phononic quantum anomalous Hall analog). For gapless phonon systems, the classification is based on band crossing degeneracy and codimension, leading to Dirac phonons, Weyl phonons, unconventional Weyl phonons, and nodal-line phonons.

**Dirac and Weyl phonons:** The Dirac phonon Hamiltonian is $H_D(\mathbf{k}) = \begin{pmatrix} v_0 \boldsymbol{\sigma}\cdot\mathbf{k} & m(\mathbf{k}) \\ m^*(\mathbf{k}) & -v_0\boldsymbol{\sigma}\cdot\mathbf{k}\end{pmatrix}$, with eigenvalues $E_\pm = \pm\sqrt{m^2 + v_0^2 k^2}$. When $m = 0$, the Dirac point decomposes into two Weyl phonons with opposite chirality, described by $H^\pm_{\text{Weyl}} = v_0(k_z \sigma_x + k_x \sigma_y \mp i k_y \sigma_z)$, carrying Chern numbers $C = \pm 1$.

**Unconventional Weyl phonons:** Higher-order Weyl phonons with $|C| = 2$ arise from spin-1 rotation generators $H(\mathbf{k}) = \mathbf{k}\cdot\mathbf{L}$ (spin-1 Weyl) or from fourfold charge-2 Dirac points. Weyl phonons with monopole charge 4 exist in three varieties: double spin-1, spin-3/2, and twofold quadruple.

### III-IV. Topological Phonons in Low Dimensions and Bulk Materials

The SSH (Su-Schrieffer-Heeger) model is adapted for 1D phononic chains, demonstrating topologically protected edge modes. In 2D, honeycomb lattice models support phononic quantum anomalous Hall-like, quantum valley Hall-like, and quantum spin Hall-like states, as well as Stiefel-Whitney insulator analogs.

In 3D bulk materials, the B-20 structure (MSi family, $M$ = Fe, Co, Mn, Re, Ru) hosts spin-1 Weyl phonons at $\Gamma$ and charge-2 Dirac phonons at $R$. The surface states follow the Weierstrass elliptic function $\wp(z; 2\pi, 2\pi)$, forming double-helicoid Riemann sheets. Face-centered silicon hosts triple-point phonons with winding number $n_W = \pm 2$. Body-centered silicon hosts $\mathbb{Z}_2$ Dirac phonons.

### V. From Topological Chirality to Rotational Chirality

**Phonon angular momentum (AM):** Defined as $l^{\alpha,\nu}_\mathbf{q} = \text{Im}[\boldsymbol{\epsilon}^*_{\mathbf{q}\nu} \times \boldsymbol{\epsilon}_{\mathbf{q}\nu}]_\alpha$, representing the circular polarization of atomic motions in the unit cell. A phonon mode with nonzero AM has atoms exhibiting net circular motion.

**Phonon helicity:** Defined as $h_{\nu\mathbf{q}} = \hat{\mathbf{q}} \cdot \mathbf{l}_{\nu\mathbf{q}}$, a pseudoscalar quantity that provides a convention-independent definition of phonon chirality. Nonzero helicity requires 3D (propagation direction plus circular motion plane), making chiral phonons inherently 3D objects.

**Pseudo-angular momentum (PAM):** Defined by the eigenvalue of the rotation operator $C_n$: $D(C_n)\mathbf{u}_{\nu\mathbf{q}} = e^{-i2\pi l_{\text{ph}}/n}\mathbf{u}_{\nu\mathbf{q}}$. PAM is a conserved quantity during phonon scattering processes in $C_n$-invariant systems but has no intrinsic one-to-one correspondence with AM. PAM is a global property; AM is local.

**Connection:** Weyl phonons are simultaneously topological (nonzero Chern number) and circularly polarized (nonzero helicity). Breaking both $P$ and $T$ symmetries is essential for realizing both nonzero Chern number and angular momentum simultaneously.

### VI. Experimental Progress

Experimental observations include: Weyl and Dirac phonons measured by IXS and INS in FeSi, CoSi, and related materials; topological phonons observed by EELS in 2D materials; circularly polarized phonons detected via helicity-resolved Raman scattering in Te and $\alpha$-HgS; phonon AM directly measured using mechanical torque setups.

### VII. Conclusions and Perspectives

Open questions identified: (1) Coupling between topological phonons and topological electrons in Weyl semimetals; (2) Quantum geometry of phonons (quantum metric as real part of quantum geometry); (3) Phonon thermal Hall effect origin in strongly correlated insulators ($\kappa_{xy}/\kappa_{xx} \sim 10^{-3}$); (4) Circularly polarized phonons for dark matter detection; (5) Topological surface phonons for robust spin and heat transport.

---

## Key Results

1. Phonons can carry nontrivial topological invariants (Berry phase, Chern number) analogous to electronic systems, classified by the ten-fold way restricted to bosonic symmetry classes
2. Gapless topological phonons include Dirac, Weyl, unconventional Weyl (spin-1, charge-2 Dirac, quadruple), and nodal-line varieties, classified by degeneracy and codimension
3. In chiral 3D crystals, all acoustic phonons at $\Gamma$ are spin-1 Weyl phonons; transverse acoustic modes carry Chern numbers $\pm 2$
4. Phonon angular momentum (AM) is a local property reflecting circular atomic motion; pseudo-angular momentum (PAM) is a global property reflecting $C_n$ eigenvalues; they are distinct quantities with no intrinsic one-to-one correspondence
5. Phonon helicity $h = \hat{\mathbf{q}}\cdot\mathbf{l}$ provides a convention-independent definition of chirality, inherently 3D
6. Weyl phonons are both topological and circularly polarized, linking topology and chirality through the Chern number
7. Topological surface phonon states form helicoid Riemann sheets described by the Weierstrass elliptic function in the MSi family
8. Experimental confirmation achieved: Weyl/Dirac phonons by IXS/INS, circularly polarized phonons by Raman in Te and $\alpha$-HgS, phonon AM by mechanical torque
9. Phonon nodal lines are more robust than electronic ones because phonons lack spin-orbit coupling
10. The quantum geometry of phonons (quantum metric) may set a lower bound on electron-phonon coupling

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Dynamical matrix (single atom) | $D^{\alpha\beta}(\mathbf{q}) = \frac{1}{M}\sum_l \Psi^{\alpha\beta}_l e^{-i\mathbf{q}\cdot\mathbf{R}_l}$ | Eq. 4 |
| Dynamical matrix (multi-atom) | $D^{\alpha\beta}_{\mathbf{q},ss'} = \frac{1}{\sqrt{M_s M_{s'}}}\sum_l \Psi^{\alpha\beta}_{l,ss'} e^{-i\mathbf{q}\cdot\mathbf{R}_l}$ | Eq. 5 |
| Phonon Hamiltonian | $H = \sum_{\mathbf{q},\sigma}(a^\dagger_{\mathbf{q}\sigma}a_{\mathbf{q}\sigma} + \frac{1}{2})\hbar\omega_\sigma(\mathbf{q})$ | Eq. 11 |
| Dynamical structure factor (1-phonon) | $S(\mathbf{Q},\omega)_{1p} \propto \sum_{\mathbf{q},\sigma}\frac{1}{\omega_\sigma}\left|\sum_s \frac{f_s(\mathbf{Q})}{\sqrt{2M_s}}e^{-W_d}\mathbf{Q}\cdot\boldsymbol{\epsilon}_{\mathbf{q}\sigma}(s)e^{i\mathbf{Q}\cdot\mathbf{r}_s}\right|^2$ | Eq. 20 |
| Chern number | $C = \frac{1}{2\pi}\int_{\text{BZ}}\Omega(\mathbf{k})\, d^2k$ | Eq. 36 |
| Dirac phonon Hamiltonian | $H_D(\mathbf{k}) = \begin{pmatrix} v_0\boldsymbol{\sigma}\cdot\mathbf{k} & m(\mathbf{k}) \\ m^*(\mathbf{k}) & -v_0\boldsymbol{\sigma}\cdot\mathbf{k}\end{pmatrix}$ | Eq. 37 |
| Weyl phonon Hamiltonian | $H^\pm_{\text{Weyl}}(\mathbf{k}) = v_0\begin{pmatrix} k_z & k_x \mp ik_y \\ k_x \pm ik_y & -k_z \end{pmatrix}$ | Eq. 38 |
| Triple-point Hamiltonian | $H_{TP} = \begin{pmatrix} v_T k_z & 0 & ck_+ \\ 0 & v_T k_z & ck_- \\ c^*k_- & c^*k_+ & v_L k_z \end{pmatrix}$ | Eq. 75 |
| Winding number | $n_W = \oint_C \frac{dl}{4\pi i}\text{Tr}[\sigma_z H_2^{-1}\partial_l H_2] = \pm 2$ | Eq. 77 |
| Weierstrass surface states | $\omega(k_x,k_y) \sim \text{Im}\{\log[\wp(z; 2\pi,2\pi)]\}$ | Eq. 74 |
| Phonon helicity | $h_{\nu\mathbf{q}} = \hat{\mathbf{q}}\cdot\mathbf{l}_{\nu\mathbf{q}}$ | Eq. 90 |
| PAM eigenvalue | $D(C_n)\mathbf{u}_{\nu\mathbf{q}} = e^{-i2\pi l_{\text{ph}}/n}\mathbf{u}_{\nu\mathbf{q}}$ | Eq. 93 |
| PAM with screw symmetry | $l_{\text{ph}} = l_{\text{rot}} + \frac{\mathbf{q}\cdot\boldsymbol{\tau}_{m/n}}{2\pi/n}$ | Sec. V.A.3 |
| Phonon polariton Hamiltonian | $H = \begin{pmatrix} \omega_{\text{phonon}}(\mathbf{k}) & \Delta \\ \Delta^\dagger & \omega_{\text{photon}}(\mathbf{k})\end{pmatrix}$ | Eq. 73 |

---

## Relevance to Phonon-Exflation

This review is directly relevant to the phonon-exflation framework's treatment of phononic excitations on the internal $M^4 \times SU(3)$ geometry. The ten-fold way classification for bosonic systems (restricted to $T^2 = +1$ classes including BDI) maps onto the project's AZ class BDI classification of the Dirac spectrum on $SU(3)$. The phonon angular momentum formalism and the distinction between AM (local, circular atomic motion) and PAM (global, $C_n$ eigenvalue) provides the condensed-matter language for understanding how quasiparticle excitations in the framework carry angular momentum quantum numbers. The Weyl phonon results -- that topology and chirality are linked through nonzero Chern number in PT-breaking systems -- parallels the project's finding that $[iK_7, D_K] = 0$ breaks $SU(3) \to U(1)_7$ in the Dirac spectrum. The topological protection of phononic surface/edge states against disorder provides a condensed-matter precedent for the integrability-protected GGE relic state found in the instanton gas analysis.
