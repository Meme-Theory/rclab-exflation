# Session 54 Workshop Extraction: All Computation Suggestions, Gates, and Open Questions

**Date**: 2026-03-22
**Extracted from**: 4 workshop synthesis documents (~3,245 lines total)
**Method**: Exhaustive catalog -- every computation suggestion, recommendation, proposed calculation, pre-registered gate, and open question

---

## Extraction

### 1. Zeta-Regularized Effective Action on 32-Cell Lattice
- **Source**: Naz x Connes, Section VI (#1); Phonon x Landau, Section VI (#1); QA x Hawking, Section VI (#1); Master, Section VI (Z1)
- **What**: Compute zeta'_D(0, tau) = -sum_{k=1}^{31} ln(E_k(tau)) on the 32-cell lattice at 50 tau points. One-line computation from existing eigenvalue data. Monotone by theorem (all 31 nonzero eigenvalues of H_TB(tau) decrease monotonically). Settles the S_occ cutoff-artifact question.
- **Inputs**: Existing 32-cell eigenvalue data at 50 tau points from S54
- **Tests**: Whether zeta'_D is monotone (predicted by all 3 workshops). If monotone, S_occ minimum confirmed as cutoff artifact. If non-monotone, Connes' prediction fails and S_occ is strengthened.
- **Pre-registered gate**: Monotone -> S_occ cutoff artifact confirmed. Non-monotone -> Connes prediction wrong. (No formal gate ID assigned; implicit settlement of SA-LATT-OCC-54 status.)
- **Cost**: ZERO
- **Priority**: CRITICAL (3/3 workshops, unanimous first priority)

### 2. E_Rich(tau) on 992-Mode Continuum at N_pair = 1
- **Source**: Naz x Connes, Section VI (#2); Phonon x Landau, Section VI (#2); Master, Section VI (D1)
- **What**: Compute the Richardson-Gaudin ground-state energy E_Rich(tau) on the 992-mode continuum Dirac spectrum at N_pair = 1. The decisive BCS stabilization test where DOS supports pairing (d/Delta ~ 0.19 on continuum vs 42 on lattice). Anderson's theorem channels tau-dependence through N(E_F); B2 van Hove singularity is the candidate non-monotone structure.
- **Inputs**: 992-mode continuum Dirac spectrum at 50 tau values
- **Tests**: Whether BCS stabilization works where DOS supports pairing
- **Pre-registered gate**: PASS if minimum in [0.10, 0.30]; FAIL if monotone. (Both Naz x Connes agents agree this is the single most important S55 computation.)
- **Cost**: MEDIUM (Richardson-Gaudin solution at 50 tau values on 992-mode spectrum)
- **Priority**: CRITICAL (2/3 workshops explicitly; "single most important S55 computation")

### 3. D_BCS Connes Distance on 32-Cell Lattice
- **Source**: Naz x Connes, Section VI (#3); Phonon x Landau, Section VI (#3); Master, Section VI (D2)
- **What**: Compute the Connes distance from the state-dependent spectral triple D_BCS(tau)_{ij} = D_{ij} / sqrt(F_i(tau) * F_j(tau)), where F_i is local BCS occupation at site i. Tests whether occupation concentration produces a metric minimum via competition between geometric expansion (J_C2 decreasing) and occupation concentration (n_0 ~ 0.96).
- **Inputs**: Existing S54 32-cell eigenvalue and occupation data; 50 SDPs or shortest-path computations
- **Tests**: Whether the workshop's central NCG emergence (D_BCS) provides a stabilization minimum
- **Pre-registered gate**: PASS if minimum exists; FAIL if monotone.
- **Cost**: MEDIUM (50 SDPs from existing data)
- **Priority**: HIGH (endorsed by 2/3 workshops at priority 3)

### 4. Sign of dS_fermionic/dtau on 992-Mode Continuum
- **Source**: Naz x Connes, Section VI (#4); Phonon x Landau, Section VI (#6); Master, Section VI (D4)
- **What**: Compute the fermionic spectral action S_f on the 992-mode continuum spectrum and determine whether dS_f/dtau is positive anywhere in [0.10, 0.30]. Connes predicts S_f is NOT monotone on the continuum because B2 near-degeneracy drives occupation redistribution that can make the occupation response term positive.
- **Inputs**: 992-mode continuum spectrum at multiple tau values; BCS occupation numbers
- **Tests**: Whether the full NCG action S_b + S_f is non-monotone on the continuum
- **Pre-registered gate**: If dS_f/dtau positive anywhere in [0.10, 0.30], S_b + S_f stabilization OPEN. If uniformly negative, CLOSED on continuum permanently.
- **Cost**: MEDIUM
- **Priority**: HIGH (Naz x Connes primary)

### 5. GCM Overlap Block-Diagonality Test
- **Source**: Naz x Connes, Section VI (#5); Master, Section VI (E3)
- **What**: Test whether the GCM overlap kernel G(tau_i, tau_j) is block-diagonal across Richardson-Gaudin sectors. Nazarewicz proposed non-orthogonality as a CC path (if G not block-diagonal, integrability breaks without Josephson coupling). Phonon x Landau closed the channel (block-diagonal by S22b theorem via Ambegaokar-Baratoff mapping).
- **Inputs**: BCS wavefunctions on neighboring cells at slightly different tau values
- **Tests**: Whether GCM non-orthogonality opens a CC path
- **Pre-registered gate**: If G not block-diagonal -> CC path OPEN via non-orthogonality. If block-diagonal -> Josephson is the only surviving path. (Phonon x Landau already closed this analytically; formal verification confirms.)
- **Cost**: LOW
- **Priority**: MEDIUM (proposed by Naz x Connes; pre-closed by Phonon x Landau)

### 6. BdG Connes Distance on 32-Cell Lattice
- **Source**: Naz x Connes, Section VI (#6); Master, Section VI (E5)
- **What**: Compute the BdG (Bogoliubov-de Gennes) Connes distance on the 32-cell lattice. Off-diagonal Nambu blocks introduce a symmetric component to [D, f], relaxing the Lipschitz constraint. First geometric signature of BCS transition in the spectral triple.
- **Inputs**: 32-cell BdG Dirac operator, existing eigenvalue data
- **Tests**: Whether pairing produces a measurable BdG Connes distance shorter than unpaired
- **Pre-registered gate**: None explicitly defined. Exploratory.
- **Cost**: MEDIUM
- **Priority**: LOW (exploratory)

### 7. Continuum Hekkelman-McDonald Integral with d=8 Weyl Asymptotics
- **Source**: Naz x Connes, Section VI (#7)
- **What**: Exploratory computation testing whether the lattice monotonicity theorem extends to the continuum via the Hekkelman-McDonald integral with d=8 Weyl asymptotics appropriate for SU(3).
- **Inputs**: 992-mode continuum spectrum
- **Tests**: Whether spectral monotonicity is a lattice artifact or a continuum property
- **Pre-registered gate**: None explicitly defined. Exploratory.
- **Cost**: MEDIUM
- **Priority**: LOW (exploratory)

### 8. Euclidean Free Energy F(tau, T_GH) on 32-Cell Lattice (EUCLID-55)
- **Source**: QA x Hawking, Section VI (#1); Master, Section VI (Z2)
- **What**: Compute F(tau, T_GH(tau)) = -T_GH(tau) * ln Z_BCS(tau, T_GH(tau)) at 50 tau points from existing eigenvalue data, where T_GH = H(tau)/(2 pi) = 0.59 M_KK. The first functional coupling acoustic and gravitational sectors without free parameters. Self-consistent loop: spectral softening -> expansion -> T_GH -> partition function -> free energy minimum -> halt.
- **Inputs**: Existing 32-cell eigenvalue data at 50 tau points; expansion rate H(tau) from S54
- **Tests**: Whether the Euclidean free energy has a minimum near the fold, producing a self-consistent stabilization
- **Pre-registered gate**: EUCLID-55: PASS if minimum in [0.10, 0.30] with barrier > 1% of F(min). FAIL if monotone or barrier < 0.1%.
- **Cost**: ZERO
- **Priority**: CRITICAL (QA x Hawking primary; replaces S_occ as candidate)

### 9. Euclidean Free Energy on 992-Mode Continuum (EUCLID-CONTINUUM-55)
- **Source**: QA x Hawking, Section VI (#2); Master, Section VI (D5)
- **What**: Repeat the EUCLID-55 computation on the 992-mode continuum spectrum. Tests whether van Hove DOS enhancement strengthens the minimum found (or not found) on 32 cells.
- **Inputs**: 992-mode continuum spectrum at multiple tau values; expansion rate H(tau)
- **Tests**: Whether the continuum DOS enhancement produces a stronger stabilization minimum
- **Pre-registered gate**: EUCLID-CONTINUUM-55: PASS if barrier on continuum exceeds barrier on 32 cells.
- **Cost**: MEDIUM (requires 992-mode spectrum at multiple tau)
- **Priority**: HIGH

### 10. Fabric-Scale Josephson Coupling Estimate (FABRIC-COUPLING-55)
- **Source**: QA x Hawking, Section VI (#3); Master, Section VI (E4)
- **What**: Estimate the inter-cell Josephson coupling t in the tessellated fabric. Compute the acoustic CC gatekeeper ratio t / (H * L_cell). The acoustic horizon analysis shows r_sonic = 0.25 cells at the fold -- every cell acoustically isolated. On the fabric, the critical ratio determines whether thermalization is acoustically permitted.
- **Inputs**: Inter-cell coupling estimate t; expansion rate H(tau); cell size L_cell
- **Tests**: Whether GGE is acoustically protected on the fabric
- **Pre-registered gate**: FABRIC-COUPLING-55: PASS (thermalization possible) if ratio > 1. FAIL (GGE acoustically protected) if ratio < 1.
- **Cost**: LOW
- **Priority**: MEDIUM

### 11. N_pair = 2 Exact Diagonalization on 8 Modes (NPAIR2-CC-55)
- **Source**: QA x Hawking, Section VI (#4); Phonon x Landau, Section VI (#4); Master, Section VI (D3)
- **What**: Perform exact diagonalization of the two-pair Fock space (dim = 28 full, dim = 6 within B2) on 8 modes. Compute P_vac(diagonal ensemble) vs P_vac(GGE). Tests integrability-breaking and whether grand canonical fluctuations break the Euler tautology.
- **Inputs**: 8-mode BCS Hamiltonian; two-pair Fock space construction
- **Tests**: Whether the CC path through integrability-breaking is viable at N_pair = 2
- **Pre-registered gate**: NPAIR2-CC-55: PASS (CC path viable) if P_vac(DE)/P_vac(GGE) < 0.1 (Phonon x Landau) or < 0.5 (QA x Hawking); FAIL if > 0.5.
- **Cost**: MEDIUM (28-dimensional exact diagonalization)
- **Priority**: HIGH (2/3 workshops)

### 12. Level Statistics of Two-Pair Fock Space
- **Source**: Phonon x Landau, Section VI (#5); Master, Section VI (D3, sub-gate)
- **What**: Compute the nearest-neighbor spacing ratio <r> for the two-pair Hamiltonian on 8 modes. Diagnostic for integrability-breaking in the many-body spectrum. Poisson gives <r> = 0.386, GOE gives <r> = 0.531. Computable from as few as 10 levels.
- **Inputs**: Two-pair Hamiltonian eigenvalues on 8 modes
- **Tests**: Whether integrability is broken at N_pair = 2
- **Pre-registered gate**: CC path PASS if <r> > 0.48 (GOE, integrability broken); FAIL if <r> < 0.40 (Poisson, integrable).
- **Cost**: LOW (subproduct of N_pair = 2 ED)
- **Priority**: HIGH (Phonon x Landau)

### 13. Transit Velocity Sensitivity of GGE Temperatures (TRANSIT-VELOCITY-55)
- **Source**: QA x Hawking, Section VI (#5); Master, Section VI (E6)
- **What**: Vary omega_tau by factors of 0.5, 2, 5 in the Landau-Zener cascade on 32 cells and measure T_k(omega_tau). Tests whether GGE temperatures depend on transit velocity.
- **Inputs**: 32-cell Landau-Zener cascade data; modified transit velocities
- **Tests**: Whether the frozen GGE distribution carries memory of when it froze
- **Pre-registered gate**: TRANSIT-VELOCITY-55: PASS (velocity-dependent) if dT_k/d(omega_tau) nonzero for at least one sector. FAIL if all dT_k/d(omega_tau) < 0.01.
- **Cost**: LOW
- **Priority**: MEDIUM

### 14. xi = F_Q/F_Q^max on 992-Mode Continuum (XI-CONTINUUM-55)
- **Source**: QA x Hawking, Section VI (#6)
- **What**: Compute the quantum fidelity ratio xi = F_Q/F_Q^max on the 992-mode continuum. Compare to Bekenstein saturation. Tests whether the 24% vs 27% coincidence on 32 cells is structural or accidental.
- **Inputs**: 992-mode continuum BCS ground state fidelity data
- **Tests**: Whether the xi-Bekenstein coincidence is structural
- **Pre-registered gate**: Structural if |xi - S/S_BH| < 0.05; accidental if > 0.10.
- **Cost**: MEDIUM
- **Priority**: LOW (dissent between QA and Hawking on interpretation)

### 15. Fabric-Scale Acoustic Re-Entry (FABRIC-REENTER-55)
- **Source**: QA x Hawking, Section VI (#7); Master, Section VI (E4, related)
- **What**: On the tessellated fabric with estimated inter-cell coupling t, compute r_fabric(tau) = t/H(tau) at multiple post-fold tau values. Identify whether acoustic re-entry ("reheating point") occurs at any tau > 0.19. Hawking showed r_sonic SHRINKS monotonically at single-cell scale; fabric-scale re-entry depends on t(tau).
- **Inputs**: Estimated inter-cell coupling t; expansion rate H(tau) at multiple post-fold tau
- **Tests**: Whether phononic analog of inflationary reheating occurs on the fabric
- **Pre-registered gate**: FABRIC-REENTER-55: PASS (reheating) if re-entry occurs. FAIL (eternal isolation) if r_fabric < L_cell at all tau.
- **Cost**: LOW
- **Priority**: MEDIUM

### 16. Self-Consistent Fixed-Point Condition (SELF-CONSISTENT-LOOP-55)
- **Source**: QA x Hawking, Section VI (#8); Master, Section VI (E7)
- **What**: Solve the fixed-point condition dF(tau, T_GH(tau))/dtau = 0 self-consistently, where T_GH depends on tau through H, which depends on the modulus dynamics governed by F. Goes beyond EUCLID-55 by closing the self-consistency loop.
- **Inputs**: F(tau, T_GH) from EUCLID-55; modulus dynamics equations
- **Tests**: Whether the self-consistent equilibrium exists and is stable
- **Pre-registered gate**: SELF-CONSISTENT-LOOP-55: PASS if fixed point exists with positive Hessian. FAIL if no fixed point or unstable.
- **Cost**: MEDIUM
- **Priority**: MEDIUM

### 17. Strutinsky Decomposition on 992-Mode Continuum
- **Source**: Phonon x Landau, Section VI (#7); Master, Section VI (E1)
- **What**: First test of the Strutinsky-NCG bridge in its regime of validity (N_smooth ~ 20 on 992 modes vs the structurally invalid N_smooth = 1.2 on 32 cells). Decompose the energy into smooth + shell-correction parts.
- **Inputs**: 992-mode continuum spectrum eigenvalues
- **Tests**: Whether shell correction matches Berry-Tabor prediction (ratio ~ 1.26) on the continuum
- **Pre-registered gate**: None explicitly defined. If shell correction matches Berry-Tabor prediction, bridge established. If not, continuum match was accidental.
- **Cost**: MEDIUM
- **Priority**: MEDIUM (Phonon x Landau)

### 18. Dimensional Ladder Independence Test on 992 Modes
- **Source**: Phonon x Landau, Section VI (#8); Master, Section VI (E2)
- **What**: On 992 modes at N_pair = 1, verify that obstructions 1 (pairing collapse) and 3 (monotonicity) break while obstructions 2 (Anderson) and 6 (integrability) persist. Discriminates between the structural-identity and coincidence interpretations of the dimensional ladder.
- **Inputs**: 992-mode continuum spectrum; N_pair = 1 BCS solution
- **Tests**: Whether obstructions break in the predicted pattern under independent variation of N_modes at fixed N_pair
- **Pre-registered gate**: None explicitly defined. Structural if obstructions break in predicted pattern; coincidence if they break uniformly.
- **Cost**: MEDIUM
- **Priority**: MEDIUM (Phonon x Landau)

### 19. Pair Mobility mu_pair Computation
- **Source**: Phonon x Landau, Section VI (#5, sub-item)
- **What**: Compute pair mobility mu_pair = E_1(tau)/2 = J_C2(tau) * lambda_1(graph)/2 at multiple tau values. Landau proved mu_pair is monotonically decreasing; formal computation verifies and resolves the apparent contradiction with S47 superfluid density anti-correlation (rho_s = mu_pair * n_s, where mu_pair decreases and n_s increases).
- **Inputs**: J_C2(tau) values; graph algebraic connectivity lambda_1
- **Tests**: Confirms monotonic decrease; resolves S47 anti-correlation mechanism
- **Pre-registered gate**: None. Verification of proven result.
- **Cost**: ZERO
- **Priority**: LOW

### 20. Brody Parameter / Nearest-Neighbor Spacing Ratio for Two-Pair Space
- **Source**: Phonon x Landau, Section V (Q2 follow-up)
- **What**: At dim = 28 (full two-pair space) with t/d = 3.9, compute the Brody parameter beta (expected 0.7-0.9) and nearest-neighbor spacing ratio <r> (Poisson: 0.386, GOE: 0.531). Within B2 (dim = 6), <r> is the correct diagnostic since Brody is not well-defined at small dimension.
- **Inputs**: Two-pair Hamiltonian eigenvalues
- **Tests**: Integrability-breaking diagnostic
- **Pre-registered gate**: Same as #12 (<r> > 0.48 for GOE, < 0.40 for Poisson)
- **Cost**: LOW (subproduct of N_pair = 2 ED)
- **Priority**: HIGH (part of the D3 computation)

### 21. Continuum Bogoliubov Spectrum Non-Thermality Test
- **Source**: QA x Hawking, Section II (three-ingredient convergence)
- **What**: Compute the 992-mode Bogoliubov spectrum and verify the pre-registerable prediction: smooth (ingredient 3 approximately restored) but non-thermal (ingredients 1 and 2 still absent -- no horizon, no exponential blueshift).
- **Inputs**: 992-mode continuum spectrum; Bogoliubov transformation at transit
- **Tests**: Whether the continuum Bogoliubov spectrum is non-thermal (as predicted from the three-ingredient decomposition)
- **Pre-registered gate**: If the continuum produces a thermal spectrum, the three-ingredient analysis has an error. Non-thermal confirms.
- **Cost**: MEDIUM
- **Priority**: LOW

### 22. E_Rich(tau) on Continuum: Uncomputed Entry in NCG-Nuclear Hierarchy Table
- **Source**: Naz x Connes, Section III (hierarchy table, row 6)
- **What**: The NCG-Nuclear hierarchy table identifies E_Rich (continuum Richardson energy) as UNCOMPUTED. This is the continuum analog of the lattice BCS energy. Same as #2 but noted independently as an explicit gap in the hierarchy table.
- **Inputs**: Same as #2
- **Tests**: Same as #2
- **Pre-registered gate**: Same as #2
- **Cost**: MEDIUM
- **Priority**: CRITICAL (same as #2)

### 23. S_b + S_f Full NCG Action on Continuum
- **Source**: Naz x Connes, Section III (S_fermionic emergence)
- **What**: Compute the full NCG action S_b + S_f on the 992-mode continuum. S_f decomposes as occupation response + spectral drift. On the continuum, B2 quartet near-degeneracy produces sharp occupation redistribution that can make the first term positive. Subsumes #4 as the complete test.
- **Inputs**: 992-mode continuum spectrum; BCS occupation; spectral action computation
- **Tests**: Whether S_b + S_f has a minimum on the continuum
- **Pre-registered gate**: Same as #4 for the fermionic component
- **Cost**: MEDIUM
- **Priority**: HIGH

### 24. Bures Velocity / Fisher Metric Minimum Test
- **Source**: Naz x Connes, Section III (D_BCS emergence); hierarchy table row 5
- **What**: The D_BCS construction predicts competition between geometric expansion and occupation concentration could produce a minimum in the Bures velocity (sublinear Bures-Fisher metric). The hierarchy table lists d_B(tau, tau') as "Sublinear (W2-3)". Test whether the Bures velocity has a minimum.
- **Inputs**: D_BCS data; BCS occupation numbers at multiple tau
- **Tests**: Whether the Bures velocity minimum exists (related to D_BCS stabilization)
- **Pre-registered gate**: None explicitly. Related to #3.
- **Cost**: MEDIUM
- **Priority**: MEDIUM

### 25. N_pair = 2 Diagonal Ensemble Vacuum Energy
- **Source**: Phonon x Landau, Section III (GGE diagonal ensemble refinement, E1)
- **What**: At N_pair = 2 on 8 modes (dim = 28), compute the diagonal ensemble rho_DE = sum_n |c_n|^2 |n><n| and its vacuum energy P_vac(DE). Compare to P_vac(GGE). The system reaches a diagonal ensemble, not thermal equilibrium, at dim = 28 (ETH requires dim > 10^3). Tests whether the CC path requires full thermalization or can work through the diagonal ensemble.
- **Inputs**: Two-pair Hamiltonian eigenstates; initial post-transit state expansion coefficients |c_n|^2
- **Tests**: Whether P_vac(DE) << P_vac(GGE) (CC path via diagonal ensemble)
- **Pre-registered gate**: PASS if P_vac(DE)/P_vac(GGE) < 0.1; FAIL if > 0.5. (Same as #11 but focused on the DE computation.)
- **Cost**: MEDIUM
- **Priority**: HIGH

### 26. N_pair = 3-4 ETH Threshold Test
- **Source**: Phonon x Landau, Section III (E1, GGE refinement); QA x Hawking, Section II (crystal-glass-liquid)
- **What**: At N_pair = 3-4 on 8 modes, the Fock space dimension reaches the ETH threshold (~10^3) and the diagonal ensemble approaches the microcanonical. Compute to verify ETH onset and test connection to Volovik's q-theory self-tuning (Lambda_eff -> 0 in equilibrium).
- **Inputs**: 3-4 pair Hamiltonian on 8 modes
- **Tests**: Whether ETH onset occurs at predicted N_pair; whether microcanonical P_vac approaches zero
- **Pre-registered gate**: None explicitly defined. Exploratory.
- **Cost**: HIGH (Fock space dimension ~10^3)
- **Priority**: LOW (beyond S55 immediate scope)

### 27. Independent Variation of N_pair and N_modes
- **Source**: Phonon x Landau, Section III (dimensional ladder dissent); Master, Section V
- **What**: Increase N_modes at fixed N_pair = 1 (should break obstructions 1, 3, 5 while 2 and 6 persist) and increase N_pair at fixed N_modes = 8 (should break 5 and 6 while 1 and 3 persist). Discriminates structural identity from coincidental threshold.
- **Inputs**: Variable-size lattice and multi-pair computations
- **Tests**: Whether obstructions break in the predicted pattern
- **Pre-registered gate**: None explicitly. Structural if predicted pattern holds; coincidence if uniform breaking.
- **Cost**: HIGH (multiple lattice sizes and pair numbers)
- **Priority**: MEDIUM

### 28. K_7-Dependent Pairing with Off-Jensen Deformations
- **Source**: Phonon x Landau, Section V (Q1 follow-up); Phonon x Landau, Section II (Anderson's theorem)
- **What**: The conjugation symmetry C forces Delta_+ = Delta_- at mean-field level on the Jensen line. Anderson's theorem holds at all tau on-Jensen. Escape requires explicit C-breaking: off-Jensen deformations, fluctuation corrections beyond mean field, or multi-pair occupation-dependent interactions. Compute K_7-dependent pairing with C-breaking perturbations.
- **Inputs**: Off-Jensen metric perturbations; BCS Hamiltonian with C-breaking terms
- **Tests**: Whether off-Jensen deformations produce K_7-dependent pairing gaps
- **Pre-registered gate**: None explicitly defined.
- **Cost**: MEDIUM
- **Priority**: LOW (beyond immediate S55 scope)

### 29. Superfluid Density rho_s as Physical Stabilization Observable
- **Source**: Phonon x Landau, Section III (BCS free energy classification, L1-L2)
- **What**: Landau identifies the superfluid density rho_s (thermodynamic quantity with Meissner kernel interpretation) as the correct physical observable for stabilization, not S_occ. Compute rho_s(tau) on the lattice and continuum. F_GL(tau) = -a(tau)^2/(4b(tau)) is monotone on the lattice because N(E_F) is essentially constant.
- **Inputs**: BCS gap, density of states, Meissner kernel
- **Tests**: Whether rho_s has non-monotone behavior on the continuum
- **Pre-registered gate**: None explicitly defined.
- **Cost**: MEDIUM
- **Priority**: MEDIUM

### 30. Coleman-De Luccia Bounce Action and Zero-Point Fluctuation
- **Source**: QA x Hawking, Section V (Q6a answer)
- **What**: Hawking computed S_bounce ~ 4.7 x 10^6 (Coleman-De Luccia). Quantum stable against tunneling. But zero-point amplitude delta_tau_0 ~ 0.01 is comparable to barrier width ~ 0.05 -- marginal. Full computation needed to determine if zero-point fluctuations destabilize the putative minimum.
- **Inputs**: Modulus potential (from whichever stabilization candidate has a minimum); zero-point dynamics
- **Tests**: Whether zero-point fluctuations destabilize the modulus
- **Pre-registered gate**: None explicitly. Tunnel-stable confirmed; ZPF-marginal flagged.
- **Cost**: LOW
- **Priority**: LOW (downstream of stabilization candidate confirmation)

### 31. Acoustic Horizon Evolution on Fabric
- **Source**: QA x Hawking, Section III (acoustic horizon emergence, E2 + E4)
- **What**: Compute r_fabric(tau) = t/H(tau) on the tessellated fabric at multiple tau values. Identify the critical inter-cell coupling t_critical ~ H * L_cell = 3.706 M_KK. Determine whether the dimensionless ratio t/(H * L_cell) exceeds 1 at any tau, permitting thermalization.
- **Inputs**: Inter-cell coupling t; H(tau) at multiple tau; cell size L_cell
- **Tests**: Whether acoustic-causal protection fails on the fabric, enabling the CC through thermalization
- **Pre-registered gate**: Overlaps with #10 (FABRIC-COUPLING-55) and #15 (FABRIC-REENTER-55).
- **Cost**: LOW
- **Priority**: MEDIUM

### 32. Non-Trivial Bundle Topology Route to 4D Expansion
- **Source**: Master, Section VII (#3, unresolved question)
- **What**: All three workshops agree the Connes distance growth is compliance expansion (spectral softening), not geometric expansion. Whether compliance expansion drives 4D spacetime expansion through a mechanism not captured by the O'Neill A-tensor remains unresolved. The non-trivial bundle topology route (Baptista, master collab) was not explored in the workshops.
- **Inputs**: Baptista bundle topology framework; O'Neill A-tensor analysis
- **Tests**: Whether non-trivial bundle topology converts compliance expansion to 4D geometric expansion
- **Pre-registered gate**: None defined. Open question.
- **Cost**: MEDIUM
- **Priority**: MEDIUM (unresolved by all three workshops)

### 33. Coupling Regime Classification on Continuum
- **Source**: Master, Section VII (#6, unresolved question); Master, Section IV (emergence 1)
- **What**: Determine where the physical system sits in the coupling landscape. At g*N(E_F) = 0.015 on 32 cells, it is deep weak-coupling. On the continuum at B2 near-degeneracy, it may approach intermediate coupling. The stabilization candidates span different coupling regimes. Which regime governs depends on the DOS at the Fermi level.
- **Inputs**: 992-mode continuum DOS at Fermi level; coupling constant g
- **Tests**: Whether the physical system is in intermediate coupling on the continuum (where F(tau, T_GH) is the correct functional)
- **Pre-registered gate**: None defined. Classification result.
- **Cost**: LOW (subproduct of continuum computations)
- **Priority**: MEDIUM

### 34. GGE-to-Diagonal-Ensemble Decay Timescale at N_pair = 2
- **Source**: QA x Hawking, Section II (crystal-glass-liquid); Phonon x Landau, Section III (E1)
- **What**: Compute the scrambling timescale t_scramble at N_pair = 2. Hawking estimates ~ 4.4 M_KK^{-1} (O(1) natural units, fast scrambling, V/D = 55 Ericson regime). Verify whether the GGE -> diagonal ensemble transition occurs on a timescale shorter than the transit.
- **Inputs**: Two-pair Hamiltonian; Fock-space dynamics
- **Tests**: Whether the GGE decays fast enough for the CC mechanism to operate during transit
- **Pre-registered gate**: None explicitly defined.
- **Cost**: MEDIUM (subproduct of N_pair = 2 ED)
- **Priority**: MEDIUM

### 35. Integrability-Breaking Rate at N_pair = 2
- **Source**: Phonon x Landau, Section V (P4-Q1 answer)
- **What**: Landau computed the integrability-breaking rate Gamma ~ (t/g)^2 * d, with Gamma ~ 0.76 M_KK at N_pair = 2 -- O(1) natural timescale. Verify this estimate numerically from the two-pair Hamiltonian.
- **Inputs**: Two-pair Hamiltonian with inter-cell hopping
- **Tests**: Whether integrability breaks on the expected O(1) timescale
- **Pre-registered gate**: None explicitly defined.
- **Cost**: LOW (subproduct of N_pair = 2 ED)
- **Priority**: MEDIUM

### 36. omega_att = 9*(B3-B1) Tau-Sweep Confirmation
- **Source**: Implicit from MEMORY.md (S38 permanent result: "omega_att = 9*(B3-B1) at 0.08% precision -- OPEN (tau-sweep needed to confirm/deny)")
- **What**: The S38 near-resonance omega_att = 9*(B3-B1) at 0.08% precision remains OPEN, requiring a tau-sweep to confirm or deny. Not explicitly mentioned in S54 workshops but carried forward as an open computation.
- **Inputs**: B1, B3 eigenvalues across tau sweep
- **Tests**: Whether the 0.08% precision relation holds across tau
- **Pre-registered gate**: None defined. Confirmation/denial of structural identity.
- **Cost**: LOW
- **Priority**: LOW

---

## Open Questions That Could Become Computations

### OQ1. Is S_occ the Correct Action?
- **Source**: Master, Section VII (#1)
- **What**: Three workshops diagnosed symptoms but the zeta computation (formal execution) remains unperformed. Resolved by computation #1.

### OQ2. What Stabilizes the Modulus?
- **Source**: Master, Section VII (#2)
- **What**: Three candidates exist; all uncomputed at S55 scope. Resolved by computations #1, #2, #3, #8, #9.

### OQ3. Does Compliance Expansion Correspond to Anything in 4D?
- **Source**: Master, Section VII (#3)
- **What**: All workshops agree Connes distance is compliance, not geometric. The non-trivial bundle topology route unexplored. See computation #32.

### OQ4. What Breaks Integrability at N_pair >= 2 and Does It Solve the CC?
- **Source**: Master, Section VII (#4)
- **What**: CC path open but doubly gated (algebraic + acoustic-causal). See computations #11, #12, #25, #26, #34, #35.

### OQ5. Is the Dimensional Ladder Structural or Coincidental?
- **Source**: Master, Section VII (#5)
- **What**: Seven obstructions break at N_pair >= 2, N >= 66 modes. Landau's caveat untested. See computations #18, #27.

### OQ6. Coupling Regime of the Physical System
- **Source**: Master, Section VII (#6)
- **What**: Which coupling regime governs? See computation #33.

### OQ7. Is S_fermionic Non-Monotone on Continuum?
- **Source**: Naz x Connes, Section III
- **What**: Connes claims S_f is NOT monotone on continuum due to B2 near-degeneracy. See computation #4.

### OQ8. Does D_BCS Provide Stabilization?
- **Source**: Naz x Connes, Section III
- **What**: The state-dependent spectral triple is the workshop's highest-value new construction but entirely uncomputed. See computation #3.

### OQ9. Does F(tau, T_GH) Have a Minimum?
- **Source**: QA x Hawking, Section III
- **What**: Qualitative analysis says LIKELY but uncomputed. See computation #8.

### OQ10. Does the Strutinsky-NCG Bridge Hold on the Continuum?
- **Source**: Naz x Connes, Section IV (dissent); Phonon x Landau, Section III
- **What**: Components survive independently; bridge as framework disputed. Requires continuum computation. See computation #17.

### OQ11. Transit Classification: Landau-Zener vs Kibble-Zurek
- **Source**: Phonon x Landau, Section IV (dissent)
- **What**: At S55 scope (32 cells, N_pair <= 2), Landau-Zener is exact. Kibble-Zurek requires genuine phase transition at N_pair >> 1 with d/Delta < 1. Domain relevance dissent survives.

### OQ12. 24% vs 27% Information Capacity Coincidence
- **Source**: QA x Hawking, Section IV (dissent)
- **What**: QA argues structural (B2 quartet dominance); Hawking argues accidental (different scaling dimensions). See computation #14.

### OQ13. Transit Velocity Dependence of GGE Temperatures
- **Source**: QA x Hawking, Section IV (dissent)
- **What**: Both agree in extreme diabatic limit; dissent over moderate variations. See computation #13.

### OQ14. Acoustic Horizon Scope at Cell Scale
- **Source**: QA x Hawking, Section IV (dissent, resolved to partial agreement)
- **What**: Narrowed to whether the acoustic horizon concept applies at the cell scale at all. Richardson-Gaudin state is global (Hawking) vs supersonic isolation (QA).

### OQ15. rho + 3P Invariance and Grand Canonical Escape
- **Source**: QA x Hawking, Section II (Euler tautology convergence)
- **What**: P_vac = 1 - E_GGE unchanged by thermalization at N_pair = 1 (canonical). CC exit requires grand canonical N_pair fluctuations. See computations #11, #25.

---

## Summary of Pre-Registered Gates

| Gate ID | Computation | PASS Criterion | FAIL Criterion | Source |
|:--------|:-----------|:---------------|:---------------|:-------|
| (zeta monotonicity) | #1 zeta'_D on 32-cell | Non-monotone (S_occ strengthened) | Monotone (S_occ is cutoff artifact) | All 3 workshops |
| (E_Rich continuum) | #2 E_Rich on 992-mode | Minimum in [0.10, 0.30] | Monotone | Naz x Connes, Phonon x Landau |
| (D_BCS distance) | #3 D_BCS on 32-cell | Minimum exists | Monotone | Naz x Connes |
| (S_fermionic continuum) | #4 dS_f/dtau on 992-mode | Positive anywhere in [0.10, 0.30] (S_b+S_f OPEN) | Uniformly negative (CLOSED on continuum) | Naz x Connes |
| EUCLID-55 | #8 F(tau, T_GH) on 32-cell | Minimum in [0.10, 0.30], barrier > 1% | Monotone or barrier < 0.1% | QA x Hawking |
| EUCLID-CONTINUUM-55 | #9 F(tau, T_GH) on 992-mode | Barrier on continuum > barrier on 32-cell | Barrier weaker on continuum | QA x Hawking |
| FABRIC-COUPLING-55 | #10 t/(H*L_cell) | Ratio > 1 (thermalization possible) | Ratio < 1 (GGE acoustically protected) | QA x Hawking |
| NPAIR2-CC-55 | #11 P_vac(DE)/P_vac(GGE) | < 0.1 (CC path viable) | > 0.5 (CC path closed) | Phonon x Landau, QA x Hawking |
| (level statistics) | #12 <r> for two-pair space | > 0.48 (GOE, integrability broken) | < 0.40 (Poisson, integrable) | Phonon x Landau |
| TRANSIT-VELOCITY-55 | #13 T_k(omega_tau) | dT_k/d(omega_tau) nonzero for >= 1 sector | All dT_k/d(omega_tau) < 0.01 | QA x Hawking |
| XI-CONTINUUM-55 | #14 xi on 992-mode | \|xi - S/S_BH\| < 0.05 (structural) | \|xi - S/S_BH\| > 0.10 (accidental) | QA x Hawking |
| FABRIC-REENTER-55 | #15 r_fabric(tau) | Re-entry occurs (reheating) | r_fabric < L_cell at all tau (eternal isolation) | QA x Hawking |
| SELF-CONSISTENT-LOOP-55 | #16 dF/dtau = 0 fixed point | Fixed point with positive Hessian | No fixed point or unstable | QA x Hawking |

---

Total suggestions extracted: 36 (36 computations/recommendations + 15 open questions) from 4 workshop syntheses