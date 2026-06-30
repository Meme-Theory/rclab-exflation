# Session 100a Wave 5 — Neutrino Sector (Results Working Paper)

**Session**: 100 | **Wave**: 5 | **Plan**: session-100a-plan-w5.md | **Theme**: Neutrino sector — substrate-forward seesaw normalization (zero-free-parameter Σmν uniqueness test) + KO-dim-6 Pfaffian Majorana 0νββ observable leg (D5 Majorana-vs-Dirac discriminator).

## Gate Sections

### §W5-1. S100a-MD-NORMALIZATION (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S100a-MD-NORMALIZATION`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (substrate-forward Dirac-Yukawa map uniqueness; type-I seesaw Σmν re-gate)
**Agent**: `neutrino-detection-specialist` (cross-axis: connes-ncg-theorist for the Dirac-side D_F texture)
**Hypothesis**: The D_K bottom light-triple (~0.82–0.87 M_KK E1/E2/E3) either UNIQUELY pins the Dirac Yukawas Y_i — making Σmν a genuine zero-free-parameter prediction reproducing 0.0582053272 eV — or admits a residual Dirac-scale normalization, confirming the S99 track_B oscillation-anchored caveat as irreducible.
**Plan reference**: `sessions/session-plan/session-100a-plan-w5.md` §W5-1 (machinery pin, thresholds, MAP-A/MAP-B uniqueness test, substitution chain source).

**Output Artifacts**:

| Artifact | Path | must_contain verification |
|:---------|:-----|:--------------------------|
| script | `computations/session-100a/s100a_md_normalization.py` | EXISTS; `from canonical_constants import` ✓ (line 103); `print_verdict_payload` ✓ (def + call) |
| data | `computations/session-100a/s100a_md_normalization.npz` | EXISTS (full-float64 Sigma_mnu_MAP_A_eV / Sigma_mnu_MAP_B_eV / uniq_ratio / all cross-checks / dual-SHA / verdict 3-tuple) |
| plot | `computations/session-100a/s100a_md_normalization.png` | EXISTS (3-panel: Yukawa shapes vs required; Σmν per map vs reproduce band + DESI; per-generation rescale non-constancy) |
| verdict_line | `computations/session-100a/s100a_gate_verdicts.txt` | `^S100a-MD-NORMALIZATION:.* audit_sha256=[a-f0-9]{64}` ✓ via `emit_verdict` MCP (race-safe, 6 rows: canonical + dual-SHA companion + schema-v2 [SIGN] 3-tuple + 3 detail rows) |
| wp_section | this section | Status COMPLETED ✓ / Verdict ✓ / Output Artifacts ✓ / MCP Pre-Compute Audit ✓ |

**MCP Pre-Compute Audit**:

Queries executed BEFORE computing (per plan §W5-1 MCP block); gate NOT pre-closed — `S100a-MD-NORMALIZATION` had no prior evaluation in the knowledge graph:

1. `get_constant('Sigma_mnu_FW')` → `0.0582053272` (S99, source `s99_w3_seesaw_summnu.npz`, gate `S99-W3-SEESAW-SUMMNU`, not superseded) — the reproduce-band target.
2. `get_constant('M_KK')` → `7.428660036284456e16` GeV (S42 `CONST-FREEZE-42`, alias of `M_KK_gravity`, spectral-zeta route) — the M_R scale.
3. `get_constant('Sigma_mnu_bound_DESI_2024')` → `0.072` eV (DESI 2024 arXiv:2404.03002, DR1 BAO, LCDM + Σmν, 95% CL) — the laboratory-IN falsifier bound.
4. `trace_entity('seesaw')` → `S99-W3-SEESAW-SUMMNU` PASS (Σ=0.05821 eV < 0.072; NO; track_B HONEST-SCOPE caveat — the baseline this gate re-tests); `S96-MATTER-SEESAW-D5` INFO (2.2016, seesaw-vs-direct reconciliation); `S96-MATTER-R-HIERARCHY` FAIL (9.86183067373777, direct-spacing rank-1 wall); Connes 2006 theorem (NCG SM: Yukawas + M_R order-one FREE — the external-anchor precedent this gate tries to remove). No closure covering the substrate-FORWARD Y_i question.
5. `search_knowledge('S96-MATTER-R-HIERARCHY bottom-triple')` → S96 gate FAIL `value=9.86183067373777`, `scheme=direct-DK-eigenvalue-spacing-no-seesaw`, provenance `s96_matter_r_hierarchy.py` — pins the bottom-triple identity + the R_direct cross-check anchor used below.

**Verdict**: **INFO** — composite per the schema-v2 collapse rule from the [SIGN] 3-tuple (`sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=VALID`). The bottom-triple → Y_i map is **NON-UNIQUE**: registry state `residual-Dirac-scale-normalization-IRREDUCIBLE` (pre-registered INFO_meaning, plan §W5-1). The S99 track_B caveat is confirmed **structurally irreducible**.

**Results**:

4-tuple: `(value='SigmaA=5.2917e-04eV;SigmaB=7.8012e-04eV;uniq_ratio=0.4742>0.05_NONUNIQUE;reproduce_reldiff_A=0.9909;rescale_Yref_A=10.488_B=8.638;shape_Y3overY2_req=2.4883_vs_A=1.0444_B=1.5000;DESI_ok_both;map_unique=False;residual-Dirac-scale-normalization-IRREDUCIBLE;trackB_0.9', scheme=type-I-seesaw-substrate-forward-Yi-from-DK-bottom-triple, convention=ABSOLUTE, L_max=12)`

Dual-SHA: `audit_sha256=4f92a5513ad69b07c0ae4ee8d5ed3ffe263aadfd67f19c6634d9d2a1be4d0c3f`, `content_sha256=596ff203a03763094febea8ae1960e1171971d6ca5bc6128a11ccd841befcc8e`.

**(1) Bottom light-triple (tower-resolved, L12 block-diagonal master cache; NO re-diagonalization).** The three lowest Peter-Weyl towers' bottom |λ| at τ_fold = 0.19:

| gen | E_i [M_KK] | tower (p,q) | triality | C₂(p,q) |
|:----|:-----------|:------------|:---------|:--------|
| 1 | 0.81974111 | (0,0) trivial | 0 | 0 |
| 2 | 0.83589351 | (1,0)⊕(0,1) fundamental | 1 ⊕ 2 | 4/3 |
| 3 | 0.87297503 | (1,1) adjoint | 0 | 3 |

Conjugate-pair degeneracy (1,0)/(0,1): split 4.4e-16 (exact). Triple identity cross-checks: (a) conv-A spacings reproduce the S96 R_direct: 9.86183067374 vs S96 verdict 9.86183067373777, reldiff **1.0e-13** — same triple the S96 rank-1 wall was read from; (b) all three tower bottoms present in the `s55_bogoliubov_992.npz` ω_f post-transit spectrum at reldiff [0, 0, 0] (exact; alternate-source confirmation).

**(2) The two pre-registered substrate-forward maps** (shared substrate-natural scale Y_ref = E₁ = 0.8197411121, the raw dimensionless bottom eigenvalue — zero external input; Y₁ = 0 from rank-deficiency, PROVEN normal ordering):

| map | Y₂ | Y₃ | shape Y₃/Y₂ | m_D [GeV] | m_ν [eV] | Σmν [eV] |
|:----|:---|:---|:------------|:----------|:---------|:---------|
| MAP-A (Y_i = E_i) | 0.83589351 | 0.87297503 | 1.044362 | [0, 145.402, 151.852] | [0, 2.6387e-4, 2.6531e-4] | **5.2917079242e-04** |
| MAP-B (Y_i = E₁·√(C₂ⁱ/C₂⁽²⁾)) | 0.81974111 | 1.22961167 | 1.500000 (=3/2 exact) | [0, 142.593, 213.889] | [0, 2.5377e-4, 5.2636e-4] | **7.8012116406e-04** |

Structural sub-result (diagnostic, not a verdict driver): MAP-B's Casimir grading yields Y₁ = 0 **EXACTLY** (C₂(0,0) = 0) — the rank-deficient lightest generation (m₁ = 0, normal ordering) *emerges* from the grading instead of being imposed.

**(3) Pre-registered gate clauses** (M_R = B-branch D_K fold energies [1.00439566, 1.07857332, 1.17000260] M_KK from the pinned S99 baseline npz):

| clause | operator | result | met? |
|:-------|:---------|:-------|:-----|
| PRIMARY (DESI) | Σ < 0.072 eV | A: 5.29e-4 ✓, B: 7.80e-4 ✓ | YES (both) |
| JOINT (reproduce) | \|Σ − 0.0582053272\|/0.0582053272 ≤ 0.05 | A: 0.990909, B: 0.986597 | **NO** (both ~99% off; ≈100× below band) |
| UNIQUENESS | \|Σ_A − Σ_B\|/Σ_A ≤ 0.05 | **0.474233** | **NO** (9.5× over tol) |
| FAIL ceiling | Σ > 0.12 eV (overshoot) | max Σ = 7.8e-4 ≪ 0.12 | not triggered |

`map_unique = False` (per plan method (2): maps must agree AND the parameter-free evaluation must land in the band; neither holds) → **INFO**.

**(4) Residual-freedom quantification (the track_B content).** Required overall Y_ref rescale to reach Σ = 0.0582 eV: MAP-A ×10.488, MAP-B ×8.638 (Σ ∝ Y_ref²; factors 110.0 / 74.6 in Σ). But the residual freedom is NOT even 1-parameter: the per-generation required rescale Y_i^{S99}/Y_i^{map} is **non-constant** — MAP-A [5.735, 13.663], MAP-B [5.848, 9.700] — so no single Dirac scale reproduces both m₂ AND m₃. The oscillation-required Yukawa shape is Y₃/Y₂ = 2.4883 (= √(m₃M₃/m₂M₂)); MAP-A's eigenvalue shape gives 1.0444, MAP-B's √C₂ shape gives 1.5000 exactly. (Post-hoc diagnostic observation, NOT a gate input: even a linear-C₂ grading would give 9/4 = 2.25, still 9.6% short in Y — no low-order Casimir grading of the three lowest towers reproduces 2.4883.) The bottom-triple fails on BOTH axes: absolute scale (this gate) and shape (consistent with the S96-MATTER-R-HIERARCHY rank-1 wall, R_direct = 9.86 vs measured 33.8).

**(5) [SIGN] substitution chain (with substituted numbers; direction pre-registered in plan §W5-1):**

```
Step 1: m_D,i = Y_i·v_ew/√2  [v_ew = 246 GeV canonical];  M_i = M_R,i·M_KK  [M_KK = 7.428660036284456e16 GeV]
        M_GeV = [7.4613e16, 8.0124e16, 8.6916e16]
Step 2: d m_ν,i/d M_i = d/dM_i [m_D,i²/M_i] = m_D,i²·(−M_i⁻²)
Step 3: = −m_D,i²/M_i²;  m_D,i ≥ 0 ([J,D_K]=0 ⇒ M_R real), M_i > 0 ⇒ strictly negative for i=2,3
        MAP-A: [−3.293e-30, −3.052e-30];  MAP-B: [−3.167e-30, −6.056e-30]  (all < 0 ✓)
Step 4: heavier M_R ⇒ lighter m_ν (suppression); m_D/M_R = 2.46e-15 (deep seesaw, regime VALID);
        δ_A = Σ_A − 0.072 = −7.147e-2 < 0 ✓;  δ_B = −7.122e-2 < 0 ✓
Conclusion: sign_verdict = PASS (suppression direction identical to S99); the substrate-forward
        Y_i change only the ABSOLUTE Σ — which is exactly what the uniqueness test interrogates.
```

**(6) Cross-checks (all pass):**
- **CC0 (baseline re-derivation)**: this script's seesaw pipeline with the S99 back-solved Y = [0, 4.79356602, 11.92759634] reproduces Σ = 0.0582053272 eV — reldiff 0.0 vs the S99 npz, 8.27e-10 vs the canonical `Sigma_mnu_FW` (machinery validated before the forward maps run through it).
- **CC-R (triple identity)**: R_direct from the cache-read triple = 9.86183067374 vs S96 verdict 9.86183067373777 (reldiff 1.0e-13 < 1e-6).
- **CC-s55 (alternate source)**: all three tower bottoms present in ω_f at reldiff [0, 0, 0].
- **CC-MR (spectral coincidence)**: M_R B-branch fold energies vs L12 cache union-of-90-sectors: reldiff [0.0177, 1.3e-4, 5.0e-3], maxrel **0.0177 < tol_MR = 0.02** (matches the S99 value 0.0177).
- **CC-S60 (texture)**: M_R fold-energy triple confirmed present in `s60_lepto_cp_log.txt`.

**(7) track_A/track_B posterior reallocation (pre-registered discriminator, plan §W5-1 dual_prior):** outcome = INFO (map non-unique) → **reallocate 0.9 to track_B** (prior was track_A 0.35 / track_B 0.65). The S99 HONEST-SCOPE caveat is **confirmed PERMANENT**: the Dirac-scale normalization is structurally irreducible on the bottom-triple route; the absolute Σmν is oscillation-anchored, NOT substrate-forced. The dual_prior's track_B rationale (the S96 rank-1 wall implies the bottom-triple spacing cannot carry the Yukawa hierarchy) is borne out quantitatively: the spacing carries neither the hierarchy (shape 1.04–1.5 vs required 2.49) nor the scale (×8.6–10.5 in Y_ref).

**Assessment (substrate framing — PARTICLE).** The explanation flows D_K eigenvalues (bottom light-triple, towers (0,0)/(1,0)⊕(0,1)/(1,1)) → substrate-forward Yukawa map → m_D = Y·v_ew/√2 → type-I seesaw with M_R = B-branch D_K fold energies (Majorana scale INTERNAL to the spectrum) → Σmν vs DESI; never inverted. What this INFO constrains: the FIRST arrow (eigenvalue → Yukawa) is NOT a unique substrate map at the two pre-registered reductions — the solution space for a zero-free-parameter Σmν now excludes both the eigenvalue-proportional and the √C₂-graded readings of the bottom triple at the substrate-natural Y_ref = E₁ normalization. What survives unchanged (PASS-grade substrate-FIRST content from S99): M_R = D_K eigenvalues (coincidence 1.77% < 2%), the seesaw structure, the suppression direction (sign=PASS here), and normal ordering (m₁ = 0 — now with the MAP-B observation that the Casimir grading produces it EXACTLY). The Dirac-side D_F texture reading (whether ANY representation-theoretic structure of the finite Dirac operator forces a bottom-triple → Y_i map with the required shape 2.4883) is the cross-axis question owned by `connes-ncg-theorist` (derivation-author tag, plan §"Cross-axis dispatch note"); the quantitative wall this gate erects for that reading: the map must produce Y₃/Y₂ = 2.4883 AND an overall scale ~10× above E₁ — neither available from the three lowest towers' eigenvalues or low-order Casimirs.

**Session-close routing (plan §"Wave 5 → Wave 6 Decision Point", INFO branch):** capstone §7.3 item-(4) records the Dirac-scale anchor as irreducibly external; NO canonical-constant value change (`Sigma_mnu_FW = 0.0582053272` unchanged; its provenance note gains the uniqueness-INFO finding). Cross-gate (within wave): §W5-2's m_ββ absolute scale inherits the residual-Dirac-scale caveat (per the soft within-wave ordering note).

**Process note (fix-in-session):** a pre-existing `SyntaxError` in `computations/_shared/canonical_constants.py` line 1800 (PROVENANCE `"sigma_over_m"` entry, unescaped nested double quotes) blocked ALL S34+ script imports; fixed in-session (inner quotes → single quotes, content verbatim) before the gate run. The gate's `audit_sha256` pins the fixed file.

---

### §W5-2. S100a-D5-0NUBB-MAJORANA (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S100a-D5-0NUBB-MAJORANA`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (KO-dim-6 Pfaffian Majorana texture → 0νββ effective mass m_ββ vs experimental bounds)
**Agent**: `neutrino-detection-specialist` (cross-axis: dirac-antimatter-theorist for the KO-dim-6 Pfaffian Majorana determination)
**Hypothesis**: The substrate KO-dim-6 Pfaffian Majorana texture (M_3(ℂ) singlet) with the S99 normal-ordering masses [0, 0.0086776, 0.0495278] eV and δ_CP ∈ {0,π} yields m_ββ below KamLAND-Zen and inside the NO funnel (consistent Majorana, LEGEND-1000 falsifiable), supplying the OBSERVABLE leg of the D5 discriminator only.
**Plan reference**: `sessions/session-plan/session-100a-plan-w5.md` §W5-2 (S96-MATTER-0NUBB machinery re-use, S99 Route-A masses, NuFit-6.0 PMNS pins, substitution chain source).

**Output Artifacts**:

| Artifact | Path | must_contain verification |
|:---------|:-----|:--------------------------|
| script | `computations/session-100a/s100a_d5_0nubb_majorana.py` | EXISTS; `from canonical_constants import` ✓ (star import + explicit names); `print_verdict_payload` ✓ (def + call) |
| data | `computations/session-100a/s100a_d5_0nubb_majorana.npz` | EXISTS (full-float64 m_ββ central/band/240×40 grid, U_ei², m_i, bounds, funnel pins, full PART-1 determination + all cross-checks, dual-SHA, verdict) |
| plot | `computations/session-100a/s100a_d5_0nubb_majorana.png` | EXISTS (2-panel: Majorana-phase band vs bound ladder + funnel; KO-dim-6 axiom residuals re-run vs S96 stored) |
| verdict_line | `computations/session-100a/s100a_gate_verdicts.txt` | `^S100a-D5-0NUBB-MAJORANA:.* audit_sha256=[a-f0-9]{64}` ✓ via `emit_verdict` MCP (race-safe; 5 rows: canonical + dual-SHA companion + scope-pin + scale-provenance + diagnostics rows; NO [SIGN] 3-tuple — [VERIFY] trigger) |
| wp_section | this section | Status COMPLETED ✓ / Verdict ✓ / Output Artifacts ✓ / MCP Pre-Compute Audit ✓ |

Path note: the plan's `method.producing_script` field reads `computations/_shared/…` while the binding `output_artifacts:` block (and the dispatch override) pin `computations/session-100a/…` — landed at the output_artifacts path.

**MCP Pre-Compute Audit**:

Queries executed BEFORE writing the script (per plan §W5-2 MCP block); gate NOT pre-closed — no prior evaluation of m_ββ with the S99 hierarchical masses exists in the knowledge graph:

1. `get_constant('m_betabeta_KamLANDZen')` → `0.122` eV (KamLAND-Zen 800 upper limit, loose-NME end; canonical comment notes tight end ~0.028 eV) — the current-bound gate threshold.
2. `get_constant('m_betabeta_LEGEND200_reach')` → `0.075` eV (LEGEND-200 design sensitivity, loose-NME end).
3. `get_constant('m_betabeta_nextgen_reach')` → `0.010` eV (LEGEND-1000/nEXO target reach floor; ~6–20 meV design band).
4. `query_entity('gates','S96-MATTER-0NUBB')` → INFO, `value='MAJORANA;…'`, scheme `KO-dim-6-Pfaffian-Majorana-on-H_K+`, L_max=12 — the determination machinery this gate re-uses. Its INFO was the W4-2 framework-PMNS prereq caveat on the m_ββ half (the half this gate replaces with Route-A), NOT a determination weakness.
5. `trace_entity('KO-dim-6 Majorana')` → no indexed entity under that exact phrase (the machinery lives under the S96 gate + `matter_0nubb` provenance entities).
6. `list_constants('sin2_theta')` → only `sin2_thetaW_MSbar` (0.23122) and `sin2_thetaW_fold` (0.583853) — the PMNS `sin2_theta12/13_NuFit` pins are ABSENT from canonical_constants → pinned in-script as `# (local)` laboratory-IN values with the NuFit-6.0 source comment, per the plan Input-SHA-Ledger note (Source-Reconciliation class (f) does not fire).
7. (bonus) `search_knowledge('0nubb m_bb effective Majorana mass funnel')` → plan-W5 equation entities + the S96 gate + `matter_0nubb` provenance only — confirms NOT PRE-CLOSED.

**Verdict**: **PASS** — m_ββ^{central} = 3.695 meV < 122 meV (KamLAND-Zen) AND inside the pre-registered NO funnel [1.5, 4.5] meV (plan §W5-2 strict_PASS_boundary; both conjuncts met). Registry state: `MAJORANA-admitted-m_bb-funnel`. The W5-1 track_B residual-Dirac-scale caveat is INHERITED IN FRAMING (encoded in the verdict value string + the `m_bb_FW` canonical provenance), not verdict-downgrading — see the verdict-reading note in Results (7).

**Results**:

**(0) SCOPE PIN (load-bearing, per plan + dispatch).** This gate supplies the **OBSERVABLE leg ONLY** of the D5 Majorana-vs-Dirac discriminator. Capstone §7.3 D5 STATUS stays **`unreconciled`** regardless of this PASS; the §0 "no-seesaw" vs Majorana-M_R prose adjudication is a **workshop question** (`Investigating-Workshops.md §Q1`, routed via `/rclab-investigate`), NOT this gate's output; the m_ββ falsifier-master-inventory row routes to **`mack-cosmic-bridge` as SOLE WRITER** at session close (`feedback_mack-bridge-role.md`). Per the plan's cross-pillar-bridge scope declaration, this is a falsifier-inventory LABORATORY FALSIFIER-ROW LANDING, not a §VII bridge entry — the 5-anatomy block is not required at this landing.

4-tuple: `(value='MAJORANA-admitted-m_bb-funnel;m_bb_central=3.695meV;band=[1.516,3.695]meV;KamLAND-Zen=122meV(x33.0-below);LEGEND200=75meV(x20.3-below);nextgen-floor=10meV(x2.7-below;detection-above-funnel-falsifies);in-NO-funnel[1.5,4.5]meV=True;deltaCP{0,pi}-degenerate;m_i=S99-osc-anchored-trackB-residual-Dirac-scale-caveat(W5-1-INFO);scope=observable-leg-only-D5-prose-workshop-deferred', scheme=KO-dim-6-Pfaffian-Majorana-on-H_K+_S99-oscillation-anchored-m_i-RouteA, convention=ABSOLUTE, L_max=12)`

Dual-SHA: `audit_sha256=a2d29b975d8cb170dc561a35034a24c8f8d3900358ae2e0c84465e499b34bbc6`, `content_sha256=9ddd1ba53d9c4f2fc4a1aef8f639d678e981e602f7c240cb7afa09e654966945`.

**(1) PART 1 — KO-dim-6 Pfaffian Majorana determination (S96-MATTER-0NUBB machinery re-run; FULL physical Cl(8) build, not SCHEMATIC).** The determination is DEFINITE and re-confirmed bit-exactly:

| quantity | re-run value | S96 stored | match |
|:---------|:-------------|:-----------|:------|
| KO-dim-6 axioms (J²=+1, JD=DJ, Jg=−gJ, {g32,D32}=0, antilinear-Tsym) | all **0.0** exact | all 0.0 | ✓ |
| linear-[C2,D_F] pitfall contrast (NOT a signal) | 0.663480 | 0.663480 | ✓ (reldiff 0) |
| (1,1,0) SM singlet | state 0, weight (−1,−1,−1,−1) | state 0 | ✓ |
| C1-conjugate index / same chirality | 15 / True | 15 / True | ✓ |
| Dirac partners in H_K− (opposite-chirality singlets) | **0** ⇒ Dirac IMPOSSIBLE | 0 | ✓ |
| H_F+ Majorana block Frobenius | 3.5666252277 > 10⁻¹² | 3.5666252277 | ✓ (reldiff 0.0) |
| bare bilinear \|⟨Jξ\|D_F\|ξ⟩\| | 0.0 (T4: tree = 0; mass is seesaw-generated) | 0.0 | ✓ |
| **DETERMINATION** | **MAJORANA** | MAJORANA | ✓ (`all_match=True`) |

CC-CACHE (L12 master cache, 90 sectors): the (0,0) sector of D_K **is** the bare singlet D_F (T_a act as 0 on the trivial rep), and the 16 cache `abs_evals` match the re-run D_F spectrum to **maxdiff 0.0 exact**; min |eval| = 0.81974111 on both — the same E₁ the §W5-1 bottom-triple read from the (0,0) tower (cross-gate consistency of the singlet sector).

**(2) PART 2 — m_ββ = |Σᵢ U_eᵢ² mᵢ| (Route-A: S99 oscillation-anchored masses × laboratory-IN PMNS pins).**

Inputs: m_i = [0, 0.0086776, 0.0495278] eV from `s99_w3_seesaw_summnu.npz` (plan-triple maxdiff 4.3e-8; **ordering NO confirmed**: m₁ = 0 rank-deficient lightest, m₂ < m₃). Implied Δm²: 7.5300e-5 / 2.4530e-3 eV² vs canonical NuFit-6.0 pins (7.49e-5 / 2.513e-3): reldiff **0.53% / 2.39%** — the S99 masses were anchored to the PDG-style |Δm²₃₂| convention; ordering identical, magnitudes within 2.5% (cross-check, non-gating). PMNS pins (plan machinery_pin_map; in-script `# (local)`): sin²θ₁₂ = 0.307, sin²θ₁₃ = 0.0220 → U_eᵢ² = [0.677754, 0.300246, 0.022000]; electron-row closure |ΣU_eᵢ² − 1| = **0.0 exact** (unitarity).

| quantity | value |
|:---------|:------|
| terms U_eᵢ² mᵢ | [0, 2.6054e-3, 1.0896e-3] eV (both nonzero terms positive at zero phase) |
| **m_ββ^{central}** (δ_CP = 0, Majorana phases 0) | **3.6950127968e-3 eV = 3.6950 meV** (full float64 in npz; publication_precision=4) |
| δ_CP ∈ {0,π} degeneracy | \|m_ββ(0) − m_ββ(π)\| = **0.0 exact** (δ enters only via e^{−2iδ} = 1 at both substrate-forced values) |
| Majorana-phase band (pre-registered 240×40 grid, step 2π/240 × 2π/40) | **[1.5158, 3.6950] meV** |
| analytic band cross-check [\|t₂−t₃\|, t₂+t₃] | absdiff 2.2e-19 / 8.7e-19 (π and 0 are on-grid) |
| central = band max | True — no-cancellation positive sum ⇒ the central IS the funnel upper edge |
| plan-freeze hand-substitution (3.69e-3 eV) | reldiff 0.14% ✓ |

**(3) Bound placement (laboratory falsifier ladder):**

| bound | value [meV] | central below? | margin |
|:------|:------------|:---------------|:-------|
| KamLAND-Zen 800 (current, loose NME) | 122 | YES | ×33.0 (even at the tight-NME end ~28 meV: ×7.6 — the PASS is NME-robust) |
| LEGEND-200 reach (loose NME) | 75 | YES | ×20.3 |
| next-gen floor (LEGEND-1000/nEXO) | 10 | YES | ×2.7 |
| pre-registered NO funnel | [1.5, 4.5] | central **INSIDE** | full band [1.516, 3.695] also inside (lower edge sits 1.05% above the funnel floor) |

Detection-physics statement (falsifiability mode): the predicted band [1.52, 3.70] meV lies BELOW the next-gen design floor (6–20 meV NME band; canonical floor pin 10 meV). The next-gen test is therefore **one-sided**: a 0νββ detection at m_ββ > 4.5 meV would FALSIFY the (NO, m₁=0, Majorana-texture) configuration outright; a next-gen null result is consistent but non-confirming. Direct two-sided coverage of the predicted band requires beyond-next-gen ~meV-class sensitivity. This makes the plan's "next-gen-or-bust" framing precise: the falsifier-inventory row (mack-routed) should carry the one-sided-detection clause, not a naive "LEGEND-1000 will see it" claim.

**(4) Substitution chain with substituted numbers** (pre-registered in plan §W5-2; [VERIFY] gate — no 3-tuple):

```
Step 1: m_bb = |U_e1² m_1 + U_e2² m_2 + U_e3² m_3|;  m_1 = 0 (NO, PROVEN);  pins s12² = 0.307, s13² = 0.0220
Step 2: m_bb^{central} = |s12² c13² m_2 + s13² m_3|        (m_1 term vanishes; zero phases)
Step 3: c13² = 1 − 0.0220 = 0.9780;  s12² c13² = 0.300246
        term_2 = 0.300246 × 0.0086776 = 2.6054e-3 eV
        term_3 = 0.0220   × 0.0495278 = 1.0896e-3 eV
        m_bb^{central} = 2.6054e-3 + 1.0896e-3 = 3.6950e-3 eV   (both terms > 0 ⇒ NO cancellation ⇒ funnel UPPER edge)
Step 4: 3.695 meV << 122 meV (below current bound)  AND  3.695 ∈ [1.5, 4.5] meV (in funnel)  ⇒ PASS
        Majorana-phase scan only LOWERS m_bb (cancellation), bracketing [1.516, 3.695] meV.
```

**(5) Cross-checks (all pass) + diagnostics (non-gating):**
- **CC-P1**: PART-1 re-run vs `s96_matter_0nubb.npz` — determination match, frob reldiff 0.0, all KO residuals 0.0, `all_match=True`.
- **CC-CACHE**: L12 (0,0)-sector ≡ D_F spectrum, maxdiff 0.0 (90 sectors present).
- **CC-UNI**: PMNS electron-row closure exact (c₁₂²c₁₃² + s₁₂²c₁₃² + s₁₃² = 1, residual 0.0).
- **CC-DCP**: δ_CP ∈ {0,π} m_ββ-degenerate to 0.0 — the substrate-forced δ set is 0νββ-equivalent.
- **CC-DM2**: implied Δm² vs NuFit-6.0 canonical pins 0.53%/2.39% (PDG-vs-NuFit convention spread; ordering identical).
- **CC-BAND**: 240×40 grid band = analytic [|t₂−t₃|, t₂+t₃] to ≤8.7e-19.
- **CC-HANDSUB**: plan-freeze hand value 3.69e-3 eV reproduced at 0.14%.
- **(d1)** NuFit-6.0 Δm²-implied masses (m₂=√7.49e-5, m₃=√2.513e-3): m_ββ = 3.7013 meV (+0.17%).
- **(d2)** NuFit-6.0 IC19+SK best-fit angles (0.303/0.02225): m_ββ = 3.6728 meV (−0.60%). PMNS-version note: the plan's 0.307/0.0220 pins (labeled NuFit-6.0) match NuFit-5.x/PDG-style central values; the NuFit-6.0 IC19+SK NO best fit is 0.303/0.02225. The gate uses the PLAN pins (pre-registration discipline); the 0.60% sensitivity is decision-irrelevant at every boundary (funnel width is a factor ~3, bound margins ×2.7–×33).
- **(d3)** S96 W4-2 framework-U_ei route: 8.273 meV — the 2.2× difference is PURELY the U_ei source (the W4-2 framework angles were the S96 INFO caveat; replacing them with laboratory-IN NuFit pins is exactly what cleans the m_ββ half to Route-A).

**(6) track_A/track_B posterior reallocation (pre-registered discriminator, plan §W5-2 dual_prior):** outcome = PASS (m_ββ < KamLAND-Zen AND in NO funnel) → **reallocate 0.95 to track_A** (prior was track_A 0.85 / track_B 0.15): the substrate IS Majorana (KO-dim-6 J-self-conjugate singlet, zero Dirac partners) at a falsifiable laboratory magnitude; the OBSERVABLE leg supports the seesaw/Majorana reading and FEEDS the D5 workshop. Note the axis separation: W5-2's tracks discriminate Majorana-texture-consistency; they are ORTHOGONAL to §W5-1's zero-free-param/oscillation-anchored tracks, whose 0.9-to-track_B reallocation stands unchanged and is inherited here as the scale caveat.

**(7) Verdict-reading note — why the inherited track_B caveat frames but does not downgrade PASS→INFO.** The plan's INFO_meaning lists "the S100a-MD-NORMALIZATION track_B residual feeds the absolute scale" as an example m_ββ qualification. Reading that clause as verdict-forcing would make the pre-registered PASS boundary unreachable BY CONSTRUCTION: the gate's own method step (2) pins the S99 OSCILLATION-ANCHORED masses as the Route-A design (the plan chose this knowing the anchor), and `boundary_reachable_analytically: true` declares the PASS band reachable. Per the closing-paragraph-coherence pattern (`epistemic-discipline.md`), the self-consistent reading is: the numerical operator decides PASS/FAIL; the INFO clause covers material NEW qualifications arising at compute time (PMNS prereq failure, scale AMBIGUITY in the m_i values). W5-1's INFO created no such ambiguity — it confirmed the already-declared PROVENANCE of the unchanged m_i (oscillation-anchored, residual-Dirac-scale-normalization-IRREDUCIBLE). The caveat is therefore carried as pre-registered framing: **m_ββ is a prediction CONDITIONAL on the measured Δm² plus the substrate-structural inputs (NO ordering, m₁ = 0 exact, Majorana texture, δ_CP ∈ {0,π}) — NOT a zero-free-parameter substrate number.** It is encoded in the verdict value string, the verdict-file scale-provenance companion row, and the `m_bb_FW` canonical provenance comment.

**Assessment (substrate framing — PARTICLE).** The neutrino's Majorana-vs-Dirac character is NOT an external assumption — it is fixed by the real structure J of the spectral triple. The flow: D_K + J (KO-dim-6 on the doubled ℂ³²; M_3(ℂ) summand of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)) → the (1,1,0) SM singlet is J-self-conjugate within its chirality with ZERO opposite-chirality Dirac partners → MAJORANA texture (Pfaffian on H_K+) → the seesaw light masses (S99; substrate D_K eigenvalues seesaw-suppressed) contract with the laboratory-IN PMNS U_ei → m_ββ → the laboratory 0νββ half-life observable (KamLAND-Zen / LEGEND). Never inverted. What this PASS constrains: the substrate's Majorana character now sits at a CONCRETE laboratory magnitude — m_ββ ∈ [1.52, 3.70] meV with central 3.695 meV at the no-cancellation upper edge — consistent with every current non-detection, NME-robust against the current bound, and one-sided-falsifiable at next-gen (any detection above the 4.5 meV funnel edge kills the (NO, m₁=0, Majorana) configuration). What it does NOT do (SCOPE PIN): reconcile capstone §7.3 D5 — the "no-seesaw" §0 prose vs the Majorana M_R the seesaw uses remains the workshop adjudication. Cross-axis: `dirac-antimatter-theorist` owns the KO-dim-6 Pfaffian determination review (derivation-author tag, plan §"Cross-axis dispatch note").

**Session-close routing (plan §"Wave 5 → Wave 6 Decision Point", PASS branch; canonical write-order):** (1) verdict line landed via `emit_verdict` (race-safe; audit `a2d29b97…`, content `9ddd1ba5…`); (2) **`m_bb_FW = 0.0036950127968154492` promoted to `canonical_constants.py` SECTION E in-session** with full provenance + band + caveat (single unambiguous `update_constant` ⇒ fix-in-session per `math-scripts.md` §"In-session promotion vs carry-forward"); (3) the falsifier-master-inventory 0νββ row → `mack-cosmic-bridge` (SOLE WRITER) at session close, carrying the one-sided next-gen falsification clause from Results (3). `/weave --update` at session close (orchestrator) indexes the new constant.

---

## Wave 5 Synthesis (team-lead)

**Date**: 2026-06-06. **Gates**: 2 (1 PASS, 1 INFO). Both verdict lines carry full 64-char dual-SHA closures in `computations/session-100a/s100a_gate_verdicts.txt` (W5-1 with schema-v2 `[SIGN]` 3-tuple; W5-2 `[VERIFY]`, correctly no 3-tuple); all artifacts on disk and content-verified.

### 1. The uniqueness question is now ANSWERED, not caveated (W5-1)

**W5-1 (INFO, track_B 0.9)**: the D_K bottom light-triple does NOT uniquely pin the Dirac Yukawas — MAP-A vs MAP-B disagree at uniqueness ratio 0.4742 (9.5× over the 0.05 tolerance), and both maps land ~100× below the 0.0582053272 eV target. Decisively, the residual freedom is NOT a single overall scale: the per-generation rescales required to reach the S99 baseline are non-constant ([5.73, 13.66] MAP-A; [5.85, 9.70] MAP-B) and the required shape Y₃/Y₂ = 2.4883 matches neither map (1.0444 / 1.5000 exact). The S99 track_B caveat ("m_D Yukawa normalization oscillation-anchored") is therefore **confirmed PERMANENT on the absolute-scale axis** — the Dirac scale is irreducibly external at every bottom-triple-anchored normalization, shape-independently; the SHAPE corridor through the W2/W3 sector-keyed exponential ε_LX class remains open and is pre-registered for S101 (S101-NU-DIRAC-ENVELOPE-MAP), with the one identified scale-closing corner (√C₂ q→0⁺ edge, post-hoc) queued for falsification there *(phrase scoped 2026-06-07 per `session-100a-yukawa-wall-scope-synthesis.md` §IV.2 — Q3/Q4 designated-writer patch; original read "irreducibly external, not a refinable approximation", which as all-maps breadth would assert the SHAPE corridor closed — FAIL-branch language the INFO verdict does not license)*. What SURVIVES at PASS-grade: M_R = D_K B-branch fold energies (cross-checked to 0.0177 < 0.02 vs the S60 texture), the seesaw structure, the suppression direction (strictly negative derivatives both maps), and normal ordering. **New structural sub-result**: MAP-B's Casimir grading forces Y₁ = 0 EXACTLY (C₂(0,0) = 0) — seesaw rank-deficiency (the massless lowest state) EMERGES from the substrate grading rather than being imposed.

### 2. The D5 observable leg lands at falsifiable magnitude (W5-2)

**W5-2 (PASS, track_A 0.95 on the texture)**: the KO-dim-6 Pfaffian Majorana determination is bit-exact (S96 machinery re-run: all residuals 0.0, zero Dirac partners, the (1,1,0) M₃(ℂ) singlet J-self-conjugate ⟹ MAJORANA admitted), and the Route-A effective mass lands m_ββ^{central} = **3.695 meV**, Majorana-phase band **[1.516, 3.695] meV** — ×33 below KamLAND-Zen AND inside the NO funnel [1.5, 4.5] meV (both pre-registered conjuncts met). δ_CP ∈ {0, π} is m_ββ-degenerate exactly. **Detection-physics nuance for the inventory row**: the band lies below the next-gen 10 meV floor, so the next-generation test is ONE-SIDED — a detection above 4.5 meV falsifies the texture; a null is consistent but non-confirming. Internal consistency across the wave: W5-2's D_F spectrum cross-check reproduced W5-1's E₁ = 0.81974111 at maxdiff 0.0 (the same L12 (0,0)-sector eigenvalue read by two independent routes).

### 3. How the two verdicts compose

The INFO caps the confidence of the ABSOLUTE neutrino-mass scale (Dirac-scale anchor external); the PASS establishes the TEXTURE + funnel placement. W5-2's m_ββ inherits the W5-1 caveat in framing only (encoded in its verdict value string + the `m_bb_FW` canonical provenance) — the funnel-placement verdict is robust because the oscillation-anchored m_i are the very inputs the caveat scopes. Per the plan's cross-gate note, this is the pre-registered composition, executed in order (W5-1 batch 1 → W5-2 batch 2).

### 4. Downstream implications

| Stream | Effect of W5 | Action |
|:-------|:-------------|:-------|
| Capstone §7.3 item-(4) scorecard | Σmν NOT zero-free-parameter; Dirac-scale anchor irreducibly external (uniqueness-INFO) | mack-cosmic-bridge records the §7.3 item-(4) re-scope at session close (capstone-hygiene Q3) |
| `Sigma_mnu_FW` canonical | Value unchanged; provenance comment gains the uniqueness-INFO finding | EFFECTED in-session (orchestrator-direct comment edit, import-verified) — see Effected In-Session |
| 0νββ falsifier surface | New canonical `m_bb_FW = 3.695 meV` + band + one-sided next-gen clause | mack-cosmic-bridge lands the inventory 0νββ row at session close (write-order step 3) |
| Capstone §7.3 D5 STATUS | stays `unreconciled` (SCOPE PIN honored regardless of PASS) | No edit; the §0 no-seesaw-vs-Majorana-M_R prose adjudication is a Q1 workshop seed for `/rclab-investigate` (NOT a CF) |

### 5. Wave classification

**Falsifier-sharpening + scope-honesty.** W5 converted a standing caveat into a structural permanence result (non-uniqueness measured, shape mismatch quantified, Y₁ = 0 emergence found) and landed the framework's 0νββ observable at a magnitude that is simultaneously consistent with all current bounds and concretely falsifiable (one-sided) by the LEGEND-class generation.

### Effected In-Session (NON-MATH — team-lead orchestrator)

- [x] `m_bb_FW = 0.0036950127968154492` PROVENANCE promotion (canonical write-order step 2) — effected in-gate by W5-2 via `update_constant`; orchestrator import-verified — `computations/_shared/canonical_constants.py` SECTION E — `a2d29b975d8cb170`
- [x] `Sigma_mnu_FW` provenance comment gains the uniqueness-INFO finding (plan W5→W6 decision point, INFO branch: "only its provenance note gains the uniqueness-INFO finding") — orchestrator-direct comment-only edit, value unchanged, import re-verified clean — `computations/_shared/canonical_constants.py:664` — `4f92a5513ad69b07`
- [x] Capstone §7.3 surface items (item-(4) Dirac-scale re-scope; 0νββ inventory row with one-sided clause) consolidated into the session-close `mack-cosmic-bridge` sole-writer dispatch queue (executes this session before STOP; tracked task #26) — per `feedback_mack-bridge-role.md`
- [x] D5 prose adjudication tagged as Q1 workshop seed (routes via `/rclab-investigate`, NOT a CF; SCOPE PIN honored) — recorded here + §W5-2 Results
- [x] Orchestrator-direct presentation patches: none required (both sections landed complete; zero must_contain misses)

## Carry-Forward Computations

No carry-forwards: all wave outcomes closed in-session. (Both gates landed their pre-registered branches; the W5-1 FAIL-branch trigger for a distinct-substrate-forward-map CF did not fire — the verdict is INFO, and the plan's INFO branch routes to provenance/scope recording only, executed above. The D5 prose adjudication is a workshop seed per `Investigating-Workshops.md` §Q1, not a compute CF.)

> **Addendum (2026-06-07, `/rclab-investigate` consolidation)**: the statement above stands for the plan's pre-registered triggers, but one Q2 item surfaced FIRST at investigation (`workshops/_seed-w5.md`; the plan's Input-SHA-Ledger note promised the post-gate hook would promote the PMNS pins per the write-order — it did not, an upstream wave-synthesis miss). Canonical Q2 routing (housekeeping §B append) is the orchestrator's; this block is the WP mirror `/rclab-plan` consumes. The D5 adjudication is scheduled as `session-100a-workshop-schedule.md` W-4; the D_F-texture wall-scope review as S-3.

### CF-W5-1 — PMNS-pin canonical promotion with version-disambiguation sub-keying [Q2-hygiene — registry-hygiene compute carry-forward; housekeeping §B mirror]

1. **What**: Promote the W5-2 PMNS electron-row pins (sin²θ₁₂ = 0.307, sin²θ₁₃ = 0.0220, currently in-script `# (local)` only) to `canonical_constants.py` with version-correct names — the gate's own (d2) diagnostic shows the plan's "NuFit-6.0" labels actually match NuFit-5.x/PDG-style central values (true NuFit-6.0 IC19+SK NO best fit: 0.303/0.02225, a −0.60% m_ββ shift, decision-irrelevant), so the promotion requires a sub-keying decision (e.g., `sin2_theta12_PDG` + `sin2_theta12_NuFit60` pair, or a convention-tagged single pin) rather than a single unambiguous `update_constant` call — exactly the `math-scripts.md §"In-session promotion vs carry-forward"` CARRY-FORWARD branch.
2. **Inputs**: `computations/session-100a/s100a_d5_0nubb_majorana.py` (the `# (local)` pins + NuFit source comments); verdict companion row (`s100a_gate_verdicts.txt:32`: "PMNS pins ... in-script (local) per plan - absent from canonical_constants"; audit `a2d29b975d8cb170`); WP §W5-2 diagnostics (d2); `canonical_constants.py:2111` (existing audit-allowlist tokens `sin2_12_pdg`/`sin2_13_pdg`/`sin2_23_pdg` to reconcile).
3. **Gate**: `S101-HK-PMNS-PIN-PROMOTION` — PASS iff both pins land with version-tagged names + PROVENANCE + the allowlist tokens reconciled, import-verified.
4. **Effort**: ~0.1 wave-equivalents.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-06 | Substrate-forward Σmν normalization (S99 track_B successor) | OPEN — "does the bottom-triple uniquely pin Y_i?" | CLOSED-INFO — map NON-UNIQUE (0.4742 ≫ 0.05), residual NOT 1-parameter (shape mismatch 2.4883 vs 1.04/1.50), Dirac-scale anchor irreducibly external; M_R + structure + direction + ordering survive PASS-grade; Y₁ = 0 emerges exactly in MAP-B | S100a-MD-NORMALIZATION INFO (`4f92a5513ad69b07`) |
| 2026-06-06 | D5 Majorana-vs-Dirac observable leg | Determination registered (S96) but no m_ββ magnitude on the books | m_ββ = 3.695 meV [1.516, 3.695] — MAJORANA admitted bit-exact; inside NO funnel; ×33 below KamLAND-Zen; one-sided next-gen falsification | S100a-D5-0NUBB-MAJORANA PASS (`a2d29b975d8cb170`) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| S100a-MD-NORMALIZATION | `s100a_md_normalization.py` | `s100a_md_normalization.npz` | `s100a_md_normalization.png` | — | 40.9 KB / 21.7 KB / 119.2 KB |
| S100a-D5-0NUBB-MAJORANA | `s100a_d5_0nubb_majorana.py` | `s100a_d5_0nubb_majorana.npz` | `s100a_d5_0nubb_majorana.png` | — | 39.3 KB / 108.2 KB / 80.5 KB |

(Both gates emit to `computations/session-100a/s100a_gate_verdicts.txt` via the race-safe `emit_verdict` MCP tool.)
