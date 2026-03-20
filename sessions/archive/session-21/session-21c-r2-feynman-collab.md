# Feynman -- Round 2 Collaborative Review of Session 21c

**Author**: Feynman
**Date**: 2026-02-20
**Re**: Session 21c Master Synthesis + Errata Review

---

## Section 1: Key Observations

I have read the master synthesis, both errata, and the full CP-1 investigation output. Let me evaluate what the 15-reviewer process got right, what it got wrong, and what the new data means.

### 1.1 What Round 1 Got Right

The synthesis correctly identified the dual algebraic trap as the session's permanent mathematical contribution. Fifteen independent framings of the same theorem -- from Bianchi identities to phonon equipartition to impedance mismatch -- constitute the strongest validation any result in this project has received. The synthesis's structural conclusion is correct: the perturbative spectral program on SU(3) is finished, closed by representation theory rather than by computational failure.

The unanimous prioritization of delta_T as the decisive next computation was also correct. All 15 reviewers identified the right question. The problem is that the answer has now arrived, and it is not the one the framework needed.

### 1.2 What Round 1 Missed

The CP-1 mislabel is not a minor administrative error. It caused 15 specialists to skip an algebraic identity that turned out to be Trap 2 discovered from the flux side. The erratum correctly identifies this: b_1/b_2 = 4/9 at all tau, to machine precision, is the same group-theoretic fact as Theorem 1's branching coefficient ratio. The Cartan 3-form channel and the gauge-threshold correction are the same Dynkin embedding index. KK saw it from the flux side (Session 21b). Theorem 1 saw it from the branching side (Session 21c Phase A). The two independent derivations converging on the same ratio is the mark of a genuine structural constraint, and the synthesis buried it under a "REFUTED" label.

This is a concrete failure of the review process: label precision matters. "REFUTED AS MINIMUM MECHANISM" should have been parsed into two separate verdicts from the start. The synthesis's Section III (New Physics) contains 11 items, zero of which address the flux-spectral identity. That is a gap.

### 1.3 The 11 "New Physics" Findings: Assessment

I will evaluate each briefly from the path-integral / shut-up-and-calculate perspective.

**III.1 Jahn-Teller at M0**: Correct physics. The conical intersection at tau=0 with (0,0)/(1,1) degeneracy at lambda = sqrt(3)/2 is a textbook Jahn-Teller instability. The Jensen deformation IS the symmetry-lowering distortion. This elevates Jensen from parametrization to geometric necessity. Good physics, but does not change the computation.

**III.2 Acoustic Impedance Trapping**: Interesting idea, but the numbers need checking. A Fabry-Perot cavity in modulus space requires coherent reflection at both boundaries, which requires the modulus to behave as a propagating wave with well-defined impedance. The modulus is a CLASSICAL degree of freedom in the spectral action; calling it a "wave" requires the quantum mechanics of the modulus itself (the Wheeler-DeWitt equation). This is a Tier 2 computation, not Tier 0.

**III.3 EIH Derivation**: Pure theoretical check. If the modulus EOM follows from the 12D Bianchi identity, that is elegant but changes no numbers. Zero computational impact.

**III.4 Higgs-Sigma Portal**: This is the most underrated proposal. The coupling lambda_{H,sigma}(tau) comes from the a_4 coefficient of the spectral action, not from a spectral sum. It is structurally independent of the constant-ratio trap. Connes has been saying this since Session 20b. The synthesis correctly includes it but does not flag it as the highest-priority Tier 1 computation. It should be.

**III.5 BCS-BEC Crossover**: g*N(0) ~ 8-10 putting the system in the BEC regime is a quantitative observation with real consequences. In my Paper 05 (superfluid helium), the distinction between BCS weak-coupling and BEC strong-coupling is the distinction between exponentially small and O(1) gap. If the system is BEC, the condensate is ROBUST -- it does not require fine-tuned attractive interaction. This upgrades the BCS route.

**III.6 Lambda from Algebraic Trap**: Qualitative insight. The trap means perturbative vacuum energy cannot stabilize anything -- modulus or cosmological constant. As a direction for thought, fine. As evidence, zero.

**III.7-III.11**: Various interesting directions, none with immediate computational content.

**Net assessment**: The "New Physics" section is heavy on qualitative insight and light on computable predictions. III.4 (Higgs-sigma portal) and III.5 (BCS-BEC) are the items with the most concrete computational consequences.

---

## Section 2: Assessment of Errata

### 2.1 CP-1 Mislabel Correction: Correct and Important

The correction is precisely right. The CP-1 result always had two components:
1. The prediction that S_signed has a minimum -- REFUTED (S_signed is monotonically decreasing).
2. The algebraic identity that b_1/b_2 = 4/9 -- CONFIRMED to machine precision at all 21 tau values.

The investigation output confirms S_b1/S_b2 = 0.444444 at every single tau point with 0.00% deviation. The e^{-4tau} exponential component in S_b1(tau) is real (89.5% RSS improvement over linear fit), and the amplitude ratio A_b1/A_b2 = 0.4444 = 4/9 exactly. The identity propagates through the full nonlinear spectral action, not just at leading order.

From the proper-time perspective (Paper 11, SW-3), the spectral action Tr f(D^2/Lambda^2) can be decomposed into gauge-sector contributions:

```
S[tau] = S_singlet[tau] + S_fund[tau] + S_adj[tau] + ...
```

Each sector's contribution is individually tau-dependent, but the RATIO between the U(1) gauge-threshold piece (proportional to b_1) and the SU(2) piece (proportional to b_2) is LOCKED at 4/9 by the embedding. This is a representation-theoretic identity that holds for any smooth cutoff function f. It is tau-independent, f-independent, and Lambda-independent. It is the price the SM pays for living inside SU(3).

The connection to Trap 2 is exact: Trap 2 says Delta_b = b_1 - b_2 = -(5/9)*b_2 < 0 for all sectors. CP-1 says the same ratio appears in the Cartan flux channel. They are both reading off the Dynkin embedding index of SU(2) x U(1) in SU(3). Two independent calculations, same number.

### 2.2 Mode Reordering: Physical Window Confirmation

The first crossing at tau ~ 0.15 (sector (0,1) -> (0,0)) and second at tau ~ 1.55 (back to (0,1)) define the (0,0)-singlet dominance window [0.15, 1.55]. This is consistent with the three-monopole structure (M1 at ~0.10, M2 at ~1.58) to within the coarse grid resolution (dtau = 0.1).

The important observation from the output: the first crossing is driven by HYPERCHARGE ASYMMETRY (Delta_b1 = -0.667), while the later crossings between (0,1) and (1,0) at tau > 1.55 have Delta_b1 = 0 -- they are driven by a different mechanism (likely the exponential growth of the SU(2) vs U(1) scale factors in the Jensen metric). This is a structural distinction the synthesis did not flag.

### 2.3 Z_3 Triality: Uniform Distribution

All three Z_3 classes have delta_T positive throughout [0, 2.0], with ratios locked near 1/3 each (0.3324-0.3338). There is no Z_3 symmetry breaking in this channel. The slight asymmetry (Z3=0 slightly below 1/3, Z3=1,2 slightly above) is at the 0.4% level and likely a finite-cutoff effect.

This CLOSES any hope that Z_3-dependent structure in delta_T could select generations or provide sector-dependent fixed points. The e^{-4tau} identity acts uniformly across triality. The Z_3 symmetry is unbroken in the self-consistency map at one loop.

### 2.4 delta_T Positive Throughout: The Decisive Result

This is the new information that was not available during Round 1, and it demands an honest assessment.

delta_T(tau) = T(tau) - tau is positive for ALL tau in [0, 2.0]. It decays from 3399 at tau=0 to 3.04 at tau=2.0, monotonically. There is no zero crossing anywhere on the computed domain.

In my Round 1 review, I wrote: "crossing in [0.15, 0.35] -> 55-60%. No crossing -> framework drops to 33-37%." All 15 reviewers agreed on this pre-registered gate. The master synthesis stated: "crossing in [0.15, 0.35] -> 55-62%; no crossing -> ~35%."

No crossing was found. The pre-registered gate FAILS.

Let me be precise about what this means from the path integral (Paper 01, PI-1):

```
Z[tau] = integral D[fields] exp(-S_spectral[fields, tau])
```

The self-consistency condition tau = T[tau] requires delta_T to cross zero. At one loop, using the existing block-diagonal eigenvalue data and the branching coefficients, delta_T is everywhere positive. This means:

**T(tau) > tau for all tau.** The self-consistency map pushes the modulus to LARGER values at every point. There is no fixed point. The modulus runs away to infinity.

Now, there are escape routes from this conclusion:
1. **Off-diagonal coupling** (P1-2): The block-diagonal approximation neglects inter-sector mixing. The coupled diagonalization could shift the spectrum enough to create a crossing.
2. **Higher-loop corrections**: The one-loop result may be modified at two loops.
3. **Non-perturbative effects**: BCS condensate, instantons, flux -- all of which contribute terms not captured by the spectral sum.
4. **The computation is delta_T for a SPECIFIC definition of the self-consistency map.** Different regularization schemes could give different results.

But escape route (1) is the only one testable with existing technology. Escape routes (2)-(4) are increasingly speculative. And the pre-registered gate was stated without these caveats.

The honest assessment: the one-loop self-consistency map has no fixed point. This is a SOFT CLOSURE on the self-consistency route at one loop.

---

## Section 3: Collaborative Suggestions

### 3.1 Priority Reassessment After delta_T

The delta_T result changes the priority ordering. Let me reassess from the Tier 0 list:

**ELEVATED to Tier 0 #1: Coupled V_IR (was Tier 1 #1)**
With delta_T failing, the coupled diagonalization becomes the last remaining route to a perturbative fixed point. The block-diagonal treatment that underlies delta_T neglects mode mixing. If the off-diagonal coupling at the gap edge modifies the lowest eigenvalues by even a few percent, the delta_T profile could develop a zero. This is now the single most important computation. It requires eigenvector extraction, which bumps it to Tier 1 in cost, but it is Tier 0 in priority.

**ELEVATED to Tier 0 #2: Higgs-sigma portal (was Tier 1 #6)**
Connes's lambda_{H,sigma}(tau) is independent of spectral sums and therefore independent of the constant-ratio trap. With delta_T failing, non-spectral-sum stabilization mechanisms gain urgency. The a_4 coefficient computation is analytic and well-defined.

**My proper-time regularization sweep (was Tier 0 #2): STILL RELEVANT**
The delta_T result is computed with a specific cutoff (max_pq = 6). The proper-time regularization would test whether the positive-definite sign of delta_T is an artifact of the hard cutoff or robust across regularization schemes. From Paper 04 (MF-1), the Schwinger-regulated version:

```
delta_T_reg(tau, Lambda) = Sum_n Delta_b(n) * ln(lambda_n^2) * exp(-lambda_n^2/Lambda^2)
```

If delta_T_reg develops a zero at some Lambda, the hard-cutoff result is not robust. This remains a zero-cost diagnostic and should be run.

**DEMOTED: T''(0) IR decomposition (was Tier 0 #3)**
With delta_T positive everywhere, the IR decomposition of T''(0) is academic. The sign of T''(0) at the origin does not matter if the map never crosses the diagonal.

### 3.2 What the delta_T Profile Actually Tells Us

The decay from 3399 to 3.04 over tau in [0, 2] is approximately exponential. From the output:

```
delta_T(0.0) = 3399
delta_T(0.5) = 530
delta_T(1.0) = 96.9
delta_T(1.5) = 17.6
delta_T(2.0) = 3.04
```

This is consistent with delta_T ~ A * exp(-alpha * tau) with alpha ~ 3.5. The exponential decay means the map APPROACHES the identity T(tau) = tau asymptotically at large tau, but never reaches it. In the language of Wilson's RG (Paper 13, WI-1):

delta_T is a RELEVANT perturbation at tau = 0 (large magnitude) that flows to an IRRELEVANT perturbation at tau -> infinity (small magnitude). The "fixed point" is at tau = infinity, which is the decompactification limit -- the internal SU(3) collapses to a point, and the 12D theory reduces to 4D with no extra dimensions.

This is physically the WRONG fixed point. It means the one-loop self-consistency map drives the modulus toward decompactification, not toward the Weinberg angle window tau ~ 0.30.

### 3.3 The Non-Perturbative Route: What Must Be True

For the framework to survive, the non-perturbative correction must be NEGATIVE and must DOMINATE over delta_T ~ 530 at tau = 0.5 (the middle of the physical window). Let me estimate what this requires.

The BCS condensate contributes a term of order:

```
delta_T_BCS ~ -N(0) * Delta^2 / (64 pi^2)
```

where N(0) is the density of states at the gap edge and Delta is the gap. For this to overcome delta_T_pert ~ 530, we need:

```
N(0) * Delta^2 > 530 * 64 pi^2 ~ 3.3 x 10^5
```

With N(0) ~ 2 (from the singlet sector DOS) and Delta ~ Lambda * exp(-1/(g*N(0))):

```
Delta^2 > 1.65 x 10^5
Delta > 406
```

In natural units where the lowest eigenvalue lambda_1 ~ 0.87, this requires Delta ~ 400 lambda_1. The BCS gap would have to be 400 times the single-particle energy scale. This is not BCS weak-coupling -- this is deep BEC strong-coupling, consistent with Tesla's g*N(0) ~ 8-10 estimate. The condensate would have to be extremely strong.

This is not impossible -- in superfluid He-4, the condensate fraction is nearly 100% at T=0 (Paper 05, He-1). But it places a severe quantitative constraint on the BCS/BEC mechanism. The coupling must be VERY strong.

The instanton route faces a similar challenge: S_inst(tau) must produce a correction that overcomes delta_T ~ 530 at the relevant tau. Instanton contributions go as exp(-S_inst), so we need S_inst < ln(530) ~ 6.3. An instanton action of O(6) on SU(3) is not unreasonable -- it is in the semi-classical regime where instanton calculations are marginally reliable.

### 3.4 Novel Proposals from Section VII: My Rankings

From the 25 proposals, I rank the top 5 by computational tractability and physics content:

1. **#4 Higgs-sigma portal** (Connes, Tier 1): Independent of spectral sums. The a_4 coefficient is computable from the heat kernel. This is the cleanest escape from the trap. HIGHEST PRIORITY.

2. **#5 BCS-BEC crossover** (Tesla/QA, Tier 1): The g*N(0) ~ 8-10 estimate places the system in BEC regime. This changes the gap equation from BCS (exponentially sensitive) to BEC (power-law). The BEC gap is O(g*n) rather than exp(-1/g*N(0)). COMPUTE THE GAP in the BEC regime.

3. **#13 Stokes phenomenon at monopoles** (Berry, Tier 1): Instanton actions can undergo Stokes jumps at phase boundaries. If S_inst(tau) discontinuously decreases at M1 (tau ~ 0.10), the non-perturbative correction could switch on abruptly inside the physical window. This is a specific, computable prediction.

4. **#8 Order-one condition as algebraic tau_max** (Connes/Baptista, Tier 1): If the NCG first-order condition fails at some tau_max, the spectral triple itself ceases to exist. This would bound the modulus from above without any dynamics. Purely algebraic check.

5. **#2 Acoustic impedance mismatch** (QA/Tesla, Tier 0): The simplest version is: compute the WKB reflection coefficient at M1 and M2 using the spectral data. If R > 50%, the modulus bounces. Zero-cost diagnostic.

### 3.5 Connection to My Research Papers

**Paper 05 (Superfluid Helium)**: The delta_T result has a direct analog in superfluid He-4. Above T_lambda, the normal-fluid component dominates, and the "self-consistency map" (the Landau two-fluid equation for rho_s/rho) has no fixed point with rho_s > 0. Below T_lambda, the macroscopic BEC drives rho_s to finite values non-perturbatively. The perturbative (phonon gas) calculation never predicts superfluidity -- it predicts rho_s = 0 at all temperatures. The BEC is a non-perturbative phenomenon.

The analogy: delta_T > 0 everywhere is the perturbative calculation saying "no superfluid." The actual superfluid (if it exists) requires the non-perturbative BCS/BEC condensate to override the perturbative result. This is EXACTLY what happens in real condensed matter systems. The perturbative calculation always misses the phase transition.

**Paper 11 (Schwinger)**: The proper-time representation gives:

```
Gamma_eff = integral ds/s * f_tilde(s) * Tr exp(-s * D_K^2)
```

The delta_T computation uses the full eigenvalue data, not the Seeley-DeWitt expansion. But the SIGN of delta_T is controlled by the same UV/IR balance that determines whether the effective action is bounded below. The Schwinger pair-production formula (SW-5) shows that the effective action develops an imaginary part when eigenvalues become negative -- but Session 20b confirmed no tachyonic modes. So the real part of Gamma_eff is well-defined and delta_T is reliable within its one-loop, block-diagonal approximation.

**Paper 13 (Wilson RG)**: The delta_T profile is a RG flow. T(tau) > tau means the beta function is POSITIVE (modulus runs to larger values). The "fixed point" at tau = infinity is the Gaussian (free) fixed point. For a non-trivial fixed point at finite tau, the beta function must change sign. This requires a RELEVANT operator that is not captured by the one-loop spectral sum -- which is exactly the BCS condensate or the Higgs-sigma coupling.

---

## Section 4: Connections to Framework

### 4.1 The Perturbative-Nonperturbative Boundary

The delta_T result completes the perturbative program. Let me state the situation with full clarity:

**Everything the spectral action can compute perturbatively has been computed.**

The results: all perturbative spectral sums are monotonic (trapped by F/B = 4/11 and b_1/b_2 = 4/9). The self-consistency map at one loop has no fixed point. The effective potential has no minimum. The Seeley-DeWitt coefficients are all monotonic.

The framework now lives or dies on non-perturbative physics. This is not a retreat -- it is a sharpening. The perturbative closure tells us EXACTLY what the non-perturbative contribution must do: it must produce a negative delta_T correction of magnitude > 530 at tau ~ 0.5, or equivalently, it must create a minimum in V_eff at depth greater than the perturbative monotonic growth.

From the path integral (Paper 01), the non-perturbative sector consists of:
1. Instanton configurations (saddle points of the action with finite Euclidean action)
2. Condensates (non-zero vacuum expectation values that break the perturbative vacuum)
3. Topological contributions (Pfaffian signs, theta-terms, flux quantization)

Each of these is computable in principle. The question is whether any of them has the right magnitude and sign.

### 4.2 The A-B Tension Revisited

My predictions session (from memory) identified an A-B tension: the Weinberg angle wants tau_0 ~ 0.30, while phi_paasch wants tau_0 ~ 0.15. The delta_T result adds a third constraint: the perturbative self-consistency map has delta_T ~ 1081 at tau = 0.30 and delta_T ~ 1565 at tau = 0.20. The non-perturbative correction must overcome BOTH of these. The correction required at tau = 0.30 (for the Weinberg angle) is SMALLER than at tau = 0.15 (for phi_paasch), which slightly favors the Weinberg angle window.

### 4.3 The Spectral Action as Partition Function

The identification S_spectral = -ln Z (Paper 11, SW-3; Hawking Paper 07) means V_eff(tau) = -T * ln Z(tau) in the thermodynamic analogy. The perturbative monotonicity means the "free energy" has no minimum. In the condensed matter analogy, this is a system above its critical temperature -- the ordered phase (superfluid/superconductor) does not exist perturbatively. The BCS transition is the critical temperature below which the condensate forms.

The delta_T result quantifies the "distance from criticality": the perturbative delta_T at the Weinberg angle window (tau ~ 0.30) is 1081. The non-perturbative correction must exceed this threshold. This is the analog of the BCS condition g*N(0) > g_c*N_c(0) for the onset of superconductivity.

---

## Section 5: Open Questions

### 5.1 Is delta_T > 0 an Artifact of the Block-Diagonal Approximation?

The delta_T computation uses eigenvalues from block-diagonal diagonalization -- each (p,q) sector is diagonalized independently, with no inter-sector coupling. At the gap edge (lowest eigenvalues), the coupling between (0,0) and (0,1)/(1,0) sectors is STRONG (4-5x the eigenvalue spacing, from the Phase 0 analysis). The block-diagonal treatment misses this entirely.

In my experience with degenerate perturbation theory (Paper 04, Feynman parametrization), off-diagonal coupling ALWAYS modifies the lowest eigenvalues. The question is the SIGN: does coupling push the lowest eigenvalue DOWN (increasing the spectral sum, making delta_T more positive) or UP (decreasing it, making delta_T less positive or negative)?

Level repulsion generically pushes eigenvalues APART -- the lowest goes down, the highest goes up. This would make the spectral sum at the gap edge LARGER (more negative contribution to delta_T), potentially creating a zero. But this is hand-waving. The coupled diagonalization (P1-2) must be computed.

### 5.2 What Is the Correct Regularization for delta_T?

The formula used in the computation involves Sum Delta_b * ln(lambda^2), which is a UV-divergent sum regulated by the hard cutoff at max_pq = 6. Different regularization schemes (proper-time, zeta-function, Pauli-Villars) give different finite parts. Is delta_T > 0 robust across all consistent regularization schemes?

From dimensional regularization (the standard in QFT, Paper 12, DY-2), the finite part of a logarithmically divergent sum depends on the renormalization scale mu. If delta_T includes a mu-dependent piece, its sign could change with the choice of mu. This is why my proper-time sweep (Section 3.1) remains relevant even after the delta_T result.

### 5.3 The Deepest Question

Fifteen reviewers unanimously agreed that delta_T was the decisive computation. The computation has been done. The answer is: no zero crossing. By the pre-registered gate, the framework drops to ~35%.

The question that follows is: do we honor the pre-registration, or do we invoke the escape routes (off-diagonal coupling, non-perturbative corrections, regularization dependence)?

From my perspective (Paper 13, Wilson RG): the escape routes are legitimate physics. Off-diagonal coupling is a REAL effect that the block-diagonal computation misses. Non-perturbative corrections are REAL in every condensed matter system with a phase transition. Regularization dependence is a REAL issue for UV-divergent sums. None of these are post-hoc excuses; they are standard caveats that apply to any one-loop, block-diagonal, hard-cutoff computation.

But Sagan would say: each time a gate fails, invoking a new caveat to save the framework is exactly the accommodation pattern that Section IV.5 of the synthesis flags. Ten proposed-and-closed mechanisms across seven sessions. Now the self-consistency map joins the list.

Both positions are defensible. I choose to weight the pre-registration at approximately 70% and the escape routes at 30%. The framework takes a hit, but it is not closed.

---

## Section 6: Probability Update

### Pre-registered gate: delta_T crossing in [0.15, 0.35]
**Result: NO CROSSING. Gate FAILS.**

### Adjustments from my Round 1 assessment (42%)

| Factor | Shift | Justification |
|:-------|:------|:-------------|
| delta_T no crossing | -6 pp | Pre-registered gate failure. I stated 33-37% for no crossing. |
| CP-1 identity confirmed (= Trap 2) | +1 pp | Two independent derivations of the same ratio strengthens the mathematical structure. |
| Z_3 uniformity in delta_T | -1 pp | Closes sector-dependent fixed point hopes. |
| Mode reordering confirms physical window | 0 pp | Consistent with existing knowledge, not new evidence. |
| BCS-BEC crossover insight (III.5) | +1 pp | BEC regime means stronger condensate, partially offsets delta_T failure. |
| Off-diagonal coupling caveat | +2 pp | Legitimate physics not captured by computation. Partial restoration. |

**New assessment: 39%, range 35-42%.**

This is a genuine downward revision from my Round 1 value of 42%. The pre-registered gate failed, and I must take the hit. The 3 pp I recover from the off-diagonal caveat and the BCS-BEC insight prevent a full drop to the pre-registered 33-37%, because the computation that failed is explicitly block-diagonal and UV-regulated -- both known limitations.

The conditional has shifted:
- Coupled V_IR (P1-2) shows minimum -> 50-55% (upgraded from 55-60% because the perturbative landscape is now worse)
- P1-2 monotonic -> 30-33% (true closure of the self-consistency route)

---

## Closing Assessment

The master synthesis was an excellent product of the 15-reviewer process. It correctly identified the physics, correctly prioritized the computation, and correctly pre-registered the gates. The delta_T result answered the question that all 15 reviewers agreed was decisive. The answer was not the one the framework needed.

The CP-1 erratum was a genuine correction that deserved its own review. The flux-spectral identity (b_1/b_2 = 4/9 at all tau) is now confirmed from two independent directions, making Trap 2 one of the most thoroughly validated results in the project. The lesson -- label precision matters -- should be institutionalized for future sessions.

The framework survives, but with a wound. The one-loop self-consistency map has no fixed point. The non-perturbative route (BCS/BEC condensate, instantons, Higgs-sigma portal) must now overcome a quantitatively specified barrier: delta_T ~ 1081 at tau = 0.30. This is a concrete number. Either the non-perturbative physics can produce a negative correction exceeding 1081, or it cannot.

The perturbative calculation says "no superfluid." In He-4, the perturbative calculation also says "no superfluid." The lambda transition is real nonetheless. The question is whether SU(3) with Jensen deformation is more like He-4 (where the non-perturbative transition exists) or more like an ideal gas (where it does not).

The coupled diagonalization (P1-2) is now the last perturbative handle. After that, we are in the domain of non-perturbative physics, where computation becomes genuinely difficult. That is where the interesting physics always lives.

---

*Review grounded in: Feynman Papers 01 (path integral), 04 (proper-time regularization), 05 (superfluid He-4), 11 (Schwinger effective action), 13 (Wilson RG); CP-1 investigation output `tier0-computation/s21c_cp1_output.txt`; master synthesis + errata `sessions/session-21/session-21c-master-collab.md`; agent memory from Sessions 19d, 20b, 21a, 21c.*
