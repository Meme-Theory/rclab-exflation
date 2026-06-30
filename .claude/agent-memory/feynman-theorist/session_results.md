---
name: Session Results Archive
description: Compressed key computation results. Recent gate verdicts (S83-S84) verbatim; older sessions reduced to structural anchors only.
type: project
---

## S84 W1a-2 DYNAMICS-DRESSING (FAIL, confirmation-of-wall)

- **Verdict**: F_supp_max = 1.043783 < 1.10 threshold by 5.62e-2 absolute. Reproduces plan's expected 1.0438 to 4 sf.
- **6 dressing channels** (sum 1/X_i = 4.378e-2):
  - Ch1 NNNLO @ SU(3): 1/752 (S83 G35)
  - Ch2 1/N_gauge geometric resum: 1/44.5 **DOMINANT** (closed-form (1/3)^n/N_c^n at N_c=3)
  - Ch3 a_4+ p=2 cross-slot: 1/1400 (S83 G15)
  - Ch4 c_sub tau-shift: 1/396 (S83 G12)
  - Ch5 W2-2 saturation: 1/1.33e4 (S82 UNIFIED-BACKREACT-79)
  - Ch6 1/N_field NLO EFT envelope: 1/60 (eps_H=0.02163)
- **Add vs mult CC**: |F_mult - F_add| = 5.65e-4 < 1e-3. Faithful to ~1 part in 100.
- **All 7 cross-checks PASS** (CC-i through CC-vii). CC-vii independence load-bearing on [J,D_K]=0 CPT decomposition.
- **Structural meaning**: A_s closure problem RELOCATED from dynamics to baseline layer. Dynamics-sub-surface EXHAUSTED as A_s rescue.
- **Surviving rescue paths**: W1a-1 (0.89% log-DC H_tilde window), W1a-3 SV1-SV5 (w_0 branch-iv), W1b (substrate-native H_tilde).
- **Rule**: No future plan should propose dressing-layer rescue without overturning at least one of 6 channel ceilings via explicit re-derivation of upstream gate.
- Data: computations/s84_w1a_dynamics_dressing.{py, npz, png}. Closure SHA a2a801a7cdb4515e69d8d16d0ffe948cf02f73b493d6b0606c31da25d02e1b63.
- **Lesson (confirmation-of-wall vs failure)**: pre-registered FAIL is a CONSTRAINT, not weakness. Formal closure of rescue hypothesis, not new elimination.

## S83 W2-G9 CC7-UV-DECAY (PASS)

- n_fitted = 1.995088 (|delta| = 4.9e-3, ~40x inside PASS band 0.2). Zubarev: n_Z = 1.969649. Regulator consistency |n - n_Z| = 0.025 < 0.1.
- **3PI-NLO matching-ansatz form**: F_3PI(k) = (1/(16pi^2)) * k^2/(k^2 + 4 M_eff^2)^2, M_eff = sqrt(tau_fold) * M_KK ~ 0.436 M_KK. UV asymptote: C_0 * k^{-2}, C_0 = 1/(16 pi^2).
- **Structural identity**: 3 internal propagators * 4D loop volume = k^{-6} * k^4 = k^{-2}. Gauge-group-independent at leading 1/N.
- **PRU lesson**: naive triangle reduction gave log(k^2)/k^2 -> n_fitted = 1.65 (INFO). Berges-Serreau matching-ansatz derivative kills the log.
- **Rule for UV-exponent gates**: when hypothesis is n=integer power-law, check bare-diagram form for log-contamination from endpoint singularities of Feynman-parameter integrals before fitting. If log present, use LSZ-amputated/subtracted form (derivative of B_0^sub) to get clean power law.
- Data: s83_w2_g9_cc7_uv_decay.{py, npz, png}. Closure SHA d71193dacc7d5d12ae9e12fc487916d9129b1d5ca081f11ebcc6d2204fbd7e20.

## S80 W1-3 FOLD-INST-GRADIENT (FAIL, independent consult)

- tau_peak = 0.25 (right edge), |delta tau| = 0.06 > 0.05. Two prescriptions both FAIL, both tau_peak=0.25 (100% A/B agreement).
- **Structural reason**: Z(tau) = d^2 S_total/dtau^2 monotonically increasing across [0.05, 0.30], not peaked at fold.
- **Rule**: canonical S42 Z(tau) has no local max in tau-scan range; peak at fold must come from non-Z sources (R_K(tau), F^2) if it exists.
- 4th Fold Transit Event functional NOT provided by dS_inst/dtau. Three-functional set (dS/dtau+, v_mach>c_s, Hessian>0) remains minimal.
- Files: s80_fold_inst_gradient_feynman.{py,npz,png}.

## Earlier Session Anchors (S40-S60)

- **S40**: 27th equilibrium closure (HESS-40 22/22 transverse positive, min=1572). T_acoustic 0.7%. B2 integrable (<r>=0.401, rank-1 86%). GSL structural PASS.
- **S41-42**: S_F^Connes=0 identically (BDI). Z=74,731 (fabric stiffness). m_tau=2.062 M_KK. w_0=-1+O(10^{-29}). CDM from GGE: NFW, sigma/m=5.7e-51 cm^2/g. eta=3.4e-9 (0.7 OOM off). N_eff step 32->240 at infinitesimal tau.
- **S52**: |M|_max=0.02273 M_KK (B2[1]+B2[2]). M-matrix DIAGONAL: only elastic forward scattering. Pair scattering |M_pair|_max=0.0715. a/xi_BCS=0.002 (WEAK). u_B2=0.932, v_B2=0.361.
- **S53**: BDG-SPECTRAL-DET MONOTONE (inherits W4, wrong bridge). 7-DOF saddle: ONE local maximum at tau=0.2015 (d2V=-679), ZERO minima. |dE_cond/dV_KK|=1.30 at fold (Van Hove amplification, 40x).
- **S54**: SA-LATT-OCC PASS (5.35% barrier sharp cutoff Lambda=1.0 only). ED-SWEEP FAIL (d/Delta=42 pairing collapse, 193x shortfall). THRESHOLD CLOSED (4 OOM mismatch). Berry-Tabor integrable. Massey: 1378 crossings all xi<1e-3. Starobinsky EXCLUDED (M_scalaron 255x too high). n_s=0.501 (14x overshoot).
- **S55 EFT-RULES**: 8-mode L_eff with V_kl. G_k(omega)=1/(omega-eps_k+i eta), -iV_kl, F_k anomalous. |M|_max=0.0799 M_KK. 57 nonzero amplitudes. 3 attractive (MAC=-0.1039), 5 repulsive. d=0+1 ALL marginal. UV-COMPLETE 256 states. OPTICAL-THEOREM PASS 1.1e-15.
- **S56**: F_fabric monotone increasing (Josephson F_J=-50*E_J*m dominates). Isotropic Josephson preserves R-G integrability. CC=adiabaticity problem. W_Josephson + W_integ_Josephson walls.
- **S60**: LEPTO-CP FAIL: [J,D_K]=0 forces M_R real => epsilon_1=0 exact. **W_J_Majorana wall: universal CP shield**. M_R~M_KK too high for perturbative seesaw. Surviving escapes: twisted spectral triple, UV completion, gravitational anomaly.

## alpha_s = n_s^2 - 1 Paper

- Paper at papers/alpha-s-ns/main.tex, 13 pages, compiles clean.
- **Core derivation**: P(K)=T/(JK^2+m^2). y=m^2/(JK^2). n_s-1=-2/(1+y), y=(1+n_s)/(1-n_s). dy/d(ln K)=-2y. alpha_s = dn_s/d(ln K) = -4y/(1+y)^2 = -(1-n_s^2) = n_s^2-1.
- **Five proofs of robustness** (all within Josephson phase sector):
  1. 3-pole Leggett: poles 99.95% degenerate, delta_alpha_s=5.8e-9
  2. Running mass: gamma<1-n_s=0.035 (algebraic). Physical gamma=-6.76e-4
  3. Zero-mode protection: Goldstone n=0 KK mode, <V>=0 identically
  4. RPA suppression: delta_alpha_s=1.1e-5
  5. Goldstone theorem: K^2 dispersion structural for broken U(1)
- **Tension**: 6.1 sigma with Planck (honest).

## Data File Inventory (Active)

| File | Session | Contents |
|------|---------|----------|
| s40_*.npz (11 files) | S40 | B2 integrability, T_acoustic, GSL, CC transit, no-hair, QRPA, Page curve, Hessian off-Jensen, ATDHFB, self-consistent ODE |
| s55_eft_rules.npz | S55 | EFT Feynman rules, V_kl, amplitudes |
| s60_lepto_cp.npz | S60 | Leptogenesis CP violation |
| s80_fold_inst_gradient_feynman.npz | S80 | Z(tau) prescriptions A/B |
| s83_w2_g9_cc7_uv_decay.npz | S83 | UV exponent fit |
| s84_w1a_dynamics_dressing.npz | S84 | 6-channel dressing F_supp_max |
