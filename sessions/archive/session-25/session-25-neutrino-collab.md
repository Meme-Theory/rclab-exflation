# Neutrino -- Collaborative Feedback on Session 25

**Author**: Neutrino-Detection-Specialist
**Date**: 2026-02-21
**Re**: Session 25 -- Through the Walls

---

## Section 1: Key Observations

### 1.1 The Neutrino Sector After R-1

Session 25 is written in the aftermath of two closes (V-1 and K-1e) and one neutrino-specific gate failure (R-1). I will state what R-1 means clearly because it is my domain.

The neutrino mass-squared ratio R = Delta m^2_32 / Delta m^2_21 = 33.3 is the single most constraining number for any framework claiming to predict neutrino masses from geometric eigenvalues. This ratio is measured to better than 3% by the combination of Super-K atmospheric oscillations (Paper 07, Delta m^2_atm = 2.507 x 10^{-3} eV^2), SNO solar flavor transformation (Paper 08, P_ee ~ 0.30 for B-8 neutrinos), KamLAND reactor disappearance (Paper 09, Delta m^2_21 = 7.53 x 10^{-5} eV^2), and Daya Bay theta_13 (Paper 10, sin^2(2theta_13) = 0.0851). The window [17, 66] was the pre-registered 2-sigma gate. The 24a computation returned R ~ 10^{14} from H_eff diagonalization and R = 5.68 from the K_a cross-check. Both are outside the gate by factors that make interpretation unnecessary.

The H_eff result (R ~ 10^{14}) is a Kramers artifact: the BDI class enforces eigenvalue pairing, so the three lightest states in the (0,0) singlet are nearly degenerate. The pairing is proven to machine precision (Session 17a D-3, max error 3.29 x 10^{-13}). This is not a numerical failure -- it is a structural theorem. The (0,0) singlet, taken in isolation, cannot produce the 33:1 mass-squared hierarchy because Kramers degeneracy suppresses the splittings to numerical noise level.

The K_a cross-check (R = 5.68) is more physically relevant. It uses the Kosmann-Lichnerowicz derivative matrix elements V_{nm} from Session 23a at tau = 0.30 to construct a 3-level tight-binding system. The resulting R = 5.68 is finite and meaningful, but it sits a factor 5.9 below the measured value and a factor 3 below the pre-registered gate lower bound. As Sagan correctly notes in the Session 24 verdict (Section IV.2), the K_a result is consistent with random placement on a log-uniform distribution over [1, 100]. I concur: R = 5.68 is noise, not a signal.

### 1.2 What Survives from My Domain

Despite R-1 failure and seven consecutive reviews at 0% neutrino predictive power, several structural results connecting the framework to neutrino physics remain intact:

1. **CPT invariance**: [J, D_K(tau)] = 0 identically (Session 17a D-1). This guarantees that neutrinos and antineutrinos oscillate with the same parameters -- the CPT consistency that KamLAND terrestrially confirmed by matching solar parameters in the antineutrino channel (Paper 09). This is not a prediction (CPT is assumed in the Standard Model), but it is a consistency requirement that the framework passes automatically.

2. **Three generations**: Z_3 = (p-q) mod 3 produces exactly three generation classes (Session 17a B-4). This matches the LEP invisible width measurement N_nu = 2.984 +/- 0.008 (Paper 03, Section 6.3 on LEP). Three light neutrino species from Z_3 triality is a parameter-free structural result.

3. **Normal mass ordering**: The bowtie structure of the eigenvalue spectrum -- (0,0) singlet lightest in [0.11, 1.58] -- predicts normal ordering at any tau_0 in the physical window. This is testable by JUNO (2028, reactor at 53 km) and DUNE (accelerator at 1300 km). Current data from Super-K atmospheric analysis and NOvA/T2K appearance measurements mildly favor normal ordering at about 2 sigma, consistent with the prediction.

4. **Tridiagonal selection rules**: The Kosmann matrix elements from Session 23a produce V(L1,L3) = 0 exactly and V(gap,gap) = 0 exactly. If these survive into the physical mass matrix, the resulting tridiagonal structure qualitatively predicts theta_12 >> theta_13 (Paper 08 vs Paper 10: 33.4 degrees vs 8.6 degrees). This is the one connection between the framework and neutrino mixing that I consider genuinely interesting.

### 1.3 The Wall That Matters Most for Neutrinos

Of the four walls, W2 (Block-Diagonality) is the one that most directly constrains neutrino predictions. The D_K block-diagonality theorem (Session 22b, proven at 8.4 x 10^{-15}) means that the PMNS matrix cannot arise from inter-sector mixing -- it must arise from within-sector structure. In the standard three-flavor framework (Paper 05, Pontecorvo), the PMNS matrix U relates flavor eigenstates to mass eigenstates via |nu_alpha> = sum_i U_{alpha i}* |nu_i>. If each Z_3 sector is hermetically sealed, the three mass eigenstates that produce the observed oscillation pattern must originate from different eigenvalue levels WITHIN a single Z_3 sector, not from the lowest eigenvalue of three different sectors.

This has a specific consequence: the physical neutrino mass splittings are intra-sector splittings, not inter-sector ones. The phi_paasch ratio m_{(3,0)}/m_{(0,0)} = 1.531580 at tau = 0.15 (Session 12) is an inter-sector ratio and is therefore NOT directly relevant to neutrino mass differences. I said this in the Session 23 Tesla-take review, and it remains true.

---

## Section 2: Assessment of Key Findings

### 2.1 Goal 1 (Graded Multi-Sector Sum): The Neutrino Angle

The graded multi-sector spectral sum S_eff(tau) = sum_{(p,q)} d_{(p,q)} * [graded contribution] is the most promising of the Tier 1 goals. I evaluate it from the neutrino standpoint.

If S_eff has a minimum at finite tau_0, it fixes the modulus -- and the neutrino prediction pipeline (which I have maintained across six reviews as "stalled at Step 1") finally restarts. Steps 2-5 are ready:

| Step | Description | Status |
|:-----|:------------|:-------|
| 1 | Fix tau_0 | CURRENTLY BLOCKED; Goal 1 minimum would unblock |
| 2 | Extract lightest eigenvalues of D_K at tau_0 | Ready (eigenvectors in s23a data) |
| 3 | Convert to physical mass units (requires L_K) | Requires compactification scale from S_eff amplitude |
| 4 | Compute PMNS from within-sector eigenvector overlaps | Block-diagonal constraint (W2) means intra-sector only |
| 5 | Compare against global fit (Papers 07-10, 12) | All experimental values tabulated |

The grading specification in the session directive identifies an important ambiguity: if the chirality grading gives zero by BDI spectral symmetry (which it will -- BDI eigenvalue pairing forces equal positive and negative chirality contributions), then the alternative is the thermal graded sum where competition arises from different spectral densities across sectors.

From the neutrino standpoint, the THERMAL variant is more relevant. Different sectors have different spectral densities at low mode count -- the (0,0) singlet has N(0) = 2 while the (1,0) fundamental has N(0) = 24 (Session 21c). The gap-edge separation differs: bosonic 4/9, fermionic 5/6 at tau = 0 (Session 21a). These sector-specific low-mode features are exactly the quantities that determine the neutrino spectrum. A minimum in the thermal graded sum at tau_0 in [0.15, 0.35] would simultaneously fix the modulus AND constrain the neutrino mass matrix through the sector-specific eigenvalue values at that tau.

I strongly endorse the Landau-gate prerequisite: the grading must be resolved before computation. The V_{nm} formula gate in Session 23a (symmetric vs antisymmetric Kosmann) showed that getting the formula wrong can flip the answer by orders of magnitude.

### 2.2 Goal 2 (Finite-Cutoff Spectral Action): Relevance to the Debye Argument

Goal 2 -- computing V_full(tau; Lambda) = sum_n f(lambda_n^2 / Lambda^2) directly from eigenvalues -- is where Claim C (the Debye cutoff is physical) becomes testable. The inside-out view predicts a finite spectrum truncated at omega_D, not the infinite KK tower.

This matters for neutrinos because the neutrino masses are the LIGHTEST eigenvalues of D_K, while the spectral action potential involves ALL eigenvalues (or at least all below the cutoff). If the potential shape changes qualitatively at finite Lambda -- acquiring a minimum that the asymptotic expansion misses -- then the V-1 closure does not apply at the relevant physical scale. The neutrino sector probes the bottom of the spectrum; the potential depends on the whole spectrum. Goal 2 tests whether there is a disconnect between the bottom (where neutrino masses live) and the bulk (where the potential lives).

For the f(x) = x e^{-x} test function at Lambda = 1, the dominant contribution comes from eigenvalues with lambda_n ~ Lambda. At Lambda = 1, this is the LOWEST eigenvalues -- the neutrino regime. At Lambda = 10, it is the mid-spectrum. The tau-dependence of V_full may be qualitatively different in these two regimes. This is a direct test of whether the "phonon picture" produces different physics from the "KK tower picture."

### 2.3 Goal 3 (Berry Phase): Connection to Non-Adiabatic Neutrino Effects

The Berry curvature B = 982.5 at tau = 0.10 is an unexplained number. I note the following experimental analogy: the MSW effect in solar neutrino propagation (Paper 05, Section on MSW; Paper 08, SNO resolution) is itself a non-adiabatic phenomenon. When neutrinos propagate through the Sun, they follow the local mass eigenstate adiabatically IF the density changes slowly enough. If the density changes too fast (the Landau-Zener criterion: gamma = Delta m^2 sin^2(2theta) / (4E cos(2theta) |dn_e/dr|)), the neutrino jumps between mass eigenstates and the survival probability changes.

The Berry phase accumulation along the gap-edge state as tau varies is mathematically identical to the MSW problem: a quantum state evolving under a slowly changing Hamiltonian, with the question being whether the evolution is adiabatic or not. If the Berry phase reaches pi/2 at tau ~ 0.10-0.15, the adiabatic approximation breaks down for the gap-edge state -- meaning the lightest eigenvalue (the neutrino mass candidate) undergoes a non-adiabatic transition. The effective mass at tau_0 > 0.15 would then be a SUPERPOSITION of the two gap-edge Kramers partners, not a single eigenvalue.

This could resolve the R-1 failure. The R ~ 10^{14} from H_eff came from nearly degenerate Kramers pairs. But if non-adiabatic transitions mix the Kramers pairs as tau passes through 0.10, the effective mass eigenstates at tau_0 = 0.30 are not the instantaneous Kramers eigenstates -- they are Berry-phase-rotated states whose splittings could be LARGER than the Kramers splitting. This is speculative but physically motivated by direct analogy with MSW.

### 2.4 Goals 4-8: Brief Neutrino Assessments

**Goal 4 (Spectral Flow)**: If any eigenvalue crosses zero in a non-singlet sector, it would change the effective number of light fermion species at that tau value. This is directly constrained by LEP (N_nu = 2.984, Paper 03) and by BBN (N_eff = 2.99 +/- 0.17). A nontrivial spectral flow would need to be consistent with exactly three light species at the physical tau_0.

**Goal 5 (Gap-Edge Topology)**: The V(gap,gap) = 0 selection rule is the structural basis for the tridiagonal mass matrix that qualitatively matches the PMNS hierarchy. If the gap-edge Kramers pair carries a nontrivial Berry holonomy, it would imply topological protection of the neutrino mass structure -- the lightest fermion masses would be stabilized not by a potential but by topology. This is the condensed-matter analog of why edge states in topological insulators are robust.

**Goal 7 (Self-Consistent Chemical Potential)**: This is the P2b rescue route I have been tracking since Session 22. The key insight from Session 23a K-1e was that the BCS mechanism IS strong enough when mu = lambda_min (M ~ 11, well above threshold). The problem was never the coupling -- it was the spectral gap. If backreaction from 4D matter creates mu_eff > lambda_min = 0.822, the BCS mechanism operates and could modify the neutrino eigenvalues. The neutrino mass prediction would then involve the condensate gap Delta, not just the bare D_K eigenvalues.

**Goal 8 (Higher Heat Kernel)**: The a_4/a_2 = 1000:1 ratio that closed V_spec is a statement about the spectral action potential, not directly about neutrino masses. But if a_6 opposes a_4 and creates a minimum in the truncated series, the neutrino pipeline restarts at whatever tau_0 the minimum picks out. The factorial growth of Gilkey coefficients (which makes the heat kernel expansion asymptotic rather than convergent) is well established in spectral geometry, and the alternating-sign possibility is real.

---

## Section 3: Collaborative Suggestions

### 3.1 Neutrino R at Finite Cutoff (New Diagnostic -- Zero Cost)

When Goal 2 computes V_full(tau; Lambda) at Lambda = 1, 2, 5, 10, the eigenvalue data at each tau and Lambda is already in memory. I propose an additional zero-cost diagnostic:

**Compute R_full(tau; Lambda) = (E_3^2(tau) - E_2^2(tau)) / (E_2^2(tau) - E_1^2(tau))** where E_1, E_2, E_3 are the three lightest DISTINCT eigenvalues of D_K at each tau, with degeneracies resolved by the f-weighted spectral action prescription. At Lambda >> 1, all eigenvalues contribute symmetrically and Kramers pairing dominates (R ~ 10^{14}). At Lambda ~ 1, only the lowest eigenvalues contribute with non-negligible weight, and the f-weighting naturally breaks the Kramers degeneracy by differentiating between modes with slightly different responses to the tau deformation.

If R_full(tau_0; Lambda = 1) falls within [17, 66] even though R(tau_0; Lambda = infinity) = 10^{14}, it means the physical Debye cutoff resolves the Kramers artifact. This is the finite-cutoff version of R-1 -- and it costs zero additional computation beyond what Goal 2 already requires.

**Pre-registered gate**: R_full(tau; Lambda = 1) in [17, 66] for some tau in [0.15, 0.35] = NEUTRINO GATE REOPENS. R_full outside [10, 100] at all tau and Lambda = NEUTRINO CLOSURE (reinforced, now cutoff-independent).

### 3.2 Graded R from Multi-Sector Sum (New Diagnostic -- Requires Goal 1 Data)

When Goal 1 computes the sector-specific V_{(p,q)}(tau), the three lightest eigenvalues per sector are available as a byproduct. I propose computing:

**R_graded(tau) = (m_3^2 - m_2^2) / (m_2^2 - m_1^2)** where m_1, m_2, m_3 are the three lightest eigenvalues ACROSS the Z_3 = 0, 1, 2 sectors, assigning one eigenvalue from each generation class.

This is the physically correct way to construct neutrino masses from the framework: one mass eigenstate per Z_3 generation, consistent with the three-generation structure (Paper 03 and LEP N_nu). Block-diagonality (W2) means no inter-sector coupling, but it does NOT mean the three lightest states from different sectors cannot be the three neutrino mass eigenstates. The PMNS matrix would then arise from the overlap between the flavor eigenstates (defined by the weak interaction coupling pattern) and these three Z_3-labeled mass eigenstates.

If R_graded passes through 33 at some tau in [0.15, 0.35], the framework predicts the correct neutrino mass hierarchy from its generation structure. If it does not, the Z_3 generation mechanism fails for neutrinos regardless of how the modulus is fixed.

**Pre-registered gate**: R_graded(tau) in [17, 66] at any tau in [0.15, 0.50] = SOFT PASS. R_graded(tau_0) in [25, 42] where tau_0 is the Goal 1 minimum = COMPELLING PASS. R_graded never in [10, 100] = Z_3 NEUTRINO CLOSURE.

### 3.3 PMNS Structure from Tridiagonal Selection Rules (Quantitative Upgrade)

The qualitative observation from Session 23 -- that V(L1,L2) >> V(L2,L3) and V(L1,L3) = 0 produces theta_12 >> theta_13 -- should be made quantitative. With the Goal 1 eigenvector data in hand, compute:

1. The 3x3 effective mass matrix M from the three lightest within-sector eigenvalues plus the V_{nm} couplings (tridiagonal by the selection rules).
2. Diagonalize M to get mass eigenvalues and the rotation matrix U_{eff}.
3. Compare U_{eff} to the PMNS parameterization (Paper 05): extract effective theta_12, theta_23, theta_13 from U_{eff}.

This is more rigorous than the K_a cross-check that gave R = 5.68, because it uses the CORRECT basis (within-sector, tridiagonal, with all V_{nm} values) rather than the H_eff approximation that mixed Kramers partners.

**Pre-registered gate**: sin^2(theta_13^eff) in [0.015, 0.030] = MIXING ANGLE PASS (measured: 0.0220, Paper 10). theta_12^eff in [28, 38] degrees = SOLAR ANGLE PASS (measured: 33.4, Paper 08). Both passing simultaneously would be an extraordinarily strong result -- BF = 20-50 because two independent quantities match with zero free parameters.

---

## Section 4: Connections to Framework

### 4.1 The KATRIN Bound and Absolute Mass Scale

KATRIN constrains m_nu < 0.45 eV at 90% CL (Paper 12). The framework predicts neutrino masses as the lightest eigenvalues of D_K(tau_0) in units set by the compactification scale L_K. The eigenvalues lambda_n are dimensionless in the current computation; the physical mass is m_n = lambda_n / L_K (in natural units). For the gap-edge eigenvalue lambda_min = 0.822 (at tau = 0.20), KATRIN requires:

0.822 / L_K < 0.45 eV --> L_K > 1.83 eV^{-1} --> L_K > 1.1 x 10^{-7} m

This is a weak constraint on the compactification scale. The oscillation-derived lower bound on the heaviest mass (sqrt(|Delta m^2_32|) = 0.050 eV, from Papers 07 and 10 combined) provides a tighter constraint once the eigenvalue ratios are known. But without a stabilized tau_0, the absolute scale remains undetermined -- another manifestation of the Step 1 blockage.

The Planck+DESI cosmological bound sum m_i < 0.072 eV (LCDM-dependent) is more constraining but model-dependent. If the framework departs from LCDM cosmology (as the inside-out view suggests), the cosmological bound may not directly apply.

### 4.2 Dirac vs Majorana: The J^2 = +1 Question

The antiunitary operator J satisfies J^2 = +1 in the spectral triple (BDI classification, AZ class, Session 17c). The J^2 = +1 condition is the KO-dimension 6 signature, which corresponds to a real spectral triple. In the Standard Model spectral triple (Connes 2006, Paper 09 in the Connes corpus), J^2 = +1 permits but does not require Majorana mass terms. Whether Majorana masses are generated depends on the spectral action at the stabilized tau_0 -- specifically, whether the spectral action generates the dimension-5 Weinberg operator (L L H H / M) that gives Majorana neutrino masses.

Neutrinoless double-beta decay experiments (LEGEND, nEXO, targeting m_{beta beta} ~ 0.01 eV) will test the Majorana hypothesis. If the framework stabilizes and produces predictions, the Dirac/Majorana question is a discriminant: a Majorana mass would require the spectral action to generate the Weinberg operator at the stabilized tau_0, while a purely Dirac mass would be the bare D_K eigenvalue. The current framework does not compute this -- it is a Tier 3 target at best.

### 4.3 The Inside-Out View and Neutrino Propagation

Claim A (the inside-out view) has a specific implication for neutrino physics that the session directive does not mention. If spacetime is what SU(3) looks like "from the inside," then neutrino propagation through spacetime is phonon propagation through the SU(3) crystal. The MSW effect (Paper 05) -- matter-enhanced oscillation in the Sun and Earth -- would correspond to the phonon-medium interaction in regions of varying density. The neutrino's effective mass in matter (m_eff^2 = m^2 - 2E V_CC, where V_CC = sqrt(2) G_F n_e) would be a dispersion relation modification in the phonon medium.

This is currently unfalsifiable because it makes no quantitative prediction beyond the standard MSW formula. But if the framework were to predict a deviation from standard MSW at specific energies (e.g., at E ~ M_KK where KK excitations become accessible), that would be testable by JUNO's solar neutrino program and by atmospheric neutrino observations at IceCube/DeepCore.

---

## Section 5: Open Questions

### 5.1 Can the Graded Sum Fix Both the Modulus AND the Neutrino Spectrum?

This is the central question for Session 25 from my perspective. If Goal 1 produces a minimum in S_eff(tau) at tau_0, the modulus is fixed. But does the SAME tau_0 produce the correct neutrino mass spectrum? These are two independent constraints on a single parameter:

- Constraint 1: S_eff(tau_0) = minimum --> fixes tau_0
- Constraint 2: R(tau_0) = 33.3 --> requires specific eigenvalue spacing at tau_0
- Constraint 3: m_heaviest(tau_0) > 0.050 eV --> requires L_K < some value

If Constraint 1 and Constraint 2 are satisfied at the SAME tau_0, it is a zero-parameter prediction of the neutrino mass hierarchy from the spectral geometry. The probability of this happening by chance is P(R in [17, 66]) ~ 10% on a log-uniform prior over [1, 10^4]. If it does happen, the BF is 1/0.10 ~ 10, from the neutrino sector alone.

### 5.2 What Does a "Soft" Neutrino Gate Look Like?

I have been applying hard gates (R in [17, 66]) because precision neutrino data demands precision predictions. But there is a softer question: does the framework produce the correct QUALITATIVE pattern of neutrino masses? The pattern has three features:

1. Two mass scales: Delta m^2_atm ~ 2.5 x 10^{-3} eV^2 and Delta m^2_sol ~ 7.5 x 10^{-5} eV^2 (Papers 07-09)
2. Hierarchical mixing: theta_12 ~ 33 degrees (large), theta_23 ~ 49 degrees (near-maximal), theta_13 ~ 8.6 degrees (small) (Papers 07, 08, 10)
3. Normal ordering preferred: m_1 < m_2 < m_3 (current data, ~2 sigma)

The framework already predicts normal ordering (bowtie structure). The tridiagonal selection rules qualitatively predict theta_12 >> theta_13. If the graded multi-sector sum produces two distinct low-energy scales (rather than a single degenerate cluster), the framework would match all three qualitative features. This would warrant a soft BF of 2-5, insufficient for revival but sufficient to justify continued computation.

### 5.3 KATRIN-TRISTAN and KK Excitations

KATRIN-TRISTAN (the upgrade to search for keV-scale sterile neutrinos, Paper 12 Section on sterile search) is the only planned experiment that could directly test the KK tower prediction. If the SU(3) compactification radius is L_K ~ 10^{-7} m, the first KK excitation mass is m_KK ~ 2 eV -- within KATRIN-TRISTAN's sensitivity range of m_4 in 1-100 eV^2. A kink in the beta spectrum at the KK mass would be a smoking-gun signature of extra dimensions, whether or not the phonon-exflation framework survives.

However, the absence of evidence for sterile neutrinos in KATRIN's current data (|U_e4|^2 < 0.01-0.1 for m_4^2 in 1-100 eV^2, Paper 12) already constrains the mixing of any KK excitation with the electron neutrino. The framework would need to predict |U_e4|^2 below current bounds -- which is natural if the KK modes live in higher Peter-Weyl sectors with small overlap onto the Z_3 = 0 gap-edge mode.

---

## Closing Assessment

This is my eighth consecutive review. The neutrino-specific predictive power of the phonon-exflation framework remains at 0%. No quantitative neutrino prediction has been produced; no tau_0 has been fixed; the R-1 gate failure (R ~ 10^{14} and R = 5.68) is a clean negative result.

The structural results that survive -- CPT, three generations, normal ordering prediction, tridiagonal selection rules -- are genuine but not sufficient. They correspond to Level 2 on Sagan's evidence hierarchy: structural consistency without quantitative prediction. Pontecorvo's oscillation framework (Paper 05) is a theoretical structure that was confirmed by experiment over decades. A competing framework must meet or exceed the precision of the measurements that confirmed Pontecorvo. At present, the phonon-exflation framework cannot even state what its neutrino mass predictions ARE, because Step 1 (fix tau_0) is blocked.

Session 25's computational goals offer three paths to unblock Step 1: Goals 1, 2, and 3. If ANY of these produces a minimum at finite tau, I will immediately compute the neutrino R at that tau using the diagnostics proposed in Section 3. The pre-registered gates are stated above. The pipeline is ready. The experimental comparison data (Papers 07-10, 12) is tabulated to the precision needed.

I assign the following Bayes factors for Session 25 outcomes as they affect the neutrino sector specifically:

| Outcome | Neutrino BF | Rationale |
|:--------|:------------|:----------|
| Goal 1 minimum + R_graded in [17, 66] | 10-25 | Two independent constraints met at same tau |
| Goal 1 minimum + R_graded outside [17, 66] | 0.3-0.5 | Modulus fixed but neutrinos wrong |
| Goal 2 minimum + R_full(Lambda=1) in [17, 66] | 8-20 | Debye cutoff resolves Kramers + correct R |
| Goal 3 Berry phase pi/2 + non-adiabatic R correction | 3-8 | MSW-analog resolution of Kramers |
| All Tier 1 monotone, no minimum anywhere | 0.2 | Neutrino program effectively closed |

The information value of these computations is positive. Run them.

---

*Neutrino-Detection-Specialist, 2026-02-21. The framework knows how to count to three (Z_3 generations). It knows how to preserve CPT ([J, D_K] = 0). It knows the lightest state is lightest for a reason (bowtie structure). What it does not yet know is the single number -- tau_0 -- that would turn structural consistency into quantitative prediction. Three computations will tell us whether that number exists.*
