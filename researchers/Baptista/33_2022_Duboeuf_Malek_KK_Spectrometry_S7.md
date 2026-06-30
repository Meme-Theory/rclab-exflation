# Kaluza-Klein Spectrometry beyond Consistent Truncations: The Squashed S^7

**Author(s):** Bastien Duboeuf, Emanuel Malek, Henning Samtleben
**Year:** 2022 (revised 2023)
**Journal:** JHEP 04 (2023) 062
**arXiv:** 2212.01135
**Relevance:** HIGH (Full KK spectrum of squashed S^7 via ExFT; universal conformal dimension formula; first computation beyond consistent truncation)

---

## Abstract

We show how to use Exceptional Field Theory to compute the full Kaluza-Klein spectra of 10- and 11-dimensional supergravity around deformations of backgrounds of maximal gauged supergravity by scalar modes that do not form part of the consistent truncation. This includes deformations of AdS_4 x S^7 and AdS_5 x S^5 by modes that are not part of the N = 8 supermultiplet. As an application, we compute the full Kaluza-Klein spectrum of the N = 1 and N = 0 squashed S^7. In this example, all conformal dimensions are captured by a universal formula in terms of the Casimir operators and additional quantum numbers which organise the spectrum.

---

## Key Arguments and Derivations

### 1. Extension Beyond Consistent Truncations (Section 3)

The paper extends the ExFT KK spectrometry method of Malek-Samtleben (2019-2020) to vacua that are NOT part of the N = 8 consistent truncation. The key insight is that continuous deformations preserve generalised parallelisability (a topological condition), even when they exit the N = 8 truncation.

**Generalised parallelisable:** Globally well-defined twist matrix U_M^A and scalar density rho.

**Generalised Leibniz parallelisable (stronger):** Additionally satisfies L_{U_A} U_B^M = X_{ABC} U_C^M with CONSTANT intrinsic torsion X_{ABC}. This implies a consistent truncation to maximal supergravity.

For the squashed S^7: The background is generalised parallelisable but NOT Leibniz parallelisable. The intrinsic torsion X_{ABC}(y) depends on the internal coordinates.

### 2. Fluctuation Ansatz (Section 3.1)

KK fluctuations are expanded via the twist matrix:

V(x,y) = U(y) (I + P^I sum_Sigma j_{I,Sigma}(x) Y_Sigma(y))

where Y_Sigma(y) are scalar harmonics. The non-constant intrinsic torsion causes **level mixing** (space-invader scenario) compared to the round S^7.

**Quadratic constraints** from the section condition link X^2, dX, Xd, and d^2 terms:

d_C X_{ABC} = 0  (for theta_A = 0)
2 d_{[A} d_{B]} - X_{ABC} d_C = 0

### 3. Mass Operators (Section 3.3)

**Spin-2 mass operator:**
M_{spin-2} = -d_A d_A + (theta_A)^2

**Spin-1 mass operators:** Two coupled operators for vector fluctuations, involving X_{ABC} and d_A.

**Spin-0 mass operator:** The 70 scalar fluctuations have mass operator:

(M_{spin-0})_{IJ} = M^{(0)}_{IJ} + (N_{IJC} - N_{JIC}) d_C + d_C N_{IJC} + delta_{IJ} M_{spin-2}

where M^{(0)}_{IJ} contains X^2 terms and N_{IJC} contains linear X terms. These generalize the constant-X formulas of Malek-Samtleben by including dX contributions.

### 4. The Squashed S^7 in ExFT (Section 4.1)

The S^7 is represented as the coset:

S^7 = (Sp(2) x Sp(1)_0) / (Sp(1)_L x Sp(1)_D)

The consistent truncation retaining Sp(2) x Sp(1) singlets is:

V(x,y) = U_round(y) exp[sum_singlets phi_i(x) s^{I,Sigma}_i P_I Y_Sigma(y)]

with scalar target space SL(2)/SO(2) x SL(2)/SO(2).

Four Sp(2) x Sp(1) singlet scalars sit at KK levels 0, 2, 4:
- l = 0: [0,0,2,0]_2
- l = 2: [0,0,0,0]_6 + [0,2,0,0]_4
- l = 4: [2,0,0,2]_6

### 5. Universal Conformal Dimension Formula (Section 4.2)

The N = 1 KK spectrum on the left-squashed S^7 organizes into long N = 1 supermultiplets L[J, Delta]. The conformal dimension of the superconformal primary is:

**Eq. (1.1):**
Delta = 1 + (5/3)s + (1/3) sqrt{(3J + 2s^2)^2 + 5C_3}

where:
- J = spin of the primary
- C_3 = C(p,q) + 3C(r) = (1/2)(p^2 + 2q^2 + 4p + 6q + 2pq) + (3/4)r(r+2) for Sp(2) x Sp(1) representation [p,q,r]
- s in (1/2)Z is an additional R+ charge

**For most KK towers**, the range of s amounts to the L_z eigenvalues of fixed SL(2) representations, suggesting elevation of R+ to full SL(2).

### 6. Spectrum Organization (Section 4.2)

The KK spectrum organizes into towers:

[k,q,k] (k>1,q>1): L[3/2] x [0] + L[1] x [1/2] + L[1/2] x [1/2 x 1/2] + L[0] x [1/2 x 1]
[k,q,k+2] (k>0,q>1) & [k+2,q,k]: L[0] x [1/2] + L[1] x [1/2] + L[1/2] x [1/2 x 1/2]
[k,q,k+4] (q>1) & [k+4,q,k]: L[1/2] x [0] + L[0] x [1/2]

with degeneracies for small representations.

### 7. The Right-Squashed S^7 (Section 4.3)

The N = 0 right-squashed S^7 is obtained by orientation reversal (skew-whiffing). The conformal dimensions are modified:

Delta'_{J,s} = 1 + (5/3)s + (1/3) sqrt{(3J + 2s'^2)^2 + 5C_3}

where s' = s - 1 for towers with s > 0, and s' = -s - 1 for the s <= 0 components.

### 8. Rational Conformal Dimensions and Marginal Deformations (Section 4.4)

All conformal dimensions on the squashed S^7 are irrational except in a finite number of representations. The paper identifies potential marginal operators (Delta = 3) and finds that boundary conditions can be chosen to eliminate all marginal single-trace operators, consistent with the non-supersymmetric vacuum being perturbatively stable.

---

## Key Results

1. **Method extension**: First computation of full KK spectrum beyond consistent truncations, using generalized (non-Leibniz) parallelisability in ExFT.

2. **Universal formula** (Eq. 1.1): All conformal dimensions on the squashed S^7 captured by a single algebraic formula involving Casimirs and quantum numbers J, s.

3. **N = 1 squashed S^7 spectrum**: Complete organization into long N = 1 supermultiplets, with explicit tower structure.

4. **N = 0 right-squashed spectrum**: Complete spectrum obtained by skew-whiffing, relevant for AdS swampland conjecture.

5. **Perturbative stability**: Boundary conditions can be chosen to eliminate all marginal operators, supporting perturbative stability of the non-supersymmetric vacuum.

6. **Level mixing/space-invaders**: The squashed S^7 requires excitations from KK level l = 2 relative to the round S^7, causing level mixing in the spectrum.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Universal Delta | $\Delta = 1+\frac{5}{3}s+\frac{1}{3}\sqrt{(3J+2s^2)^2+5C_3}$ | Eq. (1.1) |
| Casimir combination | $C_3 = C(p,q)+3C(r) = \frac{1}{2}(p^2+2q^2+4p+6q+2pq)+\frac{3}{4}r(r+2)$ | Eq. (4.4) |
| Spin-2 mass operator | $M_{\mathrm{spin-2}} = -\partial_A\partial_A + (\vartheta_A)^2$ | Sec. 3.3.1 |
| Spin-0 mass operator | $(M_{\mathrm{spin-0}})_{IJ} = M^{(0)}_{IJ}+(N_{IJC}-N_{JIC})\partial_C+\partial_C N_{IJC}+\delta_{IJ}M_{\mathrm{spin-2}}$ | Eq. (3.11) |
| Gen. Lie derivative | $\mathcal{L}_\Lambda V^M = \Lambda^N\partial_N V^M - 12\partial_K\Lambda^L\mathbb{P}^{KL}{}_{MN}V^N+\lambda V^M\partial_N\Lambda^N$ | Eq. (2.3) |
| Non-constant torsion | $\mathcal{L}_{U_A}U_B{}^M = X_{ABC}(y)\,U_C{}^M$ | Eq. (3.3) |
| Quadratic constraint | $2\partial_{[A}\partial_{B]}-X_{ABC}\partial_C = 0$ | Eq. (3.17) |
| S^7 coset | $S^7 = \frac{Sp(2)\times Sp(1)_0}{Sp(1)_L\times Sp(1)_D}$ | Eq. (3.17) |
| KK singlet scalars | $\ell=0:[0,0,2,0]_2$; $\ell=2:[0,0,0,0]_6\oplus[0,2,0,0]_4$; $\ell=4:[2,0,0,2]_6$ | Eq. (3.15) |

---

## Relevance to Phonon-Exflation

This paper provides the **complete KK spectral technology** for the framework's S^7 (or SU(3)) compactification:

1. **Universal conformal dimension formula**: The formula Delta = 1 + (5/3)s + (1/3)sqrt{(3J+2s^2)^2 + 5C_3} is the ExFT analog of the framework's Dirac spectrum formula on SU(3). Both reduce the full KK tower to Casimir eigenvalues and quantum numbers. Comparing the two approaches (NCG spectral triple vs. ExFT KK spectrometry) would be a powerful cross-check.

2. **Beyond consistent truncation**: The framework's Jensen deformation takes the SU(3) fiber outside the N = 8 consistent truncation, exactly as the squashing takes S^7 outside. The paper's demonstration that ExFT still computes the full spectrum in this regime validates the approach for the framework's geometry.

3. **Non-constant intrinsic torsion = tau-dependent D_K**: The y-dependent X_{ABC}(y) on the squashed S^7 is the ExFT translation of the framework's tau-dependent Dirac operator D_K(tau). Both produce level mixing and space-invader phenomena.

4. **Perturbative stability analysis**: The elimination of marginal operators via boundary conditions is directly relevant to the framework's stability question. If analogous boundary conditions exist for the SU(3) compactification, they could resolve the stabilization problem identified in Sessions 36-38.

5. **SL(2) structure in the spectrum**: The surprising SL(2) organization of the quantum number s in the KK towers may have a counterpart in the framework's observation that the BCS pair vibration has a natural SL(2) structure (creation/annihilation of Cooper pairs).
