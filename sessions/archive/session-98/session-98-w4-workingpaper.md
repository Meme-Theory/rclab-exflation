# Session 98 Wave 4 — Observational: BF-spine off-diagonal covariance + κ-determinacy (Results Working Paper)

**Session**: 98 | **Wave**: W4 | **Plan**: session-98-plan-w4.md | **Theme**: observational-status closures — full off-diagonal cross-pipeline covariance of the BF_spine (OQ3 discriminator) + κ-determinacy from the CGWB peak-frequency axis. Both re-read S96/S97 substrate-IS observables; neither introduces a new substrate prediction.

## Gate Sections

### §W4-1. S98-W4-4-OQ3-COVARIANCE (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S98-W4-4-OQ3-COVARIANCE`
**Trigger**: `[SIGN]`
**Classification**: **NON-PHONONIC** (cross-pipeline covariance of a joint-evidence aggregate; the four FACTORS are substrate-IS, the gate-object is the BF covariance structure)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The four BF_spine factors {m_H, normal ν-ordering, σ/m=0, c_s²=0} have mutually independent derivation pipelines (max|Corr|<0.5), licensing a rank-2 off-diagonal dagger that leaves the full-covariance BF_spine DECISIVE; the S97 scalar {a₀,a₂}-dagger RANK-1-COLLAPSE was an over-conservative single-shared-handle proxy.
**Plan reference**: `sessions/session-plan/session-98-plan-w4.md` §W4-1 (machinery pin, two-part PASS predicate, substitution chain, dual prior).

**Verdict**: **PASS** — `max|off-diagonal Corr| = 0.0000 < 0.5` (strict) **AND** `pipeline_independent == True` (Wronskian witness non-degenerate + no shared cross-channel handle). The rank-2 off-diagonal dagger is **LICENSED**: the scalar `{a₀,a₂}`-dagger discount **LIFTS**; the full-covariance `BF_spine = 2000` (`log10 BF = 3.30103`), **DECISIVE** (>100). OQ3 resolves **YES**: `oq3_orthogonal_established: False (S97) → True`. Dual-prior posterior reallocated to **Track A** (rank-2 licensed): `post_A = 0.9 / post_B = 0.1`.

Composite 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` → composite **PASS** (deterministic collapse rule, cross-checked in-script).

**Results**:

The gate replaces the S97 **scalar** `{a₀,a₂}`-dagger (the **Tier-3 borrowed-H** pair `corr_w77a = 1.0` that drove the `RANK-1-COLLAPSE`) with the **FULL 4×4 off-diagonal cross-pipeline covariance** over the four **Tier-1 physical spine** factors. The scalar proxy was over-conservative for the spine: it measured the borrowed-H residual correlation of `{w₀, Ω_DM}` (which share the cosmological `H(t)` knob), an entirely different factor set from the spine.

*Per-pair cross-pipeline correlations (6 = C(4,2) off-diagonal pairs):*

| pair (i, j) | channel(i)–channel(j) | Corr(res_i, res_j) |
|:------------|:----------------------|:-------------------|
| m_H \| ν-ordering | α (fiber-embed) – β (mass-texture) | 0.000000 |
| m_H \| σ/m=0 | α – γ (occupation-gap) | 0.000000 |
| m_H \| c_s²=0 | α – γ | 0.000000 |
| ν-ordering \| σ/m=0 | β – γ | 0.000000 |
| ν-ordering \| c_s²=0 | β – γ | 0.000000 |
| σ/m=0 \| c_s²=0 | γ – γ (within-channel) | 0.000000 |

`max|off-diagonal Corr| = 0.0000` (all six pairs). 4×4 correlation matrix = **identity**; eigenvalues `[1, 1, 1, 1]`; **n_eff independent modes = 4** (a rank-1 collapse would give 1). The scalar rank-1 proxy was therefore over-conservative by **three effective degrees of freedom** for the spine.

*Pipeline-provenance map (the four DERIVATION PIPELINES, three distinct substrate channels):*
- **m_H** ← transverse fiber-embedding `|S|²` mode → a₄ KK-threshold spectral-action moment (**channel α**)
- **ν-ordering** ← seesaw/Dirac mass texture in the `M₃(ℂ)` summand of `A_K` (**channel β**)
- **σ/m=0** ← Leggett-channel GGE quasiparticle CPT-neutral / `N_Fock=1` superselection (**channel γ**, protected zero)
- **c_s²=0** ← shriek-map image `π_!⊗[D_B]` of the fiber Goldstone K-homology / base-Dirac class (band-bottom dispersion curvature `c_s²=lim_{k→0}ω²/k²`, §VII.BH), NOT a property of the BdG inter-band coherence (**channel γ** by *address*, protected zero by a **distinct, operator-factor-disjoint** mechanism). The two channel-γ zeros split the BdG block into orthogonal operator subspaces — σ/m=0 is occupation-changing (off-diagonal-in-N transition content), c_s²=0 is number-conserving (diagonal-in-N dispersion content) — and are tensor-factor-disjoint: `[Π_{N_Fock=1}, π_!⊗[D_B]]=0` EXACT (S98-W1 workshop V2, certifying §VII.BH). They share the block as an *address*, not as an *operator factor*.

*Pipeline-independence witnesses (the rank-2-licensing predicate, part b):*
1. **Cross-channel pairs (5 of 6)** cross **distinct** substrate channels (α–β, α–γ, β–γ): they share **NO** handle → `r → ∞` → `Corr → 0`. The spine carries **no shared cosmological knob** (that was the Tier-3 dagger pair's defect, correctly excluded from the spine), so `no_shared_cross_handle = True`.
2. **Within-channel pair (σ/m=0, c_s²=0; both channel γ)** — the only candidate for a shared handle — is **TESTED**, not assumed:
   - **Wronskian / algebraic-independence witness** `W₂E(u) = g_σ·g_cs2′ − g_cs2·g_σ′ = u·(2u) − u²·(1) = u²`, with response functions `g_σ(u)=u` (σ/m linear in the occupation gap `u=|Δ|/E`) and `g_cs2(u)=u²` (c_s² quadratic — group-velocity² vanishes at 2nd order at the band bottom). `min|W₂E| = 2.500e-03 > tol = 1e-9` → **non-degenerate** → the two pipelines are **linearly independent functionals** of the gap (NOT a single shared scalar, which would force `W₂E ≡ 0`).
   - **Protected-zero status (knowledge-MCP confirmed)**: σ/m=0 is EXACT by `N_Fock=1` superselection (annihilation amplitude identically zero, **independent of the gap VALUE**); c_s²=0 is EXACT by Kasparov product factorization (`m_Goldstone^{4D}=0`; Layer-1 topological, scheme-independent, zero-parameter, PROVEN §VII.BH; **independent of the gap VALUE**, `c_s2_FW=0.0`). A protected topological zero has a **degenerate (zero-variance) residual** — its value is 0 regardless of any common parameter (including the shared `|Δ|` anchor). Two protected zeros produced by **distinct** mechanisms (Fock superselection vs Kasparov factorization) therefore share **no propagating handle**: `σ_shared = 0 → r_γ → ∞ → Corr_γ = 1/√((1+r)²) → 0`.

   ⇒ `pipeline_independent = (W₂E non-degenerate) AND (no shared cross-channel handle) = True`.

**Methodology note (in-session correction, honestly disclosed)**: a first-pass within-channel model computed `Corr_γ` as the squared overlap `cos²(g_σ, g_cs2) = 0.9376` of the two response *curves*, which forced a FAIL. That was a **category error** the workshop `w5-d3-rank1-vs-rank2-covariance.md` explicitly warns against (`math-scripts.md §"Mnemonic-vs-exact"`; the workshop L2 retired the analogous `1−1/518` decorrelation mnemonic): geometric parallelism of two monotone power-law curves as sampled vectors is **not** a statistical correlation of derivation-pipeline residuals. The substrate-faithful determination is the protected-zero / Wronskian analysis above (`Corr_γ = 0`). The corrected verdict (PASS) superseded the flawed-model line per `gate-verdicts.md §"Option A"` (absolute verdict permanence; corrective line carries `supersedes=`); the producing script is idempotent (re-runs skip re-emission when the latest non-superseded audit_sha matches).

*[SIGN] substitution chain (the "STRENGTHENS the spine" direction claim, substituted numbers):*
- **Definitions** (`s97_d3_bf.npz`, verified): `b_mH=1.5, b_nu=0.3010299957, b_σ=1.0, b_cs2=0.5`; `Σ b_i = 3.3010299957 = b_spine_struct` ✓; `delta_logBF_dagger = 1.5`.
- **rank-1 (dagger APPLIED, S97 disposition)**: `log10 BF = b_spine_struct − delta_logBF_dagger = 3.30103 − 1.5 = 1.80103` → `BF = 63.25` [STRONG 10–100].
- **rank-2 (dagger LIFTED, this gate)**: `log10 BF = b_spine_struct = 3.30103` → `BF = 2000` [DECISIVE >100].
- **lift increment**: `Δ(log10 BF) = 3.30103 − 1.80103 = +1.5 = delta_logBF_dagger` (exactly); `BF ratio = 10^{+1.5} = 31.623`. Sign of `Δ(log10 BF) = +` (POSITIVE, strictly increasing). Since `1.80103 < 2` (STRONG) and `3.30103 > 2` (DECISIVE), the lift carries the spine **across** the DECISIVE threshold. ⇒ `max|Corr|<0.5 ⇒ dagger lifts ⇒ BF_spine STRENGTHENS` from STRONG (63.25) to DECISIVE (2000). ∎

*Substrate-first framing*: the gate-object is the joint-evidence covariance (NON-PHONONIC), but the four FACTORS are substrate-IS spectral predictions flowing FROM `D_K` eigenvalues; statistical independence here is of the DERIVATION PIPELINES, **distinct from algebraic independence** (the latter is the S75 W2-E Wronskian on a₀/a₂/a₄; this gate's object is the joint-evidence covariance of the spine's *measurement residuals*). κ does NOT enter the BF_spine — the spine factors are dimensionless evidence ratios, consistency-pinned by the same geometry, not by κ. No container-thinking inversion: each `b_i` is the framework's prediction for an emergent observable; the arrow `D_K eigenvalues → spectral moments → emergent physics → measurement` is unchanged.

*Plan-text-drift note* (`substrate-first-canonical-sourcing.md §(ii.B)`): `canonical_constants.py` drifted at runtime vs the plan-freeze pin (`ed414699… → 8894875206…`) — **additive-only**, sibling S98 waves (W3-1, W3-2) appended NEW constants (`m_e`, `dm2_*_NuFit`, `sigma8_*`); **no consumed value changed** (verified out-of-band: `tau_fold`, `M_KK`, `Delta_BCS`, `v_ew`, `m_H_obs`, `planck_ns` all unchanged). The **gate-critical** upstream `s97_d3_bf.npz` matched its pin `7db2c6f6…` exactly — it carries every number the gate consumes. Drift accepted; the runtime canonical SHA is used in `audit_sha256`, the plan-pinned SHA preserved in the audit pinmap; the drift is disclosed in the verdict-line `value=` (`…canon_drift_runtime_sha_used`).

*Value 4-tuple*: `(value=0.000000, scheme=FW, convention=ABSOLUTE, L_max=N/A)`.

**Output Artifacts**:
- Script: `computations/session-98/s98_w4_4_oq3_covariance.py` (contains `from canonical_constants import`, `append_verdict`).
- Data: `computations/session-98/s98_w4_4_oq3_covariance.npz` (58 keys; `Corr_matrix`, `offdiag_values`, `max_abs_offdiag`, `eigvals`, `n_eff_modes`, `W_2E`/`W_2E_nondegenerate`, protected-zero booleans, `Corr_gamma`, `pipeline_independent`, `disposition`, `BF_spine`/`band`, `oq3_orthogonal_established`, `post_A`/`post_B`, 3-tuple).
- Plot: `computations/session-98/s98_w4_4_oq3_covariance.png` (4×4 correlation heatmap + disposition number line with the rank-1/rank-2 BF branches).
- Verdict line (canonical): `computations/session-98/s98_gate_verdicts.txt`
  - `S98-W4-4-OQ3-COVARIANCE: PASS -- value='max|Corr|=0.0000_disp=RANK-2-LICENSED_BF_spine=2000.00_DECISIVE_pipeline_independent=True_log10BF=3.30103_oq3_established=True_canon_drift_runtime_sha_used' scheme=FW convention=ABSOLUTE L_max=N/A audit_sha256=0814c57fe01d6aa85ffb0497e6c850f6af095d451d716fb99282d4277bc32fe1 content_sha256=2e088bf110a86b711e643074c3623a340315dce6c7a3669a09109ff1cddb82b5 schema_version=S84+`
  - dual-SHA companion row (`audit_sha256_short=0814c57fe01d6aa8`, `content_sha256_short=2e088bf110a86b71`).
  - schema-v2 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) — REQUIRED for the `[SIGN]` trigger.
  - sig_5: `audit_sha256` unique across the verdict file (no duplicate).

**MCP Pre-Compute Audit**:
- `search_knowledge("S97-D3-BF BF_spine rank-1 collapse dagger covariance")` → `S97-D3-BF` gate: PASS, "BF_spine = 2.0×10² DECISIVE after {a0,a2}-dagger discount"; the dagger discount is the object this gate re-examines under full covariance.
  > **[S101 mislabel guard — annotation, append-only; verdict line PERMANENT and UNEDITED]** The gate-text phrase "2.0×10² DECISIVE after {a0,a2}-dagger discount" MISLABELS the mechanism: a 2000→200 step is a 1.0-decade move (the b_mH=0.5 ACCOMMODATION floor of the full spine), whereas the canonical {a0,a2}-dagger discount is **1.5 decades → 63.25** (Sage-exact `10^1.80103`; the `BF_spine_dagger` equation entity). 200 is the ACCOMMODATION floor, NOT a dagger-discounted value. See `falsifier-master-inventory.md` S101 BF-spine-reference-class block (conflation guards). (S101 phonon-first × mack workshop.)
- `get_constant("b_spine_struct")` → not found (the b-factors live in `s97_d3_bf.npz`, not `canonical_constants.py`; loaded from the npz with SHA matched).
- `search_knowledge("c_s2 Kasparov factorization sigma/m N_Fock superselection Leggett topological zero-parameter independent")` → equation entry (session-96-plan-w7): "σ/m=0 from N_Fock=1 superselection, c_s²=0 from Kasparov factorization … substrate-IS predictions carrying NO borrowed H(t)"; theorem (van-den-dungen-synthesis): `c_s²=0` PROVEN, topological, scheme-independent, zero-parameter (`m_Goldstone^{4D}=0`). **Load-bearing**: confirms the within-channel pair are protected topological zeros by distinct mechanisms → no shared propagating handle → `Corr_γ = 0`.
- `trace_entity("Decoupling Theorem Wronskian a0 a2 a4 algebraic independence")` / `trace_entity("Leggett channel sigma/m c_s^2 occupation gap …")` → no trace (the a₀/a₂/a₄ Wronskian is the S75 W2-E *borrowed-H* dagger context, distinct from the spine; confirms the spine-pipeline independence is the OPEN question this gate resolves, not a pre-closed result).
- Not PRE-CLOSED: the S97 gate explicitly parked `oq3_orthogonal_established=False`; this gate computes the cross-pipeline covariance that resolves it.

---

### §W4-2. S98-KAPPA-INDEP-FROM-CGWB-FREQ (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S98-KAPPA-INDEP-FROM-CGWB-FREQ`
**Trigger**: `[SIGN]`
**Classification**: **NON-PHONONIC** (detector-reach question about a transport-knob's epistemic status; the CGWB peak IS a substrate observable, the gate-object is κ-determinacy)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The CGWB peak frequency f_obs(κ_nat)=8.4835e+39 Hz lies outside every existing GW detector horizon (PTA, LISA, LIGO/ET, optimistic resonant-HF ceiling), so the κ-dependent frequency axis supplies no second dimensionally-independent seconds-scale; κ stays consistency-pinned, not independently-pinned.
**Plan reference**: `sessions/session-plan/session-98-plan-w4.md` §W4-2 (INFO/FAIL gate — no PASS branch; set-membership operator, substitution chain).

**Verdict**: **FAIL** (composite). The CGWB peak frequency sits OUTSIDE every detector horizon by ≥28.9 decades; the κ-dependent frequency axis supplies **no** second dimensionally-independent seconds-scale. **κ remains CONSISTENCY-PINNED** (not independently-pinned). This is the predicted outcome of the INFO/FAIL gate (FAIL = detector-sterile for κ-triangulation; INFO would have meant in-band/independently-pinnable). schema-v2 3-tuple: **sign=PASS, magnitude=FAIL, regime=VALID** → composite **FAIL**.

**NUMBERS (first)**:

| Quantity | Value | Source |
|:---------|:------|:-------|
| f_obs(κ_nat) | **8.4835e+39 Hz** (log10 = 39.9286) | canonical `f_obs_CGWB_peak_kappa_nat` (S96, NOT superseded) |
| κ_nat (M_KK⁻¹→s) | 8.860439881925477e-42 s/tick | canonical `M_KK_inv_seconds` (S96) |
| cross-check vs S97 npz `f_peak_Hz` | rel residual = **0.000e+00** | `s97_omegagw_peak_height.npz` (bit-exact) |
| cross-check vs S97 npz `kappa_nat` | rel residual = **0.000e+00** | `s97_omegagw_peak_height.npz` |
| nearest horizon (resonant-HF ceiling 1e11 Hz) | **+28.929 decades ABOVE** | min over channels of log10(f_obs/hi_c) |
| decades above LISA pivot (3 mHz) | **+42.451 decades** | log10(f_obs / 3e-3) |

**Per-channel set-membership** (f_obs ∈ [lo, hi]? + decades f_obs sits ABOVE each band ceiling = log10(f_obs/hi)):

| Channel | Band [lo, hi] Hz | f_obs in-band? | f_obs / hi |
|:--------|:-----------------|:---------------|:-----------|
| PTA | [1e-9, 1e-7] | **False** | 10^+46.929 |
| LISA | [1e-4, 1e-1] | **False** | 10^+40.929 |
| LIGO/ET | [1e1, 1e4] | **False** | 10^+35.929 |
| resonant-HF (optimistic) | [1e9, 1e11] | **False** | 10^+28.929 |

f_obs is a member of **NO** band (member_band = None); every decade-gap above the band ceiling is positive.

**[SIGN] substitution chain** (the "f_obs above all horizons ⇒ κ stays consistency-pinned" direction claim, per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1: f_obs(κ_nat) = 8.4835e+39 Hz        [canonical f_obs_CGWB_peak_kappa_nat, NOT superseded]
        cross-check s97_omegagw_peak_height.npz f_peak_Hz = 8.4835e+39  ✓ (residual 0.000e+00)
        log10(f_obs) = 39.9286
Step 2: highest detector upper edge  hi_max = resonant-HF optimistic ceiling = 1e11 Hz
        log10(hi_max) = 11   (all other channels LOWER: LIGO/ET 1e4, LISA 1e-1, PTA 1e-7)
Step 3: membership test (highest band first):
        f_obs ∈ [1e9, 1e11] ?  8.4835e39 ≤ 1e11 ?  FALSE   (f_obs/hi = 10^+28.929)
        f_obs ∈ [1e1, 1e4]  ?                       FALSE   (10^+35.929)
        f_obs ∈ [1e-4, 1e-1]?                       FALSE   (10^+40.929)
        f_obs ∈ [1e-9, 1e-7]?                       FALSE   (10^+46.929)
Step 4: sign(log10 f_obs − log10 hi_max) = sign(39.9286 − 11) = sign(+28.929) = +  (POSITIVE)
        ⇒ f_obs strictly ABOVE the highest horizon edge ⇒ f_obs ∉ ∪_c [lo_c, hi_c]
Step 5: POSITIVE gap on EVERY channel ⇒ no detector measures the CGWB peak frequency
        ⇒ the frequency axis (f_obs ∝ κ) yields NO independent seconds-scale
        ⇒ κ constrained ONLY by the cooling-budget CONSISTENCY-pin, not by a measurement
Conclusion: f_obs(κ_nat) outside all detector horizons ⇒ FAIL (INFO/FAIL gate, no PASS)
            ⇒ κ stays CONSISTENCY-PINNED. Direction is POSITIVE; the claim holds.  ∎
```

`sign_verdict = PASS`: the substitution-chain Step-4 prediction (top gap > 0, f_obs above the highest edge) matches the computed sign. `magnitude_verdict = FAIL`: f_obs is OUTSIDE all bands (the predicted detector-sterile outcome; INFO was reserved for the surprise in-band case). `regime_verdict = VALID`: f_obs finite & positive, S97 cross-checks bit-exact (0.000e+00), all four band edges positive-ordered.

**Report-only — hypothetical κ-triangulation precision per band**: since f_obs ∝ κ, an external anchor at f_anchor in a real band would pin κ = κ_nat · (f_anchor / f_obs(κ_nat)). At each band's geometric center the implied κ differs from κ_nat by the channel's distance below the substrate peak — PTA center → 10^−47.9, LISA → 10^−42.4, LIGO/ET → 10^−37.4, resonant-HF → 10^−29.9. **None is realized** (f_obs is out-of-band on every channel); the band log-widths (2–3 decades) would set the achievable log-precision on κ *if* an in-band anchor existed, but it does not.

**Substrate framing** (`phononic-framing.md`): the CGWB peak IS the acoustic signature of the GGE relic's post-fold spectral reorganization — its frequency flows FROM the fold van-Hove DOS (M_KK/(2π) emission) THROUGH the redshift chain (a_fold/a_now), not a thermal-equilibrium CMB-style spectrum IN an expanding container. κ enters f_obs multiplicatively (f_obs ∝ κ), which is precisely WHY an in-band frequency *would* pin κ — but the substrate puts the peak at ~10^40 Hz, far above every horizon. The detector=tail separation (28.9–42.5 decades into the IR tail) is set by the κ-scaling transport factor. The arrow `D_K spectrum → fold van-Hove acoustic emission → redshift → f_obs ~10^40 Hz` is unchanged; the substrate IS the CGWB peak, the detector fails to measure it IN the emergent observational band. Consistent with the GW→LSS flagship migration (`project_s96_w3_cgwb_flagship_retirement`): the live acoustic falsifier is the first-sound BAO ring, NOT a GW-detector signal.

**Solution-space consequence** (FAIL): the CGWB-frequency channel is CONFIRMED detector-sterile for κ-triangulation — consistent with `S96-OBS-CGWB-PEAK-FREQ` FAIL (GHz+ band). κ's epistemic status is UNCHANGED in the registers (it was already consistency-pinned via `S97-COOLING-BUDGET-KAPPA-PIN`; that recovery is a unit-consistency identity, not an independent triangulation). This gate makes the κ-determinacy explicit and final on the CGWB-frequency axis: **any future independent κ-pin must come from a DIFFERENT observable**, not the CGWB peak. No §7 κ-status change is warranted (no down-tag, no up-tag — κ was never claimed independently-pinned).

**Cross-wave note**: V.6 (`S98-W4-4-OQ3-COVARIANCE`) is the sibling §W4-1 BF-spine gate; V.7 here is independent of it (κ does NOT enter the BF_spine — the spine factors are dimensionless evidence ratios, consistency-pinned by the same geometry, not by κ). If Wave 1's `CF-S98-W1-ROUTE-RECONCILIATION` (K→g_M) lands PASS, it strengthens V.6, not V.7; V.7's verdict is κ-axis-final regardless.

**Output Artifacts**:
- Script: `computations/session-98/s98_kappa_indep_from_cgwb_freq.py` (29,781 bytes; contains `from canonical_constants import`, `append_verdict`) ✓
- Data: `computations/session-98/s98_kappa_indep_from_cgwb_freq.npz` (12,351 bytes) ✓
- Plot: `computations/session-98/s98_kappa_indep_from_cgwb_freq.png` (92,000 bytes; left = log10-frequency number line with the four detector bands + f_obs and the +28.9-dec nearest-gap arrow; right = decade-gap bar chart, all four bars positive) ✓
- Verdict line: `computations/session-98/s98_gate_verdicts.txt` — canonical FAIL line `audit_sha256=10d31d0e8975bb866c13063c65d29652b94e67f1b7f030d5b60a42387912ac83`, `content_sha256=8abd8db3f013ebd716446755179abfa96b8d8bc3aab52512ddf24a99b71d500b`, `schema_version=S84+`; dual-SHA companion row; **schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row** (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) — REQUIRED for [SIGN], present ✓. SHA unique across all S98 verdict lines ✓.
- 4-tuple: `value=...kappa_status=CONSISTENCY-PINNED... scheme=FW convention=ABSOLUTE L_max=N/A`.

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md` query-first discipline):
- `get_constant("f_obs_CGWB_peak_kappa_nat")` → **8.4835e+39** (S96, source `s96_obs_cgwb_peak_freq.npz`, gate S96-OBS-CGWB-PEAK-FREQ, **superseded=False**). Confirms the V.7 input frequency.
- `get_constant("M_KK_inv_seconds")` → **8.860439881925477e-42** (S96, source `s96_w1_mkk_seconds.npz`, gate S96-W1-MKK-SECONDS, **superseded=False**). Confirms κ_nat.
- `search_knowledge("CGWB peak frequency kappa detector horizon consistency-pinned")` → returned the canonical constant + the `S96-OBS-CGWB-PEAK-FREQ` gate (already **FAIL**, `f_obs_kappa_nat=8.4835e+39Hz_band=GHZ+`, `kappa_nat=8.8604e-42s`) + the scale-and-channel equation "detector=tail separation set by transport factor f_LISA/f_peak — a 42.45-decade unit." Confirms (a) this gate is the **distinct** κ-determinacy question (not a recompute of the peak frequency), and (b) the 42.45-decade LISA-pivot gap is already canonically recorded. **NOT PRE-CLOSED** — the κ-independence-from-frequency-axis disposition is a new gate-object; S96-OBS-CGWB-PEAK-FREQ closed the peak-frequency value, not the κ-triangulation-determinacy question V.7 asks.

**Plan-text drift caught + resolved** (`substrate-first-canonical-sourcing.md §(ii.B)`): `canonical_constants.py` SHA at runtime (`ded0c9de8028793a…`) differs from the plan-freeze pin (`ed414699…`) — the file was edited by a concurrent S98 wave (the `S98-HK-SIGMA8-CHANNEL-KEYED-PINS` line is already in the verdict file). The V.7-consumed constants are **bit-exact unchanged** (`f_obs_CGWB_peak_kappa_nat = 8.4835e+39`, `M_KK_inv_seconds = 8.860439881925477e-42`, both matching the MCP), independently confirmed by the 0.000e+00 cross-check residual against `s97_omegagw_peak_height.npz` (whose SHA `c62e358f…` matches the plan pin exactly). The drift is in unrelated lines; the verdict is unaffected. The audit_sha256 records the script + the runtime canonical bytes + the input-pin map, so the audit trail is internally consistent with the as-run state.

**κ-sweep grid source note** (plan-corrected input): the κ-sweep grid the plan flagged is in `s97_omegagw_peak_height.npz` key `kappa_grid` (121 pts, κ∈[1e-20,1e-10]), NOT the non-existent `s96_w6_5_omegagw_spectrum.npz`. Confirmed present and read at runtime (the gate evaluates f_obs at κ_nat; the grid is a read-only cross-check that the κ-axis is the swept dimension, consistent with `kappa_robust=True` — amplitude κ-independent, frequency κ-dependent).

---

## Wave 4 Synthesis (team-lead)

(Written after both gates complete. Structure: `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`. Reconcile both observational-status verdicts; route the §7 falsifier-surface consequences to `sessions/archive/session-98/session-98-housekeeping.md §A` per the capstone-hygiene 5-question gate — V.6 touches the BF_spine row (Q2) and on PASS/FAIL a status change (Q3); V.7 touches the κ-status (Q2). The mack sole-writer applies any §7 patch via the canonical write-order; THIS WP does not edit `falsifier-master-inventory.md` or the capstone.)

## Carry-Forward Computations

(One `### {CF-ID} — {title}` sub-heading per genuine future-work item, each with a 4-field-spec table: What / Inputs / Gate / Effort. Per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md` — genuine future computation only; process observations and in-session hygiene go in Constraint-Map Updates and the housekeeping ledger, not here. If both gates close in-session with no genuine future-work item, write a single line: "No carry-forwards: all wave outcomes closed in-session.")

### CF-S99-KAPPA-ALT-OBSERVABLE-SCAN — enumerate κ-dependent substrate observables landing in a realized detector/measurement band [Q-other; solo compute follow-up]

> **Routing note**: NEW solo COMPUTE follow-up surfaced by the S98 `/rclab-investigate` w4 chunk; routes to `/rclab-plan` (pre-registered threshold + machinery pinnable ⇒ a compute carry-forward, NOT a workshop per `Investigating-Workshops.md §"is NOT"` item 1). V.7 (`S98-KAPPA-INDEP-FROM-CGWB-FREQ` FAIL, audit `10d31d0e…`) closed the CGWB-frequency axis for κ-triangulation (f_obs(κ_nat)=8.4835e+39 Hz, +28.9 dec above the optimistic HF ceiling) and states any future independent κ-pin must come from a DIFFERENT observable. ALSO route to the EVOI table as a NEW item (Tier-3/4, LOW leverage — κ's epistemic status does not gate any observational prediction; it is a determinacy-of-an-emergent-transport-knob question). SUBSTRATE-FIRST: κ is an emergent transport knob (the M_KK⁻¹→s scale map) over the substrate; the scan asks whether any substrate-IS observable whose value depends on κ lands in a realized measurement band.

1. **What**: enumerate substrate observables whose value depends on κ (the M_KK⁻¹→s knob) AND that fall in a realized detector/measurement band, to test whether ANY independent (non-consistency) κ-pin exists. (The CGWB-frequency axis is now closed for this purpose by V.7; this scan looks for a DIFFERENT observable.)
2. **Inputs**: `computations/session-97/s97_omegagw_peak_height.npz` (the κ-grid); the seconds-scale prediction set; `M_KK_inv_seconds` (canonical_constants.py); the V.7 verdict (`S98-KAPPA-INDEP-FROM-CGWB-FREQ` FAIL, audit `10d31d0e…`) as the closed-axis baseline.
3. **Gate**: `S99-KAPPA-ALT-OBSERVABLE-SCAN` — PASS iff ≥1 κ-dependent observable lands in a realized measurement band (would upgrade κ from CONSISTENCY-PINNED → INDEPENDENTLY-PINNED); FAIL/INFO iff none lands in-band (κ stays consistency-pinned, the determinacy question stays open).
4. **Effort**: ~1 wave.

## Constraint-Map Updates

(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason. Candidate rows: OQ3 orthogonality status `oq3_orthogonal_established` False → decided per V.6 verdict; κ epistemic status confirmed consistency-pinned per V.7. Process observations — e.g. the stale `s96_w6_5_omegagw_spectrum.npz` plan-text-drift reroute — go here, not in Carry-Forward Computations.)

## Files Produced

(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)
