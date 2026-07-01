---
name: w0-regulator-sv1-84-result
description: S84 W1-3.SV1 PASS. w_0=-0.842454 branch (iv) reproduced to 2.76e-7 from two-component Zubarev-dressed closed form. All 5 CCs verify.
type: project
---

# S84-W0-REGULATOR-RESOLUTION-SV1 — branch (iv) canonical verification

**Verdict**: PASS (2026-04-19).

**Primary result**: `w_0^(iv) = -0.842454` reproduced to `|delta| = 2.76e-7` (tolerance 1e-5 RATIO).

**Closed form (branch iv)**:
```
F_Josephson^Zub  = xi_J * F_Josephson^zeta        = 0.008911 * -336.641 = -3.000 M_KK
rho_J^cell(Zub)  = |F_J^Zub| / N_cells            = 3.000 / 32          = 0.09375
rho_GGE(Zub)     = xi_E_GGE * rho_GGE^zeta        = 0.019646 * 1.709    = 0.03358
P_GGE(Zub)       = xi_E_GGE * P_GGE^zeta          = 0.019646 * -0.688   = -0.01352
w_0^(iv)         = (-rho_J + P_GGE) / (rho_J + rho_GGE) = -0.10726 / 0.12732 = -0.84245
```

**Structural content** (substrate framing):
- Branch (iv) is the two-component substrate vacuum EoS with BOTH Josephson and GGE sectors Zubarev-dressed.
- Ratio `R_JE = xi_J / xi_E_GGE = 0.4536` reflects that BCS TB spectrum (F_Josephson source) is weighted toward HIGHER eigenvalues than the L_max=5 D_K spectrum (GGE source). Same Gaussian mollifier `exp(-lam^2/M_KK^2)` suppresses F_J MORE than rho_GGE.
- **This is spectral-moment physics, not dark-energy container physics**.
- Relative to scheme (i) zeta+zeta (-0.9165) and scheme (ii) zeta-J + Zub-GGE (-0.998), branch (iv) LIFTS w_0 toward 0 because F_J is suppressed by factor 112 (10.52 -> 0.0937) while GGE only by 51.

**Why Md1 blocks branch (i) + strict-(iii)**:
- Branch (i) full-regulator-average requires `xi_J -> 1` asymptotically. Computed `xi_J = 0.008911` — bounded away by factor 112. Md1 deficit `|1 - xi_J| = 0.991`.
- Strict-(iii) requires `lambda = xi_J / xi_E_GGE = 1` (exact covariance). Computed `lambda = 0.4536`. Covariance error `|1 - lambda| = 0.546`.

**Cross-checks (all PASS)**:
- CC-i: Md1 deficit 0.991 > 0.5 threshold -> branch (i) closed.
- CC-ii: lambda=0.4536 != 1 -> strict-(iii) closed.
- CC-iii: Branch (ii) reproduced w_0 = -0.998 to 9.9e-5.
- CC-iv: Linear response under 1e-8 perturbations, amplifications 0.13-0.26 (all O(1)).
- CC-v: sgn(F_J) = -1, w_0 < 0 NEC-consistent.

**Anchor provenance**:
- `xi_J = 0.008911` -- W0-workshop / s83_sagan_rho_j_audit.py
- `xi_E_GGE = 0.019646` -- S83 W3-G51 energy-weighted Zubarev
- `F_Josephson^zeta = -336.641 M_KK` -- S58 canonical
- `rho_GGE^zeta = 1.709, P_GGE^zeta = -0.688` -- S57 cc_sign
- Delta_BCS, tau_fold, N_cells from canonical_constants.py

**Artifacts**:
- Script: `computations/s84_w1a_w0_sv1.py`
- Data: `computations/s84_w1a_w0_sv1.npz`
- Verdict SHA-256: `6c0063d22c520da95f1926574ba3a7139a1ddfb70d0d3e8dac8d11c121e608b2`

**Next steps in S84**: SV2 (L_max in {6,7,8} stability of R_JE), SV3 (Delta_BCS bracket), SV4 (tau off-fold), SV5 (R_842 migration — already PASS). Joint PASS of SV1-SV4 adopts (iv) as S84 canonical.

**Volovik-frame significance**: Branch (iv) is the substrate analog of partial regulator-covariance in a two-fluid superfluid: the Josephson condensate (heavier-mode-dominated) and the GGE excitation pool (lighter-mode-dominated) respond differently to the same UV cutoff. This partial covariance is a GENERIC feature of any two-fluid spectral system with different effective UV distributions; NOT an artifact of TB-32 truncation.
