---
name: S84 W1a-1 BASELINE-HTILDE-SENSITIVITY
description: PASS window for A_s closure located in H_tilde in [4.599e-3, 4.829e-3] under CC3 identity; log-measure 0.89%, all 6 cross-checks PASS, CC-iv at machine epsilon
type: project
---

# S84 W1a-1 — BASELINE-HTILDE-SENSITIVITY (PASS, 2026-04-19)

## Verdict

PASS. Log-measure of PASS-1.05 window = **0.8901%** within TD/LI divergence-chase interval `[2.46e-5, 5.91e-3]`. Linear-measure 3.9072%. Both inside the tight bands [0.80%, 1.05%] and [3.5%, 4.5%] respectively. All 6 cross-checks PASS; CC-iii and CC-iv hit machine epsilon.

4-tuple: `(value=0.8901, scheme=zeta, convention=TD, L_max=5)`.
Full closure SHA: `a47383031046171c062e822a735c7e5cd42261aad45996d9ebae9e65f6b77c19`.

## PASS window

`H_tilde in [4.599e-3, 4.829e-3]` (CC3 closed form at the 2.10e-9 Planck value with factor-1.05 envelope).

Analytically: H = H_canonical_TD * sqrt(A_s_target / A_s_canonical) with anchor (5.9076e-3, 3.30e-9).

## CC3 identity — d(ln A_s)/d(ln H_tilde) = +2

Recovered numerically to 1.835e-12 absolute (CC-iv). Structural theorem of the UNIFIED-AS-79 ledger under tau-stationary eps_H, F_conversion, M_Pl_eff at the CMB pivot (S83 G12 DRESSING-TAU-FLOW PASS slope = 1.75e-3).

## Cross-checks (all PASS)

- CC-i   log-measure% 0.8901 vs spec 0.913, |delta| 0.023 (< 0.05)
- CC-ii  linear-measure% 3.9072 vs spec 3.907, |delta| 0.0002 (< 0.02)
- CC-iii sqrt monotonicity max dev 4.44e-16 (machine epsilon)
- CC-iv  slope 1.999999999998, |delta-2| 1.835e-12 (< 1e-6)
- CC-v   Parker IC n_pairs=59.8, P_exc=1.000 (W2-4 anchor)
- CC-vi  A_s(H_LI) = 5.741e-14, spec 5.73e-14, rel dev 0.20% (< 1%)

## Interpretation for A_s closure

The S83 Wave-2 dynamics-dressing exhaustion (188+ OOM short) closed the dynamics-layer rescue corridor. S84 W1a-1 RELOCATES the A_s closure rate-limiter to substrate-baseline derivation of H_tilde. Inversion: "dynamics rescue impossible" -> "baseline derivation must hit 0.89% log-target".

Anchor gap: TD endpoint H=5.9076e-3 sits 1.57x above PASS-1.05 band centre (Δ_OOM = +0.196). To close, H_tilde must be reduced by factor 0.797 (= sqrt(2.10/3.30)).

## Rate-limiting next steps

1. S84 W1a-3 / W1b canonical baseline-H landings — do they hit [4.599e-3, 4.829e-3]?
2. H_tilde divergence chase (TD vs LI) — 267-vs-55 e-folds ambiguity is the substantive upstream uncertainty. LI endpoint A_s = 5.74e-14 (FAIL-GT15 Δ_OOM = -4.56).
3. W2-baseline DC refinement may tighten the target below 0.89% log-DC.

## Falsification meaning

If future baseline derivation lands H_tilde outside [4.599e-3, 4.829e-3], framework FAILS A_s closure. Relocation from dynamics to baseline is structurally falsifiable.

## Files

- Script: `computations/s84_w1a_baseline_htilde_sensitivity.py`
- Data:   `computations/s84_w1a_baseline_htilde_sensitivity.npz`
- Plot:   `computations/s84_w1a_baseline_htilde_sensitivity.png`
- Verdict: `computations/s84_gate_verdicts.txt` line 6
- Working paper §W1-1: `sessions/archive/session-84/session-84-w1-workingpaper.md`
