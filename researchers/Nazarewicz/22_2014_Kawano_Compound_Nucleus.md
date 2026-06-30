# Theoretical Descriptions of Compound-Nuclear Reactions: Open Problems & Challenges

**Author(s):** Brett V. Carlson, Jutta E. Escher, Mahir S. Hussein
**Year:** 2014
**Journal:** Journal of Physics G: Nuclear and Particle Physics (proceedings)
**arXiv:** 1403.0923
**Relevance:** HIGH

---

## Abstract

Compound-nuclear processes play an important role for nuclear physics applications and are crucial for our understanding of the nuclear many-body problem. Despite intensive interest in this area, some of the available theoretical developments have not yet been fully tested and implemented. We revisit the general theory of compound-nuclear reactions, discuss descriptions of pre-equilibrium reactions, and consider extensions that are needed in order to get cross section information from indirect measurements.

---

## Key Arguments and Derivations

### Section 2.1: Bohr's Hypothesis and Hauser-Feshbach Cross Section

The Bohr independence hypothesis states that formation and decay of the compound nucleus are independent. This leads to the product form $\sigma_{cc'} = \xi_c \cdot \xi_{c'}$. Unitarity plus the Bohr hypothesis yield the Hauser-Feshbach (HF) cross section $\sigma_{cc'} = T_c T_{c'} / \sum_{c''} T_{c''}$, where $T_c$ are transmission coefficients. Width fluctuation corrections $W_{cc'}$ account for channel correlations, producing an elastic enhancement factor between 2 (strong absorption) and 3 (weak absorption).

### Section 2.2: Feshbach's Projection-Operator Theory

Feshbach introduces projection operators $P$ (open channels) and $Q$ (closed/compound channels). The effective equation for $P|\Psi\rangle$ contains the strongly energy-dependent term $PHQ G_Q QHP$ where $G_Q = 1/(E - QHQ)$. Energy-averaging with a Lorentzian of width $I \gg \Gamma$ yields the optical model with its intrinsically complex potential. The S-matrix separates into a unitary background term and a sum over compound nucleus resonances.

### Section 2.3: Kawai-Kerman-McVoy (KKM) Theory

KKM eliminates the compound-direct interference term by introducing the optical potential at the outset. The energy-averaged cross section becomes an incoherent sum: $\sigma_{cc'} = \sigma^{\mathrm{opt}}_{cc'} + \hat{\sigma}^{\mathrm{fl}}_{cc'}$. The fluctuation cross section involves $X$ and $Y$ matrices built from resonance amplitudes. In overlapping resonances, $Y$ is negligible and the HF result with direct reactions is $\sigma^{\mathrm{fl}}_{cc'} = (P_{cc}P_{c'c'} + P_{cc'}P_{c'c}) / \mathrm{Tr}(P)$, giving the elastic enhancement factor of 2. In isolated resonances (weak absorption), the enhancement is 3.

### Section 2.4: Intermediate Structure and Doorway Resonances

A third projection operator $D$ is introduced for doorway states (simpler than CN resonances). In the extreme doorway model ($PHQ = QHP = 0$), the S-matrix becomes $S_{00} = S^{(0)}_{00} [1 - i\Gamma^{\uparrow}_D / (E - E_D + i(\Gamma^{\uparrow}_D + \Gamma^{\downarrow}_D)/2)]$, where $\Gamma^{\uparrow}_D$ is the escape width and $\Gamma^{\downarrow}_D$ the spreading width. The transmission coefficient has a Breit-Wigner form $P_{00} = \Gamma^{\uparrow}_D \Gamma^{\downarrow}_D / [(E - E_D)^2 + (\Gamma_D/2)^2]$. Doorway states can be as simple as 2p-1h or as complex as giant resonances.

### Section 2.5: Ericson Fluctuations

In overlapping resonances, the cross-section correlation function $C_{cc'}(\varepsilon) = \langle \sigma_{cc'}(E) \sigma_{cc'}(E+\varepsilon) \rangle$ takes a Lorentzian form with correlation width $\Gamma_{\mathrm{corr}}$ related to $\sum_c P_{cc}$ via $2\pi \Gamma_{\mathrm{corr}}/D = \sum_c P_{cc}$. This provides a direct experimental probe of compound-nucleus lifetimes and densities of states.

### Section 3: Pre-equilibrium Reactions

The exciton model classifies states by exciton number $n = p + h$. The master equation governs transitions between exciton configurations with rates $\lambda_{\pm}(n)$ and emission rate $\lambda_e(n)$. For small $n$: $\lambda_+(n) > \lambda_0(n) > \lambda_-(n)$, meaning the equal-occupation assumption is generally violated. The equilibrium exciton number satisfies $\lambda_+(n_{\mathrm{eq}}) = \lambda_-(n_{\mathrm{eq}})$ and scales as $n_{\mathrm{eq}} \approx \sqrt{gE}$. Quantum multistep direct and multistep compound models refine the semiclassical picture but share the equilibration difficulty.

### Section 4: Surrogate (Hybrid) Reactions

The surrogate method uses a transfer reaction $d + D \to b + B^*$ to produce the compound nucleus $B^*$ indirectly, measuring $P_{\delta\chi}(E) = \sum_{J,\pi} F^{\mathrm{CN}}_\delta(E,J,\pi) G^{\mathrm{CN}}_\chi(E,J,\pi)$. The spin-parity distribution $F^{\mathrm{CN}}_\delta$ must be calculated theoretically. Non-equilibrium decay (5-20% above 15 MeV) contaminates the measurement and must be modeled.

## Key Results

1. Hauser-Feshbach theory with width fluctuation corrections remains the standard framework for compound nuclear reactions
2. KKM theory eliminates compound-direct interference, yielding incoherent sum of optical and fluctuation cross sections
3. Elastic enhancement factor: 2 (overlapping resonances) to 3 (isolated resonances)
4. Doorway states provide intermediate structure with escape and spreading widths
5. Ericson correlation function gives experimental access to compound nucleus lifetime via $\Gamma_{\mathrm{corr}}$
6. Equal-occupation assumption in exciton model is generally violated for low exciton numbers
7. Surrogate reactions require careful treatment of spin-parity distributions and non-equilibrium decay
8. At energies >30 MeV, leading-particle approximation in multistep direct model breaks down
9. Pre-equilibrium reactions are at least partially coherent over a wide range of exciton numbers

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hauser-Feshbach cross section | $\sigma_{cc'} = T_c T_{c'} / \sum_{c''} T_{c''}$ | Eq. (3) |
| Width fluctuation correction | $\sigma_{cc'} = W_{cc'} T_c T_{c'} / \sum_{c''} T_{c''}$ | Eq. (4) |
| Feshbach Q-space Green's function | $G_Q = 1/(E - QHQ)$ | Eq. (9) |
| Optical model Green's function | $\langle G_Q \rangle = 1/(E - QHQ + iI/2)$ | Eq. (10) |
| KKM S-matrix decomposition | $S_{cc'} = S^{\mathrm{opt}}_{cc'} - i \sum_q g_{qc} g_{qc'} / (E - \varepsilon_q)$ | Eq. (14) |
| Fluctuation cross section (KKM) | $\sigma^{\mathrm{fl}}_{cc'} = (P_{cc}P_{c'c'} + P_{cc'}P_{c'c}) / \mathrm{Tr}(P)$ | Eq. (26) |
| Doorway S-matrix | $S_{00} = S^{(0)}_{00} \left[\frac{E - E_D - i(\Gamma^{\uparrow}_D - \Gamma^{\downarrow}_D)/2}{E - E_D + i(\Gamma^{\uparrow}_D + \Gamma^{\downarrow}_D)/2}\right]$ | Eq. (34) |
| Doorway transmission | $P_{00} = \Gamma^{\uparrow}_D \Gamma^{\downarrow}_D / [(E - E_D)^2 + (\Gamma_D/2)^2]$ | Eq. (35) |
| Ericson correlation function | $C_{cc'}(\varepsilon) = (\langle\sigma_{cc'}\rangle)^2 / [1 + (\varepsilon/\Gamma_{\mathrm{corr}})^2]$ | Eq. (41) |
| Exciton master equation | $\frac{dP(n)}{dt} = \lambda_-(n+2)P(n+2) + \lambda_0(n)P(n) + \lambda_+(n-2)P(n-2) - \lambda(n)P(n)$ | Eq. (42) |
| Surrogate probability | $P_{\delta\chi}(E) = \sum_{J,\pi} F^{\mathrm{CN}}_\delta(E,J,\pi) G^{\mathrm{CN}}_\chi(E,J,\pi)$ | Eq. (56) |
| Desired cross section | $\sigma_{\alpha\chi}(E_a) = \sum_{J,\pi} \sigma^{\mathrm{CN}}_\alpha(E,J,\pi) G^{\mathrm{CN}}_\chi(E,J,\pi)$ | Eq. (55) |

## Relevance to Phonon-Exflation

This paper is directly relevant to the S42 Hauser-Feshbach analysis of KK branching ratios. The HF formula $\sigma_{cc'} = T_c T_{c'} / \sum T_{c''}$ provides the statistical framework for computing decay branching of excited KK states into visible vs. hidden channels. The doorway-state formalism (Section 2.4) maps onto the Feshbach doorway identified in S38 for the pair-removal/B3-B2 near-resonance (2.9% detuning). The escape width $\Gamma^{\uparrow}_D$ and spreading width $\Gamma^{\downarrow}_D$ directly parallel the competing decay channels of the KK doorway state. Ericson fluctuation analysis could diagnose whether the KK spectrum is in the overlapping or isolated regime, determining the appropriate enhancement factor for elastic back-scattering.
