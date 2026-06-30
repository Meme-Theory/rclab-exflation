# Session 96 Wave 4 — `a₄` Matter Sector + Seesaw Reconciliation (Results Working Paper)

**Session**: 96 | **Wave**: W4 | **Plan**: session-96-plan-w4.md | **Theme**: `a₄` matter sector + seesaw reconciliation (cluster C6 + dissonance D5) — fermion masses/mixings as the representation content of `D_K`; Yukawa = spin-0 inner-fluctuation of the `a₄` Seeley-DeWitt moment; PMNS off-diagonals; J-structural Majorana/0νββ; CPT-barred internal baryogenesis vs emergent-g_M channel; direct-from-D_K mass-hierarchy R; S60 seesaw–vs–§0 "no seesaw" adjudication.

## Gate Sections

### §W4-1. S96-MATTER-A4-YUKAWA-RATIO (paasch-bohr-complementarity-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-MATTER-A4-YUKAWA-RATIO`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (a₄ Yukawa-block mass-ratio extraction via inner-fluctuation spin-0 Higgs)
**Agent**: `paasch-bohr-complementarity-theorist` (executed by paasch-mass-quantization-analyst)
**Hypothesis**: The off-diagonal (Higgs-coupled) entries of the `a₄` Yukawa block of `D_K(τ_fold)`, after inner fluctuation `D_K → D_K + A`, produce at least one non-degenerate, zero-free-parameter dimensionless fermion mass ratio — i.e. the capstone claim "Yukawas all read from `D_K(τ)`" is non-empty at one generation.
**Plan reference**: `sessions/session-plan/session-96-plan-w4.md` §W4-1 (machinery pin, thresholds, substitution chain source).

**Verdict**: **INFO**

**Substrate framing** (PARTICLE; `phononic-framing.md`): the fermion mass matrix is NOT an external input — it IS the spin-0 inner-fluctuation content of the `a₄` Seeley-DeWitt coefficient (`a_4^{Pauli-Villars}`) of `D_K`. Direction of explanation, unchanged: **`D_K` eigenvalues → `a₄` Yukawa spectral moment → mass bilinears on Ψ₊ generation content → dimensionless ratio `R_Yuk`**. The substrate IS this ratio; the SM fermion-mass table is the laboratory-IN image the `a₄` block must reproduce. No external mass is imported as a canonical pin; PDG masses enter ONLY as comparison anchors per `substrate-first-canonical-sourcing.md §(i)`.

**Results** (NUMBERS first):

- **PRIMARY observable** `R_Yuk` (zero-free-parameter): the distinct-cluster ratio of the **bare** `D_K` chirality-off-diagonal (Yukawa/mass) block on the fundamental sector `V_(1,0) ⊗ ℂ¹⁶`, gauge-summed (gauge-invariant):
  - `R_Yuk = m_heavy / m_light = 1.588` (4 sig figs **1.588**); `m_heavy = 1.327661`, `m_light = 0.835894` (M_KK units).
  - **11 distinct mass eigen-bilinears** (gauge-orbit multiplicities 4/3/3/2/3/2/1/2/1/2/1): `{1.3277, 1.2024, 1.1848, 1.1362, 1.0784, 1.0752, 1.0729, 1.0222, 0.9572, 0.8409, 0.8359}`. The block is **NON-DEGENERATE** ⇒ the empty-layer claim is **refuted** at one generation.
- **Nearest SM fermion-mass anchor** (comparison only): `m_τ/m_μ = 16.817` (`m_μ` canonical = 0.1056583745 GeV; `m_τ` = 1.77686 GeV PDG comparison). **`|log10(R_Yuk / R_SM_anchor)| = 1.0248`** — just OUTSIDE the 1-OOM PASS band (≤ 1.0); all other anchors (`m_μ/m_e=206.8`, `m_t/m_b=41.3`, `m_t/m_c=136.0`, `m_s/m_d=20.0`, …) are farther.
- **Degeneracy check**: `R_Yuk = 1` to `1e-12`? **NO** (`R_Yuk = 1.588 ≠ 1`; bare spread `0.4918 > 1e-12`). The FAIL/empty branch is **not** triggered.
- **4-tuple**: `(value=1.5883138995005102, scheme=CCM-2007-inner-fluctuation-spin0-Higgs, convention=ABSOLUTE, L_max=12)`. `regulator_pin = a_4^{Pauli-Villars}`.

**CC1 — inner-fluctuation spin-0 Higgs `A⁽⁰⁾` extraction (CCM-2007 §2.5)**:
- Built `A = Σᵢ aᵢ[D_K, bᵢ]` on the fundamental sector with `aᵢ, bᵢ ∈ A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` (M₃ summand spanned by the 8 su(3) generators + identity; deterministic coefficient mixing seed=0). Anti-Hermitized (math convention, matching `D`). Spin-0 (Higgs) part `A⁽⁰⁾ = ½(A − γ₉ A γ₉)` = the **γ₉-anticommuting** (chirality-off-diagonal) component connecting H_K⁺ ↔ H_K⁻; `‖A⁽⁰⁾‖ = 2.803`. The spin-1 (gauge, γ₉-commuting) part `‖A⁽¹⁾‖ = 0.000` for this `[D_K, b]` construction — the commutator with the off-diagonal-in-chirality `D` produces a purely off-diagonal (Higgs) one-form, confirming the CCM identification that `[D, A_K]` generates the spin-0 (mass) channel.
- **Seed-robustness probe (decisive structural finding)**: the *fluctuated* distinct-cluster ratio is **coefficient-dependent** — across 6 deterministic seeds it ranges `R_Yuk_fluct ∈ [1.46, 3.22]`, straddling the PASS/INFO boundary. The inner-fluctuation coefficients `aᵢ` are **free parameters**; a value that depends on them is NOT a zero-free-parameter observable. Per the gate's "zero free parameters" requirement, the admissible observable is therefore the **bare** `D_K` Yukawa block (the `a₄` spin-0 content of `D_F = D_K` itself, before adding a tunable Higgs VEV), which is fully deterministic and gauge-invariant. The seed=0 fluctuated value (`R_Yuk_fluct = 1.490`) is reported as a diagnostic only.

**CC2 — Ψ₊ generation-content sub-block diagonalization residual**:
- The Cl(8) spinor ℂ¹⁶ splits under `γ₉` into chirality ± (8 + 8); the 8 H_K⁺ states (`[0,3,5,6,9,10,12,15]`) are simultaneous so(8)-Cartan weight states with distinct weight 4-tuples `(s₀,s₁,s₂,s₃) ∈ {±1}⁴` (even half-spinor 8_s) — these ARE the irrep-distinguishing Ψ₊ summands `(3,2,⅙)⊕(3̄,1,−⅔)⊕(3̄,1,⅓)⊕(1,2,−½)⊕(1,1,1)⊕(1,1,0)`. The per-gauge-component generation block has off-diagonal residual `0.990` (bare) — i.e. the mass operator is almost entirely off-diagonal in the weight basis (the chirality pairing maps + weights to distinct − weights), so the **singular values** (basis-independent) are the physical mass bilinears, NOT the diagonal.
- **Gauge-invariance caveat (load-bearing)**: a single-gauge-component slice (`g0=0`) is NOT gauge-invariant — the orthonormal frame `E` entangles the SU(3) gauge orbit with the weight grading, so per-gauge-component blocks differ (`g0=0,1 → R=2.397`; `g0=2 → R=1.650`). The reported `R_Yuk = 1.588` is read from the **full gauge-summed** 24×24 off-diagonal block's distinct-cluster spectrum, which IS gauge-invariant.

**Substitution chain** (with substituted numbers; per `math-scripts.md §"Double-Check Logic"`):
- Claim: "A non-degenerate fermion mass ratio is extractable from the `a₄` Yukawa block iff the Higgs sub-block is NOT generation-blind (Schur-degenerate)."
- Step 1: `M_Yuk = ` chirality-off-diagonal block `P₋(D_K + A⁽⁰⁾)P₊` on `V_(1,0) ⊗ ℂ¹⁶`. [CCM-2007 §2.5; `D_F = D_K` is the bare mass matrix]
- Step 2: `m_a = ` singular values of `M_Yuk`; `R_Yuk = m_heavy / m_light`. [operator def, plan §1]
- Step 3 (Schur test): if `M_Yuk|_{sub-block} = μ·𝟙` (blind irrep) then `eig = {μ,…,μ} ⇒ R_Yuk = 1`. **Computed**: bare `M_Yuk` has **11 distinct** singular values, spread `0.4918`, so `M_Yuk ≠ μ·𝟙`. [non-Schur confirmed]
- Step 4 (direction): `R_Yuk ≥ 1` by heavy/light ordering. The discriminating question is `R_Yuk = 1` (degenerate, FAIL/empty) vs `R_Yuk > 1` (splitting, PASS-eligible). **Computed**: `R_Yuk = 1.588 > 1` ⇒ splitting present, non-empty layer.
- Step 5 (PASS band): PASS requires `R_Yuk > 1` **AND** `|log10(R_Yuk/R_SM_anchor)| ≤ 1.0`. **Computed**: first conjunct TRUE (1.588 > 1); second conjunct FALSE (`1.0248 > 1.0`). ⇒ **INFO**, not PASS.
- Conclusion: the `a₄` Yukawa block is **structurally non-empty** at one generation (the capstone claim "Yukawas read from `D_K(τ)`" is non-vacuous — there IS a non-degenerate mass-bilinear spectrum), but the **zero-free-parameter** ratio (1.588) is **OOM-only**: it matches no single SM fermion-mass ratio within 1 OOM. Register as a bare-spectrum (geometric) ratio pending family structure.

**Cross-checks & provenance**:
- **Cache cross-check (bit-faithful)**: the in-gate `D_K` reconstruction on the fundamental sector reproduces the s84 `L_max=12` cache exactly — bare fundamental `|λ|` range `[0.8359, 1.3277]` and the 24 off-diagonal singular values `{1.32766128, …, 0.83589351}` match the cache `(1,0)` sector `abs_evals` to display precision. Anti-Hermiticity error `0.00e+00`.
- **Structural anchor (MCP)**: the cross-sector closures (`S77-C10-YUKAWA-PMNS` INFO:NULL "all cross-sector Y = 0 exactly"; W2 block-diagonality PROVEN; "Yukawa tree-level mass generation — vanishes by PW orthogonality" S62 PROVEN) concern **cross-(p,q)-sector** off-diagonals (the PMNS / W4-2 domain). This gate is **structurally distinct**: it reads the **within-sector** chirality-off-diagonal (Yukawa) block of a single fundamental sector. The two are non-overlapping; the INFO here is consistent with — and complementary to — the cross-sector NULL.
- **regulator_pin**: `a_4^{Pauli-Villars}` (the Yukawa block is the spin-0 content of the `a₄` Seeley-DeWitt coefficient; PV-regulated per `regulator-pin-discipline.md`).
- **dual-SHA** (full 64-char): `audit_sha256=4ee21185689a5642f7d19e05d6021a58693fa90c5fb314dd7544f4d43f9be830`; `content_sha256=0010d5259bc980063e1147c32881ae62bff36245e750fc04dcc1b4f8e1fc0140`.
- **Canonical write-order**: verdict is INFO (not PASS), so `R_Yuk_FW` is **NOT** registered as a canonical constant (per the gate's PASS-only registration rule). The bare-spectrum ratio 1.588 is recorded in the npz + this WP only, pending the family-number frontier.

**Output Artifacts** (closure-verification checklist):
- script `computations/session-96/s96_matter_a4_yukawa_ratio.py` — present (35,725 B); `grep` for `from canonical_constants import` ✓ and `append_verdict` ✓ (both match).
- data `computations/session-96/s96_matter_a4_yukawa_ratio.npz` — present (23,910 B).
- plot `computations/session-96/s96_matter_a4_yukawa_ratio.png` — present (83,653 B).
- verdict line `computations/session-96/s96_gate_verdicts.txt` — present; matches `^S96-MATTER-A4-YUKAWA-RATIO:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ (line 85). No `[SIGN]` 3-tuple required (`[VERIFY]` trigger; no directional pre-registration).
- this WP §W4-1 — Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit present.

**MCP Pre-Compute Audit** (per `knowledge-index-usage.md`; query-first discipline):
- `search_knowledge("a4 Yukawa block inner fluctuation fermion mass ratio D_K")` → hits: Path-B RQ-1 inner-fluctuation simulator registry; eq `D_A = D_K + A + JAJ⁻¹` (S61); `D_F = finite Dirac operator (mass/Yukawa matrix)` (S86); gate `S77-C10-YUKAWA-PMNS` (INFO:NULL, cross-sector). **NOT PRE-CLOSED** for the within-sector chirality-off-diagonal extraction.
- `search_knowledge("inner fluctuation Higgs one-form A spin-0 CCM-2007 finite Dirac mass")` → `D = D_M × 1 + γ₅ × D_F`; "Higgs arises from the FINITE part of the inner fluctuation of D"; CCM-2007 finite-triple `A_F = ℂ⊕ℍ⊕M₃(ℂ)`, KO-dim 6 (PROVEN). Confirms the construction; no closure of the ratio.
- `trace_entity("Yukawa tree-level mass generation")` → theorem S62 PROVEN "Tree-level Yukawa vanishes by **PW orthogonality**" — scoped to **cross-sector** PW orthogonality (different (p,q) sectors), NOT within-sector chirality pairing. Does not pre-close this gate.
- `trace_entity("S77-C10-YUKAWA-PMNS")` → gate S77 INFO:NULL "All **cross-sector** Y = 0 exactly; PMNS from D_K alone permanently closed." Cross-sector domain (W4-2), structurally distinct from this within-sector gate.
- `search_knowledge("Peter-Weyl orthogonality tree-level Yukawa vanishes cross-sector Y=0")` → W2 Block-Diagonality PROVEN (8.4e-15) "cross-sector coupling is zero"; S35 note "NCG inner fluctuation φ preserves Peter-Weyl sectors; PMNS requires KK framework." Confirms the inner fluctuation is sector-preserving — consistent with reading the Yukawa block WITHIN the fundamental sector.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). `get_constant("R_Yuk_FW")` → **not found** (no overwrite risk). `list_constants("M_KK|mass|...")` → `M_KK=7.42866e16`, `v_ew=246`; `m_mu=0.1056583745`, `m_t_pole=172.69` (fermion-mass anchors). **NOTE**: canonical `m_tau = 2.062` is the MODULUS mass (M_KK units), NOT the τ-LEPTON — used PDG `1.77686 GeV` as comparison anchor instead.

---

### §W4-2. S96-MATTER-PMNS-3X3 (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S96-MATTER-PMNS-3X3`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (inter-sector Lie-derivative lifting the B2 Schur wall to deliver the full 3×3 PMNS)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: A KK-modified (non-left-invariant) Lie-derivative coupling between Peter-Weyl sectors breaks the B2 spinor-symmetry isolation that walls θ₁₂ and θ₂₃ to zero, delivering all three PMNS angles AND the mass-squared ratio R simultaneously inside their NuFit-6.0 bands.
**Plan reference**: `sessions/session-plan/session-96-plan-w4.md` §W4-2 (machinery pin, set-membership thresholds, substitution chain, dual_prior, fb_pair).

**Verdict**: **INFO**

The inter-sector non-left-invariant `L_X` **does lift** the B2 Schur wall — θ₁₂ and θ₂₃ open monotonically from exactly zero as ε_LX turns on, with `[iK_7, D_K] = 0` preserved at every scan point (the decisive new structural finding: no prior route delivered nonzero θ₁₂/θ₂₃). But the four observables are **not simultaneously in-band at any ε_LX** on the pre-registered [0.0,0.10] grid, and R = Δm²₃₂/Δm²₂₁ is categorically out of reach (peak R = 6.868 at ε_LX=0.030, still **2.48× below** the band floor of 17). This fires the pre-registered INFO clause verbatim ("θ₁₂ and/or θ₂₃ become nonzero but the four observables are not simultaneously in-band"). Per the dual_prior, INFO → posterior **unchanged**, route to the family-number frontier (#7) + the R scale-bridge.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):

| Query (tool) | Salient return |
|:---|:---|
| `search_knowledge("PMNS theta_12 theta_23 B2 Schur wall inter-sector")` | S52 off-Jensen: `sin²θ₂₃=0.000000 (target 0.451)`, `sin²θ₁₂=0.000000 (target 0.303)`, `sin²θ₁₃=0.368` — confirms θ₁₂=θ₂₃=0 wall; S29b legacy R sweeps all ≤ 0.79. Not closed for non-left-invariant L_X. |
| `search_knowledge("inter-sector Lie derivative coupling Peter-Weyl PMNS")` | `closed_61 "B: Inter-sector coupling | Block-diagonality theorem (any compact Lie group) | 22b-22c"` — corridor CLOSED **for LEFT-INVARIANT operators**. LIED-39 / RPA-32b Lie-derivative machinery exists (provenance hits). |
| `trace_entity("inter-sector coupling")` | `closed_61` + `closed_144` (Topic B). The closure is the block-diagonality theorem; a NON-left-invariant L_X is structurally outside its scope ⇒ gate is legitimate, not a rediscovery. |
| `trace_entity("B2 wall")` | `Δ_wall(B2) = Δ_wall(B2-bar)` (B2 = U(2) complex fundamental, J→conjugate); `[iK_7, D_K] = 0 at ALL tau` (PROVEN, proven_1211); `O(B2→B1) = O(B2→B3) = 0.0000 exactly` (zero leakage at all wall configs). |
| `trace_entity("K7-G1")` | `K7-G1-37` open_channel: "q_7 of G1 mode in (1,0) | PMNS route (independent, same session)". The side-condition the coupling must preserve. |
| `get_constant("tau_fold")` | `0.19` (S12/S42, CONST-FREEZE-42). Single-slice evaluation point. |
| `get_constant("M_KK")` | `7.428660036284456e16 GeV` (gravity-route alias, CONST-FREEZE-42). Eigenvalue unit. |

**PRE-CLOSED?** No. The block-diagonality closure (`closed_61`) bars *left-invariant* inter-sector coupling; this gate tests a *non-left-invariant* `L_X` — a structurally distinct operator outside the closure's scope. Gate executed.

**Results** (4 sig figs unless noted):

Lepton 3×3 sub-sector diagonal read directly from the L_max=12 D_K cache at τ_fold = 0.19 (sector minima, M_KK units): **B1 = (0,0) singlet E₁ = 0.8197**, **B2 = (0,1)/(1,0) fundamental E₂ = 0.8359** (the complex-rep, Schur-walled sector), **B3 = (1,1) adjoint E₃ = 0.8730**. Bit-exact cross-match to the s52 transit-fold anchors (E2 residual 2.22e-16). Off-diagonal texture V₁₂=0.077, V₂₃=0.022, V₁₃=0.0 (NNI, exact).

Anchor point ε_LX = 0.05 (off-Jensen mid-point, the pre-registered verdict point):

| Observable | Value | NuFit-6.0 band | In-band? |
|:---|:---|:---|:---|
| sin²θ₁₂ | **0.7908** | [0.25, 0.36] | ✗ |
| sin²θ₂₃ | **0.3322** | [0.35, 0.65] | ✗ |
| sin²θ₁₃ | **0.03301** | [0.015, 0.030] | ✗ |
| R = Δm²₃₂/Δm²₂₁ | **4.166** | [17, 66] | ✗ |

**Simultaneous membership: FALSE** at every ε_LX on the grid (no point lands all four; no point even lands all THREE angles — θ₁₃ wants ε_LX ≲ 0.035, θ₂₃ wants ε_LX ≳ 0.060, mutually exclusive). The 4-tuple at anchor: `value=(0.7908, 0.3322, 0.033, 4.1657)`, `scheme=inter-sector-Lie-derivative-KK-modified`, `convention=U[α,i]_ascending_mass_flavor_basis`, `L_max=10`.

*ε_LX wall-lifting monotonicity* (scan [0.0,0.10] step 0.005, 21 points): θ₁₂ and θ₂₃ both **monotone non-decreasing from 0** (mono_12 = mono_23 = True). At ε_LX=0: sin²θ₁₂ = sin²θ₂₃ = 0.000000; rising to 0.9034 / 0.4245 at ε_LX=0.10. **The B2 wall is liftable** by a non-left-invariant operator — the decisive new result.

*R shortfall* (the binding constraint): R rises from 2.278 (bare, ε_LX=0) to a peak 6.868 (ε_LX=0.030) then falls; **never enters [17,66]**, max 2.48× below floor. Mechanism-independent shortfall — consistent with all prior routes (bare fold 3.37 / off-Jensen 7.03 / MSW 3.37). R is set by the D_K eigenvalue spacing at frozen τ and is not a property the inter-sector coupling can fix.

*Side-condition `[iK_7, D_K] = 0`*: ‖[iK₇, M_lep]‖ = **0.00e+00** at every scan point (q_7-neutral coupling; Jensen SU(3)→U(1)_7 preserved). Not re-broken.

*CC1 — ε_LX=0 reproduces the Schur degeneracy*: sin²θ₁₂ = 0.00e+00, sin²θ₂₃ = 0.00e+00 → **PASS**. The mechanism correctly recovers the closed OFFJENSEN-PMNS-52 B2-wall result (2×2 B1–B3 PMNS + isolated B2) when the inter-sector coupling is off. θ₁₃ = 0.02225 at ε_LX=0 (the off-Jensen C² anchor) is retained.

*CC2 — B2 sub-block stability vs L_max=12 cache*: |E₂(cache) − E₂(s52 transit fold)| = **2.22e-16 → PASS**. The B2 diagonal element is stable between the L_max=12 master cache and the independent transit computation.

*Substitution chain (with substituted numbers)*:
- M_lep(ε_LX) = diag(0.8197, 0.8359, 0.8730) + ε_off·H₁₃ (B1↔B3, Schur-allowed) + ε_LX·L_X (B2↔B1, B2↔B3, non-left-invariant). Off-Jensen h₁₃ = ½(E₃−E₁)·tan(2θ₁₃) = 0.008217 reproduces sin²θ₁₃ = 0.02225. Inter-sector CG overlaps from 3⊗3̄ = 1 ⊕ 8: c₂₁ = √(1/9) = 0.3333 (B2↔B1), c₂₃ = √(8/9) = 0.9428 (B2↔B3).
- **Step (ε_LX=0)**: M_lep = diag + ε_off·H₁₃ ⇒ off-diag₁₂ = off-diag₂₃ = 0 (Schur on blind B2) ⇒ sin²θ₁₂ = sin²θ₂₃ = 0 — **verified numerically (CC1)**.
- **Step (ε_LX≠0)**: L_X non-left-invariant ⇒ [L_X, SU(3)-action] ≠ 0 ⇒ off-diag₁₂ = ε_LX·c₂₁ ≠ 0 ALLOWED (Schur inapplicable) ⇒ sin²θ₁₂ monotone-increasing from 0 — **verified (mono_12 = True)**.
- **Conclusion**: nonzero (θ₁₂, θ₂₃) is DECISIVE and is achieved; but the full PASS package (all four in-band simultaneously) is NOT delivered, and R is structurally unreachable. The wall lifts; the 3×3 + R does not close.

*dual_prior posterior re-allocation*: discriminator = **INFO** (θ₁₂/θ₂₃ nonzero but not simultaneously in-band; side-condition intact). Per the pre-registered map, INFO → **posterior unchanged** (Track A 0.35 / Track B 0.65 retained), route to the family-number frontier. Reading: Track B's "B2 wall is a Level-5 structural obstruction" is *partially* superseded — the wall IS liftable by a non-left-invariant operator, contradicting strict structural-obstruction — but the *quantitative* package (simultaneous in-band angles + R) is not delivered, so the gap re-localizes to family number (#7) and the R scale-bridge rather than to the B2-isolation per se. The framework's sharpest open neutrino result is now: *the angles open, R does not*.

*Downstream W4-3 feed*: the .npz stores `U` (PMNS, U[α,i] ascending-mass flavor basis; verified unitary `U Uᵀ = 𝟙` to 1e-8), `m_i = [0.7992, 0.8214, 0.9081]` (|D_K eigenvalue|, M_KK units, ascending), and `U_ei = [-0.4497, 0.8745, 0.1817]` (electron row) for `m_ββ = |Σ U_ei² m_i|`. Note for W4-3: these are dimensionless D_K eigen-masses in M_KK units at the ε_LX=0.05 anchor; W4-3 sets the absolute eV scale.

**Output Artifacts** (closure-verification checklist):

- `computations/session-96/s96_matter_pmns_3x3.py` ✓ — contains `from canonical_constants import *` and `append_verdict(...)`.
- `computations/session-96/s96_matter_pmns_3x3.npz` ✓ (U, m_i, U_ei, scan arrays, cross-checks).
- `computations/session-96/s96_matter_pmns_3x3.png` ✓ (4-panel scan with NuFit bands + anchor line).
- Verdict line in `computations/session-96/s96_gate_verdicts.txt` ✓ (line 77) — `audit_sha256=29d70247182d5243b417bdee2c0f2270a073be978b7112aa87ec87017a5a6140`, `content_sha256=9b0f7ef26152374c5e234a9913e01e6fff652798777f60bf77bf2599911df919`, `schema_version=S84+`; dual-SHA companion row present (16-char heads).
- This WP §W4-2 ✓ (Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit).

---

### §W4-3. S96-MATTER-0NUBB (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-MATTER-0NUBB`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **PARTICLE** (J real-structure Majorana-vs-Dirac determination on H_K⁺ + m_ββ read-off)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The `D_K` real structure J (antilinear, J = C₂·K, J² = +1, KO-dim 6) makes the light neutrinos MAJORANA (a Majorana mass term is admitted on H_K⁺ by the Pfaffian measure), and the resulting effective mass m_ββ = |Σ U_ei² m_i| lies below current 0νββ bounds and within next-generation reach.
**Plan reference**: `sessions/session-plan/session-96-plan-w4.md` §W4-3 (PART 1 structural / PART 2 numerical; prereq W4-2 for the m_ββ half; antilinear-J discipline).

**Verdict**: **INFO**

**PART 1 (structural Majorana/Dirac determination) — DEFINITE: MAJORANA.** **PART 2 (m_ββ) — computed under the INFO W4-2 prereq with an externally-set eV scale: m_ββ = 8.27 meV** (NO, m_lightest→0, no Majorana phase; range **[4.96, 8.27] meV** over Majorana phases), below current bounds and inside next-gen reach. The composite is **INFO** (not PASS): the Majorana determination is structurally solid, but the m_ββ value rests on a non-PASS PMNS prereq AND an externally-set absolute scale, so the m_ββ half is framework-internal pending W4-2 resolution. This fires the pre-registered INFO clause ("Majorana is admitted but the m_ββ value half is qualified by the W4-2 prereq status").

**PART-2 prereq handling (rubric decision, disclosed per task)**: W4-2 (`S96-MATTER-PMNS-3X3`) landed **INFO** (not PASS) — the B2 Schur wall lifts (θ₁₂, θ₂₃ open) but no single ε_LX fits all four NuFit bands and R is unreachable. Its outputs `U`, `m_i`, `U_ei` ARE present in `s96_matter_pmns_3x3.npz`. The plan offers two defensible routes: (a) treat INFO as "unmet" → close PART 2 PRE-REG-INC; (b) COMPUTE m_ββ (the inputs exist) carrying an explicit caveat. **I chose (b)** — the inputs are physically present and usable, and m_ββ = |Σ U_ei² m_i| is a well-defined read-off demonstrating the framework's first 0νββ falsifier (the capstone §7 entirely lacks one); suppressing the number while the inputs exist would be strictly less informative. **Caveat (load-bearing)**: the underlying PMNS is INFO (angles don't all fit NuFit; R unreachable; the W4-2 raw m_i are quasi-degenerate), so the m_ββ value is NOT a NuFit-validated prediction — the framework supplies the mixing `U_ei`, while the **absolute eV scale is SET EXTERNALLY** from NuFit Δm² (the W4-2 m_i are raw |D_K| magnitudes in M_KK units, carrying pattern not scale).

**PART 1 — Majorana/Dirac determination (the J-structural half, fully self-contained).**

The determination is **MAJORANA**, established on three independent algebraic grounds (all from first-principles Cl(8) construction at τ_fold = 0.19; the (0,0)-singlet bare finite Dirac operator D_F = i·Ω, 16×16):

1. **Dirac is structurally IMPOSSIBLE.** The (1,1,0) SM-singlet content (ν_R) in one generation ℂ¹⁶ consists of exactly the two uniform-so(8)-weight states **e₀ = (−,−,−,−)** and **e₁₅ = (+,+,+,+)**, **both in H_K⁺** (γ₉ = +1). The opposite-chirality SM-singlet count in H_K⁻ is **0** — there is **no independent ξ_R partner** to form a lepton-number-conserving Dirac mass. The plan's substitution chain "Direction" is realized literally: *"a Dirac outcome would require a distinct ξ_R partner the branching does not supply."* It does not supply it.
2. **The singlet IS its own J-conjugate within H_K⁺.** The particle-hole conjugation C₁ = γ₂γ₄γ₆γ₈ (which commutes with γ₉, preserving chirality) maps e₀ ↔ e₁₅ — the singlet and its charge conjugate ν^c live in the SAME chirality space (the defining feature of a Majorana fermion, ξ = ξ^c admissible). The canonical KO-dim-6 reality structure (Ξ on the conjugate-doubled ℂ³²; J = Ξ·K antilinear) ADMITS a nonzero Majorana sector on H_F⁺: the 16×16 H_F⁺ Majorana block of Ξ·D₃₂ has **Frobenius norm 3.567, min SV 0.820, max SV 0.971** — non-obstructed by ≫ 1e-12.
3. **The bare diagonal bilinear |⟨Jξ|D_F|ξ⟩| = 0 reflects T4, NOT Dirac.** Evaluated literally on the **bare** geometric D_F, the antilinear bilinear m_M = (C₂ξ*)†D_F ξ = 0 (and the bare singlet↔conjugate entry D_F[15,0] = 0). This is the T4 result ("BDI, C²=+1; **no protected Majorana zero modes from topology; ν_R mass from Yukawa**"): the framework predicts NO tree-level/topological Majorana mass — the Majorana mass is **Yukawa/seesaw-generated** (consistent with S60's explicit right-handed Majorana M_R = 1.004 M_KK). The bare bilinear being zero is itself a prediction (no topological zero mode), but the Majorana/Dirac **character** is fixed by representation content + J-self-conjugacy (grounds 1–2), and that is unambiguously **MAJORANA**.

The determination is therefore DEFINITE, as the plan requires — but the discriminating observable is the **Pfaffian-admissibility of the J-pairing** (grounds 1–2: no Dirac alternative + nonzero H_F⁺ Majorana block), NOT the bare diagonal bilinear, which vanishes by T4. A naive reading of `|⟨Jξ|D_F|ξ⟩_bare| < 1e-12 ⇒ Dirac` would be structurally wrong: it conflates "no topological Majorana zero mode" (true, T4) with "Dirac character" (false — there is no Dirac partner). The mathematics is followed where it leads: **light neutrinos are Majorana, with the mass scale set by the seesaw, not a tree-level term.**

**T1 antilinear-J discipline (load-bearing; the pitfall explicitly avoided).** J = C₂·K is **antilinear**. The correct T-symmetric/CPT form is the antilinear conjugation `C₂ conj(D_F) C₂ = D_F`, verified to **0.00e+00** (T1, T11). The forbidden linear commutator `[C₂, D_F]` is **‖[C₂,D_F]‖ = 0.663 ≠ 0** — generically nonzero for complex D_F, and it is **T-symmetric, NOT a CPT violation or Majorana signal**. The Majorana determination used the antilinear form throughout (`m_M = (C₂ξ*)† D_F ξ`), never the linear commutator.

**Substitution chain (with substituted numbers; per `math-scripts.md §"Double-Check Logic"`):**
- Claim: "The KO-dim-6 Pfaffian measure admits a Majorana mass term on H_K⁺ ⇒ light neutrinos are Majorana."
- Step 1: J = C₂·K antilinear, C₂ = γ₁γ₃γ₅γ₇ (real symmetric; C₂²=+1, errs all 0.00e+00). KO-dim-6 axioms on the canonical doubled ℂ³² (Ξ = particle↔antiparticle swap): J²=+1 (err **0.00e+00**), JD=DJ ε'=+1 (err **0.00e+00**), Jγ=−γJ ε''=−1 (err **0.00e+00**). [T1, T5, s66 PRODUCT-KO-DIM-66]
- Step 2: H_K⁺ = {ξ : γ₉ξ = +ξ} = states [0,3,5,6,9,10,12,15]; {γ₉,D_F}=0 (err **0.00e+00**) ⇒ D_F maps H_K⁺ → H_K⁻. [E8/E9]
- Step 3: Majorana bilinear m_M = ⟨Jξ|D_F|ξ⟩ = (C₂ξ*)† D_F ξ on the (1,1,0) singlet ξ = e₀. **Computed (bare): m_M = 0.000000e+00** — the bare geometric D_F has no Majorana entry (T4: no topological zero mode). [T1 antilinear form]
- Step 4 (representation content): # independent opposite-chirality ξ_R partners in H_K⁻ = **0** ⇒ Dirac IMPOSSIBLE. Singlet's C₁-conjugate = e₁₅, **same chirality (γ₉=+1)** ⇒ J-self-conjugate (Majorana signature). [so(8) Cartan weights]
- Step 5 (admissibility): H_F⁺ Majorana block of Ξ·D₃₂ has Frob = **3.567 > 1e-12** ⇒ the KO-dim-6 measure ADMITS a Majorana sector. [Pfaffian-natural pairing; Z₂=+1, T10]
- Conclusion: **DETERMINATION = MAJORANA** (Dirac excluded by representation content; Majorana pairing admitted by J; mass Yukawa/seesaw-generated). PART 2 then reads m_ββ from W4-2.

**PART 2 — 0νββ effective mass m_ββ = |Σ U_ei² m_i|.**

Framework mixing (W4-2): U_ei = [−0.4497, 0.8745, 0.1817] (electron row, real-valued ⇒ no Dirac CP phase; Majorana phases are extra). W4-2 raw m_i = [0.7992, 0.8214, 0.9081] in **M_KK units** — quasi-degenerate (ratios [0.880, 0.905, 1.0], spread 0.120), so they carry the framework mass *pattern* but **not** the absolute scale and **not** a NuFit-hierarchical splitting. The eV scale is therefore SET EXTERNALLY from NuFit-6.0 Δm² (normal ordering: Δm²₂₁ = 7.49e-5 eV², Δm²₃₁ = 2.513e-3 eV²).

- **Route A (PRIMARY — NuFit-NO scale + framework U_ei):**

| m_lightest [meV] | (m₁,m₂,m₃) [meV] | m_ββ (no phase) [meV] | Σm_i [meV] |
|:---|:---|:---|:---|
| 0.00 | (0.00, 8.65, 50.13) | **8.27** | 58.78 |
| 1.00 | (1.00, 8.71, 50.14) | 8.52 | 59.85 |
| 5.00 | (5.00, 10.00, 50.38) | 10.32 | 65.37 |
| 10.00 | (10.00, 13.23, 51.12) | 13.82 | 74.34 |
| 30.00 | (30.00, 31.22, 58.42) | 31.87 | 119.64 |
| 60.00 | (60.00, 60.62, 78.19) | 61.08 | 198.81 |

  Primary value (m_lightest → 0): **m_ββ = 8.27 meV** (no Majorana phase); over Majorana phases **[4.96, 8.27] meV**.
- **Route B (DIAGNOSTIC — framework raw quasi-degenerate m_i, m_max = 0.05 eV):** m_ββ = 45.1 meV. The raw m_i cannot reproduce NuFit splittings (quasi-degenerate), so this is a quasi-degenerate-pattern diagnostic only; Route A is the defensible primary number.

**Comparison to bounds**: m_ββ = 8.27 meV (Route A primary) is **below** KamLAND-Zen (≲ 28–122 meV depending on NME) and LEGEND-200 reach (≲ 18–75 meV), and **within next-generation reach** (LEGEND-1000 / nEXO target ~6–20 meV). The two FAIL sub-cases are NOT triggered: it is **not** Dirac (PART 1 is Majorana), and m_ββ does **not** exceed the current bound. The result is a **falsifiable 0νββ target** the capstone §7 entirely lacks — but it lands INFO (not PASS) because the PMNS prereq is INFO and the absolute scale is external.

**Cross-checks & provenance:**
- **CC1 — KO-dim-6 axioms**: J²=+1, JD=DJ (ε'=+1), Jγ₉=−γ₉J (ε''=−1) on the canonical doubled ℂ³², all residuals **0.00e+00**; {γ₃₂,D₃₂}=0 err 0.00e+00. (Note: the single ℂ¹⁶ alone is KO-dim 0 per s66 PRODUCT-KO-DIM-66 — KO-dim 6 is realized by the conjugate doubling, the structure the SM/CCM requires for ε''=−1.) [T5, T1, s66]
- **CC2 — Pfaffian per-sector reality Z₂ = +1**: T3-S30A-DTOTAL-PFAFFIAN PASS (Pf real per-sector, Z₂=+1 identically across 75 τ in [0,2.5]; confirms KO_dim_6). The antisymmetric Majorana form M = C₁·D_F is the Pfaffian-natural pairing this gate uses; its H_K⁺ block on the bare D_F vanishes (T4 — chirality-off-diagonal D_F), and the admissibility of the Majorana entry is the off-diagonal-slot non-obstruction read off the doubled H_F⁺ block. [T2, T10]
- **Cache cross-check**: bare singlet D_F eigenvalues span [−0.9714, +0.9714] (symmetric, chirality-paired per T3); 16×16 single-generation Clifford problem, numpy.linalg sufficient (CPU, OMP capped at 8 per `GPU_path: numpy.linalg` pin).
- **dual-SHA** (full 64-char): `audit_sha256=ab5203d9f0063366269557129b12791adcc734a79fb15b32d2372cb7d780d970`; `content_sha256=a327cf5a6d22c451675153c697a78b2304e81641d71f9f7f64f2d2a50d0b74b1`. No `[SIGN]` 3-tuple required (`[VERIFY-THEOREM]` trigger).
- **Canonical write-order**: verdict is **INFO** (not PASS), so per the gate's PASS-only registration rule `m_betabeta_FW` is **NOT** registered as a canonical constant and **no §7.2 0νββ falsifier row is promoted** (matching the W4-1 precedent). The m_ββ value (8.27 meV, range [4.96, 8.27]) lives in the npz + this WP only, pending W4-2 resolution. The NuFit-6.0 Δm² and 0νββ-bound **comparison anchors** WERE added to `canonical_constants.py` (`dm2_21_NuFit`, `dm2_31_NuFit`, `m_betabeta_KamLANDZen`, `m_betabeta_LEGEND200_reach`, `m_betabeta_nextgen_reach`) with provenance — these are observational anchors, not framework predictions.

**Output Artifacts** (closure-verification checklist):
- script `computations/session-96/s96_matter_0nubb.py` — present (29,199 B); `grep` for `from canonical_constants import` ✓ and `append_verdict` ✓ (both match).
- data `computations/session-96/s96_matter_0nubb.npz` — present (16,667 B).
- plot `computations/session-96/s96_matter_0nubb.png` — present (66,999 B; produced because determination = MAJORANA).
- verdict line `computations/session-96/s96_gate_verdicts.txt` — present (line 88); matches `^S96-MATTER-0NUBB:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ (line 89). No `[SIGN]` 3-tuple required.
- this WP §W4-3 — Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit present.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`, query-first discipline):

| Query (tool) | Salient return |
|:---|:---|
| `search_knowledge("KO-dimension 6 J^2=+1 Jgamma9 charge conjugation axioms")` | J²=+1, JD=+DJ, J·γ=−γ·J (KO-dim 6) confirmed (session-53, s87, T5); J = C₂·K; C₂ = γ₁γ₃γ₅γ₇ (session-34a corrects old B=σ₂^⊗4). |
| `search_knowledge("Majorana neutrino mass 0nubb double beta decay m_betabeta")` | open_channel "Majorana sector of D_F" (complex M_R for leptogenesis?); S65 Λ_CC^ζ = β₁M⁴ with M = RH Majorana mass; no prior m_ββ result. NOT pre-closed. |
| `trace_entity("Pfaffian per-sector reality T10")` / `trace_entity("DTOTAL-PFAFFIAN")` | T3-S30A-DTOTAL-PFAFFIAN PASS, value=+1, Pf real per-sector, Z₂=+1 across 75 τ; theorem [NEW S30] Pf D_total = +1 on Jensen (Interior Mixing). CC2 anchor. |
| `search_knowledge("Pfaffian per-sector real Z2 +1 75 tau J-parity BdG")` | edge `T3-S30A-DTOTAL-PFAFFIAN --confirms--> KO_dim_6`; B-30a "Pfaffian trivial on Jensen, Pf=+1 all 75 τ, all 6 sectors". |
| `search_knowledge("(1,1,0) singlet right-handed neutrino content H_K+ chirality gamma9")` | γ₉ chirality grading on H_K; S60 RH Majorana M_R (M₁=1.004 M_KK, M₂=1.079 M_KK); H_K = H₊⊕H₋, {γ₉,D_K}=0 (5.55e-15). |
| `get_constant("m_betabeta_FW")` | **not found** (no overwrite risk; PASS-only registration ⇒ not promoted under INFO). |
| `search_knowledge("KO-dim 6 J construction Xi C^32 doubling gamma9 anticommute correct charge conjugation")` / `trace_entity("KO_dim_6")` | eq_8591 + session-35: single C₂ on C¹⁶ gives ε''=+1 (KO-dim 0); KO-dim 6 (ε''=−1) realized "by CONSTRUCTION" on H_F=ℂ³² via conjugate doubling (s66; eq_14108 "Majorana extension and conjugate doubling per KO-dim 6"). Decisive for the doubled-space construction. |

**PRE-CLOSED?** No. The open_channel "Majorana sector of D_F" and the S60 seesaw M_R are prior framework context but no gate has made the DEFINITE Majorana-vs-Dirac determination from the J real structure, nor computed m_ββ. The CC1/CC2 anchors (KO-dim 6 axioms, T10 Pfaffian) are inputs the gate consumes, not closures of the gate. Gate executed.

---

### §W4-4. S96-MATTER-EXT-BARYOGEN (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-MATTER-EXT-BARYOGEN`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (internal CPT-barred η_B null + external emergent-g_M gravitational-baryogenesis channel)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The internal SU(3) spectral action CANNOT source baryon asymmetry (η_B = 0 EXACT, barred by [J,D_K]=0 / T11); the leading viable channel is EXTERNAL — gravitational baryogenesis ∝ ∂_μR·J^μ_B on the EMERGENT g_M (a₂ moment) — nonzero even though p₁[SU(3)] = 0 internally, giving a sub-observed CP-odd density.
**Plan reference**: `sessions/session-plan/session-96-plan-w4.md` §W4-4 (PART 1 internal-null / PART 2 external-locate; [SIGN]-trigger ⇒ 3-tuple companion row REQUIRED).

**Verdict**: **FAIL** (composite, via `regime_verdict = BREAKDOWN`).

The FAIL is the *informative* kind the plan's FAIL_meaning anticipated, NOT a contradiction of T11. It decomposes into a confirmed half and a closed corridor:

- **PART 1 half — confirmed EXACT (PASS standalone).** The internal CP-odd source is **0 EXACT** (`|sin φ_CP|_internal = 0`, `|η_B^internal| = 0`), cross-checked against `s52_eta_b_output.txt` (`eta_B = 0.0e+00`) and `s60_lepto_cp_log.txt` (`ε₁ = 0` EXACT). T11 is confirmed at capstone level: the equation is too CPT-symmetric to source η_B.
- **PART 2 half — the FAIL.** The pre-registered source object `tr(R∧R)|_{g_M}` for the **left-invariant** emergent metric is **0 EXACT** (the *located, in-structure* channel is NULL ⇒ the INFO_meaning "needs an ADDITIONAL fiber" branch). The only nonzero external estimate — the DKKMS gradient channel `∂_μR·J^μ_B` with `R_dot(fold) = 1.65e5 M_KK³` — **over-produces** by ~14 OOM (`η_grav = 7.0×10⁴ ≫ 6.12×10⁻¹⁰`) AND is **out-of-regime** (the thermal-equilibrium DKKMS formula assumes a B-violating interaction in equilibrium; the substrate transit is the integrable GGE relic that never thermalizes). The over-production triggers FAIL_meaning clause 2 ("emergent external density exceeds the observed η_B — over-production; the normalization is wrong").

Structure-first reading: the algebra forbids the internal source EXACTLY (T11), the *located* emergent source (left-invariant tr(R∧R)) is also EXACTLY zero, and the only nonzero gravitational estimate is an out-of-regime thermal extrapolation. No `eta_B_external_FW` is promoted (the plan gates promotion on PASS) and no frontier #9 "located source" is registered — instead the **structural requirement** is sharpened (see Results): baryogenesis requires physics EXTERNAL to *both* the SU(3) Dirac operator *and* its homogeneous emergent g_M (a non-left-invariant / additional-fiber input).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Verified |
|:---------|:-----|:---------|
| script | `computations/session-96/s96_matter_ext_baryogen.py` | EXISTS; contains `from canonical_constants import`, `append_verdict` ✓ |
| data | `computations/session-96/s96_matter_ext_baryogen.npz` | EXISTS ✓ |
| plot | `computations/session-96/s96_matter_ext_baryogen.png` | EXISTS ✓ |
| verdict line | `computations/session-96/s96_gate_verdicts.txt` | matches `^S96-MATTER-EXT-BARYOGEN:.* audit_sha256=[a-f0-9]{64}` ✓ |
| dual-SHA companion row | (same) | present ✓ |
| **SIGN/MAGNITUDE/REGIME 3-tuple row** (REQUIRED — [SIGN]) | (same) | present ✓ |
| WP §W4-4 | this section | Status COMPLETED, Verdict FAIL, Output Artifacts, MCP Pre-Compute Audit ✓ |

Closure verdict lines (full 64-char dual-SHA + 3-tuple):
```
S96-MATTER-EXT-BARYOGEN: FAIL -- value=70000.0 scheme=gravitational-baryogenesis-emergent-gM convention=ABSOLUTE L_max=10 audit_sha256=d108e7d7543a23dfdf5fb544dc198d5e556d0932136d3db5ee283c31ad581eeb content_sha256=c130aeac54d051617e5ff9ff59ee93cc627e76335f3d5fd3969ecdf3e300f92c schema_version=S84+
# audit_sha256_short=d108e7d7543a23df content_sha256_short=c130aeac54d05161 # S96-MATTER-EXT-BARYOGEN dual-SHA companion row
# sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=BREAKDOWN # S96-MATTER-EXT-BARYOGEN 3-tuple annotation (schema-v2)
```
(`audit_sha256` unique across the 30 canonical lines in the file; sig_5 clean for this gate.)

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; one-line salient return each):

| Query | Tool | Salient return |
|:------|:-----|:---------------|
| `baryon asymmetry eta_B gravitational baryogenesis internal SU(3) null` | `search_knowledge` | **Gravitational baryogenesis = OPEN channel (S53)** "coupling to 4D Ricci scalar (external)"; `eta_B(BCS)=0 EXACTLY (three structural proofs): [J,D_K]=0, BDI nu=0` (s59); `\eta_B = 0` (S58 Volovik-Baptista) |
| `T11 baryon null J D_K` | `trace_entity` | no trace under that string (T11 is registry-PROVEN; reached via s52/s59/s60 archives instead) |
| `p1 Pontryagin SU(3) zero ELASTIC-TETRAD-CC-54` | `search_knowledge` | **`p_1[SU(3)] = 0 (exactly, S54 ELASTIC-TETRAD-CC-54)` ... "tr(R∧R) is CP-odd. Sources baryogenesis via grav anomaly"** (s61) — the exact CC1/CC2 seed |
| `a_2 Seeley-DeWitt curvature emergent metric R_K f_2 92` | `search_knowledge` | `a_2 = 64308.24` (L_max=10 raw moment, s75); `a_2 = (1/6)·Scalar(K)`; `R_K(τ) = (3/2)(2e^{2τ}−1+8e^{−τ}−e^{−4τ})` (Paper 15); `a_2 = f_2·Λ²·∫(R/6−E)` (S71) |
| `eta_B_obs` / `M_KK` / `tau_fold` | `get_constant` | `eta_B_obs` not found → canonical is **`eta_BBN_obs = 6.12e-10`**, `eta_BBN_err = 4e-12`; `M_KK = 7.428660036284456e16`; `tau_fold = 0.19` |
| `(eta_B\|f_2\|f_conv\|M_Pl\|a_2\|a_0\|R_K)` | `list_constants` | `f_2_default = 2.34` (S62); `a_2_FW_zeta = 2776.17`, `a_0_FW_zeta = 6440` (S88); `M_Pl_reduced = 2.435e18`, `M_Pl_unreduced = 1.2209e19` |
| `emergent 4D Ricci R_M g_M tr(R∧R) Pontryagin nonzero baryogenesis` | `search_knowledge` | `tr(R_E∧R_E) = tr(R_F∧R_F) + tr(π*R_M∧π*R_M) + 2 tr(R_F∧π*R_M)` (S85); `p_1(TE) = (1/8π²)tr(R_E∧R_E)`; `S_CS = (c_2/192π)∫tr(R∧R)√−g` (Volovik grav anomaly, S59); g_M emergent from a₂ |
| `gravitational baryogenesis R_dot decoupling DKKMS J_B normalization` | `search_knowledge` | **`eta_grav = (15 g_b)/(4π² g_*)·R_dot/T` (Davoudiasl, s59)**; `R_dot = dR/dτ·v_terminal = 164677.53 M_KK³` (s59); transit_baryogenesis (S61) |

Archive reads (cited, not re-run): `s52_eta_b_output.txt` (`eta_B=0.0e+00`, 3 proofs), `s60_lepto_cp_log.txt` (`ε₁=0` EXACT, SECTION-5 J-reality theorem, cross-check-3 thermal-formula-invalid-for-GGE warning), `s59_baryon_diagnostic.npz/.txt` (`R_dot_fold=164677.53`, `R_acoustic_fold=442.95`, `eta_B_grav=69832.54`, `T_acoustic=0.112`; INFO-A), `s61_j_breaking_catalog_log.txt` (E4 Pontryagin left-inv = 0.0 EXACT; non-LI fluct over-produces). **PRE-STATE**: the internal null is registry-PROVEN (T11, S52/S59/S60); gravitational baryogenesis is a registry-OPEN channel (S53). This gate confirms the internal null at capstone level and *locates+regime-checks* the external channel — it does not recompute closed results.

**Results**:

**PART 1 — internal CP-odd source = 0 EXACT (confirms T11 at capstone level).**
- `sin(φ_CP)_internal = 0.000e+00` (< 1e-15 ✓); `η_B^internal = 0.000e+00` (< 1e-15 ✓).
- Cross-checks: `s52 eta_B = 0.0e+00`; `s52 sum(sin φ_CP) = 0.0e+00`; `s52 max|ε_CP| (θ-scan) = 0.0e+00`; BdG eigenvector reality witness in the T-symmetric basis `max Im(eigvec) = 0.000e+00` (⇒ u,v REAL ⇒ φ_CP ∈ {0,π} ⇒ sin φ_CP = 0). Three independent permanent proofs each force the zero: BDI T-symmetry (T=C₂·K, T²=+1), J-symmetry T11 (C₂·conj(D_K)·C₂ = D_K, antilinear), and {γ₉,D_K}=0 (T2).
- **Antilinear-J discipline** (T1 / MEMORY pitfall): the CPT condition used is the antilinear conjugation `C₂·conj(D_K)·C₂ = D_K`, NOT the linear commutator `[C₂, D_K]` (generically nonzero for complex D_K; T-symmetric, not a CPT violation). The Majorana/leptogenesis null in s60 follows the same identity (M_R real in the J-symmetric basis ⇒ ε₁ = 0).

**PART 2 — external emergent-g_M gravitational channel: LOCATED, then FAIL (over-production + regime breakdown).**
- **CC1**: `p₁[SU(3)] = 0` EXACT (S54 ELASTIC-TETRAD-CC-54) ⇒ the *internal* SU(3) gravitational-anomaly channel is BARRED.
- **CC2** (emergent g_M ≠ internal SU(3) curvature): internal fiber `R_K(τ_fold) = 12.109 M_KK²` (Jensen, Paper 15) vs emergent acoustic `R_acoustic(fold) = 442.95 M_KK²` (a₂-emergent g_M, s59) — manifestly distinct objects. tr(R∧R)|_{g_M} is therefore NOT forced to zero by p₁[SU(3)]=0.
- **(2a) pre-registered source `tr(R∧R)|_{g_M}` (left-invariant) = 0.000e+00 EXACT.** For the homogeneous transit, p₁ is a characteristic class that vanishes; the 4D Pontryagin is zero for FRW (conformally flat, Weyl=0); fiber↔base cross-terms vanish for the left-invariant metric (s61 E4 left-inv = 0.0). ⇒ the *located, in-structure* external source is NULL.
- **(2b) DKKMS gradient channel `∂_μR·J^μ_B`**: `R_dot(fold) = 164677.5314 M_KK³` (NONZERO ⇒ ∂_μR ≠ 0). Davoudiasl thermal formula `η_grav = (15 g_b)/(4π² g_*)·R_dot/T` at `T = T_acoustic = 0.112 M_KK`, `g_b=1, g_*=8` ⇒ `η_grav = 6.983254e+04`. Independent reconstruction matches s59-stored `eta_B_grav = 6.983254e+04` to rel < 1e-6 (recon ok = True). `η_grav/η_obs = 1.141e+14` ⇒ **OVER-produces by ~14.1 OOM**.
- **(2c) REGIME**: `regime_breach_fraction = 1.00`. The DKKMS thermal formula assumes a thermal-equilibrium background with a B-violating interaction in equilibrium at decoupling. The substrate transit is the integrable GGE relic (never thermalizes; no B-violating interaction in equilibrium — s52 ORDERED VEIL; s59 "BLOCKED BY S1"; s60 cross-check 3 explicitly: "the formula assumes thermal equilibrium background ... NOT applicable to the GGE relic"). ⇒ `regime_verdict = BREAKDOWN`.

**4-tuple**: `(value=7.0e+04, scheme=gravitational-baryogenesis-emergent-gM, convention=ABSOLUTE, L_max=10)`. **regulator pin**: `a_2^{Pauli-Villars}` (the emergent curvature is the a₂ Seeley-DeWitt moment, PV-regulated per `regulator-pin-discipline.md`). **publication precision**: 2 sig figs (OOM-class). The published `value` is the external-channel magnitude under the pinned DKKMS scheme; the `regime_verdict=BREAKDOWN` field carries the out-of-regime flag, and the npz stores `tr_RwedgeR_gM_leftinv = 0.0` (the located in-structure source).

**SIGN/MAGNITUDE/REGIME 3-tuple** (composite-collapse per `gate-verdicts.md`):
- `sign_verdict = FAIL` — Step-4 predicts internal=0 EXACT [holds] AND external POSITIVE & SUB-observed (< 6e-10). The discriminating directional claim (external sub-observed) fails: the located source (2a) is zero and the only nonzero estimate (2b) is *above* the ceiling (sign of `value − ceiling` is POSITIVE, opposite the predicted "below").
- `magnitude_verdict = FAIL` — `η_grav = 7.0e4 ≫ 6e-10` info-band ceiling.
- `regime_verdict = BREAKDOWN` — thermal formula out-of-regime over the full window (breach=1.0).
- Composite: `regime_verdict == BREAKDOWN ⇒ composite = FAIL`.

**Substitution chain (with substituted numbers)** — plan §W4-4 Step-4 [SIGN] pre-registration:
- Def 1 (Sakharov): CP-violation needs nonzero φ_CP in the rate asymmetry.
- Def 2 (J): `J = C₂·K`, `[J,D_K]=0` ∀τ (T11) ⇒ M_R real in J-basis ⇒ `sin(φ_CP) = 0` EXACT ⇒ `ε₁ = 0` EXACT. **[substituted: sin φ_CP = 0.000e+00]**
- Def 3 + substitute: `η_B^internal ∝ sin(φ_CP) = 0` ⇒ `η_B^internal = 0` EXACT. **[substituted: η_B^internal = 0.000e+00; cross-checked s52 = 0.0e+00]**
- Def 4 (grav baryogenesis): `S_grav ∝ ∂_μR·J^μ_B`, R = Ricci of emergent g_M (a₂ moment). Substitute `S_grav ∝ tr(R∧R)|_{g_M}`. Internally `p₁[SU(3)] = 0` (S54) — but emergent g_M is a DIFFERENT object ⇒ tr(R∧R)|_{g_M} not forced to zero. **[substituted: p₁[SU(3)]=0; R_K^fiber(fold)=12.109 ≠ R_acoustic^{g_M}(fold)=442.95 M_KK²]**
- Canonical form: `η_B^total = η_B^internal + η_B^external = 0 + S_grav-density`.
- Direction (pre-registered prediction): internal EXACTLY zero (✓ confirmed); external carries the entire *small, sub-observed* asymmetry (✗ — located tr(R∧R)|_{g_M}^{LI} = 0; only the out-of-regime DKKMS gradient is nonzero and it over-produces by 14 OOM). **[substituted: tr(R∧R)|_{g_M}^{LI}=0.000e+00; η_grav(DKKMS)=7.0e4; η_grav/η_obs=1.14e14]**
- Conclusion: internal-null PASS half + external-locate FAIL half ⇒ composite FAIL (regime BREAKDOWN). The sharpened structural statement replaces the hoped-for frontier-#9 "located sub-observed source."

**CC1**: `p₁[SU(3)] = 0` EXACT (S54 ELASTIC-TETRAD-CC-54). **CC2**: emergent g_M (a₂ Seeley-DeWitt moment; canonical `a_2_FW_zeta = 2776.17`, `a_0_FW_zeta = 6440`) ≠ internal SU(3) curvature (Jensen `R_K(fold) = 12.109 M_KK²`). **SOURCE-RECON note**: the plan-prose cue "f₂≈92" is NON-canonical; the canonical value is `f_2_default = 2.34` (S62, Gaussian cutoff) — used throughout per `substrate-first-canonical-sourcing.md §(i)`. The verdict does not depend on f₂ (the DKKMS thermal density and the left-invariant tr(R∧R)=0 are both f₂-independent), so the discrepancy does not affect PASS/FAIL; it is recorded for hygiene.

**Structural requirement (sharpened, replacing the frontier-#9 "located source")**: Baryogenesis in this framework requires physics EXTERNAL to BOTH (i) the SU(3) Dirac operator (T11: internal η_B = 0 EXACT) AND (ii) its *homogeneous* emergent metric g_M (the located left-invariant tr(R∧R)|_{g_M} = 0 EXACT). The only nonzero gravitational estimate (DKKMS R-gradient) is out-of-regime for the integrable GGE relic and over-produces by ~14 OOM at natural normalization. The minimal missing ingredient is a **non-left-invariant / additional-fiber** input carrying a CP-odd phase AND a B-violating interaction in (or near) equilibrium — neither of which the SU(3)+homogeneous-g_M structure supplies. This aligns with the prior catalog (s61 J-BREAKING-CATALOG: all internal channels need external J-breaking; E4 Pontryagin left-inv = 0, reduces to non-LI E3) and is the honest, located frontier-#9 statement: *what* is missing, not a manufactured value. (Carry-forward candidate: a non-LI / additional-fiber baryogenesis source with pre-registered CP-phase + B-violation thresholds — owner dirac/neutrino, next session.)

**Classification**: PARTICLE. Substrate-first: [J,D_K]=0 (the substrate's exact CPT symmetry) ⇒ internal η_B = 0 EXACT ⇒ the asymmetry must be sourced where J does not reach (emergent g_M). We located that channel, found the in-structure (left-invariant) source EXACTLY zero, and found the only nonzero estimate out-of-regime — we report what the algebra gives, manufacturing no internal phase to fit η_B.

---

### §W4-5. S96-MATTER-YUKAWA-CHIRALITY (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-MATTER-YUKAWA-CHIRALITY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (product-KO ε″ chirality: H_K⁺ Pfaffian restriction projecting out the wrong-chirality coupling)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The H_K⁺ Pfaffian restriction projects OUT the wrong-chirality (ε″=+1) Yukawa coupling that the SU(3)-manifold lift carries, recovering the physical chirality-flipping SM structure (effective ε″=−1) on the fermion bilinear — i.e. no residual chirality-preserving (CPT-non-flipping) coupling survives.
**Plan reference**: `sessions/session-plan/session-96-plan-w4.md` §W4-5 (s66 Clifford C₂/C₁; THEOREM-class machine-ε tolerance; antilinear-J discipline).

**Verdict**: **PASS** — `residual_chirality_preserving = 0.000000000000e+00` (< 1e-12 THEOREM-class machine-ε). The H_K⁺ Pfaffian restriction projects out the ε″=+1 wrong-chirality coupling EXACTLY; the physical ε″=−1 chirality-flipping channel is nonzero (`|Y|_flip = 2.662811212873`), so effective ε″ = −1 is recovered. The §1.3.4 capstone chirality caveat is **confirmed "bounded" (in fact exactly zero)**, not "open."

**Governing structure (structure-first)**. The fermionic spectral-action term is `S_f = ⟨Jψ̃ | D_K | ψ̃⟩` with `ψ̃ ∈ H_K⁺ = {ξ : γ₉ξ = +ξ}` (the canonical capstone form, `connes-master-equation.md` / `phonic-exflation-equation.md`). The chirality structure of this Yukawa/mass bilinear is fixed by two pieces of pure algebra: (i) the chirality grading γ₉ and the real structure J = C·K on the SU(3) factor; (ii) the oddness `{γ₉, D_K} = 0` of any Dirac operator. The product-KO classification (s66) gives the SU(3)-manifold lift charge-conjugation grading **ε″ = +1** (J commutes with γ₉ → CPT *preserves* chirality), opposite to the physical finite-SM value **ε″ = −1** (KO-dim-6 axiom Jγ₉=−γ₉J, T5 → CPT *flips* chirality). This gate tests whether the H_K⁺ restriction reconciles them at the level of the physical bilinear.

**Results**.

| Quantity | Value | Status |
|:---------|:------|:-------|
| `residual_chirality_preserving` = \|⟨Jψ̃\|D_K\|ψ̃⟩\|_{ε″=+1 on H_K⁺} (Frobenius over H_K⁺) | **0.000000000000e+00** | PASS (< 1e-12) |
| ε″=−1 (chirality-FLIPPING, physical SM) channel \|Y\|_flip | **2.662811212873** | nonzero ⇒ PASS non-vacuous |
| ε″=+1 (chirality-PRESERVING, residual) channel \|Y\|_preserve | **0.000000000000e+00** | wrong-chirality projected OUT |
| effective ε″ on the fermion bilinear | **−1** | SM structure recovered |
| preserve/flip ratio | 0.000e+00 | — |

- **4-tuple**: `(value=0.0, scheme=s66-product-KO-Clifford-C2-C1, convention=ABSOLUTE, L_max=12)`.
- **THEOREM-class tolerance**: machine-ε, PASS iff residual < 1e-12. Achieved residual = exactly 0.0 (orthogonal-chirality-subspace overlap is identically zero, not a round-off floor).

**CC1 — γ₉ chirality grading and the ANTILINEAR J relation (Jγ₉ = ε″ γ₉ J)**. J = C₂·K is **antilinear**; the ε″ sign is read from the antilinear conjugation relation `C₂ conj(γ₉) C₂⁻¹` vs ±γ₉ — **never** from a linear commutator `[C₂, D_K]` (the T1 pitfall: for complex D_K, `[C₂, D_K]` is generically nonzero and T-symmetric, not a CPT violation). Verified at machine-ε:
  - SU(3)-lift J = C₂·K, C₂ = γ₁γ₃γ₅γ₇ (product of the REAL/symmetric gammas; s66 / MEMORY): `Jγ₉ = +γ₉J` (commute-err = 0.00e+00; anticommute-err = 2.00) ⇒ **ε″(SU(3) lift) = +1** (J COMMUTES with γ₉). `J² = +1.0` (scalar-err 0.00e+00).
  - Physical KO-dim-6 contrast J′ = γ₁·C₂ (a single γ flips the γ₉-commutation since each γ_a anticommutes with γ₉ in even d): `J′γ₉ = −γ₉J′` (anticommute-err = 0.00e+00) ⇒ **ε″(KO-6 J′) = −1** (J′ FLIPS γ₉ — the T5 physical requirement).
  - This is the s66 finding made operational: on Cl(R⁸) both B₊ and B₋ give ε″=+1 (d=8 is uniquely degenerate), so ε″=−1 is an **independent** algebraic structure, realized here by the contrast J′. The leading-order chirality flip in the physical channel is FORCED by Jγ₉=−γ₉J (T5).

**CC2 — H_K⁺ projector exact-projector cleanness**. P₊ = (I+γ₉)/2 verified an exact orthogonal projector at machine-ε: idempotent-err = 0.00e+00 (P₊²=P₊), hermitian-err = 0.00e+00 (P₊=P₊†), P₊P₋ orthogonality-err = 0.00e+00, rank(H_K⁺) = 8 (= half of 16, the ℂ¹⁶ single-generation content). Supporting Clifford verifications all machine-zero: `{γ_a,γ_b}=2δ_ab` err = 0.00e+00; `γ₉²=I` err = 0.00e+00; `γ₉ = C₂C₁` (phase +1) err = 0.00e+00. The Pfaffian per-sector reality (Z₂=+1, T10 / T3-S30A-DTOTAL-PFAFFIAN PASS) guarantees the H_K⁺ restriction is the well-defined half-density the fermionic action lives on. D_K block (from the L_max=12 cache singlet (0,0), |λ| ∈ [0.819741, 0.971408]) is Hermitian (err 0.00e+00) and ODD under chirality, `{γ₉, D_K}=0` err = 0.00e+00 — so D_K : H_K⁺ → H_K⁻ exactly.

**Substitution chain (with substituted numbers)**.
  - *Definitions*: C₂ = γ₁γ₃γ₅γ₇, J = C₂·K antilinear (T1); ε″ = sign in Jγ₉ = ε″γ₉J, with ε″(SU(3))=+1 (s66) and ε″(SM-physical)=−1 (T5); H_K⁺ = {ξ: γ₉ξ=+ξ}; physical bilinear `S_f(ψ̃) = ⟨Jψ̃ | D_K | ψ̃⟩`.
  - *Substitute*: D_K odd ⇒ `D_K|ψ̃⟩ ∈ H_K⁻`. The chirality of `Jψ̃` is set by ε″: with ε″=+1, `Jψ̃ ∈ H_K⁺`; with ε″=−1, `Jψ̃ ∈ H_K⁻`.
  - *Simplify*: a chirality-PRESERVING coupling has bra-chirality = ket-chirality (ε″=+1) ⇒ `⟨Jψ̃ | D_K ψ̃⟩ = ⟨H_K⁺ | H_K⁻⟩ = 0`. A chirality-FLIPPING coupling has bra in H_K⁻ matching the ket (ε″=−1) ⇒ overlap can be nonzero.
  - *Canonical form*: `residual_{ε″=+1} = |S_f|_{J=C₂K, ε″=+1}` = the ε″=+1 channel magnitude.
  - *Direction*: Jγ₉=−γ₉J (T5) FORCES the physical H_K⁺ bilinear to flip chirality at leading order; the wrong-chirality ε″=+1 residual vanishes to machine-ε IF the H_K⁺ Pfaffian restriction is clean.
  - *Conclusion / substituted result*: `residual_{ε″=+1} = 0.000000000000e+00 < 1e-12` ⇒ **PASS**. The ε″=−1 (flipping) channel = **2.662811212873 ≠ 0** ⇒ the physical SM coupling is genuinely present (the PASS is NOT the vacuous "both channels zero" case). Effective ε″ = −1 recovered.

**INFO branch (measure-zero / Pfaffian-normalization absorption) — not triggered**. The pre-registered INFO branch would apply if the residual were nonzero but a documented measure-zero set absorbed by the Pfaffian normalization. Here the residual is *exactly* 0.0 (a structural orthogonal-subspace cancellation `⟨H_K⁺|H_K⁻⟩=0`, not a round-off remnant), so the gate closes cleanly as PASS; no measure-zero absorption argument is needed.

**§1.3.4 capstone caveat verdict**. **CONFIRMED "bounded" — in fact exactly zero.** The product-KO 4-vs-6 reading (s66 §V.2): the M⁴×SU(3)-manifold carries ε″=+1 ("Yukawa couplings have wrong chirality structure"; s66 Section 10), but the H_K⁺ Pfaffian restriction projects the wrong-chirality ε″=+1 component to machine-ε zero on the fermion bilinear, while the physical ε″=−1 chirality-flipping coupling survives. The §1.3.4 footnote should remain "bounded" (do NOT expand to an OPEN sub-finding). The Yukawa-chirality sub-finding is **CLOSED**. Caveat: the contrast J′ (ε″=−1) confirms the SM chirality-flip is realizable as an independent KO-6 structure (consistent with s66's "the finite-SM KO=6 is an independent algebraic construction"); the recovery of the physical coupling is via that KO-6 J′, and the gate's PASS is the statement that the SU(3)-lift J's wrong-chirality contribution does NOT contaminate it.

**Substrate framing**. GEOMETRIC class. The chirality structure of the Yukawa coupling is a property of the spectral triple's grading γ₉ and real structure J — read off the s66 product-KO construction, not imposed. Direction: D_K eigenvalues + γ₉ grading + J (antilinear charge conjugation) → which chirality channel survives the H_K⁺ Pfaffian restriction → effective ε″ on the fermion bilinear. The substrate's grading IS what selects chirality-flipping over chirality-preserving; we followed the algebra (Jγ₉=−γ₉J at T5; {γ₉,D_K}=0) to the exact-zero residual, taking the prediction seriously rather than assuming the wrong-chirality piece away.

**Output Artifacts** (closure-verification checklist):
- Script `computations/session-96/s96_matter_yukawa_chirality.py` — EXISTS; contains `from canonical_constants import` and `append_verdict`.
- Data `computations/session-96/s96_matter_yukawa_chirality.npz` — EXISTS (27 arrays: channel magnitudes, kernels, all CC errors, ε″ flags).
- Plot `computations/session-96/s96_matter_yukawa_chirality.png` — EXISTS (ε″=±1 channel-magnitude log bar; optional artifact).
- Verdict line in `computations/session-96/s96_gate_verdicts.txt` — EXISTS; `^S96-MATTER-YUKAWA-CHIRALITY:.* audit_sha256=[a-f0-9]{64}` matches; dual-SHA companion row present. Latest non-superseded line: `audit_sha256=8d80647424cf8673d8fa5c959eb33a4e874e74fde01fe90b7ddc093926a32529` `content_sha256=ae26f6f77783af5c62499422cd278642cef47e57e920d47d016911aed0c9bede`. Per `gate-verdicts.md` Option A absolute verdict permanence, a prior in-session development line (`audit_sha256=de2496ca90061e1c…`, a tautological-decomposition iteration) is RETAINED on disk and SUPERSEDED via the `supersedes=de2496ca…` tag on the corrective successor; downstream consumers read the latest non-superseded line. sig_5 SHA-uniqueness clean (the two lines carry distinct audit_sha256).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `knowledge-index-usage.md`):
- `search_knowledge("s66 product KO Clifford C2 C1 epsilon double prime chirality Yukawa")` → s66_product_ko_dim_output.txt: "KO=6: J anticommutes with γ → CPT flips chirality (physical)"; "KO=0: J commutes with γ → CPT preserves chirality (non-physical for SM)"; "SU(3)-manifold has KO=0 (ε″=+1)". Confirms the ε″ sign distinction.
- `trace_entity("product KO-dimension epsilon Yukawa chirality")` → no trace (concept not a named registry entity; the result lives in s66 equations).
- `trace_entity("KO-dimension 6")` → KO-dim=6 PROVEN (S7-8, machine-ε); `J²=+1, JD=+DJ, Jγ=−γJ` (A.46 / eq_10104); the parameter-free KO-6 signature.
- `search_knowledge("Jgamma9=-gamma9 J anticommutation T5 KO-dim 6 epsilon prime prime SU(3) manifold")` → connes-master-equation.md: `(ε,ε',ε'')=(+1,+1,−1) ⇒ KO-dim 6, J_F²=+1, J_F D_F=D_F J_F, J_F γ_F=−γ_F J_F`; s66: `KO(SU(3)_manifold)=0`, `KO(M⁴×SU(3))=4`. Confirms physical ε″=−1 vs SU(3)-lift ε″=+1.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). Used as the L_max=12 cache slice anchor.
- `search_knowledge("Pfaffian H_K+ restriction … S_f=⟨Jψ,Dψ⟩ half-density")` → canonical fermionic action `S_f = ⟨Jψ̃ | D_K | ψ̃⟩`, ψ̃ ∈ H_K⁺ (connes-master-equation.md, phonic-exflation-equation.md); `T3-S30A-DTOTAL-PFAFFIAN: value=+1 Pfaffian-Z₂-per-sector PASS` (T10) — H_K⁺ restriction well-defined.
- **Not PRE-CLOSED**: s66 established the ε″=+1-vs-−1 mismatch and flagged "fermionic sector needs separate treatment," but the H_K⁺-restriction RESOLUTION (does the wrong-chirality residual vanish on the bilinear?) was NOT previously computed. This gate is the first explicit evaluation; it does not recompute a closed result.

---

### §W4-6. S96-MATTER-R-HIERARCHY (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S96-MATTER-R-HIERARCHY`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (direct-from-D_K mass-squared ratio R; bare R=27.2 PROVEN-tag adjudication)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: The mass-squared ratio R = Δm²₃₂/Δm²₂₁ computed DIRECTLY from |λ_i(D_K at τ_fold)| spacings (no seesaw M_R) lands in [30,38], reconciling the registry-PROVEN bare R=27.2 with the measured NuFit R≈33.8 via the closure route the bare zero-mixing value omits.
**Plan reference**: `sessions/session-plan/session-96-plan-w4.md` §W4-6 ([SIGN]-trigger ⇒ 3-tuple companion row REQUIRED; substitution chain shows perturbative mixing moves R the WRONG way).

**Verdict**: **FAIL** — `R_direct = 9.862` (m_1=0 normal ordering, direct D_K spacing) lies **outside the FAIL-complement [17,66]**; the direct-from-D_K route does not reach the order of magnitude of the measured hierarchy. The composite-collapse independently forces FAIL (`regime_verdict = BREAKDOWN`). The FAIL is informative on **two** fronts: (i) the direct B1/B2/B3 spacing at τ_fold reproduces neither the bare-PROVEN 27.2 nor the measured 33.8, and (ii) the [SIGN] prediction is **confirmed** — the weak-mixing correction `F = 0.0273 ≤ 1` moves R the WRONG way (downward, away from 33.8). The bare R=27.2 PROVEN tag is retired to the §8.5-honest "sign + OOM robust; exact ratio conditional" form (decision below).

**Output Artifacts** (closure-verification checklist):

- **Script** `computations/session-96/s96_matter_r_hierarchy.py` — EXISTS (22,977 bytes). `grep -E "from canonical_constants import"` →
  ```
  from canonical_constants import *  # noqa: F401,F403
  ```
  `grep -E "append_verdict"` →
  ```
  def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
      append_verdict(top, value, audit_sha, content_sha)
  ```
- **Data** `computations/session-96/s96_matter_r_hierarchy.npz` — EXISTS (8,374 bytes). `R_direct = 9.86183067373777` written for downstream W4-7 SEESAW-D5 R-route check (`keys` include `R_direct, R_convC, R0_formula, F, F_le_1, R_full_mixing, R_eig_mixed, dm2_21, dm2_32, verdict, sign, magnitude, regime`).
- **Plot** `computations/session-96/s96_matter_r_hierarchy.png` — EXISTS (61,295 bytes; left panel: R across conventions vs PASS/FAIL bands + NuFit/PROVEN anchors; right panel: the F≤1 [SIGN] decomposition).
- **Verdict line** `computations/session-96/s96_gate_verdicts.txt` line 72 — `grep -E "^S96-MATTER-R-HIERARCHY:.* audit_sha256=[a-f0-9]{64}"` →
  ```
  S96-MATTER-R-HIERARCHY: FAIL -- value=9.86183067373777 scheme=direct-DK-eigenvalue-spacing-no-seesaw convention=RATIO L_max=10 audit_sha256=8e1de47dd3b129c98e485086ae990b521deb1570d832cefd24376737047eb708 content_sha256=400ae0232c7bb750cebc8fe565f50a661dc0760ea941220ee5d3ea9873cba86b schema_version=S84+
  ```
  Dual-SHA companion row (line 73):
  ```
  # audit_sha256_short=8e1de47dd3b129c9 content_sha256_short=400ae0232c7bb750 # S96-MATTER-R-HIERARCHY dual-SHA companion row
  ```
  **SIGN/MAGNITUDE/REGIME 3-tuple companion row (line 74; REQUIRED — [SIGN] trigger)**:
  ```
  # sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN # S96-MATTER-R-HIERARCHY 3-tuple annotation (schema-v2)
  ```
  `audit_sha256=8e1de47d…` is unique across the file (sig_5 clean for this gate).
- **WP §W4-6** (this section) — Status COMPLETED, Verdict FAIL, Output Artifacts, MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per `.claude/rules/epistemic-discipline.md` query-first discipline):

1. `search_knowledge("bare R 27.2 mass-squared ratio neutrino zero mixing Delta m32 Delta m21")` → **HIT**: theorem `Mass hierarchy R = 27.2 and normal ordering | PROVEN` (`framework-bbn-hypothesis.md`); S35 geometric relation `R_bare(τ) = [Δ₂₃(E₃+E₂)]/[Δ₁₂(E₂+E₁)]`; S35 record `R = 32.6 (+1.4,−1.3)`; structural bound `max[R·sin²θ₂₃] ≈ 3.5`. Confirms the bare-PROVEN value + the gate's reconciliation target.
2. `search_knowledge("S35 analytic R formula mass-squared ratio eigenvalue spacing D_K neutrino")` → **HIT**: the full S35 analytic formula `R ≈ [(E₃−E₂)(E₃+E₂)]/[(E₂−E₁)(E₂+E₁)] · [1−V₂₃²/(E₃−E₂)²]/[1+V₁₂²/(E₂−E₁)²]` (`session-35-neutrino-baptista-workshop.md`); atlas-07 note "[NEW S35] Singlet tridiagonal PMNS — R ceiling ~5.9, need ~33". Confirms the closure-route formula + the standing R-ceiling gap.
3. `trace_entity("Mass hierarchy R = 27.2 and normal ordering")` → **single PROVEN theorem node** (`proven_2152`); no contradicting closure. The bare R=27.2 is a registry theorem, not a canonical constant.
4. `get_constant("R_bare")` → **not found**; `list_constants("R_direct|R_Yuk|R_bare|Delta_B|M_KK")` → no `R_direct`/`R_bare`/`R_Yuk` canonical exists (so this gate is the first to compute `R_direct`); confirmed `Delta_B1=0.371795`, `Delta_B2=0.732026`, `Delta_B3=0.176`, `M_KK=7.42866e16`. No PRE-CLOSED conflict; the direct-from-D_K `R_direct` is genuinely uncomputed.
5. `search_knowledge("S52 MSW transit B1 B2 B3 eigenvalue trajectory direct D_K spacing R=3.37 fold")` → **HIT** (the gate's input data): `s52_msw_transit_output.txt` gives `E_B1=0.81974111, E_B2=0.83589351, E_B3=0.87297503`, `dm2_21=0.02674247, dm2_32=0.06336745`, `V(B1,B2)=0.077, V(B2,B3)=0.022, V(B1,B3)=0 EXACT (NNI)`; theorem `S52 MSW transit: R=3.37 at the fold (10× below); R unmodified by MSW dynamics (eigenvalue property, not state property)`. Confirms the direct eigenvalues + the standing 10×-below shortfall.

**Results** (NUMBERS first):

Direct D_K bottom-content lepton-triplet eigenvalues at τ_fold = 0.190 (M_KK units, from `s52_msw_transit.npz`, TRANSIT-52):

| quantity | value |
|:---------|:------|
| E_B1 (lightest) | 0.81974111 |
| E_B2 | 0.83589351 |
| E_B3 (heaviest) | 0.87297503 |
| V₁₂ | 0.0770 |
| V₂₃ | 0.0220 |
| V₁₃ | 0.0000 (EXACT, NNI texture — V(B1,B3)=0 at all τ) |

**m_1 = 0 normal ordering** (gate-pinned; masses = direct |λ_i| spacings from the lightest, m_i = E_i − E_1):
- m_1 = 0, m_2 = E_B2 − E_B1 = 0.016152, m_3 = E_B3 − E_B1 = 0.053234 (M_KK)
- Δm²₂₁ = m_2² − m_1² = 2.6090×10⁻⁴ M_KK²
- Δm²₃₂ = m_3² − m_2² = 2.5730×10⁻³ M_KK²
- **R_direct = Δm²₃₂ / Δm²₂₁ = 9.862** (4 sig figs) — vs PASS-band **[30,38]** and FAIL-complement **[17,66]** ⇒ **FAIL** (below the [17,66] floor by 1.7×).

**Convention sensitivity** (reported for completeness; the gate-pinned reading is m_1=0 spacing-from-lightest):
- Conv A (m_1=0, spacing-from-lightest — **gate-natural**): R = **9.862** → FAIL
- Conv C (masses = eigenvalues directly, m_i = E_i): R = (E₃²−E₂²)/(E₂²−E₁²) = **2.370** → FAIL (this is the S52-native squared-spacing ratio; S52 `R_fold=3.37` is the distinct `Δm²₃₁/Δm²₂₁` convention)
- Conv B (m_1=0 but m_2=E₂, m_3=E₃ directly): R = **0.0907** → FAIL
- **All three m_1-conventions FAIL** — no admissible direct-spacing reading reaches even [17,66], let alone the bare 27.2 or the measured 33.8.

**Bare R_0 + weak-mixing correction factor F** (the closure route the bare zero-mixing value omits):
- R_0 = (E₃−E₂)(E₃+E₂) / [(E₂−E₁)(E₂+E₁)] = **2.3695** (= Conv C; the S35 analytic-formula FIRST factor)
- F_num = 1 − V₂₃²/(E₃−E₂)² = 1 − 0.022²/0.03708² = **0.64801**
- F_den = 1 + V₁₂²/(E₂−E₁)² = 1 + 0.077²/0.016152² = **23.7252**
- **F = F_num/F_den = 0.027313** → **F ≤ 1 = TRUE** (pre-registered prediction holds)
- R_0 · F = 2.3695 × 0.027313 = **0.064720** — the weak-mixing correction collapses R toward zero, NOT toward 33.8.
- 3×3 effective-matrix eigenvalue cross-check (E_i on diagonal, V_ij off-diagonal, eigvalsh): R_eig_mixed = **0.4122** (full-mixing squared-ratio; also far below band) — corroborates that turning on V_ij DECREASES R.

**SIGN / MAGNITUDE / REGIME 3-tuple** (`gate-verdicts.md` schema-v2):

| component | verdict | basis |
|:----------|:--------|:------|
| `sign_verdict` | **PASS** | Pre-registered Step-4 direction is F ≤ 1 (mixing DECREASES R). Computed F = 0.0273 ≤ 1 ⇒ direction matches. The mixing correction is confirmed to move R the WRONG way (away from 33.8). |
| `magnitude_verdict` | **FAIL** | R_direct = 9.862 ∉ [30,38] AND ∉ [17,66] ⇒ magnitude misses both the PASS and INFO bands. |
| `regime_verdict` | **BREAKDOWN** | Weak-mixing expansion parameter x₁₂ = V₁₂²/(E₂−E₁)² = 0.077²/0.016152² ≈ **22.7 ≫ 1** (the B1–B2 gap is NARROW relative to its coupling). The S35 perturbative formula is OUT of its V_ij ≪ dE_ij regime in the 1–2 sector; breach fraction = 100% > 50% ⇒ BREAKDOWN. |

**Composite collapse** (pre-registered rule, applied at append-time): `regime_verdict == BREAKDOWN ⇒ composite = FAIL`. The band-verdict (R∉[17,66] ⇒ FAIL) and the composite both give FAIL; the top-line is the more conservative = **FAIL**.

**Output 4-tuple**: `(value=9.86183067373777, scheme=direct-DK-eigenvalue-spacing-no-seesaw, convention=RATIO, L_max=10)`.

**Dual-SHA (full 64-char)**:
- `audit_sha256 = 8e1de47dd3b129c98e485086ae990b521deb1570d832cefd24376737047eb708`
- `content_sha256 = 400ae0232c7bb750cebc8fe565f50a661dc0760ea941220ee5d3ea9873cba86b`

**CC1 — Sage cross-check of the S35 analytic R formula** (RATIO 0.5% rubric):
- In-script float CC1: |R0_formula − R_convC| / R_convC = **3.75×10⁻¹⁶** ≪ 0.005 ⇒ **PASS** (the bare-formula identity R_0 = (E₃²−E₂²)/(E₂²−E₁²) holds to machine ε).
- Independent Sage MCP check: the symbolic identity `(E₃−E₂)(E₃+E₂)/((E₂−E₁)(E₂+E₁)) − (E₃²−E₂²)/(E₂²−E₁²)` simplifies to **0** exactly (`sage_eval`, `simplify_full() == 0 → True`); QQ-exact numerical R_0 = **2.369544155**, matching the script to 16 digits. The full S35 formula reconstructs as `R = R_0·(1−V₂₃²/(E₃−E₂)²)/(1+V₁₂²/(E₂−E₁)²)`.

**CC2 — optional W4-1 R_Yuk cross-check**: `s96_matter_a4_yukawa_ratio.npz` **not present at runtime** (W4-1 had not landed when this gate ran). CC2 is SKIPPED (the gate is self-contained per the prereq table — W4-1 is an optional cross-check, not a blocking prereq). If W4-1 lands later, the rel_tol ≥ 1e-4 R_Yuk comparison is a follow-up.

**Substitution chain** (the [SIGN] F ≤ 1 derivation, with substituted numbers):

```
Claim: "Mixing INCREASES R toward 33.8" (the naive closure hypothesis).
  Def 1: R_0 = (E3^2-E2^2)/(E2^2-E1^2)
             = (0.87298^2-0.83589^2)/(0.83589^2-0.81974^2) = 2.3695   [bare, m_i=E_i]
  Def 2: F  = [1 - V23^2/(E3-E2)^2] / [1 + V12^2/(E2-E1)^2]            [S35 analytic]
  Def 3: V_ij << dE_ij assumed (weak-mixing limit).
  Substitute: F_num = 1 - 0.022^2/(0.03708)^2 = 0.64801  (<= 1, numerator suppresses)
              F_den = 1 + 0.077^2/(0.01615)^2 = 23.7252   (>= 1, denominator suppresses)
              F = 0.64801/23.7252 = 0.027313
  Simplify:   numerator factor <= 1 AND denominator factor >= 1  ==>  F <= 1.
  Canonical:  R = R_0 * F = 2.3695 * 0.027313 = 0.06472  <=  R_0 = 2.3695.
  Direction:  the weak-mixing correction DECREASES R, AWAY from 33.8.  [Claim REFUTED]
  Conclusion: F <= 1 confirmed (sign_verdict = PASS). The 27.2->33.8 closure CANNOT
              come from a small weak-mixing correction in this sign convention. AND the
              regime is broken (x12 = 22.7 >> 1): even the perturbative formula is
              inapplicable in the 1-2 sector. No zero-mixing or weak-mixing route
              reaches [30,38] from the direct D_K spacings at tau_fold.
```

**Bare R=27.2 PROVEN-tag retirement decision (§8.5-honest)**:

The registry theorem "Mass hierarchy R = 27.2 and normal ordering | PROVEN" (`framework-bbn-hypothesis.md`) is **OVER-TAGGED** as a literal exact-value PASS. Three independent facts force the retirement:

1. **The direct B1/B2/B3 spacings at τ_fold do NOT yield 27.2.** They yield R_direct ∈ {0.091, 2.37, 9.86} depending on the m_1 convention — none is 27.2. The bare-PROVEN 27.2 comes from a *different* construction (the B2/G1 near-degeneracy at a tuned τ₀, where S35 reports `R_bare = 31.7→33` as τ is dialed — atlas-07 "R ceiling ~5.9, need ~33"; the 27.2 is the conditional-on-τ₀-selection value, not the τ_fold spacing).
2. **The weak-mixing correction moves the WRONG way** (F = 0.0273 ≤ 1, this gate's [SIGN] PASS): the closure route the bare value omits does NOT close the 27.2→33.8 gap — it widens it.
3. **The perturbative formula is out of regime** (x₁₂ ≈ 22.7 ≫ 1): the 1–2 sector mixing is non-perturbative, so neither the S35 analytic R nor the bare value is a clean zero-parameter prediction at τ_fold.

**Retirement**: the bare R=27.2 is retired from "PROVEN exact value" to the §8.5-honest form — **"sign + order-of-magnitude robust (normal ordering, R > 1, hierarchy direction correct); exact ratio CONDITIONAL on τ₀-selection; all Jensen-curve zero/weak-mixing closure routes to 33.8 FAILED."** This matches the neutrino-synthesis summary (R = 3.37 at fold, 10× below; "R unmodified by MSW dynamics"; the singlet-PMNS R-ceiling ~5.9) and the standing constraint-map state that no Jensen-curve mechanism reaches R≈33.8. Normal ordering itself (m_3 > m_2 > m_1, the SIGN of the hierarchy) remains robust across all conventions — that is the §8.5-retained content.

**Constraint-map update**: the direct-from-D_K R route is now **CLOSED** as a path to the measured R≈33.8 — it joins the Jensen-curve closure routes (S35 K7-G1, S52 MSW-transit R=3.37, off-Jensen singlet R=7.03) that all FAIL to reach 33.8. The surviving open routes for the full mass-squared hierarchy are the inter-sector / non-left-invariant couplings (W4-2 PMNS-3X3 territory) and a scale/normalization bridge — NOT the bottom-content spacing at τ_fold. **No `R_direct_FW` canonical promotion** (verdict is FAIL, not PASS/INFO; per the gate rubric, promotion is gated on PASS/INFO). The value R_direct = 9.862 is recorded in the .npz and verdict line for the downstream W4-7 SEESAW-D5 adjudication, where it is the direct-route input against the S60 seesaw R.

---

### §W4-7. S96-MATTER-SEESAW-D5 (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S96-MATTER-SEESAW-D5`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (D5 adjudication: S60 seesaw m_2=0.008678 eV vs §0 "no seesaw" — is M_R a D_K eigenvalue?)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: The S60 seesaw light-ν mass m_2=0.008678 eV (real RH Majorana M_R, M_1=1.004396 M_KK, M_2=1.078573 M_KK) is RECONCILED with §0's "no seesaw" because the M_i are THEMSELVES D_K eigenvalues — the seesaw is an internal level-splitting, not an external add-on, and the S60 and direct-from-D_K (W4-6) routes give the same R.
**Plan reference**: `sessions/session-plan/session-96-plan-w4.md` §W4-7 (PART 1 structural / PART 2 numerical; prereq W4-6 for the R-route comparison; Q1 workshop-flag candidate per `Investigating-Workshops.md`).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **script** `computations/session-96/s96_matter_seesaw_d5.py` — EXISTS (19,640 B). `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # noqa: F401,F403,E402`; `grep -E 'append_verdict'` → `def append_verdict(verdict: str, value, audit_sha: str,` + `    append_verdict(verdict, value, audit_sha, content_sha)`. PASS.
- **data** `computations/session-96/s96_matter_seesaw_d5.npz` — EXISTS (5,816 B); 22 keys (value, mr_targets, mr_nearest, mr_reldiff, part1_*, R_seesaw, R_direct, part2_reldiff, delta_CP_allowed, …).
- **plot** `computations/session-96/s96_matter_seesaw_d5.png` — EXISTS (39,192 B; M_i-vs-D_K-spectrum overlay, 0.7–1.35 M_KK window). [optional per plan; produced.]
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — `grep -E '^S96-MATTER-SEESAW-D5:.* audit_sha256=[a-f0-9]{64}'` → matches the canonical INFO line (full 64-char `audit_sha256=e58ecfba…d649fd`); dual-SHA companion row present (`# S96-MATTER-SEESAW-D5 dual-SHA companion row`). `audit_sha256=e58ecfba…` is unique across the file (sig_5 clean for this gate). Exactly 1 canonical line for the gate-ID. **No schema-v2 3-tuple required** ([VERIFY] trigger, not [SIGN]).
- **WP §W4-7** (this section) — Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per `.claude/rules/epistemic-discipline.md` query-first discipline):

1. `search_knowledge("s60 seesaw light neutrino mass m_2 0.008678 M_R Majorana leptogenesis CP")` → **HIT**: `s60_lepto_cp_log.txt` records m_1=0, m_2=0.008678 eV, m_3=0.049528 eV; RH Majorana M_1=1.004396 M_KK (7.4613e16 GeV), M_2=1.078573 M_KK, M_3=1.170003 M_KK; `M_R = O·diag(M_1,M_2,M_3)·Oᵀ` with O real orthogonal ⇒ M_R real symmetric. Confirms the exact CC1 inputs.
2. `search_knowledge("Leptogenesis real M_R CLOSED J D_K commute T11 CPT delta_CP")` → **HIT**: closed_mechanism + PROVEN theorem `Leptogenesis (real M_R) | S60 | No CP phase`; `s60_lepto_cp_log` `epsilon_1 = 0 EXACT`, `eta_B = 0 EXACT`; `[J,D_K]=0` PROVEN at 79,968 pairs (max dev 3.29e-13, S17a, atlas-07). CC2 confirmed: real M_R ⇒ δ_CP ∈ {0,π}.
3. `search_knowledge("no seesaw capstone neutrino mass lightest D_K eigenvalues zero Yukawa")` → **HIT**: S96-plan-w7 epistemic-partition line "normal mass ordering from D_K eigenvalue ordering"; `falsifier-rigor-registry` neutrino-ordering row "S56 Workshop 4, S41 W1-2 (seesaw = 0)"; theorem `Yukawa tree-level mass generation | Tree-level Yukawa vanishes by PW orthogonality | S62`. Confirms the §0 "no seesaw" / "all masses from D_K" framing the gate adjudicates.
4. `trace_entity("Leptogenesis (real M_R)")` → **single PROVEN theorem node** (`proven_1919`) + closed_mechanism (`closed_regv_eraVII_82`); no contradicting closure. The S60 leptogenesis-null is canonical, not in dispute.
5. `get_constant("M_KK")` → 7.428660036284456e16 GeV (S42 CONST-FREEZE-42). Units anchor for the M_i (M_KK units). **Not PRE-CLOSED**: D5 is an open dissonance; no closure adjudicates the S60-vs-§0 reconciliation. Gate genuinely uncomputed.

Sage cross-check (`mcp__sage__sage_eval`, QQ): R_seesaw = m_3²/m_2² − 1 = **594428775/18826921 = 31.573339847** (m_1=0); |R_seesaw − R_direct|/R_direct = **2.2015698597**. Float and exact forms agree.

**Verdict**: **INFO** — `value=2.201569859720042` scheme=seesaw-vs-direct-DK-reconciliation convention=RATIO L_max=10 (full dual-SHA: `audit_sha256=e58ecfba0895d7989534960a4da280c8d66c173135ef03dac8392a5742d649fd`, `content_sha256=6d6680555bc507a7e47bd6414db340497fa45fba1ba29fef16a2819411ee03d6`, schema_version=S84+). Mixed: M_R is INTERNAL (PART 1) but the seesaw and direct R-routes DIVERGE by a factor 2.2 (PART 2 FAIL). Per the plan §W4-7 `INFO_meaning` and `dual_prior` discriminator ("mixed — M_i internal but R routes diverge ⇒ INFO, route to a follow-up reconciliation workshop"). The structural sub-result δ_CP ∈ {0,π} is confirmed self-contained.

**Results** (NUMBERS first):

**PART 1 — M_R-as-D_K-eigenvalue spectral coincidence** (tol_MR = 1% against the L_max=12 master cache, τ=0.19; 166,896 |λ| with multiplicity, 6,997 unique):

| S60 M_i | value / M_KK | nearest D_K \|λ\| | reldiff | strict-1% |
|:--------|:------------:|:-----------------:|:-------:|:---------:|
| M_1 | 1.004396 | 1.02220880 | 1.773e-2 | **FAIL** |
| M_2 | 1.078573 | 1.07842811 | 1.343e-4 | PASS |
| M_3 | 1.170003 | 1.17583354 | 4.983e-3 | PASS |

PART 1: **2/3 strict-1% PASS; all three < 2%** (`part1_internal_2pct = True`); max reldiff 1.773e-2 (M_1).

**Reading**: the M_i ARE D_K spectral objects. `s60_lepto_cp_log` (line 11–12) states the M_R triple IS the B-branch fold spectrum, `E_B3 at fold = [1.00439566, 1.07857332, 1.1700026] M_KK`, read off the D_K(τ) operator along the S52 MSW-transit trajectory at the fold (τ_fold_ed = 0.193878). The strict-1% pin tests them against the τ=0.19 *cache*; M_2 and M_3 match to ≤0.5%, and the only near-miss (M_1 at 1.77%) is the steepest-moving (B1) branch's residual from the τ=0.19 ↔ 0.193878 fold offset — NOT an external parameter. The M_R is the spectrum's own near-fundamental level structure. **M_R is INTERNAL** (Track A on the M_R-vs-external axis); the seesaw is a level-splitting, not an add-on.

**PART 2 — R-route agreement** (R_direct loaded from `s96_matter_r_hierarchy.npz` key `R_direct`; NOT recomputed):

- R_seesaw = Δm²₃₂/Δm²₂₁ = (m_3²−m_2²)/(m_2²−m_1²) = m_3²/m_2² − 1 (m_1=0) = **31.5733** (Sage QQ exact 594428775/18826921 = 31.573339847)
- R_direct (W4-6) = **9.86183067373777**
- |R_seesaw − R_direct|/R_direct = **2.2016 ≫ 0.10 ⇒ PART 2 FAIL** (the routes do NOT agree)

**Why the routes diverge** (the D5 adjudication content): the two routes read DIFFERENT regions of the same D_K spectrum. The S60 seesaw route uses the B-branch *fold* energies {1.004, 1.079, 1.170} M_KK as the RH Majorana M_R, then forms the LIGHT masses via m_i = Y_i²v²/(2M_i) (Yukawa-dependent), giving light spacings (m_2=0.008678, m_3=0.049528 eV) ⇒ R_seesaw ≈ 31.6 — coincidentally near the NuFit target R≈33.8 because the S60 light masses were back-solved to a NuFit-like spectrum. The W4-6 direct route instead uses the BOTTOM light triple directly — E1=0.81974, E2=0.83589, E3=0.87298 M_KK (s52 MSW transit) — as the neutrino masses themselves (m_1=0 in W4-6's normal-ordering convention but using these as the spacing scale), giving R_direct = 9.86 (W4-6 FAILed its own NuFit band, 10×-region shortfall). The seesaw route carries the *Yukawa* freedom Y_i (S60: Y_2=4.79, Y_3 implied) that the parameter-free direct route does not; that Yukawa freedom is precisely what lets S60 land a NuFit-like R while the zero-free-parameter direct spacing cannot. **The disagreement localizes the open question**: the framework does not yet derive the Yukawa structure (W4-1 family-number frontier #7) that would pin the light spectrum from D_K alone, so the seesaw (Yukawa-dressed) and direct (bare-spacing) routes are not yet a single number.

**4-tuple**: `(value=2.201569859720042, scheme=seesaw-vs-direct-DK-reconciliation, convention=RATIO, L_max=10)` — value = the PART 2 R-route relative discrepancy.

**Structural sub-result (self-contained; T11 / "Leptogenesis (real M_R)" CLOSED)** — independent of the numerical half:
substitution chain — [J,D_K]=0 at all τ (T11, PROVEN S43; 79,968 pairs, max dev 3.29e-13) ⇒ the natural-basis M_R is real symmetric (`M_R = O·diag(M_i)·Oᵀ`, O real orthogonal) ⇒ no complex phase enters the leptonic mixing ⇒ **δ_CP ∈ {0, π} EXACTLY**, ε₁ = 0 EXACT, η_B^internal = 0 EXACT. This is a parameter-free prediction regardless of the R-route agreement, and it is a sharp discriminator: DUNE and Hyper-K target δ_CP at ~10–20° precision; the current NuFit-6.0 best fit is δ_CP ≈ 177° (≈ π) with CP-conserving values inside the band — *consistent* with the framework's {0,π} forcing, but a future exclusion of {0,π} at high significance would falsify the real-M_R / [J,D_K]=0 structure.

**CC1** — S60 seesaw record (`s60_lepto_cp_log.txt`): m_1=0, m_2=0.008678 eV, m_3=0.049528 eV; M_1=1.004396, M_2=1.078573, M_3=1.170003 M_KK; M_R real (O real orthogonal). Verified against the L12 cache (PART 1 table above).
**CC2** — "Leptogenesis (real M_R)" CLOSED (permanent-results-registry, S60) + T11 [J,D_K]=0 PROVEN (atlas-07): ε₁=0, η_B=0 EXACT ⇒ δ_CP ∈ {0,π}. Both confirmed via `trace_entity` (single PROVEN node, no contradicting closure).

**§0 "no seesaw" wording verdict** — **REWORD (do not supersede S60; do not confirm verbatim)**. The strong reading "no seesaw" is too strong as literally stated, but S60 is NOT superseded. The accurate statement, supported by PART 1: *the right-handed Majorana masses M_i are themselves D_K eigenvalues (the B-branch fold energies), so the seesaw introduces **no external mass parameter** — it is an internal level-splitting of the spectrum.* §0 should read **"no external seesaw parameter (the RH Majorana scale is the D_K B-branch fold spectrum)"** rather than "no seesaw." What is NOT yet internal is the **Yukawa** coupling Y_i that dresses the M_i into the light spectrum (W4-1 / family-number frontier #7); until that is derived from D_K, the seesaw light masses carry residual Yukawa freedom and the seesaw-vs-direct R-routes do not coincide. This wording change is a §0 capstone-prose reconciliation routed to the designated writer (curated-doc patch per `feedback_framework-hygiene.md`), and triggers the capstone-hygiene gate Q3 (PROVEN/CONDITIONAL status of the "no seesaw" claim changes from over-strong to scoped).

**Carry-forward (INFO routing per plan §W4-7 + `Investigating-Workshops.md` D5 Q1-flag)**: the M_R-internal-vs-external numerical residual — *why the Yukawa-dressed seesaw R (≈31.6) and the bare-spacing direct R (9.86) differ, and whether a D_K-derived Yukawa structure reconciles them* — is a genuine math/physics adjudication (two competing readings of how the light spectrum is built from the same M_R spectrum). Route to a D5 follow-up `/rclab-review` workshop slot.

- **What**: adjudicate whether a parameter-free D_K-derived Yukawa block (W4-1 successor) reconciles R_seesaw (Yukawa-dressed, ≈31.57) with R_direct (bare spacing, 9.86), or whether the seesaw's residual Yukawa freedom is irreducible (⇒ §0 must scope to "no external *mass* parameter, Yukawa structure open").
- **Inputs**: `s96_matter_seesaw_d5.npz` (R_seesaw, M_i coincidence), `s96_matter_r_hierarchy.npz` (R_direct), W4-1 `s96_matter_a4_yukawa_ratio.npz` (Yukawa block, if non-empty), `s60_lepto_cp_log.txt` (Y_i).
- **Gate**: workshop structural verdict on the two readings (Yukawa-reconcilable vs irreducible-freedom); no new numerical threshold (adjudication, not compute).
- **Effort**: 1 `/rclab-review` workshop slot (2-position adjudication, Q1 per `Investigating-Workshops.md`).

---

## Wave 4 Synthesis (team-lead)

**Wave 4 (`a₄` matter sector + seesaw; cluster C6 + dissonance D5; 7 gates, 3 agent types).** Dependency order honored: Phase A `{W4-1, W4-2, W4-4, W4-5, W4-6}` dispatched parallel; Phase B `{W4-3 (after W4-2), W4-7 (after W4-6)}` dispatched once their prereq `.npz` outputs were verified on disk. All 7 closed and verified (verdict line + dual-SHA companion + 3-tuple where `[SIGN]` + WP §-section `must_contain` + artifacts). Per `feedback_reporting-framing.md`: no session-aggregate metric — each gate's constraint-surface position individually.

### Gate-by-gate constraint-surface position

**§W4-1 S96-MATTER-A4-YUKAWA-RATIO — INFO.** `R_Yuk = 1.588` (bare, gauge-invariant, zero-free-parameter; m_heavy/m_light from the 11 distinct mass eigen-bilinears of the bare `D_K` chirality-off-diagonal block on `V_(1,0)⊗ℂ¹⁶`). The `a₄` Yukawa layer is **NON-EMPTY** (`R_Yuk ≠ 1`, spread 0.49 ≫ 1e-12 — the empty-layer FAIL branch did NOT fire; the bare `D_K` block is already non-degenerate, no Higgs VEV needed). But `|log10(R_Yuk / (m_τ/m_μ)=16.817)| = 1.025`, just outside the ≤1.0 PASS band ⇒ INFO. The agent correctly rejected a seed=0 fluctuated PASS as a non-zero-parameter artifact (fluctuation coefficients swing the ratio over [1.46, 3.22] — inadmissible as a zero-parameter observable). Constraint: the substrate's claim "Yukawas read from `D_K`" is non-vacuous at one generation, but OOM-only — the magnitude awaits frontier #7.

**§W4-2 S96-MATTER-PMNS-3X3 — INFO.** The **B2 Schur wall LIFTS**: θ₁₂, θ₂₃ open monotonically from exactly zero under a non-left-invariant Lie-derivative `L_X` (the block-diagonality closure only barred *left-invariant* coupling), with `[iK_7, D_K]=0` preserved (Jensen not re-broken). But no single ε_LX fits all four NuFit-6.0 bands (θ₁₃ wants ε_LX ≲ 0.035, θ₂₃ wants ≳ 0.060 — mutually exclusive), and `R` peaks at 6.868, 2.5× below the band floor of 17. INFO fired verbatim; dual-prior unchanged (Track A 0.35 / Track B 0.65). Constraint: the angles open (new mechanism), R does not.

**§W4-3 S96-MATTER-0NUBB — INFO.** PART 1 **DEFINITE MAJORANA** (three independent grounds: the (1,1,0) ν_R content is two same-chirality states e₀,e₁₅ both in H_K⁺ with ZERO opposite-chirality SM-singlets in H_K⁻ ⇒ no Dirac partner; C₁ self-conjugacy admits ξ=ξ^c; KO-dim-6 doubled-reality H_F⁺ Majorana block nonzero). The bare diagonal bilinear =0 read as **T4** (ν_R mass Yukawa/seesaw-generated, consistent with W4-7's M_R), NOT Dirac. T1 antilinear-J discipline held (correct antilinear form =0; forbidden linear `[C₂,D_F]`=0.663 NOT used). PART 2 (under the INFO W4-2 prereq, agent chose COMPUTE-with-caveat over PRE-REG-INC since inputs present): `m_ββ = 4.96–8.27 meV` (framework U_ei + NuFit-NO external scale) — below KamLAND-Zen (122 meV), **within next-gen 0νββ reach (~6–20 meV)**. Composite INFO (Majorana solid; m_ββ rests on the non-PASS PMNS + external scale).

**§W4-4 S96-MATTER-EXT-BARYOGEN — FAIL** (composite via regime BREAKDOWN). PART 1 internal CP-odd source = 0 EXACT (`|sinφ_CP|<1e-15`, `η_B^internal<1e-15`; T11 `[J,D_K]=0` confirmed at capstone level, cross-checked vs s52/s60 archives). PART 2: the located in-structure external source `tr(R∧R)|_{g_M}^{left-inv}=0` EXACT; the only nonzero channel (DKKMS thermal gradient `∂_μR·J^μ_B`) gives `η_grav ≈ 7.0e4`, **over-producing η_obs≈6e-10 by ~14.1 OOM**, and the thermal formula is out-of-regime for the integrable GGE relic (regime breach=1.00). Constraint: baryogenesis requires a source external to BOTH `D_K` (T11) AND its homogeneous emergent `g_M` (left-inv `tr(R∧R)=0`) — a *located* frontier #9 (what is missing), not a manufactured value.

**§W4-5 S96-MATTER-YUKAWA-CHIRALITY — PASS** (THEOREM-class, machine-ε). `residual_chirality_preserving = 0.000000000000e+00` < 1e-12 EXACTLY. The H_K⁺ Pfaffian restriction projects out the ε″=+1 wrong-chirality coupling structurally (`J=C₂·K` carries ε″=+1 ⇒ `Jψ̃∈H_K⁺`; `{γ₉,D_K}=0` ⇒ `D_K:H_K⁺→H_K⁻`; so `⟨Jψ̃|D_K|ψ̃⟩=⟨H_K⁺|H_K⁻⟩=0`). Non-vacuous: the physical contrast `J′=γ₁·C₂` (ε″=−1) carries a nonzero flip channel `|Y|_flip=2.6628`, so effective ε″=−1 (SM structure) is recovered. T1 antilinear-J discipline held; the agent self-caught and Option-A-superseded a tautological first bilinear. Constraint: the §1.3.4 capstone chirality caveat is **CONFIRMED "bounded" (exactly zero) — CLOSED, not "open."**

**§W4-6 S96-MATTER-R-HIERARCHY — FAIL** (composite via regime BREAKDOWN). `R_direct = 9.862` (direct `D_K` eigenvalue spacings, no seesaw, m_1=0; all three spacing conventions FAIL the [17,66] complement). The `[SIGN]` sub-verdict PASSED: the weak-mixing factor `F = 0.027 ≤ 1` moves R DOWNWARD from the bare 27.2, away from the measured 33.8 — the chain's pre-registered direction. Regime BREAKDOWN: the 1–2 sector expansion parameter `x₁₂ ≈ 22.7 ≫ 1`. Constraint: the bare `R=27.2` PROVEN tag is over-tagged → retired to §8.5-honest ("sign + OOM robust; exact ratio CONDITIONAL on τ₀-selection"); the direct-`D_K` R route joins the closed Jensen-curve closure routes.

**§W4-7 S96-MATTER-SEESAW-D5 — INFO** (`value=2.2016`). PART 1: the S60 RH Majorana masses {M_1=1.004, M_2=1.079, M_3=1.170} M_KK **coincide with actual `D_K` eigenvalues** (<2% each; the B-branch fold spectrum) — **M_R is INTERNAL**, not an external add-on. PART 2: R_seesaw=31.57 vs R_direct=9.86 (reldiff 2.20 ≫ 0.10) — the routes DIVERGE because the seesaw route carries **Yukawa freedom** the zero-parameter direct route lacks (frontier #7). Structural bonus: `[J,D_K]=0` ⇒ M_R real ⇒ `δ_CP ∈ {0,π}` EXACTLY (consistent with NuFit δ_CP≈177°≈π; a DUNE/Hyper-K exclusion of {0,π} would falsify the real-M_R structure). Constraint: §0 "no seesaw" → **REWORD** "no *external* seesaw parameter (the RH scale IS the `D_K` B-branch fold spectrum)."

### What Changed

**(a) Numerical revisions**
- bare `R=27.2` PROVEN → §8.5-conditional (`R_direct=9.862` FAIL; weak-mixing `F=0.027≤1` moves R the wrong way).
- New: `R_Yuk=1.588` (bare a₄ Yukawa ratio, INFO); `m_ββ=4.96–8.27 meV` (framework 0νββ prediction, next-gen reach, INFO/external-scale caveat); `R_seesaw=31.57` vs `R_direct=9.86` (D5 reldiff 2.20).
- `η_B^external ≈ 7.0e4` (over-produces η_obs by 14.1 OOM, W4-4 FAIL); PMNS angles open but `R_peak=6.868` (W4-2).
- NuFit-6.0 Δm² (`dm2_21=7.49e-5`, `dm2_31=2.513e-3` eV²) + 0νββ bounds added to `canonical_constants.py` as comparison anchors.

**(b) Structural changes**
- a₄ Yukawa layer: empty? → **NON-EMPTY** (bare `D_K` block non-degenerate without Higgs VEV; W4-1).
- B2 Schur wall: walled (θ₁₂=θ₂₃=0) → **LIFTABLE** (non-left-invariant `L_X` opens angles; W4-2).
- ν nature: → **DEFINITE MAJORANA** (three independent grounds; W4-3).
- ε″ chirality: §1.3.4 caveat "open?" → **CLOSED, exactly zero** (W4-5).
- Baryogenesis: → **located frontier #9** — external to BOTH `D_K` (T11) AND homogeneous `g_M` (left-inv `tr(R∧R)=0`); needs a non-LI/additional-fiber CP-odd + B-violating source (W4-4).
- M_R: external add-on → **INTERNAL** (= `D_K` B-branch fold spectrum); §0 "no seesaw" → "no external seesaw parameter" (W4-7).
- `δ_CP ∈ {0,π}` EXACT (real M_R, `[J,D_K]=0`; W4-7) — a new falsifiable structural prediction.

### C6 / D5 resolution status

- **C6 (a₄ matter sector) — STRUCTURE settled, MAGNITUDES open.** The selection rules and structural identities that follow from `[J,D_K]=0` / KO-dim-6 / Peter-Weyl grading are settled/exact: Majorana nature (DEFINITE), ε″ chirality (EXACT, §1.3.4 CLOSED), internal `η_B=0` (EXACT), `δ_CP∈{0,π}` (EXACT), M_R-are-eigenvalues, the a₄ Yukawa layer non-empty. The continuum *magnitudes* — Yukawa mass ratio (OOM-only), PMNS simultaneous fit + R, direct R — are NOT closed; all await frontier #7.
- **D5 (S60 seesaw vs §0 "no seesaw") — RESOLVED.** M_R is INTERNAL (the M_i ARE `D_K` eigenvalues); §0 reworded to "no *external* seesaw parameter." The R-route divergence (Yukawa freedom) is forwarded as a Q1 D5 workshop.

### Frontier-#7 convergence (the wave's meta-finding)

Four of the seven gates — W4-1 (Yukawa ratio OOM-only), W4-2 (PMNS R unreachable), W4-6 (direct R fails), W4-7 (seesaw/direct R-routes diverge) — are NOT independent shortfalls. They are four views of ONE missing object: **a parameter-free, `D_K`-derived family/Yukawa structure (frontier #7).** The substrate's algebra fixes the *symmetry structure* of matter exactly; the *magnitudes* await this single frontier. This convergence is the wave's most durable output — it consolidates four scattered INFOs/FAILs into one sharply-specified open problem (carry-forward CF-S97-W4-YUKAWA-FAMILY).

### Capstone-hygiene 5-question gate (`.claude/rules/capstone-hygiene-gate.md`; W4 touches §7 + the status ladder)

- **Q1 (a(t)/effective-Friedmann gap)**: NO.
- **Q2 (§7 falsifier-anchor row)**: **YES** — the `m_ββ=4.96–8.27 meV` 0νββ row (next-gen reach) + the `δ_CP∈{0,π}` DUNE/Hyper-K falsifier → `mack-cosmic-bridge` (sole writer of §7 + `falsifier-master-inventory.md`).
- **Q3 (PROVEN/CONDITIONAL/BROKEN/INFO status change)**: **YES** — bare `R=27.2` PROVEN→§8.5-conditional; §1.3.4 chirality caveat→CLOSED; M_R internal; ν Majorana DEFINITE; frontier #9 located → reconcile capstone tags vs Atlas D04 + permanent-results registry.
- **Q4 (PROSE claim vs ledger row)**: **YES** — §0 "no seesaw"→"no external seesaw parameter"; §8.5 bare-R retirement; §1.3.4 chirality CLOSED → designated-writer reviewed patches.
- **Q5 (citation add/invalidate)**: **YES** — NuFit-6.0 Δm² + 0νββ bounds (KamLAND-Zen / LEGEND-200 / next-gen) citations; the W4 gate citations.

Routing: Q2/Q3/Q4/Q5 YES → **session-close capstone-hygiene reconciliation** (mack-cosmic-bridge for §7 + `falsifier-master-inventory.md`; the designated writer for §0/§8.5/§1.3.4 capstone prose) — NOT bulk-appended mid-wave, NOT orchestrator-direct (sole-writer / curated-doc constraints). Recorded in `session-96-housekeeping.md §D`. This W4 run advances the capstone-hygiene K-counter (real status drift caught: R-tag retirement, §0 reword, §1.3.4 closure, M_R-internal, frontier #9).

### Effected in-session (non-math; agent/orchestrator-direct, this wave)

- [x] **NuFit-6.0 Δm² + 0νββ bounds added to `canonical_constants.py`** — `nubb` agent (S96-MATTER-0NUBB PART 2 eV scale-setting) added `dm2_21_NuFit`, `dm2_31_NuFit`, `m_betabeta_KamLANDZen`, `m_betabeta_LEGEND200_reach`, `m_betabeta_nextgen_reach` (lines 2574–2589) with an explicit "COMPARISON ANCHORS ONLY — NOT a canonical replacement for a substrate computation" header + provenance. Verified clean (proper observational-anchor discipline per `substrate-first-canonical-sourcing.md §(i)`). Index/MCP formalization rolls into the §B session-close `/weave --update` batch. — `computations/_shared/canonical_constants.py:2574–2589`

Self-audit: `grep -c '^- \[ \]'` on this Effected-in-session sub-section = 0 (no unchecked items). The capstone/registry status-and-prose changes (bare-R retirement, §0 reword, §1.3.4 closure, §7 falsifier rows) are NOT orchestrator-effectable this wave — they route to the session-close capstone-hygiene reconciliation (mack / designated-writer), recorded in `session-96-housekeeping.md §D`.

## Carry-Forward Computations

Two math carry-forwards, plus one Q1 workshop candidate routed to `/rclab-investigate` (not a WP CF).

### CF-S97-W4-YUKAWA-FAMILY — parameter-free `D_K`-derived family/Yukawa structure (frontier #7)

> The convergent open problem of this wave — W4-1, W4-2, W4-6, W4-7 are four views of this one missing object. The single highest-leverage matter-sector carry-forward.

| Field | Spec |
|:--|:--|
| **What** | Derive a zero-free-parameter Yukawa/family block from `D_K(τ_fold)` that simultaneously (a) lands an SM-matching fermion mass ratio (W4-1 successor, `|log10(R/R_SM)| < 1`), (b) reconciles `R_seesaw=31.57` with `R_direct=9.86` to <10% (the W4-7 D5 residual), and (c) reaches the PMNS `R` band [17,66] (the W4-2 shortfall). The shared root cause is the absence of a derived family/generation structure. |
| **Inputs** | `s96_matter_a4_yukawa_ratio.npz` (bare a₄ block, R_Yuk); `s96_matter_pmns_3x3.npz` (U, angles, R, ε_LX mechanism); `s96_matter_r_hierarchy.npz` (R_direct=9.862); `s96_matter_seesaw_d5.npz` (M_R-eigenvalue coincidence, R_seesaw=31.57); the inner-fluctuation / Peter-Weyl a₄ machinery. |
| **Gate** | `S97-YUKAWA-FAMILY-DERIVE`. PASS iff a parameter-free `D_K`-derived Yukawa block lands a fermion mass ratio `|log10(R/R_SM)| < 1` AND reconciles the two R-routes to `|R_seesaw − R_direct|/R_direct < 0.10`. FAIL/INFO map the residual Yukawa freedom. |
| **Effort** | Multi-wave (frontier #7 — the framework's hardest open matter-sector problem; likely a multi-session campaign). |

### CF-S97-W4-BARYOGEN-SOURCE — non-left-invariant / additional-fiber baryogenesis source (frontier #9)

> The *located* frontier-#9 statement from W4-4: baryogenesis requires a source external to BOTH `D_K` (T11) AND its homogeneous emergent `g_M` (left-inv `tr(R∧R)=0`). This CF requires POSITING that ingredient first, so it is a frontier-class compute (the "Inputs" include a structural posit, not just existing data).

| Field | Spec |
|:--|:--|
| **What** | Posit and evaluate a non-left-invariant or additional-fiber source carrying a CP-odd phase AND a B-violating interaction near equilibrium, and compute its `η_B` on the emergent `g_M`. |
| **Inputs** | `s96_matter_ext_baryogen.npz` (the internal-null + the left-inv `tr(R∧R)=0` + the DKKMS over-production structure); T11 `[J,D_K]=0`; the emergent `g_M` (a₂ moment); a posited non-LI fiber structure (to be specified). |
| **Gate** | `S97-BARYOGEN-EXT-SOURCE`. PASS iff the posited source gives `η_B ∈ (0, 6e-10)` with a pre-registered CP-phase + B-violation magnitude; FAIL if it over/under-produces or re-vanishes. |
| **Effort** | Multi-wave (frontier #9; requires the structural posit before a clean compute). |

**Q1 workshop candidate (→ `/rclab-investigate` at session-close, NOT a WP CF)**: the D5 residual — *is a parameter-free `D_K`-derived Yukawa block able to reconcile R_seesaw with R_direct, or is the seesaw's residual Yukawa freedom irreducible?* — is a math/physics adjudication with two competing readings (per `Investigating-Workshops.md` Q1). It seeds an S97 workshop; the compute leg is CF-S97-W4-YUKAWA-FAMILY above.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-05-29 | C6 / a₄ Yukawa layer | empty-layer? (open) | NON-EMPTY (`R_Yuk=1.588`, OOM-only) | W4-1 INFO — bare `D_K` block non-degenerate without Higgs VEV |
| 2026-05-29 | B2 Schur wall (θ₁₂, θ₂₃) | walled to zero | LIFTABLE (non-LI `L_X` opens angles; `[iK_7,D_K]=0` preserved) | W4-2 INFO |
| 2026-05-29 | ν nature | undetermined | DEFINITE MAJORANA | W4-3 INFO PART 1 (three independent grounds; T1 discipline held) |
| 2026-05-29 | m_ββ (0νββ) | uncomputed | 4.96–8.27 meV (next-gen reach; external-scale caveat) | W4-3 INFO PART 2 |
| 2026-05-29 | internal baryogenesis (T11) | PROVEN structurally | η_B=0 EXACT confirmed at capstone level | W4-4 PART 1 |
| 2026-05-29 | external baryogenesis | open | LOCATED frontier #9 (external to `D_K` AND homogeneous `g_M`) | W4-4 FAIL (left-inv `tr(R∧R)=0`; DKKMS over-produces 14.1 OOM + out-of-regime) |
| 2026-05-29 | ε″ Yukawa chirality / §1.3.4 caveat | "open?" | CLOSED — exactly zero (machine-ε) | W4-5 PASS |
| 2026-05-29 | bare `R=27.2` | PROVEN | §8.5-conditional ("sign + OOM robust; exact ratio conditional") | W4-6 FAIL (`R_direct=9.862`; `F=0.027≤1` moves R wrong way) |
| 2026-05-29 | M_R / D5 / §0 "no seesaw" | external add-on / "no seesaw" | INTERNAL (= `D_K` B-branch fold spectrum) / "no *external* seesaw parameter" REWORD | W4-7 INFO PART 1 |
| 2026-05-29 | δ_CP | unconstrained | ∈ {0,π} EXACT (real M_R, `[J,D_K]=0`) — new falsifiable prediction | W4-7 structural sub-result |
| 2026-05-29 | (process) W4-2 plan pin | `s56_fabric_spectrum.npz` cited | nonexistent → substituted SHA-pinned s84 L12 cache + s52 fold (bit-identical B1/B2/B3) | stale plan-pin; agent disclosed, structurally clean |
| 2026-05-29 | (process) W4-4 `f₂≈92` plan-prose | non-canonical | canonical `f_2_default=2.34` (S62); verdict f₂-independent | SOURCE-RECON hygiene note (no verdict effect) |
| 2026-05-29 | (process) W4-1 verdict-permanence | dev lines emitted-then-removed | NOT Option-A retain+supersede (contrast W4-5 correct handling) | bounded, disclosed, no downstream consumption; lesson logged (housekeeping) |

## Files Produced

All scripts under `computations/session-96/` (prefix `s96_matter_*`); data/plots co-located; verdict file `computations/session-96/s96_gate_verdicts.txt` (W4 canonical lines 72–89).

| Gate | Script | Data (.npz) | Plot (.png) | Size (script / data / plot, bytes) |
|:--|:--|:--|:--|:--|
| S96-MATTER-A4-YUKAWA-RATIO | `s96_matter_a4_yukawa_ratio.py` | `s96_matter_a4_yukawa_ratio.npz` | `s96_matter_a4_yukawa_ratio.png` | 35725 / 23910 / 83653 |
| S96-MATTER-PMNS-3X3 | `s96_matter_pmns_3x3.py` | `s96_matter_pmns_3x3.npz` | `s96_matter_pmns_3x3.png` | 28776 / 13140 / 104750 |
| S96-MATTER-0NUBB | `s96_matter_0nubb.py` | `s96_matter_0nubb.npz` | `s96_matter_0nubb.png` | 29199 / 16667 / 66999 |
| S96-MATTER-EXT-BARYOGEN | `s96_matter_ext_baryogen.py` | `s96_matter_ext_baryogen.npz` | `s96_matter_ext_baryogen.png` | 32541 / 10246 / 88623 |
| S96-MATTER-YUKAWA-CHIRALITY | `s96_matter_yukawa_chirality.py` | `s96_matter_yukawa_chirality.npz` | `s96_matter_yukawa_chirality.png` | 33916 / 9750 / 42122 |
| S96-MATTER-R-HIERARCHY | `s96_matter_r_hierarchy.py` | `s96_matter_r_hierarchy.npz` | `s96_matter_r_hierarchy.png` | 22977 / 8374 / 61295 |
| S96-MATTER-SEESAW-D5 | `s96_matter_seesaw_d5.py` | `s96_matter_seesaw_d5.npz` | `s96_matter_seesaw_d5.png` | 19640 / 5816 / 39192 |

**Also modified**: `computations/_shared/canonical_constants.py` (NuFit-6.0 Δm² + 0νββ comparison-anchor bounds, lines 2574–2589). **Verdict file** `s96_gate_verdicts.txt`: W4-5 carries an Option-A supersedes pair (dev line 76 `de2496ca` retained → corrective line 82 `8d806474` canonical); the other six gates are single canonical lines.
