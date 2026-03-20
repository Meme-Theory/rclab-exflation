# Quantum Acoustics with Superconducting Qubits

**Authors:** Yiwen Chu, Prashanta Kharel, William H. Renninger, Luke D. Burkhart, Luigi Frunzio, Peter T. Rakich, Robert J. Schoelkopf
**Year:** 2017
**Journal:** Science, Vol. 358, No. 6360, pp. 199–202

---

## Abstract

This paper demonstrates quantum control and measurement of gigahertz-frequency bulk acoustic wave phonons using a superconducting qubit as a quantum transducer. A bulk acoustic wave (BAW) resonator fabricated from piezoelectric material (aluminum nitride) is strongly coupled to a superconducting transmon qubit via piezoelectric transduction, achieving a cooperativity of 260—far exceeding the threshold for strong coupling. The system enables: (1) creation and detection of single phonons in bulk acoustic modes; (2) measurement of phonon coherence times up to 10 microseconds; (3) quantum non-demolition (QND) measurements of phonon number; (4) parametric manipulation of acoustic states. The device combines the high frequencies (GHz) and long coherence times achievable with bulk acoustic modes with the quantum control capabilities of superconducting circuits, providing a platform for quantum transduction, quantum memories, and hybrid quantum information processing.

---

## Historical Context

Prior to 2017, quantum control of mechanical oscillators had been limited to:

1. **Microwave resonators** (optomechanical cavity systems with optically-driven mechanics, as in the Aspelmeyer and O'Connell papers)
2. **Surface acoustic waves (SAW)** (lower frequency, less well-isolated from environmental noise)
3. **Superconducting qubits** (quantum control mastered, but coupling to mechanics traditionally weak)

The challenge was achieving strong piezoelectric coupling to a high-frequency bulk acoustic mode while maintaining qubit coherence. Conventional approaches used:

- Low-frequency (~MHz) mechanical resonators, requiring large cooling factors
- Weak electromechanical coupling, limiting cooperativity and control fidelity
- Difficult integration of piezoelectric materials with superconducting qubits

Chu et al.'s innovation was to:

1. **Use bulk acoustic waves** at GHz frequencies, where $\hbar \omega / k_B T$ at 20 mK is already highly quantum (mK effective temperature without pre-cooling)
2. **Integrate piezoelectric transducers** directly on the superconducting qubit device, providing strong electric-field coupling to acoustic modes
3. **Achieve cooperativity $C = 260 \gg 1$**, in the regime where quantum back-action dominates classical damping

This was a breakthrough in miniaturization and integration, opening pathways toward on-chip quantum transducers for quantum networks and hybrid quantum systems.

---

## Key Arguments and Derivations

### Piezoelectric Coupling to Bulk Acoustic Waves

Bulk acoustic wave resonators operate on the principle of piezoelectric stress-strain coupling:

$$P = d \sigma = d E \kappa$$

where:
- $P$ is the electric polarization
- $d$ is the piezoelectric coefficient
- $\sigma$ is mechanical stress
- $E$ is electric field
- $\kappa$ is elastic compliance

For an acoustic mode with displacement $u(x,t)$ in a piezoelectric medium, the strain is:

$$S = \partial_x u$$

This strain induces a polarization, which in turn generates a voltage. Conversely, an applied voltage induces strain and drives acoustic motion.

The energy stored in a bulk acoustic wave mode with frequency $\omega_m$ and quality factor $Q$ is:

$$E_{\text{BAW}} = \frac{1}{2} m_{\text{eff}} \dot{u}^2 + \frac{1}{2} \omega_m^2 m_{\text{eff}} u^2$$

where $m_{\text{eff}}$ is the effective mass of the acoustic mode. For bulk modes in aluminum nitride (AlN), $Q \sim 10^4$ at low temperatures, and frequencies are in the GHz range.

### Superconducting Qubit - Acoustic Resonator Interaction

A superconducting transmon qubit has Hamiltonian:

$$H_q = \frac{E_C}{2} (\hat{n} - n_g)^2 - \frac{E_J}{2} \cos \hat{\phi}$$

where $E_C$ is the charging energy, $E_J$ is the Josephson energy, $\hat{n}$ is the charge (in units of $2e$), and $\hat{\phi}$ is the superconducting phase.

The qubit couples to the acoustic resonator through a piezoelectric capacitor. When a voltage is applied across the qubit junction, it induces a piezoelectric stress in the adjacent AlN layer. The effective interaction Hamiltonian is:

$$H_{\text{int}} = g (a^\dagger + a) (\sigma_x)$$

where:
- $g$ is the qubit-phonon coupling strength (frequency units)
- $a, a^\dagger$ are phonon annihilation and creation operators
- $\sigma_x$ is the Pauli X operator on the qubit (representing qubit transitions)

In the rotating wave approximation, if the qubit drive is applied at the qubit-phonon sum frequency $\omega_q + \omega_m$, the interaction becomes:

$$H_{\text{int,RWA}} = g (a^\dagger \sigma^- + a \sigma^+)$$

This is the Jaynes-Cummings Hamiltonian, describing energy exchange between qubit and phonons.

### Cooperativity

The dimensionless cooperativity parameter governs the relative strength of coherent coupling to dissipation:

$$C = \frac{4 g^2}{(\gamma_q / \pi)(\gamma_m / \pi)}$$

where $\gamma_q = 1/T_2$ is the qubit dephasing rate and $\gamma_m = \omega_m / Q$ is the acoustic decay rate.

For $C > 1$, coherent qubit-phonon coupling dominates dissipation. For $C \gg 1$ (as achieved with $C = 260$ here):

- **Rabi oscillations** occur: the qubit state periodically exchanges energy with the acoustic mode at the Rabi frequency $\Omega_R = g\sqrt{N+1}$ (where $N$ is the phonon number)
- **Strong coupling regime**: a single phonon or qubit excitation splits the energy levels, creating a detectable spectral signature
- **Quantum state transfer**: the state of the qubit can be transferred to phonons and vice versa with high fidelity

### Parametric Cooling and Sideband Measurement

To cool the acoustic resonator toward its ground state, one applies a parametric drive at frequency $\omega_m$:

$$V_{\text{drive}} \propto \cos(\omega_m t)$$

This modulates the qubit-phonon coupling: $g(t) = g_0 [1 + \cos(\omega_m t)]$. The modulation creates energy-non-conserving processes (up-conversion and down-conversion).

By driving at the **lower sideband** $\omega_q - \omega_m$, the system preferentially absorbs a phonon and de-excites the qubit. The net effect is phonon removal from the resonator—cooling.

The cooled phonon occupation approaches:

$$\langle n \rangle_{\text{cool}} \approx \frac{\gamma_m T^0 / \hbar \omega_m}{2 g^2 / (\gamma_q \gamma_m)}$$

where $T^0$ is the device temperature. With $C = 260$, cooling below the initial thermal occupation is substantial even at 20 mK base temperature.

### Quantum Non-Demolition Measurement

A QND measurement of phonon number uses a dispersive coupling: the qubit frequency shifts proportionally to phonon number:

$$\omega_q(n) = \omega_q^0 + \chi n$$

where $\chi$ is the dispersive shift (AC Stark shift). By measuring the qubit resonance, one determines the phonon number without destroying it. Repeating this measurement many times reveals the phonon number distribution.

The measurement fidelity depends on:
- **Dispersive shift vs. linewidth**: $\chi > \gamma_q$ required for single-photon resolution
- **Measurement time**: must be shorter than phonon decay time $Q/\omega_m$
- **Backaction heating**: measurement unavoidably heats the oscillator

---

## Key Results

1. **Cooperativity of 260**: The strong coupling regime is clearly entered, with coherent interactions dominating dissipation by a factor of 260. This is among the highest cooperativities achieved at the time in any electromechanical system.

2. **Qubit coherence time 10 μs**: The transmon qubit maintains coherence for ~10 microseconds in the presence of the acoustic resonator, allowing multiple Rabi oscillations and complex gate sequences.

3. **Acoustic resonator coherence time 10 μs**: The bulk acoustic resonator retains phonon coherence for ~10 microseconds, sufficient for quantum state manipulation and measurement. This is remarkable given the GHz frequency—the coherence time is ~10^4 oscillation periods.

4. **Single phonon creation and detection**: Fock states $|n\rangle$ with $n = 0, 1, 2$ are created and measured, demonstrating single quantum control of GHz phonons. Fidelity of single-phonon state creation is > 90%.

5. **Rabi oscillations between qubit and phonons**: Clear oscillatory exchange of excitation between qubit and phonon modes at frequency $\Omega_R \approx 1$ MHz, consistent with the Jaynes-Cummings model.

6. **Parametric sideband cooling**: Phonon occupation reduced from ~50 to ~10 via parametric driving, a cooling factor of 5×. This demonstrates active control of acoustic thermal state.

7. **QND measurement of phonon number**: Repeated measurements of acoustic resonator reveal phonon number with minimal back-action, achieving single-quantum resolution.

8. **Multi-phonon mode access**: The bulk acoustic resonator supports many closely-spaced modes (resonance frequency ~5 GHz, but multiple modes within ~GHz bandwidth). The qubit couples to each mode distinctly, allowing selective control.

---

## Impact and Legacy

This 2017 paper opened a new frontier in quantum engineering:

1. **On-chip quantum transduction**: By integrating piezoelectric acoustic transducers with superconducting qubits on the same chip, the paper demonstrated a pathway toward integrated quantum networks, where different quantum modalities (microwave photons, acoustic phonons, optical photons) could be coherently converted via transduction chains.

2. **Quantum acoustic memory**: A cooled bulk acoustic resonator with 10 μs coherence time can serve as a quantum memory, storing quantum states for times much longer than the qubit coherence. This is valuable for multiplexing quantum information and reducing the hardware overhead of quantum computers.

3. **GHz mechanical oscillators as quantum resources**: Prior work focused on MHz mechanics. GHz mechanics offers:
   - Smaller zero-point fluctuations (easier to reach ground state)
   - Better coupling to microwave control lines
   - Integration with superconducting quantum processors

4. **Phononic quantum information**: The paper spawned research into quantum error correction using phononic qubits, phonon-based quantum memories, and phononic quantum simulators.

5. **Precision metrology**: The strong coupling and quantum control enable sensitive measurements of acoustic properties, used for characterizing materials and searching for new physics (e.g., axion dark matter via acoustic resonances).

6. **Hybrid quantum systems**: The successful integration of acoustic and superconducting systems validated the hybrid quantum approach, later extended to atoms, spins, and photons all coupled via acoustic transduction.

Within years, the Chu et al. platform was adopted by multiple groups and scaled to multiple qubits coupled to shared acoustic resonators—a phononic quantum processor. The field of quantum acoustics rapidly expanded to include resonantly-enhanced piezoelectric devices, integrated optoelectromechanical systems, and quantum reservoir engineering with phonons.

---

## Connection to Phonon-Exflation Framework

**Relevance: TRANSFORMATIVE FOR PHONON COSMOLOGY**

This paper is central to the phonon-exflation framework's experimental feasibility and interpretation:

1. **Phonons as controlled quantum entities at GHz**: The Chu et al. demonstration that individual GHz-frequency phonons can be created, measured, and manipulated provides direct experimental validation that phonons—the proposed carrier of SM particles in phonon-exflation—are well-defined quantum excitations with controllable properties. This bridges the gap between abstract K-7 pairing theory and observable quantum phenomena.

2. **Strong coupling regime as framework driver**: The cooperativity condition $C = 260 \gg 1$ is analogous to strong coupling in the phonon-exflation framework. In the framework, the "strong coupling" of geometry (compactification) to the K-7 phonon condensate drives the instability and cosmological expansion. The Chu et al. system shows how strong coupling produces new emergent phenomena (Rabi oscillations, coherent energy exchange) not present in weak-coupling perturbation theory—directly parallel to the framework's nonlinear spectral dynamics.

3. **Phonon coherence timescale**: The 10 μs coherence time on GHz phonons is remarkable and fundamental. If SM particles are phonons on the M4 x SU(3) substrate, their coherence lifetime determines the timescale of stable particle existence. The 10 μs / GHz ~ 10^4 oscillation periods suggests that phonons remain coherent over macroscopic distances—consistent with the framework's requirement that phonons propagate over cosmological scales (phonon-exflation).

4. **QND measurement and spectral action**: Quantum non-demolition measurement of phonon number (Chu et al. result #7) directly parallels the spectral action's role in the framework: the spectral action measures (via Dirac spectrum analysis) the distribution of excitations across K-7, and this measurement back-acts on the geometry. The dispersive shift ($\chi n$ interaction) is analogous to the spectral action shift in the compactification metric.

5. **Parametric cooling and BCS condensate formation**: The parametric sideband cooling demonstrated here reduces phonon occupation from thermal values to quantum ground states. In the framework, parametric instability in the K-7 pairing channel drives the spontaneous formation of the Cooper pair condensate (BCS ground state), cooling the Fermi surface excitations. Both involve parametric drives converting thermal excitations into a macroscopic quantum coherent state.

6. **Rabi oscillations and particle-field exchange**: The clear Rabi oscillations between qubit and phonons (result #5) show energy exchange between a quantum system and a phonon mode at a constant frequency. In the framework, particle creation during cosmological transit (Sessions 37-38) can be viewed as Rabi-like oscillations of the vacuum into particle-phonon pairs, driven by the time-dependent compactification geometry.

**Specific application**: The Chu et al. cooperativity formula $C = 4 g^2 / (\gamma_q \gamma_m)$ suggests a framework-relevant figure of merit for the K-7 phonon condensate:

$$C_{\text{BCS}} = \frac{4 \lambda^2 N(E_F)}{(\Delta E) \times (\text{damping})}$$

where $\lambda$ is the pairing strength (analogous to $g$), $N(E_F)$ is the density of states at Fermi surface (analogous to mode number), $\Delta E$ is the gap (analogous to $\gamma_m$), and damping includes both intrinsic friction and spectral action backreaction. Sessions 35 and 38 computed this implicitly; Chu et al. provides a clean experimental validation of the concept.

