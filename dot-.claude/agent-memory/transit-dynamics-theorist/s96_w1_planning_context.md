---
name: s96-w1-planning-context
description: S96 Wave-1 (emergent FRW a(t) closure, cluster C1 FLAGSHIP) plan-authoring context — what S95 already settled, what the 7 gates build on
metadata:
  type: project
---

# S96 W1 — Emergent FRW a(t) closure (cluster C1, FLAGSHIP, multi-session)

Authored `sessions/session-plan/session-96-plan-w1.md` (7 gates). Owner = transit-dynamics-theorist. Carry-forward source = 31 capstone-review syntheses (`sessions/framework/equation-collab/*-synthesis.md §V`), NOT a prior-session WP. Dedup key = C1 cluster (~15 reviewers → 7 distinct gates).

**Why:** Cluster C1 (derive a(t)) is the panel's #1-converged harvest. The capstone delivers the EH kinematic skeleton (a₂) but NOT the sourced dynamical FRW; every late-time observable borrows ΛCDM's H(t).

**How to apply:** When any future S96+ gate touches the a(t) closure, build on the S95 W3-3 superseding INFO (below) — do NOT re-derive the single-crystal divergence.

## LOAD-BEARING — what S95 already settled (do NOT recompute)
- **S95-W3-3-BACK-REACTION-CLOSURE** has TWO verdict lines. The SECOND (`supersedes=32c43a9f...`) is canonical: composite=INFO. Single-crystal source DIVERGES (`sc_diverges=True, sc_runaway=True, sc_has_fixed_point=False`), BUT the NOMINAL fabric-occupation reading has a CONDITIONAL fixed point: `nominal_tau_star=0.451041`, `nominal_H2_star_reduced=7.478844e-03`, stiffness `nominal_stiffness_d2S_over_dS=5.417550` (= ks_threshold). `rho_relic_MKK=26.553854` (B1=2.7792, B2=21.8876, B3=1.8871). `wellposed=True` (nominal). `kappa_drive_fold=0.234353`. Source is definite-positive all branches.
- **S95-W3-2-EFF-FRIEDMANN-GENRE**: composite=INFO. The H²(τ,τ̇) closed form EXISTS (`closed_form_exists=True, count_form_independent=True`) but is blocked by `residual_free_normalization_count=2`, `free_scalars=Z_norm+V0`. Genre = IKKT-matrix-model (`matrix_model_class=True, no_T_duality, no_Hagedorn`). `a2_E3_fold=2.018144`, `dS_fold=58672.80`, `G_DeWitt=5.0`, `f2_dict=92.0`. This IS the kaku V.1 "2-vs-3 normalization residual" — count_trackA=1 vs count_trackB=2.
- **S95-W3-1-EMERGENT-EIH-LIFT**: PASS. `noether_ratio=1/2`, `obstruction_norm_onshell=0.0`, on-shell `∇_μ G_eff^μν=0` EXACT on modulus EOM, scheme-independent. BUT `seconds_norm_open(a(t)_magnitude_only)=True` — the M_KK⁻¹→seconds normalization is the open piece. Lift is from internal K; emergent g_M lift is "owed."
- **S95-W3-5-EMERGENT-EP-NLO**: PASS. `kappa_EP=1.000000` EXACT (Reading A = geometric Bochner universal quarter; Lichnerowicz R/4). EP discriminator = geodesic-deviation curvature coupling, NOT Casimir self-energy. The NNLO Casimir discriminator (C3, W3 of S96) is where value-content first appears — NOT a W1 item.
- **S95-W5-4-COMPRESSIBILITY-G-N**: INFO. `Z_fold=74730.7641`, `a2_fold=2776.165389`, `G_N=1/(16π·a2)·M_KK²=1.2986e-39 GeV⁻²`. SHEAR channel Z FLOWS (factor 2.324); VOLUME channel FLAT (det_g=1). Corroborates PROVEN G6 (dG/dτ=0).

## Canonical pins verified in canonical_constants.py (use these)
- `M_KK = 7.428660036284456e16` GeV (line ~?); `tau_fold = 0.19` (288); `c_fabric = 209.97368021` (503)
- `a_0_FW_zeta = 6440.0` (603); `a_2_FW_zeta = 2776.165389` (604); `a_4_FW_zeta = 1350.7216` (464)
- `G_DeWitt = 5.0` (500); `n_pairs = 59.8` (394); `P_exc_kz = 1.0` (512)
- `Mach_max_framework = 13.75` (1994), `Mach_max` alias (1996)
- **SI: `hbar_SI = 1.054571817e-34` J·s (line 43); `GeV_to_inv_s = 1.5193e24` s⁻¹ (line 238)** — gate-3 M_KK→seconds machinery EXISTS.
- S86 `s86_w11_lab_si_translation.py` already does the M_KK→SI translation (uses GeV_to_inv_s, hbar_SI, M_KK). S52 output: `5.573349e-04 M_KK⁻¹ = 1.680e+03 seconds`.

## NOT-yet-pinned (gate-3 / hygiene targets)
- `tau_NEC = 1.383`, `t_star = 0.08832`, `Z_fold` (fork: S95 W5-4 gives 74730.76 shear-channel), `R₁` exact-vs-float. These are W7 hygiene mostly, but gate-3 promotes a seconds-normalization constant.

## The 7 W1 gates (gate-ID space clear of S95)
1. S96-W1-AOFT-FRIEDMANN-MAP (flagship; first leg = lift Bianchi K→g_M + construct S_eff[g_M]; defer Z_norm/V0 pin to leg-2, seconds to gate-3)
2. S96-W1-ONEILL-NONFLAT (van-den-dungen V.1: cross-terms under O'Neill A≠0; Gilkey a_4 A-tensor term)
3. S96-W1-MKK-SECONDS (mack: M_KK⁻¹→seconds; closes the seconds_norm_open from W3-1)
4. S96-W1-VOLOVIK-2FLUID (volovik V.7: two-fluid normal+superfluid; normal component sources H²)
5. S96-W1-GFT-FRIEDMANN (lqg V.3: LQC/GFT-condensate effective-Friedmann transfer target)
6. S96-W1-TAUDOT-PROFILE (transit V.3: global τ̇(τ) one-param family bounded by fold rate + clock)
7. S96-W1-QFLOW-RESIDUAL (kaku V.1: reconcile q-flow vs τ-flow {Z_norm,V0} 2-vs-3 normalization)

## Decision-point logic
Gate-3 (seconds) is a PREREQUISITE for the a(t) MAGNITUDE in gate-1/4/5; gate-7 ({Z_norm,V0}) is a prereq for collapsing W3-2's residual_free_normalization_count=2→0. Gate-6 (τ̇ profile) feeds the rate into gate-1's ρ_relic(τ) integration. Gate-2 (O'Neill) is the STRUCTURAL prerequisite (van-den-dungen): if cross-terms grow O(1) under bundling, the additive S_SA=a₀−a₂+a₄ does NOT lift to curved M⁴ and the whole a(t) closure must carry cross-terms.
