# Conformal Einstein evolution

**Author(s):** Helmut Friedrich
**Year:** 2002
**Journal:** arXiv preprint (Lecture Notes in Physics, Springer)
**arXiv:** gr-qc/0209018
**Relevance:** HIGH
**Substitutes for:** Penrose 1963 (Phys. Rev. Lett. 10:66)

---

## Abstract

We discuss various properties of the conformal field equations and their consequences for the asymptotic structure of space-times.

---

## Key Arguments and Derivations

*Substitute reference for Penrose 1963 conformal compactification paper (Phys. Rev. Lett. 10:66, pre-arXiv).*

**Section 1 — Introduction.** Friedrich motivates the conformal field equations by the centrality of the null cone structure (equivalently the conformal structure) in Einstein's theory. Penrose ([65] = Penrose PRL 1963; [66] = Penrose Riv. Nuovo Cim. 1964) proposed analyzing asymptotic behavior by extending the conformal structure to null infinity I⁺. Friedrich's subsequent work ([23], [24]) showed Einstein's equations are conformally regular — they admit conformal representations which do not contain factors Ω⁻¹ in the principal part and for which the conformal factor is determined by the equations themselves. This places Einstein's equations between conformally singular equations (like the massive Klein-Gordon equation on a fixed background) and conformally invariant equations (Maxwell, Yang-Mills in four dimensions).

**Section 2 — Conformal geometry.** The decomposition of the Riemann tensor is R^μ_νλρ = 2{g^μ_[λ L_ρ]ν − g_ν[λ L_ρ]^μ} + C^μ_νλρ (eq. 4) with L_μν = (1/(n−2))[R_μν − (1/(2(n−1))) R g_μν] (eq. 5) the Schouten tensor and C^μ_νλρ the Weyl tensor. A Weyl connection ∇̂ for Cᵍ satisfies ∇̂_ρ g_μν = −2 f_ρ g_μν (eq. 6) with a 1-form f. The connection coefficients transform as Γ̂_μ^ρ_ν = Γ_μ^ρ_ν + S(f)_μ^ρ_ν (eq. 7). When f = −Ω⁻¹ dΩ, the Weyl connection coincides with the Levi-Civita connection of g̃ = Ω⁻² g (eq. 8). The Ricci scalar under conformal rescaling satisfies 4[(n−1)/(n−2)] ∇_μ ∇^μ θ − R[g] θ = −R̃[g̃] θ^((n+2)/(n−2)) with θ = Ω^(−(n−2)/2) (eq. 9).

**Section 2.1.1 — Conformal geodesics.** These are curves x(τ) obtained with an associated 1-form b(τ) as solutions of (∇̃_ẋ ẋ)^μ + S(b)_λ^μ_ρ ẋ^λ ẋ^ρ = 0 (eq. 14) and (∇̃_ẋ b)_ν − (1/2) b_μ S(b)_λ^μ_ν ẋ^λ = L̃_λν ẋ^λ (eq. 15). They admit fractional-linear parameter transformations, are conformal invariants, and form a larger class than metric geodesics.

**Section 2.2 — Derivation of the conformal field equations.** The physical metric g̃ satisfies the vacuum Einstein equations (1). Writing g = Ω² g̃ and using the Weyl tensor transformation C^μ_νλρ (conformally covariant), Friedrich introduces the rescaled conformal Weyl tensor d^μ_νλρ = Ω^(3−n) C^μ_νλρ (eq. 25) which satisfies the Bianchi equation ∇_μ d^μ_νλρ = 0 (eq. 26). Combining with the decomposition (eq. 27) and the contracted Bianchi identity gives ∇_λ L_ρν − ∇_ρ L_λν = Ω^(n−4) ∇_μ Ω d^μ_νλρ (eq. 28). The equation for the conformal factor becomes ∇_μ ∇_ν Ω = −Ω L_μν + s g_μν (eq. 32) with s = (1/n) ∇_λ ∇^λ Ω + R Ω/(2n(n−1)). The integrability condition is ∇_μ s = −∇^ν Ω L_νμ (eq. 33). The cosmological constant appears through λ = (n−1)(2Ω s − ∇^ρ Ω ∇_ρ Ω) (eq. 34).

**Section 2.2.1 — The metric conformal field equations.** The system (26), (27), (28), (32), (33), (34) for the unknowns {g_μν, Ω, s, L_μν, d^μ_νλρ} is the metric conformal field equations. The Ricci scalar R of the conformal metric plays the role of a gauge source function for the conformal scaling (from eq. 9). These equations hold for any vacuum solution g̃ and any conformal factor Ω. They are regular even where Ω = 0 (the conformal infinity I), so they allow a smooth Cauchy problem to be formulated that "reaches" null infinity in a finite parametric time.

**Section 2.2.2 — The Bianchi equation as a hyperbolic system.** In n = 4 dimensions the Weyl tensor and its dual coincide; the contracted Bianchi identity ∇_μ d^μ_νλρ = 0 is equivalent to the full Bianchi identity. In spin-frame form, with the rescaled Weyl spinor φ_abcd completely symmetric, the Bianchi equation becomes Λ_abca' ≡ ∇^f_a' φ_abcf = 0 (eq. 36). Decomposition into space-spinor components gives six real constraints and six evolution equations. The reduced system is symmetric hyperbolic (eq. 37) and the large gauge freedom allows adaptation to characteristic, Cauchy, and initial-boundary value problems. In dimensions n ≥ 5 the Bianchi equation provides insufficient evolution equations, so the conformally regular representation works cleanly only in four dimensions.

**Section 2.2.3 — Constraints.** On a spacelike hypersurface the conformal field equations imply a system of conformal constraints that comprises but is larger than the usual vacuum constraints: it includes integrability conditions and the Gauss-Codazzi equations. The free data may admit logarithmic singularities r^k log^l r near the compactification points Σ representing space-like infinity, but under mild additional assumptions these logarithmic terms are absent.

**Section 2.2.5 — General conformal field equations.** Using Weyl connections (not only rescalings) and a conformal Gauss gauge based on a congruence of conformal geodesics, Friedrich obtains a different representation. The unknown is u = (e^μ_k, Γ̂_i^j_k, L̂_jk, d^i_jkl) (eq. 38). The system (eqs. 39-42) consists of a torsion equation (39), the curvature equation with the Weyl connection (40), the Bianchi-Codazzi equation (41), and the rescaled-Weyl Bianchi equation (42). Remarkably, for vacuum with cosmological constant λ, Θ and d_k are given explicitly by Θ = Θ_*{1 + τ <b_*, ẋ_*> + (τ²/2)[Θ_*^(−2) λ/6 + (1/2) g^♯(b_*, b_*)]} (eq. 44) and d_0 = Θ̇, d_a = <b_*, Θ_* e_a*> (eq. 45). The cosmological constant enters through this explicit formula, encoding Einstein's equations into the gauge itself.

## Key Results

1. Einstein's vacuum field equations admit a conformally regular reformulation: the metric conformal field equations (MCFE) are a system of tensor equations in {g_μν, Ω, s, L_μν, d^μ_νλρ} with no factors of Ω⁻¹ in the principal part, so they remain well-defined at conformal infinity I = {Ω = 0}.
2. In n = 4 dimensions the contracted Bianchi identity is equivalent to the full Bianchi identity, and the reduced system is symmetric hyperbolic — this enables numerical evolution on finite grids that reach null infinity in finite parameter time.
3. In n ≥ 5 dimensions the contracted Bianchi identity alone provides insufficient evolution equations; the conformally regular representation works cleanly only in four dimensions.
4. The general conformal field equations (GCFE) using a conformal Gauss gauge built from conformal geodesics admit an explicit closed-form expression for the conformal factor Θ (eq. 44) and the 1-form d_k (eq. 45) in terms of initial data and the cosmological constant λ.
5. The Ricci scalar R of the conformal metric plays the role of a gauge source function for the conformal scaling; in the GCFE version the cosmological constant is encoded directly into the gauge formula.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Einstein field equations | R̃_μν − λ g̃_μν = κ(T_μν − (1/2) T g̃_μν) | Eq. (1) |
| Conformal Ricci transformation | R_νρ[g] = R̃_νρ[g̃] − ((n−2)/Ω) ∇_ν ∇_ρ Ω − g_νρ g^λδ[(1/Ω)∇_λ∇_δΩ − ((n−1)/Ω²)∇_λΩ ∇_δΩ] | Eq. (3) |
| Riemann decomposition | R^μ_νλρ = 2{g^μ_[λ L_ρ]ν − g_ν[λ L_ρ]^μ} + C^μ_νλρ | Eq. (4) |
| Schouten tensor | L_μν = (1/(n−2))[R_μν − (1/(2(n−1))) R g_μν] | Eq. (5) |
| Weyl connection | ∇̂_ρ g_μν = −2 f_ρ g_μν | Eq. (6) |
| Conformal geodesic eq. 1 | (∇̃_ẋ ẋ)^μ + S(b)_λ^μ_ρ ẋ^λ ẋ^ρ = 0 | Eq. (14) |
| Conformal geodesic eq. 2 | (∇̃_ẋ b)_ν − (1/2) b_μ S(b)_λ^μ_ν ẋ^λ = L̃_λν ẋ^λ | Eq. (15) |
| Rescaled Weyl tensor | d^μ_νλρ = Ω^(3−n) C^μ_νλρ | Eq. (25) |
| Bianchi equation | ∇_μ d^μ_νλρ = 0 | Eq. (26) |
| Curvature decomposition | R^μ_νλρ = 2{g^μ_[λ L_ρ]ν − g_ν[λ L_ρ]^μ} + Ω^(n−3) d^μ_νλρ | Eq. (27) |
| Schouten equation | ∇_λ L_ρν − ∇_ρ L_λν = Ω^(n−4) ∇_μΩ d^μ_νλρ | Eq. (28) |
| Conformal factor eq. | ∇_μ ∇_ν Ω = −Ω L_μν + s g_μν | Eq. (32) |
| Integrability for s | ∇_μ s = −∇^ν Ω L_νμ | Eq. (33) |
| Cosmological constant | λ = (n−1)(2Ω s − ∇_ρ Ω ∇^ρ Ω) | Eq. (34) |
| Bianchi spinor form | Λ_abca' = ∇^f_a' φ_abcf = 0 | Eq. (36) |
| GCFE explicit Θ | Θ = Θ_*{1 + τ<b_*, ẋ_*> + (τ²/2)[Θ_*^(−2) λ/6 + (1/2) g^♯(b_*, b_*)]} | Eq. (44) |

## Relevance to Phonon-Exflation

Penrose's conformal compactification is the central methodology for mapping the asymptotic structure of spacetime to a finite boundary — the Penrose diagram. In the phonon-exflation framework, the same methodology is applied to the Jensen-deformation modulus space, converting an infinite-τ evolution of the fiber into a finite conformal picture where the "dump point" τ ≈ 0.19 sits at a distinguished fold in the conformal infinity of the spectral-action landscape. The fact that Einstein's equations are conformally regular (allowing smooth numerical evolution to I⁺ on finite grids) is the direct precedent for the framework's block-diagonality theorem — the spectral action is regular across the fold, so the transit is not a singularity but a phase transition. The general conformal field equations with the explicit Θ(τ) formula (eq. 44) give a concrete template for how the conformal factor can be determined analytically even in the presence of a cosmological constant, matching the framework's approach to the dS/dτ ≈ +58,673 spectral-action gradient at the fold. This paper substitutes for Penrose 1963 (the original PRL introducing conformal compactification), which is cited wherever the framework uses Penrose-diagram methodology on modulus space.
