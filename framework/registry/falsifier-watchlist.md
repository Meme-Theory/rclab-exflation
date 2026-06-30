# Falsifier Watchlist — LRD-JWST-Analyst Live Observational Tests

**Registry ID**: `falsifier-watchlist`
**Owner agent(s)**: `little-red-dots-jwst-analyst` (primary), `mack-cosmic-bridge` (forecast liaison)
**Last updated**: `2026-06-06, S100b plan-freeze litreview anchor-currency batch (mack-cosmic-bridge)`
**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores rows as `open` entities (live tests = not yet verdict-resolved).

---

## Scope

The live observational tests the framework stakes predictions on — detectors, timelines, σ-distance from LCDM. Promoted from `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Live Observational Tests (AMRI-LIKELY per `computations/_agent_memory_inversion_audit.py` S85-W4 scan; all 4 flags fired including both formal AMRI tests: INPUT_PIN_TEST from §W4-4, OUTPUT_TARGET_TEST from §W4-8).

Consumer gates cite this file as the authoritative watchlist. This registry holds the **S58-established 6-channel LRD watchlist**. The **W4-introduced 5-channel CMB-S4 / DESI-DR3 / LiteBIRD / CMB-HD / 21-cm detector-correlation roster** is a distinct (related) registry produced by §W4-2 at `sessions/framework/correspondence/cross-channel-correlation-matrix.md`.

---

## Summary table

| Test | Framework prediction | Instrument | Data year | σ from LCDM | Status |
|:-----|:---------------------|:-----------|:----------|:------------|:-------|
| `w_0` | −0.918 (Volovik partition) | DESI DR3 | ~2027 | 2.9σ from DR2 | LIVE |
| `w_a` | ~0 (< 0.03) | DESI DR3 | ~2027 | near-constant DE | LIVE |
| `g_1/g_2` | 0.684 at τ=0.19 | RGE computation | S59+ | 3.5% below measured 0.709 | LIVE |
| `α_s` | TWO-SCALE (scale, channel): substrate-distance **−0.085 872 79** (`α_s_canonical = n_s_FW_exact² − 1`, s=3 Mellin, BZ-internal) / Goldstone-pivot **≈ 0** (`α_s_pivot_goldstone`, CMB-pivot leaf) | CMB-S4 2030 / CMB-HD 2035 (substrate value detector-facing via deg(T)=+2 NON-SCALAR relocation, atlas-09 Item-47 / S93-W7-1) | **13.99σ** vs Aiola+ 2020 ACT DR4 + Planck (+0.0023 ± 0.0063); 12.15σ vs Planck-2018 legacy | LIVE |
| `proton_lifetime` | ~10^36 yr | Hyper-K | ~2030s | one-parameter (M_KK) | LIVE |
| `H_0` | **67.40 km/s/Mpc** via the G_N-ratio channel (G_N^FW/G_N^obs = 1.000000; anchor-degeneracy disclosure — NOT anchor-independent H₀); spinor factor √16 = 4 RESOLVED S100a, magnitude RE-PINNED S101 W4-4 (65.4 RETIRED) | direct (ladder + CMB-ΛCDM + TDCOSMO lensing) + G_N-ratio channel | now | G_N-ratio channel (σ vs CMB anchor not computed — readout anchor-degenerate; anchor-independent H₀ = CF-S102) | LIVE — **FLAGSHIP** (S100a; re-pinned S101) |

---

## Entry detail

### `w_0` — dark-energy equation of state (zeroth moment)
- **Framework prediction**: −0.918 from Volovik partition
- **Detector**: DESI DR3 | **Data year**: ~2027
- **σ from LCDM**: 2.9σ from DR2 central (w_0 = −1.000)
- **Source**: S58 Volovik-partition derivation; `sessions/framework/registry/baseline-findings-s66.md`
- **Falsifier consequence**: null result (w_0 = −1.000 ± 0.015) closes the Volovik-partition branch at ~5σ

### `w_a` — dark-energy equation-of-state derivative
- **Framework prediction**: ~0 (bounded above by 0.03)
- **Detector**: DESI DR3 | **Data year**: ~2027
- **Interpretation**: framework predicts near-constant dark energy
- **Falsifier consequence**: |w_a| large falsifies near-constant-DE claim

### `g_1/g_2` — gauge-coupling ratio at τ=0.19
- **Framework prediction**: 0.684
- **Measurement target**: RGE running from M_Z
- **Observed**: 0.709 | **Tension**: 3.5% below observed — not yet decisive
- **Session anchor**: S59+

### `α_s` — scalar spectral-tilt running (TWO-SCALE)
- **Framework prediction (current canonical, two-scale per `phononic-framing.md §"Scale-and-channel-tagging"`)**: substrate-distance running **α_s_canonical = −0.085 872 79** (= `n_s_FW_exact² − 1` bit-exact, Sage-QQ; substrate-distance-1 Mellin pole s=3; the BZ-internal substrate-IS observable) AND Goldstone-pivot running **α_s_pivot_goldstone ≈ 0** (`P_{∇φ}=K⁰` at the CMB pivot; S92, NOT superseded). Which scale a detector measures is set by `deg(T_{BZ→pivot}) = +2 NON-SCALAR` (atlas-09 Item-47 / `S93-W7-1` PASS, formalized S103 W1-7) — the substrate value is detector-facing at CMB-S4/CMB-HD, NOT at the Planck pivot.
- **Detector**: CMB-S4 (primary, σ_α_s ≈ 2.3e-3) / CMB-HD (secondary, σ_α_s ≈ 1.1e-3) | **Data year**: ~2030 / ~2035
- **σ from LCDM**: substrate-distance value **13.99σ** vs the current canon (Aiola+ 2020 ACT DR4 + Planck, `+0.0023 ± 0.0063`); **12.15σ** vs Planck-2018 legacy (`−0.0045 ± 0.0067`). Both ≥ 5σ within CMB-S4 reach (≥ 30σ at CMB-HD) ⇒ FIRST multi-σ falsifier within near-term observational reach (inventory Row #3).
- **Falsifier consequence**: a CMB-S4 measurement confirming the Planck/ACT near-zero central (`≈ +0.0023 ± 0.0063`) falsifies the substrate-distance Route-B identity `α_s_canonical = n_s_FW_exact² − 1` at ≥ 13.99σ at projected precision (the §"CMB α_s discriminators" S90-CMB-S4 FAIL band fires at `|α_s_obs − α_s_canonical|/σ_obs > 5`; → Row #3 PERMANENT-WALL). The Goldstone-pivot leaf (≈0) is INSTEAD consistent with the near-zero pivot measurement (a measured ≈0 at the pivot is the EXPECTED Goldstone reading, NOT a falsification) — the two scales are graded on DIFFERENT channels.
- **PLAN-DRIFT historical note (dated 2026-06-10, S104 plan-freeze mack dispatch)**: this row PREVIOUSLY cited a pre-S85 single-scale value `−0.069 ± 0.008` at `6.0σ from Planck` with an `~8σ` null-falsifier consequence. That value (`alpha_s_inflation_framework = −0.068968`, the S50-51 `n_s² − 1` identity@observed-pivot with early `n_s ≈ 0.9649`) is **SUPERSEDED** (MCP `get_constant` → `Superseded: True`, "SUPERSEDED by the S92 two-observable scale/channel resolution; identity@observed-pivot, NOT a substrate-IS observable"). The summary-table and this entry-detail cell were re-pinned in-place to the current two-scale canonical this dispatch (the §"Post-W4 Unified Schema" `α_s` row and the §"CMB α_s discriminators" S90 landing already carried the current value; this fix removes the last live citation of the superseded `−0.069 ± 0.008` from the summary surface). The `−0.069` CMB-pivot-leaf is RETAINED elsewhere ONLY as the LQC cross-framework discriminator (inventory Row #74, capstone §7.2 #3-X) with explicit scale-and-channel tagging — that is a different (value, scheme) use, not this drift.

### `proton_lifetime`
- **Framework prediction**: ~10^36 yr
- **Detector**: Hyper-K | **Data year**: ~2030s
- **Parameter count**: one-parameter (M_KK)

### `H_0` — Hubble constant
- **Framework prediction**: **67.40 km/s/Mpc** via the G_N-ratio channel (G_N^FW/G_N^obs = 1.000000), WITH the anchor-degeneracy disclosure — this is a G_N prediction re-expressing the OBSERVED anchor by the ratio's deviation from 1, NOT an anchor-independent H₀; at deficit closure (N → 1) the readout degenerates to H_obs. Spinor-factor contingency DISCHARGED (√16 = 4 first-principles, `S100a-H0-SPINOR-FACTOR` PASS, audit `39abff2d…`; atlas-08 Q27 RESOLVED); magnitude RE-PINNED S101 W4-4 (`S101-H0-PROPER-A2` PASS, audit `cd8e8c0b125a…`; N = 0.999859, |N−1| = 1.4e-4 in ≤0.05 band). The 65.4 km/s/Mpc figure is RETIRED (S58 W3-16 prose projection — non-reproducible from any pinned chain artifact, displacement-sign-inverted vs the computed chain; only computed value 68.77 RETRACTED-S60).
- **Status**: LIVE — **FLAGSHIP** (promoted S100a per the pre-registered CONTINGENT → FLAGSHIP contract; magnitude re-pinned S101 W4-4; NON-PROMOTION-BY-HELD-NUMBER LIFTED)
- **σ-distances**: NOT computed against the 67.40 ratio-channel readout (the readout is anchor-degenerate with H_obs by construction); the prior 65.4-based σ-distances (3.59σ below Planck-ΛCDM 67.34 ± 0.54; 1.88σ below TDCOSMO-2025 71.6 on the lower bar) are SUPERSEDED — they were computed on the retired 65.4. An anchor-independent H₀ magnitude carrying σ-distances awaits `CF-S102-H0-ANCHOR-INDEPENDENT`.
- **Session anchor**: S58 W3-16 (prediction) / S100a W4-15 (factor grounding) / S101 W4-4 (magnitude re-pin)

---

## Consumer gates

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| `S85-W4-4-FALSIFIER-WATCH-CERT` | S85 | INPUT-PIN | Certifies every row has pinned σ_prediction + xcorr class + EVOI |
| `S85-W4-8-WATCHLIST-UPDATE` | S85 | OUTPUT-WRITER | Post-AMRI target: updates THIS file (replaces prior agent-memory target) |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-23 | S85-W4 AMRI | Initial migration from LRD agent memory | orchestrator |
| 2026-06-06 | S100b plan-freeze | S99-litreview anchor-currency annotations appended (§"S100b litreview anchor-currency annotations"): w_0/w_a post-Dovekie audit-pin (2.130σ canonical / 0.731σ branch-iv / w_a 3.429σ; 0.081σ Pantheon+ headline marked SUPERSEDED) + H_0 TDCOSMO-2025 (1.88σ lower-bar) / S100-H0-SPINOR-FACTOR-queue annotation; statuses UNCHANGED (H_0 stays LIVE-PENDING) | mack-cosmic-bridge |
| 2026-06-07 | S100b W1-3 | `S100b-WA-ROBUST` w_a robustness audit-pin appended (d_sigma = 2.946 INFO vs Planck-low-ell-independent combination; statuses UNCHANGED -- DR3 stays the binding instrument) | mack-cosmic-bridge |
| 2026-06-10 | S104 plan-freeze | §"S104 plan-freeze mack landings" appended (gem-triage §7-C): saddle-dominated-scrambling methodology guard (pairs S104 W3 KRYLOV-KCP); unified area-quantum WATCH (closed S89/S94 corridor, NEW LISA-echo context only, NOT a re-open, NOT two rows); two external-calibration notes (X(2370) 0⁻⁺ glueball long-horizon pin + g-2-is-now-lattice anti-stale). No status changes; no compute gates | mack-cosmic-bridge |
| 2026-06-10 | S104 plan-freeze | α_s PLAN-DRIFT repair (supersede-in-place): summary-table row 25 + entry-detail §"`α_s`" + Post-W4 Unified Schema `α_s` block re-pinned from the superseded single-scale `−0.069 ± 0.008` (and the intermediate `+0.00117`) to the current TWO-SCALE canonical — substrate-distance `−0.085 872 79` (s=3 Mellin) / Goldstone-pivot `≈0`; σ 6.0σ→**13.99σ** (Aiola ACT-DR4+Planck) / 12.15σ (Planck-legacy); deg(T)=+2 atlas-09 Item-47 scale/channel tag added. Stale value retained ONLY as dated PLAN-DRIFT history. Verified MCP `get_constant`: `alpha_s_inflation_framework` Superseded=True; `alpha_s_pivot_goldstone`=0.0 (S92, not superseded). No new prediction value; no compute gate | mack-cosmic-bridge |

---

## Migration notes

- Pre-migration path: `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Live Observational Tests
- AMRI tests fired: INPUT_PIN_TEST (§W4-4 line 357), OUTPUT_TARGET_TEST (§W4-8 line 711)
- Pointer installed in memory: `> See sessions/framework/registry/falsifier-watchlist.md (AMRI-promoted 2026-04-23; was § Live Observational Tests)`

---

## Post-W4 Unified Schema — S85-W4-8-WATCHLIST-UPDATE

**Gate**: `S85-W4-8-WATCHLIST-UPDATE` (appended 2026-04-23).

**Schema**: every row carries the 8-column unified format (`prediction, sigma_pred, detector, sigma_detect, sigma_distance, xcorr_class, evoi_class, fisher_sha`). Columns are populated by cross-reference with §W4-2 (cross-channel-correlation-matrix), §W4-4 (falsifier-watch-cert), §W4-6 (multi-d-jfd), §W4-7 (null-elim-map).

**Reframe note (2026-04-23)**: plan §W4-8 originally called for writing `project_watchlist-v85.md` INSIDE `.claude/agent-memory/little-red-dots-jwst-analyst/`. User directive flagged this as bad practice (project-level registry content does not belong in agent memory per `.claude/rules/agent-standards.md` §AMRI). This gate instead AUGMENTS the existing file (already AMRI-migrated earlier in S85-W4) with the §Post-W4 Unified Schema section below. Zero writes to agent memory.

### Per-row unified entries

#### `w_0`

- **prediction**: -0.918 (Volovik partition)
- **sigma_pred**: <pinned by S58 derivation; no published theory σ>
- **detector**: DESI DR3
- **sigma_detect**: 0.025 (DESI DR3 projected)
- **sigma_distance**: +3.28σ (framework above LCDM null w_0=-1.000; §W4-7)
- **xcorr_class**: PARTIALLY_CORRELATED with CMB-S4/CMB-HD α_s (§W4-2 pair (0,1), (1,3); r_d ladder)
- **evoi_class**: FLAGSHIP (binding falsifier; R_842 rectangle locked per S84-DR3-RESPONSE-PROTOCOL)
- **fisher_sha**: WARRANT-DEFERRED (DESI DR3 Fisher PDF pending)

#### `w_a`

- **prediction**: ~0 (< 0.03)
- **sigma_pred**: <pinned by S74 W4-Z framework>
- **detector**: DESI DR3
- **sigma_detect**: 0.10 (DESI DR3 projected)
- **sigma_distance**: ~0.3σ (framework near LCDM near-constant-DE null)
- **xcorr_class**: PARTIALLY_CORRELATED with w_0 (same instrument; ρ_w0_wa ≈ -0.85 DESI DR3 projection)
- **evoi_class**: FLAGSHIP-JOINT (evaluated jointly with w_0 in the CPL plane; S84-DR3-RESPONSE-PROTOCOL R_842)
- **fisher_sha**: WARRANT-DEFERRED (DESI DR3 Fisher PDF pending)

#### `g_1/g_2`

- **prediction**: 0.684 at τ=0.19
- **sigma_pred**: <pinned by S59+ RGE derivation>
- **detector**: RGE computation (not a detector)
- **sigma_detect**: N/A (no detector — comparison to PDG-derived 0.709)
- **sigma_distance**: 3.5% below observed 0.709 (NOT σ-distance; observational uncertainty on 0.709 dominates)
- **xcorr_class**: N/A (out of 5-channel detector roster)
- **evoi_class**: DERIVED (RGE-computed, not observational; evaluated against PDG measurement)
- **fisher_sha**: N/A (not a Fisher-paper channel)

#### `α_s`

- **prediction**: TWO-SCALE (current canonical, S89–S92 resolution) — substrate-distance **α_s_canonical = −0.085 872 79** (`n_s_FW_exact² − 1`, s=3 Mellin pole, Sage-QQ bit-exact, S89 W7a triple-verified) / Goldstone-pivot **α_s_pivot_goldstone ≈ 0** (CMB-pivot leaf, S92, NOT superseded). [PLAN-DRIFT history, re-pinned 2026-06-10 S104 plan-freeze mack dispatch: this field PREVIOUSLY cited `+0.00117` (S63 RUNNING-NS-63, S85 W1a-intermediate), and before that `−0.069 ± 0.008` (pre-S85). BOTH are superseded — `+0.00117` by the S89–S92 two-scale resolution (the §"CMB α_s discriminators" CF-33 landing supersedes the `+0.00117` reading explicitly, line ~184); `−0.069 ± 0.008` = `alpha_s_inflation_framework`, MCP `Superseded: True`. The summary table + entry-detail cells were re-pinned to this two-scale canonical the same dispatch.]
- **sigma_pred**: substrate-distance value is bit-exact (`−8587279/100000000`, Sage-QQ, no scheme-dependence — FI/zeta-invariant per inventory Row #3); Goldstone-pivot ≈0 is the Layer-1 topological-floor reading
- **detector**: CMB-S4 (primary, σ_α_s ≈ 2.1×10⁻³) + CMB-HD (secondary, σ_α_s ≈ 1.1×10⁻³); substrate value detector-facing via `deg(T_{BZ→pivot}) = +2 NON-SCALAR` (atlas-09 Item-47 / S93-W7-1)
- **sigma_detect**: 2.1×10⁻³ (CMB-S4); 1.1×10⁻³ (CMB-HD)
- **sigma_distance**: substrate-distance value **13.99σ** vs current canon (Aiola+ 2020 ACT DR4 + Planck `+0.0023 ± 0.0063`) / **12.15σ** vs Planck-2018 legacy (`−0.0045 ± 0.0067`); both ≥ 5σ within CMB-S4 reach, ≥ 30σ at CMB-HD (inventory Row #3). The Goldstone-pivot ≈0 leaf is consistent with the near-zero pivot measurement (graded on the DIFFERENT channel — the substrate value is the falsifier, the pivot leaf is the consistency reading)
- **xcorr_class**: COMMON_MODE between CMB-S4 and CMB-HD (§W4-2 pair (0,3) ρ=0.7); PARTIALLY_CORRELATED with DESI DR3 w_0
- **evoi_class**: FLAGSHIP (CMB-S4) / SECONDARY (CMB-HD redundant)
- **fisher_sha**: WARRANT-DEFERRED (CMB-S4 Science Book v2 + CMB-HD Sehgal 2019 Whitepaper Fisher PDFs pending)

#### `proton_lifetime`

- **prediction**: ~10³⁶ yr (one-parameter from M_KK)
- **sigma_pred**: <pinned by M_KK provenance>
- **detector**: Hyper-K (current); DUNE (future)
- **sigma_detect**: Hyper-K projected bound ~10³⁵ yr at 10-year exposure
- **sigma_distance**: one-sided lower-bound test (no σ-distance; rate-limit)
- **xcorr_class**: N/A (out of 5-channel detector roster)
- **evoi_class**: LONG-TERM (data window post-2030; not bound-decisive until Hyper-K Yr-10 or DUNE)
- **fisher_sha**: N/A (lifetime bound, not Fisher-parameter channel)

#### `H_0`

- **prediction**: **67.40 km/s/Mpc** via the G_N-ratio channel (G_N^FW/G_N^obs = 1.000000) WITH anchor-degeneracy disclosure (NOT anchor-independent H₀; degenerates to H_obs at N → 1). Factor = √16 = 4 EXACT (`spinor_norm_factor_FW = 4.0` canonical; `S100a-H0-SPINOR-FACTOR` PASS, audit `39abff2d275ce8b509b1312513560ffa6e1299995b3c3398e09b936713d51788`); magnitude RE-PINNED S101 W4-4 (`S101-H0-PROPER-A2` PASS, audit `cd8e8c0b125a64cf73debf8b9b7663e4389f0860159fc7cd524550674c983f22`; N = 0.999859, convergent local-SD route, neg-control divergence NOT reproduced). 65.4 RETIRED (non-reproducible prose projection, displacement-sign-inverted).
- **sigma_pred**: structural leg EXACT (factor √16 = 4 integer-mesh; rel to empirical 3.92 = 1/49 = 2.041%, the S59 PW-truncation residual); magnitude leg `|N − 1| = 1.4e-4` (357× inside the ≤0.05 band), G_N^FW/G_N^obs = 1.000000
- **detector**: direct (SH0ES + Planck joint; TDCOSMO lensing) + G_N-ratio channel
- **sigma_detect**: SH0ES σ ≈ 1.0; Planck σ ≈ 0.4; TDCOSMO-2025 (+3.9/−3.3)
- **sigma_distance**: NOT computed against the 67.40 ratio-channel readout (anchor-degenerate with H_obs); the prior 65.4-based figures (3.59σ below Planck-ΛCDM 67.34 ± 0.54; 1.88σ below TDCOSMO-2025; further below SH0ES 73.04) are SUPERSEDED (computed on the retired 65.4). Anchor-independent H₀ + σ-distances → `CF-S102-H0-ANCHOR-INDEPENDENT`.
- **xcorr_class**: N/A (out of 5-channel detector roster)
- **evoi_class**: **FLAGSHIP** (promoted S100a from CONTINGENT per this entry's own pre-registered contract; magnitude re-pinned S101 W4-4, NON-PROMOTION-BY-HELD-NUMBER LIFTED — EVOI rank-7b RESOLVED)
- **fisher_sha**: N/A

---

## CMB α_s discriminators (S90 W3 mack-cosmic-bridge live-watch)

> **Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the substrate's intrinsic Mellin running at substrate-distance-1 pole s=3 IS `α_s_canonical = n_s_FW_exact² − 1 = -8587279/100000000`. The CMB-S4 detector measures this quantity IN a laboratory-IN continuum container; the direction of explanation flows substrate → bridge map → laboratory observable per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`.

### S90-CMB-S4-ALPHA-S-DISCRIMINATOR-FORWARD-FALSIFIER

**Origin gate**: `S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING` (Wave-3 mack-cosmic-bridge sole-writer; CF-S90-MACK-2 / CF-33)

**Class**: forward-falsifier with quarterly poll cadence; model `S87-ALPHA-S-CMB-S4-WATCH` precedent (this CF-33 entry **SUPERSEDES** the legacy S87 watchlist polling discipline at the framework-current `α_s_canonical = -0.085 872 79` value, NOT the legacy `alpha_s_inflation_framework = -0.068968` Planck-2018-anchor value nor the intermediate `+0.00117` S63 RUNNING-NS-63 reading)

**Substrate prediction**: `α_s_canonical = -0.085 872 79` (= `-8587279/100000000` bit-exact in Q; `n_s_FW_exact² − 1` Route-B identity at substrate-distance-1 Mellin pole s=3; symbol pinned at `canonical_constants.py:n_s_FW_exact` per S88 W-15 W15-V.2 bit-exact rational pin; derived form is the substrate-IS Mellin observable on Pillar-VI inflationary scaling axis)

**Triple-verification SHA**: S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (Sage-QQ exact identity `n_s_FW_exact² − 1 ≡ α_s_canonical`)

**Joint hypersurface SHA**: S89 W4-4 `audit_sha256=e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` (joint (n_s, α_s) hypersurface lab-discrimination; Class-8.5 PRU 2D verdict-line value-field calibration instance #1)

**Laboratory anchor (current canonical)**: `α_s_canon_2020 = +0.0023 ± 0.0063` (Aiola+ 2020 ACT DR4 + Planck combined; canonical pin at `canonical_constants.py:alpha_s_canon_2020` per S86-W13 P12; supersedes Planck-2018 legacy `planck_alpha_s = -0.0045`)

**Trigger condition**: CMB-S4 inflation working-group publication with `σ_α_s ≤ 2.3 × 10⁻³` on the inflationary running of the scalar spectral index (NOT QCD `α_s(M_Z)`; the symbol overload is documented at the calibration-corpus instance landed via CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING`)

**PRDR Machinery Pin (4-element verifier rubric per Class 8.2 MANDATORY)**:

- **Pattern set** (lexical match against publication text):
  1. `(?i)\bCMB[-\s]?S[-\s]?4\b` AND `(?i)\b(alpha[-_]s|\\alpha_s|α[-_]s|running)\b` co-occurrence within 200-character window
  2. `(?i)\b(?:running of (?:the )?spectral index|scalar running|dn_?s/d ?ln ?k)\b` (semantic disambiguation: inflationary running, NOT QCD)
  3. `(?i)\bσ[\s_]?α[-_]?s\b` (uncertainty symbol; ASCII variants `sigma_alpha_s`, `sigma(alpha_s)`)
- **Disjunction-vs-conjunction declaration**: patterns 1 AND 2 in conjunction (rule: must be CMB-S4 AND must be inflationary α_s, not QCD α_s); pattern 3 disjunctive accept (any one form of the uncertainty symbol)
- **Negative-marker set** (auto-fail patterns; if matched, the publication does NOT trigger this watchlist row):
  1. `(?i)\bα[-_]?s\s*\([Mm][_\s]?[Zz]\)` (QCD `α_s(M_Z)` evaluation point; disambiguation per CF-36 corpus instance)
  2. `(?i)\b(?:strong coupling|QCD running)\b`
- **Exemplar SHA**: `<pinned at first-PASS-poll>` (reserved; populates at the first PASS poll publication event; until then carries the literal `<pinned at first-PASS-poll>` placeholder per Class 8.2 reserved-field discipline)

**PASS/INFO/FAIL bands** (against substrate prediction `α_s_canonical = -0.085 872 79`):
- **PASS** (substrate-consistent): `|α_s_obs − α_s_canonical| / σ_α_s,obs ≤ 2` (within 2σ of substrate prediction)
- **INFO** (marginal): `2 < |α_s_obs − α_s_canonical| / σ_α_s,obs ≤ 5` (mack-cosmic-bridge dispatches synthesis within 1 week)
- **FAIL** (falsified): `|α_s_obs − α_s_canonical| / σ_α_s,obs > 5` (5σ rejection of substrate-distance-1 Route-B identity; mack-cosmic-bridge dispatches falsification verdict within 24 hours; framework α_s axis flagged at `falsifier-master-inventory.md` Row #3 PERMANENT-WALL classification)

**Substitution chain for direction claim** (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1: α_s_canonical = -0.085 872 79             [substrate prediction; canonical pin via n_s_FW_exact² − 1]
Step 2: α_s_obs       = +0.0023 ± 0.0063         [current laboratory anchor; ACT DR4 + Planck combined]
Step 3: Δα_s          = α_s_obs − α_s_canonical
                      = 0.0023 − (−0.085 872 79)
                      = +0.088 172 79             [explicit substitution]
Step 4: |Δα_s| / σ_α_s,obs_current
                      = 0.088 172 79 / 0.0063
                      = 13.997...                 [≈ 14σ separation; substrate predicts FAR more negative running]
Step 5: At CMB-S4 projected σ_α_s = 2.3 × 10⁻³:
        Sub-case if α_s_S4 ≈ α_s_canon_2020 ≈ +0.0023:
          |Δα_s|/σ_S4 = 0.088172/0.0023 ≈ 38σ    [substrate FALSIFIED at 38σ; far beyond 5σ FAIL band]
        Sub-case if α_s_S4 ≈ α_s_canonical ≈ -0.0859:
          |Δα_s|/σ_S4 = 0/0.0023 = 0σ            [substrate CONFIRMED; PASS at < 2σ]
Direction: CMB-S4 will either CONFIRM substrate at very-near-zero σ OR FALSIFY at ~38σ; no middle ground at projected precision.
```

**Poll cadence**: quarterly (every 90 days); each poll runs the regex pattern set against the CMB-S4 inflation working-group publication stream (preprint feeds: arXiv astro-ph.CO; institutional preprint servers; CMB-S4 collaboration releases). Negative polls (no publication matches) log to `falsifier-watchlist.md` quarterly-poll-log subsection with timestamp + `<no-match>` status. Positive poll triggers fire mack-cosmic-bridge dispatch within 24 hours for FAIL band, 1 week for INFO band, 4 weeks for PASS band.

**Cross-links**:
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3 T7-W2-FALS-1 (CMB-S4 sign-test entry; **post-CF-29 audit-pin sub-row updated** at S90 W2 audit_sha256=`92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27`)
- `sessions/framework/registry/alpha-s-structural-protection.md` line 166 (CMB magnitude-test row; 25× below CMB-S4 1σ projection)
- `sessions/framework/registry/alpha-s-watchlist.md` (legacy S87-ALPHA-S-CMB-S4-WATCH polling discipline at +0.00117 RUNNING-NS-63 source; THIS CF-33 entry SUPERSEDES at framework-current `α_s_canonical = -0.085 872 79`)
- `.claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` Class 8.2 MANDATORY (4-element rubric specification structurally inherited)
- `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY for the `α_s_canonical` pin (derivative of `n_s_FW_exact` via Route-B identity; PRIMARY canonical is `n_s_FW_exact = Fraction(9561, 10000)` at `canonical_constants.py:n_s_FW_exact`)
- CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING` (Wave-3; calibration corpus instance for 3 distinct α_s symbols; documents QCD vs LEGACY inflationary vs BIT-EXACT inflationary axis distinction)

> **Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the LO α_s contribution IS the Route-B identity at substrate-distance-1 pole s=3 (`α_s_canonical_LO = -8587279/100000000`); the NLO ε² contribution IS the slow-roll second-order substrate correction at `eps_H_W6 = 0.02163` (canonical_constants.py:eps_H_W6). The CMB-HD detector measures the composite LO + NLO observable IN a laboratory-IN continuum container; the direction of explanation flows substrate → bridge map → laboratory observable per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`.

### S90-CMB-HD-ALPHA-S-NLO-EPS-SQUARED-DISCRIMINATOR

**Origin gate**: `S90-CMB-HD-ALPHA-S-NLO-WATCHLIST-LANDING` (Wave-3 mack-cosmic-bridge sole-writer; feynman-theorist CO-AUTHOR for NLO ε² substrate-side derivation cross-check; CF-S90-MACK-3 / CF-34)

**Class**: forward-falsifier with two-piece discrimination band (LO substrate-distance-1 pole + NLO ε² substrate slow-roll second-order)

**Substrate prediction — LO**: `α_s_canonical_LO = -0.085 872 79` (= `-8587279/100000000` bit-exact in Q; `n_s_FW_exact² − 1` Route-B identity at substrate-distance-1 Mellin pole s=3; symbol pinned at `canonical_constants.py:n_s_FW_exact`; S89 W7a triple-verified `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`)

**Substrate prediction — NLO ε² piece**: `ε²_NLO_piece` magnitude is `O(eps_H_W6²) ≈ (0.02163)² ≈ 4.679 × 10⁻⁴` (raw substrate slow-roll second-order); refined to `≈ 1.12σ` discrimination at projected CMB-HD precision per mack synthesis §VI.2 + feynman-theorist CO-AUTHOR cross-check (full substrate-second-order calculation; see W3 working paper §W3-2 sub-section §"feynman CO-AUTHOR verification note"). `eps_H_W6 = 0.02163` pin source: `canonical_constants.py:eps_H_W6` (slow-roll bound pinned from S80 dS/dtau at fold; used as NLO-margin cap in W6-70 field-expansion convergence + W6-69 F_amp^3PI FI chain). `n_s_FW_exact = Fraction(9561, 10000)` bit-exact rational pin: `canonical_constants.py:n_s_FW_exact` (S88 W-15 W15-V.2). **CRITICAL — bit-exactness firewall**: NLO ε² substrate-side derivation MUST NOT use legacy `alpha_s_inflation_framework = -0.068968` (canonical_constants.py:alpha_s_inflation_framework; Planck-2018-anchor DERIVATIVE form; superseded at S88 W-15 W15-V.2 by bit-exact pin per `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE).

**Composite substrate prediction**: `α_s_LO+NLO_substrate = α_s_canonical_LO + ε²_NLO_piece` (signed sum per slow-roll convention; LO dominates ≈ 80σ at projected CMB-HD precision; NLO contributes ≈ 1.12σ refined per mack synthesis §VI.2 — comparable to detector resolution; LO discrimination remains the headline)

**Laboratory anchor (current canonical)**: `α_s_canon_2020 = +0.0023 ± 0.0063` (Aiola+ 2020 ACT DR4 + Planck combined; canonical pin at `canonical_constants.py:alpha_s_canon_2020` per S86-W13 P12; supersedes Planck-2018 legacy `planck_alpha_s = -0.0045` at `canonical_constants.py:planck_alpha_s`)

**Trigger condition**: CMB-HD inflation working-group publication with `σ_α_s ≤ 1.1 × 10⁻³` on the inflationary running of the scalar spectral index (NOT QCD `α_s(M_Z)`; cross-link CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING` calibration corpus)

**PRDR Machinery Pin (4-element verifier rubric per Class 8.2 MANDATORY)**:

- **Pattern set** (lexical match against publication text):
  1. `(?i)\bCMB[-\s]?HD\b` AND `(?i)\b(alpha[-_]s|\\alpha_s|α[-_]s|running)\b` co-occurrence within 200-character window
  2. `(?i)\b(?:running of (?:the )?spectral index|scalar running|dn_?s/d ?ln ?k)\b` (semantic disambiguation: inflationary running, NOT QCD)
  3. `(?i)\bσ[\s_]?α[-_]?s\b` (uncertainty symbol; ASCII variants `sigma_alpha_s`, `sigma(alpha_s)`)
- **Disjunction-vs-conjunction declaration**: patterns 1 AND 2 in conjunction (rule: must be CMB-HD AND must be inflationary α_s, not QCD α_s); pattern 3 disjunctive accept (any one form of the uncertainty symbol)
- **Negative-marker set** (auto-fail patterns):
  1. `(?i)\bα[-_]?s\s*\([Mm][_\s]?[Zz]\)` (QCD `α_s(M_Z)` evaluation point; disambiguation per CF-36)
  2. `(?i)\b(?:strong coupling|QCD running)\b`
- **Exemplar SHA**: `<pinned at first-PASS-poll>` (reserved field; trigger event 2034+ first-data window)

**PASS/INFO/FAIL bands (LO + NLO composite)** (against substrate prediction `α_s_LO+NLO_substrate`):
- **PASS** (substrate-consistent): `|α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs ≤ 2`
- **INFO** (marginal): `2 < |α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs ≤ 5`
- **FAIL** (falsified): `|α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs > 5`

**PRDR Machinery Pin — NLO ε² sub-piece (Class 8.2 MANDATORY additional element)**:
- **NLO ε² magnitude pin**: feynman-theorist CO-AUTHOR-verified value at W3 working paper §W3-2 sub-section "feynman CO-AUTHOR verification note" (cited at watchlist landing); NLO contribution `≈ 1.12σ` at projected CMB-HD precision (refined from raw `O(eps_H_W6²) ≈ 4.679 × 10⁻⁴ / 1.1 × 10⁻³ ≈ 0.43` via full substrate-second-order calculation per mack synthesis §VI.2)
- **NLO ε² recompute trigger**: if `eps_H_W6` or `n_s_FW_exact` canonical pins change in a future `canonical_constants.py` update, the NLO ε² sub-piece MUST be recomputed; the watchlist row reserves a `nlo_eps_sq_provenance_sha` field cross-linking to the canonical_constants.py PROVENANCE entry

**Substitution chain — NLO ε² substrate-side direction** (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1: eps_H_W6 = 0.02163                                                  [slow-roll bound pin; canonical_constants.py:eps_H_W6]
Step 2: n_s_FW_exact = Fraction(9561, 10000)                                [bit-exact rational pin; canonical_constants.py:n_s_FW_exact]
Step 3: α_s_canonical_LO = n_s_FW_exact² − 1 = -8587279/100000000           [Route-B LO identity at substrate-distance-1 pole s=3]
Step 4: ε²_NLO_piece magnitude = O(eps_H_W6²) ≈ O((0.02163)²) ≈ O(4.679e-4) [slow-roll second-order; explicit form per feynman-theorist CO-AUTHOR]
Step 5: α_s_LO+NLO_substrate = α_s_canonical_LO + ε²_NLO_piece (sign per slow-roll convention; feynman verifies)
Step 6: At CMB-HD projected σ_α_s = 1.1 × 10⁻³:
        Raw substitution: ε²_NLO_piece / σ_CMB-HD ≈ 4.679e-4 / 1.1e-3 ≈ 0.43  [magnitude; order-1 ratio]
        mack synthesis §VI.2 refined: NLO discrimination ≈ 1.12σ              [full substrate-second-order]
Direction: NLO ε² sub-piece is comparable to CMB-HD detector resolution; LO discrimination (~80σ) dominates the headline; NLO is a CONFIRMATION test for substrate slow-roll second-order structure.

⚠️ DO NOT USE: legacy `alpha_s_inflation_framework = -0.068968` (canonical_constants.py:alpha_s_inflation_framework; Planck-2018 anchor DERIVATIVE; superseded at S88 W-15 W15-V.2 by bit-exact pin). Drift = -0.085872 − (-0.068968) = -0.016904 ≈ 15σ at projected CMB-HD precision — critical Planck-anchor-drift pathology if naively substituted in NLO chain.
```

**Poll cadence**: quarterly (every 90 days) for CMB-HD inflation WG publication stream until 2034+ first-data; on-deployment cadence escalates to monthly.

**Cross-links**:
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3 T7-W2-FALS-2 (CMB-HD magnitude-test row; updated post-CF-29 W2 at `audit_sha256=92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27`)
- `sessions/framework/registry/alpha-s-structural-protection.md` line 166 (CMB-HD 13× below 1σ projection)
- `canonical_constants.py:eps_H_W6 = 0.02163` (NLO ε² pin source; S80 dS/dtau at fold + S85 W9-2 W6-70 commit)
- `canonical_constants.py:n_s_FW_exact = Fraction(9561, 10000)` (LO Route-B identity source; S88 W-15 W15-V.2)
- `canonical_constants.py:alpha_s_inflation_framework = -0.068968` (LEGACY Planck-anchor pin; NOT to be used for NLO recompute)
- CF-33 `S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING` (S90 W3 sibling watchlist row; CMB-S4 LO-only at `audit_sha256=736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028`)
- CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING` (S90 W3 calibration corpus instance; documents 3 distinct α_s symbols)
- S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (LO bit-exact triple-verification)
- S89 W4-4 `audit_sha256=e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` (joint (n_s, α_s) hypersurface lab-discrimination; Class-8.5 PRU 2D verdict-line value-field calibration instance #1)

## 3He-B inheritance-falsifier liaison schedule (S90 W3 mack-cosmic-bridge live-watch + volovik CO-AUTHOR)

> **Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` with algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; the kernel of the inheritance morphism `ι : A_K → A_BdG = M_2(ℂ)` is `ker(ι_*) = M_3(ℂ)` (the substrate's SU(3)-coloured sector that does NOT inherit into the 3He-B BdG-restricted laboratory parent). The substrate's cocycle-asymmetry ratio `‖φ_67‖_BdG / ‖φ_88‖_BdG = 7.324992` IS the substrate's intrinsic Hochschild-pairing ratio between the chiral pair generator [φ_67] and the Cartan hypercharge generator [φ_88]; the 3He-B Aalto LTL apparatus measures this ratio IN a laboratory-IN superfluid container; the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5) guarantees the substrate-derived 7.324992 is preserved INTACT in the laboratory measurement, INDEPENDENT of the precise pressure-temperature operating point per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`.

### S90-3HE-B-AALTO-LTL-LIAISON-FORWARD-FALSIFIER

**Origin gate**: `S90-3HE-B-LIAISON-WATCHLIST-LANDING` (Wave-3 mack-cosmic-bridge sole-writer; volovik-superfluid-universe-theorist CO-AUTHOR cocycle-asymmetry verification; CF-S90-MACK-6 / CF-35)

**Class**: forward-falsifier with liaison-state poll cadence; pre-empts CMB-S4 α_s detector horizon by 2-3 years via earlier substrate-cleanliness measurement on a structurally orthogonal axis (3He-B BdG sector vs CMB observational running)

**Substrate prediction — Class A NULL (decisive triplet)**: NULL kernel-signature on F1 + F2 + F5 falsifier rows per `.claude/rules/inheritance-falsifier-protocol.md §"Class A — Kernel-Signature Test"`; substrate predicts NO signal under BDI parent-symmetry protection on the φ_67 chiral-pair generator (rows F1 = Caroli-Matricon ladder asymmetry; F2 = polar-vortex line asymmetry; F5 = µSR knight-shift asymmetry).

**Substrate prediction — Class B cocycle ratio**: `substrate_cocycle_ratio_67_88 = 7.324992` (Sage-QQ exact at machine precision; equivalent rational `114453/15625` in Q; canonical_constants.py:substrate_cocycle_ratio_67_88 line 276 per S86 W-5 R2-B Convergence #3; PROVENANCE entry at line 1191); preserved INTACT in lab measurement under (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5 machine-precision Python verification at 0.0e+00 residual); volovik-superfluid-universe-theorist CO-AUTHOR verified at W3 working paper §W3-3 sub-section "volovik CO-AUTHOR verification note".

**Substrate prediction — Class A NULL (supporting pair)**: NULL kernel-signature on F3 + F4 falsifier rows (F3 = NMR/EPR g-factor asymmetry; F4 = thermal-conductivity anisotropy on chiral-pair vs Cartan generator)

**Substrate prediction — Class B slope discrimination**: F4 multi-pressure slope (Jacobi-cubic vs φ_88-linear) over 0–34 bar pressure scan; substrate predicts Jacobi-cubic slope from φ_67-chiral-pair-dominated thermal-conductivity anisotropy, NOT φ_88-linear from Cartan-hypercharge generator alone.

**Cocycle norm pins (S86 W-5 C2)**:
- `cocycle_norm_phi67 = 0.793346 M_KK²` (canonical_constants.py:cocycle_norm_phi67 line 274; `‖φ_67‖² = δE_6 · δE_7`)
- `cocycle_norm_phi88 = 0.108307 M_KK²` (canonical_constants.py:cocycle_norm_phi88 line 275; `‖φ_88‖² = (δE_8)²`; Jensen-rate-limited at τ_fold=0.19)
- Ratio: `cocycle_norm_phi67 / cocycle_norm_phi88 = 0.793346 / 0.108307 = 7.324992` (Sage-QQ exact = `114453/15625`)

**Laboratory anchor**: 3He-B Aalto LTL apparatus (Helsinki ROTA cells variant; alternate: Lancaster MCT-3); BDI-protected B-phase under (p, T) operating point near polycritical pressure (`P_pc ≈ 21.22 bar, T_pc ≈ 2.273 mK` per `aalto-ltl-multi-session-protocol.md`)

**Liaison schedule (5-element pre-registration)**:
  1. **Q4 2026 first-contact deadline**: mack-cosmic-bridge sends introductory liaison email to Aalto LTL leadership (Vlasov / Krusius successor team; cross-link to S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION INFO record at `s88_gate_verdicts.txt` for groups roster Krusius + Tuoriniemi + Eltsov, A=26+B=38+C=26 lab counts) citing S87 W2-1 paper artifact + substrate prediction structural protection at `7.324992 ± 0.1%` (NOT 7.3250 round form per mnemonic-vs-exact discipline)
  2. **2-3 year program duration**: experimental program 2026 Q4 → 2029 Q4 (3-year window) for full deployment of Gates 1-4
  3. **Feasibility window 2028-2029**: first publishable data targeted for 2028 Q4 - 2029 Q4; pre-empts CMB-S4 first-data 2028+ by parallel timeline AND CMB-HD first-data 2034+ by 5-6 years (cross-link CF-33 + CF-34 sibling watchlist rows)
  4. **4-gate falsifier protocol deployment** (per `.claude/rules/inheritance-falsifier-protocol.md §"Four-Gate Structure"`):
     - Gate 1: kernel-signature NULL on F1 (Caroli-Matricon ladder asymmetry; φ_67-clean) + F2 (polar-vortex line) + F5 (µSR knight-shift) — decisive triplet
     - Gate 2: cohomology-asymmetry ratio prediction `7.3250 ± 0.1%` (substrate-falsifying; Sage-exact 7.324992; mnemonic-vs-exact discipline cite the 7.324992 Sage-exact form, not the round 7.3250)
     - Gate 3: kernel-signature NULL on F3 (NMR/EPR g-factor) + F4 (thermal anisotropy) — supporting pair
     - Gate 4: F4 multi-pressure slope discrimination (Jacobi-cubic vs φ_88-linear over 0–34 bar)
  5. **Cross-links to substrate-side derivation**:
     - S87 W2-1 paper artifact: `papers/s87-3he-b-alpha-s-equivalent.md` (audit_sha prefix `1f38f9888538011c…`)
     - S89 W4-3 3He-B related INFO verdict: audit_sha prefix `5da87779e18e8174…`
     - S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION INFO record: `s88_gate_verdicts.txt` (protocol pre-registered with substrate_ratio=7.324992; A=26+B=38+C=26 lab counts; Krusius+Tuoriniemi+Eltsov groups; horizon S88→S100+ at 2027-2032 lab years; rows 45+46) — cross-link discovery via MCP knowledge index, not in plan §6 cross-link list
     - `.claude/rules/inheritance-falsifier-protocol.md §"Calibration corpus"` S86 W-5 W11-C5 (3He-B vortex-core spectroscopy) + W11-C6 (3He-A µSR)
     - `.claude/rules/cross-pillar-bridge-anatomy.md §VII.W-3.LAB STAGE-1-CANDIDATE` (S88 W4a-17 calibration corpus instance #3; post-CF-21 OE-form retrofit)
     - `sessions/framework/registry/falsifier-master-inventory.md` Row #5 T7-W2-FALS-5 (3He-B Aalto LTL row)
     - `atlas-07-permanent-results §VII.AB.8` (multi-year Aalto LTL liaison CANDIDATE-PENDING; 5-yr horizon 2031)

**PRDR Machinery Pin (4-element verifier rubric per Class 8.2 MANDATORY)**:

- **Pattern set** (liaison-state poll patterns):
  1. `(?i)\b(Aalto|LTL|Low Temperature Lab|Helsinki ROTA|Lancaster MCT-?3?)\b` AND `(?i)\b(3-?He-?B|³He-B|3He B-phase|superfluid helium-3 B-phase)\b` co-occurrence (institution AND substrate)
  2. `(?i)\b(?:Caroli[-\s]Matricon|vortex[-\s]core spectroscopy|µSR|muon spin (?:rotation|resonance))\b` (apparatus-specific lexical markers)
  3. `(?i)\b(?:cocycle|inheritance morphism|kernel signature|BdG asymmetry)\b` (theoretical lexical markers)
- **Disjunction-vs-conjunction declaration**: pattern 1 conjunction (institution AND substrate); pattern 2 disjunctive (any apparatus); pattern 3 disjunctive accept (any theoretical marker; for liaison-state poll completeness signal)
- **Negative-marker set** (auto-fail patterns):
  1. `(?i)\b3He-?A\b(?!.*B)` (3He-A only without B-phase content; wrong superfluid phase)
  2. `(?i)\b(?:superconductor|3He superfluid bulk)\b(?!.*BdG)` (bulk superfluidity without BdG-restriction; wrong sector)
- **Exemplar SHA**: `<pinned at first-publication-poll>` (reserved field; trigger event 2028 Q4 first publishable data)

**PASS/INFO/FAIL bands (Gates 1-4 conjunction)**:
- **PASS** (substrate-consistent): Gates 1+2+3 all return NULL on F1+F2+F5+F3+F4 AND Gate 2 cocycle-ratio measurement `|R_lab / 7.324992 − 1| ≤ 0.001` (0.1% RATIO tolerance per `.claude/rules/inheritance-falsifier-protocol.md §"Four-Gate Structure"` Gate 2 + cross-pillar bridge K=B 0.1%) AND Gate 4 slope matches Jacobi-cubic prediction (NOT φ_88-linear) over 0–34 bar
- **INFO** (marginal): Gate 1 OR Gate 3 returns ambiguous signal at rows F1/F2/F5 OR F3/F4 OR Gate 2 ratio agrees within 0.1% < tolerance ≤ 1% OR Gate 4 slope discrimination ambiguous
- **FAIL** (falsified): Gate 1 returns non-NULL on any of F1+F2+F5 OR Gate 2 ratio diverges from 7.324992 by > 1% OR Gate 4 slope matches φ_88-linear (excludes substrate's chiral-pair structural protection)

**Substitution chain for substrate-side cocycle-asymmetry direction** (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"` + `.claude/rules/math-scripts.md §"Mnemonic-vs-exact ratio discipline"`):

```
Step 1: cocycle_norm_phi67 = 0.793346 M_KK²                                 [S86 W-5 C2 pin; canonical_constants.py line 274; substrate spectral triple kernel structure; ‖φ_67‖² = δE_6 · δE_7]
Step 2: cocycle_norm_phi88 = 0.108307 M_KK²                                 [S86 W-5 C2 pin; canonical_constants.py line 275; Cartan hypercharge generator; ‖φ_88‖² = (δE_8)²]
Step 3: substrate_cocycle_ratio_67_88 = cocycle_norm_phi67 / cocycle_norm_phi88
                                       = 0.793346 / 0.108307
                                       = 7.324992                            [Sage-QQ exact at machine precision; equivalent rational 114453/15625 in Q]
Step 4: (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5):
        lab(F_i) / lab(F_j) = ‖φ_a‖ / ‖φ_b‖ × (f_i / f_j)
        for common exponents p_i = p_j = p
        ⇒ R_lab_measured = substrate_cocycle_ratio_67_88 = 7.324992          [preserved INTACT under common p; machine-precision Python verification at 0.0e+00 residual]
Step 5: PASS band: |R_lab_measured / 7.324992 − 1| ≤ 0.001                  [Class B 0.1% RATIO per inheritance-falsifier-protocol.md Gate 2]
Direction: substrate predicts the 3He-B Aalto LTL apparatus will measure R_lab = 7.324992 ± 0.1% IF AND ONLY IF substrate's chiral-pair-vs-Cartan structural protection is correct; ANY divergence > 0.1% FALSIFIES substrate.

⚠️ Mnemonic-vs-exact discipline: cite 7.324992 (Sage-exact = 114453/15625 in Q), NOT 7.3250 (round form); per `.claude/rules/math-scripts.md §"Mnemonic-vs-exact ratio discipline"` S86 W-3 RULE-3, mnemonic forms understate or overstate structural ratios. The Gate 2 description carries 7.3250 as a SHORTHAND but the canonical reference value is the Sage-exact 7.324992 form.
```

**Poll cadence**: quarterly (every 90 days) liaison-state poll between mack-cosmic-bridge and Aalto LTL contact + publication-stream regex polling for 3He-B BdG cocycle-asymmetry preprints; escalates to monthly during 2028-2029 deployment window.

**Cross-links**:
- `sessions/framework/registry/falsifier-master-inventory.md` Row #5 T7-W2-FALS-5 (3He-B Aalto LTL row; post-CF-21 OE-form retrofit will update Element 2 from PROSE to `Π^{vortex}_{B-phase}` / `Π^{µSR}_{A-phase}` regex per S88 W7a-73 K=2 MANDATORY)
- `.claude/rules/inheritance-falsifier-protocol.md §"Four-Gate Structure"` (4-gate template; W11-C5/C6 calibration)
- `.claude/rules/cross-pillar-bridge-anatomy.md §VII.W-3.LAB STAGE-1-CANDIDATE` (S88 W4a-17 calibration corpus #3; cross-pillar-bridge anatomy K=3 MANDATORY)
- canonical_constants.py PROVENANCE lines 1185, 1188, 1191 (`cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`; S86 W-5 pins)
- S87 W2-1 paper artifact: `papers/s87-3he-b-alpha-s-equivalent.md` (audit prefix `1f38f9888538011c…`)
- S89 W4-3 INFO verdict: audit prefix `5da87779e18e8174…`
- S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION INFO record (MCP-discovered; not in plan §6 cross-link list): `s88_gate_verdicts.txt` (substrate_ratio=7.324992; groups Krusius+Tuoriniemi+Eltsov; horizon S88→S100+ at 2027-2032 lab years; rows 45+46)
- `aalto-ltl-multi-session-protocol.md` (multi-session protocol reference; polycritical anchor P_pc=21.22 bar, T_pc=2.273 mK)
- Wave-3 sibling watchlist rows: CF-33 CMB-S4 (audit `736178083caa51c0…`) + CF-34 CMB-HD (audit `be1e362c5db63e73…`)
- S89 W7a Sage-QQ exact triple-verification: `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (LO α_s axis cross-reference; same Sage-QQ machine-precision discipline)
- S89 W4-4 joint hypersurface (Class-8.5 PRU 2D verdict-line value-field calibration): `e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89`
- CF-29 S90 W2 falsifier-master-inventory Row #3 update (sibling axis): `92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27`


## S100b litreview anchor-currency annotations (S99 litreview campaign → S100b plan-freeze; mack-cosmic-bridge sole-writer)

> **Origin**: S99 litreview campaign G2 dark-energy sweep (`sessions/archive/session-99/session-99-litrev-dark-energy-mack.md` §II.2 + §II.6; `…-dark-energy-sagan.md` σ-distance correction; consolidation `session-99-litreview-consolidated-gen-physicist.md` §II G2-3 + §V hygiene-routing). Append-only audit-pin sub-entries on the EXISTING `w_0` / `w_a` / `H_0` rows above — NO value changes, NO status changes (H_0 stays LIVE-PENDING), NO verdict lines (the review campaign produced reports only; the canonical write-order does not apply — no new framework prediction value).

### w_0 / w_a — post-Dovekie anchor-currency audit-pin (supplements the DR2-era σ-figures above)

- The summary-table + entry-detail + unified-schema `w_0` figures above ("2.9σ from DR2", "+3.28σ vs the LCDM null") and the `w_a` "~0.3σ vs the near-constant-DE null" are DR2-era σ-from-LCDM-null readings — historical, PRESERVED VERBATIM above. The registry-live EXTERNAL anchor has moved to **post-Dovekie 2026** (Popovic et al., arXiv:2511.07517v3 — DES-Dovekie SN + DESI DR2 BAO + Planck/ACT/SPT joint Flat w₀wₐCDM: w_0 = −0.803 ± 0.054, w_a = −0.72 ± 0.21, ρ(w_0, w_a) ≈ −0.85).
- **Post-Dovekie measured-central σ-distances** (source of record: `falsifier-master-inventory.md` Row #1.dovekie-2026-update, S88 W5; atlas-08 Q37 / Window-14 cited for consistency — atlas-08 NOT edited here): canonical `w0_FW = −0.918` → **2.130σ**; branch-(iv) `w0_FW_R842 = −0.842454` → **0.731σ**; `w_a = 0` four-fold lock → **3.429σ** (tension ADVANCED; Atlas D04 C5 = BROKEN — the framework's live wager).
- **Superseded-headline guard (anchor-currency)**: the **0.081σ** "R_842 vs DR2 Pantheon+ (−0.838 ± 0.055)" coincidence is the historically-tightest but SUPERSEDED comparison — do NOT cite it as the live state (S99 litrev G2-3, both reports CONVERGENT on the anchor-currency flag). The binding anchor is post-Dovekie; the binding INSTRUMENT remains DESI DR3 (window-open 2026-04-23 with hard lockouts A–F; data-release 2027; the R_842 binding event is NOT triggered by any SN reanalysis on DR2 BAO).
- **Branch-resolution guard**: the w_0 branch choice (canonical −0.918 vs R_842 −0.842454) must be resolved on INDEPENDENT geometric grounds (`w0-primary-decision-rule.md`; consolidation G2-3, S101-plan routed). Until then the 0.731σ branch-(iv) proximity is NOT scored as a PASS — branch-shopping guard.

### H_0 — LIVE-PENDING contingency + TDCOSMO-2025 anchor audit-pin

- **Status UNCHANGED: LIVE-PENDING.** H_0 = 65.4 km/s/Mpc is CONTINGENT on the √16 spinor-factor resolution (atlas-08 Q27 / Window-19, structurally unresolved since S58 — the "unresolved through S85" wording above extends through S99). The S99 litreview INDEX over-stated 65.4 as a firm prediction; THIS watchlist's contingency framing is the correct register (litrev G2 §II.6 honesty correction — both G2 reports flag it).
- **First-principles resolution QUEUED**: gate `S100-H0-SPINOR-FACTOR` (S100a plan, W4) — derives the spinor normalization √16 = 4 from the d_spec=8 16-component spinor (Tr = 16) vs the empirical 3.92 (rel ≈ 2.04%). On resolution, `evoi_class` CONTINGENT → FLAGSHIP per the unified entry above.
- **New external anchor (annotation only — nothing becomes binding while LIVE-PENDING)**: TDCOSMO-2025 H_0 = **71.6 (+3.9/−3.3)** km/s/Mpc (mass-sheet-degeneracy-marginalized, blinded; litrev G2 paper 08). 65.4 sits **1.88σ below** on the relevant lower error bar ((71.6 − 65.4)/3.3 = 1.879; 1.59σ on the +3.9 upper bar) — NOT excluded, but the central value pulls away from 65.4. Against the Planck-anchored DESI+CMB ΛCDM H_0 = 67.34 ± 0.54: **3.59σ below** — the framework's most exposed Hubble-sector claim (it predicts BELOW the CMB anchor, on neither side of the standard Hubble tension). σ-distances Sage-verified in the G2 source report (`…-litrev-dark-energy-mack.md` §II.6; sagan's lower-bar 1.88σ correction adopted).
- **RESOLVED S100a — the queued gate DELIVERED; FLAGSHIP promotion FIRES (mack-cosmic-bridge sole-writer landing, 2026-06-06).** `S100a-H0-SPINOR-FACTOR` PASS (`audit_sha256=39abff2d275ce8b509b1312513560ffa6e1299995b3c3398e09b936713d51788`, `content_sha256=e6928cadd8929c6229abb2ba4774a61a834f23db512cd7ebc780688b22e90296`, verdict line 49 of `computations/session-100a/s100a_gate_verdicts.txt`): the empirical spinor factor 3.92 derives first-principles as **√16 = 4 EXACT** — `Tr_spinor = 2^⌊8/2⌋ = 16` (Clifford(ℝ⁸); `Res_{s=8} ζ_D` carries the 16, S87) × the surviving 4-of-64 Δ₁₂ block (Route D, S58), `√(4/64) = 1/4` exact; Sakharov induced-gravity cross-reading gives the same factor. Agreement `rel = 1/49 = 2.041% ≤ 2.5%` (Class-8.3 publication-precision-floored boundary; the empirical anchor is 3 sig figs); the 2% residual is the S59 PW-truncation deficit (implied a₂ deficit 99/2500 = 3.96% vs S59 measured ~4.1%, scale AND sign match — 3.92 converges TOWARD 4 as truncation lifts). atlas-08 Q27 **RESOLVED**; `spinor_norm_factor_FW = 4.0` canonical. **Per the pre-registered contract above: status LIVE-PENDING → LIVE; `evoi_class` CONTINGENT → FLAGSHIP** (summary table + entry detail + unified entry updated this batch). The TDCOSMO-2025 (1.88σ below, lower bar) and Planck-anchored ΛCDM (3.59σ below) σ-distances in the preceding bullet are NO LONGER annotation-only — they are the LIVE FLAGSHIP watch anchors: H₀ = 65.4 km/s/Mpc is now a structurally-grounded prediction sitting BELOW the CMB anchor, on neither side of the standard Hubble tension — the framework's sharpest now-data-exposed Hubble-sector claim. Companion landings same batch: capstone §7.2 row #10 + `falsifier-master-inventory.md` Row #81.

> **SUPERSEDED by the S101 W4-4 re-pin (2026-06-08) — this 2026-06-06 dated record is preserved as the S100a-era state; it is NOT the live prediction.** The convergent-route recompute `S101-H0-PROPER-A2` (PASS, audit `cd8e8c0b125a64cf73debf8b9b7663e4389f0860159fc7cd524550674c983f22`) RE-PINNED the value: the published 65.4 is RETIRED (non-reproducible from any pinned chain artifact + displacement-sign-inverted vs the computed chain; the only computed value 68.77 is RETRACTED-S60). The live H₀ row above (summary table + entry detail + unified schema, all updated S101 W6-9) reads **67.40 km/s/Mpc via the G_N-ratio channel** (G_N^FW/G_N^obs = 1.000000, N = 0.999859) WITH the anchor-degeneracy disclosure — a G_N prediction, NOT an anchor-independent H₀. The 65.4-based σ-distances in this dated block (3.59σ / 1.88σ) are SUPERSEDED (computed on the retired 65.4). NON-PROMOTION-BY-HELD-NUMBER LIFTED; anchor-independent H₀ → `CF-S102-H0-ANCHOR-INDEPENDENT`.

---

## S100b W1-3 w_a robustness audit-pin (S100b-WA-ROBUST)

#### `w_a (Planck-low-ell-independent)` -- S100b-WA-ROBUST audit-pin

- **What**: the four-fold lock w_a = 0 (S58) scored against the Planck-low-ell-INDEPENDENT
  combination (compressed Planck+ACT geometric CMB + DESI DR2 BAO + Pantheon+) -- the
  combination free of the three DDE-signal localizations (SN photometric offset, Planck
  ell<~30 anomaly, single z~0.7 H(z) bump).
- **Result**: w_a(robust) = -0.7970 +0.2705/-0.2808 => d_sigma = 2.946
  (INFO; sigma_gov = toward-zero bar) vs canonical baselines 2.92 (DR2-marginalized) /
  3.74 (DESY5-joint) / 2.82 (PP-joint). Route-B published anchors (Giare Tab. II):
  ACT+WMAP 2.136 sigma; SPT+WMAP 1.160 sigma.
- **Sagan caveat (pre-registered)**: w_a = 0 is a NULL that LCDM shares -- survival earns
  FALSIFICATION-SURVIVAL only, NO Bayesian credit over LCDM; the discriminating quantity is
  w_0 at fixed w_a = 0 (W1-4 + DESI DR3 R_842).
- **Status impact**: `w_a` row stays LIVE; DR3 remains the binding instrument (R_842,
  S84-DR3-RESPONSE-PROTOCOL). This sub-row is the master-inventory `1.wa-robust-s100b` mirror.
- **Provenance**: gate `S100b-WA-ROBUST` (INFO), audit `15c54621f59184cc` / content `077dc843babcc59c`
  (full 64-hex in computations/session-100b/s100b_gate_verdicts.txt);
  data computations/session-100b/s100b_wa_robust.npz.

---

## S102 W7-1 post-fold-tail resonance ABUNDANCE-BENIGN annotation (mack-cosmic-bridge sole-writer; W7→W8 decision-point Item-30 PASS-branch routing)

#### post-fold-tail live resonance — ABUNDANCE-BENIGN (CF-S102-OQ5-RECTIFIED-DRIVE PASS)

- **What**: the post-fold-tail live resonance (the late-time rectified-drive channel raised at
  open-question OQ5) was tested at the ABUNDANCE level: does the post-fold-tail resonant drive
  contribute a relic abundance above the budget?
- **Result**: `R_rect = 1.271486e-06 ≪ 0.05` budget (margin 3.93e4 = budget/R_rect). The
  post-fold-tail resonance is **ABUNDANCE-BENIGN** — the rectified-drive contribution is ~5 OOM
  below the 0.05 abundance budget. The clause-(d) coincidence-bound demotion **STANDS at the
  abundance level**: the resonance is a real substrate feature but its relic-abundance imprint is
  negligible, so it does not promote to a falsifier row.
- **Status impact**: NO new falsifier row; the post-fold-tail resonance is recorded here as
  ABUNDANCE-BENIGN (live-watch annotation only). The atlas-08 reconciliation of OQ5 lands at
  S103 plan-time (NOT this gate's surface — the watchlist annotation is the mack sole-writer
  surface; the atlas-08 open-question reconciliation is a separate S103 plan-time action).
- **Substrate framing (PHONONIC)**: the post-fold-tail resonance IS a residual spectral feature
  of the D_K spectrum post-transit (read FORWARD from the eigenvalue reorganization at the fold);
  its abundance image under the relic-projection is 5 OOM below budget, so the substrate feature
  is genuine but observationally benign at the abundance channel.
- **Provenance**: gate `W7-1` (`CF-S102-OQ5-RECTIFIED-DRIVE`) PASS, audit `f30c6a4a…`
  (W7-1 PASS; full 64-hex in computations/session-102/s102_gate_verdicts.txt); routed per
  `sessions/session-plan/session-102-plan-w7.md §"Wave 7 → Wave 8 Decision Point"` Item-30 PASS
  branch ("record in atlas-08 / falsifier-watchlist"). The falsifier-watchlist surface is the
  mack sole-writer leg; the atlas-08 OQ5 reconciliation is deferred to S103 plan-time.

---

## S104 plan-freeze mack-cosmic-bridge landings (2026-06-10; gem-triage §7-C routing)

> **Origin**: S104 plan-time maintenance dispatch routed from `/rclab-plan` Phase 1c-REGISTERS, consuming `downloads/research-sweep-s103/GEM-TRIAGE.md §7-C`. These are WATCH-surface / methodology-guard / external-calibration annotations only — NO compute gates, NO new prediction values, NO status changes to any LIVE row above. Each item dated 2026-06-10 so the S104 session-close capstone-hygiene Q1–Q5 block can cite this dispatch.

### S104-SADDLE-SCRAMBLING-GUARD — standing methodology guard on any future fold OTOC/Lyapunov/Krylov-growth claim

> **Substrate framing (PHONONIC)**: the van Hove fold (τ_fold = 0.190) IS an A₂-catastrophe saddle in the substrate's order-parameter phase space (read FORWARD from the D_K eigenvalue reorganization at the fold); apparent "scrambling" at a saddle is a property of the SADDLE GEOMETRY, not of genuine spectral chaos. The substrate's spectrum is PROVEN Poisson (CG(24) ⟨r⟩ = 0.367, integrable; verified `search_knowledge` this dispatch) and its OTOC is PROVEN sub-exponential (`C(t) ~ t^1.9, no Lyapunov exponent, λ_L = 0`, S38, PROVEN; verified this dispatch).

**Guard (interpretive, NOT a compute gate)**: Bhattacharjee+ (arXiv 2203.03534) prove that INTEGRABLE systems with unstable phase-space saddles produce LINEAR Lanczos-coefficient growth + exponential early-time Krylov/OTOC growth — the textbook chaos signature — entirely as a SADDLE ARTIFACT, NOT genuine chaos. Therefore ANY future substrate Krylov/OTOC computation near the fold that shows exponential early-time growth (or linear Lanczos b_n growth) MUST first be cleared against the saddle-dominated-scrambling alternative BEFORE being read as a Lyapunov exponent. The framework pre-commits: no fold Lyapunov exponent may be claimed from Krylov/OTOC growth without an explicit saddle-vs-chaos discriminator.

- **Status today**: NO live exponential claim exists (CHAOS-2 gives t^1.9; `framework-chaotic-instantons.md §5.4` independently derives power-law, not exponential, decay at the van Hove branch point). So this is NOT a compute gem and changes NO verdict — it is a standing interpretive guard that becomes LOAD-BEARING the moment a Krylov b_n computation runs at the fold.
- **Pairs with the S104 W3 `S104-KRYLOV-KCP` gate** (rmt-seed GEM-1 / Rank 11, the Lanczos-b_n / Krylov-complexity-peak internal-consistency gate): that gate carries this saddle-caution in its pre-registration rubric as the mandatory interpretive companion. If its b_n ladder grows linearly at the fold, that is the saddle (per Bhattacharjee), NOT chaos — the substrate spectrum is Poisson and λ_L = 0.
- **Provenance**: 2026-06-10 S104 plan-freeze mack dispatch; gem-triage §7-C / rmt-seed GEM-2 (Rank 12). Substrate state verified `search_knowledge` (CG(24) Poisson ⟨r⟩=0.367; OTOC t^1.9 no Lyapunov S38; τ_fold=0.190 van Hove S85), this dispatch. Source: Bhattacharjee+ saddle-dominated-scrambling (arXiv 2203.03534), fetched-content via `downloads/research-sweep-s103/_triage/_seed-random-matrix-quantum-chaos.md` GEM-2.

### S104-AREA-QUANTUM-WATCH — unified long-horizon area-quantization WATCH (the closed S89/S94 corridor; NEW observational context only — explicitly NOT a re-open, NOT two parallel rows)

> **Substrate framing (GEOMETRIC)**: the substrate's emergent-horizon area IS the a₂-channel spectral moment (`area_SA = a₂_fold / N_edges`); the microstate-count route to a discrete Bekenstein-Mukhanov area-QUANTUM was tested and is CLOSED both ways (see below). This note records ONLY the new observational LISA-band echo-forecast context — it does NOT re-open the closed compute corridor and is deliberately a SINGLE note (the gw-mine and holo-mine area-quantization hooks dedup to ONE WATCH per gem-triage §2 dedup-ledger (a) — NOT two parallel rows).

**The closed compute corridor (verified canonical this dispatch, both directions)**:
- `S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION` **FAIL** — α = −1.59e-116, rel_dev = 1.0, Tr_HSS = 38 = R_CM (the Class-8.7 degenerate-observable / finite-cardinality-tautology pathology). The microstate-count route to a discrete area-quantum is CLOSED-FAIL.
- `CF-S95-W7-23-NARROW-PATH-REGIME-II` **PASS** (verified `search_knowledge` this dispatch: `γ_emergent = 398.08, band [398.077, 400.767], rel = 0.0068, mismatch = 1676.11× vs γ_BH = 0.2375, K0rank = 2, is_exact = False`) — the substrate landed its OWN Regime-II effective geometry, matching NEITHER Bekenstein (γ_BH = 0.2375) NOR LQG (mismatch 1676×). The substrate has its own area-quantization regime; the compute corridor is CLOSED.

**NEW observational context (the only new content — long-horizon WATCH, explicitly NOT a re-open)**:
- LISA-band ringdown echo forecasts from BH area quantization (Deppe+ arXiv 2411.05645) report sub-% sensitivity to the area-quantum α via QNM-overtone spacing — a future LISA-era observable.
- Spin-broadening washout caveat (Coates+ arXiv 2201.03245 / Völkel-Kokkotas 1909.01254, NOT-FETCHED abstracts only — cited as abstracts, not read in full): merger-induced QNM broadening can wash out the discrete area-quantum echo signature, weakening the observational reach.
- **Disposition**: long-horizon WATCH. The substrate makes NO live area-quantum prediction (the microstate route FAILed; the substrate's Regime-II matches neither Bekenstein nor LQG, and the area-IS-a₂-moment identity does NOT yield a discrete quantum α via microstate-count). The existing LISA QNM/echo falsifier (`S88-CF-CURV-15-CARDOSO-PANI-ECHO-LISA-RINGDOWN` PASS, NULL-predicted, stacked-SNR 8.216σ) already covers the echo-detection channel — this note does NOT add a parallel row; it records the area-quantization observational context as moot-for-the-framework (no live prediction) and long-horizon.
- **Provenance**: 2026-06-10 S104 plan-freeze mack dispatch; gem-triage §7-C / §2 dedup-ledger (a) (gw-seed hook 04 + holo-seed GEM-2, unified to ONE note). Closed-corridor state verified `search_knowledge` (S89 FAIL; CF-S95-W7-23-NARROW-PATH-REGIME-II PASS γ_emergent=398.08 mismatch 1676×), this dispatch. Sources: Deppe+ (arXiv 2411.05645); Coates+ (arXiv 2201.03245), Völkel-Kokkotas (arXiv 1909.01254) — the latter two NOT-FETCHED (abstracts only). Fetched-content for the dedup via `_seed-holography-bh-information.md` GEM-2 + `_seed-gw-backgrounds-pta.md` hook 04/09.

### S104-EXTERNAL-CALIBRATION-NOTES — two anchor-calibration notes (X(2370) glueball + g-2-is-now-lattice)

> External-anchor calibration notes (NOT framework predictions, NOT falsifier rows; recorded so future gates pre-register against current targets, not stale ones). The framework has NO substrate machinery for either object today (no pure-gauge-sector glueball-mass gate; no emergent R-ratio / a_μ^HVP computation) — both are long-horizon / anti-stale-source calibration anchors.

- **X(2370) 0⁻⁺ pseudoscalar-glueball candidate (long-horizon pure-gauge-sector target pin)**: BESIII (arXiv 2605.26495) fixes J^PC = 0⁻⁺ for the X(2370) via PWA of γK⁰_SK⁰_Sη′ at >14σ / >20σ in two new channels; mass m = 2359 MeV ≈ 2.36 GeV, width 170 MeV — the lightest-pseudoscalar-glueball candidate. The substrate's fiber IS SU(3) Yang-Mills; a glueball is a pure-gauge-sector (glue-only, zero-valence-quark) relay pattern. **Calibration use**: IF the framework ever builds a₄-Yang-Mills pure-gauge excitation-ladder machinery (a multi-session prerequisite — `search_knowledge` confirms NO pure-gauge bound-excitation gate exists today, only SM quantum numbers from C¹⁶), the X(2370) supplies a J^PC = 0⁻⁺ mass pin (2.36 GeV) and the LQCD ordering (0⁺⁺ < 2⁺⁺ < 0⁻⁺) supplies an ordering target. NOT pre-registerable now (no nameable machinery → would be BLOCKED as a compute gate). Long-horizon WATCH-tier observational seed.
- **muon g-2 is now a lattice-vs-data-driven-HVP question, NOT a new-physics 5σ (anti-stale-source calibration note)**: the historic ~4–5σ a_μ anomaly has largely EVAPORATED into a lattice-HVP-vs-(e⁺e⁻ data-driven) THEORY tension — the 2025 Theory Initiative White Paper is now lattice-HVP-dominated and SM-consistent (Di Luzio+ arXiv 2408.01123 on HVP model-independent tests; Davies+ arXiv 2503.03364 g-2 endgame review). **Calibration use**: any FUTURE framework a_μ^HVP gate MUST pre-register against the lattice (no-new-physics) target, NOT the stale 2020 BNL/FNAL-vs-2020-WP discrepancy — an `epistemic-discipline.md §"Source Reconciliation"` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE anti-stale anchor. No substrate machinery exists today (no emergent R-ratio computation; a_μ^HVP is laboratory-IN at m_μ), so this is a calibration note only, not a gate.
- **Provenance**: 2026-06-10 S104 plan-freeze mack dispatch; gem-triage §7-C / qcd-seed GEM-3 (Rank not retained — folds to these two WATCH/calibration notes). `search_knowledge` confirmed NO glueball / X(2370) inventory row and NO pure-gauge-sector excitation gate (registration/machinery gap), this dispatch. Sources: BESIII X(2370) (arXiv 2605.26495); Di Luzio+ HVP (arXiv 2408.01123); Davies+ g-2 endgame (arXiv 2503.03364) — fetched-content via `downloads/research-sweep-s103/_triage/_seed-qcd-hadron-oddities.md` GEM-3.

---

## S105 mack-cosmic-bridge landings (2026-06-11; W2-4 SN-null run-time routing)

> **Origin**: S105 W2-4 run-time routing per `sessions/session-plan/session-105-plan-w2.md §"Item 4 (SN-null) → mack run-time routing"`. UNLIKE the S104 plan-freeze notes above (which are no-live-prediction calibration/WATCH anchors), this is a LIVE forward-falsifier with an exact-0 substrate prediction and a near-term laboratory horizon — a live-watch pointer to the newly-landed inventory `falsifier-master-inventory.md` Row #87.

### S105-SN-NULL-WATCH — Schrödinger-Newton self-gravity substrate exact null (live forward-falsifier; pointer to inventory Row #87)

> **Substrate framing (PHONONIC)**: the substrate's area operator a₂ = Σ_j mult_j/λ_j² (the 2nd Seeley-DeWitt moment, G_N = 1/(16π a₂ M_KK²)) IS a fixed functional of the D_K spectrum, read FORWARD from the eigenvalues; the spectral action Tr f(D_K²/Λ²) is UNIVERSAL — it depends ONLY on (A_K, H_K, D_K), never on an external matter wavefunction \|ψ\|². So ∂a₂/∂⟨x̂⟩ = 0 EXACT (THEOREM-class, sympy structural, L-independent; verified this dispatch via the s105_w2_4_sn_null.npz ground truth), and the substrate self-gravity self-frequency ω_SN,substrate ≡ 0 EXACT — there is no \|ψ\|²-area feedback channel for matter-wavefunction self-gravity to source.

**Live forward-falsifier (this IS a live prediction, NOT a moot calibration note)**: gate `S105-W2-4-SN-NULL` (S105 W2-4, PASS; `[SIGN]` 3-tuple `sign=PASS magnitude=PASS regime=VALID`) DERIVED a zero-free-parameter exact null: **ω_SN,substrate = 0.0 EXACT** vs the Yan 2411.17817 torsion-balance ceiling `ω_SN,Yan = 1.589646e-02 rad/s` (= 2π·2.53 mHz) ⇒ ratio `0.000e+00 < tol 1e-6` PASS. ANY confirmed torsion-balance / levitated-optomechanical DETECTION of a nonzero SN self-frequency FALSIFIES ∂a₂/∂⟨x̂⟩ = 0 (LOAD-BEARING — the substrate would need a \|ψ\|²-area coupling channel it provably lacks at any L_max).

- **Prediction**: ω_SN,substrate = 0.0 EXACT (zero-free-parameter; THEOREM-class, no normalization knob — contrast Row #77 Σm_ν which carries an oscillation-anchoring caveat). `box_4_substrate_FOURTH_BOX` (DISTINCT from box-1 graviton / box-2 Møller-Rosenfeld semiclassical / box-3 full Schrödinger-Newton).
- **Detector / horizon**: torsion-balance SN self-gravity searches (now — Yan-class apparatus, arXiv 2411.17817 the current finite ceiling) → next-gen torsion-balance + levitated-nanosphere / matter-wave self-gravity bounds (near-term). The bound TIGHTENS toward the exact-0 prediction as sensitivity improves; the framework predicts the null SURVIVES every tightening. Adjacent (separate, UNDERIVED) channel: BMV gravitationally-induced-entanglement tabletop QG (2030s) — the substrate's BMV-entanglement contrast-prediction is the OTHER half of the "fourth box" and remains a separate bridge-spec compute item (this row lands ONLY the SN self-frequency null leg).
- **σ from LCDM / status**: N/A as a σ-distance (the prediction is an EXACT structural zero, not a value with an error band); the discriminator is presence-vs-absence of a detected SN self-frequency. **Status: LIVE** (structural-zero forward-falsifier).
- **Disposition**: live-watch pointer to `falsifier-master-inventory.md` Row #87 (the canonical inventory landing; this watchlist entry is the live-detector-roster pointer, the inventory row is the falsifier-side authority). PROMOTES the prior Row #86 (lines 2041/2045) already-consistent-null mention from "UNDERIVED / routes-to-S104 bridge-spec candidate" to a landed forward-falsifier.
- **Provenance**: 2026-06-11 S105 W2-4 run-time mack dispatch; gate `S105-W2-4-SN-NULL` PASS, `audit_sha256=57f48392a588bce56f8ee0aeba87a6fcbb5575b2abba50d36a2b98476f5fdf57` (full 64-hex on verdict line 1 of `computations/session-105/s105_gate_verdicts.txt`); `content_sha256=eec40073c1a4edf5b6105e91e38482388e11653705990463088c485188e5dfac`. Canonical pin `omega_SN_substrate = 0.0` (`canonical_constants.py` line 705, gate S105-W2-4-SN-NULL, Class-8.3 PIN-PROMOTES-TO-CANONICAL-ON-PASS); `a_2_FW_zeta = 2776.165389` (line 610, the ζ-regulated moment whose ψ-independence IS the null). Ground truth verified this dispatch via `s105_w2_4_sn_null.npz` (`d_a2_d_xhat=0.0`, `d_a2_symbolic_is_exact_zero=True`, `omega_SN_substrate=0.0`, `ratio=0.0`, `taxonomy_placement=box_4_substrate_FOURTH_BOX`). WP `sessions/session-105/session-105-w2-workingpaper.md` §W2-4. Yan 2411.17817 = methodological cross-check ceiling, NOT canonical source (`substrate-first-canonical-sourcing.md §(i)`). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole writer for `falsifier-watchlist.md` (forecast-liaison surface) + `falsifier-master-inventory.md` (sole writer, AMRI-PROMOTED 2026-04-28).

---

## S113 mack-cosmic-bridge landings (2026-06-23; WS-6 OBSAXIS campaign routing)

> **Origin**: S113 EVOI-frontier workshop-campaign routing per `sessions/session-113/session-113-workshop-campaign-synthesis.md` §4 (FIRM — route to mack-cosmic-bridge) + the WS-S112-6 OBSAXIS verdict `sessions/session-113/workshops/ws-s113-6-obsaxis/ws-s113-6-obsaxis-verdict.md` §4 ROUTE-mack #3. UNLIKE a no-live-prediction calibration note, this is a CONSTRUCTIBILITY-PENDING falsifier candidate — a higher-leverage, weight-free, FRIB-anchored dense-matter discriminant that ESCAPES the M_KK keystone, but whose first job is to determine whether it has any detector-reachable σ at all. Ranked #2 (the f·σ₈ growth gate `CF-S113-FSIGMA8-EUCLID-7BIN` is ranked #1, fund-first).

### S113-CO-SIGNDISC-FRIB-L-WATCH — weight-free dense-matter SIGN / FRIB-L discriminant (~~constructibility-pending candidate; ranked #2~~ → **CLOSED — STRUCTURAL NO-GO, S114 W1-2**: the weight-free FRIB-L discriminant does NOT exist; σ_reach=0)

> **STATUS UPDATE (2026-06-23, S114 W1-2): CLOSED — CONSTRUCTIBILITY RESOLVED NO-GO.** The constructibility SCOPE gate `CF-S114-CO-SIGNDISC-FRIB-L-SCOPE` closed **FAIL** (`audit_sha256=faea15a71fddfe5bacee34f35a832cb8234eac4b92ed77c907320fd02d3ae8a2`): the dimensionless `Ô`-type discriminant `R_stiff = dlnΔ_CFL/dlnμ = 46.8992` lands OUTSIDE the FRIB band `L/J ∈ [1.2500, 2.1875]` by ~21–25× → `σ_reach = 0.0000` (< the 0.5 PASS threshold), `sign_degenerate_in_band = True`, with Track-B intrinsic-dilute corroboration (`ratio_plateau = 0.1017`, `C_max = 2.257e-4` sub-floor). **No weight-free dense-matter discriminant with detector-reachable σ exists** — the dense-matter axis is a STRUCTURAL NO-GO (Track B), and the §EVOI.BF non-CMB falsifier surface is confirmed SINGLE (the growth axis Row #71 f·σ₈ alone). Falsifier-side authority: `falsifier-master-inventory.md` Row #88.compute-S114-W1-2-FRIB-L-NO-GO. This watchlist candidate is CLOSED (discharged-not-deferred; a closed corridor is not a forward CF per `Investigating-Workshops.md`).

> **Substrate framing (PHONONIC)**: the substrate's native dense phase IS CFL (the same SU(3) that color-locks IS the fiber, read FORWARD from the spectral content); the diquark-stiffening SIGN `dΔ_CFL/dμ > 0` IS a dimensionless, M_KK-WEIGHT-FREE substrate prediction about diquark density-dependence (the W2-1 SIGN-PASS, a genuine `Ô`-type observable on the ANCHORED side of the `§VII.BS NNU` partition). This CONTRASTS with the dimensionful M_max/compactness falsifier, which rides the one M_KK import (`M_max = M_KK · M̂_max`) and is structurally a FREE DIAL (Row #88.audit-S113-WS6-CO-FREE-DIAL).

**Constructibility-pending candidate (NOT yet a live prediction — the constructibility scope IS the first gate)**: `CF-S113-CO-SIGNDISC-FRIB-L` ties the durable W2-1 SIGN-PASS (`dΔ_CFL/dμ > 0` at every scan point, M_KK-free) to a dimensionless terrestrial observable — the substrate-derived symmetry-energy slope L (or the dimensionless EoS-stiffening-sign at supra-saturation) — tested against the FRIB-constrained `L ≈ 40–70 MeV` band (Sorensen+ 2024, χEFT + HIC + neutron-star combined). This REPLACES the free-dial `S113-CO-MR-NICER` (M_max-in-M_⊙ / C, both M_KK-weighted, structurally un-pinnable). **Explicit discipline**: no M_max-in-M_⊙ comparison; tuning the surface to hit a dimensionful target is ansatz-forced PASS (PROHIBITED Class 4).

- **Prediction**: TBD — the gate's FIRST job is to determine whether a weight-free dimensionless dense-matter discriminant has any detector-reachable σ at all (derive the discriminant from the substrate; map it to FRIB L; establish σ-reach). The W2-1 SIGN-PASS `dΔ_CFL/dμ > 0` is the durable weight-free seed.
- **Detector / horizon**: FRIB heavy-ion symmetry-energy data (terrestrial) + the Sorensen+ 2024 combined `L ≈ 40–70 MeV` band; secondary consistency cross-check against NICER `R_{1.4} ≈ 12–13 km` AS A DIMENSIONLESS-RATIO CONSISTENCY TEST ONLY (not a primary mass discriminator). Near-term terrestrial — the FRIB cross-check the growth axis structurally LACKS.
- **σ from LCDM / status**: **σ_reach = 0.0000** (RESOLVED — the discriminator `R_stiff = dlnΔ_CFL/dlnμ = 46.8992` is degenerate-in-band, ~21–25× outside FRIB `L/J ∈ [1.2500, 2.1875]`). **Status: ~~CONSTRUCTIBILITY-PENDING~~ → CLOSED — STRUCTURAL NO-GO (S114 W1-2, `CF-S114-CO-SIGNDISC-FRIB-L-SCOPE` FAIL).** The "if NO weight-free discriminant with σ-reach exists" clause FIRED: the dense-matter axis is confirmed a structural no-go (Track B — intrinsic dilute, M_KK-weighted all the way down), so the §EVOI.BF non-CMB falsifier surface is SINGLE (growth axis Row #71 alone). The #1 growth gate `CF-S113-FSIGMA8-EUCLID-7BIN` separately closed PASS (joint 2.96σ, S114 W1-1).
- **Disposition**: live-watch candidate; the falsifier-side authority is `falsifier-master-inventory.md` Row #88.audit-S113-WS6-CO-FREE-DIAL (the M_max free-dial annotation + the surviving weight-free recast), this watchlist entry is the constructibility-pending detector-roster pointer. Higher-LEVERAGE than the growth axis (it would open a terrestrial-anchored, FRIB-cross-checked falsifier) but NOT yet constructed and NOT pre-registrable-today — hence ranked #2 on tractability.
- **Provenance**: 2026-06-23 S113 WS-S112-6 OBSAXIS campaign routing; verdict `sessions/session-113/workshops/ws-s113-6-obsaxis/ws-s113-6-obsaxis-verdict.md` §3 (RANK #2 weight-free recast) + §4 Gate #2 + ROUTE-mack #3; campaign synthesis `sessions/session-113/session-113-workshop-campaign-synthesis.md` §3 Tier-3 item 8 + §4. On-disk dense-matter facts: `S110-CF-CO1-EOS` (gap 4.821→0.102, `C_max = 2.26e-4` sub-floor), `S110-CF-CO2-FALSIFIER` FAIL (`PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE`), the W2-1 SIGN-PASS `dΔ_CFL/dμ > 0`. NO canonical_constants pin (the verdict mints no value — the candidate is constructibility-pending). Source band: Sorensen+ 2024 (FRIB symmetry-energy slope L ≈ 40–70 MeV) = methodological cross-check anchor, NOT canonical source (`substrate-first-canonical-sourcing.md §(i)`). Cross-link `falsifier-master-inventory.md` Row #88.audit-S113-WS6-CO-FREE-DIAL (the falsifier-side authority) + Row #88.audit-S110-W1-WS-CO-1 (the WS-CO-1 STERILE precedent, same M_KK split) + Row #71.audit-S113-WS6-FSIGMA8-EUCLID (the #1 ranked growth axis funded first). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge forecast-liaison for `falsifier-watchlist.md` + sole writer for `falsifier-master-inventory.md` (AMRI-PROMOTED 2026-04-28).
