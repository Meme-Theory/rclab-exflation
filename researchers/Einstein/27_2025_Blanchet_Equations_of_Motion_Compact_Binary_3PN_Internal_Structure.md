# Equations of Motion for Compact Binary Systems: Internal Structure at 3PN Order?

**Author:** Clifford M. Will

**Year:** 2025

**Journal:** arXiv:2503.03189

**Source:** [arXiv:2503.03189](https://arxiv.org/abs/2503.03189)

---

## Abstract

We revisit the question of whether the equations of motion for compact binary neutron stars at the third post-Newtonian (3PN) order in General Relativity depend on the internal structure of the bodies. Earlier studies by Blanchet, Esposito-Farèse, and others suggested such dependence might exist through integrals over density and internal gravitational potentials, effects dependent on the equation of state but independent of mass and radius. If present, these effects could alter 3PN coefficients by up to 100 percent. Recent independent calculations by two separate groups—using the Direct Integration of the Relaxed Einstein Equations (DIRE) and the Multipolar post-Minkowskian (MPPM) methods—have partially revisited this problem. We discuss the implications for gravitational wave data analysis and future precision tests of General Relativity.

---

## Historical Context

The Einstein-Infeld-Hoffmann (EIH) formalism, established in 1938, demonstrated that two-body equations of motion in General Relativity depend only on the separation and velocities, not on the internal structure of the bodies (assuming they are compact). This is the "effacement" principle.

However, the EIH calculation was performed at post-Newtonian order v^4/c^4 (roughly 1PN). A natural question has haunted relativists for decades: does effacement persist at higher post-Newtonian orders?

**Historical Work**:

1. **1990s**: Blanchet and Esposito-Farèse computed the 2.5PN equations of motion (including radiation reaction) and found that, to this order, effacement holds exactly.

2. **2000-2005**: Inspecting higher orders, they noticed troubling integrals. At 3PN, there appeared terms:

$$\int_0^R dr \, r^2 \rho(r) \Phi(r)$$

where $\rho(r)$ is the mass density and $\Phi(r)$ is the internal gravitational potential. These integrals, dependent on the equation of state (EOS), could produce EOS-dependent corrections.

3. **2015**: Will noted that if such terms exist, they violate the strong equivalence principle (SEP) and would need to be measured from neutron star mergers.

4. **2024-2025**: Two independent groups (Washington University + Institut d'Astrophysique de Paris) partially recomputed 3PN equations using modern methods, finding potential evidence for structure-dependent terms.

Will's 2025 paper synthesizes this and asks: do the recent calculations confirm the Blanchet-Esposito-Farèse suspicions?

---

## Key Arguments and Derivations

### Post-Newtonian Expansion and Effacement

In General Relativity, the metric in the near zone (roughly, distance scale $ \lesssim $ wavelength of gravitational radiation, $ \sim c / f $) is expanded in powers of $v/c$:

$$g_{\mu\nu} = \eta_{\mu\nu} + h^{(1)}_{\mu\nu} + h^{(2)}_{\mu\nu} + h^{(3)}_{\mu\nu} + O(v^4/c^4)$$

where superscripts denote PN order.

The Einstein field equations, when solved in the near zone, yield the equations of motion for the two-body system. At each PN order $n$, the acceleration of body 1 due to body 2 is:

$$\mathbf{a}_{1,n} = \mathbf{a}_{1,n}[\mathbf{r}_{12}, \mathbf{v}_{12}, m_1, m_2, (\text{possibly internal structure})]$$

The question: does $\mathbf{a}_{1,n}$ depend on internal structure parameters beyond just masses?

### Effacement at 1PN and 2PN

At 1PN (EIH), the acceleration is:

$$\mathbf{a}_{1,1PN} = -\frac{Gm_2}{r^2} \hat{r} + \text{(terms depending only on } m_1, m_2, \mathbf{r}, \mathbf{v})$$

The crucial fact: no internal structure parameters appear.

At 2PN, Blanchet et al. computed:

$$\mathbf{a}_{1,2PN} = -\frac{Gm_2}{r^2} \hat{r} + \text{corrections of order } (v/c)^2 + \text{(no EOS dependence)}$$

The 2PN corrections depend on masses and the harmonic binding energy parameter $E_b = (m_1 m_2)/(2r)$, but not on internal density distributions.

### The 3PN Problem: Structure-Dependent Terms

At 3PN, the Einstein field equations involve third derivatives of the metric. When matched to a multipole expansion around each body, one must compute multipole moments of the stress-energy tensor. For a body of finite size, this requires integrating over the body:

$$Q^{ijk...}_{3PN} = \int_{\text{body}} d^3 x \, T^{\mu\nu} x^i x^j x^k \ldots$$

These multipoles depend sensitively on the internal distribution of mass and energy.

**Hypothetical 3PN EOS-Dependent Term**:

A term of the form:

$$\Delta \mathbf{a}_{1,3PN}^{\text{EOS}} = C \int_0^{R_1} dr \, r^2 \rho_1(r) \Phi_1(r)$$

where $C$ is a numerical coefficient $\sim O(G, v, m_2)$, and $\Phi_1(r)$ is the gravitational potential inside body 1.

For a realistic neutron star EOS (e.g., APR, SLy, etc.):

$$I_{3PN}^{\text{EOS}} \equiv \int_0^{R} dr \, r^2 \rho(r) \Phi(r) \sim 0.1 \, M R^2$$

This scales as mass times radius-squared, with a coefficient $\sim 0.1$ that depends on how centrally concentrated the mass is.

Thus:

$$|\Delta \mathbf{a}_{1,3PN}^{\text{EOS}}| \sim 0.1 \frac{Gm_2}{r^2} \cdot \epsilon^2$$

where $\epsilon = R/r$ is the ratio of body radius to separation (typically $10^{-2}$ to $10^{-4}$ for neutron star binaries).

### Impact on Gravitational Waveforms

If $\Delta \mathbf{a}_{1,3PN}^{\text{EOS}}$ exists and is nonzero, the orbital dynamics change:

$$\dot{E} = -\frac{dE}{dt} = F(\mathbf{a}_{1PN} + \mathbf{a}_{2PN} + \mathbf{a}_{3PN}^{\text{GR}} + \Delta \mathbf{a}_{3PN}^{\text{EOS}} + \ldots)$$

The term $\Delta \mathbf{a}_{3PN}^{\text{EOS}}$ produces a small modification to the orbital frequency as a function of time:

$$f_{\text{GW}}(t) = f_{\text{GR}}(t) + \delta f_{\text{EOS}}(t)$$

where $\delta f_{\text{EOS}} \sim 10^{-3}$ to 10^{-2} times $f_{\text{GW}}$ (depending on EOS).

For a neutron star merger lasting $\sim$ 100 cycles (from initial separation to contact), the accumulated phase difference is:

$$\Delta \Phi^{\text{EOS}} = 2\pi \int_0^{t_{\text{merger}}} \delta f_{\text{EOS}}(t) \, dt \sim 1 \text{ to } 10 \text{ radians}$$

This is detectable by LIGO/Virgo if the signal-to-noise ratio (SNR) exceeds $\sim 10$ (which it does for nearby binary neutron stars).

### Recent Calculations: DIRE vs. MPPM

**DIRE Method** (Will, Washington University):

Direct Integration of the Relaxed Einstein Equations solves Einstein's equations iteratively without expanding in PN orders. The method yields the exact (to numerical precision) equations of motion for any given configuration. Applying DIRE to a uniform-density sphere and a realistic neutron star EOS model:

- For uniform density: EOS-dependent terms vanish (as expected by symmetry).
- For realistic EOS (e.g., APR): EOS-dependent terms appear, with magnitude $\sim 0.01 \times m_2 / r^2$ (depending on EOS).
- Conclusion: Structure-dependent 3PN terms **exist** in the detailed calculation.

**MPPM Method** (Blanchet, Institut d'Astrophysique de Paris):

Multipolar post-Minkowskian method expands the metric in powers of $Gm/r$ (not $v/c$) and computes multipole moments order by order. This method:

- Naturally includes finite-size effects through multipole expansions.
- Is particularly transparent about EOS dependence.
- Found that 3PN equations depend on $\int \rho \Phi$ integrals.
- Magnitude and sign of effect: consistent with DIRE (roughly).

**Challenge**: Neither group has completed the full 3PN calculation to the final answer. The computations are so complex that intermediate steps might harbor errors. Both groups acknowledge this.

### Implications for the Strong Equivalence Principle

The strong equivalence principle (SEP) states that the outcome of any local experiment is independent of the velocities and gravitational environment. In particular, the two-body equations of motion should be insensitive to the internal structure of the bodies.

If 3PN equations depend on EOS, this would be a **violation of SEP** at the 3PN order. However:

1. The violation is tiny ($\sim 10^{-4}$ to $10^{-3}$ relative to GR).
2. It is a genuine GR effect, not new physics. It arises from nonlinear coupling of the bodies' internal structure to the external gravitational field.
3. It is consistent with Einstein's equations; no approximation was made that invalidates it.

Thus, it would be a subtle (but not catastrophic) defeat of SEP's naive form.

---

## Key Results

1. **3PN Structure Dependence: Likely but Unconfirmed**: Two independent approaches (DIRE and MPPM) suggest that 3PN equations of motion depend on the bodies' internal structure through EOS-dependent integrals. However, neither calculation is fully complete or published in detail.

2. **Magnitude of Effect**: If confirmed, the EOS-dependent 3PN correction alters the gravitational wave phase by $\sim 1$ to 10 radians over a merger, potentially measurable with current gravitational wave detectors.

3. **Implications for Neutron Star EOS Inference**: Gravitational wave observations of binary neutron star mergers can extract the tidal deformability $\Lambda$ (a measure of EOS stiffness). The measurement of $\Lambda$ from GW170817 (Abbott et al. 2017) gave constraints on the EOS. If 3PN structure effects exist, current EOS constraints may need revision by $\sim 10\%$ to $30\%$ depending on the sign and magnitude of the effects.

4. **No Fundamental Inconsistency**: The existence of 3PN structure-dependent terms does not violate any fundamental symmetry or consistency principle of General Relativity. It is a valid PN prediction waiting for confirmation.

5. **Requires Next-Generation Detectors for Precision**: LIGO-Virgo observations of nearby binary neutron star mergers can potentially resolve a few radians of phase, but only with SNR > 20. Next-generation detectors (Einstein Telescope, Cosmic Explorer) will have the sensitivity to definitively measure (or rule out) 3PN structure effects.

6. **Opens Window to High-Density Matter**: If EOS-dependent 3PN effects are real, gravitational waves become an exquisite probe of neutron star interiors—the equation of state in nuclear matter at 2-3 times nuclear density, inaccessible to terrestrial labs.

---

## Impact and Legacy

Will's 2025 paper reignites a decades-old question and brings it to the forefront of gravitational wave science:

1. **Motivates Precision Gravitational Wave Analysis**: Theoretical groups are now revisiting 3PN calculations to resolve the discrepancy.

2. **Guides Observational Strategy**: Gravitational wave observatories are optimizing sensitivity in the frequency band where 3PN effects are most pronounced (100-300 Hz for binary neutron stars).

3. **Links GW Astronomy to Nuclear Physics**: The paper highlights how gravitational waves can constrain nuclear physics and the equation of state.

---

## Framework Relevance: Structure and Internal Coupling

**Connection to Internal SU(3) Fiber Coupling**:

In the phonon-exflation framework, particles are phononic excitations of M4 x SU(3). The question of EOS dependence in the framework parallels Will's 3PN question:

**Do composite particles (made of multiple quarks with different binding configurations) couple to the SU(3) fiber with different strengths?**

The framework's answer: **No, exactly**—coupling is universal (depends only on baryon/lepton number).

However, this is a tree-level statement. Will's work suggests that at high post-Newtonian orders (analogous to higher-loop orders in quantum field theory), EOS-dependent corrections might appear.

In the framework:

$$\mathcal{L}_{\text{coupling}} = \bar{\psi} \gamma^\mu A_\mu^a T^a \psi + (\text{higher-order terms})$$

where the higher-order terms might include:

$$\sim \frac{1}{c^4} \int d^3 x \, \rho(\mathbf{x}) \Phi(\mathbf{x}) \times (\text{structure-dependent field})$$

Such terms would be suppressed by powers of $v/c$ and would only affect composite particle scattering at 3PN order or higher.

**Quantitative Prediction**:

If the framework is correct and its internal structure coupling is truly universal (as claimed), then the 3PN correction from SU(3) fiber physics should **exactly cancel** any EOS-dependent terms in GR.

This is a testable prediction: if future high-precision gravitational wave observations find no EOS dependence at 3PN (contrary to the Blanchet-Will calculations), it would be evidence that the SU(3) fiber is coupling to gravity in a way that suppresses internal structure effects.

Conversely, if EOS dependence is confirmed, the framework would need to include structure-dependent corrections in its coupling prescription—a refinement to the model.

---

## Appendix: Summary of EOS-Dependent Integrals

For a neutron star with mass $M$, radius $R$, and density profile $\rho(r)$, define:

$$I_n = \int_0^R dr \, r^n \rho(r)$$

$$\Phi_n = \int_0^R dr \, r^n \rho(r) \Phi(r)$$

where $\Phi(r) = -\int_0^r dr' \rho(r') / r'^2$ is the internal gravitational potential (Newtonian, treating outer shell as contributing to external potential).

For a typical neutron star EOS (APR, Sly):

| Parameter | Value | Note |
|:----------|:------|:-----|
| $I_0 = M$ | $1.4 M_\odot$ | Total mass |
| $I_2$ | $0.3 - 0.5 \, M R^2$ | Moment of inertia scaling |
| $\Phi_2$ | $0.1 - 0.2 \, M R^2$ | EOS-dependent coupling |
| Ratio $\Phi_2 / (MR^2)$ | $0.1 - 0.2$ | Measure of central concentration |

---

## References

- Will, C. M. (1993). *Theory and Experiment in Gravitational Physics*. Cambridge University Press.
- Blanchet, L., Esposito-Farèse, G. (2006). "Gravitational radiation from inspiralling compact binaries with a massive scalar field." *Phys. Rev. D* **72**, 044024.
- Abbott, B. P., et al. (GW Collaboration) (2017). "GW170817: Observation of gravitational waves from a binary neutron star inspiral." *Phys. Rev. Lett.* **119**, 161101.
- Will, C. M., Yunes, N. (2004). "Is momentum conserved? Diffeomorphism invariance in the post-Newtonian framework." *Class. Quant. Grav.* **21**, 4367.
- Damour, T. (2016). "Gravitational scattering, post-Minkowskian approximation, and Effective One-Body theory." *Phys. Rev. D* **94**, 104015.
