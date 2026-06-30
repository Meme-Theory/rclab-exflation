---
name: omega-gw-roundfigure-fidelity
description: The "round-figure 1e-57 understates Omega_GW^(C) by ~10x/~2 OOM" claim in regulator-pin-discipline + W6 plan prose is ITSELF overstated; exact figure is 1.205x / 0.081 OOM
metadata:
  type: project
---

# Omega_GW^(C) round-figure understatement — the rule/plan prose overstates its own error

**Fact**: `regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW"` and the S96 W6-4 plan substrate_framing both say the forbidden round figure `1e-57` "understates Ω_GW^(C)=8.299e-58 by ~10× (~1 OOM) and propagates a ~2 OOM error to the (A)/(C) split." Sage-exact (QQ): `1e-57 / 8.299e-58 = 1.20496×` = **0.08097 OOM**, NOT 10×/1 OOM. The split error from the round figure is **0.081 OOM**, NOT 2 OOM.

**Why**: the round figure is ~1.2× the exact (C)-class value — a sub-0.1-OOM distortion. The "~10×" framing appears to conflate the *leading digit being 1 vs 8* with an order-of-magnitude gap; it is not one (`8.299e-58` and `1e-57` are within the same decade).

**How to apply**:
- The DISCIPLINE remains binding and correct: use the Sage-exact rational (`Ω_GW^(C)=8299/10⁶¹`, `Ω_GW^(A)=1/10¹⁰`, OOM split = **47.080974**; canonical `OOM_split_AC_regulator_class=47.081` is the rounded form). Never publish `1e-57` in registry text.
- The REASON to use the exact form is publication-precision hygiene (Class-8.3), NOT a 1–2 OOM blunder. When citing the rule, state the corrected magnitude (1.205× / 0.081 OOM), do not repeat "~10×".
- Flagged in the S96 W6-4 WP §(A) + the falsifier-master-inventory Row #7.audit FIDELITY NOTE for the **W8-2 inventory consolidation**. If a future session repeats the "~10×/~2 OOM" claim, correct it.
- This is a [[reference_key-constraints]]-adjacent do-not-overstate instance: the bridge-role check applies to the project's OWN rule prose, not only to external Planck/DESI claims.

**Provenance**: S96 W6-4 gate `S96-OBS-OMEGAGW-GGE-VS-ZN` (PASS), Sage MCP QQ verification; `computations/session-96/s96_obs_omegagw_gge_vs_zn.{py,npz}`.
