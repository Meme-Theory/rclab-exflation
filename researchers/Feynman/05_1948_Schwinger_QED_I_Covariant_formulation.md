# Quantum Electrodynamics. I. A Covariant Formulation

- **Author**: Julian Schwinger
- **Year**: 1948 (received July 29, 1948; published November 15, 1948)
- **Journal**: Physical Review, Vol. 74, No. 10, pp. 1439–1461
- **Relevance**: CRITICAL — foundational covariant QED paper; introduces interaction representation, space-like-surface quantization, invariant collision operator S, reaction operator K, and variational principle. Sets the mathematical stage for what the Phonon-Exflation program calls the "spectral action one-loop expansion" via the heat-kernel / proper-time kernel. Schwinger-instanton duality used in S38 traces directly to the interaction-representation formalism built here.

## Abstract (verbatim)

> Attempts to avoid the divergence difficulties of quantum electrodynamics by mutilation of the theory have been uniformly unsuccessful. The lack of convergence does indicate that a revision of electrodynamic concepts at ultrarelativistic energies is indeed necessary, but no appreciable alteration of the theory for moderate relativistic energies can be tolerated. The elementary phenomena in which divergences occur, in consequence of virtual transitions involving particles with unlimited energy, are the polarization of the vacuum and the self-energy of the electron, effects which essentially express the interaction of the electromagnetic and matter fields with their own vacuum fluctuations. The basic result of these fluctuation interactions is to alter the constants characterizing the properties of the individual fields, and their mutual coupling, albeit by infinite factors. The question is naturally posed whether all divergences can be isolated in such unobservable renormalization factors; more specifically, we inquire whether quantum electrodynamics can account unambiguously for the recently observed deviations from the Dirac electron theory, without the introduction of fundamentally new concepts. This paper, the first in a series devoted to the above question, is occupied with the formulation of a completely covariant electrodynamics. Manifest covariance with respect to Lorentz and gauge transformations is essential in a divergent theory since the use of a particular reference system or gauge in the course of calculation can result in a loss of covariance in view of the ambiguities that may be the concomitant of infinities. It is remarked, in the first section, that the customary canonical commutation relations, which fail to exhibit the desired covariance since they refer to field variables at equal times and different points of space, can be put in covariant form by replacing the four-dimensional surface t=const. by a space-like surface. The latter is such that light signals cannot be propagated between any two points on the surface. In this manner, a formulation of quantum electrodynamics is constructed in the Heisenberg representation, which is obviously covariant in all its aspects. It is not entirely suitable, however, as a practical means of treating electrodynamic questions, since commutators of field quantities at points separated by a time-like interval can be constructed only by solving the equations of motion. This situation is to be contrasted with that of the Schrödinger representation, in which all operators refer to the same time, thus providing a distinct separation between kinematical and dynamical aspects. A formulation that retains the evident covariance of the Heisenberg representation, and yet offers something akin to the advantage of the Schrödinger representation can be based on the distinction between the properties of non-interacting fields, and the effects of coupling between fields. In the second section, we construct a canonical transformation that changes the field equations in the Heisenberg representation into those of non-interacting fields, and therefore describes the coupling between fields in terms of a varying state vector. It is then a simple matter to evaluate commutators of field quantities at arbitrary space-time points. One thus obtains an obviously covariant and practical form of quantum electrodynamics, expressed in a mixed Heisenberg-Schrödinger representation, which is called the interaction representation. The third section is devoted to a discussion of the covariant elimination of the longitudinal field, in which the customary distinction between longitudinal and transverse fields is replaced by a suitable covariant definition. The fourth section is concerned with the description of collision processes in terms of an invariant collision operator, which is the unitary operator that determines the over-all change in state of a system as the result of interaction. It is shown that the collision operator is simply related to the Hermitian reaction operator, for which a variational principle is constructed.

## Key Arguments

### 1. Divergence landscape of QED and the renormalization question
The divergences of QED are confined to two elementary virtual processes: (i) vacuum polarization (virtual e+e− pair creation modifies photon propagation; in a gauge-invariant theory the photon proper mass must be zero, a non-trivial requirement), and (ii) electron self-energy (virtual photon emission/absorption plus exclusion-principle suppression of coupled vacuum fluctuations; yields a logarithmic electromagnetic proper mass). Both effects logarithmically renormalize e and m. Schwinger frames the fundamental question: are *all* physically significant divergences absorbable into charge and mass renormalization? The series is motivated by the Lamb–Retherford shift and the anomalous g of the electron (Kusch–Foley), for which Schwinger's earlier (Phys Rev 73, 415, 1948) calculation showed radiative corrections simultaneously explain both deviations from Dirac.

### 2. Covariance in the Heisenberg representation (Section 1)
Conventional canonical commutators [A_μ(r,t), ∂_t A_ν(r',t)/c] = iħc δ_μν δ(r−r') are tied to equal-time surfaces, which breaks manifest Lorentz invariance — intolerable in a divergent theory where ambiguities could masquerade as physics. Schwinger generalizes the equal-time surface to an arbitrary **space-like surface** σ, on which (x_μ − x'_μ)² > 0 for any two points. Commutators vanish between field operators at distinct space-like-separated points (kinematical independence), and a covariant surface-integrated commutator replaces the δ-function normalization. Self-consistency is established via **functional derivatives with respect to the surface** δ/δσ(x), with Gauss's theorem converting them into local coordinate derivatives.

### 3. Interaction representation (Section 2)
A unitary transformation Ψ[σ] = U[σ]Φ with iħc δU/δσ(x) = ℋ(x) U, choosing ℋ(x) = −(1/c) j_μ(x) A_μ(x) (negative of the Lagrangian interaction term), transforms the Heisenberg field equations into those of **free fields** while loading the dynamical content into the state-vector evolution δΨ/δσ(x) = −(i/ħc) ℋ(x) Ψ. This is the covariant generalization of Tomonaga's many-time formalism. Free-field commutators at *arbitrary* space-time separation are then expressible in closed form through invariant functions D(x) (photon) and Δ(x) (electron), which satisfy □²D = 0 and (□² − κ₀²)Δ = 0 and encode Cauchy data on any space-like surface.

### 4. Covariant elimination of the longitudinal field (Section 3)
Using an arbitrary time-like unit vector n_μ (not the non-covariant n_μ = (0,0,0,i)), A_μ decomposes into Λ (n-gradient), Λ' (transverse-gradient), and the divergence-less 𝒜_μ. The supplementary condition ∂_μ A_μ Ψ = 0 reduces to (Λ − Λ')Ψ = 0. A further canonical transformation Ψ → exp(−iG'[σ]) Ψ with G' = (1/ħc)∫(1/c)j_μ(x)Λ'(x)dσ_μ removes Λ' and produces an equation of motion containing only 𝒜_μ plus a covariant instantaneous Coulomb term ∝ j_μ(x) j_λ(x') ∂_μ 𝔇(x − x')/∂x_λ — the covariant expression of the Coulomb interaction between charges.

### 5. Invariant collision operator S and reaction operator K (Section 4)
Defining S = U[+∞, −∞], the overall change in state Ψ[+∞] = SΨ[−∞] is governed by the **integral equation** U[σ, −∞] = 1 − (i/ħc)∫_{−∞}^{σ} ℋ(x') U[σ', −∞] dω'. Introducing V[σ] by U[σ, −∞] = V[σ]·½(1+S), the symmetric equation V[σ] + (i/2ħc) ∫ ε[σ,σ'] ℋ(x') V[σ'] dω' = 1 yields the Hermitian **reaction operator** K = (1/2ħc) ∫ ℋ(x) V[σ] dω and the Cayley form **S = (1 − iK)/(1 + iK)**. K is Hermitian iff S is unitary. A **variational principle** is constructed: K viewed as a bilinear functional K' = V'[σ] (∫ ℋ V dω)⁻¹ · 2ħc · ⟨…⟩ is stationary δK = 0 when V, V⁺ satisfy the integral equations. Translation invariance of S gives [S, P_μ^(0)] = 0 — energy-momentum conservation in collisions.

## Key Results (numbered)

1. **Space-like-surface quantization**: Canonical commutators become manifestly Lorentz covariant when time slices are replaced by arbitrary space-like surfaces σ, with kinematical independence [A_μ(x), A_ν(x')] = 0 for (x − x')² > 0.
2. **Functional-derivative calculus**: δF[σ]/δσ(x) = ∂F(x)/∂x_μ (via Gauss) gives a consistent local notion of "surface evolution."
3. **Interaction-representation canonical transformation**: Generator ℋ = −(1/c) j_μ A_μ precisely reduces Heisenberg-picture coupled equations to free-field equations plus a state-vector Tomonaga–Schwinger equation iħc δΨ/δσ(x) = ℋ(x) Ψ.
4. **Invariant propagation functions** D(x), Δ(x) satisfy □²D = 0 and (□² − κ₀²)Δ = 0 with odd-function property D(−x) = −D(x), Δ(−x) = −Δ(x); solve the Cauchy problem on any σ.
5. **Free-field covariant (anti)commutators**: [A_μ(x), A_ν(x')] = iħc δ_μν D(x − x'); {ψ_α(x), ψ̄_β(x')} = (1/i)(γ_μ ∂_μ − κ₀)_{αβ} Δ(x − x').
6. **Covariant longitudinal elimination**: After two canonical transformations the physical electromagnetic degrees of freedom reduce to the divergence-less 𝒜_μ plus a covariant Coulomb kernel ∂𝔇/∂x_μ coupled bilinearly in the current.
7. **Cayley form of S**: S = (1 − iK)/(1 + iK) with K = K⁺; equivalent to unitarity of S.
8. **Variational principle for K**: δK = 0 at the solution of the integral equation (4.14), enabling first-order errors in V to produce second-order errors in scattering observables — Schwinger's scattering variational principle generalized to covariant QED.
9. **Translation invariance / conservation law**: [S, P_μ^(0)] = 0, proving total 4-momentum of the free-field operator is preserved by interaction.

## Key Equations

| # | Equation | Description |
|---|---|---|
| 1.9 | ℒ = −½(∂_μ A_ν)² − (ħc/2) ψ̄[γ_μ(∂_μ − ieA_μ/ħc) + κ₀]ψ − (ħc/2)ψ̄'[γ_μ(∂_μ + ieA_μ/ħc) + κ₀]ψ' | Lorentz-, gauge-, charge-conjugation-invariant Lagrangian density |
| 1.14 | j_μ(x) = (iec/2)[ψ̄γ_μψ − ψ̄'γ_μψ'] | Charge-symmetric four-current |
| 1.15 | □²A_μ(x) = −(1/c) j_μ(x) | Maxwell in Lorenz gauge |
| 1.18 | ∂_μ A_μ(x) Φ = 0 | Gupta-Bleuler-type supplementary condition on physical state |
| 1.39 | (x_μ − x'_μ)² > 0 | Space-like-separation condition defining σ |
| 1.43 | ∫_σ [A_μ(x), ∂/∂x_λ' A_ν(x')] dσ_λ' = (ħc/i) δ_μν | Covariant surface-integrated commutator |
| 1.44 | δF[σ]/δσ(x) = lim_{δω→0} (F[σ'] − F[σ])/δω | Functional derivative w.r.t. space-like surface |
| 2.5 | iħc δU[σ]/δσ(x) = ℋ(x) U[σ] | Tomonaga–Schwinger equation for U |
| 2.6 | iħc δΨ[σ]/δσ(x) = ℋ(x) Ψ[σ] | Interaction-picture state evolution |
| 2.7 | ℋ(x) = −(1/c) j_μ(x) A_μ(x) | Interaction Hamiltonian density |
| 2.17 | □²D(x) = 0, D(x)=0 for x_μ² > 0, ∫_σ ∂D/∂x_μ dσ_μ = 1 | Photon invariant function |
| 2.18 | (□² − κ₀²)Δ(x) = 0, Δ(x)=0 for x_μ² > 0, ∫_σ ∂Δ/∂x_μ dσ_μ = 1 | Electron invariant function |
| 2.28 | [A_μ(x), A_ν(x')] = iħc δ_μν D(x − x') | Free-field photon commutator |
| 2.29 | {ψ_α(x), ψ̄_β(x')} = (1/i)(γ_μ ∂_μ − κ₀)_{αβ} Δ(x − x') | Free-field electron anti-commutator |
| 2.32 | [∂_μ A_μ(x) − ∫_σ D(x − x') (1/c) j_μ(x') dσ_μ'] Ψ[σ] = 0 | Covariant supplementary condition in interaction picture |
| 2.41 | G[σ] = (1/ħc) ∫_σ (1/c) j_μ(x) Λ(x) dσ_μ | Gauge-transformation generator on Ψ |
| 2.52 | P_μ[σ] = P_μ^(0) − (1/c) ∫_σ ℋ(x) dσ_μ | Energy-momentum split: free plus interaction |
| 3.16 | ∂_μ A_μ(x) = (n_μ ∂_μ)²(Λ − Λ') | Longitudinal piece isolated |
| 3.26 | (Λ(x) − Λ'(x)) Ψ[σ] = 0 | Reduced supplementary condition after gauge transformation |
| 3.32 | iħc δΨ/δσ(x) = {−(1/c) j_μ 𝒜_μ − ½ ∫_σ n_ν ∂𝔇(x−x')/∂x_ξ · n_μ j_μ(x)(1/c) j_λ(x') dσ_λ'} Ψ | Physical interaction-picture evolution with covariant Coulomb term |
| 4.6 | U[σ, −∞] = 1 − (i/ħc) ∫_{−∞}^{σ} ℋ(x') U[σ', −∞] dω' | Volterra integral equation for U |
| 4.14 | V[σ] + (i/2ħc) ∫ ε[σ,σ'] ℋ(x') V[σ'] dω' = 1 | Symmetric integral equation (advanced + retarded) |
| 4.15 | K = (1/2ħc) ∫ ℋ(x) V[σ] dω | Hermitian reaction operator |
| 4.16 | **S = (1 − iK)/(1 + iK)** | Cayley parametrization; manifestly unitary for K = K⁺ |
| 4.23 | V'[σ] = V[σ] · ( ∫ ℋ V dω )⁻¹ · 2ħc · K | Stationary functional giving δK = 0 variational principle |
| 4.24 | [S, P_μ^(0)] = 0 | Total-momentum conservation across collision |

## Relevance to Phonon-Exflation

1. **Proper-time → heat kernel → spectral action**. Schwinger's interaction representation treats the coupling ℋ = −(1/c)j_μ A_μ as generating evolution in a Lorentz-covariant "surface time." His companion QED-II paper will introduce the proper-time representation G(x,x') = −i∫₀^∞ ds ⟨x|exp(−isH)|x'⟩ for the one-loop effective action, and that same kernel is exactly the heat kernel Tr exp(−s D²) that underlies Connes' spectral action principle **S_spectral = Tr f(D/Λ)**. Every Seeley–DeWitt coefficient a_{2k} in our framework's spectral expansion traces back to Schwinger's proper-time representation first systematized here. The covariant interaction picture (Eq. 2.5–2.7) is the direct ancestor of the effective-action machinery that generates gravity (a_2), Yang–Mills (a_4), and the Higgs potential in the NCG program.

2. **Schwinger-instanton duality (S38)**. Framework session S38 identified S_Schwinger = S_inst = 0.069 — the Schwinger pair-production action at the van Hove fold equals the instanton action for tunneling through the Jensen deformation. The mathematical basis for this duality is precisely the Wick-rotated proper-time kernel that Schwinger's 1948 apparatus produces: imaginary-time evolution in σ converts the collision operator S into a Euclidean tunneling amplitude exp(−S_inst/ħ). The S-matrix representation S = (1 − iK)/(1 + iK) (Eq. 4.16) with Hermitian K is the continuation into the region where K develops an imaginary part through threshold singularities, reproducing the Parker pair-creation probability used in framework's transit calculations.

3. **Space-like surface quantization ↔ acoustic white-hole front**. Schwinger's replacement of equal-time slices by space-like σ is structurally identical to the framework's treatment of the transit front as a Cauchy surface through which quasiparticle excitations propagate. The functional derivative δ/δσ(x) is the continuum analog of "how the eigenvalue spectrum of D_K reorganizes when the fabric deforms locally at x" — the variational statement at the fold.

4. **Covariant Coulomb kernel ↔ effective long-range interaction between relay patterns**. Section 3's covariant Coulomb term n_ν ∂𝔇(x−x')/∂x_ξ · j_μ j_λ is the ancestor of any instantaneous effective interaction derived after integrating out a constrained mode — in framework language, the analog is the residual long-range interaction between surviving GGE quasiparticles after the longitudinal (Λ, Λ') modes of the Jensen deformation have been gauge-fixed away.

5. **Variational principle for K**. Schwinger's δK = 0 stationary principle (Eq. 4.22–4.23) is a direct template for the framework's pre-registered gate methodology: define a functional whose stationary point is the physical amplitude, then evaluate with a trial V[σ]; first-order error in V gives second-order error in K. This is the same logic we use when Bogoliubov trial states are inserted into the GPE action to bound quasiparticle spectra.

6. **No landscape of gauge choice**. The paper's central epistemic posture — "manifest covariance is essential in a divergent theory because gauge/frame choice can convert ambiguity into false physics" — is exactly the discipline applied in framework's constraint-map methodology: eliminate gauge/convention freedom at the action level before computing, so that divergent intermediate expressions cannot hide convention-shopping.
