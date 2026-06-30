# Generalization of the Geroch-Held-Penrose formalism to higher dimensions

**Author(s):** Mark Durkee, Vojtech Pravda, Alena Pravdova, Harvey S. Reall
**Year:** 2010
**Journal:** arXiv preprint (later Class. Quantum Grav.)
**arXiv:** 1002.4826
**Relevance:** LOW

---

## Abstract

Geroch, Held and Penrose invented a formalism for studying spacetimes admitting one or two preferred null directions. This approach is very useful for studying algebraically special spacetimes and their perturbations. In the present paper, the formalism is generalized to higher-dimensional spacetimes. This new formalism leads to equations that are considerably simpler than those of the higher-dimensional Newman-Penrose formalism employed previously. The dynamics of p-form test fields is analyzed using the new formalism and some results concerning algebraically special p-form fields are proved.

---

## Key Arguments and Derivations

The authors generalize the 4D Geroch-Held-Penrose (GHP) formalism to arbitrary d >= 4. The d-dim NP frame has two null vectors ℓ = e_(0), n = e_(1) and d-2 spacelike m_(i) with ℓ·n = 1, m_(i)·m_(j) = δ_ij, and orthogonality constraints N_0a + L_1a = 0, M^i_0a + L_ia = 0, etc. Geodesy of ℓ is encoded by κ_i ≡ L_i0 = 0 and optics by ρ_ij ≡ L_ij (expansion, shear, twist from trace/tracefree-symmetric/antisymmetric parts).

Section 2.2 defines GHP scalars: objects transforming covariantly under SO(d-2) spatial rotations (spins, T_{i_1...i_s} → X_{i_1 j_1}...X_{i_s j_s} T_{j_1...j_s}) and under boosts (ℓ → λℓ, n → λ^{-1} n, m_(i) → m_(i)), with boost weight b scaling T → λ^b T. Most NP scalars become GHP scalars except L_10, L_11, L_1i (which fail boost covariance) and M^i_j0, M^i_j1, M^i_jk (which fail spin covariance). Table 1 assigns names: ρ_ij, ρ, κ_i, τ_i (boost weight 1, 2, 0, 0 resp.) for derivatives of ℓ, and primed versions ρ'_ij, ρ', κ'_i, τ'_i for derivatives of n.

Section 2.3 defines GHP derivative operators þ (thorn), þ' (thorn-prime), δ_i (eth) which add connection terms to compensate for the non-covariance of NP derivatives:
þ T_{i_1...i_s} = D T_{i_1...i_s} - b L_10 T_{i_1...i_s} + Σ_r M^k_{i_r 0} T_{i_1...k...i_s}
and similarly for þ' and δ_i. These are GHP covariant, obey Leibniz, and are metric for δ_ij.

Section 2.4 decomposes the Weyl tensor by boost weight and spin (Table 2): Ω_ij (bw 2), Ψ_ijk, Ψ_i (bw 1), Φ_ijkl, Φ_ij, Φ (bw 0), Ψ'_ijk, Ψ'_i (bw -1), Ω'_ij (bw -2). The Ricci tensor is similarly decomposed (Table 3): ω, ψ_i, φ_ij, φ, ψ'_i, ω' with boost weights 2, 1, 0, 0, -1, -2.

Section 2.5 reviews the higher-d Petrov classification via WANDs (Weyl-aligned null directions killing bw+2 components) and multiple WANDs (killing bw+2 and +1). Types O, N, III, II, I, G correspond to progressively weaker alignment.

Section 2.6 derives the transformation of all GHP scalars under null rotations with ℓ fixed (equations 2.21-2.35). Section 2.7 describes the priming operation that exchanges ℓ ↔ n, which halves the number of independent NP/Bianchi equations when symmetry is unbroken.

Section 2.8 presents the GHP-form Newman-Penrose equations for any matter content (equations NP1-NP4), which are dramatically simpler than the direct NP versions. Section 2.9 gives the GHP Bianchi equations for Einstein spacetimes.

Later sections (not fully extracted) analyze Maxwell (p-form) test fields in the GHP formalism, prove that a null vector field multiply aligned with a nonzero Maxwell field must be geodesic with a specific shear constraint, and show that for d > 4 this shear constraint is incompatible with multiple alignment to the Weyl tensor of Schwarzschild (except possibly for d = even with p = d/2).

## Key Results

1. A higher-dimensional GHP formalism defined for any d >= 4, dramatically reducing the complexity of the NP and Bianchi equations.
2. GHP derivatives þ, þ', δ_i are defined, shown to be GHP-covariant, Leibniz, and metric-compatible.
3. The Weyl tensor is decomposed into ten independent sets (Ω, Ψ, Ψ_i, Φ_ijkl, Φ_ij, Φ, Ψ', Ψ'_i, Ω') indexed by boost weight and spin.
4. The priming operation (ℓ ↔ n) halves the number of independent field and Bianchi equations when symmetry is preserved (e.g., in type D).
5. NP/Ricci-identity equations are presented in four compact boost-weight sectors (NP1-NP4) plus their primes.
6. For d > 4, the condition for a vector field to be multiply aligned with a nonzero Maxwell test field (geodesic, with specific shear) is incompatible with being a multiple WAND of the Schwarzschild Weyl tensor, except possibly for even d with a rank-d/2 Maxwell field.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Frame basis | {ℓ = e_(0) = e^(1), n = e_(1) = e^(0), m_(i) = e_(i) = e^(i)} | (2.1) |
| Rotation-coefficient definitions | L_μν = ∇_ν ℓ_μ, N_μν = ∇_ν n_μ, M^i_μν = ∇_ν m_(i)μ | (2.3) |
| Orthogonality | N_0a + L_1a = M^i_0a + L_ia = M^i_1a + N_ia = M^i_ja + M^j_ia = 0 | (2.4) |
| Geodesy | κ_i ≡ L_i0 = 0 | (2.6) |
| Optics matrix | ρ_ij ≡ L_ij | (2.7) |
| GHP scalar under spin | T_{i_1...i_s} → X_{i_1 j_1} ... X_{i_s j_s} T_{j_1...j_s} | (2.11) |
| GHP scalar under boost | T_{i_1...i_s} → λ^b T_{i_1...i_s} | (2.12) |
| GHP þ derivative | þ T = D T - b L_10 T + Σ_r M^k_{i_r 0} T (indices-shifted) | (2.15) |
| GHP þ' derivative | þ' T = Δ T - b L_11 T + Σ_r M^k_{i_r 1} T | (2.16) |
| GHP δ_i derivative | δ_i T = δ_i T - b L_1i T + Σ_r M^k_{j_r i} T | (2.17) |
| NP equation (bw+2) | þ ρ_ij - δ_j κ_i = -ρ_ik ρ_kj - κ_i τ'_j - τ_i κ_j - Ω_ij - (1/(d-2)) ω δ_ij | (NP1) |
| NP equation (bw+1 single) | þ τ_i - þ' κ_i = ρ_ij(-τ_j + τ'_j) - Ψ_i + (1/(d-2)) ψ_i | (NP2) |
| NP equation (bw+1 pair) | δ_{[j|} ρ_{i|k]} = τ_i ρ_{[jk]} + κ_i ρ'_{[jk]} - (1/2) Ψ_ijk - (1/(d-2)) ψ_{[j} δ_{k]i} | (NP3) |
| NP equation (bw 0) | þ' ρ_ij - δ_j τ_i = -τ_i τ_j - κ_i κ'_j - ρ_ik ρ'_kj - Φ_ij - (1/(d-2))(φ_ij + φ δ_ij) + ... | (NP4) |

## Relevance to Phonon-Exflation

The framework operates in D=10 (M4 × SU(3)), so any higher-D GHP machinery could in principle be used to analyze the emergent effective 10D or 4D+6D gravitational sector once one projects the spectral-action gradient onto a metric description. However, the direct utility is limited because the phonon-exflation framework derives gravity as an emergent consequence of the a_2 Seeley-DeWitt coefficient (Level-2 emergent) rather than starting from a Lorentzian metric and finding its WANDs. If one ever needs to connect the substrate picture to 10D classical GR solutions (e.g., to compare the fold transit to a higher-dimensional black-hole interior), then the GHP priming operation and the simplified NP1-NP4 equations would provide the cleanest classical-geometry reference frame. For twistor-based analyses of U(1)_7 KK gauge fields, the Durkee et al. Weyl-decomposition table is also useful for classifying which boost-weight components survive in D=10 black-hole-like solutions.
