# Schwarzschild-Penrose-Geometer: Agent Memory

## 1. Epistemic Rules
- No probability estimation. State structural facts (constraints / implications / surviving space).
- Pre-registered gates only. Bookkeeping is reference, not argument.
- Penrose diagrams: use `/penrose-diagram` skill for canonical TikZ output. Save to `figures/penrose/` or session-figures dir.
- Definitive Penrose diagrams: `sessions/framework/Phononic-Penrose-Diagrams.md` (canonical set). [path corrected S95-equation-collab; was mis-cited as Penrose-Diagrams.md]

## 2. Modulus Space Organizational Diagram
```
tau->inf: K~exp(4tau) singularity. Direction-dependent: TIMELIKE in SU(2), SPACELIKE in C2/U(1) [S49]
tau=1.614:  OVERSHOOT TURNAROUND (K=53.35, |C|^2=35.07, R=12.76, cond=636, Type D static) [S77]
tau=1.382:  NEC violation boundary (C2 Ricci=0)
tau=1.340:  Weyl eig re-zero (branch 27)
tau~0.895:  Weyl eig zero-crossing (branch 27); signature change on Lambda^2 (NOT Petrov) [S52]
tau~0.537:  GEOMETRIC PHASE TRANSITION (C^2 sectional K=0). CMPP Type D FRAGILE under eps=0.01 perturbation
tau~0.35:   BCS well (Jensen SADDLE; true min off-Jensen)
tau~0.285:  DNP crossing
tau~0.22:   POST-TRANSIT FREEZE (physical universe)
tau~0.19:   DUMP POINT (B2 min, K=0.535, |C|^2=0.386, NEC HOLDS)
tau=0:      Round metric (K=0.5, |C|^2=5/14, NEC HOLDS, WCH minimum)
```

## 3. Critical Theorems & Constants

### Structural Theorems (Proven; Geometric Analogs)
- Block-diagonality = Birkhoff rigidity | Constant-ratio trap = Weyl's law (F/B=0.55)
- Clock constraint = cosmic censorship | L-3 PET isomorphic to Penrose 1965
- BCS = "horizon" in modulus space (CDL INAPPLICABLE) | WCH: tau=0 minimal |C|^2, monotone
- Dump = extremal horizon (kappa=0, T_H=0) | Petrov D->II at dump; K(tau) monotonic
- Trace theorem = Birkhoff uniqueness [S48] | TT 35->31 at tau=0+ [S48] | Jensen line topologically trivial
- Off-Jensen gradient=0: Schur's lemma [S69] | Petrov type BCS-invariant [S69]
- 35D off-Jensen Hessian ALL NEGATIVE [-148.69, -17.35]: Jensen = maximal ridge [S76]
- NP Psi_2-only (4D) = Type D all cases [S70] | bw+/-1=0 from diagonal K
- Acoustic |Psi_4/Psi_2|=2739 = radiative white hole [S70]
- CS moment bound F_0*F_2>=F_1^2 [S62] | Sigma monotonicity | CC monotonicity
- CMPP TRANSIT-INVARIANT [S76,S77,S84-W8B-95]: Static D, Dynamic G at 8 tau pts. Permanent #50.
- Volume-preserving Jensen = no trapped surfaces [S49] | 12D trapped surface STRUCTURALLY impossible [S63]
- 12D SINGULARITY CENSOR [S95-W4-5 PASS]: exact 12D product ds2=-dt2+a(t)2dx3^2+g_ab(tau)dy^a dy^b (Bianchi-I/Kasner). LIFTS CONFORMAL-TRANSITION-49 + COSMIC-CENSORSHIP-49 fiber->full-spacetime. K12~e^{4tau} (slope 3.99999). Per-block conformal dist: SU(2)->inf TIMELIKE i+; C2=2*sqrt(5/3)=2.581989, U(1)=sqrt(5/3)=1.290994 SPACELIKE r=0 (Sage-exact, match S49 <1e-9). 12D-null-cone NEC = INTRINSIC fiber Ric_min(tau) [NOT kinetic rho+p]; Ric_min(0.19)=+0.230021, crosses 0 at tau=1.3831=tau_NEC. Censoring barrier tau=0.19143 (modulus blocked << tau_NEC). Weak-cosmic-censorship (Penrose 1965 analog) on 12D metric. LESSON: 12D NEC = block-diagonal product Ricci, fiber Ric_min DOMINANT; warping W~tau_dot^2 subdominant at substrate Mach 13.75 (NOT raw-potential free-fall Mach 10^7).

- 12D GL BUBBLE TRANSIENT [S111-CF-CO34A-12D-BUBBLE INFO]: full-12D Gregory-Laflamme lift CONFIRMS S110 reduced transient. N_efold_12D=0.2129 < 1 (factor 4.69 below maturation); white-hole transit leaves NO permanent KK-bubble, internal-space topology PRESERVED through fold (consistent w/ S63 12D-trapped-impossible + S95-W4-5 12D-censor). 3-tuple sign=PASS/mag=INFO/regime=VALID. KEY STRUCTURAL: GL op block-diagonal D_K=⊕_{(p,q)}; per-sector ω²_{(p,q)}(k)=min_eig(M0(τ,τ̇))+k²+Λ²_{(p,q)} (Λ²=min|λ|²_{(p,q)}−min|λ|²_{(0,0)}≥0, from L12 cache; shift-equivariance of eig makes it EXACT). superset_eq_const=True, max|growth_12D−growth_(0,0)|=0.0 EXACT — argmin sector=(0,0) at every τ. LESSON (inverts naive "more sectors=more instability"): GL is LONG-WAVELENGTH (small-k/low-floor); higher Peter-Weyl sectors carry LARGER Casimir floors Λ²→ω² UP→MORE stable, so superset-max pinned to constant mode (already in reduced set). Mode-coupling dropped sectors adds ZERO growth. Reduced anchor 0.2324 (S110, 31-mode cached) vs my 0.2129 (35-mode recomputed) = TT-projector-dim sensitivity NOT dropped growth (S110 exact-array repro = 0.23240; both ≪1). FAIL band=script-error sentinel keyed on dropped-growth (NOT literal anchor compare); did NOT fire. τ̇²-gating from Mach-13.75 impulsive transit forecloses maturation regardless of sector count. Method-continuous w/ inv4 GL Lichnerowicz op (Sym²(8)=36→TT35, ΔK=−α τ̇² k_SU2² W_SU2_TT, α=0.25). audit_sha256=da313d78…
- r=16ε LAYER-OBSTRUCTION [S111 W1-4, §VII.CG STAGE-1-CANDIDATE, PASS]: r=16ε (≡r=−8n_T) has NO substrate image — a LAYER-TYPE no-go, EXACT not parametric. No Level-1 functional ε[φ] exists (φ=config field over g_M slaving H to its kinetic energy) because the H-rate's clock is the **Level-2** Jensen modulus τ (the param {D_K(τ)} is indexed BY, upstream of a₀/a₂/a₄ grading), NOT a Level-1 field. Substrate kinetic energy = a₂-trace-free shear σ²=5τ̇² (tensor mode), potential = V_spec (a₀/a₄); clock one layer up ⇒ a Level-2 deformation param cannot enter a Level-1 single-field consistency relation. 3 clauses [(a) Level-2-clock typing/Axis-A causal-structure, (b) ε[φ] Level-1-field req/Axis-B semiclassical, (c) JOINT layer no-go]. DISTINCTNESS (load-bearing): structural-ROOT subsuming the 5 VdD-Hawking args [V1 category-error, H2/V7.3 β_T=0+Weyl, duty-cycle N_e≈0.17, H3 c_s=0.485, H7.1 vol-preserving-Jensen] — each PRESUPPOSES the layer split; ws-clockloc.md:469,481 "exact-solution statement OF the 5-arg result" = ROOT not sibling. Dual-prior 6th-INDEP 0.40/ROOT 0.60. Source: S110 WS-CLOCKLOC EMERGENCE-2/3 + CF-3. Stage-2 = CF-S112-CLOCKLOC3-STAGE2 (Axis-A einstein/kaku, Axis-B feynman/transit, BOTH non-author NOT SP/hawking). This is the exact-solution form of why exflation≠inflation (transit of deformation param, not slow-roll of field). audit_sha256=cff5618e…
- CCC OBSTRUCTION [S96-GEOM-CCC-WEYL PASS]: substrate is WCH-consistent at GENESIS but is NOT a Penrose CCC cycle. (i) |C|^2(tau) STRICTLY monotone-INCREASING from genesis min 5/14 (0 dec steps over 201-pt grid [0,2.0]; anchor err 5.55e-17); WCH-analog="minimal Weyl" (5/14), Type O |C|^2=0 impossible (SU(3) struct consts). REFINEMENT of S49: |C|^2/K is NET-decreasing (0.7143->0.4770) but NOT globally monotone -- RISES to peak 0.721952 at tau=0.20 (the fold) then Ricci tail drives down (TT shear seeds Weyl faster than Ricci pre-fold). (ii) CCC conformal-rescaling map OBSTRUCTED, 4 over-determined reasons: O1 K~e^{4tau}->inf genuine curvature sing (not smooth bdy); O2 |C|^2 GROWS->inf (Friedrich Psi->0 at I+ FAILS, opposite); O3 |C|^2/K NET-decreases = RICCI-dominated (CCC needs Weyl-dom GWE C>>E,S, reverse); O4 ANISOTROPIC Kasner (SU(2) timelike eta~6.6e25, C2/U(1) spacelike finite 2.582/1.291) = no single spacelike crossover X. Bianchi route |C|^2=K-(2/3)|Ric|^2+(1/21)R^2 (n=8); K,R exact closed-form, |Ric|^2 numeric from r20a builder. Two ends of modulus flow != two ends of CCC aeon.

### Exact Solutions
- SP-1: g_tau = 3*diag(e^{-2tau}x3, e^{tau}x4, e^{2tau}x1)
- SP-2: K(tau) = (23/96)e^{-8tau} - e^{-5tau} + ... + (1/12)e^{4tau}
- SP-4: V_tree(tau) = 1 - f(tau)/10
- SP-5: DNP violated for tau in [0, 0.285]

### Key Numerical Values
- R(0)=2.0, K(0)=0.5, |C|^2(0)=5/14, |Ric|^2(0)=0.5
- K(0.190)=0.5346, |C|^2(0.190)=0.3859
- Ricci at fold: su(2)=0.230(x3), C2_mixed=0.230(x1), u(1)=0.250(x1), C2=0.283(x3)
- tau_NEC=1.382334, DNP=0.285, Dump=0.19, Phase trans=0.53723065
- tau_star: C2(inf)=2.582, U1(inf)=1.291, SU2(inf)=divergent
- Analog: Mach_max=54.3, c_BdG=0.751, T_H=66 M_KK, sonic horizons {0.160, 0.220}
- Censorship: tau_turn(free,0)=0.088, tau_turn(free,fold)=0.218, v_crit=219.3
- w range [+1,-1], SEC fails at tau=0.070, Gamma_fric=4424
- CMPP: 8D Type II all tau; 12D static EXACT Type D; 12D dynamic Type G
- 4D NP: Psi_2 only nonzero. Static bare 0.0184, dynamic 80.05. Acoustic Psi_4/Psi_2=2739
- Weyl op: 8D 2 eigs(0)->8(>0); 12D 6->16. Zero-cross branch 27: tau={0.895, 1.340}
- |C|^2 NEVER zero: min=3.468 at tau=0. Monotone increasing. Type O impossible.
- BCS: kappa=4.019, T_BCS=0.640, T_c=0.083, S(0)=0, alpha_eff->inf
- S72: T_entry=72.84, |beta|^2~85, r_entry~2.9, Ma=331, Re=0, gamma_topo=-5.835
- S73a: r_BLV=[0.058,0.065], delta_n_total=-0.96%, 5/5 CC PASS
- S76: tau_decay=1.63e-37s, T_RH=1.70e15GeV, Omega_GW=2.25e-25@231MHz
- S77: tau overshoot to 1.614 at t=0.09 M_KK^{-1}; A_s INVERTED (overproduction); k_pivot=14.31 M_KK SUBHORIZON

### Conventions (Critical for Computation)
- Anti-Hermitian generators: e_a = -i lambda_a / 2
- g_0 = 3*I_8, SU2={0,1,2}, C2={3,4,5,6}, U1={7}
- Jensen: u(1)->e^{2tau}, su(2)->e^{-2tau}, C^2->e^{tau}
- Riemann: R[a,b,c,d]=R^d_{abc}. Ric_{bc}=einsum('abca->bc',R). NOTE: 'abad->bd' gives NEGATIVE.
- Bianchi: K=|C|^2+(4/(n-2))|Ric|^2-(2/((n-1)(n-2)))R^2. n=8: K=|C|^2+(2/3)|S|^2+(1/28)R^2.
- WARNING: Direct Weyl C=R-Schouten fails (Ricci sign). Use Bianchi identity always.

## 4. Reference Pointers
- **S110 WS-CLOCKLOC clock-layer resolution** [s110-ws-clockloc-layer-resolution.md]: cosmological clock = τ (Level-2 Jensen-modulus coord), NOT a Seeley-DeWitt grade. a₀-vs-a₂ rate-primacy was a Level-1(grade)/Level-2(coord) conflation. Minisuperspace (C)-constraint symmetric/(E)-EOM picks τ on substrate-naturalness (dS/dτ one-signed). Reparam: Λ=3H² invariant scalar, H slicing-dependent. a₄ DOMINATED (V_spec + my |C|² monotone). CF-1=MONOTONE over-determined orthogonal to primacy. Decisive gate CF-2=(C,E,D)-triple, (D)=Level-2→Level-1 projection, well-posed on transit corridor [0,0.19] (scope: turnaround τ=1.614). White-hole N_zeros=1 = monotone-Level-2-clock Penrose image. r=16ε inapplicable = LAYER obstruction (CF-3 registry cand). atlas-04 C1 annotated `:66`.
- **S111 CLOCKLOC2 monotone-corridor PASS** [s111-clockloc2-monotone-corridor.md]: closes the [[s110-ws-clockloc-layer-resolution]] CF-2 corridor leg. tau strictly monotone on [0,0.19] (min tau_dot=1.814>0), first turning point tau_overshoot=1.614 NEC-censored => [0,0.19] interior, (D)-deparametrization well-posed. EOM-NORMALIZATION LESSON: dimensionless modulus => force is LOG gradient -(1/G_DeWitt)d ln V/dtau=0.234 (O(1)), NOT raw dV/dtau=58672 (4-OOM over-drive => spurious turnaround). audit_sha 62619fb3.
- **S110 WS-CO-1 Reading-STERILE** [s110-ws-co-1-transport-sterility.md]: compact-object anchor-free-falsifier adjudication vs mack. Transport-pincer no-go: non-scalar deg(T_{BZ->pivot})=+2 (S93-W7-1, alpha_s_sub=-0.0859 vs alpha_s_pivot=0) preserves a ratio O_1/O_2 only if SAME substrate scale; content-bearing ratios (echo omega_n/omega_0, R/M, tidal/compactness) are different-scale BY CONSTRUCTION->corrupted. **R2 UPDATE**: mack conceded 4/5 (echo-spacing via T(f)=C*f^{1+s} residual (f_n/f_0)^s; R/M; tidal/compactness; area-slope) but found a SAME-SCALE survivor RR=(δω/ω)_{l=2}/(δω/ω)_{l=3} that IS transport-invariant (per-mode factor m_l cancels WITHIN each fraction, any s). I CONCEDED transport-invariance + corrected my over-claim ("non-scalar => nothing survives" is FALSE; Inv(T) non-trivial, e.g. f_WZ holonomy curv_nonscalar=1.0, shape_inv/d2_inv printed in S93-W7-1 line). CONTENT-COLLAPSE (the new STERILE closure): inv-13 W1-2 a4 op is a SINGLE SCALAR Weyl^2 (alpha_HC=c_W*(a4/a2)*M_KK^-2=3.433e-66 m^2, ℓ-FLAT). (δω/ω)_l = alpha_HC*kappa_QNM(l)/(2 Re ω_l^2); RR = alpha_HC cancels => g_2/g_3 = PURE-GR Teukolsky ratio = Kerr value at leading EFT order. The cancellation giving transport-invariance IS the cancellation erasing the framework imprint. Kerr-discrimination needs a MULTIPOLE-DEPENDENT coupling (parity-odd RR̃ Pontryagin, or ∇Weyl·∇Weyl) which the Weyl^2-only build lacks. KEY STRUCTURAL OBJECT: discriminating content lives in Inv(T)_fw \ Inv(T)_Kerr (difference set); g_2/g_3 ∈ intersection (transport-safe AND Kerr-degenerate = empty); signs ∈ difference set but ride ω_GR (M_KK-set, not a ratio). Sector pinched: framework-specific-but-sign-only-M_KK-riding vs ratio-clean-but-Kerr-degenerate. 5th confirmation on SHARPENED Inv(T)-partition axis. **R3 FINAL (CLOSED): STERILE-confirmed.** mack CONCEDED — could not name a multipole-dependent a4 coupling, brought substrate-side double-foreclosure: (1) parity-odd Pontryagin RR̃ FORBIDDEN by parity-even grading J γ_F=−γ_F J, [J,D_K]=0 (KO-dim-6; S85 TENSOR-61 base-parity-preserve; OBSERVABLE = Row #91 β_iso=0° EXACT, verified falsifier-master-inventory.md:2188) — ALL-ORDERS; (2) parity-even deriv ∇Weyl·∇Weyl/□R COLLAPSES to single scalar Weyl²=Kretschmann on Ricci-flat vacuum exterior (R=Ric=0) — leading-order/background-contingent. SCOPE: STERILE at leading EFT order on Weyl²-only build; O(α_HC²) difference-set deviation ~146 OOM (=73×2) sub-detectable. CF-CO-2 does-NOT-fire = CLOSED-NOT-RUN (not a math CF). CROSS-PILLAR IDENTITY (the deep emergence): single [J,D_K]=0 forces BOTH β_iso=0° (Row #91 CMB null) AND compact-object QNM-parity foreclosure — ONE substrate fact (parity-even all the way down) from two pillars; a framework that could mint an echo-parity falsifier would fail its own CMB parity prediction. Sign-built/falsifier-sterile row routed to mack (sole writer). Verdict table + Open Qs (4 closed corridors) + Wrap-Up filled in ws-co-1.md.
- **Definitive Penrose diagrams**: `sessions/framework/Phononic-Penrose-Diagrams.md` (canonical set) [path corrected S95]
- **Collab reviews**: `sessions/session-{22,23,25,28,29,32,36,39,40,44,48,49,54,56,60}/session-*-sp-collab.md`
- **Mechanism Chain (37 closures post-S48)**: I-1, RPA(chi=20.43), Turing(W=1.9-3.2x), Wall(rho=14.02), BCS(M_max=[1.351,1.674])
- **Knowledge MCP**: query first for closures + canonical constants (S87+ discipline)
