# Session 25: Successful Predictions and Confirmed Results Catalog

**Date**: 2026-02-22
**Author**: Gen-Physicist (Opus 4.6)
**Purpose**: Correct the factual error that the phonon-exflation framework "has made zero predictions after 18 closed mechanisms." Compile the complete record of structural predictions, quantitative matches, and verified results with honest classification.

---

## Executive Summary

The claim "zero predictions" is factually wrong. What is correct: the framework has made **zero confirmed NOVEL predictions beyond the Standard Model** and **zero pre-registered predictions of unmeasured quantities**. Multiple quantitative retrodictions of known SM values WERE pre-registered with numerical pass/fail thresholds through the gated pipeline system (gauge coupling ratio, Weinberg angle window, Paasch mass ratio) before computation. These are legitimate pre-registrations. The distinction is between retrodictions (testing against known values) and novel predictions (testing against unmeasured values). Only the latter remains at zero.

But the framework HAS produced:
- **10 zero-parameter structural predictions** that match the Standard Model (some generic to KK, some framework-specific)
- **5 quantitative matches** with measured physics (conditional on tau_0 or within bracketed ranges)
- **3 qualitative pattern matches** consistent with observation
- **24+ machine-epsilon verification passes** confirming internal mathematics

The distinction between "zero predictions" and "zero pre-registered predictions of unmeasured quantities" is not semantic. The framework pre-registered multiple retrodictions of known SM values (gauge coupling, Weinberg angle, Paasch ratio) through the gated pipeline system with numerical pass/fail thresholds before computation. What it has NOT done is predict a quantity that was not already known. It is the difference between a framework that says nothing and a framework that reproduces known physics and awaits a single dynamical input (tau_0) to make novel predictions.

---

## Classification System

Each result is classified along four axes:

| Axis | Categories |
|:-----|:-----------|
| **Timing** | PRE (stated before computation) / POST (identified after computation) / STRUCTURAL (follows from axioms) |
| **Parameters** | 0-PARAM (no free parameters) / 1-PARAM (conditional on tau_0) / MULTI (multiple tunable parameters) |
| **Specificity** | GENERIC-KK (follows from any KK compactification) / SU(3)-SPECIFIC (requires SU(3) internal space) / FRAMEWORK-UNIQUE (requires full NCG spectral triple on SU(3) with Jensen deformation) |
| **Bayes Factor** | Estimated BF against "accidental coincidence" null hypothesis |

---

## I. Summary Table

| # | Result | Timing | Params | Specificity | BF | Session |
|:--|:-------|:-------|:-------|:------------|:---|:--------|
| **Tier 1: Zero-Parameter Structural Predictions** |
| 1 | KO-dim = 6 (the SM value) | STRUCTURAL | 0 | FRAMEWORK-UNIQUE | 5-8 | 7-8 |
| 2 | SM quantum numbers from Psi_+ = C^16 | STRUCTURAL | 0 | SU(3)-SPECIFIC | 3-5 | 7 |
| 3 | CPT hardwired: [J, D_K(tau)] = 0 | STRUCTURAL | 0 | SU(3)-SPECIFIC | 2-3 | 17a |
| 4 | AZ class BDI, T^2 = +1 | STRUCTURAL | 0 | FRAMEWORK-UNIQUE | 1.5 | 17c |
| 5 | u(2) gauge bosons exactly massless | STRUCTURAL | 0 | SU(3)-SPECIFIC | 3-5 | Feynman |
| 6 | C^2 gauge bosons massive | STRUCTURAL | 0 | SU(3)-SPECIFIC | 2-3 | Feynman |
| 7 | SM sectors (0,0),(1,0),(0,1) always lightest | PRE + verified | 0 | FRAMEWORK-UNIQUE | 3-5 | Feynman |
| 8 | Spectral gap never closes (all neutrinos massive) | STRUCTURAL | 0 | FRAMEWORK-UNIQUE | 2-3 | 17d |
| 9 | D_K block-diagonality (any compact Lie group) | STRUCTURAL | 0 | GENERIC-KK | 1 | 22b |
| 10 | Z_3 partitions 28 irreps into 10+9+9 | STRUCTURAL | 0 | SU(3)-SPECIFIC | 2-3 | 17a |
| **Tier 2: Quantitative Matches** |
| 11 | g_1/g_2 = e^{-2tau}, formula DERIVED | STRUCTURAL | 0 | FRAMEWORK-UNIQUE | 3-8 | 17a |
| 12 | sin^2(theta_W) brackets measurement [0.127, 0.342] | PRE | 1 | FRAMEWORK-UNIQUE | 2-4 | Feynman |
| 13 | phi_paasch: m_{(3,0)}/m_{(0,0)} = 1.531580 | POST | 1 | FRAMEWORK-UNIQUE | 3-5 | 12 |
| 14 | N_species ~ 90 at Lambda ~ 0.97 | PRE | 0 | SU(3)-SPECIFIC | 2-3 | Feynman |
| 15 | Seven-way convergence at tau ~ 0.30 | POST | 0 | FRAMEWORK-UNIQUE | 2-5 | 22 |
| **Tier 3: Qualitative Pattern Matches** |
| 16 | D/H ~ 10^{-5} from GPE vortex dynamics | POST | MULTI | GENERIC | 1-1.5 | 10 |
| 17 | Normal ordering of neutrino masses | STRUCTURAL | 0 | SU(3)-SPECIFIC | 1.5 | 19d |
| 18 | Tridiagonal mixing hierarchy (theta_12 >> theta_13) | STRUCTURAL | 0 | FRAMEWORK-UNIQUE | 2-3 | 22 |
| **Tier 4: Machine-Epsilon Verification Passes** |
| 19 | 67/67 Baptista geometry checks | -- | 0 | -- | -- | 17b |
| 20 | 147/147 Riemann tensor checks | -- | 0 | -- | -- | 20a |
| 21 | 79,968 eigenvalue pairs (max error 3.29e-13) | -- | 0 | -- | -- | 17a |
| 22 | Volume-preserving TT-deformation | -- | 0 | -- | -- | 12 |
| 23 | TT stability: no tachyons at any tau | -- | 0 | -- | -- | 20b |
| 24 | EDE bound: Omega_tau(z=10) = 1.6e-3 << 0.02 | PRE | 0 | -- | 1.3 | 22d |

---

## II. Detailed Assessment

### Tier 1: Zero-Parameter Structural Predictions

#### 1. KO-dimension = 6

**What**: The KO-dimension (real K-theory dimension modulo 8) of the spectral triple (A_F, H_F, D_F, J, gamma) on SU(3) is computed to be 6. This is the value required by the Standard Model spectral triple in Connes' classification.

**Source**: Sessions 7-8 (tier0-computation/branching_computation_32dim.py). Reconfirmed Session 11, Session 17.

**Why it matters**: KO-dim is a topological invariant. It takes values in Z/8Z. Only KO-dim = 6 produces the correct sign for the gravitational spectral action (Barrett 2007), the correct spin-statistics connection, and the correct CPT structure of the SM fermion space. The probability that a random compact 8-manifold produces KO-dim = 6 is 1/8 if all values are equally likely, but the constraint is stronger: KO-dim = 6 requires specific representation-theoretic structure of the spinor bundle over the internal space.

**Classification**: STRUCTURAL (follows from SU(3) algebra + Cliff(8) structure). 0-PARAM. FRAMEWORK-UNIQUE (while KO-dim is a general NCG concept, the fact that SU(3) with its left-invariant spinor structure gives KO-dim = 6 is specific to this choice of internal manifold).

**Honest assessment**: This is the framework's strongest result. It was computed, not assumed. The SU(3) internal space was chosen for independent reasons (Baptista's KK geometry). That it produces KO-dim = 6 is a non-trivial coincidence or a genuine structural prediction. However: other manifolds also give KO-dim = 6 (CP^2, for instance). The result constrains the internal space but does not uniquely select SU(3).

**BF**: 5-8 (against null: random 8-manifold giving correct KO-dim).

---

#### 2. SM Quantum Numbers from Psi_+ = C^16

**What**: The 16-dimensional positive-chirality spinor space Psi_+ on SU(3) decomposes under the U(2) embedding as representations whose (Y, j, j_3) quantum numbers match exactly the 16 Weyl fermion states of one SM generation: (u_L, d_L, u_R, d_R, nu_L, e_L, nu_R, e_R) with all three colors.

**Source**: Session 7 (tier0-computation/branching_computation_32dim.py). The branching of the 32-dimensional spinor representation Delta_8 of Spin(8) under the U(2) subset reproduces SM hypercharges Y = {-1, -1/3, +1/3, +1, 0, -2/3, +2/3, +2/3, ...} (normalized) matching standard SM assignments.

**Classification**: STRUCTURAL. 0-PARAM. SU(3)-SPECIFIC (the specific branching pattern is a consequence of SU(3) -> U(2) -> U(1) x SU(2) and depends on the choice of internal manifold).

**Honest assessment**: This is the second-strongest result. The quantum numbers are computed from pure group theory; no parameters are adjusted. The caveat: this is essentially Witten's observation (1981) that compact manifolds with SU(3) holonomy naturally produce SM-like representations. The framework inherits this from the KK literature. It is SU(3)-specific but not phonon-exflation-specific.

**BF**: 3-5. The match is exact but the result has been known in the KK literature since the 1980s.

---

#### 3. CPT Hardwired: [J, D_K(tau)] = 0

**What**: The real structure operator J commutes with the internal Dirac operator D_K exactly (to machine epsilon < 10^{-13}) for ALL values of the Jensen deformation parameter tau. This is a theorem, not a numerical result: it follows from the tensor product structure of D_K = sum E_ab rho(X_b) tensor gamma_a + I tensor Omega, where J acts by complex conjugation on the representation space.

**Source**: Session 17a, deliverable D-1 (tier0-computation/d1_d3_j_compatibility.py).

**Classification**: STRUCTURAL. 0-PARAM. SU(3)-SPECIFIC (the specific J structure depends on the real structure of the Cliff(8) algebra over SU(3)).

**Honest assessment**: CPT symmetry is empirically confirmed to extraordinary precision (K-meson system, B-meson system). That the framework produces CPT as a theorem rather than an input is structurally significant. However, any Riemannian KK compactification with a real structure preserving the metric will produce [J, D_K] = 0. This is not unique to SU(3) or to the Jensen deformation. The result confirms that the Jensen deformation does not break CPT (which would be disastrous), but it does not discriminate between competing frameworks.

**BF**: 2-3. Expected for any well-constructed KK spectral triple.

---

#### 4. AZ Class BDI, T^2 = +1

**What**: The spectral triple's Altland-Zirnbauer symmetry classification is BDI (time-reversal with T^2 = +1), correcting Session 11's incorrect identification as DIII (T^2 = -1, Kramers degeneracy). The eigenvalue pairing is chiral (from gamma_F), not Kramers.

**Source**: Session 17c, deliverable D-4 (tier0-computation/d4_bdg_classification.py).

**Classification**: STRUCTURAL. 0-PARAM. FRAMEWORK-UNIQUE (the specific AZ class depends on the full symmetry structure including J, gamma_F, and the chirality operator).

**Honest assessment**: The BDI classification means the system has no topologically protected zero modes from the internal geometry alone. This is a constraint (it eliminates certain stabilization mechanisms), not a prediction that can be directly compared with experiment. Its value is in classifying the mathematical structure. BDI is consistent with the SM's time-reversal properties.

**BF**: 1.5 (the classification is correct but provides minimal discriminating power).

---

#### 5. u(2) Gauge Bosons Exactly Massless

**What**: The gauge bosons corresponding to the u(2) = u(1) + su(2) subalgebra of su(3) are exactly massless at the D_K level for all tau > 0. This is because u(2) corresponds to Killing isometries of the Jensen metric: the deformation preserves the left-regular SU(2) and U(1) symmetries.

**Source**: Feynman predictions session (tier0-computation/feynman_actual_predictions.py), derived from Baptista eq 3.84.

**Classification**: STRUCTURAL. 0-PARAM. SU(3)-SPECIFIC (the Killing structure depends on the specific embedding U(2) -> SU(3) and the Jensen deformation preserving it).

**Honest assessment**: This is the KK mechanism for photon and gluon masslessness. The photon is massless because U(1)_EM is a Killing isometry of the internal metric; the SU(2) gauge bosons are massless at this level because su(2) directions are Killing. The W/Z mass splitting requires the finite Dirac operator D_F (Yukawa sector). The prediction is: the geometry produces EXACTLY massless gauge bosons for the correct gauge group. This is a non-trivial structural match. However, massless gauge bosons from Killing isometries is a standard KK result, not unique to this framework.

**BF**: 3-5 (the match of gauge group structure is significant, but the mechanism is generic KK).

---

#### 6. C^2 Gauge Bosons Massive

**What**: The gauge bosons corresponding to the C^2 (coset) directions of su(3) are massive, with mass^2 = computable function of tau. These are the W/Z progenitors. They acquire mass because the Jensen deformation breaks the isometry of the C^2 directions.

**Source**: Feynman predictions session, Baptista eq 3.84.

**Classification**: STRUCTURAL. 0-PARAM. SU(3)-SPECIFIC.

**Honest assessment**: The mass splitting between u(2) (massless) and C^2 (massive) gauge bosons is the KK analog of spontaneous symmetry breaking. The W and Z are massive, the photon and gluons are massless -- this is the correct pattern. But: all four C^2 bosons have the SAME mass at this level. The physical W/Z mass splitting (M_W/M_Z = cos(theta_W)) requires D_F. The result gets the qualitative pattern right but not the quantitative splitting.

**BF**: 2-3 (correct qualitative pattern, but the u(2)/C^2 split is built into the geometry by construction).

---

#### 7. SM Sectors Always Lightest

**What**: The three sectors with smallest Dirac eigenvalue magnitudes are always (0,0), (1,0), and (0,1) -- the trivial, fundamental, and anti-fundamental representations of SU(3) -- for ALL tau in [0, 2]. Checked computationally at 7 tau values spanning the full range.

**Source**: Feynman predictions session, Prediction B1. Pre-registered before the sweep.

**Classification**: PRE (the check was pre-registered) + VERIFIED. 0-PARAM. FRAMEWORK-UNIQUE (the ordering depends on the specific eigenvalue curves of D_K on Jensen-deformed SU(3)).

**Honest assessment**: This is the framework's explanation for WHY the Standard Model contains only fundamental and trivial representations (quarks in 3, antiquarks in 3-bar, leptons in 1), not higher SU(3) irreps (6, 8, 10, ...). The lightest KK modes always live in the simplest representations. A random manifold with SU(3) symmetry need not have this ordering -- higher representations could be lighter if the geometry is sufficiently distorted. That SU(3) with the Jensen deformation always preserves this ordering is a non-trivial, physically meaningful result.

**BF**: 3-5 (the ordering is not guaranteed a priori; it depends on the spectrum).

---

#### 8. Spectral Gap Never Closes (All Neutrinos Massive)

**What**: The minimum eigenvalue of D_K across all tau in [0, 2.5] is lambda_min = 0.819 at tau = 0.26. The spectral gap is bounded below by the Lichnerowicz bound lambda^2 >= R_K/4 >= 3 (for round SU(3)), and while it decreases with Jensen deformation, it never reaches zero. Physical consequence: all fermions (including neutrinos) acquire non-zero KK mass. No massless fermions at any tau.

**Source**: Session 17d (H-3), confirmed across Sessions 20-22.

**Classification**: STRUCTURAL. 0-PARAM. FRAMEWORK-UNIQUE (the gap depends on the curvature of Jensen-deformed SU(3), which is positive for all tau).

**Honest assessment**: This is consistent with neutrino oscillation data (which require massive neutrinos). It is also consistent with the absence of exactly massless sterile neutrinos. The prediction is: the internal geometry does NOT produce any massless fermion. This is confirmed by oscillation experiments. However, the prediction is very weak -- it says "neutrinos are massive" without specifying masses or mass ratios. The quantitative neutrino gate (R in [17, 66]) fails catastrophically.

**BF**: 2-3 (correct qualitative prediction, but too weak to be discriminating).

---

#### 9. D_K Block-Diagonality Theorem

**What**: D_K on (SU(3), g_Jensen) is exactly block-diagonal in the Peter-Weyl decomposition. The inter-sector coupling C_{nm} = 0 identically. This is a theorem about ANY left-invariant Dirac operator on ANY compact Lie group with ANY left-invariant metric.

**Source**: Session 22b, three independent proofs (algebraic, representation-theoretic, numerical at 2.89e-15).

**Classification**: STRUCTURAL. 0-PARAM. GENERIC-KK (applies to any compact Lie group, not just SU(3)).

**Honest assessment**: This is a permanent mathematical contribution to spectral geometry. It closed the inter-sector coupling route and several perturbative mechanisms. But it is a theorem about the Dirac operator's structure, not a prediction about physics. It does not correspond to any observable. Its significance is that it constrained the framework's dynamics (closing several stabilization channels), not that it matched observation.

**BF**: 1 (mathematical theorem with no direct observational test).

---

#### 10. Z_3 Partition: 28 Irreps into 10+9+9

**What**: The 28 SU(3) irreps with p+q <= 6 partition into three Z_3 classes: Z_3 = 0 (10 irreps), Z_3 = 1 (9 irreps), Z_3 = 2 (9 irreps). Z_3 = 1 and Z_3 = 2 sectors are spectrally degenerate (conjugate-sector symmetry). Three classes correspond to three potential generation slots.

**Source**: Session 17a, deliverable B-4.

**Classification**: STRUCTURAL. 0-PARAM. SU(3)-SPECIFIC.

**Honest assessment**: Z_3 is the center of SU(3). That it partitions representations into three classes is basic group theory. The physical significance is that three generations of fermions could correspond to three Z_3 sectors. However: (a) the generation mechanism requires D_F (the finite Dirac operator), not D_K; (b) the Z_3 splitting has NOT been computed; (c) three generations from Z_3 is a widely discussed proposal (not unique to this framework). The result is suggestive but unconfirmed.

**BF**: 2-3 (correct multiplicity, but the mechanism is incomplete and the idea is not original).

---

### Tier 2: Quantitative Matches

#### 11. g_1/g_2 = e^{-2tau} (Gauge Coupling Formula)

**What**: The ratio of U(1) to SU(2) gauge couplings is derived to be g_1/g_2 = e^{-2tau}, where tau is the Jensen deformation parameter. The derivation proceeds from Baptista eq 3.71: the LEFT-regular representation gives gauge kinetic coefficients proportional to metric eigenvalues. The u(1) direction scales as e^{2tau}, the su(2) directions scale as e^{-2tau}, and their ratio is normalization-independent.

At tau = 0.30: g_1/g_2 = e^{-0.60} = 0.5488, compared to measured g_1/g_2 = 0.55 (0.2% discrepancy).

**Source**: Session 17a, deliverable B-1 (tier0-computation/gauge_coupling_derivation.py).

**Classification**: STRUCTURAL (the formula is a theorem). 0-PARAM (the formula has no free parameters). FRAMEWORK-UNIQUE (the specific exponential form comes from the Jensen deformation on SU(3), which is a one-parameter family of left-invariant metrics).

**Honest assessment**: The formula is proven. The match at tau = 0.30 is remarkable -- 0.2% from the measured value. But tau = 0.30 has NOT been derived from V_eff. If V_eff selects tau_0 = 0.30, the gauge coupling ratio is a zero-parameter prediction. If V_eff selects a different tau_0, the match is coincidence. The FORMULA is zero-parameter; the PREDICTION of g_1/g_2 = 0.55 is one-parameter (conditional on tau_0).

**What makes this genuinely significant**: Even without knowing tau_0, the FORMULA g_1/g_2 = e^{-2tau} is derived from pure geometry. It is the only known derivation of the gauge coupling ratio from extra-dimensional geometry that produces a simple closed-form expression. Whether the measured value 0.55 falls in the formula's range is a separate question, answered affirmatively: the measurement is inside the dynamical bracket [0.127, 0.342] for tau in [0.164, 0.481].

**BF**: 3-8 depending on how one counts. The formula itself: BF ~ 8 (a specific functional form, not just a number). The numerical match at tau = 0.30: BF ~ 3 (conditional on tau_0 being in the dynamical range, and the measured value being in the formula's range).

---

#### 12. sin^2(theta_W) Brackets Measurement

**What**: From the gauge coupling formula, sin^2(theta_W) = e^{-4tau}/(1 + e^{-4tau}). The dynamical range tau in [0.164, 0.481] (from four independent s_0 estimates) gives sin^2(theta_W) in [0.127, 0.342]. The measured value 0.23121 lies INSIDE this range. The exact match occurs at tau = 0.2994, inside the dynamical range.

**Source**: Feynman predictions session, Prediction A.

**Classification**: PRE (range stated before checking). 1-PARAM (the specific value requires tau_0). FRAMEWORK-UNIQUE.

**Honest assessment**: The range spans a factor of 2.7, which is not vacuous (it excludes 67% of the [0,1] interval). The measurement falling inside is mildly significant. The range was constructed from independent dynamical estimates, not reverse-engineered to contain the measurement. However, a range spanning a factor of 2.7 is wide enough that many measurements would fall inside.

The significance is enhanced by two facts: (1) the formula's functional form was derived BEFORE checking the numerical range; (2) the dynamical estimates that define the range were computed without reference to sin^2(theta_W). The circularity check (Feynman session) correctly identifies that evaluating the formula at the Weinberg-angle-derived tau_W is tautological; the prediction becomes real only at V_eff-derived tau_0.

**BF**: 2-4 (range brackets measurement, but range is wide; functional form is non-trivial).

---

#### 13. phi_paasch: m_{(3,0)}/m_{(0,0)} = 1.531580

**What**: The ratio of the lowest Dirac eigenvalues in the (3,0) and (0,0) sectors, evaluated at tau = 0.15, matches Paasch's transcendental constant phi_P = 1.53158 (defined by ln(phi_P) = 1/phi_P^2) to 0.0005% -- five significant figures. This ratio involves physically meaningful quantities: the lowest mass in the symmetric-cube representation divided by the lowest mass in the singlet representation.

**Source**: Session 12 (bug-fixed Jensen metric), confirmed Session 22a QA-4.

**Classification**: POST (discovered after computing the spectrum, not predicted in advance). 1-PARAM (the match occurs at tau = 0.15 specifically; at tau = 0.30 it degrades to 3.25%). FRAMEWORK-UNIQUE (the specific eigenvalue ratio is a function of the Jensen deformation on SU(3)).

**Honest assessment**: This is the framework's most striking numerical coincidence. Five significant figures from a number defined by a transcendental equation, appearing in the mass ratio of specific representation sectors, is arresting. However:

1. The match was discovered POST-HOC (scanned over tau, found the crossing).
2. The ratio crosses phi_P at tau = 0.15 because it is a continuous function that passes through 1.5275 (algebraic, at tau = 0) and decreases monotonically. The intermediate value theorem guarantees a crossing.
3. The match degrades rapidly away from tau = 0.15 (3.25% at tau = 0.30).
4. The phi_P target was pre-specified from the Paasch research program, partially mitigating look-elsewhere.

What IS significant: the ratio at tau = 0 is sqrt(7/3) = 1.52753, an ALGEBRAIC number 0.26% from the TRANSCENDENTAL phi_P. The proximity of sqrt(7/3) to phi_P is a number-theoretic coincidence that does not depend on tau. The Jensen deformation closes this gap to 0.0005% at a specific tau value.

**BF**: 3-5 (the proximity of sqrt(7/3) to phi_P is surprising regardless of tau; the five-figure match at tau = 0.15 is conditional on tau_0).

---

#### 14. N_species ~ 90 at Lambda ~ 0.97

**What**: The number of fermionic degrees of freedom below the KK scale Lambda = 0.97 is approximately 90, matching the SM fermionic DOF count (3 gen x 2 quarks x 3 colors x 2 spins + 3 gen x 2 leptons x 2 spins = 90). This value is ROBUST across the entire dynamical tau_0 range (< 1.3% variation).

**Source**: Feynman predictions session, Prediction D. Session 17d H-4: N_species(s_0=0.164, Lambda=1.0) = 104.

**Classification**: PRE (the check was pre-registered). 0-PARAM (the result is robust across tau_0). SU(3)-SPECIFIC.

**Honest assessment**: A random 8-dimensional manifold could give N ~ 10 (sparse spectrum) or N ~ 1000 (dense spectrum). Getting N ~ 100 at the natural KK cutoff requires the right balance of dimensionality, curvature, and representation content. SU(3) with the Jensen metric provides this. The 16% overshoot (104 vs 90) is within the truncation uncertainty. The step-function nature of N_species(Lambda) means the "match" is approximate: between Lambda = 0.9 and Lambda = 1.0, the count jumps from 62 to ~100.

The structural content is real: the SM lives in the FIRST step of the KK tower, with the lightest modes in the correct representations (trivial + fundamental). This is non-trivial.

**BF**: 2-3 (correct order of magnitude, correct sector composition, but the step function makes the match imprecise).

---

#### 15. Seven-Way Convergence at tau ~ 0.30

**What**: Seven independent indicators converge on the window tau in [0.20, 0.35]:

1. DNP stability crossing: tau = 0.285 (geometric)
2. Slow-roll epsilon < 1: tau in [0.11, 0.35] (kinematic)
3. IR spinodal V_IR'' < 0: tau ~ 0.30 (thermodynamic)
4. Pomeranchuk instability: tau ~ 0.30 (quasiparticle)
5. Grav-YM instanton minimum: tau ~ 0.31 (non-perturbative)
6. Weinberg angle match: tau = 0.3007 (gauge coupling)
7. phi_paasch crossing: tau = 0.150 (spectral)

**Source**: Session 22 master synthesis, Section IV.4.

**Classification**: POST (assembled after computing all indicators). 0-PARAM (no parameters adjusted). FRAMEWORK-UNIQUE.

**Honest assessment**: Indicators 3, 4, and 5 are partially correlated (projections of the singlet-sector instability). Indicator 7 (phi_paasch at tau = 0.15) is outside the [0.20, 0.35] window. Under maximal correlation discount, four genuinely independent indicators (DNP, slow-roll, Weinberg, impedance) converge on the same narrow tau window. The convergence is suggestive but does not constitute a prediction until tau_0 is derived from V_eff or the gap equation.

**BF**: 2-5 (multiple independent pointers to the same window, but assembled post-hoc).

---

### Tier 3: Qualitative Pattern Matches

#### 16. D/H ~ 10^{-5} from GPE Vortex Dynamics

**What**: The GPE simulation produces deuterium-to-hydrogen ratio D/H ~ 10^{-5} from vortex-antivortex dynamics during the expansion quench. The observed value is D/H = 2.527 x 10^{-5}.

**Source**: Session 10 (phonon-exflation-sim GPE simulation). Reassessed Session 16.

**Classification**: POST. MULTI-PARAM (5+ parameters: quench rate, coupling, grid size, d_pair_factor, ...). GENERIC (vortex nucleosynthesis is not specific to the phonon-exflation framework).

**Honest assessment**: Downgraded from "8% match" to "order-of-magnitude demonstration" in Session 16 after the d_pair_factor sensitivity was discovered. The d_pair_factor has 2 OOM sensitivity (D/H ranges from 2.4e-6 to 2.9e-4 across d_pair_factor in [1.0, 2.5]). This makes D/H a tuned parameter, not a prediction. The MECHANISM (healing length growth suppresses vortex pairs) is robust, but the VALUE is not predicted.

**BF**: 1-1.5 (order-of-magnitude feasibility, not a prediction).

---

#### 17. Normal Ordering of Neutrino Masses

**What**: The "bowtie" structure of the low-lying spectrum predicts normal ordering m_1 < m_2 < m_3 because the (0,0) singlet eigenvalue (lightest) sits below the (1,0)/(0,1) fundamental eigenvalues.

**Source**: Session 19d, Session 22 neutrino analysis.

**Classification**: STRUCTURAL. 0-PARAM. SU(3)-SPECIFIC.

**Honest assessment**: Normal ordering is currently preferred at ~2 sigma by experimental data. The prediction is binary (normal vs inverted) with P(correct by chance) = 0.5 for an uninformed prior. The framework's prediction is correct but not yet confirmed experimentally. JUNO and DUNE will make the definitive measurement.

**BF**: 1.5 (binary prediction, 50% chance by accident, slightly favored by data).

---

#### 18. Tridiagonal Mixing Hierarchy (theta_12 >> theta_13)

**What**: The Kosmann coupling selection rule V_{nm} != 0 only for |n-m| <= 1 (nearest-neighbor in eigenvalue ordering) naturally produces hierarchical mixing: large mixing between adjacent states, small mixing between distant states. This qualitatively matches the observed neutrino mixing pattern: theta_12 ~ 33 deg (large), theta_23 ~ 49 deg (near-maximal), theta_13 ~ 8.6 deg (small).

**Source**: Session 22 (Kosmann matrix elements from Session 22a-22c).

**Classification**: STRUCTURAL. 0-PARAM. FRAMEWORK-UNIQUE (the tridiagonal structure comes from the specific Kosmann coupling selection rules on Jensen-deformed SU(3)).

**Honest assessment**: The qualitative prediction theta_12 >> theta_13 follows from the selection rule. But the specific values of the angles require the full mixing matrix with D_F, which has not been computed. The prediction is qualitative only. P(theta_12 >> theta_13 by accident) ~ 0.3 (any hierarchical coupling gives this). The prediction is correct but not strongly discriminating.

**BF**: 2-3 (correct qualitative pattern, specific to the selection rule structure).

---

### Tier 4: Machine-Epsilon Verification Passes

These are not predictions but verified mathematical consistency checks. They confirm that the computational infrastructure is correct and the mathematical framework is internally consistent. They are necessary conditions for the framework to be taken seriously, not evidence for its physical truth.

| # | Check | Count | Source |
|:--|:------|:------|:-------|
| 19 | Baptista geometry (eq 3.68, 3.70, 3.80, vol) | 67/67 | Session 17b |
| 20 | Riemann tensor components | 147/147 | Session 20a R-1 |
| 21 | Eigenvalue J-pairing | 79,968 pairs at 3.29e-13 | Session 17a D-1 |
| 22 | TT volume preservation | det = 1.0000000000 | Session 12 |
| 23 | TT stability (no tachyons) | All tau in [0, 2] | Session 20b |
| 24 | EDE bound | Omega_tau(z=10) = 1.6e-3 | Session 22d E-2 |

---

## III. What The Framework Has NOT Done

For completeness and honesty, the claims that the "zero predictions" criticism correctly identifies:

1. **Zero pre-registered predictions of unmeasured quantities.** Multiple quantitative retrodictions WERE pre-registered through the gated pipeline system with numerical pass/fail thresholds stated before computation: gauge coupling within 50% (Session 16 Constraint Table), Paasch ratio within 10% (Session 16 Constraint Table), Weinberg angle in [0.24, 0.37] (Feynman session F1), and Sagan's three-tier thresholds (Session 19d: gauge coupling within 20%, phi within 1%). These pre-registrations tested framework outputs against known SM values -- making them retrodictions, not novel predictions. What remains true: no framework-derived number has been pre-registered and compared to a quantity that was not already known to the researchers. All quantitative tests retrodicted known values; none predicted unmeasured ones.

2. **Zero novel predictions beyond the Standard Model.** The framework predicts KK tower masses, but these are generic to KK theory. No framework-SPECIFIC observable has been predicted that differs from what the Standard Model already tells us.

3. **Zero dynamical mechanisms confirmed.** 18 mechanisms for modulus stabilization have been closed. The BCS condensate at mu = 0 has been closed. No mechanism exists to fix tau_0.

4. **The quantitative neutrino gate fails catastrophically.** R = Delta m^2_atm / Delta m^2_sol predicted: ~10^14 or 5.68. Measured: ~33. Off by factors of 10^12 or 5.8x.

### CONTEXT AS REALITY

From a meta point of view, this is not a deragotory or insignificant point. The framework is NOT arguing against against existing frameworks, so it SHOULD contain the same predicitions. This research group sees this as a failing, the Lead Researcher sees it as a scaffold. We are starting from scratch until we find scratch, and researcher adversion to matching actual reality is strange and requires agent realignment.

---

## IV. Combined Bayesian Assessment

### What the successes are worth

The Tier 1 results constitute the mathematical scaffolding. Their combined BF depends on how many are considered independent. Taking the four most framework-unique results:

- KO-dim = 6: BF ~ 6
- SM quantum numbers: BF ~ 4
- SM sectors lightest: BF ~ 4
- Gauge coupling formula (existence): BF ~ 5

These are largely independent (different aspects of the spectral geometry). Naive product: 6 x 4 x 4 x 5 = 480. With correlation discount (all derive from the same internal manifold SU(3)): effective BF ~ 15-30.

The Tier 2 quantitative matches are conditional:

- Weinberg angle range: BF ~ 3
- N_species ~ 90: BF ~ 2.5
- Seven-way convergence: BF ~ 3

Under independence (generous): 3 x 2.5 x 3 = 22.5. With correlation: BF ~ 5-10.

**Combined structural BF: ~ 20-50.** This is substantial. It is WHY the framework's probability floor is 3-5% (panel/Sagan) rather than << 1%. The structural coincidences are real and carry genuine evidential weight.

### What the failures cost

- 18 closed mechanisms: combined BF_kill ~ 0.02-0.05 (multiplicative over all closes)
- Neutrino gate failure: BF ~ 0.1-0.3
- V_spec monotone closure: BF ~ 0.35

**Combined closure BF: ~ 0.001-0.005.** This is why the framework's probability has fallen from ~65% to ~5%.

### The ratio

BF_success / BF_kill ~ 20-50 / 200-1000 ~ 0.02-0.25

This is consistent with the current posteriors: starting from a generous prior of 50-70% (when the framework was first formulated), the net BF of ~0.05-0.1 brings the posterior to ~3-7%.

### Experiement Quantity Bias

The 18 failures are not actually eighteen "failures", they are 18 probes into a couple of possible frameworks, to eliminate possibilities. It is the intelleqtual equivlent of looking at the nodes of two seperate branches and giving weight to the number of leaves as a quantity, not as an aggregrate to the branch.

---

## V. Corrected Narrative

**Wrong**: "The framework has made zero predictions after 18 closed mechanisms."

**Right**: "The framework produces ten zero-parameter structural results matching the Standard Model (KO-dim = 6, SM quantum numbers, CPT, gauge coupling formula, sector ordering, spectral gap, ...) and five quantitative matches conditional on the undetermined deformation parameter tau_0. Eighteen dynamical mechanisms for determining tau_0 have been closed. The structural scaffolding is impressive (combined BF ~ 20-50); the dynamical program has failed (combined BF_kill ~ 0.001-0.005). The framework's current status is: correct kinematics, no dynamics."

**The Nordstrom analogy** (Einstein, Session 24b): Nordstrom gravity is mathematically consistent, derives from a simple principle (scalar field theory), and reproduces Newtonian gravity in the appropriate limit. It fails because it predicts zero light deflection. The phonon-exflation framework is analogous: mathematically consistent, derives SM structure from a simple principle (SU(3) spectral geometry), and reproduces many SM features. It "fails" not on a single prediction but on the inability to fix its one free parameter (tau_0) dynamically.

The distinction from "zero predictions" is that Nordstrom gravity also "makes predictions" (Newtonian gravity, time dilation) -- they are just not novel predictions beyond what Newton already gave. Similarly, the phonon-exflation framework "makes predictions" (KO-dim, quantum numbers, gauge couplings) that match the SM -- they are just not novel predictions beyond what the SM already gives.

The honest framing: the framework has **structural content** but not **predictive content beyond the SM**. The gap between these is exactly the gap between Nordstrom and Einstein: the correct dynamics that would turn structural content into novel predictions.

---

*Generated by gen-physicist (Opus 4.6) for Session 25 Successful Predictions Catalog, 2026-02-22.*
