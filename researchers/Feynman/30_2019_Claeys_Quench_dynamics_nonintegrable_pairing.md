# Synchronization in time-varying random networks with vanishing connectivity

**NOTE ON FILENAME MISMATCH:** The output filename assigned by the orchestrator ("30_2019_Claeys_Quench_dynamics_nonintegrable_pairing.md") does NOT match the actual content of arXiv:1811.09591v1, which is a synchronization/Kuramoto networks paper by Faggian, Ginelli, Rosas, and Levnajić (November 2018), not a Claeys quench-dynamics paper. Transcription reflects the actual PDF content.

**Author(s):** Marco Faggian, Francesco Ginelli, Fernando Rosas, Zoran Levnajić
**Year:** 2018 (nlin.CD, 23 Nov 2018)
**Journal:** arXiv preprint (nlin.CD)
**arXiv/DOI:** arXiv:1811.09591v1
**Relevance:** HIGH (as proxy for integrability-vs-nonequilibrium dynamics)

---

## Abstract

A sufficiently connected topology linking the constituent units of a complex system is usually seen as a prerequisite for the emergence of collective phenomena such as synchronization. We present a random network of heterogeneous phase oscillators in which the links mediating the interactions are constantly rearranged with a characteristic timescale and, possibly, an extremely low instantaneous connectivity. We show that, provided strong coupling and fast enough rewiring are considered, the network is able to reach partial synchronization even in the vanishing connectivity limit. We also provide an intuitive analytical argument, based on the comparison between the different characteristic timescales of our system in the low connectivity regime, which is able to predict the transition to synchronization threshold with satisfactory precision. In the formal fast switching limit, finally, we argue that the onset of collective synchronization is captured by the time-averaged connectivity network. Our results may be relevant to qualitatively describe the emergence of consensus in social communities with time-varying interactions and to study the onset of collective behavior in engineered systems of mobile units with limited wireless capabilities.

---

## Key Arguments and Derivations

**Section I: Introduction.** Interplay between topology and local dynamics in complex systems. Time-varying connectivity matrices $\mathcal{A}^t_{ij}$ in animal groups, time-dependent plasticity, robot swarms, social networks, communication networks of moving units. Question: under what conditions does macroscopic synchronization emerge in Erdős-Rényi networks with random rewiring and arbitrarily small instantaneous connectivity?

**Section II: Model.** Kuramoto oscillators with time-varying adjacency matrix:
$\dot\varphi_i = \omega_i + (\epsilon/m^t_i)\sum_j \mathcal{A}^t_{ij}(T)\sin(\varphi_j - \varphi_i)$ (Eq. 1), where $\omega_i$ is quenched Gaussian ($\sigma$), $m^t_i = \sum_j \mathcal{A}^t_{ij}$ is instantaneous degree, and $\epsilon$ is coupling. Adjacency matrix: instantaneous Erdős-Rényi with link probability $p$; $q = pN \approx \langle m\rangle$ is mean connectivity. Poissonian rewiring with timescale $T$.

Invariance under scaling (Eq. 2): $t' = \alpha t$, $\sigma' = \sigma/\alpha$, $\epsilon' = \epsilon/\alpha$, $T' = \alpha T$; dimensionless control parameters $T/\sigma$, $\epsilon/\sigma$, $q$.

Kuramoto order parameter $R(t) = |(1/N)\sum_k e^{i\varphi_k(t)}|$ (Eq. 3).

**Section III: Three characteristic timescales.**

1. **Local synchronization time** $\tau_{LS} \approx (2\epsilon)^{-1}$ from linearization of pair dynamics $\delta\dot\varphi = \delta\omega - 2\epsilon\sin\delta\varphi$ (Eq. 6).
2. **Local desynchronization time** $\tau_{LD} \approx \pi/(2\sqrt{2}\sigma)$ (Eq. 9) from $\tau_D\langle\delta\omega\rangle \approx \pi/2$ and Gaussian $\langle\delta\omega\rangle = \sqrt{2}\sigma$ (Eq. 8).
3. **Effective rewiring time** $\tau_{ER} = T/P_{\text{link}} \approx T/q$ (Eq. 13) in the low-connectivity limit.

**Synchronization condition:** $\tau_{LD} \approx \tau_{ER}$ (Eq. 5), giving linear transition line $T_c(q) \approx \pi q/(2\sqrt{2}\sigma)$ (Eq. 14).

**Section III.B: Fast rewiring limit.** For $T \to 0$, the dynamics is controlled by the time-averaged adjacency matrix $\langle\mathcal{A}^t_{ij}(T)/m^t_i\rangle$ (Eq. 17). Via Ott-Antonsen arguments, time-averaged network is globally connected with $A_{ij}/N \approx (1 - e^{-q})/N$ (Eq. 24), reducing dynamics to globally coupled Kuramoto with effective coupling $J = \epsilon(1 - e^{-q})$ (Eq. 26). Synchronization for $J > J_c$, with $J_c = \sqrt{8/\pi}$ for Gaussian natural frequencies.

Intercept: $q_0 = \ln[\epsilon/(\epsilon - J_c)]$ (Eq. 27); corrected transition line $T_c(q) \approx \pi(q - q_0)/(2\sqrt{2}\sigma)$ (Eq. 28).

**Section IV: Finite connectivity.** For $q > \bar{q}$ system synchronizes regardless of rewiring time. Numerical estimate $\bar{q} = 1.66(6)$ for $\epsilon/\sigma = 8$. In strong coupling limit $\bar{q} \to 1^+$ (giant-component threshold). Transition belongs to standard Kuramoto universality class with $\Delta \sim \sqrt{q - q_c}$ (mean-field exponent $\beta = 1/2$).

## Key Results

1. Synchronization achievable in vanishing-connectivity Erdős-Rényi networks with fast rewiring and strong coupling.
2. Three-timescale analysis predicts transition line $T_c(q)$ with satisfactory precision.
3. Fast-switching limit $T \to 0$ reduces to globally coupled Kuramoto with effective coupling $\epsilon(1 - e^{-q})$.
4. Finite connectivity regime: giant-component-vs-synchronization threshold distinction ($\bar{q} > 1$ for finite coupling, $\bar{q} \to 1^+$ in strong-coupling limit).
5. Critical behavior follows standard Kuramoto class with exponent $\beta = 1/2$.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Kuramoto dynamics | $\dot\varphi_i = \omega_i + (\epsilon/m^t_i)\sum_j \mathcal{A}^t_{ij}(T)\sin(\varphi_j - \varphi_i)$ | Eq. 1 |
| Order parameter | $R(t) = \|(1/N)\sum_k e^{i\varphi_k(t)}\|$ | Eq. 3 |
| Rewiring probability | $r = 1 - \exp(-dt/T)$ | Eq. 4 |
| Sync condition | $\tau_{LD} \approx \tau_{ER}$ | Eq. 5 |
| Pair dynamics | $\delta\dot\varphi = \delta\omega - 2\epsilon\sin\delta\varphi$ | Eq. 6 |
| Gaussian $\langle\delta\omega\rangle$ | $\langle\delta\omega\rangle = \sqrt{2}\sigma$ | Eq. 8 |
| Desynch time | $\tau_{LD} \approx \pi/(2\sqrt{2}\sigma)$ | Eq. 9 |
| Link probability | $P_{\text{link}} = 1 - e^{-q} \approx q$ (for $q \ll 1$) | Eq. 12 |
| Effective rewiring | $\tau_{ER} = T/P_{\text{link}} \approx T/q$ | Eq. 13 |
| Transition line | $T_c(q) \approx \pi q/(2\sqrt{2}\sigma)$ | Eq. 14 |
| Time average | $\langle\mathcal{A}^t_{ij}/m^t_i\rangle = (1/\tau_{av})\int_0^{\tau_{av}} \mathcal{A}^t_{ij}(T)/m^t_i\,dt$ | Eq. 17 |
| Averaged network | $A_{ij}/N \approx (1 - e^{-q})/N$ | Eq. 24 |
| Effective coupling | $J = \epsilon(1 - e^{-q})$ | Eq. 26 |
| Intercept | $q_0 = \ln[\epsilon/(\epsilon - J_c)]$ | Eq. 27 |
| Corrected transition | $T_c(q) \approx \pi(q - q_0)/(2\sqrt{2}\sigma)$ | Eq. 28 |
| Kuramoto critical exponent | $\Delta \sim \sqrt{q - q_c}$, $\beta = 1/2$ | §IV.B |

## Relevance to Phonon-Exflation

Despite the filename mismatch, this paper has relevance: the three-timescale framework (local sync, local desynch, effective rewiring) parallels the timescale analysis in the transit-cosmogenesis picture (Mach 13.75 transit, GGE formation time, impedance-mismatch leakage). Time-varying connectivity in Erdős-Rényi networks is a crude analog for stochastic substrate connectivity during the van Hove fold.

**Action recommended:** Orchestrator should verify arXiv ID 1811.09591 is the intended source. If the intended paper is Claeys & Caux "Quench dynamics" (e.g., arXiv:1812.01789 or similar), a re-assignment is needed. The actual paper matching the filename description would likely be:
- P. W. Claeys, J.-S. Caux, "Breaking the integrability of the Heisenberg model through periodic driving", arXiv:1708.07324 (see Ref. 267 in thesis), or
- P. W. Claeys et al., "Spin Polarization through Floquet Resonances in a Driven Central Spin Model", PRL 121, 080401 (2018), arXiv:1712.03117 (Ref. 283 in thesis).

Both are connected to quench dynamics in non/broken-integrable pairing. The GGE permanence claim in the project (S38) requires the Claeys quench-dynamics content specifically.
