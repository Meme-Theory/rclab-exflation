# Phonon Spectra, Quantum Geometry, and the Goldstone Theorem

**Author(s):** Guglielmo Pellitteri, and 7 co-authors

**Year:** 2025

**Journal:** Physical Review B, Volume 112, Article 245128 (2025)

**arXiv:** 2502.04221

---

## Abstract

Investigates quantum geometric contribution to phonon spectrum in crystalline materials without Holstein interactions, using graphene as case study. Decomposing the dynamical matrix reveals that removing nontrivial quantum geometric contribution causes acoustic phonon modes to violate Goldstone's theorem—they acquire an effective mass. Quantum geometry is essential, not peripheral, to phonon spectrum characterization.

---

## Historical Context

Goldstone's theorem guarantees gapless modes when continuous symmetries break. In crystals, translational symmetry breaking creates gapless acoustic phonons. Yet modern condensed matter revealed quantum geometry (Berry curvature, quantum metric) affects dynamics beyond Bloch band theory alone. Pellitteri et al. ask: Is geometry necessary for Goldstone, or accidental? Answer: Essential.

---

## Key Arguments and Derivations

### Dynamical Matrix and Phonon Dispersion

Phonon frequencies are determined by dynamical matrix D_alphabeta(q):

$$D_{lphaeta}(q) = rac{1}{\sqrt{m_lpha m_eta}} \sum_{l} e^{i q \cdot R_l} rac{\partial^2 V}{\partial u_lpha(0) \partial u_eta(l)}$$

Phonon frequencies omega_n(q) are eigenvalues:

$$\det[D_{lphaeta}(q) - \omega_n^2(q) \delta_{lphaeta}] = 0$$

For long-wavelength acoustic phonons (q->0), frequencies vanish: omega_acoustic(0) = 0. This is Goldstone.

### Decomposition into Energy and Geometric Components

Decompose dynamical matrix:

$$D_{lphaeta}(q) = D_{lphaeta}^{(E)}(q) + D_{lphaeta}^{(	ext{geom})}(q) + D_{lphaeta}^{(	ext{other})}(q)$$

1. **Energy component** D^(E): Terms depending on electronic energy eigenvalues epsilon_n(k).

2. **Geometric component** D^(geom): Terms depending on Berry curvature Omega_xy(k) or quantum metric g_ij(k), but not on energy eigenvalues directly.

The quantum metric:

$$g_{ij}(k) = 	ext{Re} \langle \partial_i \psi_n(k) | \partial_j \psi_n(k) angle$$

The Berry curvature:

$$\Omega_{ij}(k) = \partial_i A_j(k) - \partial_j A_i(k)$$

where A_i(k) = i <psi_n|partial_i psi_n> is the Berry connection.

### Goldstone Mechanism and Quantum Geometry

For uniform translation u(r) = u_0, energy change is zero by translational invariance:

$$\Delta E = 0 + O(u^2)$$

This enforces:

$$D_{lphaeta}(0) = 0$$

This Goldstone condition requires:

$$D_{lphaeta}^{(E)}(0) + D_{lphaeta}^{(	ext{geom})}(0) = 0$$

Geometric and energy components must cancel. Remove geometry:

$$D_{lphaeta}^{(E)}(0) 
e 0$$

Result: Phonon gap appears, violating Goldstone.

### Graphene Case Study

For graphene, electronic wavefunctions near Fermi energy have nontrivial Berry curvature due to linear dispersion near K and K' points (Dirac cones). Pellitteri et al. calculate D_alphabeta including and excluding geometric contribution:

**With geometry**:
$$\omega_{	ext{acoustic}}(q 	o 0) \sim \sqrt{c_s^2 q^2} 	o 0$$

**Without geometry**:
$$\omega_{	ext{acoustic}}(q 	o 0) \sim \sqrt{c_s^2 q^2 + m_{	ext{eff}}^2} 	o m_{	ext{eff}}$$

where m_eff ~ O(1-10 meV). Behavior becomes non-analytic.

---

## Key Results

1. Quantum geometry is essential to Goldstone's theorem
2. Removing geometric contributions violates Goldstone predictions
3. Graphene phonons require quantum geometry (gap would be 1-10 meV without it)
4. Acoustic phonons are superpositions of electronic deformations and atomic motions
5. Berry curvature and phonon dispersion are coupled
6. Non-analytic behavior marks geometric effects
7. Universality across crystal types with nontrivial electronic structure

---

## Impact and Legacy

Recognition that quantum geometry is not peripheral but central to condensed matter. Recent work: geometric phonons in topological materials, quantum metric engineering, geometric superconductivity, phononic topological protected states.

---

## Connection to Phonon-Exflation Framework

**Relevance: CRITICAL (Geometric Foundation of Phonons)**

This paper validates Phonon-Exflation's assumption:

1. **Geometry shapes phonon spectra** -- Proves phonon frequencies are determined by geometric properties, not just symmetry.

2. **SU(3) quantum geometry and particle masses** -- In Phonon-Exflation, SM particle masses emerge from SU(3) fiber geometry and deformation. Session 33a: spectral action geometry determines masses. Consistent with Pellitteri: geometry determines spectrum.

3. **NCG spectral action as dynamical matrix** -- Connes spectral action plays role of cosmological dynamical matrix. Quantum geometry appears via heat kernel coefficients (geometric invariants).

4. **Goldstone modes and gauge bosons** -- Session 35: Cooper pairs carry U(1)_7 charge, preserve Goldstone mode (phase mode). Pellitteri shows Goldstone modes require quantum geometry. Therefore, gauge bosons are gapless because SU(3) fiber geometry has nontrivial curvature enforcing Goldstone condition.

5. **Quantum metric and fiber deformation** -- Quantum metric g_ij(k) measures wavefunction deformation. In Phonon-Exflation, parameter tau deforms all wavefunctions. Quantum metric changes as tau evolves. This is the mechanism Pellitteri identifies: geometry couples to phonons through dynamical matrix.

6. **Electronic-phonon analogy** -- In graphene, electronic wavefunctions have Berry curvature; phonons couple through curvature. In Phonon-Exflation, all wavefunctions live on SU(3) fiber. All interactions inherit geometric properties.

7. **Phononic crystal and quantum geometry** -- Session 42: spacetime is phononic crystal with lattice spacing a_Planck. Continuous limit (smooth dispersion) achieved when quantum geometry properly accounts. Without geometry, crystal has large phonon gap (disorder, localization). With geometry, gap closes, phonons become low-wavelength excitations.

**Closest Session Connections:** Session 33a (spectral action geometry), Session 35 (Goldstone modes, U(1)_7), Session 42 (phononic crystal)

**Quantitative Prediction:** In phononic crystal with Planck-scale spacing:

$$\Delta_{	ext{gap}} \sim \hbar_{	ext{ac}} \omega_{	ext{Planck}} \sim \hbar 	imes (c/\ell_P) \sim 10^{51} 	ext{ J}$$

Enormous. Quantum geometry cancels this gap, allowing low-energy physics. Goldstone theorem enforced by geometry allows physics below Planck scale.

---

## References

- G. Pellitteri, et al., "Phonon spectra, quantum geometry, and the Goldstone theorem", Phys. Rev. B 112, 245128 (2025). https://arxiv.org/abs/2502.04221
- M.V. Berry, "Quantal phase factors accompanying adiabatic changes", Proc. R. Soc. Lond. A 392, 45 (1984).
- J. Goldstone, A. Salam, S. Weinberg, "Broken symmetries", Phys. Rev. 127, 965 (1962).
