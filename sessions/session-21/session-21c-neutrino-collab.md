# Neutrino -- Collaborative Feedback on Session 21c

**Author**: Neutrino
**Date**: 2026-02-19
**Re**: Session 21c Phase 0 Results

---

## Section 1: Key Observations

### 1.1 The Ratio Crossed -- But Not Where It Should

In my Session 20b review, I wrote the line that defined the neutrino diagnostic: "If R never passes through 33, the framework is closed for neutrino physics regardless of stabilization. If it does, the tau value where R = 33 is a prediction that any future stabilization mechanism must match."

Session 21c executed this diagnostic (P0-4). R does cross 32.6. That is the good news. The bad news is that it crosses at tau = 1.556, driven by an avoided crossing between the (0,0) singlet and the (1,0)/(0,1) fundamental sectors at a Berry curvature monopole near tau = 1.58. The crossing width is delta_tau ~ 4 x 10^{-6}. The modulus would need to stabilize at tau = 1.5560 +/- 0.000004 -- fine-tuning of one part in 10^5.

As an experimentalist, I know exactly what this looks like. It looks like fitting noise. When a function achieves a target value only because it has a pole, and the pole produces a brief transient through the target, that is not a physical prediction. That is an artifact. To use the reactor analogy from my 20b review: if Daya Bay could reproduce the measured oscillation signal only by placing the far detector at a single point within 4 mm of the reactor (on a 1.6 km baseline), no one would call that a measurement. They would call it numerology.

The coordinator and panel correctly reclassified P0-4 from SOFT PASS to INCONCLUSIVE. I concur. In fact, from the pure neutrino-physics perspective, I would classify it more harshly: this is a NEAR-MISS that reveals structural problems.

### 1.2 The Diabolical Point is Real and Physically Significant

What rescues P0-4 from being a complete waste is the diabolical point itself. The avoided crossing at tau = 1.58 is between states of different Z_3 triality -- the (0,0) singlet (Z_3 = 0, multiplicity 2) and the (1,0) fundamental (Z_3 = 1, multiplicity 24). This is a genuine inter-sector crossing, mediated by the Kosmann-Lichnerowicz coupling, with a gap of 7.95 x 10^{-6} that directly measures the Z_3-symmetry-breaking coupling strength at that tau value.

For neutrino physics, this matters. The three lightest eigenvalues -- which are the neutrino mass candidates -- participate in a three-level rearrangement near tau = 1.58. lambda_3 switches sector identity ((0,1) <-> (1,0)) multiple times. This is a cusp catastrophe (codimension 3), not a fold (codimension 2). The neutrino mass eigenstates are not smoothly connected through this region. Any attempt to track "neutrino 1," "neutrino 2," and "neutrino 3" through the monopole requires the Berry connection (Paper 05 in my index, Pontecorvo: the PMNS matrix is precisely the rotation between flavor and mass bases, and near a diabolical point the adiabatic basis breaks down).

### 1.3 The Dual Algebraic Trap and Its Neutrino Implications

The structural theorems proved this session -- F/B = 4/11 (Trap 1) and b_1/b_2 = 4/9 (Trap 2) -- are clean mathematical results about SU(3) with standard SM embedding. Both traps are representation-theoretic identities, independent of the metric deformation. They closure all perturbative spectral stabilization routes.

For neutrinos, the implication is precise: no perturbative mechanism can fix tau_0, so no perturbative mechanism can predict neutrino masses. This was already the situation after Session 20b, but Session 21c elevates it from an empirical observation ("we computed and found monotonicity") to a structural theorem ("monotonicity is algebraically required"). The neutrino prediction pipeline, stalled at step 1 since Session 20b, is now provably blocked at the perturbative level. Only non-perturbative physics can unblock it.

### 1.4 T''(0) is the Only Survivor -- and It Is UV-Dominated

T''(0) = +7,969 escapes both algebraic traps because it operates on eigenvalue derivatives (Berry curvature geometry), not eigenvalue magnitudes. This is the session's most important positive result. But from the neutrino perspective, I note a critical caveat: 89% of T''(0) comes from UV modes (p+q = 5-6). The IR modes (p+q <= 2), which contain the three lightest eigenvalues -- the neutrino sector -- contribute only 0.3% (23.7 out of 7,969). The self-consistency map has the right curvature in the UV. Whether it has the right curvature in the IR, where neutrino masses live, is entirely unknown.

This is the spectral analog of a problem neutrino experimentalists know well. At IceCube (Paper 11), the atmospheric neutrino flux at high energy (> 100 TeV) is dominated by prompt charm production and astrophysical sources. The oscillation signal lives at low energy (1-100 GeV). A result about the high-energy spectrum tells you almost nothing about the low-energy oscillation physics. T''(0) > 0 is a high-energy result. The neutrino sector needs an IR result.

---

## Section 2: Assessment of Key Findings

### 2.1 P0-4 Neutrino Gate: INCONCLUSIVE is Correct, but the Failure Mode is Informative

The P0-4 result is a failure of the smoothness kind, not the absence kind. R(tau) does achieve the value 32.6 -- the framework is not algebraically prevented from matching the neutrino mass-squared ratio. The failure is that R achieves this value only via a topological artifact (monopole-driven divergence/zero-crossing) rather than via smooth spectral evolution.

This matters because it constrains what a viable stabilization mechanism must do. If the framework is to produce correct neutrino masses, the stabilization mechanism must either:

(a) Stabilize tau near 1.556 with precision delta_tau < 4 x 10^{-6} (fine-tuning, unacceptable);

(b) Modify the three lightest eigenvalues through off-diagonal coupling strongly enough to shift R(tau) to ~33 at a physically relevant tau (e.g., tau in [0.15, 0.35]); or

(c) Operate through non-perturbative physics that fundamentally changes the eigenvalue flow near the FR minimum (tau ~ 0.30) so that R passes through 33 there.

Route (b) is exactly what the coupled diagonalization (P1-2) would test. baptista's finding that the coupling/gap ratio is 4-5x at the lowest modes means the three lightest eigenvalues are in the strong-coupling regime. Second-order perturbation theory shifts could easily produce O(1) changes in R at physically relevant tau values.

### 2.2 The Structural Closure is Sound

The S_signed STRUCTURAL CLOSURE (Delta_b = -(5/9)*b_2 < 0 for all sectors) is the strongest negative result of the session. From the neutrino viewpoint, I note that this closes the last hope for a signed gauge-threshold sum to produce spectral anisotropy between sectors -- the mechanism that would have given different effective masses to different generation sectors. Without such anisotropy, the neutrino mass hierarchy cannot arise from perturbative spectral sums. The hierarchy must arise from the eigenvalue structure of D_K at whatever tau_0 is selected by non-perturbative physics.

### 2.3 The Two (Three) Monopole Structure is Genuinely New

The discovery of Berry curvature monopoles bracketing the physical window [0.10, 1.58] (or [0, 1.58] with M0 at the round metric) is the session's most significant structural finding. For neutrino physics specifically:

- The (0,0) singlet controls the gap edge throughout [0.10, 1.58]. If this is the neutrino mass sector, it means the lightest neutrino is a singlet under the residual SU(2) x U(1) for the entire physical window. This has implications for the PMNS matrix structure (Paper 05): a singlet lightest mass eigenstate would produce specific patterns in U_{e1}, U_{mu1}, U_{tau1} that differ from a fundamental lightest eigenstate.

- The BCS bifurcation at tau ~ 0.10 (Session 21a) sits at Monopole 1, where the gap-edge sector switches from fundamental to singlet. This means the BCS condensate, if it forms, operates in a topological phase defined by a specific gap-edge identity. The condensate is not generic -- it is sector-specific.

- The neutrino R = 33 crossing at tau = 1.556 sits at Monopole 2. This is not a coincidence -- it is a consequence of the fact that R diverges when the denominator (lambda_2^2 - lambda_1^2) passes through zero, which happens when the two lightest eigenvalues exchange identity. The R crossing is a topological consequence of the monopole, not a smooth physical prediction.

---

## Section 3: Collaborative Suggestions

### 3.1 Coupled R(tau) from P1-2 Eigenvectors (By-product, Zero Additional Cost)

When the coupled diagonalization (P1-2) is performed to resolve V_IR, the three lightest eigenvalues of the full coupled Dirac operator will be available as a by-product. From these, recompute R(tau) = (lambda_3^2 - lambda_2^2)/(lambda_2^2 - lambda_1^2) in the coupled basis.

The key question: does R(tau) pass through 33 at a SMOOTH location away from the monopole when off-diagonal coupling is included?

In the block-diagonal basis, R only crosses 33 at the monopole artifact. But coupling/gap = 4-5x means the three lightest eigenvalues are strongly perturbed. The perturbation theory is:

```
lambda_n^{coupled} = lambda_n^{block} + Sum_{m != n} |V_{nm}|^2 / (lambda_n - lambda_m) + ...
```

where V_{nm} is the Kosmann-Lichnerowicz matrix element. For the three lightest modes, the second-order shifts are O(V^2/gap) ~ O(1) in units of the gap itself. This could shift the eigenvalue ordering and spacing enough to produce a smooth R = 33 crossing at tau in [0.15, 0.35].

This is my HIGHEST-PRIORITY neutrino suggestion. It costs nothing beyond what P1-2 already computes. If coupled R(tau) smoothly passes through 33 somewhere in the FR minimum window, that is a COMPELLING neutrino result, independent of the stabilization mechanism. If it does not -- if R(tau) in the coupled basis still only crosses 33 near the monopole -- then the neutrino gate FAILS even with coupling corrections, and the framework faces a genuine neutrino-mass problem.

### 3.2 Sector Identity Tracking Through the Physical Window

berry's precision diagnostic revealed which (p,q) sector each of the three lightest eigenvalues belongs to at each tau. This sector identity IS the framework's analog of "which mass eigenstate is which." In the Standard Model, the PMNS matrix relates mass eigenstates (nu_1, nu_2, nu_3) to flavor eigenstates (nu_e, nu_mu, nu_tau). In the framework, the (p,q) sector labels are the geometric precursors to the mass eigenstates. The Z_3 = (p-q) mod 3 assignment determines the generation.

I suggest extracting the complete sector identity table for the three lightest eigenvalues across all 21 tau values. Specifically:

| tau | lambda_1 sector | Z_3 | lambda_2 sector | Z_3 | lambda_3 sector | Z_3 |

This table exists implicitly in the computation but has only been reported near the monopoles. The full table would reveal:

1. Whether the mass ordering (NO vs IO) changes anywhere in [0.15, 0.35]
2. Whether all three eigenvalues belong to different Z_3 classes (required for three distinct generations)
3. Whether there are additional avoided crossings that the coarse grid missed

From the oscillation data: Delta m^2_32 / Delta m^2_21 ~ 33 with the current best-fit preferring normal ordering (Paper 07, Paper 10). The global fit yields |Delta m^2_32| = 2.507 x 10^{-3} eV^2 (Paper 07 Super-K updated) and Delta m^2_21 = 7.53 x 10^{-5} eV^2 (Paper 08 SNO + Paper 09 KamLAND). Normal ordering means m_3 > m_2 > m_1 with m_3 separated from m_1,m_2 by the atmospheric splitting. The framework must reproduce this pattern at tau_0.

### 3.3 The Bowtie as Mass Ordering Discriminator

baptista's bowtie crossing structure ((0,0) drops below (1,0) at tau ~ 0.11, rises back above at tau ~ 1.58) has a direct implication for the mass ordering prediction.

Inside the bowtie [0.11, 1.58], (0,0) is the lightest. If (0,0) maps to nu_1 (lightest mass eigenstate in normal ordering), then normal ordering is predicted throughout the bowtie interior. Outside the bowtie, (1,0)/(0,1) is lightest, and the ordering depends on how the three lightest modes are distributed across Z_3 sectors.

The mass ordering prediction is therefore TOPOLOGICALLY PROTECTED within the bowtie: any stabilization at tau_0 in [0.11, 1.58] gives a definite prediction for which sector is lightest. This prediction is testable by JUNO (reactor, L = 53 km, expected 3-4 sigma by ~2028, Paper 09 for the IBD technique) and DUNE (accelerator, L = 1300 km, >5 sigma sensitivity, using the MSW resonance from Paper 05).

This is a zero-parameter prediction: the framework says which sector is lightest at any given tau, and the stabilization mechanism selects tau_0. The ordering follows with no additional inputs.

### 3.4 Gap-Edge Density of States and the Neutrino Mass Scale

baptista's BCS density-of-states argument contains a result with direct implications for neutrino masses:

- Inside [0.10, 1.58]: N(0) ~ 2 (singlet multiplicity)
- Outside: N(0) ~ 24 (fundamental multiplicity)

This is the density of states at the gap edge. If the BCS condensate forms inside the singlet window, the condensate gap Delta is set by Delta ~ omega_D * exp(-1/(g * N(0))) with N(0) = 2. For a larger density of states (N(0) = 24), the condensate would be exponentially larger.

For neutrino physics, this means: the lightest fermion mass inside the condensate window is modified by the BCS gap. The neutrino mass receives a condensate correction:

```
m_nu^{eff} = sqrt(lambda_bare^2 + Delta^2)
```

If Delta >> lambda_bare, the neutrino mass is set by the condensate gap, not by the bare Dirac eigenvalue. If Delta << lambda_bare, the condensate is irrelevant to neutrino masses. The singlet window's low N(0) = 2 suppresses Delta exponentially relative to the fundamental window's N(0) = 24. This is a natural mechanism for producing SMALL neutrino masses even in a strongly coupled regime -- the condensate is large for fundamental-sector modes (charged fermions?) but exponentially suppressed for singlet-sector modes (neutrinos?).

This connection deserves quantitative investigation. The BCS gap equation from CP-4, evaluated with the measured coupling/gap ratio (g ~ 4-5) and N(0) = 2 vs N(0) = 24, would give the ratio of condensate contributions to singlet vs fundamental fermion masses. If this ratio is O(10^{-6}) -- the ratio of neutrino to charged lepton masses -- the framework has a natural explanation for the neutrino mass hierarchy with zero free parameters.

### 3.5 KamLAND CPT Test and the Monopole Structure

KamLAND (Paper 09) compared reactor antineutrino disappearance (terrestrial, controlled source, L ~ 180 km) with the solar neutrino deficit (astrophysical, L ~ 1 AU). The agreement between nu_e and nu_e_bar oscillation parameters is a direct CPT test: Delta m^2_21(nu_bar) = Delta m^2_21(nu) to within experimental precision.

Session 17a proved [J, D_K(s)] = 0 identically, guaranteeing this equality. But the monopole structure adds a subtlety. Near the diabolical points (tau ~ 0.10 and tau ~ 1.58), the eigenvalue pairing under J holds exactly (max error 3.29 x 10^{-13} at Session 17a D-3), but the SECTOR IDENTITY of paired eigenvalues changes. Across the monopole, the eigenvalue that was in sector (0,0) with Z_3 = 0 becomes sector (1,0) with Z_3 = 1. The CPT pairing (particle/antiparticle) is preserved, but the generation assignment shuffles.

If the modulus is stabilized near a monopole, the generation structure of the neutrino sector becomes sensitive to the precise tau_0. This could produce anomalously large CP-violating effects in neutrino oscillations near the monopole -- because the PMNS matrix, which depends on the overlap integrals between mass and flavor bases, changes rapidly when the mass eigenstates are exchanging sector identity.

This is speculative but testable: if DUNE measures delta_CP near 230 degrees (the current T2K hint), and if the framework predicts delta_CP from eigenspinor overlaps at tau_0 near a monopole, the rapid variation of PMNS elements near the monopole could naturally produce a CP phase far from 0 or pi -- i.e., near-maximal CP violation. This would be a qualitative prediction of the monopole structure.

---

## Section 4: Connections to Framework

### 4.1 The Neutrino Prediction Pipeline: Updated Status

My Session 20b review identified a five-step pipeline:

1. Fix tau_0 (stabilization) -- **STALLED** (Session 20b), now **STRUCTURALLY BLOCKED** at perturbative level (Session 21c dual algebraic trap)
2. Extract lightest D_K(tau_0) eigenvalues -- Ready (Tier 1 data exists)
3. Fix M_scale from a known fermion mass -- Ready (once tau_0 known)
4. Compute PMNS angles from eigenspinor overlaps -- Tier 2 (not yet started)
5. Compare against KATRIN, oscillation global fit, JUNO, DUNE -- Ready

Step 1 is now blocked by a theorem, not merely an empirical failure. This is both worse (stronger obstruction) and better (theorem identifies exact escape conditions). The escape conditions are:

(a) Pfaffian sign change in D_total (breaks Trap 1)
(b) Different SM gauge group embedding (breaks Trap 2 -- outside current framework)
(c) Non-perturbative physics: BCS condensate, FR flux, gravitational instantons
(d) T''(0) self-consistency fixed point (derivative escape, Theorem 2)

For neutrinos, route (c) is the most promising. The BCS condensate operates in a different mathematical sector from the algebraic traps, and the gap-edge density of states (N(0) = 2 in the singlet window) provides a natural mechanism for small neutrino masses.

### 4.2 What the Bowtie Means for the Framework's Neutrino Credibility

The bowtie crossing structure is the first result from the Dirac spectrum that has STRUCTURAL implications for neutrino physics. Previously, the neutrino sector was a passive recipient: compute tau_0, extract eigenvalues, compare to data. The bowtie changes this. It tells us:

1. The mass ordering is topologically determined within each phase: NO if tau_0 is in the (0,0)-gap phase, with the (0,0) singlet being lightest
2. The framework has a natural hierarchy: singlet multiplicity (2) vs fundamental multiplicity (24) gives an exponential suppression of the lightest fermion mass via BCS gap equation
3. The monopoles bracket a finite tau-window where neutrino predictions are well-defined

This is not a prediction of specific mass values. But it is a prediction of STRUCTURE -- the structure of the mass ordering, the mechanism for hierarchy, and the topological stability of the prediction within the physical window. Structure predictions are valuable because they reduce the parameter space for future computations.

### 4.3 The Oscillation Length Analogy

The dual algebraic trap has a physical analog in neutrino oscillation physics. In the two-flavor oscillation formula (Pontecorvo, Paper 05):

```
P(nu_e -> nu_mu) = sin^2(2*theta) * sin^2(Delta m^2 * L / (4E))
```

the mixing angle sin^2(2*theta) and the oscillation phase Delta m^2 * L / (4E) are independent parameters. If they were algebraically related (e.g., if sin^2(2*theta) = f(Delta m^2)), then the oscillation probability would be a one-parameter family and the data could not independently constrain both. Nature avoids this trap: theta and Delta m^2 are independent.

The framework's algebraic trap is exactly this situation. The branching coefficients b_1 and b_2, which should be independent parameters controlling the relative weights of different gauge sectors, are instead algebraically locked (b_1/b_2 = 4/9). This means the signed spectral sum S_signed is a one-parameter family, algebraically prevented from producing the sector competition needed for a minimum. The framework needs to "unlock" b_1 and b_2 -- either through a different embedding or through non-perturbative physics that introduces genuinely independent contributions.

---

## Section 5: Open Questions

### 5.1 Does the Coupled Basis Change the Neutrino Verdict?

This is the single most important open question from the neutrino perspective. The block-diagonal treatment gives R = 33 only at a monopole artifact. The coupled treatment, with 4-5x coupling/gap, could shift the three lightest eigenvalues enough to produce a smooth R = 33 crossing at a physically relevant tau. P1-2 will answer this as a by-product.

If the answer is yes: the neutrino gate reopens, and the framework gains a genuine neutrino prediction tied to the coupled eigenvalue spectrum.

If the answer is no: the framework's neutrino-mass problem becomes structural, not just a matter of fixing tau_0. The eigenvalue spectrum of D_K on Jensen-deformed SU(3), even with full off-diagonal coupling, cannot reproduce the measured mass-squared ratio. This would be a much harder problem than the stabilization problem.

### 5.2 Is the Singlet/Fundamental BCS Gap Ratio the Mass Hierarchy?

The exponential sensitivity of the BCS gap to N(0) (density of states at the gap edge) creates a natural hierarchy between singlet-sector and fundamental-sector fermion masses. If the lightest neutrinos sit in the singlet sector (N(0) = 2) and the lightest charged leptons sit in the fundamental sector (N(0) = 24), the mass ratio could be:

```
m_nu / m_e ~ exp(-1/(g * 2)) / exp(-1/(g * 24))
```

For g ~ 4-5 (the measured coupling/gap ratio), this gives ratios of order exp(-1/8) / exp(-1/96) ~ exp(-0.125 + 0.010) ~ exp(-0.115) ~ 0.89. This is FAR too large -- the actual ratio is m_nu/m_e ~ 10^{-7}. The BCS gap equation alone does not produce the required hierarchy. Additional structure is needed.

This failure is instructive. The BCS condensate provides a MECHANISM for mass generation but not the right NUMBERS. The numbers require the full eigenvalue structure of D_K at tau_0, not just the gap-edge physics. The condensate is a necessary ingredient, not a sufficient one.

### 5.3 What Does the Three-Monopole Structure Predict for delta_CP?

The three-monopole structure (M0 at tau = 0, M1 at tau ~ 0.10, M2 at tau ~ 1.58) divides the tau-line into topologically distinct phases. The PMNS matrix elements -- specifically the CP-violating phase delta_CP -- depend on the eigenspinor overlaps, which change character at each monopole.

Inside the physical window [0.10, 1.58], the (0,0) singlet dominates the gap edge. The eigenspinors of the (0,0) singlet are the simplest harmonics on SU(3) -- they are isotropic. This means the overlap integrals that determine PMNS angles are dominated by the geometry of the fundamental and adjoint sectors. The CP phase arises from the complex structure of these overlaps.

The T2K hint (delta_CP ~ 230 degrees, Paper 05 updated) and the framework's Z_3 x Z_3 CP violation structure (Baptista Paper 18) together suggest that near-maximal CP violation is natural in the singlet-gap phase. Testing this requires the Tier 2 spinor transport calculation, but the qualitative prediction -- that the framework favors large delta_CP -- is a testable consequence of the monopole structure.

### 5.4 Can Cosmological Neutrino Mass Bounds Constrain tau_0 Directly?

The most stringent bound on Sum m_i comes from Planck + DESI: Sum m_i < 0.072 eV (under LCDM). In the framework, Sum m_i = (lambda_1 + lambda_2 + lambda_3)(tau_0) * M_scale. If M_scale is fixed from the electron mass (or any other known fermion), then the cosmological bound constrains the SUM of the three lightest eigenvalues at tau_0.

Crucially, this bound is cosmological-model-dependent. The phonon-exflation framework has a different expansion history from LCDM (rolling modulus, spectral exflation). The CMB anisotropy spectrum would be affected, and the derived neutrino mass bound would shift. If the framework's expansion history is more permissive (allows larger Sum m_i), the cosmological constraint weakens. If it is more restrictive, the constraint tightens.

This is an important self-consistency test: the framework must simultaneously predict neutrino masses from D_K(tau_0) and an expansion history from the modulus dynamics, and both must be consistent with CMB + LSS data. This cross-check is a future Tier 3 deliverable but should be flagged now.

---

## Closing Assessment

Session 21c delivered three results of direct relevance to neutrino physics: the P0-4 neutrino gate (INCONCLUSIVE), the dual algebraic trap (perturbative neutrino predictions structurally blocked), and the three-monopole topology (structural constraints on mass ordering and hierarchy). The session also closed the S_signed escape route and identified T''(0) as the sole perturbative survivor.

From the neutrino perspective, the framework's status has shifted subtly. In Session 20b, the neutrino prediction pipeline was STALLED (no mechanism to fix tau_0). In Session 21c, the pipeline is STRUCTURALLY BLOCKED at the perturbative level but has acquired new structural information from the monopole topology. The framework now knows MORE about its neutrino sector -- which sectors control the gap edge, where the avoided crossings live, what the coupling strengths are -- even though it cannot yet make specific mass predictions.

The critical next computation for neutrinos is not delta_T (P1-0) or the instanton action (P1-5). It is the COUPLED R(tau) from P1-2. If the off-diagonal coupling shifts R(tau) to pass smoothly through 33 at a physically relevant tau, the neutrino gate reopens and the framework gains a genuine overconstrained prediction. If it does not, the framework faces a neutrino-mass problem that goes deeper than stabilization.

**Probability assessment**: Framework overall: 43% (consistent with panel consensus, no shift from my perspective). Neutrino-specific predictive power: still 0% (no specific mass predictions possible without tau_0). Neutrino structural consistency: upgraded from "unknown" to "plausible" -- the bowtie topology, the singlet gap-edge control, and the Z_3 generation structure all point in the right direction. Conditional: if coupled R(tau) crosses 33 smoothly at tau in [0.15, 0.35], I upgrade neutrino consistency to "promising" and the framework to 48-50%.

The neutrinos are still waiting, as they have since Pauli (Paper 01, 1930). But the geometry is no longer silent about them. The monopoles speak. The bowtie constrains the ordering. The BCS gap suggests a hierarchy mechanism. What remains is the computation that turns structure into numbers -- and JUNO, DUNE, and Project 8 are measuring now. The geometry must speak clearly enough to be falsifiable before the experiments speak for it.

---

*Neutrino-Detection-Specialist, Session 21c collaborative review*
*Reference corpus: Papers 01, 05, 07, 08, 09, 10, 11, 12 from /researchers/Neutrino-Detection/*
*Previous reviews: sessions/session-19/session-19d-neutrino-collab.md, sessions/session-20/session-20b-neutrino-collab.md*
