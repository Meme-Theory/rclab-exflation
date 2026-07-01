---
name: s117-quark-ckm-underdetermination
description: S117-W2-4 PASS — quark V_us under-determined (masses fix singular VALUES not left VECTORS); 0.3107 a multistart artifact; PDG reachable at 1.559x min eps_LX (quark analog of lepton 1.53x)
metadata:
  type: project
---

**CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM: PASS** (under-determination CONFIRMED). Canonical record: verdict line `computations/session-117/s117_gate_verdicts.txt` (audit `0a964704…c678b0`) + `s117_quark_ckm_underdetermination.npz` + WP §W2-4 `sessions/session-117/session-117-w2-workingpaper.md`. This file is my agent-private reusable reading; the npz/verdict/WP are authoritative.

**The claim, confirmed.** The S116-W2-PMNS-RESCUE COROLLARY (both sectors' mixing under-determined) is now QUANTIFIED for quarks. Masses fix singular VALUES (the quark mass spectrum), NOT left singular VECTORS (U_dL). At FIXED quark masses V_us = |(U_uL†U_dL)[1,2]| spans an interval; S111 V_us=0.3107 was ONE point selected by a multistart tie-break (least_squares start/path), NOT a forced derivation.

**Numbers (random_seed=117):** Reconstructed V_us=0.310739 = S111 V_us_fw exactly (texture: Casimir-tower diag exp(−S0·C2), S0=1.7353, C2=[4/3,3,6] + off-diag eps_LX {w12,rho13·|w12|·e^{iθ},rho23·|w12|·e^{iθ}}; down {rho13d=0.595,rho23d=0.181,|w12d|=0.0238,θ_d=1.180}).
- **(B) texture-admissible** (the framework-faithful test — down masses held EXACTLY fixed, 257 fits on mass surface rel-resid 8.4e-11, U_up fixed): V_us ∈ **[0.053, 0.986] width 0.933**. PDG 0.225 INSIDE (margin ~0.17); S111 0.3107 INSIDE. Under-determination genuine WITHIN the substrate ansatz, not just generic O(3).
- **(A) full-O(3) analytic bound:** both-free [0.0002,0.9999] width ~1.0; U_dL-only-free [0.0099,0.9686]. Masses never pin left vectors (true for any model — the limiting statement).
- **Seed-INDEPENDENCE (the signature):** width across 10 seed batches mean 0.998, std 1.48e-3, **CV=1.48e-3**. The INTERVAL is geometric/seed-independent; the SINGLE multistart value is seed-DEPENDENT (= the 0.3107 artifact).
- **(C) minimal ‖ε_LX‖ to PDG (quark analog of lepton 1.53×):** min-‖ε_LX‖=1.80e-2 texture gives V_us=0.944 (near-maximal — minimal-norm down texture is near-maximally misaligned with fixed up). Targeted mass-preserving fit reaches V_us=0.225000 EXACTLY (dv=0, mass rel-resid 6.9e-15) at ‖ε_LX‖=2.81e-2 = **1.559× min** = non-minimal. Lepton was 1.53× (S116). Clean symmetric confirmation.

**Verdict-logic note (for future re-use):** first run gave INFO from MY bug — I gated PASS on a discrete random sample landing within σ of 0.225 (sampling-resolution artifact) instead of the pre-registered MEMBERSHIP operator (PDG ∈ [V_min,V_max]) on a CONTINUOUS interval. Fix: implement the pre-registered operator + EXHIBIT the PDG-reaching texture by targeted optimization (existence, not lucky sample). NOT iterate-until-PASS — the criterion was met, my sampling was too coarse to show it. Caught + fixed BEFORE emit_verdict.

**Cross-reading reconciliation (high-order).** This reconciles the two prior quark-CKM readings — S111 over-rotation (0.3107, 38% high) and the earlier knowledge-MCP open_channel "quark-CKM FALSIFIED ~3124× ⇒ both quark chiralities share M₃(ℂ) ⇒ U_mix→identity (zero mixing)" — as TWO POINTS ON THE SAME under-determined free orbit (V_us spans ~[0,1]). Neither is "the" prediction.

**COROLLARY (with §W2-5, lizzi PASS=flat).** BOTH quark (U_dL, this gate) and lepton (U_eL, §W2-5 — flat direction of S=Tr f(D_K/Λ), ΔS/S=3.2e-15) left-rotations under-determined; NEITHER mixing matrix derived. Substrate supplies the mass spectrum (+ for leptons the M_R ruler) but NOT the mixing seed. dual_prior PASS→0.9 Track_A; cuts the connes ~0.55 V_us-overshoot base-rate to one selected point in a free family. Pairs with [[s116_pmns_rescue]] (the corollary's origin) + [[s116_lepton_pmns_texture]] (lepton θ12 overshoot = same mass-vs-mixing tension). V_us_PDG=0.225 canonical (S100a; plan-prose "0.2243"=0.225−σ, membership target-insensitive).
