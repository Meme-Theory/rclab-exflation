# Diabolical Points in the Spectra of Triangles

**Author(s):** Michael V. Berry and Michael Wilkinson

**Year:** 1984

**Journal:** Proceedings of the Royal Society of London, Series A, Vol. 392, pp. 15-43

---

## Abstract

In a quantum system with N parameters, degeneracies in the energy spectrum generically form (N-2)-dimensional surfaces (crossing surfaces). However, at special points in parameter space, level crossings are generically avoided (avoided crossings form (N-3)-dimensional surfaces). These exceptional points, where lines of degeneracy terminate, are called **diabolical points**. At a diabolical point, the eigenstate changes sign ('exchange symmetry'), and the Berry phase around a closed loop enclosing the point is $\pi$. The geometry of diabolical points is singular and cone-shaped in parameter space near the degeneracy. This work establishes the generic structure of quantum degeneracies and shows how geometric phases arise at topological singularities.

---

## Historical Context

The concept of degeneracy in quantum mechanics dates to Heisenberg and the early days of quantum theory. When multiple eigenstates have the same energy, the system has a degeneracy. In systems with time-independent parameters, degeneracies are stable structures.

However, in systems with N continuously varying parameters, the situation is subtle. Generically, exact degeneracies should not occur—they are "accidental" and destroyed by perturbations. Yet they do occur, and the question is: what is the generic structure?

Longuet-Higgins (1958) observed that in molecular potential energy surfaces, degeneracies appear as lines that terminate at special points—precursors of the diabolical point concept. Berry and Wilkinson's 1984 work provided the complete geometric theory, showing that degeneracies form lower-dimensional surfaces with topological defects (diabolical points) where the eigenstate geometry is singular.

This work was closely related to Berry's parallel 1984 paper on the geometric phase, as diabolical points represent the physical locus where geometric phases become nontrivial.

---

## Key Arguments and Derivations

### Dimensionality of Degeneracy Sets

Consider a quantum system with Hamiltonian $H(R)$ depending on N parameters $R = (R_1, R_2, \ldots, R_N)$. An exact degeneracy occurs when two eigenvalues coincide:

$E_n(R) = E_m(R)$

This is one constraint on N parameters, so the degeneracy set is generically (N-1)-dimensional.

However, in a basis where $H = \begin{pmatrix} E_n(R) & V(R) \\ V(R) & E_m(R) \end{pmatrix}$ within the 2-level subspace, the coupled equations are:

$(E_n - E_m) |c_n\rangle = V |c_m\rangle$

For a true degeneracy in the coupled basis, both the energy difference AND the coupling must vanish:

$E_n(R) = E_m(R)$
$\langle n | H_{\text{off-diag}} | m \rangle = 0$

These are TWO constraints on N parameters, so the degeneracy set is (N-2)-dimensional.

### The Cone Geometry

Near a diabolical point $R_0$, the degeneracy cone has a conical structure. Expand:

$E_n(R) \approx E_0 + a_1 (R_1 - R_1^0) + a_2 (R_2 - R_2^0) + \ldots$

$E_m(R) \approx E_0 + b_1 (R_1 - R_1^0) + b_2 (R_2 - R_2^0) + \ldots$

$V(R) \approx V_0 (R_3 - R_3^0) + \ldots$

The energy gap between the two levels near the crossing is:

$\Delta E = \sqrt{(\Delta E_{\text{diag}})^2 + 4|V|^2}$

where $\Delta E_{\text{diag}} = E_n^{(0)} - E_m^{(0)}$ is the diagonal (uncoupled) energy difference. A true degeneracy requires both $\Delta E_{\text{diag}} = 0$ and $V = 0$.

In polar coordinates centered at $R_0$, the cone angle $\alpha$ is determined by the Hessian of the energy surfaces:

$\tan(\alpha/2) = \frac{|V|}{|E_n - E_m|/2}$

At the diabolical point itself, the cone degenerates to a line, and the wave function has a **singularity**: as you encircle the point, the eigenstate picks up a sign change (phase $\pi$).

### Berry Phase at Diabolical Points

For a closed path C encircling a diabolical point in parameter space:

$\gamma_n(C) = \pi$

This is exact, independent of the strength of coupling or the shape of the path. The phase is topologically protected: it cannot change continuously to zero unless the path shrinks to zero (deforming away from the degeneracy).

The geometric phase is:

$\gamma_n = \int_S \mathcal{B}_n \cdot dA$

where the Berry curvature $\mathcal{B}_n$ has a delta-function singularity at the diabolical point:

$\mathcal{B}_n \sim \pi \delta(R - R_0)$ (in appropriate coordinates)

This shows that diabolical points act as monopoles in Berry phase space.

### Eigenstate Behavior

At a diabolical point, the eigenstate is non-analytic. Approaching along different paths in parameter space, the eigenstate can approach different phases. The general behavior is:

$|n(R)\rangle \to e^{i\theta(R)/2} |n_0\rangle$

where $\theta(R)$ is the polar angle in parameter space (in coordinates centered at the diabolical point). As $\theta$ increases from 0 to $2\pi$, the eigenstate picks up a phase of $\pi$, meaning:

$|n(2\pi)\rangle = -|n(0)\rangle$

This is a **geometric sign flip**—the eigenstate returns to its original value after a full circuit, but with opposite sign. Physically, this represents an exchange of two eigenstates at the degeneracy.

---

## Key Results

1. **Generic structure of degeneracies**: In N-parameter systems, N-2 dimensional crossing surfaces are generically diabolical. They terminate at (N-3)-dimensional diabolical point sets. For 3 parameters, degeneracies are 1-dimensional lines that meet at 0-dimensional points.

2. **Conical topology**: The energy surface near a diabolical point has a conical (Jahn-Teller type) geometry. The cone angle encodes the coupling strength between the degenerating levels.

3. **Exact Berry phase**: A closed loop encircling a diabolical point in parameter space produces $\gamma = \pi$, exact and topologically protected.

4. **Monopole structure**: Diabolical points act as monopoles in the Berry connection, with magnetic charge $\pi$ (in units where flux quantum is $2\pi$). Multiple diabolical points act as sources and sinks of Berry phase flux.

5. **Avoided crossing strength**: The Berry curvature determines the strength of avoided crossings. Systems with large Berry curvature show strong level repulsion; those with small curvature show weak avoidance.

---

## Impact and Legacy

Berry and Wilkinson's work on diabolical points became foundational for understanding degeneracies in quantum systems:

- **Molecular spectroscopy**: Explained conical intersections in molecular potential energy surfaces and their role in nonadiabatic coupling and photodissociation.
- **Solid state physics**: Applied to band structure calculations, showing how degeneracies near K-points in graphene and other materials have diabolical geometry.
- **Atomic physics**: Rydberg atoms in external fields show diabolical points; these have been mapped experimentally in microwave ionization experiments.
- **Optics**: Conical intersections in the dispersion of photonic crystals and metamaterials.
- **Topological physics**: The monopole picture of diabolical points laid groundwork for understanding topological defects in electronic bands and their role in topological insulators.

The concept of diabolical points is now standard in quantum chemistry and materials science, where they explain nonadiabatic processes and avoided crossings.

---

## Connection to Phonon-Exflation Framework

In the Jensen-deformed SU(3) geometry, the Dirac spectrum has numerous diabolical points as a function of the deformation parameter $s$:

1. **Sector crossings as diabolical points**: The avoided crossings between sectors (e.g., (3,0)-(2,0) at $s \approx 0.15$) have conical geometry. The nearest eigenvalues approach and avoid crossing in a characteristic cone shape, described by the Berry-Wilkinson theory.

2. **Topological protection of spectrum**: The $\pi$ Berry phase around avoided crossings protects the spectrum from small perturbations. If the Jensen deformation is slightly perturbed, the cone structure is preserved, and the avoidance persists.

3. **Eigenstate exchange**: As $s$ increases through a diabolical point, phonon eigenstates effectively exchange identity. This is relevant to the question of particle "generation mixing"—whether phonons in one generation can smoothly transition to another via spectral evolution.

4. **Conical intersections and nonradiative decay**: In the context of the spectral action, diabolical points create regions where the effective action has enhanced sensitivity to parameter changes. This could affect the running of coupling constants and stabilization of the modulus.

5. **Gauge structure from geometry**: The monopole structure of diabolical points (Berry curvature $\sim \delta(R-R_0)$) mirrors the role of singular points in gauge theory. In the NCG picture, the internal gauge structure may be partially encoded in the diabolical points of the Dirac spectrum.

The diabolical point geometry is essential to understanding avoided crossings in the phonon spectrum and their topological robustness.
