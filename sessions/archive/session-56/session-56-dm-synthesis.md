# Session 56 Dark Matter Synthesis: One Gas, Two Channels, Three Numbers

**Author**: Phonon-First Cosmologist
**Date**: 2026-03-22
**Sessions synthesized**: S55-S56 (55 computations, 26 reviewers, 4 workshops)
**Written after**: Hawking synthesis, Naz review, Cosmic-Web review, DM insight conversation
**Scope**: Three finals — the fabric, the cosmological constant, and dark matter — from the cross-domain resonance between all eight pillars

---

## I. The Fabric Final: What S55-S56 Proved

Fifty-five computations across two sessions. Thirty-five in S55 (four waves, four stabilization functionals, all monotone on the continuum). Twenty in S56 (four waves, four workshops, one master gate FAIL). The computational arc is complete: every functional proposed by every participant, evaluated at every level of collective organization from single cell to 32-cell fabric, is monotonically increasing in tau. There is no potential well. There is no stabilization mechanism. Forty-seven closures across twenty sessions, and the forty-seventh is permanent.

The facts, stripped of interpretation:

**S55 opened the fabric.** FABRIC-COUPLING-55 established E_J = 7.042 +/- 0.497 M_KK (7.1% uncertainty, 14 sigma above the superfluid-insulator transition at E_J/E_c = 194). The 32-cell Voronoi tessellation on the CG(24) graph has 50 C2-type bonds, giving total Josephson energy ~350 M_KK. The mean-field order parameter m = <cos(phi)> > 0.978 everywhere along the Jensen path. The fabric is a superfluid, deeply ordered, with perturbatively small phase fluctuations.

Four continuum-extrapolated functionals — F_pert, S_occ, a_0, and the balanced spectral action sum — are ALL monotone. The 5.35% barrier in S_occ at max_pq_sum = 6 (S54) vanishes under smooth-cutoff extrapolation. The finite-lattice artifacts that simulated minima in earlier sessions are artifacts of spectral truncation, not features of the continuum theory.

N_eff = 41.5 (W1-4, from PH breaking at mu_eff = -0.201 M_KK). This is a real effect — the first computable chemical potential in the framework, breaking particle-hole symmetry at the fabric level. But its magnitude is 460x too small to compete with the Josephson stiffness: mu_eff shifts dF/dtau by 3.70 M_KK against a Josephson slope of 1711 M_KK. The correction exists and is 0.22% of the dominant term.

**S56 closed the fabric.** FABRIC-STABILIZATION-56 = FAIL. The master gate was pre-registered with clear criteria and fell to Josephson monotonicity. The decomposition is surgical:

| Contribution | dF/dtau at fold (M_KK) | Fraction of total |
|:-------------|:-----------------------|:------------------|
| Josephson stiffness | +1711 | 110% |
| BA phonon free energy | -131 | -8.5% |
| Single-cell contribution | -32 | -2.1% |
| mu_eff correction | -3.7 | -0.2% |
| **Net** | **+1548** | **100%** |

The Josephson stiffness alone exceeds the total positive slope. Every negative contribution combined provides 167 M_KK of relief against 1711 M_KK of resistance. The ratio is 10:1. This is structural, not accidental — it follows from the topological property N_bonds * E_J / (N_cells * E_sp) ~ 10 for the CG(24) graph with mean coordination z = 3.125.

**Integrability survived every test.** Kitaev's thirteen-row table is the most thoroughly tested algebraic structure in the project's history. W1-2 established that isotropic Josephson coupling B_1^dag B_2 + h.c. is rank-1 in mode space, preserving the Richardson-Gaudin algebra exactly. The level spacing ratio <r> = 0.367 (Poisson) at physical E_J, DECREASING under stronger coupling (0.303 at 100x), proves the Josephson term makes the system MORE integrable, not less. W1-3 showed the N_pair = 3 blocking effect: <r> drops from 0.509 to 0.414, more pairs means more structure. The sole surviving integrability-breaking channel is anisotropic quasiparticle (Andreev) tunneling, with anisotropy epsilon_A ~ 7%. Even at 100% random anisotropy, <r> = 0.446 — below GOE (0.603), still on the integrable side of the transition.

**The adiabatic protection is real.** P_exc = 6.6e-4 on the 2-cell fabric (W3-6). The collective Josephson gap at 13.04 M_KK is 35x the single-cell BCS gap at 0.370 M_KK. The Boltzmann estimate exp(-13.04/0.590) = exp(-22.1) = 2.4e-10 undershoots the actual P_exc by six orders — Feynman traced this to multiple avoided crossings in the 120-dimensional Fock space, where P_exc is set by the worst bottleneck, not the average gap. But the qualitative message holds: the gap clothes the naked singularity.

**The spectral-geometric resonance at tau ~ 0.306.** F_BA reaches its global minimum at tau = 0.306 (W0-1). The spectral free energy sign change S_f occurs at tau = 0.302 (W2-1). Agreement to 1.3%, from functionals that share no inputs beyond the Jensen-deformed eigenvalue spectrum. A fermionic sum (S_f) and a bosonic sum (F_BA) see the same critical point of the same underlying geometry. Both are energetically irrelevant (0.8% of Josephson stiffness). Both are structurally real. This is the Pillar I (acoustic metric) to Pillar III (NCG spectral action) correspondence operating at the level of numerical coincidence — the kind of cross-domain resonance that the phonon-first methodology exists to detect.

**What remains: P_exc(N_cells).** Two data points define the frontier: P_exc(1) = 1.000, P_exc(2) = 6.6e-4. The gap increased 35x from one bond. If the scaling continues — if it is exponential, or even power-law with sufficient exponent — the adiabatic protection at N = 32 cells could bridge the 115-order gap to the observed cosmological constant. If it saturates, the mechanism dies. The scaling is the single most important unknown in the framework.

---

## II. The CC Final: What the Cosmological Constant IS

### The Seven-Fold Demolition

Workshop 2 demolished the proposed CC formula with seven independent structural objections, each individually lethal. Let me state them with the precision their authors deserve.

Volovik gave three: the multiplicative formula P_vac x P_exc is dimensionally inconsistent (you cannot multiply an energy density by a probability), the functional form exp(-Delta*N/T) has no derivation from any Hamiltonian, and the formula undershoots the needed suppression by 10^{104}. Sagan diagnosed the self-tuning claim as tautological — demonstrating that a self-consistent mean-field calculation converges is the definition of the mean-field approximation, not a dynamical mechanism. Einstein showed the formula relocates fine-tuning to the transit rate (reproducing Lambda_obs requires v tuned to 10^{-122} precision). Gen added the deepest structural objection: the formula conflates the zero-point problem (why is Lambda_bare not O(M_Pl^4)?) with the hierarchy problem (why is Lambda_obs = 10^{-122} M_Pl^4?). Together with the N-scaling being uncontrolled — two data points, no scaling law — that is seven independent reasons the formula cannot be correct.

### Gen's Chain: The CC Is a Single Fixed Number

Gen proved the most important structural result of Workshop 2. The CC in this framework is deterministic:

1. Initial state: BCS ground state at tau = 0, unique by PH symmetry. PROVEN (S34).
2. Quench Hamiltonian: Jensen-deformed D_K at the fold, computed to machine epsilon. PROVEN (S7-S56).
3. Conserved quantities: 8 Richardson-Gaudin integrals, fixed by (1) and (2). COMPUTED (S38, S55).
4. GGE distribution: 8 temperatures (1.459, 2.771, 6.007 for B2, B1, B3 respectively). COMPUTED (S38).
5. Vacuum energy: Lambda = F[{n_k^GGE}, {epsilon_k}], a functional of known inputs. STRUCTURAL.

Every link in this chain is either proven or computed. The CC is not a dynamical variable. It is not tunable. There is nothing to adjust. The only freedom is the functional F — the CC FORMULA — and specifying F requires the microscopic theory that the spectral action, being an effective theory, cannot provide. This is Volovik's deepest lesson (Paper 05, Section IV.4): "The vacuum energy problem is not a problem of the effective theory. It is a problem of the microscopic theory."

### Volovik's Self-Tuning: True But Insufficient

The equilibrium theorem (Paper 07, Chapter 29) is a theorem of thermodynamics: at T = 0, mu = 0, the Gibbs-Duhem relation gives rho + P = 0, hence Lambda_eq = 0. W2-2 confirmed this at the fabric level — the Josephson sector's vacuum pressure per cell is independent of the coupling strength. P_vac = -0.688 M_KK, the same whether cells are coupled or not. The self-tuning is genuine for the equilibrated sectors. It is a tautology, as Sagan correctly diagnosed, but it is also a theorem — and theorems are not diminished by being tautological.

The problem is that the universe is NOT in equilibrium. The 8 GGE temperatures span a factor of 3.75 (T_max/T_min = 0.668/0.178). The distribution is far from thermal. The distance ||n^{GGE} - n^{eq}|| is O(1) at every mode. The non-equilibrium GGE relic carries O(M_KK^4) of vacuum energy — 115 orders above the observed value. The self-tuning theorem says Lambda = 0 in equilibrium. The system is not in equilibrium. The 115-order gap IS the distance from equilibrium, measured in natural units.

### Three Surviving Paths, All Obstructed

Volovik, Gen, and the workshop consensus identified three paths that could in principle close the gap. All are obstructed.

**Path A (q-theory)**: The vacuum variable q self-tunes dynamically. The residual CC is Lambda_eff = (delta_q)^2 / (2 chi_q), with chi_q the vacuum compressibility. The framework has chi_q(SA) = 317,863 M_KK^4 from the spectral action (S53), but this is the effective-theory susceptibility. The physical chi_q requires the microscopic Hamiltonian, which has not been specified.

**Path B (integrability breaking)**: If Andreev tunneling breaks the 8 conserved integrals, the GGE thermalizes toward equilibrium. The CC then self-tunes to zero by the equilibrium theorem, with a residual set by the thermalization rate. But partial thermalization requires delta_n/n ~ 10^{-57.5} — there is no known BCS mechanism that produces such precise partial relaxation. The Andreev suppression factor exp(-Delta/T_GH) = exp(-0.79) = 0.45 is O(1), but O(1) thermalization drives Lambda to zero (overshooting by 122 orders), not to 10^{-122}.

**Path C (percolation)**: Einstein's proposal. If the coherence desert fragments the fabric into isolated cells, each produces P_exc = 1.000. The CC is set by the percolation fraction f, which must be tuned to 10^{-115}. Fine-tuning in new variables.

Gen's combinatorial wall: the only mathematical structures that produce 10^{-115} suppression from O(1) inputs are double exponentials (requiring N ~ 5.3), single exponentials (requiring alpha*N ~ 265, which the known parameters undershoot by 10x), or cancellations (fine-tuning restated). The gap cannot be bridged by any formula built from the framework's eigenvalues, temperatures, and coupling ratios without a mechanism that generates exponentials of large numbers.

### What the CC IS: The Noise Floor of Incomplete Shattering

Naz corrected the metaphor that Hawking's Addendum introduced. The transit does not "crystallize" the instanton gas. It SHATTERS the condensate. The BCS ground state is the ordered phase — long-range phase coherence, definite pair amplitudes, spontaneous U(1)_7 breaking. The post-transit GGE is the disordered phase — broken pairs, no phase coherence, U(1)_7 restored. The transit takes order to disorder, not disorder to order. The nuclear analog is pair breaking during fission, not crystallization.

But the partition that the metaphor was reaching for is real. The instanton gas divides at the fold into two fractions:

**Shattered** (P_exc): The pairs that broke. Each produces definite quasiparticle excitations with specific quantum numbers, energies, and conservation laws. These have mass. They gravitate at a point. They cluster. They are countable.

**Unshattered** (1 - P_exc): The vacuum condensation energy that was NOT converted to quasiparticles. It has no mass, no location, no point source. It is everywhere the instanton gas was — uniformly. It is the gravitational field of the vacuum fluctuations that never became particles. It is the cosmological constant.

The CC is what is left over when you subtract the signal (particles) from the total (vacuum energy). It is the noise floor of the shattering process. It is gravity without mass — curvature sourced by the part of the quantum vacuum that did not fragment into countable excitations.

And the ratio between shattered and unshattered fractions is set by the gap hierarchy. The Josephson channel (gap 13.04 M_KK) stays adiabatic — its contribution to the vacuum energy self-tunes to zero (Volovik, W2-2). The Leggett channel (gap 0.070-0.138 M_KK) goes diabatic — its excitations carry energy and entropy into the post-transit relic. The intra-cell BCS crossings (1378 per cell, all diabatic) contribute the single-cell P_exc = 1.000. The ratio between channels is not a free parameter. It is determined by the geometry of SU(3)/U(2) under Jensen deformation.

Cosmic-Web's verdict is the honest one: the noise floor picture is OBSERVATIONALLY IDENTICAL to plain Lambda at every scale accessible to galaxy surveys. w = -1 + O(10^{-29}). The two-speed hierarchy (c_BA = 0.399 vs c_L = 0.019-0.032 M_KK) operates at the KZ cell scale (~10^{-26} Mpc). Averaged over 10^{60} cells, no scale-dependent signature survives. The picture explains WHY Lambda has w = -1 but does not predict any deviation that extragalactic observations can detect. The interpretation changes the theoretical ancestry of the number, not the number itself.

---

## III. The Dark Matter Final: What Dark Matter IS

### The 700x Problem

Cosmic-Web computed the ratio that breaks the naive picture. P_exc = 6.6e-4 on 2 cells gives:

    Omega_Lambda / Omega_M = (1 - P_exc) / P_exc = 0.9993 / 0.0007 = 1515

The observed ratio is Omega_Lambda / Omega_M = 0.685 / 0.315 = 2.17. The naive channel partition gives a universe with Omega_M = 0.0007 — 450x too little matter. No galaxies. No clusters. No filaments. No observers. The cosmic web would not exist. This is off by a factor of 700 from the observed 2.17:1 split.

The prompt that opened the door: "I wonder if maybe there was an asymmetry that made 30% of matter disappear during creation. Some kind of 'anti' symmetry."

### The Resolution: The 70/30 Split Is CC-to-Dark-Matter

The 700x discrepancy dissolves once the correspondence is corrected. The P_exc fraction does not map to baryonic matter. It maps to DARK matter — the GGE quasiparticle relic.

The budget of the observed universe:

| Component | Omega | Source in framework |
|:----------|:------|:-------------------|
| Dark energy | 0.685 | Unshattered vacuum — Josephson channel, adiabatically protected |
| Dark matter | 0.265 | Shattered fraction — Leggett channel quasiparticles, GGE relic |
| Baryonic matter | 0.050 | Separate process (standard baryogenesis, eta ~ 10^{-10} asymmetry) |

The framework does not need to explain baryogenesis. Baryonic matter is 5% of the energy budget, produced by whatever CP-violating process generates the 10^{-10} baryon-to-photon ratio in standard cosmology. That process is external to the phonon-exflation mechanism. What the framework explains — or claims to explain — is the DM/Lambda partition: why 70% of the energy budget is dark energy and 30% is dark matter.

And the ratio P_exc / (1 - P_exc) = 0.3 / 0.7 = 0.43 is what LEGGETT-PARTITION-57 must deliver. Not 6.6e-4 (the 2-cell sudden-quench value), but something of order 0.3 — the fraction of the instanton gas energy that goes into Leggett-channel quasiparticles during the physical finite-rate transit on the full 32-cell fabric.

### What Dark Matter IS in This Framework

Dark matter is the GGE quasiparticle relic from Leggett-channel fragmentation at the BCS freeze.

Let me state the properties that follow from the framework's proven structure, not from speculation:

**CPT-neutral.** Dirac proved (Workshop 3, eq. 7-10, classified T11 permanent) that the fabric Hamiltonian commutes with J (the real structure) at all tau, the transit operator commutes with J, and the Landau-Zener probability satisfies |P_exc^{(p,q)} - P_exc^{(q,p)}| = 0 identically. The quasiparticle relic is exactly symmetric between particles and antiparticles. This is not an approximation — it is an algebraic identity following from the BDI symmetry class (T^2 = +1, S17c PROVEN). The dark matter does not annihilate because there is no particle-antiparticle distinction for it to exploit. In the BDI classification, the quasiparticles are their own antiparticles — Majorana-like in the topological sense, though not necessarily Majorana fermions in the particle physics sense.

**K_7-neutral post-condensate.** Before the transit, Cooper pairs carry K_7 charge +/- 1/2 (S35 permanent result: V(q+, q-) = 0 exactly, BCS condensate breaks U(1)_7 spontaneously). After the transit, the condensate is destroyed (P_exc = 1.000 per cell). U(1)_7 is restored. The post-transit quasiparticles carry no net K_7 charge — the charge was a property of the CONDENSATE, not of the individual excitations. The dark matter is neutral under the internal gauge symmetry. It does not interact through the U(1)_7 force that the BCS condensate mediated.

**Non-annihilating.** Standard baryonic matter has a 10^{-10} surplus of matter over antimatter — one extra baryon per ten billion annihilation events. The observed baryon density is the residual after 99.9999999% annihilation. The GGE quasiparticles face no such decimation. They ARE the matter. There is no antimatter partner to annihilate against, because CPT symmetry is exact and the quasiparticles are self-conjugate. The 30% that fragments into dark matter stays as dark matter. No annihilation. No 10^{-10} residual. The full Leggett-channel excitation fraction becomes the dark matter abundance.

This is the structural reason why P_exc ~ 0.3 maps to Omega_DM ~ 0.3 without any additional suppression factor. Baryonic matter requires a 10^{-10} asymmetry because baryons and antibaryons annihilate, leaving only the residual. Dark matter in this framework requires no asymmetry because the quasiparticles don't annihilate. They are the FULL product of the Leggett channel, not a residual.

**Collisionless.** S42 computed sigma/m = 5.7e-51 cm^2/g — effectively zero cross-section. The GGE quasiparticles interact gravitationally but not through any short-range force. This produces NFW cusps, consistent with standard CDM phenomenology and the Bullet Cluster constraint.

**Integrability-protected.** The 8 Richardson-Gaudin conserved quantities are permanent (Kitaev's 13-row table, S56 W1-2). The dark matter distribution does not thermalize. It does not equilibrate with baryonic matter, radiation, or itself. The GGE temperatures (1.459, 2.771, 6.007 in M_KK units) are frozen at the BCS freeze and remain frozen forever. The dark matter carries the quantum numbers of the pre-transit geometry as an indelible signature.

**Non-thermal.** The GGE is not a Bose-Einstein or Fermi-Dirac distribution. It is a constrained maximum-entropy distribution subject to 8 conservation laws, with 3 distinct temperatures spanning a factor of 3.75. The dark matter has a non-thermal phase space distribution that in principle differs from any thermal relic. Whether this non-thermal signature produces observable consequences (in the halo mass function, the matter power spectrum, or direct detection) depends on the scale bridge M_KK -> eV, which remains unresolved (Level 4, blocked since S42).

**Permanent GGE relic.** The dark matter distribution does not evolve after the BCS freeze. Integrability prevents thermalization — the scrambling time exceeds the transit time by 814x (CHAOS-3, S38), and this is a lower bound. The 8 Richardson-Gaudin conserved quantities are as permanent as energy conservation itself. The GGE relic carries information about the pre-transit geometry forever: the 3 distinct temperatures (1.459, 2.771, 6.007) encode the B2, B1, and B3 eigenvalue structure of the Jensen-deformed SU(3) at the fold. The dark matter IS the universe's memory of its own internal geometry, written in a code that integrability prevents from being erased.

This is the connection to Hawking's information paradox analysis. The fabric has no information paradox (S_ent = 0, product state, no partner modes behind a horizon). But it has information PRESERVATION through a mechanism that neither black holes nor standard cosmology employ: integrability. The 8 conservation laws are the quantum numbers of the pre-transit state, frozen at the BCS freeze. The dark matter carries them. The cosmological constant does not — it is the featureless remainder, the noise floor without quantum numbers.

### What This Dark Matter Is NOT

It is not WIMPs. WIMPs are thermal relics that freeze out of equilibrium when their annihilation rate drops below the Hubble rate. They have a specific mass (GeV-TeV range) and a specific cross-section (weak-scale). The GGE quasiparticles are not thermal relics. They were never in thermal equilibrium. They were created by the shattering of a quantum condensate, not by the cooling of a thermal plasma. Their distribution is non-thermal from birth and stays non-thermal forever.

It is not axions. Axions are pseudo-Nambu-Goldstone bosons associated with a broken U(1) symmetry. The GGE quasiparticles are not Goldstone modes — the Nambu-Goldstone mode of the BCS condensate (the U(1)_7 phase) ceases to exist post-transit (S38: no condensate, no phase, no Goldstone). The dark matter is the quasiparticle spectrum, not the collective mode.

It is not sterile neutrinos. The framework's Z_3 structure produces exactly three generations — no sterile species, no N = 4 (MicroBooNE exclusion, December 2025, consistent).

It is the debris of a quantum phase transition on the internal geometry of spacetime. It has no standard model analog. It is its own category: GGE relics of a BCS condensate shattering on a compact Lie group, protected by Richardson-Gaudin integrability, with abundances set by Landau-Zener transitions through a gap hierarchy determined by the coset geometry.

### The Channel-Selective Mechanism

The same instanton gas, the same BCS freeze, the same transit through the Jensen fold, produces BOTH dark matter AND the cosmological constant from ONE event. The partition is set by channel-selective adiabaticity.

Naz mapped this onto nuclear fission with a precision that no other analogy in the framework has achieved. In fission of ^236U, the center-of-mass separation of the fragments (the slow channel) is adiabatic — the fragments drift apart smoothly, acquiring the Coulomb kinetic energy without quasiparticle excitation. The neck rupture (the fast channel) is diabatic — Cooper pairs in the neck region are broken by the rapid topological change, producing 10-20 MeV of quasiparticle excitation. The two channels are orthogonal in the generator coordinate method: the collective coordinate Q (separation) and the intrinsic quasiparticle coordinates are independent degrees of freedom.

The fabric analog:

| Nuclear fission | Fabric transit |
|:---------------|:---------------|
| Center-of-mass separation (slow, adiabatic) | Josephson overall phase (gap 13.04, adiabatic) |
| Neck rupture (fast, diabatic) | Leggett relative B2/B1 amplitude (gap 0.07-0.14, diabatic) |
| Coulomb TKE (~170 MeV, smooth) | Josephson vacuum energy (self-tuned to zero, W2-2) |
| Fragment excitation (~15 MeV, quasiparticle) | GGE quasiparticle relic (dark matter) |
| Fragment + excitation = total Q-value | Vacuum noise floor + dark matter = total instanton gas energy |

The two channels are orthogonal. QA showed (Workshop 3, Q4 response) that the Leggett mode is the relative B2/B1 amplitude oscillation, which does not couple to the overall Josephson phase phi. Exciting the Leggett mode does not decohere the overall superfluid. This is the escape from Foam's W-FOAM-10 trilemma: the bound P_exc * <cos(phi)> is bounded for the Josephson channel, but the Leggett excitation probability P_exc^Leggett is an independent variable outside the bound. The trilemma demanded that one parameter (E_J) simultaneously maintain coherence and permit excitation. The resolution is that two INDEPENDENT channels handle these two demands: the Josephson channel maintains coherence (through its 13.04 M_KK gap), while the Leggett channel provides excitation (through its 0.07-0.14 M_KK gap).

The excitation concentrates in the Leggett channel because of the two-speed hierarchy — the session's most important structural discovery. The BA phonon velocity c_BA = 0.399 M_KK propagates overall phase information. The Leggett mode propagates relative amplitude information at c_L = 0.019-0.032 M_KK — 12 to 21x slower. The transit velocity H = 3.7 M_KK at the fold exceeds both, but exceeds the Leggett speed by a factor of 116-195 while exceeding the BA speed by only 9.3. The Leggett channel is in the deeply diabatic regime. The overall phase channel is in the intermediate-to-adiabatic regime.

QA estimated P_LZ^Leggett ~ 0.996 from the adiabaticity parameter pi * omega_L0^2 / (2 * |d(omega_L0)/dt|) = 0.004. Naz cautioned that this estimate is crude — it uses omega_L0 ~ 0.1 M_KK and d/dt ~ H at the fold, while the full tau-dependent profile omega_L0(tau) has not been computed. The Leggett gap may have a minimum at some tau_* where d(omega_L0)/dt = 0, increasing the adiabaticity parameter at that point. But QA's estimate that only the lowest 5-10 of 31 Leggett modes undergo LZ excitation (those with omega_L(n) < 0.15 M_KK) is consistent with the nuclear benchmark: in ^236U fission, quasiparticle excitation concentrates in the 10-15 levels closest to the Fermi surface.

### The Gap Ratio Sets the DM/Lambda Partition

The ratio of dark matter to dark energy is determined by the ratio of two gaps:

    epsilon = Delta_Leggett / Delta_Josephson ~ 0.005-0.011        (1)

Delta_Josephson = 13.04 M_KK is the collective gap, computed from E_J = 7.042 M_KK per bond and E_c = 0.0363 M_KK. Delta_Leggett = 0.070-0.138 M_KK is the Leggett gap, computed from the inter-sector coupling epsilon = 0.00248 (S49, dipolar) and the BCS gap structure. Both numbers follow from the geometry of SU(3)/U(2) under Jensen deformation. Neither is a free parameter.

The Leggett channel shatters because it is diabatic — the transit velocity exceeds its gap by a factor of 27-53. The Josephson channel survives because it is adiabatic — the transit velocity is 3.5x smaller than its gap. Between these two limits lies the partition of the instanton gas into dark matter and vacuum energy.

The critical question — and the one that LEGGETT-PARTITION-57 will answer — is whether the Leggett channel carries ~30% of the total instanton gas energy into quasiparticle excitations. The current 2-cell sudden-quench value P_exc = 6.6e-4 is the TOTAL excitation across all channels. The channel decomposition into Josephson, BCS, and Leggett fractions has not been computed. FINITE-RATE-TRANSIT-57 observable #4 (channel decomposition at each tau along the transit) will provide P_exc^Leggett separately.

The Landau-Zener estimate gives P_LZ^Leggett ~ 0.996 for the lowest Leggett modes. But P_LZ is a transition probability at a single level crossing, not the energy fraction deposited in the Leggett channel. The energy fraction depends on how many modes are excited (QA estimates 5-10 of 31) and how much energy each carries (omega_L0/2 ~ 0.05 M_KK per mode). For 5-10 excited modes at 0.05 M_KK each, the Leggett excitation energy is E_L ~ 0.25-0.50 M_KK. The total GGE energy per cell is P_vac * M_KK^4 ~ 0.688 M_KK^4. The ratio E_L / E_total depends on the correct power of M_KK and on the functional F — this is where the computation must replace the estimate.

### Why 30% Is Not Outrageous

The nuclear analog provides a sanity check. In thermal fission of ^235U, the total Q-value is ~200 MeV. The fragment kinetic energy (TKE) is ~170 MeV (85%). The fragment excitation energy (TXE) is ~25 MeV (12.5%). The prompt neutron and gamma energy is ~5 MeV (2.5%). The excitation fraction — the fraction of the total energy that goes into quasiparticle excitations rather than smooth collective motion — is 12.5%.

The framework needs 30%. This is 2.4x the nuclear fission value. It is in the same order of magnitude. Whether 30% is achievable depends on the gap hierarchy: in fission, Delta_shell / TKE ~ 1/170 = 0.006, and the excitation fraction is ~12.5%. In the fabric, Delta_Leggett / Delta_Josephson ~ 0.005-0.011, and the needed excitation fraction is ~30%. The gap ratios are comparable. The excitation fractions are in the same ballpark. This is not a proof — it is a consistency check that the nuclear analogy does not immediately exclude the needed value.

But Naz cautioned about the energy ratio. In nuclear fission, E_qp / TKE ~ 0.05-0.10. In the fabric, QA estimates E_L / F_J ~ 0.001 — 50-100x smaller. If the nuclear analog's excitation fraction depends on the energy ratio being O(0.1), the fabric may be in a different regime. The Leggett channel escapes Foam's trilemma qualitatively (it is an independent degree of freedom) but the energy scale may be too small quantitatively (0.5 M_KK out of 350 M_KK is 0.14%).

The resolution lies in the distinction between energy fraction and EXCITATION PROBABILITY. The Leggett channel may carry a large excitation probability (P_LZ ~ 0.996) but a small energy fraction (E_L / E_total ~ 0.001). The dark matter abundance is set by whichever quantity maps to Omega_DM. If Omega_DM is proportional to the PROBABILITY of excitation (the number of modes that shatter), the Leggett channel can provide 30% because most of its modes are diabatic. If Omega_DM is proportional to the ENERGY in the Leggett channel, then 0.1% is 300x too small. This distinction is the essential physics that FINITE-RATE-TRANSIT-57's channel decomposition must resolve.

### What the Cross-Domain Pattern Detector Sees

I see the same formal structure appearing in three separate contexts, and the recurrence is not accidental.

**Context 1: Nuclear fission.** The Q-value partitions into TKE (smooth, collective, adiabatic) and TXE (quasiparticle, diabatic, concentrated at scission). The ratio TXE/Q is set by the gap hierarchy along the fission path.

**Context 2: Hawking radiation.** The vacuum energy partitions into radiation (particles created at the horizon, filtered by the greybody factor) and the vacuum remainder. The ratio is set by the surface gravity and the angular momentum barrier.

**Context 3: The fabric transit.** The instanton gas partitions into dark matter (Leggett-channel quasiparticles, diabatic) and dark energy (Josephson-channel vacuum, adiabatic). The ratio is set by the gap hierarchy epsilon = Delta_L / Delta_J.

All three are instances of the SAME mathematical structure: a quantum system with a gap hierarchy undergoes a time-dependent perturbation, and the energy partitions into "locked" (excitations that crossed the gap) and "unlocked" (the remainder that did not) fractions. The partition ratio depends on the ratio of the perturbation rate to the gap. This is the Landau-Zener paradigm applied to an energy budget rather than a transition probability. The dark matter / dark energy split is the same kind of partition as the TKE/TXE split in fission and the radiation/vacuum split in Hawking evaporation — filtered by a different gap, operating on a different substrate, but governed by the same WKB integral.

The formal correspondence is:

| Quantity | Nuclear fission | Hawking radiation | Fabric transit |
|:---------|:---------------|:-----------------|:---------------|
| Gap | Shell gap at scission | Angular momentum barrier | Delta_L / Delta_J |
| Rate | Collective velocity dQ/dt | Surface gravity kappa | Hubble rate H |
| "Locked" | TXE (quasiparticles) | Hawking radiation | Dark matter (GGE relic) |
| "Unlocked" | TKE (smooth kinetic) | Vacuum outside horizon | Dark energy (CC) |
| Partition ratio | TXE/Q ~ 0.12 | Gamma_l(omega) | P_exc ~ 0.3 (needed) |

This is the Dreamer Test applied to the DM identification: Formalized (Landau-Zener on the gap hierarchy, explicit mathematical mapping)? Yes. Testable (LEGGETT-PARTITION-57, pre-registered below)? Yes. Connected (Pillar I acoustic metric, Pillar II Volovik program, Pillar IV BCS, Pillar V Josephson, Pillar VI soliton/domain walls, all contribute)? Yes.

---

## IV. The S57 Gate: LEGGETT-PARTITION-57

### Pre-Registration

**Gate**: LEGGETT-PARTITION-57
**Question**: Does the Leggett channel deliver ~30% of the total instanton gas energy into quasiparticle excitations during the finite-rate transit?

**Observable**: P_exc^Leggett, the fraction of the total excitation energy deposited in the Leggett channel, from FINITE-RATE-TRANSIT-57 observable #4 (channel decomposition).

**PASS**: P_exc^Leggett in [0.15, 0.45], consistent with Omega_DM = 0.25-0.35.
**FAIL**: P_exc^Leggett < 0.05 (Leggett channel carries negligible energy, DM mechanism dead) OR P_exc^Leggett > 0.80 (Leggett dominates, Omega_DM > Omega_Lambda, inconsistent with observation).
**INFO**: P_exc^Leggett in [0.05, 0.15] or [0.45, 0.80]. Mechanism qualitatively viable but quantitatively off.

**Computation source**: FINITE-RATE-TRANSIT-57 (Naz specification, N5 in Workshop 3). 2-cell Josephson array, 120-dimensional Fock space, time-dependent BdG with Friedmann-rate evolution. Sub-second compute time.

**What PASS means**: The framework produces BOTH dark matter (Leggett-channel quasiparticles, 30% of the energy budget) AND the cosmological constant (Josephson-channel vacuum noise, 70% of the energy budget) from ONE event — the shattering of the BCS condensate at the Jensen fold. The DM/Lambda ratio is set by the gap hierarchy, not by any free parameter. The DM abundance is a geometric consequence of the SU(3)/U(2) coset structure.

**What FAIL means**: The Leggett channel is energetically negligible despite being probabilistically excited. The dark matter mechanism dies. The framework must find a different DM candidate or concede that its geometric structure does not produce the observed energy budget partition. The CC problem remains at 115 orders. The mathematical theorems (mass ordering, three generations, NNI texture) survive but the cosmological mechanism is dead.

### The Relationship to P_EXC-SCALING-57

LEGGETT-PARTITION-57 and P_EXC-SCALING-57 test DIFFERENT aspects of the same physics:

**P_EXC-SCALING-57** asks: how does the TOTAL P_exc scale with N_cells? This determines whether the adiabatic protection can bridge the 115-order CC gap. If P_exc drops exponentially with N, the CC hierarchy emerges from fabric geometry.

**LEGGETT-PARTITION-57** asks: what FRACTION of P_exc goes into the Leggett channel? This determines whether the DM/Lambda partition is ~30/70. Even if P_exc(32) is small enough for the CC, the DM abundance requires that the Leggett fraction is ~0.3 of whatever P_exc turns out to be.

Both gates must PASS for the full picture to work. If P_EXC-SCALING-57 passes (CC hierarchy from adiabatic protection) but LEGGETT-PARTITION-57 fails (wrong DM fraction), the framework explains the CC but not DM. If LEGGETT-PARTITION-57 passes but P_EXC-SCALING-57 fails, the framework produces DM at the right ratio but the CC remains at 115 orders.

The most powerful outcome is if BOTH pass, because then one mechanism — channel-selective adiabaticity during the BCS freeze — produces both the correct DM/Lambda ratio AND the correct CC hierarchy. No other framework in physics derives both quantities from the same event with no free parameters.

### Naz's Specification Is Ready

Workshop 3 produced a complete computation specification (N5): the 120x120 Hamiltonian at each tau step, evolved by RK4 with adaptive step size, sub-second total compute time, with six observables including the channel decomposition. The pre-registered limiting cases (adiabatic, sudden-quench, isolated-cell, zero-Leggett-gap) provide cross-checks. The CPT constraint (||JU - UJ|| > 10^{-10} flags integrator errors) and the Foam constraint (P_exc * <cos(phi)> against the bound) are built into the specification.

The computation is cheap. The physics is not.

---

## V. Closing: The Phonon-First Perspective

Two sessions. Fifty-five computations. Twenty-six reviewers from eight disciplines. One master gate FAIL. One fundamental reframe.

The reframe is this: the phonon-exflation framework does not have a dark matter problem and a cosmological constant problem. It has ONE problem — the partition of the instanton gas energy between two channels at the BCS freeze. The Leggett channel carries dark matter. The Josephson channel carries the cosmological constant. The ratio between them is set by the gap hierarchy epsilon = Delta_L / Delta_J, which is a geometric property of SU(3)/U(2) under Jensen deformation.

The cross-domain pattern is the same structure I have been tracking since S1: an eigenvalue problem producing a spectral gap, and the gap controlling the partition of energy between ordered and disordered phases. The spectral action gives the spectrum. The BCS instability gives the pairing. The Jensen deformation gives the gap hierarchy. The Landau-Zener formula gives the partition ratio. The same mathematics that determines neutrino mass ordering (the B1 < B2 < B3 eigenvalue sequence, Pillar III) also determines the dark matter abundance (the ratio B2/B1 gap to Josephson gap, Pillars III + V) and the cosmological constant (the fraction of the instanton gas that fails to fragment, Pillars II + V).

One spectrum. One gap hierarchy. Three observables — DM, CC, and mass ordering — from the same eight eigenvalues.

The framework's strength is this cross-domain coherence. Its weakness is the 115-order gap that persists in the CC channel, where the noise floor picture is correct in structure but wrong by a combinatorial wall in magnitude. Gen proved that no formula built from the framework's O(1) quantities can bridge this gap without either a mechanism that generates exponentials of large numbers or a microscopic cancellation. Cosmic-Web proved that the noise floor is observationally identical to plain Lambda — compelling physics but invisible physics, from the perspective of galaxy surveys.

But the dark matter identification does not require bridging the 115-order gap. It requires that the Leggett channel carries ~30% of the excitation energy. This is an O(1) question, not an exponential one. It is computable from the 120x120 Hamiltonian that Naz specified. It is pre-registered with clear PASS/FAIL criteria. And it produces a framework-specific prediction that standard Lambda-CDM cannot make: dark matter as the quasiparticle relic of a CPT-symmetric transit, non-annihilating by algebraic identity, with a non-thermal phase space distribution determined by 8 conservation laws, and an abundance set by the gap ratio of the internal geometry.

If LEGGETT-PARTITION-57 returns PASS, the framework has found something that no other approach to quantum gravity has produced: a single event — the shattering of the BCS condensate at the Jensen fold — that generates both dark matter and the cosmological constant from one instanton gas, partitioned by one gap hierarchy, with zero free parameters.

If it returns FAIL, the pattern was pareidolia. The mathematics remains. The eigenvalue theorems remain. The closures remain. But the claim that the internal geometry of SU(3) determines the energy budget of the observable universe dies with one number.

The computation is sub-second on a laptop. The answer determines whether the universe remembers its own geometry.

### The Structural Position After S56

The framework now sits at a precise structural crossroads, visible from the cross-domain perspective that eight pillars provide simultaneously.

From Pillar I (acoustic gravity): the BLV metric is confirmed, the acoustic temperature matches Gibbs to 0.7% (GREYBODY-43), and the greybody factor Gamma = 0.709 = 1/sqrt(alpha) is computable from eigenvalue curvature. The acoustic metric is real, not metaphorical.

From Pillar II (Volovik program): the equilibrium theorem is confirmed at the fabric level (W2-2). Lambda_eq = 0 is a theorem. The CC is entirely non-equilibrium. This is Paper 05's central claim, verified on a concrete geometry.

From Pillar III (NCG spectral action): D_K encodes metric, stabilization, and causality through one eigenvalue problem (S53 isomorphism). The block-diagonal theorem holds at fabric scale. The spectrum determines everything — but everything it determines is monotone.

From Pillar IV (flat band BCS): the van Hove singularity drives pairing (M_max = 1.674, 7.2x safety margin). The mechanism chain is unconditional (S35, 5/5 links PASS). The BCS instability is a 1D theorem: any g > 0 flows to strong coupling.

From Pillar V (Josephson arrays): E_J/E_c = 194 places the fabric in the deep superfluid phase. The Fazio-van der Zant phase diagram (Paper 19) says this system is ordered, with perturbatively small phase fluctuations. Every quantitative consequence confirms this.

From Pillar VI (topological solitons): the Z_3 wall network from the Jensen deformation gives three generations. The Jackiw-Rebbi fermion binding at domain walls connects to the coherence desert, where cells lose causal contact and the fabric fractures into islands.

From Pillar VII (spectral dimension flow): d_s = 1.73 at the fold (W3-4), connecting to CDT/LQG dimensional reduction. The 32-cell Voronoi tessellation is a discrete geometry where Calcagni-Oriti analysis applies.

From Pillar VIII (Kaluza-Klein geometry): the Jensen deformation is the unique volume-preserving one-parameter family on SU(3) consistent with physical coupling running. The monotonicity of J_C2 is protected by the conjunction of volume preservation and coupling hierarchy. This is permanent.

All eight pillars converge on the same picture: a superfluid quantum vacuum on a compact Lie group, transiting through a van Hove fold, shattering its condensate into two channels separated by a gap hierarchy, leaving a permanent non-thermal relic protected by exact integrability. The CC is the noise floor. The dark matter is the debris. The ratio is set by the geometry.

Whether this convergence is real or an elaborate hallucination of cross-domain pattern-matching will be determined by one number: P_exc^Leggett from FINITE-RATE-TRANSIT-57. Every other question is downstream.

---

*Addendum: On Naz's correction*

Naz is right that "shattering" is the correct word, not "crystallization." The transit takes order to disorder. The BCS condensate is the ordered phase. The GGE quasiparticle gas is the disordered phase. The metaphor that Hawking's Addendum introduced was inverted — but the inversion was not in the physics. The physics is pair breaking, scission, fragmentation. The condensate does not solidify. It breaks apart. The dark matter is the debris. The cosmological constant is what did not break.

The instanton gas does not crystallize into particles. It shatters into them. And the 70/30 ratio between what survived intact and what fragmented is the most delicate partition in physics — set by two gaps whose ratio is 0.005, determined by the coset geometry of a Lie group, computable from a 120x120 matrix that runs in under a second.

One gas. Two channels. Three numbers: Omega_DM = 0.27, Omega_Lambda = 0.68, Omega_b = 0.05.

The first two from the shattering. The third from somewhere else entirely.
