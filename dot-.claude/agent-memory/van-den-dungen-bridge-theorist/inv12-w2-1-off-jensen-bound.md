---
name: inv12-w2-1-off-jensen-bound
description: INV12-W2-1 PASS — off-Jensen S_cross/S_base bound + the fiber-internal-vs-base-fiber O'Neill convention bug it caught
metadata:
  type: project
---

**INV12-W2-1-S-CROSS-OFF-JENSEN-BOUND (investigation 12, W2): PASS.** Off-Jensen spectral-action cross-term `|S_cross|/S_base = 3.873e-04` at the ridge-confined moduli displacement δ=0.05 (S76 W2-J), 25.8× below the 1e-2 threshold. `c_geom = ratio/δ² = 0.1549 < 4.0` (threshold-crossing, Sage-QQ exact). On-Jensen δ→0 recovery: `|S_cross|/S_base → 0` to machine ε (A-TENSOR-61 recovered by construction). [SIGN] 3-tuple sign=PASS/magnitude=PASS/regime=VALID. audit_sha256 `538981c193503f8e2683fb1a102b1dc7658beb841e2c66133508f272743e16db`. Discharges the on-Jensen-only conditional (U-1) for the **moduli direction** of the a₂→G_N additive Kasparov factorization.

**CONVENTION BUG CAUGHT (the load-bearing lesson)** — the O'Neill A,T tensors of the submersion π: M⁴×SU(3) → M⁴ live in the **BASE-FIBER off-block** structure (g_{μa}, μ base, a fiber), NOT in the fiber-INTERNAL (u1/su2/C²) sector structure.

**Why:** my first cut measured cross-SECTOR fiber frame structure constants ft[a,b,c] (su(2)/C²/u(1) mixing) as the A-tensor. WRONG — su(3) is simple, so its Lie bracket is NEVER block-diagonal in (u1,su2,C²): C² brackets close back into su(2)⊕u(1) (e.g. [λ₄,λ₅]~λ₃+√3λ₈). Cross-sector fiber structure constants are nonzero even for the PURE product Jensen metric (intrinsic to su(3), unrelated to any base-fiber split). That gave `||A||²(Jensen)=0.367 ≠ 0`, FAILING to recover A-TENSOR-61 — a measurement artifact, NOT a result.

**How to apply:** the CORRECT O'Neill A,T are sourced by the **Ehresmann connection** A_μ^a (base-fiber off-block): A_{μν}^a = ½ F_{μν}^a (non-abelian curvature F=A_μ^b A_ν^c f^a_{bc}); T = fiber 2nd fundamental form (base-derivative of the fiber metric, the τ→τ(x) modulus-field gradient). On the Jensen line A_μ^a=0 → A=T=0 EXACT BY CONSTRUCTION (recovers A-TENSOR-61). The A-tensor channel needs TWO genuinely NON-COMMUTING base profiles (su(2)+u(1) vs C²) — the equal-weight off-block profile is uniform and self-commuting (a measure-zero A=0 slice giving ||F||²~1e-34). See [[reference_van-den-dungen-bridge]].

**Scope distinction (flagged, NOT conflated):** S96-W1-ONEILL-NONFLAT (s96_w1_oneill_nonflat.py) computed the SAME Gilkey machinery but parameterized the off-Jensen knob by the principal-bundle **connection curvature** ||F_ω|| (base-bundling channel, Reading A=Hubble scale, INFO). INV12-W2-1 parameterizes it by the **35D moduli displacement** δ within the Jensen ridge (PASS at <1e-2). Complementary channels — together they saturate the off-Jensen O'Neill content (fabric deforms off-ridge AND SU(3) bundle non-flat); a₂ additivity holds to a small quantified leak in BOTH.

**Substitution chain (Sage-confirmed):** `|S_cross|/S_base = (|A|²+|T|²)/|R_K|` (the (1/6) heat-kernel coeff + fiber-vol factors cancel against S_base's own (1/6)R_K structure; via Baptista Paper 13 eq 3.4 R_P=R_M+R_K−|A|²−|T|²). Computed |A|²=3.22e-7, |T|²=7.81e-4, R_K(off-Jensen)=−2.0181. δ²=1/400 EXACT; threshold-crossing c_geom = 1e-2/2.5e-3 = 4.0 EXACT.

**Plan-text drift fixed:** the plan input_files named `computations/_shared/s84_spectrum_cache_L12_tau019.npz` but the canonical cache is at `computations/session-84/` (the path s96_w1_oneill_nonflat.py:164 loads). Corrected at runtime per substrate-first-canonical-sourcing.md §(ii.B).
