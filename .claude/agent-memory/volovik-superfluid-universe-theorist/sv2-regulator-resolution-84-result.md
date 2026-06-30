---
name: S84 SV2 Regulator-Resolution xi_J/xi_E_GGE L_max stability
description: S84-W0-REGULATOR-RESOLUTION-SV2 FAIL. R_JE drifts 0.454->4.98 across L_max=5->8. Branch (iv) retracted; w_0 UNSPECIFIED pending S85.
type: project
---

# S84-W0-REGULATOR-RESOLUTION-SV2 — FAIL

**Verdict**: FAIL (max|R_JE-0.45|/0.45 = 10.08). Branch (iv) is a TB-32 / L_max=5 truncation artifact.

**Why**: The ratio R_JE = ξ_J / ξ_E_GGE is NOT L_max-stable. ξ_J is TB-pinned (32-mode Hamiltonian at τ_fold; L-independent = 0.008911). ξ_E_GGE decreases monotonically as L_max grows because the Zubarev-weighted moment S_Zub_E saturates (Gaussian λ-cutoff at ~M_KK) while the zeta-weighted moment S_ζ_E grows ~L^4 (polynomial sector multiplicity × linear energy weight).

**How to apply**: Branch (iv) is retracted as provisional canonical. w_0 canonical is UNSPECIFIED pending S85 re-audit. NO retreat to prior canonical (-0.918 or -0.998). SV3 (Δ_BCS cusp scan) and SV4 (τ off-fold scan) are ABORTED. SV5 (R_842 rectangle migration) retains its independent PASS. The S85 re-audit must re-enumerate w_0 branches at L_max=8 (or higher) where the spectral moments are asymptotically stable.

## Numerical results

| L_max | ξ_E_GGE | R_JE | drift vs L=5 | band |
|:-----:|---------:|------:|-------------:|:-----|
| 5 (anchor) | 1.965e-02 | 0.4536 | 0% | PASS |
| 6 | 8.563e-03 | 1.041 | +129.4% | OUTSIDE |
| 7 | 3.696e-03 | 2.411 | +431.6% | OUTSIDE |
| 8 | 1.788e-03 | 4.985 | +999.1% | OUTSIDE |

PASS band [0.40, 0.50]. INFO band [0.38, 0.52]. Ceiling breached already at L=6.

## Cross-checks

- CC-i (anchor reproduction): PASS (R_JE(5)=0.453589 vs 0.453524; |Δ|=6.5e-5)
- CC-ii (10% drift bound): FAIL (129.4%)
- CC-iii (Cauchy tail): weak-PASS (106.7% < 131.7% but both >100%)
- CC-iv (GPU vs CPU on ROCm): PASS (|Δ|_rel = 1.7e-16 zeta, 2.8e-16 Zubarev)
- CC-v (Mellin cone tr(|D_K|^{-3})): FAIL (differences 1.91e+04 → 3.11e+04 → 3.84e+04, not Cauchy)

## Structural takeaway for Volovik program

The Jensen-deformed SU(3) Dirac spectrum at τ_fold=0.19 does NOT Mellin-cone converge at s=3 under sector-level truncation L_max ≤ 8. This is the geometric root of the SV2 FAIL: the branch-(iv) w_0 = -0.842 identity depends on a sector undersampling that inverts the physical ordering ξ_J < ξ_E_GGE (holds at L=5) to ξ_J > ξ_E_GGE (holds at L=8). The covariance-ordering hypothesis of strict branch-(iii) (ξ_J ≃ ξ_E_GGE) is NOT re-instated — instead, L_max extension SURPASSES covariance, giving R_JE >> 1.

Physical interpretation: under the canonical Zubarev regulator f_R(λ) = exp(-λ²/M_KK²), the Josephson sector is substantially LESS suppressed than the GGE sector at high L_max. This inverts the S57/S58 assumption that GGE dominance drives w_0 → -1 asymptotically; at L=8, Zubarev pushes w_0 AWAY from -1 via enhanced Josephson pressure P_J = -ρ_J (since ξ_E_GGE multiplicatively suppresses only the GGE side).

## Artifacts

- Script: `computations/s84_w1a_w0_sv2.py`
- Data: `computations/s84_w1a_w0_sv2.npz`
- Verdict-file SHA: `e1843c278cad62bebffc2e16905eec15247f74aa8cb5870f00de231c56593ffc`
- Working paper: `sessions/archive/session-84/session-84-w1-workingpaper.md` §W1-3.SV2
