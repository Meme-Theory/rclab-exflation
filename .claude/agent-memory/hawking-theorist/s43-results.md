---
name: S43 Key Results
description: Session 43 Hawking computations (GSL, first law, trans-Planckian, greybody) and CC workshop with Volovik
type: project
---

## S43 Hawking Computations

### GSL-43 (W6-5): PASS
- dS_gen/dt >= 0 at all 300 timesteps, 2560x safety margin
- Three-term: S_spec (monotonic by CUTOFF-SA-37) + S_GGE (0->2.21 nats) + S_defects (decreasing but subdominant)
- Bekenstein saturation: 1.5% (69x below bound). System deep sub-Bekenstein
- S_ent=0 confirmed: no information paradox (Parker regime, no horizon)

### FIRSTLAW-43 (W6-6): PASS
- dE = X_tau*dtau + T_a*dS_GGE + sigma*dA + mu*dL verified to 1.26e-7 across 8 tau
- Effacement hierarchy: geometric (10^0) >> thermal (10^{-3.8}) >> walls (10^{-4.4})
- GGE mode temperatures: T_B2=0.579, T_B1=0.296, T_B3=0.163 M_KK (population inversion)
- BCH correspondence complete: S_spec~M, tau~J, X_tau~Omega_H, T_a~T_H, S_GGE~S_BH

### TRANSP-43 (W6-7): PASS (structural)
- 0.000% variation across max_pq_sum = 4,5,6,7 (255-1248 eigenvalues)
- THEOREM: BCS quantities depend entirely on (0,0) sector = fixed 16x16 matrix
- Stronger than Hawking trans-Planckian: not insensitivity but IDENTITY
- f_NL=0.014, xi_KZ=0.00220 are infrared predictions immune to UV physics

### GREYBODY-43 (W6-8): PASS
- Gamma = 0.7093 = 1/sqrt(alpha), alpha=1.9874
- Closes temperature triangle: T_acoustic = T_Rindler * Gamma = 0.112 M_KK
- T_a/T_Gibbs = 0.993 (0.7% self-consistency)
- Soft analog horizon: xi_h = 1/sqrt(alpha) = 0.709 (finite width)
- Qualitatively opposite to Schwarzschild: Gamma decreases with omega (no centrifugal barrier)

## CC-113 Workshop with Volovik

### Converged
- C1: Spectral action is WRONG gravitating functional (entropy/free energy, not energy). Legendre duals.
- C2: Flat-band B2 = CDM candidate (W=0 exact, v_group=0). Mixed DM: 85% CDM + 15% HDM.
- C3: r ~ 10^{-9} structural prediction (BCS tensors). r > 10^{-5} excludes framework.
- C4: First-sound ring at 325 Mpc is most distinctive LSS prediction.
- C5: Carlip L=1.74mm has no dynamical selection mechanism.
- C8: Q-theory equilibrium nullifies S(0). 113-order gap from GGE perturbation only.
- C9: DM and CC are same problem (both need 120-order suppression from M_KK^4).

### Divergent
- D1: CC suppression: holographic bound (Hawking) vs generalized Gibbs-Duhem (Volovik)
- D2: n_s mechanism: spectral dimension flow (Hawking) vs Lifshitz anomalous dimension (Volovik)
- D3: Priority: CDM-RETRACTION-44 (Hawking #1) vs SAKHAROV-GN-44 (Volovik #1)
- D4: N_3 topological invariant: Volovik proposes, Hawking predicts FAIL

### Emerged
- E1: Paper 20 entropy + Gibbs-Duhem = Legendre duality (single formula: E_grav = S_fold - sum T_k S_k)
- E2: S_F^Connes=0 constrains Sakharov vs spectral action (independent G_N tests)
- E3: Multi-temperature Jacobson equation for GGE (8-fluid cosmology, negative cross-T)
- E4: Cutoff function f as computationally constrained unknown
- E5: Lifshitz eta at tau=0 might be zero (round metric has no van Hove singularities)

## S44 Hawking Proposals
1. HOLOGRAPHIC-SPEC-44 (CRITICAL): boundary-mode spectral action
2. DIMFLOW-44 (HIGH): spectral dimension flow for n_s
3. JACOBSON-SPEC-44 (MEDIUM): first-law propagation to Friedmann
4. MULTI-T-JACOBSON-44 (MEDIUM): 8-temperature Jacobson equation
5. FIRST-SOUND-44 (MEDIUM): Fisher forecast for 325 Mpc feature
