# Session 118 Wave 3 — Spectral-functional + WDW residuals (Results Working Paper)

**Session**: 118 | **Wave**: 3 | **Plan**: session-118-plan-w3.md | **Theme**: Two INDEPENDENT low-leverage residuals on distinct substrates (MIXED-DOMAIN — per-gate `agent_type`; both `gate_type: compute`). Neither alters a permanent result; each refines a previously-INFO verdict on an already-settled structure. Gates are parallel-dispatchable (no intra-S118 prerequisite; consume only frozen prior-session artifacts).

## Gate Sections

### §W3-1. CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (§VII.AV.STATE-PROJ a₀-grade UV-regulator span magnitude discriminator, OQ-4)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: With ξ_F pinned substrate-first to the s52 gap-IR BdG occupations, the additive-in-trace a₀ counterterm's UV-regulator span stays sub-threshold (rel_span(ξ_F*) ≤ 0.05) because the gap-IR occupations are all < 1/2 — forcing ξ_F* below the |D_K| spectral floor — so OQ-4 resolves INFO-stays (suppressed); the additive-channel-dominant sign-leg is robust regardless of ξ_F. **EXPECTED verdict: INFO-stays (dual-prior Track-A 0.7) or FAIL-promote (Track-B 0.3); PASS is STRUCTURALLY UNREACHABLE — §VII.AV.STATE-PROJ SD-OPEN is STAGE-3-PERMANENT, so rel_span > 1e-7 robustly.**
**Plan reference**: `sessions/session-plan/session-118-plan-w3.md` §W3-1 (machinery pin, rel_span bands, [SIGN] 3-tuple, two-leg substitution chain, input-SHA ledger).

**Output Artifacts** (verified on disk; `grep -E '<must_contain>'` output pasted below):
- `computations/session-118/s118_w3_lemp_oq4_vacuum_fermi_pin.py` (46994 bytes) — `from canonical_constants import` ✓ (lines 90–91), `print_verdict_payload` ✓ (line 233)
- `computations/session-118/s118_w3_lemp_oq4_vacuum_fermi_pin.npz` (20845 bytes; 67 keys) ✓
- `computations/session-118/s118_w3_lemp_oq4_vacuum_fermi_pin.png` (231798 bytes; 4-panel: occupation-pin, B(R) span, ξ_F*(N) robustness, verdict summary) ✓
- verdict line in `computations/session-118/s118_gate_verdicts.txt`: `CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN: INFO … audit_sha256=fb15f24efe0943352b7606f7694445d0e9cc6b7454ea9cad48131cae875375e8` + dual-SHA companion row + the schema-v2 [SIGN] 3-tuple (sign=PASS / magnitude=INFO / regime=VALID) + the `regulator_pin` and `counting_pin` extra rows (the two orthogonal axes) ✓

```
$ grep -nE 'from canonical_constants import|print_verdict_payload' s118_w3_lemp_oq4_vacuum_fermi_pin.py
90:from canonical_constants import *  # noqa: F401,F403
91:from canonical_constants import (  # noqa: E402
233:def print_verdict_payload(verdict, value, audit_sha, content_sha,
$ grep -E '^CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN:.* audit_sha256=[a-f0-9]{64}' s118_gate_verdicts.txt
CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN: INFO -- value='rel_span_xi_F=3.906305e-02_band=INFO_xi_F_star=0.03654519…' … audit_sha256=fb15f24efe0943352b7606f7694445d0e9cc6b7454ea9cad48131cae875375e8 content_sha256=e5556e11600e4ae027b833391bfb13d31d38cef966fd844e5b62c3b1f54d5fa6 schema_version=S84+
$ grep -E '^# (sign_verdict|regulator_pin|counting_pin)' s118_gate_verdicts.txt | grep CF-S118-LEMP-OQ4
# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID # CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN 3-tuple annotation (schema-v2)
# regulator_pin=a_0^{zeta}||a_0^{Pauli-Villars}||a_0^{Mellin} poleconv-A-double pole_in_s=4 curvature_grade_n=0 (a0/CC grade) # … UV-regulator axis pin
# counting_pin=RATIO-NORMALIZED-TRACE-MEAN (intensive: rel_span normalized by trace-mean |L_emp_PV|; UV-regulator _|_ counting orthogonal axes) # … counting axis pin
```

**MCP Pre-Compute Audit**:
- `search_knowledge("L_emp UV regulator span a0 counterterm VII.AV STATE-PROJ vacuum Fermi")` → **NOT PRE-CLOSED**; no closure covers the OQ-4 magnitude refinement. Salient: `L_emp_VII_AV_STATE_PROJ = −7.046336474406761` (S116; §VII.AV.STATE-PROJ STAGE-3-PERMANENT, S93 W3, Stage-2 PASS-AND S93 W3-6) — the Level-3 anchor this gate ANNOTATES, NOT recomputes. The S93 slot-split gates (OP-PROJ Cell-I / STATE-PROJ Cell-IV, cross-corner co-primary FORBIDDEN) confirm the structure is settled; only the `a_0^{<class>}` magnitude qualifier is open.
- `get_constant("Delta_BCS")` → **0.4642547394830737** (S70, R-PROTECTED, alias Delta_0_OES) — the BdG gap in v_vac²; `get_constant("L_emp_VII_AV_STATE_PROJ")` → **−7.046336474406761** (S116; not superseded) — the regime-gate canonical (kernel must reproduce to < 1e-9); `get_constant("M_KK")` → **7.428660036284456e16 GeV** (S42); `get_constant("tau_fold")` → **0.19** (S12/S42). All consumed canonicals current.
- Input-SHA ledger (all 6 plan-pinned inputs verified; no PRE-REG-INC): s52 `ecfbce08…` MATCH, L14 `fa2bfb83…` MATCH, L12 `9e6d9cf7…` MATCH, W6-2 npz `e43cd8d4…` MATCH, fwdc2 `5c6726c4…` MATCH, full-PV `6893ca6b…` MATCH. The runtime canonical-SHA (`d884a2b5…`) drift is benign (consumed constants Δ_BCS / L_emp / M_KK / τ_fold unchanged).

**Verdict**: **INFO** (INFO-stays — the substrate-first OQ-4 resolution) — sign=PASS / magnitude=INFO / regime=VALID. rel_span(ξ_F*) = **3.906305e-02** ∈ (1e-7, 0.05] at the substrate-pinned Fermi level **ξ_F* = 0.03654519**, which lands **BELOW** the |D_K| spectral floor λ_min = 0.819741 (robustly across all gap-IR sector sizes N∈{8,16,32,64}: ξ_F* = 0.0365 → 0.0555, never reaching the floor). The §VII.AV.STATE-PROJ Level-3 anchor L_emp = −7.046336474406761 is **UNCHANGED** (single-pinned, STAGE-3-PERMANENT); only the magnitude annotation refines — the `a_0^{<class>}` SD-OPEN qualifier stays **SUPPRESSED** (CC-in-microcosm TAMED, not killed). PASS is STRUCTURALLY UNREACHABLE (SD-OPEN permanent ⇒ rel_span > 1e-7 robustly).
- **4-tuple**: `(value=rel_span(ξ_F*)=3.906305e-02 band=INFO, scheme=B-of-R-multi-regulator-span-at-gap-IR-pinned-xi_F, convention=FWDC2-UV-regulator-span-a0zeta+a0PV+a0Mellin-poleconv-A-double-pole_in_s-4-curvature_grade_n-0-RATIO-NORMALIZED-TRACE-MEAN, L_max=14)` — additive a₀ channel over the s87 L14 cache; L12 (s84) L_max-stability cross-check (Δ_Mellin drift L12→L14 = 8.87e-06).
- **dual-SHA**: audit_sha256=`fb15f24efe0943352b7606f7694445d0e9cc6b7454ea9cad48131cae875375e8` · content_sha256=`e5556e11600e4ae027b833391bfb13d31d38cef966fd844e5b62c3b1f54d5fa6`.

**Results**:

*Composite verdict (banded rel_span operator; Level-3-annotation discipline)* — magnitude band: rel_span ≤ 1e-7 = PASS(FI, UNREACHABLE) / 1e-7 < rel_span ≤ 0.05 = INFO(suppressed) / rel_span > 0.05 = FAIL(physically significant). Computed rel_span(ξ_F*) = **3.906305e-02 ∈ (1e-7, 0.05] ⇒ magnitude INFO**. Per the Level-3-annotation discipline (`cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`), the verdict is governed by the rel_span CENTRAL VALUE vs the 0.05 band — a descriptive band statement is NON-LOAD-BEARING. Composite collapse (sign=PASS, magnitude=INFO, regime=VALID) ⇒ **INFO**.

*The ξ_F PIN (substrate-first; SOLVED, anti-injection)* — STEP 1: target = mean(o_a) = **0.068196665473328227** computed FROM `s52_bogoliubov_amp.npz` v_k² = {0.130467×4, 0, 0.007901×3} (NOT the rounded ≈0.06796 literals). STEP 2: ξ_F* = **0.036545185660** is the UNIQUE brentq root (xtol 1e-12) of [ mean(v_vac²(gap-IR; ξ_F)) = mean(o_a) ] over the lowest-8 |λ| L14 gap-IR modes {0.819741×2, 0.835894×6}, bracket [λ_min − 5·Δ_BCS, λ_median] = [−1.501533, 4.331207]; mean-match residual **1.45e-14**. Per-mode LSQ cross-check ξ_F = 0.031021 (RMS 6.29e-02, larger because the near-degenerate gap-IR |λ| cannot reproduce the s52 {0…0.13} occupation spread — diagnostic only), also below floor. **ANTI-INJECTION**: ξ_F* is solved from the s52 gap-IR occupation-match constraint ONLY (`xi_F_status = SOLVED-FROM-GAP-IR-OCCUPATION-MATCH`); the prior rel_span = 0.03118 and the 0.05 band are post-hoc COMPARISON TARGETS, never finder seeds (the W6-2 npz is loaded for cross-check display only). The regime gate is established INDEPENDENTLY of ξ_F: the bare kernel κ₀(K) = Var_a(|v_a(K)|²) reproduces L_emp_PV = −7.046336474406761 to rel **9.71e-14** (< 1e-9).

*Two-leg substitution chain (with substituted numbers)* —
- **Leg A (sign, model-INDEPENDENT)**: the s=4 spectral-support moment M_R is a K-independent multiplicative pre-factor — its a₀+a₂ grade is **0.6065** of M_bare(L14) (LARGE) but is ANNIHILATED by d²/d(ln K)²: |B[M_R·var_bare] − B0| = **5.17e-10** (W8-2 multiplicative-normalization-cancellation, `math-scripts.md` MANDATORY K=3). The additive-in-trace a₀ counterterm SURVIVES: additive residue |B(Mellin) − B0| = **0.275251**. |additive| = 0.2753 ≫ |multiplicative| = 5.2e-10 ⇒ **ADDITIVE-CHANNEL-DOMINANT ⇒ sign = PASS, regardless of ξ_F** (the SD-OPEN mechanism is STAGE-3-PERMANENT). EMERGENCE-1 closed form Sage-validated: Δ_Mellin · d/du[−κ₀'/κ₀²] = −6.84e-05 · 3952.5 = −0.2703 vs direct B(Mellin)−B0 = −0.2753 (err 4.99e-03, O(Δ²)+FD).
- **Leg B (magnitude direction, substrate-PINNED)**: mean(o_a) = **0.06820 < 1/2** ⇒ since v_vac²(λ;ξ_F) = ½ ⟺ λ = ξ_F and v_vac² < ½ ⟺ λ > ξ_F, the gap-IR occupations all < ½ force λ_gap-IR > ξ_F* ⇒ ξ_F* = 0.03655 **below the |D_K| floor** λ_min = 0.819741. Below floor ⇒ for every a₀-grade UV mode λ ≫ ξ_F*, (λ−ξ_F*)/E → 1 ⇒ v_vac² → 0 (the a₀-grade UV modes are EMPTY) ⇒ the additive a₀ contribution δ_Mellin = **−6.838e-05** is small: |δ_Mellin| / κ₀(K_h) = **1.0533e-02 ≪ 1** ⇒ rel_span(ξ_F*) = 3.906e-02 ≤ 0.05 ⇒ **magnitude = INFO (INFO-stays, suppressed)**. [Counter-direction: had mean(o_a) ≥ ½, ξ_F* would land in-band ⇒ Δ_R ∼ κ₀ ⇒ rel_span > 0.05 ⇒ FAIL-promote.]

*B(R) per scheme at the pinned ξ_F\** — B(ζ) = B(PV) = **−7.046336** (a₀ ABSENT: zeta S_ζ=ζ_D(0); PV (+2,−1)/(+1,−2,+1)-subtracted ⇒ δ_ζ=δ_PV=0 EXACTLY); B(Mellin) = **−7.321588** (a₀ residue RETAINED; δ_Mellin = −6.838e-05). absolute span = 0.275251 M_KK²; rel_span = span/|L_emp_PV| = 0.039063.

*Robustness + L_max stability* — ξ_F*(N gap-IR) for N∈{8,16,32,64} = {0.03655, 0.03921, 0.04240, 0.05547}, **all below floor** (a larger gap-IR sector raises ξ_F* but never to the floor) ⇒ the below-floor conclusion is robust, NOT an artifact of the N=8 sector choice. Δ_Mellin L_max-stability at the SAME pinned ξ_F*: L12 = −5.951e-05, L14 = −6.838e-05 (drift 8.87e-06). W6-2 Fermi=zero cross-check: my independent recompute = **3.117744e-02** = the stored s117 value bit-for-bit (validates the machinery without injection); ξ_F* = 0.0365 sits just above the Fermi=zero model (ξ_F=0), hence rel_span(ξ_F*) = 0.0391 slightly exceeds the W6-2 conservative 0.0312 but stays firmly INFO.

*Two orthogonal pin axes* — `regulator_pin` = a_0^{ζ}‖a_0^{Pauli-Villars}‖a_0^{Mellin}, poleconv-A-double, pole_in_s=4, curvature_grade_n=0 (the a₀/CC grade; UV-regulator axis per `regulator-pin-discipline.md §"Mellin Pole-Set Labeling"`); `counting_pin` = RATIO-NORMALIZED-TRACE-MEAN (intensive — rel_span normalized by the trace-mean |L_emp_PV|, NOT RATIO-BLOCKSUM extensive). The two axes are ORTHOGONAL (`regulator-pin-discipline.md §"4-axis orthogonality"`): this gate is regulator-class-keyed on the UV axis (the genuine SD content) AND intensive on the counting axis.

*Substrate-first assessment (GEOMETRIC; FI/SD partition)* — direction of explanation: D_K eigenvalues → a₀-grade vacuum-occupation-variance Var_a(|v_a(K)|²) on the M₂(ℂ) child of A_K = ℂ⊕ℍ⊕M₃(ℂ) → regulator-class span rel_span → the a₀/CC-grade magnitude band (the laboratory-IN cosmological-constant-scheme question, in microcosm). The substrate IS the occupation-variance; the regulator class (ζ drops a₀; cutoff/Mellin retain it) is the OTHER substrate-IS choice — WHICH spectral functional defines the fabric's action. The Fermi surface ξ_F is a FEATURE of the D_K spectrum, not a thing "in" a container; pinning it from the s52 gap-IR occupations is the IS-not-IN move. **The DEEP substrate lesson**: L_emp is a₀-suppressed not only because the log-derivative L_emp = d²/d(ln K)² projects out the K-independent pure-volume (CC) part (structurally more CC-protected than the bare action), but ALSO because the substrate's own Fermi surface sits BELOW the |D_K| floor ⇒ the a₀-grade UV modes are EMPTY in the BdG vacuum ⇒ the huge eigenvalue-moment a₀ (the CC) does NOT translate into a huge OCCUPATION counterterm. **FI/SD partition**: FI is definitively REJECTED (rel_span ≫ 1e-7 at the pinned vacuum); the UV-regulator {ζ,PV,Mellin} axis is GENUINELY SD-OPEN (additive-in-trace a₀ survives, model-independent), but the magnitude is SUPPRESSED at the substrate-pinned vacuum (CC-in-microcosm TAMED, not killed). The §VII.AV `a_0^{<class>}` qualifier closes OQ-4 as "suppressed SD-OPEN" — INFO branch, so NO mack-surface magnitude annotation is routed (the §VII.AV.STATE-PROJ −7.046336 / STAGE-3-PERMANENT anchor is untouched).

---

### §W3-2. CF-S118-WDW-S0-ONGRID (feynman-theorist)

**OPTIONAL / LOW / COSMETIC — EVOI-last, drops FIRST under capacity.** LABEL-only upgrade (S117 W5-2 INFO → PASS); the family-wide J≡0 theorem (every real separated self-adjoint / Robin extension forces J(0)=0 on [0, τ_fold]) is already E- and W-magnitude-independent and holds WITHOUT W(0)=0 on-grid.

**Status**: COMPLETED
**Gate ID**: `CF-S118-WDW-S0-ONGRID`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (Level-2 moduli-deformation substrate-IS per `phononic-framing.md §"Level 2"`; WDW minisuperspace current J at the τ=0 cold-vacuum floor)
**Agent**: `feynman-theorist`
**Hypothesis**: Recomputing the S36 spectral action S(τ) on a minisuperspace grid that reaches τ=0 evaluates the WDW anchor W(0)=2·G_DeWitt·(S(0)−E)=0 ON-GRID (E=S(0)) instead of extrapolated from τ_min=0.10, upgrading the S117 W5-2 INFO → PASS while max_θ|J(0;θ)| stays < 1e-12 across the real Robin self-adjoint family. **EXPECTED verdict: PASS (dual-prior Track-A 0.9); INFO if the grid still cannot place τ=0 as a clean node (cosmetic — drop the CF); FAIL only on a theorem-tension (NOT expected — the J≡0 theorem is analytically E-independent).**
**Plan reference**: `sessions/session-plan/session-118-plan-w3.md` §W3-2 (single discriminating pin τ_min 0.10→0.0, on-grid + |J(0)| rubric, W(0)=0 substitution chain, input-SHA ledger).

**Output Artifacts** (verified on disk; `grep -E '<must_contain>'` output pasted below):
- `computations/session-118/s118_w3_wdw_s0_ongrid.py` (31304 bytes) — `from canonical_constants import` ✓, `print_verdict_payload` ✓
- `computations/session-118/s118_w3_wdw_s0_ongrid.npz` (39999 bytes; 42 keys) ✓
- `computations/session-118/s118_w3_wdw_s0_ongrid.png` (165142 bytes) ✓
- verdict line in `computations/session-118/s118_gate_verdicts.txt`: `CF-S118-WDW-S0-ONGRID: PASS … audit_sha256=95b559c1e311536e0cbe6825c8b70200ba87e3bc917e84405456f65b4f8f4f9e` + dual-SHA companion row ✓ (NO [SIGN] 3-tuple — `[VERIFY]` trigger, `schema_v2_3tuple_required=false`)

```
$ grep -nE 'from canonical_constants import|print_verdict_payload' s118_w3_wdw_s0_ongrid.py
73:from canonical_constants import *  # noqa: F401,F403  (tau_fold, G_DeWitt, ...)
380:def print_verdict_payload(verdict, value, audit_sha, content_sha,
$ grep -E '^CF-S118-WDW-S0-ONGRID:.* audit_sha256=[a-f0-9]{64}' s118_gate_verdicts.txt
CF-S118-WDW-S0-ONGRID: PASS -- value='…' … audit_sha256=95b559c1e311536e0cbe6825c8b70200ba87e3bc917e84405456f65b4f8f4f9e content_sha256=69685a6651de52ef6f724469885e18a070ff48e3edf46fb1e777b67a77456022 schema_version=S84+
```

**MCP Pre-Compute Audit**:
- `search_knowledge("WDW Wheeler-DeWitt minisuperspace current J self-adjoint Robin tau=0")` → **NOT PRE-CLOSED**; no closure covers `CF-S118-WDW-S0-ONGRID`. Salient returns: `INV11-W3-3-WHEELER-DEWITT-PSI-TAU-EFOLD` (distinct gate — WKB e-fold count at τ_peak, FAIL); atlas-08 **Q12** "τ=0 initial conditions" (*BC-RESOLVED* — Hartle-Hawking canonical; the row this gate's on-grid anchor annotates); `s52_wdw_initial` ΔS-relative-to-τ=0 table. The on-grid W(0)=0 anchor is a new evaluation, not a recompute of a closed result.
- `get_constant("G_DeWitt")` → **5.0** (S42, `s42_gradient_stiffness.npz`, not superseded) — confirms the canonical G_DeWitt consumed; CONST-FREEZE-42 ⇒ the runtime canonical-SHA drift (`d884a2b5…` vs the W5-2 plan pin `8c850fd9…`) is benign (the constants this gate consumes — G_DeWitt + τ_fold — are unchanged).
- Input-SHA ledger (all four plan-pinned inputs verified; no PRE-REG-INC): `s63_kk_reduce_4d.npz` **MATCH** (`971782ac…`), `s63_kk_reduce_4d.py` **MATCH** (`d26a1088…`), `s36_spectral_action_gauge.py` **MATCH** (`0ec807d1…`), `s117_w5_wdw_j_rigor.py` **MATCH** (`b490d3ff…`).

**Verdict**: **PASS** — grid_reaches_tau0 = **True** (min(τ-grid) = 0.0 ≤ 1e-9; S(0) a DIRECT D_K(τ=0) eigenvalue-sum), |W(0)| = **0.0** ≤ 1e-12 (E=S(0)), max_θ|J(0;θ)| = **0.0** < 1e-12 over θ∈[0,π) (181 samples), Vilenkin J(0)=234.98 > 1e-6 (excluded, non-self-adjoint, Im(A1/A2)=−234.98≠0), current-conservation relative Wronskian residual = 8.70e-11 < 1e-9 with Im(W)=0.0 exactly, regular_endpoint = limit_circle = True, selfadj_robin_imratio_max = 0.0. The S117 W5-2 INFO is upgraded to PASS.
- **4-tuple**: `(value=grid_reaches_tau0=True|S0_direct=244839.083761|W0=0.0e+00|J0_max_abs=0.000e+00|conservation_rel_res=8.701e-11|vilenkin_J0=234.9807|crosscheck_max_rel=2.35e-16|…, scheme=limit-circle-Robin-selfadjoint, convention=real-self-adjoint-extension-family-on-grid-reaching-tau0, L_max=N/A)` — S(τ) reduction over the s63 KK sectors p+q ≤ 3 (10 sectors).
- **dual-SHA**: audit_sha256=`95b559c1e311536e0cbe6825c8b70200ba87e3bc917e84405456f65b4f8f4f9e` · content_sha256=`69685a6651de52ef6f724469885e18a070ff48e3edf46fb1e777b67a77456022`.

**Results**:

*Composite verdict (on-grid + |J(0)| rubric)* — all five conjuncts PASS: **(i)** grid_reaches_tau0 = True, **(ii)** |W(0)| ≤ 1e-12, **(iii)** max_θ|J(0;θ)| < 1e-12, **(iv)** Vilenkin excluded, **(v)** conservation residual < 1e-9 with Im(W)=0. ⇒ **PASS**.

*Substitution chain for W(0)=0 (with substituted numbers)* — Def: W(τ) := 2·G_DeWitt·(S(τ)−E), G_DeWitt = 5.0 (CONST-FREEZE-42). Set E := S(0) (regular-endpoint Hamiltonian-constraint normalization). On-grid S(0) is the DIRECT eigenvalue-sum **S(0) = 244839.08376120945**. Substitute: W(0) = 2·5.0·(244839.08376120945 − 244839.08376120945) = 2·5.0·0 = **0.0 EXACTLY**. Direction/threshold: W(0)=0 holds bit-exactly because E=S(0) AND τ=0 is a literal grid node (S(0) direct, not extrapolated). Contrast the W5-2 state: on the s63 τ_min=0.10 grid, S(0) is a `CubicSpline(0.0)` extrapolation ⇒ W(0)=0 is an extrapolated anchor ⇒ INFO. Placing τ=0 on the grid ⇒ S(0) direct ⇒ W(0)=0 on-grid ⇒ PASS.

*grid_reaches_tau0 honesty flag (Class-4 guard)* — set from `min(τ-grid) = 0.0 ≤ 1e-9` AND `S0_is_direct_eigsum = True`: S(0) is computed by `spectral_action_at_tau(0.0, …)` = Σ_{(p,q)} mult(p,q)·Σ_i|λ_i(p,q; τ=0)| directly from D_K(τ=0) (the undeformed SU(3); Jensen metric regular, volume-preserving L1·L2³·L3⁴=1), **NOT** a `CubicSpline(0.0)` value relabelled as on-grid. An extrapolated S(0) dressed as on-grid would be an ansatz-forced PASS (PROHIBITED Class-4 per `v3-closure-recovery.md`); it is explicitly excluded here.

*S(τ) cross-check vs `s63_kk_reduce_4d.npz`* — the extended-grid recompute reproduces the s63 `S_total_fine` at all **11** overlapping points [0.10, …, 0.30] to **max relative deviation = 2.35e-16** (machine precision; numpy `eigvalsh`, identical machinery). This certifies S(0) is the same eigenvalue-sum simply extended one node lower (0.10 → 0.0): e.g. S(0.10)=246355.31745979 reproduced exactly; S(τ) monotone increasing ⇒ S(0)=244839.08 < S(0.10).

*Real Robin self-adjoint family (J≡0)* — max_θ|J(0;θ)| = **0.0** over θ∈[0,π) (N_θ=181; θ=0 Dirichlet, θ=π/2 Neumann = S116-W6, θ→π⁻). J(0)=Im(Ψ*(0)Ψ'(0))=Im(sin θ·(−cos θ))=0 for every real boundary ratio; the real fundamental trajectory Ψ_θ = sin θ·u − cos θ·v is real ⇒ J(τ)≡0 (trajectory max = 0.0). Self-adjointness witness Im(cos θ / sin θ)=0 for all θ (max = 0.0).

*Vilenkin exclusion* — the complex outgoing BC Ψ'/Ψ = +ik gives J(0)=k|Ψ(0)|² = **234.98 > 1e-6** (non-vanishing net flux) and Im(A1/A2) = −k = −234.98 ≠ 0 ⇒ non-self-adjoint ⇒ **excluded**. Only the real Robin family is admissible, and it forces J(0)=0.

*Current conservation* — algebraic: dJ/dτ = Im(W)|Ψ|² = 0 since W = 2G(S−E) is strictly real (Im(W)=0.0 exactly). Numerical Wronskian witness on the oscillatory regime (E=S(τ_fold)=250360.68 ⇒ W ≤ 0 on [0,τ_fold] ⇒ bounded u,v): J(τ)=u·v′−v·u′ conserved at 1.0 with relative residual **8.70e-11 < 1e-9**.

*LABEL-only disclosure* — this gate upgrades only the verdict LABEL. The family-wide J≡0 theorem (every real separated self-adjoint / Robin extension forces J(0)=0 on [0,τ_fold]) was ALREADY established E- and W-magnitude-independently at S117 W5-2 (`s117_w5_wdw_j_rigor.py`, limit-circle Weyl-Titchmarsh; the four boundary-form identities Sage-verified). PASS adds the on-grid W(0)=0 anchor (τ=0 a literal node, S(0) direct) — **NOT new physics**. INFO would persist only if the grid could not place τ=0 as a clean node; FAIL would require some real Robin θ giving |J(0)|>1e-12 (a theorem-tension re-opening W5-2) — neither occurred.

*Substrate-first assessment (GEOMETRIC, Level-2 moduli-deformation substrate-IS)* — direction of explanation: D_K(τ) eigenvalues → spectral action S(τ)=Σ mult·Σ|λ| → WDW potential W(τ)=2G(S(τ)−E) → minisuperspace current J. The substrate IS the spectral triple (A_K, H_K, D_K(τ)); the Jensen τ-deformation manifold is itself substrate-IS (τ is the substrate's intrinsic deformation parameter, not a coordinate on a meta-container). τ=0 is the undeformed SU(3) — the cold-vacuum floor / unstable maximum (NOT a singularity; the metric is volume-preserving and well-defined there, confirmed by the clean direct S(0) eigenvalue-sum). **J≡0 across the entire real self-adjoint (Robin) family = no net amplitude flux through the τ=0 cold-vacuum floor under ANY unitary boundary law** — a substrate statement about the deformation manifold, derived FROM the spectral action, not imposed on a container. The on-grid W(0)=0 anchor sharpens the τ=0 endpoint from extrapolated to literal without altering the flux-free conclusion.

---

## Wave 3 Synthesis (team-lead)

Two independent low-leverage residuals on distinct substrates, both resolving as pre-registered (no permanent result altered):

- **3-1 `CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN` INFO** (sign=PASS / magnitude=INFO / regime=VALID). The §VII.AV.STATE-PROJ a₀-grade UV-regulator {ζ,PV,Mellin} span is **suppressed** once the BdG Fermi level is pinned substrate-first: ξ_F*=0.03655 (SOLVED from the s52 8-mode occupations, target mean(o_a)=0.0682 < ½ ⇒ ξ_F* below the |D_K| floor ⇒ a₀-grade UV modes empty; the anti-injection discipline held — ξ_F is the unique occupation-match root, never scanned to a target rel_span), so rel_span(ξ_F*)=**0.0391 ≤ 0.05** ⇒ OQ-4 closes as "suppressed". Robustness: ξ_F*(N) for N∈{8,16,32,64} all below floor. The sign leg is model-INDEPENDENT (additive-channel-dominant; the multiplicative M_R(s=4) channel annihilated to 5.17e-10 per the W8-2 multiplicative-normalization cancellation). The CC-in-microcosm scheme-dependence is **TAMED (suppressed), not killed**.
- **3-2 `CF-S118-WDW-S0-ONGRID` PASS** (the optional cosmetic label upgrade landed). τ=0 placed as a LITERAL grid node: S(0)=244839.08 computed DIRECTLY from D_K(τ=0) (reproduces s63 to 2.35e-16 = machine precision, certifying no extrapolation), |W(0)|=0 with E=S(0), max_θ|J(0;θ)|=0 across the real Robin θ-scan, Vilenkin excluded, conservation 8.70e-11. S117 W5-2 INFO → PASS. **LABEL-only**: the family-wide J≡0 theorem was already E- and W-magnitude-independent — PASS adds only the on-grid W(0)=0 anchor, no new physics.

**Solution-space (structural vs numerical):** both are (a) numerical/label refinements of already-settled structures — 3-1 bounds the magnitude of a STAGE-3-PERMANENT SD-OPEN observable (§VII.AV.STATE-PROJ L_emp=−7.046336 UNCHANGED; the `a_0^{<class>}` qualifier stays weak/suppressed SD-OPEN); 3-2 upgrades a verdict label on a theorem (J≡0) that already held. No (b) structural changes.

**Decision-point routing (plan terminal table):**
- 3-1 **INFO-stays** → OQ-4 closes "suppressed"; §VII.AV.STATE-PROJ qualifier UNCHANGED; **no mack-surface edit** (that is FAIL-promote-only); no carry-forward.
- 3-2 **PASS** → atlas-08 Q12 annotated "WDW W(0)=0 on-grid (S118 W3-2)"; the S117 W5-2 INFO superseded by the PASS (distinct gate-ID, no `supersedes=` needed); no carry-forward.

**Capstone-hygiene 5-Q gate:** Q1 (a(t)/Friedmann) NO (the WDW τ=0 BC does not alter the §6.3 substrate→FRW gap) · Q2 (§7 falsifier row) NO · Q3 (status change) NO (3-1 INFO: §VII.AV qualifier + L_emp UNCHANGED; 3-2: cosmetic label upgrade, the J≡0 theorem unchanged) · Q4 (prose) NO · Q5 (citation) NO. → No capstone reconciliation owed.

**Effected In-Session (NON-MATH):**
- [x] **atlas-08 Q12** (3-2 PASS) → "WDW W(0)=0 on-grid (S118 W3-2)" — both occurrences: LIVE DASHBOARD row (`atlas-08-open-questions.md:22`) + detailed Q12 entry (`:105-108`, new bullet). Orchestrator-direct.
- [x] **EVOI §EVOI.BF** (3-1 INFO) → lizzi-d.o.f.-cohort member-(iii) magnitude-band closure note (L_emp a₀-grade UV-regulator span bounded suppressed, rel_span(ξ_F*)=0.0391; OQ-4 "suppressed") — orchestrator-direct — `sessions/evoi-framework.md §EVOI.BF`.
- Self-audit: `grep -c '^- \[ \]'` over this block = 0.

## Carry-Forward Computations

No carry-forwards: all wave outcomes closed in-session. Both gates resolved as pre-registered (3-1 INFO-stays "suppressed"; 3-2 PASS cosmetic label upgrade) and neither routes a future-compute item — 3-1 is INFO not FAIL-promote (no §VII.AV magnitude-annotation gate owed), and 3-2 is the terminal cosmetic upgrade.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-29 | §VII.AV.STATE-PROJ a₀-grade UV-regulator span (OQ-4) | SD-OPEN, magnitude UNPINNED (W6-2 bounded by 3 heuristic vacuum models; rel_span=0.03118 at Fermi=zero) | SD-OPEN magnitude BOUNDED **suppressed** at the substrate-pinned ξ_F* (rel_span=0.0391 ≤ 0.05; ξ_F* below |D_K| floor); `a_0^{<class>}` qualifier UNCHANGED; L_emp=−7.046336 STAGE-3-PERMANENT UNCHANGED | `CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN` INFO |
| 2026-06-29 | WDW current J(0) / W(0)=0 anchor (Q12) | J≡0 PROVEN family-wide (S117 W5-2) but W(0)=0 EXTRAPOLATED off the τ_min=0.10 grid (INFO) | W(0)=0 ON-GRID (S(0) direct from D_K(τ=0); S117 W5-2 INFO → PASS) — LABEL-only, J≡0 theorem unchanged | `CF-S118-WDW-S0-ONGRID` PASS |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict (audit_sha256) |
|:-----|:-------|:------------|:------------|:-----------------------|
| CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN | `computations/session-118/s118_w3_lemp_oq4_vacuum_fermi_pin.py` | `…_lemp_oq4_vacuum_fermi_pin.npz` | `…_lemp_oq4_vacuum_fermi_pin.png` | `fb15f24e…` INFO (sign=PASS/mag=INFO/regime=VALID; + regulator_pin + counting_pin rows) |
| CF-S118-WDW-S0-ONGRID | `computations/session-118/s118_w3_wdw_s0_ongrid.py` | `…_wdw_s0_ongrid.npz` | `…_wdw_s0_ongrid.png` | `95b559c1…` PASS ([VERIFY], no 3-tuple) |
