# Kitaev-Quantum-Chaos-Theorist Agent Memory

## Top-Line Verdict: FABRIC-SCALE INTEGRABLE; single-cell thermalizes (RETRACTED-S39 scope)
"GGE never thermalizes" is RETRACTED-S39 (atlas-04 T3 BROKEN; INTEG-39 DECISIVE FAIL, S96 re-confirm: V_phys 13% non-separable, Brody beta=0.633 = 63% GOE, Thouless g=0.60, t_therm~6 M_KK^-1 at SINGLE-CELL). What survives: FABRIC-SCALE integrability (CG(24) <r>=0.367; r_pooled=0.422) + diabatic transit-freeze (R_therm=t_therm/t_transit=5251.82, S_ent=0, S95) + "transit IS the physics" (atlas-10 #8). Two-process distinction: ADH prethermalization (dephasing, 10^578 t_univ) is NOT interaction-thermalization (t_therm~6 M_KK^-1 canonical; registry wins over my older notes). Register reconcile landed S100b housekeeping §A. Kill authority NOT triggered: no scrambling, no MSS violation at fabric scale (lambda_L=0).

## Framework Summary
- Internal space: SU(3) with Jensen deformation tau (volume-preserving). Van Hove fold at tau~0.190
- D_K(tau) block-diagonal in Peter-Weyl basis (off-diag < 8.4e-15). AZ class BDI, T^2=+1
- Jensen breaks SU(3)->U(1)_7 exactly: [iK_7, D_K]=0 at ALL tau (WHY single-particle is integrable)
- BCS instability: 1D theorem, any g>0 flows to strong coupling
- Spectral action stabilization DEAD: monotonicity theorem + HESS-40 (27 closures)
- Paradigm: compound nucleus dissolution via ballistic transit, not equilibrium

## Key Numbers
- S_inst=0.069, tunneling 93%, GL barrier=0.156, E_vac/E_cond=28.8, g*N(E_F)=2.18
- Pair vibration: omega=0.792, 85.5% strength, coherence 6.3x
- 0D limit: L/xi_GL=0.031, Z_2 balance=0.998
- dS/dtau=+58,673 at fold. Transit: 38,600x faster than BCS formation
- T_Gibbs=0.113 M_KK, T_acoustic/T_Gibbs=0.993 (0.7%)
- MSS bound: lambda_L_max=0.710 M_KK, actual lambda_L=0
- V(B2,B2) 86% rank-1 (WHY B2 subsystem near-integrable)
- V_bare rank-1 captures 64%, residual 36% breaks R-G but produces NO chaos
- ADH prethermalization: t_therm/t_universe = 10^{578} (DEPHASING only; interaction-thermalization is t_therm~6 M_KK^-1 per INTEG-39 — two distinct processes, do not conflate)

## Headline Diagnostics (full table in integrability_hierarchy.md)
- Single-particle D_K: <r>=0.321 sub-Poisson, Brody beta=0.001 (S38/S53)
- Many-body 256-dim: OTOC~t^{1.9}, no Lyapunov. t_scr/t_transit=814x (S38)
- N_pair=3 pairing: <r>=0.478 RESOLVED by SFF (slope/GUE=0.002) + Sigma^2=9.92 (S65)
- N_pair=4 half-fill: <r>=0.453, SFF slope/GUE=-0.002. Blocking reinforces integrability (S66)
- 36D classical moduli: lambda_chaos=0.0, anharmonicity 6e-5 (S66). Closes last chaos channel
- Multi-cell Plancherel 10 irreps: r_pooled=0.422, Ordered Veil permanent (S74)
- Sector-resolved kNN PASS (S100b W4-2): Poisson at k=1,2,3 in (p,q) sectors; <r> 0.321->0.3910 (+1.34sig vs Poisson, GOE 40sig); V_k=0.88/0.74/0.66; beta1=0.055. CHAOS-1 sub-Poisson = degeneracy-superposition artifact, RESOLVED. Conditional on LC-lineage canonicity (UNTRUSTED-UPSTREAM)
- Sector-resolved P(s)/Berry-Robnik PASS-pooling-artifact (INV3-W1-2, investigation track): beta_block=-0.064+/-0.014 (75 blocks >=50 unique levels, PASS band [-0.15,0.30], Poisson beta=0); rho_pooled=1.0 (pure-Poisson limit); r_pooled=0.388, <r>_block=0.393 (vs Poisson 0.3863); chi2 Poisson 0.0034 << semiP 0.046 << GOE 0.081 (Poisson best 14x); beta_block(L14)=-0.107 L-stable; beta_pooled=-0.221 (superposition drives BELOW Poisson, M=90 blocks). INDEPENDENT confirm of kNN via orthogonal P(s)-FORM axis: each Peter-Weyl (p,q) sector intrinsically Poisson; CHAOS-1 pooled <r>=0.422 excess = superposition residual NOT intrinsic semi-Poisson. lambda_L=0 per sector, MSS kill NOT triggered. L12 cache HERE is 166896-mult/6997-unique (p+q<=12); 155984/78080 are the L10 figures. Method pin: P(s)/beta on UNIQUE level seq per sector (raw mult = degeneracy artifact; reconciles S46 <r> 0.321->0.439 correction)
- RP-resonance/BdG-Liouvillian at fold FAIL (INV10-W3-2, investigation track): decay form @ tau_fold=0.19 is NON-DECAY (persistent osc), NOT power-law; alpha(C(t) tail)=+0.004 (A2-fold predicts +0.5); form tau-INDEPENDENT across all 5 tau slices {0.15,0.175,0.19,0.205,0.25}; NOT tau-localized (RP-gap margin -0.013, DOS-edge margin +0.039<m_loc=0.05). DECISIVE driver: NO van-Hove A2 branch point at gap edge -- single-particle |lambda| band-bottom DOS exponent=+0.21 (DOS VANISHES, parabolic ~sqrt(E) edge), BdG gap-edge p_edge~-0.13 to -0.28, never -0.5. BCS gap Delta=0.464 REGULARIZES the would-be van-Hove edge (sqrt(xi^2+Delta^2) smooth/parabolic at E~Delta). Extractor validated: synthetic 1D fold E=-2cos(k) recovers alpha=0.4985. RETIRES edge-of-chaos (survey A4) as DYNAMICAL claim; firms bulk-integrability A3; consistent w/ prior LIOUVILLIAN-52 finite gap gamma_RP=0.0398 M_KK (t_deph/t_transit=139729). framework-chaotic-instantons.md Sec 5.4 PRELIMINARY branch-point reading + Sec6 "(D) edge-of-chaos genuinely new physics" NOT borne out -> designated-writer down-tag queued. lambda_L=0 stands, MSS kill NOT triggered. Method: C(t)=|sum_m sqrt(rho_m)exp(-iE_m t)|^2 (flat |A_mn|^2; alpha set by DOS edge per Watson lemma); Liouvillian freqs = outer-diff of 2N BdG eigenvalues (NEVER materialize (2N)^2x(2N)^2 superop)
- CG(24) graph diffusion: t_dec/t_transit=820x (S73a), heat kernel t_mix/t_transit=237 (S73b)
- GGE Bell: all 8 modes S>2. Non-thermal: CV(T_eff)=47.9% (S70)
- Bertini-Essler vs ADH: agree within 1 OOM. Both give ~10^{580} t_universe (S66)

## Key Structural Results
- Berry-Tabor confirmed: conserved [iK_7,D_K]=0 at all tau
- GGE-KMS: 8-fold modular decomposition PROVEN (Tomita-Takesaki, Type III_1)
- Spectral moment decoupling: F_{-1}(CC) vs F_{+1}(NEC) independent (PERMANENT)
- Josephson preserves integrability: rank-1, B=sum_k b_k is central (S56)
- N_pair=3 blocking: <r> DECREASES with filling (0.707->0.509->0.414) (S56)
- <r>=0.478 resolution: short-range repulsion without long-range rigidity (S65)
- V_fold===V_8x8_raw to machine epsilon: single geometric fault line (S74 W4-I)
- DC fraction scales as ~N_cells^{-1.26}: finite-size contamination, not conserved charge (S74)
- Substrate 4D emerges from Seeley-DeWitt a_2 of D_K, NOT graph spectral dim (S73b)

## S58 Dynamic Structure Factor
- Three bands: Leggett 46%, BA 23%, pair-breaking 31%. D_JS(GGE||thermal)=0.024
- B2/B3 asymmetry 10:1 = GGE fingerprint. Sharp modes, no diffusive background

## ETH-violation (eigenvector axis, NEW) — INV10-W3-4
- beta_fabric=0.181 (<<0.5) = eigenstate-level Ordered Veil (fabric eigenstates ARE non-thermal); FIRST eigenVECTOR-axis integrability diagnostic, orthogonal to all my eigenVALUE results. INFO (cell-vs-fabric eigenstate discriminator inverted Dbeta=-0.15: cell D=28-70 too small + op near-conserved; C2 SHARPENED not resolved). See [inv10-w3-4-eth-violation.md](inv10-w3-4-eth-violation.md)

## Linked Files
- [integrability_hierarchy.md](integrability_hierarchy.md) -- master diagnostic table (50 rows) + all 32 gate verdicts + structural results
- [methodology_and_data.md](methodology_and_data.md) -- methodology lessons (r-ratio, SFF, OTOC, Thouless, OEE, rank-1-BCS-pair-lift, d_s on small graphs)
- [inv10-w3-4-eth-violation.md](inv10-w3-4-eth-violation.md) -- ETH-violation result + operator-design facts (number-conserving op for cell; spinor bilinear for fabric; Delta=Sum sqrt(rho)P_k is dN=+-1 so zero within sector)
