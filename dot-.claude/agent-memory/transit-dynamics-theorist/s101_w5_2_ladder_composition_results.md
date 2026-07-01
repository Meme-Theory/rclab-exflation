---
name: s101-w5-2-ladder-composition
description: S101 W5-2 LADDER-COMPOSITION — B1 stage-split B1a·W·B1b SU(1,1) recomposition + F_amp-slot cross-check; convention-coherence is the test
metadata:
  type: project
---

# S101-LADDER-COMPOSITION (W5-2) — B1 split + F_amp-slot cross-check

**Outcome**: composite **INFO** (pre-registered). r_comp ~ 1e-13 (machine-zero, magnitude PASS); coherent-phase caveat FIRES on the F_amp-slot statement ⇒ INFO per the binding pre-registration.

**Why:** The F_amp-slot consistency claim (does the window insertion alter the UNIFIED-AS-79 F_amp slot occupancy?) requires the relative phase between the window stage and B2; the S79 P2-A anchors (|β₁|²~4.3e4, |β₂|²=1700) carry MAGNITUDES ONLY. Pre-registered INFO clause (WP hypothesis: "coherent-phase caveat fires ⇒ pre-registered INFO").

## SU(1,1) convention (Sage-verified)
S79 eq(3)-(4): `α₃=α₂α₁+β₂β₁*`, `β₃=α₂β₁+β₂α₁*`. Matrix form-1 `B=[[α, conj(β)],[β, conj(α)]]`, **product order = temporal order L→R**: `B_total = B_first · B_second · …`. So B1=B1a·W·B1b (B1a leftmost=first). The naive `B2·B1` does NOT match; must use B1·B2 with form-1.

## Construction (convention coherence is load-bearing)
- ALL three factors use SAME tuple `BD-in-out-Z-PUMP-branchC-foldclock`. W = W5-1 window TM `M_delta(Om_off)·M_box(mu²_c,L)·M_delta(Om_on)`, re-evaluated in-script → reproduces canonical β²=2.118266e-6 to rel 1.2e-14.
- B1a (SS→on), B1b (off→WKB) = FREE flanking propagations (V=0 ⇒ mu²=k²). In BD basis a free propagation is a PURE PHASE: |β_a|²=|β_b|²≈3e-33 (machine zero). So B1a·W·B1b = (phase)·W·(phase), |β_composed|²=|β_W|² EXACTLY.
- r_comp = ||β_composed|²/|β_B1,unsplit|² − 1| ~ 1e-14 to 1e-13, INVARIANT to free-tail length (1L…1000L) — convention-coherence signature. Unitarity ~2e-16 per factor + composed.

## Clock incompatibility (reusable finding)
s64 MS dense grid (500 pts, tau∈[0.01,0.45], Δtau≈8.8e-4) is COARSER than the entire impulsive window (tau∈[0.18994874,0.19005127], width 1.025e-4). All 3 window edges collapse to s64 idx 204; `s64 deta_window=0`. s64 conformal `eta` SATURATES at the fold (dS conformal time→const, eta_fold≈0.001725). The two clocks are NOT interconvertible by a factor. The local impulsive dynamics MUST be in the fold-conformal clock (Δeta=1.13e-3 M_KK⁻¹). s64 provides only the BARRIER `k2_over_zppz_fold=107.636` (k² dominates z''/z by 108× at fold ⇒ free flanking segments).

## x6.96 hazard FAIL signature (gate is not vacuous)
Coherent (Z-PUMP all factors): r_comp=7.5e-14 PASS. Incoherent (sqrt(a)-pump vs Z-PUMP weight-mix at split points, residual ~0.80): r_comp=0.855 → beyond 5e-2 FAIL edge (13 OOM inflation). The Z-PUMP/sqrt(a)-pump β² ratio = 6.956 IS the x6.96 silent-inheritance class the S-1 adjudication closed.

## F_amp-slot arithmetic
|β_W|²=2.118e-6 is 8.90 OOM below B2 anchor (1700), 183405× below F_amp_slot (0.3885). Window ΔN=1.10e-3 vs B2 N~3 ⇒ 2727× shorter ⇒ STAGE not slot-renormalization. Max coherent slot perturbation: S_W=|α_W+β_W|²∈[0.997093,1.002915] ⇒ ≤0.29%, but PHASE-DEPENDENT (swings ±0.0029 with φ_W) ⇒ caveat fires. F_amp_sc=47.92 (3PI, S82 W3-5), slot-adjusted 0.3885 (k_a2) — NOT named constants in canonical_constants.py (live in plan/registry CF22).

substitution chain bound: r_comp ≤ 4·eps_W·(cosh-factor~1)=4·1.456e-3=5.82e-3; PASS edge 1.0e-2=1.72× bound; FAIL 5.0e-2=8.6× bound.
