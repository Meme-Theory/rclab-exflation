# Resilience of the Spectral Standard Model

**Author(s):** Ali H. Chamseddine and Alain Connes
**Year:** 2012
**Journal:** Fortschr. Phys. 60, 983-989 (2012)
**arXiv:** 1208.1030
**Relevance:** HIGH

---

## Abstract

We show that the inconsistency between the spectral Standard Model and the experimental value of the Higgs mass is resolved by the presence of a real scalar field strongly coupled to the Higgs field. This scalar field was already present in the spectral model and we wrongly neglected it in our previous computations. It was shown recently by several authors, independently of the spectral approach, that such a strongly coupled scalar field stabilizes the Standard Model up to unification scale in spite of the low value of the Higgs mass. In this letter we show that the noncommutative neutral singlet modifies substantially the RG analysis, invalidates our previous prediction of Higgs mass in the range 160-180 GeV, and restores the consistency of the noncommutative geometric model with the low Higgs mass.

---

## Key Arguments and Derivations

### I. Introduction

The paper addresses a crisis in the NCG spectral model: the original prediction of $m_H \approx 160$-$180$ GeV was falsified by the experimental discovery at $\sim 125$ GeV. Two problems arise from the low Higgs mass: (1) the direct discrepancy with prediction, and (2) more seriously, a low Higgs mass makes the quartic coupling $\lambda$ go negative at high energies, ruling out the "big desert" hypothesis and invalidating the positivity of the coupling at unification, which is an essential prediction of the spectral action.

The resolution is that the full spectral action (as computed in the authors' 2010 paper) already contains a real scalar singlet field $\sigma$ associated with the Majorana mass of the right-handed neutrino. This field was previously neglected by assuming it could be integrated out. In fact, its couplings to the Higgs are exactly those independently proposed by several groups to stabilize the SM.

### II. Higgs-Singlet Scalar Potential

The spectral action for the SM gives a potential involving both the Higgs doublet $H$ and the real scalar singlet $\sigma$:

$$-\frac{2}{\pi^2}f_2\Lambda^2\int d^4x\sqrt{g}\left(\frac{1}{2}a\,H^\dagger H + \frac{1}{4}c\,\sigma^2\right)$$
$$+ \frac{1}{2\pi^2}f_0\int d^4x\sqrt{g}\left(b(H^\dagger H)^2 + a|{\nabla_\mu H_a}|^2 + 2e\,H^\dagger H\,\sigma^2 + \frac{1}{2}d\,\sigma^4 + \frac{1}{2}c\,(\partial_\mu\sigma)^2\right)$$

In the approximation where the top quark Yukawa $k_u$ and neutrino Yukawa couplings (both Dirac $k_\nu$ and Majorana $k_{\nu R}$) dominate, with $k_\nu = \sqrt{n}\, k_u$:

$$a = |k_u|^2(n+3), \quad b = |k_u|^4(n^2+3)$$
$$c = |k_{\nu R}|^2, \quad d = |k_{\nu R}|^4, \quad e = n|k_{\nu R}|^2|k_u|^2$$

After rescaling to normalized kinetic terms ($h \to h\sqrt{2/(n+3)}g$, $\sigma \to 2\sigma g$), the Higgs-singlet potential reduces to:

$$V = \frac{1}{4}\left(\lambda_h h^4 + 2\lambda_{h\sigma}h^2\sigma^2 + \lambda_\sigma\sigma^4\right) - \frac{2g^2}{\pi^2}f_2\Lambda^2(h^2 + \sigma^2)$$

with quartic couplings at unification:

$$\lambda_h = \frac{n^2+3}{(n+3)^2}\cdot 4g^2, \quad \lambda_{h\sigma} = \frac{2n}{n+3}\cdot 4g^2, \quad \lambda_\sigma = 2\cdot 4g^2$$

Key observations:
- The singlet has strong coupling: $\lambda_\sigma = 8g^2$
- The portal coupling $\lambda_{h\sigma}$ vanishes for $n = 0$ and increases to $8g^2$ as $n \to \infty$
- The Higgs quartic $\lambda_h$ ranges from $\frac{4}{3}g^2$ to $4g^2$ depending on $n$

### III. Running the RG Equations

The 1-loop RG equations for the coupled Higgs-singlet system are:

$$\frac{dk_t}{dt} = \frac{k_t}{32\pi^2}\left[-\left(\frac{17}{6}g_1^2 + \frac{9}{2}g_2^2 + 16g_3^2\right) + 9k_t^2 + 2k_\nu^2\right]$$

$$\frac{dk_\nu}{dt} = \frac{k_\nu}{32\pi^2}\left[-\left(\frac{3}{2}g_1^2 + \frac{9}{2}g_2^2\right) + 6k_t^2 + 5k_\nu^2\right]$$

$$\frac{d\lambda_h}{dt} = \frac{1}{16\pi^2}\left[12(k_t^2 + 4k_\nu^2) - (3g_1^2 + 9g_2^2)\right]\lambda_h + 2\left[12\lambda_h^2 + \lambda_{h\sigma}^2 + \frac{3}{16}(g_1^4 + 2g_1^2 g_2^2 + 3g_2^4) - 3(k_t^4 - k_\nu^4)\right]$$

$$\frac{d\lambda_{h\sigma}}{dt} = \frac{\lambda_{h\sigma}}{16\pi^2}\left[\frac{1}{2}(12(k_t^2 + 4k_\nu^2) - 3g_1^2 - 9g_2^2) + 4(3\lambda_h + \frac{3}{2}\lambda_\sigma + 2\lambda_{h\sigma})\right]$$

$$\frac{d\lambda_\sigma}{dt} = \frac{1}{16\pi^2}\left[8\lambda_{h\sigma}^2 + 18\lambda_\sigma^2\right]$$

The top quark Yukawa coupling at unification is:

$$k_t(u_{\text{unif}}) = \sqrt{\frac{4}{n+3}}\,g$$

### IV. Mass Spectrum and Higgs Mass Correction

The potential minimum occurs at $\langle h^2\rangle = v^2$, $\langle\sigma^2\rangle = w^2$ with:

$$-\mu^2 + v^2\lambda_h + w^2\lambda_{h\sigma} = 0, \quad -\nu^2 + v^2\lambda_{h\sigma} + w^2\lambda_\sigma = 0$$

The mass matrix after expanding $h = v + \phi$, $\sigma = w + \tau$ is:

$$M^2 = 2\begin{pmatrix} \lambda_h v^2 & \lambda_{h\sigma}vw \\ \lambda_{h\sigma}vw & \lambda_\sigma w^2\end{pmatrix}$$

The eigenvalues in the approximation $v^2 \ll w^2$:

$$m_+^2 \simeq 2\lambda_\sigma w^2 + \frac{2\lambda_{h\sigma}^2}{\lambda_\sigma}v^2$$

$$m_-^2 \simeq 2\lambda_h v^2\left(1 - \frac{\lambda_{h\sigma}^2}{\lambda_h\lambda_\sigma}\right)$$

The Higgs mass is **reduced** by the factor $\sqrt{1 - \lambda_{h\sigma}^2/(\lambda_h\lambda_\sigma)}$, which is of order 0.78 at low scale. The stability condition is $\lambda_{h\sigma}^2 < \lambda_h\lambda_\sigma$.

The physical masses are:

$$m_t(0) = k_t(0)\frac{246}{\sqrt{2}}, \quad m_h(0) = 246\sqrt{2\lambda_h(0)\left(1 - \frac{\lambda_{h\sigma}^2(0)}{\lambda_h(0)\lambda_\sigma(0)}\right)}$$

### V. Numerical Results

Varying the parameter $n$ and the unification scale $u_{\text{unif}} = \log(\Lambda_{\text{unif}}/M_Z)$ in the range $(25, 35)$ (corresponding to $6.5 \times 10^{12}$ to $1.4 \times 10^{17}$ GeV):

- A Higgs mass of $\sim 125.5$ GeV is achieved along a nearly straight curve in the $(n, u)$ parameter space
- All three quartic couplings $\lambda_h, \lambda_{h\sigma}, \lambda_\sigma$ remain positive in the RG running
- The stability condition $\lambda_{h\sigma}^2 < \lambda_h\lambda_\sigma$ holds at low scale
- The correction factor $\sqrt{1 - \lambda_{h\sigma}^2/(\lambda_h\lambda_\sigma)} \simeq 0.785$-$0.795$ at $u = 0$
- The top quark mass is a few percent low at 1-loop (expected to improve at 2-loop)

### VI. Conclusions

The key lesson: all fields of the NCG spectral model must be taken seriously. The singlet $\sigma$ responsible for Majorana neutrino mass plays a central role in:
1. Breaking the symmetry of the discrete space from $\mathbb{H} \oplus \mathbb{H} \oplus M_4(\mathbb{C})$ to $\mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$
2. Stabilizing the Higgs potential at high energies
3. Correcting the Higgs mass prediction from $\sim 170$ GeV down to $\sim 125$ GeV

The model predicts only three scalar fields: the Higgs, the singlet $\sigma$, and a dilaton field (from scale invariance of the spectral action).

---

## Key Results

1. **Higgs mass crisis resolved:** The real scalar singlet $\sigma$ from the Majorana sector, already present in the spectral action but previously neglected, reduces the Higgs mass prediction from 170 GeV to $\sim 125$ GeV.

2. **Mass reduction factor:** $m_h = m_{h,0}\sqrt{1 - \lambda_{h\sigma}^2/(\lambda_h\lambda_\sigma)} \approx 0.78\,m_{h,0}$

3. **Vacuum stability restored:** The positive singlet quartic coupling $\lambda_\sigma = 8g^2$ and the portal coupling $\lambda_{h\sigma}$ prevent the Higgs quartic coupling from going negative at high energies.

4. **Consistency with experiment:** For $n \in (1.6, 2.4)$ and $u_{\text{unif}} \in (25, 35)$, the model produces $m_h \approx 125.5$ GeV with all quartic couplings remaining positive.

5. **Three scalars predicted:** The NCG model predicts exactly three scalar fields: Higgs doublet, real singlet $\sigma$, and dilaton. No other particles.

6. **Same couplings as stability proposals:** The Higgs-singlet potential from the spectral action has exactly the same structure independently proposed by Elias-Miro et al. and others for SM stabilization.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Higgs-singlet potential | $V = \frac{1}{4}(\lambda_h h^4 + 2\lambda_{h\sigma}h^2\sigma^2 + \lambda_\sigma\sigma^4) - \frac{2g^2}{\pi^2}f_2\Lambda^2(h^2 + \sigma^2)$ | Eq. (12) |
| $\lambda_h$ at unification | $\lambda_h = \frac{n^2+3}{(n+3)^2}\cdot 4g^2$ | Eq. (13) |
| $\lambda_{h\sigma}$ at unification | $\lambda_{h\sigma} = \frac{2n}{n+3}\cdot 4g^2$ | Eq. (14) |
| $\lambda_\sigma$ at unification | $\lambda_\sigma = 2\cdot 4g^2 = 8g^2$ | Eq. (15) |
| Yukawa-neutrino relation | $k_\nu = \sqrt{n}\,k_u$ | Eq. (2) |
| Top Yukawa at unification | $k_t(u_{\text{unif}}) = \sqrt{\frac{4}{n+3}}\,g$ | Eq. (22) |
| Mass matrix | $M^2 = 2\begin{pmatrix}\lambda_h v^2 & \lambda_{h\sigma}vw \\ \lambda_{h\sigma}vw & \lambda_\sigma w^2\end{pmatrix}$ | Eq. (29) |
| Heavy eigenvalue | $m_+^2 \simeq 2\lambda_\sigma w^2 + \frac{2\lambda_{h\sigma}^2}{\lambda_\sigma}v^2$ | Eq. (31) |
| Light eigenvalue (Higgs) | $m_-^2 \simeq 2\lambda_h v^2(1 - \frac{\lambda_{h\sigma}^2}{\lambda_h\lambda_\sigma})$ | Eq. (32) |
| Stability condition | $\lambda_{h\sigma}^2 < \lambda_h\lambda_\sigma$ | Eq. (33) |
| Top mass at low scale | $m_t(0) = k_t(0)\frac{246}{\sqrt{2}}$ | Eq. (34) |
| Higgs mass at low scale | $m_h(0) = 246\sqrt{2\lambda_h(0)(1 - \frac{\lambda_{h\sigma}^2(0)}{\lambda_h(0)\lambda_\sigma(0)})}$ | Eq. (35) |
| RG for $\lambda_h$ | $\frac{d\lambda_h}{dt} = \frac{1}{16\pi^2}[\ldots]\lambda_h + 2[12\lambda_h^2 + \lambda_{h\sigma}^2 + \ldots]$ | Eq. (18) |
| RG for $\lambda_{h\sigma}$ | $\frac{d\lambda_{h\sigma}}{dt} = \frac{\lambda_{h\sigma}}{16\pi^2}[\ldots + 4(3\lambda_h + \frac{3}{2}\lambda_\sigma + 2\lambda_{h\sigma})]$ | Eq. (19) |
| RG for $\lambda_\sigma$ | $\frac{d\lambda_\sigma}{dt} = \frac{1}{16\pi^2}[8\lambda_{h\sigma}^2 + 18\lambda_\sigma^2]$ | Eq. (20) |
| Coefficient $a$ | $a = |k_u|^2(n+3)$ | Eq. (3) |
| Coefficient $e$ (portal) | $e = n|k_{\nu R}|^2|k_u|^2$ | Eq. (7) |

---

## Relevance to Phonon-Exflation

The Resilience paper is directly relevant to the phonon-exflation framework in multiple ways. First, the Higgs-singlet portal structure with potential $V(\lambda_h, \lambda_{h\sigma}, \lambda_\sigma)$ is the same scalar sector that the framework inherits from the spectral action on $M^4 \times F$; the framework's closure of the "Higgs-sigma portal" mechanism (Session 22c, Trap 3) was informed by this structure. Second, the singlet field $\sigma$ associated with the Majorana mass matrix $Y_R$ connects to the framework's treatment of the right-handed neutrino sector and the BCS condensate on SU(3). Third, the correction factor $\sqrt{1 - \lambda_{h\sigma}^2/(\lambda_h\lambda_\sigma)} \sim 0.78$ demonstrates that scalar mixing effects are numerically significant -- a lesson the framework applied when analyzing spectral action contributions at the fold. Fourth, the RG system for the coupled $(h, \sigma)$ sector provides the boundary conditions that the framework's computation computations must respect when evolving the spectral coefficients. Finally, the paper's conclusion that the NCG model predicts exactly three scalars (Higgs, singlet, dilaton) constrains the particle content available to the framework's phenomenology.
