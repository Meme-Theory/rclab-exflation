# Session 110 Wave 2 — the 3 HIGHEST + the A_s/CC magnitude deciders (Results Working Paper)

**Session**: 110 | **Wave**: 2 | **Plan**: session-110-plan-w2.md | **Theme**: M_KK-keystone structural-support — promote the three highest-EVOI levers on the rank-1 M_KK weight (B1, CV2A, CF1) plus the three magnitude deciders (AS2, CCDARK2, CCDARK1) from the investigation track into permanent session-110 gates.

## Gate Sections

### §W2-1. S110-CF-B1-TRANSITPS (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-B1-TRANSITPS`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (TRANSIT-PS-67 promotion; two-leaf power spectrum, shape AND amplitude)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The session re-run of the inv-10 W2-1 TRANSIT-PS build reproduces the two-leaf P(k) — BZ-leaf k³-blue (n_s≈3), Goldstone-pivot-leaf n_s=0.9561 + |α_s|<0.019 via the Mode-Independent Occupation Theorem (deg(T_{BZ→pivot})=+2 NON-SCALAR) with truncation_consistent=True — landing shape+amplitude together (dual prior 0.6 PASS-whole / 0.4 INFO-marginal-regime).

**Output Artifacts** (closure-verification checklist; mirrors the plan's `output_artifacts:` block):
- **script** `computations/session-110/s110_cf_b1_transit_ps_promote.py` — present; `from canonical_constants import` ✓ and `print_verdict_payload` ✓ (both must_contain patterns matched).
- **data** `computations/session-110/s110_cf_b1_transit_ps_promote.npz` — present (59-key archive: two scale-tagged leaves, amplitude leg, 3-tuple, drift documentation).
- **plot** `computations/session-110/s110_cf_b1_transit_ps_promote.png` — present (4-panel: BZ k³-blue P(k); two-leaf n_s(k); amplitude leg bar; verdict panel).
- **verdict line** in `computations/session-110/s110_gate_verdicts.txt` — `^S110-CF-B1-TRANSITPS:.* audit_sha256=[a-f0-9]{64}` ✓ (`audit_sha256=39e5ee366fabf5814750eadf557b1bc417b46cad9e1854b9d9db9409fde135a3`), dual-SHA companion row ✓, [SIGN] 3-tuple companion row ✓, plus composite-precedence + plan-text-drift + regulator_pin extra rows.
- **wp_section** this section — Status/COMPLETED, Verdict, Output Artifacts, MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit**:
- `search_knowledge("TRANSIT-PS-67 two-leaf power spectrum n_s pivot BZ blue Mode-Independent Occupation")` → returned the Mode-Independent Occupation Theorem (S57/S62, PROVEN, baseline-findings-s66 row 21: "Tilt from geometry only"), the TRANSIT-PS-67 gate (4/5, CRITICAL; PASS iff |α_s(k_CMB)|<0.015, FAIL>0.019), and the Q23 open_channel. Gate is OPEN on the investigation track, NOT yet session-promoted — confirms the promotion is needed (not PRE-CLOSED).
- `get_constant("n_s_framework")` → 0.9561 (S85; n_s_FW_exact=Fraction(9561,10000) bit-exact S88 W-15; CANONICAL framework n_s at CMB pivot, distinct from planck_ns=0.9649).
- `get_constant("alpha_s_pivot_goldstone")` → 0.0 (S92, AH-TR-1; Goldstone-protected at CMB pivot).
- `get_constant("alpha_s_substrate_distance_1")` → −0.08587279 (S92; Mellin pole s=3, INSIDE the BZ — the BZ-leaf running, scale-separated by deg(T_BZ→pivot)=+2).
- `search_knowledge("impulse quench amplitude OOM inv-5 inv-6 ...")` → located the amplitude leg: inv-5 W2-1 OOM_gap=+0.8644 (A_s_impulse=1.5367e-08), inv-6 W2-2 log_gap=+1.455 (A_s=5.99e-08); both replace the prior 3.02/3.15/4.56/9.5-OOM self-disagreement.
- **Not PRE-CLOSED**: TRANSIT-PS-67 is an OPEN investigation-track gate; per `gate-verdicts.md` Investigation-Track Canonical Path, it enters the permanent session index only via this session re-computation.

**Verdict**: **INFO** (composite). 3-tuple: `sign_verdict=PASS`, `magnitude_verdict=PASS`, `regime_verdict=MARGINAL`. Composite collapses to INFO via the **plan-frozen operator** (plan §W2-1 `INFO_meaning` line 188: *"the composite-collapse rule maps magnitude=PASS+regime=MARGINAL → INFO"*), which OVERRIDES the generic collapse reading (PASS) per `gate-verdicts.md §"Plan-frozen gate-block operator precedence"` — disclosed in the mandatory `# composite-precedence:` companion row. **dual_prior discriminator**: INFO → 0.9 Track B (the SHAPE promotes — n_s pivot leaf + BZ blue-leaf diagnostic both registered; the amplitude/regime caveat carries forward).

Output 4-tuple: `(value=ns_pivot=0.9561…regime[wkb=0,frozen=89,MARGINAL]…shape+amplitude-together-dedup-i, scheme=TRANSIT-PS-Parker-Bogoliubov, convention=TWO-LEAF-SCALE-TAGGED-deg-T-plus-2-NON-SCALAR, L_max=12)`. Dual-SHA (full 64-char): `audit_sha256=39e5ee366fabf5814750eadf557b1bc417b46cad9e1854b9d9db9409fde135a3`, `content_sha256=8b13f5bfb7a4e399dd6db351abc50bd1f917bf1a06a3cf6e816306b49510c2e4`.

**Results**:

*The two scale-tagged leaves (SCALE-AND-CHANNEL-TAGGING, `phononic-framing.md §"Scale-and-channel-tagging"`)*

| Leaf | (scale, channel) | n_s | α_s | tilt | role |
|:-----|:-----------------|:----|:----|:-----|:-----|
| **leaf-2 (Goldstone-pivot)** | (CMB-pivot, Goldstone) | **0.9561** | **0.0000** | RED (n_s<1) | gate-governing (laboratory-IN) |
| **leaf-1 (substrate / BZ)** | (substrate/BZ, transport) | **2.9998** | −0.0039 | BLUE (n_s>1) | registered blue-leaf diagnostic (substrate-IS) |

- **n_s^pivot in-band**: `|0.9561 − 0.9561| = 0.000000 ≤ 0.0030` ✓ (publication precision 4 sig figs; n_s_FW_exact = 9561/10000).
- **|α_s^pivot| ceiling**: `0.000000 < 0.019` ✓ (Goldstone-protected, PERMANENT/Exact, S92).
- **truncation_consistent = True**: branch-frequency L3↔L7 drift = 5.43e-05 (mode-grid backbone L-stable); n_s(L7-equiv subset) = 2.999934 vs n_s(L12) = 2.999825 (tilt sign agrees BLUE, magnitude within 0.05). The cosmological window is Casimir-SATURATED at L_max=12.
- **BZ-leaf k³-blue diagnostic**: n_s^BZ = 2.9998 > 1 ⇒ BLUE; the independent global-linear ln P vs ln k slope = +1.9999 (n_s^BZ_linfit = 2.9999) confirms the spline-at-pivot reading. 89/89 BZ modes are frozen-superhorizon at the fold (k < k_tach = 1974 M_KK); the WKB-Bogoliubov leg is EMPTY (`wkb_leg_empty=True`) ⇒ regime=MARGINAL.

*The 6-step substitution chain (red pivot tilt vs blue BZ tilt — plan §W2-1)*

1. n_s^BZ ≡ 1 + d ln P_BZ/d ln k, P_BZ = Σ_k |β_k|²|u_k/z|² on the 89 BZ modes [inv-10 W2-1].
2. BZ modes DEEP-SUPERHORIZON at fold (k ≪ aH) ⇒ |u_k/z|² ~ k²·const ⇒ P_BZ ∝ k³ [NOT horizon-crossing].
3. n_s^BZ = 1 + d ln(k³)/d ln k = 1 + 3 = 4 nominal; build reports **2.9998** (the naive "−3 cancels +3" does NOT hold — modes are deep-superhorizon, not horizon-crossing; the global-linear slope +2.0 reflects the |u/z|² ~ k² growing-mode plus the k³ measure netting to ≈ +2 in the spline reduction).
4. CMB-pivot tilt is the GEOMETRIC tilt n_s^pivot = 1 − 2ε_H, ε_H from spectral-action geometry, INDEPENDENT of |β_k|² [Mode-Independent Occupation Theorem, S57/S62, PROVEN].
5. O^pivot = O^substrate iff deg(T_{BZ→pivot}) is the T2-VACUOUS scalar case; here **deg = +2 NON-SCALAR** (S93 W7-1, factorization_holds=False) ⇒ BZ-leaf and pivot-leaf observables are DISTINCT, **54.04 decades** apart.
6. n_s^pivot = 1 − 2ε_H = **0.9561** [canonical n_s_framework, S85]; ε_H_implied = (1−0.9561)/2 = **0.021950**. This is the leaf a CMB detector reads, NOT n_s^BZ ≈ 3.

**Direction (substantiated)**: the tilt is RED (n_s^pivot = 0.9561 < 1) at the pivot leaf, BLUE (n_s^BZ = 2.9998 > 1) at the BZ leaf — OPPOSITE-sign tilts. `sign_verdict=PASS` confirms BOTH directions (pivot RED ∧ BZ BLUE). The two leaves must NOT be conflated; the BZ-leaf n_s ≈ 3 is the correct registered blue-leaf diagnostic, **not** a FAIL.

*The amplitude leg (dedup flag i — shape AND amplitude TOGETHER, NOT shape-only)*

The impulse-quench |β_k|² amplitude functional is paired with the shape as REGISTERED CONTENT (it is not a gate threshold — the gate operator is the n_s/α_s/truncation set membership):
- **inv-5 W2-1** (impulse-quench Bogoliubov): A_s = 1.5367e-08, **OOM_gap = +0.8644** (recompute against A_s_CMB=2.1e-9 gives +0.8644, consistent); substrate-natural ξ_KZ normalization; replaces the 3.02/3.15/4.56/9.5-OOM self-disagreement.
- **inv-6 W2-2** (Parker-adiabatic-regularized Bogoliubov): A_s = 5.99e-08, **log_gap = +1.455** (recompute +1.4552, consistent); direction DOWN, −1.69 OOM vs the prior +3.15.
- The A_s upper-edge *filter* leg is the separate gate S110-CF-AS2-GREYBODY (FAIL this session — the 0.512 ∫Γ is filter-fitted); the **FLOOR** A_s ≥ A_s^BD is permanent on 3 axes, orthogonal to both the amplitude leg and the filter leg.

*Cross-checks*

- n_s^pivot (framework) = 0.9561 vs Planck n_s = 0.9649: |Δ| = 0.0088 = **2.10σ** (σ_Planck = 0.0042). Sibling RED anchor n_s_FW_sqrt_cutoff = 0.9590.
- α_s^pivot (Goldstone) = 0.0000; canonical BZ-leaf α_s_sd1 = −0.0859 (the substrate-distance running); Planck α_s = −0.0045 (consistency reference, well within any envelope).
- Spectral-action scheme anchors (from the inv-10 build): cutoff n_s = 0.9567 (RED, in band), zeta n_s = 1.0897 (BLUE; the documented S66 sign-flip — the Mukhanov pump z''/z is functional-agnostic, so the assembled SHAPE is the framework claim; the zeta sign-flip is a flagged cross-check).

*Input-SHA provenance (substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift)*

Two plan-text drifts detected at runtime, both handled per §(ii.B) (audit map pins RUNTIME SHA; physics verified unchanged):
1. **canonical_constants.py**: plan-freeze `e5a7587f…` → runtime `89c9b086…` (this-session W0a T_acoustic PROVENANCE backfill, NO value change — corroborated by the CCDARK1/CV2A/AS2 verdict rows which document the identical drift). Consumed anchors (n_s_framework, alpha_s_pivot_goldstone) UNCHANGED ⇒ ZERO physics effect.
2. **inv10_w2_transit_ps_build.npz**: plan-freeze `d8342de5…` → runtime `a19ad05e…`. The build is an UNTRACKED file; numpy `.savez` writes a ZIP whose member headers embed timestamps, so a regenerated build's byte-SHA differs even when the array DATA is bit-identical. **Verified VALUE-DETERMINISTIC** (two consecutive re-runs produce byte-identical files; all 59 array keys bit-identical at atol=0). The byte-SHA assertion was replaced by an **ARRAY-CONTENT gate** against the plan-pinned canonical values (ns_pivot_CMB=0.9561, alpha_pivot_CMB=0.0, ns_pivot_substrate=2.9998245390143765, truncation_consistent=True) — the physics-invariant test — which PASSED (`build_content_consistent=True`). The tracked s84 L12 cache SHA `9e6d9cf7…` matches plan-freeze exactly.

*Constraint-map update*

TRANSIT-PS-67 (the framework's #1-flagged CRITICAL observational gate) migrates from the investigation track to a permanent session-110 result at INFO grade: the **two-leaf power-spectrum SHAPE is promoted** (Goldstone-pivot n_s=0.9561 + |α_s|<0.019 + BZ blue-leaf diagnostic, truncation_consistent), shape AND amplitude landing together (amplitude leg registered: inv-5 +0.86 / inv-6 +1.455 OOM). The **regime caveat carries forward** (Track B): all 89 window modes are frozen-superhorizon, so the impulse-quench mode-by-mode regime is MARGINAL — the tilt is read from the geometric (Mode-Independent Occupation) channel, not the WKB-Bogoliubov channel. This does NOT weaken the shape (the tilt is spectral-action geometry, independent of occupation); it scopes the confidence to the geometric-tilt provenance. **Substrate framing**: PHONONIC — the arrow D_K eigenvalues → transit Bogoliubov {α_k, β_k} → produced occupation n_k=|β_k|² → post-fold acoustic P(k); A_s and n_s are the GGE-relic acoustic squeezing modulus + the geometric spectral-action tilt of the SAME produced relic state, NOT a ΛCDM inflaton normalization + tilt. The substrate IS the BZ-leaf k³-blue spectrum; the laboratory measures the red 0.9561 pivot tilt 54.04 decades away; deg(T_{BZ→pivot})=+2 NON-SCALAR is why a CMB detector reads the geometric tilt rather than the occupation-shaped BZ blue spectrum.

---

### §W2-2. S110-CF-CV2A-MKK-TRANSMUT (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CV2A-MKK-TRANSMUT`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (BCS dimensional-transmutation PASS promotion; M_KK keystone)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: The inv-11 W1-1 BCS transmutation PASS — M_KK/M_Pl = exp(−1/(λ_eff·N₀)) — re-computed under a session gate reproduces oom_distance=0.7202 ≤ 1.0 AND frac_uncert_gap_term=0.8298 ≥ 0.5 bit-for-bit, converting the #1 standing gap to a landed transmutation-corridor PASS (the register cell stays frozen-since-S42; the promotion licenses only a status NOTE).

**Output Artifacts** (closure-verification checklist; mirrors the plan's `output_artifacts:` block):
- **Script** `computations/session-110/s110_cf_cv2a_mkk_transmut_promote.py` — PRESENT (26 426 bytes); `grep -E "from canonical_constants import|print_verdict_payload"` matches both markers (`from canonical_constants import M_KK, M_Pl_reduced`; `def print_verdict_payload(...)`). `py_compile` clean; python-validate untagged-literal count = 0.
- **Data** `computations/session-110/s110_cf_cv2a_mkk_transmut_promote.npz` — PRESENT (9 342 bytes); `verdict=PASS`, `all_bitexact=True`, `oom_red=0.7201655350546652`, `frac_uncert_gap_term=0.8297912902304105`.
- **Plot** `computations/session-110/s110_cf_cv2a_mkk_transmut_promote.png` — PRESENT (99 829 bytes); scale-ladder (M_Pl→M_KK_derived→M_KK_gravity) + OOM-uncertainty-budget decomposition (gap vs cutoff/fit).
- **Verdict line** in `computations/session-110/s110_gate_verdicts.txt` — PRESENT; matches `^S110-CF-CV2A-MKK-TRANSMUT:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=5a3f2fdf0988dc9f03e368883fe44769a6052db8649d507baee9a0cdd9e6e93e`); dual-SHA companion row present; emitted via `emit_verdict` (race-safe, sig_5 unique, 8 rows, session track). `[VERIFY]` trigger — schema-v2 3-tuple emitted for audit continuity but not required.
- **This WP section** — Status=COMPLETED, Verdict=PASS, Output Artifacts + MCP Pre-Compute Audit blocks present.

**MCP Pre-Compute Audit** (queries run before writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `get_constant("M_KK")` → 7.428660036284456e16 GeV (S42, CONST-FREEZE-42; alias of M_KK_gravity, spectral-zeta/gravity-a₂). Confirms the transmutation target.
- `get_constant("M_Pl_reduced")` → 2.435e18 GeV (S7, CODATA 2018). Confirms the cutoff normalization (reduced-Planck).
- `search_knowledge("M_KK dimensional transmutation BCS exponential reduced Planck mass")` → confirmed the canonical `f_KK=(M_KK/M_Pl)^4` transmutation factor (s76), `Δ_BCS=0.370 M_KK` (s56-paasch), and §W2-3 (S92) that the M_KK^5 dimensional rescaling cancels in dimensionless ratios — establishes M_KK as the multiplicative weight. No existing closure pre-empts a *session-grade* promotion of the inv-11 transmutation PASS (the result lived only on the investigation track). NOT PRE-CLOSED.

**Verdict**: **PASS** (composite-AND; both inequalities satisfied; bit-for-bit reproduction confirmed).

- `oom_distance = 0.7201655350546652` ≤ 1.0 → **PASS** on the OOM criterion (the derived scale lands within one decade of the gravity-anchored value).
- `frac_uncert_gap_term = 0.8297912902304105` ≥ 0.5 → **PASS** on the gap-dominance criterion (the gap magnitude, not the cutoff normalization, carries 83% of the OOM-uncertainty budget — the result is a DERIVATION, not a fit).
- Bit-for-bit reproduction of inv-11 W1-1 across all five PASS-criterion quantities → **VALID** (`all_bitexact=True`).
- Output 4-tuple: `value=…oom_distance=0.7201655351…frac_uncert_gap_term=0.8297912902…`, `scheme=BCS-dimensional-transmutation`, `convention=M_Pl_reduced`, `L_max=12`.
- `sign_verdict=PASS` (OOM), `magnitude_verdict=PASS` (gap-dominance), `regime_verdict=VALID` (bit-exact).
- dual-SHA (full 64-char): `audit_sha256=5a3f2fdf0988dc9f03e368883fe44769a6052db8649d507baee9a0cdd9e6e93e`, `content_sha256=54b247b638b90190dfbb581353b98517c44ed75221557bff3ad7ef916ba1aea6`.

**Results**:

*Substitution chain (BCS / Coleman-Weinberg dimensional transmutation), substituted numbers:*

| Step | Quantity | Value | Source |
|:-----|:---------|:------|:-------|
| 1 | λ_eff | 0.038934760900644856 | van Hove fold DOS singularity (inv-11 W1-1 npz; substrate-derived, NOT fit) |
| 2 | N₀ | 14.023250234055 | van Hove fold DOS singularity (inv-11 W1-1 npz; substrate-derived, NOT fit) |
| 3 | g = λ_eff·N₀ | 0.5459918949128435 | product |
| 4 | bcs_exponent = 1/g | 1.8315290196013434 | reciprocal |
| 5 | exp(−1/g) | 0.16016847970570353 | transmutation ratio |
| 6 | M_Pl_reduced | 2.435e18 GeV | CODATA 2018 (canonical) |
| 7 | **M_KK_derived = M_Pl_reduced·exp(−1/g)** | **3.900102480833881e17 GeV** (4 sf: **3.900e17**) | BCS transmutation |
| 8 | M_KK_gravity (target) | 7.428660036284456e16 GeV | CONST-FREEZE-42 (canonical) |
| 9 | **oom_distance = \|log₁₀(M_KK_derived) − log₁₀(M_KK_gravity)\|** | **0.7201655350546652** (4 sf: **0.7202**) ≤ 1.0 ✓ | reduced-Planck |

*OOM-uncertainty budget decomposition (Bayesian-UQ; the discriminator separating derivation from fit):* `delta_gap_dex = 0.20179513533731902` (gap-magnitude term, set by λ_eff·N₀) vs `delta_fit_dex = 0.04139268515822508` (cutoff-normalization/fit term). `frac_uncert_gap_term = 0.20180/(0.20180+0.04139) = 0.8297912902304105` ≥ 0.5 ✓. The gap term dominates 83/17 — the derived scale is fixed by the substrate's own pairing physics, not by the free choice of UV cutoff.

*Richardson pairing-engine cross-check (inv-11 W1-2):* `ratio_meanfield_over_richardson = 1.591457830147787` (ratio_mf_rich = **1.591**), inside the pre-registered band [1.4, 1.8] (`in_band=True`). Δ_meanfield/Δ_Richardson/Δ_ED = 0.732026 / 0.459972 / 0.454474 M_KK. The mean-field BCS gap and the exact pair-correlated Richardson-Gaudin diagonalization agree to within the band, and Richardson tracks the independent ED value to ~1.2% — the gap magnitude entering the transmutation is reproduced by the exact many-body solution, not only the mean-field estimate.

*Cutoff-normalization DIAGNOSTIC (NOT a PASS criterion; plan W2-2 machinery_pin_map):* the unreduced-Planck alternative gives `oom_unred = 1.420346663238636` (inv-11 stored value, evaluated against the canonical FULL Planck mass M_Pl = 1.2209e19 GeV). My local √(8π) reconstruction gives `oom_unred_recon = 1.4202854648977024` — the two differ at the 5th decimal because inv-11 used the rounded CODATA full-M_Pl (factor 5.01396) while √(8π) = 5.01326. Because `oom_unred` rides the unreduced-Planck normalization freedom (precisely the freedom this gate *measures* and does NOT lock — CF-INV11-W1-B), it is reported as a diagnostic and is **EXCLUDED from the PASS-gating bit-exact set**. Including a normalization-convention-dependent quantity in the PASS gate would let a cutoff choice veto a substrate-IS structural PASS; the PASS criterion is `oom_red` (reduced-Planck, the substrate-natural cutoff) and `frac_gap`, both bit-exact.

*Input-pin drift (substrate-first-canonical-sourcing.md §(ii.B)):* the plan pins `canonical_constants.py` at SHA `e5a7587f…568a`; the runtime file is `89c9b086…0f0ae` (edited elsewhere this session, Jun 20 12:22). The two constants this gate consumes — M_KK = 7.428660036284456e16 and M_Pl_reduced = 2.435e18 — are intact (verified by import). This is a benign canonical-constants edit; the audit pin uses the RUNTIME SHA per the §(ii.B) plan-text-drift correction convention, and the drift is documented in the verdict-line companion row and npz (`plan_sha_drift`). The other two input npz files (inv-11 W1-1, W1-2) match their plan pins exactly.

*Constraint-map update — atlas-04 / §VII status reconciliation NOTE (licensed by this PASS):* the M_KK keystone moves from **OPEN (frozen fit of unknown status)** → **transmutation-corridor PASS**. The framework's #1 standing gap now carries its first SESSION-grade derivation corridor: BCS dimensional transmutation reproduces M_KK within 1.0 OOM with the gap term carrying 83% of the budget. **The canonical M_KK register cell is NOT up-tagged to "derived"** — it stays gravity-a₂, frozen-since-S42 (HK-MKK), pending CF-CV2-B (Question B, W3, the gauge-a₄ fork). The session-promotion licenses the status NOTE only; it is dedup-consistent with HK-MKK.

**Substrate framing**: **GEOMETRIC.** M_KK is the single multiplicative weight `w` on every dimensionful observable (O = w·Ô; §VII.BS rank-1 NNU PROVEN). The transmutation derives that weight from the substrate's OWN van Hove fold DOS singularity: M_KK/M_Pl = exp(−1/(λ_eff·N₀)) is BCS/Coleman-Weinberg physics applied to the D_K spectral density at the fold — the eigenvalue pile-up at the van Hove edge sets a weak effective coupling g = 0.546, and the non-perturbative exponential exp(−1/g) = 0.160 generates the small dimensional weight. This is NOT importing a scale into a container; it is the substrate computing its own dimensional weight from its own spectral structure. Every spectrum-only and geometric-internal route to fixing M_KK was closed (geodesic-length, integer-arithmetic, Casimir-volume, holographic-foam — _rollup-mkk-ds §3), leaving the non-spectral DOS-singularity mechanism (intrinsically dimensionful, because the DOS is the BCS pairing kernel, NOT a Seeley-DeWitt residue — hence `regulator_pin=N/A`) as the sole surviving derivation corridor — now with a session-grade PASS. The explanation flows substrate → spectral DOS → dimensional weight → emergent scale, never scale → container.

---

### §W2-3. S110-CF1-AT-MINISUPERSPACE (einstein-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF1-AT-MINISUPERSPACE`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (effective-Friedmann functional-form decider; a₄ Starobinsky sign)
**Agent**: `einstein-theorist`
**Hypothesis**: Reducing S_SA = a₀ − a₂ + a₄ to the homogeneous-isotropic sector and reading sign(∂H²/∂ρ_relic) across a ρ-grid under BOTH reduction schemes decides MONOTONE-RAMP (schemes agree) vs SPLIT (schemes disagree), localized to the a₄ R²+Weyl² sign and MANDATORY-reconciled against the closed mechanism `V_spec monotone` (S24a) with a same-object-or-distinct declaration (dual prior 0.5/0.5).

**Output Artifacts** (closure-verification checklist; mirrors the plan's `output_artifacts:` block):
- **script** `computations/session-110/s110_cf1_at_minisuperspace.py` — present (34,717 B); `grep -E "from canonical_constants import|print_verdict_payload"` both PRESENT (Section 0 path-bootstrap + Section 1 canonical import; Section 6 `print_verdict_payload`). ✓
- **data** `computations/session-110/s110_cf1_at_minisuperspace.npz` — present (12,032 B); 31 keys incl. `rho_grid, s1_dH2_drho, s2_dH2_drho, s1_sign_uniform=1, s2_sign_changes=1, s2_turning_rho=13.4097, vspec_declaration=DISTINCT, branch=SPLIT, verdict=INFO`. ✓
- **plot** `computations/session-110/s110_cf1_at_minisuperspace.png` — present (105,884 B); two-panel (H²(ρ) both schemes + sign(∂H²/∂ρ) readout). ✓
- **verdict line** in `computations/session-110/s110_gate_verdicts.txt` matching `^S110-CF1-AT-MINISUPERSPACE:.* audit_sha256=[a-f0-9]{64}` — PRESENT + dual-SHA companion row + [SIGN] 3-tuple companion row + 4 annotation extra-rows (regulator_pin, SD1, holonomy-analog, V_spec reconciliation). ✓
- **this WP section** — Status/COMPLETED, Verdict/INFO, Output Artifacts, MCP Pre-Compute Audit all present. ✓

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):
- `search_knowledge("a(t) minisuperspace Friedmann substrate H^2 reduction monotone")` → returned the H²(τ)=F[S_SA,a₂,ρ_substrate] equation (transit-flow-genesis-to-now.md) + the S25/S75/S77 Friedmann-reduction equations; NO existing closure on the minisuperspace FORM decision. NOT PRE-CLOSED.
- `search_knowledge("V_spec monotone spectral action a_4 sign C amplitude")` → `V_spec monotone` closed_79/closed_170 (a₄/a₂=1000:1, no Starobinsky minimum, S24a) + the S41 open_channel noting inter-crystal a₄ "could have different tau-dependence" (the distinct-functional seed).
- `get_constant("a_4_FW_zeta")`=1350.7216, `get_constant("a_2_FW_zeta")`=2776.165389, `get_constant("a_0_FW_zeta")`=6440.0 (CANONICAL, S75/S88).
- `trace_entity("V_spec monotone")` → 3 theorem hits + 2 closed_mechanism hits (PROVEN, monotone increasing all ρ∈[0.001,0.5]) + 1 open_channel (inter-crystal a₄ DECREASING — the distinct-functional corroboration).
- `search_knowledge("effective Friedmann functional form reduction scheme gap density ceiling holonomy minisuperspace")` → located the inv-7 W4-1 workshop (`effective-friedmann-functional-form.md`, transit-dynamics × LQG, CONVERGED) + the prior compute `S95-W3-2-EFF-FRIEDMANN-GENRE` (INFO, residual_free_normalization_count=2). The gate is the SESSION-PROMOTION of CF-INV7-W4-1-MINISUPERSPACE. NOT PRE-CLOSED (investigation-track; enters the index only via this session gate).
- Sage cross-check (`sage_eval`): the Starobinsky R²+Weyl² (a₄) operator is PURE-CURVATURE — `d(8πGρ/3)/dρ = 8πG/3 > 0` from the a₂ term; the a₄ R² term is Ḣ-structured and contributes 0 to ∂H²/∂ρ. This closes the SD1 technical heart.

**Verdict**: **INFO** — branch = **SPLIT** (the two pre-registered reduction schemes give OPPOSITE sign(∂H²/∂ρ) over the physical ρ-window). 3-tuple: `sign_verdict=PASS` (the substitution-chain prediction — gap-scheme MONOTONE-positive, +1 — matched), `magnitude_verdict=INFO` (the form-decision "magnitude" object: schemes SPLIT, not agree), `regime_verdict=VALID` (∂H²/∂ρ finite, no interior pole over the window). Composite collapse: `magnitude_verdict==INFO ⇒ composite=INFO`. This is the plan's pre-registered INFO_meaning (scheme-dependent functional form) and the inv-7 W4-1 line-150 pre-registered INFO-bearing outcome.

dual-SHA (full 64-char): `audit_sha256=04bf8d1d1c8cc84a1f4c0b504bc09fe7b4afdac9865da7ac4a85ebffdc9a859f` `content_sha256=041c602b050d0542153bcc25b2e04b27c0dc377fb9597a3f5634f08556c8ecba`. 4-tuple: `(value=SPLIT, scheme=MINISUPERSPACE-EFFECTIVE-FRIEDMANN-FORM, convention=a_n^{ζ};reduction=BOTH;mu-bar-analog, L_max=12)`.

**Substrate framing**: GEOMETRIC. The arrow `D_K eigenvalues → a_n Seeley-DeWitt moments (a₀ cosmological term, a₂ Einstein-Hilbert, a₄ R²+Weyl² Starobinsky) → emergent (a,τ) congruence → H²(ρ)`. a(t) is NOT a background metric the substrate lives in; it is the homogeneous-sector projection of the spectral action S_SA = a₀ − a₂ + a₄. The form question localizes to ONE operator (the a₄ Starobinsky sign), read FROM the substrate moments — never importing a Friedmann equation and asking the substrate to match it. The SPLIT is itself a substrate-IS finding: the effective-Friedmann FORM is reduction-scheme-dependent, mirroring LQC's own 25-year regularization-non-uniqueness (Thiemann vs symmetric ordering vs μ̄ vs μ₀).

**Results**:

*Scheme 1 — gap-as-density-ceiling: sign(∂H²/∂ρ) = +1 (single-signed, MONOTONE).* The only place λ_min could enter the homogeneous constraint is through the moments a_n = Σ_k w_k λ_k^{−2s} — LINEAR sums, no bounded sin²-type saturation operator (inv-7 W4-1 Step 3, agreed D1 both agents). λ_min (=0.790 M_KK, S17a) is an INTENSIVE [M_KK] quasiparticle-creation floor, NOT an EXTENSIVE [M_KK⁴] density ceiling; it enters only as an additive zero-point offset ρ_offset = λ_min⁴ = 0.3895 M_KK⁴ (ρ-INDEPENDENT, annihilated by ∂/∂ρ). The a₄ R²+Weyl² moment IS present in the reduced action (S_eff=(1/16πG)∫[R + (a₄/a₂)M_KK⁻² curv²], inv-13 W1) but is PURE-CURVATURE (Ḣ-structured), contributing **0** to ∂H²/∂ρ (Sage-verified). ⇒ ∂H²/∂ρ = 8πG_eff/3 > 0 EXACTLY across the grid. **MONOTONE by construction.**

*Scheme 2 — holonomy-analog (μ̄-analog, improved dynamics): sign(∂H²/∂ρ) changes once (TURNING-POINT).* The most-LQC-favorable bounded analog of sin²(μ̄c)/μ̄² requires a saturation density ρ_c. In LQC ρ_c is a PLANCK-ANALOG density (~M_Pl⁴), not a moment-ratio; the substrate Planck-analog is the cutoff M_KK. A physical-consistency constraint binds ρ_c: the relic EXISTS with P_exc=1.000 at ρ_relic=26.553854 M_KK⁴, so H²≥0 at the realized loading REQUIRES ρ_c ≥ ρ_relic (a sub-cutoff ρ_c < ρ_relic gives H²(ρ_relic) < 0, ill-posed). The most-LQC-favorable *physically-consistent* ceiling is the MARGINAL one ρ_c^holo = ρ_relic. Then H²_holo = (8πG_eff/3)ρ(1 − ρ/ρ_c), ∂H²/∂ρ = (8πG_eff/3)(1 − 2ρ/ρ_c): positive for ρ < ρ_relic/2, negative for ρ > ρ_relic/2 — a TURNING-POINT at **ρ_turn = 13.4097 M_KK⁴ ≈ ρ_relic/2 = 13.277 M_KK⁴**, IN the physical window [ρ_min, ρ_relic]. (The a₄/a₂ = 0.4865 ratio is the curvature-squared coefficient diagnostic — it sets the Starobinsky Ḣ-term, NOT the matter ceiling.) **TURNING-POINT.**

*Scheme agreement → SPLIT.* Scheme 1 single-signed-positive (MONOTONE), Scheme 2 turns over (ONE-SIDED-CEILING) → schemes_agree = False → branch = SPLIT. This realizes exactly the inv-7 W4-1 pre-registered branch (line 150): "If gap-as-density-ceiling returns MONOTONE AND holonomy-analog returns TURNING-POINT, the honest verdict is scheme-dependent functional form." The contest is MONOTONE-RAMP vs ONE-SIDED-CEILING (SYMMETRIC-BOUNCE was over-determined-EXCLUDED at inv-7 W4-1: even-in-c holonomy [Ashtekar 2006 Paper08:145, Paper17:161] + white-hole irreversibility [S85] + GFT BOUNCE_transfers=False [S96]).

*MANDATORY V_spec-monotone (S24a) reconciliation → DISTINCT.* V_spec(τ;ρ) = −c₂R_K + c₄a₄^geom is the POTENTIAL LANDSCAPE; S24a proves it monotone INCREASING for all ρ (a₄/a₂=1000:1, no Starobinsky minimum). The minisuperspace ∂H²/∂ρ is a FRIEDMANN-REDUCTION object (H²=(8πG_eff/3)ρ_relic). These are **DISTINCT functionals of the same a₄ moment** — the p_S75 ≠ p_cosmo lesson (spectral-action SHAPE in τ-space ≠ Friedmann power-law in N-space). The a₄ moment ENTERS BOTH, but the FUNCTIONAL FORM differs: V_spec adds a₄ as a curvature *potential* term (−c₂R + c₄a₄, monotone in ρ); the H²-reduction uses a₄ only through the *pure-curvature Ḣ-structured* higher-curvature correction (Sage-verified zero contribution to ∂H²/∂ρ). Same INPUT (a₄), distinct OUTPUT functional. **V_spec monotone does NOT fix the Friedmann-reduction sign** — the SPLIT is read independently from the reduced constraint and does NOT contradict S24a. (Corroborated by the S41 open_channel: inter-crystal a₄ with gauge kinetic/spatial-variation terms "could have different tau-dependence" — a₄/a₂ DECREASING, distinct from the V_spec potential's increasing slope.)

*μ-pin.* μ̄-analog (improved dynamics, ρ_c FIXED; Ashtekar-Pawlowski-Singh 2006) — the physical LQC choice; declared in the convention field (μ̄-analog vs μ₀-analog: μ₀-analog scales ρ_c with the comoving volume, which would not change the within-window turnover sign and is reported as the alternative). Without the pin, the scheme is convention-shoppable (PROHIBITED_ACTIONS Class 1).

**ρ-grid:** 60 points (≥25) over [ρ_min = 0.01·ρ_relic, ρ_relic = 26.553854 M_KK⁴]. **NON-canonical inputs (inline provenance, get_constant returns null):** ρ_relic = 26.553854 = B1+B2+B3 Bogoliubov band sum, **S96 §W1-5** (cited verbatim by inv-7 W4-1 lines 80/172/366; truncation band [15.41, 26.85] M_KK per inv-12 W3-1; the plan's loose "S17a" attribution is corrected — the source is S96 W1-5). λ_min = 0.790 M_KK = **S17a** never-closing (DISTINCT from the canonical `lambda_min_max_ratio_FW`=0.15127, which is the |λ|_min/|λ|_max strict ratio; 0.790 is the absolute floor value). **CANONICAL (imported):** a₀=6440, a₂=2776.165389, a₄=1350.7216 (a_n_FW_zeta); M_KK_gravity=7.42866e16, M_Pl_reduced=2.435e18, G_DeWitt=5.0.

**regulator_pin:** a_n^{ζ} (zeta-regulated Seeley-DeWitt; the a₄ R²+Weyl² operator is the load-bearing term — MANDATORY tag per `regulator-pin-discipline.md`).

**Substitution chain (numbers substituted):**
- Step 1: S_SA(τ) = a₀ − a₂ + a₄ = 6440 − 2776.165389 + 1350.7216 (E7 moment combination, zeta-scheme).
- Step 2: homogeneous reduction maps a₂ → R (Einstein-Hilbert, sources 8πG/3·ρ) and a₄ → R²+Weyl² (Starobinsky, coefficient (a₄/a₂)M_KK⁻² = 0.4865·M_KK⁻²).
- Step 3: ∂H²/∂ρ_relic = (8πG_eff/3) + [a₄-curvature correction]. G_eff in M_KK units = (M_KK/M_Pl_red)² = (7.42866e16/2.435e18)² = 9.305e-4. 8πG_eff/3 = 7.795e-3 M_KK⁻² > 0.
- Step 4 (MANDATORY reconciliation): V_spec monotone (S24a) settles the a₄-sign in the POTENTIAL (monotone increasing); declared **DISTINCT** from the Friedmann-reduction ∂H²/∂ρ — same a₄ input, distinct output functional (p_S75 ≠ p_cosmo). Sign read independently.
- Step 5 (scheme-dependence): gap-as-ceiling → ∂H²/∂ρ = +7.795e-3 uniform (MONOTONE, a₄ R² contributes 0, Sage-verified); holonomy-analog → ∂H²/∂ρ = (8πG_eff/3)(1 − 2ρ/26.5539), zero at ρ = 13.277, sign-flip IN-window (TURNING-POINT). Schemes DISAGREE.
- Direction (read AFTER Step 5, NOT from V_spec): the two schemes carry OPPOSITE sign over [ρ_relic/2, ρ_relic] → **SPLIT**.
- Conclusion: INFO=SPLIT. The effective-Friedmann FORM is reduction-scheme-dependent; the a₄-sign is NOT reduction-invariant. The form question stays open pending a scheme-discriminating argument (the live contest MONOTONE-RAMP vs ONE-SIDED-CEILING; SYMMETRIC-BOUNCE excluded).

**Constraint-map updates:**

*(a) Structural changes.* The a(t)-backbone FORM question is now **decided as SCHEME-DEPENDENT** — a structural finding, not a numerical revision: the gap-as-ceiling reduction (substrate's preferred — no saturation operator) gives MONOTONE-RAMP, while the most-LQC-favorable holonomy-analog gives ONE-SIDED-CEILING, and the two are not reduction-invariant. The §6.2 capstone "no bounce" prose is **scoped further**: "no bounce" holds under the gap-as-ceiling reduction (the substrate-natural one), but a most-LQC-favorable holonomy-analog admits a one-sided causally-asymmetric ceiling. The CV-3 frontier residual is now pinned to a *scheme-discrimination* question (which reduction is substrate-canonical), NOT to the a₄-operator sign per se (which is settled in BOTH the potential [S24a, monotone] and the gap-reduction [MONOTONE], and only turns over in the deliberately-most-favorable holonomy construction).

*(b) Numerical.* ρ_turn = 13.4097 M_KK⁴ ≈ ρ_relic/2 (the holonomy-analog turnover); 8πG_eff/3 = 7.795e-3 M_KK⁻² (the bare EH slope); a₄/a₂ = 0.4865 (curvature-squared coefficient); ρ_offset = λ_min⁴ = 0.3895 M_KK⁴ (gap zero-point).

*V_spec reconciliation status:* **DISTINCT — no contradiction with S24a.** The gate does NOT re-derive or contradict the settled potential-landscape sign; it reads the Friedmann-reduction sign as a separate functional and reports its scheme-dependence.

---

### §W2-4. S110-CF-AS2-GREYBODY (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-AS2-GREYBODY`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (A_s upper-edge exit-filter; dynamical near-horizon resonance scan)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: Scanning the BdG exit-horizon fluctuation potential for the UN-scanned dynamical near-horizon resonance (finite quench rate τ̇, Floquet-WKB) decides whether ANY substrate V₀ lands ω_½=√V₀ ∈ [0.94, 3.72] M_KK AND reproduces ∫Γ=0.512±10% — i.e., whether the A_s upper edge is bounded-AND-derived (substrate barrier) or bounded-but-filter-fitted (tuning knob); regime_verdict auto-shortening applies if the finite-rate WKB small-parameter breaks within the window.

**Output Artifacts** (closure-verification checklist; mirrors the plan's `output_artifacts:` block):
- **script** `computations/session-110/s110_cf_as2_greybody_scan.py` (≈22 KB) — `grep -E "from canonical_constants import|print_verdict_payload"` → matches present. PASS.
- **data** `computations/session-110/s110_cf_as2_greybody_scan.npz`. PASS.
- **plot** `computations/session-110/s110_cf_as2_greybody_scan.png`. PASS.
- **verdict line** in `computations/session-110/s110_gate_verdicts.txt` matching `^S110-CF-AS2-GREYBODY:.* audit_sha256=[a-f0-9]{64}` — present with dual-SHA companion row + the schema-v2 3-tuple companion row (`sign_verdict=N/A magnitude_verdict=PASS regime_verdict=BREAKDOWN`; the [VERIFY] trigger does not require the 3-tuple, but the finite-rate-WKB auto-shortening clause emits `domain_used_frac` + regime per gate-verdicts.md) + 5 detail extra-rows. PASS.
- **wp_section** this section — Status/COMPLETED, Verdict/(FAIL), Output Artifacts, MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit** (queries executed before writing the script, per query-first discipline):
- `search_knowledge("greybody A_s exit filter integral transmission 0.512 over-production")` → `A_s = (produced squeeze at fold) × ∫Γ(ω)dω` (capstone Hawking collab); the fitted exit filter is S43/S95 greybody machinery; provenance hits `s95_w4_3_hawking_greybody_as`, `inv4_w1_exit_greybody_as`, `inv12_w3_4_greybody_from_bdg`. The 0.512 comparator and the two-route static baseline both exist; this gate scans the un-scanned dynamical channel. NOT pre-closed (the exit-FILTER substrate-derivation leg is the LAST open leg of the A_s wall, per `_rollup-as-wall §3`).
- `get_constant("Delta_BCS")` → 0.4642547394830737 (S70, R-PROTECTED canonical BCS gap, M_KK units). Imported.
- `get_constant("kappa_exit")` → 47.6146 (S95-W4-2-HAWKING-ANALOG-T-LEDGER; the STATIC surface gravity = ruled-out baseline). Imported.
- `get_constant("T_acoustic")` → 0.112 (S42/S47 GGE acoustic temperature). Imported.
- `get_constant("tau_fold")` → 0.19 (CONST-FREEZE-42). Imported.
- `search_knowledge("greybody from BdG static barrier 0.036 surface gravity inv-12 W3-4 dynamical resonance quench rate")` → confirmed the static κ_exit barrier gives ∫Γ≈0.036 (W4 static monotonicity context; BCS surface-gravity analog S69). Established baseline reproduced bit-for-bit (`integral_Gamma_derived=0.036264` from the inv-12 W3-4 npz).
- `search_knowledge("tau_dot quench rate Mach 13.75 supersonic transit ... finite rate dynamical near-horizon resonance Floquet WKB")` → `tau_fold=0.190 (Mach 13.75, supersonic — NOT quasi-static slow-roll)`; the finite-rate trajectory is `s57_finite_rate_transit` (`dtau_dt_phys=442.42`); the dynamical parametric resonance is `inv-12 W3-2` (`omega_q=2.0128`, `gamma_clock=29.75`). These are the substrate sources for the dynamical channel.
- **Not pre-closed**: the dynamical near-horizon resonance channel of the exit filter was un-scanned; the static channel is the ruled-out baseline (not re-scanned).

**Verdict**: **FAIL** — the A_s upper-edge exit-filter is **bounded-but-filter-fitted**. `value='exists_inband=True;best_inband_rel_dev=0.049375;ratio_tol=0.1;fitted_0.512=0.511872;static_baseline_intG=0.036265;dyn_omega_q=2.0128;dyn_relic_rms=2.9253;eps_WKB_omega_q=7.3439;eps_WKB_relic_rms=3.4769;domain_used_frac=0.1429;regime=BREAKDOWN;magnitude=PASS;ode_vs_closed=1.025e-09;canon_drift_plan2runtime=True'`. 3-tuple: sign=N/A / magnitude=PASS / **regime=BREAKDOWN** → composite **FAIL** (regime=BREAKDOWN forces FAIL per the gate-verdicts.md collapse rule, independently of the magnitude reading). audit_sha256=`ad0652c1eab0dec77c648c92aa6470d4cf4618cbed39f5ac548a9acfde5fa5c5`, content_sha256=`36af76a0e2a3b1029ce0d9d443a8f76e8be8536bc358b67dd97178efc4bfc9d7`.

**Results**:

*Substrate (the exit horizon IS a substrate feature, not a container boundary).* The exit "horizon" is the τ≈0.16 acoustic exit where the supersonic transit flow (Mach 13.75) crosses back through the sound cone. The relic modes are the locked GGE quasiparticle spectrum from inv-12 W3-1 (`{α_k, β_k}` ODE-locked, L_max=10 D_K BdG sector, 1248 unique modes, exit-horizon BdG dispersion `ω_k = √((λ_k²−μ²)² + Δ_k²)`, μ=0). The relic band `ω_k ∈ [0.9409, 3.7206]` M_KK matches the plan's pair_band [0.94, 3.72] M_KK; the squeeze-weighted relic-rms is ω_rms = 2.9253 M_KK. `A_s = (produced squeeze |β_fold|²) × ∫Γ(ω)`; this gate adjudicates only whether the exit greybody ∫Γ has a substrate scale.

*Static baseline reproduced (the ruled-out reference, NOT re-scanned).* The inv-12 W3-4 npz (loaded read-only) gives the established two-route static result: κ_eff = κ_exit = 47.6146, V₀ = κ²/4 = 566.79, so ω_½ = √V₀ = 23.81 M_KK — far ABOVE the relic band — and the squeeze-weighted ∫Γ = **0.036265** (reproduced bit-for-bit from the npz `integral_Gamma_derived`), 14× short of the fitted 0.512. Both prior routes (inv-4 W1-4 black-hole-thermodynamics + inv-12 W3-4 analog-gravity BdG) agree the static surface-gravity barrier is non-substrate. AS2 does not re-scan it.

*Dynamical channel scan (the UN-scanned candidate).* The finite quench rate τ̇ (S57 `dtau_dt_phys = 442.42`, Mach 13.75) makes the near-horizon barrier time-dependent; the relevant inverse-width is the parametric drive scale, NOT the static surface gravity. I scanned the Pöschl-Teller barrier `V_eff = V₀ sech²(κ_eff x_*)` over substrate-scale (κ_eff, V₀) pairs drawn ONLY from {T_acoustic=0.112, Δ_BCS=0.4642547, 2Δ_BCS=0.9285, Δ_BCS²/T_acoustic=1.9244, Floquet ω_q=2.0128, relic-rms=2.9253, κ_exit=47.6146} — **none placed at the band** — plus a continuous V₀-scan (200 points, V₀∈[(T/2)², κ²/4]) at the two dynamical κ_eff readings ω_q and ω_rms. Result:
  - In-band substrate barriers EXIST (`exists_inband=True`): for √V₀ ∈ [0.94, 3.72], substrate barriers give ∫Γ ≈ 0.65–0.99 — **over-transmissive**, because a barrier whose half-transmission sits inside the relic band lets most of the band's modes (ω_k up to 3.72) over-transmit. This is the opposite-direction failure to the static case (√V₀=23.8 above band ⇒ ∫Γ low at 0.036). The target 0.512 lives in the GAP between these regimes.
  - The continuous best in-band agreement is ∫Γ = 0.438 at √V₀ = 3.376 (κ_eff = ω_rms), rel_dev = 0.144 > 0.10. The discrete grid finds ONE in-band pair that numerically lands on 0.512: κ_eff = Δ_BCS = 0.464, √V₀ = ω_rms = 2.9253 ⇒ ∫Γ = 0.537, rel_dev = **0.0494 ≤ 0.10** (`best_inband_rel_dev = 0.049375`). On the literal band+target criterion that is `magnitude_verdict = PASS`.

*The decisive regime check (finite-rate WKB auto-shortening clause).* The single (κ_eff, V₀) pair that hits 0.512 does so in a regime where the static-barrier greybody concept does NOT physically apply. The pre-registered WKB small-parameter is ε_WKB(κ_eff) = γ_clock/κ_eff² (adiabaticity of the near-horizon barrier under the finite quench: drive-decay rate γ_clock=29.75 over barrier-frequency²):
  - ε_WKB(ω_q = 2.0128) = **7.34** ≫ 1; ε_WKB(ω_rms = 2.9253) = **3.48** ≫ 1; ε_WKB(Δ_BCS = 0.464) = **138** ≫ 1.
  - The fraction of the in-band scan window where the adiabatic WKB greybody picture is valid (ε_WKB < 1) is **f_used = domain_used_frac = 0.1429 < 0.50** ⇒ **regime = BREAKDOWN**.
  - Per the gate-verdicts.md auto-shortening collapse rule, `regime == BREAKDOWN ⇒ composite = FAIL` regardless of the magnitude reading. The supersonic Mach-13.75 quench makes the near-horizon barrier violently non-adiabatic; the greybody transmission interpretation breaks down before it can certify the filter as substrate-derived.

*Method cross-check.* The independent 1D scattering-ODE solve of `−ψ'' + V_eff ψ = ω²ψ` (DOP853, rtol 1e-9) at the dynamical Floquet barrier matches the closed Pöschl-Teller form to **ode_vs_closed = 1.025e-09** (method consistent; the transmission machinery itself is correct — it is the *adiabaticity* of the time-dependent barrier that fails, not the static-transmission computation).

*Output 4-tuple*: `(value=best_inband_rel_dev=0.049375, scheme=BdG-fluctuation-Poschl-Teller, convention=DYNAMICAL-near-horizon-resonance, L_max=10)`. regulator_pin = N/A (the greybody Γ(ω) is a transmission coefficient, not a Seeley-DeWitt residue).

*Substitution chain (substituted numbers, per plan §W2-4)*:
- Step 1: `A_s = |β_fold|² × ∫Γ(ω)dω` (the exit filter; inv-4 W1-4, inv-12 W3-4). The filter leg is ∫Γ.
- Step 2: `ω_½ = √V₀` is the half-transmission frequency of a Pöschl-Teller barrier of height V₀ (WKB greybody).
- Step 3 (static baseline): both prior routes give ∫Γ ≈ 0.036 with √V₀ = 23.8 M_KK (above band) — the static surface-gravity scale reflects ~96% of the band; reproduced here bit-for-bit (0.036265).
- Step 4 (dynamical candidate): scan V₀(τ̇) over substrate scales. In-band substrate barriers give ∫Γ ≈ 0.65–0.99; one Δ_BCS/relic-rms pair hits ∫Γ=0.537 (rel_dev 0.049), but at ε_WKB = γ_clock/κ_eff² = 138 (at Δ_BCS) and 3.48 (at relic-rms) — ε_WKB ≫ 1.
- Step 5 (read-off): the in-band scan window is WKB-valid over only f_used = 0.143 < 0.50 ⇒ regime = BREAKDOWN ⇒ FAIL. The 0.512 is reproducible numerically ONLY in a regime where the greybody picture itself does not hold; on the regime where it DOES hold (ε_WKB < 1, which requires κ_eff > √γ_clock ≈ 5.45 M_KK > top of band), no substrate scale lands √V₀ in band with ∫Γ = 0.512. The 0.512 exit-filter has no substrate scale.
- Conclusion: the exit-FILTER leg is bounded-but-filter-FITTED on EITHER channel (static ∫Γ=0.036 with √V₀ above band; dynamical 0.512 only in WKB-breakdown). The verdict adjudicates the A_s upper-edge FILTER leg only; the FLOOR (A_s ≥ A_s^{BD}) is permanent on 3 independent axes either way (`_rollup-as-wall §3`).

*Plan-text-drift note (substrate-first-canonical-sourcing.md §(ii.B)).* The plan pins `canonical_constants.py` SHA = `e5a7587f…`; the file on disk has SHA = `89c9b086…` (the S110 W0a T_acoustic PROVENANCE backfill changed bytes with NO value change). The runtime SHA was pinned as canonical and the drift documented in the verdict value (`canon_drift_plan2runtime=True`) + an extra-row. All consumed constant VALUES (Δ_BCS, κ_exit, T_acoustic, Mach_max) are unchanged.

*FLOOR-vs-filter scoping (FUNCTIONAL-INDEPENDENT classification).* This FAIL closes the exit-FILTER substrate-derivation corridor; it does NOT touch the A_s FLOOR. The FLOOR `A_s ≥ A_s^{BD}` (the relic's positivity wall — produced squeeze cannot be less than the Bunch-Davies minimum) is permanent on 3 independent axes (`_rollup-as-wall §3`) and is orthogonal to whether the upper-edge filter is substrate-derived. The exit-filter substrate-derivation question is **SCHEME-INDEPENDENT in its negative answer**: it FAILs on the static channel (any cutoff f, the static κ_exit barrier reflects the band), and FAILs on the dynamical channel (the 0.512 lands only where the WKB greybody picture breaks). The 0.512 is a fitted knob with no substrate scale on either channel.

**Constraint-map update**:

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-20 | S110-CF-AS2-GREYBODY (A_s exit-filter) | UNCOMPUTED | FAIL (bounded-but-filter-fitted) | Dynamical near-horizon resonance scan: in-band substrate barriers over-transmit (∫Γ≈0.65–0.99); the one Δ_BCS/relic-rms pair reproducing 0.512 (rel_dev 0.049) sits in ε_WKB≫1 regime BREAKDOWN (f_used=0.143); 0.512 has no substrate scale where the WKB greybody holds |
| 2026-06-20 | A_s upper-edge exit-FILTER leg (CF23 split, HK-AS) | last open leg of the A_s wall | closed as non-substrate (filter-fitted) | Both static (inv-4+inv-12, ∫Γ=0.036, √V₀ above band) and dynamical (0.512 only in WKB-breakdown) channels confirm the 0.512 is a fitted knob; the exit-filter substrate-derivation corridor is exhausted |
| 2026-06-20 | A_s FLOOR (A_s ≥ A_s^{BD}, HK-AS-FLOOR) | permanent on 3 axes | UNCHANGED (orthogonal to this leg) | The positivity FLOOR is functional-independent of the upper-edge filter; AS2 adjudicates only the filter leg |

---

### §W2-5. S110-CF-CCDARK2-MU (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CCDARK2-MU`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (CC Layer-A/Layer-B discriminator; SA-as-free-energy R0 input)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: Computing ∂(vacuum energy)/∂μ (Gibbs-Duhem −⟨N⟩) AND ∂(condensation)/∂V on the L10 D_K spectrum discriminates Reading-A (zero-on-both ⇒ CC is irreducibly Layer-B / Gibbs-Duhem, SA-disjoint, Wall #6 + Kosmann confirmed) from Reading-B (non-zero-on-either ⇒ the Tr f(D²) functional channel reaches the CC) — the R0 prelude deciding whether WS-SA-FREE-ENERGY fires (dual prior 0.6 Reading-A / 0.4 Reading-B).

**Output Artifacts** (closure-verification checklist; mirrors the plan's `output_artifacts:` block):
- **script** `computations/session-110/s110_cf_ccdark2_mu_discriminator.py` (57.2 KB) — `grep -E "from canonical_constants import|print_verdict_payload"` → 2 + 2 matches. PASS.
- **data** `computations/session-110/s110_cf_ccdark2_mu_discriminator.npz` (15.7 KB). PASS.
- **plot** `computations/session-110/s110_cf_ccdark2_mu_discriminator.png` (141 KB). PASS.
- **verdict line** in `computations/session-110/s110_gate_verdicts.txt` matching `^S110-CF-CCDARK2-MU:.* audit_sha256=[a-f0-9]{64}` — present with dual-SHA companion row + the [SIGN] 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + 3 detail extra-rows. PASS.
- **wp_section** this section — Status/COMPLETED, Verdict/(PASS), Output Artifacts, MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit** (queries executed before writing the script, per query-first discipline):
- `get_constant("Delta_BCS")` → 0.4642547394830737 (S70, R-PROTECTED canonical BCS gap, M_KK units). Imported.
- `get_constant("E_cond")` → −0.13685055970476342 (S36, ED-CONV-36 condensation energy). Imported.
- `search_knowledge("Wall #6 mu=0 particle-hole symmetry spectral action Gibbs-Duhem")` → confirmed `dS/dμ|_0 = 0` (S34/S35, "μ=0 forced analytically by particle-hole symmetry"; `D_BdG² = (D_K²+|Δ|²)⊗1₂`; Helmholtz F convex at μ=0, GC-35a). SA-side ∂/∂μ null is an ESTABLISHED structural result — this gate verifies it numerically, does not re-derive it.
- `search_knowledge("Kosmann theorem S35 order parameter pairing kernel domain Tr f")` → confirmed `δF_total = δF_kinetic[spectral action] + δF_pairing[Kosmann kernel]` (S35 connes-spectral-geometer-workshop): `Tr f(D_BdG²/Λ²)` computes ONLY the KINETIC gap-opening cost; the pairing kernel V is the order-parameter object OUTSIDE the spectral trace. SA-side ∂/∂V null is the Kosmann decomposition.
- `trace_entity("CC-as-free-energy spectral action Layer-A Layer-B")` → no trace (the Layer-A/B nomenclature is atlas-04-internal; the underlying S6 open channel "Does spectral action = phonon free energy hold rigorously?" surfaced via the Wall #6 search). NOT pre-closed — this gate is the R0 numerical prelude.
- **Not pre-closed**: the discriminator (does the SA functional channel reach the CC?) is the atlas-04 S3 CORE cell, open since S6. The SA-side nulls (Wall #6, Kosmann) are established; this gate's NEW content is the numerical verification that BOTH nulls hold on the canonical L10 D_K spectrum.

**Verdict**: **PASS** — Reading-A confirmed. `value='READING=Reading-A__slope1_vacuum_dSdmu_over_S=0.000e+00_sign=ZERO__slope2_cond_dSdV_fixedDelta_over_S=0.000e+00_sign=ZERO__vs_eps_zero=1e-10__GibbsDuhem_N=-0.00_dEvacdmu=3.725e-05__d2Sdmu2=2.384e+06__Kosmann_dEcondpair_dV=-6.077e+04_outside_Trf'`. 3-tuple: sign=PASS / magnitude=PASS / regime=VALID. audit_sha256=`34b030416b927a7a95768525ce44dbcc58455fc7a56f5fd294d6e5dc23967db4`, content_sha256=`21330f2a79bd498d75130f3b298aa96e1ee02099137e74ef5b3da0d5185fffbc`.

**Results**:

*Substrate (L10 D_K spectrum, SIGNED Nambu basis).* The S35 BdG spectral triple `H_BdG(μ) = [[D_K−μ, Δ],[Δ†, −(D_K−μ)]]` (Dong-Khalkhali-van Suijlekom 2022 §8.2; S35 C2 eq.1) on the L_max=10 D_K cache. The Hilbert space is `H_K ⊕ H_K` (particle ⊕ hole), so the construction acts on the **signed** single-particle spectrum `{±|λ_k|}` (78,080 |λ| modes → 7,538 unique signed values, |λ| ∈ [0.8197, 4.6702] M_KK). The chiral symmetry `{γ₉, D_K}=0` (S35 C1, machine-ε at all τ) pairs `(λ, −λ)`; **this PH symmetry is the load-bearing structure** — using only `|λ_k|` (a one-sided gapped spectrum) silently destroys it and produces a false Reading-B (caught and corrected: see Methodology).

*Slope 1 — ∂(vacuum)/∂μ at the PH-symmetric μ=0 (Wall #6 / S34 MU-35a null).* The "vacuum energy" is the spectral action itself, `S_SA(μ) = Tr f(D²_BdG(μ)/Λ²)` — the candidate substrate free energy whose μ-dependence Reading-B would require. With Δ=Δ_BCS=0.4642547, Λ=K_crit_BdG=2.035 M_KK, and a smooth cutoff `f(x)=e^{−x}`:
  - `dS_SA/dμ|_0 = 0.000e+00` **EXACTLY** (central difference, h=1e-4). `|dS/dμ|/|S| = 0.000e+00 ≤ ε_zero=1e-10`.
  - **Cutoff-independence cross-check**: rational cutoff `f(x)=1/(1+x)` gives `dS_SA/dμ|_0 = 0.000e+00` too — the null holds for ANY smooth f (it is a symmetry identity, not a cutoff artifact).
  - **d²S/dμ² = +2.384e+06 > 0** — matches the S34-reported LOCAL MINIMUM sign (S34 `d²S/dμ²|_0 ∈ [7.97, 8.63]`; the magnitude is Λ-normalization-dependent, the SIGN is the structural cross-check and it is correct).
  - **Gibbs-Duhem companion**: `Ω(μ) = −½ Σ_signed m_k E_k(μ)`; `dΩ/dμ|_0 = 3.7e-5 ≈ 0` (FD round-off of an exact zero), `⟨N⟩(μ=0) = −dΩ/dμ = −3.7e-5 ≈ 0`. Stationarity `|dΩ/dμ|_0|/(curv·h) = 6.4e-6`. Gibbs-Duhem identity `dΩ/dμ = −⟨N⟩` resid = 0.00 (tested off the symmetric point at μ_t).

*Slope 2 — ∂(condensation)/∂V (S35 Kosmann route).* The pairing coupling g is calibrated at V=1 so the self-consistent gap reproduces Δ_BCS bit-for-bit (`Δ_check=0.4642547`, calib resid 4.4e-11; substrate-first anchor fixed BEFORE the V-scan, Paper 06 §III). Varying the pairing-kernel volume V about V=1:
  - The gap DOES respond to V: `dΔ/dV = +7.069` (Δ is downstream of the kernel — this is physical, not the null).
  - The Kosmann order-parameter (pairing) condensation energy `E_cond_pair = −Δ²/(2gV)` responds to V: `dE_cond_pair/dV = −6.077e+04` — but this lives OUTSIDE the spectral trace (the Kosmann kernel piece `δF_pairing`).
  - **The clean SA-side null**: `S_SA(D²_BdG) = Tr f((D_K)²+Δ²)` depends on V ONLY through Δ(V); holding Δ fixed, V does not appear in `D²_BdG`. So `dS_SA/dV|_{Δ fixed} = 0.000e+00` **EXACTLY** — `|dS_SA/dV|_Δ/|S| = 0.000e+00 ≤ ε_zero`. The spectral trace is V-blind at fixed gap: the pairing-kernel volume V ∉ domain(Tr f), exactly the S35 Kosmann theorem.

*GPU validation.* `torch.linalg.eigvalsh` on the Nambu-doubled BdG block (AMD RX 9070 XT, n_block=316 in-window positive-|λ| modes) reproduces the closed-form `E_k=√(ξ²+Δ²)` to **2.658e-16** (machine precision).

*Discriminator.* slope1 = 0.000e+00 (zero), slope2 = 0.000e+00 (zero), ε_zero=1e-10. **zero-on-both → Reading-A.**

*Output 4-tuple*: `(value=READING=Reading-A..., scheme=Gibbs-Duhem-mu-scan+order-parameter-V-scan, convention=BdG/Kosmann-S35;Wall#6-mu0-PH-symmetry, L_max=10)`. regulator_pin = N/A (state-functional slopes, NOT Seeley-DeWitt residues; the SA-side nulls are anchored structurally by Wall #6 + Kosmann, not via a tagged a_n).

*Substitution chain (substituted numbers)*:
- Step 1: `∂(vacuum)/∂μ ≡ −⟨N⟩` (Gibbs-Duhem). On the signed spectrum, `S_SA(μ)=Σ m_k f((λ_k−μ)²+Δ²/Λ²)` is even in μ about μ=0 ⇒ `dS_SA/dμ|_0 = 0.000` (computed exactly, both cutoffs).
- Step 2: `∂(condensation)/∂V` of the order parameter. `S_SA` depends on V only through Δ(V) ⇒ at fixed Δ, `dS_SA/dV = 0.000` (V absent from D²_BdG).
- Step 3 (SA-side prediction, Reading-A): Wall #6 (μ=0 PH-symmetry) forces slope 1 = 0; S35 Kosmann (V ∉ dom Tr f) forces slope 2 = 0 ⇒ IF the CC is purely a Tr f(D²) object, BOTH = 0. **Both computed = 0.000.**
- Step 4 (compute): finite difference on the L10 signed spectrum (Δ_BCS=0.4642547, E_cond=−0.13685). slope1=0.000, slope2=0.000.
- Step 5 (read-off): zero-on-both (|slope| ≤ ε_zero) ⇒ **Reading-A**: the CC-selecting d.o.f. is OUTSIDE {Tr f} (Layer-B Gibbs-Duhem, SA-disjoint).

*Methodology note (in-session structural correction; honest disclosure per `v3-closure-recovery.md` Class-1 boundary).* Draft-1 loaded only `|λ_k|` (a one-sided gapped spectrum), which broke the PH symmetry and produced a spurious `dS/dμ = 4.83e-3 ≠ 0` (false Reading-B), a NEGATIVE `d²S/dμ² = −7.5e6` contradicting the S34 local-minimum sign, a broken Gibbs-Duhem identity (resid ~1.0), and a failed GPU validation (resid 0.50). All four diagnostics flagged the construction as unfaithful. The fix — using the **signed Nambu spectrum `{±|λ|}`** that the S35 `H_BdG` Hilbert space `H_K⊕H_K` actually carries — restored all four cross-checks: dS/dμ=0 exactly, d²S/dμ²=+2.38e6 (S34 sign), Gibbs-Duhem resid=0, GPU resid=2.66e-16. The correction was NOT a convention swap to reach a target verdict (Class-1 PROHIBITED); it was a faithfulness fix forced by contradiction with the established S34 result, applied before any verdict was emitted.

*atlas-04 S3 CORE-cell consequence.* Reading-A (PASS) confirms numerically that the CC's selecting degree of freedom is irreducibly Layer-B (Gibbs-Duhem order-parameter object on the (μ,V) domain), structurally DISJOINT from the spectral triple's functional Tr f(D²). **WS-SA-FREE-ENERGY collapses to housekeeping** (the R0 prelude returns Reading-A, not Reading-B). HK-SA-LAYER applies (atlas-04 S3 down-scope to Layer-A confirmed); HK-SA-RETAG to "SA = correct modulus action" stays gated as before. The S6 open channel "does spectral action = phonon free energy hold rigorously?" is answered for the VACUUM: the SA is the effective action on Layer A (spectral geometry), and Layer B (the vacuum/CC) sits OFF it on the order-parameter axis.

**Constraint-map update**:

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-20 | S110-CF-CCDARK2-MU (μ-discriminator) | UNCOMPUTED | PASS (Reading-A) | Both SA-side slopes ∂(vac)/∂μ and ∂(cond)/∂V|_Δ = 0.000 EXACTLY on the L10 signed D_K spectrum; CC confirmed Layer-B Gibbs-Duhem (Wall #6 + S35 Kosmann numerically verified) |
| 2026-06-20 | WS-SA-FREE-ENERGY (R0 gate) | scheduled (fires iff Reading-B) | collapses to housekeeping | R0 prelude returned Reading-A; the SA functional channel does NOT reach the CC |
| 2026-06-20 | atlas-04 S3 CORE cell (SA-as-free-energy) | open since S6 | Layer-A down-scope confirmed numerically | The CC-selecting d.o.f. is OUTSIDE {Tr f}; Tr f is the Layer-A effective action, the vacuum sits off it on the (μ,V) order-parameter axis |

---

### §W2-6. S110-CF-CCDARK1-BBN (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CCDARK1-BBN`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (non-thermal BBN-relief channel; the one REAL derived tension)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: Adding a PRE-REGISTERED non-thermal exchange term (parametric/Floquet pair-transfer in the §VII.BP band ω_q=2.0128 M_KK, OR a substrate-internal leak) to the inv-11 W4-1 two-fluid ODE relieves ρ_vac/ρ_rad at BBN from 0.474049 below the substrate-derived bound 0.22710731766 with sign=PASS retained — escaping the gap-suppression that killed the thermal route (53.8× short) and the de Sitter route, WITHOUT post-hoc tuning (dual prior 0.3 PASS / 0.7 FAIL-also-gap-suppressed).

**Output Artifacts** (closure-verification checklist; mirrors the plan's `output_artifacts:` block):
- Script: `computations/session-110/s110_cf_ccdark1_bbn_nonthermal.py` — present; `grep -E "from canonical_constants import|print_verdict_payload"` both match (imports the 6 canonical constants; defines `print_verdict_payload`).
- Data: `computations/session-110/s110_cf_ccdark1_bbn_nonthermal.npz` — present (81,164 bytes).
- Plot: `computations/session-110/s110_cf_ccdark1_bbn_nonthermal.png` — present (278,268 bytes; 4-panel: scan vs coupling, §VII.BP Floquet-DEAD bar, |Δ| sink bar, coupled-decay trajectories).
- Verdict line: `computations/session-110/s110_gate_verdicts.txt` — canonical line matches `^S110-CF-CCDARK1-BBN:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=9c971ad2…b4ed81d`), with dual-SHA companion row + the `[SIGN]` 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + 2 extra rows (regulator_pin N/A; source-recon drift note).
- WP section: this section (Status COMPLETED, Verdict FAIL, Output Artifacts, MCP Pre-Compute Audit all present).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; no closure pre-covers the non-thermal-channel question):
- `get_constant("rho_vac_over_rho_rad_BBN_below")` → 0.474049 (S98, n_eff=1.978 from-below; the no-exchange BBN fraction the gate must relieve). Confirms the canonical anchor matches the inv-11 W4-1 npz.
- `search_knowledge("CCDARK BBN two-fluid coupled-decay non-thermal gap-suppression …")` → the only landed BBN-relief gate is S99-W2-BBN-RELIEF **FAIL** (RVM RG-running route, relief_factor short); no non-thermal-channel gate exists. Gate is NOT pre-closed.
- `search_knowledge("VII.BP pair band omega_q 2.0128 Floquet parametric pair-transfer")` → §VII.BP is the H-PARITY-DRIVE-EXCLUSION theorem; drive ω_q^phys = 2.012813 M_KK (S101-W1). No prior non-thermal-exchange compute.
- Read `sessions/session-110/workshops/ws-floquet.md` (this session's WS-FLOQUET) → **DECISIVE**: the §VII.BP in-band resonance is **DEAD-by-depth**. Physical Mathieu depth `h_par = 8.3e-4` (inv-10's `q≈0.504` was occupation-energy-per-pair mis-mapped onto the depth slot, ~607×); `fraction_resonance = 0 EXACT`, `max|Tr M| = 1.99999 < 2`, `Re μ_F = 0 EXACT`. This pins the Floquet sub-channel's enhancement to unity BEFORE the run.

**Verdict**: **FAIL** — composite (`sign_verdict=PASS`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`).
- Output 4-tuple: `value=…rho_vac_rho_rad_BBN_nonthermal=0.467614;cleared=False;g_nonthermal=3.0000e-04;factor_short=53.845x…`, `scheme=two-fluid-coupled-decay-ODE+NON-thermal-exchange`, `convention=non-thermal-channel-PRE-REGISTERED-Floquet-pair-transfer-OR-internal-leak`, `L_max=10`.
- Dual-SHA (full 64-char): `audit_sha256=9c971ad20d98a63bf685b5c15b1d211f9177d531604f6bc2340e96852b4ed81d`, `content_sha256=8e0c871fdde04a466ce4b20df2acde1503584d776fbe451e29447ebd1c90c9a1`. SHA-unique against all prior session-110 verdict lines (sig_5 PASS).

**Results**:

**The PRE-REGISTERED non-thermal channel (declared before the run; substrate-DERIVED; no functional-shopping).** Two sub-channels, each pinned to a substrate-derived coupling BEFORE re-integrating the ODE:

1. **Parametric / Floquet pair-transfer in the §VII.BP band** (ω_q = 2.012813 M_KK). The pair-transfer rate per e-fold is the base impedance throughput (1−Γ_eff) ENHANCED by the parametric growth-per-drive-period factor `G_para = exp(Re μ_F · T_period)`, with `T_period = 2π/ω_q = 3.1216 M_KK⁻¹`. The Floquet exponent `Re μ_F` is **not a free knob** — it is pinned by the WS-FLOQUET S110 converged verdict (this session): at the physical depth `h_par = 8.3e-4`, every one of the 1248 relic modes sits in a Mathieu stability gap, so **`Re μ_F = 0` EXACT** (`max|Tr M| = 1.99999 < 2`). Therefore `G_para = exp(0) = 1` and `g_para = (1−Γ_eff)·1 = 3.0×10⁻⁴` — the parametric channel adds **no enhancement**. The counterfactual depth that would first catch the nearest-a=1 relic mode (|A−1|=0.035) is `h_par_crit = 0.0725` — a miss-factor of 87.35× over the substrate-delivered `8.3e-4` (the WS-FLOQUET text figure 84.34× used a slightly different intermediate; both are diagnostic-only and non-verdict-gating).
2. **Substrate-internal (non-Boltzmann) leak** = the raw effacement impedance-mismatch transmission (1−Γ_eff) = 3.0×10⁻⁴, read WITHOUT the `exp(−Δ/T)` Boltzmann pair-breaking factor. This is the maximal substrate-derived non-thermal coupling (the effacement channel IS the substrate's own non-Boltzmann leak; its strength is fixed at 3e-4 by S37).

The pre-registered coupling is `g_nonthermal = max(g_para, g_internal) = 3.0×10⁻⁴`. Both sub-channels land at 3e-4 because the parametric enhancement is unity — the §VII.BP resonance is Floquet-dead at the physical depth.

**Substitution chain (with substituted numbers):**
- Step 1: ρ_vac/ρ_rad|_BBN (no exchange) = **0.474049** (canonical S98; = inv-11 W4-1 npz `rho_vac_rho_rad_BBN_no_exchange`).
- Step 2: substrate-derived bound = **0.22710731766023898** (inv-11 W4-1 npz; NOT the round 0.2 — the exact ΔN_eff=1 bound (7/8)(4/11)^{4/3}).
- Step 3: rescue must remove δ_needed = 0.474049 − 0.227107 = **0.246942**, requiring `g_eff_needed = 0.0161535898` (inv-11 npz; closed-form cross-check `−ln(bound/f0)/efolds = 0.0161535898`, |Δ| = 0.00e+00).
- Step 4: thermal baseline `g_eff_substrate = 3.0×10⁻⁴` → `factor_short = 53.845` (thermal route DEAD, gap-suppressed by `exp(−Δ/T)` with `Δ_BCS ≈ 0.4643`).
- Step 5: non-thermal candidate `g_nonthermal = max(g_para=3e-4, g_internal=3e-4) = 3.0×10⁻⁴` (NO enhancement: §VII.BP Floquet-dead). `relief = exp(−g_nonthermal · efolds) = exp(−3e-4 · 45.5557) = 0.986426` ⇒ ρ_vac/ρ_rad|_BBN = 0.474049 · 0.986426 = **0.467614**.
- Direction: `sign = PASS` (the bleed is a strict SINK on ρ_vac, Δ_BBN = −0.006435 < 0). `magnitude = FAIL` (0.467614 > 0.227107; |Δ| removed = 0.006435 ≪ 0.246942 needed; **factor_short = 53.845×, IDENTICAL to the thermal route** because the parametric enhancement is unity at the physical depth).
- Two-sided Ω check (full coupled ODE): Ω_vac,today = 0.6850, Ω_DM,today = 0.2657 (boundary-preserved; the present-day composition is unperturbed at O(g)~3e-4).
- Conclusion: **FAIL** hardens the BBN over-production wall.

**g_eff scan** (60 pts, linear, [3e-4, 0.0162] per plan): ρ_vac/ρ_rad|_BBN ∈ [0.226628, 0.467614]. The bound is crossed only at the top of the scan (at `g_needed = 0.0161535898`); the substrate-delivered `g_nonthermal = 3e-4` lands at the floor (0.467614).

**Source-reconciliation note (class-(c) PIN-DRIFT-FROM-STALE-SOURCE, BENIGN).** The runtime `canonical_constants.py` SHA (`89c9b086…`) differs from the plan-frozen pin (`e5a7587f…`) — in-session W2 edits promoted other constants between plan-freeze and runtime. Per `substrate-first-canonical-sourcing.md §(ii.B)`, the runtime SHA is ground truth; the six constants this gate consumes are **unchanged** at their canonical values (`rho_vac_over_rho_rad_BBN_below = 0.474049`, `Gamma_effacement = 0.99970`, `Delta_BCS`, `w0_FW = −0.918`, `M_KK`, `tau_fold`). The inv-11 W4-1 npz SHA (`8675f970…`) matches the plan pin EXACTLY (the thermal-baseline source-of-truth is bit-stable). Drift documented in the verdict `value=` field and an extra companion row.

**Constraint-map update.** The non-thermal BBN-relief corridor is **CLOSED**. The thermal (inv-11 W4-1, 53.8× short), de Sitter (inv-11 W4-3, Γ_dS underflow), AND non-thermal (this gate, 53.8× short — Floquet-dead + bare effacement leak) routes are all closed. The BBN over-production wall (ρ_vac/ρ_rad|_BBN = 0.474 = 2.06× the substrate bound 0.2271; ΔN_eff = 2.087) is **non-relievable by any substrate-derived exchange channel**. This is a genuine closed corridor, not an agent failure: it maps the boundary that the q-theory tracking vacuum's H²-freedom — the same freedom the CC closure (DILUTION-CC) needs — necessarily pays at BBN. Per the dual-prior discriminator (FAIL → 0.9 Track B), the tension routes to **WS-CC-H₀** as the concrete cost of the tracking freedom, and feeds atlas-04 C10 (HK-C10 "scaling-form DERIVED + BBN-FALSIFIED-at-2.06×" stands, now with all three relief routes closed).

**Substrate framing.** PHONONIC. Dark energy IS the effacement residual + the tracking-vacuum a₀ leg; the CC IS the q-theory zero-point ρ_vac(q,T) ~ M_Pl² Hⁿ. The two "fluids" are the two-leg decomposition of ONE vacuum surface (a₀/effacement leg w=−0.918 + q-theory matter leg w=+1), NOT two relic species in a container. The BBN over-production reads the SAME derived ρ_vac(q,T) surface at the BBN epoch (flat in T to BBN, n_eff=1.978). The arrow: D_K eigenfrequencies → ρ_vac(q,T) tracking surface → the §VII.BP relic-mode Floquet monodromy (h_par = 8.3e-4, gap-confined) → the non-thermal pair-transfer coupling g_nonthermal = 3e-4 → the re-integrated BBN-epoch vacuum fraction 0.467614. The deepest substrate reason the channel is dead is one fact viewed twice: *the impulsive Mach-13.75 transit that froze the relic (Ordered Veil, S_ent=0) leaves too little residual modulus drive (h_par = 8.3e-4) to re-pump it* — the same smallness that protects the relic forecloses the parametric pair-transfer that could have drained the vacuum.

---

## Wave 2 Synthesis (team-lead)

**Tally**: 6 gates — 2 PASS (CCDARK-2, CV2A), 2 INFO (B1, CF1-AT), 2 FAIL (AS2, CCDARK1). All pre-registered outcomes; sig_5 clean (6 distinct audit_sha256); all artifacts on disk; all 6 WP §-sections COMPLETED.

**What changed (W2→W3 / W2→W1 seams)**:
- **CV2A PASS → CV2B (§W3-1)** — the M_KK keystone acquires its first SESSION-grade derivation corridor: `M_KK/M_Pl = exp(−1/(λ_eff·N₀))`, oom_distance=0.7202 ≤ 1.0, frac_uncert_gap_term=0.8298 (gap-magnitude carries 83% of the OOM budget ⇒ a DERIVATION, not a fit; cutoff-normalization diagnostic oom_unred=1.4203 EXCLUDED from the PASS set). Register stays gravity-a₂ frozen-since-S42 (HK-MKK); the status NOTE lands at W3-close after CV2B's Question-B canonical-value fork. Also the discriminator the WS-CC-H₀ O2/O3 H₀ question routes to.
- **CCDARK1 FAIL → WS-CC-H₀** — the non-thermal BBN-relief channel is ALSO gap-suppressed (g_eff=3e-4, 53.845× short of g_eff_needed=0.0162; Floquet sub-channel Re μ_F=0 EXACT at h_par=8.3e-4, confirming WS-FLOQUET=DEAD). Thermal + de Sitter + non-thermal routes all closed ⇒ the BBN over-production wall (ρ_vac/ρ_rad=0.468 > bound 0.227) HARDENS. CONFIRMS the WS-CC-H₀ verdict: BBN ΔN_eff=2.06× is the tracking-vacuum's sole w-free falsifiable cost.
- **AS2 FAIL** — the A_s exit-FILTER leg is bounded-but-filter-FITTED: 0.512 has no substrate scale on EITHER the static (∫Γ≈0.036) OR the dynamical near-horizon channel where the WKB greybody is valid (regime=BREAKDOWN, domain_used_frac=0.143). The last open leg of the A_s wall closes as non-substrate. FLOOR `A_s≥A_s^{BD}` permanent on 3 axes (orthogonal; WS-AS-1).
- **B1 INFO → CV6B (§W3-6) / CF-S111-AS3** — TRANSIT-PS-67 SHAPE promotes (Track B): pivot n_s=0.9561 (|dev|=0 in 0.003 band) + |α_s|=0 < 0.019 + truncation_consistent + BZ-leaf k³-blue n_s=2.9998 diagnostic; deg(T_{BZ→pivot})=+2 NON-SCALAR carries the geometric tilt 54.04 decades (re-derived ONCE in CV6B §W3-6). regime=MARGINAL (89/89 frozen-superhorizon) ⇒ composite INFO (plan-frozen-operator precedence disclosed). Amplitude/regime → CF-S111-AS3.
- **CF1-AT INFO=SPLIT → WS-CLOCKLOC CF-2** — the a(t) backbone FORM is reduction-scheme-dependent: gap-as-density-ceiling → MONOTONE (a₄ R²+Weyl² pure-curvature, contributes 0 to ∂H²/∂ρ, Sage-verified); holonomy-analog → turning-point at ρ_relic/2, SPLIT. V_spec-monotone (S24a) = DISTINCT functional (no contradiction; p_S75 ≠ p_cosmo). CV-3 residual pinned to a scheme-discrimination question → forward home = the WS-CLOCKLOC CF-2 composition gate.
- **CCDARK-2 PASS** — Reading-A (both SA-side slopes 0); CC is Layer-B Gibbs-Duhem, SA-disjoint (collapsed WS-SA-FREE-ENERGY; W1).

**Process observation (closed in-session, NOT a carry-forward)**: `canonical_constants.py` byte-SHA drifted plan-pin `e5a7587f…` → runtime `89c9b086…` (S110 W0a T_acoustic / Ω_DM / φ_paasch PROVENANCE backfills — NO value change). All four affected gates (B1, CV2A, AS2, CCDARK1) detected it at runtime, verified the consumed constant VALUES intact, and pinned the runtime SHA per `substrate-first-canonical-sourcing.md §(ii.B)` (benign class-(c) PIN-DRIFT).

**Effected In-Session (non-math)**: the atlas-04/§VII **M_KK status NOTE** (keystone OPEN → transmutation-corridor PASS; register cell stays gravity-a₂ frozen) is sequenced to **W3-close** — it lands jointly with the CV2B (§W3-1) canonical-value verdict so the curated atlas-04 M_KK cell is edited once with the complete corridor-PASS + canonical-value picture (within-session wave-pair sequencing, NOT next-session deferral). No falsifier-surface edit owed by W2 (the A_s / BBN surfaces were effected in the W1 mack pass: Row #12, Row #76).

## Carry-Forward Computations

Most W2 outputs are consumed WITHIN S110 (CV2A → CV2B §W3-1; B1 deg(T_{BZ→pivot}) → CV6B §W3-6) or confirm existing W1 carry-forwards (CCDARK1 FAIL → the WS-CC-H₀ CF-S111-MKK-RG-INVARIANCE; CF1-AT SPLIT → the WS-CLOCKLOC CF-2 composition gate). The genuine NEW S111 math carry-forward:

### CF-S111-AS3 — A_s number/band pin + all-frozen-superhorizon regime resolution

1. **What**: pin the TRANSIT-PS-67 amplitude A_s (number + band) from the impulse-quench |β_k|² functional, resolving the all-frozen-superhorizon regime (B1 INFO regime=MARGINAL: 89/89 frozen, WKB-Bogoliubov leg empty), and decide the magnitude epistemic type per the WS-AS-1 Reading-A-conditional Friedrich-Bär-temp PASS.
2. **Inputs**: `inv10_w2_transit_ps_build.npz` (locked {β_k}); `s110_cf_b1_transit_ps_promote.npz` (two-leaf build); the WS-AS-1 verdict (`ws-as-1.md`); the nazarewicz Friedrich-Bär truncation-saturation argument.
3. **Gate**: A_s within a pre-registered relic-squeezing band AND the FB-temp PASS converting WS-AS-1's conditional Reading-A to unconditional; regime resolved.
4. **Effort**: ~1 wave (the {β_k} are locked; new work = the amplitude functional + the FB-saturation check).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-20 | M_KK-DERIVATION (CV2A) | keystone OPEN, frozen-fit unknown status | transmutation-corridor PASS (oom 0.72, gap-term 83%); register stays gravity-a₂ frozen (HK-MKK) | BCS dimensional transmutation from the van Hove fold DOS, session-grade |
| 2026-06-20 | BBN over-production (CCDARK1) | thermal + de Sitter routes closed | ALL exchange routes closed (non-thermal 53.8× short); wall HARDENS = tracking-freedom cost | non-thermal channel gap-suppressed (Floquet Re μ_F=0 at h_par=8.3e-4) |
| 2026-06-20 | A_s exit-filter (AS2) | 0.512 filter, substrate-scale unknown | bounded-but-filter-FITTED (no substrate scale, static or dynamical, where WKB valid); FLOOR permanent | dynamical near-horizon scan + WKB regime BREAKDOWN |
| 2026-06-20 | TRANSIT-PS-67 (B1) | investigation-track build | SHAPE promotes (Track B): pivot n_s=0.9561 + \|α_s\|<0.019 + truncation_consistent; amplitude/regime → CF-S111-AS3 | session-gate two-leaf reproduction; regime MARGINAL |
| 2026-06-20 | a(t) backbone form (CF1-AT) | a₄-sign question | scheme-dependent (SPLIT): MONOTONE under gap-ceiling, turning-point under holonomy → CF-2 composition gate | both reduction schemes run; V_spec-distinct |
| 2026-06-20 | canonical_constants.py SHA | plan-pin e5a7587f | runtime 89c9b086 (W0a provenance backfills, NO value change) | benign class-(c) PIN-DRIFT; runtime-SHA-pinned in-session (process observation) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) |
|:-----|:-------|:------------|:------------|
| S110-CF-B1-TRANSITPS | s110_cf_b1_transit_ps_promote.py | ✓ | ✓ |
| S110-CF-CV2A-MKK-TRANSMUT | s110_cf_cv2a_mkk_transmut_promote.py | ✓ | ✓ |
| S110-CF1-AT-MINISUPERSPACE | s110_cf1_at_minisuperspace.py | ✓ | ✓ |
| S110-CF-AS2-GREYBODY | s110_cf_as2_greybody_scan.py | ✓ | ✓ |
| S110-CF-CCDARK2-MU | s110_cf_ccdark2_mu_discriminator.py | ✓ | ✓ |
| S110-CF-CCDARK1-BBN | s110_cf_ccdark1_bbn_nonthermal.py | ✓ | ✓ |

All in `computations/session-110/`; verdict lines + dual-SHA companions in `s110_gate_verdicts.txt`.
