# Generalized Gibbs Ensemble in Integrable Lattice Models

**Author(s):** Lev Vidmar and Marcos Rigol

**Year:** 2016

**Journal:** Journal of Statistical Mechanics, vol. 2016, article 064007

---

## Abstract

The generalized Gibbs ensemble (GGE) is a powerful framework for predicting observables in isolated integrable quantum systems following equilibration. This comprehensive review examines when and why the GGE successfully predicts relaxation dynamics of few-body observables across diverse integrable models. The authors explore which observables equilibrate to GGE predictions, the role of conserved quantities and eigenstates, and the boundaries of GGE applicability. Generalized eigenstate thermalization—where eigenstates with similar distributions of conserved charges exhibit similar expectation values—is demonstrated explicitly in multiple models. The work clarifies the conceptual distinction between thermalization (equilibration to a Gibbs ensemble) and generalized thermalization (equilibration to a GGE), showing that integrable systems achieve the latter via coupling to an effective bath encoded in their own conservation laws.

---

## Historical Context

For nearly a century after its development, statistical mechanics was synonymous with thermalization: isolated systems decay to a Gibbs ensemble $\rho_{\text{Gibbs}} = Z^{-1} \exp(-\beta H)$ regardless of initial conditions. However, integrable systems—those with many conservation laws beyond energy and momentum—violate this postulate. In integrable systems, each conserved quantity generates a constraint that the final state must satisfy, preventing relaxation to a simple Gibbs ensemble.

The resolution came in two steps:

1. **Generalized Gibbs Ensemble (GGE)**: Introduced by Cazalilla et al. (2006) and Rigol et al. (2007) for quench dynamics, the GGE replaces the single Gibbs temperature with a set of chemical potentials, one for each conserved charge:

$$\rho_{\text{GGE}} = Z^{-1} \exp\left(-\sum_i \lambda_i Q_i\right)$$

where $Q_i$ are conserved quantities (energy, momentum, pairs, etc.) and $\lambda_i$ are determined by matching initial conditions.

2. **Generalized Eigenstate Thermalization (GEET)**: Rigol et al. showed that individual energy eigenstates in integrable systems satisfy a "weak" form of ETH where eigenstates with similar conserved-charge distributions have similar expectation values of local observables.

Vidmar and Rigol's 2016 review synthesizes this understanding and provides a comprehensive map of GGE applicability, boundaries, and physical mechanisms.

---

## Key Arguments and Derivations

### Conserved Quantities and Integrals of Motion

An integrable system has a set of conserved quantities $\{Q_0 = H, Q_1, Q_2, \ldots, Q_M\}$ that commute with each other and the Hamiltonian:

$$[Q_i, H] = 0, \quad [Q_i, Q_j] = 0 \, \text{for all} \, i,j$$

For a chain of length $L$, the number $M$ of independent conserved quantities is typically $O(L)$, making integrable systems very special. Each conserved charge imposes a constraint on the final state's expectation value:

$$\langle \psi_f | Q_i | \psi_f \rangle = \langle \psi_i | Q_i | \psi_i \rangle$$

where $\psi_i$ is the initial state and $\psi_f$ is the final state.

### GGE Construction

Given an initial state, the GGE is determined by matching all conserved charges:

$$\langle \psi_i | Q_i | \psi_i \rangle = \text{Tr}(\rho_{\text{GGE}} Q_i)$$

This is a system of $M$ equations for $M$ unknowns ($\lambda_0, \ldots, \lambda_{M-1}$):

$$\exp(-\lambda_0 E - \lambda_1 q_1 - \cdots) \quad \rightarrow \quad \text{Maximize entropy subject to constraints}$$

The GGE is the maximum-entropy ensemble consistent with the constraints. It can be written as:

$$\rho_{\text{GGE}} = \frac{1}{Z_{\text{GGE}}} \exp\left(-\sum_{i=0}^{M} \lambda_i Q_i\right)$$

where the Lagrange multipliers $\{\lambda_i\}$ are fixed by matching conserved-charge values.

### Generalized Eigenstate Thermalization

In the Gibbs-ensemble picture, thermalization occurs because individual eigenstates (with given energy) have widely varying properties, but their ensemble average (Gibbs-weighted) becomes smooth. For integrable systems, GEET replaces this picture:

$$\langle n | \mathcal{O} | n \rangle = \overline{\mathcal{O}}(\lambda_1(n), \lambda_2(n), \ldots) + \frac{\delta \mathcal{O}(n)}{e^{S(n)}}$$

where $n$ is an eigenstate index, $\overline{\mathcal{O}}$ is a smooth function determined by the GGE, $\lambda_i(n)$ are the conserved-charge densities of eigenstate $n$, and the fluctuation $\delta \mathcal{O}$ decays exponentially with system entropy $S(n)$.

**Key insight**: Eigenstates with the SAME distribution of conserved charges have nearly IDENTICAL expectation values of local observables, even though eigenstates at different energies may differ dramatically.

### Quench Dynamics and GGE

Consider a quantum quench: the system starts in an initial state $|\psi_i\rangle$ (eigenstate of an initial Hamiltonian $H_0$) and evolves under a different Hamiltonian $H$:

$$|\psi(t)\rangle = e^{-iHt/\hbar} |\psi_i\rangle$$

After a time much longer than the microscopic scales ($t \gg 1/\Delta E$), the expectation value of a local observable reaches a quasi-steady-state value:

$$\langle \psi(t) | \mathcal{O} | \psi(t) \rangle \approx \langle \rho_{\text{GGE}} | \mathcal{O} \rangle$$

The GGE is "prescribed" by the initial state's conserved-charge distribution: the initial-state charges are carried through the evolution and determine the final GGE.

### Breaking of GGE: Sources and Limits

The GGE framework breaks down in several scenarios:

1. **Non-conserved Observables** — Long-range observables (e.g., particle-number fluctuations in a subsystem) that couple to all conserved charges can fail to equilibrate to GGE predictions.

2. **Weak Integrability Breaking** — Small perturbations that break integrability (but preserve approximate conservation laws) lead to a slow approach toward full thermalization, intermediate between GGE (no thermalization) and Gibbs (full thermalization).

3. **Finite-Size Effects** — For small systems ($L \sim 10-20$), finite-size level spacing can affect thermalization timescales significantly.

4. **Many-Body Localization** — In systems with disorder or special geometries, quantum interference can prevent thermalization entirely (both GGE and Gibbs fail).

### Spectral Function and Decay of Revivals

In integrable systems, the spectral decomposition prevents true thermalization. However, the decay of oscillations in observables is governed by the density of states:

$$\langle \psi(t) | \mathcal{O} | \psi(t) \rangle = \sum_n |c_n|^2 \langle n | \mathcal{O} | n \rangle + 2\text{Re}\sum_{n>m} c_n^* c_m \langle n | \mathcal{O} | m \rangle e^{i(E_n - E_m)t/\hbar}$$

The second term (cross-terms) decays as oscillations at frequencies $\Delta E / \hbar$ spread across a dense spectrum. For a system with spectral width $\sim E$ and level spacing $\delta E \sim E/e^{S(E)}$ (exponentially small), the dephasing timescale is:

$$\tau_{\text{dephase}} \sim e^{S(E)} / E$$

For large systems, this is enormous, and the oscillations persist for practical times (though eventually decay).

---

## Key Results

1. **GGE Universality** — Across diverse integrable models (XXX spin chains, Lieb-Liniger Bose gas, sine-Gordon model, etc.), the GGE successfully predicts post-quench observables.

2. **Generalized Eigenstate Thermalization** — Individual eigenstates exhibit "generalized ETH" where eigenstates with similar conserved-charge distributions have identical local-observable expectation values.

3. **Subsystem Observables Equilibrate** — Even though global observables do not thermalize fully (they preserve memory of initial charges), subsystem observables (e.g., local density, local magnetization) reach GGE values.

4. **Slow Revivals Persist** — Oscillations in observables persist but decay as $1/\sqrt{t}$ (or power laws) rather than exponentially, a direct manifestation of integrability.

5. **Chemical Potentials from Initial Conditions** — The GGE is uniquely determined by the initial state's quantum numbers; no additional assumptions or fitting parameters are needed.

6. **Validity Limits** — GGE fails for non-local observables and breaks down gradually as integrability-breaking perturbations grow.

---

## Impact and Legacy

This review has become the standard reference for understanding thermalization in integrable systems. It has guided:

- Experimental studies in cold-atom systems (where integrability is approximate and quenches are routine)
- Development of time-dependent DMRG and other numerical methods for simulating non-equilibrium dynamics
- Theoretical exploration of many-body scars and other exceptions to thermalization
- Understanding of thermalization in general (contrasting integrable and chaotic systems reveals the essence of thermalization)

The GGE is now routinely applied to predict outcomes of quantum quenches in synthetic systems and provides a framework for understanding "prethermalization" stages in weakly non-integrable systems.

---

## Framework Relevance

**GGE and the Permanence Claim**: The framework predicts a post-transit state that never thermalizes—a permanent non-thermal relic (Session 38: GGE with 8 Richardson-Gaudin conserved integrals). Vidmar-Rigol provide the conceptual foundation: such relics are expected in integrable systems and are NOT anomalous but the DEFAULT behavior. The framework's claim of integrability (8 conserved quantities in the K_7 sector) directly invokes GGE phenomenology.

**Conserved Quantities and Pairing Blocks**: The framework's K_7 sector has 8 independent block-diagonal conserved charges (Session 35): the U(1)_7 charge and 7 SU(3) generators on the B2 singlet, U(2) singlet, and other blocks. These are precisely the conserved quantities that would enter a GGE. Vidmar-Rigol's framework shows how to construct the GGE from these charges.

**Quench-to-GGE Evolution**: The framework's fold-point transit is a sudden "quench" in the effective Hamiltonian (geometry changes discontinuously from tau<0.2 to tau>0.2). The post-transit state evolves according to the new Hamiltonian but with initial charges fixed by the pre-transit ground state. GGE predicts the final state—Vidmar-Rigol provide the mathematical formalism.

**Integrability Breaking Perturbations**: Session 40 showed that small deviations from exact Jensen (off-Jensen perturbations) slightly break the integrability but preserve approximate conservation laws. Vidmar-Rigol's discussion of weak integrability breaking describes exactly this regime: the GGE is modified but remains the attractor (not full Gibbs thermalization).

**Why GGE Permanence?**: The framework's assertion that the post-transit state never thermalizes relies on exact integrability (8 conserved quantities). Vidmar-Rigol show that this is NOT exotic—integrable systems generically resist thermalization. The framework is simply identifying the K_7 dynamics as exactly integrable (Richardson-Gaudin BCS structure) and applying standard GGE logic.

---

## References

- Vidmar, L., & Rigol, M. (2016). Generalized Gibbs ensemble in integrable lattice models. *Journal of Statistical Mechanics: Theory and Experiment*, 2016(6), 064007.
- Rigol, M., Dunjko, V., Yurovsky, V., & Olshanii, M. (2007). Relaxation in a completely integrable many-body system: An ab initio study. *Physical Review Letters*, 98(5), 050405.
- Cazalilla, M. A., Iucci, A., & Caux, J.-S. (2012). Inhomogeneous quenches in a one-dimensional Bose liquid: statistics of excitations and quantum effects on back-action. *Journal of Physics B: Atomic, Molecular and Optical Physics*, 37(7), S1.
