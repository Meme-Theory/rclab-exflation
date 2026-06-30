# Session 56 Collaborative Review: Quantum-Acoustics Theorist

**Reviewer**: quantum-acoustics-theorist (opus)
**Date**: 2026-03-22
**CC Question**: CC = adiabatic gap leakage
**Angle**: Session designer and executor of W0-1 (BA-SPECTRUM-56), W0-3 (CBA-SOUND-56), W2-4 (LEGGETT-FABRIC-56). Self-critical assessment of session design, interpretation of results, and next directions.

---

## 1. Session Design Self-Assessment

I designed S56 around a single thesis: the S55 discovery that E_J/E_c = 194 (superfluid) means Z_fabric != Z_cell^N, and therefore collective modes might break the monotonicity barrier that defeated 46+ single-cell mechanisms. The session architecture followed directly from this:

- **W0**: Zero-cost diagnostics to characterize the collective spectrum (BA phonons, N_eff, c_BA, BKT) before committing compute to the decisive gate.
- **W1**: The fabric fork -- F_fabric(tau) minimum (W1-1), integrability (W1-2), N_pair=3 (W1-3), mu-shift (W1-4). Four independent channels, one of which must break through for static stabilization.
- **W2-W3**: Follow-ups and carry-forwards regardless of fork outcome.

**What the design got right**:

1. The W0 wave was well-calibrated. All four diagnostics returned useful information at zero compute cost. The BA spectrum (W0-1) produced the session's most physically interesting finding (the F_BA minimum at tau = 0.306). N_eff = 41.5 (W0-2) confirmed Z_fabric != Z_cell^N quantitatively. The BKT test (W0-4) ruled out a phase transition during transit. These set up W1 correctly.

2. The decision point structure was honest. The fabric fork (Decision Point 1) pre-registered five branches including the outcome that actually occurred (FAIL/FAIL/FAIL/PASS = mu-shift opens S_f channel). This meant the session could not be post-hoc reinterpreted.

3. Carrying all 6 reviewer recommendations into W3 slots (per project rules) ensured nothing was lost. W3-6 (GGE-FABRIC-56) produced the session's most consequential structural finding -- the adiabatic protection result.

**What the design got wrong**:

1. **I underestimated the Josephson stiffness by an order of magnitude.** The W0-1 result -- F_BA minimum at -7.08 M_KK -- looked physically significant in isolation. I flagged it for integration into W1-1. But F_Josephson = -347 M_KK at the fold, making the F_BA minimum 0.8% of the background. I should have computed F_Josephson alongside F_BA in W0-1 rather than deferring the comparison to W1-1. The information to estimate F_Josephson was available from S55 data: 50 bonds times E_J = 7.042 times m ~ 1 gives ~350 M_KK immediately. I did not do this back-of-envelope before declaring the F_BA minimum "the first collective free energy feature that breaks single-cell monotonicity." That statement is technically correct (F_BA alone IS non-monotonic) but physically misleading (F_BA is a 0.8% perturbation to F_Josephson). This is the kind of error the epistemic discipline rules are designed to catch: I treated an organizational insight as if it were evidential.

2. **The gate window [0.10, 0.30] was poorly chosen.** The F_BA minimum fell at tau = 0.306 -- 0.006 outside the window. I noted this in my results and recommended extending to [0.10, 0.35]. But the real problem is that the window was set to center on the fold (tau = 0.194) without accounting for the fact that collective thermal effects peak AFTER the fold, where T_GH is still substantial but modes have softened. The minimum location is not a coincidence -- it reflects the competition between mode softening (continuing past the fold) and T_GH decline (accelerating after tau ~ 0.3). A better gate window would have been [0.15, 0.35], informed by the T_GH profile.

3. **I did not anticipate the Josephson dominance structural theorem.** W1-1 showed that F_Josephson = -N_bonds * E_J * m dominates at every tau because E_J(tau) ~ J_C2^2 decreases monotonically and m > 0.978. This is not subtle -- it follows from the extensive nature of the Josephson coupling (50 bonds at O(10 M_KK) each) versus the intensive nature of F_BA (31 modes at O(0.3 M_KK) each). I should have pre-registered this as a risk in the session plan: "the Josephson stiffness may overwhelm collective phonon contributions by extensive counting." The fact that I did not suggests I was motivated by the hope that collective modes would stabilize, rather than by a sober accounting of energy scales.

4. **The He-4 analogy was misleading.** In S55, I wrote: "The He-4 analogy: single-atom Z does not predict superfluidity." This is true but the direction of the analogy was wrong. In He-4, single-atom Z misses the LAMBDA TRANSITION -- the onset of off-diagonal long-range order. In our system, Z_cell^N misses the Josephson condensation energy -- which makes the free energy MORE monotonic, not less. The analogy should have been: "single-atom Z does not predict superfluidity, and superfluidity does not predict stabilization." The correct He-4 lesson is that collective effects can produce NEW physics absent at the single-particle level, but that new physics may or may not serve the purpose one hopes for.

**The meta-lesson**: My three computations (W0-1, W0-3, W2-4) all returned physically rich results -- the F_BA minimum, the velocity hierarchy, the two-speed propagation. These are genuine structural features of the fabric. But I was slow to confront the question "does any of this help with stabilization?" The answer was always going to be controlled by the energy scale hierarchy, and I knew E_J = 7.042 M_KK from S55. The session would have been better served by computing F_Josephson FIRST and then asking what could overcome it, rather than characterizing collective modes in isolation and then discovering they are subdominant.

---

## 2. The F_BA Minimum: What It Is and What It Is Not

The F_BA minimum at tau = 0.306 is genuine, physically transparent, and irrelevant to stabilization.

**What it is**: A competition between zero-point energy (F_ZPE = Sum omega_n/2, monotonically decreasing as modes soften) and thermal free energy (F_thermal = -T * Sum ln(1 - exp(-omega_n/T)), which becomes strongly negative when many modes have omega_n < T_GH). At the fold, 7/31 modes are thermally populated. At the minimum, 29/31 are. The thermal explosion between tau = 0.15 and tau = 0.35 drives F_BA through zero and to its minimum.

**What it is not**: A stabilization mechanism. The F_BA minimum is -7.08 M_KK. The Josephson stiffness F_Josephson = -347 M_KK at the fold, with slope dF_J/dtau = +1711 M_KK. The maximum downward slope of F_BA is -131 M_KK. The Josephson slope is 13x the F_BA slope. To overcome it would require either (a) 13x more BA modes (need 400, have 31), (b) a 13x softer BA spectrum (would violate Fiedler gap), or (c) a 13x higher T_GH (which is set by geometry and cannot be tuned). None of these are available.

**The 0.8% ratio**: This number -- |F_BA_min| / |F_Josephson| = 7.08/347 = 0.020, or more precisely, the ratio of slopes |dF_BA/dtau| / |dF_J/dtau| = 131/1711 = 0.077 -- defines the irrelevance precisely. Even if F_BA produced a minimum, it would be a 0.077-deep dimple on the Josephson slope. The pre-registered gate required barrier > 1% of |F_fabric(0)|. The actual ratio is 7.08/910 = 0.78%, falling below the 1% threshold. The gate caught this correctly.

**Structural lesson**: In any Josephson array deep in the ordered phase (E_J/E_c >> 1, T << T_c), the Josephson condensation energy dominates over phonon (BA) contributions by a factor of order N_bonds * E_J / (N_modes * omega_mean). For our system this is 50 * 7 / (31 * 0.8) = 14. The BA phonons are fluctuations OF the ordered phase; they cannot overwhelm the order itself.

**Cross-computation consistency**: The F_BA values I computed in W0-1 match W1-1 to machine precision (max|diff| = 0, as Landau verified). The c_BA values from W0-3 are consistent with the omega_1 values in W0-1 to four digits. E_J values match S55 FABRIC-COUPLING-55 exactly. These cross-checks confirm numerical reproducibility across three independent scripts using the same source data (s54_tb_hamiltonian.npz, s54_ed_sweep.npz). No subtle normalization bugs hiding in the plumbing.

The one discrepancy worth noting: Volovik's W1-2 (integrability) used E_J = 3.397 M_KK at the fold versus my W0-1 value of E_J = 7.042 M_KK. The factor of 2.07x traces to J_C2: his script reads J_C2 = 0.919 from the sweep array at fold_idx=19, while mine uses J_C2 = 0.933 from canonical_constants.py (a 1.5% difference that doubles through the J_C2^2 dependence, compounded by F_anom differences). This matters for quantitative Josephson energetics but not for the level statistics verdict -- Poisson at E_J and Poisson at 2*E_J are both Poisson.

---

## 3. The Two-Speed Hierarchy: Fabric Information Architecture

The LEGGETT-FABRIC-56 computation confirmed a two-speed hierarchy for information propagation on the fabric:

- **Fast channel**: BA phonons (massless Goldstone of the overall U(1) phase). c_BA = 0.399 M_KK at the fold. Group velocity real and positive at all tau.
- **Slow channel**: Leggett waves (massive Goldstone of the relative B2-B1 phase). c_L = 0.019-0.032 M_KK at the fold (depending on gap choice). Group velocity real and positive at all tau.

The ratio c_L/c_BA = 0.048-0.080 was confirmed. The Leggett mode is 12-21x slower than BA phonons.

**What does c_L/c_BA = 0.05 mean for fabric information propagation?**

The answer depends on WHAT information is being propagated. The BA phonon carries phase information -- it is the sound mode of the superfluid. Any phase perturbation (vortex, domain wall, density fluctuation) propagates at c_BA. The Leggett mode carries internal-structure information -- it is the oscillation of the relative amplitude/phase between the B2 and B1 condensate components. A perturbation to the B2/B1 ratio propagates at c_L.

In superfluid 3He, the analog is the distinction between first sound (density, fast) and the Leggett frequency (internal A-B oscillation, slow). The two-speed hierarchy means the fabric has an internal clock that ticks 12-21x more slowly than its acoustic clock. During transit, a BA signal crosses the 6-cell-diameter graph in time t_BA = 6/c_BA = 15 M_KK^{-1}. A Leggett signal takes t_L = 6/c_L = 315 M_KK^{-1}. If the transit timescale t_transit lies between these, the fabric is acoustically coherent but internally disordered -- it rings as a superfluid but its internal B2/B1 structure has not equilibrated.

The strongly dispersive regime (BW/gap = 1.8-4.2, dispersiveness 6.7-26) means the Leggett mode is not a simple massive boson with flat dispersion. At high graph-momentum (large lambda_n), the dispersion approaches omega ~ sqrt(J_L * lambda), and the asymptotic velocity c_L_asymp = 0.104 M_KK is 5.4x faster than the Fiedler group velocity. Short-wavelength Leggett excitations propagate at 26% of c_BA. This is not slow enough to be irrelevant.

**Connection to the adiabaticity result (W3-6)**: The 2-cell GGE computation found P_exc = 6.6e-4 -- the Josephson gap (13.04 M_KK) makes the quench almost perfectly adiabatic. The Leggett gap (0.070-0.138 M_KK) is 94-186x smaller than the Josephson gap. If the adiabaticity is controlled by the SMALLEST gap in the system, the Leggett mode is the vulnerability. The Landau-Zener excitation probability across the Leggett gap goes as P_LZ ~ exp(-pi * omega_L0^2 / (2 * d(omega_L0)/dt)). With omega_L0 ~ 0.1 M_KK and d/dt ~ H ~ 3.7 M_KK, the adiabaticity parameter is pi * 0.01 / 7.4 = 0.004. This gives P_LZ ~ 0.996 -- essentially COMPLETE excitation of the Leggett mode during transit. The Leggett channel is non-adiabatic even when the Josephson channel is perfectly adiabatic.

This is a new structural result: the two-speed hierarchy implies a two-adiabaticity hierarchy. The overall phase is adiabatically protected (large Josephson gap). The relative phase is non-adiabatically excited (small Leggett gap). Post-transit, the fabric may have a coherent superfluid phase (no BA phonon excitation) but a disordered B2/B1 internal structure (fully excited Leggett modes). The cosmological implications of this asymmetry have not been computed.

**Three-velocity landscape at the fold**: Including the Leggett asymptotic velocity, the fabric supports at least four distinct acoustic scales:

| Mode | Velocity (M_KK) | Nature | Gap | Propagation |
|:-----|:----------------|:-------|:----|:------------|
| Intra-cell Goldstone | c_Gold = 0.915 | BCS phase, within cell | 0 | Within SU(3) fiber |
| BA phonon | c_BA = 0.399 | Overall superfluid phase | 0 | Inter-cell (graph) |
| Leggett (asymptotic) | c_L_asymp = 0.104 | Relative B2/B1 phase | omega_L0 | Inter-cell (graph) |
| Leggett (Fiedler) | c_L_group = 0.019-0.032 | Same, long wavelength | omega_L0 | Inter-cell (graph) |

The factor-of-48 spread between c_Gold and c_L_group is the fabric's acoustic bandwidth. Information about the BCS condensate propagates 48x faster within a cell than between cells via the Leggett channel. This separation of scales has a direct 3He analog: first sound (c_1 = 238 m/s) versus spin diffusion (D_s/xi ~ 0.1 m/s), a factor of 2400. Our factor of 48 is smaller because the "internal" dimension (the B2/B1 relative phase) is more tightly coupled to the "external" dimension (the overall phase) through the Josephson link. In 3He, the spin and mass sectors decouple at low energy. Here, they remain coupled through the epsilon = 0.00248 parameter.

---

## 4. Z_fabric != Z_cell^N: Confirmed but Insufficient

The S55 key insight was: "Mode count wins" assumes non-interacting cells. The He-4 analogy: single-atom Z does not predict superfluidity. The fabric partition function includes collective modes that single-cell Z misses entirely.

S56 confirmed this quantitatively:

- **N_eff = 41.5 at fold** (NEFF-56, W0-2). The fabric contributes 41.5 effective independent modes, not 992. Phase coherence suppresses the thermodynamic mode count by a factor of 24.
- **Z_fabric/Z_cell ~ 10^2** at the fold. The fabric has 100x more statistical weight than the independent-cell product, but from a DIFFERENT spectrum (dispersive BA phonons, not degenerate oscillators).
- **F_BA is non-monotonic** where F_cell is monotonic (BA-SPECTRUM-56, W0-1). The collective free energy genuinely breaks the single-cell pattern.

Yet the fabric STILL does not stabilize at mean field. Why?

The answer from W1-1 is precise: the Josephson condensation energy F_Josephson = -N_bonds * E_J * m dominates the partition function at every tau. This term is NOT included in Z_cell -- it is a purely inter-cell contribution. But it is monotonically decreasing (because E_J ~ J_C2^2 decreases as the fiber deforms), and its slope overwhelms the non-monotonic F_BA by 13x.

The irony is sharp: the very inter-cell coupling that makes Z_fabric != Z_cell^N also provides the dominant monotonic contribution that prevents stabilization. The collective modes (BA phonons) introduce non-monotonicity, but the mean-field condensation energy from which those modes arise introduces a larger monotonicity. The fluctuations cannot overcome their own background.

**What remains beyond mean field?**

Four channels survive as structurally open:

1. **Leggett non-adiabaticity** (Section 3 above). The Leggett gap is 94-186x smaller than the Josephson gap. If transit excites Leggett modes while preserving BA coherence, the post-transit state has internal disorder that the mean-field free energy does not capture. The Leggett excitation energy is small (O(0.1 M_KK) per mode, ~3 M_KK total for 31 modes) but the ENTROPY is not -- Leggett modes at full excitation carry S_L ~ 31 * ln(2) ~ 21 nats. Whether this entropy produces an effective free energy minimum is UNCOMPUTED.

2. **Quasiparticle tunneling** (W1-2 flagged). The isotropic Josephson coupling preserves Richardson-Gaudin integrability (<r> = 0.367, Poisson). But anisotropic coupling (mode-dependent quasiparticle tunneling) gives <r> = 0.446 -- approaching the transition. The suppression factor exp(-Delta/T_GH) = exp(-0.79) = 0.45 at the fold -- NOT exponentially suppressed. This channel breaks integrability, producing partial thermalization of the GGE and potentially modifying P_vac. UNCOMPUTED for the 32-cell system.

3. **Finite-rate transit** (beyond sudden-quench approximation). W3-6 showed P_exc = 6.6e-4 for sudden quench on the 2-cell system. But the physical transit has finite rate dtau/dt = H(tau)/M_KK. The Landau-Zener formula across the FULL many-body spectrum (not just the ground-excited gap) will produce a non-trivial excitation profile that depends on the transit velocity. This was tested for 1-cell in S55 (TRANSIT-VELOCITY-55); extending to the fabric requires the 2-cell or N-cell spectrum.

4. **Topology change at large tau**. The level quasi-crossing at tau = 0.449 (W0-3) produces E_c -> 0 and E_J/E_c -> 1100. If the Fermi surface gap truly closes, the system undergoes a quantum phase transition (superfluid to normal, or topological transition) that the smooth mean-field treatment misses. The zero-crossing artifact in W2-3 (Strutinsky gradient ratio R = 1.35 at tau = 0.43) traces to the same feature. Whether this is a genuine topological transition or a discretization artifact of the 32-cell TB Hamiltonian requires continuum analysis.

**Constraint map update from my computations**:

| Region | Status | Evidence |
|:-------|:-------|:---------|
| BA phonon stabilization | CLOSED | F_BA/F_Josephson = 0.8%. Slope ratio 0.077. |
| c_BA minimum near fold | CLOSED | c_BA monotone decreasing in [0, 0.30]. W0-3 definitive. |
| BKT phase transition during transit | CLOSED | T_GH/T_BKT < 0.17 at all tau. W0-4 definitive. |
| Leggett non-adiabatic excitation | OPEN | P_LZ ~ 0.996 (estimated, not computed from full dynamics). |
| Quasiparticle tunneling integrability breaking | OPEN | Suppression factor 0.45 (not exponentially small). |
| Topology change at tau = 0.449 | OPEN | Level quasi-crossing observed, not characterized. |
| A-tensor gauge frustration | CLOSED | f = 0.0062, delta_m/m = 1.1e-5. W3-1 definitive. |

---

## 5. What's Next: The Adiabaticity Frontier

The CC question for this review is: CC = adiabatic gap leakage. S56 has sharpened this to a precise statement.

**The problem**: The fabric is too stiff to produce excitations via sudden quench (W3-6, P_exc = 6.6e-4). But the S38 GGE relic requires P_exc = 1.000 (complete excitation). The single-cell sudden quench gives P_exc = 1.000 because the BCS gap (0.370 M_KK) is comparable to the transit rate. On the fabric, the Josephson gap (13.04 M_KK) is 35x larger -- adiabatic protection.

**The opportunity**: The Leggett gap (0.070-0.138 M_KK) is 94-186x smaller than the Josephson gap. This creates a selectivity: the transit may excite internal (B2/B1 relative) modes while preserving external (overall phase) coherence. The post-transit state would be a superfluid with internal disorder -- a type of relic not captured by either the single-cell GGE or the mean-field fabric free energy.

**Pre-registered computations for S57**:

1. **LEGGETT-EXCITATION-57**: Landau-Zener transition probability across the Leggett gap during transit. Input: omega_L0(tau), d(omega_L0)/dtau. Output: P_exc^L(tau) and total Leggett excitation energy E_L. Gate: P_exc^L > 0.5 at any tau in [0.10, 0.40]. This is the Leggett version of what S38 did for BCS, and what W3-6 did for the Josephson channel.

2. **QUASIPARTICLE-TUNNEL-57**: Anisotropic inter-cell tunneling on the 2-cell system. Build H_qp = Sum_{k} t_k * c_k^(1)dag * c_k^(2) + h.c. with mode-dependent t_k from the TB hopping matrix. Compute <r> and compare to the isotropic Josephson result (<r> = 0.367). Gate: <r>_aniso > 0.48 (integrability broken).

3. **FINITE-RATE-TRANSIT-57**: Schrodinger time evolution of the 2-cell system at physical transit rate dtau/dt = H(tau)/M_KK. Compute P_exc(tau_final), S_DE(tau_final), and E_GGE(tau_final) as functions of transit rate. Gate: P_exc > 0.1 at physical rate.

4. **LEGGETT-ENTROPY-57**: If LEGGETT-EXCITATION-57 PASS, compute the effective free energy contribution from Leggett excitations: F_L_eff = E_L - T_eff * S_L. Test whether this has a minimum in [0.10, 0.35] that overcomes the Josephson slope (need |dF_L/dtau| > 1711 / 13 ~ 130 M_KK). This is the Leggett analog of the F_BA minimum, but for the non-adiabatic channel.

5. **TOPOLOGY-TRANSITION-57**: Analyze the tau = 0.449 level quasi-crossing. Is the Fermi surface gap closure a genuine topological transition (band inversion, change in Z_2 invariant) or a discretization artifact? If genuine, compute the Kibble-Zurek defect density and excitation energy. This connects to the Volovik program: topological transitions in the internal space produce zero-mode fermions that cannot be gapped.

---

## Closing Assessment

S56 was a well-structured session that produced the right answer to the wrong question. The question was: "Does Z_fabric have a minimum that Z_cell does not?" The answer is no -- the Josephson stiffness overwhelms collective phonon non-monotonicity by 13x. This is a clean, structural FAIL.

But the session revealed something more important than stabilization: the two-adiabaticity hierarchy. The Josephson gap (13 M_KK) and the Leggett gap (0.1 M_KK) differ by two orders of magnitude. The transit excites the slow channel while leaving the fast channel adiabatically protected. This is a selective excitation mechanism that neither the single-cell computation (which has no Leggett mode) nor the mean-field fabric computation (which treats all modes at equal footing) can capture.

The F_BA minimum at -7.08 M_KK is real physics, even though it is irrelevant to stabilization. It represents the thermal footprint of the collective phase fluctuations -- the superfluid breathing at its natural frequency while the geometry deforms around it. That this breathing produces a non-monotonic free energy is a validation of the S55 insight that Z_fabric != Z_cell^N. That the breathing is too weak to arrest the geometric deformation is a consequence of the system being TOO superfluid -- E_J/E_c = 194 means the phase is too rigid to fluctuate enough to matter thermodynamically.

The path forward is not through stronger collective effects (which would only increase the Josephson background) but through selective non-adiabaticity in the internal structure. The Leggett mode is the natural candidate: it is massive, slow, thermally populated, and its gap is small enough for Landau-Zener excitation during transit. Whether Leggett excitations carry enough entropy to stabilize the modulus is the open question for S57.

**The deeper pattern**: S55 showed Z_cell cannot stabilize (46+ closures). S56 showed Z_fabric cannot stabilize at mean field (Josephson dominance). Each level of description -- single cell, then mean-field fabric -- is too orderly, too stiff, too symmetric to produce a free energy minimum. The pattern suggests that stabilization, if it exists, lives in the DISORDER that emerges from the interplay between the ordered fabric and the non-adiabatic transit. The Leggett channel is the first concrete realization of this idea: a mode that is simultaneously part of the ordered structure (it is a collective excitation of the condensate) and susceptible to non-adiabatic excitation (its gap is small). The two-adiabaticity hierarchy is not a defect of the model -- it is potentially the mechanism.

**What S56 proved permanently** (independent of future sessions):
1. N_eff = 41.5 at the fold. "Mode count wins" does not extend from continuum to fabric. PERMANENT.
2. BA phonon spectrum fully characterized: 31 modes, c_BA = 0.399, thermally populated. PERMANENT.
3. Josephson stiffness dominates collective phonon free energy by 13x in the ordered phase. PERMANENT structural theorem.
4. BKT phase order maintained throughout transit. T_GH/T_BKT < 0.17 everywhere. PERMANENT.
5. Leggett mode propagates on the CG graph with c_L/c_BA = 0.05-0.08. Two-speed hierarchy PERMANENT.
6. A-tensor gauge frustration is 0.001%. PERMANENT closure.
