# Session 45 Collaborative Review: Spectral-Geometer

**Date**: 2026-03-15
**Agent**: spectral-geometer
**Role**: Spectral geometry, heat kernel asymptotics, eigenvalue bounds, analytic torsion
**Focus**: Ways forward from spectral geometry after the S45 audit

---

## I. What S45 Proved About the Finite Spectrum

The heat kernel audit (HEAT-KERNEL-AUDIT-45) was the most consequential spectral-geometry result of this session. It drew a hard line through all prior computations, separating wheat from chaff. The three-tier classification is a PERMANENT structural result:

- **Tier 1 (exact)**: Spectral action, heat trace, spectral zeta moments. These require no continuum structure; they are finite sums, period.
- **Tier 2 (approximation)**: Seeley-DeWitt a_0, a_2, a_4. Lower bounds on the geometric integrals, converging as max_pq_sum -> infinity. Error O(30-50%) for a_2 at current truncation.
- **Tier 3 (artifact)**: Spectral dimension d_s(sigma), analytic torsion T, anything requiring zeta poles. These are not "wrong answers to the right question" -- they are answers to a question that does not exist on the finite crystal.

The Taylor expansion exactness theorem (S45-S1) is the sharpest of these results. For a finite discrete spectrum, the spectral action S(Lambda) = sum_k d_k f(lambda_k^2/Lambda^2) has a CONVERGENT Taylor expansion in 1/Lambda^2. This is qualitatively different from the continuum, where the Seeley-DeWitt expansion is asymptotic. On our spectrum, there is no non-perturbative content. The function is completely determined by its moments A_{2n} = sum d_k (lambda_k^2)^n. No cutoff function f can generate hierarchies that are not already present in these moment ratios -- and A_4/A_2 = 2.76. That is O(1). The CC hierarchy does not live in the spectrum.

**Structural constraint**: 29 spectral action closures (OCC-SPEC-45 being the 28th, UNEXPANDED-SA-45 the 29th) confirm that the spectral action approach to tau-stabilization has reached dimension zero. This is not a matter of choosing a cleverer cutoff or a better regularization. The spectral action on the truncated spectrum is an analytic function whose complete structure is known and contains no minimum.

---

## II. The Weyl Dimension d_Weyl = 6.81 and What It Means

The correct dimensionality diagnostic for a finite discrete spectrum is the Weyl counting exponent: fit N(lambda) ~ C * lambda^{d_Weyl} to the integrated density of states. At max_pq_sum = 5, this gives d_Weyl = 6.81.

This number is NOT 8 (the dimension of SU(3)), and the discrepancy is informative. It tells us quantitatively how far the truncation is from capturing the full Weyl regime. On a smooth 8-manifold, Weyl's law gives N(lambda) ~ (Vol / (4pi)^4) * lambda^8 as lambda -> infinity. At our truncation, the highest eigenvalues are lambda_max ~ 2.06, and the mode count has not yet reached the lambda^8 asymptotic. The "effective dimension" 6.81 reflects the curvature of the log(N) vs log(lambda) curve at this truncation level: the higher-order corrections (from the boundary of the Weyl region) bend the slope downward.

**What this constrains**: Any quantity extracted from the spectrum that depends on the dimension of the manifold (such as G_N ~ 1/a_2, where a_2 = (4pi)^{-d/2} * integral(R/6) * rank) inherits an O(15%) correction from the Weyl deficit. The 0.83-decade tension between M_KK^{gravity} = 7.43e16 GeV and M_KK^{Kerner} = 5.04e17 GeV (MKK-TENSION-45) may partially reflect this truncation effect. Computing at max_pq_sum = 6 or 7 would test this directly.

**Way forward 1**: Increase max_pq_sum. Each increment adds one PW shell. The computational cost scales as the number of new irreps times the size of each block (16x16 for each spinor sector). At max_pq_sum = 6, the new irreps (6,0), (5,1), (4,2), (3,3) and conjugates add sectors with dim^2 up to 441. This is tractable on the RX 9070 XT. The spectral action, being Tier 1, gives exact results at any truncation -- the question is whether d_Weyl approaches 8, and whether the M_KK tension narrows.

---

## III. What REPLACES the Failed Continuum Formulas?

This is the central question the user posed: "What is the correct spectral geometry of a finite crystal?"

The answer comes from the mathematical theory of **spectral triples at finite truncation** -- precisely the subject of Connes-van Suijlekom 2021 (Paper 28 in the Connes library, "Spectral Truncations in Noncommutative Geometry") and Hekkelman-McDonald 2024 (Paper 37, "Noncommutative Integral and Spectral Truncation").

On a finite spectral triple (A, H, D) with H finite-dimensional, the correct geometric quantities are:

1. **The noncommutative integral**: The Dixmier trace is replaced by the finite-rank trace. For our D_K, the analog of the Wodzicki residue is the spectral zeta moment at a specific s-value determined by the KO-dimension. On a KO-dim 6 triple, the relevant integral is Tr(|D|^{-6} a) for a in A.

2. **The spectral action functional itself**: As confirmed by S45-S1, the spectral action is the ONE quantity that transfers without loss from continuum to finite truncation. The polynomial expansion captures everything. The geometric content is in the moments A_{2n}, which encode progressively finer details of the eigenvalue distribution.

3. **The Connes distance formula**: d(p,q) = sup{|f(p) - f(q)| : ||[D,f]|| <= 1}. This is well-defined on the finite triple and gives the intrinsic metric geometry of the truncated space. It has NOT been computed for Jensen-deformed SU(3).

4. **The cyclic cohomology pairing**: OCCUPIED-CYCLIC-45 proved this is nondegenerate at all (beta, mu, Delta). The pairing ch^0_occ = ch^0_vac/2 at mu = 0 is exact. The topological structure (index, KO-dim, spectral flow = 0) is UNDAMAGED by truncation. The BdG spectral triple retains its full topological content.

5. **Eigenvalue statistics**: The pair correlation function R_2(s), spacing distribution p(s), and spectral form factor K(t) are all well-defined on a finite spectrum. They distinguish integrable from chaotic dynamics. CHAOS-1 found <r> = 0.321 (sub-Poisson), confirming integrability. This is a valid spectral-geometric probe that requires no continuum limit.

**What does NOT survive**: The spectral dimension d_s, analytic torsion, zeta-function pole structure, heat kernel UV asymptotics. These are the tools of SMOOTH spectral geometry. The finite crystal has DISCRETE spectral geometry, and the appropriate tools are the five listed above.

---

## IV. Ways Forward: The n_s Problem from Spectral Geometry

The n_s crisis is real: 6 routes tested, all failed (range: -4.45 to +5.7). The hose-count diagnostic (addendum) identifies the structural issue: n_s - 1 = alpha - beta, where alpha is the number of creation channels growing with k, and beta is the per-channel rate decreasing with k. Single-particle gives alpha = 6 (Weyl), collective gives alpha = 0 (one mode per branch). Planck requires alpha ~ 1.

**Way forward 2: Spectral flow under Jensen deformation as n_s generator.**

The spectral flow of D_K(tau) as tau traverses from 0 to tau_fold counts the net number of eigenvalues crossing zero. We proved in S35 that the spectral flow is zero (BDI symmetry, gap open). But the DERIVATIVE of spectral flow -- how eigenvalue trajectories redistribute as tau changes -- carries information about the perturbation spectrum that is distinct from the Bogoliubov coefficients.

Specifically: define the spectral CURRENT j(lambda, tau) = sum_k delta(lambda - lambda_k(tau)) * (d lambda_k / d tau). This is the flow of eigenvalue density in the spectral plane. Its divergence gives the change in the DOS. The Fourier transform of j in the lambda direction gives a k-dependent creation rate that is intrinsic to the spectrum -- no external k-mapping needed.

The advantage: j(lambda, tau) is a Tier 1 quantity (computed directly from eigenvalues and their tau-derivatives, both known). It naturally produces an intermediate alpha because it weights modes by their VELOCITY in the spectral plane, not by their degeneracy (alpha = 6) or unity (alpha = 0). Modes near van Hove singularities (where d lambda_k / d tau is large) contribute disproportionately, potentially giving the linear growth alpha ~ 1 that the hose-count diagnostic requires.

**Pre-registerable gate**: SPECTRAL-FLOW-NS-46. Compute j(lambda, tau) at tau_fold. Fourier transform in lambda. Extract the effective alpha from the k-dependence of the spectral current power spectrum. PASS if alpha in [0.8, 1.2].

---

## V. Ways Forward: The CC Problem from Spectral Geometry

Q-THEORY-BCS-45 PASSED (tau* = 0.209, first CC mechanism PASS in project history). The Gibbs-Duhem self-tuning with BCS-corrected trace-log gives a zero-crossing 10.2% from the fold. This is the open channel.

From spectral geometry, the key question is: what happens to the spectral zeta function in the continuum limit?

**Way forward 3: Spectral zeta at non-integer s-values.**

The truncated spectral zeta zeta(s) = sum d_k |lambda_k|^{-2s} is entire (no poles). In the continuum limit (max_pq_sum -> infinity), it develops poles at s = 4, 3, 2, 1 whose residues are the Seeley-DeWitt coefficients. The TRANSITION from entire to meromorphic -- how the poles nucleate as the truncation is removed -- carries information about which UV modes dominate the large-s behavior.

The trace-log TL = -(1/2) zeta'(0) is the most UV-sensitive quantity (it involves all modes equally, weighted by ln|lambda|). The spectral action moments A_{2n} for large n probe the same UV tail. By studying zeta(s) for non-integer s (say, s = 1/2, 3/2, 5/2), we can interpolate between the well-behaved regime (large s, dominated by IR modes) and the UV-sensitive regime (small s, dominated by the UV tail). This interpolation is Tier 1 (exact on the truncated spectrum) and reveals how the q-theory crossing location tau* depends on the UV completion.

**Way forward 4: The independent geometric a_2.**

This has been flagged since the audit but remains uncomputed. The scalar curvature R(tau) of Jensen-deformed SU(3) was computed analytically in S20a from the Riemann tensor (147/147 checks). The geometric a_2 = (4pi)^{-4} * 16 * integral(R/6 * dV) can be computed in closed form from R(tau) and Vol(SU(3)) = 8 sqrt(3) pi^4 = 8480.67. Comparing this to the spectral a_2 = 2776.17 (at fold) quantifies the truncation error and tells us whether the 0.83-decade M_KK tension is a truncation artifact or a genuine structural feature.

This is the single most informative computation that has NOT been done. It costs nothing (purely analytic) and resolves the Tier 2 approximation quality question.

---

## VI. Ways Forward: Finite Crystal Spectral Geometry

**Way forward 5: The Connes distance on truncated SU(3).**

The Connes distance d(x,y) = sup{|f(x) - f(y)| : ||[D,f]|| <= 1} is the metric geometry of the spectral triple. On the full SU(3) with bi-invariant metric, the Connes distance reproduces the geodesic distance (Connes reconstruction theorem). On the truncated triple, it gives a DIFFERENT metric -- one that reflects the resolution limit of the finite crystal.

Computing d(e, g) for the identity e and a selection of group elements g in the Jensen-deformed metric would give:
- The effective diameter of the truncated SU(3) (how "large" the crystal looks at max_pq_sum = 5).
- The anisotropy of the Jensen deformation as seen by the truncated metric (is the B2 direction "shorter" than the B1 or B3 directions?).
- A Connes-distance analog of the spectral dimension that IS well-defined on the finite crystal.

This connects to the Connes-van Suijlekom 2021 program (Paper 28) on spectral truncations. The key result there is that truncated spectral triples define a sequence of increasingly refined "quantum metric spaces" converging (in the Gromov-Hausdorff sense) to the classical manifold. The rate of convergence depends on the spectrum, and the Jensen deformation may affect this rate differently in different directions.

**Way forward 6: Spectral form factor and eigenvalue correlations.**

The spectral form factor K(t) = |sum_k d_k e^{i lambda_k t}|^2 / (sum d_k)^2 probes the two-point correlations of the eigenvalue spectrum. For integrable systems (which the Jensen-deformed SU(3) is, by CHAOS-1), K(t) has a characteristic ramp-plateau structure whose details encode the symmetry class.

On the finite crystal, K(t) is Tier 1 (exact). The TRANSITION in K(t) between the short-time dip (governed by the spectral rigidity, related to the compressibility) and the long-time plateau (governed by the level spacing statistics) occurs at the Heisenberg time t_H ~ 2pi * bar(d) where bar(d) is the mean level spacing. This transition time is a natural scale in the finite crystal -- it is the spectral analog of the Planck time, being the shortest time at which the discrete nature of the spectrum becomes visible.

If the spectral form factor has non-trivial structure at the Heisenberg scale that varies with tau, this would provide a tau-dependent observable that is entirely intrinsic to the finite spectrum (no continuum extrapolation needed).

---

## VII. Ways Forward: The True Crossing at tau = 0.19104

DOS-FINE-SCAN-45 found a TRUE crossing of T3 ((0,0) max) and T5 ((2,0)+(0,2) min) at tau = 0.19104 with delta_min = 3.27e-5. This is a genuine level crossing, not avoided, because the two trajectories come from different SU(3) representations that do not couple.

In spectral geometry, true level crossings are topologically protected: the codimension of a crossing in the space of Hermitian matrices is 2 (for a generic crossing of two levels). On the 1-parameter family D_K(tau), crossings are generically avoided (codimension 1 suffices for eigenvalue repulsion). The fact that this crossing IS true tells us it is protected by a symmetry -- namely, the block-diagonal structure of D_K in Peter-Weyl sectors (S22b theorem).

**Way forward 7: Exploit the T3-T5 crossing for the CC.**

The q-theory crossing at tau* = 0.209 is 10.2% from the fold at tau = 0.190. The T3-T5 spectral crossing is at tau = 0.191, which is 0.5% from the fold. These are close but distinct.

The T3-T5 crossing is where the (0,0) singlet top eigenvalue and the (2,0)+(0,2) bottom eigenvalue coincide. This is precisely the boundary at which the singlet BCS gap equation changes character: below the crossing, the singlet top eigenvalue is below the non-singlet bottom (no level mixing even in BCS). Above it, they overlap. The BCS gap hierarchy -- which drove the q-theory crossing from 0.47 to 0.209 (FLATBAND scenario) -- may be LOCKED to this spectral crossing.

If the self-consistent BCS gap Delta(tau) has a discontinuity or rapid variation at the T3-T5 crossing (tau = 0.191), and if this feeds back into the q-theory Gibbs-Duhem condition, the q-theory crossing tau* could be PULLED to the spectral crossing at 0.191, which is 0.5% from the fold.

This is the most promising spectral-geometric route to tau-stabilization: not through the spectral action (closed, dimension zero), but through the eigenvalue topology feeding back into the BCS gap and through the q-theory self-tuning.

**Pre-registerable gate**: Q-THEORY-T3T5-46. Solve the self-consistent BCS gap equation Delta(tau) across the T3-T5 crossing at tau = 0.191. Does Delta(tau) have a discontinuity or kink? Does the q-theory crossing tau* lock onto tau = 0.191?

---

## VIII. What Is Well-Defined on the Finite Spectrum for n_s

The user asks directly: "What spectral-geometric quantities ARE well-defined on the finite spectrum that could encode n_s?"

The answer, after the audit, is narrow but non-empty:

1. **Spectral action moments A_{2n}(tau)**: These are Tier 1. Their tau-dependence is known and smooth. The ratio A_{2n}(tau_fold)/A_{2n}(tau=0) for successive n gives a sequence of numbers that encodes how the Jensen deformation redistributes the eigenvalue distribution. If this sequence has a characteristic power-law index, it could map to n_s.

2. **Eigenvalue velocities d lambda_k / d tau**: Tier 1 (computable from the known spectrum at multiple tau values). The distribution of velocities at the fold determines the perturbation spectrum from the transit. This is the spectral current j(lambda, tau) discussed in Section IV.

3. **The Connes distance anisotropy**: The Jensen deformation makes SU(3) anisotropic. The Connes distance in the B2 direction vs B1 vs B3 gives aspect ratios that are functions of tau. The RATE at which these aspect ratios change during the transit could generate a scale-dependent perturbation.

4. **The cyclic cohomology pairing**: Proven nondegenerate (OCCUPIED-CYCLIC-45). The Chern character ch^0 = Tr(e^{-beta D^2}) evaluated at different beta values gives a family of topological invariants that probe the spectrum at different scales. The beta-dependence of the pairing is a Tier 1 quantity.

5. **Eigenvalue counting function n_s**: The cumulative count N(lambda) defines an effective "spectral tilt" through its log-log derivative d(ln N)/d(ln lambda). This varies with lambda and could have a value near 0.965 at a specific lambda -- but there is no canonical choice of lambda for this purpose.

None of these immediately solves the n_s crisis. But they define the complete set of Tier 1 spectral quantities available for future attempts. Any n_s mechanism that uses Tier 2 or Tier 3 quantities (d_s, torsion, asymptotic SD expansion) is building on artifacts.

---

## IX. The Continuum Limit: The Last Open Door

Every closure in this session (UNEXPANDED-SA, SIGMA-SELECT, ANALYTIC-TORSION artifact) applies to the FINITE truncated spectrum. The continuum limit (max_pq_sum -> infinity) restores:
- Poles in the spectral zeta at s = 4, 3, 2, 1
- Asymptotic (not convergent) character of the SD expansion
- Genuine spectral dimension d_s -> 8 as sigma -> 0
- Regulated analytic torsion (finite, computable from root system data for bi-invariant metric)

The Taylor expansion exactness theorem becomes FALSE in the continuum: the SD expansion diverges, and the full spectral action contains non-perturbative information beyond any polynomial approximation.

This means that the CC hierarchy, which is O(1) at finite truncation (A_4/A_2 = 2.76), could in principle become large in the continuum limit if the UV tail generates large corrections to A_4 relative to A_2. The Weyl law tells us that at large lambda, d_k ~ lambda^{d-1} ~ lambda^7, so the k-th moment diverges as A_{2k} ~ integral(lambda^{2k+7} d lambda). The ratio A_{2(k+1)}/A_{2k} ~ lambda_max^2 -> infinity, generating a hierarchy.

**Way forward 8: Formal moment ratios in the Weyl regime.**

For the full SU(3) Dirac spectrum with Weyl asymptotics N(lambda) ~ C lambda^8, the moment ratio is:

A_{2(k+1)} / A_{2k} = integral(lambda^{2k+2+7} d lambda) / integral(lambda^{2k+7} d lambda)

With a physical UV cutoff at lambda = Lambda, this gives A_{2(k+1)}/A_{2k} ~ Lambda^2. For Lambda ~ M_KK, this is O(1) in natural units. But for Lambda ~ M_Pl, it gives (M_Pl/M_KK)^2 ~ 10^4. The CC hierarchy of 10^{36} per step would require Lambda^2 ~ 10^{36}, i.e., Lambda ~ 10^{18} M_KK ~ 10^{34} GeV -- a trans-Planckian scale.

This is not viable as stated, but it shows that the moment hierarchy IS connected to the UV cutoff scale. In the q-theory framework, where the UV cutoff is not imposed by hand but emerges from the vacuum self-tuning, the effective Lambda may be set by the q-theory equilibrium condition itself. This would close the loop: the CC hierarchy emerges from the self-consistent UV scale of the q-theory.

---

## X. Constraints Map Update (Spectral Geometry View)

**New walls (S45)**:
1. Taylor expansion exactness on finite spectrum (S45-S1)
2. Heat kernel classification: Tiers 1/2/3 (S45-S13)
3. Spectral action dimension zero for tau-stabilization (31 closures cumulative)
4. EIH k-mapping uniqueness (S45-S2) -- removes k-mapping ambiguity forever

**Surviving region**:
- CC: q-theory + BCS, with tau* = 0.209 (OPEN, first PASS)
- n_s: NEAR-ZERO dimension. Spectral current j(lambda, tau) untested. Hose-count untested. Continuum limit untested
- DM/DE: Zubarev alpha = 0.410 (INFO, pending derivation)
- w_0 = -0.709 (falsifiable by DESI DR2/3)

**Closed regions**:
- Spectral action tau-stabilization: all directions, all cutoffs, both vacuum and occupied. PERMANENT
- d_s as dimension diagnostic: ARTIFACT on finite crystal. PERMANENT
- Analytic torsion for CC: ARTIFACT of truncation. PERMANENT
- Bogoliubov/KZ for n_s: all k-mappings, all gap values, n_s ~ -4.5. PERMANENT

**Next gates (spectral geometry priorities for S46)**:
1. Independent geometric a_2 from Jensen metric R(tau): purely analytic, quantifies Tier 2 error
2. Q-THEORY-T3T5-46: does the spectral crossing at 0.191 lock the q-theory crossing?
3. Spectral current j(lambda, tau) for n_s (Way Forward 2)
4. max_pq_sum = 6 computation to test d_Weyl convergence toward 8
5. Connes distance on truncated Jensen SU(3) (Way Forward 5)

---

## XI. The Puzzle Piece from Spectral Geometry

The user asks each discipline to provide its piece. Here is spectral geometry's.

The finite crystal is NOT a truncated manifold. It is a noncommutative geometry in its own right, with its own metric (Connes distance), its own topology (cyclic cohomology, proven nondegenerate), and its own dynamics (spectral action, exact). The error of the last 10 sessions was treating it as an imperfect approximation to the continuum and applying continuum formulas (d_s, torsion) that require structure the finite crystal does not possess.

The correct approach treats the finite truncation as the PHYSICAL object and asks what geometry it defines. The answer is given by the Connes reconstruction program at finite level:
- The algebra A is the space of functions on SU(3) truncated to PW harmonics up to max_pq_sum = 5.
- The Hilbert space H is the 6440-dimensional spinor space.
- The Dirac operator D_K is the 6440 x 6440 matrix with known eigenvalues.
- The metric, curvature, volume, and all geometric invariants are defined through the spectral action and the cyclic cohomology pairing -- both Tier 1.

In this picture, the "spectral dimension" is not d_s(sigma) (an artifact) but d_Weyl = 6.81 (the Weyl counting exponent). The "analytic torsion" is not exp(-zeta'(0)/2) (an artifact) but the product of eigenvalues in the singlet sector, T_singlet = 0.147 (a partial product that converges as the truncation grows). The "CC hierarchy" is not A_4/A_2 at finite truncation (O(1)) but the ratio that emerges in the continuum limit as the spectral zeta develops poles.

The path forward requires computing the geometry of the finite crystal AS a finite crystal: Connes distance, spectral form factor, eigenvalue current under deformation. These are the tools that match the object. Using them may reveal structure that continuum formulas, applied to a discrete spectrum, systematically miss.

---

*Filed as Session 45 Collaborative Review, Spectral-Geometer perspective. All results referenced to specific npz files and session computations. 8 ways forward identified with pre-registerable gates for 2 of them.*
