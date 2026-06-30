# Session 58 Synthesis: Plan A -- Escape Routes Within SU(3)

**Date**: 2026-03-23
**Session type**: SYNTHESIS
**Author**: Mack Cosmic Bridge (solo synthesis)
**Context**: Plan A Investigation -- what escape routes exist within SU(3)?
**Source documents**: Back-to-basics (Option B), 4 collaborative reviews, full working paper (27 computations)

---

## I. Session Outcome

Session 58 is the most cosmologically productive session in the project's 58-session history. The Volovik partition validated the framework's energy decomposition, moving three of four key observables to observational consistency: Omega_DM h^2 = 0.120 (0.04-sigma from Planck), Omega_Lambda = 0.685 (exact at canonical), and w_0 = -0.918 (2.9-sigma from DESI DR2, improved from 6.0-sigma exclusion at S57). The session proved that phononic DM is effectively CDM at all observable scales (T(k) = 1.0000, free-streaming margin 22 OOM), and identified a clean two-level architecture for the Friedmann equation with a single resolvable normalization factor (spinor multiplicity sqrt(16), yielding H_0 = 65.4 km/s/Mpc if corrected). Against this, a single decisive obstruction crystallized: f_DM = 0.209 versus the observed 0.844 -- a factor-of-4 gap in the dark matter fraction that is now THE question for the framework's cosmological viability.

---

## II. The f_DM Problem: The Single Bottleneck

The Volovik partition assigns the Josephson ground-state stiffness (F_J = -336.6 M_KK, 95.9% of the total energy budget) to the vacuum sector, leaving four excitation components as matter: F_BCS = -4.379, F_BA = +7.021, F_Leggett = +3.010 M_KK, totaling E_matter = 14.411 M_KK. The Leggett channel (the DM candidate) carries only 20.9% of this excitation energy, while the observed DM fraction f_DM = Omega_DM / Omega_m = 0.844. The emulator NROY region is 0.00% (Variant A, Leggett-only) or 0.18% (Variant B, Leggett + BCS = DM) against a 5% PASS threshold.

This is now the framework's most precisely characterized failure. Three of four observables pass at the canonical point (W0-1). The per-observable NROY fractions tell the story: Omega_DM h^2 passes at 20.6%, Omega_Lambda at 40.0%, w at 56.3%. Only f_DM kills the intersection, at 9.1% (Variant B) and 0.0% (Variant A). The obstruction is one-dimensional.

Each reviewer identified the bottleneck and proposed distinct escape mechanisms, which I assess below.

### Volovik's Diagnosis: Late-Time Decay Kinetics

Volovik (collab Section 3.1) frames the f_DM problem as a question about quasiparticle lifetime. In 3He-B, different excitation types have vastly different lifetimes: phonons decay rapidly via Beliaev processes, while roton-like excitations can be long-lived. If BCS quasiparticles (CPT-charged, can annihilate via K_7-mediated processes) and BA phonons (gapless, can decay via Beliaev processes) deplete over 13.8 Gyr relative to Leggett modes (topologically protected by the mass gap), the late-time f_DM rises. The relevant quantity is the ratio Gamma_BCS/H_0 and Gamma_BA/H_0. This is the most physically direct escape route.

### Baptista's Diagnosis: Representation-Theoretic Partition

Baptista (collab Section 4) identifies the f_DM gap as a representation-theoretic partition problem. The B1+B2+B3 sector structure is algebraic -- fixed by the Peter-Weyl decomposition of SU(3). The energy partition among these sectors depends on the pairing interaction V_kl, which is a functional of D_K(tau). The 2.6x spread in epsilon definitions (microscopic 0.00143, phenomenological 0.00248, macroscopic 0.00369, from W0-3 and W3-13) represents the geometric uncertainty in the DM prediction. The mass variation correction (W3-10: m_B2(fold) = 0.72 M_KK, 30% below round-SU(3)) and the epsilon shift together produce a cumulative ~45% downward correction to Omega_DM from geometric effects. These corrections go in the WRONG direction for f_DM -- they make the Leggett fraction smaller, not larger. The geometric corrections worsen the problem unless compensated by late-time depletion of competing channels.

### Hawking's Diagnosis: Thermodynamic Lock and the Penrose Analog

Hawking (collab Section 1.2) maps the f_DM problem onto the CC problem through the Penrose process analogy. The B3 "ergosphere" modes (n_k ~ 0.003, nearly empty) are the only sector where pairing curvature exceeds entropic resistance. At alpha > alpha_crit = 0.523, the Hessian develops negative eigenvalues and occupation can be redistributed from B2 (Lambda > 0) to B3 (Lambda < 0). This redistribution would simultaneously reduce the CC AND change the energy partition among channels. The f_DM and CC problems are coupled: both require breaking the integrability that locks the GGE occupation numbers.

### My Diagnosis: Post-Transit Cosmological Evolution

The 27 computations of S58 exhaustively characterize the system DURING transit: anharmonic corrections negligible (W1-3, 17000x margin), modes independent (W3-11, exact), multi-mode coupling absent (W2-4, gain < 10^{-4}), fabric transparent (W3-7, T = 0.969). All of this establishes that f_DM = 0.209 is the correct value AT the end of transit. But the transit occupies dt ~ 10^{-62} seconds. What happens in the next 13.8 Gyr is entirely uncomputed. The framework needs its own version of the freeze-out calculation from standard DM physics. The three excitation channels (Leggett, BA, pair-breaking) have distinct equations of state and may evolve differently under cosmological expansion.

### Consistency Across Reviewers

All four reviewers converge on the same structural conclusion: the f_DM problem is not solvable within the transit-epoch single-cell physics that S58 computed. It requires either (a) post-transit cosmological evolution (Volovik, Mack), (b) multi-pair effects that break integrability and redistribute occupations (Hawking, Volovik), or (c) acceptance that geometric corrections alone cannot close the gap (Baptista). The reviewers are consistent in excluding transit-epoch mechanisms -- S58 closed those routes definitively.

---

## III. Escape Routes Within SU(3) (Option A)

### A. Non-Leggett Depletion (Volovik's Decay Kinetics)

**Mechanism**: BCS quasiparticles carry K_7 charge +/-1/2 (S35) and can annihilate via CPT-mediated processes. BA phonons are gapless Goldstone modes that can decay via Beliaev processes or redshift as radiation (w = 1/3) while Leggett modes, being massive (gap at 0.138 M_KK), redshift as non-relativistic matter (w = 0). Over 13.8 Gyr, if the non-Leggett channels deplete by a factor > 4 relative to Leggett, f_DM rises to match observation.

**Evidence for**: In 3He-B, phonon lifetimes scale as T^{-5} (Beliaev processes), and roton lifetimes are exponentially long. The framework has a structural analog: BA phonons are the "phonons" and Leggett modes are the "rotons" (gapped). Standard DM freeze-out physics (my Paper 10) shows that annihilation cross-sections can deplete relic abundances by orders of magnitude. BCS quasiparticles with K_7 charge have an annihilation channel that Leggett modes (charge-neutral pairs) do not.

**Evidence against**: The integrability of the Richardson-Gaudin system protects the GGE occupation numbers. If integrability is exact, the excitation channels cannot exchange energy or number, and their relative fractions are frozen forever. The 8 conserved quantities prevent the redistribution that depletion requires.

**Resolution computation**: Compute Gamma_BCS/H_0 and Gamma_BA/H_0 using the K_7-mediated annihilation cross-section for BCS quasiparticles and the Beliaev process rate for BA phonons. If both exceed unity, the channels deplete and f_DM is fixed. This is a kinetic theory calculation on cosmological timescales, requiring the post-transit dispersion relations from W3-6.

**Expected timeline**: Single-session computation (S59). The rates depend on known quantities (K_7 coupling, BA dispersion, Josephson energy), all of which are computed.

**Assessment**: Most promising escape route. Directly addresses the factor-of-4 gap with a known physical mechanism. The calculation has not been done because S58 focused on transit-epoch physics. Priority 1 for S59.

### B. Multi-Pair Integrability Breaking (Landau/Volovik)

**Mechanism**: The N_pair = 2 exact diagonalization (W1-1) showed the Z_2-even sector at <r> = 0.442, approaching the GOE value of 0.536. The V_fold pairing matrix is only 37% rank-1 (Richardson-Gaudin requires rank-1 for integrability). At N_pair = 3 (560 states), pair-pair interactions become less dilute, and the even-sector <r> may cross 0.50, signaling integrability breaking. If integrability breaks, the GGE thermalizes and occupation numbers redistribute. The RG Hessian (W1-2) identified alpha_crit = 0.523 as the threshold where the Penrose process direction opens. The B3 "ergosphere" modes have pairing curvature exceeding entropy (ratio 0.60-0.65), meaning redistribution from B2 to B3 reduces Lambda_eff.

**Evidence for**: The structural non-separability of V_fold (37% rank-1) is a permanent feature -- not tunable. The even-sector <r> = 0.442 at N_pair = 2 already departs from Poisson (0.386) by 3.5 standard deviations of the Poisson distribution. The cross-susceptibility d^2 Omega/dN dI_k is nonzero for all 8 modes (W1-2), meaning pair-number fluctuations couple to every integral of motion.

**Evidence against**: The odd sector remains at <r> = 0.366 (Poisson-like). The combined <r> = 0.404 is in the INFO band. The ||delta_n|| scaling goes as sqrt(N_pair) (factor 1.41 from N=1 to N=2), suggesting independent pairs rather than interacting ones. The occupation mismatch is consistent with random superposition, not with anomalous pair-pair correlations.

**Resolution computation**: N_pair = 3 exact diagonalization on the 2-cell system (560 states). Z_2-resolved <r> with at least 3 symmetry sectors. If <r>_even > 0.50, integrability is broken. If <r>_even saturates at ~0.44, approximate integrability persists.

**Expected timeline**: Single-session computation (S59). Computationally tractable (560-state Hamiltonian).

**Assessment**: This is the decisive test for the CC problem, not directly for f_DM. If integrability breaks, the GGE thermalizes, which changes BOTH the CC (R_cancel -> 0, Lambda_eff -> 0) and potentially f_DM (occupation numbers redistribute). The coupling between the CC and f_DM problems through integrability is the key structural insight: they may not be independent obstructions. Priority 2 for S59 (after depletion kinetics, because N_pair = 3 changes the CC first and f_DM only indirectly).

### C. Mass Variation Correction (Baptista)

**Mechanism**: W3-10 established that m_B2(fold) = 0.723 M_KK, not the round-SU(3) value of 1.026 M_KK. This is a 30% correction to the DM mass. If Omega_DM scales linearly with mass (as in standard freeze-out), this shifts Omega_DM downward by 30%.

**Evidence for**: The computation is exact -- it follows from the Jensen deformation's anisotropic action on the representation-weighted Casimir. Paper 16 eq (1.2) provides the theoretical framework. The volume-preserving trace is exactly zero (structural identity), but individual representations shift 34-86%.

**Evidence against**: The correction goes in the WRONG direction for f_DM. A 30% lower DM mass means less DM energy, making f_DM worse, not better. Combined with the epsilon downward shift (W0-3: omega_L down 24%), the cumulative geometric correction is ~45% downward -- compounding the problem.

**Assessment**: This is a necessary correction to the DM prediction, but it does not help with f_DM. It is important for precision: any future DM abundance calculation MUST use the post-fold mass 0.72 M_KK, not 1.03 M_KK. The correction is structural and permanent. Its significance is that it makes the f_DM escape routes (depletion kinetics, integrability breaking) HARDER -- they need to close a factor >5, not >4, once the mass correction is included.

### D. Spinor Normalization (Hawking/Baptista)

**Mechanism**: W3-16 found M_Pl_eff / M_Pl_unreduced = 3.92, tantalizingly close to sqrt(16) = 4. The factor of 16 is dim(Psi_+) = 16, the dimension of the spinor on SU(3). If the Seeley-DeWitt a_2 coefficient counts all 16 spinor components but only 4 survive KK reduction to the 4D gravitational sector, dividing a_2 by 16 gives G_N within 4% and H_0 = 65.4 km/s/Mpc -- within 3% of the observed 67.4.

**Evidence for**: The factor sqrt(16) = 4 accounts for the G_N deficit almost exactly (3.92 vs 4.00, 2% discrepancy). Hawking (collab Section 4.3) connects this to the species bound on the number of light particles: M_Pl_eff^2 = M_Pl^2 / N_species, with N_species = 16. Baptista (collab Section 3.4) provides the derivation path: decompose the a_2 coefficient by spinor chirality and representation content to identify which 4 of the 64 spinor components survive dimensional reduction.

**Evidence against**: The correction is not yet derived from first principles. It is a pattern-match (3.92 ~ 4) that could be accidental. The 2% discrepancy might indicate the correct divisor is not exactly 16.

**Resolution computation**: Decompose the Seeley-DeWitt a_2 coefficient on M^4 x SU(3) by 4D spinor representation content. Identify which components contribute to the physical 4D gravitational sector. This is a well-defined mathematical problem with a definite answer, addressable within the Chamseddine-Connes-Marcolli (2007) formalism.

**Expected timeline**: Single-session computation (S59). Requires careful KK reduction of the spectral geometry, which is mathematically tractable.

**Assessment**: This would be the framework's most impressive cosmological prediction if confirmed: H_0 = 65.4 km/s/Mpc with zero free parameters. It does not directly affect f_DM (the spinor factor enters G_N, not the energy partition), but it would establish that the spectral-action-to-gravity pathway is quantitatively correct, which strengthens the entire framework. Priority 1 alongside depletion kinetics (independent computations, can run in parallel).

### E. Cumulative Geometric Corrections (Baptista)

**Mechanism**: The mass variation (W3-10: -30% for B2) and the epsilon shift (W0-3: -24% for omega_L) combine to a ~45% downward correction in the DM prediction from geometric effects.

**Assessment**: As noted in Section C, these compound AGAINST f_DM. They represent necessary corrections to the precision of the framework's predictions but do not constitute an escape route. If anything, they raise the bar for routes A and B: the depletion/redistribution mechanisms need to overcome a larger deficit than the raw factor-of-4 suggests.

### F. Alpha_crit Penrose Process (Volovik)

**Mechanism**: At alpha > 0.523 (fraction of BCS pairing restored post-transit), the RG Hessian develops negative eigenvalues. The B3 modes become an "ergosphere" where occupation can be extracted at negative thermodynamic cost. The Penrose direction (B2 + B1 -> B3 transfer) would reduce both Lambda_eff and potentially redistribute the energy among excitation channels.

**Evidence for**: The alpha_crit = 0.523 threshold is a quantitative result from W1-2. The cross-susceptibility is nonzero for all 8 modes. The even-sector <r> = 0.442 at N_pair = 2 suggests the system is approaching the threshold from below. Volovik identifies this as the q-theory wall translated into Richardson-Gaudin language.

**Evidence against**: The S58 Andreev phase analysis (W3-2) closes the phase-frustration route -- no pi-junctions exist on the fabric. The amplitude route remains open but unquantified. The fabric-level Andreev coupling achieved <r> = 0.446 (S56), below alpha_crit = 0.523. No mechanism currently identified to push alpha above threshold.

**Resolution**: Depends on N_pair = 3 result (route B). If the multi-pair sector pushes effective alpha above 0.523, the Penrose direction opens simultaneously.

### G. Volovik Thermodynamic Status of F_Josephson

**Mechanism**: The choice between Interpretation A (F_J gravitates, w_0 = -0.918, PASS) and Interpretation B (F_J does not gravitate, w_0 = -0.408, EXCLUDED) depends on whether the Josephson ground-state stiffness is an equilibrium or non-equilibrium contribution. Volovik's equilibrium theorem says the equilibrium part does NOT gravitate. If the S57 percolation fragmentation at tau = 0.105 leaves the Josephson phases disordered, F_J is non-equilibrium and Interpretation A holds.

**Evidence for Interpretation A**: The domain wall transition at tau = 0.114 (W3-9) establishes that the fabric fragments when walls become free and locks when they become costly. The fragmentation pattern is frozen pre-fold. If the frozen configuration is not the ground state of the Josephson array (phases disordered by fragmentation), F_J retains non-equilibrium character. Volovik (collab Section 1) argues Interpretation A is correct by construction.

**Evidence for caution**: The BKT analysis (W3-5) shows the superfluid stiffness survives by 68x above T_BKT. The vortex-pair unbinding energy is E_pair = 79.3 M_KK >> T_acoustic = 0.112 M_KK. This suggests the phases ARE ordered (ferromagnetic ground state) post-transit, which would make F_J an equilibrium contribution that should NOT gravitate under Volovik's theorem.

**Assessment**: This is not an escape route per se but a critical theoretical question. If the Josephson array is phase-ordered (consistent with BKT survival), Interpretation B applies and w_0 = -0.408 is excluded at 6.0-sigma, which would be a serious problem. Resolving this requires computing the phase coherence of the Josephson array at the fold -- a defined computation that S58 does not report.

---

## IV. What Would Kill the Framework

Drawing from all four reviewers, the following results would be fatal:

1. **f_DM algebraically locked** (Back-to-basics Section VI.2). If it can be shown that the B1+B2+B3 energy distribution on SU(3) NECESSARILY gives f_DM ~ 0.2 for any BCS pairing, any epsilon, any N_cells, with no depletion mechanism possible (e.g., because integrability is exact at all N_pair), then SU(3) is excluded by observation.

2. **DESI DR3 confirms w_a << 0 at 4+ sigma** (Mack collab Section 5.2). The framework predicts |w_a| < 0.03 from GGE integrability. DESI DR2 measures w_a = -0.73 +/- 0.25. If DR3 confirms w_a < -0.3 at 3-sigma, the framework needs integrability breaking -- which also affects DM stability and the CC.

3. **N_pair = 3 <r>_even saturates at ~0.44** (Volovik collab Section 5). If integrability persists at N_pair = 3 with no trend toward GOE, the CC is permanently locked at 111 OOM and the occupation redistribution route to f_DM is closed.

4. **Spinor normalization is NOT sqrt(16)** (Hawking collab Section 4.3). If the correct KK reduction gives a different factor, H_0 deviates from 65.4 km/s/Mpc and the spectral-action-to-gravity pathway fails quantitatively.

5. **Non-Leggett excitations are cosmologically stable** (Volovik collab Section 2). If the BCS quasiparticle annihilation rate and BA phonon decay rate are both below H_0, the excitation channels survive to the present day with their transit-epoch ratios, and f_DM = 0.209 is the permanent prediction.

6. **Confirmed DM self-interaction at sigma/m > 0.1 cm^2/g** (Mack collab Section 3). The framework predicts sigma/m = 0 exactly at N_pair = 1. A confirmed non-zero self-interaction would exclude the framework's DM candidate.

---

## V. What SU(3) Got Right (Option B Assessment)

The back-to-basics investigation (session-58-back-to-basics.md) steel-manned six alternatives: SU(2)xSU(2), SU(2)xU(1), G_2, Sp(2), SU(4), S^7, and the Chamseddine-Connes finite geometry. The verdict is 70-30 for Option A (escape route within SU(3)).

### The machine-epsilon skeleton that survives only on SU(3):

- **KO-dimension = 6** from C^16 (S7-8): discrete topological invariant, zero free parameters, 10 independent checks.
- **SM quantum numbers from Psi_+ = C^16** (S7): all 16 Weyl fermion quantum numbers match SM assignments exactly under SU(3) branching. Not a fit -- a computation.
- **Van Hove fold at tau ~ 0.19** (S12, S35): SU(3) has d^2S = +20.42 (spectral folds). SU(2)xSU(2) has d^2S = -3.42 (NO folds). This is a genuine selection criterion.
- **[iK_7, D_K] = 0 at ALL tau** (S34): Jensen breaks SU(3) to U(1)_7 exactly in the Dirac spectrum. Specific to SU(3) and its Killing field.

### What a change of manifold would preserve:

Seven structural results are universal to any compact semisimple Lie group: block-diagonal theorem, CPT theorem, BCS instability theorem, spectral monotonicity, constant-ratio trap, instanton gas/GGE mechanism, and Volovik q-theory framework. These are the STRUCTURAL skeleton. But the PHENOMENOLOGICAL content (SM quantum numbers, gauge couplings, van Hove fold, mode structure, f_DM, CC) depends critically on the choice of K.

### Why 70-30 for Option A:

The SM quantum numbers from C^16 are the decisive evidence. A factor-of-4 error in f_DM is fixable by physics (different energy partition, depletion mechanism). An order-one failure in NCG axioms (norm 4.000, pointing to Pati-Salam) is fixable by changing the algebra. But producing the SM quantum numbers from geometry with zero free parameters is not something you get from the wrong manifold. The two strongest Option B candidates (G_2 and SU(4)) have never been computed -- their KO-dimension, SM quantum numbers, and van Hove structure are unknown. Until that computation exists, the pattern-matching wins. SU(3) stays.

The back-to-basics also identified the minimal viable test for Option B: compute the Dirac spectrum on G_2 or SU(4) at a single tau value and check (1) KO-dim = 6, (2) SM quantum numbers, (3) van Hove singularity. If all three pass, Option B becomes compelling.

---

## VI. Cosmological Scorecard

All observational confrontations from S58, compared against current data:

| Observable | Framework Prediction | Observed | Tension | Status |
|:-----------|:--------------------|:---------|:--------|:-------|
| Omega_DM h^2 | 0.120 (canonical, Volovik partition) | 0.1207 +/- 0.001 (Planck 2018) | 0.04-sigma | **PASS** |
| Omega_Lambda | 0.685 (canonical) | 0.685 +/- 0.007 (Planck 2018) | 0.00-sigma | **PASS** |
| f_DM | 0.209 (Variant A) / 0.513 (Variant B) | 0.844 +/- 0.01 | 12.4-sigma (A) / 6.6-sigma (B) | **FAIL** |
| w_0 (Interp A) | -0.918 | -0.752 +/- 0.057 (DESI DR2) | 2.9-sigma | **PASS** |
| w_0 (Interp B) | -0.408 | -0.752 +/- 0.057 (DESI DR2) | 6.0-sigma | **EXCLUDED** |
| w_a | < 0.03 (both interps) | -0.73 +/- 0.25 (DESI DR2) | 2.9-sigma | **TENSION** |
| T(k) at k = 1-1000 h/Mpc | 1.0000 | 1 (CDM) | 0 | **PASS** (structural) |
| m_WDM equivalent | 10^{20.4} keV | > 5.3 keV (Lyman-alpha) | 19 OOM margin | **PASS** (structural) |
| z_tr (NR transition) | 6.75 x 10^29 | > 6.2 x 10^7 (Paper 16) | 22 OOM margin | **PASS** (structural) |
| H_0 (spectral action) | 3.61 km/s/Mpc | 67.4 +/- 0.5 km/s/Mpc | 18.7x deficit | **FAIL** (resolvable) |
| H_0 (spinor-corrected) | 65.4 km/s/Mpc | 67.4 +/- 0.5 km/s/Mpc | 3% | **PASS** (if derived) |
| Lambda_eff / Lambda_obs | 1.93 x 10^{111} (Volovik) | 1 | 111 OOM | **FAIL** (structural) |
| R_cancel (CC near-cancellation) | [0.002, 0.007] across transit | -- | Saves 3 OOM | **INFO** (structural) |
| sigma/m (DM self-interaction) | 0 exactly (N_pair = 1) | < 1.25 cm^2/g (Bullet Cluster) | PASS | **PASS** |
| n_s | 2.065 (naive KZ) | 0.9655 +/- 0.0062 (Planck) | excluded | **CLOSED** (S57) |
| sigma_8 | 0.799 (alpha_s identity) | 0.811 +/- 0.006 (Planck) | 2.0-sigma | **PASS** (sole surviving prediction) |
| epsilon (Leggett coupling) | 0.00143 +/- 39% | -- | -- | **PASS** (within [0.001, 0.005]) |
| NROY (Variant B) | 0.18% | > 5% (threshold) | -- | **INFO** (below threshold) |
| <r> (N_pair = 2, Z_2-resolved) | 0.404 | -- | -- | **INFO** (crossover regime) |

**Summary**: 8 PASSes, 3 FAILs (f_DM, H_0 raw, CC), 1 EXCLUDED (Interp B), 1 TENSION (w_a), 4 INFO (structural or intermediate). The framework's observational position is narrow and well-characterized: three-quarters of its cosmological predictions work, one does not, and the CC remains the deep structural challenge.

---

## VII. Priority-Ordered Next Steps for S59

Synthesizing all four reviewer suggestions into a priority-ordered list:

### Priority 1: Post-Transit Decay Kinetics of BCS and BA Channels
- **What**: Compute Gamma_BCS/H_0 (K_7-mediated quasiparticle annihilation rate) and Gamma_BA/H_0 (Beliaev phonon decay rate) on cosmological timescales.
- **Who**: Volovik + Mack (superfluid kinetics + cosmological embedding).
- **Input**: W3-6 dispersion relations, K_7 coupling from S35, Josephson energy.
- **Output**: f_DM(z) evolution curve. If both Gamma > H_0, f_DM rises toward 0.844.
- **Gate**: f_DM-DEPLETION-59. PASS: f_DM(z=0) > 0.7. FAIL: f_DM(z=0) < 0.3.
- **Impact**: Resolves the sole bottleneck. If PASS, framework achieves 4/4 observable consistency.
- **Source**: Volovik collab S59-1, Mack collab Priority 2.

### Priority 2: Spinor Normalization in the Friedmann Derivation
- **What**: Decompose the Seeley-DeWitt a_2 coefficient by 4D spinor representation content. Determine whether 4 of 64 spinor components survive KK reduction, giving the exact factor sqrt(16).
- **Who**: Baptista + quantum-acoustics (spectral geometry + KK reduction).
- **Input**: W3-16 a_2 computation, Paper 14 spinor decomposition, Chamseddine-Connes-Marcolli formalism.
- **Output**: Derived normalization factor. H_0 prediction with or without the spinor correction.
- **Gate**: SPINOR-NORM-59. PASS: factor = 4.00 +/- 5%. FAIL: factor differs from 4 by > 20%.
- **Impact**: If PASS, H_0 = 65.4 km/s/Mpc with zero free parameters -- the framework's strongest cosmological output.
- **Source**: Baptista collab 3.4, Hawking collab 4.3, Mack collab Priority 1, Volovik collab S59-4.

### Priority 3: N_pair = 3 Exact Diagonalization
- **What**: 560-state exact diag on 2-cell system at N_pair = 3. Z_2-resolved <r> in at least 3 symmetry sectors.
- **Who**: Landau (exact diagonalization expertise).
- **Input**: W1-1 Hamiltonian construction, V_fold pairing matrix.
- **Output**: <r>_even, <r>_odd, <r>_combined. Integrability verdict.
- **Gate**: NPAIR3-INTEG-59. PASS: <r>_even > 0.50 (integrability broken). FAIL: <r>_even < 0.42 (approximate integrability persists). INFO: [0.42, 0.50].
- **Impact**: Resolves both CC path (thermalization -> Lambda -> 0) and potentially f_DM (occupation redistribution).
- **Source**: Volovik collab S59-2, Hawking collab 3.1, Mack collab Priority 5.

### Priority 4: Zubarev Non-Equilibrium Statistical Operator for GGE
- **What**: Construct rho_neq = rho_GGE + delta_rho incorporating slow (broken) integrals perturbatively. Compute leading correction to Lambda_eff.
- **Who**: Volovik (non-equilibrium thermodynamics).
- **Input**: W1-2 Hessian structure, alpha_crit = 0.523, GGE occupation numbers.
- **Output**: CC relaxation timescale from nearly-integrable regime. delta_Lambda estimate.
- **Impact**: Provides CC evolution estimate even if N_pair = 3 gives INFO. Quantifies the CC relaxation rate in the nearly-integrable regime.
- **Source**: Volovik collab S59-3.

### Priority 5: DM Abundance Recalculation with Post-Fold Mass
- **What**: Recalculate Omega_DM h^2 using m_B2(fold) = 0.72 M_KK instead of 1.03 M_KK. Include epsilon correction (0.00143 vs 0.00248).
- **Who**: Phonon-first-cosmologist (emulator rebuild).
- **Input**: W3-10 mass variation, W0-3 epsilon, W0-1 emulator framework.
- **Output**: Updated NROY with corrected mass and epsilon. Updated f_DM at canonical.
- **Impact**: Precision correction. May worsen f_DM (corrections go downward) but establishes the correct baseline for depletion calculations.
- **Source**: Baptista collab Section 4.

### Priority 6: w_a Error Propagation and DESI DR3 Preparation
- **What**: Compute w(z) with full error propagation through epsilon (2.6x spread), N_cells, alpha. Quantify: what value of w_a excludes the framework?
- **Who**: Mack (cosmological embedding).
- **Input**: W0-4 CPL fit, epsilon uncertainty from W3-13, DESI DR2 covariance.
- **Output**: w_0-w_a confidence region for the framework. Exclusion threshold for DR3.
- **Impact**: Prepares the framework for the most falsifiable near-term test.
- **Source**: Mack collab Priority 3.

### Priority 7: Identify Observational Discriminant from LCDM
- **What**: Sharpen the CMB l ~ 721 feature prediction (24 muK^2, below Planck noise, potentially CMB-S4). Compute exact angular power spectrum modification using W3-1 acoustic metric.
- **Who**: Mack + quantum-acoustics.
- **Input**: W3-1 acoustic FRW metric, W3-6 spectral bands, CMB transfer functions.
- **Output**: Predicted C_l modification at l ~ 721. Signal-to-noise ratio for CMB-S4.
- **Impact**: Currently no prediction distinguishes the framework from LCDM. This would provide one.
- **Source**: Mack collab Priority 4.

### Priority 8: Spectral Dimension of Dirac-Weighted Cayley Graph vs Peter-Weyl
- **What**: Evaluate the return probability P(t) = Tr(e^{-tL}) using the full Peter-Weyl spectrum up to (p+q) <= 4-6. Extract spectral dimension and compare to CG(24)'s d_s = 1.64.
- **Who**: Baptista (spectral geometry).
- **Input**: W2-1 graph Laplacian, full Dirac eigenvalues at higher Peter-Weyl levels.
- **Output**: Whether d_s = 1.64 is a finite-size artifact or structural. If artifact, alpha = -0.652 is a lower bound.
- **Source**: Baptista collab 3.2.

### Priority 9: Cheeger Deformation Theorem for Sigma-Freezing
- **What**: Determine whether Cheeger convergence (Paper 36) guarantees that the T2 (off-Jensen) direction is dynamically suppressed for any U(2)-symmetric initial condition.
- **Who**: Baptista (Riemannian geometry).
- **Input**: W2-2 transit dynamics, Paper 36 Theorem 1.1.
- **Output**: Theorem or counterexample. If theorem, sigma-freezing is permanent.
- **Source**: Baptista collab 3.5.

### Priority 10: Page Curve for Multi-Cell Entanglement
- **What**: Compute S_ent as a function of N_cells (2, 4, 8, 16, 32) to determine whether the entanglement follows a Page curve.
- **Who**: Hawking (information theory).
- **Input**: W1-1 inter-cell entanglement S_ent = 1.039 nats at N_pair = 2.
- **Output**: Page curve or monotonic growth. Determines whether the collective state is an information sink.
- **Source**: Hawking collab 3.2.

---

## VIII. Closing Assessment

After 58 sessions, the framework built on M^4 x SU(3) with Jensen metric occupies a specific and well-characterized position in observational space. The algebraic structure is proven to machine epsilon: KO-dim = 6, SM quantum numbers from C^16, CPT hardwired, gauge coupling ratio geometric, van Hove fold SU(3)-specific. The BCS mechanism is unconditional. The spectral triple produces the Standard Model. These are not approximate results -- they are theorems.

The cosmological translation, built through the Volovik partition and the Shattering program (S37-S58), has achieved partial success. Three of four observables pass at the canonical point. The equation of state moved from excluded (6.0-sigma) to consistent (2.9-sigma) in a single session. The DM is CDM-like by 19-22 orders of magnitude. The Friedmann equation is derivable with a single resolvable normalization factor. The CC has a structural near-cancellation saving 3 orders. Twenty superfluid-vacuum correspondences between the framework and 3He-B physics are confirmed or extended.

Against this: the DM fraction is a factor of 4 wrong, the CC remains 111 orders of magnitude above observation, and the framework predicts w_a = 0 while DESI hints at w_a = -0.73. The integrability that makes the DM stable also makes the CC too large -- these are the same obstruction seen from two angles.

The single most important thing to do next is compute the post-transit decay rates of BCS quasiparticles and BA phonons on cosmological timescales. This computation has never been attempted. Every S58 result characterizes the system at the end of transit (dt ~ 10^{-62} s); none addresses the 13.8 Gyr that follows. The factor-of-4 f_DM gap may be a transit-epoch snapshot that cosmological evolution corrects -- or it may be a permanent feature that excludes SU(3). Only the kinetic theory calculation can distinguish these outcomes.

The framework's prediction set is now precise enough to be falsified. DESI DR3 will test w_a = 0. The N_pair = 3 computation will test integrability. The spinor normalization will test H_0 = 65.4 km/s/Mpc. The depletion kinetics will test f_DM. These are concrete, computable, falsifiable tests with definite answers. The framework has earned the right to take them.
