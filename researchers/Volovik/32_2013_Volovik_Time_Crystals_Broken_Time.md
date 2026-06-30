# On the broken time translation symmetry in macroscopic systems: precessing states and off-diagonal long-range order

**Author(s):** G.E. Volovik
**Year:** 2013
**Journal:** Pis'ma v ZhETF (JETP Letters)
**arXiv:** 1309.1845
**Relevance:** MEDIUM

---

## Abstract

The broken symmetry state with off-diagonal long-range order (ODLRO), which is characterized by the vacuum expectation value of the operator of creation of the conserved quantum number Q, has the time-dependent order parameter. However, the breaking of the time translation symmetry is observable only if the charge Q is not strictly conserved and may decay. This dichotomy is resolved in systems with quasi-ODLRO. These systems have two well separated relaxation times: the relaxation time tau_Q of the charge Q and the energy relaxation time tau_E. If tau_Q >> tau_E, the perturbed system relaxes first to the state with the ODLRO, which persists for a long time and finally relaxes to the full equilibrium static state. In the limit tau_Q -> infinity, but not in the strict limit case when the charge Q is conserved, the intermediate ODLRO state can be considered as the ground state of the system at fixed Q with the observable spontaneously broken time translation symmetry. Examples of systems with quasi-ODLRO are provided by superfluid phase of liquid 4He, Bose-Einstein condensation of magnons (phase coherent spin precession) and precessing vortices.

---

## Key Arguments and Derivations

### 1. Introduction

The paper considers systems characterized by a quasi-conserved macroscopic quantum number Q, where the relaxation time tau_Q of Q is much larger than the energy relaxation time tau_E. The charge Q can be particle number N, quasiparticle number (magnons, phonons, photons, kelvons), spin projection S_z, angular momentum projection L_z, etc.

In such systems, the initial excited state first rapidly relaxes (on timescale tau_E) to the state with minimal energy at fixed Q, then slowly relaxes (on timescale tau_Q) to equilibrium Q = Q_0 where dE/dQ = 0. When Q != Q_0, the system oscillates with frequency omega = dE/dQ. These oscillations represent a broken symmetry state with ODLRO:

<a^+> proportional to e^{i omega t + i alpha}

where a^+ is the creation operator of Q.

The key dichotomy: in the limit tau_Q -> infinity, this is a state with spontaneously broken time translation symmetry (as discussed by Wilczek). But in the strict limit tau_Q = infinity (charge strictly conserved), the oscillations become unobservable because the reference frame against which to measure them is lost.

The resolution: systems with **quasi-ODLRO** where tau_Q >> tau_E. In the intermediate time window tau_Q >> t >> tau_E, these systems exhibit ODLRO with observable broken time translation symmetry.

The canonical example is superfluid 4He where Q = N_4 (number of 4He atoms), omega = mu_4 (chemical potential). The lifetime of 4He atoms is finite due to proton decay (tau_Q > 10^{34} years), so in full equilibrium mu = 0. But we operate in the regime where N_4 is effectively conserved. Observation of the ground state oscillations would require explicit U(1) violation (proton decay), serving as experimental evidence for baryonic charge non-conservation.

### 2. Coherent spin precession and magnon BEC

When Q = S_z (spin projection along the magnetic field), the ODLRO state manifests as spontaneously emerging coherent spin precession. In full equilibrium, S_z = chi H/gamma (susceptibility times field over gyromagnetic ratio).

For superfluid 3He-B with non-equilibrium spin S^z != V chi H/gamma, the system experiences spontaneous SO(2) symmetry breaking via phase coherent precession. The precessing state has ODLRO:

<S_+> = S sin(beta) e^{i omega t + i alpha}

where beta is the tipping angle (cos beta = S_z/S), and the global frequency omega = dE/dS_z is coordinate-independent even for spatially inhomogeneous precession.

The experimental sequence (from stroboscopic records):
1. First ~0.002 s: induction signal disappears due to dephasing
2. During tau_E ~ 0.02 s: spin supercurrent redistributes magnetization, creating phase coherent precession (magnon BEC)
3. Due to magnetic relaxation with tau_Q ~ 1 s: magnon number slowly decreases but precession remains coherent

In magnon language, the quasi-conserved quantity Q is the magnon number N_M = (S - S_z)/hbar, with approximate U(1) symmetry. In full equilibrium, magnon chemical potential mu = 0. The coherent precession corresponds to magnon BEC where the chemical potential mu_M = omega depends on the number of pumped magnons. Relaxation slowly reduces the volume of magnon BEC without destroying it.

The oscillations are observed through the free induction decay signal -- observable because the electromagnetic field interaction explicitly violates SO(2) spin rotation symmetry. In a model system with uniaxial anisotropy (where spin-orbit interaction preserves S_z), the charge would be strictly conserved and the time dependence would be unobservable.

The two-species model considered by Wilczek has Q = N_+ - N_- (population difference) and omega = |mu_+ - mu_-|. Strict charge conservation makes oscillations unobservable; U(1) violation (e.g., tunneling between species) makes the state non-equilibrium with eventual relaxation to mu_+ = mu_-.

### 3. Vortex precession

Another ODLRO example: precession of a vortex line in 3He-B, where hours-long oscillations have been observed experimentally. A vortex is partially trapped by a wire. The trapped portion generates circulating flow with orbital angular momentum:

L_z = hbar (nu/2) n_3 V

where n_3 is the 3He density, nu is the number of circulation quanta, V = pi R^2 l is the volume with trapped circulation.

L_z is quasi-conserved: not strictly conserved due to boundary interaction, but highly reduced at low temperature. The precessing state has ODLRO:

<L_+> proportional to e^{i omega t + i alpha}

with omega = dE/dL_z. Oscillations are observed because the wire is not exactly centered in the cylindrical vessel, causing the vortex length to oscillate.

This coherent precession can be described using macroscopic ac Josephson effect language or BEC of Kelvin waves (kelvons) propagating along the vortex.

Related physics occurs in the propagating turbulent vortex front, where L_z relaxation is much longer than energy relaxation. At low temperature, the vortex system decouples from the environment and chooses its own angular velocity independent of the container.

### 4. Discussion

The broken time translation symmetry may emerge for large tau_Q but is absent at tau_Q = infinity when Q is strictly conserved (breaking is observable only through Q decay). The resolution is quasi-ODLRO systems.

What distinguishes these states from general periodic dynamical states is the ODLRO itself. The class of quasi-ODLRO states does NOT include:
- Amplitude (Higgs) modes after quench in superfluids/superconductors
- Oscillations in inflationary cosmology
- Vacuum energy decay models
- Cyclic universe oscillations

---

## Key Results

1. Broken time translation symmetry requires quasi-conservation (tau_Q >> tau_E), not strict conservation (tau_Q = infinity) -- the strict limit makes oscillations unobservable
2. Systems with quasi-ODLRO exhibit a time-dependent order parameter <a^+> ~ e^{i omega t} in the window tau_Q >> t >> tau_E
3. Superfluid 4He is a quasi-ODLRO system where time-dependent ground state oscillations at omega = mu_4 would be observable only if proton decay occurs (explicit U(1) violation)
4. Magnon BEC in 3He-B realizes quasi-ODLRO with Q = S_z, where tau_E ~ 0.02 s and tau_Q ~ 1 s (or much longer in magneto-textural traps)
5. Precessing vortices in 3He-B provide quasi-ODLRO with Q = L_z, with hours-long oscillations observed experimentally
6. Quasi-ODLRO is distinct from Higgs modes, inflationary oscillations, and cyclic cosmology oscillations

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| ODLRO order parameter | <a^+> proportional to e^{i omega t + i alpha} | Eq. (1) |
| Precession frequency | omega = dE/dQ | Text, Sec. 1 |
| Spin ODLRO | <S_+> = S sin(beta) e^{i omega t + i alpha}, cos(beta) = S_z/S | Sec. 2 |
| Magnon number | N_M = (S - S_z)/hbar | Sec. 2 |
| Magnon chemical potential | mu_M = omega = dE/dS_z | Sec. 2 |
| Orbital angular momentum | L_z = hbar (nu/2) n_3 V | Sec. 3 |
| Vortex precession frequency | omega = dE/dL_z | Sec. 3 |

---

## Relevance to Phonon-Exflation

1. **Quasi-ODLRO and the post-transit GGE state**: The paper's central concept -- that broken time translation symmetry exists in quasi-ODLRO systems with tau_Q >> tau_E but not in the strict conservation limit -- maps onto the framework's GGE relic state. The 8 Richardson-Gaudin conserved quantities in the post-transit state play the role of the quasi-conserved Q: they are exact within the integrable sector but would eventually relax if integrability-breaking perturbations were introduced. The tau_Q >> tau_E hierarchy is the integrability-protection mechanism.

2. **Magnon BEC as pair vibrator analog**: The magnon BEC formation sequence (dephasing -> energy relaxation -> coherent precession) is structurally identical to the framework's transit sequence (pre-transit ground state -> sudden quench -> GGE formation). The magnon BEC frequency omega = dE/dS_z parallels the giant pair vibration frequency omega = 0.792 found in Session 37.

3. **Observability requires symmetry violation**: The paper's finding that time-translation-symmetry breaking is observable only when Q is not strictly conserved connects to the framework's claim that the 4D observer cannot directly see the substrate dynamics (integrability-protected). The "veil" is penetrated only through explicit symmetry-breaking channels, analogous to the electromagnetic coupling that makes magnon BEC observable.

4. **Two-species model and Cooper pair dynamics**: Wilczek's two-species model (Q = N_+ - N_-, omega = |mu_+ - mu_-|) maps directly to the Cooper pair system in the framework where pairs carry K_7 charge +/-1/2 and the tunneling frequency is set by the BCS gap.

5. **Vortex decoupling at low temperature**: The experimental observation that the vortex system decouples from the container at low T (choosing its own rotation rate) parallels the integrability-protection of the GGE state, where the post-transit quasiparticle system decouples from the geometric substrate.
