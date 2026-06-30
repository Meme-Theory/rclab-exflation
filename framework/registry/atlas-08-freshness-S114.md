# atlas-08 Freshness Reconciliation — S114

**Date**: 2026-06-24 (`/rclab-plan --session 115` plan-freeze, Phase 1c-REGISTERS.MAINTAIN)
**Scope**: fold the S114 closures (`computations/session-114/s114_gate_verdicts.txt`, 10 gates) into `atlas-08-open-questions.md`, preserving the verbatim originals (atlas-08 §V convention: closures recorded as freshness updates, never overwrites).
**Authoritative source**: the four S114 per-wave WP synthesis/constraint-map sections + the two S114 workshop wrap-ups (`sessions/session-114/workshops/w-1-taufold-canonical-value.md`, `w-2-d4-rightreg-su3r-admissibility.md`) + `session-114-housekeeping.md`.

## Questions advanced (inline freshness bullets added)

### Q18b — Yukawa hierarchy beyond rank-1 (SHAPE branch)

**Advanced** (S114 W3-1 + W3-3 + the W-2 workshop). The SHAPE-branch of the fermion-mass hierarchy gained a STRUCTURAL wall and a COMPLETED obstruction genus:

- `CF-S114-YUK-SHAPE-WALL-VII-LANDING` PASS (audit `51f411950ae58c74c635d40fa9fb711acdc9b0a172a5959da5cecc710738171f`) → **§VII.CK "SHAPE-Branch Homogeneity Obstruction"** STAGE-1-CANDIDATE, D1–D3 closed class (D1 machine-exact `|Tr[γ₉ D_K]| = |Tr[γ₉ D_K³]| = 0`).
- `CF-S114-YUK-RIGHTREG-CONNECTION` INFO (audit `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`) → D4 (right-regular SU(3)_R `Y_R`) left open (outside left A_K-calculus, residual = 1.0 EXACT, but generation-diagonal `t(O)=0`).
- S114 **W-2 workshop** (van-den-dungen × baptista, CONVERGED R2) → D4 **CLOSED-EXTERNAL-AS-A-COUPLING** by the commutant-calculus gap: SU(3)_R is the commutant of A_K's left action (real isometry, `[L_g,R_h]=0`), its fermion coupling admissible only via the crossed product `A_K⋊SU(3)_R`, outside `Ω¹_{D_K}(A_K)` by `t(O)=±1≠0`. Genus {A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular} COMPLETE as a statement about A_K-internal couplings. Hierarchy NUMBER stays HELD (NON-PROMOTION-BY-HELD-NUMBER, unchanged).

**S115 forward**: `CF-S115-VIICK-STAGE2-VERIFY` (D1–D3 → STAGE-3-PERMANENT) + `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (D4 → STAGE-3-PERMANENT-UNCONDITIONAL) + `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` (the external corridor's forced PMNS texture residue).

## Questions NOT requiring an atlas-08 bullet (reconciled elsewhere in-session)

- **τ_fold (A4)** — W2-2 TAUFOLD INFO (region van-Hove-selected, value conditional) + the W-1 workshop two-value non-fungible convention landing: reconciled at the **atlas-04 A4 cell** + capstone §6.3 in-session (S114 housekeeping §A5/§A6; W-1 workshop "Effected In-Session" items 3a/3b). atlas-08 carries no dedicated τ_fold question; A4 is the canonical home.
- **CC residual-3% (C10)** — W2-3 CCRESID FAIL (χ_q fold-frozen, standing q-channel limitation confirmed): reconciled at the **atlas-04 C10 cell** + capstone §8.5 in-session (housekeeping §A5/§A7). Q29 (BBN-VOLOVIK-67) keys on the **BBN-epoch** arm, which is UNCHANGED-OPEN by S114 (the present-epoch residual-3% confirmation does not move the BBN-epoch tension) — no Q29 bullet owed.
- **A_s magnitude** — W4-1 FUNCTIONAL-PLURALISM-PERMANENT: routed to the **mack falsifier surface** (Row #12 / §EVOI.BF, housekeeping §A8) + refreshed at `evoi-framework.md §EVOI.BF` this plan-freeze. No atlas-08 question tracks A_s magnitude directly.

## Observational rows (mack-landed in-session; no plan-time owed)

The S114 observational-VALUE updates were landed by `mack-cosmic-bridge` (sole writer) during S114: Row #71 (f·σ8 growth joint σ-distance, the SOLE live non-CMB falsifier), Row #88 (dense-matter STRUCTURAL NO-GO + watchlist `S113-CO-SIGNDISC-FRIB-L-WATCH → CLOSED`), Row #79 (σ_SI sharpen, HK-170X-DM mis-attributed/CLOSED), Row #12 (A_s functional-pluralism). atlas-08's observational class (Q37–Q42) carries no new S114 bullet — these are detector-bound live-watch already pinned on the falsifier surface.

## Re-stamp note

A full atlas-08 header re-stamp to "Through S114" awaits the next `/weave --update` (per the standing convention — freshness bullets land now; the banner re-stamp rides the index rebuild).
