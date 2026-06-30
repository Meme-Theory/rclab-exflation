# Session 117 Wave 6 — FWD-C2 L_emp bridge regulator-axes (Results Working Paper)

**Session**: 117 | **Wave**: 6 | **Plan**: session-117-plan-w6.md | **Theme**: Resolve the Q30 FWD-C2 carry-forward into the regulator-structure of the §VII.AV.STATE-PROJ `L_emp` anchor (and its §VII.AU.OP-PROJ sibling) as **two ORTHOGONAL axes authored as non-conflated gates** — (6-1) secondary-class `{APS-1975, Cheeger-Simons, Bismut-Cheeger}` **FORCED** by PH-even-variance (confirmation; the W-4 D1 falsifier), (6-2) UV-regulator `{ζ, Pauli-Villars, Mellin}` **SD-OPEN** (the genuine open gate; the additive-in-trace a₀ counterterm survives the log-derivative), (6-3) an additive §VII.AU.OP-PROJ Element-3 FB-B-vs-FB-A scope annotation (INFO). **Orthogonality discipline (load-bearing)**: a 6-1 PASS (secondary-class FORCED) MUST NOT be read as 6-2 evidence (UV-regulator robustness), and vice versa; the two verdicts combine via logical AND ONLY at the registry-coherence layer (`registry:18819` two-orthogonal-pin re-tag, mack-routed) — the framework's own four-axis orthogonality (`regulator-pin-discipline.md §"four-axis orthogonality"`). All three gates are **COMPUTE-class**, S116-or-earlier landed (no intra-S117 prereq blocks; parallel-dispatchable, independent of W0–W5 / W7–W9).

## Gate Sections

### §W6-1. CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (secondary-class scheme-spread + bulk-gap protection on FWD-C2 `L_emp` at s=4 / n=0)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: At curvature-grade n=0 the {APS-1975, Cheeger-Simons, Bismut-Cheeger} secondary-class scheme-spread of `L_emp = −7.046336` is FORCED to vanish (Δ_scheme < 1e-3 M_KK²) by the PH-evenness of `Var_a(|v_a|²)` (`Var(1−X)=Var(X)`), and the gapped BDI bulk (Δ_BCS) admits no s=4 K-window spectral flow — the secondary-class (PH-parity) axis ONLY, SILENT on the orthogonal UV-regulator axis (6-2) (**Expected verdict**: PASS — FORCED-by-construction confirmation; this gate IS the W-4 D1 falsifier, so a nonzero n=0 spread ≥ 1e-3 M_KK² would FAIL and FALSIFY the parity argument; this is NOT a UV-regulator-robustness test).
**Plan reference**: `sessions/session-plan/session-117-plan-w6.md` §W6-1 (machinery pin, Reading-A scheme-INDEPENDENCE threshold, substitution chain Steps 1–6, Input-SHA Ledger, verdict rubric).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — content presence by regex, never line/byte counts):
- (1) Script `computations/session-117/s117_w6_fwdc2_lemp_bulkgap_protection.py` — PRESENT (40,620 B); `from canonical_constants import` (2×) AND `print_verdict_payload` (2×). ✓
- (2) Data `computations/session-117/s117_w6_fwdc2_lemp_bulkgap_protection.npz` — PRESENT (24,346 B); plot `…_bulkgap_protection.png` — PRESENT (235,129 B). ✓
- (3) Verdict line in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION:.* audit_sha256=[a-f0-9]{64}` — PRESENT (`audit_sha256=b86db4efbd586b4d8713e224bdd8b95ab222547d6620926042ff70ad88fc256a`, `content_sha256=0ef309638e7adef4…`) + dual-SHA companion row (companion_row_required ✓) + 4 extra companion rows (regulator_pin / bridge-map-scheme-suffix / FORCED-rationale / FALSIFIER). NO schema-v2 3-tuple (`[VERIFY]`, not `[SIGN]`). ✓
- (4) This §W6-1 section: Status=COMPLETED + Verdict=PASS + `**Output Artifacts**` + `**MCP Pre-Compute Audit**` blocks present. ✓

**MCP Pre-Compute Audit** (queried BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `get_constant("L_emp_VII_AV_STATE_PROJ")` → −7.046336474406761 (S116, gate S116-W8-FWDC2-LANDING; Corner-IV K-window log-derivative of `Var_a` at s=4 on M_2(C)) — the cocycle anchor this gate's observable reproduces.
- `get_constant("Delta_BCS")` → 0.4642547394830737 (S70, R-PROTECTED) — bulk-gap reference.
- `get_constant("M_KK")` → 7.428660036284456e16 — unit anchor.
- `search_knowledge("secondary-class scheme discriminator APS Cheeger-Simons Bismut-Cheeger delta_scheme")` → **S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR** (`delta_scheme=0.000e+00`, `GV_APS=GV_CS=−1.208158e+08` for an even η=0 object) — the even-object precedent (D1.1). NOT run at n=0 (the scope-limit this gate closes).
- `search_knowledge("L_emp PH-even variance occupation Var FWD-C2 forced secondary class")` → §VII.AV.STATE-PROJ STAGE-3-PERMANENT + the W-4 workshop two-axis verdict (secondary-class FORCED ∧ UV-regulator SD-OPEN). **NOT PRE-CLOSED at n=0** — this gate IS the W-4 D1 falsifier's n=0-pinned numerical realization.
- Machinery read (not re-derived): `_cm_1995_residue_formula.py` (S90 APS/CS evaluators) + `s93_w9_3_…_rho_invariant_pillar_v_bdg.py` (the 3-η-scheme BdG ρ-invariant EARNED Reading-A — the structural CONTRAST).

**Verdict**: **PASS** — FORCED-CONFIRMED. `delta_scheme({APS,CS,BC}) = 0.000000e+00 M_KK² < 1e-3` (machine precision; all three pairwise diffs `|APS−CS|=|APS−BC|=|CS−BC|=0.000e+00`) AND the K-window carries no s=4 spectral flow (`min E_a(K) = 0.944506 > 0`; L12/L14 `min|λ(D_K)| = 8.197e-01 > 0`). The secondary-class {APS,CS,BC} scheme-independence of the L_emp occupation-variance cocycle is CONFIRMED-FORCED by the PH-evenness of `Var_a` (§VII.AV.STATE-PROJ Element-3 secondary-class Reading-A establisher; single Element-3 suffix licensed). **DISTINCT from S93 W9-3's EARNED ρ-invariant Reading-A — the registry MUST NOT record this PASS as co-equal** (the FALSIFIER contrast below proves the distinction is structural, not numerical). SECONDARY-CLASS (PH-parity) axis ONLY; SILENT on the orthogonal UV-regulator axis (gate 6-2). Closes the S90-AQ n=0 scope-limit. `[VERIFY]` trigger → companion_row_required, NO schema-v2 3-tuple.

**Results**:

**4-tuple**: `(value=delta_scheme=0.000e+00, scheme=secondary-class-rho-invariant, convention=FWDC2-secondary-class-{APS-1975-secondary-class}+{Cheeger-Simons}+{Bismut-Cheeger}-READING-A-CANDIDATE-poleconv-A-double-pole_in_s-4-curvature_grade_n-0, L_max=12 [+14 cross-check])`. `audit_sha256=b86db4ef…256a`, `content_sha256=0ef30963…6874`.

**(A) PRIMARY — secondary-class scheme spread of the PH-EVEN L_emp cocycle.** Pairing the occupation-variance cocycle `Var_a(|v_a(K)|²)` against the three transgression-representatives at the FIXED `a_0^{Mellin}` s=4 UV-regulator:

| scheme R | `GV_R(Var_a)` (M_KK²) | `common_even` | `odd_R` |
|:---------|:----------------------|:--------------|:--------|
| APS-1975 | `1.348332660901` | `1.348333` | `0.000e+00` |
| Cheeger-Simons | `1.348332660901` | `1.348333` | `0.000e+00` |
| Bismut-Cheeger | `1.348332660901` | `1.348333` | `0.000e+00` |

`Δ_scheme = max − min = 0.000000e+00 M_KK²` (< 1e-3). The three `GV_R` are IDENTICAL to machine precision (nonzero common value, zero spread — mirroring the S90-AQ structure `GV_APS=GV_CS≠0, delta_scheme=0`). The scheme-dependent `odd_R` term — the secondary-class transgression `β^odd` — vanishes because it pairs an odd kernel `sign(λ)·|λ|^{−8}·ψ_R(|λ|)` against the PH-even cocycle weight `c_a²` over the BDI ±-paired Nambu spectrum.

**Substitution chain (Steps 1–6, with substituted numbers)**:
- **Step 1** — BdG normalization `|u_a|²+|v_a|²=1` mode-by-mode; max residual `2.220e-16` over the 8 modes (single-mode BdG coherence factors; Fermi-surface-lock S64 + BCS shell exactness S70 → no hybridization, closed).
- **Step 2** — PH conjugation `C = τ_x K` (`D_K → −D_K`): `|v_a|² ↦ |u_a|² = 1−|v_a|²`, `E_a ↦ −E_a`.
- **Step 3** — affine identity `Var(1−X)=Var(X)`: K-window `max|Var(|v_a(K)|²) − Var(1−|v_a(K)|²)| = 5.204e-18`; at K_h residual `0.000e+00`. Sage-QQ anchors: rounded branch set `{0.7704×4, 0, 0.176×3}` → `Var(|v|²)=Var(|u|²)=327477/3125000=0.10479264` (residual 0); exact s52 set `{0.7704351×4, 0, 0.176×3}` → `41921537691201/400000000000000` (residual 0). Holds weight-for-weight on the non-PH-closed (4,1,3) multiset.
- **Step 4** — `Var_a` PH-EVEN; the centered Nambu cocycle weight is `c_a²` (square of the PH-ODD deviation `c_a = |v_a|²−μ`): PH-even parity residual `|W(+E)−W(−E)| = 0.000e+00`; PH-odd `c_a` parity residual `|W(+E)+W(−E)| = 0.000e+00`.
- **Step 5** — {APS,CS,BC} are three transgression-reps of ONE UV-finite secondary class; differences are purely `β^odd`. S90-AQ even-object precedent: `delta_scheme=0.000e+00`, `GV_APS=GV_CS=−1.208158e+08`.
- **Step 6** — Z₂-graded pairing `⟨Var_a, β^odd⟩ = 0` (Sage-exact symbolic: PH-even cocycle × odd kernel over ±-paired spectrum `= 0`; PH-odd cocycle × odd kernel `= 2(C₁g₁+C₂g₂) ≠ 0`). Nambu `Σ sign(λ) = 0.0` (BDI ±-pairing); explicit 16×16 `D_BdG` diagonalized via `torch.linalg.eigvalsh(cuda)`, round-trip residual `0.000e+00`.

**L_emp cocycle identity**: `L_emp = d² ln Var_a/d(ln K)² = −7.046336474406` M_KK²; `|L_emp − proxy| = 6.839e-13` (the cocycle IS the canonical §VII.AV.STATE-PROJ observable).

**(B) FALSIFIER CONTRAST (the W-4 D1 falsifier made live)**: the same three scheme kernels paired against the PH-**ODD** mean-occupation cocycle `c_a` give `GV^odd_APS=−3.377445`, `GV^odd_CS=−3.377445`, `GV^odd_BC=−3.637974` → `Δ_scheme^odd = 2.605286e-01 ≠ 0`. The gate therefore genuinely **DISCRIMINATES**: `Δ_scheme=0` for `L_emp` is FORCED *because* `Var_a` is PH-EVEN, not because the test is trivially zero. A nonzero n=0 spread on the PH-even cocycle would have FALSIFIED the parity argument and vindicated a secondary-axis `β^even`; it did not.

**(C) BULK-GAP protection (no s=4 K-window spectral flow)**: `min E_a(K)` over the window `[0.95,1.05]·K_h` `= 0.944506 M_KK > 0` (B1's `Δ=0` is irrelevant — its `ξ_B1(K)=1.1437·K²` term keeps `E_B1 ≈ 1.03 ≫ 0`); `Δ_BCS = 0.464255 M_KK` (R-PROTECTED) reference. L_max-stability: L12 `min|λ(D_K)|=8.197e-01` (90 sectors), L14 `min|λ(D_K)|=8.197e-01` (119 sectors), both > 0 → gapped BDI bulk admits no bulk zero-mode at any L_max in scope ⇒ `[C, d/d(ln K)] = 0` ⇒ the static PH-even parity holds dynamically across the K-window (no `β^odd` revival at a crossing).

**Closures**: CC1 — PH-even-variance FORCED (`β^odd`-blind), Sage-exact + numerically machine-zero. CC2 — the S90-AQ n=0 scope-limit is CLOSED (`delta_scheme=0` confirmed directly at curvature-grade n=0). Pins carried in verdict: `regulator_pin a_0^{Mellin}` (poleconv-A-double, pole_in_s=4, curvature_grade_n=0; UV-regulator axis ORTHOGONAL, carried by 6-2); `bridge_map_scheme_suffix {APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger}` → single Element-3 suffix licensed ON PASS; level_class_pin=FULL; binding_axis=substrate-natural-binding.

**Substrate framing (GEOMETRIC)**: the substrate IS the BdG quasiparticle occupation structure of `D_K` on the M_2(C) child; `Var_a(|v_a(K)|²)` is the spread of occupation across the 8 SU(3)-singlet-selected phononic modes, and `C = τ_x K` is the fabric's intrinsic particle-hole conjugation. Direction: substrate IS the occupation-variance → bridge map (secondary-class transgression pairing) → laboratory secondary-class measurement. The fabric's PH-parity is scheme-free, fixed by its own `C`, read off before any scheme is chosen — that is WHY the {APS,CS,BC} collapse is forced for an even moment. This gate certifies the AUTOMATIC odd-channel blindness of an even observable, a property of the fabric, not a stringent scheme survival.

**Downstream (mack-routed, Wave-6→7 decision point)**: 6-1 PASS → §VII.AV §A8.1(i) guard re-tag pin (i): "secondary-class {APS,CS,BC} FORCED (PH-even-variance; S90-AQ `delta_scheme=0` precedent; Reading-A established; DISTINCT from S93 W9-3's EARNED ρ)". Combines via logical AND at the registry-coherence layer ONLY with gate 6-2's pin (ii) (UV-regulator FI/SD) — neither verdict stands in for the other.

**Artifacts**: `s117_w6_fwdc2_lemp_bulkgap_protection.py` (40,620 B) / `.npz` (24,346 B) / `.png` (235,129 B).

---

### §W6-2. CF-S117-LEMP-UV-REGULATOR-BR-SPAN (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-LEMP-UV-REGULATOR-BR-SPAN`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (B(R) plateau span across UV-regulator classes on FWD-C2 `L_emp` at s=4 / n=0 — the CC-problem-in-microcosm)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: `L_emp = d²ln κ_R(K)/d(ln K)²|_{K_h}` at the s=4 pole (n=0, a₀-grade) is FUNCTIONAL-INDEPENDENT across R∈{ζ, Pauli-Villars, Mellin} (rel_span ≤ 1e-7, FI) vs SCHEME-DEPENDENT (rel_span > 0.05, SD), because the additive-in-trace a₀ counterterm `κ_R = κ_0 + Δ_R` SURVIVES the log-derivative (NOT annihilated by the W8-2 multiplicative-normalization cancellation) — the genuine SD-OPEN gate of the wave (**Expected verdict**: OPEN — favored prior 0.60 Track-B SD/FAIL vs 0.30 Track-A FI/PASS; the verdict is NOT pre-judged, EVOI-positive; against the favored prior a PASS would STRENGTHEN §VII.AV beyond the vanishing-PASS).
**Plan reference**: `sessions/session-plan/session-117-plan-w6.md` §W6-2 (machinery pin, tolerance bands, dual_prior, substitution chain Definitions 1–2 + Sage EMERGENCE-1 closed form, Input-SHA Ledger, verdict rubric).

**Output Artifacts** (closure-verification checklist; content presence by regex, never line/byte counts):
- (1) Script `computations/session-117/s117_w6_lemp_uv_regulator_br_span.py` — PRESENT (39951 B); contains `from canonical_constants import` AND `print_verdict_payload`. ✓
- (2) Data `computations/session-117/s117_w6_lemp_uv_regulator_br_span.npz` (16691 B) AND plot `…png` (233600 B) — PRESENT. ✓
- (3) Verdict line in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-LEMP-UV-REGULATOR-BR-SPAN:.* audit_sha256=[a-f0-9]{64}` — PRESENT (`audit_sha256=a46b5e59…04188`); + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`; `[SIGN]` trigger, directional additive-channel-dominant prediction). ✓
- (4) This §W6-2 section: Status=COMPLETED + Verdict∈{PASS,FAIL,INFO} + `**Output Artifacts**` + `**MCP Pre-Compute Audit**` blocks present. ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("L_emp UV-regulator B(R) span scheme-dependent additive-in-trace")` → returned the S91 `B(R_SCHEMATIC)` divergence note (FULL-PV vs SCHEMATIC F-image 75×, but on the FULL/SCHEMATIC axis — orthogonal to my UV-regulator axis), the S83 `span_B=2.956 / span_A=14.685` k_a2 regulator-class spans at a₂ (bare-moment SD), the **ZETA-NOT-PHYSICAL UV-Regulator Wall (S75, PROVEN)**, and `eps_H` sign-reversal SCHEME-DEPENDENT (S66 W2-A). Confirms the bare-moment a₀/a₂ grades are SD; the open question is whether the *log-derivative* L_emp inherits it.
- `get_constant("L_emp_VII_AV_STATE_PROJ")` → `-7.046336474406761` (Corner-IV K-window log-derivative `d²ln Var_a(|v_a(K)|²)/d(ln K)²` at s=4 on BdG M_2(ℂ); S93 W3 Stage-2 PASS-AND; STAGE-3-PERMANENT). The PV reference / span normalizer.
- `trace_entity("multiplicative-normalization cancellation additive-in-trace")` → no direct entity (the scope-boundary is the S116 W-4 workshop result + my agent-memory permanent-theorem; not yet a knowledge-DB entity). NOT PRE-CLOSED — this is the genuine open gate (S116 W-4 OQ-1).
- Sage MCP (`sage_eval`) — re-verified the EMERGENCE-1 closed form `d²/du²ln(g+Δ)−d²/du²ln g = (Δ²+2Δg)g'²−(Δ²g+Δg²)g'')/(Δ²g²+2Δg³+g⁴) = Δ·d/du[−g'/g²]+O(Δ²)` (leading term matches series-O(Δ) coefficient EXACTLY, residual 0).

**Verdict**: **INFO** (composite). 3-tuple: `sign_verdict=PASS` (additive-channel-dominant: |additive residue| ≫ |multiplicative residue|) / `magnitude_verdict=INFO` (rel_span = 3.118e-02 ∈ (1e-7, 0.05]) / `regime_verdict=VALID`. `audit_sha256=a46b5e590125fcb3f24b1b1573bf473426faad4f850269d78227a3cd4a504188`, `content_sha256=f9b992991130c8cae569bf00ed1cf515984f245bb493fc9471c462afd613fcb0`.

The functional-independent hypothesis (Track A) is **REJECTED** (rel_span ≫ 1e-7 floor in EVERY vacuum model); **SD-OPEN is GENUINE** (the additive-in-trace a₀ residue survives, NOT closed by the W8-2 multiplicative cancellation — my S116 W-4 dissent against the "narrower/weaker" reading is vindicated). The composite is INFO (not FAIL) because at the conservative physical vacuum model the residue is suppressed below the 5% physical-significance threshold; the exact magnitude is the workshop's OQ-4 (vacuum-Fermi-surface-dependent, INFO→FAIL band).

**Results**:

*Verdict-direction (substrate-physics).* The CC problem in microcosm. `L_emp = d²/d(ln K)²` projects out the K-independent (pure-volume / cosmological-constant) part of the regulator selection — so it is structurally MORE CC-protected than the bare action — but "more protected" ≠ "immune": the additive-in-trace a₀ counterterm survives as a K-dependent shadow. The schemes that ELIMINATE a₀ (zeta — my signature; PV — subtracted) coincide; the scheme that RETAINS the a₀ residue (Mellin) differs. The span is regulator-class-keyed by construction.

*B(R) per scheme* (`B(R) = d²ln(κ_0(K)+δ_R)/d(ln K)²|_{K_h}`, K-window [0.95,1.05]·K_h, N_K=101, 5-pt central FD; PV reference `L_emp_PV = −7.046336474406761`):

| R | δ_R (additive a₀ offset) | B(R) | B(R)−B(0) | a₀ treatment |
|:--|:--|:--|:--|:--|
| ζ (zeta) | 0 EXACT | −7.04633647 | 0 | a₀ ABSENT (`S_ζ=ζ_D(0)`; my signature) |
| Pauli-Villars | ≈ 0 | −7.04633647 | 0 | a₀+a₂ subtracted by (+1,−2,+1) tower |
| Mellin | −5.4775e-05 | −7.26602323 | −2.197e-01 | a₀ residue RETAINED |

- **`rel_span = (max_R B(R) − min_R B(R)) / |L_emp_PV| = 3.117744e-02`** (absolute span 2.197e-01 M_KK²); band = INFO.
- Kernel reproduction: `B(0) = L_emp_kernel = −7.046336474406` vs canonical `−7.046336474407` (rel 9.71e-14 — reproduces S89/W8-2). `κ_0(K_h) = var_bare(K_h) = 6.492e-03`.

*Two-channel separation (the load-bearing S116 W-4 distinction; CF-2).* The regulator class enters κ_R(K) through two structurally distinct channels:
- **MULTIPLICATIVE channel** — the s=4 spectral-support moment M_R(s=4) is a K-INDEPENDENT pre-factor. The a₀ grade is **0.6065** (= (M_bare−M_PV)/M_bare at L14, the LARGE a₀ content) — but it is multiplicative, so `B[M_R·var_bare] = B(0)` to residual **5.17e-10** (`B[M_bare·var]=B[M_PV·var]=−7.0463364749`). **ANNIHILATED** (W8-2 cancellation reproduced; FUNCTIONAL-INDEPENDENT).
- **ADDITIVE-IN-TRACE channel** — the a₀ / CC counterterm `κ_R(K) = κ_0(K) + Δ_R`. **SURVIVES** the log-derivative. This is the surviving SD contribution.

*Substitution chain (with numbers; Sage EMERGENCE-1 closed form).* `u = ln K`, `g = κ_0 = var_bare`:
```
residue(R) = B(R) − B(0) = d²/du² ln(g+Δ_R) − d²/du² ln g
           = Δ_R · d/du[−g'/g²]|_{K_h} + O(Δ_R²)          [Sage-exact, residual 0]
  d/du[−g'/g²]|_{K_h} = −(g''g − 2g'²)/g³ = 3.9525e+03      (the residue MULTIPLIER)
  Mellin: residue (closed form) = Δ_Mellin·3952.5 = −2.165e-01
          residue (direct B(Mellin)−B(0))         = −2.197e-01
          closed-form vs direct |diff| = 3.19e-03  (O(Δ²)+FD; validates EMERGENCE-1)
```
The residue vanishes IFF `Δ_R = 0` (zeta/PV) OR `g'=g''=0` (constant base). `Δ_Mellin ≠ 0` (a₀ retained) ⇒ residue ≠ 0 ⇒ **SD-OPEN genuine**.

*`[SIGN]` directional claim — additive-channel-dominant.* `|additive residue| = 2.197e-01` ≫ `|multiplicative residue| = 5.17e-10` ⇒ **ADDITIVE-CHANNEL-DOMINANT = True** ⇒ `sign_verdict = PASS`. The surviving SD contribution is the additive-in-trace a₀ residue, NOT the (annihilated) multiplicative channel — exactly the CF-2 sub-diagnostic prediction.

*a₀ counterterm substrate-first construction.* `Δ_R` = the regularized vacuum-occupation-variance over the FULL D_K spectrum (L12/L14 caches), BdG vacuum `v_vac²(λ)=½(1−ξ/E)`, `E=√(ξ²+Δ_BCS²)`. zeta sets a₀=0 EXACTLY; PV's (+1,−2,+1) tower (`Σc=0`, `Σc·m²=0`) subtracts a₀+a₂; Mellin retains the a₀ residue (`Δ_Mellin = Mellin(a₀-kept) − PV(a₀-removed) = −5.4775e-05`). Ratio `|Δ_Mellin|/κ_0(K_h) = 8.44e-03 ≪ 1` (suppressed). L_max stability: `Δ_Mellin(L12)=−4.76e-05`, `(L14)=−5.48e-05` (drift 7.2e-06 — the a₀ counterterm is L_max-stable at the canonical vacuum model).

*OQ-4 magnitude sensitivity (the genuinely-open part).* The a₀ counterterm magnitude — hence rel_span — depends on the substrate's Fermi-surface location relative to the spectral floor, which the available data does NOT pin (the BdG occupation structure lives on the 8 gap-IR modes; the full D_K spectrum carries only bare eigenvalues). Vacuum-model scan at L14:

| Fermi model | δ_Mellin | \|δ\|/κ₀ | rel_span | band |
|:--|:--|:--|:--|:--|
| zero (canonical, conservative; Fermi below floor, UV-vacuum) | −5.48e-05 | 0.008 | 3.118e-02 | INFO |
| floor (gap-IR-matched; Fermi at spectral floor) | −8.41e-03 | 1.295 | offset > κ₀ ⇒ SD-LARGE | FAIL |
| median (mid-spectrum Fermi; unphysical upper bound) | +3.39e-02 | 5.214 | 1.196 | FAIL |

The conservative model (UV a₀-grade modes EMPTY in the BdG vacuum) gives INFO; gap-IR-matched / mid-spectrum models push the additive offset to ~κ₀ (residue O(1)) ⇒ FAIL. **ROBUST findings (model-INDEPENDENT)**: (i) FI rejected in EVERY model (`rel_span_min = 3.118e-02 ≫ 1e-7`); (ii) SD-OPEN genuine (additive survives, multiplicative cancels). **MODEL-DEPENDENT (OQ-4)**: whether the SD is publication-resolvable-but-suppressed (INFO) or physically significant (FAIL) is set by the unpinned vacuum structure.

*dual_prior posterior reallocation.* Composite INFO → reallocate 0.10 to the third reading "additive residue present but Δ_R ≪ κ_0 suppressed" (Track-A FI 0.30 / Track-B SD 0.60 otherwise unchanged). FI (Track-A PASS) is REJECTED; the SD direction (Track-B) is structurally confirmed, with the magnitude held at the conservative model pending OQ-4.

*4-tuple*: `(value=rel_span=3.1177e-02 band=INFO, scheme=B-of-R-multi-regulator-span, convention=FWDC2-UV-regulator-span-{a_0^zeta}+{a_0^Pauli-Villars}+{a_0^Mellin}-poleconv-A-double-pole_in_s-4-curvature_grade_n-0, L_max=12 [+14 cross-check])`. `regulator_pin = a_0^{ζ} ∥ a_0^{Pauli-Villars} ∥ a_0^{Mellin}` (poleconv-A-double, pole_in_s=4, curvature_grade_n=0 — NOT bare a₄; per `regulator-pin-discipline.md §"Mellin Pole-Set Labeling"`).

*Bridge-anatomy / downstream routing (mack-routed; orthogonal to gate 6-1's secondary-class axis).* §VII.AV.STATE-PROJ Level-3 anchor `−7.046336` MUST carry a regulator-class qualifier `a_0^{<class>}` (the §A8.1(i) guard pin (ii): "UV-regulator {ζ,PV,Mellin} SD-OPEN — additive-in-trace a₀ residue survives; magnitude OQ-4-suppressed at the conservative vacuum model"). This is the orthogonal pin to gate 6-1's secondary-class FORCED (pin (i)); the two combine via logical AND at the registry-coherence layer only. `cross-pillar-bridge-corpus §22` B(R) calibration: realized additive-in-trace instance. `math-scripts.md §"Scope boundary — additive-in-trace pieces are NOT annihilated"` (S116 W4): this gate is the numerical realization (the a₀ counterterm survives the log-derivative; Sage-exact closed form re-verified). Dual-SHA: `audit=a46b5e59…04188`, `content=f9b99299…3fcb0`. Artifacts: `s117_w6_lemp_uv_regulator_br_span.py/.npz/.png`.

**Carry-Forward Computations**:
- **CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN** — *What*: pin the substrate's BdG Fermi-surface location relative to the |D_K| spectral floor (the unpinned vacuum structure that sets the a₀-counterterm magnitude), then re-evaluate rel_span to discriminate INFO (suppressed) vs FAIL (significant) for the §VII.AV `a_0^{<class>}` qualifier strength. *Inputs*: the s52 8-mode BdG occupations {0.130×4, 0, 0.0079×3} (constrain ξ_F so the extended vacuum reproduces the gap-IR occupations); the L12/L14 caches; `Delta_BCS`; this gate's `reg_vacuum_variance` machinery. *Gate*: rel_span at the gap-IR-matched ξ_F vs the 0.05 band → INFO-stays vs FAIL-promote. *Effort*: low (re-run with a pinned ξ_F; no new diagonalization). *Depends on*: this gate (CF-S117-LEMP-UV-REGULATOR-BR-SPAN); the s52 BdG amplitude cache.

**Substrate framing**: GEOMETRIC. The substrate IS the BdG occupation-variance `Var_a(|v_a(K)|²)` of the eigenmodes of `D_K` on the `M_2(ℂ)` child; the regulator class R is the OTHER substrate-IS choice — WHICH spectral functional defines the fabric's action (the central question of my program: zeta vs cutoff give different physics from the SAME D_K). Direction: substrate IS the occupation-variance → bridge map → laboratory a₀/CC-grade measurement. `L_emp = d²/d(ln K)²` is the operator that PROJECTS OUT the K-independent (pure-volume, cosmological-constant) part of the regulator selection — so L_emp is structurally MORE CC-protected than the bare action. But "more protected" ≠ "immune": the additive-in-trace a₀ counterterm survives as its K-dependent shadow. This gate measured that the shadow is SCHEME-DEPENDENT (the CC problem in microcosm, localized onto the K-dependent kernel profile) — genuine, not closed by the W8-2 multiplicative cancellation — with the magnitude suppressed at the conservative vacuum model (the fabric's a₀-grade modes are empty) and OQ-4-open at the gap-IR-matched model. The fabric's PH-parity is scheme-free (gate 6-1); its a₀-grade spectral-moment value is regulator-class-keyed (THIS gate).

---

### §W6-3. CF-S117-FB-EDGE-VS-BOTTOM (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `CF-S117-FB-EDGE-VS-BOTTOM`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (edge-vs-bottom truncation-drift decomposition + zeta-vs-PV α convergence-rate on the FWD-C1 s=3 / a₂ moment)
**Agent**: `spectral-geometer`
**Hypothesis**: The s=3 (a₂, n=2) PV-subtracted moment truncation drift is λ_max-EDGE-driven not bottom-K (FB-A-null, bottom_frac < 0.05), confirming the W8-1 "friedrich-bar-saturation" label is MIS-SCOPED (FB-B Level-2 convergence, NOT FB-A bottom-K saturation), and the convergence-rate α is SCHEME-DEPENDENT across {ζ, Pauli-Villars} (**Expected verdict**: INFO by design — the W8-1 INFO verdict + all numbers are UNAFFECTED; this gate ADDS an additive §VII.AU.OP-PROJ Element-3 Level-2-envelope scope annotation, mack-routed — NOT a verdict revision; a FAIL on bottom_frac ≥ 0.05 would REOPEN the FB-A IN-SCOPE reading).
**Plan reference**: `sessions/session-plan/session-117-plan-w6.md` §W6-3 (machinery pin, tolerance bands, substitution chain Steps 1–5, Input-SHA Ledger, verdict rubric).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — content presence by regex, never line/byte counts):
*(All four artifact classes verified on disk — content presence by regex, not byte counts:)*
- (1) **script** `computations/session-117/s117_w6_fb_edge_vs_bottom.py` — present; contains `from canonical_constants import` AND `print_verdict_payload` (grep-confirmed).
- (2) **data** `computations/session-117/s117_w6_fb_edge_vs_bottom.npz` AND **plot** `computations/session-117/s117_w6_fb_edge_vs_bottom.png` — both present.
- (3) **verdict line** in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-FB-EDGE-VS-BOTTOM:.* audit_sha256=[a-f0-9]{64}` — present, with dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row + 4 `#` extra rows (regulator_pin, composite-precedence, FB-scope, alpha-SD). `audit_sha256=fe53b2c522b27f1ced0e052f08f0b959741aafc8014d73ebe363c787ecd8ba3d`, `content_sha256=aff3bfb141a8646f2579eb63a4ba038c19d55271e50e0ba5eee722c9cce84918`.
- (4) this §W6-3 section — Status=COMPLETED + Verdict=INFO + Output Artifacts + MCP Pre-Compute Audit blocks present.

**MCP Pre-Compute Audit** (query-first; `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("friedrich-bar saturation FB-A bottom-K FB-B Level-2 envelope Mellin cone a2 edge")` → returned the §VII.AU/§VII.AQ Friedrich-Bär *saturation-theorem* entries + `S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR` + the `s116_w8_fwdc1_level2_envelope_friedrich_bar` provenance. **No existing edge-vs-bottom / FB-A-vs-FB-B decomposition gate** → NOT pre-closed; this gate is new.
- `get_constant("alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22")` → `2.6926236951` (S91/S93; the α_PV reference, FULL-physical pathway-B L15–22).
- `get_constant("rho_FULL_CC_VII_AU_SAT_s3")` → `1.0076927826` (S92; PV ρ anchor, reproduced bit-exactly here).
- `get_constant("alpha_HH1_per_pole_FW_s3")` → `2.0` (S92; Wodzicki per-pole lower bound).
- `trace_entity("VII.AU.OP-PROJ Level-2 envelope Mellin-cone s3")` → no trace under that phrasing (registry-text entity); structural anchor taken from the s116 FWDC1 script + npz instead.
- verdict-file grep `CF-S117-FB-EDGE-VS-BOTTOM` → 0 prior lines (sig_5 clean before emit).

**Verdict**: **INFO** (composite, plan-frozen operator) — 3-tuple `sign=PASS / magnitude=FAIL(α SD) / regime=VALID(FB-A-null)`. The generic 3-tuple collapse would read **FAIL** (`magnitude=FAIL ∧ regime=VALID`); the plan-frozen operator (FAIL iff `bottom_frac ≥ 0.05` OR sign-mismatch; INFO iff FB-A-null ∧ sign-match ∧ `alpha_rel > 0.10`) takes PRECEDENCE → INFO, with a `# composite-precedence:` disclosure extra-row emitted per `gate-verdicts.md`. **By design**: the S116-W8-1 INFO verdict and ALL its numbers are UNAFFECTED — this gate ADDS an additive §VII.AU.OP-PROJ Element-3 scope annotation; it does NOT re-adjudicate.

**Results** — NUMBERS first (all on the static L12 s84 + L14 s87 τ=0.19 caches; NO new diagonalization):

*Pipeline validation*: M_FULL/M_BARE/ρ at L12,L14 reproduce S116-W8-FWDC1-LANDING to `rel_dev = 0.00e+00` (bit-exact; same `_pauli_villars_subtraction` PRIMARY helper); `ρ_FULL(L14)` vs canonical `rho_FULL_CC_VII_AU_SAT_s3` `rel_dev = 2.44e-11`. Caches mutually consistent: bare M(s=3) on `s87[level≤12]` vs `s84[L12]` `rel_dev = 0.00e+00` (shared modes bit-identical).

*Edge-vs-bottom (the FB-A-null operator)*: `ΔM_FULL = M_FULL(L14) − M_FULL(L12) = +5990.326`. The bottom-K region moment (`|λ| ≤ 0.845`) is L_max-INVARIANT: `109.659309 (L12) = 109.659309 (L14)`, region drift `= 0.000e+00`. The 29 NEW `p+q∈{13,14}` sectors carry `ΔM_FULL` to `rel_dev = 1.1e-15`; NEW modes with `|λ| ≤ 0.845`: **0** (min `|λ|` over NEW modes `= 3.7057 ≫ 0.845`). ⇒ **`bottom_frac = 0.000e+00 < 0.05` (FB-A-null)**, `edge_frac = 1.000000`.

*Sign cross-check*: `drift_PV (ΔM_FULL) = +5990.33 (sign +1)`; `drift_zeta (ΔM_BARE) = +5987.01 (sign +1)` → **`sign_verdict = PASS`** (both λ_max-edge-driven, same UV pole s=3).

*α FI/SD (the convergence-rate)*: 7-point sub-truncation scan (`level≤L`, L=8…14, from the L14 cache). PV ratio `ρ(L)` is **monotone-DECREASING** `1.01960 → 1.00769` (CONVERGES; `α_PV = 2.6926` canonical; L8–14 cross-check fit `α_PV_fit = 1.37`, pre-asymptotic vs the L15–22 anchor). Bare zeta `ζ_D(s=3) = M_BARE(L)` is **monotone-INCREASING** `8301.6 → 23810.2` (DIVERGES; `s=3 < d/2 = 4`, Weyl tail `λ^{d−2s} = λ^{+2}`); growth `β = +1.882` ⇒ **`α_zeta = −1.882`** (NEGATIVE — no positive convergence exponent exists). `alpha_rel = |−1.882 − 2.6926| / 2.6926 = 1.699 > 0.50` → **SD**. The three reconciled F-images SCHEMATIC `|α|=3` / Wodzicki `2` / pathway-B `2.6926` bracket the PV window `[2,3]`; the zeta exponent sits OUTSIDE (divergent) → the rate is regulator-class-keyed.

*Substitution chain (Steps 1–5, substituted)*:
1. `s=3, d=8, poleconv-A-double ⇒ n = d − 2s = 8 − 6 = 2` (a₂ Seeley-DeWitt; `Res_{s=3} ζ_D = a₂/Γ(3)`).
2. Heat-kernel locality: a₂ is the small-σ (UV) residue ⇒ UV-edge (large-λ) determined; the spectrum bottom sets the large-σ / IR tail (λ_min), never a_n.
3. Per-mode `g_PV(λ;s)` is L_max-independent ⇒ the moment is additive over mode-sets ⇒ shared bottom-K modes cancel in ΔM_FULL ⇒ `bottom_frac → 0` (computed `0.000e+00`).
4. Both schemes' drift is generated by the SAME NEW edge modes (same UV pole) ⇒ `sign(ΔM_BARE) = sign(ΔM_FULL) = +`.
5. PV ratio converges (`α = +2.69`, FB-B envelope); bare zeta diverges (`α < 0`) ⇒ `alpha_rel ≫ 0.50` (SD).

**Canonical-form direction**: the W8-1 `-friedrich-bar-saturation` label is **MIS-SCOPED** at the λ_max edge — the operative mechanism is **FB-B Level-2 convergence** (the PV ratio's `L^{−α}` envelope; the divergent UV tails of M_FULL and M_BARE cancel in `ρ`), NOT **FB-A bottom-K exact-saturation** (which IS real here — the bottom-K region is L_max-invariant — but contributes EXACTLY ZERO to the a₂ moment drift). The mis-scoping is **FUNCTIONAL-INDEPENDENT** (a₂'s UV-edge locality holds in every regularization); the convergence RATE is **SCHEME-DEPENDENT** (cutoff/zeta UV-divergent vs PV-ratio convergent).

**4-tuple**: `(value=bottom_frac=0.000e+00, scheme=edge-vs-bottom-decomposition + zeta-vs-PV-alpha, convention=FWDC1-s3-edge-bottom-{a_2^zeta}+{a_2^Pauli-Villars}-poleconv-A-double-pole_in_s-3-curvature_grade_n-2, L_max=12 and 14)`. `regulator_pin a_2^{ζ} and a_2^{Pauli-Villars}` (poleconv-A-double, pole_in_s=3, curvature_grade_n=2; cross-algebra caveat N/A — SU(3) A_K); `publication_precision=10`; `audit_sha256=fe53b2c5…ba3d`, `content_sha256=aff3bfb1…4918`.

**Bridge-anatomy (mack-routed)**: §VII.AU.OP-PROJ Element-3 Level-2-envelope **scope annotation** — the FWD-C1 s=3 envelope is **FB-B (Level-2 algebraic convergence)**, NOT **FB-A (bottom-K saturation)**; records the **UV-pole-family FB-A-ineligibility methodological wall** (a₂, a₄, … are UV-edge residues, structurally outside FB-A bottom-K scope). Pairs with the S-6 reconciliation in `session-116-housekeeping.md §A` (registry:18347). A FAIL on `bottom_frac ≥ 0.05` would have REOPENED the FB-A IN-SCOPE reading; it did not.

**Substrate framing (GEOMETRIC)**: the substrate IS the D_K spectrum on Jensen-deformed SU(3); the s=3 moment is the a₂ Seeley-DeWitt coefficient — the small-σ heat-kernel residue that generates the Einstein-Hilbert skeleton (the second spectral moment IS Newton's constant). Direction: D_K eigenvalues → a₂ heat-kernel residue (UV edge) → emergent gravity. The bottom of the spectrum (IR, λ_min) cannot source a₂ — which is precisely why FB-A bottom-K saturation cannot be the governing mechanism for a UV-pole moment.

---

## Wave 6 Synthesis (team-lead)

All three Wave-6 gates closed. The wave resolves the Q30 FWD-C2 L_emp regulator-structure as **two genuinely ORTHOGONAL axes, authored non-conflated** — and the orthogonality is the load-bearing result: the same L_emp moment is scheme-FORCED on one axis and scheme-OPEN on the other, and neither verdict stands in for the other.

### (a) Numerical revisions
- 6-1: Δ_scheme({APS,CS,BC}) = **0.000e+00** M_KK² (FORCED); the FALSIFIER contrast — same kernels on the PH-ODD mean-occupation cocycle — gives Δ_scheme^odd = **0.2605 ≠ 0**, proving the zero is genuine discrimination (PH-even-variance blindness), not a trivially-zero test.
- 6-2: rel_span = **3.118e-02** (∈ INFO band); B(ζ) = B(PV) = **−7.046336** (a₀ removed) ≠ B(Mellin) = **−7.266023** (a₀ retained); additive residue 0.2197 ≫ multiplicative residue 5.17e-10; a₀-grade is 0.6065 of the moment but MULTIPLICATIVE ⇒ cancels (reproduces W8-2).
- 6-3: bottom_frac = **0.000e+00** (FB-A-null); a₂ s=3 drift 100% λ_max-edge-driven; α_PV = +2.69 (converges, FB-B) vs α_zeta = −1.88 (diverges); alpha_rel = 1.70 ≫ 0.50 (SD).

### (b) Structural changes
- **The L_emp anchor is two-axis-tagged, not single-status** (epistemic-TYPE): §VII.AV.STATE-PROJ Level-3 = −7.046336 now carries a 2-pin qualifier — pin (i) secondary-class {APS,CS,BC} **FORCED** (PH-even-variance, Reading-A established, DISTINCT from S93 W9-3's EARNED ρ) ∧ pin (ii) UV-regulator {ζ,PV,Mellin} **SD-OPEN** (`a_0^{<class>}`). They combine via logical AND at the registry-coherence layer ONLY. This is the four-axis orthogonality discipline (`regulator-pin-discipline.md`) realized at a single anchor.
- **FI REJECTED, SD-OPEN GENUINE** (6-2): the additive-in-trace a₀ counterterm survives the log-derivative — the numerical realization of the `math-scripts.md §"Scope boundary"` (S116 W4): the multiplicative-normalization cancellation annihilates only multiplicative/additive-in-log pre-factors, NOT an additive-in-trace term. The W8-2 "multiplicative cancellation closes it" reading is correctly NOT extended here (the D2 dissent is vindicated).
- **W8-1 "friedrich-bar-saturation" label MIS-SCOPED** (6-3): the FWD-C1 s=3 envelope is FB-B (Level-2 algebraic convergence), NOT FB-A (bottom-K saturation). FB-A bottom-K IS real (bottom region L_max-invariant) but contributes EXACTLY ZERO to a UV-pole moment — a₂ is a small-σ heat-kernel residue, structurally UV-edge. This is a UV-pole-family FB-A-ineligibility methodological wall (FUNCTIONAL-INDEPENDENT; the α rate is SCHEME-DEPENDENT).

## Carry-Forward Computations

### CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN — pin the BdG Fermi surface to discriminate the L_emp SD magnitude (INFO vs FAIL)

| Field | Spec |
|:------|:-----|
| **What** | Pin the substrate's BdG Fermi-surface location relative to the |D_K| spectral floor (the unpinned vacuum structure that sets the a₀-counterterm magnitude), then re-evaluate rel_span to discriminate INFO (suppressed) vs FAIL (physically significant) for the §VII.AV `a_0^{<class>}` qualifier strength. The robust findings (FI rejected; SD-OPEN genuine) are model-INDEPENDENT; only the magnitude band (OQ-4) is open. |
| **Inputs** | the s52 8-mode BdG occupations {0.130×4, 0, 0.0079×3} (constrain ξ_F so the extended vacuum reproduces the gap-IR occupations); L12/L14 caches; `Delta_BCS`; the W6-2 `reg_vacuum_variance` machinery. |
| **Gate** | rel_span at the gap-IR-matched ξ_F vs the 0.05 band → INFO-stays (Fermi below floor, conservative) vs FAIL-promote (gap-IR-matched, Δ_R∼κ₀). |
| **Effort** | low (re-run with a pinned ξ_F; no new diagonalization). |

(Source: W6-2 §W6-2 carry-forward. 6-1 and 6-3 produce no math carry-forward — 6-1 FORCED-confirmed, 6-3 an additive scope annotation; both are non-math registry edits below.)

### Investigator-surfaced carry-forwards (S117 `/rclab-investigate` consolidation; append-only)

One NEW low-leverage Q2 cohort-note, from the consolidator's adjudication of the W6↔W1 cross-wave flag. The flag is NOT a contradiction (both W6's L_emp SD-OPEN and W1's A_s functional-pluralism hold); the residual is a cohort classification.

#### CF-W6-1 — L_emp a₀-grade UV-regulator SD as a §EVOI.BF lizzi-d.o.f.-cohort sibling (Q2 — EVOI cohort-note carry-forward; LOW leverage)

| Field | Spec |
|:------|:-----|
| **What** | The W6↔W1 flag asks whether L_emp's `a_0^{<class>}` UV-regulator {ζ,PV,Mellin} SD-OPEN (6-2, §VII.AV.STATE-PROJ; FI rejected model-independently, rel_span=3.118e-02) is the SAME permanent no-go as A_s functional-pluralism-PERMANENT (S114 W4-1 FAIL `395f6800`; §EVOI.BF "no substrate-canonical functional selector"). Consolidator determination (settled by existing machinery, NOT new physics): per the 4-axis orthogonality at `regulator-pin-discipline.md`, UV-regulator-selection ⊥ functional-selection are DISTINCT axes, and W6-2 already established the UV-regulator SD-OPEN is structurally real/permanent (`CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN` can only bound the magnitude, never select ζ/PV/Mellin). So L_emp's a₀-grade SD is a PERMANENT scheme-dependence on the UV-regulator axis — a sibling of A_s functional-selection but NOT the same d.o.f. Record as a §EVOI.BF lizzi-d.o.f.-cohort note: add L_emp's a₀-grade UV-regulator SD-OPEN as a third cohort member (alongside A_s + the a_0/a_2-CC ratio) WITH the explicit axis-distinction. |
| **Inputs** | `sessions/evoi-framework.md §EVOI.BF` (current cohort {A_s, a_0/a_2-CC}); W6-2 verdict (`s117_gate_verdicts.txt` L107); §VII.AV.STATE-PROJ registered text; `regulator-pin-discipline.md` 4-axis-orthogonality row; S114 W4-1 `CF-S114-AS-FUNCTIONAL-SELECTION` (audit `395f6800`). |
| **Gate** | Registry/EVOI cohort-note (artifact-existence): §EVOI.BF carries L_emp's a₀-grade UV-regulator SD-OPEN as a cohort member with the axis-distinction annotation. Routes via `/rclab-plan` Step 1c-REGISTERS. |
| **Effort** | low (cohort-note append; no compute). **LOW EVOI** — a magnitude-band refinement on an already-permanent §VII.AV anchor, absent from EVOI §1–§4 by leverage not oversight; the S118 planner may fold or drop. |

## Effected In-Session / routed to session-close

All §VII surface edits route to mack (sole writer, `feedback_mack-bridge-role.md`), executed at the session-close registry pass (race-free, after compute settles):

- §VII.AV.STATE-PROJ §A8.1(i) **two-orthogonal-pin re-tag**: pin (i) secondary-class {APS,CS,BC} FORCED (6-1; PH-even-variance; S90-AQ Δ_scheme=0 precedent; Reading-A established; DISTINCT from S93 W9-3 EARNED ρ) ∧ pin (ii) UV-regulator {ζ,PV,Mellin} SD-OPEN `a_0^{<class>}` (6-2; additive-in-trace survives; magnitude OQ-4-suppressed at conservative vacuum). Combined via logical AND at the registry-coherence layer ONLY — NOT a global EARNED demotion, NOT FORCED-full.
- §VII.AU.OP-PROJ Element-3 **FB-B scope annotation** (6-3): the FWD-C1 s=3 envelope is FB-B (Level-2 convergence), NOT FB-A (bottom-K saturation); records the UV-pole-family FB-A-ineligibility methodological wall. Pairs with the S-6 reconciliation in `session-116-housekeeping.md §A`.
- Calibration-corpus appends (methodology, non-§VII): `cross-pillar-bridge-corpus §22` B(R) — realized additive-in-trace instance (6-2); the `math-scripts.md §"Scope boundary"` numerical realization (6-2, Sage-exact EMERGENCE-1 closed form re-verified).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-28 | §VII.AV L_emp secondary-class axis (6-1) | n=0 scope-limit open (S90-AQ) | FORCED Δ_scheme=0 (PH-even-variance; Reading-A) | 6-1 PASS |
| 2026-06-28 | §VII.AV L_emp UV-regulator axis (6-2) | OQ-1 open (FI vs SD) | SD-OPEN genuine (additive-in-trace a₀ survives); FI rejected; magnitude OQ-4 | 6-2 INFO |
| 2026-06-28 | §VII.AU FWD-C1 s=3 FB scope (6-3) | "friedrich-bar-saturation" (FB-A label) | MIS-SCOPED → FB-B Level-2 convergence; α SCHEME-DEPENDENT | 6-3 INFO |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| 6-1 | `s117_w6_fwdc2_lemp_bulkgap_protection.py` | `.npz` | `.png` | PASS ([VERIFY]) |
| 6-2 | `s117_w6_lemp_uv_regulator_br_span.py` | `.npz` | `.png` | INFO (+[SIGN] 3-tuple) |
| 6-3 | `s117_w6_fb_edge_vs_bottom.py` | `.npz` | `.png` | INFO (+[SIGN] 3-tuple, composite-precedence) |
