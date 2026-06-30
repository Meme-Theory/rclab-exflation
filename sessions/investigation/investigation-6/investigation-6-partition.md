# Investigation 6 — Wave Partition Manifest

**Date**: 2026-06-14
**Seed**: `investigation-6-seed.md` (3-agent survey batch: dirac-antimatter-theorist + kaluza-klein-theorist + feynman-theorist)
**Shape**: fanout (4 per-wave plan files + thin plan-index)
**Source**: `investigation-6-seed.md §"Candidate gate table"` — this manifest re-buckets that table into the per-wave planner-swarm input.

Per-wave planners read this manifest's "assigned items" rows + the seed file. Owner = the wave's domain-survey author (reviewer-origin owner). Gate executors (`agent_type` in each gate block) are suggested per gate; the per-wave planner finalizes by substrate match.

---

## Wave 1 — KK scale-bracket & moduli stabilization

- **Owner-planner**: `kaluza-klein-theorist` (seed author; owns the M_KK-scale + KK-reduction + moduli-stabilization + compact-object cluster)
- **Types**: compute × 4
- **Theme**: the framework's single un-pinned dimensional input — M_KK — is treated as a number when it is a 6.79× gauge-vs-gravity bracket frozen since S42; every absolute-magnitude breakage (A_s, CC) is the bracket cashing out. This wave attacks the scale axis with KK-native machinery the framework uniquely holds the spectrum to run (Casimir volume-stabilization, threshold running, the KK soliton).

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV6-W1-1 | compute | kaluza-klein-theorist | M_KK both routes (gravity-zeta 7.428660e16 vs Kerner-gauge 5.041680e17); propagate 6.79× into a₀ (×2125) + a₂ (×46) — band injected into A_s/CC |
| 2 | INV6-W1-2 | compute | kaluza-klein-theorist | graded Casimir E_Cas(τ) of the 992-mode tower in the VOLUME direction; volume minimum → derives det-g constraint + third M_KK determination |
| 3 | INV6-W1-3 | compute | kaluza-klein-theorist | three-coupling KK-tower threshold running M_KK→m_Z (Cartan Trace Identity + (p,q) sum); (α_em, sin²θ_W, α_s) within 2% + m_H band collapse |
| 4 | INV6-W1-4 | compute | kaluza-klein-theorist | localized fiber-density excitation (Gross-Perry-Sorkin KK soliton): mass~M_KK, compactness, QNM ladder; tests the single-vs-bimetric cone fork |

- **Natural-split candidates** (if the wave stalls): {INV6-W1-1, INV6-W1-3} scale/coupling sub-wave | {INV6-W1-2, INV6-W1-4} moduli/soliton sub-wave.
- **Shared inputs**: `s84_spectrum_cache_L12_tau019.npz` (992-mode spectrum; W1-2/W1-3/W1-4); frozen `M_KK`/`M_KK_kerner`/a₂_FW_zeta/f₂/G_N canonicals (W1-1); Cartan Trace Identity S63 (W1-3); S52 unified-action small-oscillation ladder (W1-4).
- **Cross-track / cross-investigation notes**: W1-4 (KK soliton) is distinct from **inv-4 W2-4** (Gregory-Laflamme GL stability of the bulk M⁴×SU(3)) — localized soliton vs bulk instability; cross-reference. W1-1/W1-2 feed the INV6-W4-1 workshop. W1-1's A_s-band output relieves (does NOT replace) the A_s computes in inv-3/4/5 + INV6-W2-2 (scale-normalization band vs absolute floor).

## Wave 2 — Quantum-loop gravity sector & A_s normalization

- **Owner-planner**: `feynman-theorist` (seed author; path-integral / spectral-action-loop / Parker-creation vantage)
- **Types**: compute × 5
- **Theme**: the framework computed the *emergent low-energy* side of its gravity sector thoroughly while leaving the *quantum-loop* side almost untouched — no graviton loop, no finiteness statement, no Γ[τ] trajectory — and that asymmetry sources three of its five biggest gaps. The A_s 3.15-OOM miss + the BROKEN K_pivot are the absolute-normalization face. This wave attacks both with one-loop / heat-kernel / Bogoliubov machinery, most of it sitting on already-cached eigenvalue data.

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV6-W2-1 | compute | feynman-theorist | Γ[τ]=S_cl+½Tr ln(D_K²(τ)/μ²)=−½ζ'_D(0,τ) trajectory over τ∈[0.05,0.30]; correct modulus action + induced G_N(τ)/Λ(τ) signs + Sakharov M_KK self-consistency |
| 2 | INV6-W2-2 | compute | transit-dynamics-theorist (or feynman) | TRANSIT-PS-67 as Parker-Bogoliubov P_ζ(k)=(k³/2π²)|β_k|² through the fold + adiabatic reg; sets absolute A_s AND k→K_pivot map (joint G-F2/G-F4 closer) |
| 3 | INV6-W2-3 | compute | feynman-theorist | emergent graviton propagator from a₂ fluctuation; two-loop Goroff-Sagnotti R³ on finite substrate (van Nuland-van Suijlekom #17) — finite-at-M_KK or 1/ε? |
| 4 | INV6-W2-4 | compute | feynman-theorist | ω(k) to O(k⁴) for Goldstone + graviton-zero-mode on crystalline substrate (S106 κ=3); LIV bound + CPT-odd SME null (dirac UB-3 folded) |
| 5 | INV6-W2-5 | compute | feynman-theorist | substrate graviton spectral function ρ(ω); UV scaling vs asymptotic-safety/CDT d_s→2 — substrate predicts d_s→8 (no reduction), contrarian falsifiable signature |

- **Natural-split candidates**: {INV6-W2-1, INV6-W2-3, INV6-W2-5} graviton-loop / spectral-function sub-wave | {INV6-W2-2, INV6-W2-4} A_s / emergent-Lorentz sub-wave.
- **Shared inputs**: L_max=12 / 992-mode eigenvalue caches (W2-1/W2-3/W2-5); S96-plan-w3 moment pins a₀=6440/a₂=2776.165/a₄=1350.72 (W2-1); van Nuland-van Suijlekom one-loop-SA formalism, corpus #17 arXiv:2107.08485 (W2-3); S38 sudden-quench Bogoliubov machinery 59.8 pairs/P_exc=1.000 (W2-2); S106 crystalline mean-action κ=3 + `[J,D_K]=0` (W2-4); d_s(σ) machinery S92/S104-S106 + Lorentzian-QG papers #31/#32 (W2-5).
- **Cross-track / cross-investigation notes**: W2-1 (Γ[τ]) is the COMPUTE that feeds **inv-5 W3-2** (two-effective-actions adjudication connes↔landau) — flag for promotion if it lands. W2-2 (A_s) is the 4th A_s route, distinct from **inv-3 W2-3** (near-floor-DOS), **inv-4 W1-4** (exit-horizon greybody), **inv-5 W2-1** (impulse-quench), uniquely joint with K_pivot. Any `falsifier-master-inventory.md` row from A_s/d_s outputs is session-promotion + mack sole-writer (NOT an investigation edit). W2-1's M_KK self-consistency feeds the INV6-W4-1 workshop.

## Wave 3 — Baryogenesis, CPT & the antimatter sector

- **Owner-planner**: `dirac-antimatter-theorist` (seed author; Dirac/CPT/real-structure-J/baryogenesis vantage)
- **Types**: compute × 4
- **Theme**: the framework's static CPT structure (`[J,D_K]=0`, BDI, T11) is genuinely PROVEN, but its *dynamical* baryogenesis is over-tagged as closed — a hand-posited φ_88-Cartan δA gives a prediction 13.5× / 1.1 OOM below the observed η_B. This wave attacks the magnitude (two distinct substrate enhancement mechanisms), the δA uniqueness (NCG deformation classification), and the missing spatial domain structure.

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV6-W3-1 | compute | dirac-antimatter-theorist | inter-branch GGE strong-rescattering phase at τ_fold (Row #67 8-branch infra) → Im[A_weak(φ_88)·A_strong(GGE)] into C6 η_B; supplies the missing ~13.5×? (LHCb-2025 lesson) |
| 2 | INV6-W3-2 | compute | dirac-antimatter-theorist (w/ connes-ncg context) | enumerate admissible J-breaking deformations of ℂ⊕ℍ⊕M₃(ℂ) (Boyle-Farnsworth/Bochniak-Sitarz, corpus #19/#22/#29); is φ_88-Cartan the UNIQUE minimal non-leptophilic J-breaker? |
| 3 | INV6-W3-3 | compute | dirac-antimatter-theorist (or feynman) | η_B as acoustic-Schwinger pair production from the Mach-13.75 transit field gradient (φ_CP=π/2); is the 1.1-OOM shortfall a Mach-number effect? |
| 4 | INV6-W3-4 | compute | dirac-antimatter-theorist | pre-transit acoustic sound-horizon (Mach-13.75) vs present Hubble scale; single-domain explanation for Fermi-LAT antimatter-fraction <10⁻⁵ / zero annihilation γ-flux |

- **gate_type rationale**: INV6-W3-2 is the dirac agent's self-labeled "structural workshop (connes-ncg + me)" — **re-typed compute**. Per `Investigating-Workshops.md §"is NOT" item 6`, a workshop requires DISAGREEMENT; here connes + dirac would AGREE on the NCG-classification method (apply Boyle-Farnsworth/Bochniak-Sitarz to enumerate admissible J-breakers). There is no competing-reading tension — only a derivation. So it is a compute (carrying NCG-classification context), not a workshop.
- **Natural-split candidates**: {INV6-W3-1, INV6-W3-3} η_B-magnitude sub-wave (two enhancement mechanisms) | {INV6-W3-2, INV6-W3-4} δA-structure / domain sub-wave.
- **Shared inputs**: 8-branch post-transit GGE spectrum + Row #67 two-speed data (W3-1); C6 amplitude chain ε_K7=0.00248/n_pairs=59.8/φ_CP=π/2 + `eta_BBN_obs`=6.12e-10±4e-12 (W3-1/W3-3); Boyle-Farnsworth/Bochniak-Sitarz corpus #19/#22/#29 + off-Jensen 35D moduli S76 W2-J (W3-2); Mach-13.75 transit acoustic profile + corpus #24/#25/#26 (W3-3/W3-4).
- **Cross-track note**: all η_B / δ_CP^PMNS falsifier-row mints + the EVOI status down-tag are session-track curated-register edits (HY1/HY2/HY3, seed §"Non-gate items") → session-promotion at close, NOT investigation gates. The computes here produce the NUMBERS those rows would cite; the rows themselves are mack/orchestrator session-track work.

## Wave 4 — M_KK determination-route reconciliation

- **Owner-planner**: `gen-physicist` (NEUTRAL — not a workshop participant; writes a balanced adjudication spec, no orchestrator angle per `feedback_review-dispatch-no-orchestrator-angle.md`)
- **Types**: workshop × 1
- **Theme**: the framework's #1 standing gap (M_KK) admits THREE concrete substrate determinations this investigation computes — the gauge-vs-gravity bracket (W1-1), the Casimir-volume minimum (W1-2), and the Sakharov-Γ[τ] self-consistency (W2-1). kaluza-klein and feynman read WHICH route is canonical OPPOSITELY (KK: Casimir-volume is the KK-native moduli-stabilization answer; Feynman: Sakharov-loop self-consistency is the deeper constraint). This is the one genuine Q1 adjudication of the batch.

| # | Gate ID | gate_type | Agents (EXACTLY 2) | One-line scope |
|:--|:--------|:----------|:-------------------|:---------------|
| 1 | INV6-W4-1 | workshop | kaluza-klein-theorist ↔ feynman-theorist (2 rounds) | Given the bracket + Casimir-volume + Sakharov determinations: is M_KK over-determined (→derived), under-determined (→single import), or does one route dominate? STRUCTURAL VERDICT + decisive forward gate |

- **adjudication_question (a)(b)(c)(d)**: (a) does the Casimir-volume minimum (KK B-KK1) fix M_KK and resolve the bracket toward the gravity route? (b) does the Sakharov-induced-G_N ↔ spectral-zeta self-consistency (Feynman B-F3) over-determine M_KK at the loop level, making the tree bracket an artifact? (c) if the three determinations DISAGREE, is M_KK a single irreducible import (NNU rank-1 §VII.BS confirmed); if they AGREE, is that a genuine derivation? (d) what single compute decides it?
- **Closure**: artifact-existence (Wrap-Up + Effected-In-Session + Carry-Forward Computations); NO verdict line.
- **Independence note**: exploratory adjudication workshop (domain advocates argue their case) — NOT a Stage-2 joint-theorem cross-check, so the no-prior-context rule does not apply; the two advocates are SUPPOSED to bring their domain reading.
- **DEDUP vs inv-3 W4 (explicit)**: inv-3 W4 = M_KK *derivability-in-principle* (Paasch mass-quantization vs scale-free spectral triple; spectral-geometer ↔ paasch). INV6-W4-1 = M_KK *determination-route reconciliation* (Casimir-volume vs Sakharov-loop vs gauge-gravity bracket; kaluza-klein ↔ feynman). Different agents/machinery/question. Cross-cite at both `/rclab-investigate` closes; do NOT merge.

---

## Dispatch summary

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | KK scale-bracket & moduli stabilization | kaluza-klein-theorist | compute×4 | 4 | investigation-6-plan-w1.md |
| 2 | Quantum-loop gravity sector & A_s normalization | feynman-theorist | compute×5 | 5 | investigation-6-plan-w2.md |
| 3 | Baryogenesis, CPT & the antimatter sector | dirac-antimatter-theorist | compute×4 | 4 | investigation-6-plan-w3.md |
| 4 | M_KK determination-route reconciliation | gen-physicist (neutral) | workshop×1 | 1 | investigation-6-plan-w4.md |

4 per-wave planners dispatched in ONE parallel batch (≤8 concurrent). Total **14 gates** (13 compute + 1 workshop).
