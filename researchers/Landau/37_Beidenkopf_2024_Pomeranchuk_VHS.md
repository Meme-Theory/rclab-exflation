# Pomeranchuk Instability Induced by an Emergent Higher-Order van Hove Singularity on the Distorted Kagome Surface of Co3Sn2S2

**Author(s):** Pranab Kumar Nag, Rajib Batabyal, Julian Ingham, Noam Morali, Hengxin Tan, Jahyun Koo, Armando Consiglio, Enke Liu, Nurit Avraham, Raquel Queiroz, Ronny Thomale, Binghai Yan, Claudia Felser, Haim Beidenkopf
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2410.01994
**Relevance:** HIGH

---

## Abstract

Materials hosting flat bands at the vicinity of the Fermi level promote exotic symmetry broken states. Common to many of these are van Hove singularities at saddle points of the dispersion or even higher-order van Hove singularities where the dispersion is flattened further. The band structure of kagome metals hosts both a flat band and two regular saddle points flanking a Dirac node. We investigate the kagome ferromagnetic metal Co3Sn2S2 using scanning tunneling spectroscopy. We identify a new mechanism by which a triangular distortion on its kagome Co3Sn surface termination considerably flattens the saddle point dispersion, and induces an isolated higher-order van Hove singularity (HOvHS) with algebraically divergent density of states pinned to the Fermi energy. The distortion-induced HOvHS precipitates a Pomeranchuk instability of the Fermi surface, resulting in the formation of a series of nematic electronic states. We visualize the nematic order across an energy shell of about 100 meV in both real-, reciprocal-, and momentum-spaces, as a cascade of wavefunction distributions which spontaneously break the remaining rotational symmetry of the underlying distorted kagome lattice, without generating any additional translational symmetry breaking. It signifies the spontaneous removal of a subset of saddle points from the Fermi energy to lower energies.

---

## Key Arguments and Derivations

### Surface reconstruction generates HOvHS

The Co3Sn surface of Co3Sn2S2 reconstructs by an inward shift of Co ions (~10% of Co-Co bond length) within triangles not over S ions. This breaks C_6 down to C_3. Ab initio calculations show the reconstruction shifts the m-type saddle point at M downward by ~100 meV, flattening the hole-like dispersion along Gamma-M. The quadratic coefficient vanishes (a_y -> 0), making the leading dispersion quartic: epsilon(k) = a_x k_x^2 - a_y k_y^2 + b_x k_x^4 - b_y k_y^4 + b_{xy} k_x^2 k_y^2 + ...

### Tight-binding model

A minimal tight-binding model with d_z^2 orbitals on a distorted kagome lattice reproduces the mechanism:

H = epsilon sum_i c^dag_i c_i - t_1 sum_{<ij>} c^dag_i c_j - t_2 sum_{<<ij>>} c^dag_i c_j - t_3 sum_{<<<ij>>>} c^dag_i c_j - t_4 sum_{<<<<ij>>>>} c^dag_i c_j

Setting t_1 > t_2 (nearest-neighbor asymmetry) gaps the Dirac node at K. Adding t_3 = -t_4 (opposite sign inter-unit-cell hopping) shifts the m-type saddle point down, generating the HOvHS. The DOS diverges as |delta E|^{-1/4}, characteristic of quartic dispersion.

### Pomeranchuk instability

The HOvHS precipitates a d-wave Pomeranchuk instability. A patch model with degrees of freedom near the three M-points shows that forward scattering (small momentum transfer) dominates, and d-wave Pomeranchuk order appears at mean-field level and remains the leading instability under RG flow. The ground state is a linear combination O_1(k_x^2 - k_y^2) + O_2 (2k_x k_y), with a cubic Landau free energy term F_3 = O_1^2 - 3O_1 O_2^2 producing a charge nematic.

### Experimental visualization

Using STM super-resolution (collapsing hundreds of unit cells into one), the authors directly image:
- Nematic wavefunction distributions breaking C_3 symmetry within ~100 meV of E_F
- Stripe state at -80 to -35 meV
- Edge state at -20 to +50 meV (localized at inner edge of kagome hexagon)
- Wavefunction center-of-mass evolution equivalent to charge pumping (unit cell displacement between high and low energies)
- Symmetric wavefunctions recovered at |E| > 100 meV from E_F

---

## Key Results

1. Triangular surface reconstruction of kagome lattice generates HOvHS at the m-type saddle point under equilibrium conditions (no external tuning needed)
2. DOS diverges as |E|^{-1/4} at the HOvHS, pinned to E_F by the large density of states
3. The HOvHS drives a d-wave Pomeranchuk instability producing nematic charge order without translational symmetry breaking
4. Multiple nematic states cascade across ~100 meV energy shell: stripe, bond, and edge states
5. QPI patterns show C_3-broken scattering at E_F, symmetric away from it
6. The mechanism is specific to m-type saddle points and general to distorted kagome materials
7. Wavefunction center-of-mass traces a unit cell displacement (charge pumping analog)

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| TB Hamiltonian | $H = \epsilon\sum_i c^\dagger_i c_i - t_1\sum_{\langle ij\rangle} c^\dagger_i c_j - t_2\sum_{\langle\langle ij\rangle\rangle} c^\dagger_i c_j - t_3\sum_{\langle\langle\langle ij\rangle\rangle\rangle} c^\dagger_i c_j - t_4\sum c^\dagger_i c_j$ | Eq. (1) |
| HOvHS dispersion | $\varepsilon(k) = a_x k_x^2 - a_y k_y^2 + b_x k_x^4 - b_y k_y^4 + b_{xy} k_x^2 k_y^2 + \ldots$ with $a_y \to 0$ | Text |
| DOS divergence | $\rho(E) \sim |E|^{-1/4}$ | Fig. 1d |
| HOvHS condition | $a_y(t_1, t_2, t_3, t_4) = 0$ | Text |
| Distortion | $t_1 > t_2$, $t_3 = -t_4$ | Sec. 2 |
| Pomeranchuk order | $O_1(k_x^2 - k_y^2) + O_2(2k_x k_y)$ | Sec. 2 |
| Landau free energy | $F_3 = O_1^2 - 3O_1 O_2^2$ (cubic term) | Sec. 2 |
| Center of mass | $\mathbf{r}_{\text{com}} = \int_{\text{uc}} dr'\, |\Psi(E,r')|^2 r'$ | Text |

## Relevance to Phonon-Exflation

This paper provides the first experimental realization of Pomeranchuk instability at a HOvHS, directly validating the framework's Session 22c prediction that f(0,0) = -4.687 < -3 signals Pomeranchuk instability at the Van Hove singularity of the SU(3) Dirac spectrum. The distorted kagome mechanism (geometric distortion generating HOvHS) maps onto the framework's tau-dependent deformation of the SU(3) fiber, where the fold region may generate analogous HOvHS in the internal spectrum. The nematic cascade without translational symmetry breaking parallels the framework's prediction of K_7-broken but translationally invariant pairing condensate.
