---
name: inv11-w5-2-gravastar-interior
description: INV11-W5-2 INFO — substrate compact-object interior is a HORIZONLESS Lobo-DE gravastar; v(r) discharges CF-S105-RELAY-VR-CONSTRUCTION; QNM are trapped (echo-prone) normal modes not ringdown
metadata:
  type: project
---

INV11-W5-2 (investigation 11, W5-2; verdict INFO, audit_sha256=04effc46…9315e3) built the substrate compact-object interior solution. Result: the substrate's compact object is a **horizonless ultracompact gravastar with a Lobo dark-energy core**, NOT a black hole.

**What LANDED (2/4 deliverables, sign_verdict=PASS):**
- v(r) acoustic flow EXTRACTED — `v(r)=v0·exp(-(r/r0)²/2)`, `v0=Mach_core·c_BLV=1.6487·0.485=0.79963`, `c_s=c_BLV=0.485` (constant a₂-channel). Reproduces S105-TYPEIV-EMT-COMPUTE to machine precision (`S105_match=True`). **CF-S105-RELAY-VR-CONSTRUCTION discharged — inv-11 W5-2 is its home.**
- Mach=1 acoustic horizon at `r_h = sqrt(2·ln(Mach_core)) = sqrt(2·0.5) = 1.0000` exactly (single crossover = S105 r_g=1; the Γ_sub=c_s²(1−Mach²) sign-flip IS the Mach=1 surface).

**What is UNPINNED (the natural-split INFO; route to Q3 wave-together {v(r)-acoustic | nuclear-EOS-TOV | de-Sitter-core}):**
- **QNM are TRAPPED normal modes, NOT decaying ringdown.** Acoustic Regge-Wheeler operator on the subsonic exterior (torch.linalg, 426 modes) gives `n_genuine_damped=0` (all Im(ω)≈0; max|Im|=7e-4 is BC-leak only). Fundamental `ω₀ = c_BLV/r0 = 0.485 + 0i [M_KK] = 3.60e16 GeV` — the acoustic cavity light-crossing frequency. This is PHYSICALLY CORRECT (a horizonless reflecting core has no outer horizon to leak through ⇒ Cardoso-Pani w-mode trapping ⇒ ECHO-PRONE not clean-ringdown), just not the "decaying ω_I<0" the plan PASS wanted.
- **M(R) has no self-bound surface.** TOV-analog on Lobo-DE EOS (w_core=−0.92, P_scale=Z_fold·c_BLV²=1.758e4): `C_max=2.4e-4` (n_physical=17 real-surface solutions but all diffuse; ~3 OOM below NS C~0.2). EOS pressure-scale normalization underdetermined by available inputs.

**Calibration lesson (vacuous-margin):** first run FALSE-PASSED — accepted ω_I=−4.4e-19 roundoff as "ω_I<0" ringdown AND grid-edge R=12.0 as a "bound". Corrected the verdict logic to require GENUINE damping (Im < −1e-6) and a PHYSICAL surface (R<0.95·R_grid ∧ C>1e-3). This is correcting vacuous-margin acceptance, NOT iterate-to-PASS. Honest verdict is INFO.

**Observational content:** the LISA-EMRI discriminator for this object is ECHO phenomenology (the trapped-mode late-time echoes), NOT the fundamental ringdown — a substrate-IS prediction distinct from a clean-ringdown black hole.

**EOS framing (load-bearing):** vacuum is a Lobo dark-energy condensate (w_core=−0.92), NOT Mazur-Mottola de Sitter (8% structurally-significant departure from w=−1; PROVEN, sub-gravastar-structure-landau.md). The seed's "de Sitter-core" = Lobo dark-energy core.

Cross-refs: [[desitter-temperature-taxonomy]] (de Sitter thermodynamics adjacency); S105-TYPEIV-EMT-COMPUTE (the certified a₂-channel acoustic EMT this builds on); S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC (named the unpinned v(r)).
