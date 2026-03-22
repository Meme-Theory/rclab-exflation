# Atlas Collaborative Review: Neutrino Detection Specialist

**Scope**: Project Atlas (Sessions 1-51), reviewed through neutrino oscillation phenomenology and direct mass measurement
**Angle**: PMNS mixing (Level 5 closure), mass hierarchy ratio R = 27.2, normal ordering prediction, scale bridge, experimental constraints
**Date**: 2026-03-20

---

## 1. What the Atlas Shows: The Neutrino Sector in Five Numbers

The framework's neutrino sector reduces to five quantities that I can evaluate against the global oscillation dataset (NuFit-6.0, September 2024: Delta m^2_21 = 7.41e-5 eV^2, |Delta m^2_32| = 2.507e-3 eV^2, sin^2(theta_12) = 0.303, sin^2(theta_23) = 0.451, sin^2(theta_13) = 0.02225).

**R = 27.2 at the fold (tau = 0.20)**. The mass-squared difference ratio R = Delta m^2_32 / Delta m^2_21 from the three lightest Dirac branches (B1, B2, B3) at the van Hove fold. Measured: R = 33.8 (NuFit-6.0). Deficit: 19.5%. This is NOT a failure -- R sweeps steeply through tau, passing through 33 near tau = 0.21 (S36 W2-A: R_inter values: 6.6 at tau = 0.12, 11.2 at tau = 0.15, 18.9 at tau = 0.18, 27.2 at tau = 0.20, 59.8 at tau = 0.24, 336 at tau = 0.30). The physical exit tau determines R. The 19.5% deficit at the fold maps to a tau offset of approximately 0.01 from the fold -- well within the transit dynamics uncertainty (Session 39 FRIED-39, 133,000x dwell time shortfall).

**Normal ordering: B1 < B2 < B3 at ALL tau > 0**. Structural, parameter-free, proven by Schur's lemma (S34-S35, permanent theorem). The measured mass ordering is normal (NuFit-6.0: Delta chi^2 = 6.1 including Super-K atmospheric, approximately 2.5 sigma). JUNO will determine the ordering at 3 sigma with 6.5 years of data (expected approximately 2030-2031). DUNE will reach 5 sigma in approximately 2 years of beam running (early 2030s). This is the framework's most falsifiable neutrino prediction. An inverted ordering determination would close the entire neutrino sector.

**NNI texture: V(B1,B1) = 0, V(B1,B3) = 0 exactly**. The BCS coupling matrix has nearest-neighbor interaction form (Trap 1 and Trap 4, both proven by Schur orthogonality, S34). This predicts theta_12 >> theta_13, consistent with data (theta_12 = 33.4 degrees vs theta_13 = 8.5 degrees). The ratio V(B1,B2)/V(B2,B3) = 3.5, compared to the data ratio tan(theta_12)/sin(theta_13) approximately 3.9. But this is a qualitative texture, not a quantitative mixing angle prediction, because all mixing angles on the Jensen curve are exactly ZERO.

**Mixing angles: ZERO on the Jensen curve**. This is the devastating result. Five independent computations across Sessions 29-37 closed every identified route to nontrivial PMNS mixing on the 1-parameter Jensen deformation family. The mixing angle problem is classified Level 5 -- requiring fundamentally new mathematical structure, not refinement of existing computations.

**Absolute mass scale: UNRESOLVED**. The D_K eigenvalues are 0.82, 0.84, 0.98 in M_KK units (S39). KATRIN bounds m_nu < 0.45 eV (Paper 12). Planck+DESI constrains sum(m_i) < 0.064 eV (LCDM). The scale bridge from O(1) * M_KK to sub-eV physical masses requires either a seesaw-like suppression (but S_F^Connes = 0 identically on SU(3) from BDI T-symmetry, S41 W1-2) or an M_KK at the meV scale (contradicting gauge coupling matching at 10^9-10^13 GeV). This is existential.

---

## 2. The Five PMNS Closures: An Experimentalist's Autopsy

Each closure corresponds to a specific experimentally motivated question: "Can THIS mechanism produce the measured PMNS mixing angles?" I list them in chronological order with the experimental constraint that each was tested against.

**Closure 1: Bulk tridiagonal PMNS (S29Ba)**. The 3x3 effective Hamiltonian H_eff from B1-B2-B3 splittings and Kosmann couplings gives R = 0.29 at all tau. The strong-mixing regime (V_12/dE_12 approximately 6-9) suppresses the mass hierarchy rather than enhancing it. Gate: R in [17, 66]. Result: 0.29. Shortfall: 116x. Kill shot: Kramers degeneracy artifacts in H_eff construction.

**Closure 2: PMNS-corrected with spinor V (S35 W3-A)**. After the S34 bug corrections (frame V = 0.287 replaced by spinor V = 0.057), the corrected BCS coupling gives R_max = 0.57, sin^2(theta_13) = 0.010, theta_23 = 12.2 degrees. The structural ceiling: dE_23/dE_12 = 5.09 at tau = 0.20, which caps R < 5.9 in the weak-mixing limit. Gate: R in [10, 100], theta_23 in [35, 55] degrees, sin^2(theta_13) in [0.01, 0.05]. Result: two of three sub-gates FAIL. The sin^2(theta_13) marginally passes at 0.010 (compared to Daya Bay's 0.02225, Paper 10), but theta_23 = 12.2 degrees is catastrophically below the measured approximately 49 degrees (Super-K, Paper 07; NuFit-6.0).

**Closure 3: Inter-sector PMNS from Paper 18 Phi-tilde (S36 W2-A)**. The Baptista Paper 18 mechanism (misalignment between eigenspaces at different tau values) gives zero mixing at ALL tau on the Jensen curve. Physical reason: both the reference metric and the deformed metric are left-invariant under U(2), so the eigenspaces are locked by Schur's lemma. The subspace overlap O_ij is exactly diagonal: B_i(tau) projects only onto B_i(ref). R_inter = 27.2 is available at tau = 0.20 (the mass hierarchy is correct), but all mixing angles are identically zero. Gate: R in [10, 100] with nonzero mixing. Result: R PASSES, mixing FAILS with zero margin.

**Closure 4: H_eff inter-sector bound (S35 Workshop)**. Any 3x3 real symmetric H_eff with the framework's diagonal elements satisfies R * sin^2(2theta_23) < 3.5 (proven analytically, verified by 10 million Monte Carlo samples with zero hits). The required value is R * sin^2(2theta_23) = 33.8 * 0.546 = 17.8. Shortfall: 5.1x minimum. This is a structural bound on ANY coupling-based mechanism that preserves the B1-B2-B3 diagonal structure.

**Closure 5: K7-G1-37 PMNS triad (S37 W1-B)**. The (B1, B3, G1) triad was the proposed route to 3x3 mixing using one eigenvalue from each of three Peter-Weyl sectors. Kill shot: the fundamental representation (1,0) decomposes under U(1)_7 as 1_{-0.577} + 2_{+0.289}. ALL weights have q_7 nonzero. Only self-conjugate representations (p = q) have q_7 = 0 weights. This is a weight-space fact -- algebraic, representation-theoretic, independent of tau and all numerical parameters. The adjoint (1,1) has q_7 = 0 modes but gives R approximately 0.42, far below the required approximately 33.

These five closures map onto a clear experimental logic. Closures 1-2 show that the intra-sector eigenvalue spacing cannot produce R = 33 (the atmospheric/solar mass ratio from Super-K + SNO + KamLAND). Closure 3 shows that U(2)-preserving deformations cannot produce mixing (the misalignment that would create nonzero theta_12, theta_23, theta_13 from Daya Bay and the global fit). Closure 4 proves the coupling mechanism is structurally bounded below the observed R * sin^2(2theta_23). Closure 5 blocks the inter-sector escape route algebraically.

The pattern across these five closures is worth stating explicitly. Each attempt approached PMNS from a different mathematical direction -- tight-binding H_eff (Closure 1), BCS-corrected couplings (Closure 2), eigenspace misalignment (Closure 3), analytic bounds on coupling matrices (Closure 4), and representation-theoretic weight analysis (Closure 5). They were not five failed attempts at the same calculation. They were five independent routes, each exploiting a different algebraic or dynamical mechanism, each closed by a different structural obstruction. The diversity of the closures is itself informative: it is not that one particular coupling is too small or one particular matrix element vanishes. It is that the U(2) symmetry preserved by the Jensen deformation enforces zero mixing through Schur's lemma, and this enforcement operates at every level -- eigenvalues, eigenvectors, couplings, and selection rules simultaneously.

From the experimentalist's perspective, what this means is clear. Daya Bay measured sin^2(2theta_13) = 0.0851 at 2.8% precision (Paper 10). Super-K established sin^2(2theta_23) near 1.0 at better than 10% (Paper 07). SNO + KamLAND determined sin^2(2theta_12) = 0.86 at approximately 5% (Papers 08, 09). These are not approximate or ambiguous measurements. Any framework claiming to derive the PMNS matrix must produce nonzero values for all three mixing angles. Producing exactly zero for all three is not "close to the data" -- it is maximally distant from it.

The PMNS sector is not "slightly wrong." On the Jensen curve, the mixing angles are zero -- infinitely far from the measured values at ANY confidence level.

---

## 3. Does R = 27.2 Match Oscillation Data?

The short answer: R = 27.2 at the fold is 19.5% below the measured R = 33.8, but this is potentially consistent because R(tau) is a steep function and the physical exit tau is undetermined.

The longer answer requires care.

**What R = 27.2 implies for mass splittings.** If we fix Delta m^2_21 = 7.41e-5 eV^2 (measured), then R = 27.2 gives Delta m^2_32 = 2.01e-3 eV^2. The measured value is |Delta m^2_32| = 2.507e-3 eV^2 (NuFit-6.0, normal ordering). Deficit: 2.01 vs 2.507, a 20% shortfall. This is outside the 1 sigma experimental uncertainty (sigma approximately 0.03e-3 eV^2) but within the framework's theoretical uncertainty on the exit tau.

**The tau-R gradient.** Near the fold: dR/dtau approximately 1900 at tau = 0.20 (from the tabulated values: R increases from 18.9 at tau = 0.18 to 27.2 at tau = 0.20 to 59.8 at tau = 0.24). To hit R = 33.8 requires tau approximately 0.207. The fold is at tau = 0.190. So the required exit tau is 0.017 above the fold -- approximately 9% of the fold value. The steep gradient means a small shift in exit dynamics could place R at the correct value, but it equally means the prediction is sensitive to transit dynamics that are NOT under control (FRIED-39: 133,000x dwell time shortfall).

**Comparison to JUNO precision.** JUNO's first results (November 2025) improved Delta m^2_21 precision by 1.6x from 59 days of data. With full exposure, JUNO will measure Delta m^2_21 at sub-percent precision and Delta m^2_32 at approximately 0.5% precision. At that precision, R will be known to approximately 1%. The framework's prediction at the fold (R = 27.2) will be excluded at approximately 20 sigma unless the exit tau is shifted from the fold to approximately 0.207. The framework must predict the exit tau to approximately 0.3% (delta_tau approximately 6e-4) to match JUNO-era precision on R. No transit dynamics computation has achieved this.

**Comparison to other frameworks.** For context: anarchic neutrino mass models (Hall, Murayama, Weiner) predict R approximately O(1) from random matrix statistics. The observed R = 33.8 is already a non-trivial feature requiring explanation. That R(tau) sweeps through this value near the geometrically distinguished van Hove fold is a genuine structural result -- it is not fine-tuned or parameter-fit. The question is whether the framework can pin down the exit tau to place R at 33.8 rather than at 27.2 or 59.8.

**My assessment.** R = 27.2 is in the right ballpark -- it is the correct order of magnitude and has the correct sign (R >> 1, not R approximately 1 as anarchy models predict). The steep tau dependence means the framework is not excluded by R, but it is also not constrained by R until the exit tau is determined independently. R survives as a structural feature but fails as a precision prediction.

---

## 4. The Off-Jensen Route: Computable or Not?

The atlas identifies three surviving mechanisms (D05, Section III), of which only one -- Window 3: Off-Jensen 5D moduli landscape -- is relevant to the PMNS problem. The question is whether U(2)-breaking deformations can generate nonzero mixing angles.

**What off-Jensen deformation means physically.** The Jensen curve is a 1-parameter family of left-invariant metrics on SU(3) that preserves a U(2) subgroup. Breaking U(2) opens a 5-parameter family (within U(2)-invariant metrics) or the full 28-parameter family of left-invariant metrics. On the Jensen curve, Schur's lemma locks the B1, B2, B3 eigenspaces into diagonal overlap (Closure 3). Off-Jensen, this lock breaks and eigenspace rotation becomes possible.

**What the atlas shows about computability.** The off-Jensen Dirac spectrum has been computed at single points (S41 W1-1: epsilon = 0.1 along g_73 direction, BCS gap within 0.17% of Jensen). The eigenvalue splitting is quadratic in epsilon (B2 quartet splitting 4.9e-5 at epsilon = 0.1). But the PMNS overlap matrix has never been computed off-Jensen. The tools exist: the Dirac operator D_K is constructed from the left-invariant metric and Levi-Civita connection, the eigenvalue problem is standard numpy diagonalization, and the PMNS overlap is a 3x3 matrix of inner products between eigenspaces at two different metric points. Estimated computational cost: 2-5 hours per off-Jensen point (D05, Window 3).

**What off-Jensen can and cannot deliver.** Even if off-Jensen deformations produce nonzero mixing angles, there are structural limitations:

1. The B2-SPLIT-41 proposed gate asks whether intra-B2 quartet splitting relative to B2-B1 splitting gives approximately 1/33 (the Delta m^2_21 / Delta m^2_32 ratio). At epsilon = 0.1: ratio = 4.9e-5 / 0.019 = 0.0026, which is 13x too small. The full 28D scan has not been performed.

2. Off-Jensen breaks U(2) and allows B1-B3 2x2 rotation. But 2x2 rotation gives at most TWO nonzero mixing angles (theta_12 and theta_13). Full 3x3 PMNS requires three independent rotations. K7-G1-37 proved algebraically that the (1,0) sector cannot contribute q_7 = 0 modes for the third rotation. The off-Jensen route therefore faces the same algebraic obstruction for full 3x3 mixing.

3. The HESS-40 result (all 22 transverse Hessian eigenvalues positive, minimum +1572) means the Jensen fold is a 28D local minimum of the spectral action. Off-Jensen deformations INCREASE the spectral action. Any physical mechanism selecting off-Jensen configurations must overcome this gradient.

**My verdict on computability.** The 2x2 off-Jensen PMNS overlap is computable within one session. The question is well-posed, the code infrastructure exists, and the computation is not prohibitively expensive. But even a successful computation (nonzero theta_12 and theta_13 within PDG ranges) would not solve the PMNS problem completely, because the third angle (theta_23) and the CP phase (delta_CP) require either full 3x3 mixing (blocked by K7-G1-37) or a qualitatively different mechanism such as internal MSW during transit (proposed gate MSW-INTERNAL-41, never computed).

---

## 5. KATRIN, JUNO, and the Absolute Mass Scale

The framework's absolute mass predictions face a scale bridge problem that I consider existential -- not merely difficult, but structurally incoherent in the current formulation.

**The numbers.** D_K eigenvalues at the fold: B1 = 0.819 M_KK, B2 = 0.845 M_KK, B3 = 0.982 M_KK (S39). Physical neutrino masses from oscillation: m_2 >= 0.009 eV, m_3 >= 0.05 eV (normal ordering, NuFit-6.0). KATRIN: m_nu < 0.45 eV (90% CL, Paper 12). Planck+DESI: sum(m_i) < 0.064 eV (LCDM). If D_K eigenvalues ARE neutrino masses (times M_KK), then sum(m_i) = (0.819 + 0.845 + 0.982) * M_KK < 0.064 eV forces M_KK < 0.024 eV. But gauge coupling matching (S41 W1-4) gives M_KK = 10^9 GeV (Convention A) or 10^13 GeV (Convention C). The discrepancy is 10^{10} to 10^{14}.

**The standard NCG resolution -- and why it fails here.** In Chamseddine-Connes NCG, the seesaw mechanism generates small neutrino masses from a heavy right-handed Majorana mass M_R approximately 10^{11}-10^{13} GeV embedded in the Dirac operator of the finite space F. The effective light neutrino mass is m_nu approximately v^2 / M_R approximately 0.1 eV. But Session 41 (W1-2) proved S_F^Connes = 0 identically on the phonon-exflation SU(3) due to BDI T-symmetry: the bilinear form C_2 * D_K is symmetric, and symmetric bilinear forms vanish on Grassmann variables. The standard NCG seesaw does not operate.

**What KATRIN constrains.** KATRIN measures the effective electron neutrino mass m_beta = sqrt(sum |U_{ei}|^2 m_i^2) near the tritium endpoint at 18.574 keV (Paper 12, Paper 01). The current bound m_beta < 0.45 eV translates to: whatever mechanism maps D_K eigenvalues to physical masses must produce m_beta below this threshold. The framework's near-degenerate eigenvalue structure (0.82 : 0.84 : 0.98) predicts m_beta approximately m_lightest * sqrt(1 + small corrections), which for normal ordering with m_1 approximately 0 gives m_beta approximately 0.009 eV -- far below KATRIN's current sensitivity but accessible to Project 8 (target: 40 meV, Phase III development).

**What JUNO constrains.** JUNO's primary neutrino mass contribution is the ordering determination. The framework predicts normal ordering (B1 < B2 < B3, structural theorem). If JUNO determines inverted ordering at 3 sigma (expected approximately 2030 with 6.5 years), the entire neutrino sector closes. If normal ordering is confirmed, the framework's sole surviving neutrino prediction is validated. JUNO's precision on Delta m^2_21 (sub-percent with full exposure) will constrain R to approximately 1%, which at the framework's steep dR/dtau gradient near the fold translates to a tau determination of approximately 6e-4 -- an extraordinarily sharp constraint on exit dynamics.

**The meV mass window.** Combining oscillation lower bounds (sum m_i >= 0.06 eV for normal ordering) with cosmological upper bounds (sum m_i < 0.064 eV in LCDM from Planck+DESI), the allowed window is 0.06-0.064 eV for the sum. The framework's eigenvalue ratio structure predicts m_1 : m_2 : m_3 approximately 0.819 : 0.845 : 0.982 (up to overall scale). With sum = 0.062 eV: m_1 = 0.019 eV, m_2 = 0.020 eV, m_3 = 0.023 eV. This is the quasi-degenerate scenario. But the measured mass splittings give m_3 approximately 0.05 eV >> m_1 for normal ordering with m_1 near zero -- the hierarchical scenario. The framework's near-degenerate eigenvalue ratios (within 20% of each other) are inconsistent with the hierarchical mass pattern unless the scale bridge introduces a nonlinear mapping from D_K eigenvalues to physical masses. The ratios 0.82 : 0.84 : 0.98 map to R = 27.2, but the actual mass ratios are approximately 0 : 0.009 : 0.05 (assuming m_1 approximately 0), giving ratios approximately 0 : 1 : 5.6. The D_K eigenvalue ratios are not the physical mass ratios -- they are the mass-squared-difference ratios only if the mapping is linear. This distinction matters.

**Dirac vs Majorana.** The BDI classification with J^2 = +1 permits Majorana mass terms in principle (S17c). But WIND-36 found the BCS winding number nu = 0 (topologically trivial), and S_F^Connes = 0 closes the standard NCG Majorana channel. The sole remaining fermionic bilinear on SU(3) is S_F^Pfaff (involving the BCS anomalous density), which is nonzero and has never been evaluated for mass generation. Current experimental constraints: KamLAND-Zen sets T_1/2(0nu-beta-beta) > 3.8e26 yr in Xe-136, constraining the effective Majorana mass m_ee < 28-122 meV (Paper 05, oscillation formalism). LEGEND-200 combined with GERDA and MAJORANA gives T_1/2 > 1.9e26 yr in Ge-76. For normal ordering with m_1 near zero, the predicted m_ee falls in the 1-4 meV range -- below all current and planned experiments except hypothetical ton-scale detectors. LEGEND-1000 (planned, targeting T_1/2 approximately 10^28 yr) would cover the entire inverted hierarchy band (m_ee > 15 meV) but would not reach the normal hierarchy prediction. The Majorana/Dirac question therefore remains experimentally untestable within the framework for normal ordering.

**Experimental timeline for framework tests.** The critical dates:

| Experiment | Date | Measurement | Framework test |
|:-----------|:-----|:------------|:---------------|
| JUNO (operating) | 2025-2026 | Delta m^2_21, theta_12 at sub-percent | Sharpens R = 33.8 target to 1% |
| KATRIN (running) | 2025-2026 | m_beta < 0.3 eV (target) | Marginal -- framework predicts 0.009 eV |
| JUNO (full exposure) | approximately 2030 | Mass ordering at 3 sigma | DECISIVE: normal = framework survives, inverted = neutrino sector closed |
| DUNE (Phase I) | early 2030s | Ordering at 5 sigma, delta_CP | Confirms/refutes ordering; tests delta_CP (framework has no prediction on Jensen) |
| Hyper-K (data-taking) | 2028+ | CPV, ordering, proton decay | Complementary to DUNE at 295 km baseline |
| Project 8 (Phase III) | 2030s | m_beta at 40 meV | Could reach framework's predicted m_beta approximately 0.009-0.02 eV |
| LEGEND-1000 | 2030s | T_1/2 approximately 10^28 yr (Ge-76) | Covers IO m_ee band; does not reach NO prediction |
| nEXO | 2030s | T_1/2 approximately 10^28 yr (Xe-136) | Similar reach to LEGEND-1000 |

---

## Closing Assessment

The neutrino sector has three layers: one that survives, one that is structurally broken, and one that has never been computed.

**What survives.** Normal ordering (B1 < B2 < B3) is a structural, parameter-free prediction that current data prefer at 2.5 sigma and that JUNO/DUNE will test definitively by approximately 2030-2032. The NNI texture (V_11 = 0, V_13 = 0) qualitatively reproduces the observed hierarchy theta_12 >> theta_13. R sweeps through the correct value near the fold, meaning the atmospheric/solar mass ratio is geometrically accessible. These are Level 3-4 predictions: structural features that survive all 51 sessions.

**What is broken.** PMNS mixing angles are zero on the Jensen curve. Five independent closures, culminating in the algebraic K7-G1-37, leave no room for improvement within the 1-parameter Jensen family. The absolute mass scale bridge is incoherent: D_K eigenvalues at O(1) * M_KK cannot be identified with sub-eV neutrino masses without either a seesaw (blocked by S_F^Connes = 0) or an implausibly low M_KK (contradicting gauge coupling matching by 10^{10} orders). These are not technical problems awaiting a better computation -- they are structural obstructions within the current mathematical framework.

**What remains uncomputed.** The off-Jensen PMNS overlap (2x2 partial, approximately 2-5 hours per point). The internal MSW mechanism during transit (proposed S41, never tested). The B2 quartet splitting as Delta m^2_21 source (B2-SPLIT-41, requires off-Jensen eigenvalue scan). The S_F^Pfaff Majorana channel (the only nontrivial fermionic bilinear on SU(3), never evaluated for mass generation).

**Should the framework abandon PMNS claims?** The question admits a precise answer structured by what can and cannot be claimed given the current constraint surface.

The framework should NOT claim to predict PMNS mixing angles until either (a) an off-Jensen computation produces nonzero mixing within 3 sigma of NuFit-6.0 values, or (b) a new mechanism (internal MSW, transit-induced mixing) passes a pre-registered gate. Any paper or presentation stating that the framework "predicts" mixing angles in the current state would be experimentally indefensible.

The framework SHOULD claim normal ordering and the NNI texture as structural predictions, since these are proven theorems (Schur's lemma, Trap 1, Trap 4) independent of the mixing angle problem. These survive regardless of whether the off-Jensen computation succeeds or fails.

The framework SHOULD acknowledge that R = 27.2 is in the correct ballpark but is not a precision prediction until the exit tau is determined by an independent dynamical computation. The steep gradient dR/dtau approximately 1900 makes this a tau-exit constraint, not a mass hierarchy prediction.

The framework MUST resolve the scale bridge before ANY absolute mass prediction can be compared to KATRIN, JUNO, or cosmological bounds. The 10^{10}-10^{14} discrepancy between D_K eigenvalues (at M_KK) and physical neutrino masses (sub-eV) is not a parameter-tuning problem -- it requires identifying a specific suppression mechanism that operates on SU(3) where the standard NCG seesaw provably vanishes.

**Pre-registered gates for future sessions.** Based on this review, I recommend the following neutrino-sector gates:

| Gate | Criterion | PASS | FAIL |
|:-----|:----------|:-----|:-----|
| PMNS-OFFJENSEN-52 | sin^2(theta_12) in [0.25, 0.35] at any off-Jensen point | Mixing exists; compute theta_23, theta_13 | U(2) breaking insufficient; Level 5 permanent |
| B2-SPLIT-SCAN-52 | Intra-B2 splitting / (B2-B1 splitting) in [0.02, 0.05] at any direction | Delta m^2_21 from geometry identified | B2 quartet too degenerate for solar splitting |
| SCALE-BRIDGE-52 | Identified mechanism maps 0.82 M_KK to sub-eV with M_KK > 10^6 GeV | Neutrino masses derived | Scale bridge closed; neutrino sector structurally incoherent |
| MSW-INTERNAL-52 | Mode-dependent LZ transition gives sin^2(theta_23) in [0.3, 0.7] | Transit mixing viable | Internal MSW too weak; another closure |

The neutrino sector is not dead. Normal ordering is a genuine, falsifiable prediction that the next generation of experiments will test. But the mixing angle sector requires mathematics that does not yet exist within the framework, and the absolute mass scale requires physics that has not been identified. These are the walls. The door is off-Jensen deformation and transit dynamics. The window is JUNO's mass ordering determination, expected approximately 2030.

---

*Sources: Atlas D01-D05, D08. NuFit-6.0 (arXiv:2410.05380). Papers 01-12 in researchers/Neutrino-Detection/. Gate registry at .claude/agent-memory/neutrino-detection-specialist/gate-registry.md. Session results from S29, S34, S35, S36, S37, S39, S40, S41.*
