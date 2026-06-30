# Investigation 7 Wave 2 — little-red-dots high-z observational computes (Results Working Paper)

**Investigation**: 7 | **Wave**: 2 | **Plan**: investigation-7-plan-w2.md | **Theme**: the little-red-dots survey's seeds→observables pivot — the GGE-interference two-point clustering test (B3), the substrate accretion-photosphere envelope temperature from the τ_fold van Hove fixed point (B2/B4/B5), and the one mechanical precision band carrying the JWST virial-mass dispute through `n_PBH ∝ 1/L_pix³` into the published 7.2761e-23 m⁻³ anchor (Class-8.3).

**Seed**: `sessions/investigation/investigation-7/investigation-7-seed.md` §"4-field specs (W2 — little-red-dots)" + §"Candidate gate table → Wave 2"
**Plan file**: `sessions/investigation/investigation-7/investigation-7-plan-w2.md`
**Verdict ledger** (investigation-track, MANDATORY): `computations/investigation-7/inv7_gate_verdicts.txt` — emitted via `emit_verdict(session=7, track="investigation", ...)`. The `s7_`-prefix and `session-7` directory are FORBIDDEN (track-local boundary, `gate-verdicts.md §"Investigation-Track Canonical Path"`).

## Gate Sections

### §W2-1. INV7-W2-1 (little-red-dots-jwst-analyst)

**Status**: COMPLETED
**Gate ID**: `INV7-W2-1`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (GGE-interference two-point clustering vs ΛCDM Gaussian-random-field)
**Agent**: `little-red-dots-jwst-analyst` (field-generation sub-step reuses the W1-5 cosmic-web GRF+second-sound generator as a library; co-machinery)
**Hypothesis**: the two-point ξ(r) of the post-transit GGE-relic overdensity field carries an oscillatory (acoustic-interference) feature at the GGE coherence scale that a ΛCDM Gaussian-random-field of the same two-point amplitude lacks, testable against the measured LRD clustering excess at z~5 (Paper 21 Tanaka).
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source).

**Verdict**: **INFO** (composite). 3-tuple: `sign_verdict=PASS` (the predicted oscillatory PRESENCE is real), `magnitude_verdict=INFO` (residual clears the 5% floor at r_GGE but not at the measured LRD scale), `regime_verdict=VALID` (FFT linearity holds to machine-eps, r_GGE resolved on-grid). Composite collapse per `gate-verdicts.md` (`magnitude_verdict==INFO ⇒ composite INFO`). `audit_sha256=16b32225fe2b50f70e70684216a02fdc2335e70d5d49832dcd0a7090dc279084`.

**Substrate framing**: PHONONIC. The substrate IS the post-transit GGE field (59.8 Parker-produced quasiparticle pairs, P_exc=1.000, S_ent=0 product state, S38/S39 PROVEN). Flow: D_K eigenvalues reorganize at the fold (τ_fold=0.190, Mach 13.75) → the second-sound collective mode (S44 W6-2, Q=75,989) sets the coherence wavenumber k_GGE → the post-transit interference pattern of GGE acoustic excitations IS the overdensity field → its two-point ξ(r) carries the acoustic-interference phase. The discriminator Δξ(r) = ξ_framework − ξ_GRF IS the substrate-IS signature (the interference phase the GRF lacks); the ΛCDM GRF is the NULL the substrate is tested AGAINST, not the explanatory baseline. The arrow runs substrate → emergent overdensity → measured LRD clustering.

**MCP Pre-Compute Audit**:
- `search_knowledge("GGE relic second-sound coherence scale n_pairs 59.8 P_exc")` → n_pairs=59.8 saturated pairs (S38), P_exc=1.000 (S57), S_ent=0 product state; GGE relic is the substrate field generator. NOT a closure of this gate.
- `search_knowledge("CLUST-43 LRD clustering Tanaka pair-count z~5")` → CLUST-43 = `s43_lrd_clustering.py`; gate **T3-BATCH-S43-LRD-CLUSTERING: INFO** (S81, `value=MIGRATED`, scheme=batch-canonical-hygiene). This is the S43 number-density/pair-count clustering — the DISTINCT B-observable. **Cross-referenced, verdict NOT consumed** (this gate is the GGE-INTERFERENCE phase/topology signature, B3).
- `search_knowledge("f_NL 1.505 ... Row #69 ... Q 75989")` + `get_constant("max_f_NL_FW")` → `max_f_NL_FW = 1.505` (S95, gate F-NL-ROW, `s95_w6_6_f_nl_row.py`); second-sound Q=75,989 PROVEN (S44 W6-2, obs-horizon S68). The f_NL=1.505 local-NG envelope is canonical. NOT a closure of this gate.
- `get_constant("k1_first_sound_ring_invMpc")` / `("r1_first_sound_ring_Mpc")` → k1 = 0.0193150486 Mpc⁻¹, r1 = r_GGE = 325.3 Mpc (canonical; these set the second-sound feature wavenumber/scale).
- LRD clustering TARGET corpus (FETCHED, cited — TARGET only, never a pin source): **Paper 21 Tanaka** (arXiv:2412.14246) factor ~300 ACF excess at θ~0.1–0.3″ ≈ 1–2 kpc PHYSICAL (one-halo, three dual-LRD systems at z~5–6); **Paper 65 Pacucci** (arXiv:2506.04004) comoving projected w_p(r_p=1 Mpc) ~ 0.015 ± 0.010 (LRDs cluster weakly, like field galaxies; ~50× below quasars); **Paper 50 Mérida** (arXiv:2510.06408) LRD environment d_nn 0.1 Mpc (cluster) → >2 Mpc (isolated), comoving. The measured LRD clustering window is r_p ~ 1–10 Mpc comoving — entirely below r_GGE.
- **PRE-CLOSED?** No. No closure covers the GGE-interference ξ(r) phase/topology observable at the LRD scale. The gate is open and computed here.

**Output Artifacts** (on-disk verified; content-presence checks):
- script `computations/investigation-7/inv7_w2_1_gge_clustering_xi.py` — present; `grep -E 'from canonical_constants import|print_verdict_payload'` → both match (`from canonical_constants import *`; `def print_verdict_payload(...)`).
- data `computations/investigation-7/inv7_w2_1_gge_clustering_xi.npz` — present (k/r grids, P(k) triple, ξ(r) triple, Δξ substrate+canonical, all scalars).
- plot `computations/investigation-7/inv7_w2_1_gge_clustering_xi.png` — present (3-panel: P(k) GRF+feature; ξ(r) framework-vs-GRF; Δξ(r) substrate-vs-canonical contrast with GGE + measured-LRD windows shaded).
- verdict line in `computations/investigation-7/inv7_gate_verdicts.txt` matching `^INV7-W2-1:.* audit_sha256=[a-f0-9]{64}` — present, WITH dual-SHA companion row AND schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`).

**Results** (NUMBERS first):

*Upstream consumption (W1-1 LANDED — substrate-genuine feature, NOT canonical fallback)*: `feature_A_FS = 0.00388533` (the substrate-genuine second-sound amplitude; W1-1 verdict was **FAIL** — this amplitude is **52.51× WEAKER** than the canonical 0.204, which is the recombination first-sound stand-in, NOT the substrate second sound). `k_GGE = 0.0193150486 Mpc⁻¹`; `r_GGE = 2π/k_GGE = 325.30 Mpc` (cross-check 325.30, exact). f_NL = 1.505 enters as a bounded local-NG envelope (`|f_NL|/(1+|f_NL|) = 0.601`) on the feature amplitude, not a new k-mode.

*The discriminator Δξ(r) and the substitution chain (the zero-crossing PRESENCE claim)*:
- **Step 4** (`Δξ(r) = ξ_framework − ξ_GRF = FT[P_2sound]`): verified numerically — `|Δξ − FT[P_2sound]| = 7.54e-22` ≈ machine-eps. The transform linearity decomposition holds exactly.
- **Step 5** (`P_2sound ≠ 0 ⇒ Δξ oscillates, ≥1 zero-crossing in [r_GGE/2, 2·r_GGE]`): verified — **2 zero-crossings** of substrate Δξ in the GGE window [162.6, 650.6] Mpc; the ΛCDM GRF has **0** by construction (`Δξ_GRF ≡ 0`). **Direction matches the prediction ⇒ sign_verdict = PASS.** The substrate ξ(r) carries an oscillatory feature (a zero-crossing) the GRF lacks — the substrate's vaguest slogan ("structure = GGE interference") becomes a concrete, machine-precision signature.

*Magnitude vs the 5% floor (delta_osc_floor = 0.05), substrate-genuine PRIMARY*:
- At r_GGE (GGE window): peak `|Δξ|/ξ_GRF = 0.3334 ≥ 0.05` — the feature **clears the floor at its own coherence scale**.
- At the measured LRD scale (Pacucci comoving [1,10] Mpc): peak `|Δξ|/ξ_GRF = 8.63e-05 << 0.05`, with **0 zero-crossings** — GRF-indistinguishable at the observed comparison scale.

*Both-ways contrast (52.5× weakening is explicit)*: substrate peak/ξ_GRF(GGE) = 0.3334 vs canonical-0.204 peak/ξ_GRF(GGE) = 17.5067 — ratio 52.5×, exactly the W1-1 `ratio_canon_over_sub`. At the LRD scale: substrate = 8.63e-05 vs canonical = 4.53e-03 — **even the canonical 0.204 feature stays << 5% at the LRD scale**, so the scale mismatch (not the weakening alone) is the dominant INFO driver; the two compound.

*Scale-separation + measurement-uncertainty diagnostics (the two INFO triggers)*:
1. **Scale mismatch**: r_GGE = 325.30 Mpc sits **2.51 decades ABOVE** the measured LRD comoving window [1,10] Mpc (`r_gge_inside_lrd_window = False`). The substrate GGE-interference feature is real but lives at a scale the z~5 LRD clustering data does not probe. (Tanaka's ~300× excess is at ~1 kpc PHYSICAL ≈ 9e-3 Mpc comoving — one-halo, ~4.5 decades the OTHER side of the window; not a ξ(r)-ringing probe.)
2. **Measurement uncertainty too wide**: Pacucci w_p(1 Mpc) = 0.015 ± 0.010 → **67% fractional uncertainty >> 5% floor**. Even were a 5% feature present at r_p ~ 1 Mpc, the current LRD clustering data could not resolve it.

*Verdict logic (pre-registered, plan §W2-1)*: `pass_at_lrd_scale = False` (residual << floor AND 0 zero-crossings AND r_GGE outside window); `feature_present_at_gge = True` (clears floor + oscillates at r_GGE). Both INFO_meaning conditions fire → **composite INFO**. The 4-tuple: `(value=peak_rel_resid_LRD_substrate=8.63e-05 / zc_GGE=2 / r_GGE=325.3 Mpc OUTSIDE LRD window, scheme=FW, convention=RATIO, L_max=N/A)`.

**Interpretation (solution-space, third)**: This INFO maps a specific corridor of the B3 observable. The GGE-interference picture is NOT ΛCDM-GRF-degenerate in principle — Δξ(r) carries a machine-precision oscillatory signature (2 zero-crossings, peak/ξ_GRF=0.33) the GRF structurally lacks, so the seed-C3 "framework = ΛCDM at z~7" dead-end is NOT a structural identity. But the signature is **un-reachable by the current z~5 LRD two-point data** for two independent reasons: it lives at r_GGE = 325 Mpc (2.51 decades above the measured comoving window), and the measured amplitude carries 67% fractional uncertainty. The 52.5× substrate weakening (W1-1 FAIL propagated) deepens the gap at the LRD scale (8.63e-05) but is NOT the binding constraint — even the canonical 0.204 feature stays sub-floor there; the scale mismatch is decisive. **What this does NOT close**: the W1-5 persistent-homology web-topology test at the 325 Mpc ring is the COMPLEMENTARY half of convergence #3 — it probes the BEYOND-two-point topology AT r_GGE, exactly where this two-point feature lives. A two-point INFO here does not falsify W1-5; the combined reading (W2-1 two-point at z~5 LRD scale + W1-5 topology at 325 Mpc) is a `/rclab-investigate --investigation 7` convergence-#3 synthesis item. **Forward**: the substrate feature would become testable by (a) a large-scale (r_p → 100s Mpc) high-z clustering survey reaching r_GGE, or (b) a clustering measurement at the LRD scale with σ tightened below 5%. Any clustering-amplitude promotion to a falsifier row is session-track + mack (track-local boundary). CLUST-43 (T3-BATCH-S43-LRD-CLUSTERING INFO) is the distinct number-density/pair-count B-observable, cross-referenced, verdict NOT consumed.

---

### §W2-2. INV7-W2-2 (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV7-W2-2`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (van Hove fixed-point sets a characteristic photosphere temperature)
**Agent**: `landau-condensed-matter-theorist` (fixed-point / order-parameter + BCS-gap/DOS machinery; the a₄/a₂ ratio is the spectral input)
**Hypothesis**: a characteristic substrate accretion-photosphere temperature T_substrate, set by the τ_fold=0.190 van Hove fixed-point structure (an a₄/a₂-type spectral-moment ratio at the local Jensen deformation), matches the observed ~5000 K LRD Balmer-break to within a pre-registered band AND is insensitive to the accretion control-parameter over a τ-window.
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w2.md` §W2-2 (machinery pin, thresholds, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

All four artifacts verified on disk by content (regex match, not line count):

- **script** `computations/investigation-7/inv7_w2_2_substrate_photosphere_temperature.py` — present; `grep -E 'from canonical_constants import'` → `from canonical_constants import *` + explicit import block; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call site. PASS.
- **data** `computations/investigation-7/inv7_w2_2_substrate_photosphere_temperature.npz` — present (non-empty; 23 arrays incl. `T_substrate_K`, `R_moment`, `tau_grid`, `T_tau`, `frac_var_window`, `insens_metric`, 3-tuple verdict fields). PASS.
- **plot** `computations/investigation-7/inv7_w2_2_substrate_photosphere_temperature.png` — present (2-panel: T_substrate(τ) over window + fractional-deviation insensitivity vs floor). PASS.
- **verdict line** `computations/investigation-7/inv7_gate_verdicts.txt` — `^INV7-W2-2:.* audit_sha256=[a-f0-9]{64}` matches (audit_sha256=`14de96b08b26b13d1186bd665d4a5b59a398b04d92873a35d9ebec4a1576d344`); dual-SHA companion row present; schema-v2 3-tuple companion row present (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`); `regulator_pin=a_n^{zeta}` extra row present; substrate-first TARGET-only extra row present. PASS.
- **WP §W2-2** — this section: `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. PASS.

**MCP Pre-Compute Audit**:

Queries executed before writing the script (all substrate-pin sources confirmed canonical; NOT pre-closed — this is a NEW investigation-track observable):

- `get_constant('a_2_FW_zeta')` → **2776.165389** (S88; zeta-regulated 2nd Seeley-DeWitt; `canonical_constants.py:611`). PIN SOURCE.
- `get_constant('a_4_FW_zeta')` → **1350.7216** (S75; zeta-regulated 4th Seeley-DeWitt; `canonical_constants.py:469`). PIN SOURCE.
- `get_constant('tau_fold')` → **0.19** (S12/S42, CONST-FREEZE-42; `canonical_constants.py:288`). PIN SOURCE.
- `get_constant('E_B2')` → no exact match; resolved to **`E_B2_mean = 0.845269087679269`** (S38; `canonical_constants.py:731`). van-Hove band-edge reference (4 modes).
- `get_constant('M_KK')` → **7.428660036284456e16** GeV (S42, gravity-route alias `M_KK_gravity`; `canonical_constants.py:344-346`). Natural-unit→GeV map.
- `search_knowledge('van Hove non-stationarity tau_fold uniqueness S85 W10')` → **`S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` PASS** (scheme=van-Hove-cusp-non-stationarity); PERMANENT theorem **§VII.M.W10-3** ("τ_fold=0.190 promoted to van-Hove-cusp non-stationarity uniqueness theorem", connes+lizzi). Supplies Claim-B analytic content (fold is a cusp; DOS-set quantities flat-to-first-order over a window).
- `search_knowledge('rho_B2 fold 14.023 ...')` → **`rho_B2(fold) = 14.023` (Van Hove enhanced, S52)**; canonical `rho_B2_per_mode = 14.023250234055` (S37, `canonical_constants.py:729`). Confirms the DOS divergence pinning the fold band-edge.
- Auxiliary (PART-B τ-resolved cache): `s52_unified_action.npz` inspected — `tau_grid` (200-pt, [0,0.5], window [0.165,0.215] covered with 20 native pts), `R_K_grid` (τ-resolved curvature/DOS quantity driving the heat-kernel a_n moments), `V_KK_grid` (cross-check axis). NOT re-diagonalized (read + interpolated per plan).

**SUBSTRATE-FIRST SOURCING (load-bearing)**: pin source = τ_fold + a₄^ζ/a₂^ζ (both substrate canonicals). The ~5000 K is the COMPARISON TARGET ONLY — sourced from the LRD corpus (Paper 25 de Graaff Black-Hole-Star RUBIES; Paper 47 warm-outer-layer FeII/Balmer; Paper 41 supermassive-stars) — NEVER the pin source. The M_KK→Kelvin map is the canonical natural-unit conversion (E = k_B T, `k_B = 8.617333262e-5` eV/K); NO free parameter was tuned to land on 5000 K.

**Verdict**: **FAIL** (composite). 3-tuple: `sign_verdict=PASS`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`. Collapse rule (`gate-verdicts.md`): `magnitude_verdict==FAIL AND regime_verdict==VALID ⇒ composite=FAIL`. `value='T_substrate=3.545301e+29K R_moment=0.4865421943 frac_dev_vs5000=7.0906e+25 insens_window_spread=6.8692e-03 claimA=False claimB=True'` scheme=SA convention=RATIO L_max=10. audit_sha256=`14de96b08b26b13d1186bd665d4a5b59a398b04d92873a35d9ebec4a1576d344` content_sha256=`f66b51937091303d298a6aa70e26582b4c1d73c8138153d7e01526149003a999`. regulator_pin=`a_n^{ζ}`.

**Results**:

**NUMBERS FIRST.**

*Classification*: **GEOMETRIC**. The substrate IS the spectral-triple fixed-point structure at the Jensen-deformed τ_fold = 0.190 (the B2 flat optical band, 4 modes, E_B2 = 0.845 M_KK, DOS divergence ρ_B2(fold) = 14.023). The ~5000 K Balmer-break is the laboratory-IN image. Arrow: D_K eigenvalues → a_n^ζ Seeley-DeWitt moments → ratio R_moment → projected through the van-Hove band-edge onto a characteristic photosphere temperature → measured break.

| Quantity | Value | Source |
|:---------|:------|:-------|
| a₂_fold (a₂^ζ) | 2776.165389 | `a_2_FW_zeta`, S88 |
| a₄_fold (a₄^ζ) | 1350.7216 | `a_4_FW_zeta`, S75 |
| R_moment = a₄^ζ/a₂^ζ | **0.48654219426262** | computed (canonical inputs) |
| R_moment (plan Sage-exact 45024/92539) | 0.48654080982072 | plan §W2-2 |
| ‖R_moment − plan-rational‖ | 1.38×10⁻⁶ | a₄^ζ=1350.7216 (4-dp canonical) vs plan-implied 1350.72; **negligible** (gate turns on 10²⁵) |
| E_B2 (van-Hove band edge) | 0.845269 M_KK | `E_B2_mean`, S38 |
| E_substrate = R_moment·E_B2 | 0.411259 M_KK | computed |
| M_KK | 7.428660×10¹⁶ GeV | `M_KK_gravity`, S42 |
| **T_substrate** | **3.545301×10²⁹ K** | **OUTPUT** |
| TARGET (LRD Balmer-break) | ~5000 K | Paper 25/47/41 — **TARGET ONLY** |
| ‖T_substrate − 5000‖/5000 | 7.09×10²⁵ | ≫ band_T = 0.30 |
| T_substrate window spread (R_K-track) | **6.869×10⁻³** | PART B, load-bearing |
| T_substrate window spread (V_KK-track) | 6.869×10⁻³ | PART B cross-check (agrees) |
| max ‖d ln T/dτ‖·window | 8.560×10⁻³ | local-derivative form |
| insens_floor | 0.10 | threshold |

**GATE SECOND.** Composite **FAIL**. `sign_verdict=PASS` (T finite-positive), `magnitude_verdict=FAIL` (off by 25 dex), `regime_verdict=VALID` (insensitive over window). 4-tuple `(value=3.545301e+29, scheme=SA, convention=RATIO, L_max=10)`. regulator_pin `a_n^{ζ}` (a₂_fold=a₂^ζ, a₄_fold=a₄^ζ; ratio = a₄^ζ/a₂^ζ).

- **PASS** would mean: T_substrate ∈ [3500, 6500] K AND insensitive over the τ-window — the seeds→envelope temperature pivot has content. **Not realized.**
- **FAIL** (this verdict): T_substrate = 3.55×10²⁹ K lands **25 orders of magnitude** outside [3500, 6500] K. The "van Hove fold sets the ~5000 K photosphere temperature via direct R_moment·E_B2 natural-unit projection" corridor is **CLOSED**.
- **INFO** would mean: no single characteristic T emerges (degenerate projection). Not the case — a single, sharp, finite-positive T does emerge; it is simply at the substrate (M_KK) scale, not the observed scale.

**Substitution chain — Claim A (magnitude + direction)** (per plan §(7); substituted numbers):
1. a₂_fold = a₂^ζ = 2776.165389 — zeta-regulated 2nd Seeley-DeWitt [`a_2_FW_zeta`, S88]
2. a₄_fold = a₄^ζ = 1350.7216 — zeta-regulated 4th Seeley-DeWitt [`a_4_FW_zeta`, S75]
3. R_moment = a₄_fold/a₂_fold = 1350.7216 / 2776.165389 [definition; dimensionless]
4. = **0.48654219426262** [canonical form; matches plan-rational 0.48654080982072 to 1.4×10⁻⁶]
5. E_substrate = R_moment · E_B2 = 0.48654219 · 0.845269 = 0.411259 M_KK; carry to physical energy E = E_substrate · M_KK = 0.411259 · 7.42866×10¹⁶ = 3.055×10¹⁶ GeV; carry to Kelvin via the canonical natural-unit map E = k_B T (k_B = 8.617333262×10⁻⁵ eV/K = 8.617333262×10⁻¹⁴ GeV/K): **T_substrate = 3.055×10¹⁶ / 8.617×10⁻¹⁴ = 3.545×10²⁹ K**.
- Direction: a finite positive R_moment·E_B2 yields a finite positive T_substrate (sign_verdict = PASS ✓). The magnitude is the OUTPUT, not a pre-asserted direction: it lands at the substrate (M_KK) scale (~8.6×10²⁹ K), so any O(1) moment ratio × E_B2 surfaces at ~10²⁹ K. **The magnitude FAILS the [3500,6500] K band by 25 dex.**

**Substitution chain — Claim B (the LOAD-BEARING insensitivity)** (per plan §(7); substituted numbers):
1. τ_fold = 0.190 is a NON-STATIONARY cusp of S(τ) [S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM PASS, PERMANENT §VII.M.W10-3].
2. The B2 flat optical band DOS DIVERGES at the fold: ρ_B2(fold) = 14.023 (Van Hove-enhanced) [S52].
3. T_substrate is pinned by the DOS-enhanced band-edge structure (R_moment·E_B2). Its τ-dependence is inherited from the canonical S52 cache: the a_n moments are heat-kernel curvature integrals (a₂ ∼ ∫R, a₄ ∼ ∫R²), so R_moment(τ) tracks the τ-resolved curvature quantity R_K(τ) read (interpolated) from `s52_unified_action.npz`. R_K(fold) = 4.036292.
4. Substitute the cusp property numerically: T_substrate(τ) = [R_moment · R_K(τ)/R_K(fold)] · E_B2 · M_KK → K over the 101-pt grid τ ∈ [0.165, 0.215]. The full-window fractional spread = **6.869×10⁻³ (0.69%) ≤ insens_floor = 0.10** ✓. The independent V_KK-track cross-check gives the same 6.869×10⁻³, confirming the insensitivity is robust to the choice of τ-resolved DOS-coupled quantity.
- Direction: the fold is a van Hove cusp ⇒ ‖d T_substrate/dτ‖ is SMALL over the window ⇒ control-parameter-insensitive (regime_verdict = VALID ✓). This is the substrate analog of the accretion-control-parameter insensitivity the dust-free/non-variable LRD envelope demands — and it **numerically confirms** the S85-W10 PERMANENT non-stationarity theorem on this observable.

**SOLUTION-SPACE INTERPRETATION (what FAIL constrains).** The result splits cleanly: **Claim B holds, Claim A fails.** The substrate's van-Hove fold IS a robust fixed point — a DOS-pinned characteristic scale flat-to-first-order over the τ-window (0.69% spread), exactly as the cusp theorem requires, and exactly the *qualitative* signature the dust-free/non-variable LRD envelope demands. But the *magnitude* of the characteristic energy is set at the substrate scale M_KK (~8.6×10²⁹ K), 25 dex above the observed ~5000 K. The direct R_moment·E_B2 natural-unit projection therefore CANNOT be the map from the fold to the Balmer-break temperature: any O(1) spectral-moment ratio lands at the M_KK scale by construction. Closing this corridor is informative — it tells the Row #88 envelope program that the temperature observable needs an *emergent-scale* bridge (a many-decade transport from M_KK to the optical/eV scale, of the kind deg(T_{BZ→pivot}) supplies for the running/tilt observables, ~54 decades) rather than a bare natural-unit conversion. The substrate-first discipline is what produced this clean negative: had the Kelvin map carried a free parameter, it would have been tuned to 5000 K and the 25-dex structural gap (the real finding) would have been hidden. **The insensitivity (Claim B) is the durable structural output; the temperature-magnitude corridor (Claim A) is closed on the direct-projection axis, not the whole envelope program** — the INFO_meaning route (a different fixed-point observable, not temperature) remains open for the Row #88 cell.

**Output artifacts**: `computations/investigation-7/inv7_w2_2_substrate_photosphere_temperature.py` / `.npz` / `.png`. Verdict line + dual-SHA + 3-tuple + regulator_pin rows in `computations/investigation-7/inv7_gate_verdicts.txt`.

*Cross-wave note*: per plan, INV7-W2-2 (OBSERVATIONAL envelope route) and Wave-3 INV7-W3-1 (CONSTRUCTIVE LQG modular-horizon entropy) are the two complementary routes into falsifier Row #88 (the empty compact-object cell). This FAIL closes the *temperature-projection* route into that cell; the cell is not thereby filled, and the constructive route is unaffected. Any T_substrate promotion to a falsifier row would be session-track + `mack` (not an investigation edit).

---

### §W2-3. INV7-W2-3 (little-red-dots-jwst-analyst)

**Status**: COMPLETED (orchestrator-inline solo, 2026-06-15)
**Gate ID**: `INV7-W2-3`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (n_PBH band propagation; INFO-by-construction precision-hygiene)
**Agent**: `little-red-dots-jwst-analyst` (gate_type: solo — same closure as compute, executed inline by the orchestrator agent, no subagent spawn; the band endpoints are observational virial-mass-dispute calls)
**Hypothesis**: propagating L_pix_LRD as the band r_s([10⁵,10⁸] M_⊙) — the JWST virial-mass dispute — through n_PBH ∝ 1/L_pix³ (the 9-dex-in-volume sensitivity) yields a 9-decade uncertainty band on the published 7.2761e-23 m⁻³ anchor, exposing that its 3-significant-figure precision is structurally tighter than its dominant systematic (Class-8.3).
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w2.md` §W2-3 (band-report + Class-8.3 flag pre-registration; substitution chain source).

**Output Artifacts** (closure-verification checklist — all verified on disk by content-regex):
- script `computations/investigation-7/inv7_w2_3_n_pbh_lpix_error_budget.py` (13694 B) — `grep -cE 'from canonical_constants import|print_verdict_payload'` → 4 ✓
- data `computations/investigation-7/inv7_w2_3_n_pbh_lpix_error_budget.npz` (4076 B) ✓
- plot `computations/investigation-7/inv7_w2_3_n_pbh_lpix_error_budget.png` (54338 B) ✓
- verdict line in `computations/investigation-7/inv7_gate_verdicts.txt` matching `^INV7-W2-3: INFO .* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + schema-v2 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`) ✓ + 2 extra `#` rows (INFO-by-construction note + L_max=14-held note)

**MCP Pre-Compute Audit** (queries before writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `get_constant("n_PBH_FW_central")` → **7.2761e-23 m⁻³** (canonical_constants.py:**628**, gate S93-W4-5; **published at 5 sig figs**, NOT the plan's rounded "3 sf / 7.28e-23" — substrate-first sourcing uses the canonical value, and the Class-8.3 point only sharpens: 5 sf vs 9-dex systematic). Provenance: VII.AX.OP-PROJ Level-3 anchor T1.13 PASS, STAGE-3-PERMANENT-eligible, not superseded.
- `get_constant("L_PIX_LRD_M")` → NOT a registered constant — irrelevant here: the band is a RATIO sweep `n_PBH(M)/n_PBH_anchor = (M_anchor/M)³`, so the `n_edge·prob_form/k³` prefactor (and L_pix's absolute value) cancel.
- `search_knowledge("n_PBH VII.AX.OP-PROJ truncation anchor")` → formula `n_PBH(L)=central14·N_eigs(L)/N_eigs(14)`, `central14=72761/10²⁷`. CONFIRMS the L_max-truncation axis is SEPARATE — held FIXED at L=14 here; it is the **W4-2 workshop** subject (physical-identity vs convention-tautology). W2-3 sweeps the ORTHOGONAL M_BH virial axis.
- `trace_entity("n_PBH")` → S94-N-PBH-TRUNCATION-ANCHOR: the §VII.AX.OP-PROJ Level-3 m⁻³ row is **TIER-2-DIMENSIONFUL / REGISTRY-PASS-INELIGIBLE-HELD** (dN/dL>0 ∀L≥1, lim_N_eigs=+∞); `n_PBH_FW_saturated_tail=1.7581364216e-23` (distinct Tier-2 observable). This band quantifies the held status from the systematic side. **NOT PRE-CLOSED** — no prior gate computes the M_BH-virial-dispute band.

**Verdict**: **INFO** (INFO-by-construction — a precision-hygiene band; PASS/FAIL are structurally N/A, the only non-INFO outcome would be a script error). Composite INFO ← 3-tuple `sign_verdict=PASS` (n_PBH ∝ M_BH⁻³ direction confirmed: M_BH down ⇒ n_PBH up, monotone-decreasing over the four decade-anchors), `magnitude_verdict=INFO` (band report, no threshold), `regime_verdict=VALID` (exact Sage-QQ rational arithmetic). scheme=FW convention=RATIO L_max=14. audit_sha256=`850e844a73653d73cab46c40f9729aca4e4d3b24c8fc934067a04f9845efa858` content_sha256=`15a555dc68cecb545f54a1ad1f63e551449fee831436a22c9ded51297815430e`.

**Results**:

**NUMBERS FIRST.** Holding L_max=14 FIXED (the truncation axis is the separate W4-2 workshop), sweep M_BH across the JWST virial-mass dispute via the pixelation-lock `L_pix_LRD ∝ M_BH` and propagate through `n_PBH ∝ 1/L_pix³`. Normalizing to the canonical anchor cancels the `n_edge·prob_form/k³` prefactor: `n_PBH(M_BH) = n_PBH_FW_central · (M_anchor/M_BH)³`.

| M_BH (M_⊙) | regime | n_PBH (m⁻³) | factor vs anchor |
|:-----------|:-------|:------------|:-----------------|
| 1e5 | LOW (Rusakov e-scatter) | 7.2761e-17 | ×1e6 |
| 1e6 | — | 7.2761e-20 | ×1e3 |
| 1e7 | **anchor** | **7.2761e-23** | ×1 |
| 1e8 | HIGH (naive virial) | 7.2761e-26 | ×1e-3 |

- **Band** = [n_PBH(1e8), n_PBH(1e5)] = **[7.2761e-26, 7.2761e-17] m⁻³**, span **exactly 9.000 decades** (Sage-QQ exact at all four decade-anchors via `fractions.Fraction`: `72761/10²⁷` central → `72761/10²¹` and `72761/10³⁰` edges).
- **Class-8.3 flag FIRES**: the anchor is published at **5 sig figs** (canonical_constants.py:628) while its dominant systematic (the virial-mass dispute) spans **9 decades** → `precision_tighter_than_systematic = True`.
- **Substitution chain (signed direction)**: `n_PBH = n_edge·prob_form/L_pix_LRD³`; `L_pix_LRD ∝ M_BH` (pixelation-lock at r_s = 2GM_BH/c²); ⇒ `n_PBH ∝ M_BH⁻³`; M_BH DOWN ⇒ L_pix DOWN ⇒ n_PBH UP. The 3-decade M_BH dispute **cubes** to a 9-decade n_PBH band. `monotone_decreasing=True` confirms the sign (sign_verdict=PASS).
- **PASS/FAIL = N/A** (precision-hygiene gate, no threshold). **INFO is the verdict**: the held TIER-2-DIMENSIONFUL anchor's 9-decade band makes LOUD that citing "n_PBH = 7.28e-23 m⁻³" as a clean LRD prediction is unwarranted — the 5-sig-fig point-anchor's precision is structurally tighter than its dominant systematic by ~4 decades.
- **Soft cross-link to W4-2** (NOT a shared gate): W2-3 reports the band on the CURRENT §VII.AX.OP-PROJ formula at fixed L=14; W4-2 adjudicates whether the formula's g-cancellation is physical or tautological. If W4-2 rules tautology, the Level-3 anchor re-casts and this band re-targets — but the two run independently.

**Output artifacts**: `inv7_w2_3_n_pbh_lpix_error_budget.py` / `.npz` / `.png`. dual-SHA: audit `850e844a73653d73…`, content `15a555dc68cecb54…`.

---

## Wave 2 Synthesis (team-lead)

**Through-line**: the LRD seeds→envelope pivot has REAL substrate content, but every observable the substrate reaches at z~5 sits just outside what current JWST/PBH data can resolve — a sector that is structurally non-trivial yet observationally not-yet-sharp.

### (b) Structural changes

- **W2-1 INFO — GGE-interference is a genuine ΛCDM-distinct signature, but at the wrong scale for current data.** ξ_framework(r) carries an oscillatory residual Δξ(r)=FT[P_2sound] with 2 zero-crossings the ΛCDM-GRF structurally lacks (transform linearity exact to 7.5e-22; the feature clears the 5% floor at r_GGE). BUT r_GGE=325.3 Mpc lies **2.51 decades above** the measured LRD clustering window [1,10] Mpc (Pacucci w_p=0.015±0.010, 67% fractional uncertainty). So the seed-C3 "framework=ΛCDM at z~7" dead-end is NOT a structural identity (the signature exists at machine precision) — it is unreachable by current z~5 two-point data. The W1-1 52× ring-weakening propagated (LRD-scale residual 8.6e-5 vs canonical 4.5e-3) but the BINDING driver is the scale mismatch, not the weakening (even the canonical-0.204 feature stays sub-floor at the LRD scale).
- **W2-2 FAIL — the van Hove fold IS a robust fixed point, but at the wrong energy scale.** Claim B (the load-bearing insensitivity) PASSES: T_substrate varies only 0.69% over the τ-window (≪ the 0.10 floor), numerically confirming the S85-W10 van-Hove-cusp non-stationarity theorem on this observable. But Claim A FAILS by **25 OOM**: T_substrate = R_moment·E_B2 = 3.55e29 K (M_KK-scale), not the ~5000 K eV-scale Balmer-break target. Corridor CLOSED: "the fold sets the ~5000 K photosphere via a bare natural-unit projection." The envelope program needs an EMERGENT-SCALE transport bridge (a many-decade M_KK→optical `deg(T_{BZ→pivot})`-type map), not a bare E=k_B T conversion.

### (a) Numerical revisions

- **W2-3 INFO** (INFO-by-construction): n_PBH band [7.2761e-26, 7.2761e-17] m⁻³, span exactly 9.000 dex; Class-8.3 flag FIRES (5-sig-fig anchor vs 9-decade virial-mass systematic). The published "7.28e-23" is precision-tighter-than-systematic by ~4 decades. (The substantive re-cast is the W4-2 workshop CF.)

### Cross-wave complementarities (for `/rclab-investigate --investigation 7`)

- **W2-1 ↔ W1-5 (convergence #3)**: GGE-interference vs ΛCDM at two scales — web topology (Z=620σ at 325 Mpc) + two-point clustering (z~5). BOTH are structurally real, BOTH below current observational reach. The combined reading: the framework's "structure = GGE interference" slogan IS a number (machine-precision signatures), but neither scale's data can yet resolve it.
- **W2-2 ↔ W3-1 (convergence #2, empty Row #88)**: the compact-object sector is attacked observationally (W2-2 envelope, FAIL on magnitude) AND constructively (W3-1 modular entropy, FAIL on coefficient) — **both routes FAILED this investigation**; the cell stays empty. inv-6 kaluza-klein is the third vantage.
- **W2-3 ↔ W4-2 (soft cross-link)**: W2-3 reports the band on the current formula at fixed L=14; W4-2 adjudicated the formula's g-cancellation as a three-layer object with the magnitude on the unprotected floor.

## Carry-Forward Computations

### CF-INV7-W2-2-ENVELOPE-SCALE-BRIDGE — emergent-scale transport for the substrate photosphere temperature

1. **What**: Test whether the substrate fixed-point temperature reaches the observed ~5000 K Balmer-break through an EMERGENT-SCALE transport map (not the bare natural-unit E=k_B T that lands 25 OOM high). Compute T_observed = T_substrate · F(deg(T_{BZ→pivot})) where F is the substrate→emergent energy-transport factor (the same `deg(T_{BZ→pivot})`-type map that scale-separates the n_s/α_s running observables, 54 decades); test whether a substrate-natural non-scalar transport degree lands T_observed in [3500,6500] K while retaining the W2-2 fold-robustness (insensitivity PASS).
2. **Inputs**: W2-2 `inv7_w2_2_substrate_photosphere_temperature.npz` (T_substrate=3.55e29 K, R_moment=0.4865, fold-insensitivity confirmed); the `deg(T_{BZ→pivot})` transport machinery (`cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"` + `phononic-framing.md §"Scale-and-channel-tagging"`); the ~5000 K Balmer-break TARGET (Paper 25/47/41, TARGET-only); M_KK.
3. **Gate**: `T-SUBSTRATE-EMERGENT-TRANSPORT`. PASS iff a substrate-natural transport degree lands T_observed in [3500,6500] K AND the transport is NON-SCALAR (a scalar corrector is vacuous — Class-8 PRU); INFO iff the transport exists but is fitted/scalar (the envelope route needs a different observable than temperature); FAIL iff no substrate-natural transport reaches the eV scale (the temperature axis of the envelope program is structurally empty).
4. **Effort**: ~1–2 waves. Depends on: the `deg(T_{BZ→pivot})` transport degree being independently derived (cross-link to the n_s/α_s scale-separation machinery).

**Note (session-track, NOT a CF — route to `/rclab-investigate --investigation 7`)**: HY1 (`proven_1450` "JWST LRD BH-seed-mass spectrum predictions" → down-tag to OPEN, reconciling Row #88); HY2 (`lrd-observational-constraints.md` post-S85 refresh); HY3 (§VII.AX Tier-2-dimensionful HELD-status loudness). All three are session-track curated-register edits (knowledge-MCP / AMRI-registry / mack-surface), session-promotion only — an investigation MUST NOT mutate them. W2-1/W2-3 close in-investigation (W2-1 INFO = signature real, data-limited; W2-3 INFO-by-construction).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | GGE-interference clustering signature (B3) | "structure = GGE interference" slogan, unquantified | REAL machine-precision signature (2 zero-crossings vs GRF), at r_GGE=325 Mpc OUTSIDE measured LRD window | W2-1 INFO |
| 2026-06-15 | Substrate photosphere temperature (envelope route) | untested | fold ROBUST (insensitivity PASS) but energy M_KK-scale (25 OOM off 5000 K); bare-projection corridor CLOSED | W2-2 FAIL; → CF-INV7-W2-2 emergent-transport |
| 2026-06-15 | Row #88 compact-object sector | empty (S106 CORPUS-EXCEEDS) | STILL empty — both observational (W2-2) + constructive (W3-1) routes FAILed this investigation | W2-2 + W3-1 |
| 2026-06-15 | n_PBH Level-3 anchor precision | published 5 sig figs as if clean | precision-tighter-than-systematic by ~4 decades (Class-8.3 band [7.28e-26, 7.28e-17]) | W2-3 INFO-by-construction |

## Files Produced

| Gate | Script | Data | Plot | Verdict |
|:-----|:-------|:-----|:-----|:--------|
| INV7-W2-1 | `inv7_w2_1_gge_clustering_xi.py` | `.npz` | `.png` (3-panel) | INFO |
| INV7-W2-2 | `inv7_w2_2_substrate_photosphere_temperature.py` | `.npz` | `.png` | FAIL (sign=PASS, mag=FAIL) |
| INV7-W2-3 | `inv7_w2_3_n_pbh_lpix_error_budget.py` (solo) | `.npz` | `.png` | INFO-by-construction |

All scripts under `computations/investigation-7/`; verdicts in `computations/investigation-7/inv7_gate_verdicts.txt`.
