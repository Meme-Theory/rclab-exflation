# Quantum phase transition for the BEC-BCS crossover in condensed matter physics and CPT violation in elementary particle physics

**Author(s):** F.R. Klinkhamer, G.E. Volovik
**Year:** 2004
**Journal:** JETP Letters 80, 343 (2004)
**arXiv:** cond-mat/0407597
**Relevance:** HIGH

---

## Abstract

We discuss the quantum phase transition that separates a vacuum state with fully-gapped fermion spectrum from a vacuum state with topologically-protected Fermi points (gap nodes). In the context of condensed-matter physics, such a quantum phase transition with Fermi point splitting may occur for a system of ultracold fermionic atoms in the region of the BEC-BCS crossover, provided Cooper pairing occurs in the non-s-wave channel. For elementary particle physics, the splitting of Fermi points may lead to CPT violation, neutrino oscillations, and other phenomena.

---

## Key Arguments and Derivations

### Two Classification Schemes

The paper contrasts classification by symmetry (symmetry group H subgroup of G, thermodynamic transitions) with classification by universality classes (momentum-space topology at T=0). A quantum phase transition between universality classes occurs WITHOUT changing symmetry group H.

### BEC-BCS Quantum Phase Transition

For p-wave spin-triplet pairing with Bogoliubov-Nambu Hamiltonian:

H = ((|p|^2/2m - q, c_perp p . (e_1-hat + i e_2-hat)); (c_perp p . (e_1-hat - i e_2-hat), -|p|^2/2m + q))

The energy spectrum is E^2(p) = (|p|^2/2m - q)^2 + c_perp^2 (p x l-hat)^2.

- q > 0 (BCS regime): two Fermi points at p_{1,2} = +/- p_F l-hat with p_F = sqrt(2mq)
- q < 0 (BEC regime): fully gapped spectrum
- q = 0 (critical point): marginal Fermi point with N = 0

The topological charge N_a is given by the surface integral:

N_a = (1/24 pi^2) epsilon_{mu nu rho sigma} tr oint_{Sigma_a} dS_sigma G (partial/partial p_mu) G^{-1} G (partial/partial p_nu) G^{-1} G (partial/partial p_rho) G^{-1}

### CPT Violation and Fermi Point Splitting

For Dirac fermions with CPT violation:

H = (sigma . (p - b), M; M, -sigma . (p + b))

The spectrum E^2_pm = M^2 + |p|^2 + q^2 +/- 2q sqrt(M^2 + (p . b-hat)^2) with q = |b|.

Quantum phase transition at q_c = M: for q > M, two Fermi points at p_{1,2} = +/- b-hat sqrt(q^2 - M^2). The splitting magnitude is 2 sqrt(q^2 - M^2).

### Alpha-Phase: Cubic Fermi Point Structure

The alpha-phase of spin-triplet superfluid has the Hamiltonian with Sigma . p = sigma_x p_x + exp(2pi i/3) sigma_y p_y + exp(-2pi i/3) sigma_z p_z. On the BCS side, EIGHT Fermi points at vertices of a cube in momentum space. The four right-handed Weyl points: p_F(+x-hat +/- y-hat +/- z-hat)/sqrt(3) and permutations.

### Chern-Simons Term from Fermi Point Splitting

The WZNW term summed over Fermi points gives:

S_WZNW = (12 pi^2)^{-1} sum_a N_a integral d^3x dt d tau p_a . (partial_tau p_a x partial_t p_a)

This generates a CPT-violating Chern-Simons-like action:

S_CS = integral d^4x k_mu epsilon^{mu nu rho sigma} A_nu partial_rho A_sigma

with k = (e^2/12 pi^2) theta(q-M) b-hat sqrt(q^2 - M^2).

The Chern-Simons vector k is zero for the antiferromagnetic alpha-phase (cubic arrangement), but may give neutrino oscillations.

---

## Key Results

1. Quantum phase transition between fully-gapped (BEC) and Fermi-point (BCS) vacua at q_c = 0
2. The transition is purely topological: marginal Fermi point (N=0) splits into topological ones (N=+/-1)
3. For Dirac fermions with CPT violation, critical parameter q_c = M
4. The alpha-phase has 8 Fermi points at cube vertices (antiferromagnetic arrangement)
5. Fermi point splitting generates Chern-Simons-like CPT-violating terms
6. The CS coefficient is determined by topology and is unambiguous (unlike standard regularization)
7. Antiferromagnetic splitting may produce neutrino oscillations without CS term

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| BN Hamiltonian (p-wave) | $H = \begin{pmatrix} \|\mathbf{p}\|^2/2m - q & c_\perp\mathbf{p}\cdot(\hat{e}_1 + i\hat{e}_2) \\ c_\perp\mathbf{p}\cdot(\hat{e}_1 - i\hat{e}_2) & -\|\mathbf{p}\|^2/2m + q \end{pmatrix}$ | Eq.(1) |
| Spectrum | $E^2(\mathbf{p}) = \left(\frac{\|\mathbf{p}\|^2}{2m} - q\right)^2 + c_\perp^2(\mathbf{p}\times\hat{l})^2$ | Eq.(2) |
| Topological invariant | $N_a = \frac{1}{24\pi^2}\epsilon^{\mu\nu\rho\sigma}\text{tr}\oint_{\Sigma_a} dS_\sigma\, G\partial_\mu G^{-1}G\partial_\nu G^{-1}G\partial_\rho G^{-1}$ | Eq.(3) |
| Dirac CPT Hamiltonian | $H = \begin{pmatrix}\boldsymbol{\sigma}\cdot(\mathbf{p}-\mathbf{b}) & M \\ M & -\boldsymbol{\sigma}\cdot(\mathbf{p}+\mathbf{b})\end{pmatrix}$ | Eq.(6) |
| CPT spectrum | $E_\pm^2 = M^2 + \|\mathbf{p}\|^2 + q^2 \pm 2q\sqrt{M^2 + (\mathbf{p}\cdot\hat{b})^2}$ | Eq.(7) |
| Split Fermi points | $\mathbf{p}_{1,2} = \pm\hat{b}\sqrt{q^2 - M^2}$ | Eq.(8) |
| WZNW term | $S_{\text{WZNW}} = \frac{1}{12\pi^2}\sum_a N_a\int d^3x\,dt\,d\tau\;\mathbf{p}_a\cdot(\partial_\tau\mathbf{p}_a\times\partial_t\mathbf{p}_a)$ | Eq.(11) |
| CS-like action | $S_{\text{CS}} = \int d^4x\;k_\mu\epsilon^{\mu\nu\rho\sigma}A_\nu\partial_\rho A_\sigma$ | Eq.(15) |
| CS vector | $\mathbf{k} = \frac{e^2}{12\pi^2}\theta(q-M)\hat{b}\sqrt{q^2-M^2}$ | Eq.(17) |

---

## Relevance to Phonon-Exflation

1. **BEC-BCS crossover and the fold**: The quantum phase transition at q_c between fully-gapped and Fermi-point states is the direct analog of the framework's fold transition at the critical tau value. The framework's BCS instability at the fold (Session 35: any g>0 flows to strong coupling) is the 1D version of this topological quantum phase transition.

2. **Topological invariant and D_K spectrum**: The Fermi-point invariant N_a computed from the Green's function is the analog of the framework's topological invariants computed from D_K. The framework's BDI class with T^2=+1 and sgn(Pf) = -1 at all tau are the SU(3) fiber versions of this topology.

3. **Alpha-phase cube of Fermi points**: The 8 Fermi points at cube vertices in the alpha-phase bear structural resemblance to the framework's discrete symmetry patterns in the D_K spectrum on SU(3). The antiferromagnetic arrangement (zero total topological charge) parallels the framework's cancellation of chiral charges.

4. **CPT and discrete symmetries**: The paper's analysis of how CPT violation splits marginal Fermi points connects to the framework's [iK_7, D_K] = 0 result and the Jensen breaking of SU(3) to U(1)_7. The splitting mechanism is a possible route for generating neutrino mass in the framework.
