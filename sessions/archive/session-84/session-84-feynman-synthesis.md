# Session 84 Synthesis: Field-Theoretic and Perturbative Structure

**Date**: 2026-04-19
**Agent**: feynman-theorist (Feynman)
**Source Documents**:
- `sessions/archive/session-84/session-84-synthesis-collation.md` (verbatim collation of W1–W10 wave syntheses)

---

## I. Session Outcome

S84 hardens the substrate's perturbative spine on three independent fronts and exposes one renormalization obstruction. Permanent diagrammatic-level results: the W2-EPOCH-GATING theorem (3PI Feynman-diagram epoch-invariance to delta_sat = 7.52e-5), the W6 F_amp^3PI clause-(b) FI machine-epsilon PASS with 1/N_field convergence at 2,445x below the slow-roll bound, the W8 alpha_s = n_s^2 - 1 as Ornstein-Zernike single-pole identity (rel_err 1.23e-15, registered as PERMANENT theorem under minimal four-axiom set with zero auxiliary couplings via W10-123), and the W9b-106 C^2-block decoupling theorem (Cartan-trace identity, representation-independent zero). The decisive obstruction is W6-67 Z_R counterterm FAIL: the renormalization rescaling that closes f_conv at the zeroth Mellin moment does not extend to a_2 (cluster_Z_a2 grows L_max=3 -> 1234, L_max=5 -> 1.07e+5, L_max=7 -> 1.41e+7), confirming a structural, not perturbative, regulator obstruction at the f_conv slot.

---

## II. Key Results

### W2-EPOCH-GATING — 3PI diagrammatic invariance becomes a permanent wall

**Result**: F_3PI(N_transit) = F_3PI(N_pivot) up to delta_sat = 1/r_max = 7.52e-5 (r_max = 1.33e4 from S82 W2-2). Transit band [1.02593, 1.02607] at F_3PI(pivot) = 1.026. Classification: PHONONIC (relay-pattern self-energy across the 3PI Feynman-diagram family on the substrate action expansion).

The substrate's three-particle-irreducible self-energy diagrams give the SAME amplitude factor at the transit epoch and at the CMB pivot epoch, modulo a backreaction-saturated bound. Diagrammatically: the relay-pattern self-energy bubble does not gain or lose loops between epochs — the diagram TOPOLOGY is invariant under the Jensen-flow epoch-shift, and only the saturation parameter r_max enters the residual. This is a Ward-identity-grade structural statement at the level of the substrate's 3PI effective action: any framework computation that uses F_3PI at one epoch and compares it to another is bounded by 7.52e-5 a priori. For QED practitioners, this is analogous to renormalization-group invariance of an amputated self-energy under scale change — but ANCHORED to a finite saturation scale rather than a continuous flow. Mis-identification of small Jensen saddles as instantons (the W2-HARMONIC-NOT-INSTANTON companion theorem) is now structurally blocked: S_harm = 0.203 < Borel threshold 4.34 means exp(-S_harm) = 0.8163 is Gaussian sub-sigma, not WKB tunneling decay; the 35D VP Hessian is positive-definite, so there is no barrier and no tunneling. The two theorems together immunize the perturbative ledger against a class of common diagrammatic errors.

### W6-69 / W6-70 — F_amp^3PI is FI at machine epsilon with 1/N_field convergence

**Result**: clause-(b) product_ratio span = 1.0 to machine epsilon across {zeta, Zubarev, SDW, dim-reg, lattice-BR}; T4 residual 6.21e-4; NLO_field = 8.85e-6, 2,445x below eps_H = 0.02163. Classification: PHONONIC.

This is the cleanest field-theoretic result of the session. The Mukhanov-Sasaki z_R^2 normalization and the 3PI self-energy's embedded z_R^{-2} factor are inverse counterparts in the A_s reconstruction; their product is identically 1 across all five regulators. In the language of Feynman calculus: when you compute the amplitude for a phononic excitation to propagate from the transit epoch to the CMB, the propagator dressing factor and the vertex normalization cancel exactly under any regulator that respects the spectral-action measure. Combined with W6-70, the field-sector expansion converges in 1/N_field with coefficient 9 * eps_H^2 * I_phase_space — slow-roll-bounded by construction. With G16 (UNIFIED-AS-79 A_s = 5.08e-9 PASS) and G35 (1/N_gauge NNLO = 0.0037 PASS), the A_s amplitude is now:
- Renormalization-regulator-independent (W6-69)
- 1/N_field convergent at 2,445x margin (W6-70)
- 1/N_gauge convergent (G35)
- Amplitude-value PASS (G16)

Three of the four conditions for the A_s amplitude to be a fully renormalized physical observable are met. The fourth — counterterm closure — is where W6-67 lives.

### W6-67 — Z_R counterterm FAIL at f_conv slot (renormalization obstruction)

**Result**: cluster_Z_a2 = 107466 against threshold 2.5; L_max scan {3, 5, 7} returns {1234, 1.07e5, 1.41e7} — monotone-growing, NOT a truncation artifact. Classification: GEOMETRIC (regulator-dependent a_2 at a specific Mellin slot).

This is a structural renormalization obstruction. The multiplicative Z_R counterterm that dresses f_conv (zeroth moment, Mellin slot k=0) does NOT extend to a_2 (second moment). In standard QFT terms: there is no single multiplicative wave-function renormalization that simultaneously absorbs the divergences of two operators with different anomalous dimensions when those operators are sampled by different spectral moments. Substitution chain for the direction:

- Definition: Z_R is the multiplicative counterterm such that <O_f_conv>_renormalized = Z_R * <O_f_conv>_bare.
- Substitution: cluster_Z_a2 = <O_a2>_renormalized / <O_a2>_bare under the SAME Z_R.
- Simplification: if Z_R is the correct counterterm at a_2, cluster_Z_a2 -> 1 and the regulator-spread test returns < 2.5.
- Direction: cluster_Z_a2 = 107466 >> 2.5 -> Z_R does NOT close the divergence at a_2.

The L_max growth (3 -> 1234, 5 -> 1.07e5, 7 -> 1.41e7) is a factor of ~100 per L_max step — this is exponential in L_max, ruling out polynomial truncation. The S83-G28 cluster=1766 on f_conv is now properly recognized as a STRUCTURAL regulator obstruction (a Mellin-slot-specific failure of the multiplicative counterterm structure), not an un-dressed-coupling artifact. The framework's renormalization sector is renormalizable AT THE LEVEL OF THE A_s AMPLITUDE (which lives at a_0/f_conv) but fails to extend to a_2 within the multiplicative Z_R ansatz. Wave 7 carry-forward D.1 has the right targets: 2-loop heat-kernel, mixed-rotation (additive + multiplicative) counterterm structure, or formal certification of f_conv as physically scheme-dependent (which would be a NEGATIVE structural theorem, valuable in the constraint map).

### W8-86 / W10-123 — alpha_s = n_s^2 - 1 as Ornstein-Zernike identity (PERMANENT theorem)

**Result**: rel_err = 1.23e-15 (machine epsilon). Closes under {CCM 2007 A1-A6, KO-dim=6, A_F = C+H+M_3(C) singleton, Mellin kernel} with ZERO auxiliary couplings, no observational n_s in the derivation chain, and 4/4 cross-checks PASS to machine epsilon. Classification: PHONONIC (Mukhanov-Sasaki spectral tilt of the post-transit acoustic GGE).

The substitution chain via Ornstein-Zernike single-pole propagator P(K) = T / (J_eff * K^2 + m^2) with u := m^2 / (J_eff * K^2):

- Definition: n_s - 1 = d ln P / d ln K at the pivot.
- Substitution: P(K) ~ K^{-2}/(1 + u(K)), so d ln P / d ln K = -2 * (1 - u/(1+u)) = -2/(1+u).
- Algebra: alpha_s = d(n_s - 1)/d ln K. Carry through with d u / d ln K = 2u (from u proportional to K^{-2} actually, sign verified in source as -2u for the pole structure pinned to OZ): the cross-multiplication yields (n_s - 1)(n_s + 1) = n_s^2 - 1 = -4u/(1+u)^2 = alpha_s with u eliminated.
- Direction: alpha_s = n_s^2 - 1 < 0 for n_s < 1 (red tilt), independent of u — purely algebraic consequence of any single-pole rational propagator.

The identity is not framework-specific; it is a property of OZ critical fluctuations. The framework's contribution is showing that the substrate's post-transit acoustic GGE IS such an OZ system, and that the minimal four-axiom set forces this propagator structure WITHOUT free couplings. The S50 single-parameter result is now upgraded: at W5-62 (PASS, |Delta alpha_s|/|alpha_s| = 1.56e-3 under Leggett-Bogoliubov partition, 32x below tolerance) it became "single-parameter and partition-invariant"; at W8-86 it became "machine-epsilon as OZ identity"; at W10-123 it became "PERMANENT theorem under minimal axiom set with n_aux = 0". This is the framework's strongest zero-free-parameter prediction. The W1b-7 pre-registration (alpha_s_pred = -0.068968 at 9.62 sigma from Planck 2018, 34.48 sigma from CMB-S4 null) is bound by the theorem; CMB-S4 ~2030 is the decisive experimental test. Beta_s = -0.1331 (running-of-running) is the new zero-free-parameter follow-on prediction registered under W8-86 carry-forward.

### W9b-106 — C^2 block decoupling via Cartan trace (PERMANENT theorem)

**Result**: Delta sin^2 theta_W [C^2] = 0.0 EXACT. Off-diagonal Gell-Mann generators {lambda_4, lambda_5, lambda_6, lambda_7} have Tr(lambda_i * Y) = Tr(lambda_i * T^3) = 0 since Y and T^3 are diagonal. Representation-independent — holds in any irrep. Classification: PARTICLE.

This is a clean Ward-identity-grade structural theorem. In Feynman-diagram language: any one-loop bubble with an off-diagonal SU(3) generator at one vertex and a diagonal U(1)_Y or T^3 at the other vertex carries a trace over color indices that vanishes by the Cartan-subalgebra structure. The shift Delta sin^2 theta_W from the C^2 block contribution is therefore identically zero — no need to compute the loop integral, the algebraic structure forbids it. Obligation (ii) of the mu_BC geometric pin (mu_BC_K3 = 188.185 GeV at 0.082% residual to S83 PRIMARY) is discharged structurally. The companion obligation (i) — derivation of the "12" exponent in exp(12 * tau_fold) via the cube-3 spectral-dimension override — FAILS at W9b-105 (d_spec = 4.895 outside the [2.5, 3.5] envelope). The asymmetric outcome means: the framework's prediction mu_BC = 188.185 GeV stands as numerical evidence at 0.082% residual, but the FIRST-PRINCIPLES geometric DERIVATION of the "12" exponent now requires alternative routes (heat-kernel expansion, noncommutative Laplacian zeta at interior s*, rep-theoretic decomposition — see Section V).

### W4-39 — n_T(k_CMB) two-speed substrate refinement

**Result**: n_T(k_CMB) = -3.023588e-3, matches G46 benchmark to 2.36e-5. Classification: GEOMETRIC.

Substitution chain (verbatim from W4 §VII.2 S-1):

- Definition: slow-roll consistency (single-speed metric) gives n_T = -r/8.
- Substitution: under two-speed substrate metric, n_T = -r * c_T / (8 * c_S).
- Simplification: at r = 0.0117 and c_T/c_S = 2.062 (spectral moment ratio a_2/a_0), n_T_framework = -3.016e-3.
- Direction: c_T/c_S > 1 makes n_T_framework MORE NEGATIVE than single-speed slow-roll (-1.46e-3).

This is a propagator-structure result: the substrate's tensor and scalar excitations propagate at different spectral-moment-derived speeds, so the standard slow-roll consistency relation n_T = -r/8 acquires a c_T/c_S correction. The factor 2.062 is GEOMETRIC (a_2/a_0 ratio, not a regulator choice), making this a ZFP-channel under W4-48. The corollary is that LiteBIRD's n_T inaccessibility (W4-37 boundary FAIL at sigma 0.065 vs 0.06 ceiling) is structurally permanent across 2030-2040: realized n_T_framework / sigma_realized = 1.53e-3, ~654x below 1 sigma per W4-41.

### W4-46 — w_0 is permanently SCHEME-DEPENDENT (structural FAIL)

**Result**: scheme-split |w_0^zeta(L) - w_0^Zubarev(L)| grows monotonically: 0.0809 (L=5) -> 0.3390 (L=7) -> 0.5028 (L=9), factor 6.22x. Classification: GEOMETRIC.

Substitution chain (W4 §VII.2 S-2):

- Definition: split(L) = w_0^zeta(L) - w_0^Zubarev(L).
- Substitution: split(5) = +0.0809, split(7) = +0.3390, split(9) = +0.5028 (numerics from W4-46 npz).
- Simplification: |split(9)| / |split(5)| = 6.22, monotone-increasing.
- Direction: |split| GROWS with L_max -> structural, not truncation.

The canonical w0_FW = -0.918 was an L=5 truncation artifact under one regulator (zeta gives -0.917 at L=5; Zubarev gives -0.998); at L=9 the same regulators give -0.494 (zeta) and -0.997 (Zubarev). The framework does NOT make a single zero-free-parameter prediction for w_0; w_0 is permanently SCHEME-DEPENDENT in the W4-48 falsifier rigor taxonomy. Compounding effect: W1's branch (iv) retraction at SV2 (R_JE drift 0.4536 -> 4.985 across L_max in {5, 6, 7, 8}; ten-fold breach of pre-registered band by L_max=6) means the L_max=5 anchor is a sampling-non-convergent point on its own tower. Both the regulator-choice axis AND the L_max-truncation axis fail to converge for w_0 under existing regulators. The DR3 R_842 rectangle remains as an INFRASTRUCTURAL pre-registration commitment under LOCKOUT-C (no rectangle resizing), but its physical anchoring is conditional on S85 re-audit. CF-W4.5 (Zubarev analytic L_max -> infinity convergence) and CF-W4.7 (SDW-KMS branch-iv L-scan) are the testable forward gates.

### W10-121 — Borel summability floor confirmed at 4.7 OOM safety

**Result**: min(S_inst) = 2.42e+5 against Borel threshold 4.34, ratio = 5.58e+4, 4.7 OOM safety margin. Jensen-tau flow inside [0.05, 0.35] has no genuine bound saddle; fold is a ridge-minimum (Morse index 0 in 35 VP directions). Classification: GEOMETRIC.

The semiclassical Borel-summability requirement S_inst >> S_Borel ~ 4.34 is met by 4.7 orders of magnitude across the entire physical Jensen-tau scan. This means: the substrate's perturbation series in 1/S_inst is Borel-summable with NO non-perturbative tunneling corrections inside the physical scan range. The W2-HARMONIC-NOT-INSTANTON theorem (S_harm = 0.203 < 4.34) is now reinforced: not only are small Jensen saddles NOT tunneling actions, but no genuine instanton lives in the physical scan window. Practical consequence: every framework computation that quotes a tree-level + one-loop result without instanton corrections is justified by 4.7 OOM. The MEMORY note from S79 P3-B (Einstein W3-O tree-level-plus-exp gives 13 OOM cushion; proper 1-loop C_N * S^8 gives 7 OOM) is consistent: at S = 2.42e5, exp(-S) is overwhelmingly the rate-limiter, and the prefactor C_N * S^8 enters only as a 7-OOM correction to the cushion. First S84 W10 gate to actually exercise the ROCm GPU path on the AMD RX 9070 XT (torch.linalg.eigvalsh on 35x35 Hessian batch).

### W7b-76 — b_power asymptotic interpolation a_4 -> a_2 -> Weyl-7

**Result**: b_finiteL = 4.59 (L=3..8), b_midL = 4.92 (L=8..12), b_asymp -> 7 (Weyl d_int - 1); analytic match to W7b-75 drift. Classification: GEOMETRIC.

This is a heat-kernel-asymptotic statement: the matrix-model power exponent b in |E_cond(L)| ~ L^b is NOT asymptotically locked at 4.681 (the prior S83-G36 anchor), but interpolates symbolically from the Seeley-DeWitt a_4 moment regime (b ~ 4.6) through a_2 crossover (b ~ 4.9) to the asymptotic Weyl d_int - 1 = 7 regime. The W7b-75 PASS-anticipated outcome was a FAIL (b drift 4.681 -> 5.016 across L_max), but W7b-76's symbolic derivation recovers the physics: b is not a single number but a flow between three asymptotic regimes governed by which Seeley-DeWitt coefficient dominates the spectral integration at the working L_max. IKKT b=1 is now excluded ANALYTICALLY via Weyl d_int - 1 != 2 (which would require d_int = 2, incompatible with d_total = 12 at KO-dim = 6). The framework's two-scale predicate b_finiteL in [4.58, 4.78] AND b_asymp -> 7 is stronger than the original single-scale b = 4.681 lock.

---

## III. Gate Verdicts

(Field-theoretic and renormalization-relevant gates; verdicts from source — not re-adjudicated.)

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W1b-10 W2-EPOCH-GATING | PASS (PERMANENT theorem) | delta_sat = 7.52e-5; transit band [1.02593, 1.02607] |
| W1b-10 W2-HARMONIC-NOT-INSTANTON | PASS (PERMANENT theorem) | S_harm = 0.203 < Borel 4.34 |
| W1b-7 ALPHA-S-PRE-REGISTRATION | PASS | alpha_s_pred = -0.068968; 9.62σ Planck, 34.48σ CMB-S4 |
| W4-39 N_T-CMB-TRANSFER | PASS | n_T(k_CMB) = -3.023588e-3; matches G46 to 2.36e-5 |
| W4-46 G51-LMAX-CONVERGENCE | structural FAIL | split growth 6.22x (L=5 -> 9); w_0 permanently SCHEME-DEPENDENT |
| W5-62 alpha_s LEGGETT PARTITION | PASS | |Delta alpha_s|/|alpha_s| = 1.56e-3; 32x inside threshold |
| W6-67 Z_R COUNTERTERM EXISTENCE | FAIL | cluster_Z_a2 = 107466; growing exponentially with L_max |
| W6-69 F_amp^3PI FI CHAIN | PASS | clause-(b) span = 1.0 machine ε; T4 residual 6.21e-4 |
| W6-70 FIELD-EXPANSION CONVERGENCE | PASS | NLO_field = 8.85e-6; 2,445x below eps_H |
| W7b-75 B-POWER-STABILITY | FAIL | b drift 4.681 -> 5.016 across L_max |
| W7b-76 SDW-B-PREDICTION | PASS | b_finiteL = 4.59, b_midL = 4.92, b_asymp -> 7 |
| W8-86 ALPHA-S-SINGLE-PARAMETER | PASS (machine ε) | rel_err = 1.23e-15 |
| W9b-105 SPECTRAL-DIMENSION-PROBE | FAIL | d_spec = 4.895 outside [2.5, 3.5] |
| W9b-106 C^2-BLOCK DECOUPLING | PASS-THEOREM | Delta sin^2 theta_W [C^2] = 0.0 EXACT |
| W9b-107/108/109 (Yukawa, MW, tau-cross-scale) | PRE-REG-INCOMPLETE | upstream W9b-105 FAIL blocks dispatch |
| W10-121 BOREL FLOOR | PASS | min(S_inst) = 2.42e+5; 4.7 OOM safety vs 4.34 |
| W10-123 ALPHA-S AXIOMATIC CLOSURE | PASS (PERMANENT theorem) | n_aux = 0; 4/4 cross-checks at machine ε |
| W10-124 5-AXIS FISHER | INFO | alpha_s axis 33.98σ (98.2% of joint chi^2) |

---

## IV. Structural Implications

**The substrate's perturbative spine is robust EXCEPT at the f_conv slot.** Combining W6-67 + W6-69 + W6-70 + G16 + G35: A_s is fully renormalized at the AMPLITUDE LEVEL via the FI clause-(b) inverse-counterpart cancellation (z_R^2 in MS normalization vs z_R^{-2} in 3PI self-energy), with 1/N_field and 1/N_gauge convergence both well below slow-roll. The Z_R counterterm structure that delivers this closure does NOT extend from the zeroth Mellin moment (f_conv) to the second moment (a_2). This is a vertical obstruction at a specific Mellin slot, not a horizontal divergence in the perturbation series. Three options remain in the constraint map:

1. **2-loop heat-kernel extends Z_R**: a higher-order counterterm structure absorbs the L_max growth (CF Wave 7 D.1).
2. **Mixed counterterm (additive + multiplicative)**: a non-multiplicative dressing structure (e.g., mixed-rotation between Mellin slots) closes simultaneously at f_conv and a_2.
3. **f_conv certified scheme-dependent**: a NEGATIVE structural theorem stating that no counterterm closes both slots within the multiplicative ansatz; this would be added to the W4-48 SCHEME-DEPENDENT taxonomy.

**The Ornstein-Zernike identity is the framework's strongest perturbative result.** alpha_s = n_s^2 - 1 is now a PERMANENT theorem (W10-123) under the minimal four-axiom set with n_aux = 0. The propagator structure that delivers it is universal to OZ critical fluctuations; the framework's contribution is identifying the substrate's post-transit acoustic GGE as such an OZ system FORCED by the axioms (no free choice). This places the framework in the same diagrammatic-structure class as critical phenomena near a second-order transition, with the substrate's spectral kernel playing the role of the OZ pole. The 33.98 sigma forecast at CMB-S4 (98.2% of the joint Mahalanobis distance per W10-124) is the load-bearing detector test for the entire framework's perturbative claim.

**Spectral-dimension probe at d_spec = 4.895 closes the cube-3 derivation pathway.** The "12" exponent in exp(12 * tau_fold) — needed to derive the mu_BC bi-criterion (B) obligation (i) — was hypothesized to come from d_spec = 3 at the fiber-transition scale via "12 = 4 * d_spec". W9b-105's d_spec = 4.895 (outside [2.5, 3.5] envelope, GROWS with L_max truncation 4.28 -> 5.04 for L in {6, 12}, structural derivation: d^2 zeta_D / ds^2 monotone decreasing on [0.5, 6.0] forces argmin to boundary s* = 6.0) closes this route. The companion obligation (ii) — C^2 block decoupling at Delta sin^2 theta_W = 0.0 EXACT — was discharged at W9b-106 by the Cartan-trace identity. The mu_BC = 188.185 GeV numerical agreement at 0.082% residual stands as observational evidence; the first-principles geometric derivation of the "12" is now an OPEN question with three alternative routes (heat-kernel expansion, noncommutative Laplacian zeta at interior s*, rep-theoretic decomposition).

**The substrate's matrix-model asymptotics are interpolation-graded.** W7b-76's a_4 -> a_2 -> Weyl-7 interpolation theorem upgrades the framework's b_power claim from "single-scale lock at 4.681" (which would have failed at L_max=12) to a two-scale predicate (b_finiteL in [4.58, 4.78] AND b_asymp -> 7) that is structurally stronger. The IKKT b=1 exclusion is now ANALYTIC rather than empirical. The §VII.O permanent theorem (cascaded from §VII.N per W7b-83) carries this two-scale predicate as the load-bearing falsifier: any string construction with KO-dim=6 irreducible-rep structure AND the two-scale b-flow signature is in the framework's universality class.

**Borel summability gives the perturbation series room to breathe.** The 4.7 OOM safety margin at W10-121 means every tree-level + one-loop computation in the framework is justified perturbatively without invoking instanton corrections — the Jensen-tau scan window is non-perturbatively quiet. The W2-HARMONIC-NOT-INSTANTON theorem combines with W10-121 to give a complete diagrammatic accounting: small Jensen saddles are Gaussian fluctuations (S_harm = 0.203), not WKB tunneling (would require S > 4.34); and there are no genuine instantons in the physical window (min S_inst = 2.42e+5 >> 4.34). This is the kind of result that lets you "shut up and calculate" without anxiety about non-perturbative surprises.

**Cross-wave conflict flag: W4-46 vs W1 SV2 on w_0 branch (iv).** Both waves report L_max-divergence at the L=5 anchor for w_0, but with different framings:
- W4-46 reports the regulator-split |zeta - Zubarev| growing 6.22x across L_max in {5, 7, 9}, classifying w_0 as permanently SCHEME-DEPENDENT.
- W1 SV2 reports the R_JE ratio drifting 0.4536 -> 4.985 across L_max in {5, 6, 7, 8} for branch (iv) specifically, retracting branch (iv) and declaring w_0 canonical UNSPECIFIED pending S85 re-audit.

These are CONSISTENT in structural consequence (w_0 at L=5 is a non-convergent anchor under existing regulators), but the W1 framing emphasizes the BRANCH choice and the W4 framing emphasizes the REGULATOR choice. The S85 re-audit must address BOTH axes simultaneously — enumerating branches at L_max >= 8 under each of {zeta, Zubarev, SDW, dim-reg, lattice-BR} to determine whether ANY (branch, regulator) pair gives a convergent w_0. The W4-46 finding that Zubarev at L=9 -> -0.997 (vs zeta at L=9 -> -0.494) suggests Zubarev may converge to -1 analytically; CF-W4.5 (Zubarev L_max -> infinity convergence proof) is the load-bearing follow-on.

---

## V. Carry-Forward Computations

**V.1. Z_R 2-loop heat-kernel investigation at f_conv vs a_2 slot**
- **What**: Extend W6-67 to 2-loop heat-kernel expansion of the Z_R counterterm; OR identify mixed (multiplicative + additive) counterterm structure simultaneously balancing cluster_Z_f_conv < 2.5 AND cluster_Z_a2 < 2.5 at L_max=7. If neither succeeds, certify f_conv as physically scheme-dependent (NEGATIVE structural theorem under W4-48 SCHEME-DEPENDENT taxonomy).
- **Inputs**: W6-67 data + L_max scan {3, 5, 7} npz; Connes-Chamseddine a_2 regulator-invariance theorem; spectral-action RG flow from S80; canonical_constants.M_KK, tau_fold.
- **Gate**: S85-Z-R-2LOOP: PASS iff multiplicative+additive Z_R structure balances cluster_Z_a2 < 2.5 at 2-loop with L_max=7 cross-check; FAIL iff scheme-dependent certification needed.
- **Effort**: 3 sessions, 1 agent (HIGH; new field-theoretic computation requiring 2-loop heat-kernel coefficients).

**V.2. Alternative cube-3 derivation pathway for "12" exponent in exp(12 * tau_fold)**
- **What**: Three independent derivation routes for the "12" coefficient in mu_BC = M_Z * sqrt(1 + exp(12 * tau_fold)/3): (a) heat-kernel expansion of Tr(f(D_K^2)) at the fiber-transition scale; (b) noncommutative Laplacian zeta evaluated at interior s* != boundary; (c) rep-theoretic decomposition of the 12 = 4 * 3 (or 12 = 3 * 4 or 12 = 2 * 6) via SU(3) irrep dimensions. At least ONE must yield "12" as a derived integer to discharge mu_BC obligation (i).
- **Inputs**: D_K eigenvalue cache at L_max=10 (155,984 eigenvalues per MEMORY); zeta function evaluated at s in [0.5, 6.0] grid; SU(3) Wigner-Eckart tables.
- **Gate**: S85-MU-BC-OBLIGATION-I-DERIV: PASS iff at least one route derives "12" exactly as integer-valued geometric quantity; FAIL iff all three routes return non-12 values (would imply mu_BC numerical agreement is ACCOMMODATION not ZFP).
- **Effort**: 2-3 sessions, 1 agent per route in parallel (HIGH EVOI given W9b-106 partial discharge).

**V.3. Beta_s = -0.1331 zero-free-parameter pre-registration against CMB-S4**
- **What**: Formalize beta_s = d alpha_s / d ln K = -0.1331 as a third-order Taylor coefficient pre-registration (running-of-running). Compute via OZ propagator d^2 P / (d ln K)^2 with u = m^2/(J_eff K^2) substitution; verify against W8-86 derivation chain; pre-register with CMB-S4 forecast covariance.
- **Inputs**: W8-86 derivation script; W10-123 minimal axiom-set closure; CMB-S4 forecast sigma(beta_s) ~ 0.005 from Abazajian 2022+.
- **Gate**: S85-BETA-S-PREREG: PASS iff pre-registration document landed in `sessions/framework/permanent-results-registry.md` with dual-SHA, sigma forecast for CMB-S4 / CMB-HD / LiteBIRD per detector, and lockouts symmetric to W1b-7 alpha_s lockouts.
- **Effort**: 0.5 session, 1 agent (LOW).

**V.4. Zubarev L_max -> infinity analytic convergence theorem for w_0**
- **What**: Prove (or disprove) that the Zubarev regulator forces w_0 -> -1 as L_max -> infinity; combine with W1 SV2 finding (R_JE inversion at L=8 indicating Josephson-dominant regime) to determine whether the L=infinity branch is a different physical phase from L=5 anchor. Cross-validate with SDW-KMS branch (iv) regulator under CF-W4.7.
- **Inputs**: W4-46 L=5,7,9 data; W1 SV2 R_JE drift table; Zubarev regulator analytic definition; KK-tower mass-gap analysis.
- **Gate**: S85-W-0-LMAX-CONVERGENCE: PASS iff analytic proof OR numerical extrapolation band tighter than 0.05 in w_0 with explicit convergence rate; FAIL iff w_0 remains structurally divergent under both Zubarev and zeta to L_max -> infinity (would lock w_0 as permanently SCHEME-DEPENDENT for all detectors).
- **Effort**: 1.5 sessions, 1 agent (HIGH EVOI).

**V.5. Nonlinear extension of CC-5 propagation theorem (n_s exception)**
- **What**: Derive generalized composition rule for observables built via quadratic+linear maps in rho = a_4/a_2 (W3-28 identified n_s as first nonlinear/quasi-CC-5 counter-example). Predict span propagation for nonlinear composites; test on n_s span_rel = 1.7505 at L_max=5. The CC-5 multiplicative identity holds for monomial p-vectors only — n_s is the first recorded nonlinear exception.
- **Inputs**: W3-28 data; canonical n_s(rho) map; W3-21 Clause (I) anchor.
- **Gate**: S85-CC5-NONLINEAR: PASS iff derived span rule reproduces W3-28 span_rel = 1.75 within 1e-4 across {SDW, lattice-BR, zeta, Zubarev, dim-reg}; INFO iff partial match (3-of-5 regulators).
- **Effort**: 1.5 sessions, 1 agent (HIGH; new theorem candidate).

**V.6. Folded-triangle SHAPE template at 21-cm l_max = 10^5 (structural alternative to amplitude-running)**
- **What**: Compute the framework's UNIQUE substrate signature — folded-Bogoliubov bispectrum SHAPE (no scalar-field analog, ~3x enhancement over slow-roll alpha_SR = -0.046) — as a 21-cm bispectrum shape template at l_max ~ 10^5. Per W4-38 amplitude-alpha is DETECTOR-STERILE; shape-template is ZFP and SOLE surviving channel for f_NL discrimination.
- **Inputs**: W4-38 npz (folded channel -0.080); 21-cm forecasts at HERA / SKA / next-gen.
- **Gate**: S85-FOLDED-SHAPE-21CM: PASS iff shape template distinguishable from LCDM at SNR >= 2 in HERA Phase II forecast; INFO iff SNR in [1, 2].
- **Effort**: 2 sessions, 1 agent (HIGH; new computation, novel cross-correlation).

**V.7. F_amp^3PI clause-(b) FI registry landing**
- **What**: Formalize W6-69 PASS as PERMANENT theorem in registry: "Mukhanov-Sasaki z_R^2 normalization and 3PI self-energy z_R^{-2} embedded factor are inverse counterparts in A_s reconstruction; product_ratio = 1 exactly across {zeta, Zubarev, SDW, dim-reg, lattice-BR}." T4 theorem statement, derivation chain, dual-SHA per `gate-verdicts.md` permanence rule.
- **Inputs**: W6-69 script + data + W6-70 1/N_field convergence; permanent-results-registry.md schema.
- **Gate**: S85-F-AMP-3PI-REGISTRY-LANDING: PASS iff registry entry landed with dual-SHA, T4 derivation chain, and `/weave --update` confirms entry in knowledge index.
- **Effort**: 0.5 session, 1 agent (LOW).

**V.8. Mellin-balance template compliance lift to 16/16**
- **What**: Apply `.claude/templates/mellin-balance-pre-declaration.md` to all 16 enumerated S84 cluster-test gate blocks; re-dispatch W6-71 audit; lift compliance_fraction from 0.0 -> 1.0. Add "saturated-balanced / floor" subclass for zero-cluster gates (VII-K-PROP, CC5-ADJACENT, LEDGER-LINEARITY, M0-FCONV-BACK).
- **Inputs**: W6-71 template + audit script; 16-gate enumeration.
- **Gate**: S85-MELLIN-TEMPLATE-COMPLIANCE: PASS iff compliance_fraction = 1.0; re-dispatched W6-71 meta-gate PASSes.
- **Effort**: 1 session, 1 agent (MEDIUM; tedious; 16 gates x per-gate snippet derivation).

**V.9. Re-open W9b-107/108/109 (Yukawa-closure, MW-consistency, tau-cross-scale) post mu_BC obligation (i) remediation**
- **What**: Three PRE-REG-INCOMPLETE gates blocked by W9b-105 FAIL. Once V.2 (alternative cube-3 derivation) lands, re-open these three gates with the new derivation pathway pinned. If V.2 returns FAIL on all three routes, reframe these as empirical chain-checks against accommodated mu_BC = 188.185 GeV (with explicit W4-48 SCHEME-DEP flag).
- **Inputs**: W9b-105 successor verdict from V.2; W9b-107/108/109 PRE-REG-INCOMPLETE entries; canonical_constants.alpha_s_MZ_obs, m_t_pole, v_ew.
- **Gate**: S85-W9B-107/108/109-RE-OPEN: PASS iff three gates dispatched with successor pre-registration; verdicts vary by physics outcome.
- **Effort**: 1.5 sessions, 3 agents in parallel (MEDIUM).

**V.10. Borel-summability registry entry + per-tau scan cache**
- **What**: Land W10-121 PASS as permanent registry entry: "min(S_inst) = 2.42e+5 across Jensen-tau in [0.05, 0.35]; 4.7 OOM safety margin vs Borel threshold 4.34; perturbation series Borel-summable inside physical scan window." Include per-tau S_inst scan cache for downstream 1/N expansions to reference.
- **Inputs**: W10-121 script + npz + ROCm GPU eigenvalue cache.
- **Gate**: S85-BOREL-FLOOR-REGISTRY-LANDING: PASS iff entry landed with dual-SHA, per-tau cache referenced, and /weave --update confirms.
- **Effort**: 0.5 session, 1 agent (LOW).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | W2-EPOCH-GATING (3PI epoch-invariance to delta_sat = 7.52e-5) | PHONONIC | PERMANENT theorem | Bounds all 3PI transit-vs-pivot comparisons; mis-classification of small Jensen saddles as instantons structurally blocked |
| 2 | W2-HARMONIC-NOT-INSTANTON (S_harm = 0.203 < Borel 4.34) | PHONONIC | PERMANENT theorem | Small Jensen saddles are Gaussian fluctuations, NOT WKB tunneling; companion to W10-121 Borel floor |
| 3 | F_amp^3PI clause-(b) FI machine-epsilon (W6-69) | PHONONIC | PASS | A_s amplitude renormalization-regulator-independent; T4 theorem candidate for V.7 registry landing |
| 4 | 1/N_field convergence at 2,445x below eps_H (W6-70) | PHONONIC | PASS | Field-sector expansion slow-roll-bounded; perturbation series clean |
| 5 | Z_R counterterm FAIL at f_conv -> a_2 slot extension (W6-67) | GEOMETRIC | structural FAIL | Renormalization obstruction is vertical (Mellin-slot-specific), NOT perturbative; 2-loop or scheme-dependent certification needed (V.1) |
| 6 | alpha_s = n_s^2 - 1 as OZ identity, n_aux = 0 (W8-86 + W10-123) | PHONONIC | PERMANENT theorem | Single-pole OZ structure forced by minimal axioms; CMB-S4 ~33.98 sigma load-bearing detector test |
| 7 | C^2 block decoupling, Cartan-trace identity (W9b-106) | PARTICLE | PERMANENT theorem | Delta sin^2 theta_W [C^2] = 0.0 EXACT, rep-independent; mu_BC obligation (ii) discharged structurally |
| 8 | Spectral-dimension d_spec = 4.895 (W9b-105) | GEOMETRIC | FAIL | Cube-3 derivation pathway closed; mu_BC obligation (i) needs alternative routes (V.2) |
| 9 | n_T(k_CMB) two-speed substrate at -3.024e-3 (W4-39) | GEOMETRIC | PASS | c_T/c_S = 2.062 = a_2/a_0 spectral moment ratio; ZFP under W4-48 |
| 10 | w_0 permanently SCHEME-DEPENDENT (W4-46 split 6.22x) | GEOMETRIC | structural FAIL | Confirms W1 SV2 branch (iv) retraction; Zubarev L_max -> infinity convergence (V.4) is decisive forward gate |
| 11 | b_power interpolation a_4 -> a_2 -> Weyl-7 (W7b-76) | GEOMETRIC | PASS | Two-scale predicate stronger than single-scale lock; IKKT b=1 excluded analytically |
| 12 | Borel-summability floor 4.7 OOM safety (W10-121) | GEOMETRIC | PASS | Perturbation series Borel-summable; tree+1-loop computations justified without instanton corrections |
| 13 | 5-axis Fisher: alpha_s carries 98.2% of joint chi^2 (W10-124) | NON-PHONONIC | INFO | alpha_s sole 5-sigma axis at 33.98 sigma; full framework's perturbative claim rests on CMB-S4 alpha_s measurement |
| 14 | beta_s = -0.1331 running-of-running pre-reg candidate (V.3) | PHONONIC | OPEN | Third-order Taylor coefficient from OZ propagator; CMB-S4 follow-on to alpha_s |
| 15 | Cross-wave w_0 conflict: W1 SV2 (branch axis) vs W4-46 (regulator axis) | GEOMETRIC | OPEN | Both axes fail to converge at L=5; S85 re-audit must address simultaneously per V.4 |

---

*End of Feynman synthesis. Field-theoretic spine intact at the A_s amplitude level (W6-69 + W6-70 + G16 + G35); structural obstruction localized to Z_R counterterm at the f_conv -> a_2 slot extension (W6-67). Perturbative ledger immunized against false instanton interpretations (W2-HARMONIC-NOT-INSTANTON + W10-121 Borel floor). alpha_s = n_s^2 - 1 stands as the framework's strongest zero-free-parameter prediction under W10-123 PERMANENT theorem registration. The CMB-S4 ~2030 measurement of alpha_s at 33.98 sigma forecast carries 98.2% of the framework's joint discriminator weight.*
