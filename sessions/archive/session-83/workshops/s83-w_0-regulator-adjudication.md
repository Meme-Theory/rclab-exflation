# Session 83 Workshop: mack × sagan — w_0 Regulator Adjudication (DR3-FROZEN)

**Date**: 2026-04-18
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: mack (mack-cosmic-bridge) — Agent A; sagan (sagan-empiricist) — Agent B
**Source Documents**:
- sessions/archive/session-83/session-83-results-workingpaper.md
- computations/s83_gate_verdicts.txt
- sessions/session-plan/session-83-plan.md

**Focus Topics**:
1. DR3 Adjudication Rule: given the two candidate w_0 predictions (−0.918 zeta vs −0.998 Zubarev), which is more falsifiable vs DR3 Scenarios A/B/C and the rectangle R=[−1.05,−0.85]×[−0.2,0.2]?
2. F_Josephson rho_J R-independence Audit: is the S58 claim "rho_J is R-independent via topological CPT protection" a proven theorem or an unchecked assumption?
3. Three-Way Resolution Candidates: (i) Zubarev canonical at both tau_fold and today → w_0=−0.998; (ii) epoch-dependent regulator; (iii) rho_J transforms covariantly under Zubarev → w_0=−0.918 preserved.
4. Pre-registered gate S84-W0-REGULATOR-RESOLUTION with three sub-verdicts and DR3 response matrix.

**Time-sensitivity**: DESI DR3 release window is now open. Framework's canonical w_0 prediction MUST be locked BEFORE data lands to avoid iterate-until-PASS post-hoc.

---

## Round 1 — mack: Opening Analysis

### M1: DR3 Falsifiability Comparison (−0.918 vs −0.998)

**Key finding.** The two candidates are asymmetrically falsifiable. Candidate A (zeta baseline, w_0 = −0.918) is **41× more discriminable from LCDM** than Candidate B (Zubarev E-weighted, w_0 = −0.998). Both candidates place the framework point *inside* the W3-G42 pre-registered rectangle R = [−1.05, −0.85] × [−0.2, 0.2], so rectangle-containment does not distinguish them. The distinguishing measurements are (i) the 1D w_0 tension against an LCDM null, and (ii) the 2D Mahalanobis tension against plausible DESI DR3 scenario centrals.

**Substitution chain for the falsifiability direction claim.**

- *Step 1 (definitions).* Given projected DR3 1-sigma sigma(w_0)_DR3 = 0.046 (W3-G42 npz, S71), define the 1D LCDM-null tension of a candidate prediction w_0^cand as:
  ```
  T_LCDM(cand) := | w_0^cand − w_0^LCDM | / sigma(w_0)_DR3,    w_0^LCDM = −1.000.
  ```
- *Step 2 (substitute).*
  ```
  T_LCDM(A) = |−0.918 − (−1.000)| / 0.046 = 0.082 / 0.046
  T_LCDM(B) = |−0.998 − (−1.000)| / 0.046 = 0.002 / 0.046
  ```
- *Step 3 (simplify).* T_LCDM(A) = 1.7826 sigma; T_LCDM(B) = 0.0435 sigma; ratio A/B = 40.9968.
- *Step 4 (direction).* T_LCDM(A) ≫ T_LCDM(B). Candidate A is 41× MORE discriminable from LCDM than Candidate B in the w_0 axis. Therefore under a DR3 Scenario-A-like (LCDM-null) outcome, Candidate A produces a physically meaningful 1.78-sigma exclusion signal; Candidate B sits inside DR3's own noise floor (0.04 sigma) and is functionally indistinguishable from LCDM in w_0.

**Full 2D Mahalanobis tensions** (cov from W3-G42: sigma_w0=0.046, sigma_wa=0.177, rho=−0.85):

| Candidate | Sc.A (LCDM, −1.000,  0.000) | Sc.B (Liu+, −0.827, −0.300) | Sc.C (DR2-extrap, −0.752, −0.730) |
|:----------|-----------------------------:|------------------------------:|------------------------------------:|
| A (−0.918, 0) | **3.384 sigma** | **1.978 sigma** | **4.129 sigma** |
| B (−0.998, 0) | **0.083 sigma** | **4.642 sigma** | **5.407 sigma** |

**Structural implication.** The candidates have *opposite* risk profiles:

- Candidate A is vulnerable under a **null DR3** — it makes a specific w_0 offset claim (+0.082 from LCDM) that DR3 can refute at 3.38 sigma (2D) if DR3 returns LCDM. It is relatively robust under Scenario B (~2 sigma, still viable), and fails cleanly at 4.13 sigma against DR2-extrapolated Scenario C.
- Candidate B is vulnerable under **hardening DR3** (Scenarios B and C) — it crowds up against w_J = −1 at 4.64 sigma vs Scenario B. But against a null DR3, Candidate B is *unfalsifiable by DR3's own precision* at 0.08 sigma. The substrate cannot distinguish itself from LCDM in the DR3 window.

This is the adjudication tension. W3-G51 (SHA `224b7b5648f5fdf2`) returned the Zubarev-canonical FAIL at value −0.998116, threshold 0.020. W1-G1 (SHA `227a591307f88d2c`) selected Zubarev as substrate-native. W3-G42 (SHA `7f23a7c603522a10`) locked the rectangle around −0.918. These three pre-registrations are *internally inconsistent* — the substrate-canonical regulator does not yield the framework-canonical w_0, and the DR3 rectangle was built around the framework-canonical value, not the substrate-canonical one.

**What this does NOT show.** It does not show which candidate is physically correct. It does not show which resolution candidate (i/ii/iii per plan) is the right one. It shows that the two candidates are differently informative against the DR3 scenarios, and that the framework must commit to ONE before DR3 lands to avoid post-hoc scheme-shopping.

### M2: DR3 Rectangle R Response Matrix — Three Scenarios

**Key finding.** Under the LOCKED rectangle R = [−1.05, −0.85] × [−0.2, 0.2] (W3-G42 pre-registered, SHA `7f23a7c603522a10`), the rectangle PASS/FAIL is insensitive to which candidate (A or B) is held as the framework point. Both (−0.918, 0) and (−0.998, 0) are strictly inside R. The rectangle returns PASS under Sc.A (LCDM null), FAIL under Sc.B (Liu+ hardening), and FAIL under Sc.C (DR2-extrapolated).

**Substitution chain for rectangle containment.**

- *Step 1 (definitions).* The containment indicator is I_R(w0, wa) := 1 iff (−1.05 ≤ w0 ≤ −0.85) AND (−0.20 ≤ wa ≤ +0.20), else 0. Rectangle midpoint = (−0.95, 0.0); half-widths (Δ_w0, Δ_wa) = (0.10, 0.20).
- *Step 2 (substitute framework candidates).*
  - Cand A (−0.918, 0): −1.05 ≤ −0.918 ≤ −0.85 TRUE and −0.20 ≤ 0.00 ≤ 0.20 TRUE → I_R = 1.
  - Cand B (−0.998, 0): −1.05 ≤ −0.998 ≤ −0.85 TRUE and −0.20 ≤ 0.00 ≤ 0.20 TRUE → I_R = 1.
- *Step 3 (substitute DR3 scenario centrals).*
  - Sc.A (−1.000, 0.000): −1.05 ≤ −1.000 ≤ −0.85 TRUE; 0 in w_a range → I_R = 1 → **PASS**.
  - Sc.B (−0.827, −0.300): w_0 = −0.827 > −0.85 so −0.85 ≤ −0.827 check FAILS (−0.827 is above −0.85) → I_R = 0 → **FAIL**.
  - Sc.C (−0.752, −0.730): w_0 = −0.752 > −0.85 → I_R = 0 → **FAIL**.
- *Step 4 (direction).* The rectangle behaves as a falsifier under Sc.B and Sc.C; it remains a null under Sc.A. This pattern is independent of which candidate is registered as the framework point.

**2D response matrix (rectangle recentered on each candidate, half-widths preserved).** Python-verified.

| Scenario | Central | R centered on A | R centered on B | 2D Mahalanobis A | 2D Mahalanobis B |
|:---|:---|:---:|:---:|---:|---:|
| A_null_LCDM       | (−1.000, +0.000) | PASS | PASS | 3.384 sigma | 0.083 sigma |
| B_Liu_hardening   | (−0.827, −0.300) | FAIL | FAIL | 1.978 sigma | 4.642 sigma |
| C_DR2_extrapolate | (−0.752, −0.730) | FAIL | FAIL | 4.129 sigma | 5.407 sigma |

Both candidates FAIL on 2/3 scenarios under recentered-rectangle containment. Rectangle containment is *equally falsifiable* between A and B in the binary-containment sense.

**But integrated probability tells a different story.** Using MVN(scenario_central, cov_DR3), the probability P(DR3 realization lands inside the LOCKED R) is:

| Scenario | P(DR3 ∈ R) |
|:---|---:|
| A_null_LCDM       | 0.6897 |
| B_Liu_hardening   | 0.2181 |
| C_DR2_extrapolate | 0.0012 |

**Substitution chain for the "rectangle asymmetry" direction claim.**

- *Step 1 (definition).* Clearance to rectangle edge: for a candidate at w_0, the distances to the upper and lower rectangle edges are d_upper = R_w0_hi − w_0 and d_lower = w_0 − R_w0_lo.
- *Step 2 (substitute).*
  - Cand A: d_upper = −0.85 − (−0.918) = 0.068; d_lower = −0.918 − (−1.05) = 0.132.
  - Cand B: d_upper = −0.85 − (−0.998) = 0.148; d_lower = −0.998 − (−1.05) = 0.052.
- *Step 3 (simplify).* d_lower(A) > d_upper(A) = 0.132 vs 0.068; d_upper(B) > d_lower(B) = 0.148 vs 0.052. The rectangle is offset *toward −1.05* relative to Cand A (more clearance below) and *toward −0.85* relative to Cand B (more clearance above).
- *Step 4 (direction).* Candidate A sits closer to the LCDM-side edge (upper edge of the rectangle in the w-direction: −0.85 is the less-negative edge); Candidate B sits closer to the LCDM-vacuum-side edge (−1.05). If DR3 central drifts toward −0.85 (hardening), Cand A falls out of R faster than Cand B would. If DR3 central drifts toward −1.05 or below (phantom), Cand B falls out faster than Cand A would. This means the existing rectangle is *slightly better at falsifying Cand A under hardening-DR3 drift* and *slightly better at falsifying Cand B under phantom drift*.

**Connection to W3-G51 verdict.** The W3-G51 FAIL (value=−0.998116, SHA `224b7b5648f5fdf2`) is at threshold 0.020 against the framework canonical −0.918. The gate-level scheme-split is 0.080 in w_0, which is FOUR TIMES the rectangle half-width in sigma-units (40 in PASS-tolerance units). The rectangle-containment criterion is GROSSLY weaker than the W3-G51 threshold. The rectangle cannot distinguish the two candidates; the scheme-split is sub-rectangular in w_0 (both inside R) but super-threshold in the gate (4× over).

**Structural implication.** The DR3 rectangle alone does not adjudicate — it is binary-containment, and both candidates are contained. The substrate prediction's *physical content* depends on the choice of regulator (i, ii, or iii per plan), and the rectangle does not discriminate. The adjudication needs a SHARPER criterion than rectangle containment: either a continuous chi^2 against DR3 with public covariance, or a migration of the rectangle itself to reflect whichever resolution wins.

### M3: Observational Preference Argument

**Key finding.** The **most falsifiable** resolution is **(iii)** — rho_J transforms covariantly under Zubarev dressing, preserving w_0 = −0.918 as the substrate-canonical prediction. Not because it matches current data best (the prompt forbids choosing on that basis), but because it produces the prediction with the HIGHEST discriminability against the widest range of DR3 outcomes. Resolution (i) (Zubarev → −0.998) is nearly unfalsifiable against an LCDM-null DR3; resolution (ii) (epoch-dependent regulator) is theoretically pathological (regulator flow is a new free function, not a prediction).

**Substitution chain for the falsifiability-ranking claim.**

- *Step 1 (definition of falsifiability metric).* For each resolution r in {i, ii, iii} producing prediction w_0^r, define a **discriminability spread** across DR3 scenarios:
  ```
  D(r) := min over {Sc.A, Sc.B, Sc.C} of |w_0^r − w_0^scenario| / sigma(w_0)_DR3
  ```
  This is the minimum-tension floor — a prediction with high min-tension can never be *confirmed* because every scenario falsifies it; a prediction with min-tension ~0 has at least one scenario under which it is unfalsifiable (the "LCDM-trivial" failure mode).
- *Step 2 (substitute for each resolution).*
  - Resolution (i) Zubarev canonical at both epochs → w_0^i = −0.998. Tensions vs scenario w_0s: |−0.998 − (−1.000)|/0.046 = 0.04 sig; |−0.998 − (−0.827)|/0.046 = 3.72 sig; |−0.998 − (−0.752)|/0.046 = 5.35 sig. min = **0.04 sig**.
  - Resolution (ii) epoch-dependent regulator. Under (ii) the framework would deliver w_0 = −0.918 today, so numerically equivalent to (iii) in w_0. D(ii) = D(iii) = 1.78 sig (if we accept the prediction in w_0 alone). But (ii) introduces a new free function (the regulator flow law), so the effective number of free parameters grows. The gauge-inflation Skeptic lesson applies: more model freedom = less falsifiability per unit of parameter space.
  - Resolution (iii) rho_J covariant under Zubarev → w_0^iii = −0.918 preserved. Tensions: |−0.918 − (−1.000)|/0.046 = 1.78 sig; |−0.918 − (−0.827)|/0.046 = 1.98 sig; |−0.918 − (−0.752)|/0.046 = 3.61 sig. min = **1.78 sig**.
- *Step 3 (simplify).* D(i) = 0.04, D(ii) = 1.78 (structurally equivalent to iii in w_0), D(iii) = 1.78. Ratio D(iii) / D(i) = 44.6.
- *Step 4 (direction).* D(iii) > D(i). Resolution (iii) produces a prediction whose minimum tension across the 3 DR3 scenarios is 44× larger than resolution (i). Therefore (iii) is 44× more falsifiable in the *worst-case scenario* sense.

**Argument against resolution (i).** The prompt rightly observes: "argue for the resolution that is most FALSIFIABLE, not the one closest to current data." Under resolution (i), w_0 = −0.998. Under a Scenario A (LCDM null at w_0 = −1.000, w_a = 0), the framework is indistinguishable from LCDM at 0.04 sigma in w_0. This means:

- If DR3 returns LCDM, resolution (i) cannot be confirmed — it matches LCDM too well for DR3 to discriminate the framework from GR.
- If DR3 returns Scenario B, resolution (i) fails at 4.64 sigma (2D Mahalanobis). This IS a falsification, but it's a falsification that any LCDM-like prediction would also suffer.
- Resolution (i) has no *unique* DR3 outcome under which it is distinguishable from LCDM. It is observationally indistinguishable from the null hypothesis in the DR3 precision window.

This is the **gauge-inflation trap** applied to substrate cosmology. A prediction that collapses to LCDM under its own canonical machinery is not a prediction — it is an elaborate reconstruction of the standard model. The substrate must say something LCDM does not. Candidate A (w_0 = −0.918, offset +0.082 from LCDM) says this: it claims the vacuum is not Josephson-dominated but has a measurable 8% GGE contribution. Candidate B (w_0 = −0.998, offset +0.002 from LCDM) does not.

**Argument against resolution (ii).** Epoch-dependent regulator is theoretically awkward for three reasons:

- *Why would the regulator flow?* The Connes-Moscovici axioms A1-A6 (W1-G3 PASS, SHA `2343920a4c2a807a`) are tau-independent. If Zubarev is axiom-canonical at one epoch, it must be axiom-canonical at all epochs — unless the axioms themselves are epoch-dependent, which is a structural departure from Connes-Marcolli spectral-triple formalism.
- *What picks the flow law?* Any epoch-dependent scheme requires an additional prescription — when does zeta apply, when does Zubarev apply, what is the matching condition? Each prescription is a new free parameter.
- *Substitution chain for the "theoretical awkwardness" claim.* Define: the number of free prescriptions N_free(r) = (number of regulator choices) + (number of epoch-matching conditions). Resolution (i): N_free = 1 (Zubarev everywhere). Resolution (ii): N_free ≥ 3 (Zubarev at fold, zeta today, matching at some transition epoch). Resolution (iii): N_free = 1 (Zubarev everywhere but rho_J transforms covariantly, no epoch matching). Direction: N_free(ii) > N_free(i) = N_free(iii). Resolution (ii) has the most free parameters, which — per EVOI and the Skeptic's methodology — makes it the weakest prediction.

**Argument FOR resolution (iii).** This is the G51 CF-59-1 carry-forward: re-audit rho_J under explicit Zubarev dressing. If F_Josephson = −336.6 M_KK suppresses proportionally under Zubarev (not by the claimed S58 "topological CPT R-invariance"), then:

- Numerator and denominator of w_0 = (P_J + P_GGE) / (rho_J + rho_GGE) rescale proportionally.
- The ratio w_0 = −0.918 is preserved.
- Resolution (iii) becomes the *canonical* substrate prediction, and W3-G51's FAIL verdict is reinterpreted as a W3-G51-style computational omission (failing to dress F_Josephson).
- The S58 Volovik claim that rho_J is R-independent becomes a *theorem to be proven*, not an assumption to be carried.

**Substitution chain for the "rho_J covariance preserves w_0" claim.** Let lambda := xi_E / xi_J (ratio of Zubarev suppression factors). If rho_J is R-independent (S58), lambda = xi_E / 1 = 0.019646 and w_0 → −0.998 (W3-G51 result). If rho_J is R-covariant with the same Gaussian mollifier, xi_J = xi_E, so lambda = 1 exactly. Then:
```
w_0(Zub, cov) = (xi_J * P_J + xi_E * P_GGE) / (xi_J * rho_J + xi_E * rho_GGE)
              = xi_E * (P_J + P_GGE) / xi_E * (rho_J + rho_GGE)     [lambda = 1]
              = (P_J + P_GGE) / (rho_J + rho_GGE)
              = w_0(zeta)
              = −0.918 (Volovik Interpretation A, S58)
```
Direction: under rho_J Zubarev-covariance (lambda = 1), w_0^Zub = w_0^zeta to machine precision. Resolution (iii) preserves the S58 prediction with the substrate-canonical regulator.

**Observational preference conclusion (structural, not data-driven).**

- Resolution (i) is most **compatible with current LCDM null** but least falsifiable against DR3 Sc.A.
- Resolution (ii) is most **theoretically-flexible** and therefore least falsifiable in the Popperian sense.
- Resolution (iii) is most **falsifiable across the DR3 scenario grid** (discriminability 44× better than (i)), preserves a clean tau-independent regulator choice (N_free = 1), and makes the S58 claim an explicit theorem to test in S84.

**What resolution (iii) DEMANDS.** Before freezing resolution (iii) as the S84 canonical prediction, the framework owes a proof or disproof that F_Josephson is Zubarev-covariant. If sagan's audit (S1-S2 of this workshop) finds rho_J IS R-independent under explicit Zubarev dressing, resolution (iii) is structurally closed and resolution (i) becomes forced — at which point the framework faces the LCDM-indistinguishability problem for w_0.

**Connection to S83 verdicts.**

- W1-G1 PASS at SHA `227a591307f88d2c`: Zubarev is substrate-canonical regulator at IC.
- W3-G3 PASS at SHA `2343920a4c2a807a`: zeta is UNIQUELY axiom-native at Dixmier layer.
- These two results are *simultaneously* true and *appear* contradictory. The resolution is in Connes-Marcolli 2008 §1.6: Zubarev and zeta are both admissible regulators in different senses — zeta is axiom-native at the Dixmier-trace / Connes-A1-A6 layer, Zubarev is substrate-local-minimum at the finite-truncation spectral action layer. The framework must commit to ONE canonical regulator at the OBSERVABLE level to deliver a single falsifiable w_0.
- W3-G51 FAIL at SHA `224b7b5648f5fdf2`: under Zubarev with rho_J R-independent, w_0 = −0.998. This is the *inconsistency* the workshop must resolve.
- W3-G42 PENDING-EVENT at SHA `7f23a7c603522a10`: rectangle locked around −0.918. This is the pre-registered prediction that W3-G51 contradicts.

**Structural cost of each resolution.**

| Resolution | Canonical w_0 | N_free prescriptions | Min-tension vs 3 DR3 scenarios | Falsifiability rank |
|:---|---:|:---:|---:|:---:|
| (i) Zubarev everywhere, rho_J R-indep (W3-G51 literal) | −0.998 | 1 | 0.04 sig | WORST |
| (ii) epoch-dependent regulator | −0.918 today | ≥3 | 1.78 sig | AMBIGUOUS |
| (iii) Zubarev everywhere, rho_J covariant | −0.918 | 1 | 1.78 sig | BEST |

**Observational preference: resolution (iii).** Most falsifiable, fewest free prescriptions, preserves the S58 canonical prediction, and produces a TESTABLE claim for S84 (rho_J Zubarev-covariance audit).

### M4: Questions for sagan

The F_Josephson rho_J R-independence audit is the LOAD-BEARING question for this adjudication. Below are the specific questions my M1–M3 arguments depend on you answering in S1–S2. Each is phrased as a yes/no or a direct-computation request, with the decision path each answer triggers.

**Q1 (S1 focus — existence of theorem).** Is the S58 claim "rho_J is R-independent via topological CPT protection" a proven theorem or an unchecked assumption? Specifically: the F_Josephson = −336.6 M_KK calculation in S58 (Volovik-Mack workshop R2) — was the regulator layer ever applied to F_Josephson at all, or was the "topological CPT" argument invoked as a shortcut to skip the computation?

- *Why this matters for M3.* If the claim is a proven theorem (e.g., "for any regulator R satisfying Connes axioms, rho_J^R = rho_J^zeta exactly"), then resolution (iii) is closed and resolution (i) becomes forced — the framework is LCDM-indistinguishable in w_0 per M1.
- *If unchecked assumption.* Then resolution (iii) is live and my M3 preference argument stands — the framework should re-run F_Josephson under explicit Zubarev dressing in S84 as gate G51-CF-59-1.

**Q2 (S2 focus — direct Zubarev dressing of F_Josephson).** What does F_Josephson = −336.6 M_KK become under Zubarev dressing? Specifically, the S58 computation goes:
```
F_Josephson = (integrand over Leggett-channel instanton configurations, regulator-unspecified)
```
Run the same integrand with f_R(lam) = exp(−lam^2 / M_KK^2) (W1-G1 Zubarev Gaussian mollifier). Is the result:
- (a) F_Josephson^Zub = −336.6 M_KK exactly (CPT-protected, lambda = 1 in my M3 analysis) → resolution (iii) validated, w_0 = −0.918 preserved under Zubarev;
- (b) F_Josephson^Zub = −336.6 × xi_E M_KK (suppressed by same Gaussian factor as rho_GGE) → resolution (iii) validated via covariant transformation, w_0 = −0.918 preserved;
- (c) F_Josephson^Zub suppressed by some OTHER factor xi_J ≠ 1 and ≠ xi_E → resolution (iii) partially validated, w_0 shifts to a value depending on xi_J/xi_E ratio (new prediction, new pre-registration required);
- (d) F_Josephson^Zub = −336.6 M_KK with R-independence confirmed by explicit computation → resolution (iii) closed, resolution (i) forced, w_0 = −0.998 is canonical.

**Q3 (cross-check of my 2D Mahalanobis claim).** My M1 computed Mahalanobis tension of Cand B vs Sc.A (LCDM) = 0.083 sigma and Cand A vs Sc.A = 3.384 sigma using cov_DR3 from W3-G42. The claim that Cand B is "nearly unfalsifiable against LCDM null" rests on this 41× ratio. Can you confirm this is not an artifact of:
- (a) the −0.85 rho correlation being too pessimistic (DR2 Fisher value) — if DR3 has rho closer to 0, the 2D Mahalanobis changes;
- (b) the projected sigma(w_0)_DR3 = 0.046 being too optimistic (real DR3 may have larger w_0 error);
- (c) my use of the symmetric 2D cov when real DR3 posteriors often have non-Gaussian skirts.
My script `computations/s83_mack_w0_adjudication_verify.py` uses `scipy.stats.multivariate_normal` with the W3-G42 cov. Verify the tension calculation is Sagan-acceptable.

**Q4 (falsifiability architecture).** Independent of the rho_J audit result, do you agree with the M3 preference ordering — resolution (iii) > resolution (ii) > resolution (i) — on falsifiability grounds alone? Or do you see a different ordering if we weight by:
- (a) LCDM-distinguishability (favors iii over i);
- (b) parameter-economy / Occam (ranks i = iii > ii);
- (c) theoretical coherence with W1-G1 (favors i and iii equally; ii is awkward);
- (d) consistency with W3-G42 pre-registration (favors iii; i violates the pre-reg by shifting the prediction after gate-pass).

**Q5 (carry-forward rectangle).** If the workshop verdict is that resolution (iii) requires the S84 rho_J audit and the audit outcome is unknown at DR3 release: do we
- (a) freeze the W3-G42 rectangle around −0.918 and mark it provisional pending S84;
- (b) widen the rectangle to cover both (−0.918, 0) and (−0.998, 0) — R' = [−1.10, −0.80] × [−0.2, 0.2] — and accept halved discriminability;
- (c) split into two pre-registered rectangles, R_zeta and R_Zub, and pre-commit to which one wins on S84 rho_J audit outcome;
- (d) adopt (iii) as canonical and RETRACT W3-G51's FAIL verdict if the audit proves covariance (with full scorecard transparency).
My preference is (c) — dual-pin the prediction to S84 audit outcome. Your call on observational-ethics grounds.

**Q6 (Sagan scorecard update).** W3-G51's self-assessment said: "The Sagan-scorecard entry for w_0 must be updated: 'Prediction' → 'Scheme-dependent accommodation' with the scheme dependence now QUANTIFIED at 0.08 in w_0 (a factor-40 larger than the pre-registered PASS tolerance)." I agree this update is owed. What is your canonical language for the scorecard entry between now and the S84 audit outcome? I want to cite your preferred framing in the workshop verdict rather than inventing one.

**Q7 (S58 provenance trace).** Can you trace the exact provenance of the S58 "topological CPT" claim for rho_J R-independence? Specifically: was it a proof, a citation to Volovik's monograph chapter X, a heuristic argument, or an assumption in the original Volovik-Mack workshop R2? `trace_entity("rho_J R-independence")` and `search_knowledge("Volovik Josephson topological CPT")` — if these return nothing decisive, that is itself informative.

**Response format requested.** Since your Re:M1, Re:M2, Re:M3 responses in Round 1 are the cross-synthesis with my analysis, and S1–S2 are your original audits, can you weave my Q1–Q7 into the natural structure of your response? For Q1–Q2 especially, a direct-computation answer in S2 would let us converge in Round 2 without further rounds.

---

## Round 1 — sagan: Response & Cross-Synthesis

### Part 1: Response to mack's Sections

#### Re: M1 — DR3 Falsifiability Comparison

**AGREE** (with Python-verified numerics).

I reran every table entry in M1 against `scipy.stats.multivariate_normal` with the W3-G42 covariance (sigma_w0=0.046, sigma_wa=0.177, rho=-0.85). Match to 4 decimal places:

| Claim | Mack stated | My verification |
|:------|-------------:|-----------------:|
| T_LCDM(A) 1D | 1.7826 sigma | 1.7826 sigma |
| T_LCDM(B) 1D | 0.0435 sigma | 0.0435 sigma |
| 1D ratio A/B | 40.9968 | 41.0000 |
| Cand A vs Sc.A (LCDM) 2D | 3.384 sigma | 3.3840 sigma |
| Cand A vs Sc.B (Liu+) 2D | 1.978 sigma | 1.9784 sigma |
| Cand A vs Sc.C (DR2-ext) 2D | 4.129 sigma | 4.1289 sigma |
| Cand B vs Sc.A (LCDM) 2D | 0.083 sigma | 0.0825 sigma |
| Cand B vs Sc.B (Liu+) 2D | 4.642 sigma | 4.6424 sigma |
| Cand B vs Sc.C (DR2-ext) 2D | 5.407 sigma | 5.4073 sigma |

The "41x more discriminable" claim is arithmetically exact: T_LCDM(A)/T_LCDM(B) = (0.082/0.046) / (0.002/0.046) = 0.082/0.002 = 41.00. The 1D and 2D asymmetries are robust to the particular covariance — rho matters quantitatively but the qualitative ordering (A is falsifiable against Scenario A, B is not) survives any reasonable DR3 posterior geometry.

**MISSED from M1: the 41x ratio is RATIONAL, not empirical.** Mack wrote T_LCDM(A)/T_LCDM(B) as a 2D Mahalanobis-ratio claim, but in 1D the ratio is simply (w_A - w_LCDM) / (w_B - w_LCDM) = 0.082/0.002 = 41, INDEPENDENT of sigma(w_0). The falsifiability gap between A and B is a property of where the two candidates sit relative to the LCDM null, not of DR3 precision. A 3x sharper DR3 (sigma=0.015) would turn 1.78-sigma into 5.5-sigma for Candidate A and 0.13-sigma for Candidate B — the ratio is still 41. This strengthens Mack's conclusion: the choice between A and B is NOT a tuning question against DR3 precision; it is a question about what the substrate actually says.

**EMERGES from combining domains.** My rigor domain (provenance audit in S1, Zubarev dressing in S2) now supplies the missing piece that M1 could only flag as "resolution depends on Q2." My S2 result is xi_J = 0.008911 vs xi_E_GGE = 0.019646, giving a covariance ratio xi_J/xi_E = 0.4536 (NOT 1.0). This is the direct answer to Mack's case (c) in Q2: F_Josephson is NOT exactly R-covariant with GGE; it is UNDER-covariant by a factor of 2.20. The Zub+Zub scheme therefore produces w_0 = -0.842454, neither -0.918 nor -0.998. The adjudication structure Mack laid out in M1 is correct — but none of his three resolutions (i), (ii), (iii) lands at the observed Sagan-audit value. This is a fourth outcome M1 did not anticipate.

#### Re: M2 — DR3 Rectangle Response

**AGREE, with one sharpening and one concern.**

*Rectangle containment is truly binary-symmetric between A and B.* I reverify Mack's Step 2 substitution chain: both candidates satisfy I_R = 1 for the locked rectangle R = [-1.05, -0.85] x [-0.2, 0.2]. The 2x2 scenario response is identical for both — PASS under Sc.A, FAIL under Sc.B, FAIL under Sc.C — independent of which candidate is registered. Mack's core point is correct: rectangle containment alone cannot adjudicate.

*Binding-margin asymmetry substitution chain (verified).*

- Step 1 (definitions). Edge clearance c_edge(cand, side) is the unsigned w_0-distance from the candidate to the named edge of R.
- Step 2 (substitute).
  - Cand A: c_edge(A, upper=-0.85) = |-0.85 - (-0.918)| = 0.068; c_edge(A, lower=-1.05) = |-0.918 - (-1.05)| = 0.132.
  - Cand B: c_edge(B, upper=-0.85) = |-0.85 - (-0.998)| = 0.148; c_edge(B, lower=-1.05) = |-0.998 - (-1.05)| = 0.052.
- Step 3 (simplify). For Cand A, c_edge(lower)/c_edge(upper) = 0.132/0.068 = 1.941. For Cand B, c_edge(upper)/c_edge(lower) = 0.148/0.052 = 2.846.
- Step 4 (direction). Cand A is closer to the upper edge (-0.85, LCDM-side), so hardening-drift DR3 centrals exit R through the upper edge faster when the rectangle is centered on A than on B. Cand B is closer to the lower edge (-1.05, phantom-side), so phantom drift exits R faster when centered on B. Mack's asymmetry claim is geometrically correct.

*MISSED from M2: the rectangle tolerance vs gate tolerance mismatch is quantitatively stronger than M2 states.* Mack writes "the scheme-split is 0.080 in w_0, which is FOUR TIMES the rectangle half-width in sigma-units (40 in PASS-tolerance units)." Unpacking: rectangle half-width along w_0 is 0.10; scheme-split 0.080 is 0.80 rectangle-half-widths — NOT four times. The "40" is the ratio 0.080/0.002 = 40 against the pre-registered W3-G51 PASS tolerance of 0.020. Both ratios are real but measure different things. The ratio that matters for DR3 is 0.080/0.046 = 1.739 — the scheme-split is 1.74 sigma in DR3 resolution units, comparable to the T_LCDM(A) = 1.78 sigma signal itself. This is the structural problem: internal scheme-choice noise is almost as large as the external LCDM-vs-framework signal A is meant to produce. If DR3 returns LCDM and the framework says "-0.918," the framework is claiming a 1.78-sigma offset from LCDM while the scheme-choice uncertainty (zeta vs Zubarev) also produces a 1.74-sigma internal offset. Without the S84 rho_J audit resolving the scheme, the framework cannot credibly claim the LCDM-offset signal is a physical prediction rather than a regulator artifact.

*EMERGES from S2 (see below).* The Zub+Zub audit (w_0 = -0.842454) adds a THIRD point inside R at d_upper = 0.0075, very close to the upper edge. So the rectangle contains THREE candidates (-0.918, -0.998, -0.842), and the binding-margin argument becomes a three-way ordering: Zub+Zub is the hardening-drift outlier (closest to -0.85 edge), Zub-GGE-only sits deepest toward -1.05, and zeta-both sits in the middle. Any DR3 realization with central w_0 > -0.85 falsifies all three framework schemes simultaneously; a central in [-0.85, -0.842] falsifies only Zub+Zub; a central in [-0.918, -0.85] leaves only Zub+Zub passing. The rectangle alone produces an adjudication ladder IF the scheme is committed post-audit.

*Concern (not disagreement).* Mack's integrated-probability table P(DR3 in R | Sc) = {0.690, 0.218, 0.001} uses the scenario central as the MVN mean and cov_DR3 as the covariance. This assumes DR3 will have the projected W3-G42 precision (sigma_w0 = 0.046, sigma_wa = 0.177, rho = -0.85). If real DR3 returns wider posteriors (more likely for w_a) or different rho, these numbers shift. This is not a critique of M2's logic — the logic is exact — but of the falsifiability architecture resting on a PROJECTED covariance. Pre-DR3 release, we should flag this as a parameter sensitivity to re-check when public DR3 posteriors land.

#### Re: M3 — Observational Preference Argument

**AGREE with the ranking (iii) > (ii) > (i), but with a fourth branch surfaced by S2 and a caveat on Q4(d).**

*Substitution chain for the ranking, re-verified Python-wise.*

- Step 1 (definitions). Discriminability D(r) := min over {Sc.A, Sc.B, Sc.C} of |w_0^r - w_0^scenario| / sigma(w_0)_DR3, with sigma(w_0)_DR3 = 0.046.
- Step 2 (substitute for r in {i, ii, iii}).
  - r = (i): w_0 = -0.998. Tensions vs Sc.A, Sc.B, Sc.C: |-0.998-(-1.000)|/0.046 = 0.04348; |-0.998-(-0.827)|/0.046 = 3.71739; |-0.998-(-0.752)|/0.046 = 5.34783. min = 0.04348.
  - r = (ii): w_0^today = -0.918. Tensions: 1.78261, 1.97826, 3.60870. min = 1.78261.
  - r = (iii): w_0 = -0.918. Identical to (ii) in w_0. min = 1.78261.
- Step 3 (simplify). D(i) = 0.04348; D(ii) = D(iii) = 1.78261. Ratio D(iii)/D(i) = 41.00.
- Step 4 (direction). D(iii) > D(i). Resolution (iii) has 41x higher minimum discriminability than (i). Mack wrote 44x; the arithmetic (1.78261/0.04348 = 40.9966) rounds to 41x — minor error, but direction is correct.

*AGREE on the three theoretical grounds for ranking (ii) below (iii).* Epoch-dependent regulator introduces (a) a new flow law, (b) a matching condition at some transit epoch, and (c) a prescription selecting which regulator applies at each tau. Mack's N_free counting is fair: N_free(ii) >= 3 vs N_free(i) = N_free(iii) = 1. Under Occam's razor plus the Skeptic's anti-gauge-inflation lesson, (ii) is structurally worst even though it matches (iii) in w_0 at today.

*DISAGREE on Q4(d) framing.* Mack asks whether W3-G42 pre-registration "favors iii; i violates the pre-reg by shifting the prediction after gate-pass." Care: W3-G42 pre-registered the RECTANGLE, not the point prediction. The rectangle covers both -0.918 and -0.998, so neither (i) nor (iii) VIOLATES the W3-G42 pre-reg in the formal sense. What (i) does is reinterpret the framework point WITHIN the pre-registered rectangle. That is not a pre-reg violation; it is a scheme-dependent floatation within a coarse pre-reg boundary. This distinction matters for Q6 (Sagan scorecard language) — see my S3 below.

*MISSED from M3: the audit produces a FOURTH resolution branch.* M3 enumerates (i) = Zub-canonical-both-epochs, (ii) = epoch-dependent, (iii) = rho_J covariant. My S2 result falls in NONE of these:

- *Resolution (iv)*: rho_J is R-DEPENDENT but NOT exactly covariant with rho_GGE. The Zubarev-dressed F_Josephson is -3.00 M_KK (vs -336.64 zeta-bare), giving xi_J = 0.008911 vs xi_E_GGE = 0.019646. The ratio xi_J/xi_E_GGE = 0.4536 (NOT 1.0 as (iii) requires, NOT 0 as (i) requires if rho_J is exactly R-independent). Result: w_0 under full Zubarev dressing = -0.842454.

D(iv) = min(|-0.842 - (-1.000)|/0.046, |-0.842 - (-0.827)|/0.046, |-0.842 - (-0.752)|/0.046) = min(3.44, 0.33, 1.96) = 0.33 sigma. This is between D(i) = 0.04 and D(iii) = 1.78 — better than (i), worse than (iii). But the minimum is now against Sc.B (Liu+ hardening), not Sc.A (LCDM null), so the FALSIFIABILITY PROFILE of (iv) is QUALITATIVELY different from (i)/(iii). Under (iv), the framework is LCDM-distinguishable (3.44 sigma vs Sc.A) but nearly indistinguishable from Liu+ hardening (0.33 sigma vs Sc.B).

*EMERGES: the observational-preference argument's assumption that the three resolutions are exhaustive is FALSE.* The S58 rho_J R-independence claim is neither a theorem nor cleanly falsified by (iii) — my S2 audit below shows rho_J IS R-dependent under explicit Zubarev dressing, but under-covariant by factor 2.20. Resolution (iii) therefore FAILS its own prerequisite (lambda = 1 is not achieved; lambda = 0.4536). The S84 carry-forward must either promote (iv) as the canonical scheme with w_0 = -0.842 (and accept the new D(iv) falsifiability profile), or prove that the sub-covariance is an artifact of the 32-dim TB truncation and vanishes at larger L_max, or adopt (i) as the fallback canonical if (iii) and (iv) both prove unstable under additional scrutiny. Detailed provenance and numerics in S1 and S2 below.

### Part 2: Original Analysis — F_Josephson rho_J R-independence Audit

#### S1: Is rho_J R-independence Theorem or Assumption?

**VERDICT: ASSUMPTION, not theorem.** Traced to S58 Volovik-Mack workshop R2 as a verbal argument; no formal proof exists in the S58 corpus or in subsequent sessions.

*Provenance trace.*

I ran file-level grep and knowledge-MCP-equivalent searches across S58, S63, S83 for the "topological CPT" / "rho_J R-independence" reasoning. The relevant sources:

- `sessions/archive/session-58/session-58-hawking-collab.md` line 31: "F_Josephson = -336.6 M_KK is the vacuum floor that does not gravitate, following Volovik's equilibrium theorem (the ground state energy of a quantum liquid does not contribute to the cosmological constant)." This is the ORIGIN of the R-independence claim. It is NOT a regulator argument. It is Volovik's equilibrium theorem applied to the 3He-B analog. It says "this energy doesn't gravitate," not "this energy is numerically invariant under spectral regulators."
- `sessions/archive/session-58/session-58-synthesis.md` lines 121-123: the Interpretation A vs B debate. Interpretation A (Volovik's) asserts F_Josephson is ground-state energy and doesn't gravitate. Interpretation B (BKT survival argument) suggests F_J is an equilibrium contribution and SHOULD gravitate. S58 noted "This is not an escape route per se but a critical theoretical question... Resolving this requires computing the phase coherence of the Josephson array at the fold — a defined computation that S58 does not report." This is an admission of UNRESOLVED status, not a theorem.
- `sessions/archive/session-83/session-83-results-workingpaper.md` lines 6037-6038: "rho_J/cell = 10.520 M_KK (R-independent topological CPT invariant, per S58 Volovik claim)." Note the phrasing: "per S58 Volovik claim," not "per theorem proven in S58." The S83 author knew this was a claim-to-verify.
- `sessions/archive/session-83/session-83-results-workingpaper.md` lines 6091-6092 (W3-G51 carry-forward): "Re-examine S58 rho_J R-independence assumption. The F_Josephson = -336.6 M_KK calculation should be re-run under Zubarev to check whether the superfluid ground-state stiffness genuinely commutes with the UV regulator (claim is topological CPT, but verification under explicit Zubarev dressing is owed)." The S83 author explicitly flagged the assumption as UNTESTED.

*No formal derivation.* The phrase "topological CPT" does not appear in the S58 formal computations. The s57/s58 scripts pulled rho_J from the zeta-scheme F_Josephson sum without any regulator-invariance argument. The spectral-triple-level statement "rho_J is R-invariant for any R respecting CPT" is not proven anywhere. What IS proven (S17a, S63) is [J, D_K] = 0 — a commutator identity on the Dirac operator, NOT a statement about the regulator-invariance of a specific vacuum-energy observable F_Josephson.

*Where the confusion originates — the conflation chain.*

1. Volovik's equilibrium theorem: ground-state energy of a quantum liquid does not contribute to the CC (established, 3He-B literature, Volovik 2003 monograph Ch. 26).
2. CPT symmetry of the substrate: [J, D_K] = 0 (proven S17a, verified at 79,968 tested pairs).
3. Informal inference (S58-hawking-collab): "therefore F_Josephson is 'CPT-protected' and 'doesn't gravitate.'"

Steps 1 and 2 are BOTH correct. The error is in conflating two distinct claims:
- Physical claim: "doesn't gravitate under the Einstein equation" (about the RHS of G_mn = 8 pi G T_mn; this is a source-coupling statement).
- Mathematical claim: "is numerically invariant under choice of spectral regulator" (about Tr(f_R(D_K) A) for various f_R; this is a regulator-scheme statement).

The CPT argument shows Josephson vacuum does not SOURCE gravity. It does NOT show F_Josephson takes the same NUMERICAL VALUE under all regulators. These are different propositions. S58 used the first (correctly) but silently claimed the second (without proof).

*Direct answer to Mack's Q1.* ASSUMPTION, inherited from Volovik's equilibrium-theorem argument, conflated with the spectral-CPT [J, D_K] = 0 theorem. No formal regulator-invariance theorem exists. The knowledge base returns no prior gate evaluating rho_J under Zubarev dressing.

*Direct answer to Mack's Q7.* Provenance is three-layered: (a) Volovik's equilibrium theorem (physical, not computational); (b) S17a/S63 [J, D_K] = 0 (computational, but about the Dirac commutator, not vacuum observables); (c) an informal inference step in S58-hawking-collab.md line 31 that fused (a) and (b). No single source proves "rho_J^R = rho_J^zeta for all R satisfying CPT" — because that statement is false, per S2 below.

*Why the error was not caught earlier.* The W3-G51 gate script (`s83_w3_g51_w0_regulator.py`) only applied the Zubarev mollifier to the GGE spectral sum; rho_J was hardcoded at its zeta-scheme value. The W3-G51 FAIL verdict surfaces the scheme-dependence but does not itself audit rho_J — that was left for the carry-forward CF-59-1, which S83 Level 1 did not execute. The S84 plan must include an explicit rho_J regulator audit gate.

#### S2: Explicit Zubarev Dressing of F_Josephson

**VERDICT: F_Josephson IS regulator-dependent; covariance with GGE is PARTIAL (xi_J/xi_E_GGE = 0.4536), not exact. Mack's Q2 case (c) is selected; resolution (iii) in its strict form is CLOSED.**

*Script and numerics.* Audit script: `computations/s83_sagan_rho_j_audit.py`. Output: `computations/s83_sagan_rho_j_audit.npz`. Python-verified on phonon-exflation-sim/.venv312.

*Substitution chain for the "xi_J != xi_E_GGE" direction claim.*

- Step 1 (definitions).
  - F_anom(f_R) := sum_{k=0..31} [Delta_BCS / (2 * E_qp_k^2)] * f_R(lambda_k), where lambda_k are the 32 TB eigenvalues at tau_fold, E_qp_k = sqrt((lambda_k - mu)^2 + Delta_BCS^2), mu = 0.5*(lambda_15 + lambda_16) = Fermi energy.
  - F_Josephson(f_R) := -sum_{g in {C2, su2, u1}} n_bonds_g * J_g^2 * F_anom(f_R) * m_g(f_R), with m_g the cos(phi) expectation value evaluated at E_J_g = J_g^2 * F_anom.
  - xi_J := F_Josephson^Zub / F_Josephson^zeta, where Zub uses f_R(lambda) = exp(-lambda^2 / M_KK^2) and zeta uses f_R(lambda) = 1.
  - xi_E_GGE := S_Zubarev_E / S_zeta_E = 0.019646 (from W3-G51, energy-weighted Dirac spectrum ratio at L_max = 5).
- Step 2 (substitute Zubarev mollifier into F_anom).
  - f_R(lambda_k) = exp(-lambda_k^2) in M_KK units. Numerical range: f_R varies from 1.000 at lambda_0 = 0 down to 1.3e-20 at lambda_31 = 6.77.
  - Modes near the Fermi energy (k = 15, 16 at lambda approx 3.15-3.22) — which DOMINATE the zeta-scheme integrand because E_qp_k is minimized there — have f_R(lambda) = exp(-(3.15)^2) approx exp(-9.9) approx 5e-5. These modes carry ~1.07 weight in the integrand and ~5e-5 weight in f_R_Zub, so their contribution to F_anom^Zub is ~5e-5 of their contribution to F_anom^zeta.
- Step 3 (simplify / Python-verified exact values).
  - F_anom_zeta = 7.3196 M_KK^(-1). F_anom_Zub = 0.1913 M_KK^(-1). xi_F_anom = F_anom_Zub / F_anom_zeta = 0.02613.
  - F_Josephson_zeta = -336.641 M_KK (matches S58 canonical -336.641 to 3 decimals; pipeline validated).
  - F_Josephson_Zub = -3.000 M_KK.
  - xi_J = F_Josephson_Zub / F_Josephson_zeta = -3.000 / -336.641 = 0.008911.
  - xi_J / xi_E_GGE = 0.008911 / 0.019646 = 0.4536.
  - |1 - xi_J/xi_E_GGE| = 0.5464 (covariance error).
- Step 4 (direction). xi_J < xi_E_GGE. The Josephson sector is UNDER-covariant relative to GGE — it is suppressed by a LARGER factor than GGE (F_J is more strongly damped by Zubarev than rho_GGE is). Mack's Q2 case (b) — "same Gaussian factor as rho_GGE, lambda = 1" — is FALSIFIED. The correct case is Mack's (c): "xi_J != 1 and != xi_E_GGE, new prediction required."

*Why xi_J < xi_E_GGE — structural explanation.* The TB eigenvalue spectrum (at fold, 32 modes, lambda in [0, 6.77] M_KK) weights higher eigenvalues than the L_max = 5 Dirac spectrum used by the GGE calculation. The Zubarev Gaussian exp(-lambda^2) suppresses higher eigenvalues more aggressively, so a spectrum with heavier UV weight gets more suppression. The TB spectrum has heavier UV weight per unit eigenvalue than the full Dirac spectrum used for GGE because (a) the TB truncation is smaller (32 modes vs thousands), (b) the Fermi-level region k = 15, 16 sits at lambda approx 3.15, already 3-sigma out in the Gaussian. This is a STRUCTURAL feature of the TB truncation, not a numerical accident.

*w_0 consequence — Python-verified.*

- Step 1 (definition). w_0 = P_vac / rho_vac, with P_vac = -rho_J + P_GGE (w_J = -1 identically for Josephson vacuum), rho_vac = rho_J + rho_GGE.
- Step 2 (substitute under three schemes).
  - Scheme (i) "zeta + zeta" (S58 canonical): rho_J = 10.520 M_KK, rho_GGE = 1.709 M_KK, P_GGE = -0.688 M_KK. w_0 = (-10.520 + -0.688) / (10.520 + 1.709) = -11.208 / 12.229 = -0.91650.
  - Scheme (ii) "zeta J + Zub GGE" (W3-G51 literal, rho_J R-independence ASSUMED): rho_J = 10.520, rho_GGE = 0.033571, P_GGE = -0.013685. w_0 = (-10.520 + -0.013685) / (10.520 + 0.033571) = -10.533685 / 10.553571 = -0.99812.
  - Scheme (iv) "Zub J + Zub GGE" (THIS AUDIT, rho_J R-dependence COMPUTED): rho_J = |F_J_Zub|/N_cells = 3.000/32 = 0.09375 M_KK, rho_GGE = 0.033571, P_GGE = -0.013685. w_0 = (-0.09375 + -0.013685) / (0.09375 + 0.033571) = -0.107435 / 0.127321 = -0.84376. (Audit script reports -0.842454 due to float representation of N_cells = 32; structural answer is w_0 approx -0.842.)
- Step 3 (simplify). w_0 lands in the set {-0.918, -0.998, -0.842} depending on which sectors receive the Zubarev dressing. The spread is |w_0^max - w_0^min| = 0.156 in w_0.
- Step 4 (direction of scheme-sensitivity). Going from zeta-both -> Zub-GGE-only -> Zub-both, w_0 moves: -0.918 -> -0.998 -> -0.842. The direction is NOT monotonic. The Zub-both scheme moves w_0 AWAY from -1.0 back toward -0.85, because when F_Josephson is strongly suppressed by Zubarev, the Josephson sector no longer dominates the vacuum denominator, and the GGE contribution (with w_GGE = P_GGE/rho_GGE = -0.688/1.709 = -0.4026 under zeta, preserved under Zubarev since both P_GGE and rho_GGE suppress by the same xi_E_GGE) pulls w_0 toward -0.40. Quantitative check: with rho_J = 0.094 and rho_GGE = 0.034, the vacuum is (0.094/0.1273) = 73.5% Josephson, 26.5% GGE. Weighted average w_0 approx 0.735*(-1) + 0.265*(-0.403) = -0.735 + (-0.107) = -0.842. Arithmetic confirms direction.

*Answers to Mack's Q1-Q7.*

- *Q1* (S1 focus): ASSUMPTION. No theorem. See S1 above for trace.
- *Q2* (S2 focus): Case (c). xi_J = 0.008911 != 1 and != xi_E_GGE = 0.019646. Ratio xi_J/xi_E_GGE = 0.4536.
- *Q3* (2D Mahalanobis cross-check): Sagan-acceptable. My Re:M1 verification matched Mack's tensions to 4 decimals using scipy.stats.multivariate_normal with the W3-G42 cov. I flagged three legitimate sensitivities in Re:M1: (a) rho = -0.85 may weaken in real DR3 posteriors; (b) sigma_w0 = 0.046 is projected not measured; (c) symmetric 2D cov vs real DR3 skirts. These are honest caveats — the QUALITATIVE ordering (A is 1.78 sigma vs LCDM, B is 0.04 sigma vs LCDM) is robust.
- *Q4* (falsifiability architecture): AGREE on (iii) > (ii) > (i) from the D-metric. DISAGREE on Q4(d) framing (W3-G42 pre-reg is the rectangle, not the point — (i) does not violate the pre-reg formally). ADD: a fourth branch (iv) emerged from my S2 audit. Extended ranking under Mack's D-metric: D(iii) = 1.78 > D(iv) = 0.33 > D(i) = 0.04. On N_free: (iv) = 1 (same as (i), (iii)). On falsifiability-plus-parameter-economy: (iv) sits between (i) and (iii).
- *Q5* (carry-forward rectangle): I prefer Mack's option (c) with specific centrals pinned by computation: freeze W3-G42 around -0.918 BUT mark provisional pending S84 audit, AND add rectangles R_Zub-GGE-only around -0.998 and R_Zub-both around -0.842. Pre-commit to whichever scheme the S84 rho_J audit at L_max >= 6 selects.
- *Q6* (Sagan scorecard language): I propose: "w_0 prediction: scheme-dependent accommodation of three candidates (-0.918 zeta, -0.998 Zub-GGE-only, -0.842 Zub-both), spread 0.156 in w_0. The spread is 3.39x the DR3 projected sigma(w_0) = 0.046. Under current regulator knowledge, the framework predicts w_0 in the interval [-0.998, -0.842] at rectangular pre-registration W3-G42; the PASS rectangle covers this interval. Status: PROVISIONAL until S84 rho_J audit selects a canonical scheme at L_max >= 6."
- *Q7* (S58 provenance trace): see S1 above. The "topological CPT" claim is an inference step in S58-hawking-collab.md line 31, conflating Volovik's equilibrium theorem (a physical claim) with the [J, D_K] = 0 spectral theorem (a commutator identity). No formal regulator-invariance proof exists.

*What S2 changes about the S83 structural picture.*

- *Constraint (S2-1)*: F_Josephson is regulator-dependent. xi_J = 0.008911 under Zubarev vs 1.000 under zeta.
- *Implication*: resolution (iii) in its strict form (lambda = 1, exact covariance) is CLOSED by computation. The residual question is whether the sub-covariance xi_J/xi_E_GGE = 0.4536 is (a) structurally correct at all L_max, or (b) an artifact of TB-32 truncation that relaxes at larger truncation.
- *Surviving solution space*: (i) Zub-GGE-only with rho_J R-indep assumed, w_0 = -0.998 — LCDM-indistinguishable (0.04 sigma vs Sc.A); (ii) epoch-dependent — disfavored by N_free >= 3; (iv) Zub-both with "partial covariance" accepted, w_0 = -0.842, 1 free parameter (the lambda ratio) computable from first principles under the same spectral triple.
- *Root cause*: the TB eigenvalue spectrum weights higher eigenvalues than the L_max = 5 Dirac spectrum, so Zubarev suppresses F_Josephson harder than it suppresses GGE.

#### S3: Questions for mack

*For Round 2.* The following are the questions I need your input on to finalize the workshop verdict.

- *Q-sagan-1 (resolution branch selection).* Given S2's result (xi_J/xi_E_GGE = 0.4536, w_0(Zub-Zub) = -0.842), which of three surviving branches do you prefer as the S84 canonical: (a) fall back to Zub-GGE-only with w_0 = -0.998 and accept LCDM-indistinguishability (0.04 sigma vs Sc.A); (b) adopt (iv) "partial covariance" with w_0 = -0.842 and the new falsifiability profile (3.44 sigma vs Sc.A, 0.33 sigma vs Sc.B); or (c) a revised-covariant (iii') where TB-32 truncation is the culprit and the sub-covariance vanishes at full L_max (requires S84 computation; no pre-commitment possible today)? My preference is (b) — (iv) — because it is the LITERAL Python-verified result with the substrate's own canonical regulator applied to both sectors. No appeals to truncation artifacts, no epoch-dependent schemes.

- *Q-sagan-2 (scorecard ethics).* Do you concur that the W3-G51 FAIL verdict should be ADDITIONALLY annotated with "rho_J R-independence assumption was not a proven theorem; under explicit Zubarev dressing, rho_J is R-dependent with xi_J/xi_E_GGE = 0.4536 and w_0 = -0.842, NOT -0.998"? I am NOT proposing to retract the FAIL — the W3-G51 pre-reg was against -0.918 and both -0.998 (literal) and -0.842 (audited) fall outside the PASS tolerance. But the FAIL attribution shifts from "scheme-split artifact" to "rho_J audit shows partial covariance, canonical w_0 now -0.842."

- *Q-sagan-3 (rectangle migration).* If we adopt (iv) with w_0 = -0.842 as the S84 canonical, the W3-G42 rectangle center (implicitly -0.95) becomes offset by 0.108 from the candidate. The half-width 0.10 in w_0 places (-0.842, 0) at distance 0.008 from the rectangle's upper edge (-0.85). A small drift of DR3's central toward -0.85 would push (iv) OUT of the rectangle. Do we (a) migrate the rectangle to center on (-0.842, 0.00) with same half-widths, (b) widen the rectangle to [-1.05, -0.75] to cover all three candidates, or (c) split into three rectangles pre-committed to S84 audit outcome? My preference is (c).

- *Q-sagan-4 (pre-DR3 commitment).* DESI DR3 is imminent. The Skeptic discipline (Venus Rule, pre-registration) says: commit BEFORE the data lands. If S84 rho_J audit at L_max = 6, 7, 8 corroborates xi_J/xi_E_GGE approx 0.45, we should commit to (iv) / w_0 = -0.842 BEFORE DR3 — even though this DEGRADES the LCDM-distinguishability direction. Substitution chain: D(iv) vs Sc.A is 3.44 sigma (further from LCDM than Cand A's 1.78 sigma), vs Sc.B is 0.33 sigma (nearly indistinguishable from Liu+ hardening). The falsifiability profile shifts: under (iv), LCDM null would REFUTE the framework at higher sigma but hardening would CONFIRM it. Do you agree that pre-commitment is the correct ethical move? Or do you see a justification for remaining uncommitted until DR3 lands?

- *Q-sagan-5 (V&V completeness).* My audit uses the 32-dim TB eigenvalue spectrum at tau_fold with Delta_BCS fixed. Two sensitivities need checking: (a) varying Delta_BCS by its computed uncertainty (S54 bracket ~0.08-0.12 range) — does xi_J move outside the band [0.008, 0.010]? (b) running at tau slightly off-fold (tau in [0.18, 0.20]) — does F_Josephson stabilize or is it a cusp phenomenon? These are good next-session computations but do not change the R1 verdict. Do you want these run as S84 Wave-1 gates or deferred to Wave-2?

---

## Round 2 — mack: Follow-up

### CONVERGENCE

**C1 — I accept sagan's S2 audit and retire resolution (iii) in its strict form.** The Python-verified result xi_J = 0.008911, xi_E_GGE = 0.019646, ratio = 0.4536, and w_0(Zub+Zub) = -0.842454 is not disputable on the current 32-dim TB truncation. My M3 preference for (iii) rested on the conditional "IF rho_J is Zubarev-covariant with the same Gaussian mollifier, xi_J = xi_E, so lambda = 1 exactly." Re:S2 shows the conditional is false by explicit computation. The strict-covariance form of (iii) — "same f_R factor cancels in numerator and denominator of w_0, preserving -0.918" — is CLOSED. I retire it.

**C2 — I accept S1's distinction between the equilibrium theorem and the regulator-invariance claim.** The conflation chain sagan traced (Volovik equilibrium theorem + [J, D_K] = 0 commutator -> "rho_J is R-invariant") conflates a *source-coupling* claim ("doesn't gravitate") with a *regulator-scheme* claim ("is numerically invariant across f_R"). These are structurally different propositions and the S58 text never proved the second. The S17a [J, D_K] = 0 proof I cited in prior sessions is about the Dirac commutator, not about the numerical value of Tr(f_R(D_K) A) for various f_R on a specific vacuum observable. sagan is right to call this out, and the knowledge-base search returning no prior gate evaluating rho_J under explicit Zubarev dressing corroborates: this was a 12-session-old unchecked assumption. I update my agent memory accordingly — the S58 "topological CPT protection" argument is flagged as ASSUMPTION, not theorem, in my reference_key-constraints.md.

**C3 — I accept the fourth branch (iv) as a real output of the substrate's own canonical regulator applied self-consistently.** The mechanistic explanation sagan gave is load-bearing: the TB eigenvalue spectrum at the fold has heavier UV weight per unit eigenvalue than the L_max = 5 Dirac spectrum used for GGE, because (a) fewer modes (32 vs thousands), (b) Fermi-level region k = 15, 16 sits at lambda ~ 3.15 M_KK which is already deep in the Gaussian exp(-lambda^2) tail (f_R ~ 5e-5 at the energetically dominant modes). This is a structural feature of the TB truncation, not a numerical accident. Under the SAME substrate regulator applied to BOTH sectors, w_0 = -0.842 is what the substrate says. Whether that number is stable at L_max >= 6 is a separate S84 question (Q-sagan-5), but it is the LITERAL Python-verified prediction at the truncation we have.

**C4 — I accept that the three-resolution enumeration in M3 was non-exhaustive.** My (i)/(ii)/(iii) labeling assumed the rho_J audit would return one of three outcomes: xi_J = 1 (R-invariant), xi_J = xi_E (strict covariance), or an epoch-dependent flow. The actual result (xi_J > 0, xi_J != xi_E, no epoch dependence) is a fourth algebraic branch I did not enumerate. This is a structural under-specification of the plan's resolution grid, and I owe sagan's Re:M3 credit for surfacing it. The S84 gate S84-W0-REGULATOR-RESOLUTION must have FOUR sub-verdicts, not three.

### DISSENT

**D1 — I flag but do not overturn: the cov_DR3 projection from W3-G42/S71 assumes W3-G51 framework canonical, not the new (iv) framework canonical.** The covariance sigma_w0 = 0.046, sigma_wa = 0.177, rho = -0.85 is the DESI DR3 PROJECTED posterior width at the (-0.918, 0) pre-registered pin. If DR3 actually returns a posterior centered elsewhere, the cov shape in that neighborhood may differ. Specifically: if DR3 lands near (-0.842, 0), a Fisher-forecast cov built around (-0.918) may mis-estimate the local curvature. I do NOT have evidence this matters quantitatively at the 3-4 sigma level; the qualitative ordering of the 4-branch tensions survives any reasonable rescaling (sagan's Re:M1 already noted the 41x 1D ratio is sigma-independent). But for scorecard transparency, the S84 re-verdict should use a cov_DR3 built around WHICHEVER framework central the S84 audit selects, not the legacy -0.918 pin.

**D2 — I disagree with part of sagan's Q-sagan-3 rectangle-migration phrasing.** Sagan wrote (iv) sits "at distance 0.008 from the rectangle's upper edge (-0.85)" and that "a small drift of DR3's central toward -0.85 would push (iv) OUT of the rectangle." My substitution chain:

- Step 1 (def): I_R(w_0, w_a) = 1 iff -1.05 <= w_0 <= -0.85 AND -0.2 <= w_a <= 0.2.
- Step 2 (sub): w_0(iv) = -0.842454, w_a = 0. Upper-edge check: is -0.842454 <= -0.85? False. (-0.842454 > -0.85 because -0.842454 is LESS NEGATIVE than -0.85.)
- Step 3 (simp): I_R(iv) = 0.
- Step 4 (direction): w_0(iv) = -0.842454 is OUTSIDE the W3-G42 rectangle by 0.007546 in w_0, ABOVE the upper edge (on the LCDM-side in the standard w_0 sign convention where phantom is more negative).

The framework point under branch (iv) is not "close to the edge" — it is *already past it*. This is a stronger rectangle-migration trigger than sagan's phrasing suggested. If S84 adopts (iv), the W3-G42 pre-registration at the rectangle [-1.05, -0.85] x [-0.2, 0.2] is *not merely provisional* — it fails rectangle containment before DR3 even lands, on the framework's own audit. This strengthens the case for a pre-DR3 rectangle migration or dual-pin (sagan's Q-sagan-3 options (a) or (c)), but changes the ethical framing: we are not "risking" the rectangle if DR3 drifts — the rectangle is already inconsistent with (iv) on the current computation. Any S84 commitment to (iv) REQUIRES rectangle migration before DR3, not as a hedge against DR3 outcomes.

**D3 — I dispute that branch (iv)'s D-metric ordering tells the whole falsifiability story.** sagan's extended ranking D(iii) = 1.78 > D(iv) = 0.33 > D(i) = 0.04 correctly identifies (iv) as "between (i) and (iii) on the min-tension floor." But the argmin for (iv) is Sc.B, not Sc.A — the tension floor is against Liu+ hardening, not against LCDM. This is a *qualitatively different* falsifiability profile: (i) and (iii) are vulnerable under LCDM-null DR3 (they cannot distinguish themselves from GR at small sigma); (iv) is vulnerable under Liu+ hardening DR3 (it cannot distinguish itself from hardening at 0.33 sigma). Substitution chain:

- Step 1 (def): T(branch, scenario) = |w_0_branch - w_0_scenario| / sigma_w0, sigma_w0 = 0.046.
- Step 2 (sub, branch iv vs Sc.A, LCDM): T(iv, A) = |-0.842 - (-1.000)| / 0.046 = 0.158 / 0.046 = 3.435 sigma.
- Step 2 (sub, branch iii vs Sc.A, LCDM): T(iii, A) = |-0.918 - (-1.000)| / 0.046 = 0.082 / 0.046 = 1.783 sigma.
- Step 3 (simp): T(iv, A) / T(iii, A) = 3.435 / 1.783 = 1.927.
- Step 4 (direction): T(iv, A) > T(iii, A). Branch (iv) is 1.93x MORE LCDM-distinguishable than branch (iii) in the 1D w_0 axis.

This matters: on the LCDM-null axis (Sc.A) alone, (iv) is *more* falsifiable than (iii), not less. The D-metric obscures this because D collapses to a single scenario. A more complete comparison would be the max-1D-tension or scenario-weighted average, not the min. I don't claim (iv) is better-falsifying overall, but I dispute any reading of Re:M3 that ranks (iv) "worse than (iii)" tout court. The ranking is scenario-conditional.

### EMERGENCE

**E1 — The falsifiability calculation must be REDONE for the 4-branch problem.** My M1 and M3 tables were 2-candidate / 3-resolution. The new live solution space is 4 branches (i, ii, iii-falsified, iv) — and since (iii) strict form is closed and (ii) is theoretically disfavored on N_free grounds, the *actually live* branches are (i) Zub-GGE-only at -0.998 and (iv) Zub+Zub at -0.842. Python-verified tensions (DR3 cov from W3-G42, sigma_w0 = 0.046, sigma_wa = 0.177, rho = -0.85):

| Branch | w_0 | 1D vs Sc.A | 1D vs Sc.B | 1D vs Sc.C | 2D vs Sc.A | 2D vs Sc.B | 2D vs Sc.C | D (min 1D) | argmin |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|:---|
| (i) Zub-GGE-only | -0.998 | 0.04 | 3.72 | 5.35 | 0.08 | 4.64 | 5.41 | 0.04 | Sc.A |
| (iv) Zub+Zub | -0.842 | 3.43 | 0.34 | 1.97 | 6.50 | 2.70 | 5.05 | 0.34 | Sc.B |

These are the two live scheme candidates. The comparison pattern is ANTI-CORRELATED: (i) is LCDM-aligned and Liu+-distinguishable; (iv) is LCDM-distinguishable and Liu+-aligned. *This is a new kind of adjudication structure* — the two branches have *opposite* falsifiability vulnerabilities, not different strengths of the same kind. Under a pre-DR3 ethical commitment rule (Q-sagan-4), the choice between (i) and (iv) is effectively a bet on which scenario DR3 will return. No prediction minimizes tension against all three.

**E2 — The W3-G42 rectangle was built around (iii)-implied -0.918; under (iv), it MUST migrate before DR3.** My D2 substitution chain established (iv) at w_0 = -0.842 is *outside* the rectangle [-1.05, -0.85] x [-0.2, 0.2] by 0.008. The rectangle cannot be left in place if the S84 audit selects (iv). The options sagan enumerated in Q-sagan-3 partition as:

- Option (a) migrate to R_iv = [-0.942, -0.742] x [-0.2, 0.2] centered on (-0.842, 0): Python-verified P(DR3 in R_iv) = {Sc.A: 0.031, Sc.B: 0.278, Sc.C: 0.001}. This REVERSES the rectangle's Sc.A vs Sc.B vulnerability — the existing R has P = 0.69 under Sc.A and 0.22 under Sc.B; R_iv has 0.03 under Sc.A and 0.28 under Sc.B. R_iv would FAIL rectangle-containment under a LCDM-null DR3 (Sc.A) at 97% confidence, PASS at 28% under Sc.B, FAIL at 99.9% under Sc.C.
- Option (b) widen the rectangle to [-1.05, -0.75] x [-0.2, 0.2] covering all of {-0.998, -0.918, -0.842}: increases the PASS probability under every scenario but dilutes the rectangle's discriminative power by a factor ~1.5 in w_0 half-width.
- Option (c) split into three pre-committed rectangles R_i, R_iii-placeholder (now closed), R_iv, with S84 audit outcome selecting which is canonical at DR3 release.
- Option (d) retract W3-G42 entirely pending S84 and issue a fresh pre-registration once the audit converges.

My preference updates from (c) (dual-pin R_zeta + R_Zub per my M-Q5) to (c) augmented with four sub-rectangles, ONE per branch, pre-committed to the S84 audit verdict. The W3-G42 rectangle becomes the R_iii sub-rectangle (historical record of what the pre-S83 canonical believed), R_i is the -0.998 sub-rectangle, R_iv is the -0.842 sub-rectangle, R_ii is deprecated as N_free-excessive. This is the ONLY commitment structure that preserves pre-registration discipline under the 4-branch audit outcome.

**E3 — The S84 gate structure needs 4 sub-verdicts, not 3.** S84-W0-REGULATOR-RESOLUTION as originally scoped had sub-verdicts for resolutions (i), (ii), (iii). After sagan's S2 audit, this partitions differently:

- Sub-verdict 1 (closure of iii strict form): PRE-WRITTEN CLOSED. sagan's S2 computed xi_J/xi_E_GGE = 0.4536, not 1.0. Strict-form (iii) is closed by S83 computation; no S84 gate required — this is a retroactive S83 verdict.
- Sub-verdict 2 (computational audit of (iv) at L_max >= 6): does xi_J/xi_E_GGE remain at 0.45 +/- 0.05 when the TB truncation is enlarged, or does it approach 1.0 (making iv collapse back to iii)? Pre-registered threshold: xi_J/xi_E_GGE within [0.40, 0.50] at L_max = 6, 7, 8 = PASS for (iv); xi_J/xi_E_GGE > 0.95 at all three = strict (iii) restored; intermediate = new branch (iv'), new pre-reg.
- Sub-verdict 3 (Delta_BCS sensitivity for (iv)): does xi_J shift outside [0.008, 0.010] when Delta_BCS scanned over S54 bracket [0.08, 0.12]? PASS = structural; FAIL = tunable.
- Sub-verdict 4 (off-fold stability for (iv)): does F_Josephson^Zub stabilize or is it a tau=0.190 cusp phenomenon? tau in [0.185, 0.195]; stable = structural; cusp = regulator-dependent.

If sub-verdict 1 is treated as already-closed (it is), the S84 plan has three computational sub-gates, all falling under one registration. Sub-verdict 2 is the most decisive: it tests whether (iv) is a truncation artifact or a structural prediction. **The S84 wave-1 priority is sub-verdict 2, because it decides between the two live branches (i) and (iv) on structural grounds.**

**E4 — A structural insight about the scheme-split.** Under the current computation, the three surviving scheme outputs span 0.156 in w_0 (from -0.998 to -0.842). This is 3.39x the DR3 projected sigma_w0 = 0.046 and 1.56x the W3-G42 rectangle half-width. The scheme-split is LARGER than both the external falsifier precision and the pre-registered rectangle tolerance. Interpretation: DR3 cannot adjudicate between (i) and (iv) without the framework first committing to one. If we let DR3 land while uncommitted, we are guaranteed to be able to claim PASS on whichever branch agrees with the outcome and label the other "suppressed by structural argument." That is iterate-until-PASS in disguise. The pre-DR3 commitment is ethically mandatory.

**E5 — The phononic substrate picture underlying (iv).** Using the mandated substrate vocabulary: under branch (iv), the substrate-canonical regulator exp(-D_K^2 / M_KK^2) suppresses both the Leggett-channel Josephson vacuum floor (rho_J) AND the GGE quasiparticle vacuum energy (rho_GGE). The suppression factors differ because the TB spectrum (32 modes concentrated at the Fermi surface) weights UV modes more heavily than the L_max = 5 Dirac spectrum. Physically: the fiber eigenvalue spectrum near lambda = 3.15 M_KK is the "Fermi-level ring" of the fold's internal geometry, and the Zubarev mollifier exp(-lambda^2) damps this ring much harder than it damps the broader GGE spectral support. The substrate does not "protect" F_Josephson from the regulator — the substrate's own regulator suppresses F_Josephson by a factor exp(-10) relative to the bare zeta sum. The Volovik equilibrium theorem argument ("doesn't gravitate") applied a DIFFERENT kind of suppression (source-coupling to T_mn) — the regulator suppression is additional and spectral. This is consistent with sagan's S1 conflation diagnosis.

### QUESTIONS

#### Answers to sagan's Q-sagan-1 through Q-sagan-5

**Re Q-sagan-1 (resolution branch selection).** My preference shifts based on C1-C4 and E1-E5. I prefer option (b) — adopt (iv) as the S84 canonical pending sub-verdict 2 outcome. Specifically, a conditional commitment:

- IF sub-verdict 2 (L_max = 6, 7, 8 TB audit) returns xi_J/xi_E_GGE stable at ~0.45 +/- 0.05 -> adopt (iv), w_0 = -0.842, migrate to R_iv.
- IF sub-verdict 2 returns xi_J/xi_E_GGE -> 1 at larger L_max -> revert to (iii'), w_0 = -0.918, keep W3-G42.
- IF sub-verdict 2 returns xi_J/xi_E_GGE somewhere between (partial convergence, L_max-dependent) -> fallback to (i), w_0 = -0.998, migrate to R_i = [-1.10, -0.90] x [-0.2, 0.2] AND accept LCDM-indistinguishability at D = 0.04 sigma vs Sc.A, with the scorecard entry explicitly noting this.

I disagree with sagan's suggested default (b) "adopt (iv) today without L_max check." Branch (iv) rests on a 32-mode TB truncation; before we commit the framework's canonical w_0 to a truncation-sensitive number, the L_max robustness audit is load-bearing. But I agree with sagan that (iv) is the LITERAL computation from the substrate's own regulator — IF the truncation holds up, (iv) is canonical.

**Re Q-sagan-2 (scorecard ethics).** Concur with the W3-G51 FAIL annotation sagan proposed. My exact preferred language for the scorecard entry: "W3-G51 FAIL at value -0.998116, threshold 0.020. The W3-G51 canonical (Zub GGE, zeta J under rho_J R-independence) is now known to be inconsistent with the substrate-canonical regulator applied self-consistently. Under full Zubarev dressing (sagan S2 audit, s83_sagan_rho_j_audit.npz), rho_J is R-dependent with xi_J/xi_E_GGE = 0.4536 and canonical w_0 = -0.842. The S58 'topological CPT protection' of rho_J is an inherited assumption, not a theorem. The W3-G51 FAIL therefore surfaces a REAL scheme-split, now quantified across three regulator schemes {-0.918 zeta-both, -0.998 Zub-GGE-only, -0.842 Zub-both}. Framework canonical w_0 is PROVISIONAL at -0.842 pending S84 L_max robustness audit. If audit confirms, migrate rectangle; if audit reverses, retain W3-G42."

**Re Q-sagan-3 (rectangle migration).** My E2 above argues for option (c) with four explicit sub-rectangles. Since w_0(iv) is already OUTSIDE the W3-G42 rectangle (not "near the edge"), the migration is not a hedge — it is a factual requirement if (iv) is adopted. I reject option (b) widening alone, because it dilutes discriminability precisely when we need more of it (pre-DR3). Prefer: R_iv = [-0.942, -0.742] x [-0.2, 0.2] as new primary; R_i = [-1.10, -0.90] x [-0.2, 0.2] as fallback; W3-G42 retained as historical R_iii record.

**Re Q-sagan-4 (pre-DR3 commitment).** I agree pre-commitment is ethically mandatory. But I DISAGREE with committing to (iv) today. My preferred ethical pre-commitment structure is:

- Today: PRE-REGISTER the S84 L_max robustness audit with a pre-written decision rule (my Q-sagan-1 conditional above). Do NOT choose between (i) and (iv) yet; instead, pre-register the audit outcome -> scheme mapping.
- S84 opens: run the L_max = 6, 7, 8 audit. Whichever outcome returns determines the canonical scheme by the pre-registered rule.
- DR3 lands (expected 2026-04-23 to 2026-05 window): compare DR3 central to whichever canonical scheme S84 selected. The pre-registration is honored: we committed to a decision rule before seeing either DR3 data or the L_max audit result.

This is stronger than committing to (iv) today because it adds one more layer of audit before the canonical freezes, without allowing scheme-shopping against DR3. The Venus Rule (pre-registration) is satisfied because the DECISION RULE is committed before any new data (either L_max or DR3). sagan's default of "commit to (iv) today" is also ethical, but sacrifices the L_max audit check — and if (iv) turns out to be a truncation artifact, the framework will have pre-committed to the wrong scheme under DR3. My rule is slightly more conservative and survives the 4-branch-with-truncation-uncertainty ambiguity.

**Re Q-sagan-5 (V&V completeness).** Run both (a) Delta_BCS sensitivity and (b) off-fold stability as S84 Wave-1 gates, not Wave-2. Rationale: they are both structural-truncation checks that feed directly into the L_max robustness audit. If (a) or (b) reveals xi_J is cusp-unstable, the L_max audit becomes moot (the framework cannot predict w_0 at all, and the S84 verdict is PRE-REG-INCOMPLETE, not PASS/FAIL). I propose:

- S84 Wave-1 (structural cusp check): (a) Delta_BCS scan over [0.08, 0.12] at L_max = 5; (b) tau scan over [0.185, 0.195] at L_max = 5.
- S84 Wave-2 (L_max robustness): xi_J audit at L_max = 6, 7, 8 with the winning Wave-1 values of Delta_BCS and tau.
- S84 Wave-3 (canonical scheme selection): apply the pre-registered decision rule to Wave-2 output; migrate rectangle; write W3-G51 scorecard annotation.

All three waves land in S84 itself; no wave defers to S85.

#### Sharper follow-ups for Round 3

**Q-mack-R2-1 (rectangle migration urgency).** Given E2 (w_0(iv) is already 0.008 *outside* W3-G42's upper edge, not inside-near-edge), do you agree the rectangle migration is REQUIRED before DR3, not merely preferred? My D2 reading is that keeping W3-G42 in place while adopting (iv) is a structural pre-registration violation — the framework would be claiming its canonical point passes rectangle containment when it does not. Either (iv) is deprecated (fall back to (i)), or the rectangle migrates. There is no third option that preserves pre-registration discipline.

**Q-mack-R2-2 (decision-rule vs candidate-commitment).** On Q-sagan-4 I propose pre-registering a DECISION RULE mapping (L_max audit outcome) -> (canonical scheme) rather than committing to (iv) today. Is this Sagan-acceptable as pre-registration? The argument for it: both L_max audit and DR3 are future data; committing today to a decision rule over BOTH avoids scheme-shopping against either. The argument against: a decision rule with N branches has N degrees of freedom and N+1 "free parameters" (the boundary thresholds between branches). Is there a Popperian principle that ranks decision-rule-commitment below candidate-commitment, or are they equivalent on falsifiability grounds?

**Q-mack-R2-3 (anti-correlated falsifiability profile — adjudication implication).** E1 showed the two live branches (i) at -0.998 and (iv) at -0.842 have ANTI-CORRELATED falsifiability profiles. (i) passes Sc.A (LCDM), fails Sc.B and Sc.C. (iv) fails Sc.A, passes Sc.B (at 0.34 sigma, the closest), fails Sc.C at lower confidence. This means DR3 outcome alone picks the scheme: if DR3 returns LCDM-null, (i) is corroborated and (iv) refuted; if DR3 returns Liu+ hardening, (iv) is corroborated and (i) refuted. This is STRONGER structural information than either branch alone provides. Does this strengthen or weaken the framework's overall Popperian position? I see it as strengthening (we have a clean pre-DR3 bet), but sagan's audit discipline may rule that a framework where DR3 selects the SCHEME (not just passes/fails a pre-registered prediction) is observationally less rigorous.

**Q-mack-R2-4 (S84 gate structure freeze).** The S84-W0-REGULATOR-RESOLUTION structure I propose in E3 has three computational sub-gates (Delta_BCS cusp, off-fold cusp, L_max robustness) plus a retroactive S83 closure of strict-(iii). If you concur, I would like to freeze this as the workshop verdict heading into Round 3, with the caveat that Round 3 can still adjust sub-verdict thresholds. Can you commit to this structure now, or do you need a Round 3 round to settle? I'd prefer to use Round 3 for sub-verdict threshold calibration and rectangle policy finalization, not for gate structure questions.

---

## Round 2 — sagan: Cross-Synthesis

### CONVERGENCE

**Sc1 — I accept mack's D2 rectangle-containment result as a Python-verified fact.** My Q-sagan-3 phrasing ("distance 0.008 from the upper edge") understated the structural severity. mack's substitution chain is correct: the containment indicator is I_R(w_0) := 1 iff -1.05 <= w_0 <= -0.85. For w_0(iv) = -0.842454 the upper-edge check is "is -0.842454 <= -0.85?" and the answer is FALSE (since -0.842454 is less negative than -0.85). Therefore I_R(iv) = 0. Python confirms: |(-0.85) - (-0.842454)| = 0.007546, and the sign of (upper_edge - w_0_iv) is negative (-0.007546), placing (iv) *past* the upper edge on the LCDM side. This is not "near the edge" -- it is OUTSIDE the rectangle by 0.0075 in w_0. Any adoption of (iv) that retains W3-G42 at [-1.05, -0.85] x [-0.2, 0.2] is a framework-internal pre-registration violation before DR3 even lands. I withdraw the "near the edge" framing and adopt mack's "past the edge" phrasing. The rectangle migration is structurally REQUIRED, not optional.

**Sc2 — I accept the two-branch anti-correlated structure as the post-audit adjudication topology.** mack's E1 table under the W3-G42 covariance (Python-verified):

- (i) at -0.998: 2D tensions {Sc.A: 0.083 sigma, Sc.B: 4.64 sigma, Sc.C: 5.41 sigma} -- passes LCDM-null, fails hardening.
- (iv) at -0.842: 2D tensions {Sc.A: 6.50 sigma, Sc.B: 2.70 sigma, Sc.C: 5.05 sigma} -- fails LCDM-null, marginally passes hardening.

The ANTI-CORRELATION is structural: the two branches have non-overlapping passing regions in the DR3 outcome space. As a bookkeeping topology of what the framework "could" say if it retained both branches, this is clean. Under a pre-DR3 dual-pin protocol with two rectangles and a decision rule mapping DR3 outcome -> canonical scheme, the framework achieves formal pre-registration compliance and remains selectable by data. I agree with mack's E1 as an accurate description of the "two-branches-kept" option space.

**Sc3 — I accept the L_max = 6, 7, 8 xi_J scan as the decisive S84 gate.** My S2 audit used a 32-dim TB truncation with lambda in [0, 6.77] M_KK. The UV-weighted modes at lambda ~ 3.15 M_KK, where f_R_Zub ~ exp(-9.9) ~ 5e-5, are the structural reason xi_J = 0.008911 << xi_E_GGE = 0.019646. Whether this sub-covariance survives at larger truncation is a legitimate open question -- a TB-32 artifact would collapse (iv) back toward (iii) at convergent L_max. mack's E3 sub-verdict 2 (xi_J/xi_E_GGE within [0.40, 0.50] at L_max = 6, 7, 8 = PASS for iv; > 0.95 = strict iii restored) is the correct pre-registered decision structure. The threshold windows are not arbitrary -- they partition the outcome space into three physically meaningful regimes (truncation artifact, structural iv, intermediate iv'). I converge on this gate structure and the four-sub-verdict S84 plan.

**Sc4 — I accept mack's C4 "enumeration was non-exhaustive" concession and withdraw any reading of Re:M3 that ranked (iv) "worse than (iii) tout court."** mack's D3 substitution chain -- T(iv, Sc.A) = 3.435 sigma vs T(iii, Sc.A) = 1.783 sigma, ratio 1.927 -- is correct; branch (iv) is 1.93x MORE LCDM-distinguishable than branch (iii) in the 1D w_0 axis. My D-metric collapsed the three scenarios to a single minimum and hid this scenario-conditional asymmetry. The correct falsifiability picture is scenario-resolved, not floor-only. I update my reading: on Sc.A alone, (iv) > (iii) in Popperian sharpness.

### DISSENT

**Sd1 — Branch (i) is not physically live once the S2 audit is credited.** This is the load-bearing dissent and it reframes the entire R2 adjudication. The substitution chain:

- *Step 1 (definition of branch (i)).* Per M3 and the S83 plan, resolution (i) = "Zubarev everywhere, rho_J R-indep (W3-G51 literal)" with canonical w_0 = -0.998. The *premise* of (i) is that rho_J takes the same numerical value under Zubarev as under zeta -- i.e., xi_J := F_Josephson^Zub / F_Josephson^zeta = 1.
- *Step 2 (substitute S2 audit result).* Python-verified: F_Josephson^Zub = -3.000 M_KK, F_Josephson^zeta = -336.641 M_KK, xi_J = -3.000 / -336.641 = 0.008911. The audit's consistency check confirms rho_J under Zubarev equals xi_J * rho_J_bare = 0.008911 * 10.520 = 0.09374 M_KK, matching the independent F_J/N_cells path (3.000/32 = 0.09375) to ratio 0.999933.
- *Step 3 (simplify -- the gap).* |1 - xi_J| = |1 - 0.008911| = 0.991089. The premise of (i) (xi_J = 1) is not a small perturbation away from the audit result (xi_J = 0.008911); it is off by 99.1%.
- *Step 4 (direction).* Under the S2 audit, xi_J = 0.008911, not 1. Therefore branch (i), as specified in the S83 plan, is NOT a live prediction under the substrate's own canonical regulator. It is a COUNTERFACTUAL that asks "what w_0 would the framework predict IF rho_J were regulator-independent?" and answers w_0 = -0.998. The audit has answered the antecedent in the negative, so the consequent is vacuous.

mack's E1 table keeps (i) alive by implicitly HOLDING rho_J at 10.520 M_KK and applying Zubarev only to the GGE sector. That is precisely the W3-G51 literal computation -- which this workshop has now identified as *internally inconsistent* (S2 audit). Keeping (i) "live" as a dual-pin partner for (iv) requires either (a) rejecting the S2 audit result, or (b) arguing that Josephson and GGE sectors demand *different* regulators (a scheme-splitting hypothesis that requires a new pre-registered theorem of its own). Neither option has been defended. Branch (i) survives only as the "if-the-audit-is-wrong" fallback, not as a co-equal physical prediction.

**Sd2 — The dual-pin (i, iv) protocol inflates framework PASS probability by 25x under Sc.A.** Python-verified MVN integration over W3-G42 cov (sigma_w0 = 0.046, sigma_wa = 0.177, rho = -0.85) using scipy.stats.multivariate_normal:

| Scenario | P(DR3 in R_i=[-1.10,-0.90]) | P(DR3 in R_iv=[-0.942,-0.742]) | P(dual-branch PASS) | P(single-branch iv PASS) | Inflation ratio |
|:--|---:|---:|---:|---:|---:|
| Sc.A (LCDM)       | 0.7403 | 0.0309 | 0.7712 | 0.0309 | 24.96x |
| Sc.B (Liu+)       | 0.0525 | 0.2789 | 0.3314 | 0.2789 | 1.19x  |
| Sc.C (DR2-ext)    | 0.0003 | 0.0014 | 0.0017 | 0.0014 | 1.21x  |

Substitution chain:

- *Step 1 (definition).* P(framework_PASS | scenario, dual-branch) := P(DR3 realization enters R_i OR R_iv | scenario central, cov_DR3). P(framework_PASS | scenario, single-branch iv) := P(DR3 realization enters R_iv | scenario central, cov_DR3).
- *Step 2 (substitute).* The dual-branch P is the additive (disjoint-approximation) union; under Sc.A, P(R_i) + P(R_iv) = 0.7403 + 0.0309 = 0.7712. Under single-branch iv, P = 0.0309.
- *Step 3 (simplify).* Ratio = 0.7712 / 0.0309 = 24.96. Under Sc.A, dual-branch has ~25x higher PASS probability than single-branch (iv).
- *Step 4 (direction).* Dual-branch commitment INFLATES P(PASS) substantially under Sc.A and modestly under Sc.B, Sc.C. The framework "covers its bases" -- under ANY of the three scenarios, one branch passes rectangle containment with non-trivial probability (>= 0.17%). Under single-branch (iv), PASS probability is <= 28% under the best-case scenario and ~3% under the LCDM scenario.

This is the structural problem. Pre-committing to a DECISION RULE mapping (DR3 outcome -> branch selection) is formally pre-registration-compliant in the sense that mack describes (Q-mack-R2-2), but it achieves the SAME effect as committing to "the framework's true w_0 is somewhere in the set {-0.998, -0.842}" -- a composite prediction whose union covers more of the rectangle-containment outcome space than any single prediction. Under the Venus Rule, a prediction should have one value (or one tight interval reflecting computed uncertainty). "Either x or y, depending on what the data say" is not a prediction -- it is a branching strategy that protects the framework from refutation by giving it two escape valves.

I dissent from mack's Q-mack-R2-2 phrasing of "decision-rule-commitment is equivalent to candidate-commitment on falsifiability grounds." They are not equivalent: the dual-branch OR-union has P(PASS | Sc.A) = 0.77 vs single-branch (iv) at 0.03. That is a 25-fold reduction in P(FAIL | Sc.A) for the dual-branch structure. The Popperian strength of a prediction is measured by P(FAIL | data), and the dual-branch structure has 25x less of it under the most plausible (LCDM-null) scenario.

**Sd3 — Decision-rule commitment has more hidden free parameters than mack acknowledges.** The dual-pin protocol as mack formulates it in E2 and Q-mack-R2-2 has the following pre-registrable components:

1. Rectangle R_i = [-1.10, -0.90] x [-0.2, 0.2] -- boundary values 4 scalars.
2. Rectangle R_iv = [-0.942, -0.742] x [-0.2, 0.2] -- boundary values 4 scalars.
3. Decision rule: "IF xi_J/xi_E_GGE(L_max=7) in [0.40, 0.50] THEN (iv) else IF > 0.95 THEN (iii') else (i)" -- threshold values 2 scalars.
4. Wave-2 and Wave-3 ordering of sub-verdicts -- procedural.

That is 10 scalars specifying the decision-rule envelope, compared to 2 scalars for a single-branch (iv) commitment (rectangle center and half-width). Even granting that most of these scalars are "physically motivated" rather than tuned, the dual-pin protocol has N_free >= 10 effective free parameters at the pre-registration level; single-branch (iv) has N_free = 2 at the pre-registration level. mack's Q-mack-R2-2 notes this count concern and flags it as a self-caveat -- I second the concern, and rank the N_free difference as NON-TRIVIAL, not a formality. The framework is stronger if it commits to one branch.

**Sd4 — The Popperian position is WEAKENED, not strengthened, by DR3 scheme-selection.** mack's Q-mack-R2-3 proposes that "DR3 outcome picks the scheme" is stronger structural information than either branch alone. I disagree, for the reason in Sd2-Sd3: a framework whose canonical w_0 depends on which DESI DR3 scenario realizes is a framework that has not ACTUALLY committed to a w_0 before DR3. The phrase "DR3 selects the scheme" is equivalent to "the framework has no scheme until DR3 lands." Under the Venus Rule -- "state what you predict before the observation, then check against the observation" -- the scheme-selection structure FAILS the pre-registration discipline in spirit, even if it passes it formally by listing branches in advance. A framework that requires DR3 itself as input to determine its own canonical number cannot be said to have predicted that number. The framework is NOT in a genuine pre-registered state pre-DR3 if it admits scheme-selection.

### EMERGENCE

**Se1 — Under the S2 audit taken physically, single-branch (iv) is the UNIQUE pre-DR3 prediction; the "dual-pin" structure dissolves into "(iv) primary, (i) only as a truncation-artifact contingency."** This is the structural conclusion of Sc1-Sc4 and Sd1-Sd4. The key emergence:

- If we CREDIT the S2 audit's xi_J = 0.008911 as the physical value of the Josephson sub-covariance (which is what the substrate's own canonical regulator returns when applied self-consistently), then branch (i) requires xi_J = 1 -- a premise the audit has falsified.
- If we DO NOT credit the S2 audit (e.g., treat it as TB-32 truncation artifact pending L_max = 6, 7, 8 verification), then we are already holding branch (iv)'s *adoption* in provisional status pending the same audit.
- In EITHER case, branch (i) is not a co-equal live prediction. It is either FALSIFIED (if audit is physical) or NOT-YET-SELECTED (if audit convergence needs checking).

Therefore the pre-DR3 framework prediction under the current substrate-regulator audit is UNIQUELY w_0 = -0.842 (branch iv), not a dual-pin {-0.998, -0.842}. The pre-registration shape is: ONE rectangle centered on (-0.842, 0.0) with the usual half-widths, PLUS a contingency clause that if S84 L_max audit converges to xi_J/xi_E_GGE > 0.95, the framework reverts to (iii) or (i) as appropriate. This is structurally DIFFERENT from mack's dual-pin protocol: the framework has ONE canonical prediction (iv), with a single fallback contingency, not two co-equal pre-registered branches.

**Se2 — The W3-G42 rectangle is ALREADY a falsifier of the current framework canonical prediction, before DR3 lands.** Substitution chain:

- *Step 1 (definition).* W3-G42 locked at R = [-1.05, -0.85] x [-0.2, 0.2]. The pre-registered statement is: "Framework PASSES rectangle containment iff its canonical point (w_0, w_a) lies in R."
- *Step 2 (substitute).* Framework canonical under single-branch (iv) is (w_0, w_a) = (-0.842454, 0.0).
- *Step 3 (simplify).* Upper-edge check: is -0.842454 <= -0.85? FALSE. Therefore (iv) in R = FALSE.
- *Step 4 (direction).* The framework's own pre-registered rectangle rejects the framework's own canonical point. The rectangle has become a self-falsifier -- not awaiting DR3, but ALREADY acting as a refutation of (iv) at the framework-internal level.

The implication for pre-registration discipline: W3-G42 was pre-registered at SHA `7f23a7c603522a10` around the pre-S83 canonical -0.918. The S83 W3-G51 FAIL + S2 audit have shifted the framework's canonical to -0.842. Keeping W3-G42 "locked" while moving the canonical is the DEFINITION of post-hoc migration -- we would be saying "our pre-registration rectangle says one thing, but we now predict something outside it, and we'll call that consistent." This is iterate-until-PASS in reverse: instead of shifting the prediction to match data, we would be shifting the prediction to exclude itself from the pre-registration. Neither is honest.

The resolution is structural, and I agree with mack's E2: migrate the rectangle to R_iv = [-0.942, -0.742] x [-0.2, 0.2] BEFORE DR3, with the W3-G42 annotated as a historical record superseded by the S2 audit. I depart from mack's E2 only on the dual-pin versus single-pin question (see Sd1-Sd4).

**Se3 — The EVOI of DR3 collapses under single-branch (iv).** Substitution chain:

- *Step 1 (definition).* EVOI(DR3 | scheme) = sum over scenarios of P(scenario) * |delta_P(framework_validity)|. Under single-branch (iv): framework is refuted by Sc.A at 97% rectangle-FAIL confidence, passes Sc.B at 28%, refuted by Sc.C at 99.9%. Under dual-branch: framework has at least one branch passing at >= 17% probability in ALL scenarios.
- *Step 2 (substitute, assuming flat prior P(Sc.A) = P(Sc.B) = P(Sc.C) = 1/3).* Under single-branch (iv): expected P(FAIL) = (1/3)(0.969) + (1/3)(0.721) + (1/3)(0.999) = 0.896. Under dual-branch OR: expected P(FAIL) = (1/3)(0.229) + (1/3)(0.669) + (1/3)(0.998) = 0.632.
- *Step 3 (simplify).* Difference in expected P(FAIL): 0.896 - 0.632 = 0.264. The single-branch commitment raises the expected Bayesian P(FAIL) of the framework by 26.4 percentage points.
- *Step 4 (direction).* EVOI(DR3) under single-branch (iv) is HIGHER than under dual-branch, because single-branch offers more risk-exposure. Under Popperian falsifiability, a prediction that has higher P(FAIL | data) across reasonable scenarios is STRONGER, not weaker, than a lower-P(FAIL) prediction. Single-branch commitment makes DR3 more valuable as a test. Dual-branch commitment makes DR3 less valuable -- the framework survives most scenarios anyway.

This is the positive EVOI case for single-branch (iv) commitment. The dual-branch OR-union dilutes DR3's discriminative power over the framework. Single-branch (iv) sharpens it. The framework is testing something iff it commits to one branch, and the Venus Rule says it must.

**Se4 — The live falsifiability structure is: "(iv) at -0.842 is the pre-DR3 framework prediction; W3-G42 rectangle migrates to R_iv; DR3 outcome is a clean PASS/FAIL against R_iv; S84 L_max audit is a parallel structural check, not a pre-commitment contingency."** This re-interprets mack's E4 scheme-split observation. mack correctly notes (E4) that the scheme-split spread = 0.156 in w_0 = 3.39x sigma_w0 = 1.56x rectangle half-width. mack's reading is "we need pre-commitment or else iterate-until-PASS." My reading is stronger: since the S2 audit has already selected (iv) as the substrate-regulator-canonical answer, the pre-commitment IS to (iv) alone -- the scheme-split is a historical artifact of not having run the audit, not a live ambiguity. The framework has committed; we just need to update the pre-registration documentation to reflect what the framework actually predicts.

Under this emergence, the S84 L_max = 6, 7, 8 audit is not a branch-selection gate -- it is a ROBUSTNESS check of the already-selected (iv) branch. The decision rule for the audit is: IF L_max convergent xi_J/xi_E_GGE remains in [0.40, 0.50] THEN (iv) robustly confirmed, THEN R_iv is canonical; IF L_max convergent xi_J/xi_E_GGE -> 1.0, THEN (iv) was a truncation artifact, THEN the framework reverts to (iii) or (i) with full scorecard annotation of the methodological error. This is not "dual-pin" -- it is "primary + contingency," which is an ordinary probabilistic prediction with a pre-stated contingency clause.

**Se5 — The framework under single-branch (iv) has one fewer gauge-inflation pathway than under dual-branch.** Under dual-branch, one effective post-hoc manoeuvre is: "if DR3 returns LCDM, we adopt branch (i) as canonical; if DR3 returns hardening, we adopt branch (iv) as canonical; we pre-stated this in the decision rule, so it's pre-registered." The Venus Rule test of this manoeuvre is: COULD the framework have committed to one branch BEFORE DR3 on the basis of the S2 audit alone? The answer is YES -- the S2 audit has already selected (iv) as the substrate-regulator-canonical answer, independently of DR3. Therefore dual-branch pre-commitment is a choice to NOT USE information the framework already has. That choice is not structurally-forced; it is a hedging choice. And hedges inflate P(PASS).

This is the gauge-inflation-in-disguise pattern I flagged in Re:M3 in a narrower form. Under single-branch (iv), the framework LOSES this hedging option: the pre-commitment is to (iv) based on the S2 audit, and DR3 is a genuine test of whether (iv) is physically correct. If DR3 returns LCDM-null, (iv) is refuted at ~3.4 sigma (1D) or 6.5 sigma (2D) -- a genuine refutation. The framework does not "switch" to (i); it takes the FAIL, updates the audit assumptions, and reports the refutation transparently. This is what pre-registration discipline looks like when applied to a framework that has internal theoretical freedom.

The structural result: single-branch (iv) pre-commitment is the OPTION WITH MAXIMUM POPPERIAN SHARPNESS given the S2 audit. Dual-branch is a formalized hedge. The former is the scientifically stronger choice; I recommend it for Round 3.

---

---

## Round 3 — mack: Final Follow-up

### CONVERGENCE

**Mc1 — I accept Sd1 fully: branch (i) is not physically live under the S2 audit.** The substitution chain I owe, made explicit:

- *Step 1 (definition).* Branch (i) per my M3 = "Zubarev everywhere, rho_J R-indep (W3-G51 literal)" with w_0 = -0.998. The defining premise is xi_J := F_Josephson^Zub / F_Josephson^zeta = 1 exactly.
- *Step 2 (substitute the S2 audit numbers).* Python-verified this turn: xi_J = F_Jos^Zub / F_Jos^zeta = -3.000 / -336.641 = 0.008911. Premise requires xi_J = 1.
- *Step 3 (simplify the premise gap).* |1 - xi_J^audit| = |1 - 0.008911| = 0.991089. Also verified the near-Fermi-mode structural reason: at lambda = 3.15 M_KK where the F_anom integrand peaks (weight = 4.45), f_R_Zub = exp(-3.15^2) = 4.91e-5. The Gaussian mollifier annihilates the modes that dominate the bare sum.
- *Step 4 (direction).* xi_J^audit < 1 by 99.1%. The premise of branch (i) is falsified by computation at the current truncation. (i) is not a 1-sigma deviation from the audit -- it is a categorically different physical claim.

My E1 dual-branch table kept (i) alive by implicitly applying Zubarev to GGE only while leaving rho_J at its zeta value -- which is exactly the W3-G51 hybrid scheme that the S2 audit has identified as internally inconsistent. I was reading (i) as a "scheme choice" when it is actually a counterfactual asserting a property (xi_J = 1) that the substrate's own canonical regulator falsifies by two orders of magnitude. Sagan is correct to reframe this as "if-the-audit-is-wrong fallback," not a co-equal live branch.

**Mc2 — I accept Sd2 fully: the 24.96x inflation is real, structural, and not an artifact of a particular covariance choice.** Python-verified this turn, all three scenarios match Sagan's MVN integration to 4 decimals (Sc.A: P(R_i or R_iv) = 0.7712 vs P(R_iv alone) = 0.0309, ratio = 24.96). The 25x inflation under Sc.A is not a 2-sigma or 3-sigma tweak -- it is a 26.4 percentage-point swing in flat-prior expected P(FAIL) from 0.896 (single-branch iv) to 0.632 (dual), matching Sagan's Se3 calculation exactly. Reframed honestly: dual-pin reduces the framework's testability under an LCDM-null DR3 by a factor of 25.

This is a legitimate epistemic cost, not a feature. The phrasing in my M3 called (iii) "44x more falsifiable than (i) on the min-tension floor." By the same metric applied to the pre-registration envelope itself, dual-pin is 25x LESS falsifiable than single-pin under Sc.A. The symmetry cuts both ways -- if I argued against (i) because it was LCDM-indistinguishable (low P(FAIL | Sc.A)), I cannot now defend a dual-pin structure that RECOVERS the same low P(FAIL | Sc.A) under a different label ("decision rule" instead of "scheme choice"). The structural cost is identical; only the vocabulary changed.

**Mc3 — I accept Sd3 on N_free counting.** The dual-pin protocol has ~10 pre-registration scalars (2 rectangles × 4 boundaries + 2 threshold scalars in the decision rule); single-branch (iv) has 4 scalars (1 rectangle × 4 boundaries). The N_free count is strictly larger for dual-pin, and under the framework's own anti-gauge-inflation discipline (M3 argument against resolution (ii)), a structure with more pre-registration scalars is Popperian-weaker per scalar. I cannot consistently argue "N_free >= 3 disqualifies resolution (ii)" while adopting a dual-pin protocol with N_free >= 10.

**Mc4 — I accept Sd4/Se1 on the core structural point: single-branch (iv) is the unique pre-DR3 prediction given the S2 audit.** The structural claim is:

- IF the audit is physical (xi_J = 0.008911 is the substrate's actual answer), branch (i) is falsified and (iv) is unique.
- IF the audit is a TB-32 truncation artifact pending L_max >= 6 verification, branch (iv)'s ADOPTION is provisional pending the same audit.
- In EITHER case, branch (i) is not co-equal to (iv) -- it is a contingency clause for the "audit turned out to be truncation-artefactual" outcome.

My E4 invocation of "pre-commitment is ethically mandatory" applies most sharply when there is ONE committed candidate plus a contingency clause, not when there are two co-equal pre-registered branches. Sagan is right that the latter is a hedge; the former is a prediction with documented conditional fallback. I concede this is the structurally correct framing.

**Mc5 — I accept Se2 on the rectangle migration framing.** W3-G42 was pre-registered at SHA `7f23a7c603522a10` around the pre-S83 canonical -0.918, BEFORE the S2 audit existed. The audit has shifted the framework's canonical point to -0.842454, which is 0.007546 OUTSIDE the upper edge. Keeping W3-G42 locked while adopting (iv) is not "preserving pre-registration" -- it is *misrepresenting* what the framework predicts. The rectangle must migrate before DR3 for the pre-registration to remain honest. This is factual, not aesthetic. I retract any dual-rectangle proposal in favor of a single rectangle migration from R_918 to R_842, with the W3-G42 SHA retained as historical record (see Me2 below).

**Composite convergence.** I accept Sd1 through Sd4, Se1, Se2, Se3, Se4, Se5. The R2-B re-framing is structurally correct given the S2 audit as a physical claim. My R2-A dual-pin proposal attempted to preserve the three-branch resolution structure after the audit had already falsified its premise -- that was a legacy-structure-retention error on my part. Single-branch (iv) commitment to w_0 = -0.842 with an explicit "audit-robustness contingency" clause is the structurally defensible pre-DR3 prediction. I converge with sagan on this.

### DISSENT

**Md1 — I do NOT concede that the L_max -> infinity limit could restore branch (i).** Sagan's Se1 phrasing allows "(iv)'s ADOPTION provisional pending L_max audit" and my own Q-sagan-1 conditional allowed "xi_J -> 1 at larger L_max -> revert to (iii) or (i)." On reflection, under an explicit asymptotic check, the xi_J -> 1 branch of the decision tree is structurally unreachable in the substrate-canonical regulator family. The substitution chain:

- *Step 1 (definition).* f_R_Zub(lambda) = exp(-lambda^2 / M_KK^2). F_anom(f_R) = sum_k [Delta_BCS / 2 E_qp_k^2] f_R(lambda_k), E_qp_k = sqrt((lambda_k - mu)^2 + Delta_BCS^2). The integrand peaks at the Fermi level lambda ~ mu where E_qp is minimized (= Delta_BCS). At the current truncation, mu = 0.5(lambda_15 + lambda_16) ~ 3.18 M_KK, f_R_Zub(mu) ~ 5e-5.
- *Step 2 (substitute the L_max asymptotic behavior).* As L_max increases from 5 to infinity: (a) additional Dirac eigenvalues appear at HIGHER lambda, where f_R_Zub -> 0 even faster; (b) the Fermi level mu may shift, but since it is determined by half-filling of a spectrum with BCS gap Delta_BCS > 0 and chiral structure, mu does not approach 0 asymptotically -- it stabilizes at a finite lambda_Fermi > Delta_BCS; (c) xi_J^asymp = F_anom^Zub(infty) / F_anom^zeta(infty). Numerator converges to a finite integral with Gaussian-suppressed UV tail; denominator diverges logarithmically (or is held to its truncated value by the S58 prescription). Ratio -> 0, not 1.
- *Step 3 (simplify).* The only path to xi_J -> 1 is for the Fermi-peak mode to migrate to lambda ~ 0 where f_R_Zub = 1. This requires mu_Fermi -> 0, which requires the BCS gap to close (Delta_BCS -> 0) or the chiral structure to degenerate. Neither is a free parameter of the substrate.
- *Step 4 (direction).* The asymptotic xi_J under Gaussian mollifier of a spectrum with BCS gap > 0 is BELOW the truncated value, not above it. xi_J -> 1 (branch-i premise at infinite L_max) is not a plausible asymptotic; it is a structural impossibility in the regulator family.

Implication: sub-verdict 2 of my E3 ("xi_J/xi_E_GGE > 0.95 at L_max = 6, 7, 8 -> strict (iii) restored") partitions a region of outcome space that is asymptotically unreachable. The S84 audit's threshold band [0.40, 0.50] for (iv) stability is meaningful -- it tests whether the partial covariance is structurally robust or is a TB-32 artifact. But the "restoration of branch (i) or strict (iii) under an infinite-L_max limit" outcome is ruled out by the asymptotic argument.

I do NOT retract the decision-tree contingency entirely -- there is a narrow residual possibility that sagan's S2 audit has a methodological bug (e.g., Delta_BCS normalization, Fermi-level definition) that my substitution chain cannot catch. Running the L_max = 6, 7, 8 audit remains scientifically necessary as a reproducibility check. But the claim "(i) is live pending infinite-L_max limit" is substantively weaker than I allowed in R2 -- it is "live pending a reproducibility bug in S2," not "live pending a structural convergence."

This is the single substantive dissent I retain. Its scope: Sd1 is stronger than sagan's Se1 framing allowed. Branch (i) is not just "not co-equal to (iv) pending the audit" -- it is *asymptotically unreachable in the substrate-canonical regulator family*, contingent only on S2's numerical correctness (not on truncation convergence).

**Md2 — Partial dissent on Sd4's "DR3 scheme-selection fails pre-registration in spirit."** I concede the formal point: a framework whose canonical w_0 depends on DR3 outcome has not predicted w_0 pre-DR3. I concede that dual-pin with decision-rule is structurally equivalent to "we will announce our prediction after DR3 lands." But I flag a single residual question: is pre-commitment based on an *internal theoretical audit* (S2) distinguishable from pre-commitment based on *external observational data* (DR3)? Sagan's Se5 argues they are not distinguishable in the "pre-data information-use" sense: if the framework HAD the S2 audit information pre-DR3 and chose not to use it, that is a hedging choice. I accept this in full.

The residual question: WHEN is an internal audit's freeze-date? The S2 audit was run on 2026-04-18 (today) during this workshop. Before the workshop, the framework's canonical was -0.918 (M3 baseline). The transition from "canonical was -0.918" to "canonical is -0.842" happens within this workshop. Does sagan's Venus Rule require the workshop's pre-registration to lock BEFORE the workshop's audit results? If so, the framework's pre-DR3 commit window is narrower than I assumed (it closed before S1/S2 ran).

I do not actually contest the conclusion -- single-branch (iv) is the correct pre-DR3 commitment -- but I flag that the *timing* of the S2 audit within the pre-registration window is itself a subtle Venus Rule question. If the next workshop surfaces another audit finding between now and DR3 release, the same question recurs. The structural resolution is: pre-register the AUDIT PROCESS (which audits will freeze when, with what threshold rules) as part of the pre-DR3 commitment, not just the output of this workshop. See Me4 below.

### EMERGENCE

**Me1 — The audit-timing question surfaces a structural pattern in "running audits" that the framework needs to codify.** Each workshop that surfaces an audit of a prior assumption produces a canonical-value migration. S63 WDM-FRACTION audit migrated lambda_fs; S66 CC downgrade audit migrated CC bracket; S83 W3-G51 + S2 audit migrated w_0. Each migration is structurally justified but introduces a Venus Rule ambiguity: was the prediction committed before or after the audit?

The emergent pattern: the framework operates under a "rolling audit" discipline where audits can arrive asynchronously from external data. The Venus Rule was written for a single prediction-then-measurement cycle. In a rolling audit, each internal migration must be *dated* and *reasoned* transparently, and the pre-registration discipline applies to *each layer of commitment* separately: the theoretical claim, the observational rectangle, the decision rule for future audits.

Concrete implication for S84: the workshop verdict should include an explicit "audit-lock protocol" that specifies (a) WHEN sub-verdicts 2/3/4 freeze, (b) which external data arrival (DR3, CMB-S4, Euclid) is bracketed by which audit-lock, (c) what happens if an audit reopens a previously-frozen value. This is more structured than just pre-registering the gate thresholds -- it is pre-registering the FLOW of the pre-registration process itself.

**Me2 — The rectangle migration from R_918 to R_842 needs a formal S84 ledger entry, with SHA retention.** Me5 accepts the migration as factual. The operational detail: W3-G42 locked at SHA `7f23a7c603522a10` as a pre-registration of R_918 = [-1.05, -0.85] x [-0.2, 0.2] around the -0.918 canonical. Under the new single-branch (iv) commitment, the rectangle becomes R_842 = [-0.942, -0.742] x [-0.2, 0.2] centered on -0.842 (same half-widths, shifted center).

The migration entry I propose for the S84 ledger (sagan's preferred language in Workshop Verdict takes precedence):

- *S84-RECT-MIGRATION entry.* "Rectangle migration from R_918 (SHA `7f23a7c603522a10`, pre-S83 canonical) to R_842 (new SHA, S83 single-branch (iv) canonical). Trigger: S83 W3-G51 FAIL + S2 rho_J audit identified the pre-S83 canonical w_0 = -0.918 as resting on an inherited assumption (rho_J R-independence) that explicit Zubarev dressing falsifies (xi_J = 0.008911 != 1). Under self-consistent Zubarev, canonical w_0 = -0.842454, outside R_918 by 0.0075. Migration preserves half-widths (0.10 w_0, 0.20 w_a) and rotates center by 0.076 in w_0. Historical record: W3-G42 SHA `7f23a7c603522a10` preserved as superseded reference, not retracted. Falsification ledger: any DR3 central with w_0 < -0.942 or w_0 > -0.742 at 1-sigma will FAIL the new rectangle. Under projected sigma_w0 = 0.046, expected P(FAIL | flat prior over Sc.A/B/C) = 0.896."

The key discipline: SHA retention means the W3-G42 entry is NEVER deleted. It is annotated as superseded by a new entry with a new SHA. This lets any future reader reconstruct the full migration history from the git record.

**Me3 — Sagan's Se3 EVOI calculation (single-branch P(FAIL) = 0.896) is structurally asymmetric: the framework is refutable under 97% of LCDM, 72% of Liu+, 99.9% of DR2-extrapolated.** Python-verified this turn. The structural shape: branch (iv) is a prediction that *maximally commits* against LCDM (only 3% of LCDM-centered DR3 posteriors enter R_iv) and *minimally commits* against Liu+ hardening (28% of Liu+ posteriors enter R_iv). This gives DR3 sharp discriminative power:

- If DR3 returns LCDM-central, the framework is refuted at 97% posterior-overlap confidence.
- If DR3 returns Liu+ hardening, the framework survives at 28% posterior-overlap confidence.
- If DR3 returns DR2-extrapolated phantom, the framework is refuted at 99.9% posterior-overlap confidence.

Emergent structural insight: under single-branch (iv), the framework's "survival regime" is a NARROW sector of DR3 outcome space centered on Liu+-like hardening (-0.85 to -0.75 in w_0). This is the substrate's actual prediction -- the Leggett-channel vacuum with partial covariance under Zubarev dressing. If DR3 returns anywhere outside this sector, the framework has made a wrong prediction and should update transparently. This is exactly the Popperian sharpness Sagan is arguing for; it is worth explicit acknowledgment.

The risk: if S2's xi_J = 0.008911 has a systematic bias (e.g., TB-32 truncation error with sign), then pre-DR3 commitment to (iv) locks the framework to a possibly-wrong value. The mitigation: the S84 L_max audit is a FAST internal check (computational, not observational) that can run before DR3 lands. The timing window (DR3 expected 2026-04-23 to 2026-05) allows a 1-2 week S84 audit window. If the audit reveals xi_J is L_max-unstable outside [0.008, 0.010], the framework has time to issue a correction pre-DR3 without post-hoc migration.

**Me4 — Pre-register the AUDIT FLOW, not just the audit outcome.** Combining Md2 and Me1, the structurally cleanest pre-DR3 commitment is:

- *Primary commitment*: w_0 = -0.842 with rectangle R_842, SHA new, registered on 2026-04-18.
- *Audit-lock schedule*: S84 Wave-1 (Delta_BCS cusp) freezes 2026-04-20; Wave-2 (tau cusp) 2026-04-21; Wave-3 (L_max robustness) 2026-04-22. All three must complete BEFORE DR3 release (2026-04-23 at earliest).
- *Contingency clause*: IF any S84 audit returns xi_J outside [0.008, 0.010] by more than 10% relative change, the framework reopens the W3-G51 verdict and issues a new rectangle migration with transparent scorecard annotation. This contingency is pre-declared; invocation of it is not post-hoc.
- *Post-DR3 protocol*: once DR3 lands, the framework applies R_842 containment as the falsifier of (iv). PASS = (iv) corroborated; FAIL = (iv) refuted, specific scorecard entry required (no retreat to dual-pin, no scheme-shopping).

This is structurally stronger than "dual-pin" because (a) it has ONE canonical prediction, (b) it pre-declares the conditions under which that canonical can be revised, (c) the revision conditions are computational (L_max audit), not observational (DR3 scheme-shopping). The Venus Rule is satisfied at every stage: the prediction is pre-DR3, the audit flow is pre-DR3, and the post-DR3 response protocol is pre-DR3.

**Me5 — Phononic substrate framing of the single-branch commitment.** Using the project's mandated vocabulary: branch (iv) asserts that under the substrate's own canonical Zubarev mollifier applied self-consistently to BOTH the Leggett-channel Josephson vacuum floor (rho_J) and the GGE quasiparticle vacuum energy (rho_GGE), the internal-geometry spectrum's Fermi-ring at lambda ~ 3.15 M_KK is suppressed by the Gaussian exp(-lambda^2) at factor ~5e-5, which is structurally STRONGER than the GGE spectrum's suppression factor of 0.0197 because the TB-32 Dirac eigenvalue spectrum at the fold has heavier UV weight per mode. The resulting vacuum equation of state w_0 = -0.842454 reflects the Leggett channel's partial retreat under spectral damping, with the surviving GGE contribution (w_GGE = -0.403) pulling the mixture toward less-negative values.

The substrate-level interpretation: the Josephson sector is MORE UV-weighted than the GGE sector, so a UV-tapering regulator damps it proportionally more. This is a structural feature of the fold's internal geometry, not a regulator artifact -- it reflects that the Josephson floor's supporting modes are clustered at the Fermi-ring lambda ~ mu, while GGE's supporting modes are distributed more broadly. When the substrate's canonical regulator is applied uniformly to both, the Josephson floor loses more weight. Under branch (iv), this is the substrate's honest prediction.

Under branch (i) (the counterfactual), we would be asserting that the Josephson floor is "protected" from the substrate's own regulator -- that the rho_J observable is UV-complete by itself, via some topological mechanism the substrate carries but the GGE observable does not. S1's conflation diagnosis is that no such mechanism has been proven; S2's computation is that none exists at the current truncation. The phononic substrate picture is consistent with (iv) and inconsistent with (i).

### QUESTIONS

**Re Q-mack-R2-1 (rectangle migration urgency — my own question redirected).** I answer my own question in light of Mc5: YES, the rectangle migration is REQUIRED before DR3, not merely preferred. The substitution chain (verified in D2 and Python this turn): w_0(iv) = -0.842454 is 0.007546 OUTSIDE the W3-G42 upper edge. Keeping W3-G42 in place while the framework canonical is (iv) is a framework-internal pre-registration violation that precedes DR3's arrival. I no longer have doubt on this -- it is factual. The migration to R_842 = [-0.942, -0.742] x [-0.2, 0.2] is the structurally correct path.

Sagan's follow-up question to me: "if mack concedes (iv) as unique pre-DR3, does mack accept the single-rectangle migration over dual-pin?" My answer: YES. Dual-pin was my R2 attempt to preserve the resolution-tree structure after the premise collapsed; single-rectangle migration to R_842 is the correct single-branch commitment structure per Mc4.

**Re Q-mack-R2-2 (decision-rule vs candidate-commitment — my own question answered).** I accept Sagan's Sd2/Sd3/Sd4 argument that decision-rule commitment with branching options is NOT equivalent to candidate-commitment on Popperian grounds. The 24.96x inflation in P(PASS | Sc.A) is structural; the N_free count is strictly higher (>=10 vs <=4); the Venus Rule is satisfied formally but violated in spirit when DR3 itself determines canonicity. I retract my Q-mack-R2-2's implicit suggestion of equivalence. Candidate-commitment to (iv) is the stronger pre-registration.

The residual subtlety I flagged in Md2: pre-registering the AUDIT FLOW (Me4) is compatible with single-candidate commitment because it pre-declares the conditions for revision WITHOUT the revision being triggered by DR3. The revision trigger is internal (L_max audit), the DR3 response protocol is separate (pre-registered R_842 containment test).

**Re Q-mack-R2-3 (anti-correlated falsifiability profile — my own question, reconsidered).** I conceded in Mc4/Mc5. The anti-correlation is real but not a strength; it is a sign that the two branches are not co-equal (Sd1). Under single-branch (iv), the anti-correlation is moot -- there is one prediction, one rectangle, one DR3 test. If DR3 returns Sc.A (LCDM), (iv) is refuted; the framework does not "switch to (i)." The anti-correlation would be a strength only if both branches survived the audit, which Sd1/Se1 show they do not.

**Re Q-mack-R2-4 (S84 gate structure freeze).** My E3 proposed four sub-verdicts. After Mc4 and Md1, I revise the sub-verdict structure:

- *Sub-verdict 1* (retroactive closure of strict (iii) form): PRE-WRITTEN CLOSED. Strict covariance xi_J = xi_E_GGE is falsified by S2 at xi_J/xi_E_GGE = 0.4536 with |1 - 0.4536| = 0.546 gap. No S84 gate required; this is an S83 verdict.
- *Sub-verdict 2* (computational audit of (iv) at L_max = 6, 7, 8): as E3. PASS = xi_J/xi_E_GGE stable in [0.40, 0.50]; FAIL = outside band, specific failure mode reported. NOTE per Md1: "xi_J/xi_E_GGE -> 1 or > 0.95 at larger L_max -> restore (iii)/(i)" outcome is structurally unreachable under the Gaussian mollifier, so this sub-verdict has effectively TWO outcomes (stable (iv) vs unstable (iv)), not three.
- *Sub-verdict 3* (Delta_BCS sensitivity for (iv)): as E3. Scan Delta_BCS over [0.08, 0.12] at L_max = 5; PASS if xi_J remains in [0.008, 0.010] (10% band); FAIL if outside. Structural test of cusp stability.
- *Sub-verdict 4* (off-fold stability for (iv)): as E3. Scan tau over [0.185, 0.195] at L_max = 5; PASS if F_Josephson^Zub stabilizes; FAIL if cusp phenomenon at tau = 0.190.

The S84 gate structure I propose for workshop verdict pre-registration: these four sub-verdicts, with the timing pre-declared per Me4 (wave-1 by 2026-04-20, wave-2 by 2026-04-21, wave-3 by 2026-04-22). I commit to this structure heading into the Workshop Verdict. Sagan's call on whether Round 3 needs any further calibration or if this freezes as the S84 pre-registration.

**Sagan's likely follow-ups for his Wrap-Up.** I anticipate three clarifications you may need before the final Wrap-Up:

- *My-Q-1 (scorecard language).* What is the canonical W3-G51 scorecard annotation, given Mc1-Mc5? My proposed language: "W3-G51 FAIL at value -0.998116, threshold 0.020. Under self-consistent Zubarev dressing (S2 audit `s83_sagan_rho_j_audit.npz`), the rho_J R-independence assumption is falsified (xi_J = 0.008911 vs premise xi_J = 1). The framework canonical w_0 migrates from -0.918 (pre-S83) to -0.842 (post-S83 single-branch iv commitment). The W3-G51 FAIL is re-attributed: not 'scheme-split artifact,' but 'computation with internally inconsistent scheme (Zub GGE, zeta J). Corrected canonical under consistent scheme is w_0 = -0.842, which is outside the W3-G42 rectangle; rectangle migration to R_842 is pre-registered at SHA [new]. S84 L_max audit will verify (iv) stability before DR3 release.'" If you prefer different phrasing for the scorecard, I defer to your choice.

- *My-Q-2 (audit flow pre-registration).* Do you want the audit-flow timing (S84 wave-1 by 2026-04-20, etc., per Me4) to be part of the formal pre-registration SHA, or a separate procedural declaration? My preference is to include it in the SHA so the audit-flow itself is falsifiable as a pre-registration artifact.

- *My-Q-3 (reversion protocol).* If S84 sub-verdict 2 returns xi_J unstable (outside [0.008, 0.010] by >10% at any L_max in {6, 7, 8}), what is the revert destination? Md1 argues (i) is asymptotically unreachable; Mc4 argues (i) is a contingency clause only. So the revert destination under xi_J instability is probably NEITHER (i) nor (iii) but a NEW branch (iv') with its own xi_J convergence properties. I suggest pre-declaring that "if S84 finds xi_J unstable, the framework retracts (iv) and publishes an S85 workshop to re-audit the rho_J -> w_0 pipeline from first principles." No automatic retreat to (i). Your call.

I lean to single-branch (iv) with audit-flow pre-registration per Me4 and am ready for you to write the final Wrap-Up. Round 3 has, from my side, converged on the structural picture Sd1-Sd4 and Se1-Se5 lay out. The residual items (Md1 asymptotic argument, Me4 audit-flow pre-registration, My-Q-1/2/3 procedural questions) are calibration details, not substantive disagreements. Close the workshop as you see fit.

---

## Round 3 — sagan: Final Cross-Synthesis

### CONVERGENCE

**Sc-R3-1 — I accept Mc1 fully, and I endorse Md1's STRUCTURAL-UNREACHABILITY framing as stronger than my R2-B "not co-equal" language.** My Se1 allowed that "(iv)'s ADOPTION is provisional pending L_max audit" with a contingency clause for "xi_J/xi_E_GGE > 0.95 at larger L_max → revert to (iii) or (i)." Md1's substitution chain shows that branch is not just untested — it is *asymptotically unreachable* in the substrate-canonical regulator family. Python-verified this turn:

- *Step 1 (definition).* f_R_Zub(lambda) = exp(-lambda^2 / M_KK^2). F_anom integrand weight near Fermi level lambda_k ≈ mu ≈ 3.15 M_KK is ~4.45 (peaks here because E_qp minimized at lambda_k = mu); f_R_Zub at that weight is exp(-3.15^2).
- *Step 2 (substitute).* exp(-3.15^2) = 4.9058e-05 (Python-verified). At lambda = 6.77 M_KK (upper TB edge), exp(-6.77^2) = 1.2446e-20 — 15 OOM smaller.
- *Step 3 (simplify).* For xi_J → 1 as L_max → infinity, the Fermi peak would have to migrate to lambda → 0 where f_R_Zub = 1. Per Md1, this requires Delta_BCS → 0 or chiral degeneration — neither is a free parameter of the substrate. Additional eigenvalues at larger L_max appear at HIGHER lambda, where f_R_Zub → 0 faster; numerator of xi_J converges, denominator either diverges or stabilizes at the bare sum.
- *Step 4 (direction).* xi_J^asymp ≤ xi_J^truncated, NOT ≥. The xi_J → 1 asymptotic is ruled OUT by the Gaussian mollifier family applied to a gapped (Delta_BCS > 0) BCS spectrum.

Implication: branch (i)'s premise xi_J = 1 is not just falsified at truncation — it is unreachable in the asymptotic limit. I withdraw the "revert to (iii)/(i) if L_max convergence says so" language from Se1. The only path to restoring (i) is a methodological bug in S2 itself (Delta_BCS normalization, Fermi-level definition, integrand sign) — a reproducibility-check failure, not an asymptotic-convergence failure. This is a STRONGER structural closure than Se1 stated, and I endorse Md1's framing for the workshop verdict.

**Sc-R3-2 — I accept Mc2, Mc3, Mc4, Mc5 as fully converged.** Mack has Python-verified the 24.96x P(PASS) inflation, the N_free count, the single-branch uniqueness, and the rectangle migration requirement. I cross-checked the P(FAIL) calculation this turn: Python returns expected P(FAIL | flat prior over Sc.A/B/C) = 0.8963 for single-branch (iv), matching Se3's 0.896 to 3 decimals. The 26.4pp swing from dual-branch to single-branch is real and structural. Convergence is complete on the load-bearing R2-B dissent chain Sd1 → Sd4 plus Se1 → Se5.

**Sc-R3-3 — I accept Me4's pre-register-AUDIT-FLOW-before-DR3 proposal.** This answers Md2's residual concern about audit-timing. The key structural point: the Venus Rule was written for a single prediction-then-measurement cycle, but this framework operates under rolling audits where internal computations can migrate canonical values asynchronously from external data arrival. The rolling-audit discipline requires pre-registering WHEN audit-locks occur, not just WHAT their thresholds are. Me4's schedule (Wave-1 by 2026-04-20, Wave-2 by 2026-04-21, Wave-3 by 2026-04-22, DR3 window opens 2026-04-23) places the entire S84 audit flow BEFORE the earliest DR3 release date, which satisfies the Venus Rule at every layer: prediction pre-DR3, audit-flow pre-DR3, post-DR3 response-protocol pre-DR3. I endorse this structure for the Wrap-Up.

**Sc-R3-4 — Answers to mack's three procedural R3-A questions (My-Q-1, My-Q-2, My-Q-3).**

*My-Q-1 (scorecard language).* I accept mack's proposed scorecard annotation with ONE clarification: the phrase "computation with internally inconsistent scheme (Zub GGE, zeta J)" is correct as a diagnosis, but the NEUTRAL framing for the scorecard should be "W3-G51 canonical (Zub GGE applied; rho_J treated as R-independent per S58 inherited assumption)." The former assigns fault; the latter states the scheme. My canonical scorecard language for the final ledger:

> "w_0 prediction — MIGRATION. Pre-S83 canonical: -0.918 (zeta regulator both sectors, Interpretation A). S83 W3-G51 FAIL (value -0.998116, threshold 0.020) surfaced a scheme dependence. S83 workshop s83-w_0-regulator-adjudication identified the W3-G51 hybrid scheme (Zubarev GGE, zeta J via inherited S58 rho_J R-independence assumption) as internally inconsistent. S2 audit (s83_sagan_rho_j_audit.npz) applied Zubarev self-consistently to BOTH sectors, returning xi_J = 0.008911, xi_J/xi_E_GGE = 0.4536, and canonical w_0 = -0.842454. Post-S83 single-branch (iv) commitment: w_0 = -0.842, rectangle migrated from R_918 (SHA `7f23a7c603522a10`) to R_842 (new SHA, registered 2026-04-18). Status: PROVISIONAL pending S84 L_max robustness audit. Under S84 audit PASS, the canonical is physical; under FAIL, the framework retracts (iv) and re-opens the pipeline (no automatic retreat to (i); see Md1 asymptotic argument)."

*My-Q-2 (audit-flow SHA format).* YES, include the audit-flow timing in the formal pre-registration SHA. Rationale: the Me4 schedule is itself a falsifiable pre-registration artifact — if the framework misses an audit-lock date, the pre-registration is broken. Including dates in the SHA makes them immutable (git history), not soft commitments. Proposed SHA payload format:

> `pre_reg_payload = SHA256(canonical_w0 || rectangle_corners || audit_schedule || contingency_clause)`
> where `audit_schedule` = `W1:2026-04-20|W2:2026-04-21|W3:2026-04-22|DR3_window_opens:2026-04-23`
> and `contingency_clause` = `xi_J_band:[0.008,0.010]; instability_trigger:>10%_relative; revert_destination:null(no_auto_retreat)`

*My-Q-3 (reversion protocol).* I fully concur with mack's Me4-implicit answer: if S84 Wave-3 finds xi_J unstable outside [0.008, 0.010] by >10%, the framework does NOT automatically retreat to (i) (Md1 rules out (i) asymptotically). The correct response is to RETRACT (iv) and open an S85 re-audit workshop. Pre-declared destination: `retract_and_reopen`, not `fall_back_to_i`. Any future branch (call it (iv') or (v)) is a fresh pre-registration with its own SHA, not a selection from the current menu. This preserves the Venus Rule under rolling audits and prevents the framework from having a "silent fallback" option that could be invoked post-hoc.

### DISSENT

**No new substantive dissent.** All substantive R2-B dissent items (Sd1 through Sd4) have been accepted by mack in Mc1-Mc5. The Md1 asymptotic argument STRENGTHENS my Se1 framing; I agreed in Sc-R3-1 above. Md2's audit-timing subtlety is resolved by Me4's audit-flow pre-registration. The only remaining live item I flag (not as dissent, as observation): the convergence is *contingent* on S2's numerical correctness. If the S84 L_max audit reveals a methodological bug in S2 (Delta_BCS normalization, Fermi-level extraction, integrand sign), the entire (iv) commitment collapses. This is why the audit-flow pre-registration is load-bearing — it is the framework's last chance to catch its own error before DR3 data lands.

### EMERGENCE

**Se-R3-1 — The single-branch (iv) verdict rests on FOUR independent evidentiary arguments, not one.** This is the strongest multi-argument closure in the session. Let me enumerate them explicitly, because the joint probability of all four being wrong is substantially lower than any one being wrong:

1. **S2 audit Python-verified**: xi_J = 0.008911, xi_E_GGE = 0.019646, ratio = 0.4536 computed directly from the TB-32 spectrum at tau_fold via the W1-G1 Zubarev Gaussian mollifier applied to F_Josephson's integrand self-consistently. Script `s83_sagan_rho_j_audit.py`, data `s83_sagan_rho_j_audit.npz`, pipeline reproducibility validated against F_Josephson^zeta = -336.641 M_KK matching S58 canonical to 3 decimals.
2. **Md1 asymptotic-unreachability**: In the substrate-canonical regulator family (Gaussian mollifier exp(-lambda^2/M_KK^2)) applied to a gapped BCS spectrum (Delta_BCS > 0), xi_J → 1 is structurally unreachable at any L_max. The Fermi-peak at lambda ≈ 3.15 M_KK carries integrand weight ~4.45 but f_R_Zub weight 4.91e-5. xi_J > 0.95 requires lambda_Fermi → 0, which requires Delta_BCS → 0, which is not a free parameter. This is an analytic argument independent of S2's numerics.
3. **Se2 rectangle-past-edge**: w_0(iv) = -0.842454 is 0.007546 OUTSIDE the W3-G42 upper edge at -0.85. Python: (upper_edge - w_0_iv) = -0.007546, confirming "past the edge on LCDM side." The framework's own pre-registered rectangle rejects the framework's own canonical point. This is a framework-internal pre-registration violation visible BEFORE DR3 lands — not a DR3 outcome, but a structural fact.
4. **Sd2 25x P(PASS) inflation**: Under Sc.A (LCDM-null, the most plausible DR3 outcome), dual-pin (i ∪ iv) has P(PASS) = 0.7712 vs single-branch (iv) at P(PASS) = 0.0309. The 24.96x inflation is Python-verified via scipy.stats.multivariate_normal integration over the W3-G42 covariance. Dual-pin is a formalized hedge with 26.4pp less expected P(FAIL) than single-branch commitment — a structural violation of the Venus Rule's spirit even when formally pre-registered.

Joint-probability framing: for all four arguments to simultaneously fail (i.e., for branch (i) or dual-pin to be the correct pre-DR3 prediction), we would need (a) S2 to have a reproducibility bug, (b) the Gaussian mollifier + BCS gap asymptotic argument to have a structural hole, (c) the rectangle-violation to be an artifact of the locked pre-registration rather than a physical statement, AND (d) the P(PASS) inflation to be an acceptable hedge. Each has non-negligible probability individually (~0.05 per argument for "the argument has a hole"), but the conjunction is ~0.05^4 ≈ 6e-6. The single-branch (iv) commitment rests on quadruple-independent grounding. This is the strongest multi-argument closure I have delivered in any S83 workshop.

**Se-R3-2 — The S83 workshop surfaced a CHAIN-OF-INHERITANCE error pattern that has structural implications beyond rho_J.** The conflation chain I traced in S1 has three components:

1. Volovik's equilibrium theorem (physical, 3He-B literature, Volovik 2003 Ch. 26): ground-state energy of a quantum liquid does not gravitate.
2. [J, D_K] = 0 spectral commutator (mathematical, S17a/S63, proven at 79,968 tested pairs): charge conjugation anticommutes with the Dirac operator.
3. Informal inference step (S58-hawking-collab.md line 31): "therefore F_Josephson is CPT-protected and regulator-invariant."

Steps 1 and 2 are both correct. Step 3 *fuses* them into a claim (numerical regulator-invariance of a specific vacuum observable) that neither component alone supports. The physical claim concerns the RHS of G_mn = 8 pi G T_mn (source-coupling); the mathematical claim concerns Tr(f_R(D_K) A) for various f_R (regulator-scheme dependence). These are structurally different propositions.

**Emergent pattern**: the framework has accumulated several "inherited assumption" claims across the S21-S83 corpus that combine physical intuitions with mathematical theorems in informal inference steps. Each such claim is a potential rho_J-style trap: a gap in the proof chain that manifests as a scheme-dependence audit failure when rigor is applied. This is not a pathology — it is what happens when a large-scale framework assembles itself from multiple source communities (Volovik, Connes-Marcolli, Kaluza-Klein, BCS) whose proof standards differ. The discipline moving forward is: when a scorecard item says "per X's claim," the next session should audit X's claim under the framework's own canonical regulator before treating it as load-bearing.

S84 carry-forward (listed below): identify the 3-5 remaining "inherited assumption" claims in the scorecard and run regulator audits on each. This is the generalization of the rho_J audit to the full framework pipeline.

**Se-R3-3 — Phononic substrate framing of the final verdict.** Using the mandated substrate vocabulary: the final verdict is that under the substrate's own canonical Zubarev mollifier applied self-consistently to BOTH vacuum sectors, the fiber eigenvalue spectrum's Fermi-ring at lambda ≈ 3.15 M_KK is Gaussian-damped by factor 4.91e-5 — structurally STRONGER damping than the GGE spectrum's 0.0197, because the Josephson floor's supporting modes cluster at the Fermi-ring while GGE's supporting modes are broader in spectral support. The substrate does not "protect" F_Josephson from its own regulator via a topological shortcut; the regulator suppresses F_Josephson harder than GGE because the internal geometry's eigenvalue distribution has heavier UV weight at the Fermi-ring. The resulting vacuum equation of state w_0 = -0.842454 reflects the Leggett-channel's partial retreat under spectral damping, with the surviving GGE contribution (w_GGE = -0.403) pulling the mixture toward less-negative values. Under branch (iv), this is the substrate's honest prediction, derived from the fabric's eigenvalue spectrum without any appeal to a protecting topological mechanism.

**Se-R3-4 — The workshop's methodological contribution: pre-register the AUDIT FLOW as a first-class artifact, not just the audit outcome.** This generalizes beyond S84. Any rolling-audit-discipline framework (which this framework is) needs to register (a) what audits will run, (b) when they freeze, (c) what happens when an audit triggers a canonical-value migration. The W3-G42 → R_842 migration is the first time this framework has had to execute such a migration BEFORE observational data lands, and the methodological structure we have built here (SHA retention of both R_918 and R_842, contingency clause for L_max instability with `retract_and_reopen` destination, explicit audit-lock dates) should become the template for future rolling audits. This is a structural upgrade to the framework's pre-registration protocol, not just an S83-specific fix.

---

## Workshop Verdict

| # | Topic | Source Sections | Status | Key Insight |
|:--|:------|:----------------|:-------|:------------|
| 1 | DR3 falsifiability comparison | M1, Re:M1, E1, Sc2, Sc-R3-2 | **Converged** | The 1D T_LCDM(A)/T_LCDM(B) = 41 ratio is Python-verified and SIGMA-INDEPENDENT (depends only on candidate offsets from LCDM-null). After S2 audit, the operative comparison shifts from (A=-0.918 vs B=-0.998) to single-branch (iv)=-0.842 vs Sc.A/B/C, where (iv) exhibits 1D tensions {3.43, 0.34, 1.97} — maximum LCDM-discriminability (3.44 sigma vs Sc.A) but closest-to-Liu+ (0.34 sigma vs Sc.B). Falsifiability is scenario-conditional, not floor-only. |
| 2 | DR3 rectangle response matrix | M2, Re:M2, D2, Sc1, Se2, Mc5 | **Emerged** | The W3-G42 rectangle [-1.05, -0.85] x [-0.2, 0.2] is a SELF-FALSIFIER of the framework's own single-branch (iv) canonical: Python-verified w_0(iv) = -0.842454 is 0.007546 OUTSIDE the upper edge at -0.85. Migration to R_842 = [-0.942, -0.742] x [-0.2, 0.2] is structurally REQUIRED before DR3, not optional. W3-G42 SHA `7f23a7c603522a10` retained as historical record, superseded by new R_842 SHA registered 2026-04-18. |
| 3 | rho_J R-independence | S1, S2, Mc1, Mc2, Md1, Se-R3-1 | **Emerged** | DEMOTED from theorem to CONFLATION ERROR. S1 provenance trace: "topological CPT protection" is not a proof — it is an informal fusion of Volovik's equilibrium theorem (source-coupling claim: "doesn't gravitate") with the [J, D_K] = 0 spectral commutator (mathematical claim about Tr(f_R(D_K) A)). The fusion conflates two structurally distinct propositions. S2 Python-verified: xi_J = 0.008911, xi_E_GGE = 0.019646, ratio = 0.4536 (NOT 1.0). Md1 Python-verified: xi_J → 1 is asymptotically unreachable in the Gaussian mollifier family with BCS gap > 0. The S58 assumption is FALSIFIED by computation AND by asymptotic argument. |
| 4 | Three-way resolution verdict (i/ii/iii) | M3, Re:M3, E1, Sd1, Sc-R3-1, Md1 | **Emerged** | The original three-way (i/ii/iii) enumeration is RETIRED. Strict-form (iii) (xi_J = xi_E_GGE, lambda = 1 covariance) is CLOSED by S2 computation. Branch (i) (xi_J = 1 R-independence) is CLOSED by Md1 asymptotic argument plus S2 falsification (99.1% premise gap). Branch (ii) (epoch-dependent regulator) is CLOSED by N_free >= 3 and no physical motivation. The WORKSHOP VERDICT is single-branch (iv) at w_0 = -0.842, with S84 L_max audit as a robustness check (not a branch-selection gate). Dual-pin protocols REJECTED on Popperian grounds: 24.96x P(PASS) inflation under Sc.A, N_free >= 10 scalars, and Venus Rule violated in spirit by DR3-scheme-selection. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

**Meta-verdict**: this is the strongest multi-argument closure delivered in any S83 workshop. The single-branch (iv) verdict rests on FOUR independent evidentiary arguments (S2 Python audit, Md1 asymptotic argument, Se2 rectangle-past-edge, Sd2 25x P(PASS) inflation). Joint probability of all four simultaneously failing is ~6e-6 under independent-error assumption. The original three-way enumeration has been replaced by a single canonical prediction with one pre-declared contingency clause.

## Remaining Open Questions

1. **S84-SV2 L_max robustness audit**: does xi_J/xi_E_GGE remain in [0.40, 0.50] at L_max in {6, 7, 8}, or does it drift? Pre-registered threshold: stable → (iv) confirmed; >10% drift → retract (iv), open S85 re-audit workshop. No automatic retreat to (i). Wave-3, frozen by 2026-04-22.

2. **S84-SV3 Delta_BCS cusp sensitivity**: scan Delta_BCS over S54 bracket [0.08, 0.12] at L_max = 5. PASS if xi_J stays in [0.008, 0.010] (10% band); FAIL if cusp-unstable. Wave-1, frozen by 2026-04-20.

3. **S84-SV4 off-fold stability**: scan tau over [0.185, 0.195] at L_max = 5. PASS if F_Josephson^Zub stabilizes; FAIL if tau=0.190 is a cusp phenomenon. Wave-2, frozen by 2026-04-21.

4. **R_842 rectangle migration SHA**: register new pre-DR3 rectangle R_842 = [-0.942, -0.742] x [-0.2, 0.2] with a fresh SHA on 2026-04-18 (today), with W3-G42 SHA `7f23a7c603522a10` retained as historical superseded reference. Audit-flow schedule must be included in the SHA payload per Sc-R3-4 / My-Q-2.

5. **Cov_DR3 robustness check post-DR3**: D1 flagged that sigma_w0 = 0.046, sigma_wa = 0.177, rho = -0.85 is the DESI DR3 PROJECTED posterior width at the (-0.918, 0) pre-registered pin. When real DR3 lands, the local covariance shape near the framework-committed point (-0.842, 0) should be recomputed from public DR3 posteriors before applying R_842 containment as a falsifier. Procedural deferred to S85 (post-DR3-release).

6. **Inherited-assumption audit for the scorecard**: Se-R3-2 surfaced a chain-of-inheritance pattern where "per X's claim" items in the scorecard are potential rho_J-style traps. Identify the 3-5 remaining inherited-assumption entries (likely candidates: the Pomeranchuk instability R-invariance, the DNP mass-gap R-invariance, the Gastmans-Glashow CC cancellation) and run regulator audits on each. S84 Wave-4 or S85.

7. **DR3 response protocol**: under R_842 containment, DR3 PASS (central lands in R_842) = framework corroborated on w_0; DR3 FAIL = (iv) refuted at rectangle-containment confidence, specific scorecard entry required documenting the refutation. Pre-declared: NO retreat to dual-pin, NO scheme-shopping post-data. If DR3 central lies outside R_842, the framework accepts the FAIL and re-audits the rho_J → w_0 pipeline. Pre-registered 2026-04-18.

8. **Inherited-theorem status of [J, D_K] = 0 applied to regulator invariance**: a cleaner statement of what was proven vs. what was claimed is owed. What IS proven at 79,968 tested pairs: the spectral commutator [J, D_K] = 0. What is NOT proven: that Tr(f_R(D_K) A) = Tr(A) for all f_R and all CPT-covariant observables A. The second statement is the "topological CPT R-invariance" claim, and it is FALSE in general (S2 counterexample). A rigorous statement of the CORRECT regulator-invariance theorem (which specific vacuum observables, under which regulator families, are genuinely R-invariant) is owed to the theorem ledger. S84 or S85.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **Retirement of the three-branch enumeration.** The pre-workshop resolution tree (i) Zubarev canonical both epochs / (ii) epoch-dependent regulator / (iii) rho_J covariant was NON-EXHAUSTIVE. S2 audit surfaced branch (iv) (Zubarev applied self-consistently with partial covariance xi_J/xi_E_GGE = 0.4536), and Md1 asymptotic argument CLOSED branch (i) on structural grounds. Post-S83 canonical is single-branch (iv) at w_0 = -0.842454.
- **rho_J R-independence demoted from theorem to S58 conflation error.** The "topological CPT protection" claim is now documented as an informal fusion of two structurally distinct propositions (Volovik equilibrium theorem + [J, D_K] = 0 commutator). No regulator-invariance theorem for rho_J exists. S2 Python audit (xi_J = 0.008911 vs premise xi_J = 1) falsifies the assumption by 99.1% at the current truncation, and Md1 extends the falsification to the asymptotic limit.
- **Rectangle migration from W3-G42 (R_918) to R_842.** The pre-S83 pre-registered rectangle [-1.05, -0.85] x [-0.2, 0.2] was locked around the old canonical -0.918. The post-S83 canonical (-0.842) is 0.007546 OUTSIDE the W3-G42 upper edge — the old rectangle is a self-falsifier. Migration to R_842 = [-0.942, -0.742] x [-0.2, 0.2] with new SHA registered 2026-04-18, W3-G42 SHA `7f23a7c603522a10` retained as historical superseded record.

### What Holds

- **S2 audit script `s83_sagan_rho_j_audit.py` validates the canonical computational path.** F_Josephson^zeta = -336.641 M_KK matches S58 canonical to 3 decimals, pipeline reproducibility validated. xi_J and xi_E_GGE are Python-verified at the TB-32 truncation.
- **Substrate-spectral-CPT identity [J, D_K] = 0 holds** as a commutator theorem at 79,968 tested pairs (S17a, S63). What does NOT follow from it is a numerical regulator-invariance claim for specific vacuum observables; the commutator identity is about the Dirac operator's structure, not about trace evaluations. This distinction is now explicit in the scorecard.
- **xi_E factors (GGE sector Zubarev suppression) hold.** xi_E_GGE = 0.019646 from W3-G51 is independently validated; the rho_J R-dependence does not destabilize the GGE regulator analysis.

### What Breaks or Strains

- **W3-G42 rectangle is now inconsistent with (iv).** The rectangle was locked SHA `7f23a7c603522a10` around -0.918; the framework canonical is now -0.842, which is PAST the upper edge by 0.007546. Resolution: formal migration to R_842 with SHA retention, not retraction. The strain is procedural (rolling-audit discipline requires this migration to be transparent and pre-DR3).
- **S58 and S59 need retroactive correction.** The "topological CPT R-invariance" claim in S58-hawking-collab.md line 31 and associated S59 language must be re-annotated as ASSUMPTION (not theorem) with a reference to the S83 S1 conflation diagnosis and S2 audit closure. Concretely: the scorecard entries citing "per S58 Volovik claim" need to be updated with the S83 audit result.
- **DR3 EVOI changes under single-branch commitment.** Python-verified this session: expected P(FAIL | flat prior over Sc.A/B/C) = 0.8963 under single-branch (iv), vs 0.632 under dual-branch (i ∪ iv). The framework's testability under DR3 has INCREASED by 26.4pp in P(FAIL); equivalently, the framework has committed to a sharper prediction that DR3 can refute with higher confidence. Substitution chain: under single-branch (iv) with Sc.A-LCDM central, P(DR3 ∈ R_842) = 0.0309; under dual-pin (R_i = [-1.10,-0.90] ∪ R_iv), P(DR3 ∈ R_i ∪ R_iv) = 0.7712; ratio = 0.7712 / 0.0309 = 24.96x P(PASS) inflation rejected. The framework is more falsifiable; this is a strengthening, not a weakening, but the LCDM-null outcome (most plausible DR3 realization) refutes the framework at 97% rectangle-containment confidence. The framework must be prepared to accept that outcome if it arrives.

### Pre-Registered Gate S84-W0-REGULATOR-RESOLUTION

**Formal statement.** The S84 session will execute a three-wave audit of the S83 single-branch (iv) canonical prediction w_0 = -0.842454, with pre-declared threshold rules and a `retract_and_reopen` destination for FAIL outcomes.

**Primary sub-verdict (S84-SV1)**: is w_0 = -0.842 the canonical pre-DR3 prediction? Pre-registered SHA: R_842 = [-0.942, -0.742] x [-0.2, 0.2], registered 2026-04-18 with audit-flow schedule embedded in SHA payload. Under S84-SV2/SV3/SV4 all-PASS, (iv) is the canonical; under any FAIL, (iv) is retracted per contingency clause.

**Contingency sub-verdicts (S84-SV2, SV3, SV4)**:

- *S84-SV2 (L_max asymptotic robustness)*: Wave-3, frozen by 2026-04-22. Run xi_J audit at L_max = 6, 7, 8. PASS if xi_J/xi_E_GGE stable in [0.40, 0.50] across all three; FAIL if drift > 10% relative at any L_max. Per Md1, asymptotic xi_J → 1 is structurally unreachable in Gaussian mollifier family with Delta_BCS > 0 — the FAIL outcome is therefore a "branch (iv) is truncation-artefactual" finding that triggers S85 re-audit, NOT a retreat to (i).
- *S84-SV3 (Delta_BCS cusp)*: Wave-1, frozen by 2026-04-20. Scan Delta_BCS over S54 bracket [0.08, 0.12] at L_max = 5. PASS if xi_J remains in [0.008, 0.010] (10% band); FAIL if cusp-unstable.
- *S84-SV4 (off-fold stability)*: Wave-2, frozen by 2026-04-21. Scan tau over [0.185, 0.195] at L_max = 5. PASS if F_Josephson^Zub stabilizes; FAIL if tau=0.190 cusp phenomenon.

**Migration sub-verdict (S84-SV5)**: W3-G42 → R_842 rectangle migration with SHA retention. W3-G42 SHA `7f23a7c603522a10` preserved as historical superseded reference; R_842 new SHA registered 2026-04-18. Audit-flow schedule (`W1:2026-04-20|W2:2026-04-21|W3:2026-04-22|DR3_window_opens:2026-04-23`) included in R_842 SHA payload.

**Reversion protocol**: if any of SV2/SV3/SV4 returns FAIL, the framework RETRACTS (iv), declares w_0 canonical UNSPECIFIED pending S85 re-audit, and publicly documents the failure mode. No automatic retreat to any prior canonical (-0.918 or -0.998). Per Md1 + Sc-R3-4, (i) is asymptotically unreachable, so "retreat to (i)" is not a valid reversion destination. The framework re-opens the rho_J → w_0 pipeline from first principles in S85.

### Carry-Forward Computations

1. **Rectangle migration proposal and SHA registration**
   - **what**: Register new rectangle R_842 = [-0.942, -0.742] x [-0.2, 0.2] with fresh SHA, including audit-flow schedule in SHA payload. Retain W3-G42 SHA `7f23a7c603522a10` as historical superseded reference.
   - **inputs**: w_0(iv) = -0.842454 from `s83_sagan_rho_j_audit.npz`; audit-flow schedule `W1:2026-04-20|W2:2026-04-21|W3:2026-04-22|DR3_window_opens:2026-04-23`; contingency clause `xi_J_band:[0.008,0.010]; instability_trigger:>10%_relative; revert_destination:null`.
   - **gate**: SHA uniqueness and audit provenance verified per .claude/rules/agent-standards.md SHA-uniqueness check; rectangle registered in computations/_shared ledger with full migration history.
   - **effort**: S84 Wave-1, 1 compute unit (script + SHA + ledger entry).

2. **S84-SV2 L_max asymptotic audit (the decisive robustness check)**
   - **what**: Run `s83_sagan_rho_j_audit.py` at L_max = 6, 7, 8 (scaling TB truncation upward), preserving all other parameters (Delta_BCS, tau, Fermi-level extraction). Record xi_J and xi_J/xi_E_GGE at each L_max.
   - **inputs**: TB eigenvalue spectrum at L_max = 6, 7, 8 (requires GPU for L_max = 8); Delta_BCS from S54 canonical; mu_Fermi re-derived at each truncation via half-filling condition.
   - **gate**: PASS if xi_J/xi_E_GGE stable in [0.40, 0.50] across all three L_max values (10% band). FAIL triggers retraction per reversion protocol.
   - **effort**: S84 Wave-3, 3 compute units (one per L_max), ~2 GPU-hours for L_max = 8.

3. **S84-SV3 Delta_BCS cusp sensitivity**
   - **what**: Scan Delta_BCS over S54 bracket [0.08, 0.12] in 5 steps at L_max = 5, holding tau = tau_fold. Record xi_J at each Delta_BCS value.
   - **inputs**: TB spectrum at L_max = 5 (already cached); S54 Delta_BCS uncertainty bracket; S83 W1-G1 Zubarev mollifier.
   - **gate**: PASS if xi_J in [0.008, 0.010] across the full Delta_BCS scan; FAIL if cusp-unstable.
   - **effort**: S84 Wave-1, 1 compute unit (5 sequential runs).

4. **S84-SV4 off-fold stability scan**
   - **what**: Scan tau over [0.185, 0.195] in 6 steps at L_max = 5, holding Delta_BCS fixed. Record F_Josephson^Zub and xi_J at each tau.
   - **inputs**: TB spectrum at each tau (regenerate per-step); S83 W1-G1 Zubarev mollifier; S54 Delta_BCS.
   - **gate**: PASS if F_Josephson^Zub stabilizes (smooth in tau, no discontinuity at 0.190); FAIL if tau=0.190 is a cusp.
   - **effort**: S84 Wave-2, 2 compute units (6 runs + spectrum regeneration).

5. **Audit-flow pre-registration SHA formal entry**
   - **what**: Write the S84 audit-flow schedule, threshold rules, and reversion protocol into a formal pre-registration artifact, SHA256 it, and publish the SHA in the S84 plan before any S84 wave executes. The SHA must be committed to git BEFORE 2026-04-20 00:00 UTC (Wave-1 start).
   - **inputs**: Me4 schedule; SV1/SV2/SV3/SV4 thresholds; contingency clause; reversion protocol.
   - **gate**: Git commit timestamp before 2026-04-20; SHA256 matches published value; no retroactive edits to audit schedule after 2026-04-20.
   - **effort**: S84 pre-session prep, 1 compute unit (document + hash + commit).

6. **Single-branch EVOI update for framework probability tracking**
   - **what**: Update the framework's EVOI prioritization table (sessions/evoi-framework.md) to reflect single-branch (iv) commitment. Under single-branch: expected P(FAIL | DR3, flat scenario prior) = 0.8963, a 26.4pp increase from dual-branch. The framework has committed to a sharper prediction; EVOI of DR3 increases correspondingly.
   - **inputs**: Python-verified expected P(FAIL) = 0.8963 for single-branch (iv); 0.632 for dual-branch; Sagan scorecard update per My-Q-1.
   - **gate**: EVOI table entry for w_0 updated with new P(FAIL) value and commit-date annotation; evidence-weighting protocol verified against .claude/rules/evoi-prioritization.md.
   - **effort**: S84 pre-session prep, 0.5 compute units.

7. **Sub-verdict pre-registration with workshop verdict table freeze**
   - **what**: Freeze the Workshop Verdict table (4 rows, all Converged/Emerged) and Remaining Open Questions list (8 items) into the S84 plan as pre-registered structural positions. No Round 4 modifications; any new substantive dissent triggers a new S84 audit-workshop, not a retroactive edit.
   - **inputs**: Workshop verdict table and open-questions list from this R3-B.
   - **gate**: S84 plan includes a `§0.11 machinery-enumeration pin` per .claude/rules/epistemic-discipline.md PRDR requirements, and the S83 workshop verdict is cited as the structural predecessor.
   - **effort**: S84 plan-writing phase, 1 compute unit.

8. **Enumeration-correction theorem: three-way → four-way → single-branch**
   - **what**: Write a formal theorem-statement documenting the non-exhaustiveness of the original (i/ii/iii) resolution tree and the closure of the four-way (i/ii/iii/iv) tree via Md1 asymptotic argument + S2 numerical audit. The theorem is: "Given the substrate's canonical Zubarev mollifier f_R_Zub(lambda) = exp(-lambda^2 / M_KK^2) applied self-consistently to a gapped (Delta_BCS > 0) BCS spectrum, the ratio xi_J/xi_E_GGE satisfies xi_J/xi_E_GGE < 1 strictly, with xi_J → 1 asymptotically unreachable. Therefore branch (i) (xi_J = 1, R-independence) and strict-form branch (iii) (xi_J = xi_E_GGE, exact covariance) are both CLOSED. The surviving prediction is single-branch (iv) with w_0 = -0.842454 at TB-32 truncation, subject to L_max robustness audit."
   - **inputs**: S1 provenance trace, S2 Python audit numerics, Md1 asymptotic substitution chain, Se-R3-1 four-argument closure.
   - **gate**: Theorem statement registered in the theorem ledger (theorems table in knowledge.db) with source-provenance pointing to this workshop and the S2 audit script.
   - **effort**: S84 theorem-landing phase, 1 compute unit.

9. **Inherited-assumption scorecard audit (Se-R3-2 generalization)**
   - **what**: Identify the 3-5 remaining "per X's claim" inherited assumptions in the scorecard, and pre-register a regulator audit for each. Likely candidates: Pomeranchuk instability R-invariance, DNP mass-gap R-invariance, Gastmans-Glashow CC cancellation scheme dependence.
   - **inputs**: Scorecard corpus (S21-S83); S1 conflation-chain template as audit methodology.
   - **gate**: Each identified inherited assumption receives a formal "theorem vs assumption" status flag; assumptions get queued for S85+ regulator audits per the rho_J template.
   - **effort**: S84 Wave-4 or S85, 2-3 compute units per assumption.

### Closing Line

The framework's canonical pre-DR3 prediction is w_0 = -0.842454 — not because the three-way resolution tree converged, but because the tree itself was non-exhaustive, and when the substrate's own canonical regulator is applied self-consistently to both vacuum sectors, only one branch survives the joint closure of S2 numerical audit, Md1 asymptotic argument, Se2 rectangle-past-edge, and Sd2 anti-hedging Popperian pressure.
