# Geometry of Quantum Phase Transitions

**Author(s):** Angelo Carollo, Davide Valenti, Bernardo Spagnolo
**Year:** 2020
**Journal:** Physics Reports 838, 1-72 (2020)
**arXiv:** 1911.10196
**Relevance:** CRITICAL

---

## Abstract

In this article we provide a review of geometrical methods employed in the analysis of quantum phase transitions and non-equilibrium dissipative phase transitions. After a pedagogical introduction to geometric phases and geometric information in the characterisation of quantum phase transitions, we describe recent developments of geometrical approaches based on mixed-state generalisation of the Berry-phase, i.e. the Uhlmann geometric phase, for the investigation of non-equilibrium steady-state quantum phase transitions (NESS-QPTs). Equilibrium phase transitions fall invariably into two markedly non-overlapping categories: classical phase transitions and quantum phase transitions, whereas in NESS-QPTs this distinction may fade off. The approach described in this review, among other things, can quantitatively assess the quantum character of such critical phenomena. This framework is applied to a paradigmatic class of lattice Fermion systems with local reservoirs, characterised by Gaussian non-equilibrium steady states.

---

## Key Arguments and Derivations

### Geometric Phase as QPT Detector

The central thesis: quantum phase transitions are accompanied by degeneracies in the ground-state energy density that bend the geometry of the ground-state manifold. Berry curvature singularities at these degeneracy points serve as witnesses of QPTs, without requiring identification of an order parameter or knowledge of symmetry breaking patterns.

Key insight: "Singular curvature and singular metric are two complementary manifestations of the same exceptional behaviour of the quantum state arising across phase transitions." These quantities require no a priori notions of order parameters or symmetry breaking -- only the state's dependence on parameters.

### QGT and Fidelity Susceptibility at Criticality

The quantum geometric tensor (QGT) becomes super-extensive at quantum critical points. The fidelity susceptibility $\chi_F \sim L^{2/\nu}$ diverges with system size $L$ at the critical point, with exponent determined by the correlation length exponent $\nu$. The Berry curvature shows scaling behavior $F^B \sim |\lambda - \lambda_c|^{-\alpha}$ near QPTs.

### XY Model: Geometric Phase and Criticality

For the 1D XY model in transverse field, an excitation gains a nontrivial geometric phase if and only if it circulates a region of criticality. This is traced to conical intersections (degeneracy points) at the XX criticality. The scaling of the geometric phase yields critical exponents characterizing the phase transition.

### Uhlmann Phase for Mixed States and NESS-QPTs

Extension to mixed states via the Uhlmann geometric phase enables investigation of non-equilibrium steady-state QPTs where the distinction between classical and quantum phase transitions may blur. The mean Uhlmann curvature (MUC) marks incompatibility between parameters arising from quantum nature -- a measure of "quantumness" in multi-parameter estimation.

---

## Key Results

1. Berry curvature singularities at degeneracy points serve as order-parameter-free detectors of QPTs.
2. The QGT becomes super-extensive at quantum critical points: $\mathrm{Re}(Q_{\mu\nu}) \sim L^{2/\nu}$.
3. In the XY model, nontrivial geometric phase requires circulating a critical region (topological origin).
4. The Fubini-Study metric (quantum metric) diverges at QPTs, providing a geometric characterization independent of Landau-Ginzburg-Wilson paradigm.
5. The Uhlmann geometric phase extends Berry phase concepts to mixed states and non-equilibrium QPTs.
6. Correlation length divergence $\xi \sim |\lambda-\lambda_c|^{-\nu}$ is the fundamental scale driving QPTs.
7. Energy gap closes as $\Delta \sim J|\lambda-\lambda_c|^{\nu z}$ at the critical point.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Berry connection | $A^B_\mu = i\langle n(\lambda)\|\partial_\mu\|n(\lambda)\rangle$ | Eq. (11) |
| Berry phase | $\phi^B_n(C) = \oint_C A^B$ | Eq. (12) |
| Berry curvature | $F^B_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = \langle\partial_\mu n\|\partial_\nu n\rangle - \langle\partial_\nu n\|\partial_\mu n\rangle$ | Eq. (14) |
| Gap scaling | $\Delta \sim J\|\lambda - \lambda_c\|^{\nu z}$ | Eq. (2) |
| Correlation function | $G(\mathbf{r}-\mathbf{r}') \sim e^{-\|\mathbf{r}-\mathbf{r}'\|/\xi}/\|\mathbf{r}-\mathbf{r}'\|^{d-2+\eta}$ | Eq. (3) |
| Correlation length | $\xi \sim \|\lambda - \lambda_c\|^{-\nu}$ | Eq. (4) |
| Critical time | $\tau_c \sim \Delta^{-1} \propto \xi^z \propto \|\lambda-\lambda_c\|^{-\nu z}$ | Eq. (5) |
| Adiabatic state | $\|\psi(t)_n\rangle \simeq e^{-i\int\epsilon_n d\tau}\,e^{i\phi^B_n(t)}\|n(\lambda(t))\rangle$ | Eq. (7) |
| Fubini-Study metric | $ds^2_\mathrm{FS} = \langle d\psi\|d\psi\rangle - \|\langle\psi\|d\psi\rangle\|^2$ | Sec. 6.1 |
| Fidelity susceptibility | $\chi_F = \lim_{\delta\lambda\to 0}(-2\ln F)/\delta\lambda^2$ | Sec. 6.3 |

---

## Relevance to Phonon-Exflation

This paper provides the theoretical foundation for using Berry curvature singularities to detect and characterize the framework's BCS quantum phase transition at $S_\mathrm{inst} = 0.069$. The key result -- that the QGT becomes super-extensive at critical points with scaling governed by $\nu$ -- directly applies to the framework's transit physics, where the instanton parameter $s$ drives a QPT. The paper's demonstration that geometric phases detect QPTs without requiring order parameters or symmetry-breaking knowledge validates the framework's use of geometric quantities (quantum metric $g = 982.5$) as primary diagnostic tools. The connection between Berry curvature singularities and energy gap closure ($\Delta \sim |\lambda - \lambda_c|^{\nu z}$) maps directly to the BCS gap structure at the framework's transit point.
