---
name: S47 Coherence Response Analysis
description: S47 COHERENCE-RESPONSE-47 ARTIFACT. Character coherence function 95% truncation-determined. Three Volovik probes assessed: AD metric INSUFFICIENT, q-theory F(tau) SURVIVES, Sakharov G_N INSUFFICIENT. Proposed RHOS-TENSOR-47 (superfluid density tensor) as decisive dynamical probe.
type: project
---

S47 W3-3 COHERENCE-RESPONSE-47 returned ARTIFACT. Character coherence function C(theta;tau) on T^2 has r_C = 0.9192 +/- 0.0003 rad. 95% geometric (truncation), 5% BCS static, 0.13% BCS dynamic. Elasticity = 0.030.

**Why:** Peter-Weyl characters are tau-independent. Any weighted sum over characters is dominated by the characters when weight variation (5%) is small compared to character variation (10^2).

**My three probes assessed:**
1. AD emergent metric: INSUFFICIENT. Same condensate profile, same truncation problem. Curvature partially amplifies but not enough.
2. Q-theory F(tau): SURVIVES. Global integral, no characters. S45 tau*=0.209 (O(1) variation). Genuinely dynamical.
3. Sakharov G_N: INSUFFICIENT for coherence. 2.5% variation from topology, not truncation.

**Proposed computation: RHOS-TENSOR-47**
- 8x8 superfluid density tensor rho_s^{ab}(tau) via Peotta-Torma formula
- Response function (d^2F/dv_s^a dv_s^b), not state function
- Uses BdG eigenvectors, not characters -- immune to truncation dominance
- Expected O(1) tau-variation, strong directional anisotropy
- Gate: eigenvalue variation > 10% AND anisotropy > 5 -> PASS

**Key insight:** Character coherence = kinematic (Fourier decomposition). Superfluid density = dynamical (response function). The substrate self-coherence question requires a response function, not a spectral decomposition.

**How to apply:** Any future substrate diagnostic must be a response function or global integral, not a character expansion. The Peter-Weyl basis is the wrong probe for BCS dynamics.
