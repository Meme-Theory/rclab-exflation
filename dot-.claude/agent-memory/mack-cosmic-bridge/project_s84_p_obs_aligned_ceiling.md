---
name: S84 W4-49 P-OBS-ALIGNED-CEILING (DAG pre-registration)
description: S84 W4-49 pre-registers the 7/9 → 8/9 → 9/9 ceiling-lifting DAG with 4 trigger gates (A1 DERIV-I∧DERIV-II, A2 TAU-CROSS-SCALE, B1 N1 TRANSFER-FUNCTION-74, B2 ALPHA-S-CMB-S4-PROJECTION-REFINEMENT); frozen 2026-04-18; monotone DAG verified
type: project
---

# S84 W4-49 — P-OBS-ALIGNED-CEILING Registration

**Gate**: `S84-P-OBS-ALIGNED-CEILING` PASS 2026-04-18
**Classification**: NON-PHONONIC (registry/bookkeeping)
**content_sha256**: `0f8cb99b1f7a90d04a2b0957832c3e8bdd47ef2b634ff306cbd9184c2930f54e`
**audit_sha256**: `09e7d4ebd0558484b522f4aed7520c8e01457a846076c79ed2f5ca3a22499691`

## Baseline (S83 W3-G48 PASS)
- P_obs_aligned = 7/9 = 0.7778
- PASS: {n_s, r, m_H, N_eff, w_0, f_NL, A_s}
- FAIL: {sin²θ_W, α_s}
- INFO: ∅

## DAG Structure
- **7/9 → 8/9** (sin²θ_W): (A1 ≡ DERIV-I ∧ DERIV-II) ∨ (A2 ≡ TAU-CROSS-SCALE)
- **8/9 → 9/9** (α_s): (B1 ≡ N1 TRANSFER-FUNCTION-74) ∨ (B2 ≡ ALPHA-S-CMB-S4-PROJECTION-REFINEMENT)
- Min path = 2 PASS (one disjunct each); upper bound = 4 dependency edges
- Verified: 16/16 subsets yield numerator ∈ {7, 8, 9} (monotone)

## Evidence-Column Separation (critical bookkeeping distinction)
P_obs_aligned and W4-48 ZFP rigor registry are **distinct ladders**:
- **A1 ∧ B1**: +2 ZFP rows (sin²θ_W + α_s both zero-free-parameter)
- **A1 ∧ B2**: +1 ZFP (sin²θ_W only); α_s = DETECTOR-ACTIVE
- **A2 ∧ B1**: +1 ZFP (α_s only); sin²θ_W = SCHEME-DEPENDENT
- **A2 ∧ B2**: **0 ZFP rows** — bookkeeping hits 9/9 but rigor unchanged

The minimum-path A2∧B2 reaches 9/9 bookkeeping with zero ZFP additions. This keeps the framework honest: P_obs_aligned=9/9 is necessary-but-not-sufficient for a maximally-strong claim.

## Sequential Pre-Registration
Ceilings may lift **individually** before chain completes. If A1 lands PASS in S85 while B1/B2 remain open, P_obs_aligned moves 7/9 → 8/9 as a standalone event citing this DAG. Downstream verdicts cite `content_sha256=0f8cb99b…` before updating P_obs_aligned.

## When to invoke this memory
- Whenever sin²θ_W or α_s gets re-classified
- Whenever P_obs_aligned changes (it should cite this DAG)
- Whenever W4-48 ZFP column gets updated (cross-reference required)
- In S85+ planning: DERIV-I, DERIV-II, TAU-CROSS-SCALE, N1 TRANSFER-FUNCTION-74 are the 4 trigger gates that lift the ceiling

## Files
- Script: `computations/s84_w4_p_obs_aligned_ceiling.py`
- JSON: `computations/s84_w4_p_obs_aligned_ceiling_chain.json`
- NPZ: `computations/s84_w4_p_obs_aligned_ceiling.npz`
- PNG: `computations/s84_w4_p_obs_aligned_ceiling.png`
- Working paper: `sessions/archive/session-84/session-84-w4-workingpaper.md` §W4-49
- Registry: `sessions/framework/registry/pre-registered-observations.md` under tag `P-OBS-ALIGNED-CEILING-CHAIN`
