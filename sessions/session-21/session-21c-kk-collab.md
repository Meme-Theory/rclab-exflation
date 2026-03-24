# Kaluza-Klein -- Collaborative Feedback on Session 21c

**Author**: Kaluza-Klein Theorist
**Date**: 2026-02-19
**Re**: Session 21c Phase 0 Results

---

## Section 1: Key Observations

### 1.1 The Dual Algebraic Trap is a Structure Theorem about Kerner's Decomposition

The session's central negative result -- that F/B = 4/11 and b_1/b_2 = 4/9 are tau-independent, representation-theoretically exact -- is not merely an empirical observation from computation. It is a theorem about the structure of Kerner's decomposition (Paper 06, eq 26-30: R_bundle = R_K + (1/4) g_{ab} F^a F^b) when specialized to the SU(3) -> SU(2) x U(1) maximal subgroup embedding.

The key point a generalist would miss: **both traps have a single geometric root in the Dynkin embedding index**. Kerner's eq 25 gives the Yang-Mills equations from the higher-dimensional vacuum Einstein equations. The structure constants that appear in those equations -- which are the same structure constants entering the branching coefficients b_1, b_2 -- are fixed by the Lie algebra embedding, not by the metric. The Jensen deformation changes the metric on the fiber but preserves the Lie algebra structure. Therefore no metric deformation, however ingenious, can alter these ratios. The trap is a theorem about the fiber's algebraic structure, not its geometric state.

This is exactly the structural rigidity that Witten encountered from the other direction (Paper 09): the difficulty of getting chiral fermions from KK is also a structure theorem about the relationship between curvature and index on compact symmetric spaces. Both positive curvature closing the Dirac index (Witten) and fixed branching ratios closing spectral sums (Session 21c) are manifestations of the same underlying constraint: the representation theory of the structure group is too rigid for perturbative mechanisms to break.

### 1.2 T''(0) Escapes Because It Probes the Connection, Not the Curvature

The derivative escape theorem (Session 21c, Theorem 2) has a precise geometric interpretation in the KK framework that was not stated in the session minutes. The eigenvalue magnitudes that enter Casimir, CW, and S_signed sums are controlled by the **Ricci curvature** of the internal space (via the Lichnerowicz formula D^2 = nabla*nabla + R/4, Paper 09 / Paper 11 eq 21). Ricci curvature on a group manifold with invariant metric is determined by the structure constants and the metric components -- and the ratio between different components is what the algebraic traps freeze.

But the eigenvalue **derivatives** d lambda_n / d tau depend on the **connection coefficients** Gamma^a_{bc}(tau) and their variation with tau. While the Christoffel symbols are determined by the metric, their *tau-derivatives* involve how the metric components change relative to each other -- a second-order geometric quantity that is NOT frozen by the branching ratios.

In DeWitt's language (Paper 05, heat kernel expansion), the eigenvalue magnitudes appear in the Seeley-DeWitt coefficients a_0, a_2, a_4 (which are polynomial in curvature), while the eigenvalue flow depends on the **variation** of these coefficients with the deformation parameter. The algebraic traps constrain the coefficients; they do not constrain the derivatives of the coefficients.

This is why T''(0) is genuinely new information, and why the synthesis correctly classified it as COMPELLING rather than DECISIVE: it tells us the self-consistency map has the right concavity, but does not locate the fixed point.

### 1.3 The Three-Monopole Structure is a Squashing Analog

The Berry curvature monopole structure (M0 at tau=0, M1 at tau ~ 0.10, M2 at tau ~ 1.58) has a direct analog in the Duff-Nilsson-Pope squashed S^7 program (Paper 11). In the S^7 case, the round metric (maximum symmetry SO(8)) has exact degeneracies that split under squashing. The squashing parameter lambda plays the role of tau, and the level crossings as a function of lambda define topological phases of the spectrum.

Critically, DNP showed that the round S^7 is a conical intersection point in the moduli space -- exactly as M0 at tau=0 in our SU(3) case. Their stability analysis (eq 22: lambda_L >= 3m^2) was conducted at the round metric precisely because it is the maximally symmetric point where degeneracies concentrate. The fact that our (0,0)/(1,1) degeneracy at tau=0 mirrors the SO(8) degeneracies at the round S^7 is not coincidence -- it is the universal behavior of eigenvalue spectra at maximally symmetric points of compact homogeneous spaces.

The interval [0, 1.58] where (0,0) controls the gap edge is analogous to the squashing window in DNP where specific Killing spinor sectors control the ground state. This structural parallel strengthens the physical interpretation of the monopole structure.

---

## Section 2: Assessment of Key Findings

### 2.1 S_signed STRUCTURAL CLOSURE: Sound and Final

The b_1/b_2 = 4/9 identity is algebraically irrefutable. I confirmed this independently during Phase B (see session21c_results.md in agent memory): the ratio is Tr(Y^2)/Tr(T_a^2) = (2/3)/(3/2) = 4/9 on the fundamental representation, and propagates to all representations by Schur's lemma applied to the SU(3) -> SU(2) x U(1) branching rules. This means Delta_b = b_1 - b_2 = -(5/9) b_2 < 0 for every irreducible representation (p,q).

**Caveat that must be stated explicitly**: this result is specific to the **standard embedding** SU(3) -> SU(2) x U(1) where U(1) is the hypercharge direction in the Cartan subalgebra. A non-standard embedding (e.g., SU(3) -> SO(3) or SU(3) -> U(1) x U(1)) would give different branching ratios. The session synthesis acknowledged this (escape condition (b) in Theorem 1) but did not emphasize that this means the algebraic trap is a property of the **embedding choice**, not of SU(3) itself. The embedding is fixed by the requirement to reproduce the SM gauge group, so within the phonon-exflation framework the trap is inescapable, but a theorist proposing a different internal manifold with a different gauge group embedding would not face the same constraint.

### 2.2 T''(0) = +7,969: Sound Sign, Uncertain Magnitude

The sign is structurally robust: it arises from the product of two negatives (Delta_b < 0 and log-concavity of eigenvalue flow d^2 ln|lambda|/dtau^2 < 0 on average). The 89% UV dominance is a concern for phenomenological relevance but does not undermine the mathematical result.

**The UV dominance has a KK-theoretic explanation**: in Kaluza-Klein theory, the UV modes are the high KK harmonics (large p+q). These modes have the largest Casimir eigenvalues and therefore the most curvature from the Jensen deformation. They dominate any polynomial weighting of eigenvalues. This is the same reason that the Seeley-DeWitt expansion (Paper 05, heat kernel a_n coefficients) is dominated by the highest-order curvature terms at small t -- it is a short-distance (UV) effect.

The physically relevant question for T''(0) is whether the sign remains positive when restricted to the IR sector (low p+q). The session notes that IR modes contribute only 0.3% (23.7/7969). This is not alarming in itself -- the IR contribution is small because there are few low modes -- but it means P1-0 (delta_T zero-crossing) is the decisive next step, not further refinement of T''(0).

### 2.3 V_IR Minimum at N=50: Unreliable but Not Dismissible

The coupling/gap ratio of 4-5x at the lowest modes (baptista's quantification) means the block-diagonal basis is genuinely broken for the lowest eigenvalues. The N=50 minimum at tau=0.15 with 0.8% depth falls squarely within the uncertainty band of O(100%) for the lowest modes.

From the KK perspective, this is the regime where inter-sector coupling (Kosmann-Lichnerowicz mixing between different SU(3) representations) is strongest. Paper 11's stability analysis (eq 22) was conducted in the coupled basis from the start, precisely because the round S^7 has exact degeneracies where block-diagonal treatment would be meaningless. The fact that the phonon-exflation computation has not yet been done in the coupled basis at the lowest modes is a genuine gap, and baptista is correct that coupled V_IR (P1-2) is the highest-information computation available.

### 2.4 Neutrino INCONCLUSIVE: Correct Classification

The R = 32.6 crossing at tau = 1.556 from a Berry curvature monopole is a geometric artifact. The delta_tau ~ 4e-6 window requiring fine-tuning of 1:10^5 is physically unacceptable. This is the standard behavior near a conical intersection (Paper 11 calls these "space invaders" -- massive modes descending to zero mass at special points). The function R(tau) must pass through 32.6 near a pole, just as any continuous function passes through any value near a singularity. This is not a prediction; it is a topological triviality.

The correct physical prediction would require R crossing 32.6 on a smooth branch away from any monopole, in a tau-window consistent with other observables (e.g., the Weinberg angle at tau = 0.30 or the V_eff minimum). No such crossing exists in the computed data.

---

## Section 3: Collaborative Suggestions

### 3.1 delta_T(tau) Zero-Crossing (P1-0) -- Computational Specification

I wrote preliminary code for this during Phase B (file: `tier0-computation/s21c_kk_verify.py`), which the synthesis notes was not run to completion. The computation is straightforward:

delta_T(tau) = -(1 / (64 pi^2 e^{4 tau})) * Sum_{(p,q)} Delta_b(p,q) * Sum_n ln(lambda_n(tau)^2)

All ingredients exist: Delta_b = -(5/9) b_2 from branching rules (computed), lambda_n(tau) from tier1_dirac_spectrum.py sweep data (21 tau-values, stored). The computation is a pure post-processing step.

**Expected behavior from KK theory**: At tau=0 (round SU(3)), the Freund-Rubin solution (Paper 10) gives a maximally symmetric vacuum. delta_T(0) should have a definite sign. As tau increases, the Jensen deformation breaks the symmetry and the eigenvalue spectrum evolves. A zero-crossing of delta_T at some tau_0 would correspond to the self-consistency condition where the spectral back-reaction balances the geometric deformation.

**Connection to Freund-Rubin (Paper 10)**: The FR balance condition (eq in Paper 10: R_{mu nu} = -12 m^2 g_{mu nu}, R_{mn} = +6 m^2 g_{mn}) is the classical analog of delta_T = 0. In both cases, the internal geometry adjusts until a balance condition is satisfied. The FR condition is at the level of the Einstein equations (classical); delta_T = 0 is at the level of the one-loop effective action (quantum). They probe the same geometric question at different loop orders.

**Pre-registered prediction**: delta_T should have a zero in [0.15, 0.50]. If it does not, the self-consistency route closes and the framework drops to ~35%. The prediction is motivated by the FR minimum at tau = 0.30 (from the 21b Cartan flux analysis) and the Weinberg angle match at tau = 0.2994.

### 3.2 Gauge Coupling Running as the Correct Observable for the e^{-4 tau} Identity

The CP-1 post-mortem (Section VII of the synthesis) noted that the flux-threshold algebraic identity (Cartan flux channel = U(1) gauge threshold correction) survives, but S_signed was the wrong test because Delta_b has uniform negative sign.

I propose that the correct observable is the **running of the U(1) gauge coupling with tau**, not the signed spectral sum. The e^{-4 tau} factor in the Cartan 3-form norm (see session21b_cartan_flux.md: ||omega_3||^2 has a (C^2, C^2, u(1)) component scaling as e^{-4 tau}) directly enters the U(1) gauge coupling through the KK relation (Paper 06, eq 26-30; Baptista eq 3.76-3.78):

g_1^2(tau) ~ 1 / Vol_{u(1)}(tau) ~ e^{-2 tau}

but the threshold correction to g_1^2 involves the one-loop determinant weighted by the e^{-4 tau} Cartan channel. The specific computation is:

delta(1/g_1^2) = (1 / 16 pi^2) * Sum_n b_1(n) * ln(lambda_n^2 / mu^2)

where b_1(n) are the U(1) beta-function coefficients for each KK mode. This is a DIFFERENT sum from S_signed -- it uses b_1 alone, not b_1 - b_2. Since b_1 > 0 for all sectors, this sum has definite positive sign, and its tau-dependence inherits the e^{-4 tau} structure from the U(1) channel.

**Cost**: Zero -- uses existing eigenvalue data and already-computed b_1 coefficients.
**Expected outcome**: A running g_1(tau) that varies by O(1) over the physical window, with the e^{-4 tau} decrease visible in the lowest modes.
**Physical content**: If g_1(tau) has a feature (inflection, crossing with g_2(tau), etc.) at tau ~ 0.12, this would vindicate the CP-1 algebraic identity through a physically meaningful observable.

### 3.3 Scalar Laplacian for V_IR Bosonic Modes

The V_IR computation (P0-1) used bosonic data at only 4 tau values (berry's data constraint noted in the cross-pollination log). The scalar Laplacian on Jensen SU(3) has an explicit formula I derived in Session 17:

Delta_0 = -e^{-2 tau}/alpha * rho(e_7)^2 - e^{2 tau}/alpha * Sum_{a=0}^{2} rho(e_a)^2 - e^{-tau}/alpha * Sum_{a=3}^{6} rho(e_a)^2

This is diagonal in the Peter-Weyl basis and computable from existing representation matrices rho(e_a) stored by tier1_dirac_spectrum.py. The eigenvalues can be computed at all 21 tau-values in minutes, giving a dense bosonic V_IR curve to compare with the fermionic one.

**Connection to Einstein-Bergmann (Paper 04)**: The scalar Laplacian eigenvalues are the KK mass tower -- Paper 04's m_n = |n|/R generalized to the non-abelian case. Computing this at all tau values gives the complete bosonic mass spectrum as a function of the Jensen deformation, filling the gap in berry's V_IR data.

### 3.4 Coupled Diagonalization Should Use the Adjoint Sector First

For the coupled V_IR computation (P1-2), I recommend starting with the (1,1) adjoint sector. At tau=0, the (0,0) and (1,1) sectors are exactly degenerate (both eigenvalues = sqrt(3)/2 = 0.866, from the M0 conical intersection at tau=0). The coupling between them is first-order (direct Kosmann-Lichnerowicz connection: (0,0) x (1,1) = (1,1)). This means the adjoint sector is where off-diagonal coupling has its LARGEST effect.

If the coupled diagonalization shifts the (0,0)/(1,1) eigenvalues at tau=0 by a measurable amount, the gap structure changes qualitatively in the vicinity of M0, and the BCS bifurcation point M1 may shift. If the shift is small (< 1%), the block-diagonal treatment is validated for this sector, and the coupling uncertainties on V_IR are accordingly bounded.

**Technical note**: The (1,1) adjoint has dim = 8, giving a 16 x 16 D_K block (with the C^16 spinor space). The coupled (0,0) + (1,1) block is 2 + 16 = 18 spinor components, giving a 18 x 18 matrix. This is trivially diagonalizable and serves as a pilot computation before tackling the full coupled basis.

### 3.5 beta/alpha from First Principles -- The Decisive KK Computation

The Freund-Rubin double-well (Session 21b, my B-2 deliverable) predicts a minimum at tau_0 = 0.30 if beta/alpha = 0.28. The session 21c synthesis correctly identifies beta/alpha from the 12D action as a Tier 2 computation (P2-3), but I want to emphasize that this is the single highest-value computation in the entire pipeline, not just for the V_eff question but for the framework as a whole.

The reason: beta/alpha is determined by the ratio of the Einstein-Hilbert normalization to the Chern-Simons 3-form normalization in the 12D action. In the Freund-Rubin ansatz (Paper 10), this ratio is parameter-free -- it comes from the 11D supergravity action where the coefficient of F^2 relative to R is fixed by supersymmetry. In the phonon-exflation framework (12D, no SUSY), the analogous coefficient comes from the spectral action (Connes Paper 07, a_4 coefficient):

beta/alpha = f_0 * a_4^{(flux)} / (2 * f_2 * a_2^{(grav)})

where f_0, f_2 are moments of the spectral function f in S = Tr f(D^2 / Lambda^2). The a_n coefficients are computable from the Seeley-DeWitt expansion (Paper 05) on the Jensen SU(3) geometry.

If beta/alpha = 0.28 +/- 0.05 from this computation: **the Weinberg angle is a zero-parameter prediction**, upgrading the framework probability by +18-22 pp (the synthesis estimate). If beta/alpha >> 0.313: the FR minimum is at tau=0 (round SU(3)), and the Weinberg angle prediction fails. If beta/alpha << 0.15: the FR minimum is at tau > 0.5, too far from the Weinberg angle value.

**This computation does not require eigenvector extraction**. It uses only the Seeley-DeWitt coefficients a_0, a_2, a_4 evaluated on Jensen SU(3), which are polynomial functions of the curvature tensor components (already computed to machine epsilon in Sessions 17b and 20a).

---

## Section 4: Connections to Framework

### 4.1 The Perturbative Completeness Theorem

Session 21c establishes what I would call the **Perturbative Completeness Theorem** for the phonon-exflation framework: all perturbative spectral stabilization routes on (SU(3), g_Jensen) with standard SU(3) -> SU(2) x U(1) embedding are algebraically closed.

The complete list, traced through the KK literature:

| Mechanism | KK Paper Origin | Session Closed | Closure Mechanism |
|:----------|:---------------|:---------------|:---------------|
| V_tree (classical Einstein) | FR (10), DNP (11) | 17a | Monotonic R_K(tau) |
| 1-loop CW (DeWitt) | DeWitt (05) | 18 | F/B = 8.4:1, Trap 1 |
| Casimir scalar+vector | DeWitt (05) | 19d | F/B = 9.9:1, Trap 1 |
| Seeley-DeWitt a_2/a_4 | DeWitt (05) | 20a | SD coefficients monotonic |
| Casimir with TT 2-tensors | DNP (11) eq 21-22 | 20b | R = F/B = 0.55 constant |
| Signed gauge-threshold sums | Kerner (06) | 21c | b_1/b_2 = 4/9, Trap 2 |

Every entry in this table traces directly to a KK paper in the reference corpus. The perturbative toolkit of KK theory -- Einstein equations, heat kernel, Lichnerowicz operator, gauge thresholds -- has been systematically applied and exhausted.

### 4.2 What Survives is What Kerner and Witten Could Not Compute

The surviving routes -- BCS condensate, Freund-Rubin double-well, topological transitions -- are precisely the non-perturbative phenomena that the classical KK literature identified but could not compute:

- **Kerner (Paper 06)** derived the Yang-Mills equations from the bundle curvature but could not analyze the quantum vacuum (no effective action technology in 1968).
- **Witten (Paper 09)** identified the chirality obstruction but could not resolve it (no NCG spectral triple technology in 1981).
- **Freund-Rubin (Paper 10)** showed flux can drive compactification but could not compute the one-loop corrections to the flux potential.
- **Duff-Nilsson-Pope (Paper 11)** analyzed squashed S^7 stability at the classical level but deferred quantum corrections.

The phonon-exflation framework has now closed the perturbative chapter that these authors opened. What remains is the chapter they could not write: the non-perturbative quantum dynamics of the internal geometry.

### 4.3 The Two-Monopole Structure and Klein's Quantization

The two-monopole structure (M1 at tau ~ 0.10, M2 at tau ~ 1.58) with M0 at tau = 0 has an elegant connection to Klein's original quantization argument (Paper 03, eq 44-50). Klein showed that periodic boundary conditions on the compact dimension quantize charge. In the non-abelian generalization, the eigenvalues of D_K on SU(3) play the role of the quantized charges.

The Berry curvature monopoles are points where two eigenvalue branches exchange -- i.e., where the "charge" assignment (which representation controls the gap) switches. In Klein's language, this is a rearrangement of the charge spectrum. The physical window [0, 1.58] is the domain where the charge spectrum has a specific hierarchical structure (singlet at the gap edge, fundamental above), and the monopoles are the domain walls of this structure.

This connects directly to the Z_3 triality of the crossing sectors ((0,0) has Z_3 = 0; (1,0) has Z_3 = 1). The Berry curvature monopole at tau = 1.58 is not just an eigenvalue crossing -- it is a **triality-changing transition**, where the lightest excitation of the internal space changes its generation quantum number.

---

## Section 5: Open Questions

### 5.1 Is There a Witten-Type No-Go Theorem for Non-Perturbative Stabilization?

Witten showed (Paper 09) that chiral fermions cannot arise from positively curved compact spaces via the index theorem. This closed the naive KK program for decades. The phonon-exflation framework resolved this specific obstruction via KO-dim = 6 (NCG spectral triple).

The dual algebraic trap (Theorem 1 of Session 21c) is the V_eff analog of Witten's chirality obstruction: a representation-theoretic no-go for perturbative stabilization. **Is there a corresponding no-go theorem for non-perturbative stabilization?** Specifically:

- Can the BCS condensate mechanism be closed by an algebraic argument analogous to Trap 1 or Trap 2?
- Does the Freund-Rubin double-well survive when quantum corrections are included, or does the algebraic trap extend to the flux sector?
- Is there a topological obstruction to the Pfaffian sign change needed for Trap 1 escape?

If such a no-go theorem exists, it would constitute a DECISIVE closure at the structural level, reducing the framework probability to < 25%. If it can be shown that NO such theorem exists (i.e., that the non-perturbative routes are algebraically free), that would be a significant positive result.

### 5.2 Does the DNP Stability Bound Apply to Jensen SU(3)?

Paper 11, eq 22 states the stability condition lambda_L >= 3m^2 for the Lichnerowicz operator on TT 2-tensors. Session 20b computed the Lichnerowicz spectrum and found all eigenvalues positive -- but this was for the Casimir energy, not for the Freund-Rubin stability condition.

The FR stability condition requires knowing the relationship between the Lichnerowicz eigenvalue lambda_L and the Freund-Rubin mass parameter m^2 = |F|^2/(12 * Vol^2). In the standard DNP analysis, m is determined by the flux. In our framework, m would be determined by the Cartan 3-form norm ||omega_3||^2(tau), which I computed exactly in Session 21b.

**Question**: Does lambda_L(tau) >= 3 m^2(tau) hold for all tau in [0, 2], where m^2(tau) is the Freund-Rubin mass from the Cartan 3-form? If not, there exists an instability window -- which is precisely the non-perturbative mechanism the framework needs.

This is a zero-cost computation using existing data: lambda_L from Session 20b (`l20_TT_spectrum.npz`) and ||omega_3||^2(tau) from Session 21b. It directly tests whether the DNP stability machinery, when applied to Jensen SU(3) with the actual flux, produces a violation that could seed a non-perturbative transition.

### 5.3 What is the Physical Origin of the 89% UV Dominance in T''(0)?

The fact that 89% of T''(0) = 7,969 comes from UV modes (p+q = 5-6) demands a physical explanation, not just a numerical observation. In the Seeley-DeWitt framework (Paper 05), UV modes dominate heat kernel traces because K(t, x, x) ~ t^{-d/2} at small t. The eigenvalue derivative d^2 lambda_n / d tau^2 grows with the Casimir (hence with p+q) because higher representations are more sensitive to the metric deformation -- they "sample" the geometry at shorter wavelengths.

But physically, the self-consistency condition for the modulus tau is an IR question: does the vacuum energy have a minimum? If the UV modes determine the sign of T''(0) but the IR modes determine whether a minimum actually exists, there is a potential disconnect. The delta_T(tau) computation (P1-0) addresses this directly by asking whether the full self-consistency map -- including both UV and IR contributions -- has a zero-crossing.

The deeper question: **does the UV/IR decomposition of T''(0) correspond to a physical separation of scales?** In effective field theory, the UV modes would be integrated out, contributing to Wilson coefficients that govern the IR dynamics. If the IR Wilson coefficients have the wrong sign (despite T''(0) > 0 overall), the self-consistency route could fail at the physical scale while passing at the formal level.

---

## Closing Assessment

Session 21c represents the clean completion of the perturbative spectral program. The dual algebraic trap is a genuine mathematical theorem -- it should be publishable independent of the framework's ultimate fate. T''(0) > 0 is the single perturbative quantity that escapes both traps, and the derivative escape theorem explains why: dynamics (eigenvalue flow geometry) is algebraically richer than statics (eigenvalue magnitudes).

The three-monopole structure organizes the phenomenological features of the Dirac spectrum into a coherent topological picture that mirrors the squashed S^7 program of Duff-Nilsson-Pope. This is precisely the kind of structural parallel that gives confidence: the same mathematics that works for S^7 compactification in 11D supergravity is operating on SU(3) with Jensen deformation.

**Framework probability**: 40-48%, median 43%. I concur with the coordinator's BETA-2 classification. The perturbative program is done. The framework now lives or dies on non-perturbative physics: delta_T zero-crossing, coupled V_IR, beta/alpha from the 12D action, and ultimately the BCS gap equation.

**The decisive next computation is P1-0 (delta_T zero-crossing), followed closely by P2-3 (beta/alpha).** These two computations together determine whether the framework's non-perturbative routes have the correct geometry to produce a physical vacuum. If both pass, the framework enters GAMMA territory (55-70%). If both fail, it drops to ~30%.

The perturbative Kaluza-Klein program on SU(3) is now a closed book. Every page has been turned, and every mechanism has been tested. What remains is the chapter that Kaluza, Klein, Kerner, Witten, and Duff could not write: the non-perturbative quantum geometry of the compact fiber. The tools exist. The computation is feasible. The answer is weeks away.

---

*Filed by Kaluza-Klein Theorist, 2026-02-19. Cross-references: Papers 05 (DeWitt), 06 (Kerner), 09 (Witten), 10 (Freund-Rubin), 11 (Duff-Nilsson-Pope) from the KK collection. Session memory: session21c_results.md, session21b_cartan_flux.md, session20b_lichnerowicz.md.*
