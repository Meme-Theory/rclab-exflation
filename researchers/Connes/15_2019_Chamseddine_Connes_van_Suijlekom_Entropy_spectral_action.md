# Entropy and the Spectral Action

**Authors:** Ali H. Chamseddine, Alain Connes, Walter D. van Suijlekom
**Year:** 2019
**Journal:** Communications in Mathematical Physics, vol. 365, pp. 707-721
**arXiv:** 1809.02944
**Pages:** 15

---

## Abstract

We compute the von Neumann entropy from the fermionic second quantization of a spectral triple and show that it equals the spectral action for a specific universal function. We discover a remarkable connection to the Riemann zeta function: the coefficients in the heat kernel expansion relate to the Riemann xi function through a functional duality that exchanges even and odd dimensions. This work bridges quantum information theory, noncommutative geometry, and analytic number theory.

---

## 1. Introduction and Motivation

### 1.1 The Information-Geometry Bridge

For decades, information theory and differential geometry developed largely in parallel. The von Neumann entropy $S = -\text{Tr}(\rho \ln \rho)$ measures quantum information content of a density matrix $\rho$. Meanwhile, the spectral action principle extracts geometric invariants from heat kernel expansions of the Dirac operator.

This paper reveals these are the **same object**.

Consider a spectral triple $(A, \mathcal{H}, D)$:
- $A$: a C*-algebra (functions on spacetime)
- $\mathcal{H}$: Hilbert space of fermions
- $D$: the Dirac operator

When we perform fermionic second quantization (Fock space quantization), the resulting Gibbs state has entropy that precisely encodes geometric data via the spectral action.

**Significance for the phonon-exflation framework:** This result makes entropy a fundamental geometric property, not merely thermodynamic. If the universe's expansion is driven by spectral action dynamics (as phonon-exflation proposes), then entropy IS geometry. This paper provides the rigorous bridge.

### 1.2 Historical Context

Chamseddine and Connes introduced the spectral action principle in 1996:

$$S_{\text{spectral}} = \text{Tr}(f(D^2/\Lambda^2)) + S_{\text{fermion}}$$

where $f$ is a cutoff function and $\Lambda$ is an energy scale. This generates the Einstein-Cartan action plus all Standard Model interactions.

Von Neumann entropy, by contrast, arises from statistical mechanics:
- Thermal states at temperature $\beta^{-1}$
- Grand canonical ensemble with chemical potential $\mu$
- Density operator $\rho = Z^{-1} e^{-\beta(H - \mu N)}$
- Entropy $S = -\sum_n p_n \ln p_n = -\text{Tr}(\rho \ln \rho)$

This paper shows: **For spectral triples, these are equivalent.**

---

## 2. Spectral Triples and Fermionic Second Quantization

### 2.1 The Spectral Triple Formalism

A **spectral triple** is a triple $(A, \mathcal{H}, D)$ satisfying seven axioms:

1. $A$ is a C*-algebra acting faithfully on $\mathcal{H}$
2. $D$ is an unbounded self-adjoint operator on $\mathcal{H}$
3. All $[D, a]$ for $a \in A$ are bounded
4. $(D - \lambda)^{-1}$ is compact for all $\lambda \notin \mathbb{R}$
5. Regularity: derivatives exist
6. Finiteness: discrete spectrum condition
7. (Optional: Real structure $J$, grading operator $\gamma$, KO-dimension)

For a spin manifold $M$, the Dirac operator on spinors gives the **canonical example**:
- $A = C^\infty(M)$ (continuous functions)
- $\mathcal{H} = L^2(M, S)$ (spinor sections)
- $D = \slashed{D}$ (Dirac operator)

### 2.2 Fermionic Second Quantization

Given a spectral triple with Dirac operator $D$, the Fock space is:

$$\mathcal{F} = \bigoplus_{n=0}^{\infty} \bigwedge^n \mathcal{H}$$

The **fermionic Fock Hamiltonian** is:

$$H = \sum_{j} \lambda_j c_j^\dagger c_j$$

where $\lambda_j$ are the nonzero eigenvalues of $D$ (counting multiplicity), and $c_j^\dagger, c_j$ are creation and annihilation operators satisfying:

$$\{c_i, c_j^\dagger\} = \delta_{ij}, \quad \{c_i, c_j\} = 0$$

The **grand canonical ensemble** at inverse temperature $\beta = 1/k_B T$ and chemical potential $\mu$ has density operator:

$$\rho_{\beta,\mu} = \frac{e^{-\beta(H - \mu N)}}{Z(\beta, \mu)}$$

where $N = \sum_j c_j^\dagger c_j$ is the particle number operator and:

$$Z(\beta, \mu) = \text{Tr}(e^{-\beta(H - \mu N)})$$

### 2.3 Eigenvalue Expansion

For large $\beta$ (low temperature), the partition function expands in eigenvalues. Schematically:

$$Z(\beta, \mu) = \sum_n e^{-\beta(\lambda_n - \mu)} = \sum_n e^{\beta(\mu - \lambda_n)}$$

For the Dirac operator on a $d$-dimensional manifold with smooth density of states, this becomes:

$$Z(\beta, \mu) = \int_0^\infty e^{-\beta(\lambda - \mu)} \rho(\lambda) d\lambda$$

where $\rho(\lambda)$ is the density of states. For small $\beta$ (high temperature cutoff at $\Lambda = 1/\beta$):

$$Z(\beta, \mu) \sim \sum_{k=0}^{\infty} c_k(\mu) \beta^{-k}$$

The coefficients $c_k(\mu)$ contain **geometric information** via heat kernel expansion.

---

## 3. The Heat Kernel and Spectral Action Principle

### 3.1 Heat Kernel Expansion

For the Dirac operator $D$ on a compact $d$-dimensional spin manifold:

$$\text{Tr}(e^{-t D^2}) = \sum_{k=0}^{d} a_k(D^2) t^{(k-d)/2} + \text{exponentially suppressed}$$

The **Seeley-DeWitt coefficients** encode geometric data:

$$a_0(D^2) = (4\pi)^{-d/2} \text{rank}(S) \text{Vol}(M)$$

$$a_2(D^2) = (4\pi)^{-d/2} \frac{\text{rank}(S)}{6} \int_M R \, d\text{vol}$$

$$a_4(D^2) = (4\pi)^{-d/2} \int_M \left(c_1 R^2 + c_2 \text{Ric}^2 + c_3 |\text{Riem}|^2\right) d\text{vol}$$

where $R$ is scalar curvature, $\text{Ric}$ is Ricci tensor, and $\text{Riem}$ is Riemann tensor.

### 3.2 The Spectral Action Functional

The **spectral action** is defined by:

$$S_{\text{spec}}[\Lambda, f] = \text{Tr}(f(D^2/\Lambda^2))$$

where $f$ is a smooth cutoff function (e.g., $f(x) = \max(0, 1 - x)$ for $x \in [0,1]$), and $\Lambda$ is a cutoff energy scale.

By integration by parts and using the heat kernel expansion, one shows:

$$\text{Tr}(f(D^2/\Lambda^2)) = \int_0^\infty f(s) \text{Tr}(e^{-s D^2/\Lambda^2}) ds$$

$$= \int_0^\infty f(s) \left[\sum_{k=0}^{d} a_k(D^2) (s/\Lambda^2)^{(k-d)/2}\right] ds$$

$$= \sum_{k=0}^{d} a_k(D^2) \int_0^\infty f(s) (s/\Lambda^2)^{(k-d)/2} ds$$

$$= \sum_{k=0}^{d} a_k(D^2) \, \Lambda^{d-k} \int_0^\infty f(s) s^{(k-d)/2} ds$$

Defining **spectral action coefficients**:

$$c_k = a_k(D^2) \int_0^\infty f(s) s^{(k-d)/2} ds$$

we get:

$$S_{\text{spec}} = \sum_{k=0}^{d} c_k \Lambda^{d-k}$$

---

## 4. Main Theorem: Entropy as Spectral Action

### 4.1 Statement of the Main Result

**Theorem (Chamseddine-Connes-van Suijlekom 2019):**

Let $(A, \mathcal{H}, D)$ be a $d$-dimensional spectral triple, and let $\rho_{\beta,\mu}$ be the Gibbs state at inverse temperature $\beta$ and chemical potential $\mu = 0$ (zero density limit). Then:

$$S_{\text{vN}} = -\text{Tr}(\rho_{\beta} \ln \rho_{\beta}) = \frac{1}{2\pi i} \oint f_S(z) \text{Tr}\left[\frac{e^{-z}}{(D + z)^{d+1}}\right] dz$$

where $f_S$ is a specific universal function, and this can be expressed as:

$$S_{\text{vN}} = \text{Tr}(f_S(D^2/\beta^2))$$

**Interpretation:** Von Neumann entropy IS a spectral action, but with a different cutoff function $f_S$ than the geometric action.

### 4.2 Derivation Outline

**Step 1: Partition Function Expansion**

The fermionic partition function in the Fock space is:

$$Z(\beta) = \prod_j (1 + e^{-\beta \lambda_j}) \approx \prod_{\lambda > 0} (1 + e^{-\beta \lambda})$$

Taking logarithm:

$$\ln Z = \sum_{\lambda} \ln(1 + e^{-\beta \lambda})$$

**Step 2: Average Energy**

The average energy is:

$$\langle E \rangle = -\frac{\partial}{\partial \beta} \ln Z = \sum_{\lambda > 0} \frac{\lambda}{e^{\beta \lambda} + 1}$$

This is the **Fermi-Dirac distribution**:

$$\langle N_\lambda \rangle = \frac{1}{e^{\beta \lambda} + 1}$$

**Step 3: Von Neumann Entropy Computation**

For a fermionic system, the entropy is:

$$S_{\text{vN}} = \sum_j [p_j \ln p_j + (1 - p_j) \ln(1 - p_j)]$$

where $p_j = \frac{1}{e^{\beta \lambda_j} + 1}$ is the occupation probability. This yields:

$$S_{\text{vN}} = \sum_j \left[-p_j \ln p_j - (1-p_j) \ln(1-p_j)\right]$$

$$= \sum_j \left[-\frac{1}{e^{\beta \lambda_j}+1} \ln\left(\frac{1}{e^{\beta \lambda_j}+1}\right) - \frac{e^{\beta \lambda_j}}{e^{\beta \lambda_j}+1}\ln\left(\frac{e^{\beta \lambda_j}}{e^{\beta \lambda_j}+1}\right)\right]$$

**Step 4: Heat Kernel Form**

By density of states arguments, as $\beta \to 0$ (high temperature):

$$S_{\text{vN}} = \int_0^\infty f_S(\lambda, \beta) \rho_D(\lambda) d\lambda$$

where $\rho_D(\lambda)$ is the density of eigenvalues of $D^2$, and $f_S(\lambda, \beta)$ is the entropy weight:

$$f_S(\lambda, \beta) = -\left[\frac{1}{e^{\beta\lambda}+1} \ln\frac{1}{e^{\beta\lambda}+1} + \frac{e^{\beta\lambda}}{e^{\beta\lambda}+1}\ln\frac{e^{\beta\lambda}}{e^{\beta\lambda}+1}\right]$$

For large $\beta$ (low $T$), $f_S$ localizes to $\lambda = 0$ with total integral $\sim 1$. For small $\beta$ (high $T$), it extends to all $\lambda$.

**Step 5: Spectral Action Form**

The density of states can be extracted from the heat kernel via the Mellin transform:

$$\int_0^\infty t^{s-1} \text{Tr}(e^{-t D^2}) dt = \Gamma(s) \sum_{\lambda_n > 0} \lambda_n^{-2s}$$

Inverting this relation and using the heat kernel expansion, one obtains:

$$S_{\text{vN}} = \text{Tr}(f_S(D^2/\beta^2))$$

where $f_S$ is an explicit universal function determined by the fermionic entropy weights.

---

## 5. Connection to the Riemann Zeta Function

### 5.1 Heat Kernel Coefficients and Zeta Functions

The remarkable discovery is that the expansion coefficients $c_k$ in:

$$S_{\text{vN}} = \sum_{k=0}^{\infty} c_k \beta^{-k}$$

are related to the **Riemann xi function**:

$$\xi(z) = \frac{1}{2} z(z-1) \pi^{-z/2} \Gamma(z/2) \zeta(z)$$

Specifically, for even dimension $d$:

$$c(d) = \text{const} \cdot \xi(-d) = \text{const} \cdot (-d)(-d-1) \pi^{d/2} \Gamma(-d/2) \zeta(-d)$$

For $d = 4$ (spacetime dimension):

$$c_4 \propto \zeta(-4) = \zeta(5) \times \text{functional equation factor}$$

The **functional equation** of the Riemann zeta function:

$$\zeta(1-z) = 2(2\pi)^{-z} \cos(\pi z / 2) \Gamma(z) \zeta(z)$$

induces a **duality** between positive and negative dimensional coefficients. This exchanges:
- Even $d$ $\leftrightarrow$ Odd $d$
- UV expansion ($\beta \to 0$, high $T$) $\leftrightarrow$ IR expansion ($\beta \to \infty$, low $T$)

### 5.2 Interpretation

Why does entropy know about the Riemann zeta function? The answer lies in the **modular properties** of the heat kernel:

$$\text{Tr}(e^{-\beta D^2}) \quad \text{and} \quad \text{Tr}(e^{-D^2/\beta})$$

are related by $\beta \to 1/\beta$ (modular inversion). The zeta function's functional equation implements this symmetry. Thus:

**The zeta function is the "bridge" between high-temperature and low-temperature expansions of entropy in spectral geometry.**

This is not accidental: it reflects a deep number-theoretic structure in noncommutative geometry.

---

## 6. Implications for Second Quantization

### 6.1 Fock Space Thermodynamics

In the full fermionic second quantization, particles and holes coexist. For a spectral triple with both positive and negative eigenvalues of $D$, the Fock space naturally incorporates:

- **Fermions:** occupation $n_j \in \{0, 1\}$ for eigenvalue $\lambda_j > 0$
- **Holes:** complementary states for $\lambda_j < 0$

This is the **Dirac sea picture**: negative energy states act like positive energy antiparticles.

The entropy in Fock space involves both sectors:

$$S_{\text{total}} = S_{\text{particles}} + S_{\text{holes}} + S_{\text{interaction}}$$

The result shows that the **total entropy is still a spectral action**, with the universal function $f_S$ capturing the correct balance.

### 6.2 Relevance to Grand Canonical Ensembles

For finite chemical potential $\mu \neq 0$, the Gibbs state becomes:

$$\rho_{\beta,\mu} = Z^{-1} e^{-\beta(H - \mu N)}$$

The entropy becomes a **mixed** quantity:

$$S(\beta, \mu) = -\text{Tr}(\rho_{\beta,\mu} \ln \rho_{\beta,\mu})$$

While this 2019 paper focuses on $\mu = 0$, the framework extends (see Paper 16) to show that finite-density entropy also admits a spectral action representation, with modified Bessel function coefficients replacing the Riemann zeta connection.

---

## 7. Key Results and Theorems

1. **Entropy-Action Equivalence (Theorem 1):**
   - Von Neumann entropy of fermionic Gibbs state = spectral action functional
   - Cutoff function $f_S$ is universal, determined by information-theoretic principles

2. **Zeta Function Duality (Theorem 2):**
   - Heat kernel expansion coefficients in entropy expansion encode Riemann xi function
   - Functional equation of zeta function manifests as UV-IR duality
   - Even/odd dimensional coefficients are linked via Riemann's symmetry

3. **Fock Space Representation (Theorem 3):**
   - Entropy in fermionic Fock space is expressed entirely in spectral triple language
   - No external thermodynamic postulates needed
   - Emerges from second quantization + heat kernel analysis

4. **Universality (Theorem 4):**
   - Function $f_S$ is **independent** of the specific spectral triple $(A, \mathcal{H}, D)$
   - Applies to all regular, compact, finite spectral triples
   - Only depends on the Dirac operator structure

---

## 8. Impact and Legacy

### 8.1 Within NCG

This paper resolves a long-standing question: Is entropy an emergent quantity in NCG, or fundamental? The answer: **It's both.**

- Fundamental: derives from fermionic second quantization
- Emergent: manifests as geometric data via the spectral action

### 8.2 Towards Phonon-Exflation

For the phonon-exflation framework, this result is **critical**:

1. **Entropy as Geometry:** If the universe expands via spectral action dynamics, entropy IS a geometric invariant (not merely statistical).

2. **Internal Degrees of Freedom:** In the phonon-exflation scenario, the $SU(3)$ internal space can be quantized as a spectral triple. Its entropy directly feeds into the effective potential via:

$$V_{\text{eff}} = V_0 + \Delta V_{\text{Casimir}} + T \cdot S_{\text{internal}}$$

3. **Finite-Density Extension:** The framework enables study of **finite-density phenomena** (chemical potential $\mu \neq 0$) in internal spaces. This is relevant for understanding particle condensation in the deep IR (see Paper 16).

### 8.3 Connection to Modern Physics

- **Holography:** The entropy-action duality echoes the AdS/CFT correspondence between thermal entropy and bulk geometry.
- **Black Hole Thermodynamics:** Bekenstein entropy $S = A/(4\ell_P^2)$ is geometric; this paper shows thermodynamic entropy can be geometric more generally.
- **Quantum Information:** Entanglement entropy in QFT often computed via replica tricks and heat kernels; spectral action formulation provides a unified language.

---

## 9. Technical Details: Proof Sketch

### 9.1 Mellin Transform Relation

The connection between partition function and entropy uses:

$$\text{Tr}(O) = \frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} \langle O | e^{-tD^2} \rangle dt$$

for $s$ large enough. This converts eigenvalue problems into heat kernel integrals.

### 9.2 Contour Integration

The entropy density function:

$$f_S(\lambda) = \lambda \cdot \frac{d}{d\lambda} \ln(1 + e^{-\beta \lambda})$$

is obtained via residue calculus on the complex plane, with poles at $\lambda = i\pi(2n+1)/\beta$ for $n \in \mathbb{Z}$.

### 9.3 Asymptotic Expansion

For $\beta \to 0$, $f_S(\lambda) \approx \lambda / \beta$ (classical limit, equipartition).
For $\beta \to \infty$, $f_S(\lambda)$ becomes concentrated near $\lambda = 0$ (ground state dominance).

These limits are correctly encoded in the heat kernel expansion via polynomial fits to Bessel functions (in the $\beta \to \infty$ case) and polynomial fits to $\ln(1 + e^{-\beta\lambda})$ (in the $\beta \to 0$ case).

---

## 10. Limitations and Open Questions

1. **Axiom Completeness:** Does every aspect of spectral triple structure (real structure $J$, KO-dimension, grading) affect the entropy formula, or only $D$?

2. **Non-Compact Spaces:** The proof assumes compact manifolds. Extension to noncompact cases (e.g., $\mathbb{R}^d$) requires decay conditions on eigenvalue density.

3. **Noncommutative Algebras:** For truly noncommutative $A$ (not $C^\infty(M)$), the spectral action is known, but entropy computation requires more subtle analysis of the algebra's representation theory.

4. **Dynamical Aspects:** The paper is static. How does entropy-as-action evolve under time evolution? Does it remain exact or only approximate?

---

## 11. Connection to Phonon-Exflation Framework

### 11.1 Entropy in Compactified Internal Spaces

In phonon-exflation, we consider $\mathcal{M} = M^4 \times SU(3)$ where:
- $M^4$: four-dimensional spacetime
- $SU(3)$: internal isospin space (or color, or flavor)

The Dirac operator $D$ acts on spinor-valued functions on the full space. Its eigenvalues partition into:

$$\{\lambda_n\} = \{\lambda_{\text{external}}\} \cup \{\lambda_{\text{internal}}\}$$

Phonon modes correspond to quantized excitations of the internal geometry. Their entropy is:

$$S_{\text{phonons}} = -\sum_j (n_j \ln n_j + (1 - n_j) \ln(1 - n_j))$$

where $n_j$ is the Fermi-Dirac occupation. By this theorem, **this entropy is exactly a spectral action** on the internal space:

$$S_{\text{phonons}} = \text{Tr}(f_S(D^2_{\text{internal}}/\beta^2))$$

This entropy feeds into the effective potential:

$$V_{\text{eff}}(t) = V_{\text{tree}} + \Delta V_{\text{loop}} + \Delta V_{\text{Casimir}} + T \cdot S_{\text{phonons}}(t)$$

The **time-evolution of phonon entropy** thus directly drives the effective potential evolution, and hence expansion rate:

$$H(t) = \sqrt{\rho_{\text{phonon}}(t) / 3M_P^2}$$

### 11.2 Entropy-Driven Cosmology

If the universe's expansion is **entropy-driven** (not vacuum-energy-driven), then:

1. Early universe: $T$ high, $S_{\text{phonons}}$ large, $V_{\text{eff}}$ steep $\to$ rapid expansion
2. Intermediate: cooling, $S_{\text{phonons}}$ decreases, $V_{\text{eff}}$ flattens
3. Late universe: $T \to 0$, $S_{\text{phonons}} \to 0$, $V_{\text{eff}} \to V_{\text{tree}}$

This 2019 result shows the entropy term has **all the geometric structure** of the gravitational action, not just a $TS$ correction. It suggests a beautiful unification: **expansion rates and entropy are the same geometric object, viewed through different mathematical lenses.**

### 11.3 BCS Pairing in Internal Space

At finite density $\mu$ in the internal space, fermions condense into Cooper pairs. The entropy-action formalism (extended to $\mu \neq 0$ in Paper 16) applies:

$$S(\mu) = \text{Tr}(f_S^{\text{finite}}(D^2, \mu) / \beta)$$

where $f_S^{\text{finite}}$ involves modified Bessel functions. The **gap energy** of the condensate:

$$\Delta(\mu, T) = \text{min}_a a \quad \text{s.t.} \quad a = g_5 \int_0^{\Lambda} \frac{d\varepsilon}{\pi} \frac{\Delta}{2E_a} \tanh\left(\frac{E_a}{2T}\right)$$

is also expressible via spectral action (though indirectly, through the effective coupling).

This creates a **unified thermodynamic description** of the internal space: both normal and paired phases have entropy-action representations, allowing smooth phase transitions.

---

## References

- Chamseddine, A. H., Connes, A., & van Suijlekom, W. D. (2019). "Entropy and the Spectral Action." Communications in Mathematical Physics, 365, 707--721.
- Connes, A. (1994). *Noncommutative Geometry*. Academic Press.
- Connes, A., & Moscovici, H. (1998). "The Local Index Formula in Noncommutative Geometry." Geometric & Functional Analysis, 5, 174--243.
- Chamseddine, A. H., & Connes, A. (1997). "The Spectral Action Principle." Communications in Mathematical Physics, 186, 731--750.
- Gilkey, P. B. (1984). *Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem*. Publish or Perish.

---

**Word count:** ~3,200 | **Equations:** 45+ | **Theorems:** 4
