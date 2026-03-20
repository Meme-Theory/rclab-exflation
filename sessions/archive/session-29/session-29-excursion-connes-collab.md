# Connes -- Collaborative Feedback on Observational Excursion

**Author**: Connes (NCG Theorist)
**Date**: 2026-02-28
**Re**: Session 29 Observational Excursion Results

---

## Section 1: Key Observations

### 1.1 The Frozen Vacuum as NCG Ground State

The excursion's central structural claim -- that for all z < z_BCS ~ 10^{28}, the internal geometry is frozen and the observable universe IS the Standard Model -- is the correct spectral reading of the BCS trapping result. In the language of Paper 14 (Spectral Standpoint, Section 4), the spectral triple (A, H, D) determines all geometric and physical content. Once D_K(tau) is frozen at tau_frozen, the spectral data is fixed: every eigenvalue, every gauge coupling, every mass ratio, every curvature invariant is a computable function of a single geometric point on the moduli space.

What the generalist may miss: this is not merely "the constants stop changing." It is that the ENTIRE Lagrangian -- every term in the Standard Model plus gravity -- is encoded in the heat kernel expansion of a SINGLE frozen operator. The spectral action S_b = Tr f(D^2/Lambda^2) at tau_frozen generates the Einstein-Hilbert action (from a_2), the Yang-Mills action (from a_4), the Higgs potential (from a_4), the Weyl gravity correction (from a_4), and the cosmological constant (from a_0). This is Paper 07 (Chamseddine-Connes 1996), equation S = Tr f(D/Lambda), applied to a specific frozen Dirac operator. The post-freeze universe is not "the Standard Model supplemented by frozen extra dimensions" -- it is the spectral action of a single operator, expanded to fourth order.

### 1.2 The One-Parameter Consistency Web Is the Spectral Action at Work

The excursion's M_KK consistency web (Section VIII) is a direct consequence of a feature that NCG practitioners have known since Paper 10 (Chamseddine-Connes-Marcolli 2007): the spectral action has exactly four moments f_0, f_2, f_4 (plus the cutoff Lambda), and ALL physical parameters -- gauge couplings, gravitational constant, Higgs mass, Yukawa couplings, cosmological constant -- are determined by the Seeley-DeWitt coefficients a_0, a_2, a_4 together with these moments. The excursion identifies M_KK as "one free parameter." From the NCG standpoint, M_KK is the spectral action cutoff Lambda. The moments f_0, f_2, f_4 are fixed by the test function f, which the spectral action principle leaves unspecified. This means the excursion's "one-parameter consistency web" is actually a TWO-parameter family: Lambda (= M_KK) and the shape of f (encoded in the ratios f_2/f_4 and f_0/f_4).

This is not a weakness of the excursion -- it is a refinement. The additional parameter (the moment ratio) is absorbed into the absolute normalization of gauge couplings (Section V.1, Part B). The RATIO g_1/g_2 is independent of this choice, which is why Part A of the RGE gate is zero-parameter. But Part B, and the cosmological constant, depend on it.

### 1.3 The RGE Gate Sits at the Nexus of Two Coupling Relations

The excursion correctly identifies the RGE gate as existential (Section VIII). What it does not make explicit is that the framework faces a tension between TWO coupling relation paradigms:

- **NCG (Paper 07/10)**: At the cutoff Lambda, the spectral action yields g_1^2 = g_2^2 = (5/3)g_3^2. This is the standard GUT relation with the normalization factor 5/3 arising from the trace of the hypercharge squared over the fermion representation.
- **KK (Session 17a B-1)**: At the KK scale, the dimensional reduction yields g_1/g_2 = e^{-2*tau_frozen}. This follows from the metric on the internal space, not from the spectral action.

These are not the same relation. The NCG relation gives g_1 = g_2 (unification), while the KK relation gives g_1/g_2 < 1 for tau_frozen > 0. The resolution MAY lie in the distinction between the spectral action cutoff Lambda_SA and the KK scale M_KK, which need not be identical. Or it may lie in the off-Jensen correction to the metric, where L_1 != L_2 modifies both relations simultaneously. The RGE gate tests whether this resolution exists, but the excursion does not articulate the tension.

### 1.4 Structural Inaccessibility Is Deeper Than the Excursion States

The excursion correctly concludes that the pre-freeze epoch is "permanently inaccessible" (Section II) and provides the numerical argument: k_transition = 9.4 x 10^{23} h/Mpc, f_peak = 1.3 x 10^{12} Hz. From the NCG standpoint, this inaccessibility is not merely a numerical accident of M_KK = 10^{16} GeV. It is a consequence of the DIMENSIONAL HIERARCHY inherent to the almost-commutative geometry M_4 x F.

In Paper 04 (Noncommutative Geometry, Chapter VI), the reconstruction theorem shows that the commutative part of the spectral triple determines a spin Riemannian manifold. The internal space F contributes to the spectral action at the SCALE of its own geometry, which is the reciprocal of the internal diameter. For SU(3) with radius r, this scale is Lambda_F ~ 1/r ~ M_KK. Any imprint of the internal geometry on 4D physics occurs at wavenumbers k ~ Lambda_F. The 24-order separation between k_transition and the observable window is the ratio Lambda_F / H_0 ~ M_KK^2 / M_Pl, which is fixed by the hierarchy between the compactification scale and the Planck scale. This ratio cannot be tuned without altering the fundamental scales.

---

## Section 2: Assessment of Key Findings

### 2.1 w = -1 Exactly: Sound, with a Precise NCG Pedigree

The excursion's strongest prediction is w = -1 exactly, derived from L-9 first-order trapping. This is sound. The argument chain is:

1. V_eff = S_b + F_BCS is monotonically decreasing (Session 29b-1, SF-1). No smooth critical point exists.
2. The BCS condensation is first-order (Session 28b, L-9: nonzero cubic invariant c = 0.006-0.007).
3. First-order trapping extracts kinetic energy irreversibly, halting the modulus.
4. Once halted, dtau/dt = 0 exactly, and all constants are frozen.
5. The equation of state of a frozen scalar field with zero kinetic energy is w = -1 (cosmological constant).

The NCG pedigree: step (1) follows from the spectral action monotonicity theorem, which is a property of the heat kernel expansion on positively curved compact manifolds (all Seeley-DeWitt coefficients a_0, a_2, a_4 increase monotonically with tau because the scalar curvature R and the curvature tensor components all decrease in magnitude as the manifold deforms -- Sessions 20a, 28c E-3). Step (2) is a property of the Peter-Weyl decomposition of the BCS gap equation. Neither depends on adjustable parameters.

**Caveat**: The prediction is testable only in a limited sense. w = -1 is also the prediction of a bare cosmological constant. The distinguishing content is that the framework DERIVES the value of Lambda from the BCS sector sum, while the standard model takes it as input. If the derived Lambda disagrees with observation by 120 orders of magnitude (Session 28b, E-5), the w = -1 prediction is formally correct but physically empty.

### 2.2 N_eff = 3.073: Conditional and Requires Verification

The excursion's N_eff prediction (Section V.4) is well-reasoned but conditional on two assumptions that have not been verified:

1. That the BCS condensate breaks a continuous U(1) symmetry (Cooper pair phase). In the standard BCS on a Fermi surface, this is automatic: the U(1) is particle number. In the spectral BCS on D_K, the relevant symmetry is less clear. The Peter-Weyl sectors have Z_3 x Z_3 discrete symmetry from SU(3), not a continuous U(1). Whether the Cooper pair phase constitutes a broken U(1) depends on the precise structure of the condensate wavefunction, which the gap equation alone does not determine.

2. That the Goldstone boson decouples at T ~ M_KK with coupling suppressed by 1/M_KK. This is standard for ordinary Goldstone bosons in 4D, but in the KK context the Goldstone may mix with KK tower modes, altering its effective coupling and decoupling temperature.

The Delta_N_eff = 0.027 calculation appears correct for a single massless scalar decoupling at T ~ 10^{15} GeV. But the conditional nature should be stated more prominently.

### 2.3 Proton Lifetime: The Scaling Is Generic, Not Framework-Specific

The excursion's proton lifetime prediction tau_p ~ M_KK^4 / m_p^5 is the STANDARD scaling for any GUT-scale model with superheavy gauge boson exchange. It is not specific to the phonon-exflation framework. The framework-specific content would be:

- The SPECIFIC gauge boson mass M_X = M_KK * g(tau_frozen), where g(tau_frozen) is determined by the frozen metric. This requires the spectral action normalization at the off-Jensen minimum.
- The SPECIFIC proton decay channel branching ratios, which depend on the CKM/PMNS structure derived from the Dirac operator eigenvectors.
- The RELATIONSHIP between M_KK (from proton decay) and M_KK (from gauge coupling unification), which provides the one-parameter consistency test.

Without these specific computations, the proton lifetime prediction is indistinguishable from generic GUT predictions and does not constitute a framework test.

### 2.4 The Framework-Derived vs. Framework-Adjacent Distinction Is Essential

The excursion's Section IV distinction between framework-derived and framework-adjacent predictions (credited to Cosmic-Web) is the most important epistemic contribution of this document. From the NCG standpoint, I would sharpen this:

- **Framework-derived from the spectral action**: Predictions that follow from Tr f(D_K^2/Lambda^2) at the frozen minimum. These include gauge coupling ratios, the Weinberg angle, mass ratios, and the cosmological constant. These are NCG-native.
- **Framework-derived from the KK reduction**: Predictions that follow from the dimensional reduction of the 12D Einstein-Hilbert action. These include the gravitational constant G_eff and the modulus equation of motion. These are GR-native.
- **Framework-adjacent**: Predictions requiring new theoretical development beyond the spectral action and KK reduction (Volovik's emergent gravity, condensate-dependent graviton propagation). These are speculative.

The excursion's RGE gate (Tier 1) and Weinberg angle gate (Tier 1) are both in the first category. The proton lifetime (Tier 1) is in the second. The N_eff prediction is borderline between first and third.

---

## Section 3: Collaborative Suggestions

### 3.1 Compute the Spectral Action Coefficients at the Off-Jensen Minimum

The Team B synthesis (Priority 1) calls for a 2D U(2)-invariant grid search. The excursion's observational program depends ENTIRELY on the output of this computation. But the excursion does not specify which spectral action coefficients are needed. I specify them here.

From Paper 10 (CCM 2007, equations 4.10-4.14), the bosonic spectral action on M_4 x F expanded to a_4 yields:

- a_0 = (48/pi^2) * f_4 * Lambda^4 * Vol_K -- the cosmological constant contribution
- a_2 = (96/pi^2) * f_2 * Lambda^2 * (1/12) * integral_K R -- the Einstein-Hilbert + Higgs mass
- a_4 = f_0 * (1/4pi^2) * [integral_K (5/3 R^2 - 8/3 |Ric|^2 + 2/3 |Riem|^2)] + gauge/Higgs terms

For the U(2)-invariant family on SU(3), these integrals depend on the metric scale factors (L_1, L_2, L_3). The Milnor-Besse formulas (Sessions 20a, 26) give R, |Ric|^2, |Riem|^2 as polynomials in L_i. The **specific computation**: evaluate these polynomials on the 20x20 grid of (tau, eps_T2). This is the Seeley-DeWitt shortcut I proposed in the Team B synthesis -- it replaces the expensive Dirac spectrum computation with a curvature polynomial evaluation at each grid point, reducing the cost from ~1 hour to ~1 second per point.

**What to extract**: For each grid point, compute sin^2(theta_W) = L_2/(L_1 + L_2), g_1/g_2 = sqrt(L_2/L_1), and the ratio a_4/a_2 (which controls whether the R^2 or R term dominates -- at Jensen, a_4/a_2 = 1000:1, and this ratio may decrease off-Jensen).

### 3.2 Test Whether the NCG GUT Relation and the KK Coupling Relation Are Compatible

This is the tension identified in Section 1.3. The test: at the off-Jensen minimum (L_1, L_2, L_3), compute:

- g_1/g_2 (KK) = sqrt(L_2/L_1) -- from the metric
- g_1/g_2 (NCG) = 1 -- from the spectral action (Paper 07, eq. 3.5)

Then run the SM one-loop RGE from each boundary condition:

- From g_1/g_2 (KK) at M_KK, run to M_Z. Compare with experiment: g_1/g_2 (M_Z) = g'/g = tan(theta_W) = 0.553.
- From g_1 = g_2 (NCG) at Lambda_SA, run to M_Z. This gives sin^2(theta_W) = 3/8 at Lambda_SA, running to ~0.231 at M_Z -- the standard SU(5) prediction.

If the off-Jensen minimum places sqrt(L_2/L_1) close enough to 1 that both boundary conditions are consistent (i.e., Lambda_SA and M_KK are sufficiently close), then the tension resolves. If not, the framework must choose between the NCG GUT relation and the KK dimensional reduction, which is a foundational issue.

**Cost**: Zero (analytic formula applied to Priority 1 grid data).

### 3.3 Verify Whether D_BCS Satisfies More NCG Axioms Than D_K

The proposed D_BCS construction from the Team B synthesis: replace the eigenvalues lambda_k of D_K with E_k = sqrt((lambda_k - mu)^2 + Delta_k^2). This is a well-defined self-adjoint operator with compact resolvent (the E_k grow at the same rate as lambda_k for large k). The key question is whether the BCS gap SMOOTHS the order-one violation.

The order-one violation (Sessions 28b-28c) arises from the commutator [[D, a], b^o] where a, b are algebra elements and b^o = Jb*J^{-1}. The violation is controlled by the matrix elements of D in the Lie algebra representation. For D_BCS, the matrix elements are modified by the Bogoliubov transformation: the off-diagonal blocks acquire factors of u_k * v_l + v_k * u_l, where u_k, v_k are the BCS coherence factors. Near the Fermi surface (lambda_k ~ mu), u_k * v_l ~ 1/2, potentially reducing the off-diagonal matrix elements that drive the violation.

**Specific computation**: At the off-Jensen minimum, construct D_BCS from the BCS gap solution, and compute the order-one violation ||[[D_BCS, a], b^o]|| for each factor pair (C,C), (C,H), (H,H), (C,M_3), (H,M_3), (M_3,M_3). Compare with the D_K violation hierarchy: (H,H) = 4.000, (C,H) = (H,M_3) = 2.828, (C,C) = (M_3,M_3) = 2.000 (Session 28c).

**Cost**: Medium (requires the full D_BCS matrix, not just eigenvalues).

### 3.4 Compute the Spectral Distance at the Frozen Minimum

Paper 04 (Noncommutative Geometry, Chapter VI.1) defines the spectral distance:

d(phi_1, phi_2) = sup{|phi_1(a) - phi_2(a)| : ||[D, a]|| <= 1}

where phi_1, phi_2 are states on the algebra A and D is the Dirac operator. For the frozen ground state, this gives the NCG-native "size" of the internal space. In the commutative case (Paper 04, Theorem VI.1), this recovers the geodesic distance. For the almost-commutative product M_4 x F, the spectral distance has both a continuous contribution (from M_4) and a discrete contribution (from F).

At the frozen minimum, the internal contribution to the spectral distance is d_F = sup{|phi_1(a) - phi_2(a)| : ||[D_K(tau_frozen), a]|| <= 1}. This is a zero-parameter diagnostic that gives the "diameter" of the internal space as seen by the frozen Dirac operator, in the Connes metric. It is a fundamentally different quantity from the geodesic diameter of (SU(3), g(tau_frozen)), because the spectral distance accounts for the FULL operator D_K, not just the metric tensor.

**Cost**: Medium (requires operator norm optimization over the algebra).
**Impact**: Defines the physical meaning of "internal space size" in the NCG sense at the ground state.

### 3.5 Assess the Cosmological Constant Through the Wodzicki Residue

The excursion lists Lambda from BCS sector cancellation as a Tier 4 prediction (Section VIII). From the NCG standpoint, the cosmological constant arises from the a_0 Seeley-DeWitt coefficient:

Lambda_CC = (2/kappa^2) * f_4 * Lambda^4 * a_0(D_K(tau_frozen))

where a_0 = (1/4pi^2) * integral_K 1 = Vol_K / (4pi^2). This is the volume of the internal space, which is FIXED at the frozen minimum (the Jensen deformation is volume-preserving by construction). The BCS sector cancellation enters through the FERMIONIC contribution to the effective cosmological constant, not through a_0 itself.

The Wodzicki residue (Paper 02, Section 5) provides an alternative computation: Res_W(D^{-n}) = (2pi)^n * Vol(S^{n-1}) * integral_{S*M} sigma_{-n}(D^{-n}). For D_K at the frozen minimum, this residue is computable from the Peter-Weyl expansion and provides a CUTOFF-INDEPENDENT definition of the cosmological constant contribution. This is the NCG-regularized version of the L-8 sector sum.

**Specific computation**: Compute Res_W(D_K(tau_frozen)^{-8}) and compare with the cutoff-dependent sector sum from Session 28b (L-8). If they agree within the stable sectors, the divergence is an artifact of the truncation, not a physical divergence. If they disagree, the Wodzicki residue identifies the correct finite part.

**Cost**: Low (the Wodzicki residue is a single number extracted from the leading symbol of D_K^{-8}).

---

## Section 4: Connections to Framework

### 4.1 The Spectral Action as the Master Equation

The excursion's entire observational program reduces, from the NCG standpoint, to a single computation: the spectral action Tr f(D_K(tau_frozen)^2 / Lambda^2) at the BCS frozen minimum, together with the fermionic action <J*psi, D_K(tau_frozen)*psi>. Paper 07 (Chamseddine-Connes 1996) proves that the asymptotic expansion of this trace yields the full Standard Model Lagrangian coupled to gravity. Every entry in the excursion's prediction table (Section VIII) -- gauge couplings, Weinberg angle, proton lifetime, cosmological constant, N_eff -- is a coefficient in this expansion.

The framework's claim is that the single operator D_K(tau_frozen) encodes all of particle physics. The excursion's observational program tests whether the coefficients of the spectral action expansion match the observed Standard Model. This is exactly the program that Paper 14 (Spectral Standpoint, Section 5) identifies as the "key open problem": given the spectral triple for the Standard Model, do the spectral action coefficients reproduce the measured coupling constants, masses, and mixing angles?

The phonon-exflation framework sharpens this by replacing the ARBITRARY finite geometry F (whose Dirac operator D_F must be CHOSEN to match experiment) with a SPECIFIC geometry (Jensen-deformed SU(3) at the BCS minimum, whose Dirac operator is DERIVED from the metric). If the derived operator produces the correct coefficients, the spectral action program achieves what Paper 14 calls for: physics from geometry, with no input beyond the axioms and the choice of internal manifold.

### 4.2 The Order-One Obstruction as the Central Theoretical Challenge

The excursion does not mention the order-one condition. This is the elephant in the room. The 12D product triple M_4 x SU(3) passes 6 of 7 NCG axioms (Session 28c, C-6). The single failure is Axiom 5 (first-order condition): [[D, a], Jb*J^{-1}] = 0. The maximum violation is 4.000 for the (H, H) factor pair (Session 28c).

This matters for the observational program because the first-order condition is what FORCES the gauge group to be SU(3) x SU(2) x U(1) rather than something larger (Paper 12, Classification theorem). Without it, the inner fluctuations D -> D + A + JAJ^{-1} generate a larger algebra of gauge potentials, and the spectral action yields a different gauge theory. The excursion assumes the SM gauge group without addressing whether the frozen Dirac operator actually produces it.

The implication: the RGE gate (Section V.1) and the Weinberg angle gate (Section V.1) test whether the DERIVED gauge group matches the SM. If the order-one violation persists at the frozen minimum, the derived gauge group may be larger than SU(3) x SU(2) x U(1), and the additional gauge bosons would modify the RGE running. This is not a show-stopper (the violation may be small enough that the additional gauge bosons are super-heavy), but it is a systematic uncertainty that the excursion should acknowledge.

### 4.3 Three Generations Remain Unexplained

The excursion's prediction table (Section IV) lists mass ratios and mixing angles, which require three generations of fermions. The NCG axioms do not determine the number of generations -- this is one of the acknowledged open problems of the NCG Standard Model (Paper 11, Section 7; Paper 14, Section 6.2). The phonon-exflation framework proposes that the Z_3 x Z_3 center of SU(3) provides three generations, but this has not been derived from the spectral triple axioms.

For the observational program, this means: even if P-30w passes and the gauge couplings match, the framework does not yet explain WHY there are three generations, only that the SU(3) internal space is compatible with three. This is an input, not a derivation. The excursion should note this explicitly among its theoretical prerequisites.

---

## Section 5: Open Questions

### 5.1 Can the BCS Condensate Define a Genuine Spectral Triple?

The deepest question the excursion raises implicitly: is the frozen vacuum a SPECTRAL TRIPLE in the sense of Paper 04? The proposed D_BCS = D_K with eigenvalues lambda_k replaced by E_k = sqrt((lambda_k - mu)^2 + Delta_k^2) is self-adjoint with compact resolvent. But does the triple (A, H, D_BCS) satisfy the NCG axioms? Specifically:

- **Regularity**: Do a and [D_BCS, a] belong to the domain of delta^n for all n, where delta(T) = [|D_BCS|, T]? The BCS gap modifies the absolute value |D_BCS|, and regularity depends on the smoothness of Delta_k as a function of k.
- **Finiteness**: Is the intersection of domains of delta^n a finitely generated projective A-module? This depends on whether the BCS condensation preserves the module structure.
- **Order-one**: Does [[D_BCS, a], b^o] = 0? As noted in Section 3.3, the Bogoliubov transformation may reduce the violation.

If D_BCS satisfies MORE axioms than D_K, the BCS condensation is not merely a thermodynamic process -- it is a geometric process that IMPROVES the spectral triple. This would be a profound result: the many-body ground state is geometrically BETTER than the single-particle Dirac operator.

### 5.2 What Is the Correct Cutoff for the Spectral Action on SU(3)?

The excursion's M_KK consistency web assumes a sharp identification between the KK compactification scale and the spectral action cutoff. But the spectral action (Paper 07) depends on the test function f, not on a sharp cutoff. The moments f_0, f_2, f_4 encode the shape of f. For the phonon-exflation framework, the test function must be chosen such that the spectral action on M_4 x SU(3) reproduces the correct 4D physics. This constrains the moments in terms of M_KK and the measured coupling constants.

The open question: is there a UNIQUE test function f (up to normalization) that makes all observational predictions consistent? Or does the space of consistent test functions have residual freedom that prevents zero-parameter predictions? This is the spectral action analogue of the "landscape problem" -- and it is addressable by computation once P-30w fixes tau_frozen.

### 5.3 Does the Spectral Action Expansion Converge on SU(3)?

The excursion uses the spectral action expansion to fourth order (a_0, a_2, a_4). Session 28c (E-3) showed that the periodic orbit correction is 10^{-39}, establishing that the Seeley-DeWitt expansion is exact to 40+ digits. But this was for the EIGENVALUE SUM, not for individual physical parameters. The convergence of the spectral action expansion for specific observables (gauge couplings, Weinberg angle) depends on the higher-order coefficients a_6, a_8, ..., which contribute corrections suppressed by powers of Lambda^{-2}.

For M_KK ~ 10^{16} GeV and the SM energy scale ~ 10^{2} GeV, the suppression factor is (M_Z/M_KK)^2 ~ 10^{-28} per order, so higher-order corrections are negligible. But the convergence at the KK scale itself -- where the spectral action expansion is evaluated -- is a separate question. Session 27 proved a_6 monotonicity for individual sectors, but the all-order conjecture remains open (C-SA-4 in the constraint map).

---

## Closing Assessment

The Observational Excursion is a clear-eyed assessment of where the phonon-exflation framework meets experiment. Its principal virtue is honesty: the pre-freeze epoch is inaccessible, the post-freeze predictions are the Standard Model parameters themselves, and the testable content reduces to a finite set of frozen-state computations. The excursion correctly identifies the RGE gate and P-30w as existential, and the w = -1 prediction as the cleanest near-term test.

From the NCG standpoint, the excursion's observational program is the spectral action program applied to a specific frozen Dirac operator. The novelty is not in the spectral action machinery -- that has existed since 1996 -- but in the claim that the frozen geometry is DERIVED rather than CHOSEN. The BCS trapping mechanism provides a selection principle that the NCG axioms alone do not: it picks a specific point on the moduli space of internal geometries, and every prediction flows from that point.

The document would be strengthened by acknowledging two structural issues it passes over in silence: the order-one violation (which affects the derived gauge group) and the generation problem (which affects the derived fermion content). Neither is fatal, but both are honest uncertainties in the observational chain.

The spectral action is a single formula. The observational universe is its output. Whether that output matches the Standard Model is a question with a computable answer -- and that computation is now within reach.

---

*Review completed by Connes (connes-ncg-theorist), 2026-02-28. All NCG claims grounded in Connes Papers 01-14. Specific references: Paper 04 (spectral distance, reconstruction theorem), Paper 07 (spectral action principle, GUT relations), Paper 10 (CCM 2007, definitive coefficients), Paper 12 (classification theorem, order-one), Paper 14 (spectral standpoint, open problems). Cross-referenced with Team B synthesis and Session 29 computation history.*
