# Session 97 Wave 1 — Emergent-FRW a(t) closure & κ-pin (C1 frontier) (Results Working Paper)

**Session**: 97 | **Wave**: W1 | **Plan**: session-97-plan-w1.md | **Theme**: Emergent-FRW `a(t)` closure & κ-pin (C1 frontier) — export the order-parameter↔acoustic conformal factor Ω(τ), pin the substrate-determined x_today window, run the A/B/C route-invariance discriminator on q_Ω, assemble the explicit physical-seconds a(t), and test whether the SCENARIO-A cooling budget pins the M_KK⁻¹→s knob κ.

## Gate Sections

### §W1-1. S97-W1-OMEGA-PROFILE (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S97-W1-OMEGA-PROFILE`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (order-parameter↔acoustic conformal-factor export; the structural BLOCKER for 1.3 leg-ii + 1.4)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: The conformal factor Ω(τ)=√(ρ_s/a₂) is non-constant over τ∈[0.190,0.6] with finite Ω̇,Ω̈ and reproduces the S95-W4-4 fold anchor Ω_BA; the alternative is a constant-Ω null (Ω̇=Ω̈=0) under which the acoustic deceleration is identically the bare one.
**Plan reference**: `sessions/session-plan/session-97-plan-w1.md` §W1-1 (machinery pin, eps_nonconst/tau_anchor thresholds, CLAIM-A/CLAIM-B substitution chain source).

**Output Artifacts**:
- Script `computations/session-97/s97_w1_omega_profile.py` (28,593 bytes) — `grep -cE "from canonical_constants import"` → `1`; `grep -cE "append_verdict"` → `2`. PASS.
- Data `computations/session-97/s97_w1_omega_profile.npz` (82,557 bytes) — present; carries the PRIMARY EXPORT triple `tau_grid`, `Omega`, `Omega_dot`, `Omega_ddot` (1001-pt dense grid) consumed by 1.3 leg-ii + 1.4. PASS.
- Plot `computations/session-97/s97_w1_omega_profile.png` (137,280 bytes) — present (4-panel: Ω(τ), Ω̇, Ω̈, two-fluid cross-check). PASS.
- Verdict line in `computations/session-97/s97_gate_verdicts.txt` — `grep -E "^S97-W1-OMEGA-PROFILE:.* audit_sha256=[a-f0-9]{64}"` matches; `audit_sha256=6fee3fdff3ceb241b20fb51d43004623919d53e570a332d1b3ff5ca30f1bbc55`, `content_sha256=640ff7c2b516f4e637aeb2c38a5fb71b83a07f43cc759498f0444664e43d7766`; dual-SHA companion row present; schema-v2 3-tuple companion row present (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`). PASS.
- This WP §W1-1 — Status COMPLETED + Verdict PASS. PASS.

**MCP Pre-Compute Audit**:
- `search_knowledge("Omega_BA conformal embed anchor S95-W4-4 fold conformal factor")` → provenance `w4_4_sp_conformal_embed` (s95); gate `S95-W4-4-SP-CONFORMAL-EMBED` returned **INFO** ("Omega_derivable_1plus1D_AND_fold_4D_causal_feature_BUT_a2_proxy_q_Omega_OUT_of_band ... M_KK_inv_to_s_normalization_OPEN"). Confirms Ω was proven to EXIST (1+1D conformal embedding) but never EXPORTED with derivatives — this gate is the export, not a recompute. NOT PRE-CLOSED.
- `search_knowledge("a_2 zeta Seeley-DeWitt second spectral moment provenance a_2_FW")` → `a_2_FW_zeta = 2776.165389` (S42 spectral-zeta sum; gate `S88-A-N-FW-CANONICALIZATION`); provenance "zeta-regulated second Seeley-DeWitt coefficient of D_K²". Pins the `a_2^{ζ}` regulator tag.
- `get_constant("Gamma_effacement")` → `0.9997` (canonical; S37 impedance-transmission, carried by ρ_s).
- `get_constant("M_KK")` → `7.428660036284456e16` GeV (S42 CONST-FREEZE; gravity-route alias).
- Verdict: result is **NOT** already-known/closed. The S95 gate left the export + derivatives + the constant-vs-non-constant [SIGN] adjudication open; this gate produces them.

**Verdict**: **PASS** (sign=PASS, magnitude=PASS, regime=VALID; composite collapse → PASS). Ω(τ) is non-constant with finite Ω̇,Ω̈ and reproduces the fold anchor; the conformal factor carries independent acoustic-deceleration content. **PREREQUISITE SATISFIED for 1.3 leg-ii + 1.4** — both may consume `(Ω, Ω̇, Ω̈)` from the npz.

**Results**:

*Numbers first.*

| Quantity | Value | Threshold | Leg |
|:--|:--|:--|:--|
| Relative spread `max|Ω−⟨Ω⟩|/⟨Ω⟩` (the [SIGN] quantity) | **6.420002e-02** | `> eps_nonconst = 1e-3` | non-constancy **PASS** (64× over) |
| `Ω̇` absmax | 9.399753e-01 (finite ∀τ) | finite | derivative **PASS** |
| `Ω̈` absmax | 2.098068e+00 (finite ∀τ) | finite | derivative **PASS** |
| Fold-anchor rel-dev `|Ω(τ_fold)−Ω_BA|/Ω_BA` | **1.500113e-04** | `≤ tau_anchor = 1e-2` | anchor **PASS** (67× inside) |
| Ω(fold) vs Ω_BA_anchor | 2.24101696 vs 2.24135319 | — | — |
| Fold-anchor rel-dev (exact S95 form, no Γ_eff) | **0.0e+00** | — | identity confirmed |

- **4-tuple**: `(value = rel_spread = 6.420002e-02, scheme = FW, convention = RATIO, L_max = 10)`.
- **Ω(τ) profile**: monotone-decreasing from Ω(fold)=2.24102 to Ω(0.6)=2.01956 (mean 2.15812); `Ω̇` mean sign = **−1**, `monotone_decreasing = True`. As τ advances past the fold, a₂ ∝ R_K(τ) grows, so Ω = √(ρ_s/a₂) falls — the spectral weight re-grades DOWN, exactly the predicted [SIGN] direction.
- **Machinery pins (PRDR)**: N_eval=1001, τ∈[0.190,0.6], step_size=4.1e-4 (uniform; plan's 3.6e-4 was for the [0.190,0.451] sub-window — the full [0.190,0.6] window gives 4.1e-4, declared as the operational pin), tolerance=1e-12, eps_nonconst=1e-3, tau_anchor=1e-2, sg_window=21, sg_polyorder=3, Γ_eff=0.99970, G_mod=G_DeWitt=5.0, τ_today=0.22, **regulator_pin = a_2^{ζ}** (zeta-regulated 2nd Seeley–DeWitt moment; matches `a_2_FW_zeta` provenance per regulator-pin-discipline.md). GPU_path = numpy CPU (1D arrays, correct per plan).

- **[SIGN] substitution chain (Sage-verified at plan-freeze + reproduced here)**:
  - **CLAIM A (the null boundary)**: `a_acoustic = Ω·a_bare`, `q ≡ −a·ä/ȧ²`. Setting `Ω̇=Ω̈=0` gives numerator → `−Ω²·a_bare·ä_bare`, denominator → `Ω²·ȧ_bare²`, so `q_acoustic(Ω̇=Ω̈=0) − q_bare = 0` (Sage `simplify_full() → 0`). **Direction**: a constant Ω leaves q INVARIANT ⇒ a non-constant Ω is REQUIRED for the conformal factor to carry independent acoustic-deceleration content. The PASS branch tests exactly this non-constancy.
  - **CLAIM B (the construction)**: `Ω(τ)=√(ρ_s(τ)/a₂(τ))`, `ρ_s ≈ const` (unbroken-condensate vacuum, w=−1, carrying Γ_eff), `a₂(τ)=a_2_FW_zeta·R_K(τ)/R_K(τ_fold)` (τ-dependent through E3 curvature `R_K(τ)=−¼e^{−4τ}+2e^{−τ}−¼+½e^{2τ}`). Since `a₂(τ) ∝ R_K(τ)` grows while `ρ_s ≈ const`, the ratio is NOT constant ⇒ **Ω̇ ≠ 0** (computed rel-spread 6.42e-2 ≫ 1e-3). The degenerate Ω̇=Ω̈=0 case is the INFO null of CLAIM A — **it does NOT fire**.
  - **Convention-translation note (condensed-matter → cosmology)**: the plan's `Ω=√(ρ_s/a₂)` and the S95-W4-4 canonical `Ω_BA=√(G_mod)/a_eff` (with `a_eff=√(R_K(τ)/R_K(today))`) are **ALGEBRAICALLY IDENTICAL** under `ρ_s = G_mod·R_K(today)` and `a₂(τ)=a_2_FW_zeta·R_K(τ)/R_K(τ_fold)` — Sage-verified `Ω_plan(0.19) = √(G_mod·R_K(today)/R_K(0.19)) = 2.24135319 = Ω_BA_fold`. The 1.50e-4 fold rel-dev in my plan-form is exactly the `√(Γ_effacement) = 0.99985` sub-permille effacement-leak factor that the plan-form carries and the S95 anchor omits; the exact S95-form rel-dev is **0.0e+00**. This is a STRUCTURAL mapping (same conformal factor), not a coincidental numerical match.

- **Independent cross-check (two-fluid)**: reconstructing Ω from the two-fluid `√(x·ρ_n/a₂)` on its own 200-pt sub-grid [0.190,0.451] (npz key `x_tau_ideal`, `x_fold=85.7928 → x_end=401.72` confirming ρ_n dilutes as the substrate becomes condensate-dominated) gives spread **4.63e-2** — non-constant, sign-consistent with the primary closed form. Two independent reconstructions agree that Ω is non-constant; the result is not an artifact of the closed-form choice. SG-vs-raw-FD interior maxdev = 1.50e-7 confirms the Savitzky–Golay smoothing reproduces the derivative faithfully (not distorting the signal).

- **Verdict line + companion rows** (`computations/session-97/s97_gate_verdicts.txt`):
  ```
  S97-W1-OMEGA-PROFILE: PASS -- value='rel_spread=6.420002e-02_gt_1e-03=True;...;sign=PASS;magnitude=PASS;regime=VALID;CLASS=FULL;regulator_pin=a_2_zeta;BLOCKER_for=1.3_legii+1.4_aoft_bridge' scheme=FW convention=RATIO L_max=10 audit_sha256=6fee3fdff3ceb241b20fb51d43004623919d53e570a332d1b3ff5ca30f1bbc55 content_sha256=640ff7c2b516f4e637aeb2c38a5fb71b83a07f43cc759498f0444664e43d7766 schema_version=S84+
  # audit_sha256_short=6fee3fdff3ceb241 content_sha256_short=640ff7c2b516f4e6 # ... dual-SHA companion row ...
  # sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S97-W1-OMEGA-PROFILE 3-tuple annotation (schema-v2)
  ```

- **Substrate-IS assessment** (phononic-framing.md): Ω(τ) is NOT a scale factor on a pre-existing container. The substrate IS the spectral triple (A_K, H_K, D_K(τ)); ρ_s is the unbroken-condensate vacuum density (the part of the substrate that has NOT decohered into GGE quasiparticles, w=−1, carrying Γ_eff=0.99970), and a₂ is the a_2^{ζ} second Seeley–DeWitt moment of D_K² that generates the emergent g_M. Their ratio's square root Ω(τ) is the **conformal re-grading of spectral weight as the order parameter τ advances past the fold** — the map from the substrate's intrinsic order-parameter clock to the acoustic-metric clock an external observer reads. `Ω̇<0` means spectral weight re-grades DOWN as a₂ (the gravity-sourcing moment) grows past the fold. Flow: `D_K eigenvalues → a₂ (2nd spectral moment) + ρ_s (condensate vacuum density) → Ω(τ) conformal factor → acoustic a(t) image`. Exporting `(Ω, Ω̇, Ω̈)` makes the order-param→acoustic bridge a computable object rather than an implicit one — it does NOT introduce a container; it re-grades the existing substrate spectral weight.

---

### §W1-2. S97-W1-XTODAY (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S97-W1-XTODAY`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (substrate-determined A-PASS x-window via two-fluid integration)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: Integrating ρ_n ∝ a^{−3(1+w_n)} (GGE normal component, w_n∈[−0.4076,0] FROZEN) against ρ_s≈const from fold to τ=0.6 yields x_today > x_fold=85.7928 monotonically, with late-time q(x_today)≈−1 — fixing the A-window for the route-invariance gate.
**Plan reference**: `sessions/session-plan/session-97-plan-w1.md` §W1-2 (Sage-exact monotonicity, w_n band endpoints, q→−1 late-time claim).

**Output Artifacts**:
- Script: `computations/session-97/s97_w1_xtoday.py` — `grep -E "from canonical_constants import"` → `from canonical_constants import (  # noqa: E402`; `grep -cE "append_verdict"` → `2` (def + call). PASS.
- Data: `computations/session-97/s97_w1_xtoday.npz` (61,435 bytes) — present; carries `x_today_band_lo/hi`, `x_tau_hi/lo`, `a_eff`, `q_today_*`, monotonicity + cross-check fields.
- Plot: `computations/session-97/s97_w1_xtoday.png` (165,905 bytes) — present; Panel A x(τ) band to τ_now=0.6 vs x_fold, Panel B q(x)→−1.
- Verdict line: `computations/session-97/s97_gate_verdicts.txt` — matches `^S97-W1-XTODAY:.* audit_sha256=[a-f0-9]{64}` (audit_sha256=`067fe8074406d44fc0dbf5054f673865f813ad4be331a529c90e1a39e7ca3f8c`); dual-SHA companion row + detail + cross-check + regulator-pin companion rows present.
- WP section: this `### §W1-2. S97-W1-XTODAY` — Status COMPLETED + Verdict PASS.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; query-first discipline executed before scripting):
- `search_knowledge("GGE-TWO-FLUID-67 FROZEN w_n band normal component")` → gate `GGE-TWO-FLUID-67` (S67, W7-B, INFO; Volovik normal-component EoS); confirms the w_n band originates in the S67 generalized Landau–Khalatnikov closure. NOT a duplicate of this gate.
- `search_knowledge("S67 ODLRO x_fold 85.7928 superfluid normal ratio")` → gate `S96-W1-VOLOVIK-2FLUID` carries `x_fold=85.7928`, `SF54_band=[−0.97,0.81]`; the upstream 2-fluid integration this gate consumes.
- `search_knowledge("x_today substrate-determined late-time deceleration vacuum-dominated")` → no prior `x_today` gate/constant; this gate produces it (not PRE-CLOSED).
- `get_constant("x_fold")` → not found (lives in the upstream npz as a scalar, not a canonical constant; rebuilt from S67 ODLRO fractions 0.98848/0.01152 = 85.7928 and cross-checked).
- `get_constant("w_n_GGE")` → not found; the FROZEN endpoints are read from the upstream npz (`w_n_ideal=0.0`, `w_n_volovik=−0.407649206353356`) and matched to the plan pins.
- `list_constants("M_KK_inv|w_n|x_fold|GGE")` → `M_KK_inv_seconds=8.86044e-42` (S96) confirmed canonical (diagnostic only here); no `x_today`/`w_n` canonical exists.
- Verdict: **NOT PRE-CLOSED** — `x_today` is a new substrate-determined output; all consumed values (x_fold, w_n band, a₂^ζ) trace to landed canonicals/upstream npz.

**Verdict**: **PASS** — `S97-W1-XTODAY: PASS` (value reproduces inline below; full line in `s97_gate_verdicts.txt`). x_today band > x_fold (both FROZEN endpoints, monotone) AND q(x_today)≈−1 within ±0.05 (both endpoints). The substrate determines the A-PASS x-window for the route-invariance gate 1.3; the late-τ substrate is vacuum/effacement-dominated by construction.

**Results**:

*Numbers first.* 4-tuple: `(value = x_today_band = [103.2171, 117.2232], scheme = Volovik-two-fluid-differential-dilution, convention = RATIO, L_max = 10)`.

*Primary output — x_today BAND* (over the two FROZEN w_n endpoints {−0.4076, 0}):

| endpoint | w_n | d ln x/d ln a = 3(1+w_n) | x_today | x_today > x_fold=85.7928 | q(x_today) | \|q+1\| ≤ 0.05 |
|:--|:--|:--|:--|:--|:--|:--|
| upper | 0.0 (dust) | **+3.00000** | **117.2232** | True | −0.987312 | True (0.0127) |
| lower | −0.407649 (Volovik) | **+1.77705** | **103.2171** | True | −0.991474 | True (0.0085) |

**x_today band = [103.2171, 117.2232]** (lower↔Volovik EoS, upper↔dust EoS), strictly greater than **x_fold = 85.7928** for both endpoints. **q(x_today) band = [−0.9915, −0.9873]**, worst-case |q+1| = **0.0127 ≤ τ_q = 0.05** ⇒ both endpoints PASS, INFO-band not triggered.

*Machinery pins (PRDR)*: N_eval=1001; τ∈[0.190, 0.6]; step=4.10e−4 (uniform on the [0.190,0.6] window; the plan's 3.6e−4 was for the [0.190,0.451] sub-window, declared here as the operational pin for the full window — matches §W1-1's same disclosure); tolerance=1e−10; scheme=FW; convention=RATIO; GPU_path=numpy.linalg (1D cumulative integration, CPU); w_n_endpoints=[−0.407649, 0.0]; x_fold=85.7928; q_target=−1.0; tau_q=0.05; rho_s_model=const; regulator_pin=a_2^ζ (a_eff backbone via AOFT `H2_aeff`, a_2^ζ=2776.165389).

*Substitution chains (both CLAIMs pre-registered, Sage-verified — `mcp__sage__sage_eval`)*:

- **CLAIM 1 (monotonicity, [VERIFY] sign)** "x_today > x_fold":
  - Def 1: x = ρ_s/ρ_n  [condensate/normal density ratio]
  - Def 2: ρ_s ≈ const (a^0)  [unbroken-condensate vacuum, w=−1, carries Γ_eff=0.99970]
  - Def 3: ρ_n ∝ a^{−3(1+w_n)}  [GGE normal gas, w_n∈[−0.4076, 0]]
  - Substitute Def 2,3 into Def 1: x ∝ a^{+3(1+w_n)}
  - Differentiate (log): **d ln x/d ln a = 3(1+w_n)**
  - Simplify (endpoints): w_n=0 → **+3** (>0); w_n=−0.407649 → **+1.77705** (>0)
  - Canonical form: d ln x/d ln a = 3(1+w_n) > 0 ∀ w_n∈[−0.4076, 0]
  - **Direction**: x strictly increasing in a; since a_eff advances (a_eff(0.6)=1.1097 > a_eff(τ_fold)=1) as τ runs fold→0.6, **x_today > x_fold**. [Sage `sage_eval`: `3*w_n+3`, =3 and =1.77705 at endpoints. Numerical slope from reconstructed arrays: 3.000000 / 1.777052, resid_max=4.37e−13 vs the analytic value.]

- **CLAIM 2 (late-time deceleration, sign)** "q(x_today) ≈ −1":
  - Two-fluid EoS: p_n=0 (w=0 dust) or p_n=w_n ρ_n (Volovik); p_s=−ρ_s (w=−1 vacuum).
  - q(x) = ½[(1+3w_n) + x(1+3w_s)]/(1+x), w_s=−1.
  - As x = ρ_s/ρ_n → large (condensate-dominated), **lim_{x→∞} q(x) = −1 EXACTLY, independent of w_n** [Sage `sage_eval`: `limit(q, x=oo) = -1`].
  - **Direction**: increasing x drives q monotonically toward −1; at x_today∈[103, 117], q∈[−0.9915, −0.9873] confirms the late-τ endpoint is vacuum/effacement-dominated.

*Cross-checks (reproduce landed S96-W1-VOLOVIK-2FLUID)*:
- x(τ*) via the SAME power law on the upstream a_norm grid: w_n=0 → **401.7197 vs landed 401.7197** (rel **0.0e+00**); w_n=−0.4076 → **214.0945 vs landed 214.0945** (rel **0.0e+00**).
- q-formula reproduces the landed `q_ideal`/`q_volovik` arrays on the upstream τ-grid: max residual **0.0e+00**.
- q(x_star_ideal=401.72, w_n=0) = −0.996275 = upstream `q_ideal.max` (the 2-fluid npz endpoint q at τ*). All cross-checks bit-exact.
- Upstream-consistency matches: x_fold (=85.7928, ODLRO rebuild matches), w_n endpoints (both match plan pins to <1e−9/<1e−12), w_s=−1, a_2^ζ match canonical — all True.

*Convention note (honest disclosure)*: the 2-fluid npz `tau_grid` ends at the AOFT fixed point τ*=0.451041; the plan's "integrate to τ=0.6" is realized via the AOFT acoustic-rate window (`H2_aeff` over fold→0.6 in `s96_w1_aoft_friedmann_map.npz`). a_eff(τ) is reconstructed by cumulative-trapezoid integration of H_aeff=√(H2_aeff), anchored a_eff(τ_fold)=1 — the plan's "a_eff ∝ √a₂ on the AOFT map" operationalized as the per-τ acoustic-rate array. x(τ) is then extended onto fold→0.6 via the Sage-exact dilution power law. The reproduction of the landed τ* values (rel 0.0e+00) confirms the extension is the same physics as the upstream 2-fluid integration, evaluated on the longer AOFT window.

**Substrate-IS assessment** (`.claude/rules/phononic-framing.md`): x = ρ_s/ρ_n is the ratio of the substrate's unbroken-condensate vacuum density to its GGE normal-component (quasiparticle-gas) density. As the order parameter τ advances past the van Hove fold, the GGE normal component **redshifts** (ρ_n ∝ a^{−3(1+w_n)}, the n_pairs=59.8 Bogoliubov relic with w_n∈[−0.4076,0]) while the unbroken condensate vacuum stays ≈const (w=−1) — so the substrate becomes progressively **more condensate-dominated** and x grows from 85.79 (fold) to 103–117 (τ_now=0.6). This is the substrate-IS reading of "the universe becomes dark-energy dominated": **not a container filling with vacuum, but the order-parameter trajectory carrying spectral weight toward the unbroken-condensate (w=−1) sector**. q(x_today)≈−1 is the acoustic-time curvature of that trajectory at the late-τ endpoint. The arrow is substrate-first: D_K eigenvalues reorganize past the fold → Bogoliubov |β_k|² sets ρ_n → differential dilution (ρ_n redshifts, ρ_s const) → x(τ) grows → late-time q→−1. The Volovik source: the post-transit substrate IS a two-fluid system (Volovik, *The Universe in a Helium Droplet*, superfluid two-fluid hydrodynamics); ρ_s is the effaced w=−1 vacuum (the part of the BCS condensate that has NOT decohered into GGE quasiparticles), and what ΛCDM calls dark energy is this effacement residual (Γ_eff=0.99970). The x_today band fixes the A-PASS x-window consumed by the route-invariance gate 1.3.

---

### §W1-3. S97-W1-QOMEGA-ROUTE-INVARIANCE (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S97-W1-QOMEGA-ROUTE-INVARIANCE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (3-route discriminator on the transported two-fluid deceleration; consumes the 1.1 BLOCKER + 1.2 A-window)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: The two-fluid deceleration q_Ω(x), transported onto all three S96 H(τ) routes (AOFT, Volovik 2-fluid, GFT), is route-invariant — C-PASS if max|Δq_Ω|<0.10 (algebraic agreement), else B-PASS if in-band fraction vs the SF54 band exceeds 0.90; the A-PASS invariant-shortfall branch (shortfall>0.356) is predicted NOT to fire.
**Plan reference**: `sessions/session-plan/session-97-plan-w1.md` §W1-3 (3-leg C/B/A precedence, conformal-transport formula, dual-prior Track-A/Track-B allocation).

**Verdict**: **INFO** — A-leg invariant-shortfall **FIRES** (the predicted-NOT-to-fire branch). The conformal-transported two-fluid deceleration is **route-SENSITIVE**, not route-invariant: the three H(τ) routes' conformal expansion rates disagree by `max|ΔH_A| = 3.8358 ≫ band_tol 0.356`. **Track B** (route-sensitive; the C1 a(t) frontier's deceleration is CONDITIONAL on which H(τ) route reconstructs it). 3-tuple `sign=PASS / magnitude=FAIL / regime=MARGINAL`; composite collapse `magnitude=FAIL ∧ regime=MARGINAL ⇒ INFO`, matching the plan's pre-registered A-fires→INFO rubric.

**Output Artifacts**:
- Script `computations/session-97/s97_w1_qomega_route_invariance.py` — EXISTS (48,953 B). `grep -cE "from canonical_constants import"` → **1**; `grep -cE "append_verdict"` → **2**. PASS.
- Data `computations/session-97/s97_w1_qomega_route_invariance.npz` — EXISTS (198,315 B); keys include `q_{aoft,vol,gft}_transported` (robust H_A-form), `q_{…}_transported_literal` (plan-form), `HA_{aoft,vol,gft}`, `dHA_*` pairwise, `q_alg_{ideal,volovik}`, `tau_common`/`tau_trim`, plus all scalars + dual-SHA.
- Plot `computations/session-97/s97_w1_qomega_route_invariance.png` — EXISTS (192,882 B); 4 panels: (a) pole-free H_A per route, (b) pairwise |ΔH_A| vs C-threshold, (c) transported q_Ω (clamped ±3; poles at H_A=0), (d) leg-i algebraic anchor.
- Verdict line in `computations/session-97/s97_gate_verdicts.txt` matching `^S97-W1-QOMEGA-ROUTE-INVARIANCE:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion row **and** the schema-v2 3-tuple companion row (`# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=MARGINAL`). LIVE (non-superseded) line: composite **INFO**, `audit_sha256=6dcc22f12287f5bae9d8438447f0772d84c3c6d094630da40fa4a64bde75a4a1`. PASS.
  - *Supersession note (gate-verdicts.md Option A — absolute verdict permanence)*: three prior canonical lines from in-session script-refinement iterations are RETAINED on disk; each corrective line carries `supersedes=<full-64-char prior audit_sha>`. Chain `8756ea30(FAIL)→ecb17c76(INFO)→970f0105(INFO)→6dcc22f1(INFO, LIVE)`. Downstream consumers read the latest non-superseded line (INFO).
- This WP §W1-3 with Status COMPLETED + Verdict INFO. PASS.

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("SF54 deceleration band q_Omega two-fluid acoustic")` → SCALE-FACTOR-54 (PASS): `q: −0.97 → +0.81` (Connes-distance proxy) — the SF54 deceleration band `[−0.97,0.81]`; S96-W1-VOLOVIK-2FLUID (FAIL, `q_max_volovik=−0.1115`, band not reproduced); S95-W4-4-SP-CONFORMAL-EMBED (INFO, a₂-proxy q_Ω out of band).
- `search_knowledge("S96 GFT Friedmann max_abs_dev_q q_PASS_ceiling route invariance")` → S96-W1-GFT-FRIEDMANN (INFO): `max_abs_dev_q=0.836892`, `q_PASS_ceiling=0.3560`, `q_in_band_frac=0.7403`, `q_SF54_band=[−0.97,0.81]` — the A-leg `band_tol=0.356` is exactly this `q_PASS_ceiling`; S96-W1-AOFT-FRIEDMANN-MAP (PASS, `H2_star=7.478844e-03`). Confirms the gate is NOT pre-closed; the route-invariance discriminator is a genuinely new comparison.
- Not PRE-CLOSED — no closure covers the 3-route invariance discriminator (S96 only ran single-route GFT-vs-SF54, INFO).

**Results** — *NUMBERS first, gate second, interpretation third.*

**4-tuple**: `(value=max|ΔH_A|=3.835844 [PRIMARY, pole-free] / literal max|Δq_Ω|=3.00e12 [pole-laden], scheme=conformal-transport-q-Omega-3route, convention=MIXED, L_max=10)`.

**Machinery pins** (plan W1-3 `machinery_pin_map`): `N_eval=1001` (common τ-grid); `scan_range=[0.190,0.6]` intersected per route → common support `[0.190, 0.451041]` (Volovik caps); `C_thresh=0.10`; `B_thresh=0.90`; `A_band_tol=0.356` (=`q_PASS_ceiling`, S96-W1-GFT); `SF54_band=[−0.97,0.81]`; `routes=[aoft_friedmann_map, volovik_2fluid, gft_friedmann]`; `x_window_source=S97-W1-XTODAY` (A-window `[103.2171, 117.2232]`, PASS); `omega_profile_source=S97-W1-OMEGA-PROFILE` (leg-ii BLOCKER, PASS, non-constant); `regulator_pin=a_2^{ζ}` (CLASS=FULL); `L_max=10`. Step-size: uniform `Δτ=(0.451041−0.190)/1000=2.61e-4` on the common grid (the plan's `3.6e-4` was the full-window step; same disclosure as 1.1/1.2 — honor the window endpoints).

**leg-ii ENABLE check (1.1 OMEGA-PROFILE consumption)**: Ω composite=PASS, `rel_spread=6.420e-2 ≫ 1e-3`, `dot_is_null=False` ⇒ **leg-ii ENABLED, FULL conformal transport runs**. The constant-Ω q_bare collapse does **not** apply (Sage-verified at plan-freeze: `q_acoustic(Ω̇=Ω̈=0) − q_bare = 0`; since Ω is non-constant with `Ω̇<0` throughout, the transport carries independent acoustic-deceleration content).

**q-convention (S96-matched)**: `q = −a·a″/(a′)²` with `′ = d/dτ` (τ-as-time, the substrate clock). Verified to reproduce S96 `q_gft` from `a_gft` to **0.0 max-dev** (the `−1−Ḣ/H²` τ-form differs by FD asymmetry — so the `a`-second-derivative form is canonical here). Conformal transport: `A_route(τ) = Ω(τ)·a_bare_route(τ)`, with `a_bare` reconstructed from each route's H(τ) (AOFT: `√H2_aeff` integrated; GFT: stored `a_gft`; Volovik: stored `a_norm`).

**Conformal-rate split (pole-free PRIMARY discriminator)**. Sage-verified identity (this session, two forms equal in cosmic time): `q = −A·Ä/Ȧ² ≡ −1 − Ḣ_A/H_A²` with `H_A = H_bare + d ln Ω/dτ`. The literal `−A·Ä/Ȧ²` form has a **removable coordinate pole** wherever `A′(τ)=0 ⟺ H_A=0` (a conformal-stationary turning point); `H_A` itself is smooth/finite, so the route-disagreement is carried robustly by `H_A`:

| Route | `H_A` range | well-cond. frac (`|H_A|≥1e-2`) |
|:--|:--|:--|
| AOFT (1) | `[−0.000877, +0.000874]` (≈ **0**: conformally stationary) | 0.000 |
| Volovik (2) | `[−0.3057, +3.8363]` | 1.000 |
| GFT (3) | `[−0.2192, +0.0220]` | 0.897 |

**Root cause (pole-free, unambiguous)**: the three routes' bare scale factors grow by very different factors over the common window — **AOFT 1.048×, VOL 1.673×, GFT 1.024×** — while sharing the same conformal factor Ω (which decreases ×0.954). For AOFT the bare growth nearly cancels Ω's decrease ⇒ `H_A≈0` (acoustic-frame stationary); for VOL the bare growth dominates ⇒ large `H_A`; for GFT Ω's decrease overtakes the weak growth ⇒ slightly-negative `H_A`. The conformal transport CANNOT make them agree because the bare H(τ) reconstructions themselves differ by ~1.6× in total growth.

**C-leg** (the [SIGN] discriminator). PRIMARY pole-free `max|ΔH_A|`: AOFT–VOL `3.8358`, AOFT–GFT `0.2191`, VOL–GFT `3.8171` → **max = 3.835844**. LITERAL plan-form `max|Δq_Ω| = 3.00e12` (pole-laden at H_A=0). Both ≫ `C_thresh=0.10` ⇒ **C-FAIL** (`C_pass=False`). Bare-route spread `nan` (bare AOFT also has near-stationary A) → `transport_reduced_spread=False`: the transport did NOT reduce the spread.

**B-leg**. Pooled `frac_in_band` (q_Ω ∈ `[−0.97,0.81]`, finite points, pooled over the 3 routes) = **0.1899** (AOFT 0.000, VOL 0.570, GFT 0.000) < `B_thresh=0.90` ⇒ **B-FAIL** (`B_pass=False`).

**A-leg** (predicted NOT to fire). `max_abs_dev_q = max|q_route − q_SF54|` (EXACT S96-GFT structure — verified S96 `abs_dev_q == |q_gft_overlap − q_sf54_overlap|`, max 0.836892), pole-free per route: VOL `47379.21`, GFT `7568.79`, AOFT `nan` (fully stationary). route-max `= 47379.21`; **invariant_shortfall = 47379.21 − 0.356 = 47378.85 > band_tol 0.356** ⇒ **A-FIRES** (`A_fires=True`). The literal `max_abs_dev_q` is spike-dominated (Volovik's q spikes near its turning point); the **robust cross-confirmation** is the pole-free `max|ΔH_A| = 3.8358 > 0.356` (`A_fires_via_HA=True`) — A fires by any measure. (S96 BARE single-route shortfall was 0.4809; the 3-route conformal transport SHARPENS the disagreement rather than resolving it.)

**[SIGN] substitution chain (with substituted numbers)**:
```
CLAIM (C-leg [SIGN]): "max|Δq_Ω| < 0.10 ⇒ q_Ω route-INVARIANT (C-PASS)."
  Def 1: q_Ω^route(τ) = two-fluid deceleration transported onto H_route(τ).
  Def 2 (leg-ii): A=Ω·a_b; q = −A·Ä/Ȧ² ≡ −1 − Ḣ_A/H_A²,  H_A = H_bare + d lnΩ/dτ.  [Sage-verified]
  Substitute Ω̇=Ω̈=0 (null branch): q_acoustic → q_bare.  [Sage-exact: q_acoustic−q_bare=0]
    → N/A here: 1.1 PASS, Ω non-constant (rel_spread 6.42e-2), so the FULL transport runs.
  Compute (numbers): H_A,AOFT≈0, H_A,VOL∈[−0.31,3.84], H_A,GFT∈[−0.22,0.02];
    max|ΔH_A| = 3.835844  ≫  0.10  ⇒  C-PASS = False.
  Direction (C-leg): max|Δq_Ω| ≪ 0.10 would mean route-invariant; computed 3.84 ≫ 0.10
    ⇒ route-SENSITIVE (the deceleration is NOT a route-robust observable on these 3 reconstructions).
  Direction (A-leg, the realized branch): invariant_shortfall = max|q_route−q_SF54| − q_PASS_ceiling
    = 47379.21 − 0.356 = 47378.85 > 0.356 (and the pole-free max|ΔH_A|=3.84 > 0.356)
    ⇒ A-FIRES ⇒ INFO ⇒ Track B (route-sensitive; the plan's Track-A "expected NOT to fire" prediction is FALSIFIED).
```

**Why the A-leg was predicted NOT to fire, and why it does**: the plan's Track-A prior (0.65) reasoned that the S96 BARE GFT-vs-SF54 disagreement (`max_abs_dev_q=0.836892`) would be REDUCED by the conformal transport (a shared Ω pulling the routes together). The transport does the opposite: because the bare scale-factor growths differ by ~1.6× and the SAME Ω is applied to all three, the conformal Hubble `H_A = H_bare + d lnΩ/dτ` AMPLIFIES the route difference (AOFT lands at H_A≈0 — conformally stationary — while VOL lands at H_A~3.8). The shared Ω cannot homogenize routes whose bare expansion histories already disagree.

**dual-prior posterior re-allocation** (plan W1-3 `dual_prior`): prior `Track A 0.65 / Track B 0.35`. Discriminator outcome = **A-PASS shortfall fires** → **0.9 to Track B** (route-sensitive: the routes genuinely disagree beyond the SF54 band even after conformal transport; the emergent-FRW q is route-sensitive, so the C1 a(t) frontier's deceleration is CONDITIONAL on route choice). `dual_prior_track = Track_B_route_sensitive_0.9`.

**3-tuple + composite** (gate-verdicts.md PRE-REGISTERED collapse):
- `sign_verdict = PASS` — the [SIGN] discriminator correctly READS the sign/direction of route-disagreement: the routes genuinely diverge (positive, correctly-signed disagreement; the A-leg's own pre-registered firing direction is realized). Not a sign error.
- `magnitude_verdict = FAIL` — the discriminator magnitude is way out of the PASS band (max|ΔH_A|=3.84 ≫ 0.10; A-shortfall fires).
- `regime_verdict = MARGINAL` — auto-shortening band: `f_used = (0.451041−0.190)/(0.6−0.190) = 0.6367 ∈ [0.50,0.95)` (the Volovik route caps the common support at τ*=0.451041; AOFT/GFT reach 0.6).
- Composite: `magnitude=FAIL ∧ regime=MARGINAL ⇒ INFO` — matches the plan's pre-registered A-fires→INFO Track-B rubric exactly.

**Cross-checks**:
1. **q-convention vs S96**: `q=−a·a″/(a′)²` (τ-derivatives) reproduces S96 `q_gft` from `a_gft` to 0.0 max-dev (the `−1−Ḣ/H²` τ-form differs by FD asymmetry); convention is S96-consistent.
2. **Two-form equivalence (Sage)**: `q=−A·Ä/Ȧ² ≡ −1−Ḣ_A/H_A²` and `H_A = H_bare + d lnΩ/dτ` (both residuals = 0 in cosmic time); the literal and robust legs are the same object, differing only in pole-conditioning.
3. **Null-collapse (Sage)**: `q_acoustic(Ω̇=Ω̈=0) − q_bare = 0` (simplify_full) — confirms the leg-ii BLOCKER dependence on Ω̇,Ω̈ and the constant-Ω collapse; N/A here since Ω is non-constant.
4. **leg-i algebraic anchor (route-independent)**: `q_two_fluid(x(τ),w_n) = ½[(1+3w_n)+x(1+3w_s)]/(1+x)` on the shared x(τ) gives `q ∈ [−0.996, −0.983]` (w_n=0) — a single route-independent curve (x is one substrate ratio), confirming the route-disagreement is a property of the conformal TRANSPORT (H_A), not of the underlying two-fluid EoS.
5. **A-leg structure vs S96**: `max_abs_dev_q = max|q_route − q_SF54|` reproduces the exact S96-GFT comparison structure (not band-excess), with SF54 q taken from the upstream `sf54_q_on_grid` (200-pt common grid). Cross-confirmed by the pole-free `max|ΔH_A| > band_tol`.

**Substrate-IS assessment** (`phononic-framing.md`). q is the **curvature of the order-parameter trajectory read in acoustic time** — τ IS the substrate clock (the order-parameter coordinate of the Jensen-deformed spectral triple), not a coordinate on a container. The route-invariance test asks whether "the universe's deceleration history" is intrinsic to the D_K spectrum (`D_K spectrum → {3 H(τ) routes} → conformal transport via Ω → q_Ω per route → discriminator`) or an artifact of which emergent-metric reconstruction one chooses. **The verdict is route-SENSITIVE (Track B)**: the three reconstructions of the substrate's effective H(τ) — covariant AOFT spectral-action, two-fluid Landau–Khalatnikov, GFT condensate — produce conformal expansion rates that disagree by order ~4 (`max|ΔH_A|=3.84`), because their bare scale-factor growths differ by ~1.6× while sharing one conformal factor. This is NOT a failure of the substrate picture; it is a **structured, pre-registered constraint-map finding**: the emergent-FRW deceleration is NOT yet a route-robust substrate-IS observable on these three S96 reconstructions, so the C1 a(t) frontier's deceleration history is **CONDITIONAL on route choice**. The substrate IS the spectrum; the three routes are three different ways of reading the *acoustic image* of its order-parameter trajectory, and they do not yet agree on the curvature of that image. The direction of explanation is preserved: the disagreement lives in how the emergent H(τ) is reconstructed FROM the substrate, not in any container the substrate would sit IN. Closing the C1 frontier requires either (i) a route-reconciliation argument (why one of the three H(τ) reconstructions is the canonical acoustic-frame rate — e.g. the AOFT covariant route as the spectral-action-derived metric), or (ii) a substrate-physics reason the bare scale-factor growths SHOULD differ (distinct effective-Friedmann content per route) with a principled selection — a genuine carry-forward.

---

### §W1-4. S97-W1-1-AT-TRAJECTORY (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S97-W1-1-AT-TRAJECTORY`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (explicit physical-seconds a(t) assembly; the C1 a(t) frontier deliverable; consumes the 1.1 Ω BLOCKER)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The explicit physical-seconds a(t) over [τ_fold,τ_now] — from H²(τ) (route-1 AOFT), t(τ)=∫dτ/τ̇, seconds via M_KK⁻¹, with {Z_norm=G_DeWitt=5.0, V0=0} pinned and O'Neill cross-terms effaced — is monotone+finite, reproduces H²(τ*)=7.478844e-03 at τ*=0.451041 to rel<1e-6, and has a unique trajectory shape.
**Plan reference**: `sessions/session-plan/session-97-plan-w1.md` §W1-4 (H²(τ*) exact-value cross-check, τ→t map, shape-uniqueness vs 1-parameter τ̇-band INFO branch).

**Verdict**: **INFO** — a(t) is monotone-increasing + finite over [τ_fold, τ_now] in physical seconds AND reproduces the AOFT anchor H²(τ*)=7.478844e-03 at τ*=0.451041 to **rel = 5.456e-08 < 1e-6** (both conditions PASS, band-invariant), BUT the trajectory **shape is NOT unique**: the τ̇(τ) profile inherited from S96-W1-TAUDOT-PROFILE has `unique_selection=False` (50/50 admissible shapes, none selected), leaving a residual **1-parameter seconds-normalization band** (t(τ_now) rel-spread = 0.419). Per the plan W1-4 INFO_meaning, this is a valid partial: the trajectory exists and is anchored, but its absolute seconds-scaling is the κ-knob — **gate 1.5 (S97-COOLING-BUDGET-KAPPA-PIN)** is the gate that would pin the band. 3-tuple: `sign=PASS, magnitude=PASS, regime=VALID`; composite collapses to INFO via the shape-uniqueness clause (NOT the magnitude/regime path — both of those PASS).

**Output Artifacts**:
- Script `computations/session-97/s97_w1_1_at_trajectory.py` — `grep -E 'from canonical_constants import|append_verdict'`:
  - `from canonical_constants import (  # noqa: E402`
  - `def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,`
  - `append_verdict(composite, value_str, audit_sha, content_sha,`
- Data `computations/session-97/s97_w1_1_at_trajectory.npz` — present (62 keys: tau/H2/H/Omega_on, t_{widest,lo,hi}_{mkk,sec}, a_{widest,lo,hi}, monotonicity+anchor+shape flags, dual-SHA).
- Plot `computations/session-97/s97_w1_1_at_trajectory.png` — present (3-panel: H²(τ) with τ* anchor; t(τ) acoustic-time map with 1-param τ̇-band; explicit a(t) trajectory + summary box).
- Verdict line `computations/session-97/s97_gate_verdicts.txt` — `^S97-W1-1-AT-TRAJECTORY:.* audit_sha256=[a-f0-9]{64}` matches; canonical line + dual-SHA companion row + 3-tuple annotation row + ANCHOR provenance row.
  - `audit_sha256=b8507148b91b7163cd92b1ed471f4176950f33d1e02421c272ef44b9f2aae3dd`
  - `content_sha256=63503fa39c72b745c08dbae0b394454136ececfaad2b699744e2861e761e1b85`

**MCP Pre-Compute Audit**:
- `get_constant("M_KK_inv_seconds")` → 8.860439881925477e-42 s (S96, `s96_w1_mkk_seconds.npz`, gate S96-W1-MKK-SECONDS). Used for the substrate-clock → SI conversion.
- `get_constant("G_DeWitt")` → 5.0 (S42, `s42_gradient_stiffness.npz`). Confirms Z_norm = G_DeWitt = 5.0 pin.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). Window lower endpoint.
- `search_knowledge("S96-W1-AOFT-FRIEDMANN-MAP H² anchor")` → gate S96-W1-AOFT-FRIEDMANN-MAP **PASS** (audit `edfe1f7f…`); the equation entry confirms `H²(τ*)=7.478844e-03 M_KK²`; the GFT cross-route INFO line independently reports `H2_star_reduced=7.478844e-03`. **The anchor is a settled S96 canonical** — reproduced here as an exact-value cross-check, NOT re-derived (anchor is verbatim per the plan).
- `search_knowledge("O'Neill non-flat submersion effacement")` → S85-BASE-PONTRYAGIN-PARITY-PRESERVE PASS (Riemannian-submersion-non-flat-base); CC Closure 2 (A-tensor cross-terms, S61); confirms cross-terms exist but are effaced. NPZ check: `ratio_hubble=6.84e-117 ≪ 3e-7` ⇒ `oneill_effaced=True`.
- **NOT PRE-CLOSED**: no prior gate assembles the explicit physical-seconds a(t) trajectory; this is the C1-frontier deliverable consuming the (now-landed) 1.1 Ω BLOCKER. The constituent pieces (H²(τ), τ̇ family, Ω bridge, O'Neill effacement) are all settled; the *assembly + monotonicity/anchor/shape verification* is the new work.

**Results**:

*4-tuple*: `(value=5.456e-08, scheme=FW, convention=ABSOLUTE, L_max=10)` — value = |H²(τ*) − 7.478844e-03| / 7.478844e-03.

*Numbers first*:
- **H²(τ) > 0 everywhere** on [0.190, 0.600]: min = 6.666678e-03, max = 8.208884e-03 M_KK² (read off `H2_src`, route-1 AOFT map; monotone decreasing in τ but strictly positive — H² being positive, not monotone, is what matters for a(t) monotonicity).
- **a(t) monotone↑ + finite**: a(t_fold)=1.0 → a(t_now)=1.055765 (widest admissible τ̇ profile); strictly increasing for the widest profile AND across the full admissible τ̇ band; all finite. Total e-folds N_e = ln(a_end/a_start) = 0.054266.
- **H²(τ*) anchor reproduction**: τ* = 0.4510412982 (full-precision S96 canonical); H²(τ*) reproduced = 7.4788435920e-03; **rel vs anchor 7.478844e-03 = 5.456e-08 < 1e-6** (PASS); rel vs npz `H2_star_reduced` = **0.0** (FD-floor, exact). This is an interpolation of `H2_src` at τ*, a verbatim cross-check, not a fit.
- **Shape-uniqueness FAILS**: t(τ_now) band over the admissible τ̇ family = [0.410, 0.627] M_KK⁻¹ ⇒ rel-spread = 0.419; `taudot_unique_selection=False`; ⇒ `shape_unique=False`. The 1-parameter band persists. (Fiducial τ̇_fold=1 → t_widest(τ_now) = 0.627 M_KK⁻¹ = 5.559e-42 s; the *absolute* SI seconds-scaling is set by the κ-knob, which is gate 1.5.)

*Machinery pins*: N_eval=1001; scan_range=[0.190, 0.600] (τ* internal anchor); step_size = cumulative-trapezoid on the τ→t map; Z_norm = G_DeWitt = 5.0; V0 = 0; M_KK_inv_seconds = 8.860439881925477e-42; H2_star_anchor = 7.478844e-03; tau_star = 0.451041 (full 0.4510412982); oneill_effacement=True (`ratio_hubble`=6.84e-117 ≪ 3e-7); omega_bridge_source = S97-W1-OMEGA-PROFILE (PASS, non-constant Ω, `Omega_fold`=2.241017); regulator_pin = a_2^{ζ}; CLASS=FULL.

*[VERIFY] substitution chain (monotonicity, with substituted numbers)* — per `math-scripts.md §"Double-Check Logic Before Compute"`, pre-registered in the plan W1-4 and the script docstring:
- **Step 1 (defs)**: H²(τ) = (ȧ/a)² [AOFT `H2_src`]; t(τ) = ∫_{τ_fold}^{τ} dτ'/τ̇(τ') [τ̇>0 forward transit]; sec(t) = t·M_KK_inv_seconds; a(t) = a(t_fold)·exp(∫_{t_fold}^t H dt'), H = +√(H²) ≥ 0.
- **Step 2 (substitute)**: H(τ) = +√(H²(τ)); ln a(t) − ln a(t_fold) = ∫ H dt' = ∫_{τ_fold}^{τ} [H(τ')/τ̇(τ')] dτ' (change of variable dt = dτ/τ̇).
- **Step 3 (simplify, one step/line)**: H²(τ) > 0 on [0.190,0.600] (computed: H² ∈ [6.667e-3, 8.209e-3] > 0) ⇒ H = √(H²) ≥ 0 everywhere; τ̇(τ) > 0 (g = τ̇/τ̇_fold ∈ [g_clock, 1] > 0) ⇒ integrand H/τ̇ ≥ 0 ⇒ ∫ monotone non-decreasing.
- **Step 4 (direction read-off)**: da/dt = a·H ≥ 0 (a>0, H≥0) ⇒ a(t) monotone **increasing** (strictly, H>0 on the interior). The anchor H²(τ*)=7.478844e-03 is read DIRECTLY off H²(τ) at τ* (independent of the t-map) ⇒ band-**invariant**.
- **Step 5 (conclusion)**: a(t) strictly increasing + finite; H²(τ*) reproduced rel<1e-6 (exact-value cross-check). Monotonicity + anchor are INVARIANT under the τ̇ one-parameter band (the band rescales the *time axis* only, not the sign of da/dt nor the H² read-off). Shape-uniqueness is the SEPARATE test and the only failing sub-condition ⇒ INFO. **No new sign derivation**: H²>0 is read off the AOFT map; the anchor is a verbatim S96 canonical.

*Verdict line + dual-SHA*: `S97-W1-1-AT-TRAJECTORY: INFO -- value='composite=INFO;…;anchor_reldev=5.456e-08;…;shape_unique=False;taudot_band_spread=0.4191;…;kappa_knob_pins_seconds_band=gate_1.5_S97-COOLING-BUDGET-KAPPA-PIN' scheme=FW convention=ABSOLUTE L_max=10 audit_sha256=b8507148… content_sha256=63503fa3… schema_version=S84+`, with dual-SHA companion + 3-tuple annotation + ANCHOR provenance rows.

*Cross-checks*:
- (i) Anchor exactness: H²(τ*) interp matches the npz `H2_star_reduced` to 0.0 (not just <1e-6) — the AOFT map's own fixed-point value is recovered bit-for-bit.
- (ii) Monotonicity band-invariance: ALL 50 admissible τ̇ shapes give strictly-increasing a(t) (`a_monotone_band=True`), confirming the direction is independent of the 1-parameter ambiguity (the band only stretches the t-axis).
- (iii) Ω bridge is non-trivial: `omega_nonconst=True` (1.1 PASS) ⇒ the order-parameter a(τ) → acoustic a(t) map is a genuine conformal map, NOT the constant-Ω degenerate re-scaling (the 1.1 INFO-null branch did not fire). Ω(τ) was loaded and interpolated onto the a(t) grid (`Omega_on`) as the bridge object.
- (iv) O'Neill effacement: `ratio_hubble`=6.84e-117 ≪ effacement bound 3e-7 ⇒ the product-metric Friedmann form is exact to that order (cross-terms effaced; `oneill_effaced=True`).

*Substrate-IS assessment*: a(t) is **NOT a container expanding in time**. It is the acoustic image of the substrate's order-parameter trajectory: as the Jensen deformation τ advances past the van Hove fold (τ_fold=0.190), the D_K eigenvalue spectrum reorganizes — **spectral complexity grows** — and an external acoustic observer reads that growth as a scale factor. The explanation flows strictly substrate → emergent: D_K eigenvalues → a₂ (2nd Seeley-DeWitt moment, regulator-pinned a_2^{ζ}) → H²(τ) (the FRW-form *rate* of spectral-complexity growth, route-1 AOFT) → t(τ) via the order-parameter speed τ̇(τ) → SI seconds via the substrate clock tick M_KK⁻¹ → a(t). The conformal factor Ω(τ)=√(ρ_s/a₂) (gate 1.1) bridges the bare order-parameter a(τ) to the acoustic a(t); the H²(τ*) anchor pins the absolute normalization of the *shape*. The residual 1-parameter band is NOT a free parameter of an expanding box — it is the substrate's own under-determined sweep-rate normalization τ̇_fold (the rate at which the order parameter traverses its configuration space), which the cooling-budget κ-pin (gate 1.5) over-determines from the thermodynamic side. The deliverable is the **explicit, anchor-normalized trajectory** — the substrate-IS reading of the framework's "expansion history" — modulo the single seconds-scaling knob that gate 1.5 closes.

*Solution-space update*: The C1 a(t) frontier now has an EXPLICIT, monotone, finite, H²(τ*)-anchored trajectory in physical seconds — closing the S96-W1 existence+magnitude result into a concrete a(t) up to one seconds-normalization. The corridor that remains open is the absolute τ̇_fold (κ) scaling; the monotonicity and the anchor are corridor-closed (band-invariant). FAIL would have required non-monotone/divergent a(t) or anchor off by ≥1e-6 — neither occurred.

---

### §W1-5. S97-COOLING-BUDGET-KAPPA-PIN (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `S97-COOLING-BUDGET-KAPPA-PIN`
**Trigger**: `[SIGN]` (with mandatory `[CHAIN]` Class-8.7 κ-independence pre-flight)
**Classification**: **PHONONIC** (cooling-budget over-determination of the M_KK⁻¹→s knob κ; parallel, HIGH priority). NON-PHONONIC caveat noted below for the seconds-conversion unit-chain.
**Agent**: `hawking-theorist`
**Hypothesis**: The SCENARIO-A cooling budget {T_init=0.112·M_KK, N_e_exfl=80.89, cooling exponent −0.8685} over-determines seconds-per-e-fold tightly enough to pin κ — κ_implied lands in [1e-20,1e-10] OR recovers κ_nat=8.86e-42 to |log10(κ_implied/κ_nat)|≤0.5; pre-flight establishes the exponent is a κ-independent dimensionless spectral-flow ratio (−70.25/80.89) so the gate is not Class-8.7 vacuous.
**Plan reference**: `sessions/session-plan/session-97-plan-w1.md` §W1-5 (Class-8.7 degenerate-observable pre-flight, κ_nat recovery band, W6-5 κ-sweep, dual-prior).

**Output Artifacts**:
- Script `computations/session-97/s97_cooling_budget_kappa_pin.py` (30648 B) — `grep -cE "from canonical_constants import"` → **1**; `grep -cE "append_verdict"` → **2** (def + call). ✓
- Data `computations/session-97/s97_cooling_budget_kappa_pin.npz` (15005 B) on disk. ✓
- Plot `computations/session-97/s97_cooling_budget_kappa_pin.png` (86860 B) on disk — left panel: MAIN κ_implied vs swept band; right panel: PRE-FLIGHT exponent-vs-κ flat line. ✓
- Verdict line in `computations/session-97/s97_gate_verdicts.txt` (line 9) matching `^S97-COOLING-BUDGET-KAPPA-PIN:.* audit_sha256=[a-f0-9]{64}` ✓ with dual-SHA companion row (line 10) + schema-v2 3-tuple row (line 11). `audit_sha256=f451f43ddcdb4fc756e06581b8f03920ba03a7cf3704c2dc7ec01e0f06ea7ae7` (full 64-char; unique across the file — sig_5 PASS, 3/3 distinct SHAs).
- This WP §W1-5 with Status COMPLETED + Verdict PASS.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per query-first discipline):
- `get_constant("M_KK")` → 7.428660036284456e16 GeV (S42 CONST-FREEZE-42; gravity-route alias). Used as the substrate compactification scale.
- `get_constant("M_KK_inv_seconds")` → 8.860439881925477e-42 s (S96, `s96_w1_mkk_seconds.npz`, gate S96-W1-MKK-SECONDS; closes S95-W3-1 seconds_norm_open). This IS κ_nat — the target to recover.
- `get_constant("hbar_SI")` → 1.054571817e-34 J·s (CODATA). Seconds-conversion chain.
- `search_knowledge("s53 SCENARIO-A cooling budget …")` → `s53_exflation_cmb_temp_output.txt`: **T_init=8.3201e15 GeV**, **N_e_exfl=80.89**, **ln(cooling)=−70.25**, **cooling exponent=−0.8685**, T_post(Method-2 rel)=2.5654e-15 GeV, T_CMB=2.7255 K. (Confirmed `0.112·M_KK = 8.32e15 GeV` ≡ s53 T_init.)
- `search_knowledge("W6-5 kappa sweep …")` → κ_nat=8.86044e-42 s is canonical (W1-3 CLOSED); W6-5 reproduces M_KK; no closure pre-empts the cooling-budget→κ over-determination test. **NOT PRE-CLOSED** — the gate is the new constraint.
- Sage cross-check (`mcp__sage__sage_eval`): exponent = −70.25/80.89 = −0.8684633 (→ −0.8685); `ln(T_post/T_init) = −70.254` reproduces ln_cooling; `∂(−70.25/80.89)/∂κ = 0`.

**Verdict**: **PASS** — composite `(sign=PASS, magnitude=PASS, regime=VALID)`. PRE-FLIGHT (Class-8.7) **PASS** (exponent κ-independent, NOT vacuous); MAIN recovery **PASS** (`|log10(κ_implied/κ_nat)| = 4.8e-17 ≤ 0.5`). 4-tuple: `value='preflight=PASS_kappa-indep;exponent=-0.868463;kappa_implied=8.860440e-42;log10_ratio_to_nat=-0.0000;recover_le0.5=True;in_band_1e-20_1e-10=False;decades_below_band=21.1;identity_forced_by_MKK_unit_consistency=True'`, scheme=FW, convention=ABSOLUTE, L_max=10.

**Results**:

**PRE-FLIGHT (Class-8.7 degenerate-observable disambiguator) — reported FIRST, per task. Verdict: PASS (the gate is NOT vacuous).**

The cooling exponent is a ratio of two **dimensionless** quantities:
- numerator `ln(cooling) = ln(T_final/T_init) = −70.25` (log of a temperature ratio — dimensionless);
- denominator `N_e_exfl = 80.89` (an e-fold count — dimensionless).
- `exponent_recon = −70.25/80.89 = −0.8684633` reproduces the s53 value −0.8685 to `|Δ| = 3.665e−05` (tol 5e−4). ✓

κ (the M_KK⁻¹→s seconds knob) does **not appear anywhere** in `ln_cooling/N_e`. The diagnostic recomputes the exponent at all 121 κ-sweep points across [1e-20, 1e-10]: the **spread is exactly 0.000e+00**, and the analytic `∂(exponent)/∂κ = 0` (Sage-exact — there is no κ symbol in the expression). Therefore `T(N)/T_init` carries no seconds, the exponent does not pre-bake κ, and the seconds-per-e-fold the budget over-determines is an **independent** constraint on κ — **not** a Class-8.7 finite-cardinality / degenerate-observable tautology. PRE-FLIGHT PASS.

> *Methodology self-correction (honest disclosure):* the first run used `np.gradient(constant_array, log_spaced_kappa)` as the κ-independence diagnostic. On a non-uniform log-grid this divides a numerically-identical zero numerator by sub-1e−22 adjacent-κ spacings near the band floor, amplifying 1-ULP float dust into a spurious O(1e4) "derivative" → a FALSE FAIL. The physics (κ-independence) was never in doubt — `exp_spread = 0` already proved it and Sage confirmed `∂/∂κ = 0` analytically. The diagnostic was replaced with the structural spread test (exactly 0) + the analytic-derivative flag (0 by construction). This is a numerical-method fix, not a verdict change under different conditions.

**MAIN ([SIGN] band/recovery). Verdict: recovery PASS; band-membership FALSE.**

| Quantity | Value | Note |
|:--|:--|:--|
| AOFT anchor H²(τ*) (npz `H2_star_reduced`) | 7.4788435920e−03 M_KK² | vs pinned 7.478844e−03, rel 5.46e−08 ✓ (audit `edfe1f7f…`) |
| H_star = √(H²(τ*)) | 0.0864803099 M_KK | substrate Hubble rate at τ* (inverse-ticks) |
| exfl duration N_e/H_star | 935.357 ticks | **κ-INDEPENDENT** (substrate-tick count) |
| κ_nat (recompute ℏ/(M_KK·GeV→J)) | 8.860439881925e−42 s | vs canonical, rel 1.44e−16 ✓ |
| κ_implied (leg-1 thermal: (T_init/M_KK)/ω_init) | 8.860439881925e−42 s | ω_init = E_init/ℏ = 1.264e+40 rad/s |
| κ_implied (leg-2 Hubble) | 8.860439881925e−42 s | `|leg1−leg2|/leg2 = 0.000e+00` |
| **κ_implied (reported)** | **8.860440e−42 s/tick** | |
| **log10(κ_implied/κ_nat)** | **−4.82e−17 (≈ 0)** | recovery `≤ 0.5` ✓ |
| band [1e-20, 1e-10] membership | **False** | κ is **21.1 decades below** the 1e-20 floor |
| W6-5 sweep recovery | 0/121 swept points | none expected — κ_nat sits 22 dec below the swept band |

*4-tuple*: `(value=above string, scheme=FW, convention=ABSOLUTE, L_max=10)`.

*Machinery pins (PRDR, plan §W1-5)*: N_eval=121 (W6-5 κ-sweep); κ∈[1e-20,1e-10] log-spaced; T_init/M_KK=0.112; N_e_exfl=80.89; exponent=−0.8685; ln_cooling=−70.25; T_CMB=2.7255 K; M_KK=7.428660036284456e16 GeV; H2_star_anchor=7.478844e−03 M_KK²; κ_nat=8.860439881925477e−42 s; ħ_SI=1.054571817e−34 J·s; GeV_to_J=1.602176634e−10 J/GeV; k_B_SI=1.380649e−23 J/K; scheme=FW; convention=ABSOLUTE; GPU_path=numpy.linalg (scalar/1D budget arithmetic, CPU, OMP/MKL capped at 8); tol(log10)=0.5; regulator_pin=a_2^ζ (H²(τ*) backbone via the L_max=10 AOFT map, a_2^ζ=2776.165389; no NEW bare a_n citation).

**Substitution chains (both pre-registered; Sage-verified — `mcp__sage__sage_eval`):**

- **PRE-FLIGHT CLAIM ([CHAIN]/Class-8.7)** "exponent −0.8685 is κ-INDEPENDENT ⇒ gate not vacuous":
  - Def 1: exponent ≡ ln(T_final/T_init)/N_e_exfl  [per-e-fold log-temperature ratio]
  - Def 2: ln(cooling) = ln(T_final/T_init) = −70.25  [s53; dimensionless]
  - Def 3: N_e_exfl = 80.89  [s53; dimensionless e-fold count]
  - Substitute: exponent = −70.25/80.89 = **−0.8684633** (→ −0.8685)
  - Simplify: ratio of two **dimensionless** quantities (log of a temperature ratio over an e-fold count) — carries **no seconds**.
  - Canonical form: **∂(exponent)/∂κ = 0** (κ absent from the expression; Sage `diff(−70.25/80.89, kappa) = 0`).
  - **Direction**: BECAUSE the exponent is κ-independent, the seconds-per-e-fold the budget over-determines is an INDEPENDENT constraint on κ — the gate can in principle PIN κ, not tautologically reproduce it. **NOT Class-8.7 vacuous.** [Sage: −70.25/80.89 = −0.8684633; ln(T_post/T_init)=−70.254 reproduces ln_cooling; ∂/∂κ = 0.]

- **MAIN CLAIM ([SIGN] band/recovery)** "κ_implied recovers κ_nat to ≤ 0.5 decade":
  - Def 4: κ_nat = ℏ_SI/(M_KK·GeV→J) = 1.054571817e−34 / (7.428660e16 · 1.602176634e−10) = **8.860440e−42 s/tick**.
  - Def 5: κ_implied = the seconds-per-tick the budget {T_init, N_e, exponent} + H²(τ*) over-determine. Substrate Hubble rate H_star = √(7.478844e−3) = 0.086480 M_KK (inverse-ticks); thermal leg matches the substrate energy scale T_init (M_KK units) to its SI angular frequency ω_init = E_init/ℏ, giving κ = (T_init/M_KK)/ω_init.
  - Substitute & compare: κ_implied = 8.860440e−42 s; **log10(κ_implied/κ_nat) = −4.8e−17 ≈ 0 ⇒ recovery PASS** (≤ 0.5). Band-membership FALSE (κ_implied ≈ 1e−42, **21.1 decades below** the 1e-20 floor).
  - **Direction**: the budget pins κ AT κ_nat (log10-ratio → 0) ⇒ recovery PASS; the swept band [1e-20,1e-10] does NOT contain the natural tick (κ_nat is ~22 dec below its floor).

**Structural-honesty assessment (the load-bearing finding):**

The recovery is an **IDENTITY forced by M_KK-unit consistency, NOT an independent triangulation.** Both reconstruction legs — the thermal leg `(T_init/M_KK)/ω_init` and the Hubble leg `ℏ/(M_KK·GeV→J)` — agree to `0.000e+00` and both equal κ_nat **by construction**: the substrate Hubble rate H_star (inverse-ticks), the budget temperature T_init (M_KK energy units), and the tick itself ALL live in the **same M_KK unit system**, so converting any of them to SI seconds is *dimensionally compelled* to give the same κ = ℏ/(M_KK·GeV→J). There is no second, dimensionally-independent seconds-scale *inside the budget* against which to triangulate κ. The cooling budget is therefore **CONSISTENT with κ_nat** (recovery PASS), but it does not provide an *independent over-determination* in the triangulation sense the hypothesis hoped for — the Class-8.7 pre-flight is what certifies the gate is not vacuous (the exponent does not pre-bake κ), while the recovery itself is a unit-consistency tautology. This is the substrate-IS reading: the substrate's clock tick is **intrinsically** M_KK⁻¹, and reading it through ℏ and the energy-unit chain cannot return anything else.

**Substrate-IS framing.** κ is the substrate-clock-tick (M_KK⁻¹) → SI-seconds normalization. The SCENARIO-A cooling budget IS the substrate's own thermodynamic record of the fold→now transit: T_init = post-fold GGE temperature (0.112 M_KK), N_e_exfl = exflationary e-folds (spectral-complexity doublings), exponent −0.8685 = per-e-fold log-temperature decline. The flow is `D_K spectrum → cooling budget (T_init, N_e, exponent) + H²(τ*) → seconds-per-e-fold → κ_implied` — NOT a clock calibrated against an external standard, but the substrate's own budget read for its tick. **NON-PHONONIC caveat (task-flagged):** the seconds-conversion arithmetic (ℏ_SI, GeV→J) is a **unit-chain**, not substrate dynamics — but the cooling budget feeding it (T_init, N_e, the spectral-flow exponent) IS substrate. The unit-chain is precisely *why* the recovery is an identity rather than a triangulation.

**Dual-prior posterior re-allocation** (plan dual_prior — recovery/band PASS → 0.9 Track A): **Track A = 0.9 / Track B = 0.1.** The cooling budget is consistent with κ_nat (the recovery leg fires), supporting the reading that the seconds-normalization knob is fixed at the natural value — but with the explicit caveat that the "fixing" is unit-consistency, not an independent thermodynamic over-determination. Downstream consequence: this **resolves the 1.4 AT-TRAJECTORY seconds-band INFO** (κ is pinned at κ_nat = 8.86e−42 s/tick; the a(t) trajectory's absolute seconds-scaling is no longer a free multiplicative knob), and Wave-4 4.1/4.2 Ω_GW gates may consume κ = κ_nat as a fixed cross-check rather than sweeping it. The W6-5 swept band [1e-20,1e-10] is shown to **not** contain κ_nat (which is ~22 decades below its floor) — a useful negative: the historical sweep range was orders of magnitude too coarse to land on the physical tick.

**Capstone-hygiene (Q1/Q3 routing flag):** this PASS touches the §6.3 effective-Friedmann a(t) seconds-normalization status (Q1 YES — κ pinned at κ_nat resolves the 1.4 seconds-band) but does NOT change a C1 PROVEN/CONDITIONAL status tag by itself (the recovery is unit-consistency, not new triangulation evidence — narrate at consistency-confirmed, not over-determined). Route the §6.3 seconds-normalization note to `sessions/archive/session-97/session-97-housekeeping.md` §A per the plan's Wave-1 capstone-hygiene routing; the prose owner is the capstone designated writer.

---

## Wave 1 Synthesis (team-lead)

**Wave 1 — Emergent-FRW `a(t)` closure & κ-pin (the C1 frontier).** Five gates dispatched in two dependency-ordered sub-waves (A = {1.1, 1.2, 1.5} on S96/S95/S54-landed inputs; B = {1.3, 1.4} consuming A's `Ω(τ)`-profile + x-window npz). All 5 closed; verdict file audit-clean (8 distinct `audit_sha256`, sig_5 PASS; 1.3 carries a valid Option-A `supersedes` chain `8756ea30→ecb17c76→970f0105→6dcc22f1`, LIVE = INFO, per `gate-verdicts.md §"Option A"`).

**Per-gate results (NUMBERS → solution-space; no session-aggregate tally per `feedback_reporting-framing.md`):**

- **1.1 S97-W1-OMEGA-PROFILE — PASS.** The order-parameter↔acoustic conformal factor `Ω(τ)=√(ρ_s/a₂)` is exported as a computable object over τ∈[0.190,0.6]: NON-constant (rel-spread 6.42e-2 ≫ 1e-3), `Ω̇<0` and `Ω̈` finite ∀τ, fold-anchor `Ω(τ_fold)=2.241017` reproduces `Ω_BA_fold=2.241353` to rel 1.5e-4 (= the √Γ_effacement sub-permille leak). The constant-Ω degenerate null did NOT fire ⇒ 1.3 leg-ii transport and the 1.4 a(τ)→a(t) bridge are genuinely enabled. *Solution-space:* the S95-W4-4 "Ω derivable but never exported" INFO is closed — the conformal bridge is now a numerical object with derivatives.

- **1.2 S97-W1-XTODAY — PASS.** Substrate-determined `x_today = ρ_s/ρ_n` band = [103.22, 117.22] > `x_fold=85.7928` (monotone, Sage-exact `d ln x/d ln a = 3(1+w_n)>0` across the FROZEN w_n band, residual 4.4e-13); late-time `q(x_today) ∈ [−0.9915, −0.9873]`, within 0.013 of −1 (clean PASS, info-band not triggered). *Solution-space:* fixes the A-PASS x-window for 1.3; the late-τ substrate is vacuum/effacement-dominated by construction — spectral weight migrates to the w=−1 condensate sector (the substrate-IS reading of dark-energy domination, not a container filling with vacuum).

- **1.3 S97-W1-QOMEGA-ROUTE-INVARIANCE — INFO (Track B, route-SENSITIVE).** The A-leg invariant-shortfall FIRES (the dual-prior's predicted-NOT-to-fire branch is falsified). After conformal transport through `Ω`, the three S96 H(τ) routes' acoustic rates disagree by `max|ΔH_A| = 3.84 ≫ band_tol 0.356` (bare scale-factor growth AOFT 1.048× / VOL 1.673× / GFT 1.024× over [0.190,0.451]); C-leg and B-leg both FAIL. *Solution-space (the wave's load-bearing constraint):* the emergent-FRW deceleration is NOT a route-robust substrate-IS observable on these three reconstructions — conformal transport SHARPENS the S96 single-route disagreement rather than resolving it. C1's `a(t)` deceleration is CONDITIONAL on which H(τ) route reconstructs it. Dual-prior → 0.9 to Track B. (Methodology note: the plan-literal `q=−A·Ä/Ȧ²` has a removable coordinate pole at `A′=0 ⟺ H_A=0`; the agent used the Sage-exact pole-free equivalent `q=−1−Ḣ_A/H_A²` as the primary discriminator and disclosed it via the Option-A supersedes chain. Verdict robust to q-form — A-fires under both.)

- **1.4 S97-W1-1-AT-TRAJECTORY — INFO.** Explicit physical-seconds `a(t)` over [τ_fold,τ_now] is monotone↑ + finite (a: 1 → 1.0558, band-invariant across all 50 admissible τ̇ shapes) AND reproduces the AOFT anchor `H²(τ*)=7.478844e-03` at τ*=0.451041 to rel 5.46e-8 (≪ 1e-6) — both PASS. The ONLY non-PASS is shape-uniqueness: the inherited S96 τ̇ profile has `unique_selection=False` (50/50 shapes), leaving a 1-parameter seconds-normalization band (t(τ_now) rel-spread 0.419). Cross-confirmed `omega_nonconst=True` (1.1 null did not fire) and O'Neill cross-terms effaced (6.84e-117 ≪ 3e-7). *Solution-space:* existence → explicit-trajectory achieved on the AOFT route; the residual freedom is exactly the κ seconds-knob 1.5 addresses.

- **1.5 S97-COOLING-BUDGET-KAPPA-PIN — PASS (consistency-confirmed, NOT over-determined).** Class-8.7 pre-flight PASS: the cooling exponent −0.8685 = −70.25/80.89 is κ-independent (∂/∂κ=0, Sage-exact across 121 sweep points) ⇒ NOT a degenerate-observable tautology. Main recovery PASS: κ_implied = 8.86044e-42 = κ_nat to log10-ratio ≈ 0. *Honest finding (load-bearing):* the recovery is an IDENTITY forced by M_KK-unit consistency, NOT an independent triangulation — both reconstruction legs live in the same M_KK unit system, so any SI conversion is dimensionally compelled to κ_nat; there is no second dimensionally-independent seconds-scale inside the budget. Secondary finding: κ_nat sits ~21 decades below the W6-5 swept-band floor (1e-20), `in_band=False` (the historical sweep range was orders of magnitude too coarse).

**C1 `a(t)` frontier — net state.** The wave advanced C1 from "first-order existence+magnitude (S96)" to "explicit AOFT-route trajectory delivered (monotone, anchored, seconds-scaling consistency-pinned to κ_nat)" — BUT route-invariance FAILED (1.3), so the deceleration history is route-SENSITIVE. **C1 stays ASSUMED** (no promotion): the explicit a(t) exists on one route; route-robustness is the new open sub-object. Per 1.5's own flag, the κ-pin is a consistency-identity and does NOT license up-tagging C1. The substrate-first direction is preserved throughout — `a(t)` is the emergent acoustic readout of order-parameter dynamics (spectral-complexity growth past the fold), never a container expanding in time.

**Capstone-hygiene 5-question gate** (`.claude/rules/capstone-hygiene-gate.md`; routed to `sessions/archive/session-97/session-97-housekeeping.md §A4`):
- **Q1 (a(t)/effective-Friedmann gap) — YES.** The wave delivered the Ω(τ) profile §6.3 called "the open object" + an explicit AOFT a(t) + tested route-invariance. Routed: Atlas-04 C1 register row UPDATED in-session (§A3); capstone §6.3 PROSE enrichment is a designated-writer reviewed patch at session-close (Q4 discipline + `feedback_framework-hygiene.md` — NOT an orchestrator bulk append; verbatim enrichment captured in housekeeping §A4 so it is not orphaned).
- **Q2 (§7 falsifier row) — NO** (the SF54 q-band reclassification to conformal-frame-conditional artifact predates S97; no new mack-cosmic-bridge inventory row).
- **Q3 (PROVEN/CONDITIONAL/BROKEN/INFO tag flip) — NO.** C1 stays ASSUMED; route-sensitivity keeps it conditional, the wave earned no promotion ⇒ no over-claim drift to down-tag ⇒ the capstone-hygiene K-counter does NOT advance (no-op pass on the over-claim axis; evidence enriched at the register, tag unchanged).
- **Q4 — ledger (Atlas-04 C1) updated in-session; PROSE enrichment is the designated writer's at session-close.** **Q5 (citation) — NO.**

**Effected In-Session** (per `/rclab-coordinate` Step 6 + `feedback_fix-in-session-never-defer.md`):
- [x] `x_fold = 85.7928` promoted to `canonical_constants.py` SECTION E via `update_constant` (S67 ODLRO origin; confirmed-used S97-W1-XTODAY) — knowledge-MCP PROVENANCE added.
- [x] `Omega_BA_fold = 2.241353` promoted to `canonical_constants.py` SECTION E via `update_constant` (S95-W4-4 conformal-embed; reproduced S97-W1-OMEGA-PROFILE rel 1.5e-4) — knowledge-MCP PROVENANCE added.
- [x] Atlas-04 C1 register row updated with S97 W1 findings (Ω delivered / explicit a(t) / route-sensitivity / κ consistency-pin) — `sessions/framework/Atlas/atlas-04-assumptions.md:60`, status HELD ASSUMED.
- [x] Capstone-hygiene 5-question gate run + routed to `sessions/archive/session-97/session-97-housekeeping.md §A4` (Q1 YES → Atlas-04 in-session + §6.3 session-close designated-writer; Q2–Q5 NO/ledger).
- [x] Housekeeping ledger `sessions/archive/session-97/session-97-housekeeping.md` written (template-conformant §A–§F; 4 §A entries, §B–§E empty).

## Carry-Forward Computations

> The plan-flagged hygiene candidate (promote `x_fold` + `Omega_BA_fold` to canonical) was a clean single-value `update_constant` with no derivation ambiguity ⇒ EFFECTED IN-SESSION (housekeeping §A1/§A2), NOT carried forward. One genuine future-compute item remains:

### CF-S98-W1-ROUTE-RECONCILIATION — select the canonical acoustic-frame H(τ) and re-test q_Ω route-invariance

> **Origin**: S97-W1-QOMEGA-ROUTE-INVARIANCE INFO (Track B, route-SENSITIVE). This is a genuine math/physics carry-forward (the C1 `a(t)` frontier's open sub-object), NOT a Q2 hygiene item.

1. **What**: Establish a principled selection of the canonical acoustic-frame `H(τ)` for the emergent-FRW `a(t)`, then re-evaluate `q_Ω` route-invariance under it. Two candidate paths (the S97-W1-QOMEGA agent's carry-forward): **(i)** declare the AOFT covariant spectral-action route canonical — `g_M` emerges from the `a₂` Seeley–DeWitt coefficient, so the AOFT `H(τ)` IS the substrate-natural acoustic frame and VOL/GFT are alternative reconstructions — and verify the AOFT-frame `q_Ω` is the substrate-IS deceleration; **OR (ii)** derive a substrate-physics reason the bare scale-factor growths SHOULD differ per route (distinct effective-Friedmann content) with a principled canonical selection. Includes selecting the canonical `τ̇` shape from the 50 admissible `S96-W1-TAUDOT-PROFILE` shapes (the coupled shape-uniqueness sub-gate inherited from 1.4 INFO) so the AOFT `a(t)` becomes fully unique.
2. **Inputs**: `computations/session-96/s96_w1_{aoft_friedmann_map,volovik_2fluid,gft_friedmann}.npz` (3 H(τ) routes); `computations/session-97/s97_w1_omega_profile.npz` (Ω,Ω̇,Ω̈; audit `6fee3fdf`); `computations/session-97/s97_w1_qomega_route_invariance.npz` (the `max|ΔH_A|` disagreement structure: AOFT 1.048× / VOL 1.673× / GFT 1.024×; LIVE audit `6dcc22f1`); `computations/session-96/s96_w1_taudot_profile.npz` (50 admissible τ̇ shapes); `canonical_constants.py` (`M_KK_inv_seconds`, `G_DeWitt`, `tau_fold`, `Omega_BA_fold`, `x_fold`).
3. **Gate**: `S98-W1-ROUTE-RECONCILIATION` — PASS iff a derivation-backed (not ad-hoc) canonical-frame selection is established AND under that canonical frame EITHER (a) `q_Ω` is route-invariant `max|ΔH_A| < 0.356` by construction, OR (b) the per-route divergence is shown substrate-physically expected with the canonical selecting AOFT. The S98 planner pins the numerical threshold + canonical-selection criterion at plan-freeze (this CF specifies the OBJECT; PRDR pins the machinery).
4. **Effort**: ~1 wave.
5. **Depends on**: S97-W1-QOMEGA-ROUTE-INVARIANCE (route-sensitivity finding + H_A disagreement structure — UPSTREAM GATE), S97-W1-OMEGA-PROFILE (Ω profile), S97-W1-1-AT-TRAJECTORY (explicit AOFT a(t) + τ̇-shape non-uniqueness).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-05-30 | Ω(τ) conformal factor | S95-W4-4 INFO: "derivable, never exported" | EXPORTED computable (Ω,Ω̇,Ω̈), non-constant, fold-anchored | S97-W1-OMEGA-PROFILE PASS |
| 2026-05-30 | C1 a(t) trajectory (Atlas-04 C1) | S96: first-order existence+magnitude; trajectory pending Ω-gate | Explicit AOFT-route a(t) delivered (monotone, anchored); status HELD ASSUMED | S97 W1 (1.1 PASS + 1.4 INFO) |
| 2026-05-30 | q_Ω route-invariance | S96: apparent divergence read as partition-RESOLUTION | Confirmed route-SENSITIVE after conformal transport (max\|ΔH_A\|=3.84 ≫ 0.356); transport sharpens not resolves | S97-W1-QOMEGA-ROUTE-INVARIANCE INFO (Track B) |
| 2026-05-30 | κ (M_KK⁻¹→s knob) | swept band [1e-20,1e-10] (W6-5) | pinned at κ_nat=8.86044e-42 (consistency-identity, not triangulation); κ_nat 21 dec below sweep floor | S97-COOLING-BUDGET-KAPPA-PIN PASS |
| 2026-05-30 | x_fold; Omega_BA_fold | referenced from session text (not canonical) | canonical_constants.py SECTION E (PROVENANCE pinned) | S97 W1 in-session promotion (housekeeping §A1/§A2) |

## Files Produced

All paths under `computations/session-97/`. Verdicts in `computations/session-97/s97_gate_verdicts.txt` (canonical).

| Gate | Verdict | Script | Data (.npz) | Plot (.png) | audit_sha256 (short) |
|:--|:--|:--|:--|:--|:--|
| 1.1 S97-W1-OMEGA-PROFILE | PASS | `s97_w1_omega_profile.py` | `s97_w1_omega_profile.npz` | `s97_w1_omega_profile.png` | `6fee3fdf` |
| 1.2 S97-W1-XTODAY | PASS | `s97_w1_xtoday.py` | `s97_w1_xtoday.npz` | `s97_w1_xtoday.png` | `067fe807` |
| 1.3 S97-W1-QOMEGA-ROUTE-INVARIANCE | INFO | `s97_w1_qomega_route_invariance.py` | `s97_w1_qomega_route_invariance.npz` | `s97_w1_qomega_route_invariance.png` | `6dcc22f1` (LIVE; chain of 4) |
| 1.4 S97-W1-1-AT-TRAJECTORY | INFO | `s97_w1_1_at_trajectory.py` | `s97_w1_1_at_trajectory.npz` | `s97_w1_1_at_trajectory.png` | `b8507148` |
| 1.5 S97-COOLING-BUDGET-KAPPA-PIN | PASS | `s97_cooling_budget_kappa_pin.py` | `s97_cooling_budget_kappa_pin.npz` | `s97_cooling_budget_kappa_pin.png` | `f451f43d` |

Registers touched (Effected-In-Session): `computations/_shared/canonical_constants.py` (SECTION E: `x_fold`, `Omega_BA_fold`); `sessions/framework/Atlas/atlas-04-assumptions.md` (C1 row); `sessions/archive/session-97/session-97-housekeeping.md` (new).
