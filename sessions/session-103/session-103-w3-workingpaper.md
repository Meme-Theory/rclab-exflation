# Session 103 Wave 3 — Transit / Holonomy (Results Working Paper)

**Session**: 103 | **Wave**: W3 | **Plan**: session-103-plan-w3.md | **Theme**: Two transit/holonomy carry-forwards from S102 W7 — a Class-8.3 publication-precision F_amp tolerance re-pin and the orthogonal C² coset doublet Wilczek-Zee holonomy witness.

## Gate Sections

### §W3-1. S103-FAMP-TOLERANCE-REPIN (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S103-FAMP-TOLERANCE-REPIN`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (Class-8.3 publication-precision re-pin of a frozen comparator)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: Re-pinning the phase-resolved F_amp comparator's PASS_TOL to the exact asymmetric upper-envelope edge S_W_max−1, not the down-rounded literal 0.0029 nor the symmetric half-spread 2|a||b|, re-evaluates the frozen S102 deviation 2.915087e-03 against the endpoint it physically saturates.
**Plan reference**: `sessions/session-plan/session-103-plan-w3.md` §W3-1 (machinery pin, exact-edge threshold, substitution chain source).

**Verdict**: **INFO** (composite collapse: sign=PASS, magnitude=INFO, regime=VALID). The re-pin RESOLVES the sign and VINDICATES the substrate, but the knife-edge SURVIVES at publication precision.

#### Numbers first (frozen S102 npz re-read; no new physics)

| Quantity | Value (full float64) | Provenance |
|:---------|:---------------------|:-----------|
| `deviation` (value under test) | `2.9150874232022560e-03` | frozen `s102_w7_ladder_phase_resolved.npz` field `deviation` |
| **re-pinned** `PASS_TOL := S_W_max−1` | `2.9150926342005334e-03` (5sf `2.9151e-3`) | frozen field `envelope_upper_dev` |
| `deviation − PASS_TOL` | `−5.210998e-09` (`≤ 0`) | re-derived |
| `|a|=|α_W|`, `|b|=|β_W|`, `b²` | `1.0000010591`, `1.4554265e-03`, `2.118266e-06` | frozen `abs_alpha_W` / `abs_beta_W` / `beta2_W` |
| unitarity `|a²−b²−1|` | `2.22e-16` | CC2 Bogoliubov identity (machine ε) |

**Re-pinned PASS_TOL** = `S_W_max − 1` = the frozen `envelope_upper_dev`, full float64 `2.9150926342005334e-03`, published at 5 sig figs `2.9151e-3` (Class-8.3 pin; round-trip: full float64 → npz, rounded → this WP).

#### The three candidate edges (only the EXACT one is physically correct)

| Edge | Value | `deviation − edge` | Disposition | Reproduces frozen field |
|:-----|:------|:-------------------|:------------|:------------------------|
| **EXACT** `S_W_max−1` (re-pin) | `2.915093e-03` | `−5.211e-09` | **at-or-inside** (sign PASS) | — |
| symmetric half-spread `2|a||b|` | `2.910856e-03` | `+4.231e-06` (>0) | wrong edge (FAIL) | `dev_vs_half_spread` (resid 0.0) |
| down-rounded literal `0.0029` | `2.900000e-03` | `+1.509e-05` (>0) | wrong edge (FAIL; the S102 pin) | `dev_vs_pass_tol` (resid 0.0) |

Both wrong-edge deltas reproduce the frozen S102 fields bit-for-bit (residual 0.0e+00), confirming the re-read is faithful.

#### Substitution chain (MANDATORY [SIGN]; exact-threshold + direction)

- **Def 1**: `S_W(φ) := |α_W + β_W e^{2iφ}|²` (SU(1,1) phase-resolved window factor; convention SU(1,1)-form-1).
- **Def 2 (unitarity)**: `|α_W|² − |β_W|² = 1` ⇒ `a² = 1 + b²`. [npz: `a²−b² = 0.9999999999999998 ≈ 1`.]
- **Def 3**: `deviation := |F_amp_phase/F_amp_slot_mag − 1| = |S_W(φ) − 1|` = `2.9150874e-03`. [npz `F_amp_phase=0.38963251`, `F_amp_slot_mag=0.3885`.]
- **Substitute + extremize**: `S_W(φ) = a² + b² + 2ab·cos(2φ+δ)`. With `a² = 1 + b²`: `S_W = 1 + 2b² + 2ab·cos(…)`. Hence **center = 1 + 2b²** (npz `S_W_center`, resid `2.2e-16`) and **half-spread = 2ab** (npz `S_W_half_spread`, resid `1.5e-16`).
- **Exact upper edge**: `S_W_max − 1 = (center−1) + half-spread = 2b² + 2ab` = `2.9150926342e-03`, **bit-exact** vs frozen `envelope_upper_dev` (resid `7.6e-17`).
- **Direction (sign read-off)**: `deviation − (S_W_max−1) = 2.9150874e-3 − 2.9150926e-3 = −5.21e-09 ≤ 0` ⇒ **sign PASS** (predicted `≤ 0` matches computed). The DERIVED phase lands at the upper edge (`cos_phi_off_axis = 0.99999966 ≈ +1`), so the deviation **saturates** the asymmetric upper endpoint it physically arises from (`within_envelope = True`).

**Bit-exact-vs-shorthand precision finding (the Class-8.3 content).** The bit-exact decomposition of the frozen `envelope_upper_dev` is `S_W_max − 1 = 2b² + 2ab` (resid `7.6e-17`). The plan/predecessor shorthand `S_W_max−1 = 2|a||b| + |β_W|²` (= `b² + 2ab`, plan lines 67/156; predecessor companion row line 930) UNDER-counts by exactly one `b²`: it measures the spread about the OFFSET center `1 + 2b²` then adds back only one `b²`, not two. `b² + 2ab = 2.9129744e-03` disagrees with the frozen edge by `b² = 2.118e-06` and **fails the 5-sig-fig publication pin** (`2.9130e-3` vs `2.9151e-3`). The threshold VALUE is unaffected because `PASS_TOL` is sourced directly from the frozen `envelope_upper_dev` field, not reconstructed from `a, b`. The asymmetry `env_up − |env_lo| = 8.473065e-06 = 2b²` (resid `4.2e-06`) confirms the SU(1,1) window is asymmetric about 1.

#### Why INFO, not PASS (pre-registration-faithful verdict)

The pre-registered OPERATOR (plan lines 65–72) is the pure inequality `deviation ≤ PASS_TOL`, `direction: "≤"` — under which the bare comparison is true (`2.9150874e-3 ≤ 2.9150926e-3`, margin `+5.21e-09`). BUT the plan ALSO pre-registers a sharper `INFO_meaning` (lines 260–263): INFO iff `deviation == S_W_max−1` **to within publication precision** (knife-edge persists; "a precision pathology deeper than the down-rounding"). The data triggers exactly this clause:

- `deviation` (5sf) = `2.9151e-3`; `PASS_TOL` (5sf) = `2.9151e-3` → **identical at 5 sig figs** (and at 6 sig figs: `2.91509e-3` both).
- Relative separation `|deviation − PASS_TOL| / PASS_TOL = 1.79e-06` sits at the **5.7th significant figure**, below the pinned 5-sf publication precision (`rel_tol = 1e-5`).

So the deviation does PASS the bare inequality but does NOT clear the exact edge by more than publication precision — it sits ON the edge at 5sf. Forcing PASS by dropping the publication-precision band would be reverse convention-shopping (picking the bare-inequality reading specifically because it yields the hypothesis-predicted PASS while ignoring the co-pre-registered INFO clause). The honest verdict is **magnitude=INFO ⇒ composite INFO** via the generic collapse rule (`regime=VALID, sign=PASS, magnitude=INFO ⇒ INFO`). Dual-prior (plan line 214): `INFO ⇒ track priors unchanged`.

**What the re-pin accomplished** (vs the S102 INFO it re-pins): (i) **resolved the sign** — the deviation is at-or-inside the exact physical edge; the half-spread and literal 0.0029 were both the wrong comparison edge; (ii) **vindicated the substrate** — the deviation saturates the upper envelope endpoint, `within_envelope=True`, so the S102 INFO is NOT a substrate breach; (iii) **did NOT** convert the knife-edge to a margin — the deviation equals the exact edge to publication precision. The F_amp slot `0.3885` (UNIFIED-AS-79 k_a2 POWER-RATIO factor, CC2=+1) and the S79 magnitudes-only ladder anchor are undisturbed (slot value unchanged; the DERIVED relative phase only modulates the slot within the S_W window envelope).

**Carry-forward** (genuine future compute): higher-precision (mpmath / Sage 300-bit) S_W_max re-derivation to decide whether `deviation < S_W_max−1` strictly or `==` below the float64 floor (the knife-edge is at the 5.7th sig fig; float64 cannot discriminate `<` from `==` at publication precision). 4-field spec — *what*: re-derive `S_W_max` and `deviation` from the frozen B-stage Bogoliubov amplitudes at 300-bit; *inputs*: frozen `s102_w7_ladder_phase_resolved.npz` (W_alpha/W_beta re/im) + the S_W extremization; *gate*: `deviation < S_W_max−1` strict (PASS) vs `==` to 300-bit (INFO-persists); *effort*: 0.1 gate.

**Substrate framing**: PHONONIC. The F_amp slot is the UNIFIED-AS-79 amplification factor mapping fold-transit GGE-relic pair-production magnitudes into A_s. Flow: `D_K(τ)` trajectory through the van Hove fold → SU(1,1) Bogoliubov coefficients `(α_W, β_W)` of the W-stage → phase-resolved window `S_W(φ) = |α_W + β_W e^{2iφ}|²` → F_amp slot → A_s. The SU(1,1) phase window is ASYMMETRIC about 1 because the unitarity offset puts the center at `1 + 2|β_W|²`, not 1; the exact upper edge is `2|β_W|² + 2|α_W||β_W|`. This gate corrects a methodology-floor artifact (a down-rounded literal threshold tested against a value that physically saturates the asymmetric endpoint) WITHOUT touching the substrate physics — every Bogoliubov amplitude is re-used verbatim from the frozen S102 npz. The re-pin restores F-consistency between the comparator's PASS predicate and the SU(1,1) window it tests against; the residual knife-edge is a float64-precision question, not a substrate question.

**Output Artifacts** (all verified on disk by content):

- **script** `computations/session-103/s103_famp_tolerance_repin.py` — must_contain PASS:
  - `L125: from canonical_constants import *` ; `L126: from canonical_constants import M_KK, max_f_NL_FW`
  - `L240/L801: print_verdict_payload(...)`
- **data** `computations/session-103/s103_famp_tolerance_repin.npz` — exists (17473 bytes; ~50 fields incl. re-pin observable, decomposition cross-checks, drift block).
- **plot** `computations/session-103/s103_famp_tolerance_repin.png` — exists (66364 bytes; 1-D envelope diagram: deviation marker vs the three candidate edges literal 0.0029 / half-spread 2|a||b| / exact S_W_max−1, with admissible-region shading + asymmetry annotation).
- **verdict_line** `computations/session-103/s103_gate_verdicts.txt` L21 (canonical, matches `^S103-FAMP-TOLERANCE-REPIN:.* audit_sha256=[a-f0-9]{64}`):
  `audit_sha256=3455a7dacc8f756285a124c54d807c04d749aa234a6bd3a35ea63e05a0698d5f` `content_sha256=afee0d3f4606d693866deaa0e8b0205a2c36d3a7d153ffede37dc77f544a2f2e`. Dual-SHA companion row L22; `[SIGN]` 3-tuple companion row L23 (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`); 8 extra annotation rows (RE-PIN / BIT-EXACT / RE-EVAL / ASYMMETRY / DUAL-PRIOR / CANONICAL-DRIFT / write_order / regulator_pin). Emitted via race-safe `mcp__knowledge__emit_verdict` (11 rows, sig_5 unique).
- 4-tuple: `(value='PASS_TOL_repin=2.915093e-03;…;S102_was=INFO->repin=INFO;canon_drift=Y_appendonly_rePinned', scheme=FW, convention=SU(1,1)-form-1-temporal-L-to-R, L_max=12)`.

**MCP Pre-Compute Audit**:

- `search_knowledge("FAMP TOLERANCE REPIN phase-resolved S_W envelope asymmetric edge ladder")` → returned the S102 W7-2 predecessor session + the `S_W=[0.997093,1.002915]` window-factor equation; **NO** prior evaluation of `S103-FAMP-TOLERANCE-REPIN` (gate is NOT pre-closed; this re-pin is new).
- `get_constant`/`search_knowledge` — not needed for a threshold pin sourced from the frozen npz field `envelope_upper_dev`; the gate consumes NO canonical value as a comparison edge (`M_KK`/`max_f_NL_FW` imported for provenance-sanity only, not in any threshold).
- **Methodology note (process observation, in-session)**: `canonical_constants.py` SHA drifted plan-freeze `9f2fe998…` → runtime `9cd89e61…` by a parallel S103-wave APPEND (`n_s_FW_sqrt_cutoff`, `x696_ncg_coincidence_headroom_ratio`, `BF_spine_vs_incumbent_ceiling` + PROVENANCE). NONE is consumed by this gate. Handled per `substrate-first-canonical-sourcing.md §(ii.B)` (plan-text-drift): re-pinned to runtime canonical, `audit_sha256` computed over current bytes, drift disclosed in the verdict `value=` (`canon_drift=Y_appendonly_rePinned`) + companion row + npz. The frozen-npz file-byte SHA (`b70d78bf…`, the gate's sole physics input) is UNCHANGED and asserted HARD → the gate is TESTABLE, NOT mechanical-closure. Not a workshop/carry-forward (already-correct handling of an additive-only mutation).

---

### §W3-2. S103-B2-WZ-HOLONOMY-COSET2 (berry-geometric-phase-theorist)

**Status**: COMPLETED
**Gate ID**: `S103-B2-WZ-HOLONOMY-COSET2`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (frame-invariant Wilczek-Zee holonomy witness on a new coset doublet)
**Agent**: `berry-geometric-phase-theorist`
**Hypothesis**: The frame-invariant WZ Wilson-loop witness on the orthogonal off-block C² coset doublet (array-indices [3,5]) reproduces a genuine non-abelian O(ε²) holonomy (frame_resid<1e-10, f_WZ>1e-8, slope_angle∈[1.8,2.2]), completing the C² coset span (λ₄..λ₇) and confirming the B2 isotropy-breaking is non-abelian on the full coset.
**Plan reference**: `sessions/session-plan/session-103-plan-w3.md` §W3-2 (W7-3-verbatim machinery pins, coset re-parametrization, frame-invariance substitution chain).

**Output Artifacts** (all verified on disk by content):

| Artifact | Path | must_contain check |
|:---|:---|:---|
| script | `computations/session-103/s103_w3_b2_wz_holonomy_coset2.py` (55954 B) | `from canonical_constants import` → L142–143 PRESENT; `print_verdict_payload` → 2 hits PRESENT |
| data | `computations/session-103/s103_w3_b2_wz_holonomy_coset2.npz` (17257 B) | exists ✓ |
| plot | `computations/session-103/s103_w3_b2_wz_holonomy_coset2.png` (230278 B) | exists ✓ (loop-convergence plateau; frame-invariance bar; eps-family log-log slope-2 angle / slope-4 witness; verdict panel) |
| verdict_line | `computations/session-103/s103_gate_verdicts.txt` L4 | `^S103-B2-WZ-HOLONOMY-COSET2:.* audit_sha256=[a-f0-9]{64}` PRESENT (`audit_sha256=49705bbc…2093dc`); dual-SHA companion row L5; `regulator_pin=N/A` companion row L6 PRESENT |

Verdict line (canonical):
```
S103-B2-WZ-HOLONOMY-COSET2: PASS -- value='verdict=PASS_track=A_f_WZ=2.8888e-06_continuum=2.8889e-06_frame_resid=2.665e-15_frame_inv=True_eps_WZ=1e-08_TrU=3.999997_hol_angle=2.4037e-03_abel_phase=6.70e-15_angle_slope=1.9999_witness_slope=3.9996_nonscalar=1.0000_n_broken=4_posterior=TrackA=0.9_TrackB=0.1_RETIRED-W54-f_nonAb=8.886e+04-frame-dep-eigh-artifact' scheme=FW convention=FRAME-INVARIANT-WZ-HOLONOMY L_max=12 audit_sha256=49705bbc3ff1fda7a3778b2ef2472027c9fa18e42673873771b78133d52093dc content_sha256=458d582e67a78e228f02cdb76783b012f35988db382818f6f6510da2a7b31203 schema_version=S84+
```
- **audit_sha256** = `49705bbc3ff1fda7a3778b2ef2472027c9fa18e42673873771b78133d52093dc`
- **content_sha256** = `458d582e67a78e228f02cdb76783b012f35988db382818f6f6510da2a7b31203`

**MCP Pre-Compute Audit** (queries executed before authoring/running the re-parametrized script; per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("B2 WZ holonomy coset2 orthogonal doublet frame invariant lambda_4 lambda_6")` → surfaced only the S101-B2-ISOTROPY-BREAKING INFO base anchor + the W5-4 retired frame-dependent `f_nonAb=8.89e4` artifact + the VII.BR Schur-Rigidity theorem. **No prior frame-invariant WZ-holonomy gate on the [3,5] doublet.**
- `search_knowledge("S103-B2-WZ-HOLONOMY-COSET2 Wilczek-Zee Wilson loop isotropy breaking")` → only `S101-B2-ISOTROPY-BREAKING` (INFO, the base anchor), `s48_wilson_loop`/`s73b_wilson_loop` (unrelated prior Wilson-loop gates). **This gate-ID is un-run. CONFIRMED.**
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42, Superseded=False) — matches the plan pin TAU0.
- Input-SHA cross-check at runtime: canonical_constants `9f2fe998…` ✓, dirac_spectrum `dadba674…` ✓, w54_npz `5dbaedf1…` ✓ — all three match the plan-freeze pins (plan lines 426/429/432). Upstream W5-4 npz internal `audit_sha256` = `13617ab9…fe080` matches the context-cited closure (reported as a cross-check, NEVER the witness).
- **NOT PRE-CLOSED**: the orthogonal coset doublet witness is genuinely new (the W7-3 `next_pair=(3,5)`).

**Verdict**: **PASS** — Track A (genuine non-abelian isotropy-breaking; nontrivial frame-invariant WZ holonomy). Composite [VERIFY] collapse: the 3-conjunct membership operator `(frame_resid < 1e-10) AND (f_WZ > 1e-8) AND (slope_angle ∈ [1.8, 2.2])` = `True AND True AND True` = PASS; Schur-consistency cross-check True (no m1/m2 contradiction). 4-tuple: `(value=verdict=PASS_track=A_f_WZ=2.8888e-06…, scheme=FW, convention=FRAME-INVARIANT-WZ-HOLONOMY, L_max=12)`.

**Results**:

| Quantity | Value | Pre-reg threshold | Read-off |
|:---|:---|:---|:---|
| `frame_resid` (frame-invariance precondition) | `2.665e-15` | `< 1e-10` | PASS — 5 OOM inside floor |
| `f_WZ = |Tr U_hol − 4|` (Track-A discriminator) | `2.888785e-06` (N→∞ continuum `2.888916e-06`) | `> 1e-8` | PASS — 2.6 OOM above threshold; CONVERGES (genuine holonomy, not 1/N artifact, loop_conv_delta=2.72e-11) |
| `slope_angle` (curvature flux ‖log U‖_F ~ εⁿ) | `1.9999` | `∈ [1.8, 2.2]` | PASS — O(ε²) flux |
| `non_scalar_frac` (genuine-WZ diagnostic) | `1.0000` (‖M_ab=[A₃,A₅]‖_F = 1.5685e-01) | `> 0.5` (else m2 contradiction) | PASS — genuinely non-abelian band-index anisotropy |
| `n_broken` (residual-stabilizer, u(2) gens) | `4 / 4` (λ₁,λ₂,λ₃,λ₈ all broken) | `≥ 1` (Release condition R) | PASS — R fully released |
| witness slope `f_WZ ~ εⁿ` | `3.9996` | (~4, since f_WZ = ½·angle²) | consistent — `f_WZ/(0.5·angle²) = 1.0000` |
| abelian (det) Berry phase | `6.70e-15` | (~0) | pure SU(4); U(1) part trivial (S25 Ω=0) |

**3-conjunct membership**: `(2.665e-15 < 1e-10) ∧ (2.888785e-06 > 1e-8) ∧ (1.9999 ∈ [1.8, 2.2])` = **PASS**.

**Discriminator outcome vs the first doublet**: Track A, identical to the S102 first-doublet (4,6) outcome. `f_WZ([3,5]) = 2.888785e-06` matches `f_WZ([4,6]) = 2.8888e-06` (plan fb_pair line 447) to 4 sig figs, and `slope_angle = 1.9999` matches the first-doublet 1.9999. The two orthogonal C² coset directions carry holonomy of identical magnitude → U(2) is broken **isotropically across the full C² coset**, not just the first doublet (dual_prior re-allocation 0.6B/0.4A → TrackA=0.9_TrackB=0.1; posterior 0.9 to Track A).

**Frame-invariance cyclic-trace substitution chain** (the discriminator rests on it; carried verbatim from W7-3, holds for [3,5] by the SAME analytic identity since the [3,5] loop shares the SAME 4-fold-degenerate B2 band and the SAME projector/link construction): the witness is built from band frames F_k via the Berry link `F_{k+1}^† F_k`, polar-unitarized into `U_hol`. Under a global U(16) frame rotation V, each link `F_{k+1}^† F_k → F_{k+1}^† V^† V F_k = F_{k+1}^† F_k` is UNCHANGED; under a LOCAL intra-eigenspace gauge `F_k → F_k g_k` (g_k ∈ U(4)), the interior g_k telescope around the closed loop leaving `U_link → g_0^† (∏ links) g_0`, so `Tr(U_hol)` is invariant by trace-cyclicity. Hence `f_WZ` is frame-INVARIANT (numerically `frame_resid = 2.665e-15` over 9 frames incl. 8 SU(2)-lifted U(16) conjugations, seed 42), whereas the retired W5-4 `f_nonAb = 8.8862e+04` was frame-COVARIANT (an eigh-artifact — the W6-2 670× lesson). The B2 quadruplet is exactly 4-fold degenerate at |λ| = 0.845212 (spread 1.67e-15), so the eigh frame IS arbitrary — exactly the artifact source the projector/link witness is immune to.

**VII.BR Corollary U consistency**: T2 (Schur-scalar `M_ab|ranP = c_ab·1_4`) + Corollary U (symmetry-undecidability) hold on the U(2)-INVARIANT base; the [3,5] coset loop BREAKS U(2) (n_broken=4, Release condition R), which RELEASES the Schur lock — so Track A does NOT contradict Corollary U. The genuine non-abelian content (non_scalar_frac=1) is present precisely because the loop is OFF the U(2)-invariant base.

**Upstream-provenance cross-check** (reported, NEVER the witness): the script asserts the W5-4 npz internal `d['audit_sha256'] == 13617ab9…fe080` (the S101-B2-ISOTROPY-BREAKING closure SHA) → match=True; W5-4 `f_nonAb = 8.8862e+04` (RETIRED frame-dependent artifact) read for the retirement narrative only.

**dual-SHA + regulator_pin**: `audit_sha256=49705bbc…2093dc`, `content_sha256=458d582e…b31203` (companion row L5); `regulator_pin=N/A` companion row L6 (WZ-holonomy is not a regulator-tagged Seeley-DeWitt a_n moment — W7-3 precedent; no a_n cited).

**Substrate framing**: GEOMETRIC. The substrate's fiber at the fold carries the (1,1) adjoint; the B2 quadruplet is the rank-4 U(2)-isotypic sub-block at |λ|=0.845212 of D_K(0,0) on the U(2)-invariant volume-preserving TT surface. The flow is: D_K(τ_fold) eigenspectrum → the rank-4 B2 spectral projector P (cols 9..12) → a closed loop along the orthogonal C² coset generators (λ₄ = array-index 3, λ₆ = array-index 5; off-block `[ρ(g), dH_a] ≠ 0`) → the frame-invariant Wilczek-Zee holonomy `U_hol = polar-unitarize(∏ F_{k+1}^† F_k)` → the witness `f_WZ = |Tr U_hol − 4|`. The ε² deformation is the substrate's own off-block metric reorganization at the fold, NOT a field on a container. This gate completes the C² coset span (λ₄..λ₇): the fold's B2 isotropy-breaking is non-abelian across the **entire** coset.

---

## Carry-Forward Computations

### CF-S104-W3-SWMAX-MPMATH-EDGE — mpmath/Sage-300bit S_W_max edge re-derivation (the plan's pre-registered INFO-at-exact-edge route)

1. **What**: higher-precision (mpmath / Sage 300-bit) re-derivation of S_W_max from the frozen W-stage Bogoliubov pair (α_W, β_W) to adjudicate `deviation < S_W_max−1` vs `deviation == S_W_max−1` BELOW the float64 floor — resolving whether the W3-1 knife-edge is exact saturation (the DERIVED phase sits AT the envelope endpoint) or a sub-float64 strict interior point.
2. **Inputs**: `computations/session-102/s102_w7_ladder_phase_resolved.npz` (frozen; W_beta_re/W_beta_im/abs_beta_W full float64, deviation, envelope_upper_dev), `computations/session-103/s103_famp_tolerance_repin.npz` (the re-pin record).
3. **Gate**: sign(deviation − (S_W_max−1)) at ≥300-bit precision ∈ {−1 strict interior → PASS at exact precision; 0 exact saturation → structural-identity finding; +1 breach → re-opens the S79 sufficiency question} — three pre-registered branches, each a distinct registry state.
4. **Effort**: 0.25 gate (~1 h; mpmath scalar evaluation of the SU(1,1) window algebra).

## Constraint-Map Updates

(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason.)

## Files Produced

(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)

## Wave 3 Synthesis (team-lead)

**Verdicts (2/2 closed):**

| Gate | Verdict | Result | audit_sha256 (head) |
|:-----|:--------|:-------|:--------------------|
| W3-1 `S103-FAMP-TOLERANCE-REPIN` | INFO (sign=PASS, magnitude=INFO, regime=VALID) | The S102 deviation 2.9150874e-03 sits INSIDE the exact asymmetric edge S_W_max−1 = 2.9150926e-03 by +5.2e-09 — but the two are IDENTICAL at 5-6 sig figs, the plan's pre-registered INFO branch (knife-edge persists at publication precision). The exact edge vindicated: half-spread (+4.23e-06) and literal 0.0029 (+1.51e-05) both confirmed as wrong comparison edges. F_amp slot 0.3885 and the S79 magnitudes-only anchor undisturbed | `3455a7da` |
| W3-2 `S103-B2-WZ-HOLONOMY-COSET2` | PASS (Track A) | f_WZ([3,5]) = 2.888785e-06 — matches the first doublet f_WZ([4,6]) = 2.8888e-06 to 4 sig figs; frame_resid 2.665e-15, slope 1.9999, non_scalar_frac 1.0, n_broken 4/4. The C² coset span is COMPLETE: U(2) breaks ISOTROPICALLY across the full coset (the two SU(3)-symmetry-related directions carry identical curvature flux) | `49705bbc` |

**Carry-Forward Computations (MATH ONLY — propagate to S104):**

### CF-S104-W3-SWMAX-MPMATH-EDGE
1. **What**: higher-precision (mpmath / Sage 300-bit) re-derivation of S_W_max from the frozen W-stage Bogoliubov pair (α_W, β_W) to adjudicate `deviation < S_W_max−1` vs `deviation == S_W_max−1` BELOW the float64 floor — resolving whether the knife-edge is exact saturation (the DERIVED phase sits AT the envelope endpoint) or a sub-float64 strict interior point.
2. **Inputs**: `computations/session-102/s102_w7_ladder_phase_resolved.npz` (frozen; W_beta_re/W_beta_im/abs_beta_W full float64, deviation, envelope_upper_dev), `computations/session-103/s103_famp_tolerance_repin.npz` (the re-pin record).
3. **Gate**: sign(deviation − (S_W_max−1)) at ≥300-bit precision ∈ {−1 (strict interior → PASS at exact precision), 0 (exact saturation → structural identity finding), +1 (breach → re-opens the S79 sufficiency question)} — three pre-registered branches, each a distinct registry state.
4. **Effort**: 0.25 gate (~1 h; mpmath scalar evaluation of the SU(1,1) window algebra).

**Effected In-Session (NON-MATH):** none surfaced by this wave's agents — no registry/rule/constant consequences beyond the verdict lines and WP sections (the W3-2 result was cited by the W1-5 §VII.BY landing in-dispatch, agent-effected).

**Process observations (closed in-session, do NOT propagate):**

1. **Bound-decomposition correction (W3-1, bit-exact)**: the exact asymmetric upper edge decomposes as `S_W_max − 1 = 2|β_W|² + 2|α_W||β_W|` (residual 7.6e-17 against the frozen `envelope_upper_dev`); the plan/predecessor shorthand `|β_W|² + 2|a||b|` under-counts by one `|β_W|²` (the SU(1,1) window center is 1 + 2|β_W|², not 1 + |β_W|²... as carried in the S102 prose). The THRESHOLD VALUE was unaffected (sourced from the frozen npz field, not reconstructed from the shorthand) — the correction is to the decomposition narrative, recorded in the W3-1 verdict value and npz.
2. `canonical_constants.py` mid-session append-only SHA drift handled per §(ii.B) (disclosed in the W3-1 verdict; none of the appended constants consumed).
