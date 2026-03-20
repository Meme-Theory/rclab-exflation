---
name: session-49-hfb-backreaction-detail
description: S49 HFB-BACKREACTION-49 PASS - three-channel backreaction decomposition, V state-independent by Peter-Weyl
type: project
---

## S49 HFB-BACKREACTION-49: PASS

### Three Backreaction Channels

**Channel A (BdG spectral shift)**: 0% additional backreaction.
- V_{kk'} depends on Peter-Weyl mode functions (SU(3) rep theory), NOT on BCS state
- V is state-independent -> BCS gap equation is ALREADY self-consistent
- The BdG eigenvalue shift E_k^2 - lambda_k^2 = Delta_k^2 is large (~97%) but INTERNAL to BCS
- No additional iteration needed; this IS the gap equation

**Channel B (ph rearrangement)**: 1.2% primary (g_ph=0.03), 3.9% conservative (g_ph=0.10).
- BCS smearing delta_n ~ 0.26 feeds back into HF self-energy
- V^{ph} != V^{pp}: pairing force is ~10% of full ph interaction (nuclear Skyrme, Paper 02)
- g_ph parametrizes V^{ph}/V^{pp} ratio, nuclear range [0.01, 0.10]
- Self-consistent loop converges in 6-8 outer iterations
- Gap shifts are NEGATIVE (repulsive mean-field pushes levels apart, weakening BCS)
- ED confirms: E_cond shifts +1.7% (g=0.03), +5.4% (g=0.10)

**Channel C (geometric)**: 5.5e-5% (ppm level, utterly negligible).
- |E_cond|/S_fold = 5.5e-7. Metric perturbation at ppm level.
- Eigenvalue shifts < 10^{-6} M_KK

### Key Numbers (g_ph=0.03, primary)
- Delta_B2: -1.14%, Delta_B1: -0.88%, Delta_B3: -1.21%
- ED E_cond: +1.72%
- M_max (Thouless): -2.6%
- Convergence: 6 outer iterations, rate -3.4/iter
- S38 estimate 3.7%: VALIDATED (actual 1.2%)

### Tau Sweep
- All 5 tau values converge at g=0.03 and g=0.10
- Backreaction SMALLER away from fold (0.05% at tau=0.19 vs 0.13% at tau=0.00)
- Van Hove singularity at fold drives worst-case backreaction

### CC Crossing
- ec_fabric SURVIVES backreaction at all physical g_ph
- ec_fabric actually INCREASES slightly with backreaction (Delta decreases, so E_inter/E_cond ratio improves)

### Self-Correction
- v1: Used V_bare as V^{ph} with alpha_ph=0 (pure Hartree). This COLLAPSED pairing because the
  Hartree shift (~48% of level spacing) overwhelms the pairing gap. This is the well-known
  nuclear pairing collapse from overly repulsive mean fields (Paper 08).
- v2: Correctly identified that V^{pp} != V^{ph}, parametrized with g_ph, and computed all 3 channels.
  The structural insight (V state-independent by Peter-Weyl) means Channel A contributes 0% additional.

### CONFIRMED Analogy Addition (S49)
- HFB self-consistency in nuclear sd-shell (Paper 02 Table I): 1-5% correction.
  Framework result: 1.2% at nuclear g_ph. Quantitative match.
- V^{pp} state-independence from representation theory has NO nuclear analog
  (nuclear V depends on density). This is a SIMPLIFICATION in the spectral action framework.
