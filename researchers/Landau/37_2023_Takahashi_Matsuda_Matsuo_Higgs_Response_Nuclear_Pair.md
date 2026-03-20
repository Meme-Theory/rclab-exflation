# Higgs Response and Pair Condensation Energy in Superfluid Nuclei

**Author(s):** Kengo Takahashi, Yusuke Matsuda, Masayuki Matsuo

**Year:** 2023

**Journal:** Progress of Theoretical and Experimental Physics, vol. 2023, article 083D01

---

## Abstract

The Higgs response—a collective mode characterizing amplitude oscillations of the Cooper pair condensate—provides a novel probe of pairing correlations in nuclei. This work introduces a "Higgs operator" as a pair-transfer probe and analyzes its linear response within the quasi-particle random-phase approximation (QRPA) applied to the Skyrme-Hartree-Fock-Bogoliubov (SHFB) framework. The authors demonstrate that the pair condensation energy can be extracted from the Higgs strength sum and static polarizability. Calculations for $^{110}$Sn and nearby isotopes validate the approach and predict that the Higgs response should be experimentally accessible via pair-transfer reactions. This work bridges condensed-matter concepts (Higgs boson in superconductors) with nuclear physics, providing a new window into superfluid nuclear structure.

---

## Historical Context

In infinite superconducting/superfluid systems, the Higgs mode is a well-established collective excitation: a scalar amplitude oscillation of the order parameter $\Delta(t) = \Delta_0 (1 + \epsilon e^{-i\omega t})$. The Higgs frequency, $\omega_H \approx 2\Delta$ in the weak-coupling BCS limit, marks the energy to create a coherent "breathing mode" of the condensate. Unlike the Goldstone mode (phase oscillation, gapless), the Higgs mode is gapped and massive.

However, in finite systems like nuclei, the Higgs concept requires careful adaptation. Nuclei are far from infinite: typical nuclear pairing involves only a handful of pairs (e.g., $\sim 3-5$ pairs in $^{110}$Sn). Moreover, nuclei have structure—not homogeneous pairing but pairing concentrated near specific single-particle levels (the pairing window). These constraints make the nuclear Higgs response qualitatively different from superconductors.

Takahashi et al.'s work is important because:

1. It systematically defines the **Higgs operator in finite nuclei** (which previous approaches lacked)
2. It uses **QRPA** to compute linear response (valid beyond mean-field)
3. It connects to **experimental observables** (pair-transfer cross sections)
4. It shows that the **pairing strength can be inferred** from Higgs response measurements

---

## Key Arguments and Derivations

### Pair Condensation Energy and Order Parameter

In a nuclear superfluid (BCS or Bogoliubov state), the pairing correlations are characterized by the **gap parameter** $\Delta$. The condensation energy (energy gained by pairing) is:

$$E_{\text{cond}} = -\sum_{i} u_i^2 v_i^2 \Delta_i$$

where $u_i, v_i$ are Bogoliubov amplitudes (coherence factors) and $\Delta_i$ is the gap for the $i$-th level. Summing over all paired levels:

$$E_{\text{cond,total}} = -\sum_i u_i^2 v_i^2 \Delta$$

where $\Delta$ is the average gap. The condensation energy is **not directly observable** in nuclei because there is no experiment that directly measures $\Delta$. However, the Higgs mode provides an indirect route.

### The Higgs Operator

In infinite systems, the Higgs mode corresponds to a uniform modulation:

$$\Delta(t) = \Delta_0 \cos(\omega_H t / 2)$$

For a nucleus, Takahashi et al. define a **Higgs-like operator** that raises or lowers pairs with zero total momentum:

$$\hat{\mathcal{O}}_H = \sum_{k>0} c_{k,\uparrow}^\dagger c_{\bar{k},\downarrow}^\dagger + \text{h.c.}$$

where $k$ ranges over the pairing window and $\bar{k}$ is the time-reversed state. This operator excites the condensate from its ground state, creating a state with one additional Cooper pair (or removing one):

$$|\Psi_\text{Higgs} \rangle \sim \hat{\mathcal{O}}_H | \Psi_0 \rangle$$

The excitation energy is:

$$E_{\text{Higgs}} = E[\Psi_\text{Higgs}] - E[\Psi_0] \approx 2\Delta + \text{finite-size corrections}$$

### Linear Response Theory and QRPA

The Higgs response function (strength of excitations to Higgs-like final states) is computed using QRPA:

$$S(\omega) = \sum_n | \langle n | \hat{\mathcal{O}}_H | 0 \rangle |^2 \delta(\omega - E_n)$$

In QRPA, the excited states are described as:

$$|n\rangle = \sum_{\alpha\beta} (X_{\alpha\beta}^n a_\alpha^\dagger a_\beta + Y_{\alpha\beta}^n a_\beta a_\alpha) |0\rangle$$

where $\alpha, \beta$ label particle-hole excitations. The amplitudes $X, Y$ obey the QRPA equations:

$$\begin{pmatrix} A & B \\ -B^* & -A^* \end{pmatrix} \begin{pmatrix} X \\ Y \end{pmatrix} = \hbar\omega \begin{pmatrix} X \\ Y \end{pmatrix}$$

The matrices $A, B$ depend on the mean-field (HFB) state and the interaction.

### Strength Sum and Polarizability

The **strength sum** (total strength integrated over all frequencies) is:

$$m_1 = \int_0^\infty d\omega \, \omega S(\omega) = \sum_n | \langle n | [\hat{\mathcal{O}}_H, [\hat{H}, \hat{\mathcal{O}}_H]] | 0 \rangle |^2$$

By the **Kramers-Kronig relation**, this sum constrains the average frequency of excitation. For the Higgs mode, the strength sum is dominated by the $2\Delta$ pole:

$$m_1 \approx (2\Delta)^2 \times (\text{number of pairs in pairing window})$$

The **static polarizability** (response at $\omega = 0$) is:

$$\chi_0 = \int_0^\infty \frac{d\omega}{\pi} \frac{S(\omega)}{\omega}$$

This quantity measures how easily the condensate can be "pushed" (pair amplitudes modulated) without exciting real states. For a weak-coupling superconductor:

$$\chi_0 \propto \frac{1}{\Delta}$$

Lower gaps (stronger pairing) lead to higher polarizability. The combination:

$$E_{\text{cond}} \sim \frac{m_1}{\chi_0} \times \text{constant}$$

allows extraction of the condensation energy from measurable quantities.

### Finite-Size Effects in Nuclei

Unlike infinite systems, nuclear pairing involves only $N_{\text{pairs}} \sim 3-10$ pairs. The Higgs frequency is modified:

$$\omega_H = 2\sqrt{\Delta^2 + \xi^2}$$

where $\xi$ is a level-spacing effect. For $^{110}$Sn, typical values are $\Delta \sim 1.5$ MeV and level spacing $\delta \sim 0.5$ MeV, giving $\omega_H \sim 3.5$ MeV.

The fragmentation of strength (not all strength at $2\Delta$ but spread over $\sim 1$ MeV range) is a direct consequence of finite size. Takahashi et al.'s QRPA calculations capture this fragmentation explicitly.

### SHFB Framework

The mean-field basis is the Skyrme-Hartree-Fock-Bogoliubov solution (a generalization of HFB to include nuclear interactions). The Skyrme force is:

$$V_{\text{Skyrme}} = \sum_{ij} t_0 (1 + x_0 P_\sigma) \delta(\mathbf{r}_i - \mathbf{r}_j) + \ldots$$

where $P_\sigma$ exchanges spin. Different Skyrme parameterizations (SLy5, SkM*, etc.) yield slightly different gaps. The QRPA is built on top of this SHFB ground state, treating small vibrations around the mean field.

---

## Key Results

1. **Higgs Operator Definition** — A well-defined Higgs operator for finite nuclei is introduced: pair creation/annihilation with zero total momentum. This enables systematic calculation of Higgs response.

2. **Strength Sum Determines Gap** — The first moment of the Higgs strength sum, $m_1 \propto \Delta^2 \times N_{\text{pairs}}$, directly reflects the pairing gap. By measuring $m_1$ experimentally, one can infer $\Delta$.

3. **Polarizability Measures Condensation Energy** — Static polarizability $\chi_0$ is inversely proportional to condensation energy density. Experimental measurement of $\chi_0$ yields $E_{\text{cond}}$ directly.

4. **Finite-Size Fragmentation Predicted** — The Higgs strength is fragmented over a $\sim 1$ MeV range, not concentrated at a single frequency. This fragmentation is a signature of finite size (not infinite-system BCS).

5. **Pair-Transfer Experiments Accessible** — The Higgs response (matrix elements of $\hat{\mathcal{O}}_H$) can be accessed experimentally via pair-transfer reactions (e.g., $(p, ^3$He$)$ or $(\alpha, ^6$He$)$ reactions), where the transferred pair couples to the Higgs pole.

6. **QRPA Validation with Skyrme** — Calculations using multiple Skyrme parameterizations show that the Higgs response is robust (results differ by ~20% between force choices), indicating the phenomenon is not force-dependent.

7. **Pairing Strength Extraction** — From measured strength sum $m_1$ and polarizability $\chi_0$, one can extract the effective pair interaction strength $g_{\text{pair}}$ in the pairing window.

---

## Impact and Legacy

This work opens a new experimental and theoretical direction in nuclear structure physics:

- **Pair-Transfer Experiments**: Motivates searches for Higgs-like signals in pair-transfer reactions (some experiments are underway or planned)
- **Generalized Higgs Concept**: Extends the superconductor Higgs concept to nuclear and finite-size systems, bridging condensed-matter and nuclear physics
- **Pairing Diagnostics**: Provides a new tool to measure pairing strength and gap in exotic nuclei far from stability (where other methods are difficult)
- **Collective Mode Spectroscopy**: Adds to the arsenal of collective-mode measurements (quadrupole vibrations, octupole vibrations, etc.) in nuclei

---

## Framework Relevance

**Higgs Mode in K_7 BCS**: The framework's K_7 sector (8 quantum states, 7 of which are degenerate in the broken-symmetry phase) undergoes a BCS instability. The Higgs analog in the K_7 system would be an amplitude oscillation of the pair condensate on the SU(3) fiber. Takahashi et al.'s formalism (QRPA on HFB) is directly applicable to the framework's K_7 dynamics.

**Pair Condensation Energy**: Takahashi et al. extract $E_{\text{cond}}$ from response functions. The framework predicts $E_{\text{cond}} = -0.115$ (Session 35, in units where the mean-field energy ~1). The Higgs response in the framework's K_7 system should exhibit strength sum and polarizability consistent with this energy—an experimentally testable prediction if the framework can be realized in tabletop systems (e.g., synthetic materials or analog simulators).

**Fragmentation from Finite Size**: The framework operates in the extreme 0D limit ($L/\xi_{GL} = 0.031$, Session 38). Takahashi et al. show that finite-size systems fragment the Higgs strength (1 MeV spread for ~8 pairs). The framework's 8-state K_7 system has maximal fragmentation—every state couples distinctly to pair excitations. The Higgs response prediction for the framework would be a broad, structured spectrum, not a simple delta function.

**QRPA Beyond Mean-Field**: The framework's ground state is described by an HFB ansatz (mean-field). To compute realistic Higgs response, one needs QRPA corrections (as Takahashi et al. do). The framework should similarly include QRPA when computing precision predictions for external probes.

**Pairing Window Concept**: Takahashi et al. emphasize that only a limited range of single-particle levels (the "pairing window") contribute significantly to pairing. The framework's K_7 sector has only 8 levels total—effectively a single pairing window. This makes the framework an ideal laboratory for studying the Higgs response in the narrowest-possible pairing window.

---

## References

- Takahashi, K., Matsuda, Y., & Matsuo, M. (2023). Higgs response and pair condensation energy in superfluid nuclei. *Progress of Theoretical and Experimental Physics*, 2023(8), 083D01.
- Bohr, A., & Mottelson, B. R. (1975). *Nuclear Structure* (Vol. 1: Single-Particle Motion). North-Holland.
- Ring, P., & Schuck, P. (1980). *The Nuclear Many-Body Problem*. Springer-Verlag.
- Skyrme, T. H. R. (1956). The effective nuclear potential. *Nuclear Physics*, 9(4), 615-637.
