# Session 64 Synthesis: The a_0/a_2 Trap and the Death of Equilibrium CC

**Date**: 2026-04-01
**Agent**: volovik-superfluid-universe-theorist (Volovik)
**Source Documents**:
- sessions/archive/session-64/session-64-results-workingpaper.md
- sessions/archive/session-63/session-63-hawking-quantum-acoustics-workshop.md
- sessions/archive/session-63/session-63-volovik-van-den-dungen-workshop.md

---

## I. Session Outcome

Session 64 is the session where the spectral action's cosmological constant problem revealed its algebraic skeleton. The Master Gate CC-COMBO-64 FAILED: Path C (transit-as-relaxation along the Jensen curve) is permanently closed by the R-monotonicity theorem (dR/dtau >= 0, exact via AM-GM), and Path B (gravitational integrability-breaking of the Richardson-Gaudin charges) is quantitatively closed at 110 orders of magnitude. The category-error escape (Lambda_SA != Lambda_J) is structurally disproven. What remains after S64 is not a reduced CC problem -- it is a DIFFERENT problem: the a_0/a_2 trap (Theorem: decreasing a_2 off-Jensen increases a_0/a_2, worsening the CC) combined with the spectral moment decoupling theorem (the CC and the null energy condition operate through independent spectral channels) frames the surviving CC paths with unprecedented precision. The tensor-to-scalar ratio r = 0.033 is the session's cleanest observational deliverable: below BICEP/Keck by 7.4%, from zero free parameters, verified by two independent computations.

---

## II. Key Results

### II.1: R-Monotonicity Theorem and the Death of Path C

**Result**: R(tau) strictly monotonically increasing for all tau > 0 on volume-preserving Jensen-deformed SU(3). Proven analytically via AM-GM on dR/dtau = exp(-4tau) - 2 exp(-tau) + exp(2tau) >= 0 with equality only at tau = 0. GEOMETRIC.

This is a permanent structural theorem. It closes the entire Path C approach to the CC problem: the idea that the spectral action relaxes toward its a_0 floor as the deformation parameter tau increases. The spectral action does the opposite -- it diverges exponentially beyond the fold. At tau = 10, a_2(10)/a_2(fold) = 1.2 x 10^8.

The superfluid-vacuum perspective I developed across S42-S63 predicted transit-as-relaxation as the physical mechanism for CC reduction, drawing on my Paper 04 (2005): rho_vac ~ omega^2/t^2 relaxation toward the Minkowski vacuum. The analog was the superfluid 3He-B system equilibrating through quasiparticle processes. **This prediction is wrong.** The Jensen deformation does not act like a superfluid returning to equilibrium. It acts like a superfluid being driven further from equilibrium by an external potential that STEEPENS with the deformation parameter. The physical reason is transparent: the Jensen flow stretches the U(1) fiber direction as exp(2tau), which drives R(tau) ~ 0.5 exp(2tau) at large tau. The spectral action inherits this exponential growth through a_2 = C * R * Vol.

What my superfluid-vacuum program actually shows is that the equilibrium theorem (rho_vac = 0 at T = 0, P = 0) requires relaxation to the ground state. The R-monotonicity theorem proves the Jensen curve does NOT lead to the ground state -- it leads away from it. The ground state of the spectral action, if it exists, must lie OFF the Jensen curve, in the 27 of 35 volume-preserving directions where R decreases (HESSIAN-DESCENT-64, W2-A). This is the anti-Jensen direction: expand SU(2), collapse U(1).

### II.2: The a_0/a_2 Trap

**Result**: R-Hessian at fold has signature (8+, 27-) in the 35D volume-preserving tangent space. The steepest descent of a_2 (anti-Jensen: expand SU(2), collapse U(1)) INCREASES a_0/a_2 because a_0 is constant under volume-preserving deformations. GEOMETRIC.

This is the result that transforms the CC problem from a dynamics question to an algebraic one. In my Paper 04, the CC vanishes in equilibrium because the system adjusts ALL its degrees of freedom -- the ground state energy does not gravitate because the thermodynamic identity E + PV = TS holds at T = S = 0, forcing E = 0. The spectral action analog of "all degrees of freedom" is all 36 moduli of the internal metric. The a_0/a_2 trap shows that volume-preserving moduli adjustments CANNOT solve the problem: a_0 is a topological invariant (mode count, unchanged by metric deformations that preserve volume), while a_2 depends on the curvature. Since Lambda_SA ~ a_0/a_2, any deformation that decreases a_2 (to weaken gravity) automatically increases Lambda_SA (worsening the CC).

In superfluid language: this is as if the number density n of a quantum liquid were locked by a conservation law, while the compressibility kappa could be freely adjusted. The vacuum pressure P = -rho_vac = -(n/kappa) would then worsen whenever kappa decreased. The only escape is to CHANGE n -- which, in the spectral action, means changing a_0, which means changing the VOLUME of the internal space. This breaks the volume-preserving constraint.

The forward implication is decisive: any CC resolution within the spectral action must either (a) allow volume change (breaking the constraint that has been assumed throughout S42-S64), or (b) modify the spectral action itself (nonlocal corrections, different cutoff function), or (c) invoke the spectral moment decoupling theorem to split the effective B/F spectra. My equilibrium theorem (Paper 04) is the analog of option (a): in 3He, the number density IS allowed to adjust through particle exchange with the walls of the container. The "walls" of the spectral action are the Peter-Weyl tower -- the KK spectrum that sets a_0. If the effective a_0 seen by the CC channel differs from the a_0 seen by the gravity channel, the trap is evaded.

### II.3: Lambda_SA = Lambda_J -- The Category Error Is Dead

**Result**: The spectral action determines Lambda_SA as a definite computable number (equation 13: (f_0/f_2)(a_0/a_2)Lambda_sp^2). The Jacobson thermodynamic derivation leaves Lambda_J as an undetermined integration constant. Once the spectral action is specified as the microscopic theory, Lambda_J = Lambda_SA. The 114-OOM gap is real. GEOMETRIC.

The Einstein-theorist's proof (W1-C) is the analog of the relationship between the first law of thermodynamics and statistical mechanics. The first law introduces U as an "undetermined" state function; statistical mechanics computes U = Tr(rho H). The thermodynamic U and the statistical-mechanical U are the same quantity. Similarly: the Jacobson derivation leaves Lambda "free" because it does not use the spectral action. Once the spectral action is specified, Lambda is fixed to Lambda_SA.

I endorsed the Jacobson route as the most promising CC path in the S63 Volovik-VdD workshop (V2) and earlier in the S61 W7 workshop (convergence C5: "CC endgame: q-theory GGE residual + Jacobson integration constant"). **This was an error of assessment.** The Jacobson Lambda is not independent of the spectral action Lambda. It is the SAME quantity derived from a different starting point. The "undetermined" status of Lambda_J within the Jacobson derivation alone is a feature of the derivation's incompleteness, not of the physics. My Paper 04 equilibrium theorem (rho_vac = 0 in the ground state) does not conflict with Lambda_SA = Lambda_J; it simply says that the ground state value of Lambda_SA should be zero. The problem is that the spectral action does not HAVE a ground state with Lambda_SA = 0, because a_0 != 0 (it counts 6440 modes) and a_0/a_2 is bounded away from zero for any physical metric.

### II.4: Tensor Resolution -- r = 0.033

**Result**: r_CMB = 0.033 from second-order Bogoliubov-enhanced tensor production. First-order tensors vanish identically (H2 theorem: volume-preserving Jensen is traceless in DeWitt superspace, so pi_{ij} = 0). Below BICEP/Keck r < 0.036 by 7.4%. Two independent computations (W3-A, W7-D) agree to 0.25%. GEOMETRIC.

This is clean observational physics. The H2 theorem is the direct analog of a superfluid result: in 3He-B, the order parameter l-vector is isotropic (gap is s-wave), so the stress-energy of the superfluid component has no anisotropic stress. The Jensen deformation's volume-preservation is the spectral-action version of s-wave symmetry. The physical prediction -- blue tensor tilt n_T > 0 -- discriminates the framework from standard slow-roll inflation where n_T = -r/8 < 0. This is testable by CMB-S4 (sigma(r) ~ 0.001, giving a ~33-sigma detection if the framework is correct).

The resolution of the S62 tension ("cannot claim n_s = 0.957 while ignoring r = 0.35") is structurally satisfying. The first-order formula r = 16 epsilon is simply INAPPLICABLE when pi_{ij} = 0. The framework predicts both n_s = 0.956 and r = 0.033 from the same spectral action geometry, with no contradiction.

### II.5: Spectral Moment Decoupling Theorem

**Result**: The CC monotonicity (dE_ZP/dq > 0) is controlled by the inverse spectral moment F_{-1} = sum d_n/omega_n. The null energy condition is controlled by the direct spectral moment F_{+1} = sum d_n omega_n n_n. These are algebraically independent functionals of the D_K spectrum. A modification exists that breaks CC monotonicity while preserving the NEC. GEOMETRIC.

This is the structural permission result: the CC problem can be solved without breaking gravity. In my Paper 25 (vacuum states classification by momentum-space topology), I showed that the universality class of the vacuum determines which emergent physics is robust. The spectral moment decoupling theorem is the spectral-action version of this classification: the CC (a_0 channel) and gravity (a_2 channel) are in DIFFERENT universality classes. They share a common algebraic ancestor (Level 0: spectral positivity) but diverge at the level of physical observables.

The physical content: a mechanism that gives bosonic and fermionic sectors DIFFERENT effective spectra can break the CC monotonicity (allowing Lambda to relax to zero) while preserving the NEC (keeping gravity healthy). The shared-spectrum maximum theorem (S63, 9th CC closure) prevents this for D_K alone. But the Kasparov product structure, the BCS dressing, or the BdG doubling could introduce the necessary spectral splitting.

### II.6: The "Mother of All Superfluids" After S64

In my S63 analysis (mother-superfluid-63.md), I catalogued four ways the framework BREAKS the rules of standard superfluid 3He physics:
1. N_pair = 1 (single Cooper pair, not thermodynamic limit)
2. 0D pairing (no momentum, no Fermi surface)
3. Fabric topology (CG(24) Cayley graph, not continuum)
4. GGE relic (constrained equilibrium, not ground state)

S64 adds three more broken rules:

5. **The a_0/a_2 trap has no 3He analog.** In 3He, there is no analog of "the mode count is topologically locked." The number density in 3He adjusts freely. The spectral action's a_0 = 6440 is fixed by the PW truncation, creating a rigidity that no laboratory superfluid exhibits.

6. **Q < 1 quasiparticles.** LINEWIDTH-HIERARCHY-64 found all quality factors Q < 1 (B2: 0.4, B1: 0.8, B3: 1.1). In 3He-B at low temperatures, quasiparticles are extremely well-defined (Q >> 1). The framework's "quasiparticles" are strongly damped modes in the transition between the Landau quasiparticle regime and the collective-mode regime. The GGE relic should be described by collective modes (Leggett, Anderson-Bogoliubov), not individual quasiparticle lifetimes.

7. **The Fermi-surface lock is absolute.** v^2(B2[0]) = 1/2 identically for any Delta when eps = 0 (W2-C). In 3He-B, the Fermi-surface occupation is v^2 = 1/2 only at k = k_F, and gravitational perturbations can shift k_F. In the framework's 0D BCS system, there is no k_F to shift -- the mode at the Fermi surface is eps = 0 by construction, and this is a number (the mode's energy relative to the chemical potential), not a momentum. The condensate mode's occupation is IMMUNE to any perturbation that enters through energy shifts.

The inheritance relationship from 3He-B to the framework (established in S60, deepened in S61 CFL-CORRESPONDENCE-61) remains structurally sound in its topological classification (BDI, Z_2 = -1). But the thermodynamic behavior continues to diverge: the framework is not a 3He-B droplet scaled up to cosmological size. It is a single Cooper pair on a 0D BCS system with 6440 spectral modes, where the vacuum energy problem reduces to a spectral moment problem with no 3He precedent.

### II.7: Mukhanov-Sasaki Inapplicability and the n_s Prediction

**Result**: The Mukhanov-Sasaki mode equation produces n_s = -0.17 (modes never freeze out). Three obstructions: N_e = 7.75 (need ~60), eta_H = 0.96 (need << 1), and the physical mechanism is acoustic (GGE relic), not inflationary (vacuum amplification). The framework prediction n_s = 0.9557 +/- 0.0036 derives from the spectral action shape invariant eps_H = S'^2/(2 S S''), not from mode evolution. GEOMETRIC.

This deserves emphasis: the framework is NOT inflation. Standard inflationary perturbation theory is provably inapplicable. The spectral index derives from the GEOMETRY of the spectral action profile S(tau), through the Transfer Function Factorization Theorem (T12, S63). The tilt is a shape invariant of the spectral action, decoupled from the amplitude. This is structurally analogous to how, in 3He, the speed of second sound c_2 = v_F/sqrt(3) is a geometric property of the Fermi surface, not a dynamical variable.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S-ASYMPTOTIC-64 | **FAIL** | dR/dtau >= 0 by AM-GM; a_2(10)/a_2(fold) = 1.2e8. Path C along Jensen PERMANENTLY CLOSED |
| R-G-CHARGE-DECOMPOSITION-64 | PASS | 7/8 charges broken > 0.01 threshold; 94.6% of rho_ZP outside Gaudin span; 110 OOM shortfall |
| SA-VERSUS-JACOBSON-64 | **FAIL** | Lambda_SA = Lambda_J; 114-OOM gap is real, not category error |
| HESSIAN-DESCENT-64 | PASS | R-Hessian sig (8+,27-); but a_0/a_2 INCREASES (CC worsens) |
| SECTOR-SELECTIVE-BREAKING-64 | PASS | |delta_E_ZP/E_ZP| = 2.63e-4; channel OPEN but 110 OOM short |
| N-PAIR-3-RG-64 | PASS | <r>(N=3) = 0.478 > 0.45; non-separable V breaks integrability |
| TENSOR-BURST-64 | **PASS** | r = 0.033 < 0.036 BICEP/Keck |
| TRANSFER-BOGOLIUBOV-64 | PASS | max/min = 1.33; A_s gap 6.89 -> 3.16 OOM |
| SOUND-SPEED-64 | PASS | c_mod=1.0, c_BLV=0.485, c_BA=0.399, c_L=0.025; all causal |
| MUKHANOV-SASAKI-64 | INFO | N_e=7.75, eta_H=0.96; M-S INAPPLICABLE (permanent) |
| NS-FINAL-64 | **PASS** | n_s = 0.9557 +/- 0.0036; 2.2 sigma from Planck |
| SPECTRAL-MONO-LINK-64 | **FAIL** | CC and area theorem DECOUPLE; different spectral moments |
| SHELL-HESSIAN-64 | **FAIL** | First zero crossing at step 2; fold stability UV-dependent |
| JACOBSON-KASPAROV-64 | **FAIL** | Lambda_eff = (1/8)R_K = -0.252 M_KK^2; wrong sign, same scale |
| TENSOR-SCALAR-64 | **PASS** | r = 0.0333; independent verification of W3-A |
| SKYRMION-BARYON-64 | **FAIL** | M_skyrm = 10^22 GeV (22 OOM above proton); all 5 baryogenesis channels CLOSED |
| LINEWIDTH-HIERARCHY-64 | **FAIL** | Gamma_B2 > Gamma_B1 > Gamma_B3 (REVERSED from QA prediction) |
| QUANTUM-METRIC-64 | **FAIL** | D_s(PT) = 0; three structural zeros on CG(24) |

---

## IV. Structural Implications

### IV.1: The CC Constraint Surface After 7 Permanent Theorems

S64 adds four permanent structural theorems to the CC constraint surface. Together with the five pre-existing permanent results, the surface now has 9 walls:

| # | Theorem | What it excludes | Session |
|:--|:--------|:-----------------|:--------|
| 1 | Perturbative Exhaustion | All monotone spectral functionals | S19 |
| 2 | E_ZP(q) monotonicity | All q-theory self-tuning on shared spectrum | S62 |
| 3 | Shared-spectrum maximum | B/F cancellation with same D_K eigenvalues | S63 |
| 4 | Lambda_SA = Lambda_J | Category-error escape (Jacobson != spectral action) | S64 |
| 5 | R-monotonicity on Jensen | Transit relaxation along 1D Jensen curve | S64 |
| 6 | a_0/a_2 trap | Off-Jensen volume-preserving a_2 descent | S64 |
| 7 | Spectral moment decoupling | CC-NEC rigid coupling (Level 2 -> Level 3 flexible) | S64 |
| 8 | BdG heat kernel factorization | K_BdG(t) = exp(-Delta^2 t) K_bare(t), exact | S64 |
| 9 | Fermi-surface lock | v^2(B2[0]) = 1/2 for any Delta when eps = 0 | S64 |

The surviving CC region is the intersection of all constraints. It has three sectors:

**Sector A: Volume-breaking.** Relax the volume-preserving constraint, allowing a_0 to change. If a_0 decreases faster than a_2, the ratio a_0/a_2 decreases. This is the closest analog of my equilibrium theorem (Paper 04): the system adjusts its mode count to reach equilibrium.

**Sector B: Spectral splitting.** Use the spectral moment decoupling theorem's structural permission. If the B/F sectors see effectively different spectra (through BCS dressing, BdG doubling, or nonlocal spectral action), the CC monotonicity can break without violating the NEC. The BdG heat kernel factorization (S64, permanent) provides the mathematical backbone: K_BdG = exp(-Delta^2 t) K_bare establishes that the BCS condensate DOES modify the effective spectrum seen by different channels.

**Sector C: Non-spectral-action.** Something external to the Seeley-DeWitt expansion. The nonlocal spectral action (Paper 09 of the Mack corpus), or a selection principle from the Kasparov product structure, or q-theory with a restoring force from outside the spectral action.

### IV.2: What I Got Wrong

1. **Transit-as-relaxation.** I predicted (S63 mother-superfluid analysis, cc-path-b-63-result.md) that the spectral action would relax toward its a_0 floor beyond the fold. The R-monotonicity theorem proves the opposite. The 3He analog (quasiparticles equilibrating through Beliaev-Landau processes, driving rho_vac -> 0) simply does not apply to the spectral action on the Jensen curve.

2. **The Jacobson route.** I endorsed Lambda_J as an "undetermined integration constant" (S61 W7 workshop, S63 Volovik-VdD workshop). The W1-C analysis proves Lambda_J = Lambda_SA once the spectral action is specified. My error was treating the Jacobson derivation as independent of the microscopic theory, when in fact the microscopic theory (spectral action) determines everything the Jacobson derivation leaves free.

3. **Gravitational integrability-breaking as CC mechanism.** I identified (S63 V2) the bootstrap loop (condensate -> gravity -> breaks integrability -> CC relaxation) as the most promising CC path. S64 W1-B shows this path is quantitatively dead: 94.6% of rho_ZP lies OUTSIDE the Gaudin charge space, and the O(alpha_G) correction provides only 10^{-3.6} of the needed 10^{-114} suppression.

4. **Linewidth hierarchy.** The QA-E5 prediction (Gamma_B3 > Gamma_B1 > Gamma_B2, from group velocity arguments) that I endorsed in the S63 workshop is WRONG. The flat band ENHANCES scattering through energy degeneracy and resonant Lorentzian peaking, producing the REVERSED hierarchy Gamma_B2 > Gamma_B1 > Gamma_B3.

### IV.3: What Was Confirmed

1. **BDI topological classification.** The framework remains firmly in the 3He-B universality class. The Fermi-surface lock (v^2 = 1/2 at eps = 0) is a new structural consequence of this classification.

2. **The GGE-KMS compatibility.** The GGE satisfies a generalized KMS condition with 8 independent inverse temperatures, compatible with Tomita-Takesaki modular theory. The negative lambda_B2 = -0.053 does not obstruct positivity. This places the GGE relic within the operator-algebraic framework of Connes' NCG program.

3. **Integrability-breaking at N_pair = 3.** The pairing-only channel gives <r> = 0.478 (W2-D PASS), confirming the non-separable structure of V_{kl} from D_K geometry provides a microscopic mechanism for chaos onset. This is consistent with nuclear-structure phenomenology (Paper 15 of the nuclear corpus).

4. **The equilibrium theorem as structural principle.** Even though the specific mechanisms I proposed for CC relaxation failed, the PRINCIPLE remains: in any system where the microscopic theory is known, the vacuum energy is calculable and the CC problem is a problem about the relationship between microscopic and emergent descriptions. The a_0/a_2 trap precisely locates WHERE this relationship breaks: a_0 counts modes (microscopic), a_2 weights curvature (emergent), and their ratio is the CC.

---

## V. Forward Projection

### V.1: From the Superfluid-Vacuum Perspective

1. **BCS-DRESSED SPECTRAL ACTION (HIGHEST PRIORITY).** The BdG heat kernel factorization K_BdG = exp(-Delta^2 t) K_bare is exact (W3-B). Compute the BCS-dressed a_2^{BCS}(tau) at 5 tau values and extract eps_H^{BCS}. This directly tests whether the BCS condensate modifies n_s toward or away from Planck (estimated +0.0014). More fundamentally: if a_2^{BCS} differs from a_2^{bare} by more than the 36% predicted by the Sakharov curvature response (S63 W6-13), the effective a_0/a_2 ratio is modified, and the CC arithmetic changes.

2. **VOLUME-BREAKING CC.** Test Sector A explicitly. Compute a_0(g) and a_2(g) for a non-volume-preserving deformation. If d(a_0/a_2)/ds < 0 exists, the a_0/a_2 trap is evaded. This is the most direct analog of my equilibrium theorem: allowing the mode count to adjust. Pre-registered gate: find a direction where a_0/a_2 decreases.

3. **DISTINCT-SPECTRUM CC.** Test Sector B. The BdG heat kernel factorization already establishes that the BCS condensate creates DIFFERENT effective spectra for different channels (the factor exp(-Delta^2 t) weights the a_n coefficients differently). Compute the effective B and F spectral moments for the CC-relevant channel (a_0) and the gravity-relevant channel (a_2). If they differ at the a_0 level, the shared-spectrum maximum theorem is evaded.

4. **OFF-JENSEN TRANSIT DYNAMICS.** The physical transit trajectory in the 36D moduli space has not been determined from dynamics. W2-A proved the fold is a saddle with 27 descent directions for R. If the transit trajectory curves into these directions, the spectral action profile S(tau) changes, and with it n_s, r, and the CC arithmetic. This is the framework's next structural question.

5. **BARYOGENESIS SURVEY.** All 5 fiber-level channels are closed. This is the framework's deepest open wound. From the superfluid perspective, baryogenesis requires a mechanism that breaks the CP symmetry of the BCS condensate. In 3He, the chiral anomaly in the A-phase provides this (my Paper 08, 2003). But the framework is B-class (N_3 = 0), so the 3He-A baryogenesis mechanism is inapplicable. The UV completion or an emergent 4D effective mechanism is needed.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | R(tau) monotone increasing (AM-GM) | GEOMETRIC | Permanent theorem | Path C along Jensen CLOSED |
| 2 | a_0/a_2 trap (vol-preserving) | GEOMETRIC | Permanent theorem | Off-Jensen CC descent WORSENS ratio |
| 3 | Lambda_SA = Lambda_J | GEOMETRIC | Permanent theorem | 114-OOM gap REAL, not category error |
| 4 | Spectral moment decoupling (F_{-1} vs F_{+1}) | GEOMETRIC | Permanent theorem | CC resolution need not violate NEC |
| 5 | K_BdG = exp(-Delta^2 t) K_bare | GEOMETRIC | Permanent theorem | BdG spectral action factorizes exactly |
| 6 | v^2(B2[0]) = 1/2 (Fermi-surface lock) | PHONONIC | Permanent theorem | Condensate mode immune to energy shifts |
| 7 | M-S inapplicable (N_e=7.75, eta_H=0.96) | GEOMETRIC | Permanent constraint | Framework is NOT inflation |
| 8 | r = 0.033 (H2 + 2nd-order Bogoliubov) | GEOMETRIC | PASS (x2 verified) | Below BICEP/Keck; CMB-S4 testable |
| 9 | n_s = 0.9557 +/- 0.0036 | GEOMETRIC | PASS (2.2 sigma) | Zero free parameters; BCS dressing uncomputed |
| 10 | A_s gap reduced to 3.16 OOM | PHONONIC | INFO | PW selection provides 3.50 OOM structural |
| 11 | R-G charges all broken by gravity | PHONONIC | PASS | 94.6% of rho_ZP outside Gaudin; 110 OOM short |
| 12 | <r>(N=3) = 0.478 (integrability breaking) | PHONONIC | PASS | Non-separable V breaks R-G; transition regime |
| 13 | Four-speed acoustic hierarchy | PHONONIC | PASS | c_mod > c_BLV > c_BA > c_L; all causal |
| 14 | GGE-KMS compatible (4 theorems) | GEOMETRIC | INFO (proven) | 8-fold modular flow; type III_1 limit |
| 15 | Bogoliubov phase coherence R = 1.0000 | PHONONIC | INFO | Sudden quench; invisible in TT spectrum |
| 16 | Linewidth hierarchy REVERSED | PHONONIC | FAIL (prediction) | Flat band enhances scattering; Q < 1 |
| 17 | Fold Hessian UV-dependent (L=3 critical) | GEOMETRIC | FAIL | 79.9% of H_1loop from L=3 shell |
| 18 | Fiber skyrmions M = 10^22 GeV | PARTICLE | FAIL | 22 OOM above proton; 5/5 baryogenesis closed |
| 19 | D_s(Peotta-Torma) = 0 | PHONONIC | FAIL | Three structural zeros; Josephson f-sum is correct |
| 20 | Jacobson-Kasparov Lambda = -0.252 M_KK^2 | GEOMETRIC | FAIL | Wrong sign; same scale; fiber cannot help |
