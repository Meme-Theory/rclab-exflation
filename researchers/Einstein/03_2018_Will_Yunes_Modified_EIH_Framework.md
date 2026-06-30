# Testing General Relativity with Compact-Body Orbits: A Modified Einstein-Infeld-Hoffmann Framework

**Author(s):** Clifford M. Will
**Year:** 2018
**Journal:** Classical and Quantum Gravity (accepted)
**arXiv:** 1801.08999
**Relevance:** CRITICAL

---

## Abstract

We describe a general framework for analyzing orbits of systems containing compact objects (neutron stars or black holes) in a class of Lagrangian-based alternative theories of gravity that also admit a global preferred reference frame. The framework is based on a modified Einstein-Infeld-Hoffmann (EIH) formalism developed by Eardley and by Will, generalized to include the possibility of Lorentz-violating, preferred-frame effects. It uses a post-Newtonian N-body Lagrangian with arbitrary parameters that depend on the theory of gravity and on "sensitivities" that encode the effects of the bodies' internal structure on their motion. We determine the modified EIH parameters for the Einstein-Aether and Khronometric vector-tensor theories of gravity. We find the effects of motion relative to a preferred universal frame on the orbital parameters of binary systems containing neutron stars, such as a class of ultra-circular pulsar-white dwarf binaries; the amplitudes of the effects depend upon "strong-field" preferred-frame parameters $\hat{\alpha}_1$ and $\hat{\alpha}_2$, which we relate to the fundamental modified EIH parameters. We also determine the amplitude of the "Nordtvedt effect" in a triple system containing the pulsar J0337+1715 in terms of the modified EIH parameters.

---

## Key Arguments and Derivations

### 1. Motivation: Structure Dependence in Alternative Theories

In GR, the N-body equations of motion for compact bodies are identical to those of the post-Newtonian limit with weak fields everywhere -- the bodies move on geodesics of the interbody metric independent of their internal structure (Strong Equivalence Principle). In alternative theories, additional gravitational fields ($\psi_A$) influence the structure of each body via their boundary values in the matching region. The inertial mass $m_a$ becomes a function of these external fields: $m_a(\psi_A)$.

The key idea is to expand $m_a(\psi_A)$ about the asymptotic values and define dimensionless "sensitivities":
$$s_a^{(A)} \equiv \frac{\partial \ln m_a}{\partial \ln \psi_A^{(0)}}, \quad s_a'^{(AB)} \equiv \frac{\partial^2 \ln m_a}{\partial \ln \psi_A^{(0)} \partial \ln \psi_B^{(0)}}$$

These sensitivities encode how a body's inertial mass responds to changes in the external gravitational environment.

### 2. The Modified EIH Lagrangian

The paper constructs a general 1PN N-body Lagrangian with body-dependent parameters:
$$L_{\text{EIH}} = -\sum_a m_a \left[1 - \frac{1}{2}v_a^2 - \frac{1}{8}(1 + A_a)v_a^4\right] + \frac{1}{2}\sum_{a \neq b} \frac{m_a m_b}{r_{ab}} \left[\mathcal{G}_{ab} + 3\mathcal{B}_{ab}v_a^2 - \frac{1}{2}(\mathcal{G}_{ab} + 6\mathcal{B}_{(ab)} + \mathcal{C}_{ab})v_a \cdot v_b - \frac{1}{2}(\mathcal{G}_{ab} + \mathcal{E}_{ab})(v_a \cdot n_{ab})(v_b \cdot n_{ab})\right] - \frac{1}{2}\sum_{a \neq b \neq c} \mathcal{D}_{abc} \frac{m_a m_b}{r_{ab}} \frac{m_c}{r_{ac}}$$

The parameters $A_a$, $\mathcal{G}_{ab}$, $\mathcal{B}_{ab}$, $\mathcal{C}_{ab}$, $\mathcal{E}_{ab}$, $\mathcal{D}_{abc}$ depend on the theory and on the structure of each body.

In GR: $\mathcal{G}_{ab} = \mathcal{B}_{ab} = \mathcal{D}_{abc} = 1$, $A_a = \mathcal{C}_{ab} = \mathcal{E}_{ab} = 0$. The preferred-frame parameters vanish:
$$A_a \equiv \mathcal{B}_{[ab]} \equiv \mathcal{C}_{ab} \equiv \mathcal{E}_{ab} \equiv 0$$
if and only if the Lagrangian is post-Galilean invariant.

### 3. Scalar-Tensor Theories

For massless scalar-tensor theory (Brans-Dicke and generalizations), the sensitivities $s_a$ measure the response of $m_a$ to changes in the scalar field $\phi$. The modified EIH parameters become:
$$\mathcal{G}_{ab} = 1 - 2\zeta(s_a + s_b - 2s_a s_b)$$
$$\mathcal{B}_{ab} = \frac{1}{3}[\mathcal{G}_{ab} + 2(1 - \zeta)]$$
where $\zeta = 1/(4 + 2\omega_0)$. All preferred-frame parameters vanish: $A_a = \mathcal{B}_{[ab]} = \mathcal{C}_{ab} = \mathcal{E}_{ab} = 0$.

### 4. Einstein-Aether Theory

In Einstein-Aether theory, the sensitivities are defined via $\gamma \equiv -K_\mu u^\mu \equiv 1 + \Psi$. The modified EIH parameters are:
$$\mathcal{G}_{ab} = \frac{G_N}{(1 - s_a)(1 - s_b)}, \quad \mathcal{B}_{ab} = \mathcal{G}_{ab}(1 - s_a)$$
The PPN preferred-frame parameters are:
$$\alpha_1 = -\frac{8(c_3^2 + c_1 c_4)}{2c_1 - c_1^2 + c_3^2}$$

### 5. Two-Body Dynamics and Observable Effects

For a two-body system, the relative acceleration splits into "local" and "preferred-frame" parts: $\mathbf{a} = \mathbf{a}_L + \mathbf{a}_{\text{PF}}$. The local part gives the standard pericenter advance:
$$\Delta\omega = \frac{6\pi m}{p}\mathcal{P}\mathcal{G}^{-1}$$
where $\mathcal{P}$ depends on the EIH parameters.

The preferred-frame part induces a forced eccentricity in ultra-circular binary pulsars:
$$r/a = 1 - e_0\cos(\phi - \omega_0 - \omega'\phi) - \frac{1}{4}\hat{\alpha}_1 \Delta\left(\frac{m}{a}\right)^{1/2}\frac{w}{\omega'}(\hat{w}_\perp\cos\phi - \hat{w}_\Omega\sin\phi) + \ldots$$

where the "strong-field" preferred-frame parameters are:
$$\hat{\alpha}_1 = \Delta(\mathcal{C} + \mathcal{E}) - 6\mathcal{B}_- - 2\mathcal{G}\mathcal{A}^{(2)}$$
$$\hat{\alpha}_2 = \mathcal{E} - \mathcal{G}\mathcal{A}^{(1)}$$

### 6. Nordtvedt Effect in Triple Systems

For the triple system J0337+1715 (pulsar + two white dwarfs), the perturbation of the inner orbit is:
$$\delta r = -\hat{\eta}_N R \frac{a_0 \omega_b^2(1 + 2\omega_b/\Lambda)}{\omega_b^2 - \Lambda^2}\cos(\Lambda t + \Phi)$$
where the strong-field Nordtvedt parameter is $\hat{\eta}_N \equiv \mathcal{G}_{12} - \mathcal{G}_{13}$. For scalar-tensor theory: $\hat{\eta}_N = -\zeta s_1$. For Einstein-Aether: $\hat{\eta}_N = s_1/(1 - s_1)$.

---

## Key Results

1. Generalized modified EIH formalism to include preferred-frame effects.
2. Derived modified EIH parameters for scalar-tensor, Einstein-Aether, and Khronometric theories.
3. Related "strong-field" parameters $\hat{\alpha}_1$, $\hat{\alpha}_2$ to fundamental theory parameters and body sensitivities.
4. Binary pulsar J1738+0333 bounds: $|\hat{\alpha}_1| < 3.4 \times 10^{-5}$.
5. Combined pulsar bounds: $|\hat{\alpha}_2| < 1.8 \times 10^{-4}$.
6. Nordtvedt effect in J0337+1715 parameterized in terms of modified EIH parameters.
7. GR satisfies all conditions exactly: $\mathcal{G}_{ab} = \mathcal{B}_{ab} = \mathcal{D}_{abc} = 1$, all preferred-frame parameters zero.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| GR action | $I = \frac{1}{16\pi G}\int R\sqrt{-g}\,d^4x - \sum_a m_a \int d\tau_a$ | Eq. (1) |
| Alternative theory action | $I = I_G - \sum_a \int m_a(\psi_A) d\tau_a$ | Eq. (4) |
| Sensitivity definition | $s_a^{(A)} = \partial\ln m_a / \partial\ln\psi_A^{(0)}$ | Eq. (6) |
| EIH Lagrangian | $L_{\text{EIH}} = -\sum_a m_a[1 - v_a^2/2 - (1+A_a)v_a^4/8] + \frac{1}{2}\sum_{a\neq b}\frac{m_a m_b}{r_{ab}}[\mathcal{G}_{ab} + 3\mathcal{B}_{ab}v_a^2 - \ldots]$ | Eq. (9) |
| GR values | $\mathcal{G}_{ab} = \mathcal{B}_{ab} = \mathcal{D}_{abc} = 1$; $A_a = \mathcal{C}_{ab} = \mathcal{E}_{ab} = 0$ | Below Eq. (11) |
| Post-Galilean invariance | $A_a \equiv \mathcal{B}_{[ab]} \equiv \mathcal{C}_{ab} \equiv \mathcal{E}_{ab} \equiv 0$ | Eq. (17) |
| Scalar-tensor sensitivity | $s_a \equiv (d\ln m_a(\phi)/d\ln\phi)_0$ | Eq. (20) |
| Scalar-tensor $\mathcal{G}_{ab}$ | $\mathcal{G}_{ab} = 1 - 2\zeta(s_a + s_b - 2s_a s_b)$ | Eq. (29) |
| Einstein-Aether $\alpha_1$ | $\alpha_1 = -8(c_3^2 + c_1 c_4)/(2c_1 - c_1^2 + c_3^2)$ | Eq. (38) |
| Pericenter advance | $\Delta\omega = 6\pi m \mathcal{P}\mathcal{G}^{-1}/p$ | Eq. (52) |
| Strong-field $\hat{\alpha}_1$ | $\hat{\alpha}_1 = \Delta(\mathcal{C} + \mathcal{E}) - 6\mathcal{B}_- - 2\mathcal{G}\mathcal{A}^{(2)}$ | Eq. (50) |
| Nordtvedt parameter | $\hat{\eta}_N \equiv \mathcal{G}_{12} - \mathcal{G}_{13}$ | Eq. (63) |

---

## Relevance to Phonon-Exflation

This paper provides the theoretical framework for understanding how internal structure (via "sensitivities") could modify the motion of compact bodies in alternative gravity theories. For the phonon-exflation framework, the SU(3) fiber constitutes the "internal structure" of every body. The framework's central prediction is exact effacement: the SU(3) fiber sensitivities $s_a^{(\tau)} = 0$ identically, meaning the fiber modulus $\tau$ does not contribute to a body's gravitational mass differently than its inertial mass. This is the framework's analog of GR's Strong Equivalence Principle. The modified EIH formalism provides the precise mathematical language for stating this prediction: if $s_a = 0$ for all bodies, then $\mathcal{G}_{ab} = 1$, $\hat{\eta}_N = 0$, and all preferred-frame parameters vanish -- exactly the GR values.
