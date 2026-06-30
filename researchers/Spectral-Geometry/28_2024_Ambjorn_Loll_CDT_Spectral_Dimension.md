# Causal Dynamical Triangulations: Gateway to Nonperturbative Quantum Gravity

**Author(s):** Jan Ambjorn and Renate Loll
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 2401.09399
**Relevance:** MEDIUM

---

## Abstract

A powerful strategy to treat quantum field theories beyond perturbation theory is by putting them on a lattice. However, the dynamical and symmetry structure of general relativity have for a long time stood in the way of a well-defined lattice formulation of quantum gravity. These issues are resolved by using Causal Dynamical Triangulations (CDT) to implement a nonperturbative, background-independent path integral for Lorentzian quantum gravity on dynamical lattices. We describe the essential ingredients of this formulation, and how it has allowed us to move away from formal considerations in quantum gravity to extracting quantitative results on the spectra of diffeomorphism-invariant quantum observables, describing physics near the Planck scale. Key results to date are the emergence of a de Sitter-like quantum universe and the discovery of an anomalous spectral dimension at short distances.

---

## Key Arguments and Derivations

**Euclidean vs Lorentzian formulation.** The Euclidean path integral for gravity is fundamentally problematic: no Wick rotation exists without a preferred time, and the Euclidean Einstein-Hilbert action is unbounded below. CDT resolves both issues by starting from the Lorentzian path integral $Z = \int \mathcal{D}[g]\, e^{iS_{\text{grav}}[g]}$ and discretizing Lorentzian geometries with causal structure.

**Building blocks.** CDT uses Minkowskian 4-simplices with spacelike edges ($\ell_s^2 = a^2$) and timelike edges ($\ell_t^2 = -\alpha a^2$, $\alpha > 0$). Gluing rules enforce global hyperbolicity: spacetime topology $M = [0,1] \times \Sigma$ with a sliced structure of spatial triangulations $\Sigma(t_i)$ at discrete proper time.

**Regge action.** The simplicial Einstein-Hilbert action $S(T) = \tilde{k}_0 N_0(T) + \tilde{k}_1(N_4^{(1,4)} + N_4^{(4,1)}) + \tilde{k}_2(N_4^{(2,3)} + N_4^{(3,2)})$ is linear in counting variables, with couplings depending on $\kappa_2, \kappa_4, \alpha$.

**Analytic continuation.** For each Lorentzian triangulation, analytically continuing $\alpha \to -\alpha$ gives the relation $S(T, -\alpha - i\epsilon) = iS_E(T, \alpha)$, allowing Monte Carlo evaluation with real Boltzmann weights $e^{-S_E}$.

**Phase diagram.** Four phases are found: de Sitter phase $C_{dS}$ (physically interesting), branched polymer phase $A$, crumpled phase $B$, and bifurcation phase $C_b$. The $C_{dS}$-$C_b$ transition line is second-order, a candidate for a UV fixed point.

**Emergent de Sitter universe.** In the $C_{dS}$ phase, the volume profile matches a round 4-sphere: $\langle N_3(i) \rangle = c\bar{N}_4^{3/4} \frac{1}{\omega \bar{N}_4^{1/4}} \cos^3\left(\frac{i}{\omega \bar{N}_4^{1/4}}\right)$, which is exactly the volume profile of a Euclideanized de Sitter universe. Fluctuations scale as $\Delta N_3 \sim \bar{N}_4^{1/2}$, vanishing relative to the mean.

**Anomalous spectral dimension.** A key discovery: the spectral dimension, measured via diffusion return probability, shows dimensional reduction from $d_S \approx 4$ at large scales to $d_S \approx 2$ at short (Planckian) scales. This is consistent with results from other quantum gravity approaches.

## Key Results

1. Emergent 4D de Sitter-like quantum universe from the gravitational path integral
2. Anomalous spectral dimension: $d_S \approx 4 \to 2$ from IR to UV
3. Four-phase structure with second-order $C_{dS}$-$C_b$ transition (UV fixed point candidate)
4. Lorentzian and Euclidean path integrals give inequivalent results
5. Bounded conformal mode from discrete building blocks (no conformal divergence)
6. Volume profile fluctuations consistent with semiclassical perturbation theory

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Gravitational path integral | $Z = \int \mathcal{D}[g]\, e^{iS_{\text{grav}}[g]}$ | Eq. (1) |
| Einstein-Hilbert action | $S = \frac{1}{16\pi G}\int d^4x \sqrt{|\det g|}\,(R - 2\Lambda) + \int d^4x \sqrt{|\det g|}\, \mathcal{L}_m$ | Eq. (2) |
| EDT Regge action | $S_{\text{eu}}(T) = -\kappa_2 N_2(T) + \kappa_4 N_4(T)$ | Eq. (4) |
| CDT edge lengths | $\ell_s^2 = a^2,\quad \ell_t^2 = -\alpha a^2,\quad \alpha > 0$ | Eq. (6) |
| CDT Lorentzian action | $S(T) = \tilde{k}_0 N_0 + \tilde{k}_1(N_4^{(1,4)} + N_4^{(4,1)}) + \tilde{k}_2(N_4^{(2,3)} + N_4^{(3,2)})$ | Eq. (7) |
| Volume profile | $\langle N_3(i) \rangle = c\bar{N}_4^{3/4} \omega^{-1}\bar{N}_4^{-1/4} \cos^3(i/\omega\bar{N}_4^{1/4})$ | Eq. (16) |
| 4-sphere volume | $V_3(t) = V_4 \frac{3}{4\omega_0 V_4^{1/4}} \cos^3(t/\omega_0 V_4^{1/4})$ | Eq. (18) |

## Relevance to Phonon-Exflation

The CDT spectral dimension flow $d_S \approx 4 \to 2$ from IR to UV is one of the key empirical targets for dimensional reduction predictions in the phonon-exflation framework. The project's spectral geometry analysis (Carlip, Calcagni-Oriti-Thurigen, and earlier Ambjorn-Jurkiewicz-Loll papers) examines whether the M4 x SU(3) fiber compactification naturally produces such a flow. The emergence of a de Sitter-like universe from the CDT path integral provides a nonperturbative benchmark: any viable exflation scenario must reproduce this macroscopic behavior. The CDT phase structure, particularly the second-order $C_{dS}$-$C_b$ transition, may connect to the phase transition physics of the instanton gas during transit.
