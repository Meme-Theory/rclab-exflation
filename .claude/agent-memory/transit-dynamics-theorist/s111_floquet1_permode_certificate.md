---
name: s111-floquet1-permode-certificate
description: S111-CF-FLOQUET1 per-mode Floquet band-stability certificate at the most-at-risk relic mode; two-layer plan-text drift resolution on the inv-12 W3-2 npz
metadata:
  type: project
---

# S111-CF-FLOQUET1 — per-mode Floquet certificate (Wave 5, PASS, [VERIFY], audit_sha256=6d7e123d88e43eac…)

The aggregate `max|Tr M|_relic < 2` bound (INV12-W3-2, the §VII.BP H-PARITY-DRIVE-EXCLUSION DEAD pin) is now a **per-mode** certificate at the single most-at-risk relic mode. PASS, NON-verdict-gating (strengthens §VII.BP DEAD aggregate→per-mode, does not change it; §VII.BP is STAGE-3 PROVEN, audit `08f32885`, pinned 3 independent ways).

**Most-at-risk mode** (npz `i_closest = 1168`): A_relic = 9.0003712119 (nearest the **n=3** Mathieu zone a=9, dist 3.71e-4), `Tr M = −1.9999999624`, `|Tr M| = 1.9999999624 < 2` (gap-to-edge **3.76e-8** — the TIGHTEST band margin across all 1248 relic modes), `Re μ = 0` EXACT ⇒ NO re-pumping. resonance mask False. Floquet law `Re μ=0 ⟺ |Tr M|≤2` self-consistent; aggregate `max|Tr M| = 1.99999996` reproduces the survey verdict; `n_resonance = 0/1248`, `fraction_resonance = 0`.

**KEY STRUCTURAL FINDING — TWO-LAYER plan-text drift** (resolved per `substrate-first-canonical-sourcing.md §(ii.B)`: verify ARRAY CONTENT, not byte-SHA):
- **Drift-1** (plan's own DRIFT NOTE caught this): context spec `+1.98756` ≠ npz ground truth `−1.9999999624` (sign AND value). Pin to npz; `|Tr M|<2` band-membership is the load-bearing certificate; `+1.98756` NOT used as threshold.
- **Drift-2** (NEW, the gate's own finding): the plan's substitution chain defines most-at-risk as `i_closest := argmin|A_relic−1|` (= index 4, A=0.965, near n=1 zone) BUT the npz STORES `i_closest = 1168` = `argmax|Tr M|` = `argmin(dist_to_zone_A)` (the A=9.0003 n=3-zone mode). These are DIFFERENT modes. The gate's HYPOTHESIS says "the single **most-at-risk** relic mode" = tightest band margin = `argmax|Tr M|` = the npz value — MORE rigorous than the `argmin|A−1|` proxy (the proxy assumed the near-a=1 n=1 zone is widest ∝ q_M^1, but the realized relic grid puts the tightest margin at the n=3 zone, gap 3.76e-8 vs the A=0.965 mode's 3.04e-3). Read the npz `i_closest`; report `argmin|A−1|` mode as cross-check (i=4, |Tr M|=1.99696<2). **Both modes pass; verdict robust to definition; only the certificate's mode-identity tightens.**

**Lesson for future Floquet-survey reads**: the npz-stored `i_closest` in inv-12 W3-2 is `argmax|Tr M|` (most-at-risk-by-band-margin), NOT `argmin|A−1|`. When a plan quotes a "most-at-risk mode" by a proxy (near-a=1, widest-zone heuristic), CHECK whether the realized relic grid's tightest margin actually lands there — for this relic spectrum it lands at the n=3 zone (a mode 3.71e-4 from a=9), not n=1. The hypothesis word "most-at-risk" is unambiguous (tightest margin) and overrides the proxy. See [[s101_w5_2_ladder_composition_results]] (s64 clock ≠ fold-clock — same class of "the stored quantity is not what the plain-language label assumes").

Artifacts: `computations/session-111/s111_cf_floquet1_permode_monodromy.py/.npz/.png`. Mathieu/Hill normalization `v'' + [A − 2 q_M cos(2t)] v = 0`; `Re μ > 0 ⟺ |Tr M| > 2` (parametric amplification onset); h_par=8.3e-4, q_M(A)=A·h_par/2 (narrow-regime). Ordered Veil S_ent=0, R_therm=5251.82.
