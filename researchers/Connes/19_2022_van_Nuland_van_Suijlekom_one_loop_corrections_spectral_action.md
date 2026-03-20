# One-Loop Corrections to the Spectral Action

**Authors:** Teun van Nuland, Walter van Suijlekom
**Year:** 2022
**Journal:** Journal of High Energy Physics, 2022(5), 78 (arXiv: 2107.08485)

---

## Abstract

We analyze the perturbative quantization of the spectral action in noncommutative geometry and establish its one-loop renormalizability. The spectral action, when perturbed by a gauge potential, can be written as a series of generalized Chern-Simons actions and Yang-Mills actions of all orders, with generalized Chern-Simons forms integrated against odd cyclic cocycles, and powers of the curvature integrated against Hochschild cocycles. We establish that one-loop counterterms are of the same form as the original spectral action, so they can be safely subtracted. We then apply this framework to the spectral Pati-Salam model and compute the one-loop running of gauge couplings, showing that unification is preserved at the quantum level for several scalar field scenarios. The analysis demonstrates that the spectral action is renormalizable in a generalized sense and that its predictions for gauge coupling unification (and hence for the Weinberg angle) are robust to one-loop quantum corrections.

---

## Historical Context

The spectral action program had achieved considerable success by the early 2020s in predicting the Standard Model and its coupling constants from pure geometry. However, a significant gap remained: the predictions (especially the Weinberg angle sin²(θ_W) = 3/8 at unification) were all derived at the classical level, with no account of quantum loop corrections.

In quantum field theory, loop corrections are essential for precision predictions. The running of coupling constants is driven by the one-loop beta functions, which depend on the field content and interaction structure. If the spectral action framework is to be taken seriously as a fundamental theory, it must remain valid when quantum effects are included.

This raises several questions:

1. **Renormalizability:** Is the spectral action renormalizable? Do one-loop divergences appear, and if so, can they be subtracted in a way consistent with the spectral action structure?

2. **Consistency of predictions:** If one-loop corrections modify the Seeley-DeWitt coefficients (which determine the classical gauge coupling ratios), do the predictions shift? Specifically, does sin²(θ_W) still equal 3/8, or is the value corrected?

3. **Coupling unification:** The spectral action predicts that gauge couplings unify at the GUT scale. Is this unification still valid when loop corrections are included, or do one-loop effects spoil it?

4. **New scalar particles:** The spectral action framework naturally includes a Higgs field, but the scalar content can vary (e.g., adding right-handed neutrino scalars, additional Higgs bosons, etc.). How do different scalar contents affect the running?

The van Nuland-van Suijlekom 2022 paper directly addresses these questions. By developing a formal framework for one-loop corrections to the spectral action and explicitly computing the running in the Pati-Salam model, they show that the framework remains valid and predictive at the quantum level.

---

## Key Arguments and Derivations

### 1. Perturbative Expansion of the Spectral Action

The spectral action is defined as:

$$S = \text{Tr} f\left(\frac{D_A^2}{\Lambda^2}\right)$$

where D_A = D + A is the Dirac operator perturbed by a gauge potential A.

The trace can be expanded in powers of A:

$$\text{Tr} f\left(\frac{(D + A)^2}{\Lambda^2}\right) = \text{Tr} f\left(\frac{D^2}{\Lambda^2}\right) + \int d^4 x \sqrt{g} \, \mathcal{A}_1[A] + \int d^4 x \sqrt{g} \, \mathcal{A}_2[A] + \ldots$$

where $\mathcal{A}_n$ are local action functionals that depend on A and its derivatives.

The leading term (zeroth order in A) is the pure spectral action. The linear term $\mathcal{A}_1$ vanishes by symmetry (it would correspond to a tadpole, which does not appear). The quadratic term $\mathcal{A}_2$ generates the Yang-Mills kinetic term for the gauge field. Higher-order terms $\mathcal{A}_n$ generate interactions (vertices).

**Key observation:** In the spectral action framework, the action is not simply Einstein-Hilbert + Yang-Mills + matter. Instead, it is a *constrained* action where all terms (kinetic, mass, coupling) emerge from the spectral geometry. The structure of the vertices and their coefficients are fixed by the Dirac operator and the finite geometry.

This is very different from quantum field theory, where the action is usually written down as a guess, with coupling constants and masses as free parameters.

### 2. Seeley-DeWitt Expansion and Divergences

At one-loop order, quantum corrections to the effective action are given by the one-loop determinant of the operator D_A:

$$\Gamma^{(1)}[A] = \frac{1}{2} \text{Tr} \ln D_A^2 = \frac{1}{2} \sum_n \ln \lambda_n$$

where λ_n are the eigenvalues of D_A^2.

This is regularized using the zeta-function or heat-kernel method:

$$\Gamma^{(1)}[A] = \frac{1}{2} \left. \frac{d}{ds} \zeta_A(s) \right|_{s=0}$$

where $\zeta_A(s) = \text{Tr} (D_A^2)^{-s}$ is the zeta function.

The zeta function is computed using the heat-kernel expansion:

$$\text{Tr} e^{-t D_A^2} = \sum_{n=0}^{\infty} a_n(D_A) t^{(n-4)/2}$$

where the coefficients a_n are local integrals of geometric invariants.

The divergences in the one-loop effective action correspond to poles in $\Gamma^{(1)}[A]$ at certain scales. These divergences can be regularized by introducing a cutoff, and the divergent parts can be absorbed into renormalized couplings.

**Key technical point:** In the spectral action framework, the divergences are not independent of the classical action. Instead, they can be shown to have the same form as the classical action, meaning that renormalization is "automatic"—the counterterms are of the same type as the original action.

### 3. Hochschild and Cyclic Cohomology Structure

Van Nuland and van Suijlekom use the framework of cyclic cohomology to organize the structure of the spectral action and its loop corrections.

The spectral action can be written as:

$$S = \int \phi(c(D_A))$$

where:

- $c(D_A)$ is the Chern character of D_A in cyclic cohomology
- φ is a cyclic cocycle (a linear functional on cyclic chains)
- The integral is over the 4-manifold M_4

For a product geometry M_4 × F, the Chern character decomposes as:

$$c(D_A) = c_0 \otimes 1 + c_2 \otimes 1 + c_4(D_A) + \ldots$$

where c_0 and c_2 are the universal Chern character of D and 1, and c_4 depends on A.

One-loop corrections introduce *odd* cyclic cocycles:

$$\tau_{odd}(a_0, a_1, a_2, \ldots) = (-1)^{deg} \tau(a_0 [D_A, a_1] [D_A, a_2] \ldots)$$

These give rise to generalized Chern-Simons terms:

$$\int CS(\omega) = \int_M \text{Tr}(\omega \wedge d\omega + \frac{2}{3} \omega \wedge \omega \wedge \omega)$$

The remarkable feature is that the one-loop counterterms can be organized in terms of cyclic cocycles, which have a natural geometric interpretation in noncommutative geometry.

### 4. One-Loop Running of Gauge Couplings in the Pati-Salam Model

The Pati-Salam model is an extension of the Standard Model that adds a fourth color (in the name of an additional U(1) factor), arranging leptons and quarks more symmetrically. The gauge group is:

$$G_{PS} = \text{SU(4)}_c \times \text{SU(2)}_L \times \text{SU(2)}_R$$

with the Standard Model gauge group embedded as:

$$\text{SU(3)}_c \subset \text{SU(4)}_c, \quad \text{U(1)}_Y = \text{some combination of SU(2)_L, SU(2)_R, U(1) factors}$$

In the spectral action framework, the Pati-Salam model emerges from a different choice of the finite algebra (A_PS rather than A_SM). The gauge couplings are again determined by trace invariants, and one predicts unification at the GUT scale.

Van Nuland and van Suijlekom analyze the one-loop running of the Pati-Salam couplings. The one-loop beta functions are:

$$\beta_{g_i}^{(1)} = b_i \frac{g_i^3}{16\pi^2}$$

where the coefficients b_i depend on the fermionic and scalar content.

For the Pati-Salam model in the spectral action framework:

$$\beta_1 = 11 - \frac{2}{3}(N_f + N_s)$$

where N_f is the number of fermion doublets and N_s is the number of complex scalar doublets.

The key result is that unification is preserved: the three couplings g_1, g_2, g_3 (of SU(4), SU(2)_L, SU(2)_R) remain equal at the GUT scale, even after including one-loop corrections.

**Why is this non-trivial?** The beta functions for different couplings are different (they depend on different field representations). In a generic theory, the running would break unification. However, in the Pati-Salam model with the right matter content, the beta functions conspire to preserve the unification condition: if g_1 = g_2 = g_3 at the GUT scale, then they remain equal under RGE flow.

### 5. Scalar Field Scenarios and Weinberg Angle Stability

The paper considers different scenarios for the scalar sector:

**Scenario A (Minimal Higgs):** Only one Higgs doublet, as in the Standard Model. This gives specific beta function coefficients.

**Scenario B (Extended Higgs):** Additional scalar fields (e.g., right-handed neutrino scalars, exotic Higgs bosons). These change the matter content and hence the beta functions.

**Scenario C (Composite Higgs):** If the Higgs is a composite object, the scalar content can be different still.

Van Nuland and van Suijlekom show that unification (and hence sin²(θ_W) at the GUT scale) is preserved across all scenarios. The reason is that the unification condition is determined by the geometry (the finite algebra), not by the precise scalar content.

However, the running from the GUT scale down to low energies *does* depend on the scalar content. Different scenarios yield slightly different values of sin²(θ_W(M_Z)), though all remain close to the measured value.

This is important for phenomenology: it shows that the framework is robust to variations in the Higgs sector, while still making definite predictions.

### 6. Renormalizability and Consistency

A central claim of the van Nuland-van Suijlekom paper is that the spectral action is **renormalizable in a generalized sense**.

Standard renormalizability means that all divergences can be removed by redefining coupling constants and fields, without introducing new types of interactions. In the spectral action, this is achieved, but with a twist: the renormalized couplings are still governed by the spectral geometry. The counterterms are of the same form as the original action.

Mathematically, this is expressed by saying that the one-loop effective action can be written as:

$$\Gamma^{(1)}[A] = \int d^4 x \sqrt{g} \left( \sum_k c_k^{\text{ren}}(A) \, \mathcal{O}_k[A] \right)$$

where the renormalized coefficients c_k^ren are linear combinations of the original coefficients and the loop contributions. The key point is that the *structure* of the operators $\mathcal{O}_k$ does not change—no new types of terms are generated.

In conventional quantum field theory, renormalizability is checked by power-counting: a theory is renormalizable if the couplings have positive mass dimension or are dimensionless, and if the divergent parts of loop diagrams can be subtracted. The spectral action satisfies these conditions, but the organizing principle is different: instead of assuming a Lagrangian and checking power-counting, the theory is derived from spectral geometry, and renormalizability follows from the structure of cyclic cohomology.

---

## Key Results

1. **One-loop renormalizability:** The spectral action is renormalizable at one-loop order; counterterms are of the same form as the original action, confirming the internal consistency of the framework at the quantum level.

2. **Weinberg angle stability:** The prediction sin²(θ_W) = 3/8 at the GUT scale is not corrected by one-loop effects. Loop corrections shift the value slightly, but the shift is small (order α/4π ≈ 0.1%).

3. **Unification preservation:** Gauge coupling unification at the GUT scale is preserved when one-loop corrections are included, both in the Standard Model and in extended models (Pati-Salam).

4. **Coupling constant running:** The one-loop beta functions in the spectral action framework are the same as in the Standard Model (since the perturbative expansion is the same). The difference is that the initial conditions at the GUT scale are fixed by the geometry.

5. **Scalar sector robustness:** Predictions are robust to variations in the scalar content (different Higgs sectors, additional scalars), confirming that the framework is flexible enough to accommodate phenomenology.

6. **Cyclic cocycle organization:** The structure of one-loop corrections is naturally organized in cyclic cohomology, suggesting that this mathematical framework is the "correct" setting for the spectral action, not just a convenient tool.

---

## Impact and Legacy

The van Nuland-van Suijlekom paper is significant for several reasons:

### 1. Validation of Classical Predictions

By showing that one-loop corrections do not spoil the classical predictions (Weinberg angle, unification), the paper strengthens confidence in the spectral action framework. Previous criticisms that the framework was "only classical" and would break down when quantum effects are included are addressed.

### 2. Opening the Door to Precision Predictions

With one-loop renormalizability established, the framework can now be used for precision predictions. The running of coupling constants, the anomalous dimensions of operators, and other quantum effects can be systematically included.

### 3. Connection to Loop Quantum Gravity and Quantum Geometry

The use of cyclic cohomology to organize quantum corrections suggests a deeper connection between noncommutative geometry and loop quantum gravity (LQG). Both frameworks emphasize geometric degrees of freedom and the role of topology; the van Nuland-van Suijlekom result hints at a unification.

### 4. Pati-Salam as a Testbed

The application to the Pati-Salam model shows that the spectral action framework is not limited to the Standard Model. Extensions to other GUT groups or beyond-Standard Model physics can be analyzed in the same way.

### 5. Open Questions

The paper also raises new questions:

- **Two-loop effects:** Are the predictions stable under two-loop corrections? The paper only analyzes one-loop.
- **Non-perturbative effects:** At the GUT scale, where couplings might be strong, are perturbative methods reliable?
- **Matter content:** Does the framework predict or constrain the number of generations, or the values of Yukawa couplings?

---

## Connection to Phonon-Exflation Framework

The van Nuland-van Suijlekom paper is highly relevant to phonon-exflation in several ways:

### 1. Quantum Consistency Check

If phonon-exflation is to be a viable framework, it must be consistent at the quantum level. Just as Connes-Chamseddine's classical predictions could in principle be spoiled by one-loop effects, so too could phonon-exflation's. The van Nuland-van Suijlekom approach—checking renormalizability and stability of predictions under one-loop corrections—is a model for how to validate phonon-exflation.

### 2. Structure of Quantum Corrections

The paper shows that in the spectral action, quantum corrections have a specific structure: they modify the Seeley-DeWitt coefficients but do not generate new types of interaction terms. This is a very special property, related to the geometric origin of the action.

If phonon-exflation is also derived from geometry (via the dual M_4 × SU(3) structure), it should also have this property: quantum corrections should be "safe" and not break the geometric structure.

### 3. Gauge Coupling Running

Phonon-exflation will need to specify how gauge couplings run from the high-energy (compactification) scale down to low energies. The van Nuland-van Suijlekom analysis provides a template: compute the one-loop beta functions in the specific model, verify that unification is preserved, and check that the low-energy predictions (Weinberg angle, coupling constants) match experiment.

### 4. Scalar Content and Higgs

The paper's exploration of different scalar field scenarios is relevant to phonon-exflation's treatment of the Higgs field. If the Higgs arises from the internal geometry (as in Connes-Chamseddine), then the mass and couplings are constrained. But if additional scalars are present (e.g., moduli fields from the compactification), the phenomenology changes.

Phonon-exflation should clarify which scalars are present in the low-energy effective theory and how they contribute to the running.

### 5. Two-Loop and Higher-Order Effects

While van Nuland and van Suijlekom stop at one-loop, a full validation of the framework would require checking two-loop and higher-order corrections. This is especially important if phonon-exflation is supposed to describe physics all the way up to the Planck scale, where the running might introduce large corrections.

---

## References and Further Reading

- **Connes & Chamseddine (1996-1997):** "The Spectral Action Principle" (foundational).

- **Chamseddine, Connes & Marcolli (2007):** "Gravity and the Standard Model with Neutrino Mixing" (predicts Weinberg angle classically).

- **Chamseddine & Connes (2009):** "The Uncanny Precision of the Spectral Action" (discusses classical predictions and precision electroweak fits).

- **Kreimer & van Suijlekom (2012):** "Recursive relations of Hilbert series of symmetric functions" — early work on cyclic cohomology in quantum field theory.

- **Fathizadeh & Khalkhali (2016):** "The Gauss-Bonnet theorem for V-manifolds" — mathematical foundations for spectral geometry on singular spaces.

- **Poincaré Seminar papers on NCG and quantum field theory** — various authors, 2007-2020.

---

**Word count:** 2100 lines
