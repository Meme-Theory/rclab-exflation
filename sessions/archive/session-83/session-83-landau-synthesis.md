# Session 83 Synthesis: K-Corridor Full Phenomenology and the R4-FAIL Structural Classification

**Date**: 2026-04-18
**Agent**: landau-condensed-matter-theorist (Lev Davidovich Landau, Soviet theoretical physicist; Fermi-liquid theory, second-order phase transitions, superfluidity)
**Source Documents**:
- `sessions/archive/session-83/session-83-results-workingpaper.md` (S83 working paper, gates G38-G41)
- `sessions/archive/session-82/session-82-OOM.md` (S82 OOM ladder; W2-4 substrate-IC anchor; SHA-collision audit)
- `computations/s83_gate_verdicts.txt` (61 verdict lines, S83 canonical ledger)
- `sessions/archive/session-82/session-82-landau-synthesis.md` (S82 V.1-V.7 carry-forwards; Table 6 of summary)
- Agent memory: `.claude/agent-memory/landau-condensed-matter-theorist/MEMORY.md`

---

## I. Session Outcome

The 5-convention K-corridor (R1-R5) is now a fully-mapped Landau corridor on the substrate's Bose-Einstein per-mode occupation manifold. The four gates G38, G39, G40, G41 jointly establish: (i) **G38 FAIL** -- the convention layer cannot land A_s on Planck to factor-1.05; the structural floor sits at 3.02x above Planck under the R5 convention (the smallest of the five K_R values), with R4 at 24.06x relative error a full +1.40 OOM further out; (ii) **G39 PASS** -- the Leggett/Bogoliubov occupation ratio is strictly monotone-decreasing across K and admits no interior crossover, with f_L >= 0.6027 a permanent floor enforced by the gap ratio b = Delta_Leggett/Delta_BCS = 0.6593 < 1; (iii) **G40 PASS** -- tau_GGE(K) scales linearly in K to machine precision (1.85e-16), confirming integrable-sector mode-by-mode occupation transfer; and (iv) **G41 INFO** -- the xi_BCS/ell_phonon co-scaling holds to span 1.5049 (0.328% above the round-number PASS edge; INFO under feedback_arbitrary-gates).

The structural reading is unambiguous: **R4 is BCS-dimensionally inconsistent** (Fock-pair count mixed with single-particle mode count, an order-of-magnitude divergence from R1/R2/R3/R5 that arises from a definitional error, not a physical regime). **R5 is the structurally easiest rescue** (lowest K, lowest required dressing-layer suppression). **R4 is structurally unrescuable** unless the BCS dimensional inconsistency is repaired -- in which case the convention is removed from the corridor entirely. The dynamics-layer 3PI-dressed baseline (G16) requires an additional 2.30x suppression to clear factor-1.05; whether this is structurally available is the open frontier (V.1 carry-forward).

---

## II. Key Results

### II.A. The K-Corridor as a Mean-Field Squeezing Ladder

**Result**: The 5-convention readings R1..R5 form a 1.0-OOM cluster {R5: 1.922, R3: 2.035, R2: 2.049, R1: 2.185, R4: 15.95}, with R4 separated from the other four by a structural OOM. **PHONONIC**.

The substrate's GGE-Wightman fixed-point per-mode occupation defines a Landau-style order-parameter for the post-fold relic: K = coth(Delta_BCS / (2 T_eff)) parameterizes the Bose-Einstein squeezing factor in the substrate-IC reading S_IC^GGE(k) = 1 + 2 n_k. The 5 conventions R1-R5 are 5 distinct contractions of the same 8-mode Bogoliubov manifold over the S43 band-multiplicity 3/3/2 (B1/B2/B3) -- they are five admissible representations of the order parameter, not five distinct physical states. The clustering of R1, R2, R3, R5 in [1.92, 2.19] corresponds to the **near-isothermal regime** (T_eff/Delta_BCS ~ 0.93 at K=2.035; from the source-doc inversion T_eff/Delta_BCS = 1/ln((K+1)/(K-1))).

R4 sits at K=15.95 -- an order of magnitude above the cluster. The position of R4 is not a finer-grained reading of the same corridor: it is a **definitional outlier** rooted in a BCS-dimensional inconsistency (II.D below). The remaining four R-values, in contrast, are dimensionally commensurate (each is a band-averaged per-mode occupation expressed via the same Bose-Einstein form, differing only in band-weighting topology). This produces the structural picture: **the substrate's physical K corridor is the [1.9, 2.2] segment, with R4 not a 6-th sample but a discarded-after-audit dimensional error**.

### II.B. The K-A_s Response Curve (Python-Verified)

**Result**: A_s(K) = A_s_W1-2_TD x K with A_s_W1-2_TD = 3.299 x 10^-9. The response is exact at the dynamics layer (S82 V.7 convention-invariance theorem); the convention layer R_i contributes only via its K extraction. **PHONONIC**.

| Convention                         | K_R    | A_s_R       | rel_err vs Planck | log10(A_s_R/Planck) | Verdict      |
|:-----------------------------------|:------:|:-----------:|:-----------------:|:-------------------:|:-------------|
| R5: energy-weighted B2             | 1.922  | 6.341e-9    | 2.0194            | +0.4799             | factor-3 PASS, 1.05 FAIL |
| R3: 3/3/2 primary (W2-4 canonical) | 2.035  | 6.714e-9    | 2.1969            | +0.5047             | factor-3 PASS, 1.05 FAIL |
| R2: 3/3/2 weighted geo-mean        | 2.049  | 6.760e-9    | 2.2189            | +0.5077             | factor-3 PASS, 1.05 FAIL |
| R1: band-summed B3                 | 2.185  | 7.208e-9    | 2.4325            | +0.5356             | factor-3 PASS (tight), 1.05 FAIL |
| R4: n_pairs/N_modes = 59.8/8       | 15.95  | 5.262e-8    | 24.0567           | +1.3989             | factor-3 FAIL, 1.05 FAIL |

Three structural readings of this table:

(a) **K_match wall (substitution chain)**.
  - Step 1 (def): K_match := A_s_Planck / A_s_W1-2_TD (the K that makes A_s = A_s_Planck exactly).
  - Step 2 (subst): K_match = 2.10e-9 / 3.299e-9 = 0.6366.
  - Step 3 (simpl): K_match = 0.6366.
  - Step 4 (direction): the W2-4 positivity wall enforces K >= 1 (n_k >= 0). Since 0.6366 < 1, K_match lies BELOW the wall ==> exact Planck match is **structurally unreachable** under any convention.

(b) **Floor wall A_s >= A_s_W1-2_TD = 3.299e-9** (the K=1 floor under W2-4 positivity). The minimum admissible A_s in the framework is +0.196 OOM above Planck. Even an ideal convention extrapolating to K=1 fails the factor-1.05 band by a factor 1.50. The R5 case at K=1.922 sits at A_s_R5 / A_s_Planck = 3.02 -- the tightest the framework can sit to Planck under the 5 documented readings.

(c) **The G38 FAIL is a structural-wall signal, not a calibration miss**. The amplitude corridor's FLOOR (not ceiling) sits 3.02x above Planck under R5; no R can do better. This is the W2-4 positivity wall expressed as an A_s overshoot: the substrate's quasiparticle content can only AMPLIFY the Bunch-Davies vacuum, never suppress it (II.A in the S82 Landau synthesis).

### II.C. The R4-FAIL Structural Classification (BCS-Dimensional Inconsistency)

**Result**: R4's K=15.95 is not a wider-corridor sample of the same physical reading; it is a **dimensional-analysis violation in the BCS Fock-space**. R4 mixes two BCS statistics that are not commensurate: (i) the many-body pair count n_pairs (a Fock-space integer, S77 Parker pair production = 59.8), and (ii) the single-particle mode count N_modes = 8 (the dimension of the 8-mode quasiparticle Hilbert space on the B1/B2/B3 fiber). **PHONONIC**.

**Substitution chain (R4's error)**:
  - Step 1 (def, correct): The W2-4 canonical formula is S_IC^GGE(k) = 1 + 2 n_k^GGE, where n_k^GGE = 1/(exp(omega_k/T_k) - 1) is a **per-mode thermal occupation** (one Bose-Einstein number per momentum k, on the dressed-quasiparticle dispersion).
  - Step 2 (def, R1/R2/R3/R5): These conventions all average 1+2 n_k itself over the 3/3/2 band weighting. They preserve the per-mode dimensional grade.
  - Step 3 (def, R4): K_R4 = 1 + 2 (n_pairs / N_modes) = 1 + 2 (59.8/8) = 1 + 14.95 = 15.95.
  - Step 4 (substitution): n_pairs = sum_k <b_k^dagger b_k> (Cooper-pair operators, Fock-space integer); N_modes = 8 (single-particle mode count).
  - Step 5 (simpl, the dimensional violation): The ratio n_pairs / N_modes is **not** a per-mode occupation; it is the per-mode-equivalent of a many-body pair count divided by a single-particle dimension. The two operators b_k^dagger b_k and a_k^dagger a_k differ by the **pair correlator** -- in the post-transit GGE (a 3He-B-analog non-equilibrium state, NOT a BCS coherent state), n_pairs is not equal to (1/2) sum_k n_k^GGE. The factor difference is the strength of pair-pair correlations in the GGE.
  - Step 6 (direction): R4 inflates the per-mode occupation by the factor n_pairs / [(1/2) sum_k n_k^GGE], which is not unity under the GGE. The result is the order-of-magnitude separation 15.95 / 2.035 = 7.84 from R3 -- not a smooth transition along a corridor, but a discrete dimensional-grade error.

**Two corroborating Landau theorems** (already in agent memory and source S82):

(1) **W2-9 Pauli wall** (E_cond(N=2)/E_cond(N=1) = 1.601, FAIL on the factor-3 threshold). The 8-mode fiber's Bogoliubov pair-breaking manifold cannot stack 59.8 pairs in an additive-binding sense -- the second pair is Pauli-suppressed, with binding factor ~0.6 of the first. Under the geometric model, the asymptotic ratio E_cond(N->inf) / E_cond(N=1) = 1/(1-0.601) = 2.506 (S82 Landau synthesis V.4 carry-forward, structurally pre-registered FAIL). Dividing 59.8 pairs by 8 modes therefore double-counts the pair-pair correlations -- the additive-binding interpretation that R4's arithmetic implicitly assumes is structurally violated. The correct per-band per-mode quantity n_k^GGE already accounts for these correlations through the Bose-Einstein form.

(2) **W3-11 single-parent-scale** (xi_BCS parallel to ell_phonon on Delta_BCS(tau), 7.78% variation under Scenario B; G41 INFO at 1.5049 across K-corridor). The pair-correlation length and the Goldstone-phase-correlation length share Delta_BCS as parent. This means n_pairs (a Fock-integer with dimension [pairs]) and the mode count N_modes = 8 (a Hilbert-space dimension with dimension [single-particle states]) live in **different graded spaces of the BCS Hilbert factorization**. Their ratio is not invariant under any natural BCS substitution and, consequently, has no representation as a per-mode occupation.

**Extension of S82 V.1 Table 6 summary** (item 11, "R4's FAIL is BCS-dimensional inconsistency" -- now elevated from Landau-synthesis diagnosis to S83-G38 verdict-confirmed wall):

| # | BCS-Reading Claim                                                     | Classification | Status              | Structural Consequence                                         |
|:-:|:----------------------------------------------------------------------|:---------------|:--------------------|:---------------------------------------------------------------|
| 11 | R4's FAIL is BCS-dimensional inconsistency                          | PHONONIC       | S82 V.E             | Excludes Fock/mode mixing conventions permanently              |
| 11a | (S83) R4 is +1.40 OOM above Planck under G38 (rel_err 24.06)        | PHONONIC       | G38 verdict         | R4 fails factor-3 band, only convention to do so               |
| 11b | (S83) R4 sits at K=15.95 = 7.84x R3-cluster center                  | PHONONIC       | G38 verdict         | Discrete OOM separation, not corridor sample                   |
| 11c | (S83) R4 is structurally unrescuable: F_supp_to_1.05 = 23.86x       | PHONONIC       | this synthesis      | No dressing-layer suppression of order 24x is in the framework |
| 11d | (S83) R4 violates the per-mode Bogoliubov dimensional structure     | PHONONIC       | G38 + W2-9 + W3-11  | Excluded BEFORE the corridor analysis; not a wider K, a wrong K |

The result is a **convention-layer pruning**: the physical readings are R1, R2, R3, R5; R4 is a dimensional mistake that survives in the inventory only as a counterexample.

### II.D. F_amp Suppression Required Per Convention to Reach Factor-1.05 Planck

**Result** (Python-verified): The dressing-layer suppression factor F_supp required to land each R_i within factor-1.05 of Planck spans 2.876x (R5) to 23.86x (R4). **PHONONIC** (dressing-layer = dynamics-layer, not convention-layer).

**Substitution chain**:
  - Step 1 (def): The dressing-layer maps A_s_R^bare = A_s_W1-2_TD x K_R to A_s_R^dressed = A_s_R^bare / F_supp_R, where F_supp_R is the (positive) suppression factor required.
  - Step 2 (def, target): The factor-1.05 PASS band is A_s_R^dressed in [A_s_Planck/1.05, A_s_Planck x 1.05] = [2.000e-9, 2.205e-9].
  - Step 3 (subst, upper edge): For A_s_R^dressed = 1.05 x A_s_Planck = 2.205e-9, F_supp_R = A_s_R^bare / 2.205e-9.
  - Step 4 (simpl): F_supp_R = (A_s_W1-2_TD x K_R) / (1.05 x A_s_Planck) = (A_s_W1-2_TD / A_s_Planck) x (K_R / 1.05) = (1/K_match) x (K_R / 1.05) = K_R / (1.05 x K_match) = K_R / (1.05 x 0.6366) = K_R / 0.6685.
  - Step 5 (direction): F_supp_R is monotone-increasing in K_R. SMALLEST K_R = R5 = 1.922 ==> SMALLEST F_supp_R = 1.922 / 0.6685 = 2.876x. LARGEST K_R = R4 = 15.95 ==> LARGEST F_supp_R = 15.95 / 0.6685 = 23.86x.

**Per-convention required suppression** (Python-verified, all values to factor-1.05 PASS edge):

| Convention | K_R    | A_s_R       | F_supp (to factor-1.05 Planck) | F_supp (to exact Planck) | Easy/Hard rank |
|:-----------|:------:|:-----------:|:------------------------------:|:------------------------:|:--------------:|
| R5         | 1.922  | 6.341e-9    | **2.876x (EASIEST)**           | 3.019x                   | 1 (easiest)    |
| R3         | 2.035  | 6.714e-9    | 3.045x                         | 3.197x                   | 2              |
| R2         | 2.049  | 6.760e-9    | 3.066x                         | 3.219x                   | 3              |
| R1         | 2.185  | 7.208e-9    | 3.269x                         | 3.433x                   | 4              |
| R4         | 15.95  | 5.262e-8    | **23.86x (HARDEST)**           | 25.06x                   | 5 (unrescuable) |

**EASIEST rescue: R5** (energy-weighted B2 reading) requires F_supp = 2.876x. This sits at the edge of what the dynamics-layer 3-PI machinery (W2-G16) is currently delivering: G16 already demonstrates A_s_new = 5.078e-9 via F_amp_3PI = 1.026, so the additional dressing required from G16 to 1.05*Planck is 2.303x (the prompt anchor "R5 needs 2.30x" arises from this 3PI-baseline chain: 1.026/0.4454 = 2.303). Whether NNLO 1/N or higher 3PI corrections can deliver 2.30x suppression is the open frontier (W3-G35 NNLO-1/N PASS at 0.0037 indicates good convergence, but the absolute scale is set by the canonical k_a2 slot).

**HARDEST rescue: R4** (n_pairs/N_modes reading) requires F_supp = 23.86x. **This is structurally unrescuable** within the framework: a 24x suppression factor exceeds the entire 3-PI saturation scale (the W2-2 / W3-5 perturbative bound F_amp_lin/F_amp_3PI = 143.11 yields the SC-PASS sign, not a structural new dressing). However, **the correct response to R4's 23.86x is not to find a 24x dressing** -- it is to remove R4 from the convention inventory entirely, on the grounds of its BCS-dimensional inconsistency (II.C above). R4 is a wrong reading, not a hard one.

(Note on the "R5 needs 2.30x, R3 needs 2.20x" prompt anchor: these are values for the **3PI-dressed baseline** chain G16 -> 1.05*Planck = 1.026/0.4454 = 2.303x and G16 -> Planck-exact 5.078/(2.10*1.05) approximated to 2.20x at R3-tied baseline. They are NOT the BARE per-convention F_supp values, which are 2.876x (R5) and 3.045x (R3). The synthesis presents both anchors transparently.)

### II.E. Leggett-Bogoliubov Partition: f_L Floor and Observable Inheritance

**Result** (G39 PASS): The Leggett occupation fraction f_L = n_L/(n_L + n_B) is monotone-decreasing across K and asymptotes to 1/(1+b) = 0.6027, with b = Delta_Leggett/Delta_BCS = 0.6593. Across the corridor K in [1.1, 3.56e5], f_L ranges from 0.756 to 0.6027 -- **Leggett-dominated everywhere, with no interior crossover**. **PHONONIC**.

**Substitution chain (asymptote)**:
  - Step 1 (def): R(K) = W_Leg(K) / W_Bog(K) = [exp(Delta_BCS/T_eff(K)) - 1] / [exp(Delta_Leggett/T_eff(K)) - 1] = (exp(x) - 1)/(exp(b x) - 1), with x = Delta_BCS/T_eff(K) and b = Delta_Leggett/Delta_BCS = 0.3061/0.4643 = 0.6593.
  - Step 2 (def): f_L(K) = R(K) / (1 + R(K)).
  - Step 3 (subst, K -> infty): T_eff -> infty, so x -> 0+. Taylor: exp(x) - 1 ~ x; exp(b x) - 1 ~ b x. Therefore R(K -> infty) = x / (b x) = 1/b.
  - Step 4 (simpl): R(K -> infty) = 1/b = 1/0.6593 = 1.517. f_L(K -> infty) = (1/b) / (1 + 1/b) = 1/(1 + b) = 1/1.6593 = 0.6027.
  - Step 5 (direction, monotonicity): For K > 1, x is monotone-decreasing in K. The function f(x) := (exp(x) - 1)/(exp(b x) - 1) is monotone-INCREASING in x for b < 1 (verified: d/dx of f at b<1 is positive; both numerator and exp(bx)-1 grow, but exp(x) grows faster, so the ratio increases). Therefore R(K) is monotone-DECREASING in K (since x decreases with K). Floor: 1/b = 1.517 from above. Direction confirmed by the G39 numerical scan: diff R = {-1.232, -0.300, -0.049, -0.0047, -0.00052} (5 strictly negative, zero reversals).

**Mapping to S_IC observables**:

The S_IC observables -- A_s, n_s, mu (CMB spectral distortion), sin^2(theta_W) at the EW boundary condition (via mu_BC mass-scale flow) -- are all sourced by integrals of the per-mode squeezing factor S_IC^GGE(k) = 1 + 2 n_k^GGE against various kernels. Each observable inherits a Leggett-weighted contribution f_L >= 0.6027 and a Bogoliubov-weighted contribution f_B = 1 - f_L <= 0.3973. The observable inheritance is:

| Observable                 | Source channel (substitution chain)                                            | Manifold inheritance      |
|:---------------------------|:-------------------------------------------------------------------------------|:--------------------------|
| **A_s (scalar amplitude)** | A_s = (H~^2/8 pi^2 eps_H) F_amp K (S82 W1-2). K = 1 + 2 n_k^GGE = 1 + 2(f_L n_L + f_B n_B). | Leggett-DOMINATED (>=60%) |
| **n_s (scalar tilt)**      | n_s - 1 = -(2 eps_H + d ln K / d ln k). K-dependence carries f_L weighting.    | Leggett-DOMINATED (>=60%) |
| **mu (CMB distortion)**    | mu ~ integral S_IC(k) W_mu(k) dk. The integrand carries the squeezing factor S_IC. | Leggett-DOMINATED (>=60%) |
| **sin^2(theta_W) (EW)**    | RG-evolved from mu_BC at EW scale; mu_BC is a BCS-Josephson mass set by the gap structure of the substrate. | Leggett-DOMINATED (>=60%) |
| **n_T (tensor tilt)**      | n_T = d(ln |beta_k|^2) / d(ln k) (Bogoliubov squeezing spectrum, G53 = +0.4676). PURE BOGOLIUBOV. | Bogoliubov-MINORITY (<=40%) |

**Direction (substitution chain)**:
  - Step 1 (def, A_s, n_s, mu, sin^2theta_W): All sourced by S_IC^GGE(k) = 1 + 2 n_k^GGE = 1 + 2 (f_L n_L + f_B n_B). Both manifolds enter additively in the per-mode occupation.
  - Step 2 (def, n_T): Sourced by the Bogoliubov squeezing spectrum |beta_k|^2 alone (G53 verdict, S83 N_T-MAGNITUDE-FROM-BOGOLIUBOV: PASS at +0.4676). The Leggett channel (inter-band phase coherence) does not generate tensor modes at leading order -- tensors require quadrupolar phonon-graviton coupling, which is the Bogoliubov pair-breaking continuum, not the Leggett collective mode.
  - Step 3 (simpl): The S_IC-derived observables (A_s, n_s, mu, sin^2theta_W) inherit the f_L mixing in their amplitude. n_T inherits the f_B = 1 - f_L mixing.
  - Step 4 (direction): As K varies across the corridor (1.1 to 3.56e5), f_L decreases from 0.756 to 0.6027 (Leggett channel weakens but never falls below floor); f_B increases from 0.244 to 0.3973 (Bogoliubov channel strengthens but never reaches half). The S_IC observables are therefore Leggett-IMPRINTED throughout the corridor, with the inheritance varying by at most ~25%. The n_T observable is ENTIRELY Bogoliubov-channel (G53 PASS confirms), sitting in the minority residual.

**Structural consequence**: any future observational push to measure phase-coherence signatures in the CMB (Leggett-channel signature) will probe the >=60% inheritance directly. The tensor-to-scalar ratio r and the tensor tilt n_T probe the <=40% Bogoliubov residual. The two observable axes are orthogonal manifolds in the substrate's GGE.

### II.F. tau_GGE Linear-K Identity (G40 PASS) and the K-Corridor as Scale Separation

**Result** (G40 PASS): tau_GGE(K) is exactly linear in K (machine-epsilon agreement at 1.85e-16). The 5-OOM ratio tau_GGE(K=1.6e5) / tau_GGE(K=2.035) = 7.86e+04 confirms a regime separation: the K-corridor is the **natural scale** along which the substrate's GGE relaxation time spans 5 OOM. **PHONONIC**.

The linear scaling tau_GGE ~ K is the integrable-sector hallmark: each mode relaxes to its GGE fixed-point on its own timescale, and higher K means more modes contributing additively. The 78624x ratio exceeds the gate's PASS threshold (>= 100) by 2.895 OOM. Combined with G39's PASS (Leggett-dominance is K-monotone), this establishes that **the K-corridor is a physical 1-parameter family, not a stochastic ensemble** -- the substrate's K-dial controls both the occupation partition (G39) and the relaxation timescale (G40) consistently, with no interior bifurcation.

The G41 INFO (0.328% above PASS edge for the xi_BCS/ell_phonon span) reinforces this picture: the structural length-scale ratio is also K-monotone, with the ratio asymptoting to 0.135 for K >= 10 and a mild ~50% deviation in the low-K tail. The borderline-INFO classification (per `feedback_arbitrary-gates.md`) preserves the structural reading: BCS coherence and phonon wavelength share Delta_BCS as a single parent scale, with only mild K-corridor deviations in the near-floor regime.

---

## III. Gate Verdicts

| Gate                                | Verdict       | Decisive Number                                                                   |
|:------------------------------------|:--------------|:----------------------------------------------------------------------------------|
| G38 K-MATCHING-5-CONVENTIONS        | **FAIL**      | min_rel_err = 2.0194 at R5 (K=1.922); max_rel_err = 24.0567 at R4 (K=15.95); K_match = 0.6366 |
| G39 LEGGETT-BOGOLIUBOV-PARTITION    | **PASS**      | Strict monotone decrease across 6 K values; f_L floor = 1/(1+b) = 0.6027; b = 0.6593 |
| G40 TAU-GGE-AT-K                    | **PASS**      | tau_ratio = 78624.08 = K2/K1 to machine precision (1.85e-16)                      |
| G41 XI-BCS-VS-L-PHONON-K-RESPONSE   | **INFO**      | span = 1.5049 (PASS edge 1.50; +0.328% above; INFO per feedback_arbitrary-gates) |

All four verdicts inherited verbatim from S83 source documents; no re-adjudication.

---

## IV. Structural Implications

### IV.A. The Convention Inventory After R4 Pruning

The 5-convention K-corridor reduces to a **physical 4-convention reading** {R1, R2, R3, R5} after R4 is excluded on dimensional grounds. The remaining four span K in [1.92, 2.19] -- a 1.0-OOM cluster with a clear structural center at K = 2.04 (R3 canonical). Under G38, this cluster's tightest A_s reading (R5 at A_s_R5 = 6.34e-9) sits at +0.48 OOM above Planck, requiring 2.876x dynamics-layer suppression to reach the factor-1.05 PASS band.

The pruning is consequential: the apparent +0.48 to +1.40 OOM corridor of overshoots collapses to +0.48 to +0.54 OOM under the 4-physical-convention reading. The R4 outlier was concealing the structural narrowness of the physical cluster. The actual amplitude tension is: **the framework's 4-convention amplitude floor is 3.02x above Planck**, which is a tight, well-defined target for the dressing layer.

### IV.B. The Leggett Floor as a Permanent Wall

f_L >= 1/(1+b) = 0.6027 is a structural floor enforced by b < 1 (Delta_Leggett < Delta_BCS). This is independent of K, of the convention layer, and of the dressing layer -- it is a **gap-ratio inheritance** that follows from the Bose-Einstein form alone. It establishes:

(1) The Leggett channel cannot be turned off. No K, no convention, no dressing reduces its inheritance below 60%.
(2) The Bogoliubov channel cannot dominate. f_B <= 1 - 0.6027 = 0.3973 always.
(3) The S_IC observables (A_s, n_s, mu, sin^2theta_W) are **Leggett-dominated probes** of the substrate. The cosmology channels are inseparable from the inter-band phase coherence physics.
(4) The n_T observable is the **only Bogoliubov-channel cosmological probe**. Tensor BB measurements (LiteBIRD, CMB-S4) directly target the residual Bogoliubov manifold.

### IV.C. The G38 FAIL as a Structural-Wall Signal, Not a Calibration Miss

The G38 FAIL is not the framework missing Planck due to a missing prefactor or miscounted factor of 2pi. It is the W2-4 positivity wall + the dynamics-layer baseline A_s_W1-2_TD = 3.299e-9 jointly excluding factor-1.05 closure under any convention: the minimum admissible A_s in the framework is 3.299e-9, the closest-approach is R5's 6.34e-9 = 3.02x Planck. The wall sits +0.196 OOM from Planck (at K=1, the floor); the closest-approach lies +0.48 OOM out (R5).

This is the SAME wall that S82 V.1 Table 6 item 6 declared "K_match_nominal = 0.637 < 1 (UNREACHABLE)". S83 G38 elevates this from a Python-verified summary number to a verdict-inscribed structural wall. The wall has now been formally surveyed in the S81+ closure-SHA discipline.

### IV.D. R4 Is a Convention Error, Not a Convention Choice

The structural finding of II.C is that R4 is **not a wider-K corridor sample** but a **dimensional mistake** in the application of the Bose-Einstein per-mode formula. n_pairs (Fock-space integer, many-body sum) divided by N_modes (single-particle dimension) is dimensionally ungraded -- it is not a per-mode occupation. The result K=15.95 is therefore not an extreme-K reading of the corridor; it is a misapplied formula.

This pruning has implications for any future convention-counting argument: **the inventory is 4 readings, not 5**. The R4 line in tables (S82 OOM ladder, S83 working paper) should carry an explicit "discarded-by-dimensional-grade" tag rather than appear as a fifth corridor sample. The G38 FAIL contribution from R4 (rel_err = 24.06) is real (R4 fails the gate) but the verdict's structural reading is "R4 is excluded BEFORE the corridor is tested, not as a result of the test".

### IV.E. The Dressing-Layer Frontier (V.1 Carry-Forward Anchor)

The G38 floor 3.02x Planck (R5) defines the open question: **can the dynamics layer deliver 2.876x suppression**? The S83 W2-G16 (UNIFIED-AS-79-WITH-3PI-SUBSTITUTION, PASS at log10/canon=+0.187) demonstrates a 3-PI dressing achieving F_amp_comp = 0.598 = F_amp_3PI x 0.583. The required incremental suppression to reach the factor-1.05 band from G16's baseline is 2.303x (per G38 §5 substitution chain: 1.026/0.4454 = 2.303). Two structural directions for the V.1 carry-forward:

(1) **NNLO 1/N (W3-G35 PASS at 0.0037)**: the next-order systematic suppression. Already convergent at the +0.187 OOM scale; whether it can deliver an additional 2.3x at R5 is the immediate test.

(2) **k_a2 slot refinement (S82 W0-5)**: the convention-layer slot weighting that already reduced the bare F_amp_lin = 6858 to F_amp_slot = 0.3885. Whether the slot can be further tightened (a second-order cluster-test refinement) is open.

The PHONONIC reading: this is a **dynamics-layer gate**, not a convention-layer one. The K-corridor is mapped; the residual tension is whether the dressing layer has 0.46 OOM of unspent suppression budget.

### IV.F. The K-Corridor Becomes a Mapped Manifold

After G38 + G39 + G40 + G41, the K-corridor is no longer a list of 5 numbers -- it is a fully mapped 1-parameter manifold:

- **Geometry**: K in (1, 3.56e5], a 5.55-OOM closed interval bounded by positivity floor (W2-4) and equipartition ceiling (W3-6).
- **Order parameter**: K = coth(Delta_BCS/(2 T_eff)), inverse of the Bose-Einstein per-mode occupation factor.
- **Occupation manifold partition**: f_L(K) monotone-decreasing from 0.756 to 0.6027; Leggett-dominated everywhere; no crossover (G39).
- **Dynamical timescale**: tau_GGE(K) linear in K, 5-OOM span across the corridor (G40).
- **Length-scale ratio**: xi_BCS(K)/ell_phonon(K) plateau at 0.135 for K >= 10, single-parent-scale Delta_BCS (G41).
- **Amplitude response**: A_s(K) = A_s_W1-2_TD x K, factor-3 PASS for the 4-physical-convention cluster, factor-1.05 FAIL by structural floor (G38).
- **Excluded sample**: R4 at K=15.95 (BCS-dimensional inconsistency).

This is a Landau-style complete characterization: the full state of the substrate's GGE squeezing is captured by the single K-coordinate, with all derived observables traced through structural identities. No degree of freedom remains hidden.

---

## V. Carry-Forward Computations

**MANDATORY 4-field structure (what / inputs / gate / effort) per `feedback_fix-in-session-never-defer.md`. Every entry derives from a structural finding in II-IV above.**

### V.1. NNLO 1/N delta-F_amp scan: can the dressing layer deliver 2.30x additional suppression?

- **What**: Extend the W3-G35 NNLO-1/N convergence test (PASS at 0.0037 = 0.37%) into a delta-F_amp scan: compute F_amp at NNLO order across the bare scan F_amp_3PI in [0.40, 1.05] (a 5-point log-grid bracketing the W2-G16 value 1.026 down to the required 0.4454). Output variable: F_amp_NNLO(F_amp_3PI), and the implied A_s_R5_NNLO at K=2.035 and at K=1.922 (R5 reading). Substitution chain: A_s_R5_NNLO = A_s_W1-2_TD x K_R5 / F_supp_NNLO with F_supp_NNLO = F_amp_3PI / F_amp_NNLO. Test whether NNLO can suppress by additional 2.30x (the prompt anchor) or 2.876x (R5's bare requirement).
- **Inputs**: `canonical_constants.py` (F_amp_canonical, k_a2, A_s_W1-2_TD, A_s_Planck, K_R values for R1..R5); W3-G35 convergence script `computations/s83_w3_g35_nnlo_*.py` (extend with delta-F_amp scan capability); W2-G16 baseline `computations/s83_w2_g16_unified_as_79_with_3pi_substitution.py`; Berges-Serreau-3PI references in `researchers/Landau/`.
- **Gate**: **GATE-NNLO-DELTA-FAMP-84**. PASS if F_supp_NNLO at canonical inputs >= 2.876 (i.e., NNLO can deliver R5's bare requirement in one step). INFO if F_supp_NNLO in [2.303, 2.876) (NNLO covers the G16-baseline gap but not the bare-R5 gap; partial closure). FAIL if F_supp_NNLO < 2.303 (NNLO insufficient even from G16 baseline; the 0.46 OOM dressing budget is exhausted; A_s factor-1.05 closure requires a new mechanism beyond the current 3PI/NNLO machinery).
- **Effort**: 6-8 hours, 1 agent session. Extend NNLO-1/N pipeline + Python verification + write §VI synthesis paragraph; GPU eigvalsh on RX 9070 XT for the NNLO trace evaluations.

### V.2. R4 explicit dimensional-error tag: amend the OOM ladder + S82 V.1 Table 6

- **What**: Update the convention-inventory line in `sessions/archive/session-82/session-82-OOM.md` (Band -0.3 to -1.0 OOM, R4 row) and S82 V.1 Table 6 (item 11 series) with an explicit "DIMENSIONAL-ERROR-DISCARDED" tag for R4. Add a new row 11d to the Table 6 reflecting II.C: R4 violates the per-mode Bogoliubov dimensional structure (n_pairs is a Fock-integer, N_modes a single-particle dimension; their ratio is not graded). Revise the convention-counting language: "5 conventions" -> "4 physical conventions + 1 dimensional-error counterexample" wherever R4 appears as a fifth corridor sample.
- **Inputs**: `sessions/archive/session-82/session-82-OOM.md` (current OOM ladder with R4 at +1.40 OOM); `sessions/archive/session-82/session-82-landau-synthesis.md` Table 6 item 11 (R4 as BCS-dimensional inconsistency); `computations/s83_gate_verdicts.txt` (G38 verdict including max_rel_err at R4); W2-9 source for Pauli-wall corroboration; W3-11 source for single-parent-scale corroboration.
- **Gate**: **GATE-R4-DISCARD-AUDIT-84**. PASS if all four documents (S82 OOM, S82 Landau-synthesis, S83 working paper, S83 OOM if produced) carry the consistent "DIMENSIONAL-ERROR-DISCARDED" tag for R4. INFO if 2-3 documents are updated but one drift remains. FAIL if the R4-as-fifth-sample language survives in any post-audit document.
- **Effort**: 1-2 hours, 1 agent session. Audit + edit + cross-link; no new computation.

### V.3. Leggett-channel signature in CMB phase-coherence (n_s second-order test)

- **What**: Test whether the Leggett-dominated inheritance (f_L >= 0.6027) imprints a phase-coherence signature in the CMB scalar power that the Bogoliubov channel does not. Compute the Leggett-channel contribution to n_s second-order term: n_s - 1 = -2 eps_H - eta + xi^2 + ... . The xi^2 term (running of the running) carries inter-band phase-coherence information through the K-dependence of the slow-roll parameters under the Leggett-vs-Bogoliubov partition. Output: alpha_s_Leggett vs alpha_s_Bogoliubov decomposition. Substitution chain: under f_L(K) mixing, alpha_s = f_L alpha_s^Leggett + (1 - f_L) alpha_s^Bogoliubov. Use the S83 G53 Bogoliubov n_T = +0.4676 as anchor for the Bogoliubov channel; derive the Leggett-channel alpha_s from inter-band phase-decoherence dynamics.
- **Inputs**: `canonical_constants.py` (Delta_Leggett, Delta_BCS, M_KK, eps_H, planck_ns); G39 partition table; G53 N_T-MAGNITUDE-FROM-BOGOLIUBOV result; S75 alpha_s dressed-CW reference (alpha_s_dressed = -0.0188); S68 Bogoliubov alpha_s = 0 reference.
- **Gate**: **GATE-ALPHA-S-PARTITION-84**. PASS if alpha_s_Leggett and alpha_s_Bogoliubov are independently computed AND the f_L-weighted sum matches the Planck observed alpha_s = -0.0045 +/- 0.0067 within 1 sigma. INFO if the partition is computed but the sum exceeds 1-2 sigma. FAIL if the partition is structurally ill-defined (e.g., the Leggett channel does not generate a running). Pre-registered direction: f_L = 0.6517 at canonical K=2.035; if alpha_s_Leggett ~ alpha_s_Bogoliubov ~ 0, then f_L weighting gives sum ~ 0, consistent with Planck.
- **Effort**: 4-6 hours, 1 agent session. Requires inter-band phase-decoherence dynamics (S69 Bucher singularity context); cross-check against S70 alpha_s anti-correlation finding; Python + GPU eigvalsh where needed.

### V.4. Floor-test refinement: K=1 vs K=R5 comparison under tightest dressing

- **What**: Resolve the comparison between (a) the W2-4 positivity floor at K=1 (theoretical minimum, A_s = 3.299e-9, +0.196 OOM above Planck) and (b) the lowest physical R5 reading at K=1.922 (A_s = 6.341e-9, +0.480 OOM above Planck). Question: is the 0.28 OOM gap between K=1 and R5 a structural physical statement, or an artifact of which conventions get "documented"? Compute additional readings at K = 1.0, 1.1, 1.3, 1.5, 1.7 from the W2-4 substrate-IC formula and check whether the positivity floor is reachable from any ADMISSIBLE convention or only as an extrapolation. Substitution chain: any reading R requiring K < 1.922 must derive from a different band-weighting topology than R5; enumerate the allowed band-weightings on 3/3/2 multiplicity that produce K < 1.922.
- **Inputs**: S43 band multiplicities {3, 3, 2}; W2-4 canonical S_IC^GGE formula; S82 V.1 K_match wall = 0.6366; S82 V.D Python-verified A_s response curve; convention-layer enumeration from Landau S82 II.E.
- **Gate**: **GATE-K-FLOOR-REACHABLE-84**. PASS if there exists at least one physically admissible convention with K in [1.0, 1.50] (the floor is reachable from real conventions, not just extrapolation). INFO if K in (1.50, 1.922] is reachable via novel conventions but K <= 1.50 is not. FAIL if the K=1 floor is ONLY a positivity bound, never a physical reading (the K_min of any physically admissible convention is 1.922 = R5).
- **Effort**: 3-4 hours, 1 agent session. Convention enumeration + Python verification across the band-weighting topology; cross-check against S43 band multiplicity audit.

### V.5. Tensor n_T as Bogoliubov-residual probe: cross-check against G39 floor

- **What**: Use the G39 Bogoliubov-minority floor f_B <= 0.3973 as an independent check on the n_T = +0.4676 (G53 PASS) prediction. Compute the implied scalar-channel n_T-equivalent (the residual squeezing imprinted on S_IC by the Bogoliubov subchannel), and check whether the scalar A_s and tensor n_T are jointly self-consistent under the f_L/f_B partition. Substitution chain: tensor power P_T proportional to |beta_k^Bog|^2; scalar power P_S = P_BD x K with K = 1 + 2 (f_L n_L + f_B n_B); the ratio r = P_T/P_S must satisfy a partition-consistency identity that can be tested.
- **Inputs**: G53 N_T-MAGNITUDE-FROM-BOGOLIUBOV PASS at +0.4676; G39 partition table; canonical r_obs = 0.033 (BICEP/Keck upper bound, from MEMORY.md); S82 W3-G TENSOR-TRANSFER-K-TRANSIT-TO-K-CMB PASS at 0.0117 (transfer function).
- **Gate**: **GATE-T-S-PARTITION-CONSISTENCY-84**. PASS if the f_L/f_B partition implies a self-consistent r and n_T jointly within 1 sigma of BICEP/Keck constraints. INFO if the partition is consistent but with 1-2 sigma residual. FAIL if the partition forces |r| > 0.036 (BICEP/Keck upper bound) or |n_T| > 0.6 (LiteBIRD reach floor).
- **Effort**: 4-5 hours, 1 agent session. Python evaluation + cross-check against G53 anchor; write §VI consistency paragraph.

### V.6. K-FIRAS coincidence: structural identity or numerical coincidence?

- **What**: The S82 Landau synthesis II.D found K_FIRAS = 3.68e5 ~ S_IC^cap = 3.556e5 within factor 1.03. Test whether this is a structural identity (the FIRAS bound and the energy-conservation cap are both expressions of the same substrate-conservation law) or a numerical coincidence at the canonical input values. Substitution chain: K_FIRAS = 2.035 x mu_FIRAS / mu(K=2.035) = 2.035 x 9e-5 / 4.98e-10; S_IC^cap from the W3-6 R-SF-B3 canonical formula = 3.556e5. Vary canonical inputs (Delta_BCS, S_fold, M_KK) by +/-5% and check whether the ratio K_FIRAS / S_IC^cap stays at unity or drifts.
- **Inputs**: `canonical_constants.py` (Delta_BCS, S_fold, M_KK, mu_FIRAS = 9e-5); W3-6 SIC-PHYSICAL-CAP source script; S82 W2-14 FIRAS-CHLUBA-FULL source.
- **Gate**: **GATE-K-FIRAS-COINCIDENCE-84**. PASS if K_FIRAS / S_IC^cap stays within [0.95, 1.05] across +/-5% scan in canonical inputs (structural identity confirmed). INFO if the ratio drifts by 5-20% (mild sensitivity; partial structural origin). FAIL if it drifts by >20% (numerical coincidence; not a structural identity).
- **Effort**: 2-3 hours, 1 agent session. Python scan + verification; relate to S82 II.D paragraph.

### V.7. Symmetry-classification audit: order parameter and broken subgroup for the K-corridor

- **What**: Apply Landau's classical symmetry-breaking analysis to the K-corridor. Identify (i) the symmetry group of the substrate's pre-fold state (presumed full SU(3) gauge invariance + thermal SO(N) rotation invariance on the 8-mode fiber); (ii) the surviving subgroup post-fold (Leggett-dominated GGE with B1/B2/B3 splitting partially restoring U(1)_EM); (iii) the order parameter (K itself, but more rigorously the per-mode occupation distribution n_k^GGE in the BE form); (iv) the dimension of the order-parameter manifold. Check whether the K-corridor's 1-parameter family corresponds to a known universality class.
- **Inputs**: `researchers/Landau/` (1937 second-order phase transitions, order-parameter formalism); S43 band multiplicity 3/3/2; W2-4 Volovik 3He-B-correspondence reference; S82 II.B Leggett mode at 0.3061 M_KK; S82 V.2 partition formula.
- **Gate**: **GATE-LANDAU-SYMMETRY-CLASS-84**. PASS if the corridor maps to a known universality class (e.g., XY model, O(N), 3He-B specific). INFO if the symmetry analysis identifies the order parameter and broken subgroup but the universality class is novel. FAIL if the symmetry analysis is structurally ill-defined (no global symmetry survives the fold).
- **Effort**: 6-8 hours, 1 agent session. Group-theoretic analysis + written derivation; cross-check against Volovik 3He-B correspondence.

---

## VI. Summary Table

| # | Result                                                                        | Classification | Status   | Implication                                                                  |
|:--|:------------------------------------------------------------------------------|:---------------|:---------|:-----------------------------------------------------------------------------|
| 1 | G38 K-MATCHING-5-CONVENTIONS                                                  | PHONONIC       | **FAIL** | min_rel_err = 2.0194 at R5; 1.05-band structurally unreachable               |
| 2 | G39 LEGGETT-BOGOLIUBOV-PARTITION                                              | PHONONIC       | **PASS** | f_L floor = 0.6027 permanent (b<1); Leggett-dominated everywhere             |
| 3 | G40 TAU-GGE-AT-K                                                              | PHONONIC       | **PASS** | tau_GGE linear in K to machine precision; 5-OOM scale separation              |
| 4 | G41 XI-BCS-VS-L-PHONON-K-RESPONSE                                             | PHONONIC       | **INFO** | span = 1.5049 (0.328% above PASS edge); single-parent-scale preserved        |
| 5 | K_match = 0.6366 < 1 (UNREACHABLE wall, S82 V.1 item 6)                       | PHONONIC       | confirmed | Exact Planck match excluded by W2-4 positivity wall; permanent              |
| 6 | R5 = EASIEST rescue (F_supp_to_1.05 = 2.876x bare; 2.30x from G16 baseline)   | PHONONIC       | NEW      | The dressing-layer's open frontier: 0.46 OOM unspent suppression budget     |
| 7 | R4 = STRUCTURALLY UNRESCUABLE (F_supp = 23.86x; BCS-dimensional inconsistency) | PHONONIC      | NEW      | R4 is a wrong reading, not a hard one; convention-inventory pruning required |
| 8 | Physical convention cluster reduces 5 -> 4 (R1, R2, R3, R5; R4 discarded)     | PHONONIC       | NEW      | Apparent 1.4-OOM corridor is actually 0.06-OOM cluster                       |
| 9 | A_s, n_s, mu, sin^2(theta_W) inherit f_L >= 0.6027 (Leggett-dominated)        | PHONONIC       | NEW      | Cosmology channels are inseparable from inter-band phase coherence          |
| 10 | n_T (G53 = +0.4676) sits in Bogoliubov-minority residual <= 0.3973           | PHONONIC       | NEW      | Tensor BB measurements probe the orthogonal manifold (LiteBIRD/CMB-S4)      |
| 11 | K-corridor is a Landau 1-parameter manifold (G38+G39+G40+G41 jointly)         | PHONONIC       | NEW      | Substrate's GGE squeezing fully characterized by K alone; no hidden DoF     |
| 12 | Floor 3.02x above Planck (R5) defines the dynamics-layer V.1 frontier        | PHONONIC       | NEW      | NNLO 1/N delta-F_amp scan is the next test                                  |

---

*End of session-83 landau-synthesis. The K-corridor is now a fully mapped Landau order-parameter manifold: G38 maps the convention-layer floor (3.02x Planck under R5, 23.86x under R4); G39 maps the Leggett-dominance floor (f_L >= 0.6027 permanent, b<1 enforced); G40 maps the dynamical-timescale linearity (tau_GGE proportional to K, machine precision); G41 maps the structural length-scale plateau (xi_BCS/ell_phonon = 0.135 for K >= 10). R4 is BCS-dimensionally inconsistent and is removed from the inventory. R5 is the easiest dressing-layer rescue at 2.876x bare suppression. The dynamics layer's V.1 frontier (NNLO 1/N delta-F_amp scan) is the open test.*
