---
name: s110-cv2c-ointerface-coupled
description: S110-CF-CV2C-OINTERFACE PASS — Ô-interface φ_paasch/7n grading; AGREE sharpened to AGREE-COUPLED, but carried by the (3,0)/(0,0) sector ratio, NOT the BCS pairing-window gap ratios
metadata:
  type: project
---

**S110-CF-CV2C-OINTERFACE = PASS (COUPLED)**, test=5.134e-3 vs PASS_TOL=0.01 (grid-membership SET test, [VERIFY]). `audit_sha256=51976f89e5a4da98...`. Script/npz/png at `computations/session-110/s110_cf_cv2c_ointerface.*`; WP §W4a-5 in `sessions/session-110/session-110-w4-workingpaper.md`.

**The gate**: does the SAME φ_paasch/7n quantization grade the dimensionless Ô **input** (B2-sector ratios feeding λ_eff=0.038935, N₀=14.0233 in M_KK=M_Pl·exp(−1/(λ_eff·N₀))) as the **output** mass ladder (N(p)/N(K)=75/49=1.5306, 0.063% from φ_paasch)? Sharpens inv-11 W5-1 AGREE → **AGREE-COUPLED**.

**The non-obvious structural fact (carry-forward)**: the COUPLED verdict is carried SPECIFICALLY by the **(3,0)/(0,0) eigenvalue ratio** (= the φ_paasch-defining sector at τ_fold=0.19, reads 1.522754) landing 0.51% from the OUTPUT node 75/49 — NOT by the BCS pairing-window gap ratios. Strict λ_eff/N₀ pairing-window family (excluding the (3,0) sector) min dev = 1.16e-2 (`lam(0,2)/lam(0,0)→1.2`), just ABOVE the 1% band; the genuine BCS gaps `Δ_mf/Δ_rich=1.591` and `E_vH/Δ_mf=1.155` sit ~3.8–3.9% from φ_paasch / N_ratio[1]=1.2. So the input-layer grid-coincidence is the φ_paasch *spectral* channel reappearing, while the *pairing-window gap* channel is on an adjacent ~4%-looser grading. Not circular: 75/49 is Paasch's proton/kaon mass-NUMBER ratio (output construct); (3,0)/(0,0) is an INPUT D_K eigenvalue ratio — independently defined, coincide to 0.5%.

**B2 = (1,1) mult-8 "optical" band** (Fock mult (1,4,3) for (B1,B2,B3); `Delta_B2=0.732026`, `T_GGE_B2=0.668` canonical). Pairing window 2Δ_B2≈1.38 M_KK below M_KK; N(0)=14.02 gap-edge DOS → g·N(0)=3.24 (S22c). Sources: inv-11 W1-1/W1-2 transmutation build (`inv11_w1_mkk_dimensional_transmutation.npz`: E_vH=0.8453, E_min=0.8197, E_max=5.419, Δ_mf=0.7320, Δ_rich=0.4600, Δ_ed=0.4545); 7n grid `inv3_w3_casimir_graded_nj_7n.npz` (N(j)=[7,35,42,98,150]; 49=7², 98=7·14 are 7-graded; 150 is NOT 7n — supports the "7 is a mode-MULTIPLICITY unit, not a dimension" reading from [[paasch-reference]]).

CONFLICT (FAIL) cannot fire structurally: both input and output are exact eigenvalue ratios on a FINITE spectral triple (discrete Peter-Weyl mesh) — no provably-continuous input exists. Plan pinned canonical SHA e5a7587 but disk was 935c8f24 (in-session φ_paasch PROVENANCE backfill, value unchanged); resolved by runtime npz-ground-truth per substrate-first-canonical-sourcing §(ii.B). Relates to [[paasch-reference]] (n3=10, 75/49 entry, fN label).
