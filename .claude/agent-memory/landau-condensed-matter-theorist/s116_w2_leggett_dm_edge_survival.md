---
name: s116-w2-leggett-dm-edge-survival
description: S116 W2 landau×volovik workshop — survival vs sharpness two-observable separation for the inter-band Leggett DM mode; below-edge is NOT the DM-survival mechanism
metadata:
  type: project
---

# S116 W2 — Leggett DM edge-protection workshop (landau × volovik)

Adjudication: is the registered Leggett DM anchor `m_Leggett = 11.97·Δ_BCS = 5.5571 M_KK` below-edge kinematically protected (Reading B, my opener) or above-edge integrability/CPT-protected (Reading A, volovik)? Workshop doc: `sessions/session-116/workshops/s116-leggett-dm-edge-protection.md`. I CONCEDED the survival question to Reading A; held a re-scoped role for below-edge. The registry verdict (C11-conditional, graph-ANCHORED) is in the W3 WP / atlas-04 / `_promotion-triage` — those are canonical, not this note.

## Reusable lessons (the durable part)

1. **Pair-breaking of a collective mode is NUMBER-CONSERVING** (`[H_BCS,N_pair]=0`, volovik S73a). A collective mode decaying `1 → 2 BdG quasiparticles` is number-INCREASING; it reshuffles the relic CARRIER (collective mode → pair) without depleting `N_DM = Σ_k n(k)`. So **collective-mode LINEWIDTH ≠ relic depletion**. For ANY "DM as collective/Leggett mode" claim, survival is a relic-NUMBER question, not a linewidth question. The only genuine depletions: `2→0` (CPT-forbidden, BDI/[J,D_K]=0) and gravitational (`Γ_grav < H_0`, ~65-OOM margin). I conflated linewidth with depletion in my opener (L3); the correction is decisive.

2. **The kinematic pair-breaking threshold is ENERGY-vs-ENERGY — `ω_Leg < E_edge`, NO `√ρ_s`.** The `÷√ρ_s` converts a restoring curvature `√J_⊥` → frequency; it does NOT belong in a decay threshold. WS-1's eq(15c) `m < 2Δ_BCS·√ρ_s` AND my own L4 eq(7) ceiling `E_edge·√ρ_s = 13.35·Δ_BCS` BOTH carried the spurious `√ρ_s`. Stripped: sharp-mode ceiling = `E_edge^⊥` itself = `Δ_BCS + √3 = 2.196 M_KK = 4.73·Δ_BCS` (Sage-exact). Recurring convention trap — strip `√ρ_s` from any "below-edge" comparison.

3. **Two-observable separation (the EMERGENCE).** Two ORTHOGONAL substrate-IS→lab-IN bridges, NOT competing readings of one channel:
   - **Relic survival** `N_DM = Σ n(k)`: Reading A (CPT non-annihilation + GGE integrability `S_ent=0` + `Γ_grav<H_0`). REGISTERED (atlas-04 C11-conditional). Below-edge IRRELEVANT (number-conserving).
   - **Leggett-mode sharpness** (linewidth): below-edge kinematics `ω_Leg < E_edge^⊥`, lab Leggett Raman/IR peak-width (MgB₂, Fe-pnictide), modes `< 4.73·Δ_BCS`. `[CONJECTURE S117]`, convention-pinned.
   The convention/edge CF settles SHARPNESS; Reading A settles SURVIVAL regardless.

## Numbers (mass convention M, the consistent one — Sage-verified)

- Registered `5.5571 M_KK` IS the rest energy (consumed as a mass in `Ω_DM h²=0.120` / `σ_SI`; `ω_Leg²=J_⊥/χ_-` already inertia-dressed, so `÷√ρ_s` double-counts).
- Inter-band edge `E_edge^⊥ = Δ_BCS + √3 = 0.4643 + 1.7321 = 2.1963 M_KK = 4.73·Δ_BCS` (Lichnerowicz fiber floor `|λ|≥√3`; block-diagonality wall #2 forbids the pure-(0,0) channel — but volovik's caveat: that's a single-particle statement, the collective edge is a pairing-vertex quantity, CF must read it directly).
- `x^⊥ = ω_Leg/E_edge^⊥ = 5.5571/2.1963 = 2.53 > 1` → ABOVE edge → finite linewidth → survives by Reading A anyway.
- My opener's `x_G^⊥ = 0.897` was the doubly-optimistic corner (restoring-scale ∧ overall `ρ_s` not reduced `χ_-`). Reduced inertia: `χ_-=ρ_s/2 → x=1.268`, `ρ_s/3 → x=1.553` — all above edge.
- Light mode `ω_L1` (S48 `proven_1792`, atlas-07 hist 0.070 / canonical 0.138 — see omega_L1 note in MEMORY.md): below its INTRA-band edge `2Δ_BCS` → sharp/proven. DISTINCT object from the 79×-heavier 5.5571 anchor; S48 proven below-edge does NOT inherit to the heavy anchor (volovik's DE-inheritance, conceded).

## Carry-forward links
- `CF-S117-FREESTREAM-AT-ANCHOR` (live W3 CF): above-edge ⇒ carrier flips to quasiparticle PAIRS by structure-formation; freestream integral should use the PAIR occupation; coldness held by ALGEBRAIC `T^{0i}_4D=0` (CDM-by-construction S43/S44), not the collective-mode Bogoliubov occupation. [[s116_w3_goldstone_mass_ceiling]]
- `CF-S117-LEGGETT-EDGE-AND-STIFFNESS` **CLOSED S117-W4-3 PASS** (audit_sha256 `ba745a655acbec1a…`): direct read confirms **Convention M** — ω_Leg=5.5571 M_KK ABOVE the √ρ_s-free edge E_edge^⊥=Δ_BCS+√3=4.731·Δ_BCS, **x^⊥=2.5302>1** (matches pre-reg exact). Above-edge ROBUST on all 4 channels (mix/pure × Lichnerowicz/τ_fold) AND restoring-scale. **Durable theorem**: χ_-=ρ_s·f(1−f) ≤ ρ_s/4=1.99 for ANY band split (f=χ_1/χ_+; max at f=½) ⇒ the S116-opener below-edge corner x_G^⊥=0.897 (which used χ_-=ρ_s) is **mathematically IMPOSSIBLE**, not merely convention-wrong (f(1−f) max=¼). Even restoring-scale gives x^⊥≥1.793>1 for all χ_-. eq(15c)/(15d) √ρ_s WITHDRAWN→CHARACTERIZATION (registry forms still carry it; flag for mack re-scope). τ_fold-direct fiber gap 0.836<√3 (Jensen-deformed, NOT a bug) ⇒ LOWER edge ⇒ x^⊥=4.27 (even more above-edge); √3 is the conservative pre-reg. Survival UNCHANGED = Reading A.
