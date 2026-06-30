# Complete Computation of DeWitt-Seeley-Gilkey Coefficient E4 for Nonminimal Operator on Curved Manifolds

**Author(s):** V.P. Gusynin, V.V. Kornyak
**Year:** 1999
**Journal:** arXiv preprint
**arXiv:** math/9909145
**Relevance:** HIGH

---

## Abstract

Asymptotic heat kernel expansion for nonminimal differential operators on curved manifolds in the presence of gauge fields is considered. The complete expressions for the fourth coefficient (E4) in the heat kernel expansion for such operators are presented for the first time. The expressions were computed for general case of manifolds of arbitrary dimension n and also for the most important case n = 4. The calculations have been carried out on PC with the help of a program written in C.

---

## Key Arguments and Derivations

### 1. Nonminimal Operators

The paper addresses the heat kernel expansion for the generic nonminimal operator
$$A = -g^{\mu\nu}\Box + a D^\mu D^\nu + X^{\mu\nu}$$
where $\Box = g^{\mu\nu}D_\mu D_\nu$ is the covariant Laplacian, $D_\mu$ contains affine and bundle connections, $X$ is a tensor field, and $a$ is a scalar parameter satisfying $a < 1$ for ellipticity. Such operators arise in:
- Yang-Mills quantization in arbitrary covariant gauge: $A^{ab}_{\mu\nu} = -\delta_{\mu\nu}\Box^{ab} - (\frac{1}{\alpha}-1)D^{ac}_\mu D^{cb}_\nu - 2f^{acb}G^c_{\mu\nu}$
- Electromagnetic field in external gravity: $A_{\mu\nu} = -g_{\mu\nu}\Box - (\frac{1}{\alpha}-1)D_\mu D_\nu + R_{\mu\nu}$
- The Feynman gauge $\alpha = 1$ reduces these to minimal operators (DeWitt method), but general gauge requires the nonminimal treatment.

### 2. Algorithm Based on Covariant Pseudodifferential Calculus

The method uses Widom's covariant symbolic calculus rather than DeWitt's iterative procedure (which is inapplicable to nonminimal operators). The resolvent $(A - \lambda)^{-1}$ is represented via a phase function $l(x,x',k)$ and amplitude $\sigma(x,x',k;\lambda)$. Coincidence limits of covariant derivatives of $l$ and the transport function $I$ are computed via recursion relations (eq. 10). The DWSG coefficients are then obtained by:
$$E_m(x|A) = \int \frac{d^n k}{(2\pi)^n\sqrt{g}} \oint \frac{id\lambda}{2\pi} e^{-\lambda} [\sigma_m](x,k,\lambda)$$

The resulting integrals are expressed in terms of Gauss hypergeometric functions $F(m, (p+s+n/2)/r; l+m; a)$, which for integer parameters reduce to elementary functions.

### 3. Implementation

A C program of ~10,000 lines with ~200 functions handles all tensor manipulations. It consists of:
- **COLIM**: computes coincidence limits of $l$ and $I$ functions (universal, reusable)
- **DWSGCOEF**: computes $E_m$ via recursion, coincidence limits, integration, and simplification using Ricci and Bianchi identities

### 4. Results: $E_2$ and $\text{tr}_L E_4$

The $E_2$ coefficient is given with 5 scalar functions $C_1$--$C_5$ depending on $a$ and $n$ (eq. 19). The full $E_4$ has 73 tensor terms with 43 different scalar coefficients. The Lorentz trace $\text{tr}_L E_4$ contains 13 invariant structures (eq. 20) with coefficients $C_1$--$C_{13}$ that are rational functions of $a$ containing $(1-a)^{-n/2}$ factors.

---

## Key Results

1. First complete computation of $E_4$ for the nonminimal operator $-g^{\mu\nu}\Box + aD^\mu D^\nu + X^{\mu\nu}$ in arbitrary dimension
2. The Lorentz trace $\text{tr}_L E_4$ in arbitrary dimension with gauge field (13 invariant structures)
3. Specialization to $n = 4$ with explicit coefficients
4. Verification: in the limit $a \to 0$ (minimal operator), standard results for $E_4$ of the operator $-\Box + X$ are recovered
5. All scalar coefficients are rational functions of $a$ with poles at $a = 1$ (loss of ellipticity) and algebraic dependence on dimension through $(1-a)^{-n/2}$

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Nonminimal operator | $A = -g^{\mu\nu}\Box + aD^\mu D^\nu + X^{\mu\nu}$ | Eq. (6) |
| Heat kernel expansion | $\langle x|e^{-tA}|x\rangle \sim \sum_{m\geq 0} E_m(x|A) t^{(m-n)/(2r)}$ | Eq. (1) |
| $E_2$ | $(4\pi)^{-n/2}\{-C_1 X^{ab} - \frac{C_2}{4}(X^{ba} + g^{ab}X^i_i) - C_3 W^{ab} + C_4 R^{ab} + C_5 g^{ab}R\}$ | Eq. (19) |
| $\text{tr}_L E_4$ | $(4\pi)^{-n/2}\{-C_1 \Box X^i_i - C_2 D^i D^j X^{ij} + C_3(X^i_i X^j_j + X^{ij}X^{ij}) + C_4 X^{ij}X^{ji} + \ldots\}$ | Eq. (20) |
| Hypergeometric integral | $J(k^{2p}k_{a_1}\ldots/(k^{2r}-\lambda)^l[(1-a)k^{2r}-\lambda]^m) = \ldots F(m,(p+s+n/2)/r;l+m;a)$ | Eq. (13) |
| Resolvent representation | $G(x,x',\lambda) = \int \frac{d^n k}{(2\pi)^n}\sqrt{g(x')} e^{il(x,x',k)}\sigma(x,x',k;\lambda)$ | Eq. (8) |
| Recursion (principal symbol) | $A^{ab}\sigma_{0bc} = I^a_c$ | Eq. (11) |

---

## Relevance to Phonon-Exflation

This paper provides the computational technology for heat kernel coefficients of nonminimal operators, which arise when the Dirac operator on M4 x SU(3) is squared and gauge-fixing terms are included. The explicit dependence of all coefficients on the nonminimality parameter $a$ is essential for understanding how gauge choice affects the spectral action. The hypergeometric function structure connects to the parameter-dependent spectral computations in the framework's computation scripts. The fact that $E_4$ has 73 tensor terms underscores why computer algebra (the C program described here, or modern equivalents) is essential for the spectral geometry calculations.
