# Feynman-Theorist Agent Memory

Path integral, QED/QFT, renormalization, Feynman diagrams, "shut up and calculate." 14 papers in `/researchers/Feynman/`.

## Memory Index
- [library_gaps.md](library_gaps.md) -- Critical gaps in Feynman library (heat kernel, spectral action quantization, Parker creation, Richardson-Gaudin). New researcher recommendations.
- [s41_s42_key_results.md](s41_s42_key_results.md) -- S41-S42 results updating Feynman Test scorecard. S_F^Connes=0, Z(tau)=74731, CDM-from-geometry, w=-1+O(10^{-29}).

## Feynman Test Scorecard (s40 update)
| Step | Status |
|------|--------|
| 1. Write the action | CLOSED (spectral action route). S_full monotonic along Jensen + local min transverse (HESS-40). S_f monotonic for all monotone f. 27 equilibrium closures total. Post-transit EFT action is OPEN (Computation C). |
| 2. Propagators | DONE -- G_BdG has anomalous component F=Delta/(w^2-E_k^2). |
| 3. Vertices | DONE -- GL 4-pt: V_4=-24b. Cubic FORBIDDEN (U(1)_7 charge). V matrix corrected+verified. |
| 4. Power count | DONE+RG -- 1D marginal. beta=-g^2. Two-loop g*=1. Self-consistency alpha=0.478 (B2). |
| 5. Compute something | DONE -- ED N=8 E_cond=-0.137. T_acoustic/T_Gibbs=0.993 (0.7%). GSL structural. |
| 6. Check unitarity | DONE -- OPT-35 PASS to 2.2e-12. QRPA-40 stable (min omega^2=2.665). |
| 7. Compare to data | PARTIAL -- sin^2=0.333 at s=0.190. BBN FAIL (500x short). PMNS=0 on Jensen. |

## Constraint Map (s40 update)
- **W4 (spectral action monotone)**: CONFIRMED along Jensen AND transverse. HESS-40: 22/22 positive, min H=+1572, margin 1.57e7. Jensen fold is 28D local minimum.
- W1-W3, W5-W6: unchanged from s36
- **27 total equilibrium closures**: S17a through HESS-40. Search COMPLETE.
- **QRPA stable**: margin 3.1x, V_rem purely time-even
- **Quantum delocalization CLOSED**: sigma_ZP=0.026 < 0.05, M_ATDHFB=1.695 (0.34x G_mod)

## Key Session 40 Results
- **HESS-40 FAIL (COMPOUND NUCLEUS)**: 22/22 transverse H positive. Min=1572 (g_73 u(1)-complement). Condition 12.87. 27th closure.
- **T-ACOUSTIC-40 PASS**: T_a/T_Gibbs=0.993 (acoustic metric, 0.7%). T_acoustic/Delta_pair=0.341 (E5 range 0.3-0.5).
- **GSL-40 PASS (STRUCTURAL)**: v_min=0. All 3 entropy terms individually non-decreasing. 0 negative steps.
- **CC-TRANSIT-40 PASS**: delta_Lambda/S_fold=2.85e-6. GGE/Gibbs/fold agree 0.2%.
- **B2-INTEG-40 PASS**: <r>=0.401 (Poisson), g_T=0.087, rank-1=86%. B2 weight corrected 93->82%.
- **QRPA-40 FAIL (STABLE)**: min omega^2=2.665, margin 3.1x. V_rem^odd=0. 97.5% EWSR in single B2 mode.
- **PAGE-40 FAIL**: S_ent max=0.422 nats (18.5% Page). PR=3.17. Poincare recurrences.
- **NOHAIR-40 FAIL**: T varies 64.6% [10,100]. S varies 18.1%. Gap hierarchy drives mode-dependent LZ.
- **B2-DECAY-40 B2-FIRST**: t_decay=0.922. Oscillatory dephasing, NOT FGR. 89% permanently retained.
- **M-COLL-40 FAIL (CLASSICAL)**: M_ATDHFB=1.695, sigma_ZP=0.026. B1 dominates 71%.
- **SELF-CONSIST-40 FAIL (ACCELERATES)**: dwell 0.58x uncorrected. Shortfall worsens to ~114,000x.
- **Corrections**: B2 weight 82% not 93%. Pauli convention A->B. M_ATDHFB O(1) not O(100).

## Forward Program (identified in s40 collab review)
- **Computation A**: Heat kernel at finite density. delta_a_2 = -N_pairs * Delta^2 (shift in gravitational coupling). Computable from existing data.
- **Computation B**: KK graviton mass from HESS-40 eigenvalues. Compare to BCS gap hierarchy.
- **Computation C**: Post-transit effective Lagrangian. 8-species massive fermion EFT with known V_{kl} couplings. Feynman rules, power counting, decay rates.
- **Key insight**: GSL monotonicity and spectral action monotonicity are the SAME structural fact in different language (entropy = Euclidean action increasing).
- **Key insight**: T_acoustic agreement (0.7%) may be derivable from one-loop determinant det'(-d^2/dtau^2 + alpha).

## Key Structural Results (persistent)
- KO-dim=6 (parameter-free). SM quantum numbers C^16. [J,D_K]=0. g1/g2=e^{-2tau}.
- Lambda_min turnaround: tau=0.2323, depth 6.28%
- Van Hove DOS: g(omega) ~ 1/sqrt(omega-omega_min) at 1D band edge
- V_spectral(s) monotonically increasing -- internal spectral action alone INSUFFICIENT
- B2 is near-integrable island: Poisson, rank-1 86%, g_T=0.087
- Transit is classical: sigma_ZP=0.026, M_ATDHFB=1.695
- Compound nucleus dissolution IS the framework (not equilibrium stabilization)

## Critical Lessons
- USER DIRECTIVE (s40): "Stop Weighing Fails - a map doesn't fail because it draws a coast."
- USER DIRECTIVE (s40): "What energy would a graviton have? Where does the instanton energy go?"
- USER DIRECTIVE: Follow the energy. 69.1 M_KK^4 deposited, 443x condensation energy.
- USER DIRECTIVE (s36): "Give me the LAVA."
- USER DIRECTIVE (s35): "You are here to make predictions; not bitch that none are made."
- **Tr(D_K) = 0 ALWAYS. Spectral action = sum|lambda|. NEVER confuse these.**
- **NEVER use A_antisym where K_a_matrix is needed. Factor 5x error.**
- **Spectral action penalizes BCS (F.5 wrong sign). S_full is wrong functional for stabilization.**
- **Self-consistency (GCM) reduces M_max by ~50%. Margin matters.**
- **Super-critical Schwinger regime: S_inst=0.069 << 1. P_exc=1.000. Not perturbative pair creation.**

## Data Inventory (s40 additions)
| File | Contents |
|------|----------|
| s40_b2_integrability.npz | B2 integrability: <r>, g_T, rank-1, B2 weight correction |
| s40_acoustic_temperature.npz | T_acoustic, alpha, Barcelo metric, B1 comparison |
| s40_gsl_transit.npz | GSL: 3 entropy terms, Bogoliubov unitarity, v_min=0 |
| s40_cc_transit.npz | CC shift: delta_Lambda, branch decomposition, 3 states |
| s40_nohair_sensitivity.npz | No-hair: T(v), S(v), v_crit per branch, LZ |
| s40_qrpa_modes.npz | QRPA: 8 eigenvalues, EWSR, V_rem decomposition, stability margin |
| s40_internal_page_curve.npz | Page curve: S_ent(t), PR, Poincare recurrences |
| s40_b2_decay_out.npz | B2 decay: N_B2(t), eigenstate decomposition, dephasing |
| s40_hessian_offjensen.npz | Hessian: 22 directions, eigenvalue hierarchy, condition number |
| s40_collective_inertia.npz | ATDHFB: M_coll(tau), sigma_ZP, mode decomposition |
| s40_self_consistent_ode.npz | Self-consistent ODE: trajectories, dwell times, energy conservation |

## Ricci Gauge Kinetic Results (s35 -- VERIFIED)
- Ric_su2/Ric_u1 at s=0.190: **0.832** (sin^2_combined = 0.333 with NCG 3/5 trace)
- RGE MATCH at M_KK=10^{10.06} GeV (0.3% accuracy)
- Spin Casimir **PERMANENTLY EXCLUDED**: sin^2=0.523 > 3/8

## Session History (compressed, s16-s40)
- s19d-s20b: ALL perturbative mechanisms closed. Constant-ratio trap = Weyl's law.
- s22: Block-diag theorem. Pomeranchuk. BCS bifurcation. Clock constraint.
- s23a-s24b: Venus moment. V_spec monotone. Sagan 3%.
- s34: Correction session. [iK_7,D_K]=0. Schur. Trap 1. Van Hove.
- s35: N_eff resolved. BCS 1D theorem. Mechanism chain 5/5 unconditional. Sagan 32%.
- s36: TAU-STAB FAIL. Needle hole 376,000x. BBN FAIL. GL cubic forbidden. 14 computations.
- s37: CUTOFF-SA-37 FAIL (theorem). F.5 FAIL (wrong sign). Instanton gas. Paradigm shift.
- s38: Ordered Veil. CC-INST-38 closed. Schwinger-instanton duality. Permanent GGE. CHAOS ordered.
- s39: 20 computations. GGE permanence, Schwinger duality, Friedmann-BCS all closed/retracted. Compound nucleus confirmed.
- s40: Structural cartography. 27th closure (HESS-40). T_acoustic 0.7%. GSL structural. Classical transit. B2 integrable. Compound nucleus IS the framework.
