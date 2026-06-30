# A beginner's guide to the modern theory of polarization

**Author(s):** Nicola A. Spaldin
**Year:** 2012
**Journal:** Journal of Solid State Chemistry 195, 2-10 (2012)
**arXiv:** 1202.1831
**Relevance:** MEDIUM

---

## Abstract

[INCOMPLETE - not extractable from PDF in allocated reading. The paper provides a pedagogical introduction to the modern theory of electric polarization, explaining how polarization is formulated as a Berry phase of the electronic wavefunctions rather than as a simple dipole moment of the charge distribution.]

---

## Key Arguments and Derivations

The paper explains why the classical definition of polarization as dipole moment per unit volume fails for extended crystalline systems (the "polarization paradox"), and how the Berry phase formulation resolves this:

- **Classical failure:** Bulk polarization cannot be determined from the periodic charge density -- it depends on the choice of unit cell.
- **Berry phase resolution:** Polarization is expressed as a Berry phase (Zak phase) across the Brillouin zone: $\mathbf{P} = \frac{e}{(2\pi)^3}\sum_n\int_\mathrm{BZ} d\mathbf{k}\,\langle u_{n\mathbf{k}}|i\nabla_\mathbf{k}|u_{n\mathbf{k}}\rangle$.
- **Only changes matter:** The polarization itself is defined modulo a "quantum of polarization" $eR/V$ (lattice vector). Only changes in polarization (e.g., between centrosymmetric and distorted structures) are physical observables.
- **Connection to experiment:** Polarization change = integrated current during adiabatic switching. This is measurable via pyroelectric or switching current measurements.
- **Wannier function picture:** Polarization equals the sum of Wannier center positions, providing an intuitive real-space interpretation of the Berry phase formula.

---

## Key Results

1. Bulk polarization of a crystal is a Berry phase, not a simple expectation value.
2. Only polarization differences are physically meaningful (defined mod $eR/V$).
3. The Berry phase formula $\mathbf{P} = (e/(2\pi)^3)\sum_n\int_\mathrm{BZ}\langle u_n|i\nabla_\mathbf{k}|u_n\rangle\,d\mathbf{k}$ is now standard in first-principles calculations.
4. Zak's phase (Berry phase across BZ) is quantized to 0 or $\pi$ with inversion symmetry.
5. Wannier center interpretation: polarization = sum of electronic Wannier centers + ionic positions.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Berry phase polarization | $\mathbf{P}_\mathrm{el} = \frac{e}{(2\pi)^3}\sum_n\int_\mathrm{BZ} d\mathbf{k}\,\langle u_{n\mathbf{k}}\|i\nabla_\mathbf{k}\|u_{n\mathbf{k}}\rangle$ | King-Smith & Vanderbilt |
| Quantum of polarization | $\Delta P = eR/V$ (indeterminacy by lattice vectors) | Resta formulation |
| Zak phase | $\gamma_n = \int_\mathrm{BZ} dk\,\langle u_n\|i\partial_k\|u_n\rangle$ | 1D Berry phase |
| Adiabatic current | $j = -\sum_n\int_\mathrm{BZ}(dq/2\pi)\Omega^n_{qt}$ | Thouless pump |
| Wannier center | $\bar{x}_n = \frac{a}{2\pi}\gamma_n$ | Real-space interpretation |

---

## Relevance to Phonon-Exflation

This paper explains how Berry phases produce measurable macroscopic consequences (electric polarization) even when Berry curvature is small or zero -- directly relevant to the framework where $\mathrm{Im}(T) = 0$ but the system may still exhibit measurable geometric effects through the quantum metric channel. The polarization-as-Berry-phase framework demonstrates that geometric quantities of Bloch wavefunctions have observable bulk consequences, validating the framework's approach of treating the QGT as a primary physical quantity.
