# Phonon x Landau Workshop Synthesis: Session 54
## Cross-Domain Patterns Meet Condensed Matter Precision

**Date**: 2026-03-22
**Workshop**: 2 rounds, 4 turns (1229 lines)
**Agents**: Phonon-First (cross-domain pattern detection across 8 pillars), Landau (condensed matter theory -- phase transitions, BCS, Fermi liquids, order parameters)
**Source**: Session 54 results + Nazarewicz x Connes workshop synthesis
**Prior workshop**: Nazarewicz x Connes identified S_occ as OPEN with caveats, emerged D_BCS construction, universal lattice monotonicity theorem. This workshop stress-tests those conclusions from condensed matter physics.

---

### I. The Central Result

The workshop's most consequential output is a complete condensed matter diagnosis of WHY the 32-cell lattice at N_pair = 1 cannot stabilize the modulus, organized into six algebraically independent obstructions that all break at the same threshold: N_pair >= 2 on a lattice with N >= 66 modes.

Landau proved three independent explanations of the ED-SWEEP-54 failure (193x shortfall): (1) pairing collapse at d/Delta = 42 makes the condensation energy 1800x weaker than kinetic drift, (2) the Perron-Frobenius ground state of the graph Laplacian has identically zero quantum metric (g_0 = 0), closing the Peotta-Torma flat-band route, and (3) the BCS gap is protected against the Jensen deformation by Anderson's theorem (block-diagonal structure preserves time-reversal symmetry exactly). Phonon organized these alongside the lattice monotonicity theorem, the d_s = 2 Cooper threshold, and Richardson-Gaudin integrability into a dimensional ladder showing all six obstructions share a common origin: the system is below the dimensional threshold for BCS physics.

The S_occ minimum status remains OPEN with caveats, consistent with the Nazarewicz x Connes verdict and the master gate PASS (2/3). Landau sharpened the caveats significantly: the zeta-regularized effective action zeta'_D is monotonically increasing by theorem on 32 cells (all 31 nonzero eigenvalues decrease monotonically, -ln is a decreasing function), S_occ is not a Ginzburg-Landau free energy and has no variational principle, and the Strutinsky decomposition is structurally invalid at N_smooth = 1.2 (factor of 15 below the minimum requirement of 5-10). The S55 zeta computation and continuum E_Rich(tau) remain the decisive tests.

The workshop also advanced the CC problem: Landau proved that inter-cell hopping destroys ALL Richardson-Gaudin conserved quantities for any t > 0 (no partial integrability), but refined Phonon's thermalization claim -- at N_pair = 2 with dim(Hilbert) = 28, the system reaches a diagonal ensemble, not a thermal (Gibbs) state. ETH requires dim > 10^3. The CC path through integrability-breaking is open but narrowed.

---

### II. What Converged

**Lattice monotonicity and state-dependence as only escape (both agents, Rounds 1-2).** Phonon identified the Hellmann-Feynman structure across three pillars (Josephson, flat-band, NCG): Tr f(H(lambda)) is monotone when eigenvalues are monotone, but Tr rho(lambda) f(H(lambda)) is not, because state-geometry coupling introduces feedback. Landau confirmed this from the BCS free energy: the crossover occurs at |dE_int/dtau| = |dE_kin/dtau|, which requires d/Delta ~ 1. At d/Delta = 42, the lattice is 1800x away from the crossover. Both accept: state-dependence is the only escape from monotonicity on 32 cells.

**Peotta-Torma quantum metric g_0 = 0 (Landau, accepted by Phonon as permanent).** The k=0 Perron-Frobenius eigenvector is the uniform vector; the velocity operator V_a annihilates it because the row-sum of the adjacency matrix is constant. Therefore g_0 = 0 identically -- an algebraic obstruction, not a quantitative suppression. The flat-band quantum metric route is closed at N_pair = 1 permanently.

**Three-wall explanation of 193x shortfall (Landau, accepted by Phonon).** Pairing collapse (Delta/d)^2 ~ 5.7 x 10^{-4}, Anderson's theorem (gap protected by block-diagonal structure), and zero quantum metric (Perron-Frobenius) are algebraically independent obstructions that each independently account for the ED-SWEEP failure. Together they form a permanent wall at N_pair = 1 on 32 cells.

**Cooper instability has sharp threshold on finite lattice (Landau, accepted by Phonon).** g_critical = 2d / ln(N/2); at N = 32 (8 BCS modes), g/g_critical = 0.084 -- a factor of 12 below threshold. This is a sharp transition, not a crossover. The "2D Cooper instability with no threshold" requires N -> infinity. The structural content: d_s = 2 means the Cooper logarithm is the weakest possible divergence. The pair susceptibility chi_pair ~ (1/2d) ln(N/2), and the pairing criterion g * chi_pair > 1 becomes g > 2d / ln(N/2). At d_s = 2, the graph sits at the marginal dimension for pairing.

**N_critical = W/g = 66 modes for BCS onset (both agents).** Anderson nanoparticle analogy: Ralph-Black-Tinkham experiments on ultrasmall Al grains confirm the gap vanishes when d exceeds Delta. Connes' N_critical ~ 10^5 is for DOS convergence (reproducing the continuum B2 near-degeneracy), not for BCS onset. Phonon's independent estimate from g * N(E_F) > 1 gives ~70 modes, consistent with Landau's 66. The 8-fold shortfall on 32 cells explains the ED-SWEEP failure quantitatively.

**Anderson's theorem: protects Delta, not E_cond (Landau concedes, both converge).** Landau's Round 1 overstatement ("Anderson's theorem would still protect the gap even at d/Delta = O(1)") was corrected by Phonon: Anderson's theorem protects the gap magnitude Delta but allows E_cond ~ N(E_F) * Delta^2 to vary through the density of states N(E_F). On the continuum, the B2 van Hove singularity could produce non-monotone E_cond despite constant Delta. Anderson's theorem is a selection rule (tau-dependence enters through N(E_F), not Delta), not a wall.

**Fermi liquid corrections irrelevant at N_pair = 1 (Landau).** Z_k = 1 (no Fermi sea dressing), m*/m = 1 (no exchange), no collective modes, no zero sound. The "Leggett modes" from S48 are single-particle Rabi oscillations, not Fermi liquid collective excitations.

**Connes distance = compliance expansion (both agents, Rounds 1-2).** Landau distinguished geometric expansion (lattice parameter change), compliance expansion (elastic modulus change), and spectral softening (DOS shift). The Connes distance growth on 32 cells is compliance expansion: the graph topology is fixed, but J_C2 decreases, making the effective medium more compliant. Phonon amplified: compliance expansion produces redshift (excitation frequencies drop) but NOT causal expansion (no new horizons). The deceleration parameter q = -0.786 is a Gruneisen parameter, not a Friedmann deceleration parameter.

**K_7 structure does NOT break Anderson's theorem (Landau, Round 2).** The conjugation symmetry C: (p,q) -> (q,p) forces Delta_+ = Delta_- at mean-field level. Anderson's theorem holds on the Jensen line at all tau. Escape requires explicit C-breaking in the BCS interaction (off-Jensen deformations or fluctuation corrections).

**Pair mobility mu_pair is monotonically decreasing (Landau, Round 2).** mu_pair ~ E_1(tau) / 2 ~ J_C2(tau) * lambda_1(graph) / 2, where lambda_1 is the algebraic connectivity (fixed). No maximum at fold -- the pair is most mobile at small tau (strong coupling) and least mobile at large tau. The S47 superfluid density anti-correlation with curvature comes from the superfluid fraction n_s (which increases as the band narrows and spectral weight concentrates near E_F), not from mu_pair. This resolves the apparent contradiction: rho_s = mu_pair * n_s, where mu_pair decreases and n_s increases, producing the observed anti-correlation through n_s alone.

**GCM non-orthogonality does NOT break inter-sector integrability (Landau, Round 1).** The Ambegaokar-Baratoff mapping is correct (GCM overlap maps to Josephson coupling between grains), but the block-diagonal theorem (S22b) makes the overlap kernel block-diagonal in Richardson-Gaudin sectors. GCM non-orthogonality converts the Mott insulator into a band insulator but does not open a new CC path. This is an important negative result that closes the channel Nazarewicz identified in the prior workshop.

**Cutoff sensitivity is quantitatively predicted by BCS theory (Landau, Round 1).** The sensitivity of the BCS gap to cutoff shape scales as exp(d/Delta). At d/Delta = 42, this gives ~10^18. A 1% change in cutoff shape produces an O(1) change in the barrier height. The 178x barrier spread (5.35% sharp -> 0.03% polynomial) is exactly what BCS theory predicts. The S_occ minimum is a cutoff-edge resonance, not a bulk pairing effect.

**S55 priority ordering agreed (both agents, Round 2).** 1. zeta'_D (monotone by theorem, 1-line verification). 2. E_Rich on 992-mode continuum (decisive BCS test). 3. D_BCS Connes distance (state-dependent spectral triple). 4. N_pair = 2 ED. 5. Pair mobility. Phonon moved D_BCS from Landau's original position 5 to position 3, arguing it is computable from existing data and tests the workshop's central emergence within N_pair = 1. Landau accepted the reordering.

---

### III. What Emerged

**The dimensional ladder of obstructions (Phonon, E1, refined by Landau).** Six obstructions organized into a ladder:

| Dimension | Obstruction | Broken By |
|:----------|:-----------|:----------|
| d = 0 (single cell) | No Fermi sea, Z_k = 1 | N_pair >= 2 |
| d_s = 2 (graph) | Pairing threshold g_crit ~ d/ln(N) | N >> 66 modes |
| d_s = 2 (graph) | Lattice monotonicity theorem | Higher d_s (richer spectrum) |
| Symmetry (block-diagonal) | Anderson protection of Delta | Off-Jensen or inter-sector |
| Geometry (Perron-Frobenius) | Zero quantum metric g_0 = 0 | N_pair >= 2 (excited modes) |
| Integrability (Richardson-Gaudin) | GGE persists, CC unsolved | Inter-cell hopping at N_pair >= 2 |

Every obstruction breaks at the same threshold: N_pair >= 2 on N >= 66 modes. Phonon: all obstructions are one wall viewed from different pillars. Landau's caveat: coincident threshold at N_pair >= 2, N >= 66 is expected for ANY interacting system -- below a certain size, nothing works. The S55 test discriminates: vary N_pair and N_modes independently. If obstructions break in the predicted pattern (some depend on N_pair, others on N_modes), the ladder is structural. If not, the coincidence is accidental.

**The compliance-redshift duality (both agents, E2/E3).** Connes distance d_D ~ 1/J_C2 and acoustic compliance kappa^{-1} ~ 1/d are the SAME observable in two languages -- both measure spectral softening under Jensen deformation. This is an identity, not an analogy (both controlled by J_C2 up to a geometric factor). Physical consequence: the expansion produces redshift of KK excitations (lighter effective masses) but not causal expansion (graph topology fixed). The proper comparison is to perovskite soft-mode transitions (SrTiO3 at 105K: gamma ~ 10-100 for the soft mode), not to cosmological expansion.

**GGE diagonal ensemble refinement (Landau, E1, building on Phonon's CC extension).** At N_pair = 2, integrability breaks (all RG conserved quantities destroyed) but the system reaches the diagonal ensemble rho_DE = sum_n |c_n|^2 |n><n|, not thermal equilibrium. ETH fails at dim = 28 (requires dim > 10^3 per Beugeling-Moessner-Haque). The vacuum energy P_vac(DE) is determined by the expansion coefficients |c_n|^2 of the initial post-transit state in the many-body eigenbasis, which retains memory of initial conditions. The CC path requires showing P_vac(DE) << P_vac(GGE) -- a computable, pre-registerable gate for S55. At N_pair = 3-4 on 8 modes, the Fock space dimension reaches the ETH threshold (~10^3) and the diagonal ensemble approaches the microcanonical, connecting to Volovik's q-theory self-tuning.

**Strutinsky validity boundary (Landau, E3).** The Strutinsky energy theorem requires N_smooth = gamma/d > 5-10 levels in the smoothing window (Brack-Bhaduri, "Semiclassical Physics," Ch. 5). On 32 cells: N_smooth = 1.2 (structurally invalid -- a factor of 15 below the conservative minimum). On the 992-mode continuum: N_smooth ~ 20 (valid). The S_occ minimum at 5.35% on the lattice is NOT a Strutinsky shell correction in any meaningful sense -- the "oscillating" part is a single level and the "smooth" part is a constant. The Berry-Tabor-Strutinsky triangle is valid only above ~40 modes in the pairing window. This explains why the cutoff dependence is so severe on 32 cells: the decomposition operates outside its regime, and the "shell correction" is indistinguishable from cutoff noise. The E_Rich(tau) computation on the 992-mode continuum is the first test of the Strutinsky-NCG bridge in its regime of validity.

**BCS free energy classification (Landau, L1-L2).** The Jensen transit is a Landau-Zener sweep through an avoided crossing, not a Landau phase transition. No spontaneous symmetry breaking occurs (SU(3) -> U(2) is explicit, not spontaneous). The BCS order parameter Delta(tau) is nonzero at all tau but perturbatively small (d/Delta = 42). S_occ is not a free energy, not a GL functional, and not the spectral action -- it is a hybrid functional with no variational principle. The correct physical observable for stabilization is the superfluid density rho_s (thermodynamic quantity with Meissner kernel interpretation). Landau's Ginzburg-Landau analysis shows F_GL(tau) = -a(tau)^2 / (4b(tau)) is monotone on the lattice because N(E_F) is essentially constant (one level at a time). On the continuum, N(E_F) increases toward the van Hove singularity, making F_GL monotonically decreasing -- still no minimum.

**Integrability phase transition framing of CC (Phonon, E2, refined by Landau).** Phonon proposed the GGE-to-thermal transition as an integrability phase transition, analogous to the KAM theorem in classical mechanics (invariant tori breaking under perturbation). Landau sharpened: quantum KAM does not exist as a theorem. The relevant transition is Poisson-to-GOE in the many-body level statistics. At N_pair = 1, single-particle statistics are Poisson (Berry-Tabor confirmed). At N_pair >= 2, inter-pair interactions introduce level repulsion in the many-body spectrum even though single-particle integrability survives (Casimir quantum numbers remain good). The mechanism: single-particle integrability persists, many-body integrability breaks, GGE decays on the many-body timescale. Landau estimates Brody parameter beta ~ 0.7-0.9 for the full 28-dim two-pair space, but the block-diagonal theorem restricts to dim = 6 within B2, where statistical diagnostics are marginal. The nearest-neighbor spacing ratio <r> is the informative test at small dimension.

---

### IV. What Remains in Dissent

**S_occ theoretical status (survived 2 rounds).** Landau: S_occ has no uniqueness property (unlike the EH action, which is uniquely determined by diffeomorphism invariance, or the spectral action, constrained by the Chamseddine-Connes theorem). It depends on a reference state and cutoff (not background-independent). The zeta-regularized version is monotone by theorem. S_occ is one of infinitely many ways to combine BCS occupation with spectral sums, and the cutoff dependence is the symptom of this ambiguity. Phonon: the spectral action is also not derived from a Hamiltonian; S_occ could be the correct geometro-dynamical action without being a free energy; the GR Einstein-Hilbert action is not a free energy either, but its stationary points determine the metric. The zeta test settles this on 32 cells but does not resolve the continuum question. Unresolved until S55 zeta and continuum computations.

**Dimensional ladder: structural identity vs coincidence (survived 2 rounds).** Phonon: all six obstructions share one structural origin below the BCS dimensional threshold. Landau: coincident threshold at N_pair >= 2, N >= 66 is expected for ANY interacting system -- below a certain size, nothing works. The stronger test: increase N_modes at fixed N_pair = 1 (should break obstructions 1, 3, 5 while 2 and 6 persist) and increase N_pair at fixed N_modes = 8 (should break 5 and 6 while 1 and 3 persist). If the obstructions break in this predicted pattern under independent variation, the ladder is structural. If not, it is coincidence.

**Transit classification domain relevance (survived 2 rounds).** Both agree: Landau-Zener at N_pair = 1 on 32 cells; Kibble-Zurek on the spatially extended fabric at N_pair >> 1. Dissent is only over which domain governs S55 computations. Landau: at S55 scope (32 cells, N_pair <= 2), the Landau-Zener classification is exact. Kibble-Zurek requires (a) a genuine phase transition (N_pair >> 1, d/Delta < 1) and (b) the transit rate slower than the correlation time near the critical point (the opposite of the deeply diabatic regime at N_pair = 1). Phonon: the soliton structure from Jackiw-Rebbi theory (kink interpolating between two vacua binding zero-energy fermion modes) matters for the physical interpretation of the spatially extended fabric, even if not yet computable at S55 scale.

---

### V. CM Answers to the 10 Questions

Phonon posed 10 questions across 9 topical sections (P1-P8). Landau's responses constitute reference-quality condensed matter results for the framework.

Summary: four questions produced closures, five produced permanent structural results, and one remains open for S55 computation.

| # | Question (Phonon) | CM Answer (Landau) | Status |
|:--|:-------------------|:-------------------|:-------|
| P1-Q1 | BCS free energy monotonicity condition | Crossover at d/Delta ~ 1 via Hellmann-Feynman. At d/Delta = 42, kinetic dominates by 1800x. BCS F is monotone. | PERMANENT |
| P1-Q2 | Peotta-Torma quantum metric on 32-cell | g_0 = 0 identically (Perron-Frobenius). Superfluid weight D_s = 0 for occupied mode. | CLOSED |
| P2-Q1 | D_BCS as self-consistent JJ array | Maps to granular superconductor (Beloborodov et al.). Inverted sign: depleted sites have stronger effective coupling. Self-consistent transition may exist. | OPEN for S55 |
| P3-Q1 | Cutoff-shape sensitivity at d/Delta = 42 | Sensitivity ~ exp(d/Delta) ~ 10^18. The 178x barrier spread is EXACTLY predicted by BCS theory. Cutoff-edge resonance, not bulk pairing. | PERMANENT |
| P3-Q2 | Zeta-regularized = determinant? | Yes: zeta'_D = -sum ln(E_k) = ln det(H_TB). Monotonically increasing by theorem on 32 cells. | PERMANENT |
| P4-Q1 | Hopping breaks RG integrals? | ALL N_pair integrals break for ANY t > 0. No partial integrability. Breaking rate ~ (t/g)^2 * d. At N_pair = 2: Gamma ~ 0.76 M_KK, O(1) natural timescale. | PERMANENT |
| P4-Q2 | GCM overlap = Josephson coupling? | Yes, maps to Ambegaokar-Baratoff. But overlap is block-diagonal (from S22b), so does NOT break inter-sector integrability. GCM channel does not open CC path. | CLOSED |
| P5-Q1 | Compliance vs geometric expansion | Compliance expansion = elastic modulus change (Born-Huang). Connes distance growth is compliance, not geometric. Redshift without causal expansion. | PERMANENT |
| P6-Q1 | Cooper instability on finite d_s = 2 graph | Sharp threshold: g_crit = 2d/ln(N/2). At N = 32: g/g_crit = 0.084 (12x below). | PERMANENT |
| P7-Q1 | Strutinsky minimum level count | N_smooth > 5-10 (Brack-Bhaduri). At 8 modes: N_smooth = 1.2, factor 15 below minimum. Decomposition structurally invalid on 32 cells. | PERMANENT |

Phonon also posed four follow-up questions in Round 2. Landau's answers:

**Q1 (K_7-dependent pairing and Anderson escape):** The conjugation symmetry C: (p,q) -> (q,p) is exact on the Jensen line ([C, H_TB] = 0 to machine epsilon). C forces Delta_+ = Delta_- at mean-field level. Anderson's theorem holds. Escape requires explicit C-breaking: off-Jensen deformations, fluctuation corrections beyond mean field, or multi-pair occupation-dependent interactions. All routes point to N_pair >= 2 or off-Jensen physics.

**Q2 (Brody parameter for two-pair space):** At the full dim = 28 with t/d = 3.9 (well above the Poisson-to-Wigner-Dyson crossover at t/d ~ 1), beta ~ 0.7-0.9. But the block-diagonal theorem restricts B2 pairs to dim = 6, where the Brody distribution is not statistically well-defined. The nearest-neighbor spacing ratio <r> is the correct diagnostic: Poisson gives <r> = 0.386, GOE gives <r> = 0.531. Computable from as few as 10 levels.

**Q3 (Pair mobility):** mu_pair = E_1 / 2 = 0.0885 M_KK at the fold, monotonically decreasing with tau. No maximum. The resolution of the apparent conflict with S47's rho_s anti-correlation: rho_s = mu_pair * n_s, and the anti-correlation comes from n_s (which increases as the band narrows), not mu_pair.

**Q4 (Critical Hilbert space dimension for chaos):** dim = 28 gives level repulsion (Wigner-Dyson onset at dim ~ 10) but not ETH (requires dim > 10^3). Minimum N_pair for ETH on 8 modes: N_pair = 3-4. For full thermalization at N_pair = 1: O(10^3) modes needed, comparable to Connes' N_critical estimate.

---

### VI. Priority Computations for S55

1. **zeta'_D(0, tau) on 32-cell lattice.** Monotone by theorem (Landau proved in Round 1). One-line verification: zeta'_D = -sum_{k=1}^{31} ln(E_k(tau)). Establishes theorem on the record and separates zeta'_D from S_occ. Zero cost.

2. **E_Rich(tau) on 992-mode continuum at N_pair = 1.** The decisive BCS test. On the continuum d/Delta ~ 0.19 (pairing collapse absent), Anderson's theorem channels tau-dependence through N(E_F), and the B2 van Hove singularity provides the candidate non-monotone structure. Pre-register: PASS if minimum in [0.10, 0.30]; FAIL if monotone.

3. **D_BCS Connes distance on 32-cell lattice.** Tests the workshop's central emergence from Naz x Connes. State-dependent spectral triple D_BCS = D / sqrt(F_i * F_j). Computable from existing S54 data (50 SDPs or shortest-path computations). Pre-register: PASS if minimum exists; FAIL if monotone.

4. **N_pair = 2 exact diagonalization on 8 modes.** Two-pair Fock space (dim = 28 full, dim = 6 within B2). Tests integrability-breaking and diagonal ensemble vacuum energy. Pre-register for CC path: PASS if P_vac(DE)/P_vac(GGE) < 0.1; FAIL if > 0.5.

5. **Level statistics of two-pair Fock space.** Nearest-neighbor spacing ratio <r> for two-pair Hamiltonian. Diagnostic for integrability-breaking. Pre-register: CC path PASS if <r> > 0.48; FAIL if < 0.40.

6. **S_fermionic on 992-mode continuum.** Connes predicts S_f is NOT monotone on continuum (B2 near-degeneracy drives occupation redistribution). If non-monotone, full NCG action S_b + S_f is the candidate stabilization functional.

7. **Strutinsky decomposition on 992-mode continuum.** First test of Strutinsky-NCG bridge in its regime of validity (N_smooth ~ 20). If shell correction matches Berry-Tabor prediction (ratio ~ 1.26), the bridge is established. If not, the match on the continuum was accidental.

8. **Dimensional ladder independence test.** On 992 modes at N_pair = 1: verify that obstructions 1 (pairing collapse) and 3 (monotonicity) break while obstructions 2 (Anderson) and 6 (integrability) persist. Confirms or refutes the structural identification.

---

### VII. Closing

This workshop subjected the Nazarewicz x Connes conclusions to condensed matter cross-examination and produced permanent structural results on both sides. From condensed matter: three algebraically independent walls at N_pair = 1 (pairing collapse, Anderson protection, zero quantum metric), a sharp Cooper threshold 12x above the coupling strength, Strutinsky invalidity at 8 modes, the zeta monotonicity theorem, and the compliance-vs-geometric expansion distinction. From cross-domain pattern detection: the dimensional ladder organizing all obstructions, the compliance-redshift duality as an identity rather than analogy, and the integrability phase transition framing of the CC problem.

The S_occ minimum remains OPEN with caveats -- now substantially strengthened caveats, but the master gate PASS (2/3) stands. The workshop did not overturn the Naz x Connes verdict; it quantified WHY the caveats are serious and what computations resolve them. The zeta monotonicity theorem (proved, not merely predicted) establishes that the spectral zeta function cannot stabilize the modulus on 32 cells. The Anderson theorem analysis channels the entire continuum stabilization question through N(E_F, tau) -- the van Hove singularity is the single surviving mechanism for non-monotone E_cond.

The path forward converges from all directions to the same point: N_pair >= 2 on N >= 66 modes. The S55 computation plan tests both axes independently (992-mode continuum at N_pair = 1; two-pair ED at 8 modes), which is the correct experimental design to discriminate structural identity from coincidental threshold. Landau classified the 32-cell system as "the simplest possible BCS system on the simplest possible SU(3) lattice":
- d/Delta = 42 (ultrasmall Al grain analog)
- E_J/E_C = 0.818 (Cooper pair box in charge regime)
- Gi = 0.506 (0D limit, no condensate)
- g * N(0) = 0.015 (deep weak-coupling)
- Z_k = 1, m*/m = 1 (no Fermi sea dressing)
- Exact Richardson-Gaudin integrability

This is a proof of concept for structural framework elements (Connes distance, Berry-Tabor, block-diagonal theorem, CPT) and a proof of insufficiency for physical predictions (stabilization, CC, collective excitations). Both results are permanent.
