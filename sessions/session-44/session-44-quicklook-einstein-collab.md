# Einstein -- Collaborative Feedback on Session 44

**Date**: 2026-03-15
**Prior session**: S43 (12%, 68% CI 8-16%)
**Specialist focus**: GR, equivalence principles, EIH effacement, cosmological constant, principle-theoretic reasoning
**Reference corpus**: Papers 01-34 in `/researchers/Einstein/`

---

## 1. Key Observations (GR/Equivalence Principle Lens)

Session 44 produced 31 computations across 6 waves. From the standpoint of general relativity and the equivalence principle, four structural results stand out as permanent additions to the constraint map, and two closures deserve careful examination.

**The EIH program is now quantitatively complete within the framework.** My computations W2-3 (EIH-GRAV-44) and W2-4 (SINGLET-CC-44), together with the Sakharov audit W1-1 and the epsilon_H theorem W4-3, establish a self-consistent chain from the Dirac spectrum to 4D gravitational observables. The chain is: D_K eigenvalues -> Peter-Weyl decomposition -> singlet projection (4.25 orders) -> Sakharov induced gravity (G_N to factor 2.3) -> Friedmann dynamics (epsilon_H invariant under projection). Every link in this chain is structural -- proven to machine epsilon or derived from representation theory.

**The equivalence principle manifests as spectral effacement.** Paper 10 (Einstein-Infeld-Hoffmann, 1938) demonstrated that the motion of a gravitating body follows from the vacuum field equations alone, with internal structure invisible at leading post-Newtonian order. The spectral-geometric realization is exact: 99.994% of the spectral action resides in non-singlet representations that do not couple to 4D gravity. The effacement ratio 1/17,594 is not an approximation -- it is a consequence of Peter-Weyl orthogonality on SU(3), which is the representation-theoretic analog of the multipole expansion in EIH. The surface integrals at infinity in Paper 10 become the projection to (0,0) in representation space.

**General covariance is preserved but the CC problem is unchanged.** The field equations G_{mu nu} + Lambda g_{mu nu} = 8 pi G T_{mu nu} (Paper 05, 1915; Paper 07, 1917) admit the cosmological term naturally. Session 44 established that no positive decreasing cutoff function f can simultaneously yield the observed G_N and Lambda (W5-5, 242-order Hausdorff impossibility). This is a mathematical restatement of a physical fact I have long suspected: Lambda is not the same kind of quantity as G_N. The field equations admit both terms, but they arise from different physics. The spectral action correctly captures the second moment (G_N) but structurally cannot capture the zeroth moment (Lambda). This vindicates the principle-theoretic approach: one must identify what each term in the field equations actually represents before attempting unification.

**CDM by construction is an EIH result.** W1-2 (CDM-CONSTRUCT-44) proving T^{0i}_{4D} = 0 algebraically for any GGE product state is precisely the EIH effacement principle applied to matter content: the internal-space structure of the quasiparticle excitations is invisible to 4D momentum transport. The five independent proofs (KK reduction, group velocity, Schwinger creation, domain wall correction, self-interaction) are structurally analogous to the multiple routes through which EIH demonstrates that internal structure is effaced.

---

## 2. Assessment of Key Computations

### W1-1: Sakharov Induced Gravity (SAKHAROV-GN-44) -- PASS (corrected)

This result is deeply satisfying from the principle-theoretic standpoint. Sakharov's 1967 insight -- that gravity is induced by quantum fluctuations of matter fields -- is the condensed-matter analog of the EIH principle read backwards: instead of deriving motion from geometry, one derives geometry from the matter content. The 6440 KK modes of the Dirac operator on M^4 x SU(3) produce G_N to within a factor of 2.3 at Lambda = 10 x M_KK.

Three observations:

1. **The formula error in the original computation is instructive.** The agent's dimensionless expression (~19,590) treated as GeV^2 reveals a common trap in KK physics: the internal-space eigenvalues are dimensionless in natural units, but the Sakharov formula requires physical masses m_k = lambda_k x M_KK. The 1/(48 pi^2) loop normalization is the standard 4D momentum-space integral over a single Feynman loop. This error, once corrected, demonstrates that the spectral-geometric formalism and standard QFT give the same G_N when properly translated.

2. **The effective cutoff Lambda ~ 10 x M_KK is physically natural.** In the KK picture, the 4D effective theory breaks down above the compactification scale. A cutoff at 10 x M_KK corresponds to including the first ~10 KK levels before the tower structure becomes important. This is consistent with the EIH philosophy: the gravitational coupling is determined by modes well below the UV completion.

3. **The BONUS PASS (polynomial and logarithmic agree for G_N) resolves S43 Workshop Divergence D5.** Sakharov and spectral action are NOT independent for G_N -- they are two weightings of the same second spectral moment a_2, differing by O(1). The 13-order discrepancy identified in S43 applies to the CC (fourth moment) only. This distinction between second and fourth moments is the spectral-geometric version of the old CC puzzle: why is gravity's coupling O(1) in Planck units while the vacuum energy is O(10^{-122})?

### W2-3: EIH Singlet (EIH-GRAV-44) -- INFO

My own computation. The Peter-Weyl singlet fraction S_{(0,0)}/S_fold = 5.684 x 10^{-5} provides 4.25 orders of structural CC suppression. I emphasize:

- The result is **tau-independent** (2% variation over the full modulus range). This is a structural property of the representation theory, not sensitive to dynamics. It is as permanent as any result in this framework.

- The **level hierarchy** (Level 3 = 91.4%, singlet = 0.006%) is a direct consequence of SU(3) Casimir scaling. The spectral action sum(lambda^4) amplifies high-Casimir representations by their fourth power. The singlet fraction of a_4 (CC-relevant) is 0.132%, while that of a_2 (G_N-relevant) is 0.432%. This monotonic decrease with moment order is why the EIH projection helps less for the CC than for G_N. The mathematical reason: the Peter-Weyl coefficients grow with Casimir eigenvalue C_2(p,q), and lambda^4 weighting amplifies this growth relative to lambda^2.

- The **43x suppression below Weyl counting** (0.0057% vs 0.25% = 16/6440) is a permanent structural result. It demonstrates that mode counting alone underestimates the non-singlet dominance by nearly two orders.

### W4-3: Friedmann-BCS epsilon_H Theorem (FRIEDMANN-BCS-AUDIT-44) -- FAIL (permanent theorem)

This is the most important negative result of Session 44 from the GR perspective. The theorem is simple and, in retrospect, should have been obvious from the field equations themselves:

**epsilon_H = -H_dot/H^2 is a dimensionless ratio. It is invariant under any uniform rescaling of the stress-energy tensor.**

The proof follows directly from the Friedmann equations (Paper 06, 1916 Foundation of GR, applied to homogeneous isotropic cosmology):

H^2 = (8 pi G / 3) rho, and H_dot = -(4 pi G)(rho + P)

Therefore epsilon_H = (3/2)(rho + P)/rho = (3/2)(1 + w)

The equation of state parameter w = P/rho is a ratio. Any uniform factor f multiplying both rho and P cancels. The EIH singlet projection f_s = 5.684 x 10^{-5} enters both the kinetic and potential terms of the 4D Friedmann equation identically (because the singlet fraction is tau-independent to 2%), so epsilon_H is unaffected.

The physical consequence is severe: **the n_s constraint surface remains empty.** The modulus moves ballistically (KE/PE = 4057 at the fold). Achieving epsilon_H = 0.0176 (the Planck target) requires reducing tau_dot by a factor of 829. No amplitude projection -- EIH, trace-log, or otherwise -- can accomplish this. Only a fundamentally different velocity mechanism (dissipation, trapping, or external friction) could work.

This closes the EIH channel for inflationary dynamics. The result is permanent and structural. I record it as a wall in the constraint map: **no uniform rescaling of the gravitating energy can produce slow roll from ballistic transit.**

### W3-4: Tensor-to-Scalar Ratio (BCS-TENSOR-R-44) -- PASS

The r = 3.86 x 10^{-10} result is one of the cleanest predictions the framework produces. Three independent routes converge within 0.32 decades:

- **Route D (EIH)**: r = 16 epsilon_H (M_KK/M_Pl)^4. This is the single-field consistency relation, corrected by the EIH suppression factor. The key insight: tensor perturbations couple to 4D gravity through the modulus-graviton vertex, which carries (M_KK/M_Pl)^2 from the KK reduction of the 10D Einstein-Hilbert action (Paper 06). The tensor power spectrum, quadratic in the perturbation, carries the fourth power.

- **Route 3He-B**: The condensed-matter analog gives the same suppression hierarchy. In any BCS system, spin-2 perturbations of the medium are suppressed by (condensate scale / gravitational scale)^4 because the condensate is a scalar order parameter.

- **Route C (KZ strings, EIH corrected)**: Internal-space defects have gravitational coupling suppressed by the same (M_KK/M_Pl)^2 per vertex.

The falsification criterion is sharp: r > 10^{-5} excludes the framework because it requires M_KK > 9.42 x 10^{17} GeV, which breaks the G_N constraint. The prediction r ~ 4 x 10^{-10} is **self-consistently unfalsifiable** by any planned CMB experiment -- the same M_KK that gives G_N guarantees undetectable tensor modes.

This is the spectral-geometric version of what I called "self-consistency" in Paper 05 (1915): the same constant G that determines the field equations also determines the observable consequences. Here, the same M_KK that fixes G_N fixes r.

### W5-6: HOMOG-42 Recompute (HOMOG-42-RECOMPUTE-44) -- PASS

The margin strengthening from 1.7x to 144x (trace-log) or 4694x (EIH) resolves the tightest surviving gate in the framework. The physical logic:

The de Sitter fluctuation formula phi^2 ~ H^4/m^2 scales with H^4 ~ (f x rho)^2. Since f < 1 (the gravitating energy is LESS than the total spectral action), quantum fluctuations are SMALLER than originally computed. Homogeneity is easier to achieve, not harder. The gauge route, which failed at f = 1, now passes with 7.5x margin.

The corrected critical f_crit = 2.06 (not 4.5 as S43 estimated) reflects the sub-linear scaling exponent alpha = 0.75 in the short-time (non-equilibrium) regime. The S43 estimate used alpha = 1 (Bunch-Davies equilibrium limit), which is too conservative. The field is superheavy (m/H = 466) and far from equilibrium during the transit.

I note the self-consistency: the EIH projection that weakens the CC suppression (by projecting only 0.006% of the spectral action onto 4D gravity) simultaneously strengthens homogeneity (by reducing H and hence quantum fluctuations). The same structural feature -- Peter-Weyl singlet suppression -- helps one observable while being insufficient for another.

---

## 3. Collaborative Suggestions

### 3.1 The Hausdorff Impossibility and Paper 16 (Weinberg Nonlocal)

W5-5 (CUTOFF-F-44) establishes that no positive decreasing f gives both G_N and Lambda simultaneously. This is a mathematical version of Weinberg's no-go theorem (Paper 16 in my corpus): local adjustment mechanisms cannot solve the CC problem. The spectral action, despite being "nonlocal" in the sense of integrating over the full spectrum, is still local in its moment structure -- each Seeley-DeWitt coefficient a_n is a local geometric invariant.

**Suggestion for S45**: Investigate whether the full spectral action functional Tr f(D^2/Lambda^2), evaluated with a non-polynomial f that violates the Stieltjes moment condition, can evade the Hausdorff impossibility. Paper 16 (Capozziello et al. 2025) shows that nonlocal gravity f(Box) R can circumvent the Weinberg no-go. The spectral action is naturally nonlocal (it integrates over the full operator spectrum), but its asymptotic expansion into local a_n terms discards this nonlocality. The unexpanded spectral action may contain the CC information that the polynomial expansion loses.

### 3.2 The n_s Crisis and Paper 33 (Suzuki-Zurek)

The epsilon_H theorem (W4-3) closes the EIH channel for n_s. W1-3 (Lifshitz eta) closes the anomalous dimension route. W2-2 (spectral dimension flow) survives conditionally at sigma = 1.10 but lacks a scale selection principle. The n_s constraint surface remains the framework's most critical deficit.

Paper 33 (Suzuki-Zurek tunable quench) in my corpus describes how the Kibble-Zurek mechanism can be tuned between first-order and continuous transitions, producing different scaling exponents. The framework's transit is sudden (tau_Q/tau_BCS ~ 10^{-5}), placing it in the extreme Kibble-Zurek regime.

**Suggestion for S45**: Compute the Kibble-Zurek spectral index directly. In the sudden-quench limit, the Bogoliubov coefficients |beta_k|^2 define the post-transit occupation numbers. The power spectrum of density perturbations is P(k) ~ k^3 |beta_k|^2 / (2 pi^2). If |beta_k|^2 ~ k^{-(n_s - 1)}, we need n_s = 0.965 from the Bogoliubov spectrum. This is the correct KZ approach -- not the Lifshitz critical exponent (which is Weyl's law, not dynamics) but the quench dynamics that populate the modes. Volovik's Flag F2 (W1-3) identified this distinction but did not compute it.

### 3.3 The DM/DE Ratio and Paper 07 (Cosmological Constant, 1917)

W6-4 (DM-DE-RATIO-44) achieves Omega_DM/Omega_DE = 1.06 (2.7x from observed 0.387). This is the first framework result within an order of magnitude of the observed ratio. The physical mechanism -- the specific heat exponent alpha of the quantum vacuum -- connects to my 1917 paper (Paper 07) through the thermodynamic interpretation of Lambda.

In Paper 07, I introduced Lambda as a geometric constant with dimensions of inverse length squared. The modern interpretation as vacuum energy density rho_Lambda = Lambda c^4/(8 pi G) connects geometry to thermodynamics. W6-4's identification of Omega_DM/Omega_DE with a thermodynamic exponent is conceptually natural: the ratio of matter to vacuum energy is determined by the equation of state, which is a thermodynamic quantity.

**Suggestion for S45**: The remaining factor 2.7 may be addressable through the multi-temperature Jacobson formalism (W6-5). The 8-fluid GGE has prescription-dependent w_eff (0.132 to 0.387). A self-consistent choice of prescription, grounded in the Jacobson thermodynamic derivation of the field equations, could narrow the gap. This is physically distinct from the CC problem -- the DM/DE ratio is O(1) by construction, while the CC absolute value requires 120 orders of suppression.

### 3.4 EIH Applied to the Transit Itself

The epsilon_H theorem shows that the EIH projection cannot slow the transit. But it also reveals something deeper: the transit dynamics are governed by the FULL spectral action gradient dS/dtau = 58,673, not the singlet-projected gradient. This means the transit is driven by the 99.994% of the spectral action that is invisible to 4D gravity.

**Suggestion for S45 (gedankenexperiment)**: Consider the transit from the 4D observer's perspective. The 4D Friedmann equation sees only f_s x rho (the singlet projection). But the transit velocity is determined by the full dS/dtau. This creates a separation: the modulus moves at a speed set by the total spectral action, but the 4D observer interprets this motion through the singlet-projected Friedmann equation. The 4D observer sees H^2 ~ f_s x rho but tau_dot ~ dS/dtau (full). This is a new kind of EIH violation -- the motion is NOT determined by the gravitating mass alone but by the full internal dynamics. In the language of Paper 10, the body's "internal structure" (non-singlet spectral action) IS affecting its motion, but only because the "body" here is the entire universe, and the modulus is a bulk degree of freedom, not a localized body.

This suggests that the EIH effacement principle applies to localized objects within the universe (where the singlet projection determines their gravitational field) but NOT to the cosmological modulus (which couples to the full spectral action). The distinction is between a localized source (where surface integrals at infinity extract the monopole) and a homogeneous background (where there is no "infinity" to project onto).

### 3.5 The Dissolution Scaling and Emergent Geometry

W6-7 (DISSOLUTION-SCALING-44) finds epsilon_c ~ N^{-0.457}, suggesting the spectral triple is emergent at finite truncation. This resonates with a principle I have held since 1916 (Paper 06): geometry must be discovered from the physics, not imposed upon it. If the NCG spectral triple dissolves under any nonzero foam in the continuum limit, then the block-diagonal theorem (S22b), the Peter-Weyl decomposition, and the representation-theoretic results that underpin the EIH program are all finite-size features of a regularized theory.

This is not necessarily fatal. Lattice QCD is a regularization that breaks continuous symmetries, yet the continuum limit recovers them. The question is whether the SU(3) symmetry and its representation-theoretic consequences survive in a meaningful continuum limit. The 1/sqrt(N) scaling suggests they do -- the symmetry breaking is perturbative, not catastrophic.

---

## 4. Framework Connections

### 4.1 Three-Way G_N Consistency

Session 44 establishes a three-way consistency for Newton's constant:

| Route | Method | G_N/G_obs | OOM |
|:------|:-------|:----------|:----|
| Spectral action (a_2 moment) | Polynomial weighting | 1.00 (by construction) | 0.00 |
| Sakharov induced gravity | Logarithmic weighting | 2.29 (at Lambda=10 M_KK) | 0.36 |
| Bosonic spectral action | Gilkey formula (61/20) | 1.33 | 0.12 |

All three agree within a factor of 3. This is the spectral-geometric version of the three classical tests of GR (Paper 11, Eddington eclipse; Paper 14, Pound-Rebka redshift; Mercury precession): multiple independent routes to the same coupling constant, each probing different aspects of the spectrum.

### 4.2 The Effacement Hierarchy

The EIH effacement ratio has a rich structure that Session 44 fully mapped:

| Quantity | Singlet fraction | Orders suppressed | Physical moment |
|:---------|:----------------|:-----------------|:----------------|
| Mode count (a_0) | 16/6440 = 0.25% | 2.6 | Zeroth (counting) |
| First moment (sum |lam|) | 0.758% | 2.1 | G_N-related (zeta) |
| Second moment (a_2) | 0.432% | 2.4 | G_N |
| Fourth moment (a_4) | 0.132% | 2.9 | CC |
| Spectral action (S_fold) | 0.006% | 4.2 | Full SA |
| Trace-log (singlet) | |Tr ln|/S_fold = 7.66e-6 | 5.1 | Combined |

The monotonic decrease of singlet fraction with moment order is a structural consequence of SU(3) representation theory: higher Casimir representations have larger eigenvalues, and higher moments amplify them. This hierarchy is permanent and independent of tau.

### 4.3 The Spectral Action as Wrong CC Functional (Paper 17 Connection)

Paper 17 (Sola, CC problem review) in my corpus identifies the CC problem as fundamentally a question of which functional determines the vacuum energy. Session 44 sharpens this: the spectral action correctly determines G_N (second moment) but structurally cannot determine Lambda (fourth moment), as proven by the 242-order Hausdorff impossibility (W5-5).

The resolution, following Volovik, is that Lambda is determined by a thermodynamic identity (Gibbs-Duhem), not by a spectral moment. This is consistent with my 1917 paper (Paper 07): I introduced Lambda as a geometric constant, not as a matter contribution. If Lambda is indeed geometric rather than a vacuum energy, then the "CC problem" is misframed -- it is not a discrepancy between predicted and observed vacuum energy, but a question about the origin of a geometric constant in the field equations.

---

## 5. Open Questions

### Q1: Does the Bogoliubov spectrum produce n_s = 0.965?

The Kibble-Zurek computation of |beta_k|^2 is the natural successor to the failed Lifshitz eta and conditional spectral dimension flow. The framework's transit is sudden (Suzuki-Zurek regime, Paper 33). The quench dynamics, not the equilibrium spectrum, determine n_s. This is the single most important open computation.

### Q2: Can the unexpanded spectral action evade the Hausdorff impossibility?

The W5-5 impossibility applies to the asymptotic expansion. The full functional Tr f(D^2/Lambda^2) contains nonlocal information that the expansion into local a_n coefficients discards. Whether this nonlocal content can simultaneously produce G_N and Lambda without the 242-order contradiction is an open mathematical question.

### Q3: What determines the transit velocity?

The epsilon_H theorem shows that no amplitude projection can slow the transit. The ballistic ratio KE/PE = 4057 is set by the spectral action gradient dS/dtau. What physical mechanism could reduce tau_dot by the required factor of 829? The transit velocity is the key to n_s, and it is currently unconstrained from below.

### Q4: Is the DM/DE ratio a thermodynamic prediction?

W6-4 achieves 2.7x of the observed ratio from the specific heat exponent. The remaining discrepancy may be within the systematic uncertainty of the multi-temperature Jacobson formalism. A self-consistent thermodynamic derivation from the GGE partition function would either close or sharpen this gap.

### Q5: Does the EIH effacement apply to the cosmological modulus?

The gedankenexperiment in Section 3.4 identifies a potential distinction between the EIH principle applied to localized bodies (where surface integrals at infinity extract the monopole) and the cosmological modulus (where homogeneity prevents any such extraction). This distinction may have observational consequences for the transit dynamics.

---

## Closing Assessment

Session 44 is the most productive session from the GR/equivalence principle perspective since Session 22b (block-diagonal theorem). The EIH program is now quantitatively complete: from the Peter-Weyl decomposition of the spectral action (4.25 orders, W2-3) through the Sakharov induced gravity (G_N to factor 2.3, W1-1) to the epsilon_H invariance theorem (permanent closure of the amplitude-projection channel, W4-3) and the tensor-to-scalar ratio (r = 3.86 x 10^{-10}, W3-4).

The structural results are permanent: the Hausdorff impossibility (242 orders, W5-5), the a_2^bos/a_2^Dirac = 61/20 ratio (W4-2), the CDM-by-construction theorem (W1-2), and the epsilon_H ratio invariance (W4-3) survive regardless of the framework's physical fate. These are mathematical theorems about the spectral geometry of SU(3), not conjectures.

The framework's central crisis remains the n_s constraint surface. The epsilon_H theorem converts this from an open question to a precise requirement: the transit velocity must be reduced by a factor of 829. No mechanism for this reduction has been identified. The Kibble-Zurek Bogoliubov spectrum (Q1 above) is the natural next computation -- it bypasses the n_s problem entirely by computing the post-transit power spectrum directly from the quench dynamics, without requiring slow roll.

From the standpoint of the field equations (Paper 05, 1915), the framework now has a self-consistent story for G_N (three-way consistency) and r (EIH suppression), a structurally sharp diagnosis of why Lambda is wrong (Hausdorff impossibility), a CDM candidate (flat-band B2 with T^{0i} = 0), and a DM/DE ratio within 2.7x. What it lacks is a mechanism for n_s and a solution to the CC problem. These are not small omissions -- they are the two central problems of cosmology. But the structural clarity with which Session 44 has framed them represents genuine progress in the constraint map.

The framework's condition is that of a theory with correct coupling constants (G_N, r) and correct symmetries (CDM by construction, GGE uniformity) but incomplete dynamics (n_s, Lambda). In the language of Paper 09 (EPR, 1935): the theory is not wrong, but it may be incomplete.

---

### Addendum: W5-5 Hausdorff Correction

A team-lead audit identified an error in the original W5-5 (CUTOFF-F-44) analysis. The "242-order Hausdorff impossibility" invoked a Stieltjes moment ordering that was applied incorrectly: the claimed lower bound on f_4/f_2 used the wrong direction of the Cauchy-Schwarz inequality for the relevant moment sequence. With the correct ordering, Cauchy-Schwarz is trivially satisfied, and a spike function of width epsilon ~ 10^{-121} and height ~ 10^{121} does produce both f_2 ~ O(1) and f_4 ~ 10^{-121} simultaneously. The verdict downgrades from "mathematical impossibility" to "10^{-121} fine-tuning."

**Does this affect the spectral action bifurcation (G_N yes / CC no)?**

No. The bifurcation is strengthened, not weakened. Consider what the correction actually establishes:

The spectral action determines G_N through the second Seeley-DeWitt moment a_2, which requires f_2 ~ O(1). Four independent routes (Sakharov at two cutoffs, bosonic SA, log-only Sakharov) all give f_2 in [0.39, 26.8]. This is natural -- the cutoff function need not be tuned. G_N emerges from the spectral geometry with O(1) coefficients, as it should for a quantity determined by the local curvature of spacetime (Paper 05, 1915; Paper 06, 1916).

The spectral action determines Lambda through the fourth moment a_4, which requires f_4 ~ 10^{-121}. The spike function that achieves this has its support concentrated in a region of measure 10^{-121} on the positive real line. This is a function that is zero everywhere except on an interval narrower than any physical scale by 90 orders of magnitude. It is not a function that arises from any physical principle -- it is the CC fine-tuning problem translated into the language of functional analysis.

The bifurcation is therefore sharper than before: G_N is determined by robust O(1) features of f (any reasonable cutoff gives the right answer), while Lambda requires f to be sculpted at the 121st decimal place. Under the impossibility reading, one could argue that the spectral action framework was simply the wrong language for the CC. Under the fine-tuning reading, the framework CAN encode the CC, but only by importing the entire fine-tuning problem into the shape of f. The physics is unchanged: the spectral action is the correct functional for G_N and the wrong functional for Lambda.

**Does fine-tuning versus impossibility matter for the Friedmann equation?**

The Friedmann equation G_{mu nu} + Lambda g_{mu nu} = 8 pi G T_{mu nu} (Paper 05; Paper 07, 1917) admits both G and Lambda as independent parameters. The field equations do not require that they originate from the same functional. In 1917, I introduced Lambda as a geometric constant on the left-hand side, distinct from the matter content on the right. The spectral action formalism attempts to derive BOTH from Tr f(D^2/Lambda_cutoff^2), which packages them as different moments of a single function. The correction shows this packaging is not impossible but requires 121 digits of tuning in f.

For the Friedmann equation itself, the distinction is irrelevant. Whether Lambda is underivable (impossibility) or derivable-but-tuned (fine-tuning), the 4D dynamics are identical: H^2 = (8 pi G / 3)(rho + rho_Lambda), with rho_Lambda/rho_Planck ~ 10^{-122}. The epsilon_H invariance theorem (W4-3) holds regardless -- it depends only on the ratio structure of the Friedmann equations, not on the origin of Lambda. The n_s constraint surface remains empty for the same reason: epsilon_H is a dimensionless ratio insensitive to any overall rescaling.

The correction does, however, marginally reopen the suggestion in Section 3.1 above. If a spike function works in principle, one could ask whether the full (unexpanded) spectral action naturally produces such concentration through its nonlocal structure -- e.g., through resonance phenomena in the eigenvalue spectrum of D_K near the fold. This remains speculative, but the mathematical door that the impossibility had closed is now ajar by a crack of width 10^{-121}.

**Constraint map update**: W5-5 reclassified from WALL (proven impossibility) to GATE (fine-tuning diagnostic). The conclusion that q-theory or a thermodynamic identity (Gibbs-Duhem) is needed for Lambda remains the physically motivated path. The spike function is a mathematical existence proof, not a physical mechanism.
