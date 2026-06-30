---
name: inv8-w2-3-born-rule-nogo
description: INV8-W2-3 — Born rule is a substrate INPUT not derivable from GGE coarse-graining (mixed-marginal no-go); Gleason gives consistency only
metadata:
  type: project
---

# INV8-W2-3 — Born Rule Derive-or-No-Go (INFO / Branch B no-go)

**Verdict INFO** (investigation-8 track). `audit_sha256=1d970e667b0f5b49708492785b0bbb0ff044a80c033fd2849240e390b8aa42df`. Executes S58 addendum §VI.1 (flagged "defined but not yet attempted" — was FRESH).

**The structural result (the generative principle, not the number):**
The GGE `ρ_GGE=(1/Z)∏_k exp(−λ_k I_k)` is DIAGONAL in the Richardson-Gaudin (quasiparticle-number) eigenbasis because the 8 integrals are mutually-commuting occupation operators ⇒ it FACTORIZES over modes ⇒ tracing out 7 of 8 modes is a pure marginalization leaving the 8th's single-mode factor exactly. For the post-transit pure-Bogoliubov state the per-mode reduced state in the pairing basis is `ρ_A=diag(u_k²,v_k²)`.

**Why this forces a genuine two-track outcome — and lands Branch B:**
- EIGENBASIS test: `{p_i}={u²,v²}={|ψ_i|²}` EXACTLY (max_dev=0 over all 8 modes). This is NECESSARY but NOT sufficient — forced by construction (marginal eigenvalues ARE squared amplitudes in the eigenbasis). It cannot distinguish derived-from-input.
- MISALIGNED-BASIS structural probe IS the discriminator: a paired GGE marginal is MIXED (purity_B2=Tr(ρ²)=0.7731<1, purity_B3=0.9843). Gleason guarantees `p(θ)=Tr(ρ_A P_θ)` is the unique frame function for the density operator; the L²-reading posits the PURE-state `|⟨ψ|θ⟩|²`. They agree IFF ρ_A=|ψ⟩⟨ψ| (pure). For mixed ρ_A they DIVERGE — `mixed_basis_gap=0.337≫1e-6`. So the GGE trace yields a MIXED operator, NOT the pure |ψ|² the derivation needs.

**Reusable lesson (principle-theoretic):** Gleason supplies CONSISTENCY (IF frame-function THEN Tr(ρP)), never DERIVATION. A coarse-graining "reproduces |ψ|²" claim must be tested OFF the eigenbasis — the eigenbasis coincidence is trivial alignment, the misaligned-basis gap (∝ 1−purity) is the real test. The B1 unpaired mode (u=1,v=0) is PURE and passes trivially; only the PAIRED modes carry the no-go. The Born rule sits on the same footing as the metric signature: a substrate INPUT.

**Constraint-map:** S16 Born-rule open_channel DEFENSIBLE → INPUT (GGE-coarse-graining corridor to derivation CLOSED, informative). Does NOT close G-3 by derivation. Points (einstein B-2) to Penrose-Diósi `E_G(a₂, band-diff)` as the DERIVED measurement scale (next constructive attack on WHY a frame function is selected). Consistent with INV8-W4-1 M2 split: the off-eigenbasis (entanglement) content is exactly what the thermodynamic trace cannot derive.

**Substrate-first fallback used:** INV8-W1-1 absent at dispatch; s52_bogoliubov_amp.npz (u_k,v_k per 8 modes: 4×B2 u=0.9325/v=0.3612, 1×B1 u=1/v=0, 3×B3 u=0.9960/v=0.0889) is the substrate-first source. The λ_k weighting governs only the GGE labelling, NOT the marginal occupation (u²/v² from the coefficients regardless). `w1_1_present=False` disclosed in verdict + npz.

Artifacts: `computations/investigation-8/inv8_w2_3_born_rule_gge_coarse_grain.{py,npz,png}`. Links: [[investigation-1-s108-survey]] (G-3 un-derived-QM, BELL-GGE-70).
