---
name: s116-lepton-pmns-texture
description: S116-W2 FAIL — external-eps_LX lepton PMNS texture walled (mix_grp=0/4); masses do NOT fix mixing (U_eL free); J=0 from delta_CP in {0,pi}
metadata:
  type: project
---

S116-W2-LEPTON-PMNS-TEXTURE: **FAIL** (mix_grp=0/4, Track B walled). The first external-ε_LX lepton PMNS compute — lepton analog of the quark S111-CF-YUK-FULLFLAVOR. Canonical record: verdict line `computations/session-116/s116_gate_verdicts.txt` (audit f7190f1944db146a…) + `s116_lepton_pmns_texture.npz`. This file is the agent-private constraint reading; the npz/verdict are authoritative.

**Construction**: U_PMNS = U_eL^† U_νL. M_e = diag(exp(−S0·C2)) on ascending-gen tower [(3,0),(1,1),(1,0)] (C2=[6,3,4/3], S0=1.7353 lepton-fixed) + minimal-norm REAL ε_LX off-diag fit to m_μ/m_e, m_τ/m_μ. M_ν type-I seesaw, M_R=[1.0044,1.0786,1.1700] B-branch fold energies (INTERNAL per S100a, scale HELD), M_D rank-2 (Y₁=0 ⇒ m₁=0 preserved), ε_LX in 2-3 block only. Neutrino tower [(0,0),(1,0),(1,1)] is DISJOINT from the charged-lepton tower — that disjointness IS the ℂ⊕ℍ sector-asymmetry.

**What it constrains (3 robust results):**
1. **θ₁₂ OVERSHOOTS** (sin²θ₁₂=0.996 vs obs 0.303). The Casimir tower gives m_τ/m_μ=18.0 but PDG=16.82 (<18); level-repulsion only *raises* that ratio, so fitting the masses *forces* a rearranging off-diag (‖ε_LX‖=0.036) → near-maximal solar mixing. Lepton analog of the quark V_us=0.3107 overshoot — the **same mass-vs-mixing tension** walls both sectors. θ₂₃=0.059, θ₁₃=0.0087 undershoot.
2. **J_PMNS = 0 EXACTLY** — framework forces δ_CP ∈ {0,π} (canonical `delta_CP_PMNS_substrate=0.0`) ⇒ real textures ⇒ NO leptonic CP. Hard falsifiable prediction. J=0 ↔ δ_CP=180° IS within NuFIT 5.2 NO 3σ [108°,404°], so CP-conserving-CONSISTENT (below the |J| magnitude band, which assumes near-maximal δ). The J channel UNDERSHOOTS (opposite of the quark overshoot); the tension shows up in the *angle* (θ₁₂), the CP-forcing zeroes J.
3. **Masses do NOT fix the mixing (the deepest point).** For any orthogonal R, M_e=R·diag(masses)·Rᵀ reproduces the masses ⇒ U_eL is FREE ⇒ the PMNS is **not predicted** by the ε_LX texture constrained on masses alone. The observed PMNS is EXACTLY reachable at 1.53× the minimal ‖ε_LX‖ (U_eL_match construction) — a **SOFT** under-determination wall, not a hard structural exclusion. (Corollary: the S111 quark "V_us prediction" was a multistart tie-break artifact within the same free family.)

**Forced-circulant contrast** (in-artifact, never tuned): S115 J=1/(6√3)=0.0962250 recovered (2.93× above J_obs, washed-out tri-maximal) vs ε_LX J=0. Both miss — circulant from above, ε_LX from below.

**Updates the open PMNS question** [[s96_intersector_pmns]] / [[s52_offjensen_pmns]]: the external-ε_LX route (the Level-4/Level-5 escape) is now tested for the FULL lepton PMNS and does NOT rescue — it produces θ₁₂ overshoot + J=0. The Level-5 θ₁₂/θ₂₃ wall is re-confirmed from the texture side. dual_prior → 0.8 Track B (lepton walled, consistent with §VII.CK/§VII.BL multiplicity-scalar theorem extending to leptons). 3-tuple sign=PASS (J=0 matches δ_CP∈{0,π}) / mag=FAIL / regime=VALID. Pairs with the W2-2 rescue-vs-wall workshop ([[s116_pmns_rescue]] — LANDED: Track B WALLED-AS-UNDER-DETERMINED; seesaw metric real+quark-inaccessible but sufficiency-FAILED at near-deg B-branch M_R; both sectors under-determined). Seesaw structure from [[s100a_md_normalization]].
