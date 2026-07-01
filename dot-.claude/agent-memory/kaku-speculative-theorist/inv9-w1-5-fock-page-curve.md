---
name: inv9-w1-5-fock-page-curve
description: INV9-W1-5 verdict — GGE Fock trace is FINITE (no integral Dg, CONFIRMED) but produces NO Page-curve turnover (REFUTED); Ordered-Veil unitarity forbids the irreversibility a Page curve needs
metadata:
  type: project
---

INV9-W1-5-GGE-FOCK-PAGE-CURVE (investigation-9, my B-5 hidden-Fock-sum thesis): **FAIL** (sign=FAIL/mag=INFO/regime=MARGINAL), audit_sha256 `e386dc457bf8720c2b43575f55fabde735dfa95beb06fc55bd07e785a46eeafc`.

**The thesis SPLITS into two claims:**
- **Thesis-1 (CONFIRMED)**: the substrate's "sum over geometries" IS a finite Fock trace `Z = Tr_Fock e^{−βH_BdG}` over `F(H_BdG)=⊕_{n=0}^{8}∧ⁿH_BdG` (dim 2^8=256, the dominant-B2 truncation of S64's n=64), NOT `∫Dg`. Cross-checked vs free-fermion product `Π_k(1+e^{−βλ_k})` to 7.7e-16. There IS a well-defined sum, no path integral, no UV divergence.
- **Thesis-2 (REFUTED)**: that finite trace does NOT produce a Page-curve turnover. Pure quench (S_EE(0)=0): interior max 0.750 nat @ t*=16.7 but `recurs_to_peak=True` (oscillation period T_osc≈5-20, recurs forever; PR=1.93, only 2 significant eigenstates → near-two-level). Mixed GGE (canonical relic, purity 0.149): S_EE(0)=2.169 is ALREADY the global max (94.5% of Page value 2.273), only ±0.07 ripple — no rise, no turnover.

**Why (the structural reason — the durable finding):** A Page curve requires an IRREVERSIBLE information-restoring process (string: replica-wormhole saddle dominating at late times). The substrate's Ordered Veil (R_therm=5252, λ_L=0, no scrambling, no thermalization on-timescale) makes the GGE relic's evolution UNITARY and QUASI-PERIODIC — it recurs (Poincaré), it does not irreversibly restore. This is the [[s64-phonon-strings-investigation]] finding made operational: a finite-dim unitary matrix model has recurrences and CANNOT exhibit a true Page curve without explicit coarse-graining the substrate's own dynamics does not supply.

**How to apply:** ANTI-CORRESPONDENCE candidate — "string replica-wormhole Page curve ↛ substrate finite-Fock-trace dynamics" (the trace exists, but it is STATIC/REVERSIBLE where the Page curve needs DYNAMICAL/IRREVERSIBLE). Sharpens the W3-1 kaku↔string adjudication: do NOT claim "substrate lacks a sum" (it has one); the precise gap is static-trace-vs-dynamical-irreversible-process. Corridor still OPEN (regime=MARGINAL): a much larger Fock truncation (PR≫1, genuine many-body level density) could show a secular envelope decline under recurrences — forward gate. Session-promotion blocker: n_pairs=59.8 has NO canonical_constants PROVENANCE entry (add via update_constant S38 source before any §VII Page-curve-analog landing). Cross-check anchor: S40 PAGE-40 (18.5%-of-Page) is the same sub-Page-saturation family. Links: [[s64-collab-review]].
