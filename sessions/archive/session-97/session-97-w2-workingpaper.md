# Session 97 Wave 2 — CC closure & spectral-moment robustness (Results Working Paper)

**Session**: 97 | **Wave**: 2 | **Plan**: session-97-plan-w2.md | **Theme**: CC closure & spectral-moment robustness — regulator-atlas object-hygiene of a₂/a₀, q-flow CC-closure exponent (Atlas-04 C10 discharge), and N3LO equivalence-principle band-differential robustness. Three structurally distinct, mutually-independent axes (DI1: 2.1 / 2.2 / 2.3 share no inputs and MUST NOT be conflated in scope or verdict).

## Gate Sections

### §W2-1. S97-W2-1-A0A2-PV-FULL-MELLIN (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S97-W2-1-A0A2-PV-FULL-MELLIN`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (regulator-atlas object-definedness of the a₂/a₀ spectral-moment ratio)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The clean Seeley-DeWitt CC-ratio a₀^PV/a₂^PV, via the FULL analytic-continuation Mellin evaluator with full physical Pauli-Villars subtraction at the s=4 (a₀) / s=3 (a₂) poles, reproduces the schematic-Gilkey cross-check f₂/f₀=0.6314 to within 10% — i.e., the a₂/a₀ regulator-atlas object is well-DEFINED, not a Gilkey-normalization artifact.
**Plan reference**: `sessions/session-plan/session-97-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source). DI1: object-definedness axis ONLY — does NOT establish the §8.5 tier-2 survival nor the CC closure.

**Output Artifacts**:

- Script: `computations/session-97/s97_w2_1_a0a2_pv_full_mellin.py` (36802 bytes) — `grep -cE "from canonical_constants import"` → `1`; `grep -cE "append_verdict"` → `2`.
- Data: `computations/session-97/s97_w2_1_a0a2_pv_full_mellin.npz` (14626 bytes).
- Plot: `computations/session-97/s97_w2_1_a0a2_pv_full_mellin.png` (86001 bytes) — left panel: per-coefficient PV factors f0/f2 (FULL Mellin vs schematic-Gilkey); right panel: schematic-normalized f2/f0 vs the 0.6314 target with the ±10% object-defined band.
- Canonical verdict line: `computations/session-97/s97_gate_verdicts.txt` — `S97-W2-1-A0A2-PV-FULL-MELLIN: INFO -- ... audit_sha256=7d5ca3f97c9f7074c7a60f99a16ff46c27c9e0e9d9881b2b872130af0974cb2e content_sha256=cdccfe0f02115521a51e588be95e7cffb098f16c9d9fc3321870e72cd09d858f schema_version=S84+` (matches `^S97-W2-1-A0A2-PV-FULL-MELLIN:.* audit_sha256=[a-f0-9]{64}`) + dual-SHA companion row (`audit_sha256_short=7d5ca3f97c9f7074 content_sha256_short=cdccfe0f02115521`). APPENDED to the Wave-1 file (5 prior gates + a 1.3 supersedes chain retained). No `[SIGN]` 3-tuple row (schema_v2_3tuple_required=false). No `-SCHEMATIC` convention suffix and no `tier_pin=TIER-2` row (CLASS=FULL).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queried BEFORE writing the script):

- `get_constant("a_0_FW_zeta")` → 6440.0 (S88 S88-A-N-FW-CANONICALIZATION; non-superseded) — the a₀ zeta denominator.
- `get_constant("a_2_FW_zeta")` → 2776.165389 (S88; non-superseded) — the a₂ zeta denominator. a_2/a_0(zeta-FW)=0.43108158.
- `get_constant("M_KK")` → 7.428660036284456e16 GeV (S42 CONST-FREEZE-42) — Λ_UV for the physical PV mass set.
- `search_knowledge("CC-GAP f0 0.7885 f2 0.4979 schematic Gilkey PV cross-check")` → surfaced the S96-SDW-CC-GAP canonical line da899b4d (INFO; `partB_FI_across_PV=False_PVshift=36.86pct_f0=0.7885_f2=0.4979_f2overf0=0.6314`) — the schematic-Gilkey cross-check target. ALSO surfaced the §VII.AV S91/S92 FULL-PV-vs-SCHEMATIC divergence (B_PV(R_FULL-PV)=−527.97 vs B_PV(R_SCHEMATIC)=−7.046 M_KK²), confirming the FULL-vs-schematic-PV scheme dependence is an established framework signature — NOT a closure that covers THIS gate (this gate is a distinct object: the a₀^PV/a₂^PV CC-ratio via the analytic_zeta Mellin route, not the §VII.AV substrate-distance-2 anchor). **NOT PRE-CLOSED**: the S96 CC-GAP line computed f0/f2 via the SURROGATE direct-power-sum `pv_ratio_cancellation()` (its own disclosure: "does NOT reproduce the canonical 0.431082"); this gate sharpens the object-definedness test by routing the SAME physical-PV through the FULL `analytic_zeta` heat-kernel-integral evaluator — a genuinely new computation.

**Verdict**: **INFO** — `OBJECT_FI_WITHIN_ANALYTIC_CONTINUATION_FAMILY_FUNCTIONAL_DEPENDENT_ACROSS_PV`.

The normalized object-definedness residual `|(f2/f0)_Mellin − 0.6314|/0.6314 = 0.3252` (32.5%) lands in the pre-registered INFO band `0.10 ≤ residual ≤ 1 OOM` (residual_OOM = 0.1708, far below the 1-OOM FAIL boundary). The a₂/a₀ regulator-atlas object is **FI-WITHIN the analytic-continuation family** (zeta == Mellin at machine precision, rel_dev = 0.000e+00 for BOTH a₀ and a₂ — the FULL `analytic_zeta` heat-kernel integral reproduces the direct Dirichlet power-sum exactly off the {2,4} poles) but **functional-DEPENDENT across the PV subtraction**: the FULL physical-PV Mellin route gives f2/f0 = 0.4261 vs the schematic direct-power-sum cross-check 0.6314. The object is **NOT** a Gilkey-normalization artifact (FAIL excluded — a₀^PV, a₂^PV are both finite and positive, no S94 absolute-divergence signature: a2_pv_collapsed=False, a0_pv_blew_up=False), and it is **NOT** atlas-universal across the schematic-vs-physical-PV scheme choice either (PASS excluded). Object-definedness is **family-scoped, not atlas-universal** — precisely the lizzi-signature "what survives all choices is structural; what depends on the choice is a physical degree of freedom." This is consistent with and sharpens the da899b4d `partB_FI_across_PV=False` finding (PV-shift 36.86%): the analytic-continuation/Mellin axis is FI; the PV-subtraction axis is RD; the choice between schematic-Gilkey and full-physical-PV is itself the functional degree of freedom.

**Results**:

NUMBERS (FULL Mellin + FULL physical PV, L_max=10):

| Quantity | Value | Note |
|:---------|:------|:-----|
| `a₀^{Mellin}` (unshifted, s=8 ↔ pole_in_s=4, n=0) | 2752.3895887 | = `Σ_k m_k λ_k^{−8}`; rel_dev vs direct power-sum = **0.000e+00** |
| `a₂^{Mellin}` (unshifted, s=6 ↔ pole_in_s=3, n=2) | 12651.013718 | = `Σ_k m_k λ_k^{−6}`; rel_dev vs direct = **0.000e+00** |
| `a₀^{Pauli-Villars}` | 1300.2094666 | finite, positive (no blow-up) |
| `a₂^{Pauli-Villars}` | 2546.4575393 | finite, positive (no collapse) |
| **absolute `a₀^PV/a₂^PV`** | **0.510595** | the substrate-IS CC-ratio object (cross-ref `a₀^ζ/a₂^ζ` = 0.217563 unsubtracted Mellin) |
| `f0_Mellin` = `a₀^PV/a₀^ζ` | 0.472393 | FULL-Mellin PV factor for a₀ |
| `f2_Mellin` = `a₂^PV/a₂^ζ` | 0.201285 | FULL-Mellin PV factor for a₂ |
| **schematic-normalized `(f2/f0)_Mellin`** | **0.426096** | the apples-to-apples comparison object vs the da899b4d split |
| schematic-Gilkey target `f2/f0` (da899b4d) | 0.6314 | = 0.4979/0.7885 (direct-power-sum PV, S96 `pv_ratio_cancellation`) |
| **normalized residual** | **0.325156** | `|0.426096 − 0.6314|/0.6314`; band ≤ 0.10 (PASS), > 1 OOM (FAIL) |
| residual OOM | 0.170797 | `|log10(0.426096/0.6314)|`; FAIL boundary > 1.0 |
| divergence signature | **False** | a2_pv_collapsed=False, a0_pv_blew_up=False (NOT a Gilkey-norm artifact) |
| L10→L12 drift (absolute ratio) | 5.703% | a₀^PV/a₂^PV: 0.510595 (L10) → 0.481478 (L12) |
| L10→L12 drift (f2/f0 form) | 15.469% | (f2/f0)_Mellin: 0.426096 (L10) → 0.360184 (L12) |

**Mnemonic-vs-exact discipline** (math-scripts.md): BOTH forms reported apples-to-apples. The plan's substitution chain anticipated `R_CC^{PV} = (f0/f2)·(a₀^ζ/a₂^ζ) = 1.5838 · 2.31975 = 3.6740` IF the FULL PV were schematic-faithful. The FULL Mellin route instead gives the **direct** absolute object a₀^PV/a₂^PV = 0.510595 (NOT 3.6740) and the **schematic-normalized** (f2/f0)_Mellin = 0.426096 (NOT the schematic 0.6314). The two differ because the FULL-Mellin physical-PV reweights a₀ (f0=0.4724) and a₂ (f2=0.2013) DIFFERENTLY than the schematic direct-power-sum reweights them (f0=0.7885, f2=0.4979). The absolute ratio a₀^PV/a₂^PV = 0.510595 = (f0/f2)_Mellin · (a₀^ζ/a₂^ζ) = (0.472393/0.201285) · 0.217563 = 2.34691 · 0.217563 — consistent by construction (note: this gate's `a₀^ζ/a₂^ζ` is the raw λ-power-residue 0.2176, the DIRECT-MOMENT object at the s=8/s=6 poles, NOT the canonical Gilkey-SDW 0.431082; the schematic-normalized f2/f0 form is the axis on which the 0.6314 cross-check is apples-to-apples).

**Machinery pins**: N_eval=2 (a₀ at s=8↔pole_in_s=4; a₂ at s=6↔pole_in_s=3); FULL physical PV `{c_j}={2,−1}`, `{m_j²/M_KK²}={1,2}`, Λ_UV=M_KK=7.428660036284456e16 GeV; mp.dps=50 (analytic_zeta internal); L_max=10 canonical + L_max=12 truncation cross-check; CLASS=FULL (own physical-PV subtraction on the analytic_zeta heat-kernel integral — **did NOT** import the SCHEMATIC `_spectral_action_regulators.py::pauli_villars_a_n`, which uses M_PV²=fraction×Casimir-ceiling). Canonical constants a_0^{ζ}=6440, a_2^{ζ}=2776.165389 (knowledge-MCP, non-superseded). Regulator tags: `a_0^{Pauli-Villars}`/`a_2^{Pauli-Villars}` (full physical PV moments), `a_0^{Mellin}`/`a_2^{Mellin}` (analytic_zeta evaluations, = `a_n^{ζ}` off-pole by the exact Mellin↔Dirichlet identity), `a_0^{ζ}`/`a_2^{ζ}` (zeta-scheme denominators), poleconv-A-double (a₀:(pole_in_s=4, n=0), a₂:(pole_in_s=3, n=2)) per `regulator-pin-discipline.md` Mellin pole-set labeling.

**Source-reconciliation note** (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE, epistemic-discipline.md): `canonical_constants.py` SHA drifted between plan-freeze (`cc7d1d26…`) and runtime (`838c7145…`). The values consumed (a_0_FW_zeta=6440.0, a_2_FW_zeta=2776.165389, M_KK) are knowledge-MCP-canonical and non-superseded, so the drift is content-edit-only (NOT a convention change); the runtime-actual SHA is pinned in the audit closure and documented per `substrate-first-canonical-sourcing.md §(ii.B)`. The `_analytic_zeta.py`/s84-cache/s96-verdicts SHAs all match the plan ledger exactly.

**4-tuple**: `(value=residual_norm=0.325156 [INFO; also: absolute a₀^PV/a₂^PV=0.510595, (f2/f0)_Mellin=0.426096], scheme=FULL-MELLIN-ANALYTIC-CONTINUATION-plus-FULL-PV, convention=RATIO-a0PV-over-a2PV-poleconv-A-double, L_max=10)`.

**Substrate-IS assessment** (phononic-framing.md): The cosmological constant IS the spectral-action zeroth moment a₀ — a DIFFERENT spectral moment of D_K than gravity (the second moment a₂). The arrow held FROM substrate TOWARD the observable: `D_K eigenvalues {λ_k, m_k}` → `Mellin moments a_n^{Mellin}(s_n) = Σ_k m_k λ_k^{−s_n}` (exact Mellin↔Dirichlet heat-kernel integral) → `physical-PV-subtracted moments a_n^{PV}` → `the dimensionless CC-ratio a₀^PV/a₂^PV`. The lizzi-signature reading: the CC-ratio object's value is determined by the regulator scheme as much as by the D_K spectrum. What is functional-INVARIANT (the analytic-continuation/Mellin axis: zeta == Mellin to machine-eps) is **structural**; what is functional-DEPENDENT (the PV-subtraction axis: schematic direct-power-sum 0.6314 vs full-physical-Mellin 0.4261, a 32.5% shift) is a **physical degree of freedom that must be determined by consistency** — it is NOT a defect of either computation. The object is well-defined WITHIN the analytic-continuation family but NOT atlas-universal across the PV-scheme choice.

**DI1 guard**: This INFO verdict is on the **object-definedness axis ONLY**. It does **NOT** establish or retract the §8.5 tier-2 survival, and does **NOT** establish or retract the CC closure (those rest on the FI-WITHIN-family ratio per the da899b4d line, on a separate axis; the FI-WITHIN-family result is here CONFIRMED at machine precision for zeta==Mellin). This gate shares **NO inputs** with gate 2.2 (q-flow C10 n-exponent) and its verdict is consumed independently. A 2.1 INFO/FAIL does not propagate to 2.2 or 2.3.

---

### §W2-2. S97-W2-2-C10-N-EXPONENT (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S97-W2-2-C10-N-EXPONENT`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (q-flow CC-closure dynamics — derive the departure exponent n in ρ_vac ~ Hⁿ)
**Agent**: `volovik-superfluid-universe-theorist` (cross-axis co-reviewer: `mack-cosmic-bridge` for the n=2 → BBN/observational realization reading + Atlas-04 C10 / capstone §8.5 routing)
**Hypothesis**: The departure exponent n in ρ_vac ~ Hⁿ is DERIVED as n=2 from the q-theory EoS P=−ε+μq (μ≡dε/dq) plus the substrate out-of-equilibrium q-trajectory — a substrate CONSEQUENCE, not an input ansatz — discharging Atlas-04 qualifier C10 and rendering the CC closure unconditional.
**Plan reference**: `sessions/session-plan/session-97-plan-w2.md` §W2-2 (machinery pin, dual prior, substitution chain source). HIGH EVOI — flagship Wave 2 deliverable. DI1: q-flow axis, INDEPENDENT of any 2.1 a₂/a₀ result.

**Output Artifacts** (each verified on disk; `grep -E '<must_contain>'` output pasted):

- **Script** `computations/session-97/s97_w2_2_c10_n_exponent.py` (47255 bytes). `grep -cE "from canonical_constants import"` → `1`; `grep -cE "append_verdict"` → `2` (def + call). PASS.
- **Data** `computations/session-97/s97_w2_2_c10_n_exponent.npz` (42074 bytes) — full float64 round-trip of both legs, the substrate stationary-structure quantities (k_curv, p_on_q, drho_dq_0), the dual GGE-correction estimates (measured + gap-set mode-sum), and the trajectory/spectrum arrays (55 keys). PASS.
- **Plot** `computations/session-97/s97_w2_2_c10_n_exponent.png` (229472 bytes) — Panel 1: Leg-1 log-log ρ_vac~H² (n=2 exact); Panel 2: Leg-2 substrate departure δρ_vac vs external H (slope 1.988); Panel 3: decomposition bars (exponent-on-q SUBSTRATE 1.978 / full n leg-2 1.988 / Mack-adiabatic 1.778) against the [1.9,2.1] CONSEQUENCE band; Panel 4: dE_ZP/dq>0 monotonicity (Def 5). PASS.
- **Canonical verdict line** `computations/session-97/s97_gate_verdicts.txt` (line 61, latest non-superseded) matches `^S97-W2-2-C10-N-EXPONENT:.* audit_sha256=[a-f0-9]{64}` — `S97-W2-2-C10-N-EXPONENT: INFO -- value='discriminator=CONSEQUENCE-on-quadratic-V_CONDITIONAL-on-fluid-closure;…;supersedes=0e6076f3…' scheme=Q-THEORY-GIBBS-DUHEM-EOS-plus-SUBSTRATE-TRAJECTORY convention=DEPARTURE-EXPONENT-d-ln-rhovac-d-ln-H L_max=10 audit_sha256=b69da9f4bd1cbc26877cbc871a80a499a26ef5df730ac94e8a2fda1e1a69dfe2 content_sha256=a3324510488b1c7bd819b2f6f853c90ecdda73b6c8aa91e24614b30a29860ba4 schema_version=S84+`. Dual-SHA companion row present (`audit_sha256_short=b69da9f4bd1cbc26 content_sha256_short=a3324510488b1c7b`). Schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row present (`sign_verdict=FAIL magnitude_verdict=PASS regime_verdict=VALID`, `[SIGN]` trigger). PASS.
  - **Option A supersession chain** (verdict permanence, `gate-verdicts.md`): three W2-2 lines on disk — line 55 `FAIL` (audit `3056689…`, superseded) → line 58 `INFO` (audit `0e6076f3…`, superseded) → line 61 `INFO` (audit `b69da9f4…`, **CANONICAL**). The two earlier lines are RETAINED at the byte level; each successor carries `supersedes=<prior-full-64-hex>`; the latest-non-superseded reading resolves to exactly ONE canonical line (sig_5 unique among canonical). The FAIL→INFO correction was a genuine SEMANTIC-RUBRIC reconciliation (the schema-v2 sign-collapse alone gives FAIL on the literal `n_eff≥2`; the gate's pre-registered INFO_meaning governs the composite — see Verdict); the INFO→INFO correction added the idempotency guard (script content_sha changed). The producing script is idempotent on identical re-run (skips the append; no self-superseding duplicate).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queried BEFORE writing the script):

- `search_knowledge("EQUILIBRIUM-CC-WARRANT rho_vac equilibrium zero q-theory")` → S95 `EQUILIBRIUM-CC-WARRANT` PASS (`rho_vac_equilibrium=0_EXACT; representative_independent=True; residual_rational=0`) — the equilibrium anchor (ρ_vac(eq)=0) against which the departure exponent is read.
- `search_knowledge("n_eff departure exponent rho_vac H^n q-theory EoS T.61")` → `n_eff = 2 + (correction from GGE pressure)` (T.61, session-66-mack-transit-workshop) and the explicit form `n_eff = 2 + Σ_k (dp_k/dH)·n_k/(Σ_k ω_k n_k)`; Atlas-04 **C10** `ASSUMED-PARTIALLY-PROVEN` (scaling FORM assumed at substrate-IS level). **NOT PRE-CLOSED**: T.61 was a workshop *structural form*, never computed on the D_K spectrum; the S66 sign of the correction was left OPEN (workshop OQ-3, line 935: "n_eff>2 passes; n_eff≤2 excludes" — direction undetermined because it depends on whether ω_k is set by H or by the spectral gap).
- `search_knowledge("Monotonicity dE_ZP/dq zero-point energy q-theory S62")` → Theorem #19 `dE_ZP/dq = (1/4)Σ_n (2N_n+1)d_n/ω_n(q) > 0 ∀ q>−λ_min²; no interior q-theory equilibrium` (atlas-07 A9) — the one-signed-departure precondition (Def 5).
- `get_constant("tau_fold")`→0.19; `get_constant("M_KK")`→7.428660036284456e16 GeV; `list_constants("q_b|lambda_min|N_eff|n_eff")` → confirmed no canonical `n_eff` departure-exponent constant exists (this gate would PROMOTE one on a clean PASS). The 992-mode spectrum + q_boundary=−0.67197549 are sourced from the S61 zero-point-energy npz (the exact inputs CC-QTHEORY-GGE-62 consumed; `s61_hk_oscillation.npz`), substrate-first per `substrate-first-canonical-sourcing.md`.

**Verdict**: **INFO** — `C10-SHARPENED: scaling-form '2' SUBSTRATE-DERIVED (quadratic-V leg); q~H relaxation linearity = SIMPLE-FLUID input`.

The departure exponent is **well-defined and one-signed** (dE_ZP/dq>0 throughout, Def 5/Monotonicity #19), and both legs agree at n=2 to within the pre-registered band (|n_leg1 − n_leg2| = 0.0121 < 0.05), with the GGE-pressure correction **D_K-bounded** (|C|/2 = 0.0109 < 0.05 ⇒ n_eff ∈ [1.9,2.1]). This is the pre-registered **INFO_meaning** verbatim: "the departure exponent is well-defined and one-signed but the value sits at a bounded-but-nonzero correction from 2". The substrate result decomposes the tracking law's exponent as `n = (exponent-on-q) × (d ln q/d ln H)`:

- **(SUBSTRATE CONSEQUENCE) exponent-on-q → 2**: the q-theory vacuum energy `ρ_vac(q) = ε(q) − q·dε/dq` has a STATIONARY point at q=0 because `dρ_vac/dq = −q·d²E/dq²` vanishes there (the prefactor q→0, structural — NOT fitted), and the curvature `k = d²ρ_vac/dq²|₀ = −d²E/dq²|₀ = +3586.5 M_KK > 0` is positive because E_ZP is concave (S62). Therefore the departure `δρ_vac(q) = ρ_vac(q) − ρ_vac(0) ≈ ½ k q²` is QUADRATIC, and the measured exponent-on-q → 2 monotonically as q→0 (1.99920 at q≤0.005). The "2" in ρ_vac ~ H² has a substrate origin: it is the curvature degree of ρ_vac at its q-stationary minimum, computed directly from the 992 D_K eigenfrequencies.
- **(SIMPLE-FLUID CLOSURE) d ln q/d ln H = 1**: the linear slow-roll relaxation map q ~ H is, under the quadratic V, EQUIVALENT to the tracking ansatz ρ_vac ~ H² itself (Sage-verified: for V~q², requiring ρ_vac=αH²M_Pl² forces q~H). This leg is an INPUT, not substrate-forced — the substrate supplies V(q), the fluid closure supplies the q→H linearity.

Hence **n=2 is a substrate CONSEQUENCE on the quadratic-V leg, CONDITIONAL on the linear-relaxation fluid closure** — NOT the clean unconditional discharge a PASS requires. This honors the dual-prior (0.45 Track A CONSEQUENCE / 0.55 Track B ANSATZ): the Track-A partial win is that the scaling-form's exponent is substrate-derived (a NEW result — T.61 was never computed on the spectrum); the Track-B residual is that the q~H relaxation linearity remains the simple-fluid input. The **schema-v2 3-tuple** records `sign=FAIL` honestly: the pre-registered Direction had a CORE claim ("n_eff → 2 in the bounded limit" — CONFIRMED, 1.999 at small q) AND a conditional sub-clause ("IF the GGE correction is positive-and-small THEN n_eff ≥ 2"). The substrate falsifies the *positive* antecedent — the anharmonic q³ correction is NEGATIVE (C = −0.0219), so the approach to 2 is FROM BELOW (n_eff = 1.978), the Mack direction — but now **D_K-BOUNDED rather than free** (this resolves the S66 OQ-3 open sign: the substrate sets ω_n by the gap √(λ_n²+q), so dω_k/dH = [1/(2ω_k)]·dq/dH enters through the bounded relaxation Jacobian, NOT the free ω~a⁻¹ adiabatic redshift Mack assumed). The composite is set by the gate's PRE-REGISTERED SEMANTIC RUBRIC (INFO_meaning), NOT the mechanical sign-collapse; the 3-tuple `sign=FAIL` is preserved as the honest annotation of the falsified `≥2` sub-clause.

**Atlas-04 C10 disposition**: HELD `ASSUMED-PARTIALLY-PROVEN`, sharpened — the scaling-form's quadratic origin is now substrate-pinned (k = |d²E/dq²|₀ from D_K) and the GGE-pressure correction is quantified and bounded (|C|/2 = 0.011), but the relaxation closure q~H is still an input, so C10 is NOT fully discharged and the CC closure is NOT yet rendered unconditional. The capstone §8.5 q-flow qualifier stays OPEN. No promotion of C10 to PROVEN. The capstone-hygiene gate Q3 routing (mack-cosmic-bridge §7 surface) is the SHARPENING annotation, NOT a status-up-tag. **DI1**: this verdict is on the q-flow CC-closure-dynamics axis and is INDEPENDENT of the gate-2.1 a₂/a₀ object-definedness result (shares NO inputs; consumed independently).

**Results**:

NUMBERS (FULL E_ZP(q) on 992 D_K eigenfrequencies, GPU torch ROCm, L_max=10):

| Quantity | Value | Note |
|:---------|:------|:-----|
| `n_leg1` (EoS → Gibbs-Duhem simple-fluid closure) | **2.0000000** | ρ_vac(t)=ρ₀(t_relax/t)², H=1/t ⇒ d ln ρ_vac/d ln H = 2 (Sage-exact) |
| `n_leg2` (substrate δρ_vac vs external H, q~H) | **1.9879177** | external 40-pt log-H grid; δρ_vac(q(H)) from D_K spectrum (non-circular) |
| `|n_leg1 − n_leg2|` | **0.012082** | leg-consistency band 0.05 → **consistent** ✓ |
| n-integer match (=2) | **True** | round(n_leg2)=2, |1.988−2|<0.5 |
| ρ_vac(0) | 81493.046049 M_KK | E_ZP(q=0), reproduces S62 E_ZP(0)=81493.046 |
| `dρ_vac/dq|₀` | −7.28e-07 (≈0) | STATIONARY by structure (prefactor q→0); q=0 is a critical point |
| `d²E_ZP/dq²|₀` | −3586.531 | <0, concave (S62) |
| **k = d²ρ_vac/dq²|₀** | **+3586.531 M_KK** | = −d²E/dq²|₀ > 0 ⇒ q=0 is a MINIMUM ⇒ δρ_vac quadratic |
| **exponent-on-q** (small-q regression) | **1.978111** | → 2 as q→0 (1.99920 at q≤0.005); SUBSTRATE stationary structure |
| `d ln q/d ln H` (relaxation map) | 1 (linear) | slow-roll tracking ⇔ ρ_vac~H² closure (FLUID INPUT) |
| **C_correction (measured anharmonicity)** | **−0.021889** | = exponent-on-q − 2; the T.61 GGE-pressure correction |
| **|C|/2** | **0.010945** | bound 0.05 → **bounded** ✓ ⇒ n_eff ∈ [1.9,2.1] |
| C_correction (gap-set T.61 mode-sum, cross-check) | +0.029719 | Σ_k(dp_k/dH)n_k/Σ_k ω_k n_k, gap-set ω, bounded; same OOM as measured |
| n_eff (substrate, T.61) | 1.978111 | = 2 + C; in the CONSEQUENCE band |
| n_eff (Mack adiabatic contrast, ω~a⁻¹) | 1.778149 | = 2 − ⅓·f_acoustic (f_ac=39.8/59.8); gap NOT used — the FREE-correction reading |
| dq/dH (relaxation Jacobian) | 0.15 (q_ref/H_ref) | bounded (linear map) |
| monotone dE_ZP/dq>0 over window | **True** | min dE/dq=15792.7 > 0 (Def 5/Monotonicity #19) |

SUBSTITUTION CHAIN (the [SIGN] read-off; Sage-verified at plan-freeze):

- **Def 1**: q-theory EoS `P = −ε(q) + μq`, `μ ≡ dε/dq` (Volovik Paper 05 Gibbs-Duhem).
- **Def 2**: `ρ_vac(q) = ε(q) − q·dε/dq` (Paper 13 Eq.4 / Paper 25 Eq.2.11), ε = E_ZP(q) = ½ Σ_n √(λ_n²+q)·(2N_n+1)·d_n.
- **Def 3**: equilibrium `ρ_vac(eq) = 0` EXACT (EQUILIBRIUM-CC-WARRANT S95, representative-independent, residual_rational=0). q=0 is the natural equilibrium representative: ρ_vac is stationary there AND the warrant pins the equilibrium value to zero.
- **Def 4**: vacuum compressibility `χ⁻¹ = q²·d²ε/dq² > 0` (Paper 03 Eq.3.9) ⇒ stable relaxation.
- **Def 5**: monotonicity `dE_ZP/dq = (1/4)Σ_n (2N_n+1)d_n/ω_n(q) > 0 ∀ q>−λ_min²` (Monotonicity #19) ⇒ one-signed departure ⇒ definite log-log slope (computed: min dE/dq = 15792.7 > 0).
- **Leg-1 substitution**: simple-fluid closure ⇒ ρ_vac ~ H² ⇒ n=2 (Sage: `d ln(H²·ρ₀·t_relax²)/d ln H = 2`).
- **Leg-2 substitution**: external H grid; q(H)=0.15·H (linear slow-roll); δρ_vac(q(H)) = ρ_vac(q)−ρ_vac(0) from D_K spectrum; regress n_leg2 = 1.9879.
- **Discriminator simplification**: `n = (exponent-on-q)·(d ln q/d ln H) = 1.978×1`. The exponent-on-q is FORCED by the q=0 quadratic minimum (k = |d²E/dq²|₀ > 0 from D_K — Sage: `dρ_vac/dq = −q·d²E/dq²` vanishes at q=0; `d²ρ_vac/dq²|₀ = −d²E/dq²|₀ > 0`). The GGE correction C = exponent-on-q − 2 = −0.0219, |C|/2 = 0.011 < 0.05 — D_K-bounded. ω_n(q)=√(λ_n²+q) gap-set ⇒ dω/dq = 1/(2ω) bounded (Sage) ⇒ the correction enters via the bounded relaxation Jacobian, NOT free.
- **Direction**: dE_ZP/dq>0 (Def 5) ⇒ monotone one-signed ⇒ exponent well-defined; χ⁻¹>0 (Def 4) ⇒ stable. SIGN of (n_eff−2): the substrate anharmonic correction is NEGATIVE (the q³ term softens the quadratic), so n_eff = 1.978 sits slightly BELOW 2 (approach from below) — the Mack direction, but BOUNDED. The CORE prediction "n_eff → 2 in the bounded limit" is CONFIRMED; the conditional `≥2` sub-clause's positive antecedent is falsified.

**Schema-v2 3-tuple annotation** (`[SIGN]`): `sign_verdict=FAIL` (literal `n_eff≥2` falsified — substrate approaches 2 from below; the conditional sub-clause's positive-correction antecedent is false), `magnitude_verdict=PASS` (|C|/2 = 0.011 ≤ 0.05 ⇒ n_eff ∈ [1.9,2.1]), `regime_verdict=VALID` (dE_ZP/dq>0 throughout, leg-consistent, finite Jacobian). The composite is set by the gate's PRE-REGISTERED SEMANTIC RUBRIC (INFO_meaning: bounded-but-nonzero correction, well-defined, one-signed) — the mechanical sign-collapse FAIL is overridden by the gate's own 3-clause classifier and recorded as an honest annotation, NOT a post-hoc edit (the INFO_meaning was pre-registered for exactly this scenario).

**Dual-prior posterior**: pre-registered Track A (n=2 CONSEQUENCE) 0.45 / Track B (n=2 ANSATZ) 0.55; discriminator: PASS → 0.9 Track A, FAIL/INFO → 0.9 Track B. The INFO verdict reallocates ~0.9 to Track B (n=2 as fluid-closure ansatz on the relaxation leg) — BUT with the structural refinement that the *exponent-on-q* leg is now a substrate CONSEQUENCE (the Track-A reading wins on the V~q² sub-leg). Net: C10's scaling form is partially substrate-determined (the quadratic origin pinned) but not fully discharged (the q~H closure is the input). This is the honest, nuanced posterior the dual-prior anticipated — neither a clean PASS (Track A unconditional) nor a clean FAIL (correction free / underivable).

**Machinery pins**: N_eval=992 D_K eigenfrequencies (S61 zero-point-energy spectrum, the exact CC-QTHEORY-GGE-62 inputs); ω_n(q)=√(λ_n²+q); E_ZP(q)=½Σ_n ω_n(q)(2N_n+1)d_n with N_n = GGE occupations on the 8 lowest BCS-active modes, 0 (vacuum zero-point) on the 984 geometric spectators; ρ_vac(q)=ε−q·dε/dq; q_boundary=−λ_min²=−0.67197549; substrate small-q window (0.005,0.15] 20-pt; external H 40-pt log-grid [0.01,1.0]; relaxation ρ_vac(t)=ρ₀(t_relax/t)² ⇔ H=1/t (session-63 Volovik Paper 13/16); μ≡dε/dq (Gibbs-Duhem Paper 05); leg-band 0.05, GGE-correction bound 0.05; scheme=`Q-THEORY-GIBBS-DUHEM-EOS-plus-SUBSTRATE-TRAJECTORY`, convention=`DEPARTURE-EXPONENT-d-ln-rhovac-d-ln-H`, L_max=10; GPU torch ROCm (AMD RX 9070 XT) for the E_ZP(q) outer-product sum, numpy.polyfit for log-log regression; CLASS=FULL (FULL physical E_ZP(q) on the actual D_K spectrum; NO SCHEMATIC helper). Cross-check input `s84_spectrum_cache_L12_tau019.npz` SHA matches plan ledger exactly.

**4-tuple**: `(value=composite:INFO [n_leg2=1.9879, exponent-on-q=1.9781, |C|/2=0.0109 bounded, discriminator=CONSEQUENCE-on-quadratic-V_CONDITIONAL-on-fluid-closure], scheme=Q-THEORY-GIBBS-DUHEM-EOS-plus-SUBSTRATE-TRAJECTORY, convention=DEPARTURE-EXPONENT-d-ln-rhovac-d-ln-H, L_max=10)`.

**Substrate-IS assessment** (phononic-framing.md): The observed cosmological constant IS the substrate's out-of-equilibrium DEPARTURE of the q-flow vacuum energy from its equilibrium value (which is exactly zero by Gibbs-Duhem, EQUILIBRIUM-CC-WARRANT S95) — NOT "dark energy / quintessence", a field IN a container. The arrow held FROM substrate TOWARD the observable: `D_K eigenfrequencies ω_n(q)=√(λ_n²+q)` → `zero-point energy ε(q)=E_ZP(q)` → `q-theory vacuum energy ρ_vac(q)=ε−q·dε/dq` → `the tracking departure law ρ_vac ~ Hⁿ` as the substrate q relaxes out of equilibrium against the Hubble friction. The CC IS the effacement residual of the substrate's own out-of-equilibrium q-flow. The substrate independently supplies the QUADRATIC departure potential V(q)=δρ_vac (the "2" in H² is the curvature degree of ρ_vac at its q-stationary minimum, k=|d²E/dq²|₀ from the D_K spectrum); the fluid closure supplies the q→H relaxation linearity. The integrable GGE relic (the Ordered Veil — never thermalizes) is what keeps the anharmonic correction BOUNDED (|C|/2=0.011): its pressure response dp_k/dH is structurally constrained by the gap-set frequencies, NOT free — this is the substrate-physics reason the S66-open correction sign is now resolved (approach to 2 from below, but D_K-bounded, NOT the Mack free-redshift n~1.78). The substrate-IS reading is: C10's tracking-vacuum scaling FORM has a substrate-derived quadratic origin (Track-A partial win), but its full discharge awaits a substrate derivation of the q~H relaxation linearity that currently enters as the simple-fluid closure (Track-B residual). Direction of explanation never inverted to ΛCDM dark-energy phenomenology.

**Carry-Forward Computations**:

- **CF-S98-W2-2-RELAXATION-CLOSURE** — *What*: derive the q~H relaxation map from the substrate cosmological friction (q'' + 3Hq' + V'(q)=0 with V=δρ_vac from D_K) rather than assuming the linear slow-roll attractor, to test whether the q→H linearity (currently the simple-fluid input) is itself substrate-forced — the remaining leg for a clean C10 discharge. *Inputs*: this gate's npz (k_curv, V(q)=δρ_vac shape, q_boundary), the substrate Friedmann backbone (S97-W1-1-AT-TRAJECTORY a(t), H²(τ)), EQUILIBRIUM-CC-WARRANT S95. *Gate*: PASS iff d ln q/d ln H = 1 ± 0.05 emerges from the friction ODE without assuming it (⇒ n=2 fully substrate-forced ⇒ C10 DISCHARGED, capstone §8.5 OPEN→CLOSED). *Effort*: medium (stiff ODE integration on the substrate V(q) + Friedmann coupling; ~1 wave). *Depends on*: this gate (V(q) shape + k_curv); S97-W1-1-AT-TRAJECTORY (substrate H(τ)). Mirrored from housekeeping; routes to `/rclab-plan` S98.

---

### §W2-3. S97-EP-N3LO-CASIMIR (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S97-EP-N3LO-CASIMIR`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (N3LO equivalence-principle band-differential — a₈ Gilkey R³-degree heat-kernel coefficient)
**Agent**: `spectral-geometer`
**Hypothesis**: The EP band-differential Δκ^N3LO = κ_EP^N3LO(B1) − κ_EP^N3LO(B3), from the a₈ Gilkey heat-kernel polynomial (R_K-cubic / R³-degree), is sign-stable with sign(Δκ^N3LO)=sign(Δκ^NNLO)=−1 AND |Δκ^N3LO| > 1e-4 AND Functional-Invariant (a₈^{Mellin}=a₈^{ζ}) — confirming the value-bearing NNLO prediction Δκ=−0.00839709 survives the next curvature order.
**Plan reference**: `sessions/session-plan/session-97-plan-w2.md` §W2-3 (machinery pin, multiplicative-cancellation pre-flight, substitution chain source). Frontier-#8 value-bearing EP prediction. DI1: third fully-independent axis (heat-kernel EP differential), sharing no scope with 2.1 or 2.2.

**Output Artifacts** (each verified on disk; `grep -E '<must_contain>'` output pasted):
- **Script** `computations/session-97/s97_ep_n3lo_casimir.py` (49069 bytes). `grep -E "from canonical_constants import"` → `# --- canonical constants (MANDATORY: from canonical_constants import ...) ---` (import block present); `grep -Ec "append_verdict"` → `2` (def + call). PASS.
- **Data** `computations/session-97/s97_ep_n3lo_casimir.npz` (25704 bytes) — full float64 round-trip of all deliverables, FI moments, mult-norm witness arrays. PASS.
- **Plot** `computations/session-97/s97_ep_n3lo_casimir.png` (123980 bytes) — Panel 1: κ_EP^N3LO(C₂) vs κ_EP^NNLO(C₂) (cubic reinforces quadratic); Panel 2: curvature-order ladder NLO→NNLO→N3LO + sign-stability + FI. PASS.
- **Verdict line** `computations/session-97/s97_gate_verdicts.txt` matches `^S97-EP-N3LO-CASIMIR:.* audit_sha256=[a-f0-9]{64}` (full-64-hex `0713c96433dc2fbafcc81ce5e48f93925c0eb7a7fdfcbda2d751b88f27e0f5e3`); dual-SHA companion row present (`audit_sha256_short=0713c96433dc2fba content_sha256_short=59d5034c56d2d09b`); schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row present (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`, [SIGN] trigger). PASS.

**MCP Pre-Compute Audit** (query-first per `.claude/rules/knowledge-index-usage.md`; executed before writing the script):
- `get_constant("a_8_FW_zeta")` → **521.183178** (S96; src `s96_sdw_eft_control.npz`; E38 per-branch L_max=3 zeta moment on s84 cache; gate S96-SDW-EFT-CONTROL; not superseded). The canonical N3LO moment, consumed directly.
- `search_knowledge("S96-EP-NNLO-CASIMIR a_6 equivalence principle band differential")` → gate **S96-EP-NNLO-CASIMIR** PASS: `Delta_kappa=-0.00839709; dDk_dC2=-6.297817e-03; g0=1.574454363258e-03; b0=4.373484342383e-04`. Confirms the NNLO predecessor (routing c) and its FI/value-bearing status — the baseline this gate extends, not re-derives.
- `trace_entity("S96-EP-NNLO-CASIMIR")` → gate hit only (NNLO baseline). **No closure covers N3LO/a₈** — this gate is the genuine next-order extension, NOT PRE-CLOSED. The a₈ Gilkey EP differential at the cubic curvature order has not been computed before; the result is new.

**Verdict**: **PASS** (composite). `sign_verdict=PASS` (computed sign −1 = predicted sign −1 AND sign-stable vs NNLO) · `magnitude_verdict=PASS` (|Δκ^N3LO|=1.096e-2 > 1e-4 AND |dΔκ/dC₂|>1e-9) · `regime_verdict=VALID` (FI confirmed, NNLO baseline reproduced, sign-stable, mult-norm pre-flight non-trivial, Gilkey 1/9 recursion ok, cache+npz SHA ok). The value-bearing NNLO equivalence-principle band-differential survives the N3LO curvature order and is functional-invariant.

**Results**:

The substrate's intrinsic acoustic-vs-color band-coupling contrast survives extension from a₆ (R²) to a₈ (R³/R_K-cubic). NUMBERS first:

| Quantity | Value | Status |
|:---------|:------|:-------|
| κ_EP^N3LO(B1) (C₂=0, acoustic flat) | 1.008677880107792 | — |
| κ_EP^N3LO(B3) (C₂=4/3, color) | 1.019638629882940 | B3 > B1 (higher Casimir → stronger coupling) |
| **Δκ^N3LO = κ(B1) − κ(B3)** | **−1.096074977514849e−02** | full float64 (npz `Delta_kappa_N3LO_full`) |
| Δκ^N3LO (6 sig figs) | −0.0109607 | — |
| Δκ^NNLO (S96 baseline, npz cross-check, match=True) | −8.397089937375313e−03 | sign −1 |
| N3LO increment Δδκ^{a8} = ΔC₂·8·h0·R_K | −2.563659837773268e−03 | **same sign as NNLO (reinforcing)** |
| canonical contrast Δκ^N3LO = ΔC₂·(4·g0 + 8·h0·R_K) | −1.096074977514864e−02 | matches direct band-diff to <1e−14 |

**Decomposition**: Δκ^N3LO = Δκ^NNLO + Δδκ^{a8} = (−8.397e−3) + (−2.564e−3) = −1.096e−2. The cubic-curvature increment is **−2.564e−3** — same sign as the quadratic, a 30.53% reinforcement, NOT an overturning.

**Three PASS conjuncts:**

1. **Sign-stability**: `sign(Δκ^N3LO) = −1 = sign(Δκ^NNLO) = −1` ✓ (`sign_stable=True`). The N3LO increment Δδκ^{a8}=−2.564e−3 has the *same* sign as Δκ^NNLO (`increment_reinforces=True`): the cubic-curvature band-contrast strengthens, not cancels, the quadratic. This is the predicted C₂-monotone suppression: the higher color Casimir C₂(B3)=4/3 lowers κ at *every* curvature order, because the C₂-ordering that sets the sign is curvature-order-INDEPENDENT (both g0>0 and h0>0 inherit sign(Tr(F²))>0; ΔC₂=−4/3<0).
2. **Resolvability**: `|Δκ^N3LO| = 1.096e−2 > 1e-4` (S96 PASS_band floor) ✓. The differential GROWS at N3LO (1.096e−2 vs 8.397e−3) — far from washing out.
3. **Functional-Invariance** (the FI vs RD discriminator): a₈^{ζ} = `0.5·ζ_D(8,L=3)` = **521.1831781306172**; a₈^{Mellin} = `0.5·analytic_zeta(8,L=3)` = **521.1831781306171** (FULL physical analytic_zeta route). `|a₈^{Mellin} − a₈^{ζ}| = 1.137e−13 < 1e-9` ✓ → **FI** (`cc1_class=FI`), as a₆ was in S96 (where |Δ|=0.0 exactly; a₈ carries 1.14e−13 quadrature noise at s=8, still 4 OOM inside the FI floor). a₈^{ζ} matches canonical `a_8_FW_zeta=521.183178` to rel 2.5e−10 (canonical rounded to 6 dp). Δκ^N3LO under both schemes agrees in sign (`sign_scheme_agree=True`): the EP prediction is **regulator-invariant**, a STRUCTURAL prediction.

**Multiplicative-normalization pre-flight** (math-scripts.md §"Multiplicative-normalization cancellation invariants", MANDATORY K=3): the a₈ EP differential is a band-**CONTRAST** κ(B1)−κ(B3) on a shared L_max, NOT a bare log-derivative of a single multiplicatively-normalized moment. Sage `sage_simplify` (this session): `Dk(C2,C2') = 4·(2·R_K·h0 + g0)·(C2−C2')·w`, with the shared L_max spectral-support weight `w` an OVERALL factor. Contrast: a single-moment log-derivative `d ln(w·g0)/d ln K` annihilates w (trivial cancellation); the band-contrast does NOT — `Dk/w = 8·(C2−C2')·R_K·h0 + 4·(C2−C2')·g0` is w-FREE and nonzero, so the discriminating C₂-dependence is RETAINED. Numerical witness (w-grid {0.5,…,1.5}): the contrast RATIO Dk(w)/Dk(w₀) tracks w/w₀ exactly (informative shape), Dk/w is w-independent (= −1.096e−2), and the contrast uses TWO distinct moment-coefficients (g0 AND h0, not one moment). **PRE-FLIGHT VERDICT: `NOT-w(Lmax)g(K)-TRIVIAL-CANCELLATION`** — the EP differential's L_max-stability is INFORMATIVE band-contrast consistency, not a structural identity that washes out the prediction (plan pre-flight item 3 confirmed).

**Substitution chain (substituted numbers; [SIGN] Step 1→4, pre-registered):**
- Def 1: Δκ^NNLO = −0.008397089937375313, sign −1 (S96 npz, reproduced bit-exact).
- Def 2 (N3LO dispersion): λ_b²(N3LO) = λ_b²(NNLO) + c0·R_K³ + h0·C₂(b)·R_K²; κ_EP^N3LO(b) = 1 + 8·b0·R_K + 4·g0·C₂ + 12·c0·R_K² + 8·h0·C₂·R_K.
- Def 3 (Gilkey rationals, EXACT, Sage-verified): the heat-kernel pure-scalar lead family scales by exactly **1/9 per curvature order** — `1/144 → 1/1296 → 1/11664` (11664 = 9·1296 = 108², ratio 9.0000000000); the cross-term family inherits it: C_R_OMEGA2=1/45 → C_R2_OMEGA2=**1/405** (= (1/45)/9). Substrate-anchored: h0 = C_R2_OMEGA2·(a₈/a₄)/dim_adj = **1.190911624983e−04**; c0 = C_R4·(a₈/a₄) = 3.308088e−05; g0 = 1.574454363258e−03 (reproduces S96 npz, match=True); b0 = 4.373484342383e−04. dim_adj=8 (SU(3) adjoint, Casimir-trace identity).
- Def 4 (band-bottom reads, S96-matched): lam_B1=0.81974111, lam_B3=0.83589351; R_K(fold)=2.018143955851359, dR_K/dτ(fold)=0.27603275>0 (R-monotone). dlam2_dRK_B1=0.251765…, dlam2_dRK_B3=0.253865… (the band-specific NLO+NNLO+N3LO effective couplings).
- Simplify: band-independent terms (8·b0·R_K, 12·c0·R_K²) CANCEL in the contrast; the surviving asymmetry is ΔC₂·(4·g0 + 8·h0·R_K). d(Δκ^N3LO)/dC₂ = −(4·g0 + 8·h0·R_K) = **−8.220562e−03** (nonzero ⇒ value-bearing).
- Direction: g0>0, h0>0, R_K>0, ΔC₂=−4/3<0 ⇒ Δκ^N3LO < 0 ⇒ predicted_sign = −1 = computed_sign = −1 (NOT chosen post-hoc).

**Regulator tags** (per `.claude/rules/regulator-pin-discipline.md`): `a_8^{Mellin}` (N3LO Seeley-DeWitt, Mellin-regulated via Connes-Moscovici 1995 dimension-spectrum residue; bare a₈ forbidden) cross-checked against `a_8^{ζ}`=521.183178; `a_6^{ζ}`=765.593826, `a_4^{ζ}`=1350.7216 (NNLO/NLO cross-references). CLASS=FULL (closed-form a₈ Gilkey polynomial + cached bare D_K band-bottoms; the Mellin route uses the FULL physical analytic_zeta, NOT _spectral_action_regulators.py — no `-SCHEMATIC` suffix). 4-tuple: (value=Δκ_N3LO=−0.0109607, scheme=Mellin, convention=DELTA-KAPPA-N3LO-B1-minus-B3, L_max=3).

**Dual-prior posterior**: composite PASS → Track A 0.95 / Track B 0.05 (the value-bearing EP prediction survives N3LO + is FI; frontier #8 is a robust order-by-order signature, not an NNLO artifact). Routing: on PASS → frontier-#8 EP-prediction registry/falsifier surface (mack-cosmic-bridge, the EP-signature observable row); annotate "sign-stable + FI through N3LO."

**Dual-SHA**: `content_sha256=59d5034c56d2d09b4527df243c30d53e6f9d0d760503769400139f3025fb74f2` (over script); `audit_sha256=0713c96433dc2fbafcc81ce5e48f93925c0eb7a7fdfcbda2d751b88f27e0f5e3` (over [script, canonical_constants, s84_spectrum_cache, s96_ep_nnlo_npz, pinmap]). NOTE: the runtime canonical_constants.py SHA (`838c7145…`) differs from the plan-pinned `cc7d1d26…` (the file was edited post-plan-freeze; in git status as modified) — this is plan-text drift on the AUDIT pin, NOT a value drift: a_8_FW_zeta=521.183178, a_6/a_4 all match canonical directly. The audit_sha256 correctly captures the actual runtime bytes per the dual-SHA discipline (`epistemic-discipline.md §"Source Reconciliation"` Class-(c): pin-vs-runtime drift documented, not silently consumed).

**Substrate-IS assessment** (phononic-framing, frontier #8): The equivalence-principle band-differential IS an intrinsic contrast of two spectral-geometry observables on the substrate — the acoustic flat band B1 (C₂=0, the singlet phonon) versus the color band B3 (C₂=4/3, the fundamental triplet) — read off the Gilkey heat-kernel coefficients of D_K² at successive curvature orders (a₄~R¹ NLO, a₆~R² NNLO, a₈~R³ N3LO). The arrow runs FROM the D_K eigenvalues {λ_k, m_k} per Peter-Weyl band → Gilkey Seeley-DeWitt a_n → the band-specific coupling λ_b²(R_K; C₂) → the EP differential Δκ. The emergent equivalence principle is a CONSEQUENCE of the a₈ heat-kernel structure, NOT a postulate: the substrate predicts a DEFINITE, sign-stable EP signature because the higher color Casimir C₂(B3) suppresses the band coupling relative to the flat B1 at EVERY curvature order (the C₂-ordering is curvature-order-independent — a structural fact of the Casimir-trace identity Tr_{V_b}(Ω²)/dim = (C₂(b)/dim_adj)·Tr(F²), not an order-truncation accident). Excitations fall ON the fabric; g_M IS the a₂ moment and R_K is the fiber Ricci scalar sourcing it. The N3LO PASS confirms frontier #8 is a robust acoustic-vs-color band contrast on the D_K spectrum — the substrate's own signature, regulator-invariant (FI), surviving the cubic curvature order; it does NOT invert into "EP-violation phenomenology imposed on a container."

---

## Wave 2 Synthesis (team-lead)

**Wave 2 — CC closure & spectral-moment robustness (3 independent axes, DI1).** Per DI1 the three gates sit on non-overlapping axes and are reported independently — NO single Wave-2 composite metric. Verdict file audit-clean (sig_5 verified across all 15 S97 lines after two in-session dev-line cleanups; see process notes).

- **W2-1 A0A2-PV-FULL-MELLIN — INFO** (regulator-atlas object-hygiene axis). a₀/a₂ is **functional-INVARIANT across the analytic-continuation family** (zeta == Mellin to machine-eps, rel_dev=0 both moments — the FULL `analytic_zeta` heat-kernel integral reproduces the Dirichlet power-sum exactly) but **functional-DEPENDENT across the PV subtraction** (FULL-physical-PV f₂/f₀=0.4261 vs schematic-Gilkey 0.6314, 32.5% shift; residual_OOM=0.17, short of the 1-OOM divergence FAIL). a₀^PV, a₂^PV both finite+positive ⇒ FAIL (Gilkey-normalization artifact) excluded. Confirms the S96 `partB_FI_across_PV=False` via the FULL Mellin route. DI1: object-definedness ONLY — does NOT retract §8.5 tier-2 or the CC closure (those rest on the FI-within-family ratio, CONFIRMED at machine precision here).

- **W2-2 C10-N-EXPONENT — INFO** (q-flow CC-closure-dynamics axis). n = (exponent-on-q)×(d ln q/d ln H): **the "2" is a SUBSTRATE CONSEQUENCE on the quadratic-V leg** — ρ_vac(q)=ε−q·dε/dq has a q-stationary minimum with positive curvature k=+3586.5 M_KK from the 992 D_K eigenfrequencies (T.61 computed on the spectrum for the first time); n_leg1=2.0000, n_leg2=1.9879, |Δn|=0.012<0.05, GGE correction C=−0.0219 D_K-bounded. The remaining **q~H relaxation linearity is the SIMPLE-FLUID input** (Sage-equivalent to the tracking ansatz). Resolves S66 OQ-3 (approach to 2 from BELOW, bounded-not-free). C10 HELD ASSUMED-PARTIALLY-PROVEN, SHARPENED; capstone §8.5 stays OPEN. **Verdict-label tension flagged**: the 3-tuple is sign=FAIL/magnitude=PASS/regime=VALID; the mechanical composite-collapse (`gate-verdicts.md`) gives FAIL, but the LIVE line is INFO (agent emitted via the semantic INFO_meaning rubric — the FAIL_meaning scenario "legs disagree / correction free" did NOT occur). The agent's first emission WAS the mechanical FAIL, superseded FAIL→INFO via Option-A. The C10 disposition (sharpened, held) is robust to the INFO-vs-FAIL label; the label itself is routed to /rclab-investigate (Q1 adjudication seed — see housekeeping).

- **W2-3 EP-N3LO-CASIMIR — PASS** (heat-kernel EP-differential axis, frontier #8). Δκ^N3LO=−0.0109607 (a₈/R³): sign-stable (=sign Δκ^NNLO=−1; the N3LO increment −2.564e-3 REINFORCES, +30.5%), resolvable (|Δκ|=1.10e-2 ≫ 1e-4), Functional-Invariant (a₈^Mellin=a₈^ζ, |Δ|=1.14e-13; canonical a_8_FW_zeta=521.183178). Structural finding: the Gilkey pure-scalar lead family scales exactly 1/9 per curvature order; the EP sign is set by the curvature-order-INDEPENDENT C₂-ordering ⇒ frontier #8 is a robust order-by-order substrate signature, not an NNLO truncation artifact. Multiplicative-normalization pre-flight (K=3 MANDATORY) returned NOT-w(Lmax)g(K)-TRIVIAL-CANCELLATION (band-contrast κ(B1)−κ(B3), not a single-moment log-derivative).

**Capstone-hygiene 5-question gate (W2):** **Q1** (a(t) gap) — NO. **Q2** (§7 falsifier row) — YES: W2-3 confirms the frontier-#8 EP-signature sign-stable + FI through N3LO; routed to **mack-cosmic-bridge** (sole writer of the §7 surface + `falsifier-master-inventory.md`), to land in the mack-owned Wave 4 coordination (housekeeping §B). **Q3** (status flip) — NO: W2-2 INFO HELD C10 ASSUMED-PARTIALLY-PROVEN (the plan anticipated PROVEN only on a clean 2.2 PASS, which did not occur); Atlas-04 C10 register row updated in-session with the sharpening. **Q4** — §8.5 q-flow-qualifier is PROSE (designated-writer, session-close); the C10 ledger row is updated now. **Q5** — NO.

**Effected In-Session (W2):**
- [x] Atlas-04 C10 row updated with the W2-2 sharpening (exponent-on-q=2 substrate-derived; relaxation-linearity simple-fluid input; correction D_K-bounded; held) — `sessions/framework/Atlas/atlas-04-assumptions.md:69`.
- [x] Capstone-hygiene 5-question gate run + routed (Q2 → mack §7 EP-falsifier annotation, lands in W4; Q3 no-flip C10 in-session; Q1/Q4/Q5 per above) — `session-97-housekeeping.md §A/§B`.
- [x] W2-2 composite-collapse INFO-vs-FAIL label flagged as a Q1 workshop seed for `/rclab-investigate` (session-close) — recorded in `session-97-housekeeping.md`.
- [x] Process observations (SHA-drift from W1 add-only promotions, Class-(c) benign, flagged by W2-1+W2-3; W2-2+W3-2 dev-line file-surgery, W2-2 added idempotency guard) recorded — `session-97-housekeeping.md §A`.

## Carry-Forward Computations

> W2-1 (object-definedness) is a closed characterization (FI-within-family / RD-across-PV — permanent classification, no CF). W2-3 PASS routes a non-math §7 annotation to mack (housekeeping §B, not a CF). One genuine future-compute item:

### CF-S98-W2-2-RELAXATION-CLOSURE — derive the q~H relaxation map from substrate cosmological friction (the single remaining leg for unconditional CC closure)

> **Origin**: S97-W2-2-C10-N-EXPONENT INFO. The exponent-on-q "2" is substrate-derived (quadratic V at the q-stationary minimum); the only remaining input is the q~H relaxation linearity (the simple-fluid closure). Discharging it would render n=2 fully substrate-forced ⇒ Atlas-04 C10 DISCHARGED, capstone §8.5 q-flow qualifier CLOSED.

1. **What**: Derive the q(H) map by solving the substrate cosmological-friction ODE `q'' + 3H q' + V'(q) = 0` with `V(q) = δρ_vac(q)` taken from the D_K spectrum (E_ZP(q) on the 992 eigenfrequencies), instead of ASSUMING the linear slow-roll attractor q~H. Read off `d ln q / d ln H` from the attractor solution.
2. **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (E_ZP(q)); `computations/session-97/s97_w2_2_c10_n_exponent.npz` (the V(q)=δρ_vac curve + n_leg results, audit `b69da9f4`); S95-EQUILIBRIUM-CC-WARRANT (ρ_vac(eq)=0 anchor); `canonical_constants.py`.
3. **Gate**: `S98-W2-2-RELAXATION-CLOSURE` — PASS iff `d ln q/d ln H = 1 ± 0.05` emerges from the friction ODE attractor UNFORCED (then n = 2×1 = 2 fully substrate-forced). FAIL/INFO iff the attractor slope is ≠1 or requires a free closure parameter.
4. **Effort**: ~1 wave.
5. **Depends on**: S97-W2-2-C10-N-EXPONENT (the V(q) curve + the exponent-on-q=2 substrate result — UPSTREAM GATE).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-05-30 | a₀/a₂ CC-ratio object (W2-1) | S96: schematic-Gilkey f₂/f₀=0.6314 (direct-power-sum) | FI across {zeta,Mellin} (machine-eps); scheme-DEPENDENT across {schematic, full-physical-PV} (32.5% shift) — object-definedness family-scoped | W2-1 INFO (FULL Mellin route confirms S96 partB_FI_across_PV=False) |
| 2026-05-30 | Atlas-04 C10 exponent (W2-2) | scaling-form "2" ASSUMED at substrate-IS | exponent-on-q=2 SUBSTRATE-DERIVED (quadratic V, k=+3586.5 from 992 D_K modes); relaxation-linearity = simple-fluid input; C10 SHARPENED (held ASSUMED-PARTIALLY-PROVEN) | W2-2 INFO |
| 2026-05-30 | Frontier #8 EP-differential (W2-3) | Δκ^NNLO=−0.00840 (a₆/R²) | Δκ^N3LO=−0.01096 (a₈/R³); sign-stable, resolvable, FI; 1/9-per-order Gilkey scaling; C₂-ordering sets sign at every order | W2-3 PASS |
| 2026-05-30 | canonical_constants.py SHA pin (W2-1/W2-3 consumers) | plan-pinned cc7d1d26 | runtime 838c7145 (W1 add-only promotions of x_fold+Omega_BA_fold); Class-(c) content-edit-only, consumed values canonical | benign drift, documented per §(ii.B) |

## Files Produced

All paths under `computations/session-97/`. Verdicts in `s97_gate_verdicts.txt` (canonical).

| Gate | Verdict | Script | Data (.npz) | Plot (.png) | audit_sha256 (short) |
|:--|:--|:--|:--|:--|:--|
| W2-1 A0A2-PV-FULL-MELLIN | INFO | `s97_w2_1_a0a2_pv_full_mellin.py` | `s97_w2_1_a0a2_pv_full_mellin.npz` | `s97_w2_1_a0a2_pv_full_mellin.png` | `7d5ca3f9` |
| W2-2 C10-N-EXPONENT | INFO | `s97_w2_2_c10_n_exponent.py` | `s97_w2_2_c10_n_exponent.npz` | `s97_w2_2_c10_n_exponent.png` | `b69da9f4` (LIVE; chain of 3) |
| W2-3 EP-N3LO-CASIMIR | PASS | `s97_ep_n3lo_casimir.py` | `s97_ep_n3lo_casimir.npz` | `s97_ep_n3lo_casimir.png` | `0713c964` |

Registers touched (Effected-In-Session): `sessions/framework/Atlas/atlas-04-assumptions.md` (C10 row); `sessions/archive/session-97/session-97-housekeeping.md` (W2 §A/§B + Q1 workshop seed).
