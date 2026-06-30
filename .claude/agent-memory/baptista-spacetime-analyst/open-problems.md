---
name: Open Problems and Active Tensions
description: Unresolved tensions, open channels, and highest-priority uncomputed items in the KK geometry program.
type: project
---

# Open Problems and Active Tensions

## #1 alpha_s Tension (STRUCTURAL)

alpha_s = 0.022 at M_Z (5.4x below observed 0.118). Persists across all BCS corrections. [S69, S70]

- alpha_s and m_H ANTI-CORRELATED in f_0: no joint window. [S70 F0-ALPHA-S]
- CCM matching lambda=(4/3)*g3^2*(a4/a2) couples both through single DOF g3^2(M_KK). [S70]
- Resolution routes: different lambda formula, modified S_inf, off-Jensen a4/a2 ratio, non-perturbative corrections, Josephson virtual excitation (S72 Workshop).

## #2 Weinberg Angle Running

- sin^2(M_KK) = 0.5839 (scheme-independent, 3 methods at machine precision). [S72, S75]
- Pure SM running gives sin^2(M_Z)=0.357 (54.5% off). [S72]
- Universal thresholds give -0.046 (120% off). [S73a]
- Threshold ratios T_2/T_3=1, T_Y/T_3=4/3 exact. delta_1/delta_3=20/9. [S73a]
- L/R asymmetry (Paper 13 eq 3.41): CLOSED as escape route. Sets boundary at M_KK, does not fix running. [S75]
- Partial Casimir universality: C_u1/C_su2 = 1/3 exact (all reps, std=5.8e-17). [S75]
- ACCIDENTAL: 3*L2^3/(3*L2^3+L1^3) = 0.2348 (1.55% from PDG). "Cubic" formula, no derivation. [S75, S76 W2-G]
- S76 W2-G: Power-law family sin^2(n) = 3/(3+e^{4n*tau}). n=1 is Baptista. n=3.026 matches PDG. n=3 overshoots RG by factor 2.5/1.6.
- Jensen metric eigenvalues at fold: L_1=e^{2tau}=1.4623, L_2=e^{-2tau}=0.6839, L_3=e^{tau}=1.2092. [S76 W2-G]
- S77: L-R direct threshold correction (Paper 13 eq 3.41, delta*L_a) gives sin^2=-0.308. WORSE than PW-resolved (-0.046). Sign problem CONFIRMED: U(1) heavy (L_1>1) amplifies delta_1. Tree-level L-R threshold route CLOSED.
- S77: Parametric scan: PDG match requires p=-2.15 in delta_Y~L_1^p. No geometric mechanism for p<0.
- Open channels: alt-Y embedding, Pati-Salam, non-pert thresh, f_0 normalization (spectral function).

## #3 Metric Positivity (Heterotic LR)

- Paper 13 tree-level three-coupling fit at M_Z forces lambda_3 < 0. Scheme-independent. [S74 HETEROTIC-LR]
- Connection-layer vs spectral-layer failures are independent (Dynkin ratio vs metric positivity).

## #4 CC Problem

- a_0/a_2 = 6/R for ALL left-invariant metrics. CC landscape CLOSED in left-invariant geometry. [S65]
- CC escape REQUIRES breaking left-invariance or Volovik relaxation mechanism.
- Volovik CC relaxation PASS (0.01 OOM), functional-independent. [S66]
- HP4: rho_HP4 = chi_2 * H_0^2 * M_Pl^2 = 9.09e-48 GeV^4, 0.47 OOM from obs. Zero free params. [S76 W1-D]
- JLO/CM correction CLOSED: CM_factor = 1 exactly for finite spectral triples. [S76 W3-C]
- Factor-3 residual = Friedmann normalization (classical FRW), NOT index theory.
- Dictionary question: chi_2 = Omega_L directly gives 0.034 OOM (8.2% overshoot). [S76 W3-C]

## #5 Moduli Stabilization (50+ closures)

- V_eff(tau) monotonically increasing for all tau>0, all schemes, all Lambda. [S75 W1-G]
- Multi-instanton condensate: V_multi/V_bare < 7e-4 at all L_max up to 10. CLOSED. [S75 W1-F]
- Non-dilute instanton liquid: V_eff monotonic; |V_liquid/V_bare| bounded by N_BCS/N_total ~ 8/6440 ~ 10^{-3}. CLOSED PERMANENTLY. [S76 W3-D]
- Cross-spectral-moment: Both a_2 and a_4 increase with tau (d ln a_4/d ln a_2 ~ 1.97). No restoring force. [S75 W1-G]
- GGE backreaction: 90x collective inertia enhancement, tau_turn=0.226 (below 0.45-0.70 target). [S75 W1-H]
- Jensen line = attractor RIDGE (S69, S76): 35/35 off-Jensen Hessian evals negative [-148.69, -17.35]. All transverse modes massive. [S76 W2-J]
- Modulus decay: tau_decay = 1.63e-37 s, gravity-dominated (99.2%). T_RH = 1.70e15 GeV. No cosmological moduli problem. [S76 W1-B, W2-E, W2-H]
- Lambda_eff = 37*M_Pl: sqrt(Z_fold) = 273 suppresses spectral-action vertex; SM channel = 0.8% of total. [S76 W2-E]

## #6 A_s Conversion/Spectral M_Pl Tension

- f_conv = (M_KK/M_Pl)^4 x (a_2/a_0)^2 = 2.547e-10 analytically derived. PROMOTABLE TO PERMANENT. [S76 W1-F]
- Deeper identity: f_conv = pi^4/(9216*a_0^2). a_2 cancels completely. Depends on mode count alone. [S76 W2-A]
- f_conv NOT R-protected in isolation (5 OOM span L=3..9, scales as L^{-10.5}). Physical at L=3 truncation. [S76 W2-A]
- f_conv^{(4)} = 6.030e-11 (gauge channel). Family monotone in n. a_4 carries 23.67% of a_2 weight. [S76 W2-B]
- BCS immune: delta_a_2/a_2 = -0.16%, wrong sign. 0.12 OOM gap not from a_2. [S76 W2-D]
- H_Friedmann = 0.975 M_KK (601x below transit H). A_s gap: 5.75 OOM (was 9.47). [S76 W1-E]
- f_conv applies to PERTURBATIONS only (Level 1), not background Friedmann (Level 0). [S76 W3-B]

## Key Observational Status

| Observable | Value | Comparison | Status |
|-----------|-------|-----------|--------|
| m_H | 127.5 GeV (BCS) | 125.1 obs (1.9%) | PASS |
| A_s | 1.58e-9 (f_conv) | 2.1e-9 Planck (75%) | PASS (0.12 OOM) |
| n_s | 0.9649 (non-PL H) | 0.9649 Planck | PASS (W1-I) |
| n_s | 0.9595 (CW route) | 0.9649 Planck (1.28 sigma) | CONDITIONAL |
| N_eff | 3.044 (post-therm) | 3.044 SM | PASS (exact) |
| alpha_s(M_Z) | 0.022 | 0.118 obs (5.4x) | **FAIL** |
| sin^2(M_Z) | 0.357 (SM run) | 0.231 obs (54.5%) | **FAIL** |
| sin^2 cubic | 0.2348 | 0.231 PDG (1.6%) | ACCIDENTAL (no deriv) |
| w_0 | -0.918 (Noether) | DESI [-0.94,-0.88] | PREDICTION (falsifier band) |

## Active Workshop Insights (S71-S75)

- **Scheme hierarchy**: Level 1 (scheme-indep) / Level 2 (needs f) / Level 3 (scheme-dep). alpha_s is Level 3. [S71]
- **Six-layer (0,0)-protection**: Registered as permanent #48. 7 independence witnesses, 23 observables. [S73B, S75]
- **w_0 = -0.918**: Noether chain prediction. DR3 falsifier band [-0.94, -0.88]. Zero tuned parameters. [S73B]
- **R_protected_fold = 1.1287**: Pure curvature invariant. Vol(K) cancels. [S73B]
- **Two-layer architecture CONVERGED**: BCS fraction ~ 1/L^9 -> 0. Ordered Veil PERMANENT. [S72]
- **BDI topological invariance all-tau**: sgn(Pf)=-1 at 10 tau values in [0, 0.19]. Gap open throughout. [S75]
- **BDSPT J-invariance all-tau**: |Z_J/Z-1|<5.82e-11 at 5 tau values. Structural, not fold-specific. [S75]
- **Kosmann landscape**: K_7 permanent 8D kernel; joint C^2=0 (universal weak); step at tau=0. [S75]
- **Atlas 48/70 ROBUST**: Structural floor grows 121->169 entries (82.4%). [S75]
- **n*=60 permanent**: L_max=7 verified. Topological invariant of Higgs line bundle. [S75]
- **Anomaly f* incompatible**: finite vs divergent moments, red vs blue n_s. Permanent. [S75]
- **Spectral-moment decoupling certified**: a_0, a_2, a_4 algebraically independent (Wronskian). [S75]

## Unresolved Computations (S76 carry-forward)

- **BOGOLIUBOV-A_s-FRIEDMANN**: Recompute A_s with H_Friedmann=0.975 in mode equation. 5.75 OOM gap. HIGHEST PRIORITY.
- **CUBIC-WEINBERG-DERIVATION**: Does orbit volume (det g_K)^{1/2} in Paper 13 eq 5.21 produce n=3? Still no derivation.
- **POWER-LAW-p-FROM-SPECTRAL**: Derive H(tau) power-law index p=1.69 from Friedmann + SA system. Fixes 134% alpha_s model spread.
- **MU-EFF-B2-MEDIATED**: Recompute mu_eff with J_u1^{eff}=0.539 (14.2x B2-mediated enhancement). May close 1.58-decade deficit.
- **INTER-SECTOR-YUKAWA**: Inter-PW-sector coupling for PMNS matrix. W3-F establishes mixing ratio > 1 within sectors.
- **CC-DICTIONARY**: chi_2 = Omega_L gives 0.034 OOM vs chi_2 = rho_L/HP4 gives 0.47 OOM. Which mapping?
- **f_conv PERMANENCE**: Formal certification; L_max=3 as unique physical cutoff.
- **DOMAIN-WALL-GW**: S65 prediction Omega_GW~10^{-10} separate from modulus channel (S76 W3-J).
- Trap 5 analytic proof (c''=0 for real reps). Numerically machine-precision.
- Paper 18 tilde{Phi} computation (PMNS from spinor overlap).
