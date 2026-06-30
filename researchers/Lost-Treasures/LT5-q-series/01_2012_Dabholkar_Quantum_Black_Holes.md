# Quantum Black Holes, Wall Crossing, and Mock Modular Forms

**Authors:** Atish Dabholkar, Sameer Murthy, Don Zagier

**Year:** 2012

**arXiv:** 1208.4074

---

## Abstract

This seminal work establishes a deep connection between quantum black hole partition functions and mock modular forms—two mathematical structures previously thought unrelated. The paper demonstrates that the meromorphic Jacobi form counting quarter-BPS states in N=4 string theories can be decomposed into a sum of a mock Jacobi form (whose coefficients are the quantum degeneracies of single-centered black holes) and an Appell-Lerch sum (capturing multi-centered black hole degeneracies subject to wall-crossing decay). This decomposition reveals that while the full partition function is a modular form, the "physical" part corresponding to single-centered black holes is a mock modular form with a holomorphic anomaly reflecting the non-compactness of the microscopic CFT.

---

## Historical Context

The connection between black hole entropy and quantum degeneracies has been a cornerstone of string theory since Bekenstein and Hawking's foundational work. In N=4 superstring theory, BPS black holes provide a microscopic statistical explanation of black hole thermodynamics: the entropy S = A/(4G) should equal the logarithm of the number of quantum microstates.

String theory calculations (via localization and various exact methods) show that the generating function for the number of quarter-BPS black hole microstates is a modular form in the charges and asymptotic moduli. However, this modular form receives contributions from both single-centered black holes (the "physical" degeneracies) and multi-centered configurations that decay upon wall-crossing, and this decomposition was mysterious.

Simultaneously, in pure mathematics, Ramanujan's mock theta functions—studied by Rogers, Watson, and others—were finally explained by Zwegers (2002) as "non-holomorphic modular forms" or mock modular forms: functions that are almost modular, differing from a true modular form by a holomorphic anomaly term. These mathematical objects seemed abstract until Dabholkar, Murthy, and Zagier showed that they naturally appear in black hole partition functions.

This breakthrough demonstrates that mock modularity is not a mathematical curiosity but a fundamental feature of quantum gravity counting, opening a vast landscape of new examples in mathematics via string theory.

---

## Key Arguments and Derivations

### 1. Black Hole Partition Functions and Jacobi Forms

In N=4 string theory (or more generally, string theory on Calabi-Yau manifolds with 16 supercharges), the partition function counting BPS states with quantum numbers (p,q,n) is:

$$\Phi(t,\bar{t}, \tau) = \sum_{p,q,n} c(p,q,n) \, q^n \, y^p \, z^q$$

where q = exp(2πiτ), y and z encode other modular parameters, and c(p,q,n) are the Fourier coefficients—literally the number of quantum microstates.

For quarter-BPS states at fixed charges (p,q), the degeneracy function is:

$$\Psi(p,q,\tau) = \sum_n c(p,q,n) q^n$$

In the weakly-coupled regime (large volume), localization techniques show that Psi is a Jacobi form of weight -1/2 and index (p+q)/2 (or with appropriate weights in different settings).

A meromorphic Jacobi form satisfies:

$$\Psi\left( \frac{a\tau + b}{c\tau + d}, \frac{z}{c\tau + d} \right) = (c\tau + d)^k \exp\left( \frac{\pi i c z^2}{c\tau + d} \right) \Psi(\tau, z)$$

for all $(a,b,c,d) \in SL(2,\mathbb{Z})$, with weight k.

### 2. Wall-Crossing and Multi-Centered Black Holes

In string theory, black holes can form bound states of multiple simpler black holes. The "wall of marginal stability" is a locus in moduli space where the binding energy of a multi-centered configuration vanishes, and the bound state can decay.

As one moves through moduli space, the spectrum of BPS bound states changes discontinuously across the wall. The wall-crossing formula (due to Denef, Moore, Kontsevich-Soibelman, and others) expresses the change in the index (counting BPS states with sign) as:

$$\Delta \Psi = \text{(residue at wall)} = \text{sum over decay channels}$$

Crucially, the wall-crossing formula shows that the change in degeneracies of single-centered black holes equals the number of multi-centered configurations that decay through the wall. This is encoded in the Appell-Lerch sum.

### 3. Decomposition into Mock and Appell-Lerch Parts

The central theorem is:

**The meromorphic Jacobi form Psi decomposes as:**

$$\Psi(\tau, z) = \hat{\Psi}^{mock}(\tau, z) + \text{Appell-Lerch}(\tau, z)$$

where:

- **Mock Jacobi form** $\hat{\Psi}^{mock}$: Has Fourier coefficients that are the **single-centered black hole degeneracies**. It is NOT fully modular but satisfies a non-holomorphic modularity relation.

- **Appell-Lerch sum**: Captures the contributions of multi-centered black holes. These terms are meromorphic but not modular by themselves; their non-modularity exactly cancels the non-modularity of the mock form.

The explicit formula for the completion (the function that makes the mock part fully modular) involves non-holomorphic Eisenstein series:

$$\Psi^{comp}(\tau, z) = \hat{\Psi}^{mock}(\tau, z) + \int_{\infty}^{i\infty} g(\tau, z; s) \, ds$$

where g is an integration kernel involving error functions and Eisenstein series, reflecting the fact that the microscopic CFT is non-compact (contributions from infinitely many wrapped branes).

### 4. Holomorphic Anomaly and AdS3/CFT2

From the perspective of AdS3/CFT2 holography (the "MSW black strings"), the partition function should transform as a modular form under the modular group of the boundary torus. However, the single-centered black hole partition function is only a mock modular form.

This holomorphic anomaly (the non-holomorphic completion term) can be interpreted in several ways:

1. **Microscopic CFT perspective**: The non-compactness of the CFT (due to the AdS2 throat) introduces a continuous spectrum of states, contributing a non-holomorphic piece.

2. **Macroscopic gravity perspective**: Quantum corrections from supergravity fluctuations in AdS2 introduce non-holomorphic terms.

3. **Wall-crossing perspective**: The anomaly precisely accounts for the fact that multi-centered black holes exist off the main branch and contribute a continuous swath of states.

### 5. Connection to Ramanujan's q-Series

The Appell-Lerch sum generalizes classical q-series identities studied by Ramanujan:

$$A(q, y) = \sum_{n \in \mathbb{Z}} (-1)^n y^{3n(n+1)/2} q^{n(n+1)/2}$$

More generally, Appell-Lerch sums have the form:

$$\text{AL}(q,z) = \sum_{m,n} (-1)^m q^{m(m+1)/2} z^m \ldots$$

These functions, while not modular, have quasi-modular properties and can be expressed as differences of theta functions and theta functions integrated with Eisenstein series—precisely the structure that Zwegers used to define mock modular forms.

### 6. Generating Function Perspective for BCS Analogy

While the 2012 Dabholkar-Murthy-Zagier paper focuses on black holes, the mathematical structure suggests a parallel: if one writes a partition function for a pairing system as:

$$Z(q) = \sum_N d(N) q^N$$

where d(N) is the degeneracy at particle number N, then similar decompositions may apply if the system has "multi-centered" excitations (e.g., pairs that decouple into independent pairs at large separation, analogous to multi-centered black hole decay).

The question becomes: **Is the BCS partition function, summed over particle number with q = exp(-β μ), a mock modular or quasi-modular form?** The wall-crossing mechanism (pair binding/decay) is analogous to the BCS pairing instability.

---

## Key Results

1. **Mock Jacobi Form Decomposition**: The partition function of quarter-BPS black holes in N=4 string theory is a sum of a mock Jacobi form (single-centered) and an Appell-Lerch sum (multi-centered).

2. **Holomorphic Anomaly**: The single-centered black hole partition function $\hat{\Psi}^{mock}$ is NOT modular; its failure to be modular is captured by a non-holomorphic anomaly term—this is the defining property of mock modular forms.

3. **Infinite Examples**: This result generates infinitely many new examples of mock modular forms in mathematics, not previously known, by exploiting the landscape of string theory compactifications.

4. **Wall-Crossing Theorem Reformulation**: The mathematical essence of wall-crossing is the decomposition of a modular generating function into modular and non-modular (mock) parts.

5. **AdS3/CFT2 Consistency**: The holomorphic anomaly is consistent with the non-compactness of the microscopic CFT in AdS2/CFT1.

---

## Impact and Legacy

This paper has become a cornerstone connecting physics and mathematics:

- **Mathematical physics**: It provides hundreds of new examples of mock modular forms via string compactifications, enriching the mathematical landscape beyond Ramanujan's classical theta functions.

- **Quantum gravity**: It reveals a deep structure in black hole partition functions that any theory of quantum gravity must respect, and provides tools for computing black hole entropy in complex regimes (wrapped branes, multi-centered configurations).

- **String theory**: Wall-crossing formulas and modular properties now constrain the spectrum and degeneracies in string compactifications.

- **Representation theory**: The connection has led to applications in affine Hecke algebras and quantum groups.

Follow-up work by Dabholkar, Gomes, and Murthy (2015) on "Nonperturbative black hole entropy and Kloosterman sums" extended these results to non-BPS black holes, showing that even more exotic modular structures (involving Kloosterman sums) emerge.

---

## Connection to Phonon-Exflation Framework

**Tentative connection**: The BCS pairing model in phonon-exflation is a finite system with N particles and internal symmetries (particle-number conservation broken by pairing). If the grand-canonical partition function Z(q) = Σ_N Z_N(T) q^N (where q = exp(μ/T)) is reinterpreted as a formal q-series, then the question arises:

**Does Z(q) exhibit modular or mock-modular properties?**

The framework's mechanism involves BCS condensation at zero temperature and a thermal transition at finite T. If this transition is analogous to a "wall-crossing" in the q-series structure (condensate forms ↔ pairs decouple), then mock modular structure might encode:

- The finite-temperature phase transition (manifest in the holomorphic anomaly)
- The relic GGE partition (mock vs. true modular parts decompose physical vs. unphysical regimes)
- The integrable structure (conserved charges → quasi-modular deformations)

**Status**: No direct literature yet applies mock modular forms to BCS pairing. This is an open avenue connecting q-series mathematics to the framework's partition function.

---

## References

- Dabholkar, A., Murthy, S., Zagier, D. (2012). Quantum Black Holes, Wall Crossing, and Mock Modular Forms. arXiv:1208.4074
- Zwegers, S. (2002). Mock Theta Functions. Ph.D. thesis, University of Utrecht
- Kontsevich, M., Soibelman, Y. (2010). Stability structures, motivic Donaldson-Thomas invariants and cluster transformations. arXiv:0811.2435
