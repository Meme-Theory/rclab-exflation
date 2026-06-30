# Session 114 Wave 2 — Scale-Origin Deciders (KPIVOT / TAUFOLD / CCRESID) (Results Working Paper)

**Session**: 114 | **Wave**: 2 | **Plan**: session-114-plan-w2.md | **Theme**: scale-origin deciders — the three S113 EVOI-frontier workshop SYNTHESIS verdicts whose Reading-A-vs-Reading-B fork each reduces to exactly ONE pre-registered compute: KPIVOT (the BZ-edge → working-K* ratio-leg transport degree, OPEN factorization output, NOT the imported α_s/d_s +2), τ_fold (the van-Hove cusp-CROSSING location from-scratch with NO injected 0.190), CCRESID (the q-channel compressibility χ_q(τ) run-down vs fold-frozen). Three structurally-distinct sub-fields (KK fiber-integration / non-equilibrium transit-dynamics / superfluid q-thermodynamics), no cross-gate dependency, fully parallel.

## Gate Sections

### §W2-1. CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN (baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the BZ tessellation edge is a property of the D_K eigenvalue tiling on (A_K,H_K,D_K) at τ_fold — the fabric's own spectral geometry, not an excitation)
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: A `w(L_max)·κ(k)` factorization of the BZ-tessellation-edge → working-K* transfer (`R_BZ-edge=2.0 → K*≈0.0435 M_KK`, a 1.6625-decade even-sector leg) returns a substrate-natural EVEN transport degree — NOT the pre-imported α_s/d_s `+2` — whose bridge image lands K* inside the §VII L^{-α} envelope (Reading-A, ratio-to-K* leg ONLY); else an odd / non-even / scalar / non-convergent result is Reading-B on the ratio half.
**Plan reference**: `sessions/session-plan/session-114-plan-w2.md` §W2-1 (3-outcome verdict rubric, parity pre-flight, Wodzicki-degree-extraction method, FORBIDDEN-in-script foreclosure, substitution chain).
**Expected direction**: dual_prior leans Reading-B both halves (track_B = 0.70: 56-decade displacement + no extracted tessellation degree); the gate pre-registers all 3 outcomes — PASS (even degree + image lands K*) re-allocates 0.9 to Track-A on the ratio leg only.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

All five artifacts verified on disk by content (not line/byte count):

1. **script** `computations/session-114/s114_kpivot_edge_transfer_degree_open.py` (48,918 B) — `grep -E` confirms both must_contain patterns present: `from canonical_constants import (` (tau_fold, M_KK, planck_ns) and `def print_verdict_payload(`.
2. **data** `computations/session-114/s114_kpivot_edge_transfer_degree_open.npz` (15,341 B; 49 keys) — records `deg_extracted=0.0`, `deg_is_even=True`, `w_of_L` scan {5,8,10,12} = {0.8017, 0.9893, 0.9993, 1.0000}, `kappa_k` (81-pt L-independent kernel), `edge_ratio_per_L` / `cross_ratio_per_L`, `bridge_image=2.0`, `envelope_abs`, `lands_in_envelope=False`, `factorization_holds=False`, `decades_unaccounted=1.6625`, the EXCLUDED anti-rescue value `deg_T_BZ_pivot_NOT_imported=2.0`, and the 3-tuple verdicts.
3. **plot** `computations/session-114/s114_kpivot_edge_transfer_degree_open.png` (239,754 B) — 4 panels: (1) edge-transfer trace Tr^(L_max)(k); (2) w(L_max) pre-factor + k-shape invariance; (3) degree-extraction (edge same-pole vs cross-pole probe L_max flow); (4) bridge-image-vs-§VII-envelope + verdict summary.
4. **verdict_line** `computations/session-114/s114_gate_verdicts.txt` — canonical line matches `^CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=3c12c706...951a`); dual-SHA companion row + schema-v2 [SIGN] 3-tuple row present; 4 extra companion rows (anti-rescue, regulator-pin, parity-pre-flight, Reading-B). Emitted via the race-safe `emit_verdict` knowledge-MCP tool (7 rows, sig_5-unique, cross-process-locked).
5. **wp_section** this §W2-1 (Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit all present).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("KPIVOT BZ tessellation edge transfer K* transport degree")` → returned `constants:deg_T_BZ_pivot --derived_from--> sessions:93 / sessions:110` with provenance "BZ→CMB-pivot transport homogeneity degree, DERIVED ONCE on the M4 base (**dedup flag iii**)"; gate `S93-W7-1-...-BZ-PIVOT` PASS `value='...deg_T=2.0000...reading=T...'`; equation `O^pivot=O^substrate IFF deg(T) is T2-VACUOUS`. **Confirms the +2 is the α_s/d_s morphism degree on the M4 base — the value I must NOT import.**
- `trace_entity("CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN")` → "No trace found" — **the gate is not yet computed/closed** (not a re-derivation of a settled result).
- `get_constant("deg_T_BZ_pivot")` → `2.0`, S110, source `S110-CF-CV6B-DS-M4`, NOT superseded — the canonical (FORBIDDEN-to-import) value; recorded in the npz ONLY as the EXCLUDED anti-rescue value `deg_T_BZ_pivot_NOT_imported=2.0`.
- `get_constant("M_KK")` → `7.428660036284456e16` GeV (S42, CONST-FREEZE-42) — used for the scale framing only.

**Not PRE-CLOSED**: the §VII KPIVOT verdict (`ws-s113-1-kpivot-verdict.md §4.2`) explicitly pre-registered this gate as the ONE surviving degree-OPEN forward compute on the C2-ratio object; its three outcomes were left open. The α_s/d_s degree (`S93-W7-1`) is a structurally-distinct observable (two-pole running on the M4 base, not the tessellation scale-ratio) — importing it would be the dedup-flag-iii category error per `cross-pillar-bridge-corpus.md §23.0(5)`.

**Verdict**: **INFO** (composite) — `sign_verdict=PASS` / `magnitude_verdict=INFO` / `regime_verdict=VALID`.

The factorization extracted an **EVEN** transport degree (`deg(T_{BZ→K*}) = 0`, parity-consistent with `d_A=0`) — so NOT the FAIL parity branch, and NOT the SCALAR-windowed-trace FAIL branch (`factorization_holds=False`). But the bridge image of `R_BZ-edge` under the extracted degree is `R_BZ-edge=2.0` itself, which does NOT land `K*=0.0435` within the §VII `L^{-4}` envelope (residual `1.96` vs envelope `2.10e-06`; `1.6625` decades unaccounted). This is exactly the pre-registered INFO branch (plan §W2-1: "even degree extracted BUT bridge image does NOT land within the envelope"): the transport degree exists and is parity-correct, but its image does not reproduce the working pivot — neither a clean Reading-A nor a clean Reading-B on the ratio leg. The degree extraction SUCCEEDED (not a FAIL); the envelope shortfall is documented as a diagnostic.

**Solution-space**: the C2-ratio object's substrate-derivability is **partial** — a substrate-natural even transport degree (0) exists for the BZ-edge → K* leg, but it is the *trivial* (dimensionless-ratio-preserving) degree, which by the multiplicative-normalization cancellation theorem (`math-scripts.md` MANDATORY K=3) cannot SELECT which O(1) ratio hits K*. The `1.6625`-decade contraction is unaccounted. This is **NOT a §23 K=3 advancement** (a degree exists but is trivial-on-the-ratio — it does not carry an independent contraction). The dual-prior allocation is the INFO hybrid (the ~0.10 residual mass, plan line 232): track-allocation unchanged, envelope-shortfall documented. The K_pivot `M_KK^1` magnitude (C2-mag, parity-locked external) and the edge=pivot identification (C2-id, closed-negative) are untouched.

**Results**:

*Governing structure (structure-first).* The substrate IS the D_K eigenvalue tiling on the spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` at τ_fold=0.19 (90 Peter-Weyl (p,q) sectors at L=12; 166,896 eigenvalues with multiplicity). The BZ tessellation **edge** `R_BZ-edge = K_BZ/M_KK = 2.0` (d_A=0, dimensionless; verdict §2 table, log₁₀=+0.3010) is a property of that tiling. The working CMB pivot `K* = 0.0435 M_KK` (n_s=0.965 back-solve; log₁₀=−1.3615) is a laboratory-IN observable. The bridge object is the transfer `T_{BZ→K*}` (a 1.6625-decade contraction). The gate EXTRACTS `deg(T_{BZ→K*})` by a `w(L_max)·κ(k)` factorization (the S93-W7-1 METHOD route; its `deg_T=2.0` value NOT consumed).

*Extracted transport degree (OPEN OUTPUT).* `deg(T_{BZ→K*}) = +0` — **EVEN** (parity-consistent with d_A=0). The edge transfer `R_BZ-edge = K_BZ/M_KK` is a **same-pole** object (numerator K_BZ and denominator M_KK both at the BZ-edge scale pole s_edge=1, the a₂-channel 2nd-moment), so `deg = 2·(s_edge − s_edge) = 0` (Sage RealField(200)-verified). Extraction corroborated two independent ways: (i) the same-pole moment ratio M(s_edge)/M(s_edge) is L_max-FLAT (`edge_rel_spread = 0.000e+00` across {5,8,10,12}), confirming same-pole; (ii) a genuine cross-pole probe M(s_edge+1)/M(s_edge) DOES flow (`cross_rel_spread = 2.542`, values 0.2803→0.0791), confirming the diagnostic distinguishes same-pole (deg 0) from cross-pole (deg even ≠ 0). The +2 α_s/d_s degree was NEVER substituted (recorded only as the EXCLUDED anti-rescue value).

*Factorization (windowed trace).* `factorization_holds = False` (NON-scalar): the edge-window trace `Tr^(L_max)(k) = Σ m_k |λ|^{-2s_edge} e^{-(k|λ|)²}` has an L_max-DEPENDENT k-shape (k-shape max rel-dev = 9.42e-01 ≫ 1e-9; D2(k) L_max-invariance max|ΔD2| = 4.80 ≫ 1e-9). The w(L_max) multiplicative pre-factor scan: {L=5: 0.8017, L=8: 0.9893, L=10: 0.9993, L=12: 1.0000} (κ(k) = Tr^(L=12)(k), L-independent kernel by construction). Note the distinction between the *windowed trace* (NON-scalar k-structure) and the *transfer-object degree* (0, same-pole) — they are different quantities; the regime_verdict=VALID keys on the former.

*Bridge image vs §VII envelope.* A deg-0 transport is the IDENTITY on the dimensionless ratio (Sage: same-pole ratio = 1, w(L_max) cancels). Its image of R_BZ-edge is R_BZ-edge = 2.0, unchanged; per the multiplicative-normalization cancellation theorem a dimensionless transport degree cancels in every ratio and cannot SELECT which O(1) ratio hits K*. Residual `|image − K*| = 1.96` vs §VII envelope (L^{-4}·|K*| = 2.10e-06) ⇒ `lands_in_envelope = False`; `decades_unaccounted = 1.6625` (= the full contraction).

*Substitution chain (numbers substituted).* PARITY leg: every substrate-natural operation on (A_K,H_K,D_K) carries degree −2·(integer pole difference), EVEN because the d=8 dimension spectrum is integer (Sage-verified: single Wodzicki residue −2s; same-class two-pole ratio −2(s−s′); HKR ratio 0; all even); extracted deg 0 ∈ even integers ⇒ parity PASS. CONTRACTION leg: log₁₀(2.0/0.0435) = `1.6625407387093439` (Sage RealField(200) exact) > 0 ⇒ the transfer is a contraction. PARITY pre-flight d_A(R_BZ-edge)=0 ⇒ EVEN-morphism sector required; an ODD degree would be scale-leg contamination ⇒ parity-FAIL (not triggered: deg 0 even).

*Mult-norm-cancellation pre-flight.* The PASS criterion targets the asymptote/plateau DEGREE value (extracted = 0), NOT the L_max-stability per se — consistent with `math-scripts.md §"Multiplicative-normalization cancellation invariants"` (the w(L_max) leg is annihilated by any K-dependent log-derivative; the plateau is structural, and the discriminating content is the extracted degree).

*4-tuple*: `(value=deg_extracted=0 [INFO], scheme=WODZICKI-DEGREE-EXTRACTION-OPEN-OUTPUT, convention=TRANSPORT-DEGREE-OPEN-da0-EVEN-MORPHISM-SECTOR, L_max=12)`.

*FORBIDDEN-in-script confirmation*: `deg_T_BZ_pivot=2.0` does NOT appear as an imported target / expected value / hard-coded degree anywhere in the producing script — it is referenced ONLY as the EXCLUDED anti-rescue value (`deg_T_BZ_pivot_NOT_imported=2.0` npz key + the docstring anti-rescue fence). The audit_sha256 pins `s93_w7_1_alpha_s_w_kappa_factorization_deg_transport.py` as a METHOD reference (its degree value not consumed).

*Dual-SHA*: `audit_sha256=3c12c706f3b3c0784de76953f82a47107624b2a339fb62d3feeded8a16c1951a` (over [script, canonical_constants, dirac_spectrum_module, s93_w7_1_method_reference, pinmap]); `content_sha256=114763915d3ffe2129a43ae1f00fddcb36404923ab9f79df7ef3dec9ddec9cdb` (over [script]).

*Artifacts*: `computations/session-114/s114_kpivot_edge_transfer_degree_open.{py,npz,png}`.

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`): GEOMETRIC. The substrate IS the D_K eigenvalue tiling; R_BZ-edge=2.0 is the geometric edge of that tiling, not a measurement IN a container. Direction preserved: D_K eigenvalues → spectral-triple tiling → bridge-map transport → emergent pivot read-off; never inverted to "the pivot is fundamental and the edge derived." The gate credits the substrate with exactly what the factorization earns — a parity-correct even transport degree (0) IS extractable — but the data does not force more: the deg-0 morphism is trivial-on-the-ratio and supplies no contraction to K*, so the working-pivot identification remains a fit, consistent with the §VII KPIVOT verdict's Reading-B lean on the ratio half (sharpened here to "an even transport degree exists but is trivial-on-the-ratio; the contraction is unaccounted").

---

### §W2-2. CF-S114-TAUFOLD-CUSP-CROSSING (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S114-TAUFOLD-CUSP-CROSSING`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (Level-2 moduli-deformation substrate-IS: the cusp-crossing location is a property of the Jensen TT-deformation manifold {D_K(τ)}, the substrate's own deformation parameter)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The van Hove cusp-CROSSING location (the flank `dS/dτ ≠ 0` supersonic point, distinct from the DOS-peak at 0.221), computed from-scratch on a τ-grid bracketing [0.18,0.23] with NO injected 0.190 at L_max ∈ {5,8,10,12}, is L_max-MONOTONE-CONVERGENT toward 0.190 within the Friedrich-Bär saturation band (Reading-A: τ_fold van-Hove-SELECTED); else it does not converge to 0.190 / stays at the 0.221 peak / remains mesh-dependent (Reading-B: τ_fold an imported flank-point).
**Plan reference**: `sessions/session-plan/session-114-plan-w2.md` §W2-2 (3-outcome SATURATION-LIMIT + MONOTONE-TREND rubric, the NO-INJECTED-0.190 load-bearing pre-registration, crossing-vs-peak distinction, substitution chain).
**Expected direction**: dual_prior leans Reading-B (track_B = 0.58: only the cusp's EXISTENCE is L_max-robust, the LOCATION moves with the regulator on the 3 existing data points); transit pole R2 lean is Reading-A (0.42). The attractor/EOM reading is DEAD by both poles. Decide on the saturation-limit + monotone-trend, NOT a mixed-L per-point tally.

**Verdict**: **INFO** (composite, schema-v2 3-tuple collapse). 3-tuple: `sign_verdict=PASS` (convergence-direction near the fold, NOT the 0.221 DOS-peak — the crossing is 30× closer to 0.190 than the peak), `magnitude_verdict=INFO` (|τ_cross(sat) − 0.190| = 0.5464%, just OUTSIDE the ±0.5% PASS band), `regime_verdict=VALID` (Friedrich-Bär-saturated, breach_frac = 0, mesh-robust). Composite collapse `magnitude=INFO ⇒ composite=INFO`. This is the plan's **INFO_meaning HYBRID**: the cusp-crossing REGION is van-Hove-SELECTED (the substrate genuinely carries a band-edge anticrossing near τ ≈ 0.19), but the precise canonical 0.190 is a flank-sub-choice within the substrate-pinned window — strictly stronger than the M_KK external-import (M_KK has no van-Hove analog), strictly weaker than full value-selection (0.190 to ±0.5%).

**Numbers** (from `s114_taufold_cusp_crossing.runlog` / `.npz`):

| Observable | Value | Notes |
|:-----------|:------|:------|
| `τ_cross(L=5)` | **0.191038** | from-scratch, NO 0.190 injected |
| `τ_cross(L=8)` | **0.191038** | identical (sector-local ⇒ L-invariant) |
| `τ_cross(L=10)` | **0.191038** | identical |
| `τ_cross(L=12)` (saturation) | **0.191038** | gap_min = 8.495e-06 |
| alt-mesh (1e-4 step, re-bracketed around L12) | **0.191039** | mesh-robust (Δ = 1e-6) |
| `\|τ_cross(sat) − 0.190\|` | **0.001038** (rel **0.5464%**) | PASS band = 0.00095 (±0.5%); INFO |
| Friedrich-Bär band half-width \|L12−L10\| | **0.0** | coarse-L breach_frac = 0/4 |
| DOS-peak (S85 L=8 canonical, CONTRAST) | **0.221** | DISTINCT functional; \|0.221−0.190\| = 0.031 |
| DOS-shape low-L_dos=4 peak (diagnostic) | 0.182 | L-truncation-sensitive; NOT the S85 value |
| L12-cache overlap at τ=0.19 | T3_max=0.971408, T5_min=0.972246, gap=8.387e-04 | `truncation_consistent=True` (\|dT3\|=0, \|dT5\|=2.2e-16) |

**Substitution chain** (substituted numbers, per plan §W2-2 + `math-scripts.md §"Double-Check Logic"`):

- **Step 1 (crossing observable, from-scratch)**: `Δ_band(τ) = |T5_min(τ) − T3_max(τ)|`, T3 = (0,0)-sector MAX |λ|, T5 = (2,0)/(0,2)-sector MIN |λ| (S44/S45 anticrossing pair; atlas-07 "[NEW S45] Van Hove TRUE crossing T3-T5"). `τ_cross = argmin_τ Δ_band`. **0.190 is NOT supplied to the finder** — the grid brackets [0.18,0.23]; the argmin returns 0.191038.
- **Step 2 (anticrossing confirmed)**: T3_max RISES with τ (0.185→0.20: 0.968→0.978), T5_min FALLS (0.9729→0.9710); they cross at τ≈0.191 where the gap dips to 3.27e-5 — a genuine band-edge anticrossing, gap between DISTINCT magnitudes (no spurious conjugate-pair zero, since the (2,0)/(0,2) degeneracy is compared against the DIFFERENT (0,0) edge).
- **Step 3 (crossing ≠ peak)**: the cusp-crossing (band-edge anticrossing, where the monotone flow crosses the non-analytic threshold) is a DISTINCT functional from the DOS-peak (argmax of singularity STRENGTH, |dλ/dτ|→∞). Computed: crossing = 0.191, DOS-peak = 0.221 (S85 canonical). The monotone S(τ) (dS/dτ = +58672.8 > 0, empty critical set — S95 NO-WELL-ONE-LOOP) keeps FLOWING through the crossing; the cusp lives in ρ(λ;τ), not as a critical point of S.
- **Step 4 (L-invariance, sector-locality)**: T3/T5 sectors satisfy p+q ≤ 2, so they ARE the bottom band at every L_max ≥ 2; higher sectors have |λ|_min ~ √C₂ climbing away ((3,0) min = 1.248 ≫ the |λ|~0.97 crossing cluster, L12-cache-confirmed). ⇒ `τ_cross(L)` is identical to float precision across {5,8,10,12} — the crossing is L_max-saturated **by sector-locality**, the strongest form of Friedrich-Bär saturation. A flat trend is the saturation-PASS reading of the sign criterion (already_saturated, breach_frac=0), NOT a null result.
- **Step 5 (direction)**: sign=PASS (τ_cross = 0.191 < midpoint(0.190, 0.221) = 0.2055 ⇒ near the fold, not the peak; monotone/saturated within FB band). magnitude=INFO (0.5464% > 0.5%, but τ_cross ∈ [0.190, 0.221]). regime=VALID (saturation L's {10,12} agree exactly; mesh-robust). **Conclusion: the substrate's OWN ρ(λ;τ) selects a van-Hove crossing REGION near τ=0.19; the precise 0.190 is a sub-choice within it.**

**Anti-rescue fence (load-bearing, honored)**: 0.190 appears in the script ONLY as the POST-HOC comparison target `TAU_FOLD_CANON = float(tau_fold)` read AFTER the finder returns, and as the 0.221-vs-0.190 contrast reference. It is NEVER a cusp-finder seed/target/initial-guess. The τ-grid `np.linspace(0.18, 0.23, …)` brackets the region; the argmin band-edge finder + the alt-mesh re-bracket (centered on the from-scratch L12 result, NOT 0.190/0.191) return the value independently. Confirmed by the verdict NOT landing exactly on 0.190 (it lands on the substrate's own 0.191038 = the S45 TRUE crossing), the signature of a from-scratch finder rather than the S85-W10 `value='promoted'` import.

**Solution-space**: τ_fold's status moves from "imported flank-point" toward **region-selected, precise-value-conditional** (the INFO_meaning hybrid). The capstone §6.3 / atlas-04 A4 prose tag should read "τ_fold REGION van-Hove-selected (the substrate carries the band-edge anticrossing); precise value 0.190 a flank-sub-choice within the ±0.5%+ window — CONDITIONAL." The cusp-region localization (the crossing is a real substrate feature, M_KK has no analog) is the surviving substrate refinement. Reading-A (full van-Hove value-selection to ±0.5%) is NOT reached; Reading-B (irreducible-empirical-modulus, location regulator-conditional) is REFUTED — the location is L_max-INVARIANT (regulator-robust), not regulator-conditional. The dual-prior INFO branch (hybrid window) realizes.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — verified on disk by content-presence regex, NOT line/byte counts):

1. **script** `computations/session-114/s114_taufold_cusp_crossing.py` (48 KB) — `grep -E` PASS:
   - `from canonical_constants import` → `from canonical_constants import *` + `from canonical_constants import tau_fold, dS_fold, d2S_fold, S_fold`
   - `print_verdict_payload` → `def print_verdict_payload(...)` + called in `main()`
2. **data** `computations/session-114/s114_taufold_cusp_crossing.npz` (18 KB) — records `tau_cross_by_L` [L∈{5,8,10,12}], `alt_mesh_cross`, `dos_peak_canonical=0.221` (contrast), `dos_peak_lowL_shape` (diagnostic), `fb_halfwidth`/`sat_band`, `dev_sat`/`rel_dev_sat`, `monotone_converging`/`already_saturated`/`mesh_robust`/`breach_frac`, `truncation_consistent`, the 3-tuple verdicts, dual-SHA.
3. **plot** `computations/session-114/s114_taufold_cusp_crossing.png` (160 KB) — (a) band-edge gap V-curves per L_max; (b) τ_cross(L) convergence trend vs L_max + FB band + 0.190 + 0.221 + S45 0.19104; (c) DOS singularity-strength shape (L≤4) vs crossing + S85 peak; (d) T3/T5 band-edge anticrossing at L=12.
4. **verdict_line** `computations/session-114/s114_gate_verdicts.txt` — matches `^CF-S114-TAUFOLD-CUSP-CROSSING:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=7b637db142d9bea7…`), WITH dual-SHA companion row + schema_v2 [SIGN] 3-tuple row + 2 extra companion rows (DOS-peak contrast SHA + truncation_consistent). Emitted via the race-safe `emit_verdict` knowledge-MCP tool (5 rows; sig_5 unique).
5. **wp_section** this §W2-2 (Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit present).

4-tuple: `(value=0.19103812125290104, scheme=VAN-HOVE-CUSP-CROSSING-FROM-SCRATCH-NO-INJECTED-0.190, convention=FLANK-dSdtau-NONZERO-CROSSING-not-DOS-PEAK, L_max=12)`.

**Dual-SHA**: `audit_sha256 = 7b637db142d9bea7da77be5cf4cfc49b486f65aa3a39f59c197ba0fb3ff43b09` (over [script, canonical_constants, dirac_spectrum_module, s84_spectrum_cache_L12, pinmap]); `content_sha256 = ab6f935ccc431c56e6ad4771eae4280abbd19529c06ccfaf47d967dc5f649d8f` (over [script]). **Runtime-SHA note**: the `canonical_constants.py` SHA captured at runtime is `a4b8b679…`, differing from the plan-pinned `9ee1a113…` because a sibling S114 gate promoted a constant mid-session — captured as RUNTIME state per `substrate-first-canonical-sourcing.md §(ii.B)` (audit-correct, NOT an error; `tau_fold = 0.19` unchanged). audit_sha256 is unique in the verdict file (sig_5 clear).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed before/at compute, salient returns):

- `get_constant("tau_fold")` → **0.19** (S12/S42, gate CONST-FREEZE-42, source `s42_constants_snapshot.npz`, NOT superseded) — the canonical post-hoc comparison target.
- `search_knowledge("van Hove cusp tau_fold crossing 0.190 0.221 DOS peak")` → `S85-VAN-HOVE-CUSP-THEOREM: FAIL value=0.221 L_max=8` (the DOS-peak, distinct functional, CONTRAST reference); `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM: PASS value='promoted' convention=canonical_constants-S85-freeze L_max=10` (confirms the prior PASS **IMPORTED** 0.190 — frozen, not from-scratch); theorem "tau_fold = 0.190 PERMANENT van-Hove-cusp non-stationarity uniqueness theorem" (PROVEN, S85, §VII.M.W10-3, the non-stationarity/DOS-peak side).
- **NOT PRE-CLOSED**: no prior gate locates the cusp-CROSSING (band-edge anticrossing) from-scratch at saturation L_max. S85-W10 imported 0.190 (`value='promoted'`); S85-VAN-HOVE is the DOS-PEAK (0.221, distinct functional); S84-ALTERNATIVE-TAU-MESH returned `value=0` at L=5. This gate is genuinely new: a from-scratch crossing-location compute with NO injected 0.190, distinguishing the crossing (0.191) from the peak (0.221).

---

### §W2-3. CF-S114-CCRESID-CHI-Q-SCALING (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S114-CCRESID-CHI-Q-SCALING`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (χ_q = d²ε/dq² is the q-departure / Gibbs–Duhem compressibility — a thermodynamic response of the substrate's q-channel excitation spectrum)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: The q-channel compressibility χ_q(τ), computed first-principles from the D_K spectrum across the Jensen family, either RUNS the required ~118.71 OOM fold→today AND `ρ_m,today²/χ_q` reproduces the residual fraction 0.032 ± 0.005 (Reading-A: channel-internal closure real) — OR is fold-frozen (χ_q ~ S_fold, ΔS/S = 2.2%, runs <10 OOM; Reading-B: the standing-limitation verdict confirmed on channel-internal grounds).
**Plan reference**: `sessions/session-plan/session-114-plan-w2.md` §W2-3 (3-outcome run-down OOM fork + RATIO-on-0.032 magnitude rubric, a₀-channel `regulator_pin`, the χ_q ~ S_fold structural argument, substitution chain).
**Expected direction**: dual_prior leans Reading-B (track_B = 0.75: S43 dead-end has a normal vector, S99 PROVEN-corridor, χ_q ~ S_fold; the structurally-expected outcome). The verdict-rubric "PASS-of-limitation" (Reading-B confirmed) collapses to composite FAIL-of-closure; INFO is the 10≤OOM<100 quantified-shortfall branch (~0.05 mass). The τ-scan leg ALONE settles the crux (per WS-3 §4.2) if the C1 substrate→a(t) map is unavailable.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| # | Artifact | Path | must_contain check |
|:--|:---------|:-----|:-------------------|
| 1 | script | `computations/session-114/s114_ccresid_chi_q_scaling.py` | `from canonical_constants import` ✓; `print_verdict_payload` ✓ (def + call) |
| 2 | data | `computations/session-114/s114_ccresid_chi_q_scaling.npz` | present (33 keys: χ_q(τ) tau-scan, OOM_rundown_required/available, computed_frac, mag_ratio, chi_q_over_S_fold/d2S, S_spread_frac) ✓ |
| 3 | plot | `computations/session-114/s114_ccresid_chi_q_scaling.png` | present (panel a: χ_q(τ) τ-scan vs χ_q~S_fold band; panel b: run-down available vs required, log scale) ✓ |
| 4 | verdict_line | `computations/session-114/s114_gate_verdicts.txt` | `^CF-S114-CCRESID-CHI-Q-SCALING:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion + schema_v2 3-tuple + a₀-channel regulator_pin row (4 rows via emit_verdict, race-safe) |
| 5 | wp_section | this §W2-3 | Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit ✓ |

Verification by content-presence (grep), not line/byte counts. All five artifacts on disk; grep output pasted in the executor's final message.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; query-first discipline):
- `search_knowledge("chi_q compressibility q-channel CCRESID residual fold-frozen S_fold")` → returned the `Λ_residual = ρ_m²/χ_q (A.3.1)` closure equation (Paper 15 / S43; `χ_q = 300,338 M_KK⁴`), the `Λ_eff = (1/2χ_q)·(δq)²` q-theory residual form (S56), and `ρ_Λ = ρ_m²/χ_q = 1.57e-167 GeV⁴` (S43). Confirms the closure formula + the χ_q-dead-end structural argument; the τ-scan first-principles compute is NEW.
- `trace_entity("chi_q fold-frozen S_fold q-channel run-down")` → no trace (the run-down-vs-fold-frozen fork is the new question this gate adjudicates; NOT pre-closed).
- `get_constant("S_fold")` → 250360.67696101 (S42 s42_gradient_stiffness) — the χ_q ~ S_fold anchor.
- `get_constant("Omega_m")` → 0.315 (Planck 2018); `get_constant("rho_Lambda_obs")` → 2.7e-47 GeV⁴ (Planck 2018, S42); `get_constant("M_KK")` → 7.428660036284456e16 GeV.
- `get_constant("chi_q_fold")` → NOT FOUND at dispatch (session-source pin S43 TWOFLUID-W-43-V2; cited S43, did NOT hardcode placeholder per `substrate-first-canonical-sourcing.md` Class-(f)). **Promoted to canonical** on first use via `update_constant("chi_q_fold", 300338.0, S114, …)` — single-call FIX-IN-SESSION per `math-scripts.md §"Canonical Write-Order"` (no sub-keying ambiguity), warranted as this gate's run-down anchor.
- **NOT PRE-CLOSED**: the closure formula and χ_q-dead-end are known, but the first-principles χ_q(τ) τ-scan run-down test against the 118.71 OOM target is the new adjudication.

**Verdict**: **FAIL** — composite FAIL-of-closure = Reading-B / PASS-of-limitation **CONFIRMED**. `value = 0.0185` (OOM run-down available, fold→edge). 3-tuple: `sign_verdict=PASS` (fold-frozen direction predicted AND observed), `magnitude_verdict=FAIL` (RATIO=1.0 ≫ 0.156 band), `regime_verdict=VALID` (run-down cleanly in the <10-OOM fold-frozen branch). Composite collapse: `magnitude=FAIL ∧ regime=VALID ⇒ FAIL` (`gate-verdicts.md` collapse rule). `audit_sha256=e988a329b1ff7b3e8f0ff1073b901719b4475d95a0b2d5880d3afded7d0a06d6`, `content_sha256=d93260484be16b0bbf3a3469c1371e59e36e181b19b6b52b93753056d5ceb4d3`.

**Results**:

**Substrate framing (PHONONIC).** The substrate IS the q-channel excitation spectrum. χ_q = d²ε/dq² is the q-departure / Gibbs–Duhem compressibility — the curvature of the proper vacuum energy `ρ_vac = (1/V)⟨H − Σμ_a N_a⟩` about equilibrium (Volovik Paper 04 §III–IV, `04_2005_Volovik_Vacuum_Energy_Cosmological_Constant.md`). The residual `ρ_vac/ρ_obs − 1 = 0.032` is NOT an a₀-magnitude offset: the a₀ count `ζ_{D_K}(0)=6440` does NOT gravitate at equilibrium (Paper 04 §IV: `ρ_vac = −P_vac = 0`, trans-/sub-Planckian cancellation, no fine-tuning). What gravitates is the q-departure `ρ_vac = ε(q) − q·dε/dq` — the a₀-channel object, a DIFFERENT functional of the spectrum than the bare count. Direction preserved: D_K eigenvalues → grand potential ε(q) → χ_q = d²ε/dq² → q-departure residual → emergent ρ_vac.

**LEG 0 — first-principles χ_q(τ) τ-scan (the decisive leg).** χ_q(τ) = d²S/dτ² is identified with the vacuum-modulus stiffness (Volovik Paper 15/35 q-theory; S43 TWOFLUID-W-43-V2 defines `χ_q = d²S/dτ² = 300,338 M_KK⁴` at the fold). The τ-scan reads `d2S_dtau2(τ)` and `S_total(τ)` first-principles from the S42 gradient-stiffness spectral-action data (both computed FROM the D_K spectrum at each Jensen deformation τ) on the Jensen τ-grid `[0.05, 0.1, 0.13, 0.15, 0.17, 0.19, 0.20, 0.22, 0.25, 0.30]`:

| Quantity | Value |
|:---------|:------|
| χ_q(τ) = d²S/dτ² range across the FULL Jensen family | min 304,605 → max 329,626 M_KK⁴ (fold 317,863) |
| χ_q full-family fractional spread | **7.87 %** |
| χ_q full-family OOM run-down (log₁₀ max/min) | **0.0343** (sub-decade) |
| χ_q fold→edge OOM run-down (reported `value`) | **0.0185** |
| S(τ) fractional spread (the ΔS/S argument) | 5.41 % (cf. cited 2.2 %) |

χ_q does NOT run with τ. The grand-potential curvature is a near-invariant of the spectral structure across the entire deformation family — sub-decade, no mechanism for any large run-down. **This is Reading-B (fold-frozen), confirmed first-principles.**

**Structural cross-check — χ_q ~ S_fold.** `χ_q(fold)/d2S_fold = 0.9449` (near unity — χ_q IS the spectral-action curvature, by construction) and `χ_q(fold)/S_fold = 1.1996` (same order, O(1)). The S43 χ_q anchor is consistent with the canonical `d2S_fold = 317,863 M_KK⁴` to within ~5.5 %. The S97 W2-2 grand-potential curvature `k_curv = +3586.53 M_KK` is reported as a cross-check ONLY — it uses a DIFFERENT q-variable normalization (the de Sitter/Hubble-coupled departure `dq/dH = 0.15`, M_KK units) than the S43 dimensionless-τ normalization (M_KK⁴); both are q-channel responses but are not numerically interchangeable. The run-down test uses the S43 fold anchor, per plan.

**LEG 1 — RUN-DOWN (substitution chain, Sage RealField(200) verified at plan-freeze).** For channel-internal closure `Λ_residual = ρ_m²/χ_q` (Paper 15 / S43 A.3.1) to reproduce `0.032·ρ_obs`:
- `χ_q(fold) = 300,338 M_KK⁴ = 9.1464e72 GeV⁴` [S43 anchor, at M_KK_gravity = 7.42866e16 GeV]
- `ρ_m,today = Ω_m·ρ_crit = 0.315·(ρ_obs/Ω_Λ) = 0.315·(2.7e-47/0.685) = 1.2416e-47 GeV⁴` (self-consistent ρ_crit common to ρ_obs)
- `χ_q,today-NEEDED = ρ_m,today²/(0.032·ρ_obs) = 1.7842e-46 GeV⁴`
- **`OOM_rundown REQUIRED = log₁₀(9.1464e72 / 1.7842e-46) = 118.71`** (Sage-exact 118.7098; matches plan)
- **`OOM_rundown AVAILABLE = 0.0185`** (χ_q ~ S_fold, fold-frozen)
- **SHORTFALL = 118.69 OOM.**

The run-down required exceeds the run-down the substrate supplies by **118.69 orders of magnitude**. `0.0185 < 10` (the fold-frozen ceiling) → Reading-B branch.

**LEG 2 — MAGNITUDE (under fold-frozen χ_q).** With `χ_q,today ≈ χ_q(fold)`, `computed_frac = ρ_m,today²/χ_q,today/ρ_obs = 6.51e-121`, vs the target residual fraction `0.032 = 4/125`. `RATIO = |6.51e-121 − 0.032|/0.032 = 1.0000 ≫ 0.156` band (Sage-exact `0.005/0.032 = 5/32 = 0.15625`). The magnitude is off by ~119 OOM — the Ω_m² shape-match (the coincidence that `ρ_m,today²/χ_q` is dimensionally an energy density) is **coincidental**: it cannot reproduce 0.032 because χ_q is fold-frozen at ~10⁷³ GeV⁴, not run down to ~10⁻⁴⁶ GeV⁴.

**4-tuple**: `(value=0.018502261686473124, scheme=CHI-Q-D2EPS-DQ2-JENSEN-TAU-SCAN, convention=RATIO-on-residual-fraction-0.032-plus-OOM-rundown-fork, L_max=canonical)`.

**[CHAIN] 3-tuple** (the [CHAIN]+directional gate): `sign_verdict=PASS` (the substitution chain Step 3 predicted fold-frozen `χ_q ~ S_fold ⇒ OOM_rundown ≈ 0`; the first-principles τ-scan observed 0.0185 OOM — the direction MATCHES) / `magnitude_verdict=FAIL` (RATIO 1.0 > 0.156 band) / `regime_verdict=VALID` (the run-down sits cleanly in the pre-registered <10-OOM fold-frozen branch; the curvature is a well-defined magnitude across the entire family, no regime breakdown).

**regulator_pin** `a_0^{Mellin}` declared (verdict-file companion row): the residual `ρ_vac/ρ_obs − 1` is the a₀ Seeley-DeWitt zeroth-moment / Volovik-vacuum sector — the q-departure `ρ_vac = ε(q) − q·dε/dq` is the a₀-channel object, NOT a₂/a₄ (Volovik Paper 04 §III/IV).

**χ_q(a) scale-factor leg.** The plan's secondary leg (`χ_q(a)` requiring the C1 substrate→a(t) map, currently ASSUMED-with-external-import) was NOT pursued — and is not needed: per WS-3 §4.2 item 4, the **τ-scan leg ALONE settles the crux**. The fold-frozen result is established channel-internally on the Jensen-family τ-scan; no a(t) map is required to conclude the run-down is sub-decade. (NB: the COSMOLOGICAL densities ρ_DE, ρ_DM DO undergo power-law decay via energy exchange — Volovik Paper 35 §V, `35_2024_Volovik_Landau_Khalatnikov_Two_Fluid_de_Sitter.md` — but that is the run-down of the energy DENSITIES, a separate object from the run-down of the response coefficient χ_q. The closure formula `Λ_residual = ρ_m²/χ_q` has χ_q as a fixed-stiffness denominator; it is χ_q that would need to run for channel-internal closure, and it does not.)

**Solution-space.** The residual-3% is a permanent **standing q-departure-channel limitation**: the channel is correctly identified (Reading-A — the q-departure `ε(q) − q dε/dq` IS where the residual lives), but the closure is NOT demonstrated channel-internally (the S43 χ_q dead-end + the leading-α_V over-constraint). The CCRESID standing-limitation verdict is CONFIRMED on channel-internal grounds; the capstone §8.5 / `project_dilution-cc-priority` "residual-3% underived" line stays, sharpened to "standing q-channel limitation, channel identified, closure not demonstrated." The order-of-expansion dissent (does a 2.06×-overshooting BBN leading term permit a 3%-accurate next-order term?) is **moot** — there is no closure regardless of the expansion order, because χ_q cannot run. Downstream status moves (atlas-04 C10 CCRESID sub-annotation; capstone §8.5 prose tag) are applied by their designated writers AFTER this verdict, not in this wave.

**Dual-SHA**: `audit_sha256 = e988a329b1ff7b3e8f0ff1073b901719b4475d95a0b2d5880d3afded7d0a06d6` (over [script, canonical_constants @ plan-pinned `9ee1a113…`, s97_w2_2 npz, s43 reference, pinmap]); `content_sha256 = d93260484be16b0bbf3a3469c1371e59e36e181b19b6b52b93753056d5ceb4d3` (script only). **Artifacts**: `s114_ccresid_chi_q_scaling.py / .npz / .png`. **Canonical promotion**: `chi_q_fold = 300338.0` added to `canonical_constants.py` SECTION E with full provenance (S114 CF-S114-CCRESID-CHI-Q-SCALING).

---

## Wave 2 Synthesis (team-lead)

Three scale-origin deciders, each converting an S113-workshop Reading-A/Reading-B fork into a pinned position. **W2-1 KPIVOT INFO** — a substrate-natural EVEN transport degree (`deg = 0`, parity-consistent with `d_A=0`) IS extractable on the BZ-edge→K* ratio leg, so it is NOT scale-leg contamination (not Reading-B-on-the-ratio); but it is the TRIVIAL dimensionless-ratio-preserving degree, which by the K=3 multiplicative-normalization cancellation invariant cancels in every ratio and supplies no contraction to K* (1.6625 decades unaccounted, bridge image off the §VII envelope). C2-ratio is *partial-derivable* but does NOT close the K_pivot bridge from within — not a §23 K=3 advancement. **W2-2 TAUFOLD INFO (HYBRID)** — the van Hove cusp-CROSSING `τ_cross = 0.191038` (from-scratch, no 0.190 injected; reproduces atlas-07 S45 to 5sf) is L_max-INVARIANT across {5,8,10,12} ⇒ Reading-B (regulator-conditional location) REFUTED; `|τ_cross − 0.190| = 0.5464%` just outside the ±0.5% band ⇒ Reading-A (full value-selection) not reached; the cusp-crossing REGION is van-Hove-SELECTED, the precise 0.190 a flank-sub-choice. **W2-3 CCRESID FAIL (Reading-B confirmed)** — `χ_q(τ)` first-principles across the Jensen family is FOLD-FROZEN (fold→edge OOM run-down 0.0185 ≪ the 118.71 OOM the `Λ_residual = ρ_m²/χ_q` channel-internal closure requires); the residual-3% is a confirmed standing q-departure/Gibbs–Duhem-channel limitation (channel identified, closure not demonstrable channel-internally — χ_q cannot run).

### (a) Numerical revisions
- C2-ratio transport degree: extracted `deg = 0` (even, parity-correct, trivial-on-ratio); 1.6625 decades unaccounted.
- τ_fold: `τ_cross = 0.191038` (joint, L_max-invariant); deviation from 0.190 = 0.5464% (just outside ±0.5%).
- χ_q: full-Jensen-family OOM run-down `0.0343`, fold→edge `0.0185` (vs 118.71 required); `χ_q/d2S_fold = 0.9449`.

### (b) Structural changes
- C2-ratio: `narrowly-open (S113 → CF-S114-KPIVOT) → partial-derivable-trivial` ⇒ K_pivot now structural-external on ALL THREE legs (mag + id + ratio); the rank-1 §VII.BS / BF_spine ceiling confirmed structural on the ratio leg.
- τ_fold (A4): `imported flank-point → REGION van-Hove-SELECTED, precise value CONDITIONAL` (M_KK has no van-Hove analog; Reading-B refuted, Reading-A not reached).
- CCRESID (C10 residual-3%): `closability-disfavored (S113 Reading-B lean) → CONFIRMED standing q-channel limitation` (the order-of-expansion dissent is MOOT — no closure regardless of expansion order, χ_q cannot run).

## Carry-Forward Computations

**W2 compute gates (W2-1 / W2-2 / W2-3): no carry-forwards** — all three deciders resolved in-session. The plan's conditional CFs did NOT trigger — KPIVOT landed INFO not PASS (no §23 K=3 registration; the degree is trivial-on-ratio), CCRESID landed FAIL not PASS-A (the order-of-expansion trap gate is moot — χ_q is fold-frozen regardless of expansion order), and the χ_q(a) scale-factor leg is not needed (the τ-scan settles the crux channel-internally per WS-3 §4.2).

The S114 W-1 workshop (transit × lizzi — τ_fold canonical-value adjudication, branched from the W2-2 `CF-S114-TAUFOLD-CUSP-CROSSING` INFO) produced ONE confirmatory math carry-forward, mirrored here (back-filled at S114-close per the no-technical-debt rule; the workshop finalized AFTER this WP's CF section):

### CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM — confirmatory S0-KNOB cross-substitution (LOW-priority / CONFIRMATORY; CANNOT change the W-1 verdict)

> **Routing note**: Mirrored from `sessions/session-114/workshops/w-1-taufold-canonical-value.md §"Carry-Forward Computations"`. Mechanical due-diligence on Axes A+B of the W-1 output-(iii) verdict; the Axis-C exact-rational asymmetry is regulator-free arithmetic that needs no re-run.

1. **What**: re-run `s101_w3_s0_knob.py` with candidate (iii) routed as `q = 0.191038` (located crossing) instead of `q = Fraction(19,100)`, AND with the `assert abs(float(tau_f) - tau_fold) < 1e-15` guard relaxed to the substituted value, to mechanically confirm (a) the GRADED selector still selects (iii) and (b) `dev[iii] = 0.00682 ≤ PASS_BAND = 0.01` (gate still PASSes on (iii)); then Sage-confirm `CF(0.191038/0.112)` has no clean small-denominator convergent (large partial quotient 18) so the `S_0 = 95/56` exact-identity has NO analog at the located value.
2. **Inputs**: `computations/session-101/s101_w3_s0_knob.py`; `s101_envelope_carrier_discriminate.npz` (`legC_output_form=GRADED`, `S0_fit=1.694153`); `canonical_constants.py` (`tau_fold`, `T_acoustic`); Sage `continued_fraction`.
3. **Gate**: `S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` — PASS iff (selector selects (iii) under GRADED) AND (`dev[iii]^{cross} ≤ 0.01`) AND (`CF(0.191038/0.112)` has a partial quotient ≥ 10 within the first 8 terms, certifying no clean small-denom rational). CONFIRMS the analytic verdict; CANNOT flip it (the exact-rational asymmetry is regulator-free arithmetic).
4. **Effort**: Small (~15 min: one flag-guarded script edit + one Sage CF call). LOW-priority / CONFIRMATORY.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-23 | W2-1 KPIVOT / atlas-04 C2-ratio | narrowly-open (S113) | **INFO** — partial-derivable-trivial | even deg 0 extracted but trivial-on-ratio; K_pivot structural-external all 3 legs |
| 2026-06-23 | W2-2 TAUFOLD / atlas-04 A4 | value-CONDITIONAL-on-Gate-A1′ | **INFO** — region van-Hove-selected, value conditional | τ_cross L_max-invariant (Reading-B refuted); 0.5464% outside ±0.5% (Reading-A not reached) |
| 2026-06-23 | W2-3 CCRESID / atlas-04 C10 | CONDITIONAL-on-CHI-Q-SCALING | **FAIL** — standing q-channel limitation confirmed | χ_q fold-frozen (0.0185 ≪ 118.71 OOM); C10 tracking-form tag UNCHANGED |

Process observations: the `deg_T=2.0` import-foreclosure held (W2-1 emitted the EXTRACTED degree, the α_s/d_s +2 recorded only as the EXCLUDED anti-rescue value); the no-injected-0.190 discipline held (W2-2 landed the substrate's own 0.191038, NOT 0.190); the `a₀^{Mellin}` regulator tag held (W2-3). `chi_q_fold = 300338.0` promoted to `canonical_constants.py` SECTION E (single-call FIX-IN-SESSION; the mid-session SHA drift `9ee1a113→a4b8b679` traces here). Capstone-hygiene reconciliations effected in-session — atlas-04 S114 freshness note + capstone §6.3 (C2-ratio + τ_fold) + §8.5 (CCRESID); see `session-114-housekeeping.md §A`.

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:--|:--|:--|:--|:--|
| W2-1 | `s114_kpivot_edge_transfer_degree_open.py` | ✓ | ✓ | INFO (`3c12c706…`) |
| W2-2 | `s114_taufold_cusp_crossing.py` | ✓ | ✓ | INFO (`7b637db1…`) |
| W2-3 | `s114_ccresid_chi_q_scaling.py` | ✓ | ✓ | FAIL (`e988a329…`) |
