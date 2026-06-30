# Session 102 Wave 4 — Fermion-mass / particle sector (Results Working Paper)

**Session**: 102 | **Wave**: 4 | **Plan**: session-102-plan-w4.md | **Theme**: rank-9b fermion-mass / particle-sector live edge — per-generation quark kernel, first-principles κ_ν, neutrino generation grading, Model-C phenomenology, M₀-screening transfer convention, and the no-PDG-appeal m_H route-selection that KEYS the Wave-5 BF-spine refresh.

## Gate Sections

### §W4-15. CF-S102-QUARK-PERGEN-KERNEL (paasch-mass-quantization-analyst)

**Status**: COMPLETED
**Gate ID**: `CF-S102-QUARK-PERGEN-KERNEL`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (per-generation dressed-block kernel for the quark mass crossing)
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: a substrate-DERIVED per-generation slope kernel (per-gen κ_g / non-monotone ω_g) reproduces the gen-1 inversion m_u/m_d<1 AND gen-3 upright m_t/m_b>1 simultaneously — which W2-4 proved impossible for any uniform (κ_up, κ_down) pair — with [SIGN] preserved and the W3-9 walls + [J,D_K]=0 intact.
**Plan reference**: `sessions/session-plan/session-102-plan-w4.md` §W4-15 (machinery pin, thresholds, crossing-condition + selection-rule pre-flight substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-102/s102_quark_pergen_kernel.py` — PRESENT (34676 B). `grep`: `from canonical_constants import` ✓ (×2), `print_verdict_payload` ✓.
- `computations/session-102/s102_quark_pergen_kernel.npz` — PRESENT (15938 B, 58 keys, full float64).
- `computations/session-102/s102_quark_pergen_kernel.png` — PRESENT (124237 B, 3-panel: slope-asymmetry / crossing-vs-PDG / triality-masked CKM proxy).
- Verdict line — PRESENT: `^CF-S102-QUARK-PERGEN-KERNEL:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + [SIGN] 3-tuple row ✓ + 2 extra companion rows. `audit_sha256=77659eb6809d3d461d5e41f42eaec37dd831516773c1b2883624b6c57cc32c49`, `content_sha256=bb326f601b7b39df8a7639f5ce473eba4c930059d7fff59f1c859b59fdb29a27` (sig_5 unique; emitted via `emit_verdict` MCP).
- This WP section — Status COMPLETED, Verdict, Output Artifacts, MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit** (per `.claude/rules/epistemic-discipline.md` query-first discipline):
- `search_knowledge("quark per-generation kernel up down crossing uniform kappa impossibility W2-4")` → returned the S101-W3-QUARK-COMPONENT-ORIENTATION gate (`crossing=False; uniform=True; ud_g1=1.1203`) + the plan's own substitution-chain equations. Confirms the live edge is open; NOT PRE-CLOSED.
- `search_knowledge("CKM misalignment up-sector down-sector eigenbasis dressed block quark mass ratio")` → returned the S99 bridge map `V_CKM = U_up† U_down`, `U_sector = eigenbasis of [[d,w],[w*,d]]^sector` (the canonical CKM construction; arg(w) lives in the diagonalizing unitary, Connes' eigenvector result).
- `trace_entity("quark mass crossing per-generation slope asymmetry")` / `trace_entity("W2-4 uniform kappa impossibility")` → no trace (no prior closure of the per-gen DERIVED kernel; this gate IS the first attempt).
- `get_constant(m_u_msbar_2GeV)=0.00216`, `get_constant(m_d_msbar_2GeV)=0.0047` → held-out gen-1 anchor m_u/m_d = 0.4596 (PDG 2024 MS-bar). `get_constant(m_t_pole)=172.69`, `get_constant(m_b_msbar_mb)=4.183` → held-out gen-3 anchor m_t/m_b = 41.28. `get_constant(phi_paasch)=1.53158` (mass-quantization framing anchor; not consumed numerically here).
- **Conclusion**: result is NOT already known/closed/canonical. The W2-4 uniform-κ impossibility is canonical (S101 INFO); the DERIVED per-gen resolution is the open question this gate evaluates.

**Verdict**: **FAIL** — sign=FAIL, magnitude=FAIL, regime=VALID (composite collapse: `sign_verdict==FAIL ⇒ FAIL`, canonical `gate-verdicts.md` rule, unmodified). The joint quark up/down crossing is NOT forced by any substrate-natural per-generation kernel: the corridor CLOSES (W2-4 impossibility EXTENDS from uniform-κ to the substrate-DERIVED per-gen kernel). Dual prior → **Track B** (0.9). FAIL is informative — it pins the quark generation crossing as OUTSIDE substrate-derived reach on the dressed-block off-diagonal/diagonal kernel, and routes the open question to a κ_g-derivation workshop (a genuinely-new substrate ingredient is required).

**Results**:

*NUMBERS first.* Substrate ingredients loaded from `s101_w3_quark_component_orientation.npz` (SHA `ec666fbd…`, matches plan pin). Per generation (gen3↔(1,0), gen2↔(1,1), gen1↔(3,0); C₂-descending mass map):

| gen | sector | C₂ | d_up = √⟨λ²⟩_c | d_dn = √⟨λ²⟩_D | w_up (greybody) | w_dn (greybody) | r_g = (d+\|w\|)_up/(d+\|w\|)_dn |
|:----|:-------|:---|:---------------|:---------------|:----------------|:----------------|:-------------------------------|
| 3   | (1,0)  | 1.333 | 1.29642 | 1.83341 | 0.005170 | 0.000274 | **0.70982** |
| 2   | (1,1)  | 3.000 | 1.56732 | 2.21653 | 0.083025 | 0.027032 | 0.73559 |
| 1   | (3,0)  | 6.000 | 1.96289 | 2.77594 | 0.388204 | 0.346503 | **0.75296** |

- **Dressed-block construction**: physical mass = heavier eigenvalue of `B_g^S = [[d_g^S, w_g^S],[w_g^S*, d_g^S]]`, i.e. `m_{g}^S = d_g^S + |w_g^S|`. Diagonal `d_g^S` = bare-ladder RMS (√ of the multiplicity-normalized trace-mean ⟨λ²⟩_g^{(comp)} = Ω^{comp}·mean(|λ|²)); off-diagonal `w_g^S` = the S101-W3 greybody-transmitted envelope `√Ω^S·exp(−2πC₂(g)τ_fold/κ^S)`. Both substrate-derived; NO PDG in the kernel.
- **Joint-crossing verdict**: gen-1 inversion (r_1 < 1) = **True** (r_1 = 0.7530); gen-3 upright (r_3 > 1) = **FALSE** (r_3 = 0.7098 < 1). **crossing_realized = False.**
- **Diagonal floor**: r_g(|w|=0) = d_up/d_dn = √(Ω^c/Ω^D) = √(1/2) = **0.70711 at EVERY generation** (the bare ⟨λ²⟩ cancels in the up/down ratio — only the Ω-scalar survives). Up is intrinsically lighter on the diagonal; the dressing must overpower the floor to flip gen-3.
- **Held-out PDG (NOT fitted)**: gen-1 m_u/m_d = 0.4596 → DERIVED r_1 = 0.7530, rel = **63.8%** (> 30% band, > 60% info-band → FAIL). gen-3 m_t/m_b = 41.2838 → DERIVED r_3 = 0.7098, rel = **98.3%**. gen-2 m_c/m_s = 13.615 (reference).

*Crossing-condition substitution chain (with substituted numbers).* Per plan §W4-15 Step 1–5:
- **Step 4 (binding analytic constraints)**: gen-3 upright needs `(w_up,3 − w_dn,3) > (d_dn,3 − d_up,3) = +0.53699`; substrate supplies `w_up,3 − w_dn,3 = +0.00490` → **FALSE** (short by 2 OOM — the greybody dressing is exponentially suppressed at gen-3's LOW C₂). gen-1 inversion needs `(w_up,1 − w_dn,1) < (d_dn,1 − d_up,1) = +0.81305`; substrate supplies `+0.04170` → True (trivially, because the dressing is small everywhere).
- **Step 5 (sign read-off)**: crossing is reachable IFF the DERIVED per-gen slope asymmetry `(κ_g^up − κ_g^down)` (with κ_g^S ≡ |w_g^S|/d_g^S) CHANGES SIGN between g=1 and g=3. DERIVED values: **gen3 = +0.00384, gen2 = +0.04078, gen1 = +0.07295** — POSITIVE at all three, monotone-increasing, **NO sign flip** (`signflip = False`). The Step-5 crossing condition is VIOLATED → **sign_verdict = FAIL** (the predicted-direction sign structure is not realized by the substrate).
- **Root cause (substrate-physics)**: the gen-3 upright condition needs a LARGE up-dressing at gen-3 (the (1,0) low-C₂ sector), but the greybody transmission `exp(−2πC₂τ/κ)` makes the dressing exponentially SMALLEST exactly there; and gen-1 sits at the HIGHEST C₂, where any C₂-monotone up-dressing makes gen-1 the MOST up-heavy — the opposite of inversion. The slope asymmetry is structurally same-signed across all generations; the substrate provides no sign-changing per-generation kernel.
- **Route (b) exhausted**: a non-monotone ω_g(C₂) needs a strict dip/peak in the MIDDLE (gen-2) generation. The substrate quantities across (gen3,gen2,gen1) are C₂ = [1.333, 3.0, 6.0] (strictly monotone), triality t = [1, 0, 0] (a binary STEP at gen-3, not a gen-2 dip/peak), irrep dim = [3, 8, 10] (strictly monotone). **No substrate quantity is non-monotone across the three generations** → `routeb_seed = False`. Route (b) has no substrate seed.

*CKM = U_up† U_down misalignment + selection-rule pre-flight (the structural PASS sub-result).* Triality CG-admissibility, t(p,q) = (p−q) mod 3:
- **Intra-sector dressing** (the mass off-diagonal w_g, mass operator t(O)=0): admissible at ALL generations (t(a)==t(a)+0). The dressed-block construction is triality-clean — every claimed nonzero off-diagonal element passes the pre-flight.
- **Inter-generation CKM channels** (W/mass mixing, t(O)=0): gen3↔gen2 (t=1 vs t=0) → **FORBIDDEN** (exact zero); gen3↔gen1 (t=1 vs t=0) → **FORBIDDEN** (exact zero); gen2↔gen1 (t=0 vs t=0) → **admissible** (the Cabibbo channel). The triality-masked generation-space mixing proxy is `M[gen2,gen1] = 0.1534`, `M[gen3,*] = 0` exactly. **Cabibbo-dominant texture = True; gen-3 channels triality-suppressed = True.** This is a genuine substrate prediction: the third generation `(1,0)` sits in a distinct triality class, so V_ub and V_cb are triality-suppressed relative to the Cabibbo V_us — qualitatively the observed CKM hierarchy. (This sub-result stands independent of the crossing FAIL; it is a clean triality theorem on the inter-generation channels.)

*Machinery cross-checks (all PASS).* Ω^D/Ω^c = 8/3 ÷ 4/3 = **2.000000000000000** (dev 0.0e+00, ≤ 1e-12 VALID, Sage-QQ-exact). W3-9 sign-direction: diagonal ⟨λ²⟩ ascends with C₂ (mass C₂-descending, gen-3 heaviest) = **True**, intact; [J,D_K]=0 / freeze-in sign-PASS preserved. PDG held-out anchors reproduced exactly by canonical_constants (m_u/m_d = 0.00216/0.0047 = 0.4596 ✓; m_t/m_b = 172.69/4.183 = 41.284 ✓, Sage-cross-checked). regime_verdict = **VALID** (triality pre-flight holds ∧ Ω ratio exact ∧ W3-9/[J,D_K]=0 intact).

*4-tuple*: `(value=<r_g1=0.7530;r_g3=0.7098;crossing=False;signflip=False;…>, scheme=FW, convention=RATIO, L_max=10)`.

*[SIGN] 3-tuple dual-SHA*: `sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=VALID`; `audit_sha256=77659eb6…cc32c49`, `content_sha256=bb326f60…fdb29a27`.

*Substrate framing.* PARTICLE-class. Direction of explanation preserved: D_K dressed-block eigenvalue ratios → per-generation slope asymmetry → quark mass ordering + CKM texture. The content lives in the SPLITTING `m_{g,±} = d_g ± |w_g|` and the RATIO r_g — not in the absolute eigenvalues (14 OOM above the physical scale via M_KK). The FAIL is a substrate-physics boundary: the dressed-block off-diagonal/diagonal kernel — the only substrate-natural per-generation slope structure available from S101 W3 — supplies a same-signed slope asymmetry at all three generations and an exponentially-suppressed dressing at gen-3, so it cannot produce the gen-1↔gen-3 sign-changing asymmetry the crossing demands. The corridor closes; the quark generation crossing requires a substrate ingredient NOT present in the dressed-block greybody kernel (carry-forward to a κ_g-derivation workshop). The CKM triality texture (Cabibbo-dominant, gen-3 channels suppressed) is the structural payoff that survives.

*Artifacts*: `s102_quark_pergen_kernel.py` / `.npz` / `.png`.

---

### §W4-16. CF-S102-KAPPA-NU-FIRSTPRINCIPLES (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `CF-S102-KAPPA-NU-FIRSTPRINCIPLES`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (greybody-derived Dirac-neutrino shape slope)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: the greybody construction on the s84 B-branch FORCES s_ν = +0.5469 from the (c²−v²) gradient ALONE — derived independently of the S99 Y-ratios W3-3 back-solved against, sign-flip preserved — upgrading s_ν from consistent-but-not-forced to DERIVED.
**Plan reference**: `sessions/session-plan/session-102-plan-w4.md` §W4-16 (machinery pin, RATIO 1% threshold, sign-flip substitution chain, back-solve guard).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-102/s102_kappa_nu_firstprinciples.py` — present; contains `from canonical_constants import *` and `print_verdict_payload` (both `must_contain` patterns satisfied).
- **data** `computations/session-102/s102_kappa_nu_firstprinciples.npz` — present (38 keys: `s_nu_primary`, `s_nu_greybody`, `s_nu_fullrange`, `s_nu_cache`, `kappa_blv`, `lambda_om`, `E_B1/E_B2/E_B3`, `lam_tower`, `sign_*`, `guard_clean`, dual-SHA, …).
- **plot** `computations/session-102/s102_kappa_nu_firstprinciples.png` — present (3-panel: B-branch M_R(C₂); independent-construction ledger vs target; FORCED sign-flip geometry).
- **verdict_line** `computations/session-102/s102_gate_verdicts.txt` — `CF-S102-KAPPA-NU-FIRSTPRINCIPLES: INFO …` with full-64-hex `audit_sha256`, dual-SHA companion row, and `[SIGN]` 3-tuple row (sign=PASS / magnitude=FAIL / regime=VALID), plus a `# composite-precedence:` disclosure row.
- **wp_section** this section (Status COMPLETED, Verdict, Output Artifacts, MCP Pre-Compute Audit — all present).

**MCP Pre-Compute Audit**:
- `search_knowledge("kappa_nu greybody neutrino shape slope s_nu Dirac sign-flip")` → surfaced gate **S101-KAPPA-NU-GREYBODY = INFO** with the verbatim self-disclosure `mag=INFO_OPEN_compare-to-self(both=ln(Y3/Y2)/(5/3))_not-independently-derived`. This IS the open problem the gate closes — NOT pre-closed; the S101 magnitude was a tautology, this gate supplies the independent derivation.
- `search_knowledge("s84 B-branch spectrum eigenvalue crossing neutrino normal ordering")` → PROVEN `Normal mass ordering from bowtie structure` + S52 ordering; confirmed B-branch is the singlet/SU(2) fold spectrum.
- `search_knowledge("B-branch B1 B2 B3 fold energy bowtie …")` → S52 `s52_sector_ordering.txt`: at τ=0.19, **B1(0.819741) < B2(0.835894) < B3(0.872975)**; B1=singlet/U(1), B2=C²-generator (×2), B3=SU(2).
- `search_knowledge("c squared minus v squared gradient …")` + `search_knowledge("Kitaev exit rate 2 pi T a4 …")` → BLV analog surface gravity **κ = ½ ∂_n(c²−v²)|_horizon** (the (c²−v²) gradient IS the sector surface gravity); Kitaev anchor 2πT(a₄)=κ_exit.
- `get_constant`: `tau_fold=0.19`; `M_KK=7.42866e16 GeV`; `v_ew=246`; `E_B1=0.8191400`, `E_B2_mean=0.8452691`, `E_B3_mean=0.9782239` (B-branch fold energies = seesaw M_R, all canonical, imported — not hardcoded). `kappa_exit`/`Vol_SU3` not canonical pins (carried as locals with provenance).
- `trace_entity("s84 B-branch spectrum c2-v2 gradient")` → no direct trace; B-branch defined via the S52 ordering + s84 cache read directly.
- **Not pre-closed.** No closure covers an *independent* (Y-ratio-free) kappa_nu derivation; the S101 INFO explicitly routes this to "the forward gate."

**Verdict**: **INFO** (composite). `sign_verdict=PASS`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`. Track B: the sign-flip to +0.5469 is substrate-FORCED, but the magnitude +0.5469 is NOT forced by the B-branch (c²−v²) gradient — it was a coincidence of the S99 Y-ratio back-solve. Re-pins candidate-(c) at the derived magnitude.

**4-tuple**: `(value=s_nu_pred=+0.0876501 …, scheme=FW, convention=ABSOLUTE, L_max=10)`.
**dual-SHA**: `audit_sha256=1bc8e08eb55b7de93637a5ef6a84997c70f571cecee2be2f1bdbbeafd92e5933`, `content_sha256=469e65594b9cfd6cbf6080ff63bd75a2c5b0452093afab6b3d659b98c1e5fd0b`.

**Results** (NUMBERS first, gate second, interpretation third):

*Independent derivation (Y-ratio-FREE; substrate-first D_K → spectral moment → emergent shape).* The Dirac-neutrino envelope rides the seesaw m_ν = m_D²/M_R, with M_R = the B-branch D_K fold energies (capstone §5.3). The PRIMARY independent shape slope is the B-branch fold-energy log-gradient between the graded gen-2/gen-3 sectors (the II.3 (1,0)/(1,1) Casimir gap ΔC₂ = 5/3):

| Independent construction (NO Y-ratio) | s_ν | rel-to-target |
|:--------------------------------------|----:|--------------:|
| **PRIMARY** d ln M_R/dC₂ = ln(E_B3/E_B2)/(5/3) | **+0.0876501** | 0.8397 |
| greybody-bare 2π·λ_om/κ_blv | +6.891373 | 11.5997 |
| full-range ln(E_B3/E_B1)/3 | +0.059161 | 0.8918 |
| s84-cache cross-check d ln\|λ\|_min/dC₂ | +0.026043 | 0.9524 |

Canonical B-branch fold energies (M_KK, imported): E_B1=0.819140 (C₂=0), E_B2=0.845269 (C₂=4/3), E_B3=0.978224 (C₂=3). (c²−v²) sector surface gravity κ_blv = ½ d(c²)/dC₂ = 0.072733 M_KK; frequency-map slope λ_om = dE_B/dC₂ = 0.079773. s84-cache cross-check (independent file `s84_spectrum_cache_L12_tau019.npz`, N_eval=240 nu-tower eigenvalues): min|λ| = [0.819741, 0.835894, 0.872975] M_KK — confirms the gradient is O(0.03), same order as the PRIMARY.

*Magnitude verdict.* Target +0.546948; |s_ν^pred − target|/|target| = **0.8397 ≫ 0.01** → magnitude FAIL. Every substrate-natural independent construction lands at [0.026, 0.092] (8–20× BELOW target; the greybody-bare overshoots at 6.89). **No construction forces the target at 1%** (best rel-to-target = 0.8397). The +0.5469 value is reproduced ONLY by the S101 back-solve ln(Y3/Y2)/(5/3) = 0.5469481, which feeds the Y-ratios — explicitly NOT used here (`s84-cache-contrast`, for reference only).

*Back-solve guard.* `back_solve_guard` performs AST source-introspection on `compute_s_nu_independent()` with the docstring stripped: forbidden token set {`S_NU_TARGET`, `Y2_NU`, `Y3_NU`, `SHAPE_YRATIO`} — **0 hits in executable code** (guard CLEAN). (The first run tripped on the docstring's own statement of the guarantee; the AST-strip is the robust fix — verified all four tokens appear in_docstring=True, in_executable_code=False.) The independent derivation references NO Y-ratio / target.

*Sign substitution chain (FORCED to +1, widening; substituted numbers):*
- Step 1 — `sign(gv_response) = sign(e^{-τ_fold})·sign(Vol_SU3)·sign(J_C2)·sign(kernel)` [S84-s5], `sign(kernel) = −1`.
- Step 2 — `e^{-τ_fold} > 0` (τ_fold=0.19 real) ⇒ `sign(e^{-τ_fold}) = +1`; `Vol_SU3 > 0` ⇒ `+1`.
- Step 3 — `= (+1)·(+1)·sign(J_C2)·(−1) = −sign(J_C2)`. From the B-branch: `dE_B/dC₂ = +0.079773 > 0` ⇒ `sign(dE_B/dC₂) = +1`; the seesaw m_ν=m_D²/M_R INVERTS the Dirac-envelope frequency map ⇒ `J_C2 = −sign(dE_B/dC₂) = −1`.
- Step 4 — `sign(gv_response) = −sign(J_C2) = −(−1) = +1` ⇒ s_ν^pred > 0 (WIDENING).
- Step 5 — required +1 (II.3 widening) → **sign PASS**. The sign chain uses ONLY τ_fold, Vol_SU3>0, the kernel convention, and sign(dE_B/dC₂) from the B-branch spectrum — NO Y3/Y2. **Sign is substrate-FORCED.**

*[SIGN] 3-tuple:* `sign_verdict=PASS` (direction +1 matches the II.3 widening prediction); `magnitude_verdict=FAIL` (|s_ν^pred − target|/|target| = 0.84 ≫ 1%, and no independent construction forces the target); `regime_verdict=VALID` (κ_blv=0.0727>0 AND E_B monotone E_B3>E_B2>E_B1, so the B-branch dispersion is non-degenerate throughout).

*Composite collapse (plan-frozen operator precedence; disclosed via `# composite-precedence:` row).* The plan §W4-16 `dual_prior`/`INFO_meaning` PRE-REGISTERS the "derivable at a DIFFERENT magnitude" outcome as **INFO (Track B re-pins candidate-c)**, NOT FAIL — FAIL is reserved for the sign-flip itself failing. Hence `sign=PASS ∧ magnitude=FAIL ∧ regime=VALID → composite=INFO` under the plan operator, OVERRIDING the generic collapse (`magnitude=FAIL ∧ regime=VALID ⇒ FAIL`). The override is disclosed in a mandatory `# composite-precedence:` extra-row per `gate-verdicts.md §"plan-frozen gate-block operator precedence"`.

*Methodology / operational deviation (honest disclosure).* The plan pinned `GPU_path: torch.linalg` ("s84 B-branch spectrum ≥ 100×100 per-block"). The s84 per-block eigenvalues are **pre-computed and cached** in `s84_spectrum_cache_L12_tau019.npz`; this gate READS the cached |λ| and performs scalar log-gradient arithmetic — no GPU eigensolve is needed. The machinery pin records the actual path `cpu-cap-OMP8 (s84 per-block eigvals pre-cached; scalar log-gradient arithmetic)`. This is an in-session operational deviation honestly disclosed (not convention-shopping): the spectrum was diagonalized once in S84, and re-diagonalizing it would change no number.

**Substrate framing**: PARTICLE-class. The Dirac-neutrino shape slope s_ν is a signed spectral property of the s84 B-branch — D_K B-branch eigenvalue gradient → (c²−v²) sector surface gravity → greybody transmission → neutrino shape slope. The **sign** of the slope is intrinsic to the spectral geometry (`sign(gv_response) = −sign(J_C2)`, J_C2 read off the same B-branch gradient): the widening sign-flip is substrate-FORCED, not an input. The **magnitude** question — is it EXACTLY +0.5469? — is answered NO: the B-branch (c²−v²) gradient gives s_ν ≈ 0.088 (8× below the back-solved target), so the +0.5469 magnitude was a coincidence of the S99 Y-ratio fit, not a substrate consequence. The absolute Dirac SCALE remains a structural wall and is NOT a gate here (per the gate's `fb_pair.backward`).

**Constraint-map update**: candidate-(c) (the s_ν = +0.5469 neutrino shape slope) is re-pinned: **SIGN substrate-derived/FORCED (+, widening); MAGNITUDE NOT forced** — the independent B-branch gradient yields s_ν ≈ 0.088, so the shape SPECIES (widening) is forced but the specific value +0.5469 is a back-solve coincidence. The neutrino-sector solution space corridor "s_ν widens with C₂" is forced; "s_ν = +0.5469 exactly" is NOT. Forward: an independent absolute-Dirac-scale derivation (the structural wall) would be needed to close the magnitude; the shape-pair gates downstream consume the FORCED sign, not the magnitude.

---

### §W4-17. CF-S102-NU-GRADING-EXTERNAL-EPSLX (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `CF-S102-NU-GRADING-EXTERNAL-EPSLX`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (external non-LI ε_LX grading for the neutrino shape leg)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: an external non-LI ε_LX structure (the §VII.BL corollary: a fibre connection breaking W2 while preserving the grading) supplies the neutrino shape steepness Y_3/Y_2 = 2.4882512 (rel ≤ 5%) — which the gap equation provably could not (W3-4 +39.7%) — while the gap equation supplies the scale (×8.6–10.5).
**Plan reference**: `sessions/session-plan/session-102-plan-w4.md` §W4-17 (machinery pin, RATIO 5% + scale-band threshold, division-of-labor substitution chain).

**Verdict**: **INFO** — the external non-LI grading DOES reproduce the neutrino generation shape Y_3/Y_2 = 2.4882512 (rel err 5.3e-09 ≪ 5%) with the gap-eq scale leg in-band ([8.6377, 10.4878] ⊂ [8.6, 10.5]), but the required ε_LX magnitude is the residual back-out (HELD, NOT substrate-motivated). Pre-registered INFO_meaning fires verbatim: re-route to a fibre-connection-geometry derivation workshop. Dual-prior discriminator → not Track A, not Track B; the INFO branch (external structure lifts the grading, ε_LX value is a fit).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-102/s102_nu_grading_external_epslx.py` — script. `grep` confirms `from canonical_constants import` (L73) and `print_verdict_payload` (def L286 + call L387). PRESENT.
- `computations/session-102/s102_nu_grading_external_epslx.npz` — data. PRESENT (27 keys: C2, Y_S99, missing_slope, geps_ratio_from_slope, Y3Y2_full, shape_rel_err, scale_in_band, eps_LX_substrate_motivated, verdict, …).
- `computations/session-102/s102_nu_grading_external_epslx.png` — plot (left: ln(Y_g/Y_2) slopes, gap-eq flat 0.2433 vs gap+ε_LX required 0.5469, ε_LX shape-leg fill; right: Y_3/Y_2 bar — gap-eq 1.5 / full 2.4883 / required 2.4883 with ±5% band). PRESENT.
- `computations/session-102/s102_gate_verdicts.txt` — verdict line `^CF-S102-NU-GRADING-EXTERNAL-EPSLX: INFO …  audit_sha256=a3e1cf7b…995652` + dual-SHA companion row. PRESENT (emitted via race-safe `emit_verdict`).
- This WP section — Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit. PRESENT.

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("Generation-Blindness Obstruction VII.BL external non-LI fibre connection")` → §VII.BL STAGE-3-PERMANENT (S99 W3-1), corollary design rule: discharging the hierarchy REQUIRES an external non-LI fibre connection breaking W2 while preserving the grading. NOT a closure of THIS gate.
- `search_knowledge("neutrino generation grading Y_3 Y_2 shape steepness 2.4882512")` → S101-D5-MD-GAPEQ INFO (`shape_dev=0.3972, r_sol=9.5179, scale-in-band, shape-FAIL`); S60 lepto Y_2=4.79357, Y_3=11.92760. Confirms the W3-4 +39.7% shape-FAIL and the W3-1 target.
- `trace_entity("Generation-Blindness Obstruction")` → single PROVEN theorem node (proven_1002), STAGE-3-PERMANENT.
- `get_constant("R_cross")` → no exact; `R_cross_yukawa_t1_t2 = 1.019704` (the LI residual; provenance: external ε_LX is "NON-PROMOTION-BY-HELD-NUMBER (sign-lock); HELD number, NOT a framework prediction; local-diagnostic-anchor", S97).
- `get_constant("epsilon_LX")` / `get_constant("d_lnYreq_dC2")` / `get_constant("delta_A_nLI")` → ALL not found. **No canonical magnitude pins the external connection strength** — the decisive substrate-motivation discriminator.
- `search_knowledge("epsilon_LX external connection strength fibre geometry …")` → S97 W3 plan: `A_nLI = A_homog + δA`, "the STRUCTURAL POSIT (pinned, NOT discovered at runtime)" — existence/necessity posit, no derived δA magnitude.
- **PRE-CLOSED?** NO. §VII.BL (necessity of the external connection) is closed; this gate operationalizes whether a *substrate-motivated* ε_LX realizes the required steepness — distinct, uncomputed.

**Results**:

*Substrate framing* — PARTICLE-class. Direction: D_K fibre-connection geometry (external non-LI part) → generation-graded shape factor g_ε(C_2(g)) → neutrino Y_3/Y_2 steepness, with the gap-eq scale orthogonal. The §VII.BL Generation-Blindness Obstruction is a STRUCTURAL wall: the left-invariant fibre structure of D_K is generation-blind up to the permanent residual R_cross = 1.019704 (STAGE-3-PERMANENT, multiplicity-scalar π(a)=⊕π_(p,q)(a)⊗1; Skolem-Noether multiplicity-blind). The gap-equation route inherits this blindness — its generation SHAPE is nearly flat (scale cancels in any generation ratio).

*Inputs (S101 D5 gap-eq npz; both SHAs match plan pins)* — generation Casimirs C_2(g) = {0, 4/3, 3} (Peter-Weyl sectors (0,0)/(1,0)/(1,1)); W3-1 required Yukawas Y_S99 = {0, 4.79357, 11.92760} (oscillation/seesaw-anchored); ΔC_2 = C_2(3)−C_2(2) = 5/3; required log-slope d_lnYreq_dC2 = 0.5469481; gap-eq SOLVED log-slope d_lnYsol_dC2 = 0.2432791 (KS-LINEAR stationarity); scale leg rescale_B/rescale_A = 8.6377 / 10.4878 (r_sol = 9.5179).

*Division-of-labor substitution chain (substituted numbers)*:
- **Step 1 (definitions)**: Y_g = Scale_gap · h(C_2(g)); §VII.BL ⇒ h nearly flat across generations.
- **Step 2 (gap-eq shape ratio — scale cancels)**: (Y_3/Y_2)^gap = h(C_2(3))/h(C_2(2)) = exp(d_lnYsol·ΔC_2) = exp(0.2432791·5/3) = **1.5000000**. Shortfall (req−gap)/req = +0.397167 — **reproduces the npz `shape_dev` to 0.00e+00** (the W3-4 +39.7%-too-flat result). The Scale_gap CANCELS in the ratio ⇒ the gap eq provably cannot fix the shape.
- **Step 3 (external ε_LX grading)**: Y_g^full = Scale_gap · h(C_2(g)) · g_ε(C_2(g)); (Y_3/Y_2)^full = (Y_3/Y_2)^gap · (g_ε,3/g_ε,2).
- **Step 4 (canonical form / division of labor)**: scale leg from the gap eq (in-band); shape leg from ε_LX. Required g_ε,3/g_ε,2 = 2.4882512 / 1.5 = **1.6588341**; equivalently exp(missing_slope·ΔC_2) with missing_slope = d_lnYreq − d_lnYsol = 0.5469481 − 0.2432791 = **0.3036690** per unit C_2. Consistency |needed − slope-form| = 2.22e-16 (exact).
- **Step 5 (direction read-off)**: the gap eq is shape-flat (scale cancels); ONLY the external non-LI grading lifts the steepness. **Sign verdict: PASS** (the missing steepness is positive — d_lnYreq > d_lnYsol — and is supplied by the external leg, matching the pre-registered claim that the gap eq cannot and an external grading must). Full reconstruction (Y_3/Y_2)^full = 1.5 · 1.6588341 = **2.4882512**, rel err vs target = **5.3e-09 ≪ 5%**.

*Scale leg* — gap-eq scale window [8.6377, 10.4878] ⊆ band [8.6, 10.5]. **scale_in_band = True.**

*Substrate-motivation discriminator (PASS vs INFO)* — the shape leg CAN always hit the target because the required external grading is EXACTLY the residual back-out (req/gap == exp(missing_slope·ΔC_2) to 2.2e-16). The decisive test is whether the ε_LX connection-strength magnitude is INDEPENDENTLY derived from fibre geometry. MCP audit: **no canonical constant pins ε_LX / d_lnYreq_dC2 / δA_nLI**; `R_cross_yukawa_t1_t2` provenance self-identifies the external ε_LX as a HELD number, "NOT a framework prediction"; the S97 posit `A_nLI = A_homog + δA` is "pinned, NOT discovered at runtime" (existence, not magnitude). Therefore eps_LX_substrate_motivated = **False** → the external grading lifts the grading to the target, but the value is a fit.

*Constraint-map update* — INFO opens, but does not close, the neutrino generation-grading corridor. What is established: (i) the gap-eq is provably shape-flat (Step 2 reproduces W3-4 to machine ε); (ii) the scale/shape DIVISION OF LABOR is the correct architecture — scale from the gap eq (in-band), shape from an external non-LI leg; (iii) the shape leg's required steepness is fully fixed by two independent substrate quantities (oscillation-anchored required slope MINUS gap-eq solved slope = 0.3037/C_2). What remains uncomputed (the INFO re-route): an INDEPENDENT fibre-connection-geometry derivation of the ε_LX magnitude δA — without it, the steepness reproduction is a back-out, not a prediction. Backward consumers (MR-TEXTURE-ROUTE-B held; full neutrino mass-matrix assembly) inherit: scale leg PASS-eligible (in-band), shape leg INFO-gated on the δA-geometry workshop.

*4-tuple*: (value=`shape_target=2.4882512_recon_Y3Y2=2.48825_rel_err=5.30e-09_gap_flat=1.50000_geps_ratio=1.65883_missing_slope=0.30367_scale[8.6377,10.4878]_in-band=True_eps_LX-substrate-motivated=False`, scheme=FW, convention=RATIO, L_max=10).

*Dual-SHA*: audit_sha256 = `a3e1cf7b31f696467a452ed89b3fb972986236bcab794e2d6a397c1895995652`; content_sha256 = `1902ef882518bb519100e99a04e5ec2d29a6ae4561b227db336a051078861bf6`. Inputs pinned: script SHA `1902ef88…`, canonical_constants.py `9f2fe998…`, s101_d5_md_gapeq.npz `d0267a07…` (both file pins match plan).

*Artifacts*: `computations/session-102/s102_nu_grading_external_epslx.py` / `.npz` / `.png`.

---

### §W4-18. CF-S102-MODELC-PHENO-SCALES (paasch-mass-quantization-analyst)

**Status**: COMPLETED
**Gate ID**: `CF-S102-MODELC-PHENO-SCALES`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (Pati-Salam G422D 0-free-param scales vs experimental bounds)
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: the Model-C 0-free-param ordered solution on the W3-7 solved scales — M_C = 5.08e13 GeV (leptoquark S_1), M_U = 7.68e14 GeV (unification) — survives BOTH the proton-lifetime bound at M_U (Super-K / Hyper-K) AND the leptoquark S_1 flavor bounds at M_C.
**Plan reference**: `sessions/session-plan/session-102-plan-w4.md` §W4-18 (machinery pin, two-condition survival test, proton-lifetime substitution chain with the live-exclusion flag at M_U=7.68e14).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain | Status |
|:--|:--|:--|:--|
| script | `computations/session-102/s102_modelc_pheno_scales.py` | `from canonical_constants import`, `print_verdict_payload` | PRESENT (both patterns) |
| data | `computations/session-102/s102_modelc_pheno_scales.npz` | (non-stub) | PRESENT |
| plot | `computations/session-102/s102_modelc_pheno_scales.png` | (non-stub) | PRESENT |
| verdict_line | `computations/session-102/s102_gate_verdicts.txt` | `^CF-S102-MODELC-PHENO-SCALES:.* audit_sha256=[a-f0-9]{64}` + companion row | PRESENT |
| wp_section | this section | Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit | PRESENT |

Verification by content presence (grep), never line/byte count.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):

1. `search_knowledge("Pati-Salam Model-C unification scale proton lifetime leptoquark M_U M_C")` → returned the plan equations (M_U=7.68e14, alpha_U^-1=39.47) AND **Baptista eq_26**: "in model C … it can provide a solution and **does not mediate proton decay**" (the proton-decay-SAFE PS realization); + Window-17 proton-lifetime falsifier row.
2. `search_knowledge("proton decay lifetime GUT scale Super-K Hyper-K falsifier")` → Window-17 (tau_p ~ M_KK^4/m_p^5 ~10^36 yr at 10^16; Hyper-K ~10^35 reach); prior `s63_proton_decay.py` / DECAY-63 provenance.
3. `get_constant("M_KK")` → 7.4287e16 GeV (canonical; the gravity-route M_KK — NOT the Model-C M_U; gate uses the SOLVED M_U, not M_KK).
4. `trace_entity("proton_decay")` → **T17 Proton Decay Tree-Level Zero** (proven_1844 / proven_1478, atlas-07 permanent): "Exactly zero by PW orthogonality on SU(3). tau_p = 6.26e39 yr." + s63 DECAY-63 (tree-level zero forces geometrically-suppressed higher orders). + Baptista eq_26.
5. `query_entity("theorems","proven_1844")` → confirmed T17 statement and `tau_p = 6.26e39 yr` permanent value.
6. `search_knowledge("leptoquark S_1 flavor bound K-Kbar rare process constraint TeV")` → no closer-than-OOM flavor anchor in-corpus; binding flavor reach treated as the conservative external rare-process scale Lambda_NP ~ 1e5 GeV.

**Not PRE-CLOSED as a gate**, but the decisive physics IS canonical: T17 (tree-level zero, tau_p=6.26e39 yr) + Baptista Model-C (eq_26, does not mediate proton decay). This gate APPLIES those permanent results to the SOLVED M_C/M_U scales against current bounds, and adds the naive-unsuppressed falsifier-rigor companion.

**Verdict**: **PASS** — `value='PASS_modelC_survives_both …'`, scheme=MS, convention=ABSOLUTE, L_max=N/A.
- `audit_sha256 = a66f5321574435915779d9ec0763a7babe91d2ab7ceb92f1dc7892349c26103d` (canonical; supersedes `379971ce…` — corrective re-emit after adding the named `print_verdict_payload` helper; physics + verdict UNCHANGED, Option A retains both lines on disk)
- `content_sha256 = e277dd46b405a8873e2fac036d26cf385b6fe6f6927349ba7144cbce64ad9ce6`

Set-membership PASS: Model-C survives BOTH the proton-lifetime bound at M_U AND the leptoquark S_1 flavor bound at M_C. The 0-free-parameter ordered Model-C corridor of the unification solution space **remains open**.

**Results** (NUMBERS first — substrate-first: D_K SU(3) gauge content → PS multiplet decoupling scales → proton-decay rate + leptoquark amplitude → laboratory bounds):

*Input — S101 W3-7 SOLVED scales (0 free params; npz audit `f2015a0c…`, SHA-pinned `5469bc13…`):*
- M_C = 5.0823e13 GeV (log₁₀ = 13.706; leptoquark S_1 decoupling)
- M_U = 7.6819e14 GeV (log₁₀ = 14.885; sin²=3/8 unification)
- alpha_U^{-1} = 39.471 ⇒ alpha_U = 0.025335

*Condition A — proton lifetime at M_U.* Two numbers, separated cleanly:

| tau_p | value | vs Super-K (2.4e34 yr) | meaning |
|:--|:--|:--|:--|
| **naive / unsuppressed** M_U⁴/(α_U² m_p⁵) | **1.556e31 yr** | ratio 6.48e-4 (**BELOW** → EXCLUDED) | the live falsifier risk that the dimensional estimate flags |
| **framework** (T17 PW zero + Model-C) | **6.26e39 yr** | ratio 2.61e5 (**ABOVE** → SURVIVES) | tree-level amplitude EXACTLY zero; > Hyper-K reach by 6.26e4× |

The naive estimate IS below Super-K (M_U is ~1.3 OOM below the canonical 10^16 GUT scale), so survival is **not automatic** — it rests on a mechanism. That mechanism is **T17 Peter-Weyl orthogonality**: the product of two trivial-rep zero-mode quark/lepton fields lives in the trivial SU(3) rep; its overlap with the leptoquark gauge boson (nontrivial adjoint rep, 15 → 8+3+3̄+1) vanishes EXACTLY ⇒ tree-level leptoquark exchange amplitude = 0. Baptista **eq_26** independently confirms Model-C's diquark-coupling rep content "does not mediate proton decay." The framework lifetime is therefore the T17 permanent value 6.26e39 yr ≫ Super-K. **Condition A: SURVIVES.**

*Condition B — leptoquark S_1 flavor at M_C.* The S_1 is a 4-fermion contact operator, coefficient C_{S1} ~ g²/M_C² (g~1, conservative upper):
- C_{S1} = 3.872e-28 GeV⁻²; current strongest flavor reach Λ_NP ≳ 1e5 GeV ⇒ C_bound ~ 1/Λ² = 1e-10 GeV⁻².
- C_{S1}/C_bound = 3.87e-18 ≪ 1; M_C sits **8.7 OOM above** the flavor reach. The leptoquark is utterly decoupled from current flavor data. **Condition B: SURVIVES.**

*Set membership:* A ∧ B = **True** ⇒ **PASS**.

**Proton-lifetime substitution chain** (the [VERIFY] direction claim, with substituted numbers):
- *Claim:* "the SOLVED M_U=7.68e14 yields tau_p ABOVE Super-K (survives) — direction must be checked, not assumed."
- *Step 1 (defs):* M_U=7.682e14 GeV; alpha_U=1/39.471=0.025335; m_p=0.938272 GeV; tau_p ~ M_U⁴/(α_U² m_p⁵); Super-K = 2.4e34 yr; 1 GeV⁻¹ = ħ/yr = 6.582120e-25/3.155760e7 = 2.0857e-32 yr (canonical `hbar_GeV_s`, `yr_to_s`).
- *Step 2 (subst, no simplify):* tau_p^naive ~ (7.682e14)⁴ / ((0.025335)² · (0.938272)⁵) GeV⁻¹.
- *Step 3 (simplify):* M_U⁴ = 3.482e59 GeV⁴; α_U²·m_p⁵ = 4.668e-4 GeV⁵; tau_p^naive = 7.461e62 GeV⁻¹ = **1.556e31 yr** (cross-check: (M_U/1e16)⁴·1e36 = 3.48e31 yr, OOM-consistent).
- *Step 4 (direction read-off):* 1.556e31 < 2.4e34 ⇒ the **naive (tree-coupled) estimate is EXCLUDED** — this is the genuine falsifier the gate maps. BUT the framework tree-level amplitude is EXACTLY zero (T17), so the physical lifetime is 6.26e39 yr > 2.4e34 ⇒ **the realized direction is SURVIVES.** The naive exclusion is the risk-NOT-realized; the PW-orthogonality mechanism is what saves it.
- *Conclusion:* direction = SURVIVES (framework), with the naive number documenting WHY survival is mechanism-dependent, not automatic.

**Cross-checks (CC):**
- *CC1 — input SHA pins MATCH.* canonical_constants.py = `9f2fe998…`; s101 npz = `5469bc13…` (both asserted in-script; exact plan pins).
- *CC2 — SOLVED scales reproduce plan 3-sig-fig text.* M_C/5.08e13−1 < 1%, M_U/7.68e14−1 < 1%, |α_U^{-1}−39.47| < 0.01 (all asserted).
- *CC3 — naive estimate OOM-consistent two ways.* explicit M_U⁴/(α_U²m_p⁵) = 1.56e31 yr vs Window-17 (M_U/1e16)⁴·1e36 = 3.48e31 yr (same decade band).
- *CC4 — framework tau_p is the T17 permanent value*, not a re-derivation (atlas-07 / proven_1844; tree-level zero by PW orthogonality, independently corroborated by Baptista eq_26).
- *CC5 — unit conversion from canonical only* (hbar_GeV_s, yr_to_s); no hardcoded conversion constant.

**Dual-SHA**: `audit_sha256_short=379971cef72d125b content_sha256_short=01d675063c7dacd8` (companion row present in verdict file). audit_sha256 over ordered pin-map [content_sha256 | canonical SHA | pinmap JSON | s101 npz SHA]; content_sha256 over the producing script.

**Substrate framing**: PARTICLE-class. Model-C (Pati-Salam G422D) is a representation-theoretic organization of the D_K SU(3) gauge content: M_C is where the leptoquark S_1 PS multiplet decouples, M_U the sin²=3/8 unification boundary — both SOLVED 0-free-param from the M_Z couplings (S101 W3-7). The phenomenology test runs substrate → laboratory: D_K gauge content → PS multiplet decoupling scales → proton-decay rate (6-fermion via M_U gauge bosons; PW-orthogonality-zero at tree level) + leptoquark amplitude (4-fermion S_1 exchange at M_C) → laboratory IN-container bounds (Super-K / rare-flavor). The substrate PREDICTS the scales; experiment CAN exclude them — and here both survive because the same SU(3) Peter-Weyl orthogonality that organizes the spectrum also protects the proton.

**dual_prior update**: PASS → 0.9 mass to **Track A** (Model-C survives both bounds; the 0-free-param solution is experimentally viable). Track B (≥1 scale excluded — the live M_U-low proton-decay risk) is the risk-NOT-realized: the naive M_U⁴ exclusion is genuine but defused by the PW-orthogonality tree-level zero.

**Artifacts**: `computations/session-102/s102_modelc_pheno_scales.py` / `.npz` / `.png`.

---

### §W4-19. CF-S102-M0-TRANSFER-CONVENTION (paasch-mass-quantization-analyst)

**Status**: COMPLETED
**Gate ID**: `CF-S102-M0-TRANSFER-CONVENTION`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (substrate-canonical M₀-screening transfer level)
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: one of the two M₀-screening transfer conventions is substrate-canonical and DERIVABLE — boundary-RG (−0.461%) vs m_H-first-power (−11/670 = −1.642%) — collapsing the W4-5 CONVENTION-SENSITIVE spread (1.181% > 1.0%) to ≤ 1.0%, with the band-shrink direction (sign = PASS) preserved.
**Plan reference**: `sessions/session-plan/session-102-plan-w4.md` §W4-19 (machinery pin CLASS=FULL, 1.0% spread threshold, band-shrink-direction substitution chain + BCS-chain-position derivation).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- Script: `computations/session-102/s102_m0_transfer_convention.py` — present; contains `from canonical_constants import` (Section 1) and `print_verdict_payload` (Section 7). Both input-SHA pins matched at runtime (canonical `9f2fe998…`, s101 npz `46ff62ed…`).
- Data: `computations/session-102/s102_m0_transfer_convention.npz` — present (all residuals, spread, sign flags, derivation flags, 7 CCs, dual-SHA).
- Plot: `computations/session-102/s102_m0_transfer_convention.png` — present (2 panels: residual-by-convention; ambiguity-collapse vs tolerance).
- Verdict line: `computations/session-102/s102_gate_verdicts.txt` — `CF-S102-M0-TRANSFER-CONVENTION: PASS …` with `audit_sha256=cef309d6…321be504` (64-hex), dual-SHA companion row, [SIGN] 3-tuple row, + 2 chain-position/fb_backward extra rows. Emitted via the race-safe `emit_verdict` MCP tool (5 rows).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("M_0 screening transfer convention BCS Higgs residual")` → S101-M0-BCS-SCREENING (INFO; both conventions shrink, `delta_solve=0.2672`, `convention_sensitive=True`); the two conventions documented in plan-w4 equations. **NOT pre-closed** — this gate DERIVES the convention; S101 left it CONVENTION-SENSITIVE.
- `search_knowledge("Volovik partition effacement Gamma_eff boundary RG screening")` → `Gamma_eff=0.99970` screens the VACUUM partition (boundary quantity); the SAME `Gamma_eff` binds `w0_FW=-0.918` (Volovik vacuum partition, S58). This is the substrate witness for the boundary-level selection.
- `get_constant("Gamma_effacement")` → 0.9997 (S37/S58); `get_constant("m_H_FW_KK_threshold")` → 131.8 (S100a); `get_constant("m_H_obs")` → 125.1 (PDG 2024).
- `trace_entity("THRESHOLD-62 BCS gap to mass")` → no direct trace; `trace_entity("effacement screening boundary condensate first-power")` → no trace (confirms the chain-position question is NOT pre-derived in the index — this gate's substantive output is novel).
- Verified import names against `canonical_constants.py` (lines 542, 674-675, 2237, 2257): `Gamma_effacement`, `m_H_FW_KK_threshold`, `m_H_FW_tree`, `m_H_obs`, `w0_FW` all present.

**Verdict**: **PASS** — `(value=DERIVED=boundary-RG; spread_unsel=1.1806% > 1.0% (W4-5); spread_under_derived=0.0000% ≤ 1.0%; band-shrink_sign=PASS(both_conv); derived_residual=−0.4612%; Gamma_eff=0.9997(boundary vacuum partition); all_cc=True, scheme=SA, convention=MIXED→boundary-RG, L_max=N/A)`. [SIGN] 3-tuple: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID`. Dual-SHA: `audit_sha256=cef309d62959cd54f6b9391135918e9d9fff4246080f6b6ac119d490321be504`, `content_sha256=da706e9dbd8356c89799ca3334b1a730c76a66df182e96c7e4068c6467b7c411`.

**Results** (NUMBERS first, gate second, interpretation third):

*NUMBERS.* From canonical constants and the S101 W4 BCS-screening npz (forward dependency `s101_w4_m0_bcs_screening`, audit `1a1eff66…`):

| quantity | value | source |
|:---|:---|:---|
| `r_KK` unscreened KK residual | **+5.3557%** (= 67/1251 exact) | `m_H_FW_KK_threshold/m_H_obs − 1` = 131.8/125.1 − 1 |
| `r_tree` unscreened tree residual | +7.1143% (= 89/1251 exact) | `m_H_FW_tree/m_H_obs − 1` = 134/125.1 − 1 |
| `r_scr` PRIM (m_H first-power) | **−1.6418%** (= **−11/670** exact) | npz `r_KK_scr` |
| `r_scr` RG (boundary-RG) [**DERIVED**] | **−0.4612%** | npz `r_KK_scr_RG` |
| PRIM−RG spread (W4-5 ambiguity) | **1.1806%** (> 1.0% tol) | `|r_scr_PRIM − r_scr_RG|` = npz `conv_sens_dev` |
| spread under DERIVED convention | **0.0000%** (≤ 1.0% tol) | one transfer level selected ⇒ spread collapses |
| `Gamma_eff` | 0.9997 | shares with `w0_FW = −0.918` (Volovik vacuum partition) |

*Reading reconciliation (load-bearing).* The plan's substitution chain labels `−11/670` and `−0.461%` as "screening corrections δ"; the npz stores them as **screened residuals** `r_scr`. The gate's two substantive outputs are **reading-invariant**: (i) the convention spread `|r_PRIM − r_RG| = |δ_PRIM − δ_RG| = 1.1806%` (the −r_KK term cancels in the difference; verified A=B=deltas=1.1806%, CC5); (ii) the band-shrink SIGN (both screened residuals have smaller magnitude than the unscreened +5.356%; equivalently both additive deltas, −6.998% PRIM / −5.817% RG, are negative — opposite to r_KK > 0). The interpretive split between the readings does not move either verdict.

*Band-shrink substitution chain (with substituted numbers; [SIGN] direction claim).*
- Step 1 (defs): r_KK = +5.3557% > 0; r_scr_PRIM = −1.6418%; r_scr_RG = −0.4612%.
- Step 2 (band-shrink direction, no simplification): `|r_scr| < |r_KK|` iff screening moves the residual toward zero, i.e. δ opposite-sign to r_KK and |δ| < 2|r_KK|.
- Step 3 (both conventions): δ_PRIM = −6.9975% < 0 (opposite r_KK), |δ_PRIM| = 6.9975% < 2·5.3557% = 10.711% ⇒ |r_scr,PRIM| = 1.6418% < 5.3557% **[SHRINKS]**. δ_RG = −5.8169% < 0, |δ_RG| = 5.8169% < 10.711% ⇒ |r_scr,RG| = 0.4612% < 5.3557% **[SHRINKS]**.
- Step 4 (canonical form / the ambiguity): spread = |−1.6418 − (−0.4612)|% = 1.1806% > 1.0% ⇒ CONVENTION-SENSITIVE (the W4-5 result, reproduced exactly).
- Step 5 (direction read-off): both conventions shrink the band ⇒ **SIGN = PASS** (forced, convention-independent). MAGNITUDE = PASS iff the derivation collapses the spread ≤ 1.0%.

*Substrate-first convention DERIVATION (the gate's substantive output; per `.claude/rules/substrate-first-canonical-sourcing.md` — derived from substrate structure, NOT imported from an external paper).* The question is WHERE in the BCS gap-to-mass chain `gap Δ → condensate BOUNDARY (RG running) → physical m_H pole` the Volovik effacement enters. The substrate fact (S37/S58, MCP-confirmed): `Gamma_eff = 0.99970` is the impedance-transmission coefficient at the acoustic-white-hole fold acting on the **VACUUM PARTITION** — a condensate-**boundary** quantity, NOT the physical Higgs pole mass. Structural witness: the **same** `Gamma_eff` binds `w0_FW = −0.918` (the late-time equation-of-state from the Volovik vacuum partition), and `w0_FW` is a boundary EoS quantity, not a pole mass. Therefore the screening enters at the **condensate boundary (RG running of the gap)** ⇒ the substrate-canonical transfer level is **boundary-RG (−0.461%)**. The m_H-level first-power convention (−11/670) would require Γ_eff to act on the physical pole mass, which it does not. With boundary-RG selected, the residual is pinned to a single transfer level (−0.4612%) and the spread under the derived convention is 0.0% ≤ 1.0%.

*Cross-checks (all PASS).* CC1 r_KK reproduced from canonical = npz (Δ < 1e−12); CC2 r_tree = npz; CC3 PRIM is exact −11/670 (Δ < 1e−15); CC4 spread = npz `conv_sens_dev` (Δ < 1e−12); CC5 spread reading-invariant (A=B=deltas); CC6 unselected spread 1.1806% > 1.0% tol (confirms the W4-5 ambiguity exists); CC7 derived-convention spread 0.0% ≤ 1.0% (collapse confirmed). `all_cross_checks = True`.

*CLASS / machinery.* CLASS=**FULL** — the BCS gap-to-mass arithmetic is the FULL physical S62 gap-equation lineage (THRESHOLD-62), not a SCHEMATIC helper; no `_spectral_action_regulators.py`-class module consumed. `regulator_pin=N/A` (companion row): the observable is a BCS gap-to-mass ratio, not a Seeley-DeWitt `a_n` residue, so the `a_n^{regulator}` tagging discipline does not apply. scheme=SA, convention=MIXED (the gate DERIVES → boundary-RG), L_max=N/A (no Peter-Weyl truncation). GPU path numpy.linalg (CPU; deterministic scalar arithmetic, OMP capped at 8 threads), publication_precision=4.

*Interpretation / solution-space.* The W4-5 CONVENTION-SENSITIVE ambiguity is **resolved**: the m_H residual is pinned to a single transfer level (boundary-RG, −0.461%) for downstream consumption. The dual-prior re-allocates to **Track A** (convention derived, spread collapsed) per the gate's discriminator (PASS → 0.9 Track A). Backward consumer `S102-MH-ROUTE-SELECTION` (item 20): the screening level is now pinned to boundary-RG(−0.461%), feeding the m_H route residuals (fb_backward extra row in the verdict file). The band-shrink direction did NOT invert (the FAIL branch — a deeper BCS-machinery surprise — did not fire). Substrate direction: D_K |S|² transverse fiber mode → BCS gap-to-mass chain → Volovik effacement screening at the **boundary** → screened m_H residual.

---

### §W4-20. S102-MH-ROUTE-SELECTION (phonon-first-cosmologist)

**Status**: COMPLETED
**Gate ID**: `S102-MH-ROUTE-SELECTION`
**Trigger**: `[CHAIN]` ([SIGN]-chained — 3-tuple emitted per spawn directive)
**Classification**: **PARTICLE** (no-PDG-appeal a_4-moment m_H route selection; cross-wave output contract)
**Agent**: `phonon-first-cosmologist` (cross-checked by `connes-ncg-theorist` — independent a_4 |S|² spectral-action evaluation, see Cross-check below)
**Hypothesis**: the a_4-moment KK-threshold convergence structure of the |S|² mode FORCES a unique intra-KK route — KK-L5 (127.5) vs KK-threshold (131.8) — via a no-PDG-appeal saturation criterion; if no route is forced, the verdict is FAIL-ACCOMMODATION. The verdict KEYS the Wave-5 item-23 BF-spine 3-state.
**Plan reference**: `sessions/session-plan/session-102-plan-w4.md` §W4-20 + §"Wave 4 → Wave 5 Decision Point" (regulator_pin=a_4^{ζ}, saturation-diagnostic substitution chain, back-solve guard, 3-state map).

**Verdict**: **PASS** — composite (sign=PASS / magnitude=PASS / regime=VALID). The no-PDG-appeal a_4-moment KK-threshold **saturation diagnostic FORCES a unique route: Route B (KK-threshold DIRECT) = 131.8 GeV** (`m_H_FW_KK_threshold`). m_H is a substrate-DERIVED prediction, NOT an accommodation surface. Wave-5 item-23 takes 3-state **(b)** (FORCED + band-MISS — see Results). `audit_sha256=75ed7ffb1515715c62f2259cd4c99b8314118826af4a272f95efaccf71a47595`, `content_sha256=ba0c93a6a8c1defe3a8084878857408f3e92ef8e077615af633eeff75eb7da2e`.

**Substrate framing** (direction of explanation): D_K a_4 fourth spectral moment → |S|²-mode KK-threshold correction series S_L → convergence/saturation diagnostic → forced m_H route. The Higgs IS the transverse oscillation of the fiber embedding (the |S|² mode); its mass is the a_4-moment (Yang-Mills + Higgs-quartic, Φ(a_4)=Σ_3 load-bearing) KK-threshold lift of the tree-level λ_h. The two intra-family routes are two READINGS of the SAME a_4 KK-threshold series — the DIRECT converged moment vs the Aitken-Gaussian acceleration of the truncated L=4,5,6 window — and which is canonical is a purely SPECTRAL convergence question answered WITHOUT any appeal to the measured Higgs mass.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`; query-first discipline):
- `search_knowledge("m_H Higgs mass KK threshold route selection a_4 moment")` → returned `a_4^{ζ}=1350.7216` (S75), `m_H_FW_KK_threshold=131.8` (S100a, Route B), `HIGGS-ZETA-67` (m_H^ζ=138.5 INFO, zeta-EXCLUDED), theorem A10 (Filter-Independence of tree-level m_H). NOT a closed/PRE-CLOSED gate — this is a NEW selection adjudication.
- `search_knowledge("KK-L5 Aitken extrapolation 127.5 Higgs threshold correction")` → returned the S66 S-series (`S_3=0.50347910, S_4=1.14290915`), constraint-mega-matrix `m_H=127.5–131.8 GeV (Aitken-Gaussian)`, and (decisive) the S73b cross-data-point `m_H_finf=133.4` (Aitken L=3..7) vs `m_H_L3=131.8` (direct).
- `get_constant("a_4_FW_zeta")` → `1350.7216` (S75; `s75_f_conv_spectral_output.txt` L26). `get_constant("a_2_FW_zeta")` → `2776.165389`. `get_constant("m_H_FW_KK_threshold")` → `131.8` (S100a, gate `S100a-M0-MH-INHERITANCE`). `get_constant("m_H_obs")` → `125.1` (PDG; loaded ONLY for final reporting).
- `search_knowledge("Friedrich-Bar saturation Casimir bottom-K |S|^2 mode KK tower convergence L_max")` → **PROVEN**: Friedrich-Bär saturation theorem (S87 W11-2/W11-3, S89 W3-1, S90 W2) analytically certifies bottom-K D_K(τ_fold) cardinality INVARIANCE for ALL L_max ≥ 10. This is the load-bearing structural input for the saturation criterion.
- `trace_entity("m_H route selection Aitken saturation")` → no prior trace (NEW adjudication, no pre-existing verdict). `search_knowledge("mu_BC 188.19 ACCOMMODATION ...")` → confirmed `mu_BC=188.19` is the ACCOMMODATION surface (bi-criterion fit, FLAGGED), correctly excluded from the route set.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — verified on disk by content):
- Script `computations/session-102/s102_mh_route_selection.py` — present; contains `from canonical_constants import` and `print_verdict_payload`.
- Data `computations/session-102/s102_mh_route_selection.npz` — present (10,657 B; series + saturation diagnostic + 3-tuple + band-membership).
- Plot `computations/session-102/s102_mh_route_selection.png` — present (91,538 B; left: S_L full vs physical-saturated series; right: Δ_L increments + Aitken-overshoot-vs-floor bars).
- Verdict line in `computations/session-102/s102_gate_verdicts.txt` — `S102-MH-ROUTE-SELECTION: PASS -- value='FORCED=Route B (KK-threshold DIRECT)=131.8...' ... audit_sha256=75ed7ffb...` (64-hex), with dual-SHA companion row, schema-v2 3-tuple row, and `# regulator_pin=a_4^{ζ}` companion comment row (emitted via `mcp__knowledge__emit_verdict`; 6 rows).
- This WP section — Status COMPLETED, Verdict (PASS), Output Artifacts, MCP Pre-Compute Audit all present.

**Results**:

*NUMBERS (substrate-first re-derivation; m_H_obs ABSENT from the selection path):*

The KK-threshold series S_L (Formula C: `dC(p,q) = T(p,q)/(8π²)·ln(Λ²/ω_min²)·exp(−ω_min²/Λ²)`, Λ=2.048293 M_KK fixed cutoff) was RE-DERIVED substrate-first from the SU(3) Peter-Weyl rep theory (closed-form `T(p,q)`, `C_2(p,q)`) + the D_K bottom eigenvalues `ω_min(p,q)` from the L12 master spectrum cache `s84_spectrum_cache_L12_tau019.npz` (τ_fold=0.19) — NOT extracted from the S66 archive `.txt` literal. The archive value is a cross-check ONLY:

| L | S_L (full, fixed-cutoff) | Δ_L (phys) | r_L (phys) | S_L (physical, ω_min<Λ) |
|---|---|---|---|---|
| 3 | +0.503479 | +0.354878 | +2.7429 | +0.503479 |
| 4 | +1.142910 | +0.639430 | +1.8018 | +1.142910 |
| 5 | +1.920172 | +0.777262 | +1.2156 | +1.920172 |
| 6 | +2.352670 | +0.434979 | +0.5596 | **+2.355151** (SATURATED) |
| 7 | +1.637180 (−0.715490 artifact) | +0.000000 | 0 | +2.355151 |
| 8–12 | diverges to −43.6 (fixed-Λ artifact) | +0.000000 | — | +2.355151 (FLAT) |

- **S66 cross-check** (re-derived vs archive): max relative difference = **9.81e-7** (cache vs archive eigenvalue precision floor) — substrate-first match confirmed, value re-derived NOT extracted.
- **S_direct_saturated = 2.355151** (the physical KK-threshold sum over ALL sectors with ω_min < Λ; this is the DIRECT a_4-moment converged value, Route B).
- **L_saturation = 6 < canonical L_max = 10**: the first cutoff-crossing (ω_min > Λ, e.g. sector (0,6) ω_min=2.0526) occurs at L=6; the physical tail is **identically zero for ALL L ≥ 7** (`phys_tail = 0.00e+00`).
- **S_aitken (L=4,5,6 Aitken-Gaussian Δ²) = 2.895230** (Route A edge).
- **Friedrich-Bär saturation floor** Δ_phys(L=6) = **0.434979**.
- **Aitken overshoot** |S_aitken − S_direct| = **0.540079** = **1.2416 × the saturation floor** → the overshoot EXCEEDS a full physical increment.

*SUBSTITUTION CHAIN (the no-PDG-appeal selection criterion; [SIGN]/[CHAIN] mandatory):*

Claim: "A UNIQUE m_H route is selectable from the a_4-moment KK-threshold convergence structure WITHOUT appeal to which route lands nearest PDG — the selection criterion is an analytic property of the KK-series, not a proximity-to-data argument."

- **Step 1 (definitions):** Route A = Aitken-Gaussian Δ² of L=4,5,6 (S_4=1.14290915 re-derived; edge → 127.5). Route B = the directly-converged a_4-moment correction (`m_H_FW_KK_threshold`=131.8; a_4^{ζ}=1350.7216 fixes the moment). EXCLUDED: m_H^ζ=138.5 (zeta-regulated, not physical). ACCOMMODATION surface: mu_BC → 188.19 (flagged). m_H_obs=125.1 — loaded ONLY for Step-4-external reporting (back-solve guard).
- **Step 2 (criterion, no PDG):** C(route) = "is this route the substrate-FORCED convergent limit?" Route B = the DIRECT moment (NO extrapolation). Route A presupposes the bare series has NOT converged at L=6 and accelerates it. The criterion asks: does the a_4 KK-threshold series CONVERGE by the canonical L_max (⇒ Route B canonical, Aitken superfluous) or REQUIRE acceleration (⇒ Route A canonical)?
- **Step 3 (analytic convergence test):** the a_4-moment KK-threshold correction is governed by the Casimir-bounded KK-tower sum; its convergence is set by the Friedrich-Bär saturation of the new-sector eigenvalue floor. The bottom-K |S|²-mode contribution is **L_max-SATURATED at L=6** — every sector with ω_min < Λ is summed by L=6; new sectors (L≥7) have ω_min > Λ (Casimir-driven floor rise) and contribute ZERO physical content. Substitution: `S_phys(L) = S_phys(6) = 2.355151` for ALL L ≥ 6; `d S_phys/dL = 0` for L > 6.
- **Step 4 (direction read-off, no PDG):** the series is saturated (`L_saturation=6 ≤ L_max=10`) ⇒ the DIRECT moment IS the converged limit, AND Aitken acceleration of an already-saturated series overshoots (the L=4,5,6 window sits in the transitional regime r=1.80→1.22→0.56, NOT the geometric-constant regime Aitken assumes, so Aitken extrapolates PAST the saturated value: overshoot 0.5401 = 1.2416× floor 0.4350 > 1). Direction: `series_saturated=True ∧ aitken_spurious=True ⇒ Route B (DIRECT, 131.8) FORCED`. The selection is forced by the SPECTRAL convergence behaviour, NOT by `|m_H^route − 125.1|`.
- **Conclusion:** the no-PDG-appeal criterion is the a_4-moment KK-series convergence/saturation diagnostic; it FORCES a unique route (Route B). PASS.

*BACK-SOLVE GUARD:* the script asserts (and the run confirms) that `m_H_obs` (125.1) is ABSENT from the selection-criterion input set — selection inputs are `{a_4_FW_zeta, a_2_FW_zeta, Lambda_fixed, L_max, cache}` only. `m_H_obs` is loaded for the FIRST and ONLY time in the final reporting block. Guard PASS.

*3-TUPLE ([SIGN]-chained):* `sign_verdict=PASS` (computed direction — saturation forces Route B — matches the Step-4 pre-registered FORCED-Route-B direction). `magnitude_verdict=PASS` (the discriminator margin is CLEAN: overshoot_ratio=1.2416 ≥ 1.10, routes well-separated, not borderline). `regime_verdict=VALID` (the saturation is EXACT — physical tail identically zero for all L > 6; no regime breakdown). Composite collapse (gate-verdicts.md schema-v2): sign=PASS ∧ magnitude=PASS ∧ regime=VALID ⇒ **PASS**.

*4-TUPLE:* (value=`FORCED=Route B (KK-threshold DIRECT)=131.8 via a4-KK-saturation, L_sat=6<L_max=10, overshoot_ratio=1.2416, S_direct=2.3552, S_aitken=2.8952, band=MISS, wave5_state=b`, scheme=FW, convention=ABSOLUTE, L_max=10). Regulator pin: a_4^{ζ} (a_4_FW_zeta=1350.7216, S75) per `.claude/rules/regulator-pin-discipline.md`; companion comment row emitted.

*BAND-MEMBERSHIP (reporting ONLY — Wave-5 3-state input; m_H_obs loaded here for the first time):* forced m_H = 131.8 vs PDG band 125.25 ± 0.17 → deviation +6.55 GeV (+38.5σ), rel +5.36% vs PDG central 125.1 (= 67/1251 exact per the `m_H_FW_KK_threshold` provenance). **band-HIT = False** (131.8 lies far outside the tight PDG ±0.17 band — as expected for a ±2–5% framework prediction from zero geometric free parameters). NOTE: BOTH routes (127.5 and 131.8) miss the tight PDG band; the band-MISS is reported for the BF spine and does NOT enter the route selection.

*WAVE-5 ITEM-23 3-STATE (cross-wave output contract; FIXED before item 23 runs, anti-post-hoc):* composite=PASS ∧ band-MISS ⇒ **3-state (b): FORCED + band-MISS → SCHEME-FLOATING → STRAINED-PINNED; m_H contributes anecdotal → BF floor ~2.** (Per the plan §"Wave 4 → Wave 5 Decision Point" map: PASS+band-HIT→(a) ceiling 31.62; PASS+band-MISS→(b) floor ~2; FAIL-ACCOMMODATION→(c) m_H exits incumbent set; INFO→default b_mH≤1.5 unchanged.) This verdict KEYS the BF spine: m_H REMAINS in the incumbent set (it is a substrate-derived prediction, NOT removed) but contributes the anecdotal/STRAINED weight, not the full b_mH=1.5.

*CROSS-CHECK (connes-ncg-theorist, independent a_4 |S|²-mode spectral-action evaluation — structural concordance):* the a_4^{ζ}=1350.7216 / a_2^{ζ}=2776.165389 moment ratio (`a_4/a_2 = 0.486549`) is the spectral-action input to the CCM tree-level λ_h (theorem A10: λ_h = (4/3)g_3²(M_KK)·(a_4/a_2), cutoff-shape-INDEPENDENT); the L=0 CCM λ_CCM=0.14699 reproduces from `g_3(M_KK)=0.516060` to 6 sig figs (cross-checked in the derivation log). The Friedrich-Bär saturation theorem (PROVEN S87/S89/S90, queried above) is the independent NCG-axiomatic certification that the bottom-K |S|²-mode contribution is L_max-invariant for L_max≥10 — i.e., the saturation that FORCES Route B is the same structural property the spectral-action side already proved. The two axes (phonon-first KK-series convergence + connes-ncg spectral-action saturation) concur that the DIRECT moment is the converged limit.

*SOLUTION-SPACE INTERPRETATION:* this gate CLOSES the m_H-route-selection corridor. The forced route is Route B (131.8), substrate-derived via a no-PDG criterion. The corridor where m_H is a best-fit ACCOMMODATION (selected by proximity to PDG) is EXCLUDED — the convergence diagnostic discriminates the two routes WITHOUT data. The band-MISS routes the BF-spine consequence to floor ~2 (item 23), but m_H remains a genuine prediction. The no-PDG-appeal discipline here is the methodological template for the Wave-5 n_s FUNCTIONAL-COMMIT gate (item 26).

---

## Wave 4 Synthesis (team-lead)

**Dispatch record**: 6/6 gates dispatched and landed (one full-batch loss to a transient server-side API rate limit before any work product; clean re-dispatch — no partial artifacts, no verdict re-fires). All six verdict lines + dual-SHA companions verified on disk in `computations/session-102/s102_gate_verdicts.txt`; all six WP sections carry Status COMPLETED + Verdict + Output Artifacts + MCP Pre-Compute Audit (content-presence verification, never line counts). Two gates carry honest Option-A supersession chains (W4-16 `0eca27b9…` supersedes `1bc8e08e…`, unused-import cleanup; W4-18 `a66f5321…` supersedes `379971ce…`, named-helper addition — physics unchanged in both, full-64-hex supersedes tags present).

**Wave verdict ledger**:

| Gate | Verdict | 3-tuple (sign/mag/regime) | Outcome (one line) |
|:-----|:--------|:--------------------------|:-------------------|
| W4-15 `CF-S102-QUARK-PERGEN-KERNEL` | **FAIL** | FAIL/FAIL/VALID | Crossing NOT forced — W2-4 uniform-κ impossibility EXTENDS to the substrate-derived per-gen dressed-block kernel (slope asymmetry same-signed at all 3 generations; gen-3 dressing 2 OOM short); corridor closes. Structural PASS sub-result: triality CKM texture (gen3↔gen2, gen3↔gen1 exactly forbidden; Cabibbo-dominance forced). |
| W4-16 `CF-S102-KAPPA-NU-FIRSTPRINCIPLES` | **INFO** (Track B) | PASS/FAIL/VALID | s_ν SIGN substrate-FORCED (+, widening; Y-ratio-free chain); MAGNITUDE +0.5469 exposed as S99 back-solve coincidence — independent B-branch gradient gives ≈+0.0877; candidate-(c) re-pinned at the derived magnitude. Plan-frozen composite-precedence disclosed. |
| W4-17 `CF-S102-NU-GRADING-EXTERNAL-EPSLX` | **INFO** | PASS/—/VALID | Division-of-labor architecture CONFIRMED (gap-eq provably shape-flat, reproduces W3-4 +39.7% to machine ε; external grading reconstructs Y₃/Y₂ = 2.4882512 at 5.3e-09; scale leg in-band) — but ε_LX magnitude is the residual back-out, NOT substrate-motivated (no canonical pins it; S97 HELD number). |
| W4-18 `CF-S102-MODELC-PHENO-SCALES` | **PASS** | —/—/— (set-membership) | Model-C survives BOTH bounds: naive τ_p at solved M_U=7.68e14 is genuinely EXCLUDED (1.56e31 yr < Super-K), but the T17 Peter-Weyl tree-level zero (permanent) gives τ_p = 6.26e39 yr (2.6e5 × Super-K); leptoquark S₁ 8.7 OOM above flavor reach. 0-free-param corridor stays open. |
| W4-19 `CF-S102-M0-TRANSFER-CONVENTION` | **PASS** | PASS/PASS/VALID | W4-5 CONVENTION-SENSITIVE ambiguity RESOLVED substrate-first: Γ_eff = 0.99970 is a condensate-BOUNDARY quantity (same Γ_eff binds w0_FW = −0.918, a boundary EoS) ⇒ boundary-RG is the canonical transfer level; spread 1.1806% → 0.0000% under the derived convention; residual pinned −0.4612%. |
| W4-20 `S102-MH-ROUTE-SELECTION` | **PASS** | PASS/PASS/VALID | Route B (KK-threshold DIRECT, 131.8 GeV) FORCED by the a₄-moment KK saturation diagnostic — physical series saturates at L=6 < L_max=10 (Friedrich-Bär floor rise), tail identically zero; Aitken acceleration of the saturated series overshoots by 1.2416× a full physical increment ⇒ spurious. m_H is a substrate-DERIVED prediction, not an accommodation; back-solve guard CLEAN (m_H_obs absent from selection inputs). |

**Cross-wave output contract (the wave's sole intra-session export — MANDATORY record per plan §"Wave 4 → Wave 5 Decision Point")**: W4-20 composite = PASS ∧ band-MISS (131.8 vs PDG 125.25 ± 0.17, +38.5σ; both routes miss the tight band) ⇒ **Wave-5 item-23 takes 3-state (b): FORCED + band-MISS → SCHEME-FLOATING → STRAINED-PINNED — m_H REMAINS in the incumbent BF set at anecdotal weight, BF floor ~2**. The forward-pinned input `computations/session-102/s102_mh_route_selection.npz` is on disk; the 3-state map was FIXED at plan-freeze (anti-post-hoc). The W5-3 dispatch consumes this verdict.

**Substrate-first synthesis (what the wave established)**: the fermion-mass live edge moved on all six fronts without a single accommodation. The same SU(3) representation theory acts as both engine and wall: Peter-Weyl orthogonality protects the proton (W4-18) and forces the Cabibbo-dominant CKM texture (W4-15 sub-result), while the C₂-monotone greybody structure WALLS OFF the quark crossing (W4-15 FAIL) — the substrate's per-generation slope content is structurally same-signed. The neutrino sector splits cleanly into substrate-FORCED shape species (widening sign, W4-16) + architecture (division of labor, W4-17) versus HELD magnitudes (s_ν = +0.5469 and ε_LX both exposed as fits). The Higgs chain is now convention-unambiguous end-to-end: boundary-RG screening (W4-19) → a₄-saturation-forced Route B at 131.8 GeV (W4-20), with the honest +38.5σ band-MISS routed to the BF spine at anecdotal weight rather than hidden. Explanation direction preserved throughout: D_K eigenvalues → spectral moments (a₄ KK series, B-branch gradients, dressed-block ratios) → emergent particle physics → laboratory bounds.

**Fired pre-declared routings (open-question / workshop-class seeds — NOT plan CFs)**: two gate-rubric routings fired: (i) W4-15 FAIL → **κ_g-derivation** (a sign-changing per-generation kernel requires a substrate ingredient NOT in the dressed-block greybody set; route-(b) exhaustion proved no existing substrate quantity is non-monotone across generations); (ii) W4-17 INFO → **fibre-connection-geometry derivation of the δA (ε_LX) magnitude** (the required steepness 0.3037/C₂ is fully fixed; what is missing is an independent geometric derivation). Both fail the 4-field compute-CF test on the What/Inputs fields (the missing ingredient is not yet identified — no machinery pin is possible), so neither is queued as a plan CF; both are visible to `/rclab-investigate` (Q1/Q2/Q3 discriminator applies) and to the S103 plan-time register maintenance (atlas-08 / EVOI) via this synthesis.

**Effected In-Session (NON-MATH — completed by the team-lead orchestrator before STOP)**:

- [x] W4-19 canonical-constants promotion adjudication — considered and DECLINED with reason: the plan block pre-registers no promotion step; the derived convention (boundary-RG) + residual (−0.00461153 full-float in npz `r_scr_RG`/`derived_residual`) are dual-SHA-pinned in the verdict file, npz, and WP; the m_H prediction itself (131.8) is already canonical (`m_H_FW_KK_threshold`); the sole intra-session consumer (W4-20) already consumed via the fb_backward verdict row. No import-target need exists — promotion would be unconsumed machinery. — `computations/session-102/s102_m0_transfer_convention.npz` — audit `cef309d62959cd54`
- [x] Session housekeeping ledger created with the §VII.BS index-table-row §A entry (W1-1-surfaced, fixed during this dispatch) — `sessions/session-102/session-102-housekeeping.md` — §A.A1
- [x] Wave-4 synthesis + constraint-map + files tables written (this section) — `sessions/session-102/session-102-w4-workingpaper.md` — team-lead designated writer

Self-audit: `grep -c '^- \[ \]'` on this sub-section = 0 (no unchecked items).

## Carry-Forward Computations

At wave-synthesis the team-lead correctly judged the two fired rubric routings (κ_g-derivation, δA fibre-geometry derivation) FAIL the 4-field compute-CF test on What/Inputs (the missing substrate ingredient is not yet identified, so no machinery pin is possible) and routed them to `/rclab-investigate` for the Q1/Q2/Q3 discriminator rather than padding this block (`feedback_fix-in-session-never-defer.md`). The S102 `/rclab-investigate` consolidation (2026-06-10) ran the discriminator and lifts the two items below, which are absent from both this block (previously "(none)") and the S102 housekeeping ledger. The κ_g-derivation is NOT lifted as a standalone CF: it folds into the Slot-1 review S-3 (`session-102-workshop-schedule.md`, quark-crossing WALL-vs-GAP classification) and becomes a pre-registerable gate `CF-S103-QUARK-KAPPA-G-<handle>` only if S-3 classifies the corridor as a GAP with a named not-yet-tested substrate ingredient (otherwise it lands as a §VII registry-candidate WALL theorem — also out of S-3).

### CF-W4-1 — δA fibre-connection-geometry derivation of the ε_LX neutrino-grading magnitude [Q-other / Q1b solo-compute]

> **Routing note**: Q-other (single derivation with a pre-registerable gate, no adversarial DISAGREEMENT — a neutrino specialist and an NCG geometer would AGREE on the architecture and on what is missing). Surfaced for the first time by the S102 `/rclab-investigate` W4 seed (`workshops/_seed-w4.md`); NOT a workshop and NOT previously catalogued. The W4-17 INFO confirmed the scale-from-gap-eq / shape-from-external-grading division of labor (gap-eq provably shape-flat, reproduces W3-4 +39.7% to machine ε; external grading reconstructs Y₃/Y₂ = 2.4882512 at rel 5.3e-09; scale leg in-band [8.6377, 10.4878]), but ε_LX is the residual back-out — HELD, not substrate-motivated (MCP audit: no canonical pins ε_LX/δA; S97 self-identifies it as a HELD number). Borderline on the 4-field test (fails only on Inputs: the fibre-connection-geometry construction is not yet pinned); routed as a S103-plan candidate compute with the geometry-construction as the inputs-to-identify.

1. **What**: derive δA from the §VII.BL external-connection geometry and test whether an independent fibre-connection geometry FORCES the ε_LX magnitude (required steepness `missing_slope = 0.30367/C₂` is fully fixed; what is missing is a geometric derivation of δA).
2. **Inputs**: `s102_nu_grading_external_epslx.npz` (audit `a3e1cf7b31f69646…`, 27 keys); §VII.BL Generation-Blindness Obstruction external-connection geometry (STAGE-3-PERMANENT); the fibre-connection-geometry construction (TO IDENTIFY — the binding inputs-pin gap).
3. **Gate**: `CF-S103-NU-DELTA-A-FIBRE-GEOMETRY` — PASS = ε_LX substrate-motivated forces `g_ε,3/g_ε,2 = 1.6588` ⇒ Y₃/Y₂ within 5%; INFO = δA irreducibly external like the Dirac scale.
4. **Effort**: 1 gate (preceded by the geometry-construction identification; if the construction cannot be pinned at S103 plan-freeze, the item stays in `/rclab-investigate` triage).

### CF-W4-2 — CKM triality-texture theorem registry landing [Q2-hygiene]

> **Routing note**: Q2-class mechanical promotion per `Investigating-Workshops.md §"Q2"` (registry-row landing of an already-derived theorem; the resolution is a registry-state write, NOT adversarial physics). Surfaced for the first time by the S102 `/rclab-investigate` W4 seed; the structural payoff is currently buried in §W4-15 and is NOT registered, NOT in this block, and NOT in the housekeeping ledger. The W4-15 selection-rule pre-flight PROVED gen3↔gen2 and gen3↔gen1 CKM channels are EXACTLY zero (CG-inadmissible, `t(p,q)=(p−q) mod 3`, t=1 vs t=0) and gen2↔gen1 (Cabibbo) is the sole admissible channel — a genuine NEW substrate prediction (qualitatively the observed CKM hierarchy: V_ub, V_cb triality-suppressed relative to V_us) that survives independent of the crossing FAIL.

1. **What**: register the CKM triality-texture theorem (gen3↔gen2 and gen3↔gen1 channels EXACTLY forbidden by CG-inadmissibility; Cabibbo gen2↔gen1 sole admissible channel; `Ω^D/Ω^c = 2` Sage-exact; [J,D_K]=0 / W3-9 intact) as a §VII registry theorem row in the next-free slot.
2. **Inputs**: `s102_quark_pergen_kernel.npz` (audit `77659eb6809d3d46…`, 58 keys); §W4-15 selection-rule pre-flight + CKM-texture sub-result; the SU(3) triality / center-character machinery (`math-scripts.md` selection-rule pre-flight section).
3. **Gate**: `S103-CKM-TRIALITY-TEXTURE-REGISTRY-LANDING` — artifact-existence + content-marker PASS predicate (AFTER-pattern single-shot per `registry-landing.md §"Bridge-Landing Script Architecture"`).
4. **Effort**: 1 gate (registry-landing class).

### CF-S103-NO-SIGN-HANDLE — §VII registry-candidate No-Sign-Changing-Slope-Handle WALL theorem [Q2 registry landing; campaign-added]

> **Routing note**: added 2026-06-10 by the S102 review campaign. The Slot-1 S-3 classification (`session-102-phonon-first-quark-crossing-synthesis.md`) ran the WALL-vs-GAP adjudication this block's intro paragraph anticipated: verdict **WALL** — every G-invariant scalar on the single-τ-slice Peter-Weyl spectral triple is C₂-monotone or a Jensen-invariant binary triality step across the generation sectors {(1,0),(1,1),(3,0)}, never the strict gen-2 interior extremum a sign flip requires; all four GAP-candidate ingredients (full-SU(3) σ-model, off-diagonal triality, second modulus, off-Jensen Schur directions) resolve to the WALL side. **`CF-S103-QUARK-KAPPA-G-<handle>` therefore does NOT instantiate** (no fillable handle); this WALL-theorem landing replaces it. Consolidated spec: S-5 closeout (`session-102-phonon-first-closeout-landscape-synthesis.md` §V V.1).

1. **What**: land a §VII registry-candidate STRUCTURAL theorem (next-free §VII letter; AFTER-pattern single-shot per `registry-landing.md`): "the single-τ-slice spectral triple (A_K, H_K, D_K(τ_fold)) provides NO G-invariant scalar non-monotone across the three generation sectors {(1,0),(1,1),(3,0)} (C₂={4/3,3,6}); every per-generation slope kernel built from the Peter-Weyl invariant content (C₂-graded greybody, bare-ladder RMS, Jensen-invariant triality step) is same-signed across generations ⇒ the joint quark crossing (gen-1 inversion ∧ gen-3 upright) is NOT deliverable by any single-τ-slice A_K-built kernel." Declare: intra-pillar structural theorem (5-anatomy + 3-level N/A-with-reason, precedent §VII.BL); Level-1 single-τ-slice; algebra-INVARIANT operator layer; SOURCE-DOUBLE-CITE-CO-PRIMARY Corner-I (W4-15 verdict V_input + route-(b)-exhaustion enumeration C_output); STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BL (SHAPE-branch sibling — NOT co-primary; cross-corner co-primary FORBIDDEN); cite W2-11 triality-preservation + §VII.BR Schur-rigidity as the two structural pins making the WALL deformation-stable.
2. **Inputs**: `s102_quark_pergen_kernel.npz` (audit `77659eb6…`, 58 keys); §VII.BL (STAGE-3-PERMANENT, SHAPE-branch anchor); §VII.BR (STAGE-3-PERMANENT); W2-11 triality-preservation (PROVEN); the route-(b) enumeration table (S-3 synthesis §II.2).
3. **Gate**: `S103-NO-SIGN-HANDLE-REGISTRY-LANDING` — artifact-existence + content-marker PASS (PASS = §VII section body with the 5 declared structural elements + route-(b)-exhaustion table + §VII.BL sibling-companion anchor; FAIL = section absent or a declared element missing). Sole writer = registry §VII sole-writer; NOT a §7 falsifier-surface row (mack-cosmic-bridge does not apply).
4. **Effort**: 1 gate (registry-landing class; ~1 agent-session); no compute (the W4-15 verdict + the closed-form enumeration ARE the structural content).

**CF-W4-1 spec completion (2026-06-10, S-5 closeout §V V.6)**: the binding Inputs gap above ("fibre-connection-geometry construction TO IDENTIFY") is now gate-spec'd as `S103-NU-DELTA-A-FIBRE-GEOMETRY` — PASS = δA derived from fibre geometry reproduces `missing_slope = 0.3036690/C₂` at ≤5% with `eps_LX_substrate_motivated=True` (the hold DISCHARGES; Y₃/Y₂ becomes a prediction); FAIL = no substrate-geometric derivation of δA exists (the SHAPE-leg ε_LX is permanently HELD, NON-PROMOTION-BY-HELD-NUMBER); INFO = δA derivable at a DIFFERENT magnitude (re-pin, not discharge). Effort 3-4 hours, 1 agent session (neutrino-detection-specialist owns the greybody/seesaw machinery; connes-ncg-theorist cross-checks the non-LI connection embedding). Readiness per the S-5 table: **HOLD** pending the geometry-construction pin.

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-06-09 | Quark gen-1↔gen-3 crossing (W4-15) | OPEN — uniform-κ impossible (W2-4), per-gen DERIVED kernel untested | CLOSED for the dressed-block greybody per-gen kernel (sign-flip structurally absent; slope asymmetry +,+,+ monotone) | FAIL at the pre-registered Step-5 crossing condition; route-(b) non-monotone seed exhausted |
| 2026-06-09 | CKM texture (W4-15 sub-result) | qualitative observation | Triality theorem: gen3↔gen2 and gen3↔gen1 channels EXACTLY zero (CG-inadmissible, t=1 vs t=0); Cabibbo gen2↔gen1 sole admissible channel | selection-rule pre-flight on t(p,q)=(p−q) mod 3; independent of the crossing FAIL |
| 2026-06-09 | s_ν neutrino shape slope, candidate-(c) (W4-16) | consistent-but-not-forced +0.5469 (S101 compare-to-self tautology) | SIGN substrate-FORCED (+, widening); MAGNITUDE re-pinned at derived ≈+0.0877; +0.5469 = S99 Y-ratio back-solve coincidence | independent B-branch (c²−v²) log-gradient, back-solve guard CLEAN (AST-verified) |
| 2026-06-09 | ν generation grading architecture (W4-17) | W3-4 gap-eq shape-FAIL (+39.7%) unexplained | Gap-eq shape-flatness STRUCTURAL (scale cancels in ratios; reproduces W3-4 to 0.00e+00); scale-from-gap-eq / shape-from-external division of labor CONFIRMED; ε_LX magnitude HELD (back-out, not substrate-motivated) | division-of-labor substitution chain; MCP audit shows no canonical pins ε_LX/δA |
| 2026-06-09 | Model-C (Pati-Salam G422D) viability (W4-18) | SOLVED scales untested vs experiment; M_U-low proton-decay risk live | SURVIVES both bounds (τ_p = 6.26e39 yr via T17 tree-level zero, 2.6e5 × Super-K; S₁ flavor 8.7 OOM decoupled); naive estimate genuinely excluded — survival is mechanism-dependent | T17 (proven_1844) + Baptista eq_26 applied to the 0-free-param solved scales |
| 2026-06-09 | M₀-screening transfer level (W4-19) | CONVENTION-SENSITIVE (W4-5: PRIM vs RG spread 1.1806% > 1.0%) | RESOLVED: boundary-RG derived substrate-first (Γ_eff acts on the vacuum partition, a boundary quantity; w0_FW witness); spread 0.0% under derived convention; residual −0.4612% | BCS-chain-position derivation; both-convention band-shrink sign PASS (convention-independent) |
| 2026-06-09 | m_H route (W4-20) | Two-route ambiguity (KK-L5 Aitken 127.5 vs KK-threshold DIRECT 131.8) | Route B (131.8) FORCED by a₄-KK saturation (L_sat=6; Aitken spurious, overshoot 1.2416× floor); accommodation corridor EXCLUDED; W5-3 keyed to 3-state (b) | no-PDG-appeal convergence diagnostic; Friedrich-Bär saturation (PROVEN S87/S89/S90) is the structural certificate |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict rows |
|:-----|:-------|:------------|:------------|:-------------|
| W4-15 | `s102_quark_pergen_kernel.py` (34,676 B) | `s102_quark_pergen_kernel.npz` (15,938 B, 58 keys) | `s102_quark_pergen_kernel.png` (124,237 B) | canonical + companion + 3-tuple + 2 extra |
| W4-16 | `s102_kappa_nu_firstprinciples.py` | `s102_kappa_nu_firstprinciples.npz` (38 keys) | `s102_kappa_nu_firstprinciples.png` | original + corrective (`supersedes=1bc8e08e…`) + 3-tuple + composite-precedence row |
| W4-17 | `s102_nu_grading_external_epslx.py` | `s102_nu_grading_external_epslx.npz` (27 keys) | `s102_nu_grading_external_epslx.png` | canonical + companion |
| W4-18 | `s102_modelc_pheno_scales.py` | `s102_modelc_pheno_scales.npz` (9,965 B) | `s102_modelc_pheno_scales.png` (97,422 B) | original + corrective (`supersedes=379971ce…`) + companions |
| W4-19 | `s102_m0_transfer_convention.py` | `s102_m0_transfer_convention.npz` | `s102_m0_transfer_convention.png` | canonical + companion + 3-tuple + 2 extra (chain-position / fb_backward) |
| W4-20 | `s102_mh_route_selection.py` | `s102_mh_route_selection.npz` (10,657 B; W5 forward-pin) | `s102_mh_route_selection.png` (91,538 B) | canonical + companion + 3-tuple + regulator_pin row |

All in `computations/session-102/`; verdict file `computations/session-102/s102_gate_verdicts.txt`.
