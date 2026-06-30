# Waves in the Witten Bubble of Nothing and the Hawking Wormhole

**Author(s):** Alain Bachelot
**Year:** 2016
**Journal:** arXiv preprint (math-ph)
**arXiv:** 1601.03682
**Relevance:** MEDIUM
**Substitutes for:** Witten 1982 (Nucl. Phys. B 195:481)

---

## Abstract

We investigate the propagation of the scalar waves in the Witten space-time called "bubble of nothing" and in its remarkable sub-manifold, the Lorentzian Hawking wormhole. Due to the global hyperbolicity, the global Cauchy problem is well-posed in the functional framework associated with the energy. We perform a complete spectral analysis that allows to get an explicit form of the solutions in terms of special functions. If the effective mass is non zero, the profile of the waves is asymptotically almost periodic in time. In contrast, the massless case is dispersive. We develop the scattering theory, classical as well as quantum. The quantized scattering operator leaves invariant the Fock vacuum: there is no creation of particles. The resonances can be defined in the massless case and they are purely imaginary.

---

## Key Arguments and Derivations

*Substitute reference for Witten 1982 bubble of nothing paper (Nucl. Phys. B 195:481, pre-arXiv).*

**Section I — Introduction.** Witten (1982) introduced the "bubble of nothing" as an instability of the Kaluza-Klein universe (R_τ × R³_ξ × S¹_ψ with metric dτ² − dξ² − dψ²). By double analytic continuation of the 5D Schwarzschild metric (T = iψ, Θ = π/2 + it) he produced a vacuum 5D solution in which the ball {|ξ|² < τ² + R²} is removed and the surface {|ξ|² = τ² + R²} is not a boundary but a surface of minimal area — the 2+1 de Sitter space dS³. The Kaluza-Klein circle shrinks to zero there, so space ends on the bubble. Bachelot develops the mathematical theory of scalar wave propagation on this spacetime and on its equatorial slice, the Lorentzian Hawking wormhole.

**Section II — The Witten spacetime.** Starting from 5D Schwarzschild (ρ > R) and the double analytic continuation, Bachelot derives the exterior Witten metric (eq. II.2). Introducing Rindler coordinates τ = ρ sinh t, ξ = ρ cosh t (eq. II.3), the metric becomes (eq. II.4) on the region ξ² > τ² + R². The new radial coordinate r = R⁻¹√(ρ² − R²) (eq. II.5) produces the form ds² = R²{(r² + 1)dt² − g_ij(t)dx^i dx^j} (eq. II.6) with g_ij(t)dx^i dx^j = dr² + (r²+1)cosh²t(dθ² + sin²θ dφ²) + (r²/(r²+1))dψ² (eq. II.7). The transformation y = (r·exp(√(r²+1))/(1+√(r²+1)))cos ψ, z = (r·exp(√(r²+1))/(1+√(r²+1)))sin ψ (eq. II.8) gives a globally smooth line element (eq. II.9). The implicit equation r²exp(2√(r²+1))(1+√(r²+1))⁻² = y² + z² is solved using the generalized Lambert function W(+2,−2; x) (eqs. II.11-II.12). The Witten spacetime M = R_t × R²_yz × S² is a C^∞ Lorentzian manifold without boundary (eq. II.17). **Proposition II.1** (global hyperbolicity): Σ_t is a Cauchy hypersurface, proven by a direct causal-curve argument.

**Asymptotics.** At spacelike infinity (ρ → ∞) the metric approaches the 4D Rindler × S¹ (or Kaluza-Klein) form (eq. II.18). At timelike infinity (x = arcsinh r → ∞) the metric approaches the de Sitter form (eq. II.19). Using σ = (ρ + √(ρ²−1))/2 (eq. II.20), the sub-manifold Ω₁ = const is conformally flat (eq. II.21). At future/past null infinity the Witten spacetime looks like the Kaluza-Klein spacetime.

**Section III — Causal geodesics.** All future-directed causal geodesics have bounded y, z coordinates; the projection on R² × S² is bounded for timelike geodesics. The angular coordinate φ satisfies |dφ/dt| ≤ 1/cosh t, giving a cosmological horizon analogous to de Sitter's: any observer sees a maximum φ-range |φ − φ₀| ≤ 2[arctan(e^t) − arctan(e^(t₀))]. Null geodesics crossing the bubble of nothing project to whole straight lines in the (y,z) plane passing through the origin; timelike geodesics crossing r = 0 are λ-periodic in their (y,z) coordinates. There exist timelike geodesics that rotate along the full Kaluza-Klein circle S¹.

**Section IV — Klein-Gordon equation.** The equation □_g u + M²u = 0 (M ≥ 0 the mass) takes the form [∂²_t + 2 tanh t ∂_t − (1/cosh²t)Δ_S² + L]u = 0 (eq. I.1) with L a t-independent differential operator on R²_yz. The Cauchy problem is well-posed in the energy norm E(u,t) = |∂_t u|² + (1/cosh²t)|∇_S² u|² + |L^(1/2) u|². The Hamiltonian L decomposes via Fourier modes in ψ as L = ⊕_{n∈Z} L_{M,n} with L_{M,n} = −(1/sinh 2x) ∂_x(sinh 2x ∂_x) + (M² + n²) cosh²x + n² coth²x. For n = 0 this is ordinary matter; n ≠ 0 are Kaluza-Klein tower states (always massive).

**Section V — Spectral analysis and solutions.** The generalized eigenfunctions Φ(λ,·) of L satisfy LΦ(λ,·) = λ Φ(λ,·), and u decomposes as u(t,ω,·) = ∫_{σ(L)} v_λ(t,ω) Φ(λ,·) dμ(λ), where v_λ solves the Klein-Gordon equation with mass √λ on de Sitter dS³: [∂²_t + 2 tanh t ∂_t − (1/cosh²t)Δ_S² + λ] v_λ = 0. The waves on the Witten spacetime are a Kaluza-Klein tower of waves on dS³. The massive case (effective mass √(M²+n²) ≠ 0) has discrete spectrum σ(L_{M,n}) ⊂ (1,∞) with a confining potential. The massless case (M = n = 0) has absolutely continuous spectrum σ(L_{0,0}) = [1,∞).

**Section VI — Asymptotic behavior.** Defining the profile v = (cosh t) u, which solves [∂²_t − (1/cosh²t)Δ_S² + L − 1] v = 0, Bachelot compares to v_♯ satisfying [∂²_t + L − 1] v_♯ = 0. If the effective mass is nonzero, v is asymptotically almost-periodic as |t| → ∞. If M = n = 0 (massless scalar), v is asymptotically dispersive.

**Section VII-VIII — Hawking wormhole.** The Lorentzian Hawking wormhole is the submanifold ψ = {N, S} (antipodal points on S¹), with metric ds²_W = R² cosh²(x)[dt² − dx² − cosh²t dΩ²] for x ∈ R. Its throat (x = 0) is dS³; it is conformally flat, has Ricci scalar zero, violates the null energy condition, and is "weakly traversable": light rays cross the throat but timelike geodesics stay near it forever. Scalar Klein-Gordon waves on the wormhole are globally well-posed; the massless case is asymptotically free (v(t,x,ω) ~ v⁺_{in/out}(x+t, ω) + v⁻_{in/out}(x−t, ω)), so the wormhole is traversable by massless fields only.

**Section IX — Scattering.** For both the Witten spacetime and the Hawking wormhole, classical and quantum scattering operators S: v_in → v_out exist and are isomorphisms on one-particle Hilbert spaces. They are unitarily implementable in Fock-Cook quantization with no mixing between positive and negative frequencies. The quantized scattering operator leaves the Fock vacuum invariant — there is no creation of particles despite the time-dependence of the background. In the massless case resonances exist and are purely imaginary.

## Key Results

1. The Witten "bubble of nothing" spacetime is a C^∞ globally hyperbolic Lorentzian manifold R_t × R²_yz × S² without boundary; Σ_t is a Cauchy hypersurface.
2. The scalar Klein-Gordon Cauchy problem is globally well-posed on the Witten spacetime in the energy norm.
3. Scalar waves on the Witten spacetime decompose as a Kaluza-Klein tower of waves on the 2+1 de Sitter space dS³ with effective mass √(M² + n²) for the nth KK mode.
4. Massive fields (M² + n² > 0) have asymptotically almost-periodic profiles; massless fields (M = n = 0) are dispersive.
5. The Lorentzian Hawking wormhole is the ψ-antipodal submanifold; conformally flat, Ricci-scalar zero, weakly traversable (light crosses, timelike geodesics do not).
6. Classical and quantum scattering operators exist on both spacetimes and the quantized scattering leaves the Fock vacuum invariant — no particle creation despite time-dependent backgrounds.
7. Null geodesics crossing the bubble of nothing (r = 0) project to whole straight lines in the (y,z) plane through the origin; timelike geodesics crossing r = 0 are periodic.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Exterior Witten metric | ds² = ρ² dt² − (1−R²/ρ²)⁻¹ dρ² − ρ² cosh²t dΩ²₂ − (1 − R²/ρ²) dΩ²₁ | Eq. (II.2) |
| Rindler form | ds² = dτ² − dξ² − ξ² dΩ²₂ − dΩ²₁ + (R²/(ξ²−τ²)){dΩ²₁ − (τdτ−ξdξ)²/(ξ²−τ²−R²)} | Eq. (II.4) |
| Radial substitution | r = R⁻¹√(ρ² − R²) | Eq. (II.5) |
| Spatial metric | g_ij dx^i dx^j = dr² + (r²+1)cosh²t(dθ² + sin²θ dφ²) + (r²/(r²+1)) dψ² | Eq. (II.7) |
| Smooth coordinates | y = (r e^√(r²+1)/(1 + √(r²+1)))cos ψ; z = (r e^√(r²+1)/(1 + √(r²+1)))sin ψ | Eq. (II.8) |
| Lambert relation | √(r²+1) = (1/2) W(+2,−2; y²+z²) | Eq. (II.12) |
| Bubble of nothing | B = R_t × {0_R²} × S², ds² = dt² − cosh²t dΩ²₂ | Eq. (II.15) |
| Global Witten metric | ds² = (r²+1)dt² − ((1+√(r²+1))²/(r²+1))e^(−2√(r²+1))(dy² + dz²) − (r²+1)cosh²t dΩ²₂ | Eq. (II.17) |
| Hawking wormhole | ds²_W = R² cosh²(x)[dt² − dx² − cosh²t dΩ²₂], x ∈ R | (section I intro) |
| Klein-Gordon equation | [∂²_t + 2 tanh t ∂_t − (1/cosh²t)Δ_S² + L] u = 0 | Eq. (I.1) |
| KK Hamiltonian mode | L_{M,n} = −(1/sinh 2x)∂_x(sinh 2x ∂_x) + (M² + n²)cosh²x + n² coth²x | (section I) |
| Profile equation | [∂²_t − (1/cosh²t)Δ_S² + L − 1] v = 0 where v = (cosh t) u | (section VI) |

## Relevance to Phonon-Exflation

Witten's bubble of nothing is the classical reference for the gravitational instability of a compactified extra dimension — a vacuum decay channel where the Kaluza-Klein circle pinches off and the 4D universe dissolves into nothing. The phonon-exflation framework must address whether the Jensen-deformed SU(3) fiber is stable against such a semiclassical nucleation process, and the framework's answer is that the fermionic content of the spectral triple (Dirac operator D_K spinors satisfying KO-dim 6 conditions and providing a stability energy) may stabilize the fiber. The technical content of this paper — the Kaluza-Klein tower decomposition of scalar waves on the Witten spacetime into modes on dS³ with effective mass √(M² + n²), where n labels the KK mode — is precisely the mechanism the framework invokes for mass generation from the internal fiber eigenvalue spectrum. The "weakly traversable" property of the Hawking wormhole (null fields cross but timelike fields stay localized) is a direct dynamical model for the framework's acoustic white hole at the fold. This paper substitutes for Witten 1982, whose bubble-of-nothing construction is the classical argument for extra-dimensional instability that the framework must circumvent.
