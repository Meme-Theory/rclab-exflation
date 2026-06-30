# Session 106 Wave 2 — ω'_z Hawking-dressed-relic modular successor + CdGM ladder rigidity (Results Working Paper)

**Session**: 106 | **Wave**: W2 | **Plan**: session-106-plan-w2.md | **Theme**: the relocated acoustic-frozen relic ω'_z (Hawking-dressed ω) — existence/faithfulness construction, the area-clock question on σ_t^{ω'_z}, and CdGM horizon-core ladder-spacing cross-block rigidity.

## Gate Sections

### §W2-1. S106-OMEGAPRIME-Z-CONSTRUCTION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S106-OMEGAPRIME-Z-CONSTRUCTION`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (the frozen GGE relic's Hawking-dressed modular structure near the acoustic horizon)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: the Hawking-dressed occupation f'_a = 1/(1+e^{K_a z_a}) (z_a = 1/√(−g_00^eff) extracted from the S47 acoustic-metric construction) is faithful-normal on the bulk {|λ| > lam_horizon}, cleanly empty-Fock at the floor (K_floor·z_floor → +∞, the guaranteed N₃=0 fixed point), so Δ_{ω'_z}^{it} exists on the named horizon blocks.
**Plan reference**: `sessions/session-plan/session-106-plan-w2.md` §W2-1 (g_00^eff extraction, faithfulness witness, floor fixed-point DSr3-1, machinery pin, substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Verification |
|:---------|:-----|:-------------|
| script | `computations/session-106/s106_omegaprime_z_construction.py` | EXISTS (34379 B); `grep` confirms `from canonical_constants import` ✓ + `print_verdict_payload` ✓ |
| data | `computations/session-106/s106_omegaprime_z_construction.npz` | EXISTS (102814 B); 49 keys incl. `neg_g00`, `z`, `f_prime`, `delta_it_bulk`, `floor_mask`, `verdict=PASS` |
| plot | `computations/session-106/s106_omegaprime_z_construction.png` | EXISTS (100050 B); 3-panel: extracted −g_00^eff(λ) / Tolman z_a / Hawking-dressed f'_a + Layer-2 witness |
| verdict_line | `computations/session-106/s106_gate_verdicts.txt` | `^S106-OMEGAPRIME-Z-CONSTRUCTION:.* audit_sha256=[a-f0-9]{64}` ✓ (audit_sha256=`4dd27aee…44e916`); dual-SHA companion row ✓; schema-v2 3-tuple row ✓ ([CHAIN] floor-direction) |

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries executed BEFORE writing the script):
- `search_knowledge("omega prime Hawking-dressed relic modular successor acoustic frozen")` → no prior ω'_z construction; closest is the S2-1 workshop ω-corridor RESERVABLE-via-frozen-ω note + the discrete modular flow eq A.9 `σ_1^ω = Ad(Δ_ω^{i})`. **NOT PRE-CLOSED** — this is a genuine NEW-COMPUTE existence gate.
- `search_knowledge("EMr3-1 acoustic horizon g_00 Tolman redshift Bogoliubov dressing GGE relic")` → S47 acoustic-horizon provenance (HORIZON-48) + Volovik acoustic-metric `g^{00}=−1/(mnc)` (Paper 01 Eq.13) + GGE-relic R_therm=5252/S_ent=0 (S105 W2-2 framing). Confirms S47 is the methodological acoustic-construction source; g_00^eff profile not previously extracted.
- `get_constant("Delta_B3")` → 0.176 (S38, B3-sector pairing gap, M_KK units) — matches plan substitution-chain pin.
- `get_constant("T_GGE")` → resolves to `T_GGE_B2 = 0.668` — matches plan T_GGE pin (the W2-2 frozen-GGE temperature field).
- Nearest prior gate: `S104-AREA-MODULAR-GENERATOR-SPEC` (INFO; construction named, ingredients UNPINNED = ω | A_hor). This gate PINS the missing ω'_z-side ingredient (the g_00^eff profile + the dressed state).

**Verdict**: **PASS** — ω'_z is a faithful-normal state on the BULK {|λ| > lam_horizon} (0 < f'_a < 1 strict, Layer-2 witness emitted before any downstream use) AND the floor mode is cleanly empty-Fock (K_floor·z_floor → +∞, NOT 0·∞) AND Δ_{ω'_z}^{it} is constructed on the named blocks. 3-tuple: `sign=PASS / magnitude=PASS / regime=VALID`. The Hawking-dressed relic is a well-posed relocated object with its own modular flow σ_t^{ω'_z} — **unblocks 2b**. The relocated corridor is ALIVE (not stillborn).

**Results**:

NUMBERS first.

*Basis alignment (load-bearing).* The 720-mode construction is built in the EXACT `(BdG-sector outer ∈ {B2, B3, BCS}, Peter-Weyl block inner ∈ {(0,0),(1,0),(0,1),(1,1)})` concatenation order W2-3 used for `K_modular`. The rebuilt K reproduces the stored `K_modular` **bit-for-bit**: `max|K_rebuilt − K_modular| = 0.0e+00` over all 720 modes. This guarantees z_a, f'_a, K_a z_a are index-aligned to K_modular mode-for-mode.

*FIRST DELIVERABLE — extracted g_00^eff(λ) profile* (the one missing substrate input the GEM workshop named; Akama-Diakonov CF19 / S47 acoustic principle):
```
−g_00^eff(λ_a) = (|λ_a| − lam_horizon)/(λ_ref − lam_horizon)
  lam_horizon = 0.8197411121   (interp (i): global min|λ| over named blocks = the sonic surface)
  λ_ref       = 1.6695681988   (max|λ| over named blocks = UV/asymptotic edge, −g_00 = 1, metric flat)
  denom       = 0.8498270867
  −g_00^eff ∈ [0.000000, 1.000000]   (0 at the floor where the metric degenerates; 1 at the UV edge)
```
The BdG kinetic distance ξ_a = |λ_a| − lam_horizon IS the proper distance from the acoustic horizon; −g_00^eff is its normalized square, vanishing exactly at the sonic surface.

*Tolman redshift weight z_a = 1/√(−g_00^eff)*: bulk z ∈ [1.000000, 7.253487] (1 at the UV edge, large near the horizon); floor z = +∞ (6 modes — the Tolman divergence at the sonic surface). The regrade acts on K̂ ONLY (Layer-1: a state-change, not a frame-relabel of ω).

*Hawking-dressed occupation f'_a = 1/(1+e^{K_a z_a})* (bulk): min 3.523094e-04, max 3.051737e-01.

*LAYER-2 FAITHFULNESS WITNESS (emitted BEFORE any downstream use; guard (b)):* on all 714 bulk modes {|λ| > lam_horizon}, `all f'_a > EPS_FAITHFUL` = True AND `all f'_a < 1−EPS_FAITHFUL` = True (EPS = 1e-12). **BULK FAITHFUL = True.** Layer-2 margin to the nearest boundary {0,1} = 3.523094e-04 ≫ EPS — no bulk mode is depleted to the empty-Fock non-state. (No bulk mode driven to {0,1} ⇒ NOT the FAIL/ill-posed-relocation branch.)

*Floor empty-Fock (carried explicitly; interp (i); guard (c); DSr3-1):* 6 floor modes (the global-min eigenvalue appears once per BdG sector in block (0,0): B2|(0,0), B3|(0,0), BCS|(0,0) each contribute 2), all with f'_floor = 0. `floor_empty_Fock = True`.

*Δ_{ω'_z}^{it} construction:* generator diag(K_a z_a) on the bulk has dim 714, range [0.822781, 7.950648]; Δ_{ω'_z}^{it} = exp(−it·diag(K_a z_a)) is unitary at the representative t=1 (|e^{−it·Kz}| = 1, the discrete modular flow σ_1^{ω'_z} cf. eq A.9); GPU (AMD RX 9070 XT) used, GPU/numpy agree < 1e-9. The floor contributes the empty-Fock projector — a fixed point of the flow, not a finite generator value.

**Substitution chain (sign/direction claim — K_floor·z_floor → +∞ clean, NOT 0·∞; reproduced + verified, [CHAIN] mandatory):**

Claim: at the floor mode |λ| = lam_horizon, f'_floor → 0 (empty-Fock) CLEANLY via K_floor·z_floor → +∞ — not the indeterminate 0·∞ — because the BDI/N₃=0 +½ minigap makes E_floor = Δ_B3 > 0 strictly.

| Step | Substitution | Result |
|:-----|:-------------|:-------|
| 1 | ξ_floor = \|λ\|_floor − lam_horizon = lam_horizon − lam_horizon | 0 |
| 2 | E_floor = √(ξ_floor² + Δ_B3²) = √(0 + 0.176²) | 0.176 = Δ_B3 > 0 (GAPPED; CdGM +½ minigap) |
| 3 | K_floor = E_floor / T_GGE = 0.176 / 0.668 | 0.263473 > 0 STRICT (= K_modular.min(), match = True) |
| 4 | −g_00^eff(floor) = 0/(λ_ref − lam_horizon) = 0 ⇒ z_floor = 1/√0 | +∞ |
| 5 | K_floor · z_floor = (0.263473 > 0, FINITE) × (+∞) | +∞ (NOT 0·∞) |
| → | f'_floor = 1/(1 + e^{+∞}) | 0 (empty-Fock) |

Direction: K_floor > 0 FIXED, z_floor → +∞ ⇒ K_floor·z_floor → +∞ ⇒ f'_floor → 0, CLEAN. z-sweep confirms monotone descent: z=10 → f'=6.694e-02; z=50 → f'=1.900e-06; z=10³ → f'=3.759e-115. **Conclusion**: the floor-mode empty-Fock is the UNIQUE, well-defined fixed point of the dressing map, GUARANTEED by N₃=0 (E_floor = Δ_B3 > 0 removes the 0·∞ indeterminacy a 3He-A Weyl zero would have). A boundary condition, NOT a discovery. [DSr3-1] `sign_verdict = PASS`.

**4-tuple**: `(value='omegaprimez=constructed;bulk_faithful=True;floor_empty_Fock=True;n_bulk=714;n_floor=6;layer2_margin=3.523094e-04;K_floor=0.263473;K_floor_zfloor=+inf_clean;Delta_omegaprimez_it_built=True;index_align_maxdiff=0.0e+00', scheme=FW, convention=ACOUSTIC-FROZEN-OMEGAPRIME-Z;TOLMAN-REGRADE-K-HAT-ONLY;FLOOR-INTERP-(i), L_max=10)`.

**Dual-SHA + 3-tuple companion rows** (in `computations/session-106/s106_gate_verdicts.txt`): `audit_sha256=4dd27aee5ff1ce8895b113133c71ce29f0716854c9c6c9af8632a582eb44e916`, `content_sha256=fc3088537e279a76f8bfee49df6ba0453a68d684458c329cc9cd422de36bdbe0`; 3-tuple `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.

**Per-block f'_a diagnostic (bulk; not gated):** B3 (binding, smallest gap 0.176) carries the largest occupations (f'_bulk up to 0.305 — least suppressed, as expected from weakest protection); B2 (largest gap 0.732) the smallest (down to 3.5e-04). All blocks strictly interior. A-V3 scale-segregation read av3_ratio = 0.28966 (carried diagnostic, not gated).

**Plan-text drift (recorded per `substrate-first-canonical-sourcing.md §(ii.B)`):** the plan-pinned `canonical_constants.py` SHA `38e23ad271…` resolved at runtime to `82dd16e2ed…` (the file was extended by S106 W1 between plan-freeze and dispatch; mtime Jun 12 19:29). The dual-SHA captures the runtime state; the verdict is INVARIANT to this drift (the construction reads only `Delta_B2/Delta_B3/Delta_BCS/T_GGE_B2`, all unchanged — values cross-checked against the W2-2/W2-3 npz fields). Drift documented in the verdict-line companion rows. (Input npz/py pins all matched plan exactly: s105_w2_2 `7e8a…`, s105_w2_3 `25ea…`, s84_cache `9e6d…`, s47_acoustic `3e6a…`.)

**Three admissibility guards (workshop pre-registration — VERBATIM, MANDATORY per cross-wave constraint 3):**

**(a) Layer-1 identity guard (z-INDEPENDENT).** Any comparison this gate's output participates in is stated against `σ_t^{ω'_z}`, NEVER `σ_t^ω`. The `f↔K` bijection (Tomita-Takesaki) makes `ω'_z ≠ ω` for ANY `z ≠ 1`, so any downstream gate on `σ_t^{ω'_z}` tests `G_τ = σ_t^{ω'_z}`, NEVER the now-CLOSED `G_τ = σ_t^ω`. Stating the comparison against `σ_t^ω` is a CATEGORY ERROR independent of any numerical outcome (the ω-identity is CLOSED-AT-IDENTITY by Tomita-Takesaki uniqueness — S105 GEM-WORKSHOP Row 3). *(Honored: this construction's convention tag carries `ACOUSTIC-FROZEN-OMEGAPRIME-Z`; z_max = 7.25 ≠ 1 confirms ω'_z ≠ ω.)*

**(b) Layer-2 faithfulness witness (z-DEPENDENT).** ω'_z's OWN faithfulness witness (`0 < f'_a < 1` strict on every BULK mode `{|λ_a| > lam_horizon}`) is emitted BEFORE any comparison. A `z` driving a BULK mode to empty-Fock (`f'_a → 0` or `→ 1` on a mode strictly above the floor) is FALSIFIED as a faithful relocation — the substrate-physics realization of PROHIBITED_ACTIONS Class 1 ("don't change the STATE until the comparison passes"). This is gate 2a's PASS predicate. *(Honored + PASS: witness computed and emitted as step (4) above, BEFORE the Δ_{ω'_z}^{it} build; bulk margin 3.5e-04 ≫ EPS.)*

**(c) Floor-mode domain, interp (i) (boundary condition, NOT a discovery).** The floor mode `|λ| = lam_horizon = 0.8197411121` is carried EXPLICITLY empty-Fock: faithful strictly ABOVE the floor, empty-Fock AT the floor. This is the GUARANTEED N₃=0 Hawking-depletion fixed point (DSr3-1): `E_floor = Δ_B3 = 0.176 > 0` ⇒ `K_floor·z_floor → +∞` CLEAN (not `0·∞`). Pinned per interp (i) (W2-2 line 95/301: `lam_horizon = global min |λ| over the named blocks = the floor eigenvalue`) — so the construction is NOT PRU-vulnerable on the floor mode. *(Honored: floor identified by metric degeneracy −g_00^eff < 1e-12 = the sonic surface; 6 floor modes all carried f'_floor = 0 with the clean K_floor·z_floor → +∞ limit verified in the substitution chain.)*

**Assessment (substrate-first).** The substrate IS the frozen GGE relic; ω'_z is that same relic Hawking-dressed (Volovik §32), NOT a new container. The direction of explanation flows D_K spectrum (named horizon blocks) → BDI/N₃=0 (E_floor = Δ_B3 > 0) → ω-side K_a = E_a/T_GGE AND emergent −g_00^eff(λ) → Tolman z_a (regrades K̂ only) → Hawking-dressed f'_a → modular flow σ_t^{ω'_z} = Ad(Δ_{ω'_z}^{it}). The floor-mode empty-Fock is the analog-Hawking horizon doing what a horizon DOES to local occupation (total depletion at the sonic surface), GUARANTEED clean by N₃=0 — read as a substrate-internal modular structure, never as a flow IN a container-horizon. The existence gate PASSes: ω'_z is a well-posed faithful relocation with its own thermal time. This unblocks the §W2-2 area-clock comparison `‖K̂·z − Ĝ_τ‖_op < tol` (the σ_t^{ω'_z}-vs-G_τ test, NOT the closed ω-identity). The structural status of ω'_z is now: CONSTRUCTED, faithful-normal on the bulk, with an explicit empty-Fock floor fixed point — a NEW relocated modular object, registry-CANDIDATE-eligible pending its own 5-anatomy at a future session (no S106 registry write).

---

### §W2-2. S106-OMEGAPRIME-AREA-CLOCK (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S106-OMEGAPRIME-AREA-CLOCK`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (area-flow generator a_2 Seeley-DeWitt vs the Hawking-dressed-relic modular flow)
**Agent**: `connes-ncg-theorist`
**Dispatch condition**: GATED on §W2-1 (`S106-OMEGAPRIME-Z-CONSTRUCTION`) PASS. **2a PASSED** (`verdict=PASS; bulk_faithful=True; floor_empty_Fock=True; Δ_{ω'_z}^{it} built; audit_sha256=4dd27aee…`) ⇒ this gate RAN as a genuine comparison (NOT mechanically closed). Existence established; we compared.
**Hypothesis**: the area-flow generator G_τ and the Hawking-dressed-relic modular flow σ_t^{ω'_z} agree at op-norm (‖K̂·z − Ĝ_τ‖_op < tol) with cocycle sign = −1 (matching S97 dS/d(a0/a2) = −1) — a NEW cross-pillar bridge CANDIDATE, NOT a reopening of the closed G_τ = σ_t^ω (guard (a): names σ_t^{ω'_z} only).
**Plan reference**: `sessions/session-plan/session-106-plan-w2.md` §W2-2 (op-norm tol=1e-3 inherited from W2-3, S97 sign chain, dual-prior, candidate-only routing — NO S106 registry write).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-106/s106_omegaprime_area_clock.py` — EXISTS (`from canonical_constants import` + `print_verdict_payload` both present; grep-confirmed below).
- `computations/session-106/s106_omegaprime_area_clock.npz` — EXISTS (op-norm primaries, generators on the 714-mode bulk, sign chain, gating witnesses).
- `computations/session-106/s106_omegaprime_area_clock.png` — EXISTS (left: unit-normalized $\widehat{K\!\cdot\!z}$ vs $\hat G_\tau$ on the bulk; right: ungraded-vs-Tolman-regraded op-norm vs tol).
- Verdict line `^S106-OMEGAPRIME-AREA-CLOCK:.* audit_sha256=[a-f0-9]{64}` in `computations/session-106/s106_gate_verdicts.txt` — EXISTS (dual-SHA companion + schema-v2 3-tuple row + 5 extra companion rows; emitted via the race-safe `emit_verdict` MCP tool, sig_5-unique).
- WP markers Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit — present in this section. Verification by content presence, not line count.

**MCP Pre-Compute Audit**:
- `search_knowledge("area-clock modular flow Tomita-Takesaki cocycle KMS spectral triple")` → returned the S105-plan sign-equation (`cocycle-generator sign = −1 = S97 dS/d(a0/a2)`) and the modular-flow Ad(Δ^{it}) corpus; no prior 2b verdict — gate not pre-closed.
- `trace_entity("modular flow area clock")` → no trace (this exact bridge object is new at S106; consistent with a CANDIDATE-only gate).
- `get_constant("a_2_FW_zeta")` → **2776.165389** (S88; gate S88-A-N-FW-CANONICALIZATION) — the area operator Â = a_2^{ζ}; confirmed against the W2-3 npz `A_hat`.
- `search_knowledge("S97 dS d(a0/a2) area law monotonicity p_exponent decreasing cocycle sign")` → S97-DS-AREA-LAW-MONOTONICITY (`dS/d(a0/a2)=−1, decreasing=True, p_exponent=−1`) + S105-W2-3-AREA-MODULAR-AGREEMENT (`op_norm_diff=1.773745 vs 1e-3, cocycle_gen_sign=−1 eq_S97=True`, composite INFO) — the ω-side precedent this gate re-runs with the Tolman regrade.
- Sage `sage_eval` (sign chain): S = r^p, p=−1 ⇒ dS/dr = −1/r² < 0 ⇒ sign(dS/d(a0/a2)) = −1 (the analytic OUTER-class co-orientation).

**Verdict**: **INFO** (composite). 3-tuple: **sign_verdict=PASS, magnitude_verdict=FAIL, regime_verdict=VALID** → INFO via the **plan-frozen composite-precedence operator** (§W2-2 `INFO_meaning` pre-registers sign=PASS+magnitude=FAIL+regime=VALID as INFO — co-monotone-but-not-equal — overriding the generic-collapse FAIL reading; `gate-verdicts.md` "Plan-frozen gate-block operator precedence"; structurally identical to the W2-3 precedent). `audit_sha256=3ec79a94f30887c17766815ee3f761bad0a59df76e7fe92f354a79d673a744bc`, `content_sha256=19bbd49e48ad6be5012f388abdc772ad1bdc517e68461c654f6b24efbfde758c`.

**Results**:

**NUMBERS (gate first).**

| Quantity | Value | Bar | Verdict |
|:---------|:------|:----|:--------|
| `‖K̂·z − Ĝ_τ‖_op` (BULK, 714 modes) | **1.163407** | tol = 1e-3 | magnitude **FAIL** |
| W2-3 ungraded `‖K̂ − Ĝ_τ‖_op` (precedent) | 1.773745 | — | (reference) |
| Tolman-regrade gap reduction | 0.610338 (**34.41%** toward Ĝ_τ) | — | regrade moves K̂ toward Ĝ_τ but NOT below tol |
| cocycle-generator sign | **−1** | = S97 ref −1 | sign **PASS** (sign_match = True) |
| `‖K̂·z‖_op` (bulk spectral radius) | 7.950648 | — | (normalization) |
| GPU vs numpy op-norm agreement | `|Δ| < 1e-9` (gpu_used=True, agree=True) | < 1e-9 | regime VALID |
| basis alignment (2a K_mod vs W2-3 K_mod) | maxdiff = **0.0** | < 1e-12 | aligned — comparison well-posed |

4-tuple: `value=composite=INFO;op_norm_diff=1.163407e+00_vs_tol=1e-03;cocycle_gen_sign=-1_eq_S97=True;…`, `scheme=FW`, `convention=ACOUSTIC-FROZEN-OMEGAPRIME-Z-AREA-CLOCK;COMPARE-AGAINST-SIGMA-OMEGAPRIME-Z-ONLY;UNIT-NORMALIZED-OPNORM`, `L_max=10`. `regulator_pin=a_2^{ζ}` (a_2_FW_zeta = 2776.165389; poleconv-A-double, pole_in_s=3, curvature_grade_n=2).

**Substitution chain (the [SIGN] cocycle-generator claim = −1; verified Python at runtime + Sage at plan-freeze).**
- Step 1: S97 reference — S = A/(4G_N), A = a_2, G_N ∝ 1/a_2 (substrate area-IS-a_2, S63/S97). The area-law functional S ~ (a0/a2)^p has `s97_p_exponent = −1`, `s97_decreasing = True` (read from the W2-3 npz, sourced from S97).
- Step 2: Sage symbolic — S(r) = r^p with r = a0/a2; dS/dr = p·r^{p−1}; at p = −1, S = 1/r, **dS/dr = −1/r² < 0 for all r > 0** ⇒ sign(dS/d(a0/a2)) = **−1**.
- Step 3: recomputed cocycle generator (W2-3 npz, the a0/a2-axis cocycle generator of the area flow): `cocycle_generator_sign = −1`.
- Step 4: `sign_match = (cocycle_generator_sign == S97_sign_reference) = (−1 == −1) = True`; cross-check `p_sign_consistent = (sign(p_exp) == −1) ∧ decreasing = True`.
- Direction/conclusion: −1 = −1 ⇒ G_τ and σ_t^{ω'_z} are **co-oriented** along the area-law axis (both decrease the entropy-conjugate as a0/a2 grows). This is the OUTER-class / second-law datum (state-INDEPENDENT) — **necessary but NOT sufficient** for a geometric area-clock; the INNER/identity content is carried by the op-norm conjunct, which **fails** at tol. Hence `sign_verdict = PASS`, but the composite is INFO (area-clock IDENTITY not established).

**Three admissibility guards (workshop pre-registration, VERBATIM, all satisfied).**
- **(a) Layer-1 identity guard (z-INDEPENDENT).** The comparison is stated against σ_t^{ω'_z} ONLY, NEVER σ_t^ω. ω'_z ≠ ω for any z ≠ 1 (the f↔K bijection; 2a built K̂·z = K̂ Tolman-regraded by finite z on the bulk, z ranging 1.0–7.25 per the 2a per-block table). Even a PASS would NOT reopen GEM-Q1 (the now-CLOSED G_τ = σ_t^ω, S105 GEM-WORKSHOP Row 3); stating this comparison against σ_t^ω is a category error independent of numerics. The convention string `COMPARE-AGAINST-SIGMA-OMEGAPRIME-Z-ONLY` pins this in the verdict line.
- **(b) Layer-2 faithfulness witness (z-DEPENDENT).** Gate 2a emitted ω'_z's faithfulness witness (`0 < f'_a < 1` strict on the bulk; Layer-2 margin = 3.523e-04 ≫ EPS = 1e-12, n_bulk = 714) BEFORE this comparison ran — the 2a→2b gating IS the structural enforcement of "don't change the STATE until the comparison passes" (the substrate realization of PROHIBITED_ACTIONS Class 1). A z that closed this gap by depleting a BULK mode to empty-Fock would have FAILED 2a. Gating verified at runtime: `gating_status = True`.
- **(c) Floor-mode domain, interp (i).** The floor mode (n_floor = 6) is empty-Fock (gate 2a), K̂·z = +∞ there (z_floor = 1/√0 = +∞, K_floor = 0.263473 > 0 ⇒ K_floor·z_floor → +∞ clean, NOT 0·∞ — guaranteed by N₃=0, E_floor = Δ_B3 = 0.176 > 0). It carries no finite generator value and is **EXCLUDED** from the op-norm; the comparison is on `{|λ_a| > lam_horizon}` only (lam_horizon = 0.8197411121). All `K̂·z` bulk entries verified finite at runtime.

**Cross-checks.**
- **Basis alignment**: 2a `K_modular` (E_a/T per mode) == W2-3 `K_modular` to maxdiff 0.0 — the diagonal generators live on the identical 720-mode BdG ordering, so `K̂·z` and `Ĝ_τ` are directly comparable entry-by-entry (a silent mode-order drift would have raised RuntimeError; it did not).
- **Ungraded-on-bulk reproduction**: restricting the W2-3 `K̂` to the bulk and differencing against `Ĝ_τ` reproduces the W2-3 precedent op-norm **1.773745 exactly** — confirms the bulk carries the spectral radius and the only change in this gate is the Tolman regrade K̂ → K̂·z.
- **GPU/CPU agreement**: numpy op-norm (max|diff|) and torch.linalg.matrix_norm(ord=2) of diag(diff) agree to < 1e-9 (gpu_used=True on cuda:0).
- **Normalization convention**: both operands unit-normalized by their own bulk spectral radius (K̂·z by ‖K̂·z‖_op = 7.95; Ĝ_τ already unit-normalized in W2-3 by G_norm = 0.16907) — identical to the W2-3 op-norm convention; the test asks whether the two diagonal generators are proportional (= identical modular flow up to thermal-time reparametrization).

**Dual-prior posterior re-allocation.** The discriminator (§W2-2 `dual_prior`): FAIL/INFO → **0.9 to Track A** (Reading A: the Hawking-dressed relic ALSO lacks a geometric area-clock; the Tolman regrade does NOT close the gap below the same bar the ω-side test used). Track B (NEW area-clock bridge) does **NOT** get the candidate. The prior leaned A (0.6) because the workshop established the gap is a near-maximal unitary invariant in the global frame (1.7737); the regrade pushed K̂ 34.41% toward Ĝ_τ but stopped well above tol — confirming Reading A.

**Disposition (CANDIDATE-only routing).** Composite INFO ⇒ NOT a PASS ⇒ **no new bridge candidate** and (a fortiori) **no S106 registry write** (a PASS would have produced a CANDIDATE only; INFO produces none). The 5-anatomy + 3-level registration of any acoustic-area ↔ Hawking-dressed-relic-modular-flow bridge is moot for this outcome; the session-index obligation (v) — route a 2b PASS's 5-anatomy registration to S107 — does not fire. The surviving registrable relation is the **co-monotone-plus-shared-floor bridge** (sign = −1 co-orientation + the N₃=0 shared-floor empty-Fock fixed point), which does NOT depend on the area-clock outcome and stands either way. `mack-cosmic-bridge` writes no S106 falsifier-surface row (cross-wave constraint 7).

**Substrate-first framing.** The substrate IS the frozen GGE relic; σ_t^{ω'_z} is the Hawking-dressed relic's OWN thermal-time flow (gate 2a). G_τ = d/dτ on the spectral-action moment family {a_0, a_2, a_4} of D_K(τ) is the GEOMETRIC exflation-transit generator — it reads how the area-moment a_2 (= the Einstein-Hilbert/area Seeley-DeWitt coefficient, kernel 1/λ²) changes as the internal geometry deforms. The direction flows `D_K spectrum → a_2 area moment → G_τ`, compared against the 2a σ_t^{ω'_z} — NEVER inverted; the area-clock is read FROM the spectral-action grading, never as a flow IN a container-horizon. The −1 sign IS the substrate's own second-law co-orientation; the op-norm gap (1.163407 > 1e-3) is the substrate saying its geometric area-flow and its Hawking-dressed thermal-time flow are co-directed but **not the same operator** — a structural fact about the spectral triple, not a measurement against an external clock.

---

### §W2-3. S106-CDGM-SPACING-CROSS-BLOCK (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S106-CDGM-SPACING-CROSS-BLOCK`
**Trigger**: `[AUDIT]`
**Classification**: **PARTICLE** (CdGM bound-state ladder spacing — the representation-theoretic content of D_K in the B3 horizon-core sector)
**Agent**: `volovik-superfluid-universe-theorist`
**Dispatch condition**: INDEPENDENT — NO gating on 2a/2b; ran unconditionally. INFO-class by construction (the verdict is the invariant-vs-accident characterization, not a PASS/FAIL physics bar).
**Hypothesis**: the CdGM horizon-core ladder-spacing ω_0 (E_n = (n+1/2)ω_0) is a cross-block invariant surviving the χ: A_K → M₂(ℂ) projection across (0,0)+(1,0)+(0,1)+(1,1) — vs a within-block accident — measured by the per-block spacing relative variance against var_threshold = 1e-2.
**Plan reference**: `sessions/session-plan/session-106-plan-w2.md` §W2-3 (per-block B3 spectra from W2-2 per_block_json, rigid-ladder baseline Var=0, relative-variance metric).

**Substrate framing**: The substrate IS the frozen GGE relic; its horizon-core (B3) sector carries the CdGM bound-state ladder — the representation-theoretic content of D_K projected to the horizon-core. The direction of explanation flows `D_K spectrum (named blocks, L_max=10) → BDI/N₃=0 class → CdGM bound-state ladder E_n = (n+1/2)ω_0 (Volovik Paper 05 Eq.60/61) → the +1/2 minigap E_0 = ω_0/2 → the per-block ladder spacing`. The CdGM ladder is read FROM the D_K spectrum, NEVER as a ladder IN a container-horizon. This gate asks whether the equal-spacing ω_0 is a property of the horizon-core sector ACROSS the named (p,q) blocks (cross-block invariant under χ) or an accident of one block — a property of the SURVIVING co-monotone-plus-shared-floor bridge (the GEM-workshop floor result), independent of the ω'_z disposition.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-106/s106_cdgm_spacing_cross_block.py` — present; `from canonical_constants import` ✓, `print_verdict_payload` ✓ (grep-confirmed, see Completion-Checklist below).
- `computations/session-106/s106_cdgm_spacing_cross_block.npz` — present (R1/R2/R0 per-block arrays, E0_per_block, per_block_B3_json, recon_match_json, diag_sectors_json, drift_note).
- `computations/session-106/s106_cdgm_spacing_cross_block.png` — present (left: per-block B3 CdGM levels with minigap floor; right: cross-block ω_0 R1/R2 bars vs threshold).
- Verdict line in `computations/session-106/s106_gate_verdicts.txt` matching `^S106-CDGM-SPACING-CROSS-BLOCK:.* audit_sha256=[a-f0-9]{64}` — present; dual-SHA companion row present; NO 3-tuple ([AUDIT] characterization, `schema_v2_3tuple_required: false`); 2 extra companion rows (ii.B drift-note + cross-sector diagnostic).
- `audit_sha256 = 90c7eb8a41185b782ac5f7c6cffed54cc402bdb502192fd85b122e9b4f03b7a1`
- `content_sha256 = 131fca2e782c5a4a4ae27ae681f5bc7becb219f5ed186b8760568c533d882b29`

**MCP Pre-Compute Audit** (queries executed before writing the script):
- `search_knowledge("CdGM ladder spacing minigap cross-block invariant horizon-core B3")` → no prior CdGM cross-block result; only the plan-w2 equation `E_n=(n+1/2)ω_0` is indexed; related: theorem K12 (S105) "§VII.BZ BDI Horizon-Faithfulness Protection: CdGM +1/2 minigap = bosonic Wightman floor, clause (c) JOINT"; S32 "particle-hole matrix elements vanish for REAL reps (B1=trivial, B3=SU(2) adjoint)". NOT PRE-CLOSED — this is a NEW characterization.
- `trace_entity("CdGM ladder spacing")` → single hit (the plan-w2 equation eq_7333); no prior verdict or theorem on cross-block ω_0 invariance.
- `get_constant("Delta_B3")` → 0.176 (M_KK units, S38; B3-sector pairing gap, NOMINALLY the doubled-gap). Confirms the rigid-ladder gap input.

**Verdict**: **INFO** (INFO-class by construction — the workshop's own pre-registration; the verdict carries the per-block spacing table + cross-block relative variance + invariant-vs-accident classification).

`value='omega0_R1(2E0)_relvar=3.2408e-04_CROSS-BLOCK-INVARIANT;omega0_R2(med_dE)_relvar=2.8290e-02_WITHIN-BLOCK-ACCIDENT;thr=0.01;minigap_invariant=True;upper_spacing_invariant=False;recon_match=True;drift=s84cache_per_mode'`

**Results**:

*Numbers first.* The B3 horizon-core level spectrum was reconstructed per named block exactly as S105 W2-2 built it: `E_a = √(ξ_a² + Δ_B3²)`, `ξ_a = |λ_a| − lam_horizon`, `lam_horizon = 0.8197411120665` (W2-2 interp (i), the global min |λ| over named blocks), `Δ_B3 = 0.176`. The reconstruction reproduces `per_block_json`'s `E_min`/`E_max` on all 4 blocks bit-for-bit (`recon_match = True` on every block) — confirming the per-mode level source is faithful to W2-2.

Per-block CdGM ladder, B3 sector (unique levels, degeneracy collapsed):

| Block (p,q) | n_levels | E_0 (minigap) | ω_0^R1 = 2·E_0 | ω_0^R2 = median ΔE | lstsq slope | max\|resid\| |
|:-----------|:--------:|:-------------:|:--------------:|:------------------:|:-----------:|:-----------:|
| (0,0) | 3 | 0.176000 | 0.352000 | 0.028167 | 0.028167 | 0.017555 |
| (1,0) | 11 | 0.176740 | 0.353479 | 0.041573 | 0.031981 | 0.059171 |
| (0,1) | 11 | 0.176740 | 0.353479 | 0.041573 | 0.031981 | 0.059171 |
| (1,1) | 19 | 0.183875 | 0.367749 | 0.031417 | 0.029349 | 0.102895 |

Two distinct substrate-IS readings of ω_0 give OPPOSITE cross-block verdicts (relative variance metric `Var_pq[ω_0]/⟨ω_0⟩²`, intensive/block-count-independent, vs threshold 1e-2):

| Reading | ω_0 definition | per-block | mean | spread (max−min) | rel. variance | classification |
|:--------|:---------------|:----------|:----:|:----------------:|:-------------:|:--------------:|
| **R1** (rigid CdGM, MEASURED) | 2·E_0 (doubled minigap) | [0.352, 0.3535, 0.3535, 0.3677] | 0.356677 | 0.015749 | **3.2408e-04** | **CROSS-BLOCK-INVARIANT** (30× inside thr) |
| **R2** (literal `spacing_definition_pin`) | median consecutive ΔE | [0.0282, 0.0416, 0.0416, 0.0314] | 0.035682 | 0.013406 | **2.8290e-02** | **WITHIN-BLOCK-ACCIDENT** (2.8× over thr) |
| R0 (input-constant gap, TAUTOLOGY) | `per_block_json` `gap` field | [0.176, 0.176, 0.176, 0.176] | 0.176 | 0.0 | 0.0 | (tautological — see below) |

**Rigid-ladder baseline correction (substitution-chain departure).** The plan's substitution-chain Step 1–3 reads `ω_0 = gap = 0.176 → Var = 0 EXACTLY`, "verified at plan-freeze: gap = 0.176 identical across all 4 named blocks." That plan-freeze check is on the `per_block_json` `gap` field — but the W2-2 script set `gap := Δ_B3` (the *canonical pairing-gap input constant*, line 343–345 `per_block[...]= dict(gap=Dg, ...)` with `Dg = Δ_B3 = 0.176`), NOT a measured spectral spacing. So R0's variance-0 is a constant-reuse tautology, not a measurement of ladder rigidity. The MEASURED rigid-ladder quantity is the doubled CdGM minigap `2·E_0` (R1), where `E_0 = min BdG level per block`. R1 is NOT identically 0.176 across blocks: `E_0 = √(ξ_floor² + Δ_B3²)` equals exactly Δ_B3 only for (0,0) (which DEFINES lam_horizon, so ξ_floor = 0); higher blocks have `|λ|_min > lam_horizon ⇒ ξ_floor > 0 ⇒ E_0 > Δ_B3`. The measured R1 minigap is nonetheless a tight cross-block invariant (relvar 3.24e-04, 30× inside threshold).

**The dissociation finding (the substrate-physics content).** R1 (the BDI/N₃=0-protected CdGM +1/2 minigap, theorem K12 S105: "CdGM +1/2 minigap = bosonic Wightman floor, clause (c) JOINT") is a **cross-block invariant** surviving χ: A_K → M₂(ℂ). R2 (the upper-level consecutive spacing — the rank-≥3-in-sector level structure) is a **within-block accident** — it tracks each (p,q) block's Peter-Weyl multiplicity/normal-state dispersion, not a rigid CdGM ladder (the per-block `lstsq E_n = (n+1/2)ω_0` fit has max\|resid\| growing 0.018 → 0.103 from (0,0) to (1,1), and the slope ω_0 wanders 0.0282 → 0.0320 → 0.0293). The two readings cannot both be the cross-block invariant: **the rigidity that survives χ is the MINIGAP, not the upper-level spacing.** This sharpens the surviving co-monotone-plus-shared-floor bridge's "rank-≥3-in-sector ladder-spacing" clause: it holds cross-block at the protected-minigap level (the SHARED-FLOOR structural feature), but the full equal-spaced-ladder strengthening is a within-sector, block-specific claim — NOT a cross-block invariant.

**Cross-sector diagnostic (NON-GATED).** The minigap-based `2·E_0` cross-block relative variance is INVARIANT for all three BdG sectors: B3 = 3.241e-04, BCS = 7.123e-06, B2 = 1.160e-06. The smaller the gap, the larger the (still-invariant) variance — because `ξ/Δ` grows as Δ shrinks, so the floor-mode `ξ_floor² ` perturbation to `E_0 = √(ξ²+Δ²)` is a larger fractional shift for the small B3 gap. This confirms the minigap-rigidity result is robust across the named-block structure, not a B3-specific artifact.

4-tuple: `(value=<above>, scheme=FW, convention=CDGM-LADDER-SPACING-CROSS-BLOCK;B3-HORIZON-CORE-SECTOR;CHI-PROJECTION-OPNORM-LEVEL, L_max=10)`.

**Input-path drift (recorded per `substrate-first-canonical-sourcing.md §(ii.B)`).** The plan §W2-3 `input_files` block lists ONLY `s105_w2_2_omega_faithful_normal.npz`. But that npz's `per_block_json` carries per-block SUMMARY statistics (gap, f_min/max, K_abs_max, E_min, E_max, n_modes) — NOT the per-mode level set the spacing extraction requires. The per-mode `|λ_a|` lives in the S84 master cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7…`, the SAME source S105 W2-2 used to BUILD per_block_json via `load_horizon_spectrum()`). The script resolves to the real per-mode source, verifies `lam_horizon` reconstructed from the S84 cache matches the W2-2 field bit-for-bit, cross-checks the reconstructed E_min/E_max against per_block_json (`recon_all_ok = True`), and folds the S84 cache SHA into the audit closure. The drift is documented in the verdict `value` string (`drift=s84cache_per_mode`) and an extra companion row. This matches the orchestrator's input-path note (a sister W1 gate hit the same _shared/ vs session-84/ resolution).

**Completion-Checklist grep confirmation**:
```
$ grep -E "from canonical_constants import|print_verdict_payload" computations/session-106/s106_cdgm_spacing_cross_block.py
from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
from canonical_constants import Delta_B2, Delta_B3, Delta_BCS, tau_fold
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
    print_verdict_payload(verdict, value, audit_sha, content_sha,
$ grep -E "^S106-CDGM-SPACING-CROSS-BLOCK:.* audit_sha256=[a-f0-9]{64}" computations/session-106/s106_gate_verdicts.txt
S106-CDGM-SPACING-CROSS-BLOCK: INFO -- value='...' ... audit_sha256=90c7eb8a41185b782ac5f7c6cffed54cc402bdb502192fd85b122e9b4f03b7a1 content_sha256=131fca2e782c5a4a4ae27ae681f5bc7becb219f5ed186b8760568c533d882b29 schema_version=S84+
```

---

## Wave 2 Synthesis (team-lead)

(Written after all gates complete. Structure: `sessions/session-84/session-84-w1-workingpaper.md:1040–1095`. Cover: 2a faithful-relocation verdict; 2b area-clock CANDIDATE / mechanical-closure disposition + dual-prior posterior; 2c cross-block invariant-vs-accident characterization; the surviving co-monotone-plus-shared-floor bridge as the floor result regardless of branch.)

## Carry-Forward Computations

(One `### {CF-ID} — {title}` per genuine future-work item with a 4-field-spec table (What / Inputs / Gate / Effort). Candidate sources pre-flagged by the plan: a FUTURE ω'_z geometric-area-clock 5-anatomy + 3-level cross-pillar registration on a 2b PASS (Element-2 OPERATOR-EXPRESSION lab-IN observable unspecified this session); the EMr3-2 3He-B vortex-core lab-side companion seed (capacity-deferred). Empty IFF all wave outcomes close in-session.)

## Constraint-Map Updates

(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason.)

## Files Produced

(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)
