---
name: S83 W1-G1 IC-SCHEME-DERIVATION
description: First decisive uniqueness adjudication of the substrate IC regulator at tau_fold on L_max=5; Zubarev selected, Branch-B triggered.
type: project
---

# S83 W1-G1 — IC-SCHEME-DERIVATION (2026-04-18)

## Verdict

`S83-IC-SCHEME-DERIVATION: PASS -- value=Zubarev scheme=Zubarev convention=substrate-native L_max=5 sha256=227a591307f88d2cfdb1c505c6ab4a040f873db4656116c5948ae7ba3c96dcdd`

## Key numbers (re-usable in future sessions)

At tau = tau_fold = 0.19 on the p+q<=L_max=5 sector filter, sum(dim·n) = 159,936 multiplicity-weighted modes:

| Regulator | S_R | Tr_omega at s=d/2=3 | chi (KK-sign) | curv d^2S/d(log Lambda)^2 | PASS? |
|:---|:---|:---|:---|:---|:---|
| zeta    | 1.599360e+05 | 3.743069e+03 | +1 | 0.000000e+00 | FAIL (not local min) |
| Zubarev | 3.805668e+03 | 4.058265e+02 | +1 | +1.155646e+05 | **PASS** |
| SDW     | 3.049747e+05 | 5.734793e+03 | -1 | +3.148456e+05 | FAIL (KK-sign) |

Ratio S_SDW/S_Zubarev = 80.1 (1.9 OOM). Echoes S82 W-1 §EN3 H̃_B ratio 181 (2.26 OOM).

## Why **Why:**

The gate tests whether the substrate can DERIVE its IC regulator rather than inherit convention. The three Connes-axiom tests (Dixmier cyclicity, resolvent compactness, KK-sign) are dispatched in parallel with a scale-curvature local-min discriminator. Zeta is scale-invariant by construction (zeta_{D_K}(0) = counting function, no Lambda dependence) so curv = 0 exactly — not a numerical accident but a structural property. SDW's alpha·sqrt(x)+beta·exp(-x) weight pushes S_SDW near the 2·N_modes boundary where cos(pi·S/2N) flips sign, failing the KO-dim=6 classification. Zubarev sits cleanly in both regimes.

## How to apply **How to apply:**

- Under Branch-B (Zubarev canonical), the UNIFIED-AS-79 three-factor decomposition `A_s = A_s_bare · F_amp · c_sub^{-1} · f_conv · S_IC` must be re-computed with Zubarev weights throughout; do NOT mix regulators across terms.
- Any future A_s ledger reconciliation must START from Zubarev IC, not zeta.
- S82 W1-2 Branch-A PASS-F2 (A_s=3.2994e-9, Δ_OOM=+0.196) is no longer the preferred reading — Branch-B deepens FAIL by -0.17 OOM per S82 W-1 §G1 3-branch map.

## Rate-limiting follow-ons

- Sector-count drift: L_max=5 sum(dim·n) = 159,936, but S77 claimed 155,984. 2.5% drift, not load-bearing for G1 verdict but warrants a sector-count convention audit.
- KK-sign normalization uses `S_R / (2·N_modes_mult)` as the normalization into (0,1); first-principles CE6-normalized version could alter SDW chi. Follow-on for W1-G2.
- SDW weight uses S72 f* parameterization (alpha_star=0.9117, beta_star=0.0883); sensitivity sweep over Chebyshev degree would strengthen uniqueness.

## Files

- Script: `computations/s83_w1_g1_ic_scheme_derivation.py`
- Data: `computations/s83_w1_g1_ic_scheme_derivation.npz`
- Plot: `computations/s83_w1_g1_ic_scheme_derivation.png`
- Working paper: `sessions/archive/session-83/session-83-results-workingpaper.md` §W1-G1
- Verdict: `computations/s83_gate_verdicts.txt` line 10

## Context provenance

- S82 W-1 workshop (`sessions/archive/session-82/workshops/s82-w1-1-divergence-chase.md`) §EN3 and §G1 — established the 3-branch CC tree.
- S82 W1-2 (`computations/s82_w1_2_unified_as_79_full.py`) — Branch-A PASS-F2 verdict conditional on zeta canonical.
- S80 UNIFIED-AS-79 canonical infrastructure.
