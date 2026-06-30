---
name: S75 Transit-Landau Workshop Result
description: Workshop resolves CW vs isocurvature n_s ambiguity — same mechanism at different Landau hierarchy levels. Route 2 is physical; CW is mean-field shadow.
type: project
---

## S75 Transit-Landau Workshop: n_s Route Resolution

**Core result**: CW (Route 1, n_s=0.9595) and isocurvature transfer (Route 2, n_s=0.9649) are the SAME mechanism at different levels of the Landau classification:
- CW = mean-field (free energy curvature, level 3)
- Isocurvature = kinetic equation (quasiparticle relaxation, level 5)
- Observable n_s lives at level 5 (Route 2), not level 3 (Route 1)

**Why:** Laboratory BCS quench data is unambiguous: sweep rate sets amplitude, post-sweep multi-band relaxation sets spectral tilt. The CW formula double-counts the background shape that the Bogoliubov modes already propagate through. Tilts do NOT add.

**How to apply:** The framework's n_s prediction is 0.9649 (isocurvature, Planck central), pending mu_eff derivation. CW n_s = 0.9595 is a diagnostic, not a prediction. Never report them as competing alternatives.

## Key Technical Findings

1. **Temporal ordering established**: Phase 1 (transit, n_s=1, A_s^fiber=6.22) → Phase 2 (post-transit, n_s=0.9649 via isocurvature) → Phase 3 (KK projection, A_s=1.585e-9)

2. **d_eff dual structure**: Background modulus: d_eff=0, Gi~1 (mean-field OK for H(tau)). Perturbation field: d_eff=3, Gi~10^5 (CW unreliable for n_s).

3. **mu_eff gap**: Susceptibility matrix gives mu_slow~0.03-0.2 M_KK (3-20x above target 0.0102). Collective corrections from sqrt(N_pair)~7.7 help. Richardson exact-pairing at N_pair=59.8 is rate-limiting.

4. **alpha_s hierarchy**: Bogoliubov (0, exact) < isocurvature (-0.014, 1.46σ) < CW (-0.019, 2.13σ). Tracks mean-field dependence.

## Carry-Forward Computations
- MU-EFF-RICHARDSON-76 [CRITICAL]: Richardson exact-pairing at N_pair=59.8
- ALPHA-S-FIRST-PRINCIPLES-76: alpha_s from spectral-action-derived H(tau)
- TAU-DS-FROM-SPECTRAL-ACTION-76: Finer tau sampling for plateau duration
