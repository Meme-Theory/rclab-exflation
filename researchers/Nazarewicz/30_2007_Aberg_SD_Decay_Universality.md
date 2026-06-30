# Universality of Decay out of Superdeformed Bands in the 190 Mass Region

**Author(s):** D. M. Cardamone, B. R. Barrett, C. A. Stafford
**Year:** 2007
**Journal:** Physical Review C (submitted)
**arXiv:** nucl-th/0702072
**Relevance:** HIGH

---

## Abstract

Superdeformed nuclei in the 190 mass region exhibit a striking universality in their decay-out profiles. We show that this universality can be explained in the two-level model of superdeformed decay as related to the strong separation of energy scales: a higher scale related to the nuclear interactions, and a lower scale caused by electromagnetic decay. Decay-out can only occur when separate conditions in both energy regimes are satisfied, strongly limiting the collective degrees of freedom available to the decaying nucleus. Furthermore, we present the results of the two-level model for all decays for which sufficient data are known, including statistical extraction of the matrix element for tunneling through the potential barrier.

---

## Key Arguments and Derivations

### Introduction (Sec. I)
Superdeformed (SD) states with major-to-minor axis ratio ~2 exhibit new shell closures and magic numbers. After formation at high angular momentum via heavy-ion collisions, nuclei decay down the yrast SD rotational band by E2 transitions, retaining strength through many states. Then, quite suddenly, the SD band loses almost all strength over just one or two states. Wilson et al. demonstrated that the decay profiles, when corrected for differing angular momenta, are nearly identical -- this is *universality*, not merely abruptness. A purely statistical model or chaos-assisted phenomenon cannot generate universality.

### Two-Level Model (Sec. II)
The model keeps one level in each well (SD and ND), connected by a tunneling matrix element V. The Hamiltonian decomposes into three terms: $H = H_W + H_T + H_D$ where $H_W$ gives energies in each well, $H_T$ allows tunneling through the barrier, and $H_D$ gives electromagnetic decay. The full Green's function is obtained via Dyson's equation treating all three on equal footing. The resulting branching ratios are:

$$F_S = \frac{\Gamma_S}{\Gamma_S + \Gamma_N \Gamma_\downarrow / (\Gamma_N + \Gamma_\downarrow)}$$

where $\Gamma_\downarrow = 2\Gamma V^2 / (\Delta^2 + \Gamma^2)$ is the net rate for irreversible tunneling.

### Statistical Extraction of V (Sec. II.B)
Since the ND level detuning $\Delta$ is unknown, a statistical ensemble approach is used. The Wigner surmise gives level spacing distribution, and a probability density $P(V)$ is constructed. The mean tunneling matrix element $\langle V \rangle$ is extracted with $\sigma_V / \langle V \rangle \approx 84\%$, indicating $P(V)$ is well-peaked.

### Results and Universality (Sec. III)
The branching ratio depends on only two dimensionless parameters: $\Gamma_S / \Gamma_N$ and $V_c / V$, each corresponding to one energy scale. Table I provides results for all SD decays with sufficient data (192Hg, 192Pb, 194Hg, 194Pb, 152Dy). The strong separation of scales $\Gamma_S, \Gamma_N \ll D_N, \langle V \rangle$ (electromagnetic meV vs nuclear eV-keV) means SD decay is primarily coherent: thousands of virtual Rabi oscillations during a single decay event. Universality arises because decay-out only occurs when *both* $\Gamma_N \gtrsim \Gamma_S$ and $V \gtrsim V_c$, at which point branching ratios saturate and become insensitive to parameter variations.

## Key Results

1. SD decay-out universality in the A~190 region is explained by the two-level model through the strong separation of nuclear and electromagnetic energy scales
2. Decay is primarily coherent: nuclei undergo thousands of virtual Rabi oscillations during a single decay event ($\hbar\omega_r \gg \Gamma$)
3. Only two dimensionless parameters ($\Gamma_S/\Gamma_N$ and $V_c/V$) determine the branching ratio; both decrease rapidly with spin
4. Universality arises because decay-out is forbidden until both parameters cross critical values simultaneously, producing parameter-insensitive branching ratios
5. Statistical extraction yields tunneling matrix elements $\langle V \rangle$ ranging from ~0.3 eV to ~1100 eV across the dataset
6. The 150 mass region (e.g. $^{152}$Dy) shows somewhat slower variation of $\Gamma_S/\Gamma_N$, predicting less universality
7. Critical tunneling matrix element $V_c$ is extractable from experiment without knowledge of $\Gamma_\downarrow$ or $F_S$

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Well Hamiltonian | $H_W = \begin{pmatrix} \varepsilon_S & 0 \\ 0 & \varepsilon_N \end{pmatrix}$ | Eq. (1) |
| Self-energy | $\Sigma = -\frac{i}{2}\begin{pmatrix} \Gamma_S & 0 \\ 0 & \Gamma_N \end{pmatrix}$ | Eq. (3) |
| ND probability | $P_N(t) = \frac{2V^2}{\|\hbar\omega\|^2} e^{-\Gamma t/\hbar}[\cosh(\omega_i t) - \cos(\omega_r t)]$ | Eq. (7) |
| SD branching ratio | $F_S = \frac{\Gamma_S}{\Gamma_S + \Gamma_N \Gamma_\downarrow / (\Gamma_N + \Gamma_\downarrow)}$ | Eq. (10b) |
| Tunneling rate | $\Gamma_\downarrow = \frac{2\Gamma V^2}{\Delta^2 + \Gamma^2}$ | Eq. (11) |
| Universal form | $F_S = 1 - \frac{1}{1 + (V_c/V)^2 + \Gamma_S/\Gamma_N}$ | Eq. (23) |
| Critical V | $V_c^2 = (\Delta^2 + \Gamma^2)\frac{\Gamma_S/\Gamma_N}{1 + \Gamma_S/\Gamma_N}$ | Eq. (24) |
| Scale separation | $\Gamma_S, \Gamma_N \ll D_N, \langle V \rangle$ | Eq. (22) |
| Wigner surmise | $P(s) = \frac{\pi}{2} s \, e^{-\pi s^2/4}$ | Eq. (13) |
| Mean V | $\langle V \rangle = \sqrt{\frac{\Gamma_\downarrow}{2\Gamma}}\left[\frac{D_N}{4} + \mathcal{O}\left(\frac{\Gamma^2}{D_N}\right)\right]$ | Eq. (19) |

## Relevance to Phonon-Exflation

The two-level model of SD decay-out is the direct nuclear analog for the B2 sector decay-out in the phonon-exflation framework. The universality mechanism -- parameter insensitivity arising from separation of energy scales and simultaneous satisfaction of two critical conditions -- maps onto the KK transit where geometry (fast scale) and pairing (slow scale) play analogous roles. The coherent Rabi oscillation regime ($\hbar\omega_r \gg \Gamma$) parallels the inverted Born-Oppenheimer dynamics identified in S38, and the critical tunneling matrix element $V_c$ provides the template for understanding how the B2 sector's decay-out branching ratio becomes universal across different tau trajectories.
