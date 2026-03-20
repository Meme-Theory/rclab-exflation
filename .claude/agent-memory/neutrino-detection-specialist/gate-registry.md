# Pre-Registered Gate Registry

Only new computational results against these gates constitute evidence.

## Resolved Gates

| Gate | Condition | Outcome | Session | Notes |
|------|-----------|---------|---------|-------|
| R-block | R crosses 33 in [0.15, 1.55] block-diag | FAIL | 22b | R=33 only at tau=1.556 (outside window, monopole artifact) |
| R-coupled-* | R=33 in coupled basis | CLOSED | 22b | Coupled = block-diagonal (C-10). All 3 sub-gates collapsed |
| R-Heff | R from tight-binding H_eff in [20, 50] | FAIL | 24a | R ~ 10^14 (Kramers artifact) |
| R-Ka | R from Kosmann K_a in [17, 66] | FAIL | 24a | R = 5.68 |
| V-spec-min | V_spec min at tau in [0.20, 0.40] | FAIL | 24a | V_spec monotonically increasing for all rho |
| BCS-mu0 | BCS gap nontrivial at mu=0 | FAIL | 23a | M_max = 0.077-0.149, 7-13x below threshold |
| R-BCS | R_BCS in [17, 66] via uniform BCS gap | FAIL | 28-synth | R_BCS = R_bare = 5.68 |
| R-wall | R from wall H_3x3 in [5, 100] | FAIL | 33 W3 | R_max=0.71. Trap 4 at walls: V_12/V_23~2.7 locked. s33w3_wall_pmns.py |
| PMNS-tridiag | theta_13, theta_12, theta_23 in PDG | PARTIAL FAIL | 29Ba | sin^2(theta_13)=0.027 (pass). theta_12=42.8 (fail). theta_23=14.0 (catastrophic). R=0.29 |
| PMNS-wall | theta_23 + sin^2(theta_13) at wall | PARTIAL FAIL | 33 W3 | theta_23 passes (42-52 deg). sin^2(theta_13) fails (min 0.20). s33w3_wall_pmns.py |
| KC-3 | Van Hove BCS at tau>=0.50 | PASS | 29Aa | n_gap=37.3, 87% above threshold |
| L-9-first-order | First-order transition, discontinuous tau | PASS | 29Ab | F_BCS<0 everywhere. c=0.006-0.007. Trapping at E_mult<=1.5 |
| Backbend-wall | omega_c > omega_inst at dump | PASS (analytic) | W R1 | j_eff=0 at dump. omega_c~4500*Delta^2 >> omega_inst |
| TRAP-33b | M_max > 1.0 from wall BCS (spinor V) | RETRACTED | 34 | Used frame V (0.287) not spinor V (0.057). Correct spinor M_max=0.902 |
| DPHYS-34a-1 | Fold survives at phi=gap | PASS | 34 | d2=1.226 at phi=gap (increases from bare 1.176). Fold stabilized |
| TRAP1-34a | V(B1,B1)=0 exact (full 8-gen kernel) | CONFIRMED | 34 | U(2) singlet selection rule. Permanent structural result |
| DPHYS-34a-2 | V(B2,B2)>0.05 at phi=gap in D_phys basis | PASS | 34 | V=0.086 (+50% enhanced). U(1) dominant (63%) |
| RPA-34a | d2S>0.54 at phi=gap at dump | CONSISTENT | 34 | d2S=180.09 (333x margin). Monotonically increasing with phi |
| DPHYS-34a-3 | M_max>1.0 at phi=gap (step wall) | FAIL | 34 | M_max=0.899. 11% shortfall. Superseded by VH-IMP-35a |
| VH-IMP-35a | M_max>=1.0 (smooth wall + corrected imp) | PASS | 34 | M_max=1.445. rho_smooth=14.02/mode, imp=1.0, spinor V |
| BMF-35a | M_max_eff>=1.0 after fluctuations | FAIL at N_eff=4 | 34 | 35% suppression -> M=0.94. Corridor: N_eff>5.5 required |
| MU-35a | mu!=0 in canonical spectral action | CLOSED | 34 | PH forces dS/dmu|_0=0 analytically. Permanent |
| GC-35a | mu!=0 in grand canonical | CLOSED | 34 | Helmholtz F convex, mu=0 global minimum. [iK_7,D_K]=0 permanent |
| PMNS-corrected | theta_23 in [35,55], sin2_13 in [0.01,0.05], R in [10,100] | FAIL | 35 W3-A | R_max=0.57. dE_23/dE_12=5.09 caps R<5.9. sin2_13=0.010 (improved 20x). theta_23=12.2 (4x below PDG) |
| theta13-weak-mixing | sin^2(theta_13) < 0.05 with corrected V | PASS | 35 W3-A | sin2_13=0.010 at BCS point. Spinor V reduces V12*V23 by 5.6x. Enters gate [0.01,0.05] for Delta in [0.05,0.36] |
| INTER-SECTOR-PMNS-36 | R in [10,100] with inter-sector mixing | FAIL | 36 W2-A | All 3 PMNS routes CLOSED on Jensen. R_inter=27.2 available but mixing=0 (Schur on U(2)). s36_intersector_pmns.py |
| WIND-36 | nu != 0 (topological BCS) | FAIL | 36 W2-C | nu=0 at all channels. E_B2/Delta=33.4, deep trivial. mu=0 prevents band inversion |
| BBN-LITHIUM-36 | delta_H/H in [-0.15, -0.03] | FAIL | 36 W2-F | delta_H/H = -6.6e-5, 500x below threshold. BCS is UV-negligible |
| K7-G1-37 | q_7(G1) = 0 in (1,0) sector | FAIL | 37 W1-B | ALGEBRAIC: (1,0) has NO q_7=0 weights under U(1)_7. All weights are -1/sqrt(3) or +1/(2sqrt(3)). Multiplicity charges also nonzero. Blocks OFF-JENSEN-PMNS-37. PMNS classified Level 5. s37_k7_g1.py |

## Session 40 Resolved Gates (neutrino-adjacent)

| Gate | Condition | Outcome | Session | Notes |
|------|-----------|---------|---------|-------|
| NOHAIR-40 | T variation < 10% over v in [10,100] | FAIL | 40 | T varies 64.6%. Gap hierarchy (3 LZ thresholds over 4 decades). S varies only 18.1%. Mode-dependent excitation analogous to MSW adiabaticity |
| B2-INTEG-40 | <r>(B2) < 0.42 | PASS | 40 | <r>=0.401, g_T=0.087. B2 weight corrected 93->82%. Near-integrable island |
| B2-DECAY-40 | t_decay(B2) < 1 or > 10 | B2-FIRST (t=0.922) | 40 | Oscillatory dephasing, not FGR. 89.1% retained permanently. Eigenstate decomposition has off-diagonal B1/B3 content in states 3,4,5 |
| QRPA-40 | Any omega_n^2 < 0 | FAIL (STABLE) | 40 | All positive. 97.5% EWSR in single B2 mode. V_rem purely time-even |
| M-COLL-40 | sigma_ZP > 0.09 | FAIL (CLASSICAL) | 40 | M_ATDHFB=1.695, sigma_ZP=0.026. B1 dominates 71%. Van Hove velocity zero kills B2 contribution |
| HESS-40 | Any transverse H_ii < -h^2 | FAIL (COMPOUND NUCLEUS) | 40 | 22/22 positive. Min H=1572 (g_73). Jensen fold is 28D local minimum. Off-Jensen INCREASES S_full |

## Open Gates

| Gate | Condition | Status | Notes |
|------|-----------|--------|-------|
| R-full | R_full(tau; Lambda=1) in [17, 66], tau in [0.15, 0.35] | PENDING | Finite-cutoff R from Goal 2 data |
| R-graded | Inter-sector R (one eigenvalue per Z_3 gen) in [17, 66] | PENDING | From Goal 1 data |
| R-BCS-modedep | R from mode-dependent BdG eigenvalues in [10, 100] | PENDING | Escape from 29Ba strong-mixing |
| PMNS-offJensen | sin^2(theta_13) in [0.015,0.030], theta_23 in [35,55] off-Jensen | PENDING | 2D U(2)-invariant grid search |
| P-30w | sin^2(theta_W) in [0.20, 0.25] at off-Jensen BCS min | PENDING | Pre-registered 29Bb |
| NEW1-theta23 | delta_E_split(B2; phi) < W_B2 = 0.058 | PENDING | Joint SP-Naz-Neutrino constraint |
| NEC-dump | NEC holds at tau=0.19 | PENDING (likely PASS) | Ricci eigenvalues positive at 0.190 (computed 33 W3, not yet formally gated) |
| OFF-JENSEN-PMNS-37 | sin2_23 in [0.3,0.7], sin2_13 in [0.005,0.05], R in [10,100] | BLOCKED | Blocked: K7-G1-37 FAIL closes prerequisite |
| CUTOFF-SA-37 | S_f(tau) has minimum near fold | CLOSED | 37 | Structural monotonicity theorem. S_f monotonically increasing. |
| PMNS-corrected | (moved to Resolved) | FAIL | 35 W3-A |
| theta13-weak-mixing | (moved to Resolved) | PASS | 35 W3-A |
| PMNS-DYNAMICAL-41 | sin2_23 in [0.3,0.7], sin2_13 in [0.01,0.05] from diagonal ensemble | PROPOSED | Extracts 3x3 effective PMNS from B2-DECAY-40 eigenstate decomposition. Transit thermalization as mixing mechanism |
| B2-SPLIT-41 | Intra-B2 quartet splitting / (B2-B1 splitting) ~ 1/33 | PROPOSED | From QRPA or off-Jensen BCS. If confirmed, identifies Delta m^2_21 with B2 degeneracy lifting |
| MSW-INTERNAL-41 | Nonzero flavor conversion from 8x8 LZ transit | PROPOSED | Full level-crossing diagram m_k^2(tau). Mode-dependent adiabaticity as internal MSW |

## Gate Outcomes
Do not count gates or compute ratios. Consult individual entries for what each outcome constrains.
