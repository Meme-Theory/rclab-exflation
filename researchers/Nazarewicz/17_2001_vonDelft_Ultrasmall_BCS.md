# Superconductivity in Ultrasmall Metallic Grains

**Author(s):** Jan von Delft
**Year:** 2001
**Journal:** Annalen der Physik (Leipzig) 10, 1-60
**arXiv:** cond-mat/0101021
**Relevance:** CRITICAL

---

## Abstract

We review recent experimental and theoretical work on superconductivity in ultrasmall metallic grains, i.e. grains sufficiently small that the conduction electron energy spectrum becomes discrete. The discrete excitation spectrum of an individual grain can be measured by the technique of single-electron tunneling spectroscopy, and reveals parity effects indicative of pairing correlations in the grain. After introducing the discrete BCS model that has been used to model such grains, we review a phenomenological, grand-canonical, variational BCS theory describing the paramagnetic breakdown of these pairing correlations with increasing magnetic field. We also review recent canonical theories that have been developed to describe how pairing correlations change during the crossover, with decreasing grain size, from the bulk limit to the limit of few electrons, and compare their results to those obtained using Richardson's exact solution of the discrete BCS model.

---

## Key Arguments and Derivations

### Experimental Setup and Measurements (Secs. 2-3)

Ralph, Black and Tinkham (RBT) studied Al grains with radii $r \lesssim 5$ nm using single-electron tunneling spectroscopy. Key parameters: mean level spacing $d \sim 0.02$-$0.3$ meV (estimated from $d = 2\pi^2\hbar^2/(mk_F \cdot \text{Vol})$), charging energy $E_C \sim 5$-$50$ meV, bulk gap $\tilde{\Delta} = 0.38$ meV (thin film value). Anderson's criterion $d \gtrsim \tilde{\Delta}$ is satisfied in the smallest grains.

A striking parity effect was observed: even-$N$ grains show a spectroscopic gap $\gg d$ between the first two conductance peaks, while odd-$N$ grains do not. This is direct evidence for BCS pairing correlations. The gap is driven to zero by an applied magnetic field, allowing study of paramagnetic breakdown.

### Discrete BCS Model (Sec. 4)

The model Hamiltonian is:
$$\hat{H} = \sum_{j,\sigma=\pm} (\varepsilon_j - \mu - \sigma h) c^\dagger_{j\sigma} c_{j\sigma} - \lambda d \sum_{ij} c^\dagger_{i+} c^\dagger_{i-} c_{j-} c_{j+}$$
where $\varepsilon_j = jd + (1-p)d/2$ with parity $p = N \mod 2$, $h = \frac{1}{2}\mu_B g H$ is the Zeeman energy, and $\lambda$ is a dimensionless coupling constant. The bulk gap is $\tilde{\Delta} = \omega_D/\sinh(1/\lambda)$.

Orbital diamagnetism is negligible in ultrasmall grains because $H_\text{orb} \approx \Phi_0/(r^2 \sqrt{E_\text{Thouless}/d})$ grows as $r^{-3}$, giving $H_\text{orb} \approx 19$ T for $r \approx 3$ nm.

### The Blocking Effect (Sec. 4.4)

Singly-occupied levels do not participate in pair scattering, restricting the phase space available and weakening pairing correlations. Eigenstates have the form:
$$|s,B\rangle = \prod_{i \in B} c^\dagger_{i\sigma_i} |\Psi_n\rangle$$
with eigenenergies $E_\alpha = E_n + E_B(h)$, where $E_B(h) = \sum_{i\in B} (\varepsilon_i - \mu - \sigma_i h)$ contains all $h$-dependence. The pair Hamiltonian $\hat{H}_U$ acts only on unblocked levels:
$$\hat{H}_U = \sum_{ij}^U [2(\varepsilon_j - \mu)\delta_{ij} - \lambda d] b^\dagger_i b_j$$

### Canonical Characterization of Pairing (Sec. 5)

A canonically meaningful pairing parameter is defined:
$$\Delta^2_\text{can} \equiv (\lambda d)^2 \sum_{ij} (C_{ij} - \langle c^\dagger_{i+} c_{j+}\rangle \langle c^\dagger_{i-} c_{j-}\rangle)$$
where $C_{ij} = \langle b^\dagger_i b_j \rangle$. For this to be finite in the thermodynamic limit, two conditions must hold: (i) the number of $C_{ij}$ significantly different from zero must scale as $N^2$, and (ii) most $C_{ij}$ for $i < j$ must have the same phase.

The pairing correlations involve redistribution of occupation probability across $\varepsilon_F$: each level $j$ in a finite range around $\varepsilon_F$ has finite probability of being doubly occupied or empty. The "number of Cooper pairs" is roughly $\tilde{\Delta}/d$, and when this becomes $\lesssim 1$, it no longer makes sense to call the system superconducting.

### Generalized Variational BCS Approach (Sec. 6)

For states with spin $s$ and blocked levels $B$:
$$|s,B\rangle = \prod_{i\in B} c^\dagger_{i+} \prod_j^U (u^{(s,B)}_j + v^{(s,B)}_j b^\dagger_j) |0\rangle$$
Each state gets its own pairing parameter $\Delta_{s,B} = \lambda d \sum_j^U u^{(s,B)}_j v^{(s,B)}_j$.

Key findings: (a) All $\Delta_{s,B}$ reduce to $\tilde{\Delta}$ in the bulk limit. (b) Each $\Delta_{s,B}$ decreases with increasing $d$ and vanishes at a critical spacing $d^{BCS}_{s,B}$. (c) $\Delta_s$ decreases rapidly with increasing $s$ at fixed $d$ (blocking effect). (d) The regime $d/\tilde{\Delta} \in [0.77, 2.36]$ where $\Delta_0 \neq 0$ but $\Delta_{s\neq 0} = 0$ represents "minimal superconductivity." (e) A single system cannot be characterized by one pairing parameter — each state requires its own.

### Paramagnetic Breakdown (Sec. 7)

The Clogston-Chandrasekhar field $h_{CC} = \tilde{\Delta}/\sqrt{2}$ marks the bulk transition from superconducting to paramagnetic. For ultrasmall grains, the transition is "softened": the spin change decreases from macroscopically large in bulk to $\Delta s = 1$ at $d \gg \tilde{\Delta}$. After the first ground-state change, the new state is always purely paramagnetic ($\Delta_{s_1} = 0$).

### Richardson's Exact Solution (Sec. 10)

The exact eigenstates are $|\Psi_n\rangle = \prod_{\nu=1}^n B^\dagger_\nu |0\rangle$ with $B^\dagger_\nu = \sum_j (2\varepsilon_j - E_\nu)^{-1} b^\dagger_j$. The pair energies satisfy Richardson's equations:
$$\frac{1}{G} = \sum_{j=1}^L \frac{1}{\varepsilon_j - E_\nu} - \sum_{\mu=1(\neq\nu)}^M \frac{2}{E_\mu - E_\nu}$$

### Comparison of Canonical Methods with Exact Solution (Secs. 11-12)

The exact solution shows a completely smooth SC/FD crossover — no abrupt phase transition. The PBCS method underestimates correlations compared to the exact result. The condensation energy smoothly approaches zero as $d/\tilde{\Delta} \to \infty$, with residual pairing correlations surviving as fluctuations at arbitrarily large $d$. The Matveev-Larkin parameter shows a minimum near $d/\tilde{\Delta} \sim 0.5$, representing suppression of the parity effect.

### Finite Temperature Parity Effects (Sec. 14)

Parity-projected mean-field theory, variational extensions of BCS, and the static path approximation (SPA) all address finite-$T$ behavior. The SPA properly captures fluctuation effects near the transition. A re-entrant spin susceptibility is predicted for even grains.

---

## Key Results

1. Single-electron tunneling spectroscopy directly measures discrete excitation spectra of individual ultrasmall grains, revealing parity-dependent spectroscopic gaps
2. Anderson's criterion for breakdown of superconductivity is $d \gtrsim \tilde{\Delta}$, corresponding to fewer than one Cooper pair
3. The blocking effect — singly-occupied levels do not participate in pair scattering — creates parity-dependent pairing correlations and a regime of "minimal superconductivity"
4. Each eigenstate requires its own pairing parameter $\Delta_{s,B}$; a single mean-field treatment is insufficient for $d \gtrsim \tilde{\Delta}$
5. The Clogston-Chandrasekhar paramagnetic transition is softened from a bulk first-order transition to single spin-flip transitions in ultrasmall grains
6. Richardson's exact solution (rediscovered from nuclear physics) shows the SC/FD crossover is completely smooth, with pairing correlations surviving as fluctuations at all $d$
7. Randomness in level spacings enhances pairing correlations
8. The thin-film Al gap $\tilde{\Delta} = 0.38$ meV is about twice the truly bulk value, with $\lambda = 0.194$
9. Orbital diamagnetism is negligible in grains with $r \lesssim 5$ nm; Pauli paramagnetism dominates
10. The canonical pairing parameter $\Delta_\text{can}$ requires both smeared occupation across $\varepsilon_F$ and phase coherence among pair amplitudes

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Level spacing estimate | $d = 2\pi^2\hbar^2 / (mk_F \cdot \text{Vol})$ | Eq. 1 |
| Charging energy | $E_\text{pot}(N_\text{ex}) = eV_D N_\text{ex} + E_C N^2_\text{ex}$ | Eq. 2 |
| Discrete BCS Hamiltonian | $\hat{H} = \sum_{j,\sigma} (\varepsilon_j - \mu - \sigma h) c^\dagger_{j\sigma} c_{j\sigma} - \lambda d \sum_{ij} c^\dagger_{i+} c^\dagger_{i-} c_{j-} c_{j+}$ | Eq. 6 |
| Bulk gap | $\tilde{\Delta} = \omega_D / \sinh(1/\lambda)$ | Eq. 8 |
| General eigenstate | $\lvert\alpha\rangle = \prod_{i\in B} c^\dagger_{i\sigma_i} \lvert\Psi_n\rangle$ | Eq. 10 |
| Eigenenergy decomposition | $E_\alpha = E_n + E_B(h)$, $E_B(h) = \sum_{i\in B} (\varepsilon_i - \mu - \sigma_i h)$ | Eq. 12 |
| Pair Hamiltonian | $\hat{H}_U = \sum_{ij}^U [2(\varepsilon_j - \mu)\delta_{ij} - \lambda d] b^\dagger_i b_j$ | Eq. 14 |
| Canonical pairing parameter | $\Delta^2_\text{can} = (\lambda d)^2 \sum_{ij} (C_{ij} - \langle c^\dagger_{i+} c_{j+}\rangle \langle c^\dagger_{i-} c_{j-}\rangle)$ | Eq. 22 |
| BCS occupation | $v^2_j = \frac{1}{2}[1 - (\varepsilon_j - \mu)/E_j]$, $E_j = \sqrt{(\varepsilon_j-\mu)^2 + |\Delta_\text{gc}|^2}$ | Eq. 26 |
| Gap equation | $1/\lambda = d \sum_{\lvert\varepsilon_j\rvert < \omega_D} 1/(2E_j)$ | Eq. 27 |
| PBCS ground state | $\lvert\text{PBCS}\rangle = \frac{1}{(N/2)!} (\prod_j u_j) (\sum_j \frac{v_j}{u_j} b^\dagger_j)^{N/2} \lvert 0\rangle$ | Eq. 31 |
| Generalized variational state | $\lvert s,B\rangle = \prod_{i\in B} c^\dagger_{i+} \prod_j^U (u^{(s,B)}_j + v^{(s,B)}_j b^\dagger_j) \lvert 0\rangle$ | Eq. 32 |
| State-dependent pairing parameter | $\Delta_{s,B} = \lambda d \sum_j^U u^{(s,B)}_j v^{(s,B)}_j$ | Eq. 38 |
| CC critical field | $h_{CC} = \tilde{\Delta}/\sqrt{2}$ | Sec. 7 |
| Level-crossing field | $h_{s,s'} = [E_{s'}(0,d) - E_s(0,d)] / [2(s'-s)]$ | Eq. 41 |

## Relevance to Phonon-Exflation

This paper is the primary reference for ultrasmall BCS physics at the scale relevant to the framework. The framework operates at $L/\xi_{GL} = 0.031$ — deep in the ultrasmall regime where $d \gg \tilde{\Delta}$ and pairing correlations survive only as fluctuations. The blocking effect (Sec. 4.4) directly maps onto the framework's seniority structure: the B1 singlet sector has no blocked levels while B2 states have blocked levels that reduce pairing. The finding that each eigenstate requires its own pairing parameter (point (viii) of Sec. 6.2) validates the framework's approach of solving Richardson-Gaudin equations state-by-state rather than using a single mean-field gap. The smooth SC/FD crossover confirmed by Richardson's exact solution (Sec. 10-12) is the mathematical basis for the framework's claim that the transit continuously destroys the condensate ($P_\text{exc} = 1.000$) while preserving the 8 RG conserved integrals.
