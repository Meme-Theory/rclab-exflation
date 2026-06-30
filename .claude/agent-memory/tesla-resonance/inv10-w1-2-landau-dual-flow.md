---
name: inv10-w1-2-landau-dual-flow
description: INV10-W1-2 result — substrate roton/Landau v_c; the dual-flow structure (modulus laminar vs fold-transit hyper-critical) under one min[eps/p] form
metadata:
  type: project
---

**INV10-W1-2-ROTON-LANDAU-VC (PASS, investigation-10):** the Mach-13.75 fold transit is DISSIPATIVE (emits Leggett-channel rotons = 2nd DM channel). Substrate roton = the optical/Leggett C-sector branch of `s62_phonon_dispersion_full.npz` (99.9% C-weight, S58 Leggett=roton).

**Key numbers (read off s62 dispersion at L_max=10):**
- Optical branch is **gapped-monotone** (degenerate-roton): Δ_rot = 0.049006 M_KK (= ω_L0 band-edge gap at k=0), p₀=0, μ_r = −2.0066 M_KK⁻¹ (concave, negative effective mass). Roton-form Δ_rot/p₀ = ∞ (k=0 gapped mode does NOT set v_c).
- Landau **v_c = min_p[ε(p)/p] = 0.311838 M_KK** at zone edge k*=1.41744 (global minimum over all 45 bands; optical and acoustic branches give the same value).
- v_transit = Mach_max_framework·c_fabric = 13.75·209.97368021 = **2887.1381 M_KK**.
- **v_transit/v_c = 9258×** — hyper-critical by ~4 OOM, not merely supersonic. sign(v_transit−v_c)=+1.

**DUAL-FLOW STRUCTURAL INSIGHT (the durable result).** The framework has TWO distinct Landau-criterion flows, same `min ε/p` form, opposite verdicts:
1. **S72 laminar protection** — the MODULUS τ rolling through the BCS condensate at v_terminal=26.54 M_KK is SUB-critical (laminar, dissipationless). [[permanent-resonance-results.md]] laminar-protection.
2. **INV10-W1-2 fold transit** — the van-Hove fold transit at 2887 M_KK against the OPTICAL/roton branch is HYPER-critical (dissipative).

These are different flows (modulus roll vs fold crossing), different velocities (26.54 vs 2887), different branches (its own condensate vs optical/Leggett). NOT a contradiction — the MCP trace confirmed S72 only computed the modulus case; the fold-transit-vs-optical comparison was open. When you see "v_c already computed" check WHICH flow against WHICH branch.

**Degenerate-roton + Umklapp:** SU(3) has no Brillouin-zone boundary (qa B-QA-2) ⇒ the gapped Leggett mode has no Umklapp decay ⇒ emitted rotons are ETERNAL = a DM-stability mechanism. The dissipative verdict adjudicates C1 on the dissipation axis WITHOUT needing ∇φ (Landau is mode-emission, not flow-gradient) — sidesteps the φ=0 problem that blocks analog-horizon readings (bears on INV10-W4-2).

Artifacts: `computations/investigation-10/inv10_w1_roton_landau_vc.{py,npz,png}`; verdict audit_sha256=d710eba31abb7430...; WP §W1-2 in investigation-10-w1-workingpaper.md.
