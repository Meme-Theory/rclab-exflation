# Supersymmetric spectroscopy on AdS$_4 \times S^7$ and AdS$_4 \times S^6$

**Author(s):** Mattia Cesaro, Gabriel Larios, Oscar Varela
**Year:** 2021 (v2: 2024)
**Journal:** arXiv preprint (IFT-UAM/CSIC-21-025)
**arXiv:** 2103.13408
**Relevance:** HIGH

---

## Abstract

New techniques based on Exceptional Field Theory have recently allowed for the calculation of the Kaluza-Klein spectra of certain AdS$_4$ solutions of $D=11$ and massive IIA supergravity. These are the solutions that consistently uplift on $S^7$ and $S^6$ from vacua of maximal four-dimensional supergravity with SO(8) and ISO(7) gaugings. In this paper, we provide an algorithmic procedure to compute the complete Kaluza-Klein spectrum of five such AdS$_4$ solutions, all of them $\mathcal{N}=1$, and give the first few Kaluza-Klein levels. These solutions preserve SO(3) and U(1)$\times$U(1) internal symmetry in $D=11$, and U(1) (two of them) and no continuous symmetry in type IIA. Together with previously discussed cases, our results exhaust the Kaluza-Klein spectra of known supersymmetric AdS$_4$ solutions in $D=11$ and type IIA in the relevant class.

---

## Key Arguments and Derivations

### 1. Introduction and Context

The paper addresses Kaluza-Klein (KK) perturbation spectra above AdS$_4$ backgrounds of string/M-theory. For Freund-Rubin solutions AdS$_4 \times M_7$ of $D=11$ supergravity, the complete KK spectrum encodes physical information about the solution. Traditional methods (coset-space harmonic analysis from [26]) become extremely difficult on warped, flux backgrounds. The authors use new Exceptional Field Theory (ExFT) techniques from [27] that bypass the need for the full higher-dimensional solution form.

The key advantage: the ExFT-based KK mass matrices depend only on data from $D=4$ $\mathcal{N}=8$ gauged supergravity (scalar vevs at critical points, embedding tensor) plus SO(8) or SO(7) generators. Knowledge of the full 10- or 11-dimensional solution is not required.

### 2. KK Mass Matrices (Section 2)

The mass matrices for bosonic and fermionic KK perturbations are derived from $E_{7(7)}$ ExFT:

- **KK gravitino mass matrix** (eq. 2.1): $A_{1\,i\Lambda,j\Sigma} = A_{1\,ij}\delta_{\Lambda\Sigma} - 8(V^{-1})_{ij}^M (T_M)_{\Lambda\Sigma}$
- **KK spin-1/2 mass matrix** (eq. 2.2): involves $A_3$ tensors and $\epsilon$-tensor contractions
- **KK graviton mass matrix** (eq. 2.3): $(M^2_{\text{grav}})_{\Lambda\Sigma} = M_{MN}\delta_{\Omega\Omega'}(T_M)_{\Lambda\Omega}(T_N)_{\Sigma\Omega'}$
- **KK vector mass matrix** (eq. 2.4): manifestly $E_{7(7)}$ covariant, involves X-symbols codifying the embedding tensor

The index $\Lambda$ runs over symmetric-traceless representations $[n,0,0,0]$ of SO(8) (or $[n,0,0]$ of SO(7)) at KK level $n = 0, 1, 2, \ldots$

Spurious states (magnetic vectors, Goldstone/Goldstino modes) must be removed. The empirical relation found:
$$L^2 M^2_{1\,\text{Goldstone}} = 3L^2 M^2_2 + 6, \quad LM_{1/2\,\text{Goldstino}} = 2LM_{3/2}$$

### 3. New Spectra of $\mathcal{N}=1$ Solutions (Section 3)

Five AdS$_4$ solutions are treated:

| Solution | Gauging | Residual symmetry $G$ | $g^{-2}V$ |
|:---------|:--------|:---------------------|:----------|
| $D=11$ | SO(8) | SO(3) | $-55.363855$ |
| $D=11$ | SO(8) | U(1)$\times$U(1) | $-48$ |
| IIA | ISO(7) | U(1) | $-25.697101$ |
| IIA | ISO(7) | U(1) | $-35.610235$ |
| IIA | ISO(7) | $\varnothing$ | $-35.598340$ |

Conformal dimensions are obtained via:
$$L^2 M^2_2 = \Delta_2(\Delta_2 - 3), \quad L^2 M^2_1 = (\Delta_1 - 1)(\Delta_1 - 2), \quad |LM_{3/2,1/2}| = \Delta_{3/2,1/2} - 3/2$$

Key findings per solution:
- **SO(3) solution**: No accidental degeneracies beyond SO(3) representation content. Spectrum shows qualitative OSp(4|1)$\times$SU(3)$\times$U(1)$_s$ structure, with branching via $\text{OSp}(4|8) \supset \text{OSp}(4|1) \times \text{SU}(3) \times \text{U}(1)_s \supset \text{OSp}(4|1) \times \text{SO}(3)$.
- **U(1)$\times$U(1) solution**: Degeneracies 1, 2, 4, 8, and 3 (accidental). Some analytic dimensions found.
- **U(1) solutions (IIA)**: Dimensions either non-degenerate or doubly degenerate from $\pm$ U(1) charges.
- **No-symmetry solution (IIA)**: Completely non-degenerate spectrum.

### 4. Further Discussion (Section 4)

No master formula of the type $E_0 = s_0^{(2)} - 1/2 + \sqrt{9/4 + s_0^{(2)}(s_0^{(2)}+1) - s_0(s_0+1) + \alpha\,n(n+d-1) + Q^2(R)}$ (eq. 4.1) governs these five spectra, unlike the previously studied $2 \le \mathcal{N} \le 8$ cases. The characteristic polynomials of mass matrices contain rational-irreducible factors of increasing degree with KK level (quadratic, cubic, quartic, sextic, degree-12 at levels $n = 1, 2, 3$).

An envelope ansatz $E_0^{\max}(n) = 1 + \sqrt{a_{\max} + b_{\max}n + c_{\max}n^2}$ fits well for GRAV multiplets, with $a_{\max} = 9/4$.

The minimal dimensions $E_0^{\min}(n)$ show non-monotonic behavior for CHIRAL multiplets in the SO(3) and some IIA solutions, qualitatively similar to non-supersymmetric cases.

---

## Key Results

1. **Complete KK spectra computed** for all five remaining $\mathcal{N}=1$ AdS$_4$ solutions in the relevant class, exhausting known supersymmetric cases.
2. **Algorithmic ExFT procedure** requiring only $D=4$ $\mathcal{N}=8$ supergravity data (scalar vevs, embedding tensor, SO(8)/SO(7) generators).
3. **Goldstone/Goldstino relation** (eq. 2.12) holds empirically at all KK levels for all solutions.
4. **No accidental degeneracies** in the SO(3) spectrum — unique among solutions with continuous residual symmetry (shared only with the $\mathcal{N}=8$ SO(8) solution).
5. **No master dimension formula** of the type (4.1) exists for these five spectra; characteristic polynomials have rational-irreducible factors of unbounded degree.
6. **Non-monotonic minimal scalar dimensions** in some spectra, suggesting potential non-supersymmetric ISO(7) vacua with perturbative instabilities at $n \ge 1$.
7. All spectra successfully organized into OSp(4|1) supermultiplets level by level, providing a consistency check.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Gravitino KK mass | $A_{1\,i\Lambda,j\Sigma} = A_{1\,ij}\delta_{\Lambda\Sigma} - 8(V^{-1})_{ij}^M (T_M)_{\Lambda\Sigma}$ | Eq. (2.1) |
| Spin-1/2 KK mass | $A_{3\,ijk\Lambda,lmn\Sigma} = A_{3\,ijk,lmn}\delta_{\Lambda\Sigma} + \frac{\sqrt{2}}{18}\epsilon_{ijklmnpq}(V^{-1})^{pq\,N}(T_N)_{\Lambda\Sigma}$ | Eq. (2.2) |
| Graviton KK mass | $(M^2_{\text{grav}})_{\Lambda\Sigma} = M_{MN}\delta_{\Omega\Omega'}(T_M)_{\Lambda\Omega}(T_N)_{\Sigma\Omega'}$ | Eq. (2.3) |
| Vector KK mass | $(M^2_{\text{vec}})_{M\Lambda\,N\Sigma}$ (E$_{7(7)}$-covariant) | Eq. (2.4) |
| Goldstone relation | $L^2 M^2_{1\,\text{Gold}} = 3L^2 M^2_2 + 6$, $LM_{1/2\,\text{Gold}} = 2LM_{3/2}$ | Eq. (2.12) |
| Conformal dim (spin-2) | $L^2 M^2_2 = \Delta_2(\Delta_2 - 3)$ | Eq. (3.1) |
| Conformal dim (spin-1) | $L^2 M^2_1 = (\Delta_1 - 1)(\Delta_1 - 2)$ | Eq. (3.1) |
| Conformal dim (spin-3/2, 1/2) | $|LM_{3/2,1/2}| = \Delta_{3/2,1/2} - 3/2$ | Eq. (3.1) |
| Master formula (prior cases) | $E_0 = s_0^{(2)} - \frac{1}{2} + \sqrt{\frac{9}{4} + s_0^{(2)}(s_0^{(2)}+1) - s_0(s_0+1) + \alpha n(n+d-1) + Q^2(R)}$ | Eq. (4.1) |
| Envelope ansatz | $E_0^{\max}(n) = 1 + \sqrt{a_{\max} + b_{\max}n + c_{\max}n^2}$ | Eq. (4.7) |

---

## Relevance to Phonon-Exflation

This paper demonstrates the state-of-the-art for computing complete Kaluza-Klein spectra on internal manifolds ($S^7$, $S^6$) using Exceptional Field Theory. Key connections:

1. **KK spectroscopy methodology**: The ExFT-based mass matrices provide the algorithmic framework for extracting the full particle spectrum from compactification on a given internal manifold. The phonon-exflation framework on $M_4 \times \text{SU}(3)$ requires analogous spectral analysis — the Dirac spectrum $D_K(\tau)$ on SU(3) is precisely the internal-space eigenvalue problem.

2. **Internal symmetry breaking patterns**: The paper tracks how residual symmetries (SO(3), U(1)$\times$U(1), etc.) organize the KK spectrum. In the phonon-exflation context, Jensen deformation breaks SU(3) isometry $\to$ U(1)$_7$, and the spectral organization under this residual symmetry parallels the patterns studied here.

3. **Non-monotonic scalar spectra**: The finding that minimal scalar dimensions can be non-monotonic across KK levels is relevant to the framework's question of whether tau-evolution can produce instabilities at specific KK modes — analogous to the BCS instability mechanism at the fold.

4. **Absence of master formula**: For low-symmetry solutions, no closed-form dimension formula exists. This is consistent with the framework's finding that the Dirac spectrum on deformed SU(3) requires direct numerical computation rather than analytic formulas.
