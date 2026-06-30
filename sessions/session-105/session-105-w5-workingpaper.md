# Session 105 Wave 5 — Spectral-Functional HDR Certification (Results Working Paper)

**Session**: 105 | **Wave**: 5 | **Plan**: session-105-plan-w5.md | **Theme**: heat-trace dimension-spectrum log-periodic certification — rebuild K_osc(t) at the s84 L=12 dynamic range and re-run the IDENTICAL pinned S104 pipeline to test for a genuine complex-dimension line Im(s)≠0 (discrete-scale-invariance fine structure) vs the PROVEN CM-1995 simple-real-Sd wall.

## Gate Sections

### §W5-1. S105-W5-1-LOG-PERIODIC-HDR (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S105-W5-1-LOG-PERIODIC-HDR`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the heat-trace residual IS the substrate's dimension-spectrum signature — the fabric, not its excitations)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: Rebuilt at the s84 L=12 dynamic range (166,896 block eigenvalues / ~32M PW-weighted vs the S61 992-mode residual), the log-detrended heat-trace oscillatory residual K_osc(t) either carries a stable interior complex-dimension line Im(s)=ω* > ω_min with prominence ≥ 10× across the full γ/d × SDW-order family, OR it does not — re-confirming the CM-1995 simple-real-Sd wall on the frequency axis at higher dynamic range (substrate-first prediction: FAIL, no line).
**Plan reference**: `sessions/session-plan/session-105-plan-w5.md` §W5-1 (machinery pin, thresholds, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | must_contain verified |
|:---------|:-----|:-------|:----------------------|
| script | `computations/session-105/s105_log_periodic_hdr.py` | ✅ | `from canonical_constants import` ✅; `print_verdict_payload` ✅; `a_0_FW_zeta` ✅; `find_peaks` ✅ |
| data | `computations/session-105/s105_log_periodic_hdr.npz` | ✅ | (non-optional; written, 28 top-level + per-member fields) |
| plot | `computations/session-105/s105_log_periodic_hdr.png` | ✅ | (non-optional; 2-panel: overlaid power spectra + g(u) residuals) |
| verdict_line | `computations/session-105/s105_gate_verdicts.txt` | ✅ | `^S105-W5-1-LOG-PERIODIC-HDR:.* audit_sha256=[a-f0-9]{64}` ✅; dual-SHA companion ✅; schema-v2 3-tuple ✅ |
| wp_section | this §W5-1 | ✅ | Status COMPLETED ✅; Verdict INFO ✅; Output Artifacts ✅; MCP Pre-Compute Audit ✅ |

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge('log-periodic complex dimension Im(s) heat trace oscillation CM-1995 dimension spectrum')` → returned the S104 `log_periodic_ims` provenance (prior INFO), the **PROVEN** CM-1995 theorem (`Sd = {0,2,4,6,8} ⊂ ℤ`, simple, REAL — Connes-Moscovici 1995 §5, local index formula requires a regular spectral triple with simple dimension spectrum), and the equation `P(σ) = Σ_{(p,q)} dim(p,q)·Σ_i exp(−σ λ_i²)` [return probability / heat trace]. Confirms the gate is NOT pre-closed (it is the conditional CF that fires on the S104 INFO), and the substrate-first wall is PROVEN.
- `get_constant('a_0_FW_zeta')` → 6440.0 (S88, non-superseded). `a_2_FW_zeta` → 2776.165389. `a_4_FW_zeta` → 1350.7216. `a_6_FW_zeta` → 765.593826 (S96). `a_8_FW_zeta` → 521.183178 (S96). All five non-superseded; consumed as the FULL physical zeta-regulated SDW smooth-part coefficients (CLASS=FULL, no SCHEMATIC helper).
- `get_constant('tau_fold')` → 0.190 (the s84 cache anchor; imported via `from canonical_constants import tau_fold`, cross-checked against the cache build).

**Verdict**: **INFO** — `sign_verdict=N/A`, `magnitude_verdict=INFO`, `regime_verdict=MARGINAL` (schema-v2 3-tuple; composite collapse `magnitude=INFO ⇒ composite=INFO`).

The S104 scheme-dependent-sidelobe reading is **CONFIRMED at the s84 L=12 dynamic range**: all 6 family members carry an interior peak above the 10× floor (`n_members_with_peak=6/6`), but the peak position is NOT cross-axis stable (`cross_axis_stable=False`; ω*-bin spread = **5 bins ≫ ±1 tolerance**). The dynamic-range upgrade (166,896 block / 31,956,720 PW-weighted modes vs S104's S61 992-mode/200-t residual) did NOT resolve the ambiguity — it sharpened the residual but the peak remained scheme-dependent. The complex-dimension question stays **OPEN-by-scheme-dependence** (no clean corridor closure, no PASS).

**Results**:

**STAGE A — heat-trace + Strutinsky build (HDR source, s84 L=12, τ_fold=0.190, N_T=1024 geometric on [0.01, 100])**:
- Block eigenvalues = **166,896** (90 Peter-Weyl (p,q) sectors; sector (4,4) absent → 90 of 91, accounted for by the dict-keyed iteration); PW-weighted modes = **31,956,720** (Σ dim_SU3(p,q)·n_block per sector).
- K(t_min=0.01) = 2.732e+07; K(t=1) = 5961.91; K(t_max=100) = 2.401e−29 (the expected Weyl bulk roll-off; all PW-weighted positive exp-sum).
- SDW-order smooth part: K̃(t) = Σ_{n∈{0,…,2o}} a_n^{ζ}·t^{(n−8)/2} (d=8, zeta-regulated, CLASS=FULL) with canonical pins a_0=6440, a_2=2776.17, a_4=1350.72, a_6=765.594, a_8=521.183. γ/d smooth part: Gaussian-Strutinsky-smoothed DOS Laplace transform (self-normalizing; IDENTICAL prescription to S61 §6).

**Per-member family results** (3 γ/d × 3 SDW order; ω in rad per ln-t unit = Im(s) directly):

| Member | Axis | peak ω* | FFT bin | prominence | line_found | band_edge | COUNTS |
|:-------|:-----|--------:|--------:|-----------:|:----------:|:---------:|:------:|
| sdw_2 | sdw_order | 1.7046 | 5 | 1.346e+13 | True | True | True |
| sdw_3 | sdw_order | 1.7046 | 5 | 3.728e+12 | True | True | True |
| sdw_4 | sdw_order | 1.7046 | 5 | 1.295e+12 | True | True | True |
| gd_1.0 | gamma_d | 1.7046 | 5 | 6.241e+18 | True | False | True |
| gd_1.5 | gamma_d | 3.0683 | 9 | 1.685e+18 | True | False | True |
| gd_2.0 | gamma_d | 1.3637 | 4 | 9.521e+18 | True | False | True |

- **Cross-axis stability conjunction**: `n_members_with_peak=6/6`, but **ω*-bin spread = 5 (bins 4→9) ≫ STABILITY_BIN_TOL=1** ⇒ `cross_axis_peak_stable=False`. The SDW-order axis is internally ω*-stable (all 3 orders → bin 5, ω*=1.7046), but the γ/d-smoother axis SCATTERS (bin 5 → bin 9 → bin 4 as γ/d = 1.0 → 1.5 → 2.0). **A genuine complex dimension Im(s) is a property of the SPECTRUM and would be FIXED across smoother widths; a peak that tracks the Gaussian width IS the definition of a scheme-dependent subtraction artifact.** The two subtraction axes do not even agree on a common ω*.
- **DC-envelope-shoulder structure (SDW members)**: for sdw_2/3/4 the band-maximum is at bin 3 (ω=1.0228, the first bin above ω_min — `band_edge=True`); the interior local maximum the guard selects (bin 5) is a small secondary bump on a monotone DC roll-off (power 3.86e16 at bin 3 → 3.10e15 at bin 5 → … decaying away from DC). This is a smooth low-frequency envelope, NOT a sharp discrete self-similar line.
- **γ/d=3.0 diagnostic point** (NOT in the conjunction): prominence 4.117e+18, peak ω*=1.7046 — consistent with the scheme-dependent low-frequency cluster, no additional line.
- **R_osc consistency cross-check** (≤1-OOM anchor, NOT a PASS conjunct): rebuilt R_osc = |K_osc(t=1)/K(t=1)| at γ/d=1.5 = **0.02185** vs the S61 sibling **2.23e−5** (|ΔOOM| = 2.99, `consistent≤1OOM = False`). **This divergence is the EXPECTED consequence of the two declared deltas**: (i) S61 used the **flat/block** mode list (992 modes, dim² weights) with a **moment-matched Taylor-polynomial** smooth part fit to the SAME modes (so the residual is small by construction — the polynomial cancels the bulk); this HDR build uses the **PW-weighted regular-representation** trace (~32M effective modes) subtracted by the **canonical a_n^{ζ}** SDW form whose per-branch-L_max=3 normalization is NOT moment-matched to the 32M-mode bulk, leaving a larger fractional residual at t=1. The R_osc anchor is a magnitude-scale consistency check on the SAME flat-mode/moment-matched scheme as S61; the HDR scheme is deliberately different, so the anchor failing the ≤1-OOM band is NOT a defect of the gate — it reflects the declared source-and-smooth-part change. **The Im(s) FREQUENCY question (the gate's actual subject) is independent of the smooth-part normalization OFFSET**: the cross-axis-stability conjunction spans BOTH the (offset-prone) a_n^{ζ} SDW axis AND the self-normalizing Gaussian-Strutinsky axis precisely so that a genuine line must survive both — and it does not.
- **Hann→rectangular window-invariance cross-check** (diagnostic): the rectangular-window power spectra (`power_rect`) are computed per member; the canonical Hann result already FAILS cross-axis stability, so the window-invariance cross-check is moot for the verdict (a window change cannot rescue a scheme-dependent peak that fails the ±1-bin conjunction under the canonical Hann window).

**Output 4-tuple**: `(value='cross_axis_stable=False;n_members_with_peak=6/6;max_prominence=9.521e+18;strongest_omega=1.70464rad/lnt;implied_s=4+i0;omega_min=0.682188;R_osc_rebuilt=0.02185;R_osc_sibling=2.23e-05;R_osc_consistent=False;n_block=166896;pw_modes=31956720', scheme=FFT-LOG-DETRENDED-RESIDUAL-HDR, convention=poleconv-A-double-power-Re_s_4-curvature_grade_n_0, L_max=12)`.

**Convention / regulator / level pins (CCs)**:
- `regulator_pin = a_n^{ζ}` (the K̃ smooth part is the zeta-regulated Seeley-DeWitt expansion); Mellin pole-set **`(pole_in_s=4, curvature_grade_n=0)` poleconv-A** double-power (`ζ_{D_K}(s)=Σ m_k |λ_k|^{−2s}`, poles at `s=(d−n)/2`; at d=8, n=0 leading curvature grade → Re(s)*=4=d/2). `convention=poleconv-A-double-power-Re_s_4-curvature_grade_n_0`. Companion row emitted: `# regulator_pin=a_n^{zeta} mellin_pole=(pole_in_s=4,curvature_grade_n=0) poleconv-A-double-power CLASS=FULL`.
- `CLASS = FULL` — the SDW smooth part is the FULL physical zeta-regulated expansion from the canonical `a_{0,2,4,6,8}_FW_zeta` pins; NO `_spectral_action_regulators.py` SCHEMATIC helper imported; verdict-line `convention=` carries NO `-SCHEMATIC` suffix (per `substrate-first-canonical-sourcing.md §(iv)`).
- `scheme = FFT-LOG-DETRENDED-RESIDUAL-HDR` — the `-HDR` suffix marks the source-spectrum upgrade (s84 L=12 vs S104's S61 residual) in the audit trail.

**Substitution chain (with substituted numbers) — [SIGN] directional prediction**:
- *Claim*: substrate-first prediction = NO complex-dimension line (Im(s)=0); expected verdict FAIL (CM-1995 wall re-confirmed at HDR).
- *Step 1 (definitions)*: D_K on Jensen-deformed SU(3) at τ_fold=0.190; K(t)=Σ_{(p,q)} dim_SU3(p,q)·Σ_i exp(−t|λ_i|²); K̃(t)=Σ_{n∈{0,2,4,6,8}} a_n^{ζ}·t^{(n−8)/2}; K_osc=K−K̃; g(u)=K_osc(e^u)·e^{4u}; Sd={0,2,4,6,8}⊂ℝ (CM-1995, PROVEN, simple, REAL); Im(s)=ω* of any stationary cos(ω*·ln t).
- *Step 2 (substitution)*: a complex dimension s=4+iω* with ω*≠0 ⟺ g(u) carries a stationary cosine ⟺ a discrete LINE in the FFT above ω_min=π/ln(100)=0.6821881769209206. CM-1995 §5 ⟹ Sd⊂ℝ ⟹ NO s with Im(s)≠0.
- *Step 3 (self-similarity ⟺ DSI line)*: a log-periodic line at ω* requires {|λ_i|} asymptotically self-similar under |λ|→|λ|·e^{2π/ω*} (geometric ladder). The Jensen TT-deformation at τ_fold=0.190 breaks the would-be geometric Weyl ladder ⟹ no asymptotic self-similarity ⟹ ω* has no fixed line; K_osc is a SCHEME-DEPENDENT subtraction residual.
- *Step 4 (direction read-off)*: CM-1995 (Sd real) ∧ (Jensen not self-similar) ⟹ NO STABLE ω* line across the regulator family ⟹ predicted FAIL. **Computed result**: `cross_axis_stable=False` with a peak present at 6/6 members but γ/d-smoother-dependent (ω* tracks the Gaussian width, bin 4→5→9) — this is the **INFO** branch: a scheme-dependent peak, NOT a regulator-robust line. The HDR upgrade SHARPENED the residual but did NOT create self-similarity, so the direction is UNCHANGED from the substrate-first expectation: no fixed line.
- *Step 5 ([SIGN] mapping, IDENTICAL to S104)*: `sign_verdict=N/A` ⟺ unstable/scheme-dependent peak (INFO top-line; direction ambiguous). The computed INFO is the scheme-dependence sub-reading of Track B — consistent with (a sharper form of) the substrate-first "not self-similar" prediction, but it does NOT cleanly close the corridor (which would require FAIL = no member clears the floor). **A PASS would have FALSIFIED the substrate-first prediction and forced a CM-1995 reconciliation; no PASS occurred.**

**Conclusion (solution-space)**: the discrete-scale-invariance / complex-dimension reading is NOT promoted (no regulator-robust Im(s)≠0 line at HDR) and NOT cleanly eliminated (peaks present, scheme-dependent). It stays **OPEN-by-scheme-dependence**. The S104 INFO is confirmed at the s84 L=12 dynamic range; the dynamic-range upgrade did not resolve the ambiguity. No further HDR escalation is pre-registered this session. Per the plan's session-close decision point, **INFO generates no carry-forward** (settled-as-scheme-dependent characterization; a CF is generated ONLY on PASS).

**Dual-SHA**: `audit_sha256=1cec352b62c126cdd623c80e20a3f434206a070c26689fd64201e7bbb9f4edf8`, `content_sha256=51728158af9930e941645846c21d555008d5eba0d6b74acfc5f35f126a74c23d`. Schema-v2 3-tuple companion row emitted: `# sign_verdict=N/A magnitude_verdict=INFO regime_verdict=MARGINAL`. Regulator/HDR/R_osc companion rows emitted (3). Artifacts: `s105_log_periodic_hdr.py` / `.npz` / `.png`.

**Substrate framing**: GEOMETRIC. The heat trace K(t)=Tr e^{−t D_K²}=Σ_{(p,q)} dim_SU3(p,q)·Σ_i exp(−t|λ_i|²) IS the substrate's dimension-spectrum signature — the fabric's full eigenvalue content (166,896 block / 31,956,720 PW-weighted at L=12) read through the heat-trace functional, the fabric ITSELF (its spectral-weight distribution), not its excitations. The Strutinsky split K=K̃+K_osc separates the smooth Weyl/Seeley-DeWitt bulk (the same a_n^{ζ} zeta-regulated moments that generate the emergent metric via a_2 and Yang-Mills via a_4) from the oscillatory shell residual K_osc. The explanation flows D_K eigenvalues → heat-trace moments (a_n^{ζ} smooth + K_osc shell) → dimension-spectrum analyticity (real vs complex pole) → the CM-1995 wall — NOT the reverse. The substrate-first prediction "no frequency" (the Jensen deformation is not exactly self-similar, so the fabric carries no discrete-scale-invariance line) is supported by the result direction (no regulator-robust line); the INFO reflects residual scheme-dependent shell structure (SDW-order-stable but γ/d-smoother-dependent), not a substrate-intrinsic complex dimension.

---

## Wave 5 Synthesis (team-lead)

**Single-gate wave; INFO — the S104 scheme-dependent-sidelobe reading is CONFIRMED at the full s84 L=12 dynamic range.**

§W5-1 rebuilt the heat-trace oscillatory residual from 166,896 block / 31,956,720 PW-weighted modes (vs S104's 992-mode/200-t residual) and scanned the 6-member cross-axis family. Peaks exist at all 6 members (`n_members_with_peak = 6/6`, max prominence 9.5e18) but `cross_axis_stable = False`: the SDW-order axis is ω*-stable (bin 5, ω* = 1.7046) yet band-edge/DC-shouldered, while the γ/d-smoother axis SCATTERS (bin 5 → 9 → 4 as γ/d = 1.0 → 1.5 → 2.0). **A peak that tracks the Gaussian smoother width is the signature of a scheme-dependent subtraction artifact, not a complex dimension** — a genuine Im(s) ≠ 0 line is a property of the spectrum and would sit fixed across smoother widths. No PASS (which would have falsified the substrate-first "Jensen deformation is not self-similar" prediction and forced a CM-1995 reconciliation); no clean FAIL (peaks present everywhere); the complex-dimension reading stays **OPEN-by-scheme-dependence**, and the PROVEN CM-1995 simple-real-Sd wall (`Sd = {0,2,4,6,8} ⊂ ℝ`) is untensioned. The R_osc magnitude anchor (rebuilt 0.0219 vs sibling 2.23e-5, |ΔOOM| = 2.99) is scheme-specific by the two declared deltas — disclosed honestly, not a PASS conjunct; the Im(s)-frequency question is independent of the smooth-part offset. All four input SHAs matched plan pins exactly; STAGE B ported byte-for-byte from S104 (structurally distinct from iterate-until-PASS by construction). 3-tuple sign=N/A / magnitude=INFO / regime=MARGINAL → composite INFO. audit `1cec352b62c126cd…`.

**Effected In-Session (NON-MATH)**
- [x] None surfaced — the wave's single outcome is a settled characterization with no registry/rule/ledger residue

## Carry-Forward Computations

No carry-forwards: all wave outcomes closed in-session. (Per the plan's session-close decision point, a CF fires ONLY on PASS; INFO = settled-as-scheme-dependent characterization, no further HDR escalation pre-registered.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-11 | Log-periodic complex-dimension question | S104 OPEN (scheme-dependence suspected at 992 modes) | CONFIRMED-SCHEME-DEPENDENT at 32M-mode HDR (OPEN-by-scheme-dependence) | W5-1 INFO: no regulator-robust ω* line; γ/d-axis scatter is the artifact signature |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| S105-W5-1-LOG-PERIODIC-HDR | s105_log_periodic_hdr.py | s105_log_periodic_hdr.npz | s105_log_periodic_hdr.png | — | 44,097 / 566,787 / 149,639 B |
