# Quantum Acoustics with Superconducting Qubits

**Author(s):** Yiwen Chu, Prashanta Kharel, William H. Renninger, Luke D. Burkhart, Luigi Frunzio, Peter T. Rakich, Robert J. Schoelkopf
**Year:** 2017
**Journal:** Science 358, 199-202 (2017)
**arXiv:** 1703.00342
**Relevance:** HIGH

---

## Abstract

The ability to engineer and manipulate different varieties of quantum mechanical objects allows us to take advantage of their unique properties and create useful hybrid technologies. Thus far, complex quantum states and exquisite quantum control have been demonstrated in systems ranging from trapped ions and solid state qubits to superconducting microwave resonators. Recently, there have been many efforts to extend these demonstrations to the motion of complex, macroscopic objects. These mechanical objects have important practical applications in the fields of quantum information and metrology as quantum memories or transducers for measuring and connecting different types of quantum systems. In pursuit of such macroscopic quantum phenomena, mechanical oscillators have been interfaced with quantum devices such as optical cavities and superconducting circuits. In particular, there have been a few experiments that couple motion to nonlinear quantum objects such as superconducting qubits. Importantly, this opens up the possibility of creating, storing, and manipulating non-Gaussian quantum states in mechanical degrees of freedom. However, before sophisticated quantum control of mechanical motion can be achieved, we must overcome the challenge of realizing systems with long coherence times while maintaining a sufficient interaction strength. Here we experimentally demonstrate a high frequency bulk acoustic wave resonator that is strongly coupled to a superconducting qubit using piezoelectric transduction. In contrast to previous experiments with qubit-mechanical systems, our device requires only simple fabrication methods, extends coherence times to many microseconds, and provides controllable access to a multitude of phonon modes. We use this system to demonstrate basic quantum operations on the coupled qubit-phonon system.

---

## Key Arguments and Derivations

### 1. Device Architecture

The quantum electromechanical device consists of a frequency-tunable aluminum transmon qubit coupled to phonons in a sapphire substrate using a thin disk of c-axis oriented aluminum nitride (AlN), 900 nm thick and $d = 200\,\mu$m in diameter. The substrate surfaces form a phononic Fabry-Perot resonator supporting longitudinally polarized thickness modes --- a high-overtone bulk acoustic wave resonator (HBAR).

### 2. Piezoelectric Coupling Mechanism

The piezoelectricity of AlN generates stress $\sigma(\vec{x})$ from the transmon's electric field $\vec{E}(\vec{x})$, which acts on the phonon mode's strain field $s(\vec{x})$. The interaction energy is:

$$H_{\text{int}} = \int \sigma(\vec{x})\, s(\vec{x})\, dV$$

where $\sigma(\vec{x}) = c_{33} d_{33}(\vec{x}) E(\vec{x})$, with $c_{33}$ and $d_{33}$ the stiffness and piezoelectric tensor components. Quantizing and equating to the Jaynes-Cummings Hamiltonian $H_{\text{int}} = \hbar g(a b^\dagger + a^\dagger b)$, the coupling strength is estimated as $\hbar g = c_{33} \int d_{33}(\vec{x}) E(\vec{x}) s(\vec{x})\, dV$.

### 3. Mode Structure

The phonon modes are approximated by stationary modes of a cylindrical volume with strain field distributions:

$$s_{l,m}(\vec{x}) = \alpha_{l,m} \sin\left(\frac{l\pi z}{h}\right) J_0\left(\frac{2j_{0,m} r}{d}\right)$$

where $J_0$ is the zeroth-order Bessel function, $j_{0,m}$ is the $m$th root of $J_0$, $h = 420\,\mu$m is the substrate thickness, and $d = 200\,\mu$m the disk diameter. The eigenfrequencies are:

$$\omega_{l,m} = \sqrt{\frac{l^2}{h^2} v_l^2 + \frac{4j_{0,m}^2}{d^2} v_t^2}$$

with $v_l$ and $v_t$ the longitudinal and transverse sound velocities.

### 4. Strong Coupling Verification

Spectroscopy reveals evenly spaced anticrossings separated by the free spectral range $\nu_{\text{FSR}} = v_l / 2h = 13.2$ MHz, consistent with longitudinal mode number spacing. The coupling constant for the $m = 0$ mode is measured at $g = 2\pi \times (260 \pm 10)$ kHz, in agreement with the predicted $\sim 2\pi \times 300$ kHz. The cooperativity $C = g^2/\kappa\gamma = 260$, comparable to early circuit QED devices and more than an order of magnitude higher than previous qubit-mechanical systems.

### 5. Ground State and Single-Phonon Control

Using a protocol measuring Rabi oscillation amplitudes between qubit $|e\rangle$ and $|f\rangle$ states, the qubit ground state population is 92%. After a swap operation with the phonon, the qubit ground state population increases to 98%, indicating the phonon is indeed in the quantum ground state (more so than the qubit itself).

Vacuum Rabi oscillations demonstrate coherent energy exchange between qubit and phonon. By Stark-shifting the qubit on and off resonance with a phonon mode, swap operations are performed: exciting the qubit then swapping transfers one electromagnetic excitation into a single mechanical phonon.

### 6. Phonon Coherence

Phonon $T_1 = 17 \pm 1\,\mu$s (measured by exciting qubit, swapping to phonon, waiting, swapping back). Phonon $T_2 = 27 \pm 1\,\mu$s (Ramsey sequence). An additional decaying sinusoid at $2\pi \times (340 \pm 10)$ kHz appears in $T_1$ data, corresponding to the frequency difference between $m = 0$ and $m = 1$ transverse modes.

## Key Results

1. First demonstration of strong coupling between a superconducting qubit and a bulk acoustic wave resonator, with cooperativity $C = 260$.
2. Phonon mode confirmed in the quantum ground state (phonon purity $\geq 98\%$).
3. Single-phonon Fock state created and detected via qubit-phonon swap operations.
4. Phonon coherence times: $T_1 = 17\,\mu$s, $T_2 = 27\,\mu$s --- longer than the qubit coherence.
5. Multiple longitudinal modes individually addressable, separated by $\nu_{\text{FSR}} = 13.2$ MHz.
6. Piezoelectric coupling via AlN requires only simple fabrication on standard sapphire substrate.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Jaynes-Cummings coupling | $H_{\text{int}} = \hbar g(a b^\dagger + a^\dagger b)$ | In text |
| Strain field modes | $s_{l,m}(\vec{x}) = \alpha_{l,m}\sin(l\pi z/h)\, J_0(2j_{0,m}r/d)$ | Eq. (1) |
| Mode frequencies | $\omega_{l,m} = \sqrt{(l/h)^2 v_l^2 + (2j_{0,m}/d)^2 v_t^2}$ | Eq. (2) |
| Piezoelectric coupling | $\hbar g = c_{33}\int d_{33}(\vec{x}) E(\vec{x}) s(\vec{x})\, dV$ | In text |
| Free spectral range | $\nu_{\text{FSR}} = v_l / 2h = 13.2$ MHz | In text |
| Cooperativity | $C = g^2/\kappa\gamma = 260$ | In text |

## Relevance to Phonon-Exflation

This paper demonstrates that individual phonons in a macroscopic crystal can be prepared, controlled, and measured with quantum precision, reaching the strong coupling regime of quantum acoustics. For the phonon-exflation framework, this is important in two respects: (1) It validates the treatment of phonons as fully quantum-mechanical objects in macroscopic solids, supporting the program that treats particle excitations as phononic modes of the M4 $\times$ SU(3) substrate. (2) The Jaynes-Cummings interaction $H_{\text{int}} = \hbar g(ab^\dagger + a^\dagger b)$ used here is the same beam-splitter Hamiltonian structure that appears in the qubit-phonon sector of the framework's BCS condensate dynamics.
