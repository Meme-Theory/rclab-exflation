---
name: s118-pmns-joint-admissibility
description: S118-W2-1 PASS — joint NuFIT 5.2 NO 3σ box (R+3 PMNS angles) NON-EMPTY over free lepton-texture family; under-determination survives; closes the S117 W2 joint question
metadata:
  type: project
---

**CF-S118-PMNS-JOINT-ADMISSIBILITY — PASS** (audit_sha256 `85520aa6…`, 2026-06-29). The joint NuFIT 5.2 NO 3σ box {R∈[17,66] ∧ sin²θ12∈[0.270,0.341] ∧ sin²θ23∈[0.434,0.610] ∧ sin²θ13∈[0.02029,0.02391]} is **NON-EMPTY** over the free real-texture family (U_eL charged-lepton left-rotation + V_DR neutrino-Dirac orientation — the S117 2-5 flat directions), at FIXED S116 input spectra (m_e_vals; Y_nu_diag=[0,4.794,11.928] rank-2 Y1=0; B-branch M_R=[1.0044,1.0786,1.1700]).

**Why this gate:** the piecewise S117 W2 results never closed the JOINT question — 2-2 gave R_eps23=113.564 OUT (shared-εLX); 2-5 gave the U_eL flat direction; 2-3 scanned M_R at fixed U_eL. None scanned {R ∧ 3 angles} jointly over the free (U_eL,V_DR) orbit. This gate does, and confirms atlas-08 Q18b ("mixing under-determined both sectors") extends to the joint (R+angle) box.

**How it lands:**
- **Analytic witness (PASS anchor):** V_DR=I → M_ν=diag(0, Y2²/B2, Y3²/B3) → R_bare=**31.576** ∈[17,66]; U_eL=U_obs† → U_PMNS=U_obs → 3 angles at NuFIT band centers (0.303/0.572/0.02203). All 4 slots land, all edge-clear (min edge-frac 0.216 ≫ 0.05).
- **MC measure:** f_adm_free=**6.85e-5** (137 hits/2e6 Haar) ≥ floor 5e-6 (13.7× margin); CV 0.35.
- **f_R = 1.0 — STRUCTURAL:** the near-degenerate B-branch M_R (16.5% spread) confines m3/m2≈Y3²/Y2² regardless of V_DR ⇒ R∈[27.25,51.01] ⊂ [17,66] for the WHOLE V_DR orbit. The S96 R<17 shortfall is avoided at the bowtie shape. The whole free orbit is R-admissible; only the narrow sin²θ13 box (width 0.0036) cuts the fraction.
- **Factorization EXACT:** f_adm_free = f_R·f_angle = 6.85e-5 (R⊥angles: U_PMNS=U_eL†U_nuL is Haar for Haar U_eL ⇒ angle-box prob V_DR-independent).
- **Contrast (tension witness):** shared-εLX M_ν locked (recon bit-exact, w23=ε23·Y3) → R_shared=113.564 OUT → f_adm_shared=**0** even though U_eL still reaches the angles. So the **V_DR freedom — not the Majorana scale — is what makes the joint box non-empty**; forcing the shared-εLX texture (removing V_DR) would empty it.
- Cross-checks PASS: R closed-form diff 3.6e-15; m1/m3=0 (rank-2); unitarity 2.6e-16; NuFit central-R anchor dm2_31/dm2_21−1=32.55 (R_bare 3.0% from it, both interior).

**How to apply / caveats (load-bearing):**
- This is a statement about the **SHAPE of the compatible region, not a derived value**. PASS = under-determination SURVIVES the joint box (compatible, NOT predictive).
- **Oscillation-anchored** per [[s100a_md_normalization]] (S100a-MD-NORM INFO PERMANENT): D_K bottom-triple→Y_i map NON-UNIQUE (MAP-A/MAP-B), so R_bare∈band is a spectrum-channel CONSISTENCY with NuFIT, NOT zero-free-parameter. Substrate-FIRST content = seesaw STRUCTURE + bowtie M_R shape + R-is-U_eL-invariant factorization + U_eL/V_DR flatness.
- **CP EXCLUDED:** real O(3) textures → δ_CP∈{0,π} → J=0 (framework standing prediction). The CP/mixing under-determination is the separate §VII.BL / S117-W3-3 question (see [[s117_lepto_pmns_joint_image]]), NOT this gate.
- Pairs the corollary of [[s116_pmns_rescue]] (lepton shape leg WALLED-as-under-determined) and [[s117_quark_ckm_underdetermination]] (quark V_us under-determined): both sectors' mixing under-determined; this gate adds that the lepton under-determination is observationally COMPATIBLE with the full NuFIT joint box. Distinct from [[s117_seesaw_resonance_wall]] (θ12 M_R-invariant at fixed U_eL).

Script/data: `computations/session-118/s118_pmns_joint_admissibility.py/.npz/.png`. Verdict: `computations/session-118/s118_gate_verdicts.txt`.
