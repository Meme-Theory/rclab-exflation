# Investigation 5 Wave 1 — NCG Spectral-Action Joints (Results Working Paper)

**Investigation**: 5 | **Wave**: 1 | **Plan**: investigation-5-plan-w1.md | **Theme**: the joints where the spectral triple meets the Standard Model — Pati-Salam quadratic-fluctuation Higgs quartic, a₄ Weyl/trace-anomaly CC channel, Connes-distance lepton mass ladder, Tomita-Takesaki modular twist, von Neumann entropy-functional CC ratio.

**Track**: INVESTIGATION | **Verdict ledger**: `computations/investigation-5/inv5_gate_verdicts.txt` (emit via `emit_verdict(session=5, track="investigation", ...)` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`). All five gates are `gate_type: compute` → each emits a verdict line. INV5-W1-1/-2/-3/-5 carry a `[SIGN]` trigger (directional prediction → schema-v2 3-tuple companion row REQUIRED); INV5-W1-4 carries `[VERIFY-THEOREM]` (no 3-tuple). The five gates consume PROVEN/permanent on-disk machinery and dispatch in a single parallel batch (no within-wave prerequisites).

## Gate Sections

### §W1-1. INV5-W1-1-PS-QUADRATIC-FLUCTUATION-HIGGS-QUARTIC (connes-ncg-theorist)

**Status**: COMPLETED  
**Gate ID**: `INV5-W1-1-PS-QUADRATIC-FLUCTUATION-HIGGS-QUARTIC`  
**Trigger**: `[SIGN]`  
**Classification**: **PARTICLE** (the Higgs quartic + m_H are representation-theoretic content of D_K's inner fluctuations)  
**Gate type**: `compute`  
**Agent**: `connes-ncg-theorist`  
**Hypothesis**: with the order-one axiom VIOLATED at norm 4.000 and the quadratic inner fluctuations `A_quad = Σ c_ij[D_K,a_i][D_K,a_j]` RETAINED on the rank-4 Pati-Salam algebra, the a₄(D_A²) moment yields a Higgs quartic whose `m_H^PS = v_ew·sqrt(2λ)` reproduces the framework's 131.8 GeV within the eps_H functional band.  
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w1.md` §W1-1.

**Verdict**: **PASS** — composite PASS via the schema-v2 3-tuple (sign=PASS, magnitude=PASS, regime=VALID). `m_H^PS = 135.01 GeV`; `|m_H^PS − 131.8| = 3.21 GeV ≤ 6.7 GeV` (eps_H band; fractional 0.02434 ≤ 0.05083 tol). The Pati-Salam quadratic-fluctuation route — order-one VIOLATED, `A_quad` RETAINED — REPRODUCES the framework's 131.8 GeV inside the eps_H band. This **REPAIRS G-1/C-1**: the NCG-derived Higgs sector survives its own broken order-one axiom; the quadratic fluctuations reproduce the linear (Higgs-as-fluctuation) result (a +0.86 GeV upward nudge of the 134.15 tree value) rather than introducing spurious fields.

**Output Artifacts** (closure-verification checklist):
- (1) script `computations/investigation-5/inv5_w1_1_ps_quadratic_fluctuation_higgs_quartic.py` — `from canonical_constants import` ✓, `print_verdict_payload` ✓ (grep-verified).
- (2) data `computations/investigation-5/inv5_w1_1_ps_quadratic_fluctuation_higgs_quartic.npz` ✓ (exists).
- (3) plot `computations/investigation-5/inv5_w1_1_ps_quadratic_fluctuation_higgs_quartic.png` ✓ (exists).
- (4) verdict line `computations/investigation-5/inv5_gate_verdicts.txt` ✓ — canonical line matches `^INV5-W1-1-PS-QUADRATIC-FLUCTUATION-HIGGS-QUARTIC:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion + schema-v2 3-tuple + 2 extra rows present (emit_verdict, track=investigation, sig_5 unique).
- (5) this WP section ✓ — `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` present.
- 4-tuple: `(value=135.0075, scheme=CCS-2013-quadratic-fluctuation-PS, convention=RATIO, L_max=12)`.
- dual-SHA: `audit_sha256=687d9c9d48338736bd134f817a70fb89566a90a4d37c488d02fa54fe1aa44d46`; `content_sha256=094d1b8ce5f37758093e84b880c7f3da1ecfa674161233498586e5aed5afc2e4`.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `knowledge-index-usage.md`):
- `get_constant('m_H_FW_KK_threshold')` → **131.8** (S100a; KK-THRESHOLD-64). Target confirmed.
- `get_constant('a_4_FW_zeta')` → **1350.7216** (S75; baseline-findings-s66 a₄(fold)). YM+Higgs-quartic moment.
- `get_constant('a_2_FW_zeta')` → **2776.165389** (S88; S42 zeta sum + S46 a₂ split). EH moment.
- `get_constant('v_ew')` → **246.0** GeV (EW VEV, canonical line 2258).
- `get_constant('m_H_FW_tree')` → **134.0** (S100a; theorem A10 S62 Filter-Independence). Tree anchor.
- `get_constant('m_H_obs')` → **125.1** (ATLAS+CMS Run-1; exact-rational denom 67/1251, 89/1251).
- `get_constant('tau_fold')` → **0.19**; `get_constant('alpha_s_MZ_obs')` → **0.1180** (g_3(M_KK) input).
- `search_knowledge('S97-Q10-1-PS-CONDENSATE')` → gate **PASS**; `M4_forced_to_zero=True`, `abelian_only_EXTENDS=True`, `(15)-adjoint in ker(ι_*^PS)`, `nonabelian_M4_survives=False`. PS extension certified; npz `A_K_PS_summand_dims=[1,2,2,4]`.
- `search_knowledge('CCS-2013 quadratic fluctuations c_ij')` → `A_quad = Σ c_ij[D,a_i][D,a_j]` (Paper 23); order-one fails **4.000** (N3); **169 quadratic + 173 linear** directions (session-46-wave2); reduced to **2.100** after fluctuations (S100b W2, `order_one_closes=False`); limiting case (c): order-one satisfied ⇒ 169 quadratic vanish.
- `search_knowledge('lambda_h 4/3 g_3 a_4 a_2 A10')` → **A10 Filter-Independence** `λ_h = (4/3)g_3²(M_KK)·(a_4/a_2)`, cutoff-shape-INDEPENDENT; `m_H² = (8/3)(a_4/a_2)g_3²v²` (Paper 17 eq 4.8).
- `search_knowledge('g_3 unification')` + session-61/62/70 reads → **g_3(M_KK)=0.519** (SM RG from α_s(M_Z)=0.1180); **S70 RATIO-GILKEY-70 RESOLVED**: CCM formula uses `ratio_gilkey=0.4140` (pure-curvature, conv B), NOT cache-moment `a_4z/a_2z=0.4866` (zeta conv A). **Branch decision**: NOT pre-closed; the W1-1 quadratic-fluctuation λ-correction has never been computed.

**Results** (NUMBERS first):

| quantity | value | source / role |
|:---------|:------|:--------------|
| `ratio_gilkey` (CCM input) | 0.4140 | pure curvature ratio (Gilkey conv B); S70 RATIO-GILKEY-70 RESOLVED |
| `g_3(M_KK)` | 0.519 | SM RG from α_s(M_Z)=0.1180 (session-61 wave9) |
| `λ_h^tree` | 0.148687 | `(4/3)g_3²·ratio_gilkey` |
| `m_H^tree` | 134.15 GeV | `v_ew·sqrt(2λ_tree)` (= canonical m_H_FW_tree 134.0, to rounding) |
| order-one defect (bare → residual) | 4.000 → 2.100 | atlas-04 N3; S100b W2 (`order_one_closes=False`) |
| `defect_ratio` (surviving fraction) | 0.5250 | residual/bare = 2.100/4.000 |
| `‖A_quad‖/‖A_lin‖` | **0.1133** | CCS-2013 perturbative-validity ratio; **< 0.3 ⇒ regime VALID** |
| `δ_quad` (a₄ shift) | 0.01284 | `(‖A_quad‖/‖A_lin‖)²` (positive: |[D,a]|² adds to a₄ trace) |
| `λ_h^PS` | 0.150597 | `λ_tree·(1+δ_quad)` |
| **`m_H^PS`** | **135.01 GeV** | `v_ew·sqrt(2λ_PS)` (4 sig figs: 135.0) |
| `m_H^PS − 131.8` (magnitude) | **+3.21 GeV** | ≤ 6.7 band ⇒ magnitude PASS |
| `m_H^PS − 125.1` (SIGN) | **+9.91 GeV** | > 0 ⇒ sign PASS (positive residual) |
| spurious fields? | **No** | S97 abelian-only-EXTENDS, M₄ forced to zero ⇒ only the |S|² Higgs survives |
| (H,H) order-one block norm (GPU) | 2.100 | torch.linalg.eigvalsh on AMD RX 9070 XT (ROCm); gpu_used=True |
| cache-moment cross-check `a_4z/a_2z` | 0.4866 → m_H 145.4 | NOT the CCM input (atlas-row vs cache-moment orthogonality, substrate-first-sourcing §ii.A) |

**Substitution chain — SIGN read-off** (plan Step 5; numbers substituted):
`m_H^PS = v_ew·sqrt(2·λ_h^PS) = 246.0·sqrt(2·0.150597) = 135.01 GeV`. The tree value `246.0·sqrt(2·0.148687) = 134.15 GeV`; the quadratic fluctuation adds `δ_quad = (0.1133)² = +1.28%` to λ (the order-one violation's `A_quad` is a positive-definite `|[D_K,a]|²` contribution to the a₄ heat-kernel trace ⇒ it ENHANCES the quartic ⇒ pushes m_H UP). ⇒ `sign(m_H^PS − m_H_obs) = +`. Both tree AND PS-route predictions sit ABOVE the observed 125.1; the KK-threshold route lowers 134→131.8 while the PS quadratic route nudges 134.15→135.01 — both land inside the eps_H band of the substrate's KK-fiber transverse |S|² mode. SIGN PASS by construction; magnitude PASS (3.21 ≤ 6.7).

**Substrate-physics assessment** (PARTICLE): The Higgs IS the |S|² transverse oscillation of the SU(3)-fiber embedding — a representation-theoretic excitation of D_K, not a field in a container. The arrow: D_K eigenvalues → the inner fluctuation `D_A = D_K + A_lin + A_quad` (A_lin = the Higgs scalar, the off-diagonal `[D_K,b]` valued in the multiplicity bundle; A_quad = the quadratic term FORCED by the broken order-one axiom) → the a₄(D_A²) spectral moment → the Higgs quartic λ → m_H. The order-one violation at norm 4.000 (residual 2.100 after fluctuations) is **NOT a defect to patch but the substrate's own structure**: when `[[D_K,a],b] ≠ 0`, the substrate's differential calculus carries quadratic fluctuations. The decisive result is that these are **perturbatively controlled** (‖A_quad‖/‖A_lin‖ = 0.1133 ≪ 0.3) and **color-singlet** (S97: M₄ forced to zero by the inheritance morphism ι_PS, abelian-only-EXTENDS ⇒ no new colored scalars, only the |S|² Higgs survives). So the broken axiom does not break the Higgs sector — it perturbs the quartic by 1.3% and the spectral-action Higgs mass remains the substrate's intrinsic 131.8 ± 6.7 GeV prediction. The corridor "the framework's NCG Higgs is fragile to its own order-one violation" is **CLOSED**; the corridor "the NCG-derived Higgs is robust to the broken axiom" is **OPEN and now occupied** by a pre-registered PASS.

**Caveats / boundary** (honest scope): (i) the c_ij magnitude is FIXED by the order-one residual defect (no free knob), but the *mapping* from residual defect to ‖A_quad‖ uses an RMS spectral-amplitude bound (`defect_ratio·sqrt(n·λ_min²/Σλ²)`), not a full 169-direction diagonalization of A_quad — a Stage-2 refinement could diagonalize the explicit 169-direction quadratic module (session-46-wave2) and recompute δ_quad from the eigenvalue shift directly. (ii) the CCM tree uses `ratio_gilkey` per S70 RATIO-GILKEY-70; the cache-moment `a_4z/a_2z` route gives 145.4 GeV (outside the band) — the gate is correctly anchored to the RESOLVED convention. (iii) m_H_obs=125.1 is the Run-1 anchor (not PDG-2024 125.25); a re-pin (CF-S104-MH-OBS-REPIN) does not affect this gate's PASS (the target is the framework's own 131.8, not the obs value).

---

### §W1-2. INV5-W1-2-A4-WEYL-TRACE-ANOMALY-CC-CHANNEL (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W1-2-A4-WEYL-TRACE-ANOMALY-CC-CHANNEL`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the a₄ curvature-invariant decomposition is the fabric's spectral-geometry structure, not an excitation)
**Gate type**: `compute`
**Agent**: `connes-ncg-theorist`
**Hypothesis**: the substrate's a₄ moment decomposes into {Yang-Mills, Higgs-quartic, Weyl² C_{μνρσ}², Gauss-Bonnet}; the Weyl²+trace-anomaly sub-term is NON-monotone in τ (escaping the W4 monotonicity wall that closes a₀/a₂) and sources an anomaly-induced vacuum energy within OOM-striking-distance of ρ_Λ.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w1.md` §W1-2 (composite sign-test + OOM-distance set-membership, regulator pin `a_4^{ζ}`).

**Verdict**: **FAIL** — composite (sign=FAIL, magnitude=FAIL, regime=VALID). The Weyl²/trace-anomaly a₄ sub-term is **MONOTONE in τ** (0 sign changes in `d(Weyl²)/dτ` over [0.14, 0.24]) — it is therefore **ALSO covered by the W4 monotonicity wall**, and the OOM-distance of ρ_anomaly to ρ_Λ is **115.76** (far beyond the 60-OOM info ceiling). The last geometric NCG cosmological-constant channel is **CLOSED**.

**Output Artifacts** (closure-verification checklist; verified by content-presence regex, never by line count):
1. **Script** `computations/investigation-5/inv5_w1_2_a4_weyl_trace_anomaly_cc.py` — EXISTS; `grep -nE 'from canonical_constants import|print_verdict_payload'` → L80 `from canonical_constants import *`, L93 `from canonical_constants import (`, L378 `def print_verdict_payload(`, L488 `print_verdict_payload(composite, ...)`. PASS.
2. **Data** `computations/investigation-5/inv5_w1_2_a4_weyl_trace_anomaly_cc.npz` — EXISTS (arrays: `tau_grid, R, R2, Ric2, Riem2, weyl2, gauss_bonnet, I_geo, dWeyl2, dGB, sign_changes, non_monotone, a4_Weyl_zeta, rho_anomaly, oom_distance, …`). PASS.
3. **Plot** `computations/investigation-5/inv5_w1_2_a4_weyl_trace_anomaly_cc.png` — EXISTS (4-panel: invariants / Weyl²+GB / d(Weyl²)/dτ non-monotonicity test / OOM bar). PASS.
4. **Verdict line** `computations/investigation-5/inv5_gate_verdicts.txt` — `INV5-W1-2-A4-WEYL-TRACE-ANOMALY-CC-CHANNEL: FAIL -- value='weyl2_signchanges=0_non_monotone=0_OOM=115.7597_weylfrac=0.037748' … audit_sha256=2a6670454f4175a858b29c19a3d4c1e5969404d12b11df516d529f2849aef2fb content_sha256=92948ae0ec76e514fa5b7ec7a81a6d78ec4d61a56196b89672178ee60273881c schema_version=S84+` + dual-SHA companion row + schema-v2 3-tuple row (`sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`) + `regulator_pin=a_4^{ζ}` row (4 rows total, sig_5 unique, track=investigation). PASS.
5. **This WP section** — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. PASS.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script; query-first discipline):
- `search_knowledge('a4 Seeley-DeWitt Weyl Gauss-Bonnet decomposition trace anomaly cosmological constant')` → Penrose CCC `R_1 = a₀·a₄/a²` Gauss-Bonnet decomposition (PROVEN, s66); Mottola EFT "trace anomaly = a₄" (Birrell-Davies/Duff/Gilkey, PROVEN via lizzi); `spectral-geometer-layers.md §4` Seeley-DeWitt decomposition registry. The **Weyl²-specific** conformal sub-term was NOT previously isolated — NOT pre-closed.
- `search_knowledge('W4 monotonicity wall spectral action a_2k monotone S17a S37')` → Spectral Action Monotonicity W4 (PROVEN, S17a; `⟨λ²⟩(τ)` monotone, 9,600 checks); a_{2k} monotone k=0,1,2,3 (S24a); the load-bearing Eq. (4.12) `d/dτ⟨λ²⟩>0 ⇒ d/dτ a_{2k}` FIXED SIGN. W4 governs the **scalar-curvature-driven** moments — the Weyl² conformal complement is the open question.
- `get_constant('a_4_FW_zeta')` → **1350.7216** (S75; zeta-regulated 4th SDW moment; YM+Higgs-quartic). Used as the regulator-pinned `a_4^{ζ}` leg.
- `get_constant('rho_Lambda_obs')` → **2.7e-47 GeV⁴** (Planck 2018). The CC comparison anchor.
- `search_knowledge('a0 a2 C_Q R universality S65 …')` → DILUTION-CC (`CC_OOM = 115.5`, S66); `Lambda_cc = (2 f_0/f_2) a_0`. Confirms the canonical ~115-OOM scale.
- `search_knowledge('Riemann tensor 147 left-invariant Jensen metric SU(3) …')` → Riemann tensor 147/147 PROVEN at machine-eps (S20a, `r20a_riemann_tensor.py`); confirmed the `r20a_riemann_tensor.npz` is **absent from disk** → substrate-first analytic REBUILD from the left-invariant Jensen metric (E1) via the importable r20a module, per the plan §W1-2 note + `substrate-first-canonical-sourcing.md`.
- `trace_entity('Weyl trace anomaly a4 conformal cosmological constant channel')` → **no trace** — confirms the Weyl²-anomaly CC channel had NOT been computed. Gate is genuinely open; **NOT pre-closed**.

**Results**:

*Substrate-first recompute validation.* The full 8×8×8×8 Riemann tensor R_{abcd}(τ) was rebuilt from the analytic left-invariant Jensen metric `g_τ = 3·diag(e^{2τ} | e^{−2τ}×3 | e^{τ}×4)` (E1; `baptista-operator-dk-tau.md §2.1.2`) via the 147/147-verified r20a machinery (su3_generators → structure constants → Killing form B=3·𝟙 → jensen_metric → ON-frame → Koszul connection → Riemann). At every one of the 21 scan points the recompute matched the **Sage-derived exact closed forms** (this session) to **max deviation 8.882×10⁻¹⁶** (machine epsilon; tol 1e-9). Cross-checks: `R_K(0)=2.000000`, `R_K(0.190)=2.018144` (matches E3 `R−E3=0` exactly), `|Riem|²` = `kretschner_exact` exactly.

*The exact curvature-invariant closed forms (Sage QQbar, this session):*
- `R(τ) = −¼e^{−4τ} + 2e^{−τ} − ¼ + ½e^{2τ}` (= E3; `R − E3 = 0` symbolically exact)
- `|Ric|²(τ) = (1/24)(2e^{12τ}+3e^{8τ}−12e^{7τ}+26e^{6τ}+3e^{4τ}−12e^{3τ}+2)e^{−8τ}`
- `|Riem|²(τ) = (23/96)e^{−8τ}−e^{−5τ}+(5/16)e^{−4τ}+(11/6)e^{−2τ}−(3/2)e^{−τ}+17/32+(1/12)e^{4τ}`

*a₄ decomposition (Gilkey Eq. 4.8, `spectral-geometer-layers.md`), d=8:*
- **Yang-Mills** = the 60·F_{μν}F^{μν} piece. On the pure-curvature SU(3) fiber the gauge-kinetic part of a₄(K) vanishes at the Einstein point (S5); reported = 0 for the geometric fiber (the physical YM kinetic term lives in the M⁴×K matter-dressed reduction).
- **Higgs-quartic** = the |S|²-mode (matter-dressed) contribution; off the pure-geometry fiber, carried by the full-vs-geometric share of `a_4_FW_zeta`.
- **Weyl²** = C² = `|Riem|² − (4/(d−2))|Ric|² + (2/((d−1)(d−2)))R²` = `|Riem|² − ⅔|Ric|² + (1/21)R²`. At the fold: **Weyl²(0.190) = 0.385917**.
- **Gauss-Bonnet** = `|Riem|² − 4|Ric|² + R²`. At the fold: **GB(0.190) = 2.551961** (Euler/topological combination).
- Fold shares of the geometric a₄ integrand `I_geo = 5/2 R² − 2|Ric|² + 2|Riem|² = 10.223618`: **Weyl²/I_geo = 0.037748** (3.77%), GB/I_geo = 0.249614 (24.96%). The sub-terms separate cleanly (no L_max regulator-sensitivity in the analytic curvature route — they are exact geometric integrals), so the INFO-branch (non-separation) does NOT trigger.

*(a) Non-monotonicity test — the decisive result.* `d(Weyl²)/dτ` over the pre-registered 21-point window [0.14, 0.24] (step 0.005): range **[+0.2133, +0.3482]**, strictly positive — **0 sign changes** (float floor 1e-9). The Weyl² conformal sub-term is **MONOTONE-increasing** across the entire fold window. Gauss-Bonnet: also 0 sign changes (monotone).

*The structural reason (exact, Sage):* the **unique stationary point** of Weyl²(τ) on the whole Jensen ray is **τ=0** (`Weyl²'(0)=0`, `Weyl²''(0)=+2.5 > 0` → a MINIMUM; `Weyl²(0)=5/14≈0.357143 < Weyl²(0.190)=0.385917`). The nontrivial factor of `d(Weyl²)/dτ` has NO positive real roots, so for all τ>0 the derivative is strictly positive and growing (0.0025 at τ=0.001 → 8.85 at τ=1.0). This is **the identical structure that E3/W4 exhibits**: the round bi-invariant point is the sole critical point, and the volume-preserving Jensen deformation increases curvature monotonically away from it. The hypothesis "the anisotropy can rise then fall at fixed volume" is **FALSIFIED** — the conformal anisotropy of the Jensen-deformed fiber rises monotonically; it does NOT turn over in the physical window (nor anywhere on τ>0).

*Substitution-chain Step-5 SIGN read-off:* the chain pre-registered "PASS if sign(d a₄^Weyl/dτ) is NOT constant across the 21-point scan." The computed sign IS constant (always +). Predicted direction (non-constant / sign-change present) does NOT match computed (constant +) ⇒ **sign_verdict = FAIL**.

*(b) OOM-distance.* The zeta-scaled Weyl-anomaly a₄ sub-term `a₄^Weyl = (Weyl²/I_geo)|_fold · a_4_FW_zeta = 0.037748 × 1350.7216 = 50.9865`. The spectral-action Λ⁰ term carries no Λ-power, so its dimensionful vacuum-energy density is set by `ρ_anomaly = f_0 · a₄^Weyl · M_KK⁴` with `f_0 ~ O(1)` and `M_KK_gravity = 7.42866×10¹⁶ GeV`: `ρ_anomaly = 1.5527×10⁶⁹ GeV⁴`. Against `ρ_Λ = 2.7×10⁻⁴⁷ GeV⁴`: **|log₁₀(ρ_anomaly/ρ_Λ)| = 115.76** (dimensionless cross-report a₄^Weyl vs Λ_obs/M_Pl⁴: 123.25). This reproduces the canonical CC gap (`CC_OOM = 115.5`, DILUTION-CC). **magnitude_verdict = FAIL** (115.76 ≫ 60-OOM info ceiling — cosmologically irrelevant magnitude even had it been non-monotone).

*4-tuple:* `(value='weyl2_signchanges=0_non_monotone=0_OOM=115.7597_weylfrac=0.037748', scheme=Gilkey-a4-Weyl-GaussBonnet-decomposition, convention=ABSOLUTE, L_max=12)`; `regulator_pin=a_4^{ζ}` companion row (spectral-sum a₄ leg = `a_4_FW_zeta`; curvature-invariant leg regulator-free Gilkey). Dual-SHA: `audit=2a6670454f4175a8…` (over [script, canonical, pinmap]), `content=92948ae0ec76e514…` (over [script]). Schema-v2 3-tuple: `sign=FAIL magnitude=FAIL regime=VALID` (regime VALID: analytic curvature invariants exact, recompute matches analytic to 8.9e-16, no regime breakdown).

**Substrate-physics / solution-space interpretation** (substrate-first): The a₄ moment IS the fabric's fourth spectral moment, and the Weyl² piece is the conformally-invariant (scale-free) part of the substrate's own curvature anisotropy — `D_K eigenvalues → a₄ moment → {YM, Higgs-quartic, Weyl², Gauss-Bonnet} → anomaly vacuum energy → ρ_Λ`. The hypothesis was that this scale-free anisotropy escapes the W4 monotonicity wall (which acts on the volume/scalar-curvature moments a₀/a₂ via `d/dτ⟨λ²⟩>0`). It does NOT: the Weyl² anisotropy of the Jensen-deformed SU(3) fiber rises monotonically away from the round genesis point (τ=0), exactly as the scalar curvature does, with no turning point on the physical ray. **This closes the LAST geometric NCG CC channel.** Together with S65 (a₀, a₂, a₃ all monotone/frozen) the picture is now complete at the GEOMETRIC layer: **every geometric a_{2k} sub-term — including the a₄ conformal anomaly — is monotone in τ, so the cosmological constant has NO geometric escape within NCG.** This is a constraint, not a defect: it sharpens the framework's own conclusion (recorded in MEMORY: "ALL geometric SA routes CLOSED; the problem is FUNCTIONAL not GEOMETRIC; a₀/a₂ = C_Q/R universal") by extending it from the volume/scalar moments to the conformal/anisotropic moment. The surviving CC leverage is the **functional** channel — the non-monotone von Neumann **entropy** functional `S_vN = Tr f_S(D²/β²)` of INV5-W1-5 (CCvS-2019), which is the only physically-motivated escape S65 flagged but never computed. The geometric door is now provably shut; W1-5 tests the functional door.

---

### §W1-3. INV5-W1-3-CONNES-DISTANCE-LEPTON-MASS-LADDER (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W1-3-CONNES-DISTANCE-LEPTON-MASS-LADDER`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (the per-state Connes distances ARE the fermion-generation quantum-number content, the ε_LX realization)
**Gate type**: `compute`
**Agent**: `connes-ncg-theorist`
**Hypothesis**: the per-state Connes distances `d_i` on the commutative ℂ^N multiplicity-bundle channel algebra (regulator-free) build a generation-resolving mass ladder `mass_i ~ exp(-d_i/ℓ)` whose charged-lepton spacing ratio `(d_e−d_μ)/(d_μ−d_τ)` reproduces 1.889 (the PDG log-mass-spacing ratio), NOT 1 (the flat Froggatt-Nielsen power-law null).
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w1.md` §W1-3 (ratio predicate + non-degeneracy, regulator-free commutative-channel restriction).

**Output Artifacts** (closure-verification checklist; on-disk + grep-verified):
- (1) script `computations/investigation-5/inv5_w1_3_connes_distance_lepton_mass_ladder.py` — present (48712 bytes); `grep -E 'from canonical_constants import'` → 2 hits (lines 166, 167); `grep -E 'print_verdict_payload'` → 3 hits (doc + def + call sites). PASS.
- (2) data `computations/investigation-5/inv5_w1_3_connes_distance_lepton_mass_ladder.npz` — present (22413 bytes). PASS.
- (3) plot `computations/investigation-5/inv5_w1_3_connes_distance_lepton_mass_ladder.png` — present (3-panel: distance ladder / two-route discriminator / mass-map fit). PASS.
- (4) verdict line in `computations/investigation-5/inv5_gate_verdicts.txt` — present; matches `^INV5-W1-3-CONNES-DISTANCE-LEPTON-MASS-LADDER:.* audit_sha256=[a-f0-9]{64}` (audit_sha256=`949edd1dfb89530086a65950eba192fad27ec3d66c548cc6a2f4eacd66372569`); dual-SHA companion row + schema-v2 3-tuple row (`sign=PASS magnitude=INFO regime=VALID`) both present (8 rows total via race-safe `emit_verdict`, sig_5 unique). PASS.
- (5) this WP section — `**Status**: COMPLETED`, `**Verdict**: INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. PASS.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; query-first discipline per `knowledge-index-usage.md`):
- `search_knowledge('Connes distance formula multiplicity bundle subalgebra restriction regulator-free')` → S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE **PASS** (`d_C_L10 = d_C_L12 = 2.386138`, `ratio_12_over_10 = 1.000000`, ECOS/CLARABEL-SDP, regulator-free); plus the S46/S87/S88/S100a/S101 Connes-distance lineage.
- `search_knowledge('generation blindness multiplicity scalar VII.BL lepton mass ladder ε_LX')` → §VII.BL Generation-Blindness Obstruction **STAGE-3-PERMANENT** (S99 W3-1; `R_cross = 1.019704`, `n_distinct = 2`): D_K left-invariant ⇒ multiplicity-scalar ⇒ ε_LX MUST be an external non-left-invariant deformation, outside every A_K-bimodule.
- `trace_entity('S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION')` → the regulator-free A_F-restricted diameter `d_C = 2.386138`; npz on disk (cross-checked in-script, match=True).
- `trace_entity('connes_distance_ladder')` + `search_knowledge('S100a W2-4 ... greybody distance')` → **S100a-CONNES-DISTANCE-LADDER (STAGE-3)** already computed the **substrate-FORWARD** greybody distances on the SAME L12 cache: `d=(0.6987,0.7621,1.5582)` (τ,μ,e), `W_Connes = 12.5629` OUTSIDE [1.8,1.89] → INFO, sign PASS, regulator-invariant. Verdict line `5e24db72e3e5121b...`.
- `get_constant('m_tau_PDG')` → `1.77686` GeV (PDG pole mass; the value the S100a band edge 1.8894 was computed from). `list_constants('m_(e|mu|tau).*')` → `m_e = 5.10998950e-4`, `m_mu = 0.1056583745`, `m_tau = 2.062` (S42 MODULUS mass, M_KK units — name collision, NEVER a PDG target; use `m_tau_PDG`).
- **PRE-CLOSED branch (NOT taken)**: this gate is structurally DISTINCT from S100a on the **bridge-map axis** — it adds the Martinetti-Wulkenhaar two-route discriminator (substrate-forward greybody vs inverse-Yukawa ansatz) and is on the separate investigation-track ledger. NOT a re-run; it EXPOSES the 1.889 as a tautology of the ansatz, contrasted against the substrate's own 12.56. Proceeded to compute.
- **PDG ratio cross-check**: `(ln m_μ − ln m_e)/(ln m_τ − ln m_μ)` with canonical masses = **1.889035502**; plan pre-reg target 1.889035511558237 (computed from m_μ = …755) — diff 9.7e-9 (last-digit m_μ), ≪ tol 0.05.

**Verdict**: **INFO** — composite (schema-v2 collapse). 3-tuple: **sign=PASS, magnitude=INFO, regime=VALID**.

The substrate-forward per-state Connes distances are **generation-resolving and widen** (sign PASS), but the substrate's OWN widening ratio is **12.56, NOT the PDG 1.889** (magnitude INFO — correct qualitative direction, ≠ Froggatt-Nielsen null = 1, but far outside the ±0.05 band). The pre-registered 1.889 is recovered ONLY by the Martinetti-Wulkenhaar inverse-Yukawa ansatz, which is a **tautology** (ℓ cancels; the masses are the input). All NCG-axiomatic side conditions PASS (regime VALID).

**Results**:

*Two-route discriminator (the gate's content). The gate computes BOTH readings of "the Connes-distance lepton ladder" and prints both so the wrong one cannot regenerate as a substrate claim:*

| Route | Definition | spacing ratio `(d_e−d_μ)/(d_μ−d_τ)` | reading |
|:------|:-----------|:------------------------------------|:--------|
| **A — substrate-FORWARD** | greybody star `t_g = 1/ω_g`, `ω_g = λ_g(τ_fold)²`; `d(v,g) = ω_g` (star closed form) | **12.562884** | the substrate's OWN distance geometry; the framework's PREDICTION |
| **B — inverse-Yukawa ansatz** (Martinetti-Wulkenhaar) | `mass_i ~ exp(−d_i/ℓ)` ⇒ `d_i = −ℓ·ln m_i` | **1.889036** | TAUTOLOGY — ℓ cancels, ratio = PDG log-mass-spacing by DEFINITION |

- **Route A per-state distances** (regulator-free commutative ℂ⁴ channel algebra, CLARABEL-SDP): `d_τ = 0.698718`, `d_μ = 0.762085`, `d_e = 1.558163` (λ²-units); assignment e=(3,0)/μ=(1,1)/τ=(1,0) (most distant = lightest = electron, via `mass = e^{−d/ℓ}`). **Non-degenerate** (rel spread 0.5516 ≫ floor 1e-6), strict ladder. Ladder gaps `Δ_1(e−μ) = 0.796078`, `Δ_2(μ−τ) = 0.063367` → `ratio_A = 12.562884`.
- **Route A ratio vs band**: `|ratio_A − 1.889036| = 10.674` ≫ tol 0.05 → OUTSIDE [1.889±0.05]. The Jensen fold COMPRESSES the (1,0)/(1,1) floors (`Δ_2 = 0.063367` vs Casimir-ideal ~5/3 scaling) ⇒ widening inflated **6.98×** above the Casimir value 9/5 = 1.800. The substrate distances are **Casimir-graded**, not log-mass-graded.
- **FN-discrimination**: `ratio_A = 12.563 ≠ 1` (FN null) → True, and `> 1` (widens) → True. So the substrate ladder is NOT a flat Froggatt-Nielsen power law (which gives equal log-spacings, ratio = 1). The qualitative B-4 signature (widening, ≠ FN) HOLDS; the precise PDG ratio does NOT.
- **Route B**: `ln(m_μ/m_e) = 5.331599`, `ln(m_τ/m_μ) = 2.822392` → `ratio_B = 1.889035502` = PDG ratio (canonical masses; plan target 1.889035511558, diff 9.7e-9 from the m_μ last digit). This matches 1.889 by construction; it is NOT a substrate prediction.
- **Substitution-chain Step-5 SIGN read-off (substituted numbers)**: Route A `d_e = 1.5582 > d_μ = 0.7621 > d_τ = 0.6987` ⇒ `sign(d_e − d_heavy) = +` (e most distant) ⇒ `mass = e^{−d/ℓ}` gives `m_e < m_μ < m_τ`, log-spacings WIDEN (`ratio_A = 12.56 > 1 ≠` FN's 1). The widening DIRECTION is correct; the MAGNITUDE (12.56) overshoots the PDG 1.889.
- **ℓ-calibration (Route-B fit, diagnostic)**: centered OLS of `ln m^PDG` on `d_i` → `ℓ = 0.120408`, `R² = 0.9228`; Route-A spread `(d_max−d_min)/ℓ = 7.138` e-folds (PDG target 8.154).
- **Expected 4-tuple**: `(value = ratio_A = 12.562884, scheme = Connes-distance-commutative-multiplicity-bundle-channel-CN, convention = RATIO, L_max = 12)`.
- **Regulator-free / NCG-axiomatic checks (regime VALID)**: SDP-vs-closed-form max rel dev `1.9e-9`; R-sweep regulator-invariance dev `1.8e-9` (the commutative-channel restriction CURES the S87 full-`M_n(ℂ)` CLASS-γ divergence); doubling-invariance dev `1.8e-9`; **KO-dim-6**: `J² = +1` (0.0e+00), `[J,D_F] = 0` (1.6e-15, BDI conjugate-floor equality 1.2e-15), `Jγ = −γJ` (0.0e+00), `γD_F = −D_Fγ` (0.0e+00); **first-order residual 2.0450 REPORTED** (the standing §VII.BL multiplicity-bundle obstruction — a generation-resolving D_F lies outside every A_K-bimodule). S88 `d_C = 2.386138` cross-check match = True.
- **dual-SHA**: audit over [script, canonical, pinmap] = `949edd1dfb89530086a65950eba192fad27ec3d66c548cc6a2f4eacd66372569`; content over [script] = `10e6622d1efc1f627dc4f4de4476f573281025340ccfa2d08a08e17322d0e48d`. **schema-v2 3-tuple** companion row present (`sign=PASS magnitude=INFO regime=VALID`).
- **Solver note** (`substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift): plan named "ECOS-SDP"; ECOS is not installed in the venv (CLARABEL, SCS only). Operational solver = CLARABEL (the race-proven S100a IKM-SDP solver); distance is a SUP over a compact set ⇒ solver-invariant (SDP-vs-closed dev 1.9e-9 witnesses solver-independence). Methodology-floor solver choice, NOT a physics change.
- **CROSS-TRACK note**: any `falsifier-master-inventory.md` row is a session-promotion task and `mack-cosmic-bridge`'s sole-writer domain, NOT this gate. Investigation-track verdicts are not swept into the knowledge index until promoted into a session (`gate-verdicts.md §"Track-local boundary"`).

**Substrate-physics reading (PARTICLE).** The fermion generations ARE the multiplicity index of D_K's Peter-Weyl decomposition (Z₃-triality `t = (p−q) mod 3`; §VII.BL). The arrow: D_K eigenvalues → the commutative multiplicity-bundle channel algebra ℂ^N → the per-state Connes distance `d_i = sup{|φ_i(a)−φ_0(a)| : ‖[D_K,a]‖≤1}` (the metric the Dirac operator induces on its own generation-states) → the mass ladder `mass_i ~ exp(−d_i/ℓ)`. The Connes distance is NOT a distance IN a pre-existing space; it IS the metric structure D_K puts on its own generation-channels — the substrate measuring the separation between its own excitation channels. §VII.BL (STAGE-3-PERMANENT) proved the hierarchy is not built by any A_K-inner form; this gate tested whether it IS built by the substrate's INTRINSIC distance geometry. **Finding**: the substrate's own distance geometry is generation-resolving and widens (it is NOT flat / not Froggatt-Nielsen), but it predicts a widening of 12.56, not the observed 1.889 — the distances are graded by the SU(3) Casimir / Jensen-deformed floor, not by the log-masses. The PDG-matching 1.889 lives only in the inverse-Yukawa ansatz `d_i = −ℓ·ln m_i`, which is fed the masses (a tautology). **Constraint-map update**: the B-4 corridor "the §VII.BL ε_LX IS the substrate's own Connes-distance ladder" is constrained — the qualitative widening signature (≠ FN) survives, but the substrate-forward Connes distance does NOT reproduce the precise lepton spacing; the precise hierarchy requires a non-greybody reweighting (a different `d_i` ↔ mass map, or the external non-LI ε_LX of §VII.BL acting OUTSIDE the intrinsic metric). This CONFIRMS §VII.BL's reframe (the hierarchy is not in the bare/intrinsic spectral data) and sharpens it: even the substrate's intrinsic METRIC (one step beyond the bare spectrum) is Casimir-graded, not mass-graded. Consistent with the S100a-CONNES-DISTANCE-LADDER precedent (same cache, same machinery, W reproduced bit-for-bit).

---

### §W1-4. INV5-W1-4-MODULAR-TWIST-MULTIPLICITY-NONSCALAR (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W1-4-MODULAR-TWIST-MULTIPLICITY-NONSCALAR`
**Trigger**: `[VERIFY-THEOREM]` (structural set-membership; NO `[SIGN]` 3-tuple)
**Classification**: **GEOMETRIC** (the modular automorphism of the crossed-product algebra is a structural property of the spectral triple's Type-III von Neumann structure)
**Gate type**: `compute`
**Agent**: `connes-ncg-theorist`
**Hypothesis**: the Tomita-Takesaki modular automorphism `σ^ω = Ad(Δ_ω^{it})` of the §VII.BZ crossed product `A_K ⋊ ℝ` acts as a multiplicity-NON-scalar twist on the Peter-Weyl blocks (`[D_K,a]_σ` not ∝ identity on each ℂ^{m(p,q)}), EVADING the Skolem-Noether no-go that kills every ordinary block-inner twist — so the generation hierarchy ε_LX can be intra-substrate.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w1.md` §W1-4 (off-scalar residual set-membership vs `1e-6` floor; explicit ordinary-twist contrast printed in-artifact).

**Verdict**: **FAIL** (set_membership = **SCALAR**) — the Tomita-Takesaki modular twist `σ^ω` is multiplicity-SCALAR on every Peter-Weyl block; the Skolem-Noether no-go SURVIVES; `ε_LX` is **NOT** intra-substrate via the modular twist.

**MCP Pre-Compute Audit** (queries executed BEFORE authoring the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge('Skolem-Noether multiplicity-blindness no-go generation-blindness epsilon_LX')` → **[theorem] §VII.BL Generation-Blindness Obstruction** STAGE-3-PERMANENT (S99 W3-1; Stage-2 PASS-AND audit `0f0c4f65`; `R_cross=1.019704`, `n_distinct=2`): *"The twisted escape is dead by Skolem–Noether. `A_K = ℂ⊕ℍ⊕M₃(ℂ)` has three non-isomorphic simple summands, so every `σ ∈ Aut(A_K)` is block-inner ⇒ multiplicity-scalar."*
- `search_knowledge('VII.BZ BDI Horizon-Faithfulness crossed product Type-III modular Tomita-Takesaki')` → **[theorem] K12 (S105) §VII.BZ BDI Horizon-Faithfulness Protection** STAGE-3-PERMANENT (S105-S106; blind Stage-2 PASS-AND): faithful normal modular weight `ω|_{A_hor}` on `A_hor = A_K ⋊_{σ^ω} ℝ`, protected by BDI/N₃=0; modular flow `Ad(Δ_ω^{it})`; Type-II_∞.
- `query_entity(theorems, 'VII.BL Generation-Blindness')` → `proven_1098` PROVEN; the statement scopes the no-go to **`σ ∈ Aut(A_K)`**.
- `trace_entity('generation-blindness multiplicity-scalar')` / `trace_entity('modular automorphism crossed product')` → no direct stored constant (the crossed-product modular flow is *constructed*, not a stored entity).
- `get_constant('tau_fold')` → 0.19 (S12/S42; CONST-FREEZE-42).
- Reading of the §VII.BZ landing script `computations/session-105/s105_w2_1_bdi_horizon_faithfulness_stage1_landing.py` (lines 342-393): the §VII.BZ STAGE-3 theorem states the faithful-normal weight's modular generator is the **closed form `K_a = log[(1−f_a)/f_a]`** built from the GGE relic occupations `{f_a}`, and (line 344) *"the modular flow **respects the Peter-Weyl block structure**"*; `{β_a} ⟺ ω faithful ⟺ modular generator exists ⟺ modular flow respects the Peter-Weyl blocks`.
- **PRE-CLOSED? NO.** §VII.BL closes the ORDINARY-twist channel (`σ ∈ Aut(A_K)` block-inner ⇒ scalar). THIS gate's object is structurally DIFFERENT: `σ^ω` is the modular automorphism of the **crossed product** `A_K ⋊ ℝ`; it is **not** an inner automorphism of `A_K` (a Type-II_∞/Type-III modular group has no inner implementation inside `A_K`), so the §VII.BL hypothesis (`σ ∈ Aut(A_K)`) does not cover it. The escape-hatch was genuinely open at compute time — this gate tests it.

**Results**:

Numbers (L12 cache, 90 Peter-Weyl blocks; multiplicity `m(p,q) = dim` of the irrep, max `m=343`; ℂ¹⁶ SM fiber; off-scalar floor `1e-6`, FD exact-zero floor `1e-12`; scale anchor L12 BdG `λ_min = 0.8197411121`):

| quantity | value | reading |
|:---------|:------|:--------|
| **PRIMARY** `max_(p,q) ‖PT[σ^ω(a)−a]_{ℂ^m} − scalar‖` | **0.000000e+00** (0/90 blocks NON-scalar) | modular twist is **multiplicity-SCALAR** (`≤ 1e-12` exact-zero) |
| `Δ_ω^{it}` block-scalarity witness | 4.577567e-16 | `Δ_ω^{it}` is a scalar phase on each ℂ^m (machine zero) |
| modular generator `k_rep = log[(1−0.3)/0.3]` | 0.847298 (**≠ 0**) | result driven by BLOCK-CONSTANCY, not a `k=0` accident |
| **ORDINARY** block-inner twist `max ‖PT[σ_u(a)−a]−scalar‖` | 9.880002e-32 (0/90) | Skolem-Noether contrast: also **SCALAR** |
| `modular == ordinary` (both `≤ 1e-12`) | **True** | the two twists agree: both multiplicity-scalar |
| **TEST-POWER control** (resolving `K=diag(k_i)` on a GENERIC non-mult-blind probe) | **5.189184e+01** (89/90 NON-scalar) | the off-scalar test **HAS discriminating power** |
| same resolving generator on PHYSICAL mult-blind `a=1_m⊗a_f` | 0.000000e+00 | **double failure** of the physical case |
| structured fast-path vs dense `n×n` cross-check (m≤6) | 8.882e-16 | fast-path is exact |
| **DIAGNOSTIC** bare commutator `max ‖PT[[D_K,a]]−scalar‖` | 3.008695e-01 | NON-zero for a TRIVIAL reason (see below); NOT a twist effect |

**Substitution-chain Step-5 read-off** (the `[VERIFY-THEOREM]` structural verdict): `PASS ⇔ max off_scalar > 1e-6` (NON-scalar; no-go evaded). Computed `max off_scalar = 0.000000e+00 ≤ 1e-6` ⇒ **NON-scalar set-membership FALSE** ⇒ **SCALAR** ⇒ **no-go SURVIVES** ⇒ **FAIL**. The 4-tuple is `(value = 0.000000e+00, scheme = Tomita-Takesaki-modular-twist-on-crossed-product, convention = ABSOLUTE, L_max = 12)`.

**Structural derivation** (why FAIL is the *correct* and rigorous outcome, Sage-verified): the §VII.BZ modular generator `K_a = log[(1−f_a)/f_a]` is built from the GGE relic occupations `f_a`, which are **sector labels** — constant within each Peter-Weyl block. Hence `K|_block = k_rep·1_n` is BLOCK-CONSTANT, so `Δ_ω^{it}|_block = e^{−i t k_rep}·1_n` is a **scalar phase** on the entire block. Conjugation by a scalar phase is the identity: `σ^ω(a) = Δ^{it} a Δ^{−it} = a` EXACTLY, for any algebra element `a` and any `k_rep`. Sage MCP confirmed the algebra exactly: for a block-constant `K`, `σ^ω(A) − A = 0` (zero matrix); only a multiplicity-RESOLVING `K = diag(k₁,k₂)` with `k₁ ≠ k₂` produces a non-zero off-diagonal twist `∝ (e^{−it(k₁−k₂)} − 1)`. The §VII.BZ generator is not of that form. This instantiates, at the operator level, the §VII.BZ landing-script statement (line 344) that *"the modular flow respects the Peter-Weyl block structure."*

**Both-readings contrast** (printed in-artifact so the wrong reading cannot regenerate, per `regulator-pin-discipline.md` §"Channel-Scope" / "contrast-inside-the-output"): (i) the MODULAR twist action (PRIMARY observable) is exact-zero; (ii) the ORDINARY block-inner twist (Skolem-Noether) is exact-zero; (iii) `modular == ordinary = True`. The DIAGNOSTIC bare-commutator off-scalar `‖PT[[D_K,a]]−scalar‖ = 0.3009` is NON-zero **for a trivial reason** — `D_K`'s eigenvalues differ across the multiplicity index even though `a = 1_m ⊗ a_fiber` is multiplicity-blind — and since `σ^ω(a) = a`, the twisted commutator `[D_K,a]_σ` EQUALS the ordinary commutator `[D_K,a]`: it is NOT a twist effect. (A v1 implementation that read this contaminated bare-commutator residual as the gate observable would have mis-reported INFO/PARTIAL-NON-SCALAR; that trap is closed by isolating the modular twist's OWN action `σ^ω(a)−a` as the PRIMARY observable.) The TEST-POWER control proves the off-scalar set-membership test is NOT a dead probe: a hypothetical multiplicity-RESOLVING generator on a generic probe returns `5.19e+01` (NON-scalar, 89/90 blocks); the physical case fails doubly — `a` is multiplicity-blind AND `K` is block-constant.

**Solution-space implication** (FAIL = a closed corridor, per `math-scripts.md` §"All Results Are Good Results"): the §VII.BZ Type-II_∞/Type-III₁ modular flow `σ^ω` — although genuinely NON-inner in `A_K` and hence outside the §VII.BL `Aut(A_K)` hypothesis — does NOT supply a multiplicity-resolving twist. The B-1 corridor closes: `ε_LX` is **not** intra-substrate via the modular twist; the generation hierarchy genuinely requires an external (non-left-invariant) ingredient. This STRENGTHENS §VII.BL: even the most exotic intra-substrate twist (the substrate's own intrinsic time-flow, the KMS dynamics of its horizon-faithful crossed product) cannot carry a generation index, because the faithfulness-fixing modular weight is sector-labelled rather than multiplicity-resolving. The surviving channels for `ε_LX` (per §VII.BL + the §W1-3 Connes-distance probe) are external non-LI deformations, not intra-`A_K` twists nor crossed-product modular flows.

**Substrate framing** (GEOMETRIC): the crossed product `A_K ⋊ ℝ` IS the substrate's horizon-faithful algebra (§VII.BZ); its Tomita-Takesaki modular flow `σ^ω = Ad(Δ_ω^{it})` IS the substrate's own intrinsic time-evolution (the KMS dynamics of its Type-II_∞ structure). The arrow runs `D_K eigenvalues + frozen faithful-normal weight ω → modular operator Δ_ω → modular automorphism σ^ω → twisted commutator [D_K,a]_σ → whether the substrate's own time-flow carries a generation index`. The modular twist is NOT a deformation imposed ON the substrate — it IS the substrate's intrinsic modular dynamics; and that dynamics, being sector-labelled, respects the generation degeneracy rather than lifting it. The explanation runs substrate → modular dynamics → generation structure, never the reverse.

**Output Artifacts** (closure-verification; content-presence grep, never line-count):
- (1) script `computations/investigation-5/inv5_w1_4_modular_twist_multiplicity_nonscalar.py` — contains `from canonical_constants import`, `print_verdict_payload` ✓
- (2) data `computations/investigation-5/inv5_w1_4_modular_twist_multiplicity_nonscalar.npz` ✓ (verdict=FAIL, set_membership=SCALAR, all keys incl. `max_off_scalar_resolving_control`, `structured_vs_dense_max_dev`)
- (3) plot `computations/investigation-5/inv5_w1_4_modular_twist_multiplicity_nonscalar.png` ✓ (per-block modular/ordinary/resolving/diagnostic + largest-m bar comparison)
- (4) verdict line in `computations/investigation-5/inv5_gate_verdicts.txt` matching `^INV5-W1-4-MODULAR-TWIST-MULTIPLICITY-NONSCALAR:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row (NO 3-tuple row: `[VERIFY-THEOREM]`, not `[SIGN]`)
- audit_sha256 `a0b78f29a329736c2133782b1dfe5a01442d073166be5645a5c8c263afc10b31`; content_sha256 `8daed3ca76cf052b623e6070126d0b4f6effda01c9ab6ee830545b7c96c48f97`

---

### §W1-5. INV5-W1-5-ENTROPY-FUNCTIONAL-CC-A0-A2-RATIO (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W1-5-ENTROPY-FUNCTIONAL-CC-A0-A2-RATIO`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the a₀/a₂ ratio is the fabric's spectral-geometry CC moment; the entropy functional re-weights its moments)
**Gate type**: `compute`
**Agent**: `lizzi-spectral-functional-theorist` (spectral-FUNCTIONAL-SELECTION question — does the non-monotone f_S give a different moment ratio? connes-ncg-theorist co-derives the C_Q/R universality wall this gate probes)

**Verdict**: **PASS** — composite PASS (sign=PASS / magnitude=PASS / regime=VALID). `rel_diff(R1) = 121.51%` ≫ the `1%` PASS floor. **The von Neumann entropy functional BREAKS the S65 a₀/a₂ = C_Q/R universality AND the W4 monotonicity wall.** The surviving FUNCTIONAL CC channel is **LIVE**.

**Hypothesis**: under the von Neumann entropy spectral functional `S_vN = Tr f_S(D²/β²)` with the NON-monotone weight `f_S(λ) = λ·d/dλ ln(1+e^{−βλ})` (CCvS-2019), the ratio a₀/a₂ DIFFERS from the geometrically-frozen C_Q/R value the S65 theorem proved universal for all monotone functionals — breaking both the W4 monotonicity wall and the S65 a₀/a₂=C_Q/R universality. **CONFIRMED.**

**MCP Pre-Compute Audit** (queries run BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("von Neumann entropy spectral functional CCvS-2019 non-monotone a0/a2 universality")` → returns the plan's own `f_S(λ)=λ·d/dλ ln(1+e^{−βλ})` equation; my prior entropy work `s73a_entropy_fstar.py` (entropy_fstar) + `s73b_functional_select.py` (FUNCTIONAL-SELECT-67) used the entropy functional for **n_s**, NOT for a₀/a₂. The entropy-functional **a₀/a₂** ratio is **NOT pre-computed**.
- `search_knowledge("a0 a2 ratio C_Q R scalar curvature universality S65 monotonicity wall")` → `[theorem] "CC Ratio from Scalar Curvature Only — d(a_0/a_2)/ds = −(a_0/a_2)/R·dR/ds"` (baseline-findings-s66, atlas-07, S65 W1-B, **PERMANENT**, proven for MONOTONE f). Also `[gate] FOLD-CURVATURE-RATIO-67 FAIL` ("R_fold sign flips across functionals; variation 3466%; fold shape qualitatively scheme-dependent") — my own S67 functional-sensitivity result, directly supporting that the fold-curvature moment is heavily scheme-dependent. Plus `s25_einstein_results_verdict.txt`: `ratio_a0_a2(tau=0)=856.800`, `a_0 (count)=11424 (max_pq_sum=6)` — raw-count cross-check anchor.
- `trace_entity("entropy functional spectral action")` → `S_k = Tr_k(f_S(R_k/λ_k))` (per-sector KMS); `functional_select` provenance. No theorem/gate on entropy-functional **a₀/a₂**.
- `get_constant("a_0_FW_zeta")` → `6440.0` (S88, S88-A-N-FW-CANONICALIZATION, **non-superseded**; `= zeta_{D_K}(0) = Tr(1)` regularized count, CCM 2007 + S64).
- `get_constant("a_2_FW_zeta")` → `2776.165389` (S88, spectral-zeta sum a_2(spectral, S42), **non-superseded**).
- `get_constant("tau_fold")` → `0.19` (CONST-FREEZE-42, non-superseded). `get_constant("R_K_tau_fold")` → not a canonical entry; plan pins R_K(tau_fold)=2.0181 (baptista-operator-dk-tau.md Eq.2.6).
- **PRE-CLOSED?** NO. No closure covers the entropy-functional a₀/a₂ ratio. The S65 universality (MONOTONE f) and W4 monotonicity (MONOTONE f) are the WALLS this gate probes — the gate tests whether the NON-monotone f_S escapes them. Gate is open and dispatchable.

**Substitution chain** (per `math-scripts.md §"Double-Check Logic Before Compute"`; claim: "a₀/a₂ under the non-monotone entropy functional f_S DIFFERS from the geometrically-frozen C_Q/R"):
- **Step 1 (definitions)**: `f_S(λ) = λ·d/dλ ln(1+e^{−βλ})`. Sage-exact reduction: `f_S(λ) = −βλ/(e^{βλ}+1) = −(βλ)·n_F(βλ)` (Fermi-Dirac occupation; minus energy×occupation = the von Neumann information weight). S65: `a₀/a₂ = C_Q/R` universal for MONOTONE f. Canonical `a_0_FW_zeta=6440`, `a_2_FW_zeta=2776.165389`, `R_K(tau_fold)=2.0181`.
- **Step 2 (why the monotone-f proof does NOT extend to f_S)**: Sage series `f_S = −(1/2)λβ + (1/4)λ²β² + 0·β³ − (1/48)λ⁴β⁴ + O(β⁵)`. Hence **`f_S(0) = 0`** — the entropy weight VANISHES at the origin. A MONOTONE cutoff has `f(0)≠0`, so its a₀-analog is the bare regularized count `a₀ = zeta_D(0) = Tr(1)`. `f_S(0)=0` ⟹ the entropy functional reads NOTHING in the count channel. Also `|f_S|` is NON-monotone: rises from 0, peaks at `x* = βλ = 1.2784645…` (root of `(x−1)e^x=1`), decays to 0. The W4-monotone-f hypothesis FAILS for f_S ⟹ S65's universality derivation does not apply.
- **Step 3 (the entropy-functional moments)**: on the finite substrate, `S_vN(β) = Σ_k m_k f_S(λ_k;β) = −(1/2)M_1·β + (1/4)M_2·β² − (1/48)M_4·β⁴ + O(β⁵)`, with `M_j = Σ_k m_k λ_k^j` the rep-multiplicity-weighted power-moments. The leading IR moment is the **first power M_1** (β¹ coefficient `−M_1/2`), NOT the zeroth-power count.
- **Step 4 (the testable difference)**: `rel_diff = |(a₀/a₂)_{S_vN} − C_Q/R| / |C_Q/R|`. Reading-1 (β-coefficient ratio): `(a₀/a₂)_{S_vN} = c_1/c_2 = (−M_1/2)/(+M_2/4) = −2 M_1/M_2 = −0.498968`. Reading-2 (bare-count channel): `(a₀/a₂)_{S_vN} = f_S(0)·Tr(1)/a₂ = 0`. Baseline `C_Q/R = 6440/2776.165389 = 2.319747`.
- **Step 5 (direction read-off)**: `rel_diff(R1) = |−0.498968 − 2.319747|/2.319747 = 1.215096 = 121.51% > 1%`. **SIGN FLIP**: entropy ratio `−0.499 < 0 < C_Q/R = +2.320` — the deepest possible departure. Reading-2: `rel_diff = 100%`. Both ≫ floor ⟹ universality BROKEN ⟹ PASS.

**Results**:
- **rel_diff (Reading-1, reported value) = `1.215096` (121.51%)** vs the **`1%` PASS floor** → PASS (universality BROKEN). PASS = rel_diff > 1%.
- Entropy-functional `(a₀/a₂)_{S_vN}` (Reading-1, coeff ratio) = `c_1/c_2 = −2 M_1/M_2 = −0.498968` — **SIGN-FLIPPED** relative to the monotone baseline.
- Entropy-functional `(a₀/a₂)_{S_vN}` (Reading-2, bare-count channel) = `0` (because `f_S(0)=0`); rel_diff = `1.0000` (100%).
- Monotone-f baseline `C_Q/R = a_0_FW_zeta/a_2_FW_zeta = 6440/2776.165389 = 2.319747` (S65 PERMANENT value; `R_K(tau_fold)=2.0181`).
- Spectral power-moments (L12 cache, rep-multiplicity `m_k = dim(p,q)` per Peter-Weyl sector; 166,896 eigenvalue-entries, Tr(1)=3.195672e7): `M_1 = 1.257482e8`, `M_2 = 5.040331e8`, `M_4 = 8.489131e9`.
- Entropy β-expansion coefficients: `c_1 = −M_1/2 = −6.287409e7`, `c_2 = +M_2/4 = 1.260083e8`, `c_4 = −M_4/48 = −1.768569e8`.
- **β-expansion convergence (regime VALID)**: the analytic single-term coefficients (Sage-exact series summed term-by-term) agree with an independent UV-window polynomial fit (`β ∈ [0.01, 0.05]`, where `β·λ_max=0.27 ≪ 1` makes the truncation valid) to `rel(c_1)=6.78e-10`, `rel(c_2)=8.48e-08` → `c_k` converge CLEANLY on the L12 cache, NO continuum limit needed (rules out the INFO branch). The peak of the entropy weight is at `x* = β·λ = 1.2784645` (root of `(x−1)e^x=1`).
- **4-tuple**: `(value=1.215096, scheme=von-Neumann-entropy-functional-CCvS2019, convention=RATIO, L_max=12)`; `regulator_pin=a_4^{ζ}` companion row (the MONOTONE-f baseline anchor a_0_FW_zeta/a_2_FW_zeta).
- **schema-v2 3-tuple**: `sign_verdict=PASS` (the entropy ratio differs from C_Q/R in the predicted direction — a sign flip), `magnitude_verdict=PASS` (rel_diff 121.5% > 1% floor), `regime_verdict=VALID` (β-expansion converges cleanly). Composite collapse → **PASS**.
- **dual-SHA**: `audit_sha256=e3c395e64d228973cf1ee13d5bd9449ecd9271c94c9fa57da365676c78a1df6c` (script+canonical+pinmap), `content_sha256=ec520db1f6bdeb359055cf8d3b0742035e22837834b0c97c124f84837d581b40` (script).

**Substrate-physics (lizzi-signature reading)**: The fabric's eigenvalue spectrum is FIXED; only the spectral-functional LENS changes. The arrow runs `D_K eigenvalues → the entropy weight f_S(λ)=−βλ/(e^{βλ}+1) (the von Neumann information content of the fabric's fermionic Fock state) → S_vN = Tr f_S(D²/β²) → its β-expansion moments → the CC ratio`. **What is FUNCTIONAL-INDEPENDENT (structural)**: the spectral content {λ_k, m_k} itself, and the count `a₀ = zeta_D(0) = Tr(1)` (any monotone f with f(0)≠0 reads the same count at leading order). **What is FUNCTIONAL-DEPENDENT (scheme-dependent, the physical d.o.f.)**: the a₀/a₂ RATIO. Under monotone f the leading moment is the **count** (zeroth power); the entropy weight has `f_S(0)=0`, so its leading IR moment is the **first power M_1** — a categorically different channel. This is *why* the S65 universality breaks: S65/W4 prove `a₀/a₂=C_Q/R` only for monotone f (where the count channel dominates a₀); the entropy functional has NO count channel, so it reads a DIFFERENT, sign-flipped ratio out of the SAME fabric. This is the lizzi-signature thesis verbatim — what survives all functional choices is structural (the spectrum, the count); what depends on the choice is a physical degree of freedom (the CC ratio). **The CC is FUNCTIONAL, not geometrically frozen.** The surviving NCG CC channel — the only physically-motivated functional S65 never computed — is LIVE: the entropy lens reads a non-geometric CC ratio from the information content of the substrate's own spectrum, not assigned from a container.

**Solution-space**: PASS RE-OPENS the functional NCG CC channel (R-5/G-3). After the geometric channels were closed (a₀, a₂, a₃ monotone per S65; a₄-anomaly tested in INV5-W1-2), this is the surviving functional channel and it is non-trivial — the non-monotone f_S escapes both the W4 monotonicity wall and the S65 universality. This feeds INV5-W3-2 sub-question (b) on the **SA-authority-preserved** side (the spectral action retains a vacuum-energy handle via functional selection, complementing rather than competing with the Volovik/Gibbs-Duhem thermodynamic mechanism — itself a von Neumann entropy of the GGE state, so the two are the SAME information-theoretic object read at two scales). Caveat: this gate establishes that the entropy functional gives a DIFFERENT ratio; it does NOT yet pin the absolute CC magnitude to ρ_Λ (the lizzi distinction: the FI-under-functional content is the structural break; the absolute value is a physical d.o.f. to be pinned by consistency, not shopped). The absolute-magnitude / continuum-DOS / ρ_Λ-distance question is the natural carry-forward.

**Output Artifacts** (closure-verification checklist; on-disk presence + must_contain grep):
- (1) script `computations/investigation-5/inv5_w1_5_entropy_functional_cc_a0_a2_ratio.py` — present; `from canonical_constants import` ✓, `print_verdict_payload` ✓.
- (2) data `computations/investigation-5/inv5_w1_5_entropy_functional_cc_a0_a2_ratio.npz` — present.
- (3) plot `computations/investigation-5/inv5_w1_5_entropy_functional_cc_a0_a2_ratio.png` — present.
- (4) verdict line in `computations/investigation-5/inv5_gate_verdicts.txt` — present; matches `^INV5-W1-5-ENTROPY-FUNCTIONAL-CC-A0-A2-RATIO:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion row ✓; schema-v2 3-tuple row ✓; regulator_pin row ✓.
- (5) this WP section — `**Status**: COMPLETED` ✓, `**Verdict**: PASS` ✓, `**Output Artifacts**` ✓, `**MCP Pre-Compute Audit**` ✓.

---

## Wave 1 Synthesis (team-lead)

Wave 1 attacked the joints where the spectral triple meets the SM. Five compute gates: **2 PASS (W1-1, W1-5), 1 INFO (W1-3), 2 FAIL (W1-2, W1-4)**. Three coherent findings.

**Finding A — the cosmological constant has no GEOMETRIC escape, but the FUNCTIONAL channel is live (W1-2 FAIL + W1-5 PASS).** W1-2 closed the last geometric NCG CC channel: the a₄ Weyl²/trace-anomaly sub-term is monotone in τ (0 sign changes, unique stationary point at τ=0, Sage-exact to 9e-16), so it does NOT escape the W4 wall — every geometric a_{2k} moment (a₀/a₂/a₃ from S65, now the a₄-anomaly) is monotone; OOM-distance 115.76 reproduces the canonical CC gap. W1-5 then opened the functional door: the von Neumann entropy functional breaks BOTH the S65 a₀/a₂=C_Q/R universality AND W4, sign-flipping the ratio to −0.499 vs +2.320 — because f_S(0)=0 (no count channel; the leading IR moment is M₁, a categorically different channel). The a₀/a₂ ratio is permanently **SCHEME-DEPENDENT** (a functional-choice d.o.f.); the functional-invariant content is the spectrum itself. This pair is exactly the W3-2 workshop's sub-(b) evidence — which resolved that the CC lives in Layer B (μ-selected, outside the SA family).

**Finding B — the generation hierarchy ε_LX is EXTERNAL: both intra-substrate routes closed (W1-3 INFO + W1-4 FAIL).** W1-4: the Tomita-Takesaki modular twist of A_K⋊ℝ is multiplicity-SCALAR on every Peter-Weyl block (off-scalar 0.000; test-power control gives 89/90 NON-scalar on a *resolving* generator, so the null is genuine) — the §VII.BL Skolem-Noether no-go survives even the non-inner modular flow; B-1 closed. W1-3: the substrate-forward Connes distance ladder widens (sign right, ≠ Froggatt-Nielsen) but is Casimir-graded (ratio **12.56**), NOT the PDG log-mass 1.889 — and the agent exposed that the "1.889 EXACT" the plan cited was a Route-B tautology (the inverse-Yukawa ansatz feeds the masses in; ℓ cancels). B-4 constrained: even the substrate's intrinsic metric is Casimir-graded, not mass-graded. Both STRENGTHEN §VII.BL — ε_LX requires an external non-left-invariant ingredient.

**Finding C — the NCG Higgs survives its own broken axiom (W1-1 PASS).** The PS quadratic-fluctuation route (order-one violated at 4.000, A_quad retained, M₄→0 per S97) gives m_H^PS = 135.01 → 131.8 within the eps_H band (|Δ|=3.21 ≤ 6.7), A_quad/A_lin=0.113<0.3 (perturbatively controlled), no spurious colored scalars. Repairs G-1/C-1: the NCG-derived Higgs is robust to its own broken order-one axiom. (Convention note: anchored to the S70-resolved ratio_gilkey=0.4140, not the cache-moment 0.4866.) Feeds the W3-3 Higgs-residual review's QUARTIC leg.

### What Changed

#### (a) Numerical revisions
- m_H^PS = 135.01 GeV (→131.8, +3.21); (a₀/a₂)_entropy = −0.499 vs C_Q/R = +2.320 (sign-flip); a₄-Weyl OOM-distance = 115.76; Connes ladder ratio 12.56 (substrate-forward) vs 1.889 (Route-B tautology); modular off-scalar = 0.000 / 89-of-90 control.

#### (b) Structural changes
- **Last geometric CC channel CLOSED** (W1-2); **functional CC channel LIVE** and a₀/a₂ permanently scheme-dependent (W1-5).
- **B-1 (modular ε_LX) CLOSED** + **B-4 (Connes-distance ε_LX) constrained** → ε_LX is external; §VII.BL strengthened.
- **G-1/C-1 REPAIRED** — NCG Higgs robust to the order-one violation.

### Effected In-Session (non-math)
None investigation-effectable — all session-track curated-register edits, routed to `/rclab-investigate --investigation 5`:
- [→investigate] W1-3 lepton-spacing signature (substrate-forward 12.56, Casimir-graded; the Route-B 1.889 tautology flagged) → `mack` falsifier surface (sole-writer) + §VII.BL annotation.
- [→investigate] W1-2 ρ_anomaly/ρ_Λ OOM=115.76 + W1-5 functional-CC-channel-live + a₀/a₂-scheme-dependent → §VII / CC-register note (the W3-2 verdict consumes this).
- [→investigate] W1-1 convention provenance (ratio_gilkey=0.4140 per S70 RATIO-GILKEY-70, not the cache-moment 0.4866) → provenance hygiene.

## Carry-Forward Computations

Wave-1 outcomes are decisive — most close in-investigation (W1-1 within band; W1-2 cleanly monotone; W1-4 cleanly scalar by block-constancy; W1-3 a structural Casimir-grading finding, not a precision miss). One genuine forward compute:

### CF-INV5-W1-A — Absolute CC magnitude under the entropy functional (W1-5 continuation)
| Field | Spec |
|:------|:-----|
| **What** | W1-5 established a different a₀/a₂ RATIO (−0.499, scheme-dependent); compute the ABSOLUTE entropy-functional vacuum-energy magnitude + its continuum-DOS limit and its distance to ρ_Λ — pinning the CC value by consistency (the lizzi distinction: the ratio's functional-dependence is structural; the absolute value is a d.o.f. to be pinned, not shopped). |
| **Inputs** | `inv5_w1_5_entropy_functional_cc_a0_a2_ratio.py` (β-expansion c_k machinery, converged rel 6.8e-10); L12 cache; ρ_Lambda_obs; the f_S=−βλ/(e^{βλ}+1) functional. |
| **Gate** | absolute ρ_vac^{entropy} emitted with a continuum-DOS extrapolation + a pinned `|log10(ρ_vac/ρ_Λ)|`; PASS if a single defensible magnitude lands (no functional-shopping). |
| **Effort** | ~1 wave-equiv (machinery exists; new work is the absolute normalization + continuum DOS). |

(W1-3/W1-4 establish ε_LX-external as a structural finding — the forward item "identify the external non-LI ingredient" is a session-track design question, not a pinned compute. W1-1/W1-2 are closed/within-band — no compute CF.)

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:---------|:-------|
| 2026-06-15 | NCG CC — geometric channels (G-3) | a₀/a₂/a₃ monotone (S65); a₄-anomaly untested | ALL geometric a_{2k} monotone → no geometric CC escape | W1-2 a₄-Weyl 0 sign-changes, stationary only at τ=0 |
| 2026-06-15 | NCG CC — functional channel (B-2/R-5) | untested (S65 flagged, never computed) | LIVE — entropy functional breaks a₀/a₂ universality + W4 (sign-flip) | W1-5 rel_diff 121.5%, ratio −0.499 vs +2.320; a₀/a₂ scheme-dependent |
| 2026-06-15 | ε_LX intra-substrate via modular twist (B-1) | open (the non-inner-flow escape from §VII.BL) | CLOSED — modular twist multiplicity-SCALAR | W1-4 off-scalar 0.000; Skolem-Noether survives |
| 2026-06-15 | ε_LX as Connes-distance ladder (B-4/R-4) | candidate (the §VII.BL positive realization) | constrained — substrate metric Casimir-graded (12.56), not mass-graded (1.889) | W1-3; Route-B 1.889 exposed as inverse-Yukawa tautology |
| 2026-06-15 | NCG Higgs robustness to order-one violation (G-1/C-1) | open tension | REPAIRED — m_H^PS=135.01→131.8 within eps_H, A_quad/A_lin=0.113 | W1-1 PASS |

## Files Produced

| Gate | Script (`computations/investigation-5/`) | Data | Plot | Verdict | audit_sha256 (head) |
|:-----|:------------------------------------------|:-----|:-----|:--------|:--------------------|
| INV5-W1-1 | inv5_w1_1_ps_quadratic_fluctuation_higgs_quartic.py | ✓ | ✓ | PASS | 687d9c9d… |
| INV5-W1-2 | inv5_w1_2_a4_weyl_trace_anomaly_cc.py | ✓ | ✓ | FAIL | 2a667045… |
| INV5-W1-3 | inv5_w1_3_connes_distance_lepton_mass_ladder.py | ✓ | ✓ | INFO | 949edd1d… |
| INV5-W1-4 | inv5_w1_4_modular_twist_multiplicity_nonscalar.py | ✓ | ✓ | FAIL | a0b78f29… |
| INV5-W1-5 | inv5_w1_5_entropy_functional_cc_a0_a2_ratio.py | ✓ | ✓ | PASS | e3c395e6… |

(Verdict ledger: `computations/investigation-5/inv5_gate_verdicts.txt`.)
