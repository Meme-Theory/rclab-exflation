# Bell Nonlocality

**Author(s):** Nicolas Brunner, Daniel Cavalcanti, Stefano Pironio, Valerio Scarani, and Stephanie Wehner
**Year:** 2014
**Journal:** Reviews of Modern Physics, 86, 419
**arXiv:** 1303.2849
**Relevance:** HIGH

---

## Abstract

Bell's 1964 theorem, which states that the predictions of quantum theory cannot be accounted for by any local theory, represents one of the most profound developments in the foundations of physics. In the last two decades, Bell's theorem has been a central theme of research from a variety of perspectives, mainly motivated by quantum information science, where the nonlocality of quantum theory underpins many of the advantages afforded by a quantum processing of information. The focus of this review is to a large extent oriented by these later developments. We review the main concepts and tools which have been developed to describe and study the nonlocality of quantum theory, and which have raised this topic to the status of a full sub-field of quantum information science.

---

## Key Arguments and Derivations

### 1. The Locality Condition (Bell's Factorizability)

In a Bell experiment, a source $S$ distributes two physical systems to distant observers Alice and Bob. Alice chooses measurement $x$ and obtains outcome $a$; Bob chooses $y$ and obtains $b$. The experiment is characterized by the joint probability distribution $p(ab|xy)$.

The assumption of locality (no superluminal influence) implies the existence of a past common cause $\lambda$ such that:
$$p(ab|xy,\lambda) = p(a|x,\lambda)\,p(b|y,\lambda)$$

Combined with a probability distribution $q(\lambda)$ over hidden variables, this gives:
$$p(ab|xy) = \int_\Lambda d\lambda\,q(\lambda)\,p(a|x,\lambda)\,p(b|y,\lambda)$$

This is the local hidden variable (LHV) model. No assumptions of determinism or classical behavior are involved -- only locality.

### 2. The CHSH Inequality

For two measurement choices per observer ($x,y \in \{0,1\}$) with binary outcomes ($a,b \in \{-1,+1\}$), define $\langle a_x b_y \rangle = \sum_{a,b} ab\,p(ab|xy)$. Then:
$$S = \langle a_0 b_0 \rangle + \langle a_0 b_1 \rangle + \langle a_1 b_0 \rangle - \langle a_1 b_1 \rangle \leq 2$$

This is the CHSH (Clauser-Horne-Shimony-Holt) inequality. It follows from the factorization condition: $S_\lambda = \langle a_0 \rangle_\lambda \langle b_0 \rangle_\lambda + \langle a_0 \rangle_\lambda \langle b_1 \rangle_\lambda + \langle a_1 \rangle_\lambda \langle b_0 \rangle_\lambda - \langle a_1 \rangle_\lambda \langle b_1 \rangle_\lambda \leq 2$ for each $\lambda$.

### 3. Quantum Violation (Tsirelson Bound)

For two qubits in the singlet state $|\Psi^-\rangle = (|01\rangle - |10\rangle)/\sqrt{2}$, with measurements of $\vec{x} \cdot \vec{\sigma}$ and $\vec{y} \cdot \vec{\sigma}$, the quantum expectation is $\langle a_x b_y \rangle = -\vec{x} \cdot \vec{y}$. With optimal settings (Alice measures along $\hat{e}_1$, $\hat{e}_2$; Bob along $-(\hat{e}_1 + \hat{e}_2)/\sqrt{2}$, $(-\hat{e}_1 + \hat{e}_2)/\sqrt{2}$):
$$S = 2\sqrt{2} > 2$$

The Tsirelson bound establishes that for any quantum state and measurements, $S \leq 2\sqrt{2}$. The no-signaling bound allows $S$ up to 4.

### 4. Mathematical Structure of Correlations

The paper develops a hierarchy of correlation sets:
- **Local correlations** $\mathcal{L}$: form a convex polytope (the local polytope). Its facets are Bell inequalities.
- **Quantum correlations** $\mathcal{Q}$: form a convex set strictly containing $\mathcal{L}$ but strictly contained in $\mathcal{NS}$.
- **No-signaling correlations** $\mathcal{NS}$: form a polytope satisfying $\sum_a p(ab|xy) = \sum_a p(ab|x'y)$ for all $b,y,x,x'$.

The local polytope for the simplest scenario (2 parties, 2 measurements, 2 outcomes) has 16 vertices (deterministic strategies) and 24 facets, 8 of which are the CHSH inequalities.

### 5. Nonlocality vs. Entanglement

A central finding: nonlocality and entanglement are inequivalent resources.
- All pure entangled states are nonlocal (Gisin's theorem).
- There exist mixed entangled states that admit local models (Werner states for $V \leq 1/K_G(3)$ where $K_G(3)$ is the Grothendieck constant of order 3).
- "More nonlocality with less entanglement": there exist states with less entanglement that achieve greater Bell violation than maximally entangled states in certain scenarios.
- Hidden nonlocality: applying local filters before measurement can reveal nonlocality in states that are local for projective measurements.

### 6. Applications of Nonlocality

**Device-independent quantum cryptography (DIQKD)**: Security guaranteed solely by Bell inequality violation, without trusting the internal workings of devices. Key rate bounded by CHSH violation.

**Device-independent randomness generation (DIRNG)**: Certified private randomness from Bell violation. The amount of randomness is quantified by the min-entropy $H_\infty(a|x,E)$.

**Communication complexity**: Nonlocal correlations can reduce the communication required to compute distributed functions.

### 7. Multipartite Nonlocality

**Genuine multipartite nonlocality** (Svetlichny's definition): correlations not decomposable as a mixture of bi-local models for any bipartition of the parties. The Svetlichny inequality for three parties with binary inputs/outputs:
$$S_3 = \langle a_0 b_0 c_0 \rangle - \langle a_0 b_0 c_1 \rangle + \langle a_0 b_1 c_0 \rangle + \langle a_1 b_0 c_0 \rangle + \langle a_0 b_1 c_1 \rangle + \langle a_1 b_0 c_1 \rangle - \langle a_1 b_1 c_0 \rangle + \langle a_1 b_1 c_1 \rangle \leq 4$$

GHZ states achieve $S_3 = 4\sqrt{2}$.

### 8. Experimental Status

**Photonic experiments**: Aspect et al. (1982) first convincingly demonstrated Bell violations. Modern experiments close the detection and locality loopholes simultaneously.

**Loopholes**: (i) Detection loophole -- not all entangled pairs are detected. Requires efficiency $\eta > 2/(1 + 1/\sqrt{2}) \approx 82.8\%$ for CHSH. (ii) Locality loophole -- measurement choices and outcomes must be space-like separated. (iii) Finite statistics -- finite sample sizes require careful statistical analysis.

---

## Key Results

1. Bell's theorem: no local hidden variable theory reproduces all quantum predictions.
2. CHSH inequality: $S \leq 2$ for all local theories; quantum mechanics achieves $S = 2\sqrt{2}$.
3. Tsirelson bound: $S \leq 2\sqrt{2}$ for quantum mechanics.
4. Local polytope completely characterized for $(2,2,2)$ scenario.
5. Nonlocality $\neq$ entanglement: pure entangled states are always nonlocal; mixed states may not be.
6. Werner states admit local models for visibility $V \leq 1/K_G(d)$.
7. Device-independent cryptography and randomness generation from Bell violations.
8. Genuine multipartite nonlocality characterized via Svetlichny inequality.
9. All loopholes must be closed simultaneously for a definitive Bell test.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Locality condition | $p(ab\|xy) = \int d\lambda\,q(\lambda)\,p(a\|x,\lambda)\,p(b\|y,\lambda)$ | Eq. (3) |
| CHSH inequality | $S = \langle a_0 b_0 \rangle + \langle a_0 b_1 \rangle + \langle a_1 b_0 \rangle - \langle a_1 b_1 \rangle \leq 2$ | Eq. (4) |
| Quantum violation | $S = 2\sqrt{2}$ (singlet state, optimal settings) | Eq. (5) |
| Tsirelson bound | $S \leq 2\sqrt{2}$ for all quantum correlations | Sec. II.C.1 |
| No-signaling condition | $\sum_a p(ab\|xy) = \sum_a p(ab\|x'y)$ for all $b,y,x,x'$ | Sec. II.A.1 |
| Singlet correlations | $\langle a_x b_y \rangle = -\vec{x} \cdot \vec{y}$ | Below Eq. (5) |
| Werner state | $\rho_W = V\|\Psi^-\rangle\langle\Psi^-\| + (1-V)\mathbb{I}/4$ | Sec. III.A |
| Svetlichny inequality | $S_3 \leq 4$ (local bound); $S_3 = 4\sqrt{2}$ (GHZ state) | Sec. VI.B.1 |
| Detection efficiency threshold | $\eta > 2/(1 + 1/\sqrt{2}) \approx 82.8\%$ for CHSH | Sec. VII.B.1 |

---

## Relevance to Phonon-Exflation

This review is the definitive modern treatment of Bell nonlocality, providing the mathematical framework (local polytope, quantum correlations, no-signaling correlations) relevant to the quantum foundations of the phonon-exflation framework. The framework's M4 $\times$ SU(3) geometry generates quantum correlations through the fiber structure, and the CPT hardwiring theorem ($[J, D_K(\tau)] = 0$) ensures these correlations respect fundamental symmetries. The distinction between nonlocality and entanglement is relevant to the framework's GGE (generalized Gibbs ensemble) relic state, which is a non-thermal quantum state with specific entanglement properties protected by integrability. The monogamy of entanglement, discussed extensively in the review, constrains how the SU(3) fiber can mediate inter-sector correlations.
