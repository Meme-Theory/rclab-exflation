# Asymptotic and exact expansions of heat traces

**Author(s):** Michal Eckstein, Artur Zajac
**Year:** 2014
**Journal:** arXiv preprint (math-ph)
**arXiv:** 1412.5100
**Relevance:** MEDIUM

---

## Abstract

We study heat traces associated with positive unbounded operators with compact inverses. With the help of the inverse Mellin transform we derive necessary conditions for the existence of a short time asymptotic expansion. The conditions are formulated in terms of the meromorphic extension of the associated spectral zeta-functions and proven to be verified for a large class of operators. We also address the problem of convergence of the obtained asymptotic expansions. General results are illustrated with a number of explicit examples.

---

## Key Arguments and Derivations

### 1. Framework

The paper works with a positive densely defined operator $P$ with compact inverse on a separable Hilbert space $H$. The spectrum is discrete: $0 < \lambda_0 < \lambda_1 < \ldots$, with multiplicities $M_n$. The heat trace is $\text{htr}_P(t) = \text{Tr}\,e^{-tP} = \sum_n M_n e^{-t\lambda_n}$, a general Dirichlet series. The spectral zeta function is $\zeta_P(s) = \sum_n M_n \lambda_n^{-s}$.

### 2. Well-definedness Conditions

**Proposition 2.3**: The heat trace is well-defined if and only if $N(\lambda_n) = O(e^{\epsilon\lambda_n})$ for any $\epsilon > 0$, where $N(\lambda)$ is the spectral growth function. The zeta function's abscissa of convergence is $L = \inf\{\alpha : N(\lambda_n) = O(\lambda_n^\alpha)\}$.

### 3. Mellin Transform Connection (Lemma 3.1)

The fundamental relation $\mathcal{M}[\text{htr}_P](s) = \Gamma(s)\zeta_P(s)$ for $\text{Re}(s) > L$ connects the heat trace to the spectral zeta function via the Mellin transform. The inverse Mellin transform produces the heat trace expansion.

### 4. Main Theorem (Theorem 3.2)

Under four conditions on $\zeta_P$ (well-definedness, meromorphic continuation, integrability on vertical lines, and decay on horizontal segments), the heat trace decomposes as:
$$\text{htr}_P(t) = \sum_{k=1}^\infty \sum_{s \in S_k} r_s(t) + F_R(t)$$
where $r_s(t) = \text{Res}_{s'=s}(\Gamma(s')\zeta_P(s')t^{-s'})$ captures the pole contributions and $F_R(t)$ is a remainder from the vertical line integral at $\text{Re}(s) = -R$.

### 5. Asymptotic vs Exact Expansions

The paper carefully distinguishes asymptotic expansions (formal series valid as $t \to 0$) from exact (convergent) expansions. Conditions for convergence are given: if $\zeta_P$ has polynomial growth on vertical strips and no accumulation of poles, the series converges for $t$ in some interval $(0, T)$.

### 6. Examples

Applications include:
- Classical Laplacians on manifolds (recovering Seeley-DeWitt coefficients)
- Pseudodifferential operators with log-polyhomogeneous symbols
- Dirac operators on noncommutative spaces (Podles sphere)
- Operators with non-standard spectral growth

---

## Key Results

1. Necessary and sufficient conditions for heat trace well-definedness in terms of spectral growth (Proposition 2.3)
2. Mellin transform relation $\mathcal{M}[\text{htr}_P](s) = \Gamma(s)\zeta_P(s)$ (Lemma 3.1)
3. Heat trace decomposition via residues of $\Gamma(s)\zeta_P(s)$ (Theorem 3.2)
4. Sufficient conditions for convergence of asymptotic expansions
5. Recovery of classical Seeley-DeWitt coefficients as special case: $a_k(P) = \text{Res}_{s=(d-k)/2}\Gamma(s)\zeta_P(s)$

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Heat trace | $\text{htr}_P(t) = \sum_{n=0}^\infty M_n e^{-t\lambda_n}$ | Eq. (3) |
| Zeta function | $\zeta_P(s) = \sum_{n=0}^\infty M_n \lambda_n^{-s}$ | Eq. (5) |
| Mellin relation | $\mathcal{M}[\text{htr}_P](s) = \Gamma(s)\zeta_P(s)$ | Eq. (8) |
| Residue formula | $r_s(t) = \text{Res}_{s'=s}(\Gamma(s')\zeta_P(s')t^{-s'})$ | Thm 3.2 |
| Seeley-DeWitt | $a_k(P) = \text{Res}_{s=(d-k)/2}\Gamma(s)\zeta_P(s)$ | Section 1 |
| Abscissa | $L = \inf\{\alpha \in \mathbb{R} : N(\lambda_n) = O(\lambda_n^\alpha)\}$ | Prop 2.5 |
| Classical expansion | $\text{Tr}\,e^{-tP} \sim \sum_{k\geq 0} a_k(P)t^{(k-d)/2}$ | Eq. (1) |
| Pseudodiff expansion | $\text{Tr}\,e^{-tP} \sim \sum_k a_k t^{(-d+k)/m} + \sum_l b_l t^l \log t$ | Section 1 |

---

## Relevance to Phonon-Exflation

This paper provides the rigorous mathematical foundation for extracting heat trace coefficients from spectral zeta functions via the Mellin transform. In the framework, the spectral action $\text{Tr}(f(D_K^2/\Lambda^2))$ is computed from the heat trace expansion, and the convergence of this expansion determines whether the spectral action gives perturbative or exact results. The distinction between asymptotic and convergent expansions is relevant to the spectral post-mortem (sessions 37-38) where the question of whether the spectral action provides an exact potential or only an asymptotic series was central.
