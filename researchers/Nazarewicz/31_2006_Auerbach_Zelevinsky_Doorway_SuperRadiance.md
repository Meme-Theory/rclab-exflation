# Doorway States in Nuclear Reactions as a Manifestation of the "Super-Radiant" Mechanism

**Author(s):** N. Auerbach, V. Zelevinsky
**Year:** 2006
**Journal:** AIP Conference Proceedings (Nuclei and Mesoscopic Physics)
**arXiv:** nucl-th/0609004
**Relevance:** HIGH

---

## Abstract

A mechanism is considered for generating doorway states and intermediate structure in low-energy nuclear reactions as a result of collectivization of widths of unstable intrinsic states coupled to common decay channels. At the limit of strong continuum coupling, the segregation of broad ("super-radiating") and narrow ("trapped") states occurs revealing the separation of direct and compound processes. We discuss the conditions for the appearance of intermediate structure in this process and doorways related to certain decay channels.

---

## Key Arguments and Derivations

### Effective Hamiltonian (Sec. 2.1)
The Hilbert space is divided into {Q}-subspace of complicated many-body states $|q\rangle$ and {P}-subspace of open channels $|c\rangle$. Using Feshbach projection formalism, the effective Hamiltonian in Q-space is non-Hermitian: $\mathcal{H}_Q = \bar{H} - \frac{i}{2}W$, where $\bar{H}$ is the Hermitian part (shell model + principal value contributions) and $W = 2\pi \sum_{c;\text{open}} H_{QP}|c\rangle\langle c|H_{PQ}$ is the anti-Hermitian decay matrix. The scattering amplitude $T_{ba}(E)$ involves the full propagator $G(E) = 1/(E^{(+)} - \mathcal{H}_Q)$.

### Single Channel Super-Radiance (Sec. 2.2)
For one open channel, $W$ is completely separable (rank 1): $\langle q|W|q'\rangle = 2\pi A^c_q A^{c*}_{q'}$. Only one eigenvalue is nonzero, equal to the trace $\Gamma_0 = 2\pi\sum_q |A^c_q|^2$. This singles out one broad "super-radiant" (SR) state with width $\Gamma_0$ while all orthogonal states are trapped with zero width. When eigenstates of $\bar{H}$ are non-degenerate but with typical spacing $D \ll \langle\gamma_g\rangle$, the qualitative picture persists: one broad state, the rest very narrow.

### General SR Mechanism (Sec. 2.3)
For $N$ intrinsic states and $N_c$ open channels ($N_c \ll N$), the SR mechanism operates when $\kappa^c = \gamma^c / D > 1$. The segregation produces $N_c$ broad SR states and $N - N_c$ trapped states near the real energy axis. The trapped states acquire small widths: $\Gamma_t = \sum_s w_s |H_{st}|^2 / [(\Delta\varepsilon_{st})^2 + w_s^2/4]$. This constitutes a sharp phase transition in the complex energy plane.

### Single Doorway (Sec. 3.1)
When only a subset of {Q} states connects directly to {P} (the doorway states $|d\rangle$), the matrix $W$ factorizes through the doorway admixture: $\langle q|W|q'\rangle = \langle q|d\rangle\langle d|q'\rangle \cdot 2\pi\sum_c |\langle d|H_{DP}|c\rangle|^2$. The SR width equals the total decay width of the doorway: $\Gamma_s = \Gamma^\uparrow_d$. The validity criterion is $\Gamma^\uparrow_d / \Gamma^\downarrow_d > 1$ (escape width exceeds spreading width).

### Doorway Width Decomposition (Sec. 3.3)
The total observed doorway width is the sum: $\mathcal{E}_d = E_d + \Delta - \frac{i}{2}(\Gamma^\uparrow_d + \Gamma^\downarrow_d)$, where $\Gamma^\downarrow_d = 2\pi\overline{|h|^2}/\bar{D}_q$ is the spreading width (golden rule) and $\Gamma^\uparrow_d$ is the continuum decay width.

### Applications
- **Isobaric Analog States (IAS):** IAS serves as doorway with $\Gamma^\uparrow_A > \Gamma^\downarrow_A$ (ratio ~2 in lead region), explaining single-resonance appearance
- **Single-particle resonances:** The single-particle state $|\phi_{s.p.}\rangle$ is the doorway; narrow neutron resonances enveloped by s.p. resonance are the trapped states
- **Giant resonances:** Giant resonance $|G\rangle$ serves as doorway; intermediate structure appears when background states bunch in energy
- **Double-humped potentials:** States in the second minimum serve as doorways for compound states in the first (deeper) well, explaining fission isomers in $^{241}$Pu

## Key Results

1. The super-radiant mechanism produces doorway states through collectivization of widths coupled to common decay channels
2. For $N_c$ channels, exactly $N_c$ broad SR states segregate from $N - N_c$ trapped (narrow) states -- a sharp phase transition
3. A single doorway state produces factorized $W$ matrix regardless of number of open channels
4. Validity criterion: $\Gamma^\uparrow_d / \Gamma^\downarrow_d > 1$ (escape width exceeds spreading width)
5. Total doorway width decomposes additively: $\Gamma_{tot} = \Gamma^\uparrow_d + \Gamma^\downarrow_d$
6. Intermediate structure arises when several channels each have their own doorway, producing resonances with $\Gamma_q \ll \Gamma_{int} < \Gamma_{s.p.}$
7. Hierarchical spreading through multi-step dynamics generates additional structure with spreading widths $\Gamma^\downarrow_\nu = 2\pi\langle|h_{\nu\lambda}|^2\rangle / D_\lambda$

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Effective Hamiltonian | $\mathcal{H}_Q = \bar{H} - \frac{i}{2}W$ | Eq. (10) |
| Decay matrix | $W = 2\pi\sum_{c;\text{open}} H_{QP}\|c\rangle\langle c\|H_{PQ}$ | Eq. (9) |
| Scattering amplitude | $T_{ba}(E) = \sum_{qq'}\langle a\|H_{PQ}\|q\rangle\left(\frac{1}{E^{(+)} - \mathcal{H}_Q}\right)_{qq'}\langle q'\|H_{QP}\|b\rangle$ | Eq. (11) |
| SR trace width | $\Gamma_0 = 2\pi\sum_q \|A^c_q\|^2$ | Eq. (15) |
| SR criterion | $\kappa^c = \gamma^c / D > 1$ | Eq. (18) |
| Trapped state width | $\Gamma_t = \sum_s w_s \|H_{st}\|^2 / [(\Delta\varepsilon_{st})^2 + w_s^2/4]$ | Eq. (21) |
| Doorway characteristic eq. | $E - E_d + \frac{i}{2}\Gamma^\uparrow_d - \sum_\nu \frac{\|h_\nu\|^2}{E - E_\nu} = 0$ | Eq. (36) |
| Spreading width | $\Gamma^\downarrow_d = 2\pi\overline{\|h\|^2} / \bar{D}_q$ | Eq. (37) |
| Total doorway energy | $\mathcal{E}_d = E_d + \Delta - \frac{i}{2}(\Gamma^\uparrow_d + \Gamma^\downarrow_d)$ | Eq. (38) |
| Validity condition | $\Gamma^\uparrow_d / \Gamma^\downarrow_d > 1$ | Eq. (34) |

## Relevance to Phonon-Exflation

The super-radiant doorway formalism provides the theoretical backbone for the S42 doorway-state interpretation of KK mode branching. In the framework, the B2 sector acts as a doorway coupling the internal Q-space (compact KK modes) to open 4D channels. The key ratio $\Gamma^\uparrow_d / \Gamma^\downarrow_d > 1$ (Eq. 34) maps directly onto the question of whether KK decay-out proceeds through a single doorway or fragments into compound structure. The Ericson fluctuation regime ($V/D = 55$ from S42) falls in the strong-coupling limit $\kappa > 1$ where SR segregation applies, confirming that the decay-out is dominated by a small number of broad doorway resonances rather than statistical compound decay.
