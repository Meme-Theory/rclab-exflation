# Ricci identities in higher dimensions

**Author(s):** M. Ortaggio, V. Pravda, A. Pravdova
**Year:** 2007
**Journal:** Class. Quantum Grav. (arXiv preprint gr-qc/0701150, v3 dated 21 Feb 2012)
**arXiv:** gr-qc/0701150
**Relevance:** MEDIUM

---

## Abstract

We explore connections between geometrical properties of null congruences and the algebraic structure of the Weyl tensor in n > 4 spacetime dimensions. First, we present the full set of Ricci identities on a suitable "null" frame, thus completing the extension of the Newman-Penrose formalism to higher dimensions. Then we specialize to geodetic null congruences and study specific consequences of the Sachs equations. These imply, for example, that Kundt spacetimes are of type II or more special (like for n = 4) and that for odd n a twisting geodetic WAND must also be shearing (in contrast to the case n = 4).

---

## Key Arguments and Derivations

The paper completes the n > 4 extension of the Newman-Penrose formalism by deriving all frame Ricci identities. In an n-dimensional Lorentzian spacetime the authors set up a "null" frame of two null vectors m^(0) = n, m^(1) = ℓ and n-2 orthonormal spacelike vectors m^(i) with ℓ·n = 1 and m^(i)·m^(j) = δ_ij. Ricci rotation coefficients L_ab, N_ab, M^i_ab are defined via ℓ_{a;b} = L_cd m^(c)_a m^(d)_b etc. Orthogonality reduces these to n^2(n-1)/2 independent scalars.

Section 3 gives the full set of Ricci identities (11a)-(11p), each obtained by contracting v_{a;bc} - v_{a;cb} = R_{sabc} v^s with frame vectors for v = ℓ, n, m^(i). These equations are written in 16 distinct boost-weight sectors and include Weyl components C_{abcd}, Ricci components R_{ab}, and the Ricci scalar R.

Section 4 specializes to geodetic null congruences (L_i0 = 0). The matrix L_ij becomes gauge-invariant under null rotations preserving ℓ and decomposes into shear σ_ij (tracefree symmetric), expansion θ (trace), and twist A_ij (antisymmetric). Setting L_i0 = L_10 = 0 in identity (11g) and decomposing gives the n-dimensional Sachs equations (15a)-(15c). Equations (15b) and (15c) give propagation of θ, ω^2 along ℓ:
Dσ_ij = -(σ^2_ij - (1/(n-2))σ^2 δ_ij) - (A^2_ij + (1/(n-2))ω^2 δ_ij) - 2θσ_ij - 2σ_{k(i} M^k_{j)0} - C_{0i0j}
Dθ = -(1/(n-2))σ^2 - θ^2 + (1/(n-2))ω^2 - (1/(n-2))R_{00}
DA_ij = -2θA_ij - 2σ_{k[j} A_{i]k} + 2A_{k[i} M^k_{j]0}

Section 4.2 derives several consequences: Proposition 1 states that if R_00 = 0 and the congruence is non-expanding and either shearfree or twistfree, then it must automatically be both shearfree AND twistfree, and is a WAND (C_{0i0j} = 0). Proposition 2 shows Kundt spacetimes (L_i0 = L_ij = 0) are of Petrov type II or more special when R_00 = R_0i = 0. Proposition 3 is the striking higher-dimensional counterexample to a naive Goldberg-Sachs: for odd n > 4, a twisting geodetic WAND must be shearing (because A^2_ij + (1/(n-2))ω^2 δ_ij = 0 forces A_ij = 0 for odd n since det(A^2_ij) vanishes). Myers-Perry black holes in n=5 provide an explicit example of a type-D twisting shearing spacetime. Proposition 4: in type G spacetimes, a shearfree geodetic null congruence must be twisting unless it is a WAND.

## Key Results

1. Complete extension of Newman-Penrose Ricci identities to n >= 4 dimensions, equations (11a)-(11p), organized by boost-weight sectors.
2. n-dimensional Sachs equations for the propagation of shear, expansion, and twist of a geodetic null congruence (equations 15a-c), reducing to the standard 4d Sachs equations when n=4.
3. Proposition 1: With R_00 = 0, non-expanding + shearfree <=> non-expanding + twistfree <=> Kundt class, and the congruence is automatically a WAND.
4. Proposition 2: Under R_00 = R_0i = 0, n >= 4 Kundt spacetimes are algebraically special of type II or more special.
5. Proposition 3: For odd n > 4, a twisting geodetic WAND must also be shearing (counterexample to a full higher-dimensional Goldberg-Sachs theorem); Myers-Perry n=5 black holes realize this.
6. Proposition 4: In type G (algebraically general) n > 4 spacetimes, a shearfree geodetic null congruence is necessarily twisting (unless it is a WAND).
7. Integrated optical scalars for σ = R_00 = 0 case: θ(r) and ω(r) take rational forms in affine parameter r, reducing to the Podolsky-Ortaggio result in the non-twisting limit.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Metric in null frame | g_ab = 2 ℓ_(a n_b) + δ_ij m^(i)_a m^(j)_b | (1) |
| Rotation coefficient definitions | ℓ_{a;b} = L_cd m^(c)_a m^(d)_b, etc. | (2) |
| Orthogonality constraints | L_{0a} = N_{1a} = N_{0a} + L_{1a} = M^i_{0a} + L_{ia} = M^i_{ja} + M^j_{ia} = 0 | (3) |
| Covariant frame derivatives | D ≡ ℓ^a ∇_a, Δ ≡ n^a ∇_a, δ_i ≡ m^{(i)a} ∇_a | (4) |
| Ricci identity (boost weight 2) | Dρ_ij - κ sample: DL_ij - δ_j L_i0 = L_10 L_ij - ... - C_{0i0j} - (1/(n-2)) R_00 δ_ij | (11g) |
| Shear/expansion/twist decomposition | L_ij = σ_ij + θ δ_ij + A_ij | (12) |
| Optical scalars | σ^2 = ℓ_(a;b) ℓ^(a;b) - (1/(n-2))(ℓ^a_{;a})^2, θ = (1/(n-2)) ℓ^a_{;a}, ω^2 = ℓ_[a;b] ℓ^{a;b} | (14) |
| Sachs equation (shear) | Dσ_ij = -(σ^2_ij - (1/(n-2))σ^2 δ_ij) - (A^2_ij + (1/(n-2))ω^2 δ_ij) - 2θσ_ij - 2σ_{k(i} M^k_{j)0} - C_{0i0j} | (15a) |
| Sachs equation (expansion) | Dθ = -(1/(n-2))σ^2 - θ^2 + (1/(n-2))ω^2 - (1/(n-2)) R_00 | (15b) |
| Sachs equation (twist) | DA_ij = -2θ A_ij - 2σ_{k[j} A_{i]k} + 2 A_{k[i} M^k_{j]0} | (15c) |
| Integrated expansion | θ = (θ_0 + r(θ_0^2 + (1/(n-2))ω_0^2))/(1 + 2rθ_0 + r^2(θ_0^2 + (1/(n-2))ω_0^2)) | (17) |

## Relevance to Phonon-Exflation

The phonon-exflation framework operates in D=10 (M4 × SU(3)) where Petrov/Goldberg-Sachs-style questions become genuinely higher-dimensional. Proposition 3 is the most directly relevant structural result: in odd dimensions > 4, twisting multiple WANDs must be shearing, which constrains any analog of a Birkhoff-rigidity theorem for the substrate. The block-diagonality theorem for D_K on Jensen-deformed SU(3) (framework-side analog of Birkhoff rigidity) should be checked for consistency with the Kundt-class characterization (Proposition 2) when the 10D effective spacetime is sliced. The Sachs equations (15a-c) are the higher-D generalization of the null-congruence-focusing equations that Hawking uses when proving the area theorem; in the substrate picture the area theorem is Level-3 emergent from spectral monotonicity, so these Sachs equations represent how the emergent geometry propagates information from the fiber's spectral reorganization toward the 4D observable physics.
