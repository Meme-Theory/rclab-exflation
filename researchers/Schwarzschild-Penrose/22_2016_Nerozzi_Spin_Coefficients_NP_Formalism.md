# Spin coefficients and gauge fixing in the Newman-Penrose formalism

**Author(s):** Andrea Nerozzi
**Year:** 2016
**Journal:** arXiv preprint (published Phys. Rev. D)
**arXiv:** 1609.04037
**Relevance:** MEDIUM
**Substitutes for:** Newman-Penrose 1962 (J. Math. Phys. 3:566)

---

## Abstract

Since its introduction in 1962, the Newman-Penrose formalism has been widely used in analytical and numerical studies of Einstein's equations, like for example for the Teukolsky master equation, or as a powerful wave extraction tool in numerical relativity. Despite the many applications, Einstein's equations in the Newman-Penrose formalism appear complicated and not easily applicable to general studies of spacetimes, mainly because physical and gauge degrees of freedom are mixed in a nontrivial way. In this paper we approach the whole formalism with the goal of expressing the spin coefficients as functions of tetrad invariants once a particular tetrad is chosen. We show that it is possible to do so, and give for the first time a general recipe for the task, as well as an indication of the quantities and identities that are required.

---

## Key Arguments and Derivations

*Substitute reference for Newman-Penrose 1962 spin coefficient formalism paper (J. Math. Phys. 3:566, pre-arXiv).*

**Section I — Introduction and Weyl scalars.** Nerozzi reviews the NP formalism: the five complex Weyl scalars Ψ₀, Ψ₁, Ψ₂, Ψ₃, Ψ₄ obtained by contracting the Weyl tensor with the null tetrad ℓᵃ, nᵃ, mᵃ, m̄ᵃ (eqs. 1a-1e), and the twelve complex spin coefficients partitioned into three groups {ρ, μ, τ, π}, {λ, σ, ν, κ} and {ε, γ, β, α}. The paper's goal is to express the spin coefficients as functions of tetrad invariants once a transverse frame (Ψ₁ = Ψ₃ = 0) is fixed with the additional condition Ψ₀ = Ψ₄. Under these assumptions Ψ₂ = −(1/(2√3))Ψ₊ and Ψ₄ = −(i/2)Ψ₋ with Ψ₊ and Ψ₋ given by (eq. 2) in terms of the curvature invariants I and J. The invariants I = (1/32)C*_abcd C*^abcd and J = (1/384) C*_abcd C*^cd_ef C*^abef (eq. 3) fix the Weyl tensor. The scalar S = I³ − 27J² vanishes in the Petrov type D limit.

**Section I.B — Bianchi identities.** In transverse frames the Bianchi identities reduce to eight linear relations (eqs. 7a-7h) coupling the directional derivatives DΨ±, ΔΨ±, δΨ±, δ*Ψ± to the spin coefficients. This is only eight equations for twelve unknowns; the system is underdetermined.

**Section II — Self-dual forms.** The paper introduces three fundamental self-dual two-forms Σ_ab = 2ℓ_[a n_b] − 2m_[a m̄_b], Σ⁺_ab = 2ℓ_[a m_b], Σ⁻_ab = 2n_[a m̄_b] (eqs. 8a-c). All spin coefficients are projections of three "connection vectors" A_a, B_a, C_a constructed from these self-dual forms (eqs. 16a-c). The projections ρ = ℓᵃA_a, σ = nᵃB_a, ε = (1/2)ℓᵃC_a, etc., recover the NP spin coefficients. The Bianchi identities in this compact form read ∇_a Ψ₊ = −i√3 Ψ₋ B_a − 3 A_a Ψ₊ and ∇_a Ψ₋ = i√3 Ψ₊ B_a + (2C_a − A_a) Ψ₋ (eqs. 17a-b).

**Section III — Laplacian of the self-dual Weyl tensor.** Nerozzi introduces D*_abcd = ∇^μ ∇_μ C*_abcd (eq. 23) and shows via the Bianchi identities that D*_abcd = 16 I I_abcd − (3/2) C*_abef C*^ef_cd (eq. 29), the self-dual version of the Penrose wave equation ∇^μ∇_μ C_abcd = C_ab^ef C_ef_cd − 4C_aef[c C^e_d]^f_b (eq. 30). This gives D*_abcd a new role as a fundamental quadratic function of the Weyl tensor.

**Section V — Connection vectors from divergences.** The divergences of the basis tensors Σ⁺_abcd and Σ⁻_abcd couple linearly to A_a, B_a, C_a through a 2×2 matrix P_a (eq. 44). Using the identity ∇_a D*^a_bcd = S_a C*^a_bcd + T_a D*^a_bcd (eq. 49) and the contraction identities, Nerozzi derives explicit expressions for S_a and T_a in terms of ∇_a I, ∇_a J, and the auxiliary quantity R_a = (1/96) D*_abcd ∇_e D*^ebcd (eqs. 50-52).

**Section VI — Final result.** The connection vectors in transverse tetrads are given by (eqs. 61a-c):
- A_a = (E_A/12)[S̃_a + ∇_a ln(K/E_A)] − (1/6)∇_a ln I
- B_a = (iE_B/(4√3))[S̃_a + ∇_a ln(K/E_B)]
- C_a = (E_C/6)[S̃_a + ∇_a ln(K/E_C)] + (1/6)∇_a ln I

where E_A = (Θ − Θ⁻¹)², E_B = Θ² − Θ⁻², E_C = Θ² + Θ⁻² + 1, K = (Θ³ − Θ⁻³)/(Θ³ + Θ⁻³)^(1/3), and S̃_a = (I^(−1/2)/(√3(Θ³ + Θ⁻³))) S_a. This completes the demonstration: in a uniquely-fixed transverse tetrad, all twelve spin coefficients are functions of tetrad-invariant quantities (∇_a I, ∇_a J, and the invariant vector S_a).

**Section VII — The Kerr limit.** In the Petrov type D limit (Θ → 1) the connection vectors simplify to A_a = −(1/6)∇_a ln I, B_a = 0, C_a = (1/6)∇_a ln I + Z_a with Z_a = (1/2)[S̃_a + ∇_a ln K]. Nerozzi checks that the construction is consistent with the Goldberg-Sachs theorem (λ = σ = ν = κ = 0 in type D) and reproduces the Kinnersley-tetrad values of all spin coefficients for Kerr in Boyer-Lindquist coordinates after restoring the spin/boost parameter B = B₀ I^(−1/6) Γ^(−1/2).

## Key Results

1. In a transverse tetrad fixed by Ψ₁ = Ψ₃ = 0 and Ψ₀ = Ψ₄, all twelve NP spin coefficients can be written as functions of tetrad invariants (the curvature invariants I, J, and one additional invariant vector S_a).
2. The divergence of the Laplacian of the self-dual Weyl tensor, D*_abcd = ∇^μ∇_μ C*_abcd, satisfies ∇_a D*^a_bcd = S_a C*^a_bcd + T_a D*^a_bcd with S_a and T_a tetrad-invariant vectors. This relation provides the missing information beyond the Bianchi identities (eight equations) needed to fix all twelve spin coefficients.
3. The final connection-vector expressions (eqs. 61a-c) are manifestly well-defined in the Petrov type D (Kerr) limit despite apparent singularities in S = I³ − 27J².
4. The framework reproduces the Goldberg-Sachs theorem and the Kinnersley-tetrad Kerr spin coefficients.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Weyl scalars (definition) | Ψ_k = −C_abcd[tetrad contractions] | Eqs. (1a-e) |
| Ψ± reparameterization | Ψ± = I^(1/2)[exp(2πik/3)Θ ± exp(−2πik/3)Θ⁻¹] | Eq. (2) |
| Curvature invariants | I = (1/32)C*_abcd C*^abcd, J = (1/384)C*_abcd C*^cd_ef C*^abef | Eqs. (3a-b) |
| Bianchi identity compact | ∇_a Ψ₊ = −i√3 Ψ₋ B_a − 3 A_a Ψ₊ | Eq. (17a) |
| Self-dual forms | Σ_ab = 2ℓ_[a n_b] − 2m_[a m̄_b] etc. | Eqs. (8a-c) |
| Connection vectors | A_a = Σ⁺_ab T⁻ᵇ + Σ⁻_ab T⁺ᵇ, similar for B_a, C_a | Eqs. (16a-c) |
| Self-dual Weyl | C*_abcd = iΨ₋ Σ⁺⁺_abcd + (Ψ₊/√3) Σ̃_abcd | Eq. (22) |
| Laplacian identity | D*_abcd = 16 I I_abcd − (3/2) C*_abef C*^ef_cd | Eq. (29) |
| Key divergence identity | ∇_a D*^a_bcd = S_a C*^a_bcd + T_a D*^a_bcd | Eq. (49) |
| Tetrad-invariant S_a | S_a = (1/S)[−6 I² ∇_a J + 18 J R_a] | Eq. (52a) |
| Connection vector A_a | A_a = (E_A/12)[S̃_a + ∇_a ln(K/E_A)] − (1/6)∇_a ln I | Eq. (61a) |
| Connection vector B_a | B_a = (iE_B/(4√3))[S̃_a + ∇_a ln(K/E_B)] | Eq. (61b) |
| Connection vector C_a | C_a = (E_C/6)[S̃_a + ∇_a ln(K/E_C)] + (1/6)∇_a ln I | Eq. (61c) |

## Relevance to Phonon-Exflation

The Newman-Penrose formalism is the starting point for Petrov classification of the Weyl tensor, and the framework's analog statement — "Newman-Penrose Petrov type at the dump is D → II" — is a direct application of this formalism to the substrate transit through the van Hove fold. The reduction of all spin coefficients to tetrad invariants in this paper matches the framework's broader program of expressing all physical quantities as spectral moments of the Dirac operator D_K, and the NP Petrov classification applied to the internal SU(3) fiber curvature is how the framework states the algebraic-speciality condition at the fold. This paper substitutes for Newman-Penrose (1962), whose original spin-coefficient formalism is cited throughout the framework's Petrov analysis and algebraic speciality arguments.
