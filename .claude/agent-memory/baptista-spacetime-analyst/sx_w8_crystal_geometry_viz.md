---
name: sx-w8-crystal-geometry-viz
description: Session-X W8 SU(3) Jensen crystal-geometry viz expansion — curvature-convention quartet, dead-import findings, 4 figure-warranted post-S47 results, D6 orphan resolution
metadata:
  type: project
---

# Session-X W8 — Phononic-crystal-geometry_viz.py expansion (S47 → S93)

Comprehensive expansion of `sessions/framework/Phononic-crystal-geometry_viz.py` (+7 PNGs + ARCHIVE source doc). 3 gates: G1 domain survey, G2 expansion+rerun (≥3 new figs), G3 archive-migration.

**Why:** the S47-era viz predates the entire post-S47 geometry program; the figures depict only the crystal/tight-binding layer.
**How to apply:** when revisiting the crystal-geometry viz or its constants, these findings are the current state-of-domain.

## Curvature-convention QUARTET (D8 — resolved, the trap)

Four DISTINCT scalar-curvature normalizations for the SAME Jensen fold; NOT mutual rescalings (ratio drifts 3.57→4.47 across τ):
1. **Script line-534 form** `R_K=-(1/4)e^{-4t}+2e^{-t}-1/4+(1/2)e^{2t}` → R_K(0)=2.000, R_K(0.19)=2.01814. **Matches archive's +2.018 / "1% above R=2.000".**
2. **S52/S53 computed** R_K(0)=4.0, R_K(fold)=4.036288 (bi-invariant max=4.0).
3. **S61 Koszul SIGNED** R_K(fold)=−2.018 M_KK² (mostly-plus convention; Lambda_eff=(1/8)R_K).
4. **KB Paper-15 eq-3.70 STRING** `(3/2)(2e^{2t}-1+8(e^{-t}-e^{-4t}))` → R_K(0)=1.5, R_K(0.19)=7.198. **Does NOT reproduce the 4.0/4.036 the same sessions cite ⇒ OCR-garbled variant (consistent with my memory: Paper-15 eq 3.65 OCR garbled — DO NOT USE).**

DECISION: keep the script's potential-shaping formula but relabel honestly as a normalized MODEL curvature; pin the SIGNED S61 form (−2.018) for any NEW curvature figure, with bi-invariant R(0) and Koszul magnitude noted. Never silently swap formulas.

## Dead imports / stale displays (G1)

- **omega_H2=1.41, omega_H3=11.465** canonical but `BRANCHES` dict hardcodes 1.456/10.37 → DEAD IMPORTS + STALE displayed band-centers (D3).
- **Delta_0_GL=0.7704** imported, never used → dead import (D5).
- **omega_L1/L2 naming collision** (D4): imported 0.138/0.192 = S52 GL Γ-gaps; archive §9 0.070/0.107 = S48 3-band Leggett — DIFFERENT observables, same symbol.
- **J_u1=0.038** script-current; archive §1/§9 0.029 is the STALE locus; true J_C2/J_u1 ≈ 24.6 not "32:1" (D2).
- 8 of 16 imports PROVENANCE-GAP (advisory; D7).

## 4 figure-warranted post-S47 results (all KB-anchored)

- **E1** §VII.AJ partition-stability `(2,4,8,6)` at τ_fold (S87 W11-2 PERMANENT); τ-asymmetry §VII.AE δ_neg=−0.0750, δ_pos=+0.175 (S88 W2-9; atlas-03 E40); Friedrich-Bär saturation at L_max=6.
- **E2** R-monotonicity dR/dτ≥0 AM-GM (S64 W1-A PROVEN, closes CC Path C); R_protected_fold=1.1286545967627695=a_0·a_4/a_2² (S73B/S74). S64 moments a_0=6440,a_2=2776.17,a_4=1350.72 give 1.12865 ✓; L_max=10 moments (155984/64308.24/29086.18) give 1.0971 (L=7 enumeration artifact — canonical is 1.1287).
- **E3** d_s(σ)=−2 dlnP/dlnσ, P(σ)=Σ dim(p,q)Σe^{−σλ²} on NORMAL-STATE Δ=0 spectrum; fold window σ_*=1.4005 M_KK⁻²; UV d_s→8 Weyl; CDT 4→2 (same-functional-different-scale rule, S92 AH-PF-1).
- **E4** R_canonical=7.324974378387362 (S89 W2 Hochschild×Chern); R_universal bridge (S86). Optional.

## D6 — archive supersession is MIS-POINTED (orphan)

`Phononic-Substrate-Geometry.md` header line 9: "subsumed here as §7.3" BUT live §7.3 (line 244) = "R-Protection as K-Pairing Class" (spectral-functional theorem, NOT crystal content). Header also says predecessor "still valid for the 32-cell Voronoi construction and tight-binding bands." ⇒ crystal geometry is ORPHANED in the migration; only N_cells=32 survives in a key-numbers table (line 521). Curvature anatomy §7 (K(u1,su2)=0, K(u1,C²)=1/16, Ric(u1)=1/4, protected chain q_7²=1/16) are live substrate-IS results with NO live home → MIGRATE-FORWARD recommendation for W2 (tesla-resonance).

## Verified-current core (PRESERVE)

32-cell Voronoi (N_cells=32, S42 GIANT-VORONOI, not superseded); 229.5 hierarchy (proven_1157, c_Gold_over_c_fabric R-PROTECTED); N_pair=1 (PERMANENT); speed bump τ=0.2015 (S53 W3-7 PROVEN; d²V_KK/dτ²=−63.2, d²E_cond/dτ²=−67.7). CHAIN1 (2,−2,1)·(1,3,4)=0 → det g_τ=1 (Sage-exact). CHAIN2 ratio=229.4794, N_e(3+1D)=2.71791, N_e(8D)=0.77654.
