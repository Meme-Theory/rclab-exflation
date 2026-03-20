---
name: kz-ns-45-result
description: S45 KZ-NS-45 FAIL (370 sigma). Bogoliubov n_s = -0.588 from 992-mode sudden quench. Landau d=3 KZ confirmed. Last n_s route closed.
type: project
---

S45 KZ-NS-45 FAIL: Bogoliubov particle creation spectrum gives n_s = -0.588, 370 sigma from Planck 0.9649.

Key numbers:
- n_s = -0.588 (primary, degeneracy-weighted)
- n_s - 1 = -1.588 = -5.554 (beta2 slope) + 3.966 (degeneracy slope)
- |beta_k|^2 ~ k^{-5.55} (BCS physics: high-E modes barely perturbed)
- d^2 ~ k^{+3.97} (Weyl's law for SU(3) representations)
- alpha_s = -19.88 (2967 sigma from Planck)
- k-proxy ambiguity: n_s ranges [-0.59, +5.69] depending on choice
- Landau d=3 KZ formula: n_s = -0.68 (agrees with Bogoliubov to 16%)

**Why:** Structural. High-energy KK modes experience small fractional energy change during quench (E >> Delta_0), so |beta_k|^2 ~ (Delta_0/omega)^4 drops steeply. Degeneracy grows as Weyl's law d^2 ~ omega^4. Net slope is -1.6.

**How to apply:** The Bogoliubov route to n_s from discrete KK tower quench is permanently closed. Combined with epsilon_H invariance (S44 W4-3) and Lifshitz eta closure (S44 W1-3), ALL three n_s routes are now closed. Any future n_s mechanism must invoke entirely different physics or demonstrate unique KK-to-4D scale mapping.

Sensitivity: Robust against Delta_0 (0x-2x), tau_fold (0.10-0.19), quench profile. NOT robust against k-proxy choice (fundamental ambiguity).

Files: s45_kz_ns.py, s45_kz_ns.npz, s45_kz_ns.png
