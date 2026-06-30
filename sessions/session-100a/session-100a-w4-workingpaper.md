# Session 100a Wave 4 — Scale / Functional Sensitivity + Foam Survival + Q27 Spinor Factor (Results Working Paper)

**Session**: 100 | **Wave**: W4 | **Plan**: session-100a-plan-w4.md | **Theme**: SCALE-axis register/panel carry-forwards — make the §IV bosonic/fermionic layer-separation EMPIRICAL (functional sensitivity of the SCALE vs functional-independence of the RATIOS), trace the absolute-normalization m_H inheritance, test foam-survival of the generation index, and decide atlas-08 Q27 (√16 spinor factor → H₀).

## Gate Sections

### §W4-12. S100a-M0-FUNCTIONAL-SENSITIVITY (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-M0-FUNCTIONAL-SENSITIVITY`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (functional-dependence of the SCALE vs functional-independence of the RATIOS on the spectral triple)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The per-sector overall scale M₀ (and m_H) is scheme-dependent between the cutoff action Tr f(D_K²/Λ²) and the zeta action ζ_{D_K}(0)=a₄^{ζ}, while the fermion mass RATIOS from |s(h)|²-weighted eigenvalue overlaps are bit-identical across schemes — the empirical face of the Spectral-Moment Decoupling Theorem (S75 W2-E). INFO-by-design.
**Plan reference**: `sessions/session-plan/session-100a-plan-w4.md` §W4-12 (DUAL-scheme machinery pin, RATIO bit-identity threshold, two-claim substitution chain source).

**Output Artifacts**:

| Artifact | Exists | must_contain evidence |
|:--|:--|:--|
| `computations/session-100a/s100a_m0_functional_sensitivity.py` (42,144 B) | YES | `grep -cE "from canonical_constants import"` → 2; `grep -cE "print_verdict_payload"` → 3 |
| `computations/session-100a/s100a_m0_functional_sensitivity.npz` (30,191 B) | YES | full-float64 payload: O_g, M per scheme, r per scheme, ratio_dev, D_scale, f-moments, helper a_n, dual-SHA, machinery pin map |
| `computations/session-100a/s100a_m0_functional_sensitivity.png` (98,501 B) | YES | 3-panel: per-sector masses both schemes (log) / ratio-dev vs ratio_tol+info_band+leak-control / moment-ratio by functional |
| verdict line in `computations/session-100a/s100a_gate_verdicts.txt` | YES | `grep -E '^S100a-M0-FUNCTIONAL-SENSITIVITY:.* audit_sha256=[a-f0-9]{64}'` → `S100a-M0-FUNCTIONAL-SENSITIVITY: INFO -- value='D_scale=60.64_native-norm(claimA-sign>0);ratio_dev_max=2.813e-16<=1e-12;…'`; emitted via `emit_verdict` MCP (7 rows: canonical + dual-SHA companion + schema-v2 3-tuple `sign=PASS magnitude=INFO regime=VALID` + regulator_pin + `# tier_pin=TIER-2` + operational_enrichment + masses detail) |
| this WP section | YES | Status/Verdict/Output Artifacts/MCP Pre-Compute Audit markers present |

**MCP Pre-Compute Audit**:

- `search_knowledge("spectral moment decoupling fermion mass ratio functional")` → S75 W2-E Spectral-Moment Decoupling Theorem certified PERMANENT (a₀, a₂, a₄ algebraically independent, Wronskian nonzero); S64 W5-B moment-decoupling wall. NO prior gate ran the DUAL-scheme observable-layer test (cutoff-vs-zeta mass-ratio bit-identity) — gate NOT pre-closed; this is its first empirical evaluation.
- `get_constant("a_4_FW_zeta")` → 1350.7216 (S75, s75_f_conv_spectral_output.txt L26); `get_constant("a_2_FW_zeta")` → 2776.165389 (S88, gate S88-A-N-FW-CANONICALIZATION); a_0_FW_zeta = 6440.0 (S88, same gate; verified in canonical_constants.py L607).
- `get_constant("mellin_f_star_f2")` → 214.97335676 (S78 W2-D, s78_f_conv_anomaly.npz; note "int_0^50 f*(x) dx, X_max=50 regulator"); `get_constant("mellin_f_star_f4")` → 6446.63942272 (same provenance, "int_0^50 x*f*(x) dx").
- `get_constant("R1_lizzi")` → 1.128655 (S74, N16-RATIO-OF-RATIOS-PROTECTED-74; R-PROTECTED; note: "= 1.1286546, rounds to 1.128655 at 7 sf; per-branch caveat — NOT a cross-scheme conversion factor"). The per-branch caveat is honored below (R₁ recorded per scheme, never used as a conversion).

**Verdict**: **INFO** (composite; INFO-by-design as pre-registered) — schema-v2 3-tuple: **sign_verdict=PASS** (Claim A direction D_scale > 0 holds AND Claim B ratio deviation at float64 zero), **magnitude_verdict=INFO** (D_scale is the reported-not-gated SCALE characterization), **regime_verdict=VALID** (full domain, domain_used_frac=1.0; cache blocks complete n_evals=16·dim; all input cross-checks within tolerance). Collapse rule: regime VALID + sign PASS + magnitude INFO → composite INFO. Dual-prior discriminator (plan): PASS-side RATIO clause at 2.813e-16 ≤ 1e-12 → posterior 0.97 to Track A (RATIOS bit-identical, decoupling EMPIRICAL; SCALE scheme-dependent INFO). kernel_leak_flag = none (deviation below ratio_tol, not in the (1e-12, 1e-9] leak band).

**Results**:

*Numbers first.* Scheme-independent envelope (Item-6 P1/P2 construction recomputed from the s84 L_max=12 cache, SHA-pinned `9e6d9cf7fd6a6949…`): μ_H = λ_min(0,0) = 0.819741112; O_(1,0) = 8.206524294717, O_(1,1) = 10.396533177839, O_(3,0) = 3.449930040562; m_H channel O_(0,0) = 4.972082844569. Item-6 stored O_g reproduced at max rel dev **0.0e+00** (bit-exact). S97 wall floor(1,0)/floor(0,0) = 1.019704 vs `R_cross_yukawa_t1_t2` (dev 2.65e-07 < 1e-5).

| Quantity | zeta leg (FULL) | cutoff leg (SCHEMATIC) |
|:--|:--|:--|
| Bosonic-scale moment ratio | a₄^{ζ}/a₂^{ζ} = 1350.7216/2776.165389 = **0.486542194** | f₄/f₂ = 6446.63942272/214.97335676 = **29.988085593** |
| M^{(1,0)}, M^{(1,1)}, M^{(3,0)} (envelope units) | 3.992820, 5.058352, 1.678537 | 246.097953, 311.772127, 103.456797 |
| m_H channel M_H = scale·O_(0,0) | 2.419129 | 149.094128 |
| r pairs (1,0)/(1,1), (1,0)/(3,0), (1,1)/(3,0) | 0.789352003628410, 2.378750930665138, 3.013548986676090 | 0.789352003628410, 2.378750930665138, 3.013548986676091 |
| R₁ = a₀·a₄/a₂² (per-branch, recorded) | **1.1286546** (vs canonical R1_lizzi = 1.128655, rel dev 3.88e-07 < 1e-6) | f₀·f₄/f₂² = 0.0123204 (recorded; per-branch R-protection — NOT a cross-scheme conversion factor) |

- **Claim A (INFO content — the SCALE moves)**: ratio of moment-ratios = **61.6351** (native normalizations; plan chain pre-computed 61.635 — reproduced). D_scale = |M₀^{cutoff} − M₀^{ζ}|/M₀^{ζ} = **60.64** (4 sf; per-sector spread 1.42e-14 — the common envelope cancels exactly as predicted). Δ(m_H)/m_H = **60.64** under the linear riding of plan Definition 1 (m_H rides the same (a₄/a₂)-governed scale, so its fractional shift equals D_scale by construction); under the quartic/sqrt diagnostic reading (m_H² ∝ scale) the shift is √61.635 − 1 = **6.851**. Either reading: Δ(m_H) ≠ 0. The magnitude is native-normalization-dependent (the plan flags the raw factor as a normalization artifact); the PHYSICAL content is **D_scale > 0 strictly** — the two functionals weight the bosonic SCALE moment unequally.
- **Claim B (PASS-side — RATIOS invariant)**: max_ij |r_ij^{ζ} − r_ij^{cutoff}|/|r_ij^{ζ}| = **2.813e-16** ≤ ratio_tol = 1e-12 (pairwise: 2.813e-16, 0.0, 1.474e-16; pure float64 round-off from the scale multiplication, ~1.3 ε_mach). Normalized d_i deviation identical (2.813e-16). Controls (pre-registered as controls, not gates): (a) degenerate same-scale control → max dev **0.0 exact** (bit-zero; the machinery introduces nothing); (b) injected per-sector envelope leak of 1e-6 → the test sees **2.000e-06** (the gate WOULD detect a kernel-scale leak ~10⁶× above threshold; the PASS is not vacuous).
- **SCHEMATIC helper cross-check** (same schematic Casimir spectrum, same normalization on both helper legs — normalization-artifact-free Claim-A confirmation): zeta_a_n vs hard_cutoff_a_n at L_max=12, cutoff_frac=0.7 gives a₄/a₂ = 0.056555 (zeta) vs 0.070918 (hard-cutoff) → same-normalization moment-ratio shift **0.2540 > 0**. Helper R₁ analogs (diagnostic only, schematic spectrum): 1.809752 (zeta) vs 1.784821 (hard-cutoff).
- **f\*-moment re-derivation**: closed form at X_MAX=50 with w_exp = f₀ = mellin_f_star_f0 = 0.08832, w_sqrt = 1−f₀: f₂ rel dev 1.22e-11, f₄ rel dev 2.35e-13 vs canonical pins; scipy quadrature consistent (1.22e-11 / 6.69e-12). Canonical pins used as PRIMARY per plan Definition 4.

*Substitution chain — Claim A (substituted numbers)*: M₀^{sector} = (moment ratio) × O_g [Def 1] → scale_ζ = 1350.7216/2776.165389 = 0.486542194 [Def 3]; scale_cutoff = 6446.63942272/214.97335676 = 29.988085593 [Def 4] → ratio of moment-ratios = 29.988085593/0.486542194 = 61.6351 → after the SAME per-branch Vol-normalization on both legs (common O_g cancels), Δ(M₀) ≠ 0 with D_scale = 61.6351 − 1 = 60.6351 > 0 strictly ⇒ SIGN of Δ(M₀) ≠ 0. **Claim A direction CONFIRMED.**

*Substitution chain — Claim B (substituted numbers)*: O_g = Σ_{λ∈g} exp(−λ²/μ_H²) with exact-Haar unit kernel mean [Def 2; depends ONLY on the D_K spectrum + |s(h)|² kernel, never on any a_n] → r_ij^{ζ} = (0.486542194·O_i)/(0.486542194·O_j) and r_ij^{cutoff} = (29.988085593·O_i)/(29.988085593·O_j) → both reduce to O_i/O_j exactly; e.g. r_(1,0)/(1,1) = 8.206524294717/10.396533177839 = 0.789352003628 in BOTH schemes → measured max deviation 2.813e-16 ≤ 1e-12 (float64 round-off only) ⇒ sign_verdict = PASS. **Claim B CONFIRMED.**

*Cross-class disclosure (MANDATORY per substrate-first-canonical-sourcing.md §(iv), 4-class taxonomy — POSITIVE compliance profile (1)∧(2)∧(3)∧(4))*: This gate's two legs carry **asymmetric level-pins**. The **zeta leg is FULL physical** — its moment ratio is built solely from the canonical npz-sourced zeta-regulated Seeley-DeWitt coefficients a₀^{ζ}/a₂^{ζ}/a₄^{ζ} (a_n_FW_zeta, S88-A-N-FW-CANONICALIZATION); no SCHEMATIC helper enters that leg. The **cutoff leg is SCHEMATIC** — it consumes `_spectral_action_regulators.py` (hard_cutoff_a_n; the helper self-identifies SCHEMATIC per its docstring lines 23-30, verified S88 W7b-83) together with the Chamseddine-Connes 1996 §2.2-2.3 cutoff-function Mellin moments f₂/f₄ of f* at the X_MAX=50 regulator. Compliance elements: (1) CLASS=SCHEMATIC declared in the plan gate block machinery_pin_map and in the producing script; (2) the verdict-line convention carries the pre-registered `-SCHEMATIC` suffix (`RATIO-INVARIANCE-vs-SCALE-DEPENDENCE-LAYER-PINNED-SCHEMATIC`); (3) the producing script's docstring explicitly cites the helper's SCHEMATIC self-identification; (4) the `# tier_pin=TIER-2` companion row is emitted in the verdict file. The RATIO-invariance result holds for these schematic cutoff forms; a live-physical-regularization re-run of the cutoff leg (e.g. the S61/S78 Pauli-Villars pipeline at Λ_UV = M_KK) is a separate question — structurally expected to change NOTHING on the RATIO axis (the ratios never touch any a_n) and ONLY to move the SCALE-axis magnitude D_scale, which is already declared normalization-convention-dependent.

*Regulator pins (regulator-pin-discipline.md — bare a_n forbidden)*: zeta leg a₀^{ζ} = 6440.0, a₂^{ζ} = 2776.165389, a₄^{ζ} = 1350.7216; cutoff leg a₂^{cutoff} = f₂ = 214.97335676, a₄^{cutoff} = f₄ = 6446.63942272 (Mellin f-moments of f*).

*Operational enrichment (honest disclosure per math-scripts.md plan-authorship item 4)*: `s100a_yukawa_overlap_offdiag.npz` (Item 6, landed INFO this session) was consumed as a 4th pinned input for the O_g reproduction cross-check ONLY — the primary O_g is recomputed from the s84 spectrum cache; plan input_files listed 3. Reproduction dev 0.0e+00.

*4-tuple*: (value='D_scale=60.64_native-norm(claimA-sign>0);ratio_dev_max=2.813e-16<=1e-12;…', scheme=DUAL-ZETA-VS-CUTOFF-FSTAR, convention=RATIO-INVARIANCE-vs-SCALE-DEPENDENCE-LAYER-PINNED-SCHEMATIC, L_max=12). Dual-SHA: audit_sha256=`2993dbf63fcb25d97224e2b5a6e28cf8651f9b051e613c29fb277970149dc475`, content_sha256=`7a0d7ee40284ddce986a2f493f69910e60883d303699396d53bee9bc563e396c`, schema_version=S84+.

*Substrate framing (GEOMETRIC)*: The chain D_K eigenvalues → spectral moments → emergent physics splits at the first arrow into two routes. Route 1 (RATIO axis, fermionic): the |s(h)|²-weighted eigenvalue overlaps O_g are a property of the spectrum alone — they never see which spectral functional weights the moments, so the mass ratios are FUNCTIONAL-INDEPENDENT (structural; now EMPIRICAL at 2.8e-16). Route 2 (SCALE axis, bosonic): the overall scale M₀ IS a spectral-action moment ratio, and a moment IS a choice of how to weight the spectrum — cutoff and zeta weight it differently (61.6× in native norms), so the SCALE is FUNCTIONAL-DEPENDENT, a physical degree of freedom the regulator fixes. This lands the lizzi thesis empirically: what survives all choices of spectral functional is structural; what depends on the choice is a physical degree of freedom. The §IV bosonic/fermionic layer-separation moves from ASSERTED to EMPIRICAL. Downstream: Item 13 (S100a-M0-MH-INHERITANCE) consumes the M₀ scale-anchoring characterized here — the +5.36%/+7.11% m_H over-prediction question lives entirely on the SCALE axis, the scheme-dependent one.

---

### §W4-13. S100a-M0-MH-INHERITANCE (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S100a-M0-MH-INHERITANCE`
**Trigger**: `[AUDIT]`
**Classification**: **GEOMETRIC** (provenance trace of a scale anchor on the spectral triple)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The absolute per-sector mass normalization M₀ either inherits the framework's m_H over-prediction linearly (+5.36% KK-threshold / +7.11% tree-level, if |s(h)|²-anchored to the m_H mode) or is independently anchored and carries no such residual — a report-only honest-scope ledger trace, no PASS/FAIL.
**Plan reference**: `sessions/session-plan/session-100a-plan-w4.md` §W4-13 (residual definitions, linear-propagation substitution chain, canonical write-order obligation source).

**Output Artifacts**:

All plan `output_artifacts:` entries verified on disk by content:

- `computations/session-100a/s100a_m0_mh_inheritance.py` (22,255 B) — must_contain verified: `grep -nE "from canonical_constants import|print_verdict_payload"` → line 112 `from canonical_constants import *  # noqa: F401,F403  (m_H_obs, v_ew, M_KK)`; line 360 `def print_verdict_payload(...)`; line 427 call site (plus docstring mentions at 80/90).
- `computations/session-100a/s100a_m0_mh_inheritance.npz` (5,918 B) — round-trip verified: `r_kk = 0.053557154276578735 = 67/1251`, `r_tree = 0.07114308553157474 = 89/1251`, `dM0_over_M0_low/high = (0.053557…, 0.071143…)`, `dM0_over_M0_independent_branch = 0.0`, `anchored_to_sh_sq_mode = 1`; exact integer numerator/denominator keys carried alongside full float64 (Class-8.3 round-trip: downstream verifiers load from npz, not prose).
- `computations/session-100a/s100a_m0_mh_inheritance.png` (51,214 B) — optional residual-band bar chart, produced (r_KK / r_tree bars + branch-(b) zero reference + shaded inherited band).
- Verdict line in `computations/session-100a/s100a_gate_verdicts.txt` — `grep -E '^S100a-M0-MH-INHERITANCE:.* audit_sha256=[a-f0-9]{64}'` matches: `S100a-M0-MH-INHERITANCE: INFO -- value='r_KK=+5.356pct_exact_67/1251;…' scheme=KK-threshold-131.8-plus-tree-A10-134 convention=ABSOLUTE-NORMALIZATION-PROVENANCE-TRACE L_max=N/A audit_sha256=d00bbb3794ed207c803814dd01590e906e57a6f9b96e2081ed2c50ab89ac121a content_sha256=05c709740da5d345a4f72f5737ec4f9e146f1418069d8c360eb3030af4f052e1 schema_version=S84+`, with dual-SHA companion row + 2 extra companion rows (exact rationals; write-order record). Emitted via the race-safe `emit_verdict` knowledge-MCP tool (4 rows appended, sig_5 unique). NO schema-v2 3-tuple — report-only [AUDIT] INFO per plan (`schema_v2_3tuple_required: false`); sign/magnitude/regime omitted entirely.

**MCP Pre-Compute Audit**:

Queries executed BEFORE writing the script (knowledge MCP + Sage MCP):

1. `search_knowledge("M0 mass normalization m_H inheritance")` — no prior evaluation of this trace (only the plan file itself + the S84 `m_H (Higgs mass)` open-channel row, which is the DIFFERENT mu_BC-fit route: 188.19 GeV ACCOMMODATION-flagged, S84-MU-BC-GEOMETRIC; scoped OUT of this gate's two pinned routes). NOT PRE-CLOSED.
2. `get_constant("m_H_obs")` → 125.1 (canonical, PDG class) — matches plan Def 1.
3. `get_constant("m_H_FW_KK_threshold")` → NOT FOUND; `get_constant("m_H_FW_tree")` → NOT FOUND — both genuinely NEW; promotion path clear (no overwrite hazard).
4. `trace_entity("KK-THRESHOLD-64")` + `search_knowledge("m_H 131.8 KK threshold")` → gate KK-THRESHOLD-64 (S64 W4-B, INFO): `delta=2.35 (outside PASS band [0.73,1.48]); m_H = 131.8 GeV`; lineage "framework prediction from S28c … KK-mode threshold correction structure at the Jensen-deformed fiber"; S62 constraint-mega-matrix row `m_H = 127.5–131.8 GeV (Aitken-Gaussian)`.
5. `search_knowledge("m_H 134 tree filter independence A10")` → theorem A10 (atlas-07 permanent, S62): "Filter-Independence of Tree-Level Higgs Mass — λ_h = (4/3)g_3²(M_KK)·(a_4/a_2), NOT cutoff-shape-dependent"; `m_H(tree) = v·sqrt(2λ_CCM) = 246 × 0.5452 = 134.04 GeV` (s83-mu_BC-geometric-derivation.md).
6. `search_knowledge("fiber embedding transverse oscillation Higgs |S|^2 mode")` → canonical_classes.py "Higgs and EW cluster": "Framework prediction m_H = 131.8 GeV (KK threshold corrections to the |S|² mode of the fiber embedding)" — the anchor-identity statement verbatim.
7. `search_knowledge("BCS threshold correction Higgs -7%")` → S62 `s62_higgs_bcs_threshold.py` / THRESHOLD-62 / HIGGS-BCS-THRESHOLD-62 ("ACCEPTED with modification" — anomalous self-energy correction Σ_anom(q²=M_KK²) to g_3(M_KK)); S61-W8: "m_H = 134 ± 7 GeV … 7.1% from observed. BCS threshold correction (~−7%, screening…)".
8. Verdict-file grep (sibling gates): Item 6 `S100a-YUKAWA-OVERLAP-OFFDIAG` LANDED (INFO, `JENSEN-FIBER-OVERLAP-SU3-HAAR`, |s(h)|² fiber-overlap kernel machinery); Item 12 `S100a-M0-FUNCTIONAL-SENSITIVITY` not yet landed (fb_pair forward reference only — not a prerequisite of this trace). Cross-sector context: `S100a-MD-NORMALIZATION` (INFO) found the NEUTRINO Dirac-scale normalization `residual-Dirac-scale-normalization-IRREDUCIBLE` — the absolute-scale question is live across sectors.
9. `mcp__sage__sage_eval` (QQ exact): `r_KK = 67/1251 = 0.0535571542766 → +5.355715428%`; `r_tree = 89/1251 = 0.0711430855316 → +7.114308553%`; band width `= 22/1251 = 0.01758593126`; published 4 s.f. `+5.356% / +7.114%` — matches the plan substitution chain exactly.

**Verdict**: **INFO** (the SOLE pre-registered outcome — report-only provenance trace; no PASS/FAIL token). 4-tuple: `(value=<trace payload>, scheme=KK-threshold-131.8-plus-tree-A10-134, convention=ABSOLUTE-NORMALIZATION-PROVENANCE-TRACE, L_max=N/A)`. Dual-SHA: `audit_sha256=d00bbb3794ed207c803814dd01590e906e57a6f9b96e2081ed2c50ab89ac121a`, `content_sha256=05c709740da5d345a4f72f5737ec4f9e146f1418069d8c360eb3030af4f052e1`.

**Results**:

NUMBERS first (exact rational | full float64 | published 4 s.f.):

| Quantity | Exact (Sage QQ = in-script Fraction, asserted equal) | float64 | Published |
|:---------|:------------------------------------------------------|:--------|:----------|
| r_KK = m_H^{KK}/m_H_obs − 1 = 131.8/125.1 − 1 | **67/1251** | 0.053557154276578735 | **+5.356%** |
| r_tree = m_H^{tree}/m_H_obs − 1 = 134.0/125.1 − 1 | **89/1251** | 0.07114308553157474 | **+7.114%** |
| band width r_tree − r_KK | 22/1251 | 0.017585931255 | 1.759 pp |
| δM₀/M₀ branch (a), |s(h)|²-anchored | [67/1251, 89/1251] | [0.0535572, 0.0711431] | **[+5.356%, +7.114%]** |
| δM₀/M₀ branch (b), independently anchored | 0 | 0.0 | 0 |

Both residuals POSITIVE — the framework OVER-predicts m_H on both routes (direction claim verified in-script; cross-checks: Sage-QQ equality asserted exact, plan-quoted 6-d.p. ratios 1.053557/1.071143 matched to <5e-7).

**Anchor identification (the trace content)** — branch (a) IS the framework's anchor. M₀^{sector} is |s(h)|²-anchored to the SAME fiber-embedding mode that sets m_H. Evidence chain (substrate-first, D_K → |s(h)|² overlap → {m_H, M₀} → measurement):

1. canonical_classes.py "Higgs and EW cluster" states the identity verbatim: framework m_H = 131.8 GeV IS "KK threshold corrections to the |S|² mode of the fiber embedding" — m_H is the transverse oscillation of the fiber embedding.
2. KK-THRESHOLD-64 (S64 W4-B, INFO; S28c lineage) evaluates that mode at the Jensen-deformed fiber → 131.8 GeV.
3. Item 6 `S100a-YUKAWA-OVERLAP-OFFDIAG` (landed INFO this session, `JENSEN-FIBER-OVERLAP-SU3-HAAR`): the per-sector Yukawa normalization is computed from the Jensen-fiber |s(h)|² overlap kernel — M₀^{sector} rides the same fiber-embedding envelope whose transverse |S|² oscillation is m_H. Shared anchor ⇒ shared residual.
4. Theorem A10 (S62, atlas-07 permanent) fixes the tree endpoint: λ_h = (4/3)g_3²(M_KK)·(a_4/a_2) cutoff-shape-independent ⇒ m_H(tree) = 134.0 GeV.

**Linear propagation** (plan Def 5, substituted): m_H² = (4/3)g_3²(M_KK)(a_4/a_2)·v²-structure ⇒ m_H ∝ (scale)¹; M₀ ∝ (scale)¹ ⇒ δM₀/M₀ = δm_H/m_H to leading order — LINEAR at FIRST power, not squared. Substituting the residuals: δM₀/M₀ = +67/1251 … +89/1251 = **[+5.356%, +7.114%]**, the band endpoints corresponding to anchoring depth (KK-threshold-corrected mode → +5.356%; bare tree mode → +7.114%). Under branch (b) (independent anchoring, e.g. direct M_KK) the residual would be 0 — that is NOT the identified branch.

**BCS bookkeeping (honest-scope critical)**: the BCS threshold correction (~−7%, S62 THRESHOLD-62 / HIGGS-BCS-THRESHOLD-62 — anomalous self-energy correction Σ_anom to g_3(M_KK), "ACCEPTED with modification") is the documented physical mechanism closing 134 → ~125 in the m_H chain. It has been applied in the m_H discussion ONLY — it has NOT been applied to M₀^{sector}. If the same screening were applied to M₀, the inherited residual would shrink toward ~0 in step with m_H → 125. Until that computation exists, the band stands.

**Honest-scope ledger feed (capstone §7 scope row — mack sole writer; to be landed in the session-close §7/inventory batch per orchestrator dispatch)**. Row content pinned here:

> **M₀^{sector} (absolute fermion-mass normalization)** — internal-consistency scope row, NOT a detector-horizon row. The fermion-mass RATIOS are clean substrate predictions (Item 12 scope; Spectral-Moment Decoupling, S75 W2-E); the absolute SCALE is |s(h)|²-anchored to the m_H fiber-embedding mode (S100a-M0-MH-INHERITANCE, INFO, audit d00bbb3794ed207c…) and therefore inherits the documented Higgs-sector over-prediction LINEARLY: δM₀/M₀ ∈ [+5.356%, +7.114%] (exact 67/1251, 89/1251 vs m_H_obs = 125.1). BCS −7% screening (S62) applied to m_H only, NOT to M₀ — a future M₀-side BCS application is the closure mechanism. Cross-sector echo: the neutrino Dirac-scale normalization is independently IRREDUCIBLE (S100a-MD-NORMALIZATION, INFO). The §IV absolute-normalization claim carries THIS confidence, no more.

**Canonical write-order (FIX-IN-SESSION, executed this gate in the mandated order)**: (1) verdict line emitted FIRST via `emit_verdict` (race-safe MCP; 4 rows, sig_5 unique — the audit_sha256 pins the PRE-promotion canonical_constants state, as designed); (2) `m_H_FW_KK_threshold = 131.8` (source: KK-THRESHOLD-64 / S28c) and `m_H_FW_tree = 134.0` (source: theorem A10 / S62 Filter-Independence) promoted to canonical_constants.py SECTION E via `update_constant` WITH PROVENANCE (absence pre-verified in audit item 3; post-promotion import sanity-checked: both names import cleanly alongside m_H_obs); (3) inventory/§7 row deferred to the mack session-close batch per orchestrator override — row content pinned above. In-script the two values were pinned as documented `# (local)` framework-prediction literals with gate/theorem cites, per the plan's interim rule.

**Substrate framing**: GEOMETRIC — this trace reads a scale anchor off the spectral triple, not an excitation. The chain D_K eigenvalues → |s(h)|² fiber-embedding overlap → (m_H from the |S|² transverse mode AND M₀^{sector} from the same overlap envelope) → measurement. The residual is a property of how the |s(h)|² mode sits on D_K, read FROM the substrate TOWARD the lab — the framework does not "miss" the lab value as a container-level discrepancy; the substrate's fiber-embedding mode is over-normalized by 67/1251…89/1251 relative to the measured |S|² oscillation, and every mass scale riding that envelope inherits the offset at first power until the BCS screening is applied substrate-side.

---

### §W4-14. S100a-EPSLX-FOAM-SURVIVAL (quantum-foam-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-EPSLX-FOAM-SURVIVAL`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (foam-robustness of the multiplicity-bundle generation index)
**Agent**: `quantum-foam-theorist`
**Hypothesis**: The left-invariance-breaking finite-part deformation ε_LX either commutes with the foam Hamiltonian H_foam exactly ([H_foam, ε_LX]=0 — generation labels TOPOLOGICAL, foam-robust, QF-71 class) or leaves a residual scaling as N^{−α}, α>0 (GEOMETRIC, foam-fragile, QF-79 class) or O(1) N-independent (labels destroyed by foam).
**Plan reference**: `sessions/session-plan/session-100a-plan-w4.md` §W4-14 (H_foam Wheeler-√N model, ε_LX source branch, three-regime substitution chain source).

**Verdict**: **PASS** — C(N) = ‖[H_foam(N), ε_LX]‖₂ = **0 bit-exact** (max|matrix entry| = 0.0, not merely below tolerance) at **all four** N-ladder points, against commutator_tol = 1e-10. The generation index is **TOPOLOGICAL** on the multiplicity bundle — foam-ROBUST, QF-71 δn_foam = 0 class. Schema-v2 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` → composite PASS under the collapse rule. Dual-SHA: `audit_sha256=c46b1f6cf67d0fb60f52cc5499a04ad8206cabc3bbb6d57d7f80d54882c32fb1`, `content_sha256=69afbde7ca3875a238212f6d2337343f7cf3aac1b0f2d314355ac541954b6d89` (canonical line + companion row + 3-tuple row + source-branch row emitted via the race-safe `emit_verdict` MCP tool).

**ε_LX source branch (resolved at dispatch)**: Item 6 (`S100a-YUKAWA-OVERLAP-OFFDIAG`) LANDED (verdict INFO) → the **W2-form** is used: `computations/session-100a/s100a_yukawa_overlap_offdiag.npz`, key `eps_lx_block_phi0` = [[8.20652429, 0.40824829], [0.40824829, 8.20652429]] on the BDI pair t₁=(1,0) ↔ t₂=(0,1), plus the fiber profile `abs_w_phi` = 1/√6 = 0.40824829 (uniform) and `arg_w_M2_phi` = {π, +2π/3, −2π/3} at the three Z₃ center points φ ∈ {0, 2π/3, 4π/3}. The φ-dependent **phase** is the left-invariance breaking that lets ε_LX carry a generation index at all (W2 homogeneity wall, `permanent-results-registry.md`: left-invariance ⇒ multiplicity-scalar; ε_LX MUST break it). The pre-registered fallback `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` (NCG-INNER-FLUCT-EXTERNAL-NONLI / EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE, L_max=12, audit `b8487bc838683800…`) is SHA-pinned and verified present (CC-4) but **NOT USED**; the branch actually used is recorded in the verdict-line convention suffix `-EPSLX-SRC-ITEM6-W2FORM`.

**Results** (numbers first):

| N (foam cells) | h(N) [M_KK] (s53 anchor) | C_phys(N) [M_KK] | C_cf1(N) (leg L1 broken) | C_cf2(N) (leg L2 broken) |
|---:|---:|---:|---:|---:|
| 1 | 0.577350 (=1/√3, Λ_bare=M_KK²) | **0.000e+00** | 0.192450 | 0.527046 |
| 32 | 0.099760 (Λ_bare=M_P_12²) | **0.000e+00** | 0.033253 | 0.091068 |
| 1124.6 (N_Planck) | 0.016828 (Λ_bare=M_P_12²) | **0.000e+00** | 0.005609 | 0.015362 |
| 1349.74 (V_Haar) | 0.015715 (Λ_bare=M_KK²) | **0.000e+00** | 0.005238 | 0.014346 |

- **Gate observable**: max_N C(N) = 0.000000e+00 ≤ commutator_tol = 1e-10 → **PASS branch** of the pre-registered three-regime operator. α_phys = ∞ (no fit possible on exact zeros; the PASS branch keys on C ≤ tol at ALL N, not on a fit).
- **N^{−α} fit machinery (counterfactual liveness)**: CF-1 (generation-resolved foam, homogeneity-wall-breaking weights diag(O+|w|, O−|w|)): C_cf1 = 2|w|²h(N) = h(N)/3 exactly (analytic vs numerical spectral norm: max rel dev 2.0e-15), fit **α_cf1 = 0.501** (R² = 0.999945). CF-2 (Z₃ wormhole inter-cell hopping at full mean-field amplitude — the Carlip expanding/contracting-cell wormhole channel): prefactor k = ‖[𝟙⊗T_Z₃, ε_LX]‖ = 0.912871, fit **α_cf2 = 0.501** (R² = 0.999945). Both counterfactuals land in the INFO band (α > alpha_floor = 0.05) — the three-regime discriminator is **live**; the physical PASS is carried by the left-invariance structure, not by a dead diagnostic. Anchor-ladder Wheeler exponent α_h = 0.501 (pure law 1/2; 4-point LSQ on the s53 anchors).
- **Three-regime substitution chain (read-off with substituted numbers)**: Definition: C(N) = ‖[H_foam(N), ε_LX]‖₂ on the one-particle multiplicity bundle V = C²_gen ⊗ C³_φ (6-dim; for quadratic forms [H,ε]_Fock = Σ([A,B])_kl c†c, so the one-particle norm is faithful at every filling). Substitute (topological): [h(N)·O·𝟙_gen ⊗ D_cell, ε̂_j ⊗ P_j] = h(N)·O·ε̂_j ⊗ [D_cell, P_j] = 0 — leg L1: 𝟙_gen commutes with every ε̂_j (multiplicity-scalar foam, W2 homogeneity wall); leg L2: D_cell and P_j diagonal in the same cell basis (mean-field s53 pin). Simplify: C(N) = 0 ∀N ⇒ max_N C = 0 ≤ 1e-10. **Direction**: the pre-registered topological-branch vanishing HOLDS ⇒ sign_verdict = PASS; d(ln C)/d(ln N) is undefined on the zero function (the geometric branch's negative slope −α and the destroyed branch's zero slope are both empirically excluded — the counterfactuals exhibit the negative-slope INFO signature at α ≈ 0.501, confirming the sign read-off machinery). Destroyed-case note: C = O(1) flat would require a foam coupling that does not decay with N, contradicting the Wheeler-√N law Λ_eff = Λ_bare/N itself (Carlip CC-hiding IS the mechanism) — within the pinned foam class FAIL is structurally unreachable; the live discrimination is PASS vs INFO, and the two left-invariance legs decide PASS.
- **4-tuple**: (value=`max_C=0.0e+00_exact_4ptN_alpha_phys=inf_topological_QF71_cf1_alpha=0.501_cf2_alpha=0.501_z3_pinch_survival=0.6667_epslx=ITEM6-W2FORM`, scheme=`HFOAM-WHEELER-SQRTN-S43S53+EPSLX-W2FORM-ITEM6`, convention=`TOPOLOGICAL-VS-GEOMETRIC-MULTIPLICITY-INDEX-FOAM-ROBUSTNESS-EPSLX-SRC-ITEM6-W2FORM`, L_max=12).

**Cross-checks** (all PASS; asserted in-script):
- **CC-0**: npz `vol_su3_haar` ≡ canonical `Vol_SU3_Haar` = 8√3π⁴ = 1349.7399583 (rel dev 0.0).
- **CC-1**: φ₀-block reconstruction [[O,|w₀|],[|w₀|,O]] vs stored `eps_lx_block_phi0`: max dev 8.9e-15. Hermiticity of the full 6×6 ε_LX: 0.0.
- **CC-2**: all four s53 anchor strings substring-verified in the pinned `s53_foam_cc_output.txt` AND reconstructed from canonical constants via M_P_12 = (M_Pl_reduced²·M_KK⁸/Vol_SU3_Haar)^{1/10} = 7.2611e16 GeV (s53: 7.2611e16; ratio² = 0.955400 vs s53 9.5540e-01): per-anchor rel dev ≤ 1.4e-6 (rtol 2e-4). The anchor ladder mixes the two s53 bare-CC pins (M_KK² at N∈{1, V_Haar}, M_P_12² at N∈{32, 1124.6}); max wobble vs the single pure Wheeler law = 2.26% — irrelevant to the gate (C ≡ 0 at every h).
- **CC-3** (L_max=12 pin chain): s84 cache sector floors {0.83589351, 0.87297503, 1.24826413} for sectors {(1,0),(1,1),(3,0)} ≡ W2 npz `floors_lambda_min` (rel dev 0.0); eigenvalue counts {48,128,160} match.
- **CC-4**: S98-W3-1 fallback existence line present in pinned `s98_gate_verdicts.txt` (regex `^S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN: PASS`) — pinned alternate, NOT used.
- **CC-7** (zero is structural, not mean-field flattening): a sign-alternating per-cell Carlip foam (deterministic ± pattern {+1,−1,+1} on the φ-cells — expanding/contracting cells beyond the mean-field pin) STILL gives C = 0 bit-exact at all N. ANY generation-scalar, cell-diagonal foam commutes with ε_LX; the vanishing needs only the two legs, not equal cell weights.
- **CF-3** (worst-case pinching bound): the Z₃ phasor sum e^{iπ}+e^{i2π/3}+e^{−i2π/3} = −2 exactly (NOT zero — the W2 phase pattern is not a pure Z₃ character), so even a maximal Z₃-blind cell-average (N=1 pinching channel, strictly stronger than the pinned foam dynamics) preserves the between-generation coupling at |⟨w⟩|/|w| = 2/3 = 0.6667. The pinned foam DYNAMICS degrades it by exactly zero.

**MCP Pre-Compute Audit** (queries before script authorship; NOT PRE-CLOSED):
1. `search_knowledge("epsilon_LX generation multiplicity foam commutator")` → no prior [H_foam, ε_LX] closure; surfaced the PROVEN theorem "SM generation multiplicity IS the SU(3) Z₃-triality / Peter-Weyl multiplicity t=(p−q) mod 3", the S98-W3-1 existence-PASS verdict line, and S97-YUKAWA-FAMILY-DERIVE FAIL (multiplicity-scalar ⇒ democratic masses — the homogeneity wall this gate leans on).
2. `search_knowledge("foam survival topological generation index N scaling QF-79")` → no prior closure; surfaced the cautionary precedent "[NEW S46] Zak phase topological — RETRACTED S48 (index-tracking artifact)". Distinction recorded: the present PASS rests on an **exact operator identity** ([H_foam, ε_LX] = 0 from multiplicity-scalarity, verified bit-exact at the matrix level), not on numerical index tracking — structurally disjoint from the retracted S48 failure mode.
3. `trace_entity("homogeneity wall multiplicity-scalar left-invariance")` → no direct DB trace; registry grep supplies the wall verbatim (`permanent-results-registry.md` "(W2) Homogeneity wall — left-invariance ⇒ multiplicity-scalar representation; ε_LX MUST BREAK left-invariance on the multiplicity space").
4. `get_constant("Vol_SU3_Haar")` → S44, `s44_constants_corrected.py`, corrected 8880.93 → 1349.74 (Weyl integration formula); imported from canonical_constants (CC-0 verified).

**Substrate framing** (GEOMETRIC): the substrate IS the multiplicity bundle; the generation count is a label on the substrate's own Peter-Weyl multiplicity structure (triality class t = (p−q) mod 3), and the foam is the substrate's own short-distance reorganization into N Wheeler cells — not a container the generations live in. The reading flows D_K sector structure → multiplicity-bundle index (resolved by the left-invariance-breaking finite part ε_LX) → foam coarse-graining H_foam (built from left-invariant trace data, hence multiplicity-scalar) → [H_foam, ε_LX] = 0 → the observable 3-generation count. Because the foam's defining data (Haar cell volumes, a₀ trace moments) are left-invariant, the homogeneity wall that FORBADE an A_K-built generation hierarchy (S97 FAIL) here PROTECTS the generation index: the same multiplicity-scalarity that made the walls is what makes the foam generation-blind. This extends QF-71 (δn_foam = 0, occupation labels) to the between-generation deformation itself and sharpens the load-bearing geometry/topology dichotomy: the foam dissolves emergent spectral GEOMETRY (QF-79, ε_c ~ N^{−0.457}) but cannot touch the TOPOLOGICAL index sector — and the counterfactual probes show that even if either protection leg broke (generation-resolved weights, or Carlip wormhole hopping between cells), the residual would inherit h(N) ∝ N^{−1/2} and vanish in the continuum (foam-fragile-but-recovered, INFO), never the destroyed regime. Track-A/Track-B dual prior: PASS ⇒ posterior 0.9 to Track A (topological/foam-robust) per the pre-registered discriminator. Fermion-mass predictions riding the generation index are protected against Planck-scale metric fluctuations unconditionally within the pinned Wheeler-√N foam class. No new canonical constant (the result is a structural zero, QF-71 class); no carry-forward computation from this gate — the three-regime question is closed in-session.

**Output Artifacts**:
- `computations/session-100a/s100a_epslx_foam_survival.py` — producing script (contains `from canonical_constants import`, `print_verdict_payload`; OMP-8 cap before numpy per GPU_path=CPU-cap-OMP8 pin; deterministic, no RNG per random_seed=N/A pin)
- `computations/session-100a/s100a_epslx_foam_survival.npz` — full-float64 data (C_phys/C_cf1/C_cf2 ladders, α fits, ε_LX matrix, cross-check chain, dual-SHA)
- `computations/session-100a/s100a_epslx_foam_survival.png` — log-log C(N) vs N diagnostic (physical zero at display floor, counterfactual α≈0.501 lines, anchor law, tol boundary)
- `computations/session-100a/s100a_gate_verdicts.txt` — canonical PASS line + dual-SHA companion row + schema-v2 [SIGN] 3-tuple row + ε_LX source-branch row (via `emit_verdict`, race-safe)

---

### §W4-15. S100a-H0-SPINOR-FACTOR (kaluza-klein-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-H0-SPINOR-FACTOR`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (first-principles spinor normalization on the spectral triple's Clifford bundle)
**Agent**: `kaluza-klein-theorist`
**Hypothesis**: The empirical spinor-normalization factor M_Pl,eff/M_Pl,unred=3.92 derives first-principles as √16=4 from the d_spec=8 16-component spinor (Tr_spinor=2^{⌊8/2⌋}=16), the physical graviton retaining 4 of 64 Δ_12 components, reproducing 3.92 within ≈2% — the atlas-08 Q27 decisive gate; H₀=65.4 km/s/Mpc is contingent on this factor.
**Plan reference**: `sessions/session-plan/session-100a-plan-w4.md` §W4-15 (Clifford-dim + KK-surviving-block argument, √16 substitution chain, publication-precision-floored 2.5% boundary source).

**Output Artifacts**:

All four `output_artifacts:` entries verified on disk by content (greps run post-execution):

| Artifact | Path | Verification |
|:--|:--|:--|
| script | `computations/session-100a/s100a_h0_spinor_factor.py` (28,681 B) | `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # noqa: F401,F403,E402` ✓; `grep -cE 'print_verdict_payload'` → 3 ✓ |
| data | `computations/session-100a/s100a_h0_spinor_factor.npz` (12,379 B) | exists ✓ (exact num/den rational pairs + float64 mirrors + structural flags + gate metadata) |
| plot (optional) | `computations/session-100a/s100a_h0_spinor_factor.png` (82,632 B) | exists ✓ (16→4 spinor-reduction schematic: 64-cell Δ₁₂ census with surviving Δ₄ block; factor-vs-anchor band panel) |
| verdict line | `computations/session-100a/s100a_gate_verdicts.txt` | `grep -E '^S100a-H0-SPINOR-FACTOR:.* audit_sha256=[a-f0-9]{64}'` → 1 canonical PASS line ✓; dual-SHA companion row `# audit_sha256_short=39abff2d275ce8b5 content_sha256_short=e6928cadd8929c62` ✓; NO schema-v2 3-tuple row ([VERIFY] trigger — sign/magnitude/regime omitted per plan `schema_v2_3tuple_required: false`) ✓; 3 extra companion rows (derivation anchors / Class 8.3 / write-order) ✓ |

**MCP Pre-Compute Audit**:

Queried BEFORE computing (query-first discipline); no prior closure covers the gate — Q27 was LIVE-PENDING and queued to exactly this gate:

1. `search_knowledge("spinor normalization 3.92 M_Pl")` → Route D open channel (S58 workshop); **Q27 (H₀ spinor-factor) LIVE-PENDING since S58, QUEUED S100a with the S100a-queue annotation naming THIS gate** (atlas-08-freshness-S99); falsifier-watchlist H₀ row = "65.4 km/s/Mpc (if spinor factor resolved)". NOT pre-closed.
2. `search_knowledge("H0 65.4 spinor factor sqrt 16")` → Window-19 (atlas-05): "H₀ spinor-factor resolution … CONTINGENT … LIVE-PENDING; structural unresolved through S8x". Confirms first-principles derivation open.
3. `trace_entity("spinor normalization")` → S59 NORM-59: numerical N_factor = 3.920 measured on the max(p+q)=3 Peter-Weyl spectrum ("the session's strongest result"), 2% residual attributed to truncation; S81 `T3-BATCH-S59-SPINOR-NORM: INFO value=MIGRATED` is batch-canonical-hygiene (no-run-no-gate), NOT a physics resolution. PRE-CLOSED: NO.
4. `search_knowledge("s59_spinor_norm SIGMA-59 spinor")` → provenance edges: `s59_spinor_norm.py` → gate NORM-59; `s60_bayesian_h0.py` consumes `s59_spinor_norm.npz` (the H₀ = 65.4 downstream chain this gate grounds).
5. `list_constants("M_Pl|H0|spinor")` → `M_Pl_reduced = 2.435e18`, `M_Pl_unreduced = 1.2209e19` (S7, CODATA); **no prior spinor-factor constant existed** — `spinor_norm_factor_FW` is new (promoted post-verdict, see write-order below).

**Verdict**: **PASS**

```
S100a-H0-SPINOR-FACTOR: PASS -- value='factor_derived=4=sqrt16;Tr_spinor=16=2^4;Delta12=64=4x16;
  surviving=4of64;sqrt(4/64)=1/4-exact;rel=1/49=0.020408=2.041pct;boundary=0.025=1/40;
  PASS-iff-40<=49;margin=9/1960=0.004592;rel/boundary=40/49=0.8163;
  structural=EXACT-integer-mesh-not-fitted;Q27=RESOLVED;H0=65.4-grounded'
  scheme=dspec8-Clifford16+KK-surviving4+Sakharov-S44
  convention=STRUCTURAL-SQRT16-SPINOR-NORMALIZATION L_max=N/A
  audit_sha256=39abff2d275ce8b509b1312513560ffa6e1299995b3c3398e09b936713d51788
  content_sha256=e6928cadd8929c6229abb2ba4774a61a834f23db512cd7ebc780688b22e90296 schema_version=S84+
```

(Emitted via the race-safe `emit_verdict` knowledge-MCP tool, 5 rows, sig_5 unique. Scheme string is the plan's Wave-4 machinery-enumeration abbreviated form `dspec8-Clifford16+KK-surviving4+Sakharov-S44` — space-free encoding of the pinned scheme "d_spec=8 Clifford(R^8) spinor dim (16) + KK-surviving-block (4) + Sakharov induced-gravity (S44 C8/C9)" for verdict-line field-grammar safety; honest-disclosure note, no convention change.)

**Results**:

*Numbers first (all gate arithmetic EXACT — `fractions.Fraction` + `math.isqrt`; no float enters the comparison):*

| Quantity | Exact value | Float |
|:--|:--|:--|
| Tr_spinor = 2^{⌊8/2⌋} | **16** | — |
| dim(Δ₄) = 2^{⌊4/2⌋} | **4** | — |
| dim(Δ₁₂) = 2^{⌊12/2⌋} | **64 = 4×16** (multiplicativity TRUE) | — |
| surviving/total | 4/64 = **1/16** | 0.0625 |
| M_Pl^phys/M_Pl^spec = √(4/64) | **1/4** (exact rational root) | 0.25 |
| **factor_derived = M_Pl,eff/M_Pl,unred** | **4 = √16** (EXACT integer) | 4.000 |
| empirical anchor (atlas-08 Q27 / S58, 3 sig figs) | 392/100 = 98/25 | 3.92 |
| **rel = \|4 − 3.92\|/3.92** | **1/49** | 0.020408 → **2.041%** (4 s.f.) |
| strict PASS boundary (Class 8.3 floored) | 1/40 | 0.025 (2.5%) |
| PASS condition | 1/49 ≤ 1/40 ⟺ **40 ≤ 49** | TRUE |
| margin = boundary − rel | **9/1960** | 0.004592 |
| rel/boundary | **40/49** | 0.8163 |
| implied a₂ deficit = 1−(3.92/4)² | **99/2500** | 3.96% |

4-tuple: `(value=<payload>, scheme=dspec8-Clifford16+KK-surviving4+Sakharov-S44, convention=STRUCTURAL-SQRT16-SPINOR-NORMALIZATION, L_max=N/A)`. Structural identity flags: factor²==Tr_spinor TRUE; isqrt-exact TRUE; 64/4==16 (Sakharov) TRUE; multiplicativity TRUE — **ALL TRUE**.

*Derivation (explicit dimensional reduction; every step on the integer mesh):*

The bundle structure is P = M⁴ × K with K = SU(3), dim K = 8 = d_spec, total D = 12. The 12D Dirac operator on the product is D₁₂ = D₄ ⊗ 1₁₆ + γ₅ ⊗ D_K acting on Δ₁₂ = Δ₄ ⊗ Δ₈, with the irreducible Clifford module dimensions

&nbsp;&nbsp;(1) dim Δ₈ = 2^{⌊8/2⌋} = 16 (Clifford(ℝ⁸)), dim Δ₄ = 2^{⌊4/2⌋} = 4, dim Δ₁₂ = 2^{⌊12/2⌋} = 64 = 4·16

(multiplicativity of spinor modules under the even-dimensional split — verified exactly). The spectral side carries the FULL internal multiplicity: the heat-kernel product factorization (Paper 33 / S53) a_n^{M×K} = Σ_{i+j=n} a_i^M·a_j^K places the 4D Einstein-Hilbert coefficient in the a₂^M·a₀^K cross-term, and

&nbsp;&nbsp;(2) a₀^K ∝ Tr_{Δ₈}(1)·Vol(K) = 16·Vol(K),

so the spectral-action identification of 1/(16πG) inherits the factor 16 multiplicatively. Zeta-side confirmation (S87, `s87-d-eff-derivation-connes.md:176`): the leading CM-1995 dim-spectrum pole residue Res_{s=8} ζ_D(s) = (Vol(SU(3))/(2π)⁸)·16 carries the 16 = 2^{[8/2]} explicitly (context value √3/(2π⁴) = 8.8906e-3 with the canonical Vol_SU3_Haar = 1349.74). The PHYSICAL graviton is the metric zero mode h_μν: √g R₄ carries NO internal spinor index, and the on-shell-projected gravitational trace retains exactly one 4D Dirac block — 4 of the 64 Δ₁₂ components (Route D, `session-58-volovik-baptista-workshop.md:528`; Δ₁₂ = M₈ₓ₈(ℂ)). Therefore

&nbsp;&nbsp;(3) M_Pl^{phys}/M_Pl^{spec} = √(surviving/total) = √(4/64) = √(1/16) = 1/4 (exact) ⇒ M_Pl,eff/M_Pl,unred = √16 = 4.

Sakharov induced-gravity cross-reading (S44 C8/C9; S58 workshop Q3, line 712): G⁻¹ ∝ Tr(1_spinor); restricting 64 → 4 shifts G_N by 64/4 = 16, hence M_Pl by √16 = 4 — the same factor from the induced-gravity side, with no cross-term dominance assumption beyond the a₂^M·a₀^K identification of the EH term. Every quantity in (1)–(3) is a pinned integer or an exact rational root of pinned integers: **no scan, no fit, no float — the factor is structurally √16, not fitted.**

*Substitution chain (plan §W4-15 item 7, executed with substituted numbers):*

```
Definition 1: d_spec = 8                                  [SU(3) triple; CM-1995 leading pole s=8, S87]
Definition 2: Tr_spinor = 2^floor(8/2) = 2^4 = 16          [Clifford(R^8); Res_{s=8} carries 16, S87:176]
Definition 3: dim(Δ_4) = 4; Δ_12 = M_8x8(C) = 64 comps, 4 survive   [Route D, S58:528]
Definition 4: M_Pl^spec uses Tr=16 via a_2^M·a_0^K; physical graviton = on-shell Δ_4 block
Substitute:   M_Pl^phys/M_Pl^spec = sqrt(4/64) = sqrt(1/16)
Simplify:     sqrt(1/16) = 1/4                                                  [EXACT]
Invert:       M_Pl,eff/M_Pl,unred = 4 = sqrt(16)            [EXACT structural integer]
Substitute:   rel = |4 − 3.92|/3.92 = 0.08/3.92 = 8/392
Simplify:     rel = 1/49 = 0.020408 = 2.041%                                    [EXACT RATIONAL]
Direction:    rel = 1/49 ≤ 1/40 = 0.025  ⟺  40 ≤ 49  TRUE  ⇒  PASS
Conclusion:   factor IS sqrt(16)=4 first-principles; reproduces 3.92 to 2.041%,
              inside the 2.5% publication-precision tolerance ⇒ VERIFY PASS.
```

*Cross-checks:*

1. **Sage-exact structural confirmation** (Sage MCP, sagecell backend, exact QQ arithmetic): `2^floor(8/2)=16`; `2^floor(12/2)=64=4*16` TRUE; `sqrt(QQ(4)/QQ(64))=1/4` exact; `sqrt(16)==4` TRUE; `rel = 1/49`; `boundary = 1/40`; PASS (40≤49) TRUE; `margin = 9/1960 = 0.00459184`; `rel/boundary = 40/49 = 0.816327`; implied a₂ deficit `99/2500 = 0.0396`. Mirrored in-script with `Fraction`/`isqrt` (independent arithmetic path, same results bit-exact).
2. **Truncation-residual closure with S59 NORM-59**: the anchor 3.92 is the S59 numerical N_factor = 3.9196 measured on the max(p+q)=3 Peter-Weyl spectrum. The a₂-level deficit implied by 3.92 vs the structural 4 is 1−(3.92/4)² = 99/2500 = 3.96%, matching S59's direct truncation-deficit estimate (~4.1% of a₂ missing from p+q ≥ 4 sectors) in scale AND sign — all ω_n > 0, so higher sectors push N monotonically UP toward 4: the 2% residual is a truncation artifact converging TOWARD the structural value, not a substrate-physics offset away from it.
3. **Class 8.3 publication-precision floor**: the empirical 3.92 is a 3-sig-fig number (true value in [3.915, 3.925]); a naive 2.0% strict boundary would FAIL 2.041% on the anchor's own rounding, not on physics — the pre-registered 2.5% boundary is the precision-floored choice (plan §W4-15 `strict_PASS_boundary` comment). factor_derived = 4 EXACT; rel published at 4 sig figs (2.041%).
4. **Dimensional consistency**: the factor is a dimensionless ratio of two Planck masses; rel is dimensionless; the entire gate is regulator-free (no a_n citation, no Seeley-DeWitt regulator pin applies — spinor-dimension argument only, per the Wave-4 machinery-enumeration row).

*Dual-prior discriminator (plan §W4-15)*: PASS at rel ≤ 2.5% with factor structurally √16 ⇒ posterior 0.95 to **Track A (STRUCTURAL √16)**; Track B (residual-scheme) reduced to 0.05.

*atlas-08 Q27 resolution state*: **RESOLVED** (PASS). The spinor-normalization factor is no longer an empirical pattern-match — it is the Clifford-dimension root √16 = 4 derived from the substrate's spinor bundle. Consequences per the plan's PASS_meaning + Wave 4 → Wave 5 decision table: **H₀ = 65.4 km/s/Mpc is structurally grounded** (the S59/S60 corrected spectral-action chain's normalization step is now first-principles; no free spinor-normalization parameter remains in the Friedmann derivation's normalization) → **FLAGSHIP promotion**; mack-cosmic-bridge lands the H₀ observational row (sole-writer surface). Capstone-hygiene routing: Q2 fires (this gate changes the §7 falsifier-anchor H₀ row status LIVE-PENDING → grounded) → route the §7 row update + `falsifier-master-inventory.md` H₀ row to `mack-cosmic-bridge` via `session-100a-housekeeping.md` per `.claude/rules/capstone-hygiene-gate.md`.

*Canonical write-order (math-scripts §"Canonical Write-Order", executed in order)*: **(1)** verdict line emitted (audit_sha256 `39abff2d…`, above); **(2)** `spinor_norm_factor_FW = 4.0` promoted to `canonical_constants.py` SECTION E with PROVENANCE via `update_constant` (session S100a, source `s100a_h0_spinor_factor.py`, gate `S100a-H0-SPINOR-FACTOR`) — single-call FIX-IN-SESSION, no derivation ambiguity; **(3)** inventory row = mack's surface (routed above, NOT written here). The plan-pinned empirical anchor 3.92 remains a documented `# (local)` framework-empirical literal in the script with the atlas-08 Q27 / S58 cite (it is an input anchor, not this gate's produced value).

*Substrate framing (GEOMETRIC)*: the factor is a property of the fabric's Clifford structure, not an excitation. D_K acts on H_K = (spinor bundle) ⊗ (rep space); at d_spec = 8 the spinor bundle IS Δ₈ = ℂ¹⁶ → the full spectral gravitational coupling (the a₂^M·a₀^K Einstein-Hilbert cross-term of the second total spectral moment, per a_n^{M×K} = Σ_{i+j=n} a_i^M·a_j^K) traces over all 16 components → the physical 4D graviton retains only the 4 KK-surviving components → M_Pl,eff/M_Pl,unred = √16 = 4 → H₀. The Planck mass is NOT a fundamental input: it is a spectral moment of D_K, and √16 is how the FULL substrate spinor multiplicity projects onto the physical on-shell graviton. The empirical 3.92 is the lab's shadow of the substrate's Clifford structure (truncation-dressed at max(p+q)=3); the derivation reads FROM the spinor bundle TOWARD H₀ — the substrate fixing a cosmological observable through its own internal spinor geometry.

---

## Wave 4 Synthesis (team-lead)

**Date**: 2026-06-06. **Gates**: 4 (2 PASS, 2 INFO — both INFOs pre-registered as the gates' design outcomes). Verdict lines with full 64-char dual-SHA closures in `computations/session-100a/s100a_gate_verdicts.txt`; W4-12/W4-14 carry schema-v2 `[SIGN]` 3-tuples; W4-13 `[AUDIT]` and W4-15 `[VERIFY]` correctly omit them. All artifacts content-verified.

### 1. The SCALE axis is now EMPIRICALLY layered (W4-12 ∧ W4-13)

**W4-12 (INFO-by-design, Track A 0.97)**: the Spectral-Moment Decoupling Theorem (S75 W2-E) acquires its observable-layer empirical face — fermion mass RATIOS are functional-INDEPENDENT at max cross-scheme deviation **2.813e-16** (≤ 1e-12 tol, with an injected-leak control proving the test sensitive at 2.0e-6), while the per-sector SCALE moves by **D_scale = 60.64** between the zeta (FULL, a₄^{ζ}/a₂^{ζ} = 0.486542) and cutoff (SCHEMATIC f*-moments, f₄/f₂ = 29.988) functionals. **The §IV bosonic/fermionic layer-separation moves ASSERTED → EMPIRICAL.** Level-pin discipline POSITIVE profile executed in full (CLASS=SCHEMATIC cutoff leg, `-SCHEMATIC` convention suffix, `# tier_pin=TIER-2` companion row, cross-class disclosure paragraph).

**W4-13 (INFO, sole pre-registered outcome)**: M₀'s absolute normalization is anchored to the |s(h)|² fiber-embedding mode SHARED with m_H (branch a) — so it inherits the Higgs-sector residual LINEARLY: **δM₀/M₀ ∈ [+5.356%, +7.114%]** (exact rationals 67/1251, 89/1251), with the BCS −7% correction (S62) applied to m_H only, not yet to M₀. Composition with W4-12: Item 13's over-prediction question lives ENTIRELY on the scheme-dependent SCALE axis; the ratios it cannot touch are the same ratios W4-12 proved functional-independent. The honest-scope §7 ledger row content is pinned in §W4-13 for the mack session-close batch.

### 2. The generation index is foam-protected by the wall that forbade its derivation (W4-14)

**W4-14 (PASS, topological QF-71 class, Track A 0.9)**: `‖[H_foam(N), ε_LX]‖ = 0.0 BIT-EXACT` at all four Wheeler-√N ladder points (N ∈ {1, 32, 1124.6, 1349.74}), against commutator_tol = 1e-10 — with live counterfactual machinery (leg-broken variants fit α = 0.501, R² = 0.99995, proving the INFO read-off would have fired had the zero been approximate). The mechanism is structural, two independent legs: (L1) H_foam is built from left-invariant data, hence multiplicity-scalar by the W2 homogeneity wall — generation-blind; (L2) mean-field Wheeler cells are diagonal in ε_LX's fiber basis. Even sign-alternating Carlip ± cells commute (CC-7). **The S97 wall that FORBADE an A_K-built generation hierarchy is precisely what PROTECTS the generation index from the foam** — one structure, two faces. ε_LX source branch: ITEM6-W2-FORM (W2-2 landed; recorded in the convention suffix; S98 fallback pinned, unused). Distinct from the retracted S48 Zak-phase claim: exact operator identity, not index tracking.

### 3. Q27 falls: the spinor factor is √16 (W4-15)

**W4-15 (PASS)**: M_Pl,eff/M_Pl,unred = 3.92 derives first-principles as **√16 = 4 EXACT** — Tr_spinor = 2^⌊8/2⌋ = 16 (Clifford(ℝ⁸); Res_{s=8} ζ_D carries the 16) × surviving-block 4-of-64 Δ₁₂ (Route D) via √(4/64) = 1/4. Agreement: rel = 1/49 = 2.041% ≤ 1/40 = 2.5% (publication-precision-floored boundary; PASS ⟺ 40 ≤ 49, Sage-exact). Consistency closure: the implied a₂ deficit 1 − (3.92/4)² = 3.96% matches the S59 PW-truncation deficit (~4.1% at max(p+q)=3) in scale AND sign — the empirical 3.92 converges TOWARD 4 as truncation lifts. **atlas-08 Q27 RESOLVED; H₀ = 65.4 km/s/Mpc structurally grounded; FLAGSHIP promotion fires**; `spinor_norm_factor_FW = 4.0` canonical.

### 4. Downstream implications

| Stream | Effect of W4 | Action |
|:-------|:-------------|:-------|
| §IV layer-separation | ASSERTED → EMPIRICAL (ratio invariance 2.8e-16 vs scale sensitivity 61.6×) | Constraint-map row below; §IV ledger text inherits the W2-3 FAIL boundary too (overlap-diagonal ladder ≠ Casimir-graded) |
| Capstone §7 honest-scope (M₀) | absolute-normalization band [+5.36%, +7.11%] documented | mack-cosmic-bridge lands the §7 scope row at session close (capstone-hygiene Q3) |
| 3-generation index | foam-robust by exact operator identity | foam-protection theorem registration → housekeeping §B CF-S101-HK-1 (registry-landing gate; mirrored below) |
| atlas-08 Q27 / H₀ | RESOLVED; H₀ = 65.4 grounded; FLAGSHIP | mack lands the §7 H₀ row + FLAGSHIP promotion at session close (Q2); orchestrator marks atlas-08 Q27 RESOLVED in the session-close register batch |

> **§IV ledger-text disposition (W-2 workshop, 2026-06-07 — `workshops/s100a-w2-mass-functional-counting-workshop.md` R2-B B-item 8, routed to this designated-writer surface)**: the W2-3 FAIL boundary this table's row-1 ledger text inherits is counting-class-scoped, three cells — (a) extensive block-sum face: CLOSED, rung-1 sign-inversion (W = −4.66; counting-class mismatch, adjudicated s100a-w2 workshop); (b) normalized-class floor truncation (n→1): CLOSED as a widening-band candidate (W = 12.5629 bit-identical across W2-3/W2-4; van-Hove fold-compression mechanism), RETAINED as ordering chain + metric machinery (its τ = (1,0) output is one of the workshop verdict's two [SIGN] chains; its star closed form d = 1/t is the route-fork-closure theorem the S101 gate uses); (c) normalized-class full-state members (flat/weighted means): OPEN — the amended S101 gate (per-mode face measured 1.0% below the band floor). The ledger mirror must not compress "overlap diagonal" into "all diagonal functionals"; no verdict is re-adjudicated.

### 5. Wave classification

**Framework-strengthening on all four gates** — unusual for this project's constraint-map-dominated sessions: two exact structural identities (the foam commutator zero; the √16 factor), one empirical promotion of a standing theorem (decoupling), one honest-scope band (M₀). The wave's composite picture: the substrate's mass-ratio sector is functional-independent, foam-protected, and Casimir-mis-graded at the overlap diagonal (per W2-3) — the SHAPE question sharpens while the SCALE question is now cleanly quarantined to the scheme-dependent axis.

### Effected In-Session (NON-MATH — team-lead orchestrator)

- [x] `m_H_FW_KK_threshold = 131.8` + `m_H_FW_tree = 134.0` PROVENANCE promotions (write-order step 2, FIX-IN-SESSION per plan) — effected in-gate by W4-13 via `update_constant`; orchestrator import-verified — `computations/_shared/canonical_constants.py` SECTION E — `d00bbb3794ed207c`
- [x] `spinor_norm_factor_FW = 4.0` PROVENANCE promotion — effected in-gate by W4-15 via `update_constant`; orchestrator import-verified — `computations/_shared/canonical_constants.py:674` — `39abff2d275ce8b5`
- [x] Capstone §7 surface items (W4-13 honest-scope row; W4-15 H₀ row + FLAGSHIP promotion) consolidated into the session-close `mack-cosmic-bridge` sole-writer dispatch queue (executes this session before STOP; tracked task #26) — per `feedback_mack-bridge-role.md` + capstone-hygiene Q2/Q3
- [x] atlas-08 Q27 → RESOLVED register edit queued to the session-close register batch (orchestrator-direct; batched with the W6 register touches) — tracked task #26
- [x] Foam-protection theorem registration routed to housekeeping §B as CF-S101-HK-1 (Q2 mechanical promotion requiring a registry-landing compute; 4-field spec mirrored below) — `sessions/session-100a/session-100a-housekeeping.md §B`
- [x] Orchestrator-direct presentation patches: none required (all four sections landed complete; zero must_contain misses; the W4-15 agent's mtime-conflict retry self-resolved cleanly)

## Carry-Forward Computations

### CF-S101-HK-1 — foam-protection theorem registry landing [Q2-hygiene]

> **Routing note**: Q2-class mechanical promotion per `Investigating-Workshops.md §"Q2"`. Identified at S100a W4 wave-synthesis. NOT a workshop. Canonical entry: `sessions/session-100a/session-100a-housekeeping.md §B`; this block is the WP mirror.

> **Why not §A (fix-in-session)**: the registry landing requires a single-shot bridge-landing script (build_promotion_text → write_atomic_with_fsync → re_read+verify → emit) per `registry-landing.md §"Bridge-Landing Script Architecture"` — a compute artifact with its own verdict line, not an orchestrator text edit.

1. **What**: Land the W4-14 exact operator identity (`[H_foam(N), ε_LX] = 0` ∀N in the Wheeler-√N class; two structural legs L1/L2; generation index topological, QF-71 class) as a registered structural-theorem entry in `sessions/permanent-results-registry.md`, with the S97-wall-as-protector reading and the counterfactual-machinery evidence.
2. **Inputs**: `computations/session-100a/s100a_epslx_foam_survival.npz` (audit `c46b1f6cf67d0fb6`); §W4-14 WP section; `computations/_bridge_landing_script_template.py`.
3. **Gate**: `S101-FOAM-PROTECTION-REGISTRY-LANDING` — PASS iff the registry section matches the built promotion text post-fsync re-read (single-shot AFTER pattern) AND the verdict line lands with dual-SHA; FAIL emits once per `mechanical-closure-discipline.md`.
4. **Effort**: ~0.3 wave-equivalents (landing script + verdict + registry text; no new physics compute).

> **Addendum (2026-06-07, `/rclab-investigate` consolidation)**: one genuine compute carry-forward below surfaced at investigation (`workshops/_seed-w4.md`) — the W4-13 closure mechanism the WP itself defers ("until that computation exists"). The W4-15 H₀ truncation-consistency successor is scheduled as a solo review (`session-100a-workshop-schedule.md` S-2), whose conditional output may add an H₀ recompute gate spec. Note for the CF-S101-HK-1 landing text above: scope the protected operator-FORM class explicitly (legs L1/L2; CC-7 — the commutator zero is independent of specific |w| entries) so a W-3-carrier-driven ε_LX revision cannot orphan the registered theorem.

### CF-W4-1 — M₀-side BCS screening compute (the W4-13 closure mechanism) [Q-other — solo compute follow-up]

1. **What**: Apply the S62 BCS anomalous-self-energy screening (Σ_anom(q² = M_KK²) correction to g_3(M_KK); THRESHOLD-62 / HIGGS-BCS-THRESHOLD-62 — the documented mechanism closing m_H 134 → ~125, applied to date to m_H ONLY, never to M₀^{sector}) to the |s(h)|²-anchored M₀^{sector} and recompute the inherited residual band (currently δM₀/M₀ ∈ [+5.356%, +7.114%], exact rationals 67/1251, 89/1251).
2. **Inputs**: `computations/session-100a/s100a_m0_mh_inheritance.npz` (exact 67/1251, 89/1251; audit `d00bbb3794ed207c`); S62 `s62_higgs_bcs_threshold.py` machinery; canonical `m_H_FW_KK_threshold = 131.8` / `m_H_FW_tree = 134.0` / `m_H_obs = 125.1`; Item-6 overlap npz (`s100a_yukawa_overlap_offdiag.npz`, audit `871573da729c5972`).
3. **Gate**: `S101-M0-BCS-SCREENING` — PASS iff the screened band shrinks toward 0 in step with the m_H closure (exact band threshold pre-registered at S101 plan-freeze; the direction claim requires the explicit substitution chain per `math-scripts.md`). On landing, update the pinned capstone §7 honest-scope row (mack-cosmic-bridge sole-writer surface).
4. **Effort**: ~1 gate.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-06 | §IV bosonic/fermionic layer-separation | ASSERTED (S75 theorem layer) | EMPIRICAL — ratios functional-independent (2.8e-16), scale scheme-dependent (61.6×) | S100a-M0-FUNCTIONAL-SENSITIVITY INFO-by-design (`2993dbf63fcb25d9`) |
| 2026-06-06 | M₀ absolute normalization | provenance untraced | |s(h)|²-anchored (branch a); inherits m_H residual linearly, band [+5.356%, +7.114%]; BCS −7% applied to m_H only | S100a-M0-MH-INHERITANCE INFO (`d00bbb3794ed207c`) |
| 2026-06-06 | 3-generation index vs foam | foam-robustness UNTESTED (QF-71 vs QF-79 open) | TOPOLOGICAL — [H_foam, ε_LX] = 0 exact; S97 homogeneity wall is the protector; destroyed-regime unreachable in Wheeler class | S100a-EPSLX-FOAM-SURVIVAL PASS (`c46b1f6cf67d0fb6`) |
| 2026-06-06 | atlas-08 Q27 (√16 spinor factor) | LIVE-PENDING (empirical 3.92 underived) | RESOLVED — factor = √16 = 4 exact; rel 2.04% ≤ 2.5%; residual = PW-truncation deficit (S59 scale+sign match); H₀ = 65.4 grounded, FLAGSHIP | S100a-H0-SPINOR-FACTOR PASS (`39abff2d275ce8b5`) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| S100a-M0-FUNCTIONAL-SENSITIVITY | `s100a_m0_functional_sensitivity.py` | `s100a_m0_functional_sensitivity.npz` | `s100a_m0_functional_sensitivity.png` | — | 42.1 KB / 30.2 KB / 98.5 KB |
| S100a-M0-MH-INHERITANCE | `s100a_m0_mh_inheritance.py` | `s100a_m0_mh_inheritance.npz` | `s100a_m0_mh_inheritance.png` | — | ~25 KB / npz / png |
| S100a-EPSLX-FOAM-SURVIVAL | `s100a_epslx_foam_survival.py` | `s100a_epslx_foam_survival.npz` | `s100a_epslx_foam_survival.png` | — | 41.5 KB / 15.9 KB / 129.5 KB |
| S100a-H0-SPINOR-FACTOR | `s100a_h0_spinor_factor.py` | `s100a_h0_spinor_factor.npz` | `s100a_h0_spinor_factor.png` | — | py / npz / png |

(All four gates emit to `computations/session-100a/s100a_gate_verdicts.txt` via the race-safe `emit_verdict` MCP tool; sig_5 uniqueness verified across the file.)
