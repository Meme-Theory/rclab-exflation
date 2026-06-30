# Van Hove Singularity-Driven Emergence of Multiple Flat Bands in Kagome Superconductors

**Author(s):** Hailan Luo, Lin Zhao, Zhen Zhao, Haitao Yang, Yun-Peng Huang, Hongxiong Liu, Yuhao Gu, Feng Jin, Hao Chen, Taimin Miao, Chaohui Yin, Chengmin Shen, Xiaolin Ren, Bo Liang, Yingjie Shu, Yiwen Chen, Fengfeng Zhang, Feng Yang, Shenjin Zhang, Qinjun Peng, Hanqing Mao, Guodong Liu, Jiangping Hu, Youguo Shi, Zuyan Xu, Kun Jiang, Qingming Zhang, Ziqiang Wang, Hongjun Gao, X. J. Zhou
**Year:** 2024
**Journal:** [Not stated in PDF -- preprint]
**arXiv:** 2403.06085
**Relevance:** HIGH

---

## Abstract

The newly discovered Kagome superconductors AV$_3$Sb$_5$ (A=K, Rb and Cs) continue to bring surprises in generating unusual phenomena and physical properties, including anomalous Hall effect, unconventional charge density wave, electronic nematicity and time-reversal symmetry breaking. Here we report an unexpected emergence of multiple flat bands in the AV$_3$Sb$_5$ superconductors. By performing high-resolution angle-resolved photoemission (ARPES) measurements, we observed four branches of flat bands that span over the entire momentum space. The appearance of the flat bands is not anticipated from the band structure calculations and cannot be accounted for by the known mechanisms of flat band generation. It is intimately related to the evolution of van Hove singularities. It is for the first time to observe such emergence of multiple flat bands in solid materials. Our findings provide new insights in revealing the underlying mechanism that governs the unusual behaviors in the Kagome superconductors. They also provide a new pathway in producing flat bands and set a platform to study the flat bands related physics.

---

## Key Arguments and Derivations

### 1. Kagome Lattice Electronic Structure
The Kagome lattice, with corner-sharing triangle networks, gives rise to characteristic electronic structures: van Hove singularities (vHs) at the Brillouin zone boundary, Dirac cones at the zone corner, and a flat band spanning the full momentum space. The AV$_3$Sb$_5$ family (A=K, Rb, Cs) hosts CDW transitions at ~80 K (KVS), ~102 K (RVS), and ~93 K (CVS).

### 2. Observation of Four Flat Bands
Using high-resolution lab-based laser ARPES (photon energy $h\nu = 6.994$ eV, bandwidth 0.26 meV, energy resolution ~2.5 meV, momentum resolution ~0.004 1/A), four dispersionless features FB1--FB4 were observed spanning the entire measured momentum space in CsV$_3$Sb$_5$:
- FB1: binding energy ~70 meV
- FB2: binding energy ~200 meV
- FB3: binding energy ~550 meV
- FB4: binding energy ~700 meV

These flat bands are not predicted by DFT band structure calculations.

### 3. Ubiquity Across the AV$_3$Sb$_5$ Family
All parent compounds KVS, RVS, and CVS show the flat bands with similar energy scales. Upon Ti-doping in CsV$_{3-x}$Ti$_x$Sb$_5$:
- FB1 and FB2 remain pronounced with slight shifts
- FB3 and FB4 weaken, narrow their energy separation, and eventually merge into a single flat band FB34 at x=0.27 (the sample without CDW)

### 4. Temperature Dependence and CDW Connection
Temperature-dependent measurements on RbV$_3$Sb$_5$ show:
- FB1 and FB2 persist across the entire range (20--170 K) with little temperature dependence
- FB3 and FB4 merge into FB34 above the CDW transition temperature (~102 K)
This strongly indicates FB3/FB4 are related to the CDW transition.

### 5. Van Hove Singularity Origin
The energy positions of the flat bands show excellent correspondence with van Hove singularity energies at the $\bar{M}$ point. In the CDW state of CsV$_3$Sb$_5$, three van Hove singularities (vHs1, vHs2, vHs3) are present at $\bar{M}$, each splitting into upper and lower branches. The flat band energies match these vHs energies precisely.

### 6. Exclusion of Known Mechanisms
The authors systematically exclude:
- Impurity bands (multiple flat bands with vHs-matching energies)
- Localized atomic orbital bands (Fig. 4g analogy)
- Kagome geometry-induced flat bands (~1 eV from Fermi level, not matching)
- Electron-boson coupling (spectral weight should decay away from main bands, inconsistent with observed uniform momentum distribution)
- Electron-mode coupling with coexisting vHs (spectral weight decay inconsistent)

### 7. DFT Calculations
First-principles calculations using PAW-DFT (VASP) with PBE functional, DFT-D3 van der Waals corrections, 2x2x1 supercell for TrH CDW phase. Cutoff energy 600 eV, convergence 10$^{-7}$ eV. Band unfolding via BandUP code.

### 8. Spectral Function Simulation
The Migdal self-energy for electron-mode coupling was computed:
$$\Sigma_{ep}(k, i\omega_n) = \frac{1}{N}\sum_q |g_{k,q}|^2 \left(\frac{b(\Omega_q) + f(\epsilon_{k+q})}{i\omega_n + \Omega_q - \epsilon_{k+q}} + \frac{1 + b(\Omega_q) - f(\epsilon_{k+q})}{i\omega_n - \Omega_q - \epsilon_{k+q}}\right)$$
with Einstein mode $\Omega_q \equiv \Omega_0$ and constant coupling $g_{k,q} \equiv g$.

## Key Results

1. First observation of van Hove singularity-driven emergence of multiple flat bands in any solid material
2. Four flat bands (FB1--FB4) span entire 2D Brillouin zone in AV$_3$Sb$_5$
3. FB3 and FB4 are intimately connected to the CDW transition
4. Energy positions of flat bands match van Hove singularity energies at $\bar{M}$
5. Flat bands are ubiquitous across all three parent compounds (K, Rb, Cs)
6. Known mechanisms of flat band generation cannot account for the observations
7. New paradigm: vHs-driven flat band generation

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Migdal self-energy | $\Sigma_{ep}(k, i\omega_n) = \frac{1}{N}\sum_q \|g_{k,q}\|^2 \left(\frac{b(\Omega_q) + f(\epsilon_{k+q})}{i\omega_n + \Omega_q - \epsilon_{k+q}} + \frac{1 + b(\Omega_q) - f(\epsilon_{k+q})}{i\omega_n - \Omega_q - \epsilon_{k+q}}\right)$ | Eq. (1) |
| Spectral function | $A(k, \omega) = -\frac{1}{\pi}\text{Im}\, G(k, i\omega_n \to \omega + i\delta)$ | Methods |
| Green function | $G(k, i\omega_n) = (i\omega_n - \epsilon_k - \Sigma_{ep})^{-1}$ | Methods |
| Dispersion (simulation) | $\epsilon_k = 2t(\cos k_x + \cos k_y)$ | Methods |
| FB1 energy | $E_{FB1} \approx 70$ meV | Fig. 1 |
| FB2 energy | $E_{FB2} \approx 200$ meV | Fig. 1 |
| FB3 energy | $E_{FB3} \approx 550$ meV | Fig. 1 |
| FB4 energy | $E_{FB4} \approx 700$ meV | Fig. 1 |

## Relevance to Phonon-Exflation

The framework's BCS mechanism chain (instanton $\to$ RPA $\to$ Turing $\to$ van Hove $\to$ BCS) requires van Hove singularities to drive strong-coupling instabilities. This paper provides the first experimental demonstration that vHs can spontaneously generate flat bands -- a mechanism directly parallel to what the framework predicts on SU(3): saddle points in the Dirac spectrum producing divergent DOS that seeds pairing. The observation that flat bands emerge from vHs rather than from lattice geometry or localization is a new paradigm that strengthens the plausibility of the framework's van Hove $\to$ BCS link, where the Dirac operator's saddle points on SU(3) play the role of the Kagome lattice's $\bar{M}$-point vHs.
