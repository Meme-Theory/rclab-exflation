---
name: s110-cv2b-gauge-a4-fork
description: S110 CV2B Question-B M_KK fork — gauge-a4 channel does NOT independently fix M_KK (Fork-C FAIL, ONE-ROUTE-DOMINATES); dimensionless-vs-dimensionful keystone-lever structural reason
metadata:
  type: project
---

S110-CF-CV2B-GAUGE-A4 (W3-1, FAIL=Fork-C, audit_sha256 `07aa755a7e4648c578dd2c8dbe1ef0a435a34da9ed8ae95a99970b1edcd19126`). The Question-B M_KK canonical-VALUE discriminator (orthogonal to CV2A=Question-A derivation-in-principle). Verdict: the Yang-Mills gauge a_4 channel does **NOT** independently fix the keystone weight M_KK; gravity-a_2 remains the sole canonical (ONE-ROUTE-DOMINATES).

**The structural reason (REUSABLE):** the gauge a_4 (Tr F^2) channel is **dimensionless** (Yang-Mills is classically scale-invariant) ⇒ `1/g²_sub = a_4/(8π³·f₀)` is μ-INDEPENDENT (a horizontal line in ln μ); it has **no power-law lever on M_KK**. Contrast the gravity a_2 channel, which fixes M_KK via the **dimensionful** Sakharov law `M_Pl² = f₂·M_KK²·a₂` (power law in M_KK ⇒ a unique root TAUTOLOGICALLY at M_KK_gravity — the inv-6 W2-1 `root_count=1`, `M_root=M_KK_gravity` is by construction, NOT the gauge channel). A dimensionless spectral moment cannot pin a dimensionful weight. This is the spectral-geometry confirmation of the rank-1 §VII.BS NNU wall (only ratios Ô derivable; w=M_KK is one irreducible external import) and the PROVEN inner-fluctuation-impotence theorem (every A_K-built form is multiplicity-scalar).

**Two Fork-C triggers BOTH fired:**
1. No root in [1e15,1e18] GeV: μ* = 4.422e13 GeV (1680× below M_KK_gravity=7.4287e16). Root from `μ* = m_Z·exp((1/g²_mZ − 1/g²_sub)·4π²/b₃)`.
2. Cross-scheme spread = 167.1 OOM ≫ 1 OOM. Three CC normalizations of `1/g²_sub`: `a_4/(8π³f₀)`→μ*=4.42e13 (PRIMARY, =5.4454); `a_4/(2π²)`→8.15e167 (=68.43); `2f₀/π²`→6.4 GeV (=0.2026). The f₀/f₄ Mellin-moment normalization is unfixed ⇒ no scheme-invariant gauge prediction.

**Substrate vs SM-RG (the well-posed-fork lemma):** `1/g²_sub` const in ln μ; SM one-loop `1/g₃²(μ)=1/g₃²(m_Z)−(b₃/4π²)ln(μ/m_Z)` (GUT-norm g²=4πα, b₃=−7) monotone-increasing ⇒ Δ(μ) strictly monotone-decreasing ⇒ AT MOST ONE root (sign_changes_in_window=0). SM coupling is logarithmically FLAT: 1/g₃²(m_Z)=0.6744 → 1/g₃²(M_grav)=6.7622 → 1/g₃²(M_kern)=7.1017 across 15 decades.

**Normalization provenance (load-bearing for re-derivation):**
- CC (S76 W2-B, Paper 19 eq before 2.15): `1/g_YM² = f₄·a_4/(2π²)`, unification `f₄·g₀²/(12π²)=1`.
- Framework SU(3)_c summand form (S70 line 28, `s70_f0_alpha_s.py`): `α₃(tree)=2π²·f₀/a_4` ⇔ `1/g₃²=a_4/(8π³·f₀)`. S70 found α_s tops at 0.0261 (tree) / 0.0134 (KK threshold S_inf=2.895), factor ~5.4× below observed 0.118 — α_s tension is STRUCTURAL.
- inputs: a_4_FW_zeta=1350.7216 (regulator a_4^{ζ}, poleconv-A-double pole_in_s=2 grade_n=4); a_2_FW_zeta=2776.165389; f_0_sharp=1.0; alpha_s_MZ_obs=0.118; M_Z=91.1876.
- inv-6 W2-1 cross-anchor: file is `inv6_w2_1_gamma_tau_oneloop_trajectory.npz` (plan path `inv6_w2_1.npz` is drift); key `lambda_induced_fold==a_4_FW_zeta` bit-for-bit (a_4 one-loop Γ=−½ζ'_D(0) == zeta-SDW a_4).
- L12 cache real path = `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (plan `_shared/` path is a doc bug, confirms MEMORY.md note); 90 sectors, max_pq_level=12, a_4 Friedrich-Bär saturated.

dual_prior posterior: Fork-C ⇒ 0.9 to Track B (priors were A=0.45/B=0.55 → A≈0.10/B≈0.90). fb_pair backward: atlas-04 M_KK cell + §VII.BS support-row MUST NOT up-tag M_KK to "derived"; canonical stays gravity-a_2 frozen-since-S42.
