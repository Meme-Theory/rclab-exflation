# Rationality of Spectral Action for Robertson-Walker Metrics

**Author(s):** Farzad Fathizadeh, Asghar Ghorbanpour, Masoud Khalkhali
**Year:** 2014
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 1407.5972
**Relevance:** MEDIUM

---

## Abstract

We use pseudodifferential calculus and heat kernel techniques to prove a conjecture by Chamseddine and Connes on rationality of the coefficients of the polynomials in the cosmic scale factor $a(t)$ and its higher derivatives, which describe the general terms $a_{2n}$ in the expansion of the spectral action for general Robertson-Walker metrics. We also compute the terms up to $a_{12}$ in the expansion of the spectral action by our method. As a byproduct, we verify that our computations agree with the terms up to $a_{10}$ that were previously computed by Chamseddine and Connes by a different method.

---

## Key Arguments and Derivations

**Robertson-Walker Dirac operator.** The Euclidean Robertson-Walker metric $ds^2 = dt^2 + a^2(t) d\sigma^2$ is written in Hopf coordinates on $S^3$. The Dirac operator is computed explicitly as:
$$D = \gamma^1 \frac{\partial}{\partial t} + \gamma^2 \frac{1}{a}\frac{\partial}{\partial \eta} + \gamma^3 \frac{1}{a\sin\eta}\frac{\partial}{\partial \phi_1} + \gamma^4 \frac{1}{a\cos\eta}\frac{\partial}{\partial \phi_2} + \frac{3a'}{2a}\gamma^1 + \frac{\cot(2\eta)}{a}\gamma^2$$

**Pseudodifferential symbol of $D^2$.** The symbol $\sigma(D^2) = p_2 + p_1 + p_0$ is computed, with $p_2$ the principal symbol encoding the metric.

**Heat kernel method.** Using the pseudodifferential calculus for computing Seeley-DeWitt coefficients, the terms $a_0, a_2, a_4, a_6, a_8, a_{10}$ are reproduced, confirming the earlier Chamseddine-Connes computation. The new term $a_{12}$ is then computed via a significantly heavier calculation and validated by parallel computations in spherical coordinates.

**Proof of the Chamseddine-Connes conjecture.** The main theorem proves that each $a_{2n}$ in the spectral action expansion takes the form $Q_{2n}(a(t), a'(t), \ldots, a^{(2n)}(t))/a(t)^{2n-3}$, where $Q_{2n}$ is a polynomial with rational coefficients. The proof exploits a symmetry in the heat kernel arising from the Hopf coordinate system. A recursive formula for the coefficient of the highest-order derivative term in $a_{2n}$ is also obtained.

## Key Results

1. Proof of Chamseddine-Connes conjecture: all coefficients in $a_{2n}$ for Robertson-Walker metrics are rational
2. Computation of $a_{12}$ in the spectral action expansion for general Robertson-Walker metrics
3. Verification of $a_8$ and $a_{10}$ against earlier Chamseddine-Connes results
4. Recursive formula for the leading derivative coefficient in $a_{2n}$
5. Agreement of Hopf coordinate and spherical coordinate computations for $a_{12}$

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Robertson-Walker metric | $ds^2 = dt^2 + a^2(t)(d\eta^2 + \sin^2\eta\, d\phi_1^2 + \cos^2\eta\, d\phi_2^2)$ | Sec. 2.2 |
| Heat kernel expansion | $\text{Tr}(e^{-tD^2}) \sim t^{-\dim(M)/2} \sum_{n \geq 0} a_{2n}(D^2) t^n$ | Sec. 1 |
| Spectral action expansion | $\text{Tr}\, f(D^2/\Lambda^2) \sim \sum_{n \geq 0} f_{2n}\, a_{2n}(D^2/\Lambda^2)$ | Sec. 1 |
| Rationality theorem | $a_{2n} = Q_{2n}(a, a', \ldots, a^{(2n)})/a^{2n-3}$, $Q_{2n} \in \mathbb{Q}[\cdot]$ | Sec. 5.1 |
| Symbol of $D^2$ | $\sigma(D^2) = p_2 + p_1 + p_0$ | Prop. 2.1 |
| Spin connection (RW) | $\tilde{\omega} = \frac{1}{2a(t)}(a'\theta^2 \gamma_{12} + a'\theta^3 \gamma_{13} + a'\theta^4 \gamma_{14} + \cot\eta\, \theta^3 \gamma_{23} - \tan\eta\, \theta^4 \gamma_{24})$ | Eq. (1) |

## Relevance to Phonon-Exflation

The spectral action expansion for Robertson-Walker metrics provides the bridge between the NCG framework and cosmological observables. The Seeley-DeWitt coefficients $a_{2n}$ computed here, expressed as rational functions of the scale factor $a(t)$ and its derivatives, are the mathematical objects that encode how the spectral action responds to expansion. The rationality theorem constrains the structure of the spectral action at all orders, which is relevant to the monotonicity results (CUTOFF-SA-37) and the spectral action post-mortem analysis.
