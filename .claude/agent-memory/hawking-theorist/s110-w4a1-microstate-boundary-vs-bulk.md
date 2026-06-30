---
name: s110-w4a1-microstate-boundary-vs-bulk
description: S110 W4a-1 — A/4 microstate origin is boundary-localized not bulk; single-sided edge count is factor-1.9 short (S/(A/4)=0.526); two-sided island construction is the surviving corridor
metadata:
  type: project
---

S110-CF-B5A-MICROSTATE (gate I ran, FAIL-but-informative). The microstate origin of the Bekenstein-Hawking A/4 on the white-hole exit screen.

**Result (substrate-physics walls, permanent):**
- Bulk GGE conserved-charge count (inv-4 W1-1 Page curve): S_micro = 24.82 nats, **2.856 OOM undercount** of A/4 = 17806.57. Bulk excitation entropy is NOT the horizon entropy (Strominger-Vafa-style; the relic's bulk Gibbs entropy ≈ few bits).
- Boundary edge-mode count (this gate): S_boundary = 9372, **0.279 OOM** from A/4 — beats the bulk by ~2.6 orders. Microstate origin is **decisively boundary-localized** (holographic / 't Hooft-Susskind / Carlip-Strominger near-horizon edge modes, but DERIVED: entropy IS the edge-mode count, area IS the a₂ second moment).
- But **S_boundary/(A/4) = 0.526 ≈ 1/2** — factor-1.9 short of the equality. test_ratio = 0.474 > info_band 0.25 ⇒ literal equality FAILs.

**Surviving corridor:** two-sided / island boundary construction. The near-1/2 ratio = counting ONE screen orientation / ONE Bogoliubov partner of the entangled pair; full horizon entropy is the two-sided sum. Carry-forward = deeper island construction (two-sided edge-mode sum). The 1/4 NORMALIZATION (inv-4 W1-2 a₂-conical c_conical=0.25000, |R−1|=5e-7) is SECURED and untouched — only the COUNT is short.

**Why:** this is the Page-curve / island-formula microstate question in my home domain. Two corridors now excluded as the EXACT origin (bulk-charge; single-sided boundary). Re-usable on any future island/replica/Page gate.

**How to apply:** if dispatched on the two-sided island follow-up, the single-sided count is already done (9372 at λ_exit=2.4893); the target is the factor ~2. Do NOT re-derive the single-sided count and re-discover the factor of 2. λ_exit was fixed from substrate geometry (τ_exit/τ_fold × a2_fold/a0_fold = 0.363 of the spectral support [0.8197, 5.4189]), NOT fitted to A/4 — keep that anchoring (it's what makes the equality a genuine prediction). Method script: `computations/session-110/s110_cf_b5a_microstate.py`. Prior S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT is a DIFFERENT observable (astrophysical-mass-windowed HSS count, not the exit-slice boundary count) — don't conflate.

Links: bulk/boundary distinction is the substrate Page-curve analog [[see MEMORY.md Page-curve check]]. Convention pin RATIO-BLOCKSUM (Counting axis: extensive degeneracy count, not intensive state evaluation).
