# Gravity and the Standard Model with Neutrino Mixing

**Author(s):** Ali H. Chamseddine, Alain Connes, and Matilde Marcolli
**Year:** 2006 (published 2007)
**Journal:** Adv. Theor. Math. Phys. 11, 991-1090 (2007)
**arXiv:** hep-th/0610241
**Relevance:** CRITICAL

---

## Abstract

We present an effective unified theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity. The unification is based on the symplectic unitary group in Hilbert space and on the spectral action. It yields all the detailed structure of the standard model with several predictions at unification scale. Besides the familiar predictions for the gauge couplings as for GUT theories, it predicts the Higgs scattering parameter and the sum of the squares of Yukawa couplings. From these relations one can extract predictions at low energy, giving in particular a Higgs mass around 170 GeV and a top mass compatible with present experimental value. The geometric picture that emerges is that space-time is the product of an ordinary spin manifold (for which the theory would deliver Einstein gravity) by a finite noncommutative geometry $F$. The discrete space $F$ is of KO-dimension 6 modulo 8 and of metric dimension 0, and accounts for all the intricacies of the standard model with its spontaneous symmetry breaking Higgs sector.

---

## Key Arguments and Derivations

### 1. Introduction and Overview

This paper presents the definitive NCG construction of the full Standard Model with neutrino mixing and Majorana masses, coupled to gravity. The model takes as input a finite-dimensional algebra and delivers the full SM Lagrangian including the see-saw mechanism. The spectral action functional $\text{Tr}(f(D/\Lambda))$ gives the bosonic sector, while the fermionic action is $\frac{1}{2}\langle J\tilde{\xi}, D\tilde{\xi}\rangle$ with $\tilde{\xi} \in H^+_{cl}$ (classical fermions restricted to the positive chirality subspace).

Three predictions are made under the big desert hypothesis:
1. Gauge coupling unification: $g_2 = g_3 = \sqrt{5/3}\,g_1$
2. Higgs scattering parameter $\alpha_h$ at unification scale, giving $m_H \approx 170$ GeV
3. Fermion-boson mass relation: $\sum_{\text{gen}}(m_e^2 + m_\nu^2 + 3m_d^2 + 3m_u^2) = 8M_W^2$

### 2. The Finite Geometry

#### 2.1 The Left-Right Symmetric Algebra

The starting algebra is the left-right symmetric algebra:

$$A_{LR} = \mathbb{C} \oplus \mathbb{H}_L \oplus \mathbb{H}_R \oplus M_3(\mathbb{C})$$

with involution $({\lambda, q_L, q_R, m})^* = (\bar{\lambda}, \bar{q}_L, \bar{q}_R, m^*)$.

#### 2.2 The Bimodule $M_F$

The sum of all inequivalent irreducible odd $A_{LR}$-bimodules gives $M_F$ of dimension 32:

$$M_F = E \oplus E^0, \quad E = 2_L \otimes 1^0 \oplus 2_R \otimes 1^0 \oplus 2_L \otimes 3^0 \oplus 2_R \otimes 3^0$$

The antilinear isometry $J_F$ exchanges $E$ and $E^0$: $J_F(\xi, \bar{\eta}) = (\eta, \bar{\xi})$, with $J^2 = 1$.

#### 2.3 Real Spectral Triples

A real structure of KO-dimension $n \in \mathbb{Z}/8$ is an antilinear isometry $J: H \to H$ with:

$$J^2 = \epsilon, \quad JD = \epsilon'DJ, \quad J\gamma = \epsilon''\gamma J$$

The signs $(\epsilon, \epsilon', \epsilon'')$ are determined by the KO-dimension table (Definition 2.7). The order-one condition is $[[D,a], b^0] = 0$ for all $a, b \in A$, where $b^0 = Jb^*J^{-1}$.

#### 2.4 The Subalgebra

A central result: up to automorphism, there exists a unique subalgebra of maximal dimension admitting off-diagonal Dirac operators:

$$A_F = \{(\lambda, q_L, \lambda, m) \,|\, \lambda \in \mathbb{C},\, q_L \in \mathbb{H},\, m \in M_3(\mathbb{C})\} \cong \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$$

This is Proposition 2.11. The geometric requirement of allowing a Dirac operator that intertwines particles and antiparticles uniquely selects the SM algebra from the left-right symmetric algebra.

#### 2.5 Unimodularity and Hypercharges

The unimodular subgroup $SU(A_F) = \{u \in A_F \,|\, uu^* = u^*u = 1,\, \det(u) = 1\}$ gives:

$$SU(A_F) = U(1) \times SU(2) \times SU(3)$$

The hypercharge assignment follows from the unimodularity condition. The correct hypercharges of all SM fermions emerge from the grading operator $\gamma_F$ and the representation theory.

#### 2.6 Classification of Dirac Operators

The most general $D_F$ satisfying $J^2 = 1$, $[D,J] = 0$, $\{D,\gamma\} = 0$, and the order-one condition is parametrized by Yukawa matrices and a symmetric Majorana mass matrix $M_R$:

$$D(Y) = \begin{pmatrix} S & T^* \\ T & \bar{S} \end{pmatrix}$$

where $S$ contains the Dirac Yukawa couplings $Y_{(\uparrow 1)}, Y_{(\downarrow 1)}, Y_{(\uparrow 3)}, Y_{(\downarrow 3)}$ and $T$ contains the Majorana mass matrix $Y_R$ acting on the right-handed neutrino sector.

#### 2.7 Moduli Space and CKM Matrix

The moduli space of Dirac operators quotients by the natural equivalence relation from unitary transformations. For the quark sector, $C_3 \cong (U(3) \times U(3))\backslash(GL_3(\mathbb{C}) \times GL_3(\mathbb{C}))/U(3)$ of dimension 10. The CKM matrix $C \in SU(3)$ appears as the off-diagonal element: $Y_{(\uparrow 3)} = \delta_\uparrow$, $Y_{(\downarrow 3)} = C\delta_\downarrow C^*$.

#### 2.8 KO-Dimension 6

The finite space $F$ has KO-dimension 6 mod 8, meaning:

$$J_F^2 = 1, \quad J_F D_F = D_F J_F, \quad J_F\gamma_F = -\gamma_F J_F$$

The product $M \times F$ (with $M$ a 4-dimensional spin manifold of KO-dimension 4) has total KO-dimension $4 + 6 = 10 \equiv 2 \pmod{8}$.

### 3. The Spectral Action

#### 3.1-3.3 Product Geometry

The Hilbert space $H = L^2(M,S) \otimes H_F$ has dimension $N = 96$ per generation (4 spinor components $\times$ 24 fermions), giving $96 \times 3 = 288$ with 3 generations. The Dirac operator is:

$$D = \partial\!\!\!/\,_M \otimes 1 + \gamma_5 \otimes D_F$$

#### 3.4-3.5 Inner Fluctuations and Bosons

The inner fluctuations $D \to D_A = D + A + \epsilon'JAJ^{-1}$ generate the SM gauge fields:
- $U(1)_Y$ gauge field $B_\mu$
- $SU(2)_L$ gauge field $W_\mu$
- $SU(3)_c$ gauge field $V_\mu$
- Higgs doublet $\varphi$ from the $(0,1)$ fluctuations

The Higgs field $\varphi = (\varphi_1, \varphi_2)$ arises from the off-diagonal components of the inner fluctuation of $D_F$.

#### 3.7 The Spectral Action Theorem

**Theorem 3.13** gives the spectral action:

$$S = \frac{1}{\pi^2}(48f_4\Lambda^4 - f_2\Lambda^2 c + \frac{f_0}{4}d)\int\sqrt{g}\,d^4x$$
$$+ \frac{96f_2\Lambda^2 - f_0 c}{24\pi^2}\int R\sqrt{g}\,d^4x$$
$$+ \frac{f_0}{10\pi^2}\int(\frac{11}{6}R^*R^* - 3C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma})\sqrt{g}\,d^4x$$
$$+ \frac{-2af_2\Lambda^2 + ef_0}{\pi^2}\int|\varphi|^2\sqrt{g}\,d^4x$$
$$+ \frac{f_0}{2\pi^2}\int a|D_\mu\varphi|^2\sqrt{g}\,d^4x - \frac{f_0}{12\pi^2}\int aR|\varphi|^2\sqrt{g}\,d^4x$$
$$+ \frac{f_0}{2\pi^2}\int(g_3^2 G^i_{\mu\nu}G^{\mu\nu i} + g_2^2 F^\alpha_{\mu\nu}F^{\mu\nu\alpha} + \frac{5}{3}g_1^2 B_{\mu\nu}B^{\mu\nu})\sqrt{g}\,d^4x$$
$$+ \frac{f_0}{2\pi^2}\int b|\varphi|^4\sqrt{g}\,d^4x$$

The coefficients $(a, b, c, d, e)$ are defined by traces of Yukawa matrices:
- $a = \text{Tr}(Y_{(\uparrow 1)}^*Y_{(\uparrow 1)} + Y_{(\downarrow 1)}^*Y_{(\downarrow 1)} + 3(Y_{(\uparrow 3)}^*Y_{(\uparrow 3)} + Y_{(\downarrow 3)}^*Y_{(\downarrow 3)}))$
- $b = \text{Tr}((Y_{(\uparrow 1)}^*Y_{(\uparrow 1)})^2 + (Y_{(\downarrow 1)}^*Y_{(\downarrow 1)})^2 + 3((Y_{(\uparrow 3)}^*Y_{(\uparrow 3)})^2 + (Y_{(\downarrow 3)}^*Y_{(\downarrow 3)})^2))$
- $c = \text{Tr}(Y_R^*Y_R)$
- $d = \text{Tr}((Y_R^*Y_R)^2)$
- $e = \text{Tr}(Y_R^*Y_R(Y_{(\uparrow 1)}^*Y_{(\uparrow 1)} + Y_{(\downarrow 1)}^*Y_{(\downarrow 1)}))$

### 4. The Full SM Lagrangian

#### Theorem 4.3 (Main Result)

Let $M$ be a Riemannian spin 4-manifold and $F$ the finite NCG of KO-dimension 6. Then:

1. The unimodular subgroup acting by the adjoint representation is the SM gauge group.
2. The unimodular inner fluctuations give the SM gauge bosons.
3. The full SM (with neutrino mixing and see-saw) minimally coupled to Einstein gravity is:

$$S = \text{Tr}(f(D_A/\Lambda)) + \frac{1}{2}\langle J\tilde{\xi}, D_A\tilde{\xi}\rangle, \quad \tilde{\xi} \in H^+_{cl}$$

The fermion doubling problem is solved by using the Pfaffian rather than the determinant, restricting to $H^+ = \{\xi \in H : \gamma\xi = \xi\}$.

#### Normalized Action (eq. 4.11)

After rescaling and normalizing kinetic terms (with $g_3^2 f_0/(2\pi^2) = 1/4$):

$$S = \int\left[\frac{1}{2\kappa_0^2}R + \alpha_0 C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} + \gamma_0 + \tau_0 R^*R^* + \frac{1}{4}G^i_{\mu\nu}G^{\mu\nu i} + \frac{1}{4}F^\alpha_{\mu\nu}F^{\mu\nu\alpha} + \frac{1}{4}B_{\mu\nu}B^{\mu\nu}\right.$$
$$\left.+ \frac{1}{2}|D_\mu H|^2 - \mu_0^2|H|^2 - \xi_0 R|H|^2 + \lambda_0|H|^4\right]\sqrt{g}\,d^4x$$

with:

$$\frac{1}{\kappa_0^2} = \frac{96f_2\Lambda^2 - f_0 c}{12\pi^2}, \quad \mu_0^2 = \frac{2f_2\Lambda^2}{f_0} - \frac{e}{a}$$

$$\alpha_0 = \frac{-3f_0}{10\pi^2}, \quad \tau_0 = \frac{11f_0}{60\pi^2}, \quad \lambda_0 = \frac{\pi^2}{2f_0}\frac{b}{a^2}, \quad \xi_0 = \frac{1}{12}$$

### 5. Phenomenology and Predictions

#### 5.1 Coupling Constants at Unification

The gauge coupling unification relations: $g_3^2 = g_2^2 = \frac{5}{3}g_1^2$

With 1-loop RG running ($b = (41/6, -19/6, -7)$):

$$\alpha_i^{-1}(\Lambda) = \alpha_i^{-1}(M_Z) + \frac{b_i}{2\pi}\log\frac{\Lambda}{M_Z}$$

The couplings do not meet exactly, indicating new physics beyond the big desert.

#### 5.2 Higgs Mass Prediction

The Higgs quartic coupling at unification: $\tilde{\lambda}(\Lambda) = g_3^2 b/a^2$

In the top-quark dominance approximation: $\tilde{\lambda}(\Lambda) \simeq \frac{4}{3}\pi\alpha_3(\Lambda)$, giving $\lambda_0 \simeq 0.356$ at $\Lambda = 10^{17}$ GeV.

The Higgs mass (from RG running): $m_H \approx 170$ GeV. The RG equation:

$$\frac{d\lambda}{dt} = \lambda\gamma + \frac{1}{8\pi^2}(12\lambda^2 + B)$$

where $\gamma = \frac{1}{16\pi^2}(12y_t^2 - 9g_2^2 - 3g_1^2)$ and $B = \frac{3}{16}(3g_2^4 + 2g_1^2 g_2^2 + g_1^4) - 3y_t^4$.

#### 5.3 Neutrino See-Saw Mechanism

The Dirac operator restricted to the neutrino sector has a $4\times 4$ block (eq. 5.16) with Dirac mass $M_\nu$ and Majorana mass $M_R$. The see-saw formula gives light eigenvalues $\sim v^2/m_R$ and heavy eigenvalues $\sim m_R$. The Majorana mass scale is set by the spectral action equations of motion to $M_R \sim \Lambda$ (unification scale).

#### 5.4 Fermion-Boson Mass Relation

The mass relation at unification scale:

$$\sum_\sigma (m_\nu^\sigma)^2 + (m_e^\sigma)^2 + 3(m_u^\sigma)^2 + 3(m_d^\sigma)^2 = 8M_W^2$$

In terms of Yukawa couplings: $Y_2(S) = 4g^2$.

#### 5.5 Gravitational Terms

The gravitational constant: $\frac{1}{\kappa_0^2} = \frac{96f_2\Lambda^2 - f_0 c}{12\pi^2}$

The Weyl curvature coefficient: $\alpha_0 = -\frac{3f_0}{10\pi^2}$ (negative, corresponding to the correct sign for conformal gravity).

The cosmological constant depends on $f_4\Lambda^4$, the Majorana mass contribution ($c, d$), and the Higgs vev.

---

## Key Results

1. **Unique algebra selection:** The order-one condition on the Dirac operator uniquely selects $A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ as a subalgebra of $A_{LR} = \mathbb{C} \oplus \mathbb{H}_L \oplus \mathbb{H}_R \oplus M_3(\mathbb{C})$ (Proposition 2.11).

2. **KO-dimension 6:** The finite space $F$ has KO-dimension 6 mod 8 ($J^2 = 1$, $JD = DJ$, $J\gamma = -\gamma J$), resolving the fermion doubling problem.

3. **Full SM from spectral action:** The spectral action $\text{Tr}(f(D_A/\Lambda)) + \frac{1}{2}\langle J\tilde{\xi}, D_A\tilde{\xi}\rangle$ reproduces the complete SM Lagrangian coupled to Einstein gravity (Theorem 4.3).

4. **See-saw mechanism:** Naturally incorporated through the Majorana mass matrix $Y_R$ in the Dirac operator, with $M_R \sim \Lambda$ from equations of motion.

5. **CKM and PMNS matrices:** Arise from the moduli space of Dirac operators; the CKM matrix parametrizes the quark sector moduli $C_3$.

6. **Three predictions at unification:** GUT coupling relations, Higgs mass $\sim 170$ GeV (later corrected), and the fermion-boson mass relation $Y_2(S) = 4g^2$.

7. **Conformal coupling:** $\xi_0 = 1/12$ (differs slightly from the $1/6$ of the 1996 paper due to different Higgs normalization conventions).

8. **Pfaffian solution:** The fermion doubling problem is resolved by using the Pfaffian of an antisymmetric bilinear form $A_D(\xi', \xi) = \langle J\xi', D\xi\rangle$ on $H^+$, naturally dividing degrees of freedom by 4.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Left-right algebra | $A_{LR} = \mathbb{C} \oplus \mathbb{H}_L \oplus \mathbb{H}_R \oplus M_3(\mathbb{C})$ | Eq. (2.1) |
| SM algebra (subalgebra) | $A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C}) \subset A_{LR}$ | Eq. (2.22) |
| Bimodule | $E = 2_L \otimes 1^0 \oplus 2_R \otimes 1^0 \oplus 2_L \otimes 3^0 \oplus 2_R \otimes 3^0$ | Eq. (2.4) |
| KO-dim 6 signs | $J^2 = 1,\; JD = DJ,\; J\gamma = -\gamma J$ | Eq. (2.19) |
| Inner fluctuations | $D \to D_A = D + A + \epsilon'JAJ^{-1}$ | Eq. (2.15) |
| Spectral action (full) | Theorem 3.13 with terms $\Lambda^4$, $R$, $C^2$, $R^*R^*$, $|\varphi|^2$, $|D_\mu\varphi|^2$, $R|\varphi|^2$, gauge, $|\varphi|^4$ | Eq. (3.41) |
| Yukawa coefficients $a,b,c,d,e$ | Traces of Yukawa matrices | Eq. (3.16) |
| Full action | $S = \text{Tr}(f(D_A/\Lambda)) + \frac{1}{2}\langle J\tilde{\xi}, D_A\tilde{\xi}\rangle$ | Eq. (4.8) |
| Normalized bosonic action | $\frac{1}{2\kappa_0^2}R + \alpha_0 C^2 + \gamma_0 + \ldots + \lambda_0|H|^4$ | Eq. (4.11) |
| Parameter dictionary | $\kappa_0^{-2},\mu_0^2,\alpha_0,\tau_0,\gamma_0,\lambda_0,\xi_0$ in terms of $f_0,f_2,f_4,a,b,c,d,e$ | Eq. (4.12) |
| Gauge unification | $g_3^2 = g_2^2 = \frac{5}{3}g_1^2$ | Eq. (4.10) |
| Higgs coupling at $\Lambda$ | $\tilde{\lambda}(\Lambda) = g_3^2 b/a^2$ | Eq. (5.6) |
| Fermion mass relation | $\sum_\sigma(m_\nu^\sigma)^2 + (m_e^\sigma)^2 + 3(m_u^\sigma)^2 + 3(m_d^\sigma)^2 = 8M_W^2$ | Eq. (1.5) |
| See-saw eigenvalue | $M_R^*M_R = \frac{2f_2\Lambda^2}{f_0}\frac{k_R^*k_R\,\text{Tr}(k_R^*k_R)}{\text{Tr}((k_R^*k_R)^2)}$ | Eq. (5.20) |
| Higgs mass formula | $m_H = \sqrt{2\lambda}\,\frac{2M}{g}$ | Eq. (5.15) |
| RG for $\lambda$ | $\frac{d\lambda}{dt} = \lambda\gamma + \frac{1}{8\pi^2}(12\lambda^2 + B)$ | Eq. (5.13) |
| RG for $y_t$ | $\frac{dy_t}{dt} = \frac{1}{16\pi^2}[\frac{9}{2}y_t^3 - (\frac{17}{12}g_1^2 + \frac{9}{4}g_2^2 + 8g_3^2)y_t]$ | Eq. (5.9) |
| Pfaffian form | $A_D(\xi',\xi) = \langle J\xi', D\xi\rangle$ on $H^+$ | Eq. (4.3) |

---

## Relevance to Phonon-Exflation

This is the definitive reference paper for the NCG construction of the Standard Model that the phonon-exflation framework builds upon. Several elements are directly inherited by the framework: (1) The finite spectral triple with KO-dimension 6, algebra $\mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$, and 96-dimensional Hilbert space per generation is the starting point of the framework's spectral calculations. (2) The Yukawa coefficient dictionary $(a, b, c, d, e)$ in terms of traces of Yukawa matrices feeds directly into the framework's Seeley-DeWitt computations ($a_0, a_2, a_4$). (3) The Majorana mass matrix $Y_R$ and its role in the see-saw mechanism connects to the framework's BCS condensate structure on SU(3), where the condensate breaks $U(1)_7$ spontaneously. (4) The classification of Dirac operators and the moduli space structure inform the framework's analysis of the Dirac operator $D_K(\tau)$ at varying fiber complexity parameter $\tau$. (5) The fermion-boson mass relation $Y_2(S) = 4g^2$ provides a boundary condition that the framework must respect at unification scale.
