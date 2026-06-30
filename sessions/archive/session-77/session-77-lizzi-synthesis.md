# Session 77 Synthesis: Spectral Functional Analysis

**Date**: 2026-04-13
**Agent**: lizzi-spectral-functional-theorist
**Source**: `sessions/archive/session-77/session-77-results-workingpaper.md` (30 computations, 3 waves)

---

## Session Outcome

Session 77 delivered twelve permanent theorems and closed six mechanisms, but the session-defining result is not in any gate verdict. It is in the structural clarification of what the spectral moments a_n actually ARE in this framework, and how the choice of spectral functional propagates to every observable that depends on absolute moment values.

Three results form an interlocking complex that reshapes the spectral functional program:

1. The identity chi_2 = <sqrt(x)>_{d^2} (W1-D PASS) establishes that the CC concentration parameter is the spectral action evaluated with f(x) = sqrt(x) -- the non-perturbative component of f*.
2. The SA truncation analysis (W2-K INFO) proves that the canonical a_n are spectral zeta moments (sum PW * |lambda|^{-2n}), NOT Seeley-DeWitt heat kernel coefficients. Using them as HK coefficients gives values 9 OOM off.
3. The a_4 Gilkey decomposition (W3-I PASS) shows R^2 dominance at 101.6%, extracts f_conv^{zeta} = f_conv(SDW)/R_1, and confirms the zeta regularization shift is only 0.053 OOM.

The session also discovered a normalization error in the A_s chain (W2-A) that inverts the sign of the gap: P_zeta at the pivot is 9.5 OOM ABOVE Planck, not 5.75 OOM below. This transforms the A_s problem from "how to amplify" into "how to suppress" -- a qualitatively different question whose answer depends critically on the pre-fold vacuum state, which is itself a spectral functional question (what state does the fold phase transition select?).

---

## Key Results

### 1. chi_2 = <sqrt(x)>_{d^2}: The CC as a Spectral Functional Evaluation (W1-D PASS)

**What was computed.** The spectral sum S_f = (1/N) * sum_j d_j * f(lambda_j^2/lambda_max^2) was evaluated for four spectral functionals at the fold, and compared with chi_2 = 0.741419.

**Result.** chi_2 is EXACTLY the spectral action per mode evaluated with f(x) = sqrt(x):

  chi_2 = (1/N) * sum_j d_j * sqrt(lambda_j^2 / lambda_max^2) = <sqrt(x)>_{d^2}

This is an algebraic identity, confirmed to machine precision at all L_max tested. The physical f* = 0.912*sqrt(x) + 0.088*exp(-x) reproduces chi_2 to 0.95%, with the 0.95% residual exactly accountable as the 8.8% exp component pulling toward <exp(-x)> = 0.572.

**Spectral functional interpretation.** This result has a precise meaning in the spectral functional program:

(a) **chi_2 IS a spectral functional evaluation.** It is the spectral action density with f(x) = sqrt(x), normalized by mode count and cutoff. The CC concentration parameter is not an arbitrary statistic of the spectrum -- it is the spectral action at a SPECIFIC functional. This functional is precisely the dominant (91.2%) component of f*.

(b) **f(x) = sqrt(x) is NOT a Chamseddine-Connes cutoff function.** The standard CC framework assumes f(x) with f(0) finite and rapid decay at infinity, generating the HK expansion. sqrt(x) diverges at infinity and has f(0) = 0. It is the signature of a non-perturbative spectral functional -- exactly the character we identified for f* in S72.

(c) **HP4 CC and SA CC use different spectral data.** W1-D confirms: <sqrt(x)> is the first moment of the spectral distribution, while a_0 is the zeroth moment (eigenvalue count). These are algebraically independent -- HP4 probes the spectral SHAPE, the SA CC probes the spectral VOLUME. The f*-weighted spectral moments M_1^{f*} = 7.34 (positive power) vs a_2/a_0 = 0.43 (inverse power) are manifestly different objects.

**FUNCTIONAL-INDEPENDENCE classification:** chi_2 is FUNCTIONAL-DEPENDENT but in a precisely controlled way. It is the output of a specific spectral functional (sqrt). Its value changes if you evaluate with a different f(x): sharp cutoff gives 1.000, exp(-x/0.088) gives 0.005, f* gives 0.732. The fact that chi_2 ~ Omega_Lambda with f(x) = sqrt(x) is a statement about the spectrum, not a coincidence.

### 2. Canonical a_n Are Zeta Moments, Not HK Coefficients (W2-K INFO)

**What was computed.** The full spectral action Tr(f(D^2/Lambda^2)) was computed as an exact finite sum over all eigenvalues at Lambda = 5.033 M_KK, then compared to the Taylor expansion using power sum moments M_{2k} = sum PW * mu^{2k}.

**Result.** The canonical a_n = sum PW * |lambda|^{-2n} (computed throughout the project since S20) are spectral zeta moments. Using them as heat kernel coefficients (a_0*Lambda^8 + a_2*Lambda^6 + a_4*Lambda^4) gives values 9 orders of magnitude off the correct spectral action. The correct Seeley-DeWitt comparison uses the Taylor expansion of the test function at the eigenvalues: S_SDW = sum_j d_j * [1 - mu_j^2/Lambda^2 + mu_j^4/(2*Lambda^4) - ...].

**Spectral functional implications.** This is a critical clarification for the entire program:

(a) **The zeta spectral action S_zeta = zeta_D(0) = a_4 uses the ZETA moments directly.** For the zeta scheme, the canonical a_n ARE the natural objects. S_zeta = a_4 by definition. The statement "a_4 is the gauge action" is correct in the zeta scheme because we are evaluating S_zeta = sum PW * |lambda|^{-4}, which is precisely a_4.

(b) **The cutoff spectral action Tr(f(D^2/Lambda^2)) requires the HK expansion with DIFFERENT coefficients.** The power sums M_{2k} = sum PW * mu^{2k} (positive powers) enter the cutoff action, not the inverse-power zeta moments a_n. The 3-term Taylor truncation captures 96.2% of the a_4-level contribution at Lambda = 5.033, with residual 3.76%. The 5-term truncation reaches 0.003%.

(c) **The dictionary between zeta moments and cutoff moments must be systematized.** Throughout the project, a_n has been used interchangeably for both. W2-K reveals this conflation is harmless for RATIOS (where both sets give the same answer to ~0.14%) but catastrophic for absolute values (9 OOM discrepancy). This vindicates the S75 permanent theorem (ZETA-NOT-PHYSICAL): absolute spectral moments are scheme-dependent, ratios are scheme-independent.

**SCHEME-DEPENDENT quantities affected:** Every absolute value -- a_0, a_2, a_4 individually -- is a zeta moment. Using these as HK coefficients in the cutoff scheme introduces systematic error. The R-protected ratio R_1 = a_0*a_4/a_2^2 is IMMUNE (same ratio in both conventions to 0.14%).

### 3. a_4 Gilkey Decomposition: R^2 Dominance and f_conv^{zeta} (W3-I PASS)

**What was computed.** The Gilkey decomposition of the Seeley-DeWitt a_4 coefficient into curvature invariants (R^2, |Ric|^2, |Riem|^2), and the zeta-regularized conversion factor f_conv^{zeta}.

**Result.** R^2 contributes 101.6% of the a_4 Gilkey coefficient, with |Ric|^2 and |Riem|^2 providing only -1.6% combined. The dominance is structural: the Lichnerowicz endomorphism E = R/4 from D^2 generates 84% of the R^2 coefficient (420/500). The Jensen deformation barely breaks the Einstein condition (0.93% deviation from R/d = |Ric|^2/R).

**The key formula.** f_conv^{zeta} = f_conv(SDW) / R_1, where R_1 = a_0*a_4/a_2^2 = 1.1287. This gives:

  f_conv^{zeta} = 2.258e-10 (log10 = -9.646)

vs

  f_conv(SDW) = 2.549e-10 (log10 = -9.594)

The shift is 0.053 OOM (12% reduction). In the zeta scheme, f_conv is SMALLER, meaning the A_s gap is marginally WIDER: 3.36 + 0.053 = 3.41 OOM in the zeta scheme vs 3.36 OOM in the SDW scheme.

**Spectral functional interpretation.** The formula f_conv^{zeta} = f_conv(SDW)/R_1 is exact and has a clean algebraic origin:
- In the SDW (cutoff) scheme: the spectral action uses all three moments a_0, a_2, a_4 independently.
- In the zeta scheme: S_zeta = a_4, so the CC term (a_0) is absent. Newton's constant still comes from a_2 (scheme-independent, since G_N is determined by the Einstein-Hilbert term). But the normalization changes because the total action is a_4 not a_0*Lambda^4 + a_2*Lambda^2 + a_4*Lambda^0.
- The ratio R_1 encodes the difference: it measures how far the spectral moment sequence deviates from a geometric sequence. R_1 = 1 would mean the zeta and SDW schemes give the same f_conv. R_1 = 1.129 means the zeta scheme underestimates f_conv by 13%.

This 13% is negligible compared to the 3.36 OOM gap. The A_s problem is structural across all spectral functionals.

### 4. chi_2 Nonlocality: Four Proofs and Weinberg Evasion (W3-K INFO)

**What was computed.** Whether chi_2 = Tr(|D_K|)/(N * ||D_K||) can be represented as a local operator trace.

**Result.** chi_2 is PROVEN NONLOCAL by four independent arguments:

| Argument | Method | Why it excludes locality |
|:---------|:-------|:------------------------|
| Spectral projection | |D| requires sign(D), a degree-(N-1) polynomial | Full-spectrum-dependent, not low-degree curvature form |
| Moment parity | Tr(|D|) = Tr((D^2)^{1/2}); HK generates only even powers | sqrt is not polynomial; M_1 not in span{M_{2k}} |
| Shape dependence | Same-area flat tori: chi_2 differs by 4.9% | chi_2 detects global shape invisible to SDW coefficients |
| Zeta classification | chi_2 = zeta_D(-1) value; SDW = pole residues | zeta values at non-pole points are algebraically independent |

**Spectral functional interpretation.** This theorem has direct consequences for the CC problem:

(a) **Weinberg evasion.** Weinberg's 1989 no-go assumes rho_vac = sum of Lambda^4 * (local operator traces). Each sector contributes at the cutoff scale, requiring 10^{-120} cancellation. chi_2 evades this by being (i) bounded in [0,1] regardless of UV cutoff, (ii) UV-insensitive (8.5% drift from L=3 to L=9), (iii) a ratio that cancels Weyl-divergent growth.

(b) **Connection to the zeta spectral action.** Argument (D) classifies chi_2 as a zeta function VALUE at a non-pole point (s = -1/2 in the zeta_D convention). The SDW coefficients are RESIDUES at poles. These are algebraically independent objects. This is precisely the distinction between S_zeta = zeta_D(0) = a_4 and S_cutoff = Tr(f(D^2/Lambda^2)) = f_0*a_0 + f_2*a_2 + f_4*a_4 + ... The zeta value at a non-pole point carries global spectral information that no finite number of HK coefficients can reproduce.

(c) **Moment parity as a spectral functional statement.** The fact that chi_2 = <|lambda|>/lambda_max involves an ODD power of |lambda| while all SDW moments are EVEN powers (lambda^{-2k}) is the algebraic root of nonlocality. This is exactly the distinction between f(x) = sqrt(x) (odd power, generates chi_2) and f(x) = polynomial (even powers, generates SDW). The spectral functional sqrt is structurally different from any cutoff function -- it probes the spectrum's first moment rather than its inverse moments.

**FUNCTIONAL-INDEPENDENCE classification:** chi_2 nonlocality is STRUCTURAL (functional-independent). It holds for any spectral triple, regardless of which spectral functional you evaluate. The nonlocality is a property of the INVARIANT chi_2, not of the functional used to compute it.

### 5. f_conv(f*) Identity and Spectral Functional as Physical Degree of Freedom (W2-C PASS)

**What was computed.** The conversion factor f_conv under f*-weighted spectral measure.

**Result.** f_conv(f*)/f_conv(SDW) = (a_0/M_0(f*))^2 = (6440/4821.1)^2 = 1.784, an exact algebraic identity. f_conv(f*) = 4.547e-10, shifting the A_s gap by +0.25 OOM.

**Spectral functional interpretation.** The identity f_conv(f*)/f_conv(SDW) = (a_0/M_0(f*))^2 reveals the spectral functional as operating through a SINGLE number: the effective mode count M_0(f*). Since f*(x) < 1 for all x in (0,1), the f*-weighted spectral measure assigns less weight to each mode than the flat (SDW) measure. Fewer effective modes means less spectral dilution of the a_2 projection, hence larger f_conv.

The structural formula:

  f_conv = pi^4 / (9216 * M_0^2)

shows that f_conv depends on a_0 (mode count) and NOTHING ELSE -- the a_2 dependence cancels algebraically in the fixed-M_Pl normalization. The spectral functional enters ONLY through M_0(f*), the effective spectral weight. This confirms the S76 workshop finding that CC and A_s are siblings sharing the extensive parent a_0: f_conv ~ 1/a_0^2, and the spectral functional modulates a_0 through M_0(f*).

**SCHEME-DEPENDENT.** f_conv is maximally scheme-dependent: it varies by 1.784x between SDW and f*, and would vary more with other functionals. R_1(f*) = 1.116 vs R_1(SDW) = 1.129 (1.1% suppression), confirming R-protection is preserved under f*-weighting.

### 6. R-Protection Universality on Three Lie Groups (W3-M INFO)

**What was computed.** R_1 = a_0*a_4/a_2^2 on SU(3), SU(4), Sp(2) at multiple L_max.

**Result.** All three groups show R_1 drift below 5%:
- SU(3) (A_2, rank 2): 1.02% drift L=3 to L=7
- SU(4) (A_3, rank 3): 0.37% drift L=3 to L=5
- Sp(2) (C_2, rank 2): 0.69% drift L=3 to L=5

Higher rank gives better protection, consistent with O(L^{-rank}) pre-asymptotic corrections.

**Spectral functional interpretation.** R-protection is the statement that alpha_0 + alpha_4 = 2*alpha_2 (Weyl exponents sum correctly to make alpha_net = 0 in R_1). This is a structural theorem for ANY compact simple Lie group with bi-invariant metric, proven in S76 WS5. The S77 computation is the first numerical verification on groups other than SU(3).

The spectral functional reading: R_1 is an INTENSIVE quantity in the sense of the S76 intensive/extensive partition. It survives the thermodynamic limit (L_max -> infinity). The spectral functional choice affects EXTENSIVE quantities (a_0, a_2, a_4 individually) but cannot alter intensive ratios. This is why R_1 = a_0*a_4/a_2^2 is the natural observable: it is invariant under the spectral functional diffeomorphism.

The rank dependence (better protection at higher rank) suggests a large-N limit where R_1 -> 1 and the spectral moment sequence becomes geometric. SU(4) at R_1 = 1.026 is already close.

### 7. The Dilaton-Higgs Connection in Light of S77

The S77 results reshape the Higgs-dilaton connection established in the S72 spectral functional fit:

(a) **m_H is maximally scheme-dependent** (S75 permanent result, [100.5, 138.5] GeV range). The S77 a_4 Gilkey decomposition shows WHY: the Higgs quartic coupling lambda_H ~ a_4/a_2^2 in the cutoff scheme but lambda_H ~ a_4 alone in the zeta scheme. Since R^2 contributes 101.6% of a_4 and the Lichnerowicz endomorphism dominates (84%), the Higgs mass is controlled by the curvature channel of D_K^2, which is sensitive to the regularization.

(b) **f* is 91.2% sqrt.** The chi_2 = <sqrt(x)> identity means the CC channel and the Higgs channel are both controlled by the sqrt component of f*. The 8.8% exp component enters only at the 0.95% level for chi_2 and at the ~5% level for m_H (through f*(0) = t* = 0.088 setting the quartic coupling). The dilaton degree of freedom t* is the single empirical coupling (Lambda_QCD analog from S76) that tunes the Higgs mass independently of the CC.

(c) **The modulus stabilization problem (W1-A FAIL) creates a new connection.** If BCS dressing is required to stabilize tau, and BCS pairs 8 modes out of 155,984, then the stabilized tau_equil determines a_2(tau), a_4(tau), and hence m_H. The Higgs mass becomes sensitive to the BCS gap through the modulus dynamics. This is a new coupling between the condensed-matter sector and particle physics, mediated by the spectral action.

---

## Gate Verdicts

| Gate ID | Verdict | Value | FI/SD | Note |
|:--------|:--------|:------|:------|:-----|
| S77-A1-EQUIL-TAU | FAIL | BCS 72x too weak, no V_eff minimum | SD | V_bare is scheme-dependent; V_BCS is FI |
| S77-A2-BOG-FRIED-AS | INFO | A_s = 9.11e-13, gap = 3.36 OOM | SD | f_conv(SDW), invalidated by W2-A |
| S77-A3-MU-EFF-B2 | FAIL | mu_eff = 8.58e-4 < 0.001 | FI | Bottleneck migration is spectral, not functional |
| S77-A4-DIRECT-SUM-FSTAR | **PASS** | chi_2 = <sqrt(x)>, |delta| = 0.0095 | SD | chi_2 value is f-dependent; identity is FI |
| S77-B1-NPIVOT | INFO | N_pivot = 3.12, k = 14.31 M_KK (subhorizon) | FI | Normalization is geometric, not functional |
| S77-B2-P-FRIEDMANN | INFO | p_S75 = 1.69 != p_cosmo = 0.58 | FI | Category clarification, not scheme-dependent |
| S77-B3-FCONV-FSTAR | **PASS** | ratio = 1.784 = (a_0/M_0(f*))^2 | SD | Maximally scheme-dependent |
| S77-B4-LR-THRESHOLD | FAIL | sin^2 = -0.308 (wrong sign) | FI | Dynkin obstruction is representation-theoretic |
| S77-B5-ROUTE-C | PASS | Direct gap = 0.034 OOM confirmed | SD | Which gap definition = which scheme |
| S77-B6-R1-TRAJECTORY | INFO | R_1 monotone increasing, not stationary | FI | R_1 variation is geometric (tau-dependent) |
| S77-B7-MEAN-EIGEN | INFO | <|lam|> = 1.581, dS/dt* = +764 | FI | Spectral statistics are scheme-independent |
| S77-B8-BCS-TIMING | **PASS** | t_BCS/dt_transit in [102, 160] | FI | Timescale hierarchy is scheme-independent |
| S77-B9-FRICTION | INFO | N_osc = 0, F = 60.33, exp(-F) = 6.3e-27 | SD | F depends on V(tau), which depends on f |
| S77-B10-V-TAU-VALID | INFO | tau_max_reliable = 2.0 (direct) | FI | Jensen metric is algebraically exact |
| S77-B11-SA-TRUNC | INFO | Residual = 3.76% of a_4 term | SD | Truncation error IS the functional choice |
| S77-C1-CMPP-TURN | INFO | Type D at all tau, transit-invariant | FI | Algebraic type is curvature classification |
| S77-C2-MULTI-CELL | **PASS** | E = 29.42, 1.47 OOM | SD | E depends on E_J/E_C, which involves a_k |
| S77-C3-SPECTRAL-Z | FAIL | z_fw/z_GR = 1.014, 0.006 OOM | SD | alpha depends on a_4/a_2, hence on f |
| S77-C4-A2-OVERSHOOT | INFO | |delta_G/G| = 0.841 at tau = 1.614 | FI | a_2(tau) is eigenvalue sum, scheme-independent |
| S77-C5-HESSIAN-OVERSHOOT | **PASS** | 35/35 negative at tau = 1.614 | FI | Ridge topology is scheme-independent |
| S77-C6-MODE-THRESHOLD | **PASS** | Delta_2/Delta_3 = 1.0 exactly | FI | Dynkin index ratio, permanent |
| S77-C7-GGE-OCC | FAIL | delta_chi_2 = 9.63e-6 (150,000x too small) | FI | 8/408M modes, arithmetic constraint |
| S77-C8-DW-GW | FAIL | Omega_GW = 3.84e-15, 33 OOM below LISA | SD | sigma_wall from GL, bias from J_C2 |
| S77-C9-A4-GILKEY | **PASS** | R^2 = 101.6%, f_conv^{zeta} = 2.258e-10 | SD | f_conv^{zeta} vs f_conv(SDW) by factor 1/R_1 |
| S77-C10-YUKAWA-PMNS | INFO (NULL) | All cross-sector Y = 0 exactly | FI | Block-diagonality + J-conjugation |
| S77-D1-WEINBERG-LOCAL | INFO (PROVEN) | chi_2 nonlocal, 4 proofs | FI | Nonlocality is a property of chi_2, not of f |
| S77-D2-EPOCH-CONV | INFO | a* = 1.097, 1.4 Gyr future | SD | a* depends on chi_2, hence on f |
| S77-D3-R1-UNIVERSAL | INFO | Drift < 5% on SU(3), SU(4), Sp(2) | FI | R-protection is structural theorem |
| S77-D4-PATI-SALAM | INFO | No intermediate symmetry, tau > 0 | FI | Rank obstruction, group-theoretic |
| S77-D5-TRANS-PBH | INFO | F_amp = 6858, gap = -9.5 OOM (overproduction) | SD | P_dS depends on H/M_Pl, normalization |

**Classification totals**: 16 FUNCTIONAL-INDEPENDENT, 14 SCHEME-DEPENDENT.

---

## Structural Implications

### The Spectral Functional Hierarchy Clarified

S77 crystallizes the three-level structure of spectral functional dependence:

**Level 1 (Structural-FI):** Results that hold for ALL spectral functionals, with no exceptions.
- R_1 protection universality (0.37-1.02% drift across groups)
- chi_2 nonlocality (four-proof theorem)
- Block-diagonality and J-conjugation (exact zeros)
- Jensen ridge topology (35/35 negative through overshoot)
- Dynkin index ratios (Delta_2/Delta_3 = 1 exactly)
- BCS timing hierarchy (t_BCS/dt_transit > 100)
- a_0(tau) = const (topological)
- SM gauge group uniqueness for tau > 0

**Level 2 (Values-SD, Ratios-FI):** Results where the QUALITATIVE structure is functional-independent but QUANTITATIVE values shift between schemes.
- A_s gap: 3.36 OOM (SDW), 3.41 OOM (zeta), ~3.10 OOM (f*). All give gaps. None close it.
- f_conv: 2.549e-10 (SDW), 2.258e-10 (zeta), 4.547e-10 (f*). Same OOM, different values.
- chi_2 = 0.741 (SDW/identity), 0.732 (f*-weighted). The 0.95% difference is the exp component.
- Multi-cell enhancement E = 29.42 (depends on E_J/E_C, which involves a_k ratios)

**Level 3 (Maximally-SD):** Results where the spectral functional choice determines the answer qualitatively.
- Whether chi_2 or chi_2/3 identifies with Omega_Lambda (the factor-3 Friedmann normalization)
- The A_s sign (overproduction vs underproduction depends on normalization AND functional)
- m_H: [100.5, 138.5] GeV range spans the functional space (S75 permanent)
- Post-fold spectral action direction (sqrt/f* monotonically increasing; exp/compact decreasing)

### The zeta Moments vs HK Coefficients Dictionary

W2-K's finding that canonical a_n are zeta moments, not HK coefficients, has cascade implications:

1. **For S_zeta = a_4**: The zeta spectral action uses a_4 directly. No dictionary problem. The CC is absent (a_0 does not enter). This is the original Lizzi insight: S_zeta avoids the CC term structurally.

2. **For S_cutoff = Tr(f(D^2/Lambda^2))**: The HK expansion requires the TAYLOR moments M_{2k} = sum PW * mu^{2k} (positive powers), not the zeta moments a_n = sum PW * |mu|^{-2n} (negative powers). The Taylor moments converge well (3.76% residual at 3 terms, 0.003% at 5 terms for Lambda = 5.033). But using a_n in their place gives 9 OOM errors.

3. **For f***: The non-perturbative character of sqrt(x) means the HK expansion does not converge for f*. The full spectral sum must be used. This was known since S72 but W2-K makes the failure mode quantitative.

4. **For ratios**: The ratio R_1 = a_0*a_4/a_2^2 is the SAME whether computed from zeta moments or Taylor moments (to 0.14%). Ratios are the ONLY safe observables for cross-scheme comparison.

### The chi_2 Route C and Spectral Functional Selection

The chain W1-D + W3-K + W3-L establishes:
- chi_2 = <sqrt(x)>_{d^2} is the spectral action with f = sqrt (W1-D)
- chi_2 is provably nonlocal, evading Weinberg (W3-K)
- Omega_Lambda = chi_2 at a* = 1.097, 1.4 Gyr hence (W3-L)
- The analytical formula (a*/a_eq)^3 = chi_2/(1-chi_2) makes this structural (W3-L)

From the spectral functional perspective, Route C identifies the CC with a SPECIFIC spectral functional evaluation: f(x) = sqrt(x). This is NOT the Chamseddine-Connes cutoff action (which gives the CC from f_0*a_0*Lambda^4, a completely different quantity). Route C says: the CC is not the zeroth moment a_0 weighted by Lambda^4 (a local, UV-divergent, scheme-dependent disaster). The CC is the first moment M_1 normalized by N*lambda_max (a global, UV-bounded, scheme-dependent but convergent quantity).

The critical unresolved question: is the factor-3 Friedmann normalization physical? chi_2/Omega_Lambda = 1.082 (gap 0.034 OOM, direct). chi_2/(3*Omega_Lambda) = 0.361 (gap 0.44 OOM, Route C standard). The factor 3 comes from rho_crit = 3*H_0^2*M_Pl^2. Whether this 3 enters depends on whether chi_2 identifies with rho_Lambda/rho_crit (= Omega_Lambda) or with rho_Lambda (in units of some spectral scale). This is a spectral functional question: which normalization of the spectral action gives the vacuum energy density?

---

## Carry-Forward Computations for S78

### From the spectral functional perspective, the top priorities:

1. **SDW vs Zeta Moment Dictionary** (from W2-K Open Question 10). Systematize the relationship between zeta moments a_n = sum |lambda|^{-2n} and Taylor moments M_{2k} = sum lambda^{2k} throughout the codebase. Identify every computation that used a_n as HK coefficients and assess whether the ratio approximation (0.14%) is adequate or a recomputation with Taylor moments is needed.

2. **chi_2 L_max Convergence and Spectral Functional** (from W3-L Open Question 6). Does chi_2(L_max -> infinity) converge to Omega_Lambda = 0.685, or to some other value? The current drift is ~5% per decade in L. If it converges to 0.685, the direct conjecture chi_2 = Omega_Lambda is confirmed without the factor-3 ambiguity. If it converges to ~0.741, the factor-3 question remains open. Compute chi_2 at L_max = {10, 12, 15} to characterize the asymptotic behavior.

3. **Pre-fold Vacuum State as Spectral Functional Selection** (from W3-O Open Question 2). The A_s gap inversion (overproduction by 9.5 OOM) means the pre-fold vacuum state must provide O(10^{9.5}) suppression. Different spectral functionals in the fermionic sector (cutoff vs zeta vs anomaly-derived) select different vacuum states. The anomaly-derived spectral action (my arXiv:1103.0478) provides a fermionic path integral that constrains the allowed vacuum states. Compute the Bogoliubov transformation from pre-fold to post-fold vacuum using the anomaly-induced effective action.

4. **f_conv^{anomaly}** (analogous to W3-I f_conv^{zeta}). In the anomaly-derived scheme, the bosonic action arises from the fermionic anomaly. The anomaly coefficients are determined by the Dirac operator spectrum but with different weights than either the cutoff or zeta scheme. Compute f_conv in the anomaly scheme and compare with SDW (2.549e-10) and zeta (2.258e-10).

5. **a_4 R^2 Dominance Under Different Functionals.** W3-I showed R^2 dominance at 101.6% in the Gilkey decomposition. Does this persist under f*? Under the zeta scheme? The endomorphism fraction (84%) is fixed by the operator D_K^2, but the relative weighting of curvature invariants could shift with the functional. This affects m_H through the quartic coupling.

---

## Summary Table

| Result | Gate | FI/SD | CC Relevance | Key Spectral Functional Insight |
|:-------|:-----|:------|:-------------|:-------------------------------|
| chi_2 = <sqrt(x)>_{d^2} | PASS | SD (value), FI (identity) | CC = f(sqrt) evaluation of spectral action | Non-perturbative functional, not CC cutoff |
| chi_2 nonlocality | PROVEN | FI | Evades Weinberg no-go | zeta value vs pole residue distinction |
| a_n = zeta moments, not HK | INFO | FI (identity) | a_0 in SA is zeta, not cutoff CC | 9 OOM error if conflated; ratios safe |
| f_conv(f*)/f_conv(SDW) = 1.784 | PASS | SD | 0.25 OOM gap closure | f enters through M_0(f*) only |
| f_conv^{zeta} = f_conv(SDW)/R_1 | PASS | SD | 0.053 OOM widening | Zeta marginally worse for A_s |
| a_4 R^2 dominance 101.6% | PASS | FI (dominance), SD (value) | Gauge sector insensitive to higher curv. | Lichnerowicz endomorphism controls 84% |
| R-protection on SU(3), SU(4), Sp(2) | INFO | FI | Intensive observable survives all f | O(L^{-rank}) convergence, universal |
| Epoch convergence a* = 1.097 | INFO | SD | chi_2 = Omega_Lambda at a* | Structural: (a*/a_eq)^3 = chi_2/(1-chi_2) |
| A_s gap inversion (-9.5 OOM) | INFO | SD | Overproduction, not underproduction | Pre-fold vacuum = functional selection |
| SA truncation: 3.76% residual | INFO | SD | SDW adequate for ratios (0.14%) | Zeta vs cutoff moment dictionary needed |
| BCS timing: t/dt_transit > 100 | PASS | FI | Gap absent during squeeze | Scheme-independent timescale hierarchy |
| sin^2(theta_W) = -0.308 | FAIL | FI | L-R threshold permanently closed | Dynkin obstruction, not functional choice |
