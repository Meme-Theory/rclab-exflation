# Shape Coexistence and Superdeformation in 28Si

**Author(s):** D. Frycz, J. Menendez, A. Rios, A. M. Romero
**Year:** 2023
**Journal:** Proceedings of the XXXVII Mazurian Lakes Conference on Physics
**arXiv:** 2312.00750
**Relevance:** MEDIUM

---

## Abstract

We study the shape coexistence of differently deformed states within $^{28}$Si using shell-model and beyond-mean-field techniques. Experimentally, $^{28}$Si exhibits shape coexistence between an oblate ground state and an excited prolate structure. The oblate rotational band is described well within the sd shell using the USDB interaction. However, for the prolate band, a modification of this interaction is required, lowering the single-particle energy of the $1d_{3/2}$ orbit. Furthermore, we explore the possibility of a superdeformed configuration in $^{28}$Si. Our calculations, spanning both the sd and pf shells, rule out the existence of a superdeformed $0^+$ bandhead within an excitation energy range of 10-20 MeV.

---

## Key Arguments and Derivations

### Introduction (Sec. 1)
Quadrupole deformations are the most common deviations from spherical form in nuclei. Shape coexistence -- diverse shapes at different excitation energies within a single nucleus -- is prevalent throughout the nuclear chart. $^{28}$Si demonstrates shape coexistence with an oblate rotational band built on its ground state, a vibrational bandhead at ~5 MeV, and a prolate rotational band with bandhead at ~6.5 MeV. Previous theoretical studies proposed a superdeformed state at ~14 MeV, but recent experiments have not confirmed this.

### Shell Model Method (Sec. 2)
Naive filling of spherical mean-field levels for $^{28}$Si (14p, 14n) fills the $1d_{5/2}$ orbit completely, giving a spherical Slater determinant. The experimentally oblate ground state requires the sd shell as the valence space with an inert $^{16}$O core and the USDB effective interaction. The Schrodinger equation reduces to diagonalization: $H\Psi = E\Psi$, with $\Psi = \sum_i c_i \Phi_i$ as configuration mixing of Slater determinants.

### Beyond Mean-Field / GCM (Sec. 2)
An alternative uses Hartree-Fock-Bogoliubov (HFB) wavefunctions constrained to deformation parameters $(\beta, \gamma)$:

$$\beta = \frac{4\pi\sqrt{Q_{20}^2 + 2\tilde{Q}_{22}^2}}{3r_0^2 A^{5/3}}, \quad \gamma = \arctan\left(\frac{\sqrt{2}\tilde{Q}_{22}}{Q_{20}}\right)$$

with $r_0 = 1.2$ fm, $\beta = 0$ spherical, $\gamma = 0^\circ$ prolate, $\gamma = 60^\circ$ oblate. Generator Coordinate Method (GCM) performs configuration mixing: $\Psi = \sum_q f(q) \hat{P}^N \hat{P}^Z \hat{P}^J \varphi(q)$, projecting onto good quantum numbers (Z, N, J). Implemented within the Taurus suite.

### Oblate Band (Sec. 3.1)
The projected HFB total energy surface shows a minimum at oblate shape with $\beta \approx 0.25$, consistent with experiment. GCM eigenstates reproduce the oblate rotational band with strong in-band B(E2) transitions and $J(J+1)$ energy spacing. All oblate band states share similar oblate deformation. GCM calculations are in excellent agreement with exact diagonalization (ANTOINE code).

### Prolate Band (Sec. 3.2)
The standard USDB interaction does not reproduce the prolate band: states show weak in-band B(E2) transitions and inconsistent intrinsic deformation. Reducing the $1d_{3/2}$ single-particle energy gap by ~1.5 MeV (USDB-MOD) favors particle promotion from $1d_{5/2}$/$2s_{1/2}$ to $1d_{3/2}$, producing a well-behaved prolate rotational band consistent with experiment while leaving the oblate band largely unaffected.

### Superdeformation (Sec. 3.3)
Including the pf shell with the SDPF-NR interaction, GCM calculations find no superdeformed structures ($\beta \geq 0.5$) within 10-20 MeV excitation energy, disfavoring earlier theoretical predictions and consistent with negative experimental searches.

## Key Results

1. $^{28}$Si ground state is oblate with $\beta \approx 0.25$, well described by USDB in the sd shell
2. Prolate band at ~6.5 MeV requires lowering the $d_{3/2}$ single-particle energy by ~1.5 MeV (USDB-MOD)
3. GCM with symmetry-projected HFB wavefunctions reproduces experimental band structure including B(E2) values
4. No superdeformed $0^+$ bandhead found in 10-20 MeV range when including sd+pf shells (SDPF-NR interaction)
5. The oblate band is insensitive to the $d_{3/2}$ gap modification, demonstrating independence of the two shape configurations
6. Collective wavefunctions confirm consistent deformation within each band (oblate states share deformation; prolate states share deformation only with USDB-MOD)

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Schrodinger equation | $H\Psi = E\Psi$ | Eq. (1) |
| Configuration mixing | $\Psi = \sum_i c_i \Phi_i$ | Eq. (2) |
| Deformation parameter beta | $\beta = \frac{4\pi\sqrt{Q_{20}^2 + 2\tilde{Q}_{22}^2}}{3r_0^2 A^{5/3}}$ | Eq. (3) |
| Triaxiality parameter | $\gamma = \arctan\left(\frac{\sqrt{2}\tilde{Q}_{22}}{Q_{20}}\right)$ | Eq. (3) |
| GCM wavefunction | $\Psi = \sum_q f(q) \hat{P}^N \hat{P}^Z \hat{P}^J \varphi(q)$ | Eq. (4) |

## Relevance to Phonon-Exflation

$^{28}$Si is a neighboring N=Z nucleus to $^{24}$Mg, the analog identified in S38 W2 (Nazarewicz) for the phonon-exflation BCS condensate during the KK fold transit. The oblate-prolate shape coexistence at relatively low excitation energy (~6.5 MeV) demonstrates the general phenomenon of competing deformed minima in sd-shell nuclei. The absence of superdeformation in $^{28}$Si contrasts with the shape coexistence present in $^{24}$Mg, providing a boundary condition: the S38 analog requires a nucleus with accessible shape coexistence at moderate deformation ($\beta \sim 0.3$-$0.5$), which $^{24}$Mg possesses but $^{28}$Si does not extend to the superdeformed regime.
