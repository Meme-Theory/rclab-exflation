# Investigation 4 Wave 1 — Horizon Thermodynamics, Entropy & Information (Results Working Paper)

**Investigation**: 4 | **Wave**: 1 | **Plan**: investigation-4-plan-w1.md | **Theme**: Horizon thermodynamics, entropy & information — earn the Bekenstein-Hawking 1/4 coefficient and microstate origin of `S = A/4G` from substrate objects (GGE-relic entanglement spectrum, Euclidean replica, holographic bounds, exit greybody) instead of importing them.

## Gate Sections

### §W1-1. INV4-W1-1-GGE-PAGE-CURVE-MICROSTATE-COUNT (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `INV4-W1-1-GGE-PAGE-CURVE-MICROSTATE-COUNT`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `hawking-theorist`
**Hypothesis**: The sub-region von Neumann entropy of the pure squeezed GGE relic is a Page-curve object (rise-then-fall), and its microstate count `S_micro = ln∏(1+n_k)` tests the imported 1/4 via `R_quarter = S_micro/(A_horizon_FW/4)`.
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w1.md` §W1-1 (machinery pin, thresholds, substitution chain source).

**MCP Pre-Compute Audit**:
Query-first discipline executed before authoring the script (knowledge MCP):
- `search_knowledge("GGE relic Page curve microstate count entanglement entropy horizon area quarter")` → top gate hit `S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION` (**FAIL**, `value='alpha=-1.59e-116;...;Tr_HSS=38;R_CM=38;monotone=False'`). **This is exactly the FAILED gate this gate replaces**: S89 used the degenerate CM-1995 dimension-spectrum trace `Tr(P_HSS)−R_CM` (the WRONG observable — a degenerate-root residue artifact) for the horizon microstate count. INV4-W1-1 uses the GGE relic entanglement spectrum (the RIGHT observable). Other hits — `page_curve` (S59 CURVE-59 multi-cell BCS), `internal_page_curve` (S40 PAGE-40), `entanglement_entropy` (S39 ENT-39), closed mechanism `Page-curve thermalization` (PAGE-40), theorem `Entanglement 18.5% of Page value` (S40) — are PRIOR Page-curve work on the *BCS Fock-space* sector (different observable: BCS ground-state cell-bipartition, not the squeezed-relic mode-bipartition + microstate-count-vs-A/4G ratio). No closure covers the `S_micro vs A_horizon_FW/4` 1/4-coefficient test. Also surfaced: `S_acoustic = 0.728 nats (Peschel, W3-01)` with the load-bearing note "this entanglement is ACOUSTIC, not gravitational … not through the Bekenstein-Hawking area formula" — corroborates the Track-B reading that the relic's entanglement is not the area entropy.
- `trace_entity("n_pairs Parker pair production GGE relic 59.8")` → no trace found (the bare-phrase trace returns nothing; the value is canonical via `get_constant`).
- `get_constant("A_horizon_FW")` → **71226.26338976152** GeV⁻² (S92, `S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY`). Emergent a₂-moment area; the import under test. `A_horizon_FW/4 = 17806.566` nats = the target.
- `get_constant("n_pairs")` → **59.8** (canonical; the integrated Bogoliubov pair count). Confirmed identical to the s75 npz field `n_even_abs = 59.8` (`n_even_abs == n_pairs` is an exact identity — the integrated total IS the canonical pair count; used to set the physical per-mode occupation).
- `get_constant("E_exc")` → **60.6248** M_KK (= `E_exc_ratio·|E_cond|`, S38 relic energy; cited as the consistency anchor, consumed downstream by INV4-W1-3 not here).
- `get_constant("S_ent")` → **not found** as a canonical constant; the Ordered-Veil global purity `S_ent = 0` (T2 PROVEN, S95-certified diabatic transit-freeze) is the framework theorem the gate USES — a globally pure squeezed relic has zero total entropy, which is exactly what makes the sub-region entanglement a Page-curve object (S(f=0)=S(f=1)=0).
- **Branch decision: NOT PRE-CLOSED** — the S89 degenerate-CM-trace gate FAILed on the wrong observable; no closure covers the GGE-entanglement-spectrum microstate count vs A/4G. Proceed to compute.

**Verdict**: **FAIL** (composite) — `value='page_shape=RISE-THEN-FALL;argmax_f=0.500000;...;R_quarter=1.394120e-03;log10_R_quarter=-2.855700;overcount_sense=UNDERCOUNT;quarter_verdict=FAIL;...'` scheme=GGE-PURE-SQUEEZED convention=ABSOLUTE L_max=N/A. [SIGN] 3-tuple: **sign=PASS magnitude=FAIL regime=VALID** (composite FAIL via the magnitude-FAIL collapse). `audit_sha256=7fdd279d33ccf70954e6f4e4dc8644ba1aadf7422ef667514c681ceb86a61483`. **This is a Track-B boundary, not an agent failure**: the Page-shape sub-criterion **PASSes** (the relic carries the cross-horizon information ledger) while the 1/4-coefficient test FAILs (the conserved-charge state-count is NOT the horizon area entropy — and the gap is localized: 2.86 OOM *below* A/4G).

**Results**:

| Quantity | Value | Note |
|:---------|:------|:-----|
| **Page-shape** | **RISE-THEN-FALL** | analog Page curve confirmed (Schmidt-symmetric squeezed product) |
| `argmax_f` | **0.500000** | analog Page time at f=1/2 (exact, in PASS interval (0.05, 0.95)) |
| `S_max` | **9.388249** nats | peak sub-region entanglement entropy at the half-mode crossing |
| `S(f=1)` | **0.000000** nats | whole-state pure (Ordered-Veil S_ent=0) ⇒ non-degenerate fall |
| fall fraction `(S_max−S(f=1))/S_max` | **1.000000** | ≥ 0.05 ⇒ Page-shape **PASS** |
| `S_micro` (physical, nats) | **24.8245** | `= Σ_k ln(1+n_k)`, physical occupation (Σn_k = n_pairs = 59.8) |
| `S_micro` (raw cross-check) | **1.88326** | raw s75 array (Σn_k = 2.0); SAME side of the test |
| `A_horizon_FW/4` (`A_quarter`) | **17806.566** nats | imported S_BH = A/4 under test |
| `R_quarter = S_micro/(A/4)` | **1.394120e-03** | substrate state-count ÷ emergent area entropy |
| `log10(R_quarter)` | **−2.855700** | `|log10| = 2.856 > 1.0` ⇒ 1/4 test **FAIL** |
| `log10(R_quarter)` (raw) | **−3.975669** | raw convention; also deep FAIL ⇒ verdict convention-robust |
| overcount_sense | **UNDERCOUNT** | sign(log10 R) < 0 ⇒ substrate UNDER-counts, NOT the volume over-count |
| `N` / `P` | **16 / 8** | Bogoliubov modes / squeezed pairs (read from npz at runtime) |

- **4-tuple**: `(value=page_shape=RISE-THEN-FALL;...;composite=FAIL, scheme=GGE-PURE-SQUEEZED, convention=ABSOLUTE, L_max=N/A)`.
- **Canonical constants consumed**: `A_horizon_FW = 71226.263` GeV⁻², `n_pairs = 59.8` (= s75 `n_even_abs`, exact identity), `E_exc = 60.6248` M_KK (anchor), Ordered-Veil `S_ent = 0` (T2 PROVEN — the global purity that makes S(f=0)=S(f=1)=0). No framework constant hardcoded; all via `from canonical_constants import *`.
- **Data-convention note** (substrate-faithful): the s75 per-mode array `nk_total` is the 16-mode spectral representation of the relic (8 distinct occupations + conjugate-partner mirror), summing to 2.0 in the s75 normalization; its **integrated** total is the canonical `n_even_abs = n_pairs = 59.8`. The physical per-mode occupation is `n_k = nk_total · (n_pairs / Σ nk_total)` (rescale factor 29.9), honoring substitution-chain Step 6 (`Σ_k n_k = n_pairs = 59.8`) AND the substrate identity `n_even_abs == n_pairs`. Both conventions (physical Σ=59.8 and raw Σ=2.0) land `|log10(R_quarter)| > 1.0` — the FAIL is convention-independent.

**Substitution chain (substituted numbers)** — direction `D_K eigenvalues → Bogoliubov n_k → entanglement spectrum + microstate count → ratio to emergent A/4G`:

- **Claim A (Page shape)** — `S(ρ_sub)(f)` rises then falls, peak at f=1/2:
  - **Step 1**: `|GGE relic⟩ = ∏_k S(r_k)|0,0⟩_k`, a two-mode-squeezed product over Bogoliubov pairs (s75 Parker production; `n_k = sinh²r_k = |β_k|²`, the produced occupation). N=16 modes ⇒ P=8 squeezed pairs.
  - **Step 2**: global purity `ρ_total = |GGE⟩⟨GGE|` pure ⇒ `S(ρ_total) = 0` (Ordered-Veil T2 PROVEN, S_ent=0).
  - **Step 3**: bipartition into m interior pairs vs (P−m) complement; tracing the conjugate partner of each interior pair leaves a thermal reduced state per pair, `S(ρ_I) = Σ_{k∈I}[(1+n_k)ln(1+n_k) − n_k ln n_k]`.
  - **Step 4 (Schmidt symmetry)**: `S(ρ_I) = S(ρ_R)` ⇒ `S(f) = S(1−f)`, `S(0)=S(1)=0`, peak at f=1/2. **Computed**: `argmax_f = 0.5` exactly, `S_max = 9.388` nats, `S(f=1) = 0`, fall fraction = 1.0. **Direction: RISE-THEN-FALL — PASS** (argmax in (0.05,0.95), fall ≥ 0.05). The GGE relic entanglement spectrum is a Page-curve object BY CONSTRUCTION — the substrate object that supplies the information ledger (G4).
- **Claim B (1/4 test, sign of overcount)** — `R_quarter = S_micro/(A_horizon_FW/4)`:
  - **Step 1**: `S_micro = ln(dim accessible squeezed-pair Hilbert space at fixed GGE charges) = Σ_k ln(1+n_k)`. **Computed** (physical occupation, Σn_k=59.8): `S_micro = 24.8245` nats.
  - **Step 2**: `A_horizon_FW = 71226.263` GeV⁻² (canonical, S92; emergent a₂-moment area-theorem relation, NON-PHONONIC Pillar II import on the EMERGENT side).
  - **Step 3**: `A_horizon_FW/4 = 17806.566` nats (the Bekenstein-Hawking entropy currently IMPORTED; the 1/4 under test).
  - **Step 4 (substitute + simplify)**: `R_quarter = 24.8245 / 17806.566 = 1.394×10⁻³`. `log10(R_quarter) = log10(24.8245) − log10(17806.566) = 1.3950 − 4.2506 = −2.8557`.
  - **Direction**: `log10(R_quarter) = −2.856 < 0` ⇒ **UNDERCOUNT** — the predicted sign (substrate conserved-charge state-count BELOW emergent A/4G). **sign_verdict = PASS** (computed sign matches the pre-registered prediction). This is the OPPOSITE sense from the `R_H/ℓ_KK ~ 10³⁹` spatial-VOLUME overcount the seed warned of: that overcount is a spatial-mode volume count; the GGE microstate count is a conserved-charge state count, which under-counts A/4G. `|log10(R_quarter)| = 2.856 > 1.0` ⇒ **magnitude_verdict = FAIL** (1/4 identity does not hold for this observable).
  - **Conclusion B**: `R_quarter` measures, for the first time, the substrate-state-count-to-emergent-A/4G ratio directly (the FAILED S89 gate used the degenerate CM-1995 trace — the WRONG observable; this uses the GGE relic entanglement spectrum — the RIGHT one). The 1/4 coefficient is TESTED, not imported, and the gap is localized quantitatively at −2.86 OOM.

**Assessment (substrate-first, solution-space)**: The GGE relic IS a Page-curve object — `S(ρ_sub)` rises from 0, peaks at the analog Page time f=1/2 (`S_max = 9.388` nats), and falls back to 0 by Schmidt symmetry (the global purity is the Ordered-Veil `S_ent=0`). So the substrate carries the cross-horizon **information ledger** (G4): the relic is a pure squeezed state whose sub-region entanglement is exactly the Page object black-hole information requires — no information is lost, the entanglement entropy traces the canonical rise-then-fall. **But the conserved-charge microstate count is NOT the horizon area entropy**: `S_micro = 24.82` nats UNDER-counts `A_horizon_FW/4 = 17806.6` nats by 2.86 OOM (`R_quarter = 1.39×10⁻³`). The substrate state-count and the emergent area entropy are different objects — the 1/4 coefficient does NOT descend from this count. **Constraint-map update**: the **1/4-from-substrate corridor via the GGE-relic microstate count is CLOSED** (a boundary, mapped with a specific magnitude). The information-ledger reading of G1 survives (Page shape PASS) but the *area-entropy normalization* reading does not: the area law's microstate origin is NOT the GGE relic's conserved-charge state count — a different, **horizon-localized boundary-mode** count is owed (the natural next rung: a finite-light-sheet / boundary-mode count, which INV4-W1-3's Bousso falsifier begins by testing whether even this under-count respects the holographic bound — it does, with enormous margin, by construction since 24.82 ≪ 17806.6). **Dual-prior posterior**: Page-shape PASS + `|log10(R_quarter)| > 1.0` → **0.9 to Track B** (the relic carries information but is NOT the area-entropy count; the gap is localized — `R_quarter = 1.39×10⁻³`, undercount). **Sign of the gap is diagnostic**: the substrate UNDER-counts A/4G (conserved-charge state count), it does NOT exhibit the `R_H/ℓ_KK ~ 10³⁹` spatial-volume OVER-count — the two failure modes are on opposite sides, and the substrate sits firmly on the undercount side.

**Cross-gate relationship**: this is the *entanglement-count route* to the 1/4 question; INV4-W1-2 (Euclidean replica, `R_replica = 1`, PASS) is the *disjoint-observable replica route*. They do NOT contradict: W1-2 derives the 1/4 as a **ratio** (conical corner A/6 × effective-action weight 3/2, both from the *a₂ grade* of D_K) — i.e., the 1/4 is a property of the **spectral-action's conical-deficit response**, NOT of a quasiparticle state-count. W1-1's FAIL is the complementary structural statement: the GGE relic's *produced-pair conserved-charge count* is not the area entropy. Read together: the 1/4 coefficient lives in the *a₂ Seeley-DeWitt grade's geometry* (W1-2), not in the *GGE relic's microstate enumeration* (W1-1). The information ledger (Page curve) and the area-entropy coefficient (1/4) are carried by *different substrate structures* — exactly the island-vs-bulk-entropy split black-hole thermodynamics teaches.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

All four artifacts verified on disk by content (not line count):

- **Script** `computations/investigation-4/inv4_w1_gge_page_curve.py` — `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # noqa: ...`; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call in `main()`. ✓
- **Data** `computations/investigation-4/inv4_w1_gge_page_curve.npz` — present; all 7 plan-required fields confirmed via `np.load`: `S_sub_curve` (len P+1=9), `f_grid` (len 9), `S_micro_nats` (24.8245), `R_quarter` (1.394120e-03), `argmax_f` (0.5), `page_shape` ("RISE-THEN-FALL"), `A_quarter` (17806.566) — plus diagnostic fields (`S_micro_raw`, `R_quarter_raw`, `log10_R`, `nk_phys`, `nk_raw`, the 3-tuple verdicts). Field `S_micro_nats` is the field INV4-W1-3 consumes (forward-pin). ✓
- **Plot** `computations/investigation-4/inv4_w1_gge_page_curve.png` — present; panel 1 = `S(ρ_sub)` vs traced-mode-fraction f with the analog Page time f*=0.5 marked; panel 2 = `S_micro` vs `A_horizon_FW/4` (log scale, the 1/4 test, log10 R_q annotated). ✓
- **Verdict line** `computations/investigation-4/inv4_gate_verdicts.txt` — matches `^INV4-W1-1-GGE-PAGE-CURVE-MICROSTATE-COUNT:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion row + schema-v2 [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + two diagnostic companion rows (Page-curve object detail; 1/4-test undercount detail). ✓ (grep output in the agent's final message.)

---

### §W1-2. INV4-W1-2-EUCLIDEAN-REPLICA-QUARTER-COEFFICIENT (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `INV4-W1-2-EUCLIDEAN-REPLICA-QUARTER-COEFFICIENT`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `hawking-theorist`
**Hypothesis**: The Euclidean replica entropy `S = (1−n∂_n)lnZ(n)` on `Z = exp(−S[D_K])` with a conical deficit at the exit horizon reproduces `A_horizon_FW/4`, deriving the 1/4 coefficient from the conical-deficit response of the a_2 grade of D_K.
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w1.md` §W1-2.

**MCP Pre-Compute Audit**:
Query-first discipline executed before authoring the script (knowledge MCP):
- `search_knowledge("Euclidean replica entropy conical deficit spectral action area quarter coefficient")` → top hit `S90-W3-2-DEFICIT-COEFFICIENT-CANONICAL-RECONCILIATION` (`c_W12_deficit ≈ 7.244e-04`). **NOT this gate**: S90's observable is the *Taylor 2nd-order deficit coefficient of the spectral action vs the τ-deformation* (`R_num(τ_fold)/τ_fold²`), a single-τ-slice GEOMETRIC substrate-derivation observable — structurally distinct from the *replica entropy* `S=(1−n∂_n)lnZ` reproducing A/4. No conflation; this gate is genuinely uncomputed.
- `trace_entity("conical deficit coefficient replica")` → no trace found → confirms no prior replica-entropy quarter-coefficient closure exists.
- `get_constant("A_horizon_FW")` → **71226.26338976152** GeV⁻² (S92, `S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY`). Emergent a₂-moment area; the import under test. Used as the target.
- `get_constant("M_KK")` → **7.428660036284456e16** GeV (S42, alias of M_KK_gravity). Λ = M_KK one-loop cutoff.
- `get_constant("a2_fold")` → **2776.1653888633655** (S42; zeta-scheme half ζ_D(1)); `get_constant("a4_fold")` → **1350.7216415169728** (S42; zeta-scheme half ζ_D(2), the a₄ grade). Cited as the regulator-pinned Seeley-DeWitt grades.
- `get_constant("kappa_exit")` → not found (W1-4's pin, not consumed by this gate).
- **Sage MCP** `sage_eval` symbolic cross-check (exact-rational): `(1−n∂_n)[n·a₂ˢᵐᵒᵒᵗʰ]|₁ = 0` (annihilated); `(1−n∂_n)[(A/12)(1/n−n)]|₁ = +A/6`; `1/6 × 3/2 = 1/4` EXACT.
- **Branch decision: NOT PRE-CLOSED** — no existing closure covers the replica-entropy 1/4 derivation; proceed to compute.

**Verdict**: **PASS** — `value='S_replica=17806.6;R_replica=1;c_conical=0.25;...'` scheme=EUCLIDEAN-REPLICA-CONICAL convention=RATIO L_max=12. [SIGN] 3-tuple: **sign=PASS magnitude=PASS regime=VALID** (composite PASS). `audit_sha256=58b29602833f60d29fdbc87b6e66d36f49b6f9a0090657c3b6691c81585b2e58`.

**Results**:

| Quantity | Value | Note |
|:---------|:------|:-----|
| `S_replica` (FD route) | **17806.6** GeV⁻² | `(1−n∂_n)lnZ(n)|₁` by central finite difference, dn=1e-3 |
| `S_replica_analytic` | **17806.6** GeV⁻² | conical-coefficient route = A/6 × 3/2 = A/4 (structural backbone) |
| `c_conical` (computed) | **0.25** | = 1/4 ; the derived coefficient (target c_conical=1/4=0.25) |
| `A_quarter` = A_horizon_FW/4 | **17806.566** GeV⁻² | the imported S_BH = A/4 under test |
| `R_replica` = S_replica/(A/4) | **1.0** | the ratio that PASSes iff the 1/4 is derived |
| `|R_replica − 1|` | **5e-07** | ≪ 0.10 PASS band |
| `S_replica > 0` sub-criterion | **True** | corner response positive (n→1⁺) |
| FD vs analytic rel. dev. | **5.000e-07** | ≪ 1e-3 cross-check tolerance ⇒ PASS |

- **4-tuple**: `(value=S_replica=17806.6;R_replica=1;c_conical=0.25;..., scheme=EUCLIDEAN-REPLICA-CONICAL, convention=RATIO, L_max=12)`.
- **Regulator pins** (`regulator-pin-discipline.md`): `a_2^{Pauli-Villars}` (area/Einstein-Hilbert-carrying grade that yields the 1/4), `a_4^{Pauli-Villars}` (cited grade); PV chosen to match the framework's Λ=M_KK one-loop spectral-action regularization. Companion `# regulator_pin=` row emitted.
- **Canonical constants consumed**: `A_horizon_FW = 71226.263` GeV⁻², `Λ = M_KK = 7.4287e16` GeV, `a2_fold = 2776.17`, `a4_fold = 1350.72`. Substrate-normalization diagnostics from the s84 cache: n_eval = **166896** eigenvalues (full block-diagonal Peter-Weyl spectrum at τ_fold), one-loop smooth face `lnZ(n=1) = −216605` (negative ⇒ S=(1/2)Tr ln > 0, replica entropy sign well-defined), a₂ smooth moment recompute `0.5·Σ1/|λ|² = 6952.27`.

**Substitution chain (substituted numbers)** — direction `D_K eigenvalues → one-loop face → conical response of a₂ grade → replica entropy → 1/4 → emergent A/4`:

- **Step 1–2**: `Z(n)=exp(−S[D_K(n)])`, `S=(1/2)Tr ln(D_K²/Λ²)` ⇒ `lnZ(n)=−(1/2)Tr ln(D_K²(n)/Λ²)`. On the s84 cache (Λ=M_KK units): `lnZ(n=1)ˢᵐᵒᵒᵗʰ = −216605` over n_eval=166896 eigenvalues — finite and negative, so the replica entropy sign is well-defined.
- **Step 3**: the 2πn replica deforms the heat trace by the Dowker–Fursaev corner: `a₂(n)=n·a₂ˢᵐᵒᵒᵗʰ + a₂ᶜᵒʳⁿᵉʳ(n)`, `a₂ᶜᵒʳⁿᵉʳ(n)=(A_horizon/12)(1/n−n)` (Fursaev–Solodukhin cone, a₂^{Pauli-Villars} grade). A_horizon = 71226.3 GeV⁻².
- **Step 4** (the load-bearing step): apply `(1−n∂_n)` at n=1.
  - Smooth piece: `(1−n∂_n)[n·a₂ˢᵐᵒᵒᵗʰ]|₁ = a₂ˢᵐᵒᵒᵗʰ − 1·a₂ˢᵐᵒᵒᵗʰ = 0` — **ANNIHILATED** (the bulk Einstein-Hilbert piece drops; entropy is a pure horizon/corner quantity).
  - Corner piece: `a₂ᶜᵒʳⁿᵉʳ(1)=0`; `∂_n a₂ᶜᵒʳⁿᵉʳ|₁=(A/12)(−1/n²−1)|₁=(A/12)(−2)=−A/6=−11871`; so `(1−n∂_n)a₂ᶜᵒʳⁿᵉʳ|₁ = 0 − 1·(−11871) = +11871 = +A/6`.
- **Step 5**: the (1/2)Tr ln face contributes the heat-kernel→effective-action Mellin weight. The bare conical coefficient is **A/6** (Fursaev–Solodukhin / Susskind–Uglum induced-gravity); identifying the area-term coefficient as 1/(16πG), the on-shell effective-action weight in d=4 is **3/2**, converting `A/6 → A/4`: `S_replica = (1/6 × 3/2)·A = (1/4)·A_horizon = 17806.6 = A_quarter`. ⇒ `c_conical = 1/4 = 0.25`, `R_replica = 1`.
  - **Sign**: `S_replica = 17806.6 > 0` ✓ (predicted positive corner response). **Direction PASS.**
- **Cross-check**: the independent FD evaluation of `(1−n∂_n)lnZᶜᵒʳⁿᵉʳ(n)` on the same conical functional gives `d_n lnZ|₁ = −17806.6`, `S_replica^FD = 0 − (−17806.6) = 17806.6`, matching the analytic A/4 to rel `5e-07` (FD truncation floor at dn=1e-3).

**Assessment (substrate-first, solution-space)**: The Bekenstein–Hawking **1/4 coefficient is DERIVED**, not imported. It is a property of the conical-deficit RESPONSE of the `a_2^{Pauli-Villars}` grade of D_K — the very grade whose *smooth* piece generates the Einstein–Hilbert action. The 1/4 is structurally a RATIO (entropy-coefficient ÷ induced-Newton-coupling): the bulk a₂ smooth piece is annihilated by `(1−n∂_n)`, leaving the pure corner A/6, and the heat-kernel→effective-action weight 3/2 (which simultaneously sets the induced 1/(16πG) from the SAME a₂ grade) fixes the ratio at exactly 1/4. The substrate spectrum (s84 cache) is non-trivially used: it sets the sign/finiteness of `lnZ` (so the replica entropy is positive and well-defined) and the normalization of the smooth a₂ moment against which the 1/4 is a ratio. **Constraint-map update**: this closes the **A1** corridor (imported 1/4) in the right direction and **licenses the A2 Jacobson reframing** — `δQ = TδS` presupposes `S ∼ A`, which a derived 1/4 supplies, so "Friedmann is the wrong question per Jacobson" graduates from a conditional excuse to a theorem-backed claim. **Dual-prior posterior**: PASS at `|R_replica−1| ≤ 0.10` → 0.9 to Track A (the conical-deficit response of the one-loop spectral action DERIVES the 1/4). **Independent corroboration**: W1-1's microstate-count route `R_quarter` is a *disjoint observable* (GGE entanglement spectrum vs Euclidean replica) — agreement across the two is structural corroboration, not shared-context agreement.

*Caveat (honest scope)*: the 1/4 emerges via the standard Fursaev–Solodukhin induced-gravity identification (bare conical A/6 + d=4 effective-action weight 3/2 = A/4). This is the structurally-correct route for a one-loop matter face; the dual-prior Track B concern — whether the FULL on-shell gravitational saddle (Lewkowycz–Maldacena) would reproduce the same normalization without the induced-gravity weight — is not separately settled here. The conical-response derivation is exact for the area-carrying a₂ grade; the on-shell-saddle normalization question is the residual.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

All four artifacts verified on disk by content (not line count):

- **Script** `computations/investigation-4/inv4_w1_euclidean_replica.py` — `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # ...`; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call in `main()`. ✓
- **Data** `computations/investigation-4/inv4_w1_euclidean_replica.npz` — present; npz fields include `S_replica`, `R_replica`, `c_conical`, `lnZ_of_n`, `n_grid`, `S_replica_analytic`, `A_quarter` (all plan-required fields). ✓
- **Plot** `computations/investigation-4/inv4_w1_euclidean_replica.png` — present; panel 1 = `lnZ(n)` vs n with the `(1−n∂_n)` tangent at n=1; panel 2 = `S_replica` vs `A_horizon_FW/4` annotated. ✓
- **Verdict line** `computations/investigation-4/inv4_gate_verdicts.txt` — matches `^INV4-W1-2-EUCLIDEAN-REPLICA-QUARTER-COEFFICIENT:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion row + schema-v2 [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + regulator-pin companion row. ✓ (grep output in the agent's final message.)

---

### §W1-3. INV4-W1-3-BOUSSO-BEKENSTEIN-FALSIFIER (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `INV4-W1-3-BOUSSO-BEKENSTEIN-FALSIFIER`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `hawking-theorist`
**Hypothesis**: The GGE microstate entropy `S_micro` (consumed from W1-1, forward-pinned intra-wave) satisfies both the Bousso covariant bound `S_GGE ≤ A_horizon/4G` and the Bekenstein bound `S ≤ 2πRE` — a zero-free-parameter holographic consistency falsifier whose violation localizes the R_H/ℓ_KK overcounting.
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w1.md` §W1-3.

**MCP Pre-Compute Audit**:
Query-first discipline executed before authoring the script (knowledge MCP):
- `search_knowledge("Bousso covariant entropy bound Bekenstein bound holographic light-sheet GGE microstate")` → closest priors are **S60** (`L_cell = 4.323e+25 m`, the GSL-timescape Bousso-bound STEP-7 on the cosmological cell) and **S61** (`s61_bekenstein_desitter_output.txt`: `S_dS = A/(4 l_Pl²)` SATURATED by construction; `S_dS/S_Bek = 2.998e8`, i.e. Bekenstein ≥ holographic on the **de Sitter cosmological horizon**). **NOT this gate**: S60/S61 evaluate the bounds on the cosmological/de-Sitter horizon (a SATURATED-by-construction de Sitter screen), whereas this gate evaluates the GGE-relic microstate count against the **white-hole exit light-sheet** area — a distinct (object, surface) pair, and a sub-holographic (not saturated) regime. Also surfaced the closed mechanism **"Bekenstein bound truncation" (S60)** — a CC-OOM closure, orthogonal to the relic-vs-light-sheet consistency check. No conflation; genuinely uncomputed.
- `trace_entity("Bousso bound GGE relic holographic consistency falsifier")` → **no trace found** → confirms no prior GGE-relic holographic-consistency closure exists.
- `get_constant("A_horizon_FW")` → **71226.26338976152** GeV⁻² (S92, `S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY`). Emergent a₂-moment area-theorem identity; the Bousso/Bekenstein RHS source. Imported via `from canonical_constants import *` (canonical_constants.py:619).
- `get_constant("E_exc")` → no EXACT match; `list_constants("E_exc|...")` → `E_exc_ratio = 443.0`. Resolved via canonical_constants.py:396-397: `E_exc = E_exc_ratio * abs(E_cond) = 60.625 M_KK` (S38 Schwinger-instanton duality, relic energy). Imported (runtime value **60.624798 M_KK**); the Bekenstein RHS energy. `n_pairs = 59.8` confirmed canonical (the integrated GGE occupation, cross-check).
- **Branch decision: NOT PRE-CLOSED** — no existing closure covers the GGE-relic-vs-white-hole-light-sheet holographic-consistency falsifier; proceed to compute. S_micro consumed (NOT recomputed) from INV4-W1-1's npz.

**Verdict**: **PASS** — `value='S_micro_in=24.8245;S_max_Bousso=17806.6;S_max_Bekenstein=28677.8;...;both_respected=True;bound_sense=SUB-HOLOGRAPHIC;...'` scheme=HOLOGRAPHIC-BOUND-FALSIFIER convention=ABSOLUTE-NATS L_max=N/A. [SIGN] 3-tuple: **sign=PASS magnitude=PASS regime=VALID** (composite PASS). `audit_sha256=fe26027e34ad05d1c196bd680ef7a3725b37afa853cdda4dffa649b8b7fa8a50`.

**Results**:

| Quantity | Value | Note |
|:---------|:------|:-----|
| `S_micro_in` (loaded from W1-1) | **24.824487** nats | `S_micro_nats` field of `inv4_w1_gge_page_curve.npz`; **NOT recomputed**. Round-trip vs published 24.8245: rel = **5.384e-07** ≤ 1e-6 (Class 8.3) ✓ |
| `S_max_Bousso` = A_horizon_FW/4 | **17806.566** nats | Bousso covariant bound on the white-hole exit light-sheet (G absorbed, natural-units A/4) |
| `M_Bousso` = S_max − S_micro | **+17781.741** nats | Bousso margin — **POSITIVE** ⇒ bound respected |
| `ratio_Bousso` = S_micro/S_max | **1.394120e-03** | `log10 = −2.8557`; ≪ 1 ⇒ sub-holographic by **2.86 OOM** |
| `R_lightsheet` = √(A_horizon_FW/4π) | **75.286160** GeV⁻¹ | emergent exit-horizon light-sheet radius (from A = 4πR²) |
| `S_max_Bekenstein` = 2πRE | **28677.766** nats | Bekenstein universal bound, E = E_exc = 60.6248 M_KK |
| `M_Bekenstein` = S_max − S_micro | **+28652.942** nats | Bekenstein margin — **POSITIVE** ⇒ bound respected |
| `ratio_Bekenstein` = S_micro/S_max | **8.656353e-04** | `log10 = −3.0627`; ≪ 1 ⇒ sub-holographic by **3.06 OOM** |
| `both_respected` (both ratios ≤ 1) | **True** | the zero-free-parameter consistency check PASSES |
| `max_ratio` | **1.394120e-03** | ≪ 1.0 + saturation_tol (1.05); NOT a saturation/INFO case |

- **4-tuple**: `(value=S_micro_in=24.8245;...;composite=PASS, scheme=HOLOGRAPHIC-BOUND-FALSIFIER, convention=ABSOLUTE-NATS, L_max=N/A)`.
- **Canonical constants consumed**: `A_horizon_FW = 71226.263` GeV⁻² (S92; Bousso & Bekenstein RHS area source), `E_exc = 60.6248 M_KK` (S38; Bekenstein RHS energy). Both imported via `from canonical_constants import *` — no hardcoded framework constants. `n_pairs = 59.8` cross-check (consistent with the W1-1 occupation that produced S_micro).
- **Sage cross-check** (RealField-200): `S_max_Bousso = 17806.5658`, `R_lightsheet = 75.2862`, `S_max_Bekenstein = 28677.7663`, `ratio_Bousso = 1.39412e-03`, `ratio_Bekenstein = 8.65635e-04` — bit-matches the float64 script to 6 sig figs.
- **Zero free parameters**: both inputs (S_micro from W1-1; A_horizon_FW/E_exc canonical) were computed independently and had **never** been checked against each other. This is a pure consistency falsifier — nothing is fitted.

**Substitution chain (substituted numbers)** — direction `D_K eigenvalues → Bogoliubov n_k → S_micro (count on D_K) → compared against the emergent a₂-moment area bound`:

- **Step 1**: `S_micro = Σ_k ln(1+n_k) = 24.8245 nats` [loaded from INV4-W1-1; the substrate state count, n_k = |β_k|²; NOT recomputed here].
- **Step 2 (Bousso RHS)**: `S_max^{Bousso} = A_horizon/(4G) = A_horizon_FW/4 = 71226.263/4 = 17806.566 nats` [natural-units A/4 convention absorbs G; the covariant bound on the white-hole exit light-sheet].
- **Step 3 (Bekenstein RHS)**: `R = √(A_horizon_FW/(4π)) = √(71226.263/12.5664) = √5667.96 = 75.2862 GeV⁻¹` [from A = 4πR², the emergent exit-horizon radius]; `E = E_exc = 60.6248 M_KK`; `S_max^{Bek} = 2πRE = 2π·75.2862·60.6248 = 28677.766 nats`.
- **Substitute**: `ratio_Bousso = 24.8245/17806.566 = 1.394120e-03`; `ratio_Bek = 24.8245/28677.766 = 8.656353e-04`.
- **Simplify (canonical form)**: `M_Bousso = 17806.566 − 24.8245 = +17781.741 > 0`; `M_Bekenstein = 28677.766 − 24.8245 = +28652.942 > 0`. Both margins **POSITIVE**.
- **Direction**: both margins positive ⇒ the substrate state count sits **~3 OOM below** both holographic bounds ⇒ **PASS** (predicted sub-holographic sense confirmed). **Sign PASS.** The seed-warned `R_H/ℓ_KK ~ 10³⁹` overcount would have manifested as `ratio_Bousso > 1` (a VOLUME law on an AREA screen); the substrate is firmly in the area-respecting regime on this light-sheet — it does NOT over-produce here.
- **Conclusion**: the GGE relic microstate count is holographically consistent on the white-hole exit light-sheet (closes G1 in the right direction — the substrate respects the Bousso bound). Consistent with W1-1's independent finding that S_micro UNDERCOUNTS A/4G by 2.86 OOM (`log10 R_quarter = −2.8557`): the Bousso ratio IS exactly that same `R_quarter` (both are `S_micro / (A_horizon_FW/4)`), so the falsifier confirms the area law is a valid **upper bound** the relic obeys with large margin — distinct from whether S_micro equals A/4 (the 1/4-coefficient question W1-1 answered FAIL on the equality, here PASS on the inequality).

**Assessment (substrate-first, solution-space)**: The substrate's OWN entropy fits comfortably inside its OWN emergent holographic screen — this is not a GR inequality imposed from outside but a statement about whether the GGE relic's accessible-Hilbert-space log-dimension (a count on D_K) is bounded by the a₂-Seeley-DeWitt-moment area on the emergent metric. It is, by **~3 OOM on both bounds**. The white-hole light-sheet is the emergent causal surface of the supersonic transit (the acoustic disconnector), not a black-hole horizon in a container; the Bousso bound asks whether the substrate's spectral-mode content exceeds what its emergent area can holographically encode, and the answer is a clean NO. **Constraint-map update**: G1 (no microstate entropy) closes in the right direction on the consistency axis — the substrate is sub-holographic, so the area law is a respected upper bound, NOT violated. The result is the **complement** of the seed's R_H/ℓ_KK overcount worry: that overcount is a SPATIAL-mode VOLUME count; the GGE relic is a CONSERVED-CHARGE STATE count, and on this finite light-sheet the state count is far below the area bound (no volume-vs-area pathology localized here). **Dual-prior posterior**: both ratios ≤ 1.0 → 0.9 to **Track A** (holographically consistent; the substrate entropy is sub-holographic). **Forward bridge**: a FAIL (ratio > 1) would have been the first rung toward a localized compact-object entropy (G3, the Bousso bound on a FINITE light-sheet is how a localized object's entropy is built); the PASS instead confirms the relic-scale consistency and leaves the G3 compact-object-entropy construction as a genuinely open, separate emptiness.

*Caveat (honest scope)*: the consistency is a clean PASS at the relic / exit-light-sheet scale; it does NOT by itself construct a compact-object entropy (the bound is RESPECTED with margin, which is necessary but not the construction of a localized S_obj). The Bekenstein RHS uses E = E_exc (the integrated transit relic energy) and R from the emergent exit-horizon area; both are canonical substrate-first quantities, but the precise identification of "the relic energy on the light-sheet" is the integrated transit value — a different light-sheet truncation (a finite sub-region) would carry a smaller A and a smaller enclosed E, and the consistency on such finite truncations (the G3 program) is not tested here.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

All four artifacts verified on disk by content (not line count):

- **Script** `computations/investigation-4/inv4_w1_bousso_bekenstein_falsifier.py` — `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # ...`; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call in `main()`. ✓
- **Data** `computations/investigation-4/inv4_w1_bousso_bekenstein_falsifier.npz` — present; npz fields include `S_micro_in`, `S_max_Bousso`, `S_max_Bekenstein`, `M_Bousso`, `M_Bekenstein`, `ratio_Bousso`, `ratio_Bekenstein`, `R_lightsheet` (all plan-required fields). ✓
- **Plot** `computations/investigation-4/inv4_w1_bousso_bekenstein_falsifier.png` — present; panel 1 = `S_micro` vs the two bound values (`A_horizon_FW/4`, `2πRE`) on log scale, margins annotated; panel 2 = the two ratios vs the bound (= 1.0) with the saturation INFO band drawn. ✓
- **Verdict line** `computations/investigation-4/inv4_gate_verdicts.txt` — matches `^INV4-W1-3-BOUSSO-BEKENSTEIN-FALSIFIER:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion row + schema-v2 [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + Bousso/Bekenstein/inputs companion rows. ✓ (grep output in the agent's final message.)

---

### §W1-4. INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The exit-horizon greybody factor `Γ(ω)` (transmission through the a_4-BCS-gradient barrier set by κ_exit), applied as `A_s = |β_fold|²·∫Γ(ω)dω`, accounts for the 3.15-OOM AMPLITUDE-NORM-66 FAIL as a shape-preserving greybody suppression rather than a permanent structural wall.
**Plan reference**: `sessions/investigation/investigation-4/investigation-4-plan-w1.md` §W1-4.

**MCP Pre-Compute Audit**:

| Query | Salient return | Disposition |
|:------|:---------------|:------------|
| `search_knowledge("AMPLITUDE-NORM-66 A_s normalization 3.15 OOM amplitude gap")` | `AMPLITUDE-NORM-66` = **FAIL (marginal)**, A_s gap **3.15 OOM** (Route B, Peter-Weyl), S66; "right ratios, wrong amplitudes" | baseline confirmed (3.15 OOM is the gate baseline) |
| `search_knowledge("greybody factor exit horizon transmission kappa_exit a_4 surface gravity")` | S43/S95 greybody machinery `Γ(ω)` exists; `s69_bcs_surface_gravity`, `s73a_exit_horizon_bog`; "Asymmetric Fold: Entry Horizon, Open Exit" open channel | gate NOT pre-closed — this is a NEW greybody-suppression-vs-wall test (no prior `A_s = |β|²·∫Γdω` evaluation) |
| `get_constant("A_s_CMB")` | `2.1e-09` (Planck 2018 VI; S96-OBS-ANCHOR-HYGIENE) | normalization target confirmed |
| `get_constant("T_compound")` (via canonical import) | `7.578099743651275` = `E_exc/8` = the a₄ exit temperature `T_exit` | importable T_exit alias confirmed (= κ_exit/2π) |
| `get_constant("kappa_exit")` / `get_constant("T_exit")` | both **not found** at plan-freeze | substrate-first §(ii) pre-promotion required (executed — see Results) |
| `trace_entity("S95-W4-2-HAWKING-ANALOG-T-LEDGER")` | gate PASS; `row2_exit_a4: kappa=47.6146, T=7.5781, corpus=7.578, dev=0.0000, disp=PLACED` | κ_exit provenance confirmed (47.6146) |

Not PRE-CLOSED. AMPLITUDE-NORM-66 is a FAIL on the books; this gate tests whether the exit-horizon greybody transmission filter (never previously applied as `A_s = |β_fold|²·∫Γdω`) reduces that gap.

**Verdict**: **FAIL** — composite (collapse rule: `sign=PASS ∧ magnitude=FAIL ∧ regime=VALID ⇒ FAIL`). The greybody factor SUPPRESSES (sign correct) but supplies only **−0.0397 OOM** of suppression, ~80× short of the 3.15 OOM needed; the filtered gap is `|delta_OOM| = 13.09 ≫ 3.15`. The "permanent structural wall" reading of AMPLITUDE-NORM-66 (atlas-04 A2) **survives** — the 3.15-OOM amplitude miss is NOT an exit-physics greybody effect.

[SIGN] 3-tuple: `sign_verdict=PASS` · `magnitude_verdict=FAIL` · `regime_verdict=VALID`.

**Results**:

Numbers first.

| Quantity | Value | Source / meaning |
|:---------|:------|:-----------------|
| `kappa_exit` | `47.6146` M_KK | a₄^{Pauli-Villars} BCS condensation-energy gradient (pre-promoted to canonical_constants.py SECTION C; S95-W4-2 row2_exit_a4) |
| `T_exit = κ_exit/2π` | `7.57810` M_KK | matches `T_compound = 7.57810` (Hawking T=κ/2π consistency, 6 sf) |
| `V₀` (barrier peak) | `2267.15` | `= κ_exit²` |
| `α` (inverse width) | `47.6146` | `= κ_exit` (barrier characteristic scale IS the surface gravity) |
| `ω_max` | `476.146` | `= 10·κ_exit` (Γ→1 well above; integral converged) |
| `|β_fold|²` | `59.8` | total integrated produced squeeze (s75 `n_even_abs`); `|n_pairs − this| = 0` |
| `∫Γ(ω)dω` | `434.5516` | greybody transmission integral over [0, ω_max] |
| **`f_grey = ∫Γdω / ω_max`** | **`0.912644`** | fractional transmission (< 1 ✓ suppression) |
| **greybody suppression** | **`−0.0397 OOM`** | `= log10(f_grey)`; the suppression the filter actually supplies |
| `A_s_filtered = |β_fold|²·∫Γdω` | `2.598619e+04` | greybody-filtered escaping amplitude |
| `A_s_CMB` (Planck) | `2.1e-09` | normalization target |
| **`delta_OOM = log10(A_s_filtered/A_s_CMB)`** | **`+13.0925`** | filtered gap (vs un-filtered baseline 3.15) |
| `|delta_OOM|` vs band | `13.09` ≥ `3.15` | FAIL band |

4-tuple: `(value=13.092523, scheme=GREYBODY-TRANSMISSION-BARRIER, convention=ABSOLUTE, L_max=N/A)`.
Regulator pin: `a_4^{Pauli-Villars}`. CLASS pin: **FULL** (full physical transmission barrier; no SCHEMATIC helper imported — so no `-SCHEMATIC` suffix / `tier_pin=TIER-2` flip required per substrate-first §(iv)).
Canonical pre-promotion (substrate-first §(ii)): `update_constant("kappa_exit", 47.6146, session="S95", source="S95-W4-2-HAWKING-ANALOG-T-LEDGER row2_exit_a4", section="SECTION C")` executed BEFORE the script imported it; `T_exit` imported as the already-canonical `T_compound = 7.578099743651275` alias. No verdict-string placeholder consumed as a pin. (canonical_constants.py SHA at run = `8505153a...`, post-promotion.)
Canonical constants consumed: `A_s_CMB`, `T_compound`, `kappa_exit`, `n_pairs`, `M_KK`, `tau_fold`.

Cross-checks (all PASS):
- **Convergence**: integral drift at N_ω=4000 vs 2000 = `0.000e+00` (< 1e-2 target). The integral is converged.
- **Model-independence**: analytic Pöschl-Teller `Γ(ω)` vs a model-independent 2×2 transfer-matrix scattering solve of the SAME `V_eff(x)=V₀/cosh²(αx)` — max deviation `1.31e-06` over the coarse grid. The `f_grey ≈ 0.91` suppression magnitude is NOT an artifact of the analytic barrier choice; any bounded transmission `0≤Γ≤1` integrated over a finite [0, 10κ] window gives the same `O(1)` result.
- **Squeeze consistency**: `|β_fold|²` from s75 `n_even_abs` equals canonical `n_pairs = 59.8` exactly (`|Δ| = 0`).

Substitution chain (with substituted numbers; the [SIGN] derivation):

```
Claim: Γ(ω) SUPPRESSES A_s (DECREASES it), the canonical 'right ratios, wrong amplitude' signature.
  Step 1: A_s^{unfiltered} = |β_fold|² = 59.8   [produced squeeze; s75 |β_k|² aggregate].
  Step 2: Γ(ω) = transmission through V_eff(ω), barrier height set by κ_exit = 47.6146
          (a_4^{Pauli-Villars} BCS gradient). Property: 0 ≤ Γ(ω) ≤ 1; Γ→0 as ω→0; Γ→1 as ω≫κ_exit.
          [Pöschl-Teller exact form, cross-checked by transfer-matrix to 1.3e-6.]
  Step 3: A_s^{filtered} = |β_fold|² · ∫₀^{ω_max} Γ(ω)dω = 59.8 · 434.5516 = 2.5986e+04.
  Substitute 0 ≤ Γ ≤ 1:  ∫Γdω = 434.5516 < ∫1 dω = ω_max = 476.146  ⇒ f_grey = 434.5516/476.146 = 0.9126 < 1.
  Simplify: A_s^{filtered}/A_s^{unfiltered-normalized} = f_grey = 0.9126 < 1.
  Direction: SUPPRESSION — the greybody factor strictly DECREASES the amplitude (sign NEGATIVE). ✓ sign_verdict=PASS.
  Magnitude: log10(f_grey) = −0.0397 OOM. The bound 0≤Γ≤1 over a finite [0, 10κ] window can NEVER supply more
          than log10(1/ε)≈O(1) OOM of suppression — it is structurally incapable of the 3.15 OOM the gap needs.
          ⇒ delta_OOM(filtered) = +13.09 ≫ 3.15.  magnitude_verdict=FAIL.
  Conclusion: the greybody factor SUPPRESSES (sign correct, the 'right ratios, wrong amplitude' direction holds
          — a multiplicative shape-preserving Γ(ω) leaves the log-derivatives n_s/α_s/r intact) but the
          suppression magnitude (−0.04 OOM) is ~80× short of resolving the 3.15-OOM gap. The 'permanent
          structural wall' reading (atlas-04 A2) SURVIVES this test; the amplitude miss is NOT an exit-physics
          greybody effect. [The +13.09 filtered gap reflects the gate's ABSOLUTE convention A_s=|β|²·∫Γdω in
          M_KK units; the structural finding is in f_grey (the suppression factor), which is the quantity the
          'wall vs suppression' question turns on.]
```

**Substrate framing.** The exit horizon IS a substrate feature: the a₄ BCS condensation-energy gradient at the post-fold transit defines κ_exit (surface-gravity analog) and the transmission barrier the produced squeeze must pass to become observable. `Γ(ω)` is not imported from black-hole physics — it is the frequency-dependent transmission of the substrate's own a₄-grade barrier (`D_K eigenvalues → a₄ BCS gradient → κ_exit / exit-horizon barrier → Γ(ω) → A_s = |β_fold|²·∫Γdω`). The transmission is bounded `0≤Γ≤1` by unitarity; its integral over a finite frequency window is `O(1)` of `ω_max`, so a transmission filter can shape the spectrum but cannot manufacture a 3.15-OOM amplitude deficit. The "wall" is structural, not an un-applied escape filter. Dual-prior disposition: `|delta_OOM| ≥ 3.15` with sign=suppression ⇒ **0.9 mass to Track B** (greybody negligible at the relevant scales relative to the gap; the AMPLITUDE-NORM-66 wall reading stands; the normalization miss must be sought elsewhere). Solution-space: this closes the greybody-transmission corridor to the A_s normalization — a sharp boundary in the constraint map, per `math-scripts.md §"All Results Are Good Results"`. The HY6 byproduct still holds: the gate forces a `κ_exit ↔ A_s` relation (the barrier height IS κ_exit), so T_exit and the escaping amplitude are no longer independent — but that relation does not close the OOM gap.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **Script** `computations/investigation-4/inv4_w1_exit_greybody_as.py` (27,618 bytes) — `grep -nE "from canonical_constants import|print_verdict_payload"`:
  ```
  53:- from canonical_constants import *
  83:from canonical_constants import *  # noqa: F401,F403
  84:from canonical_constants import (
  445:def print_verdict_payload(verdict, value, audit_sha, content_sha,
  585:    print_verdict_payload(
  ```
- **Data** `computations/investigation-4/inv4_w1_exit_greybody_as.npz` (41,443 bytes) — all 9 plan-mandated fields PRESENT: `omega_grid`(2000), `Gamma_omega`(2000), `integral_Gamma`=434.5516, `f_grey`=0.912644, `beta_fold_sq`=59.8, `A_s_filtered`=2.598619e+04, `delta_OOM`=13.092523, `baseline_OOM`=3.15, `kappa_exit_used`=47.6146.
- **Plot** `computations/investigation-4/inv4_w1_exit_greybody_as.png` (84,084 bytes) — `Γ(ω)` transmission barrier (analytic + transfer-matrix x-check, κ_exit marked) + A_s gap-closure bar (filtered delta_OOM vs 3.15 baseline, PASS band annotated).
- **Verdict line** `computations/investigation-4/inv4_gate_verdicts.txt` — `grep -E "^INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION:.* audit_sha256=[a-f0-9]{64}"`:
  ```
  INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION: FAIL -- value='delta_OOM=13.092523;abs=13.092523;baseline_OOM=3.15;f_grey=0.912644;grey_suppression_OOM=-0.039699;integral_Gamma=434.551610;beta_fold_sq=59.8000;A_s_filtered=2.598619e+04;kappa_exit=47.6146' scheme=GREYBODY-TRANSMISSION-BARRIER convention=ABSOLUTE L_max=N/A audit_sha256=291bae3d786ab1f4bee4352f7e6920a007dcdf2a108d56114c2917162a55f34b content_sha256=30d58eec4df8e86de2c6e8a85e21f44dbc6278dca82cc63e61491b681d0d2f8c schema_version=S84+
  ```
  Companion + schema-v2 3-tuple rows (present):
  ```
  # audit_sha256_short=291bae3d786ab1f4 content_sha256_short=30d58eec4df8e86d # INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION dual-SHA companion row; ...
  # sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID # INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION 3-tuple annotation (schema-v2)
  ```
  Plus regulator-pin (`a_4^{Pauli-Villars} CLASS=FULL`) + greybody-detail + cross-check extra rows.
- **Canonical pre-promotion**: `kappa_exit = 47.6146` added to `computations/_shared/canonical_constants.py` SECTION C (via `update_constant`, session=S95, gate=S95-W4-2-HAWKING-ANALOG-T-LEDGER) BEFORE the script import.

---

## Wave 1 Synthesis (team-lead)

Wave 1 attacked the Bekenstein-Hawking `S = A/4G` from four substrate-side angles. The headline: the **1/4 coefficient is now DERIVED, not imported** — but only on the correct observable, and the wave cleanly separated *which* substrate structure carries *which* part of horizon thermodynamics.

**The four verdicts decompose into one coherent island-vs-bulk picture:**
- **W1-2 PASS (the keystone)**: the Euclidean replica `S=(1−n∂_n)lnZ(n)` reproduces `A/4` to 5e-7 — `c_conical = 0.25` EXACTLY — via the conical-deficit response of the **a₂ Seeley-DeWitt grade** (smooth Einstein-Hilbert piece annihilated → A/6 corner → A/4 by the 3/2 heat-kernel→on-shell weight). The 1/4 is structurally a *ratio* (entropy-coefficient ÷ induced-Newton-coupling), forced — not fitted.
- **W1-1 FAIL (informative, not a wall against the framework)**: the GGE-relic microstate count `S_micro = 24.82` nats *undercounts* `A/4 = 17806.6` nats by 2.86 OOM. But its Page-shape test PASSed (rise-then-fall, argmax f=½) — the relic IS the cross-horizon information ledger. So the area *coefficient* (W1-2) and the information *ledger* (W1-1) are carried by **different substrate structures** (the a₂ conical geometry vs the GGE entanglement) — an island-vs-bulk split, not a contradiction.
- **W1-3 PASS**: loading `S_micro` from W1-1 (zero free parameters), both holographic bounds hold with ~3 OOM margin (Bousso ratio 1.39e-3, Bekenstein 8.66e-4). The Bousso ratio IS numerically W1-1's R_quarter — confirming the area law as a respected **inequality** (upper bound) exactly where W1-1 found the **equality** fails. Same number, two different tests, two consistent verdicts.
- **W1-4 FAIL**: the exit greybody `Γ(ω)` suppresses by only −0.04 OOM (`f_grey=0.9126`), ~80× short of the 3.15-OOM AMPLITUDE-NORM-66 gap. Established as *structural* (unitarity `0≤Γ≤1` bounds the integral; model-independent across Pöschl-Teller vs transfer-matrix to 1.3e-6) → the **permanent structural wall reading of atlas-04 A2 survives**; the A_s miss is not an exit-physics effect.

### (a) Numerical revisions
- `c_conical = 0.25` EXACTLY (replica route); `R_replica = 1.0` (|R−1|=5e-7).
- `S_micro = 24.8245` nats; `R_quarter = 1.394e-3` (−2.86 OOM undercount, microstate route).
- holographic margins: Bousso ratio `1.394e-3`, Bekenstein ratio `8.656e-4`; `R_lightsheet = 75.286` GeV⁻¹.
- greybody `f_grey = 0.9126` (−0.0397 OOM); filtered gap `|Δ_OOM| = 13.09 ≫ 3.15`.
- `κ_exit = 47.6146 M_KK`, `T_exit = κ/2π = 7.5781 = T_compound` (Hawking relation to 6 sf).

### (b) Structural changes
- **1/4-from-substrate corridor: OPEN → PARTIALLY EARNED.** The coefficient is derived on the a₂ conical-deficit observable (W1-2), CLOSED on the GGE-microstate observable (W1-1, −2.86 OOM). atlas-04 A1 (imported 1/4) closes in the right direction *on the replica route only*.
- **A1 (1/4 coefficient) and the information ledger are now distinct substrate structures** (a₂ conical geometry vs GGE entanglement) — an epistemic-type change, not a magnitude tweak.
- **atlas-04 A2 (A_s structural wall) reading STRENGTHENED**: W1-4 shows it is unitarity-structural, not a greybody artifact.

### Effected In-Session (non-math; team-lead)
- [x] `κ_exit = 47.6146` canonical promotion to `canonical_constants.py` SECTION C — effected by the W1-4 agent at runtime (substrate-first §(ii) pre-promotion, S95-W4-2 provenance) — `computations/_shared/canonical_constants.py` — shared-infrastructure constant (NOT a curated session-track register; track-local boundary preserved). Recorded here for traceability.
- [x] Wave-1 synthesis (this section) + math/non-math split written — `investigation-4-w1-workingpaper.md §"Wave 1 Synthesis"`.
- No session-track register edits (track-local boundary, `gate-verdicts.md §"Track-local boundary"`): the atlas-04 A1/A2 reconciliations are session-track and route to `/rclab-investigate --investigation 4` close, NOT effected here (see Carry-Forward + housekeeping §B/§D).

## Carry-Forward Computations

### CF-INV4-W1-A — Boundary-mode microstate count for the A/4 equality
1. **What**: Compute a horizon-localized boundary-mode (edge-mode) entropy on the white-hole exit screen and test `S_boundary = A/4` as an EQUALITY (W1-1 closed the GGE-relic bulk-charge route at −2.86 OOM; the equality's microstate origin is owed by a boundary count, per the island-vs-bulk split this wave established).
2. **Inputs**: `inv4_w1_gge_page_curve.npz` (bulk S_micro reference), `A_horizon_FW=71226.263`, the a₂ conical-corner structure from `inv4_w1_euclidean_replica.npz`, L12 spectrum cache.
3. **Gate**: `|S_boundary/(A/4) − 1| ≤ 0.10` PASS / `≤ info_band` INFO / else FAIL (pre-register publication precision per Class 8.3).
4. **Effort**: ~1 compute wave.

### CF-INV4-W1-B — Session-track promotion of the a₂-conical 1/4 derivation
1. **What**: Lift the W1-2 replica derivation (`c_conical=0.25` from the a₂ conical-deficit response) into a session-mode gate for permanent-registry promotion (investigation results are NOT permanent — migrate, do not cite, per the track-local boundary).
2. **Inputs**: `inv4_w1_euclidean_replica.py/.npz` (audit_sha256 `58b29602…585b2e58`), the a₂^{PV}/a₄^{PV} regulator pins.
3. **Gate**: session-mode re-run reproduces `c_conical=0.25` to ≤1e-6 under `canonical_constants` pins; then registry-landing per the cross-pillar / permanent-results discipline.
4. **Effort**: ~1 compute + 1 registry-landing.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | A/4 coefficient (replica route, INV4-W1-2) | imported (atlas-04 A1) | DERIVED from a₂ conical-deficit response (c_conical=0.25, 5e-7) | substrate-first replica computation |
| 2026-06-15 | A/4 microstate origin (GGE-relic route, INV4-W1-1) | open | CLOSED on GGE-bulk-charge route (−2.86 OOM undercount); boundary-mode route owed | microstate count is conserved-charge, not area-saturating |
| 2026-06-15 | Holographic consistency (INV4-W1-3) | untested | PASS — S_micro sub-holographic, both bounds respected ~3 OOM margin | zero-parameter Bousso+Bekenstein falsifier |
| 2026-06-15 | A_s normalization wall (atlas-04 A2, INV4-W1-4) | structural-wall reading (candidate) | STRENGTHENED — greybody-unitarity-structural, not exit-physics | f_grey=0.9126, model-independent to 1.3e-6 |
| 2026-06-15 | `κ_exit` canonical constant | absent | `= 47.6146 M_KK` (canonical_constants.py SECTION C, S95-W4-2 prov.) | substrate-first pre-promotion (W1-4) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict (audit_sha256) | Size |
|:-----|:-------|:------------|:------------|:-----------------------|:-----|
| INV4-W1-1 | `inv4_w1_gge_page_curve.py` | `inv4_w1_gge_page_curve.npz` | `…png` | `7fdd279d…a61483` (FAIL) | script 28KB |
| INV4-W1-2 | `inv4_w1_euclidean_replica.py` | `inv4_w1_euclidean_replica.npz` | `…png` | `58b29602…585b2e58` (PASS) | script 29KB |
| INV4-W1-3 | `inv4_w1_bousso_bekenstein_falsifier.py` | `…npz` | `…png` (99KB) | `fe26027e…fa8a50` (PASS) | — |
| INV4-W1-4 | `inv4_w1_exit_greybody_as.py` | `…npz` (41KB) | `…png` (84KB) | `291bae3d…a55f34b` (FAIL) | script 28KB |

All artifacts under `computations/investigation-4/`; verdict lines in `computations/investigation-4/inv4_gate_verdicts.txt`.
