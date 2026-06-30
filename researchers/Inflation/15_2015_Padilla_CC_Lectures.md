# Lectures on the Cosmological Constant Problem

**Author(s):** Antonio Padilla
**Year:** 2015
**Journal:** Lectures at X Mexican School on Gravitation and Mathematical Physics
**arXiv:** 1502.05296
**Relevance:** CRITICAL — for a project studying phonon-exflation cosmology where the CC overshoot is the key open problem

---

## Abstract

These lectures on the cosmological constant problem were prepared for the X Mexican School on Gravitation and Mathematical Physics. The problem itself is explained in detail, emphasising the importance of radiative instability and the need to repeatedly fine tune as we change our effective description. Weinberg's no go theorem is worked through in detail. I review a number of proposals including Linde's universe multiplication, Coleman's wormholes, the fat graviton, and SLED, to name a few. Large distance modifications of gravity are also discussed, with causality considerations pointing towards a global modification as being the most sensible option. The global nature of the cosmological constant problem is also emphasized, and as a result, the sequestering scenario is reviewed in some detail, demonstrating the cancellation of the Standard Model vacuum energy through a global modification of General Relativity.

---

## Key Arguments and Derivations

### Section 2: What is the Problem?

Padilla emphasizes that the CC problem is commonly misstated. The real problem is not fine-tuning per se, but **radiative instability** -- the need to repeatedly fine-tune at each successive order in perturbation theory.

**Vacuum energy from QFT**: The one-loop vacuum diagram for a scalar of mass $m$ using dimensional regularization yields:
$$V_{\text{vac}} \sim \sum_{\text{particles}} \mathcal{O}(1)\, m_{\text{particle}}^4$$
Given the Standard Model includes particles up to the TeV scale, $V_{\text{vac}} \gtrsim (\text{TeV})^4$. The electron contribution alone gives a cosmological horizon at $r_H \lesssim 10^6$ km (Earth-Moon distance), far smaller than the observed $r_H \sim 10^{26}$ m.

**Renormalization and the real problem**: The action $S = \int d^4x\sqrt{-g}\left[\frac{M_{\text{pl}}^2}{2}R - \mathcal{L}_m - \Lambda\right]$ contains a counterterm $\Lambda$ that absorbs divergences, leaving $\Lambda_{\text{ren}} = \Lambda + V_{\text{vac}}$. Observations require $\Lambda_{\text{ren}} \lesssim (\text{meV})^4$, representing a fine-tuning of $\lesssim 10^{-60}$ between $\Lambda$ and $V_{\text{vac}}^{\text{finite}} \gtrsim (\text{TeV})^4 \sim 10^{60}(\text{meV})^4$.

This is NOT the real CC problem. The real problem: at two loops, corrections scale as $\lambda m^4$ (not significantly suppressed for perturbative couplings like the Higgs $\lambda \sim 0.1$), completely spoiling the one-loop cancellation. At three loops, four loops, etc., retuning is required each time. The vacuum energy is "uber-sensitive" to unknown UV physics.

**Wilson action perspective**: Equivalently, the vacuum energy is unstable against changing the Wilsonian cutoff $\mu$. Moving from $\mu$ to $\hat{\mu} < \mu$ requires retuning the counterterm -- unlike how effective field theory is supposed to work.

**Phase transitions**: The electroweak phase transition shifts vacuum energy by $\Delta V_{\text{EW}} \sim (200\,\text{GeV})^4$, the QCD transition by $\Delta V_{\text{QCD}} \sim (0.3\,\text{GeV})^4$, spoiling any pre-transition cancellation.

### Section 3: Some Things NOT to Do

**3.1 Unimodular gravity does NOT help**: Restricted variation with $|\det g| = 1$ gives the traceless Einstein equation $M_{\text{pl}}^2(R_{\mu\nu} - \frac{1}{4}Rg_{\mu\nu}) = T_{\mu\nu} - \frac{1}{4}Tg_{\mu\nu}$. Although vacuum energy is pure trace and drops out, the Bianchi identity and energy conservation force $T + M_{\text{pl}}^2 R = 4\Lambda$ where $\Lambda$ is an integration constant playing exactly the same role as the GR counterterm. It must be retuned order by order, gaining nothing.

**3.2 Weinberg's no-go theorem**: Assuming (i) field content $g_{\mu\nu}$ plus self-adjusting fields $\varphi_i$, (ii) a translationally invariant vacuum ($g_{\mu\nu}, \varphi_i = \text{const}$), and (iii) a general Lagrangian $\mathcal{L}[g, \varphi_i]$, Weinberg shows that any self-adjustment mechanism either requires fine-tuning ($V(\varphi_i) = 0$) or the field equations are not independent (related by $2g_{\mu\nu}\frac{\partial\mathcal{L}}{\partial g_{\mu\nu}} = \sum_i f_i(\varphi)\frac{\partial\mathcal{L}}{\partial\varphi_i}$), which after substitution into the vacuum equations yields flat spacetime only if $f_i$ satisfies restrictive conditions equivalent to fine-tuning. Key assumption to evade: translational invariance of the vacuum.

### Section 4: Symmetry Approaches

**'t Hooft naturalness**: A parameter is natural if setting it to zero enhances the symmetry of the theory. For the CC, setting $\Lambda = 0$ does not obviously enhance any symmetry of the Standard Model coupled to GR.

**Supersymmetry**: Cancels boson/fermion vacuum contributions but is badly broken ($E_{\text{SS}} > 100$ GeV), leaving $V_{\text{vac}} \sim E_{\text{SS}}^4$ -- still too large.

**Scale invariance** and **energy parity** (Linde's universe multiplication): Various symmetry proposals are reviewed; none fully solve the problem in our universe.

### Section 5: Coleman's Wormholes

Coleman's proposal that wormhole corrections to the Euclidean path integral peak the probability at $\Lambda = 0$ is reviewed. Relies on Euclidean quantum gravity assumptions of dubious validity.

### Section 6: Short Distance Modifications

**SLED** (Supersymmetric Large Extra Dimensions): Two large extra dimensions with bulk supersymmetry can absorb vacuum energy into the compact space curvature. Challenges remain with moduli stabilization.

**Fat graviton**: Sundrum's proposal that the graviton has a finite size $\ell_{\text{fat}} \sim 1/\text{meV}$ so it cannot resolve vacuum fluctuations at shorter distances. Requires a UV completion.

### Section 7: Long Distance Modifications and the Sequester

**7.1 Fab Four**: A subtheory of Horndeski's general scalar-tensor theory that admits Minkowski solutions for any vacuum energy value, evading Weinberg's theorem by allowing the scalar to vary in time.

**7.2 Causality argument**: A local causal theory that modifies gravity at $L \gtrsim 1/H_0$ cannot decide which sources to degravitate early on. Three options: (1) large CC not cancelled until late (ruled out by nucleosynthesis), (2) short-wavelength sources also cancelled (dangerous phenomenology), (3) only global causality violation. This points to a **global** modification of gravity.

**7.3 The Sequester** (Kaloper-Padilla): Promotes the cosmological counterterm $\Lambda$ to a global dynamical variable (spacetime constant, not a field) and introduces a second global variable $\lambda$ coupling to the matter sector via the action:
$$S = \int d^4x\sqrt{-g}\left[\frac{M_{\text{pl}}^2}{2}R - \lambda^4\mathcal{L}_m(\lambda^{-2}g^{\mu\nu}, \Psi) - \Lambda\right] + \sigma\left(\frac{\Lambda}{\lambda^4\mu^4}\right)$$
where $\sigma$ is an odd, differentiable function (not integrated over spacetime). The global equations of motion yield $\Lambda = \frac{1}{4}\langle T^\alpha_\alpha\rangle$ (spacetime average), so $M_{\text{pl}}^2 G^\mu_\nu = \tau^\mu_\nu - \frac{1}{4}\delta^\mu_\nu\langle\tau^\alpha_\alpha\rangle$ where $\tau^\mu_\nu$ are local excitations. **The Standard Model vacuum energy drops out completely** at every loop order, thanks to diffeomorphism invariance and universal coupling via $\tilde{g}_{\mu\nu} = \lambda^2 g_{\mu\nu}$. The residual CC $\Lambda_{\text{eff}} = \frac{1}{4}\langle\tau^\alpha_\alpha\rangle$ is radiatively stable and depends only on the historic average of locally excited matter. Phase transition effects are suppressed by $\epsilon_{\text{PT}} \sim (a_{\text{PT}}/a_{\max})^3(H_{\text{turn}}/H_{\text{PT}}) \ll 1$. The universe must be spatially closed and dark energy must be transient ($w \neq -1$ exactly).

### Section 8: Final Thoughts

The CC problem is compared to the QED divergence crisis of the 1930s. The sequester represents "radical conservatism" -- locally indistinguishable from GR, with deviation only at the global level. The CC should be viewed as a radiatively stable "yardstick for cosmology" -- measured, not predicted.

## Key Results

1. The CC problem is fundamentally about **radiative instability**, not one-time fine-tuning. Each loop order requires retuning to $\sim 10^{-60}$ accuracy.
2. Unimodular gravity does NOT solve the CC problem -- the integration constant $\Lambda$ must be retuned order by order, identical to the GR counterterm.
3. Weinberg's no-go theorem forbids self-adjustment mechanisms under assumptions of (a) general local Lagrangian, (b) translationally invariant vacuum, (c) Poincare-invariant solutions.
4. The sequestering mechanism cancels SM vacuum energy at every loop order through global dynamical variables $\Lambda$ and $\lambda$, leaving a radiatively stable residual $\Lambda_{\text{eff}} = \frac{1}{4}\langle\tau^\alpha_\alpha\rangle$.
5. Phase transition contributions to the residual CC are suppressed as $(a_{\text{PT}}/a_{\max})^3 \ll 1$.
6. Sequestering requires: (a) spatially closed universe ($k > 0$), (b) finite spacetime volume, (c) transient dark energy ($w \approx -1$ but $w \neq -1$ exactly).
7. Causality arguments point to a **global** rather than local modification of gravity as the most viable approach to the CC problem.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Vacuum energy estimate | $V_{\text{vac}} \sim \sum_{\text{particles}} \mathcal{O}(1)\,m_{\text{particle}}^4$ | Eq. (2.2) |
| Vacuum energy-momentum tensor | $T^{\text{vac}}_{\mu\nu} = -V_{\text{vac}}\,g_{\mu\nu}$ | Eq. (2.7) |
| Action with counterterm | $S = \int d^4x\sqrt{-g}\left[\frac{M_{\text{pl}}^2}{2}R - \mathcal{L}_m(g^{\mu\nu}, \Psi) - \Lambda\right]$ | Eq. (2.9) |
| Renormalized CC | $\Lambda_{\text{ren}} = \Lambda + V_{\text{vac}}$ | Eq. (2.10) |
| Renormalized 1-loop CC | $\Lambda_{\text{ren}}^{1\text{loop}} \sim \frac{m^4}{(8\pi)^2}\left[\log\left(\frac{m^2}{M^2}\right) - \text{finite}\right]$ | Eq. (2.14) |
| Traceless Einstein eq. (unimodular) | $M_{\text{pl}}^2\left[R_{\mu\nu} - \frac{1}{4}Rg_{\mu\nu}\right] = T_{\mu\nu} - \frac{1}{4}Tg_{\mu\nu}$ | Eq. (3.1) |
| Integration constant recovery | $T + M_{\text{pl}}^2 R = 4\Lambda$ | Eq. (3.2) |
| Weinberg's no-go: Lagrangian form | $\mathcal{L} = \sqrt{-g}\,V(\varphi_i) \implies V(\varphi_i) = 0$ (fine-tuning) | Eq. (3.11) |
| Weinberg's no-go: dependent eqs. | $2g_{\mu\nu}\frac{\partial\mathcal{L}}{\partial g_{\mu\nu}} = \sum_i f_i(\varphi)\frac{\partial\mathcal{L}}{\partial\varphi_i}$ | Eq. (3.12) |
| Sequestering action | $S = \int d^4x\sqrt{-g}\left[\frac{M_{\text{pl}}^2}{2}R - \lambda^4\mathcal{L}_m(\lambda^{-2}g^{\mu\nu}, \Psi) - \Lambda\right] + \sigma\left(\frac{\Lambda}{\lambda^4\mu^4}\right)$ | Eq. (7.3) |
| Global $\Lambda$ equation | $\frac{1}{\lambda^4\mu^4}\sigma'\left(\frac{\Lambda}{\lambda^4\mu^4}\right) = \int d^4x\sqrt{-g}$ | Eq. (7.5) |
| Counterterm from global eqs. | $\Lambda = \frac{1}{4}\langle T^\alpha_\alpha\rangle$ | Eq. (7.8) |
| Sequestered Einstein equation | $M_{\text{pl}}^2 G^\mu_\nu = \tau^\mu_\nu - \frac{1}{4}\delta^\mu_\nu\langle\tau^\alpha_\alpha\rangle$ | Eq. (7.10) |
| Residual CC | $\Lambda_{\text{eff}} = \frac{1}{4}\langle\tau^\alpha_\alpha\rangle$ | Eq. (7.11) |

## Relevance to Phonon-Exflation

Padilla's lectures are directly relevant to the CC overshoot in the exflation framework on three levels. First, the emphasis on radiative instability -- not just one-time fine-tuning -- sharpens the DILUTION-CC challenge: it is insufficient for the spectral action to produce a small $a_0$ at one particular value of $\tau$; the cancellation mechanism must be stable against all loop corrections to the matter sector living on the spectral triple. Second, Weinberg's no-go theorem constrains any self-adjustment mechanism within the spectral action: if one seeks a local scalar field on $M^4$ that absorbs the $a_0$ overshoot, the vacuum must not be translationally invariant (the exflation transit through the van Hove fold at $\tau = 0.190$ does break translational invariance, potentially evading this assumption). Third, the sequestering mechanism's key insight -- that the CC is a global quantity requiring a global measurement (scanning all of spacetime) -- has a structural echo in the spectral action formalism where the vacuum energy is a spectral sum over ALL eigenvalues of $D_K$ (a global property of the fiber geometry), not a local field-by-field contribution. The question for exflation is whether the spectral triple's structure contains an analog of the sequestering's global constraint $\langle R \rangle = 0$ that could render the residual CC radiatively stable.
