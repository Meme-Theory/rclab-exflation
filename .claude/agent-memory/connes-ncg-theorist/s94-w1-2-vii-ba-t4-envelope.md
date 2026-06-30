---
name: S94 W1-2 VII.BA T4 envelope extension — T5-SOLE sharpening
description: T4|s≠s'=Res_W(s)/Res_W(s') deg+2 differential-SUM-growth DIVERGES via Friedrich-Bar tail to L=100; L3>L2 persists; FAIL the L3<L2 test ⇒ T5 SOLE registry-PASS-eligible Element-3 for §VII.BA
type: project
---

## Verdict: FAIL (composite, S87+ schema-v2 [SIGN] gate)

- gate_id: `S94-VII-BA-T4-ENVELOPE-EXTENSION`
- audit_sha256: `a74e9f1ef2d42610e98c319811ab88ec4058913b254f59279c5bd1d223dfaa67`
- content_sha256: `f05c819ceedef2adfd7596cc3ae3ca9751715f31159a574b71403bc427e55030`
- 3-tuple: sign=PASS, magnitude=FAIL, regime=VALID → composite FAIL
- script: `computations/session-94/s94_w1_2_vii_ba_t4_envelope_extension.py`

## Structural finding (the durable result)

The §VII.BA composite-bridge dimensional-class taxonomy formulation **T4|s≠s' = Res_W(s)/Res_W(s')** (deg = 2(s'−s); s=2,s'=3 ⇒ deg=+2) satisfies BOTH admissibility conjuncts (deg-match + non-scalar) — it is structurally admissible — but its Level-3 anchor NEVER falls below its Level-2 envelope, so it is **NOT registry-PASS-eligible**.

- T4 ratio Res_W(2)/Res_W(3) **DIVERGES monotonically**: 9.82 (L=12) → 323.5 (L=100, power-law tail) / → 487.4 (κ-band). Robust to calibration method.
- Envelope exponent **α = −0.71 NEGATIVE everywhere** ⇒ the sequence is DIVERGENT; the Aitken Φ_∞ is a meaningless artifact (returns negatives for a positive ratio). ΔL = L3−L2 = +0.095 (L=12) → +0.042 mean over [50,100], stays > 0.
- Obstruction: deg-+2 differential SUM-growth — the s=2 numerator moment grows faster than the s=3 denominator in the ratio. The higher pole s=3 is MORE concentrated on small eigenvalues, so new high-level sectors contribute proportionally LESS to Res_W(3) ⇒ ratio keeps growing.

**Consequence**: **T5 (Connes-Karoubi K_0-pairing ⟨[φ],Ch(P_0)⟩, deg 0, L_max-saturated per S93 W1-3) remains the SOLE registry-PASS-eligible Element-3 for §VII.BA.** The admissible set is NOT widened to {T3,T4|s≠s',T5}. T4|s≠s' is admissible-but-not-saturated. This SHARPENS the bridge.

## Method reusables (for future envelope-saturation gates)

- **Res_W(s,L_max) = Σ_k m_k·|λ_k|^{−2s}** over Peter-Weyl sectors p+q≤L_max; each sector (p,q) has 16·dim(p,q) eigenvalues, m_k=dim(p,q). This IS `bare_mellin_moment` (CM-1995 §III.4 unique-trace value on the FINITE triple). Reproduces S84 L=12 cache bit-for-bit.
- **Friedrich-Bär analytic tail** (no raw diagonalization above L=12): per-eigenvalue moment ⟨|λ|^{−2s}⟩(p,q) ~ A_s·C_2(p,q)^{−β_s} calibrated on the 89 nonzero-Casimir cache sectors (r²≈0.99). Empirical band ratio **mean|λ|/√C_2 → 0.595**, min|λ|/√C_2 = η_FB floor = **0.4365 at (1,1)** ≥ η_FB_lower=0.40. NEW-sector p+q=13 worst-bound 3.0022 > bot-8 ceiling 0.8409 ⇒ saturation_pass ⇒ regime VALID.
- SU(3): C_2(p,q)=(p²+pq+q²+3p+3q)/3, dim=(p+1)(q+1)(p+q+2)/2 (from `_cm_1995_residue_formula.py`).
- Envelope construction = S93 W1-3 `level2_envelope_and_level3` (Aitken Δ² 3-pt, step-2 window; L2=C·L^{−α}, L3=|Φ(L)−Φ_∞|).

## Parallel-writer race note

WP edits raced with concurrent wave writers (orchestrator finalizing §W1-1, others on §W1-3/4/5). Edit-tool failed mtime-conditional twice. Fix: parallel-safe Python in-place edit scoped to the §W1-2 slice (anchor-to-next-anchor string replacement + os.replace atomic write), per epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race". Cleaned up temp helpers after.
