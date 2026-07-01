---
name: S68 BCS-DRESSED-MODE-68 Result
description: BCS dressing of Bogoliubov mode functions - PASS, 11.2% A_s increase, 0.046 OOM gap reduction
type: project
---

Gate: **PASS**. |delta_As/As| = 0.1117 > 0.1 threshold.

Three channels: B (eps_H, +15.5%) dominant, A (variance, -1.6%), C (sound speed, -2.2%) partially cancel.

**Why:** BCS condensate modifies spectral action tau-dependence through BdG spectrum, reducing eps_H by 7.7% (7.2% mean-field S65 + 0.5% vertex S67). Since A_s ~ 1/eps_H^2, this gives +15.5% A_s. Channels A and C oppose (mass increase reduces variance, sound speed correction), leaving net +11.2%.

**How to apply:** BCS dressing provides 0.046 OOM of the 0.80 OOM A_s gap. Not sufficient alone. Must combine with acoustic transfer function and RG propagation results. The eps_H channel is structurally dominant -- any future modification to eps_H has 2x amplification in A_s.

Key numbers: Sigma_L=0.206, Sigma_H=3.557 M_KK^2. delta_ns=+0.021 (correct sign). Sakharov fraction 29.9%. n_s(BCS)=0.723 (57.6 sigma tension remains).

a_2 decomposition: 10.8% MF + 0.8% vertex = 11.6%. a_4: 24.0% MF + 5.8% vertex = 29.8%.

Files: `computations/s68_bcs_dressed_mode.{py,npz,png}`
