# The BCS-BEC crossover: From ultra-cold Fermi gases to nuclear systems

**Author(s):** Giancarlo Calvanese Strinati, Pierbiagio Pieri, Gerd Ropke, Peter Schuck, Michael Urban
**Year:** 2018
**Journal:** Physics Reports (submitted to Elsevier)
**arXiv:** 1802.05997
**Relevance:** HIGH

---

## Abstract

This report addresses topics and questions of common interest in the fields of ultra-cold gases and nuclear physics in the context of the BCS-BEC crossover. By this crossover, the phenomena of Bardeen-Cooper-Schrieffer (BCS) superfluidity and Bose-Einstein condensation (BEC), which share the same kind of spontaneous symmetry breaking, are smoothly connected through the progressive reduction of the size of the fermion pairs involved as the fundamental entities in both phenomena. This size ranges, from large values when Cooper pairs are strongly overlapping in the BCS limit of a weak inter-particle attraction, to small values when composite bosons are non-overlapping in the BEC limit of a strong inter-particle attraction, across the intermediate unitarity limit where the size of the pairs is comparable with the average inter-particle distance.

The BCS-BEC crossover has recently been realized experimentally, and essentially in all of its aspects, with ultra-cold Fermi gases. This realization, in turn, has raised the interest of the nuclear physics community in the crossover problem, since it represents an unprecedented tool to test fundamental and unanswered questions of nuclear many-body theory. Here, we focus on the several aspects of the BCS-BEC crossover, which are of broad joint interest to both ultra-cold Fermi gases and nuclear matter, and which will likely help to solve in the future some open problems in nuclear physics (concerning, for instance, neutron stars). Similarities and differences occurring in ultra-cold Fermi gases and nuclear matter will then be emphasized, not only about the relative phenomenologies but also about the theoretical approaches to be used in the two contexts. Common to both contexts is the fact that at zero temperature the BCS-BEC crossover can be described at the mean-field level with reasonable accuracy. At finite temperature, on the other hand, inclusion of pairing fluctuations beyond mean field represents an essential ingredient of the theory, especially in the normal phase where they account for precursor pairing effects.

---

## Key Arguments and Derivations

### 1. Historical Background and BCS Wave Function (Sections 1.1-1.2)

The BCS-BEC crossover idea dates to shortly after the BCS theory (1957), when differences between BCS (strongly-overlapping Cooper pairs) and Schafroth-Butler-Blatt theory (non-overlapping composite bosons undergoing BEC) were emphasized. Pioneering theoretical work was done by Eagles (1969), Leggett (1980), and Nozieres-Schmitt-Rink (1985). The crossover took on experimental importance with ultra-cold Fermi gases from 2003 onward.

The BCS ground-state wave function is shown to contain BEC of composite bosons as a limit. When the ratio $v_k/u_k$ is defined as $g_k$, the BCS state can be rewritten as a coherent state of pair operators. When $v_k^2 \ll 1$ for all $k$ (large negative chemical potential), the pair operator becomes effectively bosonic, yielding a BEC state.

### 2. BCS Mean Field (Section 2)

The paper derives the standard gap and number equations for a contact interaction, showing how the chemical potential $\mu$ drives the crossover from BCS ($\mu > 0$, Fermi surface present) to BEC ($\mu < 0$, Fermi surface dissolved). The coupling parameter $(k_F a_F)^{-1}$ parameterizes the crossover: negative for BCS, zero at unitarity, positive for BEC. The crossover region of interest is approximately $-1 \lesssim (k_F a_F)^{-1} \lesssim +1$.

The Bogoliubov-de Gennes (BdG) equations are derived for inhomogeneous systems, and limiting forms (Ginzburg-Landau near $T_c$, Gross-Pitaevskii in BEC limit) are obtained. The treatment of spin-imbalanced (polarized) systems introduces the Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) state.

### 3. Pairing Fluctuations (Section 3)

The Nozieres-Schmitt-Rink (NSR) approach extends the mean-field treatment above $T_c$ by including Gaussian fluctuations of the pairing field. The pair propagator $\Gamma_0(Q)$ is constructed from the particle-particle ladder diagrams and yields the equation for $T_c$ when $\Gamma_0(Q=0)^{-1} = 0$. The density equation is modified by the fluctuation contribution to the thermodynamic potential.

Intra-pair and inter-pair correlations are distinguished: the pair coherence length $\xi_{\text{pair}}$ characterizes the size of individual pairs, while the healing length $\xi$ characterizes inter-pair correlations. The pseudo-gap above $T_c$ is associated with precursor pairing effects where local pairing order survives without long-range coherence.

### 4. Ultra-cold Fermi Gases (Section 4)

Fano-Feshbach resonances provide the experimental means to tune the interaction strength continuously across the crossover. The unitary limit ($|a_F| \to \infty$) is a universal regime where the only energy scale is the Fermi energy, and all thermodynamic quantities are universal functions times their free-gas values. The Bertsch parameter $\xi_B = E/E_{\text{free}}$ at $T=0$ is measured to be $\xi_B \approx 0.376$.

The Tan contact $C$ governs the high-momentum tail of the momentum distribution $n_k \to C/k^4$ and connects to thermodynamic quantities through exact relations. The Josephson effect, collective modes, quantum vortices, and moment of inertia are all discussed across the crossover.

### 5. Nuclear Systems (Section 5)

The deuteron provides a paradigmatic example of a bound state whose BCS-BEC crossover character depends on density. In symmetric nuclear matter, the deuteron transitions from BEC at low density to BCS at high density. Proton-neutron correlations, isospin imbalance, and the liquid-gas transition in nuclear matter are analyzed.

For neutron matter, there is no bound state but a virtual state at nearly zero energy, placing dilute neutron matter (inner crust of neutron stars) close to the unitary limit. The generalized nuclear contact and quartet (alpha-particle) condensation are discussed.

## Key Results

1. The BCS wave function continuously interpolates between BCS and BEC limits through the chemical potential $\mu$, which changes sign at the crossover point.
2. The coupling parameter $(k_F a_F)^{-1}$ provides a universal parameterization of the crossover, with the physically interesting region being $-1 \lesssim (k_F a_F)^{-1} \lesssim +1$.
3. Pairing fluctuations (NSR approach) are essential at finite temperature, particularly in the normal phase for pseudo-gap physics and precursor pairing.
4. The Bertsch parameter at unitarity is $\xi_B \approx 0.376$, confirmed by both experiment and quantum Monte Carlo.
5. The Tan contact $C$ provides exact thermodynamic relations connecting high-momentum behavior to bulk properties.
6. Dilute neutron matter is nearly at the unitary limit, enabling cross-fertilization between cold-atom and nuclear physics.
7. The pair coherence length $\xi_{\text{pair}}$ decreases monotonically from BCS to BEC, while the healing length $\xi$ increases in the BEC limit.
8. The FFLO state for imbalanced systems occupies a narrow sliver of the phase diagram in 3D but is more robust in lower dimensions.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| BCS wave function | $\|\text{BCS}\rangle = \prod_k (u_k + v_k c^\dagger_{k\uparrow} c^\dagger_{-k\downarrow})\|0\rangle$ | Eq. (1) |
| Coherence factors | $v_k^2 = 1 - u_k^2 = \frac{1}{2}\left(1 - \frac{\xi_k}{E_k}\right)$ | Eq. (2) |
| Quasiparticle energy | $E_k = \sqrt{\xi_k^2 + |\Delta_0|^2}$, $\xi_k = k^2/(2m) - \mu$ | Sec. 1.2 |
| BCS as BEC | $\|\text{BCS}\rangle \propto \exp\left(\sum_k g_k c^\dagger_{k\uparrow} c^\dagger_{-k\downarrow}\right)\|0\rangle$, $g_k = v_k/u_k$ | Eq. (3) |
| Gap equation (contact) | $-\frac{m}{4\pi a_F} = \int \frac{d^3k}{(2\pi)^3}\left(\frac{1}{2E_k} - \frac{m}{k^2}\right)$ | Eq. (8) |
| Number equation | $n = \int \frac{d^3k}{(2\pi)^3}\left(1 - \frac{\xi_k}{E_k}\right)$ | Eq. (9) |
| Pair coherence length | $\xi_{\text{pair}}^2 = \int dr\, r^2 |\phi(r)|^2 / \int dr\, |\phi(r)|^2$ | Eq. (6) |
| NSR pair propagator | $\Gamma_0(Q)^{-1} = -\frac{m}{4\pi a_F} - \int \frac{d^3k}{(2\pi)^3}\left(\frac{1-f(\xi_{k+Q/2})-f(\xi_{-k+Q/2})}{i\Omega_\nu - \xi_{k+Q/2} - \xi_{-k+Q/2}} - \frac{m}{k^2}\right)$ | Eq. (55) |
| Tan contact tail | $n_k \to C/k^4$ for $k \to \infty$ | Sec. 4.5 |
| BdG equations | $\begin{pmatrix} \mathcal{H}_0(\mathbf{r}) & \Delta(\mathbf{r}) \\ \Delta^*(\mathbf{r}) & -\mathcal{H}_0(\mathbf{r}) \end{pmatrix} \begin{pmatrix} u_\nu \\ v_\nu \end{pmatrix} = E_\nu \begin{pmatrix} u_\nu \\ v_\nu \end{pmatrix}$ | Eq. (28) |

## Relevance to Phonon-Exflation

This comprehensive review of the BCS-BEC crossover provides the theoretical foundation for the pairing instability mechanism central to the phonon-exflation framework. The crossover from BCS (large, overlapping pairs) to BEC (tight, non-overlapping composites) mirrors the transit dynamics on the SU(3) fiber where the BCS condensate forms via the Van Hove-driven instability. The NSR treatment of pairing fluctuations above $T_c$ directly informs the pseudo-gap and GGE physics identified in Session 38, while the nuclear-matter connections (deuteron crossover, neutron matter at unitarity) provide experimental anchors for the framework's predictions about quasiparticle spectra and pair coherence during the fold transit.
