---
name: inv9-w1-3-bcs-transmutation
description: INV9-W1-3 verdict — QCD↔BCS dimensional-transmutation analogy holds at UNIT level (Var(δ*)=0 exact) but BREAKS at asymptotic-freedom level (homogeneity Var=1e-2); full Kosmann-BCS HFB gap = 0.316, 32% short of ED canonical 0.464
metadata:
  type: project
---

INV9-W1-3-BCS-DIMENSIONAL-TRANSMUTATION (investigation-9, kaku) — composite **FAIL**, [SIGN] 3-tuple **sign=PASS, magnitude=FAIL, regime=VALID**. audit_sha256 `e59f0ba999fdbe6a…`.

**The decisive reframe (query-first surfaced it)**: the gate's premise assumed a scale-free *inter-sector* Kosmann coupling. PA-2 (S22b, STRUCTURAL CLOSURE) proves the inter-sector `<n|K_a|m>` between distinct Peter-Weyl (p,q) sectors of D_K is EXACTLY ZERO (re-verified: `max|coupling|=0.0e+00` over all 54 blocks; `K_norm=2.78e-17` at fold). What survives is the BLOCK-DIAGONAL Ltilde coupling (`K_Ltilde=0.152~τ`). So the genuine OPEN-P1 gap kernel is the WITHIN-sector 8-mode BdG pairing `V_bare` (S52/S53), NOT a dense inter-sector matrix. This run supersedes the S23a constant-coupling closure with the full 8×8 V_bare.

**Cross-domain bridge — REGIME OF VALIDITY (the durable Kaku finding)**: the QCD↔BCS dimensional-transmutation analogy (Λ_QCD from b₀g² ↔ Δ_BCS from Kosmann coupling on van-Hove DOS) splits into two levels:
- **UNIT level — HOLDS EXACTLY**: the gap equation `δ=½V·(δ/√(ε̃²+δ²))` has M_KK nowhere on the RHS. Perturbing M_KK→λM_KK leaves δ* bit-identical: `Var_λ(δ*)=0.0e+00`. M_KK IS the unit, not a parameter. This is genuine dimensional transmutation and SUPPORTS §VII.BS rank-1 NNU (`O=w·Ô`, w=M_KK) from the BCS-gap channel.
- **ASYMPTOTIC-FREEDOM level — BREAKS**: rescaling the dimensionless spacing `(ε−μ)→f(ε−μ)` gives `Var(δ*/f)=1.04e-2 ≠ 0`. The finite spectrum + fixed-magnitude V breaks exact homogeneity degree-1 (true asymptotically-free QCD rescales Λ with μ exactly). The substrate's finite spectrum is NOT a continuum RG flow.
- **Sharp boundary**: the analogy = dimensional-transmutation-AS-UNIT-FIXING, NOT -AS-ASYMPTOTIC-FREEDOM.

**Magnitude FAIL (closes a corridor)**: full-matrix mean-field gap `max|Δ|=0.1565 M_KK` — SAME as the S23a shortfall (`M_max 0.077–0.149`); the full matrix elements do NOT rescue the gap. Beyond-mean-field HFB correction = S53 ED/BCS factors {2.02,1.71,1.59}; best (N_pair=2): `δ_HFB=0.3155`, residual **32.0%** vs ED canonical 0.4643. ALL factor/gap-definition variants land FAIL (32–46%) → structurally stable, not knife-edge. The canonical 0.464 is a 256-state EXACT-DIAGONALIZATION correlation quantity the 8-mode HFB truncation under-captures; the 0.464-vs-0.156 gap re-localizes onto the **Fock-space-truncation axis** (forward gate: 256-state ED-matched HFB).

Links: [[s64-collab-review]] (spectral-moment decoupling — same finite-matrix-model substrate), [[s64-phonon-strings-investigation]] (substrate is IKKT-adjacent finite matrix model — the homogeneity break is the finite-model fingerprint, the same reason there is no Hagedorn / no continuum-RG limit). Correspondence-registry candidate: a new "QCD-transmutation ↔ BCS-gap" entry, GENUINE at unit-level / STRUCTURAL-only at asymptotic-freedom-level (regime-split entry).
