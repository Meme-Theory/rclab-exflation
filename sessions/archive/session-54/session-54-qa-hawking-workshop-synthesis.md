# QA x Hawking Workshop Synthesis: Session 54
## Quantum Acoustics Meets Semiclassical Gravity on the 32-Cell Lattice

**Date**: 2026-03-22
**Workshop**: 2 rounds, 4 turns (1144 lines)
**Agents**: QA (quantum acoustics -- phonon modes, dispersion, lattice dynamics), Hawking (semiclassical gravity -- particle creation, information paradox, singularity theorems, Euclidean methods)
**Source**: Session 54 results + both prior workshop syntheses
**Prior workshops**: Naz x Connes (S_occ OPEN with caveats, D_BCS emerged); Phonon x Landau (dimensional ladder, integrability breaking, compliance-redshift duality)

---

### I. The Central Result

The workshop's headline emergence is a new stabilization candidate that neither prior workshop identified: the Euclidean free energy F(tau, T_GH) evaluated at the Gibbons-Hawking temperature T_GH = H/(2 pi) = 0.59 M_KK, derived from the lattice expansion rate. Hawking introduced this in his H2 analysis (Round 1), reasoning from the Euclidean path integral: the thermal partition function Z[tau] = Tr exp(-beta H_BCS(tau)) at T_GH defines a free energy F = E_0 - T_GH * S whose entropy term depends on the level spacing structure. Near the van Hove singularity, enhanced DOS increases S, pulling F downward. The competition between spectral softening (lowering E_k, increasing occupation and entropy) and Gibbons-Hawking cooling (H decreasing post-fold, lowering T_GH and hence the entropy weight) can produce a minimum near the fold.

QA recognized this immediately as the workshop's most consequential result: the first functional in the framework's history that couples the acoustic and gravitational sectors without a free parameter. The temperature is not imposed -- it is derived from the expansion rate, which is itself derived from the spectral softening. The self-consistency loop is closed: spectral softening produces expansion, expansion sets T_GH, T_GH determines the free energy, and the free energy minimum (if it exists) determines where the spectral softening halts. Hawking's quantitative analysis of dF/dtau (E5, Round 2) found the minimum LIKELY near the fold: the spectral softening dominates at the fold while the cooling effect strengthens post-fold, and the competition crosses zero somewhere in between.

This functional replaces S_occ as the primary stabilization candidate. Both agents converged (Round 2) that zeta'_D is monotone on the 32-cell lattice (Landau's proof) and likely monotone on the 992-mode continuum (4 B2 modes out of 992 cannot overturn 988 monotonically decreasing modes). The S_occ minimum is confirmed as a sharp-cutoff artifact. F(tau, T_GH) is cutoff-independent (Z converges for any bounded spectrum), self-consistent (T derived from the dynamics), and computable from existing S54 eigenvalue data at zero cost.

---

### II. What Converged

**Three missing ingredients for thermality (QA Q2a + Hawking R1, accepted by both).** Hawking decomposed the GGE non-thermality into three independent physical ingredients, each absent from the framework transit:

1. **No horizon** -- the Jensen deformation is smooth on a compact group, making this Parker-type cosmological particle creation, not Hawking radiation. There is no causal boundary separating in/out regions.
2. **No exponential blueshift** -- mode frequencies track Josephson couplings smoothly, with no conformal divergence. The Bogoliubov coefficients depend on d(omega_k)/dtau, not on exponential peeling.
3. **Discrete spectrum** -- 8 modes impose a lattice of allowed frequencies, destroying any smooth Planck distribution.

QA translated these onto acoustic properties: connectivity (all cells linked by finite-velocity paths), smoothness of elastic moduli (polynomial in tau), and band structure discreteness (phononic crystal, not continuum). Each ingredient has an independent physical role: discreteness determines the NUMBER of distinct GGE temperatures (8 vs continuous), the absence of a horizon determines the NON-THERMALITY (Parker spectrum rather than Planck), and integrability determines the PERMANENCE. Both agents record a pre-registerable continuum prediction: the 992-mode Bogoliubov spectrum should be smooth (ingredient 3 approximately restored) but non-thermal (ingredients 1 and 2 still absent). If the continuum somehow produces a thermal spectrum, the analysis has an error.

**Silent point at the fold (Hawking Q4b + QA R2 refinement).** Hawking identified dm^2_B2/dtau = 0 at tau* = 0.190158 as a selection rule: the Landau-Zener formula gives P_LZ -> 0 when the diabatic slope vanishes, making B2-B2 crossings maximally adiabatic at the fold. Particle creation occurs primarily before and after the fold, not at it. QA sharpened: the van Hove singularity IS the mass stationarity condition, so the fold and the silent point are the same physical feature, not a 0.08% coincidence. The B2 modes are simultaneously a BIC in momentum space (v_g = 0), a silent point in moduli space (dm^2/dtau = 0), and the dominant BCS pairing channel (93.3%). The fold is the eye of the storm.

**Quantum defocusing non-universality (Hawking Q1a + QA R2).** Hawking proved the theta_Q > 0 defocusing requires three simultaneous conditions: (1) volume-preserving classical geometry (theta_classical = 0), (2) a nontrivial many-body ground state with tau-dependent entanglement structure (F_Q > 0), and (3) SEC violation from the many-body vacuum energy. QA confirmed acoustically: a phononic crystal with trivial vacuum (Fock |0>) has F_Q = 0 identically, because |<0(tau)|0(tau+dtau)>|^2 = 1 regardless of spring constants. The defocusing is specific to the BCS-on-SU(3) system, not a universal property of compliance expansion.

**Crystal-glass-liquid GGE phases (QA Q3b + Hawking H5).** QA classified the multi-pair evolution: N_pair = 1 is crystal (exact Richardson-Gaudin integrability, permanent GGE), N_pair = 2 is glass (integrability broken, diagonal ensemble via decoherence, no full thermalization at dim = 28), N_pair >= 3-4 is liquid (dim > 10^3, ETH applies, approach to microcanonical). Hawking confirmed with the compound nucleus analogy: t_scramble ~ 4.4 M_KK^{-1} at N_pair = 2 (O(1) natural units, fast scrambling, V/D = 55 Ericson regime). The two-stage GGE decay is physically important: stage 1 is loss of phase coherence between phonon modes (GGE -> diagonal ensemble, non-chaotic, no positive Lyapunov exponent required); stage 2 is redistribution of energy among modes (diagonal ensemble -> microcanonical, requires chaos/ETH). The CC resolution requires reaching the liquid phase -- the glass phase (diagonal ensemble) retains memory of initial conditions through the expansion coefficients |c_n|^2.

**Zeta monotonicity on continuum (Hawking Q5a + QA R2).** Hawking's UV-dominance argument: the zeta function is dominated by UV modes at s -> 0, and the 4 B2 modes with non-monotone tau-dependence are a 0.4% perturbation against 988 monotonically decreasing modes. QA accepted. S_occ is confirmed as a cutoff artifact by all three workshops. The Euclidean free energy F(tau, T_GH) replaces S_occ as the candidate stabilization functional.

**Two quantum metrics are independent (Hawking Q6b).** Band-structure quantum metric g^{band} = 0 (Perron-Frobenius, Landau's proof) measures Bloch state distance in the Brillouin zone. Modulus quantum metric g^{modulus} = F_Q/4 = 0.479 measures BCS ground state distance in moduli space. Different manifolds, different physics. The vanishing of g^{band} (closing the Peotta-Torma route) does not constrain the modulus inertia.

**GSL is kinematic, not thermodynamic (Hawking H1 + QA FQ4).** On the integrable 32-cell lattice, the GSL holds by construction: S_geometric ~ d_D^2 is monotonically increasing (Connes distance grows), S_matter >= 0 (Parker creation only adds occupation). No H-theorem is needed. Hawking qualified QA's "vacuous" label: the GSL constrains the solution space (any mechanism that contracts the Connes distance is excluded) even though it says nothing about approach to equilibrium.

**T_GH = 0.59 M_KK as natural temperature (Hawking H2 + QA R2).** The Gibbons-Hawking temperature from the expansion rate sits between T_B2 = 0.668 and T_B1 = 0.435, within the GGE temperature distribution. Both agents accept this as the natural temperature for the Euclidean partition function of the lattice.

**DeWitt-Schwinger analog identified (Hawking Q5b).** One-loop: Gamma = -(1/2) zeta'_{D^2}(0, tau). Many-body: Gamma_MB = -ln Z. S_occ is neither -- it is a hybrid with no derivation from either path integral. The correct effective action depends on coupling strength: one-loop dominates at weak coupling (g*N(E_F) = 0.015 on 32 cells), many-body dominates when g*N(E_F) ~ O(1) (continuum).

**rho + 3P invariant within canonical N_pair = 1 (Hawking E7).** The Euler tautology P = 1 - E at canonical N_pair = 1 forces rho + 3P = 3 - 2E for ANY state at fixed energy. Thermalization within N_pair = 1 cannot change the gravitational source term. QA proposed that the Volovik q-theory thermodynamic identity Lambda_eff -> 0 in equilibrium could provide a CC path through thermalization, but Hawking proved the Euler tautology is canonical, not just a GGE property -- both the GGE and the Gibbs state at E = 1.688 M_KK have identical P_vac = -0.688. The CC exit requires grand canonical N_pair fluctuations (N_pair >= 2), where the Euler tautology can break.

**Information budget 7:1 (Hawking H3).** The GGE relic contains 8 mode occupations (~8 nats of information). A 4D observer measuring only the stress-energy tensor can access 1 number (total energy density rho). The remaining 7 nats are permanently hidden by the KK projection. This is the framework's version of the information paradox, but without a paradox: unitarity is preserved sector by sector, the internal and 4D sectors decouple, and there is no evaporation mechanism. On the tessellated fabric (~10^{183} cells), the total hidden information is ~10^{184} bits -- vastly exceeding the Bekenstein bound for the observable universe (~10^{122} bits). The resolution: internal information does not contribute to the holographic bound because it is geometrically orthogonal to the 4D area. The maximum N_pair per cell is set by Pauli exclusion, not holographic entropy bounds (Bekenstein bound trivially satisfied, E8).

**Singularity avoidance is perturbative (Hawking Q4a).** The theta_Q > 0 defocusing is necessary but not sufficient for singularity avoidance. The 24% quantum correction (xi = 0.24 at fold) slows the transit but does not halt it. No singularity exists in the standard sense (SU(3) is compact at all tau). The "singularity" would be tau -> infinity (geometric collapse), and the quantum defocusing adds a repulsive potential proportional to F_Q that resists large tau -- but the dynamical stabilization question (whether F(tau, T_GH) or E_Rich provides a binding potential) is decisive, not the Raychaudhuri correction.

**Trans-Planckian separation confirmed on lattice (Hawking H4).** Particle creation (Bogoliubov coefficients from MASSEY-FOLD-54) is UV-safe -- it depends on gap structure at each avoided crossing, an IR quantity. The spectral action (S_occ from SA-LATT-OCC-54) is UV-sensitive -- it depends on the cutoff Lambda. This separation confirms the S46 result and the S37 "play vs stage" distinction: the physical observables (GGE particle content) are cutoff-independent while the stabilization functional (S_occ) is cutoff-dependent.

---

### III. What Emerged

**Euclidean free energy as self-consistent stabilization (QA E1 + Hawking E5).** F(tau, T_GH(tau)) = -T_GH(tau) * ln Z_BCS(tau, T_GH(tau)) is the first functional coupling acoustic and gravitational sectors without free parameters. The self-consistency loop is the physical core: spectral softening drives expansion, expansion determines T_GH = H/(2 pi), T_GH sets the partition function weight, and the free energy minimum (if it exists) determines where the modulus halts -- closing the loop. QA identified this as the phononic analog of Gibbons-Hawking thermal equilibrium: a de Sitter space reaches thermal equilibrium with its own radiation at T_dS. Here, the phononic crystal reaches equilibrium with the "radiation" generated by its own compliance expansion.

Hawking analyzed dF/dtau quantitatively (E5): the spectral softening (lower E_k -> higher occupation -> higher entropy -> lower F) competes with Gibbons-Hawking cooling (H decreasing post-fold -> lower T_GH -> lower entropy weight -> higher F). At the fold, spectral softening is maximal (van Hove singularity) while cooling is moderate (q = -0.786). Post-fold, cooling accelerates (q > 0, H drops faster). The bandwidth drops 82% over the full tau range while H drops only 35%, suggesting spectral softening dominates and the competition crosses zero near the fold. Minimum is LIKELY but uncomputed. Computable from existing S54 eigenvalue data at 50 tau points with zero new cost.

**Acoustic horizon on the fabric (QA R2 dissent + Hawking E4 resolution).** QA computed r_sonic = v_sound / H = 0.25 cells at the fold -- the expansion is supersonic, and every cell is acoustically isolated. Hawking partially accepted but refined the scope. Within a single cell, the acoustic horizon is irrelevant because the Richardson-Gaudin state is global (all 8 pair modes are entangled with the vacuum simultaneously; the Bogoliubov transformation is a global operation on the full Hilbert space that does not require acoustic signal propagation).

On the spatially extended fabric, the acoustic horizon is real and controlled by the dimensionless ratio t / (H * L_cell), where t is the inter-cell Josephson coupling. The CC requires BOTH algebraic protection (Richardson-Gaudin integrability) AND acoustic-causal protection (acoustic horizon) to fail. These coincide on 32 cells but separate on the fabric.

**Dual GGE protection (Hawking E4).** Two independent protections against GGE decay: (1) algebraic (exact Richardson-Gaudin integrability within each cell), (2) acoustic-causal (acoustic horizon prevents inter-cell communication during transit). At N_pair >= 2 on the fabric, algebraic protection breaks (inter-pair interactions) but acoustic-causal protection persists if t / (H * L_cell) < 1. The CC requires both to fail simultaneously.

**Three-candidate stabilization hierarchy (Hawking E6).** The workshop clarified three distinct stabilization candidates, ordered by theoretical rigor:

| Rank | Functional | Physics Included | Cutoff Status | Assessment |
|:-----|:-----------|:----------------|:-------------|:-----------|
| 1 | Gamma = -(1/2) zeta'_D(0, tau) | One-loop spectral geometry (free Dirac fields) | Independent (zeta regularization) | Monotone on 32 cells (proved). Likely monotone on continuum (UV dominance). Likely CLOSED. |
| 2 | F(tau, T_GH(tau)) | Thermal effects at Gibbons-Hawking temperature | Independent (Z converges for bounded spectrum) | Self-consistent (T from expansion rate). Minimum LIKELY near fold. PRIORITY S55. |
| 3 | E_0^Rich(tau, N_pair >= 2) | Full many-body BCS with inter-pair interactions | N/A (exact diag) | Includes all pairing physics. Requires multi-pair computation. VIABLE, UNTESTED. |

The hierarchy reflects a trade-off: (1) is the most rigorous but has no many-body physics; (2) includes thermal effects but not pairing; (3) includes everything but requires the most computation. If (2) has a minimum, stabilization is thermodynamic (Gibbons-Hawking equilibrium), independent of whether pairing works. The physical picture: the modulus tau evolves until the phononic crystal reaches thermal equilibrium with the "radiation" generated by its own spectral softening, at the temperature T_GH = H/(2 pi) derived from the expansion rate itself.

**Silent-point-as-BIC acoustic laser (QA E3).** The fold is simultaneously a bound state in continuum (v_g = 0 from flat dispersion), a silent point for particle creation (dm^2/dtau = 0 from mass stationarity), and the BCS pairing maximum (93.3% of the condensate in B2). In acoustic physics, this combination is a phonon laser: a mode with infinite lifetime (BIC), zero particle creation/annihilation rate at the operating point (silent), and strong cooperative coupling (BCS condensation). QA interprets: the fold is the lasing threshold. Below the fold, B2 modes are sub-threshold (too stiff, no van Hove enhancement). At the fold, they reach threshold in all three channels simultaneously. Above the fold, the B2 mode begins to create particles (dm^2/dtau departs from zero) and loses its BIC character (dispersion develops) -- stimulated emission of quasiparticle pairs produces the GGE. The instanton gas IS the above-threshold phonon laser output. This connects to the S37 paradigm shift: the fold is not a stabilization point but a threshold the phononic crystal crosses.

**Hairy black hole analogy for GGE (Hawking Q7a).** The multi-temperature GGE ({T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178}) is the internal-space analog of a hairy black hole with nontrivial external fields beyond (M, J, Q). The 8 Richardson-Gaudin integrals are the "hair." A 4D observer measuring only T_{mu,nu} sees a perfect FRW metric (the analog of the no-hair exterior), but an observer probing the internal structure detects the non-thermal distribution. Critical difference from black holes: the no-hair theorem FAILS permanently at N_pair = 1 because integrability prevents relaxation (a black hole's hair is dynamically radiated away on the quasinormal mode timescale). At N_pair >= 2, integrability breaks and the hair is "shaved off" on the scrambling timescale t_scramble ~ 4.4 M_KK^{-1}. The S40 result (NOHAIR-40: FAIL on T, approximate on S) is consistent: 64.6% temperature variation across modes (hair), 18.1% entropy variation (near-bald).

**No acoustic reheating at cell scale (Hawking E9).** QA asked whether the post-fold deceleration grows the acoustic horizon back above 1 cell (the phononic analog of inflationary reheating). Hawking computed r_sonic(tau) = J_C2(tau)/H(tau) at multiple post-fold tau values and found it SHRINKS monotonically: 0.252 at fold, 0.220 at tau = 0.235, 0.192 at tau = 0.347. J_C2 decays exponentially (exp(-4*tau)) while H decays sub-exponentially. Modes never re-enter the acoustic horizon during transit at the single-cell level. Fabric-scale re-entry depends on the inter-cell coupling t(tau) -- if t is approximately constant while H decays, the fabric-scale acoustic horizon r_fabric = t/H could grow, potentially enabling partial thermalization. This is a fabric-scale question not answerable from the 32-cell data.

**Acoustic horizon as UV/IR bridge (QA E2 + Hawking E4).** QA identified that the acoustic horizon radius r_sonic sets a natural length scale on the lattice: modes with wavelength lambda > r_sonic are "super-horizon" and freeze during transit, while modes with lambda < r_sonic can propagate and thermalize. On 32 cells, r_sonic < 1 cell, so ALL modes are super-horizon -- this provides an acoustic explanation of GGE permanence independent of Richardson-Gaudin integrability. On the fabric, the critical inter-cell coupling is t_critical ~ H * L_cell = 3.706 M_KK. The dimensionless ratio t/(H*L_cell) is the acoustic CC gatekeeper: above 1, thermalization is acoustically permitted; below 1, the GGE is acoustically protected.

---

### IV. What Remains in Dissent

**24% vs 27% information capacity coincidence (survived 2 rounds).** QA argues both xi = F_Q/F_Q^max = 0.24 and Bekenstein saturation = 0.27 scale as N_active/N_total ~ 4/16 = 0.25 because B2 dominates both quantities; the acoustic derivation (B2 quartet out of 16 Fock states) predicts the coincidence is structural and will persist on the continuum. Hawking counters that the Bekenstein bound S_BH depends on the 4D area (M_Pl^{-2}), not the internal mode count, while xi depends on mode count; S_spectral ~ Vol(SU(3)) ~ M_KK^{-8} and S_BH ~ Area_4D ~ M_Pl^{-2} scale with different powers of the geometry and decouple on the continuum. Hawking predicts the Bekenstein saturation stays at ~27% while xi evolves to ~N_B2/N_total ~ 250/992 ~ 0.25 (accidentally close). Pre-registerable test: compute both on 992-mode continuum; structural if |xi - S/S_BH| < 0.05, accidental if > 0.10.

**Transit velocity dependence of GGE temperatures (survived 2 rounds).** Hawking: in the deeply diabatic limit (xi ~ 10^{-6}), alpha ~ 0 -- temperatures are independent of omega_tau because occupation numbers freeze to initial BCS values regardless of velocity. QA: the Kibble-Zurek freeze-out point shifts with omega_tau through the initial BCS state; a phononic crystal undergoing rapid spring-constant modulation freezes its phonon distribution at the moment when the modulation rate exceeds the phonon relaxation rate, and the frozen distribution carries memory of WHEN it froze. Moderate velocity changes (factors of 2-5) produce measurable T_k variation even in the diabatic regime. Both agree in the extreme diabatic limit; dissent is over moderate variations. Pre-registerable: vary omega_tau by factors of 0.5-5 and track T_k.

**Acoustic horizon scope (resolved to partial agreement).** QA computed r_sonic = v_sound/H = 0.25 cells at the fold -- supersonic expansion, every cell acoustically isolated. Hawking accepted the mathematics and the physical conclusion for the fabric but rejected the cell-scale interpretation: the 32-cell lattice represents a single KK cell, the Richardson-Gaudin ground state is global (all 8 pair modes entangled with the vacuum simultaneously), and the diabatic transit preserves this global state through a global Bogoliubov transformation that does not require acoustic signal propagation. Hawking retracted his own "trivial causal structure" claim from H6 and replaced it with: trivial causal structure WITHIN a single cell (global state), nontrivial acoustic causal structure ON the fabric (controlled by t/(H*L_cell)). The dissent narrowed to whether the acoustic horizon concept applies at the cell scale at all.

---

### V. Hawking's Answers to the 16 Questions

| # | Question (QA) | Answer (Hawking) | Key Result |
|:--|:-------------|:-----------------|:-----------|
| Q1a | Is quantum defocusing universal for compliance expansion? | No. Requires: volume-preserving, nontrivial many-body state, SEC violation. Trivial vacuum has F_Q = 0. | NON-UNIVERSAL |
| Q1b | Does 24% xi signal information capacity limit? | No. 24% measures Fock space bandwidth usage, not Bekenstein capacity. 8 modes too small for holographic bounds. Coincidence with 27% is accidental. | ACCIDENTAL (disputed by QA) |
| Q2a | What prevents thermality: discreteness, integrability, or both? | Three separate physics: no horizon -> non-thermality; discrete spectrum -> number of temperatures; integrability -> permanence. | THREE INGREDIENTS |
| Q2b | Is there T_eff = omega_tau/(2pi*...)? | No exact formula (Parker, not Hawking). Mode-dependent T_eff(omega) exists but does not reproduce GGE. Deeply diabatic: alpha ~ 0. | NO SIMPLE FORMULA |
| Q3a | Is F_Q peak a Page curve analog? | Physically meaningful but structurally distinct. Page: entanglement entropy between spatial subsystems. F_Q: parameter sensitivity. Both peak at critical points. | PARALLEL, NOT EQUIVALENT |
| Q3b | Can GGE decay without chaos? | Yes. (1) Prethermalization: GGE -> diagonal ensemble (non-chaotic). (2) Decoherence without chaos. Full thermalization (DE -> microcanonical) does require chaos/ETH. | TWO-STAGE DECAY |
| Q4a | Does theta_Q > 0 guarantee singularity avoidance? | No. Necessary but not sufficient. 24% correction is perturbative. No singularity to avoid (SU(3) compact). Stabilization question is decisive. | PERTURBATIVE, NOT QUALITATIVE |
| Q4b | Does dm^2/dtau = 0 create a silent point? | Yes. Selection rule: B2-B2 Bogoliubov mixing suppressed at fold (P_LZ -> 0 when diabatic slope vanishes). Fold = eye of the storm. | SILENT POINT CONFIRMED |
| Q5a | Can van Hove break zeta monotonicity on continuum? | Likely no. 4 B2 modes vs 988 monotonic modes = 0.4% perturbation. Zeta dominated by UV modes. Expect monotone with inflection near tau = 0.19. | LIKELY MONOTONE |
| Q5b | What is the DeWitt-Schwinger analog? | One-loop: Gamma = -(1/2) zeta'_{D^2}. Many-body: Gamma_MB = -ln Z. S_occ is neither. Correct functional depends on coupling regime. | THREE FUNCTIONALS IDENTIFIED |
| Q6a | What is S_bounce for modulus tunneling? | S_bounce ~ 4.7 x 10^6 (Coleman-De Luccia). Quantum stable. But zero-point amplitude delta_tau_0 ~ 0.01 comparable to barrier width ~ 0.05. Marginal. | TUNNEL-STABLE, ZPF-MARGINAL |
| Q6b | Are band-structure and modulus quantum metrics independent? | Yes. g^{band} on Brillouin zone, g^{modulus} on tau-line. Different manifolds. g^{band} = 0 does not constrain modulus inertia. | INDEPENDENT |
| Q7a | Is multi-T GGE analogous to hairy BH? | Yes, precisely. 8 RG integrals = "hair." Permanent at N_pair = 1 (no-hair theorem fails). Shaved at N_pair >= 2 on scrambling timescale. | HAIRY BH ANALOG |
| Q7b | Self-consistent expansion-thermalization equilibrium? | No Abbott-type solution. Euler tautology: P_vac = 1 - E_GGE unchanged by thermalization at N_pair = 1 (energy conservation + canonical constraint). | CC LOCKED AT N_PAIR = 1 |
| Q8a | How does van Hove structure Bogoliubov coefficients? | Block structure: B2-B2 mixing suppressed (silent point); B2-B1/B3 cross-sector mixing strong. DOS divergence -> logarithmic concentration of particle creation near B2 energy. | BLOCK STRUCTURE + LOG DIVERGENCE |
| Q8b | Is d_s = 2 an acoustic near-horizon analog? | Structural connection to UV d_s -> 2 running in quantum gravity. But finite-size effect on 32 cells, not UV fixed point. d_s = 2 means logarithmically slow information propagation -- consistent with GGE permanence. | STRUCTURAL CONNECTION, NOT DYNAMICAL |

---

### VI. Priority Computations for S55

1. **EUCLID-55**: Compute F(tau, T_GH(tau)) = -T_GH(tau) * ln Z_BCS(tau, T_GH(tau)) from existing 32-cell eigenvalue data at 50 tau points. Zero cost beyond partition function evaluation. Pre-register: PASS if minimum in [0.10, 0.30] with barrier > 1% of F(min). FAIL if monotone or barrier < 0.1%.

2. **EUCLID-CONTINUUM-55**: Repeat EUCLID-55 on 992-mode continuum spectrum. Tests whether van Hove DOS enhancement strengthens the minimum. Pre-register: PASS if barrier on continuum exceeds barrier on 32 cells.

3. **FABRIC-COUPLING-55**: Estimate inter-cell Josephson coupling t in the tessellated fabric. Compute the acoustic CC gatekeeper ratio t / (H * L_cell). Pre-register: PASS (thermalization possible) if ratio > 1. FAIL (GGE acoustically protected) if ratio < 1.

4. **NPAIR2-CC-55**: At N_pair = 2 on 8 modes (dim = 28), compute P_vac(diagonal ensemble) vs P_vac(GGE). Tests whether grand canonical fluctuations break the Euler tautology. Pre-register: PASS (CC path viable) if P_vac(DE)/P_vac(GGE) < 0.5.

5. **TRANSIT-VELOCITY-55**: Vary omega_tau by factors of 0.5, 2, 5 in the Landau-Zener cascade on 32 cells. Measure T_k(omega_tau). Pre-register: PASS (velocity-dependent) if dT_k/d(omega_tau) nonzero for at least one sector. FAIL if all dT_k/d(omega_tau) < 0.01.

6. **XI-CONTINUUM-55**: Compute xi = F_Q/F_Q^max on 992-mode continuum. Compare to Bekenstein saturation. Pre-register: structural if |xi - S/S_BH| < 0.05; accidental if > 0.10.

7. **FABRIC-REENTER-55**: On tessellated fabric with estimated t, compute r_fabric(tau) = t/H(tau). Identify whether acoustic re-entry ("reheating point") occurs at any tau > 0.19. Pre-register: PASS (reheating) if re-entry occurs. FAIL (eternal isolation) if r_fabric < L_cell at all tau.

8. **SELF-CONSISTENT-LOOP-55**: Solve the fixed-point condition dF(tau, T_GH(tau))/dtau = 0 self-consistently (T_GH depends on tau through H, which depends on the modulus dynamics governed by F). Pre-register: PASS if fixed point exists with positive Hessian. FAIL if no fixed point or unstable.

---

### VII. Closing

This workshop placed the phonon-exflation framework at the intersection of its two founding disciplines and discovered something neither could find alone. Two prior workshops -- Naz x Connes and Phonon x Landau -- had exhausted the spectral-geometric and condensed-matter routes to stabilization on the 32-cell lattice. The zeta-regularized effective action is monotone. The S_occ minimum is a cutoff artifact. The BCS ground state energy is monotone. Every purely geometric or purely many-body functional fails.

What QA and Hawking found is a functional that is NEITHER purely geometric NOR purely many-body: the Euclidean free energy F(tau, T_GH), where the temperature comes from the gravitational sector (expansion rate) and the partition function comes from the acoustic sector (BCS eigenvalues). The acoustic-gravity interface is not merely a translation layer between two descriptions of the same physics -- it is the domain where new functionals exist that have no analog in either sector alone.

The S_occ minimum status remains OPEN with caveats, consistent with both prior workshops and the master gate PASS (2/3). The Euclidean free energy does not replace S_occ as a result -- it replaces it as a candidate. Whether F(tau, T_GH) has a minimum is an uncomputed question that EUCLID-55 will settle at zero cost.

The workshop also delivered permanent structural results: the three-ingredient decomposition of non-thermality, the silent point selection rule at the fold, the dual (algebraic + acoustic-causal) protection of the GGE, the crystal-glass-liquid phase classification, and the proof that rho + 3P is invariant under thermalization within canonical N_pair = 1. These constrain the solution space regardless of whether EUCLID-55 passes or fails. The acoustic-gravity interface is where this framework lives -- and three workshops in, the interface is producing physics that neither side knew it contained.
