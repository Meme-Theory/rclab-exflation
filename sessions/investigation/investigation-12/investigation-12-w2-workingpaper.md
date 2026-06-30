# Investigation 12 Wave 2 — NCG bridge: factorization bounds, pole-audit, Krein, FWD-C1 (Results Working Paper)

**Investigation**: 12 | **Wave**: 2 | **Plan**: investigation-12-plan-w2.md | **Theme**: van den Dungen topology/analysis boundary — the Kasparov product factorizes the K-HOMOLOGY class (topology: indices, mass ordering, c_s²=0, w_a=0), NOT the spectral-action MOMENTS (a₀, a₂, a₄ → Λ, G_N, Yang-Mills). Five gates (3 compute + 2 solo, all `van-den-dungen-bridge-theorist`) bound what the framework's "computed" numbers actually are. Verdict-line ledger: `computations/investigation-12/inv12_gate_verdicts.txt`.

## Gate Sections

### §W2-1. INV12-W2-1-S-CROSS-OFF-JENSEN-BOUND (van-den-dungen-bridge-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W2-1-S-CROSS-OFF-JENSEN-BOUND`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (O'Neill A,T → Gilkey a₂(D_total²) product-correction; off-Jensen cross-term leak bound)
**Agent**: `van-den-dungen-bridge-theorist`
**Hypothesis**: At one ridge-confined off-Jensen point, the spectral-action cross-term ratio `|S_cross|/S_base` (the O'Neill A²/T² remainder the additive heat-kernel factorization drops) is bounded small (< 10⁻²), so `a₂(D_total)=a₀(D_M)a₂(D_K)+a₂(D_M)a₀(D_K)` holds to a quantified O(δ²) leak along the physical trajectory.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source).

**Output Artifacts** (closure-verification checklist; per the gate-block `output_artifacts:` YAML):

1. **Script** `computations/investigation-12/inv12_w2_1_s_cross_off_jensen_bound.py` (52,204 bytes). `grep -E 'from canonical_constants import|print_verdict_payload'`:
   - `from canonical_constants import *` + `from canonical_constants import (` ✓ (2 matches)
   - `def print_verdict_payload(` ✓ (line 281)
2. **Data** `computations/investigation-12/inv12_w2_1_s_cross_off_jensen_bound.npz` (14,144 bytes) — present. Holds the δ-scan arrays (`delta_grid`, `A_sq_of_delta`, `T_sq_of_delta`, `ratio_of_delta`, `R_K_of_delta`), the on-Jensen baseline (`A_on=0.0`, `T_on=0.0`, `conn_norm_on=0.0`), the off-Jensen-point scalars (`A_sq_phys=3.2235e-07`, `T_sq_phys=7.8125e-04`, `ratio_phys=3.872728e-04`, `c_geom=0.154909`), and the verdict scalars (`s61_exact_recovered=True`, `monotone_increasing=True`, `sign_direction_ok=True`).
3. **Plot** `computations/investigation-12/inv12_w2_1_s_cross_off_jensen_bound.png` (235,837 bytes) — present. 4-panel: (A) `|S_cross|/S_base` vs δ growing quadratically from EXACTLY 0 at δ=0; (B) log-log slope-2 confirmation; (C) `||A||²`, `||T||²` vs δ (both =0 EXACT at δ=0); (D) diagnostic summary.
4. **Verdict line** `computations/investigation-12/inv12_gate_verdicts.txt` matches `^INV12-W2-1-S-CROSS-OFF-JENSEN-BOUND:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + the schema-v2 3-tuple row ✓ ([SIGN]) + 3 regulator_pin/tier_pin/scope extra rows.
5. **This wp_section** — present (Status/Verdict/Output Artifacts/MCP Pre-Compute Audit blocks populated).

**MCP Pre-Compute Audit** (queries run BEFORE writing the script; query-first discipline per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `trace_entity("A-TENSOR-61")` | **A=T=0 EXACT** on the product (Jensen) metric; empirically 0.47% cross-terms at numeric floor; additive rule `a₂(D_total)=a₀(D_M)a₂(D_K)+a₂(D_M)a₀(D_K)` holds when A=T=0; `R_K(fold)=−2.018 M_KK²` (Koszul, S61); Gilkey a₄ cross `∝ Tr(A·A)` (Thm 4.8.16). **This IS the δ=0 baseline.** |
| `search_knowledge("off-Jensen Hessian 35 negative eigenvalues ridge restoring potential")` | **S76 W2-J** `Off_Jensen_Hessian_35_35_Negative` (35/35 negative SA-Hessian evals, Jensen=ridge); S77-C5 confirms ridge persists at τ=1.614 (modulus confined); moduli basis `v_J=(2,−2,1); n_V=(1,3,4)`. |
| `get_constant("a_2_FW_zeta")` | **2776.165389** (S88) = a₂(D_K), the SU(3) fiber zeta moment = S_base. |
| `search_knowledge("O'Neill tensor A T submersion Gilkey a2 cross-term S_cross spectral action")` | `S_cross = S_total − S_base − S_fiber` (S63 VdD-Hawking; session-96-plan-w1); Gilkey a₂ remainder `a₂(D_total²)=[a₀(D_M)a₂(D_K)+a₂(D_M)a₀(D_K)]+ΔA,T`; Baptista Paper 13 eq 3.4 `R_P=R_M+R_K−|A|²−|S|²`. |

**NOT PRE-CLOSED** — A-TENSOR-61 is the *on-Jensen* A=T=0 exactness; this gate is the distinct *off-Jensen displacement* bound (the leak at δ>0). **Scope distinction flagged**: S96-W1-ONEILL-NONFLAT (s96_w1_oneill_nonflat.py) computed the same Gilkey machinery but parameterized the off-Jensen excursion by the principal-bundle **connection curvature** `||F_ω||` (base-bundling channel, Reading A = Hubble scale); THIS gate parameterizes it by the **35D moduli displacement** δ within the Jensen ridge (S76 W2-J). The two are complementary channels; the S96 W1 result does not cover the moduli direction, so this gate is what discharges the on-Jensen-only conditional for the moduli excursion specifically.

**Verdict**: **PASS** — `value='|S_cross|/S_base=3.872728e-04@delta=0.05_ridge_confined;PASS_ceiling=1e-2;result=PASS;c_geom=ratio/delta^2=0.1549(threshold_crossing_c_geom=4.0_delta=0.05);||A||^2=3.2235e-07;||T||^2=7.8125e-04;R_K_offJensen=-2.0181;on_Jensen_recovery_ratio(delta=0)=0.00e+00(A=T=0_EXACT_A-TENSOR-61=True);||A||^2(Jensen)=0.00e+00;||T||^2(Jensen)=0.00e+00;monotone_from_0=True;S_base=a2_DK=2776.17;S_fiber=103554.67;on_Jensen_only_conditional_DISCHARGED_for_G_N_n_s=True;band_tag=PASS_...'` scheme=FW convention=RATIO L_max=12. audit_sha256 `538981c193503f8e2683fb1a102b1dc7658beb841e2c66133508f272743e16db`, content_sha256 `9c535ad03b70c73b09e4096e08adf4325fdb06727cad57c4d54a0990245f017e`. 4-tuple `(value=3.872728e-04, scheme=FW, convention=RATIO, L_max=12)`. [SIGN] 3-tuple: **sign=PASS magnitude=PASS regime=VALID**.

**Results**:

**Headline**: at the ridge-confined off-Jensen point δ=0.05, `|S_cross|/S_base = 3.873×10⁻⁴`, **25.8× below** the 10⁻² PASS threshold (Sage-QQ exact margin = 9.613×10⁻³). The O'Neill remainder the additive Kasparov-factorization drops is a quantified O(δ²) leak; G_N, Einstein-Hilbert, and the n_s machinery inherit at most an O(δ²) A/T correction along the physical trajectory. **The on-Jensen-only conditional (U-1) is discharged to a quantified small bound for the moduli direction.**

**On-Jensen δ→0 recovery (A-TENSOR-61 cross-check)**: `||A||²(Jensen)=0.0`, `||T||²(Jensen)=0.0`, Ehresmann connection norm `=0.0` ⇒ `|S_cross|/S_base(δ=0)=0.0` to machine ε (`s61_exact_recovered=True`). The construction recovers A-TENSOR-61 by construction: on the block-diagonal Jensen metric the base-fiber connection vanishes identically, so A=T=0 EXACTLY.

**Full substitution chain with substituted numbers** (Sage-verified, the script re-derives it numerically):
- **Step 1 (defs)**: A-TENSOR-61: A=T=0 EXACT on Jensen (block-diagonal metric ⇒ base-fiber connection = 0). Gilkey a₂ O'Neill remainder `Δ_{A,T}=c_A|A|²+c_T|T|²`, =0 iff A=T=0. `S_cross=S_total−S_base−S_fiber`. S76 W2-J: 35/35 negative Hessian ⇒ Jensen=ridge ⇒ `|A|²,|T|²~δ²`.
- **Step 2 (substitute)**: `|S_cross|/S_base = |Δ_{A,T}|/|a₀(D_M)a₂(D_K)+a₂(D_M)a₀(D_K)| = (|A|²+|T|²)/|R_K|` (the (1/6) heat-kernel coefficient and the fiber-volume factor cancel against S_base's own (1/6)R_K fiber-volume structure; via Baptista Paper 13 eq 3.4 `R_P=R_M+R_K−|A|²−|T|²`).
- **Step 3 (order-count)**: A=T=0 at δ=0, smooth ⇒ `|A|=O(δ)`, `|T|=O(δ)` ⇒ `|A|²=O(δ²)`, `|T|²=O(δ²)`. Computed: `||A||²=3.2235×10⁻⁷` (non-abelian connection curvature `F_{01}^a=A_0^b A_1^c f^a_{bc}`, su(2)+u(1) vs C² non-commuting profiles), `||T||²=7.8125×10⁻⁴` (fiber second fundamental form, modulus-gradient). `S_base=a₂(D_K)=a_2_FW_zeta=2776.17` (O(1)·O(10³)).
- **Step 4 (direction read-off)**: `|S_cross|/S_base = (3.2235e-07 + 7.8125e-04)/2.018144 = 3.8727×10⁻⁴ = δ²·c_geom` with `c_geom=ratio/δ²=0.1549`. SIGN of (threshold − value) is **POSITIVE** (PASS direction). Threshold-crossing requires `c_geom > tau_PASS/δ² = 1e-2/2.5e-3 = 4.0` (Sage-QQ EXACT); computed `c_geom=0.1549 < 4.0` with **25.8× headroom** (`|R_K(fold)|=2.018` is O(1) not O(10), as the substitution chain anticipated).
- **Step 5 (conclusion)**: `|S_cross|/S_base ~ 3.87×10⁻⁴ < 10⁻²` at the ridge-confined off-Jensen point. The additive factorization holds to a quantified leak; the δ→0 limit recovers `|S_cross|/S_base → 0` (A-TENSOR-61) to machine ε. No sign flip; the CAVEAT branch (c_geom > 4 ⇒ INFO) does not fire.

**Constraint-map consequence (the van den Dungen topology/analysis boundary, moduli channel)**:
- **The additive a₂ → G_N read-off survives off-Jensen for the moduli direction.** The Kasparov product factorizes the K-HOMOLOGY class `[D_total]=π_!⊗[D_M]` EXACTLY (topology — mass ordering, c_s²=0, w_a=0 — is dressing- and deformation-rigid, independent of δ). The spectral-action MOMENTS (analysis side) acquire an O'Neill A/T correction off-Jensen, but at the ridge-confined δ=0.05 that correction is `3.87×10⁻⁴` of S_base — bounded, quantified, NOT unbounded. Every G_N / n_s number quoted on the Jensen line carries at most an O(δ²) A/T correction along the physical trajectory; the framework need NOT restrict the gravity-sector read-off to A=T=0 exactness.
- **Two complementary off-Jensen channels, both bounded.** S96-W1-ONEILL-NONFLAT bounded the **base-bundling connection-curvature** channel (`||F_ω||`, effacement-suppressed at the Hubble scale, INFO). This gate bounds the **moduli-displacement** channel (δ within the Jensen ridge, PASS at < 10⁻²). The two saturate the off-Jensen O'Neill content: the fabric's internal geometry can deform off the ridge (this gate) AND the SU(3) bundle over M⁴ can be non-flat (S96 W1); in BOTH directions the a₂ additive factorization holds to a small, quantified leak.
- **fb_pair backward**: INV12-W2-3 (Paper-10 bounded-perturbation theorem) supplies the structural REASON `S_cross` is a BOUNDED-ANALYTIC correction, not a topological one — off-Jensen excursions cannot flip the K-homology class, so the leak is confined to the soft analysis side. The gravity-sector G_N / n_s read-off inherits this O(δ²) bound. **Forward**: a refined-δ scan (the INFO discriminator, not needed here since PASS) would tighten the bound across the full ridge-confined region.

**Substrate framing**: GEOMETRIC. The substrate IS the spectral triple (A_K, H_K, D_K(τ)) on Jensen-deformed SU(3). The a₂ Seeley-DeWitt moment of D_total² IS the emergent 4D Einstein-Hilbert term (a₂ → G_N). The Kasparov product factorizes the K-HOMOLOGY class (topology); the heat-kernel product rule `a_n(D_total²)=Σ_{j+k=n}a_j(D_M²)a_k(D_K²)` holds EXACTLY when the O'Neill submersion tensors A=T=0 (the product metric on the Jensen line, A-TENSOR-61). Off-Jensen the fabric's internal geometry deforms off the ridge; the base-fiber Ehresmann connection (A-tensor) and the fiber second fundamental form (T-tensor) turn on linearly in δ, and the a₂ moment acquires an O(δ²) O'Neill remainder. This gate measures that the remainder — the spectral weight the additive factorization drops — is small enough (3.87×10⁻⁴) that the emergent G_N / n_s read-off survives along the physical (off-ridge) trajectory. Direction substrate-first: D_K eigenvalues → a₂ moment → emergent gravity; the off-Jensen leak is an internal-geometry correction to the emergent metric, NOT a container-curvature effect.

---

### §W2-2. INV12-W2-2-A-N-POLE-CONVERGENCE-AUDIT (van-den-dungen-bridge-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W2-2-A-N-POLE-CONVERGENCE-AUDIT`
**Trigger**: `[AUDIT]`
**Classification**: **GEOMETRIC** (CM-1995 dimension-spectrum pole-status ledger; cache-deliverable vs residue-subtracted partition)
**Agent**: `van-den-dungen-bridge-theorist` (solo→compute, positioned-specialist dispatch)
**Hypothesis**: Every load-bearing canonical a_n (a₀, a₂, a₄, gauge-module rank, R_K) admits a unique `(pole_in_s, curvature_grade n=d−2s, convergent? s>d/2)` tag at d=8; a complete ledger separates cache-deliverable convergent-pole numbers from residue-subtracted analytic-continuation numbers, with a₂ (s=3 double-power) provably in the divergent class per the §VII.CB S109 wall.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w2.md` §W2-2.

**Output Artifacts** (closure-verification checklist; per the gate-block `output_artifacts:` YAML):

1. **Script** `computations/investigation-12/inv12_w2_2_a_n_pole_convergence_audit.py` (27,392 bytes). `grep -E 'from canonical_constants import|print_verdict_payload'`:
   - `from canonical_constants import (` ✓
   - `def print_verdict_payload():` ✓
2. **Data** `computations/investigation-12/inv12_w2_2_a_n_pole_convergence_audit.npz` (10,798 bytes) — present. Holds the CLASS-I ledger arrays (`ci_pole_in_s_double`, `ci_convergent`, `ci_convergence_label`), the non-residue rows (`nonresidue_labels`, `nonresidue_class`), the a₂-canary cross-validation scalars (`a2_canary_consistent=True`, `s109_anchor_L10=280743.235367`), and the verdict scalars (`n_divergent_residue=5`, `ledger_complete=True`).
3. **Plot** `computations/investigation-12/inv12_w2_2_a_n_pole_convergence_audit.png` (67,779 bytes) — present. Pole-map: double-power s-axis vs the `s=d/2=4` convergence threshold (dashed); CLASS-I bars colored green (convergent) / red (divergent); a₂ canary annotated with the S109 Weyl-divergent anchor.
4. **Verdict line** `computations/investigation-12/inv12_gate_verdicts.txt` matches `^INV12-W2-2-A-N-POLE-CONVERGENCE-AUDIT:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + 2 regulator_pin/class-split extra rows. **NO 3-tuple** ([AUDIT], not [SIGN]) ✓.
5. **This wp_section** — present (Status/Verdict/Output Artifacts/MCP Pre-Compute Audit blocks populated).

**MCP Pre-Compute Audit** (queries run BEFORE writing the script; query-first discipline per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("a_2 divergent pole Weyl spectral action S109 VIICB")` | **`S109-VIICB-ZETA-NATIVE-LEVEL-3`** FAIL: `is_weyl_divergent=True`, anchor_L6/L8/L10 = 39619→109123→280743, g_M=2776.165389; ζ-native route CLOSED (audit_sha `e976ab54…`). This IS the a₂ canary. |
| `search_knowledge("Mellin pole convergence dimension spectrum residue subtracted cache")` | T5 Mellin-Strip theorem: `S_d={0,2,4,6,8}` for SU(3) at d=8; residue formula `Res(ζ_D,s=d/2−k)=a_{2k}/Γ(d/2−k)` (S46). |
| `get_constant("a_2_FW_zeta")` | **2776.165389** (S88; == S109 g_M — the residue equals the Weyl coefficient). |
| `get_constant("a_4_FW_zeta")` / `get_constant("a_0_FW_zeta")` | a_4=1350.7216 (S75); a_0=6440.0 (S88). |
| `list_constants("a_[0-9]_FW")` | full canonical set: a_0=6440, a_2=2776.17, a_4=1350.72, a_6=765.594, a_8=521.183. |
| `search_knowledge("R_K Koszul fold -2.018 …")` | **R_K(fold)=−2.018 M_KK²** (Koszul, S61); a curvature scalar that FEEDS a₂, NOT itself a ζ residue → CLASS II. |
| `search_knowledge("gauge module rank 775 …")` | **gauge-module rank 775** (S61/S63 MODULE-61, Paper 05); a K₀ index → CLASS III. |
| `search_knowledge("d=8 cone apex … s>d/2")` | d_cone_apex=8 (S85 W6-13); poles at s={4,3,2,1,0} double-power; Conv. A/B definitions (S108 W2). |

**NOT PRE-CLOSED as a ledger** — the S109 canary closes the a₂ *single* row; this gate's deliverable is the *complete* per-a_n ledger across the load-bearing set, which is new. The S109 verdict is consumed as the a₂ cross-check anchor (the input pin `s109_gate_verdicts.txt`, sha `f830d00b…`).

**Verdict**: **PASS** — `value='ledger_complete=True;n_classI_residue=5;n_convergent=0;n_divergent=5;divergent=a_0+a_2+a_4+a_6+a_8;a2_double_s=3_n=2_DIVERGENT;a2_canary_S109_consistent=True;nonresidue=R_K+gauge_rank775_pole_free;d_apex=8;thresh_s_gt_4'` scheme=Mellin convention=BOTH-poleconv-A-double-AND-B-single L_max=N/A. audit_sha256 `fcad3d1dcca5139642a0ec19dcc8a7dcb92bbed3a1c903869e4595f43cab18b0`, content_sha256 `6e8bb2a4850f95a82b73a575ce301716b8fe946555626479c15b2c0a76451c0b`. 4-tuple `(value=<ledger>, scheme=Mellin, convention=BOTH-poleconv-A-double-AND-B-single, L_max=N/A)`. [AUDIT] — no 3-tuple. The ledger is complete (5/5 CLASS-I residues tagged with internally-consistent triples; n=d−2s recovered in both conventions to machine ε) AND the a₂ double-power s=3<d/2=4 DIVERGENT status reproduces the §VII.CB S109 `is_weyl_divergent=True` verdict bit-for-bit.

**Results**:

**Per-a_n pole-convergence ledger** (d_cone_apex = 8; convergence threshold `s > d/2 = 4` on the double-power exponent; convergence is a property of the underlying heat-trace Dirichlet series `Σ m_k |λ_k|^{−2s}`, identical in both printed conventions):

| a_n | class | curvature grade n | pole_in_s (A-double) | pole_in_s (B-single) | convergent? `s>4` | cache-deliverable? | canonical value | physics role |
|:----|:------|:---:|:---:|:---:|:---:|:---:|:---|:---|
| a₀ | I — ζ-residue | 0 | **4** | 8 | **DIVERGENT-MARGINAL** (log-div at s=d/2) | **No** | 6440.0 | Λ (cosmological term) |
| a₂ | I — ζ-residue | 2 | **3** | 6 | **DIVERGENT** | **No** | 2776.165389 | G_N, Einstein-Hilbert (**the S109 canary**) |
| a₄ | I — ζ-residue | 4 | **2** | 4 | **DIVERGENT** | **No** | 1350.7216 | Yang-Mills + Higgs quartic |
| a₆ | I — ζ-residue | 6 | **1** | 2 | **DIVERGENT** | **No** | 765.594 | higher-order EFT control |
| a₈ | I — ζ-residue | 8 | **0** | 0 | **DIVERGENT** | **No** | 521.183 | higher-order EFT control |
| R_K(fold) | II — Koszul curvature | — | — (pole-free) | — | N/A (NON-RESIDUE) | Yes (metric invariant) | −2.018 M_KK² | fiber scalar curvature (FEEDS a₂; Koszul, S61) |
| gauge-module rank | III — K-theory index | — | — (pole-free) | — | N/A (NON-RESIDUE) | 775 | gauge-module K₀ rank (Paper 05; deformation-invariant per Paper 10) |

Convention map cross-check (per `regulator-pin-discipline.md §"Mellin Pole-Set Labeling"`): Conv. A (double-power) `ζ_D(s)=Σ m_k λ_k^{−2s}`, poles `s=(d−n)/2` ⇒ `n=d−2s` ⇒ S_s={4,3,2,1,0}; Conv. B (single-power) `ζ_D(s)=Σ m_k λ_k^{−s}`, poles `s=d−n` ⇒ `n=d−s` ⇒ S_s={8,6,4,2,0}. `{0,2,4,6,8}` is ALWAYS the curvature grade n. Internal consistency `n=d−2·s_double=d−s_single` verified to machine ε for all five rows (`ledger_complete=True`).

**Headline INFO diagnostic — the divergent count**: **5 of 5 CLASS-I zeta-residue a_n live at divergent poles** (`s ≤ d/2 = 4`). ZERO are convergent partial-sum limits under the strict `s > d/2` shell-sum criterion the gate pre-registered. Every analysis-side framework number quoted "from the L_max=10/12 cache" — a₀→Λ, a₂→G_N, a₄→YM+Higgs, a₆/a₈→EFT — is a **residue-subtracted analytic continuation**, NOT a convergent partial sum. The cache delivers them only as meromorphic residues, not as limits.

**The a₀ marginal-pole subtlety** (sharper than the gate hypothesis's "CONVERGENT marginal" parenthetical): a₀ sits at the boundary pole `s_double = d/2 = 4` EXACTLY. Substitution chain — the partial-sum tail integral over the Weyl-counting shell `m(λ)~λ^{d−1}` is `∫^L λ^{d−1}·λ^{−2s}dλ = ∫^L λ^{d−1−2s}dλ`; at s=d/2 the exponent is `d−1−d = −1` so the integrand is `λ^{−1}` and `∫^L λ^{−1}dλ = ln L → ∞`. The a₀ partial sum **diverges logarithmically**; a₀ is `DIVERGENT-MARGINAL`, not cache-deliverable as a finite limit. The strict `s>d/2` test the gate pre-registered (machinery_pin_map line 288; method step 3) correctly yields 0 convergent residues — the parenthetical "CONVERGENT marginal" guess in the hypothesis is the one cell the audit overturns.

**a₂ canary cross-validation against §VII.CB S109-VIICB-ZETA-NATIVE-LEVEL-3** (the input pin):
- Audit first-principles: a₂ at double-power `s=3 < d/2=4` ⇒ DIVERGENT (computed independently from `n=2`, `s=(8−2)/2=3`).
- S109 verdict: `is_weyl_divergent=True` ⇒ **agrees** (audit `a2_status_agrees_with_s109=True`).
- Anchor monotone-increasing 39619 → 109123 → 280743 (trend=+1) ⇒ partial sum grows without bound, consistent with divergent-pole classification (`anchor_monotone_increasing=True`).
- anchor_L10=280743.235367 > g_M=2776.165389 ⇒ misses the Weyl coefficient from above by ~10⁵× (`anchor_misses_gM_from_above=True`).
- `a_2_FW_zeta == S109 g_M` (residue == Weyl coefficient) ⇒ `a2_value_is_gM=True`.
- Composite `a2_canary_consistent=True`. The audit reproduces the S109 wall bit-for-bit from first principles.

**Constraint-map consequence (the topology/analysis boundary made explicit at the per-moment level)**:

- **The "from-the-cache" partition is sharper than expected**: the convergent/divergent split among ζ-residues is `0 / 5`, not `1 / 4`. NO load-bearing analysis-side moment is a convergent finite-L sum. This does NOT impugn the values (the residue-subtracted analytic continuation is the *correct* definition of a₀/a₂/a₄ on a d=8 cone — the spectral action IS the regularized Tr f(D/Λ), and the residue at a meromorphic pole is exactly what it extracts); it BOUNDS what "computed from the L=10/12 cache" can claim: these numbers are L-unverifiable as partial sums and MUST be reported as residue values, with their L-truncation behavior (Weyl-divergent growth, S109) disclosed. This tightens the W2 wave's thesis — the analysis side (spectral-action moments) is the soft, scheme-/regulator-laden side of my topology/analysis boundary, and now we know *every* load-bearing moment lives there.
- **The three-class structure is the load-bearing refinement**: the gate named 5 "load-bearing a_n," but they are NOT all ζ-residues. R_K(fold) (CLASS II, Koszul curvature) and gauge-module rank 775 (CLASS III, K₀ index) are **pole-free non-residue invariants**. They are L-stable for a *topological/algebraic* reason — R_K is a fixed metric invariant; the gauge rank is a deformation-invariant K₀ rank (Paper 10 locally-bounded-perturbation protection) — NOT because their shell sum converges. Collapsing them into a "convergent cache number" column would misrepresent them. This is precisely the substrate-IS/topology-vs-analysis distinction: the TOPOLOGY (gauge rank, deformation-rigid) and the GEOMETRY (R_K, fixed-metric) are robust by structural type; the ANALYSIS (a_n residues) is regulator-soft AND L-unverifiable-as-sums.
- **Forward (fb_pair backward)**: every framework number quoted "from the cache" (a₀→Λ, a₂→G_N, a₄→YM+Higgs, gauge rank, R_K) inherits this tag. Pairs with INV12-W1-4 (lizzi's R_1 same-regulator audit) as the same-regulator-consistency leg. **Pole-status ledger LANDED, ready for HY6 registry-lift** (seed R-4 / HY6 — the registry-lift of these tags into `sessions/framework/registry/` is Q2 hygiene, NOT this gate). NO substitution chain on the gate itself — classification audit, no directional CLAIM (the one structural sign-fact, a₂ DIVERGENT, is imported from S109, with the marginal-a₀ log-divergence sub-chain verified above).

**Substrate framing**: GEOMETRIC. The substrate IS the spectral triple; its analysis-side observables (a₀→Λ, a₂→G_N, a₄→YM+Higgs) are residues of `ζ_{D_K}(s)` at the CM-1995 dimension-spectrum poles. A pole at `s>d/2` would be the L→∞ limit of a CONVERGENT partial sum over D_K eigenvalues; a pole at `s≤d/2` is a residue-subtracted analytic continuation at a meromorphic pole where the shell sum `L^{d−2s}` diverges. This audit makes the IS-not-IN distinction explicit at the per-moment level: ALL five load-bearing ζ-residues are analytic continuations (substrate-IS as meromorphic residues, but finite-L-unverifiable as sums), while R_K and the gauge rank are pole-free invariants robust by structural type. The direction is substrate-first throughout: the pole status is a property of the D_K spectrum's growth (Weyl-divergent, S109), NOT of any external regulator imposed on it.

---

### §W2-3. INV12-W2-3-PAPER10-BCS-DRESSING-INVARIANCE (van-den-dungen-bridge-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W2-3-PAPER10-BCS-DRESSING-INVARIANCE`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Mesland–van den Dungen Paper-10 bounded-perturbation; K-homology dressing-invariance)
**Agent**: `van-den-dungen-bridge-theorist` (solo)
**Hypothesis**: The BdG dressing `D_K → D_K + V_BdG` (|Δ_BCS|=0.4642547 finite, bounded) satisfies the Paper-10 (1608.02506) local-boundedness hypothesis, so the K-homology class [D_K] is preserved EXACTLY (mass ordering, c_s²=0, w_a=0 dressing-invariant even off-Jensen) while a_n shifts by a bounded analytic correction — promoting S69 W5-G from per-case observation to a structural theorem.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w2.md` §W2-3.

**Output Artifacts** (closure-verification checklist; per the gate-block `output_artifacts:` YAML):
- (1) **script** `computations/investigation-12/inv12_w2_3_paper10_bcs_dressing_invariance.py` — EXISTS. `grep -E "from canonical_constants import|print_verdict_payload"` →
  - `from canonical_constants import Delta_BCS, omega_L1  # noqa: E402`
  - `def print_verdict_payload():` + `_ = print_verdict_payload()`
- (2) **data** `computations/investigation-12/inv12_w2_3_paper10_bcs_dressing_invariance.npz` — EXISTS (records `V_BdG_norm`, `rel_D_bound`, `commutator_norm`, `is_tensor_factor_disjoint`, `paper10_hypothesis_satisfied`, `theorem_applies`, `k_homology_class_preserved`, `a_n_shift_is_bounded_analytic`).
- (3) **plot** `computations/investigation-12/inv12_w2_3_paper10_bcs_dressing_invariance.png` — EXISTS (schematic: hypothesis legs + topology-rigid/analysis-soft split; OPTIONAL per plan).
- (4) **verdict_line** `computations/investigation-12/inv12_gate_verdicts.txt` — EXISTS, matches `^INV12-W2-3-PAPER10-BCS-DRESSING-INVARIANCE:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + 2 theorem-detail rows. NO 3-tuple ([VERIFY-THEOREM], not [SIGN]).
- (5) this **wp_section**.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; one-line salient return each):
- `get_constant("Delta_BCS")` → **0.4642547394830737**, S70, R-PROTECTED, gate BCS-GAP-CANONICAL-70, alias for `Delta_0_OES`. The boundedness witness: `‖V_BdG‖ = |Δ_BCS| < ∞`.
- `get_constant("omega_L1")` → **0.138** (M_KK; Leggett-1 frequency). The a_n analytic-shift scale (inter-band-coherence).
- `trace_entity("S69 W5-G")` → no direct trace node (the per-case observation lives in agent memory + as a registry headline); the BdG-dressing equation thread is grounded instead via `trace_entity("BdG dressing")` → eq_552 (paraphrases this gate's own hypothesis: "|Δ_BCS|=0.4642547 finite ⇒ V_BdG bounded ⇒ rel-D-bound 0 < 1, hypothesis holds A FORTIORI") + the tensor-factor-disjoint commutator.
- `search_knowledge("bounded perturbation K-homology preserved Mesland van den Dungen")` → **closed_mechanism "K-homology stability (bounded perturbation) | Theorem | S61 (alpha=0.081<1/2)"** (`framework-cc-oom.md`). The relative-bound precedent; S61 verified it for the *Jensen deformation* (α=0.081). NOT a pre-closure of THIS gate (which concerns the BdG *dressing*, a structurally distinct perturbation that is BOUNDED, hence stronger).
- `search_knowledge("ABELIAN-SUBFACTOR D_BdG squared Delta tensor Nambu")` → `D_BdG² = (D_K²+|Δ|²)⊗1₂` (S82, cc-path-e.md E-3/E-30); `K_BdG(t) = 2·exp(−t·Δ²)·K_DK(t)` (S36) — the bounded-analytic a_n-shift tower.
- `search_knowledge("K-homology stability alpha 0.081 relative bound half")` → S82 Connes synthesis: `α := ‖[D_F^(def) − D_F^(τ=0)] R(D_F^(τ=0))‖`, `α ≤ 0.081+0.00014 = 0.08114 < 1` (Kato-Rellich, the **Jensen-deformation** bound). Confirms S61 is a *deformation* bound, kept DISTINCT from the BdG-dressing bound here.
- **PRE-CLOSED?** NO. S61 closed the *deformation* invariance (α=0.081 < ½); this gate closes the *BdG-dressing* invariance via the Paper-10 locally-bounded-perturbation theorem — a different perturbation class, and the promotion of S69 W5-G to a structural theorem is new.

**Verdict**: **PASS** — `audit_sha256=9f861259c3f69ae66bb21c7cc7b8ad1543bac039eb6a504ba19fc8d041dffb0d`, `content_sha256=b3f86187621591291e6ead941264430ef5ed5538873ee934d56aaf14ee8a6033`. 4-tuple `(value='theorem-SATISFIED=True…', scheme=FW, convention=ABSOLUTE, L_max=N/A)`.

**Results**

*Paper-10 theorem, faithfully stated (arXiv:1608.02506, Mesland–van den Dungen, JNCG 12 (2018) 639–680; abstract fetched).* Let `(A, E, D)` be an unbounded Kasparov module with `D` a regular self-adjoint operator on a Hilbert module. If `V` is a **locally bounded symmetric** operator — "locally bounded" meaning the composition `a·V` is bounded for every `a` in the approximate identity `{u_n}` of `A` (NOT global operator-norm boundedness) — then `D+V` is again regular and self-adjoint, AND the Kasparov class `[D] ∈ KK(A,B)` is **UNCHANGED**.

*Boundedness witnesses (all machine-exact):*

| Leg | Quantity | Value | Status |
|:----|:---------|:------|:-------|
| (i) symmetric | Hermiticity residual `‖V_BdG − V_BdG†‖` | `0.0e+00` | self-adjoint ✓ |
| (ii) bounded | `‖V_BdG‖ = |Δ_BCS|` | `0.4642547395` | finite ✓ |
| (ii) cross-check | numeric opnorm (max σ of `[[0,Δ],[Δ*,0]]`) | `0.4642547395` (residual `0.0e+00`) | = `|Δ_BCS|` ✓ |
| (ii) ⇒ locally bounded | `‖a·V_BdG‖ ≤ ‖a‖·|Δ_BCS| < ∞` (a-fortiori) | `True` | locally bounded ✓ |
| (iii) regularity | relative-D-bound (bounded ⇒ 0) | `0.0 < 1` | regular + s.a. ✓ |
| (iv) algebra-action | `[V_BdG, a]` for `a∈A_K` (tensor-factor-disjoint) | `0.0e+00` EXACT | commutes ✓ |

`paper10_hypothesis_satisfied = True` (legs i ∧ ii ∧ iii); `theorem_applies = True` (∧ leg iv, reinforcing).

*The a-fortiori chain (faithful, NOT overstated).* The actual Paper-10 hypothesis is "**locally bounded** symmetric." The BdG dressing is **globally** bounded (`‖V_BdG‖ = |Δ_BCS| = 0.4642547 < ∞`, the off-diagonal Nambu pairing block `[[0,Δ],[Δ*,0]]` having eigenvalues `±|Δ|`). Global boundedness ⇒ local boundedness trivially (`‖a·V_BdG‖ ≤ ‖a‖·|Δ_BCS|`), so the hypothesis holds **a fortiori** — the BdG dressing is in the *interior* of the admissible perturbation class, not on its boundary. The plan's PASS-bundle (`‖V_BdG‖<∞ ∧ rel-bound=0<1 ∧ [V_BdG,a]=0`) is a **sufficient-condition cluster**: `‖V_BdG‖<∞` ⇒ the locally-bounded hypothesis (the load-bearing leg); `rel-bound=0` ⇒ the Kato-Rellich regularity-preservation leg; `[V_BdG,a]=0` is a **reinforcing** structural fact (S98 W1 tensor-factor-disjointness) that is **not strictly required** by Paper 10 but cleanly shows the dressing acts trivially on the algebra action, so the analytic a_n shift cannot leak into the topological class.

**Structural theorem (the S69 W5-G promotion).** The BdG dressing `D_K → D_K + V_BdG` satisfies the Mesland–van den Dungen locally-bounded-perturbation hypothesis, therefore

> **`[D_K + V_BdG] = [D_K]` in `KK(A_K, ℂ)` EXACTLY** — the K-homology class is invariant under the BdG dressing, at every L_max (L-independent).

This converts S69 W5-G ("BCS = Ricci-type, modifies a_n, preserves topology") from a **per-case numerical observation** into a **STRUCTURAL THEOREM**: the topology side (Kasparov product, K-homology class) is **dressing-RIGID**, and the analysis side (spectral-action heat-kernel moments `a_n → Λ, G_N`) is **dressing-SOFT**. The a_n shift is **bounded-analytic**: `K_BdG(t) = 2·exp(−t·|Δ|²)·K_DK(t)` (S36) gives a finite `e^{−t|Δ|²}` Taylor tower with leading scale `|Δ_BCS|² = 0.215532` (and `ω_L1 = 0.138` setting the inter-band-coherence shift scale). The shift is finite *precisely because* `|Δ_BCS| < ∞` — the same finiteness that delivers local boundedness. No regulator pin is required: the theorem's content is exactly that the topological side needs no regulator.

**Relation to the S61 precedent (kept distinct).** S61 K-HOMOLOGY-STABILITY (`α = 0.081 < ½`, Kato-Rellich) verified class invariance for the **Jensen deformation** `D_F^(def) − D_F^(τ=0)` — a *relatively*-bounded perturbation. The BdG dressing is a **bounded** perturbation (rel-bound `0 < 0.081`), strictly **stronger** than the deformation case, and via the *bounded*-perturbation theorem (not merely Kato-Rellich) it gives **EXACT** class invariance. Two perturbation classes, two theorems; the cross-check `bdg_stronger_than_deformation = True` records `0 < 0.081`.

**Constraint-map consequence.** PASS discharges the topology/analysis split from per-case to STRUCTURAL:

- **Mass ordering, `c_s²=0` (§VII.BH), `w_a=0`** are now **dressing-invariant by theorem** — they are K-homology-class observables (TOPOLOGY), rigid under any `|Δ_BCS|`-finite BdG perturbation, and (composed with the **backward** leg to INV12-W2-1, which bounds the off-Jensen O'Neill leak) **off-Jensen-safe**: an off-Jensen excursion perturbs the analytic moments but **cannot** flip the K-homology class.
- This **constrains** the INV12-W4-2 adjudication (wrong-functional [lizzi] vs wrong-signature [vdd] diagnosis of the SA failure): since the topology is **provably dressing-safe**, any SA-failure diagnosis must locate the failure on the **analysis** side (the a_n / functional choice), not the topological side. The dressing cannot be the culprit for a topological observable.
- A FAIL (had the hypothesis not held — e.g. `[V_BdG,a]≠0`) would have left the split per-case, forcing each topological observable's dressing-invariance to be re-verified individually and removing the structural anchor for the W2-1 off-Jensen-safety backward leg. It did not: all four legs hold to machine ε.
- **Forward / open**: `GAUGE-DRESSED-PROTECTION` (does W5-G extend to the gauge dressing `D → D + A + JAJ⁻¹`?) is the natural next case — `A + JAJ⁻¹` is also self-adjoint, and if it is locally bounded (the gauge field bounded on the finite-L truncation) the same theorem applies; that extension is a separate verification, not discharged here.

*Substrate framing.* GEOMETRIC. The substrate IS `(A_K, H_K, D_K)`; the BCS/Bogoliubov physics dresses `D_K → D_K + V_BdG` (the fabric's internal geometry acquires a pairing field). The K-homology class is the substrate's topological skeleton, carrying the scheme-independent zero-parameter observables; Mesland–van den Dungen says a bounded dressing cannot deform that skeleton. Direction substrate-first: `D_K`'s K-homology class → the rigid topological observables; the dressing perturbs the analytic moments but cannot touch the class. *No substitution chain — set-membership theorem verification, no directional CLAIM.*

---

### §W2-4. INV12-W2-4-KREIN-LORENTZIAN-A0 (van-den-dungen-bridge-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W2-4-KREIN-LORENTZIAN-A0`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (pseudo-Riemannian submersion spectral triple; Krein a₀ vs Euclidean a₀ — the DILUTION-CC Λ leg)
**Agent**: `van-den-dungen-bridge-theorist`
**Hypothesis**: On the pseudo-Riemannian submersion triple (timelike M⁴, Riemannian SU(3) fiber) built per Paper 04 (1207.2112) with the Krein fundamental symmetry J (linear, J²=+1 — distinct from Connes' antilinear J), the Krein zeroth Seeley-DeWitt moment a₀^{Krein} equals the Euclidean a₀ that DILUTION-CC's Λ consumes — the naive Wick rotation is validated for the cosmological-constant leg, so the DILUTION-CC number is signature-robust.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w2.md` §W2-4.

**Output Artifacts** (closure-verification checklist; per the gate-block `output_artifacts:` YAML):

- **(1) script** `computations/investigation-12/inv12_w2_4_krein_lorentzian_a0.py` (25,503 bytes) — `grep -cE "from canonical_constants import"` → `2`; `grep -cE "print_verdict_payload"` → `2`. PASS.
- **(2) data** `computations/investigation-12/inv12_w2_4_krein_lorentzian_a0.npz` (9,492 bytes) — present (`rel_diff`, `a0_eucl`, `a0_krein`, `volume_factor`, `trace_factor`, `signed_trace_ratio`, `j_involution_err`, `J_convention`, …). PASS.
- **(3) plot** `computations/investigation-12/inv12_w2_4_krein_lorentzian_a0.png` (82,263 bytes) — present (2-panel: a₀^Krein vs a₀^Eucl bar; the volume/dim-count factors vs the a₀-irrelevant signed super-trace). PASS.
- **(4) verdict_line** `computations/investigation-12/inv12_gate_verdicts.txt` — canonical line matches `^INV12-W2-4-KREIN-LORENTZIAN-A0:.* audit_sha256=[a-f0-9]{64}`:
  `INV12-W2-4-KREIN-LORENTZIAN-A0: PASS -- value='0.0' scheme=Krein-FW convention=RATIO L_max=12 audit_sha256=677f4185d6a8aa0c652c778544f9a6942a0c48818695bf0bf93f88cdaa172838 content_sha256=8225d5298dada4079e0b75ac2a29fea038358531d92b359ae27b796134a466c6 schema_version=S84+`
  dual-SHA companion row present; schema-v2 3-tuple row present (`# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`). PASS.
- **(5) wp_section** — this section. PASS.

**MCP Pre-Compute Audit** (queries run before writing the script; one-line salient return each):

- `trace_entity("Krein space spectral triple")` → **No trace found** — confirms this is the framework's FIRST Lorentzian/Krein NCG construction (the plan's framing is correct; nothing to recompute).
- `get_constant("a_0_FW_zeta")` → **6440.0** (S88, gate `S88-A-N-FW-CANONICALIZATION`) — the Euclidean a₀ that DILUTION-CC consumes; the comparison anchor.
- `search_knowledge("DILUTION-CC a_0 Volovik cosmological constant")` → **DILUTION-CC PROVEN S66** (rho_vac/rho_obs=1.032, 114-OOM gap closed) AND edge `gates:DILUTION-CC --depends_on--> constants:a_0_FW_zeta` — confirms the a₀→Λ dependency this gate stress-tests.
- `search_knowledge("pseudo-Riemannian Krein Wick rotation KO-dimension SU(2,1)")` → **KO-dimension = 6 (G4) PROVEN, "Survives pseudo-Riemannian SU(2,1) extension (S46)"**; `s46_pseudo_riemannian` data_provenance located — the Krein-machinery construction seed (KO-dim=6, J²=+1, Krein (8,8)).
- `search_knowledge("a_0 Weyl volume heat kernel dimension counting signature")` → canonical structural statement (session-75 baptista-qa-workshop): `a_0 = (4π)^{-d/2} · dim(V) · Vol, purely topological (counting dimensions and volume)` AND `a_0(K) = 6440` (twice independently) — the substrate-physics basis for the dim-counting-trace argument (Step 3ii).

**PRE-CLOSED?** NO. No prior gate computes a₀ on an indefinite-signature triple. The DILUTION-CC closure (S66) *assumed* the Euclidean a₀; this gate is its first signature-robustness test.

**Verdict**: **PASS** — `rel_diff = |a₀^{Krein} − a₀^{Eucl}| / |a₀^{Eucl}| = 0.0` (EXACT) ≤ 10⁻³ threshold. Schema-v2 3-tuple: **sign=PASS** (substitution-chain-predicted EQUALITY direction confirmed), **magnitude=PASS** (`|rel_diff − 0| = 0 ≤ 10⁻³`), **regime=VALID** (the a₀ Weyl leading-coefficient is exact — no truncation, no small-parameter expansion, no regime breakdown). 4-tuple: `(value=0.0, scheme=Krein-FW, convention=RATIO, L_max=12)`. Dual-SHA: `audit=677f4185…2838`, `content=8225d529…66c6`.

**Results**:

| Quantity | Value | Note |
|:---------|:------|:-----|
| a₀^{Eucl} (S88 `a_0_FW_zeta`) | **6440.000000** | the a₀ DILUTION-CC reads as Λ (rho_vac/rho_obs=1.032, S66) |
| a₀^{Krein} (this gate) | **6440.000000** | timelike-M⁴ × Riemannian-SU(3) indefinite triple |
| \|a₀^{Krein} − a₀^{Eucl}\| | **0.000e+00** | absolute difference |
| **rel_diff** = \|Δa₀\|/\|a₀^{Eucl}\| | **0.000e+00** | the gate observable (PASS ≤ 1e-3) |
| det(g_Eucl) / det(g_Krein) | +1.0 / −1.0 | one timelike direction: det flips by (−1)¹ |
| VOLUME factor √\|g_Krein\|/√g_Eucl | **1.000000** | √\|·\| removes the sign — signature-robust |
| J²=+1 involution error | **0.00e+00** | Krein-linear J (NOT Connes' antilinear J), exact |
| Krein split (dim_H, n₊, n₋) | (16, 8, 8) | matches s46 `krein_verdict = VALID (8,8)` |
| a₀-RELEVANT trace factor (dim-count ratio) | **1.000000** | Tr_dimcount(1_H)/Tr(1_H) = 16/16 — signature-robust |
| a₀-IRRELEVANT signed super-trace Tr(J)/dim_H | **0.000000** | the graded INDEX, NOT a₀ — reported as contrast |
| fiber (SU(3) Riemannian, Vol_SU3=1349.74) | signature-blind | only the M⁴ base flips signature |

- **CLASS=FULL** — genuine indefinite-D² Krein construction per Paper 04/08 (the J-weighted Krein trace, the H=H₊⊕H₋ decomposition), NOT a `_spectral_action_regulators.py` SCHEMATIC analog.
- **J_convention=Krein-linear-J2=+1** — the Krein fundamental symmetry J is the LINEAR self-adjoint involution, J²=+1 (Paper 04 lines 59–60; Paper 08 line 18), DISTINCT from Connes' ANTILINEAR real-structure J (J²=±1) that the framework uses elsewhere. Verified J²=+1 to machine zero. Mis-identifying the two is the canonical convention failure (my survey R-4; memory J-ambiguity warning) — explicitly guarded here.

**Full substitution chain** (the [SIGN] equality claim, with substituted numbers):

> **Claim**: a₀^{Krein} = a₀^{Eucl} (naive Wick rotation validated for the Λ leg).
>
> **Step 1 (Definitions)**. a₀^{Eucl} = (4π)^{−d/2}·Vol_Eucl(M⁴×SU(3))·Tr(1_H) = `a_0_FW_zeta` = **6440** (S88; DILUTION-CC → Λ). a₀^{Krein} = (4π)^{−d/2}·∫√\|g_Krein\| d⁸x·Tr_{J-relevant}(1_H) on the timelike-M⁴ × Riemannian-SU(3) triple, Tr_J the J-weighted Krein trace. J: linear, J²=+1 (Paper 04/08).
>
> **Step 2 (Substitute, no simplification)**. a₀^{Krein}/a₀^{Eucl} = [∫√\|g_Krein\|·Tr_{J-rel}] / [∫√g_Eucl·Tr].
>
> **Step 3 (Simplify — the two factors that could differ)**. **(i) Volume**: \|det g_Krein\| = \|det g_Eucl\| because the timelike sign flip multiplies det g by (−1)^{#timelike} = (−1)¹ = −1, and √\|·\| removes the sign → √\|g_Krein\| = √g_Eucl pointwise → **volume factor = 1** (computed: det_Eucl=+1, det_Krein=−1, √\|·\| both = 1.000000). **(ii) Trace**: a₀ is the COEFFICIENT of the leading t^{−d/2} heat-kernel term = the spinor-module dimension count. Under Paper 04's Main Theorem H=H₊⊕H₋ (J=+1 on H₊, −1 on H₋), the heat kernel sees Tr e^{−tD₊²} + Tr e^{−tD₋²}, whose leading coefficients sum to (4π)^{−d/2}·Vol·(dim H₊ + dim H₋) = (4π)^{−d/2}·Vol·dim H. The Weyl dim-count dim H₊ + dim H₋ = 8 + 8 = 16 = dim H is a signature INVARIANT → **trace factor = 16/16 = 1** (computed: 1.000000). **NB**: this is the dim-COUNT \|H₊\|+\|H₋\|, NOT the signed super-trace Tr(J) = dim H₊ − dim H₋ = 0 (the a₀-IRRELEVANT graded index, reported as the contrast so the wrong reading cannot regenerate).
>
> **Step 4 (Direction read-off)**. a₀^{Krein}/a₀^{Eucl} = (vol=1)·(trace=1) = 1 → rel_diff = 0 (≤ 10⁻³). **DIRECTION: EQUALITY.** a₀ is signature-ROBUST because it is the Weyl dim-counting leading coefficient — the moment LEAST sensitive to the indefinite signature.
>
> **Step 5 (Conclusion, with caveat)**. a₀^{Krein} = a₀^{Eucl} to < 10⁻³ (in fact 0 EXACT) → the naive Wick rotation IS validated for the Λ leg; DILUTION-CC's a₀ → Λ is signature-robust. SIGN of the equality holds (PASS direction). **CAVEAT — a₀-SPECIFIC**: a₂ (gravity, ~R) and a₄ (Yang-Mills+Higgs, ~R²) carry CURVATURE; the indefinite signature DOES enter those heat-kernel coefficients non-trivially. The expected/computed PASS is for a₀ specifically; the higher moments are the multi-session follow-on (NOT this gate).

**Why the result is EXACT (0), not merely small**: the volume-element determinant under √\|·\| and the spinor dim-count under H=H₊⊕H₋ are both *signature-blind by construction* — there is no small-parameter that could leave an O(ε) residual. This is a structural identity at the Weyl-leading-coefficient layer, machine-ε. A contrast worth flagging: in **s46**, a₀ *diverged* (Obstruction 3) — but that was an **IR / non-compactness** effect (Vol(SU(2,1))=∞ on a non-compact *fiber*), NOT a signature effect. W2-4 keeps the fiber compact and Riemannian and flips only the timelike *base*, isolating the pure signature effect on a₀, which vanishes. The two are orthogonal: s46's divergence is a fiber-volume IR pathology; W2-4's robustness is a base-signature topology result.

**Constraint-map consequence**:

- **U-2 discharged AT a₀** (my survey next-step 4 / NCG-bridge unknown U-2 "naive Wick rotation unsupported"): the Euclidean→Lorentzian transport of the a₀ volume moment is now a *computed identity*, not an assumption. DILUTION-CC's a₀ → Λ (S66, rho_vac/rho_obs=1.032) is **signature-robust** — the cosmological-constant number does not shift under the rigorous Krein construction.
- **Boundary preserved (topology/analysis split)**: this PASS is exactly the boundary my Wave-2 thesis predicts. a₀ is the topological/dim-counting moment (`a₀ ~ Vol · dim(V)`, the most topological of the Seeley-DeWitt coefficients), so it is signature-rigid — consistent with the Kasparov-product topology being signature-robust while the *curvature-carrying* analysis moments (a₂, a₄) remain the open Lorentzian question.
- **Forward (the higher-moment Krein construction)**: the a₂/a₄ Krein moments are the decisive follow-on. The dual-prior discriminator (plan §W2-4) reallocates 0.9 to Track A (Λ leg signature-robust) on this PASS; the escalation gate is the a₂^{Krein} computation, where curvature R enters the heat-kernel coefficient and the signature can genuinely shift the emergent G_N / Einstein-Hilbert term.
- **Feeds INV12-W4-2** (the SA-failure-diagnosis adjudication, wrong-functional [lizzi] vs wrong-signature [vdd]): this gate is the FIRST concrete test of the wrong-signature diagnosis. The verdict — *a₀ is signature-robust, the curvature moments are where signature could bite* — sharpens the adjudication: the wrong-signature hypothesis is NOT load-bearing at the volume term, so any signature-driven SA discrepancy must live at a₂/a₄, not a₀.

**Substrate framing**: GEOMETRIC. The substrate IS the spectral triple. The framework computes every spectral-action moment on the RIEMANNIAN M⁴×SU(3), then Wick-rotates by hand to physical Lorentzian signature. Van den Dungen's Krein program (Papers 04/08) is the rigorous indefinite-signature construction. The direction is substrate-first: the indefinite D_K² spectrum (Krein) → the a₀ heat-kernel moment → the emergent Λ. This gate establishes that the substrate's vacuum-energy term IS the same object in both signatures (a₀^{Krein} = a₀^{Eucl}) — the emergent Λ is signature-robust at the volume term, and DILUTION-CC is safe at a₀.

---

### §W2-5. INV12-W2-5-FWD-C1-BISMUT-CHEEGER-ETA (van-den-dungen-bridge-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W2-5-FWD-C1-BISMUT-CHEEGER-ETA`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (FWD-C1 cross-pillar-bridge LANDING; Bismut-Cheeger adiabatic-limit η-form ↔ integrated Bogoliubov pair-production)
**Agent**: `van-den-dungen-bridge-theorist`
**Hypothesis**: The Bismut-Cheeger η-form of the adiabatic-limit-breaking τ-family {D_K(τ)} across [0, τ_fold] (the non-integer families-index part, Paper 02 / Paper 12) is computable AND quantitatively identifies with the integrated Bogoliubov pair-production (59.8 pairs, S38), establishing FWD-C1 (substrate-IS spectral-flow/η-form ↔ laboratory-IN CMB power spectrum) with a binding Level-2 L^{−α} envelope and a NEW bridge-map class (adiabatic-limit η-form, NOT HKR — advances the Hybrid-Independence-Test K-counter via criterion (iii)).
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w2.md` §W2-5 (FWD-C1 LANDING; FULL 5-anatomy + 3-level discipline MANDATORY per `cross-pillar-bridge-anatomy.md`).

**Verdict**: **INFO** — composite (3-tuple `sign=FAIL, magnitude=FAIL, regime=VALID`). The bridge-map class (adiabatic-limit Bismut-Cheeger η-form) **exists and is computable**, and it yields a **Level-1 cohomology identity: η-form ≡ 0** (NOT the quantitative match to 59.8 the plan hypothesized). FWD-C1 reserves its §VII slot as **REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT**. `audit_sha256=934b66e4e694921231ed451e55d00f14e8489987e915f8016ab120dd7cc9c106`.

**Output Artifacts** (closure-verification checklist; per the gate-block `output_artifacts:` YAML — all confirmed on disk by content):
- **(1) script** `computations/investigation-12/inv12_w2_5_fwd_c1_bismut_cheeger_eta.py` (31,848 B) — `grep -cE "from canonical_constants import|print_verdict_payload"` → **3** (both must_contain present).
- **(2) data** `computations/investigation-12/inv12_w2_5_fwd_c1_bismut_cheeger_eta.npz` (8,410 B) — present.
- **(3) plot** `computations/investigation-12/inv12_w2_5_fwd_c1_bismut_cheeger_eta.png` (124,191 B) — present (3-panel: (a) η(τ) curve ≡ 0 across [0,τ_fold] at L=8; (b) |η-form| structural floor at every L; (c) the [SIGN] bar: η-form=0 vs S38 n_pairs=59.8 vs W3-1 N_pair_eff=5.49 vs mode-mix(L8)=759.8).
- **(4) verdict_line** `computations/investigation-12/inv12_gate_verdicts.txt` — matches `^INV12-W2-5-FWD-C1-BISMUT-CHEEGER-ETA:.* audit_sha256=[a-f0-9]{64}` (✓), dual-SHA companion row (✓), schema-v2 3-tuple row `# sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID` (✓, [SIGN]), `convention=RATIO-Bismut-Cheeger` carrying the Element-3 `-Bismut-Cheeger` scheme suffix (✓), `# regulator_pin=none` + `# OPERATIONAL-DEVIATION` extra rows (✓). Emitted via the race-safe `emit_verdict(session=12, track="investigation", ...)`.
- **(5) this wp_section** — COMPLETED.
- **CROSS-WAVE INPUT consumed**: `inv12_w3_1_relic_spectrum_ode_lock.npz` (orchestrator-canonical name; sha256=`323f1c74…`) — locked per-mode {β_k} consumed for the pair-production side; W3-1 landed, so the FULL FWD-C1 landing ran (no PRE-REG-INC partial-input close). `Σ mult·|β_k|² = N_pair_eff = 5.489098`, `N_trunc_rel = 0.3779` (the L_band_ceiling=7 truncation band, reported honestly per the orchestrator override).

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries executed BEFORE writing the script; one-line salient return each):
- `trace_entity("FWD-C1")` → FWD-C1 is **already substantially landed via a DIFFERENT route**: §VII.AU.OP-PROJ is the canonical FWD-C1 content host (S89 W7c REGISTRY-1 Stage-0 candidate → S90-A24 RETRY `all_8_booleans=True` → S91-W8-CF-67 Stage-2 cross-axis verify PRE-REG-INC). That route's bridge map is HKR/Mukhanov-Sasaki (n_s slope). **This gate is a SECOND FWD-C1 incarnation on a DISTINCT bridge-map class** (Hybrid-Independence-Test criterion (iii)) — NOT "the first FWD-C1 anything."
- `trace_entity("Bismut-Cheeger eta form")` → **no trace** (the families η-FORM is new to the framework as a bridge map; only the single-operator η-INVARIANT and the GV-Heitsch S88/S91 secondary-class scheme list mention "Bismut-Cheeger").
- `search_knowledge("Bogoliubov pair production eta invariant family spectral flow")` → **`η(D_K) = 0` EXACTLY** (S25/S35, five independent proofs, BDI symmetry); `sf(D, D_BdG) = 0`; `ETA-INVARIANT-60` FAIL `η(0)=0 exact, η(s)<1e-12 ∀s`. **Decisive**: the single-operator η-INVARIANT vanishes by BDI ±-symmetry at every slice.
- `get_constant("n_pairs")` → **59.8** (S38, T4 PROVEN, sudden-quench Bogoliubov; no PROVENANCE entry beyond S38). `get_constant("tau_fold")`=0.19, `get_constant("Delta_BCS")`=0.4642547395 (R-PROTECTED), `get_constant("M_KK")`=7.4287e16.
- `search_knowledge("families index eta form adiabatic limit ... Bismut Cheeger")` → confirms the **Level-1 splitting** `Index({D_K(τ)}) = ∫Â (local, integer) + η-form (non-integer), sf=0 ⇒ integer part fixed` is the families-index identity; the only prior "Bismut-Cheeger" usage is the S88/S91 GV-Heitsch secondary-class scheme triplet {APS-1975, Cheeger-Simons, Bismut-Cheeger}, NOT a families-η-form bridge.

**Results**:

**THE FIDELITY-CRITICAL FINDING (the substrate-IS content).** The plan's hypothesis — "the Bismut-Cheeger η-form quantitatively MATCHES the integrated pair-production 59.8" — conflates **two distinct families-objects** of {D_K(τ)}. As the fidelity-keeper, the central result of this gate is to separate them:

1. **Bismut-Cheeger η-FORM** (the genuine families-index spectral-asymmetry transgression): `η-form = ∫_{[0,τ_fold]} (d/dτ)[η(D_K(τ))] dτ = η(D_K(τ_out)) − η(D_K(τ_in))` (FTC). Because D_K is a **self-adjoint BDI** operator with a **± symmetric spectrum at every τ** (numerically: `signed_sum(fold) = {L8: −1.39e-12, L10: 0, L12: 0}`) and a **gap that never closes** (`sf=0`, J-protected, S61), the η-INVARIANT `η(D_K(τ)) = Σ_k sgn(λ_k) e^{−(λ_k/Λ)²} = 0` at every slice — so the transgression is **structurally ZERO**:
   - **L=8 full τ-trajectory** (45 sectors, 24-point τ-integral): η-form = **−1.465494e−13** (machine zero).
   - **L=10 cache-saturation** (65 sectors, 78,080 modes, fold slice): η-form = **0.0** EXACT, |λ|_max=4.6702.
   - **L=12 cache-saturation** (90 sectors, 166,896 modes, fold slice): η-form = **0.0** EXACT, |λ|_max=5.4189.
   The families index is **pure-integer** (∫Â); there is **no non-integer η-form remainder** to identify with 59.8.

2. **Unsigned mode-mixing** (the pair-production-type content): `∫_{[0,τ_fold]} Σ_k |dλ_k/dτ| / (2ω_k) dτ` with `ω_k = √(λ_k² + Δ_BCS²)` — the adiabaticity-violation measure. At L=8 full this is **759.84** (a structural-form diagnostic, NOT a calibrated count — the calibrated pair count is W3-1's `N_pair_eff = 5.489` from the actual Bogoliubov ODE). This is a **DIFFERENT functional**: the *unsigned* (mode-mixing) family integral, not the *signed* (asymmetry-transport) one.

**These two families-objects are structurally orthogonal**: one is `O(10⁻¹³)≈0`, the other is `O(10²)`. The [SIGN] equality `|η-form − 59.8|/59.8 = 1.0000` (≫ 5% band) is **FALSIFIED at the sign level** — but NOT because "no η-form exists" (the FAIL fork); the η-form *does* exist and equals 0. This is the **INFO fork**.

**[SIGN] substitution chain (with substituted numbers)**:
- *Step 1 (Definitions)*: η-form := `∫_{[0,τ_fold]} (d/dτ)[Σ_k sgn(λ_k(τ)) e^{−(λ_k/Λ)²}] dτ` (Bismut-Cheeger transgression, Paper 02 / Paper 12 APS=spectral-flow, η-invariant boundary term). N_pair := `Σ_k mult_k |β_k|² = 5.489` (W3-1 locked) or 59.8 (S38 c_continuum). Families splitting `Index = ∫Â + η-form`, `sf=0` (S61, gap 0.82 M_KK) fixes ∫Â integer.
- *Step 2 (Substitute)*: the BDI spectrum is `{+|λ|, −|λ|}` in equal multiplicity ⇒ `η(D_K(τ)) = Σ_{|λ|}[+g(|λ|) − g(|λ|)] = 0` pointwise ⇒ the integrand `(d/dτ)[0] = 0`.
- *Step 3 (Simplify)*: η-form `= η(τ_out) − η(τ_in) = 0 − 0 = 0`, INDEPENDENT of L (verified L=8/10/12: −1.5e−13, 0, 0). The unsigned mode-mixing `Σ|dλ/dτ|/2ω = 759.8 ≠ 0` — a distinct, non-cancelling functional.
- *Step 4 (Direction read-off)*: predicted PASS direction was "match ratio → 0". Computed: `|η-form − 59.8|/59.8 = 1.000` (the η-form is 0, not 59.8). **The equality SIGN FAILS** (`sign_verdict = FAIL`); the magnitude is off by ~100% (`magnitude_verdict = FAIL`); the computation IS within its regime — the structural zero is the CORRECT families-index result, not a method breakdown (`regime_verdict = VALID`).
- *Step 5 (Conclusion)*: the bridge-map CLASS (adiabatic-limit families-index η-form) exists and is computable; it yields a **Level-1 cohomology identity η-form ≡ 0**, NOT a quantitative match. The physical pair-production lives on the **non-self-adjoint Dirac-Schrödinger D + V(τ) families object** (van den Dungen Paper 09, 1710.09206 — `ind(D+V) = ⟨[V],[D]⟩`), whose spectral flow is the |β_k|² mode-mixing content; NOT the self-adjoint D_K family η-form. The operational gate (forward) is this re-identification.

**Composite-collapse note (plan-frozen INFO fork)**: the generic collapse rule (`gate-verdicts.md`) gives `sign=FAIL ⇒ composite=FAIL`. The plan-frozen `INFO_meaning` explicitly covers "η-form computed but match qualitative / Level-2 non-binding → REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT", and the plan `dual_prior` discriminator maps INFO → 0.9 Track B (slot reserved, operational-alignment forward gate). The structural reading honors the plan's INFO rubric: the bridge-map class is established (as a Level-1 ZERO identity), the quantitative match fails. The 3-tuple records the faithful `sign=FAIL` on the equality; the composite is the plan-anticipated INFO.

**FULL cross-pillar-bridge block (5 IS-not-IN anatomy elements + 3-level ladder)**:

- **Element 1 — substrate-IS observable**: the Bismut-Cheeger η-form of the finite-L τ-family `{D_K^{≤L}(τ)}_{τ∈[0,τ_fold]}`. **Level declaration: Level-2 (MODULI-DEFORMATION substrate-IS)** per `phononic-framing.md §"Single-τ-slice vs moduli-deformation"` — the τ-family across [0,τ_fold] IS the substrate's intrinsic Jensen-deformation manifold, NOT a meta-container coordinate. **Computed value: η-form = 0** (Level-1 identity; L8 full −1.5e−13, L10/L12 cache-sat 0).
- **Element 2 — laboratory-IN observable (OE-form)**: `P_ζ(k) = ∫_{[0,τ_fold]} Tr_{H_K}( P_{pair} · (dD_K/dτ) e^{−s D_K²} ) dτ |_{transit→CMB transport}` — integration domain `∫` over the transit τ-interval, trace `Tr_{H_K}` (the η-form spectral-asymmetry trace), named projector `P_{pair}` (the Bogoliubov pair-production projector onto the produced-quasiparticle sector; not a generic P). The lab measures `P_ζ(k)` (the CMB primordial power-spectrum amplitude/tilt) IN the continuum sky (Planck/LiteBIRD/CMB-S4). **FIDELITY CAVEAT**: with `P_{pair}` projecting onto the η-form (signed-asymmetry) trace, this OE-form evaluates to 0; the physical `P_ζ(k)` is sourced by the *unsigned* mode-mixing, i.e. the `D+V(τ)` non-self-adjoint families object, NOT the self-adjoint D_K η-form. The OE-form as written is the η-form image; its structural zero IS the finding.
- **Element 3 — bridge map**: the Bismut-Cheeger η-form **ADIABATIC-LIMIT class** (Paper 02 families index / Paper 12 APS & spectral flow / Bismut-Cheeger 1989 η-form). **EXPLICITLY NOT HKR** (FWD-C3 / §VII.W's map) and **NOT the Connes-Karoubi pairing** (FWD-C2 / §VII.AV's map) — Hybrid-Independence-Test criterion (iii) distinct-bridge-map-class is satisfied. **Scheme suffix** (Element-3 multi-scheme discipline): `convention=...-Bismut-Cheeger` (the adiabatic-limit η-form reading, distinct from APS-1975-secondary-class and Cheeger-Simons full-leaf readings — the same three-scheme axis as S88/S91 GV-Heitsch). **Binding incarnation** (Element-3 fiducial-anchor binding): substrate-self-consistent (the pair-production target is a framework prediction at the same algebra-axis family, S38), NOT an external-observation pin.
- **Element 4 — algebraic envelope**: the Level-2 `L^{−α}` convergence-rate bound. **Sub-class DECLARED: Level-2-NON-BINDING.** The η-form is identically 0 at every L (machine floor: L8 −1.5e−13, L10/L12 0) — it is a **STRUCTURAL FLOOR (Level-1 cohomology identity), NOT a binding `L^{−α}` continuum image** to 59.8. There is no `c_continuum`-binding adiabatic-limit map for the η-form because the η-form does not converge TO 59.8 — it is structurally 0. Per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"`, **Level-2-non-binding is FORBIDDEN for registry-PASS** ⇒ INFO / slot reserved.
- **Element 5 — empirical anchor**: at canonical `L_max=12`, η-form = 0 (cache-saturation), vs the c_continuum reference 59.8 (S38) and the W3-1 locked count 5.489. **Level-3 residual = |0 − 59.8| = 59.8 ≫ Level-2 floor** ⇒ Level-3 does NOT satisfy a binding Level-2 (there is none). Registry-PASS criterion `Level-3 < Level-2 at canonical L_max` is **not met** (and would be counted toward PASS only if Level-2 were binding, which it is not). **`L_max=12` reached via STRUCTURAL-SATURATION from `s84_spectrum_cache_L12_tau019.npz`** (the irrep CONSTRUCTION at p+q≥10 is empirically infeasible — `np.kron` 52 GiB blow-up in `irrep_symmetric_power`; `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility"`); the η-form is an L-INDEPENDENT Level-1 identity, so the cache fold-slice CONFIRMS (not refines) the structural floor — disclosed in the verdict `# OPERATIONAL-DEVIATION` row.

- **3-level structural-confidence ladder**:
  - **Level 1 — Substrate-IS structural identity (cohomology-class)**: STRUCTURAL THEOREM, regulator-invariant, L-independent. `Index({D_K(τ)}) = ∫Â (local, integer) + η-form (non-integer)`. `sf=0` (J-protected, S61) fixes ∫Â integer; the η-form is the well-defined non-integer remainder. **Here the remainder = 0** (BDI ±-symmetry ⇒ η-invariant ≡ 0 at every τ ⇒ transgression ≡ 0). Verified L-independent: L8 −1.5e−13, L10 0, L12 0. THIS IS THE LANDED RESULT.
  - **Level 2 — Algebraic convergence envelope**: STRUCTURAL PREDICTION. Sub-class **NON-BINDING** — the η-form is a machine-floor structural identity at every L, NOT an `L^{−α}`-convergent quantity with a continuum image binding to 59.8.
  - **Level 3 — Empirical anchor at canonical L_max=12**: η-form = 0 ≠ 59.8 (match ratio 1.000 ≫ 5% band). Registry-PASS NOT achieved (Level-2 non-binding + Level-3 residual exceeds any envelope).

- **Constraint-map consequence**: **FWD-C1 via the Bismut-Cheeger η-form route ⇒ INFO**, slot reserved **REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT** (NOT STAGE-1 — there is no binding Level-2). The Hybrid-Independence-Test K-counter advancement via criterion (iii) (NEW bridge-map class) is **conditionally seeded but NOT consummated**: the bridge-map class is genuinely distinct (adiabatic-limit η-form, not HKR/Connes-Karoubi), but per `cross-pillar-bridge-anatomy.md §"Two-clause separation"` the K-counter advances on a calibration-LANDING (registry-PASS-eligible entry), and this entry is registry-INCOMPLETE — so it records as a **calibration LANDING candidate pending operational-alignment**, not a consummated K-advance. As the **6th A_s route**: the η-form route does NOT deliver an A_s-normalization handle as hypothesized — the η-form is 0, carrying no normalization content; the genuine A_s handle would be the **unsigned `D+V(τ)` mode-mixing** object, which is the operational-alignment forward gate (cross-linked to INV12-W4-1 + INV12-W4-3). **Honest A_s-route status: the Bismut-Cheeger η-form route is structurally CLOSED for A_s normalization (η-form ≡ 0); the live handle migrates to the non-self-adjoint D+V(τ) families spectral flow.**

- **4-tuple**: `(value=match_ratio=1.000, scheme=Bismut-Cheeger-adiabatic-eta, convention=RATIO-Bismut-Cheeger, L_max=12)`. **publication_precision=4** (downstream W4-1/W4-3 rel_tol ≥ 1e-4, Class 8.3). schema-v2 3-tuple `(FAIL, FAIL, VALID)`. dual-SHA `audit=934b66e4…`, `content=681d6fb2…`.

**Track-local boundary honored**: this is a registry-eligible bridge landing, but per the orchestrator override + `gate-verdicts.md §"Investigation-Track"`, an investigation cannot mutate `permanent-results-registry.md` — the landing is recorded here in the WP and routes to session-promotion at investigation close. NO write to the curated session-track register was performed.

---

## Wave 2 Synthesis (team-lead)

**Per-gate roll-up** (all 5 verified on disk):

| Gate | Verdict | Result | Constraint-map move |
|:-----|:--------|:-------|:--------------------|
| W2-1 S-CROSS-OFF-JENSEN-BOUND | **PASS** | \|S_cross\|/S_base = 3.873e-4 at δ=0.05, 25.8× below 1e-2; δ→0 recovers A=T=0 EXACT | on-Jensen-only conditional (U-1) DISCHARGED for the moduli direction; G_N/n_s need not be A=T=0-restricted |
| W2-2 A-N-POLE-CONVERGENCE-AUDIT | **PASS** [AUDIT] | 5/5 CLASS-I ζ-residues at DIVERGENT poles (a₀ marginal log-divergent at s=d/2=4); a₂-canary reproduces S109 bit-for-bit | topology(rigid)/geometry(fixed)/analysis(regulator-soft + L-unverifiable) split made explicit per-moment |
| W2-3 PAPER10-BCS-DRESSING-INVARIANCE | **PASS** | BdG dressing is a Paper-10 locally-bounded perturbation ⇒ [D_K+V_BdG]=[D_K] in KK(A_K,ℂ) EXACT (4 legs machine-exact) | S69 W5-G promoted per-case → STRUCTURAL THEOREM; mass-order/c_s²=0/w_a=0 dressing-invariant + off-Jensen-safe |
| W2-4 KREIN-LORENTZIAN-A0 | **PASS** | Krein-a₀ vs Euclidean-a₀ resolved (Krein split (16,8,8), linear J²=+1) | the DILUTION-CC Λ a₀ leg is signature-robust |
| W2-5 FWD-C1-BISMUT-CHEEGER-ETA | **INFO** | η-form structurally ZERO (−1.5e-13 @ L8 → 0.0 EXACT @ L10/L12 cache-saturation); η(D_K)=0 per S25/S35 | bridge-map CLASS exists + distinct (criterion iii) but Level-2 NON-BINDING → registry-PASS-INELIGIBLE; slot REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT |

**Structural reading** — the topology/analysis boundary verdict: the **topological** content (Kasparov-product K-homology class) is dressing-RIGID (W2-3, now a STRUCTURAL THEOREM) and signature-robust (W2-4), while the **analysis** side (a_n spectral moments → Λ, G_N) is regulator-soft and L-unverifiable (W2-2 — every a_n is a residue-subtracted continuation, not a cache limit) yet bounded off-Jensen (W2-1, O(δ²) leak 3.9e-4). The W2-5 result sharpens the A_s program: the η-form — a *signed* families-index handle — carries ZERO normalization content (η(D_K)=0 because D_K is self-adjoint BDI with ±-symmetric spectrum and a gap that never closes), so the principled A_s bridge is structurally empty on the self-adjoint D_K. The live A_s handle migrates to the **non-self-adjoint D+V(τ) families spectral flow** (vdD Paper 09). Feeds: W2-3+W2-4 → W4-2 (SA-failure: topology dressing-safe ⇒ the failure must be analysis-side); W2-5 → W4-1 + W4-3 (η-form route closed).

**Effected In-Session** (non-math; investigation track registry-quarantined — no session-track register mutation):
- [x] No in-track register edits — W2-2's HY6 pole-status registry-lift and W2-3's S69 W5-G → STRUCTURAL-THEOREM promotion are session-track register actions; both route to session-promotion at `/rclab-investigate --investigation 12` close. Recorded in the WP gate sections + mirrored to housekeeping ledger §D.

## Carry-Forward Computations

### CF-INV12-W2-A — FWD-C1 operational-alignment via the non-self-adjoint D+V(τ) families spectral flow

| Field | Specification |
|:------|:--------------|
| **What** | Realize FWD-C1 on the operational-alignment axis: compute the spectral flow / index of the non-self-adjoint Dirac-Schrödinger family D_K+V(τ) (vdD Paper 09, ind(D+V)=⟨[V],[D]⟩) and identify it with the unsigned mode-mixing \|β_k\|²=N_pair (the η-form being structurally 0 carries no normalization content — the unsigned content lives on the non-self-adjoint object). Lands or closes the FWD-C1 slot held REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT. |
| **Inputs** | W3-1 locked {α_k,β_k} (`inv12_w3_1_relic_spectrum_ode_lock.npz`); W2-5 η-form artifacts (`inv12_w2_5_*`); V_BdG block ‖V_BdG‖=\|Δ_BCS\|=0.4642547; D_K L12 cache. |
| **Gate** | NEW (van-den-dungen-bridge-theorist). PASS = ind(D+V) binds a Level-2 envelope to N_pair; INFO = symbolic-only no numerical anchor; FAIL = no families-index handle. **NOTE: this is the SAME object as the W4-2 forward gate (INV13 KREIN-MODULAR-PAIRING-SIGN) approached from the families-index side — consolidate at session-promotion; do NOT double-count.** |
| **Effort** | MEDIUM; ~1 agent-session. Depends on nothing un-landed. |

(No other W2 gate seeds a compute CF — W2-1/2/3/4 all closed PASS in-session; their register consequences are non-math, routed to session-promotion.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-17 | On-Jensen-only conditional (U-1) on G_N/n_s | conditional, A=T=0 only | DISCHARGED for moduli direction (W2-1 PASS) | O'Neill cross-term leak O(δ²)=3.9e-4 ≪ 1% off-Jensen |
| 2026-06-17 | S69 W5-G (BdG-dressing K-homology invariance) | per-case observation | STRUCTURAL THEOREM (W2-3 PASS) | Paper-10 locally-bounded ⇒ KK class EXACT |
| 2026-06-17 | DILUTION-CC a₀ signature dependence | untested under Lorentzian/Krein | signature-robust (W2-4 PASS) | Krein-a₀ = Euclidean-a₀ |
| 2026-06-17 | FWD-C1 (Pillar I↔II η-form bridge) | never landed | slot RESERVED REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT (W2-5 INFO) | η-form ≡ 0 (Level-1 identity), Level-2 NON-BINDING |
| 2026-06-17 | a_n pole-convergence status | unaudited | all CLASS-I divergent-pole; analysis-side = continuations (W2-2 PASS) | s ≤ d/2 for all 5 a_n |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict line |
|:-----|:-------|:------------|:------------|:------------|
| W2-1 | inv12_w2_1_s_cross_off_jensen_bound.py | ✓ | ✓ | PASS |
| W2-2 | inv12_w2_2_a_n_pole_convergence_audit.py | ✓ | ✓ | PASS [AUDIT] |
| W2-3 | inv12_w2_3_paper10_bcs_dressing_invariance.py | ✓ | ✓ | PASS |
| W2-4 | inv12_w2_4_krein_lorentzian_a0.py | ✓ | ✓ | PASS |
| W2-5 | inv12_w2_5_fwd_c1_bismut_cheeger_eta.py | ✓ | ✓ | INFO (5 emit rows) |

All verdict lines at `computations/investigation-12/inv12_gate_verdicts.txt`; sig_5 unique.
