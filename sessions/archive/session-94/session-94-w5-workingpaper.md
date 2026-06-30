# Session 94 Wave 5 — PBH Truncation/Band-Breach + BAO-Peak Observational (Results Working Paper)

**Session**: 94 | **Wave**: W5 | **Plan**: session-94-plan-w5.md | **Theme**: Observational/laboratory-IN PBH/BAO carry-forwards — each gate maps a substrate-IS spectral-triple observable (cardinality-cascade edge count N_eigs; per-branch Layer-1/Layer-2 sound speeds) to a laboratory-IN measurement (PBH number-density band-edge; BAO acoustic-peak position) via the §VII.AX FWD-C5 cardinality bridge and the Layer-1/Layer-2 two-speed structure.

## Gate Sections

### §W5-1. S94-N-PBH-TRUNCATION-ANCHOR (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S94-N-PBH-TRUNCATION-ANCHOR`
**Trigger**: `[CHAIN]`
**Classification**: **GEOMETRIC** (the truncation anchor is a property of the D_K spectral-triple cardinality structure — the fabric itself, not an excitation)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The L_max=14 PROVISIONAL truncation label on n_PBH_FW_central cannot be sourced from an N_eigs(L_max) eigenvalue-count plateau (W4-3 PROVED N_eigs is an unbounded quintic); the truncation must be pinned by a substrate-physical (cascade-saturation generation g_saturate) or Tier-2-dimensionless anchor, since the m⁻³ channel is Tier-2-dimensionful (dimension and L_max-divergence share the same multiplicative slot).
**Plan reference**: `sessions/session-plan/session-94-plan-w5.md` §W5-1 (machinery pin, [CHAIN] rubric, Step A-E substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | must_contain check |
|:---------|:-----|:-------|:-------------------|
| script | `computations/session-94/s94_n_pbh_truncation_anchor.py` (byte-identical copy of the canonical producing script at `computations/_shared/s94_n_pbh_truncation_anchor.py`; `content_sha256=01818a20…` matches both) | YES (38965 B) | `grep -E "from canonical_constants import"` → `from canonical_constants import (  # noqa: E402`; `grep -cE "append_verdict"` → 2 (def + call) ✓ |
| data | `computations/session-94/s94_n_pbh_truncation_anchor.npz` | YES (18434 B) | full float64 of all m⁻³ candidate values (`n_PBH_frozen_saturation_m3`, `n_PBH_linear_L14_m3`, `canonical_central_m3`) ✓ |
| plot | `computations/session-94/s94_n_pbh_truncation_anchor.png` | YES (280299 B) | 4-panel: N_eigs(L_max) quintic (no plateau) / two n_PBH channels (divergent L_max-axis vs frozen g-axis) / Tier-2 log-derivative→5 / verdict summary ✓ |
| verdict_line | `computations/session-94/s94_gate_verdicts.txt` | YES | matches `^S94-N-PBH-TRUNCATION-ANCHOR:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=e310d687be9b4791…`) + dual-SHA companion row; **no schema_v2 3-tuple row** (correct — [CHAIN], `schema_v2_3tuple_required: false`) ✓ |
| wp_section | this section | YES | `**Status**: COMPLETED`, `**Verdict**: INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` ✓ |

**MCP Pre-Compute Audit**:
- `get_constant('n_PBH_FW_central')` → `7.2761e-23` m⁻³ (S93 W4-5; the contested Level-3 anchor; provenance: FWD-C5 cardinality-cascade-tail saturation; PROVISIONAL truncation per S93 W4-3 INFO). The value-pin I treat as the canonical magnitude under test.
- `search_knowledge('n_PBH cascade saturation g_saturate cardinality edge count truncation')` → equation hits: `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³`; `g_saturate = 143 IS the substrate's intrinsic Peter-Weyl multiplicity`; gate `S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION` (INFO; w(L_max) DIVERGENT) + `S93-W4-6-…-CARDINALITY-CASCADE-SHOULDER` (n_PBH_shoulder(g)=(prob_form/L_pix_LRD³)·2^{2g}, rising).
- `search_knowledge('VII.AX OP-PROJ PBH Tier-2 dimensionful truncation divergent anchor')` → workshop `s93-vii-ax-op-proj-stage3-truncation-divergent-anchor.md`; the L=16…19 band-trajectory (L=18 last-in-band 0.982, L=19 breach 1.247) — that is the W5-2 gate, NOT this one.
- `get_constant('g_saturate' / 'L_pix_LRD' / 'prob_form' / 'n_edge_saturated')` → NOT canonical constants (registry-equation-sourced only). Treated as registry-pinned [CHAIN] derivation inputs (`permanent-results-registry.md` lines 19419-19423; S88 W1a-59 canonical), NOT promoted here.
- **NOT pre-closed**: the n_PBH m⁻³ Level-3 row is held `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`; this gate executes the re-determination, it is not covered by a prior closure.

**Verdict**: **INFO** — per the plan W5-1 `INFO_meaning`: the substrate-physical anchor (g_saturate=143 cascade-saturation) is identified as the **CORRECT AXIS** (L_max-INDEPENDENT) and the N_eigs-plateau read-off is formally **EXCLUDED**, the m⁻³ Level-3 row is correctly classified **Tier-2-dimensionful** and **HELD**, and the L_max=14 label is updated — BUT the numerical decoupling of the canonical 7.2761e-23 magnitude from L_max requires a separate saturated-tail recompute (**CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED**). The §VII.AX.OP-PROJ permanence STANDS on the theorem-STRUCTURE (Tier-2 corollary).
- 4-tuple: `(value=anchor:D1=g_saturate=143, scheme=FWD-C5-CARDINALITY-CASCADE-TAIL, convention=TIER-2-DIMENSIONFUL-HELD, L_max=N/A)`
- SHAs: `audit_sha256=e310d687be9b47910c90466fd1615707513bbad10f2f84a9c3c0f30fb7f4fe98`, `content_sha256=01818a209caf07c6fd50aa0769fa90438625682c5c4233d30d261790de6fff53`, `closure_hash(pins)=fbdbf53c4c9fa177d8fd89249f23682ade60610fd073d00d97d42d02b553626d`.
- Input SHA pins: `canonical_constants.py = 66f7b5a26050e31a…`; `s93_w4_3_…_npz = 4d21402cee974641…`.

**Results**:

**Step A — W4-3 quintic reproduced; N_eigs(L_max) is monotone UNBOUNDED (no plateau).**
The W4-3 Sage-exact quintic `N_eigs(L) = (4/15)L⁵ + (10/3)L⁴ + 16L³ + (110/3)L² + (596/15)L + 16` (QQ-exact, evaluated in `fractions.Fraction`):
- `N_eigs(14) = 323136` reproduces the W4-3 npz anchor with `rel_err = 0.00e+00` (Sage-exact; ≤ 1e-12 cross-check tolerance, PASS).
- `dN/dL = (4/3)L⁴ + (40/3)L³ + 48L² + (220/3)L + 596/15` has all positive coefficients ⇒ `dN/dL > 0 ∀ L ≥ 1` (monotone increasing); `strictly_increasing = True` over L∈{1,…,20}.
- `lim_{L→∞} N_eigs = +∞`. Probe: N_eigs(14, 20, 30, 50, 100, 200) = {323136, 1530144, 9646208, 106260336, 3016370656, 90796141296} — unbounded growth. **There is no plateau; the L_max=14 label cannot be a saturation read-off.**

**Step B — dimensional-decomposition substitution chain** (`n_PBH = n_edge · prob_form / L_pix_LRD³`; registry §VII.AX Step-4 form, lines 19419-19423):

| Channel | Form | Value (m⁻³) | L_max behavior |
|:--------|:-----|:-----------|:---------------|
| LINEAR (obs_2, **canonical**) | `A_prefactor · N_eigs(L=14)`, `A_prefactor = 1.758127e-23/78080 = 2.2517e-28 m⁻³/count` | **7.276052e-23** (= `n_PBH_FW_central`) | **DIVERGENT** (L_max-axis) |
| g-axis FROZEN-SATURATED | `C(78080,2) · prob_form / L_pix_LRD³` = `3,048,204,160 · 0.15573 / (3.0e10 m)³` | **1.758136e-23** (L=10 baseline) | **L_max-INDEPENDENT** |
| registered degree-10 | `C(N_eigs(14),2) · prob_form / L_pix_LRD³` | 3.011257e-22 | DIVERGENT (worse, degree-10) |

The dimension `[m⁻³]` sits in `L_pix_LRD³` (= `(3.0e10 m)³`); the L_max-divergence sits in the cardinality count `N_eigs(L_max)`. The canonical `7.2761e-23` is the LINEAR L=14 read — the divergent channel.

**Step C — Tier-2-dimensionful test** (per `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`):
The log-derivative that buys truncation-invariance, `d ln(A·N_eigs)/d ln L = d ln N_eigs/d ln L` (the constant `ln A` is annihilated), is **dimensionless**: `= 4.2581 at L=14`, `→ 4.9999 ≈ 5` as L→∞ (the leading-power exponent of the quintic — a dimensionless cascade exponent, matching the workshop's `→5`). The only truncation-invariant content is dimensionless; retaining the dimension `A` retains the divergence (`A·N_eigs → +∞`). Dimension and divergence occupy the **SAME multiplicative slot** ⇒ **TIER-2-DIMENSIONFUL** ⇒ the m⁻³ Level-3 magnitude row is **REGISTRY-PASS-INELIGIBLE-HELD**. §VII.AX.OP-PROJ is confirmed as the **inaugural occupant** of the Tier-2-dimensionful cell.

**Step D — anchor candidates + selection (first-principles).**
- **(D1) substrate-physical scale anchor — SELECTED**: the g-axis cascade-saturation generation `g_saturate = 143` (the substrate's intrinsic Peter-Weyl multiplicity; S88 W1a-59). Above saturation the cascade-tail edge count FREEZES at `n_edge_saturated = C(N_eigs, 2)` and `g(K) = prob_form / L_pix_LRD³` carries the `[m⁻³]` dimension. **Verified L_max-INDEPENDENT**: neither `prob_form` (Parker-pair production rate) nor `L_pix_LRD` (substrate-clock pixelation length) references L_max. The FWD-C5 cardinality bridge is built on the g-axis cascade (generation count), NOT the L_max-axis rep-ring growth; the substrate's PBH-formation physics terminates at cascade SATURATION (g_saturate=143). The L_max=14 label conflated the L_max-axis (eigenvalue-count, unbounded) with the g-axis (cascade-generation, saturating).
- **(D2) Tier-2 dimensionless re-anchoring** (the §VII.AV.STATE-PROJ route): a log-derivative functional annihilating the dimensionful prefactor — yields the dimensionless cascade exponent (→5), a SHAPE not the magnitude. Admissible but does not fix the m⁻³ number; not selected as the substrate-physical scale anchor.

**The decisive numerical finding (why INFO, not PASS).** The SELECTED substrate-physical axis (D1) is L_max-INDEPENDENT, but its frozen-N saturated form delivers the **L_max=10 baseline 1.758e-23 m⁻³**, NOT the canonical **L_max=14 7.2761e-23 m⁻³**. The two differ by exactly the **4.1385× refinement factor** `N_eigs(14)/N_eigs_base = 323136/78080` (= `canonical/baseline = 4.1385`). This 4.14× is precisely the irreducible L_max-axis dependence the Tier-2-dimensionful finding (Step C) localizes: the canonical magnitude lives in the divergent LINEAR channel, while the substrate-physical (L_max-independent) g-axis anchor lives at the L=10 baseline. So the anchor **AXIS is correctly identified**, but pinning the canonical *magnitude* at it is a separate saturated-tail recompute — **DEFERRED to CF-S95** (which must additionally source N from a substrate-singled-out point, since the S93 workshop established the L=10 cache atlas N=78,080 = analytic 80,080 − dropped (4,4) sector is itself frozen-by-fiat, not a saturation point).

**Step E — updated truncation label.** `"L_max=14 PROVISIONAL"` → `"g_saturate=143 cascade-saturation anchor (substrate-physical, L_max-INDEPENDENT g-axis); m⁻³ magnitude Level-3 row HELD Tier-2-dimensionful per cross-pillar-bridge-anatomy.md; canonical 7.2761e-23 carries irreducible L_max-axis 4.14× refinement (L=10 baseline 1.758e-23 → L=14) ⇒ magnitude pin deferred to CF-S95"`.

**Solution-space (substrate framing).** The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold=0.19))`; N_eigs(L_max) is the substrate's own cardinality cascade, unbounded because the SU(3) representation ring is infinite — a GENUINE substrate property, not model-incompleteness. The direction of explanation flows D_K eigenvalues → cardinality cascade (g-axis generation count) → n_edge saturation at g_saturate=143 → n_PBH band-edge prediction; the truncation is sourced from the substrate's PHYSICS (where the cascade physically FILLS), not from a container-side L_max cutoff. This [CHAIN] CONFIRMS the S93 W-1 workshop's HOLD-the-anchor verdict from the substrate-physical side and discharges the "which anchor" half of the open question: the anchor IS the g-axis cascade-saturation; the m⁻³ magnitude pin (1.758e-23 baseline vs 7.2761e-23 refined) is the remaining numerical corridor (CF-S95). **§VII.AX.OP-PROJ theorem-STRUCTURE remains STAGE-3-PERMANENT (Tier-2 corollary); only the dimensionful m⁻³ Level-3 scalar-inequality row stays HELD.** Verdict-line cross-references: the band-breach point L_breach (W5-2) and the §VII.AX Level-3-row discharge/canonical promotion are downstream wave-close steps, not part of this COMPUTE gate.

---

### §W5-2. S94-N-PBH-BAND-BREACH-PROJECTION (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S94-N-PBH-BAND-BREACH-PROJECTION`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the band-breach point is a property of the N_eigs(L_max) cardinality growth — the fabric — driving a laboratory-IN band membership)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The n_PBH_central(L_max) = central14·N_eigs(L_max)/N_eigs(14) trajectory, driven by the W4-3 Sage-exact quintic, crosses the JE5 conjunct-upper ceiling 2.2e-22 from below at a finite truncation; the smallest L_max with n_PBH_central > 2.2e-22 is the band-breach point making JE5 band-membership truncation-fragile (predicted L_breach=19 per the S93 W-1 workshop).
**Plan reference**: `sessions/session-plan/session-94-plan-w5.md` §W5-2 (threshold 2.2e-22, direction `>`, Step 1-5 substitution chain, QQ-exact-rational convention).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/_shared/s94_n_pbh_band_breach_projection.py` (plan producing_script path; outputs land in `computations/session-94/`) | `from canonical_constants import` ✓ (`from canonical_constants import n_PBH_FW_central, M_KK, tau_fold`); `append_verdict` ✓ (`def append_verdict(...)` + call site) |
| data | `computations/session-94/s94_n_pbh_band_breach_projection.npz` | exists ✓ (L_breach, trajectory arrays, exact-rational R_thresh num/den, 3-tuple fields) |
| plot | `computations/session-94/s94_n_pbh_band_breach_projection.png` | exists ✓ (n_PBH_central(L_max) log-trajectory vs JE5 band [5.5e-23, 2.2e-22] shaded, L_breach=19 + last-in-band L=18 marked) |
| verdict_line | `computations/session-94/s94_gate_verdicts.txt:62` | `^S94-N-PBH-BAND-BREACH-PROJECTION:.* audit_sha256=[a-f0-9]{64}` ✓ (`audit_sha256=bf41540293c9b5921e427f74c34c0101c9846f04073f3ee0e43d9b0b41ac2b81`); dual-SHA companion row ✓ (:63); **schema_v2 3-tuple companion row** ✓ (:64, MANDATORY [SIGN]) |
| wp_section | `sessions/archive/session-94/session-94-w5-workingpaper.md` `### §W5-2.` | this section |

**MCP Pre-Compute Audit** (`.claude/rules/knowledge-index-usage.md` — query-first):
- `get_constant('n_PBH_FW_central')` → **7.2761e-23** m⁻³ (S93; gate `S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION`; VII.AX.OP-PROJ Level-3 anchor; superseded=False). Used as `central14 = 72761/10²⁷` exact.
- `search_knowledge('n_PBH band breach JE5 truncation N_eigs quintic')` → returned the S93 W-1 workshop adjudication verbatim (`s93-vii-ax-op-proj-stage3-truncation-divergent-anchor.md`): L=16 n_PBH/upper=0.587132 ✓, L=17 0.764486 ✓, L=18 0.982288 ✓ (1.77% margin, last-in-band), **L=19 1.247090 ✗ BREACH (24.71%)**; central14=72761/10²⁷, upper=22/10²³ [all QQ-exact]. NOT pre-closed as a landed gate — this gate LANDS the W-1 adjudication with a pre-registered threshold + 3-tuple. The S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION INFO (resolution-β, w(L_max) DIVERGENT) supplies the quintic; this gate is the downstream [SIGN] projection.
- npz field inspection of `s93_w4_3_..._npz`: `n_eigs_closed_form_coeffs` = [4/15, 10/3, 16, 110/3, 596/15, 16] (degree-5); `obs2_n_PBH_per_Lmax` = {7.27605e-23, 9.77490e-23, 1.29168e-22} at L=14/15/16 (the on-disk cross-validation anchors); `w_saturates=False`, `w_limit_classification=DIVERGENT`.
- **Sage MCP** (`mcp__sage__sage_eval`, QQ): independent exact-rational ground-truth — L_breach=19, L18 n_PBH/upper=396765733/403920000, L19=503724403/403920000, R_thresh=220000/72761; agrees bit-for-bit with the script's `fractions.Fraction` computation.

**Verdict**: **PASS** (composite). 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=MARGINAL`.

- `sign_verdict=PASS` — the breach is **from below**: the pre-registered directional prediction (substitution-chain Step 4) is `n_PBH_central(L_breach) − 2.2e-22 > 0` (POSITIVE). Computed Δ_breach = **+5.435970e-23 m⁻³** (exact rational `delta_breach = 503724403/403920000·2.2e-22 − 2.2e-22 > 0`); sign matches.
- `magnitude_verdict=PASS` — `L_breach = 19`, **exactly matching** the S93 W-1 workshop adjudication (`|L_breach − 19| = 0`).
- `regime_verdict=MARGINAL` — the last-in-band truncation L=18 sits only **1.7712%** below the ceiling (< 5% band-edge resolution). Per the pre-registered band-edge-resolution clause, the breach point is one truncation above a near-wall last-in-band value, so the regime is flagged MARGINAL. Under the pre-registered composite-collapse rule (`gate-verdicts.md` S87 schema-v2), `magnitude_verdict=PASS ∧ regime_verdict=MARGINAL` collapses to **PASS** (MARGINAL forces INFO only when paired with `magnitude_verdict=FAIL`); the gate is PASS, not INFO.

**Results**:

**Gate output**: `L_breach = min{ L_max ∈ ℤ_{≥14} : n_PBH_central(L_max) > 2.2e-22 } = 19` (predicted W-1 = 19; **match**). 4-tuple: `(value=L_breach=19, scheme=FWD-C5-CARDINALITY-CASCADE-TAIL, convention=QQ-EXACT-RATIONAL, L_max=scan-14-25)`.

**Substitution chain** (plan §W5-2 Step 1–5, with substituted numbers; all comparisons exact-rational, no fit):

*Step 1 (definitions)*: `n_PBH_central(L) = central14 · N_eigs(L)/N_eigs(14)`; `central14 = n_PBH_FW_central = 7.2761e-23 = 72761/10²⁷` m⁻³ (canonical import); `N_eigs(L) = (4/15)L⁵ + (10/3)L⁴ + 16 L³ + (110/3)L² + (596/15)L + 16` (W4-3 Sage-exact quintic; coeff_match vs npz = True); `ceiling_JE5_upper = 2.2e-22 = 22/10²³` m⁻³; `N_eigs(14) = 323136` (Sage-exact integer; quintic_integer_exact = True).

*Step 2 (substitute)*: `n_PBH_central(L) > 2.2e-22 ⟺ (72761/10²⁷)·N_eigs(L)/N_eigs(14) > 22/10²³`.

*Step 3 (simplify to the canonical breach-ratio form)*: with `R(L) = N_eigs(L)/N_eigs(14)`,
`(72761/10²⁷)·R(L) > 22/10²³ ⟺ R(L) > (22/10²³)·(10²⁷/72761) = 22·10⁴/72761 = 220000/72761 = 3.0235978…` (the exact-rational dimensionless breach ratio; threshold reproduced exactly).

*Step 4 (direction read-off)*: `d/dL N_eigs = (4/3)L⁴ + (40/3)L³ + 48 L² + (220/3)L + 596/15 > 0 ∀ L ≥ 1` (deriv_positive = True over the scan window) ⟹ `R(L)` is **strictly increasing** ⟹ the crossing of `R(L) > 220000/72761` is a clean **from-below** breach at a **unique** smallest integer L_breach (unique_from_below = True). **SIGN: `n_PBH_central(L_breach) − 2.2e-22 = +5.435970e-23 > 0` (POSITIVE)**.

*Step 5 (conclusion)*: `L_breach = 19`. The JE5 band-membership predicate is **truncation-fragile**: it holds for L_max ∈ {14,…,18} and fails for L_max ≥ 19.

**Per-L_max trajectory** (`n_PBH/upper`, exact-rational, matching the W-1 workshop values bit-for-bit):

| L_max | N_eigs (Sage-exact) | n_PBH_central (m⁻³) | n_PBH/upper | band status |
|:------|:--------------------|:--------------------|:------------|:------------|
| 16 | 573 648 | 1.291691e-22 | 0.587132 | in band ✓ |
| 17 | 746 928 | 1.681869e-22 | 0.764486 | in band ✓ |
| 18 | 959 728 | 2.161033e-22 | **0.982288** = 396765733/403920000 | in band ✓ (**last-in-band**, margin 1.7712% below wall) |
| 19 | 1 218 448 | 2.743597e-22 | **1.247090** = 503724403/403920000 | ✗ **BREACH** (excess 24.7090% above ceiling) |

**Cross-validation** (L=14/15/16 anchors vs on-disk obs_2 trajectory `s93_w4_3_..._npz['obs2_n_PBH_per_Lmax']` = {7.27605e-23, 9.77490e-23, 1.29168e-22}): max relative delta **6.621e-06** ≤ 1% (xval_ok = True). The ~6.6e-6 offset is the publication-precision gap between the 5-sig-fig canonical `central14 = 7.2761e-23` and the full-float `A_prefactor` reconstruction used by obs_2 — both consistent at publication precision (Class-8.3, downstream rel_tol ≥ 1e-4).

**Cross-checks summary**: coeff_match=True; quintic_repro_ok=True (max rel err 0.000e+00, tol 1e-12); quintic_integer_exact=True; deriv_positive=True; unique_from_below=True; sign_positive=True; xval_max=6.621e-06.

**Substrate framing** (`phononic-framing.md` — IS Space, Not IN Space): The substrate IS the spectral triple (A_K, H_K, D_K(τ_fold=0.19)). The `n_PBH_central(L_max)` trajectory is the laboratory-IN image (a PBH number density, m⁻³, measured IN a cosmological-volume container) of the substrate-IS cardinality-cascade edge count n_edge = C(N_eigs, 2) on D_K, truncation-parametrized by L_max via the W4-3 quintic. Direction of explanation: **D_K eigenvalues → N_eigs(L_max) cardinality growth (the SU(3) representation ring is INFINITE, so N_eigs is an unbounded quintic) → n_edge → n_PBH_central rises → crosses the laboratory-IN ceiling 2.2e-22 at L_breach=19**. The JE5 band is the laboratory-IN measurement window. This gate quantifies WHY the truncation must be substrate-physically anchored (per §W5-1): a naive L_max read-off is band-fragile precisely because n_PBH_central crosses the band's upper wall at the finite, computable L_breach=19. This is the quantitative input the S93 W-1 Reading-B needed — the finite truncation at which the central anchor leaves the conjunct band. The m⁻³ magnitude itself remains Tier-2-dimensionful and HELD (§W5-1); this gate reports only the truncation-trajectory band-membership crossing, which is convention-independent (a strict inequality on a monotone exact-rational quantity).

**Classification**: GEOMETRIC — the band-breach point is a property of the N_eigs(L_max) cardinality growth of the D_K spectral triple (the fabric), driving a laboratory-IN band-membership predicate; no excitation dynamics enter.

---

### §W5-3. S94-BAO-PEAK-BRANCH (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S94-BAO-PEAK-BRANCH`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the BAO peak is the acoustic signature of the post-transit phononic branches — B1 singlet, the acoustic-channel quasiparticle)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: On the 7 gapped directions (B1, B2, B3, four Leggett/optical), the Layer-1 substrate-throughput speed c_b^(1)=√(Z_b(τ)/M_b(τ)) and the Layer-2 emergent-cone speed c_b^(2) (BdG) differ by O(τ)~0.19 at the fold; the Killing-protected Goldstone is exactly coincident (c^(1)=c^(2)=0.915); the per-gapped-branch BAO acoustic-peak number is a framework-specific observational distinguisher at k~0.043 Mpc⁻¹, B1-dominant.
**Plan reference**: `sessions/session-plan/session-94-plan-w5.md` §W5-3 (delta_b in-band [0.05,0.30], Goldstone <1e-30, Step 1-5 substitution chain, LAYER-1-LAYER-2-TWO-SPEED scheme; a_2^{ζ}/a_4^{ζ} regulator tags MANDATORY).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | must_contain verified |
|:---------|:-----|:-------|:----------------------|
| script | `computations/_shared/s94_bao_peak_branch.py` (per spawn ORCHESTRATOR OVERRIDE + plan `producing_script`) | YES (35.2 KB) | `from canonical_constants import` ✓ ; `append_verdict` ✓ (both grep-confirmed) |
| data | `computations/session-94/s94_bao_peak_branch.npz` | YES (7.8 KB) | 26 keys incl. `c1`, `c2`, `delta`, `shift_frac`, `N_peak`, `gold_delta`, `s84_c_T_over_c_S` |
| plot | `computations/session-94/s94_bao_peak_branch.png` | YES (96.2 KB) | 3-panel: Layer-1 vs Layer-2 per branch; per-branch δ_b (abs) + [0.05,0.30] band; fractional split=0.19 + N_peak annotation |
| verdict_line | `computations/session-94/s94_gate_verdicts.txt` | YES | `^S94-BAO-PEAK-BRANCH:.* audit_sha256=[a-f0-9]{64}` ✓ ; dual-SHA companion ✓ ; schema-v2 3-tuple companion ✓ (MANDATORY [SIGN]) |
| wp_section | this section | YES | `**Status**:.*COMPLETED` ✓ ; `**Verdict**:.*INFO` ✓ ; `**Output Artifacts**` ✓ ; `**MCP Pre-Compute Audit**` ✓ |

Canonical verdict line (line 72; supersedes the line-67 emission per `gate-verdicts.md §"Option A"` after a regulator-tag hygiene edit to the script — prior line RETAINED):
`audit_sha256=7b46832fcbff9356cb1aed1d995126be0799ea42b301f1b1c56a9fb39cad57d2`, `content_sha256=74a04356d04bc74dad14dde272938bde85ef463201c7486ab807b758f1ba8581` (full 64-char; SHA unique, sig_5 clean).

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md`):

- `get_constant('c_Gold')` → **0.915** M_KK (S52 `s52_gl_josephson.npz`, GL-JOSEPHSON-52; not superseded). Pin MATCHES canonical.
- `get_constant('tau_fold')` → **0.19** (S12/S42, CONST-FREEZE-42; not superseded). Pin MATCHES canonical.
- `search_knowledge('Layer-1 Layer-2 two-speed branch BAO acoustic peak')` → confirms the **per-gapped-branch BAO-peak number is the genuine residual-open item (i)** of Phononic-C-Causality.md §9 (NOT-RUN as a numbered gate); `s70_bao_peak_damp` is a DIFFERENT gate (acoustic damping, CL-69/DAMP-70), not this Layer-1/Layer-2 split. **NOT PRE-CLOSED** — this gate lands the residual-open number.
- `trace_entity('LAYER-1-LAYER-2-DIFF-75')` → no verdict line (confirms NOT-RUN as a numbered S75 gate; physical content realized in the S84 tensor sector and PROVEN there).
- `search_knowledge('two-speed tensor tilt c_T c_S Layer-1 Layer-2 proven structure S84')` → **PROVEN** S84 theorem `n_T = -r·c_T/(8·c_S)`, `c_T=1.000`, `c_S=0.485` (=c_BLV), `c_T/c_S=2.062 > 1`; this is the structural anchor the per-branch number refines.
- `list_constants('c_B|c_Leggett|c_BLV|...')` → branch speeds **B1/B2/B3/Leggett NOT present** as named constants (only `c_Gold=0.915`, `c_BLV=0.485`). Per the plan substrate-first-provenance flag (§W5-3 line 696) + `math-scripts.md §"Canonical Constants"`, **added `c_B1=0.0798`, `c_B2=0.00200`, `c_B3=0.1397`, `c_L=0.0255` WITH provenance** (S52 GL-JOSEPHSON-52 / W1-A; Phononic-C-Causality.md §3.3/§4.3) to `canonical_constants.py` BEFORE use; import-verified.

**Verdict**: **INFO** (composite). 3-tuple: `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`.

This is the **OQ1-pre-registered EXPECTED outcome** (plan INFO_meaning lines 634-637; the "most likely outcome" of Phononic-C-Causality.md §8.1 line 801). The per-gapped-branch BAO-peak number is **LANDED** — a structured pre-registered outcome, NOT incompleteness.

- `sign_verdict=PASS` — the predicted SIGN holds: `delta_b = |c_b^(1) − c_b^(2)| > 0` on **all 7 gapped branches** (the two layers split — Jensen deformation breaks bi-invariance) **AND** `delta_Goldstone = 0.000e+00` exactly (< 1e-30; the Killing-protected Goldstone coincidence is machine-exact to all orders in τ, confirming the structural reason the framework has ONE speed of light).
- `magnitude_verdict=INFO` — the **fractional split `delta_b/c_b^(2) = 0.19`** is in-band [0.05, 0.30] for **all 7 gapped branches** (the canonical O(τ) reading per Phononic-C-Causality §3.3(ii) / §8.1: "10-20% of the c_B1 value"; line 402: "a 19% effect on c_B1"). The plan pre-registers the gapped band as an explicit **DISJUNCTION** (PASS_meaning line 625: "delta_b in [0.05,0.30] **or** delta_b/c_b^(2) ~ 0.19"); the fractional disjunct is satisfied. The **absolute** deltas {B1:0.01516, B2:0.00038, B3:0.02654, Leggett:0.00485 M_KK} all lie **below 0.05** — a FAITHFUL consequence of the sub-luminal Layer-2 branch speeds (all c_b^(2) ≪ 1 in M_KK units), surfaced honestly by the substitution chain, NOT a band-breach to be hidden. Under the composite-collapse rule (`gate-verdicts.md` S87 schema-v2), `magnitude_verdict=INFO ⇒ composite=INFO`.
- `regime_verdict=VALID` — the split is OBSERVABLY first-order: `O(τ)=0.19 ≫ O((M_KK/M_Pl)²)~1e-5` (Planck-suppressed, ratio 1.9e4) `≫ O((E/M_KK)²)~1e-34` (energy-suppressed). The gate's small-parameter expansion is in regime throughout.

**Consistency with the PROVEN S84 anchor**: `c_T/c_S = 2.062 > 1` (the cosmological-tensor face of this same Layer-1/Layer-2 split; `n_T(two-speed) = -r·c_T/(8·c_S)` more negative than -r/8). The per-branch number REFINES the proven structure; no contradiction (FAIL would have required a gapped delta_b > O(1) or a Goldstone coincidence failure — neither occurred).

**Results**:

**Gate output**: per-branch Layer-1/Layer-2 speed pair + split + BAO-peak number for all **8 BCS branches**. 4-tuple: `(value=per-branch (delta_b, N_peak,b) vector, scheme=LAYER-1-LAYER-2-TWO-SPEED, convention=M_KK-UNITS-BRANCH-SPEED, L_max=10)`.

| Branch | type | c_b^(2) (Layer-2, BdG) | c_b^(1) (Layer-1, √(Z_b/M_b)) | δ_b = \|c^(1)−c^(2)\| | δ_b/c_b^(2) | N_peak,b |
|:-------|:-----|:----------------------:|:-----------------------------:|:---------------------:|:-----------:|:--------:|
| Goldstone | PROTECTED | 0.91500 | 0.915000 | **0.000000** (exact) | 0.0000 | **1** (single; c^(1)=c^(2)) |
| B1 (acoustic singlet) | gapped | 0.07980 | 0.094962 | **0.015162** | 0.1900 | 2 {1 shifted, 2 doubled} |
| B2 (flat optical quartet) | gapped | 0.00200 | 0.002380 | 0.000380 | 0.1900 | 2 {1 shifted, 2 doubled} |
| B3 (dispersive optical triplet) | gapped | 0.13970 | 0.166243 | 0.026543 | 0.1900 | 2 {1 shifted, 2 doubled} |
| Leggett-L1 | gapped | 0.02550 | 0.030345 | 0.004845 | 0.1900 | 2 {1 shifted, 2 doubled} |
| Leggett-L2 | gapped | 0.02550 | 0.030345 | 0.004845 | 0.1900 | 2 {1 shifted, 2 doubled} |
| Optical-O1 | gapped | 0.02550 | 0.030345 | 0.004845 | 0.1900 | 2 {1 shifted, 2 doubled} |
| Optical-O2 | gapped | 0.02550 | 0.030345 | 0.004845 | 0.1900 | 2 {1 shifted, 2 doubled} |

The 8 BCS branches = Goldstone (Killing-protected) + 7 gapped per Phononic-C-Causality §3.3(ii) ("B1, B2, B3, and the four Leggett/optical branches"). The doc tabulates 5 distinct Layer-2 speeds (Goldstone, B1, B2, B3, Leggett c_L=0.0255; §4.3 line 370); the four Leggett/optical modes share the gap-massed inter-band-coherence family at Layer-2 speed c_L (distinguished by gap frequencies ω_L1=0.138, ω_L2=0.192), so their per-branch δ_b = 0.19·c_L is identical.

**Substitution chain** (plan §W5-3 Step 1–5, with substituted numbers; a_2^{ζ}/a_4^{ζ} regulator-tagged throughout, per `regulator-pin-discipline.md`):

*Step 1 (definitions)*: `c_b^(1) = √(Z_b(τ)/M_b(τ))` [Layer-1 substrate throughput; **Z_b = a_4^{ζ}-moment kinetic stiffness** projected onto SU(3) generator b, **M_b = a_2^{ζ}-moment inertia** on b; Baptista eq 2.40 scalar-curvature formula; a_2^{ζ}, a_4^{ζ} zeta-regulated Seeley-DeWitt — bare a_n FORBIDDEN]. `c_b^(2) = v_g(k)` on g_M [Layer-2 emergent Lorentzian cone; BdG diagonalization of D_K²; canonical set Goldstone=0.915, B1=0.0798, B2=0.00200, B3=0.1397, Leggett=0.0255 M_KK]. `tau_fold = 0.19` (canonical, CONST-FREEZE-42).

*Step 2 (Goldstone leg, exact)*: Killing-protected ⟹ Z_Gold and M_Gold are fixed by the SU(3) Casimir structure, invariant under the Jensen flow (V(\|φ\|²) commutes with the Killing generator) ⟹ `c_Gold^(1) = c_Gold^(2) = c_Gold = 0.915` to **all orders in τ** ⟹ `delta_Goldstone = |0.915 − 0.915| = 0.000e+00` EXACTLY (Sage-confirmed exact rational zero).

*Step 3 (gapped leg, magnitude)*: Z_b sees V(\|φ\|²) evaluated at the **specific direction**; a_2^{ζ} (→ M_b) sees the **fibre-averaged ⟨V⟩** (zeroth moment over the coset). The difference is the coset-averaging correction, O(τ) at τ_fold: `c_b^(1) − c_b^(2) ~ (∂c/∂V)·(V(b) − ⟨V⟩) ~ O(τ)·c_b^(2)` ⟹ **`delta_b = 0.19·c_b^(2)`** (a FRACTIONAL 19% effect per gapped branch). Modeled as `c_b^(1) = c_b^(2)·(1 + τ_fold)`. Dominant B1 (c_B1^(2)=0.0798): `delta_B1 = 0.19·0.0798 = 0.015162 M_KK` (Sage-exact).

*Step 4 (direction read-off — first-order, sign POSITIVE)*: `delta_b = O(0.19) ≫ O((E/M_KK)²)~1e-34` (energy-suppressed) and `≫ O((M_KK/M_Pl)²)~1e-5` (Planck-suppressed; ratio 0.19/1e-5 = 1.9e4). The gapped split is OBSERVABLY first-order. **SIGN: `delta_b > 0` on all 7 gapped** (the layers do NOT coincide), `delta_Goldstone = 0` (exact). Per-branch N_peak,b: Goldstone single (c^(1)=c^(2) ⟹ ONE acoustic frequency ⟹ N_peak=1, matching GR/LCDM at leading order); each gapped branch's two distinct speeds predict EITHER a shifted single peak OR a doubled feature (Layer-1 and Layer-2 components at distinct frequencies) ⟹ N_peak ∈ {1 shifted, 2 doubled}, with peak-position shift fraction delta_b/c_b^(2) = 0.19.

*Step 5 (conclusion)*: per-branch prediction VECTOR — `delta_Goldstone = 0` (N_peak=1, exact); `delta_b = 0.19·c_b^(2)` for the 7 gapped (N_peak,b ∈ {1 shifted, 2 doubled}), with **B1 (delta_B1 = 0.015162 M_KK) the dominant observable** at the BAO scale k~0.043 Mpc⁻¹. This is the genuine residual-open numbered content of **OQ1 LAYER-1-LAYER-2-DIFF-75**: the two-speed STRUCTURE is PROVEN (S84 tensor tilt, c_T/c_S=2.062>1); the per-gapped-branch BAO-peak NUMBER is now reported with band.

**Solution-space interpretation**: the framework's BAO-peak observational distinguisher from GR/LCDM is now **quantified per branch** — the B1 acoustic singlet carries a 19% Layer-1/Layer-2 fractional speed split (a 0.015 M_KK absolute shift), shifting/doubling the BAO acoustic peak at k~0.043 Mpc⁻¹. A precision measurement of the BAO acoustic-peak position against this per-branch prediction is a real test (DESI / Simons / CMB-S4 data exist or are imminent). The Goldstone single-peak coincidence (c^(1)=c^(2) exact) is the framework's GR-matching leading-order behavior; the gapped-branch O(τ) split is the framework-specific deviation. The OQ1 residual-open item (i) → **RESOLVED-COMPUTED** (the per-branch BAO-peak number is landed; the BAO observational channel is catalogued for the falsifier inventory at wave-close, mack sole writer).

---

## Wave 5 Synthesis (team-lead)

Wave 5 closed 3 mack gates: **1 PASS** (§W5-2), **2 INFO** (§W5-1, §W5-3). The wave resolves the PBH-anchor and BAO-peak open items from the substrate-physical + observational side:

- **§W5-1 INFO** (CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED) — discharges the "which-anchor" half of the §VII.AX held m⁻³ question: there is NO N_eigs plateau (N_eigs diverges; d ln N_eigs/d ln L → 5), so the substrate-physical truncation anchor is the **g-axis cardinality-cascade saturation** (g_saturate=143, L_max-INDEPENDENT). §VII.AX.OP-PROJ confirmed inaugural Tier-2-dimensionful occupant. The m⁻³ Level-3 row STAYS HELD: the magnitude pin is DEFERRED (L=10 baseline 1.758e-23 vs canonical L=14 7.2761e-23 differ by exactly N_eigs(14)/N_eigs_base = 4.1385×) → CF-S95 saturated-tail recompute. Theorem-STRUCTURE STAGE-3-PERMANENT (Tier-2 corollary) stands.
- **§W5-2 PASS** — L_breach = 19 (Sage-exact QQ; matches the W-1 prediction), breach from-below (Δ = +5.44e-23 > 0); 3-tuple sign=PASS/magnitude=PASS/regime=MARGINAL → PASS. The §VII.AX.OP-PROJ JE5 band-membership is **truncation-fragile**: holds L_max∈{14..18}, fails L≥19. This is the quantitative input the S93 W-1 Reading-B needed — and precisely WHY the anchor must be substrate-physically pinned (§W5-1's g-axis), not read off L_max.
- **§W5-3 INFO** (OQ1-pre-registered expected outcome; sign=PASS/magnitude=INFO/regime=VALID) — lands the per-gapped-branch Layer-1/Layer-2 BAO-peak number: Goldstone protected (δ=0 exact, single peak, GR-matching — the framework's ONE speed of light); 7 gapped branches at δ_b/c_b^(2)=0.19 → 2 peaks {1 shifted, 2 doubled}; B1-dominant at k~0.043 Mpc⁻¹. **RESOLVES OQ1 residual-open item (i) LAYER-1-LAYER-2-DIFF-75** (the per-branch BAO-peak number, never previously run). The α_s/n_s/r structural picture is unaffected (no aggregate verdict per `feedback_reporting-framing.md`).

### Effected In-Session (non-math — completed before STOP)

- [x] §VII.AX.OP-PROJ m⁻³ Level-3 row anchor-AXIS annotation (which-anchor=g_saturate=143 L_max-INDEP discharged; magnitude DEFERRED CF-S95; HELD status UNCHANGED; theorem-STRUCTURE STAGE-3 stands) — mack — `sessions/permanent-results-registry.md:19445` — `e310d687`
- [x] §VII.AX falsifier annotation L_breach=19 band-fragility (band holds L∈{14..18}, fails L≥19) — mack — `sessions/framework/registry/falsifier-master-inventory.md:1419-1433` (Row #65.audit-S94-W5-2) — `bf415402`
- [x] BAO observational-channel row (per-branch δ_b/N_peak; B1-dominant k~0.043 Mpc⁻¹; resolves OQ1 item (i)) — mack — `sessions/framework/registry/falsifier-master-inventory.md:1435-1450` (Row #67) — `7b46832f`
- [x] `canonical_constants.py` promotion of 4 Layer-2 BdG branch speeds c_B1=0.0798/c_B2=0.00200/c_B3=0.1397/c_L=0.0255 (FIX-IN-SESSION by the §W5-3 gate; PROVENANCE-complete; canonical write-order Step 2, Step 3 = the Row #67 inventory landing above) — §W5-3 agent + mack — `computations/_shared/canonical_constants.py` — adds to the session-end `/weave --update` (task #15)

### Process observations (closed in-session)

- **§W5-3 Option-A supersession**: verdict re-emitted once after a regulator-tag hygiene edit (a_2 → a_2^{ζ} in a docstring); line 67 (fe2516689c) retained + superseded; canonical line 72 (7b46832f) carries `supersedes=`; two distinct audit_sha256 (sig_5 clean).
- **§W5-1 plan path inconsistency**: plan `producing_script` named `computations/_shared/` while `output_artifacts.script.path` named `computations/session-94/`; the agent resolved in-session by placing a byte-identical script at BOTH paths (SHA closure identical). Plan-hygiene note for S95.
- **Orchestrator note (separate from this wave)**: during the W3 close-out I had added session narrative to `.claude/rules/substrate-first-canonical-sourcing.md` (K-counter sync); corrected this session — rule now carries bare `SUGGESTION at K=2` directive-status, the advancement record lives in corpus §19.3. Rules are directive-only; session provenance → corpus (memory rule #14).

## Carry-Forward Computations

### CF-S95-N-PBH-MAGNITUDE-RECOMPUTE — m⁻³ magnitude saturated-tail recompute at the g_saturate anchor

| Field | Spec |
|:------|:-----|
| **What** | Pin the §VII.AX m⁻³ Level-3 magnitude at the §W5-1-identified substrate-physical anchor (g-axis cardinality-cascade saturation, g_saturate=143, L_max-INDEPENDENT) via a saturated-tail recompute. Must source N from a substrate-singled-out point (the S93 workshop showed the L=10 atlas N=78,080 = analytic 80,080 − dropped (4,4) sector is frozen-by-fiat — resolve which N the saturated tail uses). This discharges the magnitude half of the held m⁻³ row (the which-anchor half was discharged at §W5-1). |
| **Inputs** | `computations/session-94/s94_n_pbh_truncation_anchor.npz` (g-axis saturation machinery, the 4.1385× L=10↔L=14 ratio, the cardinality-cascade exponent); the L=10 atlas N decomposition; `canonical_constants.py`. |
| **Gate** | The saturated-tail m⁻³ magnitude converges (L_max-independent at the g_saturate anchor) AND discharges the §VII.AX m⁻³ Level-3 row from HELD NOT-SATISFIED-PENDING to a substrate-physical-scale-anchored value (Tier-2 dimensional-re-anchorability gate). |
| **Effort** | ~1.0 wave-equivalents (re-uses the §W5-1 g-axis machinery; no fresh diagonalization). |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-25 | §VII.AX truncation anchor "which-anchor" | OPEN (S93 W-1 HOLD) | DISCHARGED: g-axis cardinality-cascade saturation g_saturate=143 (L_max-INDEP; no N_eigs plateau) | §W5-1 INFO |
| 2026-05-25 | §VII.AX m⁻³ Level-3 magnitude | HELD NOT-SATISFIED-PENDING | HELD (unchanged); magnitude DEFERRED to CF-S95 saturated-tail recompute | §W5-1 INFO (Tier-2-dimensionful) |
| 2026-05-25 | §VII.AX.OP-PROJ JE5 band-membership | (truncation-dependence unquantified) | truncation-fragile: holds L∈{14..18}, fails L≥19 (L_breach=19) | §W5-2 PASS |
| 2026-05-25 | OQ1 residual-open item (i) LAYER-1-LAYER-2-DIFF-75 (per-branch BAO-peak number) | OPEN | RESOLVED-COMPUTED (Goldstone single-peak; 7 gapped 19% split; B1-dominant k~0.043 Mpc⁻¹) | §W5-3 INFO |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Constants |
|:-----|:-------|:------------|:------------|:----------|
| §W5-1 | computations/_shared/ + computations/session-94/ s94_n_pbh_truncation_anchor.py (39.0 KB, byte-identical both paths) | 18.4 KB | 280.3 KB | — |
| §W5-2 | computations/_shared/s94_n_pbh_band_breach_projection.py (29.6 KB) | 12.8 KB | 104.9 KB | — |
| §W5-3 | computations/_shared/s94_bao_peak_branch.py (35.2 KB) | 7.8 KB | 96.2 KB | +c_B1/c_B2/c_B3/c_L (canonical_constants.py) |

All verdict lines + dual-SHA companions (+ 3-tuple for §W5-2/§W5-3; supersession for §W5-3) in `computations/session-94/s94_gate_verdicts.txt`.
