# Dense Nuclear Matter Equation of State from Heavy-Ion Collisions

**Author(s):** Agnieszka Sorensen, Kshitij Agarwal, Kyle W. Brown, Zbigniew Chajecki, Pawel Danielewicz, Christian Drischler, Stefano Gandolfi, Jeremy W. Holt, Matthias Kaminski, Che-Ming Ko, Rohit Kumar, Bao-An Li, William G. Lynch, Alan B. McIntosh, William G. Newton, Scott Pratt, Oleh Savchuk, Maria Stefaniak, Ingo Tews, ManYee Betty Tsang, Ramona Vogt, Hermann Wolter, Hanna Zbroszcyk, et al. (including Witold Nazarewicz among endorsing authors)
**Year:** 2024 (v4)
**Journal:** Progress in Particle and Nuclear Physics
**arXiv:** 2301.13253
**Relevance:** MEDIUM

---

## Abstract

The nuclear equation of state (EOS) is at the center of numerous theoretical and experimental efforts in nuclear physics. With advances in microscopic theories for nuclear interactions, the availability of experiments probing nuclear matter under conditions not reached before, endeavors to develop sophisticated and reliable transport simulations to interpret these experiments, and the advent of multi-messenger astronomy, the next decade will bring new opportunities for determining the nuclear matter EOS, elucidating its dependence on density, temperature, and isospin asymmetry. Among controlled terrestrial experiments, collisions of heavy nuclei at intermediate beam energies (from a few tens of MeV/nucleon to about 25 GeV/nucleon in the fixed-target frame) probe the widest ranges of baryon density and temperature, enabling studies of nuclear matter from a few tenths to about 5 times the nuclear saturation density and for temperatures from a few to well above a hundred MeV, respectively. Collisions of neutron-rich isotopes further bring the opportunity to probe effects due to the isospin asymmetry. However, capitalizing on the enormous scientific effort aimed at uncovering the dense nuclear matter EOS, both at RHIC and at FRIB as well as at other international facilities, depends on the continued development of state-of-the-art hadronic transport simulations. This white paper highlights the essential role that heavy-ion collision experiments and hadronic transport simulations play in understanding strong interactions in dense nuclear matter, with an emphasis on how these efforts can be used together with microscopic approaches and neutron star studies to uncover the nuclear EOS.

---

## Key Arguments and Derivations

### Section 1: Introduction

The EOS describes emergent macroscopic behavior from underlying strong interactions, controlling nuclear structure (binding energy, incompressibility, neutron-skin thickness) and properties at extreme densities/temperatures (neutron stars, heavy-ion collisions). Heavy-ion collisions at intermediate energies ($\sim 10$ MeV/nucleon to $\sim 25$ GeV/nucleon) probe densities from $\sim 0.3 n_0$ to $\sim 5 n_0$ ($n_0 \approx 0.16$ fm$^{-3}$). The symmetry energy expansion characterizes isospin dependence around saturation density.

### Section 2.1: Transport Model Simulations

The Boltzmann-Uehling-Uhlenbeck (BUU) equation governs the single-particle phase-space distribution:
$$\frac{\partial f}{\partial t} + \frac{\partial \epsilon}{\partial \mathbf{p}} \cdot \nabla_{\mathbf{r}} f - \frac{\partial \epsilon}{\partial \mathbf{r}} \cdot \nabla_{\mathbf{p}} f = I_{\mathrm{coll}}[f]$$
where $\epsilon(\mathbf{r}, \mathbf{p})$ is the single-particle energy and $I_{\mathrm{coll}}$ is the collision integral incorporating Pauli blocking. Two main implementations: BUU (test-particle methods) and QMD (quantum molecular dynamics with wave packets). The Transport Model Evaluation Project (TMEP) benchmarks different codes.

Key EOS constraints from collisions include: collective flow (directed $v_1$, elliptic $v_2$), kaon production (sensitive to EOS at $2{-}3 n_0$), pion ratios ($\pi^-/\pi^+$ for symmetry energy), and nucleon coalescence.

### Section 2.2: Microscopic Calculations

Chiral effective field theory ($\chi$EFT) provides systematic nuclear forces with controlled uncertainties. Many-body methods include: coupled-cluster theory, self-consistent Green's function, quantum Monte Carlo, many-body perturbation theory. The EOS of pure neutron matter is relatively well constrained up to $\sim 2 n_0$; symmetric matter less so. Finite-temperature extensions are becoming available.

### Section 2.3: Neutron Star Theory

Neutron star observables constrain the EOS: maximum mass ($\sim 2 M_\odot$), radius measurements from NICER ($R_{1.4} \approx 12{-}13$ km), tidal deformability from GW170817. The TOV equation connects the EOS to stellar structure. Phase transitions (hadron-quark, hyperonic matter) may produce features in the mass-radius relation.

### Section 3: Heavy-Ion Collision Experiments

Experiments span FRIB (low-energy, symmetry energy), HADES/GSI (up to $2.5 n_0$), STAR/RHIC BES-II (up to $\sim 5 n_0$), future CBM/FAIR and NICA. Observables: directed and elliptic flow, stopping, particle production, HBT correlations, light cluster yields. Isotope ratios from neutron-rich beams at FRIB probe symmetry energy at sub- and supra-saturation densities.

### Section 4: Combined Constraints

Bayesian analyses combining $\chi$EFT, neutron star observations, and heavy-ion collision data yield increasingly tight constraints. The density range $1{-}2 n_0$ is constrained by flow data; above $2 n_0$ remains uncertain. The symmetry energy slope parameter $L$ is constrained to $L \approx 40{-}70$ MeV from combined analyses.

### Section 5-6: Connections and Exploratory Directions

Transport simulations also used for detector design, radiation therapy, space exploration. Hydrodynamic models complement transport at high densities. Exploratory topics include: nuclear EOS with dark matter admixture in supermassive neutron stars, reduced-dimensional nuclear EOS, short-range correlations, and high-density symmetry energy.

## Key Results

1. Heavy-ion collisions probe $0.3{-}5\, n_0$ in controlled terrestrial experiments
2. Symmetric matter EOS constrained by collective flow; stiff EOS favored at $1{-}3\, n_0$
3. Symmetry energy at saturation: $S_v \approx 30{-}34$ MeV; slope $L \approx 40{-}70$ MeV
4. Transport code comparison (TMEP) reveals model uncertainties as dominant systematic error
5. Kaon production sensitive to EOS at $2{-}3\, n_0$; pion ratios probe symmetry energy
6. Bayesian combination of HIC + neutron stars + $\chi$EFT narrows allowed EOS band
7. Non-equilibrium effects in transport require careful treatment for EOS extraction
8. FRIB isotope beams will provide unique symmetry energy constraints
9. Phase transitions may manifest as softening of EOS at $\sim 2{-}4\, n_0$

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Nuclear EOS expansion | $E/A(n, \delta) = E/A(n, 0) + S(n)\delta^2 + \mathcal{O}(\delta^4)$ | Sec. 1 |
| Symmetry energy expansion | $S(n) = S_v + \frac{L}{3}\frac{n - n_0}{n_0} + \frac{K_{\mathrm{sym}}}{18}\left(\frac{n - n_0}{n_0}\right)^2 + \cdots$ | Sec. 1.1 |
| BUU transport equation | $\frac{\partial f}{\partial t} + \frac{\partial \epsilon}{\partial \mathbf{p}} \cdot \nabla_{\mathbf{r}} f - \frac{\partial \epsilon}{\partial \mathbf{r}} \cdot \nabla_{\mathbf{p}} f = I_{\mathrm{coll}}[f]$ | Sec. 2.1.1 |
| Skyrme-type mean field potential | $U(n, \delta, p) = \alpha\frac{n}{n_0} + \beta\left(\frac{n}{n_0}\right)^\gamma + U_{\mathrm{sym}}(n)\delta\tau_3 + U_{\mathrm{mom}}(n, p)$ | Sec. 2.1.1 |
| TOV equation | $\frac{dP}{dr} = -\frac{G(\epsilon + P)(m + 4\pi r^3 P)}{r(r - 2Gm)}$ | Sec. 2.3 |
| Tidal deformability | $\Lambda = \frac{2}{3}k_2\left(\frac{R c^2}{G M}\right)^5$ | Sec. 2.3 |
| Directed flow | $v_1 = \langle p_x / p_T \rangle$ | Sec. 3.1.1 |
| Elliptic flow | $v_2 = \langle (p_x^2 - p_y^2) / p_T^2 \rangle$ | Sec. 3.1.1 |

## Relevance to Phonon-Exflation

The nuclear EOS serves as the substrate analog for the phonon-exflation framework. The density-dependent collective behavior described here -- emergence of macroscopic EOS from microscopic nucleon interactions -- parallels the emergence of effective cosmological constants from the instanton gas on the SU(3) fiber. The BUU transport equation's structure (single-particle distribution + collision integral) maps onto the BdG quasiparticle dynamics during the tau-transit, where the "collision integral" is the instanton-mediated pair creation. The symmetry energy's parabolic dependence on isospin asymmetry $\delta$ echoes the framework's parabolic behavior of spectral quantities near the fold. The white paper's emphasis on non-equilibrium transport for EOS extraction resonates with the framework's GGE (generalized Gibbs ensemble) post-transit state that never thermalizes.
