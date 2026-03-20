---
name: qtheory-sc-46-result
description: S46 Q-THEORY-SELFCONSISTENT-46 INFO. E_cond-constrained SC gap gives no crossing (eps(0)<0). B3 gap 2.1x smaller than FLATBAND (0.084 vs 0.176). FLATBAND tau*=0.210 confirmed with 20pt grid. Crossing existence hinges on Delta_B3 > 0.13. V_B3B3 direct computation is open channel.
type: project
---

## Q-THEORY-SELFCONSISTENT-46 Result (Session 46 W1-1)

### Gate: INFO (2026-03-15)

E_cond-constrained self-consistent BCS gap equation does NOT produce a Gibbs-Duhem crossing in [0.17, 0.21]. The self-consistent Delta_B3 = 0.084 (vs 0.176 FLATBAND) shifts eps(tau_min) negative, eliminating the crossing. FLATBAND constant-gap tau* = 0.210 confirmed with 20-point tau grid (vs 7 in S45).

### Key Numbers
- alpha* = 0.4347 (V_HF rescale to match E_cond = -0.137)
- SC gap at fold: [0.372, 0.732, 0.084] M_KK
- FLATBAND gap: [0.385, 0.770, 0.176] M_KK
- B1, B2 match FLATBAND to 3-5%. B3 is 2.1x smaller.
- TL_SC(fold) = +0.530 vs TL_FB(fold) = +0.798 (34% lower)
- eps(tau_min) = -0.024 (SC, NEGATIVE) vs +0.361 (FB, positive)
- E_cond sensitivity: crossing at factor 1.26 (tau* = 0.250)
- V_B3B3 = 0.008 (estimated from V_B2B3^2/V_B2B2)
- V_B2B2 = 0.589, V_B2B1 = 0.299, V_B2B3 = 0.068 (direct)
- B2 van Hove at tau = 0.19016 (0.08% from fold)
- 20/23 tau points resolved in singlet

### T3-T5 Diagnostic
- NO eigenvalue crossing in (0,0) singlet sector
- Degeneracy (2, 8, 6) preserved at all tau
- Delta(tau) smooth (no slope discontinuity)
- Q-THEORY-T3T5-46: FAIL

### Structural Finding
The q-theory crossing exists IFF Delta_B3 > ~0.13 M_KK. The self-consistent gap equation with E_cond constraint gives 0.084 (below threshold). The FLATBAND value 0.176 (above threshold) produces S45 PASS. The entire q-theory CC result hinges on the B3 sector gap.

### S45 FLATBAND Confirmation
- S45 (7pt): tau* = 0.2094
- S46 (20pt): tau* = 0.2101
- Agreement to 0.0007 (0.3%). FLATBAND result is robust against grid refinement.

### Open Channels
1. V_B3B3 direct computation (currently estimated at 0.008, need > 0.015 for crossing)
2. E_cond from multi-sector ED with different B3 count
3. Tau-dependent V(tau) from spectral geometry

**Why:** The most important computation in the framework -- whether the q-theory equilibrium (Volovik Paper 05) locks onto the fold. The answer is conditional on a single quantity: the B3 inter-sector pairing interaction.

**How to apply:** Future CC computations must use the E_cond-constrained coupling (alpha = 0.435), not the raw Hauser-Feshbach V matrix. The FLATBAND result (tau* = 0.210) remains the best available estimate pending V_B3B3 determination, but it is not self-consistent.

Files: s46_qtheory_selfconsistent.py, s46_qtheory_selfconsistent.npz, s46_qtheory_selfconsistent.png
