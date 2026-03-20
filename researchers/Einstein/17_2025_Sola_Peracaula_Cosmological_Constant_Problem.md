# The Cosmological Constant Problem: From Newtonian Cosmology to the Greatest Puzzle of Modern Theoretical Cosmology

**Author:** Joan Solà Peracaula

**Year:** 2025

**Journal:** Philosophical Transactions of the Royal Society A, vol. 383, no. 2311, article 20230292

---

## Abstract

This comprehensive review traces the cosmological constant problem from its origins in Newtonian gravity and General Relativity through quantum field theory to modern observational challenges. The paper synthesizes classical and quantum aspects, covering Einstein's original Lambda, observational discoveries (Type Ia supernovae, CMB, BAO), vacuum energy density paradoxes, and proposed solutions including the Running Vacuum Model (RVM). Solà Peracaula argues that the cosmological constant is not a true fundamental constant but rather a "running parameter" that evolves with the universe's expansion, similar to the running coupling in quantum chromodynamics. This reframing resolves several tensions between theory and observation.

---

## Historical Context

The cosmological constant appears first in Einstein's 1917 field equations as a term added to maintain a static universe:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

Einstein called it the "cosmological constant." When Hubble discovered cosmic expansion (1929), the need for Lambda vanished, and Einstein called its introduction his "greatest blunder."

For decades, Lambda was considered zero or negligible. But in 1998, Type Ia supernova observations (Riess et al., Perlmutter et al.) revealed accelerating expansion, implying a positive, non-zero Lambda. The measured value is:

$$\Lambda \sim 10^{-52} \text{ m}^{-2} \quad \text{or} \quad \rho_\Lambda \sim 10^{-47} \text{ GeV}^4$$

**The Problem**: Vacuum energy in quantum field theory is estimated as:

$$\rho_{\text{vac}}^{\text{QFT}} \sim M_{\text{Planck}}^4 \sim 10^{113} \text{ GeV}^4$$

The discrepancy is 160 orders of magnitude—the "worst prediction in physics." Conventional approaches (cosmological constant as a true constant, quintessence with a contrived potential) have failed to explain this naturalness crisis.

Solà's running vacuum model emerged in the 2000s as a radical reinterpretation: what if Lambda is not a constant, but a running parameter that decreases with cosmic time, like the strong coupling constant $\alpha_s$ in QCD?

---

## Key Arguments and Derivations

### Classical Origin of the Cosmological Constant

In Einstein's formulation (1917), the field equations include Lambda explicitly:

$$R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

Geometrically, Lambda is a curvature parameter characterizing the "vacuum" geometry of spacetime. The trace of the field equation gives:

$$R - 2\Lambda = -8\pi G T$$

In a vacuum (T=0), the Einstein tensor $G_{\mu\nu}$ has zero divergence by the Bianchi identities, implying R = constant everywhere (homogeneous curvature). For a cosmological solution (FLRW metric), the Ricci scalar depends on the scale factor a(t):

$$R(t) = 6\left(\frac{\ddot{a}}{a} + \frac{\dot{a}^2}{a^2} + \frac{k}{a^2}\right)$$

For a flat universe ($k=0$), if $\Lambda=0$, then $R = 6(\ddot{a}/a + \dot{a}^2/a^2)$. Einstein required $\ddot{a} = 0$ (static universe), which forced $\dot{a}=0$ (universe at rest). To achieve this with matter (requiring $\ddot{a}<0$), he introduced Lambda > 0 to balance the attractive gravity. The static solution is:

$$a(t) = \text{constant}, \quad \rho + 3p = 0$$

This requires $\rho_\Lambda + 3 p_\Lambda = 0$, or $p_\Lambda = -\rho_\Lambda$ (vacuum equation of state $w = -1$).

### Quantum Field Theory Origin and the Vacuum Energy Crisis

In quantum field theory, the vacuum state is not empty. Virtual particle-antiparticle pairs fluctuate at all energy scales. The zero-point energy of a scalar field is:

$$E_0 = \frac{1}{2} \hbar \omega$$

for each mode. Summing over all modes up to a cutoff $\Lambda_{\text{UV}}$:

$$\rho_{\text{vac}} = \int_0^{\Lambda_{\text{UV}}} \frac{d^3 k}{(2\pi)^3} \frac{1}{2} \omega_k \sim \frac{\Lambda_{\text{UV}}^4}{(2\pi)^2}$$

If we set $\Lambda_{\text{UV}} = M_{\text{Planck}}$, we get $\rho_{\text{vac}} \sim 10^{113}$ GeV$^4$, vastly exceeding observations ($\rho_\Lambda \sim 10^{-47}$ GeV$^4$). The ratio is the "hierarchy problem" of cosmology.

Renormalization in QFT is supposed to handle infinities by absorbing divergences into counterterms. But for vacuum energy, the situation is worse: even a finite but large cutoff-dependent result cannot be absorbed into a counterterm without fine-tuning. The bare cosmological constant must be adjusted order-by-order in perturbation theory to cancel loop contributions to machine precision.

### Running Vacuum Model (RVM)

Solà proposes a radical reinterpretation: **what if Lambda is not fundamental, but "runs" with the expansion of the universe?**

In QCD, the coupling $\alpha_s(Q^2)$ runs according to the beta function:

$$\frac{d \alpha_s}{d \ln Q^2} = \beta_0 \alpha_s^2 + \ldots$$

Solà proposes an analogous running for the cosmological term:

$$\Lambda(H) = \Lambda_0 + \nu H^2 + \ldots$$

where $H = \dot{a}/a$ is the Hubble parameter, and $\nu$ is a "running parameter" related to quantum corrections. Equivalently, the effective dark energy density evolves:

$$\rho_\Lambda(t) = \rho_{\Lambda,0} + \nu H^2(t)$$

where $\rho_{\Lambda,0}$ is the current value. This gives an **effective equation of state**:

$$w(a) = \frac{p_\Lambda}{\rho_\Lambda} = -1 + \frac{\nu H^2}{\rho_{\Lambda,0} + \nu H^2}$$

In the early universe (large H), w deviates from -1. As the universe expands (H decreases), w approaches -1 asymptotically. The model naturally explains:

1. Why today's Lambda is small: it is a residual of the running
2. Why the equation of state is approximately -1: in the late universe, H is small
3. Why there are anomalies (if any) in acceleration: the transition at intermediate redshifts

### Adiabatic Renormalization and RVM Derivation

Solà derives RVM from quantum field theory in curved spacetime using **adiabatic renormalization**. The renormalized energy-momentum tensor in FRW spacetime is:

$$\langle T_{\mu\nu} \rangle_{\text{ren}} = \langle T_{\mu\nu} \rangle_{\text{bare}} - \langle T_{\mu\nu} \rangle_{\text{counter}}$$

Using the adiabatic subtraction scheme (Birrell-Davies), the vacuum energy density of a scalar field of mass m in expanding FRW is:

$$\rho_{\text{vac}}(t) = \frac{1}{2\pi^2} \int_0^\infty dk k^2 \omega_k(k,t) + \text{renormalization}$$

where $\omega_k = \sqrt{k^2 + m^2 + \xi R(t)}$ (with $\xi$ the coupling to Ricci scalar R). The adiabatic order-by-order subtraction removes divergences, leaving:

$$\rho_{\text{vac}}^{(2)} = \frac{1}{2\pi^2} m^4 I_2(\beta) + \frac{m^2 R}{12\pi^2} + \ldots$$

where $I_2$ is an adiabatic integral. Importantly, the second term $\propto m^2 R$ **runs with the curvature**. Since $R \propto H^2$ in FRW:

$$\rho_{\text{vac}} \propto H^2$$

This is the origin of the running vacuum model. The coefficient $\nu$ is:

$$\nu = \frac{1}{12\pi^2} \sum_i N_i m_i^2 c_i$$

where the sum runs over all quantum fields (fermions, bosons, scalars) with multiplicities $N_i$ and running factors $c_i$.

### RVM and Cosmic History

With $\Lambda(H)$, the Friedmann equations become:

$$H^2 + \frac{k}{a^2} = \frac{8\pi G}{3} \rho_m + \frac{\Lambda(H) + \nu H^2}{8\pi G}$$

Rearranging:

$$H^2 \left(1 - \frac{8\pi G \nu}{3}\right) = \frac{8\pi G}{3} \rho_m - \frac{k}{a^2} + \frac{\Lambda_0}{3}$$

Define the effective dark energy density:

$$\rho_\Lambda^{\text{eff}} = \frac{\Lambda_0}{8\pi G} + \nu H^2$$

Then:

$$H^2 = \frac{8\pi G}{3} (\rho_m + \rho_\Lambda^{\text{eff}})$$

The scale factor evolves non-trivially. In the early universe (radiation/matter dominance), H >> 0, and RVM contributes extra vacuum energy density. In the late universe (vacuum dominance), H decreases, and RVM asymptotically approaches ΛCDM.

For inflation-scale universes, the RVM predicts **no need for an inflaton field**. The early universe is driven by the running vacuum itself:

$$\rho_\Lambda(H_{\text{inf}}) \sim M_{\text{Planck}}^4 / \text{poly}(\text{logs})$$

which is much larger than typical inflation scales (10^{-10} M_Planck^4), so standard inflation is a low-energy consequence of RVM.

---

## Key Results

1. **Running Cosmological Constant**: The cosmological "constant" is not constant but evolves as $\Lambda(H) = \Lambda_0 + \nu H^2$, where the running parameter $\nu$ is determined by quantum field loops (order 10^{-2} in natural units).

2. **Equation of State Evolution**: The effective dark energy equation of state is $w(z) = -1 + \delta w(z)$, where:

$$\delta w(z) \approx \frac{\nu H^2}{\rho_{\Lambda,0}} \sim 0.01-0.1 \text{ at } z \sim 1$$

This predicts observable deviations from ΛCDM at intermediate redshifts accessible to DESI and future surveys.

3. **Tension Resolution**: RVM reduces (though does not eliminate) the cosmological constant problem: the observed Lambda is small because we live in the late universe where H is small. The "true" vacuum scale (quantum corrections) is still large, but its contribution is suppressed by H^2 factors.

4. **Inflation as Low-Energy Limit**: Early-universe inflation emerges naturally from the running vacuum, without requiring separate inflaton physics. The primordial spectral index and tensor-to-scalar ratio are predictions of the running vacuum, not free parameters.

5. **Observational Signature**: Type Ia supernovae, BAO, and CMB data can distinguish RVM from ΛCDM via the redshift dependence of the equation of state. Current data (through 2024) show marginal preference for RVM over ΛCDM (Δχ² ~ 1-3 depending on dataset combinations). DESI DR2 will provide the first definitive test.

6. **Primordial Nucleosynthesis**: RVM predicts a slightly different expansion history at early times (BBN epoch), affecting the predicted He-4 abundance. Observations of primordial He/D are consistent with RVM predictions at ~1σ level.

---

## Impact and Legacy

Solà Peracaula's running vacuum model has become an influential alternative framework for dark energy. Its impact includes:

- **Paradigm Shift**: From treating Lambda as a fundamental constant to viewing it as an effective running parameter (analogous to QCD couplings)
- **Quantum Field Theory Foundation**: RVM is derived from first-principles QFT, providing a more rigorous alternative to phenomenological quintessence
- **Observational Tests**: RVM makes falsifiable predictions testable by DESI, CMB-S4, Vera Rubin Observatory, and future surveys
- **Resolution of Fine-Tuning**: Reduces the need for anthropic arguments by explaining smallness of Lambda through running, not luck

The 2025 review synthesizes two decades of RVM work and positions it as a serious contender for post-ΛCDM cosmology.

---

## Connection to Phonon-Exflation Framework

**DIRECT AND PROFOUND ANALOGY.**

The phonon-exflation framework predicts that the universe's expansion is driven by a **dynamical cosmological constant**:

$$\Lambda_{\text{eff}}(\tau) = \Lambda_0 f(\tau) + \text{higher order}$$

where $\tau$ is the deformation parameter of the SU(3) fiber, and $f(\tau)$ is a monotonically increasing function (from Session 24's spectral action studies).

This is structurally identical to Solà's RVM in one crucial aspect: **both frameworks propose that what appears to be a cosmological constant is actually a dynamical quantity**.

**Quantitative comparison**:

| Aspect | RVM (Solà) | Framework |
|--------|-----------|-----------|
| Running Parameter | $H^2$ (Hubble) | $\tau$ (moduli) |
| Origin | QFT loops in FRW | Spectral action on M4 x SU(3) |
| Effective EoS | $w(z) \approx -1 + \delta w(z)$, $\delta w \sim 0.01-0.1$ | $w \approx -1 + O(10^{-29})$ (predicted) |
| Observational Status | Marginal preference, DESI TBD | DESI DR2: 2.5-3.7σ tension |

**Critical Difference**: RVM predicts $w$ varies by ~ 0.1 (large enough for DESI to measure). The framework's spectral action predicts $w = -1$ to extraordinary precision, which is **inconsistent with DESI DR2 data** (which shows $w_0 \sim -0.75$).

**Possible Synthesis**: The framework's dark energy is NOT purely from the spectral action (which is monotonic and has no stasis point), but from the **time-dependent instanton gas** during the tau evolution (Session 37-38 mechanism). The instantons act like an effective "running" parameter, similar to how RVM's running vacuum changes with Hubble parameter.

In this reinterpretation:

$$\rho_\Lambda^{\text{eff}}(\tau, t) = \rho_{\text{spec}}(\tau) + \rho_{\text{inst}}(n_{\text{inst}}(t))$$

where $n_{\text{inst}}(t)$ is the time-dependent instanton density during the Kibble-Zurek transition. The dark energy equation of state becomes:

$$w(t) = \frac{\rho_{\text{spec}} + p_{\text{inst}}}{\rho_{\text{spec}} + \rho_{\text{inst}}}$$

This would allow the framework to predict $w \neq -1$ in agreement with DESI, while maintaining the underlying noncommutative geometry structure.

**Key Open Question for the Framework**: Is the instanton density evolving during the cosmological transit? If yes, the framework converges with RVM in spirit, and Session 39+ should focus on computing $\rho_{\text{inst}}(t)$ as a function of cosmic time, not just at the tau-fold point.

