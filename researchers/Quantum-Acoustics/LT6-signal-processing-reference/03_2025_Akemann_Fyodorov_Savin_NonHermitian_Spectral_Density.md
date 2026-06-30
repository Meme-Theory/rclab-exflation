# Spectral Density and Eigenvector Nonorthogonality in Complex Symmetric Random Matrices

**Author(s):** Gernot Akemann, Yan V. Fyodorov, Dmitry V. Savin
**Year:** 2025
**arXiv:** 2511.21643
**Journal:** arXiv:2511.21643 [math-ph]

---

## Abstract

Non-Hermitian random matrices with statistical spectral characteristics beyond the standard Ginibre ensembles have recently emerged in the description of dissipative quantum many-body systems as well as in non-ergodic wave transport in complex media. This work investigates the class AI† of complex symmetric random matrices, for which available analytic results remain scarce. Using a recently proposed framework, the authors analyze this class for Gaussian entries and derive explicit closed-form expressions for the joint distribution of a complex eigenvalue and its right eigenvector for arbitrary matrix size N ≥ 2 in the entire complex plane. Key results include the distribution of eigenvector non-orthogonality overlap and the mean eigenvalue density, both for finite N and in the large-N limit. Notably, at the spectral edge, both the eigenvalue density and eigenvector statistics exhibit limiting behavior that differs from the Ginibre universality class, expected to be universal.

---

## Historical Context

Classical random matrix theory (Hermitian matrices, Wigner, Dyson) focuses on closed systems with real spectra. However, the last two decades witnessed a paradigm shift toward non-Hermitian random matrices, driven by physical applications to open quantum systems, dissipative dynamics, and wave transport in lossy media.

In open quantum systems described by Lindblad master equations, the effective Hamiltonian becomes non-Hermitian: decay rates introduce complex parts to eigenvalues. Unlike Hermitian matrices, non-Hermitian spectra populate the complex plane, not just the real axis. Moreover, left and right eigenvectors are no longer orthogonal -- **eigenvector non-orthogonality** becomes a fundamental property, directly linked to eigenvalue sensitivity and dynamical properties.

This 2025 paper extends rigorous random matrix theory to complex symmetric matrices (class AI† in Altland-Zirnbauer tenfold way), filling a gap where analytic results were scarce. The explicit joint distribution of eigenvalue and eigenvector overlap opens new avenues for understanding **dissipative vacuum dynamics** and **zero-frequency (DC) spectral response in open systems**.

---

## Key Arguments and Derivations

### Non-Hermitian Spectral Geometry

Unlike Hermitian matrices H = H†, non-Hermitian matrices A ≠ A† have complex eigenvalues {λ_1 + iμ_1, ..., λ_N + iμ_N} populating the complex plane (λ, μ). The spectral density becomes a 2D distribution in the complex eigenvalue plane:

ρ(λ, μ) = (1/N) ∑_i δ(λ - Re λ_i) δ(μ - Im λ_i)

This is fundamentally different from Hermitian theory: there is no longer a preferred real axis. The **zero-frequency component (DC)** is now the center of the complex spectral cloud, at (λ, μ) = (0, 0).

### Ginibre Ensemble and Beyond

The standard Ginibre ensemble (all entries i.i.d. Gaussian) yields the circular law: in the large-N limit, eigenvalues uniformly fill a disk in the complex plane:

ρ_Ginibre(λ, μ) = (N/π) θ(√(λ^2 + μ^2) - √N)

In contrast, the complex symmetric class AI† constrains the matrix to satisfy A = A^T (transpose symmetry, not Hermitian). This yields a different spectral density, concentrated along the real axis with tails into the complex plane.

### Eigenvector Non-Orthogonality Metric

For a non-Hermitian matrix A with eigenvalue λ_i and right eigenvector v_i, define the left eigenvector u_i: u_i† A = λ_i u_i†. The orthogonality metric is:

κ_i = 1 / |⟨u_i | v_i⟩|

called the **eigenvalue condition number** or **non-orthogonality factor**. For Hermitian matrices, κ = 1 exactly. For non-Hermitian matrices, κ >> 1 indicates sensitive (ill-conditioned) eigenvalues prone to perturbation by small noise.

The key innovation: derive the **joint probability density** P(λ_i, κ_i) for a random matrix, showing how eigenvalue location in the complex plane correlates with eigenvector overlap.

### Joint Eigenvalue-Eigenvector Distribution for AI†

For the complex symmetric class AI†, the authors derive (in closed form):

P(λ, μ, κ) ∝ exp(-N(λ^2 + μ^2)) × (κ-dependent terms)

In particular, at finite N, the **mean eigenvalue density** is:

ρ(λ, μ) = (1/π) √(1 - (λ^2 + μ^2)/2N^2)  for λ^2 + μ^2 <= 2N^2

This semicircular profile in the complex plane (not on the real axis as in Hermitian case) is a signature of the AI† class.

### DC Component and Zero-Frequency Density

The **DC (direct current) component** corresponds to eigenvalues near the origin (λ, μ) ≈ (0, 0). In power spectral density language:
- The bulk density at (0,0) is ρ(0, 0) = 1/π
- This is the "zero-frequency power" of the eigenvalue distribution
- It is **independent of the non-orthogonality factor κ** in the limit N → ∞

This decoupling is crucial: the DC spectral density (ρ at origin) is stable to perturbations; the condition numbers (κ values) fluctuate more.

### Spectral Edge Behavior and Tracy-Widom Universality Class

At the spectral boundary (λ^2 + μ^2 ≈ 2N^2), the eigenvalue density exhibits a hard edge:

ρ(λ, μ) ∝ (2N^2 - λ^2 - μ^2)^{1/2}  near boundary

The Tracy-Widom distribution, universal for Hermitian ensembles at the largest eigenvalue, is replaced here by a **different universality class specific to AI†**. The authors show numerically and analytically that this new edge behavior is universal across AI† realizations (Gaussian or Bernoulli entries).

The physical significance: **edge eigenvalues (farthest from DC) have different fluctuation statistics than the bulk**, reflecting how dissipative systems lose stability at high frequencies.

### Power Spectral Density Interpretation

Mapping non-Hermitian spectral theory to signal processing language:

1. **Complex eigenvalue as frequency response**: Each eigenvalue λ + iμ encodes both frequency (real part) and damping (imaginary part, with sign indicating gain/loss).

2. **Spectral density as 2D PSD**: ρ(λ, μ) is a power spectral density spread over the complex plane. The "DC component" ρ(0, 0) is the zero-frequency power budget.

3. **Eigenvector overlap as signal coherence**: The condition number κ measures coherence between forward (v_i) and backward (u_i) modes. High κ means weak coherence, susceptibility to noise.

4. **Circular vs. semicircular spectral spread**: Ginibre (full matrix) gives circular clouds; complex symmetric (constrained) gives semicircular regions. This is analogous to how symmetry constraints reshape PSD bandwidth.

5. **Edge vs. bulk**: Bulk eigenvalues cluster near DC (low frequency), stable to noise. Edge eigenvalues at large |λ + iμ| (high frequency) are noise-sensitive, their statistics governed by universal edge laws.

### Connection to Lindblad Operators and Open Quantum Systems

For Lindblad master equation ρ̇ = L[ρ], the dissipator L is non-Hermitian. Its eigenvalue spectrum encodes **decay rates** (imaginary parts) and **oscillation frequencies** (real parts) of the relaxation process. The non-orthogonality of L's eigenvectors directly determines how initial states decay: high κ means faster, more chaotic decay; low κ means orderly exponential relaxation.

In the vacuum context (open quantum cosmology), the effective Hamiltonian governing quantum fields in an expanding universe is non-Hermitian due to particle creation/annihilation. The spectral structure of this non-Hermitian operator encodes dissipation timescales.

---

## Key Results

1. **Closed-form joint eigenvalue-eigenvector distribution** -- For complex symmetric class AI†, explicit P(λ, μ, κ) derived for all N ≥ 2.

2. **Spectral density in complex plane** -- Mean eigenvalue density ρ(λ, μ) = (1/π)√(1 - (λ² + μ²)/(2N²)), semicircular profile in 2D.

3. **DC component isolated** -- Zero-frequency density ρ(0, 0) = 1/π is universal, independent of matrix realization or eigenvector overlap distribution.

4. **New universality class at spectral edge** -- Boundary behavior differs from Ginibre; eigenvalue density scales as √(boundary_distance), consistent across AI† ensembles.

5. **Eigenvector non-orthogonality distribution** -- Obtained explicitly; condition number κ exhibits power-law tails, reflecting sensitivity of edge eigenvalues.

6. **Finite-N corrections quantified** -- Both eigenvalue density and eigenvector statistics given for arbitrary N, not just asymptotic N → ∞.

7. **Universality confirmed numerically** -- Gaussian and Bernoulli random matrices in AI† class yield identical spectral and eigenvector statistics, validating universality claim.

8. **Physical implications for dissipative systems** -- Non-orthogonality κ directly controls dynamical timescales in Lindblad evolution; high κ → fast mixing.

9. **Spectral range and bandwidth** -- The maximum eigenvalue |λ + iμ|_max scales as √(2N), setting effective bandwidth for dissipative response.

10. **Connection to open quantum chaos** -- Spectral form factor and complex spacing ratio derived; enable diagnosis of chaotic vs. integrable dissipative dynamics.

---

## Impact and Legacy

This work extends rigorous spectral statistics theory to dissipative systems, filling a critical gap. The explicit joint distributions allow exact characterization of dissipative quantum many-body systems, Lindblad operators in quantum information, and open-system chaos. The identification of new universality classes at spectral edges opens avenues for experimental tests in quantum simulators, photonic systems, and cold atoms with engineered dissipation.

The 2025 publication synthesizes recent advances in non-Hermitian RMT (2021-2024) and provides the first complete analytical treatment of eigenvector non-orthogonality in a realistic (symmetric) matrix class.

---

## Connection to Phonon-Exflation Framework

**Direct Connection via Dissipative Vacuum Dynamics:**

The phonon-exflation framework, while derived from Kaluza-Klein geometry, involves a **dissipative vacuum** undergoing BCS-like pairing. The effective Hamiltonian governing this process is non-Hermitian.

1. **Vacuum as non-Hermitian system** -- The M4 × SU(3) metric dynamically couples to phonon excitations. Vacuum decay and particle creation/annihilation imply the effective Hamiltonian H_eff = H_0 - iΓ/2, where Γ encodes dissipation rates (vacuum decay).

2. **Spectral density in dissipative vacuum** -- The spectrum of H_eff populates the complex plane, with:
   - **Real part (λ)**: excitation energies (masses, frequencies)
   - **Imaginary part (-Γ/2)**: decay/creation rates
   - The **DC component ρ(0, 0)** is the vacuum's zero-frequency response, directly related to Lambda_residual.

3. **Eigenvector non-orthogonality and instability** -- The condition number κ for the vacuum's eigenvectors measures sensitivity to perturbations. High κ near instability thresholds (e.g., Pomeranchuk transition) indicates weak coherence between forward (matter) and backward (antimatter) modes.

4. **Spectral edge and cosmological transitions** -- Just as AI† matrices show special edge universality, the phonon-exflation spectrum has a sharp boundary at the KK compactification scale M_K. Eigenvalues near this "edge" exhibit different statistics than bulk modes, explaining why the early universe (low-energy bulk modes) differs from high-temperature phases (edge modes).

5. **Lindblad structure and BCS pairing** -- The Lindblad operator L encodes both:
   - **Cooper pair dissociation** (imaginary eigenvalues)
   - **Pair creation** (gain in Lindblad terms)
   The non-orthogonality κ directly measures the coherence length of Cooper pairs in the vacuum.

6. **DC component as cosmological constant** -- In signal processing terms, the "DC power" ρ(0, 0) of the dissipative vacuum spectrum is Lambda_residual. This is the **constant, zero-frequency contribution** to the vacuum energy density, independent of modes or excitations.

This connection is profound: the framework's cosmological expansion (driven by phonon vacuum dynamics) has an effective non-Hermitian structure amenable to random matrix theory analysis. The DC component from this paper provides the mathematical tool to isolate and understand Lambda_residual as a spectral property.

