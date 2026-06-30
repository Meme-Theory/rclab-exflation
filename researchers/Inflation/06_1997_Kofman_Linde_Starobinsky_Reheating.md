# Towards the Theory of Reheating After Inflation

**Author(s):** Lev Kofman, Andrei Linde, Alexei A. Starobinsky
**Year:** 1997
**Journal:** Physical Review D 56, 3258-3295 (1997)
**arXiv:** hep-ph/9704452
**Relevance:** HIGH -- foundational paper on preheating via parametric resonance after inflation; introduces the concept of stochastic resonance in an expanding universe; establishes the theory of how the inflaton's coherent oscillations transfer energy to matter fields, completing the inflationary picture

---

## Abstract

Reheating after inflation occurs due to particle production by the oscillating inflaton field. In this paper we briefly describe the perturbative approach to reheating, and then concentrate on effects beyond the perturbation theory. They are related to the stage of parametric resonance, which we called preheating. It may occur in an expanding universe if the initial amplitude of oscillations of the inflaton field is large enough. We investigate a simple model of a massive inflaton field $\phi$ coupled to another scalar field $\chi$ with the interaction term $g^2\phi^2\chi^2$. Parametric resonance in this model is very broad. It occurs in a very unusual stochastic manner, which is quite different from parametric resonance in the case when the expansion of the universe is neglected. Quantum fields interacting with the oscillating inflaton field experience a series of kicks which, because of the rapid expansion of the universe, occur with phases uncorrelated to each other. Despite the stochastic nature of the process, it leads to exponential growth of fluctuations of the field $\chi$. We call this process stochastic resonance.

---

## Key Arguments and Derivations

### Section II: Evolution of the Inflaton Field (pp. 3-4)

After inflation ends in $V(\phi) = \frac{1}{2}m^2\phi^2$, the inflaton oscillates sinusoidally with decreasing amplitude: $\phi(t) = \Phi(t)\sin(mt)$ where $\Phi(t) = M_p/\sqrt{3\pi m t} \approx M_p/(3mt)$. The energy density decreases as $\rho_\phi \sim a^{-3}$ (matter-like).

### Section III: Elementary (Perturbative) Theory of Reheating (pp. 4-6)

The perturbative decay rate is $\Gamma(\phi \to \chi\chi) = g^4\sigma^2/(8\pi m)$ for symmetry breaking ($\sigma \neq 0$) and $\Gamma(\phi \to \psi\bar\psi) = h^2 m/(8\pi)$ for fermionic decay. The inflaton equation with decay is $\ddot\phi + 3H\dot\phi + \Gamma\dot\phi + m^2\phi = 0$. Reheating completes when $H \sim \Gamma$, giving reheating temperature $T_r \simeq 0.2\sqrt{\Gamma M_p}$. For $\sigma = 0$ and no fermion coupling, the perturbative decay rate $\Gamma \propto \Phi^2 \propto t^{-2}$ decreases faster than $H \propto t^{-1}$, so reheating never completes perturbatively -- this is a strong constraint on model building.

### Section IV: Parametric Resonance vs. Perturbation Theory (pp. 6-9)

The mode equation for $\chi$ fluctuations coupled to the oscillating inflaton is $\ddot\chi_k + (k^2 + g^2\sigma^2 + 2g^2\sigma\Phi\sin mt)\chi_k = 0$, which reduces to the Mathieu equation $\chi_k'' + (A_k - 2q\cos 2z)\chi_k = 0$ with $A_k = 4(k^2+g^2\sigma^2)/m^2$, $q = 4g^2\sigma\Phi/m^2$. For narrow resonance ($q \ll 1$), modes in the first instability band grow as $\exp(qmt/4)$. Particle production rate is $\propto n_k$ (Bose enhancement), fundamentally different from perturbative decay.

### Section V: Broad vs. Narrow Resonance (pp. 9-10)

For chaotic inflation without symmetry breaking, the mode equation is $\ddot\chi_k + (k^2 + g^2\Phi^2\sin^2 mt)\chi_k = 0$, giving Mathieu parameters $q = g^2\Phi^2/(4m^2)$. When $q \gg 1$ (broad resonance), the standard narrow-resonance analysis breaks down. Particle production occurs in bursts each time $\phi(t)$ passes through zero.

### Sections VI-VII: Stochastic Resonance in Expanding Universe (pp. 10-20)

In an expanding universe, the amplitude $\Phi$ decreases, causing $q$ to change. Each growing mode scans many instability/stability bands within a single oscillation. The resulting particle production is stochastic: the occupation number $n_k$ changes chaotically but grows exponentially on average. The occupation number $n_k$ (an adiabatic invariant) is the proper variable, not $\langle\chi^2\rangle$ which oscillates wildly.

### Sections VIII-X: Backreaction and Rescattering (pp. 20-32)

Produced $\chi$-particles modify the effective potential of $\phi$: the backreaction contribution is $\propto |\phi|$ (not $\phi^2$), changing the oscillation frequency. Preheating proceeds in stages: (1) resonance without backreaction, (2) backreaction increases oscillation frequency (enhancing production), (3) rescattering of $\chi$-particles terminates the resonance.

---

## Key Results

1. Preheating via broad parametric resonance transfers energy from the inflaton to matter fields exponentially fast, far more efficiently than perturbative decay.
2. In an expanding universe, broad resonance becomes stochastic: phases are randomized by expansion.
3. The occupation number $n_k$ is an adiabatic invariant and the proper variable for describing preheating.
4. Backreaction of produced particles on the inflaton potential is $\propto |\phi|$, not $\phi^2$.
5. Reheating never completes in the parametric resonance regime; it always transitions to perturbative decay.
6. The reheating temperature $T_r \simeq 0.2\sqrt{\Gamma M_p}$ is determined by the perturbative stage.
7. For $\sigma = 0$ and no fermionic couplings, the inflaton never fully decays -- a strong model constraint.
8. Preheating can produce particles with mass much greater than the inflaton mass.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Inflaton oscillation | $\phi(t) = \Phi(t)\sin(mt)$, $\Phi(t) = M_p/\sqrt{3\pi m t}$ | Eq. (4) |
| Inflaton energy density | $\rho_\phi = \frac{1}{2}m^2\Phi^2$ | Eq. (7) |
| Perturbative decay equation | $\ddot\phi + 3H\dot\phi + \Gamma\dot\phi + m^2\phi = 0$ | Eq. (13) |
| Reheating temperature | $T_r \simeq 0.2\sqrt{\Gamma M_p}$ | Eq. (19) |
| $\chi$ mode equation (general) | $\ddot\chi_k + 3\frac{\dot a}{a}\dot\chi_k + \left(\frac{k^2}{a^2} + m_\chi^2(0) - \xi R + g^2\phi^2\right)\chi_k = 0$ | Eq. (21) |
| Mathieu equation form | $\chi_k'' + (A_k - 2q\cos 2z)\chi_k = 0$ | Eq. (23) |
| Occupation number | $n_k = \frac{\omega_k}{2}\left(\frac{|\dot\chi_k|^2}{\omega_k^2} + |\chi_k|^2\right) - \frac{1}{2}$ | Eq. (25) |
| Broad resonance parameter | $q = g^2\Phi^2/(4m^2)$ | Sec. V |
| Resonance conditions | $qm \gtrsim \Gamma$, $q^2 m \gtrsim H$ | Eqs. (26)-(27) |

---

## Relevance to Phonon-Exflation

This paper is directly relevant to the exflation framework's GGE (generalized Gibbs ensemble) relic formation mechanism. (1) In standard inflation, reheating converts inflaton coherent oscillations into particles via parametric resonance (preheating) followed by thermalization. In the exflation picture, there is no inflaton to decay -- instead, the supersonic transit through the van Hove fold produces Parker pair excitations ($P_{\rm exc} = 1.000$, 59.8 quasiparticle pairs) directly from the spectral reorganization. This is analogous to particle production when $\phi$ passes through zero (where the effective mass of $\chi$ vanishes), but in exflation it happens once (the fold transit) rather than repeatedly (oscillations). (2) The stochastic resonance phenomenon -- where expansion randomizes phases between successive kicks -- has a direct analog in the post-transit GGE: the quasiparticle pairs produced at the fold propagate through an acoustic white hole boundary where causal contact is severed, preventing thermalization and preserving the GGE structure. (3) The key finding that reheating never completes via parametric resonance alone (requiring perturbative completion) maps to the exflation picture where the GGE relic never thermalizes -- it remains an ordered, non-thermal state permanently (the Ordered Veil).
