---
name: Complete Integrability Hierarchy and Gate Verdicts
description: All chaos diagnostics (level spacing, OTOC, SFF, Thouless, Lyapunov) across every subsystem tested S38-S74. Master reference for Ordered Veil.
type: project
---

# Complete Integrability Hierarchy

SCOPE (reconciled S100b, per RETRACTED-S39): FABRIC-SCALE integrable (CG(24) <r>=0.367; r_pooled=0.422; 36D moduli lambda=0; transit-freeze R_therm=5251.82, S_ent=0). SINGLE-CELL interacting system THERMALIZES: INTEG-39 DECISIVE FAIL (S96 re-confirm: V_phys 13% non-separable, Brody beta=0.633 = 63% GOE, Thouless g=0.60, t_therm~6 M_KK^-1; atlas-04 T3 BROKEN). The table rows below are point-in-time measurements and stand; the retired claim is the single-cell PERMANENCE narration, not the fabric-scale diagnostics. ADH 10^578 = dephasing-prethermalization, distinct from interaction-thermalization (registry wins).

## Master Diagnostic Table

| Level | Diagnostic | Result | Session |
|:------|:-----------|:-------|:--------|
| Single-particle D_K (2,1) | Brody beta | 0.001 (Poisson) | S53 |
| Single-particle D_K (2,1) | <r> ratio | 0.329 (sub-Poisson) | S53 |
| Single-particle D_K | <r> level spacing | 0.321 sub-Poisson | S38 |
| D_K L12 cache degeneracy-resolved SFF-unfold | <r> | 0.4118 (SPEC-B global merge, Poisson); xchk Weyl-smooth 0.3888≈Poisson surmise, spec-A 0.4527 — all Poisson-incommensurate, repro S46 0.439 (\|Δ\|=0.027<0.03) | S106 W1-2 |
| D_K L12 @tau_fold connected-SFF + number-variance (INV3-W1-1) | p_Sigma2, ramp, <r> | INFO-arithmetic: p_Sigma2=0.6198 on [0.5,6.25] (Poisson=1, GUE=0.25); NO SFF ramp (trend -1.54 vs GUE +2); <r>=0.3915≈Poisson(0.3863). Sigma^2 SATURATES L_sat=6.25(L12)->7.75(L14) = FINITE-N rigidity ceiling, NOT RMT ln-growth. Per-(p,q)-block distinct-level unfold (87/90 blocks, 13452 levels) | INV3-W1-1 |
| D_K L12 @tau_fold sector-resolved P(s) (INV3-W1-2) | beta_block, rho | PASS-pooling-artifact: beta_block=-0.064+/-0.014 (each block Poisson), rho_pooled=1.0, per-block <r>=0.393. CONFIRMS the pooled <r>-excess is superposition residual, not intrinsic repulsion (independent confirm of W1-1 INFO reading) | INV3-W1-2 |
| D_K L12+L14 deep-truncation POOLED SPEC-B Sigma^2 + SFF (INV10-W3-3) | Sigma^2/L, regime | INFO: SUPER-POISSON decisive — Sigma^2/L=54.6(L12)->227.97(L14), persists+GROWS w/ depth (Berry-Tabor superposition of ~120 (p,q) sub-spectra). NOT chaotic (GUE=Sigma^2/L<1 falling; D_K exceeds GUE by ~2000x). In-run Poisson ctrl(slope0.97,Sigma^2/L1.02) + GUE ctrl(Sigma^2/L0.11 falling) VALIDATE the small-L discriminator. LITERAL slope>=0.7 window-sweep pre-reg RUBRIC-FORM BROKEN (PRU Class-8.2: unfolding kills long-range Sigma^2 — Poisson ctrl itself fails slope>=0.7); re-anchored to calibration-valid SMALL-L Sigma^2/L. Single-spectrum SFF ensemble-limited=DIAGNOSTIC-ONLY (fails own GUE ctrl; no-ramp of record=SFF-NPAIR3-65 slope/GUE~0.002). RESOLVES G2/A3 genuine-vs-superposition: integrability is SUPERPOSITION-Poisson NOT complete-conserved-charge; Ordered Veil robust leg = transit-freeze NOT protected integrable skeleton. Counted-w-mult degeneracy-saturated(frac0.97)=Sigma^2 ill-defined (why SPEC-B is primary). lambda_L=0 stands, kill NOT triggered. Consistent w/ INV3-W1-1 per-block saturation (each block Poisson; pooling 120 blocks = super-Poisson) | INV10-W3-3 |
| Many-body Fock 256-dim | OTOC growth | t^{1.9}, no Lyapunov | S38 |
| Many-body Fock 256-dim | Scrambling time | 814x too slow | S38 |
| B2 subsystem | <r>, Thouless g_T | 0.401, 0.087 | S40 |
| Entanglement B2\|rest | Page curve | 18.5% of S_Page | S40 |
| Information B2 occ | Diagonal ensemble | 89% retained | S40 |
| Liouvillian N_pair=1 | <r>, RP gap | 0.407, gamma=0.040 | S52 |
| 2-cell Josephson N_pair=2 | <r> | 0.367 Poisson | S56 |
| 1-cell N_pair=3 | <r> | 0.414 Poisson (blocking) | S56 |
| 2-cell large E_J (100x) | <r> | 0.303 sub-Poisson (emergent sym) | S56 |
| 2-cell Andreev+Josephson N_pair=2 | <r> | 0.407 (MF), 0.439 (ED) | S57 |
| 2-cell Andreev tau sweep | <r> max | 0.476 at tau=0.102 (K2 FAIL) | S57 |
| 2-cell Andreev SFF | ramp/plateau | NONE (slope/GUE = -0.008) | S57 |
| 2-cell Andreev OTOC | lambda_L | 0.117 (R^2=0.83 < 0.90, NO Lyapunov) | S57 |
| S(q,omega) GGE | D_JS(GGE\|\|eq) | 0.024 (non-thermal resolvable) | S58 |
| S(q,omega) structure | mode sharpness | discrete peaks, no diffusive bg | S58 |
| 2-cell OTOC N_pair=2 | lambda_L | 0 (R^2=0.041, C~t^1.04) | S59 |
| 2-cell OTOC N_pair=2 | t_scr/t_transit | 524,000x (no scrambling) | S59 |
| N_pair=3 pairing-only | <r> (full V, lifted) | 0.478+/-0.021 (transition!) | S64 |
| N_pair=3 pairing-only | <r> (RG, lifted) | 0.213+/-0.037 (super-integrable) | S64 |
| N_pair=3 pairing-only | Brody beta | 0.01+/-0.14 (CONTRADICTS <r>) | S64 |
| N_pair=3 pairing-only | SFF ramp slope/GUE | 0.002 (NO RAMP, R^2=0.086) | S65 |
| N_pair=3 pairing-only | Number variance Sigma^2(5) | 9.92 (2x Poisson, 13x GUE) | S65 |
| N_pair=3 OTOC (n1 vs n2) | lambda_L, R^2_exp | 0.000, 0.039 (flat dephasing) | S65 |
| N_pair=3 OTOC (n4 vs n5) | lambda_L, R^2_exp | 0.006, 0.640 (C~t^{0.79}) | S65 |
| N_pair=3 OTOC scrambling | t_scr/t_transit | 6,887x to 151,514x | S65 |
| N_pair=3 Thouless g_T | ensemble (n=50) | 0.484 +/- 0.127 | S65 |
| N_pair=3 PR/dim | participation ratio | 0.218 (66% of GOE) | S65 |
| ADH prethermalization | log10(t_therm/t_univ) | 578 (PERMANENT) | S65 |
| N_pair=4 half-fill SFF | slope/GUE | -0.002 (NO RAMP) | S66 |
| N_pair=4 half-fill | <r> (n=500) | 0.453+/-0.001 | S66 |
| N_pair=4 half-fill | Sigma^2(5) | 10.06 (2x Poisson) | S66 |
| N_pair=3 OEE (n_0 B2) | alpha (log coeff) | 0.324 (LOG R2>LINEAR R2) | S66 |
| N_pair=3 OEE saturation | S_sat/S_max | 0.49 (chaotic=~1.0) | S66 |
| **36D classical moduli** | **Lyapunov** | **0.0 M_KK (INTEGRABLE)** | **S66** |
| 36D anharmonicity | max deviation | 6.0e-5 (QUADRATIC) | S66 |
| CG(24) beta-relaxation | omega_1 | 0.114 M_KK = 1.29e40 Hz | S67 |
| CG(24) phase-slip | WKB | S_inst=16.3, Gamma=1.64e32 Hz | S67 |
| GGE Bell (8 modes) | Horodecki CHSH | min S=2.351, all 8 > 2 | S70 |
| GGE thermality | CV(T_eff) | 47.9% (NON-THERMAL) | S70 |
| CG(24) Berry-Dennis | chi^2/ndof | 329 (FAIL) | S70 |
| CG(S_N) velocity | D_KL(P_N\|\|P_24) | max 0.153 (INFO) | S71 |
| Modular chirp | d^2(H_mod)/dtau^2 | FAIL (8.4 OOM vs kappa) | S72 |
| CG(24) GGE entropy | S_cell | 2.213 nats, I=0.371/bond | S72 |
| CG(24) graph diffusion | t_dec/t_transit | 820.6 (FAIL) | S73a |
| CG(24) Ramanujan heat kernel | t_mix/t_transit | 237 (FAIL, S73b confirms 73a) | S73b |
| 10 PW irreps L_max=3 | r_pooled (118 ratios) | 0.4220 +/- 0.27 PASS | S74 |
| DC fraction scaling | 4c->8c->12c | 0.204->0.139->0.046 (FAIL) | S74 |
| V_fold === V_8x8_raw | Frobenius norm | 5.07e-17 (machine eps) | S74 |
| <r> V_fold vs V_phys | relative diff | 5.77% (0.436 vs 0.463) | S74 |

## Gate Verdicts (final)

| Gate | Verdict | Key number |
|:-----|:--------|:-----------|
| CHAOS-1 (level spacing) | FAIL | <r>=0.321 sub-Poisson |
| CHAOS-2 (OTOC) | FAIL | t^{1.9}, no Lyapunov |
| CHAOS-3 (scrambling) | FAIL | t_scr/t_transit=814x |
| B2-INTEG-40 | PASS | <r>=0.401, g_T=0.087 |
| PAGE-40 | FAIL | 18.5% of S_Page |
| NOHAIR-40 | FAIL | T varies 64.6% |
| LIOUVILLIAN-52 | INFO | gamma_RP=0.040, Poisson |
| BRODY-53 | PASS-INTEGRABLE | beta=0.001 |
| FABRIC-INTEG-56 | FAIL | <r>=0.367, Josephson is rank-1 central |
| NPAIR3-ED-56 | FAIL | <r>=0.414, blocking strengthens integrability |
| GGE-FABRIC-56 | INFO | gap=13.04 (35x), adiabatic protection |
| ANDREEV-INTEG-57 | INFO | <r>=0.439 ED, K2 all FAIL |
| SCRAMBLING-59 | FAIL | lambda_L=0, t_scr=524,000x transit |
| SFF-NPAIR3-65 | FAIL | slope/GUE=0.002, no rigidity |
| OTOC-NPAIR3-65 | INFO | C~t^{0.79}, no Lyapunov. Sides with Brody |
| THOULESS-65 | INFO-TRANSITION | g_T=0.63, prethermalization without thermalization |
| PRETHERM-65 | PASS | t_therm/t_univ=10^{578} |
| SFF-NPAIR4-66 | PASS-INTEGRABLE | <r>=0.453, no ramp |
| S106-W1-SFF-UNFOLDING-L12 | PASS | Track-B Poisson-incommensurate reproduced on L12 cache. SPEC-B (global degeneracy-merge, S46 poly staircase, E=\|λ\|² D_K²): <r>=0.4118, N_uniq=7002, deg=7. Repro \|<r>-0.439\|=0.027<0.03. 3 indep unfold methods all Poisson (Weyl-smooth 0.3888 σ-insensitive ≈ Poisson surmise; spec-A 0.4527), none near clustered 0.27. Confirms CHAOS-1 0.321 sub-Poisson = exact-degeneracy artifact (3rd indep confirmation after S100b 0.3910). audit b9ea49e2... |
| OEE-NPAIR3-66 | PASS-INTEGRABLE | log growth, S_sat/S_max=0.49 |
| CLASSICAL-LYAPUNOV-36D | PASS-INTEGRABLE | lambda=0.0, closes last chaos channel |
| BERTINI-ESSLER-66 | PASS | agrees with ADH within 1 OOM |
| GGE-VOLOVIK-67 | PASS | Gamma_beta=1.29e40 Hz |
| BELL-GGE-70 | PASS | all 8 modes S>2, non-thermal |
| DISCRETE-BD-70 | FAIL | chi^2=329, no discrete limit |
| DISCRETE-RW-71 | INFO | max D_KL=0.153, d_s undefined |
| MODULAR-CHIRP-72 | FAIL | 8.4 OOM incommensurable |
| CG24-GGE-ENTROPY-72 | INFO | f_OV=0.26-0.60 |
| GRAPH-DECOHERENCE-73a | FAIL | 820x too slow |
| RAMANUJAN-73B | INFO | t_mix/t_transit=237; CG(24) too small for d_s power-law |
| MULTI-CELL-PLANCHEREL-74 | PASS | r_pooled=0.422 (10 PW irreps L_max=3, N_pair=60) |
| DC-PERMANENCE-74 | FAIL | drops to 0.046 at 12-cell |
| W2E-INTEG-LINK-74 | PASS | V_fold===V_8x8_raw, single geometric source |
| INTEG-39 (S96 re-confirm) | DECISIVE FAIL (single-cell) | Brody beta=0.633, t_therm~6 M_KK^-1, V_phys 13% non-sep, Thouless g=0.60 — atlas-04 T3 BROKEN |

## S100b W4 (plan-freeze 2026-06-06; W4-2 RUN 2026-06-07)
- S100b-DK-ERGODICITY: Hekkelman-McDonald 2412.00628 (Def 2.3 Weyl, Thm 2.7 NC-integral, Def 6.10/Thm 6.11 QE=unique-vacuum) on D_K L12 cache; PASS=non-ergodic n_vacuum>=2, QE_defect>0.01; INFO=Weyl-fit out of band (d=8±1.5, R^2>=0.98) [connes-side gate; see W4 WP]
- S100b-KNN-ORDERED-VEIL: Shir 2504.20134 corrected kNN surmise (exponent Eq.15 in Eq.2+4; variance Eq.8 c_1=4/pi-1 GOE vs Eq.11 Poisson Delta=k; GoF Eq.18; unfold App.B) inside (p,q) sectors. Cache feasibility verified: 52 sectors n_unique>=100, 27 p>=q reps ((p,q)===(q,p) exact), 5846 pooled distinct levels, 5819 NN spacings. Boundaries: V_k=0.5 midpoint, Brody 0.3, rigidity guard V_k<-0.25 (Berry-Tabor exception class, NOT chaos)
  - RESULT: **PASS** — Poisson at ALL k in {1,2,3} inside resolved sectors. KS D_k(P)=0.032/0.042/0.057 << D_k(corr-Wigner)=0.195/0.200/0.208; V_k=0.882/0.737/0.663 (all >=0.5, GOE band EMPTY); Brody beta_1=0.0551 (MLE); <r>_resolved=0.3910 (+1.34 sigma vs 0.3863; GOE 40 sigma). <r> rose 0.321->0.3910: CHAOS-1 sub-Poisson baseline FULLY accounted for as exact-degeneracy superposition artifact (Claim C verified). First kNN-range (k>1) integrability anchor. Both schemes PASS class (secondary V_k=3.5-4.0 = mean-norm density-modulation artifact; its KS/beta_1 still Poisson). V_k declines with k (0.88->0.66): poly-unfolding long-wavelength absorption + candidate residual multiplet correlation — diagnostic only. (4,4)-repair robustness: shifts <=0.003. UNTRUSTED-UPSTREAM caveat: conditional on LC-lineage (t=1/2) canonicity (TAU0-LAITEH escalation pending). audit 04e3d4d2244ce3d2... line s100b_gate_verdicts.txt:75. sign/mag/regime = PASS/PASS/VALID.

## Key Structural Results
- Berry-Tabor: [iK_7, D_K]=0 at ALL tau -> single-particle integrable (conserved quantity)
- V(B2,B2) 86% rank-1 -> B2 subsystem near-integrable
- Josephson preserves integrability: rank-1, B=sum_k b_k is central
- N_pair=3 blocking: <r> DECREASES with filling (0.707->0.509->0.414)
- Non-separable V_bare: rank-1 captures 64%, residual 36% breaks R-G but does NOT produce chaos
- GGE-KMS: 8-fold modular decomposition PROVEN (Tomita-Takesaki, Type III_1)
- Spectral moment decoupling: F_{-1}(CC) vs F_{+1}(NEC) independent (PERMANENT)
- <r>=0.478 resolved: short-range repulsion from V_perp without long-range rigidity (SFF+Sigma^2)
- V_fold (W4-A) === V_8x8_raw (S37) to machine epsilon -> single geometric fault line

## S58 Dynamic Structure Factor
Three bands: Leggett [0.138,0.383] (46%), BA [0.209,1.368] (23%), pair-breaking [0.929,inf) (31%). D_JS(GGE||thermal)=0.024, B2/B3 asymmetry 10:1 GGE fingerprint. Sharp modes + structured continuum, no diffusive background.

## CG(24) Notes (S73a + S73b)
- 6-regular Cayley graph of S_4 on transposition generators, 24 vertices, 72 edges, diameter 3
- Laplacian: lambda_0=0, lambda_1=4 (Ramanujan: >= 6-2sqrt(5)=1.5279, CONFIRMED), lambda_max=12
- 5 distinct eigenvalues -> finite-sum heat kernel, NO power-law d_s regime (d_s window-dependent: 0.004 to 1.291)
- Substrate 4D emerges from Seeley-DeWitt a_2 of D_K, NOT graph spectral dim. Category error to compare d_s(CG24) to 4
- Ramanujan optimality cannot rescue mechanism: bottleneck is supersonic transit speed, not graph expansion

## S74 Multi-cell Plancherel Notes
- 10 PW irreps at L_max=3, N_pair=60 thermal at T_GGE=T_acoustic=0.112 M_KK, V_pair=J_C2=0.933 M_KK, tau=tau_fold
- Per-sector (2,1) and (1,2) at 40 ratios each: r_uniq=0.3638 sub-Poisson
- METHODOLOGY GOTCHA: rank-1 BCS pair-lift on sparse Dirac spectrum produces Cauchy-interlacing equidistribution -> <r>_pair=0.61 super-Wigner appearance despite integrable underlying. DO NOT cite rank-1 pair-lift r-ratio as chaos evidence

## Kill Authority
NOT triggered. No scrambling, no chaos bound violation at any scale tested. MSS bound (lambda_L <= 2*pi*T) trivially satisfied: lambda_L=0. The 0.4625 <r> at S39 was sector-mixing (S40 retraction), not many-body chaos.
