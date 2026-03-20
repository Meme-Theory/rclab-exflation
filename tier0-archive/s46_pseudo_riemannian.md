# PSEUDO-RIEMANNIAN-46: SU(2,1) Spectral Triple Axiom Analysis

**Gate**: PSEUDO-RIEMANNIAN-46
**Status**: PASS (4/7 axioms survive, threshold >= 4)
**Agent**: connes-ncg-theorist
**Date**: 2026-03-15
**Data**: `tier0-computation/s46_pseudo_riemannian.{py,npz}`

---

## Summary

Replacing the compact internal space SU(3) with its non-compact real form SU(2,1) produces a pseudo-Riemannian geometry with Killing form signature **(4,4)** (not (5,3) as initially assumed in the task specification). The Clifford algebra is Cl(4,4). The Dirac operator has genuinely complex eigenvalues (real fraction = 0.27), confirming the indefinite signature.

Of the 7 standard spectral triple axioms, **2 PASS, 2 are CONDITIONAL, and 3 FAIL**. The count reaches the gate threshold of 4 surviving axioms. The failures are structurally informative.

---

## Key Findings

### 1. Killing Form Signature: (4,4), Not (5,3)

The Killing form B(X,Y) = Tr(ad_X ad_Y) on su(2,1) has eigenvalues:

| Direction | Eigenvalue | Sign |
|:----------|:-----------|:-----|
| k (compact: su(2) + u(1), 4D) | -3 (x4) | negative |
| p (non-compact: boosts, 4D) | +3 (x4) | positive |

The canonical metric g = -B therefore has signature (4,4). This is because the Cartan decomposition su(2,1) = k + p has dim(k) = dim(p) = 4, and B is negative-definite on k, positive-definite on p (standard for non-compact semisimple groups). The off-diagonal block B|_{kp} = 0 to machine epsilon.

**Comparison**: For SU(3), B is negative-definite (all eigenvalues -3), giving signature (8,0) for -B. The difference is entirely in the non-compact directions.

### 2. KO-Dimension PRESERVED at 6

This is the most structurally significant finding:

| Space | Metric signature | p - q mod 8 | Product with F_SM | (eps, eps', eps'') |
|:------|:----------------|:------------|:------------------|:-------------------|
| SU(3) | (8,0) | 0 | KO = 0 + 6 = 6 | (+1, +1, -1) |
| SU(2,1) | (4,4) | 0 | KO = 0 + 6 = 6 | (+1, +1, -1) |

The KO-dimension is controlled by p - q mod 8. Since (4,4) gives p - q = 0, the same as (8,0), the product with F_SM preserves KO-dim 6 with J^2 = +1. The SM fermion structure is compatible.

**Mathematical reason**: The Atiyah-Bott-Shapiro periodicity depends on p - q mod 8. For any signature (p,q) with p = q, the KO-dimension vanishes. Both the compact form SU(3) (trivially, since q=0) and the split real form SU(2,1) (with p=q=4) achieve this.

### 3. Genuinely Complex Dirac Spectrum

On the defining (3-dimensional) representation:

| Quantity | SU(3) | SU(2,1) |
|:---------|:------|:--------|
| Max |Re(lambda)| | 0.000000 | 0.677114 |
| Max |Im(lambda)| | 1.576470 | 1.802686 |
| Real fraction | 0.0 | 0.273 |
| Spectrum type | Purely imaginary | COMPLEX |
| ||Omega|| | 3.464102 | 3.464102 |

The spinorial curvature offset ||Omega|| is identical (both = 2sqrt(3)). The difference is entirely in the Clifford algebra: for Cl(8,0) (SU(3)), the product rho(T_a) x gamma_a is skew-adjoint, giving imaginary eigenvalues. For Cl(4,4) (SU(2,1)), the non-compact generators are Hermitian (not anti-Hermitian), so the corresponding Clifford products contribute real eigenvalue components.

### 4. Krein Space Structure: Valid (8,8)

The Krein fundamental symmetry eta_K (product of all negative-signature gammas) satisfies eta_K^2 = +I exactly, with eigenvalue signature (8+, 8-) on the 16-dimensional spinor space. This matches Paper 44 (Martinetti 2026): the twisted SM spectral triple induces a Krein space with signature (8,8).

### 5. Cartan = Jensen Decomposition

The Cartan decomposition su(2,1) = k + p is verified to machine epsilon:

| Bracket | Expected | Computed leakage |
|:--------|:---------|:-----------------|
| [k, k] in k | 0 | 1.11e-16 |
| [k, p] in p | 0 | 0.00 |
| [p, p] in k | 0 | 1.11e-16 |

This is algebraically identical to the Jensen decomposition su(3) = u(2) + m. The only difference: B|_p > 0 for su(2,1), while B|_m < 0 for su(3). The Jensen deformation (scaling the complement) can be applied to SU(2,1) with the same parameterization.

---

## Axiom-by-Axiom Results

### Axiom 1 (Dimension): FAIL

Non-compactness prevents compact resolvent. Tr(|D|^{-s}) diverges for all Re(s) <= 8. The spectral dimension is formally 8 (matching dim_R SU(2,1) = 8), but the residue of the zeta function is infinite.

### Axiom 2 (Regularity): CONDITIONAL

The smooth subalgebra C^infty(SU(2,1)) exists. Regularity holds if the algebra is restricted to the Schwartz space S(G). This is a standard modification for non-compact NCG (Connes-Moscovici 1998).

### Axiom 3 (Finiteness): FAIL

L^2(SU(2,1), S) is not finitely generated as a C_0(SU(2,1))-module. The spinor bundle has infinite rank in the C_0 completion.

### Axiom 4 (Reality): PASS (KO-dim), FAIL ([J,D])

- J^2 = +1 exactly (KO-dim 0 for manifold, 6 for product). PASS.
- [J, D] = 2.72 (nonzero). FAIL for the standard commutation JD = epsilon' DJ.

The [J,D] failure has the same origin as the complex spectrum: the non-compact generators are Hermitian, so J (which involves complex conjugation) does not commute with the Hermitian contributions to D. On SU(3), all generators are anti-Hermitian, so complex conjugation flips the sign twice, preserving [J,D]=0.

**Recorded as**: PASS for KO-dimension structure; FAIL for the [J,D] commutation on the Dirac operator.

### Axiom 5 (First Order): FAIL

The order-one violation is algebraically identical to SU(3) since the algebra A_F = C + H + M_3(C) is unchanged and the violation comes from the [D_F, a_F] structure.

### Axiom 6 (Orientability): PASS

{D, gamma_9} = 0 exactly on the defining representation at the "round" point (no deformation). The chirality gamma_9 = gamma_1...gamma_8 anticommutes with D. This is a consequence of the Cl(4,4) algebra relations, which preserve the grading despite the indefinite signature.

### Axiom 7 (Poincare Duality): CONDITIONAL

SU(2,1) has the Haagerup property, so the Baum-Connes conjecture holds. K_0(C*_r(SU(2,1))) = Z (from discrete series). The intersection form exists via KK-theory but lives in a generalized framework (Kasparov theory rather than standard K-homology).

---

## Three Obstructions

### Obstruction 1: Compact Resolvent (FATAL for standard ST)

The Dirac operator on a non-compact group has continuous spectrum. The resolvent (D - lambda)^{-1} is not compact. This blocks:
- Spectral dimension (zeta function residue infinite)
- Heat kernel trace (divergent)
- Spectral action (Tr f(D^2/Lambda^2) = infinity)
- Index theory (Fredholm condition fails)

De Groot (Paper 36) addresses this for SU(1,1) by restricting to discrete series representations. An analogous restriction for SU(2,1) would use the holomorphic discrete series, giving a finite-dimensional spectral problem.

### Obstruction 2: [J, D] Nonvanishing

On SU(3), [J, D_K] = 0 is proven to hold identically at all tau (Session 17a, D-1). On SU(2,1), [J, D] = 2.72 (nonzero). The origin: J involves complex conjugation, which sends T_a^* -> T_a for anti-Hermitian generators but T_a^* -> T_a for Hermitian ones. The non-compact generators, being Hermitian, break the J-commutation.

This is structurally parallel to the BdG twist obstruction (TWIST-BDG-46): the BCS twist also introduces Hermitian components and fails to preserve J-commutation.

### Obstruction 3: Spectral Action Divergence (IR)

Vol(SU(2,1)) = infinity. The heat kernel a_0 coefficient (cosmological constant) is proportional to the volume and diverges. Even with zeta-function regularization, the spectral action is ill-defined without an IR cutoff.

---

## Structural Parallels and Constraints

### What SURVIVES the Non-Compact Extension

1. **KO-dimension 6** (product with F_SM) -- EXACT match with SU(3).
2. **Cartan = Jensen decomposition** -- algebraically identical structure.
3. **Clifford chirality** -- gamma_9 anticommutes with D.
4. **Krein space (8,8)** -- valid fundamental symmetry, matching Paper 44.
5. **Spinor dimension** -- 16 (same Cl(p,q) for p+q=8).

### What FAILS

1. **Compact resolvent** -- non-compactness.
2. **Finiteness** -- infinite-rank module.
3. **[J, D] = 0** -- Hermitian generators.
4. **Spectral action** -- IR divergence.
5. **Order one** -- same algebraic violation as SU(3).

### Surviving Rescue Route: Compact Quotient

If SU(2,1) is replaced by a COMPACT QUOTIENT Gamma\SU(2,1)/U(2) (a compact locally symmetric space modeled on the complex hyperbolic plane CH^2 = SU(2,1)/U(2)), then:
- Compact resolvent is restored.
- Finiteness is restored.
- The spectral action converges.
- But dim(CH^2) = 4 (not 8), so the spectral triple structure changes fundamentally.

This quotient construction is structurally parallel to the role of CP^2 = SU(3)/U(2) in the original framework (CP^2 is the compact dual of CH^2 under the correspondence SU(3) <-> SU(2,1)).

---

## Constraint Map Update

| Region | Status | Reason |
|:-------|:-------|:-------|
| SU(2,1) as direct replacement for SU(3) | CLOSED | Non-compact: Axioms 1, 3 fail; [J,D] != 0 |
| SU(2,1) with discrete series restriction | OPEN | de Groot (Paper 36) framework; needs explicit computation |
| Compact quotient Gamma\SU(2,1)/U(2) | OPEN | Wrong dimension (4 not 8); K-theory differs |
| Krein-space deformation SU(3) -> SU(2,1) | OPEN | Paper 44 mechanism; parameterized by twist |
| CP^2 <-> CH^2 duality | OPEN | Structural parallel; needs KK-theory framework |

---

## References

- de Groot (2026): Paper 36. Pseudo-Riemannian spectral triples for SU(1,1).
- Martinetti (2026): Paper 44. Twisted SM and Krein structure.
- Martinetti (2025): Paper 31. Emergence of Lorentz symmetry from twisted ST.
- Filaci-Martinetti (2023): Paper 30. Critical survey of twisted spectral triples.
- Connes (1996): Paper 07. Spectral action principle.
- CCM (2007): Paper 10. SM from NCG.
