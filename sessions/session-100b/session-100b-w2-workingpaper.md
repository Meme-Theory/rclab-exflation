# Session 100b Wave 2 — Substrate Texture / Algebra Classification (Results Working Paper)

**Session**: 100b | **Wave**: 2 | **Plan**: session-100b-plan-w2.md | **Theme**: representation-theoretic classification of the finite-algebra content of `(A_K, H_K, D_K)` — Sym³(3) cubic-ladder hierarchy-exponent corroboration of §VII.BL, Pati-Salam variant ID from the rescued order-one defect fingerprint, M_R two-zero texture classification under the discrete {0, π} CP set.

## Gate Sections

### §W2-1. S100b-SYM3-CUBIC-LADDER-P-EXPONENT (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-SYM3-CUBIC-LADDER-P-EXPONENT`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (generation-sector cubic-ladder hierarchy-exponent fit)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: Feeding the bottom-3 generation-sector D_K eigenvalues at τ_fold ((1,0)/(1,1)/(3,0), C₂ = 4/3, 3, 6) through the paper-02 exceptional-Jordan Sym³(3) cubic ladder yields p ∈ [0.8, 1.2] and a widening residual ≤ the 9/5 benchmark — the expected Track-B INFO quantifies the §VII.BL ε_LX gap in both scale and shape.
**Plan reference**: `sessions/session-plan/session-100b-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain, dual-prior, circularity guard).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

| Artifact | Path | Existence | must_contain verification |
|:---------|:-----|:----------|:--------------------------|
| script | `computations/session-100b/s100b_w2_1_sym3_cubic_ladder_p_exponent.py` | on disk (37,371 B) | `grep -c "from canonical_constants import"` → 2; `grep -c "print_verdict_payload"` → 3 |
| data | `computations/session-100b/s100b_w2_1_sym3_cubic_ladder_p_exponent.npz` | on disk (17,067 B; 44 keys) | n/a (optional: false; satisfied by existence) |
| plot | `computations/session-100b/s100b_w2_1_sym3_cubic_ladder_p_exponent.png` | on disk (134,006 B) | n/a (optional: false; satisfied by existence) |
| verdict_line | `computations/session-100b/s100b_gate_verdicts.txt` | appended via `emit_verdict` (5 rows: canonical + dual-SHA companion + schema-v2 3-tuple + 2 extra rows) | `grep -E '^S100b-SYM3-CUBIC-LADDER-P-EXPONENT:.* audit_sha256=[a-f0-9]{64}'` → 1 canonical line (INFO; full line quoted under Verdict below) |
| wp_section | this section | this section | Status/Verdict/Output Artifacts/MCP Pre-Compute Audit blocks present |

**MCP Pre-Compute Audit**:

- `search_knowledge("Sym3 cubic ladder p exponent")` → 10 hits, ALL either the plan-w2 equations themselves or unrelated (S36 GL-cubic, S55 ladder_test, S88 base-2 ladder spectroscopy, cubic-BC exponent open channel). **NOT PRE-CLOSED** — no prior verdict for this gate ID.
- `get_constant("m_tau_PDG")` → **1.77686** (S100a, source: PDG tau pole mass 1776.86 ± 0.12 MeV, gate S100a-CONNES-DISTANCE-LADDER) — equals the plan inline pin exactly; imported from canonical and runtime-asserted equal.
- `get_constant("m_e")` → 0.00051099895 GeV (S98, PDG 2024/CODATA; gate S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN).
- `get_constant("m_mu")` → 0.1056583745 GeV (no PROVENANCE entry — hygiene flag below).
- `get_constant("m_tau")` → 2.062, **no PROVENANCE entry** — the S42 modulus-mass-at-fold (M_KK units) = S62 J-ratio image; the FORBIDDEN circular target (guard enforced in-script).

**Verdict**: **INFO** — the pre-registered Track-B expected outcome (dual-prior 0.90 → posterior 0.9 track_B). Ladder strictly present; clause (a) FAIL and clause (b) FAIL. Canonical line (emitted race-safe via `emit_verdict`):

```
S100b-SYM3-CUBIC-LADDER-P-EXPONENT: INFO -- value='p2param=15.52;panchored=14.82;band=[0.8,1.2];Wladder=0.1214;WPDG=1.889;resid=1.768;bench=0.08904;clauseA=FAIL;clauseB=FAIL;ladder=strict;track_B_posterior_0.9' scheme=Sym3-cubic-ladder-paper02 convention=log-LSQ-3pt-PDG-target L_max=12 audit_sha256=5c06a124046cdcf471cd6f7c25c235801ba769497d70d5019f404a78863936ad content_sha256=dcfd1da4c9605ab01da8c187ba235929cc6bb6b3060bea5392f531e353837221 schema_version=S84+
```

Schema-v2 3-tuple (directional prediction pre-registered in the plan substitution chain): `sign_verdict=PASS` (predicted direction realized: p out-of-band ABOVE at O(10), substrate ladder narrows where the data widen, both clauses fail), `magnitude_verdict=INFO` (the plan's INFO_meaning assigns ANY ladder-present clause-failure to INFO — the pre-registered INFO band is unbounded by construction), `regime_verdict=VALID` (deterministic 3-point closed-form fit on SHA-pinned cache reads; no scan, no expansion, no auto-shortening). Collapse-rule consistency asserted in-script: collapse(PASS, INFO, VALID) = INFO = gate-rubric composite.

**Results** (NUMBERS first; all from `s100b_w2_1_sym3_cubic_ladder_p_exponent.py`, wall 0.5 s, cpu-cap-OMP8):

*Eigenvalue triple* (L12 master cache, SHA `9e6d9cf7…` runtime-asserted = plan pin; plan-freeze drift 0.000e+00):

| gen | sector (p,q) | λ_min (M_KK) | C₂ exact | triality t = (p−q) mod 3 | η_FB = λ/√(C₂+1) |
|:----|:-------------|:-------------|:---------|:------------------------|:------------------|
| e | (1,0) | 0.8358935078737343 | 4/3 | 1 | 0.5472 |
| μ | (1,1) | 0.8729750338775074 | 3 | 0 | 0.4365 |
| τ | (3,0) | 1.2482641332621027 | 6 | 0 | 0.4718 |

Ladder-presence: strict ordering with rel-seps (0.04436, 0.42990) ≫ 1e-9 → PRESENT (FAIL branch not taken). Triality diagnostic t = (1, 0, 0) as pinned.

*Clause (a) — scale*: p_fit = **15.52** (2-param log-LSQ headline; full float64 15.52300190868059, intercept c = −2.6009) vs band [0.8, 1.2] → **FAIL**. Operator-block anchored cross-check form: p = **14.82** (14.822672739495449) → FAIL; clause-(a) verdict identical under both forms (agreement flag True). Per-step exponents p₂₁ = 122.83, p₃₂ = 7.892 — mutually DISCORDANT, so no single power law describes the bare triple at any p. Paper-convention image (paper-02 Eq. 63: √m ∝ Λ^p ⇒ ln m = 2p ln Λ): p_paper = p_fit/2 = 7.76 — out-of-band under EITHER convention; the verdict is convention-robust.

*Clause (b) — shape (p-independent)*: W_ladder = **0.1214** (0.12137993993490456, NARROWING) vs W_PDG = **1.8890** (1.889035501870293, WIDENING); residual |W_ladder − W_PDG| = **1.768** vs benchmark |9/5 − W_PDG| = **0.08904** (runtime, from canonical full-precision pins; plan-freeze reference 0.08910 from the rounded plan-printed masses — anticipated in the plan's strict_PASS_boundary note) → **FAIL** (residual ≈ 19.85× benchmark). Internal-consistency identity W_ladder/W_PDG = p₃₂/p₂₁ verified to < 1e-12.

*Sage-QQ cross-checks* (plan method, executed via Sage-MCP, sagecell backend): C₂(1,0) = 4/3, C₂(1,1) = 3, C₂(3,0) = 6 — exact QQ match to the in-script `fractions.Fraction` computation. W_PDG = 1.8890355018702926… and |9/5 − W_PDG| = 0.0890355018702926… at 120-bit precision with exact-rational mass arguments (m_e = 510998950/10¹², m_mu = 1056583745/10¹⁰, m_tau_PDG = 177686/10⁵) — the script float64 values agree to full float precision. Band edges exact: 4/5, 6/5, 9/5.

*Substitution chain (runtime-substituted numbers, mirroring plan §W2-1 item 7)*:
- Step 1: λ = (0.8358935078737343, 0.8729750338775074, 1.2482641332621027) [cache, drift 0 vs plan-freeze]
- Step 2: r₂₁ = λ₂/λ₁ = 1.044362; r₃₂ = λ₃/λ₂ = 1.429897
- Step 3: m_μ/m_e = 206.7682810; m_τPDG/m_μ = 16.8170295 [canonical full-precision pins]
- Step 4: p₂₁ = ln(206.768)/ln(1.044362) = 122.83; p₃₂ = ln(16.817)/ln(1.429897) = 7.892 — discordant
- Step 5: single-p LSQ lands between per-step values: 15.52 (2-param) / 14.82 (anchored), O(10) ≫ 1.2
- Step 6: W_ladder = 0.1214 (narrowing) vs W_PDG = 1.8890 (widening); 1.768 ≫ 0.08904
- Direction: BOTH clauses fail for the bare triple, exactly as pre-registered → Track B realized; sign_verdict = PASS.

*Diagnostics (not gate-bearing)*: Friedrich-Bär ratios η_FB = (0.5472, 0.4365, 0.4718) — non-constant, i.e. the Jensen deformation at τ_fold distorts the tower away from pure Casimir scaling in the NARROWING direction (the (1,0)–(1,1) gap is squeezed, η_FB drops 0.547 → 0.436). Pure-Casimir tower widening W_Casimir = ln(√4/√(7/3))/ln(√7/√4) = 0.9632 < 1: even the undeformed √(C₂+1) ladder narrows slightly, the deformed substrate ladder narrows hard (0.1214), and the data WIDEN (1.8890) — the widening cannot come from this sector tower at τ_fold under either the bare or Casimir-floor shape.

*ε_LX two-axis gap quantification (the INFO content per plan INFO_meaning)*: scale gap p/1 = **×15.52**; shape gap residual/benchmark = **×19.85**. The ε_LX deformation required by §VII.BL is two-dimensional — scale AND shape — now quantified on the paper-02 mechanism.

*Paper-02 corroboration (fetched-source-only; SHA `86f95f08…` runtime-asserted = plan pin)*: Teli & Singh (arXiv:2605.24866) reach p ≃ 1 ONLY by promoting (r, p, Φ_e) to FITTED spectral moduli — best fit r = −0.98747, p = 0.98747, cos Φ_e = −0.50877, χ²_log = 0.0745 (runtime regex-verified in the pinned PDF: extraction_ok = True, "0.98747" ×2, "0.50877", "0.0745" all present). Their own charged-lepton construction needs an extra spectral tilt T_ℓ^p on the lower rung beyond the pure cubic ladder (their Eqs. 61–62) — the same wall: a pure ladder cannot carry the charged-lepton widening. The substrate, with DERIVED eigenvalues and nothing fitted, lands at p = 15.52 — the corroboration is genuine and non-shared-context (different algebra: J₃(O_C) vs A_K; external authors; same fitted-moduli admission).

*Phase-free mass-fit → mixing-sector ε_LX mapping (plan structural annotation)*: the mass-sector fit is REAL (phase-free LSQ on |λ| magnitudes vs real PDG masses), consistent with the S99 reality adjudication — mass splitting from |w| only. The octonionic-phase analog (arg w) lives in the MIXING sector (PMNS/CP), not in masses; paper-02's fitted charged-lepton octonionic phase Φ_e (entering their cubic det-invariant τ, Table II "64 cos Φ_e") is mapped onto the MIXING sector of ε_LX in the substrate realization, not onto this mass fit. Recorded in the npz `structural_annotation` and as a verdict-file extra row.

*Circularity-guard hygiene flags*: (1) the PDG target used is m_tau_PDG = 1.77686 (plan inline pin = canonical S100a value, asserted equal in-script); canonical `m_tau = 2.062` (S42 modulus mass = S62 J-ratio image 19.52 × m_mu = 2.0625, identity confirmed in-script to < 5e-4) was NEVER consumed as target — guard assert passed. (2) Hygiene gap remaining: `m_tau = 2.062` and `m_mu` still lack PROVENANCE dict entries in canonical_constants.py (MCP returns "No PROVENANCE entry"); m_tau carries only the line-497 inline comment. The name-collision warning itself is already documented at the m_tau_PDG line-675 comment (S100a remediation), so the residual gap is provenance-dict-only.

*Methodology deviation note (honest disclosure per math-scripts.md §"Plan-author discipline")*: the plan block carries two non-identical fit forms — method.description + machinery_pin_map.fit_form specify "log-LSQ, 3 points, 2 params (p, c)" while operator.form writes the anchored 1-param contrast form argmin_p Σᵢ[ln(mᵢ/m₃) − p ln(λᵢ/λ₃)]². Both were computed (15.52 vs 14.82); clause (a) is evaluated headline on the 2-param form (2-of-3 plan fields + the convention tag `log-LSQ-3pt-PDG-target`), with the operator form as cross-check; the two forms are clause-equivalent on this data, so the intra-plan discrepancy is NOT a verdict lever (no convention-shopping surface). Both values and the agreement flag are in the npz and the verdict-file extra row.

**4-tuple**: (value=`p2param=15.52;…;track_B_posterior_0.9`, scheme=Sym3-cubic-ladder-paper02, convention=log-LSQ-3pt-PDG-target, L_max=12). Publication precision 4 sig figs (Class 8.3; downstream rel_tol ≥ 1e-4; full float64 in the npz).

**Dual-SHA**: audit_sha256 = `5c06a124046cdcf471cd6f7c25c235801ba769497d70d5019f404a78863936ad` (script + canonical_constants + pinmap incl. machinery-pin pseudo-entry per plan audit_discriminators); content_sha256 = `dcfd1da4c9605ab01da8c187ba235929cc6bb6b3060bea5392f531e353837221` (script only). Input pins: cache `9e6d9cf7fd6a6949…` (= plan pin, hard-asserted), paper-02 PDF `86f95f0839ca24df…` (= plan pin, hard-asserted), canonical_constants `440f6ba11ce90575…` (runtime), permanent-results-registry `120dfc2c5dce2915…` (runtime; §VII.BL anchor presence asserted).

**Substrate framing** (PARTICLE): the three generations ARE the Z₃-triality multiplicity content of the Peter-Weyl decomposition of D_K on SU(3); the tower (1,0)/(1,1)/(3,0) IS the substrate's bottom generation-sector eigenvalue triple at τ_fold. The arrow runs D_K eigenvalues → sector ladder → candidate Yukawa scales → PDG charged-lepton masses: the PDG masses are laboratory-IN shadows of the substrate-IS sector spectrum. §VII.BL (STAGE-3-PERMANENT) proves every A_K-built form is multiplicity-scalar — this gate measures, on an external 2026 J₃(O_C) mechanism that independently hit the same wall (and bought its p ≃ 1 with three fitted moduli), exactly how far the bare substrate ladder is from the data: ×15.5 in scale and ×19.9 in shape. The ε_LX deformation is thereby QUANTIFIED, not assumed; the obstruction is corroborated from outside the algebra. Per the plan's Wave-2 → Wave-3 decision point, the quantified (p, W_ladder) two-axis gap feeds the Q18b ε_LX corridor as a carry-forward constraint, to be cross-cited into the S100a rank-9b cluster reading (S100a-CONNES-DISTANCE-LADDER, SOFT cross-cite) at next synthesis.

> **Orientation rider (s100a-w2 mass-functional workshop, 2026-06-07; routed via orchestrator)**: this section's substrate-framing prose carries the lowest-C₂-first generation map; the cross-session adjudication pins the REVERSED (C₂-descending) charged-lepton orientation (e = (3,0); two S100a routes + this gate's own two-axis kill as corroboration); the prose map is superseded as orientation — the INFO verdict (audit `5c06a124046cdcf4`) and all numbers stand.

---

### §W2-2. S100b-PS-VARIANT-ID (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-PS-VARIANT-ID`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (Pati-Salam variant classification from the order-one defect fingerprint)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The S93 order-one defect fingerprint (4.000 → 2.100 under inner fluctuations, order_one_closes=False) matches exactly one Aydemir/CCS Pati-Salam variant, converting the RESCUED axiom status (§VII.W-3 Q10, STAGE-3-PERMANENT) into a positive beyond-SM identification with unification-boundary sin²θ_W = 3/8 exact and S₁(3̄,1,1/3) leptoquark extraction. *(The plan-block's "KO_dim=2" is a plan-text drift — see Methodology deviations below; the SHA-pinned npz ground truth is KO_dim=6.)*
**Plan reference**: `sessions/session-plan/session-100b-plan-w2.md` §W2-2 (3-axis fingerprint pin, taxonomy sources, 3/8 operationalization, rescued-axiom framing law).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

| Artifact | Path | Exists | must_contain verification |
|:---------|:-----|:-------|:--------------------------|
| script | `computations/session-100b/s100b_w2_2_ps_variant_id.py` (41,348 B) | YES | `grep -E "from canonical_constants import"` → `from canonical_constants import M_KK, sin2_thetaW_MSbar, tau_fold`; `grep -cE "print_verdict_payload"` → 2 |
| data | `computations/session-100b/s100b_w2_2_ps_variant_id.npz` (52,126 B) | YES | non-optional; carries grid/block matrices, 6-cell score table, sin² rationals, leptoquark JSON, source-quote pins, drift documentation |
| plot | `computations/session-100b/s100b_w2_2_ps_variant_id.png` (120,037 B) | YES | non-optional; 25×25 defect heat-map + per-block max matrix + 6-cell variant score table |
| verdict_line | `computations/session-100b/s100b_gate_verdicts.txt` | YES | `grep -E "^S100b-PS-VARIANT-ID:.* audit_sha256=[a-f0-9]{64}"` → canonical INFO line present; dual-SHA companion row + schema-v2 3-tuple row + 4 extra companion rows (regulator_pin, mellin_context, plan_text_drift, rescued_framing) appended by `emit_verdict` (race-safe, 7 rows) |
| wp_section | this section | YES | Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit / RESCUED all present |

**MCP Pre-Compute Audit**:

1. `search_knowledge("Pati-Salam variant identification sin2 theta_W")` → no prior verdict for `S100b-PS-VARIANT-ID`; related gates are out-of-scope for closure: `S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION` (PASS — K-counter candidate identification, different observable) and `S83-SIN2-THETA-W-2-LOOP-PLUS-MU-BC` (PASS — M_Z-scale accommodation row, cited as laboratory-IN CONTEXT ONLY per plan item (3), NOT gate-bearing here). NOT PRE-CLOSED.
2. `trace_entity("S93-W6-1 Pati-Salam SU4 algebra extension")` → no trace; the S93-W6-1 npz is consumed directly as the FAIL-as-input datum (plan Prerequisites: "that FAIL **is the input datum**").
3. Plan-freeze pre-checks (plan §"Wave 2 Summary", 2026-06-06, re-relied-on here): "PS-W3-I" carries NO knowledge-graph numerical pin → consistency-with-PS-W3-I operationalized as the exact-3/8 unification-boundary match (plan item (3)).
4. `canonical_constants.py` direct read: `sin2_thetaW_MSbar = 0.23122` (PDG 2024, M_Z context only), `tau_fold = 0.19`, `M_KK = M_KK_gravity` — npz context keys cross-asserted in-script (M_KK rel-diff < 1e-12, tau_fold abs < 1e-12).
5. `mcp__sage__sage_eval` (QQ-exact, plan-mandated): `Tr(T3L²) = 2`, `Tr(Q²) = 16/3`, `sin2_trace = sin2_matching = sin2_ncg = 3/8`, `all_equal_3_8 = True`; `Delta = -19/10 < 0` with endpoint `21/10 > 0`.

**Verdict**: **INFO** — pre-registered INFO clause realized: *unique* variant identified on fingerprint axes (i)+(ii) — **Model C (G422D, left-right D-symmetric)** — with the sin² clause satisfied *exactly* (|sin²θ_W(M_U) − 3/8| = 0.0 ≤ 1e-12), but the KO axis (iii) is **indeterminate from the published taxonomy** (zero "KO" occurrences in the SHA-pinned Aydemir PDF text layer; no per-variant KO/J-sign statements in researchers/Connes/23/24/27/40). The extracted (variant, sin², leptoquark) triple is registered as a **new-prediction candidate**, not a consistency PASS.

4-tuple: `(value=variant_id=C-G422D-LR..., scheme=Aydemir-CCS-variant-taxonomy, convention=defect-fingerprint-3axis, L_max=N/A)`. Schema-v2 3-tuple: `sign_verdict=PASS` (both substitution-chain directional predictions verified from data), `magnitude_verdict=INFO` (outcome sits in the pre-registered INFO band: KO-axis indeterminacy), `regime_verdict=VALID` (exact set-membership + exact rationals; no expansion window; all consistency asserts pass). Collapse: magnitude INFO → composite INFO.

Dual-SHA: `audit_sha256=eab1199c543a5e8e8291c7b9c26cc93c8bcbf8f5ab83b6752ef8e14c55f88428`, `content_sha256=202b14c6b9e4db463219cd09b2768424298739078435ba65ea694585a4c1b2ce` (audit closure over script bytes + canonical_constants bytes + sorted pinmap JSON incl. the 7 input-file SHAs and the machinery pinmap hash; content over script bytes only).

**Results**:

*Input fingerprint (S93-W6-1 npz, SHA `11ea23cf...` verified == plan pin).* `axiom4_defect_max = 4.000000` (= 2², (ℍ,ℍ) sector, N3 PROVEN); `axiom4_defect_max_after_inner_fluctuation = 2.100000`; Δ = −1.900000 < 0 and endpoint 2.100000 > 0 → inner fluctuations REDUCE but do NOT close (`order_one_closes = False`; reduction ratio 0.525) — substitution Chain 1 verified with substituted numbers: Δ = 2.100 − 4.000 = −1.900 < 0 ✓, endpoint > 0 ✓ (Sage-QQ: −19/10, 21/10). KO sign triple (J², JD-vs-DJ, Jγ) = (+1, +1, −1) → KO_dim = 6 by the even-dim real-structure table, equal to both the npz `KO_dim` and `EXPECTED_KO_DIM` keys; H_F = 32 per generation, matching the (4,2,1)+(4,1,2) fermion content of the published taxonomy (16 Weyl × 2 under J).

*Axis (i) — defect localization (25×25 `ps_factor_pair_grid`, generators C(1) + M2L(4) + M2R(4) + M4PS(16) = 25).* Grid levels exactly {1.0, 2.0, 4.0}; global max 4.000 = the bare defect. Per-block MAX matrix (rows/cols C, M2L, M2R, M4PS):

```
C    : 1.0  1.0  1.0  2.0
M2L  : 1.0  4.0  1.0  2.0
M2R  : 1.0  1.0  4.0  2.0
M4PS : 1.0  2.0  2.0  4.0
```

Max-level support: BOTH SU(2) diagonals at 4.0 — (M2L,M2L) at generator pairs {2,3} and (M2R,M2R) at {2,3} — PLUS the (M4PS,M4PS) diagonal at 4.0 (generator pairs {4,5},{10,11},{12,13}), with all M4PS cross-blocks elevated at 2.0 and the remaining cross-blocks at the 1.0 floor. The per-block max matrix is **exactly LR-swap symmetric** (M2L↔M2R exchange invariant at tolerance 1e-6). Mean-level diagnostic (NOT gate-bearing): full-grid LR-swap residual max = 1.000; mean(M2L,M4PS) = 1.3750 vs mean(M2R,M4PS) = 1.1875 — a sub-max-level deviation from exact D-symmetry in defect *magnitudes* consistent with the SM-inherited D_F's chirally asymmetric Yukawa content; the max-level *support* (which fixes which scalar classes the quadratic fluctuations generate at leading strength) is D-symmetric.

*Variant scoring (published taxonomy from SHA-pinned sources ONLY: Aydemir PDF `2fb24a7a...` §3.1 Table 1 + Eq. 12 + §3.2–3.3; researchers/Connes/23/24/27/40).* Aydemir Table 1: Model A | G422 | φ(1,2,2), Σ(15,1,1), Δ̃_R(4,1,2) ("composite model" — order-one satisfied; H^{ȧIḃJ} and Σ composite); Model B | G422 | φ(1,2,2), Σ̃(15,2,2), Δ_R(10,1,3), H_R(6,1,1) (fundamental, "unlike model C, is not le[f]t-right symmetric, H^{aIbJ} is turned off"); Model C | G422D | all Eq.-12 fields fundamental incl. Δ_L(10,3,1) + H_L(6,1,1) ("In model C, we have all of these fields"; D = the Z₂ "which keeps the left and the right sectors equivalent"). The published taxonomy occupies THREE of the six candidate cells: A-noLR, B-noLR, C-LR; the cells A-LR, B-LR, C-noLR are not in the published taxonomy. Defect-support semantics per CCS-2013 (Connes/23: quadratic coefficients c_ij vanish iff order-one holds — the persistent quadratic-fluctuation sector is supported exactly where the defect is): (M2L,M2L) max-support ⇔ L-Majorana scalar class H^{aIbJ} = Δ_L+H_L generated; (M2R,M2R) ⇔ R-Majorana class Δ_R+H_R; (M4PS,M4PS)+crosses ⇔ SU(4)-charged 15/10/6 components; LR-symmetric support ⇔ D-symmetric generated sector. Six-cell unique-match table:

| cell | published | axis (i) localization | axis (ii) non-closure | axis (iii) KO | match (i)∧(ii) |
|:-----|:----------|:----------------------|:----------------------|:--------------|:----------------|
| A-noLR | yes | no (predicts zero defect: order-one satisfied) | no (predicts closure) | indeterminate | — |
| A-LR | no | — | — | indeterminate | — |
| B-noLR | yes | no (predicts NO L-Majorana support, LR-asymmetric max; data has (M2L,M2L)=4.0 and LR-symmetric max) | yes | indeterminate | — |
| B-LR | no | — | — | indeterminate | — |
| C-noLR | no | — | — | indeterminate | — |
| **C-LR** | **yes** | **yes (both SU(2) diagonals + M4PS diagonal + both crosses, LR-symmetric)** | **yes** | **indeterminate** | **UNIQUE MATCH** |

`variant_id = C-LR` — **Model C, G422D**, the "most general model" with all scalar fields fundamental. Uniqueness holds on axes (i)∧(ii); axis (iii) cannot be scored against the published taxonomy (0 "KO" hits in the PDF; no J-structure statements per variant in any pinned source) → the pre-registered INFO clause "the variant matches on axes (i)-(ii) but the KO axis is indeterminate from the published taxonomy" fires verbatim. Family-level KO consistency holds (framework KO 6 from (+1,+1,−1); fermion content match 32/gen) — the framework's real structure is *consistent with* the family, just not *discriminated by* the published variant set.

*sin²θ_W at the unification boundary (substitution Chain 2, three exact-rational routes, Sage-QQ cross-checked + in-script `Fraction` reproduction).* Route 1, hypercharge-embedding trace ratio over the variant fermion rep (4,2,1)+(4,1,2) (common to all variants — variants differ in scalar content only): Tr(T₃L²) = (3+1)·2·(1/4) = 2 exactly; Tr(Q²) = 2·[3·(4/9+1/9) + 1] = 16/3 exactly; sin²θ_W = 2/(16/3) = **3/8**. Route 2, coupling matching: 1/g′² = 1/g_R² + (2/3)/g_4² at g_L = g_R = g_4 = g ⇒ g′² = (3/5)g² ⇒ sin²θ_W = (3/5)/(8/5) = **3/8**. Route 3, the framework's canonical NCG normalization g₃² = g₂² = (5/3)g₁² (Aydemir Eq. 6, identical to CC-1996/CCM-2007): sin²θ_W = (3/5)/(1+3/5) = **3/8**. All three routes equal 3/8 EXACTLY; |sin²(M_U) − 3/8| = 0.0e+00 ≤ 1e-12 — the sin² clause is satisfied at the exact-rational level, and a variant preserving the canonical embedding Y = T_{3R} + (B−L)/2 lands on 3/8 by construction (any deviation would have been an embedding change, i.e. a new prediction — not realized). This IS the PS-W3-I operationalization: the PS channel's first numerical content. The M_Z accommodation row (sin2_thetaW_MSbar = 0.23122, S83-W3-G47 / S82-W3-10) is laboratory-IN context ONLY and was NOT scored — no RGE running performed (scale-conflation forbidden per plan audit note (3)).

*S₁(3̄,1,1/3) leptoquark extraction (Model-C content, from the pinned PDF §3.2–3.3).* S₁ = H*₃L ⊂ complexified H_L(6,1,1)₄₂₂, via Eq. 15–16: H^{aIbJ} = Δ_L(10,3,1) + H_L(6,1,1); H_L(6,1,1)₄₂₂ → H₃L(3,1,−1/3)₃₂₁ + H̄₃L(3̄,1,+1/3)₃₂₁. The S₁ at (3̄,1,+1/3) possesses couplings to left-handed fermions while "proton-decay-mediating diquark couplings of this leptoquark are **automatically absent due to the geometric construction**, rather than by ad hoc assumptions" — the NCG-geometric diquark-coupling exclusion. Model-C-specificity: "The S1 leptoquarks in models A and B couple either only to right-handed fermions or only to diquarks; hence, they are not useful for the R_D(*) anomaly" — i.e. the phenomenologically loaded S₁ (LH couplings + proton-decay protection) exists ONLY in the variant the defect fingerprint selected. Note the S₁ host is H_L — a field present only in the G422D (D-symmetric) cell, i.e. the L-Majorana scalar class whose generation the framework's (M2L,M2L) = 4.0 defect support implies.

*Substrate framing (PARTICLE; substrate-first).* The finite algebra A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) IS the substrate's internal gauge content; the order-one condition [[D,a], JbJ⁻¹] = 0 is the NCG axiom whose bare failure at 4.000 (N3, PROVEN) the Wedderburn-Frobenius rescue (§VII.W-3 Q10, **RESCUED** STAGE-3-PERMANENT, S88 W4a-17: A_F = ℂ+ℍ+M₃(ℂ) is the unique 7-axiom algebra under M₃ χ-kill) already resolved at the SM level. The order-one axiom is NOT live-broken — the conversion performed here is RESCUED-axiom → positive-variant-ID, never broken-axiom → feature (both G4 litrev reports flag the source index's "broken order-one" framing as WRONG; this section complies). The S93 SU(4)_PS extension's defect signature is substrate-IS data about which ENLARGED algebra the substrate tolerates; the published PS variants are the laboratory-IN organized taxonomy of the same relaxation (CCS-2013 inner fluctuations without first order). The arrow: D_total defect structure → variant ID (Model C, G422D) → boundary couplings (sin²θ_W(M_U) = 3/8) → laboratory observables (S₁ leptoquark searches; PDG sin²θ_W at M_Z as laboratory-IN shadow, context only).

*Functional/scheme tags (lizzi output standards).* The classification consumes the defect fingerprint (algebra-INVARIANT operator-norm data on the finite triple) and exact rep-theory rationals — FUNCTIONAL-INDEPENDENT (no spectral-functional choice enters: no f(x), no ζ, no heat-kernel moment is numerically consumed). The cited Aydemir/CCS bosonic-action moment structure is tagged a_n^{cutoff} (Tr f(D/Λ) spectral action) as a structural citation only — regulator_pin row appended to the verdict file. Mellin context anchor declared (cited, not consumed): §VII.BE FWD-C4 SU(4)_PS, algebra = rank-4 A_K^PS, poleconv-A-double, (pole_in_s = 6, curvature_grade_n = N/A — substrate-distance family), shell-sum threshold s > 9/2 (d_eff = 9 = 8+1), residue_s6_PS_Linf = 0.000939364.

*Methodology deviations (plan-text drift, substrate-first-canonical-sourcing.md §(ii.B) MANDATORY correction).* The plan-block hypothesis and machinery pin state "KO_dim shifted to 2 (S93-W6-1 npz)" and score track_B on "the KO_dim=2 shift is the axis most likely to break all published variants, which carry KO 6 or 0 real structures". The SHA-pinned npz (the gate's pinned input, SHA verified equal to the plan's own Input-SHA Ledger entry) carries `KO_dim = 6`, `EXPECTED_KO_DIM = 6`, sign triple (+1,+1,−1) — independently recomputed from the sign triple via the even-dim KO table in-script. The runtime value KO_dim = 6 is canonical; the correction is documented in the verdict companion row (`plan_text_drift:` row) and here. Consequence: the track_B rationale (KO mismatch breaks all variants) is DISSOLVED — the framework's real structure is family-consistent with the published CCS construction, which moves the outcome decisively into Reading_1. A second, minor transcription note: the plan writes A_F^PS = ℍ_R + ℍ_L + M₄(ℂ) (Aydemir Eq. 7's three-summand real form); the npz operationalizes the complexified four-summand basis ℂ ⊕ M₂(ℂ)_L ⊕ M₂(ℂ)_R ⊕ M₄(ℂ) with 25 self-adjoint generators (1+4+4+16) — a basis convention of the same extension, not a drift (the ℂ factor is the lepton projection, factor name `C_lepton_proj`).

*Dual-prior resolution.* Pre-registered: track_A (within the CCS/Aydemir PS taxonomy; PASS or INFO) prior 0.7; track_B (outside; FAIL) prior 0.3; discriminator "PASS or INFO → posterior 0.9 Reading_1". Outcome INFO → **posterior 0.9 Reading_1**: the framework's rescued D_total lies WITHIN the published spectral Pati-Salam taxonomy, as Model C (G422D). The audit-trail requirement (which track the verdict feeds) is satisfied in the verdict line's `dual_prior=track_A_posterior_0.9` field.

*Routing (Wave-2 decision point, W2-2 INFO branch).* Per plan: "W2-2 INFO → (variant, sin²) lands as a new-prediction candidate in the WP carry-forward block (no inventory row without the consistency clause)." No falsifier-master-inventory row is routed to mack-cosmic-bridge (that routing is PASS-only). Carry-forward candidate content for the Wave-2 synthesis CF block: **new-prediction candidate** (variant = Model C / G422D; sin²θ_W(M_U) = 3/8 exact; S₁(3̄,1,+1/3) ⊂ H_L(6,1,1) with geometric diquark exclusion), with the natural forward gate being a per-variant KO/J-structure derivation for the CCS Model-C finite triple from the primary CCS-2013/2015 constructions (which would promote the axis-(iii) score from indeterminate to determinate and re-open the PASS pathway), plus the plan's pre-registered FAIL/INFO follow-up surface (§VII.AQ channel scoping retained as-is since the variant ID *succeeded* on (i)∧(ii)).

**Output 4-tuple**: `(value=variant_id=C-G422D-LR_unique_on_axes_i+ii;KO_axis=indeterminate-published_0_KO_hits_in_pinned_sources;KO_dim_npz=6_plan_text_drift_corrected_from_2;sin2_MU=3/8_exact_diff=0.0e+00_tol=1e-12_3_routes;S1=(3bar,1,+1/3)_in_HL(6,1,1)_LH_couplings_diquark_excluded_geometric;closure_pair=(4.000000,2.100000)_not_closed;dual_prior=track_A_posterior_0.9, scheme=Aydemir-CCS-variant-taxonomy, convention=defect-fingerprint-3axis, L_max=N/A)`

---

### §W2-3. S100b-MR-TEXTURE-CLASS (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-MR-TEXTURE-CLASS`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (M_R two-zero texture classification under the discrete CP set)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The S99 B-branch M_R fold energies, PMNS-congruence-rotated over the discrete phase grid {0, π}³, reduce to a two-zero texture matching exactly one Ma/Xu/Zhao Eq.-8 survivor class {A₁, A₂, B₃, B₄, B₆} at ε = 1e-10, phase-consistently with the substrate δ_CP ∈ {0, π} (π/2 stays in the baryogenesis sector — conflation guard).
**Plan reference**: `sessions/session-plan/session-100b-plan-w2.md` §W2-3 (congruence construction, phase grid, NuFit pins, route-(a) scope, sector-conflation guard).

**Verdict**: **FAIL** — the pre-registered Track-B outcome (dual-prior 0.85), realized with an analytic forcing the plan's Chain-1 "structured cancellation" prior did not anticipate in full strength (lemma L2 below). No grid point yields any survivor-class zero pattern at ε = 1e-10; no near-zero pattern appears even at the loosest diagnostic rail ε = 3e-2. Canonical line (emitted via race-safe `emit_verdict`, 6 rows):

```
S100b-MR-TEXTURE-CLASS: FAIL -- value='no_survivor_class_match_at_eps1e-10_on_full_grid_{0,pi}^3_x8; min_z A1=1.000 A2=0.9606 B3=1.000 B4=0.9606 B6=0.9606; structural: all 5 survivors carry a diagonal zero and real-orthogonal congruence forces z_ii >= M1/M3 = 0.8585 (9.9 OOM above eps); offdiag z range [0.00892, 0.0493] (Chain-1 generic scale); d_B = pi/2 maximal (Chain-2 realized); route-(a) scope; vintage-robust(NuFIT-5.2)=True; drift=0.000' scheme=MXZ-Eq8-two-zero convention=UT-MR-U-congruence-PDG-PMNS-NuFit60 L_max=12 audit_sha256=78f88f1375eedddeaecda49eb493f38ad4caf5a9f049d06f9340286338f95263 content_sha256=292b07c3def3771b85c1d3aaaf2512e2827461ec5a6b115bcd8c06db608f59ba schema_version=S84+
```

Schema-v2 3-tuple: `sign_verdict=PASS` (both pre-registered chain directions verified numerically: Chain-1 generic off-diagonal scale ≫ ε; Chain-2 B-class phase distance = π/2 exact), `magnitude_verdict=FAIL` (the membership outcome), `regime_verdict=VALID` (exact finite arithmetic; unitarity max residual 1.11e-16 < 1e-12; all consistency asserts enforced). Composite collapse rule cross-checked in-script: sign=PASS ∧ magnitude=FAIL ∧ regime=VALID → FAIL ✓.

**MCP Pre-Compute Audit**:

1. `search_knowledge("M_R texture zero Ma Xu Zhao two-zero Majorana classification")` → no prior verdict for this gate ID; nearest related entities: S96-MATTER-0NUBB (INFO; Majorana nature via KO-dim-6 Pfaffian on H_K+ — the substrate-IS premise of this gate, not a closure of it), s65 `yukawa_texture` / s47 `texture_corr` provenance rows. NOT PRE-CLOSED.
2. `get_constant("delta_CP_PMNS_substrate")` → 0.0 (S100b; source S99-W3-SEESAW-SUMMNU verdict δ_CP=[0,π]; sector-split per G3 dirac flag) — the set representative; the two-valued set {0, π} is the prediction.
3. `get_constant("phi_CP_K7_transit")` → 1.5707963267948966 = π/2 (S100b; source S98-W3-2-BARYOGEN-UNIQUENESS) — baryogenesis **sector**, guard-excluded from this gate's grid.
4. `get_constant("dm2_21_NuFit")` → 7.49e-5 and `get_constant("dm2_31_NuFit")` → 2.513e-3 — both flagged *no PROVENANCE entry* at query time; this gate's runtime extraction confirmed both equal the NuFit-6.0 PDF as-printed (IC24-with-SK-atm NO column), discharging the plan's vintage-adjudication pin; provenance backfilled in-session via `update_constant` (see hygiene note).
5. `search_knowledge('"M_R" flavor congruence U^T diag heavy Majorana s60')` → no FTS hit; the congruence form is carried by the plan block's s60 pin (`M_R^{flavor} = U^T · M_R^{diag} · U`), implemented verbatim.

**Results**:

*Governing structure and construction.* The M₃(ℂ) factor of A_K is the lepton-number-violating heavy Majorana sector; the B-branch D_K fold energies ARE the heavy spectrum (substrate-IS): M_R = diag(7.46131393e16, 8.01235452e16, 8.69155156e16) GeV = diag(1.00439566, 1.07857332, 1.17000260) M_KK (s99 npz, SHA `48e53bc6…` = plan pin). Route-(a) scope: the s99 construction has m_D = diag(0, 833.83250791, 2074.78472743) GeV — diagonal with m_D[0] = 0 **exactly** (S62 rank-1 Yukawa, m₁ = 0 EXACT) — so the Ma/Xu/Zhao basis condition (m_D diagonal, charged leptons diagonal) is met as-is and the entire PMNS rotation is carried by the heavy sector: M_R^flavor = U^T · diag(M_R) · U (congruence, not conjugation), U = R₂₃(θ₂₃)R₁₃(θ₁₃,δ)R₁₂(θ₁₂)·diag(1, e^{iρ}, e^{iσ}), scanned exhaustively over (δ,ρ,σ) ∈ {0,π}³ (8 points). The m_D-carried-mixing alternative is OUT OF SCOPE here and belongs to S100a-MD-NORMALIZATION (soft cross-cite, no dependency created). All five class patterns were extracted from the SHA-pinned paper-08 PDF **at runtime** (Eq. 8; consistency-checked: 5 classes, each symmetric with exactly 2 independent zeros, pairwise distinct — training-knowledge texture labels never consumed):

| Class | zero positions (1-based, upper triangle) | contains diagonal zero |
|:--|:--|:--|
| A₁ | (2,3), (3,3) | yes — (3,3) |
| A₂ | (2,2), (2,3) | yes — (2,2) |
| B₃ | (1,3), (3,3) | yes — (3,3) |
| B₄ | (1,2), (2,2) | yes — (2,2) |
| B₆ | (1,3), (2,2) | yes — (2,2) |

*Numbers.* Gate-bearing angles AS PRINTED in the SHA-pinned NuFit-6.0 PDF (Table 1, "IC24 with SK atmospheric data", NO best-fit column): sin²θ₁₂ = 0.308, sin²θ₂₃ = 0.470, sin²θ₁₃ = 0.02215. Drift detector vs plan-freeze provisional floats (0.308, 0.02215, 0.470): drift = (0.000, 0.000, 0.000) — no drift, no recall annotation. At every one of the 8 grid points the zero set at ε = 1e-10 is **empty** → match = None everywhere → FAIL. The diagnostic near-zero scan finds no survivor pattern at ε ∈ {1e-6, 1e-3, 3e-2} either. Per-class proximity min_z (min over grid of the max z over the class's required zero positions; 4 sig figs per the Class-8.3 pin; full float64 in the npz):

| | A₁ | A₂ | B₃ | B₄ | B₆ |
|:--|:--|:--|:--|:--|:--|
| min_z (NuFit-6.0, gate-bearing) | 1.000 | 0.9606 | 1.000 | 0.9606 | 0.9606 |
| min_z (NuFIT-5.2 diagnostic re-run) | 1.000 | 0.9748 | 1.000 | 0.9748 | 0.9748 |

Every class sits ≥ 0.96 in normalized modulus where it needs a machine-zero — **9.9–10.0 OOM above the gate threshold** and 1.5 OOM above even the generic-off-diagonal diagnostic rail 3e-2. Off-diagonal entries span z ∈ [0.00892, 0.0493], confirming Chain 1's generic O(3e-2) congruence scale (spread 0.0790 × mixing factors). Unitarity ‖U†U−1‖_max = 1.11e-16; |Im U|_max = 8.82e-17 (U exactly real-orthogonal at all CP-conserving points, to float64); GeV-vs-M_KK z-matrix scale invariance 4.44e-16; npz `delta_CP_allowed` ≡ canonical sector set {0, π} to 0.0e+00 (assert at 1e-12).

*Structural lemmas (why the FAIL is forced, not generic).* Two algebraic facts, both verified numerically in-script, sharpen the pre-registered Chain-1 prior into an impossibility proof:

- **L1 (Majorana-phase transparency of modulus textures)**: with U = R(θ,δ)·P and P diagonal unimodular, (U^T D U)_ij = P_ii (R^T D R)_ij P_jj, so |M_R,ij^flavor| = |(R^T D R)_ij| — independent of (ρ, σ) for ALL values, and independent of the Majorana-matrix convention (PDG diag(1,e^{iρ},e^{iσ}) vs paper-08 diag(e^{iρ},e^{iσ},1) differ by an overall rephasing the modulus kills). Verified: max deviation 0.00e+00 on both axes. The pattern axis of this gate sees only (θ_ij, δ) — the 8-point grid carries exactly 2 distinct z-matrices (visible in the plot), and the ρ,σ axes re-enter only through the class's predicted phase regions.
- **L2 (CP-conserving diagonal-zero obstruction)**: at any (δ,ρ,σ) ∈ {0,π}³, U is real orthogonal, so (M_R^flavor)_ii = Σ_k M_k U_ki² with U_ki² ≥ 0, Σ_k U_ki² = 1 — a **convex combination** of the fold energies, bounded in [M₁, M₃]; with max|M_kl| ≤ M₃ (Cauchy–Schwarz), z_ii ≥ M₁/M₃ = 0.858456 (empirical min z_ii = 0.921527). **Every survivor class carries a diagonal zero** (table above), so no class can match at ANY CP-conserving point for ANY positive heavy spectrum and ANY mixing angles — the FAIL is analytically forced, 9.93 OOM above ε. Diagonal texture zeros require complex cancellation among the U_ki² — which is exactly why the Ma/Xu/Zhao B-classes live at δ ≈ 1.5π, ρ ≈ σ ≈ π/2: the substrate's discrete CP-conserving phase set and the survivor-texture obstruction are the same algebraic fact viewed from two sides.

*Substitution chains (pre-registered, realized).* Chain 1: M_R^flavor = M̄·1 + U^T diag(δM)U with M̄ = 8.05507e16 GeV, spread max|δM|/M̄ = 0.0790 → generic off-diagonals O(3e-2)·max|M_R| — measured z range [0.00892, 0.0493] ✓; ε = 1e-10 cleanly separates exact zeros from generic non-zeros (8 OOM gap) ✓; Step-5 prior (Track B / FAIL) realized ✓. Chain 2: substrate set D = {0, π}; B-class preference δ_B ≈ 1.5π (extracted from the paper's §2 prose at runtime); d(δ_B, D) = min(π/2, π/2) = π/2 — the MAXIMAL possible distance from a CP-conserving point ✓. Realized exactly: min d_B over the grid = 0.500π on every B-class phase axis (δ, ρ, σ), and the A-class Majorana relation ρ ∼ σ ± π/2 also sits exactly π/2 from every grid point (ρ−σ ∈ {0, ±π}); the A-class δ-interval [π, 2π] touches the grid only at its closed boundary. Phase-region containment (clause for the would-be INFO branch): FALSE at the encoded tol = π/4 and for ANY tolerance < π/2 — tolerance-independent, not a band choice. Had a pattern matched, the verdict would have been INFO (phase conflict); no pattern matched, so the verdict is FAIL with the phase conflict documented as the pre-registered B-class disfavor.

*Sector-conflation guard (audit criterion, enforced in code).* The PMNS-sector grid is built from the canonical `delta_CP_PMNS_substrate` sector set {0, π} (asserted ≡ npz `delta_CP_allowed` at 1e-12, dev 0.0). `phi_CP_K7_transit` = π/2 is the **baryogenesis-sector** phase (S98-W3-2 CLOSED-SOURCED-UNIQUE) and was asserted EXCLUDED from the grid (min distance of π/2 to every grid δ, checked in code). The numerical coincidence d(1.5π, {0,π}) = π/2 = phi_CP_K7_transit is precisely the conflation the source index committed ("B-class Majorana phases ~π/2 match phi_CP=π/2") and is NOT imported as a leptonic-phase match: the two phases live in different sectors of the substrate, and this gate's grid never contained π/2. The π/2 appearing in Chain 2 is a phase **distance** on the PMNS circle, not a phase value.

*Diagnostics (not gate-bearing).* (i) Vintage robustness: re-run at the paper-08-stated Table-1 inputs (sin²θ₁₂ = 0.303, sin²θ₂₃ = 0.572, sin²θ₁₃ = 0.02203, Δm²₂₁ = 7.41e-5, Δm²₃ℓ = 2.511e-3 — the NuFIT-5.2-era vintage, extracted from the SHA-pinned PDF) gives the identical class verdict (no match anywhere; min_z table above): **vintage-robust = True**, resolving the litrev H2 vintage flag for this gate. (ii) m₁ = 0 EXACT annotation: m_ν(NuFit-6.0, m₁=0) = (0, 0.00865448, 0.05012983) eV vs npz (0, 0.00867756, 0.04952777) eV — reldiff (+0.2667%, −1.2010%); the npz spectrum is PDG-vintage (7.53e-5, 2.453e-3) — a provenance observation on the s99 record, not a verdict lever. The paper-08 A-classes imply m_lightest ≈ 0.005 eV (near-floor but NOT exactly zero — in tension with m₁ = 0 EXACT), and the B-classes imply m_lightest ≈ 0.1 eV ⟹ Σm_ν ≳ 0.3 eV, excluded by the substrate Σm_ν = 0.0582 eV and by DESI 0.072 eV: both mass axes cohere with the texture-axis FAIL. (iii) Canonical dm² vintage: runtime extraction confirmed `dm2_21_NuFit` = 7.49e-5 and `dm2_31_NuFit` = 2.513e-3 equal the NuFit-6.0 PDF as-printed (asserted at 1e-12).

*Dual-prior resolution and solution-space reading.* Track B (prior 0.85) realized → posterior 0.9 track_B per the pre-registered discriminator. The MXZ discrete-classification corridor is **closed for the route-(a) basis assignment** (all mixing in M_R), and closed with a stronger-than-expected wall: lemma L2 shows the closure is not contingent on the specific fold energies or NuFit angles — ANY positive heavy spectrum under ANY real-orthogonal (CP-conserving) congruence fails every survivor class, because all five survivors demand a diagonal zero and real congruence diagonals are convex combinations of the spectrum. The substrate's two discrete CP predictions (δ_CP ∈ {0,π}, PMNS sector) and its non-membership in the MXZ survivor set are therefore a single joint structural statement: **CP conservation in the leptonic sector ⟺ no two-zero M_R texture of the experimentally-viable classes**. What survives: (a) the m_D-carried-mixing alternative (S100a-MD-NORMALIZATION, soft cite — lemma L2 does not apply there because the texture condition moves off the congruence diagonal structure); (b) textures outside the two-zero survivor family (one-zero, or zero-cofactor conditions imposed directly on M_ν); (c) the paper's own complex-phase regime, which the substrate's discrete CP set excludes by construction. Per the Wave-2→3 decision point, the closest-class diagnostic (min_z table; A₂/B₄/B₆ nearest at 0.9606) feeds the S100a-MD-NORMALIZATION interpretation.

*Substrate framing (PARTICLE).* The arrow runs D_K fold energies → M_R texture → seesaw image → oscillation/0νββ observables. Ma/Xu/Zhao's own thesis ("M_R is more fundamental than M_ν; texture zeros belong on M_R") states the substrate-first direction externally: this gate classified the substrate object directly, and the light data (NuFit angles — laboratory-IN shadows) only filtered it. The result is a clean discrete constraint, not a miss: the substrate's heavy Majorana sector is NOT MXZ-two-zero-classifiable under route-(a), for the same algebraic reason its leptonic CP set is discrete.

*Hygiene notes.* (1) `dm2_21_NuFit` / `dm2_31_NuFit` carried no PROVENANCE dict entries; this gate verified both against the SHA-pinned NuFit-6.0 PDF as-printed and backfilled provenance in-session via `update_constant` (fix-in-session, single-call, no derivation ambiguity). (2) The s99 npz m_ν spectrum is PDG-vintage (7.53e-5, 2.453e-3) rather than NuFit-6.0 — diagnostic-only here (M_R_GeV is the gate input, not m_ν); flagged for the s99 record.

**4-tuple**: `(value=no_survivor_class_match…, scheme=MXZ-Eq8-two-zero, convention=UT-MR-U-congruence-PDG-PMNS-NuFit60, L_max=12)` — L_max inherited verbatim from the s99 npz key.
**Dual-SHA**: `audit_sha256=78f88f1375eedddeaecda49eb493f38ad4caf5a9f049d06f9340286338f95263` (script + canonical_constants + pinmap incl. input-file SHAs and the methodology pinmap: construction, phase grid, ε_texture, nufit_pins, scope_pin), `content_sha256=292b07c3def3771b85c1d3aaaf2512e2827461ec5a6b115bcd8c06db608f59ba` (script bytes).

**Output Artifacts** (closure-verification checklist; each entry verified on disk by content-presence grep):

| Artifact | Path | Exists | must_contain verification |
|:---------|:-----|:-------|:--------------------------|
| script | `computations/session-100b/s100b_w2_3_mr_texture_class.py` (47,546 B) | YES | `grep -E "from canonical_constants import"` → `from canonical_constants import *  # noqa: F401,F403`; `grep -cE "print_verdict_payload"` → 3 |
| data | `computations/session-100b/s100b_w2_3_mr_texture_class.npz` (32,083 B) | YES | non-optional; full float64 z-matrices (8×3×3), min_z, runtime-extracted patterns, region rows, NuFit-6.0/5.2 extraction records, verdict + 3-tuple + dual-SHA |
| plot | `computations/session-100b/s100b_w2_3_mr_texture_class.png` (151,105 B) | YES | non-optional; 8 z-matrix heat maps (lemma-L1 2-distinct-matrix structure visible) + per-class proximity bars vs ε rails + L2 structural-bound line |
| verdict_line | `computations/session-100b/s100b_gate_verdicts.txt` | YES | `grep -E "^S100b-MR-TEXTURE-CLASS:.* audit_sha256=[a-f0-9]{64}"` → canonical FAIL line present; dual-SHA companion row (`audit_sha256_short=78f88f1375eeddde content_sha256_short=292b07c3def3771b`) + schema-v2 3-tuple row + SECTOR-GUARD / STRUCTURAL-L2 / CHAIN-2 companion rows appended via `emit_verdict` (race-safe, 6 rows) |
| wp_section | this section | YES | Status COMPLETED / Verdict FAIL / Output Artifacts / MCP Pre-Compute Audit / sector-guard prose all present |

---

## Wave 2 Synthesis (team-lead)

**Written**: 2026-06-07, session close. All 3 gates landed; verdicts verified on disk against each gate's `output_artifacts` must_contain set.

| Gate | Verdict | Headline value |
|:-----|:--------|:---------------|
| §W2-1 S100b-SYM3-CUBIC-LADDER-P-EXPONENT | **INFO** (Track-B, prior 0.90) | ladder strictly present; p_fit = 15.52 vs [0.8, 1.2]; shape residual 19.85× benchmark (audit `5c06a124046cdcf4…`) |
| §W2-2 S100b-PS-VARIANT-ID | **INFO** | Model C (G422D) unique on axes (i)+(ii); sin²θ_W(M_U) = 3/8 exact ×3 routes; KO axis indeterminate (audit `eab1199c543a5e8e…`) |
| §W2-3 S100b-MR-TEXTURE-CLASS | **FAIL** (Track-B, prior 0.85) | zero-set empty at all 8 CP-conserving points, ε = 1e-10; analytically forced (L2 convexity z_ii ≥ 0.8585) (audit `78f88f1375eedddedee…` → `78f88f1375eeddde…`) |

**Wave reading.** All three gates landed on their dominant pre-registered tracks — the substrate-texture wave is a constraint-mapping sweep, not a surprise generator, and that is its value. W2-1 QUANTIFIES the §VII.BL ε_LX gap for the first time on an external mechanism: the 2026 J₃(O_C) cubic ladder (Teli & Singh) hits the same multiplicity-scalar wall the substrate proved internally, and the bare substrate eigenvalue triple misses the PDG charged-lepton ladder by ×15.52 in scale AND ×19.85 in shape (with the tower NARROWING where the data WIDEN — even the Casimir floor gives W = 0.963 < 1). The ε_LX deformation is now a measured two-axis target, not an assumption; per the decision point this feeds the Q18b ε_LX corridor as a carry-forward CONSTRAINT (planning input, not a compute CF — it has no gate of its own) with the S100a-CONNES-DISTANCE-LADDER rank-9b cluster as SOFT cross-cite. W2-2 pins the framework's Pati-Salam-adjacent classification to a UNIQUE published variant (CCS Model C / G422D) on the defect-localization and closure axes, with sin²θ_W(M_U) = 3/8 exact on three independent routes — the KO-axis indeterminacy is a property of the published taxonomy (no per-variant KO computation exists in the literature), so the PASS pathway re-opens exactly when CF-S101-CCS-MODELC-KO-DERIVATION lands. W2-3's FAIL is the strongest closure of the wave because it is analytically forced: CP conservation in the leptonic sector ⟺ no viable two-zero M_R texture (diagonal entries are convex combinations of fold energies under real-orthogonal congruence, 9.93 OOM above threshold) — the substrate's discrete δ_CP ∈ {0, π} and MXZ non-membership are ONE algebraic fact, robust to any future angle-vintage update. The sector guard held throughout (φ_CP^K7 = π/2 never entered the leptonic grid).

**Decision-point evaluation** (plan §"Wave 2 → Wave 3 Decision Point"): W2-1=INFO (expected) → Q18b corridor feed + rank-9b SOFT cross-cite recorded here (the W2-1 PASS escalation path did NOT fire — no Q1 tension). W2-2=INFO → new-prediction candidate lands in the CF block below; NO falsifier-inventory row (that routing is PASS-only; correctly not exercised). W2-3=FAIL (expected) → MXZ corridor closed route-(a); closest-class diagnostic (B4/A2/B6 at min_z = 0.96) feeds S100a-MD-NORMALIZATION's interpretation as SOFT cite; m_D-carried mixing survives as the open route.

**Carry-Forward Computations (MATH ONLY — propagate to S101)**

### CF-S101-CCS-MODELC-KO-DERIVATION — per-variant KO/J-structure derivation for the CCS Model-C finite triple

Lifted from §W2-2 routing paragraph (W2-2 INFO branch): **What** — derive the KO-dimension and real-structure (J, ε, ε′, ε″) signs for the CCS Model-C (G422D) finite spectral triple from the primary CCS-2013/2015 constructions, promoting the axis-(iii) score from indeterminate to determinate (KO_dim = 6 match/mismatch vs the substrate's npz-pinned KO_dim = 6). **Inputs** — `s100b_w2_2_ps_variant_id.npz` (defect fingerprint + KO sign triple (+1,+1,−1)), CCS-2013/2015 primary constructions (paper pins in plan §W2-2 input_files), `permanent-results-registry.md` KO-dim=6 PROVEN record. **Gate** — PASS iff the derived Model-C KO-dim and sign triple MATCH the substrate's (KO_dim = 6, (+1,+1,−1)) → re-opens the W2-2 PASS pathway (unique-variant + KO-consistency clause); FAIL iff derivation yields a determinate mismatch → Model-C identification demoted to axes-(i,ii)-only. **Effort** — 1 solo-theorist derivation gate (lizzi or connes), ≤ half a session; no new diagonalization.

*(Constraint-feed, not a CF: the W2-1 (p, W_ladder) = (15.52, 0.1214) two-axis gap is handed to the Q18b ε_LX corridor as a planning constraint; cross-cite S100a-CONNES-DISTANCE-LADDER rank-9b at next planning. No gate of its own → fails the 4-field test by design.)*

### CF-W2-1 (PS-RGE-MODELC-SIN2-MZ) — Model-C RGE run sin²θ_W(M_U) = 3/8 → M_Z *(investigation append, 2026-06-07, /rclab-investigate consolidator; Q-other solo compute, SEQUENCED)*

The plan's fb_pair pre-named "future PS-RGE gates if a variant is identified"; the trigger fired (W2-2 INFO: Model C / G422D identified). **What** — RGE running of the G422D Model-C couplings from the unification boundary sin²θ_W(M_U) = 3/8 down to M_Z with the Model-C scalar content (W2-2 npz) in the beta functions; compare against PDG sin²θ_W(M_Z) = 0.23121 ± 0.00004 AND against the framework's existing accommodation row (0.23480 @ fitted μ_BC = 188.44 GeV; S83-W3-G47 / S82-W3-10) — the comparison the W2-2 plan correctly FORBADE in-gate as scale-conflation becomes the legitimate OBJECT of this successor. **Inputs** — `s100b_w2_2_ps_variant_id.npz` (variant ID, scalar content, sin² rationals), Aydemir PDF (SHA `2fb24a7a…`, carries the published intermediate-scale RGE analysis), `sin2_thetaW_MSbar` canonical. **Gate** — pre-register |sin²θ_W(M_Z)_ModelC − 0.23121| band at S101 plan-freeze (or INFO-by-design two-route comparison vs the accommodation row). **Effort** — 1 gate, 1 agent. **Depends on** — `CF-S101-CCS-MODELC-KO-DERIVATION` outcome (a determinate KO mismatch demotes Model-C to axes-(i,ii)-only and this gate re-scopes or drops) — sequence AFTER it at S101 planning.

### CF-W2-2 (MR-TEXTURE-ROUTE-B) — two-zero/one-zero M_R texture re-classification under m_D-carried mixing *(investigation append, 2026-06-07, /rclab-investigate consolidator; Q-other conditional compute — trigger NOT yet fired)*

W2-3's route-(a) closure (lemma L2, diagonal-convexity) does NOT apply when mixing moves into m_D — route-(b) is genuinely open. **What** — re-run the MXZ-class membership test with mixing assigned to m_D per a substrate-pinned non-diagonal m_D construction. **Inputs** — a non-diagonal substrate-pinned m_D (NOT YET LANDED — see conditionality), `s100b_w2_3_mr_texture_class.npz` (closest-class diagnostic min_z table A₂/B₄/B₆ at min_z = 0.9606; L1/L2 lemma machinery), paper-08 PDF (SHA `3229fffb…`). **Gate** — same set-membership operator as W2-3 with the route-(b) construction pinned at plan-freeze. **Effort** — 1 gate, 1 agent. **Conditionality (verified at consolidation, 2026-06-07)** — `S100a-MD-NORMALIZATION` landed INFO (audit `4f92a5513ad69b07`): both tested maps were DIAGONAL (MAP-A eigenvalue-prop / MAP-B Casimir-graded, both excluded at Y_ref = E₁); Dirac-scale anchor irreducibly EXTERNAL; **no non-diagonal m_D was landed** → the route-(b) trigger has NOT fired. This CF stays CONDITIONAL (not void — a non-diagonal m_D was not excluded, merely not constructed); the natural upstream producer is the S100a W5 S1-1 review of the D_F-texture wall (surviving-map-class output, reading (ii)). If S101 planning finds no non-diagonal m_D construction on the queue, hold this CF rather than dropping it — route-(a) closure is final ONLY for the all-mixing-in-M_R basis.

### CF-W2-3 (Z3-PHASE-REPHASING-INVARIANCE) — is the charged-lepton Z₃ phase content rephasing-removable, or does it feed PMNS δ_CP? *(investigation append, 2026-06-07, orchestrator per the consolidator's cross-session adjudication #5 residual; Q-other forward derivation — consistency certification, no landed contradiction)*

The schedule's cross-session adjudication #5 settled arg(w) vs δ_CP as DIFFERENT MATRICES (arg(w) ∈ {π, ±2π/3} lives on the charged-lepton Dirac Yukawa off-diagonal — second-Z₃ on the BDI fund↔antifund s-LINEAR channel, S100a W2-2, audit `871573da729c5972`; δ_CP ∈ {0, π} is the PMNS Dirac-phase restriction, S99-W3-SEESAW-SUMMNU, canonical `delta_CP_PMNS_substrate`) — but left one RESIDUAL forward derivation not landed anywhere. **What** — rephasing-invariance analysis: whether the Z₃ phase content of the charged-lepton texture (Weingarten-exact arg(w) values) is removable by field rephasing or propagates into PMNS δ_CP through the lepton diagonalization U_PMNS = U_ℓ† U_ν; certifies consistency with the substrate-forced δ_CP ∈ {0, π} OR escalates to a genuine S100a↔S100b cross-session contradiction (the one outcome that would re-open adjudication #5 as a workshop). **Inputs** — S100a W2-2 texture [[d, w],[w*, d]] with |w| = 1/√6 EXACT + arg(w) ∈ {π, ±2π/3} (`s100a_gate_verdicts.txt:36-40`); `delta_CP_PMNS_substrate` canonical; S100b W2-3 CP-conserving-grid scoping (`s100b_w2_3_mr_texture_class.npz`, sector guard φ_CP^K7 = π/2 never entered); standard rephasing-invariant (Jarlskog-class) machinery. **Gate** — pre-register at S101 plan-freeze: PASS iff the Z₃ phases are rephasing-removable (δ_CP ∈ {0, π} consistency certified); FAIL iff a non-removable phase forces δ_CP ∉ {0, π} (escalates to cross-session contradiction workshop); INFO if removability is basis-conditional (scope clause emitted). **Effort** — 1 solo-theorist derivation gate, ≤ half a session; no diagonalization compute beyond 3×3 algebra.

**Effected In-Session (NON-MATH — completed before STOP)**

- [x] `dm2_21_NuFit` + `dm2_31_NuFit` PROVENANCE backfill (values unchanged, vintage asserted at 1e-12 vs SHA-pinned NuFit-6.0 PDF) — dirac-antimatter-theorist in-gate — `computations/_shared/canonical_constants.py:1820,1823` (values at 2869-2870) — gate `S100b-MR-TEXTURE-CLASS`
- [x] `m_tau` + `m_mu` PROVENANCE backfill (flagged missing by W2-1; values unchanged; formalizes the constants' own inline comments at lines 497/2194) — orchestrator-direct at session close — `computations/_shared/canonical_constants.py` SECTION E backfill block after `dm2_31_NuFit`; module re-import verified clean — flagged by gate `S100b-SYM3-CUBIC-LADDER-P-EXPONENT`
- [x] Plan-text KO_dim drift (plan pinned KO_dim=2; SHA-pinned npz ground truth KO_dim=6) corrected at runtime per `substrate-first-canonical-sourcing.md §(ii.B)` — lizzi-spectral-functional-theorist in-gate — `plan_text_drift` companion row in `s100b_gate_verdicts.txt` + WP §W2-2 Methodology deviations — no plan edit (correct protocol)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-07 | §VII.BL ε_LX deformation magnitude | unquantified (obstruction proven, gap unmeasured) | QUANTIFIED two-axis on external J₃(O_C) mechanism: scale ×15.52, shape ×19.85 | W2-1 INFO (Track-B expected) |
| 2026-06-07 | Pati-Salam variant identification (§VII.AQ-adjacent) | open across CCS/Aydemir 6-cell taxonomy | Model C (G422D) UNIQUE on (i) defect-localization + (ii) closure; KO axis pending CF-S101-CCS-MODELC-KO-DERIVATION | W2-2 INFO |
| 2026-06-07 | MXZ two-zero M_R textures, route-(a) | candidate corridor | CLOSED — analytically forced for ANY positive heavy spectrum + angles at CP-conserving points; m_D-carried mixing is the surviving route | W2-3 FAIL (L1+L2 lemmas in-script) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| W2-1 | s100b_w2_1_sym3_cubic_ladder_p_exponent.py | ✓ (44 keys) | ✓ | — | 37.4 KB / 17.1 KB / 134 KB |
| W2-2 | s100b_w2_2_ps_variant_id.py | ✓ | ✓ | — | 41.3 KB / 52.1 KB / 120 KB |
| W2-3 | s100b_w2_3_mr_texture_class.py | ✓ | ✓ | — | 47.5 KB / 32.1 KB / 151 KB |
