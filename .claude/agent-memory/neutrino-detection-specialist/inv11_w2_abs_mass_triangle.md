---
name: inv11-w2-abs-mass-triangle
description: INV11-W2-2 absolute-mass triangle INFO — one S99-W3 triple lands in all 3 direct-mass detector windows; PMNS PDG-vs-NuFit6.0 version-disambiguation; m_beta~0.009 eV non-detection
metadata:
  type: project
---

INV11-W2-2-ABS-MASS-TRIANGLE closed **INFO** (investigation track, `inv11_gate_verdicts.txt:32`; audit `5f4aa7b143950b17...`). Three-channel absolute-mass triangle from ONE oscillation-anchored S99-W3 light triple m_ν=[0, 0.0086776, 0.0495278] eV (NO; m₁=0 EXACT, Casimir C₂(0,0)=0; δ_CP∈{0,π} J-forced).

Results (PDG PMNS primary — see disambiguation below):
- **Σm_ν** = 0.0582053272 eV — reldiff vs `Sigma_mnu_FW` = 8.3e-10; 19.2% below DESI `Sigma_mnu_bound_DESI_2024`=0.072 (Row #77). PASS-direction.
- **m_β** = √(Σ|U_ei|²m_i²) = **8.751 meV ≈ 0.00875 eV** — kinematic NON-DETECTION: ×34.3 below KATRIN final (~0.3 eV), ×4.6 below Project-8 target (~0.04 eV). The publishable forward number. (No canonical pin existed; this gate produced it. m_β has NO canonical_constants entry as of INV11.)
- **m_ββ** = |Σ U_ei² m_i| band **[1.516, 3.695] meV**, central 3.695013 meV — reproduces canonical `m_bb_FW`=0.0036950128 eV (Row #80, S100a) to **reldiff 0.0e+00**. Below LEGEND-200 (×20.3) and next-gen 10 meV floor.

**Why INFO not PASS** (pre-registered marginal-edge outcome): the m_ββ central IS the no-cancellation upper funnel edge by construction (Row #80), so it lands ON the band's upper edge, not strictly interior → fires the marginal flag → plan §W2-2 INFO_meaning ("straddles an edge"). NOT a failure — triangle closes (all 3 reproduce from one triple). A first run FAILed on a literal `≤` against the rounded 3.695 by +3.5e-6 rel — a **Class-8.3 publication-precision-floor artifact** (`m_bb_FW` published 4 sf); fixed in-script by widening the band-membership edges by `rel_tol=1e-4` per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"` item 2. Operator-precision fix, NOT iterate-until-PASS.

**REUSABLE PMNS version-disambiguation (canonical-sourcing, S101 PAIR-OF-PAIRS)**: `canonical_constants.py:699-702` records that the pair Row #80 / `m_bb_FW` ACTUALLY CONSUMED is `sin2_theta12_PDG=0.307`, `sin2_theta13_PDG=0.0220` (de-facto NuFit-5.x/PDG) — the plan's "NuFit-6.0" label is a MISLABEL. The TRUE NuFit-6.0 pair is `sin2_theta12_NuFit60=0.303`, `sin2_theta13_NuFit60=0.02225`. PDG→NuFit6.0 shifts m_ββ central by **−0.60%** (DECISION-IRRELEVANT; both inside NO funnel [1.5,4.5] meV). **For any future neutrino flavor/0νββ/m_β gate: pin PDG as PRIMARY to reproduce the canonical Row #80 anchor; carry NuFit-6.0 as diagnostic.** Per `substrate-first-canonical-sourcing.md §(iv)` — canonical anchor beats plan prose.

m₁=0 (rank-deficient lightest) keeps the m_ββ lower edge **finite** (1.516 meV, not 0) — forbids the deep-cancellation 0νββ null a non-zero-lightest model permits. Non-vanishing 0νββ is itself a substrate prediction in this (NO, m₁=0, Majorana) config. Absolute-scale caveat: irreducibly oscillation-anchored (`S100a-MD-NORMALIZATION` INFO, track_B 0.9, PERMANENT) — m_β and m_ββ are forward predictions CONDITIONAL on measured Δm² + structural inputs, NOT zero-free-parameter. Strength = cross-channel coherence + falsifiable non-detection horizons. See [[s100a_md_normalization]], [[s56_fabric_neutrino]].
