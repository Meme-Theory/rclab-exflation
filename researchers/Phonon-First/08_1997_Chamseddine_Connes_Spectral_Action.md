# The Spectral Action Principle

**Author(s):** Ali H. Chamseddine and Alain Connes
**Year:** 1996 (published 1997)
**Journal:** Commun. Math. Phys. 186, 731 (1997)
**arXiv:** hep-th/9606001
**Relevance:** CRITICAL

---

## Abstract

We propose a new action principle to be associated with a noncommutative space $(A, H, D)$. The universal formula for the spectral action is $(\psi, D\psi) + \text{Trace}(\chi(D/\Lambda))$ where $\psi$ is a spinor on the Hilbert space, $\Lambda$ is a scale and $\chi$ a positive function. When this principle is applied to the noncommutative space defined by the spectrum of the standard model one obtains the standard model action coupled to Einstein plus Weyl gravity. There are relations between the gauge coupling constants identical to those of $SU(5)$ as well as the Higgs self-coupling, to be taken at a fixed high energy scale.

---

## Key Arguments and Derivations

### 1. Introduction: From Riemannian to Spectral Geometry

The paper opens by recalling the basic data of Riemannian geometry: a manifold $M$ with line element $ds^2 = g_{\mu\nu} dx^\mu dx^\nu$. The laws of physics are encoded in the action functional $I = I_E + I_{SM}$, where $I_E = \frac{1}{16\pi G} \int R \sqrt{g}\, d^4x$ is the Einstein action and $I_{SM}$ is the standard model action containing gauge bosons, scalars (Higgs), and fermions. The symmetry group is the semidirect product $G = U \rtimes \text{Diff}(M)$ where $U = C^\infty(M, U(1) \times SU(2) \times SU(3))$.

The basic data of noncommutative geometry consists of an involutive algebra $A$ of operators in a Hilbert space $H$ and a selfadjoint unbounded operator $D$. The inverse $D^{-1}$ plays the role of the infinitesimal line element $ds$. For a compact spin manifold, the spectral triple is $(A, H, D) = (C^\infty(M), L^2(M, S), \partial\!\!\!/\,_M)$ where $\partial\!\!\!/\,_M$ is the Dirac operator. The geodesic distance is recovered by

$$d(x,y) = \sup\{|a(x) - a(y)|\,;\, a \in A,\, \|[D,a]\| \leq 1\}$$

The parity of the dimension $n$ implies a $\mathbb{Z}/2$ grading $\gamma$ of $H$ and a real structure given by an antilinear isometry $J$ satisfying $J^2 = \epsilon$, $JD = \epsilon' DJ$, $J\gamma = \epsilon'' \gamma J$ with signs determined by $n \bmod 8$.

The key hypothesis is the **spectral invariance principle**: "The physical action only depends upon $\Sigma$" (the spectrum of $D$).

### 2. The Algebra and Product Geometry

To match the symmetry group $G$ of the SM action, the algebra is $A = C^\infty(M) \otimes A_F$ where the finite-dimensional algebra is

$$A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$$

with $\mathbb{H}$ the quaternion algebra. The product geometry is:

$$H = L^2(M,S) \otimes H_F, \quad D = \partial\!\!\!/\,_M \otimes 1 + \gamma_5 \otimes D_F$$

where $H_F$ is finite-dimensional with basis labelled by elementary leptons and quarks. The grading $\gamma_F$ is $+1$ for left-handed and $-1$ for right-handed. The operator $D_F$ has the form

$$D_F = \begin{pmatrix} Y & 0 \\ 0 & \bar{Y} \end{pmatrix}$$

where $Y$ is the Yukawa coupling matrix.

### 3. Internal Fluctuations

The inner fluctuations of the metric are given by

$$D = D_0 + A + JAJ^{-1}, \quad A = \sum a_i [D_0, b_i], \quad a_i, b_i \in A, \quad A = A^*$$

When computed for the product geometry $M \times F$, these fluctuations are parametrized exactly by the SM gauge bosons ($\gamma$, $W^\pm$, $Z$, eight gluons) and the Higgs field $H$. The fermionic part of the action is simply $\langle\psi, D\psi\rangle$.

### 4. The Spectral Action Principle

The central proposal is the **spectral action**:

$$\text{Trace}\,\chi\!\left(\frac{D}{\Lambda}\right) + \langle\psi, D\psi\rangle$$

where $\chi$ is a positive cutoff function and $\Lambda$ is a mass scale. The bosonic part $\text{Trace}\,\chi(D/\Lambda)$ depends only on the spectrum of $D$, implementing the spectral invariance principle.

### 5. Heat Kernel Expansion and Seeley-DeWitt Coefficients

The spectral action is computed via the heat kernel expansion. Writing $P = D^2$, one uses:

$$\text{Tr}\,e^{-tP} \simeq \sum_{n\geq 0} t^{(n-m)/d} \int_M a_n(x,P)\, dv(x)$$

with $m = 4$ (manifold dimension), $d = 2$ (order of $P$). This gives:

$$\text{Tr}\,\chi(P) \simeq \sum_{n\geq 0} f_n\, a_n(P)$$

where the moments of $\chi$ are:

$$f_0 = \int_0^\infty \chi(u)\, u\, du, \quad f_2 = \int_0^\infty \chi(u)\, du, \quad f_{2(n+2)} = (-1)^n \chi^{(n)}(0)$$

The Seeley-DeWitt coefficients for an elliptic operator $P = -(g^{\mu\nu}\partial_\mu\partial_\nu \cdot \mathbb{1} + A^\mu\partial_\mu + B)$ are:

- $a_0(x,P) = (4\pi)^{-m/2}\,\text{Tr}(\mathbb{1})$
- $a_2(x,P) = (4\pi)^{-m/2}\,\text{Tr}(-\frac{R}{6}\mathbb{1} + E)$
- $a_4(x,P) = (4\pi)^{-m/2}\frac{1}{360}\text{Tr}((-12 R_{;\mu}{}^\mu + 5R^2 - 2R_{\mu\nu}R^{\mu\nu} + 2R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma})\mathbb{1} - 60RE + 180E^2 + 60E_{;\mu}{}^\mu + 30\Omega_{\mu\nu}\Omega^{\mu\nu})$

where $E$ and $\Omega_{\mu\nu}$ are constructed from the connection.

### 6. Einstein-Yang-Mills System

As a test, the spectral action is computed for $A = C^\infty(M) \otimes M_N(\mathbb{C})$, yielding:

$$a_0(P) = \frac{N}{4\pi^2}\int_M \sqrt{g}\, d^4x$$

$$a_2(P) = \frac{N}{48\pi^2}\int_M \sqrt{g}\, R\, d^4x$$

$$a_4(P) = \frac{1}{16\pi^2}\frac{N}{360}\int d^4x\sqrt{g}\left((12R_{;\mu}{}^\mu + 5R^2 - 8R_{\mu\nu}R^{\mu\nu} - 7R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}) + \frac{120}{N}g^2 F^i_{\mu\nu}F^{\mu\nu i}\right)$$

### 7. Standard Model Spectral Action

For the SM, the Yukawa coupling matrices $Y_q$ and $Y_\ell$ for quarks and leptons enter through the Dirac operators $D_q$ (36x36 matrix, eq. 3.8) and $D_\ell$ (9x9 matrix, eq. 3.13), incorporating gauge fields $B_\mu$, $A^\alpha_\mu$, $V^i_\mu$ and Higgs field $H$.

The full bosonic spectral action is (eq. 3.16):

$$I = \frac{9m_0^4}{\pi^2}\frac{5}{4}f_0\int d^4x\sqrt{g} + \frac{3m_0^2}{4\pi^2}f_2\int d^4x\sqrt{g}\left(\frac{5}{4}R - 2y^2 H^*H\right)$$
$$+ \frac{f_4}{4\pi^2}\int d^4x\sqrt{g}\bigg[\frac{1}{40}\frac{5}{4}(12R_{;\mu}{}^\mu + 11R^*R^* - 18C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma})$$
$$+ 3y^2\left(D_\mu H^* D^\mu H - \frac{1}{6}RH^*H\right) + g_{03}^2 G^i_{\mu\nu}G^{\mu\nu i} + g_{02}^2 F^\alpha_{\mu\nu}F^{\mu\nu\alpha} + \frac{5}{3}g_{01}^2 B_{\mu\nu}B^{\mu\nu} + 3z^2(H^*H)^2 - y^2(H^*H)_{;\mu}{}^\mu\bigg]$$

where $y^2 = \text{Tr}(|k_0^d|^2 + |k_0^u|^2 + \frac{1}{3}|k_0^e|^2)$ and $z^2 = \text{Tr}((|k_0^d|^2 + |k_0^u|^2)^2 + \frac{1}{3}|k_0^e|^4)$.

### 8. Normalizations and Predictions

Normalizing the Einstein and Yang-Mills kinetic terms yields:

$$\frac{15 m_0^2 f_2}{4\pi^2} = \frac{1}{\kappa_0^2}, \quad \frac{g_{03}^2 f_4}{\pi^2} = 1$$

and the GUT-like gauge coupling relations:

$$g_{03}^2 = g_{02}^2 = \frac{5}{3}g_{01}^2$$

After Higgs field rescaling $H \to \frac{2}{3}\frac{g_{03}}{y}H$ and normalizing, the full action takes the form of the SM coupled to Einstein-Weyl gravity (eq. 3.20) with specific relations among the bare couplings:

$$\mu_0^2 = \frac{4}{3\kappa_0^2}, \quad \lambda_0 = \frac{4}{3}g_{03}^2\frac{z^2}{y^4}, \quad \xi_0 = \frac{1}{6}, \quad b_0 = 0$$

The conformal coupling $\xi_0 = 1/6$ is a prediction of the spectral action.

### 9. Phenomenology

Using 1-loop RG equations, the unification scale is $\Lambda \sim 10^{15}$ GeV, and $\sin^2\theta_w \sim 0.21$ (10% off from the experimental 0.2325). The Higgs mass is predicted in the range 160-180 GeV (later corrected by the sigma field, see Paper 10). The Higgs self-coupling at unification: $\lambda(\Lambda) \simeq \frac{16\pi}{3}\alpha_3(\Lambda) \simeq 0.402$.

---

## Key Results

1. **The Spectral Action Principle:** The universal action for any noncommutative geometry is $\text{Tr}\,\chi(D/\Lambda) + \langle\psi, D\psi\rangle$, depending only on the spectrum of $D$ and a cutoff scale $\Lambda$.

2. **SM from NCG:** The internal fluctuations of the product geometry $M \times F$ with $A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ reproduce exactly the SM gauge bosons and Higgs field.

3. **Einstein-Weyl gravity:** The spectral action contains not only the Einstein-Hilbert action but also the Weyl curvature term $C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}$ and the Gauss-Bonnet topological term $R^*R^*$.

4. **GUT-like coupling unification:** $g_3^2 = g_2^2 = \frac{5}{3}g_1^2$ at the cutoff scale, identical to $SU(5)$ relations.

5. **Higgs self-coupling predicted:** $\lambda_0 = \frac{4}{3}g_3^2 \frac{z^2}{y^4}$ at unification scale (simplified: $\lambda(\Lambda) \simeq \frac{16\pi}{3}\alpha_3(\Lambda)$).

6. **Conformal Higgs-gravity coupling:** $\xi_0 = 1/6$ (conformal coupling) is a geometric prediction.

7. **Vanishing $R^2$ term:** $b_0 = 0$ at the bare level; generated only through radiative corrections.

8. **Cosmological constant:** $e_0 = \frac{45}{4\pi^2}f_0 m_0^4$, related to the difference between fermionic (90) and bosonic (28) degrees of freedom.

9. **Unification scale:** $\Lambda \sim 10^{15}$ GeV from gauge coupling running, with $\sin^2\theta_w \sim 0.21$.

10. **Higgs mass:** 160-180 GeV from boundary condition and RG running (later revised by sigma field).

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spectral action | $\text{Tr}\,\chi(D/\Lambda) + \langle\psi, D\psi\rangle$ | Eq. (1.28) |
| Geodesic distance | $d(x,y) = \sup\{|a(x)-a(y)|;\; \|[D,a]\|\leq 1\}$ | Eq. (1.5) |
| Real structure signs | $J^2 = \epsilon,\; JD = \epsilon'DJ,\; J\gamma = \epsilon''\gamma J$ | Eq. (1.7) |
| Algebra | $A = C^\infty(M) \otimes (\mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C}))$ | Eqs. (1.16)-(1.17) |
| Product Dirac | $D = \partial\!\!\!/\,_M \otimes 1 + \gamma_5 \otimes D_F$ | Eq. (1.19) |
| Finite Dirac | $D_F = \begin{pmatrix} Y & 0 \\ 0 & \bar{Y}\end{pmatrix}$ | Eq. (1.21) |
| Order-one condition | $[[D,a], b^0] = 0,\;\forall a,b \in A$ | Eq. (1.22) |
| Inner fluctuations | $D = D_0 + A + JAJ^{-1},\; A = \sum a_i[D_0, b_i]$ | Eq. (1.23) |
| Heat kernel expansion | $\text{Tr}\,\chi(P) \simeq \sum_{n\geq 0} f_n\, a_n(P)$ | Eq. (2.14) |
| Moment integrals | $f_0 = \int_0^\infty \chi(u)u\,du,\; f_2 = \int_0^\infty \chi(u)\,du,\; f_{2(n+2)} = (-1)^n\chi^{(n)}(0)$ | Eq. (2.15) |
| $a_0$ coefficient | $a_0 = (4\pi)^{-m/2}\text{Tr}(\mathbb{1})$ | Eq. (2.16) |
| $a_2$ coefficient | $a_2 = (4\pi)^{-m/2}\text{Tr}(-\frac{R}{6}\mathbb{1} + E)$ | Eq. (2.16) |
| $a_4$ (Weyl form) | $a_4 \sim \int d^4x\sqrt{g}(-\frac{3}{20}C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} + \frac{1}{120}(11R^*R^* + 12R_{;\mu}{}^\mu) + \frac{g^2}{N}F^i_{\mu\nu}F^{\mu\nu i})$ | Eq. (2.24) |
| Gauge coupling relations | $g_{03}^2 = g_{02}^2 = \frac{5}{3}g_{01}^2$ | Eq. (3.18) |
| Normalized SM action | $I_b = \int d^4x\sqrt{g}[\frac{1}{2\kappa_0^2}R - \mu_0^2 H^*H + a_0 C^2 + \ldots + \lambda_0(H^*H)^2]$ | Eq. (3.20) |
| Higgs coupling | $\lambda_0 = \frac{4}{3}g_{03}^2\frac{z^2}{y^4}$ | Eq. (3.21) |
| Conformal coupling | $\xi_0 = \frac{1}{6}$ | Eq. (3.21) |
| RG for gauge couplings | $\frac{dg_i}{dt} = \frac{1}{16\pi^2}b_i g_i^3,\; b = (\frac{41}{6}, -\frac{19}{6}, -7)$ | Eq. (3.24) |
| Higgs mass estimate | $160 < m_H < 200$ GeV | Eq. (3.34) |

---

## Relevance to Phonon-Exflation

This paper is the foundational reference for the spectral action principle that underlies the entire phonon-exflation framework. The framework's product geometry $M^4 \times F$ with $F$ encoding the internal space is a direct descendant of the construction here, where $A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ defines the finite geometry. The Seeley-DeWitt coefficients $a_0$, $a_2$, $a_4$ computed here are the same objects whose behavior under $\tau$-evolution the framework tracks to study stabilization: $a_0$ gives the cosmological term, $a_2$ gives the Einstein term with Higgs mass, and $a_4$ gives gauge kinetic terms and the Higgs quartic coupling. The heat kernel expansion $\text{Tr}\,\chi(D^2/\Lambda^2) \simeq \sum f_n a_n$ is the master formula whose monotonicity properties were studied in the framework's spectral post-mortem (Sessions 20-37). The inner fluctuation formula $D \to D + A + JAJ^{-1}$ is the mechanism by which the framework generates gauge and Higgs fields from the Dirac operator on $M^4 \times SU(3)$.
