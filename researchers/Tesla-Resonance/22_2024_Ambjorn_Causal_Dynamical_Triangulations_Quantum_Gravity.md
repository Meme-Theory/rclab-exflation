# Causal Dynamical Triangulations: Gateway to Nonperturbative Quantum Gravity

**Authors:** Jan Ambjørn, Renate Loll

**Year:** 2024

**Journal:** arXiv (review)

**Identifier:** arXiv:2401.09399

---

## Abstract

Causal Dynamical Triangulations (CDT) is a nonperturbative, background-independent formulation of quantum gravity constructed via the path integral on dynamical lattices. The framework implements Lorentzian signature quantum gravity by carefully preserving causality at the lattice level—a key distinction from earlier Euclidean approaches. The 2024 review documents how CDT achieves concrete, measurable predictions on the spectra of diffeomorphism-invariant quantum observables at the Planck scale, including the emergence of a de Sitter-like quantum universe and the discovery of an anomalous spectral dimension that flows from 4 at infrared scales to approximately 1.8 near the Planck cutoff.

---

## Historical Context

Quantizing gravity while preserving background independence has been a fundamental challenge for 80+ years. String theory sidesteps the issue by embedding gravity in higher dimensions. Loop quantum gravity uses canonical quantization with geometric operators. Asymptotic safety proposes that gravity flows to a non-trivial fixed point under renormalization group flow.

CDT, initiated by Ambjørn, Jurkiewicz, and Loll in the 1990s, took a different path: lattice regularization using dynamical triangulations—random triangulations whose connectivity changes during the path integral sum. The critical innovation was imposing a causal structure: each triangle is labeled with a "time step," enforcing that the triangulation respects a foliation into spacelike hypersurfaces.

This causal constraint resolves a catastrophic problem that plagued earlier Euclidean triangulation schemes: the phase structure of Euclidean gravity diverges pathologically, and you cannot reliably extract 4D continuum behavior. By enforcing Lorentzian causality, CDT avoids this pathology and demonstrates that continuum 4D spacetime emerges naturally from the lattice path integral at large length scales.

The 2024 Ambjørn-Loll review synthesizes 25 years of developments, emphasizing new results on the spectral dimension flow—a diagnostic of fundamental spacetime structure at the Planck scale.

---

## Key Arguments and Derivations

### Path Integral Formulation on Dynamical Lattices

The partition function in CDT is:

$$Z = \sum_{\text{triangulations}} \frac{1}{C(T)} (-\kappa_0)^{N_4} e^{-S_\text{Regge}[T]}$$

where:
- The sum runs over all causal triangulations $T$
- $N_4$ is the number of 4-simplices (the fundamental building blocks)
- $S_\text{Regge}[T]$ is the regge action—a discretized Einstein-Hilbert action computed from edge lengths and dihedral angles
- $\kappa_0$ is the coupling controlling the vacuum energy density
- $C(T)$ accounts for symmetries

The Regge action is:

$$S_\text{Regge} = \sum_{\text{hinges}} \theta_h (\ell) \cdot A_h$$

where $\theta_h(\ell)$ is the deficit angle at each hinge (edge), depending on edge lengths $\ell$, and $A_h$ is the dual area.

### Causality Constraint and Foliation

Unlike Euclidean triangulation schemes, CDT imposes that each simplex carries a "time label" $t \in \{0, 1, ..., T_\text{max}\}$. All edges are either:

- **Timelike**: connect simplices at time $t$ to time $t+1$
- **Spacelike**: connect simplices within the same time $t$

This foliation constraint ensures:

$$g_{00} = -1 \quad (\text{ADM gauge, approximately enforced on lattice})$$

and prevents the "Baby Universe" condensate phase that dominates Euclidean gravity simulations.

### Spectral Dimension Flow

The spectral dimension $d_s(\lambda)$ is defined through the return probability of a random walker on the lattice:

$$P(\mathbf{r}, t) \sim t^{-d_s/2}$$

for short times $t$. Equivalently:

$$d_s = -2 \frac{d \log P}{d \log t}$$

Measurements in CDT find:

- **Infrared (large scales)**: $d_s \approx 4$ (matches classical 4D spacetime)
- **Intermediate scales**: Smooth transition
- **Ultraviolet (Planck scale)**: $d_s \approx 1.8-2$ (fractal, lower-dimensional)

This anomalous dimensionality means that distances and volumes scale differently near the Planck cutoff than in classical geometry:

$$\text{Vol}(B_r) \sim r^{d_s(r)}$$

where $d_s(r)$ varies from 4 to ~1.8 as $r \to 0$.

### Emergence of de Sitter Space

In the phase where spacetime is both causal and has correct signature, the "blob" (largest connected component of the triangulation) naturally forms a universe-like structure resembling de Sitter space locally. The average scale factor $a(t)$ exhibits expansion:

$$\langle a^2(t) \rangle \sim \sinh^2(\lambda t)$$

where $\lambda$ is a scale parameter related to the effective cosmological constant. This emergence is **unforced**—there is no bare cosmological constant term in the action. The de Sitter behavior arises from the combinatorics of causal triangulations.

---

## Key Results

1. **Nonperturbative path integral**: CDT successfully computes the Euclidean partition function for gravity without expanding in coupling constants, yielding results unattainable by perturbation theory.

2. **Spectral dimension anomaly**: The dimensionality of spacetime flows from 4 at large scales to $d_s \approx 1.8$ at Planck scale, indicating that quantum gravity makes space fractal at smallest distances.

3. **De Sitter emergence**: A 4D expanding universe emerges naturally from the causal triangulation lattice, without a bare cosmological constant term in the action. Expansion rates scale as $\sinh(\lambda t)$.

4. **Planck-scale structure**: Diffeomorphism-invariant observables (scalar volume fluctuations, spectral measures) exhibit quantum behavior with characteristic scale set by the Planck length, approximately $\ell_P \sim 10^{-35}$ m.

5. **Phase diagram mapping**: CDT phase space shows a transition between "crumpled" (spacelike-dominated) and "elongated" (timelike-dominated) phases, with the physically relevant phase at intermediate coupling.

6. **Absence of gravitons**: The graviton propagator in CDT does not dominate the long-distance physics, suggesting that gravitons are not fundamental excitations but emergent degrees of freedom. This aligns with holographic duality ideas.

---

## Impact and Legacy

CDT has become the leading lattice approach to nonperturbative quantum gravity, complementing string theory and loop quantum gravity. Its key conceptual contributions:

**Background independence**: Unlike perturbative gravity or string theory on fixed backgrounds, CDT requires no background metric. Spacetime is constructed entirely from the dynamics of the lattice.

**Lorentzian signature preservation**: Most quantum gravity approaches (Euclidean QFT, Wick rotation tricks) disguise Lorentzian physics in Euclidean language. CDT maintains Lorentz signature throughout, avoiding unphysical Wick rotations.

**Prediction of spectral dimension flow**: The discovery that dimension anomalously flows to ~1.8 at Planck scale has motivated related work in asymptotic safety, causal sets, and loop quantum gravity. All now explore whether their frameworks predict similar dimensional flow.

**Feasibility of numerical simulations**: CDT can be simulated on modern computers, unlike superstring theory. This has enabled precision measurements of quantum gravity effects.

---

## Connection to Phonon-Exflation Framework

**Spectral dimension as diagnostic**: The phonon-exflation framework makes a parallel prediction about spectral dimension. In the framework, the internal SU(3) fiber undergoes a fold (symmetry-breaking transition) during cosmological expansion. The internal geometry's dimensionality changes during this transit, potentially exhibiting a flow similar to CDT's $d_s$ anomaly.

Specifically, the framework predicts that the internal metric's effective "dimensionality" (measured via the spectrum of the Laplacian on SU(3)) changes from the high-curvature regime ($\tau$ near 0) to the low-curvature classical regime ($\tau$ large). Comparing the framework's internal $d_s(\tau)$ to CDT's external $d_s(\ell)$ may reveal whether the external spectral dimension flow is a signature of internal fiber dynamics becoming visible in the 4D effective metric.

**Emergent spacetime from discrete substrate**: Both CDT and phonon-exflation propose that spacetime emerges from discrete, microscopic degrees of freedom. CDT uses random triangles; phonon-exflation uses Cooper pair phonons in a K-theoretic condensate. The two approaches may describe the same physics at different scales: CDT's lattice spacing as the scale where the phonon degrees of freedom decohere into geometric triangles.

**De Sitter emergence without bare Lambda**: CDT's emergence of de Sitter expansion without a bare cosmological constant term parallels phonon-exflation's prediction that Dark Energy emerges from the BCS instability and spectral action geometry, not from a fundamental cosmological constant.

**Planck-scale fractality**: If CDT's fractal dimension $d_s \sim 1.8$ at the Planck scale reflects genuine quantum geometry, then quantum fluctuations in the phonon-exflation substrate should exhibit similar fractal structure at the scale of the pairing instability (which sets the effective "Planck scale" for the cosmological dynamics). Testing whether BCS pair correlations in the framework exhibit power-law decay consistent with $d \sim 1.8$ is a concrete prediction.

The framework can be viewed as providing a **specific microscopic realization** of the CDT paradigm: the "triangles" in CDT are emergent artifacts of BCS pairing dynamics in internal space, and their causal structure is inherited from the forward-time evolution of the cosmological fold.
