---
name: S82 W2-4 PS-SUBSTRATE-MATCHED-IC result
description: GGE-Wightman substrate IC closes S79 P2-B axiomatic IC gap; K_sub=2.04, A_s=6.72e-9 PASS-F3 vs W1-2
type: project
---

**Gate**: S82-PS-SUBSTRATE-MATCHED-IC
**Verdict**: PASS (PRIMARY R3, S43 band-multiplicity 3/3/2)

**Closure (substitution chain, pre-asserted direction)**:
- W_GGE(k) = n_k + 1/2, S_IC = 1 + 2n_k = coth(omega_k/2T_k) for thermal GGE
- n_k >= 0 (physical) => S_IC >= 1 => K_substrate >= 1
- Substrate IC CANNOT SUPPRESS A_s relative to BD; structural bound
- Ratio to W1-2 is pre-bounded at 1, above; FAIL vs PASS = magnitude only

**Numerics (per-band, M_KK units)**:
- B2 (flat): T=0.668, Delta=0.770, x=1.153, n=0.461, S_IC=1.922
- B1 (acoustic): T=0.435, Delta=0.464, x=1.067, n=0.524, S_IC=2.049
- B3 (softest): T=0.178, Delta=0.176, x=0.989, n=0.592, S_IC=2.185

**5 readings**:
- R1 B3-only: K=2.185 PASS
- R2 geo-mean: K=2.049 PASS
- R3 weighted 3/3/2 (PRIMARY): K=2.035 PASS
- R4 naive 59.8/8: K=15.95 FAIL (legacy/artifact)
- R5 B2-only: K=1.922 PASS

**4/5 readings PASS at factor-3**. A_s^substrate = K * W1-2 = 6.72e-9 (R3), within factor 3.2 of Planck 2.1e-9.

**Structural significance**:
- First closure of S79 P2-B axiomatic IC gap
- Substrate-GGE IC is the UNIQUE admissible IC after P2-B closed 5 horizon-exit principles
- Volovik 3He-B correspondence (paper 25 §V + paper 26 §4) = direct physical realization
- No free parameters: T_k, Delta_k, multiplicities all from S43 gge-temp-43 data
- STRUCTURAL bound K >= 1 from n_k >= 0 (positivity); CC verified machine-eps

**Cross-checks (all pass)**:
- CC1: S_IC >= 1 per band structural
- CC2: 1+2n = coth(x/2) to <1e-12 per band
- CC3, CC4: averages within band min/max
- CC5: all K positive

**Connection to other agents' results**:
- Uses W1-2 TD-branch A_s = 3.299e-9 as baseline (transit-dynamics-theorist)
- Uses S43 gge-temp-43 per-band T_k, multiplicities (landau-condensed-matter-theorist + self)
- Uses canonical_constants Delta_0_GL, Delta_0_OES, Delta_B3, T_GGE_B2 (spectral-geometer)
- Closes IC gap identified in S79 P2-B (mack-cosmic-bridge + transit)
- S61 GGE-THERM-61 Thouless >> transit (factor 2625x) justifies GGE occupation preservation

**4-tuple**: `(value=2.0353, scheme=GGE-WIGHTMAN, convention=3HE-B-CORRESPONDENCE, L_max=GGE-BAND-MULT-3/3/2)`
**Closure SHA**: `66b77b8863d8a4d6b86bdf038ccde9bf5780b5633143db5c34254cdbbbf5429f`

**Files**: `computations/s82_w2_4_ps_substrate_matched_ic.{py,npz,png}`, WP §V.D
