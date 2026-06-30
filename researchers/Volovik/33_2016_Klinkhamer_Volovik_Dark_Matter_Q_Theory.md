# Dark matter from dark energy in q-theory

**Author(s):** F.R. Klinkhamer, G.E. Volovik
**Year:** 2017
**Journal:** JETP Letters 105, 74 (2017)
**arXiv:** 1612.02326
**Relevance:** CRITICAL

---

## Abstract

A constant (spacetime-independent) q-field may play a crucial role for the cancellation of Planck-scale contributions to the gravitating vacuum energy density. We now show that a small spacetime-dependent perturbation of the equilibrium q-field behaves gravitationally as a pressureless perfect fluid. This makes the fluctuating part of the q-field a candidate for the inferred dark-matter component of the present universe. For a Planck-scale oscillation frequency of the q-field perturbation, the implication would be that direct searches for dark-matter particles would remain unsuccessful in the foreseeable future.

---

## Key Arguments and Derivations

### 1. Introduction
q-theory is a condensed-matter-type approach to the cosmological constant problem. An effective theory with conserved q-fields describes the thermodynamics and dynamics of the deep quantum vacuum without detailed knowledge of Planck-scale degrees of freedom. For constant q-fields, thermodynamics leads to exact cancellation of zero-point energies in equilibrium, partly solving the cosmological constant problem.

### 2. Setup
The action for q-theory based on a 3-form gauge field $A$ with 4-form field strength $F \propto q$:

$$S = -\int d^4x\sqrt{-g}\left(\frac{R}{16\pi G_N} + \epsilon(q) + \frac{1}{8}K(q)g^{\alpha\beta}\nabla_\alpha(q^2)\nabla_\beta(q^2) + L_{\text{SM}}\right)$$

where $q^2 \equiv -\frac{1}{24}F_{\alpha\beta\gamma\delta}F^{\alpha\beta\gamma\delta}$. The generalized Maxwell equation yields an integration constant $\mu$ (chemical potential of the conserved quantity). The energy-momentum tensor for constant $q$ gives $\Lambda_{\text{eff}}(q) = \rho_V(q) \equiv \epsilon(q) - q\,d\epsilon/dq$.

### 3. Equilibrium q-field
In equilibrium: $q = q_0$ (constant), $\mu_0 = d\epsilon/dq|_{q_0}$, and $\epsilon(q_0) - \mu_0 q_0 = 0$. This gives $\Lambda_{\text{eff}}(q_0) = \rho_V(q_0) = 0$ -- exact nullification of gravitating vacuum energy density. The stability condition requires positive inverse vacuum compressibility: $(q^2 d^2\epsilon/dq^2)|_{q_0} > 0$.

### 4. Pressureless Perfect Fluid (Dark Matter)
Consider a small perturbation $q(x) = q_0 + q_0\xi(x)$ with $|\xi| \ll 1$. The Klein-Gordon equation gives rapidly oscillating solutions:

$$\xi(t) = a_\xi\sin(\omega t + \phi_\xi), \quad \omega^2 = (q_0)^{-1}(\chi_0)^{-1} \sim E_P^2$$

The energy-momentum tensor for this oscillation:
- $T^{(q)}_{00} = \frac{1}{2}(\chi_0)^{-1}(a_\xi)^2$ (energy density)
- $\langle T^{(q)}_{11}\rangle = \langle T^{(q)}_{22}\rangle = \langle T^{(q)}_{33}\rangle \sim 0$ (time-averaged pressure vanishes)

This is a pressureless perfect fluid -- cold dark matter. The q-field perturbation clusters gravitationally just like CDM for length scales $L \gg c/\omega \sim l_P \sim 10^{-35}$ m.

### 5. Conclusion
The fluctuating part of the q-field is a dark matter candidate. If the oscillation frequency is Planck-scale, direct detection of dark-matter particles will fail. Open questions: the mechanism producing the small constant $\delta q$ (dark energy) and the perturbative $\xi(x)$ (dark matter), and the correct ratio $\rho_{\text{DE}}/\rho_{\text{DM}} \sim 3$.

---

## Key Results

1. Constant q-field automatically cancels Planck-scale vacuum energy: $\Lambda_{\text{eff}}(q_0) = 0$
2. Small spacetime-dependent perturbation of q-field behaves as pressureless perfect fluid (CDM)
3. Oscillation frequency is Planck-scale: $\omega \sim E_P$
4. Dark matter and dark energy are two aspects of the same q-field: constant part gives $\Lambda = 0$ (with small residual $\delta q$ for dark energy), oscillating part gives dark matter
5. Direct DM detection predicted to fail if this picture is correct
6. The q-field energy-momentum tensor for perturbations has the same structure as a fundamental scalar field

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| q-theory action | $S = -\int d^4x\sqrt{-g}\left(\frac{R}{16\pi G_N} + \epsilon(q) + \frac{1}{8}K(q)g^{\alpha\beta}\nabla_\alpha(q^2)\nabla_\beta(q^2) + L_{\text{SM}}\right)$ | Eq. (1a) |
| Gravitating vacuum energy | $\Lambda_{\text{eff}}(q) = \rho_V(q) \equiv \epsilon(q) - q\,d\epsilon/dq$ | Eq. (7) |
| Equilibrium nullification | $\epsilon(q_0) - \mu_0 q_0 = 0 \implies \Lambda_{\text{eff}}(q_0) = 0$ | Eqs. (8c), (9) |
| Stability condition | $(\chi_0)^{-1} \equiv [q^2 d^2\epsilon/dq^2]_{q_0} > 0$ | Eq. (10) |
| Oscillation frequency | $\omega^2 = (q_0)^{-1}(\chi_0)^{-1} \sim E_P^2$ | Eq. (17b) |
| DM energy density | $\rho_{\text{DM}} = T^{(q)}_{00} = \frac{1}{2}(\chi_0)^{-1}(a_\xi)^2$ | Eq. (21a) |
| DM pressure | $P_{\text{DM}} \sim 0$ | Eq. (21b) |

---

## Relevance to Phonon-Exflation

This paper is CRITICAL for the framework because:

1. **q-theory IS the framework's vacuum variable**: The 4-form field $q$ providing a dynamic vacuum variable that self-tunes $\Lambda = 0$ is exactly the mechanism the framework uses. The user has noted "q-theory is F-theory in a dress" -- same variational principle $d\rho/dq = 0 \leftrightarrow dV/d\phi = 0$.

2. **Dark matter from vacuum oscillations**: The prediction that DM is a Planck-frequency oscillation of the vacuum variable -- not a particle -- aligns with the framework's prediction that DM arises from quasiparticle dispersion on the phononic substrate rather than from new fundamental particles.

3. **Cosmological constant solution**: The thermodynamic self-tuning $\Lambda_{\text{eff}}(q_0) = 0$ without fine-tuning is the foundation of the framework's approach to the CC problem (sessions 22-38).

4. **Direct detection prediction**: The framework's "dark matter from vacuum" picture makes the same prediction as Klinkhamer-Volovik: direct detection experiments will not find DM particles.

5. **Two dark sectors from one field**: The unified origin of dark energy (constant $\delta q$) and dark matter (oscillating $\xi$) from a single vacuum field is the framework's central structural prediction.
