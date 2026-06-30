# Session 86 Wave W13 — Inventory consolidation + framework registries (Results Working Paper)

**Session**: 86 | **Wave**: W13 | **Plan**: session-86-plan-w13.md | **Theme**: 7-gate consolidation wave for Session 86's observational pin commitments — 3 inventory-write gates (P11, P2, P1), 2 registry-create gates (P10, P8), 1 adjudication gate (P9), 1 canonical-constants update + 2 re-emissions (P12). Bulk effort is registry I/O + cross-reference plumbing; only P12 re-runs producing scripts.

## Gate Sections

### §W13-1. S86-MASTER-INVENTORY-W6-W13-LAND (mack-cosmic-bridge)

**Status**: CLOSED
**Gate ID**: `S86-MASTER-INVENTORY-W6-W13-LAND`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (every promoted observable is a substrate excitation pin — w_0/α_s/CGWB ρ_AC/f_NL_folded/A_s ε-sensitivity/lab-falsifier suite)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: Applying 6 PAIR-enrichments + 1 NEW lab-falsifier row class (#13–#21, 9 atomic predictions) to `falsifier-master-inventory.md` yields a self-consistent inventory with every row carrying scheme + convention + L_max + dual-SHA, with 0 row-count regressions.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-1.

**MCP Pre-Compute Audit**:
- `search_knowledge("falsifier master inventory")` → 10 hits; structural equation row from `session-86-plan-w14.md` confirms `S86-WATCHLIST-W1-EDIT` writes to this same file family with `audit_sha256=<closure of input-pin map>` template — registry-write protocol established. No prior closure subsumes P11.
- `search_knowledge("PAIR enrichment W6 W13")` → 1 closed_mechanism (`S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN`), 4 equation hits, 2 theorem hits. The W6-W13 portion synthesis sourced from `session-85-mack-synthesis-w6-13.md` §III.3 enumerates the 6 PAIR rows. No PRE-CLOSED — this gate IS the landing.
- `trace_entity("falsifier-master-inventory.md")` → 1 hit (W14 plan structural row); confirms file is canonical sole-writer location for mack-cosmic-bridge.
- `list_constants(pattern="r_FW|alpha_s_canon|f_NL_folded")` → 0 matches; W13-2 / W13-5 / W13-1 pin landing IS where these become canonical (cross-ref §W13-5 P12 for α_s).
- `search_knowledge("S86-LAB-SI-TRANSLATION verdict")` → 0 direct hits (FTS5 limitation; verdict file confirmed by direct grep at line 182 = INFO `'9-rows-populated'`). W11 C5 PREREQUISITE CLEARED.
- `search_knowledge("S86-LAB-FALSIFIER-EVOI-TREE")` → 0 direct hits (FTS5 limitation); confirmed by direct grep at line 197 = PASS `'9-rows-leveled-and-treed'`. W11 C6 PREREQUISITE CLEARED.

Pre-flight conclusion: no PRE-CLOSED; both W11 prerequisites cleared; proceed with FULL PAIR-enrichments + NEW row class (no PRE-REG-INCOMPLETE INFO clause).

**Verdict**:
```
S86-MASTER-INVENTORY-W6-W13-LAND: PASS -- value=row_class_count=13_PAIRs=6_NEW_atomic=9_PASS=1 scheme=registry-write convention=mack-9A-III.3 L_max=N/A audit_sha256=8da95e45fd526ff59b1fc76ad2dbfc854d7afc8f067ae829449ba611d3c26f72 content_sha256=088668f68b04d811b5fdfef0290be91a7e4fbbefd37e0fc06ed551d405a97c08 schema_version=R3
# audit_sha256_short=8da95e45fd526ff5 content_sha256_short=088668f68b04d811 # S86-MASTER-INVENTORY-W6-W13-LAND dual-SHA companion row (W9a-99 split); PAIRs_landed=6/6; NEW_class=#13-#21 (9/9 atomic); baseline_sha=fc44785a81b40b77; final_sha=088668f68b04d811; upstream=W11_C5,W11_C6,S82_W3-4,S85_W13-2,S85_W8-4,S86_W1c-8
```

**Results**:

- **row_class_count_after_landing**: 13 (= 12 baseline canonical observables [w_0, r dual-fn + 1.a sub-row, α_s, m_H, n_s, r_running, CGWB ρ_AC, sin²θ_W, f_NL_folded, N_eff, alpha_s SU(3) running, A_s] + 1 NEW row class lab-falsifier suite #13–#21 with 9 atomic predictions). Target 13 ACHIEVED.
- **4-tuple**: `(value=row_class_count=13_PAIRs=6_NEW_atomic=9_PASS=1, scheme=registry-write, convention=mack-9A-III.3, L_max=N/A)`.
- **CC1 (baseline-row-count ≥ 12)**: VERIFIED. The W1c-8 baseline file at SHA `fc44785a81b40b77` carried 1 explicit row + 1 sub-row but indexed 12 canonical observable slots per W6-W13 mack synthesis §III.1. P11 lands the canonical 12 + 1 NEW class.
- **CC2 (every-row-dual-SHA-presence)**: VERIFIED. All 6 PAIR rows (#1, #2, #3, #7, #9, #12) + 9 NEW class rows (#13–#21) carry `content_sha256` and `audit_sha256` fields. Field-presence ABSOLUTE check returned all 8 sub-checks True.
- **dual-SHA**: `audit_sha256 = 8da95e45fd526ff59b1fc76ad2dbfc854d7afc8f067ae829449ba611d3c26f72`; `content_sha256 = 088668f68b04d811b5fdfef0290be91a7e4fbbefd37e0fc06ed551d405a97c08` (= SHA-256 of final on-disk inventory).
- **Per-row diff summary** (full detail in `s86_w13_p11_master_inventory_w6_w13_land.json`):
  - **PAIR-1 (row #1, w_0)**: 3-row regulator-layer sub-pin table landed. L=8 = +0.0204 (W7-7 Zubarev branch-iv re-audit; pending-emit-pre-S87 tag); L=10 = w0_FW = -0.918 (Volovik partition canonical, from `canonical_constants.py`); L=12 lower = -0.998 (Zubarev convergent limit); L=12 upper = -0.842454 (W10-2 branch-iv substrate-compaction inside R_842). W10-2 audit-pin SHA referenced. Cross-reference to §W13-3 P9 PRIMARY-VALUE-RESOLVE active.
  - **PAIR-2 (row #3, α_s)**: framework prediction `alpha_s_inflation_framework = -0.068968` UNCHANGED (S50-51 identity n_s²−1 invariant). W13-2 joint-Fisher pin `f514d642fe2a80ac` landed. Cross-reference to §W13-5 P12 (Planck 2018 → Aiola+ 2020 ACT DR4 canon move) active.
  - **PAIR-3 (row #7, CGWB ρ_AC)**: Companion-null (C-regulator) column added with W13-2.Ω value `8.299e-58`. Documents (A) flat acoustic-class vs (C) Companion-null discriminator structure — LISA 2035 5+ OOM null below (A) band.
  - **PAIR-4 (row #9, f_NL_folded)**: 3-pathway projection table landed: S82-GGE-equilateral 0.0547 / S67-GGE-folded 0.129 / W9-3-analytic-template-folded 0.7685. All 3 within Planck 1-σ (-26±21). Cross-reference to §W13-2 P10 authoritative `f-nl-folded-pathway-registry.md` active.
  - **PAIR-5 (row #12, A_s)**: ε-sensitivity sub-note added: A_s_FW(ε=0.02163) = 3.11e-9 → A_s_FW(ε=0.020) = 4.27e-9 spans ~37%. ε_pivot is S86 SECTOR-1 carry-forward (W5a P3 FOLD-PIVOT-RUNNING-FLOW-SECTOR-1) — sequencing pointer landed.
  - **PAIR-6 (row #2, r cross-ref)**: minimal annotation pointing to §W13-7 P2 BOTH-Pathways landing (SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030 + 36.5% scheme-floor flag). Per orchestrator override, P11 added the cross-reference annotation only; P2 (W13-B) writes the detector chain content.
  - **NEW row class #13–#21 (9 atomic predictions)** — all sourced from W11 C5 SI translation (audit `6a2d523920c34032`) + W11 C6 EVOI level (audit `8f1210e9a1123bf3`):

    | # | obs_id | platform | λ-direction | δE_a (W8_4_ratio) | SI value | σ_detect | det_ratio | EVOI_tier |
    |:-:|:-------|:---------|:------------|:-------------------|:---------|:---------|:----------|:----------|
    | 13 | SW1 | 3He-A | λ_6 | 1.7267 | 58.96 MHz | 0.001 MHz | 58958.86 | LAB-FALSIFIER-A |
    | 14 | SW2 | FeSe | λ_7 | 1.8226 | 364.52 ppm | 5.0 ppm | 72.90 | LAB-FALSIFIER-A |
    | 15 | SW3 | 173Yb | λ_8 | 2.8500 | 1.425 s⁻¹ | 0.05 s⁻¹ | 28.50 | LAB-FALSIFIER-A |
    | 16 | XA1 | 3He-A | λ_6 | 1.7267 | 58.96 MHz | 0.001 MHz | 58958.86 | LAB-FALSIFIER-A |
    | 17 | XA2 | FeSe | λ_6 | 0.7674 | 153.48 ppm | 5.0 ppm | 30.70 | LAB-FALSIFIER-A |
    | 18 | XA3 | 173Yb | λ_6 | 5.4938 | 2.747 s⁻¹ | 0.05 s⁻¹ | 54.94 | LAB-FALSIFIER-A |
    | 19 | XB1 | 3He-A | λ_7 | 0.5756 | 19.65 MHz | 0.001 MHz | 19652.95 | LAB-FALSIFIER-A |
    | 20 | XB2 | FeSe | λ_7 | 1.8226 | 364.52 ppm | 5.0 ppm | 72.90 | LAB-FALSIFIER-A |
    | 21 | XB3 | 173Yb | λ_7 | 13.1852 | 6.593 s⁻¹ | 0.05 s⁻¹ | 131.85 | LAB-FALSIFIER-A |

    All 9 rows in LAB-FALSIFIER-A level (decisive: detection_ratio ≥ 10). Each row carries P_decisive = 0.30–0.50 (5-yr 2031 horizon) + 5-yr decision tree pointer to `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.json:rows[i]` (4-branch tree per row: PASS-AT-LAB / REGISTERED-NO-CLOSE / FAIL-AT-LAB / UNINFORMATIVE-NULL) + source_gate_SHA = closure_hash(W8-4 audit + W11 C5 audit + W11 C6 audit).

- **Substrate-framing assessment** (per `.claude/rules/phononic-framing.md`):
  - The PAIR-enriched rows are substrate excitation channels in observational coordinates: w_0 IS the spectral-action gradient at the fold projected onto the late-time accelerating sector; α_s IS the running of the GGE-acoustic spectral tilt (second derivative of GGE quasiparticle dispersion at the pivot scale); CGWB ρ_AC IS the GGE relic tensor power partition (B2-mode flat-band fraction from the Mach-13.75 supersonic transit); f_NL_folded IS the three-point coupling among GGE quasiparticles in the folded triangle limit; A_s IS the substrate-curvature pivot amplitude. These are NOT LCDM parameters re-fit to data; each row is a substrate-derived prediction frozen against future detection.
  - The NEW row class #13–#21 frames the laboratory observables as direct cross-platform substrate-parameter verification, NOT analog cosmology. The 3He-A NMR Kelvin-wave shifts (λ_6 sweet-spot direction) probe the substrate's δω_K/ω_K ratio at the M_KK = 7.43e16 GeV compactification scale; FeSe Knight-shift anisotropy ppm probes the same substrate at the λ_7 direction; 173Yb 3-body loss s⁻¹ probes at λ_8. The detection_ratio = SI_value / σ_detect quantifies how many σ above lab floor each prediction sits — these are not analog modeling of cosmological signals; they are the substrate's predictions for laboratory measurements along the same Jensen-deformation directions that fix cosmological w_0/α_s/r/A_s. A non-detection at lab precision falsifies the substrate-direction along that λ in the laboratory frame, with cosmological consequences via the same Jensen-deformation tensor.
  - All 13 row classes (12 canonical + 1 NEW) are PHONONIC: substrate excitation channel (cosmological frame) + substrate excitation channel (laboratory frame) — same fabric, two projection angles. Substrate-first reasoning preserved throughout the registry text (Provenance + Substrate framing sections explicitly chain D_K spectral moments → emergent observable).

- **Artifacts on disk** (verified post-execution):
  - `computations/s86_w13_p11_master_inventory_w6_w13_land.py` — 41037 bytes, executable
  - `computations/s86_w13_p11_master_inventory_w6_w13_land.json` — 11214 bytes, 239 lines (per-row diff log + input pin map + machinery pin map + substrate-framing assessment block)
  - `sessions/framework/registry/falsifier-master-inventory.md` — 16933 bytes, 127 lines (was 4260 bytes / 64 lines pre-landing); SHA `088668f68b04d811...`
  - Verdict line + companion row appended to `computations/s86_gate_verdicts.txt` at lines 203–204

**Solution-space interpretation** (per plan §11):

PASS implications (LANDED):
- Master inventory is now the authoritative single-page summary for downstream sessions to cite. Future gates citing "the framework's r prediction" or "the framework's f_NL_folded prediction" point to a row in this file with a dual-SHA pin, eliminating the citation drift class observed in S78-W3-G that forced the SDW-KMS divergence.
- Row #1 carries a 3-row regulator-layer sub-pin table (L=8 / L=10 / L=12) as the canonical machinery-pin reference for any DR3 sub-tree gate that needs to specify which L_max the framework's w_0 is asserted at. The W10-2 LOCKOUT-C audit-pin reference makes the geometric-pin status explicit.
- Row #3 (α_s) preserves the framework prediction across the §W13-5 P12 canon move: only the observational reference moves (Planck 2018 → Aiola+ 2020 ACT DR4); the framework is unchanged. This separation is now SHA-pinned.
- The 9 lab-falsifier predictions in the NEW row class are now SHA-tagged with full source_gate closure hash — Aalto/Helsinki, Florence/Grenoble, Florence/JILA/Munich experimentalist contacts can cite the exact framework prediction + literature anchor (lit_sha) + EVOI level in any proposal without ambiguity.

Counterfactual (FAIL would have meant): master inventory remains ambiguous; downstream sessions risk re-citing pre-W13 stale values. Each missing PAIR-enrichment would have been a row promoted in S87-W0; each missing atomic prediction would have been a single-line registry edit deferred to S87.

PRE-REG-INCOMPLETE (not triggered): would have fired if W11 C5 or C6 had not landed. Both VERIFIED at lines 182 (C5 INFO) and 197 (C6 PASS) of `s86_gate_verdicts.txt`, so the FULL gate body executed.

---

### §W13-2. S86-FNL-FOLDED-PATHWAY-REGISTRY (mack-cosmic-bridge)

**Status**: CLOSED
**Gate ID**: `S86-FNL-FOLDED-PATHWAY-REGISTRY`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (f_NL_folded IS three-point GGE-quasiparticle coupling in folded triangle limit — substrate inter-band coherence projected onto post-transit acoustic modes)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: Consolidating 3 framework f_NL_folded pathway predictions (S82 GGE-equilateral 0.0547 / S67 GGE-folded 0.129 / W9-3 analytic-template-folded 0.7685) into a single dedicated registry yields a 3-row table with each row carrying scheme + convention + L_max + 64-char SHA + cross-references back to source verdict lines.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-2.

**MCP Pre-Compute Audit**:

- `search_knowledge("f_NL folded pathway")` — 20 hits across `equation`, `open_channel`. Confirms `f_NL_folded = 0.129` is the canonical S67 value (s69, s70 cross-checks); `s85_w9_folded_triangle_21cm_shape.py` produces the analytic-template form. No prior pathway-registry exists — registry-CREATE corridor open.
- `search_knowledge("GGE bispectrum")` — provenance returns S67 producing-script `s67_gge_bispectrum.py`, S74 `s74_gge_bispectrum.py`; theorem-table cite `GGE-BISPECTRUM-67` with `f_NL prediction from in-in formalism. Unique folded-triangle shape`. Confirms 3-pathway sub-channel structure (equilateral / folded / multi).
- `trace_entity("f_NL_folded")` — 1 open_channel hit (`f_NL (folded) | 0.129 | unconstrained`), 10 equation hits. Pre-existing master-inventory row #9 PROJECTS this registry; no canonical pathway disambiguation yet — gap this gate fills.
- `query_entity("gates", "S82-W3-4-GGE-FNL-CHANNEL")` — no entity in `gates` table; resolved by direct read of `computations/s82_gate_verdicts.txt` line 34 (PASS, value 5.470224e-02, sha256 `fe8c7d0e6b96187d5139a78adbea67a67736d75e555488fd9aa4c47889b483c9`).
- `query_entity("gates", "S67-GGE-BISPECTRUM-67")` — no entity in `gates` table (pre-S81 INFO verdict, no SHA-pinned verdict file). Resolved by direct read of `sessions/archive/session-67/session-67-results-workingpaper.md` §W2-C: "Gate verdict: GGE-BISPECTRUM-67 = INFO" + "f_NL^{diag} = 0.129". Content SHA pulled from producing script `s67_gge_bispectrum.py` (pre-S81 fallback identity).
- `query_entity("gates", "S85-W9-3-ANALYTIC-TEMPLATE-FOLDED")` — no entity in `gates` table; resolved by direct read of `computations/s85_gate_verdicts.txt` line 161 (PASS, value 0.7685380225919217, audit_sha256 `2484b4a24419329157645bfbd5426b77d861649bc02a05c2a7dc7cd3a78ee274`, content_sha256 `d0f08fb302eb13fc5779ca608c5c5b532ef38329e286df991bf5434510d87c1c`).
- Closure status: NOT PRE-CLOSED. Registry-CREATE event is novel; the 3 source verdicts are pre-existing but their pathway-disambiguation registry is being created at this gate.

**Verdict**:

`S86-FNL-FOLDED-PATHWAY-REGISTRY: PASS -- value=3 scheme=registry-create convention=mack-9A-VI.8 L_max=10 audit_sha256=2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3 content_sha256=a9cc92cafda8d51de62e282840c779d317849de018bdc49f02cd776c25d2a7bd schema_version=S84+`

**Results**:

- **Row count**: 3 / 3 target (PASS) — `S82-GGE-equilateral`, `S67-GGE-folded`, `W9-3-analytic-template-folded`.
- **Output 4-tuple**: `(value=3, scheme=registry-create, convention=mack-9A-VI.8, L_max=10)` — matches plan §W13-2.8 expectation exactly.
- **CC1 source-value exact-echo verification (PASS)**:
  - `S82-GGE-equilateral`: expected `0.0547`, got `0.0547` (4-sig-fig display of full-precision `5.470224e-02` from S82 verdict line 34) — OK
  - `S67-GGE-folded`: expected `0.129`, got `0.129` (verbatim from session-67 working-paper §W2-C) — OK
  - `W9-3-analytic-template-folded`: expected `0.7685`, got `0.7685` (4-sig-fig display of full-precision `0.7685380225919217` from S85 verdict line 161) — OK
  - All three values match within 0 tolerance (exact string echo).
- **CC2 8-column field presence (PASS)**: every row carries all 8 required columns `[Pathway_ID, f_NL_folded, scheme, convention, L_max, source_gate, content_sha256, audit_sha256]`. Verified by post-write disk round-trip parser (Section 10 of producing script): re-read the markdown table, confirmed 3 rows × 8 cells.
- **Registry-CREATE abort-if-exists check (PASS)**: `sessions/framework/registry/f-nl-folded-pathway-registry.md` did NOT exist at script entry; the OUT_MD.exists() pre-flight check confirmed registry-CREATE corridor was open. Had it existed, the script would have ABORTed with a FAIL verdict and `value="REGISTRY-EXISTS"` per plan §W13-2.6 verification step 1.
- **Dual-SHA**:
  - `audit_sha256 = 2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3` (closure hash of the 7-entry input pin map: framework-directory listing + s82/s85 verdict files + S67 working paper + S67 producing script + 2 mack memory files).
  - `content_sha256 = a9cc92cafda8d51de62e282840c779d317849de018bdc49f02cd776c25d2a7bd` (SHA-256 of the emitted `f-nl-folded-pathway-registry.md` file bytes).
  - Companion comment row written to `s86_gate_verdicts.txt` per S81+ dual-SHA discipline.
- **Artifacts on disk**:
  - `computations/s86_w13_p10_fnl_folded_pathway_registry.py` (31416 bytes; producing script)
  - `computations/s86_w13_p10_fnl_folded_pathway_registry.json` (3828 bytes; full construction log incl. row inventory + input pin map + closure hash)
  - `sessions/framework/registry/f-nl-folded-pathway-registry.md` (6844 bytes; NEW registry file with header + methodology + 3-row table + pathway-comparison + detector-correspondence + input-pin-map subsections)
  - Verdict line + companion comment row appended to `computations/s86_gate_verdicts.txt` (final 2 lines).
- **Pathway spread (the structural finding)**: `0.0547` / `0.129` / `0.7685` span ~14× across the three sub-channel projections. This is methodological spread — three distinct reductions of the substrate inter-band coherence — not measurement uncertainty. The W9-3 analytic-template projection (`0.7685`) is the ONLY pathway reaching detector-discriminability in the 2030s instrument suite (SKA-1 at the folded ridge, sigma ~ 0.15 per S85 W9-3 INFO). The S82 GGE-equilateral (0.0547) and S67 GGE-folded (0.129) values are detector-sterile in the current horizon (CMB-S4 sigma 6.9, Planck sigma ~5.7).
- **Substrate-framing assessment**: registry preserves PHONONIC framing throughout. The §Methodology subsection states explicitly that f_NL_folded IS the three-point coupling among GGE quasiparticles in the folded triangle limit, projected from substrate inter-band coherence onto post-transit acoustic modes — not a measurement of an "inflaton non-Gaussianity in a curved-spacetime container." The 3 pathways are sub-channel projections of the SAME substrate observable, not 3 competing models. Downstream substrate-prediction citations of "the framework's f_NL_folded prediction" are now required to specify the pathway tag (S82-GGE-equilateral / S67-GGE-folded / W9-3-analytic-template-folded), eliminating the conflation hazard called out in plan §W13-2.11.
- **Solution-space update**: pre-this-gate, "the framework's f_NL_folded" was an ambiguous reference whose value silently consumed whichever sub-channel a downstream gate picked. Post-this-gate, the 3 pathways are individually pinned (each at <0.6σ of Planck 2018 −2.5 ± 5.7), the master-falsifier-inventory Row #9 has an authoritative back-pointer, and SKA-1 is identified as the primary discriminator for the W9-3 pathway. No pathway is excluded; all are consistent with current data.

---

### §W13-3. S86-W0-PRIMARY-VALUE-RESOLVE (sagan-empiricist)

**Status**: CLOSED — PASS
**Gate ID**: `S86-W0-PRIMARY-VALUE-RESOLVE`
**Trigger**: `[AUDIT]` + `[SIGN]`
**Classification**: **PHONONIC** (w_0_FW IS late-time projection of substrate's spectral-action gradient at fold)
**Agent**: `sagan-empiricist` (mack self-blacklist: own-carry-forward adjudication; cosmic-web-theorist as second-choice)
**Hypothesis**: A pre-registered decision rule selecting either w_0_A=-0.918 (Volovik partition, S5) or w_0_B=-0.842454 (substrate-compaction, W10-2) as PRIMARY can be derived from 4 independent criteria (theoretical-priority + DR3-rectangle-membership + falsifiability + registry-history) without invoking post-hoc data-fitting; PRIMARY designation is REVERSIBLE under DR3-trigger conditions.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-3.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("w_0 primary substrate compaction Volovik partition")` → 10 hits, including the plan-cited equation `w_0_B = -0.842454 (S85 W10-2 branch-(iv), substrate-compaction)` and `wa_FW = 0.0` Volovik substrate-compaction partition; canonical references confirmed.
- `get_constant("w0_FW")` → `-0.918` (no PROVENANCE entry; canonical pin matches S5 row #1 / Volovik partition; downstream-citation discipline preserves this value as PRIMARY).
- `trace_entity("S86-DR3-W0-FALSIFIER-REGISTRATION-74")` → no trace found (entity not yet registered; deferred to S87+ or pre-created via cross-reference in `falsifier-master-inventory.md` Row #1 footnote update by P11).
- `trace_entity("S84-W1b-9-DR3-RESPONSE-PROTOCOL")` → 3 hits confirming `R_842 = [-1.05, -0.85] × [-0.2, +0.2]` plan-prompt envelope AND mack-9A canonical `R_842 = [-0.942, -0.742] × [-0.2, +0.2]` (center -0.842, half-widths 0.100/0.200); both rectangles documented in §1 of `w0-primary-decision-rule.md`.
- `query_entity("gates", "S85-W10-2")` → no exact gate-ID match; canonical anchor for B=-0.842454 lives at gate `S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT: PASS` (audit_sha256=`8de72cde7d635949f45716191288da6656f8a9fe05411532ab848fdb93fd04e8`; content_sha256=`b9a6a3014218386add94df8fef1034df5e17feb467c4d4b9cecacadfb133cd09`; offset 0.000454 inside R_842).
- **PRE-CLOSED check**: NOT pre-closed. Adjudication required; both candidates remain live until decision rule lands.

**Verdict**:
```
S86-W0-PRIMARY-VALUE-RESOLVE: PASS -- value='PRIMARY=A=-0.918' scheme=4-criterion-adjudication convention=registry-history-priority L_max=N/A audit_sha256=8893fbc2ee44af27585268b01481eff5560817013ec3e60ae47ee0821ccaaf0a content_sha256=51b5584d5d807bc3bdb1b73954f2dcf36768f50b094fc34e50b078f46ffa5f7e schema_version=S84+
```
- **value**: `PRIMARY=A=-0.918`
- **scheme**: `4-criterion-adjudication`
- **convention**: `registry-history-priority`
- **L_max**: `N/A`
- **audit_sha256**: `8893fbc2ee44af27585268b01481eff5560817013ec3e60ae47ee0821ccaaf0a` (full 64-char; script+canonical+pinmap)
- **content_sha256**: `51b5584d5d807bc3bdb1b73954f2dcf36768f50b094fc34e50b078f46ffa5f7e` (full 64-char; script-only)
- **schema_version**: `S84+`
- **Pre-registered PASS criteria** (5/5 satisfied):
  1. Decision rule landed in `sessions/framework/registry/w0-primary-decision-rule.md` (12,774 bytes; 6 sections present).
  2. PRIMARY designated (`**PRIMARY = w_0_A = -0.918**` literal in §4 of decision-rule MD).
  3. Reversibility protocol pre-registered (§5 of decision-rule MD; DR3-trigger band [-0.86, -0.83] explicit).
  4. Both candidates cross-referenced (§1.1 + §1.2 of decision-rule MD).
  5. Adjudication arithmetic correct (Sage exact-rational + Python float64 cross-checked; arithmetic_correct=True).

**Results**:

**4-tuple**: `(value='PRIMARY=A=-0.918', scheme=4-criterion-adjudication, convention=registry-history-priority, L_max=N/A)`

**PRIMARY designation**: `w_0_A = -0.918` (Volovik partition, S5 row #1; matches `canonical_constants.py` `w0_FW`).

**SECONDARY-with-reversibility**: `w_0_B = -0.842454` (substrate-compaction, S85 W10-2 branch-(iv); preserved against DR3 reversal trigger).

**4-criterion adjudication table**:

| # | Criterion | A=-0.918 | B=-0.842454 | Verdict |
|:-:|:----------|:---------|:------------|:--------|
| 1 | theoretical-priority (more-fundamental substrate construction) | post-fold integral over expansion history | direct fiber-tau density at z=0 | **tie** (both first-principles) |
| 2 | DR3-rectangle-membership (mack-9A R_842 = [-0.942, -0.742]) | inside (offset 0.076, 76.0% of hw) | inside (offset 0.000454, 0.45% of hw) | **both inside** (neither excluded) |
| 3 | falsifiability (distance from LCDM, σ-units of DR3 fiducial 0.025) | d=0.082, n_σ=3.28 | d=0.157546, n_σ=6.30 | **B more discriminable** (Δn_σ=+3.022) |
| 4 | registry-history (canonical-pin longevity) | 28+ sessions (S58 → S85) | 0-1 sessions (S85 → S86) | **A long-standing** |

**Score**: A wins Criterion 4; B wins Criterion 3; ties on Criteria 1 and 2.

**Substitution chain** (per plan §W13-3.10; [SIGN] trigger MANDATORY; Python+Sage exact-rational verified):

```
Step 1 — Definitions:
  w_0_A = -0.918              (Volovik partition; canonical_constants.py current pin)
  w_0_B = -0.842454           (substrate-compaction, S85 W10-2 branch-(iv))
  w_0_LCDM = -1.0             (LCDM cosmological-constant equation of state, by definition)
  d(X) := |X - w_0_LCDM|       (Euclidean distance from LCDM in 1-D w-space)
  σ(w_0)_DR3 = 0.025          (DR3 fiducial sigma per S69 master synthesis)

Step 2 — Substitute (Sage exact rationals + Python float64):
  d(w_0_A) = |-0.918 - (-1.0)| = |0.082| = 0.082000           (= 41/500 exact)
  d(w_0_B) = |-0.842454 - (-1.0)| = |0.157546| = 0.157546     (= 78773/500000 exact)

Step 3 — Simplify:
  Δd := d(w_0_B) - d(w_0_A) = 0.157546 - 0.082000 = +0.075546  (= 37773/500000 exact)

Step 4 — Direction:
  Δd > 0 → d(w_0_B) > d(w_0_A) → w_0_B is FURTHER from LCDM than w_0_A.

Falsifiability corollary (DR3 σ(w_0) = 0.025 fiducial per S69 master):
  n_σ(A) = d(A)/σ = 0.082000/0.025 = 3.280000                  (= 82/25 exact)
  n_σ(B) = d(B)/σ = 0.157546/0.025 = 6.301840                  (= 78773/12500 exact)
  Δn_σ = n_σ(B) - n_σ(A) = +3.021840                            (= 37773/12500 exact)

  Direction: Δn_σ > 0 → DR3 will discriminate B from LCDM at +3.022σ MORE
  than it discriminates A from LCDM (under fiducial σ(w_0)=0.025).

Conclusion: under the falsifiability criterion (Criterion 3), w_0_B is more
discriminable; under the registry-history-priority criterion (Criterion 4),
w_0_A is the long-standing canonical. Decision rule: PRIMARY = w_0_A pending
DR3 publication; rule REVERSES to B if DR3 returns w_0 ∈ [-0.86, -0.83]
(per the pre-registered S84 R_842 lockout protocol).
```

**Pre-registered key numbers** (matches plan §W13-3.10 expectations):

| Quantity | Value | Exact rational |
|:---------|:-----:|:--------------:|
| d(A) | 0.082000 | 41/500 |
| d(B) | 0.157546 | 78773/500000 |
| Δd | +0.075546 | 37773/500000 |
| n_σ(A) | 3.2800 | 82/25 |
| n_σ(B) | 6.3018 | 78773/12500 |
| Δn_σ | +3.0218 | 37773/12500 |

**DR3 scenario tension table** (σ-distance of FW from each scenario, σ_DR3=0.025):

| Scenario | DR3 returns w_0 | n_σ for A=-0.918 | n_σ for B=-0.842454 |
|:---|:---:|:---:|:---:|
| A_LCDM | -1.0000 | 3.2800 | 6.3018 |
| B_w095 | -0.9500 | 1.2800 | 4.3018 |
| C_w086 | -0.8600 | 2.3200 | 0.7018 |
| B_precise_w091 | -0.9100 | 0.3200 | 2.7018 |

**Reversibility-trigger documentation** (per plan §W13-3.6 Step 6):

The PRIMARY designation A=-0.918 is REVERSIBLE under the following pre-registered protocol (§5 of `w0-primary-decision-rule.md`):

- **Reversal condition**: DR3 publication returns measured w_0 ∈ [-0.86, -0.83].
- **Action on trigger**: PRIMARY automatically flips A → B (substrate-compaction value -0.842454 becomes canonical).
- **Justification**: Within the [-0.86, -0.83] band, B is at most 0.70σ from the measurement while A is at least 2.32σ from the measurement; Bayes factor B/A ≥ exp((2.32² - 0.70²)/2) ≥ 11.1 in favor of B.
- **Anti-reversal**: if DR3 returns w_0 closer to A's band ([-0.95, -0.88]) or to LCDM ([-1.05, -0.95]), PRIMARY remains A.
- **Provenance**: S84 W1b-9 DR3-RESPONSE-PROTOCOL (R_842 lockout protocol; mack-9A canonical rectangle [-0.942, -0.742]).
- **Locked machinery** (cannot be retroactively re-tuned): reversal band edges [-0.86, -0.83], σ_DR3=0.025 fiducial, registry-history-priority dominant unless reversal triggers.

**Substrate-framing assessment** (per `.claude/rules/phononic-framing.md`):

w_0_FW IS the substrate's late-time spectral-action gradient projected onto observational coordinates. The two candidates A and B are NOT competing models; they are TWO METHODOLOGICALLY-DISTINCT projections of the SAME substrate observable:

- **A (Volovik partition)**: integrates the substrate-internal spectral-action gradient over the post-fold expansion history; output is the time-averaged effacement-residual coupling.
- **B (substrate-compaction)**: pinpoints w(z=0) directly from fiber-tau density tracking; output is the instantaneous late-time projection of the spectral-action gradient at z=0.

Both are first-principles substrate predictions. The PRIMARY designation is OBSERVATIONAL-CITATION discipline (which value downstream gates cite as canonical), NOT a physics ranking. The DR3 reversibility protocol is the substrate's external falsifier — the experiment, not the framework, decides which projection is the right substrate-coordinate at z=0. This satisfies the IS-not-IN reframe: A and B are not "two predictions in superspace" — they are two distinct spectral-functional projections of the substrate's z=0 fold-residual.

**Artifacts on disk**:

| Artifact | Path | Bytes |
|:---------|:-----|:-----:|
| Producing script | `computations/s86_w13_p9_w0_primary_value_resolve.py` | 45,256 |
| Machine-readable adjudication | `computations/s86_w13_p9_w0_primary_value_resolve.json` | 8,116 |
| Decision-rule registry (NEW) | `sessions/framework/registry/w0-primary-decision-rule.md` | 12,774 |
| Verdict line + dual-SHA companion | `computations/s86_gate_verdicts.txt` | (appended) |

**What PASS means for solution space**: the framework now has ONE primary w_0 prediction (A=-0.918) with explicit reversibility conditions ([-0.86, -0.83] DR3 band). Downstream sessions citing "the framework w_0" point to PRIMARY=A with documented reversibility trigger. The DR3 publication (window opened 2026-04-23 per S84-W1b-9) becomes the deterministic test that flips PRIMARY (or confirms it). The W10-2 vs S5-row-#1 conflation that mack-9A §VI.7 flagged is eliminated. The non-PRIMARY candidate B is preserved in the registry and pre-armed for promotion.

---

### §W13-4. S86-DR3-SUB-TREE-3-ROW-PIN (cosmic-web-theorist)

**Status**: **CLOSED** (INFO per spawn-prompt L=8 PRE-REG-INCOMPLETE FALLBACK; plan §W13-4.9)
**Gate ID**: `S86-DR3-SUB-TREE-3-ROW-PIN`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (DR3 sub-tree maps substrate's w_0/w_a prediction surface against BAO observational measurement; both axes are substrate observables — w_0 = spectral-action gradient at fold, w_a = first scale-derivative)
**Agent**: `cosmic-web-theorist` (mack self-blacklist: own-carry-forward source)
**Hypothesis**: Extending S85 W1b-1's 2-row DR3 sub-tree (L=10, L=12) to a 3-row tree (L=8 from W7-7 + L=10 + L=12) at 7 cells per row produces a 21-cell decision matrix with all cells deterministic AND monotone in L_max (no oscillation A→B→A across L_max), pre-registering a regulator-first DR3 adjudication protocol with 4 deterministic outcome branches.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-4.

**MCP Pre-Compute Audit**:
- `search_knowledge("DR3 sub-tree W1b-1 W7-7 L_max regulator")` → 15 hits; surfaces `S85-DR3-REGULATOR-SUCCESSOR-TREE` PASS at L_max=8 (15 leaves) and `S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE` FAIL flipping A1→B2 at L=12; the W1b-1 producing-script `s85_w1b_cf_m2_dr3_regulator_tree.py` carries the `# (local) NOTE: L_max=8 unavailable` annotation that grounds the L=8 PRE-REG-INCOMPLETE fallback.
- `trace_entity("S86-DR3-W0-FALSIFIER-REGISTRATION-74")` → no trace (gate ID absent from knowledge graph; falsifier slot tracked elsewhere via S84 W1b-9 + S85 W0-DR3-REGULATOR-SUCCESSOR-TREE).
- `trace_entity("S84-W1b-9-DR3-RESPONSE-PROTOCOL")` → 3 hits; pins R_842 = [-1.05, -0.85] × [-0.2, +0.2] from S84 W1b-9; locks the parent-gate rectangle and the LOCKOUT-A through LOCKOUT-G chain (no rectangle-resizing, no scheme-shopping, no dual-pin retreat, no w_a-axis migration, no post-2026-04-23 branch-(iv) redefinition, no tau_fold relocation).
- `query_entity("gates", "S85-W7-7")` → no canonical gate row in the gates table; the W7-7 verdict line lives in `computations/s85_gate_verdicts.txt:175` as `S85-W7-W0-RE-AUDIT-AT-L8: PASS value=0.0204` — a max-L-sensitivity scalar over an unrelated basket of 8 W_0-dependent constants {K_R5, K_substrate, K_crit, Gamma_effacement, f_conv, c_sub_at_kpivot, F_amp_linearized, f_GGE_Leggett}, NOT a w_0(L=8) value, NOT a 7-scenario decomposition.
- `query_entity("gates", "S85-W1b-1")` → no canonical gate row; the W1b-1 verdict line lives in `computations/s85_gate_verdicts.txt:38` as `S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE: FAIL value='FLIP-A1-to-B2-at-L12' L_max=enumerated{5,10,12}` (FLIP between cell A1 at L=10 and cell B2 at L=12 in the W4-44 7-cell partition).
- `get_constant("w0_FW")` → `-0.918` (S58 Volovik partition + effacement; canonical L=10 anchor).
- `get_constant("wa_FW")` → `0.0` (S74 W4-Z four-fold lock canonical).

**Verdict**:

```
S86-DR3-SUB-TREE-3-ROW-PIN: INFO -- value=21cells=14pop+7stub,mono=7/7 scheme=3-row-7-cell convention=mack-9A-VI.6 L_max=multi=[8,10,12] sha256=eccedb2a53dca48186ca131378c24e9c95772328706e97d066df578020100a11 schema_version=R3
# S86-DR3-SUB-TREE-3-ROW-PIN: audit_sha256=eccedb2a53dca48186ca131378c24e9c95772328706e97d066df578020100a11 content_sha256=8abdc38ff0d0c688b0663a5f726ecc97f2c8b7ca7e98cb5f373bd5214a6b50d5 dual-SHA-companion (W9a-99 split)
```

The verdict is INFO under the plan §W13-4.9 PRE-REG-INCOMPLETE INFO clause: the L=8 row's 7-scenario sub-cell decomposition is unavailable from the W7-7 source, so the gate emits INFO with the partial 14-cell + 7-stub matrix. Re-dispatch slot pre-registered for S87 after L=8 sub-cell extraction. INFO is NOT a degraded PASS; it is the pre-registered honest output of the scenario the plan anticipated.

**Results**:

- **4-tuple**: `(value=21cells=14pop+7stub,mono=7/7, scheme=3-row-7-cell, convention=mack-9A-VI.6, L_max=multi=[8,10,12])`. The `21cells=14pop+7stub` value-string conveys the populated/stub split; `mono=7/7` is column-monotonicity; the matrix-cell-count target 21 = 3 × 7 met by construction.
- **dual-SHA**: `audit_sha256=eccedb2a53dca48186ca131378c24e9c95772328706e97d066df578020100a11`, `content_sha256=8abdc38ff0d0c688b0663a5f726ecc97f2c8b7ca7e98cb5f373bd5214a6b50d5`. Verdict line + companion comment row in `computations/s86_gate_verdicts.txt:221-222`.
- **Cell-count breakdown**: 21 = 3 L_max × 7 scenarios. Populated 14 (L=10 row × 7 scenarios + L=12 row × 7 scenarios). Stub 7 (L=8 row × 7 scenarios). Cell-SHA-back-trace 21/21 (all L=10 / L=12 cells trace to the W1b-1 source verdict line `audit_sha256=beba9cad44f34103f...`; all L=8 stub cells flagged with the W7-7 source pin `dddf9edda82b4f3e...` plus PRE-REG-INCOMPLETE status, marking each as L=8-extraction-required for S87).
- **Framework prediction per L_max** (Zubarev scheme):
  - L=8: w_0 = PRE-REG-INCOMPLETE; W7-7 publishes only `max_L_sensitivity = 0.0204` over an unrelated basket of 8 W_0-dependent constants; no w_0 value, no 7-scenario decomposition. Occupied scenario UNAVAILABLE.
  - L=10: w_0 = -0.918, w_a = 0.0 (canonical w0_FW). Framework lands INSIDE R_842 (parent gate G42 PASS); for the 7 outside-R_842 W4-44 scenarios this row reports `PASS-PARENT` (parent-gate domination) in every cell.
  - L=12: w_0 = -0.635, w_a = 0.0 (S85 W1b-1 docstring step 3 / S85 W0-Zubarev L=12 extrapolation). Framework lands in scenario B2 (w_0-driven exclusion: w_0 > -0.742 quintessence-side, |w_a| ≤ 0.2 in lock).
- **Column-monotonicity (CC1, target 7/7 True)**: A1=True (degenerate, all-eq), A2=True (degenerate), B1=True (degenerate), **B2=True** (non-decreasing: STUB → PASS-PARENT → TENSION; STUB excluded from rank ladder, populated subsequence (PASS-PARENT, TENSION) non-decreasing under the partial order PASS-PARENT(0) ≤ TENSION(2) ≤ PASS(3)), B3=True (degenerate), C1=True (degenerate), C2=True (degenerate). Net: 7/7 True; zero oscillations across the 14 populated cells. No A→B→A flipping in any column.
- **Cell-SHA-back-trace (CC2, target 21/21)**: 21/21 traced. All L=10 / L=12 cells (14 populated) pin to the W1b-1 verdict line `beba9cad44f34103f...`. All L=8 cells (7 stub) flagged as L=8-extraction-required with the W7-7 source pin `dddf9edda82b4f3e...` annotated PRE-REG-INCOMPLETE.
- **Pre-registered 4-branch adjudication protocol**:
  - **(1) REG-INVARIANT**: trigger — all 3 L_max rows (L=8, L=10, L=12) for the DR3-occupied scenario column S* give the SAME decision_branch. Decision output — adopt the unanimous branch (PASS / TENSION / EXCLUDED). Substrate interpretation — w_0 prediction is REGULATOR-INVARIANT in this scenario (true substrate observable).
  - **(2) REG-DEP-MAJORITY**: trigger — 2 of 3 L_max rows agree, one dissents. Decision output — adopt majority branch AND flag dissenting L_max as a regulator-class flag in the scorecard. Substrate interpretation — w_0 prediction has REGULATOR-DEPENDENT residual at the dissenting L_max (truncation-axis sensitivity revealed at that L).
  - **(3) STRUCTURAL-AMBIGUITY-FREEZE**: trigger — all 3 L_max rows give different branches. Decision output — FREEZE adjudication; re-dispatch in S87 with refined L_max scan (e.g., L_max ∈ {7, 8, 9, 10, 11, 12, 13}). Substrate interpretation — w_0 prediction is STRUCTURALLY AMBIGUOUS across the L_max axis; the substrate eigenvalue computation has not converged in the W4-44 scenario partition; finer L_max sampling required.
  - **(4) EXTERNAL**: trigger — the column S* contains at least one PRE-REG-INCOMPLETE row. Decision output — DEFER to populated rows; emit EXTERNAL flag for S87 re-dispatch after L_max gap closure. Substrate interpretation — the regulator-stratified prediction surface has gaps; adjudication cannot conclude until the gap is closed by direct computation at the missing L_max.

  Branches registered: 4/4. Self-test on 7 W4-44 example points (A1, A2, B1, B2, C1, C2 plus INSIDE_R_842): 7/7 deterministic (same input → same branch on repeat invocation). Current sub-tree state (L=8 stubs in every column) routes ALL non-INSIDE_R_842 DR3 inputs to branch (4) EXTERNAL by construction; the INSIDE_R_842 example routes to PARENT-GATE (G42 dominates) with decision PASS-PARENT.

- **L=8 PRE-REG-INCOMPLETE INFO clause** (the structural finding): the L=8 stub row is the plan §W13-4.9 PRE-REGISTERED INFO sub-class, NOT a FAIL and NOT a degraded PASS. The plan explicitly anticipated this scenario: "if W7-7's L=8 row does not contain all 7 scenario sub-cells (only the headline value), the L=8 row is PRE-REG-INCOMPLETE and the gate emits INFO with the partial 14-cell + 7-stub matrix; re-dispatch in S87 after L=8 sub-cell extraction." The W7-7 verdict-line scope is L_max-stability across an unrelated basket of W_0-dependent constants under the ANALYTIC-SENSITIVITY-MODEL, not a 7-cell DR3 contingency decomposition at L=8. Per the spawn-prompt L=8 PRE-REG-INCOMPLETE FALLBACK, fabrication of L=8 cell content from the W7-7 headline scalar is structurally barred. The S87-W0 carry-forward slot is `S87-DR3-SUB-TREE-3-ROW-PIN-PROMOTION` — direct Zubarev w_0 extraction at L=8 from the L=8 D_K eigenvalue cache, scenario classification, fill 7 stubs, re-emit gate at PASS level.
- **Sibling gate distinction**: the S86 W12-4 sibling `S86-DR3-3-LAYER-SUB-TREE` (verdict file `computations/s86_gate_verdicts.txt:195`) reached an INFO verdict at value=`21/21,7/7` by constructing an L=8 w_0 via a canonical-anchored offset against the published Zubarev convergence series (`rho(L=8) = -0.504 + offset_-0.341 = -0.845`, occupying scenario A1 by classification). That is a STRUCTURALLY DISTINCT gate with a different fallback discipline — it permits offset-based reconstruction. P8 forbids fabrication; the spawn-prompt fallback is binding. The two gates' INFO verdicts agree on the structural outcome (the 3-row matrix is operative; L=8 row is the soft point) but differ on whether to populate L=8 by reconstruction or to flag the gap honestly. P8's discipline preserves audit-provenance integrity at the cost of leaving the L=8 row stubbed.
- **Files written**:
  - `computations/s86_w13_p8_dr3_sub_tree_3_row_pin.py` (51224 bytes; producing script with full docstring, 7-cell roster, classification predicate, monotonicity check, adjudication protocol + self-test, dual-SHA closure).
  - `computations/s86_w13_p8_dr3_sub_tree_3_row_pin.json` (11717 bytes; machine-readable matrix with cell entries, source pins, self-test results, determinism + monotonicity tallies, dual-SHA).
  - `computations/s86_w13_p8_dr3_sub_tree_3_row_pin.npz` (5755 bytes; numerical 3×7 rank array `matrix_ranks`, branch labels `matrix_branches`, occupancy flags `matrix_occupancy`, plus per-L_max w_0 / w_a / occupied scenarios, tallies, dual-SHA).
  - `sessions/framework/registry/dr3-3row-7cell-subtree.md` (8296 bytes; NEW registry file with header + 7-cell scenario roster + framework-prediction-per-L_max table + 21-cell decision matrix + determinism / monotonicity tally + 4-branch adjudication protocol description + W4-44 self-test table + source-SHA pins + substrate framing + status + carry-forward).
  - Verdict line + companion comment row appended to `computations/s86_gate_verdicts.txt:221-222`.
- **Substrate-framing assessment** (per `.claude/rules/phononic-framing.md`): the registry preserves PHONONIC framing throughout. Each L_max row IS a different truncation of the SAME substrate eigenvalue computation. The substrate's w_0 prediction IS the spectral-action gradient at the fold; w_a IS its first scale-derivative. As L_max increases (8 → 10 → 12), the cutoff-axis tightens and more substrate eigenmodes contribute to the spectral moment. A scenario column monotone in L_max indicates the substrate's prediction at that scenario is REGULATOR-INVARIANT (a true substrate observable); an oscillating column would indicate REGULATOR-DEPENDENT prediction (a truncation artifact). Cell content is FRAMEWORK-RESPONSE (substrate scorecard outcome under DR3 occupation), not a measurement IN a curved-spacetime container. The 4-branch adjudication protocol IS the substrate's self-test under external observational input — a pre-registered classification of "regulator-class self-consistency" that DR3 will fire deterministically on. DR3 will not just measure w_0; it will measure the substrate's regulator-class self-consistency across the 7-scenario partition.
- **Solution-space interpretation**: pre-this-gate, the framework's DR3 response was 2-row (L=10 / L=12 only via W1b-1), already showing A1→B2 cell flip and structurally insufficient to discriminate REGULATOR-INVARIANT from REGULATOR-DEPENDENT outcomes. Post-this-gate, the 3-row matrix is REGISTERED with 14 cells populated, 7 stubs explicitly tagged PRE-REG-INCOMPLETE for L=8, the 4-branch adjudication protocol pre-registered with deterministic self-test, and a single S87-W0 carry-forward (`S87-DR3-SUB-TREE-3-ROW-PIN-PROMOTION`) to PROMOTE INFO → PASS in the next session via direct L=8 7-cell extraction. PASS-on-the-14-populated-cells means the regulator-first DR3 protocol is operative for the L=10 / L=12 axis; STUB on the 7 L=8 cells means the L=8 re-dispatch is the next-session carry-forward; the 4-branch decision tree is now pre-registered against DR3 publication (window opened 2026-04-23 per S84-W1b-9). When DR3 publishes (w_0^DR3, w_a^DR3), the protocol fires deterministically; current state routes all non-INSIDE_R_842 inputs to branch (4) EXTERNAL until L=8 closure — which is the pre-registered honest output, not a degradation.

---

### §W13-5. S86-ALPHA-S-CANONICAL-UPDATE (mack-cosmic-bridge)

**Status**: **CLOSED**
**Gate ID**: `S86-W13-P12-ALPHA-S-CANONICAL-UPDATE`
**Trigger**: `[VERIFY]` + `[SIGN]`
**Classification**: **PHONONIC** (α_s IS running of GGE-acoustic spectral tilt — second derivative of GGE quasiparticle dispersion at pivot scale; the framework prediction `α_s = n_s^2 - 1 = -0.068968` derives from S50-51 substrate-eigenvalue identity, not data fitting)
**Agent**: `mack-cosmic-bridge` (canonical-constants edit + 2 re-emissions; self-execution permitted because edit is mechanical and re-emission is gate-numerics-preserving — not adjudication of own work)
**Hypothesis**: Updating `canonical_constants.py` from `planck_alpha_s=-0.0045 ± 0.0067` (Planck 2018) to `alpha_s_canon_2020=+0.0023 ± 0.0063` (Aiola+ 2020 ACT DR4 + Planck) per S85 W1b-8 FAIL produces a self-consistent additive pin AND both re-emissions (S85 W1a-9 7D Fisher + S85 W1b-3 σ_corr/σ_diag) emit non-error verdict lines under the new pin; framework prediction (-0.068968) is UNCHANGED, only canon moves.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-5 (lines 700-911).

**MCP Pre-Compute Audit**:
- `list_constants(pattern="alpha_s")` → 7 matches; confirmed baseline `planck_alpha_s = -0.0045`, `planck_alpha_s_err = 0.0067`, `alpha_s_inflation_framework = -0.068968` (from `n_s_canon**2 - 1`).
- `search_knowledge("alpha_s ACT DR4 Aiola 2020")` → 10 hits; documents W1b-8 recommended pin update `alpha_s_canon_2020 = +0.0023 ± 0.0063` from Aiola+ 2020 Table 5 col 3.
- `trace_entity("S85-W1b-8")`, `trace_entity("S85-W1a-9")`, `trace_entity("S85-W1b-3")` → no traces (gates not yet entity-promoted in knowledge index; identified instead via direct file grep on `s85_gate_verdicts.txt`: baseline lines `S85-W1a-MULTID-FISHER-FRAMEWORK: PASS value=827.9255704800152` and `S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED: PASS value=1.1297479814965643`).
- No PRE-CLOSED closure covers this gate; the canonical-pin update + re-emission pattern is the registered W1b-8-remediation path per plan §W13-5.5.

**Verdict**: **PASS** (P12 + both re-emissions PASS).

Verdict lines on disk (`computations/s86_gate_verdicts.txt` lines 211-216 — see also lines 205-210 for the precision-floor first-attempt FAIL retained for audit transparency per S86 W1c-5 all-3-lines-retained discipline):

```
S86-W13-P12-ALPHA-S-CANONICAL-UPDATE: PASS -- value=0.0023 scheme=Aiola-2020-ACT-DR4-Planck convention=additive-edit L_max=N/A audit_sha256=d8b259b33eac2792a32f16b6818dcee03e6541786d374e62a63a81703c83d216 content_sha256=cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497 schema_version=S84+
S85-W1a-9-RE-EMIT-S86-W13-P12: PASS -- value=827.9255704800152 scheme=7D-Fisher convention=block-diagonal-correlation L_max=10 audit_sha256=41da50b65fea7b5a18d9ef1ed622a73a68eeb27876baeb0d051b4d76cdbbfa01 content_sha256=cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497 schema_version=S84+
S85-W1b-3-RE-EMIT-S86-W13-P12: PASS -- value=1.1297479814965643 scheme=Fisher-marg-Gauss convention=block-diag-C L_max=n/a audit_sha256=a670ab3e287c554787162bcc363b3388d3d5272b09458c760b2a830c227107dd content_sha256=cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497 schema_version=S84+
```

**Results**:

**(1) Canonical-constants pin update (additive; legacy retained)**

`computations/canonical_constants.py` modified additively at lines 1221-1240 (post-edit):

```python
# LEGACY (retained, marked superseded; back-compat preserved):
planck_alpha_s = -0.0045       # LEGACY Planck-2018 pin; superseded by alpha_s_canon_2020 per S86-W13 P12. Use alpha_s_canon_2020 for new computation scripts.
planck_alpha_s_err = 0.0067    # LEGACY Planck-2018 1-sigma on alpha_s.

# NEW (S86 W13 P12; Aiola+ 2020 ACT DR4 + Planck combined):
alpha_s_canon_2020 = +0.0023        # ACT DR4 + Planck combined (Aiola+ 2020); post-2018 canonical pin
alpha_s_canon_2020_err = 0.0063     # Aiola+ 2020 1-sigma on alpha_s
alpha_s_canon_2020_source = "Aiola+ 2020 (ACT DR4 + Planck combined)"
alpha_s_canon_2020_session = "S86 W13 P12"
```

Both `from canonical_constants import planck_alpha_s` (legacy) and `from canonical_constants import alpha_s_canon_2020` (new) succeed — back-compat preserved per plan §W13-5.6 ADDITIVE EDIT DISCIPLINE.

Framework prediction `alpha_s_inflation_framework = n_s_canon**2 - 1 = -0.068967990` (full float64) **UNCHANGED** — derives from substrate-eigenvalue identity (S50-51), not from data fitting.

**(2) 4-tuple (P12)**

```
(value=alpha_s_canon_2020=+0.0023, scheme=Aiola-2020-ACT-DR4-Planck, convention=additive-edit, L_max=N/A)
```

**(3) [SIGN] Substitution chain (Python-verified; matches plan §10 exactly)**

```
Step 1 — Definitions:
  α_s^old   = -0.0045    (planck_alpha_s, Planck 2018 central)
  σ^old     =  0.0067    (planck_alpha_s_err, Planck 2018 1-σ)
  α_s^new   = +0.0023    (alpha_s_canon_2020, Aiola 2020 ACT DR4 + Planck central)
  σ^new     =  0.0063    (alpha_s_canon_2020_err, Aiola 2020 1-σ)
  α_s^FW    = -0.068968  (alpha_s_inflation_framework, UNCHANGED across this gate)
  gap(X)    = α_s^X - α_s^FW           (signed; canon central minus framework)
  n_σ(X)    = |gap(X)| / σ^X           (1-D Gaussian-equivalent tension)

Step 2 — Substitute (Python-verified):
  Δ(central)  = α_s^new − α_s^old
              = (+0.0023) − (−0.0045)
              = +0.006800

  gap_old     = α_s^old − α_s^FW
              = (−0.0045) − (−0.068968)
              = +0.064468

  gap_new     = α_s^new − α_s^FW
              = (+0.0023) − (−0.068968)
              = +0.071268

  Δ(gap)      = gap_new − gap_old
              = (+0.071268) − (+0.064468)
              = +0.006800

Step 3 — Simplify:
  n_σ_old    = |gap_old| / σ^old
             = 0.064468 / 0.0067
             = 9.622 σ

  n_σ_new    = |gap_new| / σ^new
             = 0.071268 / 0.0063
             = 11.312 σ

  Δ(n_σ)     = n_σ_new − n_σ_old
             = 11.312 − 9.622
             = +1.690 σ

Step 4 — Direction (each predicate True under Python evaluation):
  Δ(central) > 0   → canon central MOVES toward POSITIVE
  α_s^FW < 0       → framework prediction is NEGATIVE
  Δ(gap) > 0       → gap WIDENS (signed canon − framework, positive direction)
  Δ(n_σ) > 0       → tension INCREASES from 9.622 σ to 11.312 σ (+1.690 σ worse)

Conclusion: Δ(central) = +0.0068 (canon shifts toward POSITIVE); framework
α_s^FW = −0.068968 is NEGATIVE and UNCHANGED; gap WIDENS by 0.0068
(signed canon − framework); n_σ INCREASES from 9.62 σ (Planck-2018) to
11.31 σ (Aiola-2020), Δ(n_σ) = +1.690 σ; tension HARDENS but framework
prediction is UNCHANGED — only the observational reference moved.
```

The script `s86_w13_p12_alpha_s_canonical_update.py` reproduces this chain at runtime (Step 6 `all_match = True`); deltas vs plan §10 expected values are below 1e-6 absolute (delta_central, gap_old, gap_new, delta_gap) and 1e-2 absolute (n_σ_old, n_σ_new, delta_n_σ — published at 3 sig figs in plan).

> **T8-2 install (S86 W2 WP-PATCH-2 Fairbairn+eBOSS parallel pin annotation, NEEDS-DECISION installed with `(NEEDS-ORCHESTRATOR-FOLLOWUP)` annotation per W2 V3 L622-661 + R2-A CONVERGENCE L753-762 + R3-FINAL What Changed L1609, applied 2026-04-27)**:
>
> The 11.31σ tension citation (Aiola-2020 ACT DR4 + Planck) recorded above SUPERSEDES the Planck-2018 9.62σ baseline. **Subsequent S86 W2 workshop closed at R3-FINAL** with a parallel Fairbairn-Heurtier-Olea-Romacho 2025 (arXiv:2511.01612) Table IV ACT+P+SPT+eBOSS canonical pin: `alpha_s_canon_Fairbairn = -0.00323 ± 0.00389` (per S86 W2 CANONICAL-1, READY-TO-INSTALL; canonical Fairbairn three-row dataset pin landed at `session-86-w12-workingpaper.md` §C36 via T8-4 install). Substitution-chain summary (per W2 R3-FINAL "What Changed" L1609; not re-derived here, only cited):
>
> ```text
> Under Fairbairn+eBOSS canonical pin:
>   α_s^new   = -0.00323
>   σ^new     =  0.00389
>   gap_new   = α_s^new − α_s^FW = -0.00323 − (-0.068968) = +0.065738
>   n_σ_new   = |gap_new| / σ^new = 0.065738 / 0.00389 ≈ 16.901 σ
>   Δ(n_σ)    = n_σ_Fairbairn − n_σ_Aiola = 16.901 − 11.312 = +5.589 σ
> Direction: tension HARDENS further from 11.31 σ (Aiola-2020) to 16.90 σ (Fairbairn+eBOSS), Δ(n_σ) ≈ +5.6 σ worse.
> Sign-lock: α_s^new is NEGATIVE-signed (matches framework prediction sign at central-value level); sign-lock-CONFIRMED.
> Trend across data inclusions (ACT+P → +SPT → +eBOSS): α_s central monotone-decreasing (-0.001 region depending on combination, but the canonical eBOSS-included row is decisively negative); confirms direction-toward-substrate-truth.
> ```
>
> Per W2 R3-FINAL "What Changed" L1609: the 11.31σ Aiola-only citation should be **augmented** (not replaced) by the Fairbairn+eBOSS 16.90σ tension as a **parallel pin** to preserve the audit trail of the canonical-source progression. The sign-lock-CONFIRMED + trend-monotone-decreasing direction-toward-substrate-truth is the substantive finding from the W2 closure. **Decision pending (NEEDS-ORCHESTRATOR-FOLLOWUP)**: whether the W13 working paper §W13-5 P12 verdict line should be re-emitted under the Fairbairn pin (creating a new S86-W13-P12-ALPHA-S-CANONICAL-UPDATE-FAIRBAIRN companion verdict), or whether the Fairbairn pin annotation here suffices without disturbing the Aiola-2020-based PASS verdict. The framework prediction `alpha_s_inflation_framework = -0.068968` remains UNCHANGED across all three observational pins (Planck 2018 → Aiola 2020 → Fairbairn 2025) — only the observational reference moves; the framework's substrate-side value is invariant per the S50-51 n_s²−1 identity.

**(4) W1a-9 re-emission (S85-W1a-9-RE-EMIT-S86-W13-P12: PASS)**

The S85 W1a-9 7D Fisher script (`s85_w1a_multid_fisher.py`) is **numerically invariant under the pin update** because:

(a) Framework prediction vector `p_FW = (w_0, w_a, n_T, r, β_s, α_s_running, f_NL)` is fixed via canonical sources (S58 `w0_FW = -0.918`, S74 `w_a = 0`, S66 `n_T = -3.024e-3`, S83 `r_CMB_framework = 0.011731`, S84 `β_s = -0.1331`, S63 `α_s_running = 0.00117`, S82 `f_NL = 0.0547`).

(b) LCDM reference vector is the inflation-consistency-relation null `(-1, 0, -r/8, 0, 0, 0, 0)` — the α_s LCDM slot is **0.0 by construction** (vanilla LCDM null), NOT the canonical observational central. The pin update (which moves the canonical observational central from -0.0045 to +0.0023) does **not** change the LCDM reference, so the Fisher pull `(α_s_running − 0)/σ_CMB-S4 = 0.00117/2.1e-3 = 0.557` is unchanged.

(c) Detector 1-σ projections (DESI DR3, LiteBIRD, CMB-S4, SKA-1) are pre-registered detector-noise budgets, independent of which canonical-pin convention is in force.

Re-computed value: `log10(BF_FW/LCDM) = +827.9256` (matches S85 baseline `827.9255704800152` to 1e-3 absolute = baseline-S85-match: True). χ²_total = 3812.69; subset-χ² (excl r, β_s) = 14.86 (S84 cross-check expected 13.9 within 20% tolerance: PASS).

**Auxiliary diagnostic** (under the new pin, for the alpha_s-slot-only canon-vs-framework pull using observational σ):
- old (Planck-2018): pull = (-0.0045 − (−0.068968))/0.0067 = +9.622
- new (Aiola-2020):  pull = (+0.0023 − (−0.068968))/0.0063 = +11.312
- widening: +1.690 σ (matches §10 substitution chain Δ(n_σ)).

This diagnostic is informational only; the gate's PASS verdict turns on the 7D joint log10(BF) ≥ 2 threshold (+827.9 ≫ 2: PASS).

**(5) W1b-3 re-emission (S85-W1b-3-RE-EMIT-S86-W13-P12: PASS)**

The S85 W1b-3 widening-ratio script (`s85_w1b_alpha_s_joint_fisher_correlated.py`) is **numerically invariant under the pin update** because:

(a) Detector σ(α_s) values (σ_S4 = 2.1e-3, σ_HD = 1.5e-3, σ_LB = 1.05e-2, σ_DR3 = 1.0e-2, σ_LISA = 1.0e-1) are forecast projections per individual-detector noise budgets, NOT the canonical observational σ.

(b) The 5×5 correlation matrix C with off-diagonals (ρ_S4-HD = 0.30, ρ_S4-LB = 0.15) is plan-pre-registered (S85 W1b-2 §W1b-2.2) and does not depend on the canonical-pin convention.

(c) The Cauchy-Schwarz widening ratio `σ_corr/σ_diag` depends only on (a) detector σ-vector and (b) C; neither moves under the pin update.

Re-computed value: `ratio = σ_corr/σ_diag = 1.1297479814965643` (matches S85 baseline to 1e-6: `baseline-S85-match: True`). σ_corr = 1.3597e-3, σ_diag = 1.2035e-3, det(C) = 0.8875, identity-sanity ratio (C = I) = 1.000000000000 (within 1e-12). PASS_RATIO = 1.25; ratio 1.1297 ≤ 1.25 → PASS.

**(6) Tension-widening INFO sub-tag**

The pin update WIDENS the framework-vs-canonical-observation tension on α_s:

| Era | Canon central | Canon σ | Framework α_s | n_σ |
|:---|:---|:---|:---|:---|
| Planck-2018 (legacy) | −0.0045 | 0.0067 | −0.068968 | **9.622 σ** |
| Aiola-2020 (canonical) | +0.0023 | 0.0063 | −0.068968 | **11.312 σ** |
| Δ(n_σ) | — | — | UNCHANGED | **+1.690 σ** |

The framework's α_s prediction (−0.068968) is FROZEN by the S50-51 substrate-eigenvalue identity. The pin update is OBSERVATIONAL discipline (which external reference is canonical for tension calculations), not a framework adjustment. Reported as INFO sub-tag in the verdict: tension HARDENS but framework prediction is UNCHANGED — only the observational reference moved.

**Solution-space implication**: the framework's α_s prediction is increasingly discriminable from current data; CMB-S4 / CMB-HD / SKA-1 forecast σ values (which depend on the canonical center for noise modeling) shift accordingly. The 11.31 σ tension under Aiola-2020 puts α_s as the framework's currently-largest single-observable tension (was 9.62 σ under Planck-2018). Whether this is a real prediction failure OR indicates the framework's α_s derivation needs revisiting is a DOWNSTREAM question, not a P12 verdict.

**(7) Dual-SHA**

| Verdict line | audit_sha256 | content_sha256 |
|:---|:---|:---|
| `S86-W13-P12-ALPHA-S-CANONICAL-UPDATE` | `d8b259b33eac2792a32f16b6818dcee03e6541786d374e62a63a81703c83d216` | `cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497` |
| `S85-W1a-9-RE-EMIT-S86-W13-P12` | `41da50b65fea7b5a18d9ef1ed622a73a68eeb27876baeb0d051b4d76cdbbfa01` | `cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497` |
| `S85-W1b-3-RE-EMIT-S86-W13-P12` | `a670ab3e287c554787162bcc363b3388d3d5272b09458c760b2a830c227107dd` | `cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497` |

Companion comment rows present for all 3 verdicts (gate-verdicts.md S81+ canonical form). Audit SHAs are unique across the 3 lines (no SHA-hardcoding); content SHA shared because the producing script is the same (this is structurally correct — content_sha pins the script bytes).

**Audit-trail note**: lines 205-210 of `s86_gate_verdicts.txt` retain the first-attempt FAIL verdict (precision-floor bug in `canon_check_ok` aggregator: original tolerance `1e-12` against `alpha_s_inflation_framework + 0.068968` mismatched the 6-sig-fig publication precision of `-0.068968` vs the full-float64 `-0.06896799`). Per S86 W1c-5 all-3-lines-retained discipline, both runs persist. The fix loosened the aggregator's tolerance to `1e-5` (one OOM looser than the 6-sig-fig publication precision, per `.claude/rules/epistemic-discipline.md` Publication-Precision Pre-Registration rule, W1c-8 precedent). The gate's actual physics (legacy retained, new added, diagnostic chain match) was always correct; only my pre-flight aggregator had a publication-precision-floor bug. PROHIBITED_ACTIONS Class-1/6 (convention-shopping / iterate-until-PASS) does NOT apply: the threshold for PASS was never modified and the script's underlying numerics were unchanged.

**(8) Substrate-framing assessment** (per `.claude/rules/phononic-framing.md` + plan §13)

α_s IS the substrate's GGE-acoustic spectral tilt's running — the second derivative of the GGE quasiparticle dispersion at the pivot scale. The framework prediction (−0.068968) is FROZEN; it derives from the substrate's S50-51 spectral identity `α_s = n_s² − 1` with `n_s_canon = 0.9649`, NOT from data fitting or convention choice.

The pin update is OBSERVATIONAL discipline (selecting the post-2018 ACT DR4 + Planck combined reference over the legacy Planck-2018-only reference for tension calculations), NOT a framework adjustment. The widening 9.62 σ → 11.31 σ tension is the substrate's PREDICTION facing a hardening external constraint; future detector data (CMB-S4 by 2028, CMB-HD by 2030, SKA-1 Phase-1 by 2028, SKA-2 by 2030+) will resolve whether the substrate-derived value is correct.

This is NOT framed as "the framework is in 11 σ tension and therefore wrong." It IS framed as "the substrate's α_s prediction is increasingly discriminable; future detector data will resolve whether the substrate-derived value is correct." The substrate prediction is FALSIFIABLE — that is its scientific value, not a defect.

**Artifacts on disk**:
- `computations/canonical_constants.py` (modified; additive entries at lines 1221-1240; back-compat preserved)
- `computations/s86_w13_p12_alpha_s_canonical_update.py` (producing script, 39 879 bytes)
- `computations/s86_w13_p12_alpha_s_canonical_update.json` (P12 audit log, 3 463 bytes)
- `computations/s86_w13_p12_re_emit_w1a_9.json` (W1a-9 re-emit detail, 2 228 bytes)
- `computations/s86_w13_p12_re_emit_w1b_3.json` (W1b-3 re-emit detail, 1 492 bytes)
- `computations/s86_gate_verdicts.txt` (verdict lines 205-216: 3 verdicts × 2 runs × 2 rows each = 12 lines including dual-SHA companion rows; first-run FAIL retained for audit transparency, second-run PASS canonical)

---

### §W13-6. S86-FROZEN-COMMIT-LANDING (mack-cosmic-bridge)

**Status**: CLOSED
**Gate ID**: `S86-FROZEN-COMMIT-LANDING`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (every frozen prediction in commit IS substrate-channel observable; 4-level unit-class taxonomy partitions substrate predictions by normalization convention; Both-Pathways r is substrate-prediction dual-registration discipline)
**Agent**: `mack-cosmic-bridge` (registry-write extending mack S-7 §V.2 + W-2 workshop; not adjudication)
**Hypothesis**: Landing FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 4-level unit-class taxonomy + Both-Pathways r registration in `sessions/framework/registry/baseline-findings-s66.md` (or successor) produces a single authoritative source for the framework's frozen-prediction discipline that downstream sessions can cite verbatim, with per-level edit-discipline preventing convention-shopping at the framework level.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-6.

**MCP Pre-Compute Audit**:

| MCP query | Salient return |
|:----------|:---------------|
| `search_knowledge("FROZEN PREDICTION DISCIPLINE COMMIT 2026")` | 20 hits — first appearance is `s73b_desi_dr3_predictions.py` (frozen 2026-04-10 with w_0=-0.918 +/- 0.06, w_a=0); pre-registration with `frozen_date` already established at S73b. Master invocation across S82+S84+S85 verdicts; no full-form COMMIT 2026-2030 closure existed prior to this gate. |
| `search_knowledge("4-level unit-class taxonomy")` | 20 hits — `s85_w12_w0_regulator_taxonomy.py` is the 5-regulator-axis taxonomy (different axis); `s85-5a-pin-drift-taxonomy.md` is the 4-mode pin-drift taxonomy (parallel structure but not identical); the W-2 4-level (sub-derivation-layer) taxonomy is unique to S86 W-2 closure 2026-04-25. |
| `search_knowledge("Both-Pathways r registration")` | 20 hits — `s84_w1b_theorem_registration.py` + `s82_w2_7_w3g_beta_R3.py` are pre-registration scaffolds; no Both-Pathways (Path-H + Path-C dual-r) registration existed prior. The W-2 workshop is the source of record for the dual-pathway split. |
| `trace_entity("baseline-findings-s66")` | 21 entries (10 theorems + 10 gates + 1 equation). Confirms the file is the authoritative framework registry (Section 1A-D, Section 5 observational scorecard). PRE-CLOSED: NO. The frozen-commit, taxonomy, and r-Both-Pathways sections were not present prior to this gate. |
| `get_constant("planck_ns")` | 0.9649 (Planck 2018 TT,TE,EE+lowE+lensing); echoed verbatim into Element 1 frozen-pin table. |
| `get_constant("w0_FW")` | -0.918 (S58 Volovik vacuum + effacement); echoed verbatim into Element 1. |
| `get_constant("r_CMB_framework")` | 0.011731522176014426 (S83 G46 TENSOR-TRANSFER PASS; canonical Path-C); echoed verbatim into Elements 1 + 3. |
| `get_constant("alpha_s_inflation_framework")` | -0.068968 (S50 identity n_s^2-1 with `n_s_canon = planck_ns`); echoed verbatim into Element 1. |
| `get_constant("eps_baseline")` | 0.01755 ((1-planck_ns)/2; CMB pivot); used to anchor Element 1 A_s epsilon-range echo. |

**Verdict**: **PASS** — `value=3 scheme=baseline-findings-edit convention=mack-S-7-V.2-W-2-workshop L_max=N/A sha256=e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c`
Companion row: `audit_sha256_short=e774fc99cb1ea3d2 content_sha256=f6a9e5aaeb45c1dae7033ab36d4dee8c3929195bcf67c6beac6f52992eb36c18 audit_sha256=e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c`
Verdict file: `computations/s86_gate_verdicts.txt` line 217 (canonical) + line 218 (companion).

**Results**:

*4-tuple*: `(value=3, scheme=baseline-findings-edit, convention=mack-S-7-V.2-W-2-workshop, L_max=N/A)`. The `value=3` is the count of commit elements landed (FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 4-Level Unit-Class Taxonomy + r Both-Pathways Registration).

*3-element landing count* (target 3, achieved 3/3, all sections present and parseable in `sessions/framework/registry/baseline-findings-s66.md` after the write):

| # | Element | Section header on disk | Mode | Lines | Body bytes |
|:--|:--------|:-----------------------|:-----|:-----:|:-----:|
| 1 | FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 | `## FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030` | APPENDED | 35 | 3,553 |
| 2 | 4-Level Unit-Class Taxonomy (S86 W-2 workshop landing) | `## 4-Level Unit-Class Taxonomy (S86 W-2 workshop landing)` | APPENDED | 22 | 3,791 |
| 3 | r Both-Pathways Registration (S86 W-2 workshop landing) | `## r Both-Pathways Registration (S86 W-2 workshop landing)` | APPENDED | 32 | 4,256 |

All three were APPENDED (no prior section with the matching header existed in the baseline file at dispatch time). The atomic shadow-rename writer wrote new file content via `os.replace(tmp, p)` to minimize race surface against parallel registry writers (P8/P9/P10/P11/P12).

*CC1 — Reversibility-trigger registration for w_0 / r / alpha_s* (Element 1):

- **w_0**: trigger event = DR3 publication, R_842 rectangle lockout per S84-W1b-9 (`content_sha256=9cc7f47e...79d9f`). Window opens 2026-04-23. Single-detector trigger.
- **r**: TWO-step trigger chain — BK-Array publication 2026 (`content_sha256=e2ca24d6...882d3`, S84-W4-42 4-branch tree) AND LiteBIRD publication 2030 (per §W13-7 P2 SEQUENCED detector chain). BOTH legs of Both-Pathways carry parallel reversibility under the SAME chain. Single-detector publication does NOT trigger r re-pin; it triggers a BRANCH-ASSIGNMENT update on the 4-branch decision tree.
- **alpha_s**: trigger event = CMB-S4 publication (2028+), per S86 C36 quarterly poll for explicit sigma(alpha_s) availability. Pin updatable on canon drift via `update_constant("alpha_s_inflation_framework", ...)`. The S50 identity alpha_s = n_s^2-1 is structural; only the reference observational canon `n_s_canon` (=planck_ns) can move.

3 reversibility triggers, 3 frozen pins under triggered re-pin. The framework's commitment is asymmetric: 7 frozen-prediction families covered (n_s, r-Path-H, r-Path-C, w_0, alpha_s, f_NL_folded 3-pathway tuple, A_s epsilon-range), only 3 have pre-registered reversibility triggers in the 2026-2030 window. The other 4 (n_s, f_NL_folded, A_s) are reversibility-frozen against the entire window — any update requires the PRDR re-file route (the structurally-incomplete-pre-registration exception).

*CC2 — 4-level per-level edit-discipline statements* (Element 2; verbatim on disk):

| Level | Edit-discipline (2026-2030) |
|:-----|:----------------------------|
| Level 1 — Fold structural-floor | NEVER edit during 2026-2030. A change at Level 1 invalidates the entire downstream cascade — every Level 2/3/4 prediction inherits from this layer. |
| Level 2 — Pre-fold convention-pin | Edit ONLY via PRDR sub-diff at plan-freeze (NOT post-hoc). A Level 2 edit requires a `pre-registration-update:` log entry on the producing gate; iteration-until-PASS is forbidden. |
| Level 3 — Observational boundary | Edit ONLY via documented detector-data update (Fisher PDF SHA-pinned per S86 C32 / W4-3 / W4-6). Updates land as additive Fisher-pin entries, never as silent overwrites. |
| Level 4 — Observational prediction | Edit ONLY via reversibility trigger (per FROZEN-PREDICTION-DISCIPLINE-COMMIT) AND re-derivation through Levels 1-3. Level 4 cannot be edited in isolation. |

Each level's edit-discipline is a statement of what would constitute a PERMITTED edit during 2026-2030 — not a confidence claim about the layer. The taxonomy is editability-graded, not certainty-graded. Level 1 is most-restricted; Level 3 is most-mechanical (clean detector-data updates land additively). Level 4 is the only layer whose edits depend on data outside the framework's own internals.

*Baseline-findings pre/post diff per element*:

- **Pre-write file SHA**: `9686e01527d7c961a49d042f886f78f3727f83c234a258b04c8013546bd44a65` (31,657 bytes; baseline-findings-s66.md at S86 W13-A dispatch).
- **Post-write file SHA**: `f6a9e5aaeb45c1dae7033ab36d4dee8c3929195bcf67c6beac6f52992eb36c18` (43,061 bytes; +11,404 bytes = 3 sections at 3,553 + 3,791 + 4,256 + section spacing).
- Per-element text-cumulative pre/post SHAs are recorded in `computations/s86_w13_p1_frozen_commit_landing.json` `diff_log[].pre_sha256/post_sha256`. Each element's `mode=APPENDED` reflects no prior collision; the find-section-bounds parser confirms zero header-line matches before the write for all 3 element headers.

*Dual-SHA closure*:
- `audit_sha256` = `e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c` (closure hash over input_pin_map ∪ machinery_pin_map ∪ baseline_sha_post ∪ elements_landed; full 64-char hexdigest).
- `content_sha256` = `f6a9e5aaeb45c1dae7033ab36d4dee8c3929195bcf67c6beac6f52992eb36c18` (full SHA-256 of `sessions/framework/registry/baseline-findings-s66.md` post-write).
Both 64-char hexdigests, distinct, written as canonical-line + companion-row in `computations/s86_gate_verdicts.txt:217-218`.

*Artifacts produced*:
- `computations/s86_w13_p1_frozen_commit_landing.py` (~29.9 kB) — producing script. Imports from `canonical_constants` (planck_ns, w0_FW, r_CMB_framework, alpha_s_inflation_framework, eps_baseline). CPU-only with `OMP_NUM_THREADS=8` cap. Atomic shadow-rename writer for the registry edit (per `.claude/rules/epistemic-discipline.md` §Registry-Write Hygiene). All numeric literals tagged `# (local)` or imported.
- `computations/s86_w13_p1_frozen_commit_landing.json` (~5.5 kB) — 3-element diff log with per-element pre/post SHAs, presence-check, frozen-pin echo table, split-arithmetic, and 4-tuple. Read by the post-dispatch verifier.
- `sessions/framework/registry/baseline-findings-s66.md` — modified additive (3 new top-level sections appended; no prior content edited or removed; file size 31,657 -> 43,061 bytes).
- `computations/s86_gate_verdicts.txt` — verdict line + dual-SHA companion row at lines 217-218.

*Substrate-framing audit* (per `.claude/rules/phononic-framing.md` §13 reminder):
- Element 1 frames the FROZEN-PREDICTION-DISCIPLINE as the **substrate's commitment to its own predictions for the duration of the active detector window** — substrate self-restraint against post-hoc data-fitting, NOT a confidence claim. Verified in §"What this discipline IS" closing paragraph on disk.
- Element 2 frames the 4-level taxonomy as **substrate self-knowledge** — a partition of substrate-prediction OBJECTS by sub-derivation layer, with each level carrying its own edit-discipline because each sub-layer has different epistemic obligations. Verified in §"What this taxonomy IS" closing paragraph on disk.
- Element 3 frames Both-Pathways r as **substrate self-test** — one tensor-to-scalar ratio emitted through TWO of the substrate's own internal projection channels (transverse fiber-osc B2 vs longitudinal acoustic compaction B1 through the G46 transfer); explicitly NOT "the framework predicts two numbers". Verified in §"What Both-Pathways IS" closing paragraph on disk.
- The `project_substrate-not-c-limited.md` carry-forward (mack memory) is honored: each frozen pin is a substrate-channel observable, not a c-limited propagation; the discipline locks substrate predictions, not propagated CMB realizations.

*What PASS/FAIL means for solution space* (per plan §W13-6 item 11):
- **PASS** (this verdict): the framework's frozen-prediction discipline is now codified in the baseline-findings file. Downstream sessions citing "the frozen pins" point to a single authoritative source. The 4-level taxonomy provides per-level edit-discipline that prevents convention-shopping at the framework level (S78 Class 1 execution failure). Both-Pathways r is the substrate's TWO-channel prediction for the tensor-to-scalar ratio; downstream gates citing r must select Path-H or Path-C explicitly (or carry both rows side-by-side under Both-Pathways framing).
- **FAIL counterfactual** (would-have-meant): the framework would continue without a codified frozen-prediction discipline; risk of unauthorized re-pinning during the 2026-2030 detector window. This counterfactual is closed by the present PASS.

---

### §W13-7. S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING (volovik-superfluid-universe-theorist)

**Status**: CLOSED
**Gate ID**: `S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (r IS GGE relic tensor power / scalar acoustic power partition — substrate eigenvalue partition between transverse fiber modes B2 and longitudinal acoustic modes B1 at the fold)
**Agent**: `volovik-superfluid-universe-theorist` (parent-framework owner of dual-pathway derivation; mack-cosmic-bridge as second-choice runtime fallback — runtime owner = volovik per spawn-prompt assignment)
**Hypothesis**: Promoting r to dual-function entry in `falsifier-master-inventory.md` (Path-H r=0.00745 + Path-C r=0.0117 with 36.3% Path-C-relative split exceeding 12.5% scheme-floor flag, plus SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030) extends C29 single-row promotion (W1c) into fully-specified dual-pathway falsifier without conflict — additive extension only.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-7.

**MCP Pre-Compute Audit**:

| MCP query | Salient return |
|:----------|:---------------|
| `search_knowledge("r Path-H Path-C tensor-to-scalar dual pathway")` | 8 equation hits + 2 theorem hits; confirms `r_Path_H = 0.00745` and `r_Path_C = 0.0117` are pinned in plan §W13-7; cross-references S86 W12 boundary table (`b1_b2 = 0.005`, `b2_b3 = 0.015`, `b3_b4 = 0.030`); the legacy atlas-07 row `r = 3.86e-10` (`Unobservable`) is the pre-S60 prediction now superseded by the dual-pathway W1c-8 promotion. Not closed; gate is a registry-extension of C29. |
| `search_knowledge("BK-Array 2026 LiteBIRD 2030 detector sequence")` | 7 equation hits + 1 closed-mechanism hit (`LITEBIRD-NT-DISCRIMINATION-2030-2040`) + 1 gate hit (`S84-BICEP-KECK-2026-PRE-REGISTER` PASS at L_max=N/A). Confirms the LiteBIRD STRUCTURAL-FLOOR registry is landed (S85 W1a) and the BK-Array 4-branch tree is pre-registered (S84 W4-42 PASS, content_sha=`e2ca24d6...`). |
| `trace_entity("S86-FALSIFIER-MASTER-INVENTORY-PROMOTION")` | No trace (knowledge index lags S86 W1c-8 closure). Verified directly via `grep` on `computations/s86_gate_verdicts.txt:55` — PASS verdict present (audit `32c60c2f69fe6150...`, content `144a9999104f3662...`). C29 prerequisite SATISFIED. |
| `trace_entity("S84-W4-42-BICEP-KECK-2026-PRE-REGISTER")` | No trace (knowledge index lags). Verified via `grep` on `computations/s84_gate_verdicts.txt:45` — PASS verdict present (content `e2ca24d63cdbdcca...`, audit `b1eb9e61ece7b046...`). 4-branch tree consistency SATISFIED (CC2 PASS). |
| `trace_entity("S84-W4-41-OBSERVATIONAL-BOUNDARY-LITEB-NT")` | No direct trace; the S85 W1a re-registration `S85-W1a-LITEBIRD-NT-REGISTRY-LANDING` PASS at line 24 of `s85_gate_verdicts.txt` (value=`588.78`, scheme=`transfer-function-54-decade`, convention=`STRUCTURAL-FLOOR`, content `0c1ab0e9ab063c59...`, audit `f5a285d8548129b0...`) is the canonical successor. STRUCTURAL-FLOOR confirmed (CC3 PASS). |
| `query_entity("gates", "S85-W1a-4")` | No gate found by that ID; the Path-H r=0.011732 source is the S85 W1a workshop §W2 OQ-7 (`s85-w2-as-band-authority.md` line 1882) carry-forward — already cited in `falsifier-master-inventory.md` Provenance line 101. The W1c-8 promotion mapped 0.011732 → 0.00745 per OQ-7 derivation (Path-H is the H_tilde-rescaling closure, not Mellin-tilt). |
| `get_constant("M_KK")` (canonical-constants source) | `M_KK = 7.428660e+16 GeV` (consistent with master-inventory line 137 substrate-framing block; Mass-scale used for Path-H/Path-C derivation kinematics but not directly in r value). |

**Verdict**: **PASS** (`value=DUAL_PATHWAY scheme=2-pathway-2-detector convention=mack-S-7-V.1 L_max=10 audit_sha256=e747495c1fbf8af144c3701ecaf5e77b2497d3b876281bdffb703d8db22839f3 content_sha256=41f96976d86eec38583618d70acf2da302f47d79e8531b858f64125ca8730cce schema_version=S84+`); appended to `computations/s86_gate_verdicts.txt` with dual-SHA companion row per W9a-99 split.

**Results**:

**4-tuple**: `(value=DUAL_PATHWAY, scheme=2-pathway-2-detector, convention=mack-S-7-V.1, L_max=10)`

**CC1 — W1c C29 PASS prerequisite check** (per plan §W13-7.6 PRECONDITION + §W13-7.9 INFO clause): `S86-FALSIFIER-MASTER-INVENTORY-PROMOTION` PASS verdict present at `computations/s86_gate_verdicts.txt:55` (audit `32c60c2f69fe6150a1d8e89a81961046cfb68091373cc0b8721106d35ebdd5f6`, content `144a9999104f3662fc5a5920e3779cb533cb7581e9014007010d89a028273aef`). C29 PRE-REG-INCOMPLETE INFO clause NOT triggered; gate proceeds with full registry extension.

**CC2 — BK-Array 4-branch tree mapping consistency with S84 W4-42**: `S84-BICEP-KECK-2026-PRE-REGISTER` PASS at `computations/s84_gate_verdicts.txt:45` (content_sha256=`e2ca24d63cdbdcca3c42b0c1841681134e9128f9d939b0af6f4e8f4e200882d3` matches the spawn-prompt-pinned anchor `e2ca24d6...`). The 4-branch boundary table written into the master inventory uses the boundaries (b1_b2=0.005, b2_b3=0.015, b3_b4=0.030) pinned in `s84_w4_bicep_keck_2026_pre_register.py` and reproduced in `s86_w13_w0_4_bk_array_classifier_pre_build` (s86 verdict line 175). CC2 PASS.

**CC3 — LiteBIRD STRUCTURAL-FLOOR consistency with S84 W4-41 / S85 W1a**: `S85-W1a-LITEBIRD-NT-REGISTRY-LANDING` PASS at `computations/s85_gate_verdicts.txt:24` (content `0c1ab0e9ab063c59e8d8d3c10ddc6aeab667cb414200a0f92d2a7dbcf1b203ba`, audit `f5a285d8548129b053b0c34d54043f7fd00487ee4549d43cf367fff015f6c8b7`, convention `STRUCTURAL-FLOOR`). LiteBIRD 2030 sigma(r) ≈ 0.001 fiducial (6-yr nominal mission) is the pre-registered Stage-2 discriminator. CC3 PASS.

**Three split-fraction interpretations** (documentation discipline per plan §W13-7.6 EDIT SPEC — record ALL THREE; designate one as "registered"):

```
Definitions: r_H = 0.00745  (Path-H, transverse fiber-oscillation, mack S-7 V.1)
             r_C = 0.0117   (Path-C, substrate-compaction, Volovik-9A / W10-2)
             |Δr| = |r_C − r_H| = 0.00425

(1) Raw fractional difference (Path-H-relative):
        |r_H − r_C| / r_H = 0.00425 / 0.00745 = 0.570470 → 57.0%

(2) Symmetric split (two-pathway natural form):
        2·(r_C − r_H) / (r_H + r_C) = 0.00850 / 0.01915 = 0.443864 → 44.4%

(3) Path-C-relative split (REGISTERED — matches mack S-7 §V.1 "36.5%"):
        |r_C − r_H| / r_C = 0.00425 / 0.0117 = 0.363248 → 36.3%

REGISTERED SPLIT = 36.3% (Path-C-relative).
```

**Scheme-floor flag — DUAL_PATHWAY classification (deterministic boolean per [VERIFY] trigger)**:

```
Threshold: scheme_floor = 0.125  (12.5%, per S86 W3-7 C27 PASS-clause re-pin in W0c)
Comparison: 0.363248 > 0.125  →  TRUE  →  DUAL_PATHWAY = TRUE
Registered tags: DUAL_PATHWAY=true, SCHEME_FLOOR_EXCEEDED=true
```

The 36.3% Path-C-relative split EXCEEDS the 12.5% scheme-floor by 2.91× — the dual prediction is REAL substrate physics, NOT regulator artifact. (Plan §W13-7.10 footnote: this is a deterministic boolean, not a sign/direction claim, so the substitution-chain rule does not apply.)

**n_T = −r/8 consistency relation (S84 W4-39 exact)** — single-field-inflation tensor tilt identity, inherited by both pathways from the underlying B2-mode kinematics:

| Pathway | r       | n_T = −r/8 |
|:--------|:--------|:-----------|
| Path-H  | 0.00745 | **−0.000931** |
| Path-C  | 0.0117  | **−0.001463** |
| Δn_T    | —       | **−0.000532** |

LiteBIRD 2030 sigma(n_T) at sigma(r) ≈ 0.001 → sigma(n_T) ≈ 0.000125 → Δn_T = 4.25σ separable; Path-H vs Path-C distinguishable at >4σ in the LiteBIRD nominal-mission Stage-2 readout.

> **T8-3 install (S86 W2 WP-PATCH-3 Path-H/Path-C n_T residual annotation, NEEDS-DECISION installed with `(NEEDS-ORCHESTRATOR-FOLLOWUP)` annotation per W2 V2 L591-595 + R3-FINAL Verdict row 6 L1574, applied 2026-04-27)**:
>
> The displayed values `n_T(Path-H) = −0.000931` and `n_T(Path-C) = −0.001463` are the **rounded 4-sig-fig presentations** of the single-field-consistency identity `n_T = −r/8`. The **bit-exact rationals** computed from the displayed r values are:
>
> - `−r_H/8 = −0.00745/8 = −0.00093125` exactly (residual against displayed `−0.000931` is +2.5 × 10⁻⁷ rounding artifact at the 4-sig-fig publication precision)
> - `−r_C/8 = −0.0117/8  = −0.0014625`  exactly (residual against displayed `−0.001463` is −5.0 × 10⁻⁷ rounding artifact at the 4-sig-fig publication precision)
>
> Both rounding residuals are O(10⁻⁷), well below any detector-relevant precision floor (LiteBIRD's σ(n_T) ≈ 1.25 × 10⁻⁴ is ~2.5 OOM larger than the rounding residual). The 4-sig-fig n_T displays are consistent with `n_T = −r/8` to bit-exact rational precision at the 4-sig-fig publication-precision floor — **the n_T = −r/8 single-field consistency identity is satisfied at 4-sig-fig rounding**, no genuine deviation. Per `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration (S86 W1c-8 follow-up surface)": for downstream verifiers comparing against these published n_T values, use rel_tol ≥ 1e-3 (4-sig-fig presentation precision) — tighter tolerances will surface the rounding residual as a precision-comparison artifact.
>
> **Cross-link to LiteBIRD 5-outcome typology** (per S86 W2 R3-B EMERGENCE (iv) L1547-1563 + Verdict row 11 L1579 + CORRESPONDENCE-2): the W2 workshop established that LiteBIRD measurement of (r, n_T) discriminates between three regulator-class outcomes — Outcome 1 (Path-H r ≈ 0.00745, L1 zeta closure), Outcome 2 (Path-C r ≈ 0.0117, L3 per-Q span closure), Outcome 3 (intermediate-r, L2 Zubarev or third regulator) — extended to a 5-outcome typology when paired with the Path-H/Path-C 4σ-separation criterion at LiteBIRD nominal-mission. The 5-outcome typology cross-references this row's Path-H/Path-C n_T pair via the n_T = −r/8 single-field invariant (which holds in all three regulator classes — the regulator class fixes r, and n_T inherits the −r/8 relation). **Decision pending (NEEDS-ORCHESTRATOR-FOLLOWUP)**: whether the 5-outcome typology cross-link should be promoted to a sub-row of the master falsifier inventory Row #2 (overlap with T7-39 LiteBIRD entry refinement and T8-9 rank-2 product detector matrix item — both currently SKIP per parent's relocation directive on `falsifier-master-inventory.md`).

**SEQUENCED detector chain** (Stage 1 → Stage 2):

- **Stage 1 (2026)** — **BK-Array (BICEP/Keck Array)**: 4-branch decision tree per S84 W4-42 (`content_sha256=e2ca24d6...882d3`):

  | Branch | r window         | Path-H verdict | Path-C verdict | Substrate r-channel |
  |:-------|:-----------------|:---------------|:---------------|:--------------------|
  | 1      | [0.000, 0.005]   | FAIL           | FAIL           | NULL — both excluded |
  | 2      | [0.005, 0.010]   | PASS-WITHIN    | TENSION        | Path-H favored |
  | 3      | [0.010, 0.015]   | TENSION        | PASS-WITHIN    | Path-C favored |
  | 4      | [0.015, 0.040]   | FAIL           | FAIL           | substrate r-channel WRONG |

- **Stage 2 (2030)** — **LiteBIRD** (Hazumi+ 2022; STRUCTURAL-FLOOR per S84 W4-41 / S85 W1a `0c1ab0e9...b203ba`): sigma(r) ≈ 0.001 fiducial under 6-yr nominal mission; first-data target 2030. Stage-2 discriminates Path-H vs Path-C at sub-1% precision via the n_T = −r/8 consistency relation.

  | LiteBIRD discrimination band       | Verdict on Path-C |
  |:------------------------------------|:-------------------|
  | \|r_obs − 0.0117\| < 1σ              | Path-C CONFIRMED at LiteBIRD precision |
  | 1σ ≤ \|r_obs − 0.0117\| < 3σ          | Path-C TENSION |
  | \|r_obs − 0.0117\| ≥ 3σ              | Path-C EXCLUDED |

**Sequencing rule**: If Stage-1 lands in Branch 1 OR Branch 4, substrate r-channel FAILS; both pathways excluded; Stage-2 dispatch is moot. If Stage-1 lands in Branch 2 OR Branch 3, ONE pathway passes initial test; advance to Stage 2 LiteBIRD discriminator.

**Field-presence verification (ABSOLUTE, per plan §W13-7.9 PASS criterion)**: 20/20 checks pass (post-edit master inventory at `889fe029...` → `d64650fb...`, +6003 bytes; all of: Row #2 r extension section, Path-H value, Path-C value, three split-fraction interpretations (57.0% / 44.4% / 36.3%), registered-split designation, scheme-floor flag, BK-Array 2026 4-branch table + content_sha pin, LiteBIRD 2030 STRUCTURAL-FLOOR + content_sha pin, n_T(Path-H)=−0.000931, n_T(Path-C)=−0.001463, S84 W4-39 citation, sequencing rule, PHONONIC substrate framing block, AND C29 + P11 PAIR-6 cross-ref preservation).

**Substrate framing assessment (PHONONIC, volovik-specific perspective)**: Path-H and Path-C are not two competing inflaton scenarios; they are two distinct substrate-closure pathways for the A_s-Planck divergence (S85 W2 §lines 903-920). Path-H closes via H_tilde rescaling (transverse fiber-oscillation - direct B2-mode tensor-mode generation at the fold, no c_sub variation; Hawking-type mechanism). Path-C closes via c_sub upper-spread expansion via fiber-tau density compaction (3He-B-inheritance per `.claude/agent-memory/mack-cosmic-bridge/project_3heb-inheritance.md`; Volovik droplet → universe inheritance, Mellin-weight kinematics from S78 W2-E). Both project from the SAME substrate observable (eigenvalue partition between B2 transverse fiber modes and B1 longitudinal acoustic modes evaluated at the pivot scale); the dual-pathway registration IS the substrate's TWO sub-channel projections of its tensor-mode generation mechanism, NOT a model-selection question. The substrate predicts BOTH; observation will rule out at most one OR rule out the substrate r-channel entirely. (Substrate-first: r is logically prior; the BK-Array and LiteBIRD detectors are external acoustic perturbations that probe the substrate's pre-existing eigenvalue partition — they do not "create" r in some embedding spacetime container.)

**Dual-SHA closure** (per `.claude/rules/gate-verdicts.md` S81+ canonical form):
- `audit_sha256` = `e747495c1fbf8af144c3701ecaf5e77b2497d3b876281bdffb703d8db22839f3` (closure_hash of input_pin_map | machinery_pin_map: inventory pre/post SHAs, plan W13 SHA, s86/s84/s85 verdict-file SHAs, C29 / BK-Array / LiteBIRD audit SHAs, path_count=2, r_H=0.00745, r_C=0.0117, scheme_floor=0.125, dual_pathway=True, detector_1=BK-Array/2026, detector_2=LiteBIRD/2030)
- `content_sha256` = `41f96976d86eec38583618d70acf2da302f47d79e8531b858f64125ca8730cce` (SHA-256 of canonicalised diff-log JSON)

**Artifacts produced**:
- Producing script: `computations/s86_w13_p2_r_both_pathways_watchlist_landing.py`
- Per-field diff log: `computations/s86_w13_p2_r_both_pathways_watchlist_landing.json`
- Modified registry: `sessions/framework/registry/falsifier-master-inventory.md` (post-P11 23895 bytes → post-P2 29898 bytes; +6003 bytes; new section "## Row #2 r — Path-H / Path-C SEQUENCED detector chain (S86 W13 P2)" inserted before `## Provenance`)
- Verdict line + companion row: `computations/s86_gate_verdicts.txt`

**What PASS means for solution space (per plan §W13-7.11)**: The master inventory's Row #2 r is now dual-function — live-watch envelope (from C29) PLUS internal-consistency Path-H/Path-C registration (from this gate). Downstream gates citing "the framework's r prediction" must now specify Path-H OR Path-C. The SEQUENCED detector chain pre-registers a deterministic 2-stage falsification: BK-Array 2026 first-light classifies branch via 4-branch tree (S84 W4-42); LiteBIRD 2030 discriminates Path-H vs Path-C via n_T consistency at >4σ separation. The substrate's tensor-to-scalar prediction is now externally testable in 2 stages with explicit pre-registered branch mapping — a frozen, falsifiable prediction in the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 window codified by §W13-6 P1.

---

## Wave W13 Synthesis (team-lead)

**Date**: 2026-04-26. **Gates**: 7 (6 PASS + 1 INFO). **Dispatched**: W13-A (6 parallel: P11, P10, P9, P8, P12, P1) + W13-B (1 sequential: P2). All artifacts on disk; `computations/s86_gate_verdicts.txt` carries 7 gate verdict lines for W13 + 4 P12-driven re-emission lines (S85 W1a-9 + S85 W1b-3, two runs each) + 1 retained P12 first-attempt FAIL, with dual-SHA companion rows for every canonical line. 5 framework files touched (3 NEW + 1 modified twice + 1 modified once + canonical_constants.py edited additively).

### 1. Structural outcome — observational pin commitments codified at the framework level

Wave W13 is the consolidation wave for Session 86's observational pin commitments. None of the 7 gates produced a new physics result; every gate WROTE a registry / canonical-constants entry that downstream sessions cite verbatim. The wave's product is registry-discipline: by the end of W13, every framework prediction the substrate makes against an external-detector observation lives in a single authoritative file with a dual-SHA pin. This eliminates the citation-drift class observed in S78 W3-G that forced the SDW-KMS divergence.

The 5 framework files touched, with pre/post sizes:

- `sessions/framework/registry/falsifier-master-inventory.md`: 4,260B → 21,131B (P11 PAIR-1..6 + NEW row class #13–#21) → 30,009B (P2 r dual-pathway extension before §Provenance). Two writes, sequenced across W13-A → W13-B to avoid the parallel-writer-race documented in `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race".
- `sessions/framework/registry/f-nl-folded-pathway-registry.md`: NEW; 6,844B (P10 — 3 sub-channel projections of f_NL_folded with all 8 columns).
- `sessions/framework/registry/w0-primary-decision-rule.md`: NEW; 12,774B (P9 — 4-criterion adjudication + reversibility protocol + R_842 rectangle dual-definition record).
- `sessions/framework/registry/dr3-3row-7cell-subtree.md`: NEW; 8,296B (P8 — 14-pop + 7-stub matrix + 4-branch protocol).
- `sessions/framework/registry/baseline-findings-s66.md`: 31,657B → 43,061B (P1 — FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 4-level taxonomy + Both-Pathways r registration; +11,404B as 3 appended sections of 3,553/3,791/4,256 bytes).
- `computations/canonical_constants.py`: additive edit at lines 1221-1240 (P12 — `alpha_s_canon_2020 = +0.0023 ± 0.0063` Aiola+ 2020 ACT DR4 + Planck added alongside legacy `planck_alpha_s = -0.0045 ± 0.0067` Planck 2018 with LEGACY docstring; back-compat preserved — both `from canonical_constants import planck_alpha_s` and `from canonical_constants import alpha_s_canon_2020` succeed).

### 2. P9 source-reconciliation — runtime agent caught a rectangle drift the plan did not

The most structurally interesting in-wave finding is P9's runtime detection of an R_842 definition drift between the plan §W13-3.6 INPUT-PIN MAP (`R_842 = [-1.05, -0.85] × [-0.2, +0.2]`; range-form, half-width 0.100, center -0.95) and the mack-9A canonical from `sessions/archive/session-85/session-85-mack-synthesis-w6-13.md:75` (`R_842 = [-0.942, -0.742] × [-0.2, +0.2]`; center -0.842 from W10-2 branch-(iv) anchor, half-widths 0.100/0.200). These are geometrically distinct rectangles: under the plan-prompt rectangle, w_0_B = -0.842454 sits 0.0075 outside the upper edge -0.85; under the mack-9A canonical, both A=-0.918 and B=-0.842454 are inside.

This is exactly the SOURCE-RECONCILIATION sub-audit Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY drift pattern that `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" was written to surface. Sagan-empiricist did the right thing at runtime: recorded both definitions in §1 of `w0-primary-decision-rule.md`, honored the mack-9A canonical (the structural reference per the W10-2 branch-(iv) re-pin), and verified the verdict is INVARIANT under either rectangle (under canonical, both candidates inside Criterion 2 ties; under plan-prompt, A inside / B outside — but A wins on Criterion 4 registry-history-priority anyway). The decision rule is unaffected.

This drift should be added to the SOURCE-RECON calibration corpus alongside W1c-8 (`n_s` precision-floor) and W2-4 (cluster-span canonical-metric algebraic factor-2). Plan-freeze should have caught it; runtime caught it. The S86+ SOURCE-RECON pipeline is being extended to validate plan-prompt INPUT-PIN MAPs against the structural-source canonical at plan-freeze (technical-debt action item — clearable in-session via `epistemic-discipline.md` §"Source Reconciliation" calibration-corpus extension).

### 3. P12 tension-widening — the substrate's largest single-observable tension hardens; re-emissions numerically invariant

P12 updated the canonical α_s pin from Planck-2018 (-0.0045 ± 0.0067) to Aiola+ 2020 ACT DR4 + Planck (+0.0023 ± 0.0063). The framework prediction (`alpha_s_inflation_framework = -0.068968`, full float64 -0.06896799) is FROZEN — it derives from the S50-51 substrate-eigenvalue identity n_s² − 1 with n_s_canon = 0.9649, NOT data fitting.

Substitution chain (Python-verified, matches plan §W13-5.10 exactly):

| Quantity | Planck-2018 era | Aiola-2020 era | Δ |
|:---------|:---------------:|:--------------:|:--:|
| canon central (α_s^canon) | −0.0045 | +0.0023 | +0.0068 |
| gap = α_s^canon − α_s^FW | +0.064468 | +0.071268 | +0.0068 |
| canon σ | 0.0067 | 0.0063 | -0.0004 |
| n_σ = \|gap\|/σ | 9.622 σ | 11.312 σ | +1.690 σ |

α_s is now the framework's currently-largest single-observable tension. Substrate-framing assessment (per `phononic-framing.md`): this is "the substrate's α_s prediction is increasingly discriminable; future detector data (CMB-S4 by 2028, CMB-HD by 2030) will resolve whether the substrate-derived value is correct" — NOT "the framework is in 11σ tension and therefore wrong". The substrate prediction is FALSIFIABLE; that is its scientific value, not a defect. Reported as INFO sub-tag in the verdict line.

The W1a-9 + W1b-3 re-emissions are NUMERICALLY INVARIANT under the pin update:
- W1a-9 7D Fisher log10(BF_FW/LCDM) = +827.9256 (matches S85 baseline 827.9255704800152 to 1e-3); LCDM α_s reference is 0.0 (vanilla LCDM null), NOT canonical observational central — Fisher pull insensitive to canonical-pin convention.
- W1b-3 σ_corr/σ_diag = 1.1297479814965643 (matches S85 baseline to 1e-6); detector σ values are forecast noise budgets, NOT canonical observational σ — Cauchy-Schwarz widening ratio insensitive to canonical-pin convention.

The pin only enters tension calculations, not Fisher structure or detector-σ projections.

P12 also exposed a precision-floor bug in its own pre-flight aggregator (1e-12 tolerance against the 6-sig-fig published `-0.068968` vs full float64 `-0.06896799`) that produced a first-attempt FAIL at lines 205-206 retained alongside the second-attempt PASS at lines 211-212 per S86 W1c-5 all-3-lines-retained discipline. The fix loosened aggregator tolerance to 1e-5 per the W1c-8 Publication-Precision Pre-Registration rule (W1c-8 precedent). The gate's actual physics PASS threshold was never modified — PROHIBITED_ACTIONS Class-1/6 (convention-shopping / iterate-until-PASS) does not apply because the gate's underlying numerics were unchanged across runs; only the post-process verifier tolerance moved.

### 4. P8 INFO — methodological discipline divergence from W12-4 sibling

P8 emits INFO (`value=21cells=14pop+7stub,mono=7/7`). The L=8 row of the 3-row × 7-cell DR3 sub-tree could not be populated because S85 W7-7 publishes only `max_L_sensitivity = 0.0204` over an unrelated basket of 8 W_0-dependent constants {K_R5, K_substrate, K_crit, Γ_effacement, f_conv, c_sub_at_kpivot, F_amp_linearized, f_GGE_Leggett}, NOT a Zubarev w_0(L=8) value or a 7-scenario sub-decomposition. Per plan §W13-4.9 PRE-REG-INCOMPLETE INFO sub-class, the gate emits INFO with the partial 14-cell + 7-stub matrix; the 14 populated cells (L=10 + L=12, all 7 scenarios) are monotone in all 7 columns; the 4-branch adjudication protocol (REG-INVARIANT / REG-DEP-MAJORITY / STRUCTURAL-AMBIGUITY-FREEZE / EXTERNAL) is pre-registered against DR3 publication.

Methodological note: the W12-4 sibling gate `S86-DR3-3-LAYER-SUB-TREE` chose canonical-anchored offset reconstruction to populate L=8 (rho(L=8) + offset = -0.845, occupying scenario A1) and PASSed; P8's discipline forbids that fabrication path because extracting L=8 sub-cell values from a single-headline-value sensitivity scan would be ansatz-forced reconstruction. This is a productive divergence — W12-4 produces the 21-cell matrix with offset-reconstructed L=8 cells, P8 produces the 14-cell honest matrix with explicit L=8 stubs. Downstream sessions can choose which discipline to cite. The S87-W0 carry-forward `S87-DR3-SUB-TREE-3-ROW-PIN-PROMOTION` is pre-registered for direct Zubarev w_0(L=8) extraction from the L=8 D_K eigenvalue cache to PROMOTE INFO → PASS without offset reconstruction.

### 5. Sequencing-dependency outcomes — both prerequisites cleared

The wave's two cross-batch sequencing dependencies both cleared:

- **W11 C5 + W11 C6 → P11 NEW row class**: `S86-LAB-SI-TRANSLATION` INFO `9-rows-populated` at `s86_gate_verdicts.txt:182` and `S86-LAB-FALSIFIER-EVOI-TREE` PASS `9-rows-leveled-and-treed` at line 197. P11's NEW row class #13–#21 fully populated with 9 atomic predictions (3 sweet-spot + 6 cross-platform across 3He-A/FeSe/173Yb), all in LAB-FALSIFIER-A level with detection_ratio ≥ 10. PRE-REG-INCOMPLETE INFO clause NOT triggered.
- **W1c C29 → P2 r-row extension**: `S86-FALSIFIER-MASTER-INVENTORY-PROMOTION` PASS at `s86_gate_verdicts.txt:55` (audit `32c60c2f69fe6150...`, content `144a9999104f3662...`). P2 extends C29's single-row promotion (live-watch envelope only) into the dual-pathway falsifier (Path-H 0.00745 + Path-C 0.0117 + 36.3% Path-C-relative split + 12.5% scheme-floor flag DUAL_PATHWAY=TRUE + SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030). PRE-REG-INCOMPLETE INFO clause NOT triggered.

Cross-row file coordination: P11 and P2 both wrote `falsifier-master-inventory.md` — the orchestrator split them across W13-A (P11) and W13-B (P2) sequentially. P11 added a minimal cross-reference annotation on Row #2 r pointing to §W13-7 (P2); P2 then landed the full detector chain content the cross-reference points to. Same-wave registry construction with intra-wave dependency, no race.

### 6. Downstream implications

| Stream | Effect of W13 | Downstream action |
|:-------|:--------------|:------------------|
| Master inventory | row count 12 → 13; 9 lab-falsifier predictions newly SHA-tagged | W14 + W15 cite as authoritative single-page summary; lab-falsifier suite dispatchable to Aalto/Helsinki, Florence/Grenoble, Florence/JILA/Munich contacts via SHA-pinned proposal |
| f_NL_folded | 3-pathway disambiguation (S82 0.0547 / S67 0.129 / W9-3 0.7685) | downstream gates citing "the framework's f_NL_folded" must specify pathway tag; SKA-1 sole 2030s-era discriminator (W9-3 pathway only); CMB-S4 σ=6.9 detector-sterile across all three |
| w_0 PRIMARY | A=-0.918 designated; B=-0.842454 SECONDARY-with-reversibility | DR3 publication (window opened 2026-04-23 per S84-W1b-9) is deterministic test; PRIMARY reverses to B if w_0_obs ∈ [-0.86, -0.83] (R_842 lockout protocol) |
| R_842 rectangle drift | both definitions recorded; verdict invariant | technical-debt action: extend SOURCE-RECON calibration corpus with this drift class so plan-freeze validators flag it next time |
| DR3 sub-tree | 14-pop + 7-stub matrix; 4-branch protocol pre-registered | S87-W0 dispatches `S87-DR3-SUB-TREE-3-ROW-PIN-PROMOTION` to extract L=8 sub-cells from L=8 D_K eigenvalue cache; W12-4 sibling provides offset-reconstructed alternative (downstream chooses discipline) |
| α_s canon | -0.0045 (Planck-2018) → +0.0023 (Aiola-2020 ACT DR4 + Planck) | tension hardens 9.62σ → 11.31σ; framework UNCHANGED; CMB-S4 by 2028 decisive; CMB-S4 / CMB-HD / SKA-1 forecast σ shift accordingly |
| FROZEN-COMMIT 2026-2030 | 7 frozen pins + 4-level taxonomy + Both-Pathways r registered | downstream sessions citing "frozen pins" point to `baseline-findings-s66.md`; per-level edit-discipline blocks convention-shopping at framework level; 3 reversibility triggers (w_0/DR3, r/BK+LiteBIRD, α_s/CMB-S4) |
| r dual-pathway | Path-H 0.00745 + Path-C 0.0117 + 36.3% split + SEQUENCED detector chain | BK-Array 2026 classifies branch via 4-branch tree (S84 W4-42); LiteBIRD 2030 discriminates Path-H vs Path-C at >4σ via n_T = -r/8 (Path-H -0.000931, Path-C -0.001463) |

### 7. Wave classification

This is a **registry-consolidation wave**, not a constraint-map-advancing one. W13 produces no new physics predictions; it codifies existing predictions into authoritative sources with explicit reversibility triggers. Taken as a set, W13:

- **Codified** the framework's frozen-prediction discipline (FROZEN-COMMIT 2026-2030 with 3 reversibility triggers + 4-level edit-discipline taxonomy).
- **Disambiguated** two previously-conflated multi-value predictions (f_NL_folded 3-pathway; r dual-pathway).
- **Selected** a PRIMARY among two competing w_0 candidates with explicit reversibility protocol; recorded both rectangles for the runtime-detected R_842 drift.
- **Updated** one observational canon (α_s) with re-emission of dependent verdict lines (numerically invariant by structural-independence argument).
- **Documented** the L=8 DR3 sub-tree gap as a structured INFO outcome with pre-registered S87-W0 carry-forward; preserved methodological-discipline divergence from W12-4 sibling.
- **Promoted** 9 lab-falsifier predictions to a NEW master-inventory row class with full SHA-tagged source provenance through W11 C5/C6.

The wave's outputs are not new walls in the constraint map; they are the framework's pre-publication discipline against the 2026-2030 detector window. DR3 (2026-04-23 window open), BK-Array (2026), CMB-S4 (2028), LiteBIRD (2030) read against these pinned predictions. Whether the substrate's predictions survive is a question for the experiments, not for any further pre-registration step in S86+.

dual-SHA closure (per `gate-verdicts.md` S81+ canonical form): all 7 gates carry full 64-character `audit_sha256` and `content_sha256` with companion comment rows. P12 emits 3 verdict-line classes (P12 + W1a-9 RE-EMIT + W1b-3 RE-EMIT) each with their own dual-SHA across two runs (FAIL+PASS for P12 itself, PASS+PASS for both re-emissions; the FAIL was a precision-floor verifier bug, not a physics defect). v3-ladder sig_2 (dual-SHA presence) satisfied for all W13 verdict lines in `computations/s86_gate_verdicts.txt`.

---

## Appendix A — Triple-protection map for α_s structural rigidity (T8-5 install, NEEDS-DECISION installed with `(NEEDS-ORCHESTRATOR-FOLLOWUP)` annotation per S86 W2 WP-PATCH-5 + R3-B EMERGENCE (i) L1465-1494 + R3-B CONVERGENCE L1390-1394, applied 2026-04-27)

> **Source**: S86 W2 workshop R3-FINAL closure (volovik R3 FINAL turn complete; all 13 Workshop Verdict rows Converged/Emerged); R3-B EMERGENCE (i) lines 1465-1494 (triple-protection structural reading); R3-B CONVERGENCE lines 1390-1394 (Class I-V dominant-floor table).

The S86 W2 workshop closure established that the framework's α_s = n_s² − 1 identity is **TRIPLE-ANCHORED** at the substrate level. Three independent structural mechanisms protect the identity from regulator-class deformation; substrate ceiling on the deformation is `|δα_substrate| ≲ 8.65 × 10⁻⁵` absolute (`1.25 × 10⁻³` relative), 10⁴× below the sign-flip requirement `δα = 0.069`.

### Three-anchor block diagram

```
                      ┌─────────────────────────────────────────┐
                      │   α_s = n_s² − 1  (S50-51 identity)     │
                      │   substrate-derived; rational-exact     │
                      │   at u_pivot = 19649/351 = 55.9800..    │
                      │   α_s_FW = -6896799/100000000           │
                      │            = -6.896799 × 10⁻²           │
                      └────────────────────┬────────────────────┘
                                           │
                ┌──────────────────────────┼──────────────────────────┐
                │                          │                          │
        ┌───────▼────────┐        ┌────────▼────────┐        ┌────────▼────────┐
        │  ANCHOR 1      │        │  ANCHOR 2       │        │  ANCHOR 3       │
        │  BDI           │        │  Kinematic      │        │  Sub-threshold  │
        │  universality  │        │  suppression    │        │  inter-band     │
        │                │        │  of optical-    │        │  coupling       │
        │  Leggett       │        │  branch weight  │        │                 │
        │  dipolar gap   │        │  at CMB pivot   │        │  Gap >> ω_pivot │
        │  protection;   │        │                 │        │  precludes      │
        │  KO-dim 6 +    │        │  (k_pivot/      │        │  rotation of    │
        │  AZ symmetry   │        │   ω_L1)² ~ 10⁻⁴ │        │  optical mode   │
        │  algebra TRS-  │        │                 │        │  contribution   │
        │  PHS-chiral    │        │  places sub-    │        │  through Γ-pre- │
        │                │        │  strate at CMB  │        │  factor channel │
        │  K-homogeneity │        │  pivot in       │        │                 │
        │  enforced at   │        │  Class I/II of  │        │  Class V        │
        │  pivot         │        │  propagator     │        │  running-mass   │
        │                │        │  taxonomy       │        │  γ leakage =    │
        │  ⇒ Class I/II  │        │                 │        │  γ·u/(1+u) at   │
        │     anchor     │        │  ⇒ excludes     │        │  γ_pivot ~      │
        │                │        │     Class IV    │        │  4.4×10⁻⁵       │
        │                │        │     leakage     │        │                 │
        │                │        │     (1.9×10⁻⁹)  │        │  ⇒ 8.65×10⁻⁵    │
        │                │        │                 │        │     absolute    │
        │                │        │                 │        │     ceiling     │
        └────────────────┘        └─────────────────┘        └─────────────────┘
                │                          │                          │
                └──────────────────────────┼──────────────────────────┘
                                           │
                            ┌──────────────▼─────────────────┐
                            │ Substrate ceiling on deformation: │
                            │  |δα_substrate| ≲ 8.65 × 10⁻⁵    │
                            │  10⁴× below sign-flip δα = 0.069  │
                            └────────────────────────────────────┘
```

The three anchors are **structurally independent** — each enforces a different aspect of the identity protection. Anchor 1 (BDI universality) is a representation-theoretic property of the spectral triple's KO-dimension and AZ symmetry algebra; Anchor 2 (kinematic suppression) is a substrate-spectral fact about the ω_L1 hierarchy at the CMB pivot; Anchor 3 (sub-threshold coupling) is a Wilsonian effective-action argument about which inter-band channels can rotate the C1 identity. Removal of any one anchor would not lift the identity (the remaining two would still hold); removal of all three simultaneously would require a specific substrate-physics scenario (BDI → non-BDI universality class transition + ω_L1 hierarchy collapse + sub-threshold gap closure) that no single observational signal can drive.

### Class I-V propagator taxonomy row table (per R3-B CONVERGENCE L1390-1394 dominant-floor table)

| Class | Definition | Identity status | Leading deviation coefficient | Substrate location at CMB pivot |
|:------|:-----------|:----------------|:------------------------------|:--------------------------------|
| **I** | Single literal pole | EXACT (residue ≡ 0 symbolically) | n/a | **DOMINANT** (substrate Goldstone propagator) |
| **II** | Degenerate multi-pole, shared (J, m²) | EXACT (algebraically reduces to Class I) | n/a | **DOMINANT** (universality with Class I) |
| **III** | K-homogeneity ODE family at A ≠ −1, f(u) = 2A/(u−A) | EXACT BY CONSTRUCTION (mathematical tool) | n/a | NOT-INSTANTIATED (mathematical-only solutions; no substrate counterpart) |
| **IV** | Independent multi-pole, distinct (J_i, m_i²) | BROKEN at order w_2 · asymmetry | (16/840123) · w_2 at substrate-physical test point (J_1=1, m_1²=56, J_2=2, m_2²=100, K=1) | **SUB-DETECTOR LEAKAGE** at 1.9 × 10⁻⁹ — kinematically suppressed by Anchor 2 |
| **V** | Running-mass m²(K) = m_0² · (K/K_0)^γ with γ ≠ 0, 2 | BROKEN at order γ · u/(1+u) | γ · 2u/(1+u) at γ_pivot ~ 4.4 × 10⁻⁵, u_pivot = 55.98 | **SUB-DETECTOR LEAKAGE** at 8.65 × 10⁻⁵ absolute (1.25 × 10⁻³ relative) — sub-threshold-suppressed by Anchor 3 |

The substrate at the CMB pivot is **Class I/II dominant** (single-effective-pole equivalence class — Anchor 1) with **Class IV and Class V sub-detector leakages** (Anchors 2 and 3 cap each leakage well below detector resolution at CMB-S4 σ_α_s ≈ 2.1 × 10⁻³). The leakage ceiling is 8.65 × 10⁻⁵ absolute, 10⁴× below the sign-flip requirement δα = 0.069 — i.e., the substrate's structural protection of α_s = n_s² − 1 is robust against any combination of Class IV and Class V leakages by 4 orders of magnitude.

### Substrate-framing reading (per R3-B EMERGENCE (i))

The triple-protection map is a **substrate-physics structural reading** of why the C1 identity α_s = n_s² − 1 is rigid against regulator-class redefinition. None of the three anchors is "the" reason — they are three independent corollaries of the spectral triple's structure at the τ_fold slice (Anchor 1 from KO-dim + AZ algebra; Anchor 2 from the post-fold spectral hierarchy; Anchor 3 from the Wilsonian effective coupling structure). The (16/840123) · w_2 Class IV leading coefficient and the γ · 2u/(1+u) Class V leakage form are Sage-symbolic-verified at substrate-physical test points; the multiplicative substrate ceiling 1.25 × 10⁻³ relative is the structural floor of the framework's α_s protection at the current spectral-triple pinning.

**Decision pending (NEEDS-ORCHESTRATOR-FOLLOWUP)**: whether this appendix should be promoted to a permanent §VII registry entry (overlap with W2 OTHER-FRAMEWORK-1 / OTHER-FRAMEWORK-5 candidate `sessions/framework/alpha-s-structural-protection.md` extension) or remain as W13 working-paper appendix only. The triple-protection map is structurally complete at workshop closure; the registry-promotion decision is an architectural choice about whether α_s_protection becomes a top-level §VII observational-anchor or a W13-internal supporting argument.

---

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-04-26 | falsifier-master-inventory row count | 12 canonical observable rows | 13 (12 + 1 NEW lab-falsifier suite #13–#21, 9 atomic predictions) | P11 PASS — 6 PAIR-enrichments + 9 atomic predictions; all rows carry dual-SHA |
| 2026-04-26 | f_NL_folded pathway registry | absent (3 sub-channel values scattered across S82/S67/S85 verdicts) | created at `f-nl-folded-pathway-registry.md` (3-row × 8-column) | P10 PASS — exact-echo of S82 0.0547 / S67 0.129 / W9-3 0.7685 |
| 2026-04-26 | w_0 PRIMARY designation | undesignated (A=-0.918 in canonical_constants, B=-0.842454 contender from W10-2) | A=-0.918 PRIMARY, B=-0.842454 SECONDARY-with-reversibility | P9 PASS — 4-criterion adjudication; reversal triggers on DR3 w_0 ∈ [-0.86, -0.83] |
| 2026-04-26 | R_842 rectangle definition (drift detected at runtime) | plan-prompt: `[-1.05, -0.85]`; mack-9A canonical: `[-0.942, -0.742]` (silent drift) | both definitions recorded in `w0-primary-decision-rule.md` §1; mack-9A canonical honored; verdict invariant | P9 runtime detection of Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY drift; SOURCE-RECON calibration-corpus extension queued |
| 2026-04-26 | DR3 sub-tree | 2-row × 7-cell (L=10, L=12) from S85 W1b-1 | 3-row × 7-cell (L=8 stub + L=10 + L=12); 14-pop + 7-stub matrix | P8 INFO — plan §W13-4.9 PRE-REG-INCOMPLETE; L=8 sub-cells unavailable from W7-7; S87-W0 promotion pre-registered |
| 2026-04-26 | DR3 4-branch adjudication protocol | absent | pre-registered (REG-INVARIANT / REG-DEP-MAJORITY / STRUCTURAL-AMBIGUITY-FREEZE / EXTERNAL) | P8 — operative for L=10/L=12 axis on DR3 publication |
| 2026-04-26 | α_s canonical pin | `planck_alpha_s = -0.0045 ± 0.0067` (Planck 2018) | `alpha_s_canon_2020 = +0.0023 ± 0.0063` (Aiola 2020 ACT DR4 + Planck) added; legacy retained | P12 PASS additive edit; framework α_s prediction (-0.068968) UNCHANGED |
| 2026-04-26 | α_s framework-vs-canon tension | 9.622σ (vs Planck-2018) | 11.312σ (vs Aiola-2020); Δn_σ = +1.690σ | P12 substitution chain — INFO sub-tag; substrate prediction FROZEN, only canon moved |
| 2026-04-26 | S85 W1a-9 7D Fisher log10(BF) | 827.9256 (Planck-2018 era) | 827.9256 (Aiola-2020 era; numerically invariant) | P12 re-emission — Fisher structure independent of canonical observational central (LCDM null = 0.0) |
| 2026-04-26 | S85 W1b-3 σ_corr/σ_diag | 1.1297 (Planck-2018 era) | 1.1297 (Aiola-2020 era; numerically invariant) | P12 re-emission — detector-σ projections independent of canonical-pin convention |
| 2026-04-26 | FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 | absent (per-pin commitments scattered across canonical_constants + S73b + W-2 workshop) | landed in `baseline-findings-s66.md` (3 sections, +11,404B) | P1 PASS — 7 frozen pins + 3 reversibility triggers (w_0/DR3, r/BK+LiteBIRD, α_s/CMB-S4) |
| 2026-04-26 | 4-level unit-class taxonomy | absent | landed in `baseline-findings-s66.md` | P1 — Level 1 Fold structural-floor / Level 2 Pre-fold convention-pin / Level 3 Observational boundary / Level 4 Observational prediction with per-level edit-discipline |
| 2026-04-26 | r BOTH-Pathways watchlist (master-inventory Row #2) | C29 single-function (live-watch envelope only) | dual-function (live-watch + Path-H/Path-C internal-consistency + SEQUENCED detector chain) | P2 PASS additive extension — Path-H 0.00745 + Path-C 0.0117 + 36.3% Path-C-relative split + 12.5% scheme-floor flag DUAL_PATHWAY=TRUE |
| 2026-04-26 | r SEQUENCED detector chain | absent (BK-Array + LiteBIRD listed separately as detectors) | pre-registered 2-stage falsifier (BK-Array 2026 4-branch tree → LiteBIRD 2030 n_T = -r/8 discrimination) | P2 — Stage-1 classifies branch (S84 W4-42); Stage-2 discriminates Path-H vs Path-C at >4σ via n_T separation |
| 2026-04-26 | P12 first-attempt FAIL retention discipline | precedent unestablished for canonical-update gates | first-attempt FAIL at lines 205-206 retained alongside second-attempt PASS at lines 211-212 per S86 W1c-5 all-3-lines-retained discipline | aggregator-tolerance precision-floor bug fixed via W1c-8 Publication-Precision rule; gate physics threshold unchanged; PROHIBITED_ACTIONS Class-1/6 not triggered |

---

## Files Produced

| Gate | Producing script | Data files | Framework file modified / created | Verdict file lines |
|:-----|:-----------------|:-----------|:----------------------------------|:-------------------|
| §W13-1 P11 | `computations/s86_w13_p11_master_inventory_w6_w13_land.py` (41,037B) | `.json` (11,214B) | `falsifier-master-inventory.md` (4,260B → 21,131B; +PAIR-1..6 + NEW row class #13–#21) | 203 + companion 204 |
| §W13-2 P10 | `s86_w13_p10_fnl_folded_pathway_registry.py` (31,416B) | `.json` (3,828B) | `f-nl-folded-pathway-registry.md` (NEW; 6,844B) | 201 + companion 202 |
| §W13-3 P9 | `s86_w13_p9_w0_primary_value_resolve.py` (45,256B) | `.json` (8,116B) | `w0-primary-decision-rule.md` (NEW; 12,774B) | 219 + companion 220 |
| §W13-4 P8 | `s86_w13_p8_dr3_sub_tree_3_row_pin.py` (51,224B) | `.json` (11,717B) + `.npz` (5,755B) | `dr3-3row-7cell-subtree.md` (NEW; 8,296B) | 221 + companion 222 |
| §W13-5 P12 | `s86_w13_p12_alpha_s_canonical_update.py` (39,879B) | `.json` (3,463B) + `_re_emit_w1a_9.json` (2,228B) + `_re_emit_w1b_3.json` (1,492B) | `canonical_constants.py` (additive lines 1221-1240; legacy retained with LEGACY docstring) | 205-216 (P12 FAIL+PASS + W1a-9 PASS×2 + W1b-3 PASS×2, all with companions; 12 lines) |
| §W13-6 P1 | `s86_w13_p1_frozen_commit_landing.py` (29,892B) | `.json` (5,489B) | `baseline-findings-s66.md` (31,657B → 43,061B; +3 appended sections of 3,553/3,791/4,256 bytes) | 217 + companion 218 |
| §W13-7 P2 | `s86_w13_p2_r_both_pathways_watchlist_landing.py` (38,384B) | `.json` (3,787B) | `falsifier-master-inventory.md` (21,131B → 30,009B; new "Row #2 r — Path-H / Path-C SEQUENCED detector chain" section before §Provenance) | 229 + companion 230 |

7 producing scripts under `computations/s86_w13_*.py`; 9 JSON diff/audit logs (P12 has 3); 1 NPZ (P8 only); 5 framework files touched (`falsifier-master-inventory.md` ×2 [P11+P2] + 3 NEW + `baseline-findings-s66.md` modified) + `canonical_constants.py` modified; W13's footprint in `computations/s86_gate_verdicts.txt` spans lines 201-230 (interleaved with parallel-session WATCHLIST gates at 223-226 from non-W13 dispatch).

Verdicts appended; framework registries modified; canonical_constants.py extended additively; knowledge-MCP `update_constant` calls deferred to `/weave --update` post-synthesis.

---

**End of Wave W13 Working Paper.** 7 gate sections (6 PASS + 1 INFO) with full Verdict + Results + dual-SHA + substrate-framing assessment + on-disk artifacts; orchestrator synthesis section (§"Wave W13 Synthesis (team-lead)") + Constraint-Map Updates (15 entries) + Files Produced.
