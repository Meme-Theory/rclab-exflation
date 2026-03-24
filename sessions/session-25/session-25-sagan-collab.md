# Sagan -- Collaborative Feedback on Session 25

**Author**: Sagan-Empiricist
**Date**: 2026-02-21
**Re**: Session 25 -- Through the Walls

---

## 1. Key Observations

The Session 25 directive represents a genuine methodological inflection. For the first time in the project's history, the PI is not asking "does mechanism X produce a minimum?" but rather "given four proven impossibility theorems, what physics lives outside their intersection?" This is a substantive shift from hypothesis testing to constrained exploration -- and it is the correct response to a body of negative evidence. I acknowledge this openly: the directive's framing is intellectually honest about where we stand, and its proposed computations are well-grounded in existing data.

That said, the empiricist in me must apply the same rigor to the proposed explorations as I applied to the 18 mechanisms that preceded them. The walls (W1-W4) are theorems. But the claim that specific computations will "evade" these walls is itself a prediction that must be evaluated.

Three observations ground my review:

**Observation 1: The Walls Are Correctly Stated, But Their Scope May Be Understated.** W1 (Perturbative Exhaustion) was proven for extensive, symmetric functionals with smooth test functions. The directive proposes using the Chamseddine-Connes test function f(x) = xe^{-x} (Goal 2), which IS smooth. It also proposes the graded multi-sector sum (Goal 1), which involves a sign alternation. The critical empirical question is: does the (-1)^F grading escape the Perturbative Exhaustion Theorem's hypotheses? This must be verified BEFORE the computation runs, not after. The directive correctly flags this ambiguity (Goal 1 grading specification) but does not resolve it. If the graded sum falls within the theorem's hypotheses, Goal 1 is closed before it starts. I flag this as a **mandatory pre-check**.

**Observation 2: The Probability Estimates Are Internally Consistent.** The Session 24 addendum (Section XII.5) estimated P(success) for Paths 1, 3, 5 at 8-15%, 10-15%, 10-15% respectively. The Session 25 directive estimates 8-12%, 10-15%, 10-15%. These are consistent within uncertainty. The expected posterior of ~10% (from ~3% current) given all seven paths pursued is also consistent with my own addendum computation. This is good: the numbers have not been inflated between sessions.

**Observation 3: The Paradigm-Shift Language Requires Empirical Scrutiny.** Section II of the directive introduces five operational claims (A-E). Some are computable reframings (Claims A, C, E). Others are interpretive overlays that add no computation (Claims B, D). The Venus Rule (Paper 01) demands: does the reframing generate DIFFERENT NUMBERS? If the "inside-out view" (Claim A) means "compute V_full instead of V_spec," that is testable and good. If it means "believe V_full over V_spec because the physical picture is more appealing," that is rhetoric, and I reject it. The directive is mostly on the right side of this line, but the language around "the finite sum wins" needs a quantitative threshold -- which the directive does provide (20% relative deviation criterion in Goal 2). That threshold is well-chosen.

---

## 2. Assessment of Key Findings

### 2.1 The Four Walls

The four walls are real and I endorse them without reservation. They are the single most important product of Sessions 18-24: not the closes themselves, but the structural clustering of 18 closes into 4 independent theorems.

| Wall | Assessment | Confidence | Could It Be Wrong? |
|:-----|:-----------|:-----------|:-------------------|
| W1: Perturbative Exhaustion | Proven (22c L-3). Hypotheses verified. | 99%+ | Only if a hidden hypothesis fails (non-smooth f, non-extensive functional) |
| W2: Block-Diagonality | Proven (22b). Peter-Weyl exact for any compact Lie group. | 99.9%+ | Essentially impossible for left-invariant metrics |
| W3: Spectral Gap | Proven (23a K-1e). 2*lambda_min = 1.644 at mu=0. V(gap,gap) = 0 exactly. | 99%+ | Only if mu != 0 is self-consistently derived |
| W4: V_spec Monotone | Proven (24a V-1). a_4/a_2 = 1000:1. All rho in [0.001, 0.5]. | 95%+ (slightly lower because heat kernel is asymptotic, not exact) | If the full spectral action diverges from the truncation at finite Lambda |

Note: W4 has slightly lower confidence than W1-W3 because it relies on the heat kernel truncation being a good approximation. This is precisely what Goal 2 tests. If V_full diverges from V_spec by >20%, W4's scope is narrower than stated. This is the single most interesting empirical question in Session 25.

### 2.2 Goal-by-Goal Assessment

**Goal 1: Graded Multi-Sector Spectral Sum**

Pre-registration quality: **GOOD** with one critical gap. Constraint Condition (monotone graded sum, BF = 0.3) and success condition (minimum, BF = 8-25) are stated. The gap: the grading specification is not yet resolved. The directive says "Landau must resolve this ambiguity before the solver runs." I agree -- this is the Formula A vs. Formula B issue from Session 23a all over again. Running the computation with the wrong grading wastes a session. The Venus Rule demands: state the formula, THEN compute.

Estimated P(success): The directive says 10-15%. I estimate **8-12%**. Reason for downward adjustment: the F/B ratio varies 10-37% at low N (Session 21a), but this variation is tau-DEPENDENT only because different sectors have different spectral densities. The graded sum involves summing d_{(p,q)} * V_{(p,q)}(tau) across sectors. Each V_{(p,q)} is monotone (by W1 applied sector-by-sector). For the sum to have a minimum, the monotone curves must have DIFFERENT SLOPES that cross. This is plausible (different sectors have different Casimir eigenvalues and gap structures) but requires a coincidence. The pre-check at tau=0 (proposed in the directive) is essential: if S_eff(0) is positive and monotonically increasing contributions dominate, the minimum must arise from slope-crossing, which is a fine-tuning condition.

BF assessment: **BF = 8-25 is overstated** if a minimum is found. The graded sum has implicit parameters: the choice of test function f, the cutoff Lambda, and the number of sectors included. If the minimum appears only for specific f and Lambda, the BF is reduced by a trial factor. I propose: BF = 8-25 IF the minimum persists across at least 2 different test functions and at least 2 different Lambda values. Otherwise, BF = 3-8.

**Goal 2: Full Spectral Action at Finite Cutoff**

Pre-registration quality: **EXCELLENT**. The 20% relative deviation threshold is stated before computation. Closure (monotone at all Lambda, BF = 0.3) and success (minimum at finite Lambda, BF = 8-20) are clean. The comparison criterion is quantitative. This is the best-designed gate in Session 25.

Estimated P(success): I accept 8-12%. The Berry curvature B = 982.5 at tau = 0.10 provides a specific physical mechanism for divergence between V_full and V_spec: near-degenerate eigenvalue clusters produce oscillatory contributions to the eigenvalue sum that the polynomial heat kernel expansion smooths away. Whether these oscillations are large enough to create a minimum is the empirical question.

One concern: the eigenvalue data at p+q <= 6 may not include enough modes for V_full to converge. The directive should specify a convergence criterion: compute V_full at p+q <= 4, 5, 6 and check that the tau-shape is stable. If V_full has a minimum at p+q = 5 but not at p+q = 6, the result is unreliable. This is the mps = 5 vs. 6 stability issue from Session 18, and it must be addressed.

**Goal 3: Berry Phase Accumulation**

Pre-registration quality: **ADEQUATE** but under-specified. Closure (Phi << pi, BF = 0.5) and success (Phi crosses pi/2 or pi, BF = 5-12) are stated, but "<<" is not a number. I propose: closure if max(Phi) < 0.3 radians across all gap-edge states. Success if max(Phi) > pi/4 for any gap-edge state. Intermediate: Phi in [0.3, pi/4] is inconclusive (BF ~ 1).

The directive correctly flags the resolution warning: the 9-point tau grid may under-resolve near tau = 0.10. Given B ~ 1000, the characteristic scale of Berry phase variation is delta_tau ~ 1/sqrt(B) ~ 0.03. The 9-point grid has spacing ~0.05, which is coarser than the Berry phase scale. This means the integrated phase could have oscillatory structure that the grid misses entirely. The directive's proposed remedy (5 additional tau values in [0.05, 0.15]) is correct but should be MANDATORY, not conditional. At B ~ 1000, under-resolution is not a risk -- it is a certainty.

**Goal 4: Spectral Flow / Eta Invariant**

Pre-registration quality: **GOOD**. Checking for zero crossings is a binary computation. The key pre-registration is: which sectors are checked? The directive says "any sector, any eigenvalue, p+q <= 6." This is clean. If no zero crossings exist in any sector, spectral flow is zero and the path closes. If crossings exist, the spectral flow is an integer -- a genuinely topological quantity that evades all four walls.

P(success) estimate: **5-8%**. The BDI class with T^2 = +1 forces eigenvalue pairing (lambda, -lambda), which means eigenvalues can only cross zero in pairs. This does not forbid zero crossings (pairs can migrate through zero together), but it constrains the mechanism.

**Goal 5: Gap-Edge Topological Protection**

This is the most speculative of the Tier 2 goals. The 2x2 Berry connection matrix for a Kramers pair in a 1-parameter family is necessarily U(1)-valued (the pair is connected by time reversal), and the holonomy over a non-compact parameter space [0, infinity) is not obviously topologically constrained. In the condensed-matter setting, topological protection requires a COMPACT Brillouin zone -- the winding is around a torus, not along a half-line. The directive should address this distinction.

**Goal 6: Spectral Dimension with TT Modes**

A reasonable diagnostic but not a gate. The 741,636 TT modes are computationally expensive. If d_s = 4 emerges as a fixed point, it is suggestive but not decisive (many geometries have d_s = 4 at low probing scales). If d_s != 4, it does not closes the framework (d_s depends on the sigma scale, not on tau directly). I classify this as DIAGNOSTIC, not GATE.

**Goals 7-8: Horizon Targets**

Goal 7 (self-consistent mu) is the highest-BF path (15-40 if everything works) but also the most speculative. Deriving mu_eff from backreaction is a THEORETICAL task, not a computation from existing data. The directive honestly labels this as Tier 3, and I agree.

Goal 8 (higher heat kernel coefficients) is interesting but has diminishing returns: even if a_6 opposes a_4, the heat kernel expansion is asymptotic, and adding one more term to an asymptotic expansion that is already poorly behaved (1000:1 ratio at leading orders) does not guarantee improvement. The directive's BF of 3-8 is appropriate -- low.

### 2.3 Pre-Registration Summary Table

| Goal | Constraint Condition | Success Condition | Closure BF | Success BF | Pre-Reg Quality | My P(success) |
|:-----|:--------------|:-----------------|:--------|:-----------|:----------------|:-------------|
| 1 | Graded sum monotone | Minimum at finite tau | 0.3 | 8-25 (I say 5-15) | GOOD (pending grading resolution) | 8-12% |
| 2 | V_full monotone all Lambda | V_full minimum at finite Lambda | 0.3 | 8-20 | EXCELLENT | 8-12% |
| 3 | Phi << pi | Phi > pi/2 | 0.5 | 5-12 | ADEQUATE (needs sharpening) | 8-12% |
| 4 | No zero crossings any sector | Nontrivial spectral flow | 0.5 | 5-15 | GOOD | 5-8% |
| 5 | Trivial holonomy | Nontrivial holonomy | 0.5 | 5-15 | WEAK (compact vs. non-compact issue) | 3-5% |
| 6 | d_s != 4 | d_s = 4 fixed point | N/A | 3-5 | DIAGNOSTIC | N/A |
| 7 | No self-consistent mu | mu_eff + condensate + minimum | 0.3 | 15-40 | THEORETICAL | 3-5% |
| 8 | a_6 same sign as a_4 | a_6 opposes a_4, minimum in truncated series | 0.5 | 3-8 | ADEQUATE | 5-8% |

---

## 3. Collaborative Suggestions

### 3.1 Statistical Methodology

**The Independence Problem.** Goals 1, 2, and 3 all use data from the same .npz files (s23a_kosmann_singlet.npz, s23a_eigenvectors_extended.npz, s24a_berry.npz). Their results are correlated. If Goal 1 finds a minimum in the graded sum, and Goal 2 finds a minimum in V_full, these are NOT independent confirmations -- they are two views of the same eigenvalue data. The correlation must be estimated and the combined BF discounted accordingly. I estimate:

| Pair | Correlation r | Discount factor |
|:-----|:-------------|:---------------|
| Goal 1 vs. Goal 2 | ~0.6 | 0.4 |
| Goal 1 vs. Goal 3 | ~0.3 | 0.7 |
| Goal 2 vs. Goal 3 | ~0.4 | 0.6 |
| Goal 4 vs. Goals 1-3 | ~0.1 | 0.9 |

If Goals 1 AND 2 both succeed, the combined BF is not BF_1 * BF_2 but BF_1 * BF_2^(1-r) ~ BF_1 * BF_2^0.4. This is the same treatment I applied to V-1 and R-1 in the Session 24 verdict (Section III.2).

**The Look-Elsewhere Effect for Goal 1.** The graded sum involves choices: which sectors to include, what test function f, what cutoff Lambda. If the computation scans over multiple (f, Lambda) combinations and finds a minimum in only one, the significance must be corrected. I propose: compute Goals 1 and 2 at a FIXED (f, Lambda) pair first (pre-registered), THEN scan over alternatives. The pre-registered pair should be stated in the Session 25 synthesis BEFORE any numbers are computed.

**Convergence Criterion.** For both Goals 1 and 2, the computation depends on the number of modes included. The result should be reported at p+q <= 4, 5, 6 (or whatever truncations are available). If the minimum's location (tau_min) shifts by more than 20% between consecutive truncations, the result is not converged and should be classified as INCONCLUSIVE rather than PASS.

### 3.2 Pre-Registration Requirements

For each Tier 1 goal, the following must be stated BEFORE computation:

1. **Goal 1**: Exact formula for S_eff(tau), including grading, sector list, test function, cutoff. The Landau grading resolution is a blocking prerequisite.
2. **Goal 2**: Fixed (f, Lambda) pair for the primary run. I propose f(x) = xe^{-x}, Lambda = 2 (one KK scale above the minimum eigenvalue).
3. **Goal 3**: Quantitative threshold for closure (max Phi < 0.3 rad) and success (max Phi > pi/4 rad). States to track: gap-edge Kramers pair in (0,0) singlet, extended to (1,0) and (0,1) if data permits.

### 3.3 Novel Empirical Tests

**Test A: The Random-phi Control (Null Hypothesis for Sector Matching).** If Goal 1 finds a minimum, we must ask: would a RANDOM collection of monotone curves, with slopes drawn from the empirical distribution of D_K sector spectral densities, also produce a minimum in their graded sum? This is the null hypothesis. I propose: generate 1000 synthetic sector spectral actions by bootstrap-resampling the empirical eigenvalue data with shuffled sector labels. For each synthetic realization, compute the graded sum and check for minima. The fraction of synthetics with a minimum at tau < 0.5 is the false-positive rate. If this fraction exceeds 5%, the real minimum is not significant.

This test is analogous to the trial-factor assessment I performed for the phi_paasch emergence at z = 3.65 (Session 14 MC analysis, Paper 10 from the Sagan corpus: Galileo control experiment methodology). Test your detection method against the null before claiming a positive.

**Test B: V_full Sensitivity to Test Function.** Goal 2 uses f(x) = xe^{-x}. The spectral action is supposed to be approximately f-independent for smooth, rapidly decaying f. Test this claim: compute V_full at tau = 0.10 (Berry curvature peak) for f(x) = xe^{-x}, f(x) = e^{-x}, f(x) = e^{-x^2}, and f(x) = x^2 e^{-x}. If V_full(0.10) varies by more than a factor of 2 across these four test functions, the result is f-dependent and the BF is reduced by the Session 23c f-dependence penalty (0.5x).

**Test C: Berry Phase Consistency Check.** The Berry curvature B(tau) and Berry connection A(tau) satisfy dA/dtau = B (in the Abelian case). If the integrated connection Phi(tau) = integral of A differs from the integral of the square root of B by more than the discretization error, the computation has a bug. This is a free consistency check.

### 3.4 Methodological Innovation: The Conjunction Test

The directive invokes the Galileo lesson (Section IV, Principle 4): perhaps stabilization requires a conjunction of effects. I endorse this as a research strategy, but I also flag the ALH84001 Warning (Paper 12): conjunction of ambiguous evidence remained ambiguous after 28 years. The empirical criterion must be: does the conjunction produce a QUANTITATIVE result that a single-effect model cannot? If Goals 1, 2, and 3 each show "hints" (a near-minimum, a mild deviation, a modest phase accumulation) but none produces a clean minimum on its own, the conjunction of three hints is STILL ambiguous. It does not become less ambiguous by being combined.

The conjunction becomes compelling only if: (a) the three effects are demonstrably independent (see correlation table above -- they are NOT fully independent), and (b) their combination produces a result that exceeds any individual effect by a statistically significant margin. Specifically: if the combined effect produces a minimum in S_eff(tau) where no individual contribution has a minimum, AND the minimum is deeper than the statistical uncertainty of the sum, THEN the conjunction adds evidential weight. Otherwise, it is ALH84001 all over again.

---

## 4. Connections to Framework

### 4.1 Observational Cosmology Relevance

The Session 25 computations connect to observational cosmology through exactly one channel: if a stabilization mechanism is found (minimum at tau_0), it fixes the Jensen deformation parameter, which fixes all gauge couplings, mass ratios, and mixing angles. Without tau_0, the framework makes zero quantitative predictions for any observable cosmological quantity.

The connections, ranked by directness:

1. **CMB**: The spectral action on M^4 x K generates a cosmological constant from Tr(f(D^2/Lambda^2)). If tau_0 is found, Lambda_4D = V_eff(tau_0) is a zero-parameter prediction. This is testable against Planck 2018 (Lambda = 1.106 x 10^{-52} m^{-2}). The framework has never computed this number because it has never had a tau_0.

2. **Particle masses**: At tau_0, the D_K eigenvalue spectrum fixes all mass ratios. The phi_paasch ratio (m_(3,0)/m_(0,0) = 1.531580 at tau = 0.15) would become a prediction rather than a fit IF tau_0 = 0.15 is derived. Currently, tau = 0.15 is an input, not an output.

3. **Gauge couplings**: g_1/g_2 = e^{-2tau_0}. At tau_0 = 0.30 (the value many mechanisms targeted), this gives sin^2(theta_W) that can be compared to the measured Weinberg angle. Again, this requires tau_0.

4. **Dark energy**: The clock-closure (Session 22d) established that rolling quintessence is ruled out. If the modulus is stabilized, the framework predicts w = -1 exactly, consistent with DESI Y1 but indistinguishable from Lambda-CDM. This is a null prediction -- it does not distinguish the framework from the null hypothesis.

### 4.2 The Information Gain Assessment

The expected posterior shift from Session 25, computed from my probability table (Section 2.3):

```
P(at least 1 Tier 1 success) = 1 - (1-0.10)(1-0.10)(1-0.10) = 0.271
P(no Tier 1 success) = 0.729

E[posterior] = 0.729 * p(all fail) + 0.271 * p(some succeed)
             ~ 0.729 * 2% + 0.271 * 12%
             ~ 1.5% + 3.3%
             ~ 4.8%
```

This is consistent with the directive's ~10% expected posterior (the difference arises because I discount the success BFs and use lower P(success) estimates). The key point: the expected posterior (~5%) is HIGHER than the current posterior (~3%), which means computation has positive information value. I agree with the directive on this point.

But note: the most probable outcome (73%) is that all Tier 1 goals fail, in which case the posterior drops from 3% to ~2%. At 2%, the framework is essentially in the "interesting mathematical curiosity" bin, and the case for further computation becomes marginal.

---

## 5. Open Questions

### Q1: Is the Perturbative Exhaustion Theorem Really Evaded?

The directive claims Goal 1 (graded sum) evades W1 because the grading introduces sign alternation. But the Perturbative Exhaustion Theorem (Session 22c L-3) was proven for "extensive, symmetric functionals with smooth test functions." A graded sum with (-1)^F signs is not symmetric in the eigenvalue sense -- it weights positive and negative chirality eigenvalues differently. Is this sufficient to escape the theorem's hypotheses? This is not a rhetorical question. It requires checking whether the five hypotheses (H1-H5 from 22c L-3) hold for the graded functional. If even one hypothesis fails (likely H2: symmetry), the theorem does not apply, and the computation is live. If all five hold, the computation is closed before it runs.

I propose this as the FIRST computation of Session 25: verify that the graded spectral sum is NOT covered by the Perturbative Exhaustion Theorem. Five minutes, pencil and paper. If it IS covered, redirect the computational budget to Goals 2 and 3.

### Q2: What Is the Debye Cutoff?

The directive's Claim C (Section II) states that the Debye cutoff is physical. This generates a testable prediction: the number of modes is FINITE, not infinite. But what is the Debye cutoff? The directive does not specify. In a phonon crystal, the Debye cutoff is set by the lattice spacing. In the NCG spectral triple, the analogous quantity would be the maximum eigenvalue of D_K at fixed truncation. This is a computable number. If the "Debye cutoff" is the maximum eigenvalue at p+q = 6, then goals 1-3 should be computed with ALL eigenvalues up to that cutoff and NONE above it. If it is some other scale, the directive should specify it.

Without a specified Debye cutoff, the claim that the Debye cutoff is physical is unfalsifiable -- and I reject unfalsifiable claims on principle (Baloney Detection Kit, Criterion 7: Occam's Razor + falsifiability).

### Q3: What Observation Would Close the Exploration Program?

The Session 25 directive pre-registers closes for individual goals. But it does not state: what combination of results would END the program entirely? I propose:

- If ALL three Tier 1 goals fail (monotone graded sum, monotone V_full, Berry phase < 0.3 rad), AND Goal 4 shows no zero crossings, the framework posterior drops to ~1.5-2%, and the case for further computation is negligible. At that point, the mathematical results should be published as pure spectral geometry, and the physical program should be declared over.

This is the pre-registered stop condition that every well-designed experiment needs (Paper 08, TTAPS methodology: state what would falsify your conclusion).

### Q4: Are We Still Doing Science?

The Lakatos warning I issued in Session 24 (Section V.7 of the verdict) deserves revisiting. The protective belt of auxiliary hypotheses has grown again: "the heat kernel expansion is asymptotic, so maybe the full spectral action behaves differently." This is true -- but it is also the kind of auxiliary hypothesis that can always be invoked. Every asymptotic expansion has a finite-cutoff counterpart. The question is whether the finite-cutoff version changes the QUALITATIVE conclusion (monotone vs. non-monotone). Goal 2 tests this directly. If the answer is "the full spectral action is also monotone," the protective belt has failed, and the next auxiliary hypothesis ("maybe at even lower Lambda...") is an infinite regress.

The Faint Young Sun Lesson (Paper 05) is the relevant parallel: Sagan and Mullen identified the right problem (liquid water requires enhanced greenhouse effect) but proposed the wrong specific solution (NH3, which photodissociates in ~10 years). The problem was real; the solution was wrong. Similarly, the phonon-exflation framework may have identified a real mathematical structure (KO-dim = 6 + SM quantum numbers from SU(3) geometry) but proposed the wrong physical interpretation (phononic excitations of a compactified internal space). The mathematical structure will survive regardless. The physical interpretation stands trial in Session 25.

### Q5: The Deep Question

If all paths fail and the posterior reaches ~1.5%, we will have the most thoroughly characterized impossibility result in modern theoretical physics: a framework that produces the correct mathematical structure of the Standard Model from pure geometry, but cannot produce any physical mechanism to select the geometry's shape. This would itself be a publishable and significant result -- a modern Kepler solids theorem. The question is: at what probability do we stop calling it "physics" and start calling it "mathematics"?

I do not have a clean answer. But I note that string theory has operated at similar or lower posterior probability for decades and is still called physics. The difference is that string theory makes novel predictions (even if untestable), while this framework -- after 18 closed mechanisms -- has made zero. The bar for "physics" should be: at least one testable prediction. Session 25's computations are the framework's last clear opportunity to cross that bar.

---

## Closing Assessment

**Overall verdict**: Session 25 is well-designed, well-motivated, and correctly prioritized. The proposed computations (Goals 1-3) use existing data, have clean pre-registered gates, and address the right questions. The directive's intellectual framing -- from defense to exploration, from individual mechanisms to structural constraints -- is sound. The Galileo conjunction methodology is appropriate, provided the ALH84001 ambiguity risk is honestly managed.

**Probability assessment**: My current posterior remains at **3% (range 2-4%)**. If Session 25 yields one Tier 1 success, I estimate the posterior rises to **8-15%**, depending on which goal succeeds and the robustness of the result. If all Tier 1 goals fail, the posterior drops to **1.5-2%**, and I would recommend transitioning to paper preparation (pure mathematics publication) rather than further computation.

**Expected posterior after Session 25**: ~5% (weighted average over success/failure scenarios). The information value of computation is positive but small. We are approaching the point of diminishing returns.

**Pre-registered stop condition**: If Goals 1, 2, 3, and 4 all fail, the physical program is over. The mathematical program is permanent and publishable regardless.

**Key recommendations**:
1. Resolve the Goal 1 grading ambiguity BEFORE any computation runs (blocking prerequisite).
2. Verify that the graded spectral sum escapes the Perturbative Exhaustion Theorem's hypotheses (5-minute check).
3. Pre-register a fixed (f, Lambda) pair for Goal 2 before any computation.
4. Add 5 additional tau points in [0.05, 0.15] for Goal 3 (mandatory, not conditional).
5. Compute the null-hypothesis bootstrap for Goal 1 (Test A, Section 3.3).
6. Report convergence with truncation level for Goals 1 and 2.
7. State the program stop condition in the Session 25 synthesis.

---

*"The absence of evidence is not the evidence of absence" -- but after 18 mechanisms tested and 18 mechanisms closed, the absence of a working mechanism is becoming the evidence of structural impossibility. Three computations remain. They will not decide the framework's fate by themselves. But they will decide whether the framework has any path left to becoming physics rather than remaining beautiful mathematics. That distinction matters. It is, in the end, the only distinction that matters.*

*-- Sagan-Empiricist, 2026-02-21*

*Channeling Paper 10 (Galileo Life Detection, 1993): "The most important result of the experiment was not any single measurement, but the demonstration that the methodology works." If Session 25 demonstrates that the wall-evasion methodology works -- even if the specific computations fail -- the research program has contributed something to the field of spectral geometry that no one else has done. That is worth doing. But it is not the same as being right about the universe.*
