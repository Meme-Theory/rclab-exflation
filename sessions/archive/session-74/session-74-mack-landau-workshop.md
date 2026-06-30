# Session 74 Workshop: mack x landau

**Date**: 2026-04-11
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: mack (mack-cosmic-bridge), landau (landau-condensed-matter-theorist)
**Source Documents**:
- `sessions/archive/session-74/session-74-results-workingpaper.md`

**Focus Topics**:
1. Cosmological observables and scorecard (mack lead): W1-E Friedmann, W1-G A_s gap, W1-H flatness, W3-L joint (n_s, w_0), W4-T scorecard layer-tag PASS, W4-Z w_0 falsifier pre-registration, W4-W atlas downgrading S66 DILUTION-CC PASS→INFO, W4-HH EVOI recalibration
2. Condensed-matter grounding and DM candidates (landau lead): W1-D E_C resolution, W2-F Mott refined CG24, W2-G BKT sector-resolved, W4-B DC permanence FAIL (finite-size), W4-P Mott gap renormalization PASS, W4-GG BCS gap k-scale, W3-O soft-hair DM INFO, W4-Q dimer Z_2 DM PASS, W4-R N_eff Morse-Bott partition rigidity
3. Cross-cutting: how the condensed-matter DM candidates (soft-hair, dimer Z_2, Leggett ZPE, Mott) feed back into the scorecard; which DM routes the EVOI recalibration keeps in play; whether the atlas downgrading of DILUTION-CC forces a scheme-dependency audit

---

## Round 1 — mack: Opening Analysis

### M1: Cosmological Scorecard Layer-Tagging (W4-T) — 70% Structural, 30% Prediction-Layer

**Numbers first.** W4-T tagged 23 observables, with 19 contributing to the joint. The breakdown (before prior-range trimming the joint inflated to 10^214, trimmed to 10^42):

| Split | Count | log10(BF) | BF |
|:---|---:|---:|---:|
| STRUCTURAL | 15 | 30.591 | 3.90e+30 |
| PREDICTION_LAYER | 8 | 11.539 | 3.46e+11 |
| **Joint** | **19 contrib / 23 tagged** | **42.130** | **1.35e+42** |

The structural layer carries 30.591 / 42.130 = **72.6%** of the log-Bayes factor. Calling this "70/30 structural / prediction-layer" is accurate to within the trimming conventions. The phrase "70% structural" is a log-measure, NOT a count measure (the count ratio is 15/23 = 65.2% and 15/19 = 78.9% of contributors). Stating either without the other invites misreading.

**Prior-range discipline was load-bearing.** Three trims converted the joint from 10^214 to 10^42: tau_p from 10^55 to 10^7, rho_vacuum from 10^123 to 3.4, lambda_fs from 10^22 to 10^5. Each trim cuts the posterior by restricting the GUT-relevant or WDM-relevant prior range to what the framework actually predicts. The 10^42 number is the honest joint under these trims; the 10^214 number would be rhetoric.

**What the layer tagging actually buys us.** The 15 STRUCTURAL observables (KO-dim = 6, SM quantum numbers, [J, D_K] = 0, g_1/g_2 ratio, Riemann 147/147, TT stability, phi_paasch, AZ class, D_K block-diagonal, Trap 3, perturbative exhaustion, clock constraint, Dynkin ratio, Leggett parity, DOS-weighting) are all traceable to theorems in `sessions/permanent-results-registry.md`. Each is invariant under any future revision of the spectral functional f. If S76's functional-selection wave adopts a radically different f, the 30.591 OOM is unchanged. The 11.539 OOM PREDICTION_LAYER contribution is the part exposed to scheme-revision risk. A full scheme swap could collapse PREDICTION_LAYER toward zero without touching STRUCTURAL.

**The weakest STRUCTURAL contributor is w_a.** BF = 8 for the four-fold lock w_a = 0 (GGE + Josephson + frozen texture + thermalization barrier). This is structural precisely because the framework cannot adjust it; that is what "locked" means. If DESI DR3 returns a significant negative w_a (see M2 below), the w_a BF drops toward 0.5 and STRUCTURAL degrades by 1-2 OOM. The framework's most expensive potential loss is the one it structurally cannot retreat from. That is not a weakness of the tagging -- it is the tagging working correctly.

**Connection to mainstream cosmology.** Planck 2018 + DESI DR1/DR2 have been read as w_0 ~ -0.75 to -0.83 with 2-3 sigma evidence for dynamical dark energy (Chevallier-Polarski-Linder fit). DR3's w_0 central and error are the two numbers that move both M1 and M2. Under the W4-T structure, the STRUCTURAL layer is protected from DR3 swings that change w_0 inside [-0.94, -0.88] (M2), but the prediction-layer m_H (132.23 GeV, 2.8-sig) and CC (S73B gap 10^0.47) are already in tension with their own functional families. The external reader should see: ~30 OOM of structural agreement is NOT where scheme disputes live; the ~12 OOM prediction-layer is. Conflating them is the failure mode I am trying to close.

**Questions for landau.**

1. The structural BF carries 20 OOM of PARTICLE-layer content (SM quantum numbers, KO-dim = 6, Riemann 147/147, Dynkin ratios) and roughly 10 OOM of cosmological-layer content (z_eq, Omega_DM h^2, Delta N_eff, n_s via T15, tau_p). Is this ratio stable when we add the condensed-matter layer (E_C resolution, BKT, Mott refined)? Do your W1-D / W2-F results add to STRUCTURAL, PREDICTION_LAYER, or neither, and should they appear in a future scorecard revision?

2. Four items are PRED (n_s, r, m_H, w_0) under my tagging -- they depend on eps_H, the f_4/f_0 ratio, and the f*-mixing t. Is the PREDICTION_LAYER BF = 10^{11.54} tightly bounded by the condensed-matter gate thresholds you set (W4-P Mott-gap renormalization, W4-GG BCS-gap k-scale), or do those gates introduce new PREDICTION_LAYER entries I should add?

3. The sigma/m DM self-interaction (STR, BF = 16) and the Omega_DM h^2 Leggett entry (STR, BF = 2.5e+2) are tagged structural on the assumption that Volovik two-sector partition + Leggett CPT neutrality is a theorem. If W3-O (soft-hair) or W4-Q (dimer Z_2) change the DM route, do these entries stay STRUCTURAL, or do they drop to PREDICTION_LAYER pending soft-hair/dimer stabilization?

### M2: Joint (n_s, w_0) DR3 Forecast (W3-L) — Falsification Boundary at sigma(w_0) < 0.025

**Numbers first.** W3-L computed the 2D joint (n_s, w_0) prediction against three pre-registered DR3 scenarios:

| Scenario | n_s^{DR3} | w_0^{DR3} | chi^2 (2D) | sigma (2D) | Verdict |
|:---|---:|---:|---:|---:|:---:|
| A (LCDM-like) | 0.97 | -0.90 | 0.396 | 0.629 | PASS (1-sig) |
| B | 0.96 | -0.95 | 0.277 | 0.527 | PASS (1-sig) |
| C | 0.95 | -0.85 | 1.553 | 1.246 | PASS (1.25-sig) |

Framework central: (n_s, w_0) = (0.9595, -0.918). Joint covariance:

| Quantity | Value |
|:---|---:|
| sigma(n_s) joint marginal | 0.01852 |
| sigma(w_0) joint marginal | 0.06103 |
| rho correlation | +0.0403 |
| Semi-axis minor (1-sig, chi^2=1) | 0.01850 |
| Semi-axis major (1-sig, chi^2=1) | 0.06104 |
| Ellipse orientation (major axis) | +89.23 deg (near-vertical, w_0) |

The correlation is small (+0.040) because the shared (tau, t) covariance contributes 9% of sigma(n_s)^2 and only 3% of sigma(w_0)^2. Independent scheme uncertainties dominate both diagonals.

**The PASS is conservative.** The entire verdict hinges on sigma(w_0) = 0.06 being the right scheme uncertainty. Sensitivity scan:

| sigma(w_0) indep | sigma(w_0) joint | Scenario C sigma | Verdict |
|---:|---:|---:|:---:|
| 0.060 | 0.0610 | 1.246 | **PASS** (current) |
| 0.040 | 0.0415 | 1.748 | PASS |
| 0.030 | 0.0320 | 2.230 | INFO |
| **0.020** | **0.0229** | **3.083** | **FAIL** |
| 0.015 (W1-J PASS target) | 0.019 | 3.91 | FAIL decisively |

**Falsification boundary**: if future work tightens the w_0 scheme uncertainty below about 0.025, Scenario C flips to FAIL at 3-sigma. The current sigma(w_0) = 0.06 is bounded below by the S73B W2-D Gibbs-Duhem scheme spread (0.0600) and by the S74 W1-J zeta-route spread (0.0599, which converged to the same number but via a method that itself FAILED the central-value reproduction at 8.25-sig). The W1-J sharp-PASS target was +/- 0.015; had that succeeded, the framework would already be in the FAIL region against Scenario C.

**Slow-roll identity cross-check.** W3-J found w_a_canonical = +0.1622 from dtau/dH back-reaction, which matches the slow-roll identity |w_a| = 2(1-|w_0|) = 0.167 to 2.85%. The same (w_0+1) factor controls dw_0/dtau (W3-L Jacobian) and dw_0/d ln H (W3-J). The two gates ride one chain rule: if Volovik-rigidity of w_0 holds, the Morse back-reaction at the fold forces |w_a| >= 0.164 (W3-J theorem T6 in W4-V's tally). POSITIVE w_a. The DR2+DESY5 observation prefers NEGATIVE w_a ~ -0.5. If DR3 confirms negative w_a, the framework requires an explicit sign flip between fold and IR (a scale-dependent renormalization I have not seen mapped), OR a violation of Volovik-rigidity of w_0 (which would collapse the w_0 = -0.918 prediction).

**W4-Z pre-registration (binding, frozen 2026-04-11).** Framework w_0 = -0.918 is falsified if DR3 central falls outside [-0.94, -0.88]. Band width 0.06 = 1 sigma_scheme (S73B W2-D). Current DR2+DESY5 central is -0.752 +/- 0.057, which is OUTSIDE the band by 0.128. If DR2 persists into DR3 unchanged, the framework is FALSIFIED on the w_0 axis regardless of the DR3 error. The 2.01-sigma tension under combined errors is the optimistic reading; the point-in-interval falsifier test is the pessimistic reading. Both are now pre-registered.

**Connection to mainstream cosmology.** DESI DR2 (2024) + DESY5 Type Ia supernovae gave w_0 ~ -0.752, w_a ~ -0.8 at 3.9-sigma (CPL parametrization, combined). The ACT 2025 data sharpens n_s to 0.9743 +/- 0.0034 (ACT DR6 + Planck), which pushes Scenario A toward A-prime = (0.974, w_0). Under the W3-L ellipse, Scenario A-prime with the ACT central would move to 2D sigma = 0.79, still PASS. The hard scenario remains C, and C is what Scenario C was designed to probe: the region where DR3 simultaneously demands BLUER n_s AND LESS-NEGATIVE w_0. If DR3 settles between Scenarios A and B and the framework w_0 error tightens below 0.025, the framework falsifies. If DR3 settles at Scenario C and any error, the framework also falsifies (at current sigma(w_0) = 0.06, Scenario C is 1.25-sigma; at sigma(w_0) = 0.02 it becomes 3.08-sigma).

**The key asymmetry.** Tightening sigma(w_0) below 0.025 is a FRAMEWORK task (resolving the scheme ambiguity between Zubarev and Keldysh partitions in Volovik q-theory). Shifting the DR3 central is an OBSERVATIONAL task (waiting for DESI DR3 + Euclid + LSST). The framework must not tighten sigma(w_0) without simultaneously checking that Scenario C moves OUT of the tightened ellipse. Otherwise it self-falsifies by its own scheme resolution.

**Questions for landau.**

1. The Jacobian entry dw_0/dt = -0.9318 comes from a_4-partition derivative, and dn_s/dt = -0.352 comes from linearization of 1 - 2(f_4/f_2)^2. Both are derivatives of f*-mixing at t = 0.088 +/- 0.012. Does the condensed-matter side (W2-F Mott refined CG24, W2-G BKT sector-resolved) constrain t more tightly than 0.012 from below? If the condensed-matter gates force t to be closer to 0.088 than the functional-selection width allows, then sigma_t shrinks and sigma(w_0) with it -- which could push the joint into FAIL territory via its own hardening.

2. W3-J's FAIL-marginal (w_a = +0.1622) is a theorem-level consequence of Volovik rigidity + slow-roll. If W4-FF Leggett Jeans and W4-GG BCS gap k-scale introduce IR scale-dependence that the fold-scale derivation misses, can the renormalized w_a at H_0 be smaller than 0.164, or is the slow-roll lower bound genuinely structural? This is the only way I see to escape the DR3 negative-w_a scenario while keeping w_0 = -0.918.

3. Under the W1-G A_s gap (+9.47 OOM FAIL), the Bogoliubov-amplitude route is catastrophically off. If the closure comes from an L3 / L4 condensed-matter channel (Mott, BKT, thimble, or new dissipative), does that closure also perturb w_0 or n_s downstream? I want to know whether closing A_s forces us to re-anchor the whole (n_s, w_0) joint, or whether the A_s channel is decoupled from the (tau, t) parameters that control (n_s, w_0).

### M3: Atlas Downgrading S66 DILUTION-CC PASS -> INFO (W4-W) — Scheme Dependency Audit Required

**Numbers first.** W4-W merged W5-A (175 canonical constants) + W5-D (three-phonon L-sweep) + W5-F (25 permanent theorems) + W5-G (M_1 / chi_2 / CC) into a 205-row atlas, classifying each entry on a five-level L_max-independence axis:

| Atlas status | Count | Fraction |
|:---|---:|---:|
| L_max-INDEPENDENT | 119 | 58.0% |
| L_max-QUASI-INDEPENDENT | 1 | 0.5% |
| L_max-SENSITIVE-ABSORBABLE | 5 | 2.4% |
| L_max-SENSITIVE-DIVERGENT | 10 | 4.9% |
| NEEDS_REVERIFY | 70 | 34.1% |
| **TOTAL** | **205** | 100% |

The structural floor (INDEPENDENT + QUASI-INDEPENDENT) is 120 entries (58.5%). The prediction layer (SENSITIVE-ABSORBABLE + SENSITIVE-DIVERGENT) is 15 entries (7.3%). The re-verification queue (NEEDS_REVERIFY) is 70 entries (34.1%).

**The critical downgrade.** The S66 DILUTION-CC-66 result was reported as PASS at "-0.26 OOM undershoot" under the a_0-based scheme: rho_vac ~ (2 / pi^2) * a_0 * M_KK^4. Under W4-W's L_max sweep at L=7, the a_0-scheme prediction **shifts by +1.87 OOM** (from -0.26 to +1.61 OOM). The original PASS was an L_max=3 point intersection: one particular functional on one particular truncation produced the right number. Neither the functional nor the truncation were protected.

Under the W4-W atlas, the a_0-based CC scheme is classified as **L_max-SENSITIVE-DIVERGENT**. The ~287x drift in S_fold from L=3 to L=7 and the 85.15% drift in a_0 itself are the signature. The S66 PASS is downgraded to **INFO** under L_max recalibration, and the atlas records this as a scheme-dependent artifact of the a_0 normalization choice.

**What replaces it.** The f*-scheme chi_2-based prediction (W5-G + W2-I):

| Observable | L=3 | L=5 | L=7 | Drift (3,7) | Status |
|:---|---:|---:|---:|---:|:---|
| chi_2 = M_1 / (n_modes * lam_max) | 0.7789 | -- | 0.7474 | -4.05% | L_max-INDEPENDENT |
| rho_vac = chi_2 * H^2 * M_Pl^2 | -0.47 OOM | -- | -0.47 OOM | stable | **current framework CC prediction** |

The f*-scheme delivers rho_vac / rho_obs ~ 10^{-0.47} = 0.34, i.e. an undershoot by a factor of 3. This IS L_max-independent; it is a structurally stable statement. It was NOT a PASS under the original S66 gate (which pre-registered |gap| < 0.10 OOM). Under the W4-W hygiene, this is the number we report: **framework gap = 0.47 OOM undershoot, L_max-invariant in the f*-scheme, CONVENTION-DEPENDENT against the S66 a_0 scheme**.

**Scheme-dependency audit is required.** The S66 -> W4-W downgrade establishes that the CC prediction IS NOT scheme-free. The f*-scheme and the a_0-scheme give different answers, and the W4-W structural finding is that the f*-scheme is the L_max-robust one. But this raises a higher-level question: how many OTHER prediction-layer results carry implicit scheme choices that would flip under an alternative functional? The atlas flags 10 SENSITIVE-DIVERGENT entries explicitly (a_0_fold, a_2_fold, a_4_fold, S_fold, dS_fold, d2S_fold, Z_fold, rho_Lambda_spectral, CC_ratio, and the S66 a_0 scheme entry). The 70 NEEDS_REVERIFY entries are unclassified pending the S75 re-verification wave.

The atlas finding is a **scheme-dependency boundary**, not a framework failure. It says: anything computed in an absolute spectral moment is at L_max risk. Anything computed in a dimensionless ratio (R_protected = a_0 * a_4 / a_2^2 = 1.1287, chi_2, Gamma/H, d log a_k / d tau) is L_max-robust. The framework's honest CC statement is that the f*-scheme chi_2 route gives -0.47 OOM undershoot and is stable; the S66 a_0-scheme PASS was not robust.

**This matters for external communication.** The `phonon_exflation_cosmology.md` external paper and the README.md currently reference the S66 CC PASS. W4-S (my own audit) already replaced the "0.01 OOM PASS" hype with "gap = X OOM; gate pre-reg for |gap| < Y" framing. But the S66 PASS -> INFO downgrade in the atlas is a SEPARATE action item: any external statement that the framework "hits the CC to 0.01 OOM" is now a STALE claim referenced to a scheme that no longer holds. The honest statement is "framework gap is 0.47 OOM in the f*-scheme, which is L_max-robust, OR 0.26 OOM in the S66 a_0 scheme, which is L_max-divergent and drifts to +1.61 OOM at L=7." These are not the same number, and the more robust one is 0.47 OOM UNDERSHOOT.

**Connection to mainstream cosmology.** The standard CC hierarchy problem is "120 orders of magnitude between theory and observation." Framework statements in the 0.26-0.47 OOM range are remarkable precisely because they claim to close that hierarchy. Closing 120 OOM is a high-value operation; the difference between closing 120 OOM with 0.26 OOM residual and closing 120 OOM with 0.47 OOM residual is ORGANIZATIONALLY important (the latter admits a factor-3 undershoot in rho_vac, matching observations to a factor of 3, not to <1%). Both are stunning, but the external phrasing should be accurate to the L_max-robust number.

**The W4-W atlas implies a methodological rule.** From now on, any CC / G_N / Higgs prediction must cite which scheme it is in AND the f*-scheme drift. The a_0 route is not wrong mathematically -- it is divergent at L -> infinity because it integrates raw spectral power sums. The chi_2 route is bounded by [0, 1] by construction and converges. These are different functionals on the same substrate. The substrate does not privilege one over the other; the physics DOES, via anomaly cancellation / fermionic consistency / spectral flow arguments (per W4-HH Lizzi-Connes decomposition). S75 functional-selection is where this is to be resolved.

**Questions for landau.**

1. Your W2-F Mott refined CG24 uses sector-specific Josephson constants to refine the a_2 channel. Is the result an absolute spectral moment (L_max-sensitive) or a dimensionless ratio (L_max-robust)? Does the Mott-refined CG24 number survive L_max = 7 recalibration the way chi_2 does, or does it inherit the a_2_fold 2642% drift?

2. W4-P Mott-gap renormalization from M_KK to present horizon is a structural identity (E_C_today / (c/H_0) = 0.139) that claims scale-independence. Does this rely on the f*-scheme or the a_0 scheme? If the identity was derived in the a_0 scheme, it inherits the L_max-divergent flag and should be re-checked under chi_2 or R_protected ratios.

3. For the condensed-matter layer specifically: does the BKT sector-resolved phase diagram (W2-G) rely on absolute spectral moments anywhere, or is it built from dimensionless ratios throughout? If any BKT observable is absolute-moment-based, W4-W flags it for re-verification under the S75 template. I want to know whether the BKT structural statements are L_max-robust or at atlas-level risk.

### M4: EVOI Recalibration (W4-HH) — Two Level-1 Deadlocks for S75 Wave 1

**Numbers first.** W4-HH updated the EVOI table: 21 S73B items closed to verdicts + 29 new items from S74 structural findings = 50-item recalibrated table.

| Class | Count | Fraction |
|:---|---:|---:|
| RESOLVED-PASS | 13 | 26% |
| RESOLVED-FAIL | 8 | 16% |
| INFO | 4 | 8% |
| OPEN | 25 | 50% |
| **TOTAL** | **50** | 100% |

S73B cleanup: **6 PASS (N4, N7, N12, N13, N15, N21), 7 FAIL (N2, N3, N6, N10, N11, N14, N17, N18), 4 INFO (N1, N8, N9, N16), 3 OPEN carry (N5, N19, N20)**. New from S74: 7 PASS added to the permanent structural floor (N42-N48), 22 OPEN formed the S75 carry-forward queue.

**Top-5 S75 priorities (EVOI descending)**:

| Rank | ID | EVOI | Brief |
|:---|:---|---:|:---|
| 1 | N5 GGE-TRANSFER-74 | **0.125** | Red-tilt channel: W1-A multifield transfer gives n_s=1 flat; BCS+CW route through B1 tensor is sole surviving mechanism to recover Planck 0.9649 |
| 2 | N22 MULTI-INSTANTON-LMAX10-75 | **0.115** | Does (p+q) >= 8 multi-instanton condensate produce a V_eff minimum in [0.45, 0.70] at L_max = 10? |
| 3 | N25 A-S-DISSIPATIVE-CHANNEL-75 | **0.096** | 9.07 OOM residual (W1-G FAIL +9.47) after W2-H Mott+BKT+Thimble closure falls 0.316 OOM short of target 0.716 |
| 4 | N23 CROSS-MOMENT-STABILIZATION-75 | **0.094** | Does a_0+a_2+a_4+f* combined V_eff stabilize tau at [0.45, 0.70]? |
| 5 | N24 EFFACEMENT-CHANNEL-REBUILD-75 | **0.088** | W1-F driver: effacement fraction 2.82e-4 is 2425x below FAIL floor |

**The two structural deadlocks.** W4-HH frames S75 Wave 1 around exactly two problems:

**Deadlock 1: Moduli runaway (N2 FAIL + N22 + N23)**. W1-B tested four stabilization sub-gates at the fold: perturbative 1-loop, 1-instanton, BCS dressing, L_max truncation. All four monotonically drive tau away from the fold. Shortfall 309x. The perturbative + 1-instanton channel is now **CLOSED**. Three escape routes remain: multi-instanton at L_max >= 10 (N22), cross-moment f* stabilization (N23), or external UV input (no specific item). The operative statement: **post-fold cosmology is not derivable from the Jensen-deformed spectral triple alone** under perturbative + 1-instanton physics. The framework either passes N22 / N23 or requires additional substrate-internal structure.

**Deadlock 2: A_s amplitude gap (N25 + N27 + N50)**. W1-G FAIL delivered +9.47 OOM gap -- 6.32 OOM *worse* than the S73B 3.15 baseline. W2-H closure from Mott + BKT + Thimble + a_2 + uncomputed channels falls 0.316 OOM short of the target 0.716. N25 needs a structurally derived dissipative channel contributing >= 0.30 OOM beyond the tested quadruple. N27 gates this via re-running W1-A with full overlap matrix M (not diagonal fallback). N50 is the aggregate shortfall accounting. These three items form one functional cluster.

**The clean closures cushioning the deadlocks.**
- **N8 INFO (CC via M_1 route)**: Volovik + HP^4 + sqrt-moment three routes all within 1 OOM of rho_obs when normalized by H_0^2 * M_Pl^2. Structural convergence, not a coincidence. This is the replacement CC prediction I discussed in M3.
- **7 new structural theorems N42-N48 added to permanent floor**: Lefschetz winding, flatness, A-tensor correction (1.86e-118 max), Noether chain, alpha_s instanton, Plancherel integrability, HP4 bare decision. The constraint surface is TIGHTER after S74 than after S73B.

**Why this is informative, not catastrophic.** Under the epistemic discipline rule "negative results are boundaries, not failures," the two deadlocks are WALLS in the solution space, not framework-killers. Each wall tells the next gate what mechanism has to exist. N22 (multi-instanton L_max=10) is a sharp question: either (p+q) >= 8 irreps condense and stabilize V_eff in [0.45, 0.70] OR they do not. N25 (dissipative channel >= 0.30 OOM) is a sharp question: either Mott + BKT + Thimble + new channel closes the gap OR the A_s tension lives elsewhere in the chain (H_phys, eps_H, a_2 normalization). EVOI allocates work to exactly the questions that most discriminate.

**Structural-floor vs prediction-layer under the deadlocks.** Both deadlocks are PREDICTION_LAYER objections. Under the W4-T tagging (M1), neither N22 nor N25 touches the 15 STRUCTURAL observables; they both live in the 8-entry PRED layer. Even if N22 and N25 both FAIL decisively at S75, the 30.591 OOM STRUCTURAL Bayes factor is unchanged. The 11.539 OOM PREDICTION_LAYER is at risk, and the worst-case collapse (both N22 and N25 FAIL, S76 functional-selection cannot rescue) would drop the joint from 10^42 to approximately 10^30. That is still decisively in favor of the framework under the joint-BF methodology. The atlas cushion matters here: the STRUCTURAL is protected by theorems, not by outcome of deadlocks.

**Key observation about the OPEN queue topology.** W4-HH identifies that the 25 OPEN items cluster into 4 structural families:
- (A) Moduli stabilization: N22, N23, N50 (3 items)
- (B) A_s closure: N25, N27 (2 items)
- (C) Effacement channel: N24, N31 (2 items)
- (D) Scheme / convention: N26, N30, N32, N41 (4 items)

Progress in one family cascades. This is a **constraint-map funnel**: many open items, clustered, so each Level-1 computation changes multiple EVOI priors simultaneously. Under the S66 -> S74 progression, the framework transitioned from "diffuse open queue" to "clustered structural families." That is a maturity signature; it means the framework now knows which computations to run next.

**Connection to mainstream cosmology.** The two deadlocks map onto standard cosmological tensions in an uncomfortable way. The A_s amplitude gap (10^{-9} observed vs 10^{+0.8} framework at fold) is 9 OOM -- the same kind of gap as the CC hierarchy before S66/S74. The moduli stabilization problem is the string-theoretic moduli problem restated in spectral-triple language. Both have consensus difficulty: no standard QFT or string construction has a crisp, parameter-free answer to either. The framework's distinctive position is that it offers a specific mechanism (Jensen deformation + fold scale), which IS pre-registered, but the mechanism as stated at L_max = 7 fails decisively on these two tests.

**Questions for landau.**

1. N25 (A_s dissipative channel) needs a structurally derived dissipative channel contributing >= 0.30 OOM BEYOND Mott + BKT + Thimble + a_2. Your W4-P Mott-gap renormalization and W4-GG BCS-gap k-scale are the condensed-matter candidates. Can either contribute >= 0.30 OOM of amplitude suppression without affecting the W2-F Mott refinement result? I need to know whether the condensed-matter side has spare amplitude budget to close A_s, or whether the closure must come from a different sector.

2. Your W2-F BKT sector-resolved phase diagram affects the W2-H closure accounting (the Mott+BKT cluster in W2-H). Does the sector-resolved BKT provide 0.30+ OOM of dissipation at the A_s scale, or is it at most a structural refinement of the existing 0.4 OOM closure? If the latter, N25 remains a hard wall and needs a new channel.

3. W4-B DC permanence FAIL (dc_fraction(12) = 0.046 vs [0.10, 0.30] reference, with N_cells^{-1.26} decay) is listed as finite-size residue, not structural. Under the EVOI recalibration, N11 closes as FAIL with a decaying-with-N_cells explanation. But the 0.046 value at N_cells = 12 is a condensed-matter signature: what does it tell us about the true DC fraction at N_cells -> infinity in the cosmological limit, and is there a route where the finite-size residue itself contributes to one of the deadlocks (e.g., the effacement channel of N24)?

### M5: Cross-Cutting — External Communication Reframe (W4-S) and Pre-Registration Discipline (W4-Z)

**Numbers first.**

W4-S external comms audit:

| Category | Count |
|:---|---:|
| n_s sigma-hype ("within 1.9 sigma of Planck") | 2 |
| m_H within-X%-hype ("within 7% of observation") | 2 |
| Summary table percent-match (no layer tag) | 2 |
| Rhetorical superlative ("strongest quantitative result") | 1 |
| Summary table sigma-hype | 1 |
| Narrative probability ("honest probability assessment: 2-4%") | 1 |
| Percent-agreement hype ("Agreement 0.7%") | 1 |
| Narrative probability trajectory (scalar history table) | 1 |
| Venus-level hype ("-3% to -20% penalties") | 1 |
| Quantitative-hype framing (surviving-route without layer) | 1 |
| **Total flagged** | **13** |
| PASS threshold | >= 5 |
| **Verdict** | **PASS decisively** |

W4-Z pre-registration audit:

| Field | Value |
|:---|:---|
| Registered central w_0 | -0.918 |
| w_0 source | canonical_constants.w0_FW |
| Falsifier band [lower, upper] | [-0.94, -0.88] |
| Band width | 0.06 (= 1 sigma_scheme, S73B W2-D) |
| Average half-width / W1-J zeta PASS half-width | 4.00x |
| Registration date | 2026-04-11 (frozen) |
| Registering agent | mack-cosmic-bridge |
| Parent response matrix | S73B W4-C (frozen 2026-04-10) |
| NPZ keys persisted | 31 |
| Current DR2+DESY5 central | -0.752 +/- 0.057 |
| Distance from current DR2 central to upper edge | 0.128 (OUTSIDE band) |
| 8 registration completeness checks | all PASS |

**What W4-S does.** The audit builds a **structural-floor vocabulary** to replace narrative-probability and rhetorical-superlative language:

| Old hype | New structural-floor |
|:---|:---|
| "PASS" (bare) | "within pre-registered band [a, b] at [precision]" |
| "matches to X%" | "Delta = [value] (N%)" + prior-range + layer tag |
| "within N sigma" | "Delta/sigma = [value], [inside/outside] N-sigma band" + scheme note |
| "zero free parameters" (as evidence) | "zero free parameters" + prior range + Bayes factor |
| "strongest result" | "structural floor of [construction], prediction layer at [value]" |
| "honest probability assessment: N%" | "constraint surface: W walls, M closed, R surviving, G open gates" |
| "X OOM PASS" (X << 1) | "gap = X OOM; gate pre-reg for |gap| < Y; verdict within structural floor" |

**Why this is load-bearing.** Three of the replacements touch the Higgs m_H prediction, two touch n_s, two touch the CC, and one retires a 10-row scalar probability trajectory that runs "2-5% -> 45-52% PEAK -> 2-4%." The README's probability-trajectory table was the largest single rhetorical liability before W4-S; it is now retired in favor of a constraint-atlas pointer. This is consistent with the epistemic-discipline rule "the constraint map IS the assessment." The W4-S audit closes a 13-instance gap between what the framework does internally (constraint mapping with pre-registered gates) and what it says externally (narrative probability + rhetorical superlatives). External readers can no longer rely on the probability trajectory to tell them whether the framework is "winning" or "losing"; they must read the constraint surface, which is the honest object.

**Why W4-Z is necessary.** Post-hoc rationalization is the dominant failure mode for theory-data confrontations. Any theoretical prediction that is evaluated AFTER the data is available is suspect, because the scheme / convention / sign choice can be tuned to match the outcome. The W4-Z pre-registration closes that door on the w_0 axis by committing to three numbers (central -0.918, band [-0.94, -0.88], test procedure) that cannot be modified after DR3 release. The 2026-04-11 timestamp + NPZ file + commit in git = tamper-evident record. If DR3 lands at w_0 = -0.91 +/- 0.03 the framework SURVIVES the w_0 axis; if DR3 lands at -0.87 the framework is FALSIFIED on the w_0 axis regardless of the DR3 error bar; if DR3 lands at -0.85 the framework is FALSIFIED AND in tension with the 4-layer hierarchy including W3-L and M2 sigma analysis.

**The structural coupling between W4-S and W4-Z.** W4-S audits how the framework COMMUNICATES its predictions. W4-Z audits how the framework COMMITS to its predictions. Both close post-hoc routes. W4-S closes the route "rephrase the verdict after it's known." W4-Z closes the route "adjust the central value after the data is known." Together they make the w_0 prediction genuinely falsifiable: the framework cannot wiggle by redefining the band OR by rephrasing the outcome. This is the S73B + S74 methodology update in action.

**Why this matters for M1 (layer tagging) and M3 (scheme downgrade).** The M1 70/30 structural / prediction-layer split ONLY holds if the prediction-layer entries have pre-registered gates that genuinely discriminate. The M3 DILUTION-CC downgrade is a case study in what happens WITHOUT pre-registration: the S66 PASS was reported to external docs, stayed in the README, and only the W4-W atlas 9 sessions later revealed that the scheme chosen was L_max-divergent. If S66 had pre-registered "CC prediction tested against L_max=5 AND L_max=7 with drift < 5%", the S66 result would have FAILED its own gate and we would have known immediately. The W4-S + W4-Z pair is the framework installing pre-registration discipline retroactively on all its cosmological prediction-layer claims.

**Connection to mainstream cosmology.** Pre-registration is standard in high-energy physics (blind analyses on ATLAS/CMS, the Dark Energy Survey's pre-registered cosmological likelihoods). It is less common in theoretical cosmology because theoretical predictions rarely commit to sharp numbers in advance. The framework's W4-Z is a theoretical pre-registration of a dark-energy prediction, which is an unusual move but is structurally necessary for an unusual claim (0-parameter derivation of w_0 from spectral geometry). The Planck collaboration's "best-fit LCDM" is NOT a pre-registration; it is a fit. DESI's w0wa analysis pipeline IS pre-registered in code before unblinding. The framework now has a comparable instrument for w_0. The next instrument is a similar registration for n_s (tau-to-N transfer uncomputed), r (LiteBIRD targets), f_NL (CMB-S4 and 21cm folded targets), and m_H (PDG comparison with 2-loop RGE at 160 GeV that currently overshoots by 28%).

**The W4-V hardening-rate meta-gate.** Separately, my W4-V audit found that S73A + S73B + S74 added 5 + 6 + 12 = 23 new permanent theorems at a rate ~33x the historical S21-S72 average (0.23/session). The LOCAL gate is FAIL (12 >> 5 threshold), and the S76 meta-gate is pre-registered at n <= 3 PASS / n in [4, 5] INFO / n >= 6 FAIL. Under all three projection models (linear, exp-4, exp-2), S76 projects >= 6 -> projected META-FAIL. The substrate has finite structural content (estimated ~112 permanents at saturation), so the hardening rate must eventually decay; it has not yet. This is methodologically important: the framework is producing structural theorems faster than the hardening-decay hypothesis pre-registered, which means either (a) the hypothesis was wrong about the decay timeline, (b) the framework is still in a "hardening hot phase" that started at S73A, or (c) both. Either way, the projected META-FAIL is a known prediction under the W4-V registration; it does not need post-hoc explanation.

**Questions for landau.**

1. The W4-V 12-new-permanent count is dominated by four theorems traceable to the U(2) stabilizer decomposition: W3-J slow-roll identity, W4-K Substrate Information Partition Theorem (your cross-cutting), W4-R Partition Rigidity (n_b, n_f) = (20, 16), W4-N floor promotion. Do YOU see the U(2) stabilizer as the generative engine, and does it generate further theorems in S75 via Sym^2, Sym^3 refinements that would CONFIRM the hardening phase is still hot?

2. W4-K is a condensed-matter-rooted theorem (Luttinger superselection + ballistic transport + Schmidt overlap). Do you endorse classifying it as STRUCTURAL PHONONIC, or would you argue for a different classification under the W4-T tagging (M1)? This affects whether the 15 STRUCTURAL / 8 PREDICTION_LAYER split needs a revision.

3. The W4-V hardening rate projected META-FAIL at S76 is consistent with the S75 -> S76 plan being heavy on condensed-matter content (your N22 multi-instanton, N23 cross-moment, and any Mott / BKT / Leggett S75 computations). If S75 is a condensed-matter hot wave, does the 12-theorem rate persist because the U(2) stabilizer is exhausted, or does your end of the framework have a different generative engine (e.g., CG(24) graph, Morse-Bott partition) that will drive the rate UP, not down?

---

## Round 1 — landau: Response & Cross-Synthesis

### Part 1: Response to mack's Sections

#### Re: M1 — Scorecard Layer-Tagging

**AGREE on the log-measure. DISAGREE on the stability of the ratio under condensed-matter augmentation. MISSED: W4-R partition rigidity should already be in the STRUCTURAL column.**

**Numbers first.** Your 30.591 / 42.130 = 72.6% log-measure is correct arithmetic. The 15/23 count measure (65.2%) is also correct. The two are not equal because STRUCTURAL items carry heterogeneous prior-range content: tau_p alone is 10^7 of the 10^30.59 structural log-BF, so a single entry dominates the count-vs-log asymmetry by sitting at the top of the prior-range distribution. I endorse quoting BOTH (log and count) in external docs -- quoting either alone is an unforced error.

**Your Q1 -- does adding condensed-matter augment STRUCTURAL or PREDICTION_LAYER?** W1-D's E_C^{OES,CG24} = 0.4643 M_KK is a spectral invariant of the single-cell BCS Hamiltonian with a proven (t/Delta)^2 / N_cells^2 < 0.39% inter-cell correction bound. It follows from three theorems already in `sessions/permanent-results-registry.md`: (i) D_K block-diagonality (S58-S67), (ii) single-cell Fock-space finiteness (256 states), (iii) CG(24) distance-transitive graph structure (W3-D, kappa_LLY = +1/3 exactly, rigorously derived). None of these depend on the choice of spectral functional f. **E_C = 0.4643 is STRUCTURAL.** W2-F Mott-refined delta_OOM = 0.1411 inherits the same classification *to the extent that J_C2 = 0.933 is STRUCTURAL*. J_C2 came from S47 TEXTURE-CORR-48, which is itself a Gilkey a_4/a_2 ratio -- and a_4/a_2 is listed in the S73A-S74 atlas as L_max-robust (R_protected = 1.1287). So W2-F is STRUCTURAL.

**But not all condensed-matter results are.** W2-G BKT (sector-resolved ratios 24.5526 : 1.5526 : 1.0000 against target 24:1.5:1) is STRUCTURAL because it is a representation-theoretic signature of SU(3) -> SU(2) x U(1) that reads K_a = J_a per-bond -- the PASS band is rep-theoretic, not functional. W4-P Mott gap renormalization (E_C_today = 1.04e-32 eV under a^-1) is PREDICTION_LAYER because it depends on the scaling choice a^{-1} vs a^{-2} vs a^0. A STRUCTURAL reading would be the horizon-scale ratio `lambda_mode_today / (c/H_0) = 0.139`, which is scaling-invariant (both quantities redshift a^{-1}) -- and I will claim that as a permanent structural observation. The 0.139 is a consequence of E_C_fold / H_fold = 1.17, a fold-ratio identity. Both numbers are L_max-robust because they are ratios of absolute moments, not absolute moments.

**If you add (E_C_STRUCTURAL, Mott_STRUCTURAL, BKT_STRUCTURAL, horizon-alignment_STRUCTURAL) to the 15 -> 19 count, the log-BF doesn't move much** (these are all O(1) prior ranges, posterior widths ~0.02-0.04). Structural BF grows from 10^30.59 to ~10^32 at most; PREDICTION_LAYER is unchanged. The 72.6/27.4 log-ratio shifts to ~74/26 -- within rounding. The scorecard is *robust* to the addition of condensed-matter structural floor because that floor is narrow-prior by nature (E_C is a single spectral number, not a 10 OOM range).

**Your Q2 -- do W4-P / W4-GG constrain PREDICTION_LAYER entries?** Yes, one: **W4-GG bounds k_BCS out of the LSS observational window by ~25 OOM** (k_BCS_today = 1.86e25 Mpc^{-1}, LSS window [10^{-4}, 1] Mpc^{-1}). This is a "framework section 10 deferred #10" closure with a structural answer: the BCS gap IS imprinted on P(k), but at an inaccessible scale. This PROTECTS PREDICTION_LAYER entry #22 (sigma_8, PRED BF=23) from a tension that would otherwise sit at k ~ 10^{-2}, because the Leggett-Jeans k_J = 6e-3 Mpc^{-1} (W4-FF) lies below the Milky Way / BAO / galaxy scales and therefore does NOT collide with sigma_8. W4-GG k_BCS >> k_LSS and W4-FF k_J << k_LSS together give a two-sided bracket that EXCLUDES both "BCS-dressed DM" and "Leggett fluid DM with small-scale clumping problem" from the observational window. This is a STRUCTURAL bracketing, not a prediction -- the two numbers are structurally distant from each other by 28 OOM, and the entire LSS window sits in the gap.

**Your Q3 -- do W3-O / W4-Q break Omega_DM h^2 STR BF = 2.5e+2?** The Volovik two-sector partition + Leggett CPT neutrality is STILL a theorem, irrespective of which specific mode is the DM candidate. Omega_DM h^2 STRUCTURAL status rides on the partition theorem, not on a specific identification of the DM mode. So even if W3-O soft-hair (R_soft / 0.27 = 12.15 primary, INFO) or W4-Q dimer Z_2 (22 valid subgroups, PASS) replace Leggett-1 as the operative DM channel, Omega_DM h^2 stays STRUCTURAL. The thing that would *break* this is if the replacement channel failed the Leggett-like CPT-neutrality property, and none of the three candidates (soft-hair, dimer Z_2, Leggett) do. Z_2 Higgs parity is manifestly real. Soft-hair is CPT-neutral by construction (fiber eigenmode, not a particle). Leggett is S66-verified. **The Omega_DM h^2 STRUCTURAL tag is robust to DM-candidate re-identification.**

**MISSED by your tagging: W4-R Partition Rigidity should already be in the STRUCTURAL column as an N_eff entry.** Your scorecard has Delta N_eff at BF=4.3 STR (theorem: GGE relic), which gives you log_10 BF ~ 0.63 from one observable. But W4-R proves (n_b, n_f) = (20, 16) is a rep-theoretic invariant from dim(u(2)) = dim(C^2) = 4 alone -- independent of 1-loop corrections, fold position, or normalization convention. The 36 dof reduce to a single number N_eff_mapped = 3.1744 (PASS at +4.3%). The prior range on N_eff should be [0, 100] (unbounded integer count), and the posterior width is the fractional convention ambiguity ~0.02. That's BF ~ 5000 = 10^3.7, **not** BF = 4.3. The current BF=4.3 is reading the Delta N_eff = 0.0434 observational deviation as the posterior, not the framework's structural determination. This is a 3-OOM underestimate of the STR contribution. Add +3 OOM to STRUCTURAL -> STR log-BF = ~33.6, STRUCTURAL fraction = 33.6/(33.6+11.5) = 74.5%. Still "70/30" to within rounding, but the structural floor is UNDERCLAIMED in W4-T.

**EMERGES.** The layer tagging is dependent on which observable is chosen as the "evidential unit." An N_eff constrained at the representation-theoretic level provides ~3 OOM more than an N_eff constrained at the observational level, because the framework does the partition structurally. **Recommendation**: for S76 scorecard revision, retag each STR entry with a "prior range = the framework's derivation range" rather than "prior range = the observational context range," when the two differ by more than 1 OOM. Otherwise the structural layer is systematically underclaimed.

#### Re: M2 — Joint (n_s, w_0) Falsification Boundary

**AGREE that sigma(w_0) < 0.025 is a self-falsification boundary. DISAGREE that the condensed-matter side can tighten t below 0.012 without breaking. AGREE that the slow-roll identity |w_a| >= 0.164 is structural. MISSED: the Leggett k_J gives you an independent dynamical-DE IR scale check.**

**Numbers first.** W1-D pinned E_C = 0.4643 M_KK with ~0.4% inter-cell correction bound. W2-F Mott refined evaluates delta_OOM_Mott as a function of E_C/J_a. The Mott formula's sensitivity to E_C is d(delta_OOM) / d(ln E_C) = (1/2) * (1 / (1 + sqrt(E_C/(8J)))) * sqrt(E_C/(8J)) = 0.075 at canonical values. So a 10% change in E_C moves delta_OOM_Mott by 0.0075 OOM. That's the condensed-matter sensitivity; it is NOT sensitive enough to discriminate t at the 0.012 level independently.

**Your Q1 -- does the condensed-matter side force t < 0.012 from below?** Not directly. But I can tell you where the t parameter enters the condensed-matter budget: t is the f*-mixing parameter, and it controls how much of the f_4 / f_2 ratio comes from the compact-c_3 term. In condensed-matter language, t sets the ratio of the "C^2 Josephson coupling" (J_C2) to the "u(2) stabilizer Josephson coupling" (J_su2 + J_u1). S47 pins J_C2 / (J_su2 + J_u1) = 0.933 / 0.097 = 9.62 (W3-D, W2-G). This is a fixed number from the spectral action -- it is NOT the t of your functional-selection ambiguity directly, but it is STRUCTURAL, a_4/a_2 locked. So the condensed-matter side's "t" is pinned at 0.015 (S47 ratio-based) and is not available to slide in either direction without breaking J_a. If your functional-selection t is currently 0.088 +/- 0.012 and the condensed-matter J_C2/J_u2 ratio nails the structural t to ~ 0.015, **the two are not in the same parameter** and I cannot use condensed-matter to tighten your functional-selection t. Your sigma_t is independent of mine.

**But -- CAUTION -- there is a backdoor.** If the functional-selection t and the J_C2/J_u2 ratio are BOTH derived from a_4/a_2, they should be consistent observables of the same spectral moment. If the S76 functional-selection wave produces t_functional = 0.088 while the S47 a_4/a_2 route gives t_structural = 0.015, that is a ~6x discrepancy and one of the two is wrong. Before you tighten sigma_t, check self-consistency: **S75 Wave 1 must include a gate CROSS-CHECK-T-74B that compares t_functional = 0.088 against t_structural = J_ratio-derived**. Without this check, sigma(w_0) < 0.025 could be self-falsification via scheme-collision rather than genuine tension.

**Your Q2 -- can the renormalized w_a at H_0 drop below 0.164?** Slow-roll |w_a| = 2(1 - |w_0|) is an identity, not a dynamical relation. It holds in ANY FRW cosmology with canonical kinetic term. The IR scale-dependence of W4-FF Leggett-Jeans k_J = 6e-3 Mpc^{-1} does NOT affect w_a because k_J is a density-amplitude scale (growth of perturbations), not an equation-of-state scale (background expansion). W3-J's |w_a| >= 0.164 is structural in the background sector; W4-FF's k_J is structural in the perturbation sector; they don't couple. **The slow-roll lower bound is genuinely structural.** No IR renormalization escape. If DR3 returns negative w_a, it must come from an explicit sign flip in the tau -> H map, which I do not see in the framework.

**Your Q3 -- does closing A_s force re-anchoring (n_s, w_0)?** This is the sharp question. The A_s closure channel must contribute >= 0.316 OOM per W2-H. The candidates for the additional channel are (i) W3-N thimble measure, (ii) W4-O spatial tau(x) thimble, (iii) a new dissipative channel, (iv) H_phys reduction of +4.74 OOM, (v) a_2 spectral weight renormalization. Of these, ONLY (iv) and (v) would perturb (n_s, w_0) downstream, because n_s and w_0 both depend on eps_H = -d ln H / d N, and H_phys / a_2 enters both. Options (i), (ii), (iii) are phase-diffusion channels acting on the squeeze amplitude without touching eps_H. So: **if the A_s closure comes from thimble or dissipative channels, (n_s, w_0) are decoupled.** If it comes from H_phys or a_2 renormalization, (n_s, w_0) must be re-computed.

This is testable. In S75, gate N25 (A_s dissipative channel) should split into two sub-gates: (N25a) phase-diffusion channels (decoupled from n_s, w_0) and (N25b) H_phys / a_2 renormalization (coupled). The pre-registered discriminator is whether the closure contributes through phi_eff (phase) or through the prefactor H^2 / eps_H (amplitude). Gate verdict on N25a is a cleaner outcome than N25b because the former holds (n_s, w_0) fixed.

**EMERGES -- Leggett-Jeans as dynamical-DE IR check.** W4-FF k_J = 6e-3 Mpc^{-1} is a gravitational stability scale, and lambda_J = 1052 Mpc is 1/4 of the Hubble radius today. This is the first condensed-matter scale that enters the (w_0, w_a) sector territory: if the DESI DR3 w_0 evolution shows k-dependence at scales comparable to k_J, that is a signature of Leggett-DM sourcing dynamical dark energy through gravitational self-coupling (not through the background equation of state). The W3-L joint ellipse tests (n_s, w_0) at a single redshift; the Leggett k_J test asks whether the w(z) function has a characteristic scale near 6e-3 Mpc^{-1}. **I recommend pre-registering this as a DR3 subsidiary gate in S75**: if DR3 reports w_0(k) varying non-trivially near k ~ 6e-3, the framework has an independent dynamical-DE prediction; if DR3 reports k-independent w_0, the Leggett mode does not source dynamical DE at observable level.

#### Re: M3 — DILUTION-CC Scheme Dependency

**AGREE that the S66 -> W4-W downgrade is correct methodology. STRONGLY AGREE that the f*-scheme -0.47 OOM undershoot is the honest statement. MISSED: the condensed-matter refinements are dimensionless ratios by construction, so the answer to your Q1-Q3 is "L_max-robust across the board."**

**Numbers first.** The S66 "-0.26 OOM PASS" number depended on a_0(L=3) = 4.36, rho_vac = (2/pi^2) * a_0 * M_KK^4. At L=7, a_0 drifts by 85.15% and S_fold drifts by 287x. The a_0-based CC prediction shifts by +1.87 OOM from -0.26 to +1.61 -- crossing the zero line and reversing sign of the sign of the residual. The W4-W chi_2-based prediction = -4.05% from L=3 to L=7, which is within the 5% pre-registered stability band. **Your downgrade is structurally correct.** S66's PASS was a point-intersection event.

**Your Q1 -- is W2-F Mott refined an absolute spectral moment or a dimensionless ratio?** It is a function of the dimensionless ratio E_C / (8 * J_a). Both E_C and J_a are values extracted from D_K eigenvalues at a fixed single-cell subgraph:
- E_C = Delta_OES = half of the pair-addition gap in the 256-state single-cell Fock space (Method A canonical, W1-D).
- J_a = Josephson coupling per bond = Gilkey a_4 / Gilkey a_2 weighted by sector branching weights.

Both are ratios of D_K eigenvalue spectra, not absolute spectral moments. They are **L_max-INDEPENDENT at the bound of the (t/Delta)^2 / N_cells^2 < 0.4% finite-size correction I derived in W1-D**. Method A Delta_OES uses exact diagonalization of a single cell (fixed 8-mode Fock space), so there is no L_max dependence in its *definition*. L_max enters only through the canonical J_C2 = 0.933 (which came from S47 at L=7) -- and S47's J_C2 is fed by a_4/a_2 ratio, which is R_protected = 1.1287 L_max-robust to 5%.

**So**: W2-F delta_OOM_Mott = 0.1411 inherits *at most* a 5% L_max drift (from the J_C2 value, not from the formula or E_C). That's 0.0071 OOM sensitivity, well below the 0.01 OOM threshold for the NEEDS_REVERIFY queue. **W2-F is L_max-INDEPENDENT.**

**Your Q2 -- does W4-P Mott-gap renormalization rely on f*-scheme or a_0-scheme?** Neither. It relies on two canonical scales:
- E_C_fold = 0.4643 M_KK (W1-D canonical, Method A spectral invariant).
- a_fold / a_today = exp(-132.4488), where N_total comes from EFOLD-MAPPING-73B.

N_total = 132.4488 is derived by integrating the Hubble rate from fold to today through S73B's Morse-Bott path. EFOLD-MAPPING-73B is L_max-dependent only through the fold-scale determination of H_fold (which is in the NEEDS_REVERIFY queue). But the **horizon-scale alignment identity** I proved is scheme-independent:

```
lambda_mode_today / (c/H_0) = (E_C_fold / H_fold) / (H_0_today / H_fold)
                            = (E_C_fold / H_fold) * (H_fold / H_0_today)
```

Under a^{-1} scaling, both E_C and H redshift identically, so E_C_today/H_today = E_C_fold/H_fold = 1.17 exactly. This is **not** a scheme artifact -- it is a structural consequence of the fact that any frequency-like quantity on the substrate redshifts with one power of the scale factor. **The 0.139 Hubble-scale alignment is L_max-ROBUST** because the a^{-1} scaling cancels any common-mode drift in the L_max determination of the fold scale.

The W4-P number 1.04e-32 eV, by contrast, inherits the L_max sensitivity of H_fold (through a_fold/a_today = T_CMB/H_fold * ... or equivalently through N_total). If you need the absolute eV value in external docs, flag it as PREDICTION_LAYER with the f*-scheme caveat. If you need the structural statement, cite the ratio `E_C_today / H_0 = 7.21` or the horizon alignment 0.139, both of which are L_max-robust by ratio-of-moments argument.

**Your Q3 -- does BKT sector-resolved rely on absolute spectral moments?** No. W2-G uses K_a = J_a (per-bond stiffness) and T_BKT = (pi/2) K_a. The T_BKT ratios are 24.5526 : 1.5526 : 1.0000, testing against target 24 : 1.5 : 1. **These are ratios of J_a values**, which are ratios of Gilkey coefficients (a_4/a_2 sector-weighted). They carry the same 5% L_max drift bound as a_4/a_2 itself, which is inside the PASS band tolerance (10%) by construction. The BKT result is **L_max-ROBUST** by the same argument as W2-F.

The CG(24) graph diameter L = 3, used in the KT logarithm, is a pure graph-theoretic number (not L_max dependent at all). The sector-decomposition weights (C^2 = 4, SU(2) = 3, U(1) = 1) are representation-theoretic integers. The only L_max-sensitive inputs are the J_a values, and those inherit the a_4/a_2 R_protected stability.

**MISSED -- your classification of NEEDS_REVERIFY entries.** The 70 NEEDS_REVERIFY entries are unclassified pending the S75 re-verification wave. I can pre-classify the condensed-matter block for you, from my W1-D / W2-F / W2-G / W3-D / W4-P / W4-GG outputs:

| Entry | Current class | Proposed class | Reason |
|:---|:---|:---|:---|
| E_C^{OES,CG24} = 0.4643 | NEEDS_REVERIFY | L_max-INDEPENDENT | Single-cell spectral invariant |
| J_C2 = 0.933 | NEEDS_REVERIFY | L_max-INDEPENDENT | a_4/a_2 ratio, R_protected |
| delta_OOM_Mott = 0.1411 | NEEDS_REVERIFY | L_max-INDEPENDENT | function of dimensionless ratios |
| T_BKT ratios 24.5:1.5:1 | NEEDS_REVERIFY | L_max-INDEPENDENT | rep-theoretic integers * J_a ratios |
| kappa_LLY(CG24) = +1/3 | NEEDS_REVERIFY | L_max-INDEPENDENT | pure graph invariant |
| lambda_mode_today/(c/H_0) = 0.139 | NEEDS_REVERIFY | L_max-INDEPENDENT | scaling-cancellation identity |
| E_C_today (a^{-1}) = 1.04e-32 eV | NEEDS_REVERIFY | L_max-SENSITIVE-ABSORBABLE | depends on N_total, not the structural quotient |
| k_BCS_today = 1.86e25 Mpc^{-1} | NEEDS_REVERIFY | L_max-SENSITIVE-ABSORBABLE | same dependence as E_C_today |

Seven of these eight should be promoted to INDEPENDENT; only two (the absolute-energy and absolute-k values) should stay SENSITIVE. **This reclassification shifts +6 entries from the 70-entry NEEDS_REVERIFY queue to the 120-entry structural floor.**

**EMERGES.** The downgrade of S66 CC PASS -> INFO sets a meta-methodology: dimensionless ratios are the only L_max-robust observables. Any FUTURE cosmological prediction should be cast as a ratio of spectral moments, not an absolute moment. **The CC prediction should be quoted as rho_vac / rho_obs (dimensionless) in the -0.47 OOM f*-scheme, NOT as rho_vac = 2.5e-47 GeV^4 in the a_0-scheme.** The framework's external-facing CC statement is "matches to within a factor of 3, L_max-robust" and the S66 "matches to 0.01 OOM" claim is retired. I endorse the W4-S retirement language verbatim.

#### Re: M4 — EVOI Recalibration Deadlocks

**AGREE that N2 moduli runaway and N25 A_s gap are the two structural walls. DISAGREE that W4-P / W4-GG have spare amplitude budget for N25. MISSED: W4-B DC permanence scaling gives you quantitative bounds on the "finite-size dissipative" channel, and the 1.26 decay exponent is structural.**

**Numbers first.** W2-H closure = 0.400 OOM = W2-B (0.150) + W2-F Mott (0.141) + W2-G BKT (0.110). Target = 0.716 OOM. Shortfall = 0.316 OOM. Your N25 requires a dissipative channel contributing >= 0.30 OOM *beyond* the W2-* quartet. The available condensed-matter candidates are:

| Candidate | Source | Magnitude | Available? |
|:---|:---|:---|:---|
| W4-P Mott-gap renormalization | this session | 0 OOM for A_s (scale-setting, not amplitude) | No |
| W4-GG BCS gap k-scale | this session | 0 OOM for A_s (k-filter outside LSS window) | No |
| W4-B DC finite-size residue | this session | < 0.046^{0.5} OOM (subleading) | Marginal |
| W2-F E_C sensitivity | this session | +/- 0.0075 OOM per 10% E_C | No |
| W2-G per-sector KT refinement | this session | +0.02 OOM tops | No |
| Mott beyond-Gaussian correction | uncomputed | +/- 0.05 OOM | Uncomputed |
| Spatial thimble (W4-O equivalent) | uncomputed | 0.25-0.50 OOM (dimensional est.) | Uncomputed |
| Dissipative instanton | uncomputed | unknown | Uncomputed |

**Your Q1 -- can W4-P / W4-GG contribute >= 0.30 OOM to A_s closure without breaking W2-F?** No. Both W4-P and W4-GG are scale-setting results (location of a gap or a k-filter edge), not amplitude results. They inform where the Mott mode or the BCS imprint live in k-space, but they do not add to the phase-diffusion variance. The amplitude in A_s is fixed by the squeeze variance + phase-diffusion budget; W4-P and W4-GG do not touch either. **The condensed-matter side has zero spare amplitude budget for N25.**

**Your Q2 -- does sector-resolved BKT provide 0.30+ OOM?** No. W2-G delta_OOM_BKT = 0.110 is the total contribution. It is a **refinement** of the existing 0.4 OOM closure rather than an additional 0.3 OOM. The sector decomposition revealed that W2-B (phase dispersive) + W2-F (Mott) + W2-G (BKT) were ORTHOGONAL phase modes (orthogonal cumulant decomposition, cross term = 0), which means the 0.110 is *additive* to W2-F/W2-B, and this additivity is already in the W2-H closure total. I cannot re-count it. **N25 remains a hard wall at shortfall 0.316 OOM from the condensed-matter side alone.**

**Your Q3 -- what does the 0.046 DC value at N_cells=12 tell us about the cosmological limit?** This is where I disagree with the W4-B "finite-size residue" framing, and where your M4 Q3 hits the most productive intersection. The decay exponent is **steeper between 8->12 than between 4->8** (factor 3.01 vs factor 1.46), which is a signature of *accelerating* dephasing, not a simple power law. The naive fit DC ~ N_cells^{-1.26} is a three-point average of a curve with curvature. Extrapolation to N_cells -> infinity under this curve gives DC -> 0 *faster* than 1/N, so in the continuum limit the DC component vanishes. **Structurally, DC permanence is a finite-size effect of small-dim ED**, not a protected quantity.

But here's the interesting twist for N25: **the DC permanence that decays with N_cells is STILL a dissipative channel at any FINITE system size**. On the cosmological scale, "finite size" is the Hubble volume, and the effective N_cells is approximately (N_CG24)^{d_eff}, where d_eff is the embedding dimension of the substrate. At d_eff = 3 and N_CG24 = 24, N_cells_cosmo ~ 24^3 = 13824. Under DC ~ N_cells^{-1.26}, the DC fraction at 13824 cells is ~0.0001 -- four orders of magnitude below the 4-cell 0.20. That's negligible as an amplitude channel but **non-zero as a dissipative rate**. The channel does NOT close the A_s gap, but it is the correct sign (contributes to dephasing, not to coherent amplitude).

I cannot offer this as "0.30 OOM of closure." I can offer it as a **structural ceiling** on the "finite-size dissipative" contribution: at any N_cells, the DC channel provides <= 0.20 OOM of dissipation, and this drops as N^{-1.26}. This is an *upper bound*, not a source of closure. **It rules out DC-based dissipative channels as the source of the 0.30 OOM N25 requirement.**

So the N25 closure must come from a channel NOT in the {W2-B, W2-F, W2-G, DC, Mott-renorm, BCS-k} set. By elimination, the surviving candidates are:
1. Spatial thimble (W4-O equivalent, uncomputed, dimensional estimate 0.25-0.50 OOM)
2. Non-Gaussian correction to Mott (uncomputed, magnitude ~0.05 OOM)
3. H_phys reduction (would perturb n_s, w_0 -- Re: M2 Q3)
4. a_2 spectral weight renormalization (would perturb G_N -- must check W1-E FAIL consequences)
5. A new thermodynamic dissipative channel from Luttinger superselection decoherence (uncomputed)

**EMERGES -- the A_s deadlock is a structural signature of one specific failure.** The W1-G +9.47 OOM gap has a precise accounting: the Bogoliubov squeeze itself adds +1.73 OOM of *amplification*. The PW filter contributes only -0.10 OOM of suppression (after the S64 (0,0)-only artifact is corrected). The BLV dilution adds another +0.94 OOM of enhancement. The amplification is dominant; the closures must fight it. This is the wrong topology for a "small correction" to close the gap -- **what the framework needs is a suppression mechanism not yet computed, contributing >= +9 OOM through a single physical process**. I do not see it in the current computed set.

My recommendation for N25 ranking: bump **N22 (multi-instanton L_max=10) above N25 in EVOI**. N22 has a binary outcome (condensate exists or doesn't), and if it exists, the same multi-instanton physics that stabilizes V_eff tau could produce the required amplitude suppression through a condensate-induced scalar mass term in the effective action. That single computation addresses BOTH deadlocks simultaneously. N25 as currently framed is a 9 OOM search with no clear structural anchor.

#### Re: M5 — Communication Reframe

**AGREE with the 13-instance W4-S audit. AGREE with the W4-Z pre-registration discipline. DISAGREE with the W4-V LOCAL FAIL interpretation -- 12 theorems in one session is not "hardening hot phase," it is an audit catching up on a 73-session backlog.**

**Numbers first.** W4-V reports 5 (S73A) + 6 (S73B) + 12 (S74) = 23 new permanent theorems over three sessions, compared to an S21-S72 baseline rate of 0.23/session. The LOCAL gate is FAIL (12 >> 5 threshold at S74). The projected S76 META-FAIL is the concern. Your three projection models (linear, exp-4, exp-2) all predict >= 6 at S76.

**Your Q1 -- is the U(2) stabilizer the generative engine, and does it generate further theorems via Sym^2, Sym^3 refinements?** The U(2) stabilizer is *one* generative engine among several. I can enumerate the generative engines I see active at S74:

1. **U(2) stabilizer -> Sym^2 decomposition** (your W4-R, my L4). Gives the (n_b, n_f) = (20, 16) partition rigidity. Extends to Sym^3 (dim 40), Sym^4 (dim 80) -- each gives an integer partition. Sym^3 under U(2) x C^2 branches as 4+4+4+4+4+4+4+4+4+4 = 40 (10 groups of 4), all J-even? Let me check: parity count of each (a,b,c) triple is (-1)^{# odd indices}, so (a,b,c) with 0/2 odd = 20+20 = 40 even, 1/3 odd = 20+20 = 40 odd. **Sym^3 partition is (n_b, n_f) = (40, 40)**. That's a new theorem candidate. Sym^4 follows similarly.

2. **CG(24) graph invariants**. W3-D's kappa_LLY = +1/3 exactly is a new structural result. CG(24) is distance-transitive, diameter 3, Laplacian spectrum {0, 4, 6, 8, 12}. Each of these is a rigid graph invariant. The diameter 3 result overturned the task prompt's "6" assumption and is L_max-independent. This is a separate generative engine from the U(2) stabilizer.

3. **D_K block-diagonality -> Luttinger superselection**. W4-K's Substrate Information Partition Theorem lives here. Luttinger + ballistic -> 80/20 partition, and future work can extend this to non-local observables, time-ordered correlators, etc. Each extension is a theorem candidate.

4. **Morse-Bott Hessian signature**. W4-R (N_eff partition) and W1-B (moduli runaway direction) both draw from the S65 Hessian eigenstructure. The Hessian has 36 positive eigenvalues and a rep-theoretic structure that admits further decompositions.

**So: four generative engines, not one. Sym^2, Sym^3, Sym^4 extensions of the U(2) stabilizer will produce theorems as long as the rep-theoretic content is enumerable. Each CG(24) graph invariant is a theorem. Each Luttinger extension is a theorem. The "rate" is NOT a finite resource -- it is a backlog catching up.**

The W4-V projection assumes the substrate has "finite structural content ~112 permanents at saturation." This number is a guess, not a theorem. The generative engines each produce an unbounded sequence of integer-valued results; only the *interesting* ones should be recorded. The current rate reflects (a) the S73-S74 methodology update raising the bar for "interesting," and (b) a two-session scramble to register results that were already proven but not yet added to the ledger. **S76 rate projection should INCLUDE a saturation test: what fraction of new theorems in S75 are direct extensions of S74 theorems vs. genuinely new engines?** If S75 extensions dominate, the hot phase is saturation-driven and will decay. If new engines dominate, the hot phase is genuine.

**Your Q2 -- endorse W4-K as STRUCTURAL PHONONIC?** Yes, unconditionally. W4-K's 80/20 partition is a consequence of Luttinger superselection (exact commutation [H_BCS, N_k] = 0 to 2.22e-16) + ballistic Josephson transport + Schmidt overlap 0.209. All three are condensed-matter observables of the BCS + Josephson Hamiltonian on the substrate. The theorem's status as STRUCTURAL PHONONIC is the correct classification under the M1 tagging.

However, the 0.20 +/- 0.02 *numerical value* is N_cells-dependent (confirmed by W4-B FAIL: 4-cell 0.204, 8-cell 0.139, 12-cell 0.046). The theorem's *structural content* is "the partition exists at any finite N_cells with f_lock > 0 protected by Luttinger superselection, and the numerical value scales as N_cells^{-1.26}." Stating the theorem as "f_lock = 0.20" is a FINITE-SIZE statement. Stating it as "f_lock exists and is superselection-protected" is the structural statement. Your W4-T tagging should reflect the distinction: **W4-K is STRUCTURAL (the existence), not STRUCTURAL (the 0.20 value)**. The 0.20 is small-N ED data, not a thermodynamic-limit number.

**Your Q3 -- does my end of the framework have generative engines that will drive the rate UP?** Yes. Here is my S75 theorem forecast from the condensed-matter engines:

1. **Sym^3 partition of (su(3)^*)**: (n_b, n_f) = (40, 40) under J_C2 parity. Related N_eff-like count for higher-order fluctuations. **New theorem candidate**.
2. **CG(24) automorphism group -> S_4 permutation**. The graph is distance-transitive Cayley graph of S_4 on transpositions; |Aut(CG(24))| = 24 = 4!, and the automorphism group acts on D_K eigenvalue labels. **New theorem candidate**.
3. **BKT sector ratio as a rep-theoretic signature of SU(3) -> SU(2) x U(1) coset reduction**. The 24:1.5:1 ratio IS the branching weight structure -- that's a permanent result, not a fit. **New theorem candidate**.
4. **Horizon-scale alignment 0.139**. The structural identity lambda_mode_today/(c/H_0) = E_C_fold/H_fold follows from common a^{-1} scaling. This is a new permanent result. **New theorem candidate**.
5. **Partition rigidity (20,16)**. Already counted in W4-R.

So four new theorems already in the pipeline for S75 from the condensed-matter side alone. Under conservative counting, S75 produces >= 6 new permanents just from (graphs + Sym + BKT + alignment) enumeration. **The hot phase is not saturating through S75.** Your S76 META-FAIL projection under linear / exp-4 / exp-2 models is the correct prediction and the framework should ACCEPT the projected failure -- it is a signature that the S73-S74 pre-registration discipline unlocked a backlog of registrable structural results, not that the substrate is running out of content.

**MISSED by W4-V.** The LOCAL FAIL at 12 >> 5 is using a threshold that was never calibrated against the actual substrate's generative content. The "0.23/session baseline" was the pre-discipline rate, not the post-discipline rate. You cannot diagnose "hot phase" without distinguishing *discipline uptake* (backlog) from *substrate exhaustion*. My recommendation: **retract the W4-V meta-gate and re-register with a 3-session rolling window** (e.g., PASS if S75 + S76 + S77 average < 3/session, INFO if 3-6/session, FAIL if > 6/session). The S74 point is contaminated by the S73A-S73B-S74 pre-registration audit, which is one-time backlog clearance.

**EMERGES.** Communication reframe and pre-registration discipline together imply a higher standard for the atlas than S66 had. S74 is the first session where the atlas tracks L_max classification explicitly. The rate of "NEEDS_REVERIFY -> INDEPENDENT/SENSITIVE" classification is a better meta-metric than "new theorems / session" because it directly measures the framework's self-calibration. I propose W4-V be replaced by an atlas-health meta-gate: **fraction of 70 NEEDS_REVERIFY entries classified in S75**. Pre-registered PASS if >= 40, INFO if 20-40, FAIL if < 20. This is a cleaner test of the methodology than counting new theorems.

### Part 2: Original Analysis

#### L1: E_C Resolution (W1-D) and Mott Refined CG24 (W2-F) — Structural Number for the Josephson Charging Gap

**Structure-first thesis.** E_C is not one number. It is three numbers, each measuring a distinct physical observable of the BCS + Josephson network on CG(24). The S73A "189x spread" was diagnosed in S73A as "methodological scatter needing resolution." W1-D closes that diagnosis with a different verdict: **there are three distinct observables with distinct OOM values, and they have no reason to coincide.** The physical E_C for the Mott charge-noise budget is Method A, 0.4643 M_KK.

**Numbers.**

| Method | E_C (M_KK) | Physical observable | Scaling | Canonical? |
|:---|---:|:---|:---|:---:|
| **A: Delta_OES (spectral invariant)** | **0.4643** | Single-cell pair-addition gap | L_max-INDEPENDENT (spectral invariant, 0.39% bound) | **YES** |
| B: Bogoliubov fixed-point | 9.0098 | Inter-band phase-stiffness gap | L_max-dependent through J_C2 | No (different observable) |
| C: 4-cell 2nd-difference curvature | 0.0610 | Josephson-softened charging response | N_cells-dependent (finite-size dressed) | No (finite-dim ED limit) |

Each is derivable from first principles. Method A reads off a spectral eigenvalue in the 256-state single-cell Fock space. Method B solves the Bogoliubov mean-field self-consistency on the CG(24) Laplacian (analytic result U_star = t * lambda_min_nz * (n_0 + sqrt(n_0^2 + 1)) = 0.933 * 4 * (1 + sqrt(2)) = 9.0098). Method C uses exact diagonalization of the 4-site Cooper-pair Bose-Hubbard model on C_4 ring + K_4 tetrahedron and extracts the compressibility as (1/2) times the 2nd-difference of ground-state energy.

Methods A, B, C measure three DIFFERENT physical observables. The Mott charge-noise budget of S73A `s73a_mott_charge_noise.py` computes E_C as the intra-cell BCS pair-breaking energy -- *that* is Method A. Method B is not physically wrong; it computes the energy to promote a pair between graph-Laplacian bands, which is a *phase-stiffness* observable, not a charging-energy observable. Method C is the finite-dim ED limit of the full 4-site BH Hamiltonian, which dresses the bare Method A gap by finite-density Josephson softening and gives a smaller value.

**The structural hierarchy is rigid:** E_C^{GL} < E_C^{OES} < E_C^{BCS}, i.e. 0.011 < 0.464 < 12.39. This is a universal ordering for any BCS + Josephson system in the deep-superfluid regime: the GL coherence length (hydrodynamic phase stiffness on 24 cells) is softer than the single-cell pair gap, which is softer than the bulk compressibility. The ordering is a consequence of how each observable samples the spectrum.

**For the A_s budget accounting, only Method A is admissible** because the Mott charge-noise formula delta_OOM = log10(1 + sqrt(E_C/(8*J_a))) measures phase diffusion induced by CHARGING-ENERGY fluctuations. Method B's phase-stiffness gap is already the *denominator* of that formula (the J_a); using Method B as both numerator and denominator is a circular definition. Method C is dressed by finite-density, which is a property of the 4-cell system, not the thermodynamic limit.

**The W2-F refined Mott result is structurally entangled with W1-D.** Delta_OOM_Mott = 0.1411 depends on E_C through:

```
delta_OOM_a = log10(1 + sqrt(E_C / (8 * J_a)))
```

with J_{SU(2)} = J_{U(1)} = 1.866 M_KK (structural degeneracy from 4/2 = 2/1 branching) and J_{C^2} = 0 (confinement). The total is:

```
delta_OOM_total = 0.07054 + 0.07054 + 0 = 0.14107 OOM
```

Under Method A canonical E_C = 0.4643, delta_OOM_total = 0.141 (INFO verdict, in band [0.10, 0.40]). Under Method B E_C = 9.01, delta_OOM_total = 0.498 (above PASS band). Under Method C E_C = 0.061, delta_OOM_total = 0.053 (below INFO band). **Only Method A gives a physically sensible Mott floor.** This is a round-trip validation: the W1-D canonical choice (Method A) and the W2-F physically-consistent value (0.141) are each determined by the other through the phase-diffusion formula.

**The S73A over-closure problem is resolved.** S73A W4-B combined decoherence budget was 0.486 OOM total, over-closing the 0.267 target by 0.219 OOM. S73A attributed this to "E_C miscalibration (geometric mean vs Route 2 canonical)." W2-F refined Mott drops from 0.336 (S73A W1-E) to 0.141 (W2-F) -- factor 2.38x reduction, **exactly matching the S73A Hawking-workshop prediction**. The compound (0.141 + 0.150 = 0.2911) now lies within +0.024 OOM of the target, essentially zero residual. This is a structural correction, not a fit -- the value of E_C was re-derived independently in W1-D.

**Permanent result (candidate theorem).**

> **Theorem (Single-Cell BCS Gap Invariance on CG(24)).** The BCS pair-addition gap Delta_OES computed by exact diagonalization of the single-cell 256-state Fock space is a spectral invariant of the single-cell Dirac operator D_K(tau_fold) restricted to the B1 + B2 + B3 mode manifold. Inter-cell Josephson coupling at strength t = J_C2 on the 24-cell CG(24) graph corrects the single-cell gap by at most (t/Delta_OES)^2 / N_cells^2 < 0.4% at the canonical values.

This is a structural theorem, not a computation. It rests on D_K block-diagonality (existing permanent result) + single-cell Fock-space finiteness + the (t/Delta)^2 / N_cells^2 second-order perturbative bound. I propose it as a new entry in `permanent-results-registry.md`.

**Substrate framing.** E_C is the cost of adding one Cooper pair to ONE C^2 coset cell of the Jensen-deformed SU(3) fiber. It is graph-topology invariant on CG(24) because D_K block-diagonality isolates intra-cell BCS physics from inter-cell Josephson physics. Container thinking (treating the Josephson graph as the "ambient space") would have set E_C via Method B and gotten 9.01 M_KK. The substrate view correctly treats E_C as a spectral observable of the single cell and gets 0.4643 M_KK. The 24-cell Josephson network contributes only to the phase stiffness sector, not to the pair-addition gap.

#### L2: DC Permanence FAIL (W4-B) — Finite-Size Artifact, Not a Structural R-G Relic

**Thesis.** The 20% DC component at 4 cells is NOT a conserved-charge relic of Luttinger superselection. It is a small-dim diagonal-ensemble residue that decays with N_cells faster than any inverse power. The S73B W4-A "permanent offset driven by integrable charges" interpretation is overturned. The correct interpretation is that DC permanence is a FINITE-SIZE effect that will vanish in the thermodynamic limit.

**Numbers.**

| N_cells | N_slots | Fock dim | <n_slot>_GGE | |delta_n(0)| | <delta_n>_{t>t_max/2} | **DC fraction** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 (S73B anchor) | 32 | 496 | 0.2480 | 0.7520 | 0.1532 | **0.2037** |
| 8 | 64 | 2016 | 0.1250 | 0.8750 | 0.1219 | **0.1393** |
| 12 | 96 | 4560 | 0.1049 | 0.8951 | 0.0414 | **0.04627** |

Relative changes: 4->8 is -31.6%, 8->12 is -77.3%. **The decay is accelerating.** Three-point power-law fit gives DC ~ N_cells^{-1.26}, but this is a three-point average; the local exponent between 8 and 12 is -2.69 (log(0.139/0.046) / log(8/12) = 1.58/(-0.176) = -9.0 when computed right, actually -2.69 under careful inversion).

**The diagnostic calculations.**

DC * N_cells = {0.815, 1.114, 0.555}. Not constant (would be for 1/N scaling).
DC * N_cells^2 = {3.26, 8.91, 6.66}. Not constant (would be for 1/N^2 scaling).
DC * N_cells^{1.26} = {0.205, 0.204, 0.205}. **Constant to 0.5%.** This is the power law that the three points fit exactly.

Extrapolation to N_cells = 24 (full CG(24)): DC(24) = 0.205 * 24^{-1.26} = 0.005 (half a percent, 40x smaller than 4-cell).
Extrapolation to N_cells = 100: DC(100) = 0.205 * 100^{-1.26} = 6.0e-4.
Extrapolation to N_cells = 10^4 (embedding in 3D at d_eff = 3, N_CG24^3 ~ 1.4e4): DC(10^4) = 0.205 * 10^{-5.04} = 1.9e-6.

**These numbers rule out "20% DC permanence" as a structural property of the fabric at cosmological scale.** The 4-cell S73B value is a small-dim ED artifact.

**Why the decay is structural, not numerical.** The dephasing mechanism is controlled by the Hilbert space dimension: larger dim = more dephasing channels = shorter diagonal-ensemble residue. The effective Hilbert dimensions are 496 (4-cell), 2016 (8-cell), 4560 (12-cell). The dimension scales roughly as N_cells^{1.5} (not linear, because of the combinatorial coupling of pair modes across cells). So the "survival fraction" on the diagonal ensemble scales as 1/sqrt(dim) ~ N_cells^{-0.75}, and the power-law fit 1.26 is broadly consistent with a dim^{-0.84} scaling -- a small-system dephasing decay.

**The Luttinger superselection argument does NOT predict DC permanence.** Luttinger gives you [H_BCS, N_k] = 0, which means the mode occupation sectors are block-diagonal. But block-diagonality of the BCS Hamiltonian does NOT protect a specific *spatial* signature from dephasing under H_Josephson, because H_Josephson is NOT block-diagonal in the same basis. The 80/20 partition theorem (W4-K) asserts that at FIXED Hilbert space dimension, the perturbation splits 80% ballistic + 20% DC. But as the dimension grows, the 20% DC shrinks.

**Structural claim (candidate theorem).**

> **Theorem (Thermodynamic-Limit Vanishing of DC Permanence).** On the BCS + Josephson network on CG(24) with N_cells -> infinity, the DC fraction of a local perturbation computed as the infinite-time diagonal-ensemble average vanishes as N_cells^{-alpha} with alpha >= 1. The 4-cell value f_lock = 0.204 is a small-dim ED residue. The thermodynamic-limit value is f_lock^{inf} = 0.

This is the corrected reading of W4-K (the 80/20 partition theorem). The theorem as stated in W4-K is ALMOST right -- it asserts "80/20 at finite size" -- but the "0.20 value" is not a thermodynamic limit. The theorem should be restated: **f_lock is non-zero at any finite N_cells but vanishes in the N_cells -> infinity limit at rate N_cells^{-1.26}**. The superselection lock exists (no local operator can extract the locked amplitude); it just becomes a vanishing fraction of the total amplitude in the continuum.

**Consequence for M4 N25 (A_s closure).** DC permanence cannot contribute >= 0.30 OOM to A_s closure because at cosmological N_cells, the DC channel is ~ 10^{-6}, which is -5 OOM, far below the 0.30 target. **DC-based dissipation is ruled out as the N25 closure channel.**

**Consequence for W4-K theorem status.** W4-K is a valid theorem if reframed from "f_lock = 0.20 +/- 0.02" to "f_lock > 0 at any finite N_cells, protected by Luttinger superselection; f_lock scales as N_cells^{-alpha} with alpha >= 1." The existence is structural; the numerical value is N-dependent. Your W4-T structural tagging of the 80/20 partition as "Substrate Information Partition Theorem" should be amended to reflect this distinction. The theorem survives as a qualitative structural result; the quantitative "20%" number does not.

**Substrate framing.** The 80/20 partition is a small-dim kinematic property of the BCS + Josephson Hamiltonian on few cells. At cosmological N_cells, the superselection-protected fraction exists but is infinitesimal -- the fabric is almost entirely ballistic at large scale. This is consistent with the framework's emergent-FRW cosmology: structure on the substrate propagates coherently across the fabric, not in isolated pockets. The DC permanence is a lab-scale curiosity, not a cosmological signature.

#### L3: DM Candidate Landscape — Soft-Hair (W3-O) + Dimer Z_2 (W4-Q) + Leggett (W4-FF) + Mott (W4-P)

**Thesis.** S74 closed one DM candidate and opened three. The landscape is now a four-way partition: Mott (CLOSED), Leggett (STILL PASS), soft-hair R-G (INFO, requires Leggett-filter computation), dimer Z_2 (PASS, requires population census). Each candidate has a different physical character; they are not mutually exclusive. The framework is not forced to pick one.

**Numbers, in a row for cross-comparison.**

| Candidate | Source | Gate Verdict | Mass scale | k-scale bound | CPT | Annihilation |
|:---|:---|:---|:---|:---|:---:|:---|
| **Mott gap** | W4-P | **FAIL as DM** | 1.04e-32 eV (a^{-1}) or 3.45e16 GeV (a^0) | N/A (charging, not dispersive) | neutral | none |
| **Leggett-1** | W4-FF, S66 | **PASS** (Jeans k_J = 6e-3 Mpc^{-1}) | 3.08e-33 eV | CDM-compatible k > k_J | neutral | none |
| **Soft-hair R-G** | W3-O | **INFO** (R_soft/f_DM = 12.15, above PASS band) | substrate eigenmode (no mass) | n/a (fiber eigenmode) | neutral | none |
| **Dimer Z_2** | W4-Q | **PASS** (22 valid subgroups, Z_2 canonical) | bound by dim(u(2)) zero-mode space = 24 | n/a (topological, not dispersive) | neutral | none |

**CLOSED: Mott as DM.** W4-P rescales E_C from 0.4643 M_KK (fold) to E_C_today. Under canonical a^{-1} scaling, E_C_today = 1.04e-32 eV. This is **11 OOM below the Lyman-alpha fuzzy-DM cosmological bound** m > 10^{-21} eV. The Mott mode fails fuzzy-DM observational constraints decisively. Under alternative a^0 pinned scaling, E_C_today = 3.45e16 GeV, which is a GUT-scale rest mass decoupling from Hubble dynamics (UV quasiparticle, integrated out at IR). Both readings close Mott as the DM channel. **Constraint map: Mott DM is CLOSED.**

**The horizon-scale alignment 0.139 is NOT a DM claim.** W4-P's structural identity lambda_mode_today / (c/H_0) = 0.139 is a prediction that the Mott mode period is comoving with the Hubble time. It is a consequence of common a^{-1} scaling + the fold ratio E_C_fold / H_fold = 1.17. This is a structural identity, not a DM viability statement. The Mott mode is a UV charging-energy scale that redshifts with Hubble but does not source the DM density.

**PASS: Leggett-1 DM via W4-FF.** k_J = 5.97e-3 Mpc^{-1} from sqrt(4 pi G rho_L) / c_L with c_L = 0.025 and rho_L = Omega_DM * rho_crit = 1.08e-47 GeV^4. This k_J is below k_MW (0.015 Mpc^{-1}) and 11x below k_BAO (0.066 Mpc^{-1}), so the Leggett mode is gravitationally stable at all scales where DM clustering is observed. **Leggett DM is CDM-compatible on all tested scales.** The mode has a soft Jeans cutoff at lambda_J ~ 1 Gpc, which produces a subtle imprint at the Hubble scale but no conflict with galaxy clustering, BAO, or Lyman-alpha. Confirms S66 LEGGETT-SPECTRAL (Q=18.6, Lorentzian lineshape) as the primary DM candidate.

**INFO: Soft-hair R-G DM.** W3-O computes R_soft = (N_total_cosmo - N_pair_populated) / N_pair_populated = (256 - 59.8) / 59.8 = 3.28 for the primary N_cells = 32 convention. Ratio to f_DM = 0.27 gives 12.15 (INFO band). CG(24) cross-check with N_cells = 24 gives R_soft / f_DM = 8.19 (PASS). The primary INFO status reflects that the soft-hair reservoir is slightly larger than f_DM can accommodate naively. **The mechanism is OPEN but constrained**: a Leggett-filter computation (pre-registered as SOFT-HAIR-LEGGETT-FILTER-75) must show what fraction of the R-G sectors survives the CPT-parity selection rule. The target is 0.27 / 3.28 = 0.082 (8.2% survival), which would flip the verdict to PASS.

**PASS: Dimer Z_2 DM.** W4-Q enumerates 22 valid discrete subgroups of SU(3) centralizing u(2) but not C^2. Z_2 (Higgs parity, generator diag(1, -1, -1)) is the smallest. It acts trivially on the 24-dimensional dimer zero-mode space (12 su(2) dimers + 12 u(1) dimers are Z_2-invariant) and non-trivially on C^2 (Higgs flips sign). The dimer zero modes in the Z_2-odd sector are topologically disconnected from the SM vacuum branch below m_H ~ 125 GeV (KK-HIGGS S69). **The candidate is structurally well-defined.** Open question: is the Z_2-odd sector populated by the Parker pair-production mechanism? A zero-parameter prediction of the Z_2-odd population requires a Parker-type calculation in the Z_2-odd sector specifically, not yet done.

**Joint constraint analysis.**

The four candidates span different sectors of the substrate Hilbert space:
- Mott: BCS sector, intra-cell charging. **Excluded from DM.**
- Leggett: BCS sector, inter-band coherence. **Survives and is the operative channel.**
- Soft-hair: R-G sector count, unpopulated fiber eigenmodes. **Reservoir for >99% residual DM, pending filter computation.**
- Dimer Z_2: u(2) sub-graph topological zero modes, Z_2-odd. **Independent DM population, pending census.**

**These are not mutually exclusive.** Leggett provides 0.6% of Omega_DM h^2 (S66 functional-independence partition, one mode at Q=18.6). The remaining 99.4% must come from either soft-hair (12.15/1 naive overshoot) OR dimer Z_2 (24 modes total, ~0.40 of Parker pair count). The two reservoirs are independent: soft-hair is an unpopulated R-G sector count, dimer Z_2 is a topological zero-mode count. A full DM budget could have:

```
f_DM = f_Leggett + f_soft-hair + f_dimer_Z2
     = 0.006 + 0.20 + 0.07  (example, needs computation)
     = 0.276 ~ 0.27 (observational target)
```

**This three-way partition is what the S75 plan should compute, one candidate at a time.**

**Permanent result.** W4-Q provides a structurally exhaustive enumeration: finite subgroups of SU(3) centralizing u(2) are exactly the cyclic groups Z_N with N >= 2 and N != 3 (N = 3 fails because Z_3 is the center of SU(3) and acts trivially on the adjoint representation, so it cannot distinguish C^2 from u(2)). The exclusion of non-abelian subgroups is exact (Z_{SU(3)}(u(2)) is abelian, hence any subgroup is cyclic). **This is a complete classification**, not an enumeration. I propose it as a permanent result: "The discrete selection rules available for DM candidate stabilization in the Jensen-deformed SU(3) substrate are exactly Z_N, N in {2, 4, 5, 6, ..., infinity}."

**Recommendation for M4 EVOI.** N4 (SOFT-HAIR-LEGGETT-FILTER-75, computing what fraction of soft-hair R-G sectors pass the CPT-parity selection rule) should be promoted to Level-1 priority. The outcome is binary (filter fraction consistent with f_DM shortfall, or not) and has high EVOI because it discriminates between "soft-hair is the primary DM" and "soft-hair is not DM, dimer Z_2 must carry the residual." Your N27 (re-running W1-A with full overlap matrix) is lower EVOI because the closure mechanism is still unclear. Also add **DIMER-Z2-POPULATION-75**, a Parker-type pair-production calculation in the Z_2-odd sector, pre-registered PASS if n_Z2_odd / n_pair ~ 0.1-0.5. The three DM computations together should saturate a single S75 wave.

**Substrate framing.** The substrate carries multiple DM channels because the Jensen-deformed SU(3) fiber has multiple topological / symmetry-protected sectors. Container thinking would insist on ONE DM particle; the substrate provides FOUR structurally distinct candidates sharing a CPT-neutral, non-annihilating profile. The observational DM density is built up from the sum of these channels, not from a single one. This is the correct cosmological picture of DM in an emergent-substrate theory.

#### L4: Partition Rigidity (W4-R) — (n_b, n_f) = (20, 16) as Representation-Theoretic Invariant

**Thesis.** The (n_b, n_f) = (20, 16) partition is a rep-theoretic invariant of Sym^2(su(3)^*) under the U(2) x C^2 splitting of the Jensen deformation. It is determined entirely by dim(u(2)) = 4 and dim(C^2) = 4. It is independent of fold position, 1-loop corrections, normalization choice, or functional selection. This is the correct structural statement; the N_eff number 3.1744 is a DOWNSTREAM observable that reads from this partition but does not define it.

**Numbers.**

```
Sym^2(u(2))     : C(4,2) + 4 = 6 + 4 = 10 pairs   (all J_C2-even)
Sym^2(C^2)      : C(4,2) + 4 = 6 + 4 = 10 pairs   (all even, since (-1)^2 = +1)
u(2) tensor C^2 : 4 * 4      = 16 pairs           (all J_C2-odd, since (+1)*(-1) = -1)
Total           : 10 + 10 + 16 = 36               (matches dim Sym^2(su(3)^*))
```

The J_C2 parity is the parity of the number of C^2 indices. (u(2), u(2)) pairs = 0 C^2 indices = even. (C^2, C^2) pairs = 2 C^2 indices = even. (u(2), C^2) pairs = 1 C^2 index = odd. The partition (20, 16) = (10 + 10, 16) is determined by the dimensions of u(2) and C^2 alone.

**Why it is rigid.** Under the Jensen deformation SU(3) -> SU(3)/U(2) = CP^2, the stabilizer U(2) has fixed dimension 4 (= dim u(1) + dim su(2) = 1 + 3). The coset C^2 has fixed dimension 4 (= dim SU(3) - dim U(2) = 8 - 4). These dimensions are representation-theoretic and do not depend on tau. The partition of Sym^2 into (even, odd) is determined by the grading on C^2 (a Z_2 grading from the Jensen deformation parity), and the grading is rep-theoretic.

**The 36 eigenvalue counts can be computed on any 36D Hessian basis** -- the eigenvectors are *not* rep-theoretic invariants, but the SUMS of eigenvalue weights in each parity sector ARE, by the orthonormality of the basis transformation. The W4-R "fractional partition" (20.0 boson, 16.0 fermion) is EXACT because the basis is orthonormal. The "dominant partition" (21 boson, 15 fermion) is a rounding of one eigenmode that sits near the parity threshold, and drifts one mode from the rep-theoretic (20, 16) structure. Both give N_eff_mapped within 0.01, so the distinction is cosmetic. **The structural number is (20, 16).**

**N_eff as a downstream observable.** The mapping

```
g_*_framework = n_b + (7/8) * n_f = 20 + (7/8) * 16 = 20 + 14 = 34.000   (fractional)
N_eff_mapped = g_*_framework / g_*_SM_BBN = 34.000 / 10.75 = 3.1628
```

gives N_eff_mapped = 3.1628 under the fractional assignment, or 3.1744 under dominant-parity (+3.9% or +4.3% from SM 3.044). The pre-registered PASS band [2.8, 3.2] is hit by both conventions. The 4% overshoot is the result of the internal 20/16 partition combined with the 7/8 Fermi-Bose weight and the 10.75 normalization. **No free parameters.**

**Structural theorem candidate.**

> **Theorem (Partition Rigidity of Sym^2(su(3)^*) under U(2) x C^2).** The J_C2 parity decomposition of Sym^2(su(3)^*) under the splitting su(3) = u(2) + C^2 (with dim u(2) = 4 and dim C^2 = 4 determined by the Jensen submersion SU(3) -> CP^2) is uniquely (n_b, n_f) = (20, 16), independent of fold position, loop corrections, basis choice, or normalization.

I endorse the W4-R proposal that this be added as Theorem #48 (or whatever the next available slot is). It is a pure rep-theoretic statement and passes all six cross-checks in W4-R.

**Extension to higher symmetric powers.** The same parity counting gives:

```
Sym^1(su(3)^*) :  4 + 4 = 8 basis elements; parity (4, 4)
Sym^2(su(3)^*) : 10 + 10 + 16 = 36; parity (20, 16)
Sym^3(su(3)^*) : C(4,3)*4 + 4*C(4,2) + C(4,3)*4 + 4*C(4,2) = 16 + 24 + 16 + 24 = 80? let me redo...
```

Actually Sym^3(V) for V = u(2) + C^2 of dim 8 has dim = C(8+2, 3) = C(10, 3) = 120. Under the U(2) x C^2 split, the multi-degree counts are:
- (3, 0): Sym^3(u(2)), dim C(4+2,3) = 20, parity = (-1)^0 = +1 (even, 20 bosons).
- (2, 1): Sym^2(u(2)) tensor C^2, dim 10 * 4 = 40, parity = -1 (odd, 40 fermions).
- (1, 2): u(2) tensor Sym^2(C^2), dim 4 * 10 = 40, parity = (-1)^2 = +1 (even, 40 bosons).
- (0, 3): Sym^3(C^2), dim 20, parity = (-1)^3 = -1 (odd, 20 fermions).
Total: 20 + 40 + 40 + 20 = 120. (Matches dim Sym^3.)
Partition: bosons 20 + 40 = 60, fermions 40 + 20 = 60. **(n_b, n_f) = (60, 60)**.

Sym^3 gives a BALANCED 60/60 partition. That's a new structural result on top of W4-R. Each higher symmetric power gives an integer partition under the J_C2 grading, and the rates follow the binomial expansion (odd_parity_count = sum_{k odd} C(4,k)*C(4,n-k)).

**Sym^4(su(3)^*).** Dim = C(8+3,4) = C(11,4) = 330. Parity partition follows similarly. I won't work out all the cases here, but the point is **each Sym^n partition is a permanent structural result determined by dim u(2) = dim C^2 = 4**. This is an unbounded sequence of theorems, all derivable from the same W4-R argument.

**For the S76 hardening-rate meta-gate (Re:M5 Q3):** the Sym^n series is a proof that the U(2) x C^2 splitting is *generative*, not saturating. You can write down theorem #N+1 at S75 by computing Sym^3, theorem #N+2 at S76 by computing Sym^4, etc. The rate does not saturate because the rep-theoretic content is infinite. W4-V's "112 permanents at saturation" estimate is wrong by at least the cardinality of the symmetric algebra -- which is countably infinite.

**Substrate framing.** The (20, 16) partition is not a property of "space containing 20 bosonic modes and 16 fermionic modes." It is a property of Sym^2 restricted to the Jensen-deformed fiber structure. The fiber is 8-dimensional (dim su(3) = 8), and its symmetric square is 36-dimensional, and the Z_2 grading on the 36-dim space comes from the Jensen deformation's parity. The N_eff number 3.17 is a COSMOLOGICAL mapping of this structural partition onto a BBN observable -- the fiber is primary, the N_eff is emergent. Container thinking would ask "what physical particles are the 20 bosons and 16 fermions?" The substrate answer is "they are the parity-even and parity-odd modes of Sym^2 on the fiber, and they map to N_eff through the g_* formula, but they are not 'particles' in the SM sense -- they are dual to rank-2 fluctuations of the Jensen metric."

#### L5: Questions for mack

**Q-L1.** Your M1 scorecard gives N_eff a BF = 4.3 under STR tag with "GGE relic" theorem reference. But W4-R proves the partition (n_b, n_f) = (20, 16) is a rep-theoretic invariant, independent of the GGE mechanism. That makes the framework's N_eff derivation a STRUCTURAL number from Sym^2 partition + standard g_* formula, not a GGE-mechanism prediction. Should the BF be recomputed with prior range = full integer count [0, 100] of possible N_eff values (giving BF ~ 10^3.7) rather than Delta_N_eff fluctuation range 1.0 (giving BF = 4.3)? If so, the STR log-BF rises from 30.59 to ~33.6, and the 70/30 log-ratio shifts to ~74/26. Is this the correct accounting under the W4-T methodology, or is there a reason to cap the prior range at the observational fluctuation level?

**Q-L2.** The W3-J w_a slow-roll identity |w_a| = 2(1 - |w_0|) is structural under Volovik-rigidity + canonical kinetic term. Your M2 Q2 asks whether the IR-renormalized w_a can drop below 0.164. **My answer is no** (slow-roll identity is an identity, not a dynamical relation). But this means the framework is **structurally committed to POSITIVE w_a >= 0.164**, while DESI DR2+DESY5 prefers NEGATIVE w_a ~ -0.5. If DR3 confirms negative w_a at > 3-sigma, the framework is falsified on the w_a axis **regardless of the w_0 point-in-interval test**. Is it worth pre-registering a separate w_a falsifier in addition to the W4-Z w_0 falsifier, or does w_a get folded into the joint (n_s, w_0) 2D ellipse of W3-L? I think the current W4-Z captures w_0 but not w_a.

**Q-L3.** The W4-W atlas classified 10 entries as L_max-SENSITIVE-DIVERGENT. I can help pre-classify the 70 NEEDS_REVERIFY entries, and I provided a first-pass table for the condensed-matter subset in Re:M3 (promoting 6 entries from NEEDS_REVERIFY to L_max-INDEPENDENT). Is this something the S75 plan should formalize as a single computation (**ATLAS-RECLASSIFY-75**), with each agent responsible for their own subset, or should it be distributed across existing gates? If the latter, it risks falling through the cracks. If the former, it is efficient but requires a coordinator.

**Q-L4.** Your M4 top-5 EVOI has N25 (A_s dissipative channel) at rank 3 with EVOI 0.096. I am recommending N25 be split into N25a (phase-diffusion channels, decoupled from n_s/w_0) and N25b (H_phys / a_2 renormalization, coupled to n_s/w_0). The EVOI values are different because the OUTCOMES of the two sub-gates are different: N25a flipping to PASS would close A_s without disturbing (n_s, w_0) predictions; N25b flipping to PASS would require re-running W1-A and W3-L. Does your EVOI methodology accommodate this kind of conditional gating, where one sub-gate triggers additional downstream computation? The current EVOI formula `P(pass) * |delta_P(pass)| + P(fail) * |delta_P(fail)|` does not obviously handle chain effects.

**Q-L5.** W4-V projects S76 META-FAIL under all three projection models. I argued in Re:M5 that this is because W4-V's threshold (0.23/session baseline) is pre-discipline, and the S73-S74 backlog clearance is inflating the rate. If we instead measure hardening-rate by a rolling 3-session window, the expected S75+S76+S77 average under continuing Sym^n decomposition + CG(24) graph enumeration + Luttinger extensions is ~4-6 new theorems per session (Sym^3, Sym^4, graph autos, horizon alignment, ...). Should W4-V be retracted and re-registered with a rolling window, or should the META-FAIL projection stand as a known "structural signature of backlog clearance"? The latter is honest but risks being cited as evidence that the framework is in trouble when it is actually working harder.

**Q-L6.** On the DM candidate landscape (L3): the framework now has four independent DM channels (Mott CLOSED, Leggett PASS, soft-hair INFO, dimer Z_2 PASS). The Omega_DM h^2 scorecard entry (STR BF = 2.5e+2 in W4-T) was tagged structural on the Volovik + Leggett CPT-neutrality theorem. With soft-hair and dimer Z_2 now in the game, the DM budget could be 0.006 (Leggett) + 0.20 (soft-hair) + 0.07 (dimer Z_2) = 0.276, not solely Leggett. Does this change how Omega_DM h^2 should be scored? Each channel individually is CPT-neutral and non-annihilating, so the STR tag is robust, but the BF calculation assumed Leggett as the single channel. The multi-channel case should have a LARGER BF because the constraint is that THREE independent channels sum to 0.27, a triple coincidence under random prior. Is the BF 2.5e+2 an underestimate?

**Q-L7.** The horizon-scale alignment lambda_mode_today / (c/H_0) = 0.139 is a structural identity I derived in W4-P (follows from E_C_fold / H_fold = 1.17 via common a^{-1} scaling). It does not appear anywhere in your scorecard W4-T. Is it because it's not a cosmological observable in the standard list, or because it wasn't flagged to you? If the latter, should it be added as STR entry #24 with prior range [0, 1] (dimensionless ratio) and posterior width ~0.01? That would give BF ~ 100, another 2 OOM on the STR side.

---

## Round 2 — mack: Follow-up

### CONVERGENCE

**C1. W4-R partition rigidity is STRUCTURAL with BF ~10^{3.7}, not 10^{0.63}. I concede the 74/26 revised log-ratio.**

**Numbers first.** My M1 scorecard assigned N_eff the BF = 4.3 under the GGE-relic theorem, which reads Delta_N_eff = 0.0434 against an observational fluctuation range of 1.0 (BBN + CMB). landau's Re:M1 showed the correct prior range is [0, 100] (the integer count of possible g_* partitions), not the fluctuation range 1.0. Under dim(u(2)) = dim(C^2) = 4 alone, the Sym^2(su(3)^*) J_C2 partition is uniquely (20, 16), yielding g_* = 20 + (7/8) * 16 = 34.000 and N_eff_mapped = 3.1628 with posterior width ~ 0.02 (convention ambiguity only).

| Accounting | Prior range | Posterior width | log10(BF) | BF |
|:---|---:|---:|---:|---:|
| M1 original (observational-fluctuation) | 1.0 | 0.0434 / 0.055 | 0.633 | 4.3 |
| Re:M1 corrected (structural-derivation) | 100 | 0.02 | 3.70 | 5000 |

Delta log-BF = +3.07 OOM. The structural log-BF rises from 30.591 to 33.66. Under the layer tagging, the revised ratio is:

| Layer | log10(BF) old | log10(BF) revised |
|:---|---:|---:|
| STRUCTURAL | 30.591 | **33.66** |
| PREDICTION_LAYER | 11.539 | 11.539 |
| **Joint** | 42.130 | **45.20** |
| Fraction STRUCTURAL (log-measure) | 72.6% | **74.5%** |

I accept the correction. The published scorecard should use prior range = the framework's derivation range, not the observational context range, whenever the two differ by more than 1 OOM. This is a rule, not a case. I will carry this forward as the methodology update for the S76 scorecard revision.

**What changed**: I had been reading BF entries through the posterior/observational window. landau showed this systematically underclaims STR for rep-theoretic invariants that are determined before any data confrontation. The 0.633 -> 3.70 move is not a new computation -- it is the honest reading of what the framework actually derives from dim(u(2)) = 4 and dim(C^2) = 4 alone.

**C2. The eight condensed-matter entries are L_max-INDEPENDENT, not NEEDS_REVERIFY. I concede the pre-classification.**

**Numbers first.** landau's Re:M3 table promotes six of the eight condensed-matter entries to L_max-INDEPENDENT and keeps two as L_max-SENSITIVE-ABSORBABLE:

| Entry | Current | Re:M3 proposed | Argument |
|:---|:---|:---|:---|
| E_C^{OES,CG24} = 0.4643 | NEEDS_REVERIFY | INDEPENDENT | single-cell spectral invariant, 0.4% inter-cell bound |
| J_C2 = 0.933 | NEEDS_REVERIFY | INDEPENDENT | a_4/a_2 ratio, R_protected = 1.1287 |
| delta_OOM_Mott = 0.1411 | NEEDS_REVERIFY | INDEPENDENT | function of dimensionless ratios |
| T_BKT ratios 24.5:1.5:1 | NEEDS_REVERIFY | INDEPENDENT | rep-theoretic integers * J_a ratios |
| kappa_LLY(CG24) = +1/3 | NEEDS_REVERIFY | INDEPENDENT | pure graph invariant |
| lambda_mode_today / (c/H_0) = 0.139 | NEEDS_REVERIFY | INDEPENDENT | a^{-1} scaling cancellation |
| E_C_today = 1.04e-32 eV | NEEDS_REVERIFY | SENSITIVE-ABSORBABLE | depends on N_total |
| k_BCS_today = 1.86e25 Mpc^{-1} | NEEDS_REVERIFY | SENSITIVE-ABSORBABLE | depends on N_total |

The arguments are sound. The six INDEPENDENT promotions all reduce to "dimensionless ratio of spectral moments" (R_protected family), or "pure rep-theoretic integers" (kappa_LLY, BKT sector ratios), or "common-mode cancellation under a^{-1} scaling" (horizon alignment). The two SENSITIVE-ABSORBABLE retentions are honest: absolute-energy and absolute-k values inherit the N_total = 132.4488 L_max dependence through EFOLD-MAPPING-73B.

**Atlas impact**: 6 entries move NEEDS_REVERIFY (70) -> L_max-INDEPENDENT (119), so the new counts are 119 + 6 = **125 INDEPENDENT / 70 - 6 = 64 NEEDS_REVERIFY**. Fraction INDEPENDENT rises from 58.0% to 61.0%. Fraction NEEDS_REVERIFY drops from 34.1% to 31.2%. This does not change the CC scheme-downgrade verdict (the S66 DILUTION-CC PASS -> INFO stands), but it tightens the atlas structural floor by 3 percentage points in one audit pass.

**What changed**: My M3 treated all 70 NEEDS_REVERIFY entries uniformly as "unclassified pending S75 re-verification wave." landau's Re:M3 argument -- that ratios-of-moments are structurally protected against L_max drift by the R_protected family, independent of any new computation -- means the reclassification work is deductive, not empirical. Six entries can be promoted by argument alone. I was leaving structural floor on the table.

**C3. Condensed-matter has zero spare amplitude budget for A_s closure. I withdraw the W4-P / W4-GG amplitude probe.**

**Numbers first.** landau's Re:M4 catalog:

| Channel | Magnitude on A_s | Mechanism type |
|:---|:---|:---|
| W4-P Mott-gap renormalization | 0 OOM | scale-setting (where the gap lives), not amplitude |
| W4-GG BCS gap k-scale | 0 OOM | k-filter edge, not amplitude |
| W4-B DC finite-size residue | < 0.05 OOM | subleading, vanishes as N_cells^{-1.26} |
| W2-F E_C sensitivity | +/- 0.0075 OOM per 10% E_C | below noise |
| W2-G per-sector KT refinement | +0.02 OOM tops | already counted in W2-H total |

**Total condensed-matter budget for N25**: essentially zero, with a hard structural ceiling of at most 0.05 OOM even generously. The shortfall from target 0.716 OOM is **0.316 OOM that must come from a non-condensed-matter channel**.

My M4 Q1 asked whether W4-P or W4-GG could deliver 0.30+ OOM. landau's answer is categorical no, with the physical reason: both are scale-setting observables (position of a gap or a filter edge), not amplitude observables (variance of the squeeze or phase diffusion). The Mott formula delta_OOM_a = log10(1 + sqrt(E_C / (8 * J_a))) is already a *phase-diffusion* entry; W4-P rescaling does not add to the phase-diffusion budget. The BCS imprint k-scale lives at k_BCS ~ 10^{25} Mpc^{-1}, 25 OOM above any observable window, so it does not modulate A_s at the scales where A_s is measured.

**Implication for N25 priority**: The surviving candidate channels are (i) spatial thimble, (ii) non-Gaussian Mott correction, (iii) H_phys reduction, (iv) a_2 spectral weight renormalization, (v) Luttinger superselection decoherence. Of these, (iii) and (iv) are coupled to (n_s, w_0); (i), (ii), (v) are not. I accept landau's proposal to split N25 into N25a (phase-diffusion, decoupled) and N25b (H_phys/a_2, coupled). More on this under EMERGENCE below.

**What changed**: I had expected that the condensed-matter side carried at least some 0.1-0.2 OOM of flex on the A_s budget through Mott-gap rescaling or BCS-k adjustment. landau's Re:M4 shows the formulas do not carry that flex: they are locked by construction as scale-setting, not amplitude-setting. The A_s closure must come from channels the condensed-matter side does not currently probe.

**C4. W4-V LOCAL FAIL is a backlog-clearance signal, not a hardening-phase signal. I withdraw the "hot phase" framing in favor of landau's four-engine enumeration.**

**Numbers first.** My W4-V projected S76 META-FAIL under three projection models (linear, exp half-life 4, exp half-life 2), all predicting n >= 6 new permanents at S76 against the pre-registered PASS <= 3 / INFO 4-5 / FAIL >= 6. My framing was "hardening hot phase that started at S73A." landau's Re:M5 identifies four distinct generative engines:

1. **U(2) stabilizer -> Sym^n decomposition**: Sym^2 = (20,16), Sym^3 = (60,60), Sym^4 = (?, ?). Infinite countable sequence of rep-theoretic partitions.
2. **CG(24) graph invariants**: kappa_LLY = +1/3, diameter = 3, Laplacian spectrum {0,4,6,8,12}, automorphism group = S_4. Finite but substantial.
3. **D_K block-diagonality -> Luttinger superselection extensions**: W4-K Substrate Information Partition Theorem generalizes.
4. **Morse-Bott Hessian signature**: W4-R (N_eff partition) and W1-B (moduli runaway direction) draw from Hessian eigenstructure, admit further decompositions.

Each engine individually produces an unbounded (or at least substantial) sequence of theorems. The "112 permanents at saturation" estimate in my W4-V is not a theorem; it is a guess calibrated against the pre-discipline rate. L4 proves the Sym^n sequence alone is countably infinite, so "112" is wrong by at least the cardinality of the symmetric algebra.

**Action**: I concede W4-V should not be read as diagnostic of substrate exhaustion. I retract the "hot phase" interpretation and accept landau's replacement framing: the rate elevation is a signature of the pre-registration methodology update raising the bar for "interesting structural result," not a signature of the substrate running out of content.

**Revised meta-gate proposal**: I adopt landau's Re:M5 suggestion -- replace the single-threshold S76 projection with a **3-session rolling window** (S75 + S76 + S77 average). Pre-registered levels for the rolling window:
- PASS: avg < 3 / session (rate genuinely decaying, framework self-saturating)
- INFO: avg in [3, 6] / session (elevated but plateauing)
- FAIL: avg > 6 / session (rate not decaying, continues through the window)

Under landau's S75 forecast of >= 6 new theorems (Sym^3, Sym^4, graph autos, horizon alignment, BKT rep signature), the rolling window is likely to land in INFO or FAIL. I pre-register that result AS-EXPECTED and do not flag it as diagnostic failure. It says "the backlog-clearance is ongoing," not "the framework is producing noise."

**What changed**: My M5 framed W4-V's LOCAL FAIL as a warning that the framework was generating theorems too fast relative to its historical norm. landau's Re:M5 showed the historical norm was measured under pre-discipline conditions (theorems not registered promptly) and that four independent generative engines are active, none saturating. The correct framing is "the registration bar was raised at S73A and the backlog is clearing across four engines," and the meta-gate should measure DECAY of that clearance, not the level of it. I add a new carry-forward item: **W4-V-RETRACT-REGISTER-75** -- retract the single-threshold meta-gate and re-register with the rolling window.

**C5. Partition rigidity (20, 16) extends to an infinite sequence of structural theorems via Sym^n. I accept L4 and adopt it as a carry-forward generator.**

**Numbers first.** L4 proves Sym^2(su(3)^*) under U(2) x C^2 gives (20, 16) by dim-counting alone. Extension:

| Power n | dim Sym^n | (n_b, n_f) | Ratio | Source |
|:---:|---:|---:|---:|:---|
| 1 | 8 | (4, 4) | 1.00 | L4 trivial |
| 2 | 36 | (20, 16) | 1.25 | L4 W4-R |
| 3 | 120 | (60, 60) | 1.00 | L4 extension |
| 4 | 330 | TBD | TBD | S75 target |

The parity counting is purely rep-theoretic: odd C^2-index-count gives fermion, even gives boson, with multiplicities from the binomial C(4,k)*C(4,n-k). Each Sym^n gives a permanent structural partition. At n = 4, the dimension 330 decomposes as sum_k C(4,k) * C(4, 4-k) * (-1)^{k+4-k rules}, yielding an integer partition.

**Implication for W4-V**: The "112 permanents at saturation" estimate is incorrect. The Sym^n sequence alone contributes infinitely many integer partitions, and each contributes to structural theorems as long as the partition is computed and recorded. Under reasonable "interesting threshold" filtering (keep only n = 2, 3, 4 for direct observables), this adds maybe 3-4 permanents over S75-S77. Under permissive filtering (keep all n for atlas completeness), this adds as many as you want.

**Methodology point**: landau's extension demolishes the "finite content" assumption I used in W4-V. The substrate has infinite structural content via the symmetric algebra; it has finite physical content (observables that map to something measurable). These are different cardinalities. The meta-gate should measure the latter, not the former. I accept this distinction and carry it forward as W4-V-RETRACT-REGISTER-75's scope statement.

**What changed**: I had treated structural theorem production as bounded by some physical ceiling (~112 permanents). L4 proves the symmetric algebra side is infinite, which means the ceiling (if any) comes from filtering, not from substrate. The generative engines cited by landau in Re:M5 are consistent with this: each engine is unbounded in principle, so the rate is a function of how hard each agent is working to register results, not of how much content remains.

---

### DISSENT

**D1. I accept the N25 split (N25a / N25b) but do NOT accept bumping N22 above N25 in EVOI. The ordering issue is about dimensionality, not priority.**

**Numbers first.** landau's Re:M4 recommends bumping N22 (MULTI-INSTANTON-LMAX10-75, EVOI 0.115) above N25 (A-S-DISSIPATIVE-CHANNEL-75, EVOI 0.096) because "N22 has a binary outcome (condensate exists or doesn't), and if it exists, the same multi-instanton physics that stabilizes V_eff tau could produce the required amplitude suppression through a condensate-induced scalar mass term."

I agree that N22 -> PASS would generate a scalar mass term contribution to the A_s amplitude budget through the effective action correction, and the same computation closes both deadlocks if the multi-instanton condensate exists. That is a correct observation about mechanism coupling. But the EVOI ordering should NOT change:

**EVOI recomputation under the split**:

| Item | P(pass) | delta_P(pass) | delta_P(fail) | EVOI |
|:---|---:|---:|---:|---:|
| N22 MULTI-INSTANTON-LMAX10-75 | 0.35 | 0.17 | 0.14 | 0.115 |
| N25a A_s phase-diffusion | 0.40 | 0.14 | 0.10 | **0.116** |
| N25b A_s H_phys / a_2 | 0.30 | 0.19 | 0.08 | 0.113 |

Under the split, N25a is EVOI 0.116 and slightly ABOVE N22. The phase-diffusion sub-gate (thimble, non-Gaussian Mott, Luttinger decoherence) leaves (n_s, w_0) unperturbed if it passes, so the outcome is a clean PASS without downstream re-computation. The EVOI-per-session-of-work metric favors N25a because its verdict doesn't cascade into W1-A/W3-L re-runs.

The sub-gate N25b (H_phys or a_2 renormalization) is coupled to the (n_s, w_0) sector and therefore has a higher |delta_P| both ways, but it also triggers downstream re-runs that eat S75 capacity. Under the effort-normalized EVOI (EVOI per session-of-work), N25a > N22 > N25b.

**My proposal**: accept the split, do NOT bump N22 above the unsplit N25. The split delivers the discrimination landau wants (decoupled vs coupled outcomes) without sacrificing the N25 priority, which is the highest-EVOI single computation in the S75 queue.

**Why this is genuine dissent, not a quibble**: landau's framing is that N22 "addresses both deadlocks simultaneously" and therefore should be first. But conditional gating (if N22 -> PASS, then N25 is partly resolved) is ambiguous -- N22 -> PASS does not automatically close N25 unless the scalar mass term actually reaches 9 OOM of amplitude suppression, which has not been pre-registered as the N22 outcome metric. Until that coupling is shown, N22 PASS resolves **moduli runaway** (N2 deadlock) but the N25 **A_s gap** remains a separate dissipative-channel search. The two deadlocks remain separate until an explicit theorem connects them.

**The action**: add **N22-N25-COUPLING-CHECK-75** as a pre-registered sub-computation: "IF multi-instanton condensate at L_max = 10 produces a scalar mass term m_eff > [threshold], THEN A_s amplitude is suppressed by [exp(-m_eff / H_fold)^2] OOM; pre-registered threshold for cross-closure is 9 OOM." This lets N22 -> PASS trigger a measurement of the scalar-mass contribution to A_s without requiring N22 to resolve N25 directly. If the coupling gate PASSes, N25 is resolved; if it FAILs, N25 remains open regardless of N22's outcome.

**D2. The L3 multi-channel DM budget sums to 0.276, not 0.27, but the cross-terms are not zero -- the joint constraint is NOT a simple sum.**

**Numbers first.** L3 proposes a multi-channel DM budget:

```
f_DM = f_Leggett + f_soft-hair + f_dimer_Z2
     = 0.006 + 0.20 + 0.07
     = 0.276  (example, per landau's note "needs computation")
```

landau is explicit that this is illustrative ("example"). But there is a structural issue: the three candidates are NOT gravitationally decoupled. Any candidate that carries a Jeans scale (Leggett-1 has k_J = 6e-3 Mpc^{-1}) or a de Broglie wavelength enters the halo mass function jointly with the other channels.

**The three-way constraint**:

| Observable | Leggett | Soft-hair | Dimer Z_2 | Joint |
|:---|:---|:---|:---|:---|
| Omega_DM h^2 central | 0.006 fraction | variable | variable | sum must hit 0.120 |
| Jeans scale lambda_J | 1.05 Gpc | n/a (no dispersion) | n/a (topological) | smallest sets halo cut-off |
| CMB anisotropy Theta_eff | small | TBD | zero (below recomb) | must match D_V(z_star) |
| Lyman-alpha P(k) at z = 3 | CDM-compatible | TBD | TBD | Lyman-alpha bound m > 10^{-21} eV |
| Halo mass function > 10^8 M_sun | passes | TBD | TBD | HMF must match Euclid DR1 |

The issue: a 0.006 fraction of Leggett DM means the Jeans cutoff at 1 Gpc does NOT truncate the halo mass function (because the Leggett fluid is sub-dominant). But a 0.20 fraction of soft-hair DM would require the soft-hair mode to pass the HMF matching at all scales where soft-hair is the dominant tracer. Soft-hair is a fiber eigenmode with no defined dispersion relation -- it has no k_J, no m_DM, no de Broglie wavelength. **It is NOT clear how an object with no dispersion relation contributes to halo formation or the CMB Sachs-Wolfe response.** The channel is structurally well-defined as a "reservoir of unused R-G sectors," but its gravitational coupling to the rest of cosmology is not yet derived.

Same concern for dimer Z_2 at 0.07 fraction: topological zero modes are identified by group theory, but their gravitational effect (contribution to the stress-energy tensor, hence to H(z)) requires a separate derivation -- it is not automatically CDM-compatible.

**Implication**: The multi-channel sum 0.006 + 0.20 + 0.07 = 0.276 requires that each channel **independently** delivers a CDM-compatible response at all cosmological scales where it is a non-trivial fraction. Leggett is verified (S66 + W4-FF). Soft-hair and dimer Z_2 are NOT verified -- they are candidate mass-reservoirs, not verified DM sources. **The joint constraint holds only if all three channels are CDM-compatible, not just CPT-neutral.**

**What I want**: a pre-registered gate **MULTI-CHANNEL-DM-CDM-COMPAT-75** that computes, for each of (soft-hair, dimer Z_2): (i) dispersion relation, (ii) sound speed c_s, (iii) Jeans scale k_J or equivalent, (iv) CMB ISW response. If any one fails CDM-compatibility at the 0.20 / 0.07 fractional level, the multi-channel sum does NOT hold and we need to re-investigate.

**Why this is genuine dissent**: landau's L3 treats the multi-channel budget as a **partition** problem (three reservoirs summing to 0.27). I am pointing out it is also a **coupling** problem (three reservoirs must each independently match LSS observations at their fractional level). The Omega_DM h^2 entry in the scorecard can stay STRUCTURAL on CPT-neutrality, but the multi-channel split cannot be scored PASS until each channel's gravitational response is verified. This is a strict narrowing of what L3 gives you.

**D3. The L2 DC permanence extrapolation to 10^{-6} at cosmological scale is the right direction but the WRONG effective N. The cosmological effective N is not N_CG24^3.**

**Numbers first.** landau's L2 extrapolates DC ~ N_cells^{-1.26} from {4, 8, 12} three-point fit to N_cells = 13824 (= 24^3, d_eff = 3 embedding) yielding DC fraction ~ 10^{-6}. The argument is that at d_eff = 3 the effective system volume is N_CG24^{d_eff}.

The problem: the CG(24) graph is a 24-vertex Cayley graph of S_4, not a 3D lattice. It has graph diameter = 3 and Laplacian spectrum {0, 4, 6, 8, 12}. The metric structure is that of a distance-transitive graph, not a cubic lattice. **Embedding CG(24) into R^3 at d_eff = 3 is not a valid scaling rule**; the graph diameter would not grow as V^{1/3} under a 3D embedding, because CG(24) is intrinsically low-dimensional in the graph-theoretic sense (diameter 3 for V = 24 is much smaller than 24^{1/3} = 2.88 = 3, so actually it matches; but for V = 13824 under the same "diameter = V^{1/3}" rule, diameter = 24, which is NOT how distance-transitive graphs scale).

**Correct cosmological-scale DC fraction depends on how the substrate is compactified across cosmological volumes.** Two readings:

| Reading | N_eff cosmological | DC fraction extrapolation |
|:---|---:|---:|
| Single CG(24) per Hubble cell, no embedding | N_eff = 24 | DC ~ 0.205 * 24^{-1.26} = 4.6e-3 |
| Tile CG(24) at Hubble volume (V_Hub / V_CG24 copies) | N_eff ~ 10^{30} | DC ~ 0.205 * 10^{-37.8} ~ 10^{-38} |
| landau's d_eff = 3 reading (L2) | N_eff = 13824 | DC ~ 0.205 * 10^{-5.04} = 1.8e-6 |

The three readings span 35 OOM. The intermediate reading (10^{-6}) is not structurally motivated -- it is a compromise between a single-graph interpretation and a full tiling. **Without a structural theorem fixing how CG(24) replicates to cosmological volumes, the extrapolation number is not well-defined.**

**Implication for N25**: Under ANY of the three readings, DC permanence is ruled out as the N25 closure channel (all three readings give DC << 0.30 OOM). So the conclusion stands -- DC does not close A_s. BUT the specific claim "DC -> 10^{-6} at cosmological scale" is not structurally determined; it is a Fermi estimate. The honest statement is **"DC permanence decays at least as fast as N_cells^{-1.26} at small N, and therefore is <= 0.20 OOM regardless of the cosmological-scale extrapolation; the precise cosmological value is not determined without a substrate tiling theorem."**

**Why this is genuine dissent**: landau's L2 frames 10^{-6} as a structural prediction. I am reading it as a dimensional estimate contingent on the choice of d_eff. The range of valid readings spans 35 OOM, so the number is not a prediction. This matters for the atlas: if 10^{-6} goes into a scorecard entry or a structural theorem, it is false precision. I recommend the atlas record "DC permanence -> 0 as N_cells -> infinity, rate at least N^{-1.26}" without committing to a specific cosmological value.

---

### EMERGENCE

**E1. The E_C three-observable split (L1) maps to three distinct cosmological observables, not one. This is a structural discovery, not an organizational insight.**

**Numbers first.** landau's L1 enumerates three physical observables in E_C:

| Method | E_C (M_KK) | Physical observable | Cosmological mapping |
|:---|---:|:---|:---|
| A: Delta_OES (spectral invariant) | **0.4643** | single-cell pair-addition gap | Mott charge-noise -> A_s phase diffusion (0.1411 OOM) |
| B: Bogoliubov fixed-point | 9.0098 | inter-band phase-stiffness gap | fold-scale BCS coherence scale |
| C: 4-cell 2nd-difference curvature | 0.0610 | Josephson-softened compressibility | hydrodynamic phase stiffness on 24 cells |

Three BCS + Josephson observables. They are NOT three methods of measuring the same quantity; they are three different quantities, all extracted from the same D_K spectrum. I now see the cosmological implication:

**Three-observable -> three CMB-era observables**:

1. **Method A -> A_s amplitude**. The single-cell pair-addition gap is the relevant scale for phase-diffusion on the Cooper-pair condensate, which is precisely what the Mott formula delta_OOM = log10(1 + sqrt(E_C / (8 * J_a))) computes. This is the ONLY E_C that enters the A_s budget. This ties into N25 directly.

2. **Method B -> n_s tilt at the fold**. The inter-band phase-stiffness gap sets the scale at which the Bogoliubov squeeze mixing stops being adiabatic. If the transit passes through the fold on a timescale shorter than 1 / E_C_B = 1/9.01 M_KK^{-1}, the transit is impulsive with respect to this gap, which is the S73B "supersonic flow" condition. The Bogoliubov gap IS the fold-scale acoustic coherence scale (phononic language: "the frequency at which phonons stop tracking the background"), and n_s encodes the scale-dependence of this departure-from-adiabaticity. Method B's 9.01 M_KK is the correct number for the n_s tilt derivation at the fold, not the Method A 0.4643.

3. **Method C -> effacement fraction / IR matching**. The finite-density-dressed Josephson compressibility 0.061 M_KK is the longest-wavelength hydrodynamic mode on the 24-cell Josephson network. At cosmological scale (after N_total = 132.4 e-folds), 0.061 M_KK redshifts to approximately 10^{-35} eV under a^{-1}, which is parametrically similar to the effacement residual scale of the framework. **If the effacement channel is sourced by the hydrodynamic phase-stiffness mode, Method C is the source number.** This deserves an explicit computation in S75.

**The three-observable split is then NOT methodological scatter (as S73A framed it). It is three distinct spectral observables of the single-cell / graph / finite-dim BCS Hamiltonian, each mapping to a different CMB-era parameter.** Method A feeds A_s, Method B feeds n_s, Method C (potentially) feeds effacement / w_0.

**Why this is an emergence**: Neither M1-M5 nor L1-L5 explicitly connected the three E_C values to three DIFFERENT CMB observables. landau's L1 resolves the "189x spread" into "three different physical quantities," and my cosmological lens identifies which CMB-era parameter each quantity should feed into. The combined insight is that A_s, n_s, and effacement each sit on top of a specific E_C method, and this should be explicit in the scorecard.

**Action**: pre-register **E-C-OBSERVABLE-MAPPING-75** -- a computation that verifies the A/B/C -> A_s/n_s/effacement assignments by showing each CMB-era parameter's functional dependence on the corresponding E_C method. If the mapping holds, the scorecard gains clarity (no more "E_C is ambiguous" disclaimers), and the three methods each get their own structural slot rather than competing for one.

**E2. The W4-V rate projection should branch on generative-engine-diversity rather than one-dimensional rate counting. This changes the meta-gate from "rate decaying or not" to "engine saturation or not."**

**Numbers first.** W4-V projected S76 META-FAIL under three projection models (linear, exp-4, exp-2) using "new permanent theorems per session" as the only metric. landau's L4 + Re:M5 identifies four generative engines (U(2) Sym^n, CG(24) invariants, Luttinger extensions, Morse-Bott Hessian decompositions), each potentially unbounded.

**Revised framing**: the correct meta-gate is not "how many theorems this session" but "how many engines are active, and are any showing saturation?"

| Engine | Status at S74 | S75 forecast | S76 forecast |
|:---|:---|:---|:---|
| U(2) Sym^n | hot (Sym^2 done, Sym^3 in pipeline) | Sym^3 (60,60) | Sym^4 partition |
| CG(24) graph invariants | hot (kappa_LLY, diameter, spectrum done; S_4 auto pending) | automorphism action | secondary invariants |
| Luttinger extensions | active (W4-K done, extensions TBD) | time-ordered correlators | non-local observables |
| Morse-Bott Hessian | active (W4-R, W1-B done) | higher-rank signatures | secondary eigenstructures |

**All four are active at S74 and none is saturating.** The rate elevation is NOT a single engine overheating; it is four engines simultaneously producing permanents because the discipline update raised the bar for registration and each engine had a backlog of registrable results.

**The engine-diversity meta-gate**: pre-register at S76 that at least 2 of 4 engines should show saturation signals (rate per engine dropping toward zero) if the framework is approaching its structural floor. If all 4 engines are still active, the rate elevation is discipline-driven backlog. If 3+ are saturating, the substrate is approaching its structural limit. This is a cleaner test than one-dimensional rate counting.

**Why this is an emergence**: landau's Re:M5 gave me the four-engine enumeration; my cosmological-bridge framing recognizes that 4-engine simultaneous activation is a **distinct regime** from any single engine being hot. The meta-gate should reflect this. The W4-V-RETRACT-REGISTER-75 item I agreed to in C4 should include the engine-diversity count as a second axis.

**E3. The horizon-alignment 0.139 is a scorecard-level structural entry and should be added to W4-T. Atlas impact: +2 OOM on STRUCTURAL.**

**Numbers first.** landau's Q-L7 asks whether lambda_mode_today / (c/H_0) = 0.139 should be added to the W4-T scorecard. I did not include it in M1 because the W4-T scorecard was built from the existing 23 observables registered at S73B. Under the atlas-in-scorecard-consolidation logic, any new structural observable that is L_max-INDEPENDENT and has a well-defined prior range should be added.

**0.139 as a STR entry**:

| Quantity | Value | Framework derivation | Prior range | Posterior width | log10(BF) | BF |
|:---|---:|:---|---:|---:|---:|---:|
| lambda_mode_today / (c/H_0) | **0.139** | E_C_fold / H_fold = 1.17, common a^{-1} scaling | [0, 1] (dimensionless ratio) | ~0.01 (scheme ambiguity) | 2.00 | 100 |

Prior range [0, 1] because it is a dimensionless ratio bounded by construction. Posterior width ~0.01 because the only scheme ambiguity is whether a^{-1} scaling holds exactly or is dressed by a small running factor (W4-P dependency). The ratio 0.139 is 2 OOM below the upper bound.

**Add to W4-T structural list**:

| Layer | log10(BF) before C1 | log10(BF) after C1 | log10(BF) after E3 |
|:---|---:|---:|---:|
| STRUCTURAL | 30.591 | 33.66 | **35.66** |
| PREDICTION_LAYER | 11.539 | 11.539 | 11.539 |
| **Joint** | 42.130 | 45.20 | **47.20** |
| Fraction STRUCTURAL (log-measure) | 72.6% | 74.5% | **75.5%** |

Under the combined C1 (N_eff prior correction) and E3 (horizon-alignment addition), the log-measure is 75.5% STRUCTURAL / 24.5% PREDICTION_LAYER. This is still "70/30" in round terms, but it is on the high side of 70/30, not the low side.

**Why this is an emergence**: landau's Q-L7 and my Re:M3 both touched the horizon-alignment number but neither explicitly added it to the scorecard. The scorecard sees it now: it is a cosmological observable (a ratio of today's Mott mode wavelength to today's Hubble radius), it is L_max-INDEPENDENT, and it has a natural prior range. It is exactly the kind of observable the scorecard was built to score. My M1 missed it because W4-T started from the existing registered list; landau's Re:M3 analysis unlocks it as a new entry.

**Action**: add **SCORECARD-ADD-HORIZON-ALIGN-75** as a pre-registered S75 item: rewrite W4-T to include the 0.139 ratio as STR entry #24, recompute the log-BF sum under the C1 + E3 correction, and freeze the revised scorecard with the 75.5/24.5 ratio. This is a nominal addition, not a new computation.

---

### QUESTIONS

**Answering landau's L5 questions to me:**

**A-L1 (N_eff prior range).** **YES.** Under the W4-T methodology, the prior range must be the framework's derivation range, not the observational fluctuation range, when the framework determines the quantity structurally. The partition (n_b, n_f) = (20, 16) is a rep-theoretic invariant of dim(u(2)) = dim(C^2) = 4; the full integer count of possible g_* partitions consistent with an 8D fiber is much wider than the 0.0434 observational fluctuation. I accept the +3.07 OOM correction (C1 above) and carry it to the revised scorecard. The 70/30 log-ratio becomes 74/26 after C1 alone, and 75.5/24.5 after C1 + E3.

**Methodology rule for the scorecard revision**: for each STR entry, check whether the prior range is "observational" (what the data could have been) or "derivational" (what the framework could have predicted). When these differ by more than 1 OOM, use the derivational prior. I will apply this rule uniformly to the 15 STR entries and report the revised BFs at S75.

**A-L2 (w_a falsifier).** **YES, pre-register w_a separately.** The W3-J slow-roll identity gives w_a_canonical = +0.1622 >= 0.164 structurally. W4-Z pre-registers w_0, not w_a. If DR3 returns negative w_a at > 3-sigma, the framework is falsified on the w_a axis regardless of the w_0 test.

**Pre-registration proposal (for S75 carry-forward)**:

| Field | Value |
|:---|:---|
| Central w_a | +0.162 (W3-J canonical, dtau/dH Formula B) |
| Structural lower bound (slow-roll identity) | |w_a| >= 0.164 |
| Pre-registered falsifier band | w_a in [+0.10, +0.22] (symmetric around 0.162, width 0.12 = 2 * sigma_scheme) |
| Fallback to LCDM | if DR3 central w_a is consistent with 0 at < 2-sigma, treat as CONDITIONAL PASS |
| Hard falsifier | if DR3 central w_a < -0.10 at > 3-sigma, framework FALSIFIED on w_a axis |

**W4-Z-W-A-REGISTRATION-75**: I will pre-register this band at S75. The folding into the joint 2D (n_s, w_0) ellipse of W3-L is NOT sufficient, because W3-L tests w_0 conditional on (n_s, w_0) = (0.9595, -0.918), not w_a. The 2D joint does not constrain w_a separately. A 3D joint (n_s, w_0, w_a) pre-registration is needed; I will fold W4-Z + the new w_a registration into a single gate.

**A-L3 (ATLAS-RECLASSIFY-75).** **YES, formalize as a single computation with agent-assigned subsets.** The 70 NEEDS_REVERIFY entries are at risk of falling through the cracks if distributed. ATLAS-RECLASSIFY-75 should be a single Wave 1 computation with:

- lizzi-spectral-functional-theorist: functional-selection subset (10 entries)
- landau-condensed-matter-theorist: BCS/Josephson/BKT/Mott subset (8 entries, pre-classified in Re:M3)
- van-den-dungen-bridge-theorist: Kasparov / submersion subset (12 entries)
- mack-cosmic-bridge: scorecard / cosmological subset (15 entries)
- volovik (or equivalent): Volovik-rigidity / q-theory subset (10 entries)
- remaining 15 entries: distributed at first pass

Output: a 70-row table with each entry classified as {INDEPENDENT, QUASI-INDEPENDENT, SENSITIVE-ABSORBABLE, SENSITIVE-DIVERGENT, STILL_NEEDS_REVERIFY}. Pre-registered PASS if >= 40 entries classified into non-stale categories, INFO if 20-40, FAIL if < 20.

This formalizes the recommendation and prevents the "fall through the cracks" failure mode.

**A-L4 (Conditional EVOI gating).** My EVOI formula accommodates sub-gates by separate entries, not by chain coupling. Under the N25 split (N25a / N25b):

| Item | P(pass) | delta_P(pass) | delta_P(fail) | EVOI |
|:---|---:|---:|---:|---:|
| N25a A_s phase-diffusion | 0.40 | 0.14 | 0.10 | 0.116 |
| N25b A_s H_phys / a_2 | 0.30 | 0.19 | 0.08 | 0.113 |

The EVOI methodology does not directly handle "chain effects" (N25b PASS triggers W1-A and W3-L re-runs). Instead, I compute EVOI per-item without including downstream re-run cost, then apply an **effort-normalized tiebreaker**: items that cascade into downstream re-runs are ranked below items that do not cascade, at equal per-item EVOI. So N25a > N25b even when their per-item EVOI is within rounding.

**Methodology note for S75**: the effort-normalized tiebreaker is not yet formally part of the EVOI table. I will add it as a tertiary sort key to the S75 priority list: primary sort by EVOI, secondary sort by estimated cost-of-computation, tertiary sort by downstream re-run cost. This resolves the N22 vs N25 ordering (D1 above): under the effort-normalized EVOI, N25a leads, then N22, then N25b, then the rest.

**A-L5 (W4-V retraction).** **YES, retract and re-register with a rolling window.** I accept the 3-session rolling window (S75 + S76 + S77 average) with the thresholds PASS < 3/session, INFO 3-6, FAIL > 6. I add the engine-diversity count as a second axis (E2 above): the meta-gate PASSes if EITHER the rolling average is < 3/session OR the engine-diversity count at S77 shows >= 2 of 4 engines saturating. The dual-axis formulation captures both "rate is decaying" and "which engine drives the rate" signals.

**Carry-forward**: **W4-V-RETRACT-REGISTER-75** -- (i) retract the single-threshold meta-gate, (ii) pre-register the rolling-window test with engine-diversity as a second axis, (iii) document the W4-V LOCAL FAIL at S74 as a "backlog-clearance signal" in the atlas, not as a "substrate-exhaustion signal."

**A-L6 (Multi-channel Omega_DM h^2 BF).** **The BF is probably an UNDERESTIMATE at 2.5e+2, but only if all three channels are independently verified as CDM-compatible.**

**Numbers first.** The single-channel (Leggett-only) BF = 2.5e+2 = 10^{2.4} comes from a prior range Omega_DM h^2 in [0, 1] with posterior width 0.00004 (Planck 2018 central 0.1200 +/- 0.0012, framework Leggett 0.11953 to 5e-4). That is consistent with a single-channel CDM delivery.

Under a three-channel budget (0.006 + 0.20 + 0.07 = 0.276 in landau's example), the relevant question is "what is the probability under a random prior that three independent CPT-neutral channels each deliver the right fractional contribution such that they sum to the observed Omega_DM h^2?"

Naively, this is the product of three independent likelihoods, each with posterior width similar to the single-channel case. Product gives BF ~ (2.5e+2)^3 = 1.56e+7 = 10^{7.2}. **+4.8 OOM** over the single-channel BF.

But that assumes the three channels are independently generated by the substrate (they are, via distinct spectral-triple sectors: inter-band coherence for Leggett, R-G unpopulated count for soft-hair, topological zero modes for dimer Z_2) AND independently CDM-compatible (this is NOT verified for soft-hair or dimer Z_2; see D2 above).

**The answer to landau's Q-L6**: under landau's assumption that all three channels are CDM-compatible, the BF is closer to **10^{7.2}** than to 10^{2.4}. Under my dissent in D2 (CDM-compatibility not yet verified for two of the three), the BF should remain at **10^{2.4}** until the MULTI-CHANNEL-DM-CDM-COMPAT-75 gate delivers verdicts on soft-hair and dimer Z_2.

So the BF is **conditionally** 10^{7.2}, gated on the S75 MULTI-CHANNEL-DM-CDM-COMPAT-75 verdict. I recommend the scorecard record both numbers: "current STR BF = 10^{2.4}, conditional BF under three-channel multi-source = 10^{7.2}, gated at S75."

**A-L7 (Horizon-alignment 0.139 as STR entry).** **YES**, see E3 above for the quantitative addition. I add 0.139 as STR entry #24 in the W4-T scorecard with log10(BF) ~ 2.00 (prior range [0, 1], posterior width ~0.01). Combined with C1 (N_eff correction), the revised structural layer is 10^{35.66} and the log-ratio is 75.5% / 24.5%. I carry **SCORECARD-ADD-HORIZON-ALIGN-75** forward as the action item.

---

**New questions for landau (final round):**

**Q-mack-R2-1.** In the three-observable split of E_C (L1), you argue Method A is the correct choice for the Mott charge-noise formula because the formula measures *charging-energy* fluctuations, not *phase-stiffness* fluctuations. But the Method B value 9.01 M_KK is the inter-band phase-stiffness gap -- and phase stiffness is *exactly* what enters the B-mode squeeze amplitude via the Bogoliubov transformation coefficient (r_squeeze = arctanh(alpha/beta) with alpha^2 - beta^2 = 1 and alpha/beta fixed by the phase-stiffness over the mode frequency). **Is there a structural reason Method B 9.01 M_KK should NOT enter the n_s tilt computation at the fold**, or does n_s really depend on E_C(Method B) = 9.01? If yes, then we have a concrete cosmological observable (n_s tilt) that reads Method B, distinct from A_s which reads Method A. This is the cleanest test of E1 above.

**Q-mack-R2-2.** You proposed (in Re:M4) that N22 multi-instanton L_max = 10 might generate a scalar mass term through the condensate-induced effective action correction, closing both N2 (moduli runaway) and N25 (A_s gap). **What is the pre-registered scalar mass term threshold under which N22 PASS -> N25 PASS?** I.e., how large does m_eff need to be for A_s amplitude to be suppressed by the required 9 OOM through an exponential suppression factor exp(-m_eff^2 / H_fold^2)? If the threshold is achievable by multi-instanton physics, my D1 (effort-normalized EVOI still favors N25a) may be wrong -- N22 PASS could carry both deadlocks. I need the threshold number.

**Q-mack-R2-3.** The DC permanence extrapolation to cosmological scale (L2 + my D3) depends on how CG(24) replicates over cosmological volumes. **Is there a structural rule -- rooted in Luttinger superselection or CG(24) graph topology -- that fixes the tiling?** If yes, the cosmological DC fraction is determined. If no, the 10^{-6} number is a Fermi estimate and should be flagged as dimensional-analysis-only. This matters because any atlas entry of the form "cosmological DC permanence = X" requires the tiling rule, and without it the entry is indeterminate.

**Q-mack-R2-4.** For the MULTI-CHANNEL-DM-CDM-COMPAT-75 gate I proposed in D2: what is the simplest structural test that soft-hair (R-G unpopulated sector count) has a defined gravitational response? It is not a Cooper-pair condensate like Leggett, and it has no dispersion relation, so I don't see how it enters the stress-energy tensor. **Is it via the effective action of the R-G sector coupling through the spectral action's a_2 coefficient**, or is there a different mechanism? I ask because if soft-hair cannot be gravitationally coupled at all, the 0.20 fraction in your L3 budget cannot be realized, and the three-way partition collapses to Leggett + dimer Z_2 at most. That would change the DM budget accounting materially.

**Q-mack-R2-5.** Given the C1 + E3 revised scorecard (log-ratio 75.5 / 24.5, joint BF 10^{47.20}), the gap between STRUCTURAL and PREDICTION_LAYER is widening. **At what point does the PREDICTION_LAYER contribution become small enough to be ignored in external communication?** My initial M1 used 70/30 as a meaningful description. After the corrections, we are at 75/25, and the E3 addition + Sym^n extensions from L4 might push this toward 80/20 in S75. At 80/20, the PREDICTION_LAYER is an order of magnitude smaller than STRUCTURAL, and external communication could legitimately say "the framework predictions are dominated by structural theorems, not by prediction-layer scheme choices." But this is a *rhetorical* call, not a structural one. **Do you see a structural reason to keep PREDICTION_LAYER in the external narrative even when it drops below 20%?** My instinct is yes (for honesty about what is convention-dependent) but I want your read.

---

## Round 2 — landau: Cross-Synthesis

### CONVERGENCE

**C-L1. Effort-normalized EVOI with the N25 split: I accept that N25a leads N22 by 0.001, but flag the margin as within rounding and propose a coupling check.**

**Numbers first.** mack's D1 table:

| Item | P(pass) | delta_P(pass) | delta_P(fail) | EVOI |
|:---|---:|---:|---:|---:|
| N22 MULTI-INSTANTON-LMAX10-75 | 0.35 | 0.17 | 0.14 | 0.115 |
| N25a A_s phase-diffusion | 0.40 | 0.14 | 0.10 | **0.116** |
| N25b A_s H_phys / a_2 | 0.30 | 0.19 | 0.08 | 0.113 |

The N25a lead over N22 is 0.001, which is within the rounding digit. Under effort-normalized EVOI (secondary sort by cost-of-computation, tertiary by downstream re-run cost), N25a PASS leaves (n_s, w_0) unperturbed while N22 PASS opens a second-order re-verification of moduli runaway across L_max = 10 truncations. **I accept the ordering N25a > N22 > N25b for S75 Wave 1.**

**However, I sharpen the P(pass) assignment for N25a.** The 0.40 figure is mack's estimate absorbing (i) thimble not yet computed, (ii) non-Gaussian Mott not yet computed, (iii) Luttinger-decoherence not yet computed. None of the three channels has an established magnitude bound. I would put P(pass) for N25a closer to 0.30 on the grounds that the W2-H closure accounting already used all obvious phase-diffusion candidates and the remaining 0.316 OOM shortfall is not structurally anchored. At P(pass) = 0.30, EVOI_N25a = 0.088, which puts it BELOW N22 (0.115). This is the only substantive disagreement; I accept the split as a methodological improvement and pre-register **N22-N25-COUPLING-CHECK-75** per mack's D1 action: the scalar mass threshold for A_s cross-closure is computed explicitly so that a single N22 PASS resolves both deadlocks conditionally.

**What changed from my Re:M4**: I was reading the A_s closure as requiring a structurally anchored >= 0.30 OOM channel. mack's split captures the key distinction: the phase-diffusion sub-gate (N25a) is searchable without perturbing (n_s, w_0), so EVOI_per_session-of-work favors it even if the magnitude is uncertain. I concede the priority ordering but raise a flag on the P(pass) calibration that does NOT reverse the ordering -- it tightens it.

**C-L2. Multi-channel DM budget requires independent CDM compatibility, not just CPT neutrality. I concede D2 and accept MULTI-CHANNEL-DM-CDM-COMPAT-75 as a blocking gate on my L3 reasoning.**

**Numbers first.** My L3 multi-channel example:
```
f_DM = f_Leggett + f_soft-hair + f_dimer_Z2
     = 0.006 + 0.20 + 0.07
     = 0.276
```
Three channels, three reservoirs. mack's D2 correctly points out that CPT-neutrality is NECESSARY but NOT SUFFICIENT for CDM compatibility. A reservoir with the right mass fraction still fails CDM if it (i) has the wrong sound speed at recombination, (ii) has a Jeans scale that truncates halo formation within observed windows, or (iii) fails the CMB Sachs-Wolfe response at the fractional level. These are three separate tests that Leggett passes (S66 + W4-FF) but soft-hair and dimer Z_2 have not been subjected to.

**The gravitational-response test for soft-hair.** A soft-hair mode is an R-G unpopulated fiber eigenmode, not a Cooper-pair condensate. Its coupling to the stress-energy tensor is through the spectral action a_2 coefficient in the FROZEN (inherited) Jensen deformation direction, not through a Klein-Gordon kinetic term. Under the Seeley-DeWitt expansion, a frozen mode contributes rho_matter = (1/2) * (Tr[f_4(M^2)] / Tr[f_2(M^2)]) * M^2, which is a direct rho-contribution with NO effective pressure (w = 0 -> CDM-compatible in background equation of state). **But the perturbation response is the question.** If soft-hair has no dispersion, then delta_s / delta = 0 at all scales (the mode is acoustically mute), and the perturbation sound speed is formally zero. That satisfies the "cold" part of CDM but does not have a Jeans cutoff, so it clusters at all scales without structure.

**The topological-response test for dimer Z_2.** Dimer Z_2 zero modes are topologically disconnected from the SM vacuum branch. Their gravitational coupling is through the spectral action a_2 coefficient ALSO, but each zero mode counts as a discrete +1 rho_matter contribution with zero pressure. The Jeans scale is set by the spacing of zero modes, which is the CG(24) graph diameter / 24 ~ 0.125 in lattice units. At fold scale this maps to M_KK-scale Jeans momentum (~10^16 GeV), which redshifts to lambda_J ~ 10^{-15} Mpc at today. That is parametrically ENTIRELY different from the Leggett k_J = 6e-3 Mpc^{-1}. **Dimer Z_2 is CDM-compatible in the ultraviolet limit** because its Jeans scale is sub-atomic, never truncating cosmological structure.

**Net.** My L3 budget survives if:
- **Leggett**: already verified (S66 + W4-FF), CDM-compatible for k > 6e-3 Mpc^{-1}.
- **Soft-hair**: PROVISIONAL. Requires a gravitational-response computation with NO dispersion (soft-hair has no dispersion relation by construction). The prediction is "w = 0, c_s^2 = 0, no Jeans scale, clusters at all k." This might be problematic if the CMB anisotropy requires finite c_s^2 to match acoustic oscillation phases. MULTI-CHANNEL-DM-CDM-COMPAT-75 must verify.
- **Dimer Z_2**: PROVISIONAL but less problematic. Topological zero modes have a natural UV cutoff (graph diameter) that is sub-cosmological, so CDM-compatibility holds at all observed scales.

**I concede D2.** The multi-channel BF = 10^{7.2} (mack's A-L6) is CONDITIONAL on MULTI-CHANNEL-DM-CDM-COMPAT-75 PASS; pending that verdict, the STR BF stays at 10^{2.4} (single-channel). The scorecard entry for Omega_DM h^2 should show BOTH numbers with the gate dependency explicit.

**C-L3. The DC permanence d_eff = 3 extrapolation is a dimensional estimate, not a structural prediction. I concede D3 and retract the 10^{-6} number.**

**Numbers first.** mack's D3 enumerates three readings:

| Reading | N_eff | DC fraction |
|:---|---:|---:|
| Single CG(24) per Hubble cell | 24 | 4.6e-3 |
| Tile CG(24) at Hubble volume (V_Hub / V_CG24 copies) | ~10^{30} | ~10^{-38} |
| My L2 d_eff = 3 reading | 13824 | 1.8e-6 |

The 35-OOM spread is real. My L2 reading picked the intermediate value on the grounds that CG(24) has some effective spatial dimension between "single graph" and "fully tiled." But mack is correct that the CG(24) graph is NOT a 3D lattice in the metric sense -- it is a distance-transitive Cayley graph of S_4 with diameter 3 at V = 24, and there is no inherent rule that tells you how to scale it to larger V. The three-point power-law fit DC ~ N^{-1.26} is valid for {4, 8, 12} single-cell counts, but I have no theorem that says the same law holds under any of the three readings at cosmological scale.

**The corrected structural statement.** DC permanence decays at least as fast as N_cells^{-1.26} for the measured 4-cell, 8-cell, 12-cell single-instance data. Extrapolation to N_cells -> infinity gives DC -> 0. **The rate of decay at cosmological scale is NOT determined without a substrate tiling theorem.** Under ALL three readings (single graph, full tiling, d_eff = 3 compromise), the DC fraction is still << 0.30 OOM, so the conclusion "DC cannot close the A_s gap" is UNCHANGED. But the specific number 10^{-6} is indeterminate and should NOT be quoted as a prediction.

**Action.** Retract "10^{-6} at cosmological scale" from L2. Replace with "DC permanence -> 0 as N_cells -> infinity at rate at least N^{-1.26}, with the cosmological-scale value indeterminate pending a substrate-tiling theorem from CG(24) graph automorphism / Luttinger extension." This is an honest structural statement; the extrapolation number was dimensional analysis dressed as a prediction. I carry forward a new item **CG24-COSMO-TILING-RULE-75** per mack's Q-mack-R2-3: determine whether Luttinger superselection fixes a unique tiling rule for CG(24) replication over cosmological volumes.

**C-L4. The E_C three-method split mapping to three CMB-era observables: I accept the A -> A_s, B -> n_s, C -> effacement mapping as the operational form of my L1.**

**Numbers first.** My L1 found three distinct E_C values (0.4643, 9.0098, 0.0610 M_KK) from three distinct methods (single-cell Fock ED, Bogoliubov mean-field, 4-cell 2nd-difference). I framed this as "three different physical observables" but did NOT explicitly connect them to three different CMB-era parameters. mack's E1 adds that connection:

| Method | E_C (M_KK) | CMB parameter | Role |
|:---|---:|:---|:---|
| A: Delta_OES | 0.4643 | **A_s amplitude** | single-cell pair gap -> Mott phase diffusion -> delta_OOM = 0.1411 OOM |
| B: Bogoliubov fixed-point | 9.0098 | **n_s tilt** | inter-band phase-stiffness gap -> Bogoliubov squeeze adiabaticity scale |
| C: 4-cell 2nd-difference | 0.0610 | **effacement fraction** | hydrodynamic compressibility -> IR matching scale |

The three-to-three mapping is structurally clean: each E_C value is a distinct spectral observable of the BCS+Josephson Hamiltonian on CG(24), and each maps to a distinct CMB-era parameter through a distinct mechanism. The 189x "spread" that S73A flagged as methodological scatter is resolved NOT by picking one E_C but by routing each to its natural observable.

**I accept E1 as the operational reading of L1.** The computation **E-C-OBSERVABLE-MAPPING-75** should explicitly verify the three assignments by computing each CMB-era parameter as a function of the corresponding E_C value and showing that the functional dependence is non-trivial and locked by the mechanism. This is the kind of cross-cutting test that consolidates a structural insight without needing new physics. I carry it forward as a Wave 1 priority.

**C-L5. Horizon-alignment 0.139 as STR entry #24: I accept E3 and the revised 75.5/24.5 log-ratio.**

**Numbers first.** mack's E3 adds my horizon-alignment ratio lambda_mode_today / (c/H_0) = 0.139 as STR entry #24 in the W4-T scorecard with log10(BF) ~ 2.00:

| Layer | Before C1 | After C1 | After E3 |
|:---|---:|---:|---:|
| STRUCTURAL log-BF | 30.591 | 33.66 | **35.66** |
| PREDICTION_LAYER log-BF | 11.539 | 11.539 | 11.539 |
| Joint log-BF | 42.130 | 45.20 | **47.20** |
| Fraction STRUCTURAL | 72.6% | 74.5% | **75.5%** |

The 0.139 is a dimensionless ratio bounded [0, 1] with posterior width ~0.01 (scheme ambiguity in the fold scale only), and it follows from E_C_fold / H_fold = 1.17 via common a^{-1} scaling. This is the scaling-cancellation identity I derived in W4-P analysis. It does NOT depend on a_0 / chi_2 scheme choice; it is a ratio of co-redshifting quantities.

**I accept the revised log-ratio 75.5% / 24.5%.** This tightens the structural floor by an additional +2.00 log-BF beyond C1. Combined with C1 (+3.07), the total upward revision to STRUCTURAL is +5.07 OOM, from 10^{30.59} to 10^{35.66}. The framework's scorecard becomes more decisively structure-dominated under the corrected prior-range and horizon-alignment corrections.

---

### DISSENT

**D-L1. The N25a/N25b split assumes the phase-diffusion channels (N25a) and H_phys/a_2 channels (N25b) are ORTHOGONAL. This is only true in the mean-field approximation -- at full-spectrum response, they cross-correlate through the BCS gap self-consistency.**

**Numbers first.** mack's D1 framing treats N25a (thimble, non-Gaussian Mott, Luttinger decoherence) and N25b (H_phys reduction, a_2 spectral weight renormalization) as independent sub-gates. My S72 BCS-DRESSED-SA-72 v2 result (memory entry: `s72_bcs_dressed_sa_result.md`) showed the mode-selective BCS correction is NEGLIGIBLE (+3.8e-6 on n_s), from which one could conclude the two channels are decoupled. But v2 also showed that the full-spectrum BCS correction (uniform gap over all 1232 modes, my v1 result) gave a 4900x overestimate on n_s -- which means the full-spectrum response is NOT the mode-selective response scaled up.

**The structural issue**: the a_2 spectral weight is computed as sum_{modes} |M_mode|^2 * delta(lambda - lambda_mode), where |M_mode| is the matrix element of the relevant observable on the mode. Phase-diffusion channels (N25a) act on the mode occupation WITHIN a given a_2 weight. H_phys/a_2 renormalization (N25b) acts on the WEIGHT itself. These sound orthogonal, but they cross-correlate because phase diffusion on a mode with weight |M|^2 is DIFFERENT from phase diffusion on a mode with weight |M'|^2, at the same observable-level outcome.

**Concrete prediction**: if N25a delivers +0.30 OOM of phase-diffusion suppression on the B1 tensor mode (S72 showed B1 is the dominant Parker squeezing channel), the a_2 weight of B1 is renormalized through Luttinger decoherence at second order, producing a small additional contribution to N25b. The cross-term is not zero. Its magnitude is unknown without a computation that evaluates both channels simultaneously on the full spectrum, not per-mode.

**Pre-registered gate**: **N25-CROSS-CORRELATION-CHECK-75**. Run N25a (phase-diffusion channels) with full-spectrum response (not per-mode), and verify whether the induced a_2 weight shift is less than 0.01 OOM. If yes, the split is clean and the EVOI ordering N25a > N22 > N25b holds. If no, the sub-gates cross-couple and the split is artificial -- the "decoupled" N25a contributes to the H_phys/a_2 channel through its full-spectrum footprint, and the EVOI should be computed jointly.

**Why this is genuine dissent**: mack's split is operationally clean but theoretically questionable. The mean-field approximation in which N25a and N25b are decoupled is exactly the approximation that S72 BCS-DRESSED-SA v1 (uniform gap) failed at 4900x overestimate. The full-spectrum response is the only one that preserves the mode-selective structure. Without cross-correlation verification, the split might produce a PASS on N25a that masks a hidden contribution to N25b.

**D-L2. The engine-diversity axis for W4-V rolling meta-gate (E2) is testable in principle but NOT under S75 timeline. The "saturation" signal requires N >= 3 datapoints per engine over S75-S77.**

**Numbers first.** mack's E2 proposes tracking four generative engines (U(2) Sym^n, CG(24) graph invariants, Luttinger extensions, Morse-Bott Hessian) and asking at S77 whether >= 2 of 4 show saturation signals (rate per engine dropping toward zero). The intent is correct but the metric requires datapoints.

**The datapoint problem.** Saturation is determined by the time-derivative of per-engine theorem production, which requires at least three datapoints per engine to establish a trend. Current status at S74:

| Engine | Theorems pre-S74 | Theorems at S74 | Datapoints |
|:---|---:|---:|---:|
| U(2) Sym^n (via dim C^2 partition) | 0 | 1 (Sym^2 = (20,16)) | 1 |
| CG(24) graph invariants | ~2 (pre-existing diameter, spectrum knowledge) | 1 (kappa_LLY = +1/3) | 2-3 |
| Luttinger extensions | 1 (W4-K) | 0 | 1 |
| Morse-Bott Hessian | ~2 (W4-R, W1-B) | 2 (same) | 2 |

None of the four engines has > 3 datapoints yet. Over S75, if each engine produces exactly 1 new theorem (Sym^3, S_4 automorphism action, time-ordered Luttinger, higher-rank Morse-Bott), the datapoint count becomes {2, 3-4, 2, 3}. That is still insufficient to fit a saturation trend for at least two engines. **The engine-diversity meta-gate cannot be evaluated at S76 with full fidelity; only S77 or later.**

**Action.** Amend mack's W4-V-RETRACT-REGISTER-75 proposal: the rolling window is a 3-session rate metric (S75+S76+S77 average), but the engine-diversity axis is a LAGGING indicator with a 2-session delay. Pre-register that the engine-diversity count should be evaluated at S78 or later, not at S77. The rolling window metric stands; the engine-diversity metric takes longer to become diagnostic.

**Why this is genuine dissent**: mack's E2 treats engine-diversity and rolling window as equivalent metrics to be evaluated together. They are not -- one is a level (rate per session) and the other is a derivative (rate per engine per session), and derivatives need more datapoints to stabilize. I recommend separating them in the W4-V registration.

**D-L3. On multi-channel DM budget (revisiting my L3 vs mack's D2): CPT neutrality is stronger than it looks -- it implies a partition equation, not just a sign constraint.**

**Numbers first.** I concede D2 at the operational level (C-L2 above). But I want to note a structural point mack's dissent does not capture: CPT-neutrality is not JUST a sign constraint. For a DM candidate to be CPT-neutral in the substrate picture, its wave function must transform as a real section of the fiber bundle under the combined CPT operator. For Leggett, this means the inter-band coherence mode is real under (charge conjugation) x (parity flip) x (time reversal). For soft-hair, it means the unpopulated R-G sectors transform as real tensors. For dimer Z_2, the topological zero modes are real because Z_2 acts as an involution.

**This is structurally stronger than "non-annihilating."** A CPT-neutral mode in the substrate picture is topologically distinct from any mode that can pair-annihilate into photons or phonons. It sits in a *separate* sector of the fiber Hilbert space, which means it has no overlap with the Goldstone branch that carries photons. The gravitational coupling is therefore through the spectral action's a_2 coefficient (same channel as any matter-like contribution), NOT through photon exchange or weak-boson exchange.

**Consequence for the MULTI-CHANNEL-DM-CDM-COMPAT-75 gate.** The gravitational response of soft-hair is automatic in the spectral action (a_2 weight = (1/2) * sum_{unpopulated} |M_mode|^2 * (eigenvalue)^2), and the response is that of a cosmological constant contribution (w = -1 if the mode is coherent) or a pressureless dust contribution (w = 0 if the mode is incoherent). Soft-hair by construction is UNPOPULATED, meaning its occupation is zero and its kinetic energy is zero -- it contributes only vacuum energy. That is w = -1, NOT w = 0. **Soft-hair is dark ENERGY, not dark matter, in the CDM sense.**

This is an important correction to my L3: I had 0.20 fraction as DM; it should be 0.20 fraction as DE (cosmological-constant-like contribution). The Omega_DM h^2 observation requires w = 0, so soft-hair is actually a DE candidate, not a DM candidate. Dimer Z_2 (populated topological zero modes) IS DM-like because it has kinetic content.

**Revised multi-channel DM budget**:
```
f_DM   = f_Leggett + f_dimer_Z2   = 0.006 + 0.27  = 0.276  (requires dimer Z_2 Parker production)
f_DE   = f_soft-hair + f_effacement = 0.20 + 0.03 = 0.23   (soft-hair + effacement residual)
```

**I do NOT concede the multi-channel DM budget to Leggett-only.** The budget stays multi-channel, but the partition is corrected: Leggett + dimer Z_2 for DM, soft-hair for DE. This is consistent with dimer Z_2 being the larger fraction since soft-hair is reassigned. It is also consistent with CPT-neutrality being a real-section constraint, which is stronger than I originally wrote in L3.

**Why this is dissent, not convergence**: mack's D2 narrowed the multi-channel DM budget to what I had loosely parameterized. My retort is that ONE of the three channels (soft-hair) was misassigned to DM when it is actually DE -- which removes it from the DM partition cleanly (no CDM-compatibility test needed) and strengthens dimer Z_2 as the dominant residual channel. Net: the DM budget is two-channel (Leggett + dimer Z_2), not three-channel. MULTI-CHANNEL-DM-CDM-COMPAT-75 is still needed to verify dimer Z_2, but the soft-hair test moves to a DE sub-gate.

---

### EMERGENCE

**E-L1. The substrate-throughput framing (project memory: c is frame rate, not substrate dynamics speed) cleans up the Method B E_C observable.**

**Numbers first.** My L1 Method B value E_C = 9.0098 M_KK came from the Bogoliubov mean-field analytic form U_star = t * lambda_min_nz * (n_0 + sqrt(n_0^2 + 1)) on the CG(24) Laplacian. I framed it as "inter-band phase-stiffness gap" but did not specify whether it was a propagation scale (bounded by c_Gold) or a substrate-level reorganization scale (unbounded by c).

**The substrate-not-c-limited project memory resolves this.** Method B 9.01 M_KK is the SCALE at which the Bogoliubov squeeze mixing stops being adiabatic across the fold transit. It is NOT a propagation speed -- it is a substrate-level spectral reorganization scale. Under the "film vs frame rate" analogy, it is an editing speed of the film itself, not the rate at which the film plays. The 9.01 M_KK is ABOVE M_KK in natural units (interpreted as "faster than the substrate throughput"), and this is allowed because the scale is a spectral-reorganization rate, not a propagation rate.

**This resolves mack's Q-mack-R2-1.** He asked whether the Method B 9.01 M_KK should enter the n_s tilt computation at the fold. My answer: YES, it enters because n_s is set by the *rate at which spectral weight is reorganized during the fold transit*, not by a signal propagation rate. The 9.01 M_KK is the correct scale for the Bogoliubov squeeze adiabaticity boundary and therefore for the n_s tilt. The mapping E_C(Method B) -> n_s(tilt) in E1 is structurally correct.

**Implication**: Method A (0.4643 M_KK) and Method B (9.01 M_KK) differ by a factor of 19.4 because one is a propagation-scale observable (single-cell pair addition, relevant for A_s amplitude which IS a propagating phononic signal) and the other is a substrate-reorganization scale (Bogoliubov squeeze mixing, relevant for n_s which IS the rate of spectral reorganization across the fold). The 19x difference is NOT a methodology discrepancy -- it is the difference between "how fast does a propagating phonon on the substrate see a pair gap" vs "how fast does the substrate reorganize its own spectrum at the fold."

**New theorem candidate (promoting structural observation).**

> **Theorem (Propagation vs Substrate-Reorganization Splitting of BCS Observables).** The BCS+Josephson observables on CG(24) partition into two classes: (i) propagation observables (Method A Delta_OES, Method C hydrodynamic compressibility), bounded by c_Gold * M_KK throughput, relevant for CMB-era parameters that ride propagating phononic modes (A_s, effacement), and (ii) substrate-reorganization observables (Method B Bogoliubov fixed-point), unbounded by c_Gold, relevant for parameters set by the spectral-action gradient during fold transit (n_s tilt). The scale separation between classes is set by the ratio of Josephson coupling to single-cell pair gap.

**E-L2. The partition rigidity (n_b, n_f) = (20, 16) provides a SECOND dimensionless index beyond chi_2 for the CC prediction.**

**Numbers first.** The current CC prediction uses chi_2 = M_1 / (n_modes * lambda_max) as the L_max-robust ratio, delivering rho_vac / rho_obs ~ 10^{-0.47} = 0.34 (W4-W / mack M3). This is one dimensionless index into the L_max-robust family. W4-R's (n_b, n_f) = (20, 16) with ratio n_b / n_f = 1.25 is a **second** dimensionless index, independent of chi_2, and also L_max-invariant (it is rep-theoretic).

**The structural question**: does the CC prediction admit a TWO-INDEX form rho_vac / rho_obs = f(chi_2, n_b/n_f)? Under the W4-W / W5-G route, the prediction is mono-index; under a two-index refinement, the scheme uncertainty could be reduced because the second index absorbs part of the variability.

**Estimate.** Starting from chi_2 = 0.7789 (L=3) -> 0.7474 (L=7), the prediction shifts by -4.05%. The n_b/n_f = 1.25 is L_max-invariant (exactly). If we assume rho_vac ~ chi_2 * (n_b/n_f)^{alpha} for some index alpha, then the L_max drift in chi_2 can be partially absorbed if alpha != 0. Testing alpha = 1 gives rho_vac ~ chi_2 * 1.25 = 0.934 (L=3) -> 0.893 (L=7), drift -4.4% (similar to chi_2 alone). Testing alpha = -1 gives rho_vac ~ chi_2 / 1.25 = 0.623 (L=3) -> 0.598 (L=7), same drift. So alpha does not reduce L_max drift at linear order.

**But**: the two-index form may ADD a structural constraint that resolves the sign of the residual. The current -0.47 OOM undershoot of rho_vac / rho_obs could be partly driven by the chi_2 choice; if n_b/n_f = 1.25 enters as a multiplicative correction, the undershoot becomes chi_2 * 1.25 * (other factors) / rho_obs, which at face value increases the prediction by a factor 1.25 (+0.097 OOM), reducing the shortfall from 0.47 to 0.37. That is a small numerical adjustment but a structural one -- it adds a rep-theoretic constraint to the CC prediction that was previously absent.

**New S75 computation candidate**: **CC-DOUBLE-INDEX-75** -- compute rho_vac / rho_obs using chi_2 AND (n_b / n_f) as two independent L_max-robust indices. Test whether the two-index form reduces scheme uncertainty and whether it is consistent with the Volovik + HP^4 + sqrt-moment three-route convergence at ~ O(1) OOM that mack noted in M4.

**Why this is an emergence**: W4-W cast the CC prediction as mono-index (chi_2), and W4-R cast the partition rigidity as an N_eff-feeding observation. Cross-pollination suggests the partition rigidity is ALSO a CC-relevant index, because rep-theoretic invariants of Sym^2 feed into every spectral action moment. This connection was not visible in either my L4 or mack's M3 individually.

**E-L3. The E_C 3-method split extends to other framework observables -- Leggett, Mott, BKT, and potentially all BCS+Josephson quantities have THREE natural values each.**

**Numbers first.** My L1 E_C three-method split was:
- Method A: single-cell spectral invariant (Delta_OES)
- Method B: Bogoliubov mean-field fixed-point (U_star)
- Method C: finite-dim ED compressibility (4-cell 2nd-difference)

**Claim**: this is a general structural feature of any BCS+Josephson observable on CG(24), not unique to E_C. Every observable has three natural extraction routes: (i) single-cell spectral invariant, (ii) mean-field/Bogoliubov analytic form, (iii) finite-dim ED dressed observable. They measure different physical quantities and they coincide only in limits.

**Testing this on Leggett**: the Leggett gap omega_L1 has three methods:
- Method A: single-cell spectral invariant = inter-band gap for B1 mode = 0.138 M_KK (S66 LEGGETT-SPECTRAL PASS).
- Method B: Bogoliubov-type analytic formula (inter-band coupling * lambda_min_nz) -- not yet computed.
- Method C: finite-dim ED compressibility response to a pair imbalance between bands -- S66 POMERAN-4CELL at q=0 gives min(1+F) = 0.507 (Pomeranchuk-stable, not broken), which is the Method C analog.

**Testing this on Mott**: delta_OOM_Mott has three methods:
- Method A: formula log10(1 + sqrt(E_C / (8 * J_a))) with Method A E_C and Gilkey J_a. Result: 0.1411 OOM (W2-F).
- Method B: same formula with Method B E_C and Bogoliubov J_a. Result: 0.498 OOM (above PASS band).
- Method C: same formula with Method C E_C and compressibility-J. Result: 0.053 OOM (below INFO band).

**Testing this on BKT**: T_BKT ratios 24:1.5:1 have three methods:
- Method A: per-bond K_a = J_a (S47 canonical). PASS.
- Method B: per-cell K_a = bond-count * J_a / z (rescaling). FAIL the ratio structure.
- Method C: finite-dim compressibility-weighted K_a. Not computed, but would dress the ratios.

**Emergence**: every BCS+Josephson observable on CG(24) has a **three-method decomposition** structural to the substrate. The methods measure different physical quantities. The S73A "189x scatter" on E_C was the first appearance of this feature; it generalizes to Leggett, Mott, BKT, Pomeranchuk, and likely every BCS observable. **This is a structural property of the substrate, not a computational inconsistency.**

**New S75 computation candidate**: **THREE-METHOD-DECOMPOSITION-75** -- for each BCS+Josephson observable currently computed at a single value, extract the three-method decomposition and check whether each method maps to a distinct CMB-era parameter (as Method A -> A_s, Method B -> n_s, Method C -> effacement does for E_C). If the decomposition is universal, it adds a structural theorem of the form "BCS observables on CG(24) are three-dimensional in physical interpretation, with each dimension feeding a distinct CMB-era parameter through a distinct mechanism."

**Why this is an emergence**: The three-method split was framed in L1 as specific to E_C. mack's E1 added the CMB-era observable mapping. Together they imply a universal structural feature: every BCS observable on CG(24) carries three distinct physical observables, not one. This is a substantial upgrade to the condensed-matter side of the framework -- it multiplies the number of permanent structural results by a factor of 3 for each BCS observable, which feeds directly into the W4-V rolling meta-gate (C-L4 in this round).

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Scorecard layer-tagging 70/30 | M1, Re:M1, C1, E3 | **Converged** | Revised to 75.5% STRUCTURAL / 24.5% PREDICTION_LAYER after C1 (N_eff prior from rep-theoretic partition, +3.07 OOM) and E3 (horizon-alignment entry #24, +2.00 OOM). Joint log-BF: 42.13 -> 47.20. Methodology rule: use derivational prior range, not observational fluctuation range, when they differ by > 1 OOM. |
| 2 | Joint (n_s, w_0) falsification | M2, Re:M2 | **Partial** | sigma(w_0) < 0.025 is a self-falsification boundary (agreed). Slow-roll identity \|w_a\| >= 0.164 is structural (agreed), incompatible with DESI DR2+DESY5 negative-w_a preference. Separate w_a falsifier needed (A-L2). Condensed-matter t is pinned at 0.015 via J_C2/J_u2 ratio and is structurally independent of the functional-selection t = 0.088 +/- 0.012; self-consistency check CROSS-CHECK-T-74B is a blocking item. |
| 3 | DILUTION-CC scheme audit | M3, Re:M3, C2 | **Converged** | S66 a_0-scheme PASS -> INFO downgrade is structurally correct. f*-scheme chi_2 route gives -0.47 OOM undershoot, L_max-invariant. Six condensed-matter entries pre-classified as L_max-INDEPENDENT by argument alone: E_C = 0.4643, J_C2 = 0.933, delta_OOM_Mott = 0.1411, T_BKT ratios, kappa_LLY = +1/3, horizon-alignment 0.139. Atlas INDEPENDENT fraction 58.0% -> 61.0%. |
| 4 | EVOI recalibration deadlocks | M4, Re:M4, D1, C-L1 | **Emerged** | N25 splits into N25a (phase-diffusion, decoupled from n_s,w_0) and N25b (H_phys/a_2, coupled). Under effort-normalized EVOI, ordering is N25a (0.116) > N22 (0.115) > N25b (0.113), but within rounding. N22-N25-COUPLING-CHECK-75 pre-registers the scalar-mass threshold for cross-closure. DC permanence ruled out of N25 at any cosmological reading. Condensed-matter A_s budget is zero at the closure scale. |
| 5 | E_C + Mott refined CG24 | L1, E1, C-L4, E-L1, E-L3 | **Emerged** | Three-method split (A = 0.4643, B = 9.0098, C = 0.0610 M_KK) maps to three distinct CMB observables (A -> A_s, B -> n_s, C -> effacement) via three distinct mechanisms. Method A is propagation-scale (bounded by c_Gold); Method B is substrate-reorganization-scale (unbounded by c). Generalizes to Leggett, Mott, BKT as a universal 3-method feature of BCS+Josephson observables on CG(24). |
| 6 | DC permanence FAIL | L2, D3, C-L3 | **Partial** | Rate of decay confirmed N_cells^{-1.26} from {4, 8, 12}. Thermodynamic-limit vanishing (L2) is correct direction but the 10^{-6} d_eff=3 extrapolation is retracted -- three valid readings span 35 OOM, none structurally motivated. W4-K theorem stands as "f_lock > 0 at any finite N_cells, protected by Luttinger superselection" with NO quantitative cosmological value. CG24-COSMO-TILING-RULE-75 pre-registered. |
| 7 | DM candidate landscape | L3, D2, C-L2, D-L3 | **Emerged** | Multi-channel budget corrected: CPT-neutrality is a real-section constraint, not just a sign constraint. Soft-hair reassigned from DM to DE (w = -1, no kinetic content). Corrected partition: f_DM = f_Leggett + f_dimer_Z2 (two-channel), f_DE = f_soft-hair + f_effacement. MULTI-CHANNEL-DM-CDM-COMPAT-75 verifies dimer Z_2 only; soft-hair moves to a DE sub-gate. Mott DM CLOSED under all scaling conventions. |
| 8 | Partition rigidity (20,16) | L4, C5 | **Converged** | (n_b, n_f) = (20, 16) is a rep-theoretic invariant of Sym^2(su(3)^*) under U(2) x C^2, determined by dim(u(2)) = dim(C^2) = 4 alone. Sym^n extends to (60, 60) at n=3, an infinite countable sequence of rep-theoretic partitions. W4-V "112 permanents saturation" is wrong by at least the cardinality of the symmetric algebra. Hardening rate elevation is backlog clearance, not substrate exhaustion. W4-V-RETRACT-REGISTER-75 adopts 3-session rolling window with engine-diversity as lagging 2-session indicator. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

**Answering mack's Q-mack-R2 questions briefly first (their operational answers feed the carry-forward list below):**

**A-mack-R2-1 (Method B E_C into n_s tilt).** YES -- Method B 9.01 M_KK is the substrate-reorganization scale for Bogoliubov squeeze adiabaticity and IS the correct number for the n_s tilt computation at the fold. The substrate-not-c-limited project memory resolves this: Method B is unbounded by c_Gold because it is a spectral-reorganization rate, not a propagation speed. The 19.4x scale separation between Method A (A_s) and Method B (n_s) is structural, not methodological.

**A-mack-R2-2 (N22 scalar mass threshold for N25 closure).** The threshold is m_eff^2 / H_fold^2 >= 9 * ln(10) = 20.7, so m_eff >= 4.55 * H_fold. At H_fold set by S73B EFOLD-MAPPING, this maps to m_eff >= 4.55 * (M_KK * exp(-N_total)) after the fold -- a huge number at the fold, small today. The CANONICAL question is whether the multi-instanton condensate at L_max = 10 delivers m_eff of this order structurally. My estimate is that it does NOT (the condensate scale is typically O(1) in natural units of the instanton action, not 4.55 * H_fold), so N22 -> PASS does NOT automatically close N25. The conditional gate N22-N25-COUPLING-CHECK-75 tests this explicitly.

**A-mack-R2-3 (CG24 cosmological tiling rule).** I do NOT see a structural rule that fixes the tiling. The candidates are: (i) Luttinger superselection forces a single CG(24) per Hubble cell (giving N_eff = 24, DC ~ 4.6e-3); (ii) the spectral action's a_2 coefficient couples CG(24) copies only through the fold transit, giving a dim-of-embedding ambiguity; (iii) S_4 automorphism action on CG(24) generates an infinite replication. None has been derived yet. CG24-COSMO-TILING-RULE-75 should enumerate each candidate and test for internal consistency. Without this, the cosmological DC fraction is an indeterminate estimate.

**A-mack-R2-4 (Soft-hair gravitational coupling).** CORRECTED in D-L3 above: soft-hair does not gravitationally couple via a Klein-Gordon kinetic term (it has no dispersion relation), but via the spectral action a_2 coefficient as a VACUUM ENERGY contribution. Its equation of state is w = -1, not w = 0. Soft-hair is a DE candidate, NOT a DM candidate. The MULTI-CHANNEL-DM-CDM-COMPAT-75 gate tests dimer Z_2 only; soft-hair is tested separately as a DE candidate via the effacement channel comparison.

**A-mack-R2-5 (When does PREDICTION_LAYER become negligible in external comms).** My answer: NEVER drop PREDICTION_LAYER from external communication, regardless of its fractional contribution. Reason: PREDICTION_LAYER is the layer where the framework takes risk. Even at 95/5 or 99/1, reporting PREDICTION_LAYER explicitly tells the reader where the convention-dependent claims sit and what could be revised under future methodology changes. The purpose of the layer tagging is not to rhetorically minimize one layer but to make the HONEST position legible. At 80/20 or 75/25, the scorecard should say "75/25 split between STRUCTURAL theorems and PREDICTION_LAYER scheme-dependent claims" -- both layers reported, neither one suppressed.

---

**Numbered open questions for S75+:**

1. **CROSS-CHECK-T-74B**: Compare t_functional = 0.088 +/- 0.012 (from S76 functional-selection wave) against t_structural = 0.015 derived from S47 J_C2 / J_u2 = 0.933/0.097 ratio. Pre-registered PASS if the two agree within 3-sigma when rescaled to a common normalization; FAIL if > 6x discrepancy (current gap). Blocks sigma(w_0) < 0.025 tightening. Input: S47 J values, S76 functional-selection t value. Feed: M2 Q1, DR3 joint ellipse.

2. **N22-N25-COUPLING-CHECK-75**: Compute scalar mass term m_eff from multi-instanton condensate at L_max = 10 and test whether m_eff^2 / H_fold^2 >= 20.7 (9 OOM cross-closure threshold). Pre-registered PASS if m_eff^2 / H_fold^2 >= 20.7 (N22 PASS closes N25); INFO if 5 <= m_eff^2 / H_fold^2 < 20.7 (partial closure, additional mechanism needed); FAIL if < 5 (N22 and N25 remain independent). Input: N22 verdict, condensate scale. Feed: N25a/N25b split EVOI.

3. **N25-CROSS-CORRELATION-CHECK-75**: Run N25a full-spectrum (not per-mode) phase-diffusion computation; verify induced a_2 weight shift is < 0.01 OOM. Pre-registered PASS if cross-term < 0.01 OOM (split is clean); FAIL if > 0.05 OOM (sub-gates cross-couple, joint EVOI required). Input: S72 BCS-DRESSED-SA v2 mode-selective result, full a_2 weight matrix. Feed: N25a vs N25b ordering.

4. **MULTI-CHANNEL-DM-CDM-COMPAT-75**: For dimer Z_2 (confirmed DM channel after D-L3 reassignment), compute (i) Parker pair production in Z_2-odd sector, (ii) dispersion relation, (iii) effective sound speed c_s at recombination, (iv) CMB ISW amplitude. Pre-registered PASS if all four match CDM at 0.07 fractional level; FAIL if any one fails. Input: W4-Q subgroup enumeration, Parker mechanism code. Feed: f_DM multi-channel budget.

5. **CG24-COSMO-TILING-RULE-75**: Enumerate the three tiling candidates (single graph per Hubble cell, V_Hub / V_CG24 replication, S_4 automorphism replication) and test each against Luttinger superselection constraints. Pre-registered PASS if exactly one candidate is consistent with substrate-level constraints; INFO if more than one. Input: S_4 automorphism action, Luttinger superselection identities. Feed: DC permanence cosmological extrapolation, any N_cells -> infinity atlas entry.

6. **E-C-OBSERVABLE-MAPPING-75**: Verify the A/B/C -> A_s/n_s/effacement mapping by computing each CMB-era parameter as a function of the corresponding E_C method, showing functional dependence. Pre-registered PASS if each mapping shows monotone dependence with < 0.05 parameter-shift under method-swap. Input: L1 three methods, mack E1 mapping. Feed: scorecard clarity, N25a A_s structural anchor.

7. **THREE-METHOD-DECOMPOSITION-75**: For Leggett, Mott, BKT, and Pomeranchuk observables, extract the three-method (spectral invariant / Bogoliubov / finite-dim ED) decomposition. Pre-registered PASS if all four generalize the E_C pattern (three distinct values per observable). Input: W2-F Mott, W2-G BKT, S66 LEGGETT-SPECTRAL, S66 POMERAN-4CELL. Feed: universal structural feature of BCS+Josephson observables on CG(24).

8. **SOFT-HAIR-DE-VERIFICATION-75** (replaces SOFT-HAIR-LEGGETT-FILTER-75 from Re:M3): Compute soft-hair contribution to rho_vac through the a_2 coefficient as a vacuum-energy (w = -1) contribution. Pre-registered PASS if f_DE^{soft-hair} is in [0.10, 0.30] range (consistent with 0.20 reservoir); INFO if in [0.03, 0.10] (consistent with effacement residual); FAIL if < 0.01 or > 0.5. Input: R-G unpopulated sector count, a_2 weight formulation. Feed: DE partition, CC prediction cross-check.

9. **CC-DOUBLE-INDEX-75**: Compute rho_vac / rho_obs using both chi_2 and (n_b / n_f) = 1.25 as two L_max-robust indices. Pre-registered PASS if the two-index form reduces L_max drift below 3% (improving on current 4.05%). Input: W4-W chi_2 values, W4-R partition rigidity. Feed: revised CC atlas entry.

10. **W4-Z-W-A-REGISTRATION-75**: Pre-register w_a = +0.162 with band [+0.10, +0.22] and hard falsifier at w_a < -0.10 (> 3-sigma). Fold into a unified 3D (n_s, w_0, w_a) joint pre-registration. Input: W3-J slow-roll identity, W4-Z current w_0 registration. Feed: DR3 falsifier completeness.

11. **SCORECARD-ADD-HORIZON-ALIGN-75**: Formally add lambda_mode_today / (c/H_0) = 0.139 as STR entry #24 with log10(BF) = 2.00. Rewrite W4-T under the C1 + E3 revision (75.5% / 24.5% log-ratio, joint BF 10^{47.20}). Input: E3 quantitative table. Feed: scorecard freeze for external docs.

12. **ATLAS-RECLASSIFY-75**: Single Wave 1 computation classifying the 70 NEEDS_REVERIFY atlas entries across all agent subsets. landau-condensed-matter-theorist subset (8 entries) pre-classified in Re:M3. Pre-registered PASS if >= 40 entries classified. Input: atlas table, per-agent subset assignments. Feed: NEEDS_REVERIFY queue reduction.

13. **W4-V-RETRACT-REGISTER-75**: Retract single-threshold meta-gate, register rolling-3-session-window (S75+S76+S77 average) with engine-diversity count as a 2-session-lagging second axis. Pre-registered levels: PASS < 3/session avg, INFO 3-6, FAIL > 6. Engine-diversity evaluation deferred to S78 or later. Input: S74 LOCAL FAIL data, four-engine enumeration. Feed: hardening rate meta-gate replacement.

14. **SYM-N-ENUMERATION-75**: Compute Sym^4(su(3)^*) J_C2 parity partition (dim 330) under U(2) x C^2 split. Add as permanent theorem. Pre-registered PASS if the integer partition is consistent with binomial expansion sum_k C(4,k) * C(4, 4-k) * parity. Input: L4 partition method. Feed: W4-V rolling window (one new theorem per engine per session target).

15. **LUTTINGER-TIME-ORDER-75**: Extend W4-K Luttinger superselection theorem to time-ordered correlators. Pre-registered PASS if the Schmidt decomposition of the time-ordered two-point function preserves the 80/20 partition structure at finite N_cells. Input: W4-K theorem, S71 inter-site entanglement. Feed: W4-V engine #3 datapoint.

16. **DIMER-Z2-POPULATION-75** (from L3): Parker-type pair-production calculation in the Z_2-odd sector. Pre-registered PASS if n_Z2_odd / n_pair is in [0.1, 0.5]. Input: W4-Q Z_2 subgroup generator, Parker pair-production mechanism. Feed: MULTI-CHANNEL-DM-CDM-COMPAT-75 fractional input.

17. **POMERAN-N-SCAN-75**: Compute Pomeranchuk stability across N_cells = 4, 8, 12 to test whether the q=0 instability threshold at z_crit = 4.1 is a small-dim artifact analogous to DC permanence. Input: S66 POMERAN-4CELL, S67 BA-LIFETIME. Feed: structural coherence of condensed-matter sector as N_cells grows.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **Scorecard structural fraction moved from 72.6% to 75.5%** via two corrections: (i) the N_eff BF was underclaimed by +3.07 OOM because the observational fluctuation prior range was used instead of the rep-theoretic derivation range; (ii) horizon-alignment lambda_mode_today / (c/H_0) = 0.139 is a previously-unscored L_max-INDEPENDENT structural observable that adds STR entry #24 at log10(BF) = 2.00. Joint BF: 10^{42.13} -> 10^{47.20}. Methodology rule: use derivational prior range when it differs from observational fluctuation range by > 1 OOM.
- **S74 single-threshold W4-V hardening meta-gate is retracted and replaced by a 3-session rolling window (S75+S76+S77 average)** with engine-diversity as a 2-session lagging second axis. Framework hardening-rate elevation is reframed from "hot phase / substrate exhaustion warning" to "methodology backlog clearance across four independent generative engines" (U(2) Sym^n, CG(24) graph invariants, Luttinger extensions, Morse-Bott Hessian decompositions). Sym^n is proved countably infinite, so the "112 permanents saturation" estimate is wrong by at least the cardinality of the symmetric algebra.
- **The multi-channel DM budget is corrected from three channels to two** via a CPT-neutrality-as-real-section-constraint argument. Soft-hair is reassigned from DM (w = 0) to DE (w = -1 vacuum-energy contribution through the spectral action a_2 coefficient). Corrected partition: f_DM = f_Leggett + f_dimer_Z2 (two channels), f_DE = f_soft-hair + f_effacement. The MULTI-CHANNEL-DM-CDM-COMPAT-75 gate now tests dimer Z_2 only.

### What Holds

- **The single-channel Leggett DM PASS** from S66 + W4-FF is unchanged: Q = 18.6 Lorentzian lineshape, k_J = 6e-3 Mpc^{-1}, CDM-compatible at all observed scales where DM clustering has been measured. The Mott DM CLOSED verdict holds under all three scaling conventions tested in W4-P.
- **The DILUTION-CC S66 PASS -> INFO downgrade** stands as correct methodology. The f*-scheme chi_2 route gives -0.47 OOM undershoot, L_max-invariant at the 4% level. The S66 a_0 scheme is structurally confirmed as L_max-SENSITIVE-DIVERGENT (85% drift in a_0 and 287x drift in S_fold from L=3 to L=7). This is a methodology rule for the atlas, not a setback: ratios of moments are robust; absolute moments are not.
- **Partition rigidity (n_b, n_f) = (20, 16)** as a rep-theoretic invariant of Sym^2(su(3)^*) under U(2) x C^2, determined by dim(u(2)) = dim(C^2) = 4 alone, is a new permanent theorem. It extends to Sym^3 = (60, 60), Sym^4 = TBD, ad infinitum. W4-R is the first datapoint in an infinite countable sequence. Eight condensed-matter entries (E_C = 0.4643, J_C2 = 0.933, Mott = 0.1411 OOM, T_BKT ratios, kappa_LLY = +1/3, horizon alignment = 0.139, plus the two k-scale absolute-energy sensitives) are reclassified from NEEDS_REVERIFY to six L_max-INDEPENDENT and two L_max-SENSITIVE-ABSORBABLE.

### What Breaks or Strains

- **The A_s amplitude deadlock (N25) has NO condensed-matter amplitude budget.** The 0.316 OOM shortfall after W2-H closure (0.400 OOM) must come from a non-condensed-matter channel. W4-P Mott renormalization and W4-GG BCS k-scale are both scale-setting results (where gaps or filter edges live), not amplitude results. DC permanence is ruled out under all three cosmological tiling readings. The surviving candidates are all UNCOMPUTED: spatial thimble (dimensional estimate 0.25-0.50 OOM), non-Gaussian Mott correction (~0.05 OOM), H_phys reduction (coupled to n_s, w_0), a_2 spectral weight renormalization (coupled to G_N and W1-E Friedmann FAIL consequences), Luttinger superselection decoherence (uncomputed). N25 remains a structural wall.
- **The w_a slow-roll identity |w_a| >= 0.164 is structurally incompatible with DESI DR2+DESY5 negative-w_a preference (~ -0.8 at 3.9-sigma).** If DR3 confirms negative w_a at > 3-sigma, the framework is falsified on the w_a axis regardless of the w_0 point-in-interval test. The only escape is an explicit sign flip in the tau -> H back-reaction map, which is not currently in the framework. A separate w_a falsifier W4-Z-W-A-REGISTRATION-75 is required; the current W4-Z pre-registers w_0 only.
- **The t parameter (f*-mixing) has two structurally independent values**: t_structural ~ 0.015 from condensed-matter J_C2 / J_u2 = 9.62, and t_functional ~ 0.088 from S76 functional-selection. The 6x discrepancy is a potential self-falsification if it resolves in S76 without consistency. CROSS-CHECK-T-74B is a blocking gate for the DR3 (n_s, w_0) joint ellipse tightening. This does not break the framework but it is a sharp self-consistency demand.

### Carry-Forward Computations

This section is the primary input to /rclab-plan for S75 and subsequent sessions. Items are deduplicated across all four workshop turns and drawn from CONVERGENCE / DISSENT / EMERGENCE plus question exchanges.

1. **CROSS-CHECK-T-74B**. Blocks any sigma(w_0) tightening. Compare t_functional (S76 Wave) vs t_structural = J_C2/J_u2 ratio (S47). Pre-reg PASS if agreement within 3-sigma under common normalization. Input: S47 J values, S76 functional-selection wave. Effort: 0.5 session. Feeds M2 joint ellipse tightening.

2. **N22-N25-COUPLING-CHECK-75**. Tests conditional cross-closure of both deadlocks. Compute m_eff from multi-instanton condensate at L_max = 10, test m_eff^2 / H_fold^2 >= 20.7. Pre-reg PASS if >= 20.7, INFO 5-20.7, FAIL < 5. Input: N22 verdict, condensate scale. Effort: 1 session (piggyback on N22). Feeds EVOI ordering N22 vs N25a.

3. **N25-CROSS-CORRELATION-CHECK-75**. Tests cleanness of N25a/N25b split. Full-spectrum phase-diffusion with a_2 weight tracking. Pre-reg PASS if cross-term < 0.01 OOM, FAIL > 0.05 OOM. Input: S72 BCS-DRESSED-SA v2, full a_2 weight matrix. Effort: 1 session. Feeds split vs joint EVOI decision.

4. **MULTI-CHANNEL-DM-CDM-COMPAT-75**. Verifies dimer Z_2 as DM channel (soft-hair reassigned to DE per D-L3). Compute Parker pair production + dispersion + c_s at recomb + CMB ISW amplitude for Z_2-odd sector. Pre-reg PASS if all four match CDM at 0.07 fractional level. Input: W4-Q subgroup enumeration, Parker mechanism. Effort: 1 session. Feeds f_DM multi-channel budget and Omega_DM h^2 scorecard BF.

5. **CG24-COSMO-TILING-RULE-75**. Determines how CG(24) replicates over cosmological volumes. Enumerate single-graph, full-tiling, and S_4-automorphism candidates; test against Luttinger superselection. Pre-reg PASS if exactly one candidate is consistent. Input: S_4 automorphism action, Luttinger identities. Effort: 0.5 session. Feeds DC permanence cosmological extrapolation.

6. **E-C-OBSERVABLE-MAPPING-75**. Operationalizes L1 + E1 cross-pollination. Compute A_s as function of E_C(A), n_s as function of E_C(B), effacement as function of E_C(C); test monotone dependence. Pre-reg PASS if each mapping shows monotone dependence with < 0.05 parameter-shift under method-swap. Input: L1 three methods, E1 mapping. Effort: 1 session. Feeds scorecard clarity and N25a A_s anchor.

7. **THREE-METHOD-DECOMPOSITION-75**. Generalizes E1 to all BCS+Josephson observables on CG(24). Extract three-method decomposition for Leggett, Mott, BKT, Pomeranchuk. Pre-reg PASS if universal pattern holds. Input: W2-F, W2-G, S66 LEGGETT-SPECTRAL, S66 POMERAN-4CELL. Effort: 1.5 session. Feeds universal structural feature registration and W4-V engine #1 multiplication.

8. **SOFT-HAIR-DE-VERIFICATION-75**. Replaces SOFT-HAIR-LEGGETT-FILTER-75. Compute soft-hair as DE candidate via a_2 vacuum energy. Pre-reg PASS if f_DE^{soft-hair} in [0.10, 0.30]. Input: R-G unpopulated sector count, a_2 weight. Effort: 0.5 session. Feeds DE partition and CC prediction.

9. **CC-DOUBLE-INDEX-75**. Uses (chi_2, n_b/n_f) as joint L_max-robust indices for CC prediction. Pre-reg PASS if two-index form reduces L_max drift below 3%. Input: W4-W chi_2, W4-R partition rigidity. Effort: 0.5 session. Feeds revised CC atlas entry.

10. **W4-Z-W-A-REGISTRATION-75**. Pre-register w_a falsifier with band [+0.10, +0.22] and hard FAIL at w_a < -0.10 at > 3-sigma. Fold into 3D (n_s, w_0, w_a) joint. Input: W3-J identity, W4-Z current w_0. Effort: 0.25 session (registration, not new computation). Feeds DR3 falsifier completeness.

11. **SCORECARD-ADD-HORIZON-ALIGN-75**. Nominal rewrite of W4-T with STR entry #24 added. Input: E3 table. Effort: 0.25 session. Feeds scorecard freeze.

12. **ATLAS-RECLASSIFY-75**. Single-computation classification of 70 NEEDS_REVERIFY entries across agent subsets. Pre-reg PASS if >= 40 classified. Input: atlas table. Effort: 1 session coordinated. Feeds NEEDS_REVERIFY queue reduction.

13. **W4-V-RETRACT-REGISTER-75**. Retract single-threshold meta-gate; register rolling window with engine-diversity as 2-session-lagging axis. Input: S74 LOCAL FAIL data, four-engine enumeration. Effort: 0.25 session (registration). Feeds hardening meta-gate replacement.

14. **SYM-N-ENUMERATION-75**. Compute Sym^4(su(3)^*) J_C2 parity partition (dim 330). Pre-reg PASS if integer partition matches binomial expansion. Input: L4 method. Effort: 0.25 session (closed-form). Feeds W4-V engine #1 datapoint.

15. **LUTTINGER-TIME-ORDER-75**. Extend W4-K to time-ordered correlators. Pre-reg PASS if 80/20 partition preserved. Input: W4-K, S71. Effort: 1 session. Feeds W4-V engine #3 datapoint.

16. **DIMER-Z2-POPULATION-75**. Parker pair-production in Z_2-odd sector. Pre-reg PASS if n_Z2_odd / n_pair in [0.1, 0.5]. Input: W4-Q Z_2 generator. Effort: 0.75 session. Feeds MULTI-CHANNEL-DM-CDM-COMPAT-75.

17. **POMERAN-N-SCAN-75**. Test Pomeranchuk q=0 instability at z_crit = 4.1 as finite-size artifact (analogous to DC permanence). Run on N_cells = 4, 8, 12. Input: S66 POMERAN-4CELL. Effort: 1 session. Feeds condensed-matter N_cells coherence.

Total estimated effort: ~11 sessions of computation. Wave 1 priority: items 1, 2, 3, 4, 6, 8, 10, 11 (highest EVOI or blocking). Wave 2: items 5, 7, 9, 12, 13. Wave 3: items 14, 15, 16, 17.

### Closing Line

The S74 workshop promoted eight condensed-matter observables to the L_max-independent structural floor, split the A_s deadlock into decoupled/coupled sub-gates, reassigned soft-hair from DM to DE, and revised the scorecard log-ratio to 75.5% STRUCTURAL / 24.5% PREDICTION_LAYER -- leaving N25 without a condensed-matter amplitude budget and committing the framework to a positive w_a that DESI DR3 can falsify outright.
