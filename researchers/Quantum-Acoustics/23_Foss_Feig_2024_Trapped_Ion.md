# Progress in Trapped-Ion Quantum Simulation

**Author(s):** Michael Foss-Feig, Guido Pagano, Andrew C. Potter, Norman Y. Yao
**Year:** 2024
**Journal:** Annual Reviews (preprint)
**arXiv:** 2409.02990
**Relevance:** MEDIUM

---

## Abstract

Trapped ions offer long coherence times and high fidelity, programmable quantum operations, making them a promising platform for quantum simulation of condensed matter systems, quantum dynamics, and problems related to high-energy physics. We review selected developments in trapped-ion qubits and architectures and discuss quantum simulation applications that utilize these emerging capabilities. This review emphasizes developments in digital (gate-based) quantum simulations that exploit trapped-ion hardware capabilities, such as flexible qubit connectivity, selective mid-circuit measurement, and classical feedback, to simulate models with long-range interactions, explore non-unitary dynamics, compress simulations of states with limited entanglement, and reduce the circuit depths required to prepare or simulate long-range entangled states.

---

## Key Arguments and Derivations

### 2. Trapped-Ion Hardware Developments

Qubits are encoded in two long-lived atomic states: either hyperfine ground states ($^2S_{1/2}$) or ground-metastable pairs ($^2S_{1/2}$-$^2D_{5/2}$). The OMG (Optical-Metastable-Ground) architecture uses multiple qubit encodings in a single ion for preparation, gate, and storage operations, with the advantage of converting physical leakage errors into erasure errors for higher error-correcting thresholds.

**Architecture developments:** Three scaling approaches are discussed:
1. **2D ion crystals** in Penning traps (hundreds of ions, long-range interactions, $p \approx 0.02$-$0.18$) and Paul traps (up to 300 ions in 2D transverse-field Ising simulations)
2. **QCCD (Quantum Charge Coupled Device)** with microfabricated surface traps supporting transport, splitting/merging, and integrated photonics (waveguides, grating couplers for 369nm, 435nm, 760nm, 935nm)
3. **Optical interconnects** linking distant modules via entangled photons ($R_{\text{ent}} = 182\,\text{s}^{-1}$ at 94% fidelity)

Two-qubit gate fidelities reach $\sim 99.9\%$ across Molmer-Sorensen, light-shift, and magnetic field gradient gates. N-body entangling interactions via state-dependent squeezing forces enable single-step N-qubit Toffoli gates.

### 3. Unitary Dynamics and Hamiltonian Digitization

The native trapped-ion unitary evolution is:
$$U_{ij}(t) = \exp\left[-i\zeta_i(t)\sigma^\alpha_i - i\zeta_j(t)\sigma^\alpha_j - i\chi_{ij}(t)\sigma^\alpha_i\sigma^\alpha_j\right]$$
In the uniform-illumination limit, this produces a long-range Ising Hamiltonian $H = \sum_{i<j}\frac{J_0}{|i-j|^p}\sigma^\alpha_i\sigma^\alpha_j$ with tunable power-law exponent $0 \leq p \leq 3$.

**Simulation of nuclear and high-energy physics:**
- Confinement of mesonic excitations observed via domain walls in long-range Ising chains, with discrete meson mass spectra measured experimentally.
- The Schwinger model (1+1D QED) is mapped to a spin Hamiltonian via Kogut-Susskind staggered formulation and Jordan-Wigner transformation:
$$H = w\sum_{n=1}^{N-1}[\sigma^+_n\sigma^-_{n+1} + \text{h.c.}] + \frac{m}{2}\sum_n(-1)^n\sigma^z_n + \frac{J}{2}\sum_{n,l>n}c_{nl}\sigma^z_n\sigma^z_l$$
where gauge constraints are enforced by commutation with Gauss law operators. Simulated with up to $N = 20$ spins variationally.
- Collective neutrino flavor oscillations mapped to all-to-all Heisenberg Hamiltonian $H = \sum_p \vec{B}_p\cdot\vec{\sigma}_p + \mu\sum_{p,q}(1-\cos\theta_{p,q})\vec{\sigma}_p\cdot\vec{\sigma}_q$, realized for $N = 4$ and $N = 8$ neutrinos.
- Beta decay of a baryon simulated using 20 qubits; scattering amplitudes extracted from time delays.

**Quantum metrology via spin squeezing:**
One-axis twisting $H_{\text{OAT}} = \frac{(\sigma^z_T)^2}{N}$ generates spin-squeezed states with sensitivity scaling $\sim 1/N^{5/6}$. Demonstrated with up to $N = 219$ ions in 2D Penning traps (4.0 dB enhancement) and $N = 51$ ions in 1D Paul traps (3.2 dB). The squeezing parameter is $\xi^2 = N\frac{\min_{\hat{n}\perp\hat{x}}\text{Var}[\hat{n}\cdot\vec{\sigma}_T]}{\langle\sigma^x_T\rangle^2}$.

**Hydrodynamics with long-range interactions:**
The long-range XY model $H_{XY} = \sum_{i<j}\frac{J_0}{|i-j|^p}(\sigma^+_i\sigma^-_j + \text{h.c.})$ exhibits tunable transport regimes: diffusive ($z = 2$) for $p > 3/2$ and Levy flight superdiffusion ($z = 2p - 1$) for $1/2 \leq p \leq 3/2$. Experimentally observed in 51-ion chains with $p = 0.9, 1.1, 1.5$.

### 4. Non-Unitary Dynamics from Measurement

**Topological order preparation:** Mid-circuit measurements enforce Gauss' law in lattice gauge theories, enabling constant-depth preparation of toric code ($\mathbb{Z}_2$ gauge theory) ground states. For $\mathbb{Z}_2$ theory: $\prod_{\langle ij\rangle \in +_i} X_{ij} = \sigma^z_i$. Demonstrated on QCCD architectures with qubits arranged on a torus geometry (possible only in shuttling architectures). Non-Abelian ($S_3$) topological order achieved with 22 qubits, including demonstration of non-Abelian anyon braiding.

**Measurement-induced phase transitions (MIPTs):** Competition between entangling unitary gates and disentangling projective measurements produces phase transitions in entanglement structure. A volume-law to area-law transition occurs at a critical measurement rate $p_c$. The topological entanglement entropy $\gamma_{\text{topo}}$ distinguishes these phases.

**Quantum tensor network methods:** Holographic simulation uses mid-circuit measurement and qubit reuse to simulate systems larger than the physical qubit count. Matrix Product States (MPS) with bond dimension $\chi$ require only $\mathcal{O}(\log\chi)$ qubits. Demonstrated for 1D critical Ising model and 2D isoTNS states, achieving up to 62-qubit simulations on 20 physical qubits.

---

## Key Results

1. Two-qubit trapped-ion gate fidelities reach $\sim 99.9\%$ with credible pathways to 10x improvement via laser-free gates
2. QCCD architecture demonstrated at unprecedented scales with 1D racetrack traps and progress toward 2D grid architectures
3. Mesonic bound states observed in long-range Ising chains, connecting to lattice gauge theory confinement
4. The Schwinger model (1+1D QED) Trotterized and simulated with up to $N = 6$ sites digitally; ground state prepared variationally with $N = 20$ spins
5. Collective neutrino oscillations simulated for $N = 8$ neutrinos on Quantinuum hardware
6. Spin squeezing demonstrated with up to 219 ions (4 dB enhancement), approaching scalable regimes
7. Emergent hydrodynamics observed in 51-ion chains with tunable power-law interactions spanning diffusive to Levy flight regimes
8. Non-Abelian ($S_3$) topological order prepared and anyon braiding demonstrated using measurement-assisted circuits on 22 qubits
9. Measurement-induced phase transitions observed with tomographic and entanglement witnesses
10. Holographic quantum simulation achieves 62-qubit equivalent simulation on 20 physical qubits via MPS compression

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Native unitary | $U_{ij}(t) = \exp[-i\zeta_i\sigma^\alpha_i - i\zeta_j\sigma^\alpha_j - i\chi_{ij}\sigma^\alpha_i\sigma^\alpha_j]$ | Eq. 1 |
| Long-range Ising | $H = \sum_{i<j}\frac{J_0}{\|i-j\|^p}\sigma^\alpha_i\sigma^\alpha_j$ | Eq. 2 |
| Schwinger model | $H = w\sum_n[\sigma^+_n\sigma^-_{n+1} + \text{h.c.}] + \frac{m}{2}\sum_n(-1)^n\sigma^z_n + \frac{J}{2}\sum_{n<l}c_{nl}\sigma^z_n\sigma^z_l$ | Eq. 3 |
| Neutrino Hamiltonian | $H = \sum_p\vec{B}_p\cdot\vec{\sigma}_p + \mu\sum_{p,q}(1-\cos\theta_{p,q})\vec{\sigma}_p\cdot\vec{\sigma}_q$ | Eq. 4 |
| One-axis twisting | $H_{\text{OAT}} = \frac{1}{N}\sum_{i,j}J\sigma^z_i\sigma^z_j = \frac{(\sigma^z_T)^2}{N}$ | Eq. 5 |
| Squeezing parameter | $\xi^2 = N\frac{\min_{\hat{n}\perp\hat{x}}\text{Var}[\hat{n}\cdot\vec{\sigma}_T]}{\langle\sigma^x_T\rangle^2}$ | Eq. 6 |
| Long-range XY | $H_{XY} = \sum_{i<j}\frac{J_0}{\|i-j\|^p}(\sigma^+_i\sigma^-_j + \sigma^-_i\sigma^+_j)$ | Eq. 7 |
| Gauss law ($\mathbb{Z}_2$) | $\prod_{\langle ij\rangle \in +_i}X_{ij} = \sigma^z_i$ | Eq. 8 |
| Remote entangling rate | $R_{\text{ent}} = \frac{1}{2}(P_{\text{gen}}P_{\text{coll}})^2 R$ | Sec. 2.1.3 |

---

## Relevance to Phonon-Exflation

This review documents the trapped-ion platform's capability to simulate lattice gauge theories, including the Schwinger model (1+1D QED) and collective neutrino oscillations, which are directly relevant to the phonon-exflation framework's treatment of gauge field dynamics on the internal geometry. The long-range Ising and XY models with tunable power-law interactions ($0 \leq p \leq 3$) provide a concrete experimental platform for testing condensed matter analogs of the framework's BCS instanton physics. The observation of emergent hydrodynamics in Levy flight regimes with adjustable dynamical exponents could inform the framework's treatment of transport during the tau-transit. The holographic simulation approach (MPS compression with qubit reuse) offers a potential route to simulate the framework's finite-dimensional BdG Hamiltonian on near-term quantum hardware.
