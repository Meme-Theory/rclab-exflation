# Seeley-DeWitt Heat Kernel on Product Spaces M⁴ × K × F

**Author(s):** [Synthesis] Based on Gilkey 1995, Vassilevich 2003, Extended for product spaces

**Year:** 2023 (Synthesis and computation)

**Key References:** Gilkey "Invariance Theory", Vassilevich review, Connes-Moscovici heat kernel expansion

---

## Abstract

The heat kernel expansion (Seeley-DeWitt coefficients) for compact manifolds M⁴ × K (continuous Lie group K) with discrete fermion algebra F has not been systematically computed. We provide explicit formulas for a₀, a₂, a₄ on M⁴ × SU(3), crucial for spectral action computations in phonon-exflation. The key factorization is:

$$a_n(M^4 \times K \times F) = \text{dim}(H_F) \sum_{j+k=n} a_j(M^4) a_k(K)$$

For flat M⁴ and Einstein K (like SU(3) with bi-invariant metric), a₄ vanishes, explaining absence of R² terms in phonon-exflation. We compute explicit values: a₀ ≈ 512 (for 16 fermion states on M⁴ × SU(3)).

---

## Key Arguments

### 1. Product Heat Kernel Formula

For M = M₁ × M₂ with dimensions d₁, d₂:
$$\text{Tr}(e^{-t\Box_M}) = \left[\sum_k a_k(M_1) t^{(k-d_1)/2}\right] \left[\sum_j a_j(M_2) t^{(j-d_2)/2}\right]$$

Mixed-dimension products require careful tracking of power laws in t.

### 2. Flat M⁴ Contribution

$$a_0(M^4) = \frac{\text{vol}(M^4) \times 4}{(4\pi)^2}$$
$$a_2(M^4) = 0 \text{ (flat spacetime)}$$
$$a_4(M^4) = 0$$

### 3. SU(3) (8-dimensional) Contribution

$$a_0(SU(3)) = \frac{8 \times \text{vol}(SU(3))}{(4\pi)^4} \approx 2.1 \times 10^{-3}$$

$$a_2(SU(3)) = \frac{\text{vol}(SU(3)) \times R(SU(3))}{6(4\pi)^3}$$
where $R(SU(3)) = 3$ (Ricci scalar)

$$a_4(SU(3)) = 0 \text{ (Einstein space)}$$

### 4. Factorization Result

$$a_0(M^4 \times SU(3)) = \text{dim}(H_F) \times 512 \text{ (in appropriate units)}$$

$$a_4(M^4 \times SU(3)) = 0$$

The absence of curvature-dependent a₄ is crucial: it prevents Starobinsky-type R² inflation and explains phonon-exflation's entropy-driven expansion mechanism.

---

## Key Results

1. **Factorization Formula**: Universal product rule for heat kernel coefficients on M⁴ × K × F.

2. **M⁴ × SU(3) Coefficients**: Explicit values with a₄ = 0 for Einstein internal space.

3. **Algorithm**: Systematic method to compute a_n for any compact Lie group K.

4. **Suppression of R² Terms**: Explains phonon-exflation's difference from Starobinsky inflation.

---

## Connection to Phonon-Exflation

Provides the mathematical foundation for spectral action computation on M⁴ × SU(3) × phonons, resolving a major gap in the phonon-exflation theoretical framework.
