# Investigation 5 Wave 2 — Condensed-Matter Functionals (impulse-quench / pseudogap / self-energy) (Results Working Paper)

**Investigation**: 5 | **Wave**: 2 | **Plan**: investigation-5-plan-w2.md | **Theme**: Fix the FUNCTIONAL — replace the equilibrium/budget free-energy objects (slow-roll `1/ε_H` prefactor, single-mass Leggett anchor, fitted Volovik-effacement factor) with the correct sudden-quench / pseudogap / continuum-self-energy objects on the framework's two largest live quantitative gaps (the A_s amplitude floor and the ~170× dark-matter mass).

**Track**: INVESTIGATION | **Verdict ledger**: `computations/investigation-5/inv5_gate_verdicts.txt` (emit via `emit_verdict(session=5, track="investigation", ...)` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`). All four gates are `gate_type: compute`, all carry the `[SIGN]` trigger → each emits a canonical verdict line + dual-SHA companion row + the `[SIGN]` 3-tuple companion row. Investigation-track results are exploratory: they enter the knowledge index / `canonical_constants.py` / `falsifier-master-inventory.md` ONLY on session-promotion (`gate-verdicts.md §"Track-local boundary"`) — these gates COMPUTE the substrate numbers and emit verdict lines to the `inv5` ledger; they do NOT write `canonical_constants.py` or the inventory.

## Gate Sections

### §W2-1. INV5-W2-1-AS-IMPULSE-QUENCH-BOGOLIUBOV (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W2-1-AS-IMPULSE-QUENCH-BOGOLIUBOV`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the scalar power `A_s` is the spectral-weight content of the frozen Bogoliubov occupation `|β_k|²` — the GGE relic of the supersonic transit, read off the cached transit spectrum)
**Gate type**: `compute`
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: in the impulse (sudden-quench) limit `A_s` is set by the frozen Bogoliubov occupation `Σ_k|β_k|²` normalized by the saturated KZ correlation length `ξ̂` (NOT the slow-roll `1/ε_H` prefactor × additive decoherence budget), yielding ONE canonical amplitude OOM (replacing the 3.02×/3.15/4.56/9.5-OOM self-disagreement) plus the frozen wavenumber `k̂ = 1/ξ̂` as the characteristic comoving scale.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source).

**Verdict**: **INFO** (composite). 3-tuple: **sign=PASS** (impulse < slow-roll, `ratio = 0.0378 < 1`), **magnitude=INFO** (the canonical OOM is the deliverable, not a pre-set target; `OOM_gap = +0.8644`, factor 7.32 over Planck — sub-1-OOM, far below the 9.5-OOM wall), **regime=VALID** (sudden limit `dt/T_L = 1.25e-5 ≪ 1`; frozen spectrum UV-flat, slope −0.003). Composite collapse (`gate-verdicts.md`): regime=VALID ∧ sign=PASS ∧ magnitude=INFO ⇒ **INFO**. The impulse-quench normalization is the correct functional and lands ONE defensible number; the residual overproduction is now sub-OOM (collapsed from the 9.5-OOM wall) — the wall is largely a normalization-scheme artifact. **Dual_prior re-allocation**: SIGN=PASS + single regime-VALID OOM emitted ⇒ **0.85 → Track A** (bridge B-1 substantially confirmed; A_s is a normalization-scheme object, the impulse normalization collapses +9.16 → +0.86 OOM); residual sub-OOM gap means the wall persists at a single pinned, defensible height (the INFO registry state). **Audit**: `audit_sha256=01da2112cfab6f3935441c807265a79a1469bd25e72c523038b1f4070a0b85c6`, `content_sha256=7eb0ea72cc43bc5918d1a1eaffc7f6bf28f0fba66ce8e63c5462bfe6781611d0`.

**Output Artifacts**:
- **Script**: `computations/investigation-5/inv5_w2_1_as_impulse_quench.py` (must_contain `from canonical_constants import`, `print_verdict_payload` — both present).
- **Data**: `computations/investigation-5/inv5_w2_1_as_impulse_quench.npz` (A_s_raw, OOM_gap, k_hat, N_norm, beta2_khat, the SIGN-test ratios, the xi_BCS cross-check anchor + its D_max, the full `k_grid`/`beta2_spectrum`, atlas-T4 branch structure).
- **Plot**: `computations/investigation-5/inv5_w2_1_as_impulse_quench.png` (panel a: frozen `|β_k|²` spectrum with `k̂`/`k_pivot` marked, UV near-flat; panel b: OOM ladder — impulse `+0.86` vs slow-roll-ledger `+2.29` vs raw-slow-roll `+3.99` vs n_pairs-naive `+9.16` vs Planck).
- **Verdict line**: `computations/investigation-5/inv5_gate_verdicts.txt` (canonical line + dual-SHA companion + `[SIGN]` 3-tuple row + regulator_pin row; emitted via `emit_verdict(session=5, track="investigation", ...)`).
- **WP section**: this section.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `get_constant('xi_KZ_FW')` → **0.018760052113614718** (S89; substrate-natural impulse-regime ξ̂). PINNED.
- `get_constant('A_s_Planck')` → **2.1e-09** (Planck 2018; OOM-gap denominator). PINNED as methodological cross-check anchor.
- `get_constant('n_pairs')` → **59.8**; `get_constant('P_exc_kz')` → **1.0** (KZ saturation, S38). Used in the aggregate cross-check.
- `get_constant('xi_BCS')` → **0.8083468754** M_KK⁻¹ (S53 BCS coherence length). Reported ONLY as the xi_BCS cross-check anchor; D_max(0.808 vs 0.0187601) = **1.6344** ⇒ HARD-HALT band if consumed as ξ̂ (the Class-(f) PIN-PLACEHOLDER pathology the plan flags); NOT used as ξ̂.
- `get_constant('M_KK')` → 7.42866e16 GeV (substrate scale).
- `trace_entity('A_s amplitude floor')` → CF23 "**HARDENED to PERMANENT WALL** — A_s amplitude floor"; S84 F_supp dynamics-side rate-limiter (F_supp_max=1.043783). **Branch decision: NOT pre-closed.** The CF23 wall was established for the *slow-roll / UNIFIED-AS-79 ledger* route (the F_supp dynamics rate-limiter). The impulse-quench-Bogoliubov-normalized-by-ξ̂ route is a STRUCTURALLY DISTINCT functional that has NOT been computed — this gate tests whether that functional dissolves or confirms the wall. Reported honestly: the prior literature leans Track-B (wall is real for the ledger route); this gate's SIGN=PASS + sub-OOM result is the Track-A evidence that the *normalization scheme* carried most of the 9.5-OOM overproduction.
- `search_knowledge('A_s amplitude impulse-quench Bogoliubov beta_k Kibble-Zurek frozen occupation')` → prior A_s figures are the ledger route (`A_s = 3.30e-9` FROZEN Branch-A S86; AMPLITUDE-NORM-66 FAIL 3.15 OOM Route-B graph-mode occupation); the GGE relic uses `n_k = |β_k|²` (Kofman-Linde-Starobinsky); **the impulse-quench-ξ̂ normalization is NOT among the prior computations** — this gate is new.
- `trace_entity('impulse-quench Bogoliubov A_s')` → no trace (confirms novelty).

**Results**:

**(i) Canonical amplitude OOM — the deliverable.** A_s^impulse = **1.5367e-08**; **OOM_gap = log10(A_s^impulse / A_s_Planck) = +0.8644** (4 s.f.), i.e. factor **7.32** over Planck `2.1e-9`. Scheme `IMPULSE-QUENCH-BOGOLIUBOV`, convention `FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL-XI-KZ`, L_max=10. This ONE number replaces the 3.02/3.15/4.56/9.5-OOM self-disagreement.

**(ii) Frozen wavenumber.** k̂ = 1/ξ̂ = **53.3048 M_KK** (ξ̂ = xi_KZ_FW = 0.0187601 M_KK⁻¹). Ratio to the CMB pivot k_pivot = 14.311 M_KK (fold normalization): **k̂/k_pivot = 3.7247** — the frozen spectrum's characteristic scale sits a factor 3.72 ABOVE the pivot. This is the substrate-derived `deg(T_{BZ→pivot})` target scale (G-3): the substrate's own answer to "where is the pivot."

**Substrate-natural construction (dimensional, NOT fit).** Standard dimensionless power `P_ζ(k) = (k³/2π²)|ζ_k|²` with `[|ζ_k|²]=k⁻³`. Impulse-quench source (del Campo & Zurek 1310.1600): the frozen field's mode spectral weight at the characteristic scale is the frozen occupation spread over the KZ coherence VOLUME, `|ζ_k|² = |β_k|²·ξ̂³`, so `N_norm = ξ̂³ = 6.6024e-06` is the substrate-natural KZ coherence volume — NOT a tuned normalization. At the frozen mode k̂=1/ξ̂, since `k̂³ξ̂³ = 1` exactly (asserted in-script), the construction collapses to `A_s^raw = |β_{k̂}|²/(2π²)`. The occupation `|β_{k̂}|² = 3.0333e-07` is read from the S100b box-delta sudden-limit Bogoliubov spectrum (`s100b_box_delta_bogoliubov.npz`; scheme BOX-DELTA-SUDDEN; 3-code-path PASS to 1.4e-13; unitarity 1.9e-14) — evaluated at k̂=53.30 by power-law UV-tail extrapolation. The UV tail is near-FLAT (log-log slope −0.0031), so `|β_k|²` is nearly scale-invariant in the impulse regime (the substrate signature of the sudden limit, consistent with the framework's frozen-spectrum n_s≈1); the value is robust whether evaluated at k̂ (3.033e-07), at k_max (3.035e-07), or at the pivot (3.045e-07).

**SIGN sub-test (substitution-chain Step-5, with substituted numbers).** The chain claims `A_s^impulse / A_s^slow-roll < 1`. The slow-roll assembly being replaced, `A_s^slow-roll = P_pref·(1/ε_H)·F_amp·(1/c_sub)·f_conv`, carries the explicit slow-roll-specific factor `1/ε_H = 1/0.02163 = 46.232` (≫1). The impulse numerator `|β_{k̂}|²/(2π²)` is a bounded frozen-occupation sum (no 1/ε_H blow-up; n_pairs=59.8 finite, P_exc=1.000). Substituted: A_s^slow-roll (UNIFIED-AS-79 ledger, Branch-A) = **4.0693e-07** → `ratio_impulse/slow-roll = 1.5367e-08 / 4.0693e-07 = 0.0378 < 1` ✓; against the untamed `P_pref/ε_H = 2.0435e-05` → `ratio = 7.52e-04 ≪ 1`. **sign of (A_s^impulse − A_s^slow-roll) is NEGATIVE** (sign_verdict=PASS): the impulse normalization REDUCES A_s relative to the slow-roll-prefactor assembly, exactly as Step 5 predicts from ε_H ≪ 1 ⇒ 1/ε_H ≫ 1.

**Cross-checks / alternative constructions (NOT the deliverable; reported for transparency).** Bare 64-mode `Σ_k|β_k|²/(2π²)` → OOM +2.70; `n_pairs/(2π²)` (the naive total-occupation dump) → OOM **+9.16**, which reproduces the historical ~9.5-OOM wall — confirming that the wall is exactly the artifact of dumping the total aggregate occupation rather than reading the per-coherence-cell frozen-mode occupation. Atlas-T4 branch structure (B1 / B2[0-3] / B3[0-2]; B2 DOS 14.0233 van Hove enhancement) consistent with n_pairs=59.8, P_exc=1.000. Regime: dt/T_L=1.25e-5 (sudden) ∧ UV-flat ⇒ regime_verdict=VALID.

**Substrate-physics reading.** A_s IS the loudness of the post-transit GGE acoustic interference pattern — the spectral-weight content of the frozen Bogoliubov occupation at the adiabatic-impulse boundary, read off the cached `|β_k|²`, NOT a slow-roll inflaton's 1/ε_H. The flow is `D_K eigenvalues → frozen Bogoliubov occupation |β_k|² → scalar power A_s → CMB amplitude`. The slow-roll 1/ε_H prefactor is the container-thinking error (there is no inflaton rolling down a potential — there is a substrate spectrum frozen by a Mach-13.75 supersonic transit); replacing it with the substrate-natural frozen-occupation-per-KZ-cell normalization collapses the +9.16-OOM overproduction to +0.86 OOM. **CROSS-TRACK note**: the canonical A_s OOM, the HY1 three-named-quantity `canonical_constants.py` pin, and any `falsifier-master-inventory.md` A_s row are **session-promotion + `mack-cosmic-bridge` sole-writer** — NOT written here; this gate emits to the `inv5` verdict track ONLY. The CF23 "PERMANENT WALL" tag stands for the slow-roll/ledger route; this gate's result (sub-OOM under the impulse normalization) is the Track-A evidence that the *scheme* carried most of the overproduction, pending session-promotion adjudication.

---

### §W2-2. INV5-W2-2-NSR-PSEUDOGAP-TWO-SCALE-DM (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W2-2-NSR-PSEUDOGAP-TWO-SCALE-DM`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the dark-matter quasiparticle IS the Leggett inter-band coherence mode of the (0,0)-sector; its mass is a spectral moment of `D_K` on the (0,0) block)
**Gate type**: `compute`
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: the ~170× DM-mass shortfall is the symptom of forcing ONE scale (`Δ_BCS` × the 11.97× Leggett anchor) to do the job of TWO distinct NSR/pseudogap scales — phase-stiffness `D_s` (gives the correct `Ω_DM h²=0.120`) vs single-particle pseudogap `Δ_pg` (probes structure formation); an NSR two-scale split supplies the missing ~14× via the `Δ_pg` leg WITHOUT breaking the abundance match on the `D_s` leg.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w2.md` §W2-2 (two-condition AND operator, tol_abundance/tol_shortfall, regulator pin).

**Verdict**: **FAIL** — composite=FAIL via the `[SIGN]` collapse rule (`sign_verdict=FAIL ⇒ composite=FAIL`). The substrate INVERTS the pre-registered pseudogap-regime ordering: `Δ_pg < D_s`-scale, not `Δ_pg > D_s`. 3-tuple = (**sign=FAIL**, magnitude=INFO, regime=VALID).

**Output Artifacts** (closure-verification checklist):
- (1) script `computations/investigation-5/inv5_w2_2_nsr_pseudogap_two_scale.py` — EXISTS; `grep -E 'from canonical_constants import'` → matches (`from canonical_constants import (`); `grep -E 'print_verdict_payload'` → matches (def + call site).
- (2) data `computations/investigation-5/inv5_w2_2_nsr_pseudogap_two_scale.npz` — EXISTS (all legs + ratios + 3-tuple fields saved).
- (3) plot `computations/investigation-5/inv5_w2_2_nsr_pseudogap_two_scale.png` — EXISTS (Panel A energy-scale bars; Panel B `r_2scale` vs anchor target band).
- (4) verdict line in `computations/investigation-5/inv5_gate_verdicts.txt` — EXISTS; `grep -E '^INV5-W2-2-NSR-PSEUDOGAP-TWO-SCALE-DM:.* audit_sha256=[a-f0-9]{64}'` → matches (canonical line + dual-SHA companion + 3-tuple companion, 3 rows).
- (5) this WP section — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):
- `search_knowledge('NSR Nozieres-Schmitt-Rink pseudogap two-scale superfluid stiffness dark matter')` → LEGGETT-MOMENT-70 (first Type-F DM channel, PROVEN); `framework-dm-properties` registry (Leggett-channel; `little`/`mack` sole-writer). No pseudogap-two-scale gate exists.
- `search_knowledge('Peotta Torma quantum metric superfluid weight D_s phase stiffness')` → **`Peotta-Torma for CC` theorem #79 PROVEN: "Flat-band superfluid weight route inapplicable to CC"** (S64); `D_s = D_conv + D_geom` decomposition; **`QUANTUM-METRIC-64` gate FAIL: `D_s(PT)=0.000` vs `D_s(Josephson)=6.283`** (my own S64 W6-D).
- `trace_entity('QUANTUM-METRIC-64')` → the geometric quantum-metric route gives `D_s≈0` from **three structural zeros** (pure-gauge CG(24) Peierls flux; mode-preserving pair-hop `T=E_J·I_8` → k-independent eigenvectors → `g_nn=0`; linear band dispersion → `d²E/dγ²=0`). The PHYSICAL stiffness is the Josephson f-sum-rule.
- `get_constant('Delta_BCS')` → `0.4642547394830737` (R-PROTECTED, S70). `get_constant('Mass_LeggettDM_over_Delta_BCS')` → `11.97` (C11 CONDITIONAL on Γ_grav<H_0, S70/S96). `get_constant('Omega_DM_h2')` → `0.120` (Planck OBSERVATIONAL-ANCHOR; Leggett-channel coincides at 0.6%). `get_constant('omega_L1')` → `0.138` (Leggett-1 mode). `get_constant('rho_B2_per_mode')` → `14.0233`. `get_constant('M_DM_Leggett_GeV')` → `4.128e17` GeV.
- `m_required/m_Leggett = 170` confirmed as `atlas-spectral-geometer-collab.md §5` equation (NOT a canonical pin; consumed as the structure-formation target, reported in .npz).
- **Branch on pre-closed**: the gate is NOT pre-closed, but the `D_s` leg is governed by a PROVEN structural wall (`QUANTUM-METRIC-64`, theorem #79) — the geometric superfluid-weight route is dead; the physical phase stiffness is the Josephson f-sum-rule. This wall is the reason the SIGN inverts (below).

**Results** (numbers first):

| Quantity | Value | Source |
|:---------|:------|:-------|
| `D_s_JPT` (superfluid weight, Josephson f-sum-rule) | **6.3563 M_KK²** | s61_superfluid_weight (`2·E_J·S_+/V_cell`) |
| `D_s_QM` (flat-band geometric route) | **1.72e-05 ≈ 0** | s61/s64 — three structural zeros (QUANTUM-METRIC-64) |
| `m_Meissner = √D_s` (phase-stiffness ENERGY) | **2.5212 M_KK** | this gate |
| `Δ_pg = Δ_BCS` (single-particle pseudogap) | **0.4643 M_KK** | canonical (Delta_BCS) |
| NSR pair pole `ω₊` | 0.7917 M_KK | s37_pair_susceptibility |
| pair-breaking continuum `2Δ_BCS` | 0.9285 M_KK | s37 (`E_vac_cutoff`) |
| `m_Leggett = 11.97·Δ_BCS` (abundance anchor) | 5.5571 M_KK | C11 |
| `m_struct = 170·Δ_BCS` (structure target) | 78.9233 M_KK | collab §5 |
| **`r_2scale = m_Meissner/Δ_pg`** | **5.4306** | this gate |
| `r_direct = Δ_pg/m_Meissner` | **0.1841** | this gate |
| target `r = 170/11.97` | **14.2022** | two anchors |
| **SIGN: `Δ_pg − m_Meissner`** | **−2.0569 (NEGATIVE)** | this gate |
| ABUNDANCE dev (`Ω_DM` leg) | **0.0000** (tol 0.05 → OK) | Leggett mode untouched |
| SHORTFALL dev (`r` vs 14.20) | 0.6176 (tol 0.20 → OFF-TARGET) | this gate |

4-tuple: `(value='r_2scale=5.4306|target=14.2022|Δ_pg=0.4643|m_Meissner=2.5212|sign=NEG|abundance_dev=0.0000', scheme=NSR-PSEUDOGAP-TWO-SCALE, convention=PHASE-STIFFNESS-Ds-VS-SINGLE-PARTICLE-PSEUDOGAP-Dpg, L_max=10)`.
dual-SHA: audit=`cd6e2297fea1d4ce6b0799abaed9e816895f06a72e4b74e2a854485a2bf0ebed`, content=`8ac372c613cdf83a5144e811223c2fddceb4c130496e5757c48258f98baa807b`.
3-tuple companion: `sign_verdict=FAIL magnitude_verdict=INFO regime_verdict=VALID`.

**Substitution chain — SIGN read-off (the load-bearing result), with substrate numbers:**

The plan's Step-4/5 claim was `Δ_pg ≥ Δ_c ≥ (phase-stiffness ∝ D_s)` ⇒ `Δ_pg > D_s` ⇒ `r_2scale > 1` from the *generic* BCS-BEC-crossover preformed-pair ordering. The substrate FALSIFIES this ordering:

1. `Δ_pg = Δ_BCS = 0.4643 M_KK` (single-particle pseudogap — confirmed: the (0,0) N=1 state is in the **BEC regime**, `μ/E_F = 0.192 < 1`, strong-coupling, pairs preform — so the pseudogap-regime *premise* HOLDS).
2. `D_s` as an energy scale = `m_Meissner = √(2·E_J·S_+/V_cell) = √6.3563 = 2.5212 M_KK`, with `E_J = 3.397 M_KK` (the per-bond Josephson coupling is LARGE).
3. `Δ_pg − m_Meissner = 0.4643 − 2.5212 = −2.0569 < 0` ⇒ **`Δ_pg < D_s`-scale**, `r_2scale = m_Meissner/Δ_pg = 5.43`, and the plan's intended `Δ_pg/D_s = 0.184 ≪ 1`.

**Why the chain inverts (substrate-first):** the standard pseudogap ordering `Δ_pg > D_s` holds for systems whose phase stiffness is set by a WEAK inter-cell hopping `J`. THIS substrate's phase stiffness is NOT a weak hop — it is the Josephson **f-sum-rule** (exact kinetic energy `2·E_J·S_+`, S61/S64), which the flat-band condensate makes anomalously LARGE while the geometric quantum-metric contribution is exactly ZERO (QUANTUM-METRIC-64 three structural zeros). The condensate is deeply **phase-rigid**: stiffness dominates the single-particle gap by 5.4×. The generic BCS-BEC ordering does not apply because the substrate is in the flat-band-Josephson stiffness regime, not the weak-hopping regime.

**Solution-space (constraint map):**
- **SIGN=FAIL ⇒ the B-3 bridge corridor is CLOSED at the energy-scale level.** The (0,0)-gap does NOT split into a small-stiffness/large-pseudogap pair; it splits the OTHER way (large stiffness, small gap). The two-scale NSR decomposition does NOT supply the +14× shortfall via a larger `Δ_pg` — the single-particle gap is the *smaller* scale.
- **ABUNDANCE leg preserved (dev=0):** the Leggett-mode abundance anchor (`m_Leggett=5.557 M_KK`, `Ω_DM h²=0.120` at 0.6%) is untouched — introducing a second scale did not degrade the abundance match. The abundance leg stands.
- **The 170× structure-mass shortfall remains OPEN.** It is NOT a two-scale pseudogap artifact resolvable by promoting `Δ_pg`. The single-mass-scale Leggett anchor (`11.97·Δ_BCS`) stands as the only substrate DM mass; the structure-formation factor 170 is not supplied by the gap-vs-stiffness separation.
- **dual_prior re-allocation:** SIGN=FAIL routes **0.85 → Track B** (the (0,0)-gap is not in a small-stiffness pseudogap regime that separates toward the shortfall; the 170× remains an open mass problem). Track A (B-3 correct, r≈14.2) is disfavored.
- **C-4 (static-3D-Ising vs sudden-quench) does NOT dissolve via this route** — the planned dissolution (phase-stiffness=static class, pseudogap=impulse object with r≈14.2) required SIGN=PASS.

**Robustness note (narrative only, not a gate):** neither single substrate energy scale reaches 170×. Reading the structure mass off the phase-stiffness ENERGY rather than the gap gives `m_Meissner/Δ_BCS = 5.43`, still below the Leggett `11.97`. The mass shortfall is robust to the two-scale reading — no choice of (gap, stiffness) leg as the "structure scale" supplies the factor 170.

**Substrate framing.** The dark-matter quasiparticle IS the Leggett inter-band coherence mode of the (0,0)-sector (CPT-neutral, non-annihilating). The flow is `D_K (0,0)-eigenvalues → {phase-stiffness D_s (Josephson f-sum-rule; geometric quantum-metric leg = 0 by QUANTUM-METRIC-64) , single-particle pseudogap Δ_pg (NSR pair-susceptibility)} → DM abundance + structure`. The substrate IS a BCS-BEC-crossover condensate in the BEC/pseudogap regime (`μ/E_F<1`), but its phase stiffness is set by the flat-band Josephson f-sum-rule, not a weak hop — so the gap is the SMALLER of the two scales, inverting the generic pseudogap ordering. The "170× problem" is NOT dissolved by treating the DM mass as two NSR scales: the substrate's two scales separate in the wrong direction to supply the structure-formation factor.

---

### §W2-3. INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the Higgs IS the `|S|²`-radial / amplitude mode of the substrate order parameter — a spectral excitation of the (0,0)-sector decaying into its own two-quasiparticle pair-breaking continuum)
**Gate type**: `compute`
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: the Higgs `|S|²`-mode's −5.36% residual against PDG (= 67/1251 exact, currently absorbed by the fitted Volovik-effacement factor `Γ_eff=0.99970`) is a DERIVED Pekker-Varma continuum self-energy — `Re Σ_continuum/m_H ≈ −5.36%` from coupling to the substrate's own B2/B3 two-quasiparticle pair-breaking continuum.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w2.md` §W2-3 (equality operator, tol=0.01 PASS / tol_info=0.03, Kramers-Kronig PV pin).

**Verdict**: **FAIL** (composite). `[SIGN]` 3-tuple = **sign=FAIL · magnitude=FAIL · regime=VALID**. At the pre-registered PRIMARY frequency `ω_H3 = 11.465` (the `|S|²`-radial m_H carrier) the computed `Re Σ_continuum = +0.03596 M_KK` is **POSITIVE**, opposite the plan's pre-registered `Re Σ < 0`. The plan's §W2-3 note is explicit: *"if the computed Re Σ is POSITIVE the bridge B-2 is falsified regardless of magnitude (the gate FAILs on sign)."* Composite collapse (`gate-verdicts.md` rule): `sign_verdict == FAIL ⇒ composite = FAIL`.

**Output Artifacts** (closure-verification; all on disk, content-verified):
- (1) script `computations/investigation-5/inv5_w2_3_pekker_varma_higgs_self_energy.py` — contains `from canonical_constants import` (Section 1) and `print_verdict_payload` (verdict-payload emitter). VERIFIED.
- (2) data `computations/investigation-5/inv5_w2_3_pekker_varma_higgs_self_energy.npz` — VERIFIED on disk.
- (3) plot `computations/investigation-5/inv5_w2_3_pekker_varma_higgs_self_energy.png` — VERIFIED on disk (2-panel: `Re Σ(ω)` sweep with continuum band + both Higgs modes; fractional-shift bars vs the −5.356% target band).
- (4) verdict line in `computations/investigation-5/inv5_gate_verdicts.txt` — matches `^INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=d51071e0c98040bf498e82d7e1ba2cfc4bb127a2e2c61fc264e317fdc199620d`, `content_sha256=fac8ad5b53973dd55bb34d69a79aa212b6a3d15e05b1255816ce85dbf5327fb1`; dual-SHA companion row + `[SIGN]` 3-tuple row + 6 diagnostic extra rows present (9 rows total). VERIFIED.
- (5) this WP section — `**Status**: COMPLETED`, `**Verdict**: …FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present.

**MCP Pre-Compute Audit** (queries executed BEFORE computing; query-first discipline):
- `search_knowledge('Pekker-Varma Higgs amplitude mode self-energy two-quasiparticle continuum')` → only hit on the **plan-w2.md itself** (`Σ_continuum = Σ_j |V_{Hj}|² G_2qp,j`, `G_2qp,j = 1/(ω−Ω_j+iε)`) + `c_Br5_Higgs3 = 11.465307` (S82 amplitude-mode Γ-point). **No prior INV5-W2-3 verdict / no closure** → gate is OPEN, not pre-closed.
- `search_knowledge('amplitude mode self-energy Im Sigma B2 B3 pair-breaking continuum S43 W6')` → S43-W6 IMAGINARY-part machinery EXISTS: `Im[Σ_i(ω_i)] = π Σ_j |V_{ij}|² ρ_j(ω_i)` (session-43-wave6.md); `Q_B2 = ω_B2/(2 Im[Σ_F,B2]) = 9.8` (S41 collab). The REAL part via Kramers-Kronig is the NEW piece.
- `trace_entity('Pekker-Varma amplitude mode continuum self-energy')` → **No trace found** (confirms novelty).
- `get_constant('m_H_FW_KK_threshold')` → **131.8**; `m_H_obs` (canonical_constants.py:2259) → **125.1**; residual `r_KK = 131.8/125.1 − 1 = 67/1251` Sage-exact = **+5.35572%** (target = NEGATIVE of this).
- `get_constant('Delta_BCS')` → **0.4642547394830737** (R-PROTECTED, S70) ⇒ pair-breaking edge `2Δ_BCS = 0.928509`.
- `get_constant('omega_H3')` → **11.465** (`|S|²` amplitude-mode Γ-point, PRIMARY); `get_constant('omega_H2')` → **1.410** (Higgs-Leggett hybrid, cross-check).
- `get_constant('rho_B2_per_mode')` → **14.023250** (B2 DOS anchor); `get_constant('Gamma_effacement')` → **0.99970** (the fitted factor being tested-against; `(1−Γ_eff)=3e-4 = 0.03%` is a DISTINCT quantity from the 5.36% residual — survey C-2/U-2).
- **Branch**: NOT pre-closed → proceed to compute.

**Results** (NUMBERS first):

*Substrate inputs* (FULL physical caches; NEITHER SCHEMATIC; no tier_pin row):
- (0,0)-sector gaps `Δ_B[1,2,3] = [0.37179, 0.73203, 0.08415] M_KK` and DOS `ρ_B[1,2,3] = [3.9359, 14.6683, 0.4839]` — from `s48_leggett_mode.npz` (`Delta_fold`, `rho_fold`, τ_fold=0.19).
- Higgs-continuum vertex `V_B2B2 = 0.58921` and `Δ_pair = 0.46425 (= Δ_BCS)` — from `s43_fano_continuum.npz` (the S43-W6 Fano/self-energy machinery).
- `|S|²`-radial Hessian `H_ss = 2.0982` (s54_higgs_modulus.npz) — bare-mode cross-check.

*B2/B3 two-quasiparticle pair-breaking continuum* (channel j=(a,b): threshold `Δ_a+Δ_b`, joint-DOS weight `∝ ρ_a ρ_b`, bandwidth `W = 2Δ_BCS = 0.92851`):

| channel | threshold (M_KK) | norm joint-DOS weight |
|:--|:--|:--|
| B3+B3 | 0.1683 | 0.0008 |
| B1+B3 | 0.4559 | 0.0064 |
| B1+B1 | 0.7436 | 0.0521 |
| B2+B3 | 0.8162 | 0.0238 |
| B1+B2 | 1.1038 | 0.1940 |
| **B2+B2** | **1.4641 (band top)** | **0.7229 (dominant)** |

Continuum support: `Ω ∈ [0.1683, 1.4641+W]`; the dominant spectral weight is the B2+B2 channel at `2Δ_B2 = 1.464`.

*Self-energy* `Re Σ(ω) = Σ_j |V_{Hj}|² P∫ ρ_j(Ω)/(ω−Ω) dΩ` (Kramers-Kronig; symmetric PV excision, ε→0):
- **PRIMARY `ω_H3 = 11.465`: `Re Σ = +0.03596 M_KK` ⇒ `Re Σ/m_H = +0.3136%`** (POSITIVE). `Im Σ(ω_H3)=0` (mode outside the continuum ⇒ pure dispersive repulsion). ε→0 PV spread `= 0.0` ⇒ regime VALID.
- Cross-check `ω_H2 = 1.410`: `Re Σ = −0.79509 M_KK` ⇒ `Re Σ/m_H = −6.9349%` (or `−56.39%` normalized by its own frequency); `Im Σ(ω_H2)=0.31701` (mode inside the continuum). SIGN here is NEGATIVE — the correct softening direction — but the magnitude is wrong and it is the WRONG mode.
- Target: `−5.3557% = −67/1251` exact. `|primary − target| = 5.669 pp ≫ 3 pp` INFO band ⇒ magnitude=FAIL.

*Substitution chain — SIGN read-off (executed, not assumed; `math-scripts.md` "Double-Check Logic")*:
- Step 1: `Re Σ(ω) = Σ_j |V_{Hj}|² P∫_{thr_j}^{thr_j+W} ρ_j(Ω)/(ω−Ω) dΩ`, with `ρ_j ≥ 0`, `|V_{Hj}|² ≥ 0`.
- Step 2: substrate continuum weight lives in `Ω ∈ [2Δ_B3, 2Δ_B2+W]`; dominant weight at `2Δ_B2 = 1.464` (since `ρ_B2 = 14.67 ≫ ρ_B1, ρ_B3`).
- Step 3 (PRIMARY `ω_H3 = 11.465`): every continuum state has `Ω ≤ 1.464+0.929 = 2.393 < 11.465` ⇒ `(ω_H3 − Ω) > 0` for ALL `Ω` in support.
- Step 4: integrand `= (ρ_j ≥ 0)/((ω−Ω) > 0) =` POSITIVE everywhere ⇒ `P∫ > 0` ⇒ `Re Σ(ω_H3) > 0`. A discrete mode FAR ABOVE a continuum is repelled UPWARD (away from the weight below it).
- Step 5: `Re Σ(ω_H3) > 0 ⇒ m_H^dressed = m_H^bare + Re Σ > m_H^bare`. **Computed sign is POSITIVE** ⇒ `sign_verdict = FAIL` (the predicted direction was `Re Σ < 0`).

*Confirmed numerically*: `Re Σ(ω_H3) = +0.03596 > 0`. The plan's "amplitude-mode softening toward 2Δ" (`Re Σ < 0`) is the physics of a mode sitting **just above** the `2Δ` threshold being pulled DOWN — that is `ω_H2`'s situation (`ω_H2 = 1.410`, just below band-top `2Δ_B2 = 1.464`), NOT the `|S|²`-radial m_H carrier `ω_H3 = 11.465`, which sits a full order of magnitude above the entire continuum.

*Dual-prior re-allocation* (plan discriminator): SIGN=FAIL (`Re Σ > 0`) ⇒ **0.85 → Track B** — the continuum self-energy does NOT reproduce the residual; the `−5.36%` is a genuinely separate screening/effacement effect, not the `|S|²` amplitude-mode self-energy.

*Effacement distinction*: `Γ_eff = 0.99970 ⇒ (1−Γ_eff) = 3e-4 = 0.03%` — a DISTINCT quantity from the `5.36%` m_H residual (survey C-2/U-2). The gate's deliverable was whether the self-energy supplies the `5.36%`; it does not (it supplies `+0.31%` of the WRONG sign at the m_H carrier).

**Substrate-physics**: PHONONIC. The Higgs IS the `|S|²`-radial transverse fiber-embedding mode of the substrate order parameter; its dressed mass is the bare quartic PLUS the self-energy from decay into the substrate's own B2/B3 two-quasiparticle pair-breaking continuum. The flow is `D_K (0,0)-eigenvalues → bare quartic [the +5.36% overshoot] → Pekker-Varma continuum self-energy Re Σ → dressed m_H → PDG`. The substrate's verdict is unambiguous: the `|S|²` carrier `ω_H3 = 11.465` sits an order of magnitude ABOVE its own pair-breaking continuum (`2Δ_B2 = 1.464`), so the level repulsion is UPWARD (`Re Σ > 0`), the opposite of a softening. The amplitude-mode softening the bridge B-2 needs is a real substrate phenomenon — it is present at the Higgs-Leggett hybrid `ω_H2 = 1.410` (`Re Σ = −0.795 < 0`) which sits AT the continuum edge — but that is a different mode of the wrong magnitude. The `Γ_eff = 0.99970` effacement is a `0.03%` impedance quantity, structurally distinct from the `5.36%` residual; the residual is NOT this continuum self-energy.

**Solution-space**: bridge **B-2 corridor CLOSED** (plan `FAIL_meaning`). The `−5.36% = −67/1251` Higgs residual is NOT a Pekker-Varma continuum self-energy of the `|S|²`-radial mode; converting `Γ_eff` into a Landau amplitude-mode self-energy fails on SIGN at the m_H carrier. The residual remains a separate screening/effacement effect (C-2 NOT de-circularized via this route; U-2 NOT killed). This is a clean directional falsification, not an inconclusive result. CROSS-TRACK: any m_H residual re-tag touches the capstone / atlas-04 m_H claim — that prose-status reconciliation is the capstone-hygiene Q3 + designated-writer's domain (session-promotion), NOT an investigation edit; this gate COMPUTES `Re Σ` and emits the `inv5` verdict line ONLY. Feeds the **INV5-W3-3** 3-way Higgs-residual synthesis review (alongside W1-1 PS-quartic `+3.21 GeV` and W3-1 a₄-tail FAIL): all three INV5 Higgs-residual routes computed to date FAIL to derive the `+5.36%` — the residual's origin remains OPEN.

---

### §W2-4. INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the U(1)_7 Goldstone IS the phase boson of the substrate's broken-U(1)_7 sector; its mass is a spectral property of the (0,0)-sector phase dynamics)
**Gate type**: `compute`
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: the U(1)_7 Goldstone acquires a finite Imry-Ma / random-field mass `m_Goldstone² ~ 1/ξ_disorder²` with `ξ_disorder` set by the non-C² Josephson couplings (`J_su2=0.059`, `J_u1=0.038`); this mass is parametrically LARGER than the bare Leggett anchor (toward the structure-formation 170× `Δ_BCS`) WHILE staying below the pair-breaking edge (`ω_Goldstone/2Δ_BCS < 1`), preserving the below-edge protection the DM-survival argument (U-3) relies on.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w2.md` §W2-4 (two-condition AND inequality, ENHANCEMENT + PROTECTION boundaries; pre-registered Q3 GOLDSTONE-MASS-FROM-DISORDER).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- (1) **script** `computations/investigation-5/inv5_w2_4_goldstone_mass_disorder.py` — EXISTS (27764 B). `grep -E 'from canonical_constants import'` → `from canonical_constants import (  # noqa: E402`; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call in `main()`. ✓
- (2) **data** `computations/investigation-5/inv5_w2_4_goldstone_mass_disorder.npz` — EXISTS (24173 B). ✓
- (3) **plot** `computations/investigation-5/inv5_w2_4_goldstone_mass_disorder.png` — EXISTS (93353 B; two panels: LEG-1 enhancement bracket + LEG-2 below-edge bracket). ✓
- (4) **verdict line** `computations/investigation-5/inv5_gate_verdicts.txt` — `grep -E '^INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER:.* audit_sha256=[a-f0-9]{64}'` → matches `INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER: FAIL -- value='enh=0.0231|...' ... audit_sha256=630a025cb9...` + dual-SHA companion row + `[SIGN]` 3-tuple row. ✓
- (5) **this WP section** — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. ✓

**MCP Pre-Compute Audit** (queries run BEFORE writing the script; query-first discipline per `.claude/rules/epistemic-discipline.md`):
- `search_knowledge('Imry-Ma disorder Goldstone mass random field XY')` → no prior Imry-Ma-disorder Goldstone gate; surfaced the substrate disorder propagator `P(K)⁻¹ = J K² + m² + Σ(K)` (S50 landau-collab) and the dispersion `ω_G(k) = sqrt(J k² + m²)/sqrt(ρ_s)` (S48 tesla-collab) — the two equations the gate uses.
- `search_knowledge('Goldstone mass disorder Josephson coupling J_su2 J_u1')` → confirmed `J_u1=0.038, J_su2=0.059 (u(2) sector), J_C2=0.933 (coset)`; provenance `s48 goldstone_mass`, `s29b josephson_coupling`.
- `search_knowledge('Leggett channel anchor pair-breaking edge below-edge DM survival')` → C11 Leggett anchor `Mass_LeggettDM/Δ_BCS=11.97` (CONDITIONAL); `Ω_DM h²=0.120` Leggett-channel (0.6% Planck); below-edge survival is the U-3 protection.
- `trace_entity('GOLDSTONE-MASS-FROM-DISORDER')` → **NO trace** (gate is NEW — the pre-registered Q3, never run).
- `trace_entity('Imry-Ma disorder correlation length')` → **NO trace** (NEW mechanism).
- `get_constant('J_su2')` → **0.059** (canonical, matches seed).
- `get_constant('J_u1')` → **0.038** CANONICAL — the seed/survey "0.034" is STALE; `D_max = |log10(0.038) − log10(0.034)| = 0.0483 < 0.1` ⇒ SOURCE-RECON NO-ACTION band, BUT pinned the canonical 0.038 (canonical_constants is the import-target, not survey prose). Reconciliation recorded in `.npz` (`sourcerecon_J_u1_canonical/seed_stale/D_max`).
- `get_constant('omega_L1')` → **0.138** (bare Leggett-1 FREQUENCY anchor; distinct from the S49 DIPOLAR Goldstone MASS `m_L1=0.070`, reported as `enh_dipolar` alt-ratio in the .npz).
- `get_constant('Delta_BCS')` → **0.4642547394830737** (R-PROTECTED, S70); edge `2·Δ_BCS = 0.9285094789661474`.
- **Branch**: NOT pre-closed — the Imry-Ma disorder route is genuinely new. Adjacent PROVEN wall (cited, not re-derived): the **spectral-action Goldstone mass = 0 EXACTLY** (S48 GOLDSTONE-MASS-48 FAIL; `Tr[f(D(φ)²)] = Tr[f(D²)]` under unitary conjugation — wall #7). The SA cannot mass the Goldstone; this gate tests whether DISORDER (Imry-Ma), a different mechanism, can.

**Verdict**: **FAIL** (composite). 3-tuple: **sign=FAIL, magnitude=FAIL, regime=VALID**. The LEG-1 ENHANCEMENT prediction is contradicted by the substrate numbers — the Imry-Ma disorder mass is parametrically SMALLER than the bare Leggett anchor (`enhancement = 0.0231 ≪ 1`), so `sign_verdict=FAIL` collapses the composite to FAIL regardless of the protection leg. The corridor (bridge **B-4**: "non-C² disorder supplies a protected second DM-mass scale toward 170×") is **CLOSED** in the enhancement direction.

**Results**:

*Substrate inputs (canonical):* `ρ_s = 7.962` (s48 phase stiffness `rho_s_C2`); `J_C2 = 0.933` (C² coset, 4 bonds — ordered elastic backbone); `J_su2 = 0.059` (su(2), 3 bonds); `J_u1 = 0.038` (u(1), 1 bond, softest — CANONICAL); `ω_L1 = 0.138 M_KK` (bare Leggett-Goldstone FREQUENCY anchor); `Δ_BCS = 0.4642547 M_KK`; pair-breaking edge `2·Δ_BCS = 0.9285 M_KK`. PROVEN wall cited: SA Goldstone mass `= 0` EXACT (S48; so the bare mass is NOT spectral-action — Imry-Ma is the only candidate mechanism for a finite Goldstone gap).

*Random field from the non-C² Josephson couplings:* the C² coset (`J_C2=0.933`, 4 bonds) is the ORDERED elastic backbone; the non-C² directions (su(2) 3 bonds + u(1) 1 bond) ARE the random field. RMS random-field coupling `h_rf = sqrt(mean(0.059², 0.059², 0.059², 0.038²)) = 0.054514 M_KK`; spread `std(non-C²) = 0.009093 M_KK`.

*ξ_disorder (Larkin, CANONICAL construction A):* weak-disorder continuum RF formula `ξ_L = J_stiff / h_rf = 0.933 / 0.054514 = **17.115 bond units**` — a LONG correlation length because the ordered backbone is ~17× stiffer than the random field (the substrate is in the **weak-disorder regime**). Imry-Ma mass `m_Goldstone² = h_rf² / ξ_L² = 1.0145e-05 M_KK²` ⇒ `m_Goldstone = **0.003185 M_KK**`. Goldstone gap via the framework dispersion `ω_Goldstone = m_Goldstone / sqrt(ρ_s) = 0.003185 / sqrt(7.962) = **0.0011288 M_KK**`.

*The two pre-registered ratios (AND-verdict):*
- **(i) LEG-1 ENHANCEMENT** `m_Goldstone / m_L1_bare = 0.003185 / 0.138 = **0.02308**`. Required `> 1`. **FAILS** — the disorder mass is ~43× SMALLER than the bare anchor, not larger. (vs the S49 DIPOLAR mass anchor `m_L1=0.070`: `enh_dipolar = 0.0455`, also ≪ 1.) Fraction of the 170× structure mass reached: `4.04e-05`; fraction of the `170/11.97 = 14.20×` two-scale factor: `1.63e-03`.
- **(ii) LEG-2 PROTECTION** `x_Goldstone = ω_Goldstone / (2·Δ_BCS) = 0.0011288 / 0.9285 = **0.001216 < 1**`. **PASSES** — deeply below the pair-breaking edge (even further below than the bare L1 cross-check `x_L1 = 0.138/0.9285 = 0.148625`, matching the plan's 0.149 reference and confirming the bare mode is below-edge as the U-3 argument claims).

*Robustness bracket (five ξ_disorder constructions; the verdict is construction-robust):*

| construction | ξ (bond) | E_disorder | m_G (M_KK) | ω_G (M_KK) | enhancement | x_Goldstone |
|:---|---:|---:|---:|---:|---:|---:|
| **A_Larkin_weak (CANONICAL)** | 17.115 | 0.05451 | 0.003185 | 0.001129 | **0.0231** | 0.00122 |
| B_saturated_hrf (ξ=1, E=h_rf) | 1.000 | 0.05451 | 0.05451 | 0.01932 | 0.3950 | 0.02081 |
| C_saturated_Ju1 (ξ=1, E=J_u1) | 1.000 | 0.03800 | 0.03800 | 0.01347 | 0.2754 | 0.01450 |
| D_std_nonC2 (ξ=1, E=std) | 1.000 | 0.00909 | 0.00909 | 0.00322 | 0.0659 | 0.00347 |
| E_max_bond_J_C2 (ξ=1, E=J_C2; unphysical upper) | 1.000 | 0.93300 | 0.93300 | 0.33065 | 6.7609 | 0.35611 |

LEG-1 enhancement `< 1` for A, B, C, D — every substrate-natural construction. Only construction E (treating the *entire* bond network including the C² backbone as random field — physically unjustified: the backbone is the ORDER, not the disorder) clears `enhancement > 1`, reaching 6.76× — still an order of magnitude short of the 571.9× needed for 170×Δ_BCS, and even then `x_Goldstone = 0.356 < 1` (below-edge). LEG-2 PROTECTION holds in ALL five constructions.

*SIGN substitution chain (plan §W2-4 (7)) — read-off with substituted numbers:*
- LEG 1 predicted POSITIVE: `m_Goldstone − m_L1_bare = 0.003185 − 0.138 = −0.134775 < 0` → **NEGATIVE** (prediction CONTRADICTED). The plan's Step 4 took the Imry-Ma term `1/ξ_disorder² > 0` to imply `m_Goldstone > m_L1_bare`, but it added the disorder mass on top of a `m_bare²` it implicitly took as `ω_L1²`; the substrate's actual Imry-Ma contribution `c/ξ_disorder²` is ~0.0005% of `ω_L1²`, so it does NOT lift the mass above the bare frequency — the disorder term is real and positive but parametrically negligible against the bare anchor.
- LEG 2 predicted NEGATIVE: `x_Goldstone − 1 = 0.001216 − 1 = −0.998784 < 0` → **NEGATIVE** (prediction CONFIRMED, below-edge).
- Composite `sign_verdict = PASS iff BOTH legs hold` → LEG 1 FAIL ⇒ **sign_verdict = FAIL**.

*4-tuple:* `(value='enh=0.0231|x_G=0.0012|m_G=0.00319|xi_L=17.115|leg1=NEG|leg2_belowedge=True|frac170=4.036e-05', scheme=IMRY-MA-RANDOM-FIELD-GOLDSTONE-MASS, convention=DISORDER-LENGTH-FROM-NON-C2-JOSEPHSON-COUPLINGS, L_max=10)`.

*Dual-SHA:* `audit_sha256 = 630a025cb92246394f5347536874802ea800405ef171b24e3c497fc59866565a` (over [script, canonical_constants.py, pinmap of s48+s29b SHAs]); `content_sha256 = 4cb9f9f88da4d5ca542c7d155311f5d59a23ad1690085b4975d041455a2f05a4` (over [script]). 3-tuple companion row: `sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`.

*dual_prior re-allocation:* the discriminator routes **0.85 → Track B** ("the window is EMPTY"). The specific Track-B sub-reading realized is the FIRST disjunct: the disorder mass is **too small to matter** for the 170× shortfall (enhancement fails to reach the structure scale) — NOT the second disjunct (enhancement crosses the edge). So the 170× fix and the U-3 below-edge survival are NOT mutually exclusive *via this mechanism* — they simply do not meet, because the substrate's weak disorder gives a negligible Imry-Ma mass. The U-3 below-edge protection is INTACT (and reinforced: the disordered mode is even further below-edge than the bare mode), but bridge B-4 does NOT supply the second DM-mass scale.

*SOURCE-RECON record:* `J_u1` pinned CANONICAL **0.038** (seed/survey's 0.034 is STALE; `D_max = 0.0483 < 0.1` NO-ACTION band; recorded in `.npz`: `sourcerecon_J_u1_canonical=0.038`, `sourcerecon_J_u1_seed_stale=0.034`, `sourcerecon_D_max=0.0483`). The `ω_L1=0.138` FREQUENCY vs `m_L1=0.070` MASS distinction is flagged: BOTH ratios reported (`enhancement` against 0.138, `enh_dipolar` against 0.070); both `< 1`, so the verdict is invariant to the anchor choice.

*Artifacts:* `inv5_w2_4_goldstone_mass_disorder.py` / `.npz` / `.png`.

---

## Wave 2 Synthesis (team-lead)

Wave 2 tested condensed-matter functionals against three standing gaps. Four compute gates: **1 INFO (W2-1), 3 FAIL (W2-2, W2-3, W2-4)**. Three findings.

**Finding A — A_s retired to one number (W2-1 INFO).** The impulse-quench Bogoliubov functional collapses the historical A_s OOM self-disagreement (3.02 / 3.15 / 4.56 / 9.5) to one defensible value: **A_s = 1.54×10⁻⁸, +0.86 OOM**, by reading the *per-coherence-cell* frozen-mode occupation (k̂=53.3 M_KK, over the KZ volume ξ̂³) — NOT aggregating total occupation (which reproduces the +9.16-OOM wall). Bridge B-1 substantially confirmed: A_s is largely a normalization-scheme object. Routes to HY1 session-promotion.

**Finding B — the 170× DM-mass shortfall stays OPEN; both candidate routes fail, complementarily (W2-2 FAIL + W2-4 FAIL).** W2-2: the NSR pseudogap two-scale split *inverts* the expected ordering (Δ_pg=0.464 < D_s-scale m_Meissner=2.521; r=5.43 vs target 14.2) — the condensate is anomalously *phase-rigid* (Josephson f-sum-rule stiffness E_J=3.40 large), so the single-particle gap is the SMALLER scale and cannot supply the structure-formation factor; B-3 closed at the energy-scale level. W2-4: the Imry-Ma disorder Goldstone mass is ~43× SMALLER than the Leggett anchor (enhancement 0.023; weak-disorder regime, Larkin length 17 bond units); B-4-disorder closed. Both leave the abundance match (Ω_DM h²=0.120, Leggett anchor) intact and the below-edge protection (U-3) intact/reinforced. The 170× shortfall (G-2) is hardened as a genuine open gap with two specific corridors closed for *complementary* reasons (too phase-rigid vs too weakly disordered).

**Finding C — the m_H residual is NOT the Pekker-Varma self-energy (W2-3 FAIL).** Re Σ for the |S|² carrier ω_H3=11.465 is POSITIVE (+0.31%/m_H), target −5.36% with Re Σ<0 — the carrier sits an OOM ABOVE the B2/B3 continuum (band-top 1.464), so by Kramers-Kronig it is repelled UP, not softened. Bridge B-2 closed (clean directional falsification). Feeds the W3-3 review's SELF-ENERGY leg (FAIL).

### What Changed

#### (a) Numerical revisions
- A_s = 1.54×10⁻⁸ (+0.86 OOM, k̂=53.3 M_KK), replacing the 3.02/3.15/4.56/9.5 spread; W2-2 r_2scale=5.43 vs 14.2 (Δ_pg=0.464, m_Meissner=2.521); W2-4 enhancement=0.023 (Larkin 17 bonds); W2-3 Re Σ/m_H=+0.31% vs −5.36%.

#### (b) Structural changes
- **A_s OOM ambiguity → one number** (B-1 confirmed, A_s is normalization-scheme).
- **B-2 (Pekker-Varma) CLOSED on sign**; **B-3 (pseudogap two-scale) + B-4-disorder (Goldstone) both CLOSED** → 170× DM-mass shortfall **hardened-open** (abundance match + below-edge protection both intact).

### Effected In-Session (non-math)
None investigation-effectable — all session-track. Route to `/rclab-investigate --investigation 5`:
- [→investigate] **HY1** — pin the single A_s OOM number + k̂ + the K_pivot/deg(T_{BZ→pivot}) mapping (G-3) into `canonical_constants.py` (3 named quantities); any `falsifier-master-inventory.md` row is `mack`-sole-writer on session-promotion. (See CF-INV5-W2-A.)
- [→investigate] The 170× DM-mass shortfall is now a hardened open gap (two corridors closed) — a constraint-map note for the standing-gap register; not a re-tag.

## Carry-Forward Computations

### CF-INV5-W2-A — HY1: session-promote the single canonical A_s number (mack sole-writer for the falsifier row)
| Field | Spec |
|:------|:-----|
| **What** | Lift the single A_s OOM (+0.86, A_s=1.54e-8) + frozen k̂=53.3 M_KK + the k̂/k_pivot=3.72 → deg(T_{BZ→pivot}) mapping into `canonical_constants.py` (the HY1 three-named-quantity pin) on a session-track re-compute; `mack-cosmic-bridge` writes any `falsifier-master-inventory.md` row (sole-writer). |
| **Inputs** | `inv5_w2_1_as_impulse_quench.py`; xi_KZ_FW=0.0187601; A_s_Planck; the S100b box-delta sudden-limit |β_k|² spectrum. |
| **Gate** | one regulator-tagged A_s OOM reproduced on the session track + `update_constant` provenance; inventory row by mack. |
| **Effort** | ~0.5 wave-equiv (value computed; session-promotion + pin). |

(W2-2 / W2-3 / W2-4: corridors closed — the 170× DM-mass shortfall is a hardened open GAP, not a pinned next compute; both candidate mechanisms failed for complementary reasons, so there is no re-run CF. The B-3⊕B-4 "joint DM-mass closure" the plan pre-flagged does not apply — neither leg landed.)

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:---------|:-------|
| 2026-06-15 | A_s OOM self-disagreement (UB-3/UB-4) | 3.02/3.15/4.56/9.5-OOM spread | one number +0.86 OOM (B-1: A_s is normalization-scheme) | W2-1 impulse-quench per-coherence-cell occupation |
| 2026-06-15 | DM-mass scale via pseudogap two-scale (B-3) | candidate 170× route | CLOSED — ordering inverted (phase-rigid condensate) | W2-2 r=5.43 vs 14.2, Δ_pg < D_s-scale |
| 2026-06-15 | DM-mass scale via disorder Goldstone (B-4) | candidate 170× route | CLOSED — too weak (enhancement 0.023, weak-disorder) | W2-4 ~43× under anchor; below-edge protection reinforced |
| 2026-06-15 | 170× DM-mass shortfall (G-2) | open, two candidate corridors | hardened-open — both corridors closed; abundance + below-edge intact | W2-2 + W2-4 complementary FAILs |
| 2026-06-15 | m_H residual via Pekker-Varma self-energy (B-2) | candidate −5.36% screening | CLOSED on sign — Re Σ > 0 (mode above continuum) | W2-3 +0.31%/m_H, Kramers-Kronig repulsion-up |

## Files Produced

| Gate | Script (`computations/investigation-5/`) | Data | Plot | Verdict | audit_sha256 (head) |
|:-----|:------------------------------------------|:-----|:-----|:--------|:--------------------|
| INV5-W2-1 | inv5_w2_1_as_impulse_quench.py | ✓ | ✓ | INFO | 01da2112… |
| INV5-W2-2 | inv5_w2_2_nsr_pseudogap_two_scale.py | ✓ | ✓ | FAIL | cd6e2297… |
| INV5-W2-3 | inv5_w2_3_pekker_varma_higgs_self_energy.py | ✓ | ✓ | FAIL | d51071e0… |
| INV5-W2-4 | inv5_w2_4_goldstone_mass_disorder.py | ✓ | ✓ | FAIL | 630a025c… |

(Verdict ledger: `computations/investigation-5/inv5_gate_verdicts.txt`.)
