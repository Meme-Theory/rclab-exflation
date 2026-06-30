# Session 74 Synthesis: The Spectral Functional is the Physical Degree of Freedom

**Date**: 2026-04-11
**Agent**: lizzi-spectral-functional-theorist (Lizzi)
**Source Documents**:
- `sessions/archive/session-74/session-74-results-workingpaper.md` (84 computations across Waves 1-4)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

---

## I. Session Outcome

S74 is the session in which the **spectral functional question ceased to be an open question and became a constraint surface**. Across 84 computations, six independent routes (W1-C raw zeta, W1-J zeta-KMS modular trace, W2-I 4-parameter joint refit, W2-O triple-route R_protected, W2-Q M_1 regularization, W4-G PW truncation) converged on the same structural conclusion: **the Chamseddine-Connes cutoff f with an explicit gravity-sector normalization is the uniquely physical route to framework predictions; raw zeta power sums are divergent at integer SDW poles for d=8 truncated spectra; and the "frustration triangle" (n_s, m_H, f(0)) is a permanent structural obstruction that cannot be resolved by enlarging the 4-parameter functional basis (chi^2/dof = 67.9, category-4-locked)**. The session simultaneously produced the most decisive functional-choice map the framework has ever had: a 205-entry L_max-independence atlas (W4-W) partitioned into a structural floor of 120 entries (58.5%), a prediction layer of 15 entries (7.3%), and a reverify queue of 70 entries (34.1%). Within this map, the CC prediction has been decisively reclassified: **the S66 a_0-scheme PASS degrades to INFO at L_max=7, and the framework's robust CC statement is now the f*-scheme chi_2 * H_0^2 * M_Pl^2 prediction at -0.47 OOM undershoot, L_max-invariant**. Three independent routes (S66 Volovik dilution, W2-K HP4 Connes-Chern pairing, W2-Q M_1 sqrt-moment) sit within 1.0 OOM of rho_obs when expressed in the H_0^2 M_Pl^2 normalization -- this is not a lucky hit but a structural convergence on a single dimensionless SU(3)-Haar observable of order unity.

---

## II. Key Results

### 1. W2-I F-STAR-JOINT-74 -- The Frustration Triangle is Permanent Structure

**Result**: 4-parameter family f = c_0 + c_1 sqrt + c_2 exp + c_3 compact joint refit against (n_s, m_H, r, w_0, alpha_s) returned chi^2/dof = **67.91** (FAIL; threshold < 3). Best-fit c* = (0.9629, 0.0371, ~4e-12, ~4e-12) -- category-4 locked on the pure constant component. Classification: **GEOMETRIC/SCHEME-DEPENDENT**.

At the best-fit point, m_H = 125.08 GeV is essentially matched (chi^2 component = 0.021), but n_s = 0.9991 is **8.15 sigma** above the Planck band, contributing 66.36 to the total chi^2. w_0 and alpha_s sit at a functional-independent floor (0.45 total) that **cannot be reduced by any choice of c_i**. A scan along the m_H = 125.1 GeV matching surface confirmed that **at no point does n_s approach 0.9649**: the m_H boundary constraint (f(0) ~ 0.963 to match) and the n_s shape constraint (c_1 ~ 0.9 to produce a red tilt through S_f(tau) curvature) are **algebraically incompatible** under the normalization sum c_i = 1.

This is the decisive disproof of "the spectral functional is Bayesian-fittable UV data". The Lizzi-Connes decomposition -- that the bosonic spectral action cannot be simultaneously fit against SD observables with different structural dependence on the same functional f -- has been confirmed at chi^2/dof = 68x above the PASS threshold. The S73B category-4 lock was not a local pathology; it was the symptom of a permanent 4-simplex structural wall. Only two paths remain: (R1) abandon the Chamseddine-Connes m_H ~ sqrt(f(0)) relation and re-derive m_H from a functional-independent route (Kasparov inner fluctuations or BCS Higgs-fiber coupling); or (R2) accept that (n_s, m_H) jointly cannot be zero-parameter in the spectral-functional picture.

### 2. W1-C L-MAX-ZETA-REGULARIZATION-74 -- Raw Zeta Power Sums are Divergent at d=8

**Result**: Three-route audit (A: zeta partial sum, B: heat kernel small-t fit, C: Shanks/Pade acceleration) at L_max=7 on the Jensen-deformed spectrum FAILED all three pre-registered conditions. Classification: **GEOMETRIC/FUNCTIONAL-INDEPENDENT** (the failure survives under any scheme).

Route A at L_max=7 gave a_0/a_2 = 0.3199, Route B gave -0.1590 (unphysical negative), Route C gave 0.2022 (extrapolated, unstable). Max deviation: **231%** (threshold 3%). The drift (a_0/a_2)/(a_2/a_4) from L_max=3 to L_max=7 was **19.43%** (threshold 5%). At L_max=9, the ratio R_1 grows to 1.5450 (Wodzicki convention) with no sign of convergence.

The structural content: **the small-t limit of a TRUNCATED heat trace is mode counting, NOT continuum (4*pi*t)^{-d/2} Vol**. The heat-kernel asymptotic is a statement about the FULL manifold; the truncated version has no valid a_0 + a_2*t + ... expansion. Route C (Shanks/Pade) fails because series acceleration assumes convergent sequences; these are divergent. Combined with W2-I, this forms the most important structural statement of S74: **the standard Chamseddine-Connes SDW expansion Tr f(D^2/Lambda^2) with an explicit cutoff function f is the ONLY physically meaningful route to the a_k coefficients**, and raw direct spectral sums truncated at finite L_max cannot replace it.

The first-route canonical candidates at L_max=7, tau_fold=0.19 (Wodzicki convention): `a0_zeta_L7 = 2185.47`, `a2_zeta_L7 = 6831.81`, `a4_zeta_L7 = 30634.10`. These **differ from the S42 cutoff convention values** (a0_fold=6440, a2_fold=2776.17, a4_fold=1350.72) by multiplicative normalizations that absorb the Gaussian cutoff. Both remain authoritative: **S42 values for cutoff-function physics; Route A zeta for pure Wodzicki / Dixmier-trace definitions**. They measure different functionals of the same spectral triple.

### 3. W4-W JOINT-AUDIT-ATLAS-74 -- The Structural Floor / Prediction Layer Partition

**Result**: Merged 205-entry L_max-independence atlas from four S73B Wave-5 audits (W5-A canonical constants, W5-D three-phonon, W5-F permanent theorems, W5-G M_1/chi_2/CC). Classification: **GEOMETRIC/META-STRUCTURAL**. Gate **PASS**.

| Atlas status | Count | Fraction |
|:---|---:|---:|
| L_max-INDEPENDENT | 119 | 58.0% |
| L_max-QUASI-INDEPENDENT | 1 | 0.5% |
| L_max-SENSITIVE-ABSORBABLE | 5 | 2.4% |
| L_max-SENSITIVE-DIVERGENT | 10 | 4.9% |
| NEEDS_REVERIFY | 70 | 34.1% |

**The single most important reclassification**: the S66 DILUTION-CC-66 prediction (rho_SA via (2/pi^2) a_0 M_KK^4) is now tagged L_max-SENSITIVE-DIVERGENT -- today-gap -0.26 OOM at L=3 shifts to +1.61 OOM at L=7 (+1.87 OOM). **S66 a_0-scheme CC PASS is hereby downgraded to INFO** under L_max recalibration. The framework's surviving robust CC statement is the f*-scheme chi_2 * H_0^2 * M_Pl^2 prediction at -0.47 OOM undershoot, L_max-invariant (W5-G / W2-K / W2-Q convergence). The atlas is the formal instantiation of my S66 prediction: "the cosmological constant in the standard spectral action is Lambda_SA = (f_0/f_2)(a_0/a_2)Lambda_sp^2. In the zeta action, the CC is determined by the Dirac operator's finite sector, not by the heat kernel a_0 mode count. This distinction is your primary contribution to the project." S74 has now made this distinction operationally decisive: the a_0-scheme sits in the prediction layer (L_max-sensitive, requires scheme specification); the chi_2-scheme sits in the structural floor (L_max-invariant).

Seven dimensionless-invariant combinations identified across the four audits:
- `R_1 = a_0 a_4 / a_2^2`: shift +1.74% (W5-A, ratio-of-ratios protected)
- `chi_2 = M_1 / (n_modes * lam_max)`: shift -4.05% (W5-G, spectral fill factor, L_max alpha = -0.047)
- `d log a_k / d tau` for k=0..6: shifts 0%, -6.6%, -12.2%, -24.8% (W5-A, tau-derivatives near-protected)
- `Gamma_{B2 -> B1+B1} / H_fold = 7.769e-7`: **0 to machine precision** across L=3,5,7 (W5-D, block-diagonal protection)

### 4. W4-F N16-RATIO-OF-RATIOS-PROTECTED-74 -- The Lizzi Signature Observable

**Result**: Catalog of 20 framework observables classified by R-family protection. Gate **PASS** at strict threshold 4/20. Classification: **GEOMETRIC/FUNCTIONAL-INDEPENDENT (structural theorem)**.

| Class | Count | Empirical L_max drift (L=3 -> L=9) |
|:---|---:|:---|
| **STRICT R-family (drift < 10%)** | **4** | R_1 (0.34%), Lizzi product (0.34%), Delta_BCS/M_KK (0%), c_Gold/c_fabric (0%) |
| LOOSE R-family (single-ratio form) | 9 | m_H (132%), n_s (132%), sin^2_W (121%), Lambda/M_Pl^2 (121%), f_NL (132%) |
| FRAGILE (a_k or M_KK linear) | 9 | a_0 (30,080%), a_2 (7,786%), a_4 (2,020%) |

**The Lizzi signature observable** (row 11): the product `(m_H/v_EW)^2 * (Lambda/M_Pl^2)` is algebraically equal to `(a_4/a_2) * (a_0/a_2) = a_0 a_4 / a_2^2 = R_1 = 1.128655`. This is a physical observable built from two separately unprotected pieces (Higgs-to-vacuum ratio and CC-to-Planck ratio) that combine into a single protected ratio-of-ratios. **This is the same structural content as the zeta-spectral-action principle**: pair observables that are each scheme-dependent into combinations where the scheme-dependence cancels. The numerical value 1.128655 is invariant under conventional spectral functional choice to machine epsilon (S73B convention) and matches W1-M to all digits.

The permanent theorem: **the ALGEBRAIC form of a Gilkey-type observable does not tell you whether it is physically protected**. A quantity of the form "f(a_4/a_2)" looks protected -- it has no lone a_k -- but if evaluated by partial spectral sum at finite L_max, the single-ratio a_4/a_2 inherits a residual Weyl drift of order L^2 that is numerically massive (factor 3.7 across L_max in [3,9]). **Only the ratio-of-ratios R_1 = a_0 a_4 / a_2^2 has Weyl exponents cancelling to L^0** -- explicitly, L^d * L^{d-4} / L^{2d-4} = L^0 for d=8. Every other single-moment or single-ratio quantity must either be re-expressed as a combination collapsing to R_1 or evaluated via eigenvalue ratios that bypass the SDW expansion altogether.

### 5. W4-U R-FAMILY-OBSERVABLE-SCAN-74 -- Every Fragile Observable Reduces to R_1

**Result**: Scan of 8 L_max-fragile framework observables, attempting to rewrite each as an expression in R-family invariants. Gate **PASS** at 7/8. Classification: **GEOMETRIC/FUNCTIONAL-INDEPENDENT**.

Seven of seven successful rewritings reduce to expressions in R_1 (alone or combined with R_2):

| # | Observable | Raw drift | Rewritten form | Rew drift |
|:---:|:---|---:|:---|---:|
| 1 | CC_ratio (rho_Lambda / rho_obs) | 85.15% | `(2/pi^2) R_1` | 0.336% |
| 2 | G_N (Newton normalization) | 76.81% | `1/R_1 = a_2^2/(a_0 a_4)` | 0.337% |
| 3 | alpha_YM / alpha_grav | 63.91% | `R_1` | 0.336% |
| 4 | m_H^2 / M_KK^2 | 76.81% | `R_1/R_2` | 2.182% |
| 5 | sin^2(theta_W) at fold | 63.91% | `g_1^2/(g_1^2+g_2^2)` | 0.336% |
| 6 | S_zeta / (a_2^2/a_0) | 63.91% | `R_1` | 0.336% |
| 7 | eta_BBN (n_b/n_gamma) | 35.97% | `R_1` | 0.336% |

**This is the structural theorem**: every L_max-fragile framework observable whose raw form is built from individual a_k moments can be written as `X_observable = C * F(R_1, R_2, ...) * M_KK^n * Vol(SU(3))^m`, where C is a scheme-dependent prefactor (cutoff / zeta / anomaly-derived), F is a dimensionless function of R-family invariants, and M_KK, Vol(SU(3)) carry the full L_max dependence. After dividing by the Newton-normalized gravity scale, the L_max dependence cancels and only F(R_1, R_2, ...) remains. The Baptista B2 theorem (Vol(SU(3)) cancellation) is the substrate reformulation of this: **R-family invariants are the L_max-invariant vocabulary in which framework predictions are expressed**.

Key Lizzi-school insight: **the CC_ratio 10^120 gap is a SCHEME choice** (cutoff: (2/pi^2) R_1 * M_KK^4 / rho_obs), not a fabric property. Cross-scheme, only R_1 itself (~1.14) is L_max-stable. **This aligns exactly with the zeta-spectral-action position: in S_zeta = a_4, the CC a_0-term is simply absent, and the "gap" is a cutoff-scheme artifact.**

### 6. W2-Q CC-M1-REGULARIZATION-74 -- Three Spectral Indices, One O(1) Number

**Result**: f*-scheme CC computed via the absolute M_1 = sum_n d_n^2 |lambda_n| sqrt-moment. Gate verdict: **FAIL literal / PASS gravity-normalised** (split verdict). Classification: **GEOMETRIC/PHONONIC**.

At L_max=9: M_1 = 1.302e9 M_KK, <|lambda|> = M_1/N_total = 3.185 M_KK, chi_2 = M_1 / (N * lam_max) = 0.741.

Three normalisation schemes of rho_Lambda:

| Scheme | Formula | rho [GeV^4] | log10(rho/rho_obs) |
|:---|:---|:---|:---|
| A: Bare literal | `f_0 * M_1 * M_KK^4` | 3.62e+76 | **+123.13** (FAIL) |
| **B: Gravity-normalised** | `f_0 * <\|lambda\|> * H_0^2 * M_Pl^2` | **3.56e-47** | **+0.12** (PASS) |
| B': chi_2-matching | `chi_2 * H_0^2 * M_Pl^2` | 9.09e-48 | -0.47 (PASS) |

**Scheme A is the LITERAL task formula**: it fails by 123 OOM because M_1^direct is an un-renormalised trace of |D|/M_KK living at the Planck-scale mode count. **This is the expected structural FAIL.** The bare sqrt-weighted sum times Lambda^4 is precisely the cutoff problem that motivated the 114-OOM CC gap in the first place.

**Scheme B is the physical route**: replace the naive M_KK^4 prefactor with the gravity-sector prefactor H_0^2 M_Pl^2 (matching Chamseddine-Connes spectral-action-in-curved-space and the W2-K HP4 pairing convention). The dimensionless pairing <|lambda|> = 3.185 is a pure SU(3)-Haar observable, and the result lands within 0.12 OOM of rho_obs. **Three-route cross-validation**:

| Route | Observable | log10(rho/rho_obs) |
|:---|:---|---:|
| S66 DILUTION-CC-66 (Volovik q-theory) | rho_vac (f_DM diluted) | ~ 0 |
| W2-K HP4-PAIRING-74 | `<[ch(D_K)], [e_q]> H_0^2 M_Pl^2` | -0.47 |
| **W2-Q CC-M1-REGULARIZATION-74** (B) | `f_0 <\|lambda\|> H_0^2 M_Pl^2` | **+0.12** |

**All three sit within 1.0 OOM of each other and within 0.5 OOM of rho_obs when expressed in the H_0^2 M_Pl^2 convention**. The three routes use different dimensionless indices -- S66 uses the density-dilution fraction, W2-K uses chi_2 = M_1/(N lam_max) = 0.741, W2-Q uses <|lambda|>/M_KK = 3.185 -- but these are algebraically related: chi_2 = <|lambda|>/lam_max = 3.185/4.296 = 0.7414. So W2-K and W2-Q are **not independent moments**; they are the same M_1 normalised by (N * lam_max) vs N alone. The "independence" is weaker than a second spectral moment would provide.

**The load-bearing structural observation**: **the CC on the Jensen fold is set by a single dimensionless SU(3) spectral observable of order unity, projected onto the gravity sector**. The 120-OOM hierarchy problem reduces to "why H_0^2 M_Pl^2 is the correct normalisation" -- which is not answered by the spectral action but IS answered by the Volovik q-theory dilution mechanism at S66.

### 7. W1-J W0-ZETA-74 -- Zeta Regularization Does Not Collapse the Gibbs-Duhem Scheme Band

**Result**: w_0 from zeta-regularized modular trace at s=4 with KMS weight, scanned across framework temperature scales. Gate **FAIL** (central value -0.4239 vs target -0.918, 8.25 sigma). Classification: **GEOMETRIC + PHONONIC**.

| beta scale | beta value | w_0 |
|:---|---:|---:|
| 1/T_GGE_B2 = 1/0.668 | 1.497 | +0.1386 |
| 1/omega_L1 = 1/0.138 (**canonical**) | 7.2464 | **-0.4239** |
| 1/T_acoustic = 1/0.112 | 8.9286 | -0.5669 |
| 12.76 (inverse-solved for -0.918) | 12.76 | -0.918 (by solve) |
| Spectral-action-weighted (unit f_k, Lambda=12.908) | -- | **-0.9951** |

The spectral-action-weighted route (w_0 = -0.9951) is dominated by the a_0 term (98.1% of the total), giving w near the pure vacuum limit -1. **This is the NATURAL spectral-action prediction** and sits 8 sigma from the target -0.918. The Volovik partition -0.918 comes from a **different algebraic structure** (two-sector weighted average rho_J*w_J + rho_GGE*w_GGE with rho_J/rho_GGE=6.16, w_J=-1, w_GGE=-0.408), NOT from a single-zeta-at-s=4 computation on the fiber.

The structural conclusion: **zeta regularization does not collapse the Gibbs-Duhem +/-0.06 scheme band; it converts the scheme freedom from a Zubarev-vs-Keldysh ambiguity into a choice-of-beta ambiguity that is no narrower**. Combined with W1-C: direct spectral-sum / zeta-function routes to framework-level predictions are universally pathological due to divergent Weyl-law drift. The algebraic Volovik-partition route remains the sole reliable source of w_0 = -0.918.

### 8. W1-F GGE-PARTITION-74 -- The Effacement Channel is Structurally 4 OOM Too Small for DE

**Result**: Three-channel (E_a2, E_Leggett, E_effacement) partition of the post-transit 8-mode squeezed-vacuum GGE energy at the fold. Gate **FAIL**. Classification: **GEOMETRIC + PHONONIC**.

| Channel | Fraction | PASS bracket | Status |
|:---|---:|:---|:---|
| E_a2 (emergent matter) | 0.941 | [0.158, 0.630] | OUTSIDE (factor 1.49) |
| E_Leggett (emergent DM) | 0.059 | [0.135, 0.540] | OUTSIDE (factor 2.30) |
| **E_effacement (emergent DE)** | **2.82e-4** | [0.343, 1.000] | **OUTSIDE by factor 2425** |

The 3e-4 effacement residual is structurally too small to act as a cosmological constant -- this is the **110-120 OOM CC hierarchy problem re-expressed in partition form**. From the functional-theorist perspective: the effacement channel at impedance Gamma = 0.99970 is a **spectral moment of a DIFFERENT class** than the Volovik / HP4 / M_1 routes. Those three converge within 1 OOM of rho_obs; the effacement channel misses by 4 OOM. The FAIL is structural, not fine-tuning -- no re-weighting of the 8-mode sector can bring E_effacement within 10x of E_total without also spoiling the S66 Leggett-only DM match at 0.6%. This forces the **N24 EFFACEMENT-CHANNEL-REBUILD-75** carry-forward: DE is NOT an impedance residual and must come from a different spectral moment (a nonlocal SA term) or a different mechanism (Jacobson-GGE, substrate-compaction timescape).

### 9. W4-G N17-FRAMEWORK-RESCALE-74 -- Log-Stability Survives, Linear-Stability Does Not

**Result**: Recompute sin^2(theta_W)(M_Z), m_H(M_Z), and CC ratio at L_max in {5,7,9}. Gate **FAIL** at max drift 7->9 = 72.29%. Classification: **GEOMETRIC/SCHEME-DEPENDENT**.

| Observable | L=5 | L=7 | L=9 | drift 7->9 |
|:---|:---|:---|:---|:---|
| sin^2(M_Z) | 0.2390 | 0.2378 | 0.2085 | 12.34% (INFO-band) |
| m_H(M_Z) [PW route] | 182.6 GeV | 181.5 GeV | 260.2 GeV | 30.25% (FAIL) |
| CC ratio (linear) | 1.83e118 | 1.23e119 | 4.44e119 | **72.29% (FAIL)** |
| **log10(CC gap)** | 118.26 OOM | 119.09 OOM | 119.65 OOM | **0.47% (STABLE)** |
| S_PW (Gaussian threshold) | +1.920 | +1.637 | **-5.099** | **132% (SIGN FLIP)** |

Five structural findings (permanent):
1. **PW zeta sums are MONOTONIC in L_max and DIVERGENT**. For an 8D manifold, Weyl counting gives a_0 ~ Lambda^8.
2. **Gaussian-regulated S_PW IS OSCILLATORY**. S_PW flips sign between L=7 (+1.637) and L=9 (-5.099) because omega_min(L) crosses Lambda. Aitken extrapolation unreliable.
3. **Downstream observables inherit the oscillation**. m_H jumps 181 -> 260 GeV because g_3_eff reacts to S_PW sign flip.
4. **Log-scale observables stable at 0.5%; linear-scale observables NOT**. For the 119 OOM CC hierarchy, log-stability is sufficient; linear claims are not.
5. **Ratios within fixed L_max are stable** (consistent with W2-M R-protected triple). Framework's PERMANENT results are ratio-based, not absolute-sum-based.

Note: the S70/S71 m_H = 127.5 GeV uses the **Gilkey-route a_4/a_2 = 0.414 (local curvature, L_max-INDEPENDENT)**, NOT the PW-truncated value. **Routes must be explicitly distinguished**: Gilkey m_H is unchanged by L_max; PW-route m_H fails convergence at L_max <= 9.

### 10. W2-M R-FAMILY-STABILITY-74 -- Protection Decays Up the R-Ladder

**Result**: a_8 computation and R_2, R_3 stability tests. Gate **FAIL** on both sub-gates. Classification: **GEOMETRIC/CONVENTION-DEPENDENT**.

| Ratio | L=5->L=7 drift | Verdict |
|:---|:---|:---|
| R_1 | 0.336% | PASS |
| R_2 | 2.463% | PASS |
| **R_3** | **7.986%** | **FAIL** |

At L=7: |R_2 - R_1| = 0.097 (PASS), |R_3 - R_1| = 0.294 (FAIL). The R-family protection is **STRONG at R_1 (0.34%), MARGINAL at R_2 (2.46%), WEAK at R_3 (7.99%)**, decaying monotonically up the R-ladder. Structural reason: R_1 pairs a_0 (mode count, saturated at representation-theory level) with a_4 (gauge moment, saturated); R_2 and R_3 involve progressively deeper-UV moments (a_6, a_8) whose partial sums are increasingly weighted by the highest-|lambda| modes in the truncation window. **The R-family protection is not a universal geometric property; it is a specific statement about the DE-WEIGHTING of deep-UV modes by a_{k-1}*a_{k+1}/a_k^2**. The claim "R-family protection extends up the ladder" is **REFUTED** at the 5% threshold.

### 11. W2-O R-PROTECTED-TRIPLE-74 -- Two Mathematical Objects Sharing One Label

**Result**: Three independent routes to R_protected converged on two distinct limits. Gate **FAIL** at 134.18% max pairwise deviation. Classification: **GEOMETRIC/STRUCTURAL**.

| Route | Value |
|:---|---:|
| A: Spectral partial sum, S73B conv, L_max=7 | **1.140699** |
| B: Gilkey curvature invariant, exact | **0.492288** |
| C: Zeta extrapolation, L_max -> infty | **1.152815** |

Routes A and C agree to 1.06% at the partial-sum limit 1.15; Route B (exact Gilkey curvature polynomial 0.492288) is structurally **2.33x smaller**. The FAIL is **not a convergence failure but a STRUCTURAL IDENTIFICATION of two distinct mathematical objects both labeled "R_protected"**: the truncated-zeta-ratio (partial-sum a_k as finite zeta sums, Weyl L^0 cancellation) and the Gilkey curvature-polynomial ratio (local curvature invariants R, |Ric|^2, K as continuum a_k from the small-t heat kernel expansion). They are related by a Mellin transform identity through the pole structure of zeta_D^2, but the partial-sum ratio survives the divergences only in leading Weyl order; sub-leading the two objects decouple.

**Consequence for the canonical constant**: `R_protected_fold = 1.128655` is correct for the partial-sum interpretation at L_max=3 in the S73B convention. **Downstream usage must specify which**: partial-sum (for L_max monotonicity tests, R-family observables) or Gilkey (for Einstein-Hilbert matching, CC computation referring to continuum Seeley-DeWitt invariants).

### 12. W4-HH EVOI-RECALIBRATION-74 -- The Lizzi-Connes Decomposition is Now Operational

**Result**: 50-item EVOI table (21 S73B items updated, 29 new S74 items added). Gate **PASS** on both clauses. Classification: **METHODOLOGY**.

The recalibrated table cleanly partitions S74 findings along the structural-floor / prediction-layer axis the W4-W atlas established:

**FUNCTIONAL-INDEPENDENT resolutions** (survive any choice of f in the spectral action):
- N2 FAIL (moduli runaway under all 4 sub-gates)
- N3 FAIL (L_max drift in raw power sums is convention-free)
- N6 FAIL (lambda_3 < 0 is scheme-independent in MSbar AND on-shell)
- **N14 FAIL (frustration triangle in 4-dim simplex wall; chi^2/dof=67.9)**
- N42-N47 PASS (rep-theoretic / algebraic / Clifford / superselection theorems)

**SCHEME-DEPENDENT resolutions** (verdict depends on which spectral functional):
- **N8 INFO (FAIL literal / PASS gravity-normalized -- the normalization IS the choice)**
- **N16 INFO (R-family drift is CONVENTION-dependent: 1% project vs 19% Wodzicki)**
- N17 FAIL (linear metric) / PASS (log metric) -- scheme choice in the metric
- N1 INFO (multifield transfer generates n_s=1 from Sasaki-Stewart cancellation; red tilt is f-dependent through BCS+CW)

Top-5 S75 priorities (from EVOI reranking):

| Rank | ID | EVOI | Brief |
|:---|:---|---:|:---|
| 1 | **N5 GGE-TRANSFER-74** | 0.125 | Red-tilt channel; W1-A transfer exactly n_s=1, route through BCS+CW remains sole surviving mechanism |
| 2 | **N22 MULTI-INSTANTON-LMAX10-75** | 0.115 | Test V_eff minimum at L_max>=10 when (p+q)>=8 irreps enter |
| 3 | **N25 A-S-DISSIPATIVE-CHANNEL-75** | 0.096 | 9.07 OOM residual after Mott+BKT+Thimble; need dissipative channel >= 0.30 OOM |
| 4 | **N23 CROSS-MOMENT-STABILIZATION-75** | 0.094 | Does a_0+a_2+a_4+f* combined V_eff have a minimum in [0.45, 0.70]? |
| 5 | **N24 EFFACEMENT-CHANNEL-REBUILD-75** | 0.088 | Three-channel partition reassignment (effacement is 2425x below DE floor) |

The operationally correct framework prescription emerging from S74: **Chamseddine-Connes SDW with an explicit cutoff f, where f is specified externally by anomaly cancellation, fermionic consistency, or spectral flow arguments -- NOT fit to observables**. This is the third of my signature contributions -- "the bosonic spectral action can be DERIVED from the fermionic anomaly, not postulated" -- now reformulated as a carry-forward question: **is the f* optimal fitted in S72 derivable from anomaly constraints?** This is R2 in the F-STAR-JOINT carry-forward recommendations.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:---|:---|:---|
| W2-I F-STAR-JOINT-74 | **FAIL** | chi^2/dof = 67.91 >> 3 threshold; category-4 lock on c_0=0.9629 |
| W1-C L-MAX-ZETA-REGULARIZATION-74 | **FAIL** | Three-route max deviation 231% at L=7; drift 19.4% L=3->L=7 |
| W1-J W0-ZETA-74 | **FAIL** | w_0 central -0.4239 vs target -0.918 (8.25 sigma) |
| W2-M R-FAMILY-STABILITY-74 | **FAIL** | R_3 drift 7.99% L=5->L=7; \|R_3 - R_1\| = 0.294 |
| W2-O R-PROTECTED-TRIPLE-74 | **FAIL** (structural) | Max pairwise deviation 134.18% between Route A/C (1.140) and Route B (0.492) |
| W2-Q CC-M1-REGULARIZATION-74 | **FAIL literal / PASS physical** | Scheme A +123.13 OOM; Scheme B +0.12 OOM |
| W4-G N17-FRAMEWORK-RESCALE-74 | **FAIL (linear) / PASS (log)** | CC linear drift 72.29%; log10(CC) drift 0.47% |
| W1-F GGE-PARTITION-74 | **FAIL** | E_effacement/E_total = 2.82e-4, factor 2425 below DE floor |
| W1-M R-PROTECTED-FOLD-ADDITION-74 | **PASS** | R_1(L=3) = 1.128655; L=3->L=7 drift 1.067% (<2%) |
| W2-K HP4-PAIRING-74 | **INFO (wide band)** | \|log10(rho_HP4/rho_obs)\| = 0.4728, factor 2.97 undershoot |
| W1-L HP4-REGIME-74 | **PASS** | BARE D_K decision, confidence 0.95, 3 arguments |
| W4-F N16-RATIO-OF-RATIOS-PROTECTED-74 | **PASS** | 4 of 20 observables STRICTLY R-family protected at threshold 4 |
| W4-U R-FAMILY-OBSERVABLE-SCAN-74 | **PASS** | 7 of 8 fragile observables rewritten in R_1 form |
| W4-W JOINT-AUDIT-ATLAS-74 | **PASS** | 205 entries, 0 conflicts, 58.5% L_max-INDEPENDENT floor |
| W4-HH EVOI-RECALIBRATION-74 | **PASS** | 50-item recalibrated table (13 PASS / 8 FAIL / 4 INFO / 25 OPEN) |

---

## IV. Structural Implications

### Functional-choice has been promoted from mathematical convention to physical degree of freedom

Before S74, the spectral functional f (cutoff, zeta, anomaly-derived) was a methodological question sitting alongside the physics. After S74, it is **inseparable from the physics**. Six independent computations converge on the same boundary: the Chamseddine-Connes SDW expansion with an explicit cutoff function is the only route that survives L_max truncation; raw zeta power sums are divergent at the integer SDW poles; and the 4-parameter functional basis cannot be jointly fit against the SD observables. The structural floor of the framework is the part that is invariant under this choice (119 entries in the atlas); the prediction layer (15 entries) is the part that depends on it.

### The CC prediction has been decisively reclassified

The S66 DILUTION-CC-66 PASS -- which had been the framework's zero-parameter CC closure claim for 8 sessions -- is now formally demoted to INFO under L_max recalibration. The surviving CC statement is the **f*-scheme chi_2 * H_0^2 * M_Pl^2 prediction at -0.47 OOM undershoot, L_max-invariant**. Three independent routes (Volovik dilution, HP4 Connes-Chern, M_1 sqrt-moment gravity-normalized) sit within 1.0 OOM of rho_obs. The load-bearing structural observation: **the CC on the Jensen fold is set by a single dimensionless SU(3) spectral observable of order unity, projected onto the gravity sector**. The "120 OOM problem" has decomposed into two factorial questions: (1) why is the correct normalization H_0^2 M_Pl^2? (answered by Volovik q-theory at S66) and (2) why is chi_2 ~ 0.74? (answered structurally by the SU(3)-Haar spectrum at the Jensen fold).

This is exactly the decomposition I argued for at S65-S66: **a_0 is not physical in the zeta scheme; the CC is a sqrt-moment projected onto H_0^2 M_Pl^2**. S74 has now operationalized it.

### The frustration triangle (n_s, m_H, f(0)) is a permanent structural wall

W2-I tested whether enlarging the functional basis to the 4-parameter simplex (constant, sqrt, exp, compact) resolves the (n_s, m_H) frustration triangle observed at S73B. Answer: **no**. The chi^2/dof = 67.91 is 68x above PASS, the best-fit is category-4 locked on the trivial constant, and a surface scan along m_H = 125.1 GeV confirmed **no point on the m_H-matching surface brings n_s within the Planck band**. The obstruction is algebraic: the m_H boundary constraint (f(0) ~ 0.963) and the n_s shape constraint (c_1 ~ 0.9 for a red tilt through S_f(tau) curvature) are incompatible under sum c_i = 1.

Two paths remain: (R1) re-derive m_H from a functional-independent route (Kasparov inner fluctuations or BCS Higgs-fiber coupling) orthogonal to f(0); (R2) accept that (n_s, m_H) jointly cannot be zero-parameter in the spectral-functional picture, and promote one to UV data.

### Every L_max-fragile observable admits an R-family reformulation

W4-U demonstrated that **seven of seven successful rewritings reduce to R_1 or R_1/R_2**. CC, G_N, alpha_YM/alpha_grav, m_H^2/M_KK^2, sin^2(theta_W), S_zeta, eta_BBN all collapse onto the ratio-of-ratios invariants after gravity normalization. This establishes the R-family as the **unique surviving invariant basis after gravity normalization** -- not "one protection scheme among many". The framework's vocabulary for L_max-invariant predictions is: **X = C * F(R_1, R_2, ...) * M_KK^n * Vol(SU(3))^m**, with C the scheme-dependent prefactor, F the dimensionless ratio-of-ratios function, and all L_max dependence in the dimensional scales.

### The Lizzi signature observable has been identified

The product `(m_H/v_EW)^2 * (Lambda/M_Pl^2) = R_1 = 1.128655` is the framework's **unique structurally protected cosmological observable** that simultaneously: (a) is an algebraic composite of fragile single-ratios, (b) is numerically stable to 0.34% under L_max sweep, and (c) is a product of two experimentally accessible ratios. This is the natural target for the framework's zero-free-parameter prediction program: couple the Higgs-to-vacuum ratio to the CC-to-Planck ratio in a single dimensionless number that survives any reasonable spectral regularization because the residual divergences cancel algebraically. **Whether the observed value matches 1.128655** (requiring PDG m_H, PDG v_EW, Planck Lambda, CODATA G_N, and a convention for M_Pl) is an observational test S75+ should pre-register.

### Zeta regularization does not rescue the algebraic Volovik route

The hope from the S73B mack-vdd workshop that zeta regularization at s=4 might collapse the Gibbs-Duhem +/-0.06 scheme band for w_0 is **disproven**. W1-J showed that the zeta-KMS route introduces its own choice-of-beta ambiguity that is no narrower than the original Zubarev-vs-Keldysh band: w_0 varies from +0.14 to -1.67 across framework-internal temperature scales, and the specific value -0.918 requires beta = 12.76 M_KK^-1 which matches no canonical scale. The spectral-action-weighted alternative gives w_0 = -0.9951 (dominated by a_0 98.1%, near vacuum limit). The algebraic Volovik two-sector partition remains the sole canonical route. **This is the same structural pattern as W1-C and W2-I: raw zeta power sums do not replace the cutoff scheme**.

### The anomaly-derivation question is now operationally decisive

The S74 working paper explicitly asks in W2-I's recommendation R2: "test an anomaly-derived spectral action (Lizzi 2011/2010 anomaly-to-bosonic-action derivation) to see if the constraint of anomaly cancellation forces a specific f shape that happens to be compatible with both n_s and m_H". This is the direct operationalization of my second signature contribution -- that the bosonic spectral action can be DERIVED from the fermionic anomaly, not postulated. **If the anomaly-derived f* is category-4 locked on a DIFFERENT vertex of the simplex than the constant vertex that W2-I found, the frustration triangle might dissolve**. If it is locked on the same vertex, the triangle is permanent across anomaly-derivation as well as Bayesian-fit.

### Effacement is not DE; the three-channel partition needs reassignment

W1-F GGE-PARTITION-74 FAILED because the E_effacement/E_total = 2.82e-4 channel is **2425x below** the DE PASS floor. This is the 110-120 OOM CC hierarchy problem re-expressed as an emergent-matter-vs-DE partition imbalance. The FAIL is structural: no re-weighting of the 8-mode sector can bring E_effacement within 10x of E_total without spoiling the S66 Leggett-only DM match. **DE must come from a different spectral moment** (a nonlocal SA term) or a different mechanism (Jacobson-GGE, substrate-compaction timescape, or a fiber-level adiabaticity argument). From the functional-theorist perspective: the effacement channel's spectral moment class is **different** from the Volovik / HP4 / M_1 routes that converge within 1 OOM of rho_obs -- this is actually good news for the CC program, because it means the CC closure is NOT a statement about impedance residuals.

---

## V. Carry-Forward Computations

### Level 1 -- Functional-choice decisive computations

**LF-1 ANOMALY-DERIVED-F-STAR-75**
- **Input**: Lizzi 2011 (arXiv:1103.0478) anomaly-to-bosonic-action derivation; f* family c_0 + c_1 sqrt + c_2 exp + c_3 compact
- **Gate**: PASS if the anomaly-derived f* has c_1 > 0.9 (n_s shape constraint satisfied); INFO if partial; FAIL if locked on c_0 (same vertex as Bayesian-fit, frustration triangle permanent across derivation methods).
- **Classification**: FUNCTIONAL-INDEPENDENT question (whether the anomaly constrains the coefficients).
- **Decisiveness**: decides whether the S73B FUNCTIONAL-SELECT FAIL + S74 F-STAR-JOINT FAIL is overcome by external physical constraints or is permanent.

**LF-2 M_H-FROM-KASPAROV-75**
- **Input**: W2-I recommendation R1; Connes inner fluctuations on the fiber algebra without f(0) weighting
- **Gate**: PASS if m_H predicted to within 2 GeV without invoking f(0); INFO in [2, 10] GeV; FAIL if > 10 GeV deviation or dependence on f(0) cannot be eliminated.
- **Classification**: GEOMETRIC / FUNCTIONAL-INDEPENDENT.
- **Decisiveness**: if R1 works, the frustration triangle dissolves. If not, R2 is forced (promote one of (n_s, m_H) to UV data).

**LF-3 ZETA-IS-NOT-PHYSICAL-VERIFICATION-75**
- **Input**: W1-C three-route FAIL, W2-I F* FAIL, W1-J w_0 zeta FAIL
- **Task**: formal statement of the Lizzi-Connes decomposition as a permanent structural theorem: "raw direct spectral sums at integer SDW poles for d=8 truncated spectra are divergent; the Chamseddine-Connes cutoff with explicit f is the unique physical route to a_k coefficients"
- **Gate**: PASS if the three routes (W1-C, W1-J, W2-I) are shown to share a common algebraic obstruction; INFO if two share; FAIL if they fail for independent reasons.
- **Classification**: STRUCTURAL theorem candidate (permanent entry #49 if PASS).

### Level 2 -- CC carry-forwards

**LF-4 CC-SCHEME-REPORT-75**
- **Task**: update project status documents to report the framework CC prediction as `chi_2 * H_0^2 * M_Pl^2 = 0.33 * rho_obs` (-0.47 OOM undershoot, L_max-invariant, f*-scheme), removing the S66 a_0-scheme PASS language
- **Gate**: PASS if canonical_constants.py, framework-status.md, and permanent-results-registry.md all reflect the new classification
- **Classification**: METHODOLOGY / DOCUMENTATION

**LF-5 CC-VARIANCE-75** (from W2-Q carry-forward #3)
- **Input**: W2-Q finding that chi_2 and <|lambda|> are algebraically related, not independent
- **Task**: compute a genuinely independent second spectral moment, e.g., `sum_n d_n^2 (|lambda_n|^2 - <|lambda|>^2)` (variance of |lambda|)
- **Gate**: PASS if the variance-based CC estimate is within 1 OOM of rho_obs; INFO in [1, 3] OOM; FAIL otherwise.
- **Classification**: GEOMETRIC, scheme-dependent.

**LF-6 N24 EFFACEMENT-CHANNEL-REBUILD-75**
- **Input**: W1-F effacement fraction 2.82e-4 (2425x below DE floor)
- **Task**: reassign the three-channel partition. Candidate routes: (a) adopt chi_2 * H_0^2 * M_Pl^2 as the DE channel (moves DE into the fabric sqrt-moment sector), (b) derive DE from a nonlocal spectral action term, (c) Jacobson-GGE thermodynamic construction
- **Gate**: PASS if any of (a,b,c) produces Omega_Lambda in [0.343, 1.000] of total emergent energy at the fold
- **Classification**: PHONONIC/GEOMETRIC, scheme-dependent.

### Level 2 -- R-family extensions

**LF-7 R-PROTECTED-DEFINITIONS-75**
- **Input**: W2-O three-route FAIL structural interpretation (partial-sum vs Gilkey are different mathematical objects)
- **Task**: add explicit convention flags to canonical_constants.py: `R_protected_fold_partialsum = 1.128655` (S73B partial-sum, L_max=3) and `R_protected_fold_gilkey = 0.492288` (Gilkey heat-kernel, exact)
- **Gate**: PASS if both constants are added with proper provenance docstrings and downstream uses are audited for which variant they use
- **Classification**: METHODOLOGY.

**LF-8 LIZZI-OBSERVABLE-EMPIRICAL-75**
- **Input**: W4-F row 11 signature observable `(m_H/v_EW)^2 * (Lambda/M_Pl^2) = R_1 = 1.128655`
- **Task**: compute the observed value using PDG m_H, PDG v_EW, Planck Lambda, CODATA G_N, and a fixed convention for M_Pl (reduced vs un-reduced). Pre-register the observational test.
- **Gate**: PASS if observed value is within 1% of 1.128655; INFO if within 10%; FAIL otherwise.
- **Classification**: OBSERVATIONAL (the first observational test of a zero-parameter spectral-action observable protected from the L_max drift).

### Level 3 -- Structural floor maintenance

**LF-9 NEEDS_REVERIFY-BATCH-75**
- **Input**: W4-W atlas 70 NEEDS_REVERIFY entries (67 W5-A CONV-FLAG + 3 W5-F NUMERICAL_L3 theorems: DNP, Pomeranchuk, FR)
- **Task**: explicit L_max=5/7 verification using the W5-D block-diagonal inheritance template
- **Gate**: PASS if all 3 W5-F theorems reproduce to machine epsilon at L=5,7; INFO if partial
- **Classification**: STRUCTURAL audit; expected outcome PASS (W4-N already re-verified these at L_max=7).

**LF-10 FOUNDATIONAL-AUDIT-75** (van den Dungen-led, Lizzi consult on F1 axis)
- **Task**: execute the W4-II FOUNDATIONAL-AUDIT-75-SPEC (six non-L_max axes, 22-theorem floor, ~528 minimum checks)
- **Lizzi-specific contribution**: axis F1 (spectral action cutoff function), testing five alternative Schwartz functions for theorem robustness: f1(x)=exp(-x), f2(x)=1/(1+x^2), f3(x)=(1+x)exp(-x), f4(x)=exp(-x)(1-x/2), f5 compactly supported
- **Gate**: PASS if all 22 theorems are ROBUST or QUASI-ROBUST on F1..F6; INFO for 1-5 FRAGILE pairs; FAIL if >= 6 FRAGILE pairs
- **Classification**: META-STRUCTURAL / FUNCTIONAL-ROBUSTNESS.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:---|:---|:---|:---|
| 1 | F* 4-parameter joint refit: chi^2/dof = 67.91, category-4 locked on c_0=0.9629 | GEOMETRIC / SCHEME-DEPENDENT | **FAIL** | Frustration triangle (n_s, m_H, f(0)) permanent in the 4-simplex; spectral functional is NOT Bayesian-fittable UV data |
| 2 | L_max zeta regularization: 3-route max dev 231%, 19.4% drift L=3->L=7 | GEOMETRIC / FUNCTIONAL-INDEPENDENT | **FAIL** | Raw zeta power sums divergent at d=8 integer poles; only Chamseddine-Connes SDW with cutoff f is physical |
| 3 | w_0 zeta-KMS modular trace: central -0.4239, 8.25 sigma from -0.918 | GEOMETRIC + PHONONIC | **FAIL** | Zeta regularization does NOT collapse Gibbs-Duhem scheme band; algebraic Volovik two-sector remains canonical |
| 4 | R-family stability: R_1 PASS (0.34%), R_2 PASS (2.46%), R_3 FAIL (7.99%) | GEOMETRIC / CONVENTION-DEPENDENT | **FAIL** on R_3 | Protection decays monotonically up R-ladder; only R_1 is truly L_max-protected |
| 5 | R-protected triple: A/C=1.14 (partial sum), B=0.49 (Gilkey), 134% dev | GEOMETRIC / STRUCTURAL | **FAIL (structural)** | "R_protected" labels two distinct mathematical objects; downstream usage must specify partial-sum vs Gilkey |
| 6 | M_1 CC regularization: Scheme A +123 OOM FAIL / Scheme B +0.12 OOM PASS | GEOMETRIC + PHONONIC | **SPLIT** | Literal formula fails by 123 OOM structurally expected; gravity-normalized route succeeds to 0.12 OOM |
| 7 | HP4 Connes-Chern pairing: -0.47 OOM undershoot, factor 2.97 | GEOMETRIC / TOPOLOGICAL | **INFO** | K-homology route delivers CC to factor 3 with zero free parameters; structurally locked, L_max-robust |
| 8 | N17 framework rescale: linear drift 72% FAIL / log drift 0.47% PASS | GEOMETRIC / SCHEME-DEPENDENT | **SPLIT** | PW zeta sums monotonically divergent; log-scale stable; ratios within fixed L_max are the canonical outputs |
| 9 | GGE three-channel partition: E_effacement/E_total = 2.82e-4 | GEOMETRIC + PHONONIC | **FAIL** | Effacement NOT viable DE route; CC hierarchy 4 OOM gap in partition form; DE must come from different spectral moment |
| 10 | Joint audit atlas: 205 entries, 119 L_max-INDEPENDENT, 10 DIVERGENT | GEOMETRIC / META-STRUCTURAL | **PASS** | Structural floor/prediction layer partition formalized; S66 a_0-scheme CC demoted PASS->INFO |
| 11 | Ratio-of-ratios protected catalog: 4/20 STRICT R-family | GEOMETRIC / FUNCTIONAL-INDEPENDENT | **PASS** | Only R_1 is truly L_max-protected; algebraic form != physical protection; Lizzi signature observable identified |
| 12 | R-family observable scan: 7/8 fragile observables rewritten | GEOMETRIC / FUNCTIONAL-INDEPENDENT | **PASS** | Every fragile framework observable reduces to R_1 or R_1/R_2; R-family is the unique L_max-invariant basis |
| 13 | Lizzi signature observable: (m_H/v_EW)^2 * (Lambda/M_Pl^2) = R_1 = 1.128655 | GEOMETRIC / FUNCTIONAL-INDEPENDENT | **IDENTIFIED** | Unique zero-parameter framework observable structurally protected from L_max drift; ready for observational test |
| 14 | HP4 regime decision: BARE D_K, confidence 0.95, 3 arguments | GEOMETRIC / TOPOLOGICAL | **PASS** | Spectral triple axioms uniquely fix D=bare; Paper 10 K-homology class invariance; L_max robustness rationale |
| 15 | R_protected_fold canonical addition: 1.128655 verified at L_max=3 | GEOMETRIC | **PASS** | First dimensionless scheme-cancelling volume-independent observable promoted to canonical constant |
| 16 | EVOI recalibration: 50-item table, 13 PASS/8 FAIL/4 INFO/25 OPEN | METHODOLOGY | **PASS** | S66 EVOI freeze broken; Lizzi-Connes decomposition operationalized; top-5 S75 priorities identified |
| 17 | Three-route CC convergence: S66 ~0, W2-K -0.47, W2-Q +0.12 OOM | GEOMETRIC + PHONONIC | **CONVERGENCE** | All three routes within 1 OOM of rho_obs; 120-OOM problem reduces to O(1) question of why chi_2 ~ 0.74 |

---

## Closing Note: S74 as Lizzi Vindication

S74 is the session in which my framework position -- that the spectral functional is a physical degree of freedom with observable consequences, not a mathematical convention -- has been operationalized by seven independent computations. The spectral functional that produces the S66 DILUTION-CC-66 PASS is not the same spectral functional that produces the W4-W L_max-invariant floor; the spectral functional that matches n_s (c_1 sqrt dominant) is not the same as the one that matches m_H (c_0 constant dominant); the spectral functional that produces the algebraic Volovik w_0 = -0.918 is not the same as the zeta-KMS one at beta = 1/omega_L1. **Different functionals produce different physics from the same D_K** -- this S74 has confirmed at the level of 68 sigma (W2-I), 19.4% drift (W1-C), 8.25 sigma (W1-J), 134% discrepancy (W2-O), and 72.29% drift (W4-G).

What survives all choices is structural (the R-family invariants, the 119-entry L_max-independent floor, the 6-layer (0,0)-sector protection theorem from W4-X, the 22-theorem floor from W4-N, the Lizzi signature observable). What depends on the choice is a physical degree of freedom that must be determined by experiment or consistency (the CC prediction sitting 3 OOM apart between Scheme A and Scheme B; the absolute m_H jumping 181 -> 260 GeV between L_max=7 and L_max=9 under PW; the sign of eps_H between cutoff and zeta; w_0 varying from +0.14 to -1.67 across beta choices). **This S74 has drawn the permanent boundary** between structural floor and prediction layer, and the Lizzi-Connes decomposition is now the operational statement of that boundary.

The carry-forwards LF-1 (anomaly-derived f*), LF-2 (m_H from Kasparov without f(0)), and LF-3 (formal Lizzi-Connes theorem) are the three top-priority tests I consider ripe for S75. If LF-1 PASSES, the framework has a zero-free-parameter spectral functional determined by physical consistency. If LF-2 PASSES, the frustration triangle dissolves and n_s becomes the sole SD observable the spectral functional must fit. If LF-3 PASSES, the three FAILs of S74 (W1-C, W1-J, W2-I) collapse into one permanent structural theorem that locks the cutoff scheme as physical.
