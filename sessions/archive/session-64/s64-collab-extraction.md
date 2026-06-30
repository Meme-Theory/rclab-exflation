# S64 Collab + Investigation Extraction for S65 Planning

**Generated**: 2026-04-02
**Sources**: 7 collaborative reviews (Kitaev, Einstein, Tesla, Phonon-First, Mack, Baptista, Kaku) + 1 investigation (Phonon-Strings)

---

## Computation Suggestions (Deduplicated)

### CONVERGENT (proposed by 2+ reviewers)

| # | Title | Proposers | Input | Output | Gate | Priority |
|:--|:------|:----------|:------|:-------|:-----|:---------|
| C1 | Volovik B/F spectral asymmetry: split a_0 by KO grading | Phonon-First (S3-1), Kaku (III.E, #7), Einstein (Q3) | D_K eigenvalues + degeneracies + real structure J at fold | a_0^B, a_0^F, ratio (a_0^B - a_0^F)/a_0; IR B/F splitting | SPECTRAL-ASYMMETRY-65: PASS if ratio < 0.01 (>2 OOM reduction). Kaku gate: splitting > 10% = CC channel OPEN | HIGH |
| C2 | Volume-breaking CC trajectory: d(a_0/a_2)/ds along non-vol-preserving directions | Einstein (3.1 partial, #7), Tesla (3.3), Phonon-First (S3-7 partial), Baptista (3.2), Kaku (3.1) | Full 36D Hessian (not vol-preserving); a_0 gradient (proportional to dVol/dm) | Sign of d(a_0/a_2)/ds, breathing mode coupling | VOLUME-CC: PASS if d(a_0/a_2) < 0 in at least one direction | HIGH |
| C3 | Off-Jensen gradient flow / transit dynamics in 36D moduli space | Baptista (3.1, 3.5), Kitaev (3.6), Kaku (V.B) | S62 H_eff data, S64 R-Hessian (s64_hessian_descent.npz), DeWitt metric | Transit trajectory g(t), eps_H along path, deviation from Jensen; Lyapunov spectrum; instability timescale | OFF-JENSEN-TRANSIT: PASS if trajectory deviates > 5% from Jensen at fold exit. Kitaev: INFO (lambda_1 > 0 = chaotic). Kaku: tau_inst < tau_transit = Jensen curve unstable | HIGH |
| C4 | BCS-dressed spectral action profile (eps_H^BCS, delta n_s) | Einstein (#6), Kaku (#6), Phonon-First (S3-7 partial), Mack (Q2 context) | BdG D_K at 5-7 tau values; W3-B factorization | eps_H^BCS, delta(n_s), Hessian structure | PASS if |delta(eps_H)/eps_H| > 0.01 | HIGH |
| C5 | Blue tensor tilt n_T from eps_H(tau) + c_BLV(tau) + |beta(k)|^2 | Mack (M-64-2), Einstein (Sec 2.5 context), Tesla (Sec 2 assessment) | n_T numerical value + sign; comparison with slow-roll consistency relation n_T = -r/8 | NT-BLUE-65: PASS if n_T > 0. FAIL if n_T < 0 | HIGH |
| C6 | Collective (RPA) Leggett mode linewidth and DM viability | Tesla (3.2), Phonon-First (Sec 2 assessment, S3-6 related), Mack (M-64-4 partial) | s64_linewidth_hierarchy.npz, S49 Leggett data, RPA susceptibility | Q_L(RPA), Leggett pole of chi(omega), collective vs single-particle damping | PASS: Q_L(RPA) > 1 | HIGH |
| C7 | D_K spectrum at U(1) collapse / fiber degeneration | Kaku (III.D, #2), Baptista (Q3 related), Einstein (Q4 partial) | Left-invariant metric with c_u1 = epsilon -> 0 | Eigenvalue count, a_0, a_2 in degenerate limit; whether topology changes | a_0 changes: topology-change CC channel OPEN | HIGH |
| C8 | 2D spectral action landscape S(tau, sigma) on Jensen x R-descent plane | Baptista (3.5), Kaku (V.B related) | D_K structure constants, fold metric, two 36D directions from W2-A | Contour plot of S, new saddle points, eps_H(tau, sigma) | -- | HIGH |
| C9 | Swampland distance conjecture at one-loop + anti-Jensen | Einstein (3.3), Kaku (3.1) | s64_hessian_descent.npz, S63 1-loop data, DeWitt metric G=5 | |V'|/V and Delta phi along both Jensen and anti-Jensen at one-loop; geodesic distance to R=0 surface | PASS if |V'|/V > 1 or |eta_V| > 1. Kaku: Distance > 1.0 = swampland-excluded | HIGH (Einstein) / HIGH (Kaku) |
| C10 | L_max convergence of a_0/a_2 + nonlocal SA structure | Einstein (3.4, #4, #8) | D_K spectrum at L=10,11,12 | a_0(L), a_2(L), a_4(L), convergence rate | PASS if a_0/a_2 decreases > 0.1 OOM from L=10 to L=12 | HIGH |
| C11 | Scale-transfer mechanism: k_KK to k_CMB for tensor burst | Mack (M-64-1), Einstein (Q5 context) | GGE dispersion on CG(24), expansion history from SA Friedmann, k_transit/k_CMB ratio | Whether tensor burst transfers to CMB scales (r_CMB = 0.033 or 1.77e-5) | SCALE-TRANSFER-65: If localized, r_CMB < 0.001 (interp B). If transferred, r_CMB = 0.033 (interp A) | HIGH |
| C12 | Anderson-Bogoliubov mode A_s normalization | Phonon-First (S3-3), Tesla (Sec 4 context), Mack (Q4) | c_BA = 0.399, H_phys = 0.396 M_KK, eps_H = 0.0216 | A_s from AB mode Garriga-Mukhanov, bypassing PW selection | AB-AS-65: PASS if log10(A_s/A_s_obs) < 1.0 | HIGH |
| C13 | Per-shell scaling at L=4 (Hessian UV convergence) | Kaku (3.5, #7), Baptista (3.3 related) | D_K at L=4, S64 shell Hessian methodology | Per-shell Frobenius norm, Hessian convergence | SHELL-L4: PASS if L=4 contribution < L=3 (convergent). Kaku: L=4/L=3 < 0.5 | MED-LOW |
| C14 | Sphaleron rate from SA Yang-Mills (baryogenesis) | Kaku (3.3), Mack (Sec 4 baryogenesis context) | a_4 coefficients, GGE branch temperatures T_B2, T_B1, T_B3 | Gamma_sph / H_phys ratio; whether EW baryogenesis is active | Gamma_sph / H > 1: active. < 1: frozen out | HIGH |
| C15 | Van Hove enhancement of A_s transfer function | Tesla (3.4), Phonon-First (Sec 2 linewidth context) | s63_phonon_dos.npz, s64_transfer_bogoliubov.npz | Enhancement factor g(E_B2)/g_avg, revised A_s gap | INFO: report revised gap in OOM | MED |
| C16 | Off-Jensen BCS gap survival: Delta(anti-Jensen, s) | Phonon-First (S3-7), Baptista (3.1 related) | D_K eigenvalues along W2-A descent, BCS gap equation | Delta(s), survival vs destruction of condensate | GAP-ANTIJENSEN-65: PASS if Delta(s=200) > 0.1 Delta_0 | HIGH |
| C17 | T-dual metric a_0/a_2 ratio | Kaku (3.4, #6), Einstein (Q4 partial) | W2-A anti-Jensen endpoint metric; T-dual: c_u1 -> 1/c_u1 | a_0(T-dual), a_2(T-dual), CC comparison | a_0/a_2(T-dual) < a_0/a_2(fold): CC improved | MED |

### UNIQUE (proposed by 1 reviewer)

| # | Title | Proposer | Input | Output | Gate | Priority |
|:--|:------|:---------|:------|:-------|:-----|:---------|
| U1 | SFF K(t) for N=3 pairing-only H_full | Kitaev (3.1) | s64_npair3_rg.npz (eigenvalues) | K(t) plot, ramp/plateau detection, slope/GUE ratio | SFF-NPAIR3-65: PASS if slope/GUE > 0.3 | HIGH |
| U2 | Thouless parameter g_T for N=3 sector | Kitaev (3.2) | s64_npair3_rg.npz + s64_rg_charge_decomp.npz | g_T value, Anderson transition comparison | THOULESS-NPAIR3-65: INFO (g_T > 0.5 = transition, < 0.1 = localized) | HIGH |
| U3 | OTOC C(t) for pairing-only H_full at N=3 | Kitaev (3.3) | s64_npair3_rg.npz (eigenvectors, eigenvalues) | C(t) time series, lambda_L extraction (R^2 > 0.90) | OTOC-NPAIR3-65: PASS if lambda_L > 0 with R^2 > 0.90. FAIL if R^2 < 0.90 | HIGH |
| U4 | Operator entanglement entropy growth in N=3 pairing-only | Kitaev (3.4) | s64_npair3_rg.npz | S_op(t) time series, growth rate (linear vs logarithmic) | -- | MED |
| U5 | Prethermalization timescale from Gaudin charge breaking | Kitaev (3.5) | s64_rg_charge_decomp.npz (breaking strengths) | t_pretherm, t_therm estimates, comparison to cosmological timescales | -- | MED |
| U6 | High-energy level statistics of (2,1) sector | Kitaev (#7) | s27_multisector_bcs.npz or recomputed at L_max=10 | <r>, P(s) for eigenvalues above median in (2,1) block | -- | LOW |
| U7 | SYK-inspired G-Sigma framework for D_K spectrum | Kitaev (3.7) | D_K eigenvalues, degeneracies | Large-N resummation of spectral moments; F_{-1} and F_{+1} independence test | -- | LOW |
| U8 | EIH-CC projection: effective a_0^{grav}/a_2^{grav} | Einstein (3.1) | s64_rg_charge_decomp.npz, S44 EIH data | Effective CC ratio including EIH effacement suppression | a_0^{grav}/a_2^{grav} < bare ratio by > 1 OOM: PASS | HIGH |
| U9 | EP test through transit: delta G_N/G_N | Einstein (3.2) | W1-A a_2(tau), S38 timescale | delta G_N/G_N, eta_N, dG/dt/G | dG/dt/G < 10^{-13} yr^{-1} post-transit: PASS | MED |
| U10 | Bell nonlocality of GGE relic (S_CHSH) | Einstein (3.5) | s64_local_entangle.npz | S_CHSH for maximal site pair; classification | -- (INFO) | LOW |
| U11 | BLV-BA impedance matching and standing wave | Tesla (3.1) | s64_sound_speed.npz, S56 impedance data | 4x4 transfer matrix, standing wave frequencies, A_s modulation | -- | HIGH |
| U12 | Acoustic white-hole QNM ringdown spectrum | Tesla (3.5) | s64_sound_speed.npz, S38 transit profile | First 3 QNM frequencies and damping rates in M_KK units | INFO: report omega_QNM / M_KK | MED |
| U13 | Aoki K-theory eta-invariant on CG(24) | Tesla (3.6) | S56 Josephson hopping, Paper 39 formalism | eta(D_fabric, tau) at 5 tau values | INFO: nonzero eta at fold? | LOW |
| U14 | Josephson Mott transition: E_vac(E_J/E_C) curve | Phonon-First (S3-2) | S_fold, E_J = 34 M_KK, a_0 for E_C, pair Hamiltonian on CG(24) | Phase diagram, rho_vac vs E_J/E_C | MOTT-CC-65: PASS if rho_vac drops > 10 OOM at Mott boundary | HIGH |
| U15 | KZ domain count on discrete CG(24) | Phonon-First (S3-4) | CG(24) graph, transit parameters | N_domain(CG(24)) vs continuum KZ estimate | -- | MED |
| U16 | BdG spectral dimension d_s(t) | Phonon-First (S3-5) | K_BdG(t) from W3-B factorization, bare spectrum | d_s(t) flow, comparison to CDT d_s: 4 -> 2 | DS-BDG-65: INFO (report UV and IR d_s values) | MED |
| U17 | Modular power spectrum S(omega) from GGE | Phonon-First (S3-6) | GGE Lagrange multipliers, R-G charges | Peak frequencies, multi-periodic structure | -- | LOW |
| U18 | Updated f*sigma_8(z) at w_0 = -0.918 + DR3 projection | Mack (M-64-3) | S59 growth-rate ODE code, w_0 = -0.918, DESI precision | f*sigma_8(z) at 7 bins, combined D_V + f*sigma_8 discriminating power | -- | MED |
| U19 | DM relic abundance through Bogoliubov transfer function | Mack (M-64-4) | W3-D transfer function, Leggett-mode spectral weight, c_L = 0.025 | f_DM(revised), comparison with f_DM = 0.844 | FDMPW-65: PASS if f_DM > 0.5. FAIL if f_DM < 0.1 | MED |
| U20 | Multi-field vacuum stability (bounce action in 36D) | Mack (M-64-5) | W2-A Hessian eigenvectors, S(tau) potential | B_{36D} vs B_{1D} = 2.1e5; cosmological lifetime | BOUNCE-36D-65: INFO. If B < 100, flag metastability risk | MED |
| U21 | High-z structure formation diagnostic (JWST) | Mack (M-64-6) | w_0 = -0.918, H(z) from SA Friedmann at z = 6, 8, 10 | t_universe(z) for framework vs LCDM | -- | LOW |
| U22 | Chiral asymmetry matrix C in 5 non-singlet VAB sectors (Yukawa textures) | Baptista (3.4) | D_K eigenvectors at fold, Kosmann lift, s64_vab_rank.npz | Yukawa eigenvalue ratios per sector; mass hierarchy comparison | YUKAWA-TEXTURE: PASS if any pair has ratio within 1 OOM of m_t/m_b | MED |
| U23 | Lichnerowicz spectrum via Schwahn Casimir formula at fold | Baptista (3.3, 3.6) | Structure constants of SU(3), Jensen metric at tau=0.19 | Exact Delta_L eigenvalues; comparison to per-irrep Hessian | -- | MED |
| U24 | Weyl decomposition |W|^2/|Riem|^2 along the transit | Baptista (3.6) | S64 curvature data at 6 tau values from W1-E | Near-Einstein deviation profile; Weyl + traceless Ricci contributions | -- | LOW |
| U25 | Breathing mode Hessian coupling to R-descent direction | Baptista (3.2 zero-cost diagnostic) | S64 full 36D Hessian (not volume-projected) | Off-diagonal H_{vol,descent}; sign determines CC channel viability | -- | MED |
| U26 | Odd Seeley-DeWitt a_3 on SU(3) (theta-vacua for CC scanning) | Kaku (III.C investigation) | D_K spectrum at fold, eta-invariant method | a_3 value; whether theta-vacua exist | a_3 != 0: theta-scanning OPEN | HIGH |
| U27 | Anti-Jensen instability timescale | Kaku (V.B investigation) | W2-A Hessian eigenvalues, H_phys at fold | tau_instability = 1/sqrt(|lambda_min|); compare to tau_transit | tau_inst < tau_transit: Jensen curve unstable | HIGH |
| U28 | Eigenvalue density phase transition (matrix model prediction) | Kaku (V.A investigation) | D_K spectrum at 10 Lambda values | rho(lambda; Lambda) non-analytic behavior | Non-analytic = matrix model phase transition | MED |
| U29 | Partition function convergence (Hagedorn test) | Kaku (V.D investigation) | Full D_K spectrum | Z(beta) for beta in [0.001, 1000] | Z(beta) < infinity for all beta: NO Hagedorn | MED |

---

## Open Questions Requiring Computation

| # | Question | Source | Implied Computation |
|:--|:---------|:-------|:--------------------|
| Q1 | Is <r> = 0.478 at N=3 genuine partial chaos or finite-size artifact? | Kitaev Sec 5 Q1 | SFF K(t) + Thouless g_T (= U1 + U2 above) |
| Q2 | Does the prethermalization timescale from Gaudin breaking match any cosmological timescale? | Kitaev Sec 5 Q2 | Prethermalization timescale computation (= U5) |
| Q3 | Is the 36D moduli gradient flow classically chaotic? | Kitaev Sec 5 Q3 | Lyapunov spectrum of gradient flow (= C3 partial) |
| Q4 | Does the D_K spectrum at high energy exhibit emergent random-matrix correlations? | Kitaev Sec 5 Q4 | High-energy level statistics of (2,1) sector (= U6) |
| Q5 | What is the operator entanglement growth rate in pairing-only H at N=3? | Kitaev Sec 5 Q5 | Operator entanglement (= U4) |
| Q6 | Why does a_0 gravitate at all? Does EIH effacement apply differentially to a_0 vs a_2? | Einstein Sec 5 Q1 | EIH-CC projection (= U8) |
| Q7 | Is the SDW expansion the correct gravitational functional? Does gravity couple to full trace or only a_2? | Einstein Sec 5 Q2 | Conceptual -- requires theoretical analysis |
| Q8 | What breaks the rigid L0->L1->L2 hierarchy? | Einstein Sec 5 Q3 | B/F spectral splitting (= C1), nonlocal SA (= C10) |
| Q9 | Does the off-Jensen moduli space contain a CC-favorable volume-changing trajectory? | Einstein Sec 5 Q4 | Volume-breaking CC (= C2) |
| Q10 | What replaces the Mukhanov-Sasaki equation for exflation? | Einstein Sec 5 Q5 | BdG equation on M4 x SU(3) through transit -- new formalism needed |
| Q11 | Is the BLV acoustic horizon a resonant cavity with discrete QNMs or an open system? | Tesla Sec 5 Q1 | QNM ringdown (= U12) |
| Q12 | What is the collective quality factor of the Leggett mode? | Tesla Sec 5 Q2 | RPA Leggett linewidth (= C6) |
| Q13 | Can the van Hove flat-band enhancement close the 3.16 OOM A_s gap? | Tesla Sec 5 Q3 | Van Hove enhancement (= C15) |
| Q14 | Does the 36D moduli cavity have volume-changing unstable modes via nonlinear coupling? | Tesla Sec 5 Q4 | Volume-breaking CC + gradient flow (= C2 + C3) |
| Q15 | What is the sonic ringdown signature of the transit? | Tesla Sec 5 Q5 | QNM frequencies (= U12) |
| Q16 | Does the KO-dimension 6 grading split a_0 into B/F with partial cancellation? | Phonon-First Sec 5 Q1 | Volovik B/F asymmetry (= C1) |
| Q17 | Is there a Mott transition in the Josephson pair space? | Phonon-First Sec 5 Q2 | Josephson Mott (= U14) |
| Q18 | What is the spectral dimension d_s of the BdG-dressed fabric? Does it show d_s: 4->2 flow? | Phonon-First Sec 5 Q3 | BdG spectral dimension (= U16) |
| Q19 | Why does the first-order n_s truncation work when slow-roll expansion fails at second order? | Phonon-First Sec 5 Q4 | Theoretical -- non-renormalization theorem analysis |
| Q20 | Can the 27 R-descent directions be physically accessed during the transit? | Phonon-First Sec 5 Q5 | Off-Jensen gradient flow (= C3) |
| Q21 | What is the physical mechanism that transfers perturbations from k_KK to k_CMB? | Mack Sec 5 Q1 | Scale-transfer arbitration (= C11) |
| Q22 | Does the one-loop correction to n_s converge, or does the series drift further from Planck? | Mack Sec 5 Q2 | Two-loop n_s estimate + BCS dressing (= C4) |
| Q23 | Can the framework generate w_a from first principles? | Mack Sec 5 Q3 | Off-Jensen moduli flow producing w_a -- new computation |
| Q24 | Does the 3.16 OOM A_s gap close under proper GGE acoustic normalization? | Mack Sec 5 Q4 | AB mode A_s (= C12) + van Hove enhancement (= C15) |
| Q25 | What is the blue tensor tilt n_T quantitatively? | Mack Sec 5 Q5 | Blue tilt computation (= C5) |
| Q26 | Does the transit trajectory curve away from Jensen? | Baptista Sec 5 Q1 | Off-Jensen gradient flow (= C3) |
| Q27 | What is the Lichnerowicz spectrum at the fold? | Baptista Sec 5 Q2 | Schwahn Casimir formula (= U23) |
| Q28 | Does the breathing mode open a CC channel? | Baptista Sec 5 Q3 | Breathing mode coupling (= U25 + C2) |
| Q29 | Why does the L=3 shell dominate the one-loop Hessian (79.9%)? | Baptista Sec 5 Q4 | Lichnerowicz decomposition (= U23) + L=4 extension (= C13) |
| Q30 | Can the generation-direction rank-5 result be sharpened to rank-3? | Baptista Sec 5 Q5 | Chiral asymmetry matrix (= U22) |
| Q31 | Does T-duality extend to the spectral action on left-invariant metrics? | Kaku Sec 5 Q1 | T-dual metric test (= C17) |
| Q32 | What is the Connes spectrum of the full 36D modular flow? | Kaku Sec 5 Q2 | Theoretical -- classification of joint GGE x moduli algebra |
| Q33 | Can the a_0 = 6440 mode count jump under topology change at U(1) collapse? | Kaku Sec 5 Q3 | Fiber degeneration (= C7) |
| Q34 | What is the SFT analog of the BdG heat kernel factorization? Is it genuine or kinematic? | Kaku Sec 5 Q4 | Theoretical -- structural comparison |
| Q35 | Is the 2.2-sigma n_s tension meaningful or artifact of truncation? | Kaku Sec 5 Q5 | BCS-dressed eps_H (= C4) |

---

## Discussion Points (no computation needed)

| # | Point | Source |
|:--|:------|:-------|
| D1 | The Brody parameter beta is unreliable at dim=56; KS test, participation ratio, and SFF are the correct diagnostic chain | Kitaev Sec 2 |
| D2 | Q < 1 linewidths signal dephasing without scrambling -- distinct from chaos; MSS bound applies to many-body Lyapunov, not single-particle decay | Kitaev Sec 2 |
| D3 | GGE-KMS type III_1 is formal in the thermodynamic limit; finite system is type I (finite-dimensional) | Kitaev Sec 2 |
| D4 | The CC problem is a spectral geometry problem about a_0, not a chaos/dynamics problem | Kitaev Sec 4, Closing |
| D5 | Lambda_SA = Lambda_J is a categorical result: emergent Einstein equations are projections of spectral action, not independent | Einstein Sec 1, Sec 2.1 |
| D6 | The SDW expansion caveat: nonlocal spectral action effects could modify a_0 contribution | Einstein Sec 2.1 |
| D7 | Unruh temperature may acquire corrections from BCS condensate acoustic speed (O(c_BLV^2 - 1) ~ 0.24) | Einstein Sec 2.3 |
| D8 | r = 0.033 with blue n_T > 0 is the framework's most falsifiable near-term prediction; CMB-S4 tests at 33-sigma | Einstein Sec 2.5, Mack Sec 2 |
| D9 | The CC problem requires a new principle, not a new mechanism -- a_0/a_2 is structural | Einstein Closing |
| D10 | The fold is a critically damped cavity (Q_eff ~ 1.9) with UV-dominated restoring force (L=3 shell = 79.9%) | Tesla Sec 1.1 |
| D11 | Four-speed hierarchy maps to He-3B four-sound system -- same dispersion physics, not analogy | Tesla Sec 1.2, Phonon-First Sec 2 |
| D12 | Linewidth hierarchy reversal is textbook resonance: flat band = max DOS = max scattering rate | Tesla Sec 1.3 |
| D13 | Bogoliubov transfer function is literally a phononic crystal filter cascade | Tesla Sec 1.4 |
| D14 | Sudden-quench Bogoliubov phases (phi_Bog = pi, R = 1.0000) = impulsive resonator excitation | Tesla Sec 1.5 |
| D15 | c_BLV(tau) monotonically increasing means acoustic horizon is a gradient ("sonic ramp"), not a sharp wall | Tesla Sec 2 caveat |
| D16 | Strong coupling ||V||/W = 2.59 raises perturbative control questions; vertex corrections may matter at Q < 1 | Tesla Sec 2 caveat |
| D17 | Condensed-matter hierarchy inversion: 3 FAILs (linewidth, Peotta-Torma, BdG Sakharov 31%) all signal collective > single-particle | Phonon-First Pattern 2 |
| D18 | Transit-as-Quench universality confirmed from 6 independent angles | Phonon-First Pattern 3 |
| D19 | BCS occupation spectral action: NCG cutoff is not BCS cutoff; Meissner screening (98.85%) may provide natural cutoff | Phonon-First Sec 2 (W1-D) |
| D20 | BdG Kasparov factorization is operator identity, not perturbative -- spectral action Anderson-Higgs mechanism | Phonon-First Sec 2 (W3-B) |
| D21 | The framework is NOT a variant of inflation -- it is a genuinely different cosmological mechanism (quantum quench) | Mack Sec 4, Phonon-First Pattern 3 |
| D22 | 7.4% margin between r = 0.033 and BICEP/Keck r < 0.036 is thin; BICEP Array test expected 2027-2028 | Mack Sec 2 |
| D23 | Bogoliubov enhancement factor (1+2|beta|^2)^2 = 9.18 is the swing factor; verify |beta|^2 = 1.015 | Mack Sec 2 |
| D24 | n_s one-loop correction moves AWAY from Planck (-0.00103); direction is concerning | Mack Sec 2 |
| D25 | DESI pattern mismatch: framework w_0 = -0.918 matches direction but not z-dependent Quintom B structure | Mack Sec 2 |
| D26 | Every CMB prediction carries an asterisk until the k_KK -> k_CMB scale transfer mechanism is identified | Mack Closing |
| D27 | R-monotonicity holds only along 1D Jensen curve; 27 off-Jensen R-descent directions are unexplored | Baptista Sec 2 |
| D28 | Anti-Jensen direction = expand SU(2), shrink C^2 and U(1) -- geometric opposite of Jensen transit | Baptista Sec 2 |
| D29 | The 1D Jensen era is closing; the full moduli-space dynamics begins | Baptista Closing |
| D30 | Near-Einstein property at fold: |Ric|^2/(R^2/8) = 1.009, only 0.94% deviation | Baptista Sec 3.6 |
| D31 | W7-D H2 theorem connection: volume-preserving = traceless in DeWitt superspace = zero pi_{ij} = BCS natural gauge choice | Baptista Sec 2 |
| D32 | Framework is NOT string theory in disguise -- it is emergent gravity with KK geometry and BCS condensation (Volovik convergence) | Kaku Sec 4 |
| D33 | Substrate is structurally closer to IKKT matrix model than to any conventional SFT | Kaku/Investigation II.B |
| D34 | No Hagedorn temperature: polynomial (not exponential) density of states from PW decomposition | Kaku/Investigation II.C |
| D35 | The a_0/a_2 trap is structurally analogous to the SUGRA eta problem; different algebra, same obstruction | Kaku Sec 2, Investigation #13 |
| D36 | All 5 baryogenesis channels closed at fiber level; must emerge at 4D effective theory level | Kaku Sec 2, Mack Sec 4 |
| D37 | Framework satisfies more God Equation criteria than string theory, LQG, or LCDM | Kaku Sec 3.6 |
| D38 | 36D moduli space is finite, fully computable -- unlike string landscape (~10^500 vacua) | Kaku Sec 1, Investigation I.#5 |
| D39 | KKLT moduli stabilization is ABSENT in the framework -- 35 transverse moduli are unconstrained, a structural deficit | Investigation I.#15 |
| D40 | The "string" in this framework is a truncated Regge trajectory = finite matrix model, not conventional SFT | Investigation II.A-B |

---

## Cross-Domain Patterns Identified

### Pattern 1: The a_0/a_2 Spectral Moment Stratification
**Noted by**: Einstein, Phonon-First, Baptista, Kaku, Tesla, Mack
The CC, gravity (G_N), and NEC each depend on different spectral moments (a_0, a_2, F_{+1}). These moments cannot be independently tuned within volume-preserving moduli space. The spectral moment decoupling theorem (W5-B) grants structural permission for resolution, but the a_0/a_2 trap (W2-A) closes all volume-preserving paths. Every reviewer converges on volume-breaking and/or B/F spectral splitting as the surviving CC routes.

### Pattern 2: Off-Jensen Moduli Space as the Next Frontier
**Noted by**: All 7 reviewers + investigation
The 36D moduli space with saddle structure (8+, 27-) at the fold is universally identified as the framework's critical unexplored territory. The 1D Jensen curve explored in sessions 1-63 is a submanifold of a much richer landscape. The off-Jensen gradient flow, the anti-Jensen direction, the volume-changing modes, and the 2D landscape are all proposed as highest-priority computations by multiple reviewers.

### Pattern 3: Collective Modes Replace Single-Particle Description
**Noted by**: Tesla, Phonon-First, Kitaev, Mack
The Q < 1 linewidths, Peotta-Torma FAIL, and BdG Sakharov 31% capture collectively signal that the quasiparticle picture breaks down. The correct description uses collective modes: RPA susceptibility, Leggett mode, Anderson-Bogoliubov mode. This transitions the framework from kinetic (Boltzmann) to hydrodynamic (collective) regime. The DM prediction and A_s normalization both depend on getting the collective description right.

### Pattern 4: Transit-as-Quench Universality
**Noted by**: Phonon-First, Tesla, Mack, Einstein
Six independent angles confirm the sudden-quench character: N_e = 3.73e-3, Mach 13.8, modes never freeze, Bogoliubov phases pinned to pi, KZ overproduction, scattering prediction failure. The framework is NOT inflation -- it is a quantum quench, and the correct perturbation theory is the sudden approximation.

### Pattern 5: The r = 0.033 / n_T > 0 Discriminant
**Noted by**: Einstein, Tesla, Mack, Baptista, Kaku
The cleanest zero-parameter observational prediction: r = 0.033 with blue tensor tilt n_T > 0, discriminating against all single-field slow-roll models (which give n_T = -r/8 < 0). Testable by BICEP Array (2027-2028), CMB-S4 and LiteBIRD. The Bogoliubov enhancement factor (1+2|beta|^2)^2 = 9.18 is the key uncertainty.

### Pattern 6: The Baryogenesis Crisis
**Noted by**: Kaku, Mack, Einstein (implicit)
All 5 fiber-level baryogenesis channels are closed. The surviving route is the 4D effective theory (sphaleron from SA Yang-Mills). This is the framework's most serious structural deficit alongside the CC.

### Pattern 7: The A_s Normalization Gap
**Noted by**: Tesla, Phonon-First, Mack
The 3.16 OOM A_s gap (down from 8.01) is the framework's second-most pressing observational deficit. Multiple independent routes proposed to close it: Anderson-Bogoliubov mode (bypasses PW selection), van Hove enhancement, impedance matching standing waves, proper GGE acoustic normalization.

### Pattern 8: Scale Transfer Problem
**Noted by**: Mack (primary), Einstein (related)
The fundamental mechanism mapping transit-scale perturbations (k_KK ~ 10^16 GeV) to CMB scales (k_CMB ~ 10^-9 GeV) across 57 e-folds remains unidentified. Standard inflation uses exponential expansion; the framework has N_e = 7.75. This is the deepest open question for observational connection.

---

## Investigation-Specific Proposals

From `investigation-phonon-strings.md` (Kaku):

| # | Computation | Input | Output | Gate | Priority |
|:--|:-----------|:------|:-------|:-----|:---------|
| I1 | Odd Seeley-DeWitt a_3 on SU(3) | D_K spectrum at fold, eta-invariant method | a_3 value; theta-vacua for CC scanning | a_3 != 0: theta-scanning OPEN | HIGH |
| I2 | D_K spectrum at U(1) collapse (conifold transition) | Left-invariant metric with c_u1 -> 0 | a_0, a_2 in degenerate limit; topology change test | a_0 changes: topology-change CC channel OPEN | HIGH |
| I3 | Anti-Jensen instability timescale | W2-A Hessian eigenvalues, H_phys | tau_instability vs tau_transit | tau_inst < tau_transit: Jensen curve unstable | HIGH |
| I4 | Eigenvalue density phase transition (matrix model) | D_K at 10 Lambda values | rho(lambda; Lambda) non-analytic behavior | GWW-type transition detected | MED |
| I5 | Partition function convergence (Hagedorn test) | Full D_K spectrum | Z(beta) for all beta | Z < infinity: NO Hagedorn (confirms non-string) | MED |
| I6 | T-dual metric a_0/a_2 | Anti-Jensen endpoint; c_u1 -> 1/c_u1 | a_0, a_2, ratio on T-dual metric | CC improved: duality channel OPEN | MED |
| I7 | IR B/F spectral splitting from BCS | BdG D_K; separate by KO-grading | Delta(a_2^B - a_2^F) in IR sector | Splitting > 10%: CC reduction OPEN | HIGH |

**Key investigation conclusions:**
- The substrate is NOT a string theory; it is a finite matrix model (closer to IKKT than Kaku-Kikkawa or Witten SFT)
- Correspondence: 4 GENUINE, 7 STRUCTURAL, 4 PARTIAL, 2 BROKEN, 2 ANTI
- Deepest breaks: T-duality and S-duality (require propagating extended objects absent in substrate)
- Deepest matches: SUSY B/F cancellation = shared-spectrum theorem T9, graviton emergence, anomaly cancellation
- Productive direction: use string-theory TOOLS (matrix models, moduli stabilization, topology change, B/F splitting) in the computable substrate setting

---

## Summary Statistics

- **Total unique computations identified**: 46 (17 convergent + 29 unique)
- **HIGH priority**: 25
- **MED priority**: 16
- **LOW priority**: 5
- **Open questions requiring computation**: 35
- **Discussion points (no computation)**: 40
- **Cross-domain convergent patterns**: 8
- **Investigation proposals**: 7

### Priority Levels for S65 Planning

**computation (must-do, highest EVOI):**
- C1: Volovik B/F spectral asymmetry (CC path)
- C2: Volume-breaking CC trajectory (CC path)
- C3: Off-Jensen gradient flow in 36D (transit physics + CC)
- C4: BCS-dressed spectral action (n_s correction)
- C5: Blue tensor tilt n_T (key discriminant)
- C11: Scale-transfer k_KK -> k_CMB (observational foundation)
- C12: Anderson-Bogoliubov mode A_s (A_s gap)

**Level 1 (high priority, clear gates):**
- U1/U2/U3: Kitaev N=3 chaos diagnostics (SFF, Thouless, OTOC) as a package
- C7: D_K at U(1) collapse / fiber degeneration (CC topology-change path)
- C8: 2D spectral action landscape (moduli exploration)
- U8: EIH-CC projection (CC path)
- U14: Josephson Mott transition (CC path)
- C14: Sphaleron rate from SA Yang-Mills (baryogenesis)
- U26: Odd Seeley-DeWitt a_3 (CC theta-vacua)
- U27: Anti-Jensen instability timescale (transit physics)
- C6: Collective Leggett mode linewidth (DM viability)

**Level 2 (medium priority):**
- C9: Swampland at one-loop + anti-Jensen
- C10: L_max convergence of a_0/a_2
- C15: Van Hove enhancement of A_s
- C16: Off-Jensen BCS gap survival
- U5: Prethermalization timescale
- U9: EP test through transit
- U11: BLV-BA impedance matching
- U12: QNM ringdown
- U15-U16: KZ on CG(24), BdG spectral dimension
- U18-U20: f*sigma_8, DM abundance, bounce action
- U22-U25: Yukawa textures, Lichnerowicz, Weyl decomposition, breathing mode

**Level 3 (lower priority, exploratory):**
- U6, U7, U10, U13, U17, U21, U24, C13, C17, U28, U29
