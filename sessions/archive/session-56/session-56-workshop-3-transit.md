# Session 56 Workshop 3: The Transit Microscope
## Naz × QA — What excitations survive the finite-rate transit?

**Date**: 2026-03-22
**Format**: 2-agent iterative workshop (2-3 rounds)
**Agents**: Naz (nazarewicz-nuclear-structure-theorist), QA (quantum-acoustics-theorist)
**Team source collabs** (ALL must be read by both agents):
- `sessions/archive/session-56/session-56-naz-collab.md`
- `sessions/archive/session-56/session-56-qa-collab.md`
- `sessions/archive/session-56/session-56-dirac-collab.md`
- `sessions/archive/session-56/session-56-foam-collab.md`
- `sessions/archive/session-56/session-56-connes-collab.md`
- `sessions/archive/session-56/session-56-cw-collab.md`

**Central question**: The single-cell transit gives P_exc = 1.000 (complete excitation). The 2-cell fabric at equilibrium gives P_exc = 6.6e-4 (adiabatic). The PHYSICAL transit is neither — it's a finite-rate sweep through a partially coherent array during the coherence desert. What excitations actually survive? Naz says nuclear fission dissipation. QA says Leggett excitation (P_LZ ~ 0.996). Both must confront Foam's three incompatible demands and Dirac's CPT constraint.

---

## Round 1 -- Naz: Opening Synthesis

### N1. Synthesis of All 6 Team Reviews

Six reviewers examined 20 computations from six distinct disciplinary angles. The master gate FABRIC-FREE-ENERGY-56 is a clean FAIL: F_fabric is monotonically increasing, with the Josephson stiffness slope (+1711 M_KK at the fold) overwhelming the combined non-monotonic contributions from F_cells (-32) and F_BA (-131) by a factor of 13. Every reviewer concurs on this verdict and its structural character.

The convergence across disciplines is itself informative. Let me organize what each perspective uniquely contributes to the transit question.

**Nuclear structure (my review)**: The transit is a large-amplitude collective motion of the internal geometry. The 1378 diabatic level crossings (S54 Massey data, xi_med = 1.6e-6) are the microscopic mechanism for quasiparticle production. The N_pair blocking trend (<r> = 0.707, 0.509, 0.414 for N = 1, 2, 3) shows that single-cell integrability breaking is permanently closed at all filling fractions. The Josephson-Coulomb analogy (R = 0.051 on fabric vs 0.711 single-cell) places the framework in the superheavy limit where smooth backgrounds dominate shell corrections by 20x.

**Quantum acoustics (QA review)**: The two-speed hierarchy is the session's most important structural discovery. The BA phonon velocity c_BA = 0.399 M_KK at the fold propagates phase information across the fabric. The Leggett mode propagates relative B2/B1 amplitude information at c_L = 0.019-0.032 M_KK -- 12-21x slower. This separation implies a two-adiabaticity hierarchy: the Josephson channel (gap 13.04 M_KK) is adiabatically protected while the Leggett channel (gap 0.070-0.138 M_KK) has estimated P_LZ ~ 0.996 -- essentially complete non-adiabatic excitation. QA's self-critical admission that the session design underestimated the Josephson stiffness by an order of magnitude is honest and instructive: the F_BA minimum at -7.08 M_KK is 0.8% of the Josephson background.

**CPT/antimatter (Dirac review)**: Every excitation channel is CPT-symmetric. The fabric Hamiltonian commutes with J (eq. 7 in Dirac's review), the transit operator commutes with J (eq. 9), and the Landau-Zener probability satisfies |P_exc^{(p,q)} - P_exc^{(q,p)}| = 0 exactly. This is structural (T11, permanent). The baryogenesis closure is reinforced at fabric level: no internal J-breaking can produce matter-antimatter asymmetric leakage. The constraint is not restrictive for the CC problem -- it says whatever P_exc we compute, it applies equally to both sectors.

**Quantum foam (Foam review)**: Three incompatible demands on one parameter (W-FOAM-10, SUPPRESSION-EXCITATION DUALITY). Large E_J maintains superfluid coherence needed for consistent 4D physics but exponentially suppresses quasiparticle excitation needed for CC. Small E_J permits excitation but destroys coherence. The product P_exc * <cos(phi)> is bounded. This is the fabric analog of Carlip's inflation/CC incompatibility (S53). Foam also computes the specific N_eff ~ 12.7 cells needed to match Lambda_obs via the CC ~ exp(-Delta * N / T) formula -- a pre-registerable target if the finite-rate transit can be computed.

**NCG (Connes review)**: The Josephson coupling IS single-cell spectral geometry projected onto inter-cell bonds. E_J ~ J_C2(tau)^2, which inherits the Lie derivative monotonicity theorem. The fabric Dirac operator D_fabric = D_K tensor 1 + 1 tensor D_Gamma has a well-defined spectral action that includes Josephson physics through the cross term -- but this inclusion WORSENS monotonicity. The surviving NCG route is anisotropic inner fluctuations (not central in the pairing algebra), which would break integrability. Connes also notes the order-one condition remains at 4.000 unchanged at fabric scale.

**Cosmic web (CW review)**: Every element of the cosmic web contains ~10^{56-58} KZ cells. The thermodynamic limit kills any spatial CC variation: delta(CC)/CC ~ 10^{-27} between cluster and void. ALPHA-ENV-43 reinforced as CLOSED. The BKT coherence length (~ 10 * xi_KZ ~ 10^{-25} Mpc) does not bridge to cosmological scales. CW identifies the "incoherent desert" (0.22 < tau < 0.49, where E_J_GGE/H < 1) as the sole mechanism that could produce isolated-cell physics despite the fabric gap. The three-phase chronology (coherent -> desert -> recoherent) is the CW-testable prediction if the transit can be computed.

**The consensus**: Static partition function routes are exhausted (47+ closures). The surviving physics is dynamic: finite-rate transit, selective non-adiabaticity, and the interplay between the incoherent desert and the gap hierarchy.

### N2. The Nuclear Fission Dissipation Analog (Expanded)

I now develop the nuclear fission dissipation analog in light of all six reviews, because it provides the quantitative framework for the finite-rate transit computation.

**The setup.** A heavy nucleus undergoing fission is the closest physical analog to the fabric transit. The nucleus (= fabric pre-transit) is a finite quantum system in a BCS-paired ground state. The fission pathway (= Jensen deformation) is a large-amplitude collective motion parameterized by the elongation coordinate Q (= tau). The question is: how much excitation energy is deposited in the fission fragments (= post-transit cells)?

**The three dissipation regimes in nuclear fission:**

(1) *Slow (adiabatic) fission.* The collective velocity dQ/dt is small compared to all quasiparticle excitation gaps. The nucleus follows the adiabatic potential energy surface. Zero quasiparticle excitation. Cold fragments. This is the W3-6 regime on the fabric: P_exc = 6.6e-4.

(2) *Fast (diabatic) fission.* dQ/dt exceeds the smallest gaps. Level crossings are traversed diabatically -- the system does NOT follow the adiabatic path. Quasiparticles are produced at each crossing. Hot fragments. This is the S38 single-cell regime: P_exc = 1.000, 59 quasiparticle pairs.

(3) *Intermediate (partially dissipative) fission.* dQ/dt is comparable to some gaps but smaller than others. SELECTIVE excitation: some channels are diabatic, others adiabatic. The excitation pattern depends on the gap hierarchy.

The fabric transit is in regime (3). Here is why.

**The gap hierarchy on the fabric has three distinct scales:**

| Channel | Gap (M_KK) | Nature | P_LZ estimate |
|:--------|:-----------|:-------|:--------------|
| Josephson bonding | 13.04 | Overall phase, 2-cell | ~6.6e-4 (adiabatic) |
| Single-cell BCS | 0.370 | Intra-cell quasiparticle | ~1.000 (diabatic, S38) |
| Leggett relative | 0.070-0.138 | B2/B1 relative phase | ~0.996 (QA estimate) |

The Josephson gap is 35x larger than the BCS gap, which is 3-5x larger than the Leggett gap. The transit velocity (set by H ~ 3.7 M_KK at the fold) is:
- Much smaller than the Josephson gap: 3.7/13.04 = 0.28. Adiabatic.
- Comparable to the BCS gap: 3.7/0.370 = 10. Diabatic -- confirmed by 1378 diabatic crossings at xi ~ 10^{-6}.
- Much larger than the Leggett gap: 3.7/0.1 = 37. Strongly diabatic.

This is precisely the intermediate regime. The overall superfluid phase follows adiabatically (Josephson gap protects it). The intra-cell quasiparticle spectrum does NOT follow adiabatically (BCS gap is too small). The relative B2/B1 structure is maximally excited (Leggett gap is smallest).

**What nuclear fission teaches us about this regime:**

In nuclear physics, the intermediate regime is computed using the time-dependent Hartree-Fock-Bogoliubov (TDHFB) formalism. The collective path is parameterized by the generator coordinate Q, and the quasiparticle excitation is computed from the non-adiabatic coupling:

    <qp_n(Q) | d/dQ | 0(Q)> = V_{n0} / (E_n - E_0)

where V_{n0} is the matrix element of the cranking operator and E_n - E_0 is the excitation gap. The transition probability at each level crossing is the Landau-Zener formula:

    P_LZ = exp(-2*pi*gamma), gamma = |V_{12}|^2 / (hbar * |dE/dQ| * dQ/dt)

The CUMULATIVE excitation over the full fission path is:

    E_exc = Sum_crossings P_LZ(i) * delta_E(i)

In nuclear fission of actinides (^236U -> ^140Xe + ^94Sr), there are typically 10-50 level crossings along the fission path, producing 10-20 MeV of quasiparticle excitation energy (about 5% of the total kinetic energy release). The fragment excitation energy determines the neutron multiplicity (nu_bar = 2-3 for thermal fission).

For the framework, the S54 Massey calculation found 1378 level crossings along the Jensen path from tau = 0 to the fold. All were diabatic (xi_med = 1.6e-6). This was for the SINGLE-CELL spectrum. On the fabric, the relevant crossings are:

(a) Intra-cell crossings: Still 1378 per cell, still diabatic. The Josephson coupling does not modify the intra-cell spectrum significantly (it acts on inter-cell phase, not intra-cell levels).

(b) Inter-cell crossings: The TB spectrum has its own crossings as tau varies. These are the new physics. The TB eigenvalues (32 per tau value) undergo avoided crossings whose gaps are set by the Josephson coupling J_C2. These crossings have larger gaps (order J_C2 ~ 1 M_KK) and may be adiabatic or intermediate.

(c) Leggett-channel crossings: The relative B2/B1 amplitude, when viewed as a time-dependent order parameter during transit, sweeps through the Leggett gap. QA estimates P_LZ ~ 0.996 from pi * omega_L0^2 / (2 * d(omega_L0)/dt) = 0.004. This is a single effective crossing with near-complete excitation.

**The critical confrontation with Foam's W-FOAM-10.** Foam identifies the suppression-excitation duality: the same E_J that maintains coherence also suppresses excitation. The nuclear analog is precise. In nuclear fission, the pairing gap Delta ~ 1 MeV suppresses quasiparticle excitation at each individual crossing (larger Delta means fewer quasiparticles per crossing). But the COLLECTIVE coordinate still moves (the nucleus still fissions). The total excitation depends on the PRODUCT of the number of crossings times the per-crossing excitation. A large gap suppresses per-crossing excitation but does not prevent the collective motion.

In the fabric: the Josephson gap suppresses OVERALL phase excitation (channel a above remains adiabatic). But the Leggett gap does NOT suppress relative-phase excitation (channel c is strongly diabatic). And the intra-cell BCS crossings (channel a, 1378 per cell) remain diabatic regardless of the Josephson coupling, because they involve intra-cell levels that the inter-cell coupling does not protect.

Foam's three incompatible demands (coherence + excitation + stabilization on one parameter E_J) are partially resolved by recognizing that E_J controls the OVERALL phase gap, not the Leggett or intra-cell gaps. The demands are incompatible only if one requires ALL channels to be simultaneously excited. Selective excitation -- adiabatic overall phase, diabatic intra-cell and Leggett -- escapes the trilemma.

**Dirac's CPT constraint applies uniformly.** Whatever P_LZ we compute for each channel, it is CPT-symmetric: P_LZ^{(p,q)} = P_LZ^{(q,p)} exactly. This does not restrict the excitation magnitude, only its matter-antimatter symmetry. The CC is a J-even quantity (Dirac eq. 10). This is consistent with the nuclear analog: fission fragment excitation energy is charge-conjugation symmetric (nu_bar is the same for ^140Xe and ^94Sr's conjugate, up to Coulomb corrections).

### N3. What Excitations Survive -- The Inventory

I catalog every excitation channel identified across all six reviews, with estimated rates and suppression factors. The classification follows nuclear reaction theory: each channel has a threshold energy, a coupling matrix element, a barrier penetration factor, and a selection rule.

| # | Channel | Gap (M_KK) | Coupling | P_LZ or rate | Status | Source |
|:--|:--------|:-----------|:---------|:-------------|:-------|:-------|
| 1 | Josephson phase (overall U(1)) | 13.04 | E_J = 7.04 per bond | 6.6e-4 (adiabatic) | CLOSED | W3-6 |
| 2 | Intra-cell BCS quasiparticles | 0.370 | V_kk' ~ 0.1 | ~1.000 (diabatic) | OPEN | S38 + S54 Massey |
| 3 | Leggett relative phase (B2/B1) | 0.070-0.138 | epsilon = 0.00248 | ~0.996 (QA est.) | OPEN, UNCOMPUTED | QA Sec. 3 |
| 4 | Anisotropic qp tunneling | Delta/T_GH ~ 0.79 | exp(-0.79) = 0.45 | <r> = 0.446 (near GOE) | OPEN, UNCOMPUTED | W1-2 |
| 5 | BA phonon thermal | omega_1 = 0.209 | T_GH = 0.590 | 7/31 modes populated | INFO (subdominant) | W0-1 |
| 6 | BA phonon non-adiabatic | omega_1 = 0.209 | H/omega_1 = 17.7 | H >> omega_1 at fold | OPEN, UNCOMPUTED | Foam Esc. 1 |
| 7 | Topology change (tau = 0.449) | ~0.003 | Level quasi-crossing | Unknown | OPEN, possibly artifact | W0-3, QA Sec. 4 |
| 8 | Domain wall formation | T_BKT - T_GH ~ 5.5 | KZ defect density | Unknown during transit | OPEN, UNCOMPUTED | CW Sec. 4, Foam Sec. 5 |

**Suppression hierarchy:**

Channel 1 is definitively closed. The Josephson gap is too large for the transit to excite.

Channels 2-3 are the primary open channels. They have complementary character:
- Channel 2 (intra-cell BCS) was the S38 mechanism (P_exc = 1.000, 59.8 pairs). It operates on individual cells. On the fabric, it survives if the cell is effectively isolated during transit.
- Channel 3 (Leggett) is new to S56. It operates between cells. It is the lowest-gap collective mode.
- Channel 4 (anisotropic tunneling) breaks integrability partially. Suppression factor 0.45 -- not exponential.

Channels 5-8 are secondary. Channel 5 is thermal equilibrium (already captured in F_BA). Channel 6 is the acoustic non-adiabaticity Foam identifies: H/omega_1 = 17.7 at the fold, so the transit is fast compared to the lowest BA mode. Channel 7 is potentially an artifact. Channel 8 is the CW three-phase chronology -- whether the incoherent desert (E_J_GGE/H < 1 for 0.22 < tau < 0.49) creates effective domain walls.

**The key nuclear insight**: In nuclear fission, the total fragment excitation is dominated by the SLOWEST channel -- the last level crossings before scission, where the neck is thin and the coupling is weakest. Analogously, the fabric excitation will be dominated by the channel with the SMALLEST gap relative to the transit velocity. This is the Leggett channel (gap 0.07-0.14 M_KK vs transit velocity H = 3.7 M_KK: ratio 0.02-0.04).

**What energy does Leggett excitation carry?** QA estimates 31 Leggett modes at full excitation carry S_L ~ 31 * ln(2) ~ 21 nats of entropy. The energy is E_L ~ 31 * omega_L0/2 ~ 31 * 0.1/2 ~ 1.6 M_KK for zero-point, plus thermal. This is small compared to the Josephson background (347 M_KK) -- about 0.5%. But the ENTROPY is not small. Whether this entropy produces an effective free energy contribution that can compete with the Josephson slope is the question for LEGGETT-ENTROPY-57 (QA's pre-registered computation 4).

### N4. Questions for QA

**Q1 (Leggett P_LZ rigor).** Your estimate P_LZ ~ 0.996 uses the adiabaticity parameter pi * omega_L0^2 / (2 * d(omega_L0)/dt) = 0.004. Two concerns:

(a) What is d(omega_L0)/dt? You write d/dt ~ H ~ 3.7 M_KK. But the Leggett gap omega_L0 = sqrt(2 * epsilon * E_J * Delta_B2 * Delta_B1 / (Delta_B2 + Delta_B1)) depends on E_J(tau) through J_C2^2 AND on the gap ratio through epsilon. Does d(omega_L0)/dtau have the same sign as dE_J/dtau throughout transit, or does the gap ratio epsilon introduce a non-monotonic correction? If omega_L0 has a minimum at some tau_*, the Landau-Zener formula applies at tau_* and the adiabaticity parameter could be much larger (closer to adiabatic) than your estimate.

(b) The 31 Leggett modes have different graph-momenta (lambda_n). The highest-momentum modes have c_L_asymp = 0.104 M_KK (5.4x faster than Fiedler group velocity). Does the Landau-Zener calculation apply independently to each mode, or is there collective enhancement (as in superradiant decay)? In nuclear physics, coherent particle-hole excitations across a deformed potential produce GIANT resonances -- collective states that carry enhanced transition strength. Could the 31 Leggett modes undergo collective excitation rather than independent Landau-Zener transitions?

**Q2 (Two-speed hierarchy and fission analogy).** Your two-adiabaticity hierarchy (Josephson adiabatic, Leggett diabatic) maps beautifully onto nuclear fission. In fission, the slow channel is the center-of-mass motion of the fragments (adiabatic -- the fragments separate smoothly) while the fast channel is the quasiparticle excitation in the neck region (diabatic -- the neck ruptures suddenly). The fabric analog:
- Slow = overall phase (Josephson, adiabatic)
- Fast = relative B2/B1 phase (Leggett, diabatic)

My question: in nuclear fission, the neck rupture produces a BURST of quasiparticles at a specific point along the collective path (the scission point). Is there an analog "scission point" for the Leggett channel -- a specific tau value where the Leggett excitation concentrates? Or is it distributed along the transit?

**Q3 (Design error retrospective).** You identify three design errors in your self-assessment. The most important is underestimating the Josephson stiffness. I want to push this further: given that E_J = 7.042 M_KK was known from S55, and the graph has 50 bonds, F_Josephson ~ 350 M_KK was computable before S56 began. Should S56 have been designed around the Leggett channel from the start, rather than around the BA phonon stabilization? In nuclear physics, we learned decades ago that the mean-field energy surface is dominated by the smooth (LDM) contribution, and shell effects are corrections. The Strutinsky procedure was designed to EXTRACT the correction, not to discover it. Should the S57 plan adopt a Strutinsky-like approach: compute the smooth (Josephson) background first, subtract it, and study the residual?

**Q4 (Foam's trilemma escape).** Foam identifies W-FOAM-10: P_exc * <cos(phi)> is bounded. But my N2 analysis suggests the trilemma is partially resolved by channel selectivity. Do you agree that the Leggett excitation (channel 3) provides entropy without destroying overall phase coherence? If so, is W-FOAM-10 too strong -- should it be reformulated as a constraint on the JOSEPHSON channel only, with the Leggett channel as an independent degree of freedom?

### N5. The Finite-Rate Transit Computation -- Specification

**FINITE-RATE-TRANSIT-57**: The decisive S57 computation, incorporating all six perspectives.

**Physical setup.** The fabric is a 2-cell (or N-cell) Josephson array. Each cell has 8 BCS-active modes with single-particle energies epsilon_k(tau) from the Jensen-deformed SU(3) Dirac spectrum. Inter-cell coupling is H_J = -(E_J/2) * (B_1^dag B_2 + h.c.). The collective coordinate tau sweeps from tau_i to tau_f at rate dtau/dt determined by the Friedmann equation: dtau/dt = H(tau) / M_KK (from S54 scale factor data).

**Method: Time-dependent BdG on the fabric.** This is the nuclear TDHFB adapted to the framework. The state vector |Psi(t)> evolves under the time-dependent Hamiltonian H(tau(t)):

    i * d|Psi>/dt = H(tau(t)) * |Psi>

with H = H_BCS^{(1)} + H_BCS^{(2)} + H_J(tau), and initial condition |Psi(0)> = |GS(tau_i)>.

For the 2-cell system at N_pair = 1: dim = C(16,2) = 120. The Hamiltonian is 120x120. Time evolution is numerically exact via fourth-order Runge-Kutta with adaptive step size.

**Input data:**
- Single-particle energies: s54_tb_hamiltonian.npz (50 tau, 32 eigenvalues)
- Pairing matrix: s54_ed_sweep.npz (V_kl at each tau)
- Scale factor: s54_scale_factor.npz (H(tau) at 10 points, interpolated)
- Josephson coupling: E_J(tau) from canonical_constants + F_anom(tau)
- Leggett parameters: epsilon = 0.00248 (S49), omega_L0(tau) from W2-4 data

**Output observables (at each tau along the transit):**
1. P_exc(tau) = 1 - |<GS(tau)|Psi(tau)>|^2. Total excitation probability.
2. E_exc(tau) = <Psi|H(tau)|Psi> - E_GS(tau). Excitation energy.
3. S_DE(tau) = -Sum |c_n|^2 ln|c_n|^2. Diagonal ensemble entropy.
4. Channel decomposition: project P_exc onto (a) Josephson channel (bonding/antibonding), (b) intra-cell BCS quasiparticles, (c) Leggett (relative phase) channel.
5. n_k(tau) for each mode: track occupation evolution.
6. delta_P_vac = P_vac(fabric, t_final) - P_vac(ground state). The CC contribution.

**Pre-registered gate:**
- **PASS**: P_exc(tau_final) > 0.1 at physical transit rate. Sufficient excitation to produce non-trivial GGE.
- **FAIL**: P_exc(tau_final) < 0.01 at physical transit rate. Adiabatic protection survives.
- **INFO**: 0.01 < P_exc < 0.1. Partial excitation, channel decomposition becomes decisive.

**Complementary sub-computations:**

(a) LEGGETT-LZ-57: Landau-Zener across the Leggett gap specifically. Compute omega_L0(tau) from the W2-4 formula at each tau in the transit. Apply the LZ formula at each local minimum of omega_L0(tau). Compare to the full time-dependent result. This tests whether the Leggett channel is well-described by independent LZ transitions (nuclear crossing model) or requires collective treatment (giant resonance model). Gate: P_LZ^Leggett > 0.5 at physical rate.

(b) CHANNEL-DECOMP-57: At the end of the transit, decompose the final state into Josephson, BCS, and Leggett components. The decomposition uses projection operators: P_J projects onto bonding/antibonding Josephson states, P_BCS projects onto intra-cell quasiparticle excitations, P_L projects onto Leggett-mode excitations. The energy and entropy in each channel determine which mechanism (if any) produces the CC contribution.

(c) RATE-SCAN-57: Scan the transit rate from 0.01 * H_physical to 100 * H_physical. Map P_exc vs rate. Identify the critical rate where P_exc transitions from adiabatic (< 0.01) to diabatic (> 0.1). Compare this critical rate to H(tau) at each point in the transit. If H(tau) > H_critical for any tau in [0.10, 0.40], excitation is guaranteed at that point.

**CPT constraint (from Dirac):** The computation must verify [J, U(t_f, t_i)] = 0 at each time step. By eq. 9 of Dirac's review, this is guaranteed algebraically, but numerical verification provides a cross-check on the time-evolution algorithm. If ||JU - UJ|| > 10^{-10} at any step, the integrator has introduced symmetry-breaking errors.

**Foam constraint (W-FOAM-10 test):** Compute P_exc and <cos(phi)> simultaneously. If P_exc * <cos(phi)> exceeds the Foam bound at any tau, the selective-excitation escape from the trilemma is quantitatively confirmed.

**CW constraint (incoherent desert test):** Track E_J_GGE(tau)/H(tau) during the evolution. If this ratio drops below 1 in the interval [0.22, 0.49] (the coherence desert from W3-2), the cells effectively decouple. The time-dependent computation should show enhanced excitation in this window, confirming the three-phase chronology.

**Nuclear benchmarks:** The computation should reproduce the following limiting cases:
1. dtau/dt -> 0 (adiabatic limit): P_exc -> 0. Matches W3-6.
2. dtau/dt -> infinity (sudden quench): P_exc -> P_exc^{sudden} = 6.6e-4 for 2-cell. Matches W3-6.
3. E_J -> 0 (isolated cells): P_exc -> 1.000 for each cell. Matches S38.
4. Leggett gap -> 0: P_exc^Leggett -> 1.000 (complete Leggett excitation).

**Estimated compute requirements:** The 120x120 Hamiltonian diagonalization at ~1000 time steps (adaptive RK4 with dt ~ 0.01/H): ~120,000 matrix operations. At ~10 microseconds per 120x120 diag on CPU: ~1.2 seconds total. Memory: negligible. The computation is CPU-cheap; the physics is the hard part.

**What this computation decides:** If PASS (P_exc > 0.1), the Leggett + intra-cell excitation channels provide enough entropy and energy to produce a non-trivial post-transit state, potentially with modified P_vac. The CC mechanism (non-thermal relic from transit excitations) survives at the fabric level. If FAIL (P_exc < 0.01), adiabatic protection persists even at finite rate, and the GGE relic mechanism is closed on the fabric. The framework would then need either the off-Jensen deformation space (to find non-monotonic E_J) or an entirely different CC mechanism.

This is the decisive computation for S57. It is computationally cheap, physically well-motivated by the nuclear fission analog, and pre-registered with clear pass/fail criteria that all six reviewers can evaluate against their domain expertise.

---

## Round 1 -- QA: Response & Cross-Synthesis

### Part 1: Response to Naz's Sections (N1-N5)

**Re: N1 (Synthesis).** The six-reviewer synthesis is accurate and well-organized. One refinement: Naz writes that Connes identifies "anisotropic inner fluctuations (not central in the pairing algebra)" as the surviving NCG route. This is structurally identical to the quasiparticle tunneling channel I flagged in my collab (Section 4, channel 2) and that Naz catalogs as channel 4 in N3. The NCG language (non-central inner fluctuation) and the condensed-matter language (anisotropic quasiparticle tunneling) and the nuclear language (Andreev reflection vs supercurrent) all name the same mathematical object: a mode-dependent inter-cell coupling H_qp = Sum_k t_k c_k^{(1)dag} c_k^{(2)} + h.c. that breaks Richardson-Gaudin integrability because the coupling constants {t_k} are not proportional to the identity in mode space. This three-domain convergence on a single object is structural, not coincidental. The surviving constraint surface is low-dimensional: the Leggett channel and the anisotropic tunneling channel are the two independent degrees of freedom that the six reviews collectively identify.

**Re: N2 (Fission analog).** The nuclear fission dissipation mapping is the sharpest physical analog we have for the transit, and Naz's development of the three regimes is correct. I want to sharpen one point. Naz writes that "intra-cell crossings are still 1378 per cell, still diabatic. The Josephson coupling does not modify the intra-cell spectrum significantly." This is correct at leading order: E_J acts on the inter-cell phase, not on intra-cell levels. But there is a second-order correction. The Josephson coupling shifts the effective on-site Hamiltonian by delta_H ~ E_J^2 / (2 * Delta_charge), where Delta_charge is the charging energy gap. At E_J = 7.042 and E_c = 0.036, delta_H ~ 49 / 0.07 ~ 700 M_KK. This is enormous -- it renormalizes the ground state energy but is a constant shift (independent of the quasiparticle configuration), so it does NOT modify the intra-cell level crossings. The crossings are between quasiparticle states, which differ by O(Delta_BCS) = 0.37 M_KK; the Josephson renormalization is a rigid shift of the entire ladder. The 1378 diabatic crossings survive on the fabric. This is worth verifying explicitly in the FINITE-RATE-TRANSIT-57 computation by comparing intra-cell Massey parameters with and without H_J.

**Re: N3 (Excitation inventory).** The eight-channel catalog is comprehensive. I have two additions.

First, channel 3 (Leggett relative phase) and channel 6 (BA phonon non-adiabatic) are not independent. The BA phonon is the massless Goldstone of the overall U(1); the Leggett mode is the massive pseudo-Goldstone of the relative U(1). They couple through the epsilon parameter (S49: epsilon = 0.00248). During transit, a non-adiabatic excitation of the BA modes can PUMP the Leggett modes through the epsilon coupling. The rate is parametrically small (O(epsilon^2) ~ 6e-6 per scattering event), but the BA mode has 14.3 thermal quanta at the fold and the transit traverses 1378 crossings. The cumulative BA-to-Leggett transfer could be O(1) if the resonance condition omega_BA(k) = omega_L(k') is met for any mode pair. From the dispersion data: the lowest BA mode has omega_1 = 0.209 M_KK, while the Leggett band spans [0.070, 0.474] M_KK. The BA band spans [0.209, 1.368] M_KK. The overlap region [0.209, 0.474] contains 17 Leggett modes and 5 BA modes. This inter-channel resonance has not been computed. It should be a sub-computation of FINITE-RATE-TRANSIT-57: track the energy flow between BA and Leggett sectors during the time evolution.

Second, Naz's "key nuclear insight" that fragment excitation is dominated by the SLOWEST channel is precisely the argument for why the Leggett channel is decisive. But I want to add the acoustic corollary: in the two-speed hierarchy, the Leggett mode is the "neck" of the fission. The BA phonon (fast, c_BA = 0.399) is the fragment center-of-mass motion -- it follows the collective path adiabatically. The Leggett mode (slow, c_L = 0.019-0.032) is the neck -- the thin connection between the two condensate components that ruptures during transit. The "scission point" (Naz's Q2) occurs where the Leggett gap is smallest relative to the transit velocity, which I address in Q2 below.

**Re: N4 (Questions).** Answered in Part 2.

**Re: N5 (Finite-rate transit spec).** The specification is well-designed and I endorse it with three modifications.

Modification 1: Naz's benchmark case 2 ("dtau/dt -> infinity: P_exc -> P_exc^{sudden} = 6.6e-4 for 2-cell") requires clarification. The sudden-quench limit of a FABRIC system is NOT the same as the W3-6 GGE result. W3-6 computed the overlap of the 2-cell ground state at tau_i with the ground state at tau_f: |<GS(tau_f)|GS(tau_i)>|^2 = 1 - 6.6e-4. In the sudden limit of the time-dependent computation, the system stays in the initial state |GS(tau_i)> (because there is no time for evolution), and then we project onto the eigenstates at tau_f. This gives P_exc = 1 - |<GS(tau_f)|GS(tau_i)>|^2 = 6.6e-4 for the 2-cell Josephson ground state. So the benchmark is correct, but it must be understood as the ground-state overlap at the two endpoints, not as a time-evolution result. The time-dependent computation at dt -> infinity reproduces this only if the initial state is the tau_i ground state and the final projection is at tau_f.

Modification 2: The channel decomposition (sub-computation b) needs explicit projectors. I propose: P_J projects onto states where the 2-cell pair number is even (bonding sector, Josephson-protected), P_BCS projects onto states where intra-cell quasiparticle number differs from the ground state, and P_L projects onto states where the relative B2/B1 amplitude differs from the ground-state ratio. These three projectors are not orthogonal (a state can have both BCS and Leggett excitation), so the channel decomposition should report both the individual projections and the overlap matrix <P_i P_j>.

Modification 3: The CPT constraint check (||JU - UJ|| > 10^{-10}) is a good numerical diagnostic, but the relevant symmetry for the Leggett channel is not CPT alone. The Leggett mode breaks the relative U(1) between B2 and B1 sectors. The transit operator should also be tested against the individual sector number operators N_B2 and N_B1: track <N_B2(t)> and <N_B1(t)> independently, not just their sum. If the Leggett channel is excited, <N_B2 - N_B1> will deviate from its ground-state value during transit.

### Part 2: Answers to Naz's Questions (Q1-Q4)

**Q1 (Leggett P_LZ rigor).**

(a) The tau-dependence of omega_L0. The Leggett gap formula is:

    omega_L0(tau) = sqrt(2 * epsilon * E_J(tau) * Delta_B2(tau) * Delta_B1(tau) / (Delta_B2(tau) + Delta_B1(tau)))

This has three tau-dependent factors: E_J(tau) ~ J_C2(tau)^2 * F_anom(tau), Delta_B2(tau), and Delta_B1(tau). The E_J factor decreases monotonically (J_C2 monotone, F_anom nearly constant per S55). The BCS gaps Delta_B2 and Delta_B1 are non-monotonic: they peak near the fold (where the DOS is highest, enhancing pairing) and decrease on either side. The product E_J * Delta_eff therefore has competing monotonic (E_J down) and non-monotonic (Delta_eff peaked) contributions.

Naz asks whether omega_L0 has a minimum at some tau_*, which would increase the adiabaticity parameter. The answer: YES, omega_L0 likely has a minimum. At small tau, E_J is large but Delta is small (low DOS suppresses pairing). At large tau, Delta is small again (DOS drops past the fold). Near the fold, Delta is maximal but E_J is moderate. The product E_J * Delta should peak somewhere between tau = 0 and the fold (where E_J is still large and Delta is growing), then decrease. omega_L0 = sqrt(product) follows the same pattern: it rises, peaks, then falls. After the peak, it decreases toward the fold and beyond.

The adiabaticity parameter gamma = pi * omega_L0^2 / (2 * |d(omega_L0)/dt|) is smallest (most diabatic) where omega_L0 is both small AND rapidly varying. If omega_L0 has a minimum at tau_*, then d(omega_L0)/dt = 0 at tau_*, and gamma -> infinity (perfectly adiabatic at the exact minimum). Near tau_*, the LZ formula does not apply (it requires linear level crossing). The relevant quantity is the MINIMUM of gamma across the entire transit, excluding isolated stationary points where the level-crossing picture breaks down.

My P_LZ ~ 0.996 estimate used omega_L0 ~ 0.1 M_KK and d/dt ~ H ~ 3.7 M_KK evaluated at the fold. This is crude. The honest statement: the Leggett P_LZ is UNCOMPUTED from the full tau-dependent omega_L0(tau) profile. The computation LEGGETT-LZ-57 (Naz's sub-computation a) must evaluate omega_L0 at every tau, identify all local minima and maxima, and apply the LZ formula at each crossing or near-crossing. If the minimum of omega_L0 occurs AT the fold (where d(omega_L0)/dt is largest), the estimate holds. If the minimum occurs elsewhere (where d(omega_L0)/dt could be smaller), the adiabaticity parameter could be larger and P_LZ smaller. This is a concrete risk to the Leggett excitation hypothesis.

(b) Collective vs independent LZ for the 31 modes. The 31 Leggett modes have graph-momenta lambda_n spanning [0.171, 7.328]. Their gaps are omega_L(n) = sqrt(omega_L0^2 + J_L * lambda_n). The highest modes have omega_L(31) = 0.474 M_KK (for the GL gap choice). These are 6.8x larger than omega_L0. The adiabaticity parameter for mode n scales as omega_L(n)^2, so high-momentum modes are ~47x MORE adiabatic than the Fiedler mode. The expectation: the lowest ~5 Leggett modes (those with omega_L(n) < 0.15 M_KK) undergo LZ excitation; the highest ~20 modes (omega_L(n) > 0.3 M_KK) are adiabatically protected.

Regarding giant resonance analogy: collective enhancement requires the coupling between modes to be comparable to the level spacing. The Leggett inter-mode coupling arises from anharmonic terms in the Josephson potential (beyond the quadratic approximation). At the quadratic level (which is where the W2-4 computation lives), the 31 modes are independent harmonic oscillators on the graph. The anharmonic coupling scales as (phi_rel/phi_0)^4 where phi_rel is the relative phase fluctuation and phi_0 = sqrt(8 E_c / E_J). At the fold, <phi_rel^2>^{1/2} / phi_0 ~ 0.03 (from the quantum rotor estimate). The anharmonic coupling is O(10^{-3}), negligible compared to the mode spacing. The Leggett modes undergo INDEPENDENT LZ transitions, not collective. The giant resonance analog does not apply here.

**Q2 (Scission point).** In nuclear fission, scission is the point where the neck radius goes to zero and the fragments separate. The analog for the Leggett channel is the tau value where the Leggett gap omega_L0(tau) is smallest relative to the local transit velocity d(tau)/dt.

The transit velocity varies during transit. From the Friedmann equation, d(tau)/dt = H(tau)/M_KK. H(tau) varies with the scale factor: it is largest near the BCS transition (early tau) and decreases during expansion. The ratio omega_L0(tau) / H(tau) determines the adiabaticity at each tau. The "scission point" tau_s satisfies:

    d/dtau [omega_L0(tau) / H(tau)] = 0,  with  omega_L0(tau_s) / H(tau_s) minimal

From the available data: omega_L0 is O(0.1 M_KK) near the fold (tau ~ 0.2). H(tau) at the fold is ~3.7 M_KK (from the scale factor data). The ratio is ~0.03. At early tau (say tau ~ 0.05), E_J is larger (J_C2 ~ 1) so omega_L0 is larger (~0.2 M_KK), and H is also larger (~5 M_KK from the steeper scale factor), giving ratio ~0.04. At late tau (say tau ~ 0.4), E_J is much smaller (J_C2 ~ e^{-0.8} ~ 0.45) so omega_L0 is smaller (~0.05 M_KK), and H is smaller (~2 M_KK), giving ratio ~0.025.

The minimum ratio appears to occur at late tau (0.3-0.4), where the Leggett gap collapses faster than the Hubble rate decreases. This suggests the "scission" is distributed across the late transit (tau > 0.25), not concentrated at a single point. The Leggett excitation accumulates gradually as the system traverses the region where omega_L0/H < 0.05. This is qualitatively different from nuclear fission, where scission is abrupt (neck rupture). The fabric analog is more like "slow necking" -- a gradual weakening of the B2/B1 coupling during the descent from the fold.

The RATE-SCAN-57 computation (Naz's sub-computation c) will resolve this: by tracking P_exc(tau) at each point during the transit, we can identify whether excitation concentrates at a specific tau or accumulates smoothly. My prediction: smooth accumulation, no sharp scission.

**Q3 (Design error retrospective).**

Naz asks: should S56 have been designed around the Leggett channel from the start? Should S57 adopt a Strutinsky-like approach (compute smooth background first, subtract, study residual)?

The answer to the first question is: partially yes, partially no. The S55 FABRIC-COUPLING-55 result gave E_J = 7.042 M_KK. The back-of-envelope F_Josephson ~ 50 * 7 * 1 ~ 350 M_KK was available. I should have computed this before the session began and used it to set the energy scale. The Leggett mode was already identified in S49 (omega_L1 = 0.070, omega_L2 = 0.107, epsilon = 0.00248). The two-speed hierarchy was discoverable from S49 + S55 data without any new computation.

However, the BA spectrum characterization (W0-1) was not wasted. It established the THERMAL REGIME -- the fact that 7/31 modes are thermally populated at the fold, rising to 29/31 at the F_BA minimum. This information is needed for the N5 finite-rate computation: the thermal occupation determines the initial state from which the transit begins. If we had skipped W0-1 and gone directly to Leggett dynamics, we would have been working in a vacuum regarding the BA thermal background. The W0-1 result tells us that the pre-transit state is NOT the zero-temperature ground state but a finite-temperature ensemble with non-trivial BA occupation.

The answer to the second question (Strutinsky approach for S57) is YES. The smooth Josephson background should be computed FIRST at each tau, subtracted from the total, and the residual studied for non-monotonic behavior. This is what the Strutinsky procedure does in nuclear physics, and it is what I failed to do in S56. The S57 plan should structure its computations as:

1. Compute the smooth background: F_smooth(tau) = F_Josephson(tau) + F_cells(tau)
2. Compute the full transit dynamics: F_full(tau) from time-dependent BdG
3. Extract the shell correction: delta_F(tau) = F_full(tau) - F_smooth(tau)
4. Analyze delta_F for non-monotonic features and their physical origin

This Strutinsky decomposition guarantees that we never again mistake a 0.8% ripple for a significant feature.

**Q4 (Foam's trilemma escape).**

Yes, I agree that the Leggett excitation provides entropy without destroying overall phase coherence, and that this partially resolves W-FOAM-10. The argument is precise:

Foam's W-FOAM-10 states that P_exc * <cos(phi)> is bounded -- large E_J suppresses excitation (low P_exc) while maintaining coherence (high <cos(phi)>), and vice versa. The bound is on a SINGLE parameter E_J controlling BOTH quantities.

The Leggett channel breaks this single-parameter constraint. The Leggett gap omega_L0 depends on epsilon * E_J * Delta_eff, not on E_J alone. The relative phase phi_rel (between B2 and B1) is an INTERNAL degree of freedom that does not couple to the overall phase phi (the Josephson variable). Exciting the Leggett mode (increasing phi_rel fluctuations) does not decohere the overall phase (does not decrease <cos(phi)>).

Therefore: W-FOAM-10 should be reformulated. The original form bounds P_exc_total * <cos(phi)>. The corrected form should bound P_exc_Josephson * <cos(phi)>, with the Leggett excitation probability P_exc_Leggett as an INDEPENDENT variable not entering the bound. The Leggett channel provides a degree of freedom orthogonal to the suppression-excitation duality.

However, this escape has a quantitative limit. The Leggett entropy is S_L ~ N_excited * ln(2), where N_excited is the number of Leggett modes that undergo LZ excitation. From Q1(b), I estimate N_excited ~ 5-10 of the 31 modes (those with omega_L(n) < 0.15 M_KK). The corresponding energy is E_L ~ 5-10 * omega_L0/2 ~ 0.25-0.5 M_KK. This is 0.07-0.14% of F_Josephson. Whether this entropy contribution produces a free energy slope that competes with the Josephson slope is the quantitative question. At face value: dF_L/dtau would need to be O(1711/13) ~ 130 M_KK to compete. With 5-10 modes at 0.1 M_KK each, the Leggett free energy scale is ~1 M_KK. A slope of 130 M_KK from 1 M_KK of energy requires a 130:1 lever arm. This is implausible from entropy alone.

The honest assessment: the Leggett channel escapes W-FOAM-10 qualitatively (it is an independent degree of freedom) but may not escape it quantitatively (the energy scale is too small to compete with Josephson stiffness). The LEGGETT-ENTROPY-57 computation will resolve this.

### Part 3: Independent Analysis

**A1. The Leggett Channel in Detail -- Why It Is the Primary Excitation Candidate.**

The six reviews converge on the Leggett channel as the primary surviving excitation mechanism. I collect the structural reasons:

1. **Smallest gap in the system.** omega_L0 = 0.070-0.138 M_KK vs BCS gap 0.370 vs Josephson gap 13.04. The Leggett gap is 3-5x below BCS and 94-186x below Josephson. Landau-Zener excitation probability increases exponentially as the gap decreases.

2. **Absent at single-cell level.** The Leggett mode requires at least two cells with distinct internal structure (B2 and B1). It is a FABRIC excitation, invisible to all single-cell computations (S7-S55). This is why it was not discovered until S56. Every prior closure (46+ mechanisms through S55) operates on single-cell physics.

3. **Orthogonal to the Josephson phase.** Dirac's eq. 7 ([J, H_J] = 0) guarantees CPT symmetry of all excitations. But within the CPT-symmetric sector, the Leggett mode is an INTERNAL excitation that does not couple to the external (Josephson) phase. Exciting it does not destroy superfluid coherence. This is the escape from W-FOAM-10.

4. **Thermally populated at the fold.** omega_L0/T_GH = 0.12-0.23. The mode is in the classical regime (occupation >> 1). This means thermal fluctuations pre-seed the Leggett excitation before the transit begins. The LZ transition does not start from vacuum -- it starts from a thermally populated state with large amplitude.

5. **Carries entropy without energy.** A fully excited Leggett mode at omega_L0 ~ 0.1 M_KK carries entropy S ~ ln(2) ~ 0.7 nats but only energy E ~ 0.05 M_KK. The entropy-to-energy ratio S/E ~ 14 nats/M_KK is high. If entropy drives the CC (through the GGE non-thermal distribution), the Leggett channel is efficient: it produces maximum information-theoretic content per unit energy.

6. **Verified by CW's desert chronology.** The incoherent desert (0.22 < tau < 0.49, where E_J_GGE/H < 1) is precisely the regime where Leggett modes decouple from the Josephson background. During the desert, each cell's B2/B1 structure evolves independently (because the Josephson coupling is too weak to enforce coherence at the transit rate). Post-desert, when E_J/H > 1 again (recoherence), the Leggett modes that were excited during the desert remain as frozen excitations. This is the three-phase chronology: coherent (Leggett modes follow adiabatically) -> desert (Leggett modes excited independently) -> recoherent (Leggett excitations frozen as GGE relics).

**A2. The Two-Speed Hierarchy's Implications for Cosmological Observables.**

The two-speed hierarchy (c_BA/c_L = 12-21) has a direct cosmological implication that has not been discussed in any of the six reviews.

In standard LCDM, the dark energy equation of state w = -1 is scale-independent. Any w != -1 model (quintessence, k-essence) has a sound speed c_s^2 = dP/d(rho) that determines the dark energy clustering scale. If c_s^2 = 1 (canonical quintessence), dark energy does not cluster below the Hubble scale. If c_s^2 << 1, dark energy clusters on sub-Hubble scales, producing ISW signatures in the CMB and scale-dependent growth.

The fabric has TWO sound speeds: c_BA for the overall phase (dark energy bulk motion) and c_L for the internal structure (dark energy anisotropic stress). If the 4D observer sees an effective dark energy fluid with TWO distinct propagation speeds, the phenomenology goes beyond a single w(z):

- The BULK dark energy (overall phase) propagates at c_BA = 0.399 M_KK. In 4D units, this is c_s,bulk = c_BA / c (expressed in natural units where c_BA/M_KK is the dimensionless ratio).
- The INTERNAL dark energy (B2/B1 relative amplitude) propagates at c_L = 0.019-0.032 M_KK. This is 12-21x slower.

A two-fluid dark energy model with fast (bulk) and slow (internal) components would produce a SCALE-DEPENDENT effective w(z,k): at wavelengths shorter than the Leggett sound horizon (r_L ~ c_L / H ~ 0.005 in M_KK units), the internal component clusters independently of the bulk. At longer wavelengths, both components move together.

This is a PREDICTION: if the Leggett channel is excited during transit, the post-transit dark energy has anisotropic stress and scale-dependent clustering. Euclid's weak lensing tomography is sensitive to w_a (the time variation of w) at the 0.1 level. Whether the two-speed hierarchy produces a detectable w_a signature is UNCOMPUTED and should be added to the S57 plan as a follow-up to CHANNEL-DECOMP-57.

**A3. Session Design Self-Critique -- The Deeper Error.**

Q3 asks whether S56 should have been designed around the Leggett channel from the start. My answer in Part 2 was "partially yes." Here I give the deeper answer.

The S56 session plan was structured around the He-4 analogy: "single-atom Z does not predict superfluidity, so Z_cell does not predict Z_fabric." The hope was that collective modes (BA phonons) would break single-cell monotonicity the way phonon exchange in He-4 breaks the mean-field Gross-Pitaevskii equation. This analogy was wrong in a specific, identifiable way.

In He-4, the collective mode (phonon) energy is COMPARABLE to the single-atom kinetic energy. The lambda transition occurs when the phonon contribution to the free energy becomes thermodynamically significant -- both terms are O(k_B T) per atom. In the fabric, the collective mode energy (F_BA ~ 7 M_KK) is NOT comparable to the Josephson condensation energy (F_J ~ 350 M_KK). The ratio is 1:50. The He-4 analogy would have predicted stabilization only if the BA and Josephson energy scales were comparable. They are not, and this was knowable from E_J = 7.042 M_KK (S55) and N_bonds = 50 (S54).

The error was an ANALOGY FAILURE: applying a qualitative physical picture (He-4 superfluidity) without checking whether the quantitative preconditions (comparable energy scales) were met. This is a variant of the dictionary-entry trap that the epistemic discipline rules warn against. The He-4 analogy is a dictionary entry -- a mapping between two systems that preserves structure but not necessarily scale. The mapping preserved structure (both systems are BCS superfluids on a lattice) but not scale (He-4 has K/E_J ~ 1; the fabric has F_BA/F_J ~ 0.02).

The lesson for S57: before applying any physical analogy, verify that the ENERGY SCALE RATIOS match between the analog and the target. The nuclear fission analogy (Naz's N2) should be subjected to the same test. In nuclear fission, the ratio of quasiparticle excitation energy to collective kinetic energy is E_qp/E_kin ~ 10-20 MeV / 200 MeV ~ 0.05-0.10. In the fabric transit, the estimated Leggett excitation energy is E_L ~ 0.5 M_KK, and the total Josephson potential energy difference across the transit is delta_F_J ~ 350 M_KK. The ratio is E_L/delta_F_J ~ 0.001 -- 50-100x smaller than in nuclear fission. If the nuclear analogy's quantitative predictions depend on this ratio being O(0.1), the fabric is in a different regime. The FINITE-RATE-TRANSIT-57 computation must determine the actual E_L/delta_F_J ratio, not assume it matches the nuclear value.

**A4. Revised S57 Specification -- Incorporating All Six Perspectives.**

I endorse Naz's N5 specification with the modifications from Part 1 and the following additions from the six reviews:

**From Foam (W-FOAM-10 test):** Add a computation of P_exc_Leggett * <cos(phi)> at each tau during the transit. If P_exc_Leggett > 0.5 AND <cos(phi)> > 0.9 simultaneously at any tau, the trilemma escape is quantitatively confirmed. Pre-register: PASS if both conditions hold at the same tau. FAIL if P_exc_Leggett * <cos(phi)> < 0.1 at all tau. This is the direct test of whether the Leggett channel is orthogonal to the Josephson phase, as I argued in Q4.

**From CW (desert chronology):** Add explicit tracking of the E_J_GGE(tau)/H(tau) ratio during time evolution, as Naz specifies. But also track the CORRELATION between cells: compute the inter-cell phase correlation <cos(phi_1 - phi_2)>(tau) during the transit. If this drops below 0.5 during the desert (0.22 < tau < 0.49), the cells are genuinely decoupled and the single-cell GGE physics activates. Pre-register: PASS if <cos(phi_1 - phi_2)> < 0.5 for any tau in [0.22, 0.49]. This directly tests CW's three-phase chronology.

**From Connes (anisotropic inner fluctuation):** The QUASIPARTICLE-TUNNEL-57 computation should test whether the mode-dependent tunneling breaks the R-G algebra. Explicitly: compute the commutator [H_qp, Q_j] where Q_j are the 8 Richardson-Gaudin conserved quantities. If ||[H_qp, Q_j]|| / ||Q_j|| > 0.1 for any j, the integrability is broken. This is the NCG non-central-inner-fluctuation test translated into the many-body language.

**From Dirac (CPT):** Track |<N_B2>(t) - <N_B2>(t_0)| and |<N_B1>(t) - <N_B1>(t_0)| independently. By eq. 10 of Dirac's review, these must remain CPT-paired. Any deviation signals a numerical error, not new physics.

**Prioritization for S57.** Taking the six reviews together, the computation priority is:

1. FINITE-RATE-TRANSIT-57 (Naz N5, decisive). This is the umbrella computation. All sub-computations (LEGGETT-LZ-57, CHANNEL-DECOMP-57, RATE-SCAN-57) are outputs of the same time evolution.

2. QUASIPARTICLE-TUNNEL-57 (my collab, channel 4). Independent of TRANSIT-57. Tests the second surviving degree of freedom (anisotropic integrability breaking).

3. LEGGETT-ENTROPY-57 (my collab, conditional on TRANSIT-57 PASS). Computes the free energy contribution from Leggett excitations. Tests whether the Leggett channel can overcome the Josephson slope.

4. N-SCALING-GAP-57 (CW recommendation). Compute Josephson gap for N = 2, 4, 8, 16, 32. Determines the thermodynamic limit behavior.

5. TOPOLOGY-TRANSITION-57 (my collab, lower priority). Characterize the tau = 0.449 quasi-crossing. Deferred if TRANSIT-57 returns decisive results.

All 5 computations are cheap (120x120 matrices at most, sub-second per diag). The bottleneck is the physical design, not the compute. S56 taught us that misidentifying the relevant energy scale wastes a session. S57 must open with the Strutinsky decomposition (smooth background first) and then compute the transit dynamics against that background.

