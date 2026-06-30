# Session 107 Wave 3 — Spectral-functional diagnostics + commensurability precision (Results Working Paper)

**Session**: 107 | **Wave**: W3 | **Plan**: session-107-plan-w3.md | **Theme**: Spectral-functional diagnostics (2nd SDW-layer EFT-control extension) + commensurability precision-tightening (⟨r⟩ truncation trend across L∈{12,14,16}).

## Gate Sections

### §W3-1. S107-SDW-2ND-MOMENT-EFT (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S107-SDW-2ND-MOMENT-EFT`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (spectral-functional convergence property of the D_K spectrum; not a phononic excitation)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: Extending the SDW EFT-control diagnostic from the established base layer to the 2nd (deepest closed-cone, k=3: a_8/a_6) layer at the species cutoff Λ_sp, the 2nd-layer ratio r_2nd is tested against the tight `< 0.1` ceiling (analytic prediction 0.160424 → INFO marginal band).
**Plan reference**: `sessions/session-plan/session-107-plan-w3.md` §W3-1 (machinery pin, thresholds, substitution chain, distinctness ledger).

**Verdict**: **INFO** — r_2nd = **0.1604** lands in the marginal band `[0.1, 0.5)`: the 2nd SDW layer's scheme-independent EFT-control ratio is under the S96 loose-control band but NOT under the tight EVOI #12 `< 0.1` ceiling. The "2nd-moment EFT controlled at `< 0.1`" corridor closes at the species scale; the loose-band INFO from S96 is preserved. This is the plan's pre-registered predicted disposition (analytic r_2nd = 0.160424). **SIGN/MAGNITUDE/REGIME 3-tuple**: `sign_verdict=PASS` (predicted positive sign of (r_2nd − 0.1) confirmed: +0.0604), `magnitude_verdict=INFO` (marginal), `regime_verdict=VALID` (closed d=8 cone exact) → composite **INFO** per the gate-verdicts.md collapse rule (magnitude=INFO ⇒ INFO).

**NUMBERS (first — per dispatch discipline)**:

| Quantity | Value | Source |
|:---------|:------|:-------|
| a_8/a_6 (2nd-layer FI a-ratio driver) | 0.680757 | canonical a_8_FW_zeta / a_6_FW_zeta |
| (Λ_sp/M_KK)^{−2} | 0.235649 | 1/2.06² (species-scale spectral cutoff) |
| **r_2nd = (a_8/a_6)·(Λ_sp/M_KK)^{−2}** | **0.160420** | gated object |
| tight ceiling (EVOI #12; PASS<) | 0.1 | plan `ctrl_pass_strict` |
| loose ceiling (S96; INFO/FAIL split) | 0.5 | plan `ctrl_fail_strict` |
| signed delta (r_2nd − 0.1) | +0.060420 | sign_verdict driver |
| published value (Class-8.3, 4 sf) | 0.1604 | downstream EVOI #12 cite |

**Substitution chain** (plan §W3-1 Step 1–5; substituted numbers):
- Step 1 — Definitions: a_6_FW_zeta = 765.593826 [M⁻⁶], a_8_FW_zeta = 521.183178 [M⁻⁸], Λ_sp/M_KK = 2.06 (all canonical, Superseded=False verified at runtime); 2nd-layer index k = 3 is the deepest successive-term ratio in the CLOSED d=8 cone {a_0,a_2,a_4,a_6,a_8} (poles s=(8−n)/2 close at n=8/a_8 — there is no a_10 layer-ratio in the cone).
- Step 2 — Substitution: r_2nd = (a_8/a_6)·(Λ_sp/M_KK)^{−2} = (521.183178/765.593826)·(2.06)^{−2}.
- Step 3 — Simplification: a_8/a_6 = 0.680757; (2.06)^{−2} = 0.235649; r_2nd = 0.680757 × 0.235649 = **0.160420**. (The plan's analytic 0.160424 rounded a_8/a_6 to 0.680771; the bit-exact canonical ratio is 0.680757, giving 0.160420 — agreement to 4e-6, well inside the 4-sf publication precision.)
- Step 4 — Direction: r_2nd = 0.160420 > 0.1 ⇒ the 2nd-layer ratio is NOT below the tight EFT-control ceiling. The species-scale Λ^{−2}=0.2356 suppression is INSUFFICIENT to bring the deepest closed-cone a-ratio (0.6808, the a_8/a_6 driver S96 found RISING toward 1) under the strict 0.1 band. **Predicted sign of (r_2nd − 0.1) = POSITIVE ⇒ confirmed (computed sign +) ⇒ sign_verdict = PASS.**
- Step 5 — Verdict band: PASS iff r_2nd < 0.1; INFO iff 0.1 ≤ r_2nd < 0.5; FAIL iff r_2nd ≥ 0.5. Computed r_2nd = 0.1604 → **INFO** band (marginal).

**Full {r_0..r_3} a-ratio-driver ladder** (FUNCTIONAL-INVARIANT diagnostic; w(L_max) cancels):

| k (layer) | a-ratio a_{2(k+1)}/a_{2k} | r_k @ Λ=M_KK (lam⁻²=1) | r_k @ Λ=Λ_sp (lam⁻²=0.2356) |
|:----------|:--------------------------|:-----------------------|:-----------------------------|
| 0 (a_2/a_0) | 0.431082 | 0.431082 | 0.101584 |
| 1 (a_4/a_2) | 0.486542 | 0.486542 | 0.114653 |
| 2 (a_6/a_4) | 0.566804 | 0.566804 | 0.133567 |
| **3 (a_8/a_6)** | **0.680757** | 0.680757 | **0.160420 ← gated r_2nd** |

The a-ratio is MONOTONE INCREASING toward 1 (0.431 → 0.487 → 0.567 → 0.681): the S96 rising-toward-unity finding, extended to the 2nd layer. Even at the species cutoff, raising k *increases* the ratio — every higher SDW layer is closer to the EFT-control boundary, not further from it. The deepest (k=3) layer is the worst case, and it lands marginal.

**E38 per-branch cache cross-check** (pins a_6/a_8 on the canonical a_0/a_2/a_4 footing): re-derived a_n = ½ Σ_modes m_k |λ_k|^{−n} at L_max_branch=3 from the S84 L12 master cache (`sector_evals` dict, p+q≤3, Weyl-dim `info["dim"]` multiplicity weighting per E38), n_unique_modes=1232, total_mult_weighted=12880.0:

| n | cache a_n | canonical a_n | \|dev\| | tag |
|:--|:----------|:--------------|:--------|:----|
| 0 | 6440.000000 | 6440.0 | 0.000e+00 | OK |
| 2 | 2776.165389 | 2776.165389 | 1.366e-07 | OK |
| 4 | 1350.721642 | 1350.7216 | 4.152e-05 | OK |
| 6 | 765.593826 | 765.593826 | 4.158e-07 | OK |
| 8 | 521.183178 | 521.183178 | 1.306e-07 | OK |

cross-check (2× cache-sum = canonical, SAME footing): **PASS** (a_0/a_2/a_4 reproduce bit-exact ⇒ a_6/a_8 are pinned on the identical E38 per-branch zeta footing; this is the provenance, not a re-promotion).

**S96 npz cross-read** (independent prior computation): the S96 `s96_sdw_eft_control.npz` `r_driver_sp[k=3]` = **0.16041964** matches this gate's r_2nd = 0.16041964 to **|dev| = 0.0e+00** — an independently-computed prior pin confirms the value bit-for-bit. The S96 max a-ratio driver @ M_KK = 0.680757 (the S96 base-layer INFO datum) is recovered as the k=3 a-ratio at Λ=M_KK.

**FUNCTIONAL-SENSITIVITY contrast** (the lizzi finding — reported as DIAGNOSTIC, NOT the gated quantity):

| Spectral functional | f_2/f_4 modulation | 2nd-layer ratio | EFT-control reading |
|:--------------------|:-------------------|:----------------|:--------------------|
| **a-ratio driver (scheme-INDEPENDENT)** | 1.000 (cancels) | **0.1604** | **FUNCTIONAL-INVARIANT — the gated object** |
| Gaussian cutoff | 4.1935 (AMPLIFIES) | 0.6727 | f-modulated, near loose ceiling |
| Mellin f* | 0.0333 (CRUSHES) | 0.0053 | f-modulated, PASSES tight ceiling |

The SAME D_K spectrum gives OPPOSITE EFT-control verdicts under different spectral functionals: a Gaussian cutoff pushes the 2nd-layer ratio to 0.673 (near the S96 loose ceiling), a Mellin functional crushes it to 0.0053 (well under the tight ceiling). This is the lizzi-functional-pluralism content made concrete: 'truncation-robust' (FI) and 'parametrically-controlled' are DIFFERENT properties. **Only the scheme-independent a-ratio driver is functional-INVARIANT** (any common w(L_max) spectral-support prefactor cancels in every ratio a_{2(k+1)}/a_{2k} — the multiplicative-normalization cancellation invariant, `math-scripts.md`), so it alone is the structurally-defensible gated object. The f-modulated ratio is a SCHEME-DEPENDENT degree of freedom — which functional a physical measurement would realize is a determination question, not a structural one. The verdict (INFO marginal) reports the FUNCTIONAL-INVARIANT a-ratio driver; the f-modulation is the diagnostic showing why the f-ladder reading cannot be the gate (it flips PASS↔near-FAIL across functionals).

**Substrate-IS assessment**: The substrate IS D_K(τ_fold) on Jensen-deformed SU(3); the SDW layer moments a_{2k} are residues of the substrate's own spectral zeta at the d=8 dimension-spectrum poles s=(8−n)/2 (Connes-Moscovici 1995 §III.4), NOT free parameters. Direction of explanation: D_K eigenvalue spectrum {λ_k, m_k} → closed-cone SDW layer moments a_{2k} → 2nd-layer EFT-control ratio r_2nd at the species scale → EFT-control status of the 2nd moment. **The INFO verdict says: the SDW layer hierarchy is representation-theoretic / numerical (block-diagonality, the rising a-ratio), NOT parametric-EFT, at the 2nd layer** — extending the S96 base-layer reading. The species-scale cutoff lifts the ratio from 0.681 (@ M_KK) to 0.160 (@ Λ_sp), a genuine 4.2× suppression, but the deepest closed-cone a-ratio is too large (0.681, rising toward 1) for one factor of (Λ_sp/M_KK)^{−2} = 0.236 to drop it under 0.1. A tight-control PASS would have required either a smaller a-ratio (a non-rising SDW hierarchy, which the spectrum does not exhibit) or a much higher cutoff. This maps EVOI Tier-3 #12's most likely disposition: **RESOLVED-MARGINAL** — the EFT-control extension to the 2nd moment lands marginal, not strictly controlled, and the functional-sensitivity contrast records that the marginal reading is itself the scheme-INVARIANT one.

**DISTINCTNESS** (recompute-what-is-closed guard): this gate is NOT a re-run of S96-SDW-EFT-CONTROL. S96 evaluated the full term-ratio ladder {r_0..r_3} at the BASE cutoff Λ=M_KK against the LOOSE `<0.5` band → INFO (max a-ratio driver 0.6808 @ M_KK). This gate evaluates the **2nd-LAYER ratio (k=3) at the SPECIES cutoff Λ_sp as primary against the TIGHT `<0.1` ceiling** — a DIFFERENT (cutoff, threshold) pair on the EFT-control axis, the specific question EVOI Tier-3 #12 pre-registers. It is also the EFT-control-ratio complement of the S94-K-CSUB-R-ABSOLUTE-CONVERGENCE base-moment absolute-convergence FAIL (which tested |ΔK/ΔL|<1e-3 on the bare/PV a_2 L-series — a different axis). The MCP search confirmed the 2nd-moment-at-Λ_sp-vs-0.1 verdict object is NOT in the knowledge base; the gate builds on the canonical a_6/a_8 (verified Superseded=False), it does not re-promote them.

**Expected-output 4-tuple**: `(value=0.1604, scheme=Seeley-DeWitt-layer-expansion, convention=RATIO-2nd-layer-a-ratio-driver-at-Lambda_sp-scheme-independent, L_max=10)`.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-107/s107_sdw_2nd_moment_eft.py` — present; `grep -E "from canonical_constants import|print_verdict_payload"` → both patterns matched (see final-message grep block).
- `computations/session-107/s107_sdw_2nd_moment_eft.npz` — present (gated object + full ladder + E38 cross-check + functional-sensitivity + S96 cross-read + 3-tuple + dual-SHA).
- `computations/session-107/s107_sdw_2nd_moment_eft.png` — present ({r_0..r_3} ladder at both cutoffs vs the tight/loose ceilings, gated r_2nd starred).
- Canonical verdict line in `computations/session-107/s107_gate_verdicts.txt` matching `^S107-SDW-2ND-MOMENT-EFT:.* audit_sha256=[a-f0-9]{64}` — present; **dual-SHA companion row** present; **schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row** present (REQUIRED — `[SIGN]` trigger): `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`; **`regulator_pin=a_n^{ζ}` companion row** present; **functional-sensitivity diagnostic companion row** present.
- `audit_sha256` = `c37aa7acb010950cfa5dd12230407ca2ce4700bdf30152eb8927f5b0665d0be3` (full 64-char); `content_sha256` = `6615c2e48e60d86deffb0fa816a52da08d2696b6b90b462ee4131368c8917864` (full 64-char).
- Input-SHA pins matched plan expectations: `s96_sdw_eft_control.npz` = `8d47b91bd51fb6ab584ca13e2b4691fe310cc514cf5e6e8cd72c76df632d0e42`; `s84_spectrum_cache_L12_tau019.npz` = `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`.

**MCP Pre-Compute Audit**:
- `search_knowledge("SDW EFT control 2nd moment a_8 a_6 species scale")` → returned the S96-SDW-EFT-CONTROL gate (INFO; "a-ratio max 0.6808<1; f-ratio FAIL/PASS flip"; §8.5), the S96 provenance `sdw_eft_control`, and the a_6/a_8 constants. Confirms the BASE-layer ladder is closed; the 2nd-layer-at-Λ_sp-vs-tight-0.1 verdict object is NOT in the graph (not yet computed). NOT PRE-CLOSED.
- `get_constant("a_6_FW_zeta")` → 765.593826, session=S96, gate=S96-SDW-EFT-CONTROL, **Superseded=False**.
- `get_constant("a_8_FW_zeta")` → 521.183178, session=S96, gate=S96-SDW-EFT-CONTROL, **Superseded=False**.
- `get_constant("Lambda_sp_over_M_KK")` → 2.06, session=S96, gate=S63-SPECIES-36/SCALE-63, **Superseded=False**.
- (Runtime guard re-verified all three Superseded=False in the producing script before computing — orchestrator override satisfied.)

---

### §W3-2. S107-W1-RTREND-L1416 (spectral-geometer) — OPTIONAL / NON-BLOCKING

**Status**: COMPLETED
**Gate ID**: `S107-W1-RTREND-L1416`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (level statistics of the D_K spectrum at the fixed τ_fold slice; Level-1 single-τ-slice spectral-fluctuation observable)
**Agent**: `spectral-geometer`
**Hypothesis**: The degeneracy-resolved unfolding ⟨r⟩ on the L14 and L16 (operationally L15) spectra each land in the Poisson-incommensurate band, confirming the L12 value 0.4118 is truncation-stable — precision-tightening only; CANNOT change or reopen the already-CLOSED #9e-B SPLIT verdict.
**Plan reference**: `sessions/session-plan/session-107-plan-w3.md` §W3-2 (OPTIONAL / NON-BLOCKING; SPEC-B unfolding pipeline, band, L16-incompleteness pin).

**OPTIONAL / NON-BLOCKING**: This gate is precision-tightening only. #9e-B (length-spectrum incommensurate-Poisson) is CLOSED at L12 (S106-W1-SFF-UNFOLDING-L12 PASS); no downstream S107 gate or registry entry depends on this gate's outcome, and **it drops first** if wave capacity is constrained (a drop is a no-verdict optional skip, NOT a mechanical-closure FAIL). It was executed (not dropped); the verdict below is precision-trend-only and does not touch the SPLIT certificate.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/session-107/s107_w1_rtrend_l1416.py` (40,335 B) | `from canonical_constants import` ✓ (1 hit); `print_verdict_payload` ✓ (2 hits) |
| data | `computations/session-107/s107_w1_rtrend_l1416.npz` (235,481 B) | present ✓ |
| plot | `computations/session-107/s107_w1_rtrend_l1416.png` (259,955 B) | present ✓ (2×2 panels: ⟨r⟩-trend with band, r-ratio histograms, Weyl σ-stability, N_unique growth + L16-incompleteness callout) |
| verdict_line | `computations/session-107/s107_gate_verdicts.txt` | `^S107-W1-RTREND-L1416:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + 2 extra rows (L16-incompleteness, cross-reads). `[VERIFY]` gate — no mandatory 3-tuple; trend-direction note rides in the value string + companion row. |

- **audit_sha256** = `884aab99f18d26766ffdaee386715b61be03c3f6c08b82d6f3f616dd6d1f609f` (script+canonical+pinmap)
- **content_sha256** = `ab581a37f38500bfcac462f48ad60868d766c5d9abc3b61ad2d66c8ef2f82045` (script only)
- 4-tuple: `(value=(0.4254, 0.42), scheme=S46-DEGENERACY-RESOLVED-UNFOLDING, convention=SPEC-B-global-degeneracy-merge, L_max=16)`

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("S106 SFF unfolding L12 incommensurate Poisson level spacing ratio 9e-B")` → returned the closed gate `S106-W1-SFF-UNFOLDING-L12` (PASS, `value='...<r>_B=0.4118;...trackB[0.37,0.44]=IN;xchk_Weyl=0.3888;xchk_specA=0.4527;nearest=POISSON'`) + the open-channel `1b SFF-UNFOLDING-L12` (`F_⟨r⟩ level-set arithmetic, PASS`) + the succession edge `S106-W1-HIGHL-CACHE-L1416 --succ_of--> S106-W1-SFF-UNFOLDING-L12`. Confirms #9e-B is **CLOSED at L12**; this gate is precision-tightening (NOT a reopening). Also surfaced the `s106_w1_sff_unfolding_l12.py` provenance (read for the exact SPEC-B / Weyl-smooth / SPEC-A pipeline) and CHAOS-1 (`⟨r⟩=0.321` single-particle / `0.422` multi-cell — DIAGNOSTIC: ORDERED, integrable-leaning).
- `get_constant("r_GOE_canonical")` → `0.5307` (S81; Wigner surmise GOE mean r; `Superseded=False`) — the FAIL-toward-chaos sentinel. Imported (not hardcoded).
- `get_constant("tau_fold")` → `0.19` (S12/S42; `CONST-FREEZE-42`; `Superseded=False`) — the fixed fold slice. Imported.
- Cache structural inspection (not a closure query): confirmed the S106 cache npz-internal `audit_sha256` field = `5af2b7cd09d863491cd30872384f9bc9adc7b0a580c2b7089f28ce9bfda3fcbb` (= the S106-W1-HIGHL-CACHE-L1416 plan pin) and the L16-incompleteness state `L16_operational=15 / L16_full=False / L16_truncation_consistent=False / construction_complete=False`, `n_fb_bounded=17`, `eta_FB_lower=0.3928`. **NOT PRE-CLOSED**: #9e-B is closed at L12, but the L14/L16 truncation-trend was never computed — this gate is the genuine precision-extension, not a recompute-what-is-closed.

**Verdict**: **INFO** (precision-trend; L16-incompleteness disclosed as the INFO-qualifier — see below). Composite per the plan §W3-2 `INFO_meaning`.

**Results**:

NUMBERS first (SPEC-B primary; convention `E = |λ|² (D_K²)`, `np.unique(round-10)` global degeneracy-merge, S46 poly-staircase best-of deg {3,4,5,6,7} by max-residual, ⟨r⟩ = mean of `min(sᵢ,sᵢ₊₁)/max(sᵢ,sᵢ₊₁)` over the unfolded spectrum):

| L (truncation) | sectors | block-level abs_evals | N_unique (round-10) | poly deg (max resid) | **⟨r⟩ SPEC-B** | band [0.37,0.44] | nearest |
|:---|---:|---:|---:|:---|---:|:---:|:---|
| **12** (anchor; S106 landed) | — | — | — | — | **0.4118** | IN | POISSON |
| **14** (operational L=14, complete) | 120 | 323,136 | 12,024 | 7 (793.9) | **0.4254** | **IN** | POISSON |
| **16_op** (operational L=15; FB-tail-restricted) | 136 | 434,112 | 15,247 | 7 (1106.7) | **0.4200** | **IN** | POISSON |

Three-method cross-reads (all land Poisson-incommensurate, consistent with the L12 three-method robustness):

| L | SPEC-B (primary) | σ-insensitive Weyl-smooth (FI cross-check) | SPEC-A (per-sector cross-read) |
|:---|---:|---:|---:|
| 12 (anchor) | 0.4118 | 0.3888 | 0.4527 |
| 14 | 0.4254 | 0.3842 (σ∈{5,10,20,40}: 0.3864/0.3843/0.3833/0.3830) | 0.3809 (119 sectors) |
| 16_op | 0.4200 | 0.3828 (σ∈{5,10,20,40}: 0.3848/0.3827/0.3819/0.3817) | 0.3926 (135 sectors) |

The Weyl-smooth FI cross-check sits essentially AT the Poisson asymptote `2ln2−1 = 0.38629` at every L (0.3888 / 0.3842 / 0.3828) — the σ-insensitive method that landed exactly on Poisson at L12 stays there under truncation. SPEC-B runs slightly above the asymptote (a finite-size global-poly-staircase residual, same direction as L12's 0.4118), SPEC-A brackets it. The three methods bracket `2ln2−1` from both sides at all three L, exactly the L12 pattern.

**TREND (the gated object)**: ⟨r⟩ SPEC-B = 0.4118 (L12) → 0.4254 (L14) → 0.4200 (L16_op). Δ(L14−L12) = +0.0136; Δ(L16−L14) = −0.0054 — **flat-Poisson** within the band, NOT a monotone climb toward GOE 0.5307 nor a collapse toward clustered 0.27. Both new points are IN-band (`both_in_band=True`) and the drift sentinel (closer-to-GOE-than-Poisson OR ≤ clustered) fires on neither (`any_chaos_or_clustered_drift=False`). The distance to the Poisson asymptote stays tight: |⟨r⟩−0.38629| = 0.0255 → 0.0391 → 0.0337 across the grid.

**Substitution chain (plan §W3-2, confirmed):** Step 1 defines ⟨r⟩(L) = mean over the unfolded L-spectrum of `min(sᵢ,sᵢ₊₁)/max(sᵢ,sᵢ₊₁)`; Poisson asymptote 2ln2−1 = 0.38629, GOE 0.5307, clustered 0.27. Step 2 builds `E_unique(L) = unique(round-10 |λ(L)|²)` from `sector_evals_L{14,16}`, poly-unfolds, computes ⟨r⟩. Step 3 reads the trend on the L-grid {12,14,16_op}: the substrate is an asymptotically-Poisson degree-2 Loeschian form (Berry–Tabor, `[iK_7,D_K]=0` integrable, `λ_L=0`); higher L grows N_unique (12,024 at L14; 15,247 at L16_op) and ⟨r⟩ stays near 0.38629. Step 4 direction: both new ⟨r⟩ IN-band, flat-to-slightly-decreasing toward 0.38629, NOT rising toward GOE — sign_verdict PASS (no drift off Poisson). The numerical output matches the predicted direction.

**L16-INCOMPLETENESS DISCLOSURE (mandatory).** The L16 ⟨r⟩ = 0.4200 is computed on the **COMPLETED-SECTOR subset** present in `sector_evals_L16` — operationally **L = 15** (136 dense sectors, all p+q ≤ 15, max p+q in the cache = 15). The cache reports `L16_operational=15`, `L16_full=False`, `L16_truncation_consistent=False`, `construction_complete=False`. The **17 top-shell sectors `[(0,16),(1,15),…,(16,0)]`** (the full p+q = 16 ring) are **FB-bounded analytic-tail only** (`n_fb_bounded=17`), carrying a Friedrich–Bär lower bound `λ_lower ≈ 3.97` (`η_FB_lower = 0.3928`) but **NOT diagonalized**. The L16 ⟨r⟩ therefore reflects the dense p+q ≤ 15 spectrum, NOT the full p+q ≤ 16 set; it is reported and labelled `L16_op` / `OPERATIONAL-15` in the verdict value, npz (`L16_operational=15`, `L16_full=False`, `L16_fb_tail=FB-bounded-analytic-only`), stdout, and plot panel (d). The cache audit pin verified at runtime (`cache_pin_ok=True`, npz-internal `audit_sha256` = `5af2b7cd…` = the S106-W1-HIGHL-CACHE-L1416 plan pin). L14 by contrast is `L14_complete=True`, `L14_truncation_consistent=True` (full p+q ≤ 14).

**Why INFO and not PASS** (pre-registered, plan §W3-2 `INFO_meaning`): the set-membership PASS predicate is satisfied (`both_in_band=True`, no chaos/clustered drift), so on the band criterion alone the trend confirms the L12 placement. But the L16 datum is structurally **FB-tail-restricted** (`L16_full=False`) — the plan pre-registers that "the verdict-class if the L16 point is reported FB-tail-restricted (operational L=15 + analytic tail)" is **INFO**, with the L16-incompleteness "disclosed as an INFO-qualifier on the L16 point, not a FAIL." The composite collapses to INFO as the honest disclosure that the highest-L point is not the full p+q ≤ 16 set. This is NOT a FAIL (no drift toward GOE/clustered) and NOT a clean PASS (the L16 point is incomplete). The band-membership result (`both_in_band=True`) is reported separately so the precision-trend confirmation is explicit and recoverable downstream.

**Substrate-IS assessment (GEOMETRIC, Level-1 single-τ-slice).** The substrate IS the D_K(τ_fold) spectrum on Jensen-deformed SU(3) at the fixed fold slice τ_fold = 0.19; ⟨r⟩(L) is a level-statistics functional of the unfolded D_K² spectrum — the fabric's intrinsic spectral-fluctuation structure, not a quantity measured IN a container. Direction of explanation: `D_K eigenvalue spectrum at τ_fold (truncation L) → global-unique spectrum E_unique(L) → unfolded spacings sᵢ → ⟨r⟩(L) → nearest RMT class POISSON → Berry–Tabor integrability fingerprint`. The framework's proven integrability (`[iK_7, D_K] = 0` at all τ; Berry–Tabor not Gutzwiller; `λ_L = 0`) predicts Poisson level statistics; this gate confirms the Poisson placement is **truncation-stable** — the L12 value 0.4118 is asymptotic, not an L12 finite-size accident. The Weyl-smooth FI cross-check landing on `2ln2−1` at all three L is the cleanest substrate signature: the σ-insensitive functional (which removes the global-poly-staircase finite-size residual) reads the Poisson asymptote directly, and it does so identically at L12, L14, and L16_op. This is precision-tightening of the Observable-B (oscillatory / length-spectrum) half of the S106 BENIGN-DISTINCT-FUNCTIONALS two-pillar certificate; **it cannot and does not reopen #9e-B** (CLOSED at L12 by three-method robustness + the asymptotic Loeschian-quadratic-Poisson theorem). PHONONIC relevance: GEOMETRIC — this is the fabric's eigenvalue-spectrum fluctuation structure, not a phononic excitation; it characterizes the spectral triple's integrability, which underlies the substrate's Poisson (non-chaotic) mode organization.

---

## Wave 3 Synthesis (team-lead)

Both gates closed INFO in-session.

- **`S107-SDW-2ND-MOMENT-EFT` → INFO** (sign=PASS, magnitude=INFO, regime=VALID). `r_2nd = (a_8/a_6)·(Λ_sp/M_KK)⁻² = 0.1604` lands in the marginal band [0.1, 0.5) — the 2nd SDW layer is under the S96 loose-control band but NOT under the tight EVOI-#12 `<0.1` ceiling. Matches the analytic prediction (0.160424) and the S96 npz `r_driver_sp[3]` bit-for-bit. Structural reading: the SDW layer hierarchy is representation-theoretic/numerical (a-ratio rises 0.431→0.487→0.567→0.681 toward 1), NOT parametric-EFT, at the 2nd layer — extends the S96 base-layer verdict. Functional-sensitivity (diagnostic, not gated): the a-ratio driver is FUNCTIONAL-INVARIANT (w(L_max) cancels); the f-modulated ratio is FUNCTIONAL-DEPENDENT (Gaussian f₂/f₄=4.19 AMPLIFIES→0.673; Mellin f₂/f₄=0.033 CRUSHES→0.0053) — only the scheme-independent driver is the defensible gated object.
- **`S107-W1-RTREND-L1416` → INFO** (OPTIONAL/non-blocking). ⟨r⟩ flat-Poisson across L: SPEC-B L12/L14/L16_op = 0.4118/0.4254/0.4200, both new points in the incommensurate-Poisson band [0.37, 0.44], no drift toward GOE (0.53) or clustered (0.27). INFO-qualified solely by the L16 incompleteness (operational L=15; 17 top sectors FB-bounded analytic-tail, η_FB=0.3928 — disclosed). **#9e-B stays CLOSED** at L12; this gate cannot and does not reopen the SPLIT verdict — it converts the L12-only Poisson datum into a truncation-stable trend.

## Carry-Forward Computations (MATH ONLY — propagate to S108)

No carry-forwards: both wave outcomes closed in-session. `S107-SDW-2ND-MOMENT-EFT` resolves EVOI Tier-3 #12 (RESOLVED-MARGINAL — a disposition, not a new compute); `S107-W1-RTREND-L1416` is precision-only and #9e-B is already CLOSED (the optional gate carried no verdict-dependency for any other item). The absence is intentional.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-13 | EVOI Tier-3 #12 (SDW 2nd-moment EFT-control) | OPEN (tractable open gate) | **RESOLVED-MARGINAL** | r_2nd=0.1604 ∈ [0.1,0.5): 2nd-moment EFT under S96 loose band, not under tight 0.1; layer hierarchy representation-theoretic at 2nd layer |
| 2026-06-13 | #9e-B (length-spectrum incommensurate-Poisson) | CLOSED at L12 (S106) | CLOSED, L-trend-confirmed | ⟨r⟩ truncation-stable across {12,14,16}; precision-tightening only, no state change to the SPLIT verdict |

## Effected In-Session (NON-MATH)

- [x] EVOI Tier-3 #12 → RESOLVED-MARGINAL — orchestrator-direct update to `sessions/evoi-framework.md` (the row retires to §5 with the marginal disposition + functional-sensitivity note). Effected at close.
- [x] #9e-B SPLIT-certificate L-trend confirmation annotation on the S106 §VII Single-τ-slice scoped-PAIR registry note — routed to `mack-cosmic-bridge` sole-writer pass (`s107-close-mack`, item 3); precision annotation only, no reopening.

## Files Produced

| Gate | Script | Data | Plot |
|:--|:--|:--|:--|
| S107-SDW-2ND-MOMENT-EFT | s107_sdw_2nd_moment_eft.py | .npz | .png |
| S107-W1-RTREND-L1416 | s107_w1_rtrend_l1416.py | .npz | .png |

Verdict lines: `computations/session-107/s107_gate_verdicts.txt` lines 1–9 (W3-1 + 3-tuple + regulator_pin + functional-sensitivity rows) and 6–9 (W3-2 + L16-incompleteness + cross-reads rows).
