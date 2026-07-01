---
name: S74 All Results
description: S74 session results -- 6 computations, 2 PASS, 4 FAIL (47th-49th closures), sin^2 Jensen-blind, instanton sector irrelevant, PW sums divergent
type: project
---

## S74 Gate Results

### PASS
- **QCD-OPENING-74**: Instanton-dressed alpha_s at M_KK in Region II. (S_inst/2pi)*exp(-S_inst)=6.28e-4, |Da/a|=1.3e-5 (~7500x below PASS). Whole instanton sector irrelevant to alpha_s at M_KK. Region II scan to tau=1.0: max shift 6.2e-4.

### FAIL (closures)
- **JENSEN-THRESHOLD-74 (47th)**: sin^2=-1.17 unphysical. T_1_GUT/T_3=7.2 permanent structural ratio across ALL 52 PW sectors. sin^2 is Jensen-BLIND at per-sector resolution. S72 Model A 0.229 = false coincidence from wrong 1:1:1 ansatz.
- **MODULAR-SIN2-74 (48th)**: Modular flow preserves 7.2:1:1 ratio to 2.3e-15 at per-component/per-gradient resolution. Per-component escape CLOSED. Only rep-theory rescue remains (different algebra or U(1)_Y generator).
- **N17-FRAMEWORK-RESCALE-74 (49th)**: Max drift L=7->9 = 72.29% (CC ratio). PW zeta sums divergent (a_0: 6440->538560->1.94e6). S_PW sign-flips +1.64 -> -5.10. log10(CC) stable 0.47%. Gilkey vs PW route must be distinguished. Absolute sums are L_max-specific; ratios at fixed L_max remain stable.

### FAIL (sub-threshold)
- **TH-OOFT-VERTEX-MODULUS-74**: Vertex 2.55e-12 of bare at tau=0.48, 7 OOM below W1-B instanton. Vertex only reaches 1% at tau>=1.53 past runaway. CLOSED.
- **L-MAX-ZETA-REGULARIZATION-74**: Route A power sums diverge at integer s. Drift 19.4% L3->L7. R_i non-protected up SDW ladder. Heat kernel small-t inapplicable to truncated spectra. Shanks fails on divergent sequences. Cutoff function is load-bearing.

## Permanent Structural Theorems (S74)

1. **Per-sector Dynkin-index ratio**: T_1_GUT(p,q)/T_3(p,q) = 7.200, T_2/T_3 = 1.000 identically for ALL (p,q). Embedding identity.
2. **Jensen-blindness of sin^2(theta_W)**: Under ANY spectral functional, ANY cutoff, ANY tau, ANY decoupling recipe. Extended to per-gradient resolution (2.3e-15). Only rep-theory modifications can break this.
3. **PW zeta sums diverge**: On d=8 manifold, growth polynomial (~L^5 for a_0). Not truncation error but structural divergence at zeta poles.
4. **'t Hooft vertex irrelevant**: Vertex/bare < 1% requires tau >= 1.53 (past runaway). Strictly weaker than instanton channel.

## Carry-forwards
- PS-W3-I: Repeat modular sin^2 on Pati-Salam algebra
- ALGEBRA-ALTERNATIVE-SIN2: Classify NCG algebras giving sin^2 in [0.22, 0.24]
- Y-EMBEDDING-CLASSIFY: Enumerate alternatives to Y=diag(-2,+1,+1)
