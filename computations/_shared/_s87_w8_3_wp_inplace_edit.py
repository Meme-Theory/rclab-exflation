"""One-shot Python writer to atomically replace the §W8-3 stub in the S87 unified WP.

Uses str.replace on a loaded snapshot to avoid the Edit-tool mtime race
(per `.claude/rules/agent-standards.md` §"Registry-Write Hygiene under
Parallel-Writer Race", S86 W1c calibration corpus).

The replacement is keyed on the unique stub line:
    "### §W8-3. S87-C45-SIXTH-REGULATOR-PROMOTION (gen-physicist)"
which is unique in the WP.
"""
from pathlib import Path

WP = Path(__file__).resolve().parent.parent / "sessions" / "session-87" / "session-87-results-workingpaper.md"

OLD = """### §W8-3. S87-C45-SIXTH-REGULATOR-PROMOTION (gen-physicist)

**Status**: NOT STARTED
**Gate ID**: `S87-C45-SIXTH-REGULATOR-PROMOTION`
**Trigger**: `[VERIFY, CHAIN]`
**Classification**: **GEOMETRIC** (C45 sixth-regulator candidate promotion to A_4 → A_5+ atlas extension)
**Agent**: `gen-physicist`
**Hypothesis**: A sixth regulator (C45 candidate) admits promotion from S86 W-8 candidate status to A_4 → A_5+ atlas extension, with the promotion-substitution chain showing the new regulator does not break cluster-span / channel-independence at L_max=10.
**Plan reference**: `sessions/session-plan/session-87-plan-w8.md` §W8-3.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: C45 promotion verdict + atlas extension manifest, 4-tuple, CC1 cluster-span preservation under A_4 → A_5+ extension, CC2 channel-independence preservation, substitution chain, dual-SHA, artifacts)*

---"""

NEW = """### §W8-3. S87-C45-SIXTH-REGULATOR-PROMOTION (connes-ncg-theorist)

**Status**: COMPLETE
**Gate ID**: `S87-C45-SIXTH-REGULATOR-PROMOTION`
**Trigger**: `[VERIFY, CHAIN]`
**Classification**: **GEOMETRIC** (C45 sixth-regulator candidate promotion to A_4 → A_5_v2 atlas extension)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: There exists a candidate sixth regulator R_6 such that R_6 (a) PASSes all 4 LAYER 2 admissibility channels (axiom-sourcing minimality / inner-fluctuation lift / HBW positive-cone / routing-Λ-scaling) AND (b) matches §VII.M layer-membership target, promoting A_4 → A_5_v2 with R_6 in the slot.
**Plan reference**: `sessions/session-plan/session-87-plan-w8.md` §W8-3.

**MCP Pre-Compute Audit**:
- `mcp__knowledge__.search_knowledge(\"Connes-Moscovici 1995 Hopf cocycle inner fluctuation\")` → S85-CC-3-CONNES-MOSCOVICI-RESIDUE (FAIL, dim-spec-signed-residue), S83 W3-G54 HP^even-completeness, CM-1995 §III.4 cocycle generators (R_universal/R_BDI/R_PV/R_anomaly) confirmed.
- `mcp__knowledge__.search_knowledge(\"W-8 GATE A FAIL cutoff_AL2010 L^8 Peter-Weyl growth a_0 channel\")` → S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS FAIL canonical (alpha_star=-1.5467, k_eff=6.1867 at L=10); load_bearing_set(a_0, cutoff_AL2010)={dim, fin}; substrate L^8/960 growth confirmed as structural pre-determination.
- `mcp__knowledge__.search_knowledge(\"A_4 atlas zeta Zubarev SDW anomaly four-regulator\")` → A_4 = {ζ, Zubarev, SDW, anomaly} canonical post-W-8 cascade (cutoff_sqrt structurally excluded; A_5 → A_4).
- `mcp__knowledge__.trace_entity(\"inner-fluctuation L^8 redirect\")` → no trace; this is NEW carry-forward content per plan §SOURCE-RECON.
- `mcp__sage__.sage_eval` channel-2 algebra (CM-1995 §III.4 generators on Mellin transforms): Schwinger M_S(s)=Gamma(s) M_S(4)/M_S(2)=6; under R_universal ratio=12 (FAIL); R_BDI=10 (FAIL); R_PV at s=4 = -18; R_anomaly=3.6 (reduces 0.6×); CM-canonical lift M_CM(s)=Gamma(s)·(s-4)/(s-3) gives M_CM(4)=0 EXACT (a_0 ZEROED), Res_{s=3}=-2 (a_2 sourced), M_CM(2)=2 (a_4 preserved).

**Verdict**: **INFO** — n_PASS = 0 / 5; no candidate clears all 4 channels + layer-match; 3 PARTIAL-INFO eligible candidates.

**4-tuple**: `(value=(0, None), scheme=4-channel-chain-test, convention=A_4_to_A_5_v2_promotion_attempt, L_max=10)`
**audit_sha256**: `51eb6ecc2f0c697375858a87b6810c30471af26dcdd3da6ca4b0f8e52a96fee3`
**content_sha256**: `90d4c46f6b54c255bc3244acce093a2df832b87fcd05e722feb4324829895d92`

---

#### PART-1. Candidate enumeration (pre-registration)

The sixth-regulator candidate set is PRE-REGISTERED at plan §W8-3 §5:

```
R_6_candidates = {
    Schwinger_proper_time,
    Lorentz_kinematic,
    dimensional_reg_d_minus_eps,
    Borel_resummation_kernel,
    Connes_Moscovici_Hopf_cocycle_dressing
}
```

The set is constructed to span the structural axes of regulator design at the LAYER 2 admissibility level:
- **Schwinger_proper_time** — heat-kernel exponential `w_S(λ) = exp(-λ/Λ²)`. Mellin: `M_S(s) = Γ(s)`. Axiom set `{dim, reg}`.
- **Lorentz_kinematic** — Lorentzian profile `w_L(λ) = 1/(1+λ/Λ²)`. Mellin: `M_L(s) = π/sin(πs)` (strip 0 < Re s < 1). Axiom set `{dim, fin}`.
- **dimensional_reg_d_minus_eps** — power-law `w_D(λ) = λ^{-ε}` with ε → 0+ pole prescription. Axiom set `{dim, reg, fin}`.
- **Borel_resummation_kernel** — Gaussian-after-Borel-transform `w_B(λ) = exp(-λ²/Λ⁴)`. Mellin: `M_B(s) = Γ(s/2)/2`. Axiom set `{dim, reg}`.
- **Connes_Moscovici_Hopf_cocycle_dressing** — dressed kernel with intrinsic (s−4)/(s−3) Hopf-cocycle factor: `M_CM(s) = Γ(s)·(s−4)/(s−3)`, dictated by CM-1995 §III.4 cocycle algebra acting on the SU(3) d=8 dimension spectrum. Axiom set `{dim, reg, real, 1st-order, orient}`.

Channels (per plan §5):
- **Channel-1 (axiom-sourcing minimality)**: load-bearing CCM-2007 axiom subset cardinality ≤ 4.
- **Channel-2 (inner-fluctuation lift)**: admits Hopf-cocycle dressing with simple zero at s=d/2=4 and finite non-zero residue at s=3 (sources a_2; redirects L^8 weight out of a_0).
- **Channel-3 (HBW positive-cone)**: MP-abs-conv at s ∈ {2, 4, 6} on f_2=0.0, f_4=0.05, f_6=0.1 yields no negative residues.
- **Channel-4 (routing/coupling-Λ-scaling)**: α-scan over [-2, +2] step 0.05 of `Λ(L) = Λ_0·L^α`; PASS iff some α ≥ 0 yields bounded `g(L) = f_0·Λ(L)⁴·a_0(L)` as L → ∞.

The structural one-way implication (Step 3, plan §9): **channel-2 FAIL ⇒ channel-4 FAIL** (a_0-direct regulators inherit the L^8/960 Peter-Weyl growth from the cutoff_AL2010 substrate paragraph; k_eff(L=10)=6.1867 forces α_star=−k_eff/4 = −1.5467, no positive-α admissible).

#### PART-2. Per-channel results (5 × 4 PASS/FAIL grid)

| Candidate | ch-1 axiom (≤4) | ch-2 lift | ch-3 HBW | ch-4 Λ-scale | layer-match |
|:---|:---:|:---:|:---:|:---:|:---:|
| Schwinger_proper_time | PASS \\|2\\| | **FAIL** | PASS | **FAIL** (α_eff=−1.55) | FAIL |
| Lorentz_kinematic | PASS \\|2\\| | **FAIL** | **FAIL** | **FAIL** | FAIL |
| dimensional_reg_d_minus_eps | PASS \\|3\\| | **FAIL** | PASS | **FAIL** | FAIL |
| Borel_resummation_kernel | PASS \\|2\\| | **FAIL** | PASS | **FAIL** | FAIL |
| Connes_Moscovici_Hopf_cocycle_dressing | **FAIL** \\|5\\| | PASS | PASS | PASS (α_eff=0.0) | FAIL |

**Channel-1 (axiom-sourcing minimality)**: 4 of 5 candidates PASS. The CM-Hopf candidate FAILs at cardinality 5 — CM-1995 §III.4 Hopf algebra `H_CM` acting on the spectral triple genuinely requires {regularity + reality + first-order + orientability} on top of {dim, reg}, exceeding the ≤4 minimality budget set by the A_4 baseline pattern.

**Channel-2 (inner-fluctuation lift)**: Only the CM-Hopf candidate PASSes. The four standard regulators (Schwinger, Lorentz, Dim-reg, Borel) all read off a_0 directly — their Mellin transforms do NOT vanish at s=d/2=4. Sage-verified base ratios `M(4)/M(2)`: Schwinger 6.0 (a_0 weighted 6× over a_4), Borel 1.0, Lorentz pole-laden, Dim-reg ε-pole-incompatible. Standard Hopf-cocycle dressings on Schwinger inflate the ratio further (R_universal → 12, R_BDI → 10, R_PV → 18) or force an external R_anomaly add (3.6, but adds a 5th axiom). Only the CM-Hopf candidate carries the (s−4)/(s−3) factor BY CONSTRUCTION: `M_CM(s=4) = Γ(4)·0/1 = 0` EXACT, residue at s=3 = `Γ(3)·(3−4) = −2`, value at s=2 = `Γ(2)·(2−4)/(2−3) = 2`.

**Channel-3 (HBW positive-cone)**: 4 of 5 PASS (Schwinger, Dim-reg, Borel, CM-Hopf). Lorentz FAILs because `π/sin(πs)` has poles at all integer s — positive-cone is ill-defined. CM-Hopf's M(s=4)=0 is consistent with channel-2's a_0 zeroing (not a positivity violation), and M(s=2)=2, M(s=6)=80 remain positive on the framework-truncated f_n.

**Channel-4 (routing-Λ-scaling)**: Only the CM-Hopf candidate PASSes (α_eff=0.0 admissible because its channel-2 redirect routes the L^8 weight to a_2, where the framework truncation f_2=0.0 kills the leading divergence). The other 4 candidates inherit the cutoff_AL2010 structural defect: k_eff(L=10) = 6.1867, α_star = −1.5467 < 0; no α ≥ 0 is admissible.

**Layer-membership match (§VII.M ladder)**: All 5 FAIL because the pre-registration requires `all_4_PASS = True` as a precondition, and no candidate clears all 4 channels.

#### PART-3. R_6 winner identification — FAIL summary

**No R_6 winner.** The 5-candidate × 4-channel chain test produces zero candidates that PASS all four channels:

```
n_PASS = 0 / 5
R_6_winner = None
```

The structural failure mode bifurcates cleanly:
- **4 candidates** (Schwinger, Lorentz, Dim-reg, Borel) FAIL channel-2 (a_0-direct readings; no native Hopf-cocycle structure). The structural one-way implication forces channel-4 FAIL on these 4. Three of them (Schwinger, Dim-reg, Borel) PASS channels {1, 3} — they are PARTIAL-INFO eligible per plan §5, recording as S88 \"depth-extension promotion\" carry-forwards.
- **1 candidate** (CM-Hopf) PASSes channel-2 by construction (intrinsic (s−4)/(s−3) cocycle), and propagates channel-4 PASS via the L^8 → a_2 redirect under f_2=0.0 truncation, AND PASSes channel-3 HBW. But it FAILs channel-1 axiom-sourcing minimality at cardinality 5: the CM-1995 §III.4 Hopf algebra requires {dim, reg, real, 1st-order, orient} as load-bearing axioms (the regularity axiom is required for the dimension spectrum to be discrete; the reality and first-order axioms are required for the Hopf algebra to act on `[D, a]`; orientability is required for the orientation cycle the cocycle integrates against). Cardinality 5 > 4 violates the A_4 baseline minimality budget.

**Verdict per plan §5 collapse rule**: `n_PASS = 0 ∧ ∃ R with channel_1_PASS ∧ channel_3_PASS ∧ ¬(channel_2_PASS ∧ channel_4_PASS)` → **INFO** (PARTIAL-INFO; 3 candidates qualify: Schwinger, Dim-reg, Borel).

**Atlas consequence** (per plan §10): A_4 = {ζ, Zubarev, SDW, anomaly} REMAINS canonical. No promotion to A_5_v2. The 3 PARTIAL-INFO candidates record as S88 depth-extension carry-forwards. The CM-Hopf candidate is structurally the closest to a sixth regulator but is blocked by channel-1 axiom-sourcing — this is a quantifiable structural finding: *the only candidate that natively redirects L^8 weight requires a strictly larger axiom budget than the A_4 minimality discipline tolerates*.

**Substrate framing**: The substrate IS the Jensen-deformed SU(3) spectral triple. Its Peter-Weyl mode-count growth L^8/960 at d=8 is intrinsic. A regulator that does NOT carry a Hopf-cocycle (s−4)/(s−3) factor in its Mellin transform reads off a_0 directly and inherits the L^8 growth — this is substrate physics, not a regulator deficiency. The CM-Hopf candidate reorganizes the spectral weight from a_0 to a_2; this redistribution IS the substrate's structural response to the cocycle dressing. The channel-1 ≤4 minimality budget is a PROJECT-imposed discipline (matching A_4 baseline pattern), not a substrate axiom; future S88+ work could relax this to admit CM-Hopf as the first 5-axiom regulator (atlas A_5_v2 with strictly larger axiom budget).

**Cross-wave dependency** (per plan §\"NOTE — cross-wave dependency\"): The channel-2 Hopf-cocycle infrastructure is written to `computations/session-87/s87_w8_c45_sixth_regulator_promotion.json` under the `hopf_cocycle_dressing_space` key, including the 4 generator dressings on Schwinger, the canonical CM lift `M_CM(s) = Γ(s)·(s−4)/(s−3)`, the channel-2 admissibility predicate, and the structural one-way implication. §W8-7 (Zubarev verify) consumes this for SHA-pinned reuse.

**Open question routed to S88**: Does there exist a Hopf cocycle requiring strictly fewer than 5 axioms while still carrying a simple zero at s=4 and finite residue at s=3? The S86 W-8 substrate paragraph and CM-1995 §III.4 generator algebra suggest no — the (s−4)/(s−3) factor is the minimal Hopf-cocycle structure on the d=8 dimension spectrum, and its action on `[D, a]` requires regularity + reality + first-order + orientability. If this proof can be sharpened in S88 (either tightened or counter-example-constructed), the channel-1 vs channel-2 trade-off becomes a structural theorem about the lower bound on axiom budget for L^8 redirection.

**Carry-forward 4-field specs**:
1. **What**: Structural theorem on minimum axiom budget for L^8 redirect via Hopf cocycle. **Inputs**: CM-1995 §III.4 generator algebra, S86 W-8 substrate paragraph, channel-2 admissibility predicate from this gate's JSON. **Gate**: `S88-MIN-AXIOM-BUDGET-L8-REDIRECT-THEOREM` (THEOREM tolerance; PASS iff cardinality ≥ 5 is provably necessary). **Effort**: ~4 hours (axiomatic; Sage MCP for Hopf algebra structure constants).
2. **What**: Depth-extension promotion of {Schwinger, Dim-reg, Borel} (channels {1,3} PASS / {2,4} FAIL). **Inputs**: S87 §W8-3 PARTIAL-INFO list, S86 W-8 GATE A α-scan anchor data. **Gate**: `S88-DEPTH-EXTENSION-3PARTIAL-INFO-PROMOTION` (per-candidate channel-2 lift attempt with relaxed Hopf-cocycle requirement). **Effort**: ~5 hours.

**Artifacts**:
- Script: `computations/session-87/s87_w8_c45_sixth_regulator_promotion.py`
- Data (5×4 grid + α-scan + Hopf-cocycle infra): `computations/session-87/s87_w8_c45_sixth_regulator_promotion.json`
- Plot (5×4 PASS/FAIL grid color-coded): `computations/session-87/s87_w8_c45_sixth_regulator_promotion.png`
- Verdict line: `computations/session-87/s87_gate_verdicts.txt` (S87-C45-SIXTH-REGULATOR-PROMOTION)

---"""

text = WP.read_text(encoding="utf-8")
if OLD not in text:
    print("ERROR: stub block not found verbatim; aborting (no edit performed).")
    print("Searching for partial signature...")
    idx = text.find("### §W8-3. S87-C45-SIXTH-REGULATOR-PROMOTION (gen-physicist)")
    print(f"  partial-signature index: {idx}")
    raise SystemExit(1)

new_text = text.replace(OLD, NEW, 1)
WP.write_text(new_text, encoding="utf-8")
old_lines = OLD.count("\n") + 1
new_lines = NEW.count("\n") + 1
print(f"OK: replaced §W8-3 stub ({old_lines} lines) with full content ({new_lines} lines)")
print(f"WP file size: {len(new_text)} bytes (was {len(text)} bytes)")
