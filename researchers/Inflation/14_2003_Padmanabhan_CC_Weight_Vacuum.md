# Cosmological Constant — The Weight of the Vacuum

**Author(s):** T. Padmanabhan
**Year:** 2003
**Journal:** Physics Reports 380, 235-320 (2003)
**arXiv:** hep-th/0212290
**Relevance:** CRITICAL — for a project studying phonon-exflation cosmology where the CC overshoot is the key open problem

---

## Abstract

Recent cosmological observations suggest the existence of a positive cosmological constant $\Lambda$ with the magnitude $\Lambda(G\hbar/c^3) \approx 10^{-123}$. This review discusses several aspects of the cosmological constant both from the cosmological (sections 1-6) and field theoretical (sections 7-11) perspectives. After a brief introduction to the key issues related to cosmological constant and a historical overview, a summary of the kinematics and dynamics of the standard Friedmann model of the universe is provided. The observational evidence for cosmological constant, especially from the supernova results, and the constraints from the age of the universe, structure formation, Cosmic Microwave Background Radiation (CMBR) anisotropies and a few others are described in detail, followed by a discussion of the theoretical models (quintessence, tachyonic scalar field, ...) from different perspectives. The latter part of the review (sections 7-11) concentrates on more conceptual and fundamental aspects of the cosmological constant like some alternative interpretations of the cosmological constant, relaxation mechanisms to reduce the cosmological constant to the currently observed value, the geometrical structure of the de Sitter spacetime, thermodynamics of the de Sitter universe and the role of string theory in the cosmological constant problem.

---

## Key Arguments and Derivations

### Section 1: Introduction — The Many Faces of the Cosmological Constant

Padmanabhan identifies two dual interpretations of the CC from the action $A = \frac{1}{16\pi G}\int (R - 2\Lambda)\sqrt{-g}\,d^4x + \int L_{\text{matter}}\sqrt{-g}\,d^4x$:

1. **Matter interpretation**: $\Lambda$ is a shift in the matter Lagrangian $L'_{\text{matter}} = L_{\text{matter}} - \Lambda/(8\pi G)$, equivalent to a shift in the vacuum energy. This leads to an extra term $Q^i_k = (\Lambda/8\pi G)\delta^i_k \equiv \rho_\Lambda \delta^i_k$ in the energy-momentum tensor, corresponding to an ideal fluid with $P_\Lambda = -\rho_\Lambda$.

2. **Geometric interpretation**: Gravity is described by two constants, $G$ and $\Lambda$, with the Lagrangian $L_{\text{grav}} \propto (1/G)(R - 2\Lambda)$. The CC appears on the left side of Einstein's equations: $R^i_k - \frac{1}{2}\delta^i_k R - \delta^i_k \Lambda = 8\pi G T^i_k$.

**The effective CC**: Both effects combine: $\Lambda_{\text{eff}} = \Lambda + 8\pi G V(\phi_{\min})$, where $V(\phi_{\min})$ is the vacuum energy from matter fields at their minima. Observations constrain $\Lambda_{\text{eff}}$, not $\Lambda$ alone.

**Key property**: The geodesic acceleration equation $\nabla \cdot \mathbf{g} = -4\pi G(\rho + 3P)$ shows that the source of gravitational acceleration is $(\rho + 3P)$, not $\rho$. Since $(\rho_\Lambda + 3P_\Lambda) = -2\rho_\Lambda$, a positive CC produces repulsive gravity.

**The two CC problems**:
1. **Old problem**: Why is $\Lambda L_P^2 \lesssim 10^{-123}$? No known symmetry requires $\Lambda = 0$. Supersymmetry requires vanishing ground state energy but is badly broken.
2. **New problem (coincidence)**: Why is $\rho_\Lambda / \rho_{\text{NR}} = \mathcal{O}(1)$ at the current epoch? Since $\rho_\Lambda$ is constant while $\rho_{\text{NR}}$ decreases, this ratio requires extreme fine-tuning in the early universe.

**Zeldovich's estimate**: The gravitational self-energy of vacuum fluctuations at energy scale $E$ gives $\rho_\Lambda \approx GE^6/(c^8\hbar^4)$, corresponding to $\Lambda L_P^2 \approx (E/E_P)^6$. For $E \approx 1$ GeV this contradicts the bound by "only" 9 orders of magnitude.

### Sections 2-6: Observational Review (brief summary)

Padmanabhan reviews the standard Friedmann cosmology, supernova evidence for acceleration, age constraints, gravitational lensing bounds, quintessence and tachyonic scalar field models, structure formation with dark energy, and CMBR anisotropy constraints. Key observational conclusions: $\Omega_{\text{tot}} = 1.02 \pm 0.02$ (WMAP), $\Omega_{\text{NR}} = 0.27 \pm 0.04$, $\Omega_\Lambda \approx 0.7$, $n_s = 0.93 \pm 0.03$ (WMAP at $k = 0.05$ Mpc$^{-1}$), $w < -0.78$ at 95% CL.

### Section 7: Reinterpreting the Cosmological Constant

**7.1 CC as Lagrange multiplier**: The action $(1/16\pi G)\int (R - 2\Lambda)\sqrt{-g}\,d^4x$ can be viewed as extremizing $\int R\sqrt{-g}\,d^4x$ subject to fixed 4-volume, with $\Lambda$ as the Lagrange multiplier. This would give a time-dependent $\Lambda(t)$ with $\Lambda(t)H(t)^{-2} \sim \mathcal{O}(1)$, but is difficult to implement in a generally covariant theory.

**7.2 CC as constant of integration (unimodular gravity)**: If one restricts variations to satisfy $g^{ab}\delta g_{ab} = 0$ (trace-free), Einstein's equation reduces to its traceless part: $R^i_k - \frac{1}{4}\delta^i_k R = 8\pi G(T^i_k - \frac{1}{4}\delta^i_k T)$. Combined with Bianchi identity and $T^{ab}_{;b} = 0$, one recovers $R + 8\pi GT = \text{const} \equiv -4\Lambda$, giving the full Einstein equation with CC as an integration constant unrelated to vacuum energy.

**7.3 CC as stochastic variable (Padmanabhan's proposal)**: The quantum microstructure of spacetime at Planck scale absorbs vacuum energy like a sponge, but quantum fluctuations leave a residual CC. Treating $(\Lambda_{\text{eff}}/8\pi L_P^2, \mathcal{V})$ as conjugate variables with $\Delta\Lambda \approx 8\pi L_P^2/\Delta\mathcal{V}$, and assuming the 4-volume consists of $N$ Planck-scale cells with Poisson fluctuation $\Delta\mathcal{V} \approx \sqrt{\mathcal{V}}(\alpha L_P)^2$, one obtains $\Delta\Lambda = (8\pi/\alpha^2)H_0^2$, giving $\Omega_\Lambda = 8\pi/(3\alpha^2)$ -- the correct order of magnitude for $\alpha = 2\sqrt{\pi}$. This combines the UV cutoff ($L_P$) with the IR scale ($H_0^{-1}$).

**7.4 Anthropic interpretation**: Galaxy formation requires $\Omega_\Lambda/\Omega_{\text{NR}} \lesssim (1 + z_{\text{gal}})^3 \approx 125$, giving a bound only two orders of magnitude above observation. Padmanabhan notes the anthropic principle has no predictive power and is "suspect in any scientific discussion."

### Section 8: Relaxation Mechanisms

A field $\phi$ coupling to the trace $T = T^a_a$ of the energy-momentum tensor evolves toward $T = 0$, which would give zero CC. However, Weinberg's no-go theorem shows this requires fine-tuning equivalent to the original problem. Padmanabhan discusses explicit models and their failures.

### Sections 9-10: de Sitter Geometry and Thermodynamics

Detailed treatment of de Sitter spacetime structure, horizons, Gibbons-Hawking temperature $T = H/(2\pi)$, and entropy $S = A_H/(4L_P^2)$. Padmanabhan emphasizes the deep connection between thermodynamics and spacetime geometry, and discusses conceptual issues in de Sitter thermodynamics.

### Section 11: String Theory and the CC

Brief discussion of the role of string theory, noting that no concrete mechanism has emerged from string theory to solve the CC problem as of the time of writing.

## Key Results

1. The CC problem has two distinct aspects: the "old" problem ($\Lambda L_P^2 \lesssim 10^{-123}$) and the "new" coincidence problem ($\rho_\Lambda \sim \rho_{\text{NR}}$ today).
2. The CC can be equivalently viewed as a vacuum energy shift (matter side) or a geometric constant (gravity side), with $\Lambda_{\text{eff}} = \Lambda + 8\pi G V(\phi_{\min})$.
3. Unimodular gravity (trace-free variation) recovers Einstein's equation with CC as an integration constant, decoupled from vacuum energy.
4. Padmanabhan's stochastic CC proposal: Planck-scale fluctuations in a discrete spacetime give $\Delta\Lambda \sim H_0^2$ from the UV/IR connection $\Delta\Lambda = 8\pi L_P^2/\Delta\mathcal{V}$.
5. Quintessence and tachyonic scalar field models are reviewed; all suffer from cosmic degeneracy -- different models produce nearly identical observational signatures.
6. Zeldovich's second-order vacuum energy estimate gives $\Lambda L_P^2 \approx (E/E_P)^6$, demonstrating the hierarchy between QFT vacuum energy and the observed CC.
7. Relaxation mechanisms coupling a scalar field to $T^a_a$ generically fail due to Weinberg's no-go theorem.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Einstein-Hilbert + CC action | $A = \frac{1}{16\pi G}\int (R - 2\Lambda)\sqrt{-g}\,d^4x + \int L_{\text{matter}}\sqrt{-g}\,d^4x$ | Eq. (3) |
| Einstein equation (matter side) | $R^i_k - \frac{1}{2}\delta^i_k R = 8\pi G(T^i_k + Q^i_k);\quad Q^i_k \equiv \frac{\Lambda}{8\pi G}\delta^i_k$ | Eq. (4) |
| Einstein equation (geometry side) | $R^i_k - \frac{1}{2}\delta^i_k R - \delta^i_k \Lambda = 8\pi G T^i_k$ | Eq. (5) |
| Effective CC | $\Lambda_{\text{eff}} = \Lambda + 8\pi G V(\phi_{\min})$ | Eq. (7) |
| Geodesic acceleration | $\nabla \cdot \mathbf{g} = -4\pi G(\rho + 3P)$ | Eq. (8) |
| Zeldovich vacuum energy | $\rho_\Lambda \approx \frac{G E^6}{c^8 \hbar^4}$ | Eq. (9) |
| Electroweak symmetry breaking potential | $V = V_0 - \mu^2\phi^2 + g\phi^4$ | Eq. (10) |
| Traceless Einstein equation (unimodular) | $R^i_k - \frac{1}{4}\delta^i_k R = 8\pi G\left(T^i_k - \frac{1}{4}\delta^i_k T\right)$ | Eq. (105) |
| Wave function phase factor | $\Psi \propto \exp\left[-i\left(\frac{\Lambda_{\text{eff}}\mathcal{V}}{8\pi L_P^2}\right)\right]$ | Eq. (110) |
| Stochastic CC from Planck fluctuations | $\Delta\Lambda = \frac{8\pi L_P^2}{\Delta\mathcal{V}} = \frac{8\pi}{\alpha^2}\frac{1}{\sqrt{\mathcal{V}}} \approx \frac{8\pi}{\alpha^2}H_0^2$ | Eq. (111) |
| Anthropic galaxy formation bound | $\frac{\Omega_\Lambda}{\Omega_{\text{NR}}} \lesssim (1 + z_{\text{gal}})^3 \approx 125$ | Eq. (115) |

## Relevance to Phonon-Exflation

Padmanabhan's review is directly relevant to the CC overshoot problem in the phonon-exflation framework on multiple levels. First, his clear distinction between the "matter interpretation" ($\Lambda$ as vacuum energy shift) and the "geometric interpretation" ($\Lambda$ as a constant of gravity) maps precisely onto the spectral action formalism where the zeroth Seeley-DeWitt coefficient $a_0$ is the vacuum energy and the second coefficient $a_2$ is Newton's constant -- both are spectral moments of the same Dirac operator $D_K$, making them structurally linked in a way that neither the matter nor the geometric interpretation alone captures. Second, Padmanabhan's stochastic CC proposal -- where $\Delta\Lambda \sim H_0^2$ arises from Poisson fluctuations in Planck-scale discrete spacetime cells -- has a structural parallel in the exflation framework: the 155,984 eigenvalues of $D_K$ at $L_{\max}=10$ define a discrete spectral structure, and the CC overshoot is precisely the question of how the raw spectral sum (the "bulk value" in Padmanabhan's sponge analogy) gets reduced to the observed residual. Third, his discussion of unimodular gravity (CC as integration constant) is relevant because the spectral action's trace formula naturally produces a trace over eigenvalues that could in principle be split into a bulk (absorbed) piece and a fluctuation piece, analogous to Padmanabhan's UV/IR connection. The key open question for the exflation framework remains: what mechanism in the spectral triple plays the role of Padmanabhan's "sponge" -- absorbing the $\sim L_P^{-4}$ bulk contribution while leaving only the $\sim H_0^2$ residual?
