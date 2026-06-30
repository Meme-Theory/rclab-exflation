# Entropy and the Spectral Action

**Author(s):** Ali H. Chamseddine, Alain Connes, Walter D. van Suijlekom
**Year:** 2019
**Journal:** Journal of Geometry and Physics 137, 16-31 (2019)
**arXiv:** 1809.02944
**Relevance:** CRITICAL

---

## Abstract

We compute the information theoretic von Neumann entropy of the state associated to the fermionic second quantization of a spectral triple. We show that this entropy is given by the spectral action of the spectral triple for a specific universal function. The main result of our paper is the surprising relation between this function and the Riemann zeta function. It manifests itself in particular by the values of the coefficients $c(d)$ by which it multiplies the $d$-dimensional terms in the heat expansion of the spectral triple. We find that $c(d)$ is the product of the Riemann xi function evaluated at $-d$ by an elementary expression. In particular $c(4)$ is a rational multiple of $\zeta(5)$ and $c(2)$ a rational multiple of $\zeta(3)$. The functional equation gives a duality between the coefficients in positive dimension, which govern the high energy expansion, and the coefficients in negative dimension, exchanging even dimension with odd dimension.

---

## Key Arguments and Derivations

### Spectral Triples and Second Quantization

Starting from a spectral triple $(\mathcal{A}, \mathcal{H}, D)$, the authors perform fermionic second quantization using the Clifford algebra $\mathcal{C} := \text{Cliff}_\mathbb{C}(\mathcal{H}_\mathbb{R})$ of the underlying real Hilbert space. The operator $D$ generates a one-parameter group of automorphisms $\sigma_t \in \text{Aut}(\mathcal{C})$:

$$\sigma_t(A) = e^{itH} A e^{-itH}$$

### KMS State

For any inverse temperature $\beta > 0$, there exists a unique KMS$_\beta$ state $\varphi_\beta$ on the $C^*$-dynamical system $(\mathcal{C}, \sigma_t)$. The KMS condition states:

$$\varphi(a\sigma_t(b))|_{t=i\beta} = \varphi(ba), \quad \forall a,b \in \mathcal{C}$$

The density matrix for the KMS state is $\rho = Z e^{-\beta H}$ with $Z = 1/\text{Tr}(e^{-\beta H})$.

### Physical Fock Representation

The Dirac sea construction uses the complex structure $I = i \cdot \text{sign}(D)$. In the physical Fock representation, the one-parameter group is implemented by $W(t) = \bigwedge \exp(it|D|)$. The KMS state at inverse temperature $\beta$ is:

$$\varphi_\beta(A) = \frac{1}{Z} \text{Tr}\left(\bigwedge \exp(-\beta|D|) \cdot \gamma_I(A)\right)$$

### The Central Result: Entropy = Spectral Action

**Theorem 3.4.** The von Neumann entropy of the KMS state $\varphi_\beta$ equals the spectral action for the specific test function $h(x) := E(e^{-x})$:

$$S(\varphi_\beta) = \text{Tr}(h(\beta D))$$

where the **entropy function** $E(x)$ for a partition is:

$$E(x) := \frac{\log(x+1) - x\log(x)}{x+1}$$

and the spectral function is:

$$h(x) = E(e^{-x}) = \frac{x}{1+e^x} + \log(1+e^{-x})$$

This is an even, positive function with derivative:

$$h'(x) = -\frac{x}{4\cosh^2(x/2)}$$

### Taylor Expansion

$$h(\sqrt{x}) = \log(2) - \frac{x}{8} + \frac{x^2}{64} - \frac{x^3}{576} + \frac{17x^4}{92160} - \frac{31x^5}{1612800} + \cdots$$

### Connection to the Riemann Zeta Function

The moments of $h$ that appear as coefficients in the heat expansion are:

$$2\int_0^\infty h(x) x \, dx = \frac{9\zeta(3)}{2}, \qquad 2\int_0^\infty h(x) x^3 \, dx = \frac{225\zeta(5)}{4}$$

More generally:

$$\int_0^\infty h(x) x^\alpha \, dx = \frac{1 - 2^{-\alpha-1}}{\alpha+1} \Gamma(\alpha+3)\zeta(\alpha+2)$$

The coefficient of $t^a$ in the heat expansion is:

$$\gamma(a) = \frac{1 - 2^{-2a}}{a} \pi^{-a} \xi(2a)$$

where $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ is the Riemann xi function.

### Key Coefficient Values

In dimension 4, the relevant coefficients are:

| $a$ | $\gamma(a)$ |
|:----|:------------|
| $-2$ | $\frac{225\zeta(5)}{4}$ |
| $-3/2$ | $\frac{14\pi^{7/2}}{45}$ |
| $-1$ | $\frac{9\zeta(3)}{2}$ |
| $-1/2$ | $\frac{\pi^{3/2}}{3}$ |
| $0$ | $\log(2)$ |
| $1/2$ | $\frac{1}{2\sqrt{\pi}}$ |
| $1$ | $\frac{1}{8}$ |
| $3/2$ | $\frac{7\zeta(3)}{8\pi^{5/2}}$ |
| $2$ | $\frac{1}{32}$ |

### Duality from the Functional Equation

The functional equation of the Riemann zeta function gives a duality between the coefficients in positive dimension (governing the high energy expansion) and those in negative dimension, exchanging even with odd dimension.

---

## Key Results

1. **The von Neumann entropy of the fermionic second quantization of a spectral triple equals the spectral action** for the universal test function $h(x) = E(e^{-x})$.
2. The test function $h$ is intimately related to the **Riemann zeta function**: the heat expansion coefficients $c(d)$ involve the Riemann xi function evaluated at $-d$.
3. In dimension 4: $c(4)$ is a rational multiple of $\zeta(5)$, and $c(2)$ is a rational multiple of $\zeta(3)$.
4. The functional equation provides a **duality** between high-energy (positive dimension) and low-energy (negative/odd dimension) coefficients.
5. The entropy functional is **additive** for direct sums of spectral triples, consistent with thermodynamic extensivity.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Entropy = Spectral Action | $S(\varphi_\beta) = \text{Tr}(h(\beta D))$ | Theorem 3.4 |
| Entropy function | $h(x) = \frac{x}{1+e^x} + \log(1+e^{-x})$ | Sec. 4 |
| Binary entropy | $E(x) = \frac{\log(x+1) - x\log(x)}{x+1}$ | Lemma 3.1 |
| $h$ derivative | $h'(x) = -\frac{x}{4\cosh^2(x/2)}$ | Lemma 4.1 |
| Moments of $h$ | $\int_0^\infty h(x) x^\alpha dx = \frac{1-2^{-\alpha-1}}{\alpha+1}\Gamma(\alpha+3)\zeta(\alpha+2)$ | Lemma 4.5 |
| Heat coefficient | $\gamma(a) = \frac{1-2^{-2a}}{a}\pi^{-a}\xi(2a)$ | Lemma 4.6 |
| $c(4)$ coefficient | $\gamma(-2) = \frac{225\zeta(5)}{4}$ | Lemma 4.5 |
| $c(2)$ coefficient | $\gamma(-1) = \frac{9\zeta(3)}{2}$ | Lemma 4.5 |
| KMS state | $\varphi_\beta(A) = Z^{-1}\text{Tr}(\bigwedge e^{-\beta|D|}\gamma_I(A))$ | Prop. 2.6 |
| Entropy additivity | $S(\varphi_1 \otimes \varphi_2) = S(\varphi_1) + S(\varphi_2)$ | Sec. 3 |

## Relevance to Phonon-Exflation

This paper is **central** to the phonon-exflation framework. The identity $S_{\text{vN}} = \text{Tr}(h(\beta D))$ proves that the spectral action IS the von Neumann entropy -- the same functional that governs the internal geometry simultaneously encodes the information content. This is the microscopic realization of Jacobson's vision (Paper 17): the spectral action = free energy, and $\delta Q = T \, dS$ becomes a statement about the Dirac spectrum. The specific function $h(x)$ replaces the arbitrary test function $\chi$ traditionally used in the spectral action principle, providing a unique, physically motivated choice determined by second quantization. The connection to the Riemann zeta function through the heat expansion coefficients ($\zeta(3)$, $\zeta(5)$) is unexplained and may point to deeper number-theoretic structure in the framework.
