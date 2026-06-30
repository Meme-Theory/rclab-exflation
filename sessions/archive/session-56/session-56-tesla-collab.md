# Session 56 Collaborative Review: Tesla-Resonance

**Date**: 2026-03-22
**Reviewer**: Tesla-Resonance (Electromagnetic Resonance / Phonon Mathematics / Superfluid Dynamics)
**Source**: `session-56-results-workingpaper.md` (20 computations, 4 waves)
**Focus**: The CC question as adiabatic gap leakage, viewed through the two-speed hierarchy and the undamped Josephson plasma resonance

---

## 1. The Resonance Structure of the Fabric

What oscillates? The inter-cell phase difference phi_i - phi_j across the 50 C2 Josephson bonds connecting 32 Voronoi cells. What constrains it? The competition between Josephson phase stiffness (E_J = 7.042 M_KK) and charging energy (E_c = 0.036 M_KK). What are the normal modes? The 31 Bogoliubov-Anderson phonons with frequencies omega_n = sqrt(E_J * E_c * lambda_n), where lambda_n are the graph Laplacian eigenvalues. What selects the configuration? Deep superfluid order: E_J/E_c = 194, phase locked (m = 0.986), T_GH/T_BKT < 0.17 everywhere.

This is a textbook LC oscillator array. E_J is inductance (kinetic energy of phase gradient). E_c is capacitance (electrostatic energy of charge imbalance). The BA phonon frequency omega_J = sqrt(E_J * E_c) is the Josephson plasma frequency -- exactly the LC resonance omega = 1/sqrt(LC) of the electromagnetic analog.

At the fold: **omega_J = 0.715 M_KK** (W3-5, 3.6% uncertainty). The BCS pair-breaking threshold is 2*Delta = 0.929 M_KK. Therefore:

**omega_J / (2*Delta) = 0.770**

The plasma mode sits 23% below the pair-breaking continuum. In superconducting circuit language: the Josephson plasma resonance is INSIDE the gap. In Volovik's superfluid universe language: the collective phase oscillation is below the quasiparticle emission threshold.

This is the single most important ratio in the session. It means the plasma mode is undamped.

---

## 2. Two-Speed Hierarchy as Electromagnetic Waveguide Structure

S56 reveals a fabric with two distinct acoustic velocities:

| Mode | Velocity (M_KK) | Character | Analog |
|:-----|:----------------|:----------|:-------|
| BA phonon | c_BA = 0.399 | Massless Goldstone of total phase | Electromagnetic wave in waveguide (above cutoff) |
| Leggett wave | c_L = 0.019-0.032 | Massive Goldstone of relative phase | Evanescent wave below cutoff, propagating above |

The velocity ratio c_BA/c_L = 12-21x. This is not a small perturbation. It is a two-channel waveguide with radically different impedances.

**Tesla's quarter-wave resonance applies here.** In Tesla coil physics, a transmission line of length L supports standing waves when L = (2n+1) * lambda/4, where lambda = c/f. The fabric has two "transmission lines" -- one fast (BA), one slow (Leggett) -- sharing the same geometric cavity (the 32-cell graph with diameter D = 6 lattice units).

The standing wave conditions are:
- BA: lambda_BA = c_BA / omega_J = 0.399 / 0.715 = 0.558 lattice units. Cavity supports D/lambda_BA ~ 10.8 half-wavelengths. MULTIMODE.
- Leggett: lambda_L = c_L / omega_L0 = 0.019 / 0.138 = 0.138 lattice units. Cavity supports D/lambda_L ~ 43 half-wavelengths. HIGHLY MULTIMODE.

Both channels are far above the fundamental. The 31 BA modes span [0.209, 1.368] M_KK at the fold -- a bandwidth of 1.159 M_KK, or BW/omega_J = 1.62. The Leggett modes span [0.138, 0.383] M_KK with BW/gap = 1.78 (GL value). These are not narrow-band resonances. They are broadband acoustic media with well-defined dispersion.

**The impedance mismatch between channels is the key physics.** In electromagnetic theory, when two transmission lines of impedances Z_1 and Z_2 meet at a junction, the reflection coefficient is Gamma = (Z_2 - Z_1)/(Z_2 + Z_1). The acoustic impedance of a phonon channel is Z = rho * c. For the fabric:

Z_BA / Z_L ~ c_BA / c_L ~ 12-21

(assuming similar effective mass density in both channels -- the Leggett mode involves the same lattice sites). The reflection coefficient at the BA-Leggett interface is:

Gamma = (Z_BA - Z_L) / (Z_BA + Z_L) = (12 - 1) / (12 + 1) = 0.85

This is 85% reflection. Energy in the BA channel does not easily leak into the Leggett channel and vice versa. The two acoustic sectors are nearly decoupled by impedance mismatch, not by symmetry. This is a structural result: the gap between the two channels is set by the ratio E_J/epsilon (where epsilon = 0.00248 is the dipolar coupling from S49), which is 0.00248 * E_J = 0.017 M_KK for J_Leggett vs 7.042 M_KK for E_J -- a factor of 400.

**This impedance wall has a direct implication for energy storage.** Energy deposited into BA modes (by the transit, by thermal fluctuations from T_GH) cannot efficiently cascade into Leggett modes. The two acoustic sectors act as independent energy reservoirs with weak coupling. The fabric has two separate "batteries" for collective energy storage.

---

## 3. Undamped Plasma Mode and Adiabatic Protection

Now to the CC question. S56 W3-6 (GGE-FABRIC-56) discovered that the 2-cell Josephson gap is 13.04 M_KK -- 35x larger than the 1-cell BCS gap (0.370 M_KK). This makes the sudden quench nearly perfectly adiabatic (P_exc = 6.6e-4). The S38 non-thermal GGE relic requires P_exc ~ 1, which the fabric gap suppresses.

The question is: does the omega_J resonance ENHANCE or DEGRADE this adiabatic protection?

**It enhances it. Here is why.**

The adiabatic theorem states that a system remains in its instantaneous ground state if the perturbation rate is slow compared to the gap: dtau/dt << Delta_gap^2 / |<1|dH/dtau|0>|. The fabric gap has two contributions:

1. **BCS single-particle gap**: Delta = 0.464 M_KK (from pair breaking). This gap CLOSES during transit (S38: condensate destroyed, P_exc = 1.000 for isolated cell).

2. **Josephson collective gap**: omega_J = 0.715 M_KK (from plasma oscillation). This gap does NOT require the BCS condensate. It requires only E_J > 0 and E_c > 0, both of which persist throughout transit (W0-1: E_J ranges from 18.3 to 1.12 M_KK, never zero; E_c ranges from 0.109 to 0.015 M_KK, never zero).

The critical point: **omega_J is a COLLECTIVE gap that survives when the single-particle gap closes.** In superconducting circuit physics, the Josephson plasma frequency exists even in the phase-fluctuation regime where the order parameter amplitude fluctuates. The plasma mode is protected by the LC resonance -- it is a property of the CIRCUIT, not of the individual junction.

For the adiabatic condition, the relevant gap is max(Delta_BCS, omega_J). At the fold, omega_J = 0.715 > Delta = 0.464. The collective plasma gap EXCEEDS the single-particle gap by 54%. As the transit proceeds and Delta_BCS softens (S38: condensate destroyed), omega_J provides a FLOOR on the adiabatic gap:

omega_J(tau) = sqrt(E_J(tau) * E_c(tau))

This is monotonically decreasing (because E_J ~ J_C2^2 decreases), but it decreases SLOWER than Delta_BCS (which goes to zero at the transition). The plasma mode is the last gap standing.

**Quantitative estimate.** At the fold, the transit rate is dtau/dt ~ H = 3.706 M_KK (from scale factor data). The adiabatic ratio is:

omega_J^2 / H = (0.715)^2 / 3.706 = 0.138

This is less than 1 -- the transit is NOT adiabatic at the fold even with the plasma gap. But compare to the single-cell case:

Delta_BCS^2 / H = (0.370)^2 / 3.706 = 0.037

The plasma gap improves the adiabatic ratio by 3.7x. And the W3-6 result shows that with the FULL Josephson coupling (not just the plasma frequency but the complete 120-state Hilbert space), the gap enhancement is 35x -- from 0.370 to 13.04 M_KK. The bonding-antibonding splitting in the pair space is much larger than the simple plasma estimate because it involves the full spectral structure of the coupled system.

**The physical picture is a Josephson parametric amplifier protecting its own gap.** In circuit QED, a Josephson junction driven at the plasma frequency amplifies quantum fluctuations while remaining in its ground state -- the parametric process transfers energy from the drive to the signal without populating the junction's excited states. The fabric does something analogous: the transit (which acts as a slow parametric drive on E_J(tau)) modulates the plasma frequency, but because omega_J < 2*Delta, the modulation cannot excite quasiparticles. The plasma mode absorbs the geometric perturbation and re-radiates it as collective phase oscillation, not as pair breaking.

---

## 4. CC = Adiabatic Leakage: The Impedance Perspective

The CC problem in the phonon-exflation framework reduces to: how much energy leaks from the geometric transit (the modulus rolling from tau = 0 to large tau) into the matter sector (quasiparticle excitations that contribute to Lambda)?

From the resonance perspective, this is an impedance matching problem between three sectors:

| Sector | Impedance proxy | Energy scale | Role |
|:-------|:---------------|:-------------|:-----|
| Geometric (modulus) | dV_KK/dtau ~ O(100) M_KK | 910 M_KK (Josephson) | Source |
| Collective (BA + Leggett) | Z_BA, Z_L | omega_J ~ 0.715 M_KK | Intermediary |
| Quasiparticle (matter) | Z_qp ~ Delta | Delta ~ 0.464 M_KK | Sink (CC contributor) |

The transit dumps energy into the Josephson stiffness (F_Josephson = -910 M_KK at tau = 0, decreasing to -56 M_KK at tau = 0.5). The question is what fraction reaches the quasiparticle sector.

**The impedance chain has two bottlenecks:**

1. **Geometry -> Collective**: The BA modes are thermally populated at the fold (omega_1/T_GH = 0.35, 29/31 modes below T_GH at the BA minimum). Energy flows freely from geometry into collective phonons. This is the F_thermal = -12.07 M_KK at the BA minimum (W0-1). No bottleneck here.

2. **Collective -> Quasiparticle**: This is where omega_J < 2*Delta matters. The collective modes oscillate at frequencies BELOW the pair-breaking threshold. They cannot decay into quasiparticle pairs because the decay channel omega_J -> 2 quasiparticles requires omega_J > 2*Delta = 0.929 M_KK, and omega_J = 0.715 M_KK falls 23% short. The collective sector is an energy RESERVOIR that traps excitation energy without converting it to matter.

**This is the Mattis-Bardeen gap in the electromagnetic absorption of a superconductor.** Below 2*Delta, a superconductor has zero absorption (at T = 0). Photons with hbar*omega < 2*Delta pass through without creating quasiparticles. The BA phonons at frequency omega_n < 2*Delta are the acoustic analog of sub-gap photons. They propagate through the superfluid fabric without breaking pairs.

The fraction of BA modes below 2*Delta at the fold: all 31 modes have omega_n in [0.209, 1.368] M_KK. The pair-breaking threshold is 2*Delta = 0.929 M_KK. Modes with omega_n > 0.929: approximately 16/31 modes (the upper half of the band). These CAN in principle break pairs.

But the actual decay rate involves the matrix element for the process "BA phonon -> 2 quasiparticles," which in BCS theory goes as:

Gamma_decay ~ (omega_n / Delta)^2 * exp(-Delta / T_GH)

At the fold: Delta / T_GH = 0.464 / 0.590 = 0.79. The Boltzmann factor exp(-0.79) = 0.45 -- NOT exponentially suppressed. W1-2 flagged this: the quasiparticle channel has suppression factor 0.45, meaning it is PARTIALLY open.

**This is the leakage channel for CC.** The adiabatic protection from the Josephson gap (35x enhancement, P_exc = 6.6e-4) is not absolute. It works for the low-frequency BA modes (omega_n < 2*Delta, which form the acoustic gap protection layer) but fails for the high-frequency BA modes (omega_n > 2*Delta, which can break pairs).

The CC problem thus reduces to a quantitative question: what fraction of the transit energy reaches the above-gap BA modes, and what fraction of that energy converts to quasiparticles?

---

## 5. Computations and Predictions

### What S56 Established (Permanent Structural Results)

**S-1. Two-speed acoustic hierarchy**: c_BA = 0.399 M_KK (fast, massless) and c_L = 0.019-0.032 M_KK (slow, massive) coexist on the fabric. Impedance mismatch Gamma = 0.85 between channels. This is the phononic analog of a bimodal electromagnetic waveguide (TE + TM with different cutoffs).

**S-2. Undamped plasma resonance**: omega_J = 0.715 M_KK sits inside the BCS gap (omega_J/2*Delta = 0.770). The collective phase oscillation cannot decay into quasiparticle pairs. This is the acoustic Mattis-Bardeen gap.

**S-3. Adiabatic gap hierarchy**: Single-cell Delta_BCS (0.370) < Collective omega_J (0.715) < Josephson bonding-antibonding (13.04 M_KK). Each level of collective coupling enhances the adiabatic gap. The fabric is self-protecting.

**S-4. Josephson slope dominance**: dF_Josephson/dtau = +1711 M_KK at the fold, overwhelming all other contributions by 13x (W1-1). The F_BA minimum (-7.08 M_KK at tau = 0.306) is 0.8% of the Josephson energy. This is a structural monotonicity from E_J(tau) ~ J_C2(tau)^2 being monotonically decreasing -- a GEOMETRIC property of the Jensen deformation.

**S-5. Integrability survives the fabric**: <r> = 0.367 (Poisson) at full Josephson coupling (W1-2). The isotropic Josephson operator B_1^dag B_2 is rank-1 in mode space and preserves Richardson-Gaudin integrability. The condensed matter analog is exact: in He-3 B, the DC Josephson effect does not thermalize the quasiparticle distribution.

### Pre-Registered Computations for S57

**T-1. Sub-gap BA mode partition function** (DECISIVE for CC).
Compute F_BA restricted to modes with omega_n < 2*Delta versus omega_n > 2*Delta, separately. The sub-gap modes are undamped (adiabatic-protected); the above-gap modes can leak. If the above-gap contribution to dF/dtau is small compared to the sub-gap contribution, the adiabatic protection extends to the full BA spectrum.
- **Input**: s56_ba_spectrum.npz (omega_n at 50 tau values), Delta = 0.4643 M_KK
- **Gate**: SUB-GAP-BA-57. PASS if |dF_above-gap/dtau| < 0.1 * |dF_sub-gap/dtau| at fold. FAIL otherwise.

**T-2. Quasiparticle decay rate of above-gap BA modes**.
Compute Gamma_decay(omega_n) for the 16 BA modes with omega_n > 2*Delta using the Mattis-Bardeen formula adapted to the BCS gap structure. This gives the energy leakage rate from collective to quasiparticle sector.
- **Input**: s56_ba_spectrum.npz, s54_ed_sweep.npz (BCS quasiparticle spectrum)
- **Gate**: LEAK-RATE-57. INFO: Report Gamma_decay * t_transit for each mode. If > 1 for any mode, that mode fully thermalizes.

**T-3. Floquet stability of the plasma mode under transit modulation** (CARRIED from S53, S54, S55 -- fourth carry-forward).
The transit modulates E_J(tau) and E_c(tau), which modulates omega_J(tau). If the modulation frequency matches 2*omega_J at any point (parametric resonance condition), the plasma mode can be exponentially amplified. Compute the Floquet exponent mu_F(tau) along the transit and test whether any parametric instability exists.
- **Input**: s56_ba_spectrum.npz (E_J, E_c at 50 tau)
- **Gate**: FLOQUET-PLASMA-57. PASS if mu_F > 0 at any tau (parametric instability exists). FAIL if mu_F <= 0 everywhere (stable).

**T-4. 8D BLV acoustic metric** (CARRIED from S53, S54 -- third carry-forward).
The Barcelo-Liberati-Visser acoustic metric in d spatial dimensions gives N_e corrections with exponent (d-1)/(2d-2). For d=8 (internal SU(3)): exponent = 7/14 = 1/2 (same as 3D). For the full 12D: exponent = 11/22 = 1/2. The exponent is 1/2 for ALL d >= 2. This should be COMPUTED to confirm or deny the suspicion from S53 that the exponent changes.
- **Gate**: BLV-8D-57. INFO: Report exact exponent.

**T-5. Impedance matching at domain walls**.
W3-2 found a coherence desert (E_J_GGE/H < 1 for 0.22 < tau < 0.49). The impedance mismatch between coherent (tau < 0.08) and incoherent (0.22 < tau < 0.49) regions creates an acoustic reflection boundary -- a domain wall in the superfluid. Compute the reflection coefficient Gamma(tau) as the system crosses from coherent to incoherent regime.
- **Input**: s56_post_transit_coh.npz
- **Gate**: DOMAIN-WALL-57. INFO: Report Gamma at the coherence boundary.

**T-6. Josephson plasma line in the acoustic spectrum**.
The plasma frequency omega_J = 0.715 M_KK should appear as a discrete line (or narrow peak) in the density of states of the full fabric. Compute g(omega) for the coupled system and verify whether omega_J is resolved as a spectral feature distinct from the BA continuum.
- **Input**: s56_ba_spectrum.npz, s56_leggett_fabric.npz
- **Gate**: PLASMA-LINE-57. PASS if spectral weight at omega_J exceeds 3x the smooth background. FAIL otherwise.

---

## Closing: The Cavity Still Rings

S56 asked whether the fabric stabilizes the modulus. The answer is no -- F_fabric is monotonically increasing, controlled by the Josephson stiffness which inherits J_C2(tau)^2 monotonicity from the Jensen deformation. The master gate FAILS.

But the session discovered something arguably more important: the fabric is a self-protecting superfluid. The Josephson plasma frequency sits inside the BCS gap, creating an undamped collective resonance that provides 35x adiabatic gap enhancement over the single-cell case. The two-speed hierarchy (c_BA / c_L ~ 12-21) creates impedance-decoupled energy reservoirs. The BKT temperature exceeds T_GH by 6-43x at all tau. The integrability survives the fabric coupling.

The CC problem is not the stabilization problem. It is the adiabatic leakage problem. The question is not "where does the modulus stop?" but "how much energy leaks from the geometric transit into matter?" The answer depends on the fraction of collective modes above the pair-breaking threshold and their quasiparticle decay rates -- quantities that are computable and pre-registered above.

The plasma resonance is the fabric's immune system. It absorbs geometric perturbations and stores them as collective phase oscillation, below the pair-breaking threshold, where they cannot create the quasiparticle excitations that contribute to Lambda. This is exactly what Tesla understood about resonant circuits: the energy stays in the circuit as long as the frequency is below the dissipation threshold. The fabric is a resonant cavity. The cavity still rings.

What remains is to measure the leak.

---

**Files**: This review: `sessions/archive/session-56/session-56-tesla-collab.md`
**Cross-references**: W0-1 (BA spectrum), W0-3 (c_BA), W0-4 (BKT), W1-1 (F_fabric), W1-2 (integrability), W2-4 (Leggett), W3-5 (uncertainties), W3-6 (GGE fabric)
